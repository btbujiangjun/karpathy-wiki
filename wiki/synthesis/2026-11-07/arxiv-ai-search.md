---
title: arXiv AI Research Paper Search Report — 2026-11-07
type: synthesis
created: 2026-11-07
updated: 2026-11-07
sources: [arxiv.org]
tags: [arxiv, AI, LLM, recommendation, advertising, CTR, sequential-modeling, games, generative-recommendation, agents, game-theory]
---

# arXiv AI Research Paper Search Report — 2026-11-07

**Generated**: 2026-11-07 | **Scope**: AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games
**Window**: arXiv `recent` listings for **Wed 4 Nov → Fri 6 Nov 2026** (cs.IR, cs.CL, cs.AI, cs.GT, cs.MA), plus targeted CTR/advertising searches for late-October items.

**Methodology**: The arXiv Export API returned empty/rate-limited responses during this run, so paper data was collected directly from the arXiv category listing pages (`/list/{cs.IR,cs.CL,cs.AI,cs.GT,cs.MA}/recent`), arXiv search result pages, and individual `/abs/` pages. Affiliations were parsed from the rendered `arxiv.org/html` author blocks and are **never inferred**; entries without a rendered affiliation are marked as such. All summaries are **abstract-only** — no PDF full text was read. Rankings are a curated selection, not an exhaustive sweep.

---

## At a Glance

