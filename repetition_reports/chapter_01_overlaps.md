# Chapter 1 — Intra-Chapter Overlap Report

## Sections analyzed / excluded
Narrative files read in full (wrapper order):
- `chapter_01/sections/1.0_introduction.tex` (untitled intro)
- `chapter_01/sections/1.1_evidence_for_dark_matter.tex` (§1.1, subsecs 1.1.1–1.1.3)
- `chapter_01/sections/1.2_wimp_paradigm.tex` (§1.2, subsecs 1.2.1–1.2.4)
- `chapter_01/sections/1.3_searching_for_dark_matter.tex` (§1.3, subsecs 1.3.1–1.3.2)
- `chapter_01/sections/1.4_indirect_detection.tex` (§1.4, subsecs 1.4.1–1.4.7)
- `chapter_01/sections/1.5_summary.tex` (§1.5, Summary)

Excluded (not read, not cited as a source): `chapter_01/sections/1.2_wimp_paradigm.backup.tex` (stale backup).

Note on §1.4 subsection numbering (labels only in source; numbers inferred by order): 1.4.1 Annihilation and Decay Physics, 1.4.2 Spectral Features, 1.4.3 Density Profiles, 1.4.4 Flux Factorization, 1.4.5 Observational Targets, 1.4.6 Multi-Messenger, 1.4.7 Status of the Field.

## A. Narrative-vs-narrative overlaps  [PRIMARY]

### A1. Fermi-LAT stacked dSph analysis: 15→50 dwarfs, thermal-relic exclusion below ~100 GeV in b̄b — Severity: High
The same result (with the same two citations, the same "15 dSphs → 50 dSphs / 14 years" evolution, and the same "excluded the thermal relic cross-section below ~100 GeV in the b̄b channel") is stated in full twice inside §1.4, in two different subsections.
- Occurrence 1: `1.4_indirect_detection.tex` · §1.4.5 (Targets) · ~line 336 — "The original combined analysis of 15 kinematically confirmed dSphs excluded the thermal relic cross-section ($\langle \sigma v_\text{rel} \rangle \simeq 2.2 \times 10^{-26}$ cm$^3$/s) for dark matter masses below $\sim 100$ GeV in the $b\bar{b}$ channel ...; the most recent legacy analysis extends this to 50 dSphs with 14 years of data".
- Occurrence 2: `1.4_indirect_detection.tex` · §1.4.7 (Status) · ~lines 397–399 — "The original combined analysis of 15 dSphs with six years of data excluded the thermal relic cross-section for dark matter masses in the range $\sim 10$--$100$ GeV in the $b\bar{b}$ channel ...; The most recent legacy analysis extends the sample to 50 dSphs and 14 years of Fermi-LAT exposure".
- (Supporting recap, expected: `1.5_summary.tex` · ~line 17 — "Fermi-LAT constraints from dwarf galaxies already excluding the thermal relic cross-section for masses below ${\sim}\,100$~GeV in the $b\bar{b}$ channel".)
- Recommendation: CONDENSE→xref. Keep §1.4.7 (Status) as the primary location for the numeric result, since that subsection's explicit purpose is the current-status roundup; in §1.4.5 (Targets) shrink the two-sentence numeric restatement to the qualitative point ("stacked dSph analyses give the tightest cross-section limits to date; see §1.4.7") plus the Chapter 5 pointer. Avoid the internal 10–100 GeV vs "below 100 GeV" mismatch by quoting the range in one place only.

