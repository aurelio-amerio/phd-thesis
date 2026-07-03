# Chapter 5 — Intra-Chapter Overlap Report

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

### A1. "Dark" subhalos below ~10^8 M_sun host no stars/gas/EM, but would shine in gamma rays if DM annihilates — Severity: Medium (High on the 3-way restatement of the core claim)
The same physical claim — subhalos below the ~10^8 M_sun baryon-retention threshold produce no conventional electromagnetic signal, yet would emit gamma rays if DM annihilates, and are therefore the target of this search — is stated three times.
- Occurrence 1: `5.1_introduction.tex` · §5.1 · ~lines 13–15 — "The great majority of these subhalos have masses well below the threshold for retaining baryonic matter ... produce no electromagnetic radiation ... If, however, the dark matter particle annihilates into Standard Model final states, the densest of these subhalos could generate detectable gamma-ray emission."
- Occurrence 2: `5.2_dark_matter_substructure.tex` · §5.2.2 · ~lines 40–44 — "Below $\sim 10^8\,M_\odot$ ... The vast majority of dark matter subhalos therefore contain no stars, no gas, and produce no conventional electromagnetic signature. These are the truly ``dark'' subhalos ... If dark matter annihilates, however, these objects could shine in gamma rays, and it is precisely this population that we target".
- Occurrence 3: `5.3_dm_subhalos_gamma_ray_targets.tex` · §5.3 · ~line 33 — "unlike the Galactic Center (Chapter~\ref{ch:4}), a subhalo below $\sim 10^8\,M_\odot$ contains no stars or gas, and any detected gamma-ray emission would originate entirely from dark matter annihilation."
- Recommendation: KEEP-primary in §5.2.2 (the dedicated "Luminous Satellites vs. Dark Subhalos" treatment). §5.1 is legitimate intro preview — leave. §5.3 line 33 makes a distinct "clean target vs. Galactic Center" point but re-asserts the no-stars/gas premise; CONDENSE→xref (e.g. "a dark subhalo, as established in §5.2.2, contains no stars or gas ...").

### A2. "The posterior p(k|x) absorbs the training-set class prevalences → prior shift invalidates a classifier" (both citing §3.4.2) — Severity: Medium
The core mechanism against classify-and-count is stated in full in two consecutive subsections of §5.4, both anchored to Section 3.4.2.
- Occurrence 1: `5.4_unassociated_sources.tex` · §5.4.2 · ~lines 40–43 — "the posterior probability $p(k|\mathbf{x})$ produced by any discriminative classifier absorbs the class prevalences of its training set (Section~\ref{sec:3.4.2}). When classifiers are trained on balanced datasets ... the resulting predictions reflect these imposed priors ... The same prior shift problem arises when a model trained on associated sources ... is applied to the unassociated population".
- Occurrence 2: `5.4_unassociated_sources.tex` · §5.4.3 · ~lines 57 (and 62) — "as shown in Section~\ref{sec:3.4.2}, the posterior absorbs the class prevalences of the training set: through Bayes' theorem, $p(k|\mathbf{x}) \propto p(\mathbf{x}|k)\,p(k)$, so any change in the underlying class fractions between the associated and unassociated populations invalidates the classifier's predictions."
- Recommendation: MERGE / CONDENSE→xref. §5.4.2 should state the problem once as the second flaw of classify-and-count; §5.4.3 can then cite it ("recall the prior-shift argument of §5.4.2") instead of re-deriving the Bayes-theorem statement. Currently the full mechanism is spelled out twice within ~20 lines.

### A3. "No DM subhalo has ever been confirmed / observed" — Severity: Low–Medium
The empirical-anchor fact is restated across all three §5.4 subsections, each time to motivate a different sub-argument.
- Occurrence 1: `5.4_unassociated_sources.tex` · §5.4.1 · ~line 24 — "To date, no unassociated Fermi-LAT source has been confirmed as a dark matter subhalo".
- Occurrence 2: `5.4_unassociated_sources.tex` · §5.4.2 · ~line 38 — "no dark matter subhalo has ever been identified, so the ``DM'' class used in supervised classification has no empirical anchor".
- Occurrence 3: `5.4_unassociated_sources.tex` · §5.4.3 · ~lines 52, 66 — "If we had access to an already well established population of DM subhalos ... but that is currently not the case" and "a class never observed (dark matter subhalos)".
- Recommendation: KEEP-primary the §5.4.1 statement (the natural home, and it carries the `\aure{}` note about contested recent claims). Trim the §5.4.2/§5.4.3 restatements to brief back-references; the fact is load-bearing each time but need not be re-narrated at full length thrice. (Note the open `\aure{}` at §5.4.1 line 25 flags this "no confirmed" wording may soften — coordinate any edit with that.)

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
- Recommendation: CONDENSE→paper (narrative only; paper untouched). Keep the narrative's conceptual bridge to Chapter 3 quantification learning, but shorten the three-flaw enumeration to a pointer that the paper introduction develops it; currently the full argument runs in both.

