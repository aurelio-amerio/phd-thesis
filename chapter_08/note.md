# Chapter 8 — Design Notes

## Design Decision Summary

**Approach**: Funnel (Why → What → Where)  
**Budget**: ~10 pages for sections 8.0–8.3, followed by the inserted Paper 5  
**Formalism depth**: Conceptual — all equations live in Section 3.5 (to be expanded with Paper 5's Appendix B content)  
**Narrative arc**: Parts II–III searched for DM in resolved targets and characterized unresolved populations → the UGRB contains DM emission from unresolved halos/subhalos → cross-correlations exploit the anisotropy of this emission to separate it from astrophysical sources → CTAO is the future instrument

## Key Structural Decision

> [!IMPORTANT]
> Section 3.5 will absorb the full cross-correlation formalism from the paper's Appendix B (Limber approximation, window functions, HOD, noise terms). This means Chapter 8 sections can be **entirely physics-driven** with zero new equations, cross-referencing Section 3.5 for all math. The paper's Appendix B can then be removed from the inserted paper.

---

## Physics Corrections (from brainstorming)

### dN/dS Framing

The ML-based dN/dS search (Chs. 6–7) does **not** use a "different observable" to probe dark matter. It is a study at a different *scope*: characterizing the aggregate astrophysical source population regardless of origin. dN/dS recovery and probabilistic cataloging are **prerequisites** for DM searches — they map the landscape in which any DM contribution must hide — but they are not DM search methods themselves.

### DM Signal Physics

The dark matter signal targeted by cross-correlations originates from **unresolved individual halos and subhalos** across cosmic epochs, not a "smooth diffuse glow." These structures form the hierarchical cosmic web:
- DM annihilation/decay occurs in every halo and subhalo at all redshifts
- The resulting gamma-ray emission inherits the **spatial anisotropies** of the underlying matter distribution
- For annihilation, the signal scales as ρ², making it concentrated in the densest structures and peaked at low redshift (z < 0.1)
- The signal contains angular correlations that can be decomposed into 1-halo (within a single structure) and 2-halo (between different structures) terms
- These anisotropies have a different angular, spectral, and redshift signature than astrophysical sources — this is the discriminating handle

---

## Relationship to Other Chapters

| Element | Where it lives | Chapter 8 action |
|---|---|---|
| APS formalism (C_ℓ, Limber, window functions) | Section 3.5.1 | Cross-reference |
| SNR, Δχ² test statistic | Section 3.5.2 | Cross-reference |
| HOD formalism, beam functions, noise terms | Section 3.5 (to be expanded) | Cross-reference |
| UGRB definition | Section 2.2 (IGRB/GDE) | Brief recap in 8.1.2 |
| DM halo profiles, J-factor | Section 1.4 | Brief recap in 8.1.2 |
| 1-halo / 2-halo decomposition | Section 3.5.1 | Cross-reference in 8.2.2 |
| Blazar/MSP/SFG populations | Section 2.2 | Brief recap in 8.1.2 |
| Paper's Appendix B (full derivations) | → To be absorbed into Section 3.5 | Removed from paper |

---

## Section 3.5 Expansion (separate task)

The current Section 3.5 already covers: spherical harmonic decomposition, APS definition, Limber approximation, window functions (annihilation, decay, astrophysical), 1-halo/2-halo decomposition, SNR and Δχ².

To absorb Paper 5's Appendix B, Section 3.5 would additionally need:
- Beam window function B_ℓ (from PSF)
- Photon noise C_N and galaxy shot noise C_{N_g} (currently mentioned but could be expanded)
- HOD parameterization (Eqs. B21–B22 of the paper)
- EBL attenuation details
- Astrophysical source window functions (unresolved blazars HSP/LISP)

---

## Note on Auto-Correlation vs. Cross-Correlation

(See also `note_on_autcorr.md`)

The key insight: gamma-ray maps are 2D projections that lack distance information. A bright pixel could be a nearby faint source or a distant luminous one. Auto-correlation measures the total "clumpiness" of the gamma-ray sky but cannot distinguish *where* the fluctuations originate in redshift.

Cross-correlating with a galaxy catalog of known redshift distribution effectively "assigns a redshift" to the gamma-ray fluctuations. Because the cross-power spectrum depends on the overlap of the two window functions W_γ(z) and W_g(z), choosing a catalog that peaks at z < 0.1 isolates the low-redshift component of the gamma-ray emission — exactly where DM annihilation is strongest.

This is why 2MASS is the "golden channel": it maps the local universe where DM signal is maximized and astrophysical blazars are mostly already resolved by Fermi-LAT.
