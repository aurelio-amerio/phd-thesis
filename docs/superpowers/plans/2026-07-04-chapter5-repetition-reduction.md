# Chapter 5 Repetition Reduction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reduce intra-chapter redundancy in Chapter 5 (§5.3 and §5.4) by condensing five duplicated passages to a primary treatment plus cross-references, without gutting any section.

**Architecture:** Five surgical, single-passage edits across two narrative `.tex` files. Each edit `%`-comments the original line(s) and inserts a `\blue{}`-wrapped replacement directly below, so the change is visible in the rendered PDF and the old text is recoverable. No physics content, advocacy, or citations change. Prose wording is the implementer's decision; each task fixes only *what* to keep, drop, and cross-reference.

**Tech Stack:** LaTeX (memoir + `dinostyle.sty`), `latexmk`/`pdflatex`, BibTeX (JHEP).

## Global Constraints

- New/modified text wrapped in `\blue{...}` (defined `macros.tex:58`). Apply per sentence/clause. `\blue{}` must **not** span paragraph breaks and must **not** contain `%` characters.
- Never delete a replaced sentence: keep the original as a `%`-commented line directly above its replacement. Pure deletions → comment out, don't remove.
- Citations: existing bib keys only. Do **not** create BibTeX entries. All keys needed here already appear in §5.4.
- Preserve **every** `\aure{}` marker in the touched passages (§5.4.1 line 17, line 25; §5.4.2 line 31, line 39). Do not delete or move them.
- Cross-reference labels used — all verified to exist: `sec:5.2.2` (`5.2_dark_matter_substructure.tex:32`), `sec:5.4.1`, `sec:5.4.2` (in `5.4_unassociated_sources.tex`), `sec:stat-model` (`paper_dm_halos/sections/statistical_analysis.tex:101`).
- Do **not** edit `paper_dm_halos/` prose, the `5.6` wrapper, or any other chapter. The author's paper-intro commenting is already done — do not touch it.
- Locate each edit by the quoted **anchor text**, not by line number (line numbers drift as edits are applied).

---

### Task 1: A1 — condense the "clean target" restatement in §5.3

**Files:**
- Modify: `chapter_05/sections/5.3_dm_subhalos_gamma_ray_targets.tex` (the sentence beginning "Dark subhalos are, in this respect, exceptionally clean targets")

**Interfaces:**
- Consumes: nothing.
- Produces: a cross-reference to `sec:5.2.2` in §5.3 (no symbols other tasks depend on).

**What and why:** The claim "a subhalo below ~10⁸ M☉ contains no stars/gas → any γ-ray emission is pure DM annihilation" is stated in §5.1 (preview), §5.2.2 (dedicated primary), and here in §5.3. Keep §5.2.2 as the primary and §5.1 as legitimate preview. In §5.3, **keep the distinct point** — dark subhalos are exceptionally *clean targets unlike the Galactic Center* — but **drop the re-asserted no-stars/gas premise and the ~10⁸ M☉ figure**, replacing that clause with a cross-reference to `sec:5.2.2`. The implementer writes the exact wording.

- [ ] **Step 1: Locate the passage**

Anchor: `Dark subhalos are, in this respect, exceptionally clean targets: unlike the Galactic Center (Chapter~\ref{ch:4}), a subhalo below $\sim 10^8\,M_\odot$ contains no stars or gas, and any detected gamma-ray emission would originate entirely from dark matter annihilation.`

- [ ] **Step 2: Comment the original and insert the replacement**

`%`-comment the entire original sentence. Directly below it, add the replacement as a single `\blue{...}` sentence that (a) retains the "exceptionally clean target vs. the Galactic Center" contrast and the "emission originates entirely from DM annihilation" conclusion, and (b) replaces the "below ~10⁸ M☉ contains no stars or gas" clause with a pointer to `Section~\ref{sec:5.2.2}`. Keep `\ref{ch:4}`.

- [ ] **Step 3: Verify the edit locally**

Run: `grep -n "sec:5.2.2" chapter_05/sections/5.3_dm_subhalos_gamma_ray_targets.tex`
Expected: the new `\blue{}` line appears with `\ref{sec:5.2.2}`, and the original sentence is present on the line above, prefixed with `%`.
Confirm by eye: the `\blue{}` contains no `%` and no paragraph break.

