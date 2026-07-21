---
title: arXiv AI Research Search Report
type: synthesis
created: 2026-07-21
updated: 2026-07-21
tags: [arxiv, AI, LLM, recommendation, advertising, sequential-modeling, CTR, games, reasoning, agents]
---

# arXiv AI Research Search Report — 2026-07-21

Curated selection of recent arXiv papers spanning LLMs, CTR prediction, recommendation systems, advertising/bidding, sequential modeling, AI games, and reasoning/agents.

---

## 1. Large Language Models (LLMs)

### 1.1 Challenges and Research Directions for Large Language Model Inference Hardware

- **Authors:** Xiaoyu Ma, David Patterson
- **Institution/Company:** Google
- **Date:** 2026-01-08 (Accepted by IEEE Computer, 2026)
- **Abstract:** LLM inference is fundamentally different from training due to the autoregressive Decode phase. The primary challenges are memory and interconnect rather than compute. The paper highlights four architecture research opportunities: High Bandwidth Flash for 10X memory capacity with HBM-like bandwidth; Processing-Near-Memory and 3D memory-logic stacking for high memory bandwidth; and low-latency interconnect to speedup communication.
- **Key Innovations:**
  - Identifies memory/interconnect (not compute) as the primary LLM inference bottleneck
  - Proposes High Bandwidth Flash for 10x memory capacity with HBM-like bandwidth
  - Introduces Processing-Near-Memory and 3D memory-logic stacking architectures
  - Reviews applicability for both datacenter and mobile devices
- **Link:** https://arxiv.org/abs/2601.05047

### 1.2 LLMs as High-Dimensional Nonlinear Autoregressive Models with Attention: Training, Alignment and Inference

- **Authors:** Vikram Krishnamurthy
- **Institution/Company:** Cornell University
- **Date:** 2026-01-31
- **Abstract:** Provides a concise mathematical reference formulating LLMs as high-dimensional nonlinear autoregressive models with attention-based dependencies. The framework encompasses pretraining via next-token prediction, alignment methods (RLHF, DPO, RSFT, RLVR), and autoregressive generation. Self-attention emerges as a repeated bilinear-softmax-linear composition.
- **Key Innovations:**
  - Unified mathematical formulation of LLM training, alignment, and inference
  - Covers RLHF, DPO, RSFT, and RLVR under one framework
  - Enables principled analysis of sycophancy, hallucination, in-context learning, and CoT prompting
  - Includes nanoGPT/nanochat-style code examples for reproducibility
- **Link:** https://arxiv.org/abs/2602.00426

### 1.3 Understanding Reasoning from Pretraining to Post-Training

- **Authors:** Jingyan Shen, Ang Li, Salman Rahman, Yifan Sun, Micah Goldblum, Matus Telgarsky, Pavel Izmailov
- **Institution/Company:** University of Illinois Urbana-Champaign
- **Date:** 2026-07-17
- **Abstract:** Uses chess as a controlled testbed to study how pretraining choices shape RL post-training returns. Finds that post-RL performance at a given compute level is well-predicted from pretraining loss, and RL does not simply sharpen the SFT policy—it amplifies correct moves on easy puzzles and surfaces nearly absent correct moves on hard puzzles.
- **Key Innovations:**
  - Controlled study of pretraining-to-post-training pipeline using chess as a testbed
  - Demonstrates pretraining loss predicts post-RL performance across compute budgets
  - Shows RL has qualitatively different effects on easy vs. hard problems
  - Establishes relationship between pretraining tokens and RL reward curve slope
- **Link:** https://arxiv.org/abs/2607.16097

### 1.4 Agentic Chain-of-Thought Steering for Efficient and Controllable LLM Reasoning

