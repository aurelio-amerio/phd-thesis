# Eckner Quick Pass — Design

**Date:** 2026-08-27
**Status:** approved in chat (brainstorming session), pending spec review
**Input:** `reply_eckner.md` (authoritative item ledger: IDs, verified facts, approved
draft prose, status table) + 30 Review Mode annotations on that file (author approvals
and modifications, all fetched 2026-08-27).

## Scope

All **38 non-deferred (🟡) items** from `reply_eckner.md`. The 8 deferred (⏳) items are
explicitly OUT of scope: E-4.1, E-4.3, E-4.5, E-4.6, E-4.8 (chapter-4 rebalance,
substantive pass), E-3.1 (terminology decision), E-6.4, E-6.7 (need author input).

Author decisions from the annotation pass (override the reply-doc drafts where they
conflict):

| Item | Author modification |
|------|--------------------|
| E-4.2 | Change the quoted ρ⊙ range itself and cite the newer papers — do NOT append the long clause drafted in the reply doc. Updated range must be consistent with de Salas & Widmark (Gaia-era local determinations 0.4–0.6, global analyses 0.3–0.5 GeV/cm³); exact wording at implementation. |
| E-4.12 | Do NOT modify integrated-paper text. Emphasis goes in thesis-authored text only: §4.6 summary if thesis-authored (verify at implementation), else `conclusion/conclusion.tex`. |
| E-1.2 | Minimal edit only, along the lines of "…generally weaker due to the experimental difficulties in detecting them…". |
| E-2.2 | Concise version: "…for the GeV dark matter searches undertaken in this thesis. On the other hand, at TeV energies…" — no filler connectives or qualifiers. |
| E-5.1 | Short parenthetical only: mass at the time of formation/accretion/infall. |
| E-3.3 | Re-derive integration so the KL remark reads naturally; first verify where/whether KL is formally defined in §3.2. |
| E-1.6 | Draft is direction only — rethink how to properly address the TeV/CTAO outlook point. |
| E-2.1 | Draft approved but double-check the phrasing. |
| E-5.3 | Typos marked `\blue{}` (default confirmed). |
| E-5.4 | Option (a): demote inner headers, all 3 sites. |

All other annotated items ("ok" / "sounds good" / "agree"): apply as drafted in
`reply_eckner.md`. Un-annotated 🟡 items (E-4.9/E-G.1, E-6.6, E-6.8, E-6.9, E-7.2,
E-7.3, E-8.1, E-M.1, E-M.2): in scope per author decision, apply as drafted.

## Non-negotiable conventions

- All new/reworded prose wrapped in `\blue{}` (including typo fixes, per E-5.3 default).
- No BibTeX entries written by hand — InspireHEP (or arXiv) only. Papers not found
  there go in an MD artifact (authors, year, title, journal) with `\aure{}` placeholders
  in the LaTeX.
- Draft prose lives in `reply_eckner.md`; this spec holds structure only.
- Vocabulary blacklist and sentence-length ceiling checked before presenting prose.
- Review passes run in fresh-context subagents, never inline.
- **Model policy for prose:** any subagent that writes or rewrites prose (drafting,
  humanizer, scientific-writing review) runs on Fable or Opus 4.6 only — never Sonnet
  or Haiku (author: worse at prose writing). Author directive (2026-08-27): do NOT use
  the `scientific-prose-writer` agent definition; dispatch generic agents with the
  model set explicitly. Since the Agent tool's per-call `model` only takes aliases and
  `opus` resolves to Opus 5 (verified), generic prose agents run with
  `model: "fable"`. Mechanical tasks (grep sweeps, bib fetches) are exempt and may use
  any model.
- `\aure{}` WIP markers are never silently deleted.

## Execution order

### Batch 1 — Bibliography fetch (blocking; everything downstream cites these)

For each: check `bibliography.bib` first; fetch only what is missing.

| arXiv / DOI | For items |
|---|---|
| astro-ph/0305003 (Pooley) | E-4.4 |
| 1302.2549 (Bahramian) | E-4.4 |
| 1711.05127 (Eckner 2018) | E-4.4 (likely already cited in Ch. 4 — check) |
| 2012.11477 (de Salas & Widmark) | E-4.2 |
| 1901.07025 (Song) | E-4.7 |
| 2212.08528 (Clark/TRAPUM) | E-4.11 |
| 2512.16699 (Berteaud) | E-4.11 |
| 1612.08002 (Ahlers & Mertsch) | E-1.3 (one ref suffices; 1812.05682 optional) |
| 2409.07515 (De la Torre Luque) | E-1.5 |
| hep-ph/0512090 (Cirelli MDM) | E-1.6 |
| one CTAO sensitivity ref (2007.16129 preferred) | E-1.6 |
| DOI 10.1126/science.1106924 (Grenier 2005 — **no arXiv**; InspireHEP by DOI, else MD artifact + `\aure{}`) | E-2.1 |
| 1602.07246 (Acero, Fermi IEM) | E-2.1 |
| 1603.06978 (NGC 1275 ALP) | E-1.1, E-2.3 |
| 1410.3747 (SN1987A ALP) | E-1.1, E-2.3 |
| 2107.09070 (List, Rodd & Lewis) | E-6.3 (distinct from List:2025qbx — verify) |
| 2307.12546 (4FGL-DR4) | E-7.1 |

