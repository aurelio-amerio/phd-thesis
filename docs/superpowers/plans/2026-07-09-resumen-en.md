# Resumen (English draft) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Write the ≥5,000-word English draft of the thesis summary ("Resumen de la Tesis") in `resumen/resumen_en.tex`, ready for the author's approval and later Spanish translation.

**Architecture:** A single unnumbered chapter compiled after the bibliography, built section by section. Task 1 scaffolds the file; Task 2 builds a verified source dossier from the actual chapter texts; Tasks 3–10 draft one section each by dispatching the `scientific-prose-writer` agent with a self-contained brief and inserting the returned prose; Task 11 runs fresh-context review passes; Task 12 is final verification.

**Tech Stack:** LaTeX (memoir + dinostyle), `latexmk`/`pdflatex`, `texcount`, the `scientific-prose-writer` agent, fresh-context referee/humanizer review agents.

**Spec:** `docs/superpowers/specs/2026-07-09-resumen-design.md`

## Global Constraints

- Content comes ONLY from prose already written in the thesis (chapters 1–8, `frontmatter/abstract_en.tex`). Never invent content. Chapter 9 / GenSBI does not exist and is never mentioned.
- No bullet points or `itemize`/`enumerate` anywhere — Objectives and future directions are flowing prose.
- 5–10 displayed equations total across the whole resumen, using the `\be` / `\ee` macros. No derivations.
- Sparse citations: `\cite` only for specific measurements/claims and the five thesis papers, reusing keys that already exist in `bibliography.bib`. Never add bib entries.
- No glossary macros (`\gls`, `\ac`, …): spell out every acronym at first use inside the resumen (e.g. "the Large Area Telescope (LAT)").
- Internal headings are `\section*{...}` (unnumbered). The chapter header lines already in `resumen/resumen_en.tex` are kept as-is.
- Every quantitative statement must match the chapter text verbatim in value (verified via the Task 2 dossier). If a number cannot be verified, mark it `\aure{verify: ...}` instead of guessing.
- Style: thesis voice per `CLAUDE.md` (first-person plural, physical picture first, long self-contained paragraphs, bold lead-ins in the methodology section, no vetoed vocabulary, no AI-writing patterns).
- All prose drafting is dispatched to the `scientific-prose-writer` agent (it returns prose in its report and writes no files); review passes run in fresh-context subagents, never inline.
- Commit after every task. Commit messages end with `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`.

**Compile check used throughout** (fast single pass, run from repo root):

```bash
pdflatex -interaction=nonstopmode -draftmode main.tex 2>&1 | grep -E "^!" ; echo "exit: $?"
```

Expected: no `!` lines printed (grep exits 1). A full `latexmk -pdf main.tex` is only required in Tasks 1, 11 and 12.

**Word-count check used throughout:**

```bash
texcount -sum -1 resumen/resumen_en.tex
```

---

### Task 1: Scaffold `resumen_en.tex` and switch the main.tex import

**Files:**
- Modify: `resumen/resumen_en.tex`
- Modify: `main.tex:137`

**Interfaces:**
- Produces: `resumen/resumen_en.tex` with eight `\section*` headings, each followed by an HTML-comment-style LaTeX marker (`% <<SECTION-NAME>>`) that later tasks replace with prose. Later tasks rely on these exact marker strings.

- [ ] **Step 1: Write the skeleton**

Replace the content of `resumen/resumen_en.tex` with:

```latex
\chapter*{Summary of the thesis}
\addcontentsline{toc}{chapter}{Summary of the thesis}

\section*{Preface}
% <<PREFACE>>

\section*{The dark matter problem}
% <<DM-PROBLEM>>

\section*{The gamma-ray sky and the \textit{Fermi} Large Area Telescope}
% <<GAMMA-SKY>>

\section*{Objectives}
% <<OBJECTIVES>>

\section*{Methodology: statistics and machine learning for faint signals}
% <<METHODOLOGY>>

\section*{Results}
% <<RESULTS-MSP>>
% <<RESULTS-SUBHALOS>>
% <<RESULTS-DNDS>>
% <<RESULTS-CATALOG>>
% <<RESULTS-XCORR>>

\section*{Conclusions and future directions}
% <<CONCLUSIONS>>
```

