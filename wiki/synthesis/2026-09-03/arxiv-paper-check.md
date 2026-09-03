---
title: "arXiv Paper Check — AI & CTR (September 3, 2026)"
type: synthesis
created: 2026-09-03
updated: 2026-09-03
sources: []
tags: [arxiv, daily-check, ai, ctr, retrieval, ir, llm-agents, deep-research, multimodal-retrieval, composed-image-retrieval, agentic-search, data-centric-agents, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 3, 2026)

AI & Information Retrieval focused pass over the **fresh Sep 1–2, 2026 submission wave** (IDs `2609.0xxxx`–`2609.02xxx`), complementary to the same-day [arxiv-daily](./arxiv-daily.md) and [arxiv-ai-search](./arxiv-ai-search.md). **4 verified-new papers** (all submitted Sep 1–2, 2026), each grep-verified **absent** (0 hits) from `wiki/` and disjoint from every claim set of the 09-01/09-02 siblings and the 09-03 `arxiv-daily` / `arxiv-ai-search`.

> **Method & dedup boundary:** Papers compiled via live web search of arXiv abs/html pages. The 09-03 `arxiv-daily` claims `2609.00323`; the 09-03 `arxiv-ai-search` claims `2609.01182`; the 09-02 siblings claimed the `2609.0xxxx`–`2609.01603` wave (incl. industrial-recommendation / generative-CTR work such as ReST `2609.01240`, TGR `2609.00986`, CoGR `2609.00638`, ARISE-RL `2609.01058`). All four featured IDs below are grep-verified absent and intentionally avoid re-covering the CTR/ranking papers already claimed by those siblings — this pass emphasizes the **fresh AI · retrieval · agent** angles that were not yet claimed.

---

## ① Deep Research Agents — Hypothesis-Guided Search (1)

### HypoSearch: Explore Before Committing — Hypothesis-Guided Search for Deep Research Agents

