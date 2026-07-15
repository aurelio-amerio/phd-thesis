# Over-Citation Audit — `Cirelli:2024ssz` & `Hooper:2024`

**Goal:** thin out repeat citations of the two review-type references in Ch. 1 (and Ch. 2). Fine to cite each once (or a few times) per section where material is first introduced; the problem is repeat cites within the same paragraph/section and citing *both* together when one suffices.

**Legend:** KEEP · REMOVE (drop the cite, or drop this key from a multi-key `\cite`) · DEMOTE→key (multi-key cite carrying both reviews → keep only the named key).

**Preserved throughout:** figure-credit lines, explicit "we refer the reader to the reviews by…" signpost sentences, the one direct quotation.

> Backup/duplicate files (`.bk`, `copy.tex`, `~lock~`) and `%`-commented lines were excluded.

> **Amended 2026-07-15 (second-pass review).** Verdicts below already incorporate the amendments: two cite groups missed in the first pass added (1.4 L323, 1.4 L390 second group); over-removals that orphaned review-sourced numbers reversed (L133, L350); kept-cite placement swapped onto the load-bearing claim where the first pass mechanically kept the paragraph's *first* cite (L165→L173, L232→L234); further thinning where a paragraph still carried two review hits or duplicated a treatment elsewhere (L67, L397, L417).

---

## Summary

| Key | Compiled uses | KEEP | REMOVE / demoted-away |
|---|---:|---:|---:|
| `Cirelli:2024ssz` | 102 | 40 | 62 |
| `Hooper:2024` | 46 | 21 | 25 |
| **Combined** | **148** | **61** | **87** |

**Per-section:**
- §1.0 Introduction — Cirelli 3→2
- §1.1 Evidence — Cirelli 14→6
- §1.2 / freezout — Cirelli 6→4
- §1.3 Searching for DM — Cirelli 10→5; Hooper 6→4
- §1.4 Indirect detection — **Cirelli 68→22; Hooper 30→11 (worst offender)**
- §2.1 Production mechanisms — Hooper 10→6
- §2.2 Astrophysical sky — Cirelli 1→1 (no issue)

**Removal patterns (decreasing safety):**
1. Review tacked onto a sentence that already carries a specific primary cite (ATLAS, IceCube, PAMELA, Cuoco, Bonnivard, Fermi-LAT, Bergstrom, Bringmann, Ciafaloni, Blumenthal, Strong, DGRB-review, Cohen/Blanco).
2. Both reviews cited together where one suffices (11 pairs → DEMOTE).
3. Consecutive-sentence repeats of the same review for closely related sub-claims.

**Placement principle (added in second pass):** when a paragraph keeps a single review cite, place it on the most load-bearing claim — usually the quantitative one, often at the paragraph's end — not mechanically on the first occurrence. A review cite that is the *actual source of a number* outranks a definitional or scene-setting sentence.

---

## chapter_01/sections/1.0_introduction.tex

| Line | Cite | Verdict | Why |
|---|---|---|---|
| 8 | `\cite{Cirelli:2024ssz}` | KEEP | First Cirelli in the chapter (CMB matter density). |
| 12 | `\cite{Cirelli:2024ssz,Steigman:2012nb}` | KEEP | First WIMP-miracle claim; paired with distinct specific source. |
| 13 | `\cite{Cirelli:2024ssz,Bergstrom:1997fj}` | REMOVE Cirelli | 1 sentence after L12; Bergstrom carries the indirect-detection claim. |

## chapter_01/sections/1.1_evidence_for_dark_matter.tex

