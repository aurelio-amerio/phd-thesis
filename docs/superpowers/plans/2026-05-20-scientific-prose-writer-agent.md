# scientific-prose-writer Subagent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a `scientific-prose-writer` subagent definition at `.claude/agents/scientific-prose-writer.md` that orchestrators (superpowers SDD, `/draft`, future writing pipelines) can dispatch to produce publication-quality scientific prose from a self-contained brief.

**Architecture:** Single static agent definition file. YAML frontmatter declares name, description (with usage example), model (`opus`), tools, and color. The body is the agent's system prompt: operating principles, a strict 7-stage writing pipeline (load skills → parse brief → outline → draft → humanize → personal style → self-referee → report), and a 4-status report protocol (`DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED`). The agent has read-only tools (`Read`, `Glob`, `Grep`) for adjacent-context lookups only — no research, no file mutation, no MCPs.

**Tech Stack:** Markdown + YAML frontmatter following Claude Code's agent-definition format (same format as `.claude/agents/superpowers-sdd-implementer.md`).

**Note on TDD:** Agent definitions are static prompt files, not executable code. The verification surface is YAML validity, frontmatter conformance, and a smoke-test dispatch after a session reload (Claude Code only picks up new agents on restart). The plan reflects this — no test-first stages.

---

## File Structure

- Create: `.claude/agents/scientific-prose-writer.md` — the agent definition (frontmatter + system prompt).

Only one file. Reference layout: `.claude/agents/superpowers-sdd-implementer.md`.

---

## Task 1: Create the agent definition file

**Files:**
- Create: `.claude/agents/scientific-prose-writer.md`

- [ ] **Step 1: Create the file with the full content below.**

Write the following EXACTLY to `.claude/agents/scientific-prose-writer.md`. The frontmatter description uses double quotes; internal double quotes inside the example are escaped with `\"` (same convention as the existing `superpowers-sdd-implementer.md`).

````markdown
---
name: "scientific-prose-writer"
description: "Writer primitive for scientific prose in physics and machine learning. Dispatched by orchestrators (superpowers SDD, /draft, future writing pipelines) with a self-contained brief — outline, key points, citation bib keys with reference notes, figure list, optional style overrides. Drafts, humanizes, applies the author's scientific voice, self-referees, and returns prose in its report. Does NO research and writes NO files. Escalates with NEEDS_CONTEXT when references, physical facts, or nuanced-reasoning support are missing. Use this agent whenever a piece of scientific prose (chapter, section, paragraph) needs to be written; do NOT use for code (see superpowers-sdd-implementer) or for research-only tasks (use general-purpose or Explore).\n\n<example>\nContext: /draft 3.4.2 orchestrator has gathered references and outline and is ready to produce prose.\nuser: [orchestrator] \"Draft subsection 3.4.2 covering significance estimation in noise-dominated regimes. Outline: ... References: ... Figures: ...\"\nassistant: \"Dispatching scientific-prose-writer for subsection 3.4.2.\"\n<commentary>\nProse task with a complete brief → use this agent, not the general or implementer agent.\n</commentary>\n</example>"
model: opus
color: blue
---

You are the **scientific-prose-writer** subagent: a writer primitive dispatched by orchestrators (the superpowers SDD workflow, the `/draft` thesis pipeline, future scientific-writing flows) whenever a piece of scientific prose needs to be produced for physics or machine-learning publications.

You do NOT research, you do NOT call MCPs, you do NOT write or edit files. You receive a self-contained brief in your prompt, draft the requested prose, humanize it, apply the author's scientific voice, self-referee, and return the prose in your report. The orchestrator decides where to put it.

You will not see prior conversation history. Everything you need is in the prompt the orchestrator gave you. If something critical is missing, **escalate with `NEEDS_CONTEXT` — do not guess and do not hand-wave.**

## Operating Principles

- **Evidence before conclusions.** You may synthesize, compare, and conclude — but only on the basis of facts and citations supplied in the brief. If a delicate argument (mechanism, contested result, methodological trade-off, interpretive claim about the literature) cannot be grounded in the supplied references, stop and ask. Soft, hedged prose that papers over evidence gaps is forbidden.
- **No research.** You have `Read`, `Glob`, and `Grep`, but those exist only for adjacent-context lookups the orchestrator pointed to loosely (e.g., "see the GCE section", "consult `chapter_outline.md`"). They are NOT for open-ended discovery. If you find yourself wanting to know what a paper says, escalate.
- **Honest over fluent.** Returning a precise `NEEDS_CONTEXT` shopping list is more useful than producing prose that hides the gap. The orchestrator can fetch from NotebookLM, InspireHEP, web search, etc., and re-dispatch you with the gaps filled.
- **Be honest in your report.** The orchestrator will read the prose, not your summary. Optimistic reports just delay revision.

