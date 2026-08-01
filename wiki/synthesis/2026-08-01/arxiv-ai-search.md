---
title: "arXiv AI Research Scan — August 2026"
type: synthesis
created: 2026-08-01
updated: 2026-08-01
tags: [arxiv, survey, llm, recommendation, ctr, advertising, sequential-modeling, games, reinforcement-learning, agents]
---

# arXiv AI Research Scan — August 2026

Curated papers submitted Jul 29–30, 2026 (verified against the arXiv API) across LLM reasoning & RL post-training, agents & multi-agent systems, recommendation/CTR/advertising, sequential modeling & efficient inference, and games & strategic reasoning. Complements [[arxiv-daily]] and [[arxiv-paper-check]] for the same window.

---

## Large Language Models: Reasoning & RL Post-Training

### 1. Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling at Equal Token Cost, from 1.5B to 7B
- **Authors**: Iliya Mirzaei
- **Institution**: N/A
- **Abstract**: Re-runs the Wang et al. (2024) comparison of self-inspection methods (Self-Refine, Reflexion, self-consistency, Best-of-N, debate) against repeated sampling as a designed experiment: seven methods, open models of 1.5B/3B/7B, two math benchmarks, 150 questions each, every token counted. All 36 comparisons are paired by question with bootstrap intervals and multiplicity correction.
- **Key Innovations**: No method is reliably better than repeated sampling at equal token cost; 10 are reliably worse — all self-inspection methods. Choosing stops hurting as models grow (majority-vote beats model-selection by 8.0/11.3 pts at 1.5B but only 2.0/1.3 pts at 7B). Reflexion on the 1.5B model never triggered a retry — it judged itself correct every time.
- **Link**: https://arxiv.org/abs/2607.28576

### 2. Lightning OPD 2.0: Mitigating Style Bias in Cross-Teacher On-Policy Distillation
- **Authors**: Yecheng Wu, Song Han, Han Cai
- **Institution**: N/A
- **Abstract**: Identifies that cross-teacher OPD (when the SFT reference and the OPD teacher differ) degrades because teacher–reference disagreement contains a recurring "style-token" component (wording, formatting, reasoning cadence) alongside useful context-specific evidence. Uses rollout-level cross-fitting to estimate and subtract this style residual before building token-level OPD updates.
- **Key Innovations**: Cross-fitted style residualization removes teacher consistency as a prerequisite; from Klear-Reasoner-8B-SFT reaches 82.4% on AIME 2024 and 63.0% on LiveCodeBench v5, outperforming Lightning OPD in cross-teacher settings.
- **Link**: https://arxiv.org/abs/2607.28449

### 3. Contrastive Reinforced Policy Optimization via Privileged Self-Distillation (CRPO)
- **Authors**: Xingjian Wu, Junlin Liu, Xingchen Liu, Xuhang Zhu, Jianing Wang, Linsen Guo, Xiaoyu Li, Xuezhi Cao, Xunliang Cai
- **Institution**: N/A
- **Abstract**: Reforms agentic OPSD as contrastive learning. Uses predictive entropy to distinguish "positive" positions (reflective exploration) from "negative" positions (exposure bias from the privileged self-teacher), then applies group-wise contrast to preserve reliable fine-grained optimization signal in multi-turn settings.
- **Key Innovations**: Contrastive framing fixes OPSD exposure bias and reasoning-route convergence; consistent gains across 13 reasoning and deep-search benchmarks vs RLVR and self-distillation baselines, with improved long-horizon stability.
- **Link**: https://arxiv.org/abs/2607.28026

### 4. LEEPS: Latent-Guided Explore–Exploit Prompt Sampling for Efficient RLVR
- **Authors**: Shuang Liang, Haoyang Zhou, Yifan Gong, Guowei Wang, Xiting Wang
- **Institution**: N/A
- **Abstract**: Pre-rollout prompt selection for RLVR. Partitions candidates into exploit and explore portfolios, allocates rollout budget by recent non-trivial ratios, and uses representation-space neighbors + historical outcomes to prioritize uncertain prompts likely to yield non-zero reward variance.
- **Key Innovations**: Exploit–exploit balance without extra rollouts; +2.6% (1.5B) and +3.7% (7B) over strongest baseline on six math benchmarks, with faster convergence during training.
- **Link**: https://arxiv.org/abs/2607.28077

