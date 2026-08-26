"""Render past-edition cards from "::: edition" blocks.

In the content files, each past edition is one block:

    ::: edition
    year: 2026
    image: images/past/2026.jpg
    venue: Technical University of Munich
    location: Munich, Germany
    date: March 23-25
    url: https://satml.org/2026/
    :::

and renders as a clickable card: image on the left, year/venue/location/
date on the right, the whole card linking to `url`. All six fields are
required - a missing one fails the build with an error naming the block.
"""

import re

from pelican import signals

# Written without blank lines, the whole block is one markdown paragraph:
# <p>::: edition\nyear: ...\n...\n:::</p>. Keep it that way in the content
# files - a blank line inside a block leaves the ::: visible on the page,
# which makes the mistake easy to spot.
BLOCK = re.compile(r'<p>:::\s*edition\s*\n(.*?)\s*\n:::\s*</p>', re.DOTALL)

FIELDS = ('year', 'image', 'venue', 'location', 'date', 'url')

# Styled inline on purpose: the whole card - structure and look - lives in
# this one file, no cross-linking into custom.css needed.
CARD = '''<div class="card mb-5" style="position: relative; border-radius: 8px; overflow: hidden;">
  <a href="{url}" style="position: absolute; inset: 0; z-index: 1;"></a>
  <div class="columns is-gapless">
    <div class="column is-one-third">
      <figure class="image is-5by3" style="width: 100%; height: 100%;">
        <img src="/{image}" alt="IEEE SaTML {year}"
             style="object-fit: cover; width: 100%; height: 100%;">
      </figure>
    </div>
    <div class="column">
      <div class="card-content">
        <p class="title is-size-3" style="color: brown;">IEEE SaTML {year}</p>
        <p class="title is-size-3">{venue}</p>
        <p class="subtitle is-size-4">{location}</p>
        <p class="subtitle is-size-4">{date}</p>
      </div>
    </div>
  </div>
</div>'''


def _card(match):
    data = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(':')
        data[key.strip()] = value.strip()
    missing = [f for f in FIELDS if not data.get(f)]
    if missing:
        raise ValueError(
            f"::: edition block ({match.group(1)[:60]!r}...) is missing: {missing}")
    return CARD.format(**data)


def render_editions(instance):
    html = instance._content
    if html and ':::' in html:
        instance._content = BLOCK.sub(_card, html)


def register():
    signals.content_object_init.connect(render_editions)
