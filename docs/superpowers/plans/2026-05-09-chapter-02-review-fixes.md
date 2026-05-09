# Chapter 2 Review Fixes — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement all actionable issues from `chapter_02/chapter_review.md`, working through the 3 critical, 6 important, and 4 applicable minor issues in priority order, then verify the thesis compiles cleanly.

**Architecture:** All changes are confined to `chapter_02/sections/` `.tex` files and `chapter_02/references.md`. No bib keys are renamed globally — only chapter-02-local occurrences of `2020ApJS..247...33A` are replaced (other chapters continue using that key). Build is verified with `latexmk` at the end.

**Tech Stack:** LaTeX (pdflatex + BibTeX), latexmk, JHEP bib style.

---

## File Map

| File | Issues addressed |
|---|---|
| `chapter_02/sections/2.2_astrophysical_sky.tex` | 1, 2, 8, 11 |
| `chapter_02/sections/2.3_fermi_lat.tex` | 3, 4, 6, 7, 9 |
| `chapter_02/sections/2.1_production_mechanisms.tex` | 5 |
| `chapter_02/references.md` | 12, 13, 15 |

---

## Task 1: Critical Cross-Reference Fixes

**Files:**
- Modify: `chapter_02/sections/2.2_astrophysical_sky.tex:77,96`
- Modify: `chapter_02/sections/2.3_fermi_lat.tex:65`

### Issue 1 — Wrong chapter number for dN/dS (2.2_astrophysical_sky.tex line 96)

The text sends readers to Chapter 4 (GCE/MSP paper) for dN/dS via SBI; it should be Chapter 6 (Paper 1). Also removes the erroneous "dense stellar environments" phrase which conflates two separate analyses.

- [ ] **Step 1: Apply the fix**

  In `chapter_02/sections/2.2_astrophysical_sky.tex`, find line 96:

  ```latex
  Characterizing this $dN/dS$ distribution is the central observational objective of Chapter~4, where we use simulation-based inference to extract the properties of unresolved source populations from the high-latitude sky and dense stellar environments.
  ```

  Replace with:

  ```latex
  Characterizing this $dN/dS$ distribution is the central observational objective of Chapter~\ref{ch:6}, where we use simulation-based inference to extract the properties of unresolved source populations from the high-latitude sky.
  ```

### Issue 2 — Wrong paper numbers for blazar relevance (2.2_astrophysical_sky.tex line 77)

Paper 3 (MSPs/GCE) is not about blazars. The correct papers for blazar populations are Papers 1, 2, and 4.

- [ ] **Step 2: Apply the fix**

  In `chapter_02/sections/2.2_astrophysical_sky.tex`, find line 77:

  ```latex
  the classification and modeling of blazars are central to the research presented in Papers~2, 3, and~4.
  ```

  Replace with:

  ```latex
  the classification and modeling of blazars are central to the research presented in Sections~\ref{ch:dnds}, \ref{ch:dnds_catalog}, and~\ref{ch:dm_halos}.
  ```

### Issue 3 — Wrong paper numbers for population methods (2.3_fermi_lat.tex line 65)

Paper 3 (MSPs/GCE) does not develop sub-threshold population methods. Papers 1 and 2 are the correct references.

- [ ] **Step 3: Apply the fix**

  In `chapter_02/sections/2.3_fermi_lat.tex`, find line 65:

  ```latex
  motivates the use of statistical population methods---such as those developed in Papers~2 and 3---rather than standard source-by-source extraction.
  ```

  Replace with:

  ```latex
  motivates the use of statistical population methods---such as those developed in Sections~\ref{ch:dnds} and~\ref{ch:dnds_catalog}---rather than standard source-by-source extraction.
  ```

- [ ] **Step 4: Verify all three edits look correct**

  Open the three modified lines and confirm the numbers are as intended. No compilation needed yet.

---

## Task 2: Formatting and Annotation Fixes

**Files:**
- Modify: `chapter_02/sections/2.3_fermi_lat.tex:129-130,136`
- Modify: `chapter_02/sections/2.1_production_mechanisms.tex:138,143-144`

### Issue 4 — Missing space merging two sentences (2.3_fermi_lat.tex line 136)

This fix is bundled with Issue 9 below (they affect the same location on line 136). See Task 3, Step 2.

### Issue 5 — Unresolved `\aure{}` annotation (2.1_production_mechanisms.tex line 138)

The annotation marks a spot where chapter cross-references should be added to the mentions of Paper 1 and Paper 4.

