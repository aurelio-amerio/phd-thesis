# Chapter 2 — Intra-Chapter Overlap Report

## Sections analyzed / excluded

**Analyzed in full (wrapper order):**
- `2.0_introduction.tex` — chapter opening (§2.0, untitled)
- `2.1_production_mechanisms.tex` — §2.1 Gamma-Ray Production Mechanisms (§2.1.1 Hadronic, §2.1.2 Leptonic, §2.1.3 GDE Model)
- `2.2_astrophysical_sky.tex` — §2.2 The Astrophysical Gamma-Ray Sky (§2.2.1 Galactic Sources, §2.2.2 Extragalactic Sources)
- `2.3_fermi_lat.tex` — §2.3 The Fermi Large Area Telescope (§2.3.1 Instrument Overview, §2.3.2 IRFs, §2.3.3 Data Products and Catalogs)
- `2.4_summary.tex` — §2.4 Summary

**Excluded:** None. Chapter 2 has no integrated paper subtree and no `.old`/`.backup` files.

---

## A. Narrative-vs-narrative overlaps  [PRIMARY]

### A1. Template decomposition of the sky as "linear combination of diffuse + isotropic + point sources"  — Severity: Medium (with a near-verbatim isotropic-component phrase, locally High)
The description of the observed sky as a linear combination of Galactic diffuse templates, a spatially-uniform isotropic component, and individual point sources is set up twice — once as the GDE modeling procedure, once as the catalog-construction likelihood. The isotropic-component clause is near-verbatim.
- Occurrence 1: `2.1_production_mechanisms.tex` · §2.1.3 · ~line 135 — "fit to a linear combination of: the GALPROP-derived $\pi^0$-decay, ICS, and bremsstrahlung templates; a catalog of individually resolved point sources; ... and a spatially uniform isotropic component representing the combined extragalactic background and residual instrumental contamination."
- Occurrence 2: `2.3_fermi_lat.tex` · §2.3.3 · ~line 106 — "modeled as a linear combination of spatial and spectral templates: the highly structured Galactic diffuse emission, a spatially uniform isotropic component capturing the extragalactic background and residual instrumental noise, and individual point sources each parametrized by a position and spectral model."
- Recommendation: CONDENSE→xref. Both are legitimate in context (2.1 = foreground/GDE model with free normalizations; 2.3 = maximum-likelihood catalog detection with TS). Keep 2.3's likelihood formulation as the primary technical treatment and shorten 2.1's sentence to state the template set and cross-reference §2.3.3 for the fitting framework — or vice versa. At minimum, the duplicated "spatially uniform isotropic component ... extragalactic background and residual instrumental [contamination/noise]" clause should appear in only one place.

### A2. Galactic Diffuse Emission as the dominant foreground and largest source of systematic uncertainty  — Severity: Medium
The GDE's status as the brightest component and the leading systematic in Fermi-LAT analyses is asserted in §2.1.3 (with full quantitative detail) and re-asserted in §2.2.1 and the summary.
- Occurrence 1: `2.1_production_mechanisms.tex` · §2.1.3 · ~line 139 — "Imperfect modeling of the interstellar emission remains the largest single source of systematic uncertainty in gamma-ray astrophysics, introducing errors between 15\% and 30\% depending on the energy range."
- Occurrence 2: `2.2_astrophysical_sky.tex` · §2.2.1 · ~line 17 — "The Galactic Diffuse Emission dominates the observed sky and, as discussed in Section~\ref{sec:gde_model}, its template-based modeling remains the largest source of systematic uncertainty in Fermi-LAT analyses."
- (Also `2.4_summary.tex` · §2.4 · ~line 8 — "the Galactic Diffuse Emission is the dominant foreground whose imperfect modeling introduces systematic uncertainties in every Fermi-LAT measurement.")
- Recommendation: Mostly acceptable — §2.2.1 already carries an explicit `\ref{sec:gde_model}` cross-reference, and the summary line is legitimate recap. No cut needed, but confirm §2.2.1 does not re-derive; as written it correctly defers. Keep §2.1.3 as KEEP-primary (it holds the 15–30% number). Flagged for awareness rather than action.