- **Authors:** Yu Xia, Zhouhang Xie, Xin Xu, Byungkyu Kang, Prarit Lamba, Xiang Gao, Julian McAuley
- **Institution/Company:** UC San Diego
- **Date:** 2026-06-02
- **Abstract:** Proposes ACTS, which formulates reasoning steering as a Markov decision process where a controller agent adaptively steers a frozen reasoner during inference. At each step, the controller observes the reasoning trace and remaining thinking budget, then issues a steering action consisting of a reasoning strategy and a steering phrase.
- **Key Innovations:**
  - MDP-based framework for adaptive inference-time reasoning control
  - Budget-aware strategy control that preserves generation continuity
  - Controller initialized from synthetic steering trajectories with multi-budget augmentation
  - Reinforcement learning optimization with budget-conditioned reward shaping
- **Link:** https://arxiv.org/abs/2606.03965

---

## 2. CTR Prediction

### 2.1 Dual-Stream MLP is All You Need for CTR Prediction

- **Authors:** Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution/Company:** Renmin University of China
- **Date:** 2026-06-03 (Accepted by TKDD)
- **Abstract:** Proposes DS-MLP, a novel feature interaction framework for CTR prediction. It leverages knowledge distillation to consolidate explicit feature interaction learning into a main MLP, while a parallel MLP captures implicit interactions as a complement. Despite being a vanilla MLP, it achieves SOTA on three benchmarks.
- **Key Innovations:**
  - Dual-stream MLP architecture with knowledge distillation for explicit/implicit feature interactions
  - Two alignment strategies for optimizing dual MLP components
  - SOTA performance with a simple MLP (no complex feature interaction engineering)
  - Scalable solution for large-scale recommendation systems
- **Link:** https://arxiv.org/abs/2606.04944

### 2.2 Generative Long-term User Interest Modeling for Click-Through Rate Prediction

- **Authors:** Jiangli Shao, Kaifu Zheng, Hao Fang, Huimu Ye, Zhiwei Liu, Bo Zhang, Shu Han, Xingxing Wang
- **Institution/Company:** Meituan, Beijing, China
- **Date:** 2026-05-15
- **Abstract:** Proposes GenLI for CTR prediction. It consists of an interest generation module (IGM), behavior retrieval module (BRM), and interest fusion module (IFM). IGM generates multiple target-independent interest distributions; BRM selects behaviors via simple lookup (O(1) complexity); IFM uses gating mechanisms for interest features.
- **Key Innovations:**
  - Generative approach to long-term user interest modeling (target-independent)
  - O(1) time complexity for behavior retrieval via simple lookup
  - Multiple interest distribution generation for diverse interest capture
  - Deployed in production serving hundreds of millions of users at Meituan
- **Link:** https://arxiv.org/abs/2605.15905

### 2.3 IDProxy: Cold-Start CTR Prediction for Ads and Recommendation

- **Authors:** (Multiple authors)
- **Institution/Company:** (Industry lab)
- **Date:** 2026-06-24
- **Abstract:** Addresses the cold-start CTR prediction problem for new items with no historical behavior patterns, proposing IDProxy as a solution for ads and recommendation systems.
- **Key Innovations:**
  - Addresses cold-start CTR prediction without historical item behavior data
  - Novel proxy mechanism for new item representation
- **Link:** https://arxiv.org/abs/2606.28191

---

## 3. Recommendation Systems

### 3.1 Efficient Sequential Recommendation for Long Term User Interest Via Personalization

- **Authors:** Qiang Zhang, Hanchao Yu, Ivan Ji, Chen Yuan, Yi Zhang, Chihuang Liu, Xiaolong Wang, Christopher E. Lambert, Ren Chen, Chen Kovacs, Xinzhu Bei, Renqin Cai, Rui Li, Lizhu Zhang, Xiangjun Fan, Qunshu Zhang, Benyu Zhang
- **Institution/Company:** Meta (Facebook Research)
- **Date:** 2026-01-07 (ICDM 2025)
- **Abstract:** Compresses long user interaction histories into learnable tokens, combined with recent interactions for recommendations. Significantly reduces computational costs while maintaining high accuracy. Applicable to HSTU and HLLM transformer-based recommendation models.
- **Key Innovations:**
  - Personalized token compression of long user histories into learnable tokens
  - Applicable to existing transformer-based recommenders (HSTU, HLLM)
  - Addresses quadratic scaling of transformer-based sequential models
  - Open source: https://github.com/facebookresearch/PerSRec