### A2. Galactic Center excess: ~40–70 GeV WIMP → b̄b at thermal rate, MSP alternative, Chapter 4 — Severity: High
The GCE is described in near-identical substantive detail twice within §1.4 (Targets and Status), each time giving the mass window, the b̄b channel, the thermal cross-section, the millisecond-pulsar competitor, and the Chapter 4 pointer.
- Occurrence 1: `1.4_indirect_detection.tex` · §1.4.5 (Targets) · ~lines 318–323 — "the so-called Galactic Center excess (GCE) ... consistent with the predictions for a $\sim 40$--$70$ GeV dark matter particle annihilating into $b\bar{b}$ quarks at a rate close to the thermal relic value ... an unresolved population of millisecond pulsars in the Galactic bulge provides an equally plausible astrophysical explanation ... motivates the dedicated analysis in Chapter~\ref{ch:4}".
- Occurrence 2: `1.4_indirect_detection.tex` · §1.4.7 (Status) · ~lines 411–413 — "The Galactic Center gamma-ray excess --- a signal first reported in 2009 and consistent with a $\sim$40--70 GeV dark matter particle annihilating into $b\bar{b}$ at the thermal cross-section --- remains the most debated ... Chapter~\ref{ch:4} ... challenging the leading astrophysical interpretation of the excess as an unresolved population of millisecond pulsars".
- (Partial third mention, different numbers: `1.2_wimp_paradigm.tex` · §1.2.4 · ~line 243 — "GeV-scale candidates relevant to the Galactic Center excess ... a $\sim 30$--$50\,\mathrm{GeV}$ \WIMP annihilating at $\langle\sigma v\rangle \approx (1$--$3)\times 10^{-26}$" — note the 30–50 GeV here vs 40–70 GeV in §1.4.)
- Recommendation: CONDENSE→xref. Keep §1.4.5 (Targets) as the primary GCE description (it sits with the Galactic Center target and the Chapter 4 motivation reads naturally there). In §1.4.7 (Status) reduce to a one-line entry ("the GCE remains the most debated anomaly (§1.4.5)") retaining only the "first reported 2009 / most debated" framing. Also reconcile the 30–50 vs 40–70 GeV figures across §1.2.4 and §1.4.

### A3. Definition of the "WIMP miracle" restated repeatedly — Severity: High
The WIMP-miracle statement (stable particle, electroweak-scale mass and coupling, thermal production, yields the observed relic abundance) is given in near-full form three times within §1.2, in addition to the expected intro preview and summary recap. Line 151 is nearly verbatim to the intro at line 12.
- Occurrence 1: `1.2_wimp_paradigm.tex` · §1.2 opening · ~line 16 — "the so-called \emph{\WIMP miracle} --- the observation that a thermal relic with electroweak-scale mass and coupling naturally reproduces the observed dark matter abundance".
- Occurrence 2: `1.2_wimp_paradigm.tex` · §1.2.1 · ~line 45 — "The observation that a particle with weak-scale mass and coupling naturally yields the observed relic abundance --- the \WIMP miracle --- has made \glspl{WIMP_} one of the dominant paradigms ... for over two decades".
- Occurrence 3: `1.2_wimp_paradigm.tex` · §1.2.2 · ~line 151 — "This result is known as the \emph{\WIMP miracle}: a stable particle with mass and coupling strength at the electroweak scale, produced thermally in the early Universe, naturally yields a relic abundance consistent with the observed dark matter density".
- (Expected preview/recap, keep: `1.0_introduction.tex` · ~line 12; `1.5_summary.tex` · ~line 10.)
- Recommendation: KEEP-primary / CUT-secondary. The derivation-anchored statement at §1.2.2 line 151 is the natural home (it is the payoff of the freeze-out calculation). Cut the full restatement at §1.2.1 line 45 to a brief "the WIMP miracle (Section 1.2.2)" and trim the §1.2 opening line 16 to a one-clause forward reference rather than a full definition. The "over two decades / dominant paradigm" framing also appears at both line 16 and line 45 and should live in only one.

