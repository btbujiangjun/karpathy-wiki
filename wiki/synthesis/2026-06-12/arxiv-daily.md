---
title: "arXiv Daily — 2026-06-12"
type: synthesis
created: 2026-06-12
updated: 2026-06-12
sources: []
tags: [arxiv-daily, llm, recommendation, ctr, games, sequential-modeling, reinforcement-learning, time-series, transformers, scaling-laws, agents]
---

# arXiv Daily — 2026-06-12

Recent papers spanning AI, LLMs, recommendation systems, CTR prediction, sequential modeling, games, and related areas. Papers are primarily from June 2026 submissions.

---

## LLMs & Architectures

### 1. Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling (LightningLM 0.1V)
- **Authors**: Rohan Shravan
- **Institution**: — (Independent)
- **Link**: https://arxiv.org/abs/2606.07404
- **Abstract**: Reports training a 120B-parameter sparse MoE on a single 8-GPU node end-to-end. LightningLM 0.1V grows from a dense 1.78B seed through 5B and 9B MoE stages to 120B with 460 routed experts (top-12). Uses reversible recurrence (activation memory flat across depth), state-preserving growth (each expansion preserves learned interface), and TQP (quantized base weights + trained LoRA adapters cutting optimizer state ~45x).
- **Key Innovations**: End-to-end 120B MoE on one node; reversible recurrence stack; state-preserving growth principles; TQP for single-node economics.

### 2. SigmaScale: LLM Compression with SVD-based Low-Rank Decomposition and Learned Scaling Matrices
- **Authors**: Ernests Lavrinovics, Marco Letizia, Roy Janco, Shai Segal, Johannes Bjerva, Maurizio Pierini
- **Institution**: CERN / Aalborg University
- **Link**: https://arxiv.org/abs/2606.07098
- **Abstract**: Learns auxiliary scaling matrices S for truncated SVD-based LLM compression. Optimizes row/column scaling vectors under activation-aware loss, lowering effective intrinsic rank of weight matrices. Competitive with SVD-based SOTA on Llama 3.1 8B and Qwen3-8B.
- **Key Innovations**: Learned activation-aware scaling for SVD; effective-rank entropy analysis; flexible low-rank compression without specialized hardware.

### 3. Chiaroscuro Attention: Spending Compute in the Dark (CHIAR-Former)
- **Authors**: Prateek Kumar Sikdar
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.08327
- **Abstract**: Proposes CHIAR-Former, a hybrid transformer routing tokens to DCT spectral mixing or full self-attention based on per-token spectral entropy. Discovers routing collapse: DCT + Attention alone are complementary and sufficient. Achieves 45% PPL improvement over full-attention baseline on WikiText-103 with 62.5% fewer attention FLOPs.
- **Key Innovations**: Spectral entropy-based token routing; routing collapse discovery; DCT+Attention hybrid outperforms full attention on large-scale text.

### 4. Parallel Causal Associative Fields: Gated Sparse Memory for Long-Context Language Modeling (PCAF)
- **Authors**: Muhammad Ahmed
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.10435
- **Abstract**: Proposes PCAF, a parallel content-addressed memory over causal successor records. Writes local records into hash buckets, retrieves bounded candidate sets, forms sparse cache distribution over successor tokens, and mixes with a parametric local LM via learned gate. 303M model reaches 36.31 PPL on WikiText-103 vs 47.49 for dense Transformer, with higher throughput (0.61M vs 0.43M tokens/s on TPU v4-32).
- **Key Innovations**: Hash-bucket associative memory for LM; gated sparse cache; avoids fixed recurrent state bottleneck.

### 5. NF-CoT: Latent Reasoning with Normalizing Flows
- **Authors**: Zhai et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.06447
- **Abstract**: Places a scalable normalizing flow inside the LLM's causal stream, modeling continuous thoughts distilled from explicit CoT. Preserves left-to-right generation, KV-cache decoding, and tractable likelihood estimation. On MBPP, HumanEval, and LiveCodeBench v6, improves pass rates over explicit-CoT and prior latent-reasoning baselines while substantially reducing intermediate reasoning cost.
- **Key Innovations**: TARFlow-style normalizing flow for latent reasoning; exact likelihoods for continuous thoughts; policy-gradient optimization in latent reasoning space.

### 6. CART: Context-Anchored Recurrent Transformer
- **Authors**: Christopher Capps
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.01495
- **Abstract**: Parameter-efficient LM that reuses a single shared core block R times. Computes K,V once from a multi-layer prelude and reuses them via MLA cross-attention throughout the recurrent core. A learned LTI gate settles on spectral radius [0.79, 0.83] across all scales, ensuring stable recurrence.
- **Key Innovations**: Frozen K,V anchor for recurrent LM core; LTI gate for provable stability; separates context encoding from iterative refinement.

### 7. Cubit: Token Mixer with Kernel Ridge Regression
- **Authors**: G. Chen, B. Yin, et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2605.06501
- **Abstract**: Reinterprets attention as Nadaraya-Watson regression and proposes replacing it with Kernel Ridge Regression in Transformers. Uses closed-form KRR solution combining kernel similarities with inverse kernel matrix normalization. Introduces Limited-Range Rescale for training stability.
- **Key Innovations**: KRR as drop-in attention replacement; stronger theoretical foundation than standard attention; performance gains increase with sequence length.

