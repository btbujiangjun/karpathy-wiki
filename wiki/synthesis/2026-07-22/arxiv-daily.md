# arXiv Daily Research Report - 2026-07-22

## Executive Summary

Today's report covers recent papers across AI, LLMs, recommendation systems, advertising, sequential modeling, CTR prediction, and games. Key themes include:
- **LLM Optimization**: New methods for model merging, reasoning control, and inference efficiency
- **Recommendation Systems**: Advanced sequential modeling and multi-sequence learning approaches
- **CTR Prediction**: Scalable architectures with improved efficiency and performance
- **AI-Native Games**: Comprehensive survey defining the field and future roadmap

---

## 1. Large Language Models

### 1.1 Rethinking Heterogeneous LLM Merging: A Weighted Model Averaging Perspective
- **Authors**: Jiahe Fan, Yinghao Hou, Si Chen, Aiyuan Zhang, Hong Xie, Defu Lian
- **Institution**: Not specified in abstract
- **Date**: 20 Jul 2026
- **Abstract**: Explores whether LLMs with substantially different parameter spaces can be merged via direct weighted averaging without training or semantic alignment. The paper introduces training-free dimensional adaptation with ratio-controlled interpolation, testing on Qwen-family models across mathematical reasoning, code generation, language understanding, and commonsense reasoning benchmarks.
- **Key Innovations**:
  - Union-style merging (expanding smaller model into larger parameter space)
  - Intersection-style merging (truncating larger model into smaller space)
  - Demonstrates simple parameter averaging can be a strong baseline for heterogeneous LLM merging
- **arXiv Link**: https://arxiv.org/abs/2607.18026

### 1.2 Can We Break LLMs Out of Self-Loops? Fine-Grained Reasoning Control with Activation Steering
- **Authors**: Sheldon Yu, Tong Yu, Xunyi Jiang, Rohan Surana, Gagan Mundada, Sungchul Kim, Lina Yao, Julian McAuley, Junda Wu
- **Institution**: Not specified in abstract
- **Date**: 20 Jul 2026
- **Abstract**: Addresses the problem of LLM reasoning getting stuck in self-loops, exhausting token budgets without progress. Proposes SOPHIA (Steering Of reasoning Processes via Hidden-state Intervention and Activations) that treats reasoning traces as sequences of latent states and enables inference-time interventions for fine-grained control.
- **Key Innovations**:
  - Latent state classification of reasoning prefixes
  - Steering vector bank indexed by state pairs
  - Online self-loop detection from transition structure
  - Improves end task accuracy and token efficiency
- **arXiv Link**: https://arxiv.org/abs/2607.18100

### 1.3 Causal-Audit: Explicit and Auditable Graph-based Reasoning via Target-Aware Causal Chain Construction
- **Authors**: Su Lan, Xuefei Yin, Yanming Zhu, Alan Wee-Chung Liew
- **Institution**: Not specified in abstract
- **Date**: 22 Apr 2026 (Accepted at ACL 2026)
- **Abstract**: Proposes an explicit and auditable causal reasoning framework for context-free intervention-based QA. Formulates causal inference as structured reasoning over explicit causal graphs through four modular stages rather than implicit end-to-end prediction.
- **Key Innovations**:
  - Target-aware causal graph construction strategy
  - Path-level causal evidence aggregation mechanism
  - Modeling both reinforcing and counteracting effects
  - Consistently outperforms existing LLM-based methods on three benchmarks
- **arXiv Link**: https://arxiv.org/abs/2607.15281

---

## 2. Recommendation Systems

### 2.1 POEM: Partial-Order Enhanced Real-Time Sequential Modeling for Recommendation
- **Authors**: Linxiao Che, Yijia Sun, Siyuan Lou, Shanshan Huang, Qiang Luo, Ruiming Tang, Han Li, Kun Gai
- **Institution**: Kuaishou (implied from deployment)
- **Date**: 29 Jun 2026
- **Abstract**: Addresses dynamic drift of user interests in real-time recommendation systems. Proposes POEM framework built upon intrinsic partial-order relations from recommendation cascade, using real-time multi-task ranking scores to construct dynamic partial-order sequences.
- **Key Innovations**:
  - Partial-order guided sequence construction paradigm
  - Multi-objective score fusion module with normalized rank-aware weighting
  - Hierarchical sample learning strategy with hard negatives
  - Deployed on Kuaishou with significant online gains (0.249% watch time lift)
