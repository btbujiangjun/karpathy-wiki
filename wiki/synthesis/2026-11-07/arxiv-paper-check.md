---
title: arXiv Paper Check — AI & CTR (November 7, 2026)
type: synthesis
created: 2026-11-07
updated: 2026-11-07
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
  - generative-recommendation
  - reranking
  - retrieval
  - agents
  - reasoning
  - llm
---

# arXiv Paper Check — AI & CTR (November 7, 2026)

> **Window note:** The user requested papers from the "last 24 hours." As checked on 2026-11-07 10:20 CST, arXiv API queries (`cs.AI`/`cs.LG`/`cs.CL`/`cs.IR`, sorted by submission date, plus CTR/click-through keyword search) show the latest announced submissions primarily from **2026-11-05** (with CTR-specific recent hits including **2026-11-03**). A `submittedDate` filter for 2026-11-06–2026-11-07 returned no results at query time, consistent with arXiv announcement timing. This report curates the most interesting **recent** AI and CTR/recommendation/ads papers from that latest available window.

## Highlights

| Area | Pick | Why it matters |
|------|------|----------------|
| AI agents / optimization | **SwarmEvolve** (2611.08483) | Latent-space agent swarms + KV-cache crossover; reports much faster evolutionary program search. |
| CTR / ads / retrieval | **ReuseGR** (2611.04259) | Decouples large-model query planning from lightweight personalized completion for generative retrieval in search ads; reports online CTR/revenue gains. |
| Generative recommendation | **BRIDGE** (2611.07425) | Targets the semantic quantization gap in SID-based generative rec; reports offline gains and online eCPM lift. |
| Industrial ranking / ads mix | **OneTrans-GSR** (2611.04720) | Unifies reranking + mix-ranking as one autoregressive slate generator; reports GMV/advertiser/repurchase gains with lower latency. |
| Re-ranking / behavior modeling | **ICE/JBM** (2611.07591) | Models display→impression→click as a browsing journey; Taobao A/B reports click and revenue lifts. |
| Test-time reasoning | **StepBack** (2611.08403) | Localizes likely first CoT error and resamples suffixes; matches self-consistency accuracy with fewer tokens. |
| Productivity agents | **Agent-R²** (2611.08219) | Real-source task synthesis + rubric-based RL; small model reportedly beats much larger baseline on productivity benchmarks. |
| CTR tooling / evaluation | **NumEmbBench** (2611.01090) | Benchmark/taxonomy for numerical embeddings in CTR prediction with a unified FuxiCTR interface. |

## 1) CTR, Recommendation, Advertising & Retrieval

