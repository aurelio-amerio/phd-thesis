# Chapter 4 Repetition Reduction + Framing Rebalance — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the verified Chapter 4 repetition report and rebalance the pre-paper narrative (§4.0–4.4) into a neutral "pendulum" arc, with all new text in `\blue{}` and all replaced text `%`-commented.

**Architecture:** Five editing tasks (one per section, body sections first, intro last so its previews match the final body), then a verification task (compile + fresh-context referee). Spec: `docs/superpowers/specs/2026-07-04-chapter4-repetition-rebalance-design.md` — read it before starting any task.

**Tech Stack:** LaTeX (memoir + dinostyle), `latexmk`/`pdflatex`, NotebookLM MCP for fact checks.

## Global Constraints

- **This is a prose-revision plan.** Per the author's standing preference, tasks give structural directives, anchor quotes, and required content points — the implementer drafts the actual sentences, matching the house style in `CLAUDE.md` (long paragraphs, no bullets in narrative prose, calibrated hedging, cross-references as connective tissue).
- Every new or modified sentence is wrapped in `\blue{...}` (defined `macros.tex:58`). `\blue{}` must not span a paragraph break (blank line) and must not contain a `%` character.
- Never delete a sentence being replaced or removed: keep it as a `%`-commented line directly above its replacement (or in place, for pure removals). One `%` per line; comment the full original line(s).
- Locate edit sites by the **anchor quotes** given in each task, not by line number — earlier edits in the same file shift lines.
- Citations: reuse bib keys already present in Chapter 4 (`Buschmann:2020adf`, `Calore_2021`, `manconi2024galacticcenterexcesshighest`, `Fermi-LAT:2015att`, `Leane:2019xiy`, `Leane:2020pfc`, `Macias:2016nev`, `Macias:2019omb`, `Bartels:2017vsx`, `Hooper:2016rap`, `Holst:2024fvb`, `Amerio:2024qor`, `Lee:2015fea`, `List:2025qbx`, `Daylan:2014rsa`, `Calore:2014xka`, `Cirelli:2024ssz`). Never hand-write a new BibTeX entry; if a new key is truly needed, query NotebookLM first and use an `\aure{}` placeholder if unresolvable.
- Do NOT edit anything under `chapter_04/sections/paper_msp/`. Do NOT touch or reference the commented block at the end of `4.4_breaking_the_stalemate.tex` (recycling-history note + email draft, from `\aure{An important comment...}` through the email text).
- Do NOT modify section titles (§4.3.3 "Recent Revival of the Dark Matter Hypothesis" stays). Do not remove existing `\aure{}` / `\red{}` markers.
- Existing labels to use in xrefs: `sec:4.1` … `sec:4.1.4`, `sec:4.2`, `sec:4.2.1`, `sec:4.2.2`, `sec:4.3`, `sec:4.3.1`–`sec:4.3.3`, `sec:4.4`, `sec:msp_paper`, `chap:methods`.
- Compile check command (fast, per task): `pdflatex -interaction=nonstopmode -draftmode main.tex` from repo root; PASS = exit without `!` errors (`grep -c "^!" main.log` → 0). Full `latexmk -pdf` only in Task 6.
- Commit after each task with a one-line message describing the section touched.

---

### Task 1: §4.1 — A3 dedup + §4.1.4 tone-down

**Files:**
- Modify: `chapter_04/sections/4.1_discovery_and_characterization.tex`

