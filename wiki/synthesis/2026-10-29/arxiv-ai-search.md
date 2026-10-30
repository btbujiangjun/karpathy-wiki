---
title: arXiv AI Search - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-10-29)
type: synthesis
created: 2026-10-29
updated: 2026-10-29
sources: [arxiv.org]
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, generative-recommendation, auctions, auto-bidding, calibration, memory, agents, moe, mamba, embeddings]
---

# arXiv AI Search - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-10-29)

> Generated: 2026-10-29 | Effective submission window: 2026-10-23 to 2026-10-28 (latest indexed listings at query time)
>
> A curated sweep of recent arXiv submissions across AI, LLMs, recommendation, advertising, CTR, sequential modeling, and games. Abstracts are condensed from arXiv; institutions are parsed from rendered author blocks or HTML author affiliations, never inferred. Where no affiliation is listed, the field says so explicitly. This report features **24 papers not previously covered in the wiki** and cross-references 10 same-window papers already summarized in the [2026-10-29 arXiv Paper Check](./arxiv-paper-check.md).

## Summary

- **CTR research is moving from architecture to input and evaluation hygiene.** OptIDC jointly configures samples, features, and embedding units instead of tuning one axis; a temporal calibration study finds random splits understate ECE by 38–45%, and wider 12-hour recalibration slices beat the freshest few hours. Both papers target assumptions upstream of the ranker.
- **Industrial ranking is consolidating heterogeneous signals into one backbone.** HiRank fuses sequential and non-sequential features with effective-rank-aware attention and reports +2.27% orders per user at Alibaba; BehaveRec (Walmart) quantifies exactly when 90-day history and behavioral-graph signals pay off, yielding a ~20-interaction deployment threshold.
- **Generative recommendation is attacking the cost of depth.** LoopGR treats recurrent depth as a scaling axis, alternating a shared decoder with a lightweight context updater and distilling a low-budget trajectory from a high-budget teacher; model size drops up to 52% versus an encoder-decoder baseline.
- **Advertising work is split between production control and mechanism design.** Pinterest's RLBP uses RL as a daily meta-controller for PID bidding parameters and reports lower eCPC with no revenue loss; two auction papers close long-open gaps on cascade position auctions, achieving factor-6 and factor-2 truthful-in-expectation guarantees under general click models.
- **LLM systems papers focus on stability and memory bandwidth.** EnergyCal suppresses Muon-family MoE loss spikes via expert-update energy calibration; GateRQ makes conditional-memory lookups precision-adaptive; balanced state subspaces cut Mamba-2 state size in half; an Edge-of-Stability study finds a new "Edge of Convexity" failure mode across LLM pretraining up to 787M parameters.
- **Agents are being evaluated on memory quality, proactivity, and security rather than raw task success.** ETAMem and DiscernMem both separate memory content from memory use; ProactMem validates behavioral regularities before acting; Log-To-Leak shows successful MCP task completion can coexist with 62.64–100% attack success.
- **Games remain the cleanest stress test for long-horizon, hidden-information, and interface-heavy agents.** AutoTavern's LLM research agents build a Hearthstone Battlegrounds simulator and reach top-human ladder statistics; a small-budget Riichi Mahjong replication finds text is the bottleneck; GLEE combines game-theoretic solvers with moral-rhetoric framing; UnityBench-Mini3D shows coding agents fall from 80.9% on easy to 35.2% on hard Unity tasks.

## Methodology and scope

- **Source sweep**: arXiv recent-listing pages for `cs.IR`, `cs.CL`, `cs.AI`, `cs.LG`, `cs.GT`, and `cs.MA` (250 entries each), deduplicated to **903 unique arXiv IDs**. The listings covered **2026-10-22 to 2026-10-28**; **853 IDs** fall in the 2026-10-23 to 2026-10-28 window used here.
- **Selection**: title/abstract screening for recommendation, CTR, advertising/auctions, sequential modeling, LLM training and inference, agent memory/security, and games. **24 papers** were selected for full entries; **10 more** same-window papers are cross-referenced because they already have entries in the [2026-10-29 arXiv Paper Check](./arxiv-paper-check.md).
- **Metadata**: titles, authors, abstracts, dates, and categories come from `arxiv.org/abs`; affiliations come from `arxiv.org/html` author blocks. The arXiv Export API returned `Rate exceeded` throughout the sweep, so listing pages plus abstract/HTML pages were used instead.
- **Novelty check**: all 24 featured IDs were grep-verified as **zero prior hits** in `wiki/` at write time. The 10 cross-referenced IDs are explicitly marked as companion coverage rather than re-summarized.
- **Caveats**: this is an **abstract-only** review. All numbers are author-reported and were not independently reproduced. Venue labels follow arXiv comments. Institution attribution is conservative: `2610.37062`, `2610.37280`, and `2610.34791` list no structured affiliation on arXiv (the last is identified only by an author footnote).

---

## 1. Recommendation, CTR, and Sequential Modeling

### 1.1 Towards a Unified Framework of Optimal Input-Side Dimensional Configuration for Deep CTR Prediction (OptIDC)
- **Authors**: Chaohua Yang, Fuyuan Lyu, Xing Tang, Dugang Liu, Xiuqiang He, Zhong Ming
- **Institution/Company**: Shenzhen University; McGill University; Shenzhen Technology University
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35695
- **Categories**: cs.IR, cs.AI

**Abstract**: Deep CTR models increasingly optimize feature-interaction architectures, but performance also depends on how input-side information is configured before interaction modeling. Prior work selects informative samples, features, or embedding units independently along a single axis, ignoring their shared form and cross-level dependencies. OptIDC jointly learns sample-, feature-, and embedding-unit-level configurations in one framework, and introduces a **selection-weighted optimal transport** mechanism that aligns coarse- and fine-grained selections over finite measures, reducing cross-level selection conflicts while preserving each level's semantics. The framework is model-agnostic and plugs into existing CTR models. On four real-world benchmarks it consistently achieves higher AUC than existing input-side selection methods.

