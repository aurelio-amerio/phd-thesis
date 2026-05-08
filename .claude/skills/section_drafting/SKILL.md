---
name: section_drafting
description: Use when writing actual thesis prose for a specific section or subsection. Orchestrates research, drafting with scientific-writing principles, humanization, and personal style adaptation. Callable via /draft X.Y or /draft X.Y.Z.
---

# Thesis Section Drafting

Writes thesis prose for a specific section (X.Y) or subsubsection (X.Y.Z). Orchestrates NotebookLM research, drafting, and iterative refinement through a three-layer writing pipeline.

## Target Notebook

- **Name**: `thesis references`
- **ID**: `1b7df790-7858-4fc8-879c-39f41238c4ae`

## Prerequisites

- A target chapter directory (e.g., `chapter_01`) with `chapter_outline.md` and `references.md` already produced
- `outline.md` (root thesis outline)
- The `source_registry` skill must be called once per conversation before this skill

## Writing Pipeline (Three Layers)

All prose passes through three layers in sequence:

### Layer 1: `scientific-writing` (Primary Driver)

- **Two-stage process**: outline key points from research → convert to flowing paragraphs
- **Paragraph coherence**: topic sentence → supporting evidence → transition
- **Verb tense**: past for completed work/results, present for established facts and conclusions
- **Conciseness and precision**: apply principles from `writing_principles.md`
- **Citation integration**: weave `\cite{}` naturally into prose, never as standalone lists

### Layer 2: `humanizer` (Anti-AI Pass)

After the initial draft, check against the `humanizer` skill's anti-patterns:
- Strip AI vocabulary ("crucial", "pivotal", "landscape", "delve", "underscore", "foster")
- Remove rule-of-three patterns, negative parallelisms ("not only…but"), false ranges
- Kill copula avoidance ("serves as" → "is")
- Remove significance inflation and promotional language
- Ensure varied sentence rhythm — not all sentences the same length

### Layer 3: Personal Style Adaptation

Apply the author's voice while prioritizing clarity:

| Dimension | Style |
|---|---|
| **Tone** | Formal, academic, graduate-level assumed |
| **Voice** | Active "we" for own work; passive for universe/instruments |
| **Concepts** | Intuitive explanation first, then formal math |
| **Transitions** | Explicit sequential signposting ("Our first step…", "We now turn to…") |
| **Sentences** | Clear and precise. Qualify claims with conditions + citations, but **prioritize clarity over complexity** |
| **Motivation** | Physics always drives methodology — never ML-first |
| **Introductions** | "Funnel": broad context → specific problem → gap → "In this chapter we…" |

**Style balance**: The author writes naturally with longer, qualified sentences (Italian-English characteristic). **Retain this personal voice** but **soften toward standard scientific English**. Don't flatten into generic textbook prose — keep the personality — but prefer clarity when a sentence becomes too nested. Split complex sentences when it improves readability without losing voice.

**Per-chapter overrides**: If `chapter_outline.md` contains a `## Style Notes` section, apply those overrides (e.g., "more pedagogical for this chapter", "assume less background"). During iteration, record any user style corrections for future sections.

### Related Skills (Awareness)

Know these exist and reference if the situation calls for it:

| Skill | When it might help |
|---|---|
| `review` | Automatically invoked in Step 9 for a critical review pass; can also be called manually via `/referee X.Y` |
| `scientific-brainstorming` | Section outline feels thin or poorly motivated |
| `scientific-critical-thinking` | Evaluating conflicting evidence in the literature |
| `scientific-visualization` | Data plots or diagrams would strengthen the section |
| `scientific-schematics` | Concept diagrams or flowcharts |

## Section Granularity

### `/draft X introduction` — Chapter Introduction

Draft the untitled opening paragraphs of Chapter X (the "Section X.0" from the chapter outline). This is **not** a subsection intro — it covers the entire chapter at a high level.

