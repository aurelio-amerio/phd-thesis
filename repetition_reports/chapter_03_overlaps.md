# Chapter 3 — Intra-Chapter Overlap Report

## Sections analyzed / excluded

**Analyzed in full (wrapper order):**
- `3.0_introduction.tex` (chapter intro / roadmap)
- `3.1_inference.tex` (§3.1 Frequentist and Bayesian Inference; subs 3.1.1–3.1.4)
- `3.2_sbi.tex` (§3.2 Simulation-Based Inference; subs 3.2.1–3.2.3)
- `3.3_ml_astrophysics.tex` (§3.3 Machine Learning in Astrophysics; subs 3.3.1–3.3.4)
- `3.4_domain_shift.tex` (§3.4 Domain Shift; subs 3.4.1–3.4.2)
- `3.5_cross_correlations.tex` (§3.5 Cross-Correlations; subs 3.5.1–3.5.2)
- `3.6_summary.tex` (§3.6 Summary)

**Excluded:** None. Chapter 3 has no integrated paper subtree.

**Calibration note.** This is a methods chapter built on the "Application preview" pattern: bold lead-ins and one-liners pointing forward to Chapters 4–9 where each abstract method is concretely used. Per the brief, such forward pointers are EXPECTED signposting and are NOT flagged. The intro (3.0) previewing and the summary (3.6) recapping are likewise expected. Below I flag only cases where the SAME method/argument/model is spelled out in substantive DETAIL twice within distinct narrative sections.

---

## A. Narrative-vs-narrative overlaps  [PRIMARY]

### A1. Chapter-6 frequentist cross-check of the Bayesian dN/dS uncertainty, re-described in full   — Severity: Medium
The same validation procedure — the Chapter-6 Bayesian SBI uncertainties on dN/dS cross-checked against frequentist error bars built from the distribution of residuals over the validation set, with the two estimates agreeing — is narrated with substantive detail in two separate narrative sections (and previewed a third time). The 3.2.3 occurrence even carries a "see also Section 3.1.4" xref yet still restates the whole procedure.

- Occurrence 1: `3.1_inference.tex` · §3.1.4 · ~lines 176–178 — "a simulation-based inference approach provides Bayesian posterior estimates on the reconstructed $dN/dS$, which are validated against a frequentist analysis of the same data where confidence intervals are extracted from the empirical distribution of residuals across the validation set. ... The compatibility of the two independent error estimates provides confidence that the uncertainty quantification is robust."
- Occurrence 2: `3.2_sbi.tex` · §3.2.3 · ~lines 103–105 — "In Chapter~\ref{ch:6}, the internally estimated Bayesian uncertainties are cross-checked against frequentist error bars derived from the distribution of residuals over the validation set (see also Section~\ref{sec:3.1.4}). The close agreement between the two independent error estimates provides confidence in the reliability of the uncertainty quantification."
- (Third, briefer preview: `3.1_inference.tex` · §3.1.3 · ~line 150 — "with posterior uncertainty estimates validated against an independent frequentist cross-check (Section~\ref{sec:3.1.4}).")
- Recommendation: CONDENSE→xref. Keep one full description — §3.2.3 (SBI validation) is the natural home since the surrounding text is about problem-specific SBI diagnostics — and reduce the §3.1.4 passage to the single point it uniquely adds (the "same problem solved by both paradigms as independent cross-check" illustration plus the negligible-bias finding), pointing to §3.2.3 for the mechanics. The two closing sentences ("compatibility / close agreement ... confidence in the uncertainty quantification") are near-duplicates and should appear once.

### A2. The Chapter-5 subhalo mixture model spelled out twice   — Severity: Medium
The composition of the Chapter-5 statistical model — unassociated sources modeled as a mixture of Galactic + extragalactic astrophysical components (class-conditional densities from associated sources via KDE) plus a possible DM subhalo component, with class prevalences fit by EM and a covariate-shift correction — is described in comparable detail in both §3.3.4 and the §3.4 application preview. The two passages cross-reference each other, confirming they cover the same construction.

- Occurrence 1: `3.3_ml_astrophysics.tex` · §3.3.4 · ~lines 161–162 — "In Chapter~\ref{ch:5}, this framework is extended to search for dark matter subhalos among the unassociated Fermi-LAT sources. The mixture model combines astrophysical class-conditional densities with a covariate shift correction (Section~\ref{sec:3.4}) and a possible dark matter component, with class prevalences determined via the EM algorithm following the approach of Saerens et al."
- Occurrence 2: `3.4_domain_shift.tex` · §3.4 (Application preview) · ~lines 102–106 — "The unassociated source distribution is modeled as a mixture of Galactic and extragalactic astrophysical components---whose class-conditional densities $p_{\text{assoc}}(\mathbf{x}|k)$ are estimated from the associated sources via kernel density estimation---plus a possible dark matter subhalo component ... All parameters are optimized simultaneously using the Expectation-Maximization algorithm."
- Recommendation: CONDENSE→xref. Let the §3.4 application preview carry the full model description (it is the point where both prior-shift and covariate-shift corrections are named, so the mixture reads as the natural culmination), and shorten the §3.3.4 closing paragraph to a one-line forward pointer ("this KDE+mixture+EM machinery is assembled into the subhalo search of Chapter 5; see §3.4").

