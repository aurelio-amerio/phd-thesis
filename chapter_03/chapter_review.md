# Review Report: Chapter 3 — Statistical Methods for Noise-Dominated Regimes

## Summary

Chapter 3 is a well-written methods overview that establishes the statistical and ML vocabulary used throughout the thesis. The scientific content is correct and clearly presented, with effective "application preview" paragraphs linking each formalism to its thesis paper. However, several cross-referencing errors, duplicate bibliography entries, and hardcoded chapter numbers need to be fixed before the chapter compiles cleanly.

## Verdict

**Needs revision** — scientifically sound, but has critical cross-referencing and bibliography issues.

## Issue Summary

- 🔴 Critical: 5
- 🟡 Important: 5
- 🟢 Minor: 3

## Strengths

- The scientific formalism is uniformly correct: MLE, profile likelihood, Wilks' theorem, Bayes' theorem, SBI/NPE/NLE/NRE, KDE, EM, covariate/prior shift, and the Limber approximation are all accurately presented.
- The "application preview" structure is pedagogically effective — it connects abstract formalism to concrete thesis applications without duplicating the paper-level detail.
- The distinction between the frequentist integrated likelihood and Bayesian marginalization (Sec 3.1.2–3.1.3) is carefully drawn, a subtlety many theses gloss over.
- The prose is clear, concise, and well-paced. Technical terms are defined at first use. Tense usage is consistent.
- The funnel structure of the introduction (Sec 3.0) effectively motivates the chapter and provides a clear roadmap.
- Section 3.4 (Domain Shift) is particularly strong — the formalization of covariate vs. prior shift with the Fermi-LAT example is crisp and well-illustrated by the included figure.
- The cross-correlation section (3.5) presents a compact but complete derivation of the APS formalism, window functions, and halo model decomposition, with proper attribution to the pioneering work of Camera et al. and Ando & Komatsu.

---

## Critical Issues (🔴)

### Issue 1: Broken cross-reference `\ref{sec:3.3.1}`

- **Location**: `3.3_ml_astrophysics.tex`, line 84
- **Quote**: `"The density estimation task introduced in Section~\ref{sec:3.3.1} addresses a complementary problem to classification."`
- **Problem**: The label `\label{sec:3.3.1}` is commented out on line 5 of the same file (along with its `\subsection{Learning Tasks}` heading). This produces a LaTeX warning and renders as "Section **??**" in the compiled PDF.
- **Suggested fix**: Either (a) uncomment the `\subsection` and `\label` on lines 4–5, or (b) replace the `\ref{sec:3.3.1}` with `\ref{sec:3.3}` (pointing to the parent section) and adjust the wording.

### Issue 2: Wrong chapter reference — "Chapter~9" should be Chapter 5

- **Location**: `3.3_ml_astrophysics.tex`, line 122
- **Quote**: `"This quantification learning framework---which infers population-level properties rather than individual source labels---is developed in full detail in Chapter~9."`
- **Problem**: The quantification learning framework and Paper 4's subhalo search are integrated into Chapter 5 (Dark Matter Substructures), not Chapter 9 (GenSBI, which is an optional chapter about flow matching). This is a factual error in the forward reference.
- **Suggested fix**: Replace `Chapter~9` with `Chapter~\ref{ch:5}`.

### Issue 3: Wrong chapter reference — "Chapter~10" should be Chapter 8 (×2)

- **Location**: `3.5_cross_correlations.tex`, lines 20 and 90
- **Quotes**:
  - Line 20: `"...is deferred to Chapter~10."`
  - Line 90: `"...is deferred to Chapter~10, where the full cross-correlation analysis is presented."`
- **Problem**: The cross-correlation analysis and Paper 5 are in Chapter 8 (Cross-Correlations and Future Prospects). Chapter 10 is Summary and Outlook. The same section correctly uses `Chapter~\ref{ch:8}` on line 130, making the inconsistency especially visible.
- **Suggested fix**: Replace both instances of `Chapter~10` with `Chapter~\ref{ch:8}`.

### Issue 4: Duplicate bibliography entries for Paper 4

- **Location**: Sections 3.1 and 3.3 cite `\cite{Amerio:2025sub}`; Section 3.4 cites `\cite{Amerio:2025fhz}`
- **Problem**: Both bib keys point to the same paper (arXiv:2503.14584). The compiled bibliography will contain two separate entries for the same work, with different in-text reference numbers. Similarly, `Pinetti:2025` and `Pinetti:2025hgd` are duplicates for Paper 5 (arXiv:2505.20383), though only one key is used in Chapter 3.
- **Suggested fix**: Standardize on one bib key per paper across the entire thesis. The InspireHEP keys (`Amerio:2025fhz`, `Pinetti:2025hgd`) are canonical; consider removing the manually created duplicates (`Amerio:2025sub`, `Pinetti:2025`) and updating all citations to use the canonical keys.

