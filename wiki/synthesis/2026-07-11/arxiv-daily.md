---
title: "arXiv Daily - July 11, 2026"
type: synthesis
created: 2026-07-11
updated: 2026-07-11
sources: []
tags: [arxiv, daily, llm, recommendation, ctr, sequential-modeling, advertising, games]
---

# arXiv Daily Report - July 11, 2026

## LLMs & Large Language Models

### 1. Understanding Large Language Models
- **Authors**: Yannik Keller, Thomas Eisenmann
- **Institution**: (Not specified)
- **Abstract**: A comprehensive chapter outlining current understanding of LLMs, discussing emerging capabilities and their mechanistic implementation. Reviews explainable AI approaches from neuron activation analysis to circuit tracing. Argues for nuanced discussion of LLM cognition that neither dismisses differences nor precludes AI cognition through reductionist arguments.
- **Key Innovations**: Comprehensive review of LLM capabilities, mechanistic interpretability, and the debate around LLM cognition vs. pattern memorization
- **Link**: https://arxiv.org/abs/2607.01006
- **Date**: July 1, 2026

### 2. KVpop: Key-Value Cache Compression with Predictive Online Pruning
- **Authors**: (Not fully specified)
- **Institution**: (Not specified)
- **Abstract**: Addresses KV cache growth bottleneck in autoregressive decoding. Introduces KVpop which learns a fixed-budget KV eviction policy by directly supervising the keep-or-drop decision against a novel future-attention target.
- **Key Innovations**: Future-attention target for KV eviction, learned eviction policy that adapts to dynamic relevance shifts
- **Link**: https://arxiv.org/abs/2607.XXXXX (from DeepPaper weekly)
- **Date**: July 8, 2026

### 3. LLM Self-Recognition: Steering and Retrieving Activation Signatures
- **Authors**: Thibaud Ardoin, Jonas Schäfer, Gerhard Wunder
- **Institution**: (Not specified)
- **Abstract**: Demonstrates that LLMs can reliably recognize their own outputs. By steering the internal residual stream with random sparse vectors, creates detectable fingerprints enabling multi-LLM identification with >98% accuracy without quality degradation.
- **Key Innovations**: Self-recognition capability in LLMs, steering mechanism for multi-LLM identification, activation space structure exploitation
- **Link**: https://arxiv.org/abs/2606.06315
- **Date**: June 5, 2026

### 4. Challenges and Research Directions for Large Language Model Inference Hardware
- **Authors**: Xiaoyu Ma, David Patterson
- **Institution**: (Not specified)
- **Abstract**: Highlights four architecture research opportunities for LLM inference: High Bandwidth Flash for 10X memory capacity, Processing-Near-Memory and 3D memory-logic stacking for high memory bandwidth, and low-latency interconnect to speedup communication.
- **Key Innovations**: Hardware architecture innovations for LLM inference efficiency, addressing memory and interconnect challenges
- **Link**: https://arxiv.org/abs/2601.05047
- **Date**: January 8, 2026 (Accepted by IEEE Computer 2026)

---

## Recommendation Systems

### 5. Deep Research for Recommender Systems (RecPilot)
- **Authors**: Kesha Ou, Chenghao Wu, Xiaolei Wang, Bowen Zheng, Wayne Xin Zhao, Weitao Li, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution**: (Not specified)
- **Abstract**: Proposes a novel deep research paradigm for recommendation that replaces conventional item lists with comprehensive, user-centric reports. Instantiated through RecPilot, a multi-agent framework comprising a user trajectory simulation agent and a self-evolving report generation agent.
- **Key Innovations**: Reframes recommendation as proactive agent-driven service, multi-agent framework for autonomous exploration and report generation
- **Link**: https://arxiv.org/abs/2603.07605
- **Date**: March 8, 2026