### Batch 2 — Mechanical fixes (single compile-verified batch)

- E-6.9: promote `\subsection`→`\section` etc. in
  `chapter_06/sections/paper_dnds/sections/appendix_further_tests.tex`, mirroring the
  Ch. 5 `subappendices` convention; recompile; then E-6.5: confirm the
  `\ref{sec:agal-var}` reference renders ("Appendix 6.A.x").
- E-5.4: demote inner headers at the 3 empty-container sites
  (`mixture_model_and_limits.tex`, `statistical_analysis.tex`, `dm_subhalos_model.tex`).
- Whole-thesis sweeps: `loose`→`lose` (E-6.6 ×2, E-7.3, grep for others);
  `aleatory`→`aleatoric` (E-6.8 + grep).
- E-5.3: "at lest"→"at least" (`5.4_unassociated_sources.tex:53`).
- E-3.5 part 1: "(statistical)uncertainty" spacing + nearby "undertainties" typo
  (`3.3_ml_astrophysics.tex:65,67`).

### Batch 3 — Prose edits, chapter by chapter

Order: Ch. 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → cross-chapter style items.

- **Ch. 1:** E-1.1 (PBH/ALP closing ¶, cross-ref §2.2.2 rather than re-introduce
  candidates — verify Ch. 1 introduces ALPs/PBHs earlier), E-1.2 (minimal), E-1.3,
  E-1.4 (verify [129]=Fermi-LAT:2015att against compiled PDF first), E-1.5, E-1.6
  (rethought draft).
- **Ch. 2:** E-2.1 (phrase double-checked), E-2.2 (concise), E-2.3 (cross-link with
  E-1.1 paragraph).
- **Ch. 3:** E-3.2, E-3.3 (natural integration; verify KL definition location), E-3.4,
  E-3.5 part 2 (seed-variability sentence).
- **Ch. 4:** E-4.2 (range change + newer refs), E-4.4 (both edits at
  `4.2_msp_hypothesis.tex:71` and `:73`), E-4.7 (+ check §4.3.2 flow and §4.4 summary
  consistency), E-4.10 (paper-text addition, approved as-is; needs the §4.5.5 label),
  E-4.11 (verify against published paper wording; keep `\blue{}`), E-4.12
  (thesis-authored text only).
- **Ch. 5:** E-5.1 (concise), E-5.2.
- **Ch. 6:** E-6.1 (avoid double "equally well"), E-6.2, E-6.3 (footnote-style addition
  to verbatim paper text).
- **Ch. 7:** E-7.1, E-7.2 (+ keep `conclusion.tex:124` consistent).
- **Ch. 8:** E-8.1.
- **Style:** E-M.1 (2 sites, different replacements), E-M.2 immediate fix at
  `conclusion.tex:59`.

### Batch 4 — Review passes (fresh-context subagents, per author's hard requirement)

- After each chapter's edits: dispatch one fresh-context subagent running
  humanizer + scientific-writing review over the edited sections; apply accepted
  findings; re-check vocabulary blacklist.
- E-M.2 full pass: dedicated humanizer subagent on `conclusion/conclusion.tex` and the
  chapter intros Eckner flagged; review the diff before accepting; extend the
  vocabulary blacklist with confirmed vetoes.

### Batch 5 — Acronym sweep (last, to avoid edit conflicts)

- E-G.1 / E-4.9: run `/acronyms` chapter by chapter (MSP, GCE, NFW, WIMP, NPTF, SCD,
  CNN, SBI, dSph at minimum), converting literal acronyms to glossary macros.

### Batch 6 — Verification and bookkeeping

- Full `latexmk` compile: zero new errors; appendix numbering ("6.A…") and the E-6.5
  cross-reference verified in the PDF.
- `reply_eckner.md`: statuses 🟡→✅ item by item, summary table + counts updated.
- Resolve the 30 Review Mode annotations with per-item completion notes; re-open
  Review Mode.

## Risks / notes

- E-4.10 and E-4.11 touch integrated-paper text by explicit author approval; E-4.12
  must not. Keep this asymmetry visible during implementation.
- E-4.4's long replacement must coordinate with the deferred E-4.5 (shared
  density/channel argument) — write it self-contained but avoid claims E-4.5 will
  restate.
- Bib keys in reply-doc drafts are placeholders (`<Pooley2003>` etc.) — replace with
  the real keys produced by Batch 1.
