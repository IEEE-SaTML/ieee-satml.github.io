"""Render a highlighted callout box from a fenced Markdown block.

    ::: callout
    ⚠️ **Short lead sentence.** Normal Markdown body, including links.
    :::

The block becomes ``<div class="callout">`` wrapping the parsed Markdown,
so it can hold more than one paragraph. Fences must be on their own
unindented lines. The styling is the STYLE block below, appended to every
page that contains a callout, so the whole construct lives in this file.
"""

import re
from xml.etree import ElementTree as etree

from markdown.blockprocessors import BlockProcessor
from markdown.extensions import Extension
from pelican import signals


STYLE = """<style>
.callout {
  margin: 1.5rem 0 !important;
  padding: 0.75rem 1rem;
  border: 1px solid #e6dcdc;
  border-left: 3px solid brown;
  border-radius: 4px;
  background: #fbf8f8;
}

.callout > :last-child {
  margin-bottom: 0 !important;
}
</style>"""
OPENING = re.compile(r"^::: callout[ \t]*(?:\n|$)")
CLOSING = re.compile(r"^:::[ \t]*$", re.MULTILINE)


class CalloutBlockProcessor(BlockProcessor):
    """Consume one fenced callout, then let Markdown parse its body."""

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
                raise ValueError("Callout is missing its closing ::: fence")
            parts.append(blocks.pop(0))

        box = etree.SubElement(parent, "div", {"class": "callout"})
        self.parser.parseChunk(box, "\n\n".join(parts))


class CalloutExtension(Extension):
    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(
            CalloutBlockProcessor(md.parser), "callout", 75)


def add_callout_extension(pelican):
    """Keep Pelican's configured Markdown extensions and add callouts once."""
    settings = pelican.settings.setdefault("MARKDOWN", {})
    extensions = settings.setdefault("extensions", [])
    if not any(isinstance(extension, CalloutExtension) for extension in extensions):
        extensions.append(CalloutExtension())


def add_callout_style(instance):
    """Append the callout styling to pages that actually contain one."""
    html = instance._content
    if html and '<div class="callout">' in html:
        instance._content = html + STYLE


def register():
    signals.initialized.connect(add_callout_extension)
    signals.content_object_init.connect(add_callout_style)
