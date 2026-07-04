# Revision plan — §1.2.2 freeze-out completion (supervisor feedback)

Date: 2026-07-04
Target file: `chapter_01/sections/1.2_wimp_paradigm.tex`
Source material: Cirelli–Strumia–Zupan review, `cirelli-paper/arXiv-2406.01705v3/DMreview_5_production.tex` (§5 intro, §5.2.2, §5.2.3)
Bryan notes addressed: **40** (spiegare s-wave prima), **41** (connessione tra omega e n), **48/49** (§1.2.4 paragraph title / "s-wave dominant"); resolves `\aure{}` note at line 104 (Friedmann–Boltzmann connection)

## Approved structure (Approach B — quoted-result chain)

Section spine unchanged: qualitative picture → Steigman figure → Boltzmann equation → relic formula → WIMP miracle. Derivation chain completed with two new display equations, one footnote, ~10 new sentences. No dY/dz machinery, no λ, no before/after-freeze-out asymptotics (explicitly ruled out as too heavy).

## Changes

### 1. Friedmann–Boltzmann link (prose only)
- Append ~2 sentences to the term-by-term paragraph after `eq:boltzmann` (currently lines 140–141).
- Content: H is fixed by the Friedmann equation; radiation domination ρ ∝ g_ρ T⁴ → H ~ T²/M_Pl; this is the expansion clock the annihilation rate Γ competes against.
- Delete the `\aure{bryan wants me to add the part on the connection between freedman and the boltzmann equation}` note (line 104) once done.

### 2. Approximations footnote on `eq:boltzmann`
- One footnote (~5 lines) attached to the equation. Short but complete list:
  - (i) homogeneity — inhomogeneities O(10⁻⁵), no x-dependence;
  - (ii) kinetic equilibrium via fast elastic scattering → thermal momentum distribution → single equation for integrated n_χ(t) with thermally averaged σv;
  - (iii) Maxwell–Boltzmann statistics (valid non-relativistically);
  - (iv) no particle–antiparticle asymmetry;
  - (v) single species, 2→2 annihilation dominant; co-annihilation deferred to §1.2.4;
  - (vi) detailed balance fixes creation term to ⟨σv⟩n_eq².
- Cite `Gondolo:1990dk` + `Cirelli:2024ssz` (both in bib; no new bib entries needed).

### 3. n–Ω connection (Bryan note 41) — NEW display equation
- Extend the Y ≡ n_χ/s paragraph (lines 142–143): after freeze-out Y frozen at Y_∞; today ρ_χ = M_χ s₀ Y_∞.
- New display equation: Ω_χ = M_χ s₀ Y_∞ / ρ_crit, with numerical form Y_∞ ≃ (0.44 eV/M_χ)(Ω_χh²/0.12). [Cirelli eqs. 5.4–5.5]
- One interpretive sentence: cosmology fixes the product M_χ·Y_∞ — heavier candidate ⇒ fewer survivors.
- Suggested label: `eq:omega_Y`.

### 4. Partial-wave expansion moved from §1.2.4 (Bryan note 40)
- Move lines 239–247 (eq:partial_wave + s-/p-wave definitions) nearly verbatim into §1.2.2, placed immediately after the "two cross sections" subtlety paragraph (ends line 152 — flows naturally, that paragraph already closes on velocity dependence).
- Keep label `eq:partial_wave` (no external references exist; verified by grep).
- ADD one line not present in current text: thermal average ⟨σv⟩ = σ₀ + (6T/M)σ₁ + … [Cirelli eq. 5.22] — needed so σ₁/z_fo in Change 5 is motivated.
- The halo-velocity consequences (v² ~ 10⁻⁶ suppression, s-wave constant from freeze-out to halo) STAY in §1.2.4.

### 5. General relic formula → s-wave limit (the supervisor's core edit)
- Replace lead-in to `eq:relic_abundance` (line 154). New sequence:
  - Solving eq:boltzmann gives freeze-out at z_fo ≡ M_χ/T_fo ≈ 25, mass dependence only logarithmic. Tie to (do not duplicate) the existing blue "T_fo ~ M_χ/(20–25)" statement at lines 132–133.
  - Surviving abundance Y_∞ ∝ z_fo / (M_Pl M_χ (σ₀ + 3σ₁/z_fo)) — quoted, not derived. [Cirelli eq. 5.28]
  - Convert via Change-3 relation → NEW display equation [Cirelli eq. 5.29]:
    Ω_χh²/0.12 ≈ (z_fo/25) · 2.2×10⁻²⁶ cm³/s / (σ₀ + 3σ₁/z_fo).
    Suggested label: `eq:relic_general`.
  - Then `eq:relic_abundance` presented explicitly as the pure s-wave limit (σ₁ = 0, ⟨σv⟩ = σ₀). Reader sees where the assumption enters.
- Downstream refs (lines 178, 190) already phrased "in the same s-wave limit" — remain valid, verify wording after edit.
- **Normalization consistency:** Cirelli eq. 5.29 is normalized as Ω h²/0.110 with 2.18×10⁻²⁶; the thesis `eq:relic_abundance` uses 0.12 with 2.2×10⁻²⁶ (Steigman). `eq:relic_general` MUST use the thesis normalization (0.12, 2.2×10⁻²⁶) so its σ₁→0 limit reproduces `eq:relic_abundance` exactly; the few-percent spread between references is already covered by the "to within a few percent" hedge in the surrounding text.

### 6. §1.2.4 cleanup (Bryan notes 48, 49)
- First paragraph no longer defines the expansion; opens from the velocity-mapping question, back-references Eq. eq:partial_wave in §1.2.2.
- Keeps only: s-wave ⇒ cross section constant from freeze-out (v ~ 0.2c) to halo (v ~ 10⁻³c) velocities; p-wave ⇒ present-day rate suppressed by v² ~ 10⁻⁶.
- Retitle paragraph: `\paragraph{$p$-wave suppression.}` (note 48: current title redundant once definition moved).
- Use "s-wave **dominant**" phrasing where the text means leading-order, not pure s-wave (note 49).

## Out of scope (flagged, separate revisions)
- Bryan notes 45–47: G_F²M_χ² valid only in Fermi-interaction approximation (§1.2.3).
- Bryan note 35: notation change on Steigman figure (Y vs new notation).
- Bryan note 42: model-building phrase — already commented out in tex.

## Style constraints for the drafter
- Physical picture before formulas (author preference).
- Long paragraphs, no bullets in prose; em dashes; first-person plural.
- New prose marked `\blue{}` to match the current revision-tracking convention in this file.
- No new bib entries required; cite only `Gondolo:1990dk`, `Cirelli:2024ssz`, `Steigman:2012nb` (existing).
- No operator-EFT language (author's QFT comfort: master's-level SM).