**Key Innovations**:
- Treats sample, feature, and embedding-unit selection as one joint configuration problem.
- Uses selection-weighted optimal transport to coordinate coarse and fine selection decisions.
- Remains model-agnostic and compatible with existing CTR backbones.
- Reports consistent AUC gains across four benchmark datasets.

---

### 1.2 How Much Fresh Data Should CTR Recalibration Use? A Temporal Evaluation of Post-hoc Calibration
- **Authors**: Rui Liu
- **Institution/Company**: Independent Researcher
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.33168
- **Categories**: cs.LG, cs.IR

**Abstract**: Offline CTR evaluation still defaults to random splits, although deployed models score future traffic and downstream systems consume calibrated probabilities. On Avazu (40.4M impressions), the paper trains logistic regression, DeepFM, and DCN-v2 under two rolling temporal origins and a random split, then recalibrates each test day with Platt scaling and isotonic regression fitted on preceding hours. At the nearest test day, random splits report LR's expected calibration error at **55–62% of the temporal value** in every seed; deep-model ratios are seed-unstable. Recalibration with a 6-hour slice removes up to **61% of ECE** in badly miscalibrated cells but increases it in about one third of applications. A 12-hour slice cuts harm substantially, and a 12-hour slice subsampled to the 1-hour slice's size recovers **88%** of the full slice's gain. A simulated auction moves profit by only about **−0.21% to +0.26%**.

**Key Innovations**:
- Measures calibration temporally across multiple origins and seeds rather than on random splits.
- Shows calibration error is not monotone in temporal distance.
- Finds wider 12-hour fitting windows outperform the freshest few hours.
- Separates statistical calibration gains from downstream auction profit.

---

### 1.3 Unified Heterogeneous Feature Interaction via Effective-Rank Scaling for Recommender Systems (HiRank)
- **Authors**: Ao Zhang, Haochuan Li, Boya Du, Jian Yang, Qihang Fang, Yulin Xu
- **Institution/Company**: Alibaba Group; Renmin University of China; Institute of Automation, Chinese Academy of Sciences
- **Date**: 2026-10-26 (v2 2026-10-27)
- **arXiv**: https://arxiv.org/abs/2610.35318
- **Categories**: cs.IR

**Abstract**: Industrial ranking models must jointly capture heterogeneous feature interactions, long-term user behaviors, and multi-scenario dependencies under tight serving constraints. Existing architectures process sequential and non-sequential features with separate modules, limiting bidirectional exchange; applying homogeneous self-attention to all tokens is inefficient when the two signal types have different effective ranks (eRanks), and shared representations can cause negative transfer across scenarios. HiRank integrates gated sequential attention with heterogeneous feature interaction in a unified backbone, uses scenario-aware aggregation to compress low-order tokens, and learns distinct projections that turn the compact representation into scenario-aware composite tokens with complementary global views and more uniform information density. Online A/B tests report a **2.27% increase in orders per user**.

**Key Innovations**:
- Bidirectional fusion of sequential and non-sequential features in one backbone.
- Effective-rank-aware projections instead of homogeneous attention over all tokens.
- Scenario-aware token compression to control serving cost and negative transfer.
- Industrial-scale offline scaling plus a production A/B result.

---

### 1.4 BehaveRec: When Does Long-Term Behavioral History Help Sequential Recommendation?
- **Authors**: Aysenur Inan, Reza Yousefi Maragheh, Jayesh Uddhav Kudase, Selene Xu, Kaushiki Nag, Jianpeng Xu, Sushant Kumar
- **Institution/Company**: Walmart Global Tech
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.36239
- **Categories**: cs.AI, cs.IR

**Abstract**: Sequential recommenders usually predict the next action from recent session interactions, limiting personalization when short-term signals are weak. BehaveRec combines three signals: a causal session transformer, a bidirectional **90-day User History Encoder**, and a GraphSAGE module over a **user–user graph built from behavioral embedding similarity** rather than item co-occurrence; a learned gate blends them per user. On an industrial dataset of **137M sequences from 12.6M users**, it improves R@5 by **+3.2%** over SASRec, and a larger-capacity SASRec still trails by 2.5%. A user-level dose–response analysis shows the advantage is negligible below roughly 10 interactions and grows monotonically with history richness, reaching **+0.017 R@5** for users with 101+ events. The authors derive a deployment rule of about **20 interactions per user**. A preliminary item-level check is directionally mixed and is explicitly scoped as an open question.

**Key Innovations**:
- Quantifies *when* long-term history helps instead of assuming it always does.
- Uses a behavioral-similarity user graph rather than item co-occurrence.
- Provides a user-level dose–response curve and a concrete deployment threshold.
- Reports a lightweight model (5.67M parameters) and an honest item-level caveat.

---

### 1.5 Cross-Domain Sequential Recommendation with Representation-Level User Transfer
- **Authors**: Abdulaziz Samra, Nikita Sukhorukov, Alexey Grishanov, Alexey Vasilev, Evgeny Frolov
- **Institution/Company**: Skolkovo Institute of Science and Technology; Higher School of Economics; AXXX; Sber AI Lab
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35550
- **Categories**: cs.IR, cs.AI, cs.DC
- **Venue**: CIKM 2026 (full paper track)

