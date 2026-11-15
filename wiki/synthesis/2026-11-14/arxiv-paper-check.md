---
title: arXiv Paper Check — AI & CTR (November 14, 2026)
type: synthesis
created: 2026-11-14
updated: 2026-11-14
sources:
  - http://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending
  - http://export.arxiv.org/api/query?search_query=cat:cs.IR&start=0&max_results=25&sortBy=submittedDate&sortOrder=descending
  - http://export.arxiv.org/api/query?search_query=all:%22click-through+rate%22+OR+all:CTR+OR+all:%22click+through+rate%22&start=0&max_results=20&sortBy=submittedDate&sortOrder=descending
tags:
  - arxiv
  - daily-check
  - ai
  - ctr
  - recommendation
  - ads
  - retrieval
  - agents
  - llm
  - multimodal
  - daily-digest
---

# arXiv Paper Check — AI & CTR (November 14, 2026)

> **Window note:** Queried on **2026-11-14** via arXiv API feeds for `cs.AI`/`cs.LG`, `cs.IR`, and CTR/click-through-rate keyword search (sorted by submission date). At query time the newest visible submissions were primarily dated **2026-11-12** (e.g. `2611.173xx`), with no clearly newer 2026-11-13/14 batch returned in these feeds. This report therefore curates the most interesting **recent** papers from the latest available window rather than a strictly verified last-24-hours set. All metrics and claims below are **author-reported** from abstracts/metadata unless noted; affiliations are included when explicitly present in arXiv metadata.

## Highlights

| Area | Pick | Why it matters |
|------|------|----------------|
| Multimodal LLM vision encoding | **Unbundling Multimodal Vision Encoding** (2611.17334) | Controlled study disentangles visual prior, dedicated vision capacity, and pre-fusion placement, suggesting jointly trained in/backbone-early vision capacity can rival pretrained encoders. |
| LLM architecture research process | **ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research** (2611.17332) | Proposes a public platform/workflow for documenting architectural experiments and using scaling-law predictions to evaluate ideas before large-scale training. |
| Coding agents & memory | **CoReMem: Cost-Internalizing Memory for Successive Coding Tasks** (2611.17316) | Introduces prospective segment valuation and provenance-gated credit so coding agents decide what memory to write/use based on measured next-task value and cost. |
| Semi-supervised ML agents | **AgentSSL: Can MLE Agents Leverage Unlabeled Data?** (2611.17323) | Frames SSL as program search for MLE agents; agents can exceed strong human-engineered SSL baselines in several settings but program selection remains a bottleneck. |
| LLM reasoning efficiency | **Classical Energies Learn to Reason 1,000x Faster than Looped Models** (2611.17309) | Recasts puzzle reasoning as energy descent (CRAM), reporting very fast training and high accuracy on Sudoku-Extreme/Maze-Unique with large compute savings vs looped models. |
| RLVR / verification asymmetry | **Negative-Only Policy Optimization for One-Sided Verifiable Rewards** (2611.17287) | Targets settings where failures are reliably verifiable but successes may be false positives, updating only on trusted negatives to avoid rewarding shortcut solutions. |
| Recommendation/CTR-adjacent ranking | **Sheaf-Inspired Structured Scoring Extensions of LightGCN for Collaborative Filtering** (2611.17226) | Studies structured pair-dependent scoring on top of LightGCN; shows modest ranking changes and sometimes large coverage shifts, with careful framing that results do not establish causal sheaf-geometry benefits. |
| CTR/ads training-serving alignment | **Serving-Aligned Entire-Space Conversion Modeling via Click-Through Rate Knowledge Distillation** (2611.15137) | Distills logged serving pCTR into ESMM’s auxiliary tower to reduce pCTR/pCTCVR mismatch, reporting AUC/PR-AUC gains for serving pCTCVR and pCVR on Ali-CCP. |

## 1) AI, LLMs, Agents & Reasoning

