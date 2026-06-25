---
title: "Conference & arXiv Digest — June 2026 | Top ML/AI Venues Roundup"
type: synthesis
created: 2026-06-25
updated: 2026-06-25
sources: []
tags: [conference-digest, icml-2026, iclr-2026, neurips-2025, aaai-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, recsys-2025, cikm-2025]
---

# Conference & arXiv Digest — June 2026

> Comprehensive roundup of recent papers across ICML 2026, ICLR 2026, NeurIPS 2025, AAAI 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025, covering LLMs, recommendation systems, CTR prediction, agents, generative models, games, and sequential modeling.

---

## Table of Contents

1. [ICML 2026 — Seoul](#1-icml-2026)
2. [ICLR 2026 — Rio de Janeiro](#2-iclr-2026)
3. [NeurIPS 2025 — San Diego](#3-neurips-2025)
4. [AAAI 2026 — Singapore](#4-aaai-2026)
5. [CVPR 2026 — Denver](#5-cvpr-2026)
6. [KDD 2026 — Jeju Island](#6-kdd-2026)
7. [ACL 2026 — San Diego](#7-acl-2026)
8. [EMNLP 2025 — Suzhou](#8-emnlp-2025)
9. [WWW 2026 — Dubai](#9-www-2026)
10. [SIGIR 2026 — Melbourne](#10-sigir-2026)
11. [RecSys 2025 — Prague](#11-recsys-2025)
12. [Industry Labs: Google DeepMind, OpenAI, Meta, Microsoft, NVIDIA, Apple, ByteDance, Alibaba](#12-industry-labs)

---

## 1. ICML 2026

**Location:** Seoul, South Korea | **Acceptance:** 6,352/23,918 (26.6%) | **Dates:** July 2026

### 1.1 LLM Training & Alignment

#### Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis (Self-Flow)
- **Authors:** Hila Chefer, Patrick Esser, Dominik Lorenz, Dustin Podell et al.
- **Affiliation:** NVIDIA / Academia
- **Innovation:** Integrates representation learning within the generative flow matching framework — self-supervised paradigm for multi-modal generation.
- **Comparison:** Prior flow matching methods rely on supervised signal; Self-Flow learns representations jointly with generation.

#### Do We Need Adam? Strong and Sparse RL with SGD in LLMs (Oral)
- **Affiliation:** Multiple
- **Innovation:** Demonstrates that SGD with proper sparsity can match or outperform AdamW for RL-based LLM post-training, challenging the dominant optimizer paradigm.

#### On the Convergence Rate of LoRA Gradient Descent (Oral)
- **Innovation:** Theoretical analysis of LoRA fine-tuning convergence, providing provable guarantees for low-rank adaptation dynamics.

#### Maximum Likelihood Reinforcement Learning (MaxRL) — **Oral**
- **Authors:** Fahim Tajwar, Guanning Zeng, Yueer Zhou et al.
- **Innovation:** Derives a compute-indexed family of sampling-based objectives from pass@k expansion of likelihood, interpolating between standard RL and exact MLE.
- **Results:** Consistently outperforms standard RL and GRPO, achieving higher pass@1 and substantially improved pass@k across multiple domains.
- **Paper:** ICML 2026 Oral

#### Learning Unmasking Policies for Diffusion Language Models (Oral)
- **Authors:** Metod Jazbec, Theo X. Olausson, Louis Béthune et al.
- **Innovation:** Uses RL to train sampling procedures for masked diffusion LLMs — lightweight single-layer transformer policy maps token confidences to unmasking decisions.
- **Results:** Matches SOTA heuristics with semi-autoregressive block generation, outperforms in full-diffusion setting.

#### You Can Learn Tokenization End-to-End with RL
- **Authors:** Sam Dauncey, Roger Wattenhofer
- **Innovation:** Tokenization as an RL problem — score function estimates for discrete token boundaries, tighter theoretical guarantees than heuristic methods.

### 1.2 Agents & Reasoning

#### daVinci-Dev: Agent-native Mid-training for Software Engineering (Oral)
- **Innovation:** Mid-training paradigm that embeds software engineering capabilities into LLM agents via curated code interaction trajectories.

#### Strategic Navigation or Stochastic Search? How Agents and Humans Reason Over Document Collections (Oral)
- **Innovation:** Comparative study of LLM agent vs. human search strategies over complex document collections.

#### Scaling Agentic Programs
- **Innovation:** Searches over agent program behaviors at scale to discover optimal agentic patterns.

#### ALIVE: Evaluating Games at Scale
- **Innovation:** ALIVE evaluation mechanism balancing reliability with scalability for game-playing agents.

### 1.3 Multimodal & Vision-Language

#### Unified Multimodal Autoregressive Modeling with Shared Context
- **Innovation:** Proposes that visual tokenizer design is key to unification — shared context across modalities.

#### iTryOn: Interactive Video Virtual Try-On Framework (Taotian Group / Alibaba)
- **ArXiv:** 2605.21431
- **Innovation:** 3D hand prior + Action-aware RoPE + Action-aware Constraint loss for video try-on. Treats it as conditional generation guided by clothing images and action semantics.
- **Results:** State-of-the-art on interactive and traditional video try-on benchmarks.

#### HiDe: Hierarchical Decoupling of Zoom-In for High-Resolution MLLMs (Taotian Group / Alibaba)
- **ArXiv:** 2510.00054
- **Innovation:** Four sub-operations decomposition (zoom-and-crop, TAD, LPD, single-tensor offloading). Reduces peak memory from 96GB to ~20GB.
- **Results:** SOTA on V*Bench and HRBench, cuts memory 75% and halves inference latency.

#### E-VAds: Benchmark for E-commerce Short-Video Understanding (Taotian Group)
- **ArXiv:** 2602.08355
- **Results:** Improves performance by 109.2% over strong baselines.

#### Less is Enough: Synthesizing Diverse Data in Feature Space of LLMs (Oral)
- **Innovation:** Data synthesis approach in LLM feature space — less data but more diverse.

### 1.4 Diffusion & Generative Models

#### OPUS: Efficient Principled Data Selection for LLM Pre-training (Oral)
- **Innovation:** Data selection framework with theoretical guarantees for every iteration of LLM pre-training.

#### Diffract: Spectral View of LLM Domain Adaptation (Oral)
- **Innovation:** Analyzes LLM domain adaptation through spectral lens — reveals how different frequency components transfer.

---

## 2. ICLR 2026

**Location:** Rio de Janeiro, Brazil | **Acceptance:** 5,355/19,525 (27.4%) | **Dates:** April 23-27, 2026

### 2.1 Outstanding Papers

#### Transformers are Inherently Succinct (Outstanding Paper)
- **Authors:** Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin
- **Innovation:** Theoretical proof that Transformers encode concepts more succinctly than RNNs — explains architectural power from representational efficiency perspective.

#### Multi-Turn LLM Evaluation (Outstanding Paper)
- **Innovation:** Scalable method to evaluate multi-turn capabilities; finds marked decrease in LLM aptitude and reliability in multi-turn interactions with underspecified instructions.

### 2.2 LLM Reasoning & RL

#### ReTool: RL for Strategic Tool Use in LLMs
- **Authors:** Jiazhan Feng, Shijue Huang, Xingwei Qu et al.
- **Innovation:** Dynamic interleaving of real-time code execution within natural language reasoning + RL paradigm for tool invocation timing.
- **Trend:** GRPO appears in 157 ICLR papers vs. DPO in only 55 — the field has shifted.

#### In-Place Test-Time Training (In-Place TTT)
- **Authors:** Guhao Feng, Shengjie Luo, Kai Hua et al.
- **Innovation:** Framework that seamlessly endows LLMs with test-time training ability without separate adaptation phases.

#### MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent
- **Innovation:** RL-based memory management agent for long-context LLMs.

#### RAIN-Merging: Gradient-Free Method for Instruction Following in Large Reasoning Models
- **Innovation:** Preserves thinking format while enhancing instruction following — model merging without gradient computation.

#### Reducing Belief Deviation in RL for Active Reasoning of LLM Agents (Oral)
- **Innovation:** Belief deviation reduction mechanism for more stable RL-based reasoning.

### 2.3 Architectures & Efficiency

#### Mamba-3: Improved Sequence Modeling using State Space Principles
- **Innovation:** Third-generation Mamba with enhanced SSM principles — 202 papers at ICLR mention Mamba/SSMs.

#### Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Resource
- **Innovation:** Demonstrates MoE outperforms dense models under equal FLOP/parameter budgets with proper routing.

#### Let Features Decide Their Own Solvers: Hybrid Feature Caching for Diffusion Transformers (Oral)
- **Innovation:** Adaptive caching strategy where features decide computation paths.

### 2.4 Alignment & Safety

#### SafeDPO: A Principled Approach to Direct Preference Optimization
- **Innovation:** Balances helpfulness and safety in DPO training.

#### Why DPO is a Misspecification (Oral)
- **Innovation:** Formal analysis of DPO's misspecification issues.

#### Benchmarking Empirical Privacy Protection for LLM Adaptations (Oral)
- **Innovation:** Comprehensive privacy evaluation framework for fine-tuned LLMs.

### 2.5 Apple Research at ICLR 2026

#### ParaRNN: Unlocking Parallel Training of Nonlinear RNNs for LLMs (Oral)
- **Innovation:** 665× speedup over traditional sequential RNN training; enables first 7B-parameter classical RNNs competitive with Transformers.

#### To Infinity and Beyond: Tool-Use Unlocks Length Generalization in SSMs (Oral)
- **Innovation:** Shows SSMs fail on long-form tasks beyond memory capacity; tool-use (external memory) unlocks length generalization.

---

## 3. NeurIPS 2025

**Location:** San Diego, CA + Mexico City | **Acceptance:** ~5,200/21,575 (24.5%) | **Dates:** December 2-7, 2025

### 3.1 Best Papers

#### Gated Attention for Large Language Models (Best Paper)
- **Authors:** Zihan Qiu et al.
- **Innovation:** Head-specific sigmoid gate after standard softmax attention. Tested on 15B MoE and 1.7B dense models up to 3.5T tokens.
- **Results:** Improved stability, long-context performance, eliminated "attention sink" problem.
- **Impact:** Simple modification, likely to be widely adopted.

#### 1000 Layer Networks for Self-Supervised RL: Scaling Depth Enables New Goal-Reaching Capabilities (Best Paper)
- **Innovation:** Scales ResNet-style depth to 1000 layers for self-supervised RL — 2× success rate improvement, qualitative behavior changes at depth.
- **Key Insight:** Scaling depth in RL unlocks capabilities absent in shallower networks.

#### Why Diffusion Models Don't Memorize (Best Paper)
- **Innovation:** Identifies implicit dynamical regularization in diffusion training that prevents memorization; overfitting disappears at infinite training times.

#### Artificial Hivemind: Open-Ended Homogeneity of Language Models (Best Paper — DB Track)
- **Innovation:** Systematic study of mode collapse across LLMs — measures homogeneity and proposes mitigation strategies.

### 3.2 Runner-Up Papers

#### Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?
- **Key Finding:** RLVR-trained models outperform base models at smaller k values but the advantage diminishes; RL elicits vs. creates reasoning.

#### Superposition Yields Robust Neural Scaling
- **Innovation:** Superposition (features encoded in overlapping representations) yields more robust scaling laws.

#### Optimal Mistake Bounds for Transductive Online Learning
- **Innovation:** Tight theoretical bounds for transductive online learning settings.

---

## 4. AAAI 2026

**Location:** Singapore EXPO | **Acceptance:** 4,167/23,680 (17.6%) | **Dates:** January 20-27, 2026

### 4.1 Outstanding Papers

#### LLM2CLIP (Outstanding Paper)
- **Innovation:** Leverages LLM knowledge to enhance CLIP-style vision-language representations.

#### ReconVLA: Vision-Language-Action via Reinforcement Learning (Outstanding Paper)
- **Innovation:** RL-based VLA for robotic manipulation — combines auto-regressive backbone with Flow-Matching Action Expert.
- **Results:** SOTA on SimplerEnv and LIBERO benchmarks; deployed on Galaxea A1 robot.

#### CADYT: Causal Structure Learning (Outstanding Paper)
- **Innovation:** Efficient causal discovery from observational data.

### 4.2 LLM Reasoning & Hallucination

#### CDCR-SFT: Mitigating Hallucinations via Causal Reasoning
- **Authors:** Yuangang Li et al. (USC / Stanford / Johns Hopkins)
- **Innovation:** Trains LLMs to construct explicit causal DAGs then reason over them. CDCR-SFT dataset: 25,368 samples.
- **Results:** 95.33% accuracy on CLADDER (surpasses human 94.8% for first time); 10% hallucination reduction on HaluEval.

#### LENS: Learning to Segment Anything with Unified Reinforced Reasoning (Outstanding)
- **Authors:** Lianghui Zhu et al.
- **Innovation:** RL framework jointly optimizing reasoning process and segmentation end-to-end — CoT reasoning at test time for segmentation tasks.

### 4.3 Code Generation

#### Towards Better Correctness and Efficiency in Code Generation
- **Authors:** Alibaba/Qwen Team
- **Innovation:** Efficiency-aware code generation — addresses poor runtime efficiency of LLM-generated code.

---

## 5. CVPR 2026

**Location:** Denver, CO | **Acceptance:** 4,090/16,092 (25.4%) | **Dates:** June 2026

### 5.1 Best Papers

#### D4RT: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time (Best Paper)
- **Authors:** Chuhan Zhang, Guillaume Le Moing, Skanda Koppula et al. (Google DeepMind / UCL / Oxford)
- **Innovation:** Unified transformer for 4D dynamic scene reconstruction — estimates depth, spatio-temporal correspondence, camera parameters.
- **Results:** Lightweight, highly scalable training and inference.

#### Native and Compact Structured Latents for 3D Generation (Best Paper)
- **Authors:** Jianfeng Xiang et al. (Tsinghua / Microsoft Research / USTC / Microsoft AI)
- **Innovation:** O-Voxel representation for 3D generation — captures complex topologies and surface attributes.
- **Results:** Significantly exceeds existing 3D generation models in geometry and quality.

#### SAM 3D: 3Dfy Anything in Images (Best Paper)
- **Authors:** Meta Superintelligence Labs (Xingyu Chen, FU-JEN CHU, Pierre Gleize et al.)
- **Innovation:** Generative model for visually grounded 3D object reconstruction from single image — predicts geometry, texture, layout.
- **Results:** At least 5:1 win rate in human preference tests.

### 5.2 Generative Models

#### MacTok: Robust Continuous Tokenization for Image Generation (Best Paper)
- **Authors:** Hengyu Zeng et al.
- **Innovation:** Continuous tokenization for image generation — bridges discrete VQGAN and continuous diffusion.

#### A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens (Best Paper)
- **Authors:** Tommie Kerssies et al.
- **Innovation:** Delta token representation for world models — each frame compressed to one token via temporal differencing.

#### Back to Basics: Let Denoising Generative Models Denoise
- **Authors:** Tianhong Li, Kaiming He
- **Innovation:** Reframes diffusion models to focus on the denoising objective itself.

#### BPGO: Bayesian Prior-Guided Optimization for Visual Generation
- **Authors:** Ruiying Liu et al.
- **Innovation:** Extends GRPO with Bayesian trust allocation — inter-group and intra-group uncertainty modeling.
- **Results:** Stronger semantic alignment, enhanced perceptual fidelity, faster convergence than standard GRPO.

### 5.3 Vision-Language Models

#### Molmo2: Open Weights and Data for VLMs with Video Understanding and Grounding (Best Paper)
- **Authors:** Christopher Clark, Jieyu Zhang et al. (Allen AI / Academia)
- **Innovation:** Open-source VLM with video understanding, grounding, and full open data release.

#### WorldGen: From Text to Traversable and Interactive 3D Worlds
- **Authors:** Dilin Wang et al. (Meta / Academia)
- **Innovation:** Language-driven procedural generator + image gen + image-to-3D for complete 3D worlds decomposable into individual meshes.

### 5.4 Trends
- **VLMs doubled** to 10.6% of highlighted papers (largest sub-field)
- **Video generation + world models** jumped to 8.8% (+5.0pp)
- **Classic CV** (detection, segmentation, tracking) in retreat: 3.8% → 1.2%

---

## 6. KDD 2026

**Location:** Jeju Island, Republic of Korea | **Dates:** August 9-13, 2026

### 6.1 Recommendation Systems

#### Congrats: Consistent Graph-structured Generative Recommendation
- **Affiliation:** Kuaishou
- **Innovation:** Identifies "likelihood trap" in generative recommenders — proposes Graph-structured Model with multiple decoding paths + Consistent Differentiable Training.
- **Results:** Deployed on Kuaishou (300M+ DAU) — significantly improves quality and diversity.

#### MixRAGRec: Mixture-of-Experts KG-RAG for Multi-Agent LLM Recommendation
- **Affiliation:** Multiple
- **Innovation:** Three-agent framework: MoE Retrieval Agent + Knowledge Preference Alignment Agent + Contrastive Learning-reinforced Recommendation Agent. Trained with Mixture-of-Experts Multi-Agent Policy Optimization (MAPO).

#### SPiKE: Semantic Profiles into KG for Recommender Systems Using LLMs
- **Innovation:** LLM-generated semantic profiles for KG entities + Profile-aware KG aggregation + Pairwise profile preference matching.
- **Results:** Consistently outperforms SOTA KG- and LLM-based recommenders.

#### LLM-as-a-Judge for Reliable and Explainable Offline Evaluation in Top-K Recommendation
- **Authors:** Yue Que, Junyi Zhou et al.
- **Innovation:** Semantic proxy for user preference + semantic matching principle — replaces reliance on supplementary test sets.

#### Climber-Pilot: Non-Myopic Generative Recommendation for Instruction Following
- **Affiliation:** NetEase Cloud Music
- **Innovation:** Time-Aware Multi-Item Prediction (TAMIP) + Condition-Guided Sparse Attention (CGSA).
- **Results:** 4.24% lift in core business metric at NetEase Cloud Music.

#### One Sequential Recommendation Model Pretrained from Synthetic Priors (SRPFN)
- **Authors:** Woosung Kang et al. (KAIST)
- **Innovation:** Pretrained on synthetic data (hDCSBM-generated graphs) — adapts to target datasets in a single forward pass without gradient updates.
- **Results:** 7.53% avg improvement over second-best; ~1 minute inference on new dataset vs. hours for baselines.

#### Beyond Interleaving: Causal Attention Reformulations for Generative Recommenders
- **Innovation:** AttnLFA and AttnMVP — eliminate item-action interleaving noise by encoding causality directly into attention. Reduces training time and computation.

#### HyFormer: Revisiting Sequence Modeling and Feature Interaction in CTR
- **Affiliation:** ByteDance
- **ArXiv:** 2601.12681
- **Innovation:** Unified Transformer integrating long-sequence modeling and feature interaction — Query Decoding + Query Boosting components.
- **Results:** Deployed on Douyin Search — 3B samples, 70-day window. Outperforms LONGER + RankMixer baselines.

### 6.2 CTR Prediction

#### From Scaling to Structured Expressivity: Rethinking Transformers for CTR (FAT)
- **ArXiv:** 2511.12081
- **Innovation:** Field-Aware Transformer with Basis-Composed Hypernetwork — shifts complexity from vocabulary size n to field count F.
- **Results:** Up to +4.38% AUC, +2.33% CTR, +0.66% RPM in production.

#### HeMix: Query-Mixed Interest Extraction for Scalable CTR
- **Affiliation:** AMAP (Alibaba)
- **ArXiv:** 2602.09387
- **Innovation:** Query-Mixed Interest Extraction + Heterogeneous Interaction — scalable CTR model.
- **Results:** Deployed on AMAP: +3.61% GMV, +2.78% PV_CTR, +2.12% UV_CVR over DLRM.

---

## 7. ACL 2026

**Location:** San Diego, California | **Dates:** July 2-7, 2026

### 7.1 Reasoning Architectures

#### Graph Reasoning Paradigm (GRP): Structured and Symbolic Reasoning with Topology-Aware RL
- **Authors:** Runxuan Liu et al.
- **Innovation:** PASC-GRPO uses graph-structured representations with step-level cognitive labels — replaces semantic evaluation with structured evaluation.
- **Results:** Significant improvements on math reasoning and code generation.

#### KARL: Knowledge-Augmented RL for LLM Agents on Multi-Turn Tasks
- **Authors:** Xueqiao Sun et al. (Tsinghua)
- **Innovation:** Online RL with curiosity-driven reward shaping for proactive knowledge exploration.
- **Results:** Qwen2.5-14B agent outperforms GPT-4o, Claude-4, o4-mini on 6 knowledge benchmarks.

#### Meta-Reasoner: Dynamic Guidance for Optimized Inference-time Reasoning
- **Innovation:** Contextual multi-armed bandits learn adaptive policy for reasoning strategy selection (backtrack, switch, restart).
- **Results:** +9-12% accuracy, 28-35% inference time reduction.

#### Think in Sentences: Explicit Sentence Boundaries Enhance LLM Capabilities
- **Innovation:** Teaching models to generate explicit sentence boundary delimiters via ICL or SFT.
- **Results:** Up to 7.7% on GSM8k, 12.5% on DROP; works from 7B to 600B+ parameters.

### 7.2 Constrained Generation

#### MetaJuLS: Adaptive Constraint Propagation via Meta-RL
- **Innovation:** GNN-based policy learned with meta-RL for constraint propagation — 1.5-2.0× speedups over GPU-optimized baselines.

### 7.3 Beyond 'Aha!': Meta-Abilities Alignment for Large Reasoning Models
- **Innovation:** Three-stage pipeline (individual alignment, parameter-space merging, domain-specific RL) for deduction, induction, abduction.
- **Results:** +10% over instruction-tuned baselines; 7B and 32B models across math, coding, science.

---

## 8. EMNLP 2025

**Location:** Suzhou, China | **Dates:** November 2025

### 8.1 Key Papers

#### Mind the Blind Spots: Focus-Level Evaluation Framework for LLM Reviews (SAC Highlight)
- **Innovation:** Focus distribution framework for evaluating LLM-generated peer reviews.
- **Finding:** LLMs consistently biased toward technical validity, significantly overlook novelty assessment.

#### ECom-Bench: LLM Agent Benchmark for E-commerce Customer Support
- **Authors:** Haoxin Wang et al.
- **Innovation:** First benchmark for multimodal LLM agents in e-commerce customer support.
- **Results:** GPT-4o achieves only 10-20% pass3 metric.

#### Unconditional Truthfulness: Learning Unconditional Uncertainty of LLMs
- **Innovation:** Attention-based uncertainty quantification for LLMs.

#### Mitigating Catastrophic Forgetting with Forgetting-aware Pruning
- **Innovation:** Prunes parameter updates to mitigate catastrophic forgetting during continual learning.

### 8.2 Industry Track

#### ECom-Bench: LLM Agent for E-commerce Support
- **Affiliation:** Xiaoduo AI Lab

---

## 9. WWW 2026

**Location:** Dubai, United Arab Emirates | **Dates:** April 13-17, 2026

### 9.1 CTR Prediction

#### SparseCTR: Sparse Attention on Long-term Behaviors for CTR
- **Affiliation:** Meituan / Chinese Academy of Sciences
- **ArXiv:** 2601.17836
- **Innovation:** Three-branch sparse self-attention (global interests, interest transitions, short-term) + composite relative temporal encoding.
- **Results:** Scaling law across 3 orders of magnitude FLOPs. Online: +1.72% CTR, +1.41% CPM.

#### LLaCTR: Lightweight LLM-enhanced CTR via Field-Level Enhancement
- **Authors:** Yu Cui et al. (Zhejiang University / Alibaba)
- **ArXiv:** 2505.14057
- **Innovation:** Field-level enhancement paradigm — LLMs enrich field representations; integrates with 6 representative CTR models.
- **Results:** Outperforms 4 LLM-enhanced CTR methods in 89% of cases.

#### GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning
- **ArXiv:** 2601.18251
- **Innovation:** Generative user intent framework using semantic interest cohorts — NTP-trained generative model produces candidate interest cohorts + hierarchical candidate-aware network.

#### DAIAN: Deep Adaptive Intent-Aware Network for Trigger-Induced Recommendation
- **Affiliation:** Alibaba (Xianyu)
- **ArXiv:** 2602.13971
- **Innovation:** Hybrid enhancer with ID + semantic information for intent mining.
- **Results:** Online: +1.59% CTR, +1.73% diversity, +2.37% bills at Xianyu.

#### Multi-Branch Cooperation Networks for CTR in E-Commerce Search
- **Affiliation:** Alibaba
- **Innovation:** Multi-branch architecture for large-scale e-commerce search CTR.

### 9.2 Industry Track Highlights

#### AliBoostV2: CTR-Growth Balanced Boosting Framework (Alibaba)
- **Innovation:** Boosting framework balancing CTR and business growth at billion-scale.

#### GPU-accelerated Multi-relational Parallel Graph Retrieval (Baidu)
- **Innovation:** GPU-accelerated graph retrieval for web-scale recommendations.

#### Make It Long, Keep It Fast: 10k-Sequence Modeling on Douyin (ByteDance)
- **Affiliation:** ByteDance
- **Innovation:** End-to-end 10K-length sequence modeling at billion-scale for Douyin.

#### Not All Candidates Are Equal: Heterogeneity-Aware Pre-ranking (ByteDance)
- **Innovation:** Heterogeneity-aware pre-ranking in recommender systems.

---

## 10. SIGIR 2026

**Location:** Melbourne, Australia | **Dates:** July 20-24, 2026

#### GenRec: Preference-Oriented Generative Framework at JD.com
- **Affiliation:** JD.com
- **ArXiv:** 2604.14878
- **Innovation:** Page-wise NTP + asymmetric linear Token Merger + GRPO-SR (GRPO with NLL regularization + Hybrid Rewards).
- **Results:** Month-long A/B test: +9.5% click count, +8.7% transaction count.

#### SIGMA: Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress
- **Affiliation:** Alibaba (AliExpress)
- **ArXiv:** 2602.22913
- **Innovation:** Hybrid item tokenization + multi-task SFT dataset + three-step generation with adaptive probabilistic fusion.
- **Results:** 2-week A/B test at AliExpress: +2.80% Order Volume, +3.84% CVR, +7.84% GMV.

#### Diff-MSIN: Diffusion-based Multi-modal Synergy Interest Network for CTR
- **Venue:** SIGIR 2025
- **Innovation:** FDAF module for multi-modal CTR — captures synergistic, common, and special information across modalities.
- **Results:** +1.67% improvement over SOTA.

---

## 11. RecSys 2025

**Location:** Prague, Czech Republic | **Dates:** September 22-26, 2025

#### DiffuMIN: Diffusion-driven Multi-Interest Network for Long-term CTR
- **ArXiv:** 2508.15311
- **Innovation:** Target-oriented multi-interest extraction + diffusion module guided by contextual interests.
- **Results:** Online A/B: +1.52% CTR, +1.10% CPM.

#### S-GRec: Semantic-Aware Generative Recommendation with Asymmetric Advantage
- **Affiliation:** Tencent (WeChat Channels)
- **ArXiv:** 2602.10606
- **Innovation:** Two-stage Personalized Semantic Judge (PSJ) + Asymmetric Advantage Policy Optimization (A2PO). Decouples online lightweight generator from offline LLM judge.
- **Results:** Online WeChat Channels: +1.19% GMV, +1.16% CTR, -2.02% dislike rate.

---

## 12. Industry Labs

### Google DeepMind

#### LEAP: Supercharging LLMs for Formal Mathematics with Agentic Frameworks
- **ArXiv:** 2606.03303
- **Innovation:** Proof as graph of goals/subgoals — LLM plans, splits work, reuses lemmas, learns from Lean verifier feedback.
- **Results:** Solved all 12 Putnam 2025 problems; raised general LLM performance on IMO Lean benchmark from <10% to 70%. Solved Erdős problem 527.

#### AutoHarness: Synthesizing Code Harnesses for LLM Agents
- **ArXiv:** 2603.03329
- **Innovation:** Gemini-2.5-Flash auto-generates code harness preventing illegal moves in 145 TextArena games.
- **Results:** Smaller model (Flash) outperforms larger models (Pro, GPT-5.2-High) with synthesized code policy.

#### MiRA: Milestoning RL for Long-Horizon Web Agents
- **ArXiv:** 2603.19685
- **Innovation:** Subgoal decomposition + dense milestone rewards. Gemma3-12B + MiRA: 6.4% → 43.0% on WebArena-Lite.
- **Comparison:** Surpasses GPT-4-Turbo (17.6%), GPT-4o (13.9%), WebRL (38.4%).

#### Efficient Exploration at Scale for RLHF (10-1000× Data Efficiency)
- **ArXiv:** 2603.17378
- **Innovation:** Affirmative nudge + epistemic neural network for reward uncertainty + information-directed exploration.
- **Results:** Matches offline RLHF trained on 200K labels using <20K labels (10×). Extrapolated: 1M labels matches 1B labels (1000×).

#### AlphaEvolve: Discovering Multiagent Learning Algorithms with LLMs
- **ArXiv:** 2602.16928
- **Innovation:** LLM-powered evolutionary search discovers VAD-CFR and SHOR-PSRO algorithms — competitive with human-designed baselines across 18-game suite (Poker, Goofspiel, Liar's Dice, Blotto, Battleship).

#### Advancing Mathematics Research with AI-Driven Formal Proof Search
- **ArXiv:** 2605.22763
- **Innovation:** First large-scale evaluation of AI solving open math problems. Resolved 9/353 open Erdős problems, proved 44/492 OEIS conjectures.

#### Improving Interactive In-Context Learning from Natural Language Feedback
- **ArXiv:** 2602.16066
- **Innovation:** Multi-turn didactic interactions driven by information asymmetry — transforms feedback into trainable skill.
- **Results:** Smaller model (Gemma) interactive ability nearly reaches model an order larger.

### NVIDIA

#### Nemotron 3 Super (120B-A12B) & Nemotron 3 Ultra (550B-A55B)
- **ArXiv:** 2604.12374
- **Innovation:** Hybrid Mamba-Attention MoE + LatentMoE + Multi-Token Prediction + NVFP4 pre-training.
- **Results:** Up to 7.5× higher inference throughput vs. Qwen3.5-122B; up to 5.9× vs. GLM-5.1-754B. Supports up to 1M context.

#### Sol-RL: FP4 Explore, BF16 Train — Diffusion RL via Efficient Rollout Scaling
- **ArXiv:** 2604.06916
- **Innovation:** Two-stage RL: NVFP4 rollouts for exploration → BF16 regeneration for training. Decouples exploration from optimization.
- **Results:** Up to 4.64× training convergence acceleration. Works on SANA, FLUX.1, SD3.5-L.

#### GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors
- **ArXiv:** 2606.05160
- **Innovation:** Fully virtual pipeline: 3D assets + video foundation model priors → 4D HOI trajectories → sim-to-real on Unitree G1.
- **Results:** 84% real-world pick-up success, 90% stair-climbing. 20,000+ generated sequences.

#### Introspective Training (IXT): Feedback Conditioning Improves Scaling Across All LLM Training Stages
- **ArXiv:** 2605.20285
- **Innovation:** Offline reward-conditioned RL for data annotation → prefix-conditioning with natural language critiques.
- **Results:** Up to 2.8× compute efficiency; trained up to 18T tokens.

### Meta AI

#### Deep Think with Confidence (DeepConf)
- **Innovation:** Model-internal confidence signals to filter low-quality reasoning traces. No additional training needed.
- **Results:** Up to 99.9% on AIME 2025 at @512; reduces tokens by 84.7%.

#### SAM 3D (CVPR 2026 Best Paper)
- **Innovation:** Generative 3D object reconstruction from single image — geometry, texture, layout.
- **Results:** 5:1 win rate in human preference.

#### SPG: Sandwiched Policy Gradient for Masked Diffusion Language Models
- **Innovation:** New policy gradient variant for diffusion LLMs.

### Apple

#### Entropy Control in Policy Gradient for LLM Reasoning (REPO / ADAPO)
- **ArXiv:** 2603.11682
- **Innovation:** Proves PPO clips entropy, DAPO/GSPO implicitly preserve it. Proposes REPO (advantage modification) and ADAPO (adaptive asymmetric clipping).
- **Results:** SOTA on AppWorld (79% Normal, 71% Challenge). Closes gap between off-policy and on-policy training.

#### Apple Neural Engine Reverse-Engineering (A11–A18, M1–M5)
- **ArXiv:** 2606.22283
- **Innovation:** First comprehensive reverse-engineered documentation of ANE — datapath, roofline, dispatch, compiler, firmware, weight compression.
- **Coverage:** A11 through A18, M1 through M5 families.

### ByteDance

#### HyFormer (KDD 2026)
- Unified Transformer for long-sequence + feature interaction. Deployed on Douyin Search (3B samples).

#### Make It Long, Keep It Fast: 10k-Sequence Modeling at Billion Scale (WWW 2026 Industry)
- End-to-end long sequence modeling at Douyin scale.

#### OneTrans: Unified Feature Interaction and Sequence Modeling (WWW 2026)
- One Transformer for both feature interaction and sequence modeling in industrial recommenders.

### Alibaba / Taotian Group (ICML 2026)

Five papers accepted:
1. **iTryOn** (2605.21431) — Interactive video try-on
2. **HiDe** (2510.00054) — High-res MLLM zoom-in decoupling
3. **E-VAds** (2602.08355) — E-commerce video understanding benchmark
4. **TP-GRPO** (2602.06422) — Step-wise and long-term interaction in flow-based GRPO
5. **RuCL** (2602.21628) — Rubric-based curriculum learning for MLLM reasoning

#### SIGMA (SIGIR 2026) — AliExpress generative multi-task recommender: +7.84% GMV

#### HeMix (KDD 2026) — AMAP CTR model: +3.61% GMV

#### AliBoostV2 (WWW 2026) — CTR-growth balanced boosting

### Tencent

#### S-GRec (RecSys 2025) — WeChat Channels generative recommendation: +1.19% GMV

### Kuaishou

#### Congrats (KDD 2026) — Graph-structured generative recommendation. 300M+ DAU deployment.

### Baidu

#### GPU-accelerated Multi-relational Parallel Graph Retrieval (WWW 2026 Industry)

### JD.com

#### GenRec (SIGIR 2026) — Preference-oriented generative framework: +9.5% clicks, +8.7% transactions

### NetEase

#### Climber-Pilot (KDD 2026) — Non-myopic generative recommendation: +4.24% core metric

---

## Key Cross-Conference Trends

### 1. RL Dominates LLM Post-Training
- GRPO appears in 157 ICLR papers vs. 55 for DPO
- RLVR (verifiable rewards) at 125 papers vs. 54 for RLHF
- MaxRL, PASC-GRPO, A2PO, REPO, ADAPO — new RL algorithms for LLMs

### 2. Retrieval + Reasoning Convergence
- Static retrieve-then-generate → dynamic iterative systems
- Q-RAG (ICLR Oral), KARL (ACL), MixRAGRec (KDD)

### 3. Generative Recommendation is Mainstream
- Congrats (Kuaishou), GenRec (JD), SIGMA (Alibaba), S-GRec (Tencent), Climber-Pilot (NetEase)
- Key challenge: likelihood trap, myopia, semantic-business alignment

### 4. Hybrid Architectures (Mamba + Attention)
- Nemotron 3 series (NVIDIA), Mamba-3 (ICLR)
- Long-context efficiency is king

### 5. Data Efficiency Breakthroughs
- IXT (NVIDIA): 2.8× compute efficiency via feedback conditioning
- Efficient Exploration (DeepMind): 10-1000× RLHF data efficiency
- OPUS (ICML): principled data selection
- SRPFN (KDD): zero-gradient recommendation from synthetic data

### 6. Formal Math & Verification
- LEAP (DeepMind): <10% → 70% on IMO Lean benchmark
- AI solves 9 open Erdős problems (DeepMind)
- Lean/formal verification as key agentic component

### 7. CTR Scaling Laws
- SparseCTR, FAT, HyFormer all demonstrate scaling laws in CTR
- Structured expressivity (not just size) drives performance

### 8. Agents Everywhere
- daVinci-Dev, ALIVE, AutoHarness, MiRA — agent training infrastructure
- KARL, Meta-Reasoner, GRP — agent reasoning frameworks
- Security concern: capability-vulnerability paradox (MCP Security)

---

## Statistics Summary

| Conference | Submissions | Accepted | Rate | Key Stat |
|-----------|-----------|----------|------|----------|
| ICML 2026 | 23,918 | 6,352 | 26.6% | — |
| ICLR 2026 | 19,525 | 5,355 | 27.4% | 21% reviews AI-generated |
| NeurIPS 2025 | 21,575 | ~5,200 | 24.5% | — |
| AAAI 2026 | 23,680 | 4,167 | 17.6% | 20K submissions from China |
| CVPR 2026 | 16,092 | 4,090 | 25.4% | 42% jump over 2025 |
| KDD 2026 | — | — | — | — |
| ACL 2026 | — | — | — | — |
| EMNLP 2025 | — | 1,810 | — | Largest EMNLP ever (6,000+ participants) |

---

## Paper Links (arXiv)

| Paper | arXiv ID |
|-------|----------|
| iTryOn | 2605.21431 |
| HiDe | 2510.00054 |
| E-VAds | 2602.08355 |
| TP-GRPO | 2602.06422 |
| RuCL | 2602.21628 |
| HyFormer | 2601.12681 |
| FAT | 2511.12081 |
| HeMix | 2602.09387 |
| SparseCTR | 2601.17836 |
| LLaCTR | 2505.14057 |
| GenCI | 2601.18251 |
| DAIAN | 2602.13971 |
| GenRec | 2604.14878 |
| SIGMA | 2602.22913 |
| S-GRec | 2602.10606 |
| DiffuMIN | 2508.15311 |
| Diff-MSIN | 2508.21460 |
| SRPFN | 2606.15752 |
| Climber-Pilot | 2602.13581 |
| Congrats | 2510.10127 |
| MixRAGRec | 2605.28175 |
| SPiKE | 2601.08148 |
| LEAP | 2606.03303 |
| AutoHarness | 2603.03329 |
| MiRA | 2603.19685 |
| Efficient RLHF | 2603.17378 |
| AlphaEvolve | 2602.16928 |
| Formal Proof Search | 2605.22763 |
| Interactive ICL | 2602.16066 |
| Nemotron 3 Super | 2604.12374 |
| Sol-RL | 2604.06916 |
| GRAIL | 2606.05160 |
| IXT | 2605.20285 |
| REPO/ADAPO (Apple) | 2603.11682 |
| ANE Reverse Engineering | 2606.22283 |
| BPGO | 2603.10990 |
| WorldGen | CVPR 2026 |
| Gen3R | CVPR 2026 |
| Meta-Reasoner | ACL 2026 Findings |
| KARL | ACL 2026 |
| GRP | ACL 2026 |
| MetaJuLS | ACL 2026 |
| Meta-Abilities | ACL 2026 Findings |
| CDCR-SFT | AAAI 2026 |
| Quantized Reasoning (overthinking) | 2606.00206 |
| ROI-Reasoning | 2601.03822 |
| CDCR-SFT Hallucination | AAAI 2026 |
| BCGO for Visual Generation | CVPR 2026 |
| DeepConf (Meta) | Meta Research |
| Nemotron 3 Ultra | NVIDIA Research |