- **Link:** https://arxiv.org/abs/2601.03479

### 3.2 OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender

- **Authors:** Zhaoqi Zhang, Haolei Pei, Jun Guo, Tianyu Wang, Yufei Feng, Hui Sun, Shaowei Liu, Aixin Sun
- **Institution/Company:** Nanyang Technological University / ByteDance
- **Date:** 2026 (Accepted at WWW 2026)
- **Abstract:** A single Transformer backbone that jointly performs user-behavior sequence modeling and feature interaction. A unified tokenizer converts both sequential and non-sequential attributes into one token sequence. Stacked blocks use mixed parameterization with causal attention and cross-request KV caching.
- **Key Innovations:**
  - Unified tokenizer for sequential and non-sequential features in one Transformer
  - Mixed parameterization: shared params for sequential tokens, token-specific for non-sequential
  - Cross-request KV caching for reducing training and inference cost
  - 5.68% lift in per-user GMV in online A/B testing at industrial scale
- **Link:** https://arxiv.org/abs/2510.26104

### 3.3 RGAlign-Rec: Ranking-Guided Alignment for Latent Query Reasoning in Recommendation Systems

- **Authors:** (Multiple authors)
- **Institution/Company:** Shopee
- **Date:** 2026-02-16
- **Abstract:** A closed-loop alignment framework integrating an LLM-based semantic reasoner with a Query-Enhanced (QE) ranking model. Uses Ranking-Guided Alignment (RGA) multi-stage training with downstream ranking signals as feedback.
- **Key Innovations:**
  - Multi-stage RGA training using downstream ranking signals to refine LLM reasoning
  - Query-Enhanced recommendation model for proactive intent prediction
  - 3.52% relative reduction in error rate and 0.98% improvement in CTR online
  - Bridges semantic gap between user features and knowledge base intents
- **Link:** https://arxiv.org/abs/2602.12968

---

## 4. Advertising & Auto-Bidding

### 4.1 AHBid: An Adaptable Hierarchical Bidding Framework for Cross-Channel Advertising

- **Authors:** Xinxin Yang, Yangyang Tang, Yikun Zhou, Yaolei Liu, Yun Li, Bo Yang
- **Institution/Company:** (Industry team)
- **Date:** 2026-02-26 (Accepted at WWW 2026)
- **Abstract:** Integrates generative planning with real-time control for multi-channel advertising. Employs a high-level generative planner based on diffusion models for dynamic budget allocation, with constraint enforcement and trajectory refinement mechanisms.
- **Key Innovations:**
  - Diffusion model-based generative planner for budget allocation across channels
  - Constraint enforcement mechanism for multi-channel compliance
  - Trajectory refinement for environmental adaptability using historical data
  - 13.57% increase in overall return in online A/B tests
- **Link:** https://arxiv.org/abs/2602.22650

### 4.2 Generative Auto-Bidding with Unified Modeling and Exploration (GUIDE)

- **Authors:** Mingming Zhang, Feiqing Zhuang, Na Li, Shengjie Sun, Xiaowei Chen, Junxiong Zhu, Fei Xiao, Keping Yang, Lixin Zou, Chenliang Li
- **Institution/Company:** Alibaba (Taobao)
- **Date:** 2026-05-19 (SIGIR 2026)
- **Abstract:** Uses Decision Transformer to jointly model historical bidding actions and state transitions. A Q-value module guides exploration via regularization, while an Inverse Dynamics Module provides a safe policy fallback. Online deployment on Taobao achieved +4.10% ad GMV, +1.40% ad clicks, +3.52% ad ROI.
- **Key Innovations:**
  - "Explore-safeguard-select" pipeline unifying efficiency and safety
  - Decision Transformer for joint modeling of bidding actions and environment
  - Inverse Dynamics Module for behaviorally consistent safe fallback actions
  - Large-scale deployment on Taobao with significant business metrics improvement
