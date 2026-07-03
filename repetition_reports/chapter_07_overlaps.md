# Chapter 7 — Intra-Chapter Overlap Report

## Sections analyzed / excluded

**Analyzed (narrative, wrapper order):**
- `chapter_07/sections/7.0_introduction.tex` (chapter intro, untitled)
- `chapter_07/sections/7.1_limits_of_threshold.tex` (§7.1, incl. §7.1.1 `sec:catalog_paradigm`, §7.1.2 `sec:info_below_threshold`)
- `chapter_07/sections/7.2_population_to_spatial.tex` (§7.2, incl. §7.2.1 `sec:simulated_sky`, §7.2.2 `sec:frequentist_framework`)

**Reference only (paper subtree, NOT edited/flagged for edits):**
`chapter_07/paper_dnds_catalog/sections/{introduction,data_selection,statistical_framework,results,conclusions}.tex`

**Excluded:** `7.3_transition_to_paper.tex` (orphan, not built — see Section C); `7.4_paper_dnds_catalog.tex` (standalone paper wrapper).

---

## A. Narrative-vs-narrative overlaps  [PRIMARY]

### A1. `dN/dS` extends as ~S⁻² to roughly 50× below detection threshold — Severity: High
Same headline fact restated in all three narrative sections, twice with the numeric flux.
- Occurrence 1: `7.0_introduction.tex` · chapter intro · ~line 5 — "extends as $\sim S^{-2}$ down to fluxes roughly 50 times below the nominal detection threshold"
- Occurrence 2: `7.1_limits_of_threshold.tex` · §7.1.2 · ~line 38 — "extends as $\sim S^{-2}$ down to fluxes of approximately $5 \times 10^{-12}~\mathrm{cm}^{-2}\,\mathrm{s}^{-1}$, roughly 50 times below the nominal catalog sensitivity in the $1$--$10~\mathrm{GeV}$ band"
- Occurrence 3: `7.2_population_to_spatial.tex` · §7.2.1 · ~line 18 — "extends to fluxes roughly 50 times below the Fermi-LAT detection threshold (cf.\ Section~\ref{sec:source_count})"
- Recommendation: KEEP-primary in 7.1.2 (with the number); CONDENSE→xref in 7.0 (one-line preview is fine) and in 7.2.1 (replace restated number with a bare cross-reference — 7.2.1 already carries the `cf.` pointer, so drop the re-stated "50 times below").

### A2. `dN/dS` is one-dimensional / statistical — "how many, not where" — Severity: High
Near-verbatim thesis-of-the-chapter statement, plus its paired rhetorical question.
- Occurrence 1: `7.0_introduction.tex` · chapter intro · ~line 6 — "the $dN/dS$ is a one-dimensional flux distribution: it tells us \emph{how many} sources exist at each flux, but it says nothing about \emph{where} any specific source is located"
- Occurrence 2: `7.2_population_to_spatial.tex` · §7.2 intro · ~line 8 — "The $dN/dS$ is, however, a purely statistical quantity: it tells us how many sources exist at each flux level, but nothing about where they are."
- Occurrence 3 (reinforcement): `7.2_population_to_spatial.tex` · §7.2.1 · ~line 18 — "yet it carries no spatial content whatsoever"
- Paired framing question also duplicated: 7.0 ~line 7 "whether this population-level statistical knowledge can be turned into spatial information" vs 7.2.1 ~line 19 "whether this population-level flux distribution can be leveraged to identify specific sky directions".
- Recommendation: KEEP-primary in 7.0 (it is the chapter's motivating hook); CONDENSE→xref the 7.2 restatement — 7.2 can open straight into the *how* rather than re-establishing the *what*.

### A3. Use `dN/dS` as a generative model for synthetic skies + frequentist comparison — Severity: Medium
The core-method sentence is stated in the intro and then twice inside 7.2.
- Occurrence 1: `7.0_introduction.tex` · chapter intro · ~line 10 — "use the recovered $dN/dS$ as a generative model for ensembles of synthetic skies, enabling a frequentist statistical comparison that identifies candidate source directions below the detection threshold"
- Occurrence 2: `7.2_population_to_spatial.tex` · §7.2 intro · ~line 11 — "use the recovered $dN/dS$ as a generative model for synthetic skies and then compare their pixel-level TS distributions with the real \textit{Fermi}-LAT sky using a frequentist test"
- Occurrence 3: `7.2_population_to_spatial.tex` · §7.2.1 · ~line 22 — "If the $dN/dS$ is known, one can use it as a generative model to produce realistic synthetic skies."
- Recommendation: KEEP-primary in 7.2 (this is where the method is developed); CONDENSE the 7.0 sentence to a lighter preview, and collapse the 7.2-intro (line 11) and 7.2.1 (line 22) restatements into one (they say the same thing two paragraphs apart).

### A4. Sub-threshold populations (blazars, misaligned AGN, star-forming galaxies) feed the unresolved/isotropic emission — Severity: Medium
- Occurrence 1: `7.0_introduction.tex` · chapter intro · ~line 5 — "a population of sub-threshold point sources --- blazars, star-forming galaxies, misaligned active galactic nuclei --- that contribute to the isotropic diffuse emission but remain individually undetected"
- Occurrence 2: `7.1_limits_of_threshold.tex` · §7.1.2 · ~line 35 — "blazars, misaligned active galactic nuclei, star-forming galaxies, and millisecond pulsars all contribute to this unresolved emission, and their aggregate flux may account for a large fraction of the unresolved gamma-ray background"
- Recommendation: KEEP-primary in 7.1.2 (fuller, cited, adds MSPs and the budget caveat); CONDENSE→xref the source-class list in 7.0 to avoid pre-empting the same enumeration one page later.

### A5. Fermi-LAT's locally-fitted (RoI) TS carries spatially varying significance, versus a globally coherent TS — Severity: Medium
The "local TS is position-dependent, ours is global" contrast is made in 7.1 and then twice in 7.2.
- Occurrence 1: `7.1_limits_of_threshold.tex` · §7.1.1 · ~lines 21–23 — "the same numerical TS value carries different statistical weight at different sky positions … The resulting detection scale is therefore spatially inhomogeneous"
- Occurrence 2: `7.2_population_to_spatial.tex` · §7.2.2 · ~line 55 — "Unlike the TS used by the \textit{Fermi}-LAT collaboration, which is computed locally in each region of interest and therefore carries spatially varying significance, the TS adopted here is a single, globally coherent quantity"
- Occurrence 3: `7.2_population_to_spatial.tex` · §7.2.2 · ~line 67 — "the globally homogeneous TS scale --- in contrast to the \textit{Fermi}-LAT catalog's locally computed TS"
- Recommendation: KEEP-primary the problem statement in 7.1.1 and the first contrast in 7.2.2 (line 55); CONDENSE→xref the third mention (line 67), which re-explains the same contrast within the same subsection before the cross-correlation point.

### A6. Cross-correlation as the downstream use case — larger sample worth a sub-leading spurious fraction — Severity: Medium
- Occurrence 1: `7.1_limits_of_threshold.tex` · §7.1.2 · ~lines 41–42 — "Cross-correlation studies between gamma-ray maps and galaxy catalogs … gain statistical power from a larger sample of source directions, even at the price of a moderate false-positive fraction (cf.\ Chapter~\ref{ch:8})"
- Occurrence 2: `7.2_population_to_spatial.tex` · §7.2.1 · ~line 44 — "cross-correlation studies (Chapter~\ref{ch:8}) --- where the relevant quantity is the number and angular distribution of candidate source directions, not the properties of individual sources"
- (also touched at 7.2.2 ~line 67 and 7.0 ~line 15)
- Recommendation: CONDENSE→xref. Pick one home for the "larger sample tolerates false positives → cross-correlation" argument (naturally 7.1.2, where the motivation lives) and let the 7.2 mentions be short pointers to Chapter 8.

### A7. High-TS agree / low-TS diverge → divergence point sets the probing depth — Severity: Medium
Restated across the two subsections of 7.2 in almost the same words.
- Occurrence 1: `7.2_population_to_spatial.tex` · §7.2.1 · ~lines 30–32 — "At high TS, where bright sources dominate, the synthetic and real distributions agree well. As one moves to lower TS values, the simulated distributions eventually diverge … The threshold at which this divergence becomes statistically significant determines how deep below the nominal catalog limit the method can reliably probe."
- Occurrence 2: `7.2_population_to_spatial.tex` · §7.2.2 · ~lines 58–59 — "At high $\mathrm{TS}^\star$, where bright sources dominate, the distributions agree; as $\mathrm{TS}^\star$ is lowered, background systematics cause them to diverge, setting the depth to which the method can probe."
- Recommendation: MERGE. The qualitative statement in 7.2.1 and the KS-specific statement in 7.2.2 are the same sentence; keep the quantitative one in 7.2.2 and trim 7.2.1 to the firing-pixel definition it introduces.

*(Low-severity note: chapter-roadmap / "full details in the paper body" signposting is repeated — 7.0 ~line 14, 7.2 ~lines 12–13, 7.2 ~line 71. Expected signposting, but 7.2 says "Full details appear in the paper body" twice within four lines (lines 11 and 13); collapse to one.)*

---

## B. Narrative-vs-paper over-anticipation  [FLAG ONLY]

### B1. Full synthetic-sky generation procedure re-derived in the narrative — Severity: High
The narrative reproduces the paper's map-construction recipe step by step (flux draws from `dN/dS`, expected number = integral over bin, Poisson actual number, uniform random positions, PSF convolution, exposure multiplication, pixelization on diffuse background, 5000 realizations, Gaussian-Process uncertainty sampling).
- Narrative: `7.2_population_to_spatial.tex` · §7.2.1 · ~lines 22–26 — "source fluxes are drawn from the $dN/dS$, with the expected number of sources per flux bin given by the integral of $dN/dS$ over that bin and the actual number drawn from a Poisson distribution … these synthetic sources are placed at uniformly random positions on the sphere. Each synthetic sky is then processed through the same pipeline … convolved with the Fermi-LAT PSF, multiplied by the exposure map, and converted into a pixelized photon-count map … By repeating this procedure 5000 times … within the uncertainties estimated via Gaussian Process interpolation"
- Paper covers in full: `paper_dnds_catalog/sections/data_selection.tex` (§`sec:catalog:models`, esp. ~lines 90–96: `\mathcal{M}` construction, Poisson-per-bin, uniform positions, 5000 realisations, Gaussian-Process variation) and `statistical_framework.tex`.
- Recommendation: CONDENSE→paper (narrative only; paper untouched). The narrative should convey the *idea* ("draw fluxes from `dN/dS`, scatter sources at random positions, push through the same instrument pipeline, repeat many times") and defer the per-bin Poisson / exposure / GP mechanics to the paper.

### B2. Frequentist machinery (per-pixel TS, KS two-sample test, Quality Factor) formalized in the narrative — Severity: Medium
§7.2.2 defines the three quantities with paper-level specificity, including the QF as "the fraction of the 5000 synthetic realizations passing the KS test at a given $\mathrm{TS}^\star$ and significance level $\alpha$" and the KS test "above a minimum threshold $\mathrm{TS}^\star$". This is the paper's definition set.
- Narrative: `7.2_population_to_spatial.tex` · §7.2.2 · ~lines 54–64 (per-pixel TS ~54–56; KS above $\mathrm{TS}^\star$ ~58–59; QF definition ~62–64).
- Paper covers in full: `paper_dnds_catalog/sections/statistical_framework.tex` (TS eq. `eq:catalog:TS` and "signal interest label" ~lines 25–34; two-sample KS with $\alpha \in \{0.01,0.05,0.1\}$ ~lines 52–53; quality factor definition ~line 57).
- Note: the narrative explicitly signposts deferral ("Full details appear in the paper body"), so this is borderline — the *concept preview* is expected. Flagged because the QF is given a full operational definition rather than a preview, and the author's own `\aure{check again the definition of the QF}` (line 61) signals the definition is being pinned down here rather than in the paper.
- Recommendation: CONDENSE→paper (narrative only). Preview the trio conceptually; leave the exact QF definition and the $\alpha$ grid to `statistical_framework.tex`.

### B3. TS as a "signal interest label" with meaning drawn from simulations — Severity: Low
- Narrative: `7.2_population_to_spatial.tex` · §7.2.2 · ~line 56 — "treated as a heuristic ``signal interest label'' whose probabilistic meaning comes entirely from the comparison with simulated skies, not from an assumed analytic distribution"
- Paper covers in full: `paper_dnds_catalog/sections/statistical_framework.tex` · ~line 34 — "we use it as a ``signal interest label'', and derive a probabilistic interpretation for it from simulations of synthetic maps"
- Recommendation: CONDENSE→paper (narrative only). Near-verbatim of a paper phrase; a brief nod suffices in the narrative.

### B4. Pixel-resolution / firing-pixel multiplicity detail (Nside=512 ≈ 0.12°, one source→many pixels, many sources→one pixel) — Severity: Low
- Narrative: `7.2_population_to_spatial.tex` · §7.2.2 · ~line 68 — "at the chosen pixel resolution ($N_\mathrm{side} = 512$, corresponding to $\sim 0.12^\circ$), a single astrophysical source may produce multiple adjacent firing pixels due to PSF spreading, and conversely, multiple faint sources may contribute to a single pixel"
- Paper covers in full: `paper_dnds_catalog/sections/statistical_framework.tex` · ~lines 61–63 (source-vs-firing-pixel distinction, $N_\mathrm{side}=1024$ simulation vs $512$ analysis, ≈0.12° matching LAT resolution).
- Recommendation: CONDENSE→paper (narrative only). The conceptual point (firing pixels ≠ sources) is worth previewing; the specific $N_\mathrm{side}$ values belong to the paper.

---

## C. Structural notes / borderline cases

- **Orphaned file `7.3_transition_to_paper.tex`.** This file exists (2757 bytes, `\section{Transition to the Paper}`, `\label{sec:transition_catalog}`) but is **not built**: the wrapper `chapter_7.tex` only `\input`s `7.0`, `7.1`, `7.2`, and (conditionally) `7.4_paper_dnds_catalog`. It is therefore dead prose in the current build. Note for the author: it contains concrete result numbers (~9,600 vs ~6,700 firing pixels, ~50% increase; recovery saturating above ~2×10⁻¹⁰ cm⁻² s⁻¹; >97% background-robustness; gPCS/Zenodo pointer) that overlap heavily with the paper `results.tex`/`conclusions.tex`. Since it is unbuilt, it was excluded from the Section A/B analysis per instructions; either wire it in (and then re-run overlap detection, as it would add fresh narrative-vs-paper duplication) or delete it.

- **PCAT digression flagged by the author.** `7.2_population_to_spatial.tex` §7.2.1 ~lines 35–39 carries `\aure{idk if I want to keep this part}` above a detailed PCAT comparison (transdimensional MCMC, ~250 CPU hours, 40°×40° North-Galactic-Pole patch). This is **not** paper over-anticipation — the live paper introduction mentions PCAT only in passing (and inside a `\begin{comment}` block), so the detail is narrative-original, not duplicated. Recorded here only because it is an open author decision, not an overlap.

- **4FGL construction detail in §7.1.1 is not paper duplication.** The RoI/TS>25/4σ/1750-RoIs exposition (`7.1` ~lines 14–23) and the DR3 dropped-source episode (~lines 45–49) are background motivation; the integrated paper's live text does not develop them (its detailed 4FGL prose is commented out). No B flag; legitimate pedagogical scene-setting.

- **`\aure{}` WIP markers present** in 7.2 (`idk if I want to keep this part`, `check again the definition of the QF`) — left in place per house style; not overlaps, but they intersect B1/B2 (the QF marker sits exactly on the over-anticipated definition).
