# Chapter 6 — Intra-Chapter Overlap Report

## Sections analyzed / excluded

**Analyzed (narrative, wrapper order):**
- `6.0_introduction.tex` (chapter intro, 19 lines)
- `6.1_limits_individual.tex` (§6.1, incl. §6.1.1, §6.1.2)
- `6.2_source_count.tex` (§6.2, incl. §6.2.1, §6.2.2)
- `6.3_sbi_cnn.tex` (§6.3, incl. §6.3.1, §6.3.2, §6.3.3)
- `6.4_transition.tex` (§6.4)

**Read as reference only (paper subtree, never edited):**
`paper_dnds/sections/{introduction, data_selection, synthetic_map_generation, nn_architecture_training, results, conclusions}.tex`. (Note: the paper's `introduction.tex` historical review of the 1pPDF is inside a `\begin{comment}` block and therefore does **not** render — so the narrative §6.2.2 1pPDF review is not duplicated by rendered paper text.)

**Excluded:** `6.5_paper_dnds.tex` (standalone wrapper); `appendix_further_tests.tex` was read only as reference context, not audited.

---

## A. Narrative-vs-narrative overlaps  [PRIMARY]

### A1. "Below the detection threshold lies a vast population of unresolved sources" — Severity: High
Near-verbatim topic sentence restated across three narrative sections, each followed by the same "collective imprint on the photon-count map" idea.
- Occurrence 1: `6.0_introduction.tex` · chapter intro · ~line 11 — "Below the formal detection threshold lies a vast population of sources that cannot currently be resolved individually. They collectively imprint their abundance and flux distribution onto the measured pixel counts"
- Occurrence 2: `6.1_limits_individual.tex` · §6.1.2 · ~line 36 — "Below the formal \textit{Fermi}-LAT detection threshold lies a vast population of unresolved sources. Their cumulative emission forms a significant fraction of the unresolved gamma-ray background (UGRB)"
- Occurrence 3: `6.2_source_count.tex` · §6.2.1 · ~line 19 — "Further below --- in the unresolved regime, where individual sources are too faint to be detected at all --- the cumulative emission of these sources forms the unresolved gamma-ray background (UGRB), and the $dN/dS$ must be inferred from the statistical properties of the photon-count map."
- Recommendation: KEEP-primary in §6.1.2 (where it launches the population argument). CONDENSE→xref the intro occurrence (intro preview is expected but currently near-identical wording). In §6.2.1 CUT-secondary the restated "vast population below threshold" clause and keep only the UGRB/definition content specific to that subsection.

### A2. Conceptual shift: "rather than asking whether any specific source is a dark matter subhalo" — Severity: High
The framing pivot from source-by-source to population-level is stated with almost identical wording in the intro and in §6.1.2, and previewed again in §6.1's opener.
- Occurrence 1: `6.0_introduction.tex` · chapter intro · ~line 10 — "We move from asking whether any specific source is a dark matter subhalo to a broader question: can we recover the statistical properties of the entire faint source population..."
- Occurrence 2: `6.1_limits_individual.tex` · §6.1.2 · ~line 34 — "Rather than asking whether any specific source is a dark matter subhalo, we can ask a different question: what is the statistical distribution of all sources, including those too faint to detect individually?"
- (Supporting) Occurrence 3: `6.1_limits_individual.tex` · §6.1 opener · ~line 5 — "before motivating the transition to population-level methods that forms the core of Part III."
- Recommendation: KEEP-primary in §6.1.2. CONDENSE→xref the intro sentence to a shorter preview that does not reuse the "asking whether any specific source is a dark matter subhalo" construction verbatim.

### A3. Astrophysical census is a prerequisite before attributing a residual to dark matter — Severity: Medium
Same argument (must account for known source classes before claiming an exotic/DM component) restated three times.
- Occurrence 1: `6.1_limits_individual.tex` · §6.1.2 · ~line 43 — "A thorough census of the astrophysical population is a prerequisite for any dedicated dark matter search: only after accounting for the known source classes can a residual exotic component be meaningfully constrained."
- Occurrence 2: `6.2_source_count.tex` · §6.2.2 · ~line 67 — "A more precise measurement of the total $dN/dS$ would therefore help constrain the room remaining for additional contributors such as dark matter annihilation."
- Occurrence 3: `6.4_transition.tex` · §6.4 · ~line 8 — "Quantifying their contribution is essential before any residual can be attributed to non-standard sources."
- Recommendation: KEEP-primary the §6.2.2 statement (best anchored, follows the source-class budget discussion). CONDENSE→xref or trim the §6.1.2 and §6.4 restatements to a single clause each.

### A4. Recovered $dN/dS$ becomes the empirical prior for the Chapter 7 cataloging framework — Severity: Medium
- Occurrence 1: `6.0_introduction.tex` · chapter intro · ~line 18 — "The recovered source-count distribution becomes the empirical prior for the probabilistic cataloging framework developed in Chapter~\ref{ch:7}."
- Occurrence 2: `6.4_transition.tex` · §6.4 · ~line 9 — "the recovered $dN/dS$ provides the empirical prior for the probabilistic source cataloging framework developed in Chapter~\ref{ch:7}: the flux distribution of sub-threshold sources directly determines the posterior probability that any given sky pixel contains a faint, as-yet-unresolved source."
- Recommendation: KEEP-primary in §6.4 (fuller, with the mechanistic clause). CONDENSE→xref the intro sentence (intro bookend is fine, but drop the duplicated "empirical prior for the probabilistic cataloging framework developed in Chapter 7" phrasing).

### A5. "Down to a factor of ~50 below the Fermi-LAT threshold" — Severity: Medium
Same headline result number stated as an intro preview and again in the transition.
- Occurrence 1: `6.0_introduction.tex` · chapter intro · ~line 15 — "recovering the extragalactic $dN/dS$ down to a factor of 50 below the \textit{Fermi}-LAT threshold."
- Occurrence 2: `6.4_transition.tex` · §6.4 · ~line 15 — "recover the source-count distribution down to fluxes approximately 50 times below the catalog detection threshold"
- Recommendation: KEEP-primary in §6.4 (immediately precedes the analysis). Intro preview is acceptable; if trimmed, CONDENSE→xref. Low urgency — this is a legitimate preview/payoff bookend.

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
- Recommendation: CUT-secondary the closing sentence of §6.1.2 (it duplicates the §6.2 opener that immediately follows). The §6.2 opener is the natural primary.

---

## B. Narrative-vs-paper over-anticipation  [FLAG ONLY]

### B1. Exact CNN training configuration (20 flux bins, flux range, 21 outputs, ~9×10⁵ maps) — Severity: Medium
The narrative reproduces specific training/architecture numbers that the paper states in full.
- Narrative: `6.3_sbi_cnn.tex` · §6.3.2 · ~lines 46–47 — "discretizes the output into 20 flux bins spanning $[5 \times 10^{-12},\, 10^{-7}]$~cm$^{-2}$~s$^{-1}$, plus the isotropic background level $F_\mathrm{iso}$, yielding 21 output parameters. An ensemble of $9 \times 10^5$ synthetic maps is generated for training."
- Paper covers in full: `paper_dnds/sections/nn_architecture_training.tex` (~line 6: 20 bins in $[5\cdot10^{-12},1\cdot10^{-7}]$ + $F_\mathrm{iso}$, indices $i=1,...,21$) and `paper_dnds/sections/synthetic_map_generation.tex` (~line 195: 1 million maps, 90%/10% train/val split).
- Recommendation: CONDENSE→paper (narrative only; paper untouched) — keep a one-line qualitative statement ("discretized, non-parametric output; large simulated training ensemble") and defer the exact bin count, flux limits, and ensemble size to the paper body.

### B2. Step-by-step forward-simulation pipeline — Severity: Low
- Narrative: `6.3_sbi_cnn.tex` · §6.3.2 · ~line 42 — "one draws source fluxes from a parametric $dN/dS$, places them on the sky following an assumed spatial distribution, convolves with the instrument PSF and exposure, adds the Galactic foreground and isotropic background, and applies Poisson noise to produce a synthetic photon-count map."
- Paper covers in full: `paper_dnds/sections/synthetic_map_generation.tex` (§4 map model Eq. map/count, source placement, PSF convolution, Poisson realization — ~lines 7–40, 112–125).
- Recommendation: CONDENSE→paper only if trimming elsewhere; borderline. As a methodology preview this level of summary is largely acceptable — flag for awareness, not mandatory cut.

### B3. map2patches 12-patch mechanism re-explained — Severity: Low
- Narrative: `6.3_sbi_cnn.tex` · §6.3.3 · ~lines 58–59 — "subdividing the HEALPix sphere into 12 equal-area base patches at order $n=0$, each of which is independently mapped to a 2D image and processed through standard 3D convolutions. This approach preserves the area and information content of each pixel without spherical distortion..."
- Paper covers in full: `paper_dnds/sections/nn_architecture_training.tex` (~lines 30–41: full map2patch derivation, 12 patches of 4096 pixels, 3D $(N,N,1)$ convolutions, distortion argument).
- Recommendation: Mostly acceptable — the narrative already closes with an explicit xref ("Full architectural details are presented in the paper body"). CONDENSE→paper the mechanistic "preserves the area and information content... without spherical distortion" clause if further tightening is desired; otherwise leave.

---

## C. Structural notes / borderline cases

- **Within-section preview→detail→recap of the "four 1pPDF limitations" (§6.3).** `6.3_sbi_cnn.tex` previews the four limitations at ~line 6 (§6.3 opener), details them at ~lines 15–29 (§6.3.1), and recaps "addresses the four limitations identified in Section~\ref{sec:6.3.1}" at ~line 51 (§6.3.2). This is intentional intra-section scaffolding, not cross-section redundancy — flagged as expected structure, no action.
- **Luminosity-function integral (Eq. `eq:dnds_lf`) in §6.2.1 is genuinely new** — it is not derived in the paper subtree, so it is not a Section-B duplication despite being detailed.
- **Heteroscedastic NLL / concrete dropout (§6.3.2 ~line 49)** already defers to the paper via explicit xref ("the full formalism is presented in the paper body (Section~\ref{sec:bayesian-error})"), so it is correctly condensed and NOT flagged under B.
- **Overlap coupling:** A1 and A2 both cluster at the §6.0-intro / §6.1.2 junction; if the intro is trimmed once, both are largely resolved. Consider treating the intro's population-shift paragraph (~lines 9–12) and §6.1.2's opening (~lines 33–38) as a single edit target.
