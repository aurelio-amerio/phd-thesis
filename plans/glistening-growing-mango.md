# Chapter 1 Review Fixes — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix all issues identified by the `/referee 1` review — 4 critical (broken refs, wrong citations, missing roadmap entry, wrong Part numbering), 4 important (hardcoded refs, label, summary, figure), and 3 minor (equation numbering, GCE overlap, formatting).

**Architecture:** All changes are in Chapter 1 LaTeX files. No changes to other chapters, bibliography, or build system. One new file created (`1.5_summary.tex`), one figure copied from the Cirelli paper source directory.

**Tech Stack:** LaTeX (pdflatex + BibTeX, JHEP style)

---

## File Map

| File | Action | Responsibility |
|---|---|---|
| `chapter_01/sections/1.0_introduction.tex` | Modify | Fix roadmap paragraph (Task 1) |
| `chapter_01/sections/1.4_indirect_detection.tex` | Modify | Fix citations, cross-refs, Part numbering, hardcoded refs, equation numbering (Tasks 2–6, 9) |
| `chapter_01/chapter_1.tex` | Modify | Fix chapter label, add summary input (Tasks 7, 8) |
| `chapter_01/sections/1.5_summary.tex` | Create | Chapter summary (Task 8) |
| `chapter_01/sections/1.3_searching_for_dark_matter.tex` | Modify | Add detection triangle figure, trim GCE overlap (Tasks 10, 11) |
| `chapter_01/sections/1.1_evidence_for_dark_matter.tex` | Modify | H II formatting (Task 12) |
| `chapter_01/figures/DMdetections.pdf` | Copy from `cirelli-paper/arXiv-2406.01705v3/figs/DMdetections.pdf` | Detection triangle figure (Task 10) |

---

### Task 1: Fix introduction roadmap — add Section 1.3, correct Section 1.4 ref

**Files:**
- Modify: `chapter_01/sections/1.0_introduction.tex:14-18`

**Issue:** The roadmap mentions only 3 sections and labels the indirect detection formalism as `\ref{sec:1.3}`, but that's "Searching for Dark Matter." The formalism is `\ref{sec:1.4}`.

- [ ] **Step 1: Replace the roadmap paragraph**

Replace lines 14–18 with:

```latex
This chapter lays the groundwork for the searches presented in the rest of the thesis.
We begin by reviewing the multi-scale evidence for dark matter, from galactic rotation curves to the cosmic microwave background (Section~\ref{sec:1.1}).
We then introduce the WIMP paradigm, deriving the thermal freeze-out mechanism and the resulting relic abundance calculation that defines the target cross-section for experimental searches (Section~\ref{sec:1.2}).
Section~\ref{sec:1.3} surveys the three complementary experimental strategies --- direct, collider, and indirect detection --- and argues that indirect detection via gamma-rays provides the most direct test of the WIMP hypothesis.
Finally, Section~\ref{sec:1.4} develops the indirect detection formalism in detail --- annihilation channels, spectral signatures, density profiles, and the $J$-factor/$D$-factor framework --- that connects particle physics parameters to observable gamma-ray fluxes.
The observational targets and the current status of indirect searches, reviewed at the end of this chapter, provide the direct motivation for the advanced statistical and machine learning approaches that constitute the core of this thesis.
```

- [ ] **Step 2: Commit**

```
git add chapter_01/sections/1.0_introduction.tex
git commit -m "fix: rewrite Ch1 introduction roadmap to include all four sections"
```

---

### Task 2: Fix wrong citation keys for dSph constraints in Section 1.4

**Files:**
- Modify: `chapter_01/sections/1.4_indirect_detection.tex:336-337, 416-417`

**Issue:** `Ackermann:2015tah` is the *isotropic gamma-ray background* paper. The dSph stacked analysis (arXiv:1503.02641) is `Fermi-LAT:2015att`.

- [ ] **Step 1: Replace first occurrence (line 336)**

```
old: \cite{Ackermann:2015tah, Hooper:2024}.
new: \cite{Fermi-LAT:2015att, Hooper:2024}.
```

