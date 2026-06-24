---
title: "arXiv Daily — 2026-06-24"
type: synthesis
created: 2026-06-24
updated: 2026-06-24
sources: []
tags: [arxiv, daily, LLM, recommendation, CTR, sequential-modeling, games, RL, state-space-model, KV-cache]
---

# arXiv Daily — 2026-06-24

Covering recent submissions (Jun 10–23, 2026) across AI, LLMs, recommendation, advertising, CTR prediction, sequential modeling, games, multi-agent RL, and efficient inference.

---

## LLM Reasoning & Agents

### 1. SPIRAL: Learning to Search and Aggregate
- **Authors**: Jubayer Ibn Hamid, Ifdita Hasan Orney, Michael Y. Li, Omar Shaikh, Yoonho Lee, Dorsa Sadigh, Chelsea Finn, Noah Goodman
- **Institution**: Stanford University
- **Abstract**: Introduces Sequential-Parallel-Aggregative Reinforcement Learning (SPIRAL), a framework training LMs to use sequential reasoning, parallel sampling, and trace aggregation as a unified inference compute pipeline. Uses set RL for parallel traces and standard RL for aggregation.
- **Key Innovations**: Joint training of all three inference primitives; outperforms GRPO by up to 11× scaling efficiency and 15% higher performance.
- **Link**: [2606.23595](https://arxiv.org/abs/2606.23595)

### 2. Self-Compacting Language Model Agents (SelfCompact)
- **Authors**: Tianjian Li et al.
- **Institution**: —
- **Abstract**: A scaffold allowing LMs to decide when and how to compact agent traces. Pairs a compaction tool with a lightweight rubric specifying when to fire/subpress. No fine-tuning or external supervision required.
- **Key Innovations**: Adaptive compaction without fixed-interval triggers; up to 18.1 point improvement on math, 5-9 on agentic search at 30-70% lower token cost.
- **Link**: [2606.23525](https://arxiv.org/abs/2606.23525)

### 3. Tmax: A Simple Recipe for Terminal Agents
- **Authors**: Hamish Ivison et al.
- **Institution**: —
- **Abstract**: Open RL recipe for terminal-using agents. Generates data using a novel taxonomy (difficulty control, personas, verifier diversification). Achieves 27% on Terminal-Bench 2.0 with 9B parameters, outperforming much larger models.
- **Key Innovations**: Large open-source terminal dataset (2.5× larger than prior); outcome-only RL recipe.
- **Link**: [2606.23321](https://arxiv.org/abs/2606.23321)

### 4. Can Reasoning Models Detect Changes to their Chains of Thought?
- **Authors**: Sathvik Napa, Utkarsh Singh, Chengyuan Xue, Miriam Wanner, William Walden
- **Institution**: —
- **Abstract**: Studies whether reasoning models detect interventions on their CoTs. Finds: (i) very modest detection accuracy; (ii) struggle to identify how CoT was modified; (iii) about as good at detecting own vs. others' CoT changes.
- **Key Innovations**: Systematic study of CoT tampering detection across reasoning models.
- **Link**: [2606.22085](https://arxiv.org/abs/2606.22085)

### 5. ReasoningLens: Hierarchical Visualization and Diagnostic Auditing for Large Reasoning Models
- **Authors**: Jun Zhang, Jiasheng Zheng, Boxi Cao, Yaojie Lu, Hongyu Lin, Jia Zheng, Xianpei Han, Le Sun
- **Institution**: —
- **Abstract**: Open-source framework for hierarchical visualization and diagnostic auditing of long CoT traces. Structures traces into interactive hierarchies, uses an agentic auditor for automated error detection.
- **Key Innovations**: Separates high-level strategy from low-level execution; reveals model-specific blind spots.
- **Link**: [2606.23404](https://arxiv.org/abs/2606.23404)

### 6. Abstract Representational Geometry Supports Inference in LLMs
- **Authors**: Yunan Zeng, Yuwang Wang
- **Institution**: —
- **Abstract**: Adapts contextual reversal-learning to text, comparing humans and LLMs. Finds LLM internal states exhibit hippocampal-like abstract geometric structures when inference occurs, organized hierarchically across model depth.
- **Key Innovations**: First mechanistic link between abstract representational geometry and inference in LLMs; geometric regularization of higher layers increases generalizable inference.
- **Link**: [2606.23345](https://arxiv.org/abs/2606.23345)

### 7. Structured Inference with Large Language Gibbs
- **Authors**: Sanghyeok Choi et al.
- **Institution**: —
- **Abstract**: Scheme for structured probabilistic inference using LLM conditional distributions as transition operators. Iteratively resamples variables conditioned on others via MCMC.
- **Key Innovations**: Avoids order-dependent biases of autoregressive generation; produces stationary distribution reflecting compromise between all local conditionals.
- **Link**: [2606.19264](https://arxiv.org/abs/2606.19264)

### 8. MemRefine: LLM-Guided Compression for Long-Term Agent Memory
- **Authors**: Minjae Kim et al.
- **Institution**: —
- **Abstract**: LLM-guided memory management framework that uses similarity to propose candidate pairs and defers delete/merge decisions to an LLM judge based on factual content.
- **Key Innovations**: Storage-budgeted memory management; outperforms rule-based baselines under tight budgets.
- **Link**: [2606.13177](https://arxiv.org/abs/2606.13177)

### 9. From Trainee to Trainer: LLM-Designed Training Environment for RL
- **Authors**: Chao Chen et al.
- **Institution**: —
- **Abstract**: LLM-as-Environment-Engineer framework where the policy model analyzes failure trajectories and proposes next-stage environment config modifications. Introduces MAPF-FrozenLake testbed.
- **Key Innovations**: Automated environment redesign; current RL checkpoint serves as better engineer than base model.
- **Link**: [2606.17682](https://arxiv.org/abs/2606.17682)

---

## Efficient Inference & KV Cache

### 10. MiniMax Sparse Attention (MSA)
- **Authors**: MiniMax AI
- **Institution**: MiniMax
- **Abstract**: Blockwise sparse attention built on GQA. Lightweight Index Branch scores KV blocks and selects Top-k per GQA group. On 109B MoE model, matches GQA quality with 28.4× attention compute reduction at 1M context.
- **Key Innovations**: Group-specific sparse retrieval; exp-free Top-k selection; 14.2× prefill and 7.6× decoding speedups.
- **Link**: [2606.13392](https://arxiv.org/abs/2606.13392)

### 11. Keyless Attention: Value-Space Routing and Value-Only Caching
- **Authors**: Xin Gao
- **Institution**: —
- **Abstract**: Eliminates key projection entirely. Attention scores computed directly between queries and values. Reduces KV cache by exactly 50%. Matches or outperforms standard attention on 4/5 models.
- **Key Innovations**: Value-Only Cache; Depth-m Attention Factorization; value-space routing matrix.
- **Link**: [2606.21848](https://arxiv.org/abs/2606.21848)

### 12. Tangram: Unlocking Non-Uniform KV Cache Compression
- **Authors**: —
- **Institution**: —
- **Abstract**: Serving framework that statically resolves non-uniform KV compression. Budget Reservation, Ragged Paging, and Ahead-of-Time Load Balancing. Up to 2.6× throughput improvement over full-KV baseline.
- **Key Innovations**: Head-wise retention follows offline-calibratable two-level structural regularity; drop-in substrate for non-uniform compression methods.
- **Link**: [2606.06302](https://arxiv.org/abs/2606.06302)

### 13. UltraQuant: 4-bit KV Caching for Context-Heavy Agents
- **Authors**: —
- **Institution**: —
- **Abstract**: 4-bit KV-cache compression using TurboQuant-style rotation and codebook quantization. FP4 approximation path on AMD CDNA4. Cuts P50 TTFT by 3.47× in cache-pressured late rounds.
- **Key Innovations**: Asymmetric K/V treatment; Walsh–Hadamard rotation; FP4 micro-tensors with UE8M0 scales.
- **Link**: [2606.20474](https://arxiv.org/abs/2606.20474)

### 14. RedKnot: Head-Aware KV Cache Management
- **Authors**: —
- **Institution**: —
- **Abstract**: Breaks monolithic KV cache abstraction by decomposing along KV heads. Supports position-independent KV reuse, prefix compression, hot/cold separation, distributed placement.
- **Key Innovations**: Head-level decomposition turns KV cache into structured memory object; no retraining required.
- **Link**: [2606.06256](https://arxiv.org/abs/2606.06256)

### 15. Training Transformers for KV Cache Compressibility (KV-CAT)
- **Authors**: —
- **Institution**: —
- **Abstract**: Formalizes KV compressibility as a property of learned representations. Proposes KV-CAT, a continued pretraining procedure with train-time KV sparsification policy.
- **Key Innovations**: Proves almost any function admits both compressible and non-compressible transformer implementations; incentivizes compressible representations during training.
- **Link**: [2605.05971](https://arxiv.org/abs/2605.05971)

### 16. DynaKV: Token-Wise Adaptive KV Cache Compression
- **Authors**: —
- **Institution**: —
- **Abstract**: First post-training framework for token-adaptive low-rank KV compression. Uses PCA basis transformation + learnable gating to allocate variable compression rates per token.
- **Key Innovations**: Retains 94% baseline performance with only 6% KV cache on LongBench.
- **Link**: [2603.04411](https://arxiv.org/abs/2603.04411)

### 17. TTKV: Temporal-Tiered KV Cache
- **Authors**: —
- **Institution**: —
- **Abstract**: Maps human memory system onto KV cache — fast tier (HBM) for recent tokens, slow tier (DRAM) for older states with differential quantization. Block-wise streaming attention.
- **Key Innovations**: 5.94× cross-tier traffic reduction; 76% latency reduction; 2× throughput improvement.
- **Link**: [2604.19769](https://arxiv.org/abs/2604.19769)

### 18. Self-Pruned Key-Value Attention (SP-KV)
- **Authors**: —
- **Institution**: —
- **Abstract**: Lightweight utility predictor scores each KV pair; recent KVs via local window, older pairs written only if predicted utility exceeds threshold. Joint end-to-end training.
- **Key Innovations**: 3-10× KV cache reduction; reveals structured layer- and head-specific sparsity patterns.
- **Link**: [2605.14037](https://arxiv.org/abs/2605.14037)

### 19. KV Packet: Recomputation-Free Context-Independent KV Caching
- **Authors**: Chuangtao Chen et al.
- **Institution**: —
- **Abstract**: Treats cached documents as immutable "packets" wrapped in light-weight trainable soft-token adapters. Self-supervised distillation bridges context discontinuities.
- **Key Innovations**: Near-zero FLOPs cache reuse; native compatibility with unstructured KV compression.
- **Link**: [2604.13226](https://arxiv.org/abs/2604.13226)

### 20. End-to-End Context Compression at Scale (LCLM)
- **Authors**: —
- **Institution**: —
- **Abstract**: Encoder-decoder compressors (Latent Context Language Models) trained end-to-end at scale. 0.6B-encoder, 4B-decoder models at 1:4, 1:8, 1:16 compression ratios.
- **Key Innovations**: Establishes new Pareto frontier on RULER, LongBench; efficient backbone for long-horizon agents.
- **Link**: [2606.09659](https://arxiv.org/abs/2606.09659)

---

## State Space Models & Sequence Modeling

### 21. Mamba-3: Improved Sequence Modeling using State Space Principles
- **Authors**: —
- **Institution**: —
- **Abstract**: Three core improvements: exponential-trapezoidal SSM discretization, complex-valued state updates, and MIMO formulation. At 1.5B, improves average downstream accuracy by 1.8 points over next best.
- **Key Innovations**: Complex-valued state spaces for richer state tracking; MIMO formulation for better hardware utilization without decode latency increase.
- **Link**: [2603.15569](https://arxiv.org/abs/2603.15569)

### 22. Ternary Mamba: Grouped QAT of W1.58A16 State Space Models
- **Authors**: Ramprasath Ganesaraja, Sahil Dilip Panse, Swathika N
- **Institution**: —
- **Abstract**: Ternary quantization of Mamba-2 1.3B to 3.61× compression (2,687→744 MB) using QAT with knowledge distillation in 4 GPU-hours. Identifies zero-ratio collapse instability.
- **Key Innovations**: 1,000× reduction in token budget vs from-scratch training; shows post-hoc correction fails for SSMs due to error accumulation through recurrence.
- **Link**: [2606.18114](https://arxiv.org/abs/2606.18114)

### 23. Priming: Hybrid State Space Models From Pre-trained Transformers
- **Authors**: Amazon
- **Institution**: Amazon AWS
- **Abstract**: Converts pretrained Transformers to Hybrid SSM-Attention models via layer replacement + short distillation. Evaluates GKA, GDN, Mamba-2 at 8B and 32B scale with 128K contexts.
- **Key Innovations**: GKA outperforms GDN which outperforms Mamba-2; ~2× concurrent sequences on same hardware; up to 2.3× decode throughput.
- **Link**: [2605.08301](https://arxiv.org/abs/2605.08301)

### 24. Swimba: Switch Mamba — MoE for State Space Models
- **Authors**: —
- **Institution**: —
- **Abstract**: MoE-parameterized SSM that mixes experts in parameter space, maintaining single state trajectory and single recurrence evaluation. Formalizes two MoE-SSM families.
- **Key Innovations**: Preserves efficient single-pass recurrence while scaling parameter capacity via MoE.
- **Link**: [2603.06938](https://arxiv.org/abs/2603.06938)

### 25. Bilinear Input Modulation for Mamba (Koopman Bilinear Forms)
- **Authors**: Hiroki Fujii
- **Institution**: —
- **Abstract**: Factorized bilinear input modulation augmenting SSM with state-input product (Koopman bilinear form). Coupled-BIM and Coupled-GM variants tested on memory retention and NARMA-10.
- **Key Innovations**: Clear dissociation: Coupled-GM improves memory retention, Coupled-BIM improves both memory and bilinear computation.
- **Link**: [2604.17221](https://arxiv.org/abs/2604.17221)

### 26. A Theoretical Analysis of Mamba's Training Dynamics
- **Authors**: —
- **Institution**: —
- **Abstract**: First theoretical analysis of selective SSM generalization and learning dynamics. Shows gating vector aligns with class-relevant features while ignoring irrelevant ones.
- **Key Innovations**: Formalizes feature-selection role of selective recurrence; non-asymptotic sample complexity bounds.
- **Link**: [2602.12499](https://arxiv.org/abs/2602.12499)

### 27. Architecture-Aware RL Makes Sliding-Window Attention Competitive (SWARR)
- **Authors**: Kai Liu et al.
- **Institution**: —
- **Abstract**: Two-stage recipe: convert pretrained SA to SWA with SFT, then policy adaptation with RL. On-policy RL optimizes self-generated trajectories under SWA constraint, narrowing the gap.
- **Key Innovations**: RL changes the conclusion about SWA viability for math reasoning; recovers much of the accuracy lost during SWA conversion.
- **Link**: [2606.11634](https://arxiv.org/abs/2606.11634)

---

## CTR Prediction & Advertising

### 28. Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)
- **Authors**: Kesha Ou (Renmin Univ.), Zhen Tian (ByteDance), Wayne Xin Zhao, Long Zhang (Meituan), Sheng Chen, Ji-Rong Wen
- **Institution**: Renmin University of China, ByteDance, Meituan
- **Abstract**: Uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP, with parallel MLP for implicit interactions. Two alignment strategies for optimization.
- **Key Innovations**: Vanilla MLP structure achieves SOTA across three benchmarks; scalable and efficient.
- **Link**: [2606.04944](https://arxiv.org/abs/2606.04944)

### 29. DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR
- **Authors**: —
- **Institution**: —
- **Abstract**: Dual-path inter-layer connector for CTR Transformers: Identity residual path + Block Attention Residual path with vector-wise gate. Pointwise AttnRes replaces Softmax with SiLU.
- **Key Innovations**: 1.66× steeper compute-AUC scaling law; 8-layer DeRes matches 16-layer OneTrans; up to +0.32% AUC at <5% additional FLOPs.
- **Link**: [2606.07980](https://arxiv.org/abs/2606.07980)

### 30. IDProxy: Cold-Start CTR Prediction with Multimodal LLMs
- **Authors**: Xiaohongshu
- **Institution**: Xiaohongshu (Little Red Book)
- **Abstract**: Uses MLLMs to generate proxy embeddings from content signals for cold-start items. Aligned with existing ID embedding space, optimized end-to-end under CTR objectives.
- **Key Innovations**: Deployed on Xiaohongshu Explore Feed serving hundreds of millions daily; coarse-to-fine alignment mechanism.
- **Link**: [2603.01590](https://arxiv.org/abs/2603.01590)

### 31. GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning
- **Authors**: Kesha Ou et al.
- **Institution**: —
- **Abstract**: Generative user intent framework using semantic interest cohorts. Employs next-item prediction (NTP) to produce candidate interest cohorts, then hierarchical candidate-aware network for ranking.
- **Key Innovations**: Addresses overfitting to historically dominant features; candidate-agnostic intent representations.
- **Link**: [2601.18251](https://arxiv.org/abs/2601.18251)

### 32. GRAB: Generative Ranking for Ads at Baidu
- **Authors**: Baidu
- **Institution**: Baidu
- **Abstract**: End-to-end generative CTR framework with Causal Action-aware Multi-channel Attention (CamA). Full-scale deployment at Baidu.
- **Key Innovations**: 3.05% revenue increase, 3.49% CTR lift; monotonic improvement with longer sequences.
- **Link**: [2602.01865](https://arxiv.org/abs/2602.01865)

### 33. EST: Efficiently Scalable Transformer for CTR
- **Authors**: Alibaba (Taobao)
- **Institution**: Alibaba
- **Abstract**: Fully unified modeling without lossy aggregation. Lightweight Cross-Attention (LCA) and Content Sparse Attention (CSA). Deployed on Taobao display advertising.
- **Key Innovations**: 3.27% RPM increase, 1.22% CTR lift; stable power-law scaling relationship.
- **Link**: [2602.10811](https://arxiv.org/abs/2602.10811)

### 34. CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer
- **Authors**: LinkedIn
- **Institution**: LinkedIn
- **Abstract**: End-to-end decoder-only transformer for ads CTR. Context-conditioned decoding, self-gated attention, timestamp-based RoPE, session masking. Deployed at LinkedIn.
- **Key Innovations**: Solves chicken-and-egg problem between predicted CTR and ranking; 11.04% CTR lift over LiRank baseline.
- **Link**: [2602.11410](https://arxiv.org/abs/2602.11410)

### 35. LLM-HYPER: Generative CTR for Cold-Start Ad Personalization
- **Authors**: —
- **Institution**: Top US e-commerce platform
- **Abstract**: LLMs as hypernetworks to generate CTR estimator parameters. Few-shot CoT prompting over multimodal ad content. Normalization and calibration for production.
- **Key Innovations**: 55.9% improvement in NDCG@10 over cold-start baselines; deployed in production.
- **Link**: [2604.12096](https://arxiv.org/abs/2604.12096)

### 36. LoopCTR: Loop Scaling for CTR Prediction
- **Authors**: —
- **Institution**: —
- **Abstract**: Loop scaling paradigm with sandwich architecture, Hyper-Connected Residuals, MoE, and process supervision. Train-multi-loop, infer-zero-loop strategy.
- **Key Innovations**: Zero-loop inference already surpasses all baselines; oracle reveals 0.02-0.04 AUC untapped headroom.
- **Link**: [2604.19550](https://arxiv.org/abs/2604.19550)

### 37. GenLI: Generative Long-term User Interest Modeling for CTR
- **Authors**: Meituan
- **Institution**: Meituan
- **Abstract**: Interest generation module (IGM) produces multiple target-independent interest distributions. Behavior retrieval in O(1). Deployed at Meituan.
- **Key Innovations**: 0.776% CTR increase, 1.567% RPM increase in online A/B; avoids complex matching-based retrieval.
- **Link**: [2605.15905](https://arxiv.org/abs/2605.15905)

### 38. DAIAN: Deep Adaptive Intent-Aware Network for CTR in Trigger-Induced Recommendation
- **Authors**: —
- **Institution**: E-commerce platform
- **Abstract**: Dynamically adapts to users' intent preferences in trigger-induced recommendation. Hybrid enhancer with ID and semantic information.
- **Key Innovations**: Addresses "intent myopia"; adaptive selection based on varying intents.
- **Link**: [2602.13971](https://arxiv.org/abs/2602.13971)

### 39. SparseCTR: Sparse Attention for Long-term Behaviors
- **Authors**: —
- **Institution**: —
- **Abstract**: Three-branch sparse self-attention for global interests, interest transitions, and short-term interests. Composite relative temporal encoding.
- **Key Innovations**: 1.72% CTR and 1.41% CPM increase online; clear scaling law across three orders of magnitude FLOPs.
- **Link**: [2601.17836](https://arxiv.org/abs/2601.17836)

---

## Recommendation Systems

### 40. UniRec: Bridging Generative and Discriminative Recommendation via Chain-of-Attribute
- **Authors**: Shopee
- **Institution**: Shopee
- **Abstract**: Chain-of-Attribute (CoA) prefixes SID sequences with structured attribute tokens. Joint RFT and DPO alignment framework. Deployed on Shopee.
- **Key Innovations**: +22.6% HR@50 overall; +5.37% PVCTR, +4.76% orders, +5.60% GMV online.
- **Link**: [2604.12234](https://arxiv.org/abs/2604.12234)

### 41. GR4AD: Generative Recommendation for Large-Scale Advertising
- **Authors**: —
- **Institution**: Platform with 400M+ users
- **Abstract**: Production-oriented generative recommender with UA-SID tokenization, VSL, RSPO (ranking-guided RL), and Dynamic Beam Serving. Fully deployed.
- **Key Innovations**: Up to 4.7% improvement over state-of-the-art; real-time serving at scale.
- **Link**: [2602.22732](https://arxiv.org/abs/2602.22732)

### 42. Trajectory-Based Recommender Systems as Control Systems
- **Authors**: Eriam Schaffter, Ahmed Bounekkar, Elsa Negre (UCBL)
- **Institution**: Université Claude Bernard Lyon 1
- **Abstract**: Argues Control Theory provides foundations for Trajectory-Based Recommender Systems. Models Educational RS within proposed TBRS framework.
- **Key Innovations**: First unified theoretical framework for TBRS based on control theory.
- **Link**: [2606.22957](https://arxiv.org/abs/2606.22957)

### 43. GenAIR: Generative Archetype-Grounded Item Representations for Sequential Recommendation
- **Authors**: —
- **Institution**: —
- **Abstract**: LLM generates Archetype (target audience profile) from item metadata. Behavioral calibration objective grounds representations in real interaction patterns.
- **Key Innovations**: Model-agnostic; bridges semantic richness of LLM knowledge with behavioral reality.
- **Link**: [2606.11023](https://arxiv.org/abs/2606.11023)

### 44. SRPFN: One Sequential Recommendation Model Pretrained from Synthetic Priors
- **Authors**: Woosung Kang, Jiwon Jeong, Jonghyeok Shin, Jeongwhan Choi, Noseong Park
- **Institution**: KAIST
- **Abstract**: Pretrained solely on synthetic data (hDCSBM random walks). Predicts multiple datasets without gradient updates. Single forward pass inference in ~1 minute.
- **Key Innovations**: 7.53% average improvement over second-best method; no target-domain training needed.
- **Link**: [2606.15752](https://arxiv.org/abs/2606.15752)

### 45. RoTE: Coarse-to-Fine Multi-Level Rotary Time Embedding for Sequential Recommendation
- **Authors**: —
- **Institution**: —
- **Abstract**: Decomposes timestamps into multiple temporal granularities, incorporated into item embeddings. Plug-and-play for Transformer-based models.
- **Key Innovations**: Up to 20.11% improvement in NDCG@5; captures heterogeneous temporal patterns.
- **Link**: [2604.13389](https://arxiv.org/abs/2604.13389)

### 46. ConvRec: Convolutional Networks for Attribute-Aware Sequential Recommendation
- **Authors**: —
- **Institution**: —
- **Abstract**: Hierarchical convolutional approach with linear complexity. Down-scales user sequences into compact representations.
- **Key Innovations**: Outperforms attention-based models; up to 7.82% NDCG@10 improvement; superior memory efficiency.
- **Link**: [2605.04723](https://arxiv.org/abs/2605.04723)

### 47. HyenaRec: Hyena Operator for Fast Sequential Recommendation
- **Authors**: —
- **Institution**: —
- **Abstract**: Polynomial-based (Legendre) kernel parameterization with gated convolutions. Scales linearly with sequence length.
- **Key Innovations**: Up to 6× training speedup; outperforms attention, recurrent, and other baselines.
- **Link**: [2603.25027](https://arxiv.org/abs/2603.25027)

### 48. ACE: Anisotropy-Controllable Embedding for LLM-enhanced Sequential Recommendation
- **Authors**: —
- **Institution**: —
- **Abstract**: Linear autoencoder (LAE) reshaping LLM-generated embedding distribution. L2 regularization controls anisotropy while preserving semantic structure.
- **Key Innovations**: Up to 12.4% Recall@20 and 11.8% NDCG@20 improvement over existing LLM-enhanced SR models.
- **Link**: [2605.29322](https://arxiv.org/abs/2605.29322)

### 49. Beyond Interleaving: Causal Attention Reformulations for Generative Recommender Systems
- **Authors**: —
- **Institution**: —
- **Abstract**: Reformulates HSTU-style generative recommendation by encoding in→an causal dependency. AttnLFA and AttnMVP architectures eliminate interleaved dependencies.
- **Key Innovations**: 50% sequence complexity reduction; strict causal attention without expressive power loss.
- **Link**: [2603.10369](https://arxiv.org/abs/2603.10369)

### 50. MergeRec: Model Merging for Data-Isolated Cross-Domain Sequential Recommendation
- **Authors**: —
- **Institution**: —
- **Abstract**: Data-isolated CDSR setting — no overlapping users/items, no interaction data sharing. Uses model merging to construct universal cross-domain recommender.
- **Key Innovations**: Privacy-preserving; strong generalization to unseen domains.
- **Link**: [2601.01753](https://arxiv.org/abs/2601.01753)

### 51. Scalable Sequential Recommendation under Latency and Memory Constraints (HoloMambaRec)
- **Authors**: —
- **Institution**: —
- **Abstract**: Combines holographic reduced representations for attribute-aware embedding with selective state space encoder (Mamba-style). Constant-time recurrent inference.
- **Key Innovations**: Surpasses SASRec; trails only GRU4Rec on Amazon Beauty; substantially lower memory complexity.
- **Link**: [2601.08360](https://arxiv.org/abs/2601.08360)

### 52. PerSRec: Efficient Sequential Recommendation via Personalization
- **Authors**: Meta / Facebook Research
- **Institution**: Meta
- **Abstract**: Compresses long user histories into learnable tokens combined with recent interactions. Applied to HSTU and HLLM.
- **Key Innovations**: Dramatically reduces inference cost while preserving accuracy.
- **Link**: [2601.03479](https://arxiv.org/abs/2601.03479)

---

## Multi-Agent RL & Games

### 53. Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: Chengshuai Shi, Wenzhe Li, Xinran Liang, Yizhou Lu, Wenjia Yang, Ruirong Feng, Seth Karten, Ziran Yang, Zihan Ding, Gabriel Sarch, Danqi Chen, Karthik Narasimhan, Chi Jin
- **Institution**: Princeton University
- **Abstract**: Adapted PPO with lightweight turn-level critic for training VLMs on extended game tasks. At least 3× average game progress over frontier models.
- **Key Innovations**: Turn-level critic stabilizes long-horizon RL; cross-game generalization demonstrated.
- **Link**: [2605.00347](https://arxiv.org/abs/2605.00347)

### 54. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: —
- **Institution**: —
- **Abstract**: Applies self-play to two-player zero-sum language games. Distributed actor-learner architecture with role-conditioned advantage estimation (RAE).
- **Key Innovations**: Unlimited training data through game dynamics; RAE stabilizes multi-agent training.
- **Link**: [2506.24119](https://arxiv.org/abs/2506.24119)

### 55. TARPO: Token-Wise Latent-Explicit Reasoning via Action-Routing Policy Optimization
- **Authors**: Liting Zhang, Shiwan Zhao, Xuyang Zhao, Zichen Xu, Jianye Wang, Qicheng Li
- **Institution**: —
- **Abstract**: Pure RL framework that adaptively switches between discrete token generation and continuous latent reasoning at each step via lightweight action head router.
- **Key Innovations**: Preserves stochasticity for policy exploration; outperforms existing latent/explicit reasoning RL baselines.
- **Link**: [2606.05859](https://arxiv.org/abs/2606.05859)

### 56. LangMARL: Natural Language Multi-Agent Reinforcement Learning
- **Authors**: —
- **Institution**: —
- **Abstract**: Brings credit assignment and policy gradient evolution from cooperative MARL into language space. Agent-level language credit assignment.
- **Key Innovations**: Improved sample efficiency; interpretability; strong generalization across varied agent counts.
- **Link**: [2604.00722](https://arxiv.org/abs/2604.00722)

### 57. Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **Authors**: —
- **Institution**: —
- **Abstract**: Recursive reasoning paradigm integrating opponents' reasoning processes. Centralized CoT comparison module + hybrid advantage estimation.
- **Key Innovations**: 22.1% average performance improvements across various multi-agent games.
- **Link**: [2605.04906](https://arxiv.org/abs/2605.04906)

### 58. Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution
- **Authors**: —
- **Institution**: —
- **Abstract**: LLM (Gemma 3 27B) as centralized strategic controller selecting among RL skill policies in 2v2 King of the Hill. User study (n=15): 60% perceive LLM+RL as most human-like.
- **Key Innovations**: Matches hand-crafted BT performance; hierarchical decomposition addresses credit assignment.
- **Link**: [2606.20014](https://arxiv.org/abs/2606.20014)

### 59. Beyond Static Evaluation: Co-Evolutionary Mechanisms for LLM-Driven Strategy Evolution (FAMOU)
- **Authors**: —
- **Institution**: —
- **Abstract**: LLM-driven code-level evolution generating tactical structures absent from seed strategies (lookahead search, adaptive interception). 1st place AAMAS 2026 MCTF Competition.
- **Key Innovations**: Nontrivial algorithmic innovations through code-level evolution; 68.0% win rate across ten benchmark opponents.
- **Link**: [2606.10389](https://arxiv.org/abs/2606.10389)

### 60. Agentic Monte Carlo: Simulating RL for Black-Box Agents
- **Authors**: Layer6 AI
- **Institution**: Layer6 AI
- **Abstract**: Uses Sequential Monte Carlo to sample from optimal policy of black-box LLM agents. Learns a value function to steer the agent without modifying the underlying model.
- **Key Innovations**: Outperforms prompting baselines and matches GRPO when scaling test-time compute; applicable to API-only LLMs.
- **Link**: [2606.05296](https://arxiv.org/abs/2606.05296)

### 61. GARL: Game-Theoretic RL for Multi-Agent Strategic Prioritisation
- **Authors**: —
- **Institution**: —
- **Abstract**: Two-stage game: competing agents allocate strategic resources, arbiter produces final ranking. RL guided by game-theoretic utilities.
- **Key Innovations**: Small open-source LLMs become competitive with GPT-level models via game-theoretic RL.
- **Link**: [2606.05002](https://arxiv.org/abs/2606.05002)

### 62. Foresight Optimization for Strategic Reasoning in LLMs (FoPO)
- **Authors**: —
- **Institution**: —
- **Abstract**: Incorporates opponent modeling into policy optimization for explicit foresight. Cooperative RSA and Competitive Taboo datasets in self-play framework.
- **Key Innovations**: Strong generalization to out-of-domain strategic scenarios.
- **Link**: [2604.13592](https://arxiv.org/abs/2604.13592)

### 63. AgentJet: A Flexible Swarm Training Framework for Agentic RL
- **Authors**: Qingxu Fu, Boyin Liu, Shuchang Tao, Zhaoyang Liu, Bolin Ding
- **Institution**: —
- **Abstract**: Decoupled multi-node architecture: swarm server nodes host training, swarm client nodes execute agents. Supports heterogeneous multi-model RL, multi-task cocktail training, live code iteration.
- **Key Innovations**: 1.5-10× training speedup via context tracking with timeline merging; Werewolves RPG RL experiment with Qwen2 7B/14B vs Qwen3-235B.
- **Link**: [2606.04484](https://arxiv.org/abs/2606.04484)

### 64. RuleSmith: Multi-Agent LLMs for Automated Game Balancing
- **Authors**: —
- **Institution**: —
- **Abstract**: Couples game engine, multi-agent LLM self-play, and Bayesian optimization over multi-dimensional rule space. Instantiated on CivMini (civilization-style game).
- **Key Innovations**: First automated game balancing framework using LLM agents; converges to highly balanced configurations.
- **Link**: [2602.06232](https://arxiv.org/abs/2602.06232)

### 65. MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors**: —
- **Institution**: —
- **Abstract**: Single GPT-based model trained on 1.5B expert trajectories (SMACv2, GRF, POGEMA). Single transformer-based observation encoder requiring no task-specific tuning.
- **Key Innovations**: First multitask MARL foundation model; competitive with specialized baselines across diverse environments.
- **Link**: [2604.05943](https://arxiv.org/abs/2604.05943)

### 66. Robust Adversarial RL in Stochastic Games via Sequence Modeling (CART)
- **Authors**: —
- **Institution**: —
- **Abstract**: Conservative Adversarially Robust Decision Transformer — first framework for DT robustness in adversarial stochastic games. Conditions Transformer policy on NashQ values.
- **Key Innovations**: Less exploitable and conservative to transition uncertainty; superior worst-case returns.
- **Link**: [2510.11877](https://arxiv.org/abs/2510.11877)

---

## Social World Models & Alignment

### 67. Building Social World Models with Large Language Models (SWM)
- **Authors**: —
- **Institution**: —
- **Abstract**: SWM-Bench from Polymarket/Kalshi data (Dec 2022–Jan 2026). State-of-the-art on Kalshi, outperforms GPT-5.5 on Polymarket.
- **Key Innovations**: First benchmark for news-driven belief forecasting; latent causal driver isolation paradigm.
- **Link**: [2606.11482](https://arxiv.org/abs/2606.11482)

### 68. Auditing Proprietary Alignment in LLMs: A Comparative Framework
- **Authors**: —
- **Institution**: —
- **Abstract**: Statistical framework for detecting proprietary alignment via comparative behavioral analysis. Quantifies systematic deviations without ground-truth standard.
- **Key Innovations**: Black-box auditing; provides quantitative evidence that deployment-specific alignment policies alter model behavior.
- **Link**: [2606.08381](https://arxiv.org/abs/2606.08381)