### A4. "The same cross-section that sets the relic abundance also fixes the present-day annihilation rate" — Severity: Medium
This thesis-motif sentence is stated in full three times across §1.2 subsections (and echoed in §1.4).
- Occurrence 1: `1.2_wimp_paradigm.tex` · §1.2.1 · ~line 48 — "The same annihilation cross section that sets the relic density also fixes the rate at which \glspl{WIMP_} annihilate into gamma rays in present-day halos".
- Occurrence 2: `1.2_wimp_paradigm.tex` · §1.2.2 · ~lines 165–166 — "the cross section fixed by Eq.~\eqref{eq:relic_abundance} also sets the rate at which dark matter annihilates in present-day astrophysical environments. This connection ... further motivates the gamma-ray searches".
- Occurrence 3: `1.2_wimp_paradigm.tex` · §1.2.4 · ~lines 253–254 — "the freeze-out cross section also fixes the galactic-halo annihilation rate, providing the cleanest target for indirect-detection experiments".
- Recommendation: KEEP-primary / CUT-secondary. Keep the statement at §1.2.2 (line 165), where it directly follows the relic-abundance equation. Reduce the §1.2.1 (line 48) and §1.2.4 (line 253) instances to short connective clauses; §1.2.4 legitimately needs a version because it qualifies the s-wave case, but it can lean on the §1.2.2 statement rather than re-asserting it in full.

### A5. Candidate mass range "roughly ninety orders of magnitude, from ultra-light bosons to primordial black holes" — Severity: Medium
The same span-and-endpoints phrasing recurs three times inside §1.2 (opening, figure caption, and §1.2.1 body), beyond the expected intro preview.
- Occurrence 1: `1.2_wimp_paradigm.tex` · §1.2 opening · ~line 10 — "viable masses span roughly ninety orders of magnitude, from ultra-light bosonic fields with $m \sim 10^{-22}$~eV ... up to macroscopic primordial black holes".
- Occurrence 2: `1.2_wimp_paradigm.tex` · §1.2.1 Fig. caption · ~line 30 — "viable candidate masses span roughly ninety orders of magnitude, from ultra-light bosonic fields to macroscopic primordial black holes".
- Occurrence 3: `1.2_wimp_paradigm.tex` · §1.2.1 body · ~lines 37–38 — "the range of possibilities is enormous: from ultra-light bosonic fields near $10^{-22}$~eV ... up to macroscopic primordial black holes of tens of solar masses".
- (Expected preview: `1.0_introduction.tex` · ~line 11 — "span nearly ninety orders of magnitude in mass, from ultralight axions to primordial black holes".)
- Recommendation: KEEP-primary / CUT-secondary. Keep the §1.2.1 body statement (line 37–38, which carries the physical detail: de Broglie floor, interaction-strength range) plus the figure caption (captions may restate). Cut the §1.2 opening restatement at line 10 to a brief pointer, since §1.2.1 opens a page later with the same content.

### A6. dSph mass-to-light ratios (tens → thousands, Segue 1) and "most dark-matter-dominated objects known" — Severity: Medium
The dwarf-spheroidal M/L characterization is given in substantive detail in the evidence section and again in the targets section.
- Occurrence 1: `1.1_evidence_for_dark_matter.tex` · §1.1.1 · ~lines 52–53 — "extreme mass-to-light ratios: from $M/L \sim 10\,M_\odot/L_\odot$ in the classical dwarfs ... to well over a thousand in ultra-faint systems like Segue~1 ... establishing \glspl{dSph_} as the most dark-matter-dominated objects known".
- Occurrence 2: `1.4_indirect_detection.tex` · §1.4.5 (Targets) · ~line 327 — "Dwarf spheroidals are among the most dark matter--dominated objects known: ... mass-to-light ratios ranging from tens of $M_\odot/L_\odot$ for classical dwarfs like Sculptor to thousands for ultrafaint dwarfs such as Segue~1".
- Recommendation: CONDENSE→xref. Keep §1.1.1 as the primary quantitative treatment (it is the evidence-for-DM context and introduces the Wolf mass estimator). In §1.4.5 trim to "the most dark-matter-dominated objects known (§1.1.1)" and keep only what the targets discussion adds (low backgrounds, cleanest targets).