- [ ] **Step 2: Replace second occurrence (line 337)**

```
old: \cite{Ackermann:2015tah, Hooper:2024}.
new: \cite{Fermi-LAT:2015att, Hooper:2024}.
```

- [ ] **Step 3: Replace third occurrence (line 417)**

```
old: \cite{Ackermann:2015tah, Hooper:2024}.
new: \cite{Fermi-LAT:2015att, Hooper:2024}.
```

- [ ] **Step 4: Verify no remaining occurrences**

Run: `grep -n "Ackermann:2015tah" chapter_01/sections/1.4_indirect_detection.tex`
Expected: no output

- [ ] **Step 5: Commit**

```
git add chapter_01/sections/1.4_indirect_detection.tex
git commit -m "fix: correct dSph citation key from Ackermann:2015tah to Fermi-LAT:2015att in sec 1.4"
```

---

### Task 3: Fix broken cross-reference `\ref{ch:2}`

**Files:**
- Modify: `chapter_01/sections/1.4_indirect_detection.tex:466`

**Issue:** Chapter 2's label is `chap:gamma_sky`, not `ch:2`. This renders as "Chapter ??" in the PDF.

- [ ] **Step 1: Replace the reference**

```
old: Chapter~\ref{ch:2} introduces the Fermi Large Area Telescope
new: Chapter~\ref{chap:gamma_sky} introduces the Fermi Large Area Telescope
```

- [ ] **Step 2: Commit**

```
git add chapter_01/sections/1.4_indirect_detection.tex
git commit -m "fix: correct broken cross-reference ch:2 -> chap:gamma_sky in sec 1.4"
```

---

### Task 4: Fix "Part V" → "Part IV"

**Files:**
- Modify: `chapter_01/sections/1.4_indirect_detection.tex:360, 362, 462`

**Issue:** Per `outline.md`, cross-correlations (Chapter 8) are Part IV. Part V does not exist.

- [ ] **Step 1: Fix line 360**

```
old: This cross-correlation technique forms the basis of the analysis in Part~V, where
new: This cross-correlation technique forms the basis of the analysis in Part~IV, where
```

- [ ] **Step 2: Fix line 362**

```
old: the multi-pronged programme developed in Parts II through V of this thesis.
new: the multi-pronged programme developed in Parts II through IV of this thesis.
```

- [ ] **Step 3: Fix line 462**

```
old: large-scale structure (Part~V).
new: large-scale structure (Part~IV).
```

- [ ] **Step 4: Verify no remaining occurrences**

Run: `grep -n "Part~V" chapter_01/sections/1.4_indirect_detection.tex`
Expected: no output

- [ ] **Step 5: Commit**

```
git add chapter_01/sections/1.4_indirect_detection.tex
git commit -m "fix: correct Part~V -> Part~IV references in sec 1.4"
```

---

### Task 5: Replace hardcoded section numbers with `\ref{}`

**Files:**
- Modify: `chapter_01/sections/1.4_indirect_detection.tex:135, 222, 227, 232, 277`

**Issue:** Hardcoded "Section 1.4.X" strings will silently break if sections are renumbered. The `\label{sec:...}` targets already exist.

- [ ] **Step 1: Fix line 135**

```
old: The annihilation and decay rates derived in Section 1.4.1 depend directly
new: The annihilation and decay rates derived in Section~\ref{sec:ann_decay} depend directly
```

- [ ] **Step 2: Fix line 222**

```
old: the $J$-factor and $D$-factor formalism of Section 1.4.4, which combines them with the particle physics of Section 1.4.1 to produce
new: the $J$-factor and $D$-factor formalism of Section~\ref{sec:jfactor}, which combines them with the particle physics of Section~\ref{sec:ann_decay} to produce
```

- [ ] **Step 3: Fix line 227**

```
old: Combining the particle physics of Section 1.4.1 with the density profiles of Section 1.4.3, we can now write
new: Combining the particle physics of Section~\ref{sec:ann_decay} with the density profiles of Section~\ref{sec:density_profiles}, we can now write
```

