---
title: "arXiv Daily Digest — 2026-07-08"
type: synthesis
created: 2026-07-08
updated: 2026-07-08
sources: []
tags: [arxiv-daily, llm, ctr, recommendation, rl, games, sequential-modeling]
---

# arXiv Daily Digest — 2026-07-08

> Curated from cs.AI, cs.LG, cs.IR, cs.MA, cs.CL submissions on Wed, 8 Jul 2026.

---

## LLMs & Foundation Models

### 1. DepthWeave-KV: Token-Adaptive Cross-Layer Residual Factorization for Long-Context KV Cache Compression
- **Authors**: Anna Cordoba, Adam Puente Tercero, Nerea Angulo Hijo et al.
- **arXiv**: [2607.06523](https://arxiv.org/abs/2607.06523)
- **Abstract**: Proposes a token-adaptive cross-layer residual factorization method for KV cache compression in long-context LLM inference, reducing memory overhead while preserving quality.
- **Key Innovation**: Token-adaptive depth-wise KV compression using residual factorization across layers.

### 2. FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference
- **Authors**: Anna Córdoba, Adam Puente Tercero, Nerea Angulo Hijo et al.
- **arXiv**: [2607.06519](https://arxiv.org/abs/2607.06519)
- **Abstract**: Frequency-domain analysis guides which depth layers can share KV representations, achieving robust compression for long-context inference.
- **Key Innovation**: Frequency-guided depth sharing — compresses KV cache by identifying redundant layers via frequency analysis.

### 3. A Definition and Roadmap for World Models
- **Authors**: Xinyuan Chen, Haoyu Guo, Shi Guo, Bingqi Jiang, Chunhua Shen et al.
- **arXiv**: [2607.06401](https://arxiv.org/abs/2607.06401)
- **Institution**: Multiple (academic + industry)
- **Abstract**: A comprehensive technical report providing a formal definition of world models and a roadmap for future research, spanning model-based RL, video generation, and physical reasoning.
- **Key Innovation**: Unified definition and taxonomy of world models; 58-page survey + roadmap.

### 4. ProtoType Language Models
- **Authors**: Dan Ley, Giang Nguyen, Himabindu Lakkaraju, Julius Adebayo
- **arXiv**: [2607.00510](https://arxiv.org/abs/2607.00510)
- **Abstract**: Introduces prototype-based interpretable language models that classify based on similarity to learned prototypes rather than opaque deep representations.
- **Key Innovation**: Case-based reasoning for LMs — interpretable by design via prototype matching.

---

## CTR Prediction & Advertising

### 5. Dual-Stream MLP is All You Need for CTR Prediction
- **Authors**: Kesha Ou et al. (RUCAIBox)
- **arXiv**: [2606.04944](https://arxiv.org/abs/2606.04944)
- **Institution**: Renmin University of China
- **Abstract**: Proposes DS-MLP, a dual-stream MLP framework using knowledge distillation to combine explicit and implicit feature interactions. Despite being vanilla MLP, achieves SOTA across 3 benchmarks.
- **Key Innovation**: Knowledge distillation consolidates explicit feature interaction learning into a main MLP; alignment strategies balance dual streams.
- **Published**: TKDD 2026

### 6. IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs
- **Authors**: Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan et al.
- **arXiv**: [2603.01590](https://arxiv.org/abs/2603.01590)
- **Institution**: Xiaohongshu Inc.
- **Abstract**: Uses MLLMs to generate proxy embeddings from content signals for cold-start items, aligned with ID embedding space and optimized end-to-end under CTR objectives. Deployed in production at Xiaohongshu.
- **Key Innovation**: MLLM-generated proxy embeddings replace ID embeddings for cold-start; deployed in a 300M+ MAU platform.

### 7. CADET: Context-Conditioned Ads Decoder-Only Transformer for CTR Prediction
- **Authors**: T. Song, L. Hertel, Y.J. Yun et al. (LinkedIn)
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Institution**: LinkedIn
- **Abstract**: A decoder-only transformer architecture for ads CTR prediction that handles post-scoring contextual signals and maintains offline-online consistency. Deployed at LinkedIn scale.
- **Key Innovation**: First decoder-only transformer for ads CTR; handles context conditioning and industrial-scale serving.

### 8. GenLI: Generative Long-term User Interest Modeling for CTR Prediction
- **Authors**: Jiangli Shao, Kaifu Zheng, Hao Fang et al.
- **arXiv**: [2605.15905](https://arxiv.org/abs/2605.15905)
- **Abstract**: Replaces two-stage retrieval with a generative approach: generates multiple interest distributions from short-term behavior, then retrieves via O(1) lookup.
- **Key Innovation**: Target-independent interest generation with O(1) behavior retrieval; avoids pairwise similarity computation.

---

## Recommendation Systems

### 9. HGenPush: Heterogeneous Generative Recommendation Architecture for Industrial Push Notification Systems
- **Authors**: Xiao Liang, Jiali Feng et al.
- **arXiv**: [2607.03362](https://arxiv.org/abs/2607.03362)
- **Abstract**: Heterogeneous generative architecture for push notification recommendations in industrial settings.
- **Key Innovation**: Generative recommendation for push notifications with heterogeneous user-item signals.

### 10. Autonomous Information Seeking: A Roadmap for Agentic Recommender Systems
- **Authors**: Xinyu Lin, Yashar Deldjoo, Sunhao Dai et al.
- **arXiv**: [2607.04433](https://arxiv.org/abs/2607.04433)
- **Abstract**: Roadmap paper defining agentic recommender systems that autonomously seek information on behalf of users, moving beyond reactive filtering.
- **Key Innovation**: Taxonomy and research roadmap for agentic RS — systems that proactively gather information.

### 11. LBR: Towards Mitigating Length Bias in Large Language Models for Recommendation
- **Authors**: Hongchen Li, Bohao Wang et al.
- **arXiv**: [2607.04270](https://arxiv.org/abs/2607.04270)
- **Abstract**: Identifies and mitigates length bias in LLMs used for recommendation (models prefer longer textual descriptions).
- **Key Innovation**: Debiasing technique for LLM-based recommenders against text length confounders.

### 12. Beyond Item Order: Temporal Gap Tokenization for Generative Recommendation with Semantic IDs
- **Authors**: Chengkai Huang, Tianqi Gao et al.
- **arXiv**: [2607.03918](https://arxiv.org/abs/2607.03918)
- **Abstract**: Tokenizes temporal gaps between user interactions for generative sequential recommendation with semantic item IDs.
- **Key Innovation**: Temporal gap tokenization improves sequential modeling in generative recommenders.

---

## Sequential Modeling & Time Series

### 13. RMISC: A Large-scale Real-world Multivariate Corpus for Time Series Foundation Models
- **Authors**: Qian Sun, Yong-Ming Tian et al.
- **arXiv**: [2607.06504](https://arxiv.org/abs/2607.06504)
- **Abstract**: A large-scale, real-world multivariate time series corpus designed for training and evaluating time series foundation models.
- **Key Innovation**: First large-scale real-world multivariate corpus purpose-built for TS foundation models.

---

## Reinforcement Learning & Games

### 14. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: P. Qi, D. Balcells, M. Liu et al.
- **arXiv**: [2506.24119](https://arxiv.org/abs/2506.24119)
- **Institution**: Multiple (academic)
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games against themselves. Uses role-conditioned advantage estimation (RAE). Improves reasoning by up to 10% across 8 benchmarks. Accepted at ICLR 2026.
- **Key Innovation**: Zero-sum games as a training signal for LLM reasoning; multi-agent multi-turn RL without human supervision.

### 15. FootsiesGym: A Fighting Game Benchmark for Two-Player Zero-Sum Imperfect-Information Games
- **Authors**: Chase McDonald, Nathan Tsang, Wesley N. Kerr
- **arXiv**: [2607.06514](https://arxiv.org/abs/2607.06514)
- **Abstract**: A lightweight fighting game environment (Footsies) adapted as a benchmark for RL algorithms in zero-sum imperfect-information settings.
- **Key Innovation**: Simplified fighting game benchmark; accepted at RLC 2026 RL & Video Games Workshop.

### 16. Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini et al.
- **arXiv**: [2606.20210](https://arxiv.org/abs/2606.20210)
- **Institution**: EA / Academic
- **Abstract**: Vision paper from Conference on Games 2026 describing real RL deployments in games (e.g., EA SPORTS FC 25 goalkeeper AI), bottlenecks (sample efficiency, believability vs optimality), and a readiness framework.
- **Key Innovation**: Genre-level readiness framework; production deployment details for RL game AI.

### 17. Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Turn Games
- **Authors**: (Multiple)
- **arXiv**: (May 2026)
- **Abstract**: Uses RL to teach LLMs strategic reasoning through multi-turn game playing, learning from win/loss feedback rather than static data.
- **Key Innovation**: RL-based strategic reasoning training for LLMs using game outcomes as reward signal.

---

## Multi-Agent Systems

### 18. StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems
- **Authors**: Sergey Volkov, Yang Li, Ye Luo
- **arXiv**: [2607.05844](https://arxiv.org/abs/2607.05844)
- **Abstract**: A memory system for multi-agent LLM systems that deterministically preserves conflict information across agent interactions.
- **Key Innovation**: Conflict-preserving memory ensures agents can detect and resolve contradictory information.

### 19. Doomed from the Start: Early Abort of LLM Agent Episodes via a Recall-Controlled Probe Cascade
- **Authors**: Kai Ruan, Zihe Huang et al.
- **arXiv**: [2607.06503](https://arxiv.org/abs/2607.06503)
- **Abstract**: Early episode termination for LLM agents using a lightweight probe cascade, saving compute on doomed trajectories.
- **Key Innovation**: Probe-based early abort for agent episodes — compute-efficient agent execution.

---

## Retrieval & Search (IR)

### 20. UniSGR: Unified Framework for Semantic ID Generation and Ranking
- **Authors**: Jiawei Sun, Jun Yang et al.
- **arXiv**: [2607.04068](https://arxiv.org/abs/2607.04068)
- **Abstract**: Unified framework that jointly generates semantic IDs and performs ranking, bridging generative retrieval and learning-to-rank.
- **Key Innovation**: Joint semantic ID generation + ranking in a single end-to-end framework.

### 21. Long-Term Optimization for Large-Scale Generative Retrieval with Off-Policy REINFORCE
- **Authors**: Artem Matveev, Sergei Makeev et al.
- **arXiv**: [2607.02818](https://arxiv.org/abs/2607.02818)
- **Abstract**: Applies off-policy REINFORCE to optimize generative retrieval models for long-term metrics rather than immediate relevance. Accepted at KDD 2026 Workshop.
- **Key Innovation**: Off-policy RL for long-term optimization of generative retrieval.

### 22. SCOReD: Student-Aware CoT Optimization for Recommendation Distillation
- **Authors**: Haz Sameen Shahgir, Yufei Li et al.
- **arXiv**: [2607.05734](https://arxiv.org/abs/2607.05734)
- **Abstract**: Chain-of-thought optimization for distilling recommendation models, where the teacher generates reasoning traces tailored to student capability.
- **Key Innovation**: Student-aware CoT distillation improves recommendation model compression.

---

## Trends Summary

| Theme | Signal | Key Papers |
|-------|--------|------------|
| **Generative CTR/Rec** | Strong — generative approaches replacing two-stage retrieval | GenLI, HGenPush, GenCTR |
| **LLM for Cold-Start** | Strong — MLLMs generate embeddings for new items | IDProxy |
| **Long-Context Efficiency** | Very strong — multiple KV cache compression papers | DepthWeave-KV, FreqDepthKV |
| **Game-Based RL for Reasoning** | Emerging — zero-sum games as training signal for LLMs | SPIRAL, Strat-Reasoner |
| **Agentic Systems** | Strong — proactive agentic recommenders and multi-agent memory | Autonomous Info Seeking, StateFuse |
| **World Models** | Resurging — formal definition and roadmap paper | World Models Roadmap |
| **Time Series Foundation Models** | Growing — large-scale benchmarks and pre-training | RMISC Corpus |

---

*Generated: 2026-07-08 | Sources: arXiv cs.AI, cs.LG, cs.IR, cs.MA, cs.CL*
