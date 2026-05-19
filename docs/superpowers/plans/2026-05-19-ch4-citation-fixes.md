# Chapter 4 Citation Fixes — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix misattributed, incorrect, and imprecise citations in Chapter 4 (sections 4.1–4.4) identified by the citecheck reports in `.citecheck/`.

**Architecture:** Four targeted edits across three `.tex` files, each correcting a specific citation key or adding missing references. No structural changes.

**Tech Stack:** LaTeX, BibTeX (JHEP style). All edits are to `chapter_04/sections/*.tex` files.

**Context:** The active section files included by `chapter_04/chapter_4.tex` are:
- `sections/4.1_discovery_and_characterization.tex`
- `sections/4.2_msp_hypothesis.tex` (NOT `4.2_competing_interpretations.tex`)
- `sections/4.3_systematics_stalemate.tex`
- `sections/4.4_breaking_the_stalemate.tex`

---

## Summary of Issues

| # | File | Line | Issue | Verdict | Fix |
|---|------|------|-------|---------|-----|
| 1 | 4.1 | 78 | `Abazajian:2012pn` cited for γ=1.12±0.05, but that paper reports γ=1.2 | MISMATCH | Change cite to `Abazajian:2014fta` |
| 2 | 4.2 | 41 | `Bartels:2018xom` (disk MSPs) cited for GCE-as-bulge-tracer finding | MISMATCH | Change to `Bartels:2017vsx` |
| 3 | 4.3 | 53 | `Bartels:2018xom` same wrong-paper issue as #2 | MISMATCH | Change to `Bartels:2017vsx` |
| 4 | 4.3 | 57 | `Cirelli:2024ssz` (generic DM review) too weak for NFW-vs-bulge morphology shift claim | MISMATCH | Add `Macias:2019omb` alongside existing cite |
| 5 | 4.4 | 26 | `Holst:2024fvb` confirmed; "fully consistent" overstates — paper itself says "consistent" | WORDING | Remove "fully", keep "consistent" |

Issues scored borderline but deep-check **CONFIRMED** (no action needed):
- 4.1 line 78 `Abazajian:2014fta` (score 5, deep confirmed) — correctly cited for γ=1.12±0.05
- 4.1 line 78 `Calore:2014xka` (score 6, deep confirmed) — correctly cited for morphology
- 4.1 line 108 `Cirelli:2024ssz` (score 6, deep confirmed) — Eq. 4.13 gives σv_cosmo
- 4.1 line 114 `Fermi-LAT:2015att` (score 6, deep confirmed) — dwarf limits constraining GCE
- 4.3 line 41 `Calore_2021` (score 5, deep confirmed score 9) — 1pPDF with adaptive template fitting

---

### Task 1: Fix misattributed γ value citation in 4.1

**Files:**
- Modify: `chapter_04/sections/4.1_discovery_and_characterization.tex:78`

The text attributes γ = 1.12 ± 0.05 to `Abazajian:2012pn`, but that paper reports γ = 1.2. The correct source for γ = 1.12 ± 0.05 is `Abazajian:2014fta` (deep-check confirmed via arXiv PDF).

- [ ] **Step 1: Edit the citation key**

In `chapter_04/sections/4.1_discovery_and_characterization.tex` line 78, change:

```latex
$\gamma = 1.12 \pm 0.05$~\cite{Abazajian:2012pn}
```

to:

```latex
$\gamma = 1.12 \pm 0.05$~\cite{Abazajian:2014fta}
```

Note: `Abazajian:2012pn` should remain in the general range citation group earlier on the same line (`\cite{Daylan:2014rsa,Abazajian:2012pn,Abazajian:2014fta,Calore:2014xka}`) because it does report γ = 1.2, which falls within the stated 1.1–1.3 range.

- [ ] **Step 2: Verify the edit**

Run: `grep 'Abazajian:2012pn' chapter_04/sections/4.1_discovery_and_characterization.tex`

Expected: Only one occurrence remaining (in the general range citation group on line 78), not the specific γ = 1.12 ± 0.05 attribution.

- [ ] **Step 3: Commit**

```bash
git add chapter_04/sections/4.1_discovery_and_characterization.tex
git commit -m "fix(ch4): correct gamma=1.12 citation from Abazajian:2012pn to Abazajian:2014fta

Abazajian:2012pn reports gamma=1.2; the value 1.12±0.05 comes from Abazajian:2014fta.
Identified by citecheck deep review."
```

---

### Task 2: Replace wrong Bartels citation in 4.2

**Files:**
- Modify: `chapter_04/sections/4.2_msp_hypothesis.tex:41`

`Bartels:2018xom` ("Bayesian model comparison and analysis of the Galactic disc population of gamma-ray millisecond pulsars") is about Galactic disk MSP populations. The text describes a finding that the GCE traces stellar mass in the Galactic bulge, which is from `Bartels:2017vsx` ("The Fermi-LAT GeV excess as a tracer of stellar mass in the Galactic bulge", Nature Astron. 2018, arXiv:1711.04778).

- [ ] **Step 1: Edit the citation key**

In `chapter_04/sections/4.2_msp_hypothesis.tex` line 41, change:

```latex
\ \cite{Bartels:2018xom}, who found that the GCE traces the stellar mass distribution in the inner Galaxy, suggesting a close link between the excess and the Galactic bulge population.
```

to:

```latex
\ \cite{Bartels:2017vsx}, who found that the GCE traces the stellar mass distribution in the inner Galaxy, suggesting a close link between the excess and the Galactic bulge population.
```

- [ ] **Step 2: Verify the edit**

Run: `grep 'Bartels:2018xom' chapter_04/sections/4.2_msp_hypothesis.tex`

Expected: No output (no remaining occurrences).