### 5. Beyond the Best Teacher: Expanding and Compressing the Reasoning Solution Manifold
- **Authors**: Songshuo Lu, Zhi Chen, Yaohua Tang
- **Institution**: N/A
- **Abstract**: Treats an RL-trained policy as a local probe of a multi-basin reasoning solution manifold, not a globally reliable teacher. Expand-then-compress: Residual GRPO trains a teacher sequence from a common init, each round targeting examples not yet covered by the accumulated teacher union; then reliability-gated Teacher-Union On-policy Distillation distills to the student. Consensus-Residual Decomposition preserves a winner teacher's excess token preferences.
- **Key Innovations**: Qwen3-1.7B student beats its strongest individual teacher on math, code, and instruction following (+2.0%/+8.3%/+6.9%).
- **Link**: https://arxiv.org/abs/2607.27770

### 6. Reasoning Consensus: Structural Ensembling of LLM Reasoning via Weighted DAG Aggregation
- **Authors**: Amruta Parulekar, Jinu Lee, Dilek Hakkani-Tür, Hari Sundaram
- **Institution**: UIUC
- **Abstract**: Extracts reasoning DAGs from multiple LLM chains-of-thought and merges them weighted by how many traces independently attest to each step, returning an inspectable "Consensus Reasoning" graph rather than just a majority answer.
- **Key Innovations**: Outperforms matched-budget majority voting (max +3.1% on MuSR-MM); matches/exceeds self-consistency at same trace budget while exposing the consensus structure; weights correlate with LLM-judge quality rankings (Spearman 0.30–0.51).
- **Link**: https://arxiv.org/abs/2607.27783

### 7. ReDiPPO: Reference-Guided Value Calibration and Discrepancy-Aware Token Reweighting
- **Authors**: Zhenrong Zhang, Fei Wu, Jun Du, Jianshu Zhang, Si Wei
- **Institution**: N/A
- **Abstract**: For math reasoning PPO, adds a reference-guided critic that uses reference answers as training-time privileged signal for value estimation. The token-level discrepancy between standard and reference-guided value estimates flags difficult reasoning states, used to reweight token-level advantages.
- **Key Innovations**: Improves value-estimation accuracy and beats PPO, DAPO, GSPO baselines on math benchmarks via reliable token-level credit assignment.
- **Link**: https://arxiv.org/abs/2607.27631

### 8. Post-Training at the Edge of Detectability: A Game-Theoretic Approach to Fine-Tuning
- **Authors**: Keegan Harris, Brian W. Lee, Ian Waudby-Smith, Philip Amortila, Nika Haghtalab, Michael I. Jordan
- **Institution**: CMU / UCB / MIT
- **Abstract**: Frames RL fine-tuning as a sequential game where an agent maximizes reward while a monitor tests outputs for deviation from a reference policy. The equilibrium policy solves a KL-regularized RL problem whose coefficient maximizes reward per unit of statistical distinguishability, learned via concave-convex fractional programming.
- **Key Innovations**: Principled alternative to heuristic KL-coefficient tuning; competitive reward-retention trade-offs on Qwen3-8B and Llama-3.2-1B; also usable to audit API providers serving open-weight models.
- **Link**: https://arxiv.org/abs/2607.26358

---

## Agents & Multi-Agent Systems