- [ ] **Step 2: Switch the import in `main.tex`**

At `main.tex:137`, change:

```latex
\import{resumen/}{resumen.tex}
```

to:

```latex
\import{resumen/}{resumen_en.tex}  % TODO: swap back to resumen.tex once the Spanish translation is done
```

- [ ] **Step 3: Full compile**

Run: `latexmk -pdf -interaction=nonstopmode main.tex`
Expected: exits 0; `main.pdf` contains a "Summary of the thesis" chapter after the bibliography with the eight empty section headings.

- [ ] **Step 4: Commit**

```bash
git add resumen/resumen_en.tex main.tex
git commit -m "resumen: scaffold English summary chapter"
```

---

### Task 2: Build the verified source dossier

**Files:**
- Create: `resumen/sources.md`

**Interfaces:**
- Produces: `resumen/sources.md`, one `##` section per resumen section (Preface, DM problem, Gamma sky, Objectives, Methodology, Results-MSP, Results-Subhalos, Results-dNdS, Results-Catalog, Results-Xcorr, Conclusions). Each contains: (a) the key claims/numbers to use, quoted or closely paraphrased **with source file and line reference**, (b) the bib keys allowed for that section, each verified to exist in `bibliography.bib`, (c) for Conclusions, the future-directions material found in the written chapters. Tasks 3–10 inline this material into their prose briefs.

- [ ] **Step 1: Extract per-section facts from the thesis**

Read these sources and record, under the matching dossier section, every number, claim, and phrase the spec's structure calls for (spec: `docs/superpowers/specs/2026-07-09-resumen-design.md`, "Structure and word budgets"):

| Dossier section | Primary sources |
|---|---|
| Preface | `frontmatter/abstract_en.tex`; `introduction/`* (if written); `chapter_01/sections/1.0_introduction.tex` |
| DM problem | `chapter_01/sections/1.1_evidence_for_dark_matter.tex`, `1.2_wimp_paradigm.tex`, `1.3_searching_for_dark_matter.tex`, `1.4_indirect_detection.tex` (relic abundance value, thermal cross section, master flux equation form, J-factor, target hierarchy) |
| Gamma sky | `chapter_02/sections/2.2_astrophysical_sky.tex`, `2.3_fermi_lat.tex` (LAT specs, sky components, 4FGL numbers, threshold concept) |
| Objectives | `frontmatter/abstract_en.tex` + each chapter's `X.0_introduction.tex` |
| Methodology | `chapter_03/sections/3.1_inference.tex`, `3.2_sbi.tex`, `3.3_ml_astrophysics.tex`, `3.4_domain_shift.tex`, `3.5_cross_correlations.tex` |
| Results-MSP | `chapter_04/sections/4.5_paper.tex` and the files it inputs under `chapter_04/sections/paper_msp/` (luminosity-function values, 17–37 vs 3 prediction) |
| Results-Subhalos | `chapter_05/sections/5.4_unassociated_sources.tex`, `5.6_paper_dmhalos.tex` + `paper_dm_halos/` (mixture model, no-detection statement, ⟨σv⟩ limits) |
| Results-dNdS | `chapter_06/sections/6.3_sbi_cnn.tex`, `6.5_paper_dnds.tex` (training-set size, ×50 below threshold, S⁻² extension, flux reach) |
| Results-Catalog | `chapter_07/sections/7.4_paper_dnds_catalog.tex` (per-direction likelihood, ~50% more candidates than 4FGL-DR3, public catalog) |
| Results-Xcorr | `chapter_08/sections/8.3_ctao.tex`, `8.4_paper_xcorr.tex` (2MASS, ~50 h, competitiveness statement) |
| Conclusions | closing discussions inside `4.5_paper.tex`, `5.6_paper_dmhalos.tex`, `6.5_paper_dnds.tex`, `7.4_paper_dnds_catalog.tex`, `8.4_paper_xcorr.tex`, and `chapter_08/sections/8.1`–`8.3` outlook passages. NOTE: `conclusion/conclusion.tex` is empty (7 words) — do not use it. |

