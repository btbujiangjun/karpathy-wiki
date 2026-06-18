---
title: arXiv AI Research Scan — June 2026
type: synthesis
created: 2026-06-18
updated: 2026-06-18
sources: []
tags: [arxiv, survey, llm, ctr, recommendation, games, sequential-modeling, reasoning]
---

# arXiv AI Research Scan — June 2026

Curated selection of recent arXiv preprints across AI, LLMs, recommendation, advertising, CTR, sequential modeling, games, and reasoning. Covers papers submitted ~Jun 2–17, 2026.

---

## LLM Architecture & Efficiency

### Variable-Width Transformers
- **Authors**: Zhaofeng Wu, Oliver Sieberling, Shawn Tan, Rameswar Panda, Yury Polyanskiy, Yoon Kim
- **Affiliation**: MIT, NVIDIA
- **Link**: https://arxiv.org/abs/2606.18246
- **Innovation**: Proposes `><former` — a transformer with wider early/late layers and narrower middle layers. Uses parameter-free residual resizing. Achieves 22% FLOP reduction and 15% KV cache reduction at matched loss. Demonstrates nonuniform width allocation as a resource-optimal scaling strategy for decoder-only LMs (200M–2B dense, 3B MoE).

### Mamba-3: Improved Sequence Modeling using State Space Principles
- **Authors**: Mamba team
- **Link**: https://arxiv.org/abs/2603.15569
- **Innovation**: Three core improvements over Mamba-2: (1) exponential-trapezoidal discretization for more expressive dynamics, (2) complex-valued state updates enabling richer state tracking, (3) multi-input multi-output (MIMO) formulation for better throughput. At 1.5B scale, outperforms Gated DeltaNet and prior linear-time models on retrieval, state-tracking, and language modeling.

### Swimba: Switch Mamba — MoE-Parameterized State Space Models
- **Authors**: —
- **Link**: https://arxiv.org/abs/2603.06938
- **Innovation**: First MoE-parameterized SSM layer. Each expert produces candidate SSM streams; a token-level router mixes them in parameter space before a single recurrence pass. Avoids replicating the expensive SSM recurrence across experts while scaling parameters. Deployed in NVIDIA Nemotron hybrid architectures.

### Sessa: Selective State Space Attention
- **Authors**: —
- **Link**: https://arxiv.org/abs/2604.18580
- **Innovation**: Decoder architecture injecting input-dependent attention into a feedback (recurrent) path. Combines direct-read input-dependent routing with stateful aggregation. Maintains long-range sensitivity where pure SSMs (Mamba) fail due to exponential forgetting. Theoretical analysis via temporal routing lens.

### 2Mamba2Furious: Linear Complexity Competitive with Softmax Attention
- **Authors**: —
- **Link**: https://arxiv.org/abs/2602.17363
- **Innovation**: Simplifies Mamba-2 to its core components (Mamba-2S), then adds higher-order hidden states. Achieves softmax-level accuracy with linear memory complexity. The exponentiated variant (2Mamba-E) exceeds softmax attention performance on certain benchmarks.

### UniMamba: Unified Spatial-Temporal Forecasting with SSM + Attention
- **Authors**: —
- **Link**: https://arxiv.org/abs/2604.16325
- **Innovation**: Hybrid SSM-attention framework for multivariate time series. Mamba Variate-Channel Encoding with FFT-Laplace + TCN captures global temporal dependencies; Spatial Temporal Attention Layer jointly models cross-variate correlations. Outperforms SOTA on 8 public benchmarks.

### Accelerating Speculative Diffusions via Block Verification
- **Authors**: Alexander Soen et al.
- **Link**: https://arxiv.org/abs/2606.13426
- **Innovation**: Adapts block verification (from LLM speculative decoding) to diffusion models. Free Drafter — a training-free self-speculative drafter — yields up to 6.3% speedup with negligible overhead.

---

## Reasoning & Inference-Time Compute

