# Chapter 6 — Intra-Chapter Overlap Report

> **Verification pass (2026-07-03).** All entries verified against the current `.tex` sources by a fresh-context referee; every claimed line number matched exactly. Changes: A1's §6.2.1 fix corrected (the duplicated clause there is the UGRB definition, not "vast population"); A1/A2 gain missed supporting occurrences in §6.1.1's closing paragraph; A3 and A5 downgraded to Low/KEEP; A8's fix refined to a MERGE. Three new entries added (A9, A10, B4). **Correction to the exclusion note:** the claim that the paper's introduction does not render is only half-true — `paper_dnds/sections/introduction.tex` lines 15–23 are OUTSIDE the comment block and DO render, generating the new overlap B4 with §6.4.

## Sections analyzed / excluded

**Analyzed (narrative, wrapper order):**
- `6.0_introduction.tex` (chapter intro, 19 lines)
- `6.1_limits_individual.tex` (§6.1, incl. §6.1.1, §6.1.2)
- `6.2_source_count.tex` (§6.2, incl. §6.2.1, §6.2.2)
- `6.3_sbi_cnn.tex` (§6.3, incl. §6.3.1, §6.3.2, §6.3.3)
- `6.4_transition.tex` (§6.4)

**Read as reference only (paper subtree, never edited):**
`paper_dnds/sections/{introduction, data_selection, synthetic_map_generation, nn_architecture_training, results, conclusions}.tex`. (Note: the paper's `introduction.tex` historical review of the 1pPDF — lines 1–12 — is inside a `\begin{comment}` block and does **not** render, so the narrative §6.2.2 1pPDF review is not duplicated by rendered paper text. **However, lines 15–23 of that file DO render** under the §6.5 heading — see B4.)

**Excluded:** `6.5_paper_dnds.tex` (standalone wrapper); `appendix_further_tests.tex` was read only as reference context, not audited.

---

## A. Narrative-vs-narrative overlaps  [PRIMARY]

### A1. "Below the detection threshold lies a vast population of unresolved sources" — Severity: High
Near-verbatim topic sentence restated across three narrative sections, each followed by the same "collective imprint on the photon-count map" idea.
- Occurrence 1: `6.0_introduction.tex` · chapter intro · ~line 11 — "Below the formal detection threshold lies a vast population of sources that cannot currently be resolved individually. They collectively imprint their abundance and flux distribution onto the measured pixel counts"
- Occurrence 2: `6.1_limits_individual.tex` · §6.1.2 · ~line 36 — "Below the formal \textit{Fermi}-LAT detection threshold lies a vast population of unresolved sources. Their cumulative emission forms a significant fraction of the unresolved gamma-ray background (UGRB)"
- Occurrence 3: `6.2_source_count.tex` · §6.2.1 · ~line 19 — "Further below --- in the unresolved regime, where individual sources are too faint to be detected at all --- the cumulative emission of these sources forms the unresolved gamma-ray background (UGRB), and the $dN/dS$ must be inferred from the statistical properties of the photon-count map."
- (Supporting occurrence *added at verification*: `6.1_limits_individual.tex` · §6.1.1 close · lines 26–27 — "structurally blind to the population of sources below the detection threshold. Yet this sub-threshold population is far from negligible… implies a substantial flux contribution from sources too faint to be individually resolved" — states the same fact one paragraph before occurrence 2.)
- Verification: CONFIRMED (lines 11–12, 36–37, 19).
- Recommendation (corrected at verification): KEEP-primary in §6.1.2. CONDENSE→xref the intro occurrence (lines 11–12) to avoid the verbatim "Below the formal detection threshold lies a vast population" construction. In §6.2.1 line 19 the duplicated material is **not** a "vast population" clause (that phrase does not appear there) but the second parenthesized UGRB definition — the acronym is spelled out and parenthesized in *both* `6.1:37` and `6.2:19` — plus the "inferred from statistical properties of the photon-count map" clause. Fix: write "the UGRB (Section~\ref{sec:6.1.2})" at line 19 and keep only the regime-ladder content specific to that subsection.

### A2. Conceptual shift: "rather than asking whether any specific source is a dark matter subhalo" — Severity: High
The framing pivot from source-by-source to population-level is stated with almost identical wording in the intro and in §6.1.2, and previewed again in §6.1's opener.
- Occurrence 1: `6.0_introduction.tex` · chapter intro · ~line 10 — "We move from asking whether any specific source is a dark matter subhalo to a broader question: can we recover the statistical properties of the entire faint source population..."
- Occurrence 2: `6.1_limits_individual.tex` · §6.1.2 · ~line 34 — "Rather than asking whether any specific source is a dark matter subhalo, we can ask a different question: what is the statistical distribution of all sources, including those too faint to detect individually?"
- (Supporting) Occurrence 3: `6.1_limits_individual.tex` · §6.1 opener · ~line 5 — "before motivating the transition to population-level methods that forms the core of Part III."
- (Supporting occurrence 4 *added at verification*: `6.1_limits_individual.tex` · §6.1.1 close · line 28 — "The challenge is not to look harder at individual sources, but to develop methods that extract population-level information…" — makes the pivot that §6.1.2's opening (lines 33–34) re-makes immediately after.)
- Verification: CONFIRMED (the phrase "asking whether any specific source is a dark matter subhalo" is verbatim-shared between occ. 1 and occ. 2).
- Recommendation: KEEP-primary in §6.1.2. CONDENSE→xref the intro sentence to a shorter preview that does not reuse the "asking whether any specific source is a dark matter subhalo" construction verbatim. Fold the line-28 supporting occurrence into the same §6.0/§6.1.1-close/§6.1.2-open edit target flagged in the C-notes.

### A3. Astrophysical census is a prerequisite before attributing a residual to dark matter — Severity: Low (downgraded from Medium at verification) — **revised to KEEP**
Same argument (must account for known source classes before claiming an exotic/DM component) restated three times.
- Occurrence 1: `6.1_limits_individual.tex` · §6.1.2 · ~line 43 — "A thorough census of the astrophysical population is a prerequisite for any dedicated dark matter search: only after accounting for the known source classes can a residual exotic component be meaningfully constrained."
- Occurrence 2: `6.2_source_count.tex` · §6.2.2 · ~line 67 — "A more precise measurement of the total $dN/dS$ would therefore help constrain the room remaining for additional contributors such as dark matter annihilation."
- Occurrence 3: `6.4_transition.tex` · §6.4 · ~line 8 — "Quantifying their contribution is essential before any residual can be attributed to non-standard sources."
- Verification: PARTIAL — the three statements are not the same claim at the same detail level: §6.1.2 line 43 is the full motivational argument; §6.2.2 line 67 is a *distinct, more specific* payoff (measurement precision → residual room for DM) that follows directly from the source-class budget; §6.4 line 8 is already a single-clause recap — exactly the one-line-recap form the balanced philosophy prescribes.
- Recommendation (revised): KEEP-primary §6.1.2 line 43 (the motivational anchor). KEEP §6.2.2 line 67 (distinct, more specific claim). KEEP §6.4 line 8 (already a one-clause recap). No action required.

### A4. Recovered $dN/dS$ becomes the empirical prior for the Chapter 7 cataloging framework — Severity: Medium
- Occurrence 1: `6.0_introduction.tex` · chapter intro · ~line 18 — "The recovered source-count distribution becomes the empirical prior for the probabilistic cataloging framework developed in Chapter~\ref{ch:7}."
- Occurrence 2: `6.4_transition.tex` · §6.4 · ~line 9 — "the recovered $dN/dS$ provides the empirical prior for the probabilistic source cataloging framework developed in Chapter~\ref{ch:7}: the flux distribution of sub-threshold sources directly determines the posterior probability that any given sky pixel contains a faint, as-yet-unresolved source."
- Verification: CONFIRMED (near-verbatim "empirical prior for the probabilistic [source] cataloging framework developed in Chapter 7" across both; severity borderline Low, but the verbatim phrase reuse justifies the flag).
- Recommendation: KEEP-primary in §6.4 (fuller, with the mechanistic clause). Rephrase the intro sentence, e.g. *"feeds directly into the cataloging framework of Chapter~\ref{ch:7}"* — intro bookend is fine, just drop the duplicated phrasing.

### A5. "Down to a factor of ~50 below the Fermi-LAT threshold" — Severity: Low (downgraded from Medium at verification) — **revised to KEEP**
Same headline result number stated as an intro preview and again in the transition.
- Occurrence 1: `6.0_introduction.tex` · chapter intro · ~line 15 — "recovering the extragalactic $dN/dS$ down to a factor of 50 below the \textit{Fermi}-LAT threshold."
- Occurrence 2: `6.4_transition.tex` · §6.4 · ~line 15 — "recover the source-count distribution down to fluxes approximately 50 times below the catalog detection threshold"
- Verification: CONFIRMED as located, but a single headline number in an intro preview and its payoff is the canonical legitimate bookend under this report's own rules ("only flag intro/summary echoes if they repeat *full* quantitative detail").
- Recommendation: KEEP (no action).

### A6. The astrophysical source-class triple (blazars, star-forming galaxies, millisecond pulsars) — Severity: Low
- Occurrence 1: `6.1_limits_individual.tex` · §6.1.2 · ~line 42 — "primarily astrophysical objects such as blazars \cite{Ajello:2015mfa,DiMauro:2017ing}, millisecond pulsars \cite{Manconi:2019ynl}, and star-forming galaxies \cite{Linden:2016fdd}."
- Occurrence 2: `6.4_transition.tex` · §6.4 · ~line 7 — "blazars, star-forming galaxies, and millisecond pulsars --- that collectively generate the bulk of the unresolved gamma-ray background."
- (Supporting) `6.2_source_count.tex` · §6.2.2 · ~lines 51–65 — blazars and star-forming galaxies again invoked as the archetypal bright-rare / faint-numerous populations.
- Recommendation: KEEP both (the triple is short and idiomatic); no action needed beyond awareness. Optionally CONDENSE→xref the §6.4 mention.

### A7. Forward reference to Chapter 8 cross-correlation dark-matter search — Severity: Low
- Occurrence 1: `6.0_introduction.tex` · chapter intro · ~line 19 — "the cosmological dark matter searches pursued through cross-correlations in Chapter~\ref{ch:8}."
- Occurrence 2: `6.1_limits_individual.tex` · §6.1.2 · ~line 44 — "deferred to Chapter~\ref{ch:8}, which employs angular cross-correlations with tracers of large-scale structure"
- Occurrence 3: `6.4_transition.tex` · §6.4 · ~line 12 — "a natural next step toward the dark matter cross-correlation searches pursued in Chapter~\ref{ch:8}."
- Recommendation: KEEP (signposting/connective tissue, consistent with thesis style). No change required; three light forward-refs are within normal cross-referencing.

### A8. dN/dS introduced as "the/a single primary observable" — Severity: Low
Handoff restatement across the §6.1→§6.2 boundary and again in §6.2.1.
- Occurrence 1: `6.1_limits_individual.tex` · §6.1.2 · ~line 46 — "The primary observable for characterizing the sub-threshold source population is the source-count distribution, denoted $dN/dS$."
- Occurrence 2: `6.2_source_count.tex` · §6.2 opener · ~lines 4–5 — "The analysis of the unresolved gamma-ray sky begins with a single observable: the differential source-count distribution, $dN/dS$. This function describes how many point sources exist at each flux level..."
- Verification: CONFIRMED, but cutting `6.1:46` outright would orphan line 47 ("We define **this distribution**…").
- Recommendation (refined): MERGE lines 46–47 into a single handoff sentence, e.g. *"The primary observable for this program is the source-count distribution, $dN/dS$, which we define and whose measurement we review in the following section."* This keeps §6.1.2's closer functional while removing the duplicated role-definition that the §6.2 opener restates.

### A9. "Reconstruction from the collective statistical imprint is the central problem of this chapter" — repeated four times within §6.2 — Severity: Medium  *(added at verification)*
- Occurrence 1: `6.2_source_count.tex` · line 6 — "Its reconstruction below the telescope detection threshold… is the central inference problem addressed in this chapter."
- Occurrence 2: `6.2_source_count.tex` · lines 19–20 — "…the $dN/dS$ must be inferred from the statistical properties of the photon-count map. This reconstruction is the central challenge addressed by this chapter."
- Occurrence 3: `6.2_source_count.tex` · lines 38–39 — "the $dN/dS$ must be reconstructed statistically from the collective imprint of unresolved sources on the photon-count map."
- Occurrence 4: `6.2_source_count.tex` · line 46 — "Recovering the source-count distribution below the detection threshold requires extracting population information from the collective statistical imprint of unresolved sources on the photon-count map."
- (Echoes: `6.1_limits_individual.tex` lines 28 and 38 state the same idea, partially covered by A1.)
- Recommendation: KEEP-primary line 46 (launches the §6.2.2 method discussion) and KEEP line 6 (section-opener signposting). CUT-secondary line 20 ("This reconstruction is the central challenge addressed by this chapter." — a pure repeat of line 6 fourteen lines later) and CONDENSE→xref the line-38 clause to "…must be reconstructed statistically (Section~\ref{sec:6.2.2})."

### A10. Double regime-ladder within §6.2.1 — Severity: Medium  *(added at verification)*
Lines 16–20 and lines 36–39 of `6.2_source_count.tex` both walk the same bright→faint ladder (catalog counting → efficiency-corrected → statistical reconstruction), both citing `Amerio:2023uet` for the catalog measurement.
- Occurrence 1: lines 16–20 — "For sources bright enough to be individually cataloged, $dN/dS$ is measured by simply counting objects… \cite{Amerio:2023uet}… Below this threshold, the detection efficiency degrades… Further below… must be inferred from the statistical properties of the photon-count map."
- Occurrence 2: lines 36–39 — "At the bright end, it is anchored by direct measurements from the Fermi-LAT catalog… \cite{Amerio:2023uet}. At the faint end, below the detection threshold… must be reconstructed statistically from the collective imprint…"
- Recommendation: MERGE. Keep the first ladder (lines 16–20) as primary; in the synthesis paragraph (lines 36–39) retain only the genuinely new quantitative anchors ($S^{-2}$ vs Euclidean $S^{-5/2}$ slope; $S_\mathrm{th}\sim 2\times10^{-10}$ cm⁻² s⁻¹) and drop the repeated catalog-measurement and statistical-reconstruction clauses. Overlaps with A9 occurrence 3 — one edit resolves both.

---

## B. Narrative-vs-paper over-anticipation  [FLAG ONLY]

### B1. Exact CNN training configuration (20 flux bins, flux range, 21 outputs, ~9×10⁵ maps) — Severity: Medium
The narrative reproduces specific training/architecture numbers that the paper states in full.
- Narrative: `6.3_sbi_cnn.tex` · §6.3.2 · ~lines 46–47 — "discretizes the output into 20 flux bins spanning $[5 \times 10^{-12},\, 10^{-7}]$~cm$^{-2}$~s$^{-1}$, plus the isotropic background level $F_\mathrm{iso}$, yielding 21 output parameters. An ensemble of $9 \times 10^5$ synthetic maps is generated for training."
- Paper covers in full: `paper_dnds/sections/nn_architecture_training.tex` (~line 6: 20 bins in $[5\cdot10^{-12},1\cdot10^{-7}]$ + $F_\mathrm{iso}$, indices $i=1,...,21$) and `paper_dnds/sections/synthetic_map_generation.tex` (~line 195: 1 million maps, 90%/10% train/val split).
- Verification: CONFIRMED (paper coverage verified; `conclusions.tex` line 4 additionally states "trained on 900k synthetic maps", so the narrative's $9\times10^5$ is stated verbatim-equivalent in the rendered paper twice).
- Recommendation: CONDENSE→paper (narrative only; paper untouched) — keep a one-line qualitative statement ("discretized, non-parametric output; large simulated training ensemble") and defer the exact bin count, flux limits, and ensemble size to the paper body. **Preserve the conceptual sentence at line 48** ("The discretized representation is critical: … non-parametrically") — it carries the argument; only the exact numbers should defer.

### B2. Step-by-step forward-simulation pipeline — Severity: Low
- Narrative: `6.3_sbi_cnn.tex` · §6.3.2 · ~line 42 — "one draws source fluxes from a parametric $dN/dS$, places them on the sky following an assumed spatial distribution, convolves with the instrument PSF and exposure, adds the Galactic foreground and isotropic background, and applies Poisson noise to produce a synthetic photon-count map."
- Paper covers in full: `paper_dnds/sections/synthetic_map_generation.tex` (§4 map model Eq. map/count, source placement, PSF convolution, Poisson realization — ~lines 7–40, 112–125).
- Recommendation: CONDENSE→paper only if trimming elsewhere; borderline. As a methodology preview this level of summary is largely acceptable — flag for awareness, not mandatory cut.

### B3. map2patches 12-patch mechanism re-explained — Severity: Low
- Narrative: `6.3_sbi_cnn.tex` · §6.3.3 · ~lines 58–59 — "subdividing the HEALPix sphere into 12 equal-area base patches at order $n=0$, each of which is independently mapped to a 2D image and processed through standard 3D convolutions. This approach preserves the area and information content of each pixel without spherical distortion..."
- Paper covers in full: `paper_dnds/sections/nn_architecture_training.tex` (~lines 30–41: full map2patch derivation, 12 patches of 4096 pixels, 3D $(N,N,1)$ convolutions, distortion argument).
- Recommendation: Mostly acceptable — the narrative already closes with an explicit xref ("Full architectural details are presented in the paper body"). CONDENSE→paper the mechanistic "preserves the area and information content... without spherical distortion" clause if further tightening is desired; otherwise leave. *(Verification note: lines 61–62 — NNHealpix cross-check, "order of magnitude faster" — also mirror paper line 43 ("more than a factor of 10"); same zone, same verdict, no separate entry needed.)*

### B4. §6.4 closing paragraph vs the RENDERED paper-introduction fragment — Severity: Medium  *(added at verification)*
The un-commented tail of the paper's introduction renders directly under the §6.5 heading, roughly one page after §6.4 ends, and restates the same content nearly verbatim.
- Narrative: `6.4_transition.tex` · lines 14–15 — "The analysis presented below should therefore be understood as a proof of principle for the deep-learning approach… We apply the trained CNN to 14~years of \textit{Fermi}-LAT data in the 1--10~GeV energy band…"
- Paper (renders): `paper_dnds/sections/introduction.tex` · lines 15–20 — "In this paper we update the measurement… 14 years of \fermi data… We train a convolutional neural network (CNN) on synthetic gamma-ray maps… apply the trained CNN to the 14-year \fermi map for photon energies in the (1,10) GeV band… The methodology presented here is also meant to be a proof of principle…" (also `conclusions.tex` lines 6, 13: "(1,10) GeV and to 14 years of data", "provides a proof of principle").
- Recommendation: CONDENSE→paper (narrative only). Trim `6.4` lines 14–15 to one sentence keeping only the factor-50 headline (which the paper intro fragment does *not* state) and drop the "proof of principle" phrase and the trained-CNN/14-year/1–10 GeV recitation, e.g.: *"The analysis presented in the remainder of this chapter applies this framework to real data, recovering the $dN/dS$ down to fluxes roughly 50 times below the catalog detection threshold."*

---

## C. Structural notes / borderline cases

- **Within-section preview→detail→recap of the "four 1pPDF limitations" (§6.3).** `6.3_sbi_cnn.tex` previews the four limitations at ~line 6 (§6.3 opener), details them at ~lines 15–29 (§6.3.1), and recaps "addresses the four limitations identified in Section~\ref{sec:6.3.1}" at ~line 51 (§6.3.2). This is intentional intra-section scaffolding, not cross-section redundancy — flagged as expected structure, no action.
- **Luminosity-function integral (Eq. `eq:dnds_lf`) in §6.2.1 is genuinely new** — it is not derived in the paper subtree, so it is not a Section-B duplication despite being detailed.
- **Heteroscedastic NLL / concrete dropout (§6.3.2 ~line 49)** already defers to the paper via explicit xref ("the full formalism is presented in the paper body (Section~\ref{sec:bayesian-error})"), so it is correctly condensed and NOT flagged under B.
- **Overlap coupling:** A1 and A2 both cluster at the §6.0-intro / §6.1.2 junction; if the intro is trimmed once, both are largely resolved. Treat the intro's population-shift paragraph (~lines 9–12), §6.1.1's closing paragraph (lines 24–28 — which pre-states both the A1 fact and the A2 pivot), and §6.1.2's opening (~lines 33–38) as a single edit target.
- *(Verification, cosmetic)*: the §6.3 line-6 opener lists only three of the four limitations (multi-band is absent) — no report action, but worth knowing when editing that scaffolding.
