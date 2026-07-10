---
title: "arXiv Daily: AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games"
type: synthesis
created: 2026-07-10
updated: 2026-07-10
tags: [arxiv, daily, ai, llm, recommendation, advertising, sequential-modeling, ctr, games]
---

# arXiv Daily: 2026-07-10

## Recent Papers in AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, and Games

---

### 1. LLaTTE: Scaling Laws for Multi-Stage Sequence Modeling in Large-Scale Ads Recommendation

- **Authors**: Lee Xiong, Zhirong Chen, Rahul Mayuranath, et al.
- **Institution/Company**: Meta
- **Date**: 2026-01-27
- **Abstract**: We present LLaTTE (LLM-Style Latent Transformers for Temporal Events), a scalable transformer architecture for production ads recommendation. Through systematic experiments, we demonstrate that sequence modeling in recommendation systems follows predictable power-law scaling similar to LLMs. Crucially, we find that semantic features bend the scaling curve: they are a prerequisite for scaling, enabling the model to effectively utilize the capacity of deeper and longer architectures. To realize the benefits of continued scaling under strict latency constraints, we introduce a two-stage architecture that offloads the heavy computation of large, long-context models to an asynchronous upstream user model.
- **Key Innovations**:
  - Demonstrates predictable power-law scaling in recommendation systems
  - Semantic features as prerequisite for effective scaling
  - Two-stage architecture for production latency constraints
  - 4.3% conversion uplift on Facebook Feed and Reels
- **Link**: https://arxiv.org/abs/2601.20083
- **Tags**: scaling-laws, sequential-modeling, ads-recommendation, meta

---

### 2. GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm

- **Authors**: Chuyue Xie, Rong Cheng, Zhiqiang Cao, Zehao Ju, et al.
- **Institution/Company**: Baidu
- **Date**: 2026-02-02
- **Abstract**: Traditional Deep Learning Recommendation Models (DLRMs) face increasing bottlenecks in performance and efficiency. Inspired by the scaling success of Large Language Models (LLMs), we propose Generative Ranking for Ads at Baidu (GRAB), an end-to-end generative framework for Click-Through Rate (CTR) prediction. GRAB integrates a novel Causal Action-aware Multi-channel Attention (CamA) mechanism to effectively capture temporal dynamics and specific action signals within user behavior sequences.
- **Key Innovations**:
  - Generative framework for CTR prediction
  - Causal Action-aware Multi-channel Attention (CamA) mechanism
  - 3.05% revenue increase and 3.49% CTR rise
  - Monotonic scaling with longer sequences
- **Link**: https://arxiv.org/abs/2602.01865
- **Tags**: ctr-prediction, generative-recommendation, baidu, sequence-modeling

---

### 3. CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer

- **Authors**: David Pardoe, Neil Daftary, et al.
- **Institution/Company**: LinkedIn
- **Date**: 2026-02-11
- **Abstract**: Click-through rate (CTR) prediction is fundamental to online advertising systems. We present CADET (Context-Conditioned Ads Decoder-Only Transformer), an end-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Our approach introduces several key innovations: a context-conditioned decoding architecture with multi-tower prediction heads, a self-gated attention mechanism, timestamp-based RoPE, session masking strategies, and production engineering techniques.
- **Key Innovations**:
  - Context-conditioned decoding with multi-tower prediction heads
  - Self-gated attention mechanism
  - Timestamp-based Rotary Position Embedding (RoPE)
  - Session masking for train-serve skew
  - 11.04% CTR lift compared to LiRank baseline
- **Link**: https://arxiv.org/abs/2602.11410
- **Tags**: ctr-prediction, transformer, advertising, linkedin, decoder-only

---

### 4. LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks

- **Authors**: Luyi Ma, Wanjia Sherry Zhang, Zezhong Fan, et al.
- **Institution/Company**: Amazon
- **Date**: 2026-04-13
- **Abstract**: On online advertising platforms, newly introduced promotional ads face the cold-start problem. We propose LLM-HYPER, a novel framework that treats large language models (LLMs) as hypernetworks to directly generate the parameters of the click-through rate (CTR) estimator in a training-free manner.
- **Key Innovations**:
  - LLMs as hypernetworks for CTR estimator parameter generation
  - Few-shot Chain-of-Thought prompting over multimodal ad content
  - Normalization and calibration techniques for production-ready CTR distributions
  - 55.9% improvement in NDCG@10 over cold-start baselines
- **Link**: https://arxiv.org/abs/2604.12096
- **Tags**: cold-start, llm, ctr-prediction, advertising, hypernetwork

---

### 5. Dual-Stream MLP is All You Need for CTR Prediction

- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution/Company**: Renmin University of China
- **Date**: 2026-06-03
- **Abstract**: Click-through rate (CTR) prediction holds a pivotal role in online advertising and recommendation systems. We propose Dual-Stream MLP (DS-MLP), a novel feature interaction framework for the CTR prediction task. It leverages knowledge distillation to consolidate the capacity of learning explicit feature interaction into a main MLP network, while a parallel MLP simultaneously captures implicit feature interactions as a complement.
- **Key Innovations**:
  - Dual-stream MLP architecture for feature interactions
  - Knowledge distillation for explicit interaction learning
  - Two alignment strategies for dual-stream optimization
  - State-of-the-art performance with vanilla MLP structure
- **Link**: https://arxiv.org/abs/2606.04944
- **Tags**: ctr-prediction, mlp, feature-interaction, knowledge-distillation

---

### 6. IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs

- **Authors**: Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan, et al.
- **Institution/Company**: Xiaohongshu (Little Red Book)
- **Date**: 2026-03-02
- **Abstract**: Click-through rate (CTR) models in advertising and recommendation systems rely heavily on item ID embeddings, which struggle in item cold-start settings. We present IDProxy, a solution that leverages multimodal large language models (MLLMs) to generate proxy embeddings from rich content signals, enabling effective CTR prediction for new items without usage data.
- **Key Innovations**:
  - Multimodal LLMs for generating proxy embeddings
  - Explicit alignment with existing ID embedding space
  - End-to-end optimization under CTR objectives
  - Deployed serving hundreds of millions of users at Xiaohongshu
- **Link**: https://arxiv.org/abs/2603.01590
- **Tags**: cold-start, multimodal-llm, ctr-prediction, xiaohongshu

---

### 7. RELATE: A Reinforcement Learning-Enhanced LLM Framework for Advertising Text Generation

- **Authors**: Jinfang Wang, Jiajie Liu, Jianwei Wu, et al.
- **Institution/Company**: Baidu
- **Date**: 2026-02-12
- **Abstract**: In online advertising, advertising text plays a critical role in attracting user engagement. We propose RELATE, a reinforcement learning-based end-to-end framework that unifies generation and objective alignment within a single model. Instead of decoupling text generation from downstream metric alignment, RELATE integrates performance and compliance objectives directly into the generation process via policy learning.
- **Key Innovations**:
  - End-to-end RL-based framework for ad text generation
  - Unified generation and objective alignment
  - Policy learning for performance and compliance
- **Link**: https://arxiv.org/abs/2602.11780
- **Tags**: advertising, llm, reinforcement-learning, text-generation

---

### 8. Learning to Recommend in Unknown Games

- **Authors**: Arwa Alanqary, Zakaria Baba, Manxi Wu, Alexandre M. Bayen
- **Institution/Company**: University of California, Berkeley
- **Date**: 2026-02-19
- **Abstract**: We study preference learning through recommendations in multi-agent game settings, where a moderator repeatedly interacts with agents whose utility functions are unknown. We consider two canonical behavioral feedback models—best response and quantal response—and study how the information revealed by each model affects the learnability of agents' utilities.
- **Key Innovations**:
  - Theoretical foundation for AI recommendation in strategic multi-agent environments
  - Logarithmic sample complexity under quantal-response feedback
  - Online algorithm with low regret under both feedback models
  - Geometric characterization of learnable utility sets