- **Link:** https://arxiv.org/abs/2605.19457

### 4.3 GRAD: Generative Large-Scale Pre-trained Models for Automated Ad Bidding Optimization

- **Authors:** (Meituan team)
- **Institution/Company:** Meituan
- **Date:** 2026-04-20 (KDD 2026)
- **Abstract:** A scalable foundation model for auto-bidding combining Action-Mixture-of-Experts module for diverse bidding action exploration with Value Estimator of Causal Transformer for constraint-aware optimization. Deployed at Meituan with 2.18% GMV increase and 10.68% ROI increase.
- **Key Innovations:**
  - Foundation model approach to auto-bidding with Mixture-of-Experts action module
  - Causal Transformer Value Estimator for constraint optimization (CPM, ROI)
  - Addresses offline-online distribution shift challenge
  - Deployed on one of the world's largest food delivery platforms
- **Link:** https://dl.acm.org/doi/10.1145/3770854.3783956

### 4.4 Generative Click-through Rate Prediction with Applications to Search Advertising

- **Authors:** Lingwei Kong, Lu Wang, Changping Peng, Zhangang Lin, Ching Law, Jingping Shao
- **Institution/Company:** (Large e-commerce platform)
- **Date:** 2025-07-15
- **Abstract:** Two-stage training process leveraging generative pre-training for next-item prediction to enhance discriminative CTR prediction. Uses conditional self-condition decoder and conditional negative sampling, then parameter sharing and model integration during discriminative fine-tuning.
- **Key Innovations:**
  - Two-stage generative-discriminative training paradigm
  - Conditional self-condition decoder for next-item prediction pre-training
  - Deployed on a major e-commerce platform serving hundreds of millions of users
- **Link:** https://arxiv.org/abs/2507.11246

---

## 5. Sequential Modeling

### 5.1 Multi-Behavior Sequential Modeling with Transition-Aware Graph Attention Network for E-Commerce Recommendation

- **Authors:** Hanqi Jin, Gaoming Yang, Zhangming Chan, Yapeng Yuan, Longbin Li, Fei Sun, Yeqiu Yang, et al.
- **Institution/Company:** (Multiple authors)
- **Date:** 2026-01-21
- **Abstract:** Addresses multi-behavior sequential modeling in e-commerce using transition-aware graph attention networks to capture complex behavior transitions and user preferences.
- **Key Innovations:**
  - Transition-aware graph attention for behavior sequence modeling
  - Multi-behavior modeling for e-commerce recommendation
  - Captures complex inter-behavior transition patterns
- **Link:** https://arxiv.org/abs/2601.13181

### 5.5 CoderRec: Cross-Scale Collaboration between LLMs and Lightweight Sequential Recommenders

- **Authors:** (Tsinghua University team)
- **Institution/Company:** Tsinghua University / Beijing National Research Center for Information Science and Technology
- **Date:** 2026
- **Abstract:** Introduces latent reasoning into sequential recommendation. Treats representations learned by downstream recommendation model as domain-specific latent thoughts that guide LLM training via cross-scale collaboration.
- **Key Innovations:**
  - Cross-scale model collaboration between large LLMs and small recommendation models
  - Domain-specific latent reasoning for recommendation
  - RQVAE-based warmup for semantic space alignment
  - Treats recommendation representations as "latent thoughts" for LLM guidance
- **Link:** https://arxiv.org/abs/2601.03479 (related work)

---

## 6. AI Games

### 6.1 Game-Theory-Assisted Reinforcement Learning for Border Defense

