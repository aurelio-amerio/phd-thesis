# Acronym Consistency Pass — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Normalize acronym usage across all English thesis prose to the glossaries macro system, produce a complete acronym inventory, and verify the back-matter List of Acronyms renders complete.

**Architecture:** Four phases — (1) read-only inventory of every acronym in scope, with an author checkpoint; (2) one-shot extension of `acronyms.tex` plus per-chapter `\glsresetall` resets; (3) mechanical per-chapter conversion following the repo's `acronyms` skill procedure, one commit per chapter; (4) full build + glossary verification.

**Tech Stack:** LaTeX (memoir + glossaries long-short style), `latexmk`, `makeglossaries`, repo skill `.claude/skills/acronyms/SKILL.md`.

**Spec:** `docs/superpowers/specs/2026-09-01-acronym-consistency-design.md`

## Global Constraints

- **Never modify:** `paper_*` directories and their contents; the paper wrapper files (`chapter_04/sections/4.5_paper.tex`, `chapter_05/sections/5.6_paper_dmhalos.tex`, `chapter_06/sections/6.5_paper_dnds.tex`, `chapter_07/sections/7.4_paper_dnds_catalog.tex`, `chapter_08/sections/8.4_paper_xcorr.tex`); `frontmatter/abstract_en.tex`, `abstract_es.tex`, `abstract_vlc.tex`; `resumen/`; `papers/`; any `*.bak*`, `*.bk`, `*.old`, `* copy*` file.
- **Conversion rulebook:** every conversion task's executor MUST read `.claude/skills/acronyms/SKILL.md` before editing — it defines markup forms (`\SHORT` / `\Gls{KEY_}` / `\glspl{KEY_}` / `\Glspl{KEY_}`), skip zones (math, `\cite`/`\ref`/`\label` args, comments, `\aure{}`, units, `$\Lambda$CDM`, surnames, survey/instrument proper names), the "earn the abbreviation" ≥2-uses rule, and the common-mistakes table.
- **First-use override (differs from the skill!):** this thesis uses `\glsresetall` at the start of every chapter (added in Task 2). First-use expansion is therefore **per chapter**, not document-wide: within each chapter, the earliest in-scope running-prose occurrence of a key expands; do NOT grep earlier chapters to suppress expansion. Everything else in the skill's first-use guidance (prefer running prose over captions/lead-ins, strip redundant manual "(SHORT)" parentheticals) still applies per chapter.
- **Headings stay literal:** never put `\gls`/`\SHORT` macros inside `\chapter/\section/\subsection/\paragraph` titles. Plain short form there.
- **"dark matter" / DM stays literal** (house style; the skill forbids macro-izing it) unless the author's inventory review (Task 1 checkpoint) decides otherwise.
- **No `\blue{}` marking.** Review is via git diff; one commit per chapter.
- **`acronyms.tex` is frozen after Task 2.** A conversion task that discovers a missing entry does not add it — it flags it in its report and leaves the occurrence literal.
- **New entries use `\newacro` only** (never raw `\newacronym`), key = `SHORT_`, long form lowercase except proper nouns, `[longplural={...}]` where irregular. A SHORT containing digits or hyphens cannot get a `\SHORT` command — register it for `\gls{KEY_}` use or leave it out; flag such cases.
- **Build command** (from repo root): `latexmk -pdf -interaction=nonstopmode main.tex`. If the List of Acronyms is missing from the PDF, run `makeglossaries main` and rebuild. A build "passes" when the exit code is 0 and `grep -c "Undefined control sequence" main.log` returns 0.
- **Commit footer** for every commit:
  `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`
  `Claude-Session: https://claude.ai/code/session_0129u3bcwbDuvrFvLtD5NCa2`

## In-scope file sets (used by Tasks 1 and 3–10)