- **Link**: https://arxiv.org/abs/2602.16998
- **Tags**: game-theory, recommendation, multi-agent, strategic-interaction

---

### 9. Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents

- **Authors**: Haochen Wang, Yi Wu, Daryl Chang, Li Wei, Lukasz Heldt
- **Institution/Company**: Google/YouTube
- **Date**: 2026-02-10
- **Abstract**: Optimizing large-scale machine learning systems requires navigating a massive hyperparameter search space. We propose a self-evolving system that leverages Large Language Models (LLMs), specifically those from Google's Gemini family, to autonomously generate, train, and deploy high-performing, complex model changes within an end-to-end automated workflow.
- **Key Innovations**:
  - LLM-driven autonomous model optimization
  - Offline Agent (Inner Loop) for high-throughput hypothesis generation
  - Online Agent (Outer Loop) for production validation
  - Successful production launches at YouTube
- **Link**: https://arxiv.org/abs/2602.10226
- **Tags**: llm-agents, recommendation, autonomous-optimization, youtube

---

### 10. Augmenting Game AI with Deep Reinforcement Learning

- **Authors**: Alessandro Sestini, et al.
- **Institution/Company**: Conference on Games 2026
- **Date**: 2026-06-18
- **Abstract**: Immersion in video games depends not only on graphics, audio, and game mechanics, but also on the quality of in-game characters. Producing believable characters, or game AI, remains a significant challenge. The introduction of machine learning models opens the door to creating more believable, authentic, and relatable characters in games.
- **Key Innovations**:
  - Framework for training RL models for game AI
  - Genre-level readiness framework for game studios
  - Identification of bottlenecks: sample efficiency, generalization, believability vs optimality
  - Survey of production deployment examples
- **Link**: https://arxiv.org/abs/2606.20210
- **Tags**: game-ai, reinforcement-learning, believable-agents, survey

---

### 11. Efficient Sequential Recommendation for Long Term User Interest Via Personalization

- **Authors**: Xiaoying Wang, Christopher E. Lambert, Ren Chen, et al.
- **Institution/Company**: Meta
- **Date**: 2026-01-07
- **Abstract**: We introduced a novel approach to sequential recommendation that leverages personalization techniques to enhance efficiency and performance. Our method compresses long user interaction histories into learnable tokens, which are then combined with recent interactions to generate recommendations.
- **Key Innovations**:
  - Compression of long interaction histories into learnable tokens
  - Personalization for computational efficiency
  - Compatible with existing transformer-based models (HSTU, HLLM)
  - Significant reduction in computational costs
- **Link**: https://arxiv.org/abs/2601.03479
- **Tags**: sequential-recommendation, efficiency, personalization, transformer

---

## Summary of Trends

1. **Scaling Laws for Recommendation**: LLaTTE and GRAB demonstrate that LLM-style scaling laws apply to recommendation systems, with predictable power-law improvements.

2. **Generative CTR Models**: CADET, GRAB, and LLM-HYPER show a shift toward generative/decoder-only architectures for CTR prediction, achieving significant gains.

3. **LLM Integration**: Multiple papers (LLM-HYPER, IDProxy, RELATE, Self-Evolving) leverage LLMs for recommendation tasks, from parameter generation to ad text creation.

4. **Cold-Start Solutions**: IDProxy and LLM-HYPER address the critical cold-start problem using multimodal LLMs and hypernetworks.

5. **Game Theory meets Recommendation**: Learning to Recommend in Unknown Games bridges game theory and recommendation systems.

6. **Production Deployments**: Several papers report successful production deployments (Meta, Baidu, LinkedIn, Xiaohongshu, YouTube), validating practical impact.

7. **Efficiency Focus**: Dual-Stream MLP and Efficient Sequential Recommendation prioritize computational efficiency while maintaining performance.