| Line | Cite | Verdict | Why |
|---|---|---|---|
| 7 | `\cite{Cirelli:2024ssz}` | KEEP | Named-methodology ("hierarchical classification of Cirelli et al."). |
| 15 | `\cite{Cirelli:2024ssz}` | REMOVE | 8 lines after L7; standard textbook physics. |
| 52 | `\cite{Walker:2009zp,Wolf:2009tu,Cirelli:2024ssz}` | REMOVE Cirelli | Walker/Wolf source the numbers. |
| 68 | `\cite{Cirelli:2024ssz}` | KEEP | First in cluster subsection §1.1.2; specific number. |
| 71 | `\cite{Cirelli:2024ssz,Bullock:2017xww}` | REMOVE Cirelli | 3 lines after L68; Bullock suffices. |
| 73 | `\cite{Aghanim:2018eyx,Cirelli:2024ssz}` | REMOVE Cirelli | Planck is the specific source. |
| 76 | `\cite{Cirelli:2024ssz,Bullock:2017xww}` | REMOVE Cirelli | Generic lensing description. |
| 84 | `\cite{Cirelli:2024ssz}` | REMOVE | Clowe/Milgrom already cited for Bullet Cluster. |
| 85 | `\cite{Cirelli:2024ssz}` | REMOVE | Harvey:2015hha carries this claim. |
| 94 | `Credit: …\cite{Cirelli:2024ssz}` | KEEP | Figure attribution. |
| 110 | `\cite{Aghanim:2018eyx,Cirelli:2024ssz}` | KEEP | First Cirelli in cosmology subsection §1.1.3. |
| 113 | `\cite{Cirelli:2024ssz}` | REMOVE | 3 lines after L110. |
| 127 | `Credit: …\cite{Cirelli:2024ssz}` | KEEP | Figure attribution. |
| 141 | `Credit: …\cite{Cirelli:2024ssz}` | KEEP | Figure attribution (LSS). |

## chapter_01/sections/1.2_wimp_paradigm.tex

| Line | Cite | Verdict | Why |
|---|---|---|---|
| 35 | `Credit: …\cite{Cirelli:2024ssz}` | KEEP | Figure attribution. |
| 112 | `\cite{Cirelli:2024ssz,Bertone:2004pz}` | KEEP | Only occurrence in §1.2.3; specific technical claim. |

## chapter_01/sections/freezout.tex

| Line | Cite | Verdict | Why |
|---|---|---|---|
| 87 | `\cite{Cirelli:2024ssz}` | KEEP | First in subsection (partial-wave expansion). |
| 97 | `\cite{Steigman:2012nb,Cirelli:2024ssz}` | REMOVE Cirelli | 10 lines after L87; Steigman is the technical source. |
| 112 | `\cite{Cirelli:2024ssz,Steigman:2012nb}` | REMOVE Cirelli | Third Cirelli in 25 lines; keep Steigman. |
| 121 | `Credit: …\cite{Cirelli:2024ssz}` | KEEP | Figure attribution. |

## chapter_01/sections/1.3_searching_for_dark_matter.tex

| Line | Cite | Verdict | Why |
|---|---|---|---|
| 28 | `Credit: …\cite{Cirelli:2024ssz}` | KEEP | Figure attribution. |
| 41 | `\cite{Hooper:2024}` | KEEP | First Hooper in §1.3. |
| 47 | `\cite{Cirelli:2024ssz}` | REMOVE | 2 lines before the L49 review signpost. |
| 49 | `…Schumann~\cite{Schumann:2019eaa}, Cirelli~\cite{Cirelli:2024ssz}, Hooper~\cite{Hooper:2024}` | KEEP (both) | Explicit "further reading" signpost. |
| 55 | `\cite{Cirelli:2024ssz,Hooper:2024}` | DEMOTE→Cirelli | Opens §1.3.2; both-together. |
| 56 | `\cite{Cirelli:2024ssz}` | REMOVE | Following sentence, same topic. |
| 60 | `\cite{Cirelli:2024ssz}` | REMOVE | Third Cirelli in 5 lines. |
| 62 | `\cite{ATLAS:2023tkt,Cirelli:2024ssz}` | REMOVE Cirelli | ATLAS is the specific source. |
| 64 | `\cite{Cirelli:2024ssz,Hooper:2024}` | DEMOTE→Hooper | Cirelli over-used by this point. |
| 70 | `…Boveia~\cite{Boveia:2018yeb}…Cirelli~\cite{Cirelli:2024ssz} and Hooper~\cite{Hooper:2024}` | KEEP (both) | Explicit "further reading" signpost. |
| 79 | `\cite{Lopez-Honorez:2013cua,Hooper:2024}` | REMOVE Hooper | Lopez-Honorez is the specific source. |
| 82 | `\cite{Cirelli:2024ssz}` | KEEP | First/only Cirelli in §1.3.3. |

