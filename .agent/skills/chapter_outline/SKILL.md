---
name: chapter_outline
description: Research assistant that generates detailed, structural chapter outlines by synthesizing thesis context, local references, and NotebookLM insights.
---

# Thesis Chapter Outlining Skill

This skill guides the creation of deep, structurally robust chapter outlines for a PhD thesis. It combines the high-level goals from the thesis `outline.md` with specific source material from the chapter's `references.md`, using NotebookLM to extract structural insights from key texts.

## Prerequisites
- A target chapter directory (e.g., `chapter_01`).
- A populated `references.md` file in that directory.
- Use `notebooklm-mcp` tools.

## Workflow Steps

### 1. Context Analysis
First, understand where this chapter fits in the larger picture.
- **Read Root Outline**: `view_file outline.md`. Identify the "Scope" and "Key Contribution" of the target chapter.
- **Read Chapter References**: `view_file <chapter_dir>/references.md`. Identify the "Key Specific Papers" and "Reviews/Textbooks" listed.

### 2. Structural Research (NotebookLM)
Use NotebookLM to understand *how* the experts structure these arguments.
- **Identify Key Sources**: Pick 1-2 primary reviews, textbooks, or key papers from `references.md`.
- **Query NotebookLM**:
    - Ask for the table of contents or structural flow of these specific documents.
    - Ask how they introduce concepts, order their arguments, and transition between topics relevant to this chapter.
    - *Prompt Template:* "What is the detailed structure of [Reference X] regarding [Topic]? List the section headers and a brief summary of the argumentation flow. How do they transition from [Concept A] to [Concept B]?"

### 3. Draft `chapter_outline.md`
Create the outline (`<chapter_dir>/chapter_outline.md`).
- **Synthesis**: Combine the specific requirements from `outline.md` with the structural best practices found via NotebookLM.
- **Format**: Use a nested bullet point structure.
    - **H2 Sections**: Main structural divisions (e.g., "Theoretical Basis", "Methodology").
    - **H3 Subsections**: Specific logical steps.
    - **Bullets**: Key points to cover, specific references to cite, and the "Narrative" or "Goal" of the section.
- **Connections**: Explicitly note transitions. How does this chapter end? How does it link to the *next* chapter defined in `outline.md`?

### 4. Review and Refine
Iterate on the draft.
- **Logical Flow**: Does Section A naturally lead to Section B? Are necessary prerequisites defined before they are used?
- **Weakness Check**: Are there "jumps" in logic?
- **Self-Contained vs. Connected**: Ensure the chapter stands on its own but explicitly referencing previous/future chapters where appropriate.

## Output
- A file named `chapter_outline.md` in the chapter directory.
