---
name: fixref
description: Use when you need to resolve placeholder citations (e.g., surname_year) or missing bibliography entries in the LaTeX thesis by querying NotebookLM context and InspireHEP.
---

# Fix Reference (fixref) Workflow

## Overview
A systematic workflow to resolve placeholder citations in LaTeX documents, retrieve the correct paper metadata using context-aware NotebookLM queries, fetch standard BibTeX via InspireHEP, and integrate them safely into the main bibliography without creating duplicates.

## When to Use
- When encountering placeholder `\cite{surname_year}` keys in thesis chapters.
- When expanding or verifying the bibliography for specific sections.
- Callable explicitly via `/fixref [section]`.

## Discovery & Execution Pipeline

The workflow proceeds in 5 distinct phases:

### Phase 1: Identification & Preparation
1. Call `source_registry` to ensure notebook sources are loaded if needed.
2. Read the target `.tex` document (e.g., `chapter_02/sections/2.1...tex`) and isolate all missing or placeholder citations. Look closely for patterns like `\cite{Surname_Year}`.
3. Check the central `bibliography.bib` file to see if those exact placeholder keys somehow already exist, or to map existing valid citations.

### Phase 2: NotebookLM Contextual Resolution
For citations not found directly in the bib file:
1. Extract the paragraph of text surrounding the placeholder citation.
2. Query NotebookLM (id: `1b7df790-7858-4fc8-879c-39f41238c4ae`) with the context paragraph and the placeholder name.
3. *Prompt Structure:* "Based on the thesis sources in this notebook, identify the correct paper for the placeholder citation `Surname_Year`. Here is the context: '[Context]'. Provide the full title, authors, and Notebook ID/bib-key if available."

### Phase 3: Duplication Check
1. Take the full paper title returned by NotebookLM.
2. Run a `Select-String` or `grep` search on `bibliography.bib` using exact Title/Author keywords to ensure the paper isn't already present under a *different* bib-key (e.g., `Smith:2020` vs `Smith_2020`).
3. If it exists, note the existing valid bib-key.

### Phase 4: External BibTeX Fetching
For papers confirmed totally missing:
1. (Optional) If NotebookLM didn't provide standard identifiers (arXiv ID, DOI, Inspire ID), do a quick web search to find them using the title and authors.
2. Use the `inspirehep` MCP server (`mcp_inspirehep_get_bibtex`) with the identified arXiv ID or DOI to fetch the perfectly formatted `inspirehep` standard BibTeX.
3. Note the standard `texkey` provided by InspireHEP (e.g., `Kafexhiu:2014cua`).

### Phase 5: Implementation & Verification
1. Append the newly retrieved BibTeX blocks to the bottom of `bibliography.bib`.
2. Clean up any obvious duplicate entries discovered during Phase 3.
3. Update the `.tex` file, systematically replacing the placeholder keys with the standard `texkey`s (both newly retrieved ones and pre-existing validated ones).
4. Run a final uniqueness check (e.g., PowerShell `Select-String`) on the `.tex` file's `\cite{}` commands to confirm every single key now exists in `bibliography.bib`.

## Common Mistakes
- **Skipping Title Search**: Fetching BibTeX directly from InspireHEP and injecting it before checking `bibliography.bib` by *title*. This inherently creates silent duplicate entries with differing keys. Always do Phase 3.
- **Wrong NotebookLM Context**: Asking NotebookLM blindly for "Smith 2018" without providing the LaTeX paragraph. "Smith 2018" could be any of 50 papers; the context defines *which* mechanism/result is being cited.
- **Orphan LaTeX Edits**: Updating the `bibliography.bib` but forgetting to map the new key directly back into the `.tex` file.

## Quick Reference Commands

**List all citations in a tex file:**
Use the built-in `grep_search` tool with a regular expression on the target `.tex` file:
```json
{
  "SearchPath": "/path/to/target/section.tex",
  "Query": "\\\\cite\\{([^}]+)\\}",
  "IsRegex": true
}
```

**Find a paper by title in bibliography:**
Use the built-in `grep_search` tool on the central `bibliography.bib` file:
```json
{
  "SearchPath": "/path/to/bibliography.bib",
  "Query": "Unique words from title",
  "IsRegex": false,
  "CaseInsensitive": true
}
```