- [ ] **Step 1: Apply the fix**

  In `chapter_02/sections/2.1_production_mechanisms.tex`, find lines 138–144:

  ```latex
  \aure{Here I need to add the link to the appropriate sections}
  Despite the physical sophistication of GALPROP and the flexibility of the template-fitting procedure, the GDE cannot be modeled perfectly.
  Imperfect modeling of the interstellar emission remains the largest single source of systematic uncertainty in gamma-ray astrophysics, introducing errors between 15\% and 30\% depending on the energy range \cite{Ackermann:2014usa, DGRB-review}.
  Uncertainties in the gas column densities (particularly the conversion from CO emission to molecular hydrogen), the interstellar radiation field, and the cosmic-ray propagation parameters all contribute.
  For the analyses presented in this thesis, these uncertainties are critical.
  In Paper~1, extracting the faint source-count distribution requires precise control over the diffuse background model.
  In Paper~4, mismodeling the Interstellar Emission Model directly induces a \emph{dataset shift}---a systematic discrepancy between the training simulations and the real observational data---that complicates the identification of dark matter subhalos.
  ```

  Replace with (remove `\aure{}` wrapper, replace "Paper N" mentions with section cross-references):

  ```latex
  Despite the physical sophistication of GALPROP and the flexibility of the template-fitting procedure, the GDE cannot be modeled perfectly.
  Imperfect modeling of the interstellar emission remains the largest single source of systematic uncertainty in gamma-ray astrophysics, introducing errors between 15\% and 30\% depending on the energy range \cite{Ackermann:2014usa, DGRB-review}.
  Uncertainties in the gas column densities (particularly the conversion from CO emission to molecular hydrogen), the interstellar radiation field, and the cosmic-ray propagation parameters all contribute.
  For the analyses presented in this thesis, these uncertainties are critical.
  In Section~\ref{ch:dnds}, extracting the faint source-count distribution requires precise control over the diffuse background model.
  In Section~\ref{ch:dm_halos}, mismodeling the Interstellar Emission Model directly induces a \emph{dataset shift}---a systematic discrepancy between the training simulations and the real observational data---that complicates the identification of dark matter subhalos.
  ```

### Issue 6 — Closing quotation mark on wrong line (2.3_fermi_lat.tex lines 129–130)

The closing `''` is separated from the word it closes by a line break, which can introduce an unwanted space.

- [ ] **Step 2: Apply the fix**

  In `chapter_02/sections/2.3_fermi_lat.tex`, find lines 129–130:

  ```latex
  Sources receiving a high-confidence match are labeled as ``associated''; those with firm identification through periodicity, correlated variability, or resolved angular extent are labeled as ``identified.
  '' In the 4FGL,
  ```

  Replace with:

  ```latex
  Sources receiving a high-confidence match are labeled as ``associated''; those with firm identification through periodicity, correlated variability, or resolved angular extent are labeled as ``identified.'' In the 4FGL,
  ```

---

## Task 3: Citation Fixes in 2.3_fermi_lat.tex

**Files:**
- Modify: `chapter_02/sections/2.3_fermi_lat.tex:109,115,120,131,136`