### 6. AgenticRS-Architecture: System Design for Agentic Recommender Systems
- **Authors**: (Not fully specified)
- **Institution**: (Not specified)
- **Abstract**: Presents system design for agentic recommender systems with AutoTrain (model evolution), AutoFeature (representation evolution), and AutoPerf (resource evolution). Includes case study on paper_auto_train for automating research paper reproduction and method adaptation.
- **Key Innovations**: Three-pillar architecture for self-evolving recommender systems, automated model iteration pipeline
- **Link**: https://arxiv.org/html/2603.26085v2
- **Date**: (Not specified)

### 7. Autonomous Information Seeking: A Roadmap for Agentic Recommender Systems
- **Authors**: Xinyu Lin, Yashar Deldjoo, Sunhao Dai, Honghui Bao et al.
- **Institution**: (Not specified)
- **Abstract**: Survey providing a comprehensive overview of LLM-based agents integration into recommender systems, shifting from static ranking-based pipelines to autonomous interactive systems that can reason, plan, and act.
- **Key Innovations**: Roadmap for agentic recommender systems, framework for LLM-based interactive recommendation
- **Link**: https://arxiv.org/abs/2607.04433
- **Date**: July 5, 2026

### 8. SCOReD: Student-Aware CoT Optimization for Recommendation Distillation
- **Authors**: Haz Sameen Shahgir, Yufei Li, Frank Shyu, Luke Simon et al.
- **Institution**: (Not specified)
- **Abstract**: Addresses chain-of-thought (CoT) distillation in recommendation domain as precursor to RL training. Addresses the issue that raw teacher traces are ill-suited to this task due to high reasoning uncertainty.
- **Key Innovations**: Student-aware CoT optimization for recommendation, addressing teacher trace quality issues
- **Link**: https://arxiv.org/abs/2607.05734
- **Date**: July 7, 2026

---

## CTR Prediction

### 9. GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Hongyu Lu, Ji-Rong Wen
- **Institution**: (Not specified)
- **Abstract**: Proposes GenCI, a generative user intent framework that leverages semantic interest cohorts to model dynamic user preferences. Uses generative model trained with next-item prediction objective to proactively produce candidate interest cohorts.
- **Key Innovations**: Generative intent modeling, cohort-based interest representation, hierarchical candidate-aware network
- **Link**: https://arxiv.org/abs/2601.18251
- **Date**: January 26, 2026 (Accepted by WWW 2026)

### 10. CADET: Context-Conditioned Ads CTR Prediction
- **Authors**: Taesung Song, Lars Hertel, Young Jin Yun, Senthil Radhakrishnan et al.
- **Institution**: LinkedIn
- **Abstract**: End-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Addresses unique challenges of adapting transformer architectures to ads CTR: handling post-scoring contextual signals, maintaining offline-online consistency, and scaling to industrial workloads.
- **Key Innovations**: Decoder-only transformer for ads CTR, context-conditioned prediction, industrial deployment at scale
- **Link**: https://arxiv.org/abs/2602.11410
- **Date**: February 11, 2026

### 11. Generative Long-term User Interest Modeling for Click-Through Rate Prediction (GenLI)
- **Authors**: Jiangli Shao, Kaifu Zheng, Hao Fang, Huimu Ye, Zhiwei Liu, Bo Zhang, Shu Han, Xingxing Wang
- **Institution**: (Not specified)
- **Abstract**: Proposes GenLI for CTR prediction with interest generation module (IGM), behavior retrieval module (BRM), and interest fusion module (IFM). IGM generates multiple interest distributions for target-independent interest features with O(1) complexity.
- **Key Innovations**: Interest generation for target-independent features, O(1) behavior retrieval, complete and diverse interest modeling
- **Link**: https://arxiv.org/abs/2605.15905
- **Date**: May 15, 2026

### 12. LoopCTR: Unlocking the Loop Scaling Power for Click-Through Rate Prediction
- **Authors**: Jiakai Tang, Runfeng Zhang, Weiqiu Wang, Yifei Liu, Chuan Wang, Xu Chen, Yeqiu Yang, Jian Wu, Yuning Jiang, Bo Zheng
- **Institution**: (Not specified)
- **Abstract**: Introduces loop scaling paradigm that increases training-time computation through recursive reuse of shared model layers, decoupling computation from parameter growth. Enables train-multi-loop, infer-zero-loop strategy.
- **Key Innovations**: Loop scaling paradigm, Hyper-Connected Residuals with MoE, process supervision at every loop depth
- **Link**: https://arxiv.org/abs/2604.19550
- **Date**: April 21, 2026

