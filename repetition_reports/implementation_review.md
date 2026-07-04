# Review of the implemented repetition corrections (Chapters 1–8)

**Date:** 2026-07-04
**Scope:** every `\blue{}` span (and adjacent commented-out originals) introduced while implementing the directives in `repetition_reports/chapter_0N_overlaps.md`, judged in its surrounding paragraph and at chapter level, against humanizer / scientific-writing principles and the thesis voice (CLAUDE.md style guide).
**Method:** eight independent fresh-context review agents, one per chapter, followed by a central pass applying the fixes that were clearly warranted.

## Overall verdict

The implementation is faithful and high quality across all eight chapters. The blue rewrites remove their targeted duplications without re-introducing them, keep the thesis voice, and the restructured Chapter 4 "pendulum" narrative (point-source evidence questioned → defended → weakened by energy-binned analyses) is consistent from §4.0 through §4.4, with no section left asserting a superseded claim. Around 25 small edits were needed across 16 files — mostly grammar slips and echoes the rewrites themselves introduced. All edits preserve the `\blue{}` change-tracking convention (replacements of non-blue text were made by commenting out the original and adding a blue replacement). Braces balance; changes are prose-only.

Numbers that were changed deliberately during the revision were spot-verified: 36–51 GeV and (1–3)×10⁻²⁶ cm³/s match the Daylan et al. (1402.6703) abstract, and 8.33 kpc matches Cirelli:2024ssz. All cross-reference labels used in blue spans were checked and resolve.

## Edits applied

### Meaning and grammar slips inside blue text

