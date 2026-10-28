---
title: arXiv AI Search - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-10-26)
type: synthesis
created: 2026-10-26
updated: 2026-10-26
sources: [arxiv.org]
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, generative-recommendation, auctions, agents, memory, moe, scaling-laws, rl]
---

# arXiv AI Search - AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games (2026-10-26)

> Generated: 2026-10-26 | Effective submission window: 2026-10-22 to 2026-10-23 (latest indexed mailing at query time)
>
> A curated sweep of recent arXiv submissions across AI, LLMs, recommendation, advertising, CTR, sequential modeling, and games. Abstracts below are condensed from arXiv; institutions are parsed from the rendered author blocks or PDF author pages, never inferred. Where no affiliation is listed, the field says so explicitly.

## Summary

- **Generative recommendation is optimizing the decoder, not just the generator.** Deco separates history reading from semantic-ID writing and moves beam search to a light decoder; parallel semantic-ID recommenders get item-space and code-space distillation; TCBSA injects a frozen discriminative ranker into beam decisions; TGR-EvoDAG lets LLM agents evolve the entire tokenization → pretraining → alignment pipeline. The shared target is inference cost and beam-search quality, not another backbone.
- **Industrial recommendation is turning reasoning into a serving problem.** OneLatent compresses explicit Chain-of-Thought into latent tokens at Kuaishou, reporting 17× higher inference throughput and a 9.6% revenue lift in local-services advertising. HGE (Meituan) attacks a different production mismatch: ranking containers (livestream rooms/stores) while transactions happen at item level.
- **Advertising research is expanding beyond CTR into mechanism and platform design.** This window has LLM-platform ad/subscription menu design, differentiable combinatorial auctions, and posted-price guarantees in two-sided markets. No dedicated CTR-prediction paper appeared; the closest industrial entries are HGE (GTV/conversion) and OneLatent (ads).
- **LLM training work is now about numerical and data-efficiency edges.** AMD closes most of the MXFP4-vs-BF16 gap for a 20B MoE; LARE reweights domain losses instead of rescheduling data; rounding-location alignment stabilizes BF16 RL; on-policy self-training removes human QA data; a rewriting scaling law predicts how much compute to spend on synthetic data.
- **Agents are being evaluated as systems, not just models.** Memory gets an IR-native taxonomy (AMM) and a graph-diffusion implementation (ActionRAG); MCP fault injection shows a 120B model is not more fault-tolerant than a 20B one; Frontier-OPD selects teacher interventions at the student's learning frontier.
- **Sequential and game settings remain the clean testbeds for state, timing, and allocation.** BGAFlow personalizes cross-domain transfer with a Bezier-guided flow; PlayerEmbed learns behavioral fingerprints from raw game inputs; halting heads are shown to overstate compute savings under batched generation; Werewolf agents learn when to speak; Markets of Minds allocates expert reasoning as a scarce resource.

## Methodology and scope

- **Source sweep**: arXiv Export API queries for `cs.IR`, `cs.CL`, `cs.AI`, `cs.GT`, `cs.LG`, and `cs.MA` (120 most recent entries each), deduplicated to **637 unique arXiv IDs**. The newest indexed submissions were dated **2026-10-23**, so the effective window is **2026-10-22 to 2026-10-23**.
- **Selection**: title/abstract screening for recommendation, advertising/auctions, CTR/conversion, sequential modeling, LLM training and agents, and games. **24 papers** were selected for this report. All 24 IDs were checked against the existing `wiki/` tree and had **zero prior hits** at write time.
- **Metadata**: titles, authors, abstracts, dates, and categories come from the arXiv API. Affiliations were parsed from `arxiv.org/html` author blocks, with PDF first-page extraction used when HTML was unavailable (`2610.32141`, `2610.32951`). `2610.32980` lists no affiliation on arXiv.
- **Caveats**: this is an **abstract-only** review; all numbers are author-reported and were not independently reproduced. Venue labels follow the arXiv comments. A same-window advertising paper, **Click Thinning** (`2610.30999`), was already featured in the [2026-10-23 arXiv AI Search](../2026-10-23/arxiv-ai-search.md) and is cross-referenced rather than re-summarized.

---

## 1. Recommendation and Generative Recommendation

### 1.1 Separating Thinking from Spelling for Efficient Generative Recommendation (Deco)
- **Authors**: Danil Gusak, Anna Volodkevich, Ivan Oseledets, Evgeny Frolov
- **Institution/Company**: Not listed on arXiv
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32980
- **Categories**: cs.IR

**Abstract**: Generative recommenders write semantic IDs (SIDs) code by code under trie-constrained beam search. Standard autoregressive interfaces pay for SID length twice: a history of `T` items enters the backbone as `T·K` code tokens, and every beam step runs through the backbone, so `B` candidates cost `O(B·K)` heavy decode tokens per user. Deco separates reading the history from writing the identifier: the backbone reads each item as one fused token, condenses the history once into a compact next-item concept, and a light KV-cached decoder conditioned on that concept runs the entire beam search while keeping the SID factorization and trie unchanged. On seven e-commerce, movie, and music datasets, Deco matches or beats both a standard generative recommender and its full-backbone teacher, delivering 3.2–8.6× throughput under a 50 ms p95 budget. It generates 1,000 candidates faster than its teacher generates 100; with a 1.5B LLM backbone it matches a 69M teacher's throughput at higher accuracy.

