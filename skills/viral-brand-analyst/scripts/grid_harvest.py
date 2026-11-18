#!/usr/bin/env python3
"""Harvest YouTube Shorts grids: per-channel median views and per-video multiples.

Why this exists: the Chrome route is the best way to read live content, but it is
often unavailable (extension disconnected, no display, running as a subagent).
Instagram and TikTok both hard-block unauthenticated reads. YouTube does not --
a channel's /shorts grid ships its data as JSON inside the HTML, including view
counts. That makes it the one platform where "grid first" works with no login,
which is enough to compute the baseline math the skill depends on.

Read the caveats before using the output:
  - YouTube Shorts is a PROXY for Reels/TikTok, not a substitute. Discovery and
    retention differ. Say so in any report built on this.
  - Grid titles are not spoken hooks. You get the packaging, not the first line.
  - The grid gives no per-post dates, so recency cannot be established here.

Usage:
    python grid_harvest.py @handle1 @handle2 ...
    python grid_harvest.py --file handles.txt --json out.json --min-videos 8

Output: per channel, the median view count and every video's multiple over it,
sorted by multiple. Videos far above their channel's own median are the ones
worth opening -- that is the whole point.
"""

import argparse
import json
import re
import statistics
import sys
import urllib.error
import urllib.request

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122.0 Safari/537.36"
)


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
    })
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")


def extract_initial_data(html):
    """Pull the ytInitialData JSON blob out of the page HTML."""
    m = re.search(r"var ytInitialData\s*=\s*(\{.*?\});</script>", html, re.S)
    if not m:
        m = re.search(r'ytInitialData"\]\s*=\s*(\{.*?\});</script>', html, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return None


# The Shorts grid packs title and view count into one accessibility string, e.g.
#   "The Wildest Camera Robot, 3,9 milhões de visualizações - ver o Shorts"
#   "Some title, 847 mil visualizações"
#   "Some title, 1.2M views"
# so both fields come out of a single regex rather than separate renderer keys.
_ACC_RE = re.compile(
    r"^(?P<title>.+?),\s*(?P<num>[\d.,]+)\s*"
    r"(?P<unit>milhões|milhão|bilhões|bilhão|mil|mi|bi|K|M|B|k|m|b)?\s*"
    r"(?:de\s+)?(?:visualiza|views?|watch)",
    re.I,
)

_MULT = {
    "mil": 1e3, "k": 1e3,
    "milhão": 1e6, "milhões": 1e6, "mi": 1e6, "m": 1e6,
    "bilhão": 1e9, "bilhões": 1e9, "bi": 1e9, "b": 1e9,
}


def parse_accessibility(text):
    """'<title>, 3,9 milhões de visualizações ...' -> (title, 3900000)."""
    if not text:
        return None, None
    m = _ACC_RE.match(text.replace("\xa0", " ").strip())
    if not m:
        return None, None
    num, unit = m.group("num"), m.group("unit")
    if unit:
        # Abbreviated counts carry a decimal separator: ',' in pt-BR, '.' in en.
        num = num.replace(".", ",")
        parts = num.split(",")
        num = parts[0] + ("." + parts[1] if len(parts) > 1 else "")
        try:
            val = float(num)
        except ValueError:
            return None, None
        return m.group("title").strip(), int(val * _MULT[unit.lower()])
    digits = re.sub(r"[.,\s]", "", num)
    if not digits.isdigit():
        return None, None
    return m.group("title").strip(), int(digits)


def walk(node, out):
    """Recursively collect every shortsLockupViewModel entry in the page data."""
    if isinstance(node, dict):
        lock = node.get("shortsLockupViewModel")
        if isinstance(lock, dict):
            title, views = parse_accessibility(lock.get("accessibilityText", ""))
            if title and views is not None:
                vid = None
                ep = lock.get("onTap", {}).get("innertubeCommand", {})
                if isinstance(ep, dict):
                    vid = ep.get("reelWatchEndpoint", {}).get("videoId")
                out.append({"title": title, "views": views, "video_id": vid})
        for v in node.values():
            walk(v, out)
    elif isinstance(node, list):
        for v in node:
            walk(v, out)


def harvest(handle, min_videos=6):
    h = handle if handle.startswith("@") else "@" + handle
    url = "https://www.youtube.com/%s/shorts" % h
    try:
        html = fetch(url)
    except (urllib.error.URLError, urllib.error.HTTPError, OSError) as e:
        return {"handle": h, "error": "fetch failed: %s" % e, "videos": []}
    data = extract_initial_data(html)
    if data is None:
        return {"handle": h, "error": "no ytInitialData (layout changed or blocked)", "videos": []}

    found = []
    walk(data, found)
    # Dedupe by video_id, else by title.
    seen, vids = set(), []
    for v in found:
        key = v["video_id"] or v["title"]
        if key in seen:
            continue
        seen.add(key)
        vids.append(v)

    if len(vids) < min_videos:
        return {"handle": h, "error": "only %d videos found (need >=%d for a usable median)"
                % (len(vids), min_videos), "videos": vids}

    counts = [v["views"] for v in vids]
    median = statistics.median(counts)
    for v in vids:
        v["multiple"] = round(v["views"] / median, 1) if median else None
    vids.sort(key=lambda v: v["views"], reverse=True)
    return {
        "handle": h, "error": None, "video_count": len(vids),
        "median_views": int(median), "max_views": max(counts), "min_views": min(counts),
        "videos": vids,
    }


def main():
    # Windows consoles default to cp1252 and titles are full of non-Latin-1
    # characters, so printing one crashes the whole run mid-harvest.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")

    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("handles", nargs="*", help="channel handles, e.g. @canal")
    ap.add_argument("--file", help="file with one handle per line")
    ap.add_argument("--json", help="write full results to this JSON path")
    ap.add_argument("--min-videos", type=int, default=6,
                    help="minimum videos before a median is considered usable (default 6)")
    ap.add_argument("--top", type=int, default=5, help="how many outliers to print per channel")
    args = ap.parse_args()

    handles = list(args.handles)
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            handles += [ln.strip() for ln in f if ln.strip() and not ln.startswith("#")]
    if not handles:
        ap.error("give at least one handle, or --file")

    results = []
    for h in handles:
        r = harvest(h, args.min_videos)
        results.append(r)
        if r["error"]:
            print("[!] %-24s %s" % (r["handle"], r["error"]), file=sys.stderr)
            continue
        print("\n%s  -- %d shorts, mediana %s views"
              % (r["handle"], r["video_count"], "{:,}".format(r["median_views"]).replace(",", ".")))
        for v in r["videos"][:args.top]:
            print("   %6.1fx  %10s  %s"
                  % (v["multiple"], "{:,}".format(v["views"]).replace(",", "."), v["title"][:70]))

    ok = [r for r in results if not r["error"]]
    print("\n%d/%d canais lidos." % (len(ok), len(results)), file=sys.stderr)
    if ok:
        print("Lembre: Shorts e proxy de Reels/TikTok. Titulo de grade nao e o gancho falado. "
              "Sem data por post.", file=sys.stderr)

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print("JSON -> %s" % args.json, file=sys.stderr)


if __name__ == "__main__":
    main()
