# Chapter 8 Repetition Reduction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply the Chapter 8 repetition-reduction edits from the approved design spec, commenting out redundant prose and adding `\blue{}`-marked replacements, so the chapter reads without intra-chapter duplication while every change stays visible in the rendered PDF.

**Architecture:** Four file-scoped tasks (one per narrative section file: 8.0, 8.1, 8.2, 8.3). Each task applies a set of exact-string edits, verifies by grep + a clean `pdflatex` compile, and commits. This is a prose-editing plan, not code — the "test" for each task is: the redundant text is commented, the replacement is blue, and the chapter compiles with no new undefined references.

**Tech Stack:** LaTeX (memoir + dinostyle.sty), `latexmk`/`pdflatex`, BibTeX (JHEP). `\blue{}` = `\textcolor{blue}` (macros.tex). `\aure{}` = orange author annotation.

## Global Constraints

- **Removed text → comment with `%`.** Never delete. Files are one-sentence-per-line; comment per sentence.
- **New / replacement text → wrap in `\blue{...}`.** Pure appends (an xref, nothing removed) → add only the inline `\blue{(…)}` fragment, leave the host sentence uncommented.
- **`\aure{}` markers stay.** One new `\aure{}` is added (C5).
- **Paper subtree (`paper_xcorr/`) is read-only.** Never edit it. C5 is flagged in the narrative only.
- **Cross-reference correction:** the subsection labels `sec:8.1.1` / `sec:8.1.2` are **commented out**. Every "cf. Section 8.1.2" from the report resolves to `\ref{sec:8.1}`.
- **Verified labels (all exist):** `sec:8.1`, `sec:8.2.1`, `sec:8.2.2`, `sec:8.2.3`, `sec:8.3.1`, `sec:CTA`, `app:WDM`, `app:expo`, `fig:window_main` (last three live in the paper subtree; referenced, not redefined).
- **Suggested `\blue{}` wording below is a starting point** matched to the report; the drafter may polish for voice but must preserve the stated content and every listed `\ref`/`\cite`.
- Edit by exact-string match, not line number. Line numbers are anchors — locate by content.

---

### Task 1: `8.0_introduction.tex` — A11 hand-off reword

**Files:**
- Modify: `chapter_08/sections/8.0_introduction.tex` (~L21)

**Interfaces:**
- Consumes: nothing.
- Produces: varies the "sensitivity forecast … cross-correlations between the CTAO extragalactic survey and the 2MASS galaxy catalog" phrasing so it no longer triples with §8.3 L57 and the paper bridge.

- [ ] **Step 1: Comment the old hand-off sentence and add the blue reword**

In the §8.0 roadmap paragraph (L21), find the sentence:

```
The paper that follows then presents a full sensitivity forecast for detecting dark matter signals through cross-correlations between the CTAO extragalactic survey and the 2MASS galaxy catalog~\cite{Pinetti:2025hgd}.
```

Comment it out with `%` and add immediately after:

```latex
\blue{The paper that follows~\cite{Pinetti:2025hgd} then quantifies what this combination can achieve, forecasting CTAO's reach for dark matter annihilation and decay.}
```

- [ ] **Step 2: Verify**

Run: `grep -n "quantifies what this combination" chapter_08/sections/8.0_introduction.tex`
Expected: one match. Confirm the old sentence line now begins with `%`.

- [ ] **Step 3: Commit**

```bash
git add chapter_08/sections/8.0_introduction.tex
git commit -m "Ch8 §8.0: reword paper hand-off to break triple-restatement (A11)"
```

---

### Task 2: `8.1_from_resolved_to_cosmic_web.tex` — six §8.1.2 edits (A1, A2, A6, A4, A9, A10)

**Files:**
- Modify: `chapter_08/sections/8.1_from_resolved_to_cosmic_web.tex` (~L40, L51, L63–68, L70, L74–81)

**Interfaces:**
- Consumes: `\ref{sec:8.2.2}` (A4, A9), `\ref{sec:8.2.1}` and `\ref{fig:window_main}` (A10).
- Produces: §8.1 keeps its physics-motivated opening (A1); the ρ² mechanism, EBL numbers, 2MASS overlap, and figure walk-through are stated once and deferred to §8.2 (A2, A6, A9, A10).

- [ ] **Step 1: A1 — reword the opening sentence (L40)**

Find:

```
If dark matter is a particle that annihilates, it could do so not just in our galaxy, but also inside every gravitationally bound structure across the universe.
```

Comment it and add:

```latex
\blue{If dark matter is a particle that annihilates, it does so not only in our own Galaxy but throughout the cosmic web of collapsed structures that fills the universe.}
```