**Interfaces:**
- Consumes: nothing (first task).
- Produces: §4.1.3 remains the canonical quantitative statement of GCE properties (xref target `sec:4.1.3` used by §4.3.2 and by Task 1's own edit in §4.1.2). §4.1.4 keeps per-paper values "~30–50 GeV" and "(1–3)×10⁻²⁶" — Task 5's broad intro range (30–70) must bracket these.

- [ ] **Step 1: A3 — trim the §4.1.2 duplicate enumeration.** Anchor: `First, the spectral shape of the excess was remarkably stable: regardless of the adopted diffuse model, it consistently displayed a peak at 1--3~GeV`. Comment the sentence; replace with a `\blue{}` sentence keeping only "spectral shape remarkably stable across all 60 diffuse models" + an xref deferring the quantitative properties (peak, sub-GeV rise, −2.7 tail, factor two–three flux band) to `Section~\ref{sec:4.1.3}`. Keep the following sentence ("Second, when the large correlated uncertainties…") untouched.

- [ ] **Step 2: A3 — de-attribute the §4.1.3 restatement.** Anchor: `Daylan et al.` / `showed that the data strongly disfavor any elongation`. Comment the original two-line construct; replace with a `\blue{}` consensus phrasing (no named re-attribution) stating the same facts — elongation disfavored beyond ~20%, centroid within ~0.05° of Sgr A* — citing `\cite{Daylan:2014rsa}` at the end. All numbers unchanged (this is the canonical statement).

- [ ] **Step 3: §4.1.4 tone-down, three edits.**
  1. Anchor: `This minimal model succeeds on all three fronts.` → comment; `\blue{}` replacement in consistency language (the model is *consistent with* all three observables), not success language.
  2. Anchor: `has made the GCE one of the most compelling indirect detection signals in the literature.` → comment the sentence; `\blue{}` replacement that historicizes: this convergence sustained the dark matter interpretation and kept the GCE a leading candidate signal for over a decade — interest, not verdict.
  3. After the final sentence of the section (anchor: `dwarf spheroidal galaxies place upper limits ... in tension with this interpretation for some channel and mass combinations~\cite{Fermi-LAT:2015att}.`) append one `\blue{}` forward-pointing sentence: consistency is not uniqueness — the same observational properties have also been claimed by fits tracing the stellar bulge (astrophysical origin), `cf.\ Section~\ref{sec:4.2.1}` and `Section~\ref{sec:4.3.2}`.

- [ ] **Step 4: Compile check.** Run: `pdflatex -interaction=nonstopmode -draftmode main.tex`; Expected: no `^!` lines in `main.log`.

- [ ] **Step 5: Diff self-check.** Run `git diff chapter_04/sections/4.1_discovery_and_characterization.tex`; every removed sentence appears as a `%` line, every added sentence is inside `\blue{...}`.

- [ ] **Step 6: Commit.** `git add chapter_04/sections/4.1_discovery_and_characterization.tex && git commit -m "Ch4 §4.1: dedup established properties (A3), tone down DM-consistency superlatives"`

---

### Task 2: §4.2 — A4 trim of the paper preview

**Files:**
- Modify: `chapter_04/sections/4.2_msp_hypothesis.tex`

**Interfaces:**
- Consumes: nothing.
- Produces: §4.2.2's closing pointer to `sec:msp_paper` carries NO dataset numbers (15.8 yr, 157 clusters, "most stringent to date" all removed) — Task 4 relies on §4.4 being the only narrative place with any quantitative preview. The "missing bright pulsars" punchline sentence (anchor: `only if those pulsars are systematically less luminous than any known MSP population`) stays VERBATIM here — Task 4 rewords the §4.4 twin instead.

- [ ] **Step 1: A4 — reduce the final sentence to a bare pointer.** Anchor: `In Section~\ref{sec:msp_paper}, we present a dedicated analysis that updates and extends this line of argument using 15.8 years of Fermi-LAT data and a comprehensive sample of 157 globular clusters, placing one of the most stringent constraints to date on pulsar interpretations of the GCE.` Comment it; `\blue{}` replacement: a one-clause pointer that a dedicated analysis updating and extending this argument is presented in `Section~\ref{sec:msp_paper}` — no dataset numbers, no superlatives. Everything else in §4.2 unchanged (per report: A1 keeps §4.2.1 as primary; line "appeared to decisively favor" stays — it narrates the consensus period and already carries the fragility caveat).

- [ ] **Step 2: Compile check.** Run: `pdflatex -interaction=nonstopmode -draftmode main.tex`; Expected: no `^!` lines.

- [ ] **Step 3: Diff self-check.** `git diff chapter_04/sections/4.2_msp_hypothesis.tex` — original commented, replacement in `\blue{}`.

- [ ] **Step 4: Commit.** `git add chapter_04/sections/4.2_msp_hypothesis.tex && git commit -m "Ch4 §4.2: trim paper preview to bare pointer (A4)"`

---

### Task 3: §4.3 — A1/A2/A7 dedup, Lee source-count reconciliation, §4.3.3 reframe sentence

**Files:**
- Modify: `chapter_04/sections/4.3_systematics_stalemate.tex`
- Modify (only if Step 3 requires): `chapter_04/sections/4.2_msp_hypothesis.tex`

**Interfaces:**
- Consumes: §4.2.1 unchanged as the primary Macias/Bartels treatment (Task 2 left it intact).
- Produces: §4.3 opener remains the single full statement of the systematics triad (diffuse model / Fermi Bubbles / masking / faint-end SCD parameterization); Tasks 4–5 must reference it via `Section~\ref{sec:4.3}` rather than re-enumerate.

- [ ] **Step 1: A1 — condense the §4.3.2 Macias/Bartels recap.** Anchor: `However, a series of analyses beginning with Macias et al.` through `supporting an astrophysical origin tied to the old stellar population of the inner Galaxy.` (two sentences). Comment both; `\blue{}` replacement: ONE sentence stating that the stellar-bulge template analyses introduced in `Section~\ref{sec:4.2.1}` challenged this picture by finding the boxy/X-shaped bulge fits the GCE better than a spherical NFW halo, keeping `\cite{Macias:2016nev,Macias:2019omb}` and `\cite{Bartels:2017vsx}`. Do not re-explain the near-IR method (that lives in §4.2.1).

- [ ] **Step 2: A2 — remove the triad echoes.**
  1. Anchor (§4.3.1 closer): `can be made to appear or vanish depending on the diffuse model, the treatment of spatial asymmetries, and the parameterization of the source-count function at the faint end.` — comment; `\blue{}` reword that avoids the verbatim opener phrase "parameterization of the source-count function at the faint end" (e.g. refer generically to the analysis choices enumerated at the start of this section, keeping "diffuse model" and "spatial asymmetries" since they are the NPTF-specific instances).
  2. Anchor (§4.3.2): `depending on the interstellar emission model adopted, the masking procedure applied to the Galactic plane and known point sources, and how the Fermi Bubbles emission is treated at low latitudes~\cite{Macias:2019omb,Cirelli:2024ssz}.` — comment; `\blue{}` replacement shortening the enumeration to "the diffuse-emission systematics discussed at the opening of this section" (or an explicit `Section~\ref{sec:4.3}` xref), keeping both citations.

- [ ] **Step 3: C-note — reconcile Lee et al. 400 vs 200.** First verify: query NotebookLM (notebook `1b7df790-7858-4fc8-879c-39f41238c4ae`, "thesis references") asking what number of near-threshold point sources Lee et al. (arXiv:1506.05124, `Lee:2015fea`) inferred to account for the GCE, and in what region/flux definition, and how List et al. 2025 (`List:2025qbx`) characterizes the 2016 NPTF's preferred source count (~200?). Then EITHER align both narrative numbers to the verified value(s), OR keep both with an explicit `\blue{}` clause in `4.3_systematics_stalemate.tex` (anchor: `the 2016 NPTF preferred approximately 200`) stating the definitional/region difference. If the fix requires touching `4.2_msp_hypothesis.tex` (anchor: `they estimated that $\sim 400$ near-threshold sources`), same conventions apply there. If NotebookLM is inconclusive, keep both numbers and add an `\aure{}` note flagging the discrepancy for the author.

- [ ] **Step 4: A7 — reword the §4.3.2 closer.** Anchor: `The answer depends on modeling choices for which there is no clear, model-independent criterion to adjudicate.` Comment it; `\blue{}` replacement that adds content instead of echoing the §4.3 opener's thesis: tie forward — this is the impasse that motivates the energy-dependent inference of `Section~\ref{sec:4.3.3}` and the fully independent constraints of `Section~\ref{sec:4.4}`.

- [ ] **Step 5: §4.3.3 reframe sentence.** After the anchor `The remaining 97\% is fully consistent with the smooth emission expected from dark matter.` (or after the following sentence about the 34% shift, whichever reads better), insert one `\blue{}` sentence making explicit: consistency with smooth emission reopens the dark matter hypothesis but does not demonstrate it — the result reignites the question rather than answering it. Title of §4.3.3 unchanged.

- [ ] **Step 6: Compile check.** `pdflatex -interaction=nonstopmode -draftmode main.tex`; Expected: no `^!` lines.

- [ ] **Step 7: Diff self-check.** `git diff chapter_04/sections/` — all originals `%`-commented, all new text `\blue{}`-wrapped.

- [ ] **Step 8: Commit.** `git add chapter_04/sections/4.3_systematics_stalemate.tex chapter_04/sections/4.2_msp_hypothesis.tex && git commit -m "Ch4 §4.3: condense repeated morphology/systematics passages (A1,A2,A7), reconcile Lee source counts, neutral reframe of DM revival"`

---

### Task 4: §4.4 — combined B1+B2+B3 condensation + reframing pass

**Files:**
- Modify: `chapter_04/sections/4.4_breaking_the_stalemate.tex`

**Interfaces:**
- Consumes: §4.3 opener as the triad xref target (`sec:4.3`, Task 3); §4.2.2 punchline kept verbatim (Task 2) — the §4.4 twin must be reworded here.
- Produces: §4.4 ends as the paper's de facto introduction — Task 5's §4.0 paper-framing sentence and roadmap must match the framing produced here ("independent constraint sharpening the tension with the MSP interpretation as formulated so far").

**Section-level target shape** (the section keeps its narrative jobs, loses the paper's numbers): (1) why leave the GC — systematics xref; (2) why globular clusters — one-sentence dynamical-formation/correlates summary + clean-measurement point; (3) the old-age logic — compact, with backref to §4.2.2 instead of re-citations; (4) what we did and found — qualitative only + pointer to the paper; (5) the 17–37-vs-3 implication ONCE, reworded punchline; (6) the List et al. convergence — reframed as sharpening tension, not eliminating motivation.

- [ ] **Step 1: A2 — opener triad → xref.** Anchor: `the results depend sensitively on the adopted interstellar emission model, masking procedure, and treatment of the Fermi Bubbles.` Comment; `\blue{}` replacement referring to "the diffuse-emission systematics discussed in Section~\ref{sec:4.3}" (a one-clause recap is fine — the opener legitimately motivates leaving the GC).

- [ ] **Step 2: B3 — condense the globular-cluster setup.** Anchor: the two sentences from `The high stellar densities in these systems` through `measured independently of the gamma-ray data~\cite{Amerio:2024qor}.` Comment both; `\blue{}` replacement: ONE sentence — globular clusters host large, dynamically formed MSP populations whose abundance correlates with independently measured cluster properties (encounter rate, optical luminosity), details in `Section~\ref{sec:msp_paper}`. Keep the next sentence (clean measurement far from the plane) untouched — it is §4.4's own point.

- [ ] **Step 3: B2 + backref — compact the old-age paragraph.** Anchors: `The MSP hypothesis requires the pulsars responsible for the excess to be systematically fainter` (replace the re-citation `~\cite{Hooper:2016rap,Holst:2024fvb}` with a `(cf.\ Section~\ref{sec:4.2.2})` backref) and keep the old-age/globular-cluster test logic (`One natural explanation is that the Galactic Bulge formed its stars early…` + `Globular clusters test this hypothesis directly…`) — lightly compact if drafting allows, but this hook must survive (it is the paper's de facto intro setup).

- [ ] **Step 4: B1 — replace the headline-number block with the qualitative result.** Anchor: the three sentences from `Building on an earlier study by Hooper and Linden` through `demonstrating that old stellar populations do not produce systematically fainter pulsars.` Comment all; `\blue{}` replacement (2–3 sentences, no numbers): in `Amerio:2024qor` we measured the gamma-ray luminosity function of MSPs across the Milky Way's globular cluster system with current Fermi-LAT data, building on `Hooper:2016rap`; the measured luminosity function is consistent with that of Galactic-Plane MSPs, providing **no support for the age-based faintness mechanism** (evidence-level phrasing — this replaces "demonstrating that old stellar populations do not produce…"); full analysis in `Section~\ref{sec:msp_paper}`. Drop: 15.8 yr, 56/157, 8 new, 87 clusters, ⟨L_γ⟩ range, σ_L (removes the σ_L 2.8-vs-2.7 inconsistency).

- [ ] **Step 5: keep 17–37-vs-3 once, reword the twin punchline.** Keep the sentences with `$N_\mathrm{MSP} \sim 17{-}37$` and `Only three MSP candidates` (the quantitative bridge to List et al. — verify 17–37 matches the rendered paper, it does: `introduction.tex:53`). Anchor for rewording: `The GCE can therefore originate from MSPs only if they are significantly less luminous, on average, than those found in any other observed environment.` Comment; `\blue{}` reword so it is no longer the verbatim twin of the §4.2.2 punchline — shift to the "as formulated so far" register (the population would have to be unlike any MSP population so far observed, a requirement current formulations of the hypothesis do not explain).

- [ ] **Step 6: reframe the List et al. convergence.** Anchor: `However, the globular cluster results remove the astrophysical motivation for its existence: if old age does not produce the required ultra-faint MSP populations, no known mechanism can generate $\mathcal{O}(10^5)$ sources of the necessary faintness in the Inner Galaxy.` Comment; `\blue{}` replacement: the globular-cluster results undermine the leading proposed mechanism for such a population — sharpening, from an independent direction, the tension with the MSP interpretation as it has been formulated so far. Keep the following convergence sentence and the final `The remainder of this chapter presents our analysis in full.` (adjust only if flow requires; the paper opens abruptly at "In this study, we revisit…", so the handoff sentence must survive).

- [ ] **Step 7: Compile check.** `pdflatex -interaction=nonstopmode -draftmode main.tex`; Expected: no `^!` lines.

- [ ] **Step 8: Diff self-check + de-facto-intro check.** `git diff chapter_04/sections/4.4_breaking_the_stalemate.tex` — conventions hold; then read the revised §4.4 followed immediately by `paper_msp/sections/introduction.tex` (rendered part, from `In this study, we revisit`) and confirm the handoff still lands: reader knows what GCs test, why, and what the qualitative outcome is, before the paper's numbers arrive.

- [ ] **Step 9: Commit.** `git add chapter_04/sections/4.4_breaking_the_stalemate.tex && git commit -m "Ch4 §4.4: condense paper previews (B1-B3), reframe conclusions as tension-sharpening"`

---

### Task 5: §4.0 — introduction rewrite (numbers + pendulum arc)

**Files:**
- Modify: `chapter_04/sections/4.0_introduction.tex`

**Interfaces:**
- Consumes: final state of §4.1–4.4 (Tasks 1–4) — the intro previews must match: §4.1.4's per-paper values (30–50 GeV, (1–3)×10⁻²⁶) sit inside the intro's broad bracket; the paper framing matches Task 4's ("independent constraint sharpening the tension with the MSP interpretation as formulated so far").
- Produces: the chapter's framing contract. Nothing downstream.

**Required content points for the rewritten paragraphs** (structural, implementer drafts):
- Para 1 (existence, largely keep): excess since 2009, peak 1–3 GeV, ≥10°, persists across diffuse models — unchanged apart from what follows.
- DM consistency sentence(s): spectrum/morphology/intensity **consistent with** annihilation of a WIMP with mass **roughly 30–70 GeV** and **⟨σv⟩ ∼ (1–3)×10⁻²⁶ cm³/s** (thermal-relic compatible), with an explicit clause that best-fit values vary from analysis to analysis within this bracket (NotebookLM-verified spread: 25–55 GeV per-paper, 40–70 in review literature; cite `Daylan:2014rsa,Calore:2014xka,Cirelli:2024ssz`). Comment the current `$\sim 40$--$70$~GeV` and `(1$--$2) \times 10^{-26}` sentences.
- Pendulum paragraph(s), replacing the current one-sided MSP paragraph (comment its sentences): the MSP hypothesis (`Abazajian:2010zy`) + the 2015–2016 point-source evidence (`Lee:2015fea,Bartels:2015aea`) and bulge-morphology results (`Macias:2016nev,Bartels:2017vsx`) produced a period in which an astrophysical origin was widely regarded as favored; that evidence was then challenged (`Leane:2019xiy,Leane:2020pfc`) **and defended** (`Buschmann:2020adf,Calore_2021,manconi2024galacticcenterexcesshighest`); independently, luminosity-function and LMXB constraints challenge the required MSP population (`Hooper:2016rap,Holst:2024fvb,Cholis:2014lta`); recent energy-dependent inference (`List:2025qbx`) has weakened the point-source evidence further. Explicit no-consensus statement: after more than fifteen years the community remains divided, with active literature on both sides; the dark matter hypothesis, rather than being excluded, is regaining viability — the question is being reignited, not settled.
- Paper-framing sentence: this thesis contributes one independent constraint — the globular-cluster MSP luminosity function — that further sharpens the tension with the MSP interpretation as it has been formulated so far (cite `Amerio:2024qor`).
- Roadmap sentence: update to the arc — §4.1 discovery + DM consistency; §4.2 rise of the MSP hypothesis; §4.3 the systematics stalemate and the erosion of the point-source evidence; §4.4 motivates the independent globular-cluster constraint; `sec:msp_paper` the analysis in full. Keep the existing forward-xref style.
- Keep the `\aure{}` note (line 3) and the `\red{}` transitional paragraph untouched.

- [ ] **Step 1: numbers edit** (comment originals, `\blue{}` replacements per content points above).
- [ ] **Step 2: pendulum rewrite of paragraphs 2–3** (comment each replaced sentence; `\blue{}` per sentence; house style — long connected paragraphs, no lists).
- [ ] **Step 3: paper-framing + roadmap sentences** (same conventions).
- [ ] **Step 4: Compile check.** `pdflatex -interaction=nonstopmode -draftmode main.tex`; Expected: no `^!` lines.
- [ ] **Step 5: Diff self-check.** `git diff chapter_04/sections/4.0_introduction.tex` — conventions hold; confirm 30–70 / (1–3)×10⁻²⁶ present and 40–70 / (1–2)×10⁻²⁶ only in `%` lines.
- [ ] **Step 6: Commit.** `git add chapter_04/sections/4.0_introduction.tex && git commit -m "Ch4 §4.0: broaden DM best-fit ranges, rebalance intro into no-consensus pendulum arc"`

---

### Task 6: Verification — full compile + fresh-context referee

**Files:**
- Read: all of `chapter_04/sections/4.0`–`4.4` (revised), `paper_msp/sections/introduction.tex`
- Possibly modify: any of the above (fix findings, same `\blue{}`/`%` conventions)

**Interfaces:**
- Consumes: all prior tasks.
- Produces: verified chapter; final commit.

- [ ] **Step 1: Full compile.** Run: `latexmk -pdf -interaction=nonstopmode main.tex`; Expected: PDF builds; then `grep -E "Reference .* undefined|Citation .* undefined" main.log` restricted to chapter-4 labels/keys → no NEW undefined refs relative to before the edits (pre-existing `\aure{}` placeholders elsewhere may warn).
- [ ] **Step 2: Conventions sweep.** Run: `git diff ed55a47 -- chapter_04/sections/*.tex` (or diff against the pre-plan commit) and verify: every removed sentence exists as a `%` line; every added sentence is `\blue{}`-wrapped; no edits under `paper_msp/`.
- [ ] **Step 3: Dispatch fresh-context referee subagent** (per CLAUDE.md: reviews always in fresh context). The subagent reads the revised §4.0–4.4 cold (plus the rendered paper opening) and checks: (a) the pendulum arc reads neutrally — no residual advocacy in either direction, no sentence declaring what the GCE is; (b) condensed passages still flow; every xref target exists; no orphaned "as discussed above"; (c) §4.4 still sets up the paper's abrupt "In this study, we revisit…" opening; (d) numeric consistency — intro bracket 30–70/(1–3)×10⁻²⁶ vs §4.1.4's 30–50/(1–3)×10⁻²⁶; Lee et al. source counts reconciled; no surviving σ_L 2.8; 17–37-vs-3 appears once in narrative; (e) repetition report A1–A7, B1–B3 recommendations each implemented or explicitly KEEP.
- [ ] **Step 4: Fix findings** (same conventions), re-run Step 1.
- [ ] **Step 5: Final commit.** `git add -A chapter_04 && git commit -m "Ch4: verification fixes after referee pass"` (skip if no findings).
