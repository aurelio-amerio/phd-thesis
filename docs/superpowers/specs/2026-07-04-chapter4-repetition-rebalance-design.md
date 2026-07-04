# Chapter 4 Revision: Repetition Reduction + Framing Rebalance

**Date:** 2026-07-04
**Scope:** `chapter_04/sections/4.0`–`4.4` (narrative sections only; `paper_msp/` untouched)
**Inputs:** `repetition_reports/chapter_04_overlaps.md` (verified 2026-07-03), user directives from this session.

## Goals

1. Implement the repetition report in full: A-cluster (narrative-vs-narrative), B-cluster (§4.4 vs paper), C-notes (numeric inconsistencies).
2. Rebalance the pre-paper narrative (§4.0–4.4) away from a pro-DM slant, toward the historically accurate pendulum arc: DM consensus → point-source/MSP consensus → MSP evidence eroding → **question reignited** (not: community re-converted to DM). The chapter never declares what the GCE is.
3. Frame the integrated paper as: one independent study that further sharpens the tension with the MSP interpretation *as it has been formulated so far*.

## Editing conventions

- All new/modified text wrapped in `\blue{...}` (defined at `macros.tex:58`). Apply per sentence/clause — `\blue{}` must not span paragraph breaks or contain `%` comments.
- Replaced sentences are **not deleted**: keep the original as a `%`-commented line directly above the replacement.
- Pure deletions (condensed repetition with no replacement) → comment out, optionally with a `% [dedup: see §X.Y]` note.
- Citations: existing bib keys only (`Buschmann:2020adf`, `Calore_2021`, `manconi2024galacticcenterexcesshighest`, `Fermi-LAT:2015att`, `Macias:2016nev`, `Bartels:2017vsx`, etc. — all already used in the chapter). Any genuinely new key: query NotebookLM first, never hand-write BibTeX.
- Do **not** touch the commented-out block at `4.4:40–64` (recycling-history loophole + email draft). Do not reference it in prose — open question, answer varies by who you ask.

## Per-section plan

### §4.0 introduction (largest rewrite)

- **Numbers (A6 + user directive):** state broad, analysis-spanning ranges — mass "roughly 30–70 GeV", cross section "∼(1–3)×10⁻²⁶ cm³/s" — with a clause noting best-fit values swing from analysis to analysis (verified vs NotebookLM: per-paper fits span 25–55 GeV; review quotes 40–70). This way §4.1.4's per-paper 30–50 GeV is a restriction, not a contradiction.
- **Rebalance para 2–3 into the pendulum arc:**
  - DM consistency stated as *consistency*, not as the leading conclusion.
  - MSP hypothesis with its supporting evidence (NPTF, wavelets, bulge morphology) — acknowledged as having produced a period of near-consensus for the astrophysical origin.
  - Both-sides erosion: the point-source evidence was challenged (Leane & Slatyer) *and defended* (Buschmann et al., Calore et al.); morphology claims contested in both directions; independent LF/LMXB constraints challenge MSPs.
  - Explicit no-consensus sentence: papers actively argue both sides; the question is being reignited rather than settled.
- **Paper framing sentence:** our study = an independent constraint that further sharpens the tension with the MSP interpretation as formulated so far.
- **Roadmap sentence:** update to reflect the arc (4.1 discovery + DM consistency → 4.2 MSP rise → 4.3 stalemate/erosion → 4.4 our independent constraint → paper).
- The `\red{}` transitional paragraph and `\aure{}` note at top stay (author will revisit).

### §4.1

- **A3 (KEEP-primary §4.1.3):**
  - §4.1.2 ~line 75: shorten the Calore stability sentence to point at §4.1.3 for the established numbers; drop the duplicated peak/tail/factor-two enumeration.
  - §4.1.3 ~lines 93–94: rephrase the "Daylan et al. showed" re-attribution as consensus phrasing with citations (no named re-attribution of the same numbers).