**Abstract**: Cross-domain sequential recommendation typically assumes access to auxiliary-domain interactions or item embeddings, which is problematic when business constraints isolate domains and many users have no cross-domain activity. This framework transfers information **only through learned user representations**: a lightweight adapter projects the source-domain user representation into the target-domain embedding space and integrates it with the target sequence. When source data is unavailable, the model falls back to a target-only sequential recommender while still benefiting from joint training across all users. Experiments under both a benchmark setup and a realistic scalable setup show consistent gains for shared and unshared users.

**Key Innovations**:
- Representation-level transfer without sharing raw interactions or item embeddings.
- Lightweight adapter between source and target embedding spaces.
- Graceful fallback for users observed only in the target domain.
- Evaluates the realistic cold/unshared-user regime, not just shared users.

---

### 1.6 LoopGR: Parameter-Efficient Scaling for Generative Recommendation via Recurrent Depth
- **Authors**: Huizhe Zhang, Yudong Li, Liang Chen, Chengxiang Zhuo, Zang Li
- **Institution/Company**: Sun Yat-sen University; Platform and Content Group, Tencent
- **Date**: 2026-10-25
- **arXiv**: https://arxiv.org/abs/2610.34157
- **Categories**: cs.IR

**Abstract**: Generative recommendation casts next-item prediction as autoregressive generation and shows favorable scaling behavior, but real systems face strict model-size and inference-cost limits. LoopGR scales through **recurrent depth** instead of parameter count: a hierarchical mechanism alternates between a shared generative decoder and a lightweight context updater. For efficient inference, **recurrent trajectory self-distillation** transfers a high-budget teacher's predictive distributions and evolution directions to a low-budget student. LoopGR consistently outperforms strong generative-recommendation baselines and, versus a representative encoder–decoder baseline, achieves superior performance while reducing model size by up to **52%**.

**Key Innovations**:
- Recurrent depth as a new scaling dimension for generative recommendation.
- Shared decoder plus lightweight context updater for flexible computation.
- Trajectory self-distillation aligns both predictions and state evolution.
- Substantial parameter reduction without sacrificing ranking quality.

---

### 1.7 Modeling Preference Dependencies with Directed Acyclic Graphs for Narrative-Driven Recommendation (PDG-F)
- **Authors**: Mingzhe Lu, Jian Qin, Ruize Qin, Jinhao Liu, Yunpeng Li, Hang Su
- **Institution/Company**: Not listed on arXiv
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.37280
- **Categories**: cs.IR, cs.CL

**Abstract**: Narrative-driven recommendation lets users express multifaceted needs in free-form text, where stated preferences naturally qualify and condition one another. Existing methods treat narratives as flat keyword combinations or unconstrained generative queries, missing how preferences hierarchically refine each other. PDG-F parses a request into a **directed acyclic Preference Dependency Graph (PDG)**, retrieves candidate evidence from the open Web via directed-path retrieval, and ranks recommendations by topological path ranking. Experiments across three domains in English and Chinese show consistent gains over competitive baselines, open-domain retrieval agents, and frontier language models. Diagnostic analysis shows dependency-guided retrieval raises the attainable candidate-pool ceiling.

**Key Innovations**:
- Explicit preference-dependency DAG instead of flat narrative parsing.
- Directed-path retrieval over open-web evidence.
- Topological path ranking that respects preference qualifications.
- Candidate-pool ceiling analysis isolates where the gains come from.

---

## 2. Advertising, Auctions, and Market Design

### 2.1 Reinforcement Learning for Controller Parameters in the Auto-Bidding System at Pinterest (RLBP)
- **Authors**: Yichu Zhou, Qinyi Chen, Fei Feng, Jacob Loh, Mehdi Ben Ayed, Lin Yang, Andrei Curelea, Jiajing Xu
- **Institution/Company**: Pinterest; University of California, Los Angeles
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.33248
- **Categories**: cs.LG, cs.IR

**Abstract**: Auto-bidding must balance budget delivery and cost per action across heterogeneous campaigns under non-stationary markets, and the trade-off shifts over a campaign's life: cost optimization dominates early, while delivery becomes urgent near deadlines. Fixed-tuned PID controllers are stable and interpretable but cannot adapt to campaign diversity and traffic shifts. **RLBP** uses reinforcement learning as a **daily meta-controller** that selects campaign-specific PID parameters while retaining PID for high-frequency bid adjustment. A multi-head Q-network is trained with a **relative-lift reward normalized against the production baseline**, and inference-time fusion adapts the cost–delivery trade-off without retraining. Online A/B tests show a statistically significant reduction in effective CPC with no revenue degradation; two months of holdout measurements show consistent cost reductions.

**Key Innovations**:
- RL meta-controller layered on top of an existing production PID controller.
- Relative-lift reward formulation normalized to the live baseline.
- Inference-time fusion adapts to campaign state without retraining.
- Production A/B plus a two-month holdout, not just offline simulation.

---

### 2.2 A Factor-6 Truthful-in-Expectation Mechanism for Cascade Position Auctions
- **Authors**: Qiuyu Chen, Baao Xie
- **Institution/Company**: Shanghai Jiao Tong University; Eastern Institute of Technology, Ningbo
- **Date**: 2026-10-24
- **arXiv**: https://arxiv.org/abs/2610.33707
- **Categories**: cs.GT, cs.DS

**Abstract**: In cascade position auctions, earlier clicks prevent users from reaching later placements, coupling the click probabilities of selected ads. Prior work achieved constant-factor welfare approximation and monotone logarithmic-factor approximation separately; whether both guarantees can hold simultaneously was open, because welfare-preserving rounding need not preserve the monotonicity required for truthful bidding. The paper gives a polynomial-time randomized mechanism with **factor-6 welfare approximation** and **truthfulness in expectation** for arbitrary public advertiser–position click probabilities. It optimizes a reach-weighted linear relaxation, converts the solution into feasible ordered allocations via matching decomposition, probability-bounded grouping, and calibrated attenuation, and makes each advertiser's expected CTR exactly one sixth of its fractional click coordinate. That identity transfers monotonicity to the implemented mechanism and enables exact incentive-compatible payments.

