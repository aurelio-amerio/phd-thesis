# Ch. 5 Citecheck-Deep Fixes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix two citation issues flagged by `citecheck-deep` in Chapter 5 sections 5.2 and 5.4.

**Architecture:** Two independent edits — one factual correction (wrong order of magnitude for WIMP minimum halo mass), one citation supplement (add dedicated DM subhalo search references to back an implicit-only catalog claim). No new bibliography entries needed; all candidate bibkeys already exist in `bibliography.bib`.

**Tech Stack:** LaTeX (pdflatex + BibTeX), `bibliography.bib`, `latexmk`

---

## Issues to Fix

| # | File | Line | Issue | Verdict |
|---|------|------|-------|---------|
| A | `chapter_05/sections/5.2_dark_matter_substructure.tex` | 28 | `~10^{-6}` M☉ disagrees with Cirelli 2024 eq. 2.22 which gives `~10^{-8}` M☉ | mismatch |
| B | `chapter_05/sections/5.4_unassociated_sources.tex` | 24 | "no DM subhalo confirmed" cited only to 4FGL catalog papers which do not state this explicitly | mismatch |

---

## Task 1: Verify the correct WIMP minimum halo mass value

**Files:**
- Read: `chapter_05/sections/5.2_dark_matter_substructure.tex:28`
- Read: `.citecache/pdfs/2406.01705.pdf` (Cirelli 2024, eq. 2.22)

The thesis currently says:
```latex
for a canonical WIMP, the smallest bound structures could have masses as
low as $\sim 10^{-6}\,M_\odot$~\cite{Cirelli:2024ssz}.
```

Cirelli 2024 gives M_min ~ 10^{-8} M☉ for a 100 GeV WIMP (eq. 2.22). The discrepancy arises because different sources use different WIMP parameters and different definitions (kinetic decoupling vs. free-streaming mass). Both 10⁻⁶ and 10⁻⁸ appear in the literature.

- [ ] **Step 1.1: Read Cirelli 2024 eq. 2.22 in context**

  Read `.citecache/pdfs/2406.01705.pdf`, page 58, section 2.2.5.
  Note the exact expression and parameter choices used. The agent found:
  > "eq. (2.22) shows M_min ~ 10^{-8} M_sun for M ~ M' ~ 100 GeV and coupling g'_DM ~ O(1)"

- [ ] **Step 1.2: Check Bringmann:2009vf for the 10^{-6} value**

  `Bringmann:2009vf` (arXiv:0903.0189, "Particle Models and the Small-Scale Structure of Dark Matter") is already in `bibliography.bib`. This paper is the standard reference for WIMP free-streaming masses and often quoted as giving ~10^{-6} M☉. Verify via InspireHEP or the cached abstract whether it explicitly quotes this value.

  ```bash
  cat .citecache/abstracts/Bringmann:2009vf.json 2>/dev/null | python3 -m json.tool | grep -A5 abstract
  ```

  If the abstract does not clarify, read the paper section on free-streaming mass.

- [ ] **Step 1.3: Choose the fix strategy**

  Based on the verification above, pick one of:

  **Option A** — Correct the value to ~10^{-8} M☉ and keep Cirelli as the only citation:
  ```latex
  masses as low as $\sim 10^{-8}\,M_\odot$~\cite{Cirelli:2024ssz}.
  ```
  Use this if 10^{-8} is the well-supported canonical value.

  **Option B** — Expand to a range and add Bringmann:
  ```latex
  masses as low as $\sim 10^{-6}\text{--}10^{-8}\,M_\odot$~\cite{Bringmann:2009vf,Cirelli:2024ssz}.
  ```
  Use this if both values appear in the literature for different WIMP assumptions.

  **Option C** — Keep 10^{-6} but replace the citation with one that explicitly gives this value:
  ```latex
  masses as low as $\sim 10^{-6}\,M_\odot$~\cite{Bringmann:2009vf}.
  ```
  Use this if Bringmann:2009vf explicitly quotes 10^{-6} M☉ for canonical WIMP parameters.

---

## Task 2: Apply the minimum-mass fix in 5.2

**Files:**
- Modify: `chapter_05/sections/5.2_dark_matter_substructure.tex:28`

- [ ] **Step 2.1: Open the file and locate the claim**

  File: `chapter_05/sections/5.2_dark_matter_substructure.tex`, line 28.
  Current text:
  ```latex
  for a canonical WIMP, the smallest bound structures could have masses as low as $\sim 10^{-6}\,M_\odot$~\cite{Cirelli:2024ssz}.
  ```

