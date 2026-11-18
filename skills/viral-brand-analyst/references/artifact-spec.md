# Report spec

Both modes end in an HTML report, in PT-BR.

## Where the report goes

- **If an `Artifact` tool is available in this session**, publish it there (and load the `artifact-design` skill first if it is listed — the artifact system requires it). The user gets a private link they can open on the phone.
- **Otherwise**, write a single self-contained HTML file (all CSS inline, no external scripts) to a `relatorios/` folder in the current project, named after the subject — e.g. `relatorios/teardown-nomedamarca.html` — and tell the user the path and that it opens in any browser by double-clicking. Never fail the run because there is no Artifact tool.

Either way, this report in particular lives or dies on whether evidence is scannable — someone should be able to skim it in 40 seconds and find the one thing they need in another 20.

## The reading contract

The person opening this report has one question: *what do I do differently?* Everything else is support for that answer. So the structure is inverted — the verdict comes first, the evidence follows, the method never appears. Nobody wants to read about your process.

Two failure shapes to avoid:

**The wall.** Dense paragraphs of analysis with the actionable part buried in the middle. If a finding is important, it gets its own heading and its own evidence line, not a clause in paragraph four.

**The dashboard.** Big numbers in cards with no interpretation. A metric without a comparison is decoration. Every number in this report appears next to its baseline or next to the thing it should be compared to; a lone "2,4M visualizações" tells the reader nothing they did not already know.

---

## Structure — MODO TEARDOWN

Section titles in PT-BR. Adapt them to the subject rather than pasting them literally; a heading that names the actual finding beats a generic label every time.

1. **Veredito** — three to four sentences at the top, before anything else. What happened, why, and whether it is copyable. Include the attribution label (content-earned / distribution-assisted / distribution-driven / unverifiable) and the multiple over baseline. Someone who reads only this section should still have gotten their money's worth.

2. **Os números** — the target post's metrics beside the account's median, so the multiple is visible rather than asserted. Include the engagement ratios (comment/like, save/like, share/like) when observed, because they are what distinguish an argument from a resource. Mark every unobserved figure explicitly.

3. **O gancho** — the hook, verbatim, treated as the evidence it is: set the quoted line in large type as a pull-quote, then the analysis beneath it. Include the first frame description and the timing.

4. **Mapa de batidas** — the timestamped beat table. This is the densest and most-referenced part of the report; give it room and keep it horizontally scrollable on mobile.

5. **Gramática visual e som** — the systems, described concretely. Screenshots or frame descriptions where they help.

6. **Legenda e comentários** — caption verbatim, the pinned comment, and 3–5 real comments quoted with attribution of what they reveal.

7. **O que dá pra copiar** — the replicability verdict, as three visually distinct groups: Replicável / Condicional / Não replicável. Make the third group as prominent as the first. Its whole value is that people skip it.

8. **As regras** — the 4–7 transferable constraints, each with the observation that grounds it.

9. **Três conceitos** — the ready-to-build concepts. Hook line in PT-BR set large and verbatim, beat structure with durations, visual treatment, and the build skill it routes to. These are the handoff; make them the most physically prominent blocks on the page after the verdict, because they are what the user will come back for.

10. **O que não deu pra ver** — a short, honest list of what you could not observe. Keep it brief and specific. This section buys credibility for everything above it.

## Structure — MODO DESCOBERTA

1. **O que fazer agora** — the top three moves, up front, before any research is shown.

2. **O que tá subindo** — the ascending formats, each with: what it is, how many independent accounts you saw doing it, real examples with handles and numbers, and why you think it is rising rather than peaking.

3. **O que já saturou** — what to skip, and why. Short. Saves the user from a listicle they will read next week.

4. **Ganchos que estão funcionando** — real observed hooks, quoted verbatim with source and numbers, each labeled with the mechanism it uses (abre um loop / crava uma posição / nomeia um inimigo / promete um resultado). Then hooks written in the user's voice using those mechanisms, each tagged with which mechanism it borrows. Never a list of fill-in-the-blank formulas — those are swipe-file slop, and everyone in the niche has already run them.

5. **Sons** — only if relevant to the platform, and always with the date observed and an explicit note that the window is short.

6. **Os buracos** — the content gaps, each stated as an observation plus its evidence. Usually the most valuable section; give it weight.

7. **Ideias** — specific enough to film or build. Subject, angle, format, hook line, and the build skill it routes to.

8. **Como isso foi levantado** — one short paragraph naming the accounts and posts read, the dates, and where evidence was thin. Place it at the bottom. It exists so the reader can calibrate trust, not to show work.

---

## Visual system

The house style is editorial, not dashboard: **off-white paper, black type as the protagonist, a single coral accent, generous negative space.** No neon, no glow, no gradient meshes, no glassmorphism, no dark-tech aesthetic. The report should read like a well-set printed brief.

Token skeleton — define the full light palette on bare `:root`, then redefine only what changes in the two dark blocks, as the artifact rules require:

```css
:root {
  --paper: #faf8f5;
  --ink: #14110f;
  --ink-soft: #5a534d;
  --rule: #e0d9d0;
  --coral: #e2553d;
  --card: #ffffff;
}
:root:not([data-theme="light"]) { }   /* @media (prefers-color-scheme: dark) */
:root[data-theme="dark"] { }
```

In dark mode invert to a warm near-black ground with an off-white ink — do not simply darken the coral; desaturate it slightly so it stays readable without glowing.

**Typography.** One serious sans (system stack is fine; SF Pro / Inter if loading a face) with a wide weight range. The scale should be aggressive — pull-quotes and hook lines at 2–3rem, body at 1rem or a touch under. Hooks and concept lines are the reason the page exists; set them like headlines, not like quotes inside paragraphs.

**Coral is a scalpel, not a highlighter.** It marks the verdict, the multiple over baseline, and the "não replicável" flag. If more than roughly 5% of the page is coral it has stopped meaning anything.

**Evidence formatting.**
- Verbatim quotes get visual distinction from your analysis — different weight or a left rule — so the reader can always tell an observation from an interpretation at a glance. This distinction is the report's core integrity feature; do not let it blur.
- Every metric sits next to its comparison.
- Unverified claims carry a small inline marker (a muted "não verificado" or "estimativa" tag). Inline, next to the claim. Never a footnote.

**Tables** — the beat map especially — go in an `overflow-x: auto` container so the page body never scrolls sideways on a phone. This report gets read on a phone.

**Diagrams.** A retention or rhythm curve is worth drawing when the shape is the finding — load `artifact-diagramming` if you draw one. Do not add a chart to have a chart; three numbers in a row are three numbers, not a visualization.

## Title and favicon

Title after the subject: `Teardown @nomedamarca`, `O que tá funcionando em dev tools`, `Por que o reel dos 2M funcionou`. Never `Análise de Conteúdo Viral` or any other genre label.

Favicon: something specific to the subject rather than a generic chart emoji. Keep it stable across republishes of the same report.

## After publishing

Give the user the link (or the file path) plus a two-line summary of the single most important finding — do not restate the report in the terminal. If a concept is ready to build, offer to turn it into a script with `content-script-writer`.