- [ ] **Step 3: Commit**

```bash
git add chapter_04/sections/4.2_msp_hypothesis.tex
git commit -m "fix(ch4): replace Bartels:2018xom with Bartels:2017vsx in sec 4.2

Bartels:2018xom is about Galactic disk MSPs; the correct paper for the
GCE-as-bulge-tracer finding is Bartels:2017vsx (arXiv:1711.04778).
Identified by citecheck deep review."
```

---

### Task 3: Fix Bartels citation and weak Cirelli reference in 4.3

**Files:**
- Modify: `chapter_04/sections/4.3_systematics_stalemate.tex:53,57`

Two issues on nearby lines:
1. **Line 53**: Same `Bartels:2018xom` → `Bartels:2017vsx` fix as Task 2.
2. **Line 57**: `Cirelli:2024ssz` is a generic DM review that does not address how analysis choices (masking, IEM, Fermi Bubbles treatment) shift NFW-vs-bulge morphology preference. Add `Macias:2019omb` which directly demonstrates this dependence. Keep `Cirelli:2024ssz` as general background.

- [ ] **Step 1: Fix the Bartels citation on line 53**

In `chapter_04/sections/4.3_systematics_stalemate.tex` line 53, change:

```latex
and Bartels et al.~\cite{Bartels:2018xom} challenged this picture
```

to:

```latex
and Bartels et al.~\cite{Bartels:2017vsx} challenged this picture
```

- [ ] **Step 2: Strengthen the Cirelli citation on line 57**

In `chapter_04/sections/4.3_systematics_stalemate.tex` line 57, change:

```latex
and how the Fermi Bubbles emission is treated at low latitudes~\cite{Cirelli:2024ssz}.
```

to:

```latex
and how the Fermi Bubbles emission is treated at low latitudes~\cite{Macias:2019omb,Cirelli:2024ssz}.
```

This adds `Macias:2019omb` (which directly demonstrates the NFW-vs-bulge sensitivity to analysis choices) while retaining `Cirelli:2024ssz` as general background.

- [ ] **Step 3: Verify edits**

Run: `grep -n 'Bartels:2018xom' chapter_04/sections/4.3_systematics_stalemate.tex`

Expected: No output.

Run: `grep -n 'Macias:2019omb' chapter_04/sections/4.3_systematics_stalemate.tex`

Expected: At least two occurrences (line 53 area and line 57).

- [ ] **Step 4: Commit**

```bash
git add chapter_04/sections/4.3_systematics_stalemate.tex
git commit -m "fix(ch4): correct Bartels cite key and add Macias:2019omb in sec 4.3

Replace Bartels:2018xom with Bartels:2017vsx for the bulge-tracer finding.
Add Macias:2019omb alongside Cirelli:2024ssz for the NFW-vs-bulge
analysis-dependence claim, since the Cirelli review is too generic.
Identified by citecheck deep review."
```

---

### Task 4: Match paper wording about Holst luminosity consistency in 4.4

**Files:**
- Modify: `chapter_04/sections/4.4_breaking_the_stalemate.tex:26`

The integrated paper (sec 4.5, `summary_conclusions.tex`) uses "is consistent with" when comparing the globular cluster LF to Holst:2024fvb. The thesis summary in sec 4.4 says "fully consistent", which overstates. Remove "fully" to match the paper's own language.

- [ ] **Step 1: Remove "fully"**

In `chapter_04/sections/4.4_breaking_the_stalemate.tex` line 26, change:

```latex
These values are fully consistent with the luminosity function measured independently for MSPs in the Galactic Plane~\cite{Holst:2024fvb}, demonstrating that old stellar populations do not produce systematically fainter pulsars.
```

to:

```latex
These values are consistent with the luminosity function measured independently for MSPs in the Galactic Plane~\cite{Holst:2024fvb}, demonstrating that old stellar populations do not produce systematically fainter pulsars.
```

- [ ] **Step 2: Verify the edit**

Run: `grep 'are consistent with the luminosity' chapter_04/sections/4.4_breaking_the_stalemate.tex`

Expected: One match on line 26, without "fully".

- [ ] **Step 3: Commit**

```bash
git add chapter_04/sections/4.4_breaking_the_stalemate.tex
git commit -m "fix(ch4): remove 'fully' from Holst LF consistency statement

Match the paper's own wording ('is consistent with') rather than
overstating as 'fully consistent'. Identified by citecheck deep review."
```

---

### Task 5: Rename inactive 4.2 draft to avoid confusion

**Files:**
- Rename: `chapter_04/sections/4.2_competing_interpretations.tex` → `chapter_04/sections/4.2_competing_interpretations.old`

This file is not included by `chapter_4.tex` (the active file is `4.2_msp_hypothesis.tex`). Rename it so it won't be mistakenly edited in future citecheck runs or manual edits.

- [ ] **Step 1: Rename the file**

```bash
git mv chapter_04/sections/4.2_competing_interpretations.tex chapter_04/sections/4.2_competing_interpretations.old
```

- [ ] **Step 2: Verify**

```bash
ls chapter_04/sections/4.2_competing*
```

Expected: Only `4.2_competing_interpretations.old` (no `.tex` version).

- [ ] **Step 3: Commit**

```bash
git add -A chapter_04/sections/4.2_competing_interpretations.*
git commit -m "chore(ch4): rename inactive 4.2 draft from .tex to .old

The active file is 4.2_msp_hypothesis.tex. Renaming the old draft
prevents confusion during future citecheck runs."
```

---

## Verification

After all tasks, confirm no `Bartels:2018xom` references remain in chapter 4 sections:

```bash
grep -rn 'Bartels:2018xom' chapter_04/sections/
```

Expected: No output.
