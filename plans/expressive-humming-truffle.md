# Plan: Remove circular Pinetti:2025hgd citations in Chapter 8 introduction

## Context

`Pinetti:2025hgd` is the paper integrated as section 8.4. Sections 8.1–8.3 are thesis-original pedagogy *for* that paper — citing it there is circular. The fix: keep one citation in the transition paragraph (line 57, 8.3.3) and handle the rest minimally.

## Strategy

Most occurrences cite qualitative arguments already self-evident from the surrounding pedagogy. These can simply be **deleted** — no replacement needed. Only a few cite specific quantitative details from the paper's modeling (exposure numbers, sensitivity factors); those benefit from a **cross-reference** so the reader knows where the number comes from.

Available cross-ref labels in 8.4:
- `sec:CTA` — CTAO setup and EGAL survey modeling
- `sec:formalism` — window functions, power spectra, variance
- `app:expo` — off-source 50 h scenario

---

## Occurrences (10 in compiled `.tex` files)

### `chapter_08/sections/8.2_cross_correlation_technique.tex`

| # | Line | Sentence gist | Action |
|---|------|---------------|--------|
| 1 | 19 | DM window function formula (already cross-refs sec:1.4) | **Remove** `~\cite{Pinetti:2025hgd}` — standard formula, already grounded |
| 2 | 56 | Better point-source sensitivity → lower blazar floor | **Remove** — qualitative argument, self-evident |
| 3 | 61 | Cross-corr SNR weakly sensitive to threshold | **Remove** — qualitative; line 63 already says "derived in the paper that follows" |
| 4 | 101 | 2MASS/2MRS redshift distributions match DM window for CTAO energies | **Remove** — follows logically from sec 8.2.1 discussion |

### `chapter_08/sections/8.3_ctao.tex`

| # | Line | Sentence gist | Action |
|---|------|---------------|--------|
| 5 | 28 | DM contribution peaks at z ≲ 0.1 | **Remove** — already established in sec 8.2.1 |
| 6 | 38 | EGAL is a CTAO Key Science Project | **Remove `Pinetti:2025hgd` from compound cite** → keep `~\cite{CTAConsortium:2017dvg}` only |
| 7 | 43 | Effective average exposure ~3 h per point | **Replace** → `(see Section~\ref{sec:CTA})` — specific modelling number |
| 8 | 45 | Exposure fluctuations ~10% | **Replace** → `(see Section~\ref{sec:CTA})` — specific modelling number |
| 9 | 48 | Off-source scenario: ~50 h, factor ~4 gain | **Replace** → `(see Appendix~\ref{app:expo})` — specific result |
| 10 | 57 | Transition: "The paper that follows..." | **Keep** `~\cite{Pinetti:2025hgd}` — designated introduction of the paper |

### `.md` draft files — **skip** (old artifacts, not compiled)

---

## Implementation

1. **8.2_cross_correlation_technique.tex** — delete the `~\cite{Pinetti:2025hgd}` fragment on lines 19, 56, 61, 101.

2. **8.3_ctao.tex**:
   - Line 28: delete `~\cite{Pinetti:2025hgd}`
   - Line 38: `~\cite{CTAConsortium:2017dvg,Pinetti:2025hgd}` → `~\cite{CTAConsortium:2017dvg}`
   - Line 43: `~\cite{Pinetti:2025hgd}` → `~(see Section~\ref{sec:CTA})`
   - Line 45: `~\cite{Pinetti:2025hgd}` → `~(see Section~\ref{sec:CTA})`
   - Line 48: `~\cite{Pinetti:2025hgd}` → `~(see Appendix~\ref{app:expo})`
   - Line 57: no change

## Verification

- Grep `chapter_08/` for `Pinetti:2025hgd` — only line 57 of `8.3_ctao.tex` should remain.
- Compile and check for undefined `\ref` warnings (the labels `sec:CTA` and `app:expo` already exist in the paper).
