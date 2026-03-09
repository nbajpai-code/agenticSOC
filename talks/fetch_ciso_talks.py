import os
import re
from datetime import datetime, timezone, timedelta
import pytz
from youtubesearchpython import VideosSearch

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

ONE_YEAR_AGO = datetime.now(timezone.utc) - timedelta(days=365)

OUTPUT_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "CISO_TALKS.md")

# Row format:
#   | Title | Channel | Duration | Views | Watch | Fetched |
# The "Fetched" column stores an ISO-8601 date so we can filter by age.
ROW_RE = re.compile(
    r"^\|\s*(?P<title>.+?)\s*\|\s*(?P<channel>.+?)\s*\|\s*(?P<duration>.+?)\s*\|"
    r"\s*(?P<views>.+?)\s*\|\s*\[Link\]\((?P<link>https?://[^\)]+)\)\s*\|"
    r"\s*(?P<fetched>\d{4}-\d{2}-\d{2})\s*\|$"
)


def load_existing_talks() -> list[dict]:
    """Parse the existing CISO_TALKS.md and return talks fetched within the last year."""
    if not os.path.exists(OUTPUT_FILE):
        return []

    kept = []
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()
            m = ROW_RE.match(line)
            if not m:
                continue
            fetched_str = m.group("fetched")
            try:
                fetched_dt = datetime.strptime(fetched_str, "%Y-%m-%d").replace(
                    tzinfo=timezone.utc
                )
            except ValueError:
                # Malformed date – keep it to be safe
                fetched_dt = datetime.now(timezone.utc)

            if fetched_dt >= ONE_YEAR_AGO:
                kept.append(
                    {
                        "title": m.group("title"),
                        "link": m.group("link"),
                        "channel": m.group("channel"),
                        "duration": m.group("duration"),
                        "views": m.group("views"),
                        "fetched": fetched_str,
                    }
                )

    print(f"Retained {len(kept)} talk(s) from the existing file (within the last year).")
    return kept


def fetch_new_talks() -> list[dict]:
    """Search YouTube for fresh CISO talks and return them."""
    queries = [
        "CISO Enterprise Security",
        "CISO Panel Discussion Security 2024",
        "Chief Information Security Officer Strategy",
        "CISO future of cybersecurity",
    ]

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    results_list = []
    seen_urls: set[str] = set()

    print("Fetching CISO talks from YouTube...")
    for query in queries:
        print(f"  Searching: {query}")
        try:
            videos_search = VideosSearch(query, limit=10)
            results = videos_search.result()
            if "result" in results:
                for video in results["result"]:
                    link = video["link"]
                    if link not in seen_urls:
                        seen_urls.add(link)
                        results_list.append(
                            {
                                "title": video["title"],
                                "link": link,
                                "channel": video["channel"]["name"],
                                "published": video.get("publishedTime", ""),
                                "duration": video["duration"],
                                "views": video["viewCount"]["short"],
                                "fetched": today,
                            }
                        )
        except Exception as exc:
            print(f"  Error searching for '{query}': {exc}")

    print(f"Found {len(results_list)} new talk(s) from YouTube this run.")
    return results_list


def merge_talks(existing: list[dict], new: list[dict]) -> list[dict]:
    """Merge new talks into the existing list; deduplicate by URL; newest-first."""
    seen: set[str] = set()
    merged: list[dict] = []

    # New talks take priority (they get added first so duplicates are dropped from old list)
    for talk in new:
        if talk["link"] not in seen:
            seen.add(talk["link"])
            merged.append(talk)

    for talk in existing:
        if talk["link"] not in seen:
            seen.add(talk["link"])
            merged.append(talk)

    return merged


def write_markdown(talks: list[dict]) -> None:
    """Write (or re-write) CISO_TALKS.md with the merged talk list."""
    md = "# CISO Enterprise Security Talks\n\n"
    md += f"Last Updated: {datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}\n\n"
    md += (
        "A curated list of recent talks, panels, and discussions featuring CISOs on "
        "enterprise security. Automatically updated weekly. "
        "Talks older than 1 year are automatically pruned.\n\n"
    )

    if not talks:
        md += "No talks found.\n"
    else:
        md += "| Title | Channel | Duration | Views | Watch | Fetched |\n"
        md += "|-------|---------|----------|-------|-------|---------|\n"
        for v in talks:
            title = v["title"].replace("|", "-")
            channel = v["channel"].replace("|", "-")
            md += (
                f"| {title} | {channel} | {v['duration']} | {v['views']} "
                f"| [Link]({v['link']}) | {v['fetched']} |\n"
            )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Successfully wrote {OUTPUT_FILE} with {len(talks)} talk(s) total.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def fetch_talks():
    existing = load_existing_talks()
    new = fetch_new_talks()

    if not new:
        print("No new talks discovered this run – retaining existing talks (up to 1 year old).")

    merged = merge_talks(existing, new)
    write_markdown(merged)


if __name__ == "__main__":
    fetch_talks()
