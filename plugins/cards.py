"""Render generic Markdown cards and group adjacent cards into a grid.

    ::: card
    title: Example title
    subtitle: Optional plain text
    logo: images/workshops/example.png
    website: https://example.org/
    footer: **Contact:** Example name

    Normal Markdown body, including paragraphs, links, and lists.
    :::

Only ``title`` is required; a card without ``website`` shows "Website
coming soon" in its link row instead. Every card shows the conference
logo left of its title; ``logo`` (a path below theme/static/, emitted
root-relative like the edition images) replaces it, ``logo: none``
removes it. Metadata occupies consecutive lines
immediately after the opening fence; a blank line separates it from the
Markdown body.
Fences must be on their own unindented lines. Pelican's existing Markdown
extensions handle fenced code and other Markdown features as usual.

Pages with cards need ``template: plain``: the ``page`` template splits
content at <h2> headings, and card titles are <h2>s, so it would tear the
cards apart. The styling is the STYLE block below, appended to every page
that contains cards (so the whole construct lives in this one file).
"""

import re
from ipaddress import IPv6Address
from urllib.parse import urlsplit
from xml.etree import ElementTree as etree

from markdown.blockprocessors import BlockProcessor
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.util import AtomicString
from pelican import signals


FIELDS = {"title", "subtitle", "logo", "website", "footer"}
DEFAULT_LOGO = "images/logo/satml-logo.svg"

# Appended once to every page that contains cards. Kept here rather than in
# custom.css on purpose, so plugin and look stay together; it cannot be
# inline per element because of the media queries and the subgrid rules.
STYLE = """<style>
.content-card-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.content-card {
  min-width: 0;
  display: flex;
  flex-direction: column;
  padding: 1.5rem 1.5rem 0;
  border: 1px solid #e4e1dd;
  border-top: 3px solid brown;
  border-radius: 2px;
  overflow-wrap: anywhere;
}

.content-card-heading {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-height: 5.5rem;
  margin-bottom: 1.25rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #eeece9;
}

/* The logo sits at the right end of the heading, so title, subtitle and
   body share one left edge. Height-bound only: the width follows the
   logo's aspect ratio. */
.content-card-logo {
  flex: 0 0 auto;
  order: 1;
  margin-left: auto;
  height: 4.5rem;
  width: auto;
}

.content-card-titles {
  flex: 1 1 auto;
  min-width: 0;
}

.content-card-heading h2 {
  margin: 0 0 0.2rem;
  line-height: 1.2;
}

/* Even line lengths instead of a lone word on the second line. */
.content-card-heading h2,
.content .content-card-subtitle {
  text-wrap: balance;
}

.content .content-card-subtitle {
  margin: 0;
  font-size: 1.125rem;
  font-weight: 500;
  line-height: 1.45;
  color: #454545;
}

.content-card-body {
  min-width: 0;
  margin-bottom: 1rem;
}

.content-card-body > :last-child,
.content-card-footer > :last-child {
  margin-bottom: 0;
}

.content-card-footer {
  margin: 0 0 1.25rem;
  padding-top: 0.5rem;
  color: #555;
  font-size: 0.875rem;
  line-height: 1.55;
}

.content-card-footer strong {
  color: inherit;
  font-weight: 500;
}

.content-card-links {
  display: flex;
  align-items: center;
  min-height: 3.5rem;
  margin: auto -1.5rem 0;
  padding: 0.5rem 1.5rem;
  border-top: 1px solid #eeece9;
  font-size: 0.9rem;
}

.content-card-links a {
  display: inline-flex;
  align-items: center;
  min-height: 2.75rem;
  font-weight: 500;
}

.content-card-nolink {
  color: #9a9a9a;
}

.content-card-link-icon {
  display: block;
  flex: 0 0 auto;
  width: 15px;
  height: 15px;
  margin-left: 0.45rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.65;
  stroke-linecap: round;
  stroke-linejoin: round;
}

/* Shared rows align headings, body text, and the tops of the footer blocks.
   Explicit row positions keep optional footer/link sections in their place. */
@supports (grid-template-rows: subgrid) {
  @media (min-width: 761px) {
    .content-card {
      display: grid;
      grid-row: span 4;
      grid-template-rows: subgrid;
      row-gap: 0;
    }

    .content-card-heading { grid-row: 1; }
    .content-card-body { grid-row: 2; }

    .content-card-footer {
      grid-row: 3;
      align-self: start;
    }

    .content-card-links {
      grid-row: 4;
      margin-top: 0;
    }
  }
}

@media (max-width: 760px) {
  .content-card-grid { grid-template-columns: 1fr; }

  .content-card { padding: 1.25rem 1.25rem 0; }
  .content-card-heading { min-height: 0; }
  .content-card-logo { height: 3.5rem; }

  .content-card-links {
    margin: 0 -1.25rem;
    padding-left: 1.25rem;
    padding-right: 1.25rem;
  }
}
</style>"""
OPENING = re.compile(r"^::: card[ \t]*(?:\n|$)")
CLOSING = re.compile(r"^:::[ \t]*$", re.MULTILINE)


