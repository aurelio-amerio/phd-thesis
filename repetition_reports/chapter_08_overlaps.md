# Chapter 8 — Intra-Chapter Overlap Report

## Sections analyzed / excluded

**Analyzed (narrative, wrapper order):**
- `chapter_08/sections/8.0_introduction.tex` (§8.0, untitled intro)
- `chapter_08/sections/8.1_from_resolved_to_cosmic_web.tex` (§8.1 "Dark Matter in the Cosmic Web")
- `chapter_08/sections/8.2_cross_correlation_technique.tex` (§8.2 "The Cross-Correlation Technique", subsec. 8.2.1–8.2.3)
- `chapter_08/sections/8.3_ctao.tex` (§8.3 "The Cherenkov Telescope Array Observatory", subsec. 8.3.1–8.3.2)

**Read as reference only (paper subtree, `chapter_08/paper_xcorr/sections/`):** `introduction.tex` (body commented out), `cross_correlation_signal.tex`, `sensitivity_forecast.tex`, `cherenkov_telescope_array.tex`, `conclusions.tex`, `appendix_formalism.tex`, `appendix_further_results.tex`, `appendix_offsource.tex`. Never edited; used only to locate full coverage for Section B.

**Excluded:** `chapter_08/sections/8.4_paper_xcorr.tex` (standalone paper wrapper).

Note on the paper introduction: `paper_xcorr/sections/introduction.tex` has its body **commented out** with an explicit note ("the pedagogical introduction in Sections 8.0–8.3 … covers all the same material in greater depth"). Introductory/conceptual overlap with that file is therefore by design and is NOT flagged in Section B. Section B flags only where the narrative reproduces in heavy detail what an **active** paper body/appendix section still derives in full.

---

## A. Narrative-vs-narrative overlaps  [PRIMARY]

### A1. "Dark matter annihilates inside every gravitationally bound structure" — Severity: Medium (near-verbatim, 2 sections)
- Occurrence 1: `8.0_introduction.tex` · §8.0 · ~line 12 — "In fact, if dark matter annihilates or decays, it does so inside every gravitationally bound structure across all cosmic epochs, and the accumulated, unresolved emission from this entire population would contribute to the \UGRB."
- Occurrence 2: `8.1_from_resolved_to_cosmic_web.tex` · §8.1 · ~line 40 — "If dark matter is a particle that annihilates, it could do so not just in our galaxy, but also inside every gravitationally bound structure across the universe."
- Recommendation: CONDENSE→xref. The §8.1 opening restates the intro sentence almost verbatim. Keep the §8.0 framing (KEEP-primary intro), and let §8.1 open from the "how is matter distributed" question without re-asserting the same premise.

### A2. "ρ² scaling ⇒ DM window peaks sharply at z ≲ 0.1" — Severity: High (stated 4× across 2 sections, incl. 3× within §8.1)
- Occurrence 1: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~line 49 — "The gamma-ray flux from dark matter annihilation is proportional to the square of the local dark matter density. Dense, compact structures are therefore the dominant contributors…"
- Occurrence 2: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~line 70 — "The dark matter annihilation signal peaks at low redshift (because the flux is proportional to $\rho^2$ and thus weights dense, nearby structures more heavily)…"
- Occurrence 3: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~line 75 — "$W_\gamma^\mathrm{DM}(z)$ … is sharply peaked at $z < 0.1$ due to the $\rho^2$ density scaling of the annihilation rate."
- Occurrence 4: `8.2_cross_correlation_technique.tex` · §8.2.1 · ~lines 21–22 — "The $\rho^2$ scaling makes the signal dominated by the late-time collapse of matter into dense halos and subhalos… $W_\gamma^\mathrm{DM}$ peaks sharply at $z \lesssim 0.1$ and decays rapidly thereafter…"
- Recommendation: CONDENSE→xref. State the ρ²→low-z-peak mechanism once as physics in §8.1.2 (KEEP-primary), collapse the two §8.1 restatements, and have §8.2.1 reference it (the §8.2.1 restatement is redundant with §8.1 beyond the formula it needs).