### 8. Do Transformers Need Three Projections? Systematic Study of QKV Variants
- **Authors**: Ali Kayyam, Anusha Madan Gopal, M Anthony Lewis
- **Institution**: BrainChip Inc.
- **Link**: https://arxiv.org/abs/2606.04032
- **Abstract**: Systematic evaluation of Projective Sharing in self-attention — sharing Q-K, K-V, or single projection. Merging K=V eliminates separate V cache, achieving 50% KV cache reduction. Synergistic with GQA/MQA: combined with MQA yields up to 96.9% KV cache reduction with only 0.41% accuracy loss at 1.2B scale.
- **Key Innovations**: K-V projection sharing; 50% KV cache cut; multiplicative effect with head-sharing methods.

### 9. Affine-Scaled Attention: Towards Flexible and Stable Transformer Attention
- **Authors**: Qiu et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2602.23057
- **Abstract**: Augments softmax attention weights with input-dependent scaling and bias, relaxing the unit-sum constraint. Reduces first-token bias, improves head utilization, increases attention entropy. Consistent improvements across multiple model scales.
- **Key Innovations**: Affine transformation of attention weights; reduced attention sink behavior; complementary to Gated Attention.

### 10. BAPO Bounds on Chain-of-Thought Token Complexity
- **Authors**: Kiran Tomlinson, Tobias Schnabel, Adith Swaminathan, Jennifer Neville
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2602.02909
- **Abstract**: Extends Bounded Attention Prefix Oracle (BAPO) model to prove lower bounds on CoT tokens required for binary majority, triplet matching, and graph reachability (all Ω(n) tokens for input size n). Experiments with frontier reasoning models show approximately linear scaling and failures under constrained budgets.
- **Key Innovations**: First theoretical lower bounds on CoT length; BAPO model extension; matches empirical results with frontier reasoning models.

### 11. ReasoningFlow: Discourse Structures for LLM Reasoning Traces
- **Authors**: Ziyan Liu et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.05402
- **Abstract**: Captures reasoning trace discourse structures into fine-grained DAGs with 8 node types and 14 edge types. Manually annotated 31 traces (2.1k steps) then auto-annotated 1,260 traces (247.7k steps) across 5 models. Key findings: LRMs have structurally similar traces regardless of training; most erroneous steps don't derive final answers.
- **Key Innovations**: First discourse-level annotation schema for reasoning traces; large-scale multi-model analysis; DAG-based trace structure.

### 12. Rethinking the Role of Positional Encoding: Sliding-Window Transformers without PE Remain Turing Complete
- **Authors**: Kozachinskiy, Steifer, Wałęga; Li & Wang (multiple groups)
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.01532
- **Abstract**: Proves that sliding-window Transformers without positional encoding are Turing complete via the HIST model (token itself breaks permutation symmetry). Demonstrates that PE is not indispensable for universal computation in the autoregressive setting.
- **Key Innovations**: Theoretical proof that PE is unnecessary for Turing completeness; HIST abstract model for autoregressive computation.

### 13. Unveiling Entropy Dynamics of Chain-of-Thought Reasoning
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.02020
- **Abstract**: Uncovers consistent two-phase CoT structure: Uncertainty Region of exploration → Confidence Region of convergence. Uses CUSUM change-point detection for training-free early exit and test-time scaling. Achieves 63.06% accuracy with 11.1% token reduction, outperforming DEER and Dynasor by 3.28% and 4.36%.
- **Key Innovations**: CUSUM for CoT confidence region detection; training-free early exit; test-time scaling via confidence-weighted voting.

---

## LLM Agents & Memory

### 14. Less Context, More Accuracy: A Bi-Temporal Memory Engine for LLM Agents (Engram)
- **Authors**: Liuyin Wang
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.09900
- **Abstract**: Open-source dual-process memory engine with a bi-temporal data model. Fast write path appends lossless episodes without LLM in critical path; asynchronous consolidation extracts SPO facts, builds temporal KG, resolves contradictions without per-fact LLM calls. Hybrid read path fuses dense, lexical, graph, and recency signals with point-in-time filtering. 83.6% on LongMemEval_S vs 73.2% full-context baseline (+10.4 points), using ~8x fewer tokens (9.6k vs 79k).
- **Key Innovations**: Bi-temporal knowledge graph; contradiction resolution without per-fact LLM; reproducible evaluation harness with measurement-integrity documentation.

### 15. LANTERN: Layered Archival and Temporal Episodic Retrieval for Long-Context LLM Conversations
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.05182
- **Abstract**: Lightweight memory layer proactively archiving every conversation turn, restoring relevant details after compaction via hybrid retrieval (zero LLM calls, <25ms latency). On 94 real conversations (1,894 facts), Lantern-Rerank recovers 78.3% of lost facts vs MemGPT's 72.4%, at fraction of inference cost.
- **Key Innovations**: Zero-LLM-call hybrid retrieval for conversation memory; coverage-coherence trade-off analysis; rigorous evaluation framework with human-validated facts.

### 16. Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents (MRAgent)
- **Authors**: Shuo Ji, Yibo Li, Bryan Hooi
- **Institution**: National University of Singapore
- **Link**: https://arxiv.org/abs/2606.06036
- **Abstract**: Proposes MRAgent with Cue-Tag-Content associative memory graph and active reconstruction mechanism that integrates LLM reasoning into memory access. Iteratively explores and prunes retrieval paths based on accumulated evidence. Up to 23% improvement on LoCoMo and LongMemEval benchmarks with reduced token and runtime cost. **Accepted at ICML 2026.**
- **Key Innovations**: Active memory reconstruction (not static retrieval); Cue-Tag-Content graph structure; dynamic retrieval path pruning.

### 17. Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses
- **Authors**: DataArcTech
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.08348
- **Abstract**: Treats reusable skills as hypotheses about frozen model success under given prompts/contexts. Records verified trajectory evidence, maintains feature-conditioned categorical posterior over each skill, and maps posterior state into actions (patch, split, compress, retire, explore). With DeepSeek-V4-Flash, improves SOP-Bench from 80% to 95%, Lifelong AgentBench from 90% to 100%.
- **Key Innovations**: Bayesian posterior for skill management; inspectable skill evolution; cross-harness (native, Claude Code, mini-swe-agent backends).

