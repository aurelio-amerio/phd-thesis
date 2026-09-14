# Acronym inventory — thesis prose (phase 1)

**Date:** 2026-09-01
**Plan:** `docs/superpowers/plans/2026-09-01-acronym-consistency.md` (Task 1, Steps 2–4)
**Spec:** `docs/superpowers/specs/2026-09-01-acronym-consistency-design.md`
**Status:** awaiting author checkpoint (plan Task 1 Step 5). Task 2 must not start until the
FLAG section below is answered.

## Purpose

A complete, read-only inventory of every acronym occurrence in the thesis's own English prose,
so that Task 2 can extend `acronyms.tex` once and Tasks 3–10 can convert each chapter
mechanically without re-deciding anything.

## What was scanned

39 files, read in full by nine parallel read-only scan agents (one per chapter plus end matter).
None was unreadable.

- **Ch1 (6):** `chapter_01/sections/` `1.0_introduction.tex`, `1.1_evidence_for_dark_matter.tex`,
  `1.2_wimp_paradigm.tex`, `freezout.tex`, `1.3_searching_for_dark_matter.tex`,
  `1.4_indirect_detection.tex`
- **Ch2 (4):** `chapter_02/sections/` `2.0_introduction.tex`, `2.1_production_mechanisms.tex`,
  `2.2_astrophysical_sky.tex`, `2.3_fermi_lat.tex`
- **Ch3 (6):** `chapter_03/sections/` `3.0_introduction.tex`, `3.1_inference.tex`, `3.2_sbi.tex`,
  `3.3_ml_astrophysics.tex`, `3.4_domain_shift.tex`, `3.5_cross_correlations.tex`
- **Ch4 (5):** `chapter_04/sections/` `4.0_introduction.tex`,
  `4.1_discovery_and_characterization.tex`, `4.2_msp_hypothesis.tex`,
  `4.3_systematics_stalemate.tex`, `4.4_breaking_the_stalemate.tex`
- **Ch5 (4):** `chapter_05/sections/` `5.1_introduction.tex`,
  `5.2_dark_matter_substructure.tex`, `5.3_dm_subhalos_gamma_ray_targets.tex`,
  `5.4_unassociated_sources.tex`
- **Ch6 (5):** `chapter_06/sections/` `6.0_introduction.tex`, `6.1_limits_individual.tex`,
  `6.2_source_count.tex`, `6.3_sbi_cnn.tex`, `6.4_transition.tex`
- **Ch7 (3):** `chapter_07/sections/` `7.0_introduction.tex`, `7.1_limits_of_threshold.tex`,
  `7.2_population_to_spatial.tex`
- **Ch8 (4):** `chapter_08/sections/` `8.0_introduction.tex`,
  `8.1_from_resolved_to_cosmic_web.tex`, `8.2_cross_correlation_technique.tex`, `8.3_ctao.tex`
- **End matter (2):** `conclusion/conclusion.tex`, `introduction/introduction.tex`

## What was excluded, and why

- **Integrated paper text** — every `paper_*/` directory and the five paper wrapper files
  (`4.5_paper.tex`, `5.6_paper_dmhalos.tex`, `6.5_paper_dnds.tex`, `7.4_paper_dnds_catalog.tex`,
  `8.4_paper_xcorr.tex`). These carry each paper's own conventions and are compiled verbatim
  (`main.tex:33` sets `\renderpapers` true), so their acronyms stay literal by design.
- **Non-English front/back matter** — `frontmatter/abstract_*.tex`, `resumen/`, and the
  standalone `papers/` tree.
- **Backups** — any `*.bak*`, `*.bk`, `*.old`, `* copy*` file.
- **Skip zones inside scanned files** — math, `%` comments, `\aure{}` annotations, the arguments
  of `\cite`/`\ref`/`\cref`/`\eqref`/`\label`/`\input`/`\includegraphics`, verbatim, paths/URLs,
  units, `$\Lambda$CDM`, roman numerals, surnames used as person-names, and one-off
  survey/instrument/object proper names. `\blue{...}` is **not** a skip zone (it is a revision
  colour macro over ordinary prose) and was scanned normally. Section and subsection headings are
  counted as skip zones for conversion but their content is noted.

## First use is per chapter

Task 2 adds `\glsresetall` to every chapter wrapper and to `conclusion/conclusion.tex`. Expansion
is therefore **per chapter**, not document-wide: within each chapter, the earliest in-scope
running-prose occurrence of a key prints `long form (SHORT)` and every later occurrence prints
`SHORT`. An acronym recurring across chapters is not a duplicate-definition problem — it correctly
re-expands once per chapter. Consequently the "earn the abbreviation" ≥2-uses rule was applied
**per chapter** by the scanners, and the cross-chapter reconciliation below revisits the cases
where that per-chapter view produced inconsistent verdicts.

## Resolution context: `\Fermi`, `\fermi` and "Fermi-LAT"

Five scanners (Ch1, Ch2, Ch5, Ch7, Ch8) independently raised "Fermi-LAT vs LAT" as an open
question. **It is not open.** `macros.tex:11–12` already owns the compound:

```latex
\newcommand{\Fermi}{\textit{Fermi}}
\newcommand{\fermi}{\textsl{Fermi}-LAT\ }
```

The *Fermi*-LAT compound belongs to the `macros.tex` system, not to glossaries. No `LAT`-bearing
compound is ever to be duplicated into `acronyms.tex`, and no conversion task may split
"Fermi-LAT" into `\Fermi-\LAT` or `Fermi-\gls{LAT_}`. This closes every Fermi-LAT row in every
chapter table below to `leave`. The one question that survives is narrow and is raised as **F5**:
*does bare standalone "LAT" (not the Fermi-LAT compound) convert to the registered `LAT_` entry,
or stay literal?*

## How `\newacro` constrains a SHORT

```latex
\newcommand{\newacro}[4][]{%
  \newacronym[#1]{#2}{#3}{#4}%
  \expandafter\newcommand\csname #3\endcsname{\gls{#2}\xspace}%
}
```

The convenience command is built from the SHORT via `\csname`. A SHORT containing a digit,
hyphen, space or dot therefore yields a control sequence that **cannot be typed in the source**
(`\4FGL`, `\L-C2ST`, `\BL Lac` are not valid control words). This is not a compile error — the
command is simply created and unreachable. Such an acronym can still be **registered and used
exclusively as `\gls{KEY_}`**; that is a real option, not an impossibility, and it is presented as
such below. (Ch4's scan claimed `1pPDF` would "hard-error at compile time" — corrected here: it
does not error, it produces an untypeable command.)

## Baseline

The build is green at baseline: `latexmk -pdf -interaction=nonstopmode main.tex` exits 0 and
`grep -c "Undefined control sequence" main.log` returns 0.

---

# Per-chapter inventories

## Chapter 1 — The Dark Matter Problem

**Files scanned.** All six carry rows.
`1.0_introduction.tex` (macro-using: CMB, BBN, WIMP) ·
`1.1_evidence_for_dark_matter.tex` (macro-using: CMB, BBN, SZ, ICM, MOND, dSph, BAO, WIMP) ·
`1.2_wimp_paradigm.tex` (heavily macro-using, 3 literal WIMP leaks) ·
`freezout.tex` (input from `1.2` near line 104; essentially clean) ·
`1.3_searching_for_dark_matter.tex` (4 literal WIMP leaks; introduces LHC) ·
`1.4_indirect_detection.tex` (largest and messiest; many registered terms used only literally).

| Acronym | Long form | Occurrences (file: count) | Registry status | Action |
|---|---|---|---|---|
| WIMP | weakly interacting massive particle | 1.0: 6 (6 macro); 1.1: 1 (1 macro); 1.2: 25 (22 macro, 3 literal); freezout: 1 (1 macro); 1.3: 4 literal; 1.4: 9 literal | defined+macro-used | convert — literal leaks in 1.2/1.3/1.4 → `\WIMP`/`\glspl{WIMP_}`; strip the now-redundant manual re-expansion at 1.2:16 |
| CMB | cosmic microwave background | 1.0: 4 (macro); 1.1: 11 (macro); 1.2: 1 (macro); 1.3: 5 (4 macro, 1 heading); 1.4: 5 (1 macro, 3 literal, 1 bold lead-in) | defined+macro-used | convert — 1.4:128, 133, 398 → `\CMB`; 1.3:71 is a `\subsection` title, leave; 1.4:404 `\textbf{CMB}` lead-in label, leave |
| BBN | Big Bang nucleosynthesis | 1.0: 1 (macro); 1.2: 6 (macro) | defined+macro-used | leave — already fully clean |
| dSph | dwarf spheroidal galaxy | 1.1: 3 (macro); 1.2: 1 (macro); 1.4: 3 literal | defined+macro-used | convert — 1.4:296, 418, 419 "dSphs" → `\glspl{dSph_}` (flagship mixed-markup case) |
| SZ | Sunyaev-Zel'dovich | 1.1: 2 (macro) | defined+macro-used | leave — clean |
| ICM | intracluster medium | 1.1: 2 (macro) | defined+macro-used | leave — clean |
| MOND | modified Newtonian dynamics | 1.1: 1 (macro) | defined+macro-used | leave — clean |
| BAO | baryon acoustic oscillations | 1.0: 1 literal (**chapter-earliest**); 1.1: 2 (macro) | defined+macro-used | convert — move the expansion site to 1.0:6; 1.1:153/157 drop to `\BAO`/`\gls{BAO_}` |
| PBH | primordial black hole | 1.2: 4 (macro); 1.4: 1 literal | defined+macro-used | convert — 1.4:381 → `\glspl{PBH_}` |
| FIMP | feebly interacting massive particle | 1.2: 3 (macro) | defined+macro-used | leave — clean |
| WDM | warm dark matter | 1.2: 2 (macro) | defined+macro-used | leave — clean |
| CTAO | Cherenkov Telescope Array Observatory | 1.2: 1 literal (spelled, **earliest**); 1.4: 1 literal w/ redundant "(CTAO)" | defined-but-literal | convert — expand at 1.2:155; strip the parenthetical at 1.4:464 |
| ML | machine learning | 1.0: 1 literal (spelled, **earliest**); 1.4: 1 literal | defined-but-literal | **FLAG (F1)** — reconciled: scanner said `convert`; ML is never written as "ML" anywhere in the thesis |
| PSF | point spread function | 1.4: 1 literal ("point-spread function") | defined-but-literal | convert — after the F15 hyphenation decision |
| DGRB | diffuse gamma-ray background | 1.4: 1 literal | defined-but-literal | convert — `\gls{DGRB_}` at 1.4:138 |
| UGRB | unresolved gamma-ray background | 1.4: 3 literal (intro 363, bare 364, 370) | defined-but-literal | convert — expand at 1.4:363, then `\UGRB` |
| AGN | active galactic nucleus | 1.4: 1 literal ("active galactic nuclei") | defined-but-literal | **FLAG (F2)** — reconciled: single use in chapter |
| mAGN | misaligned active galactic nucleus | 1.4: 1 literal ("misaligned active galactic nuclei") | defined-but-literal | **FLAG (F2/F8)** — reconciled: single use in chapter; key is `mAGN_` per F8 |
| SFG | star forming galaxy | 1.4: 1 literal ("star-forming galaxies") | defined-but-literal | **FLAG (F2/F15)** — reconciled: single use; hyphenation mismatch |
| FSRQ | flat spectrum radio quasar | 1.4: 1 literal ("flat-spectrum radio quasars") | defined-but-literal | **FLAG (F2/F15)** — reconciled: single use; hyphenation mismatch |
| SNR | supernova remnant | 1.4: 1 literal ("supernova remnants") | defined-but-literal | **FLAG (F2/F6)** — reconciled: single use; dual-meaning key |
| ICS | inverse Compton scattering | 1.1: 1 literal ("inverse-Compton scattering", **earliest**); 1.4: 3 (redundant "(ICS)" at 131, bare at 138, spelled at 323) | defined-but-literal | convert — expand at 1.1:71, strip "(ICS)" at 131, `\ICS` at 138/323. **Registry-status correction:** the Ch1 scan first classified ICS as `undefined`; `acronyms.tex:53` already defines `ICS_` |
| LAT | Large Area Telescope | 1.2: 1 literal ("Fermi Large Area Telescope", **earliest**); 1.4: 16 literal, all in the "Fermi-LAT" compound | defined-but-literal | leave — compound owned by `\Fermi`/`\fermi`; no bare standalone "LAT" in this chapter (see F5) |
| CR | cosmic ray | 1.4: 7 literal ("cosmic rays" ×3; "cosmic-ray X" compounds ×4) | defined-but-literal | **FLAG (F18)** — mid-compound substitution ("cosmic-ray protons" → "cosmic ray (CR) protons") changes hyphenation |
| LHC | Large Hadron Collider | 1.3: 4 (spelled at 53 **earliest**, bare at 61/65); 1.4: 1 bare | undefined | add-entry+convert — expand at 1.3:53 |
| ALP | axion-like particle | 1.4: 3 (spelled at 281 **earliest**, redundant "(ALPs)" at 379, bare "photon--ALP" at 379) | undefined | add-entry+convert — expand at 1.4:281 |
| VIB | virtual internal bremsstrahlung | 1.4: 3 (bold lead-in intro at 100, caption at 110, bare reuse at 127) | undefined | add-entry+convert — the only spelled-out occurrence is a `\textbf{}` lead-in; expansion must site there |
| GCE | Galactic Center excess | 1.4: 1 literal w/ "(GCE)" at 327 | undefined → registered via Ch4 | **FLAG (F2)** — reconciled: entry now exists (owned by Ch4); single use in Ch1 |
| SIDM | self-interacting dark matter | 1.2: 1 w/ "(SIDM)" at 92; 1.4: 1 spelled at 211 | undefined | leave — abbreviation never reused; fails ≥2-uses |
| ISRF | interstellar radiation field | 1.4: 2 (footnote 128 **earliest**, "(ISRF)" at 132) | undefined | leave — abbreviation never reused |
| gNFW | generalized Navarro-Frenk-White | 1.4: 1 w/ "(gNFW)" at 160 | undefined | leave — single use; also a digit/lowercase-prefix SHORT (F16) |
| NFW | Navarro-Frenk-White | 1.4: 12 literal (bold lead-in intro at 152, 11 reuses) | undefined | **FLAG (F9)** — reconciled: Ch1 recommended leave, Ch4 recommended add; see F9 |
| Einasto | Einasto profile | 1.4: 7 | excluded | leave — surname, skip zone |
| Burkert | Burkert profile | 1.4: 5 | excluded | leave — surname, skip zone |
| BL Lac | BL Lacertae object | 1.4: 2 (365, 366) | excluded | leave — proper name from a variable-star designation (F16) |
| SDSS | Sloan Digital Sky Survey | 1.1: 3; 1.4: 1 | excluded | leave — survey proper name, skip zone |
| DES, Gaia | Dark Energy Survey; Gaia | 1.4: 1 each (343) | excluded | leave — one-off survey/mission proper names |
| Standard Model | Standard Model | 1.0: 2; freezout: 2; 1.2: 10; 1.3: 7; 1.4: 6 (all spelled; "SM" only in math) | undefined (deliberate) | leave — spelled out everywhere by design, parallel to "dark matter" |
| DM | dark matter | pervasive in all six files; literal "DM" only in math plus one caption ("DM mass", freezout:118) | defined (`DM_`) | **FLAG (F4)** — house style: never convert |

