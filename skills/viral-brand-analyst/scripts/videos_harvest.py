"""Harvest a YouTube channel's /videos grid (long-form) from ytInitialData.
Outputs per channel: median views, each video's multiple, published age text.
"""
import json, re, sys, statistics, urllib.request, time

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128 Safari/537.36"

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9",
                                              "Cookie": "CONSENT=YES+1; PREF=hl=en&gl=US"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")

def initial_data(html):
    m = re.search(r"ytInitialData\s*=\s*(\{.*?\});\s*</script>", html, re.S)
    if not m:
        m = re.search(r"ytInitialData\"\]\s*=\s*(\{.*?\});", html, re.S)
    return json.loads(m.group(1)) if m else None

def walk(node, out):
    if isinstance(node, dict):
        if "lockupViewModel" in node:
            lv = node["lockupViewModel"]
            try:
                md = lv["metadata"]["lockupMetadataViewModel"]
                title = md["title"]["content"]
                parts = md["metadata"]["contentMetadataViewModel"]["metadataRows"][0]["metadataParts"]
                texts = [p["text"]["content"] for p in parts if "text" in p]
                vid = lv.get("contentId")
                badges = lv["contentImage"]["thumbnailViewModel"].get("overlays", [{}])[0].get("thumbnailBottomOverlayViewModel", {}).get("badges", [{}])
                length = badges[0].get("thumbnailBadgeViewModel", {}).get("text", "")
                thumb = lv["contentImage"]["thumbnailViewModel"]["image"]["sources"][-1]["url"]
                out.append({"videoId": vid, "title": title, "views_txt": texts[0] if texts else "", "age_txt": texts[1] if len(texts)>1 else "", "length": length, "thumb": thumb})
            except Exception:
                pass
        for v in node.values():
            walk(v, out)
    elif isinstance(node, list):
        for v in node:
            walk(v, out)

def txt(o):
    if not o: return ""
    if "simpleText" in o: return o["simpleText"]
    return "".join(r.get("text", "") for r in o.get("runs", []))

def views_num(s):
    m = re.search(r"([\d,\.]+)\s*([KM]?)", s.replace(",", ""))
    if not m: return None
    n = float(m.group(1)); u = m.group(2)
    return int(n * (1_000_000 if u == "M" else 1_000 if u == "K" else 1))

def age_days(s):
    # YouTube shows either "3 days ago" or the short form "3d ago" / "19h ago" / "2mo ago".
    m = re.search(r"(\d+)\s*(minutes?|min|m(?!o)|hours?|h|days?|d|weeks?|w|months?|mo|years?|y)\b", s)
    if not m: return None
    n, u = int(m.group(1)), m.group(2)
    if u.startswith("mo"): return n*30
    if u.startswith("min") or u == "m" or u.startswith("h"): return 0
    if u.startswith("d"): return n
    if u.startswith("w"): return n*7
    if u.startswith("y"): return n*365
    return None

def harvest(handle):
    html = fetch(f"https://www.youtube.com/{handle}/videos")
    data = initial_data(html)
    vids = []
    if data: walk(data, vids)
    rows = []
    for v in vids:
        # "117K views" or just "117K" depending on the layout YouTube serves
        vc = views_num(v["views_txt"]) if re.search(r"\d", v["views_txt"]) and "ago" not in v["views_txt"] else None
        rows.append({"id": v["videoId"], "title": v["title"], "views": vc, "age": v["age_txt"],
                     "age_days": age_days(v["age_txt"]), "length": v["length"], "thumb": v["thumb"]})
    rows = [r for r in rows if r["views"] is not None]
    med = statistics.median([r["views"] for r in rows]) if rows else 0
    for r in rows:
        r["multiple"] = round(r["views"] / med, 2) if med else None
    return {"handle": handle, "n": len(rows), "median": med, "videos": rows}

if __name__ == "__main__":
    handles = sys.argv[1:]
    out = []
    for h in handles:
        try:
            res = harvest(h); out.append(res)
            print(f"\n{h}  -- {res['n']} videos, mediana {int(res['median']):,}")
            recent = [r for r in res["videos"] if r["age_days"] is not None and r["age_days"] <= 14]
            for r in sorted(recent, key=lambda r: -(r["multiple"] or 0))[:6]:
                print(f"  {r['multiple']:>5}x  {r['views']:>10,}  {r['age']:<12} {r['length']:<8} {r['title'][:80]}  https://youtu.be/{r['id']}")
        except Exception as e:
            print(f"\n{h}  -- ERRO {e}")
        time.sleep(1.0)
    with open("videos_out.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