**Key Innovations**:
- Concept bottleneck: one backbone pass produces a compact `z`, and all beam search happens in a light decoder.
- Heavy/light decoupling preserves SID trie constraints while removing `O(B·K)` backbone decode cost.
- Training uses cross-entropy alone; distillation from the full-backbone teacher is optional and improves accuracy further.
- Production-style serving evidence that larger candidate pools and stronger backbones become practical.

---

### 1.2 Knowledge Distillation across Item and Code Spaces for Parallel Generative Recommendation
- **Authors**: Yixuan Xu, Hailin Liu, Linxiang Peng, Can Yang
- **Institution/Company**: The Hong Kong University of Science and Technology; University of Science and Technology of China
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32943
- **Categories**: cs.IR

**Abstract**: Semantic-ID recommenders usually train on hard labels for the observed next item, which identifies the target but gives no distributional information about alternative items. Sequential recommenders can provide item-level predictive knowledge, but transferring it into code generation is hard because teacher and student live in item and code spaces. The paper proposes two distillation objectives for parallel semantic-ID recommenders that predict all code positions simultaneously. **Item Distribution Matching (IDM)** reconstructs a catalogue-level item distribution from the student's parallel code predictions and aligns it with the teacher's item distribution. **Code Marginal Matching (CMM)** projects teacher item probabilities onto each code position through fixed item-to-code assignments and matches the resulting code marginals to the student heads. Both preserve the parallel prediction structure. IDM improves Recall@10 by 15.39% on average; CMM improves NDCG@10 by 8.28%.

**Key Innovations**:
- Item-space distillation for a code-space student via distribution reconstruction.
- Code-marginal distillation using fixed item-to-code assignments.
- Both objectives keep parallel (non-autoregressive) decoding intact.
- Consistent gains over hard-label SOTA on benchmark datasets.

---

### 1.3 TGR-EvoDAG: A DAG-based Multi-Agent Code Evolution Framework for Generative Recommendation on Tencent
- **Authors**: Junlin He, Junzhang Zhu, Yudong Li, Yihong Tang, Xuefeng Jiang, Wei Ma, Chengxiang Zhuo, Zang Li
- **Institution/Company**: Tencent Platform and Content Group; The Hong Kong Polytechnic University; McGill University; Independent Researcher
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32326
- **Categories**: cs.AI, cs.IR

**Abstract**: LLM agents enable automated code evolution, but applying recursive self-improvement to generative recommendation (GR) is difficult because GR is a module-cascaded pipeline (tokenization, pretraining, alignment), not an end-to-end model. General frameworks lack domain feedback; recommender-specific frameworks use linear evolution and are cost-blind to stage-asymmetric retraining. TGR-EvoDAG models code evolution as a directed acyclic graph, keeps multiple branches, merges complementary innovations, and combines search with GR diagnostic feedback. Stage-aware cost planning optimizes GPU-hour budgets, and active downstream co-adaptation lets promising upstream changes survive temporary regressions. On public Amazon data it improves offline metrics by up to 37.4% and Agent4Rec simulated user satisfaction by 19.7% over the strongest baseline. In Tencent's commercial media platform, the evolved GR achieves +12.16% relative offline Hit@1 and a statistically significant +0.40% online CTR.

**Key Innovations**:
- First autonomous evolution of a complete GR pipeline (tokenization → pretraining → alignment).
- DAG-structured multi-agent search instead of linear self-improvement.
- Stage-aware GPU-hour planning and downstream co-adaptation to avoid short-sighted pruning.
- Both public benchmark and Tencent production deployment evidence.

---

### 1.4 From Item Scores to Semantic Tokens: Test-Time Collaborative Adaptation for Generative Recommendation (TCBSA)
- **Authors**: Xiongfeng Shan, Xing Tang, Hanchong Chen, Fuyuan Lyu, Lingjie Li, Jingyan Jiang, Duguang Liu, Xiuqiang He
- **Institution/Company**: Shenzhen Technology University; McGill University; Shenzhen University
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32098
- **Categories**: cs.IR

**Abstract**: Generative recommenders make successive semantic-token decisions, and beam search can irreversibly prune promising item paths, especially when recent interactions signal an emerging interest. An independently trained discriminative recommender may rank the same items highly from the same history and is available at test time. TCBSA is a training-free method that injects these collaborative scores into semantic decoding: it transforms discriminative score margins into potentials over shared semantic edges and uses a confidence gate to regulate their contribution to cumulative path scores before beam selection. The paper gives a sufficient condition for target-prefix survival under global beam competition and bounds score perturbations under low discriminative confidence. Full-catalog experiments show consistent gains across datasets and across generative/discriminative recommender pairs, with better accuracy–latency trade-offs than simply widening the beam.

**Key Innovations**:
- Test-time coupling of a frozen generator with a frozen discriminative ranker; no retraining.
- Converts item-level score margins into prefix-level potentials before beam pruning.
- Confidence-gated correction with a prefix-survival guarantee.
- Gains on emerging-interest cases and better cost than native beam widening.

---

### 1.5 OneLatent: Latent Reasoning for Efficient Foundation Recommendation Models
- **Authors**: Hao Jiang, Peiru Du, Pengfei Yao, Mengting Li, Siyuan Lou, Kuo Cai, Sheng Yu, Qiang Luo, Jian Liang, Ruiming Tang, Fei Pan, Peng Jiang, Wenwu Ou
- **Institution/Company**: Kuaishou Technology
- **Date**: 2026-10-22
- **arXiv**: https://arxiv.org/abs/2610.30675
- **Categories**: cs.IR

