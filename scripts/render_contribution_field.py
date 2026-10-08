from __future__ import annotations
import datetime as dt
import os
import requests
from bs4 import BeautifulSoup

USER = os.environ.get("GITHUB_USERNAME", "MsMansiDhruv")
OUT = "assets/contribution-field.svg"
URL = f"https://github.com/users/{USER}/contributions"
LEVELS = ["#0C1917", "#103026", "#145C47", "#1B9B73", "#39E3AA"]

response = requests.get(URL, headers={"User-Agent": "profile-art-refresh/1.0"}, timeout=30)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

cells = {}
for node in soup.select("[data-date]"):
    date = node.get("data-date")
    level = node.get("data-level")
    if date and level is not None:
        try:
            cells[date] = max(0, min(4, int(level)))
        except ValueError:
            pass

if not cells:
    raise SystemExit("No GitHub contribution cells found")

dates = sorted(cells)
start = dt.date.fromisoformat(dates[0])
distribution = [0, 0, 0, 0, 0]
rects = []

for date_text in dates:
    day = dt.date.fromisoformat(date_text)
    level = cells[date_text]
    distribution[level] += 1
    offset = (day - start).days + start.weekday()
    col, row = offset // 7, day.weekday()
    rects.append(
        f'<rect x="{60 + col * 20}" y="{126 + row * 21}" width="14" height="14" rx="3" fill="{LEVELS[level]}"/>'
    )

max_count = max(distribution[1:]) or 1
bars = []
for level in range(1, 5):
    count = distribution[level]
    width = 220 * count / max_count
    y = 169 + (level - 1) * 38
    bars.append(
        f'<text x="1080" y="{182 + (level - 1) * 38}" class="m mt" font-size="11">L{level}</text>'
        f'<rect x="1110" y="{y}" width="{width:.1f}" height="17" rx="4" fill="{LEVELS[level]}"/>'
        f'<text x="{1120 + width:.1f}" y="{182 + (level - 1) * 38)}" class="m t" font-size="11">{count}</text>'
    )

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="430" viewBox="0 0 1600 430">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#06100E"/><stop offset="1" stop-color="#071614"/></linearGradient>
<style>.s{{font-family:Inter,Segoe UI,Arial,sans-serif}}.m{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}.t{{fill:#EAF4F0}}.mt{{fill:#91A8A2}}.gt{{fill:#2EE6A7}}@keyframes scan{{0%{{transform:translateX(-900px);opacity:0}}25%{{opacity:.4}}75%{{opacity:.4}}100%{{transform:translateX(900px);opacity:0}}}}</style></defs>
<rect width="1600" height="430" rx="28" fill="url(#bg)"/><rect x="1" y="1" width="1598" height="428" rx="27" fill="none" stroke="#17352F"/>
<text x="50" y="56" class="m gt" font-size="14">Mansi@GitHub:~$ ./contributions.sh</text>
<text x="50" y="88" class="s t" font-size="28" font-weight="700">Contribution Field</text>
<text x="50" y="111" class="s mt" font-size="14">The GitHub Grid, Rebuilt As A Systems Heatmap</text>
<g>{''.join(rects)}</g>
<text x="58" y="118" class="m mt" font-size="9">MON</text><text x="58" y="275" class="m mt" font-size="9">SUN</text>
<text x="1080" y="146" class="m gt" font-size="11">ACTIVITY DENSITY</text>
{''.join(bars)}
<line x1="1080" y1="329" x2="1510" y2="329" stroke="#17352F"/>
<text x="1080" y="354" class="s t" font-size="17" font-weight="700">Patterns Matter More Than A Counter</text>
<text x="1080" y="378" class="s mt" font-size="13">A visual record of when the work compounds.</text>
<rect x="0" y="0" width="5" height="430" fill="#2EE6A7" opacity=".10" style="animation:scan 8s linear infinite"/>
</svg>'''
with open(OUT, "w", encoding="utf-8") as file:
    file.write(svg)