### Issue 5: Self-citations should be cross-references

- **Location**: Throughout all section files (~30 instances)
- **Problem**: The author's own papers (Papers 1–5) are included verbatim in the thesis as chapters. Citing them via `\cite{Amerio:...}` or `\cite{Pinetti:...}` treats them as external publications, but they are internal thesis content. The correct practice for a paper-based thesis is to cross-reference the relevant chapter or section with `\ref{}`.

- **Inventory**:

| Bib key | Count | Sections | Should become |
|---|---|---|---|
| `Amerio:2023dns` (Paper 1) | 10 | 3.1, 3.2, 3.3 | `Chapter~\ref{ch:6}` / `Section~\ref{sec:...}` |
| `Amerio:2024msp` (Paper 3) | 1 | 3.1 | `Chapter~\ref{ch:4}` |
| `Amerio:2025sub` (Paper 4) | 5 | 3.1, 3.3 | `Chapter~\ref{ch:5}` |
| `Amerio:2025fhz` (Paper 4, duplicate) | 7 | 3.4 | `Chapter~\ref{ch:5}` |
| `Pinetti:2025` / `Pinetti:2025hgd` (Paper 5) | 7 | 3.1, 3.5 | `Chapter~\ref{ch:8}` |

- **Examples**:
  - `"...subjected to Poisson counting noise~\cite{Amerio:2023dns}"` → `"...subjected to Poisson counting noise (see Chapter~\ref{ch:6})"`
  - `"from \cite{Amerio:2025fhz}, Figure~1"` → `"from Chapter~\ref{ch:5}, Figure~\ref{fig:...}"` (pointing to the figure as it appears in the thesis)
  - `"the signal-to-noise ratio \cite{Pinetti:2025hgd}:"` → `"the signal-to-noise ratio (Chapter~\ref{ch:8}):"` or cite the original formalism source (e.g., Camera et al., Fornengo & Regis) if these equations predate Paper 5
- **Nuance for Sec 3.5**: Several equations in the cross-correlation section cite `Pinetti:2025hgd` for standard formalism (SNR, $\Delta C_\ell$, $\Delta\chi^2$) that actually originates in earlier work (Camera et al. 2013, Fornengo & Regis 2014). Where the formalism predates Paper 5, cite the original source instead. Where the specific form or notation is from Paper 5, use a cross-reference to Chapter~\ref{ch:8}.
- **Suggested fix**: Replace all self-citations with `\ref` cross-references. For formalism attribution, cite the original external source rather than the author's own paper that adopted it.

---

## Important Issues (🟡)

### Issue 5: "Paper~N" numbering is internal jargon — use chapter/section references

- **Location**: Throughout all section files (~20 instances)
- **Examples**:
  - `"In Paper~3 \cite{Amerio:2024msp}, the MSP luminosity function parameters..."` (3.1, line 87)
  - `"Paper~1 employs a convolutional neural network..."` (3.3, line 17)
  - `"In Paper~4, we construct..."` (3.3, line 114; 3.4, line 101)
  - `"Papers~1--5"` (3.1, line 7)
  - `"Papers~3, 4, and~5"` (3.6, line 10)
- **Problem**: The "Paper 1" through "Paper 5" numbering is an internal organizational convention of the thesis project. A reader of the compiled thesis has no way to know which paper corresponds to which number. These should reference the chapter or section where the work appears, which is what the reader can actually navigate to.
- **Mapping for replacement**:

| Internal label | Replace with |
|---|---|
| Paper~1 | Chapter~\ref{ch:6} / the $dN/dS$ analysis of Chapter~\ref{ch:6} |
| Paper~2 | Chapter~\ref{ch:7} / the probabilistic catalog of Chapter~\ref{ch:7} |
| Paper~3 | Chapter~\ref{ch:4} / the MSP analysis of Chapter~\ref{ch:4} |
| Paper~4 | Chapter~\ref{ch:5} / the subhalo search of Chapter~\ref{ch:5} |
| Paper~5 | Chapter~\ref{ch:8} / the cross-correlation forecast of Chapter~\ref{ch:8} |

