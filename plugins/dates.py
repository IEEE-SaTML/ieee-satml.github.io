"""Render conference dates from single-source markers.

Two constructs, usually used together:

1. An ISO date marker renders as the bold prose date:

       [[2026-09-29]]                  ->  Tue, Sep 29, 2026
       [[2026-11-25 -- 2026-12-09]]    ->  Wed, Nov 25 - Wed, Dec 9, 2026

2. A list wrapped in "::: dates" / ":::" is marked as a deadline list:

       ::: dates

       - Paper submission deadline: [[2026-09-29]]
           - Anonymized artifact(s) updated by: [[2026-10-02]]

       :::

   It renders wrapped in <div class="dates">. Inside such a block, the
   "Important dates" styling in theme/static/css/custom.css applies, and
   the SCRIPT below (appended automatically to any page containing such a
   block) dims past deadlines and highlights the next upcoming one with
   an "in N days" chip.

"""

import re
from datetime import date

from pelican import signals

MARKER = re.compile(
    r'\[\[\s*(\d{4}-\d{2}-\d{2})(?:\s*--\s*(\d{4}-\d{2}-\d{2}))?\s*\]\]')

BLOCK = re.compile(r'<p>:::\s*dates</p>(.*?)<p>:::</p>', re.DOTALL)

# Appended once to every page that contains a "::: dates" block. Each
# rendered date is checked against its deadline moment, 23:59:59 AoE
# (= UTC-12), so the result is correct in any visitor timezone. Past
# entries dim; each block's next upcoming entry is accented and gets an
# "in N days" chip; undated detail lines follow their parent's status.
SCRIPT = '''<script>
  document.addEventListener('DOMContentLoaded', () => {
    const AOE = 'T23:59:59-12:00';
    const now = new Date();
    const due = el => new Date(el.dataset.due + AOE);
    const end = el => new Date((el.dataset.end || el.dataset.due) + AOE);

    document.querySelectorAll('.dates').forEach(block => {
      const marks = Array.from(block.querySelectorAll('strong[data-due]'));

      marks.forEach(el => {
        if (end(el) < now) el.closest('li')?.classList.add('is-past');
      });

      // Undated detail lines under a past deadline dim with it.
      block.querySelectorAll('li.is-past > ul > li').forEach(li => {
        if (!li.querySelector('strong[data-due]')) li.classList.add('is-past');
      });

      const next = marks
        .filter(el => !el.closest('li')?.classList.contains('is-past'))
        .sort((a, b) => due(a) - due(b))[0];
      if (!next) return;
      next.closest('li')?.classList.add('is-next');

      // Whole AoE calendar days until the (start) date: 0 = that day is
      // "today" everywhere on Earth, negative = it has begun (ranges).
      const aoe = new Date(now.getTime() - 12 * 3600e3);
      const todayAoE = Date.UTC(aoe.getUTCFullYear(), aoe.getUTCMonth(), aoe.getUTCDate());
      const days = (Date.parse(next.dataset.due) - todayAoE) / 864e5;

      const chip = document.createElement('span');
      chip.className = 'due-chip';
      // Ranges: "starts today" on their first day, "in progress" once the
      // start has passed; single-date deadlines count down to their day.
      chip.textContent =
        next.dataset.end && days < 0 ? 'in progress' :
        next.dataset.end && days === 0 ? 'starts today (AoE)' :
        days === 0 ? 'today (AoE)' :
        days === 1 ? 'tomorrow' : `in ${days} days`;
      next.after(chip);
    });
  });
</script>'''


def _fmt(d, with_year=True):
    # Non-breaking spaces: a date never wraps internally. A range can
    # still break at the plain spaces around its dash.
    text = f'{d:%a},&nbsp;{d:%b}&nbsp;{d.day}'
    return f'{text},&nbsp;{d.year}' if with_year else text


def _marker(match):
    start = date.fromisoformat(match.group(1))
    if match.group(2):
        end = date.fromisoformat(match.group(2))
        text = f'{_fmt(start, with_year=start.year != end.year)} &ndash; {_fmt(end)}'
        attrs = f' data-due="{match.group(1)}" data-end="{match.group(2)}"'
    else:
        text = _fmt(start)
        attrs = f' data-due="{match.group(1)}"'
    return f'<strong{attrs}>{text}</strong>'


def render_dates(instance):
    html = instance._content
    if not html:
        return
    if ':::' in html:
        html, wrapped = BLOCK.subn(r'<div class="dates">\1</div>', html)
        if wrapped:
            html += SCRIPT
    if '[[' in html:
        html = MARKER.sub(_marker, html)
    instance._content = html


def register():
    signals.content_object_init.connect(render_dates)