def _metadata(text):
    """Return validated metadata and the remaining Markdown body."""
    header, separator, body = text.partition("\n\n")
    values = {}
    for line in header.splitlines():
        key, colon, value = line.partition(":")
        key = key.strip()
        if not colon or key not in FIELDS:
            raise ValueError(f"Card has unknown or malformed metadata: {line!r}")
        if key in values:
            raise ValueError(f"Card has duplicate metadata key: {key!r}")
        values[key] = value.strip()

    if not values.get("title"):
        raise ValueError("Card is missing required title metadata")

    if "website" in values:
        website = values["website"]
        try:
            parsed = urlsplit(website)
            valid = (
                parsed.scheme in {"http", "https"}
                and parsed.hostname
                and not any(character.isspace() or ord(character) < 32
                            or ord(character) == 127 for character in website)
                and not any(character in website for character in '\\"<>')
            )
            # Accessing port also rejects invalid ports and out-of-range values.
            parsed.port
            if parsed.netloc.rsplit("@", 1)[-1].startswith("["):
                IPv6Address(parsed.hostname)
        except ValueError:
            valid = False
        if not valid:
            raise ValueError(
                f"Card {values['title']!r} website must be an absolute http(s) URL: "
                f"{website!r}"
            )

    return values, body if separator else ""


class CardBlockProcessor(BlockProcessor):
    """Consume one fenced card, then let Markdown parse its body and footer."""

    def test(self, parent, block):
        return OPENING.match(block) is not None

    def run(self, parent, blocks):
        opening = OPENING.match(blocks[0])
        parts = [blocks.pop(0)[opening.end():]]
        while True:
            closing = CLOSING.search(parts[-1])
            if closing:
                remainder = parts[-1][closing.end():].lstrip("\n")
                parts[-1] = parts[-1][:closing.start()].rstrip("\n")
                if remainder:
                    blocks.insert(0, remainder)
                break
            if not blocks or OPENING.match(blocks[0]):
                raise ValueError("Card is missing its closing ::: fence")
            parts.append(blocks.pop(0))

        values, body = _metadata("\n\n".join(parts))
        article = etree.SubElement(parent, "article", {"class": "content-card"})
        heading = etree.SubElement(article, "header", {"class": "content-card-heading"})
        logo = values.get("logo", DEFAULT_LOGO)
        if logo != "none":
            etree.SubElement(heading, "img", {
                "class": "content-card-logo",
                "src": "/" + logo.lstrip("/"),
                "alt": "",  # decorative; the title sits right next to it
            })
        titles = etree.SubElement(heading, "div", {"class": "content-card-titles"})
        etree.SubElement(titles, "h2").text = AtomicString(values["title"])
        if values.get("subtitle"):
            etree.SubElement(titles, "p", {"class": "content-card-subtitle"}).text = (
                AtomicString(values["subtitle"])
            )

        content = etree.SubElement(article, "div", {"class": "content-card-body"})
        self.parser.parseChunk(content, body)
        if values.get("footer"):
            footer = etree.SubElement(article, "div", {"class": "content-card-footer"})
            self.parser.parseChunk(footer, values["footer"])
        # The link row is always there, so every card ends the same way;
        # without a website it carries a quiet placeholder instead.
        links = etree.SubElement(article, "div", {"class": "content-card-links"})
        if not values.get("website"):
            note = etree.SubElement(links, "span", {"class": "content-card-nolink"})
            note.text = "Website coming soon"
        else:
            link = etree.SubElement(links, "a", {"href": values["website"]})
            link.text = "Website "
            icon = etree.SubElement(link, "svg", {
                "class": "content-card-link-icon",
                "xmlns": "http://www.w3.org/2000/svg",
                "viewBox": "0 0 24 24",
                "fill": "none",
                "stroke": "currentColor",
                "stroke-width": "2",
                "stroke-linecap": "round",
                "stroke-linejoin": "round",
                "aria-hidden": "true",
                "focusable": "false",
            })
            etree.SubElement(icon, "path", {
                "d": "M14 3h7v7M21 3 10 14M10 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-5",
            })


class CardGridTreeprocessor(Treeprocessor):
    """Wrap each run of adjacent cards without relying on serialized HTML."""

    def run(self, root):
        for parent in list(root.iter()):
            grid = None
            for child in list(parent):
                if child.tag == "article" and child.get("class") == "content-card":
                    if grid is None:
                        grid = etree.Element("div", {"class": "content-card-grid"})
                        parent.insert(list(parent).index(child), grid)
                    parent.remove(child)
                    grid.append(child)
                else:
                    grid = None


class CardExtension(Extension):
    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(CardBlockProcessor(md.parser), "card", 75)
        md.treeprocessors.register(CardGridTreeprocessor(md), "card_grid", 25)


def add_card_extension(pelican):
    """Keep Pelican's configured Markdown extensions and add cards once."""
    settings = pelican.settings.setdefault("MARKDOWN", {})
    extensions = settings.setdefault("extensions", [])
    if not any(isinstance(extension, CardExtension) for extension in extensions):
        extensions.append(CardExtension())


def add_card_style(instance):
    """Append the card styling to pages that actually contain cards."""
    html = instance._content
    if html and 'content-card-grid' in html:
        instance._content = html + STYLE


def register():
    signals.initialized.connect(add_card_extension)
    signals.content_object_init.connect(add_card_style)
