# Chapter 6 Repetition Reduction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove the High/Medium intra-chapter repetitions flagged for Chapter 6 (A1, A2, A4, A8, A9, A10, B1, B4) while preserving the old prose as comments and marking every replacement in blue.

**Architecture:** Pure LaTeX prose editing across five section files. Each removed sentence is commented with `%` (never deleted); each replacement sentence is wrapped in `\blue{...}` so the change is visible in the rendered PDF. No new physics is introduced — every edit shortens, merges, or repoints existing text. §6.1.2 remains the canonical ("KEEP-primary") location for the population-shift argument throughout.

**Tech Stack:** LaTeX (memoir + dinostyle.sty), `\blue{}` macro (`macros.tex:58` = `\textcolor{blue}`), `latexmk`/`pdflatex`.

## Global Constraints

- **Never delete a line.** Comment removed prose with a leading `%`. The old text must remain recoverable in the file.
- **All new/replacement prose is wrapped in `\blue{...}`.** Pure cuts (no replacement) get no blue.
- **Do not touch `\aure{...}` WIP markers** or any `paper_dnds/` file (read-only paper subtree).
- Files are one-sentence-per-line; comment/replace at sentence granularity.
- Blue text below is the **target content** for each edit; wording may be lightly polished at implementation time but must respect the "phrases to avoid" notes (those are the verbatim duplications being removed).
- Cross-reference labels are exact: `sec:6.1.2`, `sec:6.2.2`, `ch:7`, `sec:architechture-and-training` (paper label, spelled with that typo — do not "fix" it).

---

### Task 1: `6.0_introduction.tex` — A1+A2 (intro pivot) and A4 (Ch.7 bookend)

**Files:**
- Modify: `chapter_06/sections/6.0_introduction.tex` (lines 10–12, line 18)

**Resolves:** A1 (High), A2 (High), A4 (Medium).

- [ ] **Step 1: Comment lines 10–12 (the duplicated pivot + "vast population" sentences).** Add a leading `% ` to each of these three lines:
  - L10 `We move from asking whether any specific source is a dark matter subhalo to a broader question: ...`
  - L11 `Below the formal detection threshold lies a vast population of sources that cannot currently be resolved individually.`
  - L12 `They collectively imprint their abundance and flux distribution onto the measured pixel counts, and characterizing this population requires inference techniques capable of extracting population-level observables --- most notably the source-count distribution, $dN/dS$.`
  Leave L9 (`These limitations motivate a shift in strategy.`) unchanged.

- [ ] **Step 2: Insert the blue replacement** immediately after the commented block (before the blank line preceding L14). Avoids the verbatim constructions "asking whether any specific source is a dark matter subhalo" and "Below the formal detection threshold lies a vast population"; forward-refs §6.1.2:

```latex
\blue{Rather than interrogating sources one at a time, we ask what the faint population as a whole imprints on the photon-count statistics of the gamma-ray sky. Section~\ref{sec:6.1.2} develops this population-level perspective and identifies its central observable, the source-count distribution $dN/dS$.}
```

- [ ] **Step 3: Comment line 18 and insert the A4 blue bookend.** Add a leading `% ` to L18 (`The recovered source-count distribution becomes the empirical prior for the probabilistic cataloging framework developed in Chapter~\ref{ch:7}.`), then insert immediately after it:

```latex
\blue{The recovered source-count distribution feeds directly into the cataloging framework of Chapter~\ref{ch:7}.}
```

- [ ] **Step 4: Sanity-check the file.**

Run: `grep -n "\\\\blue\|^%" chapter_06/sections/6.0_introduction.tex`
Expected: the three old pivot lines and the old L18 appear commented; two new `\blue{...}` lines present.

- [ ] **Step 5: Commit.**

```bash
git add chapter_06/sections/6.0_introduction.tex
git commit -m "Ch6 intro: dedup population-shift pivot (A1/A2) and Ch7 bookend (A4)"
```

---

### Task 2: `6.1_limits_individual.tex` — A2 (§6.1.1 close) and A8 (§6.1.2 handoff)

**Files:**
- Modify: `chapter_06/sections/6.1_limits_individual.tex` (line 28, lines 46–47)

**Resolves:** A2 supporting occurrence (High cluster), A8 (Low).

- [ ] **Step 1: Comment line 28 and insert a lean closer.** L28 currently pre-makes §6.1.2's pivot (`The challenge is not to look harder at individual sources, but to develop methods that extract population-level information from the collective photon statistics of the unresolved sky.`). Comment it (`% `), then insert immediately after:

```latex
\blue{Overcoming this blindness requires a different class of methods --- ones that operate at the level of populations rather than individual detections.}
```

- [ ] **Step 2: Comment lines 46–47 and insert the merged handoff.** These two sentences restate the "primary observable is $dN/dS$" role that the §6.2 opener (L4) repeats. Comment both:
  - L46 `The primary observable for characterizing the sub-threshold source population is the source-count distribution, denoted $dN/dS$.`
  - L47 `We define this distribution, discuss its physical interpretation, and review analytical approaches to measuring it in the following section.`
  Insert immediately after:

```latex
\blue{This population is characterized by the source-count distribution $dN/dS$, which we define and whose measurement we review in the following section.}
```

- [ ] **Step 3: Sanity-check.**

Run: `grep -n "\\\\blue\|^%" chapter_06/sections/6.1_limits_individual.tex`
Expected: old L28, L46, L47 commented; two new `\blue{...}` lines present.

- [ ] **Step 4: Commit.**

```bash
git add chapter_06/sections/6.1_limits_individual.tex
git commit -m "Ch6 6.1: soften pre-empting pivot (A2) and merge dN/dS handoff (A8)"
```

---

### Task 3: `6.2_source_count.tex` — A1 (§6.2.1 UGRB), A9 (central-problem repeats), A10 (double ladder)

**Files:**
- Modify: `chapter_06/sections/6.2_source_count.tex` (line 19, line 20, lines 36–39)

**Resolves:** A1 §6.2.1 fix (High), A9 (Medium), A10 (Medium). A9's L38 and A10 are resolved together by the L36–39 rewrite.

- [ ] **Step 1: Comment line 19 and insert the repointed version.** L19 re-defines the UGRB (already defined in §6.1.2 L37) and repeats "inferred from the statistical properties of the photon-count map." Comment L19 (`Further below --- in the unresolved regime, where individual sources are too faint to be detected at all --- the cumulative emission of these sources forms the unresolved gamma-ray background (UGRB), and the $dN/dS$ must be inferred from the statistical properties of the photon-count map.`), then insert immediately after:

```latex
\blue{Further below --- in the unresolved regime, where individual sources are too faint to be detected at all --- the sources merge into the UGRB (Section~\ref{sec:6.1.2}), and $dN/dS$ must be inferred statistically from the photon-count map.}
```

- [ ] **Step 2: Comment line 20 (pure cut, no replacement).** L20 (`This reconstruction is the central challenge addressed by this chapter.`) is a verbatim repeat of L6 fourteen lines earlier. Add a leading `% `. Do **not** add blue — nothing replaces it.

- [ ] **Step 3: Comment lines 36–39 and insert the merged synthesis.** These four lines re-walk the bright→faint ladder already given at L16–20. Comment all four:
  - L36 `The source-count distribution therefore bridges two distinct observational regimes.`
  - L37 `At the bright end, it is anchored by direct measurements from the Fermi-LAT catalog, which shows a flux distribution broadly compatible with an $S^{-2}$ power law (shallower than the Euclidean expectation $S^{-5/2}$) across most of the resolved range \cite{Amerio:2023uet}.`
  - L38 `At the faint end, below the detection threshold of approximately $S_\mathrm{th} \sim 2 \times 10^{-10}$~cm$^{-2}$~s$^{-1}$ in the 1--10 GeV band, the $dN/dS$ must be reconstructed statistically from the collective imprint of unresolved sources on the photon-count map.`
  - L39 `The techniques for performing this reconstruction --- and for extending the $dN/dS$ well below the Fermi-LAT threshold --- are the subject of the following subsections.`
  Insert immediately after. This keeps ONLY the genuinely new quantitative anchors ($S^{-2}$ vs Euclidean $S^{-5/2}$; $S_\mathrm{th}$) and the "following subsections" pointer, dropping the repeated catalog-measurement and photon-count-reconstruction phrasings:

```latex
\blue{Quantitatively, the two regimes meet near the catalog detection threshold $S_\mathrm{th} \sim 2 \times 10^{-10}$~cm$^{-2}$~s$^{-1}$ (1--10 GeV band): above it, the resolved catalog measurement follows a flux distribution broadly compatible with an $S^{-2}$ power law, shallower than the Euclidean expectation $S^{-5/2}$ \cite{Amerio:2023uet}; below it, $dN/dS$ can only be recovered statistically. The techniques for extending it well below the threshold are the subject of the following subsections.}
```

- [ ] **Step 4: Sanity-check (and confirm the `\aure{}` marker at L41 is untouched).**

Run: `grep -n "\\\\blue\|^%\|\\\\aure" chapter_06/sections/6.2_source_count.tex`
Expected: old L19, L20, L36–39 commented; two new `\blue{...}` blocks; the L41 `\aure{...}` footnote marker still present and NOT commented.

- [ ] **Step 5: Commit.**

```bash
git add chapter_06/sections/6.2_source_count.tex
git commit -m "Ch6 6.2: repoint UGRB def (A1), cut repeated central-problem line (A9), merge double ladder (A9/A10)"
```

---

### Task 4: `6.3_sbi_cnn.tex` — B1 (defer exact CNN training numbers to paper)

**Files:**
- Modify: `chapter_06/sections/6.3_sbi_cnn.tex` (lines 46–47)