- **Suggested fix**: Replace all "Paper~N" references with descriptive chapter references. Keep the `\cite{}` for the publication, but frame the reference around the chapter. For example: `"In Paper~3 \cite{Amerio:2024msp}, the MSP luminosity function..."` → `"In the MSP analysis presented in Chapter~\ref{ch:4} \cite{Amerio:2024msp}, the luminosity function..."`. The collective reference `"Papers~1--5"` in the introduction can become `"the research papers presented in Chapters~\ref{ch:4}--\ref{ch:8}"`.

### Issue 6: Application previews leak implementation details that belong in paper chapters

- **Location**: Application preview paragraphs across Secs 3.1.2, 3.1.3, 3.2.2, 3.3.2, 3.3.3
- **Problem**: Chapter 3 is a background/methods chapter — it should introduce general formalism and indicate where each method is applied, but not specify paper-specific implementation choices. Several previews cross this line:

| Location | Implementation detail that should be deferred |
|---|---|
| 3.1.2, lines 87–89 | "MSP luminosity function parameters $(\langle L_\gamma \rangle, \sigma_L)$," "observational likelihood profile of each globular cluster's gamma-ray flux is combined with the theoretical luminosity function and marginalized over the true flux," "five scaling hypotheses" |
| 3.1.3, line 151 | "CNN trained on ~900k synthetic gamma-ray sky maps" |
| 3.1.3, line 152 | "concrete dropout — a variant that self-learns the optimal dropout probability during training" |
| 3.2.2, line 74 | "9 × 10^5 synthetic gamma-ray sky maps" |
| 3.3.2, line 75 | "EfficientNet V2M architecture," "map2patch algorithm" |
| 3.3.2, line 76 | "trained on 9 × 10^5 synthetic maps" |
| 3.3.3, line 98 | "5-fold cross-validation repeated 20 times" |
| 3.3.3, lines 115–122 | Full equation for $\tilde{p}_\mathrm{unas}(\mathbf{x})$ with covariate shift modulation — this is Paper 4's specific model |

- **The right level of detail**: An application preview should say WHAT general method is used and WHY it fits the problem, then forward-link to the chapter/section where the implementation details live. It should NOT specify architecture names, training set sizes, hyperparameters, or paper-specific equations.
- **Example revision** for Sec 3.3.2 preview:
  - **Current** (5 lines): "In Paper~1, the $dN/dS$ reconstruction employs an EfficientNet V2M architecture applied to Fermi-LAT sky maps via the map2patch algorithm. The network is trained on 9 × 10^5 synthetic maps with a heteroscedastic Gaussian NLL cost function..."
  - **Revised** (2 lines): "In Chapter~\ref{ch:6}, a CNN trained on synthetic gamma-ray sky maps reconstructs the $dN/dS$ using the heteroscedastic loss and Monte Carlo dropout framework described above to estimate both the source-count distribution and its uncertainty (see Section~\ref{sec:...} for the full architecture and training procedure)."
- **Suggested fix**: Trim all application previews to 1–3 sentences that connect the general concept to the physics problem, with a forward link to the relevant chapter. This also naturally resolves the Paper 1 repetition (Issue 7), since most of the repeated content IS the implementation details.

### Issue 7: Hardcoded chapter numbers instead of `\ref` labels (related to Issues 2, 3, 5)

- **Location**: Throughout all section files
- **Instances**:
  - `Chapter~6` used 5 times (in 3.1, 3.2, 3.3)
  - `Chapter~5` used 1 time (in 3.4)
  - `Chapter~9` used 1 time (in 3.3, also wrong — see Issue 2)
  - `Chapter~10` used 2 times (in 3.5, also wrong — see Issue 3)
- **Problem**: Hardcoded numbers will silently become incorrect if chapters are reordered, inserted, or removed. The existing label infrastructure (`ch:5`, `ch:6`, `ch:8`, etc.) is already defined.
- **Suggested fix**: Replace all hardcoded `Chapter~N` with `Chapter~\ref{ch:N}` throughout. A prior review file (`sections/md/3.2_review.md`) already flagged this issue.

### Issue 8: Residual TODO comment in Section 3.5

- **Location**: `3.5_cross_correlations.tex`, line 8
- **Quote**: `% TODO: review in light of the xcorr chapter. are there some overlaps? maybe we can bring or bridge the xcorr formalism appendix here, and remove that appendix.`
- **Problem**: Unresolved editorial note. While it's a comment and won't appear in the PDF, it indicates that the relationship between Section 3.5 and Chapter 8's cross-correlation formalism has not been finalized. Potential duplication between the two should be resolved.
- **Suggested fix**: Review Chapter 8's formalism sections. If Chapter 8 has a self-contained formalism appendix, consider one of: (a) keeping Section 3.5 as the conceptual introduction and removing the Chapter 8 appendix, or (b) keeping Section 3.5 minimal and deferring all equations to Chapter 8. Then remove the TODO.