\* If `introduction/introduction.tex` is empty (it currently has 3 words), note that in the dossier and rely on the abstract + chapter introductions.

Format for each fact:

```markdown
- ⟨L_γ⟩ ~ (1–8)×10³³ erg/s (0.1–100 GeV) — chapter_04/sections/paper_msp/<file>.tex:<line>
```

- [ ] **Step 2: Verify candidate bib keys**

For each external measurement or claim that needs a citation (Planck abundance, 4FGL/4FGL-DR3, the five thesis papers, CTAO, 2MASS, …), find the key used in the chapter text and confirm it exists:

```bash
grep -n "@.*{<key>," bibliography.bib
```

Record only verified keys in the dossier, with the grep line number. If a needed citation has no existing key, record `NO KEY — use \aure{cite: ...} placeholder` (never create bib entries).

- [ ] **Step 3: Self-check the dossier**

Confirm every quantitative claim in the spec's Results section (§ "Results" of the design doc) appears in the dossier with a file:line source, or is flagged as unverifiable. Confirm the Conclusions section contains only future directions actually found in the chapter texts.

- [ ] **Step 4: Commit**

```bash
git add resumen/sources.md
git commit -m "resumen: verified source dossier"
```

---

### Task 3: Draft the Preface (~700 words)

**Files:**
- Modify: `resumen/resumen_en.tex` (replace `% <<PREFACE>>`)

**Interfaces:**
- Consumes: `resumen/sources.md` § Preface.
- Produces: the Preface prose; Task 4's brief includes its final paragraph for transition continuity.

- [ ] **Step 1: Dispatch the prose writer**

Dispatch a `scientific-prose-writer` agent with this brief (fill the `{{...}}` slots from `resumen/sources.md` § Preface before dispatching — the agent does no research):

```
Write the "Preface" section (~700 words, NO displayed equations, NO bullet
points) of the extended English summary of the PhD thesis "Probing the Dark
Universe: Machine Learning and Statistical Approaches to Gamma-Ray Dark
Matter Searches". It is the opening of a ~6000-word standalone summary
chapter; the reader is a physics committee member who has not read the
thesis.

Arc to cover, in order: (1) the evidence for dark matter across scales and
its unknown particle nature; (2) WIMPs annihilating or decaying into
Standard Model states, and gamma rays as privileged messengers (undeflected,
spectrally informative); (3) fifteen-plus years of Fermi-LAT and the
maturity problem: bright targets studied at length, remaining signals faint,
blended with foregrounds, or below the detection threshold; (4) the thesis
claim: progress in indirect detection now depends on statistical and
machine-learning methods that recover information where simple thresholding
fails; (5) the narrative arc of the thesis: as the expected signal weakens
from the Galactic Center out to the cosmic web, the methodology grows more
sophisticated; (6) close by naming the five works integrated in the thesis
and the public deliverables (the gPCS candidate-source catalog).

Verified source facts you must draw from (do not use numbers not listed
here): {{inline dossier § Preface}}

Style: first-person plural; long self-contained paragraphs (6–12
sentences); spell out every acronym at first use (no \gls macros); "assume"
never "posit"; no citations in this section unless a dossier fact carries a
mandatory key. Return ONLY the LaTeX body prose (no \section header).
```

If the agent returns `NEEDS_CONTEXT`, supply the missing dossier facts and re-dispatch; do not let it invent.

- [ ] **Step 2: Insert the prose**

Replace the line `% <<PREFACE>>` in `resumen/resumen_en.tex` with the returned prose.

- [ ] **Step 3: Verify constraints**

```bash
grep -nE "\\\\begin\{(itemize|enumerate)\}|\\\\gls|\\\\ac\{" resumen/resumen_en.tex
```

Expected: no output. Check every number in the inserted prose appears in `resumen/sources.md` § Preface.

- [ ] **Step 4: Compile check**

Run the fast compile check (see Global Constraints). Expected: no `!` errors.