### B2. Covariate/prior-shift formalism, shared sigmoid covariate modulation, and the mixture formula — Severity: Medium
§5.4.3 restates the prior-shift/covariate-shift decomposition, the $p(\mathbf{x}|k)$-invariance argument, the mixture model $\tilde p_\mathrm{unas}(\mathbf{x})=\sum_k \pi_k p(\mathbf{x}|k)$, and the specific modeling choice that the covariate-shift sigmoid functions are shared across all astrophysical classes and fitted jointly with the prevalences — all of which the paper derives formally.
- Narrative: `5.4_unassociated_sources.tex` · §5.4.3 · ~lines 62, 67–69, 75–77 — "$p_\mathrm{assoc}(\mathbf{x}|k) = p_\mathrm{unas}(\mathbf{x}|k)$; see Equation~\ref{eq:prior_shift}" ... "$\tilde{p}_\mathrm{unas}(\mathbf{x}) = \sum_k \pi_k\, p(\mathbf{x}|k)$ ... the class prevalences $\pi_k$ are free parameters" ... "the sigmoid modulation functions $\tilde{C}(\mathbf{x};\boldsymbol{\theta}_\mathrm{cov})$ ... are shared across all astrophysical classes, and their parameters are fitted jointly with the class prevalences."
- Paper covers in full: `paper_dm_halos/sections/statistical_analysis.tex` — §sec:cov_prior (~lines 71–98, covariate/prior-shift definitions) and §sec:stat-model (~lines 100–206: eq:cov1, eq:cov_model, eq:sigmoid, eq:mixture).
- Recommendation: CONDENSE→paper (narrative only; paper untouched). Some recap of the Ch.3 framework is expected here, but the paper-specific implementation detail (shared sigmoid across classes, jointly fitted parameters, mixture equation) is over-anticipated; a pointer to the paper's §sec:stat-model would suffice.

### B3. 4FGL-DR4 unassociated-source counts (2428 unassociated ≈ 1/3; 1282 at |b|>10°) — Severity: Low
- Narrative: `5.4_unassociated_sources.tex` · §5.4.1 · ~lines 14–16 — "approximately 7,200 sources ... 2,428 sources---roughly one third---remain unassociated ... 1,282 sources lie at Galactic latitudes $|b| > 10^\circ$" (carries `\aure{check these number again in the paper}`).
- Paper covers in full: `paper_dm_halos/sections/introduction.tex` (~lines 20–21) and `statistical_analysis.tex` §sec:halos:data.
- Recommendation: CONDENSE→paper is optional here; quoting the catalog census in the narrative is normal scene-setting. Flagged only for completeness — the existing `\aure{}` already asks to reconcile the numbers against the paper.

---

## C. Structural notes / borderline cases

- **Results preview in §5.4.3 (borderline B).** `5.4_unassociated_sources.tex` §5.4.3 ~lines 78–79 previews paper results — "the relative fraction of Galactic sources rises from 6\% ... to 29\% ... prior shift alone is preferred at $7\sigma$ ... covariate shift alone reaches $4.5\sigma$". These numbers live in `paper_dm_halos/sections/mixture_model_and_limits.tex` (~line 47) and `appendix_consistency_checks.tex` §app:prior_vs_cov, with the prevalence table `tab:class_prevalence_astro`. This is roadmap-style anticipation of the chapter's own results and is acceptable; no action recommended, just noted so the numbers stay in sync with the paper if edited.
- **A2/A3 are intra-file (within §5.4) across distinct subsections.** They still qualify as intra-chapter redundancy (different section numbers, 5.4.1/5.4.2/5.4.3) and are the highest-value narrative-vs-narrative cleanup targets in the chapter, since §5.4 carries the conceptual argument three times over.
- **Commented-out duplicate block.** `5.4_unassociated_sources.tex` lines 71–73 contain a commented-out earlier version of the §5.4.3 quantification-learning paragraph. Not rendered, so out of scope, but worth removing eventually to avoid a stale second copy.
- **Open `\aure{}` markers touching flagged passages:** §5.4.1 line 25 (soften "no confirmed" pending arXiv:2507.16932 / 2409.19493), §5.4.2 line 31 ("strong statement ... tone down"), lines 17/22 (number/xref checks). Any condensation in A2/A3/B1 should preserve these.