**Abstract**: LLM-based foundation recommendation models (FRMs) improve recommendations through explicit Chain-of-Thought under a Think-then-Answer paradigm, but explicit CoT is expensive and relies on hand-designed templates that struggle with diverse user interests. OneLatent compresses explicit reasoning traces into several learnable latent tokens, enabling Latent-Reason-then-Answer inference without verbose traces. It introduces Multi-View Adaptive CoT (MV-ACoT) to generate diverse teacher supervision with instance-adaptive complexity, then uses three-stage latent-token alignment to internalize traces, followed by curriculum-based post-training. On an industrial Kuaishou dataset and the public Kuaishou LLM-Rec benchmark, OneLatent improves SID@64 by 17.44% over Think and 9.33% over No-Think FRMs while achieving over 17× higher online inference throughput. A production serving system supports real-time FRM inference; an online A/B test in Kuaishou local-services advertising reports an estimated 9.6% revenue lift over strong baselines including OneRec and OneReason.

**Key Innovations**:
- Latent-token reasoning replaces long explicit CoT traces at inference.
- Multi-view, complexity-adaptive teacher trace generation.
- Three-stage alignment plus curriculum post-training for downstream recommendation.
- Production serving system and advertising A/B revenue evidence.

---

### 1.6 Hierarchical GTV Estimation: Bridging the Gap between Container-Level Ranking and Item-Level Conversion (HGE)
- **Authors**: Zerong Lan, Fan Zhang, Chuang Chen, Tianchun Huang, Teng Zhang, Xingxing Wang
- **Institution/Company**: Meituan
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32420
- **Categories**: cs.IR
- **Venue**: RecSys 2026

**Abstract**: Container-based e-commerce (livestream rooms, O2O stores) ranks and estimates at the container level while transactions occur at the item level. This granularity mismatch makes Gross Transaction Value (GTV) estimation suffer from high label variance, label sparsity, and dynamic item heterogeneity. HGE uses a Hybrid Set-Aware Encoder (HSAE) to model dynamic item composition and feature interactions, Proxy-Label Learning (PLL) to decompose post-click GTV into purchase probability, quantity, and unit price, and Residual Correction and Ensemble Fusion (RCEF) to combine item-level aggregation with container-level inference under sparsity. On large industrial data, HGE reports +0.63% offline XAUC and +1.42% online Revenue Per Search in A/B tests, and is fully deployed in main traffic.

**Key Innovations**:
- Explicit modeling of the container-vs-item granularity mismatch for GTV.
- Set-aware encoder for dynamic item composition.
- Proxy-label decomposition of GTV into interpretable purchase components.
- Residual/ensemble fusion for sparse item-level labels; full production deployment.

---

## 2. Advertising, Auctions, and Market Design

### 2.1 Monetizing Intelligence: Advertising and Subscription Design on LLM Platforms
- **Authors**: Yuhang Ji, Fasheng Xu, Tianjun Feng
- **Institution/Company**: Fudan University (School of Management); University of Connecticut (School of Business)
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32945
- **Categories**: econ.TH, cs.AI

**Abstract**: LLM platforms that introduce advertising must jointly choose costly response quality, advertising intensity, and subscription prices when ads reduce user value but better service raises ad returns. The paper studies a monopolistic platform and derives three results. First, when partly ad-supported and ad-free plans coexist, advertising can finance useful service for consumers who would receive none under pure subscription; lower effective quality in middle plans weakens premium users' alternatives and allows higher ad-free prices, so broader access can coexist with utility polarization. Second, an intermediate advertising cap can maximize consumer surplus by preserving revenue while limiting degradation. Third, cheaper compute can raise quality and reduce ad intensity, yet sufficiently large cost reductions can increase aggregate ad revenue because better service raises the value of remaining advertised interactions. Menu design, not just ad exposure, determines who gains and loses.

**Key Innovations**:
- Joint quality/ad-intensity/subscription model for LLM platforms.
- Cross-subsidy and utility-polarization results for mixed ad-supported menus.
- Non-monotone effect of compute cost on ad revenue.
- Policy lever: an intermediate ad cap can improve consumer surplus.

---

### 2.2 Differentiable Combinatorial Auction Design: Optimizing Revenue-Welfare-Fairness Frontiers with Graph Attention Networks
- **Authors**: Mai Pham, Vikrant Vaze, Peter Chin
- **Institution/Company**: Dartmouth College (Thayer School of Engineering)
- **Date**: 2026-10-22
- **arXiv**: https://arxiv.org/abs/2610.31977
- **Categories**: cs.GT, cs.LG

**Abstract**: Public-infrastructure auctions (airport slots, energy resources) involve interdependent resources and complex side constraints. VCG maximizes welfare but cannot optimize revenue or multi-objective trade-offs. The paper proposes a differentiable, constraint-aware framework for end-to-end learning of fractionally feasible, approximately strategy-proof mechanisms. Its main contribution is a combinatorial constraint-enforcement technique that guarantees fractional feasibility by construction, avoiding penalty approximations. It introduces CAGraph, a graph architecture capturing item–bidder dependencies, plus CANet and CAFormer baselines, and a Matching-Pursuit-inspired decomposition from fractional to discrete allocations with an empirical discretization-gap analysis. On synthetic benchmarks and an airport slot-divestiture case study, learned mechanisms achieve up to 73.5% and 180% higher expected revenue than VCG under small empirical regret, with visualized revenue–welfare–fairness Pareto frontiers.