- [ ] **Step 4: Fix line 232**

```
old: as discussed in Section 1.4.1.
new: as discussed in Section~\ref{sec:ann_decay}.
```

- [ ] **Step 5: Fix line 277**

```
old: the uncertainties discussed in Section 1.4.3.
new: the uncertainties discussed in Section~\ref{sec:density_profiles}.
```

- [ ] **Step 6: Verify no remaining hardcoded references**

Run: `grep -n "Section 1\.4\." chapter_01/sections/1.4_indirect_detection.tex`
Expected: no output

- [ ] **Step 7: Commit**

```
git add chapter_01/sections/1.4_indirect_detection.tex
git commit -m "fix: replace hardcoded Section 1.4.X numbers with \\ref{} in sec 1.4"
```

---

### Task 6: Number key equations in Section 1.4

**Files:**
- Modify: `chapter_01/sections/1.4_indirect_detection.tex`

**Issue:** The 4 master equations (annihilation flux, J-factor, decay flux, D-factor) use unnumbered `\[ ... \]` display math. They should be numbered for cross-referencing from later chapters. `dinostyle.sty` uses `\numberwithin{equation}{section}`, so they will be (1.4.1)–(1.4.4).

- [ ] **Step 1: Number the annihilation flux equation (line 229)**

```
old:
\[ \frac{d\Phi_\gamma}{dE\, d\Omega} = \underbrace{\frac{1}{4\pi} \frac{\langle \sigma v_\text{rel} \rangle}{2 m_\chi^2} \frac{dN_\gamma}{dE}}_{\text{Particle Physics}} \times \underbrace{J(\psi)}_{\text{Astrophysics}} \,.
\]

new:
\begin{equation}
	\frac{d\Phi_\gamma}{dE\, d\Omega} = \underbrace{\frac{1}{4\pi} \frac{\langle \sigma v_\text{rel} \rangle}{2 m_\chi^2} \frac{dN_\gamma}{dE}}_{\text{Particle Physics}} \times \underbrace{J(\psi)}_{\text{Astrophysics}} \,.
	\label{eq:flux_ann}
\end{equation}
```

- [ ] **Step 2: Number the J-factor equation (lines 235–237)**

```
old:
\[ J(\psi) = \int_\text{l.o.s.
	} \rho^2\bigl(r(s, \psi)\bigr) \, ds \,,
\]

new:
\begin{equation}
	J(\psi) = \int_\text{l.o.s.} \rho^2\bigl(r(s, \psi)\bigr) \, ds \,,
	\label{eq:jfactor}
\end{equation}
```

- [ ] **Step 3: Number the decay flux equation (line 244)**

```
old:
\[ \frac{d\Phi_\gamma}{dE\, d\Omega} = \frac{1}{4\pi} \frac{\Gamma}{m_\chi} \frac{dN_\gamma}{dE} \times D(\psi) \,, \]

new:
\begin{equation}
	\frac{d\Phi_\gamma}{dE\, d\Omega} = \frac{1}{4\pi} \frac{\Gamma}{m_\chi} \frac{dN_\gamma}{dE} \times D(\psi) \,,
	\label{eq:flux_dec}
\end{equation}
```

- [ ] **Step 4: Number the D-factor equation (lines 250–252)**

```
old:
\[ D(\psi) = \int_\text{l.o.s.
	} \rho\bigl(r(s, \psi)\bigr) \, ds \,,
\]

new:
\begin{equation}
	D(\psi) = \int_\text{l.o.s.} \rho\bigl(r(s, \psi)\bigr) \, ds \,,
	\label{eq:dfactor}
\end{equation}
```

- [ ] **Step 5: Commit**

```
git add chapter_01/sections/1.4_indirect_detection.tex
git commit -m "feat: number the four master equations (flux + J/D-factor) in sec 1.4"
```

---

### Task 7: Fix chapter label

**Files:**
- Modify: `chapter_01/chapter_1.tex:2`