**Notes.**
- **BAO expansion-site bug.** The chapter's true first mention is the spelled-out literal at
  `1.0_introduction.tex:6`, earlier in source order than the current `\Gls{BAO_}` at `1.1:153`.
  The expansion must move to 1.0:6.
- **1.2:16 redundant WIMP re-expansion.** `\WIMP` already fires the chapter's first use at
  `1.0:12`, so the hand-written `\emph{weakly interacting massive particles} (WIMPs)` at 1.2:16 is
  a second manual expansion; replace with plain `\glspl{WIMP_}`.
- **Excluded as proper names, not tabulated:** LZ, XENONnT, PandaX-4T, IceCube, ANTARES,
  Super-Kamiokande, PAMELA, AMS-02, GAPS, ATLAS, ADMX, DAMA/LIBRA, SENSEI, DAMIC, Rubin
  Observatory, PPPC 4 DM ID, CosmiXs, ETHOS, and the Bullet Cluster designation `1E 0657-558`.
- **"millisecond pulsar(s)"** is used 4× in Ch1 running prose (1.4:329, 332, 365, 470) but never
  abbreviated here. `MSP_` will exist registry-wide (owned by Ch2), so Ch1's uses fall under F2.

## Chapter 2 — The Gamma-Ray Sky and Fermi-LAT

**Files scanned.**
`2.0_introduction.tex` — **no acronyms found** (one spelled-out "Fermi Large Area Telescope", which
becomes the chapter-earliest LAT occurrence; "dark matter" spelled) ·
`2.1_production_mechanisms.tex` — acronym-bearing, entirely literal ·
`2.2_astrophysical_sky.tex` — acronym-bearing, entirely literal ·
`2.3_fermi_lat.tex` — acronym-bearing, entirely literal; heaviest instrument/catalog density.

No file in this chapter currently uses any glossaries macro.

| Acronym | Long form | Occurrences (file: count) | Registry status | Action |
|---|---|---|---|---|
| CMB | cosmic microwave background | 2.1: 4 | defined-but-literal | convert — expand at 2.1:16; strip the redundant "Cosmic Microwave Background (CMB)" at 2.1:60 |
| ICS | inverse Compton scattering | 2.1: 9 (2 long-form incl. a bold lead-in at :59; 7 bare) | defined-but-literal | convert — expand at 2.1:16; the "ICS" inside `\be...\ee` at 2.1:67 is skip-zone |
| IC | inverse Compton | 2.1: 1 (:115); 2.2: 1 (:61, hyphenated) | defined-but-literal | **FLAG (F7)** — reconciled: recommend leaving both adjectival phrases literal and not using `IC_` |
| ISM | interstellar medium | 2.1: 6 (intro w/ parens at :13; bare at :14, :92; spelled at :21, :90, :114) | undefined | add-entry+convert — expand at 2.1:13 |
| GDE | Galactic diffuse emission | 2.1: 3 (:49 spelled, :110 spelled+parens, :139 bare); 2.2: 2 (:17, :57 spelled) | undefined | add-entry+convert — expand at 2.1:49; strip the later parenthetical. Casing reconciled to lowercase "diffuse emission" (F15) |
| MSP | millisecond pulsar | 2.2: 5 (:23 intro+parens; :24, :25, :27 bare; :94 caption) | undefined | add-entry+convert — **Ch2 owns this entry** (earliest chapter earning it); expand at 2.2:23 |
| AGN | active galactic nucleus | 2.2: 2 (:10 spelled plural **earliest**; :60 spelled + redundant "(AGNs)") | defined-but-literal | convert — expand at 2.2:10; strip the parenthetical at :60 |
| mAGN | misaligned active galactic nucleus | 2.2: 4 (:70, :71, :82 prose; :94 caption) — prose always writes the hybrid "misaligned AGN(s)" | defined-but-literal | convert to `mAGN_` per **F8** |
| FSRQ | flat spectrum radio quasar | 2.2: 2 (:62 intro+parens "Flat-Spectrum Radio Quasars (FSRQs)"; :63 bare) | defined-but-literal | convert — expand at 2.2:62; hyphenation/casing per F15 |
| SFG | star forming galaxy | 2.2: 4 (:70 intro+parens; :74, :82 bare; :94 caption) | defined-but-literal | convert — expand at 2.2:70; hyphenation per F15 |
| EGB | extragalactic gamma-ray background | 2.2: 7 (:55 intro+parens; :56, 65, 66, 67, 75, 82 bare) | defined-but-literal | convert — expand at 2.2:55; casing per F15 |
| UGRB | unresolved gamma-ray background | 2.2: 4 (:57 intro+parens; :58, 72, 85 bare) | defined-but-literal | convert — expand at 2.2:57; casing per F15 |
| DGRB | diffuse gamma-ray background | 2.2: 1 (:92 caption, "Diffuse Gamma-Ray Background") | defined-but-literal | convert — only in-scope occurrence is a caption; casing per F15 |
| SED | spectral energy distribution | 2.2: 1 (:61) | undefined | leave — single use, fails ≥2-uses |
| EBL | extragalactic background light | 2.2: 1 (:66) | undefined → registered via Ch8 | **FLAG (F2)** — reconciled: entry now exists (owned by Ch8); single use in Ch2 |
| BL Lac | BL Lacertae object | 2.2: 3 (:62 intro+parens; :64, :65 bare) | undefined | **FLAG (F16)** — passes ≥2-uses but the SHORT contains a space; `\gls{KEY_}`-only or literal |
| GCE | Galactic Center excess | 2.2: 0 in-scope (1 inside the commented block at :35) | undefined → registered via Ch4 | leave — skip-zone only |
| CTAO | Cherenkov Telescope Array Observatory | 2.2: 1 (:38, inside `\blue{}`) | defined-but-literal | **FLAG (F2)** — reconciled: single use in chapter |
| WIMP | weakly interacting massive particle | 2.2: 1 (:28 bare); 2.3: 1 (:147 bare) | defined-but-literal | convert — expand at 2.2:28 |
| SNR | supernova remnant | 2.1: 2 (:46, :114 spelled); 2.2: 2 (:37, :38 spelled) | defined-but-literal | convert — expand at 2.1:46. No signal-to-noise usage in this chapter (F6 clean here) |
| IRF | instrument response function | 2.3: 5 (:56 intro+parens; :57, 58, 107, 119 bare) | defined-but-literal | convert — expand at 2.3:56 |
| PSF | point spread function | 2.3: 9 (:58 spelled **earliest**; :60 spelled+parens redundant; :62, 64 bare; :71–73 caption; :112) | defined-but-literal | convert — expand at 2.3:58; strip "(PSF)" at :60; hyphenation per F15 |
| PSF0–PSF3 | event-type labels | 2.3: 2 (:73 caption, :112) | undefined | **FLAG (F16)** — digit-suffixed; recommend literal |
| EDISP | energy dispersion (event types) | 2.3: 1 (:112) | undefined | leave — single use; Fermi-specific jargon with no spelled-out form |
| ACD | anticoincidence detector | 2.3: 4 (:42 intro+parens; :43, 44, 45 bare) | undefined | add-entry+convert — expand at 2.3:42; casing lowercased per F15 |
| TS | test statistic | 2.3: 1 running-prose intro (:125); later "TS" at :126–128, :134 all inside math | undefined → registered via Ch3 | **FLAG (F2)** — reconciled: entry now exists (owned by Ch3); only one running-prose use here |
| LAT (standalone) | Large Area Telescope | 2.0: 1 (:15 spelled, **chapter-earliest**); 2.3: 13 (:8 spelled+parens, :16 spelled+parens redundant, :24 caption, and 10 bare) | defined-but-literal | **FLAG (F5)** — the only chapter where bare standalone "LAT" genuinely earns the abbreviation (14 occurrences) |
| Fermi-LAT (compound) | — | 2.1: 3; 2.2: 5; 2.3: 6 (14 total) | defined-but-literal | leave — owned by `\Fermi`/`\fermi`; **resolved**, no longer an open question. Italicisation of "Fermi" is inconsistent across these 14 sites and is worth normalising separately |
| DM | dark matter | 2.0: 4; 2.1: 2; 2.2: 6; 2.3: 1 (always spelled out) | excluded (house style) | **FLAG (F4)** — never convert |
| GALPROP | — | 2.1: 5 | excluded | leave — software proper noun |
| DRAGON | — | 2.1: 1 | excluded | leave — software proper noun |
| CO | carbon monoxide | 2.1: 2 (:141, :142) | excluded | leave — chemical formula |
| EGRET | — | 2.3: 1 (:51) | excluded | leave — one-off instrument proper name |
| P8R3 | Pass 8 Release 3 | 2.3: 1 (:115) | excluded | leave — one-off proper name with digit |
| 1FGL / 3FGL / 4FGL / 4FGL-DR4 | Fermi-LAT catalog releases | 2.3: 1FGL ×1, 3FGL ×1, 4FGL ×2, 4FGL-DR4 ×2 | undefined | **FLAG (F16)** — digit-bearing; recommend literal |

**Notes.**
- Every `convert` row in Ch2 is a first-time conversion — the chapter uses no glossaries macro today.
- `\cite` keys containing acronym-like substrings (`Fermi-LAT:2014ryh`, `DGRB-review`) were excluded
  as `\cite`-argument skip zones.