- **Ch1:** `chapter_01/sections/1.0_introduction.tex`, `1.1_evidence_for_dark_matter.tex`, `1.2_wimp_paradigm.tex`, `1.3_searching_for_dark_matter.tex`, `1.4_indirect_detection.tex`, `freezout.tex`
- **Ch2:** `chapter_02/sections/2.0_introduction.tex`, `2.1_production_mechanisms.tex`, `2.2_astrophysical_sky.tex`, `2.3_fermi_lat.tex`
- **Ch3:** `chapter_03/sections/3.0_introduction.tex`, `3.1_inference.tex`, `3.2_sbi.tex`, `3.3_ml_astrophysics.tex`, `3.4_domain_shift.tex`, `3.5_cross_correlations.tex`
- **Ch4:** `chapter_04/sections/4.0_introduction.tex`, `4.1_discovery_and_characterization.tex`, `4.2_msp_hypothesis.tex`, `4.3_systematics_stalemate.tex`, `4.4_breaking_the_stalemate.tex`
- **Ch5:** `chapter_05/sections/5.1_introduction.tex`, `5.2_dark_matter_substructure.tex`, `5.3_dm_subhalos_gamma_ray_targets.tex`, `5.4_unassociated_sources.tex`
- **Ch6:** `chapter_06/sections/6.0_introduction.tex`, `6.1_limits_individual.tex`, `6.2_source_count.tex`, `6.3_sbi_cnn.tex`, `6.4_transition.tex`
- **Ch7:** `chapter_07/sections/7.0_introduction.tex`, `7.1_limits_of_threshold.tex`, `7.2_population_to_spatial.tex`
- **Ch8:** `chapter_08/sections/8.0_introduction.tex`, `8.1_from_resolved_to_cosmic_web.tex`, `8.2_cross_correlation_technique.tex`, `8.3_ctao.tex`
- **End matter:** `conclusion/conclusion.tex`, `introduction/introduction.tex` (3 lines, likely nothing to do — scan anyway)

---

### Task 1: Acronym inventory (read-only) + author checkpoint

**Files:**
- Create: `docs/superpowers/specs/2026-09-01-acronym-inventory.md`
- Read only: all files in "In-scope file sets" above, plus `acronyms.tex`

**Interfaces:**
- Produces: the inventory document that Task 2 turns into `\newacro` entries and that Tasks 3–10 consult for their per-chapter conversion lists.

- [ ] **Step 1: Scan every in-scope file.** For each file, collect acronym occurrences: literal SHORT tokens (`CMB`, `NFW`, `MSP`, `GCE`, `MCMC`, …), `Long Form (ABBR)` introductions, and existing macro uses (`\CMB`, `\gls{...}`). Detection and exclusion rules per the skill's step 2 (see Global Constraints). This step is read-only and parallelizable — one scan agent per chapter is fine.

- [ ] **Step 2: Write the inventory document** with one table per chapter (plus end matter), columns:

```markdown
| Acronym | Long form | Occurrences (file: count) | Registry status | Action |
```

`Registry status` ∈ {`defined+macro-used`, `defined-but-literal`, `undefined`, `excluded`}. `Action` ∈ {`convert`, `add-entry+convert`, `leave` (with one-line reason), `FLAG` (author must decide)}. Mandatory FLAG entries at minimum: "dark matter"/DM (house style says leave); any dual-meaning SHORT (e.g. SNR = supernova remnant in the registry vs signal-to-noise ratio in prose; IC vs ICS); any casing mismatch between registry long form and prose; digit/hyphen SHORTs (no `\SHORT` macro possible); single-use `(ABBR)` intros that fail the ≥2-uses rule. Close the document with a consolidated "Proposed new `\newacro` entries" block, ready to paste, grouped by chapter of first appearance.

- [ ] **Step 3: Sanity-check coverage.** Every file in the in-scope sets appears in at least one table row or an explicit "no acronyms found" line. No file outside scope appears.

- [ ] **Step 4: Commit**

```bash
git add docs/superpowers/specs/2026-09-01-acronym-inventory.md
git commit -m "acronyms: full inventory of thesis prose (phase 1)"
```

- [ ] **Step 5: CHECKPOINT — author review.** Present the FLAG rows and the proposed new-entry block to the author. Do not start Task 2 until the author resolves the flags (which flagged terms convert, which stay literal, DM decision confirmed). Record the decisions inline in the inventory file and amend the commit.

### Task 2: Extend `acronyms.tex` and add per-chapter resets