**Key Innovations**:
- Simultaneous constant-factor welfare and truthfulness-in-expectation for cascade auctions.
- Calibrated attenuation compensates for cascade dependence.
- Matching decomposition plus probability-bounded grouping for feasible ordered allocations.
- Polynomial-time allocation, payments, and exact sampling.

---

### 2.3 A Truthful-in-Expectation 2-Approximation for Pair-Specific Cascade Auctions in AI-Generated Content
- **Authors**: Tao Jiang, Minbo Gao, Shaowei Cai
- **Institution/Company**: Institute of Software, Chinese Academy of Sciences; University of Chinese Academy of Sciences
- **Date**: 2026-10-25
- **arXiv**: https://arxiv.org/abs/2610.34236
- **Categories**: cs.GT

**Abstract**: Generative AI interfaces can insert sponsored content at multiple points in an answer, where CTRs depend on the advertiser–position pair. Under the cascade model, users read ads sequentially and stop after the first click, so assignment and display order both affect welfare. For arbitrary pair-specific CTRs, prior work gave a `4/(1−ε)`-approximation whose monotonicity was not established, and a monotone `O(log m)`-approximation. This paper gives a polynomial-time mechanism that is truthful and individually rational in expectation and achieves a **2-approximation** to optimal cascade welfare for arbitrary pair-specific CTRs and any limit on displayed ads. It selects an advertiser–position matching and a designated last ad, randomly thins earlier ads so each selected ad's expected cascade CTR is a fixed fraction of its standalone CTR, and maximizes the resulting closed-form welfare over a bid-independent lottery range via linear programming.

**Key Innovations**:
- Closes the constant-factor versus monotonicity gap for pair-specific cascade CTRs.
- Random-prefix decomposition proves a tight factor-two guarantee for the lottery range.
- Exact lottery optimization preserves monotonicity, unlike optimizing the prior surrogate.
- Applies directly to multi-slot sponsored placement in AI-generated answers.

---

## 3. LLM Training, Optimization, and Inference

### 3.1 EnergyCal: Taming Loss Spikes in Muon-Family Optimizers for Sparse MoE Training
- **Authors**: Masato Fujitake
- **Institution/Company**: Not listed on arXiv
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.37062
- **Categories**: cs.LG, cs.AI, cs.CL

**Abstract**: Sparse mixture-of-experts language-model training can exhibit large loss spikes with Muon-family optimizers. EnergyCal attenuates routed-expert updates according to the **normalized squared Frobenius norm of their finite-step Newton–Schulz directions**, leaving the spectral transform unchanged and adding no persistent optimizer state. On a **4B-parameter MoE**, against a development-selected lower-learning-rate MuonH recipe, EnergyCal-MuonH reduces mean thresholded loss-spike burden by **99.51%** and final geometric-mean perplexity by **4.06%**, with a modest throughput cost. With plain Muon at matched nominal learning rate and weight decay, the reduction in mean spike burden averages **95.98%** across two tested exponents, with small endpoint improvements. The rule works with and without Hyperball in the evaluated setting.

**Key Innovations**:
- Energy-based attenuation of routed-expert updates rather than global clipping.
- Leaves the Muon spectral transform intact and adds no optimizer state.
- Large spike reduction on a 4B-parameter sparse MoE.
- Works for both MuonH and plain Muon in the tested recipes.

---

### 3.2 Advancement or Acceleration? How Data Curation Improves LLM Training
- **Authors**: Jiaxing Wang, Zicheng Zhang, Deping Xiang, Jin Xu, Yong Li, Chao Liu, Pengzhang Liu, Qixia Jiang
- **Institution/Company**: JD.com; University of Oxford
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.36983
- **Categories**: cs.LG, cs.AI

**Abstract**: Data curation is widely credited with improving LLM training, but it is unclear whether it expands what a model can ultimately learn (**advancement**) or merely reaches the same performance with less data (**acceleration**). Through an analytic characterization and real LLM experiments, the paper shows advancement requires a **correctable train–target gap**. When baseline training and target objectives coincide, no curation policy improves the endpoint, although it may accelerate training. The authors operationalize the condition as the **Δ-test**, an observable discrepancy between the uncurated baseline's training and target losses computable before expensive curation. Across experiments, an appreciably nonzero Δ predicts persistent gains, while gains near Δ = 0 diminish as the training budget grows.

**Key Innovations**:
- Formal separation of advancement from acceleration in data curation.
- Identifies a correctable train–target gap as the necessary condition for advancement.
- Proposes the pre-curation Δ-test as a cheap diagnostic.
- Reframes curation quality as a property of the task and target set.

---

### 3.3 Does LLM Pre-Training Typically Occur at the Edge of Stability?
- **Authors**: Yuhang Cai, Haodong Wen, Haofeng Huang, Deyi Liu, Yiyuan Ma, Kaifeng Lyu
- **Institution/Company**: University of California, Berkeley; Tsinghua University; ByteDance Seed
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.36778
- **Categories**: cs.LG

**Abstract**: Quadratic approximations are a common lens for neural-network optimization, but their fidelity to real LLM training is unclear. The paper highlights a distinct failure mode: **Edge of Convexity (EoC)**, where persistent negative curvature makes the quadratic dynamics diverge regardless of learning rate even though the real dynamics remain stable. After removing this learning-rate-independent instability, the authors define a generalized **Edge of Stability (EoS)** for stochastic training with adaptive optimizers, based on whether increasing the learning rate causes significant divergence in the quadratic dynamics while leaving real dynamics largely unchanged. Across LLM pretraining runs up to **787M parameters**, EoC is always observed, and EoS is prevalent but not universal: it disappears at sufficiently small learning rates (e.g., after decay) or when batch size falls below a critical threshold positively correlated with the critical batch size.