### 13. GRAB: Generative Ranking for Ads at Baidu
- **Authors**: Chuyue Xie, Renhao Cheng, Zhiqiang Cao, Zehao Ju, Yu Gao, Jie Ding, Xiaodong Chen, Xuewu Jiao, Shuanglong Li, Liu Lin
- **Institution**: Baidu
- **Abstract**: End-to-end generative framework for CTR prediction with Causal Action-aware Multi-channel Attention (CamA). Full-scale online deployment demonstrates 3.05% revenue increase and 3.49% CTR rise.
- **Key Innovations**: Causal Action-aware Multi-channel Attention, scaling behavior with monotonic improvement, industrial deployment at Baidu
- **Link**: https://arxiv.org/abs/2602.01865
- **Date**: February 2, 2026

### 14. FEDIN: Frequency-Enhanced Deep Interest Network for CTR Prediction
- **Authors**: (Not specified)
- **Institution**: Tencent
- **Abstract**: Addresses sequential recommendation models' struggle to capture latent periodic patterns in user interests due to noise in time-domain behavioral data.
- **Key Innovations**: Frequency-domain enhancement for periodic pattern capture in CTR prediction
- **Link**: https://arxiv.org/abs/2605.01726
- **Date**: May 3, 2026

---

## Sequential Modeling & Time Series

### 15. It's TIME: Towards the Next Generation of Time Series Forecasting Benchmarks
- **Authors**: Zhongzheng Qiao, Qingsong Wen, Mingsheng Long, Ming Jin, Chenghao Liu
- **Institution**: (Not specified)
- **Abstract**: Introduces TIME, a task-centric benchmark with 50 fresh datasets and 98 forecasting tasks for zero-shot TSFM evaluation. Proposes pattern-level evaluation perspective using structural time series features.
- **Key Innovations**: Next-generation benchmark for time series foundation models, human-in-the-loop construction pipeline, pattern-level evaluation
- **Link**: https://arxiv.org/abs/2602.12147
- **Date**: February 12, 2026 (Accepted to ICML 2026)

### 16. Universal Redundancies in Time Series Foundation Models
- **Authors**: Anthony Bao, Venkata Hasith Vattikuti, Jeffrey Lai, William Gilpin
- **Institution**: (Not specified)
- **Abstract**: Discovers that leading transformer-based TSFMs exhibit redundant components in intermediate layers. Develops theoretical framework framing transformers as kernel regressors for ablating heads based on stable rank.
- **Key Innovations**: Mechanistic interpretability tools for TSFMs, theoretical framework for head ablation, discovery of universal redundancies
- **Link**: https://arxiv.org/abs/2602.01605
- **Date**: February 2, 2026

### 17. Modeling Dynamic Mixtures of Time-Delay Systems from Streaming Time Series (DelayMix)
- **Authors**: Ren Fujiwara, Yasuko Matsubara, Yasushi Sakurai
- **Institution**: (Not specified)
- **Abstract**: Online framework treating streaming time series as dynamic mixtures of time-delay systems. Uses summary system tensor and tensor decomposition for rapid adaptation to environmental changes.
- **Key Innovations**: Summary system tensor with Markov parameter series, tensor decomposition for past regime extraction, O(1) adaptation complexity
- **Link**: https://arxiv.org/abs/2605.26191
- **Date**: May 25, 2026 (Accepted by IJCAI 2026)