- **Length**: 2–4 paragraphs.
- **Structure**: Funnel pattern from the Personal Style profile: broad context → specific problem → gap → "In this chapter we…" roadmap.
- **Input**: Reads the **full** `chapter_outline.md` (all sections) plus `outline.md` (thesis arc) to understand the chapter's scope and connections.
- **No subsubsection research**: Unlike `/draft X.Y`, this mode does not drill into individual reference queries. It synthesises the chapter's Goal, Narrative, and Connections blocks into flowing prose.
- **Output**: Saved to `chapter_XX/sections/X.0_introduction.md`.

### `/draft X.Y` — Subsection Level

**Ask the user** which mode:

**1. Intro-only mode**: Draft just the introductory text of Section X.Y — the prose that appears before the first subsubsection (X.Y.1). Use when subsubsections will be drafted separately.

**2. Full-section mode**: Draft the entire Section X.Y including all subsubsections **autonomously with self-quality gates**:

<HARD-GATE>
Do NOT begin researching, drafting, or working on subsubsection X.Y.(Z+1) until subsubsection X.Y.Z has been fully drafted, saved to file, and passed the self-review quality gate (Step 7). No parallel drafting of multiple subsubsections. No skipping the self-review.

Announce after each subsubsection: "Self-review GATE for X.Y.Z: I will not begin X.Y.(Z+1) until I have critically reviewed X.Y.Z, identified weaknesses, and revised them."

A gate violation is: starting research for the next subsubsection before the current one is saved and self-reviewed, drafting prose for multiple subsubsections in one pass, or skipping the self-criticism step.
</HARD-GATE>

The full flow is:
```
for Z in [1, 2, …, last subsubsection]:
    Step 4  → Reference-guided research for X.Y.Z
    Step 5  → Figure discovery for X.Y.Z
    Step 6  → Draft writing (three-layer pipeline)
    Step 7  → Self-review & self-criticism (MANDATORY — revise before proceeding)
    Save revised draft to file
    ── SELF-QUALITY GATE: announce gate, confirm quality, then proceed ──

# After all subsubsections pass their self-quality gates:
Write section introduction (text before X.Y.1)
Verify inter-subsubsection transitions
Step 8  → Coherence check on the assembled section (fix issues)
Step 9  → Review pass: run the review skill, apply fixes
Step 10 → Present the revised section to the user
```

### `/draft X.Y.Z` — Subsubsection Level

Draft a single subsubsection. Before writing, **read existing context**:
- **Subsection intro** (X.Y text, if present) — understand the framing
- **Previous subsubsections** (X.Y.1 … X.Y.(Z-1)) — ensure continuity
- **Next subsubsection outline** (X.Y.(Z+1) from `chapter_outline.md`) — set up proper transitions

## Workflow Steps

### Step 0: Parse Input & Determine Mode

1. Parse the user's `/draft` command:
   - `X introduction` → chapter introduction mode
   - `X.Y` → subsection mode
   - `X.Y.Z` → subsubsection mode
2. Map chapter `X` → directory `chapter_0X/`
3. Locate the target in `chapter_outline.md`
4. If **chapter introduction** (`X introduction`): proceed to draft the X.0 block — read the full chapter outline and thesis connections, skip per-subsection research
5. If **subsection** (`X.Y`): ask user for **intro-only** or **full-section** mode
6. If **subsubsection** (`X.Y.Z`): proceed directly

### Step 1: Context Loading

1. **Read `outline.md`** — thesis arc, how this chapter connects to predecessors and successors
2. **Read `chapter_outline.md`** — section's **Goal**, **Narrative**, key points, transitions, style notes
3. **Read `references.md`** — key references with provenance (✅ directly queryable vs ❌ cited-within-review)
4. **Read existing drafts** in `chapter_XX/sections/`:
   - Subsection intro text (if drafting a subsubsection)
   - Previous subsubsections (for continuity)
   - Next subsubsection outline (for transitions)

### Step 2: Source Registry

```
→ Call source_registry skill
→ Obtain: author_paper_ids (001), review_ids (002), general_ids
```

### Step 3: Knowledge Retrieval

```
→ Call knowledge skill (retrieve mode)
→ Input: section topic keywords
→ Output: existing insights that can skip or accelerate research
```

### Step 4: Reference-Guided NotebookLM Research