### A3. Blazar redshift distribution + EBL horizon numbers ("z ~ 0.3–0.4/0.5 at 50 GeV; z ≲ 0.1–0.2 above 1 TeV") — Severity: High (same numbers in all 3 physics sections)
- Occurrence 1: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~line 71 — "the blazar window function --- whose redshift distribution peaks at $z \sim 0.3$--0.4 --- mostly does not [overlap]." (also ~line 79: "spread over $z \sim 0.1$--0.4")
- Occurrence 2: `8.2_cross_correlation_technique.tex` · §8.2.1 · ~lines 25–26 — "Unresolved blazars … have their emission peak at $z \sim 0.3$--$0.5$ at $50\,\mathrm{GeV}$. … above ${\sim}\,1\,\mathrm{TeV}$, the observable volume contracts to $z \lesssim 0.1$--$0.2$…" (restated in the §8.2.3 blue block, ~line 99: "above roughly $1\,\mathrm{TeV}$, pair production on the EBL shrinks the gamma-ray horizon to $z \lesssim 0.1$--$0.2$")
- Occurrence 3: `8.3_ctao.tex` · §8.3.1 · ~lines 26 & 29 — "EBL absorption becomes significant above $\sim 1$~TeV, attenuating photons from sources at $z \gtrsim 0.1$--$0.2$…" and "EBL attenuation pushes their window functions, which peak at $z \sim 0.3$--$0.4$ at 50~GeV, down to $z \sim 0.1$--$0.2$ above 1 TeV."
- Recommendation: CONDENSE→xref. This blazar-window / EBL-horizon fact is the chapter's most-repeated quantitative statement. Keep the full quantitative version in §8.2.1 (KEEP-primary, where Fig. window_main is discussed), and reduce §8.1.2, the §8.2.3 blue block, and §8.3.1 to a cross-reference plus the one new point each section actually adds (§8.3.1's added point is only that blazars therefore remain a background at TeV).

### A4. Cross-correlation noise cancellation: populations that don't cluster with local galaxies drop out — Severity: Medium
- Occurrence 1: `8.0_introduction.tex` · §8.0 · ~line 18 — "…it vanishes for astrophysical source populations at redshifts incompatible with the tracer, but is maximal for dark matter emission that clusters with local structure."
- Occurrence 2: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~line 68 — "Any source population that does not cluster with the selected galaxies cancels out of the cross-power spectrum, leaving only the gamma-ray emission that traces the same structures."
- Occurrence 3: `8.2_cross_correlation_technique.tex` · §8.2.2 · ~line 59 — "The high-redshift blazar population does not correlate with a local galaxy catalog, so their 1-halo Poisson term does not appear in $C_\ell^{\gamma g}$."
- Recommendation: CONDENSE→xref. §8.0 (intro preview) is expected; the substantive duplication is §8.1.2 vs §8.2.2, which state the same cancellation principle. Keep §8.2.2 (KEEP-primary, mechanistic) and trim the §8.1.2 statement to a forward pointer.

### A5. Spectral degeneracy: energy information alone cannot separate DM from blazars — Severity: Medium
- Occurrence 1: `8.0_introduction.tex` · §8.0 · ~line 14 — "…requires more than spectral information alone, since distinct source classes partially overlap in energy."
- Occurrence 2: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~lines 54–55 — "The key challenge is spectral degeneracy. At energies accessible to \textit{Fermi}-LAT … the spectra of heavy WIMPs and certain blazar populations overlap enough that energy information alone cannot distinguish them." (reinforced ~line 58: "A purely spectral analysis of the UGRB therefore constrains combinations…")
- Recommendation: CONDENSE→xref. §8.0 preview is expected; §8.1.2 is the KEEP-primary development. Overlap is light enough that this is borderline Low/Medium — flagged because both explicitly frame "spectral information alone is insufficient."