---

## LLM Training & RL

### 18. RL Excursions during Pre-Training: Re-examining Policy Optimization for LLM Training
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.04272
- **Abstract**: Trains LLM from scratch and applies RL directly to intermediate pre-training checkpoints. Key findings: RL is effective very early in pre-training; pre-training data composition matters more than model scale; RL expands distribution (vs. SFT which sharpens + degrades general capabilities); parallel RL+SFT objective averaging outperforms pipeline approaches.
- **Key Innovations**: First systematic study of RL applied mid-pre-training; RL before SFT expands pass@k distribution; parallel RL+SFT fusion.

### 19. Rollout-Level Advantage-Prioritized Experience Replay for GRPO
- **Authors**: Charles Arnal et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.04560
- **Abstract**: Proposes replay buffer for GRPO storing individual rollouts (not groups) with age eviction and advantage-magnitude priority. Fresh-anchored composition preserves on-policy data. At Qwen3-4B scale, achieves +4.35pp on five-bench average. Gains grow with model size.
- **Key Innovations**: First effective replay buffer for GRPO; rollout-level prioritization; fresh-anchored batch composition.

### 20. EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agentic RL
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.03108
- **Abstract**: Autonomous training framework co-evolving LLM policies and diagnostic harnesses through empirical feedback. Policy self-evolution (generation, comparison, pruning, merging) + trainer self-reflection (evolving metrics/analyzers when insufficient). On SWE-9B: 38.16% BC% vs 33.77% for human-engineered RL baseline.
- **Key Innovations**: Co-evolution of policy + training harness; self-diagnosing trainer with persistent skill library; autonomous RL beyond recipe search.

### 21. Scaling Laws for RL Post-Training of LLMs
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2603.12151
- **Abstract**: Studies optimal allocation of sampling compute in LLM RL post-training. Compute-optimal number of parallel rollouts per problem increases with budget then saturates. On easy problems, more rollouts sharpen performance; on hard problems, they discover rare successful trajectories. Practical allocation rule: more problems if budget small, more rollouts as budget grows.
- **Key Innovations**: First prescription of scaling laws for RL post-training; compute-optimal rollout allocation; differentiation of easy vs hard problem regimes.

