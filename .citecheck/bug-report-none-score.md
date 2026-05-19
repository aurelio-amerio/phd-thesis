# Bug Report: `score=null` causes TypeError in citecheck-deep pipeline

## Symptom

Running `citecheck-deep` on a `.tex` file whose `.citecheck/<basename>.json` report
contains any citation with `"score": null` crashes with:

```
TypeError: '<' not supported between instances of 'NoneType' and 'int'
```

## Root Cause

`dict.get(key, default)` returns the default **only when the key is absent**.
When the key is present with value `null`/`None`, it returns `None`.

Any threshold comparison of the form:

```python
row.get("score", 10) < threshold   # FRAGILE
```

will raise `TypeError` when `score` is `null` — even though a null score clearly
signals "needs deep-check."

This affects at minimum:

- **`citecheck-deep-select-candidates`** — selects candidates for the arXiv/NLM queues.
- Any downstream step that reads `score` from the report and compares it numerically.

## When does `score=null` appear?

A citation ends up with `score=null` in the shallow citecheck report when:

- No arXiv abstract was found (no `arxiv_id`).
- The abstract fetch failed.
- The haiku scorer returned malformed JSON.

These are precisely the citations that *most* need deep verification — so they must
not be silently skipped.

## Fix

Replace every numeric comparison on `score` with a null-safe guard:

```python
# Option A — explicit guard (clearest intent)
score = row.get("score")
if score is None or score < threshold:
    # needs deep-check

# Option B — one-liner with a safe sentinel
if (row.get("score") ?? 0) < threshold:   # pseudocode; use Option A in Python

# Python equivalent of Option B
if (row.get("score") or 0) < threshold:   # only safe if score is never legitimately 0
```

**Recommended**: use Option A. Treat `score=null` as an explicit signal meaning
"unverified / no abstract" and route it directly to the NLM queue, bypassing the
arXiv-PDF stage (since there is no arxiv_id to fetch anyway).

## Suggested routing logic in `select-candidates`

```python
for row in report["all_rows"]:
    score = row.get("score")
    arxiv_id = row.get("arxiv_id")

    if score is None:
        # No abstract was found — send straight to NLM queue
        nlm_queue.append(row)
    elif score < threshold:
        if arxiv_id:
            arxiv_queue.append(row)   # will be scored by Sonnet + PDF
        else:
            nlm_queue.append(row)     # no PDF available, go to NLM directly
    # else: score >= threshold → skip
```

## Files to audit

- `bin/citecheck-deep-select-candidates`
- `bin/citecheck-deep-collate-report`
- `bin/citecheck-deep-summarize`
- Any other script that reads `score` from a report JSON and compares it numerically.
