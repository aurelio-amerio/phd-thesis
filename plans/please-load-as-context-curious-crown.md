# Plan: Revise Section 2.1 — Gamma-Ray Production Mechanisms

## Context

Section 2.1 (`chapter_02/sections/2.1_production_mechanisms.tex`) is well-structured but has six concrete issues identified in Review Mode annotations and `\aure{}` inline comments:

1. Hadronic and leptonic subsections are too technically dense for a non-astrophysics PhD thesis
2. `fig:pp_cross_section` is never cited or discussed in the text
3. `fig:ics_cross_section` is never cited or discussed in the text
4. `fig:energy_loss_coefficients` is never cited or discussed in the text
5. The template decomposition paragraph doesn't mention that the Fermi collaboration uses this procedure to produce the official `gll_iem_v07` galactic foreground template
6. The closing forward-reference paragraph contains factual inaccuracies about how diffuse emission uncertainties propagate to downstream chapters

**Approach B** (localized redraft): redraft the two zones being most touched (hadronic subsection, closing paragraph) for clean prose; add figure-anchoring sentences surgically elsewhere; leave the rest of the section intact.

---

## File to Modify

`chapter_02/sections/2.1_production_mechanisms.tex`

---

## Issue-by-Issue Actions

### Issue 1 — Light trim of technical density

**Hadronic subsection** — cut the isobaric model / Breit-Wigner / Feynman scaling paragraph (currently lines 29–35). This is the passage beginning "Modeling the pion production spectrum accurately requires combining different theoretical frameworks..." through "...widely adopted in current gamma-ray analyses \cite{Kafexhiu:2014cua}." The Kafexhiu citation should be retained where the pp cross-section figure is discussed (see Issue 2 below).

**Leptonic subsection** — compress the radiation field density paragraph (currently line 95, beginning "In practice, cosmic-ray electrons in the local interstellar medium encounter..."). Replace the three numerical rows (starlight ρ, IR ρ, CMB ρ with temperatures) with a brief qualitative statement that the dominant ICS target shifts from optical/IR to the CMB at higher electron energies due to Klein-Nishina suppression. Keep the qualitative conclusion; remove the specific energy density numbers.

**Keep**: Thomson formula, kinematic pion threshold, pion bump derivation, KN transition discussion — these anchor figures or recur in later chapters.

---

### Issues 2–4 — Integrate uncited figures into text

**`fig:pp_cross_section`** (hadronic subsection): After the sentence about the pion bump being "conclusively observed in both supernova remnants and the Galactic Plane emission", add 1–2 sentences pointing to the figure. The text should note that the figure shows the energy-dependent inclusive π⁰ cross section across the primary cosmic-ray regime, and cite Kafexhiu:2014cua there. This replaces the Kafexhiu citation that was in the cut paragraph.

**`fig:ics_cross_section`** (ICS subsection, Klein-Nishina paragraph): Add 1–2 sentences anchoring the KN suppression discussion to this figure. The text should note that the figure illustrates how the cross section drops below the Thomson value and peaks sharply near E_γ ≈ E_e at high electron energies.

**`fig:energy_loss_coefficients`** (GDE model subsection): After the sentence about ICS overtaking bremsstrahlung at high latitudes (currently line 130), add 1–2 sentences pointing to this figure. The text should note it shows the energy- and position-dependent balance between ionization, bremsstrahlung, ICS, and synchrotron as a function of Galactic radius.

---

### Issue 5 — Add gll_iem_v07 mention

In the template decomposition paragraph (currently lines 142–144), after describing the fitting procedure (linear combination of GALPROP templates + point sources + isotropic component), add a sentence explicitly noting that the Fermi collaboration applies this exact procedure to produce the official `gll_iem_v07` Galactic interstellar emission model, which is the standard foreground template used in Fermi-LAT analyses.

---

### Issue 6 — Reframe closing forward-reference paragraph

Redraft lines 147–155 with a clean, general forward-reference. Do not go into per-chapter technical detail. The key points to convey:

- Imperfect IEM modeling is a standing systematic uncertainty that enters all analyses in the thesis to varying degrees.
- Handling the Galactic foreground properly is a necessary condition to avoid biasing results — none of the analyses presented fully eliminates this problem.
- The statistical and ML methods developed in later chapters are designed to operate *robustly despite* these foreground uncertainties, not to eliminate them.
- Do not claim IEM mismodeling "directly induces a dataset shift" in any specific chapter — the relationship is more nuanced.
- Do not call any method in the thesis a "classifier" — the subhalo search (Ch. 5) uses quantification learning.
- Mention Ch. 4, Ch. 5, and Ch. 6 as chapters where foreground handling is a relevant concern, without over-specifying the mechanism in each.

Remove all `\aure{}` comment macros that correspond to resolved issues.

---

## Verification

1. Compile with `latexmk main.tex` — check for LaTeX errors and unresolved references
2. Grep for `\ref{fig:pp_cross_section}`, `\ref{fig:ics_cross_section}`, `\ref{fig:energy_loss_coefficients}` — all three must now appear in the body text
3. Grep for remaining `\aure{}` macros in the file — only non-addressed annotations (if any) should remain
4. Read the closing paragraph and verify chapter references against the mapping: Ch. 4 = GCE (Paper 3), Ch. 5 = subhalo ML (Paper 4), Ch. 6 = dN/dS SBI (Paper 1)
