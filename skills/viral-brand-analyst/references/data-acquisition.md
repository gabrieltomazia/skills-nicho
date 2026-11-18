# Data acquisition

Four routes. Pick by what the user handed you and by mode; escalate only when a route comes up short. Every route ends the same way: a set of observed facts you can cite, and an honest note about what you could not see.

**The evidence hierarchy governs everything here.** Posts you actually read on-platform > the user's own analytics > practitioner discussion > trend articles. Work down it, never up. A claim about what is working must rest on the top two levels.

## Route 1 — Pasted content

The user drops post text, captions, screenshots, a transcript, or numbers into the conversation. The most reliable route, because nothing is inferred, and often the fastest — do not push someone toward browser automation when a paste would do.

Ask for these in **one message**, not drip-fed:

1. The post itself — video file, screenshot, or a transcript of what is said and shown.
2. The visible numbers — views, likes, comments, shares, saves, follower count.
3. The caption verbatim and complete, including hashtags and line breaks. Line breaks are a design decision; preserve them.
4. Numbers from 5–10 other recent posts by the same account, for the baseline. Users skip this because it feels tedious, so give the one-line reason: without it you cannot tell a hit from a normal day.
5. Screenshots of the first 3 seconds, if the video itself is not available.

If they send a video file, watch it properly — real cut timings and on-screen text, not an impression of them.

## Route 2 — Web search and fetch

Load with `ToolSearch: select:WebSearch,WebFetch` (both deferred).

Be realistic about what this route can and cannot do.

**It cannot see social content.** Instagram, TikTok and LinkedIn serve a fetcher an OG title and a login wall. Do not dress up an OG description as an analysis of a video. YouTube is the exception — titles, descriptions, view counts and often transcripts are reachable.

**It cannot measure trends.** There is no search volume for a social hook, no ranking of "viral formats", no index of what is working this week. Searching `"viral [niche] 2026"` returns content-marketing listicles written by people who also never watched the videos. Treat anything from that genre as **vocabulary and leads to chase**, never as a finding. If a listicle names an account or a specific post, that is the useful part — go read the account.

Where this route genuinely earns its place:

- **Attribution.** Finding the news cycle a post rode, the larger account that reposted it, the press pickup. Often the single fact that reframes a whole teardown.
- **Brand context.** Who the company is, what they sell, who they sell to, what they have said publicly.
- **Practitioner discussion.** Reddit (`site:reddit.com` plus the niche), creator commentary, community threads. Strong for *why* a format works and for catching one early; weak as proof that it works.
- **YouTube.** The one platform where fetching is actually productive.

## Route 3 — Chrome automation

Requires the **Claude in Chrome** extension, installed and connected, with the user logged in to the platforms in that browser. If the tools below do not load, or `tabs_context_mcp` fails, say once that the extension is not connected, point the user to the setup guide in the README of the repository these skills came from, and fall back to `scripts/grid_harvest.py` (YouTube) and Route 1 (paste). Do not retry in a loop.

The primary route for DESCOBERTA and the strongest one for TEARDOWN, because it is the only way to see live content, real engagement numbers, and comment sections behind a login.

Load in one call:

```
ToolSearch: select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp
```

Call `tabs_context_mcp` first, open a **new** tab rather than hijacking one of theirs, then navigate and read.

Practical notes that save wasted turns:

- **Grid first, posts second.** A profile grid gives you a dozen view counts in one screenshot — that is the entire baseline in a single read. Get it before opening anything individually. For DESCOBERTA, sweeping 10 grids is a fast, high-quality survey.
- **Screenshot the frames.** `computer` screenshots at intervals give you the actual visual grammar. The DOM gives you the caption and tells you nothing about what is on screen.
- **Read comment sections.** For DESCOBERTA they are the best gap-finding surface there is — the questions people keep asking that no post answers. For TEARDOWN they carry the attribution tells ("vim pelo @fulano") and the audience's own language.
- **Read only. Never click anything destructive.** This is the user's real logged-in session: do not follow, like, comment, message, or delete. If an action seems necessary, ask first.
- **Do not trigger dialogs.** A modal blocks the extension entirely and the session goes dead.
- **Stop after 2–3 failures.** Page will not load, selectors will not resolve, rate limited — say what happened and ask the user to paste what they see. Do not grind.

## Route 4 — The user's own analytics

The simplest version, and the one most users have: ask for screenshots of the native insights (Instagram: Painel profissional → Insights; TikTok: Ferramentas de criador → Análises; YouTube: Studio → Análises). Read every number off the screenshot and treat it as observed data for that date.

**If an analytics connector is connected** (for example Windsor.ai — find it with `ToolSearch` using the query `windsor`, and do not assume it exists), it is the one route that pulls these automatically, for accounts the user has actually connected, and the one route that returns **real metrics rather than public vanity numbers** — reach, impressions, saves, shares, watch-through, follower deltas. When the subject is the user's own account, prefer it over everything else.

Sequence: `get_connectors` to see what is actually connected (check, do not assume), `get_fields` for the real field names, then `get_data`. Relevant connectors: `instagram`, `tiktok`, `youtube`, `facebook`, `linkedin`.

Two cautions. These are read tools — `execute_action` writes to the live platform and has no place in an analysis task. And the connector covers only the user's own accounts; a competitor's real reach is not available through it and no amount of querying will change that.

In DESCOBERTA this route answers a question the others cannot: *what already works for you specifically*. A format that is rising in the niche and has already outperformed for this account is the strongest possible recommendation, and it is only visible here.

## When routes conflict

Public view counts and platform-reported reach measure different things and will disagree. Native analytics win. Note the discrepancy rather than silently picking one — the gap is sometimes itself the finding: high public views with low reported reach usually means a small group watched repeatedly, which is a completely different phenomenon from broad distribution.

## Recording what you gathered

Keep a short observation log as you go — source, what you saw, the date you saw it. It becomes the evidence column of the report and it is the thing that stops a plausible-sounding number from drifting into the writeup unsourced. Every observation is a snapshot, not a fact; date it.
