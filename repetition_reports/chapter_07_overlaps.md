# Chapter 7 — Intra-Chapter Overlap Report

> **Verification pass (2026-07-03).** All entries verified against the current `.tex` sources by a fresh-context referee; every "~line" matched the actual file exactly, all B entries confirmed accurate and correctly scoped. Changes: A2's cut target disambiguated (trim §7.2.1 lines 18–19, keep the §7.2 intro recap); A4 and A6 downgraded to Low (A6 → KEEP); A7's merge direction reversed (keep §7.2.1, condense §7.2.2); two new entries added (A8, A9). **Editing-order note:** A2, A3, A5, A7, B1–B4, A9 all land in `7.2_population_to_spatial.tex` — apply the B1/B2 condensations first (they remove the most text), then resolve the A-level duplicates against the shortened file, or line references will drift.

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
- Verification: CONFIRMED — all three quotes verbatim; note all *three* occurrences carry the "roughly 50 times" quantitative factor (not just two).
- Recommendation: KEEP-primary in 7.1.2 (with the number). In 7.0, keep the qualitative hook ("extends as $\sim S^{-2}$ well below the nominal detection threshold") and drop only the "roughly 50 times" factor — the intro should not lose the shape of the result. In 7.2.1, the `cf.\ Section~\ref{sec:source_count}` pointer already carries the load: delete "roughly 50 times below the Fermi-LAT detection threshold" and keep "extends well below the detection threshold (cf.\ ...)".

