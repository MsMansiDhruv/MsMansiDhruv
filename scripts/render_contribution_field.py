from __future__ import annotations
import datetime as dt
import os
import requests
from bs4 import BeautifulSoup

USER = os.environ.get("GITHUB_USERNAME", "MsMansiDhruv")
OUT = "assets/contribution-field.svg"
URL = f"https://github.com/users/{USER}/contributions"
LEVELS = ["#0C1917", "#103026", "#145C47", "#1B9B73", "#39E3AA"]

html_text = requests.get(URL, headers={"User-Agent": "profile-art-refresh/1.0"}, timeout=30).text
soup = BeautifulSoup(html_text, "html.parser")
cells = {}
for el in soup.select("[data-date]"):
    d = el.get("data-date")
    lvl = el.get("data-level")
    if d and lvl is not None:
        try:
            cells[d] = max(0, min(4, int(lvl)))
        except ValueError:
            pass
if not cells:
    raise SystemExit("No GitHub contribution cells found")

dates = sorted(cells)
start = dt.date.fromisoformat(dates[0])
rects = []
for d in dates:
    day = dt.date.fromisoformat(d)
    offset = (day - start).days + start.weekday()
    col, row = offset // 7, day.weekday()
    x = 60 + col * 19
    y = 122 + row * 20
    rects.append(f'<rect x="{x}" y="{y}" width="13" height="13" rx="3" fill="{LEVELS[cells[d]]}"/>')

svg = [
'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="430" viewBox="0 0 1600 430">',
'<rect width="1600" height="430" rx="28" fill="#06100E"/>',
'<rect x="1" y="1" width="1598" height="428" rx="27" fill="none" stroke="#17352F"/>',
'<text x="50" y="56" font-family="ui-monospace,monospace" font-size="14" fill="#2EE6A7">Mansi@GitHub:~$ ./contributions.sh</text>',
'<text x="50" y="88" font-family="Inter,Arial,sans-serif" font-size="28" font-weight="700" fill="#EAF4F0">Contribution Field</text>',
'<text x="50" y="111" font-family="Inter,Arial,sans-serif" font-size="15" fill="#91A8A2">GitHub Activity · Updated By GitHub Actions</text>',
*rects,
'<text x="1110" y="150" font-family="ui-monospace,monospace" font-size="12" fill="#2EE6A7">SIGNALS</text>',
'<text x="1110" y="181" font-family="Inter,Arial,sans-serif" font-size="19" font-weight="700" fill="#EAF4F0">Consistency Over Decoration</text>',
'<text x="1110" y="217" font-family="Inter,Arial,sans-serif" font-size="14" fill="#91A8A2">Commit · Review · Iterate</text>',
'<text x="1110" y="254" font-family="Inter,Arial,sans-serif" font-size="19" font-weight="700" fill="#EAF4F0">Systems Work, Not Noise</text>',
'<rect x="0" y="0" width="4" height="430" fill="#2EE6A7" opacity=".10"/>',
'</svg>'
]
open(OUT, "w", encoding="utf-8").write("".join(svg))
