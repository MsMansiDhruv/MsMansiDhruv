from __future__ import annotations

from datetime import date, timedelta
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
import re


USERNAME = "MsMansiDhruv"
OUT = Path("assets/contributions.svg")


class ContributionParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.values: dict[date, int] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "td":
            return
        data = dict(attrs)
        raw_date = data.get("data-date")
        raw_level = data.get("data-level")
        if not raw_date or raw_level is None:
            return
        try:
            self.values[date.fromisoformat(raw_date)] = int(raw_level)
        except ValueError:
            pass


def fetch_levels() -> dict[date, int]:
    url = f"https://github.com/users/{USERNAME}/contributions"
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as response:
        html = response.read().decode("utf-8", errors="ignore")
    parser = ContributionParser()
    parser.feed(html)
    if not parser.values:
        raise RuntimeError("Could not parse GitHub contribution calendar")
    return parser.values


def build_svg(levels: dict[date, int]) -> str:
    end = date.today()
    start = end - timedelta(days=370)
    start -= timedelta(days=start.weekday())
    weeks = 53
    cell = 16
    gap = 4
    left = 74
    top = 58
    width = left + weeks * (cell + gap) + 30
    height = 190

    colors = ["#E8E4DA", "#D6E4F8", "#A8C4EE", "#5E8EDB", "#2E63D7"]
    rects = []
    for idx in range(weeks * 7):
        d = start + timedelta(days=idx)
        col = idx // 7
        row = d.weekday()
        x = left + col * (cell + gap)
        y = top + row * (cell + gap)
        level = max(0, min(4, levels.get(d, 0) + 0))
        delay = (col * 7 + row) * 12
        rects.append(
            f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="{colors[level]}" opacity=".82">'
            f'<animate attributeName="opacity" values=".45;.95;.45" dur="4.8s" begin="-{delay}ms" repeatCount="indefinite"/>'
            f'</rect>'
        )

    labels = [
        '<text x="74" y="24" class="m">GITHUB ACTIVITY / 370 DAYS</text>',
        '<text x="74" y="46" class="s">real contribution data · regenerated daily</text>',
        '<text x="74" y="181" class="m">LESS</text>',
        f'<text x="{width-58}" y="181" class="m">MORE</text>',
    ]
    for i, color in enumerate(colors):
        x = width - 152 + i * 23
        labels.append(f'<rect x="{x}" y="168" width="16" height="16" rx="4" fill="{color}"/>')

    scan = (
        f'<rect x="{left}" y="{top}" width="3" height="{7*(cell+gap)-4}" '
        f'fill="#E8762E" opacity=".8"><animate attributeName="x" values="{left};{left + (weeks-1)*(cell+gap)};{left}" dur="8s" repeatCount="indefinite"/></rect>'
    )

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
<style>
.bg{{fill:#F7F4EC}}.m{{font:12px "DejaVu Sans Mono",monospace;fill:#73787D;letter-spacing:2px}}.s{{font:13px "DejaVu Sans Mono",monospace;fill:#60666B}}
</style>
<rect width="{width}" height="{height}" rx="26" class="bg"/>
{''.join(labels)}
{''.join(rects)}
{scan}
</svg>
"""


def main() -> None:
    levels = fetch_levels()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(build_svg(levels), encoding="utf-8")


if __name__ == "__main__":
    main()