**Issue:** `chap:dgrb` ("diffuse gamma-ray background") is semantically wrong for "The Dark Matter Problem." No files reference this label (grep-confirmed).

- [ ] **Step 1: Replace the label**

```
old: \label{chap:dgrb}
new: \label{ch:1}
```

- [ ] **Step 2: Commit**

```
git add chapter_01/chapter_1.tex
git commit -m "fix: rename Ch1 label from chap:dgrb to ch:1"
```

---

### Task 8: Add chapter summary section

**Files:**
- Create: `chapter_01/sections/1.5_summary.tex`
- Modify: `chapter_01/chapter_1.tex` (add `\input` line)

**Convention:** Follow Chapters 2 and 3, which use `\section{Summary}` with `\label{sec:chX_summary}` and prose paragraphs.

- [ ] **Step 1: Create the summary file**

Create `chapter_01/sections/1.5_summary.tex` with content:

```latex
% Section 1.5: Summary and Transition to Chapter 2

\section{Summary}
\label{sec:ch1_summary}

This chapter has established the theoretical and observational foundation for the dark matter searches that follow.
Multiple independent lines of evidence --- flat rotation curves in spiral galaxies, the dynamics and gravitational lensing of galaxy clusters, and the precision cosmology of the cosmic microwave background --- converge on the $\Lambda$CDM concordance model, in which roughly 85\% of the matter density is composed of cold, non-baryonic dark matter.
Big Bang Nucleosynthesis independently confirms the non-baryonic character of this component, requiring that dark matter consist of a new form of matter beyond the Standard Model.

Among the candidates proposed to fill this role, the Weakly Interacting Massive Particle stands out because of the ``WIMP miracle'': a stable particle with electroweak-scale mass and coupling, produced thermally in the early universe, naturally yields a relic abundance consistent with observation.
The thermal freeze-out calculation fixes the annihilation cross-section at $\langle \sigma v_\mathrm{rel} \rangle_\mathrm{cosmo} \approx 2.2 \times 10^{-26}$~cm$^3$/s, providing a concrete, parameter-free experimental target in the GeV--TeV mass window bracketed by the Lee--Weinberg and unitarity bounds.
The same interaction that sets the relic density can be probed from three complementary directions --- scattering in underground detectors (direct detection), production at colliders, and annihilation in astrophysical environments (indirect detection).
Among these, indirect detection via gamma-rays occupies a unique position: it directly probes the annihilation cross-section, the quantity that determines the cosmological abundance.

The $J$-factor and $D$-factor formalism developed in this chapter factorizes the predicted gamma-ray flux into a particle physics term and an astrophysical term, providing the mathematical framework that underpins every analysis in this thesis.
The current null results of WIMP searches --- with Fermi-LAT constraints from dwarf galaxies already excluding the thermal relic cross-section for masses below ${\sim}\,100$~GeV in the $b\bar{b}$ channel --- demonstrate that the era of simple signal-over-background searches is reaching its limits.
Extracting weaker signals from noise-dominated data demands the statistical and machine learning methods developed in the remainder of this thesis.
The next chapter introduces the instrument that collects the data: the Fermi Large Area Telescope and the astrophysical gamma-ray sky that constitutes both the observational setting and the primary source of systematic uncertainty for the analyses that follow.
```

- [ ] **Step 2: Add `\input` to chapter file**

In `chapter_01/chapter_1.tex`, add a new line after `\input{sections/1.4_indirect_detection.tex}`:

```
old:
\input{sections/1.4_indirect_detection.tex}

new:
\input{sections/1.4_indirect_detection.tex}
\input{sections/1.5_summary.tex}
```

- [ ] **Step 3: Commit**

```
git add chapter_01/sections/1.5_summary.tex chapter_01/chapter_1.tex
git commit -m "feat: add Chapter 1 summary section"
```

---

### Task 9: Remove closing transition from Section 1.4.7

**Files:**
- Modify: `chapter_01/sections/1.4_indirect_detection.tex:464-466`

