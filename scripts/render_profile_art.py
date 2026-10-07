from __future__ import annotations

from datetime import date, timedelta
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
import json
import math

from PIL import Image, ImageDraw, ImageFont

USER = "MsMansiDhruv"
ROOT = Path("assets")
ROOT.mkdir(exist_ok=True)

BG = (9, 13, 11)
PANEL = (15, 23, 19)
FG = (232, 238, 233)
MUTED = (126, 148, 137)
GREEN = (46, 196, 182)
GREEN_D = (18, 51, 44)
GREEN_D2 = (16, 34, 29)
ORANGE = (232, 118, 46)


def mono(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
    return ImageFont.truetype(path, size)


def rounded(draw: ImageDraw.ImageDraw, box, radius=18, fill=PANEL, outline=GREEN):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=1)


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

    W, H = 960, 225
    left, top = 44, 60
    cell, gap = 13, 4
    colors = [BG, (16, 48, 40), (20, 77, 65), (31, 145, 122), GREEN]
    total = sum(v for d, v in parser.values.items() if start <= d <= end)

    frames = []
    cells = []
    for i in range(53 * 7):
        d = start + timedelta(days=i)
        col, row = i // 7, i % 7
        x = left + col * (cell + gap)
        y = top + row * (cell + gap)
        level = max(0, min(4, parser.values.get(d, 0)))
        cells.append((x, y, colors[level], i))

    for frame in range(8):
        img = Image.new("RGB", (W, H), BG)
        draw = ImageDraw.Draw(img)
        rounded(draw, (4, 4, W - 4, H - 4), 24, BG, GREEN)
        draw.text((34, 20), "mansi@github ~ $ ./contributions.sh", font=mono(12), fill=MUTED)
        draw.text((925, 20), f"{total} contributions / 370d", font=mono(12, True), fill=FG, anchor="ra")
        for x, y, color, idx in cells:
            draw.rounded_rectangle((x, y, x + cell, y + cell), radius=3, fill=color)
            if idx <= frame * 53 * 7 // 8:
                draw.rounded_rectangle((x, y, x + cell, y + cell), radius=3, outline=GREEN)
        scan_x = left + (frame / 7) * (52 * (cell + gap))
        draw.rectangle((scan_x, top - 4, scan_x + 2, top + 7 * (cell + gap) - 4), fill=ORANGE)
        draw.text((44, 193), "LESS", font=mono(10), fill=MUTED)
        draw.text((850, 193), "MORE", font=mono(10), fill=MUTED)
        frames.append(img)

    frames[0].save(ROOT / "contrib-heatmap.gif", save_all=True, append_images=frames[1:], duration=150, loop=0, optimize=True)


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

    W, H = 960, 300
    frames = []
    for frame in range(8):
        img = Image.new("RGB", (W, H), BG)
        draw = ImageDraw.Draw(img)
        rounded(draw, (4, 4, W - 4, H - 4), 24, BG, GREEN)
        draw.text((34, 20), "mansi@github ~ $ ./activity.sh", font=mono(12), fill=MUTED)
        draw.text((34, 48), "recent public work · generated from GitHub events", font=mono(10), fill=MUTED)
        draw.line((52, 76, 52, 270), fill=GREEN_D, width=2)

        if recent:
            for i, (kind, repo) in enumerate(recent):
                y = 95 + i * 34
                radius = 5 if (frame + i) % 4 else 8
                draw.ellipse((52 - radius, y - radius, 52 + radius, y + radius), fill=ORANGE if i % 2 == 0 else GREEN)
                draw.text((76, y - 8), kind, font=mono(11), fill=FG)
                draw.text((245, y - 8), repo[:48], font=mono(11), fill=FG)
        else:
            draw.text((76, 92), "no recent public events", font=mono(11), fill=FG)
            draw.text((76, 120), "the activity feed will populate as public work lands", font=mono(10), fill=MUTED)

        draw.text((34, 278), "PUSH · PR · ISSUE · CREATE · COMMENT", font=mono(10), fill=MUTED)
        frames.append(img)

    frames[0].save(ROOT / "activity.gif", save_all=True, append_images=frames[1:], duration=170, loop=0, optimize=True)


def render_whoami() -> None:
    W, H = 780, 360
    frames = []
    rows = [
        ("role", "Lead Data Engineer  ·  Solution Architect"),
        ("build", "AWS  ·  Databricks  ·  Spark  ·  PySpark"),
        ("study", "distributed systems  ·  query execution"),
        ("deep", "performance  ·  memory  ·  I/O  ·  data movement"),
        ("next", "CUDA  ·  RAPIDS  ·  accelerated data systems"),
    ]

    for frame in range(8):
        img = Image.new("RGB", (W, H), BG)
        draw = ImageDraw.Draw(img)
        rounded(draw, (4, 4, W - 4, H - 4), 24, PANEL, GREEN)
        draw.rounded_rectangle((4, 4, W - 4, 34), radius=24, fill=(16, 23, 19))
        draw.ellipse((18, 13, 25, 20), fill=ORANGE)
        draw.ellipse((32, 13, 39, 20), fill=GREEN)
        draw.ellipse((46, 13, 53, 20), fill=(102, 117, 110))
        draw.text((70, 9), "mansi@github ~ $ whoami", font=mono(11), fill=MUTED)

        y = 60
        for key, value in rows:
            draw.text((22, y), key, font=mono(11, True), fill=GREEN)
            draw.text((126, y), value, font=mono(10), fill=FG)
            y += 39

        draw.line((22, 252, 758, 252), fill=GREEN_D, width=1)
        draw.text((22, 270), "engineering rule", font=mono(10), fill=MUTED)
        draw.text((22, 294), "measure first  →  change the right layer  →  measure again", font=mono(11), fill=FG)
        x = 24 + frame * 100
        draw.rectangle((x, 326, x + 2, 350), fill=ORANGE)
        frames.append(img)

    frames[0].save(ROOT / "whoami.gif", save_all=True, append_images=frames[1:], duration=160, loop=0, optimize=True)


