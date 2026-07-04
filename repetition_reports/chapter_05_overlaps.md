# Chapter 5 — Intra-Chapter Overlap Report

> **Verification pass (2026-07-03).** All entries verified against the current `.tex` sources by a fresh-context referee; all quoted text located, line numbers accurate to within ±1, no false positives. Changes: A1's severity flattened to plain Medium; A2's fix refined to preserve the Bayes formula in §5.4.3; A3 downgraded to Low with the trims mostly withdrawn; B2 narrowed (line 62 is Chapter-3 recap, not paper anticipation); B4 added. **Key structural finding:** the `5.6_paper_dmhalos.tex` wrapper's header comment (lines 1–3) claims the paper's introduction "is replaced by the pedagogical introduction above," yet line 8 still does `\input{sections/paper_dm_halos/sections/introduction}` — as rendered, the paper introduction IS in the chapter. B1/B4's remedies are conditional on resolving this contradiction (see Overall note at the end).

## Sections analyzed / excluded

**Analyzed (narrative, in wrapper order):**
- `5.1_introduction.tex` (§5.1)
- `5.2_dark_matter_substructure.tex` (§5.2, subsecs 5.2.1–5.2.2)
- `5.3_dm_subhalos_gamma_ray_targets.tex` (§5.3)
- `5.4_unassociated_sources.tex` (§5.4, subsecs 5.4.1–5.4.3)

**Read as reference only (paper subtree, never edited):** `paper_dm_halos/sections/{introduction, dm_subhalos_model, statistical_analysis, mixture_model_and_limits, conclusions, appendix_consistency_checks, appendix_em_algorithm, appendix_simulation}.tex`

**Excluded:** `5.5_classification_to_quantification.tex.old` (stale), `5.6_paper_dmhalos.tex` (paper wrapper).

Note: the chapter wrapper `\input`s 5.1–5.4 unconditionally and the paper body (5.6) only when `\renderpapers=true`, so Section-B over-anticipation lands in the same rendered chapter whenever the paper is included.

---

## A. Narrative-vs-narrative overlaps  [PRIMARY]

### A1. "Dark" subhalos below ~10^8 M_sun host no stars/gas/EM, but would shine in gamma rays if DM annihilates — Severity: Medium (flattened from "High on the 3-way restatement" at verification: occ. 1 is a conceptual intro preview without the 10⁸ M☉ figure, so only two occurrences carry full detail)
The same physical claim — subhalos below the ~10^8 M_sun baryon-retention threshold produce no conventional electromagnetic signal, yet would emit gamma rays if DM annihilates, and are therefore the target of this search — is stated three times.
- Occurrence 1: `5.1_introduction.tex` · §5.1 · ~lines 13–15 — "The great majority of these subhalos have masses well below the threshold for retaining baryonic matter ... produce no electromagnetic radiation ... If, however, the dark matter particle annihilates into Standard Model final states, the densest of these subhalos could generate detectable gamma-ray emission."
- Occurrence 2: `5.2_dark_matter_substructure.tex` · §5.2.2 · ~lines 40–44 — "Below $\sim 10^8\,M_\odot$ ... The vast majority of dark matter subhalos therefore contain no stars, no gas, and produce no conventional electromagnetic signature. These are the truly ``dark'' subhalos ... If dark matter annihilates, however, these objects could shine in gamma rays, and it is precisely this population that we target".
- Occurrence 3: `5.3_dm_subhalos_gamma_ray_targets.tex` · §5.3 · ~line 33 — "unlike the Galactic Center (Chapter~\ref{ch:4}), a subhalo below $\sim 10^8\,M_\odot$ contains no stars or gas, and any detected gamma-ray emission would originate entirely from dark matter annihilation."
- Verification: CONFIRMED (occ. 1 at lines 13–14; occ. 2 at lines 40–44; occ. 3 at line 33).
- Recommendation: KEEP-primary in §5.2.2 (the dedicated "Luminous Satellites vs. Dark Subhalos" treatment). §5.1 is legitimate intro preview — leave. §5.3 line 33 makes a distinct "clean target vs. Galactic Center" point but re-asserts the no-stars/gas premise; CONDENSE→xref. Suggested replacement for line 33: *"unlike the Galactic Center (Chapter~\ref{ch:4}), a dark subhalo contains no stars or gas (Section~\ref{sec:5.2.2}), so any detected gamma-ray emission would originate entirely from dark matter annihilation."*