## chapter_01/sections/1.4_indirect_detection.tex  (largest offender)

### §sec:ann_decay (L20–85)
| Line | Cite | Verdict | Why |
|---|---|---|---|
| 20 | `\cite{Hooper:2024}` | KEEP | First of the section. |
| 35 | `\cite{Hooper:2024}` | KEEP | New equation (annihilation rate). |
| 36 | `\cite{Hooper:2024}` | REMOVE | Following sentence, same topic. |
| 44 | `\cite{Hooper:2024}` | REMOVE | Trivial symbol definition; 4th in 25 lines. |
| 52 | `\cite{Cirelli:2024ssz,Cirelli:2010xx,Arina:2023eic}` | KEEP | Names specific spectral libraries (PPPC4DMID, CosmiXs). |
| 63 | `\cite{Hooper:2024,Cirelli:2024ssz}` | DEMOTE→Cirelli | Continues L52 spectral-library thread. |
| 64 | `\cite{Hooper:2024}` | KEEP | Distinct claim (Fermi-LAT sensitivity). |
| 67 | `\cite{Hooper:2024}` | REMOVE | *(amended from KEEP)* Paragraph keeps a single cite at its end (L69); two Hoopers in a 4-line paragraph is the pattern we are removing. |
| 68 | `\cite{Cirelli:2024ssz}` | REMOVE | 1 line after L67. |
| 69 | `\cite{Cirelli:2024ssz,Hooper:2024}` | DEMOTE→Hooper | Single end-of-paragraph cite covering all three channel claims (L67–69). |
| 73 | `\cite{Hooper:2024}` | REMOVE | Generic synthesis sentence. |

### §sec:spectral_features (L93–138)
| Line | Cite | Verdict | Why |
|---|---|---|---|
| 93 | `\cite{Cirelli:2024ssz}` | KEEP | First in subsection (γγ line). |
| 94 | `\cite{Bergstrom:1997fj,Cirelli:2024ssz}` | REMOVE Cirelli | Bergstrom is the original line paper. |
| 101 | `\cite{Bringmann:2007nk,Cirelli:2024ssz}` | REMOVE Cirelli | Bringmann is the specific VIB paper. |
| 102 | `\cite{Bringmann:2007nk,Cirelli:2024ssz}` | REMOVE Cirelli | Same pair repeated next sentence. |
| 118 | `\cite{Ciafaloni:2010ti,Cirelli:2024ssz}` | REMOVE Cirelli | Ciafaloni is the specific EW-corrections paper. |
| 121 | `\cite{Cirelli:2024ssz}` | REMOVE | Same paragraph as L118. |
| 123 | `\cite{Cirelli:2024ssz}` | REMOVE | 7th Cirelli in subsection. |
| 127 | `\cite{Cirelli:2024ssz,Pinetti:2021jjs}` | KEEP | Opens "prompt vs. secondary" paragraph. |
| 128 | `\cite{Hooper:2024}` | KEEP | First Hooper in paragraph. |
| 131 | `\cite{Blumenthal:1970gc,Hooper:2024}` | REMOVE Hooper | Blumenthal is the original ICS paper. |
| 133 | `\cite{Cirelli:2024ssz}` | KEEP | *(amended from REMOVE)* Worked numbers (1 TeV e → 1.5 GeV / 150 GeV) are sourced to the review; sole surviving review cite for the secondary-emission paragraph, also covers the L136 synchrotron number. |
| 135 | `\cite{Strong:2007nh,Hooper:2024}` | REMOVE Hooper | Strong is the specific ISRF/GALPROP source. |
| 136 | `\cite{Cirelli:2024ssz}` | REMOVE | Third Cirelli in paragraph. |
| 138 | `\cite{Hooper:2024}` | REMOVE | Fourth Hooper in paragraph. |
| 112 | `Credit: …` | KEEP | Figure attribution. |

