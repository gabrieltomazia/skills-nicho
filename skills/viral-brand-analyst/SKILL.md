---
name: viral-brand-analyst
description: Social-content intelligence in two modes. DESCOBERTA finds what is actually working in a niche now — formats, hooks, sounds, gaps and ranked ideas read off real platforms, not listicles about virality. TEARDOWN reverse-engineers why one post blew up or flopped — baseline math, hook autopsy, timestamped beat map, visual and sound grammar, a replicability verdict, and concepts ready to build. Reads pasted posts, URLs, Chrome, or connected IG/TikTok/YouTube metrics; delivers an HTML report in PT-BR. Use whenever the user asks what is trending, what to post, for viral ideas, hooks or content research; asks why something went viral or died; wants a teardown, breakdown, engenharia reversa, desconstrução or análise of a reel, TikTok, Short, carousel or post; says "o que tá bombando", "ideias de conteúdo", "por que esse vídeo viralizou", "analisa esse perfil", "desconstrói esse reel"; or drops a link to content and wants the same for their brand. Feeds content-script-writer, which turns its concepts into filmable scripts.
---

# Viral Brand Analyst

Two jobs, one discipline. **DESCOBERTA** finds what is working. **TEARDOWN** explains why one thing worked. They chain: discover a format, then tear down its best example before building.

Instructions here are in English; **everything the user reads — the report, the briefs, the hooks — is in PT-BR.**

## Pick the mode

- A **niche, topic, industry or audience** ("o que tá bombando pra dev tools", "ideias de conteúdo pra SaaS B2B") → **DESCOBERTA**.
- A **specific post, video, profile or link** ("por que esse reel deu 2M", "analisa @fulano") → **TEARDOWN**.
- Both, when the user wants to find a format *and* learn to execute it. Run DESCOBERTA, name the strongest example found, then TEARDOWN that example. This is the highest-value path and worth proposing when the request is open-ended.

If genuinely ambiguous, ask in one line rather than guessing — the two modes gather completely different material, and starting down the wrong one wastes the whole run.

## The failure mode both modes exist to prevent

Most "what's viral" work is astrology. It notices a big post has a bold hook and fast cuts and concludes bold hooks and fast cuts cause virality — but the account's *other* posts also have bold hooks and fast cuts and got 12k views. The analysis explained nothing and the playbook it produced is noise.

Worse, the research version of this failure is invisible. Searching `"viral fitness content 2026"` returns SEO listicles written by content marketers who also never watched the videos. Summarizing those produces a report that *looks* like research and contains no observation of anything. **A trend you have not seen on a platform is a rumor.** Cite posts, not think-pieces about posts.

Three disciplines keep both modes honest:

**Baseline before praise.** A number means nothing without the account's own median. 400k views is a miracle for an account that normally does 8k and a disappointment for one that normally does 900k. Every performance claim is a claim about a *multiple over baseline*.

**Attribution before prescription.** Reach comes from somewhere — a collab, a repost by a bigger account, a news moment, paid spend, an algorithm test. If the lift was distributional and you prescribe "copy the hook," the user builds the wrong thing and blames themselves when it does 8k.

**Recency is a hard constraint.** Formats decay in weeks and sounds in days. A trend report with no dates is undated milk. Every finding carries when it was observed, and anything older than ~60 days is labeled as such or dropped.

Say "não deu pra verificar" when you cannot verify. A report that honestly marks three findings as unconfirmed is worth more than one that confidently invents nine.

---

# MODO DESCOBERTA

Find what is working in a niche right now, and turn it into things worth making.

## D1 — Define the territory

If the project has a `perfil.md`, read it first — it usually answers this step. Otherwise pull from the user, or infer and confirm: the niche, who the content is for, the platform(s) that matter, and the brand's own constraints (faceless or on-camera? PT-BR? product to demo?). A trend the user cannot execute is not an opportunity.

