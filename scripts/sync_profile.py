import json
import os
import re
import urllib.request
from pathlib import Path

GITHUB_USER = "MsMansiDhruv"
PORTFOLIO_URL = "https://portfolio-mansi-eight.vercel.app"
README_PATH = Path(__file__).resolve().parent.parent / "README.md"


def gh_get(url: str) -> dict | list:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "MsMansiDhruv-Profile-Sync",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_upstream_prs(limit: int = 8, max_per_repo: int = 2) -> str:
    query = urllib.request.quote(f"is:pr author:{GITHUB_USER} -user:{GITHUB_USER} is:public")
    url = f"https://api.github.com/search/issues?q={query}&sort=updated&order=desc&per_page=40"
    data = gh_get(url)
    items = data.get("items", [])

    rows = []
    seen = set()
    repo_counts: dict[str, int] = {}
    for item in items:
        html_url = item["html_url"]
        # Parse owner/repo from https://github.com/OWNER/REPO/pull/NUM
        parts = html_url.split("/")
        if len(parts) < 7:
            continue
        repo_full = f"{parts[3]}/{parts[4]}"
        pr_num = parts[6]
        if (repo_full, pr_num) in seen:
            continue
        if repo_counts.get(repo_full, 0) >= max_per_repo:
            continue
        seen.add((repo_full, pr_num))
        repo_counts[repo_full] = repo_counts.get(repo_full, 0) + 1

        title = item["title"].replace("|", "\\|").strip()
        if len(title) > 78:
            title = title[:75].rstrip() + "..."

        pr_meta = item.get("pull_request", {})
        if pr_meta.get("merged_at"):
            status = "Merged"
        elif item["state"] == "open":
            status = "Open (In Review)"
        else:
            status = "Closed"

        updated = item["updated_at"][:10]
        rows.append(
            f"| **{repo_full}** | [#{pr_num}]({html_url}) | {title} | {status} · {updated} |"
        )
        if len(rows) >= limit:
            break

    header = (
        "| Engine / Repository | Pull Request | Technical Scope | Status |\n"
        "| :--- | :---: | :--- | :--- |\n"
    )
    return header + "\n".join(rows)


def fetch_architecture_notes(limit: int = 4) -> str:
    # Fetch documented case studies from portfolio_mansi/lib/data/projects.js
    url = f"https://raw.githubusercontent.com/{GITHUB_USER}/portfolio_mansi/main/lib/data/projects.js"
    req = urllib.request.Request(url, headers={"User-Agent": "MsMansiDhruv-Profile-Sync"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        js_src = resp.read().decode("utf-8")

    # Extract pinned or recent project blocks
    pattern = re.compile(
        r'slug:\s*"([^"]+)".*?title:\s*"([^"]+)".*?desc:\s*"([^"]+)".*?date:\s*"([^"]+)"',
        re.DOTALL,
    )
    matches = pattern.findall(js_src)
    lines = []
    for slug, title, desc, date in matches[:limit]:
        lines.append(
            f"- **[{title}]({PORTFOLIO_URL}/projects/{slug})** (`{date}`) — {desc}"
        )

    # Also check content/posts for non-example markdown posts
    try:
        posts = gh_get(f"https://api.github.com/repos/{GITHUB_USER}/portfolio_mansi/contents/content/posts")
        for p in posts:
            name = p.get("name", "")
            if name.endswith(".md") and name != "example.md":
                slug = name[:-3]
                pretty = slug.replace("-", " ").title()
                lines.insert(0, f"- **[{pretty}]({PORTFOLIO_URL}/blog/{slug})** — Architecture Note")
    except Exception:
        pass

    return "\n".join(lines[:limit])


def replace_block(text: str, marker: str, new_body: str) -> str:
    start_tag = f"<!-- {marker}:START -->"
    end_tag = f"<!-- {marker}:END -->"
    pattern = re.compile(
        re.escape(start_tag) + r".*?" + re.escape(end_tag),
        re.DOTALL,
    )
    replacement = f"{start_tag}\n{new_body}\n{end_tag}"
    if not pattern.search(text):
        raise RuntimeError(f"Marker {marker} not found in README.md")
    return pattern.sub(replacement, text)


def main() -> None:
    readme = README_PATH.read_text(encoding="utf-8")
    prs_md = fetch_upstream_prs()
    notes_md = fetch_architecture_notes()

    updated = replace_block(readme, "OSS_PRS", prs_md)
    updated = replace_block(updated, "ARCH_NOTES", notes_md)

    if updated != readme:
        README_PATH.write_text(updated, encoding="utf-8")
        print("README.md updated with live OSS PRs and Architecture Notes.")
    else:
        print("README.md already up to date.")


if __name__ == "__main__":
    main()
