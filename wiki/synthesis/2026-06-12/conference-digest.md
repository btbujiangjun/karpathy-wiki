---
title: "Conference Digest 2026-06-12"
type: synthesis
created: 2026-06-12
updated: 2026-06-12
sources: []
tags: [conference-digest, icml2026, iclr2026, neurips2025, cvpr2026, aaai2026, kdd2026, emnlp2025, sigir2026, www2026, cikm2025, recsys2025, acl2026]
---

# Conference & arXiv Digest — 2026-06-12

> Comprehensive survey of recent papers from top ML/AI conferences and arXiv. Covers ICLR 2026, ICML 2026, AAAI 2026, NeurIPS 2025, KDD 2025/2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025, and recent arXiv preprints.

---

## Table of Contents

1. [ICLR 2026 — Outstanding Papers & Highlights](#1-iclr-2026)
2. [ICML 2026 — Overview & Key Papers](#2-icml-2026)
3. [AAAI 2026 — Overview & Key Papers](#3-aaai-2026)
4. [NeurIPS 2025 — Highlights](#4-neurips-2025)
5. [CVPR 2026 — Best Papers & Key Contributions](#5-cvpr-2026)
6. [ACL 2026 & EMNLP 2025 — NLP & LLM Papers](#6-acl-2026--emnlp-2025)
7. [KDD 2025/2026 — Data Mining & Applied ML](#7-kdd-20252026)
8. [SIGIR 2026 — Information Retrieval & Recommendation](#8-sigir-2026)
9. [WWW 2026 — Web & Recommendation](#9-www-2026)
10. [CIKM 2025 — Knowledge Management](#10-cikm-2025)
11. [RecSys 2025 — Recommender Systems](#11-recsys-2025)
12. [Agent Systems & Tool Use](#12-agent-systems--tool-use)
13. [CTR Prediction & Advertising](#13-ctr-prediction--advertising)
14. [Generative Models & Diffusion Transformers](#14-generative-models--diffusion-transformers)
15. [LLM Reasoning & Test-Time Compute](#15-llm-reasoning--test-time-compute)
16. [Code Generation & Execution Prediction](#16-code-generation--execution-prediction)
17. [Key Trends & Synthesis](#17-key-trends--synthesis)

---

## 1. ICLR 2026

> **Location**: Singapore | **Date**: April 2026 | **Submissions**: ~11,672 | **Acceptance rate**: ~26.6% | **Oral papers**: 223

### Outstanding Papers

#### 1.1 Transformers are Inherently Succinct
- **Authors**: Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin
- **Affiliation**: ETH Zurich
- **Links**: [OpenReview](https://openreview.net/forum?id=Yxz92UuPLQ)
- **Summary**: This theoretical work proposes a new perspective to explain the power of the Transformer architecture — namely, how *succinctly* it can encode some concepts compared to alternative models such as RNNs. The paper may stimulate additional theoretical and empirical investigation into succinctness of concept representation by transformers and other architectures.

#### 1.2 LLMs Get Lost In Multi-Turn Conversation
- **Authors**: Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
- **Affiliation**: Salesforce
- **Links**: [OpenReview](https://openreview.net/forum?id=VKGTGGcwl6)
- **Summary**: There is a dissonant gap between most of the data used for LLM training (text completion or single turn) and how they are deployed (multi-turn settings). This paper designs a scalable method to evaluate multi-turn capabilities, and measures a marked decrease in LLM aptitude and reliability in multi-turn interactions with underspecified instructions.

#### 1.3 Honorable Mention: Premise Selection for a Lean Hammer
- **Authors**: Thomas Zhu, Joshua Clune, Jeremy Avigad, Qiaochu Jiang, Sean Welleck
- **Affiliation**: Carnegie Mellon University
- **Links**: [OpenReview](https://openreview.net/forum?id=m04JJNeRK6)
- **Summary**: Presents LeanPremise, a novel neural premise selection system, combined with existing components to create LeanHammer — the first end-to-end domain general hammer for the Lean proof assistant. Solves 21% more goals than existing premise selectors.

### Key Oral Papers

#### 1.4 Mamba-3: Improved Sequence Modeling using State Space Principles
- **Authors**: Aakash Sunil Lahoti, Kevin Li, Berlin Chen, Caitlin Wang, Aviv Bick, Zico Kolter, Tri Dao, Albert Gu
- **Affiliation**: Carnegie Mellon University / Princeton
- **Links**: [OpenReview](https://openreview.net/forum?id=HwCvaJOiCj)
- **Summary**: Introduces three core methodological improvements inspired by the state-space model viewpoint: 1) more expressive recurrence, 2) complex state update rule enabling richer state tracking, and 3) multi-input, multi-output formulation. Together with architectural refinements, Mamba-3 achieves significant gains across retrieval, state-tracking, and downstream language modeling tasks, setting a new Pareto frontier for performance under fixed inference budget.

#### 1.5 AgentFlow: In-The-Flow Agentic System Optimization
- **Authors**: Lambda Lab team
- **Affiliation**: Lambda
- **Links**: [Lambda Blog](https://lambda.ai/blog/iclr-2026-12-papers)
- **Summary**: Introduces AgentFlow — a trainable agentic system where a team of agents learns to plan and use tools in the flow of a task, and Flow-GRPO (Flow-based Group Refined Policy Optimization). A 7B AgentFlow model beats GPT-4o on search, math, and science reasoning.

#### 1.6 WAVE: Learning Unified & Versatile Audio-Visual Embeddings
- **Authors**: Changli Tang, Qinfan Xiao, Ke Mei, Tianyi Wang, Fengyun Rao, Chao Zhang
- **Links**: [OpenReview](https://openreview.net/forum?id=MiV3WXDYJb)
- **Summary**: Proposes a framework for learning unified audio-visual embeddings using multimodal LLMs, addressing dynamic modalities like audio and video.

#### 1.7 Pre-training under infinite compute
- **Authors**: Konwoo Kim, Suhas Kotha, Percy Liang, Tatsunori Hashimoto
- **Affiliation**: Stanford University
- **Links**: [arXiv](https://arxiv.org/abs/2509.14786)
- **Summary**: Studies data efficiency and scaling laws in the regime of infinite compute. **Oral**.

#### 1.8 pi-Flow: Policy-Based Few-Step Generation via Imitation Distillation
- **Authors**: Hansheng Chen, Kai Zhang, Hao Tan, Leonidas Guibas, Gordon Wetzstein, Sai Bi
- **Affiliation**: Stanford University / NVIDIA
- **Links**: [arXiv](https://arxiv.org/pdf/2510.14974)
- **Summary**: Diffusion models, flow models, few-step generation via distillation.

### ICLR 2026 Oral Topics by Count
- **Reinforcement Learning**: 24 papers
- **Knowledge Distillation for LLMs**: 5 papers
- **LLM Agent papers**: ~40 papers

---

## 2. ICML 2026

> **Location**: Seoul, South Korea | **Date**: July 6–11, 2026 | **Submissions**: 23,918 (after desk rejects) | **Accepted**: 6,352 | **Acceptance rate**: 26.6% | **Spotlight**: 2.2%

### Selected Highlight Papers

#### 2.1 MEMO: Memory-Augmented Model Context Optimisation for Robust Multi-Turn Multi-Agent LLM Games
- **Authors**: Yunfei Xie, Kevin Wang, Bobby Cheng, Jianzhu Yao, Zhizhou Sha, Alexander Duffy, Yihan Xi, Hongyuan Mei, Cheston Tan, Chen Wei, Pramod Viswanath, Zhangyang Wang
- **Affiliation**: A*STAR CFAR / UIUC
- **Links**: [ICML 2026](https://icml.cc/virtual/2026/poster/62950)
- **Summary**: Multi-agent LLM game evaluations are unstable as early deviations amplify. MEMO improves performance and stability by optimising inference context through memory retention and exploration, significantly boosting win rates with limited self-play.

#### 2.2 Provable Benefit of Curriculum in Transformer Tree-Reasoning Post-Training
- **Authors**: Dake Bu, Wei Huang, Andi Han, Atsushi Nitanda, Hau-San Wong, Qingfu Zhang, Taiji Suzuki
- **Affiliation**: A*STAR CFAR / City University of Hong Kong / University of Tokyo
- **Links**: [arXiv](https://arxiv.org/abs/2511.07372v3)
- **Summary**: Under outcome-only reward signals, RL finetuning with curriculum strategies achieves high accuracy with polynomial sample complexity, whereas non-curriculum counterpart encounters exponential complexity bottleneck.

#### 2.3 Bias in Zeroth-Order Normal Estimation for Decision-Based Attacks (SAR)
- **Authors**: Feiyang Wang, Hangwei Qian, Xingquan Zuo, Gang Chen, Ivor Tsang
- **Affiliation**: A*STAR CFAR
- **Links**: [ICML 2026](https://icml.cc/virtual/2026/poster/65667)
- **Summary**: Proposes SAR, a plug-in query-efficient refinement leveraging sensitivity-aware rescaling to produce less perceptible hard-label adversarial examples.

#### 2.4 Revenue Efficiency of Correlated Equilibria in First Price Auctions *(Spotlight)*
- **Authors**: Anders Bo Ipsen, Stratis Skoulakis
- **Affiliation**: Aarhus University
- **Links**: [ICML 2026](https://icml.cc/virtual/2026/poster/61773)
- **Summary**: Studies revenue efficiency of correlated equilibria in first-price auctions.

#### 2.5 RECAST: Model Reconstruction via Counterfactual-Aware Wasserstein Geometry
- **Authors**: Xuan Zhao, Lena Krieger, Zhuo Cao, Arya Bangun, Hanno Scharr, Ira Assent
- **Affiliation**: Aarhus University
- **Links**: [ICML 2026](https://icml.cc/virtual/2026/poster/64184)
- **Summary**: Model reconstruction under limited data using counterfactual-aware Wasserstein geometry.

#### 2.6 Understanding Dynamics of Adam in Zero-Sum Games: An ODE Approach
- **Authors**: Yi Feng, Weiming Ou, Xiao Wang
- **Affiliation**: Aarhus University
- **Links**: [ICML 2026](https://icml.cc/virtual/2026/poster/66360)
- **Summary**: ODE-based analysis of Adam optimizer dynamics in zero-sum games.

---

## 3. AAAI 2026

> **Location**: Singapore | **Date**: January 20–27, 2026

### Key Themes
- LLM safety alignment — preventing safety drift via coupled weight and activation constraints
- Efficient robot learning through human interaction
- Robust statistics for trustworthy AI
- Persuasive AI systems and human-AI interaction
- Large-scale knowledge graph reasoning

### Selected Papers

#### 3.1 Preventing Safety Drift in LLMs via Coupled Weight and Activation Constraints
- **Links**: [PaperNotes ACL 2026](https://papernotes.org/ACL2026/) (also appears at AAAI 2026)
- **Summary**: Proposes CWAC (Coupled Weight and Activation Constraints), constraining both weight update directions and safety-critical activation features during finetuning. Shows theoretically and empirically that constraining either weights or activations alone is insufficient.

#### 3.2 Efficient Robot Learning via Interaction with Humans
- **Authors**: Erdem Bıyık
- **Summary**: New Faculty Highlight. Comparison-based feedback for robot learning without the data-hungriness of demonstrations.

#### 3.3 Harnessing Robust Statistics for Trustworthy AI
- **Authors**: Xiaorui Liu
- **Summary**: New Faculty Highlight. Robust statistics for GNNs, LLMs, deep equilibrium models.

---

## 4. NeurIPS 2025

> **Location**: San Diego, CA | **Date**: December 2–7, 2025 | **Submissions**: ~12,000+

### Selected Papers

#### 4.1 Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference *(Oral)*
- **Authors**: Jiayi Yuan, Hao Li, Xinheng Ding, Wenya Xie, Yu-Jhe Li, Wentian Zhao, Kun Wan, Jing Shi, Xia Hu, Zirui Liu
- **Summary**: Investigates numerical sources of nondeterminism in LLM inference and proposes mitigation strategies. **(Oral)**

#### 4.2 Identifiability of Deep Polynomial Neural Networks *(Oral)*
- **Authors**: Konstantin Usevich, Ricardo Augusto Borsoi, Clara Dérand, Marianne Clausel
- **Summary**: Comprehensive analysis of the identifiability of deep PNNs, including architectures with and without bias terms. Shows architectures with non-increasing layer widths are generically identifiable under mild conditions. **(Oral)**

#### 4.3 Diffusion Models with Proximal Operators
- **Authors**: Sam D. Buchanan et al.
- **Affiliation**: UC Berkeley
- **Links**: [arXiv](https://arxiv.org/abs/2507.08956)
- **Summary**: Building diffusion models with proximal operators, leading to fewer NFEs at sampling time.

#### 4.4 Memorization and Generalization in Diffusion Models
- **Authors**: Sam D. Buchanan et al.
- **Affiliation**: UC Berkeley
- **Links**: [arXiv](https://arxiv.org/abs/2508.17689)
- **Summary**: Theoretical analysis of memorization and generalization in diffusion models.

---

## 5. CVPR 2026

> **Location**: Denver, CO | **Date**: June 3–7, 2026 | **Submissions**: 16,092 (+24% over 2025) | **Accepted**: 4,089 | **Acceptance rate**: ~25%

### Best Paper & Award Highlights

#### 5.1 CVPR 2026 Best Papers
- **Announced**: June 11, 2026 via [Newswise](https://www.newswise.com/articles/cvpr-2026-honors-the-years-most-innovative-computer-vision-and-ai-research)
- Dynamic scene reconstruction, 3D generative modeling, novel solutions for scene recovery

#### 5.2 NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: NVIDIA, Stanford, Caltech, UChicago, UT Austin
- **Summary**: A vision-action foundation model for generalist gaming agents trained on 40,000 hours of gameplay across 1,000+ games. Exhibits strong competence across diverse gaming domains.

#### 5.3 Black-box Membership Inference Attacks against Fine-tuned Diffusion Models
- **Authors**: University of Virginia
- **Summary**: First reconstruction-based membership inference attack framework tailored for diffusion models in black-box access setting. High precision across four attack scenarios.

### Apple at CVPR 2026 (14 papers)

#### 5.4 AToken: A Unified Tokenizer For Vision
- **Authors**: Byeongjoo Ahn, Jiasen Lu et al. (Apple)

#### 5.5 AMUSE: Audio-Visual Benchmark and Alignment Framework for Agentic Multi-Speaker Understanding
- **Authors**: Sanjoy Chowdhury et al. (Apple)

#### 5.6 STARFlow-V: End-to-End Video Generative Modeling with Normalizing Flows
- **Authors**: Jiatao Gu et al. (Apple)

#### 5.7 Velox: Learning Representations of 4D Geometry and Appearance
- **Authors**: Rick Chang et al. (Apple)

#### 5.8 SO-Bench: A Structural Output Evaluation of Multimodal LLMs
- **Authors**: Di Feng et al. (Apple)

### Other Notable CVPR 2026 Papers

#### 5.9 DirectFisheye-GS: Enabling Native Fisheye Input in Gaussian Splatting
- **Authors**: Zhengxian Yang, Fei Xie, Xutao Xue, Rui Zhang, Taicheng Huang, Yang Liu, Mengqi Ji, Tao Yu
- **Links**: [arXiv](https://arxiv.org/abs/2604.00648)
- **Summary**: Cross-view joint optimization for native fisheye input in 3D Gaussian Splatting.

#### 5.10 CompBench: Benchmarking Complex Instruction-guided Image Editing
- **Authors**: Bohan Jia, Wenxuan Huang et al. (Shanghai AI Lab)
- **Links**: [arXiv](https://arxiv.org/abs/2505.12200)
- **Summary**: A benchmark for complex instruction-guided image editing covering diverse editing scenarios.

---

## 6. ACL 2026 & EMNLP 2025

### ACL 2026
> **Location**: (To be announced) | **Date**: 2026

#### 6.1 Tenderness: A Library for Synthetic Data Generation
- **Authors**: Pavel Stepachev et al.
- **Links**: [arXiv](https://arxiv.org/abs/2601.18026)
- **Summary**: Synthetic data generation library for multilingual LLM training.

#### 6.2 CWAC: Preventing Safety Drift in LLMs
- **Links**: [PaperNotes ACL 2026](https://papernotes.org/ACL2026/)
- **Summary**: Coupled weight and activation constraints to prevent safety drift during fine-tuning.

### EMNLP 2025
> **Location**: Suzhou, China | **Date**: November 4–9, 2025 | **Submissions**: 8,174 | **Accepted**: 1,811 (22.2%)

#### 6.3 Speculative Streaming: Efficient and Scalable Speculative Decoding
- **Authors**: Nikhil Bhendawade, Irina Belousova, Qichen Fu, Henry Mason, Antonie Lin, Mohammad Rastegari, Mahyar Najibikohnehshahri
- **Affiliation**: Apple
- **Summary**: Multi-stream attention for efficient speculative decoding.

#### 6.4 Bias after Prompting: Persistent Discrimination in LLMs
- **Authors**: Niv Sivakumar, Natalie Mackraz, Samira Khorshidi, Krishna Patel, Barry Theobald, Luca Zappella, Nick Apostoloff
- **Affiliation**: Apple
- **Summary**: Studied persistent discrimination in LLMs even after prompting interventions.

#### 6.5 Evaluating Evaluation Metrics — The Mirage of Hallucination Detection
- **Authors**: Apple
- **Summary**: Critical analysis of hallucination detection metrics.

#### 6.6 ViMUL: A Culturally-diverse Multilingual Multimodal Video Benchmark
- **Authors**: MBZUAI / UCF / multiple institutions
- **Links**: [arXiv](https://arxiv.org/abs/2506.07032)
- **Summary**: A culturally-diverse multilingual multimodal video benchmark and model.

---

## 7. KDD 2025/2026

### KDD 2025
> **Location**: Toronto, Canada | **Date**: August 3–7, 2025

#### 7.1 BurstGPT: A Real-World Workload Dataset to Optimise LLM Serving Systems
- **Authors**: Yuxin Wang, Yuhan Chen, Zeyu Li, Xueze Kang, Yuchu Fang, Yeju Zhou, Yang Zheng, Zhenheng Tang, Xin He, Rui Guo, Xin Wang, Qiang Wang, Amelie Chi Zhou, Xiaowen Chu
- **Affiliation**: A*STAR CFAR / multiple
- **Links**: [arXiv](https://arxiv.org/abs/2401.17644)
- **Summary**: BurstGPT contains 10.31 million traces from Azure OpenAI GPT services over 213 days, capturing user request concurrency, conversation patterns, model response lengths, and system failures.

#### 7.2 Temporal Restoration and Spatial Rewiring for Source-Free Multivariate Time Series Domain Adaptation (TERSE)
- **Authors**: Peiliang Gong, Yucheng Wang, Min Wu, Zhenghua Chen, Xiaoli Li, Daoqiang Zhang
- **Links**: [arXiv](https://arxiv.org/abs/2505.21525)
- **Summary**: Novel SFDA method for multivariate time series using temporal restoration and spatial rewiring.

#### 7.3 FreRA: A Frequency-Refined Augmentation for Contrastive Learning on Time Series
- **Authors**: Tian Tian, Chunyao Miao, Hangwei Qian
- **Affiliation**: A*STAR CFAR
- **Links**: [arXiv](https://arxiv.org/abs/2505.23181)
- **Summary**: Lightweight frequency-domain augmentation for time series contrastive learning.

### KDD 2026
> **Location**: Jeju Island, South Korea | **Date**: August 9–13, 2026

#### 7.4 OneMall: End-to-End Generative Recommender Family at Kuaishou E-Commerce
- **Authors**: Kun Zhang, Jingming Zhang, Wei Cheng, Yansong Chen et al.
- **Affiliation**: Kuaishou
- **Summary**: End-to-end generative recommender family deployed at Kuaishou e-commerce.

#### 7.5 PROMISE: Process Reward Models Unlock Test-Time Scaling Laws in Generative Recommendations
- **Authors**: Chengcheng Guo, Kuo Cai, Yu Zhou, Qiang Luo, Ruimin et al.
- **Summary**: Process reward models for test-time scaling in generative recommendations.

---

## 8. SIGIR 2026

> **Location**: Melbourne, Australia | **Date**: July 20–24, 2026 | **Submissions**: 1,271 | **Accepted**: 234 (18.4%)

### Recommendation System Papers (~90 papers on RecSys topics)

#### 8.1 LRAT: Learning Retrievers from Agent Trajectories
- **Authors**: Yuqi Zhou et al.
- **Links**: [arXiv](https://arxiv.org/abs/2604.04949) | [GitHub](https://github.com/Yuqi-Zhou/LRAT)
- **Summary**: Trains retrievers from intermediate behaviors of strong search agents rather than from only final answers. Converts agent search trajectories into retrieval supervision.

### Key Themes (from [知乎 SIGIR2026 综述](https://zhuanlan.zhihu.com/p/2028040319111894904))
- **LLM-based Recommendation**: continues to lead
- **Cross-Domain Recommendation**: heating up significantly
- **Sequential Modeling**: comprehensive coverage
- **Generative Recommendation**: emerging paradigm

---

## 9. WWW 2026

> **Location**: Dubai, UAE (postponed from April to June 29–July 3, 2026)

### Selected RecSys & Ads Papers

#### 9.1 NEZHA: Zero-sacrifice and Hyperspeed Parallel Decoding for Generative Recommendations
- **Authors**: Yejing Wang, Shengyu Zhou, Jinyu Lu, Ziwei Liu, Langming Liu, Maolin Wang, Wenlin Zhang, Feng Li, Wenbo Su, Pengjie Wang, Jian Xu, Xiangyu Zhao et al.
- **Affiliation**: Taobao / City University of Hong Kong
- **Summary**: Industry track. **1 online launched system at Taobao**, serving over 100 million DAU and generating over 10 billion RMB in advertising revenue. Parallel decoding architecture for generative recommendations.

#### 9.2 SAGE: Global Semantic Alignment with LLMs for Long-Tail Sequential Recommendation
- **Authors**: Maolin Wang, Tongshu Bian, Ziyan Wang, Xiaotong Jiang et al.
- **Affiliation**: City University of Hong Kong

#### 9.3 BlossomRec: Block-level Fused Sparse Attention Mechanism for Sequential Recommendations
- **Authors**: Mengyang Ma, Xiaopeng Li, Wanyu Wang et al.
- **Affiliation**: City University of Hong Kong

#### 9.4 AgentDR: Dynamic Recommendation with Implicit Item-Item Relations via LLM-based Agents
- **Authors**: Mingdai Yang, Nurendra Choudhary, Jiangshu Du, Edward W. Huang, Philip Yu, Karthik Subbian, Danai Koutra
- **Affiliation**: Amazon / UIUC

#### 9.5 FeDecider: An LLM-Based Framework for Federated Cross-Domain Recommendation
- **Authors**: Xinrui He et al.
- **Affiliation**: UIUC / Amazon

#### 9.6 From Prediction to Understanding: Leveraging Reasoning in LLM-based Recommendations
- **Authors**: Zhi-Yuan Chen et al.

#### 9.7 ScotRec: Social Chain-of-Thought LLM Reasoning for Recommendation
- **Authors**: Kaibei Li et al.

#### 9.8 Gaussian Mixture Flow Matching with Domain Alignment for Multi-Domain Sequential Recommendation
- **Authors**: Xiaoxin Ye et al.

---

## 10. CIKM 2025

> **Location**: Seoul, South Korea | **Date**: November 10–14, 2025 | **Submissions**: 1,627 (full papers) | **Accepted**: 443 (27.2%)

### Selected Papers

#### 10.1 DashCLIP: Leveraging Multimodal Models for Generating Semantic Embeddings
- **Authors**: Omkar Gurjar, Kin Sum Liu, Praveen Kolli, Utsaw Kumar, Mandar Rahurkar
- **Affiliation**: DoorDash
- **Links**: [arXiv](https://arxiv.org/abs/2504.07110)
- **Summary**: Built a framework to generate generalizable multimodal representations for CPG products and user queries using contrastive learning. Contributed to significant performance improvement across ranking and retrieval tasks at DoorDash.

#### 10.2 AGENTiGraph: Multi-Agent Knowledge Graph Interaction
- **Authors**: Fan Gao et al.
- **Affiliation**: University of Tokyo
- **Summary**: Multi-agent architecture for dynamic knowledge graph interactions. Achieves 95.12% accuracy on 3,500 test cases.

#### 10.3 HealthGenie: Interactive Knowledge-Driven LLM Framework for Dietary Guidance
- **Authors**: Fan Gao, Xinjie Zhao et al.
- **Summary**: Combines LLMs and Knowledge Graphs for personalized dietary guidance.

---

## 11. RecSys 2025

> **Location**: Prague, Czech Republic | **Date**: September 22–26, 2025 | **Submissions**: 261 | **Accepted**: 49 (19%)

### Selected Papers

#### 11.1 Beyond Immediate Click: Engagement-Aware and MoE-Enhanced Transformers
- **Links**: [ACM DL](https://dl.acm.org/doi/10.1145/3705328.3748076)
- **Summary**: Engagement-aware sequential movie recommendation with Mixture-of-Experts enhanced Transformers.

#### 11.2 LEAF: Lightweight, Efficient, Adaptive and Flexible Embedding for Large-Scale Recommendation
- **Links**: [ACM DL](https://dl.acm.org/doi/10.1145/3705328.3748078)
- **Summary**: Efficient embedding framework for large-scale recommendation models.

#### 11.3 Lasso: LLM-based User Simulator for Cross-Domain Recommendation
- **Links**: [ACM DL](https://dl.acm.org/doi/10.1145/3705328.3748048)
- **Summary**: Large Language Model-based user simulator for cross-domain recommendation.

#### 11.4 Exploring Scaling Laws of CTR Model for Online Performance Improvement
- **Links**: [arXiv](https://arxiv.org/abs/2508.15326)
- **Summary**: Investigates scaling laws for CTR prediction models in industrial settings.

#### 11.5 Multi-Granularity Distribution Modeling for Video Watch Time Prediction
- **Links**: [arXiv](https://arxiv.org/abs/2508.12665)
- **Summary**: Exponential-Gaussian Mixture Network for video watch time prediction.

---

## 12. Agent Systems & Tool Use

### 12.1 AlphaEvolve: LLM Rewrites Its Own Game Theory Algorithms
- **Authors**: Google DeepMind
- **Links**: [MarkTechPost](https://www.marktechpost.com/2026/04/03/google-deepminds-research-lets-an-llm-rewrite-its-own-game-theory-algorithms-and-it-outperformed-the-experts)
- **Summary**: An LLM-powered evolutionary coding agent that replaces manual algorithm design for Multi-Agent Reinforcement Learning (MARL). Applied to Counterfactual Regret Minimization (CFR) and Policy Space Response Oracles (PSRO). Discovers new algorithm variants that perform competitively against or better than hand-designed baselines.

### 12.2 MCMA: Meta-Cognitive Memory Abstraction for LLM Agents
- **Authors**: Multiple
- **Links**: [arXiv](https://arxiv.org/html/2601.07470v1)
- **Summary**: Proposes meta-cognitive memory abstraction method that learns structured abstract memory representations and organizes reusable hierarchical abstractions. Memory copilot trained via DPO can be transferred across domains. Experiments on ALFWorld, ScienceWorld, and BabyAI demonstrate substantial gains in robustness and OOD generalization.

### 12.3 KAIROS Benchmark
- **Authors**: Lambda Lab et al.
- **Venue**: ICLR 2026
- **Summary**: Drops models into collaborative scenarios with unreliable peers and adversarial participants, revealing that LLMs cave under peer pressure. RL recipe helps smaller models resist.

### 12.4 OpenAI o1 System Card
- **Authors**: OpenAI
- **Links**: [arXiv](https://arxiv.org/abs/2412.16720v2) (updated April 2026)
- **Summary**: o1 model series trained with large-scale RL to reason using chain of thought. Deliberative alignment for safety. State-of-the-art performance on risks such as generating illicit advice, stereotyped responses, and resisting jailbreaks.

---

## 13. CTR Prediction & Advertising

### 13.1 HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction in CTR Prediction
- **Authors**: Yunwen Huang, Shiyong Hong, Xijun Xiao, Jinqiu Jin, Xuanyuan Luo, Zhe Wang, Zheng Chai, Shikang Wu, Yuchao Zheng, Jingjian Lin
- **Affiliation**: ByteDance
- **Links**: [arXiv](https://arxiv.org/html/2601.12681v2)
- **Summary**: Presents HyFormer, a unified hybrid transformer architecture that tightly integrates long-sequence modeling and feature interaction into a single backbone. Two core components: *Query Decoding* (expands non-sequential features into Global Tokens and performs long sequence decoding) and *Query Boosting* (enhances cross-query and cross-sequence heterogeneous interactions). Outperforms LONGER and RankMixer baselines on billion-scale industrial datasets. Significant gains in online A/B tests.

### 13.2 GR4AD: Generative Recommendation for Large-Scale Advertising
- **Authors**: Ben Xue, Dan Liu, Lixiang Wang, Mingjie Sun et al. (Kuaishou)
- **Links**: [arXiv](https://arxiv.org/abs/2602.22732)
- **Summary**: Production-oriented generative recommender co-designed across architecture, learning, and serving. Fully deployed in Kuaishou advertising system with over 400 million users. Achieves high-throughput real-time serving.

### 13.3 Tencent Advertising Algorithm Challenge 2025: All-Modality Generative Recommendation
- **Authors**: Junwei Pan, Wei Xue, Chao Zhou, Xing Zhou et al.
- **Affiliation**: Tencent
- **Links**: [arXiv](https://arxiv.org/abs/2604.04976)
- **Summary**: Introduces TencentGR-1M and TencentGR-10M datasets for generative recommendation in advertising. Rich collaborative IDs and multi-modal representations from real Tencent Ads logs. Weighted evaluation for high-value conversion events.

### 13.4 Unified Value Alignment for Generative Recommendation in Industrial Advertising
- **Links**: [Semantic Scholar](https://www.semanticscholar.org/paper/Generative-Recommendation-for-Large-Scale-Xue-Liu/d8023df8a43e30a25d8144ecfcd2b02c00eae4ba)
- **Summary**: Commercial SID tokenizer injecting value-related attributes into SID construction. Generation-as-Ranking SID Decoder jointly optimized by supervised learning and eCPM-aware reinforcement learning.

---

## 14. Generative Models & Diffusion Transformers

### 14.1 Diffusion Transformers with Representation Autoencoders
- **Venue**: ICLR 2026
- **Summary**: Explores combining diffusion transformers with representation autoencoders for improved generative modeling.

### 14.2 PixelDiT: Pixel Diffusion Transformers for Image Generation
- **Authors**: Multiple
- **Links**: [arXiv](https://arxiv.org/abs/2511.20645)
- **Summary**: Single-stage, end-to-end model eliminating the need for autoencoder, learning diffusion process directly in pixel space.

### 14.3 SeedVR2: One-Step Video Restoration via Diffusion Adversarial Post-Training
- **Authors**: J. Wang, S. Lin, Z. Lin et al.
- **Venue**: ICLR 2026
- **Links**: [arXiv](https://arxiv.org/abs/2506.05301)
- **Summary**: One-step diffusion video restoration via adversarial post-training.

### 14.4 Diffusion Transformers (DiT) — Continued Scaling
- **Summary**: DiT-based architectures continuing to dominate generative modeling, with improved scaling properties. Key advances: adaLN modulation, flow matching integration, multi-modal conditioning.

---

## 15. LLM Reasoning & Test-Time Compute

### 15.1 Transformers are Inherently Succinct *(ICLR 2026 Outstanding Paper)*
- See §1.1 for details.

### 15.2 LLMs Get Lost In Multi-Turn Conversation *(ICLR 2026 Outstanding Paper)*
- See §1.2 for details.

### 15.3 Provable Benefit of Curriculum in Transformer Tree-Reasoning Post-Training *(ICML 2026)*
- See §2.2 for details.

### 15.4 OpenAI o1 / o3 — Chain-of-Thought Reasoning
- **Summary**: RL-based reasoning scaling. Deliberative alignment for safety. State-of-the-art across mathematical reasoning, coding, and scientific benchmarks.

### 15.5 DeepSeek-R1 — Reasoning via RL
- **Summary**: Open-source reasoning model using RL without supervised data. Demonstrates emergent reasoning capabilities through pure RL training.

---

## 16. Code Generation & Execution Prediction

### 16.1 MatClaw: An Autonomous Code-First LLM Agent for Materials Science
- **Authors**: Multiple
- **Links**: [arXiv](https://arxiv.org/abs/2604.02688)
- **Summary**: Code-first agent that writes and executes Python directly, composing domain libraries to orchestrate multi-code workflows on remote HPC clusters without predefined tool functions.

### 16.2 OpenHands: Open Platform for AI Software Developers
- **Summary**: Execution-grounded LLM coding agent platform. Separates agent logic, event-stream state management, and sandboxed runtime execution. Enables autonomous software engineering.

### 16.3 CodeAct: Executable Code Actions Elicit Better LLM Agents
- **Summary**: Treats executable code as the action representation of an agent. Execution becomes part of the agent's internal loop — model writes and runs code to gather feedback.

### 16.4 Survey on Code Generation with LLM-based Agents
- **Authors**: Yihong Dong, Xue Jiang, Jiaru Qian et al. (Peking University)
- **Links**: [arXiv](https://arxiv.org/html/2508.00083v1)
- **Summary**: Comprehensive survey covering single-agent and multi-agent architectures for code generation across the full software development lifecycle.

---

## 17. Key Trends & Synthesis

### Architecture & Models
- **Inference-first design**: Mamba-3 demonstrates that optimizing for inference efficiency (linear compute, constant memory) can match or exceed Transformer quality
- **MoE dominance**: Most frontier models now use Mixture-of-Experts (DeepSeek V4, Nemotron 3, Qwen 3.x)
- **Hybrid Mamba-Transformer**: Nemotron 3 validates hybrid SSM-Transformer approaches

### Recommendation Systems
- **Generative Recommendation**: paradigm shift from cascaded retrieval-ranking to end-to-end generation (OneMall, GR4AD, NEZHA, PROMISE)
- **LLM-based Recommendation**: continues to dominate SIGIR 2026 (~90 RecSys papers)
- **Scaling Laws for CTR**: both academic (Scaling Laws of CTR) and industrial (ByteDance HyFormer) exploration
- **Value-aware generation**: unified value alignment in generative recommendation (Kuaishou, Tencent)

### LLM Reasoning & Agents
- **Test-time compute scaling**: o1/o3, DeepSeek-R1, curriculum RL all point to reasoning-time compute as a new scaling axis
- **Multi-turn degradation**: identified and characterized (ICLR 2026 Outstanding Paper)
- **Agent systems**: memory abstraction (MCMA), agentic coding (CodeAct, OpenHands, MatClaw), game-theoretic agent evolution (AlphaEvolve)
- **Safety**: persistent discrimination, safety drift, alignment depth — all active areas

### Key Statistics Across Venues
| Venue | Year | Submissions | Accepted | Rate |
|-------|------|-------------|----------|------|
| ICML | 2026 | 23,918 | 6,352 | 26.6% |
| ICLR | 2026 | 11,672 | ~3,110 | 26.6% |
| CVPR | 2026 | 16,092 | 4,089 | ~25% |
| NeurIPS | 2025 | ~12,000 | ~3,200 | ~27% |
| EMNLP | 2025 | 8,174 | 1,811 | 22.2% |
| SIGIR | 2026 | 1,271 | 234 | 18.4% |
| KDD | 2026 | — | — | — |
| RecSys | 2025 | 261 | 49 | 19% |
| WWW | 2026 | — | — | — |
| CIKM | 2025 | 1,627 | 443 | 27.2% |
| AAAI | 2026 | — | — | — |

### Industry Labs Activity (ordered by volume)
1. **Google DeepMind**: AlphaEvolve, Gemini 3.5/Omni, Gemma 4, VGGT (CVPR 2025 Best Paper)
2. **Apple**: 14 papers at CVPR 2026 (AToken, AMUSE, STARFlow-V, Velox, SO-Bench), EMNLP 2025 papers on speculative decoding and bias
3. **NVIDIA**: NitroGen (gaming agents), Nemotron 3, pi-Flow
4. **ByteDance**: HyFormer (CTR), TokenMixer-Large, Douyin
5. **Kuaishou**: OneMall, GR4AD, value alignment for generative Rec
6. **Tencent**: TencentGR-1M/10M datasets, all-modality generative Rec
7. **Meta**: Llama 4, VGGT collaboration
8. **Alibaba/Taobao**: NEZHA (WWW 2026 Industry Track), Large User Model
9. **Amazon**: AgentDR, FeDecider, DashCLIP
10. **OpenAI**: o1 System Card, GPT-5, o3 reasoning
11. **Anthropic**: Claude Fable 5, Opus 4.8, S-1
12. **Netflix**: GenRec scaling laws