- [ ] **Step 5: Commit**

```bash
git add resumen/resumen_en.tex
git commit -m "resumen: draft preface"
```

---

### Task 4: Draft "The dark matter problem" (~650 words, 2–3 equations)

**Files:**
- Modify: `resumen/resumen_en.tex` (replace `% <<DM-PROBLEM>>`)

**Interfaces:**
- Consumes: `resumen/sources.md` § DM problem; the final paragraph of the Preface (for transition).
- Produces: the section prose, including the master flux equation that the Methodology and Results sections may reference in words (not by number).

- [ ] **Step 1: Dispatch the prose writer**

Brief (fill `{{...}}` from the dossier and the current file):

```
Write the section "The dark matter problem" (~650 words plus 2–3 displayed
equations using \be ... \ee) of the extended English summary. The preceding
Preface ends with: {{final paragraph of Preface}}.

Arc: (1) the pillars of evidence (rotation curves, clusters, lensing, CMB)
in one compact paragraph; (2) the cold-dark-matter abundance as measured
(use the dossier value with its verified \cite key); (3) the WIMP hypothesis
and the relic-abundance punchline — quote the thermal cross section value
as an equation or inline; (4) one paragraph on the three detection
strategies (direct, collider, indirect); (5) indirect detection: present
the master annihilation-flux equation with the J-factor exactly in the form
used in the thesis, and explain in words how it separates particle physics
from astrophysics; (6) close with the target hierarchy the J-factor implies
(Galactic Center, then dwarfs and subhalos, then the extragalactic web),
explicitly prefiguring the order of the results.

Verified source facts and equation forms (use these, nothing else):
{{inline dossier § DM problem}}

Allowed citation keys: {{verified keys from dossier}}.
Style: physical picture first — every equation quantifies a story already
told; no derivations; first-person plural; spell out acronyms at first use
unless already introduced in the Preface ({{list acronyms already introduced}}).
Return ONLY the LaTeX body prose.
```

- [ ] **Step 2: Insert the prose** — replace `% <<DM-PROBLEM>>`.

- [ ] **Step 3: Verify constraints**

Same grep as Task 3 Step 3 (expected: no output). Additionally count equations so far:

```bash
grep -c "\\\\be\b" resumen/resumen_en.tex
```

Expected: ≤ 3 at this point. Verify all `\cite` keys in the new text appear in the dossier's allowed list.

- [ ] **Step 4: Compile check** — fast compile, no `!` errors.

- [ ] **Step 5: Commit**

```bash
git add resumen/resumen_en.tex
git commit -m "resumen: draft dark matter problem section"
```

---

### Task 5: Draft "The gamma-ray sky and the Fermi LAT" (~550 words, 0–1 equations)

**Files:**
- Modify: `resumen/resumen_en.tex` (replace `% <<GAMMA-SKY>>`)

**Interfaces:**
- Consumes: `resumen/sources.md` § Gamma sky; final paragraph of the DM-problem section.

- [ ] **Step 1: Dispatch the prose writer**

Brief:

```
Write the section "The gamma-ray sky and the Fermi Large Area Telescope"
(~550 words, at most 1 displayed equation) of the extended English summary.
The preceding section ends with: {{final paragraph of DM-problem section}}.

Arc: (1) the LAT as a pair-conversion telescope — energy range, all-sky
survey cadence, angular resolution, mission duration (dossier values only);
(2) the decomposition of the GeV sky: Galactic diffuse emission, resolved
point sources dominated by blazars and pulsars, and the isotropic
unresolved background; (3) the 4FGL catalog and the concept of a detection
threshold — what it means for a source to be resolved; (4) close on the two
blind spots that motivate the thesis: sources detected but unassociated
with counterparts, and the population below the threshold whose collective
emission is measured but whose members are not.

Verified source facts: {{inline dossier § Gamma sky}}
Allowed citation keys: {{verified keys}}.
Acronyms already introduced: {{list}}. Style as before.
Return ONLY the LaTeX body prose.
```