- "ISRF"/"interstellar radiation field" appears at 2.1:13, 16, 115, 120 but is never abbreviated or
  parenthesised in this chapter, so it is not a conversion candidate here.

## Chapter 3 — Statistical Methods for Noise-Dominated Regimes

**Files scanned.** All six carry rows; none uses a glossaries macro yet.
`3.0_introduction.tex` · `3.1_inference.tex` · `3.2_sbi.tex` · `3.3_ml_astrophysics.tex` ·
`3.4_domain_shift.tex` (light load) · `3.5_cross_correlations.tex`.

| Acronym | Long form | Occurrences (file: count) | Registry status | Action |
|---|---|---|---|---|
| SBI | simulation-based inference | 3.0: 2; 3.1: 2; 3.2: 16; 3.3: 1 (21) | defined-but-literal | convert — expand at 3.0:15 (`\Gls{SBI_}`, sentence-initial); strip redundant "(SBI)" at 3.2:7 and :19 |
| NPE | neural posterior estimation | 3.2: 7; 3.3: 2 (9) | undefined | add-entry+convert — expand at 3.2:54 |
| NLE | neural likelihood estimation | 3.2: 1 | undefined | leave — single use, fails ≥2-uses |
| NRE | neural ratio estimation | 3.2: 3 | undefined | add-entry+convert — expand at 3.2:63 |
| ABC | approximate Bayesian computation | 3.2: 1 (:49) | undefined | leave — single use |
| TS | test statistic | 3.1: 10 | undefined | add-entry+convert — **Ch3 owns this entry**; expand at 3.1:71 |
| MLE | maximum likelihood estimator | 3.1: 4 | undefined | add-entry+convert — expand at 3.1:37 |
| AIC | Akaike information criterion | 3.1: 5 (1 spelled title-case + 4 literal) | undefined | add-entry+convert — expand at 3.1:105, letting `\Gls{AIC_}` synthesise the missing "(AIC)"; casing per F15 |
| KS | Kolmogorov--Smirnov | 3.1: 7 | undefined | add-entry+convert — **Ch3 owns this entry**; expand at 3.1:92. Long form excludes "test" (F15) |
| KL | Kullback--Leibler | 3.1: 2; 3.3: 4 (6) | undefined | add-entry+convert — expand at 3.1:111 (inside `\blue{}` and `\emph{}`); strip the "(KL)" parenthetical at 3.3:58 |
| MCMC | Markov chain Monte Carlo | 3.1: 2; 3.2: 4 (6) | undefined | add-entry+convert — **Ch3 owns this entry**; expand at 3.1:187; casing per F15 |
| CNN | convolutional neural network | 3.0: 1; 3.2: 1; 3.3: 8 (10) | defined-but-literal | convert — expand at 3.0:24 (`\glspl{CNN_}`); strip "(CNNs)" at 3.3:80 |
| AGN | active galactic nucleus | 3.3: 1; 3.4: 1 (2) | defined-but-literal | convert — expand at 3.3:29 (`\glspl{AGN_}`); 3.4:23 → `\gls{AGN_}` |
| ResNet | residual neural network | 3.3: 1 | defined-but-literal | leave — single use, and the occurrence names the architecture/paper, not the generic concept |
| SGD | stochastic gradient descent | 3.3: 1 (:51) | undefined | leave — single use |
| SBC | simulation-based calibration | 3.2: 1 (:105) | undefined | leave — single use |
| TARP | tests of accuracy with random points | 3.2: 1 (:106) | undefined | leave — single use |
| L-C2ST | local classifier two-sample test | 3.2: 1 (:107) | undefined | **FLAG (F16)** — hyphen + digit SHORT; also single use, so leave either way |
| KDE | kernel density estimation | 3.3: 1 spelled (all abbreviated uses are inside the commented §3.3.4 block) | undefined | leave — single in-scope use |
| GPU | graphics processing unit | 3.3: 1 (:52) | undefined | leave — single use, never spelled out |
| MSP | millisecond pulsar | 3.1: 1 (:119) | undefined → registered via Ch2 | **FLAG (F2)** — reconciled: entry now exists; single use in Ch3 |
| CL | confidence level | 3.1: 1 (:120, "95\% CL") | undefined | **FLAG (F19)** — single use, never spelled out anywhere; recommend spelling it out |
| MC (dropout) | Monte Carlo (dropout) | 3.3: 1 (:69) | undefined | leave — fixed technique name |
| APS | angular power spectrum | 3.5: 5 | undefined | add-entry+convert — expand at 3.5:25 |
| SNR | signal-to-noise ratio | 3.5: 5 (:17, 109, 111, 136) | **collision** — `SNR_` is registered as "supernova remnant" | **FLAG (F6)** — do not add a conflicting `SNR_` |
| CTAO | Cherenkov Telescope Array Observatory | 3.5: 4 | defined-but-literal | convert — expand at 3.5:18; strip the redundant "(CTAO)" at 3.5:147 |
| LAT | Large Area Telescope | 0 standalone (always in the "Fermi-LAT"/"Fermi LAT" compound) | defined-but-literal | leave — compound owned by `\Fermi`/`\fermi` |
| PSF | point spread function | 3.5: 1 (spelled "point-spread function", no letters used) | defined-but-literal | leave — single use; hyphenation noted under F15 |
| ML | machine learning | 3.0: 2; 3.2: 2; 3.3: 5; 3.4: 2; 3.5: 1 (12) — never once written "ML" | defined-but-literal | **FLAG (F1)** |
| NN | neural network | 3.0: 1; 3.1: 1; 3.2: 3; 3.3: 3 (8) — never once written "NN" | defined-but-literal | **FLAG (F1)** |
| DM | dark matter | bare "DM": 3.1: 1; 3.5: 1. Phrase "dark matter": 3.0: 3; 3.1: 3; 3.3: 5; 3.4: 4; 3.5: 28 | defined-but-literal | **FLAG (F4)** — never convert |

**Notes.**
- The commented-out §3.3.4 "Density Estimation" block (3.3, lines ~149–184) was excluded wholesale;
  it contains further KDE/EM/ELBO/PDF text that is not compiled.
- HEALPix, DeepSphere, NNHealpix, map2patch, HEAL-SWIN, VGG, 4FGL-DR4 and 2MASS were treated as
  one-off proper nouns.
- Converting KL at 3.1:111 wraps the full expansion inside the existing `\emph{}` — expected, but
  worth a compile sanity-check.
- "i.i.d.", "p-value", TPU, VAE, GAN, MLP, GP, HPD were searched for and do not occur in scope.

## Chapter 4 — The Galactic Center Excess

**Files scanned.** All five carry rows; none is acronym-free.
`4.0_introduction.tex` · `4.1_discovery_and_characterization.tex` · `4.2_msp_hypothesis.tex`
(heaviest MSP/GCE/NPTF/LMXB density) · `4.3_systematics_stalemate.tex` (heaviest NPTF/1pPDF/SCD/CNN
density) · `4.4_breaking_the_stalemate.tex` (lines 51–73 are a commented-out email draft, excluded
wholesale).

| Acronym | Long form | Occurrences (file: count) | Registry status | Action |
|---|---|---|---|---|
| GCE | Galactic Center excess | 4.0: 4; 4.1: 12; 4.2: 21; 4.3: 27; 4.4: 10 (all literal) | undefined | add-entry+convert — **Ch4 owns this entry**; expand at 4.0:13. Long form lowercased per F11 |
| MSP | millisecond pulsar | 4.0: 6; 4.1: 2; 4.2: ~35; 4.3: 8; 4.4: 9 | undefined → owned by Ch2 | convert — the entry is Ch2's; expand in this chapter at 4.0:10 (`\glspl{MSP_}`) |
| NPTF | non-Poissonian template fitting | 4.2: 3 (:34 intro, 54, 60); 4.3: 12 (+1 in a heading, not counted) | undefined | add-entry+convert — expand at 4.2:34; strip the redundant re-intro at 4.3:21 |
| 1pPDF | 1-point probability distribution function | 4.3: 8 (:47 intro "1-point Probability Density Function", 54, 83, 85, 97, 99, 104) | undefined | **FLAG (F10)** — digit-leading SHORT and a wording clash with Ch6 ("density" vs "distribution") |
| SCD | source-count distribution | 4.3: 8 (:101 intro, 104, 105, 111 caption re-intro, 113, 124, 125, 141); 4.4: 2 (:46, :47) | undefined, but collides with the registered `SCDF_` | **FLAG (F3)** — one key, not two |
| LMXB | low-mass X-ray binary | 4.2: 6 (:64 intro, 65, 66, 67, 82 ×2) | undefined | add-entry+convert — expand at 4.2:64 |
| NFW | Navarro-Frenk-White | 4.0: 1 spelled; 4.1: 6; 4.2: 3; 4.3: 6 (16) | undefined | **FLAG (F9)** — recommend registering on the `SZ_` precedent; expand at 4.0:7 if approved |
| WIMP | weakly interacting massive particle | 4.1: 8; 4.3: 1 | defined-but-literal | convert — expand at 4.1:113 |
| PSF | point spread function | 4.1: 2 (:37, spelled + literal in one sentence); 4.3: 1 (:99, "point-spread function") | defined-but-literal | convert — expand at 4.1:37; hyphenation per F15 |
| CNN | convolutional neural network | 4.3: 5; 4.4: 1 | defined-but-literal | convert — expand at 4.3:98 |
| DM | dark matter | dozens across all five files; the one bare "DM" is in a `%` comment (4.3:2) | defined+macro-used elsewhere; literal here by design | **FLAG (F4)** — never convert |
| GC | Galactic Center | 0 in-scope (5× inside the commented email draft) | undefined | leave — skip-zone only |
| IC | inverse Compton | 4.3: 1 (:78–79, spelled) | defined-but-literal | leave — single use (see also F7) |
| SBI | simulation-based inference | 4.3: 1 (:99, spelled) | defined-but-literal | **FLAG (F2)** — reconciled: single use in chapter |
| DES | Dark Energy Survey | 4.1: 1 (:149) | undefined | leave — one-off survey proper name |
| INTEGRAL | — | 4.2: 1 (:67) | undefined | leave — instrument proper name |
| GALPROP | — | 4.1: 1 (:72) | undefined | leave — software proper name |
| skyFACT | — | 4.2: 1; 4.3: 2 | undefined | leave — tool proper name, not an initialism |
| CTBCORE | — | 4.1: 1 (:36) | undefined | leave — one-off parameter proper name |
| 3FGL | Fermi third source catalog | 4.3: 1 (:112 caption) | undefined | **FLAG (F16)** — digit-bearing; recommend literal |
| p6v11 | Pass 6 v11 diffuse model | 4.3: 1 (:42, in `\texttt{}`) | undefined | **FLAG (F16)** — digit-bearing; recommend literal |
| Model O | — | 4.3: 1 (:45) | undefined | leave — proper-noun model label, not an acronym |

**Notes.**
- Additional expansion sites: WIMP → 4.1:113; PSF → 4.1:37; CNN → 4.3:98; NFW (if approved) →
  4.0:7; SCD (if approved) → the unabbreviated "source-count distribution" at 4.2:36, which
  predates the "(SCD)" intro at 4.3:101.
- Headings left literal and not counted: `\section{The Millisecond Pulsar Hypothesis}` (4.2:4),
  `\subsection{Challenges to NPTF}` (4.3:18), `\section{Discovery and Characterization of the GCE}`
  (4.1:4).
- "N-body" was considered and excluded — a compound physics term, not an initialism.

## Chapter 5 — Dark Matter Substructures

**Files scanned.** All four carry rows; none uses a glossaries macro.
`5.1_introduction.tex` · `5.2_dark_matter_substructure.tex` ·
`5.3_dm_subhalos_gamma_ray_targets.tex` · `5.4_unassociated_sources.tex`.