### Unbundling Multimodal Vision Encoding
- **Authors:** Ellis Brown, Chris Hoang, Shengyi Qian, Shang-Wen Li, Mike Lewis, Marjan Ghazvininejad, Luke Zettlemoyer, Lucas Beyer, Mengye Ren, Jakob Verbeek, Saining Xie, Hu Xu
- **arXiv:** [2611.17334](https://arxiv.org/abs/2611.17334) (submitted 2026-11-12; cs.CV/cs.LG)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Separates three intertwined design choices in multimodal vision encoding: upstream visual prior, dedicated vision capacity, and pre-fusion vs in-fusion placement.
  - Runs controlled from-scratch pretraining comparisons on common data at matched lifetime compute to isolate each factor.
  - Compares pretrained encoders, jointly trained encoders, encoder-free enlarged backbones, and early in-fusion vision modules.
- **Reported results:** A jointly trained encoder can match a pretrained encoder; dedicated vision capacity matters more than a pretrained visual prior; in-fusion vision modules placed early can perform comparably to pre-fusion encoders and may reduce time to first token (author-reported).

### ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research
- **Authors:** Jie Wang, Tong Zhu, JiaHao Kuang, Zhe Xu, Yunkai Chai, Dehong Zheng, Yu Cheng, Tao Ji, ZhouHan Lin, Qi Zhang, Bowen Zhou
- **arXiv:** [2611.17332](https://arxiv.org/abs/2611.17332) (submitted 2026-11-12; cs.CL/cs.LG)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Introduces ArchSpace as a public platform for recording proposals/experiments, community review, and referencing architectural ideas over time.
  - Aims to make negative/abandoned directions and reasoning more visible than typical industrial reports.
  - Uses scaling-law prediction from smaller experiments to triage ideas before expensive large-scale training.
- **Reported results:** Provides initial baselines/references (including Qwen3.5 and OLMo3 baselines, fitted scaling laws, reusable recipe) as a starting point for the platform (author-reported).

### CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation
- **Authors:** Peiwen Li, Harshit Verma, Sophia Zhou, Haiwen Wang, Ngoc Bui, Heng Chang, Fei Fei, David van Dijk, Rex Ying
- **arXiv:** [2611.17316](https://arxiv.org/abs/2611.17316) (submitted 2026-11-12; cs.AI/cs.CL/cs.SE)
- **Affiliations:** Yale University; Tsinghua University; Goodvision AI (from arXiv metadata).
- **Key contributions:**
  - Proposes CoReMem for successive coding tasks on evolving repositories, where memory must be chosen before the next task is known.
  - Uses prospective segment valuation to measure next-task value of trajectory segments and builds compact anchor-based memory (locations/checks).
  - Adapts the actor with on-policy memory-value estimates and provenance-gated value credit, balancing resolution and step/token costs.
- **Reported results:** On ChainSWE, raises a 27B actor’s resolve rate from **21.0% to 25.7%** with **17% fewer steps** and **11% fewer total cache-aware tokens** (including memory-module calls) versus the untrained actor without memory.

### AgentSSL: Can MLE Agents Leverage Unlabeled Data?
- **Authors:** Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun
- **arXiv:** [2611.17323](https://arxiv.org/abs/2611.17323) (submitted 2026-11-12; cs.AI/cs.LG) — *NeurIPS 2026 (per metadata comment)*
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Formulates agentic semi-supervised learning as program search under scarce labels and abundant unlabeled data.
  - Studies how MLE agents combine/adapt established SSL techniques rather than only supervised pipelines.
  - Introduces ProgramSelectBench (16,977 agent-generated and human-engineered SSL programs) to analyze program selection bottlenecks.
- **Reported results:** Exceeds strongest human-engineered baselines in **8 of 12** settings by up to **+21.8%** under weak feedback/matched compute; performance can drop by as much as **47%** when selecting programs via the agent’s feedback metric.

### Classical Energies Learn to Reason 1,000x Faster than Looped Models
- **Authors:** Benjamin Hoover, Hugh Blayney, James C. R. Whittington
- **arXiv:** [2611.17309](https://arxiv.org/abs/2611.17309) (submitted 2026-11-12; cs.AI/cs.LG)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Revives a learned Hopfield-&-Tank-style energy (CRAM) for constraint-satisfaction reasoning puzzles.
  - Highlights energy-descent benefits: early stopping, adaptive compute, training without differentiating through a solver, and interpretable constraint weights.
  - Positions results as both a promising direction for learned reasoning and a caution about over-interpreting trivially solvable benchmarks.
- **Reported results:** **99.996%** on Sudoku-Extreme and **100%** on Maze-Unique after **42 ms** and **132 ms** of training on one GPU (author-reported), with at least **1,000×** faster training than compared looped models and large inference-FLOP reductions in matched settings.

### Negative-Only Policy Optimization for One-Sided Verifiable Rewards
- **Authors:** Jiacheng Xu, Shuo He, Fuxiang Zhang, Chaojie Wang, Bo An
- **arXiv:** [2611.17287](https://arxiv.org/abs/2611.17287) (submitted 2026-11-12; cs.LG/cs.CL) — *NeurIPS 2026 Spotlight (per metadata comment)*
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Formalizes one-sided verifiability (OSV): verified negatives are reliable, but “verified” positives may be non-falsified false positives.
  - Proposes NOPO, which treats verified positives as unlabeled and suppresses only trusted verified negatives.
  - Combines reference-relative negative suppression with a group-level adapter scaled by the proportion of non-falsified responses.
- **Reported results:** Improves pass@k over baselines across unit-test, constraint-check, and LLM self-verifier settings on code, logic, and math benchmarks when oracle rewards are unavailable, with gains persisting under inference-time scaling and cross-benchmark transfer.

## 2) CTR, Recommendation & Retrieval

### Sheaf-Inspired Structured Scoring Extensions of LightGCN for Collaborative Filtering
- **Authors:** Ksenia Belkovskaya, Timur Lidzhiev, Maria Stebliy, Alexander Tarakanov
- **arXiv:** [2611.17226](https://arxiv.org/abs/2611.17226) (submitted 2026-11-12; cs.IR/cs.CE/cs.CG/cs.LG)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Adds structured, pair-dependent scoring modules on top of a fixed 3-layer LightGCN backbone (identity, diagonal, rank-one, full residual, and parameter-matched residual MLP).
  - Evaluates on Amazon-Book, Gowalla, MovieLens-1M, and Yelp2018 with ranking quality and catalog coverage at @10/@20.
  - Explicitly distinguishes geometric inspiration from implementation: no cellular sheaf construction or sheaf-Laplacian diffusion is performed.
- **Reported results:** Modest, dataset-dependent ranking changes and sometimes substantial coverage changes; authors caution that experiments do not establish a causal benefit from sheaf geometry.

### Serving-Aligned Entire-Space Conversion Modeling via Click-Through Rate Knowledge Distillation
- **Authors:** Pavel Dolin, Xun Zou, Jiatian Wu, Deguang Kong
- **arXiv:** [2611.15137](https://arxiv.org/abs/2611.15137) (submitted 2026-11-11; cs.LG)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Addresses ESMM training-serving mismatch where the deployed pCVR tower is paired at serving with a separately trained pCTR model, causing pCTCVR misalignment.
  - Uses knowledge distillation from logged serving pCTR scores to supervise ESMM’s auxiliary pCTR tower (KD-α variants).
  - Evaluates both full-data and negative-downsampling settings on Ali-CCP.
- **Reported results:** Best serving-pCTCVR variant (KD-0.3) increases ROC-AUC for serving pCTCVR and pCVR by **2.1%** and **1.6%**, and PR-AUC by **9.9%** and **8.8%** versus ESMM; downsampled KD-0.3 also improves mean AUC/PR-AUC over downsampled ESMM.

### CTR/Rec context from the latest visible window
- **When Does a Recommendation Spark Curiosity? Theory, Measurement, and Field Evidence** ([2611.14938](https://arxiv.org/abs/2611.14938), 2026-11-11): formalizes curiosity into a computable measure and reports offline gains plus online A/B increases in CTR, video views, and time spent at a major Asian video-streaming platform (author-reported). This item also appeared in recent wiki digests; included here as a key CTR/recommendation signal in the latest feed.
- **Keyword-search note:** Broad CTR keyword queries can surface non-recommender papers using “CTR” in other domains (e.g. detector coincidence time resolution in [2611.15820](https://arxiv.org/abs/2611.15820)); such results were excluded from the recommendation/ads summary above.

## Notes & Caveats
- **Timing:** `websearch` was unavailable, so discovery relied on arXiv API feeds. The strict “last 24 hours” window could not be confirmed; newest retrieved submissions were mostly from 2026-11-12 at query time.
- **Selection:** Curated for relevance/interest across requested AI and CTR categories; not exhaustive.
- **Verification:** Metrics, venues, deployment claims, and affiliations should be confirmed from PDFs/author pages before formal citation. Some items are abstract/metadata-level summaries.
- **Active preference file:** `EXTEND.md` (repo root).