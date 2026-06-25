---
description: Find, define, and mark up acronyms in a thesis .tex file. Usage: /acronyms [path] (defaults to the open file)
---

# Acronyms Workflow

**Usage**: `/acronyms` (the file currently open in the IDE) or `/acronyms <path/to/file.tex>`

Examples: `/acronyms`, `/acronyms chapter_01/sections/1.4_indirect_detection.tex`

## Instructions

1. **Determine the target file**: the path argument if one is given, otherwise the
   `.tex` file the user currently has open in the IDE. State which file you are
   operating on before doing anything else.

2. **Invoke the `acronyms` skill** using the Skill tool.

3. **Follow all steps** defined in the skill:
   - Read `acronyms.tex` (the registry) and the target file
   - Detect occurrences (already-defined + new candidates), applying the
     math/label/citation exclusions and the "don't over-convert dark matter" rule
   - Propose `\newacro` entries for missing acronyms
   - List every replacement with its correct markup form (`\SHORT`, `\Gls{KEY_}`,
     `\glspl{KEY_}`, `\Glspl{KEY_}`), marking the first-use expansion
   - **Present the plan and wait for approval** — do NOT edit before the user says OK
   - On approval: edit `acronyms.tex` + the target file, then compile to verify
   - Report what changed

**Key rule:** plan-then-apply. Never modify `acronyms.tex` or the target file
until the user has approved the proposed plan.
