# Bootstrap Workflow — Reference

Use this workflow only when the user wants to create a new LLM Wiki scaffold.
For preference lookup and first-time preference setup, follow
`references/config/extend-schema.md` before Phase 1.

## Goal

Create a ready-to-use LLM Wiki with an immutable source layer, an
LLM-maintained wiki layer, a `SCHEMA.md` operating contract, optional runtime
pointers, and editor/search configuration selected by the user.

## Phase 1: Gather Requirements

Blocking: complete this phase before creating files.

Ask all questions in one user prompt:

| Header | Question | Notes |
| --- | --- | --- |
| Domain | What is this wiki about? | Options: Research topic; Book / media; Personal (goals, health, learning); Business / team; Other. |
| Wiki name | Short name for the wiki root directory? | Free text. Suggest `{domain}-wiki`, such as `ml-wiki`, `lotr-wiki`, or `health-wiki`. |
| Runtimes | Which runtimes will read this wiki? | Multi-select: Claude Code, OpenAI Codex, Copilot (VS Code), Other / generic. |
| Editor | Primary editor for browsing the wiki? | Options: Obsidian (recommended), VS Code, Other / plain files. |
| Source types | What kind of sources will you add? | Multi-select: Web articles, PDFs / papers, Books, Meeting notes / transcripts, Personal notes / journals, Images / diagrams, Data files, Other. |
| Output location | Where to create the wiki? | Current directory or a custom absolute path. |

Store answers for later phases. If the custom output location is ambiguous,
ask one follow-up question before writing files.

## Phase 2: Create Directory Structure

Create this base tree under `{wiki-root}/`:

```text
{wiki-root}/
├── raw/
│   └── assets/             # only when image / diagram sources are selected
├── wiki/
│   ├── index.md
│   ├── concept-table.md
│   ├── log.md
│   └── overview.md
├── SCHEMA.md
├── {pointer-files}
└── .gitignore
```

Conditional outputs:

| Condition | Add |
| --- | --- |
| Source types include images / diagrams | `raw/assets/` |
| Any source type selected | `raw/.gitkeep` |
| Editor is Obsidian | Do not create `.obsidian/`; Obsidian creates it. |
| Editor is VS Code | `.vscode/settings.json` with markdown-friendly defaults. |
| Runtime includes Claude Code | `CLAUDE.md` pointer. |
| Runtime includes OpenAI Codex | `AGENTS.md` pointer. |
| Runtime includes Copilot (VS Code) | `.github/copilot-instructions.md` pointer. |

Create `.gitignore` from `references/templates/gitignore.md`.

Before writing into an existing path, inspect it. If generated files would
overwrite user content, ask for approval or choose a different wiki root.

## Phase 3: Generate `SCHEMA.md`

Write `{wiki-root}/SCHEMA.md` from `references/templates/schema.md`.

Template variables:

| Variable | Source |
| --- | --- |
| `{WIKI_NAME}` | Wiki name answer. |
| `{DOMAIN_DESCRIPTION}` | Domain answer expanded to 1-2 clear sentences. |
| `{SOURCE_TYPES}` | Source type answers, comma-separated. |
| `{EDITOR}` | Editor answer. |
| `{DATE}` | Current date in `YYYY-MM-DD`. |

Inject page-type snippets from `references/templates/domain-page-types.md`:

| Domain | Add page types |
| --- | --- |
| Book / media | Character, timeline, plot thread, theme, location. |
| Research topic | Paper summary, claim, method, dataset. |
| Personal | Journal entry, goal, habit, lesson. |
| Business / team | Decision log, meeting summary, project, stakeholder. |
| Other | Use the universal page types unless the user gave a clearer taxonomy. |

If editor is Obsidian, append an `## Obsidian Setup` section to `SCHEMA.md`:

- Set attachment folder path to `raw/assets/`.
- Recommended plugins: Dataview, Marp when slide decks are useful.
- Use graph view to inspect wiki structure.
- Bind a download-attachments hotkey if using Web Clipper.

Do not put editor-specific setup in pointer files.

## Phase 4: Generate Pointer Files

For each selected runtime other than Other / generic, create a thin pointer from
`references/templates/agent-pointer.md`.

| Runtime | Path | `{SCHEMA_PATH}` |
| --- | --- | --- |
| Claude Code | `{wiki-root}/CLAUDE.md` | `./SCHEMA.md` |
| OpenAI Codex | `{wiki-root}/AGENTS.md` | `./SCHEMA.md` |
| Copilot (VS Code) | `{wiki-root}/.github/copilot-instructions.md` | `../SCHEMA.md` |

Pointer files contain only identity context, a redirect to `SCHEMA.md`, and the
smallest useful trigger hints.

## Phase 5: Generate Initial Wiki Files

Create these seed pages:

| File | Template | Customization |
| --- | --- | --- |
| `wiki/index.md` | `references/templates/index.md` | Add universal sections plus domain-specific sections. |
| `wiki/concept-table.md` | `references/templates/concept-table.md` | Fill `{DATE}` with the current date; leave concept rows empty. |
| `wiki/log.md` | `references/templates/log.md` | Add the first wiki creation entry with the current date. |
| `wiki/overview.md` | `references/templates/overview.md` | Add a short stub explaining the wiki purpose and domain. |

Universal index sections: Core Maps, Sources, Entities, Concepts, Comparisons, Synthesis.

Domain-specific index sections:

| Domain | Sections |
| --- | --- |
| Research topic | Papers, Claims, Methods, Datasets. |
| Book / media | Characters, Timelines, Themes, Locations. |
| Personal | Journal, Goals, Habits, Lessons. |
| Business / team | Decision Logs, Meetings, Projects, Stakeholders. |

Leave empty sections with placeholder comments rather than inventing content.

## Phase 6: Editor Configuration

If editor is VS Code, create `{wiki-root}/.vscode/settings.json`:

```json
{
  "files.exclude": { "**/.DS_Store": true },
  "editor.wordWrap": "on",
  "markdown.preview.breaks": true
}
```

If editor is Obsidian or Other / plain files, do not create editor settings
beyond the Obsidian guidance already appended to `SCHEMA.md`.

## Phase 7: Summary

After all files are created, report:

```text
Wiki scaffolded at {wiki-root}/

Structure:
  raw/          -> Drop source documents here
  wiki/         -> LLM-maintained pages
  wiki/concept-table.md -> Maintained concept map
  SCHEMA.md     -> Single source of truth for agent behavior

Pointer files:
  {list generated pointer files, or "none"}

Next steps:
  1. Open {wiki-root}/ in {editor}
  2. Add the first source to raw/
  3. Tell the agent: "Read {wiki-root}/SCHEMA.md, then ingest raw/{filename}"
```

Do not initialize BM25 during bootstrap unless the user explicitly requested it
or active preferences require it. If BM25 is requested, follow
`references/workflows/bm25.md` after the base scaffold is complete.