- [ ] **Step 4: Commit**

```bash
git add chapter_05/sections/5.3_dm_subhalos_gamma_ray_targets.tex
git commit -m "Ch5 §5.3: condense clean-target restatement to xref §5.2.2 (A1)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 2: A3 — add a back-reference in §5.4.2

**Files:**
- Modify: `chapter_05/sections/5.4_unassociated_sources.tex` (the sentence "First, no dark matter subhalo has ever been identified…")

**Interfaces:**
- Consumes: nothing.
- Produces: a cross-reference to `sec:5.4.1` in §5.4.2.

**What and why:** "No DM subhalo has ever been identified" recurs across §5.4.1/5.4.2/5.4.3. §5.4.1 line 24 is the primary (carries the `\aure{}` on contested claims). At §5.4.2 the sentence is load-bearing as the *first* of the three flaws — **keep the sentence, add only a back-reference to `sec:5.4.1`**. This is the smallest possible change.

- [ ] **Step 1: Locate the passage**

Anchor: `First, no dark matter subhalo has ever been identified, so the ``DM'' class used in supervised classification has no empirical anchor and the resulting classification probabilities cannot be calibrated against reality.`
The `\aure{review this statement}` on the following line must be preserved untouched.

- [ ] **Step 2: Comment the original and insert the replacement**

`%`-comment the original sentence. Directly below, add the same sentence with a `\blue{(Section~\ref{sec:5.4.1})}` back-reference inserted after "identified". Only the inserted parenthetical is new text and inside `\blue{}`; the rest of the sentence is reproduced verbatim (it is not itself being reworded).

- [ ] **Step 3: Verify the edit locally**

Run: `grep -n "sec:5.4.1\|review this statement" chapter_05/sections/5.4_unassociated_sources.tex`
Expected: the new back-reference line with `\ref{sec:5.4.1}` appears; the `\aure{review this statement}` marker is still present.

- [ ] **Step 4: Commit**

```bash
git add chapter_05/sections/5.4_unassociated_sources.tex
git commit -m "Ch5 §5.4.2: back-reference first flaw to §5.4.1 (A3)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 3: A2 — strip re-derivation in §5.4.3, keep the Bayes formula

**Files:**
- Modify: `chapter_05/sections/5.4_unassociated_sources.tex` (the sentence beginning "However, as shown in Section~\ref{sec:3.4.2}, the posterior absorbs the class prevalences…")

**Interfaces:**
- Consumes: `sec:5.4.2` (the primary verbal mechanism, unchanged by Task 2).
- Produces: nothing new that later tasks depend on.

**What and why:** The "posterior absorbs training-set prevalences" mechanism is stated in full in both §5.4.2 (verbal, primary — lines 40–43) and here in §5.4.3. Keep §5.4.2 primary. In §5.4.3: **keep the load-bearing Bayes decomposition** `$p(k|\mathbf{x}) \propto p(\mathbf{x}|k)\,p(k)$` — it is the pivot introducing `$p(\mathbf{x}|k)$`, this subsection's subject — but **strip the re-derivation prose**, and **re-point the back-reference from `sec:3.4.2` to `sec:5.4.2`** so the two §5.4 subsections consolidate instead of both deferring to Chapter 3.

- [ ] **Step 1: Locate the passage**

Anchor: `However, as shown in Section~\ref{sec:3.4.2}, the posterior absorbs the class prevalences of the training set: through Bayes' theorem, $p(k|\mathbf{x}) \propto p(\mathbf{x}|k)\,p(k)$, so any change in the underlying class fractions between the associated and unassociated populations invalidates the classifier's predictions.`

- [ ] **Step 2: Comment the original and insert the replacement**

`%`-comment the original sentence. Directly below, add a shorter `\blue{...}` sentence that (a) back-references `Section~\ref{sec:5.4.2}` (not `sec:3.4.2`), (b) preserves the inline formula `$p(k|\mathbf{x}) \propto p(\mathbf{x}|k)\,p(k)$` verbatim, and (c) drops the "as shown … absorbs the class prevalences of the training set" re-derivation, keeping only the conclusion that the posterior cannot survive a prior shift. Wording is the implementer's.

- [ ] **Step 3: Verify the edit locally**

