"""Turn markdown task lists into checkbox-style bullets.

Write plain markdown in the content files:

    - [ ] Something to check

and this renders as:

    <ul class="checklist">
    <li><span class="checkitem"><span class="checkitem-box"></span><span>...</span></span></li>
    </ul>

The box is decorative only: it is not a real <input>, so nothing is clickable.
"""

import re

from pelican import signals

TASK_MARKER = '<li>[ ]'

LIST = re.compile(r'<ul>.*?</ul>', re.DOTALL)
ITEM = re.compile(r'<li>\[ \]\s*(.*?)\s*</li>', re.DOTALL)

STYLE = """<style>
ul.checklist {
  list-style: none !important;
  margin-left: 0.5rem !important;
  margin-top: 0.5rem !important;
}

ul.checklist li {
  margin: 0 0 0.35rem 0 !important;
}

ul.checklist span.checkitem {
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
}

ul.checklist span.checkitem-box {
  flex: 0 0 auto;
  box-sizing: border-box;
  width: 0.8rem;
  height: 0.8rem;
  margin-top: 0.32rem;
  border: 1px solid #b5b5b5;
  border-radius: 2px;
}
</style>"""


def _item(match):
    return ('<li><span class="checkitem"><span class="checkitem-box" aria-hidden="true"></span>'
            f'<span>{match.group(1)}</span></span></li>')


def _list(match):
    html = match.group(0)
    if TASK_MARKER not in html:
        return html
    return ITEM.sub(_item, html).replace('<ul>', '<ul class="checklist">', 1)


def render_checklists(instance):
    html = instance._content
    if html and TASK_MARKER in html:
        html = LIST.sub(_list, html)
        if '<ul class="checklist">' in html:
            html += STYLE
        instance._content = html


def register():
    signals.content_object_init.connect(render_checklists)
