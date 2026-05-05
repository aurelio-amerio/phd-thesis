---
name: latexindent
description: Run latexindent one-sentence-per-line on thesis chapter files. Use when the user asks to format, indent, or break lines in a chapter's LaTeX files.
---

# LaTeX Indent — One Sentence Per Line

Formats thesis `.tex` files so each sentence starts on its own line, making diffs and edits easier.

## Command

```bash
latexindent -s -w -m -l localSettings.yaml <file>
```

| Flag | Purpose |
|------|---------|
| `-s` | Silent mode |
| `-w` | Overwrite original (creates `.bak0` backup) |
| `-m` | **Enable `modifyLineBreaks`** — required or the config is ignored |
| `-l` | Use project-root `localSettings.yaml` |

## Config

The config at `localSettings.yaml` (project root) enables `oneSentencePerLine` and excludes lines containing `\begin`, `\end`, `\cite`, `\ref`, `\cref`, `\Cref`, `\eqref`.

## Scope Rules

- **Include**: `chapter_XX/chapter_X.tex` and `chapter_XX/sections/*.tex`
- **Exclude**: Any `paper_*` subdirectories — those are published papers and must not be reformatted

## Procedure

1. Identify all `.tex` files in the target chapter(s) matching the scope rules above
2. Optionally clean stale `.bak0` files from previous runs
3. Run the command on each file from the project root
4. Suppress stderr (`2>/dev/null`) — latexindent emits harmless Perl regex warnings
5. Spot-check one file via `diff <file>.bak0 <file>` to confirm sentences were split
6. Compile with `latexmk -pdf -interaction=nonstopmode main.tex` to verify no breakage

## Example

Format chapter 6:

```bash
cd /path/to/phd-thesis

for f in chapter_06/chapter_6.tex chapter_06/sections/*.tex; do
  latexindent -s -w -m -l localSettings.yaml "$f" 2>/dev/null
done
```