**Key Innovations**:
- Identifies Edge of Convexity as a failure mode of quadratic approximations.
- Generalizes Edge of Stability to stochastic adaptive-optimizer training.
- Tests the theory across LLM pretraining runs up to 787M parameters.
- Maps when EoS disappears as a function of learning rate and batch size.

---

### 3.4 Let the Gate Decide: Per-Lookup Precision for Quantized Conditional Memory in LLMs (GateRQ)
- **Authors**: Tianqi Chen, Xunchao Li, Linchuan Xie, Guanghua Yu, Jianchen Zhu, Peisong Wang, Jian Cheng
- **Institution/Company**: Institute of Automation, Chinese Academy of Sciences; Tencent; University of Chinese Academy of Sciences
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35985
- **Categories**: cs.LG, cs.AI

**Abstract**: Conditional memory layers such as DeepSeek's Engram attach large hashed n-gram tables to a language model; removing them from DeepSeek-V4.1-Flash costs **36.8 PopQA points**. Low-bit quantization loses long-tail facts first, and allocating more bits to frequently accessed rows backfires—refining lookups by access frequency is worse than refining them at random. The cause is the gate that scales each retrieved row: a lookup's quantization error is weighted by its gate, which is small for frequent n-grams and large for rare long-tail n-grams, and is computable from a 1-bit code. GateRQ stores each row as a ladder of 1-bit residual codes, keeps level 1 in GPU memory to compute the gate, and reads deeper levels only for the lookups the gate ranks highest. Without retraining, it cuts GPU table memory by **7.8×** on DeepSeek-V4.1-Flash and raises vLLM throughput by **11–31%** over FP8 tables, losing about 1 PopQA point at 1.50 bits read per lookup and 0.2 points at 2.10 bits.

**Key Innovations**:
- Gate-weighted quantization error instead of access-frequency-based bit allocation.
- Per-lookup precision ladder with a 1-bit code deciding deeper reads.
- No retraining required; integrates with an existing serving stack.
- Explicit memory/throughput/accuracy Pareto points on a frontier model.

---

### 3.5 Balanced State Subspaces for Mamba-2 State Compression
- **Authors**: Shang Tingyu, Cao Wenfei
- **Institution/Company**: Shaanxi Normal University
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.36617
- **Categories**: cs.LG, cs.AI, cs.CL, stat.AP, stat.ME

**Abstract**: Mamba-2 compresses context into a fixed-size recurrent state that dominates decoding memory and bandwidth. Existing compressors quantize state values or prune coordinates, scoring each channel independently in the native basis. Examining trained Mamba-2 states, the authors find energy is almost rank-one, but the output does not read the energetic directions: energy concentrates in a bias-like direction accumulated by the recurrence, while the content the output reads lives in a low-dimensional subspace not aligned with the state's coordinates. Compression should therefore target the **write–read subspace**. The paper instantiates **balanced truncation** with full controllability and observability Gramians and applies the rotation exactly through Mamba-2's scalar-identity transition. **HARP** allocates ranks per layer from the Hankel spectrum and protects retrieval-sensitive layers. Calibration takes one forward pass. Halving the state dimension raises WikiText-2 perplexity by only **0.3 points (1.8%)** across 130M–2.7B models, versus 1.6 points (9.3%) for GHOST.

**Key Innovations**:
- Targets the write–read subspace rather than energetic state coordinates.
- Uses balanced truncation with controllability/observability Gramians.
- HARP allocates per-layer ranks from the Hankel spectrum.
- Single-forward-pass calibration; large advantage at aggressive retention.

---

### 3.6 EmbeddingGemma 2: Unified and Efficient Multimodal Representations
- **Authors**: EmbeddingGemma Team (H. S. Vera, S. Dua, J. Andonov, et al.)
- **Institution/Company**: Google
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.37364
- **Categories**: cs.LG, cs.CL, cs.CV, cs.SD

**Abstract**: EmbeddingGemma 2 is an open multimodal embedding model that natively represents text, images, audio, video, and combinations in a unified space. It introduces simplified **per-layer embeddings** and a **multi-stage curriculum** with modality and objective progression for strong unimodal, cross-modal, and mixed-modal quality. Across embedding benchmarks for all modalities, it establishes a new Pareto frontier, outperforming specialist models and models two to twelve times larger. The design also supports resource-constrained deployment through selective modality-encoder loading, adjustable vision-token budgets, truncatable embedding dimensions, and quantized weights. The report includes ablations and releases the model.

**Key Innovations**:
- One embedding space spanning text, image, audio, video, and mixtures.
- Per-layer embeddings simplify multimodal representation extraction.
- Modality/objective curriculum improves cross-modal and mixed-modal quality.
- Deployment knobs for encoder selection, token budget, dimension truncation, and quantization.

---

## 4. Agent Memory and Security

### 4.1 ETAMem: Decoupling and Aligning Heterogeneous Memory for Long-Term Conversational Agents
- **Authors**: Xinying Qian, Ying Zhang, Yu Zhao, Xubo Liu, Baohang Zhou, Jeff Z. Pan
- **Institution/Company**: Nankai University; Tiangong University; The University of Edinburgh
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.37443
- **Categories**: cs.CL

