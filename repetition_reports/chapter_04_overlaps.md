# Chapter 4 — Intra-Chapter Overlap Report

## Sections analyzed / excluded

**Analyzed (narrative, wrapper order):**
- `4.0_introduction.tex`
- `4.1_discovery_and_characterization.tex` (§4.1, incl. 4.1.1–4.1.4)
- `4.2_msp_hypothesis.tex` (§4.2, incl. 4.2.1–4.2.2)
- `4.3_systematics_stalemate.tex` (§4.3, incl. 4.3.1–4.3.3)
- `4.4_breaking_the_stalemate.tex` (§4.4)

**Read as reference only (paper leaves, `paper_msp/sections/`):** `introduction.tex`, `fermi_data_analysis.tex`, `luminosity_function.tex`, `msps_in_globular_clusters.tex`, `comparisons.tex`, `implications_gce.tex`, `summary_conclusions.tex`, `appendix_comparison.tex`.

**Excluded:** `4.2_competing_interpretations.old`, `4.5_paper.tex`, `paper_msp/tables/*`, numeric tables (`appendix_tables.tex`).

---

## A. Narrative-vs-narrative overlaps  [PRIMARY]

### A1. Macias/Bartels "boxy/X-shaped stellar bulge" morphology finding — Severity: **High**
Nearly verbatim restatement of the same result (near-IR stellar-mass maps → bulge template fits GCE better than NFW) in two different sections.
- Occurrence 1: `4.2_msp_hypothesis.tex` · §4.2.1 · ~lines 36–41 — "Macias et al. \ argued that the GCE spatial distribution is better described by the stellar mass of the Milky Way's boxy/X-shaped bulge than by a spherically symmetric NFW profile ... Using near-infrared maps ... they found that a bulge template absorbed the excess emission with a statistically better fit than the NFW template. ... Bartels et al. ... found that the GCE traces the stellar mass distribution in the inner Galaxy"
- Occurrence 2: `4.3_systematics_stalemate.tex` · §4.3.2 · ~lines 53–54 — "a series of analyses beginning with Macias et al. and Bartels et al. challenged this picture by arguing that the GCE traces the boxy, X-shaped stellar bulge ... Using near-infrared stellar mass maps as spatial templates, these studies found that the stellar bulge template absorbed the GCE flux with a statistically better fit than a standard NFW profile"
- Recommendation: **KEEP-primary in §4.3.2 / CUT-secondary in §4.2.1** (or CONDENSE→xref). §4.3.2 is where the morphological ambiguity is the actual subject; §4.2.1 can name the bulge-morphology claim in one sentence and defer the near-IR/template-fit mechanics to §4.3.2. (Note §4.2.1 currently frames it as *evidence for* MSPs, §4.3.2 as *contested*; preserve that framing distinction when condensing.)

### A2. Systematics triad — "interstellar emission model / masking / Fermi Bubbles" — Severity: **Medium**
The same boilerplate list of the three dominant inner-Galaxy systematics is recited three times.
- Occurrence 1: `4.3_systematics_stalemate.tex` · §4.3 opener · ~line 8 — "The choice of interstellar emission model, the treatment of the Fermi Bubbles at low latitudes, the masking of known point sources, and the parameterization of the source-count function at the faint end each contribute irreducible systematic uncertainties"
- Occurrence 2: `4.3_systematics_stalemate.tex` · §4.3.2 · ~line 57 — "Whether the GCE prefers an NFW or bulge morphology can shift depending on the interstellar emission model adopted, the masking procedure applied to the Galactic plane and known point sources, and how the Fermi Bubbles emission is treated at low latitudes"
- Occurrence 3: `4.4_breaking_the_stalemate.tex` · §4.4 opener · ~line 7 — "the results depend sensitively on the adopted interstellar emission model, masking procedure, and treatment of the Fermi Bubbles"
- Recommendation: **CONDENSE→xref.** The §4.4 opener (Occ. 3) is a transition and may retain a brief version, but should point back rather than re-enumerate the identical triad already stated at the head of §4.3 and again in §4.3.2. Consider stating the triad once (§4.3 opener) and referring to it thereafter.