**Key Innovations**:
- Feasibility-by-construction for learned combinatorial auctions.
- Graph attention over item–bidder dependencies (CAGraph).
- Learned mechanisms can trade revenue, welfare, and fairness explicitly.
- Fractional-to-discrete allocation decomposition and discretization-gap evaluation.

---

### 2.3 Balanced Posted Prices in Stationary Two-Sided Markets
- **Authors**: Ilan Reuven Cohen
- **Institution/Company**: Bar-Ilan University
- **Date**: 2026-10-22
- **arXiv**: https://arxiv.org/abs/2610.31153
- **Categories**: cs.GT

**Abstract**: An intermediary buys nonperishing items from arriving sellers and sells to arriving buyers under limited storage; both sides arrive as independent Poisson processes, and the intermediary pays and charges the same fixed item prices to maximize long-run gains from trade. The benchmark can choose allocations directly, has unlimited storage, and must purchase before allocating; its optimal gain rate equals a linear program over average purchase/allocation rates. For buyers with XOS bundle valuations, the paper computes static common prices that guarantee half of this benchmark for arbitrary finite item capacities, even one storage slot per item, independent of tie-breaking and without future knowledge. Prices are polynomial-time computable from demand and supporting-value queries. The construction equalizes itemwise lower bounds on buyer and seller contributions ("contribution balance") and, in the single-item case, equalizes selected purchase and sale rates ("rate balance"), yielding the tight guarantee `C/(C+1)` for capacity `C`.

**Key Innovations**:
- Constant-factor posted-price guarantees for recurring two-sided markets with storage.
- Contribution-balance and rate-balance principles adapted from prophet inequalities.
- Works with XOS valuations, arbitrary finite capacities, and no future arrivals.
- Polynomial-time price computation from demand/supporting-value queries.

---

## 3. LLM Training, Post-Training, and Inference

### 3.1 Training an MoE LLM in MXFP4: How We Closed the Gap to BF16 (ALTO)
- **Authors**: Han Wang, Zhitao Wang, Natalia Frumkin, Xuanwu Yin, Alireza Khodamoradi, Dong Li, Emad Barsoum
- **Institution/Company**: Advanced Micro Devices (AMD)
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32229
- **Categories**: cs.AI

**Abstract**: Training LLMs in sub-8-bit arithmetic promises memory-bandwidth and compute gains, but FP4 quantization error can destabilize optimization. ALTO is an open-source training recipe for GPT-OSS-20B, a 20B-parameter MoE, on the MLPerf Small MoE Training benchmark under MXFP4 microscaling. It combines hybrid 1D/2D block quantization, randomized Hadamard transforms, and stochastic rounding with a simplified weight de-oscillation scheme. On C4 validation at global batch size 16, MXFP4 + RHT + SR + de-oscillation reaches loss 3.3350 at 16,128 steps, only 0.007 above the BF16 baseline (3.3283), closing roughly half the gap left by MXFP4 without de-oscillation (3.3418). Steps to the MLPerf quality target cut FP4 convergence overhead from +20.0% to +5.0% relative to BF16. The paper also reports negative end-to-end results for differential gradient estimation, outlier clipping, and macro-block scaling despite operator-level SNR gains. Experiments use simulated MXFP4 kernels on AMD MI300; wall-clock speed is not optimized.

**Key Innovations**:
- Open MXFP4 recipe that brings a 20B MoE within 0.007 validation loss of BF16.
- Weight de-oscillation cuts convergence overhead to +5%.
- Honest negative results for three plausible FP4 stabilizers.
- Simulated-kernel study on AMD MI300, not a production speed claim.

---

### 3.2 Beyond Data Schedule: Fast LLM Pretraining on Data Mixtures by Loss-Reweighting (LARE)
- **Authors**: Jiazheng Li, Huaqing Zhang, Jing Xu, Tianle Cai, Jingzhao Zhang
- **Institution/Company**: Tsinghua University; ByteDance Seed
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32141
- **Categories**: cs.LG, cs.CL

**Abstract**: Successive pretraining stages add capabilities but can forget earlier knowledge. The paper asks whether changing how strongly each domain contributes to learning — while keeping its data exposure fixed — improves this trade-off. In controlled knowledge–mathematics experiments, loss reweighting produces a single checkpoint that surpasses the best knowledge and reasoning scores from either stage trajectory, revealing a control independent of data-mixture ratios. LARE (Loss-Adaptive Reweighting under fixed Exposure) adjusts domain weights from running loss statistics; its normalized inverse-square-root rule balances relative loss scales without changing the sampled mixture or requiring extra search runs. Across knowledge, mathematics, and code, LARE improves all five benchmarks for a 1.5B model trained on 240B tokens, averaging +7.84 pp over a matched direct mixture, including +17.06 pp on GSM8K and +9.00 pp on MATH.

**Key Innovations**:
- Loss reweighting as an independent control from data-mixture scheduling.
- LARE adapts domain weights online from running loss statistics.
- No extra hyperparameter search or change to sampled data exposure.
- Gains across knowledge, math, and code without a larger model or more tokens.

---