**Abstract**: Long-term memory lets LLMs maintain coherent, personalized conversations, but existing systems suffer from **information entanglement** (heterogeneous information mixed in coarse memory units) and **organizational mismatch** (semantic-similarity structures ignore other associations). ETAMem parses conversations into atomic memory units and identifies affective information, then organizes them into three complementary hierarchical views: **Event, Affect, and Time**. It incrementally maintains these structures with adaptively calibrated thresholds. At retrieval, **entropy-based retrieval** allocates query-specific budgets across views and performs hierarchical search within each. On LoCoMo and LongMemEval-S, ETAMem improves accuracy by **12.46%** and **7.96%** relative to state-of-the-art baselines while maintaining competitive token efficiency.

**Key Innovations**:
- Separates heterogeneous memory content before structuring it.
- Three orthogonal views (event, affect, time) instead of one similarity graph.
- Entropy-based query-time budget allocation across views.
- Incremental maintenance with adaptive thresholds.

---

### 4.2 Proactive Memory for Event-Driven LLM Agents (ProactMem)
- **Authors**: Jinyang Li, Zichuan Fu, Xian Wu, Wenlin Zhang, Yimin Deng, Kaifeng Guo, Guojing Li, Junjia Qi, Xiangyu Zhao
- **Institution/Company**: City University of Hong Kong; Tencent
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.36967
- **Categories**: cs.AI

**Abstract**: Proactive LLM agents anticipate service opportunities from ongoing observations and accumulated history. Existing approaches emphasize recent context or retrieval of related memories, offering limited support for validating recurring behavioral regularities and assessing whether they apply to the current event. ProactMem organizes history into **recent events, temporal trajectories, and behavioral regularities**. Trajectory facts are checked against source events, and regularities are assessed through **historical replay** before being matched to current conditions. The authors also build **ProactiveStream**, a longitudinal benchmark covering three application scopes, where agents process isolated event streams chronologically under episode-aware opportunity labels. ProactMem reaches **52.6% F1**, a 21.4% relative improvement over the strongest of five external baselines.

**Key Innovations**:
- Separates episodic events, trajectories, and reusable behavioral regularities.
- Verifies trajectory facts against source events before use.
- Historical replay tests whether a regularity still applies.
- Introduces a longitudinal, episode-aware proactive-agent benchmark.

---

### 4.3 Remembering Is Not Enough: Refining Memories and Learning When to Use Them in Multi-Agent Systems (DiscernMem)
- **Authors**: Yipeng Hao, Yuxuan Cai, Wenkai Ji, Jie Zhou, Liyang Yu, Qin Chen, Zhiguo Yan, Shulei Zheng, Liang He
- **Institution/Company**: East China Normal University; Ocean University of China; Tongji University; Information Engineering University
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.36652
- **Categories**: cs.AI, cs.MA

**Abstract**: Memory helps LLM multi-agent systems reuse experience, but stored advice can be flawed or applied in the wrong situation, and team-level success or failure alone cannot show whether a memory needs correction or should not have been used. **DiscernMem** is a training-free framework that improves both memory quality and memory use. **Defect-Aware Memory Refinement (DMR)** compares team executions with a single memory and with no memory, diagnoses rule defects, and tests repairs on current and earlier tasks to guard against losing previously useful behavior. **Boundary-Learning Meta-Memory (BLM)** records each memory's past uses and effects, learning when its owner role should apply or avoid it based on task context and incoming messages. With Qwen3-4B-Instruct-2507 on four benchmarks, DiscernMem achieves the highest average score on AutoGen, CAMEL, and MacNet, exceeding the strongest reported baselines by **0.51–4.32 points**, including a PDDL score of **37.71 vs 28.48** on CAMEL.

**Key Innovations**:
- Separates memory refinement from memory-use policy.
- Diagnoses defective rules by comparing memory-on, memory-off, and no-memory runs.
- Learns per-memory application boundaries from past use and effects.
- Training-free and evaluated across three multi-agent frameworks.

---

### 4.4 Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via the Model Context Protocol
- **Authors**: Yuepeng Hu, Chongyu Fan, Sirat Samyoun, Jian Du
- **Institution/Company**: Duke University; Michigan State University; TikTok
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.36108
- **Categories**: cs.CR, cs.AI

**Abstract**: LLM agents increasingly access external tools through the Model Context Protocol (MCP), and the natural-language metadata describing those tools creates a prompt-injection surface. Within this established tool-poisoning surface, the paper studies **Log-To-Leak**, an additive post-hoc logging attack that induces a separate attacker-controlled call after the final legitimate call. Its payload targets the user query, MCP server name, server response, and agent response, and the injected directive is operationalized through **Trigger, Tool Binding, Justification, and Pressure**. Across five MCP servers and four LLM agents (18 valid model–server pairs), Log-To-Leak achieves **62.64–100% attack success** and **76.55–95.64% conditional logging accuracy**; 16 pairs have absolute target-task completion changes of at most 6.63 percentage points. Three evaluated defenses leave residual ASR above **55%** on GitHub MCP with GPT-4o, while an instruction detector flags 85.53% of benign descriptions.

**Key Innovations**:
- Defines a post-hoc logging attack that preserves legitimate task success.
- Decomposes the injected directive into trigger, binding, justification, and pressure.
- Measures effectiveness, utility, and efficiency across 18 model–server pairs.
- Shows current defenses are insufficient; motivates host-controlled secondary-call authorization.

---

## 5. Games and Game-Theoretic Learning

### 5.1 Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players (AutoTavern)
- **Authors**: Changlian Ma, Limin Wang
- **Institution/Company**: Nanjing University; Shanghai AI Laboratory
- **Date**: 2026-10-24
- **arXiv**: https://arxiv.org/abs/2610.33845
- **Categories**: cs.AI, cs.LG, cs.MA