def render_achievements() -> None:
    W, H = 780, 360
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    rounded(draw, (4, 4, W - 4, H - 4), 24, PANEL, ORANGE)
    draw.text((22, 24), "ACHIEVEMENTS / SIGNALS WORTH SHOWING", font=mono(11), fill=MUTED)

    cards = [
        (18, 55, 370, 145, "7+ years", "professional data engineering", "experience", GREEN, ORANGE),
        (398, 55, 752, 145, "GEM Award", "recognized engineering impact", "awarded", GREEN, ORANGE),
        (18, 165, 370, 255, "Master's", "graduate technical foundation", "completed", GREEN, ORANGE),
        (398, 165, 752, 255, "Production impact", "performance · cost · reliability", "delivered", GREEN, ORANGE),
    ]
    for x1, y1, x2, y2, head, sub, value, accent, dot in cards:
        rounded(draw, (x1, y1, x2, y2), 16, (16, 24, 20), ORANGE)
        draw.ellipse((x1 + 18, y1 + 18, x1 + 27, y1 + 27), fill=dot)
        draw.text((x1 + 40, y1 + 12), head, font=mono(16, True), fill=FG)
        draw.text((x1 + 18, y1 + 53), sub, font=mono(9), fill=MUTED)
        draw.text((x1 + 18, y1 + 84), value, font=mono(17, True), fill=accent)

    draw.text((22, 285), "production depth first · public work follows the same thread", font=mono(10), fill=MUTED)
    img.save(ROOT / "achievements.png", optimize=True)


def render_architecture() -> None:
    W, H = 960, 300
    stages = [(24, "BRONZE", "INGEST"), (250, "QUALITY", "GUARD"), (476, "SILVER", "SHAPE"), (702, "GOLD", "SERVE")]
    frames = []
    for frame in range(8):
        img = Image.new("RGB", (W, H), BG)
        draw = ImageDraw.Draw(img)
        rounded(draw, (4, 4, W - 4, H - 4), 20, BG, GREEN)
        draw.text((24, 18), "SENTINEL LAKEHOUSE / ARCHITECTURE IN MOTION", font=mono(11), fill=MUTED)
        draw.text((24, 44), "Raw  →  Clean  →  Reliable  →  Useful", font=mono(18, True), fill=FG)

        for x, label, title in stages:
            rounded(draw, (x, 88, x + 202, 168), 14, PANEL, GREEN)
            draw.text((x + 16, 102), label, font=mono(9), fill=MUTED)
            draw.text((x + 16, 126), title, font=mono(18, True), fill=FG)

        for x1, x2 in [(226, 250), (452, 476), (678, 702)]:
            draw.line((x1, 128, x2, 128), fill=GREEN, width=2)
            px = x1 + ((frame * 18) % 24)
            draw.ellipse((px - 4, 124, px + 4, 132), fill=ORANGE)

        rounded(draw, (250, 190, 452, 265), 14, PANEL, ORANGE)
        draw.text((264, 204), "FAILURE PATH", font=mono(9), fill=MUTED)
        draw.text((264, 228), "QUARANTINE", font=mono(15, True), fill=FG)

        rounded(draw, (476, 190, 678, 265), 14, PANEL, GREEN)
        draw.text((490, 204), "OBSERVABILITY", font=mono(9), fill=MUTED)
        draw.text((490, 228), "MEASURE", font=mono(15, True), fill=FG)
        frames.append(img)

    frames[0].save(ROOT / "architecture.gif", save_all=True, append_images=frames[1:], duration=170, loop=0, optimize=True)


def render_trajectory() -> None:
    W, H = 960, 190
    points = [(70, 116), (260, 78), (450, 116), (640, 72), (850, 112)]
    labels = ["DATA", "CLOUD", "SPARK", "SYSTEMS", "GPU"]
    frames = []
    for frame in range(8):
        img = Image.new("RGB", (W, H), BG)
        draw = ImageDraw.Draw(img)
        rounded(draw, (4, 4, W - 4, H - 4), 20, BG, GREEN)
        draw.text((26, 18), "ENGINEERING TRAJECTORY", font=mono(10), fill=MUTED)
        draw.text((26, 43), "Go deeper, not wider.", font=mono(18, True), fill=FG)

        for a, b in zip(points, points[1:]):
            draw.line((a[0], a[1], b[0], b[1]), fill=(82, 108, 97), width=2)

        for i, (x, y) in enumerate(points):
            accent = ORANGE if i in (2, 4) else GREEN
            draw.ellipse((x - 17, y - 17, x + 17, y + 17), fill=PANEL, outline=accent, width=2)
            draw.text((x, y + 24), labels[i], font=mono(9), fill=MUTED, anchor="ma")

        x = 62 + (frame * 112) % 810
        y = 105 + int(7 * math.sin(frame / 1.7))
        draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill=ORANGE)
        draw.text((26, 162), "production systems · Spark · performance · accelerated data systems", font=mono(9), fill=MUTED)
        frames.append(img)

    frames[0].save(ROOT / "trajectory.gif", save_all=True, append_images=frames[1:], duration=180, loop=0, optimize=True)


if __name__ == "__main__":
    render_contributions()
    render_activity()
    render_whoami()
    render_achievements()
    render_architecture()
    render_trajectory()