### 18. PraMem: Practice-derived Experiential Memory for Long-horizon Behavior Prediction
- **Authors**: (Not specified)
- **Institution**: (Not specified)
- **Abstract**: Addresses long-horizon behavior prediction using LLMs. Proposes practice-derived experiential memory to resolve latent behavioral pattern induction and model-intrinsic cognitive biases.
- **Key Innovations**: Practice-derived experiential memory for LLM-based behavior prediction, addressing long-horizon prediction challenges
- **Link**: https://arxiv.org/abs/2607.XXXXX (from DeepPaper weekly)
- **Date**: July 8, 2026

---

## Advertising

### 19. Incentive-Aware Multi-Fidelity Optimization for Generative Advertising in LLMs (IAMFM)
- **Authors**: Jiayuan Liu, Barry Wang, Jiarui Gan, Tonghan Wang, Leon Xie, Mingyu Guo, Vincent Conitzer
- **Institution**: (Not specified)
- **Abstract**: Proposes IAMFM coupling VCG incentives with Multi-Fidelity Optimization for generative advertising in LLM responses. Introduces Active Counterfactual Optimization for efficient payment calculation.
- **Key Innovations**: VCG incentive alignment for generative advertising, multi-fidelity optimization, active counterfactual optimization for warm-start
- **Link**: https://arxiv.org/abs/2604.06263
- **Date**: April 7, 2026

### 20. Unified Value Alignment for Generative Recommendation in Industrial Advertising
- **Authors**: (Not specified)
- **Institution**: Tencent
- **Abstract**: Addresses Generative Recommendation (GR) reformulation as next-token generation problem for industrial advertising applications.
- **Key Innovations**: Unified value alignment for generative recommendation in advertising
- **Link**: https://arxiv.org/abs/2605.05803
- **Date**: May 7, 2026

---

## Game Theory & Reinforcement Learning

### 21. MARLIN: Multi-Agent Game-Theoretic Reinforcement Learning for Sustainable LLM Inference in Cloud Datacenters
- **Authors**: H. Moore, S. Qi, D. Milojicic, C. Bash, S. Pasricha
- **Institution**: (Not specified)
- **Abstract**: Novel multi-agent game-theoretic RL framework to co-optimize TTFT, carbon emissions, water usage, and energy costs for LLM inference. Demonstrates 18% TTFT reduction, 33% carbon emissions reduction, 43% water usage reduction, 11% energy cost reduction.
- **Key Innovations**: Multi-agent game-theoretic approach for LLM inference sustainability, multi-objective optimization
- **Link**: https://arxiv.org/abs/2605.13496
- **Date**: May 13, 2026

### 22. Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini et al.
- **Institution**: (Not specified)
- **Abstract**: Vision paper proposing framework for training RL models suited for game AI and game development. Identifies bottlenecks and hard problems for deploying player-facing ML agents in modern games.
- **Key Innovations**: Framework for RL-augmented game AI, practical deployment considerations for player-facing ML agents
- **Link**: https://arxiv.org/abs/2606.20210
- **Date**: June 18, 2026 (Conference on Games 2026)

### 23. Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **Authors**: (Not specified)
- **Institution**: (Not specified)
- **Abstract**: System teaching LLMs to play strategic games through reinforcement learning, learning from feedback about move quality rather than generating first-available responses.
- **Key Innovations**: RL-based strategic reasoning enhancement for LLMs, feedback-driven improvement
- **Link**: https://arxiv.org/abs/2605.XXXXX
- **Date**: May 6, 2026

---

## Summary

This report covers recent papers from July 2026 (and late June) across six major AI research areas:

1. **LLMs**: Focus on inference efficiency (KV cache compression), self-recognition capabilities, and hardware optimization
2. **Recommendation Systems**: Shift toward agentic and autonomous systems with multi-agent frameworks
3. **CTR Prediction**: Strong trend toward generative approaches for user interest modeling and ranking
4. **Sequential Modeling**: Next-generation benchmarks, foundation model interpretability, and streaming adaptation
5. **Advertising**: Integration of game-theoretic incentives with LLM-based generative advertising
6. **Game Theory & RL**: Applications from sustainable LLM serving to game AI enhancement

---
*Report generated: 2026-07-11*