**Abstract**: Hearthstone Battlegrounds is an eight-player auto-battler with stochastic shops and battles, hidden information, and nearly a thousand interacting cards. **AutoTavern** is a self-improving research system in which specialized LLM research agents share a **typed research memory**, every claim passes verification gates, and live games close the loop, so the agents improve the simulator, opponents, and policy—and their own research process. A human sets goals and rules on ambiguous mechanics. In 20 days, AutoTavern built **TavernGym**, a full-content reproduction of the live game, and delivered 23 versions of **TavernAgent**, trained with PPO against opponents calibrated to real games. TavernAgent plays on the live ladder: its rating rose from 6,000 to about **15,000**, and its last 20 records average a placement of **1.60 with 80% first places**, better than the server's ten highest-rated players on every reported statistic (2.34, 59%). On TavernBench (960 tasks in 40 scenarios), TavernAgent answers **91%** of play tasks versus at most 63% for frontier LLMs and decides in 0.03 s where they need up to 26 s.

**Key Innovations**:
- Closed-loop LLM research system that improves simulator, opponents, policy, and process.
- Typed shared research memory with verification gates.
- Builds a faithful full-content game simulator from raw data.
- Live-ladder and benchmark evidence that the built agent beats frontier LLMs at play.

---

### 5.2 Text Is the Bottleneck: A Small-Scale Replication of LLM Game Playing in Riichi Mahjong
- **Authors**: Mingge Xu
- **Institution/Company**: The University of Tokyo (author footnote)
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.34791
- **Categories**: cs.CL

**Abstract**: This paper replicates the riichi-mahjong track of “Can Large Language Models Master Complex Card Games?” under a much smaller budget: models of at most **2B parameters**, one **16 GB consumer GPU**, and about **five GPU-days**. With matched data and labels, **text is the bottleneck**: on the same 100k-decision training set, a **2.6M-parameter convolutional board encoder** agrees with the strong AI Mortal on **80.6%** of test decisions, above every text-prompt LLM trained (best 77.8%), and places better at the table (2.85 vs ~3.0 over 1,000 games; not significant at n=100). Scaled to 1.71M decisions, a **4.9M-parameter Transformer** reaches **94.7%** agreement, beats the 0.8B LLMs on identical seeds (−0.45 ranks, p=0.005), and is statistically equivalent to parity against three Mortal champions. Training toward the teacher raises agreement more than a 2.5× parameter increase (+2.5 vs +1.5 points). The paper also documents a paper–code mismatch in the original winner filter and reconstructs two private engine patches.

**Key Innovations**:
- Small-budget replication that isolates representation from scale.
- Shows a compact board encoder outperforms text-prompt LLMs on decisions.
- Separates teacher-agreement gains from actual playing strength.
- Documents reproducibility issues and reconstructs missing engine patches.

---

### 5.3 Game-Theoretic Solvers with Bayesian Opponent Modeling and Moral Rhetoric Framing for GLEE
- **Authors**: Hayden Arnold
- **Institution/Company**: KAIST
- **Date**: 2026-10-27
- **arXiv**: https://arxiv.org/abs/2610.37397
- **Categories**: cs.GT, cs.CL
- **Venue**: IAB Workshop at NeurIPS 2026

**Abstract**: This is the agent submitted to the GLEE competition, which plays bargaining, negotiation, and persuasion games against a shared pool of human and AI opponents. The agent combines a **classical game-theoretic solver** for numeric moves, an **online Bayesian layer** to estimate opponent archetypes, and a **language model** to write messages. It uses Rubinstein bargaining, Faratin concession, and Kamenica–Gentzkow disclosure, adapting them to live opponents through a Bayesian estimate of hidden discount factor, reservation value, or signaling reliability, plus a **Thompson-sampling bandit over five moral-foundation framings** coupled with an evidence–intuition spectrum. The paper reports failure modes and guardrails from live play, 13,200 Monte Carlo games against 11 synthetic archetypes, an ablation of opponent modeling, and an analysis of 9,337 live messages in which moral-rhetoric framing is strongly correlated with purchase (χ² = 616.7, p ≈ 3.7×10⁻¹³²), surviving controls for quality, round, and configuration.

**Key Innovations**:
- Hybrid classical solver + Bayesian opponent model + LLM-generated messages.
- Online estimation of hidden game parameters rather than fixed archetypes.
- Thompson sampling over moral-foundation framings for persuasion.
- Large live-message analysis linking rhetorical framing to purchase outcomes.

---

### 5.4 UnityBench-Mini3D: Evaluating LLM Agents for 3D Game Development in Unity
- **Authors**: Yijun Zhou, Minghao Shao, Ke Zhang, et al.
- **Institution/Company**: Unity China; New York University; University of Chinese Academy of Sciences; Xiamen University; Columbia University; Peking University; The Hong Kong University of Science and Technology
- **Date**: 2026-10-26
- **arXiv**: https://arxiv.org/abs/2610.35980
- **Categories**: cs.SE, cs.AI, cs.LG

**Abstract**: Game development stresses coding agents differently from general software engineering: correctness depends on how engine APIs, serialized scene state, and runtime behavior interact, not on source code alone. Existing benchmarks mainly target platforms such as Godot and rely heavily on LLM judges or coarse task-level outcomes. **UnityBench-Mini3D** contains **77 project-level Unity tasks** organized around seven expert-defined skill categories and three difficulty tiers. Each task pairs a complete Unity project with natural-language requirements and is evaluated with **1,178 held-out, human-authored milestone tests** covering scene structure, component configuration, and runtime behavior. In-engine evaluation gives deterministic partial credit and localizes failures without subjective judges. Across **21 models and 9 coding harnesses**, average pass rate is **80.9% on easy tasks**, **35.2% on hard tasks**, and **57.7% overall**.