### A2. "The posterior p(k|x) absorbs the training-set class prevalences → prior shift invalidates a classifier" (both citing §3.4.2) — Severity: Medium
The core mechanism against classify-and-count is stated in full in two consecutive subsections of §5.4, both anchored to Section 3.4.2.
- Occurrence 1: `5.4_unassociated_sources.tex` · §5.4.2 · ~lines 40–43 — "the posterior probability $p(k|\mathbf{x})$ produced by any discriminative classifier absorbs the class prevalences of its training set (Section~\ref{sec:3.4.2}). When classifiers are trained on balanced datasets ... the resulting predictions reflect these imposed priors ... The same prior shift problem arises when a model trained on associated sources ... is applied to the unassociated population".
- Occurrence 2: `5.4_unassociated_sources.tex` · §5.4.3 · ~lines 57 (and 62) — "as shown in Section~\ref{sec:3.4.2}, the posterior absorbs the class prevalences of the training set: through Bayes' theorem, $p(k|\mathbf{x}) \propto p(\mathbf{x}|k)\,p(k)$, so any change in the underlying class fractions between the associated and unassociated populations invalidates the classifier's predictions."
- Verification: CONFIRMED (occ. 1 at lines 40–43; occ. 2 at lines 57 and 62; full mechanism twice within 17 lines, both anchored to §3.4.2).
- Recommendation (refined at verification): KEEP-primary the verbal mechanism in §5.4.2 (lines 40–43). In §5.4.3, do **not** reduce line 57 to a bare back-reference — the Bayes decomposition $p(k|\mathbf{x}) \propto p(\mathbf{x}|k)\,p(k)$ is load-bearing there (it is the pivot that introduces $p(\mathbf{x}|k)$, the subsection's subject). Instead keep the one-line formula and strip the re-derivation prose, e.g.: *"Recall from Section~5.4.2 that the posterior ties the prediction to the training-set prevalences — through Bayes' theorem, $p(k|\mathbf{x}) \propto p(\mathbf{x}|k)\,p(k)$ — so it cannot survive a prior shift."* This removes the duplication while preserving the formula §5.4.3 needs.

### A3. "No DM subhalo has ever been confirmed / observed" — Severity: Low (downgraded from Low–Medium at verification)
The empirical-anchor fact is restated across all three §5.4 subsections, each time to motivate a different sub-argument.
- Occurrence 1: `5.4_unassociated_sources.tex` · §5.4.1 · ~line 24 — "To date, no unassociated Fermi-LAT source has been confirmed as a dark matter subhalo".
- Occurrence 2: `5.4_unassociated_sources.tex` · §5.4.2 · ~line 38 — "no dark matter subhalo has ever been identified, so the ``DM'' class used in supervised classification has no empirical anchor".
- Occurrence 3: `5.4_unassociated_sources.tex` · §5.4.3 · ~lines 52, 66 — "If we had access to an already well established population of DM subhalos ... but that is currently not the case" and "a class never observed (dark matter subhalos)".
- Verification: PARTIAL — the repetition is real, but occurrences 2 and 3 are already single sentences / subordinate clauses, i.e. exactly the one-line-recap form the balanced philosophy prescribes. There is no "full length" re-narration outside §5.4.1.
- Recommendation (revised): KEEP-primary §5.4.1 line 24 (carries the `\aure{}` about contested claims). §5.4.2 line 38: add a back-reference only — "no dark matter subhalo has ever been identified (Section~\ref{sec:5.4.1})" — the sentence itself is load-bearing as the first flaw. §5.4.3 lines 52/66: KEEP (no action); they are already minimal clauses, and trimming them further would weaken each sub-argument for negligible gain. (The coordination note with the line-25 `\aure{}` stands.)

### A4. "ΛCDM predicts a vast population of subhalos" — Severity: Low (signposting, expected)
Topic-sentence recap recurs across sections as connective tissue rather than substantive redundancy.
- Occurrence 1: `5.1_introduction.tex` · §5.1 · ~line 12 — "the Milky Way's dark matter halo hosts a vast population of gravitationally bound substructures".
- Occurrence 2: `5.2_dark_matter_substructure.tex` · §5.2.1 · ~lines 20, 27 — "$\Lambda$CDM predicts that Milky Way-mass halos are populated by a large number of subhalos" / "the total number of subhalos in a Milky Way-like galaxy is vast".
- Occurrence 3: `5.3_dm_subhalos_gamma_ray_targets.tex` · §5.3 · ~line 9 — "Having established that $\Lambda$CDM predicts a vast population of dark subhalos orbiting the Milky Way".
- Recommendation: KEEP as-is. This is the expected preview→develop→recap signposting; no action needed.

---

## B. Narrative-vs-paper over-anticipation  [FLAG ONLY]

### B1. Classify-and-count strategy and its three statistical flaws, enumerated in detail — Severity: Medium–High
§5.4.2 lays out classify-and-count and its problems (no empirical anchor; posterior absorbs balanced-training priors / prior shift with the AGN-vs-pulsar imbalance example; ad hoc probability threshold yielding order-of-magnitude candidate-count swings) at a level of detail that closely mirrors the paper introduction's dedicated treatment of the same critique.
- Narrative: `5.4_unassociated_sources.tex` · §5.4.2 · ~lines 32–45 — "a set of DM subhalo candidates is selected ... upper limits ... are derived under the assumption that the number of true subhalos cannot exceed the candidate count ... suffers from three interrelated problems ... the number of DM candidates depends on an ad hoc probability threshold $p_\mathrm{DM} > p_\mathrm{threshold}$ ... different thresholds yield candidate counts that can differ by an order of magnitude".
- Paper covers in full: `paper_dm_halos/sections/introduction.tex` (~lines 26–50: threshold "selected by hand ... not based on a statistical argument"; 50/50 balanced-class bias; prior shift; unavailable realistic testing set for DM).
- Verification: CONFIRMED (narrative at lines 32–45; paper coverage at `introduction.tex` lines 26–49 in full detail — threshold "selected by hand" 36–37, 50/50 balanced-class bias 37–38, realistic-testing-set unavailability 39, prior shift 40, AGN-vs-pulsar 10:1 example 37–38). This is the chapter's largest narrative-vs-paper doubling.
- Recommendation: CONDENSE→paper (narrative only; paper untouched), with two qualifications added at verification. (1) The condensed form should keep **one sentence per flaw** — §5.4.2 is the chapter's pedagogical motivation for quantification learning and a bare pointer would gut it; e.g. keep lines 37–38 plus one-clause versions of flaws two and three, closing with "the paper introduction (Section~\ref{sec:...}) develops each of these in detail." (2) **This remedy is conditional on the wrapper contradiction** (see header note / Overall note): if the author's actual intent is to drop the paper introduction from the rendered chapter (removing the `\input` at `5.6_paper_dmhalos.tex:8` — a thesis-side wrapper edit, allowed under the rules), B1 evaporates and the narrative should stay at full detail.

### B2. Covariate/prior-shift formalism, shared sigmoid covariate modulation, and the mixture formula — Severity: Medium
§5.4.3 restates the prior-shift/covariate-shift decomposition, the $p(\mathbf{x}|k)$-invariance argument, the mixture model $\tilde p_\mathrm{unas}(\mathbf{x})=\sum_k \pi_k p(\mathbf{x}|k)$, and the specific modeling choice that the covariate-shift sigmoid functions are shared across all astrophysical classes and fitted jointly with the prevalences — all of which the paper derives formally.
- Narrative: `5.4_unassociated_sources.tex` · §5.4.3 · ~lines 62, 67–69, 75–77 — "$p_\mathrm{assoc}(\mathbf{x}|k) = p_\mathrm{unas}(\mathbf{x}|k)$; see Equation~\ref{eq:prior_shift}" ... "$\tilde{p}_\mathrm{unas}(\mathbf{x}) = \sum_k \pi_k\, p(\mathbf{x}|k)$ ... the class prevalences $\pi_k$ are free parameters" ... "the sigmoid modulation functions $\tilde{C}(\mathbf{x};\boldsymbol{\theta}_\mathrm{cov})$ ... are shared across all astrophysical classes, and their parameters are fitted jointly with the class prevalences."
- Paper covers in full: `paper_dm_halos/sections/statistical_analysis.tex` — §sec:cov_prior (~lines 71–98, covariate/prior-shift definitions) and §sec:stat-model (~lines 100–206: eq:cov1, eq:cov_model, eq:sigmoid, eq:mixture).
- Verification: PARTIAL — one component mis-attributed. `eq:prior_shift` is defined in **Chapter 3** (`chapter_03/sections/3.4_domain_shift.tex` line 83), not the paper; line 62's invariance statement is therefore a legitimate cross-chapter recap of the Ch. 3 framework, not paper over-anticipation. **Line 62 is dropped from the occurrence list.** Remaining occurrences (lines 67–69, 75–77) confirmed against the paper (`statistical_analysis.tex` lines 85–92, eq:cov1 at 118, eq:cov_model at 129, eq:sigmoid at 136–140, eq:mixture at 180–184).
- Recommendation (narrowed): CONDENSE→paper targeting **lines 75–77 only** (the shared-sigmoid $\tilde{C}(\mathbf{x};\boldsymbol{\theta}_\mathrm{cov})$ implementation and joint fitting — pure paper implementation detail, cf. paper eq:sigmoid/eq:mixture); replace with e.g. *"the covariate-shift correction is implemented as a monotonic modulation shared across astrophysical classes and fitted jointly with the prevalences (Section~\ref{sec:stat-model})."* **KEEP the mixture formula at line 67**: it is the conceptual crux of the quantification argument and a legitimate one-line anticipation. Line 62: KEEP (Ch. 3 recap, out of scope).

### B3. 4FGL-DR4 unassociated-source counts (2428 unassociated ≈ 1/3; 1282 at |b|>10°) — Severity: Low
- Narrative: `5.4_unassociated_sources.tex` · §5.4.1 · ~lines 14–16 — "approximately 7,200 sources ... 2,428 sources---roughly one third---remain unassociated ... 1,282 sources lie at Galactic latitudes $|b| > 10^\circ$" (carries `\aure{check these number again in the paper}`).
- Paper covers in full: `paper_dm_halos/sections/introduction.tex` (~lines 20–21) and `statistical_analysis.tex` §sec:halos:data.
- Verification: CONFIRMED (narrative lines 14–16; paper `introduction.tex` lines 20–21 — numbers currently agree).
- Recommendation: CONDENSE→paper is optional here; quoting the catalog census in the narrative is normal scene-setting. Flagged only for completeness — the existing `\aure{}` already asks to reconcile the numbers against the paper.

### B4. §5.4.3's quantification-learning exposition also doubles the paper *introduction*'s own treatment — Severity: Medium  *(added at verification)*
B2 cites only `statistical_analysis.tex`, but the paper **introduction** independently carries the same quantification argument, so §5.4.3 is doubled against two paper locations.
- Narrative: `5.4_unassociated_sources.tex` · lines 55–69 — $p(k|\mathbf{x})$ vs $p(\mathbf{x}|k)$, generative-vs-discriminative framing, mixture with free prevalences, new class with zero training prevalence, product likelihood + profile-likelihood intervals.
- Paper covers: `paper_dm_halos/sections/introduction.tex` · lines 50–56 (quantification learning defined, template matching) and 62–81 ("In more formal terms, we construct PDFs $p(\bx|k)$ ... Estimating $p(\bx|k)$ instead brings several crucial advantages ... include a new class ... The product of $p(\bx_i)$ over unassociated sources is the model likelihood, which we maximize").
- Recommendation: fold into B2's scope as additional paper coverage (CONDENSE→paper, narrative only). No separate action beyond B2's, but it strengthens the case that lines 75–77 (and any expansion of 55–69) should not grow further — and it feeds the same open design question as B1: if the paper introduction stays rendered, the chapter states the quantification pitch **three times** (narrative §5.4.3, paper intro, paper §sec:stat-model).

---

## C. Structural notes / borderline cases

- **Results preview in §5.4.3 (borderline B).** `5.4_unassociated_sources.tex` §5.4.3 ~lines 78–79 previews paper results — "the relative fraction of Galactic sources rises from 6\% ... to 29\% ... prior shift alone is preferred at $7\sigma$ ... covariate shift alone reaches $4.5\sigma$". These numbers live in `paper_dm_halos/sections/mixture_model_and_limits.tex` (~lines 42, 47) and `appendix_consistency_checks.tex` §app:prior_vs_cov, with the prevalence table `tab:class_prevalence_astro`. Verified in sync as of 2026-07-03. This is roadmap-style anticipation of the chapter's own results and is acceptable; no action recommended, just noted so the numbers stay in sync with the paper if edited. *(Minor addition at verification: paper line 47 also reports 6.7σ for the combined model, which the narrative omits; if the preview is ever touched, consider whether to include it.)*
- **A2/A3 are intra-file (within §5.4) across distinct subsections.** They still qualify as intra-chapter redundancy (different section numbers, 5.4.1/5.4.2/5.4.3) and are the highest-value narrative-vs-narrative cleanup targets in the chapter, since §5.4 carries the conceptual argument three times over.
- **Commented-out duplicate block.** `5.4_unassociated_sources.tex` lines 71–73 contain a commented-out earlier version of the §5.4.3 quantification-learning paragraph. Not rendered, so out of scope, but worth removing eventually to avoid a stale second copy.
- **Open `\aure{}` markers touching flagged passages:** §5.4.1 line 25 (soften "no confirmed" pending arXiv:2507.16932 / 2409.19493), §5.4.2 line 31 ("strong statement ... tone down"), lines 17/22 (number/xref checks). Any condensation in A2/A3/B1 should preserve these.

- **Overall note (added at verification): the B-section's biggest lever is a wrapper decision, not prose surgery.** `5.6_paper_dmhalos.tex` lines 1–3 say the paper introduction "is replaced by the pedagogical introduction above," but line 8 still inputs it. Either the comment is stale (paper intro renders → B1/B4 are live and CONDENSE→paper applies) or the `\input` line was meant to be removed (→ B1 and half of B4 disappear, and §5.4.2's full detail is exactly right). Removing an `\input` from the thesis-side wrapper does not touch paper prose, so it is within the rules if that is the author's intent. **Resolve this before doing any B-section edits.**