| Acronym | Long form | Occurrences (file: count) | Registry status | Action |
|---|---|---|---|---|
| LAT | Large Area Telescope | 5.1: 2 (both inside "Fermi-LAT"); 5.3: 6 (4 "Fermi-LAT", **2 standalone "the LAT"**); 5.4: 4 (all "Fermi-LAT") | defined-but-literal | leave — compound owned by `\Fermi`/`\fermi`; the 2 standalone uses fall under **F5** and fail ≥2-uses at chapter scope |
| — | "Fermi Large Area Telescope" (spelled, no parenthetical) | 5.1: 1 (:11) | defined-but-literal | leave — same resolution as above |
| WIMP | weakly interacting massive particle | 5.2: 2 (:28) | defined-but-literal | convert — expand at 5.2:28 |
| UV | ultraviolet | 5.2: 1 (:49, "UV feedback") | defined-but-literal | leave — single use |
| dSph | dwarf spheroidal galaxy | 5.2: 2 spelled (:36 "dwarf spheroidals", :37 exact match); 5.3: 8 (2 spelled, 6 literal) | defined-but-literal | convert — expand at 5.2:37; see the wording-variant note under F15 |
| ML | machine learning | 5.4: 3 spelled (:36, :47, :68); the literal "ML" at :39 is inside a `%` comment | defined-but-literal | **FLAG (F1)** — reconciled: scanner said `convert` |
| DM | dark matter | 5.4: 7 literal "DM" in running prose (:9, 29, 34, 47, 50, 68, 102); 5.1–5.3: 0 in-scope | defined-but-literal | **FLAG (F4)** — never convert. Note Ch5 is the one chapter that writes bare "DM" repeatedly in prose |
| $\Lambda$CDM | — | 5.1: 2; 5.2: 7; 5.3: 3 (all skip) | excluded | leave — explicit skip-zone term |
| 4FGL-DR4 | Fermi-LAT 4FGL Data Release 4 | 5.4: 1 (:14) | undefined | **FLAG (F16)** — digit + hyphen; recommend literal |
| SDSS | Sloan Digital Sky Survey | 5.2: 1 spelled; 5.3: 1 literal | excluded | leave — survey proper name |
| DES | Dark Energy Survey | 5.2: 1 spelled; 5.3: 1 literal | excluded | leave — survey proper name |
| VL-II | Via Lactea II | 5.2: 5 | excluded | leave — simulation proper name |
| Aquarius | — | 5.2: 1 | excluded | leave — simulation proper name |
| N-body | — | 5.2: 2 | excluded | leave — not an acronym |
| GD-1 | — | 5.4: 1 (:26) | excluded | leave — stellar-stream proper name |
| MW | Milky Way | 5.2: 1 (inside a `%` comment) | undefined | leave — skip-zone only |

**Notes.**
- **dSph wording variant.** 5.2:36 writes "the classical dwarf spheroidals" (omitting "galaxies"),
  one line before the exact match at 5.2:37. Default: leave 5.2:36 spelled out and fire the
  expansion at 5.2:37.
- The chapter never abbreviates "unassociated source"/"unidentified source" (no `unID`/`UNID`
  token), and no RF/BDT/SVM/NFW/gNFW token occurs in the four in-scope files.
- `\Fermi` is used once (5.3:37); every other "Fermi-LAT" is fully literal. Normalising that is a
  `macros.tex`-system question, outside this pass.

## Chapter 6 — From Individual Sources to Populations

**Files scanned.** All five carry rows.
`6.0_introduction.tex` · `6.1_limits_individual.tex` (heaviest concentration) ·
`6.2_source_count.tex` · `6.3_sbi_cnn.tex` (the one file in the chapter already using a macro,
`\SBI`) · `6.4_transition.tex`.

| Acronym | Long form | Occurrences (file: count) | Registry status | Action |
|---|---|---|---|---|
| SBI | simulation-based inference | 6.0: 1; 6.1: 1; 6.3: 3 (1 macro); 6.4: 1 | defined+macro-used | convert — unify to macro form; expand at 6.0:16. 6.3 currently mixes spelled/macro/literal in one file |
| CNN | convolutional neural network | 6.0: 1; 6.1: 1; 6.2: 1; 6.3: 2; 6.4: 1 | defined-but-literal | convert — expand at 6.0:16 (`\glspl{CNN_}`); strip the redundant "(CNN)" at 6.3:50 |
| UGRB | unresolved gamma-ray background | 6.1: 1; 6.2: 4; 6.4: 1 | defined-but-literal | convert — expand at 6.1:38 (casing already matches the registry) |
| PSF | point spread function | 6.3: 3 (1 spelled+parens "point-spread function", 2 literal) | defined-but-literal | convert after F15 — expand at 6.3:17 |
| GCE | Galactic Center excess | 6.0: 1; 6.1: 4; 6.2: 1 | undefined → owned by Ch4 | convert — the entry is Ch4's; expand in this chapter at 6.0:7 |
| MSP | millisecond pulsar | 6.1: 3; 6.2: 1; 6.4: 1 (all spelled out; "MSP" never written here) | undefined → owned by Ch2 | convert — the entry is Ch2's; expand at 6.1:11 (inside `\blue{}`, which is running prose) |
| MCMC | Markov chain Monte Carlo | 6.3: 2 (both literal) | undefined → owned by Ch3 | convert — the entry is Ch3's; expand at 6.3:28. Casing reconciled to lowercase "chain" (F15) |
| SFG | star forming galaxy | 6.1: 1; 6.2: 3; 6.4: 1 (all "star-forming galaxies") | defined-but-literal | convert after F15 — expand at 6.1:43 (`\glspl{SFG_}`) |
| AGN | active galactic nucleus | 6.2: 1 (:65, "AGN-like") | defined-but-literal | **FLAG (F2)** — reconciled: single use in chapter |
| mAGN | misaligned active galactic nucleus | 6.2: 2 (:71, :74, both "misaligned AGNs") | defined-but-literal (two candidate keys) | convert to `mAGN_` per **F8** |
| DM | dark matter | 6.0: 4; 6.1: 9; 6.2: 2; 6.4: 1; no literal "DM" token anywhere | excluded (house style) | **FLAG (F4)** — never convert |
| SCDF / "source-count distribution" | source-count distribution function | 6.0: 5; 6.1: 3; 6.2: 11; 6.3: 2; 6.4: 3 (24) — the acronym itself is never used | defined-but-literal | **FLAG (F3)** — the chapter's title-defining term; converting all 24 changes the chapter's voice |
| LAT | Large Area Telescope | 6.0: 1; 6.1: 6; 6.2: 12; 6.3: 3; 6.4: 2 — always the "Fermi-LAT" compound | defined-but-literal | leave — compound owned by `\Fermi`/`\fermi` |
| DGRB | diffuse gamma-ray background | 6.1: 1; 6.2: 4 — every token is inside `\cite{DGRB-review}` | excluded | leave — skip-zone only |
| — | "isotropic diffuse gamma-ray background" | 6.1: 1 (:27) | undefined | **FLAG (F20)** — matches no registry long form (not DGRB/UGRB/EGB); reads like the community term IGRB |
| TS | test statistic | 6.1: 1 (`$\mathrm{TS} > 25$`) | undefined → registered via Ch3 | leave — skip-zone only (math) |
| NFW | Navarro-Frenk-White | 6.1: 1 (:11, "NFW-squared") | undefined | **FLAG (F2/F9)** — single use here; entry decision is F9 |
| NPTF | non-Poissonian template fitting | 6.2: 1 (:68, "Non-Poissonian Template Fit (NPTF)", never reused) | undefined → owned by Ch4 | **FLAG (F2)** — reconciled: the entry now exists (Ch4); single definitional use here. Note the wording differs ("Fit" vs "fitting") |
| CPG | compound Poisson generator | 6.3: 1 (:35, intro never reused) | undefined | leave — single-use intro, fails ≥2-uses |
| 4FGL-DR4 | — | 6.1: 1 (:17) | undefined | **FLAG (F16)** — digit + hyphen; recommend literal |
| 4FGL-DR3 | — | 6.2: 1 (:16) | undefined | **FLAG (F16)** — digit + hyphen; recommend literal |
| 1pPDF | 1-point probability distribution function | 6.2: 3; 6.3: 8; 6.4: 1 (12) — intro+parens at 6.2:47 | undefined | **FLAG (F10)** — clearly earns an abbreviation but the SHORT is digit-leading |
| HEALPix | — | 6.3: 2 | undefined | leave — pixelisation-scheme proper name |
| NNHealpix | — | 6.3: 1 | undefined | leave — architecture proper name |

**Notes.**
- `dN/dS` notation was excluded throughout (math, not an acronym).
- Confirmed absent from Ch6: NPE, NLE, NRE, ML, NN, IRF, EGB, FSRQ, ISRF, gNFW, UV, TPU, MLNN, TF,
  ResNet, LSP, WIMP, CR, BBN, SZ, ICM, dSph, BAO, MOND, PBH, FIMP, WDM, CTAO, IC/ICS, SNR.
- Captions were treated as running prose; headings were not counted.

## Chapter 7 — Probabilistic Cataloging

**Files scanned.** All three carry rows; none uses a glossaries macro.
`7.0_introduction.tex` · `7.1_limits_of_threshold.tex` · `7.2_population_to_spatial.tex`.

| Acronym | Long form | Occurrences (file: count) | Registry status | Action |
|---|---|---|---|---|
| TS | test statistic | 7.1: 4; 7.2: 14 | undefined → owned by Ch3 | convert — the entry is Ch3's; expand in this chapter at 7.1:16 |
| KS | Kolmogorov--Smirnov | 7.2: 3 (:12 abbreviated, :61 long form, :66 abbreviated) | undefined → owned by Ch3 | convert — the entry is Ch3's; expand at 7.2:12. Long form excludes "test" (F15), so "a KS test" renders correctly |
| QF | quality factor | 7.2: 4 (:12, :66, :67 ×2) | undefined | add-entry+convert — expand at 7.2:12; casing lowercased per F15 |
| RoI | region of interest | 7.1: 4 (:16 intro, 17, 20 ×2); 7.2: 1 (:57 spelled again) | undefined | add-entry+convert — expand at 7.1:16 |
| mAGN | misaligned active galactic nucleus | 7.0: 1 (:6 plural); 7.1: 1 (:35 plural) | defined-but-literal | convert to `mAGN_` per **F8** — expand at 7.0:6 |
| SFG | star forming galaxy | 7.0: 1 (:6 plural); 7.1: 1 (:35 plural) | defined-but-literal | convert after F15 — expand at 7.0:6 |
| PSF | point spread function | 7.1: 1 (:20 long form); 7.2: 2 (:28, :75 literal) | defined-but-literal | convert after F15 — expand at 7.1:20 |
| 4FGL | Fermi-LAT fourth source catalog | 7.1: 3 (:14 "(4FGL)", :47 "4FGL-DR3", :51 "4FGL-DR4"); 7.2: 1 (:77 "4FGL-DR3") | undefined | **FLAG (F16)** — digit-leading; recommend literal |
| UGRB | unresolved gamma-ray background | 7.1: 1 (:35) | defined-but-literal | **FLAG (F2)** — reconciled: single use in chapter |
| FSRQ | flat spectrum radio quasar | 7.1: 1 (:49, "flat-spectrum radio quasars") | defined-but-literal | **FLAG (F2/F15)** — single use; hyphenation mismatch |
| MSP | millisecond pulsar | 7.1: 1 (:35, "millisecond pulsars") | undefined → owned by Ch2 | **FLAG (F2)** — reconciled: the entry now exists; single use here |
| SBI | simulation-based inference | 7.0: 1 (:4) | defined-but-literal | **FLAG (F2)** — reconciled: single use in chapter |
| SCDF / "source-count distribution" | source-count distribution function | 7.0: 2 (:4, :10); 7.1: 1 (:7) — every occurrence drops "function" | defined-but-literal | **FLAG (F3)** |
| DM | dark matter | 7.0: 1 (:17) | defined-but-literal | **FLAG (F4)** — never convert |
| LAT | Large Area Telescope | 7.0: 2; 7.1: 2; 7.2: 2 — all the "Fermi-LAT" compound (citation keys excluded) | excluded | leave — compound owned by `\Fermi`/`\fermi` |
| DGRB | diffuse gamma-ray background | 7.1: 1 (only as the `DGRB-review` citation key) | defined | leave — skip-zone only |
| PCAT | — | 7.2: 3 (all inside a commented block) | undefined | leave — skip-zone only |
| MCMC / RJMCMC | (trans-dimensional) Markov chain Monte Carlo | 7.2: 1 (inside the same commented block) | undefined → `MCMC_` owned by Ch3 | leave — skip-zone only |
| CPU | central processing unit | 7.2: 1 (inside the same commented block) | undefined | leave — skip-zone only |

