---
title: arXiv Daily — AI Research Survey (June 8, 2026)
type: synthesis
created: 2026-06-08
updated: 2026-06-08
sources: []
tags: [arxiv-daily, ai, llm, ctr, recommendation, sequential-modeling, moe, games]
---

# arXiv Daily — AI Research Survey

> Date: 2026-06-08 (Sun)
> Coverage: ~35 papers across LLM, CTR prediction, recommendation systems, games/agents, MoE

---

## Large Language Models

### 1. Generative Criticality in Large Language Model Temperature Scaling
- **Link**: [arxiv.org/html/2606.06238](https://arxiv.org/html/2606.06238)
- **Authors**: N/A (Qwen3 family, 0.6B–32B)
- **Key Innovation**: Proposes a statistical-field framework treating token embeddings as continuous spin variables. Finds a sharp susceptibility peak near characteristic temperature T_c ≈ 1.4 with power-law scaling, suggesting a phase-transition-like phenomenon in LLM decoding.
- **Highlights**: Robust across model scales (Qwen3 0.6B–32B) and prompt categories. Intrinsic dimension estimated by TwoNN method reaches a minimum near T_c.
- **Tags**: `LLM` `temperature-scaling` `statistical-physics` `critical-phenomena`

### 2. LLM Self-Recognition: Steering and Retrieving Activation Signatures
- **Link**: [arxiv.org/html/2606.06315](https://arxiv.org/html/2606.06315)
- **Authors**: Thibaud Ardoin et al.
- **Key Innovation**: Demonstrates reliable self-recognition of LLM outputs via internal activation signatures. Introduces steering-based watermarking by injecting random sparse vectors into the residual stream, achieving >98% attribution accuracy across multiple detection settings.
- **Highlights**: Works on Llama-3.1-8B, Ministral-3-8B; no quality degradation. Enables multi-model attribution.
- **Tags**: `LLM` `watermarking` `attribution` `interpretability` `AI-safety`

### 3. FLARE: Diffusion for Hybrid Language Model
- **Link**: [arxiv.org/pdf/2606.01774](https://arxiv.org/pdf/2606.01774)
- **Authors**: Yuchen Zhu, Jing Shi, Chongjian Ge, Hao Tan, Yiran Xu, Wanrong Zhu, Jason Kuen, Koustava Goswami, Rajiv Jain, Yongxin Chen, Molei Tao, Jiuxiang Gu
- **Key Innovation**: Converts hybrid-attention (softmax + linear) AR LLMs into diffusion LLMs (dLLMs). Identifies transfer-data quality as dominant factor for preserving AR capability. Builds unified inference system supporting both AR verified decoding and diffusion parallel denoising.
- **Highlights**: FLARE-2B/4B/9B competitive dLLM quality. Hardware-aware linear attention for diffusion visibility patterns. One checkpoint supports two generation regimes.
- **Tags**: `LLM` `diffusion` `hybrid-attention` `inference-efficiency` `dLLM`

### 4. Entropy Gate: Entropy Quenching for Near-Lossless Token Compression in LLM Pipelines
- **Link**: [arxiv.org/html/2606.03739](https://arxiv.org/html/2606.03739)
- **Authors**: N/A
- **Key Innovation**: Token compression via entropy quenching — a thermodynamic process freezing out low-energy tokens. Achieves 40–60% compression while maintaining semantic fidelity S_E > 0.80. Provides mathematical guarantee (S_E ≥ θ) that compressed prompts preserve information energy.
- **Highlights**: Stateless, model-agnostic, deploys as OpenAI-compatible HTTP proxy, 88–96% compression for agentic workloads combined with external memory.
- **Tags**: `LLM` `token-compression` `prompt-optimization` `inference-efficiency`

### 5. Enhancing LLM Metacognition via Cognitive Pairwise Training
- **Link**: [arxiv.org/html/2606.00869](https://arxiv.org/html/2606.00869)
- **Authors**: Weitao Li, Hao Zhou, Xuanyu Lei, Fandong Meng, Yuanhang Liu, Jingyi Ren, Ante Wang, Xiaolong Wang, Yuanchi Zhang, Fuwen Luo, Guangwen Yang, Lin Gan, Weizhi Ma, Yang Liu (Tsinghua University)
- **Key Innovation**: Cognitive Pairwise Training (CPT) — a mid-training stage that teaches LLMs to compare reasoning traces and internalize a reasoning-quality discrimination boundary. CPT+RL at 14B outperforms SFT+RL by +2.2 math-average and +5.2 abstention-F1.
- **Highlights**: Works across Qwen3, LLaMA, Olmo from 3B–32B. Improves math–metacognition tradeoff. Generalizes to RAG-style uncertainty handling.
- **Tags**: `LLM` `metacognition` `reasoning` `RL` `alignment`

### 6. Linguistic Productivity in LLMs: Models Coerce, but do not Preempt
- **Link**: [arxiv.org/html/2606.02953](https://arxiv.org/html/2606.02953)
- **Authors**: N/A
- **Key Innovation**: Tests usage-based linguistic theories (entrenchment vs. preemption) in LLMs. Models successfully generalize from positive evidence (coercion) but fail to use negative evidence (preemption) to constrain overgeneralization.
- **Highlights**: Even large models (Qwen3-32B, GPT-4o-mini) do not deploy negative evidence like humans. Points to a fundamental generalization gap.
- **Tags**: `LLM` `linguistics` `productivity` `cognitive-science` `generalization`

### 7. Negligible in Size, Significant in Effect: On Scale Vectors in Large Language Models
- **Link**: [arxiv.org/html/2605.26895](https://arxiv.org/html/2605.26895)
- **Authors**: N/A
- **Key Innovation**: Systematic study of normalization scale vectors in LLMs. Shows they improve optimization (not expressivity) via self-amplifying preconditioning. Proposes branch-specific heterogeneity, improved placement, and magnitude-direction reparameterization.
- **Highlights**: Experiments on dense and MoE models 0.12B–2B. Lower terminal loss than well-tuned baselines across AdamW and Muon optimizers.
- **Tags**: `LLM` `normalization` `scale-vectors` `optimization` `pre-training`

### 8. Mimir: Large-scale Multilingual Concept Modeling
- **Link**: [arxiv.org/html/2605.25263](https://arxiv.org/html/2605.25263)
- **Authors**: N/A
- **Key Innovation**: First Large Concept Model trained on multilingual data. 1.6B model trained on 38.9B sentences across 46 languages, instruction-tuned on 66.8M sentences across 35 languages. Uses sentence-level "concept" representations instead of tokens.
- **Highlights**: Leverages SONAR sentence embeddings. Inherently multilingual generation via shared concept space with per-language decoders.
- **Tags**: `LLM` `concept-modeling` `multilingual` `LCM`

### 9. Chatbots Output Meaningful (but Problematic) Language
- **Link**: [arxiv.org/html/2606.02973](https://arxiv.org/html/2606.02973)
- **Authors**: N/A (NSF-funded)
- **Key Innovation**: Philosophical argument that LLM outputs are meaningful under existing theories of human language meaning. Argues against intentionalist accounts that deny meaning to AI outputs.
- **Highlights**: Proposes that meaning is a low bar — does not require mental states or intentions. LLMs acquire lexical items mechanistically through exposure.
- **Tags**: `LLM` `philosophy-of-language` `meaning` `semantics`

---

## CTR Prediction & Recommender Systems (Industrial)

### 10. Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)
- **Link**: [arxiv.org/html/2606.04944](https://arxiv.org/html/2606.04944)
- **Authors**: RUCAIBox
- **Key Innovation**: Uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP, while a parallel MLP captures implicit interactions. Achieves SOTA with only vanilla MLP structure.
- **Highlights**: SOTA across Criteo, Avazu, Movielens. Low latency comparable to efficient baselines. Code available.
- **Tags**: `CTR` `recommender-system` `knowledge-distillation` `MLP`

### 11. HeMix: Query-Mixed Interest Extraction and Heterogeneous Interaction
- **Link**: [arxiv.org/pdf/2602.09387](https://arxiv.org/pdf/2602.09387)
- **Authors**: Fangye Wang, Guowei Yang et al.
- **Key Innovation**: Scalable CTR model unifying adaptive sequence tokenization (Query-Mixed Interest Extraction) and heterogeneous interaction (HeteroMixer block). Deployed on AMAP (AutoNavi).
- **Highlights**: +3.61% GMV, +2.78% PV_CTR, +2.12% UV_CVR over DLRM in online A/B test. Favorable scaling behavior.
- **Tags**: `CTR` `recommender-system` `industrial` `location-based` `AMAP`

### 12. LoopCTR: Loop Scaling Paradigm for CTR Prediction
- **Link**: [arxiv.org/pdf/2604.19550](https://arxiv.org/pdf/2604.19550)
- **Authors**: N/A
- **Key Innovation**: Introduces loop scaling — recursive reuse of shared model layers decouples computation from parameter growth. Train-multi-loop, infer-zero-loop strategy achieves SOTA with substantially lower inference cost.
- **Highlights**: Sandwich architecture (Entry/Loop/Exit Block) with Hyper-Connected Residuals and MoE. Oracle analysis reveals 0.02–0.04 AUC headroom. Zero-loop inference already outperforms all baselines.
- **Tags**: `CTR` `scaling` `loop` `parameter-efficiency` `recursive`

### 13. HyFormer: Unifying Sequence Modeling and Feature Interaction in CTR
- **Link**: [arxiv.org/pdf/2601.12681](https://arxiv.org/pdf/2601.12681)
- **Authors**: ByteDance (Douyin Search)
- **Key Innovation**: Hybrid transformer with Global Tokens serving as shared semantic interface between long behavior sequences and heterogeneous features. Alternates between Query Decoding and Query Boosting.
- **Highlights**: Deployed on billion-scale Douyin Search. Outperforms LONGER + RankMixer baselines. Superior scaling behavior. Online A/B test validated.
- **Tags**: `CTR` `recommender-system` `sequence-modeling` `feature-interaction` `ByteDance`

### 14. EST: Efficiently Scalable Transformer for CTR Prediction
- **Link**: [arxiv.org/pdf/2602.10811](https://arxiv.org/pdf/2602.10811)
- **Authors**: Taobao (Alibaba)
- **Key Innovation**: Unified modeling of all CTR inputs in single sequence without prior aggregation. Lightweight Cross-Attention (LCA) prunes redundant self-interactions; Content Sparse Attention (CSA) leverages content similarity.
- **Highlights**: Deployed on Taobao display advertising. +3.27% RPM, +1.22% CTR online. Exhibits stable power-law scaling.
- **Tags**: `CTR` `scaling` `transformer` `industrial` `Taobao`

### 15. FEDIN: Frequency-Enhanced Deep Interest Network for CTR Prediction
- **Link**: [arxiv.org/html/2605.01726](https://arxiv.org/html/2605.01726)
- **Authors**: N/A (SIGIR 2026)
- **Key Innovation**: Discovers distinct spectral entropy distributions in attention scores conditioned on positive vs. negative items. Introduces target-aware spectrum filtering in frequency domain branch alongside time-domain modeling.
- **Highlights**: Dual-branch architecture (frequency + time). SOTA on Tmall, Taobao, Alipay datasets. Robust to noise.
- **Tags**: `CTR` `frequency-domain` `sequential-recommendation` `SIGIR26`

### 16. CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer
- **Link**: [arxiv.org/html/2602.11410](https://arxiv.org/html/2602.11410)
- **Authors**: LinkedIn
- **Key Innovation**: End-to-end decoder-only transformer for ads CTR. Context-conditioned decoding with multi-tower prediction heads resolving the chicken-and-egg problem between pCTR and ad position. Self-gated attention, timestamp-based RoPE.
- **Highlights**: +11.04% CTR lift over LiRank (DCNv2 + sequential encoder). Deployed on LinkedIn's main sponsored feed traffic.
- **Tags**: `CTR` `advertising` `decoder-only` `transformer` `LinkedIn`

---

## Sequential Recommendation

### 17. MLTFR: Multi-LLM Token Filtering and Routing for Sequential Recommendation
- **Link**: [arxiv.org/abs/2604.18200](https://arxiv.org/abs/2604.18200)
- **Authors**: N/A
- **Key Innovation**: Uses LLM token embeddings directly (no textual input) for sequential recommendation. Multi-LLM token filtering + Mixture-of-Experts routing with Fisher-weighted semantic consensus.
- **Highlights**: Addresses semantic misalignment, insufficient task adaptation, and limited coverage of single-LLM representations. Corpus-free (no external text needed).
- **Tags**: `sequential-recommendation` `LLM` `MoE` `token-embedding`

### 18. HyTRec: Hybrid Temporal-Aware Attention for Long Behavior Sequential Recommendation
- **Link**: [arxiv.org/pdf/2602.18283](https://arxiv.org/pdf/2602.18283)
- **Authors**: N/A
- **Key Innovation**: Hybrid attention — linear attention backbone with strategically placed softmax attention layers (7:1 ratio) for high-fidelity retrieval. Temporal-Aware Delta Network (TADN) for rapid interest drift capture.
- **Highlights**: Near-linear complexity. Handles 10K+ interaction sequences. Outperforms pure linear and pure softmax approaches.
- **Tags**: `sequential-recommendation` `hybrid-attention` `temporal-modeling` `efficiency`

### 19. GrIT: Group Informed Transformer for Sequential Recommendation
- **Link**: [arxiv.org/pdf/2602.19728](https://arxiv.org/pdf/2602.19728)
- **Authors**: N/A
- **Key Innovation**: Models temporally evolving group features alongside individual histories. Learnable time-varying membership weights for latent groups derived from short/long-term interaction features.
- **Highlights**: Group representations fused with sequential representations in transformer blocks. Evaluated on 5 benchmarks, consistently outperforms SOTA.
- **Tags**: `sequential-recommendation` `group-modeling` `transformers` `temporal-dynamics`

### 20. CREATE: Cross-Representation Knowledge Transfer for Sequential Recommendation
- **Link**: [arxiv.org/pdf/2602.23471](https://arxiv.org/pdf/2602.23471)
- **Authors**: Gimranov et al. (KDD 2026)
- **Key Innovation**: Combines transformer (sequential) and GNN (graph) encoders with Barlow Twins representation alignment. Graph encoder enriches sequential model with global interaction patterns.
- **Highlights**: Consistent gains across 5 datasets. No user embeddings needed at inference. Redundancy reduction via alignment.
- **Tags**: `sequential-recommendation` `GNN` `transformer` `representation-learning` `KDD26`

### 21. FLAME: Condensing Ensemble Diversity into a Single Network
- **Link**: [arxiv.org/html/2604.04038](https://arxiv.org/html/2604.04038)
- **Authors**: N/A
- **Key Innovation**: Modular ensemble using 2 networks (one frozen, one learnable) to simulate exponential diversity (2^M combinations). Guided mutual learning for stable training. Single-network inference.
- **Highlights**: Up to 7.69× faster convergence, 9.70% improvement in NDCG@20. Architecture-agnostic (works with GRU4Rec, Caser, FMLPRec, SASRec).
- **Tags**: `sequential-recommendation` `ensemble` `knowledge-distillation` `efficiency`

### 22. SpecTran: Spectral-Aware Transformer-based Adapter for LLM-Enhanced SR
- **Link**: [arxiv.org/html/2601.21986](https://arxiv.org/html/2601.21986)
- **Authors**: N/A
- **Key Innovation**: Spectral-domain adapter that attends over the full spectrum of LLM item embeddings. Learnable spectral-positional encoding injects singular-value cues as inductive bias.
- **Highlights**: Overcomes dimension collapse of adapter-based methods and rigidity of SVD-based methods. Avg 9.17% improvement across 4 datasets and 3 SR backbones.
- **Tags**: `sequential-recommendation` `LLM` `spectral-analysis` `adapter`

### 23. ManCAR: Manifold-Constrained Latent Reasoning for Sequential Recommendation
- **Link**: [arxiv.org/pdf/2602.20093](https://arxiv.org/pdf/2602.20093)
- **Authors**: N/A
- **Key Innovation**: Grounds latent reasoning within the topology of a global interaction graph. Restricts reasoning trajectories to collaboratively reachable regions. Adaptive test-time stopping.
- **Highlights**: Up to 46.88% relative improvement in NDCG@10. Variational interpretation with ELBO-like objective preventing latent drift.
- **Tags**: `sequential-recommendation` `latent-reasoning` `manifold` `test-time-computation`

---

## Games, Agents & Reinforcement Learning

### 24. Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **Link**: [arxiv.org/pdf/2604.17696](https://arxiv.org/pdf/2604.17696)
- **Authors**: N/A
- **Key Innovation**: Extends SPIRAL self-play framework. Introduces Reasoning Transferability Coefficient (φ) to select domain-agnostic trajectories and Reasoning Evolution Reward (ψ) for adaptive reasoning development.
- **Highlights**: Strong gains on competition-level mathematics with Qwen3-4B. Ablation and human evaluation confirm transferable reasoning improvement.
- **Tags**: `games` `self-play` `reasoning` `reinforcement-learning` `transfer`

### 25. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **Link**: [arxiv.org/abs/2506.24119](https://arxiv.org/abs/2506.24119)
- **Authors**: N/A
- **Key Innovation**: Fully online, multi-turn, multi-agent RL for LLMs via self-play on zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation). Role-conditioned advantage estimation (RAE) stabilizes multi-agent training.
- **Highlights**: Up to 10% improvement across 8 reasoning benchmarks (MATH500, AIME24/25, GPQA, etc.) on Qwen3-4B/8B, Llama-3.1-8B. Multi-game training yields strongest results.
- **Tags**: `games` `self-play` `RL` `reasoning` `multi-agent`

### 26. ProAct: Agentic Lookahead in Interactive Environments
- **Link**: [arxiv.org/pdf/2602.05327](https://arxiv.org/pdf/2602.05327)
- **Authors**: N/A
- **Key Innovation**: Grounded LookAhead Distillation (GLAD) — compresses MCTS trajectories into concise reasoning chains for SFT. Monte-Carlo Critic (MC-Critic) provides low-variance value estimates for PPO/GRPO.
- **Highlights**: 4B model outperforms all open-source baselines on 2048 and Sokoban. Rivals closed-source models. Strong generalization to unseen environments.
- **Tags**: `agents` `lookahead` `MCTS` `RL` `planning`

### 27. SeeUPO: Sequence-Level Agentic-RL with Convergence Guarantees
- **Link**: [arxiv.org/pdf/2602.06554](https://arxiv.org/pdf/2602.06554)
- **Authors**: N/A
- **Key Innovation**: Models multi-turn interaction as sequential multi-agent bandit problems. Reverse-order sequential policy updates (backward induction) guarantee convergence to global optimal policy.
- **Highlights**: 43.3–54.6% relative gains on Qwen3-14B for AppWorld and BFCL v4. Critic-free with monotonic improvement guarantees.
- **Tags**: `RL` `agents` `convergence` `multi-turn` `theory`

### 28. T-STAR: Tree-structured Self-Taught Agent Rectification
- **Link**: [arxiv.org/pdf/2604.07165](https://arxiv.org/pdf/2604.07165)
- **Authors**: N/A
- **Key Innovation**: Consolidates independent trajectories into a Cognitive Tree for variance-reduced advantage estimation. In-Context Thought Grafting synthesizes corrective reasoning by contrasting successful/failed branches.
- **Highlights**: Surgical Policy Optimization with Bradley-Terry loss at critical divergence points. Works with GRPO, DAPO, GiGPO.
- **Tags**: `agents` `RL` `tree-search` `credit-assignment` `self-rectification`

### 29. MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Link**: [arxiv.org/pdf/2604.05943](https://arxiv.org/pdf/2604.05943)
- **Authors**: Cognitive AI Systems
- **Key Innovation**: Single GPT-based model trained via offline imitation learning on expert trajectories (400M+ steps) across SMACv2, Google Research Football, and POGEMA. Flexible observation encoder with no task-specific tuning.
- **Highlights**: Competitive with specialized MARL baselines across all environments. Path toward generalist MARL foundation model.
- **Tags**: `MARL` `foundation-model` `multi-agent` `imitation-learning` `transformer`

### 30. SeqComm-DFL: Multi-Agent Decision-Focused Learning via Value-Aware Sequential Communication
- **Link**: [arxiv.org/pdf/2604.08944](https://arxiv.org/pdf/2604.08944)
- **Authors**: N/A
- **Key Innovation**: Unifies sequential communication with decision-focused learning. Value-aware message generation with Stackelberg conditioning. Prosocial agent ordering determines guidance potential.
- **Highlights**: 4–6× higher rewards on healthcare and SMAC benchmarks. 13% win rate improvements. O(1/√T) convergence bounds.
- **Tags**: `MARL` `communication` `decision-focused-learning` `coordination`

---

## Mixture-of-Experts

### 31. ProbMoE: Differentiable Probabilistic Routing for MoE
- **Link**: [arxiv.org/html/2606.01509](https://arxiv.org/html/2606.01509)
- **Authors**: Heng Hugo Zhao et al.
- **Key Innovation**: Casts MoE routing as probabilistic inference over cardinality-constrained expert subsets. Uses SIMPLE gradient estimator for tractable marginal-based gradients. Supports both Exact-k and Dynamic-k routing.
- **Highlights**: Improved expert utilization and routing diversity. Dynamic-k achieves competitive performance with fewer activated experts on average.
- **Tags**: `MoE` `routing` `probabilistic` `gradient-estimation` `dynamic-k`

### 32. DAG-MoE: From Simple Mixture to Structural Aggregation in MoE
- **Link**: [arxiv.org/html/2606.01062](https://arxiv.org/html/2606.01062)
- **Authors**: Jiarui Feng et al.
- **Key Innovation**: Replaces weighted-summation expert aggregation with DAG-structured aggregation. Each expert gets a distinct structural role; enables multi-step reasoning within a single MoE layer.
- **Highlights**: Expands expert combination space without modifying experts or router. Consistently outperforms standard MoE in pre-training and fine-tuning.
- **Tags**: `MoE` `aggregation` `DAG` `structural-learning` `reasoning`

### 33. Pr2: Predictive Routing Replay for MoE-Based LLM Reinforcement Learning
- **Link**: [arxiv.org/html/2606.00395](https://arxiv.org/html/2606.00395)
- **Authors**: N/A
- **Key Innovation**: Addresses router drift in MoE RL by augmenting each router with a lightweight evolution predictor. Predicts short-horizon router evolution to enable gradient flow to likely-to-be-active experts.
- **Highlights**: +12.29% on AIME24 over routing replay on Qwen3-30B-A3B. Reduces routing mismatch, stabilizes PPO training.
- **Tags**: `MoE` `RL` `router-drift` `stability` `reasoning`

### 34. UniEP: Unified Expert-Parallel MoE MegaKernel for LLM Training
- **Link**: [arxiv.org/pdf/2604.19241](https://arxiv.org/pdf/2604.19241)
- **Authors**: N/A
- **Key Innovation**: Fuses MoE communication and computation into MegaKernels. Fine-grained SM-level scheduling for computation-communication overlap. Deterministic token ordering guarantees numerical consistency.
- **Highlights**: 1.03×–1.38× speedups over COMET. 1.09× throughput gain on 128-GPU production run (138B tokens/day).
- **Tags**: `MoE` `systems` `expert-parallelism` `training` `GPU`

### 35. Holistic Scaling Laws for Optimal MoE Architecture Optimization
- **Link**: [arxiv.org/abs/2603.21862](https://arxiv.org/abs/2603.21862)
- **Authors**: Weilin Wan et al.
- **Key Innovation**: Establishes joint constraint triad (FLOPs/token, active params, total params) for MoE. Reduces 16D search space to two sequential low-dimensional phases with algebraic constraints.
- **Highlights**: Validated across hundreds of MoE models spanning 6 orders of compute magnitude. Near-optimal configuration band widens with scale.
- **Tags**: `MoE` `scaling-laws` `architecture-search` `theory`

### 36. Optimal Expert-Attention Allocation in MoE: A Scalable Law
- **Link**: [arxiv.org/pdf/2603.10379](https://arxiv.org/pdf/2603.10379)
- **Authors**: N/A
- **Key Innovation**: Extends Chinchilla scaling laws to MoE by incorporating expert–attention FLOPs allocation ratio. Shows optimal ratio follows power-law with total compute and varies with sparsity.
- **Highlights**: Explicit formula for optimal FLOPs ratio r*. Lower sparsity favors expert-heavy; higher sparsity favors more attention capacity.
- **Tags**: `MoE` `scaling-laws` `compute-allocation` `Chinchilla`

### 37. Grouter: Decoupling Routing from Representation for Accelerated MoE Training
- **Link**: [arxiv.org/pdf/2603.06626](https://arxiv.org/pdf/2603.06626)
- **Authors**: N/A
- **Key Innovation**: Distills high-quality routing structure from fully-trained MoE models and serves as fixed router. Decouples structural optimization from weight updates.
- **Highlights**: 4.28× data utilization improvement. 33.5% throughput acceleration. Expert Folding for cross-configuration adaptation.
- **Tags**: `MoE` `routing` `distillation` `training-acceleration` `Megatron`

---

## Meta

- **Search date**: 2026-06-08
- **Sources searched**: arXiv (via web search)
- **Categories covered**: cs.LG, cs.IR, cs.AI, cs.CL, cs.MA
- **Papers highlighted**: 37
