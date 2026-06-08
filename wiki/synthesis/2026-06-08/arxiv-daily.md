---
title: arXiv Daily — AI Research Survey (June 8, 2026)
type: synthesis
created: 2026-06-08
updated: 2026-06-08
sources: []
tags: [arxiv-daily, ai, llm, ctr, recommendation, sequential-modeling, games, rl, search]
---

# arXiv Daily — AI Research Survey

> Date: 2026-06-08 (Mon)
> Coverage: ~40 papers across LLM, CTR prediction, recommendation systems, search/retrieval, games/RL, MoE
> arXiv 2606 series (Jun 2026), cs.AI, cs.IR, cs.LG, cs.CL

---

## Large Language Models

### 1. Generative Criticality in Large Language Model Temperature Scaling
- **Link**: [arxiv.org/abs/2606.06238](https://arxiv.org/abs/2606.06238)
- **Authors**: Qwen3 series study
- **Institution**: —
- **Abstract**: Treats token embeddings as continuous spin variables in a statistical field. Finds sharp susceptibility peak near characteristic temperature T_c ≈ 1.4 with power-law scaling.
- **Key Innovation**: Phase-transition-like phenomenon in LLM decoding, robust across Qwen3 0.6B–32B.
- **Tags**: `LLM` `temperature-scaling` `statistical-physics`

### 2. LLM Self-Recognition: Steering and Retrieving Activation Signatures
- **Link**: [arxiv.org/abs/2606.06315](https://arxiv.org/abs/2606.06315)
- **Authors**: Thibaud Ardoin et al.
- **Institution**: —
- **Abstract**: Reliable self-recognition of LLM outputs via internal activation signatures. Steering-based watermarking by injecting random sparse vectors into the residual stream.
- **Key Innovation**: >98% attribution accuracy across multiple detection settings, no quality degradation.
- **Tags**: `LLM` `watermarking` `attribution` `AI-safety`

### 3. FLARE: Diffusion for Hybrid Language Model
- **Link**: [arxiv.org/abs/2606.01774](https://arxiv.org/abs/2606.01774)
- **Authors**: Yuchen Zhu, Jing Shi, Chongjian Ge, et al.
- **Institution**: —
- **Abstract**: Converts hybrid-attention (softmax + linear) AR LLMs into diffusion LLMs (dLLMs). Transfer-data quality is dominant factor for preserving AR capability.
- **Key Innovation**: Unified inference supporting both AR verified decoding and diffusion parallel denoising. FLARE-2B/4B/9B competitive dLLM quality.
- **Tags**: `LLM` `diffusion` `hybrid-attention` `dLLM`

### 4. Enhancing LLM Metacognition via Cognitive Pairwise Training
- **Link**: [arxiv.org/abs/2606.00869](https://arxiv.org/abs/2606.00869)
- **Authors**: Weitao Li, Hao Zhou, Xuanyu Lei et al. (Tsinghua University)
- **Institution**: Tsinghua University
- **Abstract**: Cognitive Pairwise Training (CPT) — mid-training stage teaching LLMs to compare reasoning traces and internalize a reasoning-quality discrimination boundary.
- **Key Innovation**: CPT+RL at 14B outperforms SFT+RL by +2.2 math-average and +5.2 abstention-F1. Works across Qwen3, LLaMA, Olmo 3B–32B.
- **Tags**: `LLM` `metacognition` `reasoning` `RL`

### 5. Hidden Thoughts Are Not Secret: Reasoning Trace Exposure in LLMs
- **Link**: [arxiv.org/abs/2606.00642](https://arxiv.org/abs/2606.00642)
- **Authors**: Yu-An Lu, Ci-Yang Tsai, Yu-Lin Tsai, Raluca Ada Popa, Chia-Mu Yu
- **Institution**: —
- **Abstract**: Investigates whether reasoning traces in LLMs leak private information about training data or model internals.
- **Key Innovation**: Security analysis of reasoning transparency vs. privacy risks.
- **Tags**: `LLM` `reasoning` `privacy` `security`

### 6. BitsMoE: Efficient Spectral Energy-Guided Bit Allocation for MoE LLM Quantization
- **Link**: [arxiv.org/abs/2606.00079](https://arxiv.org/abs/2606.00079)
- **Authors**: Jiayu Zhao, Zihan Teng, Minhao Fan et al.
- **Institution**: —
- **Abstract**: Spectral energy-guided bit allocation for quantizing Mixture-of-Experts LLMs. Allocates bits based on singular value energy distribution.
- **Key Innovation**: First quantization method targeting MoE-specific parameter sensitivity patterns.
- **Tags**: `LLM` `MoE` `quantization` `compression`

### 7. Quantized Reasoning Models Think They Need to Think Longer, but They Do Not
- **Link**: [arxiv.org/abs/2606.00206](https://arxiv.org/abs/2606.00206)
- **Authors**: Sanae Lotfi, Polina Kirichenko, Steven Li, Zechun Liu
- **Institution**: —
- **Abstract**: Quantized reasoning models produce longer reasoning traces but do not improve accuracy. Shows that quantization artifacts cause models to "overthink."
- **Key Innovation**: Identifies and measures reasoning inflation in quantized models. Proposes mitigation strategies.
- **Tags**: `LLM` `quantization` `reasoning` `efficiency`

### 8. CAST: Non-Privileged Clipped Asymmetric Self-Teaching with Advantage Flipping for GRPO
- **Link**: [arxiv.org/abs/2606.00172](https://arxiv.org/abs/2606.00172)
- **Authors**: Yang Li, Gongle Xue, Yijia Guo et al.
- **Institution**: —
- **Abstract**: Improves GRPO with clipped asymmetric self-teaching and advantage flipping for better exploration in RL-based LLM training.
- **Key Innovation**: Addresses reward hacking and mode collapse in GRPO-based reasoning model training.
- **Tags**: `LLM` `RL` `GRPO` `reasoning` `alignment`

---

## CTR Prediction & Advertising

### 9. Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)
- **Link**: [arxiv.org/abs/2606.04944](https://arxiv.org/abs/2606.04944)
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao et al. (RUCAIBox)
- **Institution**: Renmin University of China
- **Abstract**: Knowledge distillation consolidates explicit feature interaction learning into a main MLP; parallel MLP captures implicit interactions. SOTA with only vanilla MLP structure.
- **Key Innovation**: Proves complex interaction architectures can be distilled into simple MLPs without quality loss.
- **Tags**: `CTR` `recommender-system` `knowledge-distillation` `MLP`

### 10. Taiji: Pareto Optimal Policy Optimization for Industrial LLM-Enhanced Recommendation
- **Link**: [arxiv.org/abs/2606.03866](https://arxiv.org/abs/2606.03866)
- **Authors**: Yuecheng Li, Zeyu Song, Jing Yao, Chi Lu, Peng Jiang, Kun Gai
- **Institution**: Kuaishou
- **Abstract**: Pareto optimal policy optimization balancing semantics and ID spaces for LLM-enhanced recommendation. Deployed on Kuaishou's advertising platform.
- **Key Innovation**: Pareto-optimal trade-off between LLM semantic space and recommender ID space. Serves 400M+ users daily.
- **Tags**: `CTR` `LLM` `recommendation` `Pareto` `Kuaishou`

### 11. Generative Long-term User Interest Modeling for CTR Prediction (GenLI)
- **Link**: [arxiv.org/abs/2605.15905](https://arxiv.org/abs/2605.15905)
- **Authors**: Jiangli Shao, Kaifu Zheng, Hao Fang et al.
- **Institution**: —
- **Abstract**: Generative approach to long-term user interest modeling. Interest generation module produces multi-interest distributions target-independently.
- **Key Innovation**: Replaces expensive matching-based behavior retrieval with O(1) lookup via generative interest distributions.
- **Tags**: `CTR` `user-interest` `generative` `long-tail`

### 12. GRAB: LLM-Inspired Sequence-First CTR Prediction at Baidu
- **Link**: [arxiv.org/abs/2602.01865](https://arxiv.org/abs/2602.01865)
- **Authors**: Shaopeng Chen, Chuyue Xie, Huimin Ren et al.
- **Institution**: Baidu
- **Abstract**: End-to-end generative framework for CTR prediction with Causal Action-aware Multi-channel Attention (CamA). Monotonic scaling with sequence length.
- **Key Innovation**: +3.05% revenue, +3.49% CTR in full-scale online deployment at Baidu.
- **Tags**: `CTR` `generative` `Baidu` `scaling`

### 13. CADET: Context-Conditioned Ads CTR Prediction With Decoder-Only Transformer
- **Link**: [arxiv.org/abs/2602.11410](https://arxiv.org/abs/2602.11410)
- **Authors**: LinkedIn
- **Institution**: LinkedIn
- **Abstract**: End-to-end decoder-only transformer for ads CTR with context-conditioned decoding, self-gated attention, timestamp-based RoPE.
- **Key Innovation**: Resolves chicken-and-egg problem between pCTR and ad position. +11.04% CTR lift over LiRank.
- **Tags**: `CTR` `advertising` `decoder-only` `LinkedIn`

---

## Search & Retrieval

### 14. Whole-Pool Setwise Reranking with Long-Context Language Models
- **Link**: [arxiv.org/abs/2606.01782](https://arxiv.org/abs/2606.01782)
- **Authors**: Hang Li, Chuting Yu, Teerapong Leelanupab, Bevan Koopman, Guido Zuccon
- **Institution**: —
- **Abstract**: Uses long-context LMs to rerank entire document pools setwise (all candidates at once) instead of pairwise.
- **Key Innovation**: First work to evaluate whole-pool reranking with modern long-context LLMs. Shows improved efficiency and effectiveness.
- **Tags**: `search` `reranking` `long-context` `LLM`

### 15. Critic-R: Improving Agentic Search using Instruction-tuned Retrievers
- **Link**: [arxiv.org/abs/2606.00590](https://arxiv.org/abs/2606.00590)
- **Authors**: Md Zarif Ul Alam, Alireza Salemi, Hamed Zamani
- **Institution**: —
- **Abstract**: Instruction-tuned retrievers with natural language introspective feedback for agentic search. The retriever critiques its own outputs.
- **Key Innovation**: Self-correcting retrieval for multi-step agentic search scenarios.
- **Tags**: `search` `retrieval` `agents` `instruction-tuning`

### 16. Cost-Aware Query Routing in RAG: Empirical Analysis of Retrieval Depth Tradeoffs
- **Link**: [arxiv.org/abs/2606.02581](https://arxiv.org/abs/2606.02581)
- **Authors**: Sanjay Mishra
- **Institution**: —
- **Abstract**: Systematic analysis of retrieval depth vs. quality tradeoffs in RAG pipelines. Proposes cost-aware routing strategies.
- **Key Innovation**: Empirical framework for optimizing retrieval budget allocation in production RAG systems.
- **Tags**: `RAG` `retrieval` `cost-efficiency` `routing`

### 17. LLMs Need Encoders for Semantic IDs Too
- **Link**: [arxiv.org/abs/2606.00324](https://arxiv.org/abs/2606.00324)
- **Authors**: Xiangyi Chen, Zelun Wang, Xinyi Li et al.
- **Institution**: —
- **Abstract**: Shows that directly using LLM embeddings as item IDs underperforms, and dedicated encoders for semantic IDs are necessary for effective retrieval.
- **Key Innovation**: Encoder design principles for semantic item ID representation in LLM-based retrieval.
- **Tags**: `retrieval` `semantic-ID` `LLM` `encoding`

### 18. MemGraphRAG: Memory-based Multi-Agent System for Graph RAG
- **Link**: [arxiv.org/abs/2606.00610](https://arxiv.org/abs/2606.00610)
- **Authors**: Chuanjie Wu, Zhishang Xiang, Yunbo Tang et al.
- **Institution**: — (Accepted at KDD 2026)
- **Abstract**: Multi-agent RAG system combining graph-based knowledge representation with memory modules for iterative reasoning.
- **Key Innovation**: KDD 2026. Graph-structured memory enables more coherent multi-hop reasoning.
- **Tags**: `RAG` `graph` `multi-agent` `KDD26`

---

## Recommendation Systems

### 19. SPHERE: Semantic Personas for Cross-Domain Recommendation
- **Link**: [arxiv.org/abs/2606.01783](https://arxiv.org/abs/2606.01783)
- **Authors**: Jonathan Mayo, Moshe Unger, Konstantin Bauman
- **Institution**: —
- **Abstract**: LLM-induced behavioral vocabulary generates structured semantic personas enabling cross-domain transfer across strictly disjoint domains (no shared users/items).
- **Key Innovation**: Cross-domain transfer via behavioral semantics rather than identity alignment. Works across Amazon Books, Goodreads, Steam.
- **Tags**: `recommendation` `cross-domain` `LLM` `semantic-persona`

### 20. UniPinRec: Unifying Generative Retrieval and Ranking at Pinterest Scale
- **Link**: [arxiv.org/abs/2606.00422](https://arxiv.org/abs/2606.00422)
- **Authors**: Hanyu Li, Yi-Ping Hsu, Aditya Mantha et al.
- **Institution**: Pinterest
- **Abstract**: Unified generative framework for both retrieval and ranking stages at Pinterest's billion-scale production system.
- **Key Innovation**: Single model handles both stages end-to-end, simplifying industrial recommendation pipelines.
- **Tags**: `recommendation` `generative-retrieval` `ranking` `Pinterest`

### 21. SAILRec: Steering LLM Attention to Dual-Side Semantically Aligned Collaborative Embeddings
- **Link**: [arxiv.org/abs/2606.04514](https://arxiv.org/abs/2606.04514)
- **Authors**: Xi Wu, Jiale Wang, Zihan Wang et al.
- **Institution**: —
- **Abstract**: Steers LLM attention toward collaborative signals using semantically aligned embeddings on both user and item sides.
- **Key Innovation**: Collaborative-semantic alignment without sacrificing LLM representational power.
- **Tags**: `recommendation` `LLM` `collaborative-filtering` `semantic`

### 22. Beyond Retrieval: Learning Compact User Representations for Scalable LLM Personalization
- **Link**: [arxiv.org/abs/2606.04547](https://arxiv.org/abs/2606.04547)
- **Authors**: Heng Cao, Fan Zhang, Jian Yao et al.
- **Institution**: —
- **Abstract**: Compact user representations that enable LLM personalization without expensive retrieval over user history. Jointly learned with LLM.
- **Key Innovation**: Scales LLM personalization to millions of users by compressing user histories into learned representations.
- **Tags**: `recommendation` `personalization` `LLM` `scalability`

### 23. Time-Aware Diffusion based on Preference Disentanglement for Generative Recommendation
- **Link**: [arxiv.org/abs/2606.01670](https://arxiv.org/abs/2606.01670)
- **Authors**: Bangguo Zhu, Peng Huo, Yuanbo Zhao et al.
- **Institution**: —
- **Abstract**: Diffusion-based generative recommendation with disentangled time-aware preference components. Generates item sets rather than scoring.
- **Key Innovation**: Preference disentanglement enables controllable generation of recommendation lists with temporal awareness.
- **Tags**: `recommendation` `diffusion` `generative` `temporal`

### 24. Trustworthy Recommendation in the Era of Large Language Models
- **Link**: [arxiv.org/abs/2606.00540](https://arxiv.org/abs/2606.00540)
- **Authors**: Bohao Wang, Yu Cui, Zhenxiang Xu et al.
- **Institution**: —
- **Abstract**: Comprehensive survey on trustworthiness challenges in LLM-enhanced recommendation systems.
- **Key Innovation**: Covers fairness, privacy, robustness, transparency, and accountability dimensions.
- **Tags**: `recommendation` `LLM` `trustworthiness` `survey`

### 25. Synthetic Data from Cross-Domain Events for Large-Scale Recommendation Systems
- **Link**: [arxiv.org/abs/2606.00282](https://arxiv.org/abs/2606.00282)
- **Authors**: Xiangyu Wang, Yawen He, Shivendra Pratap Singh et al.
- **Institution**: —
- **Abstract**: Generates synthetic training data for recommendation by leveraging cross-domain event correlations.
- **Key Innovation**: Addresses data sparsity in industrial recommenders via cross-domain synthetic data generation.
- **Tags**: `recommendation` `synthetic-data` `cross-domain` `data-augmentation`

---

## Sequential Modeling

### 26. MARS: Multi-rate Aggregation of Recency Signals for Sequential Recommendation
- **Link**: [arxiv.org/abs/2606.03718](https://arxiv.org/abs/2606.03718)
- **Authors**: Zhenyu Yu, Shuigeng Zhou
- **Institution**: —
- **Abstract**: Aggregates recency signals at multiple timescales for sequential recommendation across sparse and dense interaction regimes.
- **Key Innovation**: Multi-rate signal processing view of sequential modeling — handles both short bursts and long-term patterns.
- **Tags**: `sequential-recommendation` `recency` `multi-scale`

### 27. BAHSD: Bridging Long-tail Gap via Adaptive Distillation in Black-box Sequential Recommendation
- **Link**: [arxiv.org/abs/2606.03091](https://arxiv.org/abs/2606.03091)
- **Authors**: Xi Zhou, Famin Wu, Mingming Li et al.
- **Institution**: —
- **Abstract**: Adaptive knowledge distillation from teacher to student for sequential recommendation targeting long-tail item coverage.
- **Key Innovation**: Explicitly addresses long-tail performance gap in black-box SR settings.
- **Tags**: `sequential-recommendation` `long-tail` `distillation` `black-box`

### 28. VirtualMLE: Virtual ML Engineer that Optimizes Sequential Recommenders
- **Link**: [arxiv.org/abs/2606.03221](https://arxiv.org/abs/2606.03221)
- **Authors**: Shiteng Cao, Jingwen Liu, Junda She, Zhiheng Li
- **Institution**: —
- **Abstract**: LLM-based agent that autonomously optimizes hyperparameters and architecture choices for sequential recommender systems.
- **Key Innovation**: First automated ML engineer specifically for recommendation system optimization.
- **Tags**: `sequential-recommendation` `AutoML` `LLM-agent`

---

## Games & Reinforcement Learning

### 29. Fog of Love: Affinity-based RL in a Game Environment
- **Link**: [arxiv.org/abs/2606.04750](https://arxiv.org/abs/2606.04750)
- **Authors**: Ajay Vishwanath, Christian Omlin
- **Institution**: —
- **Abstract**: Affinity-based reinforcement learning in a two-player multi-agent board game (Fog of Love). Agents balance competitive individual virtues and cooperative relationship.
- **Key Innovation**: Extends affinity-based RL from grid worlds to complex multi-agent game environments. Human-level interpretable behavior.
- **Tags**: `games` `multi-agent` `RL` `virtuous-AI`

### 30. MARLIN: Multi-Agent Game-Theoretic RL for Sustainable LLM Inference
- **Link**: [arxiv.org/abs/2605.13496](https://arxiv.org/abs/2605.13496)
- **Authors**: H. Moore, S. Qi, D. Milojicic, C. Bash, S. Pasricha
- **Institution**: —
- **Abstract**: Game-theoretic multi-agent RL to co-optimize TTFT, carbon emissions, water usage, and energy for LLM inference in cloud datacenters.
- **Key Innovation**: -18% TTFT, -33% carbon, -43% water, -11% energy vs. SOTA frameworks.
- **Tags**: `RL` `multi-agent` `sustainability` `LLM-inference`

### 31. Emergence of Exploration in Policy Gradient RL via Retrying
- **Link**: [arxiv.org/abs/2606.00151](https://arxiv.org/abs/2606.00151)
- **Authors**: Soichiro Nishimori, Paavo Parmas, Sotetsu Koyamada et al.
- **Institution**: —
- **Abstract**: Shows that exploration emerges naturally in policy gradient methods when agents are allowed to retry actions.
- **Key Innovation**: Formal analysis of retrying as an exploration mechanism — no explicit exploration bonus needed.
- **Tags**: `RL` `exploration` `policy-gradient` `theory`

### 32. Reinforcement Learning with Pairwise Preferences in Long-Term Decision Problems
- **Link**: [arxiv.org/abs/2606.00367](https://arxiv.org/abs/2606.00367)
- **Authors**: Jonathan Colaço Carr, Prakash Panangaden, Doina Precup, Benjamin Van Roy
- **Institution**: —
- **Abstract**: Theoretical framework for RL with pairwise preference feedback in long-horizon problems. Identifies conditions for learning from preferences alone.
- **Key Innovation**: Extends preference-based RL theory from bandits to full MDPs with guarantees.
- **Tags**: `RL` `preferences` `theory` `long-horizon`

### 33. ROGUE: Misaligned Agent Behavior Arising from Ordinary Computer Use
- **Link**: [arxiv.org/abs/2606.00341](https://arxiv.org/abs/2606.00341)
- **Authors**: Jeremy Tien, Abishek Anand, Yu-Rou Tuan et al.
- **Institution**: —
- **Abstract**: Documents and analyzes misaligned behaviors that emerge from LLM agents during ordinary computer use tasks.
- **Key Innovation**: Taxonomizes failure modes of computer-use agents; provides safety recommendations.
- **Tags**: `agents` `alignment` `safety` `computer-use`

---

## Agent Systems

### 34. On Effectiveness and Efficiency of Agentic Tool-calling and RL Training
- **Link**: [arxiv.org/abs/2606.00135](https://arxiv.org/abs/2606.00135)
- **Authors**: Tong Liu, Cheng Qian, Matej Cief et al. (ICML 2026)
- **Institution**: — (ICML 2026)
- **Abstract**: Systematic study of tool-calling efficiency and the impact of RL fine-tuning on agent tool use. ICML 2026.
- **Key Innovation**: Quantifies the trade-off between tool diversity and inference efficiency. RL improves tool selection accuracy.
- **Tags**: `agents` `tool-calling` `RL` `ICML26`

### 35. TAPS: Target-Aware Prefix Tree Selection for Diffusion-Drafted Speculative Decoding
- **Link**: [arxiv.org/abs/2606.00487](https://arxiv.org/abs/2606.00487)
- **Authors**: Zhuoyu Wang, Junnan Huang, Xinyu Chen
- **Institution**: —
- **Abstract**: Target-aware prefix tree for diffusion-drafted speculative decoding — uses diffusion models as drafters for AR LLM decoding.
- **Key Innovation**: Combines diffusion and AR models for efficient speculative decoding with prefix-tree-based candidate management.
- **Tags**: `LLM` `speculative-decoding` `diffusion` `inference-efficiency`

### 36. Deterministic Horizon: When Extended Reasoning Fails and Tool Delegation Becomes Necessary
- **Link**: [arxiv.org/abs/2606.00376](https://arxiv.org/abs/2606.00376)
- **Authors**: Dongxin Guo, Jikun Wu, Siu Ming Yiu (ICML 2026)
- **Institution**: — (ICML 2026)
- **Abstract**: Formal analysis of the limits of extended reasoning in LLMs. Characterizes problems where tool delegation is provably necessary.
- **Key Innovation**: ICML 2026. The "deterministic horizon" beyond which reasoning alone cannot guarantee correctness.
- **Tags**: `LLM` `reasoning` `tools` `theory` `ICML26`

### 37. CoMIC: Collaborative Memory and Insights Circulation for Long-Horizon LLM Agents
- **Link**: [arxiv.org/abs/2606.00756](https://arxiv.org/abs/2606.00756)
- **Authors**: Yannan Wang, Longli Yang, Zhen Liu et al.
- **Institution**: —
- **Abstract**: Collaborative memory system for long-horizon LLM agents in cloud-edge systems. Enables insight sharing across agent instances.
- **Key Innovation**: Memory circulation mechanism enables agents to learn from each other's experiences in distributed settings.
- **Tags**: `agents` `memory` `collaboration` `cloud-edge`

---

## Mixture-of-Experts

### 38. ProbMoE: Differentiable Probabilistic Routing for MoE
- **Link**: [arxiv.org/abs/2606.01509](https://arxiv.org/abs/2606.01509)
- **Authors**: Heng Hugo Zhao et al.
- **Institution**: —
- **Abstract**: Casts MoE routing as probabilistic inference over cardinality-constrained expert subsets. Uses SIMPLE gradient estimator.
- **Key Innovation**: Dynamic-k routing achieves competitive performance with fewer activated experts. Improved expert utilization and diversity.
- **Tags**: `MoE` `routing` `probabilistic` `dynamic-k`

### 39. DAG-MoE: From Simple Mixture to Structural Aggregation in MoE
- **Link**: [arxiv.org/abs/2606.01062](https://arxiv.org/abs/2606.01062)
- **Authors**: Jiarui Feng et al.
- **Institution**: —
- **Abstract**: Replaces weighted-summation expert aggregation with DAG-structured aggregation. Each expert gets distinct structural role; multi-step reasoning within a single MoE layer.
- **Key Innovation**: Expands expert combination space without modifying experts or router. Consistently outperforms standard MoE.
- **Tags**: `MoE` `aggregation` `DAG` `reasoning`

### 40. BitsMoE: Efficient Spectral Energy-Guided Bit Allocation for MoE LLM Quantization
- **Link**: [arxiv.org/abs/2606.00079](https://arxiv.org/abs/2606.00079)
- **Authors**: Jiayu Zhao, Zihan Teng, Minhao Fan et al.
- **Institution**: —
- **Abstract**: Spectral energy-guided bit allocation for MoE quantization. Higher-bit for high-energy experts, lower-bit for low-energy.
- **Key Innovation**: First quantization-aware MoE compression using spectral analysis. Superior perplexity vs. uniform quantization.
- **Tags**: `MoE` `quantization` `spectral` `compression`

---

## Meta

- **Search date**: 2026-06-08
- **Sources searched**: arXiv (Jun 2026 listings + web search), alphaXiv, arXivLabs
- **Categories covered**: cs.LG, cs.IR, cs.AI, cs.CL, cs.MA (Jun 2026)
- **Papers highlighted**: 40