- [ ] **Step 2: Insert** — replace `% <<GAMMA-SKY>>`.
- [ ] **Step 3: Verify** — grep check (no itemize/gls), numbers vs dossier, cite keys allowed.
- [ ] **Step 4: Compile check** — no `!` errors.
- [ ] **Step 5: Commit**

```bash
git add resumen/resumen_en.tex
git commit -m "resumen: draft gamma-ray sky section"
```

---

### Task 6: Draft "Objectives" (~200 words, prose, no equations)

**Files:**
- Modify: `resumen/resumen_en.tex` (replace `% <<OBJECTIVES>>`)

**Interfaces:**
- Consumes: `resumen/sources.md` § Objectives.

- [ ] **Step 1: Dispatch the prose writer**

Brief:

```
Write the section "Objectives" (~200 words, ONE flowing prose passage —
absolutely NO bullet points or enumerate environments, this is a hard
requirement from the author) of the extended English summary.

Enumerate the goals inside connected prose (e.g. "The first objective of
this thesis is ... A second goal ... Finally ..."): (1) test the
millisecond-pulsar interpretation of the Galactic Center Excess by
measuring the gamma-ray luminosity function of pulsars in globular
clusters; (2) constrain a dark-matter-subhalo component among the
unassociated Fermi-LAT sources; (3) reconstruct the source-count
distribution dN/dS of extragalactic sources below the detection threshold;
(4) extend the gamma-ray catalogs probabilistically below threshold;
(5) forecast the sensitivity of the Cherenkov Telescope Array Observatory
to the cross-correlation between gamma rays and galaxy catalogs; and,
across all five, (6) develop statistical and machine-learning methodology
for faint-signal regimes that transfers to future instruments.

Verified phrasing sources: {{inline dossier § Objectives}}
Acronyms already introduced: {{list}}. No citations needed. Style as before.
Return ONLY the LaTeX body prose.
```

- [ ] **Step 2: Insert** — replace `% <<OBJECTIVES>>`.
- [ ] **Step 3: Verify** — grep check; confirm the passage contains no `\be`.
- [ ] **Step 4: Compile check** — no `!` errors.
- [ ] **Step 5: Commit**

```bash
git add resumen/resumen_en.tex
git commit -m "resumen: draft objectives section"
```

---

### Task 7: Draft "Methodology" (~950 words, 2–4 equations)

**Files:**
- Modify: `resumen/resumen_en.tex` (replace `% <<METHODOLOGY>>`)

**Interfaces:**
- Consumes: `resumen/sources.md` § Methodology; running equation count from Task 4.
- Produces: method vocabulary (simulation-based inference, neural posterior estimation, quantification learning, probabilistic cataloging, cross-correlation) that the Results briefs reuse verbatim.

- [ ] **Step 1: Dispatch the prose writer**

Brief:

```
Write the section "Methodology: statistics and machine learning for faint
signals" (~950 words, 2–4 displayed equations with \be...\ee, total
equations in the document must stay ≤ 10 and {{n}} are already used) of the
extended English summary.

Organize with bold paragraph lead-ins (\textbf{...} at paragraph start), one
per method, each paragraph closing with a plain-words pointer to the results
subsection that uses it. Methods, in this order:
(1) \textbf{Bayesian inference in the noise-dominated regime.} The
likelihood problem for high-dimensional photon data; why explicit
likelihoods become intractable.
(2) \textbf{Simulation-based inference.} Learning the posterior from
simulations; neural posterior estimation — one equation at most (the
conditional density estimator), in the exact notation of chapter 3.
(3) \textbf{Quantification learning.} Estimating class prevalences rather
than individual labels; prior shift and covariate shift and why they must
be corrected when training on associated sources and applying to
unassociated ones.
(4) \textbf{Deep learning on sky maps.} Convolutional networks as feature
extractors for map-level inference.
(5) \textbf{Probabilistic cataloging.} Assigning each sky direction a
likelihood of hosting a sub-threshold source, rather than thresholding.
(6) \textbf{Cross-correlations.} The angular cross-power spectrum between
gamma-ray anisotropies and galaxy catalogs — one equation at most, in the
thesis notation.

Verified source facts and notation: {{inline dossier § Methodology}}
Allowed citation keys: {{verified keys}}.
Acronyms already introduced: {{list}}. NO bullet points. Style as before.
Return ONLY the LaTeX body prose.
```

