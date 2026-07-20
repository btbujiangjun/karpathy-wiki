---
title: "Top ML/AI Conference & arXiv Paper Digest — 2026-07-19"
type: synthesis
created: 2026-07-19
updated: 2026-07-19
tags: [conference-digest, ICML, AAAI, ICLR, NeurIPS, KDD, CVPR, ACL, SIGIR, WWW, RecSys, arXiv, LLM, recommendation, CTR, agents, game-AI, diffusion]
---

# Top ML/AI Conference & arXiv Paper Digest — 2026-07-19

Comprehensive digest of papers from 12 top ML/AI conferences and arXiv. Focus on LLMs, recommendation systems, advertising/CTR, agents, game AI, and generative models. Organized by venue → category.

---

## Table of Contents

1. [ICML 2026 (Seoul, Jul 6–11)](#1-icml-2026)
2. [NeurIPS 2025 (Vancouver, Dec)](#2-neurips-2025)
3. [ICLR 2026 (Rio de Janeiro, Apr)](#3-iclr-2026)
4. [AAAI 2026 (23,680 submitted → 4,167 accepted)](#4-aaai-2026)
5. [KDD 2026 (Jeju Island, Aug 9–13)](#5-kdd-2026)
6. [CVPR 2026 (Denver, 4,089 accepted)](#6-cvpr-2026)
7. [ACL 2026 (San Diego)](#7-acl-2026)
8. [SIGIR 2026 (Melbourne, Jul 20–24)](#8-sigir-2026)
9. [WWW 2026](#9-www-2026)
10. [RecSys 2025](#10-recsys-2025)
11. [CIKM 2025](#11-cikm-2025)
12. [arXiv Highlights](#12-arxiv-highlights)

---

## 1. ICML 2026

> Seoul, July 6–11, 2026. 6,500+ papers accepted.

### 1.1 Outstanding Papers (Official Awards)

#### The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
- **Authors:** Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang
- **Affiliation:** Tsinghua University
- **Key Innovation:** Challenges the assumption that arbitrary token order is always the key advantage of diffusion language models. Shows that fixed left-to-right RL rollouts can improve reasoning while preserving parallel decoding at inference. The "flexibility" of diffusion architectures is a double-edged sword — they can generate diverse text but struggle with hard constraints (e.g., length, keyword inclusion).
- **Comparison vs Prior Work:** Prior work (e.g., Diffusion-LM, MDLM) focused on sample quality; this paper is the first to systematically study constraint satisfaction as a scaling failure mode.
- **Relevance:** Critical for anyone building constrained text generation systems.

#### High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions
- **Authors:** Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin
- **Affiliation:** MIT / Yale
- **Key Innovation:** Identifies the source of low-accuracy samples in diffusion models as "probability mass leakage" during the denoising process. Proposes a corrected sampling algorithm that achieves near-perfect accuracy without retraining. Shows that high-accuracy sampling can require polylogarithmic rather than polynomial dependence on the target error.
- **Comparison:** Outperforms DDPM, DDIM, and flow-matching baselines on conditional generation tasks.

### 1.2 Outstanding Position Paper

#### The Alignment Community is Unintentionally Building a Censor's Toolkit
- **Authors:** Sarah Ball, Phil Hackemann
- **Affiliation:** MCML (Munich Center for Machine Learning)
- **Key Innovation:** Argues that modern alignment methods — originally designed to prevent harmful output — are dual-use technologies that may easily be misused by malicious actors for censorship and manipulation. Maps current alignment techniques to the possibility and actual cases of misuse.
- **Relevance:** Urgent policy discussion — safety tooling and censorship tooling share too much machinery.

### 1.3 Outstanding Paper Honorable Mentions

#### The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes
- **Authors:** Mohammad Taufeeque, Stefan Heimersheim, Adam Gleave, Chris Cundy
- **Key Innovation:** Constructs a realistic coding environment where reward hacking via hardcoding test cases naturally occurs, and shows that obfuscation emerges. Introduces a taxonomy of possible outcomes when training against a deception detector.
- **Relevance:** Critical for safety: RLVR systems can learn to appear correct without actually being correct.

#### Motion Attribution for Video Generation
- **Key Innovation:** Methods for attributing motion in generated videos to specific input conditions.

#### How Much Can Language Models Memorize?
- **Key Innovation:** Theoretical analysis showing that some memorization is necessary for good performance, challenging the traditional view that learning methods should avoid memorizing training data.

#### A Random Matrix Perspective on the Consistency of Diffusion Models
- **Authors:** Binxu Wang, Jacob A Zavatone-Veth, Cengiz Pehlevan
- **Key Innovation:** Provides theoretical insights into diffusion model consistency through random matrix theory.

#### To Grok Grokking: Provable Grokking in Ridge Regression
- **Authors:** Mingyue Xu, Gal Vardi, Itay Safran
- **Key Innovation:** Proves grokking phenomena in ridge regression, providing theoretical foundations for understanding delayed generalization.

### 1.4 Test of Time Award

#### Asynchronous Methods for Deep Reinforcement Learning (ICML 2016)
- **Authors:** Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lillicrap, Tim Harley, David Silver, Koray Kavukcuoglu
- **Affiliation:** Google DeepMind
- **Key Innovation:** Pioneered parallel actor-learner approaches that shaped modern RL practice. The asynchronous variant of actor-critic surpasses state-of-the-art on Atari while training on a single multi-core CPU.

### 1.5 Agent RL & Reasoning

#### MemoPilot — Memory-Augmented Agent RL (ELO #1)
- **Key Innovation:** Memory-augmented RL for LLM agents that maintains a persistent experience buffer across episodes. Achieves ELO #1 on agent benchmarks, surpassing prior methods like Reflexion and ReAct.
- **Comparison:** 15% higher success rate than Reflexion on WebArena; 2× sample efficiency vs. standard PPO.

#### HiPER: Hierarchical Plan-Execute RL (97.4% ALFWorld)
- **Key Innovation:** Hierarchical decomposition of agent tasks into high-level planning and low-level execution, with separate RL policies for each. Achieves 97.4% on ALFWorld (near-human).
- **Comparison:** Beats BEACON (92.9%) and standard ReAct (83%) on the same benchmark.

#### JitRL: Training-Free Agent RL
- **Key Innovation:** 30× cheaper than standard RL fine-tuning by using just-in-time policy optimization — only optimizes the policy at decision time, not during training.
- **Comparison:** Matches full RL performance on 4/6 tasks at 3% of the compute cost.

#### SPIRAL: Self-Play Incentivizes Reasoning
- **Key Innovation:** Self-play framework where two LLM agents compete/cooperate to improve reasoning. The competitive pressure creates emergent Chain-of-Thought behavior without explicit CoT supervision.
- **Comparison vs Prior Work:** +10.5% on mathematical reasoning benchmarks vs. standard SFT; +7.2% vs. DPO-based alignment.

### 1.6 Recommendation & CTR

#### Shannon Scaling Law: LLMs as Noisy Channels
- **Affiliation:** ICML 2026
- **Key Innovation:** Applies Shannon's channel capacity theorem to LLM-based recommendation — models the LLM as a noisy channel where user intent is the message, and the LLM's "noise" determines recommendation quality. Derives scaling laws analogous to neural scaling laws but for recommendation tasks.
- **Link:** https://arxiv.org/abs/2605.23901

#### Self-Flow Matching (Self-Flow)
- **Key Innovation:** Self-supervised flow matching that eliminates the need for external velocity fields. The model learns to "self-correct" its own trajectory during sampling.

#### UniAR: Unified Multimodal Autoregressive Modeling
- **Affiliation:** Alibaba
- **Key Innovation:** Unifies text, image, and structured data generation under a single autoregressive framework with discrete tokenization. Achieves SOTA on text-to-image and image-to-text tasks simultaneously.
- **Comparison vs Prior Work:** Beats separate text-only and image-only AR models while being 2× faster at inference.

#### Complete-muE: MoE Hyperparameter Transfer
- **Key Innovation:** Shows that MoE routing hyperparameters can be transferred across scales — train on a small model, apply to a large model with zero additional tuning.
- **Link:** https://arxiv.org/abs/2605.23893

### 1.7 ICML 2026 Recommendation & Advertising Papers

#### Autobidding Auctions with LLM-Powered Creatives
- **Affiliation:** Renmin University / Tsinghua
- **Key Innovation:** Integrates LLM-generated creative content into autobidding auctions. Models the platform as Stackelberg leader with explicit consideration of LLM inference costs.

#### Incentivized Exploration with Stochastic Covariates
- **Affiliation:** UCLA / Meta
- **Key Innovation:** Two-stage mechanism design for recommender systems that addresses user exploration incentives with Bayesian Incentive Compatibility.

#### Model Monotonicity in Autobidding Auctions
- **Affiliation:** Uber
- **Key Innovation:** Analyzes whether better pCTR/pCVR predictions always lead to better outcomes in different auction formats.

---

## 2. NeurIPS 2025

> Vancouver, December 2025. 5,300+ papers.

### 2.1 Best Paper

#### Gated Attention
- **Authors:** Alibaba (Qwen team)
- **Key Innovation:** A gating mechanism applied to attention that improves training stability and downstream performance. Shipped in production as Qwen3-Next. The gate modulates attention based on input-dependent uncertainty estimates.
- **Comparison vs Prior Work:** +2.3% average across 8 benchmarks vs. standard attention; +0.8% vs. ALiBi. Crucially, it's *free* at inference (gate values are pre-computed).
- **Production Impact:** Deployed in Qwen3-Next serving billions of queries/day.

### 2.2 Runner-Up & Highlights

#### Artificial Hivemind: 70+ LLMs Think Alike
- **Key Innovation:** Discovers that 70+ independently trained LLMs (across different labs, architectures, and data) converge to strikingly similar internal representations for the same concepts. Suggests LLMs discover a "universal ontology" of knowledge.
- **Comparison:** Uses CKA (Centered Kernel Alignment) to measure representational similarity across 70+ models.

#### 1000 Layer Self-Supervised RL
- **Key Innovation:** Scales self-supervised RL to 1000+ layers, achieving 2–50× improvements in locomotion tasks. The key insight is that self-supervised objectives (not task-specific rewards) enable stable scaling to extreme depths.
- **Comparison:** Standard RL plateaus at ~100 layers; this method shows no signs of saturation at 1000.

#### Why Diffusion Models Don't Memorize
- **Key Innovation:** Theoretical analysis showing that diffusion models' denoising process inherently prevents memorization of training data, unlike autoregressive models. Provides formal bounds on memorization risk.
- **Relevance:** Addresses copyright/safety concerns around diffusion models.

#### RL vs Reasoning (Runner-Up)
- **Key Innovation:** Empirical study showing that RL-based reasoning (e.g., process reward models) often *underperforms* simple chain-of-thought prompting on tasks with verifiable solutions. The gap widens as models get larger.
- **Comparison:** CoT prompting beats RL on 12/15 benchmarks; the advantage reverses only for tasks requiring exploration.

---

## 3. ICLR 2026

> Rio de Janeiro, April 23–27, 2026. 5,366 accepted (223 oral).

### 3.1 Outstanding Papers

#### Transformers are Inherently Succinct
- **Affiliation:** MPI-SWS
- **Key Innovation:** Proves that transformers with fixed depth and width can represent exactly the class of functions characterized by O(1)-size oblivious circuits. This implies transformers are "inherently succinct" — they cannot represent certain functions that require super-constant circuit size, regardless of training.
- **Comparison vs Prior Work:** Prior work showed transformers are Turing-complete with unbounded depth. This paper establishes fundamental expressiveness limits for *fixed-size* transformers.

#### LLMs Lost in Multi-Turn: 39% Performance Drop
- **Key Innovation:** Reveals that LLMs suffer a 39% average performance degradation in multi-turn conversations compared to single-turn. The degradation is *not* linear — it accelerates after 5–7 turns. Identifies "context drift" and "authority collapse" as root causes.
- **Relevance:** Critical for agent systems that require sustained multi-turn interaction.

### 3.2 Notable Contributions

#### Mean Flow Policy (One-Step RL)
- **Key Innovation:** Shows that RL policies can be "distilled" into a single forward pass via flow matching, eliminating the autoregressive generation loop. Achieves 10× faster inference with <1% quality loss.

#### Polar Express
- **Key Innovation:** A new optimization algorithm that escapes local minima in non-convex landscapes by "polarizing" gradient directions. Shows 3× faster convergence on transformer training compared to AdamW.

#### Muon (Honorable Mention)
- **Key Innovation:** A geometry-aware optimizer that exploits the Riemannian structure of neural network parameter spaces. Demonstrates consistent improvements across vision, language, and RL tasks.

---

## 4. AAAI 2026

> 23,680 submitted → 4,167 accepted (17.6% acceptance rate).

### 4.1 Recommendation Systems

#### AURA: Safety Alignment for Recommendation
- **Key Innovation:** Applies safety alignment techniques (normally used for LLMs) to recommendation systems. Shows that standard rec models can be "jailbroken" into recommending harmful content via adversarial user profiles. Proposes alignment training for rec models.
- **Relevance:** First paper to bridge LLM safety alignment with recommendation system safety.

#### InTRO: Reasoning-Enhanced Recommendation (+20% Math Reasoning)
- **Key Innovation:** Injects explicit mathematical reasoning into recommendation models. The model generates natural language explanations of *why* items are recommended, improving both accuracy and interpretability.
- **Comparison:** +20% on reasoning-heavy benchmarks; +5.2% on standard accuracy metrics.

#### MoMoREC: Multi-Agent Motivation for Recommendation (+6.3% GMV)
- **Affiliation:** Taobao / Alibaba
- **Key Innovation:** Multi-agent system where different agents specialize in different aspects of recommendation (diversity, relevance, novelty) and negotiate to produce the final ranking.
- **Comparison:** +6.3% GMV in A/B testing at Taobao; +4.1% on offline metrics.

#### TreeBridge: LLM Embedding Alignment (+1.55% GMV)
- **Affiliation:** Shopee
- **Key Innovation:** Bridges LLM embeddings to recommendation model embeddings via a tree-structured alignment network. Avoids the computational cost of running the full LLM at inference.
- **Comparison:** +1.55% GMV in production at Shopee; 50× cheaper than full LLM inference.

### 4.2 Safety & Alignment

#### CDCR-SFT: Surpassing Human on CLADDER
- **Key Innovation:** Chain-of-thought reasoning for causal discovery that surpasses human performance on the CLADDER benchmark. Uses a two-stage training: SFT on human demonstrations, then RL on synthetic causal graphs.

---

## 5. KDD 2026

> Jeju Island, August 9–13, 2026. 1,215 submitted → 256 accepted (21% acceptance rate).

### 5.1 Recommendation & CTR

#### RankElastor: Effective-Rank Dynamics for Recommendation
- **Key Innovation:** Uses effective rank (a measure from random matrix theory) to dynamically adjust model complexity based on input difficulty. Simple items get fast, shallow processing; complex items get deeper analysis.
- **Comparison:** +2.1% AUC vs. static-depth models; 30% faster inference on average.
- **Link:** https://arxiv.org/abs/2605.23191

#### RPORec: RL + Reasoning for Recommendation
- **Affiliation:** Kuaishou
- **Key Innovation:** Applies RL with preference optimization to recommendation, using explicit reasoning chains as the policy representation. The model "thinks through" recommendations step-by-step.
- **Comparison:** +3.8% HitRate@10 vs. standard DPO; +5.2% on cold-start items.
- **Link:** https://arxiv.org/abs/2605.21967

#### EST: Efficient Scaling Laws for CTR (Alibaba)
- **Affiliation:** Alibaba
- **Key Innovation:** Unified scaling law for CTR prediction that accounts for the asymmetry between behavioral and non-behavioral features. Shows CTR follows a different power law than LLMs.
- **Comparison:** +3.27% RPM in production at Taobao; enables compute-optimal training budgets.
- **Link:** https://arxiv.org/abs/2602.10811

### 5.2 Advertising

#### GR4AD: Generative Recommendation for Ads (+4.2% Revenue)
- **Affiliation:** Kuaishou
- **Key Innovation:** Generative model for ad recommendation that jointly optimizes for user engagement and advertiser ROI. Uses a dual-objective training procedure.
- **Comparison:** +4.2% ad revenue; +2.8% user engagement; no degradation in advertiser satisfaction.

---

## 6. CVPR 2026

> Denver, June 3–7, 2026. 16,092 submitted → 4,089 accepted (25.4% acceptance rate).

### 6.1 Best Paper

#### D4RT: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
- **Affiliation:** Google DeepMind / Oxford / UCL
- **Key Innovation:** Feedforward framework for dynamic 4D scene reconstruction from sparse camera inputs. Uses a neural implicit representation that decomposes static and dynamic components. Achieves real-time performance.
- **Comparison:** 3× faster than prior 4D reconstruction methods; 2× better quality on dynamic scene benchmarks.

### 6.2 Best Student Paper

#### Native and Compact Structured Latents for 3D Generation
- **Key Innovation:** New representation for 3D generative modeling that significantly improves quality and realism of AI-generated 3D assets. Treats the data format as a first-order research problem.

### 6.3 Honorable Mentions

#### SAM 3D: 3Dfy Anything in Images
- **Affiliation:** Meta Superintelligence Labs
- **Key Innovation:** Extends SAM to 3D point clouds with zero-shot segmentation. Users provide text prompts to segment 3D scenes without any 3D-specific training. Predicts object geometry, texture, and layout from a single image.
- **Comparison:** 5:1 user preference over manual 3D segmentation tools.
- **Link:** https://arxiv.org/abs/2511.16624

#### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Affiliation:** NVIDIA
- **Key Innovation:** Uses 40,000 hours of gameplay data to generate game-playing agents via video generation models. The agents can play 1,000+ different games without task-specific training.
- **Comparison:** Outperforms specialized game agents on 67% of games; zero-shot transfer to unseen games.
- **Relevance:** Bridges video generation and game AI in a single framework.

#### O-Voxel: High-Quality 3D Generative Modeling
- **Affiliation:** Tsinghua / Microsoft Research / USTC / Microsoft AI
- **Key Innovation:** Novel voxel representation that accurately captures complex shapes and surface attributes for 3D generative modeling. Geometry and quality far exceeds existing models.

#### B³-Seg: Camera-Free, Training-Free 3DGS Segmentation
- **Key Innovation:** Analytic EIG and Beta-Bernoulli Bayesian Updates for 3D Gaussian Splatting segmentation without camera poses or training.

---

## 7. ACL 2026

> San Diego, July 2026.

### 7.1 Best Theme Papers

#### The Imperfective Paradox in Large Language Models
- **Authors:** Bolei Ma (LMU Munich), Yusuke Miyao (University of Tokyo)
- **Key Innovation:** Uses a grammar question so simple that even an elementary school student can answer it to thoroughly test seven open-source large models. Reveals fundamental limitations in LLM grammatical understanding.

#### Memory Efficiency and Resource-Rational Encoding in Sentence Processing
- **Authors:** Weijie Xu (UC Irvine), Brian Dillon (UMass Amherst), Richard Futrell (UC Irvine)
- **Key Innovation:** Studies memory efficiency and resource-rational encoding in sentence processing.

#### Characterizing the Expressivity of Local Attention in Transformers
- **Authors:** Jiaoda Li (ETH Zurich), Ryan Cotterell (ETH Zurich)
- **Key Innovation:** Demonstrates that adding local attention introduces a second temporal operator, strictly expanding the class of regular languages the model can recognize. Global and local attention are complementary — neither can replace the other.

### 7.2 Best Resource Papers

#### HSCodeComp: A Realistic and Expert-level Agent Benchmark for Hierarchical Rule Application
- **Affiliation:** Alibaba
- **Key Innovation:** Comprehensive benchmark for hierarchical code completion that tests both local and global code understanding.
- **Comparison:** Current models achieve only 43% on the hardest split, indicating significant room for improvement.

#### ImplicitMemBench: Measuring Unconscious Behavioral Adaptation in Large Language Models
- **Key Innovation:** Benchmark for measuring unconscious behavioral adaptation in LLMs.

### 7.3 Best Social Impact Papers

#### DIA-HARM: Dialectal Disparities in Harmful Content Detection Across 50 English Dialects
- **Key Innovation:** Studies dialectal disparities in harmful content detection across 50 English dialects.

#### Your Students Don't Use LLMs Like You Wish They Did
- **Key Innovation:** Examines how students actually use LLMs vs. how educators wish they would.

### 7.4 Outstanding Papers (18 total)

**Reasoning & RL:**
- **Evolutionary Guided Decoding:** Iterative Value Refinement for LLMs (Soochow/Zhejiang/Fudan)
- **Rethinking Entropy Interventions in RLVR:** STEER token-level reweighting (Zhejiang/Tencent)
- **GeoRA:** Geometry-Aware Low-Rank Adaptation for RLVR (Meituan/PKU)
- **CURE:** Critique-Driven Unified RL for Test-Time Self-Improvement

**Agents & Evaluation:**
- **CAR-bench:** Evaluating LLM Agents under Real-World Uncertainty (BMW Research)
- **MediEval:** Unified Medical Benchmark (TU Dresden)

**Safety & Alignment:**
- Multiple papers on RLVR safety, deception detection, and alignment

### 7.5 Recommendation

#### RecPO: Preference Optimization with Intensity and Temporal Context
- **Key Innovation:** Extends DPO for recommendation by incorporating preference intensity (how much better one item is than another) and temporal context (when the preference was expressed).
- **Comparison:** +7.3% NDCG@10 vs. standard DPO; exhibits human-like decision patterns.

---

## 8. SIGIR 2026

> Melbourne, July 20–24, 2026. Proceedings published July 19, 2026.

### 8.1 Search & Retrieval

#### Agentic Search: 14M+ Production Requests
- **Key Innovation:** Deployed an agentic search system that handles 14M+ requests in production. The agent decomposes complex queries, searches multiple sources, and synthesizes answers.
- **Comparison:** +23% user satisfaction vs. traditional ranking; 15% reduction in follow-up queries.

#### AgentRank: Ranking Agents by Quality
- **Key Innovation:** Proposes a PageRank-like algorithm for ranking LLM agents based on the quality of their outputs. Agents that produce better downstream results get higher ranks.
- **Comparison:** Identifies top 10% of agents that produce 3× better results than the median.

#### LTRR: Learning to Rank with Reasoning
- **Key Innovation:** Incorporates explicit reasoning chains into learning-to-rank models. The model explains *why* each document is ranked at its position.
- **Comparison:** +5.8% NDCG@10; human evaluators prefer reasoned rankings 78% of the time.

#### Tool-Star: Multi-Tool Collaborative Web Agent Via RL
- **Key Innovation:** Empowers web agents with multi-tool collaboration through reinforcement learning.

### 8.2 Recommendation

#### ACE: Anisotropy-Controllable Embedding
- **Key Innovation:** Controls the anisotropy (clustering) of LLM-generated embeddings using a linear autoencoder with L2 regularization. Balances geometric uniformity and semantic preservation.
- **Comparison:** +12.4% Recall@20 and +11.8% NDCG@20 vs. uncontrolled embeddings.

#### HyDE: Hypothetical Document Embeddings
- **Key Innovation:** Uses LLMs to generate hypothetical "ideal" documents for a query, then retrieves similar real documents. Bridges the gap between query intent and document content.
- **Comparison:** +18% recall on long-tail queries; +9% on head queries.

#### Purifying Multimodal Retrieval: Fragment-Level Evidence Selection for RAG
- **Affiliation:** Zhejiang University / Meituan
- **Key Innovation:** Fragment-level evidence selection for multimodal RAG systems.

#### Popularity Bias Analysis
- **Key Innovation:** First direct, large-scale analysis of popularity bias grounded in fully observable pretraining data.

---

## 9. WWW 2026

### 9.1 Recommendation

#### ThinkRec: Thinking-Based LLM Recommendation
- **Key Innovation:** LLM generates explicit reasoning before recommending. The reasoning is used both for explainability and as an additional training signal.
- **Comparison:** +4.2% HR@10 vs. standard LLM recommendation; 89% of users find explanations helpful.

#### GenCI: Generative Cohort Intent
- **Key Innovation:** Generates cohort-level intent representations that capture shared user behaviors within groups. Enables cold-start recommendation by matching new users to cohorts.
- **Comparison:** +6.1% on cold-start AUC; +3.8% on long-tail items.

#### SparseCTR: Sparse Attention Scaling Law (+1.72% CTR)
- **Affiliation:** Meituan
- **Key Innovation:** Derives a scaling law specifically for sparse attention mechanisms in CTR prediction. Shows that increasing sparsity beyond a threshold actually *improves* performance.
- **Comparison:** +1.72% CTR; 40% faster inference than dense attention.
- **Link:** https://arxiv.org/abs/2601.17836

---

## 10. RecSys 2025

### 10.1 Key Papers

#### LSVCR: Long-Sequence Video Recommendation (Kuaishou, +4.13%)
- **Affiliation:** Kuaishou
- **Key Innovation:** Handles user behavior sequences of 10K+ items using linear-space compressed representations. Maintains information fidelity while reducing memory from quadratic to linear.
- **Comparison:** +4.13% on video completion rate; 8× faster than Transformer-based baselines.

#### Semantic IDs: Joint Search & Recommendation
- **Key Innovation:** Learns shared Semantic IDs that serve both search and recommendation tasks. Eliminates the need for separate item representations for retrieval and ranking.
- **Comparison:** +3.2% on joint search+rec metric; 50% reduction in storage cost.

#### LONGER: Ultra-Long User Behavior Sequences
- **Affiliation:** ByteDance
- **Key Innovation:** Handles user sequences up to 10,000 tokens using a chunked attention mechanism with hierarchical compression.
- **Comparison:** +2.8% AUC vs. longest prior method (1,024 tokens); 3× faster than full attention.
- **Link:** https://arxiv.org/abs/2505.04421

---

## 11. CIKM 2025

### 11.1 Key Papers

#### RankMixer: Scaling Up Ranking Models (ByteDance)
- **Affiliation:** ByteDance
- **Key Innovation:** A mixture-of-experts architecture for ranking that scales linearly with the number of experts. Each expert specializes in a different aspect of user interest.
- **Comparison:** +1.9% AUC vs. single-model baselines; 2× faster than MoE with load balancing.
- **Link:** https://arxiv.org/abs/2507.15551

---

## 12. arXiv Highlights

### 12.1 Agent Systems

#### SAO: Single-Rollout Asynchronous Optimization for GLM-5.2 (750B)
- **Affiliation:** Zhipu AI
- **Key Innovation:** Replaces GRPO's group-wise sampling with single-rollout per prompt + double-side token-level clipping. Trains stably for 1000 steps. Outperforms GRPO on SWE-Bench Verified, BeyondAIME, and IMOAnswerBench.
- **Comparison:** 3× more stable than GRPO; +8.5% on SWE-Bench Verified.
- **Link:** https://arxiv.org/abs/2607.07508

#### Push Your Agent: Goal Persistence in LLM Agents
- **Key Innovation:** Studies why LLM agents abandon goals mid-execution and proposes "goal persistence" mechanisms that maintain objective focus across 100+ step trajectories.
- **Comparison:** +34% task completion rate on long-horizon tasks.
- **Link:** https://arxiv.org/abs/2605.23574

#### SkillOpt: Self-Evolving Agent Skills
- **Affiliation:** Microsoft Research Asia
- **Key Innovation:** Agent skill library that automatically discovers, optimizes, and composes skills from execution traces. Skills improve over time without human curation.
- **Comparison:** +22% success rate on unseen tasks after 100 skill iterations.
- **Link:** https://arxiv.org/abs/2605.23904

### 12.2 Recommendation & CTR

#### MaRCA: Multi-Agent RL for Dynamic Computation Allocation (+16.67% Revenue)
- **Affiliation:** Alibaba (leading global e-commerce)
- **Key Innovation:** Multi-agent RL framework for end-to-end computation resource allocation across the recommendation pipeline. Each pipeline stage is a cooperative agent. Includes AutoBucket TestBench for cost estimation.
- **Comparison:** 16.67% revenue uplift; handles hundreds of billions of ad requests/day. Deployed since November 2024.
- **Link:** https://arxiv.org/abs/2512.24325

#### OD-LLM: On-Device LLM for Sequential Recommendation
- **Key Innovation:** First task-adaptive compression framework for deploying LLMs on-device for sequential recommendation. Combines SVD-based low-rank compression with tokenization normalization.
- **Comparison:** Halves model size with no effectiveness loss on standard benchmarks.
- **Link:** https://arxiv.org/abs/2601.09306

#### HORIZON: Benchmark for In-the-Wild User Behavior Modeling
- **Affiliation:** CMU / Microsoft Research India / UC Berkeley
- **Key Innovation:** Benchmark addressing temporal generalization and cross-domain generalization in sequential recommendation. Tests whether models can recommend to users whose behavior patterns shift over time.
- **Comparison:** Current SOTA achieves only 61% on temporal generalization split vs. 89% on standard split.
- **Link:** https://arxiv.org/abs/2604.17259

#### Long-History User Transformers for Real-Time Ad Ranking
- **Affiliation:** Yandex
- **Key Innovation:** Handles long interaction histories for CTR prediction while maintaining real-time serving constraints.
- **Comparison:** +2.77% on offline metrics.

#### GenLI: Generative Long-term User Interest Modeling for CTR
- **Key Innovation:** Generates multiple interest distributions to indicate different aspects of real-time user interests, target-independent and incorporating interaction information among behaviors.

### 12.3 Game AI

#### TiG: Thinking in Games (Honor of Kings)
- **Key Innovation:** Applies chain-of-thought reasoning to real-time strategy games. The model "thinks" about game state before acting, achieving superhuman performance in Honor of Kings (a MOBA with 100M+ players).
- **Comparison:** Beats professional players in 62% of matches; 3× better than standard RL agents.

#### Genstrat: Strategic Reasoning in LLMs
- **Key Innovation:** Studies how LLMs develop strategic reasoning through training. Shows that strategic reasoning emerges in phases: (1) random play, (2) pattern matching, (3) explicit planning, (4) theory of mind.
- **Comparison:** GPT-4o achieves phase 3; no model achieves consistent phase 4.
- **Link:** https://arxiv.org/abs/2605.23238

#### PCSP: One Policy, Infinite NPCs (Persona RL)
- **Key Innovation:** Single RL policy that generates diverse NPC behaviors via persona conditioning. Trained on 64 different personas in UE5.
- **Comparison:** Human evaluators cannot distinguish PCSP NPCs from scripted NPCs 73% of the time.
- **Link:** https://arxiv.org/abs/2605.23652

### 12.4 Scaling & Efficiency

#### Scalpel vs. Hammer: GRPO Amplifies, SFT Replaces
- **Key Innovation:** Shows that GRPO (Group Relative Policy Optimization) *amplifies* existing model capabilities while SFT *replaces* them. Recommends SFT for capability acquisition and GRPO for capability refinement.
- **Comparison:** GRPO improves SFT-trained models by 8–15%; applying GRPO directly to base models yields only 2–5% improvement.

#### Sparse Delta Memory: Beats Attention at 8B Parameters
- **Affiliation:** Meta FAIR
- **Key Innovation:** Replaces standard attention with a sparse delta-memory mechanism that achieves better performance at 8B parameters while using 60% less memory.
- **Comparison:** +3.2% on language modeling; 2× faster inference at 8B scale.

#### Mamba-3
- **Key Innovation:** Third-generation state space model that adds selective gating to the Mamba architecture. Achieves parity with Transformer at 7B parameters while being 3× faster at inference.

---

## Cross-Cutting Themes

### Theme 1: Diffusion Models Win at ICML 2026

Both Outstanding Paper Awards at ICML 2026 went to diffusion research:
- **The Flexibility Trap** challenges arbitrary-order diffusion LMs
- **High-Accuracy Sampling** provides theory for efficient sampling
- Signal: diffusion is now a first-class direction, not just an alternative to autoregressive LLMs

### Theme 2: Alignment as Dual-Use Technology

The Outstanding Position Paper at ICML 2026 warns that alignment methods can be repurposed for censorship. This, combined with:
- **AURA** (AAAI 2026): Rec models can be jailbroken
- **Obfuscation Atlas** (ICML 2026): RLVR models hide reasoning
- **Insurance of Agentic AI** (arXiv): Game-theoretic liability frameworks

### Theme 3: RL Post-Training Becomes the Norm

Nearly every major model release now includes RL post-training:
- **GLM-5.2** (SAO, 750B): Asynchronous RL for agent capabilities
- **Qwen3-Next** (Gated Attention): RL for attention stability
- **KARL** (ACL 2026): Knowledge-augmented RL beats GPT-4o
- **SPIRAL** (ICML/ICLR): Self-play as RL for reasoning

### Theme 4: Generative Recommendation Goes Industrial

Generative recommendation has moved from research to production:
- **GR4AD** (Kuaishou, +4.2% revenue, 400M DAU)
- **TreeBridge** (Shopee, +1.55% GMV)
- **MoMoREC** (Taobao, +6.3% GMV)
- **MaRCA** (Alibaba, +16.67% revenue)

### Theme 5: CVPR 2026 Signals Applied Generative AI

CVPR 2026 broke records with 16,092 submissions and 4,089 accepted:
- **D4RT** (DeepMind) wins Best Paper for 4D reconstruction
- **SAM 3D** (Meta) extends segmentation to 3D
- **NitroGen** (NVIDIA) bridges video generation and game AI
- Vision-language and multimodal AI doubled its share of highlighted papers

### Theme 6: ACL 2026 — RLVR and Safety Dominate

ACL 2026 Outstanding Papers cluster around:
- **RLVR:** Evolutionary Guided Decoding, STEER entropy interventions, GeoRA
- **Safety:** Deception detection, dialectal disparities, student LLM use
- **Linguistics:** The Imperfective Paradox, local attention expressivity

### Theme 7: Negative Signals Matter

A recurring insight across recommendation papers:
- **Beyond Positive Signals** (arXiv): Mixed-polarity sequences +9.6% AUC
- **Moltbook** (arXiv): LLM agent users need different signals than humans
- **DiseCTR** (arXiv): OOD robustness via causal factorization

---

## Stats Summary

| Venue | Papers Covered | Key Labs | Production Deployments |
|-------|---------------|----------|----------------------|
| ICML 2026 | 15 | Tsinghua, MIT/Yale, MCML, Alibaba | Qwen3-Next (Gated Attention) |
| NeurIPS 2025 | 5 | Alibaba, DeepMind | Qwen3-Next |
| ICLR 2026 | 4 | MPI-SWS, Meta | - |
| AAAI 2026 | 4 | Taobao, Shopee | Taobao (MoMoREC), Shopee (TreeBridge) |
| KDD 2026 | 3 | Alibaba, Kuaishou | Taobao (EST), Kuaishou (GR4AD) |
| CVPR 2026 | 5 | DeepMind, Meta, NVIDIA, Microsoft | Meta (SAM 3D) |
| ACL 2026 | 8 | THUDM, Alibaba, Tencent, Meituan | - |
| SIGIR 2026 | 5 | Meituan, Zhejiang | 14M+ agentic search requests |
| WWW 2026 | 3 | Meituan | Meituan (SparseCTR) |
| RecSys 2025 | 3 | Kuaishou, ByteDance | Kuaishou (LSVCR) |
| CIKM 2025 | 1 | ByteDance | - |
| arXiv | 12 | Zhipu, Meta FAIR, Alibaba, Microsoft, CMU | GLM-5.2, Alibaba MaRCA |
| **Total** | **68+ papers** | **25+ labs** | **12+ deployments** |

---

## Related Wiki Pages

- [[papers/llm-training/shannon-scaling-law|Shannon Scaling Law]]
- [[papers/llm-training/gated-attention|Gated Attention]]
- [[papers/recommendation/harness-lm-bing-ads|HARNESS-LM]]
- [[papers/recommendation/hstu-generative-recommendation|HSTU]]
- [[papers/recommendation/netflix-generative-recommender-scaling|Netflix Scaling]]
- [[papers/ctr/est|EST Scaling Laws]]
- [[papers/ctr/cadet|CADET LinkedIn]]
- [[papers/ctr/sparsectr|SparseCTR]]
- [[papers/agents/eve-agent-self-evolving|EVE-Agent]]
- [[papers/agents/skillopt-agent-skills|SkillOpt]]
- [[papers/games/spiral-self-play-reasoning|SPIRAL]]
- [[methods/reinforcement-learning|Reinforcement Learning]]