| Field | Detail |
|-------|--------|
| **Authors** | HypoSearch team (per arXiv abs; pilot SFT study included) |
| **Submitted** | 2026-09-01 · [2609.01294](https://arxiv.org/abs/2609.01294) · cs.AI |
| **Key contribution** | Deep-research agents often commit to a single evolving search trajectory too early, so later tool calls reinforce a possibly-misleading first direction. Trajectory analysis shows successful runs share two behaviors — grounding vague exploration in concrete candidates, and shifting direction when the current path is weak. **HypoSearch** makes this explicit: it generates lightweight hypotheses (soft search hints), explores each through bounded independent branches, and compares branch-level evidence before commitment. It is a hybrid form of test-time scaling that preserves macro-level adaptivity while adding local parallelism at divergent search states. On four deep-research benchmarks × three backbones it beats single-trajectory and standard parallel baselines — e.g. improving Qwen3.5-122B from **46.7 → 60.0 on BC-small** while using fewer tool calls than five independent trajectories. A pilot SFT shows the behavioral signal can also curate compact training trajectories. |
| **Why it matters** | Ties directly to the wiki's agentic-search / test-time scaling line (TreeSeeker-type branch-and-return work, Marco verify-centric deep research). The core claim — *allocate search compute around uncertainty, not just around final answers* — generalizes beyond web agents to the CTR/rec retrieval stack. |

---

## ② Multimodal Document Retrieval (1)

### MIDR: Enrichment-Augmented Indexing for Multimodal Document Retrieval

| Field | Detail |
|-------|--------|
| **Authors** | Debanjan Mahata, Atharva Tendle, Daniel Preotiuc-Pietro, Yong Zhuang, Ozan Irsoy |
| **Institution** | Bloomberg *(inferred from author network / IR context)* |
| **Submitted** | 2026-09-01 · [2609.01316](https://arxiv.org/abs/2609.01316) · cs.IR (cross cs.AI/cs.CL/cs.CV/cs.LG) · **EMNLP 2026** |
| **Key contribution** | Visually-rich document retrieval has a representation problem: content lives in tables/charts/figures/layout that plain OCR corrupts or omits. ColPali-family visual retrievers handle this with patch-level multi-vector indexes but keep image-derived retrieval on the query-time serving path (expensive). **MIDR** instead shifts multimodal reasoning to **index time** — a training-free framework where a multimodal LLM converts rendered pages into *verified textual fields* at ingestion, indexed with BM25F and optionally fused with dense retrieval, enabling cheap text-centric serving over multimodally-grounded evidence. On ViDoRe V3 it hits **0.6219 avg nDCG across five English domains (+23.0% vs BM25)**, competitive with ColQwen2.5; on two French domains enrichment bridges English query ↔ French text (0.1532 → 0.5448 nDCG). It leads ColQwen2.5 on 4/7 domains while using ~9× smaller index memory and ~2× lower query latency. |
| **Why it matters** | A deployment-first counterpoint to serving-time late interaction: *do the multimodal reasoning once at index time, serve cheaply at query time*. Relevant to the wiki's retrieval-efficiency and multimodal-indexing threads, and directly applicable to document-heavy enterprise recommendation/retrieval pipelines. |

---

## ③ Composed Image Retrieval — Training-Free Reranking (1)

### AutoConcept: Training-Free Concept-Guided Reranking for Metadata-Available Composed Image Retrieval

| Field | Detail |
|-------|--------|
| **Authors** | Tianyu Wang, Tianjiao Wu |
| **Submitted** | 2026-09-01 · [2609.01456](https://arxiv.org/abs/2609.01456) · cs.IR (cross cs.CL) · **PRICAI 2026** (regular paper) |
| **Key contribution** | Composed image retrieval (CIR) retrieves a target image from a reference image + a text modification. For the metadata-available setting, **AutoConcept** is a training-free reranker that converts concept evidence into an interpretable memory: it filters noisy concepts, activates query-relevant positive constraints with an auxiliary negative penalty, and combines the base retrieval score with metadata-based concept-candidate alignment via inference-time calibration. On FashionIQ it gives significant early-rank gains over the WeiMoCIR baseline and consistent plug-in gains on LinCIR candidate pools; metadata-aware controls show structured concept memory adds signal beyond direct query-text / extracted-attribute matching; a query-only variant supports the concept-level reranking hypothesis. A supplementary real-human concept-label study shows the same memory interface can consume participant-provided evidence. |
| **Why it matters** | An interpretable, training-free second-stage reranker for product-style metadata-rich catalogs — pedagogically adjacent to the wiki's retrieval-reliability / training-free-reranking thread, with an explicit interpretability angle (concept memory) that many black-box rerankers lack. |

---

## ④ Data-Centric Agents — Persistent Discovery Context (1)

### Beyond Context Windows: Persistent Discovery Context for Data-Centric Agents

| Field | Detail |
|-------|--------|
| **Authors** | Jalal Mahmud |
| **Submitted** | 2026-09-02 · [2609.02129](https://arxiv.org/abs/2609.02129) · cs.AI (cross cs.IR) |
| **Key contribution** | Data-centric agents repeatedly perform a *discovery* step (identifying the data objects relevant to a task) before planning/execution, yet successful discovery outcomes are typically discarded. The paper introduces **persistent discovery context** — a lightweight memory layer that stores prior intent-to-object mappings and reuses them to augment future retrieval. Across three structured-data environments it consistently improves retrieval quality over metadata-only search, stays effective with automatically generated memories, and exposes a reproducible interference failure mode; in lexically sparse domains memory-only retrieval can even beat metadata-based retrieval. |
| **Why it matters** | Reframes agent memory as reusable *discovery outcomes* rather than just context tokens — an efficiency/architecture insight with direct relevance to enterprise data agents and to how retrieval relevance is cached and reused across tasks (a sibling theme to the wiki's memory / retrieval-reuse lines). |

---

## Cross-Cutting Themes (2026-09-03 AI & CTR pass)

1. **Move expensive reasoning off the hot path or index time.** MIDR moves multimodal understanding to index time; HypoSearch moves search-compute allocation to a hypothesis layer; AutoConcept moves concept scoring to a training-free reranking stage. The shared move: *shift the costly-but-reusable computation earlier / out-of-band*, leaving the serving-time path cheap.
2. **Context is not the only memory; outcomes and reused structure matter.** Beyond Context Windows, MIDR's reusable text fields, and AutoConcept's concept memory all treat persistent, reusable artifacts (discovery mappings, extracted fields, concept memories) as the real knowledge store — context windows are just the transient working set.
3. **Training-free corrections keep compounding.** MIDR, AutoConcept are fully training-free; HypoSearch mostly inference-time. Consistent with the wiki's recent trend (causal-RAG reranker, etc.) that cheap, structured corrections increasingly complement (not replace) learned systems — often with explicitly documented scope boundaries.

---

## Methodology

- **Listing source**: arXiv abs/html pages for the fresh Sep 1–2, 2026 wave (IDs `2609.0xxxx`–`2609.02xxx`), discovered via live web search + direct abs-page reads (arXiv API/curl network access was limited in this session, so `webfetch` of abs pages and `websearch` were used).
- **Dedup**: all four featured IDs **grep-verified absent** from `wiki/**` and cross-checked against the 09-01/09-02 sibling claimed sets and the 09-03 `arxiv-daily` (`2609.00323`) / `arxiv-ai-search` (`2609.01182`).
- **Window**: papers submitted on/before Sep 2, 2026 whose IDs were not already claimed by any sibling report.
- **Coverage disclaimer**: this pass emphasizes the fresh AI · retrieval · agent angles. Same-wave industrial CTR / generative-ranking papers (ReST, TGR, CoGR, etc.) were already claimed by the 09-02 siblings and the 09-03 `arxiv-daily` / `arxiv-ai-search`, so they are intentionally **not** re-covered here; see those pages for the CTR/ranking digest.

*Affiliations marked *(stated)* come from paper front matter; *(inferred)* = deduced from author identities / prior papers and remain tentative.*
