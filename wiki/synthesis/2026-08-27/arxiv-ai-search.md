---
title: "arXiv AI/LLM/RecSys/CTR/Games Paper Search Report"
type: synthesis
created: 2026-08-27
updated: 2026-08-27
sources: []
tags: [arxiv, AI, LLM, recommendation, CTR, advertising, sequential-modeling, games, reinforcement-learning]
---

# arXiv AI Research Paper Search Report — 2026-08-27

Search scope: AI, LLMs, Recommendation Systems, Advertising, CTR Prediction, Sequential Modeling, Games.

---

## 1. Large Language Models (LLM)

### 1.1 Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | NVIDIA (544+ authors) |
| **Institution** | NVIDIA |
| **Date** | 2026-04-14 |
| **arXiv** | [2604.12374](https://arxiv.org/abs/2604.12374) |

**Abstract:** Describes pre-training, post-training, and quantization of Nemotron 3 Super, a 120B (active 12B) parameter hybrid Mamba-Attention MoE model. First Nemotron 3 model pre-trained in NVFP4, leveraging LatentMoE architecture optimized for accuracy per FLOP and per parameter. Includes MTP layers for inference acceleration via native speculative decoding. Pre-trained on 25T tokens with SFT and RL post-training. Supports up to 1M context length, achieving 2.2x–7.5x higher inference throughput vs. comparable models.

**Key Innovations:**
- LatentMoE: new MoE architecture optimizing both accuracy/FLOP and accuracy/parameter
- Hybrid Mamba-Attention design alternating SSM and attention layers for long-context efficiency
- MTP layers enabling native speculative decoding for inference acceleration
- NVFP4 pre-training for efficient mixed-precision training at scale
- Open-sourced datasets and checkpoints on HuggingFace

---

### 1.2 Mamba-3: Improved Sequence Modeling using State Space Principles

| Field | Detail |
|-------|--------|
| **Authors** | Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu |
| **Institution** | Carnegie Mellon University |
| **Date** | 2026-03-16 |
| **Venue** | ICLR 2026 |
| **arXiv** | [2603.15569](https://arxiv.org/abs/2603.15569) |

**Abstract:** Introduces three methodological improvements inspired by SSM perspective: (1) more expressive recurrence from SSM discretization, (2) complex-valued state update for richer state tracking, (3) MIMO formulation for better performance without increasing decode latency. At 1.5B scale, achieves +1.8pp average downstream accuracy over Gated DeltaNet, with comparable perplexity to Mamba-2 using half the state size.

**Key Innovations:**
- Complex-valued state update rule enabling richer state tracking
- Multi-input multi-output (MIMO) formulation for latency-free performance gains
- Inference-first design philosophy prioritizing hardware efficiency
- Advances the performance-efficiency Pareto frontier for sub-quadratic models

---

### 1.3 From BERT to Frontier Agents: Eight Years of Language-Model Progress

| Field | Detail |
|-------|--------|
| **Authors** | Pranav Kumar Kaliaperumal |
| **Institution** | Independent |
| **Date** | 2026-08-13 |
| **arXiv** | [2608.13675](https://arxiv.org/abs/2608.13675) |

**Abstract:** Analyzes LLM evolution from 2018–2026, documenting ~6x/year improvement in real coding issue resolution since late 2024. Shows dramatic cost reduction (GPT-5.6 Luna at $1–6/M tokens matching flagship capabilities). Identifies trend of specialized models outperforming general-purpose ones (Claude Opus 5 for frontend, Claude Fable 5 for repo-level, GPT-5.6 Sol for terminal tasks). Includes confidence ranking tool correctly identifying 47/50 right answers in top-50 choices.

**Key Innovations:**
- Quantitative analysis of capability-cost curve collapse
- Evidence that task-targeted models now outperform general-purpose models
- Public confidence ranking tool for sorting tasks
- Comprehensive longitudinal study of 8 years of LLM progress

---

### 1.4 The Evolution of Mixture-of-Experts Architectures in Large Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Jiguo Li |
| **Institution** | Independent |
| **Date** | 2026-08-09 |
| **arXiv** | [2608.08650](https://arxiv.org/abs/2608.08650) |

**Abstract:** Technical survey organizing modern MoE systems along five coupled dimensions: expert granularity, topology, routing freedom, load balancing scope, and execution structure. Describes eight architectural milestones as a dependency graph. Analyzes systems through four control planes: Expert Topology, Routing, Balance, and Expert Parallelism. Main trend: shift from merely activating more sparse parameters toward decoupling semantic routing, computational budgets, and physical execution.

**Key Innovations:**
- Four-plane control framework (Topology, Routing, Balance, Parallelism) for MoE analysis
- Dependency graph of eight MoE architectural milestones
- Equal-budget pretraining experiments comparing MoE variants
- Identifies decoupling of semantic routing from physical execution as key trend

---

### 1.5 Federated Prompt Learning: A Unified Framework

| Field | Detail |
|-------|--------|
| **Authors** | Qinglin Yang, Chen Qiu, Hongyuan Zhang, Pengdeng Li, Yuan Liu, Zhihong Tian |
| **Institution** | Not specified |
| **Date** | 2026-08-14 |
| **arXiv** | [2608.13844](https://arxiv.org/abs/2608.13844) |

**Abstract:** Comprehensive survey of federated prompt learning (FPL) integrating FL and LLMs. Examines FPL across the full model lifecycle (pre-training, fine-tuning, applications) while discussing security, privacy, and robustness. Addresses three RQs: motivations/characteristics, performance/efficiency trade-offs, and remaining security/privacy challenges.

**Key Innovations:**
- Systematic categorization of FPL methods across model lifecycle
- Comparative analysis of performance, communication, and scalability trade-offs
- Taxonomy of security/privacy defense mechanisms for federated LLM training

---

## 2. Recommendation Systems

### 2.1 Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Haochen Wang, Yi Wu, Daryl Chang, Li Wei, Lukasz Heldt |
| **Institution** | Google (YouTube) |
| **Date** | 2026-02-10 |
| **Venue** | RecSys 2026 |
| **arXiv** | [2602.10226](https://arxiv.org/abs/2602.10226) |

**Abstract:** Proposes a self-evolving system leveraging Google Gemini LLMs to autonomously generate, train, and deploy complex model changes in an end-to-end automated workflow. The system consists of an Offline Agent (Fast Loop) for high-throughput hypothesis generation optimizing proxy metrics, and an Online Agent (Slow Loop) validating against delayed north star business metrics in live production. Agents act as specialized ML Engineers with deep reasoning capabilities, discovering novel improvements in optimization algorithms, architecture, and reward functions targeting long-term engagement. Multiple successful production launches at YouTube.

**Key Innovations:**
- LLM agents as autonomous ML Engineers for recommendation model optimization
- Dual-loop architecture: Offline (fast, proxy metrics) + Online (slow, business metrics)
- LLM-driven discovery of novel optimization algorithms and reward functions
- End-to-end automated workflow from hypothesis generation to production deployment
- Demonstrated at YouTube scale with production launches

---

### 2.2 Generative Chain of Behavior for User Trajectory Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Chengkai Huang, Xiaodi Chen, Hongtao Huang, Quan Z. Sheng, Lina Yao |
| **Institution** | University of New South Wales / Macquarie University |
| **Date** | 2026-01-26 |
| **arXiv** | [2601.18213](https://arxiv.org/abs/2601.18213) |

**Abstract:** Proposes Generative Chain of Behavior (GCB), a generative framework modeling user interactions as an autoregressive chain of semantic behaviors over multiple future steps. Encodes items into semantic IDs via RQ-VAE with k-means refinement, forming a discrete latent space preserving semantic proximity. Transformer-based autoregressive generator predicts multi-step future behaviors, capturing long-horizon intent transitions. Outperforms state-of-the-art sequential recommenders in multi-step accuracy and trajectory consistency.

**Key Innovations:**
- Multi-step trajectory prediction (beyond next-item prediction)
- RQ-VAE with k-means refinement for semantic ID encoding
- Unified generative formulation for capturing preference evolution
- Autoregressive chain-of-behavior paradigm

---

### 2.3 Auditing Return Conditioning as a Control Knob for Decision Transformer Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Jingyu Wang |
| **Institution** | Not specified |
| **Date** | 2026-08-25 |
| **Venue** | CONSEQUENCES '26 (RecSys 2026 workshop) |
| **arXiv** | [2608.24815](https://arxiv.org/abs/2608.24815) |

**Abstract:** Proposes four diagnostic checks for offline return-to-go (RTG) conditioning in Decision Transformer recommenders: intervention locality, no-RTG baseline, reward check, and RTG-content ablation. On MovieLens-25M, K=20 RTG intervention shifts Crime genre predictions by +23.61pp, while current-slot-only shifts by +1.77pp. Shuffled RTG largely removes response. Cross-diagnostic pattern reveals controllability properties.

**Key Innovations:**
- RTG locality ladder for auditing controllability of Decision Transformer recommenders
- Four-check diagnostic framework for offline return conditioning
- Evidence that dataset and genre selection matter for reward control
- Practical methodology for evaluating recommendation controllability

---

### 2.4 Efficient Sequential Recommendation for Long Term User Interest Via Personalization

| Field | Detail |
|-------|--------|
| **Authors** | (from collaborative list) |
| **Institution** | Not specified |
| **Date** | 2026-01 |
| **arXiv** | [2601.03479](https://arxiv.org/abs/2601.03479) |

**Abstract:** Addresses computational inefficiency of scaling sequence length in sequential recommenders. Proposes compressing user interaction histories (UIH) via personalized experts, demonstrating that performance (e.g., Recall@5) steadily improves with longer sequences from 128 to 2000. Personalized compression enables efficient scaling without the quadratic cost of standard transformers.

**Key Innovations:**
- Personalized expert-based compression for long user histories
- Demonstrates steady performance gains scaling from 128 to 2000-length sequences
- Practical approach to long-context recommendation without quadratic cost

---

## 3. CTR Prediction & Advertising

### 3.1 CTR-Sink: Attention Sink for Language Models in Click-Through Rate Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Zixuan Li, Binzong Geng, Jing Xiong, Yong He, et al. |
| **Institution** | Chinese Academy of Sciences (NLPR) / Ant Group |
| **Date** | 2025-08-05 (revised 2026-08-02) |
| **Venue** | KDD 2026 |
| **arXiv** | [2508.03668](https://arxiv.org/abs/2508.03668) |

**Abstract:** Addresses the structural gap between user behavior sequences (discrete actions with semantically empty separators) and coherent natural language. Proposes behavior-level attention sinks inserting sink tokens between behaviors incorporating temporal distance signals. Two-stage training guides LM attention to sink tokens, plus attention sink mechanism amplifying inter-sink dependencies. Validated on industrial dataset, MovieLens, and Kuairec. +0.42% improvement on Kuairec with RoBERTa backbone.

**Key Innovations:**
- Behavior-level attention sinks for recommendation domain adaptation
- Sink tokens carrying recommendation-specific signals (temporal distance)
- Two-stage training strategy for attention guidance
- Attention sink mechanism amplifying inter-sink dependencies
- Visualization confirming attention aggregation on sink tokens

---

### 3.2 EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling

| Field | Detail |
|-------|--------|
| **Authors** | Mingyang Liu, Yong Bai, Zhangming Chan, Sishuo Chen, Xiang-Rong Sheng, Han Zhu, Jian Xu, Xinyang Chen |
| **Institution** | Taobao & Tmall Group, Alibaba |
| **Date** | 2026-02-11 |
| **arXiv** | [2602.10811](https://arxiv.org/abs/2602.10811) |

**Abstract:** Proposes Efficiently Scalable Transformer (EST) for fully unified CTR modeling without lossy aggregation. Identifies two critical properties distinguishing CTR from LLMs: information density asymmetry and modality-specific priors. Integrates Lightweight Cross-Attention (LCA) for pruning redundant self-interactions and Content Sparse Attention (CSA) for dynamic behavior selection. Exhibits stable power-law scaling. Deployed on Taobao: +3.27% RPM, +1.22% CTR lift.

**Key Innovations:**
- Fully unified modeling eliminating information bottleneck from early aggregation
- Content Sparse Attention (CSA) using content similarity for dynamic behavior selection
- Demonstrated power-law scaling for industrial CTR prediction
- Production deployment on Taobao display advertising with significant business impact

---

### 3.3 ML-DCN: Masked Low-Rank Deep Crossing Network for Scalable Ads CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Jiacheng Li, Yixiong Meng, Yi Wu, Yun Zhao, Sharare Zehtabian, Jiayin Jin, Degao Peng, Jinfeng Zhuang, Qifei Shen, Kungang Li |
| **Institution** | Pinterest |
| **Date** | 2026-02-09 |
| **arXiv** | [2602.09194](https://arxiv.org/abs/2602.09194) |

**Abstract:** Studies scaling feature interaction modules under fixed serving budgets. Finds that naively scaling DCNv2 and MaskNet yields diminishing offline gains. Proposes ML-DCN integrating instance-conditioned masks into low-rank crossing layers, enabling per-example selection of salient interaction directions. Achieves higher AUC than DCNv2/MaskNet at matched FLOPs with stronger scaling. Online A/B tests show significant improvements in CTR and click-quality metrics, deployed in production with neutral serving cost. +1.89% relative CTR increase.

**Key Innovations:**
- Instance-conditioned mask for per-example interaction direction selection
- Low-rank crossing layer for efficient computation under budget constraints
- Combines strengths of DCNv2 and MaskNet while avoiding their scaling limitations
- Production-deployed at Pinterest ads ranking

---

## 4. Sequential User Behavior Modeling

### 4.1 Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Enhanced Sequential User Modeling

| Field | Detail |
|-------|--------|
| **Authors** | Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang |
| **Institution** | Not specified |
| **Date** | 2026-06-13 |
| **arXiv** | [2606.15252](https://arxiv.org/abs/2606.15252) |

**Abstract:** Challenges the practice of constructing behavior sequences exclusively from positive interactions. Demonstrates that mixed-polarity behavior sequences (interleaving positive and negative tokens within fixed length budget) consistently outperform positive-only sequences across diverse model architectures with negligible additional computational overhead. Proposes Target-Aware Polarity Fusion (TAPF), a lightweight target-conditioned gating mechanism. +1.9% to +9.6% relative AUC across five architectures on three benchmarks.

**Key Innovations:**
- Mixed-polarity behavior sequence paradigm (positive + negative interactions)
- Target-Aware Polarity Fusion (TAPF) for differentiating behavioral evidence
- Demonstrates that polarity bias baseline captures majority of improvement
- Consistent gains across five different architectures

---

### 4.2 PANTHER: Generative Pretraining Beyond Language for Sequential User Behavior Modeling

| Field | Detail |
|-------|--------|
| **Authors** | Guilin Li, Yun Zhang, Xiuyuan Chen, Chengqi Li, Bo Wang, Linghe Kong, Wenjia Wang, Weiran Huang, Matthias Hwai Yong Tan |
| **Institution** | WeChat Pay (Tencent) |
| **Date** | 2025-10-11 (revised 2026-03-30) |
| **arXiv** | [2510.10102](https://arxiv.org/abs/2510.10102) |

**Abstract:** Extends generative pretraining to user behavior, learning transferable representations from unlabeled behavioral data. Hybrid generative-discriminative framework unifying pretraining and downstream adaptation. Features: Structured Tokenization compressing multi-dimensional attributes into interpretable vocabulary; Sequence Pattern Recognition Module for periodic motifs; Unified User-Profile Embedding; Real-time scalability via offline caching. Deployed at WeChat Pay: +25.6% HitRate@1 for next-transaction prediction, +38.6% fraud detection recall.

**Key Innovations:**
- Generative pretraining paradigm applied to user behavior (analogous to LLM pretraining)
- Structured Tokenization for compressing multi-dimensional transaction attributes
- Sequence Pattern Recognition Module (SPRM) for periodic transaction motifs
- Production-deployed at WeChat Pay with millisecond-level inference
- Cross-domain generalization with up to +21% HitRate@1 over transformer baselines

---

## 5. Games & Reinforcement Learning

### 5.1 Augmenting Game AI with Deep Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén |
| **Institution** | Electronic Arts (EA), Stockholm |
| **Date** | 2026-06-18 |
| **Venue** | Conference on Games 2026 |
| **arXiv** | [2606.20210](https://arxiv.org/abs/2606.20210) |

**Abstract:** Vision paper on applying RL to game AI. Proposes a framework for training RL models suited to game AI and development, considering practical deployment constraints. Presents examples of RL-augmented game AI and describes practicalities of deploying player-facing ML agents in modern games. Identifies bottlenecks and hard problems, proposing research directions to accelerate ML adoption in game AI for the video game industry.

**Key Innovations:**
- Framework for training RL models with game-specific requirements
- Practical deployment guidance for player-facing ML agents in AAA games
- Identifies bottlenecks: sample efficiency, safety guarantees, integration with hand-coded systems
- Roadmap for ML adoption in commercial game production

---

### 5.2 A Survey of Large Models in Sports

| Field | Detail |
|-------|--------|
| **Authors** | Yichen Xu, Jianzhe Ma, Chuhan Wang, Zhonghao Cao, Liangyu Chen, Wenxuan Wang, Qin Jin |
| **Institution** | Renmin University of China |
| **Date** | 2026-08-14 |
| **Venue** | ACL 2026 Findings |
| **arXiv** | [2608.14377](https://arxiv.org/abs/2608.14377) |

**Abstract:** Comprehensive survey of large models in sports covering: overview of tasks and applications across participant groups, detailed analysis of sports-related datasets and benchmarks, and critical discussion of challenges and future directions. Establishes foundation for advancing research in large-model-driven sports intelligence.

**Key Innovations:**
- First comprehensive survey of (M)LLMs applied to sports
- Taxonomy of sports AI tasks across different participant groups
- Curated analysis of sports datasets and benchmarks
- Open-source GitHub repository maintained

---

## 6. Key Trends Observed

1. **LLM Agents for RecSys Optimization**: YouTube's self-evolving system demonstrates LLMs can autonomously optimize recommendation models, replacing manual iteration loops with autonomous ML Engineer agents.

2. **Hybrid Architectures (Mamba + Transformer)**: Nemotron 3 Super's hybrid design and Mamba-3 show that combining SSM and attention layers achieves superior efficiency for long-context tasks while maintaining quality.

3. **Scaling Laws in CTR Prediction**: EST (Alibaba/Taobao) and ML-DCN (Pinterest) both demonstrate that carefully designed feature interaction modules can achieve predictable scaling, similar to LLM scaling laws.

4. **Generative Paradigm for Sequential Modeling**: GCB, PANTHER, and the semantic tokenization trend (RankMixer/TokenMixer series) show the field converging on autoregressive generative approaches for recommendation.

5. **Attention Mechanisms Adapted for CTR**: CTR-Sink brings attention sink theory from LLMs to recommendation, showing that adapting LM mechanisms to domain-specific structure yields significant gains.

6. **Mixed-Polarity Sequences**: Beyond Positive Signals shows that negative user behaviors (skips, low engagement) carry significant signal, challenging the positive-only sequence convention.

7. **MoE Architecture Evolution**: From the MoE survey, the field is shifting from simple sparse activation toward decoupling semantic routing, computational budgets, and physical execution.

8. **RL for Game AI in Production**: EA's vision paper outlines practical challenges of deploying RL agents as game AI in AAA games, moving beyond benchmark performance to real-world game production constraints.