Research is guided by `references.md` — the literature groundwork done during `/chapter N`. Start with the sources already identified as relevant to this section, then broaden.

1. **Parse `references.md` for this section**: Read Section 3 ("References Breakdown by Section") to find the key sources listed for this specific section (X.Y or X.Y.Z). From the Reference Data Table (Section 4), extract ✅ Direct Sources (individually queryable in NotebookLM) and ❌ Referenced Sources (cited within reviews — note which review(s) to query from the "Cited In" column). Build a prioritized query plan: these sources are queried **first**.

2. **Priority queries — section-specific sources**:
   ```
   # For ✅ Direct Sources: query them directly
   mcp_notebooklm_notebook_query(
       notebook_id="1b7df790-7858-4fc8-879c-39f41238c4ae",
       query="<specific question about a key point in section X.Y>",
       source_ids=<direct_source_ids_from_references_md>
   )

   # For ❌ Referenced Sources: query the review(s) that cite them
   mcp_notebooklm_notebook_query(
       notebook_id="1b7df790-7858-4fc8-879c-39f41238c4ae",
       query="What does this review say about [Referenced Paper] regarding [topic]?",
       source_ids=<citing_review_source_ids>
   )
   ```

3. **Broadening queries — fill gaps**: After priority queries, identify any key points from the outline that still lack sufficient detail. For these gaps:
   - **Reviews** (`002)` source IDs): consensus definitions, equations, structural context
   - **All sources** (omit `source_ids`): specific citations, numbers, arXiv IDs

4. **Author papers** (if applicable): Only if this section references the author's own work (`001)` source IDs).

5. **Track provenance**: For each claim, record which source backs it → `\cite{bib_key}`. Prefer bib keys already in `references.md` over new ones.

### Step 5: Figure Discovery

Before drafting, identify and download figures from the literature that would strengthen this section.

1. **Query NotebookLM** for figure recommendations:
   ```
   mcp_notebooklm_notebook_query(
       notebook_id="1b7df790-7858-4fc8-879c-39f41238c4ae",
       query="For the topics covered in section [X.Y] about [topic],
              which published figures are commonly used to illustrate
              these concepts? For each, provide the paper's arXiv ID,
              figure number, and a brief description.",
       source_ids=<review_002_ids>
   )
   ```

2. **Cross-reference** with `references.md` Figure Candidates Table (if `literature_research` Phase 3 was run for this chapter) — merge any pre-identified candidates.

3. **Attempt download** for each candidate figure:
   ```python
   # Get figure URLs from InspireHEP
   mcp_inspirehep_get_paper_figures(arxiv_id="https://arxiv.org/abs/<ID>")

   # Match the target figure number from the returned list

   # Download to chapter directory
   # run_command: curl -L -o "chapter_XX/figures/<bib_key>_figN.png" "<figure_url>"
   ```
   See `paper_lookup` Recipe 3 for full details.

4. **Handle failures**: If the figure is not indexed on InspireHEP, record it for a `% TODO` placeholder in the draft (see Step 6 fallback below).

### Step 6: Draft Writing (Three-Layer Pipeline)

1. **Layer 1** (`scientific-writing`): Outline key points from Step 4 research, then convert to flowing paragraphs
2. **Layer 2** (`humanizer`): Anti-AI pass — strip patterns, vary rhythm
3. **Layer 3** (personal style): Apply voice, physics-first motivation, clarity check — break overlong sentences

**Output format** (LaTeX-ready markdown):
- Equations: `$$` for display, `$` for inline
- Citations: `\cite{bib_key}`
- Cross-references: `\label{sec:X.Y.Z}`, `\ref{sec:...}`
- No bullet points in final prose — everything in flowing paragraphs

**Literature figures**: Insert figures identified in Step 5. For each successfully downloaded figure, use:

```latex
\begin{figure}[t]
    \centering
    \includegraphics[width=\columnwidth]{figures/<bib_key>_figN.png}
    \caption{<Description of what the figure shows>, from \cite{<bib_key>}, Figure~N.}
    \label{fig:<descriptive_label>}
\end{figure}
```

