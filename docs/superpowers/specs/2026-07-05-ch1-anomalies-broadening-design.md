# Broadening the anomalies discussion in §1.4.7 — design

**Date:** 2026-07-05
**Origin:** Supervisor suggestion — don't focus on the GCE and AMS excesses alone; mention other widely known unresolved problems associated with DM (e.g. small-scale structure in simulations, cusp vs. core).
**Scope:** `chapter_01/sections/1.4_indirect_detection.tex`, §1.4.7 *The Status of the Field*, "Unresolved anomalies" block only. §1.4.3 unchanged (already treats cusp–core in full).
**Budget:** ~280–300 added words total.

## Context established from sources (NotebookLM, 2026-07-05)

- Bullock & Boylan-Kolchin (`Bullock:2017xww`) identify five small-scale challenges with statuses: missing satellites (largely resolved), cusp–core (alleviated, open), too-big-to-fail (alleviated for satellites, persists in field dwarfs), planes of satellites (open), diversity vs. regularity of rotation curves (open).
- Cirelli et al. (`Cirelli:2024ssz`) tabulate detection anomalies with statuses: 511 keV line ("astro?"), 3.5 keV line (disfavoured; XRISM will test), DAMA/LIBRA ("not confirmed" — same-target NaI cross-checks), Fermi 130 GeV line (disappeared), XENON1T excess (disconfirmed — tritium).
- Both reviews frame the anomaly graveyard as case studies in unmodelled systematics — aligns with the existing "methodological case for this thesis" closer.

## Structure

1. **Paragraph A (existing GCE + charged-CR text): keep verbatim.** No edits.
2. **Paragraph B (new, ~80–100 words): other detection anomalies.** Appended after the AMS sentence, one clause per anomaly:
   - INTEGRAL 511 keV line — persists; conventional astrophysical positron sources plausible.
   - 3.5 keV X-ray line — sterile-neutrino interpretation disfavoured (Hitomi, blank-sky); XRISM will test.
   - DAMA/LIBRA annual modulation — unconfirmed by same-target NaI experiments.
   - Closing sentence: the pattern of dissolved anomalies (Fermi 130 GeV line, XENON1T excess) as cautionary tales about systematics → feeds the existing statistical-rigour punchline.
3. **Paragraph C (new, ~150–180 words): structure-formation tensions.** New bold lead-in `\textbf{Small-scale structure tensions.}` (house style: bold lead-ins in §1.4.7).
   - Frame: a different class of problem — not candidate signals, but places where ΛCDM small-scale predictions strain.
   - Backward cross-reference to cusp–core in §1.4.3 (no duplication).
   - Missing satellites: note as largely resolved (galaxy-formation efficiency; ties to the dark-subhalos target paragraph).
   - Still open, per Bullock & Boylan-Kolchin: too-big-to-fail, diversity of dwarf rotation curves, planes of satellites — one to two sentences each at most.
   - Closing sentence: these tensions carry particle-physics information (motivate SIDM/WDM, cross-ref §1.2.1) but are entangled with baryonic feedback modelling — they constrain the nature of DM rather than detect it.

## Citations

- **Reviews only:** `Cirelli:2024ssz` (paragraph B claims) and `Bullock:2017xww` (paragraph C claims). Both already in `bibliography.bib`. **No new bib entries.**
- Originals (Boylan-Kolchin TBTF, Oman diversity, Pawlowski planes, Bulbul/Boyarsky 3.5 keV, ANAIS/COSINE) deliberately deferred; add later only if the supervisor requests.

## Style constraints for the drafter

- Match §1.4.7 house style: long multi-clause sentences, no bullet lists in prose, italics for technical terms on first appearance (*too-big-to-fail*, *planes of satellites*, etc.).
- Paragraph B stays compact — enumeration within prose, not a display list.
- Do not touch the "methodological case for this thesis" paragraph; paragraph B's closing sentence should set it up, not repeat it.
- New prose drafted via the standard pipeline (scientific-prose-writer with fresh-context review), not inline.