Name 5–15 **reference accounts** — the ones actually producing in this space. Ask the user for the accounts they already watch; they usually have a list and it is better than anything you would assemble cold. Fill the gaps yourself, and deliberately include one or two adjacent-niche accounts, because formats usually arrive in a niche from outside it.

## D2 — Read the platforms, not the listicles

Read `references/data-acquisition.md` — the Chrome route is the primary one for this mode, because it is the only one that sees live content.

The evidence hierarchy, best to worst:

1. **Posts you actually read** on-platform, with visible engagement numbers. This is the only source that supports a claim about what is working.
2. **The user's own analytics** — screenshots or exports from Instagram/TikTok/YouTube insights, or a connected analytics tool if they have one. The real numbers for their account, ideal for "what already works for *you*".
3. **Practitioner discussion** — Reddit, niche communities, creator commentary. Good for *why* something works and for spotting a format early. Weak as proof that it works.
4. **Trend/marketing articles** — useful only for vocabulary and leads to chase. Never a finding on their own.

Work down the hierarchy, not up. If you end a run having only touched levels 3 and 4, say so plainly at the top of the report and label everything as unverified leads. That is a legitimate outcome when platform access fails; passing it off as research is not.

**When Chrome is unavailable, reach for `scripts/grid_harvest.py` before falling back to articles.** Instagram and TikTok hard-block unauthenticated reads, but YouTube ships a channel's Shorts grid as JSON in the page, view counts included — so one platform still gives you level-1 evidence with no login. The script takes handles and returns, per channel, the median view count and every video's multiple over it:

```bash
python scripts/grid_harvest.py @canal1 @canal2 --json out.json
```


