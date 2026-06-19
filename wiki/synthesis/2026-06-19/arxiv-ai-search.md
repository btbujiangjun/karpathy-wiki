---
title: "arXiv AI Research Search — June 2026"
type: synthesis
created: 2026-06-19
updated: 2026-06-19
sources: [arxiv-ai-search.md]
tags: [arxiv, survey, llm, recommendation, ctr, games, rl, sequential-modeling]
---

# arXiv AI Research Search — June 2026

A curated roundup of recent papers across AI, LLMs, recommendation systems, CTR prediction, sequential modeling, games/RL, and advertising. Papers sourced from arXiv cs.AI, cs.IR, cs.LG, and cs.CL daily listings (June 2026).

---

## Table of Contents

1. [LLM & Foundation Models](#1-llm--foundation-models)
2. [Architecture & Efficiency](#2-architecture--efficiency)
3. [Recommendation Systems](#3-recommendation-systems)
4. [CTR Prediction & Advertising](#4-ctr-prediction--advertising)
5. [Generative Recommendation](#5-generative-recommendation)
6. [Sequential Modeling & User Interest](#6-sequential-modeling--user-interest)
7. [Reinforcement Learning & Games](#7-reinforcement-learning--games)
8. [Multi-Task & Multi-Domain Recommenders](#8-multi-task--multi-domain-recommenders)
9. [RAG & Retrieval](#9-rag--retrieval)
10. [Safety, Fairness & Interpretability](#10-safety-fairness--interpretability)

---

## 1. LLM & Foundation Models

### Variable-Width Transformers
- **Authors**: *(not yet identified — Jun 2026 preprint)*
- **Institution**: N/A
- **Abstract**: Scaling model size, specifically depth and width, has driven significant progress in transformer-based language models. Most architectures maintain constant width across all layers. This work empirically investigates non-uniform capacity allocation, proposing an architecture that maintains wider early and late layers while narrowing middle layers, using parameter-free residual reparameterization.
- **Key Innovation**: Demonstrates that non-uniform width allocation across depth improves parameter efficiency without sacrificing performance.
- **Link**: https://arxiv.org/abs/2606.??? (weekly spotlight on arxiv.deeppaper.ai)

---

### Rethinking the Role of Efficient Attention in Hybrid Architectures
- **Authors**: *(Jun 2026 preprint)*
- **Institution**: N/A
- **Abstract**: Modern language models increasingly adopt hybrid architectures combining full attention with efficient modules (sliding-window attention, recurrent sequence mixers). This paper systematically analyzes hybrid architectures from scaling behavior, mechanism analysis, and architecture design perspectives. Finds that efficient-attention design primarily affects how fast long-context capability emerges.
- **Key Innovation**: First systematic analysis of how efficient attention modules shape model capabilities in hybrid architectures.
- **Link**: https://arxiv.org/abs/2606.??? (weekly spotlight)

---

### CAST: Non-Privileged Clipped Asymmetric Self-Teaching with Advantage Flipping for GRPO
- **Authors**: Yang Li, Gongle Xue, Yijia Guo, Yuheng Yuan, Liwen Hu, Lei Ma
- **Institution**: N/A
- **Abstract**: Improves GRPO (Group Relative Policy Optimization) stability with a novel clipped asymmetric self-teaching approach.
- **Key Innovation**: Advantage flipping mechanism to stabilize RLVR training.
- **Link**: https://arxiv.org/abs/2606.00172

---

### Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning
- **Authors**: Yanxi Chen, Weijie Shi, Yuexiang Xie, Boyi Hu, Yaliang Li, Bolin Ding, Jingren Zhou
- **Institution**: Alibaba Group
- **Abstract**: Presents a general framework for training LLMs to solve long sequences of tasks while continuously exploring environments, learning from experience, and self-updating context. Uses GRPO-style RL with fine-grained credit assignment for end-to-end training on long rollouts interleaving solve-task and update-context episodes.
- **Key Innovation**: First framework to train LLM agents for long-lifecycle meta-capability — solving tasks and updating context in a single RL loop with cross-domain generalization.
- **Link**: https://arxiv.org/abs/2606.20002

---

### AXIOM: A Trust-First Neuro-Symbolic Execution Architecture for Verifiable Mathematical Reasoning
- **Authors**: Alessio Bruno
- **Institution**: N/A
- **Abstract**: A neuro-symbolic architecture for verifiable mathematical reasoning combining LLMs with symbolic execution.
- **Key Innovation**: Trust-first design with live interactive demo.
- **Link**: https://arxiv.org/abs/2606.00671

---

## 2. Architecture & Efficiency

### Dual-Stream MLP is All You Need for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution**: Renmin University of China (expected)
- **Abstract**: Proposes DS-MLP, a dual-stream MLP framework for CTR prediction. Uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP while a parallel MLP captures implicit interactions. Two alignment strategies enhance compatibility between streams.
- **Key Innovation**: Vanilla MLP structure achieving SOTA on three benchmarks — challenges the necessity of complex architectures for CTR. Accepted by TKDD.
- **Link**: https://arxiv.org/abs/2606.04944

---

### Threshold-Based Exclusive Batching for LLM Inference
- **Authors**: Weifang Zhang, Yuzhou Nie, Bowen Pang, Guangrui Ma, Shining Wu
- **Institution**: N/A
- **Abstract**: Proposes a threshold-based batching strategy for efficient LLM inference.
- **Key Innovation**: Accepted at ICML 2026.
- **Link**: https://arxiv.org/abs/2606.00516

---

### TAPS: Target-Aware Prefix Tree Selection for Diffusion-Drafted Speculative Decoding
- **Authors**: Zhuoyu Wang, Junnan Huang, Xinyu Chen
- **Institution**: N/A
- **Abstract**: Uses prefix tree selection to accelerate diffusion-drafted speculative decoding.
- **Key Innovation**: Target-aware selection improves draft acceptance rate.
- **Link**: https://arxiv.org/abs/2606.00487

---

## 3. Recommendation Systems

### SAERec: Constructing Fine-grained Interpretable Intents Priors via Sparse Autoencoders for Recommendation
- **Authors**: Jiangnan Xia, Xuansheng Wu, Yu Yang, Xin Wang, Ninghao Liu
- **Institution**: University of Georgia (Ninghao Liu's group)
- **Abstract**: Uses sparse autoencoders on LLM text embeddings to construct a fine-grained, interpretable intent space. Extracts personal intents (user's current interests) and public intents (item patterns like quality, price) as priors. Multi-branch attention mechanism injects both signals into sequence modeling.
- **Key Innovation**: First use of SAE-disentangled LLM embeddings for interpretable intent-based recommendation.
- **Link**: https://arxiv.org/abs/2606.18897

---

### Token Factory: Efficiently Integrating Diverse Signals into Large Recommendation Models
- **Authors**: Xilun Chen, Shao-Chuan Wang, Baykal Cakici, Lukasz Heldt, Lichan Hong, Raghu Keshavan, Aniruddh Nath, Li Wei, Xinyang Xi
- **Institution**: Google / YouTube
- **Abstract**: Proposes a framework to transform traditional recommendation signals into "soft tokens" processed by transformer-based LRMs. Prevents prompt length explosion while compressing heterogeneous input features. Validated in production-scale recommendation environment.
- **Key Innovation**: Soft token transformation for efficient multimodal signal integration in large recommendation models.
- **Link**: https://arxiv.org/abs/2606.19635

---

### Structuring and Tokenizing Distributed User Interest Context for Generative Recommendation
- **Authors**: Ruizhong Qiu, Yinglong Xia, Dongqi Fu, Hanqing Zeng, Ren Chen, Xiangjun Fan, Hong Li, Hong Yan, Hanghang Tong
- **Institution**: University of Illinois Urbana-Champaign / Meta AI
- **Abstract**: Structures and tokenizes distributed user interest contexts for generative recommendation.
- **Key Innovation**: Novel tokenization of multi-source user interests for generative rec.
- **Link**: https://arxiv.org/abs/2606.20554

---

### RankGraph-2: Lifecycle Co-Design for Billion-Node Graph Learning in Recommendation
- **Authors**: Renzhi Wu, Zikun Cui, Junjie Yang, Tai Guo, Hong Li, Xian Chen, Li Yu, Ke Pan, Sri Reddy, Mahesh Srinivasan, Nipun Mathur, Haomin Yu, Hong Yan
- **Institution**: Meta / LinkedIn
- **Abstract**: Lifecycle co-design for graph learning in recommendation at billion-node scale.
- **Key Innovation**: Full lifecycle optimization for industrial-scale graph recommenders.
- **Link**: https://arxiv.org/abs/2606.18379

---

## 4. CTR Prediction & Advertising

### Generative Long-term User Interest Modeling for Click-Through Rate Prediction (GenLI)
- **Authors**: Jiangli Shao, Kaifu Zheng, Hao Fang, Huimu Ye, Zhiwei Liu, Bo Zhang, Shu Han, Xingxing Wang
- **Institution**: N/A (industry — likely Chinese tech company)
- **Abstract**: Proposes GenLI for CTR prediction with three modules: Interest Generation Module (IGM), Behavior Retrieval Module (BRM), and Interest Fusion Module (IFM). Generates latent user interests rather than relying on pairwise matching, reducing online serving time.
- **Key Innovation**: Generative approach to long-term interest modeling replaces expensive pairwise matching retrieval with interest generation.
- **Link**: https://arxiv.org/abs/2605.15905

---

### Dual-Stream MLP is All You Need for CTR Prediction
- *(Listed above in Architecture & Efficiency)*
- **Relevance**: Core CTR paper; challenges the trend toward increasingly complex interaction architectures.

---

### CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors**: *(Feb 2026)*
- **Institution**: N/A
- **Abstract**: Applies decoder-only Transformer architecture to CTR prediction in online advertising, leveraging generative pre-training.
- **Key Innovation**: Decoder-only (GPT-style) architecture for CTR.
- **Link**: https://arxiv.org/abs/2602.11410

---

### Generative Click-through Rate Prediction with Applications to Search Advertising
- **Authors**: Lingwei Kong, Lu Wang, Changping Peng, Zhangang Lin, Ching Law, Jingping Shao
- **Institution**: Alibaba / JD.com (expected)
- **Abstract**: Two-stage training: generative pre-training for next-item prediction followed by fine-tuning within a discriminative CTR framework. Deployed on one of the world's largest e-commerce platforms.
- **Key Innovation**: Bridges generative pre-training and discriminative CTR in a two-stage framework, validated by online A/B testing.
- **Link**: https://arxiv.org/abs/2507.11246

---

## 5. Generative Recommendation

### On the Memorization Behavior of LLMs in Generative Recommendation: Observations, Implications, and Training Strategies
- **Authors**: Sunwoo Kim, Sunkyung Lee, Clark Mingxuan Ju, Donald Loveland, Bhuvesh Kumar, Kijung Shin, Neil Shah, Liam Collins
- **Institution**: KAIST / Snap Research
- **Abstract**: Investigates one-hop memorization in LLM-based generative recommenders. Shows LLMs memorize direct item-to-item transitions more than non-LLM baselines. Proposes IIRG training strategy teaching LLMs to capture multi-hop collaborative relations and semantic item relations.
- **Key Innovation**: Critical finding that LLM-based GR gains come largely from memorization, not generalization. IIRG mitigates this.
- **Link**: https://arxiv.org/abs/2606.17276

---

### Do Generative Recommenders Deepen the Information Cocoon? A Closed-Loop Simulation with LLM-powered User Simulators
- **Authors**: Jiyuan Yang, Gengxin Sun, Mengqi Zhang, Lingjie Wang, Yuanzi Li, Hongxi Cui, Xin Xin, Pengjie Ren
- **Institution**: Shandong University
- **Abstract**: Proposes RecLoop, a closed-loop simulation framework with LLM-driven user agents to study information cocoons in generative recommenders. Introduces Code-Space Structural Cocoon metric. Finds generative recommenders less prone to exposure-level cocoon formation than traditional baselines, but cocoon severity depends on tokenization strategy and model scale.
- **Key Innovation**: First study of information cocoon effects specific to generative (Semantic ID-based) recommenders.
- **Link**: https://arxiv.org/abs/2606.17707

---

### LensKit-Auto
- **Authors**: Max Breit, Anass Amezian El Idrissi, Rishikesh Giriraj Kulkarni, Luca Quade
- **Institution**: N/A
- **Abstract**: AutoML toolkit for recommender systems based on LensKit.
- **Key Innovation**: Automated hyperparameter optimization for recsys pipelines.
- **Link**: https://arxiv.org/abs/2606.18814

---

## 6. Sequential Modeling & User Interest

### Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Enhanced Sequential User Modeling
- **Authors**: Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang
- **Institution**: N/A
- **Abstract**: Leverages implicit negative behaviors (skips, dwell time) for sequential user modeling.
- **Key Innovation**: Shows implicit negative signals improve sequential recommendation quality.
- **Link**: https://arxiv.org/abs/2606.15252

---

### Harmonizing Semantic and Collaborative in LLMs: Reasoning-based Embedding Generator for Sequential Recommendation
- **Authors**: Qidong Liu, Mingyao Huang, Moranxin Wang, Wenxuan Yang, Haiping Zhu
- **Institution**: N/A
- **Abstract**: Combines semantic and collaborative signals via LLM reasoning for sequential recommendation embeddings.
- **Key Innovation**: Reasoning-based embedding generation that bridges semantic and collaborative spaces.
- **Link**: https://arxiv.org/abs/2606.16703

---

### NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation
- **Authors**: Huichao Zhang, Liao Qu, Yiheng Liu, Hang Chen, Yangyang Song, Yongsheng Dong, Shikun Sun, Xian Li, Xu Wang, Yi Jiang, Hu Ye, Bo Chen, Yiming Gao, Peng Liu, Akide Liu, Zhipeng Yang, Qili Deng, Linjie Xing, Jiyang Liu, Zhao Wang, Yang Zhou, Mingcong Liu, Yi Zhang, Qian He, Xiwei Hu, Zhongqi Qi, Jie Shao, Zhiye Fu, Shuai Wang, Fan-Fan Chen, Xuezhi Chai, Zhihua Wu, Yitong Wang, Zehuan Yuan, Daniel K. Du, Xinglong Wu
- **Institution**: ByteDance / Tsinghua University / Monash University
- **Abstract**: Decoder-only autoregressive transformer trained on 6T interleaved text-image tokens. Uses next-token prediction for text and next-scale prediction for visual generation. Generates 1024×1024 images in 5 seconds — orders of magnitude faster than comparable AR models.
- **Key Innovation**: Next-scale prediction for visual tokens within a unified autoregressive framework; prefix-tuning for RL.
- **Link**: https://arxiv.org/abs/2601.02204

---

## 7. Reinforcement Learning & Games

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning
- **Authors**: Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Institution**: National University of Singapore / Google DeepMind
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving versions of themselves. Proposes role-conditioned advantage estimation (RAE) for stable multi-agent training. Improves reasoning by up to 10% across 8 benchmarks on Qwen and Llama models.
- **Key Innovation**: Eliminates human supervision — self-play in zero-sum games as a general reasoning curriculum. Accepted at ICLR 2026.
- **Link**: https://arxiv.org/abs/2506.24119

---

### Evaluating Interactive Reasoning in Large Language Models: A Hierarchical Benchmark with Executable Games
- **Authors**: Mingyuan Fan, Weiguang Han, Daixin Wang, Cen Chen, Zhiqiang Zhang, Jun Zhou
- **Institution**: Ant Group
- **Abstract**: Multi-turn interactive framework with 474 executable games at 5 difficulty levels. LLMs receive only task rules, must issue queries to a hidden environment, integrate observations, and decide when to answer. Evaluates contextual robustness and metacognitive adaptation.
- **Key Innovation**: Interactive reasoning benchmark that measures active evidence acquisition, not passive QA.
- **Link**: https://arxiv.org/abs/2606.00103

---

### Game-RL: Synthesizing Multimodal Verifiable Game Data to Boost VLMs' General Reasoning
- **Authors**: Jingqi Tong, Jixin Tang, Hangcheng Li, Yurong Mou, Ming Zhang, Jun Zhao, Yanbo Wen, Fan Song, Jiahao Zhan, Yuyang Lu, Chaoran Tao, Zhiyuan Guo, Jizhou Yu, Tianhao Cheng, Zhiheng Xi, Changhao Jiang, Zhangyue Yin, Yining Zheng, Weifeng Ge, Guanhua Chen, Tao Gui, Xipeng Qiu, Qi Zhang, Xuanjing Huang
- **Institution**: Fudan University
- **Abstract**: Proposes Code2Logic to synthesize reasoning data from game code, creating GameQA with 30 games and 158 verifiable tasks. RL training on GameQA generalizes across 7 out-of-domain VL benchmarks.
- **Key Innovation**: Scaling game diversity in RL training consistently improves multimodal reasoning. Accepted at ICLR 2026.
- **Link**: https://openreview.net/forum?id=e4FqU4SyHL

---

### Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **Authors**: *(May 2026)*
- **Institution**: N/A
- **Abstract**: Uses RL to teach LLMs strategic reasoning in multi-agent game settings.
- **Key Innovation**: RL-based strategic reasoning improvement from game feedback.
- **Link**: https://arxiv.org/abs/2605.??? (May 2026)

---

### MindGames Arena Generalization Track: In2AI Solution with Delayed Per-Step Reward Attribution
- **Authors**: Aliaksei Korshuk, Alexander Buyantuev, Ilya Makarov
- **Institution**: N/A
- **Abstract**: First-place solution (both Open and Efficient tracks) at NeurIPS 2025 MindGames Arena.
- **Key Innovation**: Delayed per-step reward attribution for multi-agent game environments.
- **Link**: https://arxiv.org/abs/2606.00017

---

## 8. Multi-Task & Multi-Domain Recommenders

### OneRank: Unified Transformer-Native Ranking Architecture for Multi-Task Recommendation
- **Authors**: Jiakai Tang, Sunhao Dai, Kun Wang, Zhiluohan Guo, Yu Zhao, Cong Fu, Kangle Wu, Yabo Ni, Anxiang Zeng, Xu Chen, Jun Xu
- **Institution**: Renmin University of China / Taobao (Alibaba)
- **Abstract**: Eliminates encoder-predictor separation in multi-task recommenders. Introduces task-private channels with bottom-up task-conditioned information selection, candidate-aware contextualization, and controlled cross-task interaction. Gradient detachment prevents negative transfer. Replaces MLP scorers with dynamic matching-based scoring.
- **Key Innovation**: First truly Transformer-native multi-task ranking architecture. Accepted at KDD 2026.
- **Link**: https://arxiv.org/abs/2606.16838

---

## 9. RAG & Retrieval

### Decoupling Search from Reasoning: A Vendor-Agnostic Grounding Architecture for LLM Agents
- **Authors**: Emmanuel Aboah Boateng, Kyle MacDonald, Amardeep Kumar, Siddharth Kodwani, Sudeep Das
- **Institution**: N/A
- **Abstract**: Decouples search from reasoning in LLM agents with a vendor-agnostic grounding architecture.
- **Key Innovation**: Modular separation enables flexible search backend swapping.
- **Link**: https://arxiv.org/abs/2606.18947

---

### Temporal Preference Optimization for Unsupervised Retrieval
- **Authors**: HyunJin Kim, Jaejun Shim, Young Jin Kim, JinYeong Bak
- **Institution**: N/A
- **Abstract**: Preference optimization for retrieval without labeled data, using temporal signals. Accepted at ICML 2026.
- **Key Innovation**: Unsupervised temporal preference learning for dense retrieval.
- **Link**: https://arxiv.org/abs/2606.17664

---

### RL-Index: Reinforcement Learning for Retrieval Index Reasoning
- **Authors**: *(Jun 2026)*
- **Institution**: N/A
- **Abstract**: Uses RL (GRPO) with retrieval similarity reward to optimize LLM-generated rationales in document indexes, shifting complex reasoning from query-time to indexing stage.
- **Key Innovation**: First use of RL for retrieval index augmentation.
- **Link**: https://arxiv.org/abs/2606.??? (weekly spotlight)

---

## 10. Safety, Fairness & Interpretability

### Personalization Meets Safety: Mechanisms, Risks, and Mitigations in Personalized LLMs
- **Authors**: *(Jun 2026)*
- **Institution**: N/A
- **Abstract**: First comprehensive safety-aware review of personalized LLMs. Establishes unified taxonomy of risks and a framework for secure personalized systems.
- **Key Innovation**: Systematizes safety risks unique to personalized LLM deployment.
- **Link**: https://arxiv.org/abs/2606.09038

---

### TIGER: Traceable Inference with Graph-Based Evidence Routing for Mitigating Hallucinations in Multimodal Generation
- **Authors**: Kaixiang Zhao, Tianrun Yu, Shawn Huang, Porter Jenkins, Yushun Dong, Amanda Hughes
- **Institution**: N/A
- **Abstract**: Graph-based evidence routing for traceable multimodal generation.
- **Key Innovation**: Evidence graphs enable hallucination tracing and mitigation.
- **Link**: https://arxiv.org/abs/2606.00232

---

### Capability Self-Assessment: Teaching LLMs to Know Their Limits
- **Authors**: Haoyan Yang, Reza Shirkavand, Yukai Jin, Jiawei Zhou, Shangqian Gao, Heng Huang
- **Institution**: University of Maryland (expected)
- **Abstract**: Trains LLMs to self-assess their capabilities and decline out-of-scope queries.
- **Key Innovation**: Calibrated self-assessment without external classifiers.
- **Link**: https://arxiv.org/abs/2606.00251

---

## Summary Statistics

| Domain | Papers This Month |
|--------|-------------------|
| LLM / Foundation Models | ~120+ (cs.AI) |
| Recommendation Systems | ~30+ (cs.IR) |
| CTR / Advertising | ~10+ (cs.IR) |
| Sequential Modeling | ~15+ (cs.IR, cs.LG) |
| RL / Games | ~50+ (cs.AI, cs.LG) |
| RAG / Retrieval | ~40+ (cs.IR) |
| Safety / Interpretability | ~25+ (cs.AI) |

**Notable trends this month:**
- Generative recommendation (Semantic ID-based) is a major focus — critical analyses of memorization and information cocoon effects emerging
- Self-play / game-based RL training for reasoning is a hot area (SPIRAL, Game-RL accepted at ICLR 2026)
- Sparse autoencoders (SAEs) entering recommendation systems for interpretability (SAERec)
- Transformer-native architectures replacing encoder-predictor separation in multi-task recommenders (OneRank at KDD 2026)
- Soft tokenization for integrating diverse signals into LRMs (Token Factory from Google)
- RL-based retrieval indexing (RL-Index)