**Notes.**
- "Gaussian-Process" appears at 7.2:28 but the token "GP" is never used, so there is nothing to
  abbreviate.
- 4FGL-DR3/4FGL-DR4 were folded into the 4FGL row: they are catalog-version labels, not independent
  acronyms, and stay literal regardless of how F16 is answered.

## Chapter 8 — Cross-Correlations and Future Prospects

**Files scanned.** All four carry rows.
`8.0_introduction.tex` (macro-using: `\UGRB` ×2) · `8.1_from_resolved_to_cosmic_web.tex` (mixed
macro/literal) · `8.2_cross_correlation_technique.tex` (entirely literal) · `8.3_ctao.tex`
(macro-using: `\CTAO` ×4, mixed with literal CTAO).

| Acronym | Long form | Occurrences (file: count) | Registry status | Action |
|---|---|---|---|---|
| UGRB | unresolved gamma-ray background | 8.0: 2 (macro); 8.1: 1 macro + 4 literal; 8.2: 5 literal | defined+macro-used | convert — unify the 9 literal occurrences to `\UGRB`; expansion already correctly sited at 8.0:11 |
| CTAO | Cherenkov Telescope Array Observatory | 8.0: 2 literal; 8.2: 2 literal; 8.3: 4 macro + 4 literal (+1 in a heading) | defined+macro-used | convert — move the expansion site to 8.0:22 and strip its manual "(CTAO)". Knock-on: 8.3:7 will then print the short form only |
| mAGN | misaligned active galactic nucleus | 8.0: 1; 8.1: 1; 8.2: 3; 8.3: 1 — five different phrasings, incl. an explicit "(mAGN)" intro at 8.2:91 and a bare "mAGN" at 8.2:94 | defined-but-literal | convert to `mAGN_` per **F8** — expand at 8.0:15 |
| AGN | active galactic nucleus | 0 standalone (only ever "misaligned AGN(s)") | defined | leave — nothing to convert under this key here |
| SFG | star forming galaxy | 8.0: 1; 8.1: 1; 8.2: 3; 8.3: 1 (all "star-forming") | defined-but-literal | convert after F15 — expand at 8.0:15 |
| WIMP | weakly interacting massive particle | 8.1: 2; 8.3: 3 | defined-but-literal | convert — expand at 8.1:47; 8.1:57 plural |
| LAT | Large Area Telescope | 8.0: 1 spelled; 8.3: 2 (1 inside the "Fermi Large Area Telescope (Fermi-LAT)" intro, **1 bare "the LAT detects"**) | defined-but-literal | leave — compound owned by `\Fermi`/`\fermi`; the single bare use falls under **F5** and fails ≥2-uses here. The double self-definition at 8.3:14 is a prose-editing issue, noted below |
| EBL | extragalactic background light | 8.2: 3 (:19, 27, 105); 8.3: 2 (:28, 33) | undefined | add-entry+convert — **Ch8 owns this entry**; expand at 8.2:19 (the explicit "(EBL)" intro at 8.1:82 is inside a `%` comment) |
| IACT | imaging atmospheric Cherenkov telescope | 8.3: 2 (:19 intro-plural, :23 reuse) | undefined | add-entry+convert — expand at 8.3:19 |
| LST | Large-Sized Telescope | 8.3: 2 (:22 intro-plural, :29 adjectival) | undefined | add-entry+convert — expand at 8.3:22 |
| MST | Medium-Sized Telescope | 8.3: 2 (:22 intro-plural, :29 adjectival) | undefined | add-entry+convert — expand at 8.3:22 |
| SST | Small-Sized Telescope | 8.3: 1 (:22 only) | undefined | leave — single use, fails ≥2-uses |
| EGAL | Extragalactic Survey | 8.3: 5 (:40 intro, 42, 56, 57, 61) | undefined | add-entry+convert — expand at 8.3:40; genuine proper noun, title case kept |
| HSP | high-synchrotron-peaked | 8.2: 1 (footnote :26 intro); 8.3: 1 (:30 second intro) | undefined | **FLAG (F12)** — both occurrences are definitional intros, never a plain reuse |
| LISP | low-to-intermediate-synchrotron-peaked | 8.2: 1 (footnote :26 intro); 8.3: 1 (:30 second intro) | undefined | **FLAG (F12)** — same pattern |
| SNR | signal-to-noise ratio (this chapter) | 8.2: 2 (:65, both meaning signal-to-noise ratio); 8.3: 1 spelled "supernova remnants" (:31) | registered as "supernova remnant" | **FLAG (F6)** — the 8.2:65 tokens must NOT become `\SNR` |
| 2MASS | Two Micron All-Sky Survey | 8.2: 5 (:36 intro, :82 second intro, 86, 89, 105) | undefined | **FLAG (F13/F16)** — digit-leading; earns an abbreviation but needs `\gls{KEY_}`-only registration |
| 2MRS | 2MASS Redshift Survey | 8.2: 4 (:82 intro, 86, 89, 105) | undefined | **FLAG (F13/F16)** — same |
| 4FGL | — | 8.1: 1 (inside a `%` comment) | undefined | leave — skip-zone only; also digit-leading |
| SBI | simulation-based inference | 8.1: 1 (inside the same `%` comment) | defined | leave — skip-zone only |
| CR | cosmic ray | 8.2: 2 (:53, adjectival "cosmic-ray background") | defined | leave — `\CR` would render "cosmic ray-ray background"-style breakage (F18) |
| DM | dark matter | spelled: 8.0:16, 8.1:42, 8.2:7, 8.3:3; bare "DM": 8.1:1, 8.2:28, 8.3:4 | excluded (house style) | **FLAG (F4)** — never convert |

**Notes.**
- Footnote text (8.2:26) was treated as running prose, not a skip zone.
- Bare "CTA" (no trailing O) appears six times in 8.3 but only inside `\ref{sec:CTA}` — no
  CTA/CTAO terminology conflict exists.
- **8.3:14 double self-definition.** The sentence re-spells "Fermi Large Area Telescope (Fermi-LAT)"
  and is immediately followed by a bare "the LAT detects…". Under the F5 recommendation this stays
  literal, but the paragraph is worth a prose edit regardless.
- "LSS" (8.0:17, 8.1:71) and "APS" (8.1:64, 8.3:59) are discussed but never abbreviated in Ch8 —
  no occurrence to convert.
- HESS, MAGIC, VERITAS each appear once, in one list — left literal. `gNFW` and `H.E.S.S.` do not
  occur.

## End matter

**Files scanned.**
`conclusion/conclusion.tex` — acronym-bearing; own `\glsresetall` scope; no glossaries macro in use
(it does use the separate `\Fermi` and `\dnds{}` macros) ·
`introduction/introduction.tex` — **no acronyms found** (three lines: a `\chapter{Introduction}`
heading and `\initial{T}he introduction`; also not imported by `main.tex`, so it receives no
`\glsresetall` in Task 2 — scanned anyway per plan).

| Acronym | Long form | Occurrences (file: count) | Registry status | Action |
|---|---|---|---|---|
| GCE | Galactic Center excess | conclusion: 3 (all spelled out: :17, :25, :53–54) | undefined → owned by Ch4 | convert — the entry is Ch4's; expand at conclusion:17. Long form lowercased per F11 |
| MSP | millisecond pulsar | conclusion: 3 (:23–24 plural, :53 bold lead-in, :100 adjectival) | undefined → owned by Ch2 | convert — the entry is Ch2's; expand at conclusion:23 (`\glspl{MSP_}`) |
| LSS | large-scale structure | conclusion: 3 (:129, :135 bold lead-in, :146 adjectival) — never abbreviated anywhere in the thesis | undefined | **FLAG (F1)** — reconciled: scanner said `add-entry+convert`; Ch8 confirms LSS is never written as a short form |
| CTAO | Cherenkov Telescope Array Observatory | conclusion: 4 literal (:41, 137, 142, 148) | defined-but-literal | convert — expand at conclusion:41 |
| SBI | simulation-based inference | conclusion: 1 (:20, spelled) | defined-but-literal | **FLAG (F2)** — reconciled: the end-matter scan converted single uses of registered keys; Ch7's scan left them. One policy, please |
| SCDF / "source-count distribution" | source-count distribution function | conclusion: 2 (:34, :103) — both drop "function", both immediately followed by `\dnds{}` | defined-but-literal | **FLAG (F3)** |
| CNN | convolutional neural network | conclusion: 1 (:33, written "a convolutional network" — missing "neural") | defined-but-literal | **FLAG (F2/F15)** — single use, and the prose wording is a paraphrase of the registry long form |
| DM | dark matter | conclusion: 10 spelled; literal "DM" never appears | excluded | **FLAG (F4)** — never convert |
| Fermi-LAT | Large Area Telescope | conclusion: 4 literal (:24, 29–30, 56, 144) + 1 `\Fermi-LAT` (:90) | excluded | leave — compound owned by `\Fermi`/`\fermi`; worth normalising the 4 literal sites to the macro |
| 4FGL-DR3 | — | conclusion: 1 (:39) | excluded | **FLAG (F16)** — digit + hyphen; recommend literal |
| 2MASS | Two Micron All-Sky Survey | conclusion: 1 (:137) | excluded | **FLAG (F13/F16)** — one use here, four more in Ch8 |
| gPCS | gamma-ray photon count statistics | conclusion: 2 (:37–38 with a hand-written parenthetical inside `\texttt{}`; :121 bare `\texttt{gPCS}`) | excluded | **FLAG (F14)** — formalise into the registry, or keep the hand-rolled `\texttt{}` pattern? |

**Notes.**
- Excluded as ordinary prose with no abbreviation: "deep learning", "generative modeling",
  "statistical inference", "quantification learning", "Milky Way", "Inner Galaxy", "Sommerfeld
  enhancement", "Euclid", "weak lensing".

---

# Cross-chapter reconciliation

This is the part the nine partial scans could not do. Each subsection states what the partials
disagreed about and what this document decided.

## R1 — The same new acronym proposed by more than one chapter

The nine scans proposed 36 unconditional `\newacro` lines between them plus 5 conditional ones;
after deduplication there are 26 unconditional entries and 8 conditional ones. One entry each, assigned to its **chapter of first appearance in source order**
(Ch1 → Ch8 → end matter):

| SHORT | Proposed independently by | Assigned to | Reason |
|---|---|---|---|
| MSP | Ch2, Ch4, Ch6, end matter | **Ch2** | `2.2_astrophysical_sky.tex` (5 uses) is the earliest chapter that earns it |
| GCE | Ch4, Ch6, end matter | **Ch4** | Ch1 has one use (fails ≥2), Ch2 has a comment-only use; Ch4 is the earliest earning chapter (74 uses) |
| MCMC | Ch3, Ch6 | **Ch3** | `3.1_inference.tex` precedes `6.3_sbi_cnn.tex` |
| TS | Ch3, Ch7 (Ch2 flagged it single-use) | **Ch3** | `3.1_inference.tex` (10 uses) precedes Ch7 |
| KS | Ch3, Ch7 | **Ch3** | `3.1_inference.tex` (7 uses) precedes Ch7 |
| 1pPDF | Ch4, Ch6 | **Ch4** (conditional) | `4.3` precedes `6.2`; see F10 |
| NFW | Ch1 (recommended leave), Ch4 (recommended add) | **Ch1** (conditional) | `1.4` precedes `4.0`; see F9 |
| EBL | Ch8 (Ch2 flagged it single-use) | **Ch8** | Ch2's lone use fails ≥2; Ch8 has 5 |
| NPTF | Ch4 (Ch6 flagged it single-use) | **Ch4** | Ch4 has 15 uses; Ch6's one definitional use falls under F2 |
| LSS | end matter (Ch8 notes it is never abbreviated) | **end matter** (conditional) | see F1 |

No other proposed SHORT was raised by more than one scan.

## R2 — Conflicting long forms and casing for the same SHORT

