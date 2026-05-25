# llm-wiki-bootstrap Preferences

This file customizes how the llm-wiki-bootstrap skill behaves for this project or
user account. The first EXTEND.md found in the configured priority order wins.

```yaml
bm25:
  # auto_prompt: remind when thresholds are reached
  # manual: never remind automatically; only act on explicit user request
  # off: disable BM25 checks and reminders
  # enabled: use BM25 when available; initialize if missing and user approves
  # required: require BM25 for ingest/query/lint once configured
  mode: auto_prompt

  # If true, do not repeat the same auto_prompt after the user declines until
  # the strong thresholds are reached.
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

## Notes

- BM25 is optional. It is a local retrieval helper for larger Markdown wikis.
- BM25 does not replace `wiki/`, `index.md`, `SCHEMA.md`, or the LLM's judgment.
- Generated search artifacts such as `indexes/fts.sqlite` and `exports/*.jsonl`
  are rebuildable and should normally stay out of git.