### A6. "Unresolved blazars account for ~20–30% of the UGRB intensity" — Severity: Medium (same number, 2 sections)
- Occurrence 1: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~line 51 — "unresolved blazars dominate at high energies and account for about 20--30\% of the total intensity…"
- Occurrence 2: `8.2_cross_correlation_technique.tex` · §8.2.3 · ~line 82 — "Although unresolved blazars may account for roughly 20--30\% of the total UGRB intensity integrated over all redshifts~\cite{Ajello:2015mfa}…"
- Recommendation: CONDENSE→xref. Keep the number where the argument uses it (§8.2.3, where the point is that this fraction is z ≳ 0.3 and thus suppressed locally — KEEP-primary). In §8.1.2 the figure is stated only in passing; a cross-reference suffices.

### A7. 2MASS / 2MRS as the low-z (z ≲ 0.1) optimal catalog — Severity: Medium (restated 3–4× within §8.2, plus §8.1)
- Occurrence 1: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~line 76 — "Local galaxy catalogs such as 2MASS, covering $z \lesssim 0.1$--0.2, have window functions that follow this peak."
- Occurrence 2: `8.2_cross_correlation_technique.tex` · §8.2.1 · ~line 31 — "A dense, shallow catalog covering $z \lesssim 0.1$ such as the Two Micron All-Sky Survey (2MASS) overlaps nicely with the DM annihilation window function…"
- Occurrence 3: `8.2_cross_correlation_technique.tex` · §8.2.3 · ~lines 75–77 — "dense, all-sky surveys covering the local universe (z$<$0.1-0.2) are desirable… The Two Micron All-Sky Survey (2MASS) … peaking at $z \approx 0.072$…" (restated again in the §8.2.3 blue block, ~lines 97–98: "the case for 2MASS and 2MRS … trace the local universe at $z \lesssim 0.1$")
- Recommendation: CONDENSE→xref / MERGE. §8.2.3 is the dedicated catalog subsection and should be KEEP-primary. The §8.2.1 introduction of 2MASS and the §8.2.3 blue-block re-introduction ("These shallow surveys trace the local universe at $z \lesssim 0.1$") re-state what §8.2.3 already establishes; merge the redundant low-z framing.

### A8. Star-forming galaxies / misaligned AGN negligible at high (TeV) energies — Severity: Low
- Occurrence 1: `8.2_cross_correlation_technique.tex` · §8.2.1 · ~line 27 — "Star-forming galaxies trace the cosmic star-formation rate and dominate at much higher redshifts, $z \sim 1$--$3$."
- Occurrence 2: `8.3_ctao.tex` · §8.3.1 · ~line 28 — "At energies above 20~GeV and increasingly toward the TeV regime, star-forming galaxies and misaligned AGN contribute negligibly to the unresolved background."
- Recommendation: CONDENSE→xref. Light thematic overlap; the §8.3.1 statement can cross-reference §8.2.1 rather than re-assert the SFG/mAGN suppression independently.

### A9. Auto- vs cross-correlation: DM buried under blazar Poisson shot noise in the auto-spectrum — Severity: Medium
- Occurrence 1: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~lines 63–66 — "The auto-correlation power spectrum, however, suffers from a fundamental limitation: the signal from dark matter is always mixed with the shot noise and correlated fluctuations of astrophysical sources… Cross-correlating the gamma-ray map with an external gravitational tracer resolves both limitations at once…"
- Occurrence 2: `8.2_cross_correlation_technique.tex` · §8.2.2 · ~lines 52–56 — "The gamma-ray auto-correlation power spectrum $C_\ell^{\gamma\gamma}$ is dominated by the Poisson shot noise of unresolved blazars at essentially all multipoles… covering any diffuse DM component."
- Recommendation: CONDENSE→xref. §8.1.2 anticipates the full auto-vs-cross argument that §8.2.2 then develops in detail. Keep §8.2.2 (KEEP-primary); reduce the §8.1.2 passage to a one-line forward pointer ("as developed in §8.2.2").