### §sec:density_profiles (L160–234) — worst subsection (Cirelli 22→7)
| Line | Cite | Verdict | Why |
|---|---|---|---|
| 160 | `\cite{Cirelli:2024ssz}` | KEEP | First (gNFW). |
| 165 | `\cite{Cirelli:2024ssz}` | REMOVE | *(amended from KEEP)* "Later identified as a fitting function" is the weaker claim; the Einasto block's single cite moves to L173. |
| 173 | `\cite{Cirelli:2024ssz}` | KEEP | *(amended from REMOVE)* Load-bearing claim of the Einasto block ($\alpha_\text{Ein} \approx 0.17$ average fit). |
| 192 | `Credit: …` | KEEP | Figure attribution. |
| 197 | `\cite{Cirelli:2024ssz,Pinetti:2021jjs}` | KEEP | Opens "fit to Milky Way" paragraph. |
| 198 | `\cite{Cirelli:2024ssz}` | REMOVE | Following sentence. |
| 199 | `\cite{Cirelli:2024ssz}` | REMOVE | Third consecutive sentence. |
| 202 | `\cite{Cirelli:2024ssz,Navarro:1996gj,Bullock:2017xww}` | REMOVE Cirelli | Redundant with L197. |
| 203 | `\cite{Cirelli:2024ssz}` | REMOVE | Follows L202. |
| 208 | `\cite{Cirelli:2024ssz,Bullock:2017xww}` | KEEP | Names cusp–core problem. |
| 213 | `\cite{Cirelli:2024ssz,Bullock:2017xww}` | REMOVE Cirelli | Same cusp–core paragraph. |
| 215 | `\cite{Cirelli:2024ssz,Bullock:2017xww}` | REMOVE Cirelli | Third pair in 8 lines. |
| 220 | `\cite{Springel:2008cc,Diemand:2008in,Cirelli:2024ssz}` | KEEP | Opens boost-factor paragraph. |
| 223 | `\cite{Cirelli:2024ssz}` | REMOVE | 3 lines after L220. |
| 225 | `\cite{…,Cirelli:2024ssz}` ×2 | REMOVE (both) | Two Cirelli in one sentence; specific papers already listed. |
| 226 | `\cite{Cirelli:2024ssz,Sanchez-Conde:2013yxa}` | REMOVE Cirelli | Sanchez-Conde established. |
| 227 | `\cite{Sanchez-Conde:2013yxa,Moline:2016pbm,Cirelli:2024ssz}` | REMOVE Cirelli | 6th–7th mention in paragraph. |
| 228 | `\cite{Cirelli:2024ssz,Sanchez-Conde:2013yxa}` | REMOVE Cirelli | Same. |
| 232 | `\cite{Cirelli:2024ssz}` | REMOVE | *(amended from KEEP)* Definitional sentence; the paragraph's single cite moves to L234. |
| 233 | `\cite{Cirelli:2024ssz}` | REMOVE | Middle of the same chain. |
| 234 | `\cite{Cirelli:2024ssz}` | KEEP | *(amended from REMOVE)* Carries the specific number ($M_\text{min} \sim 10^{-6}\,M_\odot$) at the end of the paragraph, covering the whole L232–234 chain. |