### 3.3 Where Rounding Happens Matters: Rounding-Location Alignment Stabilizes LLM Reinforcement Learning
- **Authors**: Yijing Ke, Tianle Cai, Ruosong Wang
- **Institution/Company**: ByteDance Seed; Peking University
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32951
- **Categories**: cs.LG

**Abstract**: RL for LLMs uses separate inference and training systems. Even with identical weights and BF16 tensors, implementation differences can make an intended on-policy update off-policy and destabilize training. Existing remedies align the whole stack, change global precision, or modify the learning algorithm. This paper asks whether aligning selected parts of the execution stack is enough. It aligns training-side rounding locations with inference in three regions — RoPE, SwiGLU, and residual RMSNorm — by keeping selected intermediates in FP32 until their BF16 outputs. Across four Qwen-family models, aligning all three regions prevents the collapse seen in the default BF16 baseline; RoPE-path alignment alone also suffices in the studied runs despite remaining numerical discrepancies. The inference engine, matmul/attention kernels, and learning objective are unchanged.

**Key Innovations**:
- Localizes RL instability to rounding-location mismatch rather than global precision.
- Three targeted FP32-retention interventions: RoPE, SwiGLU, RMSNorm.
- Demonstrates a cheap partial alignment can recover stability.
- Does not require changing the inference engine or RL objective.

---

### 3.4 On-Policy Self-Training: Data-Free Self-Improvement in Large Language Models
- **Authors**: Leon Sick, Lukas Hoyer, Yannick Strümpler, Christian Reisswig, Timo Ropinski, Federico Tombari
- **Institution/Company**: Google; Ulm University
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32770
- **Categories**: cs.CL, cs.AI

**Abstract**: On-policy self-distillation can post-train foundation models without a stronger external teacher, but existing methods rely on ground-truth QA pairs, human-curated problem sets, or other supervised signals. This paper reformulates on-policy self-distillation as self-training driven by self-generated question–answer pairs and privileged reasoning demonstrations. Guided only by coarse, high-level topic descriptions, the model synthesizes its own curriculum of queries and privileged reasoning traces without human-curated prompts or answers. Self-distillation on fully synthetic privileged information improves the model across multiple domains while retaining capabilities on domains it is not self-trained on. The framework is demonstrated on text and multimodal tasks, with consistent gains on standard language benchmarks and Visual Question Answering.

**Key Innovations**:
- Removes human QA pairs and curated problem distributions from on-policy self-distillation.
- Topic-only curriculum synthesis with privileged reasoning traces.
- Cross-domain improvement without catastrophic forgetting in tested settings.
- Works for both text and multimodal (VQA) post-training.

---

### 3.5 Rewriting Scaling Laws for Synthetic Data with Compute and Data Constraints
- **Authors**: Nicholas Roberts, Ahmed Ahmed, Suhas Kotha, Percy Liang, Yu Wang, Alex Renda, Nitya Mani
- **Institution/Company**: Princeton University; Stanford University; Jane Street
- **Date**: 2026-10-22
- **arXiv**: https://arxiv.org/abs/2610.31867
- **Categories**: cs.LG, cs.CL

**Abstract**: Synthetic rewrites — a language model rewriting a natural document into a target style — are now standard in pretraining corpora, but how much compute should be spent rewriting, and whether a model trained on rewrites can beat the rewriter, are poorly understood. The paper proposes a rewriting scaling law predicting loss from model size, training tokens, rewrite fraction, and epochs over natural data, while charging the compute spent generating rewrites. In the compute-limited setting, the estimated optimal rewrite fraction rises with compute from under 10% at 3×10^18 FLOPs to 32% at 10^22 FLOPs. A 33× FLOP extrapolation to a 22B model lands within 1.1% of forecast and beats its rewriter's BPB on several web domains at one-tenth the rewriter's training compute. In the data-limited setting, with a same-size rewriter pretrained on a fixed seed set, the optimal rewrite fraction also rises with compute; up to 3B parameters, models trained on rewrites of their own pretraining data beat the best natural-data-only run at every size.

**Key Innovations**:
- Scaling law that includes rewrite fraction, epochs, and rewrite-generation compute.
- Predicts the optimal synthetic-data fraction as a function of compute budget.
- Shows a target model can outperform a stronger rewriter at lower training compute.
- Validated in both compute-limited and data-limited regimes up to 3B/22B scales.

---

## 4. LLM Agents, Memory, and Retrieval

### 4.1 Agentic Memory Management Is the Next Frontier of Information Retrieval
- **Authors**: Qingyao Ai
- **Institution/Company**: Tsinghua University
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32464
- **Categories**: cs.IR
- **Type**: Perspective paper

**Abstract**: As AI agents consume, retain, and act on information on a user's behalf, information management increasingly happens inside the agent as memory management. This perspective argues that **agentic memory management (AMM)** — the structure, analysis, organization, storage, searching, retrieval, and use of information in an agent's memory — is a natural extension of IR research. It presents a system-level AMM framework and a computational taxonomy of memory objects as **constants**, **functions**, and **operators**, each with distinct retrieval semantics. It compares AMM with established IR and outlines a research agenda: benchmarks, candidate principles of memory utility, and optimization procedures that mix parametric and non-parametric updates.

**Key Innovations**:
- Defines AMM as an IR-native research area rather than an ad hoc agent feature.
- Constants/functions/operators taxonomy for memory objects and retrieval semantics.
- Research agenda spanning benchmarks, utility principles, and hybrid parametric/non-parametric updates.
- Positions the IR community as a natural owner of agent-memory problems.