**Key Innovations**:
- In-engine milestone tests instead of LLM-as-judge or final-state checks.
- Skill-based task taxonomy spanning scene, component, and runtime behavior.
- Deterministic partial credit that localizes failures.
- Large cross-model/cross-harness evaluation with a clear difficulty gap.

---

## 6. Companion coverage (already in the wiki)

The following same-window papers are already summarized in the [2026-10-29 arXiv Paper Check](./arxiv-paper-check.md). They are listed here for completeness; this report does not re-summarize them.

| arXiv | Paper | One-line result |
|-------|-------|-----------------|
| [2610.37140](https://arxiv.org/abs/2610.37140) | Rethinking Positional Encoding and Interaction Granularity for CTR Prediction (TRIP) | Target-aware rank–time encoding + temporal group-causal interaction, up to +4.45% relative AUC |
| [2610.37286](https://arxiv.org/abs/2610.37286) | LESSRec | Level-specific semantic-ID history modeling; attention restricted to the target token's semantic level |
| [2610.36973](https://arxiv.org/abs/2610.36973) | KL-MOPD | Token-wise KL-weighted multi-objective on-policy distillation for generative recommendation; online ads A/B |
| [2610.36958](https://arxiv.org/abs/2610.36958) | PailitaoMMSearch2.0 | Deployed Taobao multimodal generative retrieval; +17.90% PV, +27.04% transactions, +8.94% GMV |
| [2610.36890](https://arxiv.org/abs/2610.36890) | Refiner | Latent residual reasoning for generative ranking; cumulative additive score corrections with LoRA |
| [2610.36000](https://arxiv.org/abs/2610.36000) | RELAY | One query, two roles for sequential recommendation; +14.22% Recall@5, 65.12% smaller predictor |
| [2610.36020](https://arxiv.org/abs/2610.36020) | Roblox exploratory creative pre-ranking | Hierarchical empirical-Bayes Thompson sampling; +8.14% predicted play-through rate, deployed |
| [2610.36408](https://arxiv.org/abs/2610.36408) | Cross-Day Compatibility of Daily Item Embeddings | Quantifies embedding drift; daily global rescaling +4.0% GAUC in industrial CTR |
| [2610.37228](https://arxiv.org/abs/2610.37228) | AutoRSE | LLM agents as recommendation engineers; +16.1% average but mostly engineering optimization |
| [2610.36114](https://arxiv.org/abs/2610.36114) | Context Is a Pipeline, Not a Window | Tool-output truncation cuts 3,827/11,189 results; yield falls 0.61 → 0.31 |

## 7. Cross-cutting observations

1. **The input side is back.** OptIDC, the temporal calibration study, and BehaveRec all show that gains can come from what enters the model and how it is evaluated, not only from a new interaction block. This is a useful counterweight to architecture-only CTR work.
2. **Industrial papers increasingly report deployment boundaries, not just averages.** BehaveRec derives a ~20-interaction rule and flags a mixed item-level result; HiRank reports an online orders-per-user lift; RLBP reports a two-month holdout. These are more actionable than a single offline AUC delta.
3. **Generative recommendation is optimizing compute, not just quality.** LoopGR's recurrent depth and 52% size reduction follow the same serve-time-cost logic seen in Deco, OneLatent, and TCBSA. The shared bet is that a smaller or shallower generator with better state handling can beat a larger one-shot model.
4. **Auction theory is closing gaps that matter for generative interfaces.** The factor-6 and factor-2 mechanisms both handle general cascade click models, and the latter explicitly targets multi-slot sponsored placement inside AI-generated answers. This is mechanism design for the surface where LLM advertising will actually run.
5. **LLM systems research is converging on localized numerical fixes.** EnergyCal, GateRQ, balanced state subspaces, and the Edge-of-Convexity analysis all identify a specific numerical or state-management failure rather than proposing a new backbone. Each reports a concrete memory, stability, or throughput win.
6. **Agent memory is splitting into content and control.** ETAMem improves what is stored and how it is retrieved; DiscernMem learns when a memory should be used; ProactMem validates regularities before acting. The common lesson is that storage alone is not memory utility.
7. **Games expose interface and representation bottlenecks.** AutoTavern shows LLM agents can build a better player than they can be; Riichi shows compact board encoders beat text prompts under matched data; UnityBench shows coding agents still collapse on hard engine-level tasks. The bottleneck is often the representation or harness, not the model's general capability.

## 8. Caveats and open questions

- **Abstract-only review.** Full papers were not read; architectures, baselines, and statistical validity were not independently checked. All performance numbers are author-reported.
- **Window and coverage.** Listings covered 2026-10-22 to 2026-10-28, with the featured set concentrated on 2026-10-23 to 2026-10-27. The sweep is a snapshot, not a complete census.
- **Companion overlap.** Ten same-window papers are already in the [2026-10-29 arXiv Paper Check](./arxiv-paper-check.md) and are only cross-referenced here. This report deliberately avoids duplicating their summaries.
- **Institution attribution is conservative.** `2610.37062` and `2610.37280` list no structured affiliation on arXiv; `2610.34791` is identified only through an author footnote. Affiliations for multi-institution papers may omit corresponding-lab details.
- **CTR/ads coverage is broader than in the previous window.** This sweep has dedicated CTR work (OptIDC, temporal recalibration), production auto-bidding (RLBP), and two cascade-auction mechanism papers. It still lacks a pure CTR-scaling architecture paper; the closest are HiRank and the companion TRIP paper.
- **Open question for the wiki:** whether BehaveRec's ~20-interaction deployment threshold transfers across domains, and whether LoopGR's recurrent-depth scaling compounds with the concept-bottleneck and latent-reasoning patterns already tracked in the wiki.
