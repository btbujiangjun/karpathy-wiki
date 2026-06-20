---
title: "arXiv AI Search — June 2026"
type: synthesis
created: 2026-06-20
updated: 2026-06-20
tags: [arxiv, survey, llm, ctr, recommendation, games, sequential-modeling, reinforcement-learning]
sources: []
---

# arXiv AI Search Report — June 2026

A curated survey of recent arXiv preprints (Feb–Jun 2026) across LLMs, recommendation/advertising systems, sequential modeling, and game-playing AI.

---

## 1. LLM Architecture & Training

### 1.1 Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling
- **arXiv**: [2606.07404](https://arxiv.org/abs/2606.07404)
- **Authors**: Rohan Shravan
- **Institution**: The School of AI, Bengaluru
- **Abstract**: Trains a 120B-parameter sparse MoE (LightningLM 0.1V) on a single 8-GPU node via four-stage progressive growth from a 1.78B dense seed. Uses reversible recurrence (flat activation memory), state-preserving growth (dense → MoE, shallow → deep), and TQP (quantized base weights + trained LoRA adapters, cutting optimizer state 45×). Achieves loss 1.78 at 120B scale.
- **Key Innovation**: Single-node 120B MoE training; silent-failure catalog from growth operations.

### 1.2 The Recurrent Transformer: Greater Effective Depth and Efficient Decoding
- **arXiv**: [2604.21215](https://arxiv.org/abs/2604.21215)
- **Authors**: Costin-Andrei Oncescu, Depen Morwani, Samy Jelassi, Alexandru Meterez, Mujin Kwun, Sham Kakade
- **Institution**: Harvard University
- **Abstract**: Each layer attends to KV pairs computed from its own activations, yielding layerwise recurrent memory. Emulates both standard transformers and token-to-token recurrent updates. An I/O-aware tiling algorithm reduces HBM traffic from Θ(N²) to Θ(N log N). Improves cross-entropy on C4 at 300M scale.
- **Key Innovation**: Recurrent attention without modifying standard autoregressive decoding; practical tiling for training efficiency.

### 1.3 Latent Recurrent Transformer (LRT)
- **arXiv**: [2605.26797](https://arxiv.org/abs/2605.26797)
- **Authors**: Zeyi Huang, Xuehai He, LiLiang Ren, Yiping Wang, Baolin Peng, Hao Cheng, Shuohang Wang, Pengcheng He, Jianfeng Gao, Yong Jae Lee, Yelong Shen
- **Institution**: Microsoft, UW-Madison, UW
- **Abstract**: Reuses a high-level source-layer hidden state from the previous token as recurrent memory. Adds a cross-layer recurrent latent pathway with only 0.3% parameter overhead. Uses interleaved parallel training at ~2× baseline compute. Improves language modeling and in-context learning.
- **Key Innovation**: Lightweight recurrent memory injection via KV Projection + Residual Injection; no pause tokens or extra depth loops.

### 1.4 Mamba-3: Improved Sequence Modeling using State Space Principles
- **arXiv**: [2603.15569](https://arxiv.org/abs/2603.15569)
- **Authors**: (Mamba team)
- **Institution**: —
- **Abstract**: Three innovations: (1) exponential-trapezoidal discretization, (2) complex-valued state spaces for state tracking, (3) multi-input multi-output (MIMO) formulation. At 1.5B, improves avg accuracy by 1.8pp over Gated DeltaNet. Half the state size of Mamba-2 at comparable perplexity.
- **Key Innovation**: Complex-valued SSM states, MIMO for inference HW utilization.

### 1.5 Swimba: Switch Mamba Model Scales State Space Models
- **arXiv**: [2603.06938](https://arxiv.org/abs/2603.06938)
- **Authors**: (NVIDIA)
- **Institution**: NVIDIA
- **Abstract**: MoE-parameterized SSM that routes over expert-produced SSM streams but mixes them in parameter space, preserving a single hidden-state trajectory. Built on Nemotron-H-8B hybrid backbone. Avoids replicating expensive recurrence across experts.
- **Key Innovation**: MoE for SSMs without multiple recurrence evaluations.

### 1.6 Hyperloop Transformers
- **arXiv**: [2604.21254](https://arxiv.org/abs/2604.21254)
- **Authors**: —
- **Institution**: —
- **Abstract**: Looped transformer with begin/middle/end blocks; only middle block is recurrent. Hyper-connections expand residual stream into matrix-valued streams after each loop. Outperforms depth-matched transformers with ~50% fewer parameters; gains persist through quantization.
- **Key Innovation**: Parameter-efficient looped architecture + hyper-connections.

### 1.7 MiniMax Sparse Attention (MSA)
- **arXiv**: [2606.13392](https://arxiv.org/abs/2606.13392)
- **Authors**: Xunhao Lai, Weiqi Xu, Yufeng Yang, Qiaorui Chen (NVIDIA), Yang Xu, Lunbin Zeng, Xiaolong Li, Haohai Sun, Haichao Zhu, Vito Zhang, Jinkai Hu, Jiayao Li, Rui Gao, Zekun Li, Songquan Zhu, Jingkai Zhou, Pengyu Zhao
- **Institution**: MiniMax, Peking University, NVIDIA, ZJU, HUST, NJU, HDU
- **Abstract**: Blockwise token selection with max-pooling scoring; retains most recent block for stability. On a 109B MoE model trained from scratch (3T tokens), MSA matches GQA on benchmarks while delivering 14.2× prefill and 7.6× decoding speedups at 1M context.
- **Key Innovation**: Occam's-razor sparse attention; ultra-lightweight index branch; practical wall-clock speedups at 1M context.

### 1.8 The Phasor Transformer
- **arXiv**: [2603.17433](https://arxiv.org/abs/2603.17433)
- **Authors**: —
- **Institution**: —
- **Abstract**: Phase-native alternative to dense attention. Combines trainable phase-shifts with parameter-free DFT token coupling. Global O(N log N) mixing without attention maps. Aligned with periodic/oscillatory temporal dynamics.
- **Key Innovation**: Unit-circle manifold sequence modeling; deterministic global DFT coupling.

### 1.9 FDM (Fan Duality Model): O(1) Decode Memory
- **arXiv**: [2604.07716](https://arxiv.org/abs/2604.07716)
- **Authors**: Yasong Fan
- **Institution**: —
- **Abstract**: Separates sequence processing into "wave" (norm-preserving Givens rotations) and "particle" (local-global cache with 272 fixed slots). Strict O(1) decode memory: 867 MB fixed vs Transformer's 4,247 MB at N=8,192 (4.9× reduction). Freeze-Scan training improves convergence 7.5×.
- **Key Innovation**: Wave-particle resolution of the sequence-modeling deadlock; Freeze-Scan training.

---

## 2. LLM Reasoning & Post-Training

### 2.1 Beyond the Commitment Boundary: Probing Epiphenomenal CoT
- **arXiv**: [2606.13603](https://arxiv.org/abs/2606.13603)
- **Authors**: Daniel Scalena, Sara Candussio, Luca Bortolussi, Elisabetta Fersini, Malvina Nissim, Gabriele Sarti
- **Institution**: —
- **Abstract**: Shows that reasoning traces cross a "commitment boundary" — a sharp single-step transition to a stable answer, followed by epiphenomenal CoT steps that don't alter the answer. Attention probes linearly decode answer formation stages. Early-exit at commitment boundary reduces CoT length up to 55% with negligible performance loss.
- **Key Innovation**: Causal importance estimation via early exit; epiphenomenal CoT identification.

### 2.2 Agentic Chain-of-Thought Steering (ACTS)
- **arXiv**: [2606.03965](https://arxiv.org/abs/2606.03965)
- **Authors**: Yu Xia et al.
- **Institution**: —
- **Abstract**: A controller agent steers a frozen reasoner via MDP: observes trace + budget, issues strategy + steering phrase. Trained on synthetic trajectories with multi-budget augmentation, optimized via RL with budget-conditioned reward shaping. Matches full-thinking performance with substantial token savings.
- **Key Innovation**: Budget-aware reasoning strategy control; controller-reasoner separation.

### 2.3 Do Post-Training Algorithms Actually Differ? (oxRL)
- **arXiv**: [2603.19335](https://arxiv.org/abs/2603.19335)
- **Authors**: —
- **Institution**: —
- **Abstract**: Unified framework implementing 51 post-training algorithms. Key findings: (1) rankings invert across scale (SimPO goes from worst at 1.5B to best at 7B); (2) loss modifications yield negligible gains (none of 20 DPO variants beat vanilla DPO); (3) algorithm leverage is task-specific (19.3pp GSM8K spread collapses to 0.54pp on MATH). Hierarchy: scale (~50pp) ≫ paradigm (~10pp) ≫ online vs offline (~9pp) ≫ loss function (~1pp).
- **Key Innovation**: Largest controlled comparison of post-training algorithms; scale-dependent ranking inversions.

### 2.4 LLM Post-Training: A Unified View of Off-Policy and On-Policy Learning
- **arXiv**: [2604.07941](https://arxiv.org/abs/2604.07941)
- **Authors**: —
- **Institution**: —
- **Abstract**: Comprehensive survey unifying SFT, preference optimization, RLHF/RLVR, process supervision, distillation, and hybrid systems under a trajectory-distribution lens. Argues many methods are different ways of intervening on the same underlying object.
- **Key Innovation**: Unified conceptual framework for all post-training paradigms.

### 2.5 Mechanistic Analysis of Alignment Algorithms
- **arXiv**: [2606.09850](https://arxiv.org/abs/2606.09850)
- **Authors**: —
- **Institution**: —
- **Abstract**: Linear probes, SAEs, and crosscoders reveal distinct alignment signatures: KTO/GRPO improve preference decodability; DPO/ORPO reduce it via different mechanisms (non-constructive rotation vs. activation attenuation). Links algorithmic design choices to feature-geometric changes.
- **Key Innovation**: Mechanistic interpretability applied to alignment algorithms.

### 2.6 PROPEL: Training Task Generators at the Learnable Frontier
- **arXiv**: [2606.18284](https://arxiv.org/abs/2606.18284)
- **Authors**: Lorenz Wolf, Connor Watts, Roger Creus Castanyer, Geoffrey Bradway, Maxwill Lin, Augustine N. Mavor-Parker, Matthew Daborn-Sargent
- **Institution**: —
- **Abstract**: Replaces solver-in-the-loop RL for task generator training with an activation probe predicting solver pass rate from frozen generator hidden states. Doubles frontier-task generation rate across math, code, and SWE. For SWE, increases target-solve-rate share from 9.8% to 19.6% with Qwen3.5-27B.
- **Key Innovation**: Solver-amortized RL for task generation; activation probes as dense reward proxies.

### 2.7 From Reasoning Traces to Reusable Modules
- **arXiv**: [2606.18089](https://arxiv.org/abs/2606.18089)
- **Authors**: —
- **Institution**: —
- **Abstract**: Formalizes compositional generalization via hierarchical latent selection model. Shows SFT supplies raw module materials in compositional traces; RL decomposes traces to identify atomic modules. SFT needs coverage of all atomic modules; RL focuses on novel compositions outside SFT support.
- **Key Innovation**: Theoretical framework explaining SFT+RL synergy in reasoning.

---

## 3. Recommendation & Advertising / CTR

### 3.1 GR4AD: Generative Recommendation for Large-Scale Advertising
- **arXiv**: [2602.22732](https://arxiv.org/abs/2602.22732)
- **Authors**: —
- **Institution**: (Industry, production system)
- **Abstract**: Production generative recommender for real-time advertising. UA-SID (MLLM-based semantic IDs + MGMR RQ-Kmeans quantization), LazyAR decoder (relaxes layer-wise AR dependencies), VSL + RSPO (value-aware online learning with list-wise RL), Dynamic Beam Serving. Achieves <100ms latency on L20 GPUs with online learning.
- **Key Innovation**: Full-stack generative recommendation co-design; LazyAR; RSPO for list-wise advertising optimization.

### 3.2 RankUp: High-rank Representations for Advertising Recommenders
- **arXiv**: [2604.17878](https://arxiv.org/abs/2604.17878)
- **Authors**: —
- **Institution**: Tencent
- **Abstract**: Addresses representation collapse in deep recommenders via randomized permutation splitting, multi-embedding paradigm, global token integration, crossed pretrained embedding tokens. Deployed on Weixin Video Accounts/Official Accounts/Moments; GMV lifts of 3.41%/4.81%/2.12%.
- **Key Innovation**: Practical solution to rank collapse in industrial recommenders.

### 3.3 GRAB: Generative Ranking for Ads at Baidu
- **arXiv**: [2602.01865](https://arxiv.org/abs/2602.01865)
- **Authors**: —
- **Institution**: Baidu
- **Abstract**: End-to-end generative CTR framework with Causal Action-aware Multi-channel Attention (CamA). Full deployment at Baidu home feed ads: 3.05% revenue increase, 3.49% CTR lift. AUC improves monotonically with model capacity and sequence length — no saturation observed.
- **Key Innovation**: CamA for temporal dynamics + action signals; scaling behavior in generative CTR.

### 3.4 Memento: Personalized RAG-Style Long-Retention Data Scaling
- **arXiv**: [2605.24051](https://arxiv.org/abs/2605.24051)
- **Authors**: (Meta)
- **Institution**: Meta
- **Abstract**: Treats user history as document corpus, ad requests as queries; retrieves via MMR. Two complementary modes: Representation Memento (retrieved embeddings for features) and Data Memento (past training examples). 5–10× resource efficiency, sub-10ms latency. 1% CTR lift and 1.2% CVR lift on Facebook Feed/Reels at 365+ days of history.
- **Key Innovation**: RAG for recommendation history scaling; temporal chunking + INT8 + async serving.

### 3.5 EST: Efficient Scaling Laws in CTR Prediction
- **arXiv**: [2602.10811](https://arxiv.org/abs/2602.10811)
- **Authors**: —
- **Institution**: Alibaba (Taobao)
- **Abstract**: Efficiently scalable Transformer for CTR prediction. Power-law scaling with model capacity and compute. Deployed on Taobao display advertising: 3.27% RPM increase, 1.22% CTR lift (Guess scenario); 2.01% CTR lift, 2.66% RPM lift (Post-purchase).
- **Key Innovation**: Verified power-law scaling for CTR Transformers at Taobao scale.

### 3.6 OneRanker: Unified Generation and Ranking with One Model
- **arXiv**: [2603.02999](https://arxiv.org/abs/2603.02999)
- **Authors**: —
- **Institution**: Tencent (Weixin)
- **Abstract**: Single-model deep integration of generation and ranking for advertising. Value-aware multi-task decoupling, coarse-to-fine target awareness (Fake Item Tokens), KV pass-through, Distribution Consistency loss. Deployed on Weixin channels: GMV +1.34%.
- **Key Innovation**: Architectural unification of generation and ranking in one model.

### 3.7 DeRes: Decoupling Residual Stability and Adaptivity for CTR
- **arXiv**: [2606.07980](https://arxiv.org/abs/2606.07980)
- **Authors**: Wenzhuo Cheng, Shipeng Nie, Qixin Guo, Xuefeng Sun, Jianguo Lou, Zhengwei Zheng
- **Institution**: —
- **Abstract**: Dual-path residual connector: Identity path (first-order reuse) + Block Attention Residual path (cross-layer attention with SiLU-based gating). Steeper compute–AUC scaling law (γ=0.118 vs 0.071). 8-layer DeRes matches 16-layer OneTrans. Up to +0.32% AUC at <5% extra FLOPs on 331M-interaction industrial dataset.
- **Key Innovation**: Dual-path residuals for CTR; Pointwise AttnRes with SiLU forgetting; 2× compute saving at equivalent AUC.

### 3.8 IDProxy: Cold-Start CTR with Multimodal LLMs
- **arXiv**: [2603.01590](https://arxiv.org/abs/2603.01590)
- **Authors**: (Xiaohongshu)
- **Institution**: Xiaohongshu
- **Abstract**: MLLM-generated proxy embeddings aligned with ID embedding space for cold-start CTR. Coarse-to-fine alignment, end-to-end CTR optimization. Serves hundreds of millions of users daily on Content Feed and Display Ads.
- **Key Innovation**: MLLM proxy embeddings replacing ID embeddings for cold-start; production deployment at Xiaohongshu.

---

## 4. Sequential Modeling & State Space Models

### 4.1 Sessa: Selective State Space Attention
- **arXiv**: [2604.18580](https://arxiv.org/abs/2604.18580)
- **Authors**: —
- **Institution**: —
- **Abstract**: Places attention inside a recurrent feedback path. Proves power-law memory tails (O(ℓ^{-β})) slower than Transformer/Mamba baselines. Only model class among comparisons that achieves non-decaying selective retrieval. Strongest long-context performance in matched experiments.
- **Key Innovation**: Attention-in-recurrence design; provable memory advantages; flexible selective retrieval.

### 4.2 Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models
- **arXiv**: [2603.08859](https://arxiv.org/abs/2603.08859)
- **Authors**: —
- **Institution**: —
- **Abstract**: Proves pure SSMs need large state (linear in hidden dim) and pure Transformers need large window (linear in context length) for composition tasks. Constructs small hybrids with logarithmic size + sublinear memory. Formalizes when hybrids win.
- **Key Innovation**: Theoretical framework proving hybrid necessity for composition tasks.

### 4.3 DMamba: Decomposition-enhanced Mamba for Time Series
- **arXiv**: [2602.09081](https://arxiv.org/abs/2602.09081)
- **Authors**: —
- **Institution**: —
- **Abstract**: Explicitly decomposes time series into trend + seasonal + residual components; aligns Mamba backbone complexity with component properties. SOTA among Mamba-based and non-Mamba models on ETT, Weather, PEMS benchmarks.
- **Key Innovation**: Decomposition-aware SSM architecture for time series.

### 4.4 UniMamba: Unified Spatial-Temporal Modeling
- **arXiv**: [2604.16325](https://arxiv.org/abs/2604.16325)
- **Authors**: —
- **Institution**: —
- **Abstract**: Mamba Variate-Channel Encoding with FFT-Laplace Transform + TCN for global temporal dependencies; Spatial Temporal Attention for inter-variate correlations; Feedforward Temporal Dynamics layer for continuous/discrete fusion. SOTA on 8 benchmark datasets.
- **Key Innovation**: Hybrid SSM + attention for multivariate forecasting.

### 4.5 Why Depth Matters in Parallelizable Sequence Models: A Lie Algebraic View
- **arXiv**: [2603.05573](https://arxiv.org/abs/2603.05573)
- **Authors**: —
- **Institution**: —
- **Abstract**: Formulates depth↔expressivity correspondence via Lie algebra extensions. Shows error diminishes exponentially with depth. Empirically validated on symbolic word and state-tracking problems.
- **Key Innovation**: Lie-algebraic theory of depth in parallel sequence models.

---

## 5. Games & Reinforcement Learning Agents

### 5.1 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **arXiv**: [2605.00347](https://arxiv.org/abs/2605.00347)
- **Authors**: Chengshuai Shi, Wenzhe Li, Xinran Liang, Yizhou Lu, Wenjia Yang, Ruirong Feng, Seth Karten, Ziran Yang, Zihan Ding, Gabriel Sarch, Danqi Chen, Karthik Narasimhan, Chi Jin
- **Institution**: Princeton University (PLI), Fudan University, Tsinghua University
- **Abstract**: Studies RL for VLMs in long-horizon game playing (Super Mario Land, 100+ turns). Proposes adapted PPO with lightweight turn-level critic, outperforming GRPO and Reinforce++. Achieves 3× average game progress over frontier models. Generalizes to unseen levels and games.
- **Key Innovation**: Stable long-horizon VLM RL; turn-level critic; open training framework.

### 5.2 Resource-Efficient Model-Free RL for Board Games
- **arXiv**: [2602.10894](https://arxiv.org/abs/2602.10894)
- **Authors**: Kazuki Ota, Takayuki Osa, Motoki Omura, Tatsuya Harada
- **Institution**: —
- **Abstract**: Model-free RL algorithm for board games competitive with search-based methods (AlphaZero). Tested on Animal Shogi, Gardner Chess, Go, Hex, Othello. Achieves efficient learning without search.
- **Key Innovation**: Model-free RL competitive with search-based methods in board games.

### 5.3 Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents
- **arXiv**: [2603.17683](https://arxiv.org/abs/2603.17683)
- **Authors**: —
- **Institution**: —
- **Abstract**: Two-player architecture (perception vs. action) + curriculum learning + database-as-control-plane + LLM-as-judge. V2 achieves 50–94× sample efficiency over comparable systems (~32 vs 1,600–3,000 interactions). Failure diagnosed as self-consistent hallucination cascade in perception layer.
- **Key Innovation**: Database-driven test-time curriculum learning; honest negative result reporting.

### 5.4 FAMOU: Co-Evolutionary LLM Strategy Evolution in Adversarial Games
- **arXiv**: [2606.10389](https://arxiv.org/abs/2606.10389)
- **Authors**: (Li et al.)
- **Institution**: —
- **Abstract**: Co-evolves evaluation alongside strategies via LLM code evolution. On 3v3 maritime capture-the-flag (MCTF 2026), achieves 61.7% win rate against unseen opponents. LLM mutation generates tactical structures absent from seeds (lookahead search, adaptive interception). 1st in hardware round-robin, 3rd in simulation at AAMAS 2026 MCTF Competition.
- **Key Innovation**: Evaluator co-evolution + weakness pressure; LLMs as directed mutation operators.

### 5.5 STRATAGEM: Learning Transferable Reasoning via Game Self-Play
- **arXiv**: [2604.17696](https://arxiv.org/abs/2604.17696)
- **Authors**: —
- **Institution**: —
- **Abstract**: Selectively reinforces domain-agnostic reasoning trajectories via Reasoning Transferability Coefficient; incentivizes adaptive reasoning via Reasoning Evolution Reward. Improves math reasoning (AIME24 from 13.3% to 20.0%, AMC-23 from 52.5% to 60.0%), general reasoning, and code generation.
- **Key Innovation**: Game self-play that transfers to mathematical reasoning; reasoning transferability coefficient.

### 5.6 MEMO: Memory-Augmented Model Context Optimization for Self-Play
- **arXiv**: [2603.09022](https://arxiv.org/abs/2603.09022)
- **Authors**: —
- **Institution**: —
- **Abstract**: Weight-free self-play with persistent memory bank (CRUD operations), tournament-style context evolution, and prioritized replay. Raises GPT-4o-mini win rate from 25.1% to 49.5% on text-based games. Uses 19× fewer self-play games than RL baselines.
- **Key Innovation**: Memory-augmented context optimization without weight updates; persistent self-play memory.

### 5.7 T-STAR: Tree-Structured Self-Taught Agent Rectification
- **arXiv**: [2604.07165](https://arxiv.org/abs/2604.07165)
- **Authors**: —
- **Institution**: —
- **Abstract**: Consolidates independent trajectories into a Cognitive Tree for variance-reduced advantage estimation. Thought grafting synthesizes corrective reasoning at divergence points. Surgical policy optimization targets critical steps. Consistent improvements over GRPO on embodied, interactive, reasoning, and planning tasks.
- **Key Innovation**: Cognitive Tree for trajectory consolidation; thought grafting for self-rectification.

### 5.8 Nemobot Games: LLM-Powered Game Agents
- **arXiv**: [2604.21896](https://arxiv.org/abs/2604.21896)
- **Authors**: —
- **Institution**: —
- **Abstract**: Extends Shannon's game-playing machine taxonomy with LLM agents. Covers dictionary-based, solvable, heuristic, and learning-based games. Integrates RLHF, self-critique, and crowdsourced learning. Programmable environment for tool-augmented game agent creation.
- **Key Innovation**: Shannon-taxonomy-aligned framework for LLM game agents.

---

## Quick Reference Table

| Domain | Paper | Venue/Date | Key Metric | Institution |
|--------|-------|-----------|------------|-------------|
| LLM Arch | Reversible Foundations (120B MoE) | Jun 2026 | 1-node 8-GPU training | School of AI |
| LLM Arch | Recurrent Transformer | Apr 2026 | Θ(N log N) HBM traffic | Harvard |
| LLM Arch | MiniMax Sparse Attn | Jun 2026 | 14.2× prefill @ 1M ctx | MiniMax + PKU |
| SSM | Mamba-3 | Mar 2026 | +1.8pp vs Gated DeltaNet | — |
| SSM | Swimba (MoE-SSM) | Mar 2026 | Single trace MoE-SSM | NVIDIA |
| Post-Train | oxRL (51 algos) | Mar 2026 | Scale inverts rankings | — |
| Post-Train | PROPEL | Jun 2026 | 2× frontier task rate | — |
| CTR/Rec | GR4AD | Feb 2026 | <100ms L20 inference | Industry |
| CTR/Rec | GRAB (Baidu) | Feb 2026 | +3.49% CTR, +3.05% CPM | Baidu |
| CTR/Rec | Memento (Meta) | May 2026 | 1% CTR, 1.2% CVR lift | Meta |
| CTR/Rec | EST (Taobao) | Feb 2026 | +3.27% RPM, +1.22% CTR | Alibaba |
| CTR/Rec | DeRes | Jun 2026 | 2× compute-AUC saving | — |
| Games | Odysseus (VLM RL) | May 2026 | 3× game progress | Princeton |
| Games | FAMOU (CoEvo) | Jun 2026 | AAMAS 2026 1st place | — |
| Games | MEMO (self-play) | Mar 2026 | 19× fewer games | — |