**Files:**
- Modify: `acronyms.tex`
- Modify: `chapter_01/chapter_1.tex` … `chapter_08/chapter_8.tex`, `conclusion/conclusion.tex`

**Interfaces:**
- Consumes: approved "Proposed new `\newacro` entries" block from the Task 1 inventory.
- Produces: frozen `acronyms.tex` (no later task edits it); `\glsresetall` in place so Tasks 3–10 can rely on per-chapter first-use semantics.

- [ ] **Step 1: Add the approved `\newacro` entries** to `acronyms.tex`, grouped under chapter comments matching the file's existing style (cf. the `% Chapter 1 (cosmology / evidence for dark matter)` block). Follow the entry conventions in Global Constraints.

- [ ] **Step 2: Add `\glsresetall` to each chapter wrapper.** In each of the 8 wrappers and the conclusion, insert a single line containing `\glsresetall` immediately after the `\label{ch:N}` line (conclusion: immediately after its `\chapter{...}`/`\label` lines; check the file — it starts with its chapter heading). Example for `chapter_04/chapter_4.tex`:

```latex
\chapter{The Galactic Center Gamma-Ray Excess}
\label{ch:4}
\glsresetall
\input{sections/4.0_introduction.tex}
```

- [ ] **Step 3: Build to verify** — new entries can collide with existing LaTeX commands (`\newcommand` in `\newacro` errors on redefinition):

Run: `latexmk -pdf -interaction=nonstopmode main.tex`
Expected: exit 0, `grep -c "Undefined control sequence" main.log` → 0, no "Command \X already defined" in `main.log`. Rendered PDF unchanged in prose (only glossary defs and no-op resets added so far).

- [ ] **Step 4: Commit**

```bash
git add acronyms.tex chapter_0*/chapter_*.tex conclusion/conclusion.tex
git commit -m "acronyms: extend registry, reset first-use per chapter (phase 2)"
```

### Task 3: Convert Chapter 1

**Files:**
- Modify: the six Ch1 files listed in "In-scope file sets"

**Interfaces:**
- Consumes: frozen `acronyms.tex` (Task 2), Ch1 rows of the inventory (Task 1), conversion rulebook + first-use override (Global Constraints).
- Produces: Ch1 prose using glossary macros; a short report of any newly discovered missing entries (left literal, flagged).

- [ ] **Step 1: Read `.claude/skills/acronyms/SKILL.md` and the Ch1 inventory rows.** Note that Ch1 already uses macros in places — the job here is completing coverage and fixing mixed literal/macro usage (one markup form per key per file).

- [ ] **Step 2: Convert each file** in source order (`1.0` → `1.1` → `1.2` → `freezout.tex` (input from 1.2 line 104) → `1.3` → `1.4`), applying the inventory's `convert` actions with the correct markup form per occurrence. Mark the per-chapter first use on the earliest running-prose occurrence in source order (note `freezout.tex` sits inside 1.2, affecting source order for keys it shares with 1.3/1.4). Strip now-redundant manual `(SHORT)` parentheticals. Respect FLAG decisions from the checkpoint. Leave headings literal.

- [ ] **Step 3: Grep audit for the chapter.** For every key the inventory marked `convert` for Ch1, confirm no literal occurrence remains outside headings/comments:

```bash
grep -nE '\b(CMB|BBN|SZ|ICM|dSph|BAO|MOND|PBH|FIMP|WDM|WIMP|...)\b' chapter_01/sections/1.*.tex chapter_01/sections/freezout.tex
```

(Substitute the actual Ch1 convert-list from the inventory.) Expected: hits only in headings, comments, or FLAG-approved literal terms. Investigate anything else.

- [ ] **Step 4: Build**

Run: `latexmk -pdf -interaction=nonstopmode main.tex`
Expected: exit 0, no undefined control sequences; spot-check the Ch1 pages in `main.pdf` for gobbled spaces ("CMBphotons"), double expansions, or an expansion firing inside a caption/lead-in.

- [ ] **Step 5: Commit**

```bash
git add chapter_01/sections/
git commit -m "acronyms: normalize chapter 1 (phase 3)"
```

### Task 4: Convert Chapter 2

Same procedure as Task 3, applied to the Ch2 file set (`2.0` → `2.3` in source order), Ch2 inventory rows, grep audit restricted to `chapter_02/sections/2.*.tex`, build, then:

```bash
git add chapter_02/sections/
git commit -m "acronyms: normalize chapter 2 (phase 3)"
```

The full step cycle (read rulebook + inventory rows → convert in source order → chapter grep audit → build → commit) is identical for Tasks 4–10; each executor still performs every step explicitly.

- [ ] Steps 1–5 as in Task 3, for Ch2.

### Task 5: Convert Chapter 3

- [ ] Steps 1–5 as in Task 3, for the Ch3 file set (`3.0` → `3.5`), commit message `acronyms: normalize chapter 3 (phase 3)`.

### Task 6: Convert Chapter 4

- [ ] Steps 1–5 as in Task 3, for the Ch4 file set (`4.0` → `4.4`; `4.5_paper.tex` is untouchable), commit message `acronyms: normalize chapter 4 (phase 3)`.

### Task 7: Convert Chapter 5

- [ ] Steps 1–5 as in Task 3, for the Ch5 file set (`5.1` → `5.4`; `5.6_paper_dmhalos.tex` untouchable), commit message `acronyms: normalize chapter 5 (phase 3)`.

### Task 8: Convert Chapter 6

- [ ] Steps 1–5 as in Task 3, for the Ch6 file set (`6.0` → `6.4`; `6.3` already partly uses macros — unify to one form per key; `6.5_paper_dnds.tex` untouchable), commit message `acronyms: normalize chapter 6 (phase 3)`.

### Task 9: Convert Chapter 7

- [ ] Steps 1–5 as in Task 3, for the Ch7 file set (`7.0` → `7.2`; `7.4_paper_dnds_catalog.tex` untouchable), commit message `acronyms: normalize chapter 7 (phase 3)`.

### Task 10: Convert Chapter 8 + end matter

- [ ] Steps 1–5 as in Task 3, for the Ch8 file set (`8.0` → `8.3`; `8.3` already partly uses macros; `8.4_paper_xcorr.tex` untouchable) plus `conclusion/conclusion.tex` and `introduction/introduction.tex` (conclusion gets its own first-use tracking via its `\glsresetall` from Task 2; the 3-line introduction likely needs nothing). Commit message `acronyms: normalize chapter 8 + end matter (phase 3)`.

### Task 11: Final verification (phase 4)

**Files:**
- Modify: none expected (fixes only if verification fails)

**Interfaces:**
- Consumes: everything above.
- Produces: a short verification report in the task output (not a file), and the final green build.

- [ ] **Step 1: Clean full build**

```bash
latexmk -C main.tex && latexmk -pdf -interaction=nonstopmode main.tex
```

If the List of Acronyms is empty/missing: `makeglossaries main && latexmk -pdf -interaction=nonstopmode main.tex`.
Expected: exit 0; `grep -c "Undefined control sequence" main.log` → 0; no glossaries warnings in `main.log` (`grep -i "glossar" main.log` shows no warnings).

- [ ] **Step 2: Check the List of Acronyms in `main.pdf`.** Every converted acronym appears; long forms read correctly (casing, plurals); sorted sensibly; no orphan entries the author would not expect (glossaries prints only referenced keys, so orphans indicate a stray `\gls`).

- [ ] **Step 3: Spot-check per-chapter first use.** Open the first pages of Chapters 4, 6, and 8 in the PDF: recurring acronyms (e.g. MSP, SBI, CTAO) re-expand at their first use in each of those chapters.

- [ ] **Step 4: Global residue audit.** Re-run the Task-3-style grep across all in-scope files with the full convert-list from the inventory. Expected: hits only in headings, comments, and FLAG-approved literals. List any residue in the report.

- [ ] **Step 5: Report to author.** Summarize: entries added, files touched, flags resolved and how, any deferred items (missing entries discovered mid-conversion, casing questions). No commit unless fixes were made (then `git commit -m "acronyms: verification fixes (phase 4)"`).