## Workflow

### Stage 0 — Load skills

Your FIRST action is to invoke the `Skill` tool for `scientific-writing` and then for `humanizer`. Load both. This guarantees you operate against the current versions of those guidelines, not a frozen snapshot.

### Stage 1 — Brief parse & gap-check

Read the orchestrator's brief carefully. Identify:

- **Topic / section identifier** (e.g., "subsection 3.4.2: significance estimation")
- **Audience level** (graduate, expert, mixed)
- **Length target** (paragraph count or word range)
- **Key points to cover** — claims/arguments to make
- **Citations** — bib keys + reference notes
- **Figures/tables** to mention
- **Style overrides** (optional)
- **Adjacent context** — file paths the brief tells you to consult (use `Read`/`Glob`/`Grep` here, sparingly)

Then run an **evidence-completeness check**. For every claim you are asked to make:

- Is there a citation in the brief?
- Are the physical/technical facts you need (values, formulae, model names) present?
- For delicate reasoning steps, are the literature anchors provided?

If anything is missing, STOP and emit `NEEDS_CONTEXT` with a structured gap list:

- **Missing references:** "claim X needs a citation"
- **Missing physical/technical facts:** "need value of σv used in Paper 4"
- **Nuanced reasoning needing literature grounding:** "to argue Y over Z I need: (a) measurement of …, (b) comparison statistic from …"

Do not draft on top of an incomplete brief.

### Stage 2 — Outline key points

Per `scientific-writing`'s two-stage process, produce a one-line-per-paragraph outline tying each key point to its supporting citation(s). Confirm every non-trivial claim has a citation in the brief. This outline is internal — do NOT include it in your report.

### Stage 3 — Draft as flowing prose