_(A10 candidate — CTAO order-of-magnitude angular-resolution / large-collecting-area claim in §8.0 line 22 vs §8.3.1 lines 8 & 22 — judged an EXPECTED intro→body preview and left unflagged, except see C2 for the within-§8.3 duplication.)_

---

## B. Narrative-vs-paper over-anticipation  [FLAG ONLY]

### B1. CTAO instrument specification (three telescope types, fields of view, energy range, generational gain over H.E.S.S./MAGIC/VERITAS) — Severity: Medium–High
- Narrative: `8.3_ctao.tex` · §8.3.1 · ~lines 21–22 — "…the Large-Sized Telescopes (LSTs, … field of view $4.3^\circ$), the Medium-Sized Telescopes (MSTs, field of view $7.5^\circ$--$7.7^\circ$), and the Small-Sized Telescopes (SSTs, fields of view $8.8^\circ$…). … \CTAO covers a broad energy range from 20~GeV up to 300~TeV, with an angular resolution and sensitivity that improve by an order of magnitude over current-generation IACTs, such as HESS, MAGIC, and VERITAS."
- Paper covers in full: `paper_xcorr/sections/cherenkov_telescope_array.tex` (§CTA, ~lines 111–117: identical LST/MST/SST split, same FoV values 4.3° / 7.5–7.7° / 8.8°, same 20 GeV–300 TeV range, same order-of-magnitude claim over H.E.S.S./MAGIC/VERITAS).
- Recommendation: CONDENSE→paper (narrative only; paper untouched). The active paper §CTA re-derives these specs in full; the §8.3.1 hardware inventory largely duplicates it. Trim the narrative to the qualitative points needed for the cross-correlation motivation (ground-based IACT, atmosphere-as-calorimeter, TeV reach), leaving the exact FoV/telescope-class enumeration to the paper.

### B2. EGAL survey parameters (quarter-sky footprint, |b|>5°, 15%/400 h South + 10%/600 h North = ~1000 h, 3° pointing grid, 0.51 h/1.11 h per pointing, ~3 h effective exposure, ~10% exposure fluctuation) — Severity: High
- Narrative: `8.3_ctao.tex` · §8.3.2 · ~lines 38–43 — "The EGAL survey targets about a quarter of the sky, covering the region defined by $-90^\circ < l < 90^\circ$ and $|b| > 5^\circ$… the Southern array will observe 15\% of the sky with 400 hours, while the Northern array will cover the remaining 10\% with 600 hours, for a total observation time of approximately 1000 hours… a grid of telescope pointings spaced by approximately $3^\circ$… observed for 0.51 hours in the south and 1.11 hours in the north, yielding an effective average exposure of approximately 3 hours… keeping the relative fluctuations in the exposure map to approximately 10\%…"
- Paper covers in full: `paper_xcorr/sections/cherenkov_telescope_array.tex` (§CTA "The Extra-Galactic survey" + "Simulating survey observations", ~lines 123–127 and ~line 142: same footprint $-90^\circ<l<90^\circ$, $b>5^\circ$; same 15%/400 h + 10%/600 h ≈ 1000 h; same ~3° grid; same 0.51 h / 1.11 h; same ~3 h effective exposure; same ~10% exposure variation).
- Recommendation: CONDENSE→paper (narrative only; paper untouched). This is near-verbatim numeric duplication of an active paper section. The chapter narrative can summarize the survey qualitatively ("~quarter-sky, ~uniform ~3 h exposure over three years") and defer the full pointing/exposure numbers to the paper via cross-reference.