- [ ] **Step 2: Insert** — replace `% <<METHODOLOGY>>`.
- [ ] **Step 3: Verify** — grep check; total `\be` count ≤ 7 at this point; notation matches chapter 3 per dossier.
- [ ] **Step 4: Compile check** — no `!` errors.
- [ ] **Step 5: Commit**

```bash
git add resumen/resumen_en.tex
git commit -m "resumen: draft methodology section"
```

---

### Task 8: Draft Results I — Galactic dark matter (2 blocks, ~450 words each)

**Files:**
- Modify: `resumen/resumen_en.tex` (replace `% <<RESULTS-MSP>>` and `% <<RESULTS-SUBHALOS>>`)

**Interfaces:**
- Consumes: `resumen/sources.md` §§ Results-MSP, Results-Subhalos; Methodology vocabulary from Task 7.
- Produces: the first two Results blocks. Each block opens with a bold lead-in (`\textbf{The millisecond-pulsar luminosity function and the Galactic Center Excess.}`, `\textbf{Dark matter subhalos among the unassociated sources.}`) rather than a subsection heading, keeping the Results section one continuous `\section*`.

- [ ] **Step 1: Dispatch the prose writer**

Brief:

```
Write the first two blocks of the "Results" section of the extended English
summary (~450 words each, no new displayed equations unless a dossier
value demands one). Each block starts with a bold paragraph lead-in, NOT a
subsection command:

Block 1 — \textbf{The millisecond-pulsar luminosity function and the
Galactic Center Excess.} Problem: the GCE as a possible dark matter signal
vs an unresolved millisecond-pulsar population. Method: measuring the
gamma-ray luminosity function of pulsars in Milky Way globular clusters
(hierarchical Bayesian analysis, per dossier). Outcome: the dossier's
luminosity-function values, and the prediction that Fermi-LAT should
already have resolved the dossier's predicted number of pulsars against
the observed count — state plainly the resulting strain on the pulsar
interpretation, in the calibrated language the thesis uses.

Block 2 — \textbf{Dark matter subhalos among the unassociated sources.}
Problem: subhalos as individually detectable dark matter clumps hiding
among sources without counterparts. Method: the generative mixture model of
unassociated sources, quantification learning, and the prior/covariate
shift corrections (reuse the Methodology section's vocabulary verbatim).
Outcome: no significant subhalo component; the upper limits exactly as
stated in the dossier (channel, mass range, confidence level).

Verified source facts: {{inline dossier §§ Results-MSP + Results-Subhalos}}
Allowed citation keys: {{verified keys, including the two thesis papers}}.
Acronyms already introduced: {{list}}. Style as before: past tense for
results obtained, quantitative hedging only.
Return ONLY the LaTeX body prose, blocks in order.
```

- [ ] **Step 2: Insert** — replace `% <<RESULTS-MSP>>` and `% <<RESULTS-SUBHALOS>>` with the two blocks.
- [ ] **Step 3: Verify** — grep check; every number matches the dossier file:line entries; cite keys allowed.
- [ ] **Step 4: Compile check** — no `!` errors.
- [ ] **Step 5: Commit**

```bash
git add resumen/resumen_en.tex
git commit -m "resumen: draft results I (GCE pulsars, subhalos)"
```

---

### Task 9: Draft Results II — The unresolved background (2 blocks, ~450 words each)

**Files:**
- Modify: `resumen/resumen_en.tex` (replace `% <<RESULTS-DNDS>>` and `% <<RESULTS-CATALOG>>`)

**Interfaces:**
- Consumes: `resumen/sources.md` §§ Results-dNdS, Results-Catalog; Methodology vocabulary.

- [ ] **Step 1: Dispatch the prose writer**

Brief:

```
Write the third and fourth blocks of the "Results" section (~450 words
each, bold lead-ins, no subsection commands):

Block 3 — \textbf{The source-count distribution below the detection
threshold.} Problem: below threshold, individual sources blur together;
the observable is the collective imprint. Method: a convolutional neural
network trained on the dossier's number of synthetic Fermi-LAT sky maps,
combined with simulation-based inference, applied to the dossier's dataset
(years, energy band). Outcome: reconstruction of dN/dS reaching the
dossier's factor below the Fermi-LAT threshold, agreement with catalogs in
the resolved regime, and the power-law extension with the dossier's index
and flux reach.

Block 4 — \textbf{Probabilistic cataloging of sub-threshold sources.}
Problem: population-level dN/dS says how many sources exist below
threshold but not where. Method: the probabilistic cataloging framework —
comparing observed and simulated skies to assign each direction a
likelihood of hosting a sub-threshold source. Outcome: the dossier's
excess of candidate directions relative to 4FGL-DR3, and the public gPCS
catalog as deliverable, suited to cross-correlation studies (forward
pointer to the final block).

Verified source facts: {{inline dossier §§ Results-dNdS + Results-Catalog}}
Allowed citation keys: {{verified keys, incl. the two thesis papers}}.
Acronyms already introduced: {{list}}. Style as before.
Return ONLY the LaTeX body prose, blocks in order.
```

- [ ] **Step 2: Insert** — replace the two markers.
- [ ] **Step 3: Verify** — grep check; numbers vs dossier; cite keys allowed.
- [ ] **Step 4: Compile check** — no `!` errors.
- [ ] **Step 5: Commit**

```bash
git add resumen/resumen_en.tex
git commit -m "resumen: draft results II (dN/dS, probabilistic catalog)"
```

---

### Task 10: Draft Results III (~450 words) and Conclusions (~650 words)

**Files:**
- Modify: `resumen/resumen_en.tex` (replace `% <<RESULTS-XCORR>>` and `% <<CONCLUSIONS>>`)

**Interfaces:**
- Consumes: `resumen/sources.md` §§ Results-Xcorr, Conclusions; the full Results text so far (for the synthesis).

- [ ] **Step 1: Dispatch the prose writer**

Brief:

```
Write the final Results block and the closing section of the extended
English summary.

Block 5 — \textbf{Cross-correlations with the Cherenkov Telescope Array
Observatory.} (~450 words) Problem: at the largest scales the annihilation
signal traces the matter distribution itself; cross-correlating gamma-ray
anisotropies with galaxy positions isolates a cosmological dark matter
component from isotropic backgrounds. Method and outcome: the forecast
exactly as in the dossier — galaxy catalog, observation time, and the
competitiveness statement for annihilating and decaying dark matter.

Section "Conclusions and future directions" (~650 words, flowing prose, NO
bullet points — hard requirement). Arc: (1) synthesis restating the thesis
arc — from the brightest anticipated signal to the faint imprint of the
cosmic web, no confirmed detection, but a demonstration that the limiting
factor in indirect detection has shifted from photon statistics to
analysis methodology ("the next steps lie less in collecting more photons
than in reading those we already have with sharper statistical tools" —
reuse or closely paraphrase the abstract's closing); (2) future directions
drawn ONLY from the dossier § Conclusions (prospects already written in
chapters 4–8) — weave them into connected prose, one or two sentences
each, in the same order as the results. Do NOT introduce any topic absent
from the dossier.

Verified source facts: {{inline dossier §§ Results-Xcorr + Conclusions}}
Allowed citation keys: {{verified keys}}.
The Results blocks written so far, for continuity: {{brief summary or final
paragraphs of blocks 1–4}}
Acronyms already introduced: {{list}}. Style as before.
Return the LaTeX body prose for both parts, clearly separated.
```

- [ ] **Step 2: Insert** — replace `% <<RESULTS-XCORR>>` and `% <<CONCLUSIONS>>`.
- [ ] **Step 3: Verify** — grep check (itemize/enumerate/gls: none in whole file); every future direction traceable to a dossier entry; cite keys allowed.
- [ ] **Step 4: Word count**

