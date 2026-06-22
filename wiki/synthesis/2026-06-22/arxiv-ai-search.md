---
title: "arXiv AI Search — June 2026"
type: synthesis
created: 2026-06-22
updated: 2026-06-22
tags: [arxiv, survey, ai, llm, recommendation, ctr, advertising, rl, games, attention]
---

# arXiv AI Search — June 2026

> Curated recent papers across AI, LLMs, recommendation, CTR prediction, advertising, sequential modeling, games, and RL. Compiled 2026-06-22.

---

## 1. LLM Training, Optimization & Scaling

### 1.1 Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling
- **Authors**: LightningLM team
- **Institution**: Academic/independent
- **Link**: [2606.07404](https://arxiv.org/abs/2606.07404)
- **Key Innovation**: Trains a 120B sparse MoE on a single 8-GPU node via reversible recurrence (flat activation memory), state-preserving growth (dense → MoE → deeper → more experts), and TQP (quantized base weights + trained LoRA adapters cutting optimizer state 45×). Reports silent failures that produce plausible checkpoints while violating invariants.
- **Tags**: `MoE`, `memory-efficiency`, `reversible-training`, `scaling`

### 1.2 Spectral Scaling Laws of Muon
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2606.04058](https://arxiv.org/abs/2606.04058)
- **Key Innovation**: First systematic study of Muon optimizer's momentum spectrum across 77M–2.8B GPT-2 models. Finds power-law stabilization values per layer with exponents from −0.25 (mid-layers) to −0.96 (final MLP). Shows uniform Newton-Schulz configuration is suboptimal at scale; final layers need more accurate orthonormalization.
- **Tags**: `optimizer`, `muon`, `scaling-laws`, `theory`

### 1.3 Rethinking Local Learning: LoPT for LLM Post-Training
- **Authors**: Humyu Shi et al.
- **Institution**: Academic
- **Link**: [2605.04913](https://arxiv.org/abs/2605.04913)
- **Key Innovation**: Places gradient boundary at transformer midpoint — second half learns from task objective, first half from feature reconstruction. Competes with full-depth backprop at lower memory and higher efficiency in both SFT and GRPO regimes.
- **Tags**: `post-training`, `memory-efficiency`, `sft`, `grpo`

### 1.4 PC Layer: Polynomial Weight Preconditioning for Improving LLM Pre-Training
- **Authors**: Senmiao Wang et al.
- **Institution**: Academic
- **Link**: [2606.06470](https://arxiv.org/abs/2606.06470)
- **Key Innovation**: Preconditioning layer via low-degree polynomial that reshapes singular-value spectrum of weight matrices during training; merges back at inference (no overhead). Improves Llama-1B pre-training loss with both AdamW and Muon. Theoretical proof for deep linear networks.
- **Tags**: `preconditioning`, `pre-training`, `optimization`

### 1.5 Schedule-Level Shared-Prefix Reuse for LLM RL Training
- **Authors**: Pengbo Li, Feiyuan Zhang et al.
- **Institution**: Academic
- **Link**: [2606.01143](https://arxiv.org/abs/2606.01143)
- **Key Innovation**: Decouples prefix/suffix computation in GRPO/PPO training — runs prefix forward once, suffixes as microbatches reusing prefix KV cache, then one prefix backward. Up to 4.4× speedup, 59% HBM reduction. Numerically equivalent to baseline.
- **Tags**: `rl-training`, `grpo`, `ppo`, `prefix-reuse`, `distributed`

### 1.6 Scaling Adaptive Depth with Norm-Agnostic Residual Networks (NAG)
- **Authors**: Tomás Figliolia, Beren Millidge
- **Institution**: Academic
- **Link**: [2606.16112](https://arxiv.org/abs/2606.16112)
- **Key Innovation**: Separates magnitude from directional info in residual stream so later layers aren't suppressed by norm growth. Enables Mixture-of-Depths (skip attention+MLP) as pretraining scaling strategy — 20–25% skip rate matches full-depth under iso-FLOP.
- **Tags**: `architecture`, `residual-networks`, `mixture-of-depths`, `scaling`

### 1.7 SpanNorm: Reconciling Stability and Performance in Transformer Normalization
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2601.22580](https://arxiv.org/abs/2601.22580)
- **Key Innovation**: Structural span from block input to final normalization, bypassing intermediate layers — combines PreNorm stability with PostNorm performance. Scaled to 128-layer 6.5B model.
- **Tags**: `normalization`, `transformer`, `training-stability`

---

## 2. LLM Architectures & Attention

### 2.1 MiniMax Sparse Attention (MSA)
- **Authors**: MiniMax AI
- **Institution**: MiniMax
- **Link**: [2606.13392](https://arxiv.org/abs/2606.13392)
- **Key Innovation**: Blockwise sparse attention with lightweight Index Branch (max-pooling scoring + Top-k per GQA group) and exact block-sparse Main Branch. On 109B MoE: 28.4× FLOP reduction at 1M context, 14.2× prefill and 7.6× decode speedup on H800.
- **Tags**: `sparse-attention`, `long-context`, `efficiency`

### 2.2 SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference
- **Authors**: Yaosheng Fu et al.
- **Institution**: Academic
- **Link**: [2606.04511](https://arxiv.org/abs/2606.04511)
- **Key Innovation**: Fourth "Forecast" projection predicts KV blocks for next layer, enabling CPU→GPU prefetch overlap. <0.5% added params. Up to 1.7× decode speedup, 5.3× decode throughput vs non-offload sparse baseline.
- **Tags**: `sparse-attention`, `inference`, `long-context`

### 2.3 HydraHead: From Head-Level Functional Heterogeneity to Specialized Attention Hybridization
- **Authors**: Zhentao Tan, Wei Chen et al.
- **Institution**: Academic
- **Link**: [2606.20097](https://arxiv.org/abs/2606.20097)
- **Key Innovation**: Hybridizes full+linear attention at head level (not layer level). Interpretability-driven selection preserves FA only on retrieval-critical heads. 69% improvement at 512K context vs baseline; approaches Qwen3.5 with only 15B training tokens.
- **Tags**: `hybrid-attention`, `linear-attention`, `long-context`

### 2.4 The Recurrent Transformer
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2604.21215](https://arxiv.org/abs/2604.21215)
- **Key Innovation**: Layerwise recurrence — each layer's KV comes from its own outputs, not previous layer. Emulates both standard Transformer and token-level RNN. IO-aware tiling reduces memory traffic from O(N²) to O(N log N).
- **Tags**: `recurrent`, `transformer`, `architecture`

### 2.5 Parallel Causal Associative Fields (PCAF)
- **Authors**: Independent
- **Institution**: Academic (Google TPU)
- **Link**: [2606.10435](https://arxiv.org/abs/2606.10435)
- **Key Innovation**: Content-addressed memory over causal successor records — hash buckets for sparse cache retrieval + parametric local LM, gated mixture. 303M model: 36.31 PPL on WikiText-103, 0.61M tok/s throughput. Avoids single fixed-state bottleneck of SSMs.
- **Tags**: `associative-memory`, `sparse-attention`, `language-modeling`

### 2.6 Hyperloop Transformers
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2604.21254](https://arxiv.org/abs/2604.21254)
- **Key Innovation**: Looped transformer (begin/middle/end blocks, middle looped) + hyper-connections (matrix-valued residual streams after each loop). Outperforms depth-matched transformers with ~50% fewer parameters. Gains persist through quantization.
- **Tags**: `efficient-architecture`, `looped`, `parameter-efficiency`

### 2.7 Efficiently Representing Algorithms with Chain-of-Thought Transformers
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2606.19697](https://arxiv.org/abs/2606.19697)
- **Key Innovation**: Proves CoT transformers can simulate Word RAM algorithms with only polylog overhead (vs quadratic for Turing machine simulations). Covers discrete CoT, continuous CoT (vector tokens), and hybrid transformer+linear RNN.
- **Tags**: `theory`, `chain-of-thought`, `expressiveness`

---

## 3. Recommendation Systems (Generative & Sequential)

### 3.1 PauseRec: Implicit Reasoning for LLM-based Generative Recommendation
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2606.14142](https://arxiv.org/abs/2606.14142)
- **Key Innovation**: Inserts trainable "pause" tokens before SID generation instead of explicit CoT rationales. Bridges text-SID gap via learned latent computation. Up to 6.22% improvement over CoT-based methods, 65% less GPU training, 71.3% faster inference.
- **Tags**: `generative-recommendation`, `implicit-reasoning`, `semantic-id`

### 3.2 GenAIR: Generative Archetype-Grounded Item Representations for Sequential Recommendation
- **Authors**: AI-Santiago
- **Institution**: Academic
- **Link**: [2606.11023](https://arxiv.org/abs/2606.11023)
- **Key Innovation**: LLM generates archetype descriptions (ideal target audience) for items, then extracts embeddings + behavioral calibration to ground in real interactions. Seamless plug-in for existing sequential models.
- **Tags**: `sequential-recommendation`, `llm`, `item-representation`

### 3.3 Gryphon: A Unified Architecture for Semantic-ID Generation and Item-Level Scoring
- **Authors**: Z. Hu, Y. Chen, Y. Pan et al.
- **Institution**: Industrial (music streaming service)
- **Link**: [2606.08604](https://arxiv.org/abs/2606.08604)
- **Key Innovation**: Adds jointly trained item-level scoring alongside SID generation in encoder-decoder GR. Resolves SID-collision/miscalibration issues. +3.7% Recall@1000 over vanilla GR. Replaced 15+ candidate generators + preranking in 7-day A/B test.
- **Tags**: `generative-recommendation`, `semantic-id`, `industrial`, `candidate-generation`

### 3.4 MLTFR: Multi-LLM Token Filtering and Routing for Sequential Recommendation
- **Authors**: Wuhan Chen et al.
- **Institution**: Academic
- **Link**: [2604.18200](https://arxiv.org/abs/2604.18200)
- **Key Innovation**: Uses token embeddings from multiple LLMs without any textual input. User-guided token filtering + MoE routing with Fisher-weighted consensus. Outperforms SOTA sequential recommenders without backbone modification.
- **Tags**: `sequential-recommendation`, `multi-llm`, `moixture-of-experts`

### 3.5 L2Rec: Dual-View Understanding of LLMs for Personalized Recommendation
- **Authors**: Independent
- **Institution**: Academic/Industrial (SIGIR 2026)
- **Link**: [2605.26717](https://arxiv.org/abs/2605.26717)
- **Key Innovation**: Unifies behavioral and semantic understanding at parameter level via Dual-view Personalized MoE (DPMoE). Single frozen LLM backbone with view-specific low-rank perturbations. Online A/B tests show significant engagement improvements.
- **Tags**: `personalized-recommendation`, `llm`, `parameter-efficient`

### 3.6 SMTPO: User Simulator-Guided Multi-Turn Preference Optimization
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2604.03671](https://arxiv.org/abs/2604.03671)
- **Key Innovation**: Reasoning LLM-based conversational recommender with simulator-guided multi-turn RL. Multi-task SFT for simulator alignment + fine-grained reward design. Addresses feedback bias accumulation in multi-turn CRS.
- **Tags**: `conversational-recommendation`, `reinforcement-learning`, `reasoning-llm`

### 3.7 From Logs to Language: Learning Optimal Verbalization for LLM-Based Recommendation
- **Authors**: Yucheng Shi, Ying Li et al.
- **Institution**: Industrial
- **Link**: [2602.20558](https://arxiv.org/abs/2602.20558)
- **Key Innovation**: RL-based verbalization agent learns how to convert structured logs into optimal text for LLM recommenders. 93% relative improvement in discovery item accuracy over template baselines. Emergent strategies: summarization, noise removal, syntax normalization.
- **Tags**: `verbalization`, `llm-recommendation`, `reinforcement-learning`

### 3.8 Principled Synthetic Data Enables First Scaling Laws for LLMs in Recommendation
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2602.07298](https://arxiv.org/abs/2602.07298)
- **Key Innovation**: Layered synthetic data curriculum (collaborative filtering + UI histories) enables first demonstrable power-law scaling (0.6B–8B, 163B tokens) for LLM CPT in recommendation. Sequential models trained on this data outperform real-data models by +130% Recall@100.
- **Tags**: `scaling-laws`, `synthetic-data`, `llm-recommendation`

### 3.9 SIDReasoner: Reasoning over Semantic IDs Enhances Generative Recommendation
- **Authors**: HappyPointer
- **Institution**: Academic
- **Link**: [2603.23183](https://arxiv.org/abs/2603.23183)
- **Key Innovation**: Two-stage framework — multi-task SFT for SID-language alignment (teacher distillation) + outcome-driven reinforced optimization. First work to elicit reasoning over SIDs without requiring reasoning annotations.
- **Tags**: `reasoning`, `semantic-id`, `generative-recommendation`

### 3.10 From Token to Item: Item-Aware Attention Mechanism (IAM)
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2603.19693](https://arxiv.org/abs/2603.19693)
- **Key Innovation**: Categorizes token relations into intra-item (content semantics) and inter-item (collaborative relations). Two dedicated attention layers per category. Explicitly models items as fundamental units in LLM-based recommenders.
- **Tags**: `attention-mechanism`, `llm-recommendation`, `item-aware`

---

## 4. CTR Prediction & Advertising

### 4.1 CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer
- **Authors**: LinkedIn
- **Institution**: LinkedIn (Microsoft)
- **Link**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Key Innovation**: End-to-end decoder-only transformer for ads CTR at LinkedIn. Context-conditioned decoding with multi-tower heads (resolves CTR×position chicken-and-egg), self-gated attention, timestamp RoPE, session masking. 11.04% CTR lift over LiRank. Deployed on LinkedIn homepage.
- **Tags**: `ctr`, `advertising`, `decoder-only`, `linkedin`

### 4.2 GenLI: Generative Long-term User Interest Modeling for CTR Prediction
- **Authors**: Independent
- **Institution**: Industrial
- **Link**: [2605.15905](https://arxiv.org/abs/2605.15905)
- **Key Innovation**: Generative multi-interest distributions (target-independent) with O(1) behavior retrieval via lookup (not pairwise matching). Serves hundreds of millions of users. 1.56% RPM lift online.
- **Tags**: `ctr`, `user-interest`, `generative`, `long-sequence`

### 4.3 IDProxy: Cold-Start CTR Prediction with Multimodal LLMs
- **Authors**: Yubin Zhang, Haiming Xu et al.
- **Institution**: Xiaohongshu
- **Link**: [2603.01590](https://arxiv.org/abs/2603.01590)
- **Key Innovation**: MLLM generates proxy embeddings for cold-start items, aligned with existing ID embedding space via CTR objectives. Deployed in both Content Feed and Display Ads on Xiaohongshu Explore Feed.
- **Tags**: `cold-start`, `ctr`, `multimodal-llm`, `xiaohongshu`

### 4.4 DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction
- **Authors**: Independent
- **Institution**: Academic/Industrial
- **Link**: [2606.07980](https://arxiv.org/abs/2606.07980)
- **Key Innovation**: Dual-path residual: Identity path (gradient flow) + Block Attention Residual (cross-layer recall) with SiLU-based gating (forgetting weights). 331M interaction industrial dataset. +0.32% AUC at <5% extra FLOPs. 1.66× steeper compute–AUC scaling law.
- **Tags**: `ctr`, `residual-networks`, `scaling`, `attention`

### 4.5 GenCI: Generative User Interest Shift via Cohort-based Intent Learning
- **Authors**: Independent
- **Institution**: Academic (WWW 2026)
- **Link**: [2601.18251](https://arxiv.org/abs/2601.18251)
- **Key Innovation**: Generative model (NTP) produces candidate interest cohorts — candidate-agnostic intent representations. Hierarchical candidate-aware network injects cohort context into ranking. Addresses interest shift and point-wise ranking myopia.
- **Tags**: `ctr`, `generative`, `user-intent`, `cohort`

### 4.6 OneRanker: Unified Generation and Ranking with One Model
- **Authors**: Tencent
- **Institution**: Tencent (WeChat Channels)
- **Link**: [2603.02999](https://arxiv.org/abs/2603.02999)
- **Key Innovation**: Value-aware multi-task decoupling via task tokens + causal mask. Coarse-to-fine target awareness: Fake Item Tokens for implicit generation, ranking decoder for explicit value alignment. Deployed on WeChat Channels. GMV +1.34%.
- **Tags**: `generative-advertising`, `unified-ranking`, `tencent`

### 4.7 GRAB: Generative Ranking for Ads at Baidu
- **Authors**: Baidu
- **Institution**: Baidu
- **Link**: [2602.01865](https://arxiv.org/abs/2602.01865)
- **Key Innovation**: Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics + action signals. Monotonic AUC improvement with model capacity and sequence length. +3.49% CTR, +3.05% CPM online. Fully deployed on Baidu.
- **Tags**: `ctr`, `generative-ranking`, `baidu`, `scaling`

### 4.8 GR4AD: Generative Recommendation for Large-Scale Advertising
- **Authors**: Kuaishou
- **Institution**: Kuaishou
- **Link**: [2602.22732](https://arxiv.org/abs/2602.22732)
- **Key Innovation**: Production GR with UA-SID (MLLM-based Unified Ad SID), LazyAR (lazy autoregressive decoder for multi-candidate generation), VSL+RSPO (ranking-aware list-wise RL). Up to 4.2% ad revenue improvement. Deployed on Kuaishou with 400M+ users.
- **Tags**: `generative-recommendation`, `advertising`, `kuaishou`, `production`

### 4.9 LLM-HYPER: Generative CTR Modeling for Cold-Start via LLM Hypernetworks
- **Authors**: Independent
- **Institution**: Industrial (top US e-commerce)
- **Link**: [2604.12096](https://arxiv.org/abs/2604.12096)
- **Key Innovation**: LLM as hypernetwork generating CTR estimator weights via few-shot CoT on multimodal ad content + CLIP retrieval. +55.9% NDCG@10 over cold-start baselines. Matches warm-start LR performance (p=0.62). Deployed in production.
- **Tags**: `cold-start`, `ctr`, `llm-hypernetwork`, `e-commerce`

### 4.10 SparseCTR: Sparse Attention on Long-term Behaviors for CTR
- **Authors**: laiweijiang
- **Institution**: Academic/Industrial
- **Link**: [2601.17836](https://arxiv.org/abs/2601.17836)
- **Key Innovation**: Personalized chunking + three-branch sparse self-attention (global interests, transitions, short-term) + composite relative temporal encoding. Scales across 3 OOM FLOPs. +1.72% CTR, +1.41% CPM online.
- **Tags**: `ctr`, `sparse-attention`, `long-behavior`, `scaling`

---

## 5. Games, RL & Agents

### 5.1 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2605.00347](https://arxiv.org/abs/2605.00347)
- **Key Innovation**: PPO with lightweight turn-level critic for Super Mario Land (100+ turn horizon). Beats GRPO/Reinforce++ in stability and efficiency. Pretrained VLMs provide strong action priors. 3× average game progress vs frontier models.
- **Tags**: `vlm`, `rl`, `games`, `long-horizon`

### 5.2 SeeUPO: Sequence-Level Agentic-RL with Convergence Guarantees
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2602.06554](https://arxiv.org/abs/2602.06554)
- **Key Innovation**: Critic-free multi-turn RL via sequential multi-agent bandit formulation + reverse-order policy updates (T→1). Monotonic improvement guarantees via backward induction.
- **Tags**: `agentic-rl`, `multi-turn`, `theory`, `convergence`

### 5.3 T-STAR: Tree-Structured Self-Taught Agent Rectification
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2604.07165](https://arxiv.org/abs/2604.07165)
- **Key Innovation**: Consolidates RL trajectories into Cognitive Tree, merges functionally similar steps. Enables In-Context Thought Grafting (contrasting successful/failed branches) + Surgical Policy Optimization (Bradley-Terry loss at critical steps). Outperforms GRPO on embodied/interactive/reasoning tasks.
- **Tags**: `agent-rl`, `tree-search`, `reasoning`, `self-rectification`

### 5.4 MemoPilot: Enhancing Test-Time Learning via RL over Memory
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2606.08656](https://arxiv.org/abs/2606.08656)
- **Key Innovation**: Trains memory update process for frozen LLM via multi-turn GRPO. Turn-wise reward + context-independent advantage estimation. #1 Elo in Limit Texas Hold'em (1762) and RPS (1590), beating DeepSeek-V3.2 and all baselines.
- **Tags**: `test-time-learning`, `memory`, `multi-turn-rl`, `games`

### 5.5 KLENT: Resource-Efficient Model-Free RL for Board Games
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2602.10894](https://arxiv.org/abs/2602.10894)
- **Key Innovation**: Model-free policy optimization (KL + entropy regularization + λ-returns) that eliminates search during training. Tested on 5 board games (Animal Shogi, Gardner Chess, Go, Hex, Othello). Competitive with search-based methods at fraction of compute.
- **Tags**: `board-games`, `model-free-rl`, `efficiency`

### 5.6 SPPO: Sequence-Level PPO for Long-Horizon Reasoning
- **Authors**: SUSTech NLP
- **Institution**: Academic (SUSTech)
- **Link**: [2604.08865](https://arxiv.org/abs/2604.08865)
- **Key Innovation**: Reformulates reasoning as sequence-level contextual bandit (collapses time horizon). Learned scalar value function avoids high variance of GRPO baselines. Matches GRPO peak with 5.9× training speedup. Decoupled critic (1.5B critic, 7B policy).
- **Tags**: `ppo`, `reasoning`, `reinforcement-learning`, `efficiency`

### 5.7 GIFT: Games as Informal Training for Generalizable LLMs
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2601.05633](https://arxiv.org/abs/2601.05633)
- **Key Innovation**: GRPO-based training across Matrix Games, TicTacToe, and Who's the Spy. Nested Training Framework (sequential "AND" composition instead of naive task mixing). Games cultivate strategic creativity and social reasoning that transfer to broad benchmarks.
- **Tags**: `games`, `informal-learning`, `generalization`, `grpo`

### 5.8 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **Authors**: spiral-rl
- **Institution**: Academic
- **Link**: [2506.24119](https://arxiv.org/abs/2506.24119)
- **Key Innovation**: Self-play on zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) via multi-agent multi-turn RL. Role-conditioned advantage estimation (RAE) stabilizes training. Up to 10% improvement on 8 reasoning benchmarks across Qwen and Llama families. Benefits even DeepSeek-R1-Distill.
- **Tags**: `self-play`, `zero-sum-games`, `reasoning`, `multi-agent`

### 5.9 LLM-as-Environment-Engineer: From Trainee to Trainer
- **Authors**: Chao Chen et al.
- **Institution**: Academic
- **Link**: [2606.17682](https://arxiv.org/abs/2606.17682)
- **Key Innovation**: Current RL policy analyzes failure trajectories and proposes next-stage environment config. Qwen3-4B outperforms larger proprietary LLMs as environment engineer. Policy learning improves self-diagnosis ability.
- **Tags**: `rl`, `environment-design`, `llm-agent`, `meta-learning`

### 5.10 Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: A. Sestini et al.
- **Institution**: EA Sports / Academic
- **Link**: [2606.20210](https://arxiv.org/abs/2606.20210)
- **Key Innovation**: Framework for deploying RL-augmented game AI (NPCs). Case study on EA SPORTS FC with human-like goalkeeping via sample-efficient RL. Identifies bottlenecks in cross-genre deployment.
- **Tags**: `game-ai`, `reinforcement-learning`, `npc`, `video-games`

### 5.11 PROPEL: Breaking the Solver Bottleneck — Training Task Generators at the Learnable Frontier
- **Authors**: Independent
- **Institution**: Academic
- **Link**: [2606.18284](https://arxiv.org/abs/2606.18284)
- **Key Innovation**: Activation probe predicts solver pass rate from frozen generator (one forward pass), replacing expensive solver rollouts during generator training. 2× rate of learnable-frontier tasks across math/code/SWE. Reduces solver trials by >50%.
- **Tags**: `task-generation`, `rl`, `solver-amortization`, `swe`

---

## Quick Stats

| Category | Papers |
|----------|--------|
| LLM Training/Optimization/Scaling | 7 |
| LLM Architectures & Attention | 7 |
| Recommendation Systems | 10 |
| CTR Prediction & Advertising | 10 |
| Games, RL & Agents | 11 |
| **Total** | **45** |

Notable trends:
- **Generative recommendation** has fully matured — nearly every major platform (Baidu, Tencent, Kuaishou, LinkedIn, Xiaohongshu) has deployed GR-based systems for ads or content recommendation.
- **Semantic IDs (SIDs)** are the dominant tokenization for GR, with work on reasoning over SIDs, implicit reasoning (PauseRec), and item-level scoring (Gryphon).
- **Scaling laws** for recommendation are emerging — both synthetic data approaches (Principled Synthetic Data) and architectural scaling (DeRes, SparseCTR, GRAB) demonstrate predictable scaling.
- **Hybrid attention** is a hot area — head-level hybridization (HydraHead), sparse attention (MSA, SparDA), layerwise recurrence (Recurrent Transformer), and associative memory (PCAF).
- **Multi-turn RL for LLMs** is thriving — self-play (SPIRAL), test-time learning (MemoPilot), tree-structured credit assignment (T-STAR), and sequence-level formulations (SPPO, SeeUPO) are pushing beyond GRPO.
- **Cold-start CTR** gets LLM-powered solutions from Xiaohongshu (IDProxy) and top US e-commerce (LLM-HYPER).
- **CTR architectures** are converging on decoder-only transformers (CADET, GRAB) with generative elements, replacing traditional DLRM ensembles.