| SHORT | Disagreement | Decision | Why |
|---|---|---|---|
| GCE | Ch4 "Galactic Center excess" vs Ch6 and end matter "Galactic Center Excess" | **"Galactic Center excess"** | `acronyms.tex` header: "long forms are lowercase except genuine proper nouns". "Galactic Center" is the proper noun; "excess" is not |
| MCMC | Ch3 "Markov chain Monte Carlo" vs Ch6 "Markov Chain Monte Carlo" | **"Markov chain Monte Carlo"** | Standard usage; "chain" is a common noun |
| KS | Ch3 "Kolmogorov--Smirnov" vs Ch7 "Kolmogorov--Smirnov test" | **"Kolmogorov--Smirnov"** | The prose writes "a KS test"; including "test" in the long form would render "Kolmogorov--Smirnov test (KS) test" |
| 1pPDF | Ch4 "1-point probability **density** function" vs Ch6 "1-point probability **distribution** function" | **"1-point probability distribution function"** | The prose clash is real (Ch4:47 vs Ch6:47); "distribution" matches the standard 1pPDF literature. Ch4's manual parenthetical is stripped at conversion, so the divergence disappears |
| 1pPDF key | Ch4 `1pPDF_` vs Ch6 `onepPDF_` | **`1pPDF_`** | Key = SHORT + `_` per the plan's convention; a digit-leading glossary *key* is legal (only the auto-built `\SHORT` command is untypeable) |
| GDE | Ch2 "Galactic Diffuse Emission" (title case) | **"Galactic diffuse emission"** | Same lowercase rule as GCE. Author may override — see F15 |
| ACD | Ch2 "Anticoincidence Detector" (title case) | **"anticoincidence detector"** | Common noun |
| QF | Ch7 "Quality Factor" in prose | **"quality factor"** | Common noun; Ch7's own scan already recommended this |
| AIC | Ch3 prose "Akaike Information Criterion" | **"Akaike information criterion"** | "Akaike" is a surname, the rest is common |
| LST / MST / EGAL | Ch8 title case | **kept title case** | CTAO's own instrument and Key-Science-Project names — genuine proper nouns |
| NPTF | Ch4 "non-Poissonian template fitting" vs Ch6 prose "Non-Poissonian Template Fit" | **"non-Poissonian template fitting"** | Ch4 owns the entry and has 15 of the 16 uses |

`longplural` is carried only where the plural is irregular — `LMXB_` ("low-mass X-ray binaries",
y→ies) and `RoI_` ("regions of interest", internal pluralisation). Three scans proposed
`longplural={millisecond pulsars}` and `longplural={axion-like particles}`; both are regular
`+s` plurals that `glossaries` forms automatically, so they are dropped. This is stricter than the
existing file, which spells out several regular plurals; harmless either way.

## R3 — `SCD` (Ch4) vs the registered `SCDF_`

Four chapters plus the conclusion talk about this quantity, and **none of them ever writes "SCDF"**:
Ch4 writes "source-count distribution (SCD)" and then "SCD" (10 uses); Ch6 writes
"source-count distribution" in full 24 times and never abbreviates it; Ch7 (3 uses) and the
conclusion (2 uses) also write "source-count distribution", always dropping the word "function". A
repo-wide grep confirms **`SCDF`, `\SCDF` and `\gls{SCDF_}` appear nowhere outside `acronyms.tex`**,
so the registered entry is currently dead.

One key, not two. See **F3** for the decision the author must make; the recommendation there is to
*rename* the dead `SCDF_` entry to `SCD_`/"source-count distribution" rather than add a second key,
because that is the phrase the author actually writes in all four places.

## R4 — `IC_` vs `ICS_`

Both are registered (`acronyms.tex:36` and `:53`). Across the whole thesis, the bare two-letter
token "IC" never appears in prose. What appears is: "inverse Compton scattering" / "ICS" (Ch1: 4,
Ch2: 9), and two adjectival phrases without "scattering" — "an inverse Compton map" (2.1:115) and
"high-frequency inverse-Compton peak" (2.2:61) — plus one spelled "This inverse Compton component"
(4.3:78). See **F7**; the recommendation is to use `ICS_` only and leave the three adjectival
phrases literal, which leaves `IC_` registered but unused (an unused entry never prints in the List
of Acronyms, so nothing is lost).

Note Ch1's scan initially classified ICS as `undefined`. **Correction applied:** `acronyms.tex:53`
defines `ICS_`, so Ch1's ICS row is `defined-but-literal`, not a new entry.

## R5 — `AGN_` vs `mAGN_` for "misaligned AGN"

Five chapters refer to this population, in five different ways: fully spelled "misaligned active
galactic nuclei" (1.4:365, 8.0:15), the hybrid "misaligned AGN(s)" (2.2:70/71/82/94, 6.2:71/74,
7.0:6, 7.1:35, 8.1:53, 8.2:93, 8.3:30), an explicit "misaligned active galactic nuclei (mAGN)"
intro (8.2:91), and one bare "mAGN" (8.2:94). The registry already carries a dedicated `mAGN_`
whose `longplural` ("misaligned active galactic nuclei") matches the author's own spelled-out
phrasing exactly. See **F8**; recommendation: map every one of these to `mAGN_`, and reserve
`AGN_` for standalone "AGN" (2.2:10/60, 3.3:29, 3.4:23, 6.2:65).

## R6 — Scanner verdicts changed by this merge

| What changed | Chapters affected | Why |
|---|---|---|
| ML rows moved from `convert` to `FLAG (F1)` | Ch1, Ch5 (Ch3 already flagged it) | Three chapters cannot answer this differently; ML is never written as "ML" anywhere in the thesis |
| LSS moved from `add-entry+convert` to `FLAG (F1)` | end matter | Ch8 confirms LSS is never used as a short form either |
| ICS registry status corrected from `undefined` to `defined-but-literal` | Ch1 | `acronyms.tex` wins over the scanner |
| Single-use-of-a-registered-key rows harmonised to `FLAG (F2)` | Ch1, Ch2, Ch4, Ch6, Ch7, end matter | Ch7's scan left these literal; the end-matter scan converted them. One policy is needed |
| All Fermi-LAT rows closed to `leave` | Ch1, Ch2, Ch5, Ch6, Ch7, Ch8, end matter | `macros.tex:11–12` owns the compound |
| Duplicate `\newacro` proposals collapsed to one entry each | Ch2/4/6/end (MSP), Ch4/6/end (GCE), Ch3/6 (MCMC), Ch3/7 (TS, KS), Ch4/6 (1pPDF) | Per-chapter `\glsresetall` means one entry re-expands per chapter; duplicates would be a redefinition error |
| "1pPDF hard-errors at compile time" corrected | Ch4 | `\csname` builds the command silently; it is merely untypeable |

## R7 — Occurrence-count overlaps

The nine scans worked on disjoint file sets, so no two of them can report a count for the same
file. **No overlap was found** — every file name appears in exactly one partial. No scanner error
of this kind to report.

---

# Author decisions required (FLAG)

Ordered by how much downstream work each decision controls. Answer these and Tasks 2–10 become
mechanical.

## F1 — Terms registered (or proposed) whose SHORT the author never writes: ML, NN, LSS

**Question.** "machine learning", "neural network" and "large-scale structure" are spelled out at
every occurrence in the thesis and are *never* written as ML / NN / LSS. Do we start abbreviating
them, or keep them spelled out like "dark matter"?

**Affected.** ML — Ch1: 2, Ch3: 12, Ch5: 3 (17 total, 3 chapters). NN — Ch3: 8. LSS — conclusion: 3,
Ch8: 2 (never abbreviated in either). `ML_` and `NN_` are already in `acronyms.tex`; `LSS_` would be
a new entry.

**Options.** (a) Leave all three spelled out; do not register `LSS_`; leave `ML_`/`NN_` registered
but unused. (b) Convert, introducing "ML", "NN" and "LSS" as visible text in five chapters where
the author never wrote them.

**Recommendation: (a) leave spelled out.** These are framing terms, not shorthand the reader needs;
converting would put abbreviations in the reader's way that the author's own prose never asks for —
the same reasoning that keeps "dark matter" literal.

## F2 — A registered acronym used only ONCE in a chapter: convert or leave?

**Question.** Under per-chapter `\glsresetall`, a single occurrence expands to "long form (SHORT)"
and the SHORT is then never used again in that chapter. Is that acceptable, or does the ≥2-uses
rule apply per chapter to registered keys too?

**Affected.** ~20 rows: Ch1 (AGN, mAGN, SFG, FSRQ, SNR, GCE), Ch2 (CTAO, EBL, TS), Ch3 (MSP, PSF,
ResNet), Ch4 (SBI, IC), Ch5 (UV), Ch6 (AGN, NFW, NPTF), Ch7 (UGRB, FSRQ, MSP, SBI), conclusion (SBI,
CNN). The scanners split: Ch7 left them literal, the end-matter scan converted them.

**Options.** (a) Leave literal — apply the ≥2-uses rule per chapter to every key, registered or not.
(b) Convert — any registered key converts wherever it appears.

**Recommendation: (a) leave literal.** A lone expansion that is never reused is pure noise; and
(a) makes one rule cover both new and existing entries, which is much easier for eight conversion
tasks to apply consistently.

## F3 — `SCD` vs the registered `SCDF_`: one key, and which one?

**Question.** The registry defines `SCDF_` = "source-count distribution function", a string that
appears nowhere else in the repo. The prose says "source-count distribution" in Ch4 (abbreviated
"SCD", 10 uses), Ch6 (24 uses, never abbreviated), Ch7 (3) and the conclusion (2).

**Options.** (a) **Rename** the dead `SCDF_` to `\newacro{SCD_}{SCD}{source-count distribution}`;
Ch4's ten "SCD" tokens then convert cleanly and the long form matches the author's own wording
everywhere. (b) Keep `SCDF_` and fold Ch4 into it — every "SCD" in the prose becomes "SCDF" and the
word "function" is inserted into sentences that do not have it. (c) Leave the term literal
thesis-wide, like "dark matter", and drop `SCDF_`.