Run: `texcount -sum -1 resumen/resumen_en.tex`
Expected: ≥ 5,000. If short, note the gap for Task 11 (the review pass may expand transitions) and flag to the user at the Task 11 checkpoint rather than padding mechanically.

- [ ] **Step 5: Compile check** — no `!` errors.
- [ ] **Step 6: Commit**

```bash
git add resumen/resumen_en.tex
git commit -m "resumen: draft results III and conclusions"
```

---

### Task 11: Fresh-context review passes (referee + humanizer)

**Files:**
- Modify: `resumen/resumen_en.tex`

**Interfaces:**
- Consumes: the complete draft; `resumen/sources.md` for fact re-checks.

- [ ] **Step 1: Dispatch a fresh-context referee review**

Dispatch a `general-purpose` subagent (fresh context — do NOT review inline) with:

```
Read /home/aure/github/phd-thesis/resumen/resumen_en.tex cold and referee
it as a 12-page thesis summary for a physics committee. Also read
/home/aure/github/phd-thesis/resumen/sources.md and
/home/aure/github/phd-thesis/docs/superpowers/specs/2026-07-09-resumen-design.md.
Check: (1) narrative coherence across sections and quality of transitions;
(2) every quantitative claim against sources.md — flag any number without
a dossier entry; (3) redundancy between sections; (4) compliance: no
bullet points, ≤10 displayed equations, acronyms spelled out at first use,
no \gls, sparse citations; (5) style: thesis voice per CLAUDE.md, no
AI-writing patterns (negative parallelisms, significance inflation,
hedge-then-inflate, copula openers, double approximation), no vetoed
vocabulary ("posit"). Return a numbered list of concrete issues with line
numbers; do not edit any file.
```

- [ ] **Step 2: Dispatch a fresh-context humanizer pass**

Invoke the `humanizer` skill flow in a second fresh subagent on the full text, returning suggested edits (not file writes).

- [ ] **Step 3: Apply accepted fixes**

Apply the referee and humanizer fixes to `resumen/resumen_en.tex`. For any fix that changes a number or claim, re-verify against `resumen/sources.md` before applying. Skip (and record) suggestions that conflict with the spec's ground rules.

- [ ] **Step 4: Full compile and word count**

Run: `latexmk -pdf -interaction=nonstopmode main.tex` — exits 0.
Run: `texcount -sum -1 resumen/resumen_en.tex` — ≥ 5,000 words.

- [ ] **Step 5: Commit**

```bash
git add resumen/resumen_en.tex
git commit -m "resumen: referee and humanizer review fixes"
```

---

### Task 12: Final verification and handoff

**Files:**
- No new files; verification only.

- [ ] **Step 1: Constraint sweep**

```bash
grep -nE "\\\\begin\{(itemize|enumerate)\}|\\\\gls|\\\\ac\{" resumen/resumen_en.tex   # expect: nothing
grep -c "\\\\be\b" resumen/resumen_en.tex                                             # expect: 5–10
grep -oP "\\\\cite\{[^}]*\}" resumen/resumen_en.tex | tr ',' '\n' | sed 's/.*{//;s/}.*//' | sort -u > /tmp/claude/resumen_keys.txt
while read k; do grep -q "{$k," bibliography.bib || echo "MISSING: $k"; done < /tmp/claude/resumen_keys.txt   # expect: no MISSING lines
grep -n "aure{" resumen/resumen_en.tex                                                # list remaining WIP markers (report, do not delete)
```

- [ ] **Step 2: Full build and visual check**

Run: `latexmk -pdf -interaction=nonstopmode main.tex` (exit 0), then extract the resumen pages with `pdftotext` and confirm: chapter appears after the bibliography, all eight sections present, ~12+ pages.

- [ ] **Step 3: Report to the author**

Summarize: final word count, page count, equation count, citation list, any remaining `\aure{}` markers or unverifiable numbers. Remind: Spanish translation into `resumen/resumen.tex` and the `main.tex:137` import swap-back are the follow-up task, out of scope here.

- [ ] **Step 4: Commit any final touch-ups**

```bash
git add -A resumen/
git commit -m "resumen: final verification pass"
```