**Issue:** With the new summary section (Task 8), the two-sentence transition to Chapter 2 at the end of Section 1.4.7 is now redundant — the summary handles the bridge.

- [ ] **Step 1: Remove the redundant transition lines**

Delete lines 464–466:

```
old:
The mathematical framework developed in this section --- the flux factorization, the $J$-factor and $D$-factor formalism, the density profiles and their uncertainties --- underpins every one of these analyses.
But before proceeding to the dark matter searches themselves, we must first understand the instrument that collects the data.
Chapter~\ref{ch:2} introduces the Fermi Large Area Telescope, whose properties --- angular resolution, effective area, point-spread function, and exposure --- determine the sensitivity of every analysis in this thesis.

new:
The mathematical framework developed in this section --- the flux factorization, the $J$-factor and $D$-factor formalism, the density profiles and their uncertainties --- underpins every one of these analyses.
```

Note: This also eliminates the broken `\ref{ch:2}` reference (Task 3 fix is no longer needed on this line since it's deleted; however, if Tasks 2–5 are committed before this task, the fix from Task 3 will already be applied to the line before it's trimmed here. Either order works.)

- [ ] **Step 2: Commit**

```
git add chapter_01/sections/1.4_indirect_detection.tex
git commit -m "refactor: remove redundant Ch2 transition from sec 1.4.7, now handled by summary section"
```

---

### Task 10: Add detection triangle figure to Section 1.3

**Files:**
- Copy: `cirelli-paper/arXiv-2406.01705v3/figs/DMdetections.pdf` → `chapter_01/figures/DMdetections.pdf`
- Modify: `chapter_01/sections/1.3_searching_for_dark_matter.tex`

**Issue:** The outline calls for a detection triangle figure showing the three Feynman diagram rotations. `DMdetections.pdf` from Cirelli et al. shows exactly this.

- [ ] **Step 1: Copy the figure**

```bash
cp cirelli-paper/arXiv-2406.01705v3/figs/DMdetections.pdf chapter_01/figures/DMdetections.pdf
```

- [ ] **Step 2: Insert figure environment after the detection triangle discussion**

Insert after line 18 (`A signal in all three would constitute an unambiguous identification.`) and before line 20 (`This section reviews each strategy in turn`):

```latex
A signal in all three would constitute an unambiguous identification.

\begin{figure}[t]
	\centering
	\includegraphics[width=0.95\textwidth]{figures/DMdetections}
	\caption{The detection triangle: three complementary strategies for detecting dark matter, each corresponding to a different reading of the same underlying interaction vertex.
		\textit{Left}: direct detection --- dark matter scatters off a Standard Model target in a laboratory.
		\textit{Center}: indirect detection --- dark matter annihilates into Standard Model particles in astrophysical environments.
		\textit{Right}: collider production --- Standard Model particles produce dark matter at accelerators.
		Figure from Cirelli et al.~\cite{Cirelli:2024ssz}.
	}
	\label{fig:detection_triangle}
\end{figure}

This section reviews each strategy in turn, with emphasis on the physical principles rather than experimental details.
```

- [ ] **Step 3: Commit**

```
git add chapter_01/figures/DMdetections.pdf chapter_01/sections/1.3_searching_for_dark_matter.tex
git commit -m "feat: add detection triangle figure (Cirelli et al.) to sec 1.3"
```

---

### Task 11: Trim GCE overlap in Section 1.3.3

**Files:**
- Modify: `chapter_01/sections/1.3_searching_for_dark_matter.tex:108-113`

**Issue:** The GCE is discussed substantively in both Section 1.3.3 (~6 lines) and Section 1.4.5 (~16 lines + figure). Trim 1.3.3 to avoid redundancy, adding a forward reference to 1.4.5.

- [ ] **Step 1: Replace lines 108–113**