**Context:** `2020ApJS..247...33A` (raw ADS key for published 4FGL) and `Fermi-LAT:2019yla` (named key for the same paper's arXiv version) are used inconsistently in chapter 2. Other chapters use `2020ApJS..247...33A` extensively — do **not** change those. Only replace within `chapter_02/sections/2.3_fermi_lat.tex`.

Additionally, on line 136 the 4FGL catalog is incorrectly cited for a ΛCDM cosmological prediction about subhalo abundances; the correct reference is `Cirelli:2024ssz` and `Springel:2008cc` (both already used in this thesis for exactly this claim in Chapter 1).

### Issue 7 — Standardize 4FGL citation key (lines 109, 115, 120, 131)

- [ ] **Step 1: Fix line 109**

  Find:
  ```latex
  The \textit{Fermi}-LAT collaboration achieves this through a global maximum likelihood framework \cite{Mattox:1996zz,2020ApJS..247...33A}.
  ```
  Replace with:
  ```latex
  The \textit{Fermi}-LAT collaboration achieves this through a global maximum likelihood framework \cite{Mattox:1996zz,Fermi-LAT:2019yla}.
  ```

- [ ] **Step 2: Fix line 115**

  Find:
  ```latex
  the catalog detection threshold of $TS > 25$ corresponds to a significance of just over $4\sigma$ \cite{Fermi-LAT:2015bhf,2020ApJS..247...33A}.
  ```
  Replace with:
  ```latex
  the catalog detection threshold of $TS > 25$ corresponds to a significance of just over $4\sigma$ \cite{Fermi-LAT:2015bhf,Fermi-LAT:2019yla}.
  ```

- [ ] **Step 3: Fix line 120**

  Find:
  ```latex
  to the Fourth Catalog (4FGL, 8 years, 5,064 sources) \cite{Fermi-LAT:2015bhf,2020ApJS..247...33A} reflects
  ```
  Replace with:
  ```latex
  to the Fourth Catalog (4FGL, 8 years, 5,064 sources) \cite{Fermi-LAT:2015bhf,Fermi-LAT:2019yla} reflects
  ```

- [ ] **Step 4: Fix line 131**

  Find:
  ```latex
  and remains unassociated \cite{2020ApJS..247...33A}.
  ```
  Replace with:
  ```latex
  and remains unassociated \cite{Fermi-LAT:2019yla}.
  ```

### Issues 4 + 9 — Fix ΛCDM citation and missing space (line 136)

Line 136 has two problems at the same location: the 4FGL catalog (`2020ApJS..247...33A`) is cited for a cosmological prediction about subhalo abundances (should be `Cirelli:2024ssz, Springel:2008cc`), and there is a missing space after the period.

- [ ] **Step 5: Fix line 136**

  Find:
  ```latex
  closely resembling an unassociated \textit{Fermi}-LAT point source \cite{2020ApJS..247...33A}.Separating such candidates
  ```
  Replace with:
  ```latex
  closely resembling an unassociated \textit{Fermi}-LAT point source \cite{Cirelli:2024ssz, Springel:2008cc}. Separating such candidates
  ```

- [ ] **Step 6: Confirm no remaining `2020ApJS..247...33A` in chapter_02/**

  Run:
  ```powershell
  Select-String -Path "C:\Users\Aure\Documents\GitHub\phd-thesis\chapter_02\sections\*.tex" -Pattern "2020ApJS"
  ```
  Expected: no matches.

---

## Task 4: Content Improvements

**Files:**
- Modify: `chapter_02/sections/2.2_astrophysical_sky.tex:18,90`

### Issue 8 — GDE 80% claim stated twice (2.2_astrophysical_sky.tex line 18)

The 80% figure already appeared in Section 2.1.3. Replace the repetition with a cross-reference.

- [ ] **Step 1: Apply the fix**

  In `chapter_02/sections/2.2_astrophysical_sky.tex`, find line 18:

  ```latex
  The Galactic Diffuse Emission (GDE) dominates the observed sky, accounting for approximately 80\% of all photons detected by the Fermi-LAT \cite{DGRB-review}.
  ```

  Replace with:

  ```latex
  As discussed in Section~\ref{sec:gde_model}, the Galactic Diffuse Emission (GDE) dominates the observed sky.
  ```

### Issue 11 — Missing first Fermi-LAT dN/dS citation (2.2_astrophysical_sky.tex line 90)

The `Fermi-LAT:2010tsy` key (Abdo et al. 2010, first Fermi-LAT dN/dS measurement) is tracked in `references.md` but never cited in the text. Add it alongside the Malyshev & Hogg citation where the 1-point PDF method is introduced.

- [ ] **Step 2: Apply the fix**

  In `chapter_02/sections/2.2_astrophysical_sky.tex`, find line 90:

  ```latex
  One effective approach uses photon-count probability distribution functions (1-point PDF or $P(D)$ statistics), which analyze the statistical fluctuations of pixel intensities across the gamma-ray sky map \cite{malyshev2011statistics, DGRB-review}.
  ```

  Replace with:

  ```latex
  One effective approach uses photon-count probability distribution functions (1-point PDF or $P(D)$ statistics), which analyze the statistical fluctuations of pixel intensities across the gamma-ray sky map \cite{malyshev2011statistics, Fermi-LAT:2010tsy, DGRB-review}.
  ```

---

## Task 5: References.md Housekeeping *(optional — skip if short on time)*

**Files:**
- Modify: `chapter_02/references.md`

Low-priority bookkeeping. The data table in Section 4 of `references.md` marks many bib keys as "needs adding ❌" or "needs checking ❌" even though the keys are present in `bibliography.bib`. Additionally, two cited keys (Mattox et al. 1996 and Fermi-LAT:2013iui) are missing from the tracking document. **Only do this task if the preceding tasks took little time; it has no impact on the compiled thesis.**

### Issue 13 — Update stale ❌ entries to ✅

The following keys are confirmed present in `bibliography.bib`:

| Paper | Old entry | Correct bib key |
|---|---|---|
| Hooper (2024) | *needs adding* ❌ | `Hooper:2024` |
| Dermer & Menon (2009) | *needs adding* ❌ | `Dermer:2009zz` |
| Blumenthal & Gould (1970) | *needs checking* ❌ | `Blumenthal:1970gc` |
| Kafexhiu et al. (2014) | *needs checking* ❌ | `Kafexhiu:2014cua` |
| Strong et al. (2007) | *needs checking* ❌ | `Strong:2007nh` |
| Pinetti (2022) | *needs checking* ❌ | `Pinetti:2021jjs` |
| Alpar et al. (1982) | *needs checking* ❌ | `1982Natur.300..728A` |
| Hooper et al. (2016) — MSP LF | *needs checking* ❌ | `Hooper:2015jlu` |
| Di Mauro et al. (2014) | *needs adding* ❌ | `DiMauro:2013xta` |
| Tamborra et al. (2014) | *needs checking* ❌ | `Tamborra:2014xia` |

- [ ] **Step 1: Update the data table in references.md**

  For each row in the Section 4 table above, replace `*needs adding*` or `*needs checking*` with the correct key and change ❌ to ✅.

  Final state of the affected rows (replace existing table content):

  ```markdown
  | Hooper (2024) — Particle Cosmology | `Hooper:2024` | ✅ | 2.1.1, 2.1.2 |
  | Dermer & Menon (2009) | `Dermer:2009zz` | ✅ | 2.1.1 |
  | Blumenthal & Gould (1970) | `Blumenthal:1970gc` | ✅ | 2.1.2 |
  | Kafexhiu et al. (2014) | `Kafexhiu:2014cua` | ✅ | 2.1.1 |
  | Strong et al. (2007) — GALPROP | `Strong:2007nh` | ✅ | 2.1.3 |
  | Pinetti (2022) — Thesis | `Pinetti:2021jjs` | ✅ | 2.1.3, 2.3.2 |
  | Alpar et al. (1982) — MSP recycling | `1982Natur.300..728A` | ✅ | 2.2.1 |
  | Hooper et al. (2016) — MSP LF | `Hooper:2015jlu` | ✅ | 2.2.1 |
  | Di Mauro et al. (2014) — mAGN | `DiMauro:2013xta` | ✅ | 2.2.2 |
  | Tamborra et al. (2014) — SFG | `Tamborra:2014xia` | ✅ | 2.2.2 |
  | Abdo et al. (2010) — Fermi dN/dS | `Fermi-LAT:2010tsy` | ✅ | 2.2.2 |
  ```

### Issues 12 + 15 — Add missing entries to tracking table

- [ ] **Step 2: Add Mattox et al. (1996) to the Sec 2.3 block**

  In the Section 4 data table, under `Sec 2.3: Fermi-LAT`, add a new row:

  ```markdown
  | Mattox et al. (1996) — TS definition | `Mattox:1996zz` | ✅ | 2.3.3 |
  ```

- [ ] **Step 3: Add Fermi-LAT:2013iui to the Sec 2.1 block**

  In the Section 4 data table, under `Sec 2.1: Production Mechanisms`, add a new row:

  ```markdown
  | Ackermann et al. (2013) — pion bump | `Fermi-LAT:2013iui` | ✅ | 2.1.1 |
  ```

---

## Task 6: Build Verification

**Files:** all of `main.tex` (entry point for latexmk)

- [ ] **Step 1: Run latexmk from the repo root**

  ```powershell
  cd C:\Users\Aure\Documents\GitHub\phd-thesis
  latexmk -pdf -interaction=nonstopmode main.tex
  ```

  Expected: exits with return code 0, `main.pdf` updated, no `LaTeX Error` lines in log.

- [ ] **Step 2: Check for undefined references**

  ```powershell
  Select-String -Path "main.log" -Pattern "undefined|Warning.*cite|Warning.*ref"
  ```

  Expected: no new undefined citation keys or broken `\ref{}` labels introduced by the edits. Any warnings present before the edits are pre-existing and out of scope.

- [ ] **Step 3: Spot-check the compiled PDF**

  Open `main.pdf` and navigate to:
  - Section 2.2.2 — confirm Chapter 6 (not 4) and Papers 1, 2, and 4 (not 2, 3, 4)
  - Section 2.3.2 — confirm Papers 1 and 2 (not 2 and 3)
  - Section 2.3.3 — confirm `\aure{}` orange text is gone; confirm closing quote on same line as "identified"
  - Section 2.1.3 — confirm `\aure{}` orange text is gone; confirm chapter cross-references appear

---

## Notes on Out-of-Scope Items

These issues from the review are **not addressed** in this plan for the reasons given:

- **Issue 10** (no subsubsection headers in 2.2.1): Stylistic choice; review says "consider". Deferred until author decides.
- **Issue 14** (PSF values vs outline): Current "3.5°–5°" range is correct (front vs. back event types); outline gives a single average. No change needed without checking Atwood et al. (2009) for the exact values.
- **Issue 16** (placeholder figures): All 6 figures need replacement with real figures; deferred until final figures are available.