**Recommendation: (a) rename to `SCD_`.** Nothing in the thesis writes "SCDF", so nothing breaks;
Ch4 gets its abbreviation; and Ch6/Ch7/conclusion, where the abbreviation is never used, then fall
under F2 (leave literal, preserving Ch6's deliberate full-phrase voice for its title term).

## F4 — "dark matter" / DM (mandatory)

**Question.** Confirm that "dark matter" stays literal everywhere, and `DM_` stays registered but
unused.

**Affected.** Every chapter. Bare "DM" appears in running prose only in Ch5 (`5.4`, 7 times) and
Ch8 (3 times); everywhere else the phrase is spelled out.

**Recommendation: leave literal (house style).** Optional follow-up, not part of this pass: the
scattered bare "DM" tokens in 5.4 and Ch8 are inconsistent with the rest of the thesis and could be
spelled out. One narrower copy-edit worth noting: `freezout.tex:118`'s caption says "DM mass" while
the same caption spells out "dark matter" twice.

## F5 — Bare standalone "LAT" (not the Fermi-LAT compound)

**Question.** *Fermi*-LAT is settled — it belongs to `\Fermi`/`\fermi` in `macros.tex` and is never
touched. The remaining question: does bare standalone "LAT" convert to the registered `LAT_`, or
stay literal?

**Affected.** Ch2 only, in substance: `2.0:15` spells out "Fermi Large Area Telescope" and `2.3` uses
bare "LAT" 13 times (14 total — this is the one place where "LAT" is genuinely a reusable
abbreviation). Elsewhere there are just 3 isolated standalone uses: `5.3` ×2, `8.3` ×1.

**Options.** (a) Convert bare standalone "LAT" in Ch2 only (expand at 2.0:15); leave the 3 isolated
uses literal under F2. (b) Convert every standalone "LAT". (c) Leave all standalone "LAT" literal.

**Recommendation: (a).** Ch2 is the instrument chapter and earns the abbreviation 14 times; the
isolated singles elsewhere do not.

## F6 — SNR: supernova remnant vs signal-to-noise ratio

**Question.** `SNR_` is registered as "supernova remnant". Ch3 (`3.5`, 5 uses) and Ch8 (`8.2:65`,
2 uses) use "SNR" to mean signal-to-noise ratio.

**Options.** (a) Keep `SNR_` = supernova remnant; leave "signal-to-noise ratio" spelled out
everywhere, with no glossary entry. (b) Mint a second key (e.g. `SNRatio_`) for the ratio sense,
accepting that two entries print the identical visible string "SNR" in different chapters.

**Recommendation: (a).** Two entries rendering the same three letters with different meanings is
exactly the confusion the reader would suffer for; spelling out "signal-to-noise ratio" costs seven
occurrences of extra words.

## F7 — `IC_` vs `ICS_`

**Question.** Both are registered. Bare "IC" never appears in the thesis; "ICS" appears 13 times
(Ch1: 4, Ch2: 9), and three adjectival phrases use "inverse Compton"/"inverse-Compton" without
"scattering" (2.1:115, 2.2:61, 4.3:78).

**Options.** (a) Use `ICS_` only; leave the three adjectival phrases literal; `IC_` stays registered
but unused (it will not appear in the List of Acronyms). (b) Convert the adjectival phrases to
`\IC` as well, so both macros appear within three lines of each other in `2.1`. (c) Reword the
adjectival phrases to "inverse Compton scattering" and fold them into `ICS_`.

**Recommendation: (a).** No prose change, no visible pair of near-identical acronyms, and the
adjectival uses are single-use in their chapters anyway (F2).

## F8 — `AGN_` vs `mAGN_` for "misaligned AGN"

**Question.** Five chapters write "misaligned AGN(s)" or "misaligned active galactic nuclei". Map to
the dedicated `mAGN_`, or leave "misaligned" literal and convert only the "AGN" part?

**Affected.** Ch1: 1, Ch2: 4, Ch6: 2, Ch7: 2, Ch8: 5 (14 occurrences across 5 chapters).

**Options.** (a) `\glspl{mAGN_}` for the whole phrase — renders "misaligned active galactic nuclei
(mAGNs)" at first use, then "mAGNs". (b) Literal "misaligned" + `\glspl{AGN_}` — renders
"misaligned active galactic nuclei (AGN)s", which reads badly.

**Recommendation: (a) `mAGN_`.** That is exactly what the entry was created for, its registered
`longplural` already matches the author's own spelled-out phrasing, and `8.2:91/94` already writes
"(mAGN)" and bare "mAGN" by hand.

## F9 — NFW: register it, or leave the surname compound literal?

**Question.** "NFW" is used 12 times in Ch1 and 16 times in Ch4 (plus 1 in Ch6) as technical
shorthand — "NFW profile", "NFW template", "NFW halo" — never to refer to the three people. The
scan briefs list "Navarro" as a surname to skip. Ch1's scan recommended leave; Ch4's recommended add.

**Options.** (a) Register `\newacro{NFW_}{NFW}{Navarro-Frenk-White}` and convert (Ch1 expands at
1.4:152, Ch4 at 4.0:7). (b) Leave literal everywhere, as with Einasto and Burkert.

**Recommendation: (a) register.** The registry already carries the exact same shape of entry —
`\newacro{SZ_}{SZ}{Sunyaev-Zel'dovich}`, a two-surname compound — and 29 uses is well past earning
it. Note that `gNFW` (one use, Ch1) stays literal regardless.

## F10 — 1pPDF: register as `\gls{1pPDF_}`-only, or leave literal?

**Question.** "1pPDF" is used 8 times in Ch4 and 12 times in Ch6 — comfortably earning an
abbreviation — but the SHORT starts with a digit, so `\newacro`'s auto-built command cannot be typed
as `\1pPDF`. (It does not error; it is simply unreachable.)

**Options.** (a) Register it and use `\gls{1pPDF_}` / `\glspl{1pPDF_}` at every site — real, just
more verbose in the source. (b) Leave literal everywhere, as with 4FGL and friends.

**Recommendation: (a) register, `\gls{}`-only.** 20 uses across two chapters is the one digit-SHORT
in the thesis that genuinely earns a glossary entry, and it gets the term into the List of Acronyms
where a reader will look for it. Sub-question, already decided in R2 unless you disagree: the long
form is "1-point probability **distribution** function" (Ch4:47 currently writes "density"; that
manual parenthetical is stripped at conversion anyway).

## F11 — GCE long form casing

**Question.** "Galactic Center excess" (Ch4's proposal) or "Galactic Center Excess" (Ch6's and the
conclusion's)? This string is printed at the first use in each of five chapters.

**Recommendation: "Galactic Center excess".** `acronyms.tex`'s own header rule — lowercase except
genuine proper nouns — and "excess" is not a proper noun. Chapter 4's *title* keeps its title case
regardless; headings are untouched by this pass.

## F12 — HSP / LISP

**Question.** Both appear exactly twice in Ch8, and **both occurrences are definitional intros** —
a footnote at `8.2:26` and a second full "(HSP)"/"(LISP)" introduction at `8.3:30`. Neither is ever
used as a plain abbreviation afterwards.

**Options.** (a) Leave both spelled out; strip the duplicate definition at 8.3:30 as a prose edit.
(b) Register both; the footnote becomes the expansion site and 8.3:30's parenthetical is stripped.

**Recommendation: (a) leave spelled out.** Two definitions and zero reuses is a term the reader
never has to carry; the real defect here is the duplicated definition, not the missing entry.

## F13 — 2MASS / 2MRS

**Question.** Both are genuinely reused abbreviations with spelled-out long forms (2MASS: 5 uses in
Ch8 + 1 in the conclusion; 2MRS: 4 uses in Ch8) but both SHORTs are digit-leading, so they would be
`\gls{KEY_}`-only.

**Options.** (a) Leave literal, consistent with how SDSS, DES and Gaia are treated everywhere else
in the thesis. (b) Register both as `\gls{}`-only entries.

**Recommendation: (a) leave literal.** These are survey proper names, and the thesis already treats
every other survey name that way. Separately: "Two Micron All-Sky Survey (2MASS)" is spelled out
*twice* in the same subsection (8.2:36 and 8.2:82) — one should be stripped either way.

## F14 — gPCS

**Question.** `\texttt{gPCS}` is introduced with a hand-written "(gamma-ray Photon Count Statistics)"
at `conclusion:37–38` and reused bare at `:121`, mirroring the glossary pattern but entirely outside
it. The registry does hold comparable tool names (`TF_` = TensorFlow, `resnet_` = ResNet).

**Recommendation: leave the hand-rolled `\texttt{}` pattern.** It is the author's own software, it
appears twice in one file, and `\texttt{}` marks it as a tool rather than a concept.

## F15 — mechanical decisions (casing, hyphenation, wording)

None of these changes *whether* an entry exists — only the exact string `glossaries` prints at the
first use in each chapter. Grouped into one table so they can be answered in one pass. A tick on
"registry wins" means the prose quietly changes to the registry's form at every converted site; a
tick on "prose wins" means `acronyms.tex` is edited to match what the author wrote.

| # | Term | Registry has | Prose writes | Sites | Recommendation |
|---|---|---|---|---|---|
| a | PSF | "point spread function" | "point-spread function" (Ch1, Ch3, Ch4, Ch6, Ch7); "Point Spread Function" (Ch2:58/60) | 6 chapters | **Prose wins** — edit the registry to "point-spread function"; five of six chapters hyphenate |
| b | SFG | "star forming galaxy" | "star-forming galaxies" everywhere, without exception | Ch1, Ch2, Ch6, Ch7, Ch8 | **Prose wins** — edit the registry to "star-forming galaxy" / "star-forming galaxies" |
| c | FSRQ | "flat spectrum radio quasar" | "flat-spectrum radio quasars" (Ch1, Ch2, Ch7) | 3 chapters | **Prose wins** — edit the registry to "flat-spectrum radio quasar" |
| d | ICS | "inverse Compton scattering" | "inverse-Compton scattering" (Ch1:71) vs unhyphenated (Ch2, 9 uses) | Ch1, Ch2 | **Registry wins** — the unhyphenated form is standard and is what Ch2 already writes |
| e | EGB / UGRB / DGRB / CMB | lowercase long forms | title case at some intro sites (2.2:55, 2.2:57, 2.2:92 caption, 2.1:60) | Ch2 | **Registry wins** — lowercase, per the file's own header rule. Note 2.2:92 is a caption, so the caption will read "diffuse gamma-ray background (DGRB)" mid-sentence |
| f | GDE (new) | — | "Galactic Diffuse Emission" (title case, 5 sites) | Ch2 | **Lowercase** — "Galactic diffuse emission" |
| g | ACD (new) | — | "Anticoincidence Detector" | Ch2 | **Lowercase** — "anticoincidence detector" |
| h | QF (new) | — | "Quality Factor" (7.2:12) | Ch7 | **Lowercase** — "quality factor" |
| i | AIC (new) | — | "Akaike Information Criterion" (3.1:105) | Ch3 | **"Akaike information criterion"** — surname capitalised only |
| j | MCMC (new) | — | "Markov Chain Monte Carlo" (3.1:187) | Ch3, Ch6 | **"Markov chain Monte Carlo"** |
| k | KS (new) | — | "Kolmogorov--Smirnov (KS) test" | Ch3, Ch7 | Long form is **"Kolmogorov--Smirnov"**, so "a KS test" renders correctly |
| l | dSph | "dwarf spheroidal galaxy" | "dwarf spheroidals" at 5.2:36 (one line before an exact match at 5.2:37) | Ch5 | **Leave 5.2:36 spelled out**; expand at 5.2:37 |
| m | CNN | "convolutional neural network" | "a convolutional network" (conclusion:33, missing "neural") | conclusion | **Leave literal** (single use, F2); or fix the prose wording as a copy-edit |
| n | NPTF (new) | — | "non-Poissonian template fitting" (Ch4) vs "Non-Poissonian Template Fit" (6.2:68) | Ch4, Ch6 | **"non-Poissonian template fitting"** — Ch4 owns 15 of the 16 uses |

## F16 — digit / hyphen / space SHORTs: leave literal (one decision for all)

None of these can produce a typeable `\SHORT` command; each could still be registered for
`\gls{KEY_}`-only use. The recommendation for the whole group is **leave literal** — they are
catalog releases, event-type labels and proper names, and the thesis already treats them that way.
1pPDF (F10) and 2MASS/2MRS (F13) are the two cases argued separately above.

| Token | Where | Uses | Recommendation |
|---|---|---|---|
| 4FGL | Ch2:132/147, Ch7:14 | 3 | literal |
| 4FGL-DR3 | Ch6:16, Ch7:47/77, conclusion:39 | 4 | literal |
| 4FGL-DR4 | Ch2:133/142, Ch5:14, Ch6:17, Ch7:51 | 5 | literal |
| 3FGL | Ch2:132, Ch4:112 | 2 | literal |
| 1FGL | Ch2:132 | 1 | literal |
| PSF0–PSF3 | Ch2:73/112 | 2 | literal |
| p6v11 | Ch4:42 | 1 | literal |
| gNFW | Ch1:160 | 1 | literal |
| L-C2ST | Ch3:107 | 1 | literal (also single-use) |
| BL Lac | Ch1:365/366, Ch2:62/64/65 | 5 | literal — SHORT contains a space |
| H.E.S.S. | — | 0 | does not occur (HESS without dots appears once, Ch8:23) |

## F17 — single-use `Long Form (ABBR)` introductions that fail the ≥2-uses rule

All are recommended **leave spelled out** — one decision covers the set. Listed so none is silently
lost: SED (2.2:61), EBL in Ch2 (2.2:66), EDISP (2.3:112), TS in Ch2 (2.3:125, all later uses are in
math), NLE (3.2:59), ABC (3.2:49), SBC (3.2:105), TARP (3.2:106), SGD (3.3:51), KDE (3.3), GPU
(3.3:52), MC dropout (3.3:69), SIDM (1.2:92 + 1.4:211), ISRF (1.4:128/132), GCE in Ch1 (1.4:327),
CPG (6.3:35), SST (8.3:22), NPTF in Ch6 (6.2:68).

## F18 — mid-compound `CR` ("cosmic-ray X")

**Question.** `CR_` = "cosmic ray" is registered, but the prose mostly writes hyphenated adjectival
compounds: "cosmic-ray protons", "cosmic-ray spectrum", "cosmic-ray background". Substituting the
macro mid-compound changes the hyphenation once the first use fires ("cosmic ray (CR) protons").

**Affected.** Ch1: 7 (3 bare plurals at 1.4:90/111/395, 4 compounds), Ch8: 2 compounds (8.2:53).

**Options.** (a) Leave all `CR` occurrences literal. (b) Convert only the three bare "cosmic rays"
plurals in Ch1 (expand at 1.4:90) and leave every hyphenated compound literal. (c) Convert
everything, accepting the hyphenation change.

**Recommendation: (b).** The bare plurals convert cleanly; the compounds do not, and forcing them
produces awkward output for no gain.

## F19 — CL ("confidence level")

`3.1:120` writes "95\% CL upper bounds"; the long form is never spelled out anywhere in the thesis
and "CL" is not registered. **Recommendation: spell it out** — "95\% confidence-level upper bounds"
— rather than leave a bare undefined abbreviation. This is a one-word prose edit, not a registry
change.

## F20 — "isotropic diffuse gamma-ray background" (6.1:27)

This phrase matches no registry long form: not `DGRB_` ("diffuse gamma-ray background"), not
`UGRB_`, not `EGB_`. It reads like the community term IGRB (isotropic gamma-ray background), which
is not registered. It is a single occurrence, two sentences before an unambiguous UGRB usage at
6.1:38. **Recommendation: confirm it is deliberate**, or reword to "unresolved gamma-ray background"
and fold it into the UGRB conversion.

---

# Proposed new `\newacro` entries

## Unconditional

Ready to paste into `acronyms.tex`, grouped under chapter comments matching that file's existing
style. Deduplicated; every SHORT here yields a typeable `\SHORT` command. Key = SHORT + `_`; long
forms lowercase except genuine proper nouns; `longplural` only where the plural is irregular.

```latex
% Chapter 1 (particle candidates / indirect detection)
\newacro{LHC_}{LHC}{Large Hadron Collider}
\newacro{ALP_}{ALP}{axion-like particle}
\newacro{VIB_}{VIB}{virtual internal bremsstrahlung}

% Chapter 2 (gamma-ray sky / Fermi-LAT)
\newacro{ISM_}{ISM}{interstellar medium}
\newacro{GDE_}{GDE}{Galactic diffuse emission}
\newacro{MSP_}{MSP}{millisecond pulsar}
\newacro{ACD_}{ACD}{anticoincidence detector}

% Chapter 3 (statistical methods / simulation-based inference)
\newacro{MLE_}{MLE}{maximum likelihood estimator}
\newacro{TS_}{TS}{test statistic}
\newacro{KS_}{KS}{Kolmogorov--Smirnov}
\newacro{KL_}{KL}{Kullback--Leibler}
\newacro{AIC_}{AIC}{Akaike information criterion}
\newacro{MCMC_}{MCMC}{Markov chain Monte Carlo}
\newacro{NPE_}{NPE}{neural posterior estimation}
\newacro{NRE_}{NRE}{neural ratio estimation}
\newacro{APS_}{APS}{angular power spectrum}

% Chapter 4 (Galactic Center excess)
\newacro{GCE_}{GCE}{Galactic Center excess}
\newacro{NPTF_}{NPTF}{non-Poissonian template fitting}
\newacro[longplural={low-mass X-ray binaries}]{LMXB_}{LMXB}{low-mass X-ray binary}

% Chapter 7 (probabilistic cataloging)
\newacro{QF_}{QF}{quality factor}
\newacro[longplural={regions of interest}]{RoI_}{RoI}{region of interest}

% Chapter 8 (cross-correlations / CTAO)
\newacro{EBL_}{EBL}{extragalactic background light}
\newacro{IACT_}{IACT}{imaging atmospheric Cherenkov telescope}
\newacro{LST_}{LST}{Large-Sized Telescope}
\newacro{MST_}{MST}{Medium-Sized Telescope}
\newacro{EGAL_}{EGAL}{Extragalactic Survey}
```

**26 entries.** Chapters 5 and 6 and the end matter propose nothing new: every acronym they earn is
either already registered or owned by an earlier chapter.

Three of these carry an open *casing* question (F15 f, g, h — GDE, ACD, QF) and two an open *wording*
question (F15 i, j, k, n — AIC, MCMC, KS, NPTF). Those decisions change the long-form string but
cannot remove the entry, which is why they are here rather than below.

## Conditional on author decisions

Do not paste any of these until the named flag is answered.

```latex
% --- Conditional: typeable SHORTs ---

% F9 — register NFW on the SZ_ precedent? (Ch1: 12 uses, Ch4: 16, Ch6: 1)
\newacro{NFW_}{NFW}{Navarro-Frenk-White}

% F3 — REPLACES the existing dead SCDF_ entry (acronyms.tex:33); this is an edit,
%      not an addition. Delete the SCDF_ line if this is approved.
\newacro{SCD_}{SCD}{source-count distribution}

% F1 — only if the author wants LSS abbreviated (never abbreviated in the prose today)
\newacro{LSS_}{LSS}{large-scale structure}

% F12 — only if HSP/LISP are kept as registry entries despite both uses being
%       definitional intros
\newacro{HSP_}{HSP}{high-synchrotron-peaked}
\newacro{LISP_}{LISP}{low-to-intermediate-synchrotron-peaked}
```

```latex
% --- Conditional: \gls{KEY_}-ONLY entries ---
% The SHORT contains a digit, so \newacro's auto-generated command
% (\1pPDF, \2MASS, \2MRS) cannot be typed in the source. Registration still
% works and the term still appears in the List of Acronyms, but EVERY in-text
% use must be \gls{KEY_} / \Gls{KEY_} / \glspl{KEY_} — never a bare \SHORT.

% F10 — recommended yes (Ch4: 8 uses, Ch6: 12)
\newacro{1pPDF_}{1pPDF}{1-point probability distribution function}

% F13 — recommended NO (survey proper names; leave literal like SDSS/DES)
\newacro{2MASS_}{2MASS}{Two Micron All-Sky Survey}
\newacro{2MRS_}{2MRS}{2MASS Redshift Survey}
```

## Recommended edits to existing entries

These modify `acronyms.tex` lines that already exist, per F15 a–c. They change what `glossaries`
prints at first use; they do not add or remove keys.

```latex
% was: \newacro{PSF_}{PSF}{point spread function}
\newacro{PSF_}{PSF}{point-spread function}

% was: \newacro[longplural={star forming galaxies}]{SFG_}{SFG}{star forming galaxy}
\newacro[longplural={star-forming galaxies}]{SFG_}{SFG}{star-forming galaxy}

% was: \newacro[longplural={flat spectrum radio quasars}]{FSRQ_}{FSRQ}{flat spectrum radio quasar}
\newacro[longplural={flat-spectrum radio quasars}]{FSRQ_}{FSRQ}{flat-spectrum radio quasar}
```

---

# Coverage verdict

**Coverage is complete. No gap.**

All 39 in-scope files appear in this document. Thirty-seven carry inventory rows; two are recorded
explicitly as having no acronyms:

- `chapter_02/sections/2.0_introduction.tex` — no acronym token; its one spelled-out "Fermi Large
  Area Telescope" is recorded as the chapter-earliest LAT occurrence (see F5).
- `introduction/introduction.tex` — three lines, a heading plus `\initial{T}he introduction`; no
  candidate token of any kind. Also not imported by `main.tex`.

Per-chapter file counts match the plan's in-scope sets exactly: Ch1 6, Ch2 4, Ch3 6, Ch4 5, Ch5 4,
Ch6 5, Ch7 3, Ch8 4, end matter 2 — 39 total. **No out-of-scope file appears** in any table: no
`paper_*/` content, no paper wrapper, no `frontmatter/abstract_*`, no `resumen/`, no `papers/`, no
backup file.

**Row count:** 220 inventory rows across the nine tables (Ch1 39, Ch2 35, Ch3 31, Ch4 22, Ch5 16,
Ch6 24, Ch7 19, Ch8 22, end matter 12). No row from any partial was dropped; every row whose
`Action` changed during reconciliation is marked in place and listed in R6.

---

# Author decisions (recorded 2026-09-09)

Resolved by the author via Review Mode annotations plus chat clarifications at the Task 1 Step 5
checkpoint. Where a decision differs from the document's recommendation, the decision below wins.

| Flag | Decision | Date |
|---|---|---|
| F1 ML / NN / LSS | Leave spelled out; do not register `LSS_`; `ML_`/`NN_` stay registered but unused | 2026-09-09 |
| F2 single-use registered keys | **CONVERT** (overrides recommendation): a registered key converts wherever it appears, even a single use in a chapter — the per-chapter expansion is pedagogical | 2026-09-09 |
| F3 SCD vs SCDF_ | (a) Rename `SCDF_` -> `\newacro{SCD_}{SCD}{source-count distribution}` | 2026-09-09 |
| F4 dark matter / DM | Keep "dark matter" spelled out (house style confirmed). Normalize the ~10 stray bare "DM" tokens in 5.4 and Ch8 to "dark matter"; if a compound turns awkward, flag rather than force | 2026-09-09 |
| F5 bare standalone LAT | **REWRITE as "Fermi-LAT"** (overrides recommendation): standalone "LAT" becomes the *Fermi*-LAT form matching the surrounding file (e.g. `\fermi` macro); no `\gls{LAT_}` conversion; `LAT_` stays registered but unused | 2026-09-09 |
| F6 SNR dual meaning | **TWO entries** (overrides recommendation): keep `SNR_` = supernova remnant; add signal-to-noise ratio via raw `\newacronym{SNRatio_}{SNR}{signal-to-noise ratio}` (`\gls{SNRatio_}`-only — a second `\newacro` would collide on the `\SNR` command). Both appear distinctly in the List of Acronyms | 2026-09-09 |
| F7 IC_ vs ICS_ | (a) `ICS_` only; adjectival "inverse Compton" phrases stay literal; `IC_` registered but unused | 2026-09-09 |
| F8 AGN_ vs mAGN_ | (a) "misaligned AGN(s)" maps to `mAGN_` | 2026-09-09 |
| F9 NFW | (a) Register `\newacro{NFW_}{NFW}{Navarro-Frenk-White}` and convert | 2026-09-09 |
| F10 1pPDF | (a) Register, `\gls{1pPDF_}`-only; long form "1-point probability distribution function" | 2026-09-09 |
| F11 GCE casing | "Galactic Center excess" (lowercase excess) | 2026-09-09 |
| F12 HSP / LISP | **REGISTER both** (overrides recommendation): they recur as source-class labels; long forms from the prose; duplicate definitional intro at 8.3:30 stripped | 2026-09-09 |
| F13 2MASS / 2MRS | **REGISTER both** (overrides recommendation), `\gls{}`-only: spelled out once per chapter, short form after; duplicate spell-out at 8.2:82 stripped; plot labels untouched | 2026-09-09 |
| F14 gPCS | Keep the hand-rolled `\texttt{gPCS}` pattern; no registry entry | 2026-09-09 |
| F15 mechanical casing table (a-n) | Accept all recommendations: prose wins for PSF/SFG/FSRQ (registry long forms edited to hyphenated forms); registry lowercase wins for ICS and the title-case intro sites; new-entry long forms per the table (rows f-k, n); dSph expands at 5.2:37; conclusion CNN row superseded by F2 = convert (with the "convolutional network" wording left as the author wrote it — copy-edit deferred) | 2026-09-09 |
| F16 digit/hyphen/space SHORTs | Leave literal: 4FGL family, 3FGL, 1FGL, PSF0-PSF3, p6v11, gNFW, L-C2ST, BL Lac. (1pPDF, 2MASS, 2MRS carved out by F10/F13) | 2026-09-09 |
| F17 single-use intros | **Revised rule + carve-outs**: the earn-the-abbreviation rule is >=2 uses THESIS-WIDE (not per chapter). Register as standard abbreviations: SED, EDISP, NLE, ABC, SBC, TARP, SGD, KDE, SIDM, ISRF (long forms from the chapter tables). GPU stays as-is (literal, no entry). MC dropout, CPG, SST: spell out, strip the "(ABBR)" parenthetical | 2026-09-09 |
| F18 CR compounds | (b) Convert only the three bare "cosmic rays" plurals in Ch1; hyphenated compounds stay literal | 2026-09-09 |
| F19 CL | Spell out "confidence-level" at 3.1:120; no entry | 2026-09-09 |
| F20 isotropic diffuse gamma-ray background | Keep written in full at 6.1:27; deliberate | 2026-09-09 |

Additional checkpoint decisions (raised in review, outside F1-F20):

| Item | Decision | Date |
|---|---|---|
| SM ("Standard Model", ~33 uses) | Keep spelled out in full everywhere, consistent with the DM decision; no `SM_` entry. Math-mode $\mathrm{SM}$ untouched (skip zone) | 2026-09-09 |
| ICM | Keep as-is: 2 uses in 1.1, both already `\ICM` macros — passes the >=2-thesis-wide rule | 2026-09-09 |