### A3. GCE "established properties" restate §4.1.2 measurements — Severity: **Medium**
The spectral and morphological numbers first delivered in §4.1.2 (as the Calore/Daylan results) are re-listed almost verbatim in §4.1.3 as the "established properties," including the same figures.
- Occurrence 1 (spectrum): `4.1_discovery_and_characterization.tex` · §4.1.2 · ~line 75 — "it consistently displayed a peak at 1--3~GeV, a steep rise at sub-GeV energies, and a falling power-law tail with index $\sim -2.7$ above the peak"
- Occurrence 2 (spectrum): `4.1_discovery_and_characterization.tex` · §4.1.3 · ~lines 86–88 — "The spectrum of the GCE displays a pronounced peak at energies of 1--3~GeV. Below the peak, the emission rises steeply ... Above the peak, the spectrum follows a power-law tail with index $\sim -2.7$"
- Occurrence 1 (morphology): §4.1.2 · ~line 58 — "approximately spherically symmetric, centered within $\sim 0.05^\circ$ of Sgr~A$^*$, and extending to at least $\sim 10^\circ$"
- Occurrence 2 (morphology): §4.1.3 · ~lines 92–95 — "approximately spherically symmetric ... the centroid of the emission lies within $\sim 0.05^\circ$ of the position of Sgr~A$^*$ ... out to at least $\sim 10^\circ$"
- Occurrence (robustness/60 models): §4.1.2 ~line 75 (60 models, flux "less than a factor of two to three") vs §4.1.3 ~line 101 ("persists across all 60 diffuse models ... flux above 1~GeV varying by less than a factor of a few")
- Recommendation: **MERGE / CONDENSE.** §4.1.3 is by design a synthesis subsection, so *some* recap is warranted, but the near-identical re-listing of peak/tail/centroid/extent/60-models is redundant. Trim §4.1.3 to the *consensus* framing (what all groups agree on, incl. the origin-agnostic point at lines 100–104) and drop the re-quoted numbers already in §4.1.2, or vice versa.

### A4. "Missing bright pulsars" luminosity-function argument — Severity: **Medium**
The core empirical anti-MSP argument (known LF ⇒ Fermi should have resolved many; only a handful/three seen) is developed in §4.2.2 and then again, quantitatively, in §4.4, with a preview already in §4.0.
- Occurrence 1: `4.2_msp_hypothesis.tex` · §4.2.2 · ~lines 66–70 — "Fermi should have already detected dozens of MSPs from the GCE population, yet only a handful of candidates have been identified ... This 'missing bright pulsars' problem represents one of the strongest empirical challenges"
- Occurrence 2: `4.4_breaking_the_stalemate.tex` · §4.4 · ~lines 28–31 — "Fermi-LAT's source catalogs should contain $N_\mathrm{MSP} \sim 17{-}37$ individually resolved pulsars ... Only three MSP candidates have been identified in this region"
- Preview: `4.0_introduction.tex` · ~line 15 — "their expected number based on known luminosity functions substantially exceeds the handful of candidates identified in current catalogs"
- Recommendation: **KEEP-primary in §4.4 / CONDENSE→xref in §4.2.2.** §4.2.2 should state the argument at the review level (Hooper & Linden, Holst & Hooper: known LF ⇒ resolved sources expected) and defer the quantitative 17–37-vs-3 statement to §4.4/the paper, rather than previewing the paper's headline in §4.2.2 line 70 *and* re-deriving it in §4.4.

### A5. NPTF "Poissonian vs point-source photon statistics" explanation — Severity: **Low**
The conceptual basis of NPTF is explained in §4.2.1 and re-explained (briefly) at the head of §4.3.1.
- Occurrence 1: `4.2_msp_hypothesis.tex` · §4.2.1 · ~lines 25–26 — "a smooth dark matter halo produces Poissonian photon counts in each pixel (the variance equals the mean), a population of faint point sources introduces additional variance through localized photon clusters"
- Occurrence 2: `4.3_systematics_stalemate.tex` · §4.3.1 · ~line 15 — "the Non-Poissonian Template Fitting (NPTF) framework, which exploits the difference in photon statistics between smooth (Poissonian) emission and populations of unresolved point sources"
- Recommendation: **CONDENSE→xref** (low priority). Occurrence 2 is a legitimate one-line recap; acceptable as signposting. Flagged only for completeness.

### A6. Intro preview of the DM-consistency case / basic GCE numbers — Severity: **Low**
`4.0` previews the three-lines-of-agreement and thermal-relic argument that §4.1.4 delivers in full, plus the peak/extent/cross-section numbers repeated in §4.1.
- Occurrence 1: `4.0_introduction.tex` · ~lines 9–11 — "peaks at energies between roughly 1 and 3~GeV, extends out to at least 10 degrees ... consistent with the signal predicted from the annihilation of $\sim 40$--$70$~GeV dark matter ... best-fit annihilation cross section, $\langle \sigma v \rangle \sim (1$--$2) \times 10^{-26}$ ... compatible with the canonical thermal relic value"
- Occurrence 2: `4.1_discovery_and_characterization.tex` · §4.1.4 · ~lines 122–132 — full treatment of spectrum/morphology/normalization convergence and the thermal-relic coincidence
- Recommendation: **KEEP** (legitimate funnel-structure previewing per house style). No action; listed to document that this is expected, not a defect.

---

## B. Narrative-vs-paper over-anticipation  [FLAG ONLY]

