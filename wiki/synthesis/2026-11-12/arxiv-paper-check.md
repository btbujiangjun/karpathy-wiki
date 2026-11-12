---
title: arXiv Paper Check — AI & CTR (November 12, 2026)
type: synthesis
created: 2026-11-12
updated: 2026-11-12
sources:
  - http://export.arxiv.org/api/query
  - https://arxiv.org/
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
  - rl
  - daily-digest
---

# arXiv Paper Check — AI & CTR (November 12, 2026)

> **Window note:** Queried on **2026-11-12** via arXiv API (`cs.AI`, `cs.LG`, `cs.IR`, and keyword search for `"click-through rate"` / `CTR`, sorted by submission date). At query time the latest retrieved submissions in these feeds were primarily dated **2026-11-10** (e.g. IDs around `2611.14xxx`–`2611.13xxx`), with no clearly visible 2026-11-11/12 batch in the returned results. This report curates the most interesting **recent** AI and CTR/recommendation/ads papers from that latest available window. All results and metrics below are **author-reported** unless noted.

## Highlights

| Area | Pick | Why it matters |
|------|------|----------------|
| CTR / A/B experimentation | **Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation in Recommendation Systems** (2611.13539) | Shows modern rec models exhibit feature-invariant scaling; predicts full-scale A/B effects from small-scale runs with confidence intervals, enabling efficient filtering of neutral/regressive changes. |
| RecSys explanations | **From Counterfactual Edits to Human Narratives: LLM-Driven Interpretations for Recommender System Explanations** (2611.13914) | Uses LLMs to summarize long counterfactual edit lists into coherent natural-language explanations; DPO improves semantic quality; evaluated with human-calibrated metrics. |
| Multimodal recommendation | **LUMIR: Decoupled Multimodal Representation Learning from Heterogeneous Data for Next-POI Recommendation** (2611.14004) | Decouples multimodal representation learning from downstream optimization via contrastive learning over unified text representations; improves across multiple sequential backbones. |
| Multimodal recommendation | **A Technique to Model Product Information and User Reviews (MPIUR)** (2611.13361) | Unifies item text, images, and user reviews in heterogeneous graphs with interaction-density-aware alignment; strong gains on sparse items. |
| Table retrieval for Text-to-SQL | **FERN: Cross-Benchmark Table Retrieval for Text-to-SQL with Frozen Retrievers and Learned Ranking** (2611.14477) | Fuses frozen retrievers + feature-engineered LightGBM ranker; strong cross-benchmark recall with low latency and no generative LLM calls. |
| Agent evaluation | **Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents** (2611.14493) | Compares trace-based LLM judging, text-only judging, and deterministic heuristics; shows complementary functional/security evaluation and high trace-based F1 (0.90). |
| Agent workflows | **ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows** (2611.14492) | Extracts conditions from agent reasoning/traces to compile SOPs into executable workflows; near-agent completion at lower cost/latency with repair. |
| Foundation models (bio) | **Emergent Biological Capabilities in a Foundation Model for Molecular Interactions** (2611.14504) | Bonbon shows zero-shot emergent capabilities (MoA, binding site localization, covalent/non-covalent) at scale; strong prospective wet-lab hit rate. |

## 1) CTR, Recommendation, Advertising & Retrieval

### Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation in Recommendation Systems
- **Authors:** Zhiliang Chen, Sammy Nammari, Jiahao Su, Xiaoqiang Luo
- **arXiv:** [2611.13539](https://arxiv.org/abs/2611.13539) (submitted 2026-11-10; cs.IR/cs.LG)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Demonstrates **feature-invariant scaling**: performance changes from different feature/architecture changes follow predictable scaling laws relative to a baseline.
  - Introduces a method combining scaling laws with statistical inference to predict full-scale A/B effects (with confidence intervals) from small-scale experiments.
  - Validated on Wukong, HSTU, and LLM-based rec models across 40+ changes; identifies improvements to SOTA on MovieLens-20M.
  - **Reported results:** Accurately distinguishes beneficial/neutral/regressive changes using a fraction of full-scale compute.

### From Counterfactual Edits to Human Narratives: LLM-Driven Interpretations for Recommender System Explanations
- **Authors:** Vojtech Cahlik, Amir Reza Mohammadi, Rodrigo Alves, Pavel Kordik, Eva Zangerle
- **arXiv:** [2611.13914](https://arxiv.org/abs/2611.13914) (submitted 2026-11-10; cs.AI/cs.IR)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Addresses long, low-level counterfactual edit lists by using LLMs to summarize them into higher-level natural-language explanations of preference patterns.
  - Optimizes mediators via preference optimization for correctness, informativeness, and linguistic quality.
  - **Reported results:** High linguistic quality across generators/models; DPO improves semantic metrics in most settings; best semantic results with high-success CFX methods (ACCENT, SPINRec).

### LUMIR: Decoupled Multimodal Representation Learning from Heterogeneous Data for Next-POI Recommendation
- **Authors:** Zehui Wang, Wolfram Höpken, Dietmar Jannach
- **arXiv:** [2611.14004](https://arxiv.org/abs/2611.14004) (submitted 2026-11-10; cs.IR/cs.LG/cs.MM)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Decouples multimodal representation learning from downstream model optimization using contrastive learning.
  - Unifies heterogeneous multimodal data into shared text space via LLMs, with interaction-aware fusion and sequential-signal constraints.
  - **Reported results:** Consistently outperforms multimodal fusion baselines in accuracy and beyond-accuracy metrics across multiple sequential backbones.

### A Technique to Model Product Information and User Reviews (MPIUR)
- **Authors:** Emna Belguith, Fajrian Yunus, Talel Abdessalem
- **arXiv:** [2611.13361](https://arxiv.org/abs/2611.13361) (submitted 2026-11-09; cs.AI/cs.IR)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Graph-based multimodal recommender encoding reviews in heterogeneous graphs, aligning image/text, with collaborative-semantic alignment adapted to interaction density.
  - **Reported results:** Best global nDCG@10/Recall@10 on Amazon Reviews 2023 Musical Instruments and Baby; best on sparse items.

### FERN: Cross-Benchmark Table Retrieval for Text-to-SQL with Frozen Retrievers and Learned Ranking
- **Authors:** Arjun Rao, Nishant Gopinath
- **arXiv:** [2611.14477](https://arxiv.org/abs/2611.14477) (submitted 2026-11-10; cs.IR/cs.CL)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Fuses three frozen retrievers into candidates, featurizes with ~120 features, re-ranks with LightGBM fitted once on BIRD.
  - **Reported results:** Strong cross-benchmark performance (Spider/BIRD/BEAVER/Fiben) with ~208ms latency per question and no hosted LLM calls.

## 2) Core AI, LLMs & Agents

### Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents
- **Authors:** Howard Zhang, Chuck Arvin, Logan Brown, Mihir Bhatia, Neelu Choudhary, Lily Miao
- **arXiv:** [2611.14493](https://arxiv.org/abs/2611.14493) (submitted 2026-11-10; cs.AI/cs.CL/cs.LG/cs.SE)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Three-phase study of trace-based LLM judging, text-only LLM judging with red-teaming, and deterministic heuristics on frozen traces.
  - **Reported results:** 97% of configs stable; trace-based achieves best precision-recall balance (F1=0.90); functional and security evaluation complementary, uncovering 24 novel failures with zero overlap.

### ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows
- **Authors:** Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta, Carlos D. Castillo, Prathap Ramachandra, Xiaofan Jiang, Francesco Carbone
- **arXiv:** [2611.14492](https://arxiv.org/abs/2611.14492) (submitted 2026-11-10; cs.AI/cs.LG/cs.MA)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Extracts conditions from agent reasoning (not just tool calls), merges across runs into compact rule docs, compiles to executable workflows per platform.
  - **Reported results:** 93.8% completion vs 96.8% for agent at 24% lower cost on production SOPs; strong results on τ²-Bench and SOP-Bench with repair.

### Emergent Biological Capabilities in a Foundation Model for Molecular Interactions
- **Authors:** Adi Mashiach et al.
- **arXiv:** [2611.14504](https://arxiv.org/abs/2611.14504) (submitted 2026-11-10; cs.LG/q-bio.BM)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Bonbon trained on ~3.2T tokens of paired protein-ligand sequences with no task supervision/structures.
  - Emergent zero-shot capabilities: mechanism of action, binding site localization (orthosteric/allosteric), and covalent vs non-covalent engagement; generalize OOD.
  - **Reported results:** State-of-the-art binding/affinity prediction at 5 orders of magnitude speed vs co-folding; prospective wet-lab hit rate 61.5% across 9 disease targets yielding structurally novel inhibitors.

### A Theory of Policy Optimization in Post-Training: Coverage Collapse and Reference Resets
- **Authors:** Audrey Huang, Nan Jiang, Sham M. Kakade, Sadhika Malladi, Akshay Krishnamurthy, Dylan J. Foster
- **arXiv:** [2611.14467](https://arxiv.org/abs/2611.14467) (submitted 2026-11-10; cs.LG/stat.ML)
- **Affiliations:** Not specified in arXiv metadata reviewed.
- **Key contributions:**
  - Shows REINFORCE/PPO/GRPO can suffer **coverage collapse** (probability of optimal responses → near zero) despite improving reward.
  - Proposes **reference resets** (resetting KL reference to recent policy) via Approximate Policy Mirror Descent (APMD).
  - Establishes coverage-preserving global convergence guarantees for stylized PPO/GRPO variants and squared-loss implementations.

## Notes
- All metrics are author-reported from abstracts. Affiliations are largely not specified in the reviewed arXiv metadata.
- The "last 24 hours" window was not fully satisfied at query time due to arXiv indexing/announcement timing; this is a recent-window curation consistent with the wiki's daily check format.