### §sec:jfactor (L242–306)
| Line | Cite | Verdict | Why |
|---|---|---|---|
| 242 | `\cite{Cirelli:2024ssz,Hooper:2024}` | DEMOTE→Cirelli | Master flux equation (punchline); keep one. |
| 257 | `\cite{Cirelli:2024ssz}` | REMOVE | Same equation exposition as L242. |
| 259 | `\cite{Cirelli:2024ssz}` | REMOVE | 2 lines after L257. |
| 261 | `\cite{Cirelli:2024ssz,Pinetti:2021jjs}` | REMOVE Cirelli | Keep Pinetti (decay-specific). |
| 281 | `\cite{Pinetti:2021jjs,Cirelli:2024ssz}` | REMOVE Cirelli | Pinetti is the decay/D-factor companion. |
| 295 | `\cite{Hooper:2024,Cirelli:2024ssz,Bonnivard:2015xpq}` | DEMOTE→Hooper | Bonnivard is the actual J-factor paper; drop 2nd review. |
| 302 | `\cite{Cirelli:2024ssz}` | KEEP | New caveats paragraph. |
| 306 | `\cite{Cirelli:2024ssz}` … `\cite{Hooper:2024}` | REMOVE Cirelli only | Cirelli redundant with L302; keep Hooper (distinct number). |

### §sec:targets (L317–371)
| Line | Cite | Verdict | Why |
|---|---|---|---|
| 317 | `\cite{Hooper:2024}` | KEEP | Opens "Galactic Center" paragraph. |
| 318 | `\cite{Hooper:2024}` | REMOVE | Following sentence. |
| 319 | `\cite{Hooper:2024}` | REMOVE | Third consecutive sentence. |
| 323 | `\cite{Hooper:2024}` | KEEP | *(added — missed in first pass)* Only cite in the astrophysical-contamination paragraph (SNRs, pulsars, Sgr A*). |
| 338 | `\cite{Cirelli:2024ssz}` | KEEP | Opens "dwarf spheroidal" paragraph. |
| 342 | `\cite{Cirelli:2024ssz}` | REMOVE | 4 lines later, same paragraph. |
| 346 | `\cite{Fermi-LAT:2015att,2024PhRvD.109f3024M,Hooper:2024}` | REMOVE Hooper | Fermi-LAT papers are the source. |
| 350 | `\cite{Cirelli:2024ssz}` | KEEP | *(amended from REMOVE)* Single-star J-factor sensitivity is a strong quantitative claim and this is the only source in the systematics paragraph (L349–353); removing both L350 and L351 would leave it unsourced. |
| 351 | `\cite{Cirelli:2024ssz}` | REMOVE | Following sentence; covered by L350. |
| 367 | `\cite{DGRB-review,Cirelli:2024ssz}` | REMOVE Cirelli | DGRB-review is the dedicated UGRB review. |
| 371 | `\cite{DGRB-review,Pinetti:2021jjs,Cirelli:2024ssz}` | REMOVE Cirelli | Same. |

### §sec:multi_messenger (L384–397)
| Line | Cite | Verdict | Why |
|---|---|---|---|
| 384 | `\cite{Cirelli:2024ssz,Hooper:2024}` | DEMOTE→Cirelli | Opens "Neutrinos" paragraph. |
| 385 | `\cite{Cirelli:2024ssz}` | REMOVE | 2nd of 4 consecutive sentences. |
| 386 | `\cite{IceCube:2016dgk,Cirelli:2024ssz}` | REMOVE Cirelli | IceCube is the specific paper. |
| 387 | `\cite{Cirelli:2024ssz}` | REMOVE | 4th consecutive sentence. |
| 389 | `\cite{Cirelli:2024ssz,Pinetti:2021jjs}` | KEEP | Opens "Charged cosmic rays" paragraph. |
| 390 | `\cite{PAMELA:2008gwm,Cirelli:2024ssz}` | REMOVE Cirelli | PAMELA is the data paper. |
| 390 (2nd group) | `\cite{Cirelli:2024ssz,Hooper:2024}` | REMOVE (both) | *(added — missed in first pass)* Same line, "widely attributed to nearby pulsars"; paragraph already anchored at L389. |
| 391 | `\cite{Cuoco:2016eej,Cirelli:2024ssz}` | REMOVE Cirelli | Cuoco is the specific paper. |
| 392 | `\cite{Cirelli:2024ssz}` | REMOVE | 4th consecutive sentence. |
| 394 | `\cite{Cirelli:2024ssz,Hooper:2024}` | DEMOTE→Hooper | Cirelli 5th redundant hit in paragraph. |
| 397 | `\cite{Lopez-Honorez:2013cua,Aghanim:2018eyx,Hooper:2024}` | REMOVE Hooper | *(amended from KEEP)* Lopez-Honorez + Planck carry the claim; the identical claim in §1.3.3 (1.3 L79) already had Hooper removed — treat both the same. |