### B1. §4.4 reproduces the paper's headline results in full detail — Severity: **Medium**
§4.4 is a transition/motivation section, but ~lines 22–31 restate the paper's actual measured results — detection counts, sample sizes, and best-fit luminosity-function numbers — that the integrated paper then presents in full.
- Narrative: `4.4_breaking_the_stalemate.tex` · §4.4 · ~lines 22–26 — "we measured the gamma-ray luminosity function of MSPs across the Milky Way's globular cluster system using 15.8 years of Fermi-LAT data. We detected statistically significant gamma-ray emission from 56 of the 157 known globular clusters, 8 of which had not appeared in previous source catalogs. By fitting the observed gamma-ray luminosities of 87 clusters ... a mean pulsar luminosity of $\langle L_\gamma \rangle \sim (1{-}8) \times 10^{33}$~erg/s ... with a log-normal width $\sigma_L \sim 1.4{-}2.8$"
- Narrative (implication numbers): §4.4 · ~lines 29–30 — "$N_\mathrm{MSP} \sim 17{-}37$ individually resolved pulsars ... Only three MSP candidates have been identified"
- Paper covers in full: `paper_msp/sections/introduction.tex` (final paragraph, lines 52–53: 157 clusters, 56 detected, 8 new, $\langle L_\gamma\rangle\sim(1-8)\times10^{33}$, $N_\mathrm{MSP}\sim17-37$); `paper_msp/sections/fermi_data_analysis.tex` (56 detections, 15.8 yr, 8 new); `paper_msp/sections/luminosity_function.tex` ($\sigma_L\sim1.4-2.7$, 87 clusters, fit procedure); `paper_msp/sections/implications_gce.tex` (17–37 vs three candidates); `paper_msp/sections/summary_conclusions.tex` (same headline numbers).
- Recommendation: **CONDENSE→paper** (narrative only; paper untouched). A transition section legitimately motivates and can name the *conclusion* ("we measure a LF consistent with the Galactic Plane, implying Fermi should have resolved many more than the three seen"), but the specific detection counts (56/157, 8 new), the 87-cluster fit, and the numeric LF parameters duplicate what the immediately following paper presents in full. Reduce §4.4 to the qualitative result + one-line pointer to §\ref{sec:msp_paper}. NOTE: keep §4.4's *unique* content — the old-age/globular-cluster logic bridging to List et al. (§4.3.3) — which is the section's real narrative job.

### B2. "Old bulge stars ⇒ faint MSPs; globular clusters are equally old, so they test this" argument — Severity: **Low**
The central physical motivation of the paper is stated in §4.4 and appears verbatim-in-spirit throughout the paper.
- Narrative: `4.4_breaking_the_stalemate.tex` · §4.4 · ~lines 17–20 — "One natural explanation is that the Galactic Bulge formed its stars early, so its pulsars are very old ... becoming intrinsically dimmer. Globular clusters test this hypothesis directly: their stellar populations are comparably old to the Bulge"
- Paper covers in full: `paper_msp/sections/introduction.tex` ~line 48; `paper_msp/sections/implications_gce.tex` ~line 18; `paper_msp/sections/summary_conclusions.tex` ~line 9.
- Recommendation: **CONDENSE→paper** (low priority; borderline). This is the section's legitimate motivating hook, so keeping a compact statement is reasonable; flagged only because the paragraph is close in content and length to the paper's own framing. If §4.4 is trimmed per B1, fold this into the same condensation.

---

## C. Structural notes / borderline cases

- **Numeric inconsistency — NPTF near-threshold source count.** §4.2.1 (~line 30) states Lee et al. estimated "$\sim 400$ near-threshold sources could account for the entire excess within $10^\circ$," whereas §4.3.3 (~line 86) states "the 2016 NPTF preferred approximately 200." Both refer to `Lee:2015fea`. Not repetition per se, but the two numbers for the same result may read as inconsistent to a careful reader; worth reconciling (region-of-interest / definition difference should be made explicit if both are kept).

- **Predicted-detections figure stated three ways.** The number of MSPs Fermi should have resolved is given as "dozens" (§4.2.2 ~line 67, Holst & Hooper), and "17–37" (§4.2.2 ~line 70 preview and §4.4 ~line 29, this work). The paper itself uses "10–35" (Galactic-Plane LF, `introduction.tex` line 46) and "17–37" (globular-cluster LF). The variants are individually correct but land close together; ensure the distinction between the Galactic-Plane-LF prediction and the globular-cluster-LF prediction is clear wherever both appear.

- **Legitimate xrefs (no action).** §4.3.2 (~line 51) recaps the §4.1.3 morphology with an explicit "As discussed in Section~\ref{sec:4.1.3}"; §4.4 (~lines 33–34) recaps List et al. with "As discussed in Section~\ref{sec:4.3.3}." These are correctly signposted backward references and are the desired connective-tissue style, not redundancy — noted to distinguish them from the A-cluster overlaps above.

- **§4.0 line 4 is wrapped in `\red{...}` and carries an `\aure{}` WIP note** ("Review this introduction when I finalize"), so some intro/preview overlap (A6) is expected to be revisited by the author regardless.