Run: `grep -n "propto p(\\\\mathbf{x}|k)" chapter_05/sections/5.4_unassociated_sources.tex`
Expected: the Bayes formula still present in the new `\blue{}` line; the new line references `sec:5.4.2`; the original references `sec:3.4.2` and is `%`-commented above.

- [ ] **Step 4: Commit**

```bash
git add chapter_05/sections/5.4_unassociated_sources.tex
git commit -m "Ch5 §5.4.3: strip posterior re-derivation, keep Bayes formula, repoint xref to §5.4.2 (A2)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 4: B4-residual — condense the generative/mixture tail in §5.4.3

**Files:**
- Modify: `chapter_05/sections/5.4_unassociated_sources.tex` (the block of five sentences from "The shift from $p(k|\mathbf{x})$ to $p(\mathbf{x}|k)$ carries a deeper conceptual consequence…" through "…profile likelihood~\cite{Amerio:2025fhz}.")

**Interfaces:**
- Consumes: nothing.
- Produces: nothing new.

**What and why:** This exposition now doubles the still-active paper introduction (`paper_dm_halos/sections/introduction.tex` lines 67–81, which the author deliberately kept). **Condense the five sentences to roughly two**, retaining (a) the one-line mixture formula `$\tilde{p}_\mathrm{unas}(\mathbf{x}) = \sum_k \pi_k\, p(\mathbf{x}|k)$` — the chapter's conceptual crux — and (b) the new-class / free-prevalence argument (core of the quantification pitch), while thinning the generative-vs-discriminative re-explanation and handing off to the paper. This edit also **absorbs A3-occurrence-3** (the "class never observed (dark matter subhalos)" clause). Preserve the existing citation keys `10.1145/3117807_Gonzalez_quantification`, `2024arXiv240100490M`, `Amerio:2025fhz`. Wording is the implementer's.

- [ ] **Step 1: Locate the passage**

Anchor start: `The shift from $p(k|\mathbf{x})$ to $p(\mathbf{x}|k)$ carries a deeper conceptual consequence: the unit of analysis moves from the individual source to the population.`
Anchor end: `…and supports statistically rigorous confidence intervals through the profile likelihood~\cite{Amerio:2025fhz}.`
Do **not** touch the already-`%`-commented block immediately below (the stale earlier draft) — leave it commented.

- [ ] **Step 2: Comment the original and insert the replacement**

`%`-comment all five original sentences (each line prefixed with `%`). Directly below, add the condensed `\blue{...}` replacement (≈2 sentences) that keeps the mixture formula and the free-prevalence/new-class argument, carries the three citation keys, and closes by pointing to the paper that follows. If the replacement is two sentences, keep both inside `\blue{}` only if no paragraph break separates them; otherwise wrap each sentence in its own `\blue{}`.

- [ ] **Step 3: Verify the edit locally**

Run: `grep -n "sum_k \\\\pi_k\|Amerio:2025fhz\|class never observed" chapter_05/sections/5.4_unassociated_sources.tex`
Expected: the mixture formula `\sum_k \pi_k` present in the new `\blue{}` text; `Amerio:2025fhz` retained; the five original sentences (including "class never observed") present but `%`-commented above.

- [ ] **Step 4: Commit**

```bash
git add chapter_05/sections/5.4_unassociated_sources.tex
git commit -m "Ch5 §5.4.3: condense generative/mixture tail, keep crux, defer to paper (B4)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 5: B2 — condense the shared-sigmoid implementation detail in §5.4.3

**Files:**
- Modify: `chapter_05/sections/5.4_unassociated_sources.tex` (the three sentences from "In practice, prior shift and covariate shift…" through "…fitted jointly with the class prevalences.")

**Interfaces:**
- Consumes: `sec:stat-model` (paper body label).
- Produces: nothing new.

**What and why:** The shared-sigmoid covariate-shift *implementation* (`$\tilde{C}(\mathbf{x};\boldsymbol{\theta}_\mathrm{cov})$`, joint fitting) is pure paper-body material (`statistical_analysis.tex` `sec:stat-model`). **Keep the covariate-shift concept** — the bias by which bright, high-latitude sources are easier to associate — but **drop the explicit sigmoid notation**, replacing it with a pointer to `sec:stat-model`. Keep the `Section~\ref{sec:3.4.2}` reference at the start (Chapter 3 recap, legitimate). Do **not** touch the results-preview sentences that follow (lines 78–79: 6%/29%, 7σ/4.5σ) or the hand-off sentence at line 80. Wording is the implementer's.