### Beyond the Commitment Boundary: Probing Epiphenomenal CoT
- **Authors**: Daniel Scalena, Sara Candussio, Luca Bortolussi, Elisabetta Fersini, Malvina Nissim, Gabriele Sarti
- **Affiliation**: University of Trieste, University of Milan, TU Delft, University of Groningen
- **Link**: https://arxiv.org/abs/2606.13603
- **Innovation**: Identifies a "commitment boundary" — a sharp transition where the model commits to a final answer mid-chain. Subsequent CoT steps are *epiphenomenal* (don't change answer probability). Early-exiting at this boundary reduces CoT length by up to 55% with negligible accuracy loss. Attention probes can decode answer formation from intermediate steps.

### Agentic Chain-of-Thought Steering (ACTS)
- **Authors**: Yu Xia et al.
- **Link**: https://arxiv.org/abs/2606.03965
- **Innovation**: Formulates reasoning steering as an MDP. A controller agent observes the trace and remaining budget, then issues a steering action (reasoning strategy + steering phrase). Trained via RL with budget-conditioned reward shaping. Matches full-thinking performance with substantial token savings across multiple benchmarks.

### Adaptive Latent Agentic Reasoning (ALAR)
- **Authors**: —
- **Link**: https://arxiv.org/abs/2606.02871
- **Innovation**: Dual-mode framework: compact latent reasoning for routine agentic turns, selective escalation to explicit CoT for hard decisions. Uses agent actions as supervision anchors for latent reasoning. Reduces generated tokens by 43.6% (search) and 84.6% (tool use) while maintaining or improving accuracy.

### Reasoning Structure of Large Language Models
- **Authors**: Frédéric Berdoz, Luca A. Lanzendörfer, Fabian Farestam, Roger Wattenhofer
- **Affiliation**: ETH Zurich
- **Link**: https://arxiv.org/abs/2606.03883
- **Innovation**: Converts unstructured CoT traces into verifiable reasoning graphs (claims + dependencies). Defines a reasoning efficiency metric measuring topological concentration. Shows structural measurements separate behaviors that token count and accuracy conflate.

### Architecture-Aware RL Makes Sliding-Window Attention Competitive (SWARR)
- **Authors**: Kai Liu et al.
- **Link**: https://arxiv.org/abs/2606.11634
- **Innovation**: Two-stage recipe: (1) convert pretrained SA model to SWA via SFT, (2) adapt via RL. On-policy RL adapts trajectories to SWA constraints, closing most of the accuracy gap. Central finding: RL changes the conclusion about SWA viability for math reasoning.

### Streaming Communication in Multi-Agent Reasoning (StreamMA)
- **Authors**: Zhen Yang et al.
- **Link**: https://arxiv.org/abs/2606.05158
- **Innovation**: Streams reasoning tokens to downstream agents as generated (pipelining). Improves both latency and accuracy — early reasoning steps are more reliable, so streaming prevents late error-prone steps from misleading downstream agents. First closed-form joint analysis of stream/serial/single protocols. Discovers a "step-level scaling law."

### RKSC: Reasoning-Aware KV Cache Sharing and Confident Early Exit
- **Authors**: Anirudh Sekar et al.
- **Link**: https://arxiv.org/abs/2606.09937
- **Innovation**: Training-free inference acceleration for multi-branch reasoning. ASKS shares prefix KV cache across semantically similar branches via cosine similarity (generalizing vLLM prefix caching). CGEE dual-level early exit (verify-skip gate + layer-level entropy exit). Achieves 3.008x mean speedup, 1.66x over vLLM, with 0.37% error rate.

### Reasoning Structure Matters for Safety Alignment (AltTrain)
- **Authors**: —
- **Link**: https://arxiv.org/abs/2604.18946
- **Innovation**: Alters reasoning structure of LRMs (R1, S1) for safety via a three-step structure: problem understanding → harmfulness assessment → conditional reasoning. 1K SFT examples, 60 min training on A6000, 2–10x token reduction. Strong generalization against diverse attack scenarios.

---

## CTR Prediction & Advertising Recommendation

### DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR
- **Authors**: Wenzhuo Cheng, Shipeng Nie, Qixin Guo, Xuefeng Sun, Jianguo Lou, Zhengwei Zheng
- **Affiliation**: Major social-media platform
- **Link**: https://arxiv.org/abs/2606.07980
- **Innovation**: Dual-path residual for CTR Transformers: Identity path (preserves gradient flow) + Block Attention Residual path (cross-layer attention over all earlier blocks). Pointwise AttnRes replaces Softmax with SiLU for parallel multi-interest activation. Up to +0.32% AUC at <5% extra FLOPs. 1.66x steeper compute-AUC scaling law — 8-layer DeRes matches 16-layer OneTrans.

### Memento: Personalized RAG-Style Long-Retention Data Scaling for Online Ads
- **Authors**: Meta
- **Link**: https://arxiv.org/abs/2605.24051
- **Innovation**: RAG-style framework treating historical user engagements as a document corpus. Two variants: Representation Memento (retrieves historical embeddings) and Data Memento (retrieves past training examples). MMR-based retrieval. 5–10x resource efficiency over linear scaling. **1% CTR lift and 1.2% CVR lift** on Facebook Feed/Reels at 365-day retention.

### GR4AD: Generative Recommendation for Large-Scale Advertising
- **Authors**: Kuaishou
- **Link**: https://arxiv.org/abs/2602.22732
- **Innovation**: Production generative recommender. UA-SID (Unified Ad Semantic ID), LazyAR (lazy autoregressive decoder relaxing layer-wise dependencies for short multi-candidate generation), VSL + RSPO (value-aware ranking-aware RL), dynamic beam serving. **Up to 4.2% ad revenue improvement**. Deployed at Kuaishou (400M+ users, <10ms latency).

### OneRanker: Unified Generation and Ranking with One Model
- **Authors**: Dekai Sun et al. (Tencent)
- **Link**: https://arxiv.org/abs/2603.02999
- **Innovation**: Architectural-level deep integration of generation and ranking. Value-aware multi-task decoupling via task token sequences + causal mask. Coarse-to-fine target awareness with Fake Item Tokens. Key/Value pass-through + Distribution Consistency Constraint Loss. Full deployment on Weixin Channels ads, **GMV +1.34%** .

### CADET: Context-Conditioned Ads CTR with Decoder-Only Transformer
- **Authors**: LinkedIn
- **Link**: https://arxiv.org/abs/2602.11410
- **Innovation**: End-to-end decoder-only transformer for ads CTR. Context-conditioned decoding with multi-tower prediction heads handling post-scoring signals (ad position, resolves chicken-and-egg). Self-gated attention, timestamp-based RoPE, session masking. **11.04% CTR lift** over LiRank baseline. Deployed on LinkedIn sponsored updates.

### GRAB: LLM-Inspired Sequence-First CTR at Baidu
- **Authors**: Baidu
- **Link**: https://arxiv.org/abs/2602.01865
- **Innovation**: Generative ranking framework with Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics. **3.05% revenue increase, 3.49% CTR lift** in production. AUC scales monotonically with model capacity and sequence length without saturation.

### IDProxy: Cold-Start CTR with Multimodal LLMs
- **Authors**: Xiaohongshu
- **Link**: https://arxiv.org/abs/2603.01590
- **Innovation**: MLLM-generated proxy embeddings for cold-start items, aligned with existing ID embedding space and optimized end-to-end under CTR objectives. Deployed in Content Feed and Display Ads.

### RankUp: High-Rank Representations for Large-Scale Ads
- **Authors**: Tencent (Weixin)
- **Link**: https://arxiv.org/abs/2604.17878
- **Innovation**: Addresses representation collapse in deep recommenders. Randomized permutation splitting over sparse features, multi-embedding paradigm, global token integration. **GMV improvements: +3.41% (Video Accounts), +4.81% (Moments), +2.12% (Official Accounts).**

### UniSID: End-to-End Semantic ID Generation for Generative Ads
- **Authors**: —
- **Link**: https://arxiv.org/abs/2602.10445
- **Innovation**: Unified SID generation framework jointly optimizing embeddings and SIDs end-to-end from raw ad data. Multi-granularity contrastive learning + summary-based ad reconstruction. Up to 4.62% improvement in Hit Rate vs SOTA baselines.

### DAIAN: Deep Adaptive Intent-Aware Network for CTR
- **Authors**: —
- **Link**: https://arxiv.org/abs/2602.13971
- **Innovation**: Adaptive intent-aware CTR for trigger-induced recommendation. Hybrid enhancer combining ID and semantic information for similarity reinforcement. Adaptive selection based on varying intents. Validated on industrial e-commerce datasets.

---

## Games & Multi-Agent RL

### Tracking vs Deciding: Dual-Capability Bottleneck in Chess Transformers
- **Authors**: —
- **Link**: https://arxiv.org/abs/2603.29761
- **Innovation**: Searchless autoregressive Transformer learning from pure move sequences. Formalizes performance as P ≤ min(T, Q) — dual-capability bottleneck between state tracking and decision quality. Elo-weighted training resolves the paradox. **Reaches Lichess bullet 2570** (120M params, no search, no board representation). Outperforms Maia-2 by 5pp on human move prediction.

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: —
- **Link**: https://arxiv.org/abs/2605.00347
- **Innovation**: First systematic study of RL-based VLM training for long-horizon (100+ turn) game playing (Super Mario Land). Adapted PPO with lightweight turn-level critic outperforms GRPO/Reinforce++. At least **3x average game progress** vs frontier models. Demonstrates cross-game generalization.

### MEMO: Memory-Augmented Model Context Optimization
- **Authors**: —
- **Link**: https://arxiv.org/abs/2603.09022
- **Innovation**: Self-play framework optimizing inference-time context via tournament-style context evolution + persistent memory bank (CRUD operations). Raises GPT-4o-mini win rate from 25.1% to 49.5% across 5 text-based games using only 2,000 self-play games (19x fewer than RL baselines). Learned contexts transfer across games.

### MemoPilot: RL over Memory for Test-Time Learning of LLM Agents
- **Authors**: —
- **Link**: https://arxiv.org/abs/2606.08656
- **Innovation**: Trains memory update process via multi-turn GRPO with turn-level advantage estimation. Frozen LLM player improves across repeated interactions. **Ranked #1 in Elo on Limit Texas Hold'em (1762) and RPS (1590)** , outperforming DeepSeek-V3.2 and all baseline memory methods.

### Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Self-Play
- **Authors**: —
- **Link**: https://arxiv.org/abs/2604.17696
- **Innovation**: Self-play with trajectory advantages modulated by Reasoning Abstraction Coefficient (φ) and Reasoning Evolution Reward (ψ). Trains on text-based games (Tic-Tac-Toe, Kuhn Poker, Simple Negotiation); transfers to math and general reasoning benchmarks. Human evaluation confirms more abstract, progressive reasoning patterns.

### Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents
- **Authors**: —
- **Link**: https://arxiv.org/abs/2603.17683
- **Innovation**: ARC-AGI-3 agent with two-player architecture (perception vs action), curriculum-based learning, database-as-control-plane (cognitive state in SQLite). Achieves 50–94x sample efficiency over comparable systems (~32 attempts vs 1,600–3,000). Failure analysis reveals bottleneck shifted to perceptual grounding.

### MARL-GPT: Foundation Model for Multi-Agent RL
- **Authors**: —
- **Link**: https://arxiv.org/abs/2604.05943
- **Innovation**: Single GPT-based model performing across diverse MARL environments (SMACv2, Google Research Football, POGEMA). Trained via offline RL on expert trajectories (400M–1B steps) with transformer-based observation encoder requiring no task-specific tuning. Competitive with specialized baselines.

### NeuroGame Transformer: Gibbs-Inspired Attention via Game Theory
- **Authors**: Djamel Bouchaffra, Faycal Ykhlef, Hanene Azzag, Mustapha Lebbah, Bilal Faye
- **Link**: https://arxiv.org/abs/2603.18761
- **Innovation**: Reconceptualizes attention as cooperative game (tokens as players) + statistical physics (tokens as interacting spins). Shapley values for global attribution + Banzhaf indices for local influence, combined via learnable gating. Attention weights emerge as Gibbs distribution marginals. 86.4% on SNLI, competitive with RoBERTa-Base.

### OpenClaw-Skill: Collective Skill Tree Search for Agentic LLMs
- **Authors**: —
- **Link**: https://arxiv.org/abs/2606.16774
- **Innovation**: Tree-search-based skill construction framework using collective intelligence. Collective Skill Node Generation (CSN-Gen) + Collective Skill Node Assessment (CSN-Assess). Multi-skill selection prevents homogeneous solutions. Significant gains in long-horizon planning and tool use.

---

## Alignment, Safety & Understanding

### The Shibboleth Effect: Cross-Lingual Distributional Skew of LLMs
- **Authors**: Hakan Mehmetcik et al.
- **Link**: https://arxiv.org/abs/2606.11082
- **Innovation**: Multi-agent geopolitical wargame (Cerulean Sea Crisis) testing 6 frontier models (GPT-4o, Llama-4, Mistral-Large, Gemini-3.1-Pro, Qwen3.6-Plus, DeepSeek-R1) in English vs Turkish. Llama-4 shows +0.800 increase in coercive rhetoric under Turkish; DeepSeek-R1 buffers via CoT anchoring. Demonstrates skew is model-architecture contingent, not universal.

### Loss Landscape Poisoning: Targeted Extraction of Unseen Training Data from LLMs
- **Authors**: —
- **Link**: https://arxiv.org/abs/2606.17110
- **Innovation**: Attack reshaping local loss landscape around target completion — creates sharp minimum forcing memorization. Up to 100% extraction success (language), 90% (vision-language). Bypasses even differential privacy via direct loss landscape probing. Applies to centralized and federated settings.

### Brain-Guided LLMs for Robust Reasoning
- **Authors**: —
- **Link**: https://arxiv.org/abs/2606.11893
- **Innovation**: Uses fMRI signals from reasoning-related brain regions to steer LLM representations. LLMs explain ~76% of explainable variance in aggregate neural responses. Brain-guided intervention yields up to 13% absolute accuracy gain across 10 LLMs (1.5B–72B), transferring across reasoning types.

### MemRefine: LLM-Guided Compression for Long-Term Agent Memory
- **Authors**: Minjae Kim et al.
- **Link**: https://arxiv.org/abs/2606.13177
- **Innovation**: Formulates storage-budgeted memory management. Uses similarity only for candidate pairing, defers delete/merge/preserve decisions to an LLM judge based on factual content. Iterates until budget is met. Consistently meets target budgets while preserving downstream performance.

---

## Summary

| Domain | Papers Found | Key Trends |
|--------|-------------|------------|
| LLM Architecture | 7 | Nonuniform width, Mamba-3 advances, MoE-SSM hybrids, SSM+Attention fusion, speculative decoding for diffusions |
| Reasoning | 8 | Epiphenomenal CoT, budget-aware steering, latent vs explicit reasoning, multi-agent streaming, KV cache sharing |
| CTR & Ads | 10 | RAG-style long retention, generative recommendation, decoder-only unification, cold-start via MLLMs, residual redesign |
| Games & Multi-Agent | 9 | Searchless chess, VLM game agents, learned memory policies, curriculum learning, MARL foundation models, game-theoretic attention |
| Alignment & Safety | 4 | Cross-lingual behavioral skew, data extraction attacks, brain-guided alignment, agent memory compression |