```
old:
The potential of gamma-ray indirect detection is hinted at by suggestive --- if contested --- observational evidence.
The \textbf{Galactic Center} is the brightest expected dark matter target, owing to its proximity (${\sim}\,8$~kpc) and the high dark matter density predicted by cuspy halo profiles~\cite{Cirelli:2024ssz,Pinetti:2021jjs}.
Observations by the Fermi Large Area Telescope have revealed a statistically significant excess of gamma-rays between 1 and 5~GeV, extending spherically to ${\sim}\,10$--$20^\circ$ from the Galactic Center~\cite{Daylan:2014rsa,Hooper:2024}.
The spectrum and morphology are consistent with a ${\sim}\,40$--$70$~GeV dark matter particle annihilating into $b\bar{b}$ at a rate matching the thermal relic cross-section~\cite{Daylan:2014rsa,Hooper:2024}.
However, the Galactic Center is also challenged by intense and imperfectly modeled astrophysical backgrounds --- diffuse emission from cosmic ray interactions with dense gas, unresolved point sources, and past outburst activity --- and the leading alternative explanation invokes an unresolved population of millisecond pulsars in the Galactic bulge~\cite{Cirelli:2024ssz,Pinetti:2021jjs}.
The origin of this excess remains vigorously debated and is a central motivation for the analyses presented in Chapter~\ref{ch:4}.

new:
The potential of gamma-ray indirect detection is underscored by the most debated anomaly in the field: the \textbf{Galactic Center excess} (GCE), a statistically significant excess of GeV-scale gamma-rays from the inner Galaxy whose spectrum and morphology are consistent with dark matter annihilation but also with an unresolved population of millisecond pulsars~\cite{Daylan:2014rsa,Cirelli:2024ssz}.
We discuss the GCE in detail in Section~\ref{sec:targets}, after developing the density profile and $J$-factor formalism needed to interpret it quantitatively; the dedicated analysis is presented in Chapter~\ref{ch:4}.
```

- [ ] **Step 2: Commit**

```
git add chapter_01/sections/1.3_searching_for_dark_matter.tex
git commit -m "refactor: trim GCE discussion in sec 1.3.3 to avoid overlap with sec 1.4.5"
```

---

### Task 12: Fix H II formatting

**Files:**
- Modify: `chapter_01/sections/1.1_evidence_for_dark_matter.tex:21`

**Issue:** `H\textsc{ii}` should be `H\,\textsc{ii}` (thin space per astronomical convention).

- [ ] **Step 1: Add thin space**

```
old: tracing approximately 70 H\textsc{ii} regions
new: tracing approximately 70 H\,\textsc{ii} regions
```

- [ ] **Step 2: Commit**

```
git add chapter_01/sections/1.1_evidence_for_dark_matter.tex
git commit -m "fix: add thin space in H II notation per astronomical convention"
```

---

## Execution Order

Tasks 1–5 and 7 are independent single-file edits that can be executed in parallel or in any order. Tasks 6 and 9 also edit `1.4_indirect_detection.tex` and should be sequenced after Tasks 2–5 to avoid merge conflicts. Task 8 depends on Task 7 (chapter label) and Task 9 (removing redundant transition). Tasks 10–12 are independent.

Recommended serial order: **1 → 2 → 3 → 4 → 5 → 6 → 7 → 9 → 8 → 10 → 11 → 12**

## Verification

After all tasks are complete:

1. **Grep checks** — confirm no remaining issues:
   - `grep -rn "Part~V" chapter_01/sections/` → no output
   - `grep -rn "Ackermann:2015tah" chapter_01/sections/` → no output
   - `grep -rn "Section 1\.4\." chapter_01/sections/*.tex` → no output
   - `grep -rn "\\\\ref{ch:2}" chapter_01/sections/` → no output
   - `grep -rn "chap:dgrb" chapter_01/` → no output

2. **Compile** — run `latexmk -pdf main.tex` and check:
   - No "??" undefined references in Chapter 1
   - Chapter 1 introduction mentions all four sections
   - Detection triangle figure renders in Section 1.3
   - Equations (1.4.1)–(1.4.4) appear numbered in Section 1.4
   - Summary section appears at the end of Chapter 1
   - No LaTeX warnings about multiply-defined or undefined labels
