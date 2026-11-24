---
title: "ArXiv Paper Check — AI & CTR (2026-11-24)"
type: synthesis
created: 2026-11-24
updated: 2026-11-24
sources:
  - https://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=40
  - https://export.arxiv.org/api/query?search_query=cat:cs.IR+OR+cat:cs.LG+OR+cat:stat.ML&sortBy=submittedDate&sortOrder=descending&max_results=60
  - https://export.arxiv.org/api/query?search_query=abs:%22click+through+rate%22+OR+ti:CTR&sortBy=submittedDate&sortOrder=descending&max_results=50
tags:
  - arxiv
  - daily-check
  - ai
  - ctr
  - recommendation
  - advertising
  - retrieval
  - ir
  - lg
  - daily-digest
---

# ArXiv Paper Check — AI & CTR (2026-11-24)

> **Window note:** Queried via the arXiv Export API at ~2026-11-24 (strict last-24h window, 2026-11-23 → 2026-11-24). AI = `cat:cs.AI`; CTR = `cat:cs.IR` / `cat:cs.LG` / `stat.ML` (home categories of click-through-rate / recommender / advertising literature) + keyword sweep (`abs:"click through rate" OR ti:CTR`). **Result: 0 new AI/CTR papers — arXiv is quiet in this window; there are no picks to summarize.** The keyword sweep matches some pre-window papers whose abstracts mention CTR (e.g. `DNA: Unlocking Depth Scaling in CTR Models` 2611.25659v1, `X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction` 2611.24283v1); all are already covered by sibling reports. Abstract/metadata-level screening only, no full-text review; metrics/claims author-reported where present.

## Coverage table

| Lane | New papers in window | Newest paper (submitted) |
|------|---------------------|--------------------------|
| AI — `cat:cs.AI` | 0 | — (freshest available: `2611.28671v1`, 2026-11-21) |
| CTR — `cat:cs.IR` | 0 | — (freshest available: `2611.28645v1`, 2026-11-21) |
| CTR — `cat:cs.LG` / `stat.ML` | 0 | — (freshest available: `2611.27983v1`, 2026-11-20) |
| CTR keyword sweep | 0 | — (matches pre-window papers, already covered) |

## Freshest available (outside the window)

- **The Evaluation Substrate Matters: Benchmarking Multi-Agent Serving Substrates** (2611.28671v1; cs.AI; Haoyuan Zheng, Dongting Li, Hancheng Ye, Qinsi Wang, Mingyuan Ma, Yuncheng Yao, Yifei Wang, Baijun Zhou, Zishan Shao, Tingjun Chen, Hai Helen Li, Danyang Zhuo, Yiran Chen). Key contribution: the MASSys benchmark, which executes the same multi-agent LLM workflows across serving substrates and load regimes, recording task quality alongside delivery, latency, cost, resource pressure and failure evidence — so benchmark results become conditional on how the workflow is executed (e.g., a "Star" workflow drops from 1st to 4th in mean-latency rank under KV-cache pressure).

- **PROSPER: LLMs as Sparse Retrievers for First-Stage Product Search** (2611.28645v1; cs.IR; Hongru Song, Yu-An Liu, Ruqing Zhang, Jiafeng Guo, Maarten de Rijke, Sen Li, Wenjun Peng, Fuyu Lv, Xueqi Cheng). Key contribution: uses LLMs as sparse retrievers for e-commerce product search while explicitly preserving lexical fidelity — a literal residual network reinforces underweighted literal terms, and a lexical focusing window uses top-k selection for early sparsification and training initialization; offline and large-scale online A/B tests show consistent improvements over existing sparse retrievers, with revenue gains for industrial hybrid retrieval.

- **Optimal Linear Regression Without a Variance** (2611.27983v1; cs.LG/stat.ML; Artin Tajdini, Jasper C. H. Lee, et al., 2026-11-20). Key contribution: a black-box reduction converting finite-variance linear regression procedures into weak-moment procedures via empirical residual pruning, with a matching minimax lower bound.

## Interpretation

- No new `cat:cs.AI` submissions in the strict last-24h window (2026-11-23 → 2026-11-24); the freshest cs.AI papers are 2611.28671v1 (2026-11-21T08:50Z) and earlier.
- No new `cat:cs.IR` submissions either (freshest 2611.28645v1, 2026-11-21T08:14Z); no new cs.LG/stat.ML entries (freshest 2611.27983v1, 2026-11-20T18:58Z).
- The keyword sweep matches are all pre-window; this is consistent with the 0-result windows of the sibling 2026-11-21/22/23 reports — arXiv activity in these categories has been idle for several days.

## Related

- [[synthesis/2026-11-23/arxiv-paper-check|2026-11-23 ArXiv Paper Check]]
- [[synthesis/2026-11-22/arxiv-paper-check|2026-11-22 ArXiv Paper Check]]
- [[synthesis/2026-11-21/arxiv-paper-check|2026-11-21 ArXiv Paper Check]]
- [[synthesis/2026-11-20/arxiv-paper-check|2026-11-20 ArXiv Paper Check]]