### A7. Direct detection and collider searches probe the scattering cross-section, not the annihilation cross-section — Severity: Medium
The "direct/collider constrain σ_scatter, only indirect measures ⟨σv⟩" point is made at the close of both §1.3 subsections, then again opening §1.4 and in the summary.
- Occurrence 1: `1.3_searching_for_dark_matter.tex` · §1.3.1 · ~line 68 — "Direct detection constrains the WIMP--nucleon scattering cross-section but is insensitive to the annihilation cross-section $\langle \sigma v_\mathrm{rel} \rangle$ that determines the thermal relic abundance --- the observable probed by indirect detection".
- Occurrence 2: `1.3_searching_for_dark_matter.tex` · §1.3.2 · ~line 93 — "direct detection and collider searches constrain the scattering cross-section, but neither directly measures the annihilation cross-section $\langle \sigma v_\text{rel} \rangle$ that determines the thermal relic abundance".
- (Also `1.4_indirect_detection.tex` · §1.4 opening · ~line 7, and `1.5_summary.tex` · ~line 13 — both expected as section-open / recap.)
- Recommendation: KEEP-primary / CUT-secondary. Occurrences 1 and 2 sit only a few paragraphs apart and make the same claim. Keep the §1.3.2 closing statement (line 93), which serves as the transition into §1.4, and drop the near-duplicate at the end of §1.3.1 (line 68) or reduce it to the mass-range-limitation point specific to direct detection.

### A8. Galactic Center flux exceeds an individual dwarf by ~3 orders of magnitude — Severity: Medium
Stated once in the Galactic Center paragraph and again in the dwarf paragraph of the same subsection (§1.4.5).
- Occurrence 1: `1.4_indirect_detection.tex` · §1.4.5 · ~line 309 — "the predicted flux from the inner $10^\circ$ exceeds that from any individual dwarf galaxy by more than three orders of magnitude".
- Occurrence 2: `1.4_indirect_detection.tex` · §1.4.5 · ~line 329 — "The expected dark matter flux from any individual dwarf is far smaller than from the Galactic Center --- roughly three orders of magnitude lower for a typical system".
- Recommendation: KEEP-primary / CUT-secondary. Keep the statement in the Galactic Center paragraph (line 309, where the number is derived from the NFW comparison). In the dwarf paragraph replace "roughly three orders of magnitude lower" with a back-reference ("far smaller than the Galactic Center, as noted above") so the contrast is retained without re-quoting the figure.

### A9. Gamma-rays propagate intact whereas charged cosmic-ray directions are erased by magnetic fields — Severity: Medium
This contrast is made three times: in §1.4.2 (both prose and figure caption), in §1.4.6, and recapped in §1.5.
- Occurrence 1: `1.4_indirect_detection.tex` · §1.4.2 · ~line 88 — "unlike charged cosmic rays, whose spectral structures are smeared by propagation through galactic magnetic fields, sharp features in the gamma-ray spectrum propagate intact from source to detector".
- Occurrence 2: `1.4_indirect_detection.tex` · §1.4.6 · ~line 377 — "Charged cosmic rays ... galactic magnetic fields randomize their arrival directions, erasing all spatial information and leaving only the energy spectrum as the main observable".
- (Also Fig. caption `1.4.2` ~line 109 "Unlike the case for charged cosmic rays, these sharp features propagate intact"; and recap `1.5_summary.tex` ~line 14.)
- Recommendation: CONDENSE→xref. Keep the §1.4.2 statement (line 88) as the primary, since it motivates the spectral-feature strategy. In §1.4.6, where the point is about cosmic rays as a messenger, keep the phrasing but it need not re-derive the gamma-ray side; a brief "(cf. the intact propagation of gamma-rays, §1.4.2)" suffices.

### A10. Direct-detection / collider results recapped in the Status subsection — Severity: Low
The Status subsection (§1.4.7) re-summarizes numeric results already given in §1.3, in a deliberate roundup.
- Occurrence 1: `1.3_searching_for_dark_matter.tex` · §1.3.1 · ~lines 54–56 (LZ/XENONnT/PandaX-4T, $\sigma_\text{SI} \lesssim 10^{-47}$–$10^{-46}$ cm$^2$) and §1.3.2 · ~line 85 (squarks/gluinos to 1–2 TeV).
- Occurrence 2: `1.4_indirect_detection.tex` · §1.4.7 · ~lines 405–406 — "dual-phase liquid xenon detectors --- LZ, XENONnT, and PandaX-4T --- has pushed the spin-independent WIMP--nucleon cross-section below $10^{-46}$ cm$^2$ ... excluding strongly interacting superpartners (squarks, gluinos) up to masses of 1--2 TeV".
- Recommendation: CONDENSE→xref (light touch). A status roundup legitimately recaps; keep it but add "(§1.3)" pointers and ensure it does not re-introduce numbers with different precision than §1.3.

