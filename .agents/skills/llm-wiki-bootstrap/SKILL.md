---
name: llm-wiki-bootstrap
description: >
  Bootstrap and operate an LLM Wiki: a persistent Markdown knowledge base with
  immutable raw sources, an LLM-maintained wiki, a SCHEMA.md operating contract,
  thin runtime pointer files, EXTEND.md preferences, and optional local BM25
  search. Use when the user asks to create or bootstrap an LLM wiki, ingest
  sources, query or lint a wiki, configure EXTEND.md preferences, or set up
  BM25/full-text search for an LLM Wiki.
version: 0.1.0
---

# LLM Wiki Bootstrap

Build and maintain a personal LLM Wiki: raw evidence stays immutable in `raw/`, durable knowledge is compiled into `wiki/`, and `SCHEMA.md` is the generated wiki's single operating contract.

This file is intentionally short. Load detailed references only for the operation the user requested.

## Operating Model

- Keep `SCHEMA.md` as the single source of truth inside every generated wiki.
- Keep `wiki/concept-table.md` as the maintained concept map: it complements `wiki/index.md` by summarizing durable concepts, relationships, sources, status, and maintenance notes.
- Keep `CLAUDE.md`, `AGENTS.md`, and `.github/copilot-instructions.md` as thin pointers to `SCHEMA.md`; never duplicate operating rules into them.
- Treat `raw/` as read-only evidence. Create and update derived knowledge only under `wiki/`.
- Apply `EXTEND.md` preferences before bootstrap, ingest, query, lint, or BM25 work.
- Ask only for missing decisions, and batch setup questions into one user prompt when possible.
- Prefer progressive disclosure: read the smallest reference file that can complete the current task.

## Intent Router

| User intent                            | Do this                                                                                                        | Reference                                                              |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Create or bootstrap a new wiki         | Run preference preflight, gather setup answers, then generate the scaffold and seed files.                     | `references/workflows/bootstrap.md`                                    |
| Ingest one or more sources             | Run preference preflight, check the optional BM25 gate, then compile source knowledge into `wiki/`.            | `references/workflows/ingest.md`                                       |
| Answer a domain question from the wiki | Run preference preflight, navigate `wiki/index.md`, use BM25 only as a candidate finder, then cite wiki pages. | `references/workflows/query.md`                                        |
| Check wiki health or consistency       | Run preference preflight, scan structure and content, report findings, then fix only approved items.           | `references/workflows/lint.md`                                         |
| Configure or use BM25 search           | Load preferences, ask before initialization, create local search files, smoke test, and log results.           | `references/workflows/bm25.md`                                         |
| Configure preferences                  | Locate or create `EXTEND.md` using the schema and template.                                                    | `references/config/extend-schema.md`, `references/templates/extend.md` |

## Preference Preflight

Before bootstrap, ingest, query, lint, or BM25 work, read `references/config/extend-schema.md` and use the first available `EXTEND.md` in its lookup order. If none exists, run the first-time preference setup and create one from `references/templates/extend.md` before continuing.

On first use in a session, briefly say which preference file is active. Do not silently use defaults.

## Reference Loading Rules

- For bootstrap, read `references/workflows/bootstrap.md`, then load each template only when creating that file.
- For ingest, query, and lint, read the matching workflow file first; read `references/workflows/bm25.md` only when preferences or the user request require search behavior.
- For schema generation, read `references/templates/schema.md` and inject domain snippets from `references/templates/domain-page-types.md` as needed.
- For pointer files, read `references/templates/agent-pointer.md` and keep the generated file minimal.
- For BM25 initialization, read `references/templates/wiki_fts.py` and `references/templates/bm25-readme.md` only after the user approves initialization.

## Package Layout Rules

- Put skill-owned runnable helpers in `scripts/` if they are meant to be executed from the installed skill package.
- Put generated-output templates in `references/templates/`, even when the generated file will become executable after it is copied into the user's wiki.
- Put long procedural documentation in `references/workflows/` and configuration schemas in `references/config/`.
- In this skill, `references/templates/wiki_fts.py` is a template for the generated wiki's `scripts/wiki_fts.py`; it is not executed in place by the skill.

## Hard Rules

- Never overwrite an existing wiki without explicit user approval.
- Never modify files in `raw/` except to create empty scaffold placeholders such as `.gitkeep` during bootstrap.
- Never answer directly from BM25 snippets; open and read the returned wiki pages first.
- Preserve source language during ingest unless the user asks for a different wiki language.
- Update `wiki/index.md` and append `wiki/log.md` whenever wiki content changes.
- If a search index rebuild fails, keep wiki edits, log the failure, and fall back to `wiki/index.md` plus text search.

## Core Outputs

A successful bootstrap creates a wiki root containing:

```text
raw/
wiki/index.md
wiki/concept-table.md
wiki/log.md
wiki/overview.md
SCHEMA.md
.gitignore
```

Optional outputs depend on setup answers and preferences: runtime pointer files, `.vscode/settings.json`, `scripts/wiki_fts.py`, `indexes/`, and `exports/`.