For **long-form** (a channel's /videos grid, with per-video age and duration), use the sibling `scripts/videos_harvest.py` the same way — it prints only videos from the last 14 days, ranked by multiple over the channel median. On Windows, prefix with `PYTHONIOENCODING=utf-8` (bash) or set `$env:PYTHONIOENCODING='utf-8'` first (PowerShell). The scripts use only the Python standard library. If `python` is not found, try `python3` or `py`, and if none exists tell the user Python is missing instead of grinding.

Videos far above their own channel's median are the ones worth opening; that ranking is the whole point, and it is the same baseline math as Step T2. Carry its caveats into the report rather than burying them: Shorts is a **proxy** for Reels and TikTok (discovery and retention differ), grid titles are packaging and not spoken hooks, and the grid carries no per-post dates, so recency cannot be established from it.

Sweep for: the top-performing posts across the reference accounts (the grid view gives you a dozen view counts in one read); repeated hook constructions; format conventions; sounds appearing across multiple accounts; and comment sections, which are where audience language and unanswered questions live.

## D3 — Separate the trend from the noise

A real pattern shows up **across accounts, not just across one account's feed**. One creator posting the same format nine times is that creator's format, not a trend. Require at least three independent accounts before calling something a pattern, and say how many you saw.

Sort what you found:

- **Ascendente** — appearing in more accounts recently, still uncrowded. The opportunity band. Say what makes you think it is rising.
- **Saturado** — everywhere, engagement flattening. Entering now means competing on production value against people who started earlier.
- **Decaindo** — was everywhere, now fading. Skip, and say so, so the user does not chase it from a listicle later.
- **Nichado** — works in this niche specifically, for a reason worth naming.

For sounds, treat anything over ~2–3 weeks old as late. For formats, the window is more like 2–3 months.

## D4 — Find the gaps

The gaps are more valuable than the trends, and harder, so give this real thought rather than filling the section.

Three places they hide:

- **Questions the comments keep asking that nobody answers in a post.** Read comment sections specifically for this — it is the highest-yield gap-finding activity there is.
- **Formats that work in an adjacent niche and have not crossed over.** Name the source niche and why it should travel.
- **Consensus nobody has argued with.** A well-argued contrarian take on something the whole niche repeats is a reliable engagement mechanism — but only if the user can actually defend it. Do not hand someone a fight they do not believe in.

State each gap as an observation plus the evidence, not as a hole you assume exists because you did not see it filled. Absence of evidence gets labeled as such.

## D5 — The report

Findings, then things to make. Read `references/artifact-spec.md` for structure and visual system.

**Hooks are examples, never swipe copy.** A list of fill-in-the-blank formulas ("Eu parei de fazer X e Y aconteceu") is exactly the generic slop this skill exists to fight — and every account in the niche already ran that formula. So: quote the real hooks you observed verbatim, with their source and their numbers, then explain *what the construction is doing* (opening a loop, staking a claim, naming an enemy, promising a payoff). The transferable thing is the mechanism, not the sentence. Then write hooks in the user's own voice that use the mechanism, and say which mechanism each one is using.

Ideas are specific enough to film or build: subject, angle, format, hook line, and how it gets produced (camera, screen + voiceover, motion graphics, carousel). "Faz um vídeo sobre produtividade" is not an idea.

---

# MODO TEARDOWN

Reverse-engineer one piece of content and hand back something buildable.

## T1 — Get the material

Read `references/data-acquisition.md`. Do not proceed on a URL you never opened — guessing a video's content from its slug produces a confident, fabricated, useless report. If a route fails (login wall, rate limit, dead link), say so and ask the user to paste what they see.

Decide the unit: a **single post** (deepest, still needs the account baseline), an **account pattern** across 10–30 posts (where the most transferable insight lives — what separates the top decile from the median), or a **format across accounts** (answers whether it travels or only works for them).

## T2 — Baseline math

Collect view/like/comment counts for 10–20 recent posts. Take the **median, not the mean** — one outlier drags a mean into uselessness, which is precisely the situation you are in. Compute the target's multiple over it.

- **under 2×** — normal variance. Not a viral post; a good post. Analyze it as such and say so.
- **2–5×** — a real outlier, and the most useful band to study because the mechanism is still legible.
- **5–20×** — broke containment. Usually one dominant mechanism plus algorithmic amplification.
- **over 20×** — almost always has a distributional component. Look hard for the repost, collab, news hook or ad spend before crediting craft.

When view counts are hidden, use comments as a proxy and say in the report that you did.

Ratios carry as much signal as counts. High **comment-to-like** means the post provoked argument or questions. High **share- or save-to-like** means it was useful, or identity-expressing enough that people wanted to be seen passing it on. Different mechanisms, different playbooks — a post people argue about and a post people save are not the same product.

## T3 — Attribution

For each candidate mechanism ask: would this have worked from a cold account with no audience?

Check before crediting content: a repost/stitch/duet/quote by a larger account (the tell is a flood of "vim pelo @fulano" comments); a collab byline; a news cycle or a sound at its peak; a "Patrocinado" label or bought-looking engagement (high views, near-zero comments); a re-upload of something that already worked.

Classify the lift — **content-earned**, **distribution-assisted**, **distribution-driven**, or **unverifiable** — and put that label near the top of the report, not buried at the end. It governs how much weight everything else carries.

## T4 — The teardown

Read `references/teardown-framework.md` for the full diagnostic (hook autopsy, beat map, visual grammar, sound, caption and comment engineering). In `references/platform-grammar.md`, read **only the section for the platform in question** plus the cross-platform notes — it has a table of contents, so do not load the whole file. Judging a LinkedIn post by TikTok norms produces nonsense, but reading about LinkedIn to analyze a Reel just burns context.

Two habits matter more than length:

**Timestamp everything.** "Cortes rápidos" is an observation nobody can act on. "Cortes a cada 0,8s dos 0:00 aos 0:04, depois um plano de 3,2s no 0:05 — a queda de ritmo marca a virada" is a specification.

**Quote verbatim.** The first hook line, the caption's opening sentence, the pinned comment — reproduce them exactly, in the original language. If the hook was "para de fazer isso" and you write "the hook creates urgency," you deleted the evidence and kept the horoscope.

## T5 — Replicability verdict

The section that makes the report useful rather than merely interesting. Label each mechanism:

- **Replicável** — transfers as-is. State the execution cost (an afternoon? a shoot? a developer?).
- **Condicional** — needs a precondition. Name it: "funciona se você tiver um produto que dá pra mostrar funcionando em 3 segundos."
- **Não replicável** — depends on something the user does not have and cannot get: the creator's face and existing parasocial relationship, a news moment, a controversy, a budget, a founder's personal story.

Be blunt in that last column. The commonest way this report fails is handing someone a playbook whose real first step is "be a person with 400k followers." Saying it plainly saves them a month.

## T6 — The playbook

**Transferable rules** — 4 to 7, stated as constraints, grounded in what you observed. Not "use strong hooks." Something like: "abra com o resultado já acontecendo na tela, nunca com o setup — nos 5 posts do decil superior o produto aparece funcionando antes do segundo 2; nos 5 da mediana, depois do 8."

**Three concepts, ready to build** — each with the hook line in PT-BR verbatim as it would be spoken or shown, the beat structure with durations, the visual treatment, and how it gets produced. These get handed straight to `content-script-writer`, so write at that resolution; a concept the user must redesign before building is a suggestion, not a concept.

Ground each in a specific mechanism from the teardown. A concept that traces back to nothing you found is an idea you had, not an analysis you did — mark it as such or cut it.

---

## Publishing the report

Both modes end in an HTML report. Read `references/artifact-spec.md` for section structure, the visual system, and where the file goes — it covers both the case where an Artifact tool is available and the case where it is not.

Title after the subject, not the genre: `Teardown @nomedamarca`, `O que tá funcionando em dev tools`, `Por que o reel dos 2M funcionou` — never `Análise de Conteúdo Viral`.

**Size is a quality constraint, not a budget note.** A teardown of one post is a page someone reads on a phone in three minutes — roughly 900–1400 words, and the beat map plus the three concepts should be a good chunk of it. Length here is not thoroughness; it is usually padding, and padding is where invented benchmark ranges and restated observations come from. Every section must survive the question *what does the reader do differently because of this?* If a section only demonstrates that you analyzed carefully, cut it. Prefer one sharp finding with its evidence to four hedged ones. A report that is half the length and drops nothing the user would act on is strictly the better report.

## Evidence discipline

The fastest way to make this skill worthless is to invent a number, and it happens quietly: a view count that was never on screen, an engagement rate computed from an assumed follower count, a "search volume" for a social keyword — which is not a thing that exists and cannot be looked up. If a number has no source, it does not go in the report.

- Every metric is **observed** (you saw it) or **stated by the user**. Nothing is estimated silently; when you estimate, write "estimativa" and say what it is based on.
- **Industry benchmark ranges are the sneakiest fabrication.** Writing "a faixa típica é 4–6%" from memory, then using it to conclude the post was exceptional, smuggles an invented number into the load-bearing position of the whole verdict — and a footnote does not fix it, because the reader already used it. Either cite where the range comes from, or drop it and compare against the account's own median, which you actually have. The median is better evidence anyway.
- Retention curves, watch time and reach breakdowns are invisible for accounts that are not the user's. Infer structure from the edit and label it inference.
- When working from a description rather than the video, say so at the top. The user will read it differently, and correctly.
- Date every observation. Counts and follower numbers drift.

Mark uncertainty inline, next to the claim — not in a bottom-of-page disclaimer nobody reads.

## Reference files

- `references/data-acquisition.md` — the four intake routes, the evidence hierarchy, and their mechanics
- `references/teardown-framework.md` — the full diagnostic: hook, beats, visual, sound, caption
- `references/platform-grammar.md` — per-platform norms, benchmarks, format conventions
- `references/artifact-spec.md` — report structure for both modes, and the visual system