| # | Area | Paper | Institution | Date | Link |
|---|------|-------|-------------|------|------|
| 1 | LLM | SpecCTMC: Exact Speculative Simulation of Diffusion LM CTMCs | Australian National University | 11-05 | [2611.08362](https://arxiv.org/abs/2611.08362) |
| 2 | LLM | Recursive Sparse Attention (RecSA) | UC San Diego / CMU | 11-04 | [2611.07232](https://arxiv.org/abs/2611.07232) |
| 3 | LLM | O²PD: Overlap-Gated On-Policy Distillation | Renmin University of China | 11-05 | [2611.07731](https://arxiv.org/abs/2611.07731) |
| 4 | LLM | Towards Foundation Decision Models: Drex | Nace.AI | 11-05 | [2611.07854](https://arxiv.org/abs/2611.07854) |
| 5 | Agents | Agent-R²: Real-Source Data Synthesis | Zhejiang University / Baidu | 11-05 | [2611.08219](https://arxiv.org/abs/2611.08219) |
| 6 | Rec | BRIDGE: Semantic Quantization Gap for Generative Recommendation | Kuaishou Technology | 11-04 | [2611.07425](https://arxiv.org/abs/2611.07425) |
| 7 | Rec | HARP: Dual-Profile Agentic Recommendation | HIT Shenzhen / Great Bay University | 11-03 | [2611.05319](https://arxiv.org/abs/2611.05319) |
| 8 | Rec | PMRecBench: Personalization under Multimodal Queries | University College London | 11-04 | [2611.06349](https://arxiv.org/abs/2611.06349) |
| 9 | Rec | CAP-Mix: Soft Prototype Mixtures for Generative Retrieval | Meta / Texas A&M | 11-04 | [2611.05799](https://arxiv.org/abs/2611.05799) |
| 10 | Ads | WISE: Agentic Whole-page Search Experience Attribution | Kuaishou Technology | 11-05 | [2611.06777](https://arxiv.org/abs/2611.06777) |
| 11 | Ads | EvoRec: Self-Evolving Agentic Recommender | Kuaishou Local Services Ads | 11-01 | [2611.01977](https://arxiv.org/abs/2611.01977) |
| 12 | Ads | Auxiliary Supervision for Ads Ranking Models | Meta Platforms | 10-31 | [2611.01280](https://arxiv.org/abs/2611.01280) |
| 13 | CTR | NumEmbBench: Numerical Embeddings for CTR | Ant Group | 10-31 | [2611.01090](https://arxiv.org/abs/2611.01090) |
| 14 | Seq | DESRec: Deliberate Latent Reasoning for Sequential Rec | Renmin University of China | 11-04 | [2611.06521](https://arxiv.org/abs/2611.06521) |
| 15 | Seq | ICE: Learning the Browsing Journey for Re-ranking | Alibaba (Taobao & Tmall) | 11-05 | [2611.07591](https://arxiv.org/abs/2611.07591) |
| 16 | Seq | OneLatent: Latent Reasoning for Foundation Rec | Kuaishou Technology | 10-21 (v2 11-02) | [2610.30675](https://arxiv.org/abs/2610.30675) |
| 17 | Games | Efficient Equilibrium Computation in Colonel Blotto | Technical University of Munich | 11-03 | [2611.05221](https://arxiv.org/abs/2611.05221) |
| 18 | Games | Polynomial-Time Extensive-Form Proper Equilibria | Ganzfried Research / Cornell | 11-04 | [2611.07089](https://arxiv.org/abs/2611.07089) |
| 19 | Games | AGiR: Mitigating Gift Over-Reliance in Mixed-Motive Games | KAIST | 11-02 | [2611.02875](https://arxiv.org/abs/2611.02875) |
| 20 | Games | Learning and Steering in Incomplete-Information Games | UIUC | 11-05 | [2611.07589](https://arxiv.org/abs/2611.07589) |

---

## 1. Large Language Models & Agents

### 1.1 SpecCTMC: Exact Speculative Simulation of Diffusion Language Model Continuous-Time Markov Chains
- **Authors**: Siva Rajesh Kasa, Yasong Dai, Sumit Negi, Hongdong Li
- **Institution**: School of Computing, Australian National University
- **Date**: 2026-11-05
- **arXiv**: https://arxiv.org/abs/2611.08362
- **Venue**: Preprint (28 pp.)

**Abstract**: Masked diffusion language models allow parallel text generation, but independently sampling multiple tokens disrupts dependencies and changes the output distribution. Exact continuous-time sampling avoids this approximation, yet normally needs one sequential model evaluation per token. SpecCTMC is a training-free speculative sampler that proposes successive token updates from previously computed predictions, evaluates intermediate states in parallel, and applies an exact acceptance-and-correction procedure. The authors prove it preserves the joint distribution of event times, generation order, and token values of the underlying CTMC.

**Key innovations**:
- **Exact speculative sampling without a draft model** — reuses the model's own cached predictions to propose multi-token updates.
- **Distribution-preserving acceptance/correction** — no time-discretization error and no extra parallel-factorization error.
- **1.73–4.38× fewer sequential model evaluations** on LLaDA-8B-Instruct and Dream-v0-Instruct-7B across five benchmarks while matching the reference sampling distribution.

---

### 1.2 Recursive Sparse Attention: Million-Token Length Extrapolation at Logarithmic Cost
- **Authors**: Ruitian Wang, Xinyu Yang, Minshen Zhang, Hao Zhang
- **Institution**: University of California, San Diego; Carnegie Mellon University
- **Date**: 2026-11-04
- **arXiv**: https://arxiv.org/abs/2611.07232
- **Venue**: Preprint (24 pp.)

**Abstract**: Dense attention is expensive at ~1M tokens, and long training documents are scarce. Most sparse attention methods score all preceding blocks/tokens, giving O(L) selection cost per query; hierarchical selection reduces this to O(log L), but prior trainable hierarchical methods only report accuracy within their training length. RecSA builds a tree over the KV cache in which each node summarizes its subtree with one key and one mean-pooled value. Each level selects at most k candidates, so each query has O(log L) selection cost and reads O(log L) entries. RoPE positions are assigned by candidate index at each level, keeping relative distances inside the training range.

**Key innovations**:
- **Logarithmic-cost hierarchical KV selection** with one shared per-layer pooler distilled from dense attention.
- **Length extrapolation by construction** — level-local positional indexing avoids out-of-range RoPE distances.
- Initialized from Qwen3-4B and trained on only 0.62B tokens at 32K length: **60.5 on RULER at 1M** vs 40.0 for the best baseline; **3.2× faster prefill and 3.8× faster decoding at 524K on one H200**.

---

### 1.3 O²PD: Overlap-Gated On-Policy Distillation on Reliable Prefix
- **Authors**: Shuaishuai Zu, Jihao Zhao, Pengfei Li, Guanghuan Fang, Ben Feng, Yuhan Liu, Biao Qin, Baochuan Yang
- **Institution**: School of Information, Renmin University of China
- **Date**: 2026-11-05
- **arXiv**: https://arxiv.org/abs/2611.07731
- **Venue**: Preprint

**Abstract**: On-policy distillation (OPD) supplies dense token-level supervision by aligning a student to the teacher's next-token distribution on its own rollouts. Existing top-k OPD applies reverse KL over the teacher's renormalized top-k support, but the teacher is scoring student-generated, off-policy rollouts, so the reliability of its next-token guidance is unclear; restricting to top-k also discards mass outside that support. O²PD asks *which tokens to align* and *how to align them*: it finds alignment on the student's trajectory prefix is more reliable than on the full context and therefore applies OPD only to the first 20% of prefix tokens.

**Key innovations**:
- **Reliability analysis of teacher supervision** on student rollouts → prefix-only alignment.
- **Diagnoses Teacher-support Uncovering and Dominant-Mode Mismatch** in top-k OPD.
- **Reset Support + Support Convergence + overlap-gated α-divergence** to interpolate per-token between mode-covering and mode-seeking behavior.

---

### 1.4 Towards Foundation Decision Models: Drex
- **Authors**: Nischay Dhankhar, Alisher Amantay, Zhanibek Datbayev, Darkhan Akhmetov, Yash Shah, Nurmukhamed Ubaidullayev, Raman Saparkhan, Dos Baha, Abulhair Saparov
- **Institution**: Nace.AI
- **Date**: 2026-11-05
- **arXiv**: https://arxiv.org/abs/2611.07854
- **Venue**: Technical report (51 pp.); open-weight models

**Abstract**: Autoregressive LLM approaches reach high accuracy but in production give inconsistent answers, require output parsing, and add cost/latency. Decision models instead return a probability distribution over user-supplied options without autoregressive decoding. Drex is a family of four open decision models — 8B (DLM), 9B (v1.5), 35B with 3B active (v2.0), and 27B (Max). A request consists of a state (document, record, or agent context, optionally images) plus questions asking for a choice, yes/no judgment, or ordered score. Training combines SFT with reinforcement learning from adjusted feedback (RLAF), plus vision tuning for Max.

**Key innovations**:
- **Non-autoregressive decision interface** returning calibrated option distributions, stable under option reordering.
- **RLAF + consistency losses** improve accuracy and robustness to option order.
- **Max: 67.52 on Decision Index 0.4.1** (vs 60.70 for Jev 1.14.0) and **183 ms** per typical request vs ~2.0 s (GPT-6 Sol) and ~3.5 s (Claude Opus 5.5).

---

### 1.5 Agent-R²: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis
- **Authors**: Teng Pan, Zixuan Wang, Yuchen Yan, Qifei Wu, Yao Chen, Yingqi Qu, Ruiqing Zhang, Yongliang Shen
- **Institution**: Zhejiang University; Baidu Inc.
- **Date**: 2026-11-05
- **arXiv**: https://arxiv.org/abs/2611.08219
- **Venue**: Preprint

**Abstract**: Agents still struggle with realistic productivity work, which requires long-horizon professional workflows, heterogeneous file contexts, and usable deliverables under fine-grained requirements. The bottleneck is scalable post-training data reflecting real work intent, authentic file environments, and deliverable-level evaluation. Agent-R² grounds synthesis in real occupational seeds, corpus-derived workflow evidence, and authentic web-sourced files. From 10k web-corpus candidates it distills 4k task instances pairing real multi-format attachments with fine-grained, deliverable-level rubrics.

**Key innovations**:
- **Real-source synthesis pipeline** instead of manually specified workflows or LLM-generated files.
- **Deliverable-level rubric RL** on top of SFT for file-grounded reasoning.
- **Agent-R²-4B beats Qwen3-235B-A22B-Thinking-2507** on GDPval (51.0% vs 48.0%) and OfficeQA (14.8% vs 13.8%) with only 4k training instances; also reduces "shortcut" deliverables.

---

## 2. Recommendation Systems

### 2.1 BRIDGE: Bridging the Semantic Quantization Gap for Generative Recommendation
- **Authors**: Yatong Xiao, Mingjie Sun, Peng Wang, Wenjin Wu, Peng Jiang
- **Institution**: Kuaishou Technology, Beijing, China
- **Date**: 2026-11-04
- **arXiv**: https://arxiv.org/abs/2611.07425
- **Venue**: Preprint

**Abstract**: Generative recommendation retrieves items by autoregressively generating Semantic IDs, where an RQ-VAE quantizes each item into a hierarchical SID sequence. The authors identify the **Semantic Quantization Gap**: quantization derives SIDs from rich continuous signals (codebook centroids, local neighborhood geometry, level-wise entropy), but the decoder receives only discrete identifiers. This causes a grounding gap (no semantic anchors when target-side information is limited), a neighborhood gap (token-level supervision discards inter-item similarity and worsens exposure bias), and a difficulty gap (uniform compute despite generation difficulty diminishing with depth).

**Key innovations**:
- **Codebook-grounded latent reasoning** injects frozen quantizer centroids as semantic anchors before SID generation.
- **Privileged EMA self-distillation** transfers neighborhood-aware knowledge from teacher to on-policy student.
- **Effort-aware recurrence** allocates more compute to early SID levels.
- **+10.9% Recall@10 / +9.7% NDCG@10** average on three Amazon benchmarks; **+0.65% eCPM** in a one-week online A/B on a large e-commerce advertising platform (5% traffic).

---

### 2.2 HARP: Training-Free Dual-Profile Agentic Communication for LLM-Based Recommendation
- **Authors**: Zhen Tao, Xun Zhou, Xuhui Chen, Ziyue Qiao, Qingqiang Sun
- **Institution**: Harbin Institute of Technology, Shenzhen; Great Bay University; Shenzhen Loop Area Institute
- **Date**: 2026-11-03
- **arXiv**: https://arxiv.org/abs/2611.05319
- **Venue**: NeurIPS 2026

**Abstract**: In LLM-based recommendation, memory acts as a user-level agent, but users and items are asymmetric: only the user gets a structured profile, it enters a bandwidth-limited reranker prompt, and it is frozen after warmup. The authors recast recommendation as agentic communication in four stages — BUILD a self-description, TRANSMIT it along the collaborative graph, UNDERSTAND the other side, and SYNC from the next interaction — and identify three missing pieces. HARP instantiates them as a training-free, three-operator addition to a frozen LLM backbone.

**Key innovations**:
- **Symmetric item profile** extracted by rules (zero extra LLM calls).
- **Channel-decomposable profile-level homophily** consumed at retrieval time rather than inside the reranker prompt.
- **Single-pass reflective in-context profile update** with no gradient step.
- **+6.9%–24.0% Hit@1** over the strongest published baseline on Yelp, Books, MovieTV, Goodreads (Holm-corrected p < 1e-9).

---

### 2.3 PMRecBench: A Benchmark for Personalization in Recommendation Agents under Multimodal Queries
- **Authors**: Xiaoyu Zhang, Yougang Lyu, Bin Wu, Sahan Bulathwela, Emine Yilmaz
- **Institution**: University College London, London, UK
- **Date**: 2026-11-04
- **arXiv**: https://arxiv.org/abs/2611.06349
- **Venue**: Preprint (13 pp.)

**Abstract**: Existing personalized recommendation benchmarks use text-only queries, while multimodal benchmarks assess query matching without evaluating personalization from real user histories. PMRecBench pairs 510 quality-controlled image-text queries across clothing and movies with the corresponding users' real histories. Queries are derived from consistent behavioral patterns in real user records, with reference images and targets linked to actual interactions. Diagnostic pools include items rated highly by the user but violating requirements, and items satisfying requirements but never rated highly.

**Key innovations**:
- **First benchmark for personalization under multimodal queries** with real user histories.
- **Two-sided diagnostic pools** separately test requirement understanding and preference following.
- Reveals a **personalization imbalance**: adding multimodal queries improves overall ranking but weakens preference following, because agents prioritize resemblance to reference images over user-history evidence; stronger backbones alone do not fix it.

---

### 2.4 Item Representations Matter: Bridging Hard Semantic IDs and Soft Prototype Mixtures for Generative Retrieval
- **Authors**: Vicente Balmaseda, Dongqi Fu, Jiarui Feng, Ren Chen, Hanqing Zeng, Tianxin Wei, Yinglong Xia, Tianbao Yang, Hong Li
- **Institution**: Meta; Texas A&M University
- **Date**: 2026-11-04
- **arXiv**: https://arxiv.org/abs/2611.05799
- **Venue**: Preprint

**Abstract**: Generative retrieval predicts the next item either as discrete codes (Semantic IDs) or as a continuous vector. SIDs give shared parameters and pretrained semantic structure but hard discretization discards information; continuous models avoid quantization but use flat item lookup tables with no parameter tying. CAP-Mix is a flow recommender that represents each item as a **soft mixture of shared prototypes plus an item-specific vector**. Assignments, prototypes, and item vectors are trained jointly, and the soft representation is kept at inference. Pretrained information is optional: SID responsibilities can act as a prior, and a content embedding can initialize the item-specific vector.

**Key innovations**:
- **Soft prototype mixture** introduces shared structure without a discrete bottleneck.
- **Optional SID prior / content initialization** — can improve a hard table built from the same tokenizer by **4.45–14.90% HR@5** given only an offline SID.
- **+6.9% HR@5 / +13.6% NDCG@5** averaged across six benchmarks vs the best per-dataset baseline, with **1.4–161×** inference throughput over discrete baselines.

---

## 3. Advertising & Ad Ranking

### 3.1 WISE: An Agentic Framework for Whole-page Multimodal Search Experience Attribution
- **Authors**: Wenyi Xu, Renzhe Zhou, Songyang Li, Feiran Zhu, Ruoqi Zhao, Chenglei Dai, Xuanping Li, Kaiqiao Zhan, Jingwei Zhuo
- **Institution**: Kuaishou Technology, Beijing, China
- **Date**: 2026-11-05
- **arXiv**: https://arxiv.org/abs/2611.06777
- **Venue**: Preprint (v2)

**Abstract**: Search, recommendation, and advertising rely on multi-stage model pipelines. Research prioritizes model optimization while post-deployment monitoring focuses on operational reliability, yet operationally healthy systems can still produce poor-quality results. The authors formulate **System Quality Diagnosis (SQD)** — extending evaluation beyond identifying poor outcomes to attributing their causes across system components. WISE is an agentic framework that discovers user-facing issues and traces their origins to underlying algorithmic components. ReTrace constructs evidence-consistent trajectory supervision; Adaptive Harness-Policy Optimization (AHPO) performs failure-guided optimization of the agent harness and model policy.

**Key innovations**:
- **New task formulation (SQD)** and **WISE-BENCH**, a real-world multimodal search benchmark with user-facing evidence, internal pipeline traces, and expert diagnosis labels.
- **Evidence-consistent trajectory supervision** plus harness/policy co-optimization.
- **75.20% end-to-end diagnosis accuracy** on Qwen3.5-35B-A3B; deployed for quality auditing, online QA, and downstream relevance-model improvement.

---

### 3.2 EvoRec: A Unified Self-Evolving Agentic Recommender with Dynamic Reflection Trees
- **Authors**: Mengting Li, Long Zhang, Hao Jiang, Sheng Yu, Fei Pan, Peng Jiang
- **Institution**: Kuaishou Local Services Ads Recommendation Foundation Model Team
- **Date**: 2026-11-01
- **arXiv**: https://arxiv.org/abs/2611.01977
- **Venue**: Preprint

**Abstract**: Conventional recommender systems rely on fixed cascaded pipelines, limiting adaptation to evolving user needs. Existing agentic recommenders add reasoning and tool use but lack end-to-end decision control and systematic failure reflection. EvoRec combines autonomous decision-making with reflection-driven self-evolution: a Need Agent infers needs from long-term, short-term, and working memory; a Planning Agent allocates retrieval budgets between Behavior Continuation and Need Satisfaction, selects tools, and sets ranking-fusion weights; an Acting Executor records decision traces. A Dynamic Reflection Tree identifies failures and validates repairs through replay.

**Key innovations**:
- **Reflection-driven self-evolution without parameter updates** — verified repairs are distilled into reusable cross-user strategies.
- **Adaptive retrieval-budget allocation** between behavior continuation and need satisfaction.
- **+15.7% Hit@50** on a Kuaishou local-services advertising dataset; **+4.6% ad revenue and +3.5% CTCVR** in a 7-day online A/B, with **+14.5% revenue for high-intent users**.

---

### 3.3 Improving Ads Ranking Models with Auxiliary Supervision: Techniques and Insights
- **Authors**: Nikhil Bhale, Apurva Pathak, SaiSujithKumarReddy MarapaReddy, Xiao Yin, Prateek Bhansali
- **Institution**: Meta Platforms
- **Date**: 2026-10-31
- **arXiv**: https://arxiv.org/abs/2611.01280
- **Venue**: IEEE ICDM WAIP 2026 workshop (5 pp.)

**Abstract**: Accurate post-click conversion rate (CVR) prediction is essential for personalized ad delivery, but conversion events are sparse or missing, limiting model learning. This paper presents a case study on auxiliary supervision from diverse user events and metadata signals beyond conversion events, plus modeling techniques to exploit them: linearized labels for improved auxiliary-signal precision, a split architecture for training-task decomposition, and a novel **Label Combination (LaCo)** approach for robustly managing noisy auxiliary data.

**Key innovations**:
- **Auxiliary event supervision** as a remedy for sparse CVR labels.
- **Linearized labels + split training architecture** to preserve auxiliary-signal precision.
- **LaCo** for noisy multi-source label combination; measurable ranking-quality gains with applicability beyond ads.

---

## 4. CTR Prediction

> CTR was unusually quiet in the 4–6 Nov block. NumEmbBench is the only fresh CTR-specific paper in the window; TRIP and FineSID are included as recent context and were already featured in the 2026-10-29/30 sibling digests. No new CTR scaling architecture entered [[ctr-scaling-landscape]] this run.

### 4.1 Numerical Embeddings for CTR Prediction: A Taxonomy, Unified Benchmark, and Open-Source FuxiCTR Extension
- **Authors**: Heng Yao, Hanwei Zhu, Tianying Liu, Yulou Shu, Siyun Hou
- **Institution**: Ant Group; Independent Researcher
- **Date**: 2026-10-31 (announced Nov 2026)
- **arXiv**: https://arxiv.org/abs/2611.01090
- **Venue**: Preprint (5 pp.)

**Abstract**: Numerical embeddings map scalar features into vectors before a CTR backbone combines fields. NumEmbBench is the first open benchmark dedicated to comparing numerical embeddings for CTR prediction. It classifies 18 configurations into six mechanism-based families and evaluates them through one FuxiCTR interface. After equal-budget validation tuning, frozen configurations are compared on three datasets, nine backbones, and five seeds under a shared train-only z-score protocol.

**Key innovations**:
- **Unified taxonomy + benchmark** for numerical embeddings, integrated as an open-source FuxiCTR extension.
- **Equal-budget, multi-backbone, multi-seed protocol** to remove tuning confounds.
- DEER has the best mean rank, but **six methods lead at least one dataset–backbone setting**; a matched native-scale test changes the winner in **11 of 27** settings, and accuracy and inference cost need not move together.

---

### 4.2 Rethinking Positional Encoding and Interaction Granularity for CTR Prediction (TRIP)
- **Authors**: Xinxun Zhang, Yuxiang Wang, Xiaokai Zhou, Jiayue Li, Yi Li, Yue Liu, Jun Zhang, Xiaoling Zhou, Tieyun Qian, Xiao Yan, Jiawei Jiang
- **Institution**: Wuhan University; Tencent Inc.; Peking University
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.37140
- **Venue**: Preprint (13 pp.)

**Abstract**: Transformer-based CTR models often use index-based or temporal positional encodings and token-level causal interaction, but the authors observe that most existing positional encodings do not outperform NoPE, while relaxing causal constraints within target-relative temporal groups yields gains. TRIP combines **target-aware rank–time positional encoding** with **temporal-group interaction modeling**. Factorized Rank Encoding represents each behavior's ordinal position through low-rank factorization; Target-Relative Time Encoding characterizes temporal distance to the target on a coarse-to-fine scale. Temporal Group-Causal Interaction enriches intra-group representations with bidirectional interaction while preserving inter-group causal order.

**Key innovations**:
- **Rank–time positional encoding** grounded in both sequence context and target relation.
- **Group-level causal interaction** instead of token-level causal masking.
- Compact group summaries for efficient higher-layer modeling; **+4.45% relative AUC** over the strongest baseline on four public benchmarks.

---

### 4.3 FineSID: Progressive Learning from Content to Relevance to Personalization for CTR Prediction
- **Authors**: Zhiguang Yang, Yulin Yang, Fuyu Lv, Dan Ou
- **Institution**: Alibaba Group
- **Date**: 2026-10-20 (announced Oct 2026)
- **arXiv**: https://arxiv.org/abs/2610.29138
- **Venue**: Preprint

**Abstract**: Multimodal CTR prediction in search depends on item content, query relevance, and user preference. Existing approaches use dense embeddings or coarse discrete IDs, making it hard to integrate fine-grained heterogeneous content with ID-based predictors. FineSID unifies content tokenization, query–item semantic pretraining, and personalized post-training through a shared fine-grained discrete representation. A multi-scale visual tokenizer and text tokenizers convert content into fine-grained Semantic IDs; full-parameter semantic pretraining establishes a matching prior; the predictor is then fine-tuned with user click supervision.

**Key innovations**:
- **Progressive content → relevance → personalization curriculum** over shared Semantic IDs.
- **Semantic pretraining as a matching prior** before click-supervised personalization.
- Improves both CTR and core business metrics, and improves within-product creative discrimination beyond ID memorization.

---

## 5. Sequential Modeling

### 5.1 DESRec: Deliberate Latent Reasoning for Sequential Recommendation
- **Authors**: Haobo Zhang, Qiannan Zhu, Yutao Zhu, Zhicheng Dou
- **Institution**: Gaoling School of Artificial Intelligence, Renmin University of China
- **Date**: 2026-11-04
- **arXiv**: https://arxiv.org/abs/2611.06521
- **Venue**: Preprint

**Abstract**: Sequential recommenders model user preferences from interaction histories. Recent methods add latent reasoning by autoregressively generating intermediate reasoning vectors, but use a fixed number of reasoning steps for all users — over-thinking simple histories and under-thinking complex ones. DESRec performs personalized latent reasoning: a reasoning-step selection module identifies the optimal step per user during training; self-distillation compresses the most informative state into the final reasoning step used at inference; a progressive preference extraction mechanism segments each history into a variable number of periods, summarizes each into a latent milestone, and feeds it into subsequent reasoning.

**Key innovations**:
- **Per-user adaptive reasoning depth** instead of a fixed step count.
- **Self-distillation** of the best intermediate state into the final representation.
- **Variable-length latent milestones** for evolving user interests; outperforms eight baselines on six public datasets and four backbones.

---

### 5.2 Beyond Independent Predictions: Learning the Browsing Journey for Sequence-Level Re-ranking (ICE)
- **Authors**: Jiayi Zhang, Jingxin Hai, Zhenjia Ma, Hongbin Pei, Dagui Chen, Han Zhu, Jian Xu
- **Institution**: Taobao & Tmall Group of Alibaba, Beijing, China
- **Date**: 2026-11-05
- **arXiv**: https://arxiv.org/abs/2611.07591
- **Venue**: Preprint

**Abstract**: Industrial re-ranking uses a Generator–Evaluator framework, where the evaluator's utility estimates govern recommendation quality. Existing evaluators follow **Independent Behavior Modeling (IBM)**, simplifying the continuous user browsing journey into independent per-item predictions (e.g., CTR). This ignores that a click can occur only after an item is reached and impressed, and that items compete for finite attention. The authors propose **Joint Behavior Modeling (JBM)** — explicitly modeling the display → impression → click process — and instantiate it as the **Impression-Click Evaluator (ICE)**.

**Key innovations**:
- **Browsing-depth distribution** estimates per-position impression probabilities.
- **Impression-aware suppression** of spurious context from unexposed items, plus a **click distribution matching** objective for intra-sequence dependencies.
- Plug-and-play evaluator; **14-day Taobao A/B: +0.70% clicks, +3.67% revenue**, followed by full-traffic deployment.

---

### 5.3 OneLatent: Latent Reasoning for Efficient Foundation Recommendation Models
- **Authors**: Hao Jiang, Peiru Du, Pengfei Yao, Mengting Li, Siyuan Lou, Kuo Cai, Sheng Yu, Qiang Luo, Jian Liang, Ruiming Tang, Fei Pan, Peng Jiang, Wenwu Ou
- **Institution**: Kuaishou Technology, Beijing, China
- **Date**: 2026-10-21 (v2 2026-11-02)
- **arXiv**: https://arxiv.org/abs/2610.30675
- **Venue**: Preprint

**Abstract**: LLMs motivate foundation recommendation models (FRMs), but explicit Chain-of-Thought reasoning imposes large inference overhead and relies on manually designed templates. OneLatent compresses explicit reasoning traces into several learnable latent tokens, enabling **Latent-Reason-then-Answer** inference without verbose traces. It introduces Multi-View Adaptive CoT (MV-ACoT) to create diverse, high-quality teacher supervision with adaptive reasoning complexity, then uses three-stage latent-token alignment to internalize CoT into latent tokens, followed by curriculum-based post-training.

**Key innovations**:
- **Latent-token reasoning** replaces explicit CoT at inference.
- **Multi-view adaptive CoT** automatically adjusts teacher reasoning complexity per instance.
- **+17.44% / +9.33% SID@64** vs Think / No-Think FRM variants, **>17× online inference throughput**, and an estimated **9.6% revenue lift** in a Kuaishou local-services ads A/B.

---

## 6. Games, Game Theory & Multi-Agent RL

### 6.1 Efficient Equilibrium Computation in Colonel Blotto Games
- **Authors**: Martin Bichler, Abheek Ghosh
- **Institution**: Technical University of Munich, Germany
- **Date**: 2026-11-03
- **arXiv**: https://arxiv.org/abs/2611.05221
- **Venue**: Preprint (75 pp.)

**Abstract**: Colonel Blotto is a fundamental resource-allocation game: two players divide budgets across battlefields, and the higher allocation on each battlefield wins its value. Computing an equilibrium efficiently had remained unresolved for the classical continuous version with arbitrary budgets and battlefield values that may vary across battlefields but are the same for both players. The authors give a **fully polynomial-time approximation scheme (FPTAS)** that computes an ε-Nash equilibrium in time polynomial in the input length and 1/ε, and nearly linear in the input length for fixed ε. For sufficiently balanced budgets and battlefield values, they also compute exact equilibria in linear time.

**Key innovations**:
- **FPTAS for continuous Colonel Blotto** with arbitrary budgets and heterogeneous battlefield values.
- **Linear-time exact equilibria** in the balanced regime.
- Settles a long-standing computational question in algorithmic game theory.

---

### 6.2 Polynomial-Time Computation of Extensive-Form Proper Equilibria in Two-Player Zero-Sum Games
- **Authors**: Sam Ganzfried
- **Institution**: Ganzfried Research; Cornell University
- **Date**: 2026-11-04
- **arXiv**: https://arxiv.org/abs/2611.07089
- **Venue**: Preprint (short)

**Abstract**: The paper gives a deterministic polynomial-time algorithm for computing an **exact extensive-form proper equilibrium** in a finite two-player zero-sum extensive-form game with perfect recall and rational data. Properness is understood in the agent normal form: an action at an information set is penalized relative to a better action while all other local behavioral choices, including the player's own future actions, remain fixed. Each information set gets a geometric permutahedron of allowable action probabilities; a scaled doubly stochastic representation embeds these restrictions in a polynomial-size sequence-form polytope.

**Key innovations**:
- **Sequence-form polytope with permutahedron restrictions** for local properness.
- **Exact equilibrium extraction** via sign stability of a parametric linear system and a persistent feasible basis.
- Rational probabilities with polynomial encoding length, including at information sets with vanishing realization probability.

---

### 6.3 AGiR: Mitigating Gift Over-Reliance in Mixed-Motive Games
- **Authors**: Woohyeon Byeon, Seongmin Kim, Jiwon Jeon, Woojun Kim, Youngchul Sung
- **Institution**: KAIST
- **Date**: 2026-11-02
- **arXiv**: https://arxiv.org/abs/2611.02875
- **Venue**: NeurIPS 2026

**Abstract**: Mixed-motive games model multi-agent scenarios where self-interested agents must both cooperate and compete. Existing gifting methods can make agents overly dependent on incoming gifts and fail to learn reward-yielding behaviors — a phenomenon the authors call **gift over-reliance**. They propose a **refusal-augmented gifting framework** with an adaptive refusal mechanism that lets agents selectively reject a portion of received gifts from their policy-update signals, mitigating over-reliance and preventing exploitation.

**Key innovations**:
- **Adaptive gift refusal** as a plug-in for existing gifting schemes.
- **Decentralized learning** without major changes to training pipelines.
- Consistently reduces gift over-reliance across MMG environments and gifting schemes, prevents lock-in to sacrificing policies, and improves α-fairness.

---

### 6.4 Learning and Steering in Incomplete-Information Games
- **Authors**: Asrın Efe Yorulmaz, Tamer Başar
- **Institution**: University of Illinois Urbana–Champaign
- **Date**: 2026-11-05
- **arXiv**: https://arxiv.org/abs/2611.07589
- **Venue**: Preprint (57 pp.)

**Abstract**: A mediator seeks to influence strategic decision dynamics using only outcome-level feedback and without knowing agents' utilities. The mediator knows the game form and her own objective but not the agents' utilities; she commits to nonnegative payments and provides recommendations and contexts, but receives only a single realized terminal outcome rather than full-information feedback. The authors develop halving-type algorithms that learn utility differences in normal-form games and conditional continuation-value differences in extensive-form games, with sample complexity Õ(ε⁻²) matching worst-case lower bounds up to logarithmic factors. They combine these with a Lagrangian formulation in an online **Learn–Compute–Steer** algorithm.

**Key innovations**:
- **Outcome-feedback-only learning** of agent utilities for mediator steering.
- **Sample-complexity matching lower bounds** for utility-difference learning.
- **Learn–Compute–Steer** achieves Õ(T⁻¹/⁴) directness and optimality gaps with Õ(T⁻¹/⁸) time-average payments, steering toward mediator-optimal extensive-form correlated equilibria.

---

## Cross-Cutting Themes

1. **Industrial recommendation is consolidating around generative retrieval + value alignment.** BRIDGE (Kuaishou), CAP-Mix (Meta), OneLatent (Kuaishou), and ICE (Alibaba) all attack the same gap: discrete Semantic IDs lose information and/or optimize likelihood rather than business value. The fixes differ — codebook-grounded latent reasoning, soft prototype mixtures, latent CoT compression, and joint display→impression→click modeling — but the target is identical.

2. **Latent reasoning is replacing explicit CoT in production recommenders.** DESRec, OneLatent, and (from the prior window) OneLatent-style FRMs show that adaptive/compressed reasoning depth beats fixed Think/No-Think regimes on both quality and throughput.

3. **Advertising research is shifting from ranking models to system-level diagnosis and self-evolution.** WISE treats post-deployment quality as a causal attribution problem across pipeline components; EvoRec treats the recommender as a reflective agent that repairs its own retrieval/planning failures without parameter updates.

4. **LLM efficiency work is increasingly exact rather than approximate.** SpecCTMC preserves the exact CTMC distribution while cutting sequential evaluations; RecSA preserves length extrapolation via level-local RoPE; O²PD explicitly characterizes when teacher supervision is reliable. The common thread is *theoretical guarantees plus wall-clock gains*.

5. **Game theory is having a computational-complexity moment.** Colonel Blotto gets an FPTAS, proper equilibria in two-player zero-sum extensive-form games become polynomial-time computable, and mediator steering gets matching sample-complexity bounds. These are foundational results rather than benchmark-driven engineering.

6. **CTR-specific architecture research remains sparse.** The window produced a benchmark/taxonomy paper (NumEmbBench) rather than a new backbone. The action is in generative recommendation and sequence-level evaluation, not in new feature-interaction operators.

---

## Source Notes & Caveats

- **Affiliations** are parsed from `arxiv.org/html` author blocks. Where a rendered affiliation block was unavailable (e.g., 2611.06323, 2610.14709), the entry was omitted rather than guessed.
- **All abstracts are paraphrased/condensed from arXiv metadata**; performance numbers are author-reported and not independently verified.
- **Overlap**: TRIP (2610.37140) and FineSID (2610.29138) were previously featured in sibling digests; they are included here as recent CTR context, not as new discoveries. BRIDGE, WISE, EvoRec, OneLatent, and related Kuaishou papers reflect the same organization's active November release cadence.
- **Date convention**: "Date" is the arXiv submission date shown on the abstract page; announcement dates may be one business day later.
- Generated for [[index|the wiki]] synthesis archive; companion daily digests for 2026-11-07 live alongside this file.
