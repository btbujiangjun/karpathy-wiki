# Query Workflow — Reference

Detailed protocol for answering questions against the wiki and optionally filing answers as new pages.

## Trigger

User asks a question about the wiki's domain. No special command needed — any question triggers this workflow.

## Core Sequence

### Step 0: Preferences and Search Gate

Load `EXTEND.md` preferences using `references/config/extend-schema.md`. If no preference file exists, run first-time preference setup before continuing.

If `bm25.mode: auto_prompt`, check configured thresholds. If reached and BM25 is not initialized, ask whether to initialize it. If the user agrees, follow `references/workflows/bm25.md`.

### Step 1: Navigate via Index

Read `wiki/index.md`. For conceptual, relationship, taxonomy, or landscape questions, also read `wiki/concept-table.md` before choosing pages. Identify pages potentially relevant to the query. If BM25 is configured, use it as an additional candidate finder after reading the index, not as a replacement for the index.

If BM25 is enabled, use it after reading the index:

```bash
python3 scripts/wiki_fts.py stats
python3 scripts/wiki_fts.py search "{user question or extracted query terms}" --limit 10
```

If `stats` reports `Fresh: no`, run `python3 scripts/wiki_fts.py rebuild` before searching. If rebuild fails and `fallback_to_rg: true`, continue with `rg` plus `wiki/index.md`.

BM25 returns candidate chunks only. Do not answer from snippets alone. Open the returned pages and read the full relevant context.

### Step 2: Read Relevant Pages

Read identified pages. If a page references other pages that seem relevant, follow those links too. Stop when you have sufficient context or have read 15+ pages (at which point, work with what you have).

If BM25 is unavailable, stale, or returns no useful results, fall back to `rg` plus `wiki/index.md` when `fallback_to_rg: true`.

### Step 3: Synthesize Answer

Compose an answer that:

- Directly addresses the user's question
- Cites wiki pages inline: `[Page Title](wiki/path/to/page.md)`
- Notes confidence level: high (multiple corroborating sources), medium (single source), low (inference)
- Flags if the wiki lacks sufficient information to fully answer

### Step 4: File Decision

After answering, assess: is this answer a valuable artifact worth preserving?

**File-worthy signals**:

- Comparison or analysis the user is likely to revisit
- New connection discovered between existing concepts
- Synthesis across 3+ sources
- Answer fills a gap in the wiki's coverage

**Not file-worthy**:

- Simple factual lookups
- Clarifying questions about wiki structure
- Trivial or one-off queries

If file-worthy, ask user: "This analysis seems worth keeping. File as `wiki/{type}/{slug}.md`?"

If user agrees:

1. Create the page with proper frontmatter
2. Add cross-references to/from related pages
3. Update `wiki/concept-table.md` if the filed answer creates, renames, merges, splits, or materially revises durable concepts
4. Update `wiki/index.md`
5. Append to `wiki/log.md`:

   ```text
   ## [{date}] query-filed | {title}
   - Question: {original question}
   - Filed as: wiki/{type}/{slug}.md
   - Related pages: {list}
   ```

## Answer Formats

Adapt output format to the question type:

| Question Type | Format |
| --- | --- |
| "What is X?" | Prose explanation, 1-3 paragraphs |
| "Compare X and Y" | Markdown table with dimensions as rows |
| "What do we know about X?" | Structured summary with source citations |
| "What are the open questions on X?" | Numbered list with confidence assessments |
| "Summarize the state of X" | Section-based overview with key claims |
| "Timeline of X" | Chronological list or table |

## When Wiki Cannot Answer

If the wiki lacks information:

1. State clearly what's missing
2. Suggest sources that might fill the gap (web search, specific documents)
3. Optionally: create a stub page noting the knowledge gap

   ```yaml
   ---
   title: "{topic}"
   type: concept
   created: {date}
   updated: {date}
   sources: []
   tags: [stub, needs-sources]
   ---
   ```