- [ ] **Step 2.2: Apply the chosen fix (from Task 1 Step 1.3)**

  Apply whichever of Option A / B / C was selected. For example, if Option A:
  ```latex
  for a canonical WIMP, the smallest bound structures could have masses as low as $\sim 10^{-8}\,M_\odot$~\cite{Cirelli:2024ssz}.
  ```

  If Option B:
  ```latex
  for a canonical WIMP, the smallest bound structures could have masses as low as $\sim 10^{-6}\text{--}10^{-8}\,M_\odot$~\cite{Bringmann:2009vf,Cirelli:2024ssz}.
  ```

- [ ] **Step 2.3: Verify LaTeX compiles without errors**

  ```bash
  cd /home/aure/github/phd-thesis
  latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | grep -E "Error|Warning|Undefined" | head -20
  ```
  Expected: no new errors or undefined citations.

- [ ] **Step 2.4: Commit**

  ```bash
  git add chapter_05/sections/5.2_dark_matter_substructure.tex
  git commit -m "fix(ch5): correct WIMP minimum halo mass value in §5.2"
  ```

---

## Task 3: Supplement the "no DM subhalo confirmed" citation in 5.4

**Files:**
- Modify: `chapter_05/sections/5.4_unassociated_sources.tex:24`

The current citation for "no unassociated Fermi-LAT source has been confirmed as a dark matter subhalo" is `~\cite{Fermi-LAT:2019yla,Fermi-LAT:2022byn}`. The 4FGL catalog papers do not explicitly state this absence — they only mention DM subhalos as a speculative possibility. Dedicated DM subhalo search papers are the correct evidence.

The following bibkeys are **already in `bibliography.bib`** and explicitly searched the 4FGL/3FGL for DM subhalo candidates without finding confirmed identifications:

| bibkey | Paper | Notes |
|--------|-------|-------|
| `2015JCAP...12..035B` | Bertoni, Hooper & Linden 2015 | 3FGL search, explicitly discusses no confirmed subhalo |
| `2019JCAP...07..020C` | Coronado-Blázquez et al. 2019a | 4FGL unidentified sources, DM subhalo targets |
| `2019JCAP...11..045C` | Coronado-Blázquez et al. 2019b | complementary analysis |

- [ ] **Step 3.1: Verify the papers explicitly state no confirmation**

  Run InspireHEP lookups to confirm the abstracts of `2015JCAP...12..035B` and `2019JCAP...07..020C` support the "no confirmed DM subhalo" claim:

  ```bash
  cat .citecache/abstracts/2015JCAP...12..035B.json 2>/dev/null | python3 -m json.tool
  cat .citecache/abstracts/2019JCAP...07..020C.json 2>/dev/null | python3 -m json.tool
  ```

  If abstracts are not cached, check via InspireHEP MCP or the arxiv IDs:
  - Bertoni 2015 → arXiv:1509.00611
  - Coronado-Blázquez 2019a → arXiv:1901.02526

- [ ] **Step 3.2: Update the citation at line 24**

  Current text (line 24):
  ```latex
  To date, no unassociated Fermi-LAT source has been confirmed as a dark matter subhalo~\cite{Fermi-LAT:2019yla,Fermi-LAT:2022byn}.
  ```

  Replace with (add dedicated search papers; keep catalog refs for context):
  ```latex
  To date, no unassociated Fermi-LAT source has been confirmed as a dark matter subhalo~\cite{Fermi-LAT:2019yla,Fermi-LAT:2022byn,2015JCAP...12..035B,2019JCAP...07..020C}.
  ```

  Alternatively, if you prefer to cite only the dedicated search papers (which more directly support the claim):
  ```latex
  To date, no unassociated Fermi-LAT source has been confirmed as a dark matter subhalo~\cite{2015JCAP...12..035B,2019JCAP...07..020C,2019JCAP...11..045C}.
  ```

- [ ] **Step 3.3: Verify LaTeX compiles without errors**

  ```bash
  latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | grep -E "Error|Warning|Undefined" | head -20
  ```
  Expected: no undefined citation keys.

- [ ] **Step 3.4: Commit**

  ```bash
  git add chapter_05/sections/5.4_unassociated_sources.tex
  git commit -m "fix(ch5): add explicit DM subhalo search refs to §5.4 confirmation claim"
  ```

---

## Self-Review

**Spec coverage:**
- Issue A (wrong M_min value) → covered by Tasks 1–2 ✓
- Issue B (weak citation for no confirmed subhalo) → covered by Task 3 ✓

**No placeholders present:** Tasks 2 and 3 provide three concrete fix options each with exact LaTeX. Task 1.3 gives decision criteria. ✓

**Risks:**
- If `Bringmann:2009vf` does not explicitly quote 10⁻⁶ M☉, Option C is off the table; choose A or B.
- If the author has already verified the 10⁻⁶ value from a different source (e.g. their own paper), Option C could also cite that source.
- The `\aure{}` comment on line 25 of 5.4 ("recently, there have been some claim of detection of DM subhalos...") is an open TODO unrelated to this plan and should be addressed separately.