| File (approx. line) | Fix |
|---|---|
| `chapter_01/.../1.4_indirect_detection.tex` (~342) | "$b\bar b$ masses below ~100 GeV" → "dark matter masses below ~100 GeV in the $b\bar b$ channel" (the mass belongs to the DM particle, not the quark pair) |
| `chapter_04/.../4.1_discovery_and_characterization.tex` (~138) | "analyses in which the excess traces the stellar bulge … describe the same data" → "models in which…" (analyses don't describe data) |
| `chapter_04/.../4.3_systematics_stalemate.tex` (~81) | stacked past participles ("constraints, obtained…, developed…") recast as a relative clause in the author's "we" voice |
| `chapter_04/.../4.4_breaking_the_stalemate.tex` (~38) | "a requirement that the hypothesis … does not explain" → "a requirement for which the hypothesis, as currently formulated, offers no explanation" |
| `chapter_05/.../5.3_dm_subhalos_gamma_ray_targets.tex` (~34) | dangling comparison ("unlike the Galactic Center, the absence of any baryonic content…") — subhalos restored as the subject |
| `chapter_05/.../5.4_unassociated_sources.tex` (~72) | "labelling" → "labeling" (US spelling, matching the section) |
| `chapter_06/.../6.2_source_count.tex` (~41) | "extending **it**" bound to the wrong antecedent (threshold, not measurement) → "extending the measurement" |
| `chapter_07/.../7.2_population_to_spatial.tex` (~28) | subject slip: fluxes were being "scattered at uniformly random positions" — now the sources are; also "exposure and Gaussian-Process treatment" → "Gaussian-Process uncertainty treatment" (exposure weighting is retained in the narrative, so deferring it was contradictory) |
| `chapter_07/.../7.2_population_to_spatial.tex` (~67) | "at a given operating point" was circular with line 69 (which defines the operating point) → "at a given $\mathrm{TS}^\star$" |
| `chapter_07/.../7.2_population_to_spatial.tex` (~76) | ambiguous attachment → "quantified in the paper body at the adopted pixel resolution" |
| `chapter_03/.../3.3_ml_astrophysics.tex` (~33) | ambiguous bare "this" disambiguated ("this search requires") |
| `chapter_08/.../8.3_ctao.tex` (~30) | typo "contitute" → "constitute" |
| `chapter_08/.../8.3_ctao.tex` (~47) | "wide, overlapping fields of view … create deliberate overlaps" tautology trimmed |
| `chapter_08/.../8.3_ctao.tex` (~53) | "Another series of observations that can be exploited … is the accumulated off-source data" (awkward agreement) → "Cross-correlation studies can also exploit the accumulated off-source data" |
| `chapter_08/.../8.3_ctao.tex` (~66) | "applies this framework" had lost its antecedent after the A11 condensation → "applies the framework developed in this chapter" |
| `chapter_08/.../8.3_ctao.tex` (~57, non-blue, adjacent) | "associated to a specifc and dedicated survey" → "associated with a specific and dedicated survey" |

### Repetitions the rewrites themselves introduced

| File (approx. line) | Fix |
|---|---|
| `chapter_01/.../1.2_wimp_paradigm.tex` (~12) | "an enormous parameter space of candidates, surveyed in Section 1.2.1" echoed the roadmap sentence and §1.2.1's opener → "a vast parameter space of candidates (Section 1.2.1)" |
| `chapter_01/.../1.2_wimp_paradigm.tex` (~48) | duplicated appeal-plus-pointer construction → "The WIMP miracle (Section 1.2.2) has kept them…" |
| `chapter_01/.../1.4_indirect_detection.tex` (~418) | "the most debated of these anomalies" echoed "Several persistent anomalies" in the previous sentence → "the most debated" |
| `chapter_04/.../4.3_systematics_stalemate.tex` (~116) | trailing ", reigniting the question … rather than answering it" stated the same idea a third time with a doubled "rather than" — cut |
| `chapter_04/.../4.4_breaking_the_stalemate.tex` (~44) | ", and the tension with the MSP interpretation, as it has been formulated so far, is correspondingly sharpened" was a near-verbatim clone of the new intro blue (4.0:27) and the third "tension" in two sentences — cut |
| `chapter_07/.../7.0_introduction.tex` (~12) | "to turn the recovered $dN/dS$ into spatial information" echoed non-blue line 8 four lines above — recast |
| `chapter_08/.../8.1_from_resolved_to_cosmic_web.tex` (~68) | xref parenthetical corrected from §8.2.2 to §8.2.1 (it attaches to the redshift-resolution limitation, which is tomography, not noise) and de-duplicated against the blue xref three lines below |
| `chapter_08/.../8.1_from_resolved_to_cosmic_web.tex` (~69) | the non-blue sentence after the condensed two-limitations span still re-enumerated both limitations near-verbatim — trimmed to "…resolves both limitations at once." (original commented out, replacement in blue) |
| `chapter_08/.../8.3_ctao.tex` (~32) | dropped an "(cf. Section 8.2.1)" identical to the one four lines up in the same paragraph |
| `chapter_08/.../8.3_ctao.tex` (~49) | "keeping the exposure map approximately uniform" was the fourth "approximately uniform" in the section → "keeping the residual fluctuations in the exposure map small" |

### Wrong statements, corrected (please confirm)

1. **`chapter_04/.../4.0_introduction.tex` (~12) — mass range 30–70 → 30–50 GeV.** The 70 GeV upper edge is supported by nothing in the chapter: §4.1.4 quotes ~30–50 GeV, no per-study value exceeds ~55 (Goodenough–Hooper 25–30, Daylan 36–51, Abazajian ~39, Calore 49±6), and report item A6 explicitly asked for alignment with §4.1.4. The cited papers (Daylan, Calore, Cirelli) don't support 70.
2. **`chapter_08/.../8.3_ctao.tex` (~45) — "three hours per pointing" → "per sky location".** Individual pointings are 0.51 h (south) / 1.11 h (north); the ~3 h effective exposure arises per sky location from overlapping pointings. As written the blue text contradicted the paper (cf. `sec:CTA`); the commented original said "per point within the survey boundary".
3. **`chapter_06/.../6.2_source_count.tex` (~41) — restored "over most of the resolved range".** The merge dropped this qualifier from the commented original, silently strengthening the $S^{-2}$ power-law claim beyond what Amerio:2023uet supports.
4. **`chapter_03/.../3.0_introduction.tex` (~16) and `3.6_summary.tex` (~18) — stale after the §3.3.4 dissolution.** Both still claimed §3.3 covers mixture models / KDE+EM; the roadmap now lists "convolutional neural networks and density estimation", and the summary sentence points the KDE/EM framework to Chapter 5 where it is developed. Both replacements are in blue with originals commented out.

## Flags left open (author decisions — not fixed)

1. **`4.3_systematics_stalemate.tex` (~92) — unverified value "~260".** The blue text reads "from ~260 when resolved catalog sources are masked to the ~400 quoted in Section 4.2.1 when they are not~\cite{Lee:2015fea}". The masked/unmasked reconciliation is what the report's C-note asked for, but 260 appears nowhere else in the repo and could not be verified against Lee:2015fea. **Check against the paper (or NotebookLM) before accepting.**
2. **`7.2_population_to_spatial.tex` (~20)** — "Since the $dN/dS$ carries no spatial content (Section~\ref{sec:threshold_limits})": §7.1 never actually states this (the chapter intro does). Consider dropping the parenthesis or pointing to Chapter 6 / `sec:source_count`.
3. **`7.2_population_to_spatial.tex` (~67)** — the QF gloss ("fraction of synthetic realizations statistically consistent with the real sky") paraphrases the original "fraction of the 5000 synthetic realizations passing the KS test" and sits directly under the live `\aure{check again the definition of the QF}`; verify against `paper_dnds_catalog/sections/statistical_framework.tex`.
4. **`1.4_indirect_detection.tex`** — (a) §1.4.5 (~342) still quotes "below ~100 GeV" while §1.4.7 (~404), the designated numeric home, quotes "~10–100 GeV" (directive A1 asked for the range in one place only; consider dropping the figure from §1.4.5); (b) the "ten orders of magnitude" claim at ~45 is now uncited at first mention — its citations (`Cohen:2016uyg`, `Blanco_2019`) moved to §1.4.7 per A13.
5. **`1.2_wimp_paradigm.tex`** — the narrowing statement still appears twice (blue §1.2 opening at ~18, non-blue "We narrow our attention now" at ~87). Sanctioned by A15 as a bare roadmap clause, but the two sentences remain near-parallel.
6. **Chapter 2 convention note** — the three Ch2 changes (2.1:7, 2.1:49, 2.3:106) deleted the originals outright instead of commenting them out; they survive only in git history / `.bak` files. Also, 2.3:106 retains "spatially uniform isotropic component", a three-word echo of 2.1:133 (the report suggested just "uniform"); and the two items the report marked "borderline / left to author" (the C-note trim at 2.3:88 and the "define the practical limits" echo 2.0:15 / 2.3:9) remain open.
7. **Chapter 3 residuals** — (a) pre-existing report defect #2 is still unfixed: `3.6_summary.tex` (~10) attributes the heteroscedastic Gaussian loss to §3.1's Bayesian side, but it lives in §3.3.2; (b) with the §3.3.3/3.3.4 xrefs redirected to Chapter 5, the first live use of "EM" (3.1:166) now precedes any in-chapter expansion — consider `\gls` or spelling it out at first use.
8. **`5.4_unassociated_sources.tex`** — (a) ~83: `Section~\ref{sec:stat-model}` resolves only inside the paper subtree (renders only when `\renderpapers=true`) — same caveat as existing 5.3 refs, so left as-is; (b) ~73: the condensation dropped the definition of *which* likelihood is profiled (it now first appears only in the paper body), while 5.3:31 also references the profile likelihood; (c) chapter-level: the B1/B4 remedies remain conditional on the unresolved `5.6_paper_dmhalos.tex` wrapper contradiction (header comment says the paper intro is replaced; line 8 still `\input`s it).
9. **`6.0_introduction.tex` (~13)** — the new sentence assigns "identifies its central observable, the source-count distribution" to §6.1.2 while the untouched roadmap (line 16) assigns "formalizes the source-count distribution" to §6.2. Consistent (identify vs formalize), but confirm the division of labor reads as intended.
10. **`8.1_from_resolved_to_cosmic_web.tex` (~41)** — the blue sentence uses "cosmic web" seven lines before the sentence that formally defines it (~48). Cosmetic.
11. **`1.4_indirect_detection.tex` (~420, non-blue)** — "further highlighting the complexity of the issue" is a limp -ing appendage now closing the paragraph a blue span opens; left because it is outside the revision text.
12. **`8.3_ctao.tex` (~56)** — the existing `\aure{}` note about the paper's "5 hrs"/"50 hrs" typo (report item C5) survives the revision and remains accurate — fix upstream in the paper.

## Verified-good (no action)

- All numeric changes made deliberately by the revision check out against sources: 36–51 GeV and (1–3)×10⁻²⁶ cm³/s (Daylan abstract), 8.33 kpc (Cirelli:2024ssz, GRAVITY 8.277), 0.2c harmonization (matches the two non-blue occurrences).
- All `\ref` labels used in blue spans resolve, including the intentionally misspelled `sec:architechture-and-training` (the typo is in the paper's own `\label`, so the ref works).
- Chapter 4's storyline consistency: no non-blue text anywhere in 4.0–4.4 still asserts the superseded "robust point-source evidence" claim; §4.2.2's softening ("no compelling astrophysical mechanism has been established") is deliberate and keeps §4.2 consistent with §4.4.
- Deferrals of instrument/survey numbers (Ch6 B1: 20 bins, 9×10⁵ maps; Ch7 B1/B4/A1: 50×, 5000 realizations, Nside=512; Ch8: pointing grid, 10% fluctuations, 50 h off-source) all read smoothly and keep the load-bearing conceptual sentences in the narrative.