- **arXiv Link**: https://arxiv.org/abs/2606.29946

### 2.2 CMSL: Constructive Multi-Sequence Learning for Recommendation Systems
- **Authors**: Zikun Cui, Renzhi Wu, Junjie Yang, Li Sheng, Jijie Wei, Linfeng Liu, Tai Guo, Tao Jia, Xiaodong Wang, Hong Li, Li Yu, Sri Reddy, Hong Yan
- **Institution**: Meta
- **Date**: 26 Jun 2026
- **Abstract**: Observes that user history is inherently multi-faceted unlike linear text, leading to context pollution in single-sequence modeling. Proposes Constructive Multi-Sequence Learning that actively constructs multiple coherent sequences in latent space rather than passive sequence ingestion.
- **Key Innovations**:
  - Learnable Sequence Construction Module for disentangling user history
  - Linear attention mechanism for efficient scaling
  - Deployed across ranking and retrieval tasks at Meta
  - Addresses the fundamental divergence between natural language and recommendation data
- **arXiv Link**: https://arxiv.org/abs/2606.28533

---

## 3. Advertising & CTR Prediction

### 3.1 Long-History User Transformers for Real-Time Ad Ranking
- **Authors**: Viacheslav Ovchinnikov, Georgii Smirnov, Nikolai Savushkin, Veronika Ivanova, Maksim Kuzin
- **Institution**: Yandex
- **Date**: 15 Jul 2026
- **Abstract**: Resolves the conflict between using long interaction histories for CTR prediction and hard serving constraints in online advertising. Decouples history encoding from real-time inference using high-capacity offline transformer and lightweight runtime model.
- **Key Innovations**:
  - Offline autoregressive pre-training on large-scale interaction logs
  - Dual objective: feedback prediction + next-item prediction
  - Recover 72-80% quality of full-history runtime transformer
  - Production A/B experiments: +2.77% search ad ranking, +2.1% Yandex Ad Network
- **arXiv Link**: https://arxiv.org/abs/2607.14331

### 3.2 CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors**: David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, Liuqing Li, Tao Song, Lars Hertel, Young Jin Yun, Senthil Radhakrishnan, Zhiwei Wang, Tommy Li, Khai Tran, Ananth Nagarajan, Ali Naqvi, Yue Zhang, Renpeng Fang, Avi Romascanu, Arjun Kulothungun, Deepak Kumar, Praneeth Boda, Fedor Borisyuk, Ruoyan Wang
- **Institution**: LinkedIn
- **Date**: 11 Feb 2026
- **Abstract**: Presents an end-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Addresses unique challenges including post-scoring contextual signals, offline-online consistency, and industrial-scale workloads.
- **Key Innovations**:
  - Context-conditioned decoding with multi-tower prediction heads
  - Self-gated attention mechanism for training stability
  - Timestamp-based RoPE capturing temporal relationships across scales
  - Session masking strategies preventing train-serve skew
  - 11.04% CTR lift in online A/B testing vs production baseline
- **arXiv Link**: https://arxiv.org/abs/2602.11410

### 3.3 DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction
- **Authors**: Wenzhuo Cheng, Shipeng Nie, Qixin Guo, Xuefeng Sun, Jianguo Lou, Zhengwei Zheng
- **Institution**: Not specified in abstract
- **Date**: 6 Jun 2026
- **Abstract**: Addresses bottlenecks in transformer-based CTR models at residual connections. Proposes DeRes with dual-path routing through Identity residual path and Block Attention Residual path for high-order recall.
- **Key Innovations**:
  - Dual-path design with Identity and Block Attention paths
  - Pointwise AttnRes replacing Softmax with SiLU for better CTR modeling
  - Steeper compute-AUC scaling law (1.66x gap vs OneTrans)
  - 8-layer DeRes matches 16-layer OneTrans (~2x compute saving)
- **arXiv Link**: https://arxiv.org/abs/2606.07980

---

## 4. Sequential Modeling