- [ ] **Step 1: Locate the passage**

Anchor start: `In practice, prior shift and covariate shift between the associated and unassociated populations act simultaneously (Section~\ref{sec:3.4.2}).`
Anchor end: `Accordingly, the sigmoid modulation functions $\tilde{C}(\mathbf{x};\boldsymbol{\theta}_\mathrm{cov})$ that correct for this bias are shared across all astrophysical classes, and their parameters are fitted jointly with the class prevalences.`
Stop before: `The results of the analysis show that prior shift is the dominant effect…` (leave untouched).

- [ ] **Step 2: Comment the original and insert the replacement**

`%`-comment the three original sentences. Directly below, add a `\blue{...}` replacement that keeps `Section~\ref{sec:3.4.2}`, retains the covariate-shift-as-association-bias concept, drops the `$\tilde{C}(\mathbf{x};\boldsymbol{\theta}_\mathrm{cov})$` notation, and points to `Section~\ref{sec:stat-model}` for the implementation.

- [ ] **Step 3: Verify the edit locally**

Run: `grep -n "sec:stat-model\|boldsymbol{\\\\theta}_\\\\mathrm{cov}" chapter_05/sections/5.4_unassociated_sources.tex`
Expected: `\ref{sec:stat-model}` present in the new `\blue{}` line; the `$\tilde{C}(...)$` notation now appears only on the `%`-commented original above; the "results of the analysis show…" sentence is unchanged.

- [ ] **Step 4: Commit**

```bash
git add chapter_05/sections/5.4_unassociated_sources.tex
git commit -m "Ch5 §5.4.3: defer shared-sigmoid implementation to paper sec:stat-model (B2)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 6: Verification — compile, referee, diff review

**Files:**
- No source edits unless a defect is found (then a follow-up fix commit).

**What and why:** Confirm the five edits compile cleanly, read well cold, and obey the editing conventions.

- [ ] **Step 1: Compile check**

Run: `latexmk -pdf -interaction=nonstopmode main.tex` (or the repository's usual build).
Expected: build succeeds; **no new** `LaTeX Warning: Reference ... undefined` for `sec:5.2.2`, `sec:5.4.1`, `sec:5.4.2`, `sec:stat-model`. Check the log:
Run: `grep -i "reference.*undefined\|multiply defined" main.log | grep -i "5.2.2\|5.4.1\|5.4.2\|stat-model"`
Expected: no output.

- [ ] **Step 2: Convention audit on the diff**

Run: `git diff main~5 -- chapter_05/sections/5.3_dm_subhalos_gamma_ray_targets.tex chapter_05/sections/5.4_unassociated_sources.tex`
Confirm by eye: every changed passage has (a) the original `%`-commented, (b) the replacement wrapped in `\blue{}`, (c) no `\blue{}` spanning a paragraph break or containing `%`, (d) all `\aure{}` markers still present.
Run: `grep -c "aure{" chapter_05/sections/5.4_unassociated_sources.tex`
Expected: the count is unchanged from before the edits (the four §5.4 markers survive).

- [ ] **Step 3: Fresh-context referee**

Dispatch a fresh-context subagent (per CLAUDE.md "review in fresh context") to read the revised §5.3 and §5.4 cold and check: (a) each condensed passage still flows and no cross-reference is orphaned; (b) §5.4.3 still reads as self-contained motivation and the mixture crux survives; (c) the hand-off into the paper body still lands; (d) no `\aure{}` marker was dropped. Address any defect it raises with a follow-up `\blue{}`/`%` fix commit.

- [ ] **Step 4: Report**

Summarize to the user: the five edits made, compile status, and the referee verdict.

---

## Notes for the executor

- Tasks 2–5 all edit the same file (`5.4_unassociated_sources.tex`) at non-overlapping locations. Applying them top-to-bottom (Task 2 → 5 is already file order) minimizes confusion; always re-locate by anchor text since line numbers shift.
- If any anchor text is not found verbatim, stop and report — do not guess a nearby passage.
- The stale `%`-commented block at the old lines 71–73 stays commented; do not un-comment or delete it.