### Issue 9: Paper 1 repetition across six application previews

- **Location**: Secs 3.1.3, 3.1.4, 3.2.1, 3.2.2, 3.2.3, 3.3.2
- **Problem**: The $dN/dS$ analysis (Chapter 6) is previewed in six separate locations. The phrases "trained on ~900k synthetic maps," "heteroscedastic Gaussian NLL," "concrete dropout," and "deferred to Chapter 6" each appear 3–4 times within ~15 pages. This issue is largely a consequence of Issue 6 (implementation details in previews) — trimming the previews to the conceptual level will naturally eliminate the repetition.

- **Diagnosis by location**:

| Location | Unique conceptual content | Repeated implementation detail |
|---|---|---|
| **3.1.3** preview | Aleatoric + epistemic framework | "900k maps," "concrete dropout," "deferred to Ch 6" |
| **3.1.4** body | Frequentist cross-check, bias estimation | "dropout + heteroscedastic loss" |
| **3.2.1** body | Forward-inverse asymmetry worked example | — (fine as-is) |
| **3.2.2** preview | NPE framing, Gaussian loss vs normalizing flow | "900k maps," "deferred to Ch 6" |
| **3.2.3** body | — | "Bayesian vs frequentist cross-check" (repeats 3.1.4) |
| **3.3.2** preview | — | "EfficientNet V2M," "900k maps," "concrete dropout," "cross-check," "deferred to Ch 6" |

- **Suggested consolidation**: After applying Issue 6 (trimming implementation details), only 3.2.1 (worked example) and 3.2.2 (NPE framing) need substantial Paper 1 content. All others reduce to one-sentence forward links.

---

## Minor Issues (🟢)

### Issue 10: "Application preview" paragraph headers

- **Location**: All sections
- **Problem**: The `\paragraph{Application preview.}` formatting is consistent but unconventional for a thesis. It reads more like a textbook or lecture note device.
- **Suggested fix**: This is a stylistic choice that works well for this chapter's pedagogical purpose. No change needed unless the thesis style guidelines discourage it. If desired, the text could be integrated into the preceding discussion without a separate paragraph header.

### Issue 11: Undefined notation in EM algorithm description

- **Location**: `3.3_ml_astrophysics.tex`, line 109
- **Quote**: `"computing the posterior class responsibilities $\gamma(z_{ik}) = p(k | \mathbf{x}_i)$"`
- **Problem**: The variable $z_{ik}$ is used as the argument of $\gamma$ but is never defined as a latent class indicator variable. The notation follows Bishop (2006) but may confuse readers unfamiliar with that convention.
- **Suggested fix**: Either define $z_{ik}$ explicitly ("where $z_{ik}$ is the latent indicator variable for class $k$") or simplify to $\gamma_{ik} = p(k | \mathbf{x}_i)$.

### Issue 12: Section 3.3.3 back-reference to a non-existent subsection heading

- **Location**: `3.3_ml_astrophysics.tex`, line 84
- **Problem**: Even after fixing the broken `\ref` (Issue 1), the back-reference says "The density estimation task introduced in Section 3.3.1" — but if the subsection heading remains commented out, there is no visible Section 3.3.1 in the text. The reader will see "Section 3.3" (the parent) and "Section 3.3.2" (Neural Networks) but no 3.3.1.
- **Suggested fix**: Uncomment the `\subsection{Learning Tasks}` heading and its label. The content is already in place (lines 7–25); it just lacks the subsection wrapper.

---

## Dimension Scores

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Scientific Rigor | 5 | No errors. Formalism is correct throughout. Claims are appropriately hedged. |
| Citation Quality | 3 | Duplicate bib keys for Paper 4 will produce double bibliography entries. All other citations are accurate and to the right sources. |
| Writing Quality | 4 | Excellent prose — clear, concise, professional. Minor repetition in application previews. |
| Structure & Transitions | 4 | Logical progression, good transitions. Commented-out subsection creates a structural gap. |
| Thesis Integration | 3 | Two incorrect chapter references, hardcoded numbers throughout, residual TODO, duplicate bib keys. |

## Cross-Chapter Integration Assessment

### Chapter 3's Role in the Thesis

Chapter 3 functions as a **shared vocabulary chapter**: it introduces the statistical and ML formalism at a conceptual level so that Chapters 4–8 can apply it without re-deriving it. A survey of all section files in Chapters 4–8 confirms that this contract is fulfilled:

