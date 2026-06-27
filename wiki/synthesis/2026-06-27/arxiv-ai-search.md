---
title: "arXiv AI Research Scan — June 2026"
type: synthesis
created: 2026-06-27
updated: 2026-06-27
tags: [arxiv, survey, llm, ctr, recommendation, games, rl, sequence-modeling, attention]
---

# arXiv AI Research Scan — June 2026

> Weekly scan of recent preprints across AI, LLMs, recommendation, CTR, sequential modeling, and games. Papers primarily from late May–June 2026.

---

## LLMs & Foundation Models

### Ling and Ring 2.6 Technical Report: Efficient and Instant Agentic Intelligence at Trillion-Parameter Scale
- **Authors**: Ant Group (100+ authors including Ang Li, Ben Liu, Bin Han, et al.)
- **Institution**: Ant Group
- **Link**: [arXiv:2606.15079](https://arxiv.org/abs/2606.15079)
- **Abstract**: Introduces Ling-2.6 (instant response) and Ring-2.6 (deep reasoning) model family at 104B–1T parameters. Upgrades Ling-2.0 via architectural migration pre-training. Key innovations: hybrid linear attention (Lightning Attention + MLA), Evolutionary Chain-of-Thought, Linguistic Unit Policy Optimization, and KPop RL framework for stable training at 1T scale on environment-grounded data. All checkpoints open-sourced.
- **Key Innovations**: Hybrid linear attention architecture; token efficiency via Evolutionary CoT; KPop RL for trillion-parameter agent training.

### Abstract Representational Geometry Supports Inference in Large Language Models
- **Authors**: Yunan Zeng et al.
- **Institution**: N/A
- **Link**: [arXiv:2606.23345](https://arxiv.org/abs/2606.23345)
- **Abstract**: Adapts contextual reversal-learning paradigm to text and compares humans vs LLMs. Finds LLMs exhibit abstract geometric structures resembling hippocampus when inference occurs. Geometry organized hierarchically: lower layers encode stimulus identity, higher layers form hippocampal-like context geometry. Geometric regularization of higher layers increases generalizable inference.
- **Key Innovations**: Mechanistic link between abstract representational geometry and LLM reasoning; hierarchical depth analysis; geometric regularization intervention.

### SciOrch: Learning to Orchestrate Expert LLMs for Solving Frontier Multimodal Scientific Reasoning Tasks
- **Authors**: Jingru Guo, Xiangyuan Xue, Lian Zhang, Wanghan Xu, Siki Chen, Philip Torr, Wanli Ouyang, Lei Bai, Zhenfei Yin
- **Institution**: Multiple (includes Philip Torr — Oxford)
- **Link**: [arXiv:2606.15872](https://arxiv.org/abs/2606.15872)
- **Abstract**: Trains a lightweight 8B VLM as orchestrator that decomposes scientific questions, delegates sub-problems to commercial frontier models, and synthesizes final answer. Uses MCTS-based offline trajectory generation + GRPO-style training. On 240-question test set achieves 56.66% accuracy, outperforming strongest single commercial model by 3.74%.
- **Key Innovations**: MCTS makes RL tractable for expensive API-call orchestration; offline gradient updates decouple training from API latency.

### UniAR: Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer
- **Authors**: Wujian Peng et al.
- **Institution**: N/A
- **Link**: [arXiv:2606.18249](https://arxiv.org/abs/2606.18249)
- **Abstract**: Unified autoregressive framework using a single discrete visual tokenizer as bridge between understanding and generation. Adapts pretrained vision encoder with multi-level feature fusion and lookup-free bitwise quantization. Parallel-bitwise-prediction jointly predicts spatially grouped multi-level visual codes, reducing sequence length. Diffusion-based decoder for high-fidelity images. SOTA on image generation/editing while competitive on understanding.
- **Key Innovations**: Single shared visual tokenizer for both understanding and generation; lookup-free bitwise quantization; parallel-bitwise-prediction.

### LLMZero: Discovering Adaptive Training Strategies for RL Post-Training via LLM Agents
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2606.18388](https://arxiv.org/abs/2606.18388)
- **Abstract**: LLM agents search over training trajectories via tree search, diagnosing pathologies at each checkpoint and proposing coordinated multi-parameter transitions. Discovers structural principle: capacity parameters accumulate monotonically, regularization parameters oscillate. Across 4 GRPO tasks, improves over base by 9–140% relative and over grid search by 6–15%.
- **Key Innovations**: Automated discovery of multi-stage training strategies; tree-search over training trajectories; identified capacity/regularization asymmetry principle.

### Structured Inference with Large Language Gibbs
- **Authors**: Sanghyeok Choi et al.
- **Institution**: N/A
- **Link**: [arXiv:2606.19264](https://arxiv.org/abs/2606.19264)
- **Abstract**: Uses LLM conditional distributions as transition operators in Gibbs sampling for structured probabilistic inference. Iteratively resamples individual variables conditioned on others rather than single-pass autoregressive generation. Avoids order-dependent biases. Applied to synthetic distributions, consistent reasoning, and Bayesian structure learning.
- **Key Innovations**: MCMC with LLM conditionals for structured inference; stationary distribution reflects compromise between local conditionals.

### MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery
- **Authors**: Enze Ma et al.
- **Institution**: N/A
- **Link**: [arXiv:2606.24595](https://arxiv.org/abs/2606.24595)
- **Abstract**: Benchmark evaluating long-term agent memory by reconstructing hidden user state from memory artifacts post-interaction. 50 simulated users × 31 hidden dimensions (1,550 recovery targets). Tests 5 memory systems. Finds task completion and recoverable memory are distinct capabilities — category-balanced recovery ~0.6 even when task success near-saturates.
- **Key Innovations**: First benchmark for direct memory recovery auditing; reveals separation between task success and memory fidelity.

---

## LLM Inference Efficiency

### SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference
- **Authors**: Yaosheng Fu et al.
- **Institution**: N/A
- **Link**: [arXiv:2606.04511](https://arxiv.org/abs/2606.04511)
- **Abstract**: Introduces fourth per-layer projection (Forecast) alongside QKV. Forecast predicts KV blocks needed by next layer, enabling lookahead CPU→GPU prefetch overlapping with current-layer execution. One Forecast head per GQA group. Adds <0.5% parameters. On sparse-pretrained 8B models: 1.25× prefill speedup, 1.7× decode speedup, up to 5.3× higher decode throughput.
- **Key Innovations**: Decoupled sparse attention architecture; Forecast-based lookahead selection; overlaps I/O with computation.

### Keyless Attention: Value-Space Routing and Value-Only Caching for Efficient Transformers
- **Authors**: Xin Gao
- **Institution**: N/A
- **Link**: [arXiv:2606.21848](https://arxiv.org/abs/2606.21848)
- **Abstract**: Eliminates key projection entirely — attention scores computed directly between queries and values. Value-Only Cache reduces KV cache by exactly 50%. Introduces Depth-m Attention Factorization (standard attention = depth-2, Keyless = depth-3 QVV). Matches/exceeds perplexity on 4/5 models tested (GPT-2, Pythia, Qwen2, Llama 3.2).
- **Key Innovations**: Keyless attention; Value-Only Cache (50% KV reduction); Depth-m Attention Factorization.

### Neural Attention Search Linear: Towards Adaptive Token-Level Hybrid Attention Models
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2602.03681](https://arxiv.org/abs/2602.03681)
- **Abstract**: Applies both linear and softmax attention within the same layer on different tokens. Automatically determines whether each token can be handled by linear attention or needs softmax attention. Jointly learns optimal attention operations with model weights. Uses Gated DeltaNet and softmax combinations across tokens.
- **Key Innovations**: Token-level adaptive hybrid attention; joint search of attention operations and model weights.

---

## Sequence Modeling & Architecture

### Parallel Hybrid Architecture (PHA): GSS-Transformer Hybrid with Learnable Mixing
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2606.16093](https://arxiv.org/abs/2606.16093)
- **Abstract**: Runs Gated State Spaces (GSS), Grouped Query Attention (GQA), and FFNs as independent parallel branches fused by learnable mixing. GSS captures global context; attention performs selective retrieval. On WikiText-103: 16.51 PPL at 125M, outperforming Hedgehog (16.70) and H3 (23.70). 24% higher throughput, 40% lower memory at long contexts.
- **Key Innovations**: Parallel (not serial) SSM + attention hybridization; learnable static mixing weights; complementary specialization of branches.

### The Recurrent Transformer: Greater Effective Depth and Efficient Decoding
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2604.21215](https://arxiv.org/abs/2604.21215)
- **Abstract**: Each layer attends to KV pairs computed off its own activations, creating layerwise recurrent memory. Preserves standard autoregressive decoding cost. Exact tiling-based algorithm reduces HBM traffic from O(N²) to O(N log N). On 150M/300M C4 pretraining improves cross-entropy over parameter-matched Transformer with fewer layers.
- **Key Innovations**: Layerwise recurrence within Transformer; I/O-aware tiling algorithm for practical training; depth–width trade-off shift.

### Native Hybrid Attention (NHA) for Efficient Sequence Modeling
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2510.07019](https://arxiv.org/abs/2510.07019)
- **Abstract**: Unifies linear RNN (long-term context in KV slots) and sliding window attention (short-term) within a single softmax attention operation. Single hyperparameter (window size) controls inter-layer behavior. Surpasses Transformers and hybrids on recall-intensive and commonsense reasoning tasks. Pretrained LLMs can be adapted with brief finetuning.
- **Key Innovations**: Unified intra-layer hybrid of linear RNN + SWA; single softmax over combined slots; chunkwise-parallel Triton kernel.

### Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2603.08859](https://arxiv.org/abs/2603.08859)
- **Abstract**: Proves pure SSMs require large internal state for a broad class of tasks, and pure Transformers require large window scaling linearly with context length. Constructs shallow hybrid models whose size scales logarithmically with task size using only sublinear memory. Theoretical analysis of memory-computation tradeoffs.
- **Key Innovations**: Formal expressivity lower bounds for pure SSMs and Transformers; provably efficient shallow hybrid construction.

### Sessa: Selective State Space Attention
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2604.18580](https://arxiv.org/abs/2604.18580)
- **Abstract**: Places attention inside a recurrent feedback path, creating multiple attention-based paths for past→future influence. Proves power-law memory tails O(ℓ⁻ᵝ) with slower decay than Transformer/Mamba. Sessa achieves flexible selective retrieval (including non-decaying profiles). Strongest on long-context benchmarks among matched models.
- **Key Innovations**: Attention inside recurrent feedback; provable power-law memory; flexible selective retrieval profiles.

---

## CTR Prediction

### DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2606.07980](https://arxiv.org/abs/2606.07980)
- **Abstract**: Dual-path residual design for CTR Transformers: Identity residual path (first-order feature reuse, gradient flow) + Block Attention Residual path (cross-layer attention over compressed prior outputs). Vector-wise gate controls path weighting. Pointwise AttnRes replaces Softmax with SiLU for parallel multi-interest patterns. Up to +0.32% AUC at <5% additional FLOPs on 331M-interaction industrial dataset. Scaling law γ=0.118 vs 0.071 for OneTrans (1.66× steeper).
- **Key Innovations**: Dual-path residual (Identity + Block Attention); SiLU-based cross-layer attention; steeper compute–AUC scaling law (8-layer matches 16-layer OneTrans).

### Dual-Stream MLP (DS-MLP) is All You Need for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution**: Renmin University of China, ByteDance, Meituan
- **Link**: [arXiv:2606.04944](https://arxiv.org/abs/2606.04944)
- **Abstract**: Proposes DS-MLP with dual streams for explicit and implicit feature interaction learning. Uses gated mechanisms at each interaction order to dynamically filter and emphasize features. Consistent outperformance across three CTR benchmarks.
- **Key Innovations**: Dual-stream architecture for explicit + implicit interactions; gated multi-order interaction filtering.

### HeMix: Query-Mixed Interest Extraction and Heterogeneous Interaction for Industrial CTR
- **Authors**: N/A
- **Institution**: AMAP (Alibaba)
- **Link**: [arXiv:2602.09387](https://arxiv.org/abs/2602.09387)
- **Abstract**: Query-Mixed Interest Extraction for joint global/real-time interest modeling + HeteroMixer block (multi-head token fusion, heterogeneous interaction, group-aligned reconstruction). Deployed on AMAP platform: +3.61% GMV, +2.78% PV_CTR, +2.12% UV_CVR online.
- **Key Innovations**: Query-Mixed Interest tokenizer; HeteroMixer as self-attention alternative; billion-scale deployment results.

### LoopCTR: Loop Scaling Paradigm for CTR Prediction
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2604.19550](https://arxiv.org/abs/2604.19550)
- **Abstract**: Sandwich architecture (Entry Block → Loop Block → Prediction Block). Loop Block uses Hyper-Connected Residuals + MoE for iterative reasoning. Process supervision at every loop depth. Train-multi-loop, infer-zero-loop matches/exceeds full multi-loop inference. Oracle analysis reveals 0.02–0.04 AUC untapped headroom.
- **Key Innovations**: Loop scaling paradigm for CTR; Hyper-Connected Residuals; process supervision; train-multi-loop/infer-zero-loop strategy.

### SparseCTR: Sparse Attention on Long-term Behaviors for CTR Prediction
- **Authors**: N/A (code at github.com/laiweijiang/SparseCTR)
- **Institution**: N/A
- **Link**: [arXiv:2601.17836](https://arxiv.org/abs/2601.17836)
- **Abstract**: Personalized time-aware chunking (TimeChunking) + three-branch sparse self-attention (global/transition/local) for long-term user behavior modeling. Composite relative temporal encoding with learnable head-specific bias. Exhibits scaling law across three orders of magnitude FLOPs. Online: +1.72% CTR, +1.41% CPM.
- **Key Innovations**: Personalized time-aware chunking; evolutionary sparse self-attention (EvoAttention); composite relative temporal encoding.

### GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2601.18251](https://arxiv.org/abs/2601.18251)
- **Abstract**: Generative user intent framework using semantic interest cohorts. Transformer generative model with next-item-prediction (NTP) produces candidate interest cohorts. Hierarchical candidate-aware network refines cohorts via cross-attention. End-to-end training with self-supervised regularization.
- **Key Innovations**: Generative (not discriminative) intent modeling; semantic interest cohorts as candidate-agnostic user intent representation; recall-ranking consistency.

### SIF: Sample Is Feature — Sample-Level Tokens for Unified Large Recommender Models
- **Authors**: N/A
- **Institution**: N/A (industrial food delivery platform)
- **Link**: [arXiv:2604.15650](https://arxiv.org/abs/2604.15650)
- **Abstract**: Elevates sequence tokens from item-level to sample-level: each sample in behavior history carries item info + context. Unified Transformer backbone for both sequence modeling and feature interaction. +0.88% GAUC offline, +2.03% CTR and +1.21% CVR online.
- **Key Innovations**: Sample-level (vs item-level) behavior tokens; unified sequence + feature interaction architecture.

### GenAIR: Generative Archetype-Grounded Item Representations for Sequential Recommendation
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2606.11023](https://arxiv.org/abs/2606.11023)
- **Abstract**: Uses LLM to infer textual description of item's ideal target audience ("Archetype"), then extracts embeddings. Behavioral calibration objective bridges gap between semantic space and actual user behavior. Plug-and-play with most existing sequential recommenders.
- **Key Innovations**: LLM-generated archetype descriptions as item representation; behavioral calibration objective; model-agnostic integration.

---

## Games & Reinforcement Learning

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2605.00347](https://arxiv.org/abs/2605.00347)
- **Abstract**: RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Adapted PPO with lightweight turn-level critic — substantially more stable than GRPO/Reinforce++. Pretrained VLMs provide strong action priors. ≥3× average game progress over frontier models. Cross-game generalization maintained.
- **Key Innovations**: PPO + turn-level critic for long-horizon VLM decision-making; systematic ablation of RL components for VLMs; cross-game generalization.

### OpenGame: Open Agentic Coding for Games
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2604.18394](https://arxiv.org/abs/2604.18394)
- **Abstract**: Open-source agentic framework for end-to-end web game creation. Game Skill = Template Skill (library of project skeletons) + Debug Skill (living protocol of fixes). GameCoder-27B: code LLM specialized via continual pre-training + SFT + execution-grounded RL. OpenGame-Bench evaluates on Build Health, Visual Usability, Intent Alignment. SOTA across 150 diverse game prompts.
- **Key Innovations**: First open-source agentic framework for end-to-end game dev; Template + Debug Skill living protocols; execution-grounded RL for code generation.

### Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: N/A (includes A. Sestini et al. — human-like goalkeeping)
- **Institution**: N/A
- **Link**: [arXiv:2606.20210](https://arxiv.org/abs/2606.20210)
- **Abstract**: Vision paper on RL for game AI / NPCs. Proposes framework for training RL models with requirements suited to game AI and development. Discusses bottlenecks: sample efficiency, believable behavior, deployment challenges. Presents examples including human-like goalkeeping in football simulation.
- **Key Innovations**: Framework for RL-based game AI with practical deployment requirements; sample-efficient human-like behavior learning.

### Nemobot Games: Crafting Strategic AI Gaming Agents with LLMs
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2604.21896](https://arxiv.org/abs/2604.21896)
- **Abstract**: Extends Shannon's taxonomy of game-playing machines using LLMs. Interactive environment (Nemobot) for creating LLM-powered game agents across 4 game classes: dictionary-based, solvable, heuristic-based, learning-based. Uses RL with human feedback and self-critique for strategy refinement. Supports tool-augmented generation and fine-tuning.
- **Key Innovations**: LLM operationalization of Shannon's game taxonomy; programmable agentic game environment; RLHF + self-critique for game strategies.

### From Trainee to Trainer: LLM-Designed Training Environment for RL
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2606.17682](https://arxiv.org/abs/2606.17682)
- **Abstract**: LLM-as-Environment-Engineer framework: current policy model analyzes failure trajectories and proposes next-stage training environment modifications. MAPF-FrozenLake testbed with multi-dimensional config generator. Qwen3-4B backbone outperforms larger proprietary LLMs (GPT, Gemini). RL checkpoint serves as better environment engineer than base model.
- **Key Innovations**: Policy model designs its own training environments; structured failure analysis for environment redesign; RL improves self-diagnosis ability.

### MARL-GPT: Foundation Model for Multi-Agent Reinforcement Learning
- **Authors**: N/A (code at github.com/Cognitive-AI-Systems/marl-gpt)
- **Institution**: N/A
- **Link**: [arXiv:2604.05943](https://arxiv.org/abs/2604.05943)
- **Abstract**: Single GPT-based model trained via offline RL on expert trajectories across diverse MARL environments (SMACv2 — 400M, GRF — 100M, POGEMA — 1B). Unified transformer-based observation encoder requiring no task-specific tuning. Competitive/superior performance vs specialized baselines in all environments.
- **Key Innovations**: First generalist foundation model for MARL across significantly different environments; unified encoder without task-specific tuning.

### T-STAR: Tree-structured Self-Taught Agent Rectification for Multi-turn Agent RL
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2604.07165](https://arxiv.org/abs/2604.07165)
- **Abstract**: Consolidates independent RL trajectories into Cognitive Tree by merging functionally similar steps. Introspective Valuation back-propagates rewards through tree for variance-reduced step-level advantage. In-Context Thought Grafting synthesizes corrective reasoning by contrasting successful/failed branches. 3–8% gains on embodied/interactive/reasoning/planning benchmarks.
- **Key Innovations**: Cognitive Tree for correlated reward structure across trajectories; thought grafting for self-rectification; Bradley-Terry surgical loss at critical divergence points.

### Fluid-Agent Reinforcement Learning
- **Authors**: N/A
- **Institution**: N/A
- **Link**: [arXiv:2602.14559](https://arxiv.org/abs/2602.14559)
- **Abstract**: Formalizes fluid-agent environments where agents can create (spawn) other agents. Proposes Partially Observable Fluid Stochastic Games (POFSG) framework; proves existence of NE and SPNE. Fluid variants of Predator-Prey, Level-Based Foraging, and new PuddleBridge environment. Agent teams dynamically adjust size to match task demands.
- **Key Innovations**: First formalization of agent-spawning in MARL; POFSG game-theoretic framework; dynamic team-size adaptation.

---

## Summary of Trends

| Theme | Signal |
|-------|--------|
| **LLM Architecture** | Hybrid SSM+Attention goes mainstream (PHA, NHA, Sessa, Recurrent Transformer). Parallel hybridization outperforms serial. |
| **Inference Efficiency** | KV cache reduction via key elimination (Keyless Attention), sparse decoupled lookahead (SparDA), token-level adaptive attention (NAtS-L). |
| **RL for LLMs** | Automated strategy search (LLMZero), environment self-design (Trainee→Trainer), tree-structured credit assignment (T-STAR). |
| **CTR / Recommendation** | Scaling laws now actively studied in CTR (LoopCTR, DeRes, SparseCTR). Unified Transformers for sequence+feature interaction (SIF, HeMix). Generative approaches to user intent (GenCI, GenAIR). |
| **Games + RL** | VLMs for long-horizon gameplay (Odysseus). Agentic game code generation (OpenGame). Generalist MARL foundation models (MARL-GPT). Fluid/swarm agent populations. |