### 22. GIFT: Games as Informal Training for Generalizable LLMs
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2601.05633
- **Abstract**: RL framework jointly training LLMs on math reasoning + game-based environments (Matrix Games, TicTacToe, Who's the Spy). Proposes Coordinated Subtask Training (CST) replacing mixed updates with sequential subtask-specific updates. For 7B models: 57.39% ability score vs 42.00% from formal training alone.
- **Key Innovations**: Games as informal training for LLMs; CST for heterogeneous RL signals; second-order gradient interaction for cross-task coordination.

---

## Agentic RL & Reasoning

### 23. Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning
- **Authors**: Chengshuai Shi et al.
- **Institution**: Princeton University
- **Link**: https://arxiv.org/abs/2605.00347
- **Abstract**: Studies RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Proposes adapted PPO with lightweight turn-level critic, outperforming GRPO and Reinforce++. Open-source Odysseus framework achieves 3x average game progress over frontier models, with cross-game generalization.
- **Key Innovations**: Turn-level critic for long-horizon VLM RL; pretrained VLMs as strong action priors; open training framework for game-playing VLMs.

### 24. Learning When Not to Act: Mitigating Tool Abuse in Agentic RL (EAPO)
- **Authors**: Liuji Chen et al.
- **Institution**: — (Under review)
- **Link**: https://arxiv.org/abs/2606.02132
- **Abstract**: EAPO framework introduces tool-free trajectories in rollout groups, difficulty-aware reward shaping to penalize redundant tool calls on easy queries, and confidence-aware token reweighting. On Qwen2.5-7B: +7.27% average performance, -18.33% tool calls vs GRPO.
- **Key Innovations**: Selective tool use via difficulty-aware shaping; tool-free rollouts as training signal; confidence-aware token-level gradient modulation.

### 25. ACTS: Agentic Chain-of-Thought Steering for Efficient LLM Reasoning
- **Authors**: Yu Xia et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.03965
- **Abstract**: Formulates reasoning steering as MDP where a controller agent adaptively steers a frozen reasoner. Issues budget-aware actions (reasoning strategy + steering phrase) at each step. Initialized from synthetic steering trajectories + multi-budget augmentation, optimized via RL with budget-conditioned reward shaping. Matches full-thinking with substantial token savings.
- **Key Innovations**: MDP formulation of CoT steering; budget-aware strategy control; synthetic trajectory initialization + RL optimization.

### 26. ThoughtFold: Folding Reasoning Chains via Introspective Preference Learning
- **Authors**: Ziyan Liu et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.03503
- **Abstract**: Fine-grained preference learning that identifies and penalizes redundant steps within correct trajectories via Dynamic Mask Strategy. Step-level signals explicitly penalize redundant exploration while preserving essential logical steps.
- **Key Innovations**: Fine-grained (step-level) reasoning policy optimization; introspective redundancy detection; Dynamic Mask Strategy for step-level precision.

### 27. Strat-Reasoner: Reinforcing Strategic Reasoning in Multi-Agent Games
- **Authors**: Yadong He et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2605.04906
- **Abstract**: RL framework improving LLM strategic reasoning in multi-agent games via recursive reasoning (agent's reasoning integrates others' reasoning). Centralized CoT comparison module evaluates reasoning quality. Hybrid advantage + group-relative RL. 22.1% avg improvements.
- **Key Innovations**: Recursive reasoning with opponent modeling for LLMs; centralized CoT comparison for reward; hybrid advantage in multi-agent settings.

### 28. Agentic Monte Carlo: Simulating RL for Black-Box Agents (AMC)
- **Authors**: Dae Yon Hwang et al.
- **Institution**: Layer 6 AI
- **Link**: https://arxiv.org/abs/2606.05296
- **Abstract**: Uses Sequential Monte Carlo to sample from the optimal policy posterior of a black-box LLM agent, treating the fixed model as the prior. Learns a value function to steer the agent without modifying parameters. Outperforms prompting baselines and even GRPO as test-time compute scales. **Accepted at ICML 2026.**
- **Key Innovations**: RL for black-box agents via Bayesian inference; SMC-based trajectory optimization; test-time compute scaling for policy optimization.

### 29. ARTIS: Agentic Risk-Aware Test-Time Scaling via Iterative Simulation
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2602.01709
- **Abstract**: Decouples exploration from commitment for agentic TTS by simulating interactions before real-world execution. Risk-aware tool simulator trained on failure-inducing data for higher fidelity on critical error cases.
- **Key Innovations**: Simulation-before-execution for agentic TTS; risk-aware simulator training; first TTS framework designed for agentic settings.

### 30. Streaming Communication in Multi-Agent Reasoning (StreamMA)
- **Authors**: Zhen Yang et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.05158
- **Abstract**: Streams each reasoning step to downstream agents as soon as generated, pipelining adjacent agents. Formalized first closed-form joint analysis of stream vs serial vs single protocols. Discovers "step-level scaling law": increasing per-agent steps improves both effectiveness and efficiency, orthogonal to agent-count scaling. +7.3pp avg across 8 reasoning benchmarks.
- **Key Innovations**: Streaming protocol for multi-agent reasoning; step-level scaling law; closed-form analysis of reasoning protocols.

### 31. Gaussian Trust Region Policy Optimization (GTR)
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.03382
- **Abstract**: Shows PPO's trust region fails in non-stationary environments. Proposes Gaussian-trust-region with non-monotonic bounded constraint — strong local stability that relaxes under sustained high-advantage updates. Strong across games, robotics, exploration, and LLM post-training.
- **Key Innovations**: Gaussian-kernel trust region for non-stationary RL; Mixture Gaussian Anchor; architecture-agnostic improvement over PPO.

### 32. MemoPilot: RL over Memory for Test-Time Learning in Games
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.08656
- **Abstract**: Plug-in memory copilot that trains memory update process via multi-turn GRPO to improve frozen LLM in sequential interactions. Turn-wise reward + context-independent turn-level advantage estimation. On Limit Texas Hold'em and Rock-Paper-Scissors, tops DeepSeek-V3.2 in Elo ratings (1762 on LHE).
- **Key Innovations**: Trainable memory update via RL; turn-level advantage estimation; game-playing LLM copilot.

---

## CTR Prediction & Advertising

### 33. DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction
- **Authors**: Wenzhuo Cheng et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.07980
- **Abstract**: Dual-path residual for Transformer CTR: Identity path preserves feature reuse, Block Attention Residual attends over all earlier blocks. Pointwise AttnRes (SiLU instead of Softmax) for parallel multi-interest. Outperforms 12 baselines; steeper compute-AUC scaling law (1.66x gap). 8-layer DeRes matches 16-layer OneTrans.
- **Key Innovations**: Dual-path residual with identity + cross-layer attention; SiLU-based forgetting weights; superior scaling law in CTR.

### 34. LoopCTR: Unlocking Loop Scaling Power for CTR Prediction
- **Authors**: Jiakai Tang et al. (Alibaba)
- **Institution**: Alibaba
- **Link**: https://arxiv.org/abs/2604.19550
- **Abstract**: Loop scaling paradigm: recursive reuse of shared model layers decouples computation from parameter growth. Sandwich architecture with Hyper-Connected Residuals and MoE. Process supervision enables train-multi-loop, infer-zero-loop strategy. Oracle analysis reveals 0.02-0.04 AUC untapped headroom.
- **Key Innovations**: Loop scaling (computation without parameter growth); process supervision; zero-loop inference matching multi-loop.

### 35. CADET: Context-Conditioned Ads CTR With Decoder-Only Transformer
- **Authors**: David Pardoe et al. (LinkedIn)
- **Institution**: LinkedIn
- **Link**: https://arxiv.org/abs/2602.11410
- **Abstract**: End-to-end decoder-only transformer for ads CTR deployed at LinkedIn. Context-conditioned decoding with multi-tower heads (solves CTR-ranking chicken-and-egg), self-gated attention, timestamp RoPE, session masking. 11.04% CTR lift vs production LiRank.
- **Key Innovations**: First decoder-only Transformer for ads CTR at scale; post-scoring signal modeling; industrial production engineering.

### 36. Memento: Personalized RAG-Style Long-Retention Data Scaling for Ads
- **Authors**: Xiaoyu Chen et al. (Meta, 24 authors)
- **Institution**: Meta
- **Link**: https://arxiv.org/abs/2605.24051
- **Abstract**: RAG-style framework treating user history as document corpus, ad requests as queries. MMR retrieval balances similarity/diversity. 5-10x resource efficiency over linear scaling. 1% CTR lift, 1.2% CVR lift on Facebook Feed and Reels at 365+ day retention.
- **Key Innovations**: RAG for long-history scaling in ads; MMR-based personalization retrieval; production with sub-10ms latency.

### 37. Dual-Stream MLP for CTR Prediction (DS-MLP)
- **Authors**: RUCAIBox
- **Institution**: Renmin University of China
- **Link**: https://arxiv.org/abs/2606.04944
- **Abstract**: Knowledge distillation consolidates explicit feature interaction into a main MLP, while parallel MLP captures implicit interactions. Alignment strategies for compatibility. Vanilla MLP achieving SOTA across three benchmarks.
- **Key Innovations**: Knowledge distillation for explicit/implicit dual-stream; vanilla MLP achieving SOTA; efficient and scalable.

### 38. EST: Towards Efficient Scaling Laws in CTR via Unified Modeling
- **Authors**: Zhang et al. (Taobao)
- **Institution**: Alibaba (Taobao)
- **Link**: https://arxiv.org/abs/2602.10811
- **Abstract**: Fully unified Transformer modeling raw inputs across modalities without lossy aggregation. Lightweight Cross-Attention (LCA) pruning redundant self-interactions. Scaling laws shown. Deployed on Taobao display ads: +3.27% RPM, +1.22% CTR.
- **Key Innovations**: Unified raw input modeling for CTR; LCA for efficient scaling; production scaling law validation.

### 39. GR4AD: Generative Recommendation for Large-Scale Advertising
- **Authors**: Multiple authors (Kuaishou)
- **Institution**: Kuaishou
- **Link**: https://arxiv.org/abs/2602.22732
- **Abstract**: Production generative recommender for real-time advertising. UA-SID from fine-tuned MLLM, VSL + RSPO (ranking-guided list-wise RL), LazyAR decoder, Dynamic Beam Serving. Up to 4.2% ad revenue improvement, <100ms latency at 500+ QPS. Deployed serving 400M+ users.
- **Key Innovations**: First production generative recommender for ads; MLLM-based SID; list-wise RL for advertising; dynamic beam serving.

### 40. LLaTTE: Scaling Laws for Multi-Stage Sequence Modeling in Ads
- **Authors**: Multiple authors (Meta)
- **Institution**: Meta
- **Link**: https://arxiv.org/abs/2601.20083
- **Abstract**: Demonstrates power-law scaling for sequence modeling in recommendation. Semantic features enable scaling. Two-stage architecture: async upstream user model (large/long) + compact downstream ranker. 4.3% conversion uplift on Facebook Feed and Reels. Largest user model at Meta.
- **Key Innovations**: Scaling laws for recommendation sequence modeling; two-stage architecture; upstream user model with fixed-bandwidth bottleneck.

### 41. GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning
- **Authors**: Multiple authors
- **Institution**: — (WWW 2026)
- **Link**: https://arxiv.org/abs/2601.18251
- **Abstract**: Generative user intent framework using semantic interest cohorts. Hierarchical quantization organizes items into cohorts; generative sequential model for dual-aspect user intent.
- **Key Innovations**: Generative cohort-based intent for CTR; candidate-agnostic cohort representations.

### 42. Field-Aware Transformer (FAT): From Scaling to Structured Expressivity for CTR
- **Authors**: Multiple authors
- **Institution**: — (KDD 2026)
- **Link**: https://arxiv.org/abs/2511.12081
- **Abstract**: Identifies structural misalignment: Transformers assume sequential compositionality, CTR needs combinatorial reasoning over fields. FAT with Basis-Composed Hypernetwork. Up to +4.38% AUC, +2.33% CTR, +0.66% RPM in production.
- **Key Innovations**: Field-centric Transformer for combinatorial reasoning; Rademacher complexity-based scaling law.

### 43. PRECTR-V2: Unified Relevance–CTR Framework
- **Authors**: Chen et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2602.20676
- **Abstract**: Unified framework for search relevance + CTR. Mines global relevance for cold-start users, hard negatives via embedding noise for exposure bias correction, LLM-distilled transformer encoder replacing frozen BERT.
- **Key Innovations**: Global relevance mining for cold-start; LLM-distilled encoder for CTR; exposure bias correction.

### 44. HeMix: Query-Mixed Interest Extraction and Heterogeneous Interaction
- **Authors**: Zheng Chai et al. (AMAP, Alibaba)
- **Institution**: AMAP (Alibaba)
- **Link**: https://arxiv.org/abs/2602.09387
- **Abstract**: Scalable CTR with Query-Mixed Interest Extraction and HeteroMixer block. Deployed on AMAP: +3.61% GMV, +2.78% PV_CTR.
- **Key Innovations**: Query-mixed attention; heterogeneous interaction blocks; billion-scale deployment.

### 45. SparseCTR: Sparse Attention on Long-term Behaviors for CTR
- **Authors**: Lai Wei Jiang et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2601.17836
- **Abstract**: Three-branch sparse self-attention: global interests, interest transitions, short-term interests. Personalized chunking, composite relative temporal encoding. +1.72% CTR, +1.41% CPM online. Scaling across 3 OOM FLOPs.
- **Key Innovations**: Three-branch sparse attention; personalized temporal chunking; scaling law in CTR.

### 46. LLM-HYPER: Generative CTR for Cold-Start Ads via LLM Hypernetworks
- **Authors**: Multiple authors (US e-commerce platform)
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2604.12096
- **Abstract**: Uses LLMs as hypernetworks to generate CTR model weights training-free. Few-shot CoT prompting over multimodal ad content infers feature weights. +55.9% NDCG@10 over cold-start baselines. Deployed in production on top US e-commerce platform.
- **Key Innovations**: LLMs as hypernetworks for cold-start CTR; training-free weight generation; production deployment for cold-start ads.

---

## Recommendation Systems — Scaling & Architectures

### 47. Gryphon: Unified SID Generation and Item-Level Scoring for Industrial Rec
- **Authors**: Multiple authors
- **Institution**: — (Industrial music service)
- **Link**: https://arxiv.org/abs/2606.08604
- **Abstract**: Encoder-decoder generative recommendation with jointly trained item-level scoring alongside SID generation. Resolves beam search miscalibration and SID collision. Highest item-level Recall@1000. Replaced 15+ candidate generators as sole candidate source in 7-day A/B test with no significant change.
- **Key Innovations**: Item-level scoring in generative retrieval; resolves beam-SID mismatch; replaces whole candidate generation pipeline.

### 48. Beyond Item IDs: Semantic-Native Long Sequence Modeling for Video Rec
- **Authors**: Multiple authors (SIGIR 2026)
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.07546
- **Abstract**: Production framework for ultra-long user sequences at billion-user scale using content-native Semantic IDs. Global-Aware Compression Transformer with non-parametric temporal folding for memory/compute reduction. Order-of-magnitude peak memory reduction. Deployed in production A/B.
- **Key Innovations**: Semantic IDs replacing Video IDs at billion-user scale; Global-Aware Compression Transformer; cold-start generalization via shared prefixes.

### 49. Kunlun: Scaling Laws for Massive-Scale Recommendation
- **Authors**: Multiple authors (Meta)
- **Institution**: Meta
- **Link**: https://arxiv.org/abs/2602.10016
- **Abstract**: Unified architecture establishing scaling laws for joint sequence-nonsequence modeling. GDPA, Hierarchical Seed Pooling, Sliding Window. CompSkip + Event-level Personalization. MFU from 17% to 37% on B200. 2x scaling efficiency. Deployed in major Meta Ads models.
- **Key Innovations**: First predictable scaling laws for joint sequence-nonsequence rec; MFU optimization; production impact at Meta.

### 50. TokenMixer-Large: Scaling Up Ranking Models in Industrial Recommenders
- **Authors**: Multiple authors (ByteDance)
- **Institution**: ByteDance
- **Link**: https://arxiv.org/abs/2602.06563
- **Abstract**: Evolved from TokenMixer: mixing-and-reverting, inter-layer residuals, Sparse Per-token MoE. Scales to 7B online / 15B offline. +1.66% orders, +2.98% GMV for e-commerce; +2.0% ADSS in advertising. Deployed in multiple ByteDance scenarios.
- **Key Innovations**: Extreme-scale ranking model; mixing-and-reverting for deep models; sparse MoE for industrial rec.

### 51. ULTRA-HSTU: Bending Scaling Curves in Recommendation
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2602.16986
- **Abstract**: Next-gen HSTU with Mixture of Transducers (MoT), sparse attention, optimized topology. 5x faster training scaling, 21x faster inference scaling. 4-8% consumption and engagement improvements. Serving billions of users daily.
- **Key Innovations**: MoT for heterogeneous user signals; ultra-efficient scaling (5x/21x); production at billion-user scale.

### 52. GenRec: Preference-Oriented Generative Framework for Large-Scale Rec
- **Authors**: Multiple authors (JD)
- **Institution**: JD
- **Link**: https://arxiv.org/abs/2604.14878
- **Abstract**: Generative retrieval deployed on JD App. Page-wise NTP task, asymmetric linear Token Merger for SID compression, GRPO-SR with Hybrid Rewards. 9.5% click + 8.7% transaction improvements in online A/B.
- **Key Innovations**: Page-wise NTP for generative rec; token merger for SID compression; GRPO with hybrid rewards.

### 53. UniMixer: Unified Architecture for Scaling Laws in Recommendation
- **Authors**: Multiple authors (Kuaishou)
- **Institution**: Kuaishou
- **Link**: https://arxiv.org/abs/2604.00590
- **Abstract**: Unifies attention-based, TokenMixer-based, and FM-based methods under single framework. Parameterized rule-based TokenMixer, Sparse-Pertoken MoE, Siamese norm. Best parameter and compute efficiency. Deployed across multiple Kuaishou scenarios.
- **Key Innovations**: Unified theoretical framework bridging attention/TokenMixer/FM; parameterized mixing; best scaling efficiency.

### 54. RankElastor: Mitigating Embedding Collapse for Dense Scaling in Rec
- **Authors**: Vasile Paskar et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2605.23191
- **Abstract**: Identifies embedding collapse in RankMixer (low effective rank). Proposes Parameterized Full Mixing + GLU-improved P-FFNs with provable collapse mitigation. Spectrum-robust embeddings. Better scaling than RankMixer.
- **Key Innovations**: Embedding collapse diagnosis in deep recommenders; provable collapse mitigation; spectral robustness.

### 55. LoopFM: Learning from Historical Representations of Foundation Model
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2605.29280
- **Abstract**: Opens high-bandwidth transfer channel from FM to VM by structuring FM intermediate embeddings as input features. ~2x knowledge transfer ratio vs KD. +0.5% to +1.22% conversion improvement in trillion-parameter FM production systems.
- **Key Innovations**: Structured FM embeddings as input features; theoretical gain decomposition; industrial-scale trillion-parameter FM transfer.

### 56. Representation Curriculum: Stagewise Training for Robust Ranking
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.09891
- **Abstract**: Semantics-aware training-time intervention staging feature utilization: foregrounds content-based merit, then introduces exposure-dependent signals while anchoring content pathway. Closed-form solution in Gaussian linear ridge setting. Online A/B in e-commerce search: increases cold-start exposure with neutral KPIs.
- **Key Innovations**: Stagewise curriculum for ranking features; closed-form analysis; cold-start improvement with neutral head performance.

### 57. Principled Synthetic Data for LLM Scaling Laws in Recommendation
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2602.07298
- **Abstract**: Layered framework for synthetic recommendation data. Sequential models trained on synthetic data outperform real-data models by +130% recall@100. First demonstration of robust power-law scaling for LLMs continually pre-trained on recommendation data (0.6B to 8B, 163B tokens).
- **Key Innovations**: First scaling laws for LLMs in recommendation; synthetic data curriculum; asymmetric synergy between data layers.

---

## Recommendation — Sequential Modeling

### 58. GenAIR: Generative Archetype-Grounded Item Representations
- **Authors**: Yifan Li et al. (CUHK)
- **Institution**: The Chinese University of Hong Kong
- **Link**: https://arxiv.org/abs/2606.11023
- **Abstract**: Uses LLMs to infer "Archetype" text (ideal target audience for each item), extracts embeddings, calibrates with behavioral signals. Seamless integration with existing models. **WWW 2026 Oral.**
- **Key Innovations**: Archetype-grounded item representations; behavioral calibration bridging semantic-behavioral gap.

### 59. MARS: Multi-rate Aggregation of Recency Signals for Sequential Rec
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.03718
- **Abstract**: Encoder-agnostic aggregation operator consuming real timestamps, producing K summaries at distinct recency scales with context-adaptive gate. Automatically selects Transformer (sparse data) or Mamba (dense data). Mean relative gain +19.7% over Transformer baselines on sparse data.
- **Key Innovations**: Multi-scale temporal aggregation; automatic encoder selection (T/M); Pareto frontier across data density.

### 60. HoloMambaRec: Scalable Sequential Rec under Latency/Memory Constraints
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2601.08360
- **Abstract**: Combines holographic reduced representations for attribute-aware embedding with selective SSM (Mamba) for linear-time sequence processing. Surpasses SASRec on Beauty and ML-1M with lower memory complexity. Constant-time recurrent inference.
- **Key Innovations**: Holographic attribute binding + SSM for rec; linear-time inference; practical for production latency constraints.

### 61. PHKT: Personalized Hypergraph KAN-Transformer for Multi-behavior Rec
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.05537
- **Abstract**: Personalized dynamic hypergraph with behavior-aware weighting + KAN replacing MLP in Transformer FFN. Captures user-specific heterogeneous high-order relationships. Outperforms 9 baselines on Tmall, RetailRocket, IJCAI.
- **Key Innovations**: Personalized dynamic hypergraph for multi-behavior; KAN-Transformer fusion; behavior-aware weights.

### 62. MCARec: Selective SSM with Collaborative Awareness for Sequential Rec
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://doi.org/10.3390/mca31020046
- **Abstract**: Integrates selective SSM with collaborative awareness module: lightweight attention for item co-occurrence, context-aware adaptive gating. On ML-1M: +3.89% HR@10, +5.52% NDCG@10 over Mamba4Rec.
- **Key Innovations**: Collaborative awareness for SSM-based rec; context-adaptive gating; strong results on dense data.

### 63. SS4Rec: Continuous-Time Sequential Rec with State Space Models
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2502.08132
- **Abstract**: Hybrid SSM combining time-aware SSM (irregular intervals) + relation-aware SSM (contextual dependencies). Variable stepsize discretization for continuous-time modeling. Strong results on 5 benchmark datasets.
- **Key Innovations**: Continuous-time SSM for sequential rec; variable stepsize for irregular intervals; dual time/relation SSM.

### 64. ManCAR: Manifold-Constrained Latent Reasoning for Sequential Rec
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2602.20093
- **Abstract**: Grounds latent multi-step reasoning within interaction graph topology as manifold constraint. Variational interpretation (ELBO-like) balancing target prediction with reasoning feasibility. Graph-induced neighborhood as structure-aware prior.
- **Key Innovations**: Manifold constraint for latent reasoning in rec; variational interpretation; graph-grounded intermediate states.

### 65. GrIT: Group Informed Transformer for Sequential Recommendation
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2602.19728
- **Abstract**: Models temporally evolving group features alongside individual user histories. Time-varying membership weights derived from short/long-term windows. Jointly captures personal and group-level temporal dynamics. Strong on 5 benchmarks.
- **Key Innovations**: Dynamic group modeling for sequential rec; time-varying membership weights; joint individual-group representations.

### 66. SpecTran: Spectral-Aware Transformer Adapter for LLM-Enhanced Rec
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2601.21986
- **Abstract**: Spectral-domain transformer adapter projecting LLM embeddings into item space. Learnable spectral-position encoding with singular-value inductive bias. Avg 9.17% improvement across 4 datasets and 3 backbones.
- **Key Innovations**: Spectral-domain adapter for LLM-rec alignment; singular-value positional encoding; adaptive spectral aggregation.

### 67. RoTE: Multi-Level Rotary Time Embedding for Sequential Rec
- **Authors**: Xiao Longtao et al.
- **Institution**: — (SIGIR 2026)
- **Link**: https://arxiv.org/abs/2604.13389
- **Abstract**: Decomposes interaction timestamps into multiple temporal granularities (coarse to fine). Lightweight plug-and-play module for Transformer-based sequential rec. Up to 20.11% NDCG@5 improvement.
- **Key Innovations**: Multi-granularity time decomposition for rec; plug-and-play temporal embedding; SIGIR 2026.

### 68. Mixture of Sequence (MoS): Theme-Aware MoE for Long-Sequence Rec
- **Authors**: Xiaolin et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2604.20858
- **Abstract**: Model-agnostic MoE addressing "session hopping" in long sequences. Theme-aware routing + multi-scale fusion (global, short-term, theme-specific experts). Consistent improvements with fewer FLOPs than alternative MoE.
- **Key Innovations**: Theme-aware routing for long sequences; session hopping identification; efficient MoE for rec.

---

## Time Series & Sequential Modeling

### 69. Trio: Time-Series Forecasting with Temporal-Spatial-Sample Attention
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.07291
- **Abstract**: Sample-aware forecasting with 3D attention: temporal, spatial, sample dimensions. TS-SCM generator creates structured synthetic tasks with dynamic lags, drift, feedback.
- **Key Innovations**: Sample attention for time series; structural causal model for synthetic pre-training.

### 70. FAiT: Frequency-Aware Inverted Transformer for Multivariate TS
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.01306
- **Abstract**: Addresses spectral bias (low-pass). Inverted Attention: high-pass branch by inverting attention matrix. DTFM for instance-conditioned spectral re-calibration.
- **Key Innovations**: Inverted attention for high-frequency recovery; DTFM for adaptive spectral modulation.

### 71. TiWeaver: Unified Temporal Dynamics via Contextual Patching
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.03121
- **Abstract**: Unified irregular multivariate TS framework. Graph-Guided Adaptive Tokenizer + Fine-grained Asynchronous Dependency Extractor. Up to 25% improvement on 12 datasets.
- **Key Innovations**: Graph-guided adaptive patching; fine-grained asynchronous cross-channel modeling.

### 72. Falcon-X: Time Series Foundation Model (591M)
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2605.27286
- **Abstract**: Decouples variates into latent prototype space. Unified Prototype Diff-Attention for synergistic/antagonistic relationships. Encoder-only TSFM. Zero-shot structural transfer.
- **Key Innovations**: Latent prototype space for heterogeneous TS; Diff-Attention for positive/negative affinities.

### 73. SARAF: Stationarity-Aware Retrieval-Augmented TS Forecasting (KDD 2026)
- **Authors**: Shiqiao Zhou et al.
- **Institution**: — (KDD 2026)
- **Link**: https://arxiv.org/abs/2606.04135
- **Abstract**: RAG-inspired TS forecasting with diversity-aware selection covering heterogeneous historical regimes. Modulates diversification by stationarity. Effective under regime shifts.
- **Key Innovations**: Stationarity-modulated retrieval diversity; RAG for time series with non-stationarity.

### 74. TimeClaw: Agentic Harness for Contextualized Time Series
- **Authors**: Multiple authors
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.05404
- **Abstract**: Agentic framework equipping LLM agents with TS-native runtime: executable temporal tools, experience-driven capability evolution, episodic multimodal memory.
- **Key Innovations**: Agentic TS reasoning with executable tools; capability evolution via experience.

### 75. Diffusion Models for Adaptive Sequential Data Generation
- **Authors**: Yinbin Han et al.
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.06007
- **Abstract**: Sequential forward-backward diffusion for adapted time series generation. Conditions on generated history. Statistical guarantees for score approximation/estimation.
- **Key Innovations**: First diffusion model with statistical guarantees for sequential data; adaptiveness preserving temporal structure.

---

## Summary of Trends

1. **MoE scaling hit a milestone**: 120B MoE trained on a single 8-GPU node (LightningLM) with reversible computing and state-preserving growth.
2. **Attention alternatives proliferate**: DCT mixing (CHIAR-Former), KRR token mixing (Cubit), sparse associative memory (PCAF), anchored recurrent core (CART), content-addressed memory.
3. **KV cache optimization is urgent**: Projective sharing achieves up to 96.9% KV cache reduction — critical for long-context inference.
4. **Latent reasoning gains traction**: NF-CoT (normalizing flows), ManCAR (manifold-constrained), and ThoughtFold (step-level folding) all extend reasoning into continuous/latent spaces.
5. **LLM agent memory converges on hybrid approaches**: Engram, LANTERN, and MRAgent demonstrate retrieval + structured memory beats full-history replay.
6. **RL for black-box agents becomes feasible**: Agentic Monte Carlo (ICML 2026) uses SMC to optimize proprietary API models without parameter access.
7. **LLM RL training challenges the pipeline**: RL is effective mid-pre-training (RL Excursions); EvoTrainer co-evolves policies and harnesses autonomously.
8. **CTR scaling shifts from parameters to computation**: LoopCTR (loop scaling), DeRes (steeper scaling law), LLaTTE (two-stage architecture) — computation-scaling emerges as alternative to parameter-scaling.
9. **CTR/Advertising adopts decoder-only and generative paradigms**: CADET (LinkedIn), GR4AD (Kuaishou), LLM-HYPER (cold-start) — generative and Transformer-based approaches go to production.
10. **RAG and FM distillation enter production recommendation**: Memento (Meta, RAG for 365+ day history), LoopFM (trillion-param FM distillation), Representation Curriculum.
11. **Recommendation scaling laws become practical**: Kunlun (Meta), TokenMixer-Large (ByteDance), UniMixer (Kuaishou), ULTRA-HSTU — major platforms publish scaling laws.
12. **LLM scaling laws for recommendation established**: Principled synthetic data enables first power-law scaling for LLM continual pre-training on rec data (0.6B to 8B).
13. **Sequential rec embraces SSMs**: MARS, HoloMambaRec, MCARec, SS4Rec — selective state-space models compete with Transformers in rec, offering linear complexity.
14. **Time series sees foundation model and agentic advances**: Falcon-X (591M), FAiT (frequency-aware), TimeClaw (agentic TS).
15. **CoT reasoning deepens**: BAPO bounds (theoretical limits), ReasoningFlow (discourse DAGs), CUSUM-based early exit, Streaming MA (step-level scaling laws) — the community gains deeper understanding of reasoning.
16. **Games as training ground for LLMs**: GIFT, MemoPilot, Odysseus, Strat-Reasoner — games increasingly used as environments for RL-based LLM training and evaluation.
