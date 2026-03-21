---
name: review
description: Critical review of thesis sections or chapters. Evaluates scientific rigor, writing quality, logical flow, and citation completeness. Supports section-level (/review X.Y) and chapter-level (/review X) scope.
---

# Thesis Review Skill

Provides structured critical review of thesis prose at two granularities: **section-level** (quick targeted feedback after drafting) and **chapter-level** (comprehensive review after all sections are assembled).

## When to Use

- After `/draft X.Y` completes — get a second opinion on a section
- After all sections of a chapter are drafted — review the full chapter
- When revising prose based on supervisor feedback
- Before finalizing a chapter for submission

## Scope Modes

### Section Review (`/review X.Y`)

Targeted review of a single section (e.g., Section 1.2 with all its subsubsections). Fast, focused on scientific content and writing quality within that section.

**Input**: The section draft file(s) in `chapter_XX/sections/`
**Context**: `chapter_outline.md`, `references.md`, adjacent section drafts (for transitions)

### Chapter Review (`/review X`)

Comprehensive review of an entire chapter. Checks everything a section review does, plus narrative arc, inter-section coherence, and chapter-level argument structure.

**Input**: All section files in `chapter_XX/sections/`
**Context**: `outline.md`, `chapter_outline.md`, `references.md`

## Review Dimensions

The review evaluates five dimensions, drawing from `scientific-critical-thinking` and `scientific-writing` principles.

### 1. Scientific Rigor (from `scientific-critical-thinking`)

- **Claim evaluation**: Does evidence support each claim? Are claims appropriately hedged?
- **Logical flow**: Are there logical jumps, non-sequiturs, or circular reasoning?
- **Fallacy detection**: Check for common scientific fallacies — correlation/causation confusion, hasty generalizations, appeal to authority without evidence
- **Proportionality**: Is confidence proportional to evidence strength? Are speculations labeled as such?
- **Completeness**: Are important caveats, alternative explanations, or conflicting results acknowledged?

### 2. Citation Quality

- **Coverage**: Is every factual claim backed by at least one citation?
- **Specificity**: Are citations to the right papers? (Not just "a review says X" but the original source)
- **Recency**: Are recent key results cited, or is the section relying on outdated references?
- **Balance**: Are opposing viewpoints and alternative interpretations represented?
- **Provenance**: Cross-check against `references.md` — are the cited bib keys consistent with the reference data table?

### 3. Writing Quality (from `scientific-writing`)

- **Clarity**: Is the prose clear and unambiguous? Are technical terms defined at first use?
- **Conciseness**: Are there redundant phrases, unnecessary qualifiers, or inflated language?
- **Precision**: Are quantities reported with appropriate precision? Are vague terms avoided?
- **Flow**: Do paragraphs follow topic sentence → supporting evidence → transition?
- **Tense consistency**: Past for completed work/results, present for established facts
- **Anti-AI patterns**: Check against `humanizer` anti-patterns — rule-of-three, "crucial/pivotal/landscape", copula avoidance, significance inflation

### 4. Structure & Transitions

- **Internal coherence**: Does the section build a clear argument from start to finish?
- **Transitions**: Are connections between subsubsections explicit and logical?
- **Section-to-section flow** (chapter review only): Does Section X.1 naturally lead to X.2?
- **Chapter arc** (chapter review only): Does the chapter tell a coherent story matching the outline?
- **Funnel structure**: Does the introduction follow the broad → specific → gap → "we will" pattern?

### 5. Thesis Integration

- **Outline alignment**: Does the content match what `chapter_outline.md` specified?
- **Cross-references**: Are forward/backward references to other chapters appropriate?
- **Paper setup** (if applicable): Does the chapter properly motivate the inserted paper?
- **Terminology consistency**: Are terms used consistently with earlier/later chapters?

## Workflow Steps

### Step 1: Load Context

1. Read `outline.md` — thesis arc, chapter connections
2. Read `chapter_outline.md` — what each section should cover
3. Read `references.md` — expected references and their provenance
4. Read the target draft file(s) in `chapter_XX/sections/`
5. For chapter review: read ALL section files in sequence

### Step 2: Dimension-by-Dimension Review

For each of the 5 dimensions, produce specific findings:

- **Quote** the problematic text (with section/paragraph reference)
- **Classify** the issue severity:
  - 🔴 **Critical** — scientific error, unsupported claim, or logical flaw
  - 🟡 **Important** — affects quality but not correctness (awkward writing, missing citation, unclear explanation)
  - 🟢 **Minor** — polish-level (word choice, sentence rhythm, formatting)
- **Explain** why it's an issue
- **Suggest** a specific fix or revision

### Step 3: Produce Review Report

Output a structured review report saved to the chapter directory.

**Section review**: `chapter_XX/sections/X.Y_review.md`
**Chapter review**: `chapter_XX/chapter_review.md`

```markdown
# Review Report: [Section X.Y / Chapter X]

## Summary
[2-3 sentence overview of the section/chapter quality]

## Verdict
[Ready / Needs revision / Major gaps]

## Issue Summary
- 🔴 Critical: [count]
- 🟡 Important: [count]
- 🟢 Minor: [count]

## Strengths
- [What works well — be specific]

## Critical Issues (🔴)
### Issue 1: [Title]
- **Location**: Section X.Y.Z, paragraph N
- **Quote**: "[problematic text]"
- **Problem**: [explanation]
- **Suggested fix**: [specific revision]

## Important Issues (🟡)
### Issue N: [Title]
...

## Minor Issues (🟢)
### Issue N: [Title]
...

## Dimension Scores

| Dimension | Score (1-5) | Notes |
|---|---|---|
| Scientific Rigor | | |
| Citation Quality | | |
| Writing Quality | | |
| Structure & Transitions | | |
| Thesis Integration | | |

## Recommendations
[Prioritized list of what to address first]
```

### Step 4: Present to User

1. Present the review report
2. Highlight the most critical issues
3. Offer to help fix specific issues (e.g., "want me to revise Section X.Y.Z to address issue #3?")

## Integration with Drafting Pipeline

The review skill is designed to slot in **after** `/draft X.Y` completes:

```
/chapter N  →  references.md + chapter_outline.md
/draft X.Y  →  section prose (with self-quality gates)
/review X.Y →  critical review of the section  ← THIS SKILL
iterate on fixes
/review X   →  chapter-level review after all sections done
```

The self-review in `section_drafting` Step 7 is a quick internal gate. This `/review` skill is a deeper, more thorough second pass from a referee perspective.
