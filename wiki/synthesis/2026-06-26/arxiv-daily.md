---
title: "arXiv Daily — 2026-06-26"
type: synthesis
created: 2026-06-26
updated: 2026-06-26
tags: [arxiv-daily, llm, attention, ctr, recommendation, rl, games, transformers, alignment]
---

# arXiv Daily — 2026-06-26

Recent papers across LLMs, efficient attention, CTR prediction, recommendation systems, reinforcement learning, and game-playing agents. Papers primarily from submissions on 20–25 Jun 2026.

---

## 1. LLM Reasoning & Alignment

### 1.1 Self-Compacting Language Model Agents

| Field | Detail |
|-------|--------|
| **Title** | Self-Compacting Language Model Agents |
| **Authors** | Tianjian Li et al. |
| **Institution** | — |
| **arXiv** | [2606.23525](https://arxiv.org/abs/2606.23525) |
| **Date** | 22 Jun 2026 |

**Abstract:** Long agent traces accumulate stale content that anchor subsequent generations and eventually outgrow the context window. Existing scaffolds use fixed-interval compaction at a token threshold, risking discard of partial results mid-derivation. The authors propose SelfCompact, a scaffold pairing (i) a compaction tool the model invokes to summarize accumulated context and (ii) a lightweight rubric specifying when to fire. Together they elicit effective adaptive compaction without fine-tuning. On six benchmarks (math and agentic search) across seven models, SelfCompact matches or exceeds fixed-interval summarization at 30–70% lower token cost.

**Key Innovation:** Model-decides-when-and-how-to-compact scaffold that closes the meta-cognitive gap — unprompted models cannot tell when their own context is rotting, but a lightweight rubric supplies this capability without training.

---

### 1.2 Pigeonholing: Bad Prompts Hurt Models to Collapse and Make Mistakes

| Field | Detail |
|-------|--------|
| **Title** | Pigeonholing: Bad prompts hurt models to collapse and make mistakes |
| **Authors** | Hyunji Alex Nam et al. |
| **Institution** | — |
| **arXiv** | [2606.24267](https://arxiv.org/abs/2606.24267) |
| **Date** | 23 Jun 2026 |

**Abstract:** Bad contexts can cause performance degradation and mode collapse — "pigeonholing" — without malicious jailbreaking intent (e.g., user asks model to justify an incorrect theorem, or context includes the assistant's previous incorrect responses). Experiments across 10 tasks and 10 models show 38–40% performance drops, monotonically worsening with conversation turns. They propose RLVR with synthetic errors, improving models by 43–60% under bad contexts.

**Key Innovation:** Identifies and names "pigeonholing" as a distinct failure mode distinct from jailbreaking; RLVR with synthetic errors as mitigation.

---

### 1.3 Abstract Representational Geometry Supports Inference in LLMs

| Field | Detail |
|-------|--------|
| **Title** | Abstract representational geometry supports inference in large language models |
| **Authors** | Yunan Zeng et al. |
| **Institution** | — |
| **arXiv** | [2606.23345](https://arxiv.org/abs/2606.23345) |
| **Date** | 22 Jun 2026 |

**Abstract:** Adapts a contextual reversal-learning paradigm to text, comparing humans and LLMs. When inference occurs, LLM internal states exhibit abstract geometric structures resembling those reported in the hippocampus — low-dimensional, approximately orthogonal manifolds. This geometry is organized hierarchically: lower layers encode stimulus identity, higher layers form a hippocampal-like functional band. Geometric regularization of higher layers increases emergence of generalizable inference.

**Key Innovation:** First mechanistic evidence that LLMs form abstract representational geometry similar to hippocampus for inference; geometric regularization improves generalization.

---

### 1.4 Words as Difference Makers: How LLMs Determine Causal Structure in Text

| Field | Detail |
|-------|--------|
| **Title** | Words as Difference Makers: How Large Language Models Determine Causal Structure in Text |
| **Authors** | Wolfgang Pietsch |
| **Institution** | — |
| **arXiv** | [2606.22430](https://arxiv.org/abs/2606.22430) |
| **Date** | 21 Jun 2026 |

**Abstract:** Argues LLMs employ variational induction (difference-making logic) to learn causal structure. Analyzes how token embeddings and self-attention realize this logic. The difference-making logic parallels the experimental method — causal relations derived by systematically varying individual circumstances.

**Key Innovation:** Philosophical/mechanistic account connecting LLM causal learning to difference-making logic and experimental methodology.

---

### 1.5 Can Reasoning Models Detect Changes to Their Chains of Thought?

| Field | Detail |
|-------|--------|
| **Title** | Can Reasoning Models Detect Changes to their Chains of Thought? |
| **Authors** | William Walden et al. |
| **Institution** | — |
| **arXiv** | [2606.22085](https://arxiv.org/abs/2606.22085) |
| **Date** | 20 Jun 2026 |

**Abstract:** Studies whether reasoning models can detect interventions on their CoTs (prefilling, editing). Under various conditions — during reasoning, after it, with own vs. other models' CoTs — models exhibit only modest detection accuracy and struggle to identify how their CoT was modified.

**Key Innovation:** Safety-relevant finding: models cannot reliably detect CoT tampering, which has implications for CoT editing, prefilling, and safety interventions.

---

### 1.6 ReasoningLens: Hierarchical Visualization and Diagnostic Auditing for Large Reasoning Models

| Field | Detail |
|-------|--------|
| **Title** | ReasoningLens: Hierarchical Visualization and Diagnostic Auditing for Large Reasoning Models |
| **Authors** | Jiasheng Zheng et al. |
| **Institution** | — |
| **arXiv** | [2606.23404](https://arxiv.org/abs/2606.23404) |
| **Date** | 22 Jun 2026 |

**Abstract:** Open-source framework for hierarchical visualization and diagnostic auditing of complex reasoning chains. Structures traces into interactive hierarchies, uses agentic auditor for automated error detection, synthesizes systemic reasoning profiles to reveal model-specific blind spots.

**Key Innovation:** First framework for structured auditing of long CoT traces from large reasoning models.

---

### 1.7 Distributed Quality-Diversity Search for Toxicity in LLMs

| Field | Detail |
|-------|--------|
| **Title** | Distributed Quality-Diversity Search for Toxicity in Large Language Models |
| **Authors** | Onkar Shelar et al. |
| **Institution** | — |
| **arXiv** | [2606.24166](https://arxiv.org/abs/2606.24166) |
| **Date** | 23 Jun 2026 |

**Abstract:** ToxSearch-S, a speciated evolutionary prompt search for red-teaming with MPI-based parallel workers. Attains competitive peak toxicity with lower cumulative search pressure. MPI distribution delivers ~1.8× with 2 workers and ~3.2× with 4 workers.

**Key Innovation:** Quality-diversity search for adversarial prompt discovery; MPI-parallelized evolutionary red-teaming.

---

## 2. Efficient Transformers & Attention Mechanisms

### 2.1 HydraHead: From Head-Level Functional Heterogeneity to Specialized Attention Hybridization

| Field | Detail |
|-------|--------|
| **Title** | HydraHead: From Head-Level Functional Heterogeneity to Specialized Attention Hybridization |
| **Authors** | Zhentao Tan, Wei Chen, Jingyi Shen, Yao Liu, Xu Shen, Yue Wu, Jieping Ye |
| **Institution** | — |
| **arXiv** | [2606.20097](https://arxiv.org/abs/2606.20097) |
| **Date** | 18 Jun 2026 |

**Abstract:** Hybridizes Full Attention (FA) and Linear Attention (LA) at the head axis rather than layer axis. Uses interpretability-driven selection to preserve FA only for ~6.5% of heads causally critical for retrieval. Scale-normalized fusion reconciles distributional gap between FA and LA. Trained on only 15B tokens from Qwen3-1.7B, achieves >69% improvement over baseline at 512K context, matching a 3:1 layer-wise hybrid at 7:1 LA-to-FA ratio.

**Key Innovation:** Head-level (vs. layer-level) attention hybridization; interpretability-driven FA head selection; 7:1 LA-to-FA compression ratio without quality loss.

---

### 2.2 Complementary Attention Head Pruning for Efficient Transformers (CAHP)

| Field | Detail |
|-------|--------|
| **Title** | Complementary Attention Head Pruning for Efficient Transformers |
| **Authors** | Yaniv Livertovsky et al. |
| **Institution** | — |
| **arXiv** | [2606.19150](https://arxiv.org/abs/2606.19150) |
| **Date** | 17 Jun 2026 |

**Abstract:** Post-hoc framework redefining head selection as a global graph-theoretical problem. Uses graph-based clustering with information-theoretic distance to preserve a topologically diverse subset of complementary heads. Automatically determines pruning ratio via diminishing marginal performance curve. Avoids "proximity bias" of gradient methods that preserve heads mainly in output-near layers.

**Key Innovation:** Graph-theoretic head pruning that preserves functional diversity; automatic pruning ratio selection; avoids proximity bias.

---

### 2.3 Emergent Capabilities Arise Randomly from Learning Sparse Attention Patterns

| Field | Detail |
|-------|--------|
| **Title** | Emergent Capabilities Arise Randomly from Learning Sparse Attention Patterns |
| **Authors** | Rosie Zhao et al. |
| **Institution** | — |
| **arXiv** | [2606.25010](https://arxiv.org/abs/2606.25010) |
| **Date** | 25 Jun 2026 |

**Abstract:** Shows emergent capabilities arise stochastically throughout training, corresponding to abrupt learning of task-relevant attention patterns. On synthetic tasks, difficulty depends on context length and pattern sparsity. Scaling attention heads improves learning efficiency; MLP-Mixer outperforms transformers on tasks with complex attention patterns.

**Key Innovation:** Mechanistic explanation: emergence = difficulty of learning sparse attention patterns; MLP-Mixer advantage for complex positional patterns.

---

### 2.4 Architecture-Aware RL Makes Sliding-Window Attention Competitive in Math Reasoning (SWARR)

| Field | Detail |
|-------|--------|
| **Title** | Architecture-Aware Reinforcement Learning Makes Sliding-Window Attention Competitive in Math Reasoning |
| **Authors** | Kai Liu et al. |
| **Institution** | — |
| **arXiv** | [2606.11634](https://arxiv.org/abs/2606.11634) |
| **Date** | 10 Jun 2026 |

**Abstract:** Two-stage recipe: (1) convert SA → SWA with SFT, (2) policy adaptation with RL. On-policy RL under SWA constraint adapts trajectories to match SWA's limited receptive field, substantially narrowing the SA–SWA gap. Central finding: RL changes the conclusion about SWA's viability for math reasoning.

**Key Innovation:** RL as architecture-aware adaptation for linear-complexity attention; empirical demonstration that RL flips the verdict on SWA viability.

---

### 2.5 Explaining Attention with Program Synthesis

| Field | Detail |
|-------|--------|
| **Title** | Explaining Attention with Program Synthesis |
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2606.19317](https://arxiv.org/abs/2606.19317) |
| **Date** | ~18 Jun 2026 |

**Abstract:** For each attention head, extracts example attention maps, prompts an LM to generate candidate Python programs reproducing those maps, and re-ranks by fit. Across BERT-Base, GPT-2-Small, TinyLlama-1.1B, and Llama-3B, substantial fraction of heads can be approximated with executable programs. Up to 25% of heads replaceable with programs while incurring only 16% perplexity increase.

**Key Innovation:** First programmatic explanations of attention heads that scale to modern LMs; programs can be inserted into live forward passes.

---

### 2.6 Efficiently Representing Algorithms with Chain-of-Thought Transformers

| Field | Detail |
|-------|--------|
| **Title** | Efficiently Representing Algorithms with Chain-of-Thought Transformers |
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2606.19697](https://arxiv.org/abs/2606.19697) |
| **Date** | ~18 Jun 2026 |

**Abstract:** Shows CoT transformers can efficiently simulate Word RAM algorithms with poly-logarithmic overhead (vs. quadratic for Turing machine simulations). Results hold for finite-precision transformers with poly-log width, continuous CoT, and hybrid transformer-RNN architectures.

**Key Innovation:** Establishes CoT transformers can match textbook Word RAM algorithm runtimes up to polylog factor, removing quadratic overhead of Turing machine simulations.

---

## 3. CTR Prediction & Advertising Recommendation

### 3.1 DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction

| Field | Detail |
|-------|--------|
| **Title** | DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction |
| **Authors** | — |
| **Institution** | Industry (major social-media platform) |
| **arXiv** | [2606.07980](https://arxiv.org/abs/2606.07980) |
| **Date** | Jun 2026 |

**Abstract:** Transformer-based CTR models face residual connection bottlenecks. DeRes routes each layer through two parallel paths — Identity residual (preserving feature reuse and gradient flow) and Block Attention Residual (attending over compressed outputs from all earlier blocks). A vector-wise gate weights each path. SiLU-based Pointwise AttnRes enables multiple past blocks to be activated simultaneously. On 331M interaction industrial dataset, Criteo (45M), Avazu (40M), outperforms 12 baselines with <5% additional FLOPs. 8-layer DeRes matches 16-layer OneTrans (~2× compute saving).

**Key Innovation:** Dual-path residual design (DPN-inspired) for CTR transformers; SiLU-based cross-layer attention for multi-interest patterns; compute–AUC scaling law γ=0.118 vs. 0.071 for OneTrans.

---

### 3.2 Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)

| Field | Detail |
|-------|--------|
| **Title** | Dual-Stream MLP is All You Need for CTR Prediction |
| **Authors** | Kesha Ou (Renmin Univ.), Zhen Tian (ByteDance), Wayne Xin Zhao (Renmin Univ.), Long Zhang (Meituan), Sheng Chen (Meituan), Ji-Rong Wen (Renmin Univ.) |
| **Institution** | Renmin University of China, ByteDance, Meituan |
| **arXiv** | [2606.04944](https://arxiv.org/abs/2606.04944) |
| **Date** | Jun 2026 |

**Abstract:** Proposes DS-MLP with dual-stream architecture (main MLP + parallel MLP) plus knowledge distillation, achieving SOTA across three CTR benchmarks while maintaining MLP-level efficiency.

**Key Innovation:** Simple dual-MLP design + knowledge distillation matches or beats complex feature-interaction architectures for CTR.

---

### 3.3 RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems

| Field | Detail |
|-------|--------|
| **Title** | RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems |
| **Authors** | — |
| **Institution** | Tencent |
| **arXiv** | [2604.17878](https://arxiv.org/abs/2604.17878) |
| **Date** | Apr 2026 |

**Abstract:** Mitigates embedding collapse and enhances latent representation diversity. Online A/B testing on 20% of Weixin traffic yields GMV increases of 3.41% (Video Accounts), 4.81% (Moments), 2.12% (Official Accounts). Dataset spans Jul 2024–Mar 2026 with 20M daily samples and 1200+ sparse features.

**Key Innovation:** Industrial-scale embedding collapse mitigation; full deployment across Weixin with significant GMV lift.

---

### 3.4 GRAB: An LLM-Inspired Sequence-First CTR Prediction Modeling Paradigm

| Field | Detail |
|-------|--------|
| **Title** | GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm |
| **Authors** | — |
| **Institution** | Baidu |
| **arXiv** | [2602.01865](https://arxiv.org/abs/2602.01865) |
| **Date** | Feb 2026 |

**Abstract:** End-to-end generative framework for CTR with Causal Action-aware Multi-channel Attention (CamA). Full deployment at Baidu home feed ads: +3.05% revenue, +3.49% CTR. AUC improves monotonically with model capacity and sequence length (no saturation observed).

**Key Innovation:** LLM-inspired generative ranking with CamA; monotonic scaling benefits from longer sequences; deployed at Baidu scale.

---

### 3.5 OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation

| Field | Detail |
|-------|--------|
| **Title** | OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation |
| **Authors** | — |
| **Institution** | Tencent |
| **arXiv** | [2603.02999](https://arxiv.org/abs/2603.02999) |
| **Date** | Mar 2026 |

**Abstract:** Unifies generation and ranking in one model via value-aware multi-task decoupling, coarse-to-fine target awareness, and input-output dual-side consistency. Deployed on Weixin Channels: GMV +1.34%.

**Key Innovation:** Architectural-level deep integration of generation and ranking stages; value-aware multi-task decoupling for advertising.

---

### 3.6 DAIAN: Deep Adaptive Intent-Aware Network for CTR Prediction in Trigger-Induced Recommendation

| Field | Detail |
|-------|--------|
| **Title** | DAIAN: Deep Adaptive Intent-Aware Network for CTR Prediction in Trigger-Induced Recommendation |
| **Authors** | — |
| **Institution** | Industry (Alibaba/Xianyu) |
| **arXiv** | [2602.13971](https://arxiv.org/abs/2602.13971) |
| **Date** | Feb 2026 |

**Abstract:** Addresses "intent myopia" in trigger-induced recommendation. Extracts personalized intent representations, uses hybrid ID + semantic similarity. Online A/B on Xianyu: +6.9% CTR, +1.73% conversion.

**Key Innovation:** Intent-aware adaptation for trigger-induced recommendation; hybrid enhancer with ID and semantic information.

---

### 3.7 Taiji: Pareto Optimal Policy Optimization for Industrial LLM-Enhanced Recommendation

| Field | Detail |
|-------|--------|
| **Title** | Taiji: Pareto Optimal Policy Optimization with Semantics-IDs Trade-off for Industrial LLM-Enhanced Recommendation |
| **Authors** | — |
| **Institution** | Kuaishou |
| **arXiv** | [2606.03866](https://arxiv.org/abs/2606.03866) |
| **Date** | 2 Jun 2026 |

**Abstract:** LLM-as-Enhancer framework. Uses reverse-engineered reasoning + open-ended rejection sampling for high-quality CoT data. Proposes Pareto Optimal Policy Optimization (POPO) for adaptive cross-domain reward weighting. Deployed on Kuaishou advertising platform since May 2026, serving 400M+ daily users.

**Key Innovation:** Theoretical Pareto-optimal trade-off between LLM semantic rewards and recommendation preference rewards; deployed at Kuaishou scale.

---

### 3.8 Trajectory-Based Recommender Systems as Control Systems

| Field | Detail |
|-------|--------|
| **Title** | Trajectory-Based Recommender Systems as Control Systems |
| **Authors** | Eriam Schaffter et al. |
| **Institution** | — |
| **arXiv** | [2606.22957](https://arxiv.org/abs/2606.22957) |
| **Date** | 22 Jun 2026 |

**Abstract:** Proposes Control Theory as foundation for formalizing Trajectory-Based Recommender Systems (TBRS). Reviews related work and shows how Educational Recommender Systems can be modeled within the TBRS framework.

**Key Innovation:** Control-theoretic framework for long-term goal-driven recommendation; formalizes TBRS as a distinct research category.

---

## 4. Sequential Recommendation

### 4.1 GenAIR: Generative Archetype-Grounded Item Representations for Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Title** | GenAIR: Generative Archetype-Grounded Item Representations for Sequential Recommendation |
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2606.11023](https://arxiv.org/abs/2606.11023) |
| **Date** | Jun 2026 |

**Abstract:** Uses LLM to infer "Archetype" (ideal target audience profile) for each item from metadata. Introduces behavioral calibration objective to ground archetype embeddings in real interaction patterns. Integrates with most existing sequential models.

**Key Innovation:** Generative archetype representation from LLM + behavioral calibration; bridges semantic representation gap with actual user behavior.

---

## 5. Reinforcement Learning for LLMs & Agents

### 5.1 Group-Graph Policy Optimization for Long-Horizon Agentic RL (G2PO)

| Field | Detail |
|-------|--------|
| **Title** | Group-Graph Policy Optimization for Long-Horizon Agentic Reinforcement Learning |
| **Authors** | Nala-YN et al. |
| **Institution** | — |
| **arXiv** | [2606.22995](https://arxiv.org/abs/2606.22995) |
| **Date** | 22 Jun 2026 |

**Abstract:** Transforms linear interaction trajectories into a global state-transition graph. Group-aggregation state-value estimation reduces variance; edge-centric advantage estimation identifies critical transitions. On WebShop, ALFWorld, AppWorld: up to 22.2% improvement over GRPO.

**Key Innovation:** Graph-structured credit assignment for multi-turn agentic RL; edge-centric advantage over standard node-centric approaches.

---

### 5.2 GraphPO: Graph-based Policy Optimization for Reasoning Models

| Field | Detail |
|-------|--------|
| **Title** | GraphPO: Graph-based Policy Optimization for Reasoning Models |
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2606.18954](https://arxiv.org/abs/2606.18954) |
| **Date** | ~18 Jun 2026 |

**Abstract:** Represents rollouts as a DAG with reasoning steps as edges and semantic states as nodes. Merges semantically equivalent paths into equivalence classes. Assigns efficiency advantages to incoming edges and correctness advantages to outgoing edges. Reduces advantage-estimation variance and improves reasoning efficiency.

**Key Innovation:** Graph-structured RL for reasoning models; merges equivalent reasoning paths for budget reallocation; dual advantage (efficiency + correctness).

---

### 5.3 Agentic Monte Carlo: Simulating RL for Black-Box Agents

| Field | Detail |
|-------|--------|
| **Title** | Agentic Monte Carlo: Simulating Reinforcement Learning for Black-Box Agents |
| **Authors** | — |
| **Institution** | Layer6 AI |
| **arXiv** | [2606.05296](https://arxiv.org/abs/2606.05296) |
| **Date** | Jun 2026 |

**Abstract:** Employs Sequential Monte Carlo to sample from optimal policy posterior of black-box LLM agents (API-only). Learns a value function to steer the agent without modifying the underlying model. Outperforms GRPO with more test-time compute on AgentGym benchmarks (WebShop, SciWorld, TextCraft).

**Key Innovation:** First RL-style optimization of black-box LLM agents via SMC without parameter access; outperforms GRPO at scale.

---

### 5.4 From Trainee to Trainer: LLM-Designed Training Environment for RL

| Field | Detail |
|-------|--------|
| **Title** | From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning |
| **Authors** | Chao Chen et al. |
| **Institution** | — |
| **arXiv** | [2606.17682](https://arxiv.org/abs/2606.17682) |
| **Date** | 16 Jun 2026 |

**Abstract:** LLM-as-Environment-Engineer framework: the current policy model analyzes failure trajectories and proposes environment configuration modifications for the next training stage. Introduces MAPF-FrozenLake testbed. The RL checkpoint serves as a better environment engineer than the base model.

**Key Innovation:** Self-improving RL pipeline where the policy designs its own training environments; insight that policy learning improves environment design ability.

---

### 5.5 Scalable Maximum Entropy RL for Diffusion Policies via Adjoint Matching

| Field | Detail |
|-------|--------|
| **Title** | Scalable Maximum Entropy Reinforcement Learning for Diffusion Policies via Adjoint Matching |
| **Authors** | Serge Thilges et al. |
| **Institution** | — |
| **arXiv** | [2606.22630](https://arxiv.org/abs/2606.22630) |
| **Date** | 21 Jun 2026 |

**Abstract:** Introduces adjoint matching for simulation-free training of diffusion policies in online RL. Avoids explicit likelihood estimation or costly backpropagation through the diffusion process.

**Key Innovation:** Adjoint matching for scalable online RL with diffusion policies; simulation-free optimization.

---

### 5.6 dVLA-RL: RL over Denoising Trajectories for Discrete Diffusion VLAs

| Field | Detail |
|-------|--------|
| **Title** | dVLA-RL: Reinforcement Learning over Denoising Trajectories for Discrete Diffusion Vision-Language-Action Models |
| **Authors** | Yuhao Wu et al. |
| **Institution** | — |
| **arXiv** | [2606.23623](https://arxiv.org/abs/2606.23623) |
| **Date** | 22 Jun 2026 |

**Abstract:** First RL fine-tuning for discrete diffusion VLA models. Models denoising process as MDP, optimizes joint probability of sampled generation path. Achieves 99.7% success on LIBERO, +30.6% over SFT baseline on RoboTwin 2.0.

**Key Innovation:** First RL for discrete diffusion VLAs; trajectory-level objective for variable denoising steps; unified step scheduling.

---

## 6. Games & Long-Horizon Decision Making

### 6.1 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Title** | Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning |
| **Authors** | Chengshuai Shi, Wenzhe Li, Xinran Liang, Yizhou Lu, Wenjia Yang, Ruirong Feng, Seth Karten, Ziran Yang, Zihan Ding, Gabriel Sarch, Danqi Chen, Karthik Narasimhan, Chi Jin |
| **Institution** | Princeton University |
| **arXiv** | [2605.00347](https://arxiv.org/abs/2605.00347) |
| **Date** | 1 May 2026 |

**Abstract:** Studies RL for VLMs in Super Mario Land (100+ turns). Proposes adapted PPO with lightweight turn-level critic, substantially more stable than critic-free methods (GRPO, Reinforce++). Odysseus framework achieves at least 3× average game progress over frontier models, with in-game and cross-game generalization.

**Key Innovation:** Long-horizon (100+ turn) VLM RL; turn-level critic for stability; 3× improvement over frontier models; cross-game generalization.

---

### 6.2 Robust Adversarial RL in Stochastic Games via Sequence Modeling (CART)

| Field | Detail |
|-------|--------|
| **Title** | Robust Adversarial Reinforcement Learning in Stochastic Games via Sequence Modeling |
| **Authors** | Xiaohang Tang et al. |
| **Institution** | — |
| **arXiv** | [2510.11877](https://arxiv.org/abs/2510.11877) |
| **Date** | 13 Oct 2025 |

**Abstract:** Conservative Adversarially Robust Decision Transformer (CART). Formulates protagonist–adversary interaction as stage games with NashQ conditioning. Generates policies that are both adversarially robust and conservative to transition uncertainty.

**Key Innovation:** First robustness framework for Decision Transformers in adversarial stochastic games; NashQ-conditioned Transformer policies.

---

## 7. Quick Reference Table

| # | Paper | Venue/Date | Area | Key Innovation |
|---|-------|-----------|------|----------------|
| 1 | SelfCompact | 22 Jun 2026 | LLM Agents | Meta-cognitive context compaction |
| 2 | Pigeonholing | 23 Jun 2026 | LLM Safety | Bad-context mode collapse; RLVR mitigation |
| 3 | Abstract Geometry | 22 Jun 2026 | LLM Mechanistic | Hippocampal-like geometry in LLMs |
| 4 | Words as Difference Makers | 21 Jun 2026 | LLM Theory | Variational induction for causal learning |
| 5 | CoT Change Detection | 20 Jun 2026 | LLM Safety | Models can't detect CoT tampering |
| 6 | ReasoningLens | 22 Jun 2026 | LLM Tools | Auditing framework for reasoning traces |
| 7 | ToxSearch-S | 23 Jun 2026 | Red-Teaming | MPI-parallel evolutionary prompt search |
| 8 | HydraHead | 18 Jun 2026 | Attention | Head-level FA/LA hybridization |
| 9 | CAHP | 17 Jun 2026 | Attention Pruning | Graph-theoretic head pruning |
| 10 | Emergent Sparse Attention | 25 Jun 2026 | Mechanistic | Emergence = learning sparse attention |
| 11 | SWARR | 10 Jun 2026 | Efficient Attention | RL makes SWA competitive for math |
| 12 | Attention Program Synthesis | 18 Jun 2026 | Interpretability | Programmatic explanations of heads |
| 13 | CoT Word RAM | 18 Jun 2026 | Theory | CoT transformers simulate algorithms efficiently |
| 14 | DeRes | Jun 2026 | CTR | Dual-path residual for CTR transformers |
| 15 | DS-MLP | Jun 2026 | CTR | Simple dual-MLP + KD for CTR |
| 16 | RankUp | Apr 2026 | Ads/Recsys | Embedding anti-collapse; Tencent deployed |
| 17 | GRAB | Feb 2026 | CTR | Generative ranking; Baidu deployed |
| 18 | OneRanker | Mar 2026 | Ads/Recsys | Unified generation + ranking; Tencent deployed |
| 19 | DAIAN | Feb 2026 | CTR | Intent-aware trigger-induced rec; Alibaba deployed |
| 20 | Taiji | 2 Jun 2026 | LLM+Recsys | Pareto-optimal semantics-IDs trade-off; Kuaishou deployed |
| 21 | TBRS as Control | 22 Jun 2026 | Recsys Theory | Control theory for trajectory-based RS |
| 22 | GenAIR | Jun 2026 | Sequential Rec | LLM-generated archetype representations |
| 23 | G2PO | 22 Jun 2026 | RL Agents | Graph credit assignment for agentic RL |
| 24 | GraphPO | 18 Jun 2026 | RL Reasoning | DAG-based RL for reasoning models |
| 25 | Agentic MC | Jun 2026 | RL Agents | SMC for black-box LLM agents |
| 26 | Trainee→Trainer | 16 Jun 2026 | RL Pipeline | Self-designing training environments |
| 27 | MaxEnt Diffusion RL | 21 Jun 2026 | RL | Adjoint matching for diffusion policies |
| 28 | dVLA-RL | 22 Jun 2026 | Robotics | First RL for discrete diffusion VLAs |
| 29 | Odysseus | 1 May 2026 | Games/VLM | 100+ turn VLM game-playing; 3× frontier |
| 30 | CART | Oct 2025 | Games/RL | Robust Decision Transformer for stochastic games |

---

*Generated 2026-06-26. Covers arXiv submissions from ~20–25 Jun 2026.*
