---
title: arXiv Paper Check — AI & CTR (June 9, 2026)
type: synthesis
created: 2026-06-09
updated: 2026-06-09
sources: []
tags: [arxiv, paper-check, AI, CTR, IR, agents, LLM]
---

# arXiv Paper Check — AI & CTR (June 9, 2026)

Survey of new submissions on arXiv (Mon, 8 Jun 2026). Sources: cs.AI (34 new, 287 total), cs.IR (14 new, 26 total).

---

## 🏆 Top Picks

### 1. Lean4Agent: Formal Modeling and Verification for Agent Workflow and Trajectory
- **arXiv**: [2606.06523](https://arxiv.org/abs/2606.06523)
- **Authors**: Ruida Wang, Jerry Huang, Pengcheng Wang, Xuanqing Liu, Luyang Kong, Tong Zhang
- **Key Contribution**: First framework using Lean4 (dependent-type formal language) to formally model and verify agent behavior. Introduces FormalAgentLib for semantic consistency verification and LeanEvolve for workflow revision. Verified workflows outperform failing ones by 11.94% on SWE-Bench-Verified. A new direction for agent reliability.

### 2. Position: Don't Just "Fix it in Post" — A Science of AI Must Study Training Dynamics
- **arXiv**: [2606.06533](https://arxiv.org/abs/2606.06533)
- **Authors**: Stella Biderman, Mohammad Aflah Khan, Niloofar Mireshghallah, Catherine Arnett, Fazl Barez, Naomi Saphra
- **Key Contribution**: ICML 2026 Oral. Argues AI research must move beyond post-hoc analysis to study training dynamics. Challenges the field to predict capabilities/biases from early training signals, intervene when trajectories go wrong, and design training procedures for desired properties. Grounded in philosophy of science.

### 3. OpenSkill: Open-World Self-Evolution for LLM Agents
- **arXiv**: [2606.06741](https://arxiv.org/abs/2606.06741)
- **Authors**: Zhiling Yan, Dingjie Song, Hanrong Zhang, Wei Liang, Yuxuan Zhang, Yutong Dai, Lifang He, Philip S. Yu, Ran Xu, Xiang Li, Lichao Sun
- **Key Contribution**: Agents that bootstrap skills and verification signals from scratch using open-world resources (docs, repos, web) with zero target-task supervision. Builds virtual tasks from self-constructed verification anchors. Skills transfer across models without adaptation.

### 4. GBLA: Gated Bidirectional Linear Attention for Generative Retrieval
- **arXiv**: [2606.07317](https://arxiv.org/abs/2606.07317) (SIGIR 2026)
- **Authors**: Artem Matveev, Vladislav Tytskiy, Sergei Makeev, Sergei Liamaev (Yandex)
- **Key Contribution**: Linear-time bidirectional attention layer extending kernelized attention with Conv1D mixing, key gating, and gated RMSNorm. Hybrid 1:2 SA:GBLA matches full self-attention quality. **8.2× single-layer speedup at 32K history length vs FlashAttention-v3.** Critical for long user histories in recommendation.

### 5. AEGIS: A Backup Reflex for Physical AI
- **arXiv**: [2606.06660](https://arxiv.org/abs/2606.06660)
- **Authors**: Josef Chen
- **Key Contribution**: Lightweight probe on weak policy activations detects high-risk steps and escalates to stronger policy only when needed. On LIBERO-Spatial, recovers 10.1% of lost trajectories vs 4.6% for blind escalation. Stronger policy activated on only 38% of steps. Pre-registered with explicit kill criteria.

### 6. Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety
- **arXiv**: [2606.06529](https://arxiv.org/abs/2606.06529)
- **Authors**: Catherine Ge-Wang, Tyler Crosse, Benjamin Hadad IV, Joachim Schaeffer, Ram Potham, Tyler Tracy
- **Key Contribution**: Strategic attackers that choose *when* to attack bypass safety monitors. Start policy reduces safety by 20pp on BashArena/LinuxArena; stop policy by 20-28pp. Existing control evaluations may overestimate safety against selective attackers.

### 7. DyCon: Dynamic Reasoning Control via Evolving Difficulty Modeling
- **arXiv**: [2606.07108](https://arxiv.org/abs/2606.07108) (ICML 2026)
- **Authors**: Tengyao Tu, Yulin Li, Hui-Ling Zhen, Libo Qin, Zhoujun Wei, Jinghua Piao, Zhuotao Tian, Yong Li, Min Zhang
- **Key Contribution**: Training-free framework using latent step-level embeddings to model dynamically evolving task difficulty. Controls reasoning depth to mitigate "overthinking." Works across 4B–32B models on math, QA, and coding (12 benchmarks).

### 8. DREAM: Dynamic Refinement of Early Assignment Mappings for Generative Recommendation
- **arXiv**: [2606.06947](https://arxiv.org/abs/2606.06947)
- **Authors**: Liwei Guan, Huanjie Wang, Hongwei Zhang, Linxun Chen, Zhaojie Liu
- **Key Contribution**: Identifies static semantic ID assignment as fundamental cold-start bottleneck in generative recommendation. Three-stage framework: intent-aware tokenizer, frozen backbone as evaluator, dynamic beam for multiple weighted SID hypotheses. Strong gains on Amazon benchmarks.

### 9. Bradley-Terry Rankings for Recommender Systems Across Dataset Taxonomies
- **arXiv**: [2606.07492](https://arxiv.org/abs/2606.07492) (KDD 2026)
- **Authors**: Ekaterina Grishina, Stepan Kuznetsov, Askar Tsyganov, Ilya Ivanov, Daria Korovaitceva, Margarita Rusanova, Uliana Parkina, Alexander Derevyagin, Evgeny Frolov, Sergey Samsonov, Anton Lysenko
- **Key Contribution**: Data-driven ranking methodology using Bradley-Terry model for recommender comparison. Shows ranking depends on key dataset statistics. Enables predicting algorithm rankings on **unseen datasets** without running models (BT trees, BT with covariates).

### 10. RISE: Retrieving Interaction Spaces for Agentic Search
- **arXiv**: [2606.06880](https://arxiv.org/abs/2606.06880)
- **Authors**: Shengyao Zhuang, Yuansheng Ni, Hengxin Fun, Jimmy Lin, Xueguang Ma
- **Key Contribution**: New paradigm: retrieval for agents should construct a bounded *interaction space* (with shell tools) rather than just selecting documents. BM25-based boundary + document processing for shell navigation. Matches DCI at 78% accuracy at roughly 1/4 per-query cost on BrowseComp-Plus.

---

## 📋 Additional Notable Papers

### AI / Agents
| arXiv | Title | Authors |
|-------|-------|---------|
| [2606.06787](https://arxiv.org/abs/2606.06787) | AdMem: Advanced Memory for Task-solving Agents | Runzhe Wang et al. |
| [2606.06976](https://arxiv.org/abs/2606.06976) | TRUST: Tool-Calling via Uncertainty-Aligned RL | Yijin Zhou et al. |
| [2606.07017](https://arxiv.org/abs/2606.07017) | The Sim-to-Real Gap of Foundation Model Agents (KDD 2026 Blue Sky) | Xiaoou Liu et al. |
| [2606.07157](https://arxiv.org/abs/2606.07157) | Discovering Implicit Knowledge Deficiencies in LLMs via Proactive Q&A | Jiashu Xu et al. |
| [2606.07299](https://arxiv.org/abs/2606.07299) | DuMate-DeepResearch: Multi-Agent with Recursive Search | Lingyong Yan et al. (Baidu) |
| [2606.06923](https://arxiv.org/abs/2606.06923) | Declarative Skills for AI Agents in Knowledge-Grounded Tool-Use | M. Danish Lim et al. |
| [2606.07027](https://arxiv.org/abs/2606.07027) | StainFlow: Entity-Stain Tracking for Process Rewards in GUI Agents | Haojie Hao et al. |
| [2606.06893](https://arxiv.org/abs/2606.06893) | W2S: Workflow-to-Skill via Routing-Workflow-Semantics Decomposition | Yuyang Zhang et al. |

### IR / Recommendation / CTR
| arXiv | Title | Authors |
|-------|-------|---------|
| [2606.06779](https://arxiv.org/abs/2606.06779) | Mind the Gap: Bridging Behavioral Silos with LLMs in Multi-Vertical Rec | Nimesh Sinha et al. (DoorDash) |
| [2606.06970](https://arxiv.org/abs/2606.06970) | SSRLive: Live Streaming with Dynamic Semantic ID | Teng Shi et al. |
| [2606.07075](https://arxiv.org/abs/2606.07075) | CaLIR: Category-Guided Latent Intent Reasoning for E-Commerce Gen Retrieval | Fuwei Zhang et al. |
| [2606.07454](https://arxiv.org/abs/2606.07454) | PaperFlow: Profiling, Recommending, Adapting Across Daily Paper Streams | Fuqiang Wang et al. |
| [2606.07235](https://arxiv.org/abs/2606.07235) | FLOWREADER: Min-Cost Flow for Multi-Modal Long Document QA | Ambuj Mehrish, Sebatiano Vascon |
| [2606.07252](https://arxiv.org/abs/2606.07252) | Constrained Dominant Sets for Multimodal Document QA | Ambuj Mehrish, Sebatiano Vascon |
| [2606.07218](https://arxiv.org/abs/2606.07218) | HKVM-RAG: Key-Value-Separated Hypergraph Evidence for Multi-Hop RAG | Mingyu Zhang, Ying Ma |
| [2606.07187](https://arxiv.org/abs/2606.07187) | RISE: A Rust Library for Inverted Index Search Engines | Angelo Savino, Rossano Venturini |
| [2606.07317](https://arxiv.org/abs/2606.07317) | GBLA: Gated Bidirectional Linear Attention for Generative Retrieval (SIGIR 2026) | Artem Matveev et al. (Yandex) |

---

## 📊 Summary

| Category | Count | Top Venues |
|----------|-------|------------|
| AI / Agents / LLM | ~18 new | ICML 2026, arXiv cs.AI |
| IR / Recommendation / CTR | ~16 new | SIGIR 2026, KDD 2026, arXiv cs.IR |
| **Total unique papers surveyed** | **34 cs.AI + 14 cs.IR new submissions** | |

**Key trends from today's batch:**
- **Formal verification for agents** — Lean4Agent opens a new direction using dependent-type theorem provers for agent reliability
- **Training dynamics as a science** — ICML 2026 Oral argues for fundamental shift in how we study AI
- **Self-evolving agents** — OpenSkill bootstraps skills from zero supervision; W2S automates skill construction from traces
- **Linear attention for long sequences** — GBLA (SIGIR 2026) achieves 8.2× speedup over FlashAttention-v3 at 32K length
- **Generative recommendation maturation** — DREAM solves cold-start SID bottleneck; SSRLive deploys dynamic SIDs in live streaming
- **Safety realism** — Attack selection paper shows strategic attackers break current control evaluations; AEGIS provides pragmatic escalation for robot failures
- **Agentic search paradigm** — RISE reframes retrieval as constructing interaction spaces rather than document selection