### ReuseGR: Offline--Online Decoupled Generative Retrieval via Adaptive Prefix Reuse
- **Authors:** Xujing Wang, Yufeng Chen, Boxuan Zhang, Chao Wei, Cai Xu, Jie Zhao, Weiru Zhang, Wei Zhao, Ziyu Guan
- **arXiv:** [2611.04259](https://arxiv.org/abs/2611.04259) (submitted 2026-11-03)
- **Categories:** cs.IR
- **Affiliations:** Not specified in arXiv metadata excerpt reviewed.
- **Key contributions:**
  - Splits generative retrieval into a **7B offline planner** that produces shared SID prefix sets per query and a **0.5B online model** that uses request history to select prefixes and complete remaining tokens.
  - **ReuseCut** chooses per-query cache depth to balance computation reuse and candidate coverage; **Path KD** transfers suffix-scoring knowledge from 7B to 0.5B.
  - **BudgetCut** (initialized by OPD, refined by GRPO) selects branches under a fixed budget for final top-100 recall.
  - **Reported results (author-reported):** on an industrial search-advertising dataset (~2M query-item records, 3.38M catalog items), query-level HR@100 +3.83 pp and mean online latency -38.9% vs all-online 0.5B (when prefixes prepared); HR@100 comparable to all-online 7B with 57.7% lower online latency. 14-day user-level A/B: CTR +0.93%, revenue per thousand requests +1.05%.

### BRIDGE: Bridging the Semantic Quantization Gap for Generative Recommendation
- **Authors:** Yatong Xiao, Mingjie Sun, Peng Wang, Wenjin Wu, Peng Jiang
- **arXiv:** [2611.07425](https://arxiv.org/abs/2611.07425) (submitted 2026-11-05)
- **Categories:** cs.IR
- **Affiliations:** Not specified in arXiv metadata.
- **Key contributions:**
  - Identifies a **Semantic Quantization Gap (SQG)** in SID-based generative recommendation: discrete SIDs lose codebook-centroid, neighborhood, and difficulty information.
  - **Codebook-grounded latent reasoning** injects frozen RQ-VAE centroids as semantic anchors before SID generation.
  - **Privileged EMA self-distillation** transfers neighborhood-aware knowledge to an on-policy student, preserving inter-item geometry and mitigating exposure bias.
  - **Effort-aware recurrence** allocates more computation to early/harder SID levels.
  - **Reported results:** +10.9% Recall@10 and +9.7% NDCG@10 average over strongest baseline across three Amazon benchmarks (up to +12.6%/+10.7%); one-week online A/B on a large-scale e-commerce advertising platform (5% traffic): eCPM +0.65%.

### OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking with One Autoregressive Transformer
- **Authors:** Feng Cheng, Yu-Hsuan Huang, Fengyi Wang, Chaofan Zhou, Zhennan Zhu, Huan He, Bo Zhang, Ruoqi Zhang, Zhanfeng Mo, Ziwei Liu, Lanyi Li, Yifeng Pan, Junhua Long, Ziqiu Zhou, Yue Lin, Shaowei Liu
- **arXiv:** [2611.04720](https://arxiv.org/abs/2611.04720) (submitted 2026-11-03)
- **Categories:** cs.IR
- **Affiliations:** Not specified in arXiv metadata.
- **Key contributions:**
  - Replaces separate reranking and mix-ranking rules/models with a **single decoder-only autoregressive policy** that generates the full exposure slate (products, short videos, livestreams, advertising cards).
  - Uses a **reward model over complete slates** plus reinforcement learning for slate-level/long-term objectives, with explicit **constraint-aware decoding** for business rules.
  - **Reported results:** slate quality improves with reward/policy compute; deployed in a large-scale industrial recommendation system. Online A/B: GMV/u +2.63%, advertiser value +2.06%, repurchase +2.03%, end-to-end reranking+mix-ranking latency -13%.

### Beyond Independent Predictions: Learning the Browsing Journey for Sequence-Level Re-ranking
- **Authors:** Jiayi Zhang, Jingxin Hai, Zhenjia Ma, Hongbin Pei, Dagui Chen, Han Zhu, Jian Xu
- **arXiv:** [2611.07591](https://arxiv.org/abs/2611.07591) (submitted 2026-11-05)
- **Categories:** cs.IR
- **Affiliations:** Not specified in arXiv metadata.
- **Key contributions:**
  - Argues standard Independent Behavior Modeling (per-item CTR/utility) ignores that clicks require exposure and items compete for finite attention.
  - Proposes **Joint Behavior Modeling (JBM)** for display→impression→click and implements **Impression-Click Evaluator (ICE)**: browsing-depth/impression estimation, suppression of unexposed-item context, and click distribution matching.
  - **Reported results:** offline gains across backbones; 14-day Taobao App A/B: clicks +0.70%, revenue +3.67%; full-traffic deployment.

### SPADE: Spatiotemporal Preference Alignment and Diversity Enhancement for Local Search
- **Authors:** Chenxu Wang, Wenxuan Yang, Yueqi Mou, Shuxian Bi, Biao Tang, Peng Yan
- **arXiv:** [2611.04662](https://arxiv.org/abs/2611.04662) (submitted 2026-11-03)
- **Categories:** cs.IR
- **Affiliations:** Not specified in arXiv metadata.
- **Key contributions:**
  - End-to-end generative query recommendation for local search with open-set vocabulary and spatiotemporal constraints.
  - **OA-BPE** aligns subword merges with business-value signals for long-tail queries; **STAR** uses continuous multi-scale spatiotemporal encodings; **MARS-DPO** aligns to production impression-click data with composite rewards/adaptive hard negatives; **SDBS** improves slate diversity.
  - **Reported results:** offline HR@5 +5.6%, GeoC@5 -40.3%, Exec@5 +1.9% vs strongest generative baseline; one-week online A/B: module CTR +1.88%, search volume +0.177%, search DAU +0.105%.

### Numerical Embeddings for CTR Prediction: A Taxonomy, Unified Benchmark, and Open-Source FuxiCTR Extension
- **Authors:** Heng Yao, Hanwei Zhu, Tianying Liu, Yulou Shu, Siyun Hou
- **arXiv:** [2611.01090](https://arxiv.org/abs/2611.01090) (submitted 2026-10-31)
- **Categories:** cs.IR
- **Affiliations:** Not specified in arXiv metadata.
- **Key contributions:**
  - Introduces **NumEmbBench**, an open benchmark for numerical embeddings in CTR prediction; classifies 18 configurations into six mechanism-based families.
  - Evaluates under one **FuxiCTR** interface across 3 datasets, 9 backbones, 5 seeds with equal-budget tuning and shared train-only z-score protocol.
  - Finds no single universal winner (DEER best mean rank, but 6 methods lead at least one setting); native-scale tests and paired latency show accuracy/cost tradeoffs are not aligned.

## 2) Core AI, LLMs & Agents

### SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization
- **Authors:** Qile Jiang, George Em Karniadakis
- **arXiv:** [2611.08483](https://arxiv.org/abs/2611.08483) (submitted 2026-11-05)
- **Categories:** cs.AI, cs.NE
- **Affiliations:** Not specified in arXiv metadata (George Em Karniadakis is widely associated with Brown University; not asserted from this feed).
- **Key contributions:**
  - Runs hundreds of low-cost agents in swarms that **reason in latent space** (no text decoding per step) and exchange information via **KV-cache passing/crossover**.
  - Uses a novelty filter in hidden-state space to preserve diverse candidate ideas.
  - **Reported results:** on 21 mathematical discovery/scientific computing problems, highest average score; median 3–8 minutes to reach best scores other SOTA frameworks reach in ~60 minutes. On some problems, SwarmEvolve with Qwen3 8B reportedly improves on solutions AlphaEvolve found with frontier LLMs.

### StepBack: Step-Level Error-Localized Resampling for Efficient Test-Time Reasoning
- **Authors:** Yang Ouyang, Jung-Eun Kim
- **arXiv:** [2611.08403](https://arxiv.org/abs/2611.08403) (submitted 2026-11-05)
- **Categories:** cs.AI, cs.CL, cs.LG
- **Comment:** NeurIPS 2026 (per arXiv comment)
- **Affiliations:** Not specified in arXiv metadata.
- **Key contributions:**
  - Improves over full-trajectory self-consistency by **localizing the likely first error step** in draft CoT trajectories using lightweight signals.
  - **Resamples only the detected error step and suffix**, then applies majority voting.
  - **Reported results:** matches self-consistency accuracy on average across 7 math reasoning/multi-hop QA benchmarks while reducing token usage by up to 41.26%; composable with adaptive inference methods.

### Agent-R²: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis
- **Authors:** Teng Pan, Zixuan Wang, Yuchen Yan, Qifei Wu, Yao Chen, Yingqi Qu, Ruiqing Zhang, Yongliang Shen
- **arXiv:** [2611.08219](https://arxiv.org/abs/2611.08219) (submitted 2026-11-05)
- **Categories:** cs.CL
- **Affiliations:** Not specified in arXiv metadata.
- **Key contributions:**
  - Addresses missing post-training data for realistic productivity agents by synthesizing tasks from **occupational seeds, corpus-derived workflow evidence, and authentic web-sourced multi-format files**.
  - Distills ~4k task instances with **deliverable-level rubrics**; trains with SFT + **rubric-based RL**.
  - **Reported results:** Agent-R²-4B (trained on 4k instances) surpasses Qwen3-235B-A22B-Thinking-2507 on GDPval (51.0% vs 48.0%) and OfficeQA (14.8% vs 13.8%); analysis suggests reduced shortcut behavior and more grounded/verified deliverables.

### FedReason: Large Language Models as Weight-Space Meta-Aggregators for Heterogeneous Federated Learning
- **Authors:** Ali Mohammadi Ruzbahani, Abbas Yazdinejad, Hadis Karimipour
- **arXiv:** [2611.08383](https://arxiv.org/abs/2611.08383) (submitted 2026-11-05)
- **Categories:** cs.CR, cs.AI
- **Affiliations:** Not specified in arXiv metadata.
- **Key contributions:**
  - Uses an LLM as a **server-side meta-aggregator** that inspects client-model statistics in a restricted sandbox and emits a short Python aggregation program (with FedAvg fallback).
  - Preserves a privacy boundary: full weight tensors do not leave the server; LLM sees only printed analysis results and may score candidates on a 500-image proxy set.
  - **Reported results (168 runs, 14 baselines):** under Dirichlet label skew, +1.26 pp average over FedAvg across 12 paired runs; strong server-side rule on CIFAR-100 but below SCAFFOLD (which changes client training). With sign-flipping Byzantine clients, excluded malicious clients from first round; proxy feedback critical (73.8% → 38.8% in one seed without it). Reported API cost ~0.79 USD/60-round run.

### Don't Prompt Your Agents. Equip Them: Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution for Logical Systems
- **Authors:** Vladimiros Peilivanidis
- **arXiv:** [2611.07652](https://arxiv.org/abs/2611.07652) (submitted 2026-11-05)
- **Categories:** cs.AI, cs.SE
- **Affiliations:** ARPA Hellenic Logical Systems (as seen in arXiv metadata context).
- **Key contributions:**
  - Proposes **Skillware**: versioned capability bundles with typed JSON contracts, deterministic Python execution, directives, datasets, and unit tests, separating agent intent from execution.
  - Provides model-agnostic adapters that translate bundles into native tool declarations for cloud or local models.
  - **Reported results:** 23 models / 368 benchmark conditions; equipped 3B–8B local models reportedly outperform unequipped frontier models on complex workflows, with up to 84.8% token reduction, 97.3% inference-cost reduction, and elimination of parameter errors.

### Scientist World: Grow a Research World for AI-Scientists
- **Authors:** Taiming Lu, Sachin Konan, Zhuang Liu
- **arXiv:** [2611.08478](https://arxiv.org/abs/2611.08478) (submitted 2026-11-05)
- **Categories:** cs.AI, cs.CL, cs.LG
- **Affiliations:** Not specified in arXiv metadata.
- **Key contributions:**
  - Converts research papers into **executable environments** for AI scientists: extracts open-ended research questions and reproduces paper methods as baselines.
  - Releases 1,000 verified environments and 6,400 hours of research traces.
  - **Reported results:** frontier AI scientists surpass human researchers 74% of the time in their evaluation setting; training on the environment raises a small model (+158%) to match frontier models in research ideation.

## Cross-cutting Observations

1. **CTR/ads systems are moving toward slate-level and generative objectives.** ReuseGR, BRIDGE, OneTrans-GSR, ICE, and SPADE all treat ranking/retrieval as sequence/slate generation or browsing-journey modeling, and several report online A/B metrics (CTR, eCPM, GMV, advertiser value, latency).
2. **Efficiency is a first-class objective, not an afterthought.** Recent methods trade full decoding or full-trajectory sampling for latent communication (SwarmEvolve), suffix resampling (StepBack), prefix reuse (ReuseGR), compute-aware recurrence (BRIDGE), and deterministic capability execution (Skillware).
3. **Evaluation is becoming more operational.** NumEmbBench standardizes CTR numerical-embedding comparisons; industrial papers increasingly report latency, traffic percentage, and business metrics alongside offline recall/NDCG/AUC.
4. **Metadata is incomplete for very recent submissions.** Affiliations/company affiliations should be verified from PDFs, author pages, or later versions before citation in a formal setting.

## Caveats

- This is a **curated check**, not an exhaustive scan of all arXiv categories.
- All metrics above are **author-reported** unless independently reproduced.
- The "last 24 hours" constraint could not be satisfied exactly at query time due to arXiv announcement/indexing timing; the report uses the latest available announced/retrievable batch and labels it explicitly.
- A related synthesis for the same date exists at [arxiv-ai-search](arxiv-ai-search.md); this paper-check focuses on AI+CTR and selects a compact set of highlights.