### A2. `dN/dS` is one-dimensional / statistical — "how many, not where" — Severity: High
Near-verbatim thesis-of-the-chapter statement, plus its paired rhetorical question.
- Occurrence 1: `7.0_introduction.tex` · chapter intro · ~line 6 — "the $dN/dS$ is a one-dimensional flux distribution: it tells us \emph{how many} sources exist at each flux, but it says nothing about \emph{where} any specific source is located"
- Occurrence 2: `7.2_population_to_spatial.tex` · §7.2 intro · ~line 8 — "The $dN/dS$ is, however, a purely statistical quantity: it tells us how many sources exist at each flux level, but nothing about where they are."
- Occurrence 3 (reinforcement): `7.2_population_to_spatial.tex` · §7.2.1 · ~line 18 — "yet it carries no spatial content whatsoever"
- Paired framing question also duplicated: 7.0 ~line 7 "whether this population-level statistical knowledge can be turned into spatial information" vs 7.2.1 ~line 19 "whether this population-level flux distribution can be leveraged to identify specific sky directions".
- Verification: CONFIRMED (all quotes exact).
- Recommendation (disambiguated at verification): KEEP-primary in 7.0 (the chapter's motivating hook). The cut target is **7.2.1 lines 18–19**, which re-establish the *what* four sentences after the §7.2 intro (lines 8–9) already did — the §7.2 intro's line 8 is the section's legitimate one-line recap and should stay. Suggested replacement for `7.2:18–19`: *"Since the $dN/dS$ carries no spatial content (Section~\ref{sec:threshold_limits}), the question is how to leverage it to identify specific sky directions likely to host sub-threshold sources."*

### A3. Use `dN/dS` as a generative model for synthetic skies + frequentist comparison — Severity: Medium
The core-method sentence is stated in the intro and then twice inside 7.2.
- Occurrence 1: `7.0_introduction.tex` · chapter intro · ~line 10 — "use the recovered $dN/dS$ as a generative model for ensembles of synthetic skies, enabling a frequentist statistical comparison that identifies candidate source directions below the detection threshold"
- Occurrence 2: `7.2_population_to_spatial.tex` · §7.2 intro · ~line 11 — "use the recovered $dN/dS$ as a generative model for synthetic skies and then compare their pixel-level TS distributions with the real \textit{Fermi}-LAT sky using a frequentist test"
- Occurrence 3: `7.2_population_to_spatial.tex` · §7.2.1 · ~line 22 — "If the $dN/dS$ is known, one can use it as a generative model to produce realistic synthetic skies."
- (Fourth echo *noted at verification*: `7.2:51` — "The $dN/dS$ enters as a generative model for the synthetic skies, not as a Bayesian prior" — adds genuinely new content (frequentist-vs-Bayesian framing) and should be KEEP (no action); recorded so it isn't swept up in the collapse.)
- Verification: CONFIRMED (lines 10, 11, 22).
- Recommendation: KEEP-primary in 7.2 (this is where the method is developed); CONDENSE the 7.0 sentence to a lighter preview. When collapsing occ. 2/3: keep `7.2:11` as the section roadmap sentence (it doubles as signposting) and let 7.2.1 open at line 23's mechanics rather than re-stating the idea at line 22.

### A4. Sub-threshold populations (blazars, misaligned AGN, star-forming galaxies) feed the unresolved/isotropic emission — Severity: Low (downgraded from Medium at verification)
- Occurrence 1: `7.0_introduction.tex` · chapter intro · ~line 5 — "a population of sub-threshold point sources --- blazars, star-forming galaxies, misaligned active galactic nuclei --- that contribute to the isotropic diffuse emission but remain individually undetected"
- Occurrence 2: `7.1_limits_of_threshold.tex` · §7.1.2 · ~line 35 — "blazars, misaligned active galactic nuclei, star-forming galaxies, and millisecond pulsars all contribute to this unresolved emission, and their aggregate flux may account for a large fraction of the unresolved gamma-ray background"
- Verification: the 7.0 instance is a three-item apposition inside the intro's scene-setting sentence; 7.1.2 carries the citations, the MSP addition, and the budget caveat. This is a repeated enumeration, not a twice-explained concept.
- Recommendation (revised): KEEP-primary in 7.1.2. The 7.0 instance is acceptable as-is under the signposting allowance; optionally trim the apposition to "a population of sub-threshold point sources that contribute to the isotropic diffuse emission but remain individually undetected" — optional polish, not a required cut.

### A5. Fermi-LAT's locally-fitted (RoI) TS carries spatially varying significance, versus a globally coherent TS — Severity: Medium
The "local TS is position-dependent, ours is global" contrast is made in 7.1 and then twice in 7.2.
- Occurrence 1: `7.1_limits_of_threshold.tex` · §7.1.1 · ~lines 21–23 — "the same numerical TS value carries different statistical weight at different sky positions … The resulting detection scale is therefore spatially inhomogeneous"
- Occurrence 2: `7.2_population_to_spatial.tex` · §7.2.2 · ~line 55 — "Unlike the TS used by the \textit{Fermi}-LAT collaboration, which is computed locally in each region of interest and therefore carries spatially varying significance, the TS adopted here is a single, globally coherent quantity"
- Occurrence 3: `7.2_population_to_spatial.tex` · §7.2.2 · ~line 67 — "the globally homogeneous TS scale --- in contrast to the \textit{Fermi}-LAT catalog's locally computed TS"
- Verification: CONFIRMED (occ. 2 and 3 sit 12 lines apart in the same subsection — genuine intra-subsection repetition).
- Recommendation: KEEP-primary the problem statement in 7.1.1 and the first contrast in 7.2.2 (line 55); CONDENSE→xref the third mention. Concrete fix: at `7.2:67` delete only the em-dash insert, leaving *"First, the globally homogeneous TS scale is particularly advantageous for statistical analyses that combine information across large sky areas, such as the cross-correlation studies discussed in Chapter~\ref{ch:8}."* — the advantage claim is new content; only the re-explanation of the contrast duplicates line 55.

### A6. Cross-correlation as the downstream use case — larger sample worth a sub-leading spurious fraction — Severity: Low (downgraded from Medium at verification) — **revised to KEEP**
- Occurrence 1: `7.1_limits_of_threshold.tex` · §7.1.2 · ~lines 41–42 — "Cross-correlation studies between gamma-ray maps and galaxy catalogs … gain statistical power from a larger sample of source directions, even at the price of a moderate false-positive fraction (cf.\ Chapter~\ref{ch:8})"
- Occurrence 2: `7.2_population_to_spatial.tex` · §7.2.1 · ~line 44 — "cross-correlation studies (Chapter~\ref{ch:8}) --- where the relevant quantity is the number and angular distribution of candidate source directions, not the properties of individual sources"
- (also touched at 7.2.2 ~line 67 and 7.0 ~line 15)
- Verification: PARTIAL — occ. 2 is mischaracterized: it does not restate the "larger sample tolerates false positives" argument; its role is different (justifying why a firing-pixel map without per-source parameters suffices for the downstream use). The 7.0 and 7.2.2 touches are already bare Chapter-8 pointers. The argument already has exactly one home (7.1.2).
- Recommendation: KEEP (no action). Removing `7.2:44`'s explanatory clause would leave the "price of simplification" paragraph unmotivated. No edit needed.

### A7. High-TS agree / low-TS diverge → divergence point sets the probing depth — Severity: Medium
Restated across the two subsections of 7.2 in almost the same words.
- Occurrence 1: `7.2_population_to_spatial.tex` · §7.2.1 · ~lines 30–32 — "At high TS, where bright sources dominate, the synthetic and real distributions agree well. As one moves to lower TS values, the simulated distributions eventually diverge … The threshold at which this divergence becomes statistically significant determines how deep below the nominal catalog limit the method can reliably probe."
- Occurrence 2: `7.2_population_to_spatial.tex` · §7.2.2 · ~lines 58–59 — "At high $\mathrm{TS}^\star$, where bright sources dominate, the distributions agree; as $\mathrm{TS}^\star$ is lowered, background systematics cause them to diverge, setting the depth to which the method can probe."
- Verification: CONFIRMED (the clause "At high TS, where bright sources dominate, the ... distributions agree" is verbatim modulo TS→TS★).
- Recommendation (direction reversed at verification): the original merge is backwards — trimming 7.2.1 "to the firing-pixel definition it introduces" would gut the core-idea subsection: the §7.2 intro (line 12) explicitly promises that 7.2.1 gives the qualitative comparison, and the firing-pixel definition at `7.2:33` depends on the divergence logic at lines 30–32. **KEEP-primary in 7.2.1 (lines 30–33 intact); CONDENSE→xref in 7.2.2 instead.** Suggested replacement for `7.2:58–59`: *"A Kolmogorov--Smirnov test then compares the cumulative TS distributions of the real sky and each synthetic realization above a minimum threshold $\mathrm{TS}^\star$; the value of $\mathrm{TS}^\star$ at which the distributions cease to agree (cf.\ Section~\ref{sec:simulated_sky}) sets the depth to which the method can probe."*

*(Low-severity note: chapter-roadmap / "full details in the paper body" signposting is repeated — 7.0 ~line 14, 7.2 ~lines 12–13, 7.2 ~line 71. Expected signposting, but 7.2 says "Full details appear in the paper body" twice within four lines (lines 11 and 13); collapse to one — keep line 11, which carries the `\ref`; delete line 13. Verified.)*

### A8. Chapter-6 dN/dS "directly confirms/quantifies" the sub-threshold population — stated twice within §7.1.2 — Severity: Medium (borderline Low)  *(added at verification)*
- Occurrence 1: `7.1_limits_of_threshold.tex` · line 34 — "Genuine astrophysical sources exist below $\mathrm{TS} = 25$ --- the $dN/dS$ recovered in Chapter~\ref{ch:6} confirms this directly ---"
- Occurrence 2: `7.1_limits_of_threshold.tex` · line 37 — "The source-count distribution recovered in Chapter~\ref{ch:6} (cf.\ Section~\ref{sec:source_count}) quantifies this sub-threshold population directly."
- Same assertion (Ch-6 dN/dS directly demonstrates the sub-threshold population), same "... directly" construction, three lines apart in the same subsection, each with its own `Chapter~\ref{ch:6}` reference.
- Recommendation: MERGE. Keep the parenthetical at line 34 (it anchors the paragraph's claim); open the second paragraph directly with the measurement, e.g. replace line 37 with *"The $dN/dS$ measured from high-latitude photon counts (Section~\ref{sec:source_count}) extends as ..."* and fold line 38 into it.

### A9. "Output is a map of firing pixels, not a traditional source catalog" — stated in both 7.2.1 and 7.2.2 — Severity: Medium  *(added at verification)*
- Occurrence 1: `7.2_population_to_spatial.tex` · line 43 — "the method does not return individual source parameters (flux, spectrum, position uncertainty); its output is a map of candidate firing pixels at a chosen pixel resolution."
- Occurrence 2: `7.2_population_to_spatial.tex` · line 69 — "The method's output is therefore a map of firing pixels, not a traditional source catalog."
- Same conclusion drawn twice, once per subsection; also anticipates the paper's own remark (`statistical_framework.tex:62`), so it interacts with B4.
- Recommendation: KEEP-primary at `7.2:43` (where the trade-off is argued in the PCAT-contrast paragraph); CONDENSE→xref at `7.2:69` — after the B4 trim of line 68, lines 68–69 can shrink to a single sentence, e.g. *"Second, because a source can fire several adjacent pixels (and several faint sources can share one), the deliverable is a firing-pixel map rather than a source list — a distinction quantified in the paper body."* Caveat: if the author deletes the PCAT paragraph flagged in the C-notes, occurrence 1's host paragraph (`7.2:41–45`) survives independently (the `\aure` marker covers only lines 36–39), so the primary stays valid either way.

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
- Recommendation: CONDENSE→paper (narrative only). Preview the trio conceptually; leave the exact QF definition and the $\alpha$ grid to `statistical_framework.tex`. *Balanced caveat (verification): the §7.2 intro (line 12) promises this subsection introduces the trio, so it must keep one conceptual sentence per quantity; strip only the operational specifics (the "5000", the exact QF-as-fraction definition, the α grid).*

### B3. TS as a "signal interest label" with meaning drawn from simulations — Severity: Low
- Narrative: `7.2_population_to_spatial.tex` · §7.2.2 · ~line 56 — "treated as a heuristic ``signal interest label'' whose probabilistic meaning comes entirely from the comparison with simulated skies, not from an assumed analytic distribution"
- Paper covers in full: `paper_dnds_catalog/sections/statistical_framework.tex` · ~line 34 — "we use it as a ``signal interest label'', and derive a probabilistic interpretation for it from simulations of synthetic maps"
- Recommendation: CONDENSE→paper (narrative only). Near-verbatim of a paper phrase; a brief nod suffices in the narrative. *Extension (verification): the same narrative paragraph (`7.2:55`) also anticipates the paper's live local-vs-global contrast (`statistical_framework.tex:34`, "We prefer to use a simple and coherent definition valid for all pixels in the sky..."); treat lines 55–56 as one condensation unit (this also intersects A5).*

### B4. Pixel-resolution / firing-pixel multiplicity detail (Nside=512 ≈ 0.12°, one source→many pixels, many sources→one pixel) — Severity: Low
- Narrative: `7.2_population_to_spatial.tex` · §7.2.2 · ~line 68 — "at the chosen pixel resolution ($N_\mathrm{side} = 512$, corresponding to $\sim 0.12^\circ$), a single astrophysical source may produce multiple adjacent firing pixels due to PSF spreading, and conversely, multiple faint sources may contribute to a single pixel"
- Paper covers in full: `paper_dnds_catalog/sections/statistical_framework.tex` · ~lines 61–63 (source-vs-firing-pixel distinction, $N_\mathrm{side}=1024$ simulation vs $512$ analysis, ≈0.12° matching LAT resolution).
- Recommendation: CONDENSE→paper (narrative only). The conceptual point (firing pixels ≠ sources) is worth previewing; the specific $N_\mathrm{side}$ values belong to the paper.

---

## C. Structural notes / borderline cases

- **Orphaned file `7.3_transition_to_paper.tex`.** This file exists (2757 bytes, `\section{Transition to the Paper}`, `\label{sec:transition_catalog}`) but is **not built**: the wrapper `chapter_7.tex` only `\input`s `7.0`, `7.1`, `7.2`, and (conditionally) `7.4_paper_dnds_catalog`. It is therefore dead prose in the current build. Note for the author: it contains concrete result numbers (~9,600 vs ~6,700 firing pixels, ~50% increase; recovery saturating above ~2×10⁻¹⁰ cm⁻² s⁻¹; >97% background-robustness; gPCS/Zenodo pointer) that overlap heavily with the paper `results.tex`/`conclusions.tex`. Since it is unbuilt, it was excluded from the Section A/B analysis per instructions; either wire it in (and then re-run overlap detection, as it would add fresh narrative-vs-paper duplication) or delete it.

- **PCAT digression flagged by the author.** `7.2_population_to_spatial.tex` §7.2.1 ~lines 35–39 carries `\aure{idk if I want to keep this part}` (at line 35) above a detailed PCAT comparison (transdimensional MCMC, ~250 CPU hours, 40°×40° North-Galactic-Pole patch). This is **not** paper over-anticipation — *verification correction: the live paper introduction does not mention PCAT at all; the only Daylan:2016tia mention sits inside the `\begin{comment}` block (`introduction.tex:27`)* — so the detail is narrative-original, not duplicated. Recorded here only because it is an open author decision, not an overlap.

- **4FGL construction detail in §7.1.1 is not paper duplication.** The RoI/TS>25/4σ/1750-RoIs exposition (`7.1` ~lines 14–23) and the DR3 dropped-source episode (~lines 45–49) are background motivation; the integrated paper's live text does not develop them (its detailed 4FGL prose is commented out). *Verification caveat: the live paper text does briefly describe Fermi's recursive per-RoI renormalisation (`statistical_framework.tex:34`, two sentences); §7.1.1's exposition is far fuller and remains legitimate pedagogy.* No B flag; legitimate pedagogical scene-setting.

- **`\aure{}` WIP markers present** in 7.2 (`idk if I want to keep this part`, `check again the definition of the QF`) — left in place per house style; not overlaps, but they intersect B1/B2 (the QF marker sits exactly on the over-anticipated definition).
