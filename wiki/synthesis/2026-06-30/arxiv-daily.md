---
title: "arXiv Daily Scan — June 30, 2026"
type: synthesis
created: 2026-06-30
updated: 2026-06-30
tags: [arxiv, survey, llm, ctr, recommendation, games, rl, sequence-modeling, attention, advertising]
---

# arXiv Daily Scan — June 30, 2026

> Papers from Jun 24–30, 2026 across cs.AI, cs.LG, cs.IR, cs.MA, cs.GT, cs.CL.

---

## LLMs & Foundation Models

### Self-Compacting Language Model Agents
- **Authors**: Tianjian Li et al.
- **Institution**: —
- **Link**: [arXiv:2606.23525](https://arxiv.org/abs/2606.23525)
- **Abstract**: Proposes SelfCompact — a scaffold allowing the model to decide when/how to compact long agent traces via a compaction tool + lightweight rubric. Matches/exceeds fixed-interval summarization at 30-70% lower token cost.
- **Key Innovations**: Model-invoked context compaction; rubric prevents compaction at harmful moments; meta-cognitive gap analysis.

### Reasoning Quality Emerges Early: Data Curation for Reasoning Models
- **Authors**: Hongyi Henry Jin, Wenhan Yang, Meysam Ghaffari, Carlos Morato, Baharan Mirzasoleiman
- **Institution**: —
- **Link**: [arXiv:2606.26797](https://arxiv.org/abs/2606.26797)
- **Abstract**: Shows diverse/challenging reasoning examples can be identified using only the first ~100 reasoning tokens' loss at a randomly perturbed checkpoint. Outperforms baselines by 1.7% while being 91% more token efficient.
- **Key Innovations**: Early-token loss as difficulty detector; gradient-similarity based curation; no strong reasoning model needed for filtering.

### On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
- **Authors**: Andrei Nicolicioiu et al.
- **Institution**: —
- **Link**: [arXiv:2606.26091](https://arxiv.org/abs/2606.26091)
- **Abstract**: Shows on-policy self-distillation achieves strong pass@1 but at cost of rollout diversity — pass@k curves flatten. Theoretical analysis: self-distillation tilts distribution by mutual information score, amplifying existing probability gaps unlike optimal RL.
- **Key Innovations**: Identifies hidden diversity cost of self-distillation; theoretical characterization of distributional bias.

### KARLA: Knowledge-base Augmented Retrieval for Language Models
- **Authors**: Francois Crespin et al.
- **Institution**: —
- **Link**: [arXiv:2606.26807](https://arxiv.org/abs/2606.26807)
- **Abstract**: Trains LLM to produce special tokens triggering knowledge base queries during generation. Factual knowledge can be updated via KB edits without retraining; smaller models match larger ones in factual accuracy.
- **Key Innovations**: Special tokens as KB query triggers; fact tracing to KB for transparency; decoupled factual updates.

### Multilingual Reasoning Cascades Need More Context
- **Authors**: Arnav Mazumder, Dengjia Zhang, Shuyue Stella Li, Yulia Tsvetkov, Niyati Bafna
- **Institution**: —
- **Link**: [arXiv:2606.27306](https://arxiv.org/abs/2606.27306)
- **Abstract**: Training-free intervention for translation cascade reasoning: providing original+translated question + reasoning trace to final translation module. Strong gains across 9 benchmarks, 285 languages. Original language question carries most beneficial context.
- **Key Innovations**: Context-aware translation cascade; identifies original-question preservation as key design principle.

### From Reasoning Traces to Reusable Modules: Understanding Compositional Generalization in Language Model Reasoning
- **Authors**: —
- **Institution**: —
- **Link**: [arXiv:2606.18089](https://arxiv.org/abs/2606.18089)
- **Abstract**: Formalizes compositional generalization via hierarchical latent selection model. Theoretically shows SFT supplies raw module materials; RL decomposes traces to identify atomic modules and recombine for new configurations.
- **Key Innovations**: Formal theory of SFT+RL complementarity for reasoning; atomic module identification theory; effective data-pairing protocol.

### Can Reasoning Models Detect Changes to their Chains of Thought?
- **Authors**: Sathvik Napa, Utkarsh Singh, Chengyuan Xue, Miriam Wanner et al.
- **Institution**: —
- **Link**: [arXiv:2606.22085](https://arxiv.org/abs/2606.22085)
- **Abstract**: Studies whether reasoning models detect interventions on their CoTs. Models exhibit only modest detection accuracy; struggle to identify *how* CoT was modified; as good at detecting changes to own CoTs as to other models'.
- **Key Innovations**: First systematic study of CoT tampering detection; implications for CoT prefilling and safety.

### Multi-Turn Memory-Augmented Test-Time Learning via RL (MemoPilot)
- **Authors**: —
- **Institution**: —
- **Link**: [arXiv:2606.08656](https://arxiv.org/abs/2606.08656)
- **Abstract**: MemoPilot trains memory update process via multi-turn GRPO for frozen LLMs in sequential games (Rock-Paper-Scissors, Limit Texas Hold'em). Achieves Elo 1762 (LHE) and 1590 (RPS), outperforming DeepSeek-V3.2.
- **Key Innovations**: Turn-wise reward + context-independent turn-level advantage estimation for multi-turn RL; plug-in memory copilot for frozen models.

### RaDaR: Specialized Reasoning LLM for Rare Disease Diagnosis
- **Authors**: Haichao Chen et al.
- **Institution**: —
- **Link**: [arXiv:2606.24510](https://arxiv.org/abs/2606.24510)
- **Abstract**: Open-source 32B reasoning LLM for rare disease diagnosis. Trained on 49K public cases + 104K synthetic cases. Outperforms DeepSeek-R1 (671B). In randomized trial, improved physician diagnostic accuracy by 21.44pp. 61% of diagnoses prioritized before clinical suspicion.
- **Key Innovations**: Phenotype-anchored synthetic narratives scaling; physician-assistance trial validation; potential 1.87-month lead time.

---

## Reasoning & Inference

### GraphPO: Graph-based Policy Optimization for Reasoning Models
- **Authors**: —
- **Institution**: —
- **Link**: [arXiv:2606.18954](https://arxiv.org/abs/2606.18954)
- **Abstract**: Represents RL rollouts as DAG with reasoning steps as edges, semantic states as nodes. Merges semantically equivalent paths, assigns efficiency/correctness advantages. Reduces advantage-estimation variance and improves reasoning efficiency.
- **Key Innovations**: Graph-structured rollouts (vs chain/tree); semantic equivalence merging; dual advantage (efficiency + correctness).

### ReasoningLens: Hierarchical Visualization and Diagnostic Auditing for Large Reasoning Models
- **Authors**: Jiasheng Zheng et al.
- **Institution**: —
- **Link**: [arXiv:2606.23404](https://arxiv.org/abs/2606.23404)
- **Abstract**: Open-source framework for hierarchical visualization of long CoT traces. Structures traces into interactive hierarchies (high-level strategy vs low-level execution); agentic auditor for automated error detection; systemic reasoning profiles.
- **Key Innovations**: Trace-to-hierarchy transformation; automated error detection via tool-augmented verification; model-specific blind spot profiling.

### Reasoning Structure of Large Language Models
- **Authors**: Frédéric Berdoz, Luca A. Lanzendörfer, Fabian Farestam, Roger Wattenhofer
- **Institution**: ETH Zurich
- **Link**: [arXiv:2606.03883](https://arxiv.org/abs/2606.03883)
- **Abstract**: Introduces scalable benchmark of logic puzzles + pipeline converting unstructured traces into verifiable reasoning graphs. Defines reasoning efficiency metric measuring concentration of logical flow. Structural measurements separate behaviors token count/accuracy conflate.
- **Key Innovations**: Reasoning-as-graph representation; reasoning efficiency metric; diagnostic tool for failure modes.

### ForEx: Formal Verification Framework for Explainable Reasoning
- **Authors**: Yihuang Kang et al.
- **Institution**: —
- **Link**: [arXiv:2606.21867](https://arxiv.org/abs/2606.21867)
- **Abstract**: Translates LLM-generated explanations into Lean4 for formal verification. Introduces LLM Argument Verification Matrix separating label consistency from formal verification. Over 90% of outputs pass verification but human agreement only ~20%.
- **Key Innovations**: Formal verification of LLM reasoning chains in Lean4; reveals gap between formal derivability and label agreement.

---

## Sequence Modeling & Attention

### ATMA: Length-Invariant Language Modeling via Polar Attention and Gated-Delta Compression Memory
- **Authors**: —
- **Institution**: Kreasof AI
- **Link**: [arXiv:2606.25156](https://arxiv.org/abs/2606.25156)
- **Abstract**: Three-channel attention: count-blind direction channel, bounded magnitude channel (participation ratio over null sink), gated-delta recurrent memory. Maintains 90%+ NIAH retrieval at 64K tokens (32× training length). Monotonic perplexity reduction.
- **Key Innovations**: Polar attention solves softmax dilution; three-channel factorization; gated-delta fast-weight memory.

### MiniMax Sparse Attention (MSA)
- **Authors**: MiniMax AI
- **Institution**: MiniMax
- **Link**: [arXiv:2606.13392](https://arxiv.org/abs/2606.13392)
- **Abstract**: Blockwise sparse attention with lightweight Index Branch for Top-K block selection per GQA group + exp-free kernel. On 109B MoE model: 28.4× attention compute reduction at 1M context; 14.2× prefill and 7.6× decode speedups on H800.
- **Key Innovations**: Group-specific sparse retrieval; exp-free Top-K; KV-outer sparse attention for tensor-core utilization; production deployment.

### HydraHead: From Head-Level Functional Heterogeneity to Specialized Attention Hybridization
- **Authors**: Zhentao Tan, Wei Chen, Jingyi Shen, Yao Liu, Xu Shen, Yue Wu, Jieping Ye
- **Institution**: —
- **Link**: [arXiv:2606.20097](https://arxiv.org/abs/2606.20097)
- **Abstract**: Hybridizes full and linear attention at head level (vs layer level). Interpretability-driven selection preserves FA only for retrieval-critical heads; scale-normalized fusion reconciles distribution gap. 7:1 LA:FA ratio matches 3:1 layer hybrid. 69% NIAH improvement at 512K with only 15B training tokens.
- **Key Innovations**: Head-level (not layer-level) hybridization; interpretability-guided head selection; three-stage transfer pipeline.

### RRAttention: Dynamic Block Sparse Attention via Per-Head Round-Robin Shifts
- **Authors**: —
- **Institution**: —
- **Link**: [arXiv:2606.27372](https://arxiv.org/abs/2606.27372) (ACL 2026)
- **Abstract**: Round-robin query sampling positions across heads within stride. Reduces complexity from O(L²) to O(L²/S²). Recovers 99%+ full attention performance at half compute; 2.4× speedup at 128K context.
- **Key Innovations**: Head round-robin sampling for global pattern discovery; query independence maintained; adaptive Top-τ selection.

### Blurry Window Attention (BLA)
- **Authors**: —
- **Institution**: —
- **Link**: [arXiv:2606.09862](https://arxiv.org/abs/2606.09862)
- **Abstract**: ABC method storing frequency window; reconstructs blurry KV history via Dirichlet kernel interpolation. 8× state efficiency vs sliding window attention on MQAR. Generalization of SWA; special case of Gated Slot Attention.
- **Key Innovations**: Dirichlet kernel-based KV interpolation; unifies ABC and SWA frameworks; frequency-domain attention state.

### Parallel Causal Associative Fields (PCAF)
- **Authors**: —
- **Institution**: Google (TPU v4-32)
- **Link**: [arXiv:2606.10435](https://arxiv.org/abs/2606.10435)
- **Abstract**: Content-addressed memory over causal successor records — writes local records into hash buckets, retrieves bounded candidate set, sparse cache distribution. 303M model: 36.31 PPL on WikiText-103 at 0.61M tok/s vs 47.49/0.43M for dense Transformer.
- **Key Innovations**: Parallel associative memory (not recurrent, not dense attention); learned gate mixing parametric + retrieved distributions.

### Superlinear Multi-Step Attention
- **Authors**: Yufeng Huang et al.
- **Institution**: —
- **Link**: [arXiv:2601.18401](https://arxiv.org/abs/2601.18401)
- **Abstract**: Multi-step attention with O(L^{1+1/N}) complexity. N=2 implementation: O(L^{3/2}) via span-search + span-attention. 114 tok/s at 1M, 80 tok/s at 10M context on 30B MoE. Strong NIAH up to 256K.
- **Key Innovations**: Sub-quadratic multi-step search formulation; structural non-exclusion of token positions; practical long-context inference at 10M.

### Sessa: Selective State Space Attention
- **Authors**: —
- **Institution**: —
- **Link**: [arXiv:2604.18580](https://arxiv.org/abs/2604.18580)
- **Abstract**: Places attention inside recurrent feedback path for power-law memory tails O(ℓ⁻ᵝ) with slower decay than Transformer/Mamba. Achieves flexible selective retrieval including non-decaying profiles.
- **Key Innovations**: Attention-in-feedback architecture; provable power-law memory; non-decaying selective retrieval.

### Towards Tight Bounds for Streaming Attention
- **Authors**: Boris Prokhorov et al.
- **Institution**: —
- **Link**: [arXiv:2606.07205](https://arxiv.org/abs/2606.07205)
- **Abstract**: Nearly tight space complexity bounds for streaming attention approximation. Uses discrepancy-based coresets + polynomial method + space partitioning. Lower bound technique via INDEX problem with side information.
- **Key Innovations**: Tight theoretical bounds for KV cache compression; multi-method algorithmic synthesis.

---

## CTR Prediction & Advertising Recommendation

### GRAB: LLM-Inspired Sequence-First CTR at Baidu
- **Authors**: Shaopeng Chen, Chuyue Xie, Huimin Ren, Shaozong Zhang, Han Zhang, Ruobing Cheng et al.
- **Institution**: Baidu
- **Link**: [arXiv:2602.01865](https://arxiv.org/abs/2602.01865)
- **Abstract**: End-to-end generative CTR framework with Causal Action-aware Multi-channel Attention (CamA). Full-scale online deployment: +3.05% revenue, +3.49% CTR. Monotonic linear scaling with longer sequences.
- **Key Innovations**: Sequence-first generative paradigm for CTR; CamA captures temporal dynamics + action signals; production scaling evidence.

### IDProxy: Cold-Start CTR at Xiaohongshu with Multimodal LLMs
- **Authors**: Guillaume Salha-Galvan et al.
- **Institution**: Xiaohongshu
- **Link**: [arXiv:2603.01590](https://arxiv.org/abs/2603.01590)
- **Abstract**: MLLM-generated proxy embeddings from content signals for cold-start items. Aligned with existing ID embedding space, optimized end-to-end. Deployed in Content Feed + Display Ads at Xiaohongshu.
- **Key Innovations**: MLLM proxy embeddings for cold-start; explicit alignment with ID embedding space; production serving at billion-user scale.

### OneRanker: Unified Generation and Ranking at Tencent Weixin
- **Authors**: —
- **Institution**: Tencent
- **Link**: [arXiv:2603.02999](https://arxiv.org/abs/2603.02999)
- **Abstract**: Architectural-level integration of generative retrieval + ranking. Value-aware multi-task decoupling; Fake Item Tokens for implicit awareness; KV pass-through consistency. Weixin deployment: GMV +1.34%.
- **Key Innovations**: Unified gen+rank architecture (not cascaded); value-aware decoupling; Fake Item Token mechanism.

### GR4AD: Generative Recommendation for Large-Scale Advertising at Kuaishou
- **Authors**: Ben Xue, Dan Liu, Lixiang Wang, Lei Meng, Peng Wang et al.
- **Institution**: Kuaishou
- **Link**: [arXiv:2602.22732](https://arxiv.org/abs/2602.22732)
- **Abstract**: Production generative recommender with UA-SID tokenization, LazyAR decoder, RSPO (ranking-guided preference optimization), dynamic beam serving. Deployed at Kuaishou (400M+ users). Up to 4.2% ad revenue improvement.
- **Key Innovations**: UA-SID semantic IDs; LazyAR for efficient short-candidate generation; dynamic beam serving adapts to traffic; full production stack.

### DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR
- **Authors**: —
- **Institution**: Major social-media platform (unnamed)
- **Link**: [arXiv:2606.07980](https://arxiv.org/abs/2606.07980)
- **Abstract**: Dual-path residual (Identity + Block Attention) with vector-wise gate; SiLU-based Pointwise AttnRes. 1.66× steeper compute-AUC scaling law than OneTrans. 8-layer DeRes matches 16-layer OneTrans at ~2× compute saving.
- **Key Innovations**: Dual-path residual design for CTR; SiLU replaces Softmax for parallel multi-interest; steeper scaling law.

### EST: Efficient Scaling Laws in CTR via Unified Modeling at Taobao
- **Authors**: Mingyang Liu, Yong Bai, Zhangming Chan et al.
- **Institution**: Alibaba (Taobao)
- **Link**: [arXiv:2602.10811](https://arxiv.org/abs/2602.10811)
- **Abstract**: Fully unified modeling without lossy aggregation. Lightweight Cross Attention (LCA) + Content Sparse Attention (CSA) for dynamic behavior selection. Stable power-law scaling. Taobao deployment: RPM +3.27%, CTR +1.22%.
- **Key Innovations**: Fully unified sequence modeling for CTR; content-similarity-based dynamic behavior selection; production scaling law validation.

### MLCC: Multi-Level Compression Cross Networks at Bilibili
- **Authors**: Jie Xia et al.
- **Institution**: Bilibili
- **Link**: [arXiv:2602.12041](https://arxiv.org/abs/2602.12041)
- **Abstract**: Hierarchical compression + dynamic composition for feature crosses. MC-MLCC extends to parallel subspaces. Up to 0.52 AUC gain with 26× parameter/FLOP reduction. Deployed in Bilibili advertising.
- **Key Innovations**: Multi-level compression crosses; efficient horizontal scaling via channel decomposition; production deployment under strict latency.

### DAIAN: Deep Adaptive Intent-Aware Network for Trigger-Induced Recommendation
- **Authors**: —
- **Institution**: Xianyu (Alibaba)
- **Link**: [arXiv:2602.13971](https://arxiv.org/abs/2602.13971)
- **Abstract**: Addresses intent myopia in trigger-induced recommendation. Hybrid ID+semantic enhancer with adaptive intent selection. Online: CTR +1.59%, diversity +1.73%, bills +2.37%.
- **Key Innovations**: Intent myopia diagnosis; hybrid ID+semantic enhancer; three-stage training strategy.

### RankUp: High-rank Representations for Large-Scale Advertising at Tencent
- **Authors**: —
- **Institution**: Tencent
- **Link**: [arXiv:2604.17878](https://arxiv.org/abs/2604.17878)
- **Abstract**: Mitigates embedding collapse via mechanisms enhancing latent representation diversity. Deployed across Weixin Video Accounts, Moments, Official Accounts. GMV lifts: +3.41%, +4.81%, +2.12%.
- **Key Innovations**: Anti-collapse embedding regularization; multi-scenario deployment results; CVR optimization focus.

### DS-MLP: Dual-Stream MLP for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution**: Renmin University, ByteDance, Meituan
- **Link**: [arXiv:2606.04944](https://arxiv.org/abs/2606.04944)
- **Abstract**: Dual-stream MLP with gated mechanisms at each interaction order for explicit+implicit feature learning. Consistent outperformance across Criteo, Avazu, Movielens.
- **Key Innovations**: Dual-stream architecture for explicit/implicit decomposition; gated multi-order filtering; simplicity + scalability.

### UniFormer: Unified Model-Centric Scaling for Industrial Recommendation at Kuaishou
- **Authors**: Bo Chen, Jinlong Jiao, Tijian Hu et al.
- **Institution**: Kuaishou
- **Link**: [arXiv:2606.27058](https://arxiv.org/abs/2606.27058)
- **Abstract**: Unified model-centric scaling decomposing feature and task spaces. Semantic-based tokenization for user-item decoupling. Online: +0.101%/+0.260% Stay Time, +0.729%/+1.113% Watch Time.
- **Key Innovations**: Model-centric (not data-centric) scaling framework; semantic tokenization for user-item decoupling.

### NOVA: Verification-Aware Agent Harness for RecSys Architecture Evolution
- **Authors**: Shaohua Liu, Liang Fang et al.
- **Institution**: —
- **Link**: [arXiv:2606.27243](https://arxiv.org/abs/2606.27243)
- **Abstract**: LLM agent harness with verification cascade (structure → local → offline → online). Architecture gradient for non-differentiable search. L3 candidate improves GMV +1.25%/+1.70%/+2.02% across three pCVR objectives.
- **Key Innovations**: Verification cascade for architecture evolution; architecture gradient for discrete search spaces.

### AgentX: Agent-Driven Self-Iteration of Industrial Recommender Systems
- **Authors**: Changxin Lao et al.
- **Institution**: —
- **Link**: [arXiv:2606.26859](https://arxiv.org/abs/2606.26859)
- **Abstract**: Production multi-agent system (Brainstorm → Develop → Evaluate → SGPO). SGPO distills execution trajectories into semantic-gradient updates for autonomous RS iteration.
- **Key Innovations**: Closed-loop autonomous RS iteration; semantic-gradient policy optimization for agent trajectories.

---

## Games & Reinforcement Learning

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: —
- **Institution**: —
- **Link**: [arXiv:2605.00347](https://arxiv.org/abs/2605.00347)
- **Abstract**: PPO with lightweight turn-level critic for VLM long-horizon gameplay in Super Mario Land. ≥3× game progress over frontier models. Cross-game generalization maintained. PPO substantially more stable than GRPO/Reinforce++.
- **Key Innovations**: Turn-level critic for long-horizon VLM RL; systematic RL component ablation for VLMs; pretrained VLM action priors.

### AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual Learning
- **Authors**: —
- **Institution**: —
- **Link**: [arXiv:2606.24893](https://arxiv.org/abs/2606.24893)
- **Abstract**: Procedurally generates open-ended text games for evaluating test-time continual learning agents. Measures world knowledge acquisition, episodic memory, exploration, action diversity, cost. Top agents leave substantial headroom.
- **Key Innovations**: First benchmark interleaving learning + inference throughout deployment; multi-faceted evaluation beyond game progress.

### MemoPilot: RL over Memory for Test-Time Learning in Games
- **Authors**: —
- **Institution**: —
- **Link**: [arXiv:2606.08656](https://arxiv.org/abs/2606.08656)
- **Abstract**: (Details in LLMs section) Multi-turn GRPO for memory updating in RPS and Limit Texas Hold'em. Elo 1762 (LHE), outperforming DeepSeek-V3.2.
- **Key Innovations**: RL-optimized memory update; turn-level advantage estimation; cross-game generalization.

### Phi-Actor-Critic: Steering General-Sum Games to Pareto-Efficient Correlated Equilibria
- **Authors**: —
- **Institution**: —
- **Link**: [arXiv:2606.11284](https://arxiv.org/abs/2606.11284)
- **Abstract**: Swap regret minimization for deep MARL. Centralized attention critic predicts vector-valued regrets in single forward pass. Lagrangian equilibrium selection optimizing social welfare under regret constraints.
- **Key Innovations**: Swap regret for deep MARL equilibrium selection; attention-based counterfactual regret estimation; Lagrangian welfare-stability trade-off.

### Regret Minimization with Adaptive Opponents in Repeated Games
- **Authors**: —
- **Institution**: COLT 2026
- **Link**: [arXiv:2606.06486](https://arxiv.org/abs/2606.06486)
- **Abstract**: Introduces Repeated Policy Regret (RP-Regret) — native metric for repeated games with adaptive opponents. Three algorithms including linearized surrogate. Minimizing RP-Regret can lead to cooperative solutions in Stag-Hunt.
- **Key Innovations**: RP-Regret metric for adaptive opponents; non-convex regret minimization algorithms; cooperative equilibrium discovery.

### From Trainee to Trainer: LLM-Designed Training Environment for RL
- **Authors**: Chao Chen et al.
- **Institution**: —
- **Link**: [arXiv:2606.17682](https://arxiv.org/abs/2606.17682)
- **Abstract**: Policy model analyzes failure trajectories and proposes next-stage training environment modifications. MAPF-FrozenLake testbed. Qwen3-4B outperforms larger proprietary LLMs. RL checkpoint serves as better environment engineer than base model.
- **Key Innovations**: Policy designs its own training environments; structured failure analysis for environment redesign; RL improves self-diagnosis.

### Scalable Maximum Entropy RL for Diffusion Policies via Adjoint Matching
- **Authors**: Serge Thilges et al.
- **Institution**: —
- **Link**: [arXiv:2606.22630](https://arxiv.org/abs/2606.22630)
- **Abstract**: Simulation-free training for diffusion policies via adjoint matching. Circumvents likelihood estimation and costly backpropagation through diffusion process. Competitive performance with reduced computational overhead.
- **Key Innovations**: Adjoint matching for diffusion policy RL; simulation-free training; practical online RL for diffusion models.

### dVLA-RL: RL over Denoising Trajectories for Discrete Diffusion VLA Models
- **Authors**: Yuhao Wu et al.
- **Institution**: —
- **Link**: [arXiv:2606.23623](https://arxiv.org/abs/2606.23623)
- **Abstract**: Shifts RL objective from marginal action probability to joint probability of generation path. Models denoising as MDP. 99.7% success on LIBERO; 30.6% improvement over SFT on RoboTwin 2.0.
- **Key Innovations**: Trajectory-level RL objective for discrete diffusion; variable denoising step scheduling; VLA-based robotics.

### CART: Conservative Adversarially Robust Decision Transformer
- **Authors**: X. Tang, Zhiyi Cheng, S. Praveen Kumar
- **Institution**: —
- **Link**: [arXiv:2510.11877](https://arxiv.org/abs/2510.11877)
- **Abstract**: First framework for adversarial robustness of Decision Transformer in stochastic games. Conditions policy on NashQ values from stage games. Superior worst-case returns across adversarial stochastic games.
- **Key Innovations**: NashQ-conditioned Transformer policy; adversarially robust sequential decision-making.

### IRumAI: First RL Agent for Indian Rummy
- **Authors**: Vignesh Mohan
- **Institution**: EURECOM
- **Link**: [arXiv:2606.21975](https://arxiv.org/abs/2606.21975)
- **Abstract**: PPO + meld-aware observation + deadwood-driven reward shaping + dual-branch conv net. 53.9% win rate vs strongest search-based opponent unseen during RL training. 0.33ms per action (7,000× faster than search-based heuristic).
- **Key Innovations**: First RL agent for Indian Rummy; implicit opponent hand modeling via linear probing; extreme inference speedup.

---

## Key Themes

| Theme | Signal |
|-------|--------|
| **Attention Architecture** | Head-level hybridization (HydraHead) surpasses layer-level. Polar attention (ATMA) solves softmax dilution at extreme context. Round-robin sparse attention (RRAttention) recovers 99%+ at half compute. MiniMax MSA achieves 28× compute reduction. |
| **CTR Scaling Laws** | DeRes (1.66× steeper γ than OneTrans), EST (stable power-law on Taobao), SparseCTR (scales across 3 OOM FLOPs). Unified modeling without lossy aggregation is the direction. |
| **GenAI for Advertising** | GRAB (Baidu), OneRanker (Tencent), GR4AD (Kuaishou) — all deploying generative retrieval+ranking in production. UA-SID, Fake Item Tokens, LazyAR as new building blocks. |
| **Reasoning Models** | SFT+RL complementarity formally characterized. GraphPO replaces chain/tree rollouts with DAG for better credit assignment. Early-token loss signals reasoning difficulty. Verification (Lean4) exposes label-reasoning gap. |
| **Self-Improving Agents** | SelfCompact (context compaction), Trainee→Trainer (policy designs its own environment), MemoPilot (RL-optimized memory). The model diagnoses and fixes itself. |
| **Games + RL** | VLMs for 100+ turn gameplay (Odysseus). Equilibrium selection via swap regret (Φ-AC). Repeated Policy Regret for adaptive opponents. First RL agent for Indian Rummy. |
