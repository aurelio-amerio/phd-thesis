# Prompt Templates & Examples

Use these patterns to form your queries to `notebooklm.ask_question`.

## 1. Author-Centric (Drafting)
**User**: "Write an intro for the gamma-ray analysis chapter."
**Agent Reasoning**: User wants to draft based on their work (001), but needs backing from refs.
**Query**:
> "Focusing strictly on papers starting with '001)', draft an introduction for a chapter on Gamma Ray analysis. Crucially, when the text mentions standard techniques, lookup those specific techniques in the other reference files to provide the citation context."

## 2. Context-Centric (Literature Review)
**User**: "How does my work fit into the current Dark Matter landscape?"
**Agent Reasoning**: Needs the "Big Picture" from 002, then the specific contrast with 001.
**Query**:
> "First, using ONLY the review articles starting with '002)', summarize the current consensus on Dark Matter indirect detection. Then, contrast this consensus with the specific findings and methodologies presented in the '001)' author papers."

## 3. Specific Reference Lookup
**User**: "What does the 2024 Smith paper say about cross-sections?"
**Agent Reasoning**: This is a direct lookup in the General References pool.
**Query**:
> "Search the general reference files (excluding 001/002) for the 'Smith 2024' paper. Summarize its findings on cross-sections."
