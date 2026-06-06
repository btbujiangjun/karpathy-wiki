---
title: "arXiv Daily — May 24, 2026"
type: synthesis
created: 2026-05-24
updated: 2026-05-24
sources: []
tags: [arxiv, survey, llm, recommendation, ctr, games, reinforcement-learning, fine-tuning]
---

# arXiv Daily — May 24, 2026

A curated survey of recent arXiv papers across AI, LLMs, recommendation systems, advertising, CTR prediction, sequential modeling, games, and reinforcement learning.

---

## Table of Contents

1. [Large Language Models: Training & Optimization](#1-large-language-models-training--optimization)
2. [Large Language Models: Post-Training & Fine-Tuning](#2-large-language-models-post-training--fine-tuning)
3. [Large Language Models: Reasoning & Alignment](#3-large-language-models-reasoning--alignment)
4. [CTR Prediction & Advertising](#4-ctr-prediction--advertising)
5. [Recommendation Systems: Generative & Agentic](#5-recommendation-systems-generative--agentic)
6. [Sequential Recommendation](#6-sequential-recommendation)
7. [Games & Reinforcement Learning](#7-games--reinforcement-learning)
8. [Diffusion Models for Language](#8-diffusion-models-for-language)
9. [Interpretability & Analysis](#9-interpretability--analysis)

---

## 1. Large Language Models: Training & Optimization

### 1.1 ScheduleFree+: Scaling Learning-Rate-Free & Schedule-Free Learning to Large Language Models

- **Link:** [arxiv.org/abs/2605.19095](https://arxiv.org/abs/2605.19095)
- **Authors:** (anonymous tech report)
- **Institution:** — (multi-institutional)
- **Abstract:** Identifies fixes to scale Schedule-Free Learning to larger batch/model sizes. Presents ScheduleFree+, a learning-rate-free method that greatly outperforms Warmup-Stable-Decay (WSD) schedules. At 1000 tokens/parameter, outperforms SOTA schedules by 31% — a 31% reduction in training time to reach the same loss.
- **Key Innovations:**
  - Modifications to beta-annealing, weighted averaging, and Polyak step-size for LLM scale
  - Demonstrates fully learning-rate-free training scales to LLMs
  - Theoretical foundation for model averaging and checkpoint merging during pretraining

### 1.2 Muown: Row-Norm Control for Muon Optimization

- **Link:** [arxiv.org/abs/2605.10797](https://arxiv.org/abs/2605.10797)
- **Institution:** — (multi-institutional)
- **Abstract:** Diagnoses spectral-norm drift in Muon optimization as driven by row-magnitude growth. Proposes Muown, a drop-in replacement that treats row-magnitude as an explicit optimizer variable under ℓ∞ geometry. Proves optimal non-convex rates in deterministic and stochastic regimes.
- **Key Innovations:**
  - Decomposes spectral norm into row-magnitude and row-coherence factors
  - Muown improves perplexity over Muon, SOAP, AdamW, and Lion from 124M to 2.7B params
  - Widens plateau of near-optimal learning rates and reduces weight-decay sensitivity

### 1.3 Warmup-Stable-Only (WSO) Outperforms Decay-Based Schedulers After SFT

- **Link:** [arxiv.org/abs/2603.16127](https://arxiv.org/abs/2603.16127)
- **Institution:** — (multi-institutional)
- **Abstract:** Examines WSO (constant LR after warmup, no decay). Shows that WSO consistently outperforms decay-based schedulers on downstream tasks after SFT, even though decay schedulers achieve better pretraining perplexity. Loss landscape analysis reveals decay leads to sharper minima while WSO preserves flatter minima.
- **Key Innovations:**
  - Systematic demonstration of "inversion" between pretrain metrics and SFT performance
  - WSO effectiveness holds across mid-training and over-training regimes
  - Practical guidance: release models trained with WSO for better downstream adaptability

### 1.4 MinT: Managed Infrastructure for Training and Serving Millions of LLMs

- **Link:** [arxiv.org/abs/2605.13779](https://arxiv.org/abs/2605.13779)
- **Authors:** Mind Lab (Cao et al.)
- **Institution:** Mind Lab
- **Abstract:** Presents MinT, a managed infrastructure system for LoRA post-training and online serving. Targets a setting where many trained policies are produced over a small number of expensive base-model deployments. Keeps base model resident and moves adapter revisions through a full lifecycle. Validated beyond 1T total parameters on frontier architectures.
- **Key Innovations:**
  - Adapter revision path: rollout, update, export, eval, serve, rollback
  - Supports dense and MoE architectures via LoRA target mapping
  - Adapter size as low as 1% of base model — eliminates full-checkpoint materialization

---

## 2. Large Language Models: Post-Training & Fine-Tuning

### 2.1 Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Principle

- **Link:** [arxiv.org/abs/2605.12483](https://arxiv.org/abs/2605.12483)
- **Institution:** — (multi-institutional)
- **Abstract:** Identifies a reward-density principle: sparse sequence-level reward is most useful on models that can explore (teacher side), while dense token-level supervision is for compressing behavior into a smaller deployment model. A four-stage workflow (teacher RL → forward-KL warmup → on-policy distillation → optional student RL) beats direct GRPO on Qwen3/Llama families.
- **Key Innovations:**
  - Teacher-side discovery + dense bridge + student-side polish
  - With Qwen3-1.7B student: 79.3% vs 75.9% on MATH; 25.2% vs 19.8% on AIME
  - Component ablation confirms each stage is load-bearing

### 2.2 LoPT: Local-Learning Post-Training

- **Link:** [arxiv.org/abs/2605.04913](https://arxiv.org/abs/2605.04913)
- **Institution:** — (multi-institutional)
- **Abstract:** Proposes placing a single gradient boundary at the transformer midpoint. Second-half block learns from task objective; first-half block is updated by a lightweight feature-reconstruction objective. Shortens backward path while limiting direct interference from narrow task gradients on early-layer representations.
- **Key Innovations:**
  - Works orthogonally to PEFT (can combine with LoRA, gradient checkpointing)
  - Competitive performance with lower memory and higher training efficiency
  - Better retention of pretrained capabilities

### 2.3 Aletheia: Gradient-Guided Layer Selection for Efficient LoRA Fine-Tuning

- **Link:** [arxiv.org/abs/2604.15351](https://arxiv.org/abs/2604.15351)
- **Institution:** — (multi-institutional)
- **Abstract:** Identifies most task-relevant layers via a lightweight gradient probe and applies LoRA adapters only to selected layers with asymmetric rank allocation. Across 81 experiments on 14 models from 8 architecture families (0.5B–72B), achieves 15–28% training speedup (mean 23.1%) with matched downstream behavior.
- **Key Innovations:**
  - 100% per-model speed win rate across tested families
  - Bounded extra forgetting on MMLU, GSM8K, HumanEval

### 2.4 LoRA-Pre: Low-Rank Optimizer for Efficient Pre-Training

- **Link:** [arxiv.org/abs/2602.24283](https://arxiv.org/abs/2602.24283)
- **Institution:** — (multi-institutional)
- **Abstract:** Establishes equivalence between EMA momentum and online linear regression. Proposes LoRA-Pre, a low-rank optimizer that compresses momentum into a compact subspace. Validated by pre-training Llama models from 60M to 1B parameters.
- **Key Innovations:**
  - LoRA-Pre achieves same or better perplexity at 1/8 the rank of baseline methods
  - For fine-tuning: +3.14 points on Llama-3.1-8B, +6.17 points on Llama-2-7B over standard LoRA

### 2.5 GRASS: Gradient-Based Adaptive Layer-Wise Importance Sampling

- **Link:** [arxiv.org/abs/2604.07808](https://arxiv.org/abs/2604.07808)
- **Institution:** — (multi-institutional)
- **Abstract:** Uses mean gradient norms as a task-aware and training-stage-aware metric for layer importance. Dynamically samples and activates a subset of layers, with optimizer state offloading. Up to 4.38 points improvement and 19.97% memory reduction.
- **Key Innovations:**
  - Adaptive (not static) layer selection
  - Layer-wise optimizer offloading with computation-communication overlap

### 2.6 TOKENSEEK: Memory Efficient Fine-Tuning via Token Ditching

- **Link:** [arxiv.org/abs/2601.19739](https://arxiv.org/abs/2601.19739)
- **Institution:** — (multi-institutional)
- **Abstract:** Instance-aware token seeking and ditching. Updates model parameters exclusively on selected tokens, achieving 65.7% max memory reduction on Llama3.2-1B with as few as 10% tokens, while maintaining competitive performance.
- **Key Innovations:**
  - Universal plugin: works across Transformer-based models
  - Compatible with QLoRA: 14.8% memory consumption of full fine-tuning
  - Interpretable token importance scores

### 2.7 Hybrid Fine-Tuning (ZO + FO) for LLMs

- **Link:** [arxiv.org/abs/2604.09940](https://arxiv.org/abs/2604.09940)
- **Institution:** — (multi-institutional)
- **Abstract:** Jointly updates both LLM (via zeroth-order optimization) and PEFT modules (via first-order). Theoretical framework centered on "hybrid smoothness." Highest accuracy in 94.5% of cases across 18 model-task combinations with no additional memory overhead.
- **Key Innovations:**
  - Combines benefits of full fine-tuning and PEFT
  - Convergence analysis for reshuffling SGD under multiple learning rates

---

## 3. Large Language Models: Reasoning & Alignment

### 3.1 LEPO: Latent Reasoning Policy Optimization for LLMs

- **Link:** [arxiv.org/abs/2604.17892](https://arxiv.org/abs/2604.17892)
- **Code:** [github.com/YuyanZhou/lepo](https://github.com/YuyanZhou/lepo)
- **Institution:** — (multi-institutional)
- **Abstract:** Injects controllable stochasticity into latent reasoning via Gumbel-Softmax, restoring LLMs' exploratory capacity. Proposes LEPO, applying RL directly to continuous latent representations. Unifies gradient estimation for both latent representations and discrete tokens.
- **Key Innovations:**
  - Stochastic latent reasoning enables diverse trajectory sampling
  - Significantly outperforms existing RL methods for discrete and latent reasoning
  - Unified gradient estimation across latent steps and discrete answers

### 3.2 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning

- **Link:** [arxiv.org/abs/2506.24119](https://arxiv.org/abs/2506.24119)
- **Code:** [github.com/spiral-rl/spiral](https://github.com/spiral-rl/spiral)
- **Institution:** — (multi-institutional)
- **Abstract:** Self-play framework where models learn by playing multi-turn zero-sum games against themselves. Introduces role-conditioned advantage estimation (RAE) for stable multi-agent training. Up to 10% improvement across 8 reasoning benchmarks on Qwen and Llama families. Even DeepSeek-R1-Distill-Qwen-7B benefits.
- **Key Innovations:**
  - No human-curated data needed — unlimited training from game dynamics
  - Multi-game training (TicTacToe, Kuhn Poker, Simple Negotiation) yields strongest results
  - Different games develop complementary cognitive patterns

### 3.3 Involuntary In-Context Learning (IICL): Bypassing Safety Alignment

- **Link:** [arxiv.org/abs/2604.19461](https://arxiv.org/abs/2604.19461)
- **Institution:** — (multi-institutional)
- **Abstract:** Introduces an attack class using abstract operator framing with few-shot examples to force pattern completion overriding safety training. Through 3479 probes across 10 OpenAI models (GPT-4.1 through GPT-5.4-pro). Semantic operator naming achieves 100% bypass rate; direct Q&A format yields 0%.
- **Key Innovations:**
  - HarmBench: 24.0% bypass against GPT-5.4 vs 0.0% for direct queries
  - Bimodal vulnerability: 6 models completely resistant, 4 models fragile
  - All "pro" variants and gpt-5.2 in the robust category

### 3.4 STRATAGEM: Transferable Reasoning via Game Self-Play

- **Link:** [arxiv.org/abs/2604.17696](https://arxiv.org/abs/2604.17696)
- **Institution:** — (multi-institutional)
- **Abstract:** Addresses domain specificity and contextual stasis in self-play for reasoning. Selectively reinforces trajectories exhibiting abstract, domain-agnostic reasoning via a Reasoning Transferability Coefficient and incentivizes adaptive reasoning via a Reasoning Evolution Reward.
- **Key Innovations:**
  - Transfers to mathematical reasoning, general reasoning, and code generation
  - Strong gains on competition-level mathematics

### 3.5 CPMobius: Coach–Player Reasoning for Data-Free RL

- **Link:** [arxiv.org/abs/2602.02979](https://arxiv.org/abs/2602.02979)
- **Institution:** — (multi-institutional)
- **Abstract:** Collaborative Coach–Player paradigm. Coach proposes instructions targeted at Player's capability and receives rewards based on improvement in Player's reasoning. No external training data needed. On Qwen2.5-Math-7B-Instruct, improves accuracy overall.
- **Key Innovations:**
  - Data-free cooperative loop, not adversarial
  - Coach and Player co-evolve to maximize learning efficiency
  - Coach rewarded for Player's growth, not for stumping the Player

---

## 4. CTR Prediction & Advertising

### 4.1 IDProxy: Cold-Start CTR at Xiaohongshu with Multimodal LLMs

- **Link:** [arxiv.org/abs/2603.01590](https://arxiv.org/abs/2603.01590)
- **Authors:** Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan, Ruiyan Han, Feiyang Xiao, Yanhua Huang, Li Lin, Yang Luo, Yao Hu
- **Institution:** Xiaohongshu
- **Abstract:** Leverages MLLMs to generate proxy embeddings from rich content signals for cold-start items. Proxy embeddings are explicitly aligned with existing ID embedding space and optimized end-to-end under CTR objectives. Successfully deployed in Content Feed and Display Ads at Xiaohongshu, serving hundreds of millions of daily users.
- **Key Innovations:**
  - Proxy embeddings act as drop-in replacement for ID embeddings at cold start
  - Seamless integration into existing large-scale ranking pipelines
  - Validated through online A/B tests in production

### 4.2 EST: Efficient Scaling Laws in CTR Prediction (Taobao)

- **Link:** [arxiv.org/abs/2602.10811](https://arxiv.org/abs/2602.10811)
- **Institution:** Alibaba (Taobao)
- **Abstract:** Revisits distinctions between CTR and LLMs. Proposes Efficiently Scalable Transformer (EST) with Lightweight Cross-Attention (LCA) and Content Sparse Attention (CSA). Exhibits stable power-law scaling. Deployed on Taobao display advertising.
- **Key Innovations:**
  - First fully unified modeling of all raw inputs in a single sequence for CTR
  - LCA prunes redundant self-interactions; CSA uses content similarity for sparse attention
  - Online: +1.22% CTR, +3.27% RPM (Guess scenario); +2.01% CTR, +2.66% RPM (Post scenario)

### 4.3 LoopCTR: Recursive Computation Scaling for CTR

- **Link:** [arxiv.org/abs/2604.19550](https://arxiv.org/abs/2604.19550)
- **Institution:** — (multi-institutional)
- **Abstract:** Introduces a sandwich architecture (Entry Block, Loop Block, Exit Block) decoupling feature encoding, iterative reasoning, and score prediction. Uses process supervision at every loop depth — train multi-loop, infer zero-loop. Oracle analysis reveals 0.02–0.04 AUC of untapped headroom.
- **Key Innovations:**
  - New scaling paradigm: computation scaling through recursive latent reasoning
  - Hyper-Connected Residuals and MoE augment Loop Block
  - Zero-loop inference already outperforms all baselines

### 4.4 PRECTR-V2: Unified Relevance–CTR with LLM-Distilled Encoder

- **Link:** [arxiv.org/abs/2602.20676](https://arxiv.org/abs/2602.20676)
- **Authors:** Shuzhi Cao, Rong Chen, Ailong He, Shuguang Han, Jufeng Chen
- **Institution:** — (multi-institutional)
- **Abstract:** Addresses search relevance + CTR coordination. Three contributions: cross-user preference mining for cold-start, exposure bias correction via loss gating, and LLM-distilled lightweight encoder replacing BERT. AUC 0.7674, GAUC 0.6933 in offline experiments.
- **Key Innovations:**
  - Unifies two traditionally separate objectives (relevance + CTR)
  - LLM distillation enables lightweight deployment
  - Online A/B validation

### 4.5 DAIAN: Deep Adaptive Intent-Aware Network for CTR in Trigger-Induced Recommendation

- **Link:** [arxiv.org/abs/2602.13971](https://arxiv.org/abs/2602.13971)
- **Authors:** Zhihao Lv, Longtao Zhang, Ailong He, Shuzhi Cao, Shuguang Han, Jufeng Chen
- **Institution:** Alibaba (Xianyu)
- **Abstract:** Addresses "intent myopia" in trigger-induced recommendation. Extracts user intent representations by analyzing correlation between clicks and trigger items. Uses hybrid enhancer with ID and semantic information. Deployed on Xianyu's TIR scenario.
- **Key Innovations:**
  - Three-stage extraction: correlation analysis → behavior retrieval → adaptive selection
  - Online: +1.59% CTR, +1.73% diversity, +2.37% bills

### 4.6 LLaCTR: Lightweight LLM-Enhanced CTR

- **Link:** [arxiv.org/abs/2505.14057](https://arxiv.org/abs/2505.14057)
- **Authors:** Yu Cui, Feng Liu, Jiawei Chen, Yuegang Sun, Xiaohu Yang, Can Wang
- **Institution:** — (multi-institutional)
- **Published at:** WWW '26
- **Abstract:** Uses self-supervised field-feature fine-tuning to distill lightweight semantic knowledge from LLMs. Enhances both feature representation and feature interactions. Integrated with 6 representative CTR models across 4 datasets. 2.24% average improvement, 10–100× cheaper than other LLM-enhanced methods.
- **Key Innovations:**
  - Field-level (not item-level) semantic enhancement
  - Self-supervised distillation — no additional labeling needed
  - Practical: compatible with existing CTR architectures

### 4.7 LLM-HYPER: Generative CTR Modeling for Cold-Start Ads

- **Link:** [arxiv.org/abs/2604.12096](https://arxiv.org/abs/2604.12096)
- **Institution:** Major US e-commerce platform
- **Abstract:** Uses LLMs as hypernetworks to directly generate parameters of a CTR estimator in a training-free manner. Few-shot Chain-of-Thought prompting over multimodal ad content. Normalization and calibration align generated weights with production CTR distributions. +55.9% NDCG@10 over cold-start baselines.
- **Key Innovations:**
  - First use of LLM-as-hypernetwork for CTR weight generation
  - Deployed on Homepage Ads cold-start ranking in production
  - Competitive with warm-start models within 30-day A/B test

### 4.8 LAIN: Length-Adaptive Interest Network for CTR

- **Link:** [arxiv.org/abs/2601.19142](https://arxiv.org/abs/2601.19142)
- **Institution:** — (multi-institutional)
- **Abstract:** Observes that longer max input sequences paradoxically degrade performance for short-sequence users. Proposes LAIN with Spectral Length Encoder, Length-Conditioned Prompting, and Length-Modulated Attention. Up to 1.15% AUC gain and 2.25% log loss reduction.
- **Key Innovations:**
  - First explicit modeling of sequence length as conditioning signal in CTR
  - Addresses attention polarization and gradient conflicts from length imbalance
  - Plug-and-play: compatible with mainstream CTR models

### 4.9 OneRanker: Unified Generation and Ranking at Tencent

- **Link:** [arxiv.org/abs/2603.02999](https://arxiv.org/abs/2603.02999)
- **Institution:** Tencent
- **Abstract:** Achieves architectural-level deep integration of generation and ranking. Value-aware multi-task decoupling architecture separates interest coverage and value optimization. Coarse-to-fine collaborative target awareness mechanism. Deployed on WeChat Channels advertising.
- **Key Innovations:**
  - Fake Item Tokens for implicit target awareness during generation
  - Key/Value pass-through and Distribution Consistency Constraint Loss
  - GMV +1.34% in production

---

## 5. Recommendation Systems: Generative & Agentic

### 5.1 GenRec: Preference-Oriented Generative Framework (JD)

- **Link:** [arxiv.org/abs/2604.14878](https://arxiv.org/abs/2604.14878)
- **Authors:** Yanyan Zou, Junbo Qi, Lunsong Huang, Yu Li, Kewei Xu, Jiahao Gao, Binglei Zhao, Xuanhua Yang, Sulong Xu, Shengjie Li
- **Institution:** JD.com
- **Published at:** SIGIR '26
- **Abstract:** Page-wise NTP task supervises over entire interaction page. Asymmetric linear Token Merger compresses Semantic IDs. GRPO-SR pairs Group Relative Policy Optimization with NLL regularization. Month-long online A/B test: +9.5% clicks, +8.7% transactions.
- **Key Innovations:**
  - Solves one-to-many ambiguity of point-wise NTP training
  - Scaling laws demonstrated for generative recommendation
  - Large-scale deployment validation

### 5.2 ARS: Agentic Recommender System with Hierarchical Belief-State Memory

- **Link:** [arxiv.org/abs/2605.14401](https://arxiv.org/abs/2605.14401)
- **Institution:** — (multi-institutional)
- **Abstract:** Treats recommendation as a partially observable POMDP. Three-tier belief state: event memory (raw signals), preference memory (fine-grained chunks with strength/evidence tracking), profile memory (coherent NL narrative). Six-operation lifecycle managed by LLM planner. +26.4% HR@1, +10.3% NDCG@10, 2.3× fewer tokens.
- **Key Innovations:**
  - First complete memory lifecycle for agentic recommendation
  - Agentic scheduling yields 21.6% further gains in evolving settings
  - Preference memory value is in structuring lifecycle, not in directly informing ranker

### 5.3 Multi-LLM Token Filtering and Routing for Sequential Recommendation (MLTFR)

- **Link:** [arxiv.org/abs/2604.18200](https://arxiv.org/abs/2604.18200)
- **Institution:** — (multi-institutional)
- **Abstract:** Shows single-LLM token embeddings yield unstable gains due to misalignment, insufficient adaptation, and restricted coverage. Proposes MLTFR with user-guided token filtering and MoE architecture with Fisher-weighted semantic consensus expert.
- **Key Innovations:**
  - Corpus-free: uses LLM token embeddings alone without textual input
  - Multi-LLM integration prevents any single LLM's limitations
  - Consistently outperforms SOTA sequential recommenders

### 5.4 ISRF: Iterative Semantic Reasoning for Generative Recommendation

- **Link:** [arxiv.org/abs/2603.13934](https://arxiv.org/abs/2603.13934)
- **Published at:** WWW '26
- **Institution:** — (multi-institutional)
- **Abstract:** Three-step reasoning: multi-step bidirectional reasoning over item attributes → similarity-based user graph for group interests → iterative batch optimization. Bridges explicit individual interests and implicit group interests.
- **Key Innovations:**
  - Semantic reasoning (not just semantic integration)
  - Iterative refinement aligns individual and group interest modeling

### 5.5 ProMax: LLM-Derived Profiles with Distribution Shaping

- **Link:** [arxiv.org/abs/2604.26231](https://arxiv.org/abs/2604.26231)
- **Published at:** SIGIR '26
- **Institution:** — (multi-institutional)
- **Abstract:** Revisits profiles from a retrieval perspective. Uses dense retrieval to uncover collaborative relationships between user and item profiles. Dual distribution-reshaping process. Model-agnostic — applied to 4 classic methods on 3 datasets.
- **Key Innovations:**
  - Profiles used as guiding signals, not auxiliary features
  - Distribution reshaping steers models toward learning preferences for unseen items

### 5.6 Deep Research for Recommender Systems (RecPilot)

- **Link:** [arxiv.org/abs/2603.07605](https://arxiv.org/abs/2603.07605)
- **Institution:** — (multi-institutional)
- **Abstract:** Proposes replacing conventional item lists with comprehensive, user-centric reports. Multi-agent framework: user trajectory simulation agent + self-evolving report generation agent. Up to 52% improvement in Recall@5. 77% of recommendations go beyond superficial preference matching.
- **Key Innovations:**
  - Paradigm shift: from passive filter to active research assistant
  - RL with model-free process rewards for trajectory simulation
  - Self-evolving optimization over structured rubrics and experience-based memories

### 5.7 STAR: Internalizing Multi-Agent Reasoning for Recommendation

- **Link:** [arxiv.org/abs/2602.09829](https://arxiv.org/abs/2602.09829)
- **Institution:** — (multi-institutional)
- **Abstract:** Multi-agent teacher system with Collaborative Signal Translation converts latent behavioral patterns into natural language evidence. Trajectory-driven distillation pipeline (SFT + GRPO) transfers agentic logic into compact STAR student. Student surpasses teacher by 8.7–39.5% while eliminating iterative latency.
- **Key Innovations:**
  - Verbalization of collaborative signals enables explicit reasoning
  - Internalization removes multi-agent coordination overhead at inference
  - Paves way for real-time, reasoning-enhanced recommendation

### 5.8 Beyond Interleaving: Causal Attention for Generative Recommender Systems (Meta)

- **Link:** [arxiv.org/abs/2603.10369](https://arxiv.org/abs/2603.10369)
- **Authors:** Hailing Cheng
- **Institution:** Meta
- **Published at:** KDD '26
- **Abstract:** Critiques interleaved token formulation in generative recommenders (e.g., HSTU). Proposes AttnLFA (causal attention pooling) and AttnMVP (mixed-value early fusion). Reduces sequence complexity by 50%. On large-scale social network data: 0.8% evaluation loss improvement, 23% training time reduction.
- **Key Innovations:**
  - First-principles causal analysis of interleaved item–action sequences
  - Encourages explicit causality encoding over token interleaving

### 5.9 GLASS: Generative Recommender for Long-Sequence Modeling

- **Link:** [arxiv.org/abs/2602.05663](https://arxiv.org/abs/2602.05663)
- **Authors:** Shiteng Cao, Junda She, Ji Liu, Bin Zeng, Chengcheng Guo, Kuo Cai, Qiang Luo, Ruiming Tang, Han Li, Kun Gai, Zhiheng Li, Cheng Yang
- **Institution:** — (multi-institutional)
- **Abstract:** Integrates long-term user interests into generative process via SID-Tier (maps long-term interactions into unified interest vector) and semantic hard search (uses coarse-grained semantic ID as dynamic key for history retrieval). Addresses data sparsity with semantic neighbor augmentation and codebook resizing.
- **Key Innovations:**
  - SID-Tier leverages compact semantic codebook for cross features
  - Adaptive gated fusion for trajectory recalibration
  - Validated on TAOBAO-MM and KuaiRec

---

## 6. Sequential Recommendation

### 6.1 MoS: Mixture of Sequence for Long-Sequence Recommendation

- **Link:** [arxiv.org/abs/2604.20858](https://arxiv.org/abs/2604.20858)
- **Published at:** WWW '26
- **Institution:** — (multi-institutional)
- **Code:** [github.com/xiaolin-cs/MoS](https://github.com/xiaolin-cs/MoS)
- **Abstract:** Identifies "session hopping" phenomenon in long sequences — interests shift across sessions and may reappear. Proposes model-agnostic MoE framework with theme-aware routing and multi-scale fusion (global + short-term + theme-specific experts).
- **Key Innovations:**
  - First systematic analysis of session hopping in sequential recommendation
  - Theme-aware routing filters out irrelevant information from interest shifts
  - Fewer FLOPs than MoE counterparts while improving performance

### 6.2 FuXi-Linear: Linear Attention for Long-Term Sequential Recommendation

- **Link:** [arxiv.org/abs/2602.23671](https://arxiv.org/abs/2602.23671)
- **Authors:** Yufei Ye, Wei Guo, Hao Wang, Luankang Zhang, Heng Chang, Hong Zhu, Yuyang Ye, Yong Liu, Defu Lian, Enhong Chen
- **Institution:** — (multi-institutional)
- **Abstract:** Addresses three challenges in linear attention for sequential rec: temporal signal crosstalk, insufficient positional info, and focus on short sequences. Proposes Temporal Retention Channel and Linear Positional Channel. Robust power-law scaling at thousand-length scale. Up to 10× prefill and 21× decode speedup.
- **Key Innovations:**
  - Temporal Retention Channel prevents mutual interference between temporal and semantic signals
  - First demonstration of power-law scaling for linear attention recommenders
  - Practical efficiency gains at production scale

### 6.3 ManCAR: Manifold-Constrained Latent Reasoning for Sequential Recommendation

- **Link:** [arxiv.org/abs/2602.20093](https://arxiv.org/abs/2602.20093)
- **Authors:** Kangle Wu, Yabo Ni, Anxiang Zeng, Cong Fu, Hui Li
- **Institution:** — (multi-institutional)
- **Abstract:** Grounds latent reasoning within the topology of a global interaction graph as a feasibility constraint. Adaptive test-time computation via convergence-based stopping criterion. Variational interpretation theoretically validates drift prevention. Up to 46.88% improvement in NDCG@10.
- **Key Innovations:**
  - Interaction graph as manifold constraint (not exhaustive graph traversal)
  - Predictive distribution stabilization as stopping criterion prevents over-refinement
  - Theoretical grounding in variational inference

### 6.4 FLAME: Condensing Ensemble Diversity into a Single Network

- **Link:** [arxiv.org/abs/2604.04038](https://arxiv.org/abs/2604.04038)
- **Authors:** WooJoo Kim, JunYoung Kim, JaeHyung Lim, SeongJin Choi, SeongKu Kang, HwanJo Yu
- **Published at:** SIGIR '26
- **Abstract:** Simulates exponential ensemble diversity using only 2 networks via modular ensemble. One frozen (semantic anchor), one learnable. Guided mutual learning aligns diverse representations. At inference, uses only the learnable network. Up to 7.69× faster convergence, 9.70% NDCG@20 improvement.
- **Key Innovations:**
  - Ensemble-level performance with single-network inference overhead
  - Modular ensemble: each network decomposed into sub-modules
  - Practical for deployment-constrained environments

### 6.5 SpecTran: Spectral-Aware Transformer Adapter for LLM-Enhanced SR

- **Link:** [arxiv.org/abs/2601.21986](https://arxiv.org/abs/2601.21986)
- **Institution:** — (multi-institutional)
- **Abstract:** Addresses dimension collapse in adapter-based methods and rigidity in SVD-based methods. Spectral-domain transformer attends to full spectrum, selecting and aggregating informative components. Learnable spectral-position encoding injects singular-value cues. 9.17% average improvement across 4 datasets and 3 SR backbones.
- **Key Innovations:**
  - Operates in spectral domain — first to do so for LLM-enhanced SR
  - Overcomes both dimension collapse and static spectral pruning
  - Lightweight, model-agnostic plugin

### 6.6 HyTRec: Hybrid Temporal-Aware Attention for Long Behavior Sequences

- **Link:** [arxiv.org/abs/2602.18283](https://arxiv.org/abs/2602.18283)
- **Institution:** — (multi-institutional)
- **Abstract:** Decouples stable preferences from short-term intent spikes. Massive historical sequences → linear attention branch; reserved softmax attention for precise retrieval. Temporal-Aware Delta Network (TADN) dynamically upweights fresh signals while suppressing historical noise. 8%+ Hit Rate improvement for ultra-long sequences.
- **Key Innovations:**
  - Hybrid attention: linear for long-term, softmax for short-term
  - TADN addresses lag in capturing rapid interest drifts
  - Linear inference speed maintained at scale

### 6.7 RoTE: Rotary Time Embedding for Sequential Recommendation

- **Link:** [arxiv.org/abs/2604.13389](https://arxiv.org/abs/2604.13389)
- **Published at:** SIGIR '26
- **Institution:** — (multi-institutional)
- **Code:** [github.com/XiaoLongtaoo/RoTE](https://github.com/XiaoLongtaoo/RoTE)
- **Abstract:** Decomposes timestamps into year/month/day and encodes via unified rotary embedding mechanism. Lightweight plug-and-play module for Transformer-based SR models. Up to 20.11% NDCG@5 improvement without backbone modification.
- **Key Innovations:**
  - Coarse-to-fine multi-level temporal modeling
  - Rotary position encoding extended to temporal domain
  - Seamless integration into existing architectures

### 6.8 FAVE: Flow-Based Average Velocity for Sequential Recommendation

- **Link:** [arxiv.org/abs/2604.04427](https://arxiv.org/abs/2604.04427)
- **Institution:** — (multi-institutional)
- **Abstract:** Learns a direct trajectory from informative prior to target distribution via flow matching. Two-stage training: foundational manifold construction + trajectory optimization with JVP-based straightness constraint. One-step generation: order-of-magnitude inference improvement.
- **Key Innovations:**
  - One-step generative sequential recommendation via flow matching
  - Semantic anchor prior addresses prior mismatch in flow methods
  - Global average velocity consolidates multi-step trajectory into single displacement

### 6.9 GrIT: Group Informed Transformer for Sequential Recommendation

- **Link:** [arxiv.org/abs/2602.19728](https://arxiv.org/abs/2602.19728)
- **Institution:** — (multi-institutional)
- **Abstract:** Captures temporally evolving group features alongside individual interaction histories. Constructs latent group representations with time-varying membership weights. Jointly captures personal and group-level temporal dynamics. Consistently outperforms SOTA across 5 benchmarks.
- **Key Innovations:**
  - First explicit modeling of dynamic group membership in sequential recommendation
  - Time-varying group affinities derived from short- and long-term interaction statistics

### 6.10 MVCrec: Multi-View Contrastive Learning for Sequential Recommendation

- **Link:** [arxiv.org/abs/2604.14114](https://arxiv.org/abs/2604.14114)
- **Institution:** — (multi-institutional)
- **Code:** [github.com/sword-Lz/MMCrec](https://github.com/sword-Lz/MMCrec)
- **Abstract:** Integrates ID-based sequential view and graph-based view via three contrastive objectives (within sequential, within graph, across views). Multi-view attention fusion combines global and local attention. Up to 14.44% NDCG@10 and 9.22% HR@10 improvement over SOTA.
- **Key Innovations:**
  - First multi-view contrastive learning between ID and graph perspectives for SR
  - Only interaction data required — no auxiliary information needed

---

## 7. Games & Reinforcement Learning

### 7.1 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games

- **Link:** [arxiv.org/abs/2605.00347](https://arxiv.org/abs/2605.00347)
- **Institution:** — (multi-institutional)
- **Abstract:** Studies RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Proposes adapted PPO with lightweight turn-level critic, substantially outperforming GRPO and Reinforce++. At least 3× average game progress over frontier models.
- **Key Innovations:**
  - Turn-level critic substantially improves stability over critic-free methods
  - Pretrained VLMs provide strong action priors, improving sample efficiency
  - Emergent in-game and cross-game generalization without losing general-domain capabilities

### 7.2 OpenGame: Open Agentic Coding for Games

- **Link:** [arxiv.org/abs/2604.18394](https://arxiv.org/abs/2604.18394)
- **Institution:** — (multi-institutional)
- **Abstract:** First open-source agentic framework for end-to-end web game creation. Core: Game Skill (Template + Debug) and GameCoder-27B (CPT + SFT + execution-grounded RL). OpenGame-Bench evaluates Build Health, Visual Usability, Intent Alignment via headless browser + VLM.
- **Key Innovations:**
  - GameCoder-27B: domain-specialized code model through 3-stage pipeline
  - Living protocol of verified fixes (Debug Skill)
  - 150 diverse game prompts — SOTA results

### 7.3 HGPO: Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks

- **Link:** [arxiv.org/abs/2602.22817](https://arxiv.org/abs/2602.22817)
- **Institution:** — (multi-institutional)
- **Abstract:** Addresses context explosion in multi-turn RL. Context-aware hierarchical grouping + adaptive weighting advantage estimation. Captures advantages at different context depths. Outperforms baselines on ALFWorld and WebShop with identical GPU memory.
- **Key Innovations:**
  - Low-bias, balanced-variance advantage estimator for multi-turn settings
  - Hierarchical grouping captures advantages at different context depths
  - Minimal additional time cost over single-turn methods

### 7.4 Sensi: Structured Test-Time Learning for LLM Game Agents

- **Link:** [arxiv.org/abs/2603.17683](https://arxiv.org/abs/2603.17683)
- **Institution:** — (multi-institutional)
- **Abstract:** LLM agent for ARC-AGI-3 with two-player architecture (perception/action separation), curriculum learning managed by state machine, and database-as-control-plane. Achieves 50–94× greater sample efficiency than comparable systems (~32 vs 1600–3000 attempts).
- **Key Innovations:**
  - Honest negative result reporting (v2 solves 0 levels but at extreme efficiency)
  - Database-as-control-plane: agent's cognitive state in SQLite tables
  - LLM-as-judge with dynamically generated evaluation rubrics

### 7.5 Self-Play on Zero-Sum Games (SPIRAL)

- *(Already detailed in Section 3.2 above — covers both reasoning and games)*

### 7.6 Nemobot: LLM-Powered Game Agents for Interactive Learning

- **Link:** [arxiv.org/abs/2604.21896](https://arxiv.org/abs/2604.21896)
- **Institution:** — (multi-institutional)
- **Abstract:** Extends Shannon's taxonomy of game-playing machines using LLMs. Four game classes: dictionary-based, rigorously solvable, heuristic-based, learning-based. LLM chatbot demonstrates capabilities across all four with tools for users to create and deploy LLM-powered game agents.
- **Key Innovations:**
  - Modernizes Shannon's taxonomy with LLM capabilities
  - Interactive agentic engineering environment (Nemobot)
  - Self-programming AI via crowdsourced learning

### 7.7 Lifelong Learning in Dark Souls III

- **Link:** [arxiv.org/abs/2601.17923](https://arxiv.org/abs/2601.17923)
- **Published at:** ICLR '26 Lifelong Agent Workshop
- **Abstract:** Models combat control as a directed skill graph with 5 reusable skills trained via hierarchical curriculum. Selective post-training under domain shift: upstream skills (camera, lock-on, movement) remain reusable; downstream skills (dodge, heal-attack) adapt.
- **Key Innovations:**
  - Real-time combat as structured skill graph
  - Selective fine-tuning under limited interaction budget
  - Upstream skills are phase-invariant and transferable

### 7.8 Cross-Entropy Games for General Capabilities

- **Link:** [arxiv.org/abs/2603.22479](https://arxiv.org/abs/2603.22479)
- **Abstract:** Proposes "cognitive training" — growing a curriculum of cross-entropy games. A meta-sampler generates games optimizing a meta-objective O for transfer value between games. Principled derivation of meta-algorithm for building general capabilities.
- **Key Innovations:**
  - Formal framework for curriculum learning via games
  - Transfer value as central quantity for game selection
  - Principled meta-objective for greedy curriculum building

---

## 8. Diffusion Models for Language

### 8.1 RePlaid: Continuous Diffusion Scales Competitively with Discrete Diffusion

- **Link:** [arxiv.org/abs/2605.18530](https://arxiv.org/abs/2605.18530)
- **Authors:** Zhihan Yang, Wei Guo, Shuibai Zhang, Subham Sekhar Sahoo, Yongxin Chen, Arash Vahdat, Morteza Mardani, John Thickstun
- **Institution:** — (multi-institutional)
- **Abstract:** Revisits Plaid (continuous diffusion language model) and constructs RePlaid by aligning architecture with modern discrete DLMs. First scaling law for continuous DLMs: compute gap of only 20× vs autoregressive (beats discrete DLM Duo with fewer params). New SOTA PPL of 22.1 among continuous DLMs on OpenWebText.
- **Key Innovations:**
  - First unified scaling law comparison between continuous and discrete DLMs
  - ELBO objective naturally recovers linear cross-entropy over time — eliminates heuristic time reparameterization
  - Likelihood-based training creates structured embedding geometries

---

## 9. Interpretability & Analysis

### 9.1 The Spectral Geometry of Thought

- **Link:** [arxiv.org/abs/2604.15350](https://arxiv.org/abs/2604.15350)
- **Institution:** — (multi-institutional)
- **Abstract:** Discovers spectral phase transitions in hidden activation spaces during reasoning vs factual recall. Across 11 models (Qwen, Pythia, Phi, Llama, DeepSeek-R1). Seven findings including: (1) Reasoning spectral compression in 9/11 models; (2) Instruction tuning spectral reversal; (3) Spectral α alone achieves AUC = 1.000 for correctness prediction in Qwen2.5-7B.
- **Key Innovations:**
  - Universal spectral direction for reasoning; architecture-specific dynamics
  - Token-level spectral cascade with exponential decay of cross-layer coupling
  - Perfect correctness prediction before final answer is generated

### 9.2 Automatically Finding Side-Effects of Interventions on LLMs

- **Link:** [arxiv.org/abs/2605.05090](https://arxiv.org/abs/2605.05090)
- **Abstract:** Automated contrastive evaluation pipeline for auditing behavioral impact of interventions. Compares base model M1 vs intervention model M2 across aligned prompt contexts. Validated on reasoning distillation, knowledge editing, and unlearning. Does not hallucinate differences when effects are absent.
- **Key Innovations:**
  - Statistically validated natural language hypotheses describing behavioral differences
  - Works for both intended and unexpected shifts
  - VibeCheck-style but fully automated

---

## Summary Statistics

| Category | Papers |
|----------|--------|
| LLM Training & Optimization | 4 |
| LLM Post-Training & Fine-Tuning | 6 |
| LLM Reasoning & Alignment | 5 |
| CTR Prediction & Advertising | 9 |
| Recommendation (Generative & Agentic) | 9 |
| Sequential Recommendation | 10 |
| Games & Reinforcement Learning | 8 |
| Diffusion Models for Language | 1 |
| Interpretability & Analysis | 2 |
| **Total** | **54** |

### Key Themes

1. **CTR is scaling:** Multiple papers from major Chinese tech (Taobao, Xiaohongshu, JD, Tencent, Xianyu) show CTR models adopting Transformer architectures with power-law scaling, unified modeling, and LLM integration.
2. **Generative recommendation matures:** HSTU-style generative recommenders are being adopted (Meta, JD, Taobao) with improvements in causal attention formulation, preference alignment via RL, and long-sequence handling.
3. **Self-play for reasoning:** Multiple approaches (SPIRAL, STRATAGEM, CPMobius) show that zero-sum games and self-play can develop transferable reasoning without human-curated data.
4. **LLM efficiency pressures:** Fine-tuning papers focus on memory reduction (token ditching, layer selection, local learning) and optimizer innovation (Muown, ScheduleFree+, LoRA-Pre).
5. **Agentic recommendation:** A new paradigm is emerging where recommendation becomes a proactive, agent-driven service with memory management, report generation, and multi-agent reasoning.
