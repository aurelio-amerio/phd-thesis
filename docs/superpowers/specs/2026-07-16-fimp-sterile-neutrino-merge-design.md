# Design: Merge FIMP/freeze-in into the sterile-neutrino paragraph (§1.2.1)

**Date:** 2026-07-16
**File affected:** `chapter_01/sections/1.2_wimp_paradigm.tex` (§1.2.1 only)

## Motivation

- Supervisor feedback: sterile neutrinos are a FIMP candidate — Dodelson–Widrow
  oscillation production is the textbook freeze-in example (cited as such by
  Hall et al., `Hall:2009bx`).
- The author finds the current transition sentence ("Mass is only one way of
  organizing the candidate space. Two further distinctions cut across it...")
  unnatural. With freeze-in moved into the mass-ordered survey, the
  "two cross-cutting distinctions" frame collapses: only the cold/collisionless
  question remains as a coda, and the production-mechanism axis needs no
  separate emphasis.

## Structural decisions

New paragraph order in §1.2.1:

1. Opening (landscape, Tremaine–Gunn, cold vs warm) — unchanged.
2. Axions — unchanged.
3. **Merged FIMP + sterile-neutrino paragraph** (replaces the current
   sterile-neutrino paragraph).
4. WIMPs — one optional clause of contrast with FIMPs (thermal equilibrium →
   freeze-out); otherwise unchanged.
5. PBHs — unchanged.
6. Cold/collisionless coda (WDM + SIDM) with a rewritten light transition.
7. Closing narrow-to-WIMP paragraph — unchanged.

Per-change details:

- **Roadmap sentence** (currently "...before turning to two classifications
  that cut across it"): survey runs by increasing mass, closing with the
  question of whether dark matter is truly cold and collisionless. No
  "classifications that cut across" language.
- **Merged paragraph**: physical picture first — candidates coupled so feebly
  they never reach thermal equilibrium; abundance built gradually via rare
  decays and 2→2 scatterings and grows with the coupling (*freeze-in*, FIMPs,
  `Hall:2009bx`); forward-reference the freeze-out contrast to §1.2.2. Then
  keV sterile neutrinos as the canonical realization: Dodelson–Widrow
  non-resonant and Shi–Fuller resonant oscillation production presented as
  freeze-in; Lyman-α / satellite-count bounds; radiative decay X-ray line.
  All existing citations retained (`Dodelson:1993je`, `Shi:1998km`,
  `Boyarsky:2018tvu`, `Drewes:2016upu`, `Hall:2009bx`).
- **Delete** the standalone FIMP block and its "Mass is only one way..."
  transition — content absorbed into the merged paragraph.
- **WDM/SIDM coda transition**: single-question opener (does dark matter
  depart from cold and collisionless?), no "second distinction" numbering.
  The existing back-reference to resonantly produced sterile neutrinos as a
  WDM realization stays.
- All new/reworded fragments wrapped in `\blue{}`; commented-out legacy lines
  may be pruned where they duplicate absorbed content.

## Out of scope

- No changes to §1.2.2–1.2.4.
- No new citations; no bibliography edits.
- No changes to the section intro (lines before §1.2.1) beyond none needed.