---

### 4.2 ActionRAG: Evidence-Refining Graph Diffusion for Long-Term Memory in LLM Agents
- **Authors**: Navyansh Mahla, Sashank Vandrangi
- **Institution/Company**: Actioneer
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32752
- **Categories**: cs.AI, cs.CL

**Abstract**: LLM agents need long-term memory that recovers precise, mutually consistent evidence from growing interaction histories, especially when answers depend on relations among facts. Current pipelines fail at two stages: indexing can fragment repeated entities or merge distinct ones, and online retrieval treats initial similarity scores as final even when graph context supports revision. ActionRAG couples cautious indexing with query-time graph retroevaluation. Indexing reconciles type labels and applies tiered entity resolution. For a query, dual-channel entity and triple retrieval forms an initial evidence set and induces a bounded local graph; query-conditioned receiver-normalized diffusion refines triple scores using local path structure. Seed protection, hub-penalized flux, and triple materialization preserve direct evidence while recovering missed connections. On MemoryAgentBench's eight deterministic-scoring columns, ActionRAG averages 55.1 accuracy, +5.4 points over the strongest retrieval-based memory baseline; mean synthesis cost stays below $0.001 per query, with retrieval-side p99 components summing to 440.7 ms on consumer Apple Silicon.

**Key Innovations**:
- Tiered entity resolution to reduce index-time fragmentation/merging errors.
- Query-time diffusion over a bounded local evidence graph.
- Seed protection and hub penalties to avoid drift toward high-degree hubs.
- Strong accuracy with explicit query-time cost and latency accounting.

---

### 4.3 Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance
- **Authors**: Antonio Ken Iannillo, Joshua Segun Owotogbe, Roberto Natella, Francesco Avallone, Kristina Kudryavtseva, Indika Kumara
- **Institution/Company**: University of Luxembourg (SnT); Tilburg University; Gran Sasso Science Institute; University of Naples Federico II
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32555
- **Categories**: cs.SE, cs.AI
- **Venue**: NeurIPS 2026 (poster)

**Abstract**: LLM agents depend on external tools exposed via the Model Context Protocol (MCP), but existing benchmarks assume tools respond correctly and on time. The paper introduces MCP-Injector, a drop-in, protocol-aware fault-injection middleware with controlled persistence (permanent, transient, intermittent) and seedable schedules. Its fault model is calibrated to the observed incident distribution of the public MCP ecosystem, mined from 57,240 issue/PR threads across 1,774 open-source MCP repositories. In a 1,350-cell experiment crossing two backbone sizes (20B, 120B), three agent stacks, and three fault conditions, faults from this permanent-heavy profile cause severe degradation: task-completion score falls by 60%, from 8.08 to 3.23 out of 10. Scale does not buy fault tolerance: the 120B model retains no larger share of its fault-free score (resilience-ratio model, p = 0.96), and its completion rate under faults is if anything lower (91.1% vs. 95.6%; difference 4.4 points, 95% CI [−0.2, 9.3]). Agent stacks differ in fault absorption, suggesting framework-level error handling matters more than model scale.

**Key Innovations**:
- Protocol-aware MCP fault injection with realistic persistence and schedules.
- Fault model calibrated on 57,240 real MCP ecosystem threads.
- Large factorial evaluation across model sizes and agent frameworks.
- Evidence that capability benchmarks can mask operational brittleness; scale is not resilience.

---

### 4.4 Frontier-OPD: Discovering the Edge of Agent Capability and Teaching Agents to Go Beyond
- **Authors**: Zheng Jiang, Yiming Chen, Houde Qian, Ling Li, Chaoyang Li, Lifeng Sun
- **Institution/Company**: Tsinghua University
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32802
- **Categories**: cs.CL

**Abstract**: On-policy distillation aligns teacher feedback with a student's current behavior, but useful supervision for multi-turn agents requires identifying both where guidance is needed and whether the student can sustain the interaction afterward. Frontier-OPD targets the student's **learning frontier**: decision situations that remain challenging but admit useful autonomous continuation after brief teacher guidance. It organizes on-policy experience into a shared-state trajectory graph, uses trajectory-balanced aggregation of teacher–student disagreement to identify intervention candidates, and assesses short teacher bridges by comparing agreement over the bridge and the ensuing student continuation against an equally long original-trajectory segment. Accepted teacher responses augment distillation data, and fresh rollouts renew the frontier estimate. ALFWorld, WebShop, and ScienceWorld show higher mean autonomous performance than compared distillation baselines across student scales and teacher configurations; in one ALFWorld timing setting, extra collection cost is offset by shorter time to target success rate.

**Key Innovations**:
- Defines and operationalizes the student's learning frontier for agent distillation.
- Shared-state trajectory graph with trajectory-balanced disagreement aggregation.
- Behavioral proxy for whether teacher guidance is actually absorbable.
- Iterative frontier refresh as the policy changes; evaluated on three agent environments.

---

## 5. Sequential Modeling

### 5.1 Bezier-Guided Adaptive Flow for Cross-domain Sequential Recommendation (BGAFlow)
- **Authors**: Ziang Lu, Yu Zhang, Xinzhe Jiang, Lei Sang, Yiwen Zhang
- **Institution/Company**: Anhui University
- **Date**: 2026-10-22
- **arXiv**: https://arxiv.org/abs/2610.30825
- **Categories**: cs.IR