### B3. Off-source data scenario (~50 h per point, ~25× the EGAL exposure, factor-~4 sensitivity gain) — Severity: Medium
- Narrative: `8.3_ctao.tex` · §8.3.2 · ~lines 47–49 — "…the accumulated off-source data collected through years of CTAO pointed observations… these off-source data sum to an effective exposure of approximately 50 hours per sky location --- roughly 25 times larger than the nominal EGAL exposure --- yielding a factor of $\sim 4$ improvement in sensitivity compared to the 3-hour scenario."
- Paper covers in full: `paper_xcorr/sections/cherenkov_telescope_array.tex` (§CTA "Off-source data scenario", ~lines 165–167: ~50 h/point, same MAGIC→CTAO extrapolation) and `paper_xcorr/sections/appendix_offsource.tex` (App. expo: derives the ~25× / ~50 h figure and the exposure distribution).
- Recommendation: CONDENSE→paper (narrative only; paper untouched). The narrative already points to App. expo; it can state the scenario in one sentence and drop the "~25×" and "factor ~4" quantitatives to the paper/appendix that derive them.

### B4. Explicit DM annihilation window-function expression — Severity: Medium
- Narrative: `8.2_cross_correlation_technique.tex` · §8.2.1 · ~line 20 — "For dark matter annihilation, it is proportional to $\langle\sigma v\rangle\,\Delta^2(z)\,\left(\Omega_\mathrm{DM}\rho_c/m_\chi\right)^2\,(1+z)^3\,e^{-\tau(E,z)}$, where $\Delta^2(z)$ is the flux multiplier…"
- Paper covers in full: `paper_xcorr/sections/cross_correlation_signal.tex` (§formalism, ~lines 53–54: the ⟨σv⟩ / m_χ⁻² scaling and flux-multiplier factor) and `paper_xcorr/sections/appendix_formalism.tex` (App. model / app:WDM, full DM window-function derivation).
- Recommendation: CONDENSE→paper (narrative only; paper untouched). Borderline — a qualitative "W^DM ∝ ⟨σv⟩ and ∝ ρ², weighted to low z" would carry the argument; reproducing the full proportionality with the (1+z)³ e^{-τ} factors anticipates the appendix derivation. Reduce the narrative to the qualitative dependence and cite App. model.

_(Considered but NOT flagged: the variance/noise-term discussion in §8.2.2 ~lines 42–50 references Eqs. `variance_cross`/`variance_auto` and the 1-halo/2-halo split — it stays conceptual and defers the equations to the paper/appendix, so it is appropriate anticipation rather than heavy duplication.)_

---

## C. Structural notes / borderline cases

- **C1. §8.2 intra-section restatement.** Beyond the cross-section clusters above, §8.2 restates its own core low-z-overlap argument at each subsection boundary: §8.2.1 (~lines 31–34), the §8.2.3 opening (~line 75), and the §8.2.3 blue block (~lines 97–99) each re-assert "2MASS/2MRS trace z ≲ 0.1 where the DM signal peaks." This is signposting drift more than new content; a single statement in §8.2.3 with back-references would tighten the section. (Covered numerically under A7.)

- **C2. §8.3 intra-section restatement of "quarter of the sky / uniform exposure."** Stated in the §8.3 opener (~line 8, "cover a quarter of the sky with approximately uniform exposure"), again at §8.3.2 opening (~line 34, "large sky maps with approximately uniform exposure"), and again at §8.3.2 ~line 38 ("targets about a quarter of the sky"). Similarly the "order-of-magnitude angular resolution over Fermi-LAT" appears at §8.3 ~line 8 and §8.3.1 ~line 22. Low severity (same section, scene-setting), but the opener could defer specifics to the subsections.

- **C3. Blue `\blue{…}` and `\aure{…}` markers.** Several flagged passages sit inside `\blue{}` blocks (§8.2.3 ~lines 97–99; §8.3.1 ~lines 28–29; §8.3.2 ~lines 47–50) and the chapter ends with `\aure{follows the paper}` (§8.3 ~line 59), indicating these are still WIP/under-revision — consistent with the overlaps in A3/A7/B3 being introduced by recent additions that duplicate settled prose.

- **C4. Intro (§8.0) previews are, on the whole, appropriately scoped.** The recap of prior chapters (~lines 4–8) and the three-section roadmap (~line 22) are expected intro material and were not flagged, except where the §8.1 opening re-states the intro's central premise near-verbatim (A1).
