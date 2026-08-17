---
title: "arXiv AI Research Search Report"
type: synthesis
created: 2026-08-17
updated: 2026-08-17
sources: []
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games]
---

# arXiv AI Research Search Report (2026-08-17)

> Auto-generated search across arXiv for recent papers in AI, LLMs, recommendation, advertising, sequential modeling, CTR prediction, and games.

---

## 1. Large Language Models (LLMs)

### 1.1 Numeracy in Large Language Models: Fundamental Limitations and Paths to Improvement
- **Authors**: Aoxin Ni
- **Institution/Company**: Not specified
- **Date**: Aug 13, 2026
- **arXiv**: [2608.13129](https://arxiv.org/abs/2608.13129)
- **Abstract**: Comprehensive survey of numerical limitations in LLMs. Proposes the Numerical Grounding Framework (NGF) to decompose numeracy into Representational Grounding (mapping numeral forms to value/magnitude) and Procedural Grounding (executing arithmetic operations). Evaluates frontier models across Number Cookbook, NumericBench, and GSM-Symbolic. Reviews architectural interventions including digit-aware tokenization and Abacus Embeddings.
- **Key Innovations**: Numerical Grounding Framework (NGF); systematic evaluation of frontier model families on atomic, contextual, and reasoning-assisted numeracy; mitigation strategy taxonomy covering tokenization, positional encoding, embedding geometry, and data distribution.

### 1.2 The Evolution of Mixture-of-Experts Architectures in LLMs
- **Authors**: Jiguo Li et al.
- **Institution/Company**: Not specified
- **Date**: Aug 9, 2026
- **arXiv**: [2608.08650](https://arxiv.org/abs/2608.08650)
- **Abstract**: Technical survey of MoE architectures organizing evolution into a dependency graph and a four-plane control framework (Topology, Routing, Balance, Parallelism). Identifies eight architectural milestones as six mainline and two orthogonal branches. Connects algorithmic choices (Top-k routing, shared experts, fine-grained experts, dynamic composition) with systems concerns (token dispatch, device placement, all-to-all communication).
- **Key Innovations**: Four-plane control framework for MoE analysis; dependency graph of MoE evolution; identification of the trend toward decoupling semantic routing from physical execution.

### 1.3 Memory for Large Language Models
- **Authors**: Sining Zhoubian, Dan Zhang, Evgeny Kharlamov, Jie Tang
- **Institution/Company**: Not specified (likely Tsinghua based on Jie Tang)
- **Date**: Jul 28, 2026
- **arXiv**: [2607.25380](https://arxiv.org/abs/2607.25380)
- **Abstract**: Systematic, architecture-centric taxonomy of memory mechanisms in LLMs. Characterizes memory along three axes: representation (implicit vs. explicit), update dynamics (offline vs. online), and persistence (short-term vs. long-term). Formalizes granular mechanisms for memory writing, routing, state transitions, and consolidation. Analyzes hybrid memory architectures and system-level efficiency trade-offs.
- **Key Innovations**: Unified taxonomy bridging implicit/explicit memory; formalization of memory state transitions and consolidation; critical analysis of hybrid architectures.

### 1.4 Understanding Large Language Models
- **Authors**: Yannik Keller, Thomas Eisenmann
- **Institution/Company**: Not specified
- **Date**: Jul 1, 2026
- **arXiv**: [2607.01006](https://arxiv.org/abs/2607.01006)
- **Abstract**: Survey covering LLM mechanisms, capabilities, and relationship to human cognition. Addresses pressing questions about how LLMs work and their relationship to human reasoning.
- **Key Innovations**: Comprehensive analysis bridging LLM mechanisms with cognitive science perspectives.

---

## 2. Recommendation Systems

### 2.1 Sona Technical Report
- **Authors**: Sona Team (Alexandr Udeneev, Aleksei Krasilnikov, Alexey Nadtochiy, et al., 34 authors total)
- **Institution/Company**: Yandex Music
- **Date**: Aug 11, 2026
- **arXiv**: [2608.11015](https://arxiv.org/abs/2608.11015)
- **Abstract**: Single-model generative recommender that replaced the entire production cascade (15+ candidate generators, pre-ranking and ranking models consuming hundreds of features) in an online A/B test. The encoder transforms user chronological engagement sequences into hidden states for both autoregressive decoder and Ranking Module. Uses next-token-prediction and distillation objectives jointly. Achieves +4.53% Active Users, +6.30% Total Listening Time, +11.42% Likes. The Active Users uplift was 2.35x the increment previously delivered by Argus.
- **Key Innovations**: Unified candidate generation and ranking around shared user representation; eliminates hand-engineered features entirely; proves a single jointly trained model can replace a mature multi-stage cascade.

### 2.2 GALLM: Graph-Aware Large Language Models for Sequential Recommendation
- **Authors**: Fenglin Yan, Bohao Wang, Jian Zhang, Yu Cui, Tongya Zheng, Ye Feng, Can Wang, Jiawei Chen
- **Institution/Company**: Not specified
- **Date**: Aug 12, 2026
- **arXiv**: [2608.12184](https://arxiv.org/abs/2608.12184)
- **Abstract**: Constructs a collaborative graph over text tokens and item tokens, modeling three relation types: Text-Text (semantic dependencies), Item-Text (aligning items with descriptions), and Item-Item (global co-occurrence patterns). Transforms relations into lightweight learnable attention biases in the LLM attention mechanism, enabling collaborative-aware token interactions without an additional graph encoder. Improves over strongest baseline by 9.76% on average in HR@5 across four benchmarks.
- **Key Innovations**: Graph-aware LLM with collaborative signal injection via attention biases; no additional graph encoder needed; three-relation modeling framework.

### 2.3 ATLAS: Learning to Recommend Across Unseen Domains
- **Authors**: Pervez Shaik, Prosenjit Biswas, Abhinav Thorat, Ravi Kolla, Niranjan Pedanekar
- **Institution/Company**: Not specified (likely Amazon/industry)
- **Date**: Aug 4, 2026
- **arXiv**: [2608.03899](https://arxiv.org/abs/2608.03899)
- **Abstract**: Multi-source recommendation domain generalization framework that learns shared, domain-invariant user-item representation from disjoint source domains for zero-shot recommendation on unseen domains. Combines Gromov-Wasserstein alignment, adversarial cross-domain item representation, and residual vector quantization (RVQ) codebooks. Trained on five Amazon domains, applied to ten unseen domains with 24% average relative HitRate gain over SOTA baselines including LLM-based methods.
- **Key Innovations**: Zero-shot cross-domain recommendation without target-domain adaptation; Gromov-Wasserstein alignment for user relation preservation; demonstrated source-domain diversity effect.

### 2.4 Deep Research for Recommender Systems
- **Authors**: Kesha Ou, Chenghao Wu, Xiaolei Wang, Bowen Zheng, Wayne Xin Zhao, Weitao Li, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution/Company**: Renmin University of China, Meituan
- **Date**: Mar 8, 2026
- **arXiv**: [2603.07605](https://arxiv.org/abs/2603.07605)
- **Abstract**: Proposes a deep research paradigm for recommendation that replaces item lists with comprehensive user-centric reports. Instantiated through RecPilot, a multi-agent framework with a user trajectory simulation agent and a self-evolving report generation agent. Reframes recommendation as proactive, agent-driven service.
- **Key Innovations**: Deep research paradigm for recommendation; RecPilot multi-agent framework; recommendation-as-report instead of recommendation-as-list.

---

## 3. CTR Prediction

### 3.1 GRAB: LLM-Inspired Sequence-First CTR Prediction (Baidu)
- **Authors**: Shaopeng Chen, Chuyue Xie, Huimin Ren, Shaozong Zhang, Han Zhang, Ruobing Cheng, Zhiqiang Cao, Zehao Ju, Yu Gao, Jie Ding, Xiaodong Chen, Xuewu Jiao, Shuanglong Li, Liu Lin
- **Institution/Company**: Baidu
- **Date**: Feb 2, 2026
- **arXiv**: [2602.01865](https://arxiv.org/abs/2602.01865)
- **Abstract**: End-to-end generative framework for CTR prediction inspired by LLM scaling. Integrates Causal Action-aware Multi-channel Attention (CamA) to capture temporal dynamics and action signals in user behavior sequences. Full-scale online deployment shows +3.05% revenue, +3.49% CTR. Demonstrates desirable scaling behavior with monotonic, approximately linear improvement as longer sequences are utilized.
- **Key Innovations**: Causal Action-aware Multi-channel Attention (CamA); LLM-inspired scaling for CTR; demonstrated scaling laws in production advertising.

### 3.2 EST: Efficient Scaling Laws in CTR Prediction (Alibaba/Taobao)
- **Authors**: Mingyang Liu, Yong Bai, Zhangming Chan, Sishuo Chen, Xiang-Rong Sheng, Han Zhu, Jian Xu, Xinyang Chen
- **Institution/Company**: Alibaba (Taobao)
- **Date**: Feb 11, 2026
- **arXiv**: [2602.10811](https://arxiv.org/abs/2602.10811)
- **Abstract**: Efficiently Scalable Transformer (EST) for unified CTR modeling without lossy aggregation. Integrates Lightweight Cross-Attention (LCA) for pruning redundant self-interactions and Content Sparse Attention (CSA) for dynamic high-signal behavior selection. Exhibits stable power-law scaling. Deployed on Taobao display advertising: +3.27% RPM, +1.22% CTR.
- **Key Innovations**: Fully unified modeling without early aggregation; LCA and CSA modules for efficient cross-feature attention; demonstrated power-law scaling in industrial CTR.

### 3.3 LoopCTR: Loop Scaling for CTR Prediction
- **Authors**: Jiakai Tang, Runfeng Zhang, Weiqiu Wang, Yifei Liu, Chuan Wang, Xu Chen, Yeqiu Yang, Jian Wu, Yuning Jiang, Bo Zheng
- **Institution/Company**: Not specified
- **Date**: Apr 21, 2026
- **arXiv**: [2604.19550](https://arxiv.org/abs/2604.19550)
- **Abstract**: Introduces loop scaling paradigm that increases training-time computation through recursive reuse of shared model layers, decoupling computation from parameter growth. Sandwich architecture with Hyper-Connected Residuals and MoE. Train-multi-loop, infer-zero-loop strategy where single forward pass outperforms all baselines. Reveals 0.02-0.04 AUC untapped headroom.
- **Key Innovations**: Loop scaling paradigm; decoupling computation from parameter growth; process supervision at every loop depth; adaptive inference frontier.

### 3.4 DS-MLP: Dual-Stream MLP for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution/Company**: Renmin University of China
- **Date**: Jun 3, 2026 (Accepted by TKDD)
- **arXiv**: [2606.04944](https://arxiv.org/abs/2606.04944)
- **Abstract**: Uses knowledge distillation to consolidate explicit feature interaction into a main MLP, with a parallel MLP capturing implicit interactions. Two alignment strategies optimize the dual-stream architecture. Achieves SOTA on three benchmarks with vanilla MLP structure.
- **Key Innovations**: Knowledge distillation for dual-stream CTR; achieving SOTA with vanilla MLP; dual alignment strategies for explicit/implicit balance.

### 3.5 GenCI: Generative User Interest Shift for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Hongyu Lu, Ji-Rong Wen
- **Institution/Company**: Renmin University of China
- **Date**: Jan 26, 2026 (Accepted by WWW 2026)
- **arXiv**: [2601.18251](https://arxiv.org/abs/2601.18251)
- **Abstract**: Generative user intent framework leveraging semantic interest cohorts for dynamic CTR prediction. A generative model with next-item prediction objective produces candidate interest cohorts as explicit, candidate-agnostic representations. A hierarchical candidate-aware network injects contextual signal via cross-attention.
- **Key Innovations**: Generative cohort-based intent modeling; addressing interest shift vs. interest matching; resolving pointwise ranking context chasm.

---

## 4. Advertising & AI

### 4.1 Generative AI Advertising as a Problem of Trustworthy Commercial Intervention
- **Authors**: Jingyi Qiu, Qiaozhu Mei
- **Institution/Company**: University of Michigan, School of Information
- **Date**: May 18, 2026
- **arXiv**: [2605.18673](https://arxiv.org/abs/2605.18673)
- **Abstract**: Argues generative AI fundamentally changes advertising from content placement to intervention on the generative process itself. Introduces taxonomy organized by influence tier: product mentions (Tier 1), information framing (Tier 2), behavioral redirection (Tier 3), long-term preference shaping (Tier 4). Analyzes across RAG and agentic pipelines. Documents advertising positions of ChatGPT, Microsoft Copilot, Perplexity, Meta AI, and Claude (ad-free).
- **Key Innovations**: Four-tier influence taxonomy for generative AI advertising; analysis of trustworthiness as attributable, measurable, contestable; comprehensive survey of deployed commercial positions in AI systems.

---

## 5. Sequential Modeling & Time Series

### 5.1 Cast-R1: Tool-Augmented Sequential Decision Policies for Time Series Forecasting
- **Authors**: Xiaoyu Tao, Mingyue Cheng, Chuang Jiang, Tian Gao, Huanjian Zhang, Yaguo Liu
- **Institution/Company**: Not specified (likely USTC based on authors)
- **Date**: Feb 14, 2026
- **arXiv**: [2602.13802](https://arxiv.org/abs/2602.13802)
- **Abstract**: Reformulates time series forecasting as sequential decision-making. Introduces memory-based state management for accumulating contextual evidence. Agent autonomously interacts with a modular toolkit (statistical feature extraction, lightweight forecasting models, reasoning-based prediction, iterative self-reflection). Trained with supervised fine-tuning + multi-turn RL + curriculum learning.
- **Key Innovations**: Agentic paradigm for time series; tool-augmented forecasting agent; memory-based state management; SFT + multi-turn RL training.

### 5.2 EnTransformer: Deep Generative Transformer for Multivariate Probabilistic Forecasting
- **Authors**: Not fully extracted
- **Date**: Mar 2026
- **arXiv**: [2603.11909](https://arxiv.org/abs/2603.11909)
- **Abstract**: Transformer-based framework for probabilistic forecasting using the engression principle (deep distributional regression with pre-additive noise). Produces probabilistic forecasts with model-intrinsic uncertainty quantification while remaining computationally lightweight.
- **Key Innovations**: Engression principle for probabilistic forecasting; minimal modifications to existing Transformer architectures; built-in uncertainty quantification.

---

## 6. Games & AI

### 6.1 Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslen
- **Institution/Company**: Electronic Arts (EA), Stockholm, Sweden
- **Date**: Jun 18, 2026 (Conference on Games 2026)
- **arXiv**: [2606.20210](https://arxiv.org/abs/2606.20210)
- **Abstract**: Vision paper on deploying RL for player-facing game AI. Proposes a framework for training RL models with game AI-specific requirements. Presents examples of games with RL-augmented AI (goalkeeping, tactical shooters), describes practicalities of deploying ML agents in modern games. Identifies bottlenecks: compute budgets, optimal vs. believable behavior tension, adaptation to diverse player styles.
- **Key Innovations**: Framework for game-specific RL training; analysis of production deployment challenges; identification of open research problems for industry adoption.

### 6.2 Game-RL: Synthesizing Multimodal Verifiable Game Data for VLM Reasoning
- **Authors**: Tong Jingqi, Tang Jixin, et al.
- **Institution/Company**: Multiple (ICLR 2026)
- **Date**: Accepted ICLR 2026
- **arXiv**: [2505.13886](https://arxiv.org/abs/2505.13886)
- **Abstract**: Synthesizes multimodal verifiable game data to boost VLMs' general reasoning. Uses game environments (Sokoban, mazes) as reasoning benchmarks. Widely adopted by Shanghai AI Lab, Peking University, Princeton, NUS, Alibaba.
- **Key Innovations**: Game environments as VLM reasoning benchmarks; verifiable game data synthesis; cross-institutional adoption.

---

## 7. Cross-Cutting Trends

### Key Themes Observed Across Papers:

1. **Generative paradigm shift in CTR/RecSys**: Multiple papers (GRAB, EST, Sona, GenCI) demonstrate that generative modeling (next-token prediction) is replacing traditional discriminative feature interaction approaches in CTR and recommendation.

2. **LLM-inspired scaling for non-NLP tasks**: CTR papers (GRAB, EST, LoopCTR) explicitly borrow scaling laws and architectural ideas from LLMs, with demonstrated power-law relationships in production.

3. **Single-model replacing multi-stage cascades**: Sona (Yandex) proves a single jointly trained model can replace 15+ candidate generators and ranking models.

4. **Agentic AI expanding beyond chat**: Cast-R1 (forecasting), RecPilot (recommendation), and Game-RL (reasoning) all deploy agentic workflows with tool use, memory, and self-reflection.

5. **Trustworthy AI advertising**: As LLMs become commercial interfaces, the advertising trust problem intensifies - the Michigan paper provides the first systematic framework.

6. **Zero-shot cross-domain generalization**: ATLAS demonstrates that domain-invariant representations can generalize to completely unseen recommendation domains.

7. **RL in games reaching production**: EA's vision paper signals that RL-augmented game AI is moving from research demos to player-facing deployment.

---

*Report generated on 2026-08-17 via arXiv web search across cs.AI, cs.CL, cs.IR, cs.LG, cs.CY categories.*
