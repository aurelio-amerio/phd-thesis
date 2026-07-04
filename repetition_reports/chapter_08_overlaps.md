# Chapter 8 — Intra-Chapter Overlap Report

> **Verification pass (2026-07-03).** All entries verified against the current `.tex` sources by a fresh-context referee. Narrative line numbers are accurate throughout; **paper line numbers in Section B were systematically wrong** (apparently derived from a concatenated build) and are corrected in place — the content claims all verified, so the B verdicts stand. Changes: **A5 and A8 are FALSE POSITIVES and are delisted** (struck through below); A1 and A4 downgraded with revised remedies; A3 gains a missed occurrence; B1 gains a third narrative FoV restatement; B4's remedy softened. Two new entries added (A10, A11), of which A10 is the chapter's highest-value consolidation (it subsumes A2/A3/A7 in §8.1.2). A likely paper typo is flagged in the C-notes.

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

### A1. "Dark matter annihilates inside every gravitationally bound structure" — Severity: Low–Medium (downgraded at verification)
- Occurrence 1: `8.0_introduction.tex` · §8.0 · lines 12–13 — "In fact, if dark matter annihilates or decays, it does so inside every gravitationally bound structure across all cosmic epochs, and the accumulated, unresolved emission from this entire population would contribute to the \UGRB."
- Occurrence 2: `8.1_from_resolved_to_cosmic_web.tex` · §8.1 · ~line 40 — "If dark matter is a particle that annihilates, it could do so not just in our galaxy, but also inside every gravitationally bound structure across the universe."
- Verification: CONFIRMED as located, but this is an intro-premise vs body-opening echo with no quantitative content; what makes it worth keeping is the near-verbatim wording ("inside every gravitationally bound structure"), not the concept repetition.
- Recommendation (revised): KEEP both locations; the original suggestion ("let §8.1 open from the 'how is matter distributed' question") would leave §8.1 without a physics-motivated opening (line 42 is a consequence clause, not a scene-setter). Instead reword §8.1 line 40 to break the verbatim echo, e.g. *"Dark matter annihilation is not a Galactic phenomenon: to qualify a cosmological gamma-ray signal we must first understand how matter is distributed across the universe."* No CONDENSE needed.

### A2. "ρ² scaling ⇒ DM window peaks sharply at z ≲ 0.1" — Severity: High (stated 4× across 2 sections, incl. 3× within §8.1)
- Occurrence 1: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~line 49 — "The gamma-ray flux from dark matter annihilation is proportional to the square of the local dark matter density. Dense, compact structures are therefore the dominant contributors…"
- Occurrence 2: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~line 70 — "The dark matter annihilation signal peaks at low redshift (because the flux is proportional to $\rho^2$ and thus weights dense, nearby structures more heavily)…"
- Occurrence 3: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~line 75 — "$W_\gamma^\mathrm{DM}(z)$ … is sharply peaked at $z < 0.1$ due to the $\rho^2$ density scaling of the annihilation rate."
- Occurrence 4: `8.2_cross_correlation_technique.tex` · §8.2.1 · ~lines 21–22 — "The $\rho^2$ scaling makes the signal dominated by the late-time collapse of matter into dense halos and subhalos… $W_\gamma^\mathrm{DM}$ peaks sharply at $z \lesssim 0.1$ and decays rapidly thereafter…"
- Verification: CONFIRMED (all four locations exact; a fifth instance exists at `8.2:98` in the §8.2.3 blue block — "precisely where the DM annihilation signal peaks" — filed under A7/C1). Stated 4–5 times; the chapter's most-repeated mechanism.
- Recommendation (refined): KEEP-primary `8.1:49` (first full statement); delete the parenthetical at line 70 and the "due to the ρ² density scaling" clause at line 75 (both restate line 49 within the same subsection). In §8.2.1, keep lines 21–22 as the one-line recap the balanced philosophy allows — the window-function formula lives there and needs its conclusion stated — but append "(cf. Section 8.1.2)" rather than cutting. See also A10, which resolves the §8.1.2 side of this cluster in one paragraph edit.