(Breaks the "inside every gravitationally bound structure" verbatim echo of §8.0 L12–13 while keeping a physics scene-setter; does not duplicate L42's "how matter is distributed".)

- [ ] **Step 2: A6 — drop the 20–30% figure (L51)**

L51 holds two sentences. Comment the whole line, then re-add the first sentence verbatim followed by the blue-modified second sentence:

```latex
This is the dark matter component of the \UGRB whose total energy spectrum between 100 MeV and 820 GeV has been measured by the \textit{Fermi}-LAT~\cite{Fermi-LAT:2014ryh}. \blue{Astrophysical source populations contribute their own guaranteed fraction to the UGRB as well: unresolved blazars dominate at high energies (their contribution is quantified in Section~\ref{sec:8.2.3}), while star-forming galaxies, misaligned AGNs, and millisecond pulsars add further contributions across the full energy range~\cite{DGRB-review}.}
```

(Drops "account for about 20--30\% of the total intensity"; the number's primary home is §8.2.3 L82.)

- [ ] **Step 3: A9 — condense the auto-correlation limitations (L63–65), keep L66**

Comment L63, L64, L65 (the three sentences beginning "The auto-correlation power spectrum, however…", "Furthermore, the \textit{measured}…", and "While the theoretical model for $C_\ell$…"). Add in their place:

```latex
\blue{The auto-correlation power spectrum, however, suffers from two limitations. First, the dark matter signal is always mixed with the shot noise and correlated fluctuations of astrophysical sources at the same angular scales; second, the measured $C_\ell$ is a line-of-sight integral over all redshifts and therefore carries no redshift resolution, since it cannot be decomposed into contributions from different distances (developed in Section~\ref{sec:8.2.2}).}
```

Leave L66 ("Cross-correlating the gamma-ray map with an external gravitational tracer resolves both limitations at once…") unchanged — it names both limitations and is the payoff sentence.

- [ ] **Step 4: A4 — append forward xref (L68)**

Find:

```
Any source population that does not cluster with the selected galaxies cancels out of the cross-power spectrum, leaving only the gamma-ray emission that traces the same structures.
```

Pure insert — do not comment. Add the blue fragment before the period:

```latex
Any source population that does not cluster with the selected galaxies cancels out of the cross-power spectrum, leaving only the gamma-ray emission that traces the same structures~\blue{(developed quantitatively in Section~\ref{sec:8.2.2})}.
```

- [ ] **Step 5: A2 — drop the ρ² parenthetical (L70)**

Find:

```
The dark matter annihilation signal peaks at low redshift (because the flux is proportional to $\rho^2$ and thus weights dense, nearby structures more heavily), precisely where a catalog of local galaxies has the highest completeness.
```

Comment it and add:

```latex
\blue{The dark matter annihilation signal peaks at low redshift, precisely where a catalog of local galaxies has the highest completeness.}
```

(The ρ² reason is already stated at L49.)

- [ ] **Step 6: A10 — compress the figure walk-through (L74–81)**

Comment L74, L75, L76, L79, L80, L81 (L77–78 are already commented). These are: "Figure~\ref{fig:window_main} illustrates the core idea.", the `$W_\gamma^\mathrm{DM}(z)$ … sharply peaked at $z<0.1$` sentence, the "Local galaxy catalogs such as 2MASS…" sentence, the "unresolved blazars … spread over $z \sim 0.1$--0.4" sentence, the "Because the cross-correlation with a local catalog…" sentence, and the "Adding redshift information…" sentence. Add in their place:

```latex
\blue{Dark matter emission is local while the blazar background is not, so cross-correlating the gamma-ray sky with a catalog of nearby galaxies selects the redshift window where dark matter dominates and suppresses the bulk of the blazar population. Section~\ref{sec:8.2.1} makes this argument quantitative (Fig.~\ref{fig:window_main}).}
```

(Subsumes A2-L75, A3-L79, A7-L76. Keeps a valid `\ref{fig:window_main}`.)

- [ ] **Step 7: Verify**

Run:
```bash
grep -n "cosmic web of collapsed structures\|two limitations\|developed quantitatively in Section\|makes this argument quantitative" chapter_08/sections/8.1_from_resolved_to_cosmic_web.tex
```
Expected: four matches (one per new blue passage; A6 shares its line). Confirm the six commented sentences begin with `%` and that KEEP items L49, L71 are untouched.

- [ ] **Step 8: Commit**

```bash
git add chapter_08/sections/8.1_from_resolved_to_cosmic_web.tex
git commit -m "Ch8 §8.1: dedupe rope2/EBL/2MASS/auto-corr previews, defer to §8.2 (A1,A2,A4,A6,A9,A10)"
```

---

### Task 3: `8.2_cross_correlation_technique.tex` — four edits (B4, A2, A3, A7)

**Files:**
- Modify: `chapter_08/sections/8.2_cross_correlation_technique.tex` (~L20, L22, L28, L97–99)

**Interfaces:**
- Consumes: `\ref{app:WDM}` (B4), `\ref{sec:8.1}` (A2), `\ref{sec:8.2.1}` (A7).
- Produces: the DM window expression keeps its load-bearing scaling and defers the full form to the appendix; the low-z/EBL/2MASS points are stated once.

- [ ] **Step 1: B4 — trim the DM window expression (L20)**

Find:

```
For dark matter annihilation, it is proportional to $\langle\sigma v\rangle\,\Delta^2(z)\,\left(\Omega_\mathrm{DM}\rho_c/m_\chi\right)^2\,(1+z)^3\,e^{-\tau(E,z)}$, where $\Delta^2(z)$ is the flux multiplier that captures the enhancement from DM clustering and substructures (see Section~\ref{sec:1.4}).
```

Comment it and add:

```latex
\blue{For dark matter annihilation, it is proportional to $\langle\sigma v\rangle\,\Delta^2(z)/m_\chi^2$, where $\Delta^2(z)$ is the flux multiplier that captures the enhancement from DM clustering and substructures (full expression in Appendix~\ref{app:WDM}).}
```

(Keeps the load-bearing $\langle\sigma v\rangle$, $\Delta^2(z)$, $m_\chi^{-2}$ dependence used at L21; drops the $(1+z)^3 e^{-\tau}$ factors to the appendix.)

- [ ] **Step 2: A2 — append recap xref (L22)**

Find:

```
As a result, $W_\gamma^\mathrm{DM}$ peaks sharply at $z \lesssim 0.1$ and decays rapidly thereafter, regardless of the DM mass or annihilation channel.
```

Pure insert — do not comment. Add the blue fragment before the period:

```latex
As a result, $W_\gamma^\mathrm{DM}$ peaks sharply at $z \lesssim 0.1$ and decays rapidly thereafter, regardless of the DM mass or annihilation channel~\blue{(cf. Section~\ref{sec:8.1})}.
```

- [ ] **Step 3: A3 — trim duplicated blazar number (L28)**

Find:

```
Figure~\ref{fig:window_main} illustrates this feature quantitatively for the benchmark scenario considered in the analysis of this chapter: the DM window functions are confined to low redshift, while blazar contributions extend to $z \sim 0.4$--$0.5$ at 50 GeV.
```

Comment it and add:

```latex
\blue{Figure~\ref{fig:window_main} illustrates this feature quantitatively for the benchmark scenario considered in the analysis of this chapter: the DM window functions are confined to low redshift, while the blazar contributions extend to higher redshift.}
```

(The "$z \sim 0.4$--0.5 at 50 GeV" figure is already stated at L25.)

- [ ] **Step 4: A7 + A3 — collapse the §8.2.3 blue block (L97–99)**

Comment the three `\blue{}` sentences currently at L97–99 (the block beginning "In the context of cross-correlation with CTAO, the case for 2MASS and 2MRS is even stronger…" and ending "…local dark matter photons arrive essentially unabsorbed.}"). Add in their place:

```latex
\blue{In the context of cross-correlation with CTAO, the case for 2MASS and 2MRS is even stronger: at TeV energies the EBL horizon (Section~\ref{sec:8.2.1}) removes the distant blazars while local dark matter photons arrive essentially unabsorbed.}
```

(Subsumes A3-L99's EBL-horizon number restatement and A7-L97/98's 2MASS/2MRS re-introduction, which duplicated L75–77 of the same subsection.)

- [ ] **Step 5: Verify**

Run:
```bash
grep -n "full expression in Appendix\|cf. Section~\\\\ref{sec:8.1}\|extend to higher redshift\|even stronger: at TeV" chapter_08/sections/8.2_cross_correlation_technique.tex
```
Expected: four matches. Confirm the old L20, L28, and L97–99 lines begin with `%`, and KEEP items L31, L75–77, L82 are untouched.

- [ ] **Step 6: Commit**

```bash
git add chapter_08/sections/8.2_cross_correlation_technique.tex
git commit -m "Ch8 §8.2: defer DM window form to appendix, collapse 2MASS/EBL restatements (B4,A2,A3,A7)"
```

---

### Task 4: `8.3_ctao.tex` — five edits + C5 flag (B1, B2, B3, A3, A11, C5)

**Files:**
- Modify: `chapter_08/sections/8.3_ctao.tex` (~L21, L26, L29, L38–43, L47–49, L57)

**Interfaces:**
- Consumes: `\ref{sec:CTA}` (B1, B2), `\ref{app:expo}` (B3), `\ref{sec:8.2.1}` (A3), `\cite{Pinetti:2025hgd}` (A11).
- Produces: the CTAO hardware/survey description keeps its qualitative points and defers exact instrument/survey numbers to the paper; the EBL restatements and paper hand-off are trimmed.

- [ ] **Step 1: B1 — trim the telescope FoV enumeration (L21)**

Find the sentence beginning `\blue{The observatory is planned as two arrays}, one in the northern hemisphere…` and ending `…deployed only in the south where Galactic observations are prioritized).` Comment it and add:

```latex
\blue{The observatory is planned as two arrays, one in the northern hemisphere and one in the south, built from three telescope classes tailored to different energy regimes: the Large-Sized Telescopes (LSTs) at lower energies, the Medium-Sized Telescopes (MSTs) in the core range, and the Small-Sized Telescopes (SSTs) at the highest energies, deployed only in the south where Galactic observations are prioritized (telescope fields of view are detailed in Section~\ref{sec:CTA}).}
```

Leave L22 (energy range + order-of-magnitude over IACTs) unchanged. (Keeps the LST/MST-for-extragalactic roles used at L27.)

- [ ] **Step 2: B1 — replace the repeated FoV values (L42)**

Find:

```
The wide fields of view of the individual telescopes --- up to $8.8^\circ$ for the SSTs and $7.5^\circ$--$7.7^\circ$ for the MSTs --- create deliberate overlaps between adjacent pointings.
```

Comment it and add:

```latex
\blue{The wide, overlapping telescope fields of view (Section~\ref{sec:CTA}) create deliberate overlaps between adjacent pointings.}
```

- [ ] **Step 3: B2 — compress the EGAL survey numbers (L39–41)**

Leave L38 (footprint: "targets \blue{about} a quarter of the sky … $|b| > 5^\circ$") unchanged. Comment L39, L40, L41 (the "split between the two array sites: 15\%/400 h … 10\%/600 h … 1000 hours" sentence, the "grid of telescope pointings spaced by approximately $3^\circ$" sentence, and the "0.51 hours in the south and 1.11 hours in the north … 3 hours per point" sentence). Add in their place:

```latex
\blue{Planned over three years and split between the two array sites, the survey delivers an approximately uniform effective exposure of about three hours per pointing across the footprint; the full pointing grid, per-site observing times, and total exposure budget are specified in Section~\ref{sec:CTA}.}
```

- [ ] **Step 4: B2 — drop the 10% exposure-fluctuation number (L43)**

Find:

```
These overlaps smooth out the exposure variations that inevitably arise when stitching together individual observations, keeping the relative fluctuations in the exposure map to approximately 10\% within the survey region~(see Section~\ref{sec:CTA}).
```

Comment it and add:

```latex
\blue{These overlaps smooth out the exposure variations that arise when stitching together individual observations, keeping the exposure map approximately uniform across the survey region~(see Section~\ref{sec:CTA}).}
```

- [ ] **Step 5: B3 — compress the off-source scenario (L49) and add the C5 typo flag**

Leave L47–48 (the `\blue{Another series of observations…}` scenario intro) unchanged. Find:

```
In the most optimistic projection, these off-source data sum to an effective exposure of approximately 50 hours per sky location --- roughly 25 times larger than the nominal EGAL exposure --- yielding a factor of $\sim 4$ improvement in sensitivity compared to the 3-hour scenario~(see Appendix~\ref{app:expo}).
```

Comment it and add (replacement + the C5 `\aure` flag together):

```latex
\blue{In the most optimistic projection, these off-source data accumulate a substantially deeper effective exposure per sky location, improving the sensitivity over the nominal EGAL scenario (see Appendix~\ref{app:expo}).}
\aure{Paper source \texttt{sensitivity\_forecast.tex} L110 reads ``5 hrs'' where ``50 hrs'' is intended (cf. the 50 h off-source scenario) --- likely a typo to fix upstream in the paper.}
```

- [ ] **Step 6: A3 — trim EBL number restatements (L26 and L29)**

Find L26:

```
More importantly for cross-correlation studies, EBL absorption becomes significant above $\sim 1$~TeV, attenuating photons from sources at $z \gtrsim 0.1$--$0.2$ and \blue{effectively suppressing the astrophysical background from more distant sources}.
```

Comment it and add:

```latex
\blue{More importantly for cross-correlation studies, EBL absorption above $\sim 1$~TeV suppresses the astrophysical background from more distant sources (cf. Section~\ref{sec:8.2.1}).}
```

Then find L29 (the `\blue{}` sentence "EBL attenuation pushes their window functions, which peak at $z \sim 0.3$--$0.4$ at 50~GeV, down to $z \sim 0.1$--$0.2$ above 1 TeV, increasing their overlap with the DM-dominated window at $z \lesssim 0.1$ (cf. Section~\ref{sec:8.2.3}). Thus, even at TeV energies, blazars remain an important background for the cross-correlation."). Comment it and add:

```latex
\blue{EBL attenuation pushes the blazar window functions down toward the DM-dominated window at $z \lesssim 0.1$ (cf. Section~\ref{sec:8.2.1}); thus, even at TeV energies, blazars remain an important background for the cross-correlation.}
```

Leave L28 (the HSP/LISP composition sentence, A8 KEEP) unchanged.

- [ ] **Step 7: A11 — shrink the paper hand-off (L57)**

Find:

```
The section that follows -- based on~\cite{Pinetti:2025hgd} -- applies this framework, forecasting the sensitivity to dark matter annihilation and decay through cross-correlations between the CTAO extragalactic survey and the 2MASS galaxy catalog, and benchmarking the results against complementary search strategies.
```

Comment it and add:

```latex
\blue{The section that follows~\cite{Pinetti:2025hgd} applies this framework to forecast CTAO's sensitivity to dark matter annihilation and decay, benchmarking the results against complementary search strategies.}
```

(Drops the "cross-correlations between the CTAO extragalactic survey and the 2MASS galaxy catalog" clause that triples with §8.0 L21 and the paper bridge.)

- [ ] **Step 8: Verify**

Run:
```bash
grep -n "three telescope classes tailored\|wide, overlapping telescope fields\|delivers an approximately uniform\|approximately uniform across the survey\|substantially deeper effective exposure\|suppresses the astrophysical background from more distant\|pushes the blazar window functions\|applies this framework to forecast" chapter_08/sections/8.3_ctao.tex
```
Expected: eight matches. Confirm the commented originals begin with `%`, the new `\aure{}` typo flag is present, and L22/L27/L28/L38 KEEPs are untouched.

- [ ] **Step 9: Commit**

```bash
git add chapter_08/sections/8.3_ctao.tex
git commit -m "Ch8 §8.3: defer CTAO instrument/survey numbers to paper, trim EBL/hand-off (B1,B2,B3,A3,A11,C5)"
```

---

### Task 5: Whole-chapter compile verification

**Files:**
- No edits — verification only.

- [ ] **Step 1: Compile the thesis**

Run: `latexmk -pdf main.tex` (or `pdflatex main.tex` twice + `bibtex main` if `latexmk` unavailable).
Expected: exit 0, `main.pdf` produced.

- [ ] **Step 2: Check for new undefined references / citations**

Run: `grep -i "undefined\|LaTeX Warning: Reference\|Citation.*undefined" main.log | grep -iv "rerun"`
Expected: no *new* undefined references introduced by these edits. In particular confirm `app:WDM`, `app:expo`, `sec:CTA`, `sec:8.1`, `sec:8.2.1`, `sec:8.2.2`, `sec:8.2.3`, `fig:window_main` all resolve. (Note: `fig:window_main`, `app:WDM`, `app:expo`, `sec:CTA` live in the paper subtree — they resolve only when `\renderpapers=true`; verify against the build configuration the author uses. If the default build has `\renderpapers=false`, these were already dangling before this pass and are out of scope — record but do not "fix" by editing the paper.)

- [ ] **Step 3: Spot-check the rendered blue**

Open `main.pdf` to Chapter 8 and confirm the changed passages render in blue and read coherently, each section still standing alone with a one-line recap + cross-reference.

- [ ] **Step 4: Final commit (if the compile produced any tracked side-effects — usually none, build artifacts are gitignored)**

```bash
git status
# If nothing to commit, this task is verification-only and complete.
```

## Notes for the implementer

- Do **not** normalize US/UK spelling or fix unrelated typos (e.g. "contitute" at §8.3 L28, "specifc" at §8.3 L50) — out of scope for this pass; the surrounding paper carried its own conventions.
- If any suggested `\blue{}` wording reads awkwardly against the neighbouring prose, adjust the wording but preserve the content and every `\ref`/`\cite` listed. The scientific-prose-writer subagent may be dispatched for the two heavier rewrites (A10 in Task 2 Step 6, B2 in Task 4 Step 3) if a closer voice match is wanted.
- Line numbers drift as edits land; always locate by the quoted string, not the number.
