"""Turn markdown task lists into real, tickable checkboxes.

Write plain markdown in the content files:

    - [ ] Something to check

and this renders as:

    <ul class="checklist">
    <li><label class="checkbox"><input type="checkbox"> <span>...</span></label></li>
    </ul>

Styling lives in `theme/static/css/custom.css` under "Checklist".
"""

import re

from pelican import signals

TASK_MARKER = '<li>[ ]'

LIST = re.compile(r'<ul>.*?</ul>', re.DOTALL)
ITEM = re.compile(r'<li>\[ \]\s*(.*?)\s*</li>', re.DOTALL)


def _item(match):
    return ('<li><label class="checkbox"><input type="checkbox"> '
            f'<span>{match.group(1)}</span></label></li>')


def _list(match):
    html = match.group(0)
    if TASK_MARKER not in html:
        return html
    return ITEM.sub(_item, html).replace('<ul>', '<ul class="checklist">', 1)


def render_checklists(instance):
    html = instance._content
    if html and TASK_MARKER in html:
        instance._content = LIST.sub(_list, html)


def register():
    signals.content_object_init.connect(render_checklists)