### A3. "Train classifiers on associated sources, apply to unassociated" setup stated twice   — Severity: Low
The core Fermi-LAT classification setup — supervised classifiers trained on associated sources (labels from multi-wavelength counterparts) then applied to the unassociated population — is laid out in the §3.3.1 classification-task discussion and again as the motivating setup in §3.4.1.

- Occurrence 1: `3.3_ml_astrophysics.tex` · §3.3.1 · ~lines 20–21 — "Roughly one-third of the sources in Fermi-LAT catalogs lack firm multi-wavelength associations ..., and supervised classification algorithms---trained on populations of identified AGNs and pulsars---are used to predict the class membership of these unassociated objects."
- Occurrence 2: `3.4_domain_shift.tex` · §3.4.1 · ~lines 22–23 — "Machine learning classifiers are typically trained on associated sources---whose class labels (e.g., pulsar or active galactic nucleus) are known from their multi-wavelength counterparts---and then applied to unassociated sources to infer their nature."
- Recommendation: CONDENSE→xref. Mild overlap that is partly justified (each section needs the setup for a different purpose — introducing classification vs. motivating dataset shift). Trim the §3.4.1 restatement to a back-reference ("the associated→unassociated classification setup of §3.3.1") and keep only the biases that §3.4 uniquely adds.

---

## B. Narrative-vs-paper over-anticipation  [FLAG ONLY]

N/A — Chapter 3 has no integrated paper subtree, so there is nothing to over-anticipate against.

---

## C. Structural notes / borderline cases

- **dN/dS-via-CNN one-liner repeated ~4×** (`3.2_sbi.tex` §3.2.2 ~lines 76–79; `3.3_ml_astrophysics.tex` §3.3 ~line 8, §3.3.1 ~line 25, §3.3.3 ~line 67, §3.3.4 ~line 134). Each is a legitimate application preview surfacing the Chapter-6 CNN in a different methodological frame (SBI / learning tasks / CNNs / density estimation), so per the brief these are EXPECTED signposting, not flags. Noted only because the aggregate density is high — a reader meets "a CNN reconstructs the source-count distribution from gamma-ray sky maps" many times. Not actionable as repetition; a light editorial pass could vary the phrasing.

- **Heteroscedastic Gaussian loss / network predicting its own variance** recurs within §3.3 (§3.3.1 ~line 26, §3.3.2 ~line 50 and ~line 54, §3.3.3 ~line 129) and again in the summary (§3.6 ~line 10). This is largely intra-section (§3.3) build-up plus an expected summary recap, so it falls below the cross-section flag threshold. The §3.3.1 forward "(described in Section 3.3.2)" is a proper xref.

- **Association bias (bright, high-latitude sources easier to associate; Galactic-plane proximity)** is stated in §3.4.1 (~line 25, "the associated sample is not a representative subsample ... biased toward high-latitude, brighter sources") and again in §3.4.2 covariate-shift paragraph (~lines 61–64, "the associated sample is biased toward high-latitude, brighter sources relative to the full population"), both citing `2023RASTI...2..735M`. This is INTRA-section (two subsections of §3.4), so outside the narrative-section-vs-section scope, but the near-verbatim repeat of "biased toward high-latitude, brighter sources" within a few paragraphs is worth a local trim.

- **Likelihood definition** $\mathcal{L}(\boldsymbol\theta)=p(\mathbf d\,|\,\boldsymbol\theta)$ is introduced in §3.1.1 (~line 18) and restated in §3.1.2 (~line 34) and §3.1.3 (~line 118). Intra-section, expected didactic scaffolding — not flagged.

- **SBI intractable-likelihood framing** appears in the §3.2 section intro (~lines 4–5) and is re-stated opening §3.2.1 (~lines 14–15), both saying "the inference methods of §3.1 require evaluating the likelihood; this breaks down for complex simulators." Intra-section (section intro vs. first subsection) and near-duplicate; a minor local tightening would remove the echo, but it is below the cross-section threshold.

- **Wilks' theorem / likelihood-ratio TS** introduced in §3.1.2 (~lines 74–80) and re-applied as the $\Delta\chi^2$ "nested-model comparison in the spirit of Wilks' theorem" in §3.5.2 (~lines 138–145). The §3.5 instance is an APPLICATION of the §3.1.2 concept to cross-correlations, not a re-derivation, and §3.1.2's own application preview already lists the Chapter-8 $\Delta\chi^2$ use. Legitimate; not flagged.
