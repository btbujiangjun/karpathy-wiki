---
title: "arXiv Daily — June 22, 2026"
type: synthesis
created: 2026-06-22
updated: 2026-06-22
sources: []
tags: [arxiv-daily, llm, recommendation, ctr, rl, games, multimodal, reasoning, alignment, efficient-inference]
---

# arXiv Daily Report — June 22, 2026

> Recent papers in AI, LLMs, recommendation, advertising, CTR, games, RL, and related areas. Coverage window: June 1–22, 2026.

---

## 1. Large Language Models & Reasoning

### 1.1 Operads for Compositional Reasoning in LLMs
- **arXiv**: [2606.13634](https://arxiv.org/abs/2606.13634)
- **Authors**: Nathaniel Bottman, Kyle Richardson
- **Inst/Company**: — 
- **Key Innovation**: Proposes **operads** (mathematical structures for many-in-one-out operations) as a formal framework for question decomposition in LLMs. Introduces **operadic consistency** — a measure of whether a model's answers agree across partial collapses of a decomposition tree — shown to correlate with accuracy across 12 LLMs and 4 multi-hop QA datasets.
- **Abstract**: Question decomposition lacks rigorous mathematical foundation. The authors define the *questions operad* Q and show QA models as algebras over Q. Operadic consistency outperforms standard temperature-based self-consistency.

### 1.2 Agentic Chain-of-Thought Steering (ACTS)
- **arXiv**: [2606.03965](https://arxiv.org/abs/2606.03965)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Formulates reasoning steering as an MDP where a **controller agent adaptively steers a frozen reasoner** during inference via reasoning strategy and steering phrase. Enables budget-aware token savings while matching full-thinking performance. Optimized via RL with budget-conditioned reward shaping.
- **Abstract**: LLMs waste tokens on extended CoT. ACTS matches full-thinking performance with substantial token savings and enables controllable accuracy-efficiency trade-offs.

### 1.3 From Reasoning Traces to Reusable Modules
- **arXiv**: [2606.18089](https://arxiv.org/abs/2606.18089)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Formalizes compositional generalization in LLM reasoning through a **hierarchical latent selection model**. Shows SFT and RL play asymmetric, complementary roles: SFT supplies atomic modules, RL decomposes traces and recombines them for novel compositions. Finds training on compound traces > training on isolated modules.
- **Abstract**: Proves theoretically and empirically that SFT supplies raw module materials and RL identifies latent atomic modules for compositional generalization.

### 1.4 Large Language Models Do Not Always Need Readable Language (BabelTele)
- **arXiv**: [2606.19857](https://arxiv.org/abs/2606.19857)
- **Authors**: Jiayi Zhu et al.
- **Inst/Company**: —
- **Key Innovation**: Introduces **BabelTele** — compact, non-standard textual representations that sacrifice human readability while preserving 99.5% semantic fidelity at 27.9% original length. Tests cross-model transfer, agent memory, and multi-agent communication.
- **Abstract**: Investigates whether semantic information can be encoded in model-centric textual forms. Shows human readability and semantic recoverability can be partially decoupled.

---

## 2. Reinforcement Learning for LLMs (RLVR / GRPO)

### 2.1 A First-Principles Derivation of LLM Policy Optimization: From Expected Reward to GRPO
- **arXiv**: [2606.16733](https://arxiv.org/abs/2606.16733)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Unified theoretical survey deriving GRPO from first principles. Identifies compound failures that require **joint design of trajectory and reward sides**. Maps boundary cases where existing solutions fail.
- **Abstract**: A principled derivation covering from expected reward to GRPO and its structural extensions, exposing failure modes.

### 2.2 Rollout-Level Advantage-Prioritized Experience Replay for GRPO
- **arXiv**: [2606.04560](https://arxiv.org/abs/2606.04560)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Proposes **rollout-level replay buffer for GRPO** with age eviction and advantage-prioritized sampling. Gains +4.35 pp on 5-benchmark average at 4B scale over standard GRPO.
- **Abstract**: Each GRPO rollout is used once then discarded. Replay buffer with staleness bounds and advantage prioritization improves sample efficiency significantly.

### 2.3 VIMPO: Value-Implicit Policy Optimization
- **arXiv**: [2606.20008](https://arxiv.org/abs/2606.20008)
- **Authors**: Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song, Xuandong Zhao
- **Inst/Company**: UC Berkeley
- **Key Innovation**: Derives **critic-free Bellman-consistent token-level credit assignment** by modeling autoregressive generation as a deterministic transition MDP. Occupies the middle ground between group-relative (GRPO) and actor-critic (PPO) methods.
- **Abstract**: Models the value function implicitly through policy log-likelihood ratio. Combines critic-free training with Bellman-consistent token-level advantages.

### 2.4 μ-GRPO: How Off-Policy Can GRPO Be?
- **arXiv**: [2605.17570](https://arxiv.org/abs/2605.17570)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Shows GRPO can tolerate **substantial rollout staleness**. Organizes training into few large generation–optimization stages. Achieves ~2× wall-clock speedup vs standard GRPO using relaxed clipping + negative-advantage veto.
- **Abstract**: Demonstrates GRPO-style algorithms tolerate high rollout staleness, achieving ~2× training speedup with matched performance.

### 2.5 GraphPO: Graph-based Policy Optimization for Reasoning Models
- **arXiv**: [2606.18954](https://arxiv.org/abs/2606.18954)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Represents rollouts as a **directed acyclic graph** with reasoning steps as edges, semantically equivalent states merged into nodes. Reduces redundant exploration and enables suffix sharing. Reduces advantage-estimation variance.
- **Abstract**: GraphPO merges equivalent reasoning paths into equivalence classes, outperforming chain- and tree-based baselines at same token budgets.

### 2.6 GRPO-VPS: Verifiable Process Supervision
- **arXiv**: [2604.20659](https://arxiv.org/abs/2604.20659)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Probes model's belief in correct answer throughout reasoning trajectory via **conditional probability of correct answer** at segment boundaries. Up to +2.6 pp accuracy and 13.7% reasoning length reduction on math tasks.
- **Abstract**: Model-free, verifiable process supervision for GRPO that provides interpretable segment-wise progress measurements without Monte Carlo rollouts or auxiliary models.

### 2.7 Latent-GRPO: GRPO for Latent Reasoning
- **arXiv**: [2604.27998](https://arxiv.org/abs/2604.27998)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Adapts GRPO to **latent-space reasoning**. Addresses three coupled bottlenecks: absent intrinsic latent manifolds, exploration-optimization misalignment, latent mixture non-closure. Outperforms explicit GRPO on high-difficulty tasks while using 3–4× shorter reasoning chains.
- **Abstract**: Combines invalid-sample advantage masking, one-sided noise sampling, and optimal correct-path first-token selection for stable latent RL.

### 2.8 Value-Gradient Hypothesis of RL for LLMs
- **arXiv**: [2605.21654](https://arxiv.org/abs/2605.21654)
- **Authors**: S. Sojoudi et al.
- **Inst/Company**: —
- **Key Innovation**: Shows critic-free RL (PPO/GRPO) is **not value-free** — the actor backward pass carries a value-gradient-like signal. Explains why critic-free methods work at long horizons. Derives criterion for when RL is most effective along pretraining trajectory.
- **Abstract**: Under differentiable rollout, actor update is value-gradient-like in expectation. Attention provides differentiable credit transport around token-sampling bottleneck.

---

## 3. Efficient LLM Inference & Architecture

### 3.1 MiniMax Sparse Attention (MSA)
- **arXiv**: [2606.13392](https://arxiv.org/abs/2606.13392)
- **Authors**: MiniMax AI
- **Inst/Company**: MiniMax
- **Key Innovation**: Blockwise sparse attention with **group-specific Top-k selection per GQA group**. Co-designed GPU kernel with exp-free TopK and KV-outer sparse attention. On 109B MoE model: 28.4× attention compute reduction, 14.2× prefill, 7.6× decoding speedup at 1M context.
- **Abstract**: MSA matches GQA accuracy while dramatically reducing compute. Production models released on HuggingFace.

### 3.2 SparDA: Sparse Decoupled Attention
- **arXiv**: [2606.04511](https://arxiv.org/abs/2606.04511)
- **Authors**: Yaosheng Fu et al.
- **Inst/Company**: —
- **Key Innovation**: Introduces a **fourth per-layer projection (Forecast)** that predicts KV blocks needed by the next layer, enabling lookahead selection overlapping CPU-to-GPU prefetch. Adds <0.5% parameters. Up to 5.3× decode throughput vs non-offload sparse baseline.
- **Abstract**: Decoupled sparse attention architecture that overlaps KV prefetch with current-layer execution via Forecast projection.

### 3.3 LiftQuant: Continuous Bit-Width LLM Quantization
- **arXiv**: [2606.04050](https://arxiv.org/abs/2606.04050)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: First framework enabling **arbitrary fractional bit-widths** (e.g., 2.4-bit) for LLMs. Uses "lift-then-project" mechanism: 1-bit lattice in higher-D space projected to target space. Decouples quantization rate from coding format.
- **Abstract**: Transforms bit-width from discrete architectural constant into continuous tunable ratio for Pareto-optimal deployment.

### 3.4 KVarN: Variance-Normalized KV-Cache Quantization
- **arXiv**: [2606.03458](https://arxiv.org/abs/2606.03458)
- **Authors**: Huawei CSL
- **Inst/Company**: Huawei
- **Key Innovation**: Calibration-free KV-cache quantizer using **Hadamard rotation + dual-scaling variance normalization**. State-of-the-art at 2-bit precision. Shows quantization errors accumulate across timesteps driven by incorrect token scales.
- **Abstract**: Establishes new SOTA for KV-cache quantization on MATH500, AIME24, HumanEval at 2-bit precision.

### 3.5 TwinQuant: Learnable Subspace Decomposition for 4-Bit Quantization
- **arXiv**: [2606.01556](https://arxiv.org/abs/2606.01556)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Learns **quantization-friendly decomposed subspaces** via joint optimization over Stiefel and general linear manifolds. Fused dual-component kernel pipelines low-rank computation on-chip. Up to 1.8× end-to-end speedup over FP16 baseline.
- **Abstract**: 4-bit quantization framework that jointly reshapes low-rank and residual components for near-FP16 accuracy.

### 3.6 Massive Spikes in LLMs are Bias Vectors (INSERTQUANT)
- **arXiv**: [2606.02288](https://arxiv.org/abs/2606.02288)
- **Authors**: Yung-Chin Chen, Chung Peng Lee, Ze-Wei Liou, Naveen Verma
- **Inst/Company**: —
- **Key Innovation**: Mechanistically identifies that **massive activation spikes are structural vector biases**, not scalars. W_K/W_Q/W_V coordinate to maintain these biases against RoPE perturbations. INSERTQUANT clamps spikes and restores function via pre-computed template vectors.
- **Abstract**: Reveals spike-carrying tokens converge to constant vectors after normalization, driving attention sink and value-state drain.

### 3.7 AIR: Activation- and Influence-Aware SVD Compression
- **arXiv**: [2606.19993](https://arxiv.org/abs/2606.19993)
- **Authors**: Nico Harder, Daniel Becking, Karsten Mueller, Wojciech Samek
- **Inst/Company**: —
- **Key Innovation**: SVD-based LLM compression using **backward-signal influence metric** with closed-form alternating least squares sweep. Improves perplexity over SVD-LLM(W) by >18% at ≤60% parameter retention. Composes orthogonally with LoRA and quantization.
- **Abstract**: Layer-local, single-sweep method that closes gap between activation-aware SVD and end-to-end retraining.

---

## 4. Recommendation, CTR & Advertising

### 4.1 CADET: Context-Conditioned Ads CTR Decoder-Only Transformer
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Authors**: LinkedIn
- **Inst/Company**: LinkedIn
- **Key Innovation**: End-to-end decoder-only transformer for ads CTR. Innovations: (1) **context-conditioned decoding** with multi-tower heads resolving position chicken-and-egg, (2) **self-gated attention** stabilizing training, (3) timestamp-based RoPE, (4) session masking. 11.04% CTR lift over LiRank baseline.
- **Abstract**: Addresses key challenges in applying autoregressive transformers to advertising. Deployed at LinkedIn scale.

### 4.2 GRAB: Generative Ranking for Ads at Baidu
- **arXiv**: [2602.01865](https://arxiv.org/abs/2602.01865)
- **Authors**: Baidu
- **Inst/Company**: Baidu
- **Key Innovation**: **Causal Action-aware Multi-channel Attention (CamA)** for capturing temporal dynamics and action signals. Shows monotonic scaling with model capacity and sequence length. 3.05% revenue increase, 3.49% CTR lift in production.
- **Abstract**: LLM-inspired sequence-first CTR paradigm. Demonstrates desirable scaling behavior across longer interaction sequences.

### 4.3 GR4AD: Generative Recommendation for Large-Scale Advertising
- **arXiv**: [2602.22732](https://arxiv.org/abs/2602.22732)
- **Authors**: Kuaishou
- **Inst/Company**: Kuaishou
- **Key Innovation**: Production generative recommender with (1) **UA-SID** unified ad semantic IDs from fine-tuned MLLM, (2) MGMR quantization, (3) **RSPO** list-wise RL algorithm, (4) **LazyAR decoder** for relaxed layer-wise dependencies. Serves 400M+ users at 500+ QPS per L20.
- **Abstract**: Co-design across representation, learning, and serving for real-time large-scale advertising.

### 4.4 OneRanker: Unified Generation and Ranking
- **arXiv**: [2603.02999](https://arxiv.org/abs/2603.02999)
- **Authors**: Tencent
- **Inst/Company**: Tencent (WeiXin Channels)
- **Key Innovation**: Value-aware multi-task decoupling via **task token sequences and causal mask**. Coarse-to-fine target awareness with Fake Item Tokens. Dual-side consistency via KV pass-through and Distribution Consistency loss. GMV +1.34% in production.
- **Abstract**: Architectural-level deep integration of generation and ranking for industrial advertising recommendation.

### 4.5 Memento: Personalized RAG-Style Long-Retention Data Scaling
- **arXiv**: [2605.24051](https://arxiv.org/abs/2605.24051)
- **Authors**: Meta
- **Inst/Company**: Meta (Facebook)
- **Key Innovation**: Treats user history as document corpus and ad requests as queries. Uses **Maximal Marginal Relevance (MMR)** for retrieval balancing similarity and diversity. 1% CTR lift, 1.2% CVR lift. Scales personalization to 365+ days of history with sub-10ms latency.
- **Abstract**: RAG-style framework for long-retention data scaling in online ads recommendation with temporal chunking, INT8 quantization, and async serving.

### 4.6 DeRes: Decoupling Residual Stability and Adaptivity for CTR
- **arXiv**: [2606.07980](https://arxiv.org/abs/2606.07980)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Dual-path inter-layer connector (Identity path + **Block Attention Residual path**) with vector-wise gating. Uses **SiLU instead of Softmax** for cross-layer attention enabling negative (forgetting) weights. 1.66× steeper compute-AUC scaling law than OneTrans.
- **Abstract**: Draws on Dual Path Networks and HORNN view of residuals. Outperforms 12 baselines on 331M-interaction industrial dataset.

### 4.7 RankUp: High-rank Representations for Advertising
- **arXiv**: [2604.17878](https://arxiv.org/abs/2604.17878)
- **Authors**: Tencent
- **Inst/Company**: Tencent
- **Key Innovation**: Mitigates **representation collapse** through randomized permutation splitting, multi-embedding paradigm, global token integration, and crossed pretrained embedding tokens. GMV improvements: 3.41% (Video Accounts), 4.81% (Official Accounts), 2.12% (Moments).
- **Abstract**: Addresses effective rank degradation in deep MetaFormer architectures for Tencent's advertising platforms.

### 4.8 EST: Efficiently Scalable Transformer for CTR Prediction
- **arXiv**: [2602.10811](https://arxiv.org/abs/2602.10811)
- **Authors**: Alibaba
- **Inst/Company**: Alibaba (Taobao)
- **Key Innovation**: **Lightweight Cross-Attention (LCA)** + **Content Sparse Attention (CSA)** for efficient scaling. Exhibits clear power-law scaling trend. 1.22% CTR lift and 3.27% RPM increase in Taobao display advertising production.
- **Abstract**: Stable power-law scaling relative to model capacity and compute cost.

### 4.9 GenCI: Generative Modeling of User Intent Shift
- **arXiv**: [2601.18251](https://arxiv.org/abs/2601.18251)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Uses **generative next-item prediction to produce semantic interest cohorts** as explicit representations of immediate user intent. Hierarchical candidate-aware network injects cohort context into ranking. End-to-end training.
- **Abstract**: Reframes recall-then-rank as integrated generate-and-interpret loop, overcoming point-wise ranking limitations.

### 4.10 SparseCTR: Sparse Attention for Long-term Behaviors
- **arXiv**: [2601.17836](https://arxiv.org/abs/2601.17836)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: **Personalized time-aware chunking (TimeChunking)** + three-branch sparse attention (global, transition, local) + relative temporal encoding. Exhibits scaling law across 3 OOM of FLOPs. CTR +1.72%, CPM +1.41% online.
- **Abstract**: Designed specifically for long-term user behavior modeling in recommendation with personalization and temporal characteristics.

### 4.11 Principled Synthetic Data Enables Scaling Laws for LLMs in Recommendation
- **arXiv**: [2602.07298](https://arxiv.org/abs/2602.07298)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: First demonstration of **robust power-law scaling for LLMs continually pre-trained on synthetic recommendation data**. Standard sequential models trained on synthetic data outperform real-data models by +130% Recall@100. Scales from 0.6B to 8B on 163B tokens.
- **Abstract**: Layered synthetic data framework establishing predictable scaling laws for LLM-based recommenders.

---

## 5. Games & Reinforcement Learning

### 5.1 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games
- **arXiv**: [2605.00347](https://arxiv.org/abs/2605.00347)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Studies RL-based training of VLMs for long-horizon decision-making in Super Mario Land. Proposes **adapted PPO with lightweight turn-level critic**, substantially improving stability over GRPO/Reinforce++. Achieves 3× average game progress over frontier models.
- **Abstract**: Identifies key ingredients for stable RL in long-horizon multi-modal settings. Open training framework Odysseus.

### 5.2 Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **arXiv**: [2604.17696](https://arxiv.org/abs/2604.17696)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Self-play framework that selectively reinforces trajectories with **domain-agnostic and adaptive reasoning**. Reasoning Transferability Coefficient (φ) measures abstraction level; Reasoning Evolution Reward (ψ) incentives deepening reasoning. Transfers to math, general reasoning, code.
- **Abstract**: Addresses domain specificity and contextual stasis in game-based reasoning transfer. Consistent improvements over base models and SPIRAL.

### 5.3 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **arXiv**: [2506.24119](https://arxiv.org/abs/2506.24119)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Multi-turn, multi-agent RL for LLMs via **self-play on two-player zero-sum language games**. Role-conditioned advantage estimation (RAE) stabilizes training. Generates unlimited training data through game dynamics.
- **Abstract**: Distributed actor-learner architecture for online self-play across multiple language games. Continuously evolving curriculum.

### 5.4 From Trainee to Trainer: LLM-Designed Training Environment for RL
- **arXiv**: [2606.17682](https://arxiv.org/abs/2606.17682)
- **Authors**: Chao Chen, Chengzu Li, Zhiwei Li, Yinhong Liu, Zhijiang Guo
- **Inst/Company**: —
- **Key Innovation**: **LLM-as-Environment-Engineer** framework where the policy model analyzes failure trajectories and proposes next-stage environment modifications. Current RL checkpoint is a better environment engineer than the base model.
- **Abstract**: Automates RL training environment redesign. Qwen3-4B outperforms larger proprietary LLMs and fixed-environment baselines.

### 5.5 MARL-GPT: Foundation Model for Multi-Agent RL
- **arXiv**: [2604.05943](https://arxiv.org/abs/2604.05943)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Single GPT-based model trained via offline RL on **400M–1B expert trajectories** across SMACv2, Google Research Football, POGEMA. Single transformer observation encoder with no task-specific tuning.
- **Abstract**: Demonstrates that a single multi-task transformer can perform well across diverse MARL environments.

### 5.6 Vintix II: Decision Pre-Trained Transformer
- **arXiv**: [2604.05112](https://arxiv.org/abs/2604.05112)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Extends Decision Pre-Trained Transformer (DPT) to multi-domain continuous control using **Flow Matching**. Agent trained across hundreds of tasks achieves clear held-out test set generalization. Surpasses prior Algorithm Distillation scaling.
- **Abstract**: Reinforces ICRL as viable alternative to expert distillation for training generalist agents.

### 5.7 SeeUPO: Sequence-Level Agentic-RL with Convergence Guarantees
- **arXiv**: [2602.06554](https://arxiv.org/abs/2602.06554)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Models multi-turn interaction as **sequentially executed multi-agent bandit problems**. Turn-by-turn sequential policy updates in reverse execution order with backward induction. Provable monotonic improvement guarantees.
- **Abstract**: Critic-free approach with convergence guarantees for multi-turn agentic RL.

### 5.8 Do We Need Transformers to Play FPS Video Games?
- **arXiv**: [2504.17891](https://arxiv.org/abs/2504.17891)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: **Negative result**: transformer-based methods (DTQN, Decision Transformer) underperform traditional methods in VizDoom FPS environment. Suggest self-attention alone insufficient for memory-intensive strategic environments.
- **Abstract**: Comparative study showing PPO outperforms transformer-based agents in both online and offline VizDoom settings.

### 5.9 Chess from Move Sequences Without Search
- **arXiv**: [2603.29761](https://arxiv.org/abs/2603.29761)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Searchless autoregressive Transformer trained on **move sequences alone** achieves 2500+ Lichess bullet Elo. Identifies **dual-capability bottleneck** P ≤ min(T, Q) between state tracking and decision quality. Elo-weighted training resolves the paradox.
- **Abstract**: Strongest reported pure move-sequence chess system. Outperforms Maia-2 by 5 pp on human move prediction.

---

## 6. Multimodal / Vision-Language Models

### 6.1 UniAR: Unified Multimodal Autoregressive Modeling
- **arXiv**: [2606.18249](https://arxiv.org/abs/2606.18249)
- **Authors**: Wujian Peng et al.
- **Inst/Company**: —
- **Key Innovation**: Single **shared discrete visual tokenizer** bridges understanding and generation. Lookup-free bitwise quantization + parallel-bitwise-prediction for spatial multi-level visual codes. Diffusion decoder for image decoding. SOTA on generation and editing.
- **Abstract**: Adapts pretrained vision encoder with multi-level feature fusion. SFT + RL achieves SOTA across understanding and generation benchmarks.

### 6.2 ARM: AutoRegressive Multimodal Model with Unified Discrete Representations
- **arXiv**: [2606.11188](https://arxiv.org/abs/2606.11188)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Discrete semantic visual tokenizer + 7B autoregressive model unifying understanding, generation, and editing. RL applied for preference alignment shows **cross-task synergy** between text-to-image generation and editing.
- **Abstract**: RL improves WISE from 0.50 to 0.56 and editing scores while inducing positive transfer between tasks.

### 6.3 TVI-CoT: Text-Visual Interleaved Chain-of-Thought Reasoning
- **arXiv**: [2606.08464](https://arxiv.org/abs/2606.08464)
- **Authors**: Lianyu Hu, Xiaoyu Ma, Zeqin Liao, Yang Liu
- **Inst/Company**: —
- **Key Innovation**: Learnable control tokens enable **dynamic switching between textual reasoning and visual feature access** during CoT. Overcomes "vision-blind reasoning" in MLLMs. +6.1% on MMMU, +3.8% on MathVerse.
- **Abstract**: First framework for explicit interleaving of text reasoning and visual grounding conditioned on evolving reasoning state.

### 6.4 UniVLR: Unified Visual Latent Reasoning
- **arXiv**: [2605.11856](https://arxiv.org/abs/2605.11856)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Renders reasoning traces + auxiliary images into **unified visual latent tokens**, eliminating text CoT path entirely. Improves reasoning accuracy by 5.4% while reducing tokens by 15.2× compared to interleaved methods.
- **Abstract**: Unified visual latent reasoning framework treating textual reasoning and visual evidence as shared visual workspace.

### 6.5 LaME: Learning to Think in Latent Space for Multimodal Embedding
- **arXiv**: [2606.13061](https://arxiv.org/abs/2606.13061)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Instantiates **Information Bottleneck principle** via K learnable reason tokens as fixed-capacity bottleneck. Dual-head design (reconstruction decoder + embedding head) structurally separates contrastive from generative supervision.
- **Abstract**: Latent reasoning multimodal embedding requiring no CoT annotation, with strong retrieval performance.

### 6.6 ROSE: Benchmarking the Perception-to-Action Gap in MLLMs
- **arXiv**: [2606.19965](https://arxiv.org/abs/2606.19965)
- **Authors**: Yihao Wang, Zijian He, Jie Ren, Keze Wang
- **Inst/Company**: —
- **Key Innovation**: Controlled benchmark holding visual scene fixed while varying region/task. Reveals **strongly model-dependent counting-to-action gap** up to 44.5 pp. Human: 98.8%, GPT-5.5: 92.2%, Gemini-3.1-Pro: 79.4%, others: 14.3–50.3%.
- **Abstract**: Diagnostic benchmark for context-conditioned visual action in MLLMs showing gap between perception and grounded action.

---

## 7. Safety, Alignment & Evaluation

### 7.1 Reasoning Structure Matters for Safety Alignment (AltTrain)
- **arXiv**: [2604.18946](https://arxiv.org/abs/2604.18946)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Shows safety failures in reasoning models stem from **reasoning structure itself**. Proposes AltTrain with three-step structure: problem understanding → harmfulness assessment → conditional reasoning. Only 1K SFT examples, no RL needed.
- **Abstract**: Explicitly alters reasoning structure for safety alignment. Generalizes across reasoning, QA, summarization, and multilingual settings.

### 7.2 STAR-S: Self-Taught Reasoning on Safety Rules
- **arXiv**: [2601.03537](https://arxiv.org/abs/2601.03537)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Iterative bootstrapping framework: **(1)** reasoning generation with flawed reasoning prefix, **(2)** reflection enhancement with safety hints, **(3)** SFT. Significantly improves jailbreak defense while balancing over-refusal.
- **Abstract**: Self-taught reasoning framework that integrates reasoning/reflection elicited by safety rules into an iterative bootstrapping pipeline.

### 7.3 Measuring the Residual Jailbreak Surface of Frontier LLMs
- **arXiv**: [2606.18193](https://arxiv.org/abs/2606.18193)
- **Authors**: AI4I / AI Security Lab
- **Inst/Company**: —
- **Key Innovation**: Systematic red-team evaluation of Anthropic Fable 5 & Opus 4.8 against 4 attack families across 7,826 harmful intents. Opus 4.8: 11.5% worst-case ASR; Fable 5: 6.1%. **Adaptive iterative attacks dominate** (95–97% of jailbreaks). 1,620 + 702 panel-confirmed harmful completions.
- **Abstract**: Even the best frontier models remain reliably breakable under sustained automated pressure. Tree-of-attacks is the strongest family.

### 7.4 Behavioral Alignment Evaluation at Depth
- **arXiv**: [2602.20813](https://arxiv.org/abs/2602.20813)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: 904 scenarios across 6 categories (Honesty, Safety, Non-Manipulation, Robustness, Corrigibility, Scheming). **Alignment behaves as unified construct** (g-factor). Even top models show gaps; most show consistent weaknesses. Human-validated scenarios.
- **Abstract**: Multi-turn evaluation framework revealing behavioral tendencies single-turn evaluations miss. Public leaderboard.

### 7.5 Emergent Alignment and the Projectability of Ethical Personas
- **arXiv**: [2606.09475](https://arxiv.org/abs/2606.09475)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Empirically demonstrates **emergent alignment**: narrow safety fine-tuning on 2 sub-categories induces broad safety behavior. Tests Constitutional AI with 4 ethical frameworks. Proposes **projectability** as alignment desideratum.
- **Abstract**: Supports persona selection hypothesis. Fine-tuned models acquire expected ethical persona (e.g., consequentialist → utilitarian alignment).

### 7.6 A Systematic Evaluation of Black-Box Uncertainty Estimation for LLMs
- **arXiv**: [2606.19868](https://arxiv.org/abs/2606.19868)
- **Authors**: Jiayi Wang, Xu-Yao Zhang
- **Inst/Company**: —
- **Key Innovation**: Benchmarks **24 black-box UE methods** across 5 categories (verbalization, sampling, explanation, multi-agent, hybrid) on 4 models. No single method dominates. Hybrid methods combining multiple uncertainty signals perform best.
- **Abstract**: Unified evaluation framework and benchmark for uncertainty estimation in API-accessible LLMs.

### 7.7 HalluScan: Benchmark for Hallucination Detection and Mitigation
- **arXiv**: [2605.02443](https://arxiv.org/abs/2605.02443)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Evaluates **72 configurations** (6 detection methods × 4 model families × 3 domains). Introduces HalluScore and Adaptive Detection Routing (ADR) achieving ~1.7× cost reduction. Self-Evaluation achieves best AUROC (0.688).
- **Abstract**: Most comprehensive hallucination benchmark framework with bootstrap confidence intervals.

### 7.8 The Governance of Human-LLM Interaction
- **arXiv**: [2606.08172](https://arxiv.org/abs/2606.08172)
- **Authors**: Manuele Reani et al.
- **Inst/Company**: —
- **Key Innovation**: Frames interaction style as governance object. Evaluates **prompt steerability and style drift** across 90,000 assistant replies with 4 persona conditions. Distinguishes safety gating, civility steering, and affective default lock-in.
- **Abstract**: Reproducible method for quantifying whether prompt-specified styles remain stable over long-horizon dialogue.

### 7.9 Adaptive Latent Agentic Reasoning (ALAR)
- **arXiv**: [2606.02871](https://arxiv.org/abs/2606.02871)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: **Dual-mode framework**: latent reasoning by default, escalates to explicit CoT only when needed. Action-Anchored Self-Distillation (AASD) trains latent mode without supervising latent states. AR-GRPO learns adaptive mode selection.
- **Abstract**: Reduces generated tokens by up to 43.6% in search and 84.6% in tool use while maintaining accuracy.

---

## 8. Synthetic Data & Data Curation

### 8.1 StateGen: State-Grounded Multi-Agent Synthetic Data Generation
- **arXiv**: [2606.16307](https://arxiv.org/abs/2606.16307)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Four-role LLM loop with **authoritative state manager** enforcing backend-is-truth invariant. Eliminates tool-call hallucinations by construction. 9.66/10 hallucination score on 49K+ samples. 23-dimensional persona trait vector.
- **Abstract**: Synthetic data platform for tool-augmented LLM agents with hierarchical multi-agent support and built-in 8-axis judge scoring.

### 8.2 Can Generalist Agents Automate Data Curation? (Curation-Bench)
- **arXiv**: [2606.04261](https://arxiv.org/abs/2606.04261)
- **Authors**: Feiyang Kang et al.
- **Inst/Company**: —
- **Key Innovation**: Agent-centric benchmark for data curation. Out-of-box agents reach strong baselines in 10 iterations. **Scaffold requiring method citation/adaption shifts agents toward meaningful exploration**. Agent autonomously composes policy beating published baselines at 1/10 data budget.
- **Abstract**: Current agents can run the curation loop, but reliable data research requires scaffolded method adaptation.

### 8.3 Trading Human Curation for Synthetic Augmentation in RLVR
- **arXiv**: [2606.03800](https://arxiv.org/abs/2606.03800)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Formalizes **cost-adjusted trade rate ρ_cost** between augmented and human-authored RLVR tasks. Retains held-out generalization. ρ_cost in [1.4×, 11.6×] across plausible cost ranges.
- **Abstract**: Substituting gated synthetic augmentations for additional human-authored tasks in RLVR maintains aggregate performance.

### 8.4 How Can We Synthesize High-Quality Pretraining Data? (FinePhrase)
- **arXiv**: [2604.13977](https://arxiv.org/abs/2604.13977)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Systematic study across rephrasing strategy, generator model, source data. **Structured output formats** (tables, math problems, FAQs, tutorials) consistently outperform baselines. Generator beyond 1B provides no additional benefit. FinePhrase: 486B tokens, 30× cost reduction.
- **Abstract**: Over 1 trillion tokens generated. FinePhrase outperforms all existing synthetic data baselines while reducing generation costs by up to 30×.

### 8.5 SUPERNOVA: Extending RLVR Beyond STEM
- **arXiv**: [2606.03800](https://arxiv.org/abs/2606.03800) (related)
- **Authors**: Ashima Suvarna, Kendrick Phan, Mehrab Beikzadeh, Hritik Bansal, Saadia Gabriel
- **Inst/Company**: —
- **Key Innovation**: Systematic curation from **natural instruction datasets** for RLVR beyond math/code. 100+ controlled experiments. Task selection tailored to target domains >> generic averaging. +64.4 pp on BigBench Extra Hard for Qwen3-0.6B.
- **Abstract**: Demonstrates human-annotated instruction data can effectively train general reasoning capabilities via strategic curation.

### 8.6 WRIT: Write-Read Intensive Trajectory Synthesis
- **arXiv**: [2606.02908](https://arxiv.org/abs/2606.02908)
- **Authors**: Hengrui Gu, Xiaotian Han, Kaixiong Zhou
- **Inst/Company**: —
- **Key Innovation**: Synthesizes agent training trajectories along **two axes**: write decisions count and evidence burden per decision. With only 2K trajectories, 4B model outperforms GPT-5.1 no-think on τ²-bench.
- **Abstract**: Addresses read-intensive decision complexity that write-intensive data alone cannot cover. Converts test-time reasoning into efficient agent behavior.

### 8.7 SynPro: Generating Pretraining Tokens from Organic Data
- **arXiv**: [2605.17849](https://arxiv.org/abs/2605.17849)
- **Authors**: —
- **Inst/Company**: CMU
- **Key Innovation**: **RL-optimized rephrasing + reformat operations** with quality, faithfulness, and data influence rewards. Continuously updated generators. Unlocks 3.7–5.2× effective tokens vs repetition in data-bound regime.
- **Abstract**: Synthetic data generation framework for learning more thoroughly from limited organic data without distribution collapse.

### 8.8 OptiMSyn: Influence-Guided Rubrics Optimization
- **arXiv**: [2604.00536](https://arxiv.org/abs/2604.00536)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Treats rubric construction as **learnable policy optimized via GRPO with influence score as reward**. Replaces heuristic rubric design with optimizer-aware gradient-aligned selection.
- **Abstract**: Closes synthesis–training loop by using target-model feedback to guide rubric generation.

---

## 9. Multi-Agent Systems & Agents

### 9.1 ALIGN: Aligned Delegation with Performance Guarantees
- **arXiv**: [2602.00127](https://arxiv.org/abs/2602.00127)
- **Authors**: —
- **Inst/Company**: —
- **Key Innovation**: Formulates LLM reasoning as an **aligned delegation game** with principal + multiple agents. Provably improves expected performance over single-agent generation even with correlated answers. Training-free.
- **Abstract**: Game-theoretic framework where agents generate candidates under designed incentives and principal selects. Theoretical guarantees.

### 9.2 Bayesian-Agent: Posterior-Guided Skill Evolution
- **arXiv**: [2606.08348](https://arxiv.org/abs/2606.08348)
- **Authors**: —
- **Inst/Company**: DataArcTech
- **Key Innovation**: Treats skills as **hypotheses with Bayesian posterior over success/failure**. Feature-conditioned categorical posterior drives patch/split/compress/retire actions. SOP-Bench 80%→95%, Lifelong AgentBench 90%→100%, RealFin-Bench 45%→65%.
- **Abstract**: Cross-harness framework for self-evolving LLM agents using posterior-guided harness optimization rather than uncalibrated prompt accumulation.

### 9.3 MemRefine: LLM-Guided Compression for Long-Term Agent Memory
- **arXiv**: [2606.13177](https://arxiv.org/abs/2606.13177)
- **Authors**: Minjae Kim, Jinheon Baek, Soyeong Jeong, Sung Ju Hwang
- **Inst/Company**: KAIST
- **Key Innovation**: Formulates **storage-budgeted memory management**. Uses similarity only to propose candidate pairs; LLM judge makes delete/merge/preserve decisions based on factual content. Consistently meets budgets while preserving performance.
- **Abstract**: Addresses unbounded memory growth in LLM agents. Outperforms rule-based baselines under tight budgets.

---

## 10. Adversarial Robustness & Uncertainty

### 10.1 Investigating Adversarial Robustness of MLLMs
- **arXiv**: [2606.13249](https://arxiv.org/abs/2606.13249) (approx.)
- **Authors**: Hashmat Shadab Malik, Muzammal Naseer, Salman Khan
- **Inst/Company**: —
- **Key Innovation**: Systematic investigation revealing **large-scale multimodal adversarial pretraining** (not unimodal scale) is critical for robustness transfer. End-to-end multimodal training yields +28 CIDEr, +11.7% VQA accuracy under attack.
- **Abstract**: Test-time visual stochastic transformations serve as effective black-box defense for non-robust MLLMs.

---

## 11. LLM Evaluation

### 11.1 Beyond Static Leaderboards: Predictive Validity for LLM Agents
- **arXiv**: [2606.19704](https://arxiv.org/abs/2606.19704)
- **Authors**: Dhaval C. Patel et al. (50+ authors)
- **Inst/Company**: —
- **Key Innovation**: Proposes ranking by **predictive validity** (in-sample vs out-of-sample rank correlation) rather than aggregate scores. 14 parallel implementation studies of MCP-based agent benchmark. 12-tier measurement apparatus.
- **Abstract**: Demonstrates aggregate score leaderboards underspecify deployed-agent evaluation. Proposes predictive validity as ranking criterion.

---

## Key Themes This Week

1. **GRPO saturation and evolution**: The field is moving past vanilla GRPO with numerous extensions — replay buffers (μ-GRPO), process supervision (GRPO-VPS), graph-based rollouts (GraphPO), latent-space variants (Latent-GRPO), and value-implicit critics (VIMPO). Clear trend toward denser credit assignment and better sample efficiency.

2. **Sparse attention goes production**: MiniMax MSA and SparDA both demonstrate that block-sparse attention can deliver order-of-magnitude speedups at very long contexts (1M+) with no accuracy loss, in production-grade systems.

3. **Generative recommenders dominate advertising**: CADET (LinkedIn), GRAB (Baidu), GR4AD (Kuaishou), OneRanker (Tencent), Memento (Meta) — all major ad platforms are deploying decoder-only / generative approaches for CTR prediction and ranking, moving past DLRM-era architectures.

4. **Synthetic data as first-class engineering**: Multiple papers demonstrate principled synthetic data generation (principled scaling laws, RL-optimized generation, cost-effective augmentation) as a systematic discipline rather than ad-hoc prompting.

5. **Safety research deepens**: From reasoning structure modification (AltTrain) to large-scale red-teaming (Anthropic models) to behavioral alignment evaluation, safety work is becoming more rigorous and structured.

6. **VLMs learn to act**: Odysseus (100+ turn game-playing), UniAR and ARM (unified multimodal generation/understanding), and TVI-CoT (interleaved visual-text reasoning) show VLMs are rapidly integrating perception, reasoning, and action.
