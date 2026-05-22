# Review-Mode annotation-ID vs thread-ID mixup — incident report

**Date:** 2026-05-22
**Reporter:** Claude (Opus 4.7, 1M context), during `/subagent-driven-development` execution of `docs/superpowers/plans/2026-05-22-section-1.3-implement-review.md`.
**Scope:** Affects any workflow that builds a plan document listing annotation IDs (e.g., the SDD plan-writing path), then later resolves them via the `update_annotation` MCP tool. Does NOT affect the `/implement-review` skill itself in its end-to-end form.

---

## TL;DR

When resolving the 26 Review-Mode annotations on `chapter_01/sections/1.3_searching_for_dark_matter.tex` at the end of a long SDD plan execution, 2 of the 26 `update_annotation` calls returned `Updated 0 annotation(s)` instead of `Updated 1`. The IDs in the plan's resolution table — `1afjqnc` (annotation at L83) and `u43f0xl` (annotation at L113) — turned out to be **thread message IDs**, not the parent annotation IDs (`l61i6yv` and `dza1ndt`). The on-disk JSON, the MCP server, and the `/implement-review` skill are all correct; the slip was a transcription error in the prior SDD design-spec / plan-writing session. The MCP server's silent `Updated 0` response made the failure trivially missable in a batch of 26 calls.

## What happened — step by step

1. **Earlier session (not the SDD execution itself):** a Claude session used the `superpowers:writing-plans` + `superpowers:brainstorming` workflow to produce a `/implement-review` design spec and execution plan for §1.3. The design spec includes a 26-row markdown table mapping each annotation ID to its fix. Two of those rows captured the **first thread message ID** instead of the **top-level annotation ID**.

   | Plan listed | Actual annotation ID | First thread message ID |
   |---|---|---|
   | `1afjqnc` | `l61i6yv` | `1afjqnc` ← plan grabbed this |
   | `u43f0xl` | `dza1ndt` | `u43f0xl` ← plan grabbed this |

2. **Execution session (today):** Task 17 of the plan iterated through the 26 IDs and called `update_annotation(annotation_ids=[id], status="resolved", message="...")` for each.

3. **Server response:** For 24 calls the server returned `Updated 1 annotation(s)`. For the 2 mismatched calls it returned `Updated 0 annotation(s)`. No error, no warning — just a numeric counter buried in a batch of 26 nearly-identical responses.

4. **Detection:** Only because I happened to scan the batch responses did I notice the two zeros. Without that, the run would have closed out with 24/26 annotations actually resolved while the run's summary claimed 26/26 — a silent failure.

5. **Recovery:** A `get_annotations` round-trip revealed the two annotations still had `status: open`, with the "missing" IDs from the plan visible as `thread[0].id` inside the real annotation objects. I issued two corrected `update_annotation` calls and verified all 26 annotations were resolved.

## Root-cause analysis

### What is NOT at fault

- **The JSON file** (`.revisions/<chapter>/<file>/rev*.json`). The on-disk schema is consistent across all 26 annotations: each annotation has a top-level `id` and a `thread` array, and each message in the thread has its own `id`. No aliased fields, no shape variation. The two problematic annotations are structurally identical to the other 24.

- **The MCP server.** `update_annotation` matches `annotation_ids` against top-level `id` only, which is the correct, unambiguous behavior. Returning `Updated 0` when no annotation matches is technically right; the issue is only that the response is silent in the failure case.

- **The `/implement-review` skill.** Reading the actual skill file at `commands/implement-review.md`, the workflow is 7 simple steps: identify file → fetch annotations → summarize → implement → resolve → re-open → report. It calls `get_annotations` and `update_annotation` directly; it does NOT build any markdown table of IDs and does NOT depend on any pre-written plan. End-to-end uses of `/implement-review` in one session would not hit this bug.

### Where the bug actually lives

A **transcription mistake** in the prior plan-writing session. When the agent generated the design-spec's annotation-resolution table from `get_annotations` output, for 2 of 26 entries it copied `thread[0].id` instead of the top-level `id`. There is no programmatic pattern in the data that explains *why* those two specifically — both problematic annotations are structurally indistinguishable from the others (each has `thread = [reviewer_message]` at plan-writing time, top-level `id` clearly distinct from `thread[0].id`). It is a human-style slip-up, the kind that's hard to catch at write-time because the wrong ID and the right ID are both 7-character alphanumeric strings.

### Why the failure was invisible

The server returns `Updated 0` silently. In a batch of 26 calls, the response sequence reads as `Updated 1 · Updated 1 · ... · Updated 0 · ... · Updated 1`. There is no error log, no explicit warning, no hint that "0" might be a problem. In an SDD pipeline where each task tends to produce many tool calls, this is exactly the signal that gets eaten by skim-reading.

## Recommendations

Ordered by **leverage ÷ effort**, highest first.

### 1. Add a diagnostic hint to `update_annotation` when `Updated 0` (server change)

The server already knows which IDs didn't match. With one extra lookup pass, it can detect when an unmatched ID is actually a thread message ID belonging to some annotation, and include a hint in the response:

```jsonc
// current behavior
{"result": "Updated 0 annotation(s)."}

// suggested behavior
{
  "result": "Updated 0 annotation(s).",
  "warnings": [
    "'1afjqnc' is a thread message ID inside annotation 'l61i6yv' (not an annotation ID).",
    "'u43f0xl' is a thread message ID inside annotation 'dza1ndt' (not an annotation ID)."
  ]
}
```

This converts silent failures into surfaced ones without any API breakage. The agent caller (or a human reading the output) sees the hint immediately and corrects the call. The lookup is O(n_thread_messages) per unmatched ID — cheap.

**Trade-off:** none material. Adds one optional field to the response shape.

**Effort:** ~10 lines of server code + test.

### 2. Add a closing `get_annotations` verification step to `/implement-review` (skill change)

The current Step 7 ("Report") just prints a status line. Adding a final `get_annotations` call and asserting no `open` / `in-progress` annotations remain would catch this whole class of bug regardless of where the slip happened:

```markdown
### Step 7 — Verify and report

Call `get_annotations(file_path=..., workspace=...)` once more. Inspect each
annotation's status:

- If all annotations are `resolved`: report success as today.
- If any annotations are still `open` or `in-progress`: list their IDs and
  startLine, and tell the user explicitly that those were NOT resolved.
  Do NOT claim a clean run.

> ✅ Review implemented for `<file>`. N comments resolved.
> ⚠️ M annotations still open: [id1 (L83), id2 (L113)]. Check the resolution call.
```

This is the most general defensive practice. It catches: (a) thread-ID-vs-annotation-ID slips, (b) annotations the agent forgot to resolve, (c) `update_annotation` calls that failed for any other reason. It costs one MCP round-trip at the end of the workflow, which is negligible.

**Trade-off:** none. Pure improvement.

**Effort:** docs/skill change only; no server work.

### 3. One sentence in the MCP server README / `update_annotation` docstring

A targeted note for anyone hand-building annotation lists from `get_annotations` output:

> The `annotation_ids` field expects the **top-level `id`** of each annotation from `get_annotations`. It does **not** match any `thread[].id` (the message-level IDs nested inside each annotation's thread). If you pass a thread message ID, the call will silently return `Updated 0` (or, with diagnostic hints enabled, a warning identifying the parent annotation).

This is the cheapest possible change and saves the next agent / human a half-hour of confusion.

**Effort:** 30 seconds.

### Not recommended

- **Make `annotation_ids` accept thread IDs by walking up to the parent.** Bad: papers over the bug, makes the API ambiguous, and risks subtle wrong-target updates if thread IDs ever collide across annotations. Keep the API strict.
- **Prefix annotation IDs / thread IDs with distinguishing namespaces (`ann_…` / `thr_…`).** Eliminates the class of bug entirely but is a breaking schema change. Probably not worth the migration cost given the small surface of affected workflows.
- **Change `/implement-review` to require a pre-written plan.** It doesn't need one. The skill is fine end-to-end in a single session. The bug only manifests when humans/agents split the workflow into "plan now, execute later" and write down IDs in between.

## Suggested priority

If you can only do one thing: **Recommendation 1** (diagnostic hint on `Updated 0`). Cheapest server-side change with the broadest payoff.

If you can do two: **1 + 2** (server hint + skill verification step). Together they make this class of bug essentially extinct: the server surfaces it loudly, and the skill double-checks the post-state regardless.

If you can do three: add the README sentence (Recommendation 3) for completeness.

## Reference data

For the maintainer's convenience, here is the exact shape from `rev1.json` (the active annotation snapshot at execution time) for one OK case and the two problematic cases. Note they are structurally identical:

```json
// OK case — plan correctly captured top-level id
{
  "id": "6t0sqyb",
  "startLine": 8,
  "thread": [
    { "id": "w8o45y5", "text": "attack -> tackles" }
  ]
}

// Problematic case 1 — plan captured thread[0].id "1afjqnc"
{
  "id": "l61i6yv",
  "startLine": 83,
  "thread": [
    { "id": "1afjqnc", "text": "maybe too specific?" }
  ]
}

// Problematic case 2 — plan captured thread[0].id "u43f0xl"
{
  "id": "dza1ndt",
  "startLine": 113,
  "thread": [
    { "id": "u43f0xl", "text": "we need at least another citation for this. maybe the cosmixs paper, the pppc, or even something else" }
  ]
}
```

No data peculiarity distinguishes the failure cases from the success cases.

## Detection script (for the curious)

A one-liner to verify post-execution that nothing was missed:

```python
import json
from urllib.parse import quote  # or whatever your MCP client uses
# Pseudocode: call get_annotations(file_path=..., workspace=...)
anns = call_mcp_get_annotations(file_path="...", workspace="...")
open_anns = [a for a in anns if a["status"] in ("open", "in-progress")]
if open_anns:
    print(f"⚠️ {len(open_anns)} annotations still open:")
    for a in open_anns:
        print(f"  id={a['id']} startLine={a['startLine']}")
else:
    print(f"✅ All {len(anns)} annotations resolved.")
```

Embedding this (or its skill-language equivalent) into `/implement-review` Step 7 is what Recommendation 2 amounts to.