| Downstream Chapter | Methods from Ch. 3 | Back-references? | Re-derivation? | Gaps? |
|---|---|---|---|---|
| **4 (GCE)** | Frequentist inference (§3.1), SBI (§3.2) | Yes | No | None |
| **5 (Subhalos)** | Dataset shift (§3.4), KDE/mixture (§3.3), EM | Yes, extensive | No | None |
| **6 (dN/dS)** | SBI (§3.2), CNN/uncertainty (§3.3) | Yes | No | None |
| **7 (Catalog)** | Frequentist likelihood (§3.1) | Implicit only | No | None |
| **8 (X-corr)** | APS/Limber (§3.5), $\Delta\chi^2$ (§3.5) | Yes, frequent | No | None |

**Key findings:**

1. **No concept gaps.** Every methodological tool used in Chapters 4–8 is introduced in Chapter 3. The coverage is complete.

2. **No unwanted re-derivation.** Chapters 4–8 treat Chapter 3's definitions as given and build on them. The "no-repetition principle" stated in the chapter outline is working.

3. **Appropriate level of repetition.** Chapter 3's treatment is deliberately more general than what appears in the papers. For example, Section 3.4 formalizes dataset shift at a textbook level (covariate shift, prior shift, combined shift), while Paper 4 in Chapter 5 applies these definitions to the specific Fermi-LAT problem. This is expansion, not redundancy — the chapter provides context the papers assume. Similarly, Section 3.5 develops the APS/Limber formalism from first principles, while Chapter 8 applies it to the specific CTAO forecast. The relationship is complementary.

4. **Cross-references are mostly explicit.** Chapters 5 and 8 are exemplary — they reference specific Section numbers in Chapter 3. Chapter 7 relies only implicitly on §3.1 (frequentist inference), which is acceptable since the concepts are standard. Chapter 4 could benefit from one additional explicit reference to §3.1 when discussing Bayes factors and test statistics for model comparison.

5. **The "application preview" paragraphs serve their purpose.** They create bidirectional links: Chapter 3 points forward to the papers, and the paper chapters point backward to Chapter 3. This makes each Part readable independently, as the thesis design principles require.

### Structural Observation

Chapter 3's greatest risk is not missing content but **overloading the reader before the physics**. At ~15 pages of pure methodology before any physics results, the chapter must earn the reader's attention. The current design handles this through the "application preview" paragraphs, which ground each abstraction in a concrete thesis problem. This is effective. The main tension is between:

- **Completeness**: every concept needed later is introduced here (currently achieved)
- **Motivation**: each concept is introduced with a reason to care (currently achieved via previews)
- **Brevity**: the chapter doesn't exhaust the reader (currently borderline — the six Paper 1 previews contribute to a sense of repetition)

The recommended consolidation of Paper 1 previews (Issue 7) would help with brevity without sacrificing completeness.

---

## Recommendations

**Priority 1 (must fix before compilation):**
1. Fix the broken `\ref{sec:3.3.1}` — uncomment the subsection label or update the reference (Issue 1)
2. Fix "Chapter~9" → `Chapter~\ref{ch:5}` in Sec 3.3.3 (Issue 2)
3. Fix "Chapter~10" → `Chapter~\ref{ch:8}` in Sec 3.5 (Issue 3)
4. Deduplicate the Paper 4 bib keys — standardize on one key (Issue 4)
5. Replace all ~30 self-citations (`\cite{Amerio:...}`, `\cite{Pinetti:...}`) with `\ref` cross-references to the relevant thesis chapters (Issue 5). For formalism attribution in Sec 3.5, cite the original external source (Camera et al., Fornengo & Regis) rather than Paper 5.

**Priority 2 (should fix before submission):**
6. Replace all "Paper~N" references with descriptive chapter/section references (Issue 6)
7. Trim application previews to conceptual level — remove implementation details and replace with forward links to the relevant chapters (Issue 7). This naturally resolves the Paper 1 repetition (Issue 10).
8. Replace all hardcoded `Chapter~N` with `\ref` labels (Issue 8)
9. Resolve the TODO in Sec 3.5 regarding overlap with Chapter 8 (Issue 9)
10. Add one explicit back-reference to §3.1 in Chapter 4 when discussing test statistics and Bayes factors
11. Add one explicit back-reference to §3.1 in Chapter 7's introduction

**Priority 3 (polish):**
12. Define $z_{ik}$ in the EM algorithm paragraph or simplify the notation (Issue 12)
13. Uncomment the `\subsection{Learning Tasks}` heading (Issue 13)