If a figure was **not available** on InspireHEP (Step 5 failure), insert a placeholder with a `% TODO` comment:

```latex
\begin{figure}[t]
    \centering
    % TODO: insert Figure 3 from arXiv:2302.01947 (Amerio et al., 2023)
    \includegraphics[width=\columnwidth]{figures/placeholder.pdf}
    \caption{Reconstructed source-count distribution from \cite{Amerio:2023uet}, Figure~3.}
    \label{fig:dnds_result}
\end{figure}
```

The `% TODO` comment must include: (1) the figure number, (2) the arXiv ID or DOI, and (3) the author/year for easy lookup. The user will replace the placeholder with the actual figure file.

### Step 7: Self-Review & Quality Gate (per subsubsection)

This step runs **after every subsubsection draft** and is the quality gate that must pass before proceeding.

<HARD-GATE>
Do NOT proceed to the next subsubsection until this self-review is complete and any identified issues have been revised in the draft.

Announce: "Self-review GATE for X.Y.Z: I will not begin X.Y.(Z+1) until I have critically reviewed X.Y.Z, identified weaknesses, and revised them."

A gate violation is: moving to the next subsubsection with known unresolved issues, skipping any of the 6 review checks below, or failing to revise after identifying problems.
</HARD-GATE>

Perform the following checks and **revise the draft** to fix any issues found:

1. **Logical flow** — does the argument build naturally? Are there logical jumps?
2. **Citation completeness** — is every factual claim backed by a citation?
3. **Style compliance** — matches personal profile + any chapter-level overrides?
4. **Transition quality** — smooth connections to previous subsubsection (if any) and setup for the next?
5. **Anti-AI check** — no remaining AI vocabulary or structural tells?
6. **Self-criticism** — actively look for weaknesses: vague claims, unsupported assertions, unclear explanations, missing context. List specific problems found and how they were addressed.

After revisions, save the updated draft to `chapter_XX/sections/X.Y.Z_title.md` and proceed to the next subsubsection.

### Step 8: Coherence Check (once, after all subsubsections)

Run this step **only after all subsubsections have passed their self-quality gates**:

**1. Chapter-level coherence**:
- Does the new text fit with existing chapter prose?
- Are transitions to/from adjacent sections smooth?
- Is terminology consistent with earlier sections?

**2. Document-level coherence**:
- Does the text align with the thesis narrative arc from `outline.md`?
- Are forward/backward references to other chapters appropriate?
- Does it maintain the framing established in the Introduction (Ch. 0)?

Fix any issues found, then proceed to Step 9.

### Step 9: Review Pass

After coherence check passes, invoke the `referee` skill using the Skill tool **automatically** on the assembled section:

1. Execute the review skill in **section review mode** (`/referee X.Y`)
2. Produce the review report with issues classified as 🔴 Critical / 🟡 Important / 🟢 Minor
3. **Apply fixes** for all 🔴 Critical and 🟡 Important issues identified
4. For 🟢 Minor issues, apply fixes where straightforward; leave the rest as notes for the user
5. Save the revised drafts to `chapter_XX/sections/`
6. Save the review report to `chapter_XX/sections/X.Y_review.md` for the user's reference

This review pass is automatic — the agent does not wait for user input. It serves as a final quality filter before presenting to the user.

### Step 10: Present to User

This step runs **once**, after the review pass is complete.

1. Present the **complete revised section** (all subsubsections + section introduction) to the user
2. Summarize the review findings: how many issues were found and fixed
3. Highlight any 🟢 Minor issues left unresolved for the user's judgment
4. Iterate on user feedback (tone, content, structure, corrections)
5. When user is satisfied → **ask** if they want LaTeX conversion
6. If yes → produce `.tex` snippet ready for `\input{}` in `chapter_X.tex`

## Output

- `chapter_XX/sections/X.Y.Z_title.md` — draft in LaTeX-ready markdown
- `chapter_XX/sections/X.Y.Z_title.tex` — LaTeX conversion (only when requested)
- `.agent/knowledge/` — key insights saved via the `knowledge` skill (if new research was performed)