### A3. The gamma-ray sky as a three-component superposition (diffuse foreground + resolved point sources + isotropic extragalactic background)  — Severity: Low
The same tripartite framing of the sky opens the chapter, reopens §2.2, and closes the chapter.
- Occurrence 1: `2.0_introduction.tex` · §2.0 · ~line 4 — "dominated by diffuse emission that traces the interstellar gas ..., punctuated by thousands of individual point sources, and underlaid by a faint, isotropic extragalactic glow."
- Occurrence 2: `2.2_astrophysical_sky.tex` · §2.2 · ~lines 8–10 — "this emission falls into two domains. The Galactic sky is dominated by the diffuse foreground ... and populated by Galactic gamma-ray sources ... The extragalactic sky ... is characterized by an isotropic background arising primarily from unresolved active galactic nuclei and star-forming galaxies."
- (Also `2.4_summary.tex` · §2.4 · ~line 7 — "a superposition of hadronic and leptonic diffuse emission ..., thousands of individually resolved point sources ... and a faint, nearly isotropic extragalactic background.")
- Recommendation: KEEP. This is legitimate signposting (intro preview) and recap (summary); the §2.2 opener re-states it as a section roadmap rather than re-deriving. No action required — noted for completeness of the three-way echo.

---

## B. Narrative-vs-paper over-anticipation  [FLAG ONLY]

N/A — Chapter 2 has no integrated paper.

---

## C. Structural notes / borderline cases

**Within-section repetition in §2.3 (not cross-section, so not an A-cluster).** Three instrument figures are stated twice inside `2.3_fermi_lat.tex`:
- Field of view ~2.4 sr and near-uniform sky exposure every ~3 hours: §2.3.1 ~lines 48–49 ("large field of view of approximately 2.4~sr at 1~GeV" / "every two orbits---approximately three hours") echoed in §2.3.2 ~lines 88–89 ("large 2.4~sr field of view" / "nearly uniform full-sky exposure every three hours").
- Peak effective area ~9,500 cm²: §2.3.1 ~line 50 ("peak effective area of $\sim$9,500~cm$^2$ at normal incidence") echoed in §2.3.2 ~lines 84–85 ("peak effective area of $\sim$9,500~cm$^2$").
These are arguably intentional (the effective-area/acceptance subsection legitimately reuses the numbers it is explaining), but the FoV + 3-hour-exposure pairing reads as mild déjà vu. Consider trimming the §2.3.1 mentions to a forward pointer, since §2.3.2 develops acceptance properly. Borderline; left to author.

**Within-section repetition in §2.1.1.** The pion-bump peak energy $m_{\pi^0}/2 \approx 67.5$ MeV is stated twice within a few lines (~line 43 rest-frame photon energy, ~line 45 the $E^2 dN/dE$ peak). This is a deliberate physical build-up (single-decay kinematics → population-level spectral feature), not redundancy. No action.

**Summary (§2.4) recaps are appropriately concise.** The MSP–WIMP spectral degeneracy (full treatment §2.2.1 ~lines 27–28 → recap §2.4 ~line 8), the PSF-driven source-confusion limit (full §2.3.2 ~lines 63–64 → recap §2.4 ~line 11), the TS>25 resolved/unresolved partition (full §2.3.3 ~lines 111–113 → recap §2.4 ~line 12), and the "~one third unassociated 4FGL sources = DM-subhalo search pool" point (full §2.3.3 ~lines 130–132 → recap §2.4 ~line 13) all appear once in full detail and once as a one-line summary echo. These are textbook intro/summary signposting and are correctly NOT flagged as A-clusters per the calibration rule.

**Well-managed cross-references (positive note).** The hadronic SFG mechanism in §2.2.2 (~line 72) explicitly defers to §2.1.1 ("as described in Section~\ref{sec:hadronic}") instead of re-deriving pion production, and §2.2.1 defers the GDE-systematic claim to §2.1.3. These are the model for how the softer overlaps above (A1, A2) should be handled.