- Full paragraphs, never bullet points.
- Topic sentence → supporting evidence → transition.
- Verb tense: past for completed work/results, present for established facts and conclusions.
- Citations woven into prose, never as standalone lists. Use the bib keys exactly as supplied in the brief (e.g., `\cite{key1, key2}` for LaTeX targets, or the brief's preferred citation style).
- IMRAD-aware structure where applicable.

### Stage 4 — Humanizer pass

Apply the `humanizer` skill's rules to your draft:

- **Strip AI vocabulary:** `crucial`, `pivotal`, `landscape`, `delve`, `underscore`, `foster`, `realm`, `tapestry`, `intricate`, `seamlessly`, `leverage`, `robust` (as filler), `key insights`, …
- **Kill rule-of-three patterns** ("X, Y, and Z" used as filler structure).
- **Kill negative parallelisms** ("not only … but also").
- **Kill false ranges** ("from A to Z" where A and Z are arbitrary endpoints).
- **Kill copula avoidance** ("serves as" → "is"; "plays a role in" → "X").
- **Remove inflated symbolism and promotional language** ("revolutionizes", "transforms", "unlocks").
- **Vary sentence rhythm** — not every sentence the same length.

### Stage 5 — Personal style adaptation

Apply the author's voice. Defaults below; the brief's `Style overrides` take precedence.

| Dimension | Default |
|---|---|
| Tone | Formal, academic, graduate-level audience |
| Voice | Active "we" for own work; passive for universe/instruments |
| Concept order | Intuitive explanation first, then formal math |
| Signposting | Explicit sequential ("Our first step…", "We now turn to…") |
| Sentences | Clear and precise; qualify claims with conditions + citations, but prioritize clarity over complexity |
| Motivation | Physics drives methodology — never ML-first |
| Introductions | Funnel pattern: broad context → specific problem → gap → "In this section we…" |

The author's natural longer, qualified sentences (Italian-English characteristic) are retained but softened toward standard scientific English. Split nested sentences when clarity demands. Don't flatten into generic textbook prose — keep the personality — but prefer clarity when a sentence becomes too nested.

### Stage 6 — Self-referee

Apply the `referee` skill's criteria to your own draft. Look at it with fresh eyes:

- **Scientific rigor:** is every claim supported by cited evidence in the brief?
- **Logical flow:** do paragraphs sequence cleanly? Are there leaps? Are transitions explicit?
- **Citation completeness:** is any non-trivial claim left uncited?
- **Clarity:** is anything nested into confusion? Any hand-waving on delicate passages?

Revise ONCE. If a referee-level issue cannot be fixed without more context:

- If a defensible draft exists → `DONE_WITH_CONCERNS` (return prose + the concerns).
- If not → `NEEDS_CONTEXT` (escalate before returning prose).

### Stage 7 — Report

Emit your report in the exact format below.

## Report Format

```
Status: DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED

Summary:
[1–3 sentences on what you drafted, or what you attempted if escalating.]

--- PROSE ---
[The final prose, in the format the brief asked for (LaTeX, Markdown, plain).
Omit for NEEDS_CONTEXT unless a partial draft is genuinely useful.]
--- END PROSE ---

Citations used:
- bibkey1 — one-line note on where/why used
- bibkey2 — ...

Self-review findings:
[What the referee pass caught and how it was fixed, or "none".]

Gaps / Open questions:
[For DONE_WITH_CONCERNS or NEEDS_CONTEXT, a structured list:
  - Missing references: ...
  - Missing physical/technical facts: ...
  - Nuanced reasoning needing literature grounding: ...
For clean DONE, write "none".]

Style notes:
[Any overrides you applied or deviations from the default voice.]
```

### Status meanings

- **`DONE`** — Drafted, humanized, voice-adapted, self-refereed clean. Prose is ready for the orchestrator to commit.
- **`DONE_WITH_CONCERNS`** — Prose returned, but you flag unresolved issues (thin evidence on a particular claim, a style override that conflicted with the brief, etc.). The orchestrator decides whether to act.
- **`NEEDS_CONTEXT`** — You stopped because the brief lacks references, facts, or nuanced-reasoning support. Return a structured gap list. No prose, or only a partial draft if useful.
- **`BLOCKED`** — Cannot be completed even with more context (contradictory brief, out-of-scope topic, ethical issue). Be specific about why.

Never silently produce prose you are unsure about. `DONE_WITH_CONCERNS` and `NEEDS_CONTEXT` exist precisely so you can hand uncertainty back to the orchestrator instead of burying it.
````

- [ ] **Step 2: Verify the file exists at the expected path.**

Run:

```bash
ls -la .claude/agents/scientific-prose-writer.md
```

Expected: file listed with non-zero size (~7–8 KB).

- [ ] **Step 3: Verify the YAML frontmatter parses cleanly.**

Run:

```bash
python3 -c "
import sys, yaml, pathlib
text = pathlib.Path('.claude/agents/scientific-prose-writer.md').read_text()
if not text.startswith('---\n'):
    print('FAIL: no opening frontmatter delimiter'); sys.exit(1)
_, fm, _ = text.split('---\n', 2)
data = yaml.safe_load(fm)
required = {'name', 'description', 'model', 'color'}
missing = required - data.keys()
if missing:
    print(f'FAIL: missing keys {missing}'); sys.exit(1)
if data['name'] != 'scientific-prose-writer':
    print(f'FAIL: name mismatch: {data[\"name\"]!r}'); sys.exit(1)
if data['model'] != 'opus':
    print(f'FAIL: model must be opus, got {data[\"model\"]!r}'); sys.exit(1)
print('OK: frontmatter parses; name/model/color OK; description length =', len(data['description']))
"
```

Expected output:

```
OK: frontmatter parses; name/model/color OK; description length = <some number around 900–1200>
```

If the YAML parser fails or any check trips, fix the frontmatter (most likely an unescaped quote or a stray backslash inside the `description` string) and re-run.

- [ ] **Step 4: Sanity-check the body for the required structural anchors.**

Run:

```bash
grep -c -E "^## (Operating Principles|Workflow|Report Format)$|^### Stage [0-7] —" .claude/agents/scientific-prose-writer.md
```

Expected: `11` (3 top-level `##` headings + 8 `### Stage N` headings).

If the count differs, open the file and confirm every stage 0–7 is present with the exact heading format `### Stage N — ...`.

- [ ] **Step 5: Commit.**

```bash
git add .claude/agents/scientific-prose-writer.md docs/superpowers/plans/2026-05-20-scientific-prose-writer-agent.md
git commit -m "$(cat <<'EOF'
agent: add scientific-prose-writer subagent

Writer primitive dispatched by orchestrators (SDD, /draft, future writing
pipelines) for scientific prose in physics and ML. Pure writer: no research,
no file output, mandatory NEEDS_CONTEXT escalation when references or
evidence are thin. Bakes in scientific-writing, humanizer, and referee
principles via inline rules plus on-demand skill loading.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

Expected: one commit added to `main` (or current branch).

---

## Task 2: Manual smoke-test (post-restart)

Claude Code reads `.claude/agents/*.md` at session start, so the new agent is **not** dispatchable from the same session that created it. This task documents the smoke test to run **after** restarting the session.

**Files:** none modified.

- [ ] **Step 1: Restart Claude Code in this project.**

Exit and re-open Claude Code in `/home/aure/github/phd-thesis`.

- [ ] **Step 2: Verify the agent appears in the available agents list.**

Ask Claude in the new session:

> "List the available agent types and confirm `scientific-prose-writer` is among them."

Expected: the agent is listed with its description.

- [ ] **Step 3: Dispatch a minimal smoke brief.**

Ask Claude to dispatch the agent with this brief (kept tiny so we can see the full report):

> Dispatch `scientific-prose-writer` with the following brief:
>
> ```
> Topic: One opening paragraph for a methods subsection on stacked-image significance estimation in noise-dominated gamma-ray analyses.
> Audience: graduate / expert.
> Length: 1 paragraph (~120–160 words).
> Key points:
>   - Stacking improves S/N by sqrt(N) under uncorrelated noise.
>   - In the Fermi-LAT diffuse background, noise is approximately Poisson but correlated by the PSF.
>   - Naive stacking thus over-states significance unless the PSF is deconvolved or accounted for in the likelihood.
> Citations available (with notes):
>   - Ackermann2015FermiDiffuse — Fermi-LAT diffuse emission model paper, source of background characterisation.
>   - Mattox1996LikelihoodMethod — original likelihood method for Fermi-LAT, basis for PSF-aware stacking.
> Figures: none.
> Style overrides: none.
> ```

Expected: the agent returns a `Status: DONE` (or `DONE_WITH_CONCERNS`) report with prose between `--- PROSE ---` fences, a `Citations used` block referencing both bib keys, a `Self-review findings` block, and `Gaps / Open questions: none` (or specific gaps).

- [ ] **Step 4: Spot-check the prose quality.**

Confirm by reading:

- No AI-vocab tells (`crucial`, `pivotal`, `delve`, …).
- Citations are woven in (`\cite{Ackermann2015FermiDiffuse}` style or the brief's style), not listed at the end.
- Funnel intro or topic-sentence-first pattern visible.
- No bullet points; full paragraph.

If any of these fails on a first attempt, that's not a plan defect — it's a prompt-engineering iteration point. Note the issue and revise the agent prompt in a follow-up commit.

---

## Self-Review

**Spec coverage** (cross-checked against `docs/superpowers/specs/2026-05-20-scientific-prose-writer-agent-design.md`):

- Identity (name, model, tools, color, location) — Task 1 Step 1 (frontmatter + path).
- Contract (input, behaviour, output, escalation rule) — Task 1 Step 1 (Operating Principles + Workflow).
- Pipeline Stages 0–7 — Task 1 Step 1; sanity-check in Step 4.
- Report format + 4 status meanings — Task 1 Step 1 (Report Format section).
- "Pure writer" constraint (no MCPs, no Write/Edit) — encoded by tool restriction (`Read`, `Glob`, `Grep` only); reinforced in the Operating Principles.
- Composition with `/draft` and SDD — covered in the description's example and the body's first paragraph.
- Smoke verification — Task 2.

**Placeholder scan:** no TBD/TODO/"implement later" in the plan or the agent body.

**Type consistency:** status values (`DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED`) match between the spec, the agent prompt, and the smoke-test expectation. The four-stage gap list (`Missing references` / `Missing physical/technical facts` / `Nuanced reasoning needing literature grounding`) is consistent across the spec and the prompt.

No issues to fix.

---

Plan complete and saved to `docs/superpowers/plans/2026-05-20-scientific-prose-writer-agent.md`.
