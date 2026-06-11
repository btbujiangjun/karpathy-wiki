---
title: "Conference & arXiv Digest — June 2026"
type: synthesis
created: 2026-06-11
updated: 2026-06-11
sources: []
tags: [conference-digest, icml-2026, aaai-2026, neurips-2025, iclr-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025, llm, recommender-system, ctr, agent, generative-model, arxiv]
---

# Conference & arXiv Digest — June 2026

> Comprehensive survey of recent papers from top ML/AI conferences and arXiv, covering LLMs, recommendation systems, CTR prediction, agent systems, generative models, and more.

---

## Table of Contents

1. [ICLR 2026 Highlights](#1-iclr-2026-highlights)
2. [AAAI 2026 Highlights](#2-aaai-2026-highlights)
3. [CVPR 2026 Highlights](#3-cvpr-2026-highlights)
4. [ICML 2026 Highlights](#4-icml-2026-highlights)
5. [NeurIPS 2025 Highlights](#5-neurips-2025-highlights)
6. [KDD 2026 Highlights](#6-kdd-2026-highlights)
7. [EMNLP 2025 / ACL 2026 Highlights](#7-emnlp-2025--acl-2026-highlights)
8. [RecSys 2025 / CIKM 2025 Highlights](#8-recsys-2025--cikm-2025-highlights)
9. [Architecture & Foundation Models](#9-architecture--foundation-models)
10. [LLM Reasoning & RL](#10-llm-reasoning--rl)
11. [Agent Systems & Tool Use](#11-agent-systems--tool-use)
12. [Recommendation & CTR Systems](#12-recommendation--ctr-systems)
13. [Industrial Lab Highlights (Google DeepMind, OpenAI, Meta, NVIDIA, ByteDance, Alibaba, Tencent, Kuaishou, Netflix)](#13-industrial-lab-highlights)
14. [Key Trends & Patterns](#14-key-trends--patterns)

---

## 1. ICLR 2026 Highlights

**Location**: Rio de Janeiro, Brazil | **Format**: Oral + Poster

### 1.1 Mamba-3: Improved Sequence Modeling using State Space Principles
- **Authors**: Aakash Sunil Lahoti, Kevin Li, Berlin Chen, Caitlin Wang, Aviv Bick, Zico Kolter, Tri Dao, Albert Gu
- **Affiliation**: CMU, Princeton, Cartesia AI, Together AI
- **Venue**: ICLR 2026 **Oral**
- **Abstract**: Mamba-3 is a new state space model (SSM) designed with inference efficiency as the primary goal. Three core improvements: (1) more expressive recurrence derived from SSM discretization, (2) complex-valued state update rule enabling richer state tracking, (3) multi-input multi-output (MIMO) formulation that improves performance without increasing decode latency. At 1.5B scale, Mamba-3 improves average downstream accuracy by 0.6pp over Gated DeltaNet; MIMO variant adds another 1.2pp. Achieves comparable perplexity to Mamba-2 with half the state size. Up to 7× faster inference than Transformers on long sequences.
- **arXiv**: [2603.15569](https://arxiv.org/abs/2603.15569)

### 1.2 AgentFlow: In-The-Flow Agentic System Optimization
- **Authors**: Lambda AI Research
- **Affiliation**: Lambda AI
- **Venue**: ICLR 2026
- **Abstract**: Introduces AgentFlow, a trainable agentic system where a team of agents learns to plan and use tools in the flow of a task, and Flow-GRPO (Flow-based Group Refined Policy Optimization) for efficient training. Breaks trajectory optimization into single-turn updates with group-normalized advantages. A 7B AgentFlow model beats GPT-4o on search, math, and science reasoning.
- **Links**: lambda.ai/blog/iclr-2026-12-papers

### 1.3 KAIROS Benchmark
- **Venue**: ICLR 2026
- **Abstract**: Drops LLM agents into collaborative scenarios with unreliable peers and adversarial participants. Reveals LLMs cave under peer pressure. An RL recipe in the same paper helps smaller models resist.

### 1.4 EdiVal-Agent: Agent-based Evaluation for Image Editing
- **Venue**: ICLR 2026
- **Abstract**: Uses agents as evaluators for multi-turn image editing. Decomposes images into objects and scores outputs on instruction-following, consistency, and visual quality.

### 1.5 Premise Selection for a Lean Hammer
- **Authors**: Thomas Zhu, Joshua Clune, Jeremy Avigad, Qiaochu Jiang, Sean Welleck
- **Venue**: ICLR 2026 **Oral**
- **Abstract**: LeanPremise, a neural premise selection system for the Lean proof assistant. Combined with existing components to create LeanHammer, the first end-to-end domain general hammer. Solves 21% more goals than existing premise selectors.

### 1.6 OpTI-BFM: Optimistic Task Inference for Behavior Foundation Models
- **Venue**: ICLR 2026 **Oral**
- **Abstract**: Addresses task inference purely through interaction with the environment at test-time. Proposes OpTI-BFM, an optimistic decision criterion that directly models uncertainty over reward functions and guides BFMs in data collection. Provides regret bound through connection to upper-confidence algorithms for linear bandits.

### 1.7 Textual Bayes: Quantifying Uncertainty in LLM-Based Systems
- **Authors**: Layer 6 AI
- **Affiliation**: Layer 6 AI
- **Venue**: ICLR 2026
- **Abstract**: Framework for uncertainty quantification in LLM-based systems using Bayesian methods.
- **Links**: [OpenReview](https://openreview.net/pdf?id=VPmsAr1OTl)

---

## 2. AAAI 2026 Highlights

**Location**: Singapore | **Date**: January 20–27, 2026 | **Submissions**: ~29,000 (nearly 2× AAAI-25)

### 2.1 AAAI-26 Overview
- **PC Chairs**: Chad Jenkins (U Michigan), Matthew Taylor (U Alberta)
- ~23,000 papers remained after policy compliance filtering
- 75,000+ unique authors; strong engagement from China (~20,000 submissions)
- Three largest areas: Computer Vision, ML, NLP
- Program Committee: 28,000+ members (3× previous year)

### 2.2 Notable AAAI 2026 Papers
- Multiple papers on MLLM/LLM topics accepted (LinkedIn reports 3 papers from one group)
- **LiteGE**: Lightweight Geodesic Embedding — 300× memory reduction vs neural approaches for 3D shape correspondence
- **Open-World Object Counting in Videos**: New task + CountVid model + VideoCount dataset
- Strong representation from Chinese labs (Tencent, Alibaba, Baidu, ByteDance) in CV, NLP, and data mining tracks

---

## 3. CVPR 2026 Highlights

**Location**: Denver, Colorado | **Date**: June 3–7, 2026 | **Submissions**: 16,092 (24% ↑ over 2025) | **Accepted**: 4,089 (~25% acceptance)

### 3.1 Conference Statistics
- Record 16,000+ submissions
- ~4,089 papers accepted
- 14 papers from Apple AI
- 6 papers from Sony AI

### 3.2 CompBench: Benchmarking Complex Instruction-guided Image Editing
- **Authors**: Bohan Jia, Wenxuan Huang, Junbo Qiao et al. (multiple institutions)
- **Venue**: CVPR 2026
- **Abstract**: Comprehensive benchmark for complex instruction-guided image editing, evaluating models on multi-step, compositional edit instructions.
- **arXiv**: [2505.12200](https://arxiv.org/abs/2505.12200)

### 3.3 DirectFisheye-GS: Enabling Native Fisheye Input in Gaussian Splatting
- **Authors**: Zhengxian Yang, Fei Xie, Xutao Xue et al.
- **Venue**: CVPR 2026
- **Abstract**: Cross-view joint optimization approach enabling native fisheye camera input for 3D Gaussian Splatting.
- **arXiv**: [2604.00648](https://arxiv.org/abs/2604.00648)

### 3.4 PaCo-RL: Reinforcement Learning for Consistent Image Generation
- **Authors**: Bowen Ping, Chengyou Jia, Minnan Luo et al.
- **Affiliation**: A*STAR CFAR
- **Venue**: CVPR 2026
- **Abstract**: Consistent image generation producing multiple images coherent in identity/style. Introduces PaCo-Dataset, PaCo-Reward for visual consistency evaluation, and PaCo-GRPO for efficient RL-based diffusion training.
- **arXiv**: [2512.04784](https://arxiv.org/abs/2512.04784)

### 3.5 SEA-Flow3D: Simplified Scene Flow
- **Authors**: Han Ling, Quansen Sun, Yinghua Yao, Ivor Tsang et al.
- **Affiliation**: A*STAR CFAR
- **Venue**: CVPR 2026
- **Abstract**: Lightweight RAFT-style dense scene-flow method with Spatial Vector Sampling, yielding SOTA KITTI/Sintel accuracy efficiently.

### 3.6 Sony AI @ CVPR 2026
- 6 papers presented
- Topics: generative modeling, 3D scene understanding, video-to-audio synthesis, domain-adaptive perception
- **Project Ace**: Robot table tennis system published in *Nature* — first AI system competing with elite humans (20.2ms latency vs 230ms for humans)

### 3.7 Apple @ CVPR 2026
- 14 AI research papers presented
- Strong presence across vision, multimodal, and generative AI tracks

---

## 4. ICML 2026 Highlights

**Location**: Seoul, South Korea | **Date**: July 6–11, 2026 | **Submissions**: 24,371 (record, 2× previous year)

### 4.1 Conference Stats
- **Total submissions**: 24,371 (more than doubled from ~12,107 in 2025)
- **Spotlight papers**: 2.2% of submissions
- Records at every level

### 4.2 MEMO: Memory-Augmented Model Context Optimisation for Multi-Agent LLM Games
- **Authors**: Yunfei Xie, Kevin Wang, Bobby Cheng et al.
- **Affiliation**: Multiple, including A*STAR CFAR
- **Abstract**: Multi-agent LLM game evaluations are unstable due to early deviations amplifying across interactions. MEMO improves performance and stability by optimizing inference context through memory retention and exploration, significantly boosting win rates with limited self-play.

### 4.3 Provable Benefit of Curriculum in Transformer Tree-Reasoning Post-Training
- **Authors**: Dake Bu, Wei Huang, Andi Han, Atsushi Nitanda et al.
- **Affiliation**: A*STAR CFAR
- **Abstract**: Under outcome-only reward signals, RL finetuning with curriculum strategies achieves high accuracy with polynomial sample complexity, while non-curriculum approaches encounter exponential complexity bottlenecks.
- **arXiv**: [2511.07372](https://arxiv.org/abs/2511.07372)

### 4.4 Agentic Monte Carlo: RL for Black-Box LLM Agents
- **Authors**: Dae Yon Hwang, Raunaq Suri, Valentin Villecroze et al.
- **Affiliation**: Layer 6 AI
- **Abstract**: Proposes Agentic Monte Carlo (AMC) to sample from optimal policy of black-box LLM agents without parameter access. Uses Sequential Monte Carlo to steer agents by learning a value function while leaving the underlying black-box model unchanged.

### 4.5 Conf-Gen: Conformal Uncertainty Quantification for Generative Models
- **Authors**: Layer 6 AI
- **Affiliation**: Layer 6 AI
- **Abstract**: Conformal prediction methods adapted for generative models, providing distribution-free uncertainty guarantees.

### 4.6 Beyond Test-Time Training: Learning to Reason via Hardware-Efficient Optimal Control
- **Authors**: Peihao Wang, Shan Yang, Xijun Wang et al.
- **Affiliation**: ASSET / Multiple
- **Abstract**: Reformulates reasoning as an optimal control problem with hardware-efficient implementations.

---

## 5. NeurIPS 2025 Highlights

**Location**: Vancouver (virtual components) | **Submissions**: 21,575 | **Accepted**: 5,275 (77 Oral, 683 Spotlight, 4,515 Poster)

### 5.1 Generalized Linear Mode Connectivity for Transformers
- **Authors**: Alexander Theus, Alessandro Cabodi, Sotiris Anagnostidis et al.
- **Venue**: NeurIPS 2025 **Oral**
- **Abstract**: Unified framework capturing four symmetry classes — permutations, semi-permutations, orthogonal transformations, and general invertible maps. Enables low-/zero-barrier linear interpolation paths between independently trained Vision Transformers and GPT-2 models. Extends to multi-model and width-heterogeneous settings.

### 5.2 Deep Compositional Phase Diffusion for Long Motion Sequence Generation
- **Authors**: Ho Yin Au, Jie Chen, Junkun Jiang, Jingyu Xiang
- **Venue**: NeurIPS 2025 **Oral**
- **Abstract**: Compositional Phase Diffusion with Semantic Phase Diffusion Module (SPDM) and Transitional Phase Diffusion Module (TPDM) for generating long, coherent motion sequences without artifacts at transition boundaries.

### 5.3 ModHiFi: Identifying High Fidelity Predictive Components for Model Modification
- **Authors**: Dhruva Kashyap, Chaitanya Murti et al.
- **Venue**: NeurIPS 2025 **Spotlight**
- **Abstract**: Model modification (pruning/unlearning) without training data or loss function access. ModHiFi-P achieves 11% speedup over SOTA on ImageNet; ModHiFi-U achieves complete unlearning on CIFAR-10 without fine-tuning.

### 5.4 Structure of Relation Decoding Linear Operators in LLMs
- **Authors**: Miranda Anna Christ, Adrián Csiszárik et al.
- **Venue**: NeurIPS 2025 **Spotlight**
- **Abstract**: Extends Hernandez et al. [2023] findings on linear operators that decode relational facts in transformer LMs — maps organization across a collection of relations.

### 5.5 CausalPFN: Amortized Causal Effect Estimation via In-Context Learning
- **Authors**: Layer 6 AI
- **Venue**: NeurIPS 2025 **Spotlight**
- **Abstract**: Uses in-context learning with prior-data fitted networks for causal effect estimation.
- **arXiv**: [2506.07918](https://arxiv.org/abs/2506.07918)

---

## 6. KDD 2026 Highlights

**Location**: Jeju Island, South Korea | **Date**: August 9–13, 2026

### 6.1 Research Track — Notable Papers
- **VaLUH**: Fast Algorithms for Configuration Model of Vertex-Labeled Undirected Hypergraphs
- Strong presence of Chinese industrial labs (Alibaba, Tencent, ByteDance, Kuaishou)
- **ADS Track**: Dedicated applied data science track for recommendation and advertising systems

### 6.2 Key Themes
- Scaling laws for CTR models
- Generative recommendation (OneRec paradigm from Kuaishou)
- Token-based ranking models from ByteDance (RankMixer, TokenMixer)
- Multi-task learning for conversion rate prediction

---

## 7. EMNLP 2025 / ACL 2026 Highlights

### 7.1 EMNLP 2025 (Suzhou, China — Nov 4-9, 2025)
- **Submissions**: 8,174 | **Accepted**: 1,811 (22.2% acceptance)
- **Findings**: 1,417 additional papers (17.3%)
- **Apple @ EMNLP 2025**: Multiple papers including:
  - Bias after Prompting: Persistent Discrimination in LLMs
  - Speculative Streaming: Efficient Speculative Decoding with Multi-Stream Attention
  - MLX: Large model inference and training on device

### 7.2 ACL 2026
- EMNLP 2026 submissions due May 25, 2026
- ACL 2026 accepts work on tokenization, multilingual systems, LLM efficiency, safety and alignment
- Notable: HPLT v4.0 (The HPLT pool) dataset release

---

## 8. RecSys 2025 / CIKM 2025 / SIGIR 2025 Highlights

### 8.1 RecSys 2025 (Prague — Sep 22-26, 2025)
- **Notable papers**:
  - Beyond Immediate Click: Engagement-Aware MoE Transformers for Sequential Movie Recommendation
  - LEAF: Lightweight Efficient Adaptive Flexible Embedding for Large-Scale Recommendation
  - Lasso: LLM-based User Simulator for Cross-Domain Recommendation
  - You Say Search, I Say Recs: Agentic Query Understanding at Spotify
  - Exploring Scaling Laws of CTR Model for Online Performance Improvement
  - Zero-shot Cross-domain Knowledge Distillation (YouTube Music)
  - User Long-Term Multi-Interest Retrieval Model for Recommendation

### 8.2 CIKM 2025 (Rome — Nov 10-14, 2025)
- **Submissions**: 2,761 (+11% YoY) | **Accepted**: 810 (29%)
- Tracks: Full Research, Short Research, Applied Research, Resource, Demo
- Notable: HealthGenie (LLM+KG dietary guidance), AGENTiGraph (multi-agent KG)
- **Alibaba**: Multi-Attribution Learning for CVR prediction (MAL)

### 8.3 SIGIR 2025 (Padua — Jul 13-18, 2025)
- Advances in retrieval-augmented generation and conversational search

---

## 9. Architecture & Foundation Models

### 9.1 Mamba-3 (Detailed)
- **Problem**: Linear models (SSMs/linear attention) trade off quality for efficiency; fail on state tracking; hardware-inefficient inference
- **Innovations**:
  1. **Expressive recurrence**: Improved discretization from SSM theory
  2. **Complex-valued state**: Enables richer state tracking than real-valued Mamba-2
  3. **MIMO formulation**: Multi-input multi-output for better quality without extra decode latency
- **Results** (1.5B scale): +0.6pp over Gated DeltaNet; MIMO variant +1.2pp additional
- **Inference**: Up to 7× faster than Transformers on long sequences
- **Open source**: Apache 2.0, Triton/TileLang/CuTe kernels
- **Industry adoption**: NVIDIA and IBM shipping hybrid Mamba-Transformer models

### 9.2 NVIDIA Nemotron 3 Ultra
- **Parameters**: 550B total / 55B active (MoE)
- **Architecture**: Hybrid Mamba-Transformer Latent MoE
- **Context window**: 1 million tokens
- **Performance**: 300+ tokens/sec on Hopper; AI Index Score 48 (tops US open-weights)
- **Training**: NVFP4 precision on Blackwell GPUs, 3T token dataset
- **Availability**: Open weights (NVIDIA Open Model License), Hugging Face, NGC
- **Agent optimization**: Trained with RL for agentic tasks, tool use, multi-step reasoning
- **Family**: Nano (8B), Super (120B/12B active), Ultra (550B/55B active)

### 9.3 Inception Mercury Diffusion LLMs
- **Company**: Inception (Stealth startup, team from Stanford, Google DeepMind, Meta AI, OpenAI)
- **Technology**: Diffusion-based language models (dLLMs) — generate multiple tokens in parallel
- **Advantages**: 3-5× faster than autoregressive LLMs, lower cost, schema control
- **Status**: Deploying at Fortune 500 companies

### 9.4 Google Gemma 4
- **Released**: May 2026
- **Focus**: On-device deployment, intelligence-per-parameter optimization
- **Variants**: 31B IT available on AI Studio

### 9.5 Google Gemini 3.5 & Gemini Omni
- **Gemini 3.5**: Latest frontier model series combining intelligence with action capabilities
- **Gemini Omni**: Create anything from anything (starting with video)
- **Live Translate**: Real-time voice translation via Gemini 3.5 Audio

### 9.6 Apple MLX Framework
- **Presented at**: EMNLP 2025
- **Capability**: Large model inference and training on Apple Silicon
- **Significance**: Enables on-device LLM deployment at scale

---

## 10. LLM Reasoning & RL

### 10.1 Key 2026 Trends (per Sebastian Raschka's curated list)
1. **Architecture & Model Design**: Continued evolution beyond pure Transformer
2. **Efficient Training & Scaling**: Data, memory, compute efficiency unification
3. **Inference Efficiency & KV Cache**: Major focus area
4. **Sparse Attention & Long Context**: 1M+ token contexts becoming standard
5. **Reasoning & Test-Time Compute**: O-series, DeepSeek-R1 lineage
6. **Reinforcement Learning & RLVR**: RL with verifiable rewards for math/coding
7. **Agent Systems & Tool Use**: Rapidly growing subfield
8. **Coding Agents & Software Engineering**: Claude Code, OpenCode, etc.
9. **Diffusion Language Models**: Inception, Mercury paradigm
10. **Model Evaluation & Benchmarks**: Arena-based and task-specific

### 10.2 Provable Benefit of Curriculum in Transformer Reasoning
- **Venue**: ICML 2026
- **Key insight**: Under outcome-only reward signals, curriculum-based RL finetuning achieves polynomial sample complexity while non-curriculum approaches face exponential bottlenecks
- **Implication**: Provides theoretical justification for curriculum design in RL-based reasoning training

### 10.3 State of RL for LLM Reasoning (2026)
- Primary methods: GRPO, DAPO, PPO with verifiable rewards
- Scaling: Test-time compute scaling (chain-of-thought, iterative refinement, tree search)
- Key players: DeepSeek (R1), OpenAI (o-series), Alibaba (QwQ), Meta (Llama reasoning variants)
- Open questions: Reward hacking, reward model scaling, inference-time vs training-time compute tradeoffs

---

## 11. Agent Systems & Tool Use

### 11.1 AgentFlow + Flow-GRPO
- **Venue**: ICLR 2026
- **Innovation**: 7B model beats GPT-4o on search/math/science
- **Method**: Single-turn trajectory optimization with group-normalized advantages
- **Significance**: Modular agent training without end-to-end RL difficulty

### 11.2 Agentic Monte Carlo (AMC)
- **Venue**: ICML 2026
- **Innovation**: RL for black-box LLM agents via Sequential Monte Carlo
- **Key idea**: Equivalence between RL and Bayesian inference; posterior over trajectories
- **Advantage**: Works with API-only access, no parameter modification needed

### 11.3 KAIROS Benchmark
- **Venue**: ICLR 2026
- **Finding**: LLMs cave under peer pressure in collaborative/adversarial scenarios
- **Mitigation**: RL training helps smaller models resist

### 11.4 NVIDIA Agent Toolkit
- **Released with**: Nemotron 3 Ultra (June 2026)
- **Components**: Agent harnesses, scaffolding, tool-use frameworks
- **Supported agents**: OpenCode, OpenClaw, Kilo Code CLI, OpenHands, Hermes Agent

### 11.5 Claude Code Vulnerabilities
- **Reported**: June 2026
- **Finding**: ~50 ways to break Claude Code's permission model (RyotaK, GMO Flatt Security)
- **CVSS 4.0**: 7.8 for GitHub Action supply chain flaw
- **Lesson**: Agent security is a class of vulnerability, not a single bug

### 11.6 Awesome AI Agents 2026
- Curated list of 100+ agent frameworks, tools, platforms
- Indicates agent ecosystem maturity beyond research papers

---

## 12. Recommendation & CTR Systems

### 12.1 CADET: Context-Conditioned Ads CTR Prediction (LinkedIn)
- **Authors**: David Pardoe, Neil Daftary et al.
- **Affiliation**: LinkedIn (Microsoft)
- **Venue**: arXiv Feb 2026
- **Innovations**:
  1. Decoder-only transformer for ads CTR prediction
  2. Context-conditioned decoding with multi-tower prediction heads
  3. Self-gated attention for training stability
  4. Timestamp-based RoPE for temporal relationships (seconds to months)
  5. Session masking for train-serve skew mitigation
  6. Production engineering: tensor packing, Flash Attention kernels
- **Results**: 11.6% online CTR improvement in A/B test
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)

### 12.2 ByteDance Token-Based Ranking Models

#### RankMixer (KDD 2025)
- Hardware-aware token mixing design replacing attention with per-token parameterized FFN + HeadMixing
- Foundational work of ByteDance's token-based recommendation series

#### TokenMixer-Large (arXiv 2026)
- **Scale**: 7B online / 15B offline parameters
- **Innovations**: Residual misalignment fix, inter-layer residuals, Sparse Per-token MoE
- **Efficiency**: MFU reaches 60%
- **Business impact**: E-commerce GMV +2.98%, advertising ADSS +2.0%

#### OneTrans (WWW 2025)
- **Innovation**: Unifies sequence (behavior) and non-sequence (profile/context) features into single token sequence via pyramid Transformer blocks
- **Results**: Single-user GMV +5.68% online A/B

#### HyFormer (arXiv 2026)
- **Innovation**: Query-decoding (global token cross-attends to each sequence independently) + query-augmentation
- **Claim**: Outperforms OneTrans

### 12.3 Generative Recommendation Evolution
- **TIGER (Google)**: Encoder-decoder retrieval, replacing dense vector indexing with text-to-text generation
- **LIGER (Meta)**: Multilingual and multimodal generative retrieval
- **OneRec (Kuaishou)**: Fully end-to-end generative recommendation integrating retrieval, ranking, and preference alignment
- **Netflix GenRec**: Scaling from O(1M) to O(1B) parameters with scaling laws
- **ContRec**: Diffusion generative recommendation with continuous tokens
- **DiffGRM**: Diffusion-based generative recommendation model
- **GRLM (Kuaishou)**: LLM-based generative recommendation via structured term identifiers (TIDs)
- **TencentGR**: All-modality generative recommendation datasets (1M/10M scale)

### 12.4 Scaling Laws for Recommendation
- Netflix: Novel scaling dynamics different from Chinchilla law
- Alibaba: Three-step paradigm based on Large User Model
- ByteDance: TokenMixer-Large demonstrates scaling from 7B to 15B parameters
- Meta: Scaling law experiments on CTR models

### 12.5 Tencent Advertising Algorithm Challenge 2025
- **Datasets**: TencentGR-1M (1M users) and TencentGR-10M (10M users)
- **Focus**: All-modality generative recommendation with advertising context
- **Features**: Real de-identified ads logs with collaborative IDs + multimodal embeddings
- **Resources**: [Hugging Face datasets](https://huggingface.co/datasets/TAAC2025)

---

## 13. Industrial Lab Highlights

### 13.1 Google DeepMind
- **Gemini 3.5**: Frontier model series with action capabilities
- **Gemini Omni**: Multimodal creation starting with video
- **Gemma 4**: Open models optimized for on-device
- **Co-Scientist**: Collaborative AI research partner
- **AlphaFold**: Protein structure prediction
- **Genie 3**: Interactive world generation
- **SIMA 2**: Agent that plays, reasons, and learns with users
- **Project Ace**: Robot table tennis in *Nature* — 20.2ms end-to-end latency
- **Publications**: Active across ICML 2026, ICLR 2026, NeurIPS 2025

### 13.2 OpenAI
- **o3 reasoning model**: Released 2025/2026
- **GPT-4.5 / GPT-5 series**: Continue to evolve
- **S-1 IPO filing**: $852B valuation (filed 2026)
- **Focus areas**: Reasoning, multimodal, agent safety

### 13.3 Anthropic
- **Claude Fable 5**: Latest model release
- **S-1 IPO filing**: $965B valuation
- **Research**: Agent safety, interpretability, recursive self-improvement
- **Claim**: Claude writes 80% of Anthropic's own code (June 2026)

### 13.4 Meta AI
- **Llama 4 Maverick**: 400B/17B active MoE model
- **LIGER**: Multilingual multimodal generative retrieval
- **Llama reasoning variants**: RL-based reasoning post-training
- **Active**: Top recommendation conference presence (KDD, RecSys)

### 13.5 Microsoft Research / LinkedIn
- **CADET**: Decoder-only CTR model (11.6% online improvement)
- **LiRank**: Large-scale ranking framework
- **Active**: KDD, RecSys, CIKM

### 13.6 ByteDance
- **RankMixer / TokenMixer**: Token-based ranking at 7-15B scale
- **OneTrans / HyFormer**: Unified sequence modeling
- **Doubao AI Chatbot**: Consumer AI product
- **Douyin**: 750M+ DAUs, recommendation-driven

### 13.7 Alibaba
- **Large User Model**: Three-step paradigm unlocking scaling laws in recommendation
- **Pantheon**: Generative ranking as Pareto-efficient policy optimization
- **QwQ reasoning model**: LLM reasoning
- **Multi-task ranking**: Various CIKM/KDD papers

### 13.8 Tencent
- **TencentGR**: Generative recommendation datasets
- **WeChat Channels**: Social recommendation leveraging 1.3B user base
- **Advertising Algorithm Challenge**: Industry-wide competition

### 13.9 Kuaishou
- **OneRec**: End-to-end generative recommendation (retrieval + ranking + alignment)
- **GRLM**: LLM-based generative recommendation with structured term identifiers
- **OneLoc / OneSearch / OneSug**: Vertical-specific generative recommenders
- **GenSAR**: Cross-domain generative retrieval

### 13.10 Netflix
- **Generative Recommendation**: Scaling from O(1M) to O(1B) parameters
- **Challenges Addressed**: Scaling laws specific to recommendation, training stability, cold-start adaptation, multi-token prediction

### 13.11 NVIDIA
- **Nemotron 3 Family**: Nano (8B), Super (120B/12B), Ultra (550B/55B)
- **Hybrid architecture**: Mamba-Transformer Latent MoE
- **Agent Toolkit**: Full-stack agent development platform
- **Hardware**: Blackwell GPUs, DGX Station, RTX Spark laptops for on-prem deployment

### 13.12 Apple
- **14 papers at CVPR 2026**: Major presence in vision research
- **MLX**: On-device LLM framework
- **Speculative Streaming**: Efficient speculative decoding
- **Research focus**: Privacy-preserving ML, on-device AI, multimodal systems

### 13.13 Amazon
- **Alexa AI**: Continued investment in LLM-powered assistant
- **AWS AI**: Bedrock, SageMaker AI infrastructure
- **Recommendation**: Powering e-commerce recommendation at scale

---

## 14. Key Trends & Patterns

### 14.1 Architecture Trends
- **SSMs catch up**: Mamba-3 proves SSMs competitive with Transformers on quality while being faster at inference
- **Hybrid models win**: Mamba-Transformer hybrids (Nemotron 3, Jamba) represent the pragmatic middle ground
- **Diffusion for language**: Inception's dLLMs signal a new paradigm — parallel token generation
- **1M+ context windows**: Becoming standard (Gemini 3.5, Nemotron 3 Ultra, Claude)

### 14.2 Inference Efficiency Dominates
- The shift from training-first to inference-first architecture design
- KV cache optimization as a major research area
- Speculative decoding becoming standard practice

### 14.3 Agent Systems Go Mainstream
- 2026 declared "the year agents went mainstream"
- Agent-specific benchmarks (KAIROS, SWE-bench, Pinchbench)
- Security vulnerabilities emerging as agents are deployed at scale

### 14.4 Generative Recommendation Replaces Cascaded Pipelines
- OneRec paradigm (Kuaishou) replacing traditional retrieval → ranking → reranking
- Scaling laws proven for recommendation (Netflix, ByteDance, Alibaba)
- Diffusion-based recommendation emerges as new subfield

### 14.5 RL for Reasoning is the Dominant Post-Training Paradigm
- GRPO/DAPO replacing PPO for verifiable reward settings
- Curriculum learning proven beneficial theoretically (ICML 2026)
- Test-time compute scaling as complementary approach

### 14.6 Conference Growth Continues Unabated
- ICML 2026: 24,371 submissions (2× ICML 2025)
- AAAI 2026: 29,000 submissions (2× AAAI 2025)
- CVPR 2026: 16,092 submissions (+24%)
- Quality control mechanisms (best paper selection, isotonic mechanism) struggling to keep pace

### 14.7 Chinese Industrial Labs Lead Recommendation Research
- ByteDance, Alibaba, Tencent, Kuaishou dominate generative recommendation and CTR
- Open datasets (TencentGR) enabling reproducible research
- Scaling to 15B+ parameter recommendation models

### 14.8 Open-Weight Models Competitive with Closed
- Nemotron 3 Ultra tops US open-weights leaderboard
- Mamba-3 available under Apache 2.0
- Gemma 4 for on-device deployment
- Democratization of frontier capabilities

---

## References

- [ICLR 2026 Papers](https://papers.cool/venue/ICLR.2026)
- [AAAI 2026 Proceedings](https://ojs.aaai.org/index.php/AAAI/issue/view/683)
- [CVPR 2026 Open Access](https://openaccess.thecvf.com/CVPR2026)
- [ICML 2026 Wikipedia](https://en.wikipedia.org/wiki/International_Conference_on_Machine_Learning)
- [NeurIPS 2025 Paper List](https://kmno4-zx.github.io/nips25-all-papers)
- [KDD 2026 Proceedings](https://dl.acm.org/doi/proceedings/10.1145/3770854)
- [RecSys 2025 Summary](https://pyemma.github.io/Recsys-2025-Paper-Summary)
- [Sebastian Raschka LLM Research Papers 2026](https://magazine.sebastianraschka.com/p/llm-research-papers-2026-part1)
- [NVIDIA Nemotron 3 Ultra](https://docs.nvidia.com/nemotron/nightly/usage-cookbook/Nemotron-3-Ultra-Base/README.html)
- [Mamba-3 Blog](https://together.ai/blog/mamba-3)
- [Layer 6 AI Publications](https://layer6.ai/publications/)
- [Sony AI @ CVPR 2026](https://ai.sony/blog/cvpr-2026-sony-ais-latest-in-computer-vision-research)
- [Apple @ EMNLP 2025](https://machinelearning.apple.com/updates/apple-at-emnlp-2025)
- [Generative Recommendation Survey (Preprints)](https://www.preprints.org/manuscript/202512.0741)
- [Awesome AI Agents 2026](https://github.com/Zijian-Ni/awesome-ai-agents-2026)
- [Modern RecSys Papers](https://github.com/ubear/modern-recsys-papers)