- **§4.1.4 tone-down (keep all physics):**
  - "This minimal model succeeds on all three fronts" → soften to consistency language.
  - "one of the most compelling indirect detection signals in the literature" → historicize (sustained interest / leading candidate signal for a decade).
  - Caveat paragraph (ρ⊙ degeneracy, dwarf tension) stays; add one forward-pointing sentence: the same observational properties are also claimed by bulge-tracing astrophysical fits (xref §4.2.1/§4.3.2) — consistency is not uniqueness.

### §4.2

- **A1:** no change to §4.2.1 morphology block (stays primary).
- **A4:** trim line 70's paper preview to a bare pointer to §\ref{sec:msp_paper}; drop 15.8 yr / 157 clusters / "most stringent constraints to date" (all restated in §4.4/paper).
- Line 43 "appeared to decisively favor" already carries the fragility caveat (line 44) — keep; it serves the pendulum arc (this WAS the consensus period).

### §4.3

- **A1 (CONDENSE→xref §4.3.2):** replace lines 53–54 (Macias/Bartels recap) with one sentence + backref to §4.2.1.
- **A2 (systematics triad):** state once in §4.3 opener (line 8, keep). Line 44 (§4.3.1): remove the verbatim "parameterization of the source-count function at the faint end" echo. Line 57 (§4.3.2): shorten enumeration to a backref to the §4.3 opener. §4.4 opener handled below.
- **A7:** reword line 76 (§4.3.2 closer) to tie forward to §4.3.3/§4.4 instead of echoing the opener's no-criterion thesis.
- **C-note (400 vs 200 Lee et al.):** reconcile — make explicit the region/definition difference or align the two numbers after checking Lee:2015fea.
- **§4.3.3:** title **unchanged** ("Recent Revival of the Dark Matter Hypothesis"). Light prose touch: one sentence making explicit that consistency with smooth emission reopens the DM hypothesis but does not demonstrate it — the question is reignited, not answered.

### §4.4 (single combined pass: B1 + B2 + B3 + reframe)

- **B3:** condense the globular-cluster setup (lines 13–14, near-verbatim clone of the paper's `msps_in_globular_clusters.tex`) to one summary sentence; keep line 15 (clean measurement, no ISM systematics — §4.4's own point).
- **B2:** keep the old-age/bulge logic (lines 17–20) but compact — it is the section's legitimate motivating hook and the paper's de facto intro setup.
- **B1:** replace the headline-number block (lines 22–26: 56/157 detections, 8 new, 87 clusters, ⟨L_γ⟩, σ_L) with the qualitative result + pointer to the paper. Must leave enough setup that the paper's abrupt rendered opening ("In this study, we revisit…") still lands.
- **σ_L C-note:** moot if numbers removed; any surviving instance uses 2.7 (matching rendered paper).
- **17–37 vs 3:** keep once (it is the bridge to the List et al. discussion) but reword the punchline sentence (line 31) so it is no longer a verbatim clone of `4.2:68`; `4.4:18` gets a backref to §4.2.2 instead of re-citing Hooper/Holst.
- **A2:** line 7's triad enumeration → "the diffuse-emission systematics discussed in Section~\ref{sec:4.3}".
- **Reframe strong claims:**
  - line 26 "demonstrating that old stellar populations do not produce systematically fainter pulsars" → evidence-level phrasing (no support found for the age-based faintness mechanism).
  - lines 36–37 "remove the astrophysical motivation… no known mechanism" → undermines the leading proposed mechanism; sharpens the tension with the MSP interpretation as formulated so far.
  - Closing framing: converging independent tensions reopen the question; not a verdict.

## Out of scope

- `paper_msp/` sections (published text, untouched).
- §4.5 wrapper, tables, figures.
- The recycling-history loophole (commented block) — stays commented, unreferenced.
- Global spelling normalization; other chapters.

## Verification

1. `latexmk` compile check (no broken refs/labels; `\blue{}` balanced).
2. Fresh-context referee subagent reads revised §4.0–4.4 cold: checks (a) pendulum arc reads neutrally — no residual advocacy in either direction; (b) condensed passages still flow and no xref orphaned; (c) §4.4 still sets up the paper's abrupt opening; (d) numbers consistent (30–70 bracket vs per-paper values; 2.7; Lee et al. reconciliation).
3. Diff review: every changed line is either `%`-commented original or `\blue{}`-wrapped new text.