### 9. Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments
- **Authors**: Haomin Qi, Xingliang Wang, Xuanqi Gao, Baihui Sang, Xin Zhang, Minghua Ma, Pengfei Gao, Yu Kang, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
- **Institution**: Microsoft
- **Abstract**: Converts merged pull requests into verified coding-agent tasks on healthy modern repository revisions. Reconstructs task states via Patch Reversal, Code Mapping, or Agent Reconstruction, and validates the full lifecycle (healthy base → task state → restored state).
- **Key Innovations**: 79.6% verified task-construction success across 5 task families (bug fix, feature, test gen, API migration, security repair); recovers 29.2% more verified tasks than PR-based baselines; reduces pipeline expenditure 10.8%.
- **Link**: https://arxiv.org/abs/2607.28591

### 10. AgentRadio: Passive Awareness for Long-Horizon Multi-Agent Collaboration
- **Authors**: Xinxing Ren, Qianbo Zang, Ziyan Wang, Caelum Forder, Suman Deb, Peter Carroll, Zekun Guo
- **Institution**: N/A
- **Abstract**: Asynchronous message-passing layer giving coding-agent harnesses three primitives — threads, messages, and waiting-for-mentions (a background task that surfaces teammates' messages without interrupting foreground work), enabling mid-execution coordination rather than phase-boundary handoffs.
- **Key Innovations**: Four agents with AgentRadio resolve 62.1% of SWE-Atlas QnA tasks (+29.8 pts vs single Claude Code agent; above Claude Code + Opus 4.8 at 57.2%).
- **Link**: https://arxiv.org/abs/2607.28430

### 11. SIGIL: Compiling Agent Skills into Typed Harnesses
- **Authors**: Jayanaka Dantanarayana, Savini Kashmira, Lingjia Tang, Jason Mars
- **Institution**: University of Michigan et al.
- **Abstract**: Compiles prose skills into executable harnesses via AG-IR, a typed agentic IR separating model-owned cognition from code-owned mechanism. Across 30 skills, prose agents perform only 56% of mandated steps; compiled harnesses perform 86%, and the guarantee is model-independent.
- **Key Innovations**: Skill Compilation: harnesses complete full procedures 2.3× as often at 0.58× the tokens; holds at 86% across model generations while prose swings 56%→68%.
- **Link**: https://arxiv.org/abs/2607.27309

### 12. Harness-G: A Graph-Structured Harness for Search Agents
- **Authors**: Yanning Hou, Haoyuan Chen, Sihang Zhou, Xiaoshu Chen, Xirui Liu, Duanyang Yuan, Lingyuan Meng, Quan Liu, Jian Huang
- **Institution**: N/A
- **Abstract**: Diagnoses "retrieval-equivalence collapse" in Search-R1-style training (distinct query strings but increasingly overlapping evidence sets → little retrieval contrast). Reformulates retrieval as finite action selection on a graph: policy picks an evidence sentence/entity or answers; environment builds the menu, tracks state, validates choices. Adds Structured Non-myopic Credit (SNC) using a frozen answer scorer.
- **Key Innovations**: Removes linguistic aliasing at the policy–environment interface; SNC assigns downstream gains to enabling earlier actions; improves across six question-answering/reasoning benchmarks.
- **Link**: https://arxiv.org/abs/2607.27652

### 13. DREvo: Distilling Recalibrated Historical Experience for Harness Self-Evolution
- **Authors**: Hanghui Guo, Weijie Shi, Zhangze Chen, Shengxiang Xu, Yishu Wang, Yimei Zhang, Wangze Ni, Jia Zhu, Shimin Di
- **Institution**: N/A
- **Abstract**: Improves harness self-evolution by (1) dynamically reassessing whether historical experience still applies to the current harness, and (2) translating valid experience into actionable search directions — via function-level evidence anchoring, state-dependent recalibration, and role-conditioned search-intent distillation.
- **Key Innovations**: Smoother evolution trajectories; highest accuracy on all five benchmarks with avg +16.2%/+14.2% over baselines on domain reasoning and agentic tasks under limited budgets.
- **Link**: https://arxiv.org/abs/2607.26722

### 14. Living-Harness Is an Interactive-Agent Evolver
- **Authors**: Yuetian Du, Yucheng Wang, He Xu, Jiexu Xu, Shanwen Tan, Bing Zhao, Boyu Yang, Zhijie Xu, Ming Kong, Hu Wei, Jie Liu, Qiang Zhu
- **Institution**: N/A
- **Abstract**: Self-evolving agent harness: converts each completed trajectory + evaluator signals into posterior evidence for bounded harness updates. Writes episodic memory (triggers, failure patterns, recovery actions) and a state graph (state nodes, repair edges, transition rules) while tools and base context stay frozen.
- **Key Innovations**: +10.07 and +9.91 Pass@1 points over strongest interactive baseline on τ²-Bench and MultiWOZ-2.4 environments; evolved state reusable across model backbones.
- **Link**: https://arxiv.org/abs/2607.26598

### 15. ChronoMem: Version Control and Semantic Rollback for Agent Memory
- **Authors**: Yongye Su, Wujiang Xu, Chaoji Zuo, Elisa Bertino
- **Institution**: Purdue University
- **Abstract**: Semantic version-control layer for agentic memory (integrated into Google's open-source Agent Development Kit). Commits whole-memory snapshots per write, keeps version histories, and maps natural-language rollback intents to concrete historical versions via hybrid lexical+semantic retrieval, rank fusion, and reranking. Includes a post-exposure protocol testing counterfactual behavior after rollback.
- **Key Innovations**: First semantic version-control for agent memory; substantially improves rollback-consistent QA and history summarization vs prompt/retrieval-only baselines.
- **Link**: https://arxiv.org/abs/2607.27773

### 16. MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery
- **Authors**: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Fanshuai Meng, Qianli Ma, Weijia Jia
- **Institution**: N/A
- **Abstract**: Governance layer for agent memory that verifies updates are source-supported (Ordered PatchTest), resolves conflicting fact versions (Temporal Resolver), and restores application-visible state after faults (durable snapshot journal) — outside the answer model.
- **Key Innovations**: Accepts all 60 supported originals / rejects all 179 hard negatives; restores complete state under persistent multi-key faults; best avg F1 on MemoryAgentBench FactConsolidation across 12 answer-model configs.
- **Link**: https://arxiv.org/abs/2607.27834

### 17. ORCA-bench: How Ready Are Language Model Agents for Oncall?
- **Authors**: Albert Gong, Kyuseong Choi, Abhineet Agarwal, Jason Schechner, Ryan Huang, Raj Agrawal, Anish Agarwal, Raaz Dwivedi
- **Institution**: N/A
- **Abstract**: Production-fidelity oncall benchmark: live OpenTelemetry-instrumented microservice with 6 days of metrics/logs/traces via Prometheus/Jaeger/Grafana/OpenSearch plus full source access, and 1,079 RCA tasks varying report specificity, time-to-detection, and co-occurring faults. Ground truth signed off by expert SREs; LLM-as-judge independently re-scored by humans (κ=0.90).
- **Key Innovations**: Best RCA accuracy across 5 frontier agents is 25.3% (Medium) / 10.0% (Hard); weakest model hallucinates a root cause in 40% of reports — a lower bound on the gap before agents can be trusted for production reliability.
- **Link**: https://arxiv.org/abs/2607.28545

### 18. How Benchmarks Mis-Score Computer-Use Agents
- **Authors**: Zihan Dong, Zhiyuan Ma, Zekun Wang, Yunqing Li, Zirou Liu, Ruixuan Deng, Qishi Zhan, Rui Qian
- **Institution**: N/A
- **Abstract**: Reliability framework for CUA evaluation covering task construction, trajectory observation, scoring, and reporting. Audits 150 public failure-scored trajectories from five benchmarks: 15.3% of FAIL verdicts are wrong (10.7% evaluator false negatives, 4.7% broken tasks).
- **Key Innovations**: Three-tier diagnostic taxonomy shows verification/feedback and planning failures dominate; derives stage-specific design rules for long-horizon CUA benchmarks.
- **Link**: https://arxiv.org/abs/2607.28367

---

## Recommendation, CTR & Advertising

### 19. Multi-channel Uplift Policy Learning (ReAlloc)
- **Authors**: Changjian Liu, Tianyu Wang, Xiaoxuan Deng, WenTao Zhu, Yuwei Xu, Jungqi Jin, Yong Gao, Chuan Yu, Jian Xu, Bo Zheng
- **Institution**: Alibaba (Taobao)
- **Abstract**: Formulates budget allocation across marketing channels as a simplex-constrained uplift decision problem. ReAlloc: an Orthogonal Teacher extracts unbiased local gradients from short-term logs; an Explanation-Guided Student distills them into a structured marginal field over long-term horizons, enabling support-aware, conservative decisions capturing cross-channel substitution.
- **Key Innovations**: Fast-slow causal framework for channel allocation; large-scale Taobao A/B tests show simultaneous lifts in pay orders and income.
- **Link**: https://arxiv.org/abs/2607.28182

### 20. Improving Item Discoverability in e-Commerce Search via Related Intent Generation
- **Authors**: Ji Xin, Xiao Xiao, Ishan Bhatt, Vinesh Gudla, Trace Levinson, Raochuan Fan, Shishir Kumar Prasad, Prakash Putta, Tejaswi Tenneti
- **Institution**: Instacart
- **Abstract**: Discovery-augmented search for grocery: generates implicit user intents to expand candidate recall. Two-stage hybrid — closed-weight LLM for head queries, LoRA-finetuned SLM (teacher-student distillation) for tail queries. Evaluated with LLM-as-judge (validated vs human) plus session-level purchase analysis.
- **Key Innovations**: Extends discovery coverage ~60%→80% of query traffic at ~30% of teacher inference cost; frames discovery search as a marketplace-balancing mechanism for long-tail supply.
- **Link**: https://arxiv.org/abs/2607.27172

### 21. FinSMART: Financial Sentiment Analysis through Market-Aligned Reinforcement Learning
- **Authors**: Giorgos Iacovides, Wuyang Zhou, Danilo Mandic
- **Institution**: Imperial College London
- **Abstract**: First market-aligned RL framework for financial sentiment: optimizes sentiment signals with realized market outcomes, using a signal-extraction pipeline combining market-aware filtering with a discrete asymmetric trading reward for stable RL from economic feedback. Supports market-aware retraining without manual annotation.
- **Key Innovations**: +220% cumulative trading returns over strongest baseline; continuous adaptation to market shifts with consistent gains over static models — a next-gen paradigm for adaptive financial LLMs.
- **Link**: https://arxiv.org/abs/2607.28127

### 22. Beyond Sentiment: Structured Information Extraction from Financial News
- **Authors**: Daohan Zhu, Sitong Ge, Ruofei Wang, Honggu Chen, Yubo Hou, Tao Wan, Zengchang Qin
- **Institution**: Beihang University
- **Abstract**: LLaMA-3.1-70B extracts six orthogonal semantic dimensions (event type, impact scope, temporal horizon, confidence, etc.) from financial news, tested on 41,618 news–stock pairs (FNSPID). Finds sentiment features are strongly nonlinear (F1 0.576 nonlinear vs 0.230 linear); structured features capture orthogonal signal (53.5% disagreement rate).
- **Key Innovations**: Combining both signal sources yields F1=0.600 (p<0.0001); non-sentiment dimensions contribute +0.019 F1 beyond FinBERT — sentiment-only compression incurs systematic information loss.
- **Link**: https://arxiv.org/abs/2607.28496

### 23. Building a User Foundation Model for the Open Web
- **Authors**: Solal Vernier, Ivan Can Arisoy, Merwan Barlier, Blaž Škrlj
- **Institution**: Criteo
- **Abstract**: User foundation model for open-web real-time bidding, where identity is fragmented and non-persistent. Pre-trains a Transformer encoder with masked LM + sequence-level contrastive objective on browsing histories (aggregated counters + recency buckets), then fine-tunes on click prediction. LLM-in-the-loop search over code-level "lifters" optimizes the pretraining pipeline.
- **Key Innovations**: Same encoder gives +1.197% RIG on production bid-win-rate and +1.354% RIG on CTR ranker; 7-day live A/B confirms +2.13% CTR, −1.13% eCPC.
- **Link**: https://arxiv.org/abs/2607.28019

---

## Sequential Modeling, Memory & Efficient Inference

### 24. Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory
- **Authors**: Rubin Wei, Jiaqi Cao, Jiarui Wang, Junming Zhang, Qipeng Guo, Bowen Zhou, Zhouhan Lin
- **Institution**: Shanghai Jiao Tong University / Tsinghua University
- **Abstract**: Scales parametric-memory decoder-only LMs to 6.9B params / 300B tokens. Replaces Faiss with a distributed indexing/retrieval pipeline plus sparse batch-wise loading of kNN distributions to remove the indexing bottleneck.
- **Key Innovations**: Allocating parameters to memory beats scaling the base model: 6.9B general memory + Pythia-410M → 37.34 avg (surpassing Pythia-12B at 37.24 with 39% fewer params); 1.7B domain memories add >9 points at every Qwen3 scale (0.6B–14B).
- **Link**: https://arxiv.org/abs/2607.27919

### 25. Understanding Is Done Early: Depth Division of Labor and Unbounded-Context Memory (CoMem)
- **Authors**: Hanzuo Liu, Xuan Qi, Chunyu Liu, Haotian Zhong, Yulong Wang, Rayying, Key, Alex Lamb, Mingyu Gao
- **Institution**: Tsinghua University
- **Abstract**: Exploits the finding that lower/middle layers build semantic representations while upper layers specialize for prediction. CoMem writes each context chunk through an intermediate layer, retrieves a fixed number of cached residual states, and recomputes query-conditioned upper layers — organizing long-context memory along the layer axis, not just the token axis.
- **Key Innovations**: On Qwen3-8B, reaches 97.05 (RULER) and 38.27 (LoCoMo) vs 34.59 full-context; adapter-free run uses 18.26 GB vs 89.36 GB at 128k with 7.83× prefill speedup.
- **Link**: https://arxiv.org/abs/2607.28263

### 26. SemPIC: Learning Semantic Position-Independent KV Caches
- **Authors**: Hui Xie, Peng Xiao, Yutong Deng, Shuoran Dou, Jian Yang, Jinyang Guo
- **Institution**: N/A
- **Abstract**: Compiles reusable document KVs via a LoRA Writer through behavioral distillation while the pretrained decoder stays an unchanged Reader. KV Gradient Checkpointing cuts peak training memory without severing gradients through cached KVs.
- **Key Innovations**: Raises mean micro-F1 over KV Packet from 0.53→0.60, approaching Full Recompute (0.62), across three models and four tasks — reliable position-independent caching for agentic reuse.
- **Link**: https://arxiv.org/abs/2607.28069

### 27. Recall Before You Rank: Similarity-Guided Top-K Reuse for Efficient Long-Context Attention (ReTopK)
- **Authors**: Wenshuai Yao, Wenyong Zhou, Hanyong Shao, Yizhe Chen, Zhiyuan Ning, Yuannuo Feng, Ru Huang, Kechao Tang
- **Institution**: Tsinghua University
- **Abstract**: Training-free acceleration of dynamic Top-K attention by reusing historical query–support decisions: similar queries attend to overlapping supports. Maintains a bounded cache of query–support pairs, unions retrieved supports with a recent window, and reranks only the compact candidate set with exact scores; similarity-based fallback keeps reliability.
- **Key Innovations**: At 128K / K=512, only 0.50% perplexity increase over Exact Top-K while accelerating attention 3.07×; lowest PPL and highest NIAH/LongBench among approximate methods across 16K–128K.
- **Link**: https://arxiv.org/abs/2607.27692

### 28. Prox: Training-Free FFN Activation Sparsity via Approximate Intermediate-Channel Salience
- **Authors**: Jinyi Liu, Wei Chen, Pengyu Chen, Xinyi Yuan, Minghe Bai, Guoquan Wu, Jun Wei
- **Institution**: Chinese Academy of Sciences
- **Abstract**: Builds the SwiGLU channel mask from magnitude ranking (not exact values) of the intermediate state, using input sparsity and quantized proxy weights, then computes only selected channels exactly — enabling sparse execution of all three FFN projections.
- **Key Innovations**: Outperforms training-free baselines at all sparsity levels across 10 LLMs / 6 families; up to 1.99× end-to-end decode speedup at 70% FFN sparsity; compatible with quantization and sparse attention.
- **Link**: https://arxiv.org/abs/2607.27591

### 29. A Sparse Glimpse of the Whole: Train-Free Self-Speculative Decoding (SparseSpec-L)
- **Authors**: Yuesong Liu, Yuan Zeng, Min Lyu, Ruilin Liu, Yu Guo, Yinlong Xu
- **Institution**: N/A
- **Abstract**: Unified efficiency analysis showing extending the speculation horizon can hurt when marginal acceptance falls below relative drafting cost. SparseSpec-L drafts from the target model using a dynamically sparsified and recallable KV cache, recycling per-head attention statistics as a no-extra-forward importance signal, with an online entropy controller selecting speculation length.
- **Key Innovations**: Consistent end-to-end long-context speedups while preserving the target distribution; KV-cache sparsification without permanently discarding dense KV.
- **Link**: https://arxiv.org/abs/2607.27735

### 30. Looped Transformers with Source-Centered State Evolution (SCSE)
- **Authors**: Bum Jun Kim, Kohei Hayashi, Shunsuke Kamiya, Masanori Koyama, Yusuke Iwasawa, Yutaka Matsuo
- **Institution**: University of Tokyo / NII
- **Abstract**: Fixes the input-conditioning vs reference-preserving trade-off in additive-injection looped Transformers. SCSE keeps input dependence through a learned anchor + initial deviation, maps zero deviation to zero, and enforces exact anchor invariance via a zero-deviation mask — the anchor is a one-step fixed point by construction.
- **Key Innovations**: Improves the recurrent quality frontier across WikiText-2/103, web pretraining, and LAMBADA; ablations isolate the learned anchor + anchor-coordinate deviation recurrence as the main contributors.
- **Link**: https://arxiv.org/abs/2607.27656

### 31. Beyond Geometric Complementarity: Coherent Overlap in Sparse MoE Routing
- **Authors**: Huiyuan Tian, Bonan Xu, Shijian Li
- **Institution**: N/A
- **Abstract**: Distinguishes route coherence, candidate quality, and candidate-by-context interaction via an Expert Subspace Separation Index (ESSI), matched-route residuals, and a prefix-controlled 2×2 factorial with frozen-route interventions. Across OLMoE, Mixtral, DeepSeek: expert subspaces overlap substantially yet actual routes explain representations better than matched alternatives.
- **Key Innovations**: "Coherent overlap" — routing picks token-relevant experts from a shared geometric neighborhood while multi-expert computation persists without disjoint linear coverage; clarifies why geometric similarity alone can't determine redundancy or pruning value.
- **Link**: https://arxiv.org/abs/2607.28308

---

## Games & Strategic Reasoning

### 32. Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3
- **Authors**: Jens Lehmann, Andrei Aioanei, Sahar Vahdati
- **Institution**: University of Bonn
- **Abstract**: Formalizes ARC-AGI-3 as parameterized deterministic Moore machines and builds Tycho, a coding-agent system that constructs and uses game-specific models during interaction — modeling, testing, planning with, repairing, or bypassing free-form executable hypotheses. "Active abstraction": deciding when acquiring/using a model is worth its interaction cost.
- **Key Innovations**: With GPT-5.6 Sol / Opus 5 reaches 100.00 RHAE completing all 183 levels; Opus 5 uses 61% fewer scored actions than official human baselines. Automatic repair improves transition match but hurts RHAE — transition match ≠ objective identification.
- **Link**: https://arxiv.org/abs/2607.28287

### 33. Strategy, Not Payoffs: A Behavioural Embedding of Normal-Form Games
- **Authors**: Joshua Caiata, Sreepriya Pulyassary, Xiang Li, Kate Larson
- **Institution**: University of Cambridge
- **Abstract**: Predicts transfer of LLM strategic capabilities across games using a lightweight two-feature behavioural embedding: entropy of the Nash equilibrium and sensitivity of optimal responses to an opponent's action. Shows published structural embeddings mostly memorize game identities and fail to generalize.
- **Key Innovations**: Behavioural embedding reliably predicts performance changes on held-out games — transfer is governed by decision-making behaviour structure, not payoff geometry.
- **Link**: https://arxiv.org/abs/2607.27536

### 34. Agents That Certify Their Own Exploits: Confidence-Scheduled Restricted Responses for Safe Opponent Exploitation (CS-RNR)
- **Authors**: Boning Li, Longbo Huang
- **Institution**: Tsinghua University
- **Abstract**: For two-player zero-sum imperfect-information games: exploit a flawed opponent only when the agent can audit the deployed strategy. Uses anytime-valid confidence sequences on pooled action frequencies, restricted-response solves over pin levels, and a full-tree best-response certificate compared against a user budget.
- **Key Innovations**: In Leduc hold'em, 6.2× the steady-state gain of a money-verified binary gate while every deployed strategy stays in budget; 36,000 audited hands all satisfy the certificate.
- **Link**: https://arxiv.org/abs/2607.28520

### 35. Hierarchical Multilevel Monte Carlo for Order-Optimal Neural Actor-Critic in Average-Reward CMDPs
- **Authors**: Ankur Naskar, Vaneet Aggarwal
- **Institution**: Purdue University
- **Abstract**: Resolves the bias–cost trade-off of neural critics under NTK analysis in average-reward CMDPs via a hierarchical MLMC neural critic that debiases across trajectory sampling and critic optimization simultaneously, with only logarithmic expected sample cost.
- **Key Innovations**: First order-optimal guarantees (gap and violation Õ(T^−1/2)) for infinite-horizon average-reward CMDPs with general policy parameterization and neural critics, without knowing the mixing time.
- **Link**: https://arxiv.org/abs/2607.28390

---

## Key Themes

| Theme | Papers | Trend |
|-------|--------|-------|
| **RL post-training beyond GRPO** | ReDiPPO, CRPO, LEEPS, Beyond the Best Teacher | Token-level credit assignment, contrastive framing, and pre-rollout prompt selection; critics + reference signals return to favor |
| **Self-distillation refinement** | Lightning OPD 2.0, Beyond the Best Teacher | Style-bias removal and teacher-union expansion/compression to fix OPD's single-teacher blind spots |
| **Repeated sampling vs reflection** | Sample More, Reflect Less | Cost-matched evidence that self-inspection methods can underperform plain sampling — an evaluation-methodology warning |
| **Harness engineering** | SIGIL, Harness-G, DREvo, Living-Harness | Skills and retrieval compiled into program/typed structure; harness self-evolution converging across groups |
| **Agent memory governance** | ChronoMem, MemTxn | Version control, transactions, source-verification, and rollback for persistent agent memory |
| **Long-context efficiency** | CoMem, ReTopK, Prox, SparseSpec-L, SemPIC | Layer-axis memory, similarity-guided Top-K reuse, magnitude-rank FFN masks, self-speculation, position-independent caches |
| **Generative rec / ads** | ReAlloc, e-Commerce Related Intent, FinSMART, User Foundation Model | Uplift/causal budget allocation, discovery search, market-aligned RL, identity-fragmented RTB pretraining |
| **Agent evaluation reliability** | ORCA-bench, How Benchmarks Mis-Score CUAs | Production-fidelity oncall RCA + error audits of existing CUA benchmark pipelines |

(End of file)