**Resolves:** B1 (Medium). **Preserve line 48** — the "discretized representation is critical … non-parametrically" sentence carries the argument and must stay.

- [ ] **Step 1: Comment lines 46–47 and insert the qualitative version.** These give exact numbers (20 bins, flux range, 21 outputs, $9\times10^5$ maps) stated in full in the paper. Comment both:
  - L46 `The specific configuration adopted for the $dN/dS$ problem discretizes the output into 20 flux bins spanning $[5 \times 10^{-12},\, 10^{-7}]$~cm$^{-2}$~s$^{-1}$, plus the isotropic background level $F_\mathrm{iso}$, yielding 21 output parameters.`
  - L47 `An ensemble of $9 \times 10^5$ synthetic maps is generated for training.`
  Insert immediately after (defers numbers to the paper architecture section, whose label is `sec:architechture-and-training`):

```latex
\blue{The configuration adopted for the $dN/dS$ problem discretizes the output into a set of flux bins plus the isotropic background level $F_\mathrm{iso}$, and trains the network on a large ensemble of synthetic maps; the exact binning, flux range, and ensemble size are specified in the paper body (Section~\ref{sec:architechture-and-training}).}
```
  Leave L48 unchanged.

- [ ] **Step 2: Sanity-check.**

Run: `grep -n "\\\\blue\|^%\|discretized representation is critical" chapter_06/sections/6.3_sbi_cnn.tex`
Expected: old L46, L47 commented; one new `\blue{...}` line; L48 ("discretized representation is critical…") present and uncommented.

- [ ] **Step 3: Commit.**

```bash
git add chapter_06/sections/6.3_sbi_cnn.tex
git commit -m "Ch6 6.3: defer exact CNN training numbers to paper body (B1)"
```

---

### Task 5: `6.4_transition.tex` — B4 (trim proof-of-principle / 14yr / 1–10 GeV recitation)

**Files:**
- Modify: `chapter_06/sections/6.4_transition.tex` (lines 14–15)

**Resolves:** B4 (Medium). The paper's rendered introduction fragment (under §6.5) restates "proof of principle", "14 years", "1–10 GeV", "trained CNN"; keep only the factor-50 headline (which that fragment does not state). **Preserve line 16.**

- [ ] **Step 1: Comment lines 14–15 and insert the trimmed sentence.** Comment both:
  - L14 `The analysis presented below should therefore be understood as a proof of principle for the deep-learning approach to population-level gamma-ray inference.`
  - L15 `We apply the trained CNN to 14~years of \textit{Fermi}-LAT data in the 1--10~GeV energy band and recover the source-count distribution down to fluxes approximately 50 times below the catalog detection threshold, demonstrating that the method produces stable, well-calibrated results across a wide dynamic range.`
  Insert immediately after:

```latex
\blue{Applied to real \textit{Fermi}-LAT data, the framework recovers the source-count distribution down to fluxes roughly 50 times below the catalog detection threshold, with stable, well-calibrated results across a wide dynamic range.}
```
  Leave L16 (`The remainder of this chapter presents the analysis in full.`) unchanged.

- [ ] **Step 2: Sanity-check.**

Run: `grep -n "\\\\blue\|^%" chapter_06/sections/6.4_transition.tex`
Expected: old L14, L15 commented; one new `\blue{...}` line; L16 present.

- [ ] **Step 3: Commit.**

```bash
git add chapter_06/sections/6.4_transition.tex
git commit -m "Ch6 6.4: trim proof-of-principle recitation duplicated by paper intro (B4)"
```

---

### Task 6: Compile verification

**Files:**
- No edits; build only.

- [ ] **Step 1: Compile the thesis.**

Run: `latexmk -pdf -interaction=nonstopmode main.tex` (or the repo's usual build).
Expected: PDF builds; no new "undefined reference" warnings for `sec:6.1.2`, `sec:6.2.2`, `ch:7`, `sec:architechture-and-training`.

- [ ] **Step 2: Check the log for broken refs introduced by these edits.**

Run: `grep -i "undefined\|LaTeX Warning: Reference" main.log | grep -i "6\.1\.2\|6\.2\.2\|ch:7\|architechture"`
Expected: no matches (pre-existing unrelated warnings, if any, are out of scope).

- [ ] **Step 3: Eyeball the rendered blue diffs** in the Chapter 6 pages of `main.pdf` — confirm each blue replacement reads cleanly in context and no `\aure{}` marker was disturbed. Report anything that reads awkwardly for a follow-up polish pass.

---

## Notes for the executor

- Line numbers drift as you comment/insert within a file. Within a single task, work **top-to-bottom** and re-locate later edits by their quoted content, not by absolute line number.
- If a proposed blue sentence reads awkwardly next to its surviving neighbors, lightly adjust wording — but do **not** reintroduce any of the "phrases to avoid" that each task calls out (those are the duplications being removed).
