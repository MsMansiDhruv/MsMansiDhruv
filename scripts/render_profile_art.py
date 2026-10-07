from __future__ import annotations

from datetime import datetime, date, timedelta, timezone
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
import json
import re

USER = "MsMansiDhruv"
ROOT = Path("assets")
ROOT.mkdir(exist_ok=True)


class Contributions(HTMLParser):
    def __init__(self):
        super().__init__()
        self.values: dict[date, int] = {}

    def handle_starttag(self, tag, attrs):
        if tag != "td":
            return
        d = dict(attrs)
        raw_date = d.get("data-date")
        raw_level = d.get("data-level")
        if raw_date and raw_level is not None:
            try:
                self.values[date.fromisoformat(raw_date)] = int(raw_level)
            except ValueError:
                pass


def fetch(url: str, accept: str = "*/*") -> bytes:
    req = Request(url, headers={"User-Agent": "MansiProfileArt/1.0", "Accept": accept})
    with urlopen(req, timeout=30) as r:
        return r.read()


def render_contributions() -> None:
    parser = Contributions()
    parser.feed(fetch(f"https://github.com/users/{USER}/contributions").decode("utf-8", "ignore"))
    if not parser.values:
        raise RuntimeError("GitHub contribution calendar could not be parsed")

    end = date.today()
    start = end - timedelta(days=370)
    start -= timedelta(days=start.weekday())
    weeks = 53
    cell, gap = 13, 4
    left, top = 54, 55
    width, height = 888, 195
    colors = ["#121A17", "#12302A", "#176052", "#1FA88F", "#2EC4B6"]

    rects = []
    for i in range(weeks * 7):
        d = start + timedelta(days=i)
        col, row = i // 7, i % 7
        x, y = left + col * (cell + gap), top + row * (cell + gap)
        level = max(0, min(4, parser.values.get(d, 0)))
        delay = i * 10
        rects.append(
            f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="{colors[level]}">'
            f'<animate attributeName="opacity" values=".25;1;.25" dur="4.2s" begin="-{delay}ms" repeatCount="indefinite"/>'
            f'</rect>'
        )

    total = sum(v for d, v in parser.values.items() if d >= start and d <= end)
    labels = [
        f'<text x="32" y="24" class="m">mansi@github ~ $ ./contributions.sh</text>',
        f'<text x="{width-34}" y="24" text-anchor="end" class="total">{total} contributions / 370d</text>',
        '<text x="54" y="190" class="m">LESS</text>',
        '<text x="820" y="190" class="m">MORE</text>',
    ]
    for i, c in enumerate(colors):
        labels.append(f'<rect x="{684+i*24}" y="176" width="15" height="15" rx="3" fill="{c}"/>')

    scan = f'<rect x="{left-8}" y="{top-4}" width="2" height="120" fill="#E8762E" opacity=".7"><animate attributeName="x" values="{left-8};{left + (weeks-1)*(cell+gap)};{left-8}" dur="7s" repeatCount="indefinite"/></rect>'

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
<style>.m{{font:12px "DejaVu Sans Mono",monospace;fill:#87A39A;letter-spacing:1px}}.total{{font:700 15px "DejaVu Sans Mono",monospace;fill:#E8EEE9}}</style>
<rect width="{width}" height="{height}" rx="24" fill="#0B100E"/>
<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="23" fill="none" stroke="#2EC4B6" stroke-opacity=".15"/>
{''.join(labels)}
{''.join(rects)}
{scan}
</svg>'''
    (ROOT / "contributions.svg").write_text(svg, encoding="utf-8")


def render_activity() -> None:
    try:
        events = json.loads(fetch(f"https://api.github.com/users/{USER}/events/public", "application/vnd.github+json").decode())
    except Exception:
        events = []

    counts = {"PushEvent": 0, "PullRequestEvent": 0, "IssuesEvent": 0, "IssueCommentEvent": 0, "CreateEvent": 0}
    recent = []
    for e in events:
        et = e.get("type", "")
        if et in counts:
            counts[et] += 1
        repo = e.get("repo", {}).get("name", "")
        if repo and et:
            recent.append((et.replace("Event",""), repo.split("/",1)[-1]))

    recent = recent[:5]
    rows = []
    for i, (etype, repo) in enumerate(recent):
        y = 90 + i * 34
        rows.append(
            f'<circle cx="38" cy="{y-4}" r="5" fill="#E8762E"><animate attributeName="r" values="5;2.8;5" dur="2.4s" begin="-{i*.4}s" repeatCount="indefinite"/></circle>'
            f'<text x="58" y="{y}" class="s">{escape(etype)}</text>'
            f'<text x="230" y="{y}" class="t">{escape(repo[:42])}</text>'
        )

    total = sum(counts.values())
    stat_text = f'public events / recent window: {total}'
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 280">
<style>.bg{{fill:#0B100E}}.m{{font:12px "DejaVu Sans Mono",monospace;fill:#87A39A;letter-spacing:2px}}.s{{font:12px "DejaVu Sans Mono",monospace;fill:#87A39A}}.t{{font:13px "DejaVu Sans Mono",monospace;fill:#E8EEE9}}.n{{font:700 22px Georgia,serif;fill:#2EC4B6}}.bar{{animation:bar 4s ease-in-out infinite}}@keyframes bar{{0%,100%{{width:40}}50%{{width:210}}}}</style>
<rect width="840" height="280" rx="24" class="bg"/>
<rect x=".5" y=".5" width="839" height="279" rx="23" fill="none" stroke="#2EC4B6" stroke-opacity=".15"/>
<text x="30" y="34" class="m">CONTRIBUTION ACTIVITY / RECENT SIGNAL</text>
<text x="30" y="66" class="n">{total}</text><text x="86" y="65" class="s">{escape(stat_text)}</text>
{''.join(rows) if rows else '<text x="30" y="108" class="s">Activity will populate from public GitHub events.</text>'}
<text x="30" y="248" class="m">PUSH · PR · ISSUE · DISCUSSION-ADJACENT WORK</text>
<rect x="30" y="258" width="250" height="3" rx="2" fill="#18332D"/><rect x="30" y="258" width="120" height="3" rx="2" fill="#2EC4B6" class="bar"/>
</svg>'''
    (ROOT / "activity.svg").write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    render_contributions()
    render_activity()
