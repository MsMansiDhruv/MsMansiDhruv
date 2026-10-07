from __future__ import annotations

from datetime import date, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen

USER = "MsMansiDhruv"
OUT = Path("assets/contributions.svg")

class Contributions(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.values: dict[date, int] = {}

    def handle_starttag(self, tag, attrs) -> None:
        if tag != "td":
            return
        data = dict(attrs)
        d = data.get("data-date")
        level = data.get("data-level")
        if d and level is not None:
            try:
                self.values[date.fromisoformat(d)] = int(level)
            except ValueError:
                pass

def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "MansiProfileArt/1.0"})
    with urlopen(req, timeout=30) as response:
        return response.read()

def render() -> None:
    parser = Contributions()
    parser.feed(fetch(f"https://github.com/users/{USER}/contributions").decode("utf-8", "ignore"))
    if not parser.values:
        raise RuntimeError("Could not read GitHub contribution calendar")

    end = date.today()
    start = end - timedelta(days=370)
    start -= timedelta(days=start.weekday())
    colors = ["#13221D", "#173D33", "#1D7560", "#24A88D", "#2EC4B6"]
    rects: list[str] = []

    for i in range(53 * 7):
        d = start + timedelta(days=i)
        c, r = i // 7, i % 7
        level = max(0, min(4, parser.values.get(d, 0)))
        x, y = 42 + c * 16, 72 + r * 18
        rects.append(
            f'<rect x="{x}" y="{y}" width="12" height="12" rx="3" fill="{colors[level]}"/>'
        )

    total = sum(v for d, v in parser.values.items() if start <= d <= end)

    OUT.write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 390">
<style>
.bg{{fill:#0B100E}}.m{{font:12px monospace;fill:#8AA299;letter-spacing:1.5px}}.n{{font:700 17px monospace;fill:#E8EEE9}}.s{{font:11px monospace;fill:#71847B}}
.scan{{animation:scan 7s linear infinite}}.bar{{animation:bar 3.6s ease-in-out infinite}}
@keyframes scan{{0%{{transform:translateX(0);opacity:0}}12%{{opacity:.7}}88%{{opacity:.7}}100%{{transform:translateX(790px);opacity:0}}}}
@keyframes bar{{0%,100%{{width:280px}}50%{{width:610px}}}}
</style>
<rect width="980" height="390" rx="26" class="bg"/>
<rect x=".5" y=".5" width="979" height="389" rx="25" fill="none" stroke="#2EC4B6" stroke-opacity=".16"/>
<text x="34" y="30" class="m">Mansi@GitHub:~$ ./contributions.sh</text>
<text x="946" y="30" text-anchor="end" class="n">{total} Contributions · Last Year</text>
<text x="34" y="56" class="s">Commit Density Across The Rolling Calendar</text>
<g>{''.join(rects)}<rect x="35" y="68" width="2" height="132" fill="#E8762E" class="scan"/></g>
<text x="38" y="232" class="m">ACTIVITY DENSITY</text>
<rect x="38" y="246" width="820" height="12" rx="6" fill="#13221D"/>
<rect x="38" y="246" width="280" height="12" rx="6" fill="#2EC4B6" class="bar"/>
<text x="38" y="286" class="s">Commits · Pull Requests · Issues · Repository Work</text>
<text x="38" y="322" class="n">The Pattern Matters More Than The Number.</text>
<text x="38" y="347" class="s">This Visual Updates From GitHub Contribution Data.</text>
</svg>''', encoding="utf-8")

if __name__ == "__main__":
    render()