### 4.1 OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer
- **Authors**: Zhaoqi Zhang, Haolei Pei, Jun Guo, Tianyu Wang, Yufei Feng, Hui Sun, Shaowei Liu, Aixin Sun
- **Institution**: Nanyang Technological University, ByteDance
- **Date**: 2026 (Accepted at WWW 2026)
- **Abstract**: Addresses the separation between feature interaction modules and user-behavior sequence modules in industrial recommendation systems. Unifies both with a single Transformer backbone using mixed parameterization.
- **Key Innovations**:
  - Unified tokenizer for both sequential and non-sequential attributes
  - Mixed parameterization: sequential tokens share parameters, non-sequential use token-specific
  - Cross-request KV caching for reduced training/inference cost
  - 5.68% lift in per-user GMV in online A/B testing
- **arXiv Link**: https://arxiv.org/abs/2510.26104v3

### 4.2 Multi-Behavior Sequential Modeling with Transition-Aware Graph Attention Network
- **Authors**: Gaoming Yang, Jian Wu, Yuning Jiang, Bo Zheng
- **Institution**: Alibaba (implied from WWW2026 acceptance)
- **Date**: 21 Jan 2026 (Accepted at WWW 2026)
- **Abstract**: Addresses high computational costs of transformer-based multi-behavior sequential modeling. Proposes Transition-Aware Graph Attention Network (TGA) with linear complexity for modeling multi-behavior transitions.
- **Key Innovations**:
  - Structured sparse graph construction from three perspectives: item-level, category-level, neighbor-level transitions
  - Transition-aware graph attention mechanism
  - Linear complexity vs polynomial for transformers
  - Deployed in large-scale industrial production
- **arXiv Link**: https://arxiv.org/abs/2601.14955

---

## 5. Games

### 5.1 AI Native Games: A Survey and Roadmap
- **Authors**: Zhiyue Xu, Fandi Meng, Kaijie Xu, Clark Verbrugge, Simon Lucas, Jian Zhao
- **Institution**: Not specified in abstract
- **Date**: 1 Jul 2026
- **Abstract**: Defines AI-native games by whether runtime generative AI is constitutive of the core loop—if the AI component were removed, the central form of play would collapse. Analyzes 53 publicly available AI-native games using a dual-axis G/N taxonomy.
- **Key Innovations**:
  - Counterfactual criterion separating AI-native from AI-augmented games
  - Dual-axis G/N taxonomy (game type vs AI mechanic)
  - Focus on mechanical invariants for stable gameplay with open-ended AI
  - Roadmap covering controllable generation, AI-as-mechanic design, multimodal systems
- **arXiv Link**: https://arxiv.org/abs/2607.00527

### 5.2 A Contextual-Bandit Oversight Game with Two-Sided Informational Asymmetry
- **Authors**: Yunjin Tong
- **Institution**: Not specified in abstract
- **Date**: 30 Jun 2026
- **Abstract**: Studies runtime human oversight of AI agents when private information runs in both directions—human knows reward function, AI knows action quality. Introduces a contextual-bandit team game with play/ask/trust/oversee interface.
- **Key Innovations**:
  - Two-sided asymmetric information framework
  - Exact one-shot characterizations in bandit setting
  - Analysis of avoidable harm gap from non-credible oversight communication
  - Dynamic resolution through passive learning and active signaling
- **arXiv Link**: https://arxiv.org/abs/2607.00155

---

## 6. Cross-Cutting Themes

### 6.1 Efficiency & Scalability
- **Model Merging**: Simple parameter averaging as baseline for heterogeneous LLM merging
- **CTR Prediction**: DeRes achieves 2x compute savings with equivalent AUC
- **Sequential Modeling**: Linear complexity alternatives to polynomial-time transformers

### 6.2 Real-World Deployment
- **POEM**: 0.249% watch time lift at Kuaishou
- **CMSL**: Deployed across ranking/retrieval at Meta
- **CADET**: 11.04% CTR lift at LinkedIn
- **OneTrans**: 5.68% GMV lift at ByteDance
- **Long-History Transformers**: +2.77% search ad ranking at Yandex

### 6.3 Novel Architectures
- **Dual-path designs** for residual connections
- **Multi-sequence learning** for disentangled user modeling
- **Context-conditioned decoding** for ad CTR prediction
- **Activation steering** for LLM reasoning control

---

*Report generated on 2026-07-22 from arXiv submissions*