**Abstract**: Cross-domain sequential recommendation transfers preference knowledge to alleviate sparsity and cold start, but users differ in how consistent their preferences are across domains. Existing global alignment or coarse transfer can inject irrelevant information and adapt poorly per user. BGAFlow combines state-adaptive semantic evolution with user-specific transfer control. It builds a shared semantic space through unified dual-domain pretraining with user profiles inferred by an LLM, estimates a personalized horizon from latent interest overlap to decide how much to transfer, and constructs a conditional Bezier curve as a geometric reference. A learned residual flow progressively refines the trajectory from intermediate preference states, using dynamic preference feedback to adjust transfer direction; recommendation supervision and trajectory regularization encourage effective, smooth adaptation. Experiments on real-world datasets show consistent gains over SOTA.

**Key Innovations**:
- Personalized transfer horizon based on latent interest overlap.
- Conditional Bezier curve as a geometric prior for semantic evolution.
- Residual flow refinement with dynamic preference feedback.
- LLM-inferred user profiles for shared cross-domain pretraining.

---

### 5.2 PlayerEmbed: Learning Behavioral Fingerprint Representations from Raw Input Sequences
- **Authors**: Tobias Schneider, Lorenz Sparrenberg, Priya Tomar, Shahzeb Qamar, Tobias Deußer, Rafet Sifa
- **Institution/Company**: Fraunhofer IAIS; University of Bonn; Lamarr Institute for Machine Learning and Artificial Intelligence
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32727
- **Categories**: cs.LG
- **Venue**: IEEE DSAA 2026

**Abstract**: Raw player input sequences in video games contain fine-grained behavioral signal but are high-dimensional and noisy. PlayerEmbed learns compact, discriminative player embeddings with deep metric learning, using a hybrid CNN-LSTM encoder trained on raw input sequences from 1,000 players. It is evaluated on held-out sequences from those players and on sequences from 1,000 players entirely unseen during training. A nearest-centroid classifier built from reference embeddings reaches balanced accuracies of 0.950 for seen players and 0.879 for unseen players. Systematically increasing the number of training players substantially improves generalization to unseen players, indicating a transition from simple fingerprinting to transferable behavioral patterns.

**Key Innovations**:
- Behavioral fingerprinting directly from raw input sequences, without handcrafted features.
- Hybrid CNN-LSTM encoder with deep metric learning.
- Explicit seen-vs-unseen player generalization protocol.
- Scaling analysis showing transferable behavior emerges with more training players.

---

### 5.3 Do Halting Heads Really Save Compute in Looped Language Models?
- **Authors**: Tsung-Han Wu, Minsuk Heo, Kenny Tan
- **Institution/Company**: Apple
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32246
- **Categories**: cs.CL, cs.LG

**Abstract**: Looped language models run each token through the same layers several times, and a halting head predicts after each iteration whether a token should stop, so easy tokens can exit early. Pretraining models from scratch up to 1.3B parameters, the paper finds two problems. First, heads trained on a mix of all iterations predict that tokens need under half the iterations, yet under the standard stopping rule tokens run almost every iteration, because training never scores the single iteration where a token stops. Scoring every iteration fixes this, but in these runs only with a strong penalty favoring early stops. Second, savings are usually reported as average iterations per token, but batched generation runs until the slowest token stops, so a model without a head is almost as good at that cost; the reported average can overstate the saving. The paper recommends reporting the iterations tokens actually run, with threshold and batch size, and gives a pre-training test that bounds a head's gain.

**Key Innovations**:
- Identifies a train/inference mismatch in halting-head objectives.
- Shows average iterations per token is the wrong metric for batched serving.
- Proposes reporting actual executed iterations with threshold and batch size.
- Provides a pre-training test to bound potential compute savings.

---

## 6. Games and Game-Theoretic Learning

### 6.1 Beyond What to Say: Proactive Utterance Timing with Inner Thoughts for Werewolf Agents
- **Authors**: Yoshiki Tanaka, Shuya Uchiyama, Daichi Hamaguchi, Michimasa Inaba
- **Institution/Company**: The University of Electro-Communications, Tokyo
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32107
- **Categories**: cs.CL, cs.AI
- **Venue**: AIWolfDial Workshop at INLG 2026

**Abstract**: Conversation requires deciding not only what to say but whether to speak at all, and in Werewolf both utterances and silence are interpreted by others. This paper introduces a Werewolf AI agent for the Anytime Utterance Track of the AIWolfDial shared task. It builds on the Inner Thoughts framework, which decides utterance timing by generating internal thoughts and evaluating the value of expressing each thought at the moment. Because the original framework targets general dialogue, the authors redesign it for the competitive, incomplete-information Werewolf setting, calling the adapted method **Adversarial Inner Thoughts**. Experiments analyze self-play logs and human evaluations to assess effectiveness.

**Key Innovations**:
- Treats utterance timing as a first-class action in a social deduction game.
- Adversarial adaptation of Inner Thoughts to incomplete-information competition.
- Combines self-play log analysis with human evaluation.
- Targets the Anytime Utterance shared-task setting rather than turn-by-turn chat.

---

### 6.2 Markets of Minds: A 51-Billion-State Economy of Intelligence
- **Authors**: Jusheng Zhang, Xuekun Wu, Wenhao Wang, Mark Wang, Ming-Hsuan Yang
- **Institution/Company**: Stanford University; Vast Intelligence Lab; University of California, Merced
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32190
- **Categories**: cs.MA

**Abstract**: When intelligence is shared, reasoning becomes a constrained allocation problem: an intervention can help its recipient yet still be a poor use of capacity if another intervention has greater expected value. Markets of Minds allocates expert reasoning across agents before expert outputs are observed. For each agent–service pair it estimates expected gain relative to the agent's default continuation, separating repair benefit from regression risk, and jointly clears assistance contracts under shared resource constraints. The paper studies a dependency-aware agent economy with 51.2 billion addressable persona–market states spanning capabilities, cognitive budgets, provider access, scarcity, and network roles. In a matched replay of 240 cases under a common 30% assistance quota, the frozen allocator reaches 85.42% task-level persona adherence versus 73.86% for equal-capacity random allocation, a gain of 11.56 percentage points. Assistance value is heterogeneous and can be negative; scarcity changes which interventions are worth purchasing.

**Key Innovations**:
- Population-level reasoning allocation instead of independent per-agent assistance.
- Separates repair benefit from regression risk before spending expert capacity.
- Joint contract clearing under shared budgets, access, and scarcity.
- Very large persona–market state space with matched-replay evaluation.

---

### 6.3 Recommender Regret for Improving Regularised RL Estimation with Bandits and MCTS
- **Authors**: Danilo Vucetic, Alexandre Larouche, Mohammad Pedramfar, Audrey Durand, Gauthier Gidel
- **Institution/Company**: Mila – Québec AI Institute; McGill University; Université Laval; Université de Montréal
- **Date**: 2026-10-23
- **arXiv**: https://arxiv.org/abs/2610.32910
- **Categories**: cs.LG, cs.AI

**Abstract**: Regularised RL relies on estimators such as Monte Carlo tree search or one-step look-ahead to provide policy, value, or Q-value estimates, but existing bandit-based frameworks evaluate sampling efficiency rather than estimate quality. This paper formalizes estimate generation as a recommendation process, treating bandit-based sampling as an improvement operator. It defines regulariser-aware **recommender regrets**, analyzes lower bounds, and proves that simple algorithms such as uniform sampling can achieve them. It then unifies bandit- and search-based target improvement under **recommender MCTS**. Across synthetic trees, arcade games, and scientific discovery tasks, recommenders often yield faster target convergence and better downstream performance. The experiments characterize the potential of regularised MCTS in scientific applications.

**Key Innovations**:
- Reframes bandit/MCTS estimate generation as a recommendation problem.
- Introduces regulariser-aware recommender regret with lower bounds.
- Unifies bandit sampling and tree search under recommender MCTS.
- Evaluated on synthetic trees, arcade games, and scientific discovery tasks.

---

## Cross-cutting observations

1. **Serve-time economics dominates recommendation research.** Deco, OneLatent, TCBSA, and TGR-EvoDAG all target the cost or quality of the decode/search stage rather than pretraining a larger recommender. The recurring pattern is to keep a strong frozen component and add a cheap, targeted adaptation layer.
2. **Industrial papers increasingly report production A/B results.** OneLatent (Kuaishou ads), HGE (Meituan search), and TGR-EvoDAG (Tencent media) include deployed-system metrics. Treat these as operational evidence, not independently audited causal claims.
3. **The advertising frontier is mechanism design as much as prediction.** LLM-platform menus, differentiable auctions, and posted-price guarantees are about incentives, feasibility, and allocation. No dedicated CTR model appeared in this window; CTR-adjacent work is embedded in generative recommendation and GTV estimation.
4. **LLM systems research is converging on "alignment of execution details."** FP4 training, BF16 RL rounding, data-loss reweighting, and halting-head accounting all show that small implementation mismatches can dominate headline algorithmic choices.
5. **Agent evaluation is shifting from capability to resilience and memory quality.** MCP fault injection, ActionRAG, AMM, and Frontier-OPD ask whether agents recover, remember consistently, and learn at the right frontier — not just whether they can complete a clean benchmark.
6. **Games remain useful because they expose timing, state, and allocation.** Werewolf tests when to speak, PlayerEmbed tests behavioral identity from sequences, and Markets of Minds tests scarce-assistance allocation. These are clean stress tests for sequential decision-making under partial information.

## Caveats and open questions

- **Abstract-only review.** Full papers were not read; architectural details, baselines, and statistical validity were not independently checked. All performance numbers are author-reported.
- **Window is narrow.** The newest indexed submissions were from 2026-10-23; no 2026-10-24/25/26 mailing appeared at query time. This report is a snapshot, not a complete census.
- **Institution attribution is conservative.** Affiliations were taken from author blocks; `2610.32980` lists none, and multi-affiliation papers may omit corresponding-lab details. No affiliation was inferred from author identity.
- **CTR coverage is indirect.** This window has no dedicated CTR-prediction paper. HGE is conversion/GTV estimation; OneLatent reports advertising revenue but is a recommendation backbone. The 2026-10-23 report's Click Thinning (`2610.30999`) remains the closest LLM-native advertising mechanism paper.
- **Open question for the wiki:** whether the "concept bottleneck" pattern in Deco generalizes beyond semantic-ID recommendation to other structured generation tasks (retrieval, code, tool calls), and whether its accuracy holds when the light decoder is aggressively compressed.