### A11. SIDM produces cored (rather than cuspy) profiles via elastic scattering — Severity: Low
- Occurrence 1: `1.2_wimp_paradigm.tex` · §1.2.1 · ~line 78 — "self-interacting dark matter (SIDM), originally proposed by Spergel and Steinhardt ... to thermalize the inner regions of halos through elastic scattering and so produce cored rather than cuspy density profiles".
- Occurrence 2: `1.4_indirect_detection.tex` · §1.4.3 · ~line 204 — "self-interacting dark matter (with $\sigma/m \approx 0.5$--$10$ cm$^2$/g) transfers heat to halo centers and produces cores of the observed size".
- Recommendation: CONDENSE→xref. Contexts differ (candidate landscape vs cusp–core solutions), so a full cut is not warranted; add a cross-reference from §1.4.3 to §1.2.1 for the SIDM definition and keep only the cusp–core-specific detail (σ/m range) there.

### A12. Thermal-relic benchmark value 2.2×10⁻²⁶ cm³/s quoted repeatedly — Severity: Low
The canonical number appears in §1.2.2 (line 148, derived), §1.2.3 (line 216), §1.4.5 (line 336), and §1.5 (line 11), plus the §1.2 preview (line 19).
- Occurrence 1: `1.2_wimp_paradigm.tex` · §1.2.2 · ~line 148 — "$\langle \sigma v\rangle_\mathrm{cosmo} \approx 2.2 \times 10^{-26}$~cm$^3$/s".
- Occurrence 2: `1.2_wimp_paradigm.tex` · §1.2.3 · ~line 216 — "the thermal benchmark $\langle \sigma v \rangle_\mathrm{cosmo} \approx 2.2 \times 10^{-26}~\mathrm{cm}^3/\mathrm{s}$".
- Recommendation: KEEP. This is a benchmark constant whose reuse is legitimate connective tissue; no change needed beyond ensuring the value (and not a variant like the 1–3×10⁻²⁶ at §1.2.4 line 243) is quoted consistently.

## B. Narrative-vs-paper over-anticipation  [FLAG ONLY]
N/A — Chapter 1 has no integrated paper. Section B proposes nothing.

## C. Structural notes / borderline cases
- **Numeric inconsistencies surfaced by the overlaps (worth reconciling, not repetition per se):** the GCE mass window is quoted as "30–50 GeV" at §1.2.4 (line 243) but "40–70 GeV" at §1.4.5 (line 319) and §1.4.7 (line 411); the Sun–Galactic-Center distance is $r_\odot \simeq 8.12$ kpc at §1.4.3 (line 191) but $r_\odot \simeq 8.33$ kpc at §1.4.4 (line 249); the freeze-out relative velocity is $v_\mathrm{rel}\sim 0.2\,c$ at §1.2.2 (line 139) / §1.2.4 (line 240) but $\sim 0.3\,c$ at §1.2.4 (line 232).
- **§1.4 Status (1.4.7) is by design a recap subsection**, which drives clusters A1, A2, A9, A10. Recap is expected, but here it re-states results at near-full detail rather than signposting; the High-severity A1/A2 flags reflect that the two §1.4 subsections duplicate the same numbers and citations, not merely that a status roundup exists.
- **Intro (1.0) and Summary (1.5) behave as intended**: they preview/recap (85% dark, WIMP miracle, 2.2×10⁻²⁶ benchmark, gamma-rays-as-best-messenger) without re-deriving. These occurrences are listed only as supporting context under the relevant clusters, not as the primary redundancy.
- **Freeze-out velocity vs halo velocity mapping** (§1.2.2 lines 138–140 → §1.2.4 lines 224–233) is a legitimate preview→detail structure with an explicit forward reference; not flagged as redundant.
