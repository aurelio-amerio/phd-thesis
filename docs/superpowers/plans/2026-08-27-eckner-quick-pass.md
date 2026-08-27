# Eckner Quick Pass Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply all 38 non-deferred (🟡) items of Eckner's thesis review, per the approved drafts and author annotations in `reply_eckner.md`.

**Architecture:** Six sequential batches — bib fetch, mechanical fixes, chapter-by-chapter prose edits (Ch. 1→8 + style), a dedicated conclusions humanizer pass, the acronym sweep, final verification. Every task updates `reply_eckner.md` statuses before committing, so the ledger always shows what remains.

**Tech Stack:** LaTeX (memoir + dinostyle, latexmk/pdflatex+BibTeX), InspireHEP API for BibTeX, Claude Code skills (`humanizer`, `scientific-writing`, `acronyms`), Review Mode MCP.

**Spec:** `docs/superpowers/specs/2026-08-27-eckner-quick-pass-design.md`

## Global Constraints

- **Content authority:** `reply_eckner.md` holds each item's verified facts, current text, and approved draft. Where an author annotation modified the draft (quoted per-task below), the annotation wins. Read the item's full entry before editing.
- **Do NOT touch deferred items:** E-4.1, E-4.3, E-4.5, E-4.6, E-4.8, E-3.1, E-6.4, E-6.7 — and do not "improve" nearby text they will later rework.
- **`\blue{}` everything:** all new or reworded prose, including typo fixes and swapped citations, is wrapped in `\blue{...}`.
- **No hand-written BibTeX:** entries come only from InspireHEP (`curl -s "https://inspirehep.net/api/arxiv/<id>" -H "Accept: application/x-bibtex"`). A paper not found there goes in `docs/superpowers/specs/2026-08-27-eckner-missing-bibs.md` (authors, year, title, journal) with an `\aure{missing bib: ...}` placeholder in the LaTeX.
- **Prose model policy:** any subagent that writes, rewords, or reviews prose runs as a **generic agent with `model: "fable"`** — never Sonnet/Haiku, never the `scientific-prose-writer` agent type. The SDD implementer default (Sonnet) is NOT acceptable for prose tasks 3–11; the orchestrator must dispatch those to generic fable agents. Mechanical tasks (1, 2, 12, 13) may use any model.
- **Style guards:** check drafted prose against the vocabulary blacklist ("posit"→"assume", "delivery mechanism", "formalized" now vetoed), the 40-word/3-clause sentence ceiling, and the surrounding section's US/UK spelling. Never delete `\aure{}` markers.
- **Review protocol (every prose task, after edits compile):** dispatch ONE fresh generic agent (`model: "fable"`) whose prompt names the edited files/line ranges and instructs it to (a) invoke the `humanizer` skill and (b) apply `scientific-writing` review principles to ONLY the `\blue{}` additions, returning a list of concrete findings. Apply accepted findings; reject with one-line reasons in the task report. Never review inline in the drafting context.
- **Status-update protocol (every task, before its final commit):** in `reply_eckner.md`, for each completed item flip the header `⬜` → `✅`, flip its Summary-table row 🟡 → ✅, and update the bottom counts line. Partial completions get a one-line note in the item's Action block instead of ✅.
- **Compile check:** `latexmk -pdf -interaction=nonstopmode main.tex` from the repo root; a task passes only if the log shows no new errors (warnings pre-existing in `main.log` don't count). `grep -c "??" main.pdf` is not reliable — check undefined references via `grep "LaTeX Warning: Reference" main.log`.

---

### Task 1: Bibliography fetch and key map

**Files:**
- Modify: `bibliography.bib`
- Create: `docs/superpowers/specs/2026-08-27-eckner-bibkeys.md` (arXiv → bib key map; later tasks consume it)
- Create (only if needed): `docs/superpowers/specs/2026-08-27-eckner-missing-bibs.md`

**Interfaces:**
- Produces: a table `| arXiv id | bib key | already-present? |` covering every id below. Tasks 3–9 substitute these keys for the `<placeholder>` keys in the reply-doc drafts.

- [ ] **Step 1: Audit existing entries.** For each id below, `grep` `bibliography.bib` for the arXiv number AND plausible keys; record hits: astro-ph/0305003, 1302.2549, 1711.05127, 2012.11477, 1901.07025, 2212.08528, 2512.16699, 1612.08002, 2409.07515, hep-ph/0512090, 2007.16129, 1602.07246, 1603.06978, 1410.3747, 2107.09070, 2307.12546. Also verify `List:2025qbx` ≠ 2107.09070 (they are different papers) and that `Fragione:2017rsp`, `Ye:2022yxt`, `2024PhRvD.109f3024M` exist.
- [ ] **Step 2: Fetch missing entries** from InspireHEP (command in Global Constraints) and append to `bibliography.bib` verbatim (no hand edits beyond whitespace).
- [ ] **Step 3: Grenier 2005 (no arXiv):** `curl -s "https://inspirehep.net/api/doi/10.1126/science.1106924" -H "Accept: application/x-bibtex"`. If not found, create the missing-bibs file listing: I. A. Grenier, J.-M. Casandjian, R. Terrier, *Unveiling extensive clouds of dark gas in the solar neighbourhood*, Science 307 (2005) 1292 — Task 4 will then use an `\aure{}` placeholder.
- [ ] **Step 4: Write the key map** file with the full table.
- [ ] **Step 5: Verify compile** (BibTeX parses: run the compile check; no `I was expecting a ...` bibtex errors in the blg/log).
- [ ] **Step 6: Commit** `bibliography.bib` + key map (`git add` those files; message "bib: add entries for Eckner quick pass (E-batch 1)").

---

### Task 2: Mechanical fixes (compile-verified batch)

**Files:**
- Modify: `chapter_06/sections/paper_dnds/sections/appendix_further_tests.tex`, `chapter_05/sections/paper_dm_halos/sections/mixture_model_and_limits.tex`, `.../statistical_analysis.tex`, `.../dm_subhalos_model.tex`, `chapter_05/sections/5.4_unassociated_sources.tex`, `chapter_03/sections/3.3_ml_astrophysics.tex`, plus files hit by the sweeps
- Modify: `reply_eckner.md` (statuses)

**Interfaces:**
- Produces: correct appendix numbering ("6.A", "6.A.1", …) that Task 13 re-verifies in the PDF.

- [ ] **Step 1 (E-6.9):** in `appendix_further_tests.tex`, promote `\subsection` → `\section` and `\subsubsection` → `\subsection` throughout, mirroring the Chapter 5 convention (`5.6_paper_dmhalos.tex:15-17` uses `\section` inside `subappendices`).
- [ ] **Step 2 (E-5.4):** at the three empty-container sites (`mixture_model_and_limits.tex:1→4`, `statistical_analysis.tex:1→4`, `dm_subhalos_model.tex:1→4`), demote the immediately-following inner header one level so each container has a real child (option (a) of the reply doc).
- [ ] **Step 3 (E-6.6, E-7.3):** `grep -rn "loose" --include="*.tex" .` — fix every misuse of "loose" for "lose" (known: `nn_architecture_training.tex:25,35`, one in `chapter_07/sections/7.4_paper_dnds_catalog.tex`), each as `\blue{lose}`.
- [ ] **Step 4 (E-6.8):** `grep -rn "aleatory" --include="*.tex" .` — fix to `\blue{aleatoric}` (known: `nn_architecture_training.tex:75`).
- [ ] **Step 5 (E-5.3):** `5.4_unassociated_sources.tex:53`: "at lest" → `\blue{at least}`.
- [ ] **Step 6 (E-3.5 part 1):** `3.3_ml_astrophysics.tex:65`: "(statistical)uncertainty" → "(statistical) uncertainty"; line 67: "undertainties" → "uncertainties" (both `\blue{}`).
- [ ] **Step 7: Compile check.** Then confirm E-6.5: `grep "LaTeX Warning: Reference" main.log` shows no `sec:agal-var` complaint, and the appendix renders as "6.A…" (check `main.toc` or the PDF).
- [ ] **Step 8: Statuses** (protocol in Global Constraints): E-5.3, E-5.4, E-6.5, E-6.6, E-6.8, E-6.9, E-7.3 → ✅; E-3.5 gets a "typo half done" note (✅ comes with Task 5).
- [ ] **Step 9: Commit** ("fix: Eckner mechanical batch (E-5.3/5.4/6.5/6.6/6.8/6.9/7.3, E-3.5 typos)").

---

### Task 3: Chapter 1 prose (E-1.1 – E-1.6)

**Files:**
- Modify: `chapter_01/sections/1.4_indirect_detection.tex`
- Modify: `reply_eckner.md`

**Interfaces:**
- Consumes: bib keys from Task 1 (2409.07515, 1612.08002, hep-ph/0512090, 2007.16129, 1603.06978, 1410.3747).
- Produces: an ALP/PBH closing paragraph in §1.4.5 that Task 4's E-2.3 paragraph cross-links to.

- [ ] **Step 1 (E-1.1):** before drafting, check where Chapter 1 first introduces ALPs and PBHs (grep `chapter_01` for "axion", "primordial black hole") — the new closing paragraph after line 376 cross-references rather than re-introduces. Apply the reply-doc draft (adapted to those cross-refs), real bib keys.
- [ ] **Step 2 (E-1.2):** author annotation, verbatim: *"make a smaller change. ...generally weaker due to the experimental difficulties in detecting them... or something similar."* — so at line 387 make ONLY a minimal in-sentence edit; do NOT use the reply-doc's two-sentence draft.
- [ ] **Step 3 (E-1.3):** apply the reply-doc draft at line 389 (Larmor radius + residual anisotropy), one bib ref suffices (Ahlers & Mertsch).
- [ ] **Step 4 (E-1.4):** first verify [129] = `Fermi-LAT:2015att` (check `main.aux`/compiled PDF bibliography order or grep the .bbl); then at line 410 append `2024PhRvD.109f3024M` to the cite.
- [ ] **Step 5 (E-1.5):** extend the multi-anomaly sentence at line 430 with the CMZ-ionisation clause per the reply-doc draft, key from Task 1.
- [ ] **Step 6 (E-1.6):** author annotation: *"good idea, think about how to properly address the point."* Treat the reply-doc draft as direction only: rethink placement (after line 449) and wording so the TeV/CTAO outlook reads as completing the survey, not as an advertisement; keep the Chapter 8 forward reference; verify the actual `\ref` label for Chapter 8 (grep `chapter_08` for `\label{ch`).
- [ ] **Step 7: Compile check.**
- [ ] **Step 8: Review protocol** (Global Constraints) on the edited ranges of `1.4_indirect_detection.tex`; apply accepted findings; recompile if changed.
- [ ] **Step 9: Statuses:** E-1.1 … E-1.6 → ✅. **Commit** ("ch1: Eckner items E-1.1–E-1.6").

---

### Task 4: Chapter 2 prose (E-2.1 – E-2.3)

**Files:**
- Modify: `chapter_02/sections/2.1_production_mechanisms.tex`, `chapter_02/sections/2.2_astrophysical_sky.tex`
- Modify: `reply_eckner.md`

**Interfaces:**
- Consumes: Task 1 keys (Grenier or `\aure{}` fallback, 1602.07246, 1603.06978, 1410.3747); Task 3's §1.4.5 paragraph (E-2.3 cross-links back).

- [ ] **Step 1 (E-2.1):** apply the dark-gas addition at `2.1_production_mechanisms.tex:141` per the reply-doc draft. Author annotation: *"sounds good, double check the phrase"* — before finalizing, verify the physics phrasing (dark gas = optically thick HI + CO-dark H₂, traced via dust or gamma rays) reads correctly against the item's verified facts, and tighten any 40+-word sentence.
- [ ] **Step 2 (E-2.2):** author annotation, verbatim: *"ok, but keep more concise. 'for the GeV dark matter searches undertaken in this thesis.', 'On the other hand, at TeV energies....'. Avoid unneeded connections and qualifiers"* — rewrite the reply-doc draft at `2.2_astrophysical_sky.tex:37` to that skeleton: end the existing sentence at "…undertaken in this thesis.", then a single new sentence starting "On the other hand, at TeV energies…" covering PWNe/SNRs as bright CTAO-relevant backgrounds with the `(cf. Chapter~\ref{...})` pointer.
- [ ] **Step 3 (E-2.3):** insert the transients paragraph after `2.2_astrophysical_sky.tex:74` per the reply-doc draft, real ALP keys; ensure it and Task 3's E-1.1 paragraph cross-reference consistently (E-1.1 points here via `\ref{sec:extragalactic_sources}` — verify that label exists, else use the actual one).
- [ ] **Step 4: Compile check.**
- [ ] **Step 5: Review protocol** on the edited ranges; apply findings.
- [ ] **Step 6: Statuses:** E-2.1, E-2.2, E-2.3 → ✅. **Commit** ("ch2: Eckner items E-2.1–E-2.3").

---

### Task 5: Chapter 3 prose (E-3.2 – E-3.5)

**Files:**
- Modify: `chapter_03/sections/3.1_inference.tex`, `chapter_03/sections/3.3_ml_astrophysics.tex`
- Modify: `reply_eckner.md`

- [ ] **Step 1 (E-3.2):** after "…the globally maximized likelihood) \cite{Mattox:1996zz}." at `3.1_inference.tex:76`, add the detection-TS clarification per the reply-doc draft.
- [ ] **Step 2 (E-3.3):** author annotation: *"re-evaluate how to integrate the comment naturally in the text."* First check whether §3.2 formally defines the KL divergence (grep `3.2` sections for "Kullback"). Then integrate a plain-words gloss of KL into the AIC sentence at line 108 in whatever form reads most naturally — an appositive, a preceding sentence, or a footnote — rather than mechanically inserting the reply-doc's em-dash parenthetical (which produces a 45-word sentence). If §3.2 lacks the definition, add the one-line formula here instead of a forward reference.
- [ ] **Step 3 (E-3.4):** extend the evidence sentence at line 132 per the reply-doc draft (evidence = total probability of the data under the model as a whole; normalization within a model, comparison measure across models).
- [ ] **Step 4 (E-3.5 part 2):** in `3.3_ml_astrophysics.tex`, after the epistemic-uncertainty definition (near line 65), add the seed-variability sentence per the reply-doc draft.
- [ ] **Step 5: Compile check.**
- [ ] **Step 6: Review protocol** on the edited ranges; apply findings.
- [ ] **Step 7: Statuses:** E-3.2, E-3.3, E-3.4, E-3.5 → ✅. **Commit** ("ch3: Eckner items E-3.2–E-3.5").

---

### Task 6: Chapter 4 prose (E-4.2, E-4.4, E-4.7, E-4.10, E-4.11, E-4.12)

**Files:**
- Modify: `chapter_04/sections/4.1_discovery_and_characterization.tex`, `chapter_04/sections/4.2_msp_hypothesis.tex`, `chapter_04/sections/4.3_systematics_stalemate.tex`, `chapter_04/sections/paper_msp/sections/comparisons.tex`, `chapter_04/sections/paper_msp/sections/implications_gce.tex`, and (for E-4.12) whichever thesis-authored file carries the emphasis
- Modify: `reply_eckner.md`

**Interfaces:**
- Consumes: Task 1 keys (2012.11477, Pooley, Bahramian, Eckner 1711.05127, Song 1901.07025, Clark 2212.08528, Berteaud 2512.16699).

- [ ] **Step 1 (E-4.2):** author annotation: *"I agree, let's just change the range and cite the newer papers."* At `4.1_discovery_and_characterization.tex:140`, do NOT append the reply-doc's long clause. Instead update the quoted range "($0.3$--$0.4$~GeV/cm$^3$)" to one consistent with de Salas & Widmark (Gaia-era local 0.4–0.6, global 0.3–0.5 — e.g. $0.3$--$0.6$) and add the 2012.11477 key to the existing cite, all in `\blue{}`.
- [ ] **Step 2 (E-4.4):** apply BOTH reply-doc edits in `4.2_msp_hypothesis.tex`: the replenishment-channel rework at line 71 and the strengthened hedge at line 73, with real keys. Keep `\cite{Fragione:2017rsp,Ploeg:2020jeh,Ye:2022yxt}` on the evolutionary-models sentence at line 72. Do not restate the density/channel argument beyond this passage (deferred E-4.5 will reuse it).
- [ ] **Step 3 (E-4.7):** apply the IC-tail rework at `4.3_systematics_stalemate.tex:71-72` per the reply-doc draft (real Song key; keep `manconi2024galacticcenterhighest`). Then read the rest of §4.3.2 and §4.4's summary sentences and align any leftover "tail argues against MSPs" phrasing with the softened claim.
- [ ] **Step 4 (E-4.10):** append the common-(L₀,σ_L) caveat paragraph at the end of `comparisons.tex` (after the Hooper & Linden comparison) per the reply-doc draft; resolve the `\ref{<sec-4.5.5-label>}` placeholder to the real §4.5.5 label (grep `implications_gce.tex` / the paper wrapper for `\label`). This paper-text addition is explicitly author-approved.
- [ ] **Step 5 (E-4.11):** rework `implications_gce.tex:20` per the reply-doc draft (targeted-not-systematic radio searches), real Clark/Berteaud keys. Explicitly author-approved paper-text change; keep it all inside `\blue{}`.
- [ ] **Step 6 (E-4.12):** author annotation, verbatim: *"I would not modify the text of the paper, but this comment is valid."* Do NOT touch `implications_gce.tex` for this item. Determine whether §4.6 (`summary_conclusions.tex` or equivalent) is thesis-authored or paper text (check whether the file lives under `paper_msp/`); place a 1–2-sentence version of the "cluster-variation model is the realistic assessment" emphasis in thesis-authored text — §4.6 if thesis-authored, else `conclusion/conclusion.tex` where the MSP constraint is summarized.
- [ ] **Step 7: Compile check.**
- [ ] **Step 8: Review protocol** on all edited ranges; apply findings.
- [ ] **Step 9: Statuses:** E-4.2, E-4.4, E-4.7, E-4.10, E-4.11, E-4.12 → ✅. **Commit** ("ch4: Eckner items E-4.2/4.4/4.7/4.10–4.12").

---

### Task 7: Chapter 5 prose (E-5.1, E-5.2)

**Files:**
- Modify: `chapter_05/sections/5.2_dark_matter_substructure.tex`
- Modify: `reply_eckner.md`

- [ ] **Step 1 (E-5.1):** author annotation, verbatim: *"ok, but make more concise, just write mass at the time of formation/accretion/infall"* — at line 35, insert only a short parenthetical/clause stating the threshold refers to the mass at infall (not the reply-doc's full tidal-stripping clause). Confirm lines 40–41 (reionization thresholds) still read consistently; no change there.
- [ ] **Step 2 (E-5.2):** at line 51, replace the topic sentence per the reply-doc draft ("The gravitational potential of the baryonic disk and bulge also modifies…").
- [ ] **Step 3: Compile check.**
- [ ] **Step 4: Review protocol** on the edited ranges; apply findings.
- [ ] **Step 5: Statuses:** E-5.1, E-5.2 → ✅. **Commit** ("ch5: Eckner items E-5.1–E-5.2").

---

### Task 8: Chapter 6 prose (E-6.1, E-6.2, E-6.3)

**Files:**
- Modify: `chapter_06/sections/6.1_limits_individual.tex`, `chapter_06/sections/6.2_source_count.tex`, `chapter_06/sections/paper_dnds/sections/synthetic_map_generation.tex`
- Modify: `reply_eckner.md`

**Interfaces:**
- Consumes: Task 1 key for 2107.09070 (List, Rodd & Lewis 2021 — NOT `List:2025qbx`).

- [ ] **Step 1 (E-6.1):** rephrase `6.1_limits_individual.tex:11` per the reply-doc draft, adjusting the tail so "equally well" appears only once in the sentence pair.
- [ ] **Step 2 (E-6.2):** expand the Γ definition at `6.2_source_count.tex:30` per the reply-doc draft (intrinsic vs observed, EBL cross-ref — verify the §2.2.2 label name).
- [ ] **Step 3 (E-6.3):** at `synthetic_map_generation.tex:104` (verbatim paper text), add the one-photon-floor qualifier as a `\blue{}` addition or footnote per the reply-doc draft, citing the 2107.09070 key. Do not reword the surrounding published sentences.
- [ ] **Step 4: Compile check.**
- [ ] **Step 5: Review protocol** on the edited ranges; apply findings.
- [ ] **Step 6: Statuses:** E-6.1, E-6.2, E-6.3 → ✅. **Commit** ("ch6: Eckner items E-6.1–E-6.3").

---

### Task 9: Chapter 7 prose (E-7.1, E-7.2)

**Files:**
- Modify: `chapter_07/sections/7.1_limits_of_threshold.tex`, `chapter_07/sections/7.2_population_to_spatial.tex`, `conclusion/conclusion.tex:124` (consistency only)
- Modify: `reply_eckner.md`

**Interfaces:**
- Consumes: Task 1 key for 2307.12546 (4FGL-DR4).

- [ ] **Step 1 (E-7.1):** insert the catalog-comparison paragraph after `7.1_limits_of_threshold.tex:49` per the reply-doc draft, real DR4 key.
- [ ] **Step 2 (E-7.2):** at `7.2_population_to_spatial.tex:67`, rephrase "more spurious directions" per the reply-doc draft (false-positive directions, i.e. firing pixels not associated with any real source); then update `conclusion/conclusion.tex:124` to the same final wording.
- [ ] **Step 3: Compile check.**
- [ ] **Step 4: Review protocol** on the edited ranges; apply findings.
- [ ] **Step 5: Statuses:** E-7.1, E-7.2 → ✅. **Commit** ("ch7: Eckner items E-7.1–E-7.2").

---

### Task 10: Chapter 8 + style spot fixes (E-8.1, E-M.1, E-M.2 line fix)

**Files:**
- Modify: `chapter_08/sections/8.2_cross_correlation_technique.tex`, `chapter_03/sections/3.1_inference.tex:17`, `chapter_02/sections/2.2_astrophysical_sky.tex:77`, `conclusion/conclusion.tex:59`
- Modify: `reply_eckner.md`

- [ ] **Step 1 (E-8.1):** rephrase `8.2_cross_correlation_technique.tex:53` per the reply-doc draft (rejecting the CR background is difficult; residual contamination survives the cuts).
- [ ] **Step 2 (E-M.1):** `3.1_inference.tex:17` "is formalized by" → `\blue{is established by}`; `2.2_astrophysical_sky.tex:77` "is formalized by" → `\blue{is made quantitative by}`.
- [ ] **Step 3 (E-M.2 line fix):** `conclusion/conclusion.tex:59`: replace "The delivery mechanism" per the reply-doc options (prefer the restructured "How the pulsars got there…" form; final call to the implementer's ear). Full conclusions pass is Task 11.
- [ ] **Step 4: Compile check.**
- [ ] **Step 5: Review protocol** on the edited ranges; apply findings.
- [ ] **Step 6: Statuses:** E-8.1, E-M.1 → ✅; E-M.2 note "line fix done, full pass pending". **Commit** ("ch8+style: Eckner E-8.1, E-M.1, E-M.2 spot fix").

---

### Task 11: Conclusions humanizer pass (E-M.2 full)

**Files:**
- Modify: `conclusion/conclusion.tex` (chiefly the bullet list around lines 50–130); chapter intro files ONLY if the review surfaces flagged AI-register phrasing there
- Modify: `reply_eckner.md`, possibly the vocabulary-blacklist memory

- [ ] **Step 1:** dispatch a fresh generic agent (`model: "fable"`) to run the `humanizer` skill over `conclusion/conclusion.tex`, focused on the conclusions bullet list, returning proposed rewordings as a findings list (NOT direct edits). Instruct it to respect `\blue{}` markup, `\aure{}` markers, and the deferred-items list (no touching MSP-result claims Task 6 didn't already settle).
- [ ] **Step 2:** review the findings in the orchestrating context; apply accepted ones as `\blue{}` edits; record rejected ones with reasons.
- [ ] **Step 3:** add any author-confirmed vetoed words from this pass to the vocabulary blacklist memory (`feedback_vocabulary_blacklist.md`).
- [ ] **Step 4: Compile check.**
- [ ] **Step 5: Statuses:** E-M.2 → ✅. **Commit** ("style: humanizer pass on conclusions (E-M.2)").

---

### Task 12: Acronym sweep (E-G.1, E-4.9)

**Files:**
- Modify: `acronyms.tex` + chapter .tex files touched by the sweep
- Modify: `reply_eckner.md`

- [ ] **Step 1:** run the `/acronyms` workflow (Skill `acronyms`) chapter by chapter — Ch. 1 through 8, introduction, conclusion — covering at minimum MSP, GCE, NFW, WIMP, NPTF, SCD, CNN, SBI, dSph. It converts literal acronyms to glossary macros and extends `acronyms.tex`; glossary macros then handle first-use expansion automatically (fixing E-4.9's §4.5.2 re-introduction).
- [ ] **Step 2: Compile check** after each chapter's conversion (glossary macros are a common source of compile breaks — commit per chapter to keep bisection easy).
- [ ] **Step 3: Statuses:** E-G.1, E-4.9 → ✅. **Final commit** ("acronyms: thesis-wide harmonisation (E-G.1, E-4.9)").

---

### Task 13: Final verification and bookkeeping

**Files:**
- Modify: `reply_eckner.md` (final counts)

- [ ] **Step 1: Full clean compile** (`latexmk -C && latexmk -pdf -interaction=nonstopmode main.tex`): no errors; `grep "LaTeX Warning: Reference" main.log` and `grep "Citation.*undefined" main.log` show nothing new.
- [ ] **Step 2: PDF spot checks:** appendix numbering "6.A/6.A.1…" (E-6.9), the E-6.5 cross-reference text, §5.4.x containers no longer empty, [129]-position dwarf citation now shows both refs.
- [ ] **Step 3: reply_eckner.md final pass:** all 38 items ✅; counts line reads "38 applied (✅) · 8 deferred (⏳)"; verification notes recorded where the plan added nuance (E-4.2 range, E-4.12 placement).
- [ ] **Step 4 (orchestrator): resolve the 30 Review Mode annotations** on `reply_eckner.md` via the review-mode MCP (`update_annotation`, status="resolved", per-item completion message), then `open_review` to refresh.
- [ ] **Step 5: Commit** ("Eckner quick pass complete: 38/46 items applied, 8 deferred").