- **Authors:** Goutam Das, Michael Dorothy, Kyle Volle, Daigo Shishika
- **Institution/Company:** (US Military Academy / West Point)
- **Date:** 2026-03-16 (ACC 2026)
- **Abstract:** Introduces a hybrid approach leveraging game-theoretic insights to improve RL training efficiency. Uses Apollonius Circle to compute equilibrium in post-detection phase, enabling early termination of RL episodes without learning pursuit dynamics.
- **Key Innovations:**
  - Hybrid game-theory + RL approach for adversarial pursuit-evasion
  - Apollonius Circle for analytical equilibrium computation in pursuit phase
  - Early termination strategy: RL learns search, game theory handles pursuit
  - 10-20% higher rewards and faster convergence across single/multi-defender settings
- **Link:** https://arxiv.org/abs/2603.15907

### 6.2 Augmenting Game AI with Deep Reinforcement Learning

- **Authors:** (Conference on Games 2026 authors)
- **Institution/Company:** (Multiple)
- **Date:** 2026-06-19
- **Abstract:** Survey paper on how RL can create more believable game AI. Identifies key bottlenecks including sample efficiency, generalization, and the tension between optimal and believable behavior. Provides a genre-level readiness framework for game studio AI teams.
- **Key Innovations:**
  - Genre-level readiness framework for RL in game AI deployment
  - Identifies believability (not optimality) as the hard problem
  - Catalogs sample efficiency as the key bottleneck for deployment
  - Survey of real-world deployment examples across game genres
- **Link:** https://arxiv.org/abs/2606.20210

### 6.3 Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Player Games

- **Authors:** (Multiple authors)
- **Institution/Company:** (Multiple)
- **Date:** 2026-05-06
- **Abstract:** Teaches language models to play strategic games better through reinforcement learning with feedback on move quality, rather than generating the first response.
- **Key Innovations:**
  - RL-based strategic reasoning for LLMs in multi-player games
  - Move quality feedback for iterative improvement
  - Beyond one-shot generation to strategic multi-step play
- **Link:** https://arxiv.org/abs/2605.04725

### 6.4 LLM Semantic Signaling Game and Mechanism Design

- **Authors:** Quanyan Zhu
- **Institution/Company:** New York University
- **Date:** 2026-06-27
- **Abstract:** Studies systematic blindness, awareness shaping, and mindset dynamics in LLM-based semantic signaling games, analyzing how LLMs behave in strategic communication settings.
- **Key Innovations:**
  - Game-theoretic framework for analyzing LLM signaling behavior
  - Mechanism design for LLM-based communication systems
  - Analysis of systematic blindness and mindset dynamics
- **Link:** https://arxiv.org/abs/2606.29113

### 6.5 GameCraft-Bench: Can Agents Build Playable Games End-to-End?

- **Authors:** Tongxu Luo, Rongsheng Wang, et al.
- **Institution/Company:** (Multiple)
- **Date:** 2026-06-16
- **Abstract:** Benchmark for evaluating whether AI agents can build playable games end-to-end in a real game engine.
- **Key Innovations:**
  - Benchmark for end-to-end game generation by AI agents
  - Evaluation in real game engines (not just code generation)
  - Tests agent capabilities across game design, implementation, and playability
- **Link:** https://arxiv.org/abs/2606.17861

---

## 7. Reasoning & Agents

### 7.1 Understanding Large Language Models (Cognitive Science Perspective)

- **Authors:** (Multiple authors)
- **Institution/Company:** (Multiple)
- **Date:** 2026-07-14
- **Abstract:** Synthesizes current research on LLM architecture, emergent cognitive-like behaviors, and interpretability methods, providing a philosophical argument against reductionist views of AI cognition.
- **Key Innovations:**
  - Non-reductionist philosophical framework for LLM cognition
  - Bridge between AI research and cognitive science
  - Analysis of emergent cognitive-like behaviors
- **Link:** https://arxiv.org/abs/2607.01006

### 7.2 LLM Vulnerabilities Survey: Attacks, Risks, Defenses, and Open Problems

