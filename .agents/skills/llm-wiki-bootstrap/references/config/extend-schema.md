# EXTEND.md Schema

`EXTEND.md` stores user preferences for llm-wiki-bootstrap. It is optional only
after the first setup has created or selected a preference file. Do not silently
fall back to defaults when no file exists.

## Lookup Order

Read the first file that exists:

| Priority | Path | Scope |
| --- | --- | --- |
| 1 | `.llm-wiki-bootstrap/EXTEND.md` | Project |
| 2 | `${XDG_CONFIG_HOME:-$HOME/.config}/llm-wiki-bootstrap/EXTEND.md` | XDG |
| 3 | `$HOME/.llm-wiki-bootstrap/EXTEND.md` | User home |

On first use in a session, briefly say which file is active:

```text
Using preferences from {path}. You can edit EXTEND.md to customize BM25 thresholds, ingest behavior, search policy, etc.
```

If no file exists, run first-time preference setup before bootstrap, ingest,
query, lint, or BM25 work.

## First-Time Preference Setup

Ask the user where to create the file:

- Project: `.llm-wiki-bootstrap/EXTEND.md` (recommended)
- XDG: `${XDG_CONFIG_HOME:-$HOME/.config}/llm-wiki-bootstrap/EXTEND.md`
- User home: `$HOME/.llm-wiki-bootstrap/EXTEND.md`

Then ask:

1. BM25 reminder mode: `auto_prompt` (recommended), `manual`, or `off`
2. Thresholds: recommended values or custom values
3. Rebuild policy after ingest: `true` (recommended) or `false`

Create the file from `references/templates/extend.md`, adapted to the answers.

## Fields

```yaml
bm25:
  mode: auto_prompt
  prompt_once: true

  thresholds:
    source_count: 30
    wiki_page_count: 150
    wiki_text_chars: 250000
    index_lines: 500
    query_read_pages: 15

  strong_thresholds:
    source_count: 50
    wiki_page_count: 300
    wiki_text_chars: 500000

  index_paths:
    - wiki

  include_raw: false
  auto_rebuild_after_ingest: true
  fallback_to_rg: true

  chunking:
    max_chars: 1800
    overlap_chars: 200

  export:
    default_format: jsonl
    include_text: true
```

## BM25 Mode Semantics

| mode | Behavior |
| --- | --- |
| `auto_prompt` | Check thresholds and ask whether to initialize BM25 when reached. |
| `manual` | Never prompt automatically; only initialize on explicit user request. |
| `off` | Disable BM25 checks and reminders. |
| `enabled` | Use BM25 when available; if missing, ask before initializing. |
| `required` | Require BM25 for ingest/query/lint once configured; stop if unavailable. |

## Threshold Semantics

If any normal threshold is reached, ask once when `mode: auto_prompt`.
If any strong threshold is reached, ask again even if the user previously
declined a normal reminder.

Recommended normal thresholds:

- `source_count >= 30`
- `wiki_page_count >= 150`
- `wiki_text_chars >= 250000`
- `index_lines >= 500`
- `query_read_pages >= 15`

Recommended strong thresholds:

- `source_count >= 50`
- `wiki_page_count >= 300`
- `wiki_text_chars >= 500000`

## Decision Recording

If the user declines initialization, record the decision in the active
`EXTEND.md`:

```yaml
bm25:
  last_prompt:
    date: YYYY-MM-DD
    decision: declined
    source_count: 34
    wiki_page_count: 168
    wiki_text_chars: 281000
```

Do not write operational state such as index freshness here. Store operational
events in `wiki/log.md` and derive freshness from file modification times or
`python3 scripts/wiki_fts.py stats`.