### §sec:status (L411–439)
| Line | Cite | Verdict | Why |
|---|---|---|---|
| 411 | `\cite{2024PhRvD.109f3024M,Hooper:2024}` | REMOVE Hooper | Specific dSph paper suffices. |
| 412 | `\cite{Cirelli:2024ssz}` | KEEP | First in subsection. |
| 413 | `\cite{Cohen:2016uyg,Blanco_2019,Cirelli:2024ssz}` | REMOVE Cirelli | Two specific lifetime-bound papers listed. |
| 417 | `\cite{Cirelli:2024ssz,Hooper:2024}` | REMOVE (both) | *(amended from DEMOTE→Cirelli)* Recap of §1.3.1 with an explicit "(see Section 1.3)" cross-ref carrying it; same treatment as L418. |
| 418 | `\cite{Cirelli:2024ssz,Hooper:2024}` | REMOVE (both) | Follows L417; already covered in §1.3.2. |
| 424 | `\cite{Daylan:2014rsa,Cirelli:2024ssz,Hooper:2024}` | DEMOTE→Cirelli | Daylan is the GCE discovery paper. |
| 428 | `\cite{Cirelli:2024ssz,Hooper:2024}` | DEMOTE→Hooper | Avoids doubling Cirelli in same paragraph. |
| 429 | `\cite{Cirelli:2024ssz}` | KEEP | New content (511 keV, 3.5 keV, DAMA/LIBRA). |
| 439 | `\cite{Cirelli:2024ssz}` | KEEP | Direct quotation ("a field at a turning point"). |

## chapter_02/sections/2.1_production_mechanisms.tex

| Line | Cite | Verdict | Why |
|---|---|---|---|
| 27 | `\cite{Hooper:2024}` | KEEP | First (pion threshold). |
| 28 | `\cite{Hooper:2024}` | REMOVE | Following sentence, same paragraph. |
| 49 | `\cite{Hooper:2024}` | KEEP | Distinct formula (pion decay spectrum). |
| 69 | `\cite{Hooper:2024}` | KEEP | Opens ICS spectral-index discussion. |
| 74 | `\cite{Hooper:2024}` | REMOVE | Symbol definition in same passage as L69. |
| 86 | `\cite{Hooper:2024}` | KEEP | New regime (Klein–Nishina). |
| 92 | `\cite{Hooper:2024}` | REMOVE | Continuation of L86. |
| 99 | `\cite{Hooper:2024}` | KEEP | Only cite in Bremsstrahlung paragraph. |
| 105 | `\cite{Hooper:2024}` | KEEP | Opens Synchrotron paragraph. |
| 107 | `\cite{Hooper:2024}` | REMOVE | Follows L105, same paragraph. |

## chapter_02/sections/2.2_astrophysical_sky.tex

| Line | Cite | Verdict | Why |
|---|---|---|---|
| 28 | `\cite{Cirelli:2024ssz}` | KEEP | Sole active occurrence; no issue. |