- **Authors:** (Multiple authors)
- **Institution/Company:** (Multiple)
- **Date:** 2026-06-30
- **Abstract:** Comprehensive systematization of LLM vulnerabilities across the entire lifecycle and application stack. Provides a structured framework for understanding security risks and outlines a strategic research agenda.
- **Key Innovations:**
  - Novel taxonomy of LLM vulnerabilities across eight lifecycle stages
  - Identifies critical trust boundary failures
  - Strategic research agenda for secure LLM deployment
  - Maps vulnerabilities across the application stack
- **Link:** https://arxiv.org/abs/2606.31639

### 7.3 Zero RL: Advancing Math Reasoning from Scratch via Multi-Stage Self-Iterative Training

- **Authors:** Alibaba DAMO Academy team
- **Institution/Company:** Alibaba DAMO Academy
- **Date:** 2026-07
- **Abstract:** Demonstrates that advanced mathematical reasoning can be bootstrapped from scratch without any human-annotated data, achieving 84.2% on AIME 2026. Larger models disproportionately benefit and spontaneously develop structured reasoning with step markers.
- **Key Innovations:**
  - Zero-data math reasoning via multi-stage self-iterative training
  - 84.2% on AIME 2026 benchmark
  - Discovery that larger models spontaneously develop step markers
  - No human-annotated data required
- **Link:** https://arxiv.org/abs/2607.10383 (related work series)

### 7.4 Harmonizing AI Safety Thresholds

- **Authors:** Wilber Sean Anterola, Matthew Ball, Luis F. Lafuerza, Markov Grey
- **Institution/Company:** (Multiple)
- **Date:** 2026-07-17
- **Abstract:** Develops a methodology for deriving harmonized capability thresholds across misuse risks (cyber and biological), and automated AI R&D, using expected harm and observed rate of AI progress as key primitives.
- **Key Innovations:**
  - Cross-company harmonization of safety thresholds
  - Risk-modeling approach for misuse risk with explicit risk channels
  - Threshold based on observed AI progress rate for automated AI R&D
  - Addresses race-to-the-bottom in safety standards
- **Link:** https://arxiv.org/abs/2607.16112

### 7.5 Understanding Reasoning from Pretraining to Post-Training

- **Authors:** Jingyan Shen, Ang Li, Salman Rahman, Yifan Sun, Micah Goldblum, Matus Telgarsky, Pavel Izmailov
- **Institution/Company:** University of Illinois Urbana-Champaign
- **Date:** 2026-07-17
- **Abstract:** Uses chess as a controlled testbed to study how pretraining choices shape RL post-training returns across a full pipeline from 5M to 1B parameters.
- **Key Innovations:**
  - Controlled pretraining-to-Post-RL study using chess
  - Pretraining loss as predictor of post-RL performance
  - Quantifies how RL amplifies vs. surfaces correct reasoning
- **Link:** https://arxiv.org/abs/2607.16097

---

## Summary of Key Trends (2026)

| Theme | Trend |
|-------|-------|
| **LLM Inference** | Memory/interconnect (not compute) identified as the primary bottleneck; High Bandwidth Flash and Processing-Near-Memory as solutions |
| **CTR Prediction** | Simpler architectures (MLP-based) achieving SOTA; generative approaches for long-term interest modeling; deployed at scale (Meituan) |
| **Recommendation** | Unified Transformers (OneTrans) for feature interaction + sequence modeling; personalized token compression for efficiency; LLM alignment for ranking |
| **Advertising** | Diffusion models and Decision Transformers for auto-bidding; cross-channel budget optimization; large-scale deployment on Taobao and Meituan |
| **Sequential Modeling** | Personalized token compression (PerSRec); cross-scale LLM-recommender collaboration; transition-aware graph attention |
| **AI Games** | Game-theory + RL hybrids; believability over optimality as the hard problem; benchmarks for AI game generation |
| **Reasoning/Agents** | Zero-RL for math reasoning from scratch; agentic CoT steering with RL; safety threshold harmonization across frontier companies |

---

*Report generated on 2026-07-21 by arXiv search across cs.AI, cs.IR, cs.LG, cs.CL topics.*