### A3. Blazar redshift distribution + EBL horizon numbers ("z ~ 0.3–0.4/0.5 at 50 GeV; z ≲ 0.1–0.2 above 1 TeV") — Severity: High (same numbers in all 3 physics sections)
- Occurrence 1: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~line 71 — "the blazar window function --- whose redshift distribution peaks at $z \sim 0.3$--0.4 --- mostly does not [overlap]." (also ~line 79: "spread over $z \sim 0.1$--0.4")
- Occurrence 2: `8.2_cross_correlation_technique.tex` · §8.2.1 · ~lines 25–26 — "Unresolved blazars … have their emission peak at $z \sim 0.3$--$0.5$ at $50\,\mathrm{GeV}$. … above ${\sim}\,1\,\mathrm{TeV}$, the observable volume contracts to $z \lesssim 0.1$--$0.2$…" (restated in the §8.2.3 blue block, ~line 99: "above roughly $1\,\mathrm{TeV}$, pair production on the EBL shrinks the gamma-ray horizon to $z \lesssim 0.1$--$0.2$")
- Occurrence 3: `8.3_ctao.tex` · §8.3.1 · ~lines 26 & 29 — "EBL absorption becomes significant above $\sim 1$~TeV, attenuating photons from sources at $z \gtrsim 0.1$--$0.2$…" and "EBL attenuation pushes their window functions, which peak at $z \sim 0.3$--$0.4$ at 50~GeV, down to $z \sim 0.1$--$0.2$ above 1 TeV."
- Missed occurrence *(added at verification)*: `8.2_cross_correlation_technique.tex` · §8.2.1 · line 28 — "blazar contributions extend to $z \sim 0.4$--$0.5$ at 50 GeV" — a fourth statement of the same numbers inside §8.2.1 itself. The same numbers also appear in the active paper (`cross_correlation_signal.tex` lines 32–34), so trimming the narrative also reduces narrative-vs-paper redundancy. Now 6–7 statements across three narrative sections plus the paper.
- Recommendation (refined): CONDENSE→xref. KEEP-primary §8.2.1 lines 25–26 (full energy-dependent version). `8.1:71` may keep the bare "peaks at z ∼ 0.3–0.4" as its light first mention (it carries §8.1.2's argument), but `8.1:79`'s "spread over z ∼ 0.1–0.4" duplicates line 71 two sentences later and should go. Cut the number restatements at `8.2:99` (blue block) and `8.3:26` & `8.3:29` down to "(cf. Section 8.2.1)" plus each location's one new point (§8.3.1: blazars remain the dominant TeV background). Note `8.3:26` and `8.3:29` also duplicate *each other* within §8.3.1.

### A4. Cross-correlation noise cancellation: populations that don't cluster with local galaxies drop out — Severity: Low (downgraded from Medium at verification) — **revised to KEEP**
- Occurrence 1: `8.0_introduction.tex` · §8.0 · ~line 18 — "…it vanishes for astrophysical source populations at redshifts incompatible with the tracer, but is maximal for dark matter emission that clusters with local structure."
- Occurrence 2: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~line 68 — "Any source population that does not cluster with the selected galaxies cancels out of the cross-power spectrum, leaving only the gamma-ray emission that traces the same structures."
- Occurrence 3: `8.2_cross_correlation_technique.tex` · §8.2.2 · ~line 59 — "The high-redshift blazar population does not correlate with a local galaxy catalog, so their 1-halo Poisson term does not appear in $C_\ell^{\gamma g}$."
- Verification: PARTIAL — all three occurrences confirmed, but mischaracterized: `8.1:68` is already a single-sentence conceptual recap (exactly the one-line recap the balanced philosophy prescribes), while `8.2:59` is the specific 1-halo mechanism. This is concept-then-mechanism, not the same explanation twice.
- Recommendation (revised): KEEP (no action), except appending a forward xref at `8.1:68–69`: *"…leaving only the gamma-ray emission that traces the same structures (developed quantitatively in Section~\ref{sec:8.2.2})."* Do not trim §8.1.2 further — line 68 is the section's thesis statement.

### ~~A5. Spectral degeneracy: energy information alone cannot separate DM from blazars~~ — **DELISTED at verification (FALSE POSITIVE)**
- Occurrence 1: `8.0_introduction.tex` · §8.0 · ~line 14 — "…requires more than spectral information alone, since distinct source classes partially overlap in energy."
- Occurrence 2: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~lines 54–55, 58 — the full spectral-degeneracy development.
- Verification: FALSE-POSITIVE. `8.0:14` is a one-clause intro preview with no quantitative detail — legitimate signposting under this report's own rules. §8.1.2 is the *sole* development; there is no second full explanation anywhere.
- Recommendation: KEEP (no action).

### A6. "Unresolved blazars account for ~20–30% of the UGRB intensity" — Severity: Medium (same number, 2 sections)
- Occurrence 1: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~line 51 — "unresolved blazars dominate at high energies and account for about 20--30\% of the total intensity…"
- Occurrence 2: `8.2_cross_correlation_technique.tex` · §8.2.3 · ~line 82 — "Although unresolved blazars may account for roughly 20--30\% of the total UGRB intensity integrated over all redshifts~\cite{Ajello:2015mfa}…"
- Verification: CONFIRMED (lines 51 and 82; note they carry *different citations* — DGRB-review vs Ajello:2015mfa — worth harmonizing when editing). Borderline Low: a single repeated statistic used in genuinely different arguments.
- Recommendation: CONDENSE→xref. KEEP-primary §8.2.3 line 82 (the argument consumes the number there). In `8.1:51` drop the figure: *"unresolved blazars dominate at high energies (their contribution is quantified in Section~\ref{sec:8.2.3})"*.

### A7. 2MASS / 2MRS as the low-z (z ≲ 0.1) optimal catalog — Severity: Medium (restated 3–4× within §8.2, plus §8.1)
- Occurrence 1: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~line 76 — "Local galaxy catalogs such as 2MASS, covering $z \lesssim 0.1$--0.2, have window functions that follow this peak."
- Occurrence 2: `8.2_cross_correlation_technique.tex` · §8.2.1 · ~line 31 — "A dense, shallow catalog covering $z \lesssim 0.1$ such as the Two Micron All-Sky Survey (2MASS) overlaps nicely with the DM annihilation window function…"
- Occurrence 3: `8.2_cross_correlation_technique.tex` · §8.2.3 · ~lines 75–77 — "dense, all-sky surveys covering the local universe (z$<$0.1-0.2) are desirable… The Two Micron All-Sky Survey (2MASS) … peaking at $z \approx 0.072$…" (restated again in the §8.2.3 blue block, ~lines 97–98: "the case for 2MASS and 2MRS … trace the local universe at $z \lesssim 0.1$")
- Verification: CONFIRMED (all locations match).
- Recommendation (prioritized at verification): KEEP-primary §8.2.3. The main cut is the **blue-block re-introduction at lines 97–98**, which restates lines 75–77 of the *same subsection*; shrink to *"the case for 2MASS and 2MRS is even stronger with CTAO: at TeV energies the EBL horizon (Section~\ref{sec:8.2.1}) removes the distant blazars while local DM photons arrive unabsorbed."* **Keep `8.2:31`** (functional example in the overlap-integral argument) and **keep `8.1:76`** (figure discussion) — cutting those would break their paragraphs.

### ~~A8. Star-forming galaxies / misaligned AGN negligible at high (TeV) energies~~ — **DELISTED at verification (FALSE POSITIVE)**
- Occurrence 1: `8.2_cross_correlation_technique.tex` · §8.2.1 · ~line 27 — "Star-forming galaxies trace the cosmic star-formation rate and dominate at much higher redshifts, $z \sim 1$--$3$."
- Occurrence 2: `8.3_ctao.tex` · §8.3.1 · ~line 28 — "At energies above 20~GeV and increasingly toward the TeV regime, star-forming galaxies and misaligned AGN contribute negligibly to the unresolved background."
- Verification: FALSE-POSITIVE (mischaracterized). `8.2:27` is a redshift-distribution claim feeding the tomography argument; `8.3:28` is an energy-spectrum claim. Related populations, different physics statements — not a restatement. (If anything, `8.3:28` lightly duplicates the *paper*, `cross_correlation_signal.tex:16`, but at one sentence it is appropriate narrative context, not over-anticipation.)
- Recommendation: KEEP (no action).

### A9. Auto- vs cross-correlation: DM buried under blazar Poisson shot noise in the auto-spectrum — Severity: Medium
- Occurrence 1: `8.1_from_resolved_to_cosmic_web.tex` · §8.1.2 · ~lines 63–66 — "The auto-correlation power spectrum, however, suffers from a fundamental limitation: the signal from dark matter is always mixed with the shot noise and correlated fluctuations of astrophysical sources… Cross-correlating the gamma-ray map with an external gravitational tracer resolves both limitations at once…"
- Occurrence 2: `8.2_cross_correlation_technique.tex` · §8.2.2 · ~lines 52–56 — "The gamma-ray auto-correlation power spectrum $C_\ell^{\gamma\gamma}$ is dominated by the Poisson shot noise of unresolved blazars at essentially all multipoles… covering any diffuse DM component."
- Verification: CONFIRMED (`8.1:63–66` vs `8.2:52–56`, key quote at line 53).
- Recommendation: CONDENSE→xref with a guard-rail added at verification: §8.1.2's motivation climax needs **both** limitations named (shot-noise mixing, no redshift resolution) — do not reduce lines 63–66 to a single pointer. Trim to one sentence per limitation and change the existing xref at line 65 to also point forward to §8.2.2. KEEP-primary §8.2.2 confirmed correct.

_(Considered but not flagged — CTAO order-of-magnitude angular-resolution / large-collecting-area claim in §8.0 line 22 vs §8.3.1 lines 8 & 22 — judged an EXPECTED intro→body preview, except see C2 for the within-§8.3 duplication.)_

### A10. §8.1.2's closing paragraph pre-states §8.2.1 wholesale — Severity: Medium–High  *(added at verification; structural consolidation of A2+A3+A7)*
- Occurrence 1: `8.1_from_resolved_to_cosmic_web.tex` · lines 74–81 — the Fig. `window_main` walk-through ("Figure~\ref{fig:window_main} illustrates the core idea. The dark matter window function … sharply peaked at $z<0.1$ … 2MASS, covering $z \lesssim 0.1$–0.2 … blazars … spread over $z \sim 0.1$–0.4 …").
- Occurrence 2: `8.2_cross_correlation_technique.tex` · lines 18–34 — the same figure discussed again ("Figure~\ref{fig:window_main} illustrates this feature quantitatively…", line 28) with the same three facts (DM window at low z; blazar window at higher z; 2MASS overlap integral).
- The individual facts are flagged as A2/A3/A7, but they *co-locate*: the whole §8.1.2 closing paragraph is a preview-in-full of §8.2.1, including a duplicate walk-through of the same paper figure.
- Recommendation: CONDENSE→xref. KEEP-primary §8.2.1 (where $W_\gamma$, $W_g$ and the overlap integral are defined). Compress `8.1:74–81` to two sentences: the qualitative "DM emission is local, blazar emission is not; a local catalog therefore selects the DM window" plus *"Section~\ref{sec:8.2.1} makes this argument quantitative (Fig.~\ref{fig:window_main})."* **Implementing A2/A3/A7 through this single paragraph edit is more coherent than three independent trims.**

### A11. Triple near-verbatim hand-off sentence "sensitivity forecast … cross-correlations between the CTAO extragalactic survey and the 2MASS galaxy catalog" — Severity: Medium  *(added at verification)*
- Occurrence 1: `8.0_introduction.tex` · line 21 — "The paper that follows then presents a full sensitivity forecast for detecting dark matter signals through cross-correlations between the CTAO extragalactic survey and the 2MASS galaxy catalog~\cite{Pinetti:2025hgd}."
- Occurrence 2: `8.3_ctao.tex` · line 57 — "…forecasting the sensitivity to dark matter annihilation and decay through cross-correlations between the CTAO extragalactic survey and the 2MASS galaxy catalog…"
- Occurrence 3 (read-only, active paper bridge): `paper_xcorr/sections/introduction.tex` · line 28 — "In this paper, we present a sensitivity forecast for detecting dark matter signals through cross-correlations between the CTAO extragalactic survey and the 2MASS galaxy catalog."
- Occurrences 2 and 3 are read back-to-back (§8.3 ends, §8.4 opens with the bridge), so the reader hits the same sentence twice within a page — three times counting the intro. The bridge paragraph is chapter-added text inside the paper file, but under the read-only convention the fix belongs in the narrative.
- Recommendation: CONDENSE→xref at `8.3:57`: shrink to *"The paper that follows~\cite{Pinetti:2025hgd} applies this framework to forecast CTAO's dark matter sensitivity."* Reword the §8.0 roadmap clause to vary phrasing (e.g. "…quantifies what this combination can achieve"). KEEP the paper bridge untouched.

---

## B. Narrative-vs-paper over-anticipation  [FLAG ONLY]

### B1. CTAO instrument specification (three telescope types, fields of view, energy range, generational gain over H.E.S.S./MAGIC/VERITAS) — Severity: Medium–High
- Narrative: `8.3_ctao.tex` · §8.3.1 · ~lines 21–22 — "…the Large-Sized Telescopes (LSTs, … field of view $4.3^\circ$), the Medium-Sized Telescopes (MSTs, field of view $7.5^\circ$--$7.7^\circ$), and the Small-Sized Telescopes (SSTs, fields of view $8.8^\circ$…). … \CTAO covers a broad energy range from 20~GeV up to 300~TeV, with an angular resolution and sensitivity that improve by an order of magnitude over current-generation IACTs, such as HESS, MAGIC, and VERITAS."
- Paper covers in full: `paper_xcorr/sections/cherenkov_telescope_array.tex` *(line numbers corrected at verification)* — order-of-magnitude over H.E.S.S./MAGIC/VERITAS: line 3; LST/MST/SST roles and 20 GeV–300 TeV range: line 5; FoVs 4.3°/7.5–7.7°/8.8°: lines 7–8.
- Additional narrative occurrence *(added at verification)*: the FoV values recur a **third** time at `8.3:42` ("up to $8.8^\circ$ for the SSTs and $7.5^\circ$--$7.7^\circ$ for the MSTs"); when condensing, replace with *"the wide, overlapping telescope fields of view (Section~\ref{sec:CTA})"*.
- Recommendation: CONDENSE→paper (narrative only; paper untouched). The active paper §CTA re-derives these specs in full; the §8.3.1 hardware inventory largely duplicates it. Trim the narrative to the qualitative points needed for the cross-correlation motivation (ground-based IACT, atmosphere-as-calorimeter, TeV reach), leaving the exact FoV/telescope-class enumeration to the paper.

### B2. EGAL survey parameters (quarter-sky footprint, |b|>5°, 15%/400 h South + 10%/600 h North = ~1000 h, 3° pointing grid, 0.51 h/1.11 h per pointing, ~3 h effective exposure, ~10% exposure fluctuation) — Severity: High
- Narrative: `8.3_ctao.tex` · §8.3.2 · ~lines 38–43 — "The EGAL survey targets about a quarter of the sky, covering the region defined by $-90^\circ < l < 90^\circ$ and $|b| > 5^\circ$… the Southern array will observe 15\% of the sky with 400 hours, while the Northern array will cover the remaining 10\% with 600 hours, for a total observation time of approximately 1000 hours… a grid of telescope pointings spaced by approximately $3^\circ$… observed for 0.51 hours in the south and 1.11 hours in the north, yielding an effective average exposure of approximately 3 hours… keeping the relative fluctuations in the exposure map to approximately 10\%…"
- Paper covers in full: `paper_xcorr/sections/cherenkov_telescope_array.tex` *(line numbers corrected at verification)* — lines 17 and 19 (footprint; 15%/400 h + 10%/600 h ≈ 1000 h; ~3° grid; 0.51 h/1.11 h; ~3 h effective) and line 34 (~10% exposure fluctuation).
- Verification: CONFIRMED at High — near-verbatim numeric duplication; the narrative even cites "(see Section~\ref{sec:CTA})" at lines 41 and 43 while still restating every number.
- Recommendation: CONDENSE→paper (narrative only; paper untouched). The chapter narrative can summarize the survey qualitatively ("~quarter-sky, ~uniform ~3 h exposure over three years, cf. Section~\ref{sec:CTA}") and defer the full pointing/exposure numbers to the paper via cross-reference.

### B3. Off-source data scenario (~50 h per point, ~25× the EGAL exposure, factor-~4 sensitivity gain) — Severity: Medium
- Narrative: `8.3_ctao.tex` · §8.3.2 · ~lines 47–49 — "…the accumulated off-source data collected through years of CTAO pointed observations… these off-source data sum to an effective exposure of approximately 50 hours per sky location --- roughly 25 times larger than the nominal EGAL exposure --- yielding a factor of $\sim 4$ improvement in sensitivity compared to the 3-hour scenario."
- Paper covers in full *(line numbers corrected at verification)*: ~50 h/point at `cherenkov_telescope_array.tex` line 59; ~25× at `appendix_offsource.tex` line 17 (figure caption); the factor-~4 at `sensitivity_forecast.tex` line 110.
- Recommendation: CONDENSE→paper (narrative only; paper untouched). The narrative already points to App. expo; it can state the scenario in one sentence and drop the "~25×" and "factor ~4" quantitatives to the paper/appendix that derive them.

### B4. Explicit DM annihilation window-function expression — Severity: Medium
- Narrative: `8.2_cross_correlation_technique.tex` · §8.2.1 · ~line 20 — "For dark matter annihilation, it is proportional to $\langle\sigma v\rangle\,\Delta^2(z)\,\left(\Omega_\mathrm{DM}\rho_c/m_\chi\right)^2\,(1+z)^3\,e^{-\tau(E,z)}$, where $\Delta^2(z)$ is the flux multiplier…"
- Paper covers in full *(line numbers corrected at verification)*: `cross_correlation_signal.tex` line 21 (qualitative scaling) and `appendix_formalism.tex` lines 209–213 (full expression, identical factor-by-factor to the narrative proportionality).
- Recommendation (softened at verification): CONDENSE→paper (narrative only; paper untouched), but the ⟨σv⟩, Δ²(z), m_χ⁻² dependence is **load-bearing** for the tomography argument at line 21 and should stay in the narrative; only the (1+z)³ e^{−τ(E,z)} factors over-anticipate the appendix. Suggested replacement: *"For dark matter annihilation, it is proportional to $\langle\sigma v\rangle\,\Delta^2(z)/m_\chi^2$, where $\Delta^2(z)$ is the flux multiplier capturing the enhancement from DM clustering and substructures (full expression in Appendix~\ref{app:WDM})."*

_(Considered but NOT flagged: the variance/noise-term discussion in §8.2.2 ~lines 42–50 references Eqs. `variance_cross`/`variance_auto` and the 1-halo/2-halo split — it stays conceptual and defers the equations to the paper/appendix, so it is appropriate anticipation rather than heavy duplication.)_

---

## C. Structural notes / borderline cases

- **C1. §8.2 intra-section restatement.** Beyond the cross-section clusters above, §8.2 restates its own core low-z-overlap argument at each subsection boundary: §8.2.1 (~lines 31–34), the §8.2.3 opening (~line 75), and the §8.2.3 blue block (~lines 97–99) each re-assert "2MASS/2MRS trace z ≲ 0.1 where the DM signal peaks." This is signposting drift more than new content; a single statement in §8.2.3 with back-references would tighten the section. (Covered numerically under A7.)

- **C2. §8.3 intra-section restatement of "quarter of the sky / uniform exposure."** Stated in the §8.3 opener (~line 8), again at §8.3.2 opening (~line 34), and again at §8.3.2 ~line 38 — triple-statement confirmed at verification. *Correction:* the claimed "order-of-magnitude angular resolution over Fermi-LAT at §8.3 line 8 and §8.3.1 line 22" is wrong — line 8 compares to *Fermi-LAT*, line 22 to *current-generation IACTs*; different claims, both legitimate. Instead, the **20 GeV–300 TeV energy range** is stated verbatim at both line 8 and line 22. Low severity (same section, scene-setting), but the opener could defer specifics to the subsections.

- **C3. Blue `\blue{…}` and `\aure{…}` markers.** Several flagged passages sit inside `\blue{}` blocks (§8.2.3 line 97; §8.3.1 lines 21, 26, 28; §8.3.2 lines 47–48 — *corrected at verification: lines 49–50 are not inside `\blue{}`*) and the chapter ends with `\aure{follows the paper}` (§8.3 line 59), indicating these are still WIP/under-revision — consistent with the overlaps in A3/A7/B3 being introduced by recent additions that duplicate settled prose.

- **C4. Intro (§8.0) previews are, on the whole, appropriately scoped.** The recap of prior chapters (~lines 4–8) and the three-section roadmap (~lines 20–21) are expected intro material and were not flagged, except the near-verbatim §8.1 echo (A1) and the hand-off sentence (A11).

- **C5. Likely paper typo (read-only — flag for the author, do not edit)** *(added at verification)*. `paper_xcorr/sections/sensitivity_forecast.tex` line 110 reads "for $3\,\textrm{hrs}$ and $5\,\textrm{hrs}$ of CTAO observations. The $5\,\textrm{hrs}$ case yields approximately a factor of 4 improvement" — almost certainly "50 hrs" (the narrative at `8.3:49` and the rest of the paper compare 3 h vs 50 h). Add an `\aure{}` in the narrative or fix in the paper source upstream.

- **C6. Highest-value fixes (verification synthesis).** The heaviest genuine problems in this chapter are B2 (EGAL numbers, near-verbatim vs paper), the A2/A3 ρ²/EBL-number cluster (best fixed via A10's single-paragraph condensation of `8.1:74–81`), and the §8.2.3/§8.3 blue blocks (C3), which is where most of the duplication entered.
