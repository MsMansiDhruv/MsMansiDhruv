from __future__ import annotations

from datetime import date, timedelta
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
import json

USER = "MsMansiDhruv"
ROOT = Path("assets")
ROOT.mkdir(exist_ok=True)


class Contributions(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.values: dict[date, int] = {}

    def handle_starttag(self, tag, attrs) -> None:
        if tag != "td":
            return
        data = dict(attrs)
        raw_date = data.get("data-date")
        raw_level = data.get("data-level")
        if raw_date and raw_level is not None:
            try:
                self.values[date.fromisoformat(raw_date)] = int(raw_level)
            except ValueError:
                pass


def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "MansiProfileArt/1.0"})
    with urlopen(req, timeout=30) as response:
        return response.read()


def render_contributions() -> None:
    parser = Contributions()
    parser.feed(fetch(f"https://github.com/users/{USER}/contributions").decode("utf-8", "ignore"))
    if not parser.values:
        raise RuntimeError("Could not read GitHub contribution calendar")

    end = date.today()
    start = end - timedelta(days=370)
    start -= timedelta(days=start.weekday())
    weeks = 53
    cell, gap = 13, 4
    left, top = 46, 60
    width, height = 960, 225
    colors = ["#101814", "#12332C", "#176052", "#1FA88F", "#2EC4B6"]

    rects = []
    for i in range(weeks * 7):
        d = start + timedelta(days=i)
        col, row = i // 7, i % 7
        x = left + col * (cell + gap)
        y = top + row * (cell + gap)
        level = max(0, min(4, parser.values.get(d, 0)))
        delay = i * 8
        rects.append(
            f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="{colors[level]}" '
            f'style="transform-origin:{x + cell/2}px {y + cell/2}px;animation:pop .5s ease-out both;animation-delay:-{delay}ms"/>'
        )

    total = sum(v for d, v in parser.values.items() if start <= d <= end)
    legend = "".join(
        f'<rect x="{758 + i*23}" y="190" width="15" height="15" rx="3" fill="{c}"/>'
        for i, c in enumerate(colors)
    )
    scan = (
        f'<rect x="{left-7}" y="{top-4}" width="2" height="110" fill="#E8762E" opacity=".8">'
        f'<animate attributeName="x" values="{left-7};{left+(weeks-1)*(cell+gap)};{left-7}" dur="8s" repeatCount="indefinite"/>'
        f'</rect>'
    )
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
<style>
.bg{{fill:#0B100E}}.m{{font:12px "DejaVu Sans Mono",monospace;fill:#8AA299;letter-spacing:1.5px}}
.n{{font:700 15px "DejaVu Sans Mono",monospace;fill:#E8EEE9}}
@keyframes pop{{0%{{opacity:0;transform:scale(.18)}}65%{{opacity:1;transform:scale(1.08)}}100%{{opacity:1;transform:scale(1)}}}}
@media(prefers-reduced-motion:reduce){{rect{{animation:none!important}}}}
</style>
<rect width="{width}" height="{height}" rx="26" class="bg"/>
<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="25" fill="none" stroke="#2EC4B6" stroke-opacity=".16"/>
<text x="34" y="30" class="m">mansi@github ~ $ ./contributions.sh</text>
<text x="925" y="30" text-anchor="end" class="n">{total} contributions / 370d</text>
<text x="46" y="48" class="m">LESS</text><text x="858" y="48" class="m">MORE</text>
<g>{''.join(rects)}</g>{scan}
{legend}
<text x="34" y="214" class="m">REAL GITHUB DATA · AUTO-REFRESHED · NO CONTRIBUTION PADDING</text>
</svg>'''
    (ROOT / "contrib-heatmap.svg").write_text(svg, encoding="utf-8")


def render_activity() -> None:
    try:
        events = json.loads(fetch(f"https://api.github.com/users/{USER}/events/public").decode("utf-8", "ignore"))
    except Exception:
        events = []

    recent = []
    for event in events:
        kind = event.get("type", "")
        repo = event.get("repo", {}).get("name", "")
        if repo and kind in {"PushEvent", "PullRequestEvent", "IssuesEvent", "CreateEvent", "IssueCommentEvent"}:
            recent.append((kind.replace("Event", ""), repo.split("/", 1)[-1]))
        if len(recent) >= 5:
            break

    rows = []
    for i, (kind, repo) in enumerate(recent):
        y = 106 + i * 34
        rows.append(
            f'<circle cx="52" cy="{y-5}" r="5" fill="#E8762E">'
            f'<animate attributeName="r" values="5;2.5;5" dur="2.4s" begin="-{i*.35}s" repeatCount="indefinite"/></circle>'
            f'<text x="76" y="{y}" class="t">{escape(kind)}</text>'
            f'<text x="245" y="{y}" class="t">{escape(repo[:48])}</text>'
        )

    if not rows:
        rows.append(
            '<circle cx="52" cy="106" r="5" fill="#E8762E"/>'
            '<text x="76" y="111" class="t">no recent public events</text>'
            '<text x="76" y="133" class="s">the feed will populate automatically as public work lands</text>'
        )

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 300">
<style>
.bg{{fill:#0B100E}}.m{{font:12px "DejaVu Sans Mono",monospace;fill:#8AA299;letter-spacing:1.5px}}
.t{{font:13px "DejaVu Sans Mono",monospace;fill:#E8EEE9}}.s{{font:12px "DejaVu Sans Mono",monospace;fill:#71837A}}
</style>
<rect width="960" height="300" rx="26" class="bg"/><rect x=".5" y=".5" width="959" height="299" rx="25" fill="none" stroke="#2EC4B6" stroke-opacity=".16"/>
<text x="34" y="34" class="m">mansi@github ~ $ ./activity.sh</text>
<text x="34" y="62" class="s">recent public work · generated from GitHub events</text>
<line x1="52" y1="88" x2="52" y2="268" stroke="#2EC4B6" stroke-opacity=".18" stroke-width="2"/>
{''.join(rows)}
<text x="34" y="286" class="m">PUSH · PR · ISSUE · CREATE · COMMENT</text>
</svg>'''
    (ROOT / "activity.svg").write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    render_contributions()
    render_activity()
