---
title: "arXiv Daily — 2026-08-27: LLM Event Tokenization, Generative Rec for Live-Streaming Ads, Native Multimodal CTR, Agent Memory Co-Evolution, Hamiltonian Sequential Rec, Agentic Game Dev for World Models, Spectral Ad Click Models"
type: synthesis
created: 2026-08-27
updated: 2026-08-27
tags: [arxiv, daily, llm, recommendation, ctr, advertising, sequential-modeling, agents, games, world-models, multimodal, generative-rec, event-tokenization, hamiltonian, live-streaming, cikm-2026, emnl-2026, daily-digest]
---

# arXiv Daily — 2026-08-27

Scanned 209 new cs.AI + 26 new cs.IR entries (Thu Aug 27 announcement wave) plus 21 cs.IR entries from Wed Aug 26. Focus: LLMs, recommendation, CTR, advertising, sequential modeling, agents, games, world models. Every paper ID verified absent from wiki index and same-day sibling digests.

---

## 🎯 CTR Prediction & Advertising

### 1. Native Multimodal Representation Learning for CTR Prediction in E-Commerce
| | |
|---|---|
| **Authors** | Chao Yi, Feifan Yang, Jiawei Feng, Sishuo Chen, Zhangming Chan, Xiang-Rong Sheng, Han Zhu |
| **Institution** | — |
| **arXiv** | [2608.24091](https://arxiv.org/abs/2608.24091) |
| **Venue** | CIKM 2026 |

**Abstract:** Multimodal representations have been widely adopted in industrial e-commerce recommendation systems. Current multimodal application frameworks follow a two-stage paradigm: pre-training a multimodal encoder on data from specific recommendation scenarios, then extracting items' multimodal representations and integrating them into the CTR prediction model. However, the training objectives and data distribution of multimodal pre-training tasks often differ from those of the CTR prediction task, which limits effectiveness on downstream tasks. The paper focuses on how to learn Native Multimodal Representation for the CTR prediction task. End-to-end training does not bring performance improvements because user behaviors in raw CTR data are driven by both multimodal semantics and non-multimodal factors, leading to ambiguous supervision and inconsistent encoder updates.

**Key Innovations:**
- Proposes **Mine-Then-Train**: mines high-quality, multimodally interpretable training samples from CTR data and uses them to fine-tune the multimodal encoder for better alignment with user click preferences
- Addresses the gap between multimodal pre-training objectives and CTR task objectives
- Demonstrates that raw end-to-end training fails due to ambiguous supervision from non-multimodal behavioral factors

---

### 2. TAGR: Temporally Adaptive Generative Recommendation for Industrial Live-Streaming Advertising
| | |
|---|---|
| **Authors** | Wencai Ye, Guangyi Liu, Chaoyi Wang, Wenbin Luo, Shengyu Wang, Mingjie Sun, Peng Wang, Quanming Yao, Wenjin Wu, Peng Jiang |
| **Institution** | — |
| **arXiv** | [2608.24034](https://arxiv.org/abs/2608.24034) |

**Abstract:** Live-streaming advertising is an important monetization channel on short-video and e-commerce platforms, where rapidly changing live content, promoted products, and user feedback impose strong freshness requirements on recommendation models. Existing generative recommenders designed for static domains fail at three levels: static semantic IDs (SID) cannot track evolving live ads; single-scale behavior modeling misses shifting intent; preference optimization conflicts between fresh on-policy feedback and training stability.

**Key Innovations:**
- **Live Semantic-Collaborative ID (LSID)**: periodically refreshes each active ad's SID based on its current live scene and promoted products, while retaining a stable hierarchical token vocabulary for autoregressive generation
- **Intent-Aware Generation (IAG)**: models live-room entry histories at multiple temporal granularities as the primary intent sequence, weights next-token prediction (NTP) using post-request intent evidence and business value
- **Intermittent On-Policy Preference Optimization (IOPO)**: periodically samples fresh candidate groups from the current policy and performs behavior- and value-aligned preference updates interleaved with supervised NTP maintenance
- **Industrial results**: +8.5% live-room entry rate, +7.4% shopping-cart click rate, +16.1% revenue lift

---

### 3. DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling in E-commerce Search
| | |
|---|---|
| **Authors** | Junzhao Zhang, Tao Zhang, Liren Yu, Feiyi Dong, Zhixuan Zhang, Dan Ou, Haihong Tang |
| **Institution** | — |
| **arXiv** | [2608.25635](https://arxiv.org/abs/2608.25635) |

**Abstract:** (Cross-listed cs.LG/cs.IR) Addresses long-term user value modeling in e-commerce search through direct causal effect optimization.

---

## 📊 Recommendation Systems

### 4. AMBER: An Event is Worth One Token — Event Tokenization for Industrial-scale LLM Recommendation
| | |
|---|---|
| **Authors** | Fan Xia, Zhaoheng Zheng, Iman Setayesh, Ruogu Lin, Yiqin Pan, Samarth Mittal, Wentao Bao, Vinti Pandey, Sachin Patil, Jianpeng Cheng, Jun Xiao, Zhuang Wang, Xiangjun Fan, Sri Reddy, Minghai Chen |
| **Institution** | — |
| **arXiv** | [2608.25546](https://arxiv.org/abs/2608.25546) |

**Abstract:** LLM-based recommendation has scaled along model capacity and sequence length, yet each position encodes only text, semantic IDs, or a few categorical features, discarding rich user, item, context, and outcome signals available at each event. Under autoregressive modeling, this yields weak queries at each position and, since each position becomes context for the next, the degradation compounds across the sequence.

**Key Innovations:**
- Introduces **snapshot resolution**: the amount of information encoded per event, as a new scaling dimension for LLM-based recommendation
- **AMBER (Autoregressive Modeling via Bottlenecked Event Representation)**: compresses each temporal snapshot into a compact Event Token, a new LLM input modality
- Event Tokens are pre-computed and cached for serving, decoupling snapshot resolution from real-time serving compute
- A single unified tokenizer outperforms dedicated per-entity tokenizers, demonstrating positive transfer across structurally different entity types
- Event Tokens also transfer across model architectures (non-LLM rankers)

---

### 5. Hamiltonian Spectral-Temporal Dissipative Dynamics for Sequential Recommendation (HSR)
| | |
|---|---|
| **Authors** | Shuiying Liao, P. Y. Mok |
| **Institution** | — |
| **arXiv** | [2608.25755](https://arxiv.org/abs/2608.25755) |

**Abstract:** Sequential recommendation requires understanding how user preferences evolve over time, yet most existing models treat such evolution as a first-order process where the next state depends solely on the current latent representation. Real user behavior often exhibits richer dynamics, including inertia, periodicity, and sudden shifts that cannot be fully captured by first-order assumptions.

**Key Innovations:**
- **Hamiltonian Spectral Recommender (HSR)**: recasts preference evolution as a dissipative Hamiltonian system in a latent phase space of position (stable preference) and momentum (short-term tendency)
- Linear time-invariant structure admits a **closed-form solution in the frequency domain**
- Learnable dissipation mechanism captures natural interest decay
- Short local impulse refinement module models abrupt behavioral fluctuations
- Consistently outperforms state-of-the-art Transformer-based and SSM-based recommenders on three benchmarks

---

### 6. TransRetrieval: Scaling Up Transformer-Based Retrieval for Industrial Recommendation
| | |
|---|---|
| **Authors** | Zhifei Zheng, Yunfei Liu, Bin Liu, Qiren Zhu, Hanbing Liu, Ziru Xu, Han Zhu, Jian Xu, Qi Qi, Bo Zheng |
| **Institution** | — |
| **arXiv** | [2608.25528](https://arxiv.org/abs/2608.25528) |
| **Venue** | CIKM 2026 |

**Abstract:** Industrial-scale transformer-based retrieval for recommendation systems.

---

### 7. RecGPT-Mobile-V2 Technical Report
| | |
|---|---|
| **Authors** | Lingqing Zhang, Bin Zhang, Weipeng Huang, Chengfei Lv, et al. (30 authors) |
| **Institution** | — |
| **arXiv** | [2608.24295](https://arxiv.org/abs/2608.24295) |

**Abstract:** Technical report for a GPT-based mobile recommendation system V2.

---

### 8. Rethinking Semantic Alignment in LLM-Enhanced Collaborative Filtering
| | |
|---|---|
| **Authors** | Yedong Jin, Shaowen Peng, Tsunenori Mine, Shoko Wakamiya, Eiji Aramaki |
| **Institution** | — |
| **arXiv** | [2608.24363](https://arxiv.org/abs/2608.24363) |

**Abstract:** Proposes a spectral decoupling approach to rethink semantic alignment in LLM-enhanced collaborative filtering.

---

### 9. CRAMER: Control via Request-Aware Masking for Editing Recommenders
| | |
|---|---|
| **Authors** | Zhiyuan Julian Su, Naihe Feng, Zhen Luther Qin, Ga Wu |
| **Institution** | — |
| **arXiv** | [2608.25370](https://arxiv.org/abs/2608.25370) |
| **Venue** | ICML 2026 |

**Abstract:** Request-aware masking for controlling and editing recommender system behavior.

---

### 10. MOTIF: Motivation-guided Topology Inference for Cold-start Multimodal Recommendation
| | |
|---|---|
| **Authors** | Yurui Shi, Yuchen Miao, Ximing Hu, Zijun Wang, Chang Han |
| **Institution** | — |
| **arXiv** | [2608.25381](https://arxiv.org/abs/2608.25381) |
| **Venue** | WISE 2026 |

**Abstract:** Addresses cold-start multimodal recommendation through motivation-guided topology inference.

---

### 11. D3ER: Multi-Modal Recommendation via Disentangle and Distillation-based Dynamic Ensemble
| | |
|---|---|
| **Authors** | Bingnan Wang, Yi Li, Xiongxin Tang, Fanjiang Xu, Jiangmeng Li |
| **Institution** | — |
| **arXiv** | [2608.25737](https://arxiv.org/abs/2608.25737) |
| **Venue** | ACMMM 2026 |

**Abstract:** Dynamic ensemble combining disentanglement and distillation for multi-modal recommendation.

---

### 12. Tlow: Flow-based Item Tokenizer for Recommendation
| | |
|---|---|
| **Authors** | Nian Li, Chonggang Song, Jingtao Ding, Lingling Yi, Yong Li, Qingmin Liao |
| **Institution** | — |
| **arXiv** | [2608.24176](https://arxiv.org/abs/2608.24176) |
| **Venue** | CIKM 2026 |

**Abstract:** Flow-based generative approach to item tokenization for recommendation.

---

### 13. SWIM: Step-Wise Integrated Measure for Session-supervised List Evaluation in Generative Re-ranking
| | |
|---|---|
| **Authors** | Yuanhao Pu, Chenghao Zhang, Chao Feng, Xunyong Yang, Xiang Li, Yongqi Liu, Defu Lian, Kaiqiao Zhan, Kun Gai |
| **Institution** | — |
| **arXiv** | [2608.25104](https://arxiv.org/abs/2608.25104) |

**Abstract:** Step-wise evaluation metric for generative re-ranking in list-wise settings.

---

### 14. Adaptive Item-based Collaborative Structures via Noise Rescheduling in Diffusion for Generative Recommendation
| | |
|---|---|
| **Authors** | Jiaqi Wang, Tianying Liu, Heng Chang, Jihong Guan, Wengen Li, Shuigeng Zhou |
| **Institution** | — |
| **arXiv** | [2608.23400](https://arxiv.org/abs/2608.23400) |

**Abstract:** Uses diffusion-based noise rescheduling to build adaptive collaborative structures for generative recommendation.

---

## 🤖 Agents & Multi-Agent Systems

### 15. HiPS: Learning What to Share and What to Personalize — Hierarchical Strategy Co-Evolution for Agent Memory
| | |
|---|---|
| **Authors** | Yupeng Han, Shuochen Liu, Kai Zhang, Ze Liu, Zhihong Pan, Xianquan Wang |
| **Institution** | — |
| **arXiv** | [2608.25329](https://arxiv.org/abs/2608.25329) |
| **Venue** | EMNLP 2026 Main |

**Abstract:** Memory-augmented agents maintain compact user profiles throughout extended conversations, enabling personalized and consistent responses without processing the entire dialogue history. Existing methods typically employ a static, one-size-fits-all strategy established before training. In practice, the optimal memory decision is inherently user-specific and dynamically evolves alongside policy optimization.

**Key Innovations:**
- **HiPS (Hierarchical Personalized Strategy)**: decouples memory management into a globally shared foundation and a user-specific adaptive tier
- **Universal Strategy**: extracts shared principles from cross-persona trajectories
- **Persona Delta Distillation**: generates tailored rules for users whose behaviors diverge from general patterns
- **Cross-Level Rule Flow**: dynamically calibrates boundaries by promoting broadly validated personal rules and demoting contradicted global ones
- Co-evolution loop where all strategy refinements are anchored to task outcomes

---

### 16. ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs
| | |
|---|---|
| **Authors** | Somgyuan Li, Ahmed M. Abdelmoniem, Shiqiang Wang |
| **Institution** | — |
| **arXiv** | [2608.25992](https://arxiv.org/abs/2608.25992) |
| **Venue** | EMNLP 2026 Findings |

**Abstract:** Online decision-making framework for orchestrating multi-agent LLM workflows with quality-cost tradeoffs.

---

### 17. Tunable Tool-Call Rates in LLM Agents via Representation Steering
| | |
|---|---|
| **Authors** | Yuqi Chen, Vincent Siu, Yang Liu, Dawn Song, Chenguang Wang |
| **Institution** | — |
| **arXiv** | [2608.25198](https://arxiv.org/abs/2608.25198) |

**Abstract:** Uses representation engineering to tune how often LLM agents call external tools.

---

### 18. CaSKG: Counterfactual-Causal Skill Graphs for Scalable Agent Skill Retrieval
| | |
|---|---|
| **Authors** | Zhiyuan Li, Linyuan Gao, Xuechun Ding, Hongwei Chen, Yuan Wu, Yi Chang |
| **Institution** | — |
| **arXiv** | [2608.25500](https://arxiv.org/abs/2608.25500) |

**Abstract:** Counterfactual-causal graph-based approach for scalable agent skill retrieval and composition.

---

### 19. Repair or Resample? Rethinking Failure Debugging in LLM Multi-Agent Systems
| | |
|---|---|
| **Authors** | Zhongwen Luan, Xiaoyu Zhang, Ming Hu, Yue Yang, Jiongchi Yu, Xiaohong Chen |
| **Institution** | — |
| **arXiv** | [2608.25920](https://arxiv.org/abs/2608.25920) |

**Abstract:** Rethinks failure debugging strategies in LLM multi-agent systems — whether to repair the failing agent or resample from the population.

---

## 🎮 Games & World Models

### 20. Agentic Game Development as a Verifiable Trajectory Data Engine for Scaling World Models
| | |
|---|---|
| **Authors** | Pengfei Zhou, Hexin Wang, Zhengfeiyang Zhang, Yixing Ma, Zhenglin Wan, Kaipeng Zhang, Wangbo Zhao, Yang You |
| **Institution** | — |
| **arXiv** | [2608.25518](https://arxiv.org/abs/2608.25518) |

**Abstract:** A common strategy for scaling world models is to train on more crawled video with more compute. We argue that this strategy is inefficient: scaling world models also requires a recursive data engine that offers grounded reward signals. The success of code agents illustrates why this matters — as code is executable, compilers and runtimes can provide high-quality rewards for RL post-training of LLMs. By contrast, spatial generation still relies largely on fuzzy proxies such as CLIP scores.

**Key Innovations:**
- Proposes **Reinforcement Learning with Human-Engine Verification (RLHEV)**: a post-training paradigm that combines dense engine signals (collision, physics, navigability, bounded playability) with implicit human acceptance feedback
- Game development provides a missing reward environment for spatial world models — scenes encoded by game engines are executable world specifications
- Provides real-world long-horizon trajectory data for RL post-training
- Addresses the fundamental gap between code agents (verifiable) and spatial world models (fuzzy reward signals)

---

### 21. Choose Your Game Wisely: Measuring Game-Theoretic Structures in Real-World Vehicle Interactions
| | |
|---|---|
| **Authors** | Yueyuan Li, Rongcheng Nie, Weijie Xi, Mingyang Jiang, Songan Zhang, Hanyang Zhuang, Ming Yang |
| **Institution** | — |
| **arXiv** | [2608.25917](https://arxiv.org/abs/2608.25917) |

**Abstract:** Measures and classifies game-theoretic structures in real-world vehicle interactions for autonomous driving.

---

## 🧠 LLM Training & Reasoning

### 22. AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs
| | |
|---|---|
| **Authors** | Sheng Liang, Yongyue Zhang, Nathanael Brian, Hang Lv, Hao Wang, Chen Zhang, Yong Liu |
| **Institution** | — |
| **arXiv** | [2608.26004](https://arxiv.org/abs/2608.26004) |
| **Venue** | EMNLP 2026 Main |

**Abstract:** Addresses the challenge that agentic LLMs have highly asymmetric contexts between prompt and generation, which makes standard speculative decoding ineffective.

---

### 23. ToST: A Tree-of-Thought Socratic Teaching Framework
| | |
|---|---|
| **Authors** | Feng Ling, Heng Yu |
| **Institution** | — |
| **arXiv** | [2608.25775](https://arxiv.org/abs/2608.25775) |

**Abstract:** Multi-path guidance and parallel thinking framework combining tree-of-thought with Socratic teaching methods.

---

### 24. Training Alignment Auditors via Reinforcement Learning
| | |
|---|---|
| **Authors** | Paul Rosu, Rowan Wang |
| **Institution** | — |
| **arXiv** | [2608.25460](https://arxiv.org/abs/2608.25460) |

**Abstract:** Uses RL to train auditors that can evaluate alignment of LLM outputs. 82-page comprehensive study.

---

### 25. Distance Is Not Enough: Forget-Retain Alignment Gap Predicts LLM Relearning Robustness
| | |
|---|---|
| **Authors** | Yi Chen, Hanna Hsieh, Shuhong Liu, Chuanbo Hua, Zihan Ma, Kun Wang, Joo-Young Kim |
| **Institution** | — |
| **arXiv** | [2608.25429](https://arxiv.org/abs/2608.25429) |
| **Venue** | EMNLP 2026 Main |

**Abstract:** Identifies that the alignment gap between forget and retain sets predicts LLM relearning robustness better than distance-based metrics.

---

## 🔄 Sequential Modeling

### 26. Auditing Return Conditioning as a Control Knob: An Offline Diagnostic for Decision Transformer Recommendation
| | |
|---|---|
| **Authors** | Jingyu Wang |
| **Institution** | — |
| **arXiv** | [2608.24815](https://arxiv.org/abs/2608.24815) |
| **Venue** | CONSEQUENCES '26 (RecSys 2026 Workshop) |

**Abstract:** Provides an offline diagnostic framework for understanding how return conditioning affects decision transformer-based recommendation.

---

### 27. RetrievalFormer: A Dual-Encoder Transformer for Efficient Approximate Nearest Neighbor Retrieval and Cold-Item Recommendation
| | |
|---|---|
| **Authors** | Theodore Rogers, Joe Standerfer, Dmitrii Timoshenko, Haoxue Li, Zuhaib Akhtar, Soyoung Yang |
| **Institution** | — |
| **arXiv** | [2608.24079](https://arxiv.org/abs/2608.24079) |

**Abstract:** Dual-encoder transformer architecture for efficient ANN retrieval with focus on cold-item recommendation.

---

## 🔧 Efficiency & Serving

### 28. PUMA: Post-Hoc Sparsification of Universal Multimodal Embeddings for Efficient Retrieval
| | |
|---|---|
| **Authors** | Matteo Attimonelli, Alessandro De Bellis, Franco Maria Nardini, Claudio Pomo, Cosimo Rulli, Rossano Venturini, Tommaso Di Noia |
| **Institution** | — |
| **arXiv** | [2608.25780](https://arxiv.org/abs/2608.25780) |

**Abstract:** Post-hoc sparsification method for universal multimodal embeddings to improve retrieval efficiency.

---

### 29. Hierarchical MoE for Multi-Modal ILD Diagnosis
| | |
|---|---|
| **Authors** | Alec K. Peltekian, Gorkem Durak, et al. |
| **Institution** | — |
| **arXiv** | [2608.25261](https://arxiv.org/abs/2608.25261) |
| **Venue** | MLMI @ MICCAI 2026 |

**Abstract:** Hierarchical Mixture-of-Experts architecture for multi-modal interstitial lung disease diagnosis.

---

## 📐 Benchmarks & Evaluation

### 30. Less can be More: Relieving RAG Bottlenecks via Evidence Frontloading and Pressure-Adaptive Budgeting
| | |
|---|---|
| **Authors** | Weibin Cai, Reza Zafarani |
| **Institution** | — |
| **arXiv** | [2608.25115](https://arxiv.org/abs/2608.25115) |

**Abstract:** Addresses RAG bottlenecks through evidence frontloading and adaptive budgeting strategies.

---

## 📌 Key Trends Today

1. **Event-level tokenization for LLM Rec**: AMBER (2608.25546) introduces "snapshot resolution" as a new scaling dimension — encoding full event information per position rather than just text/IDs
2. **Generative Rec goes live-streaming**: TAGR (2608.24034) shows temporally adaptive generative recommendation achieving +16.1% revenue in live-streaming advertising, with live-ad SID refresh and intermittent on-policy preference optimization
3. **Physics-inspired sequential rec**: HSR (2608.25755) recasts preference evolution as a Hamiltonian system with closed-form frequency-domain solutions, outperforming Transformers and SSMs
4. **Native multimodal CTR**: Mine-Then-Train (2608.24091) shows that end-to-end multimodal training fails for CTR due to ambiguous supervision — mining interpretable samples first is critical
5. **Agent memory co-evolution**: HiPS (2608.25329) decouples memory into global shared + user-specific tiers with cross-level rule flow, accepted at EMNLP 2026
6. **Game engines as world model reward**: RLHEV (2608.25518) proposes using game development as a verifiable trajectory data engine, bridging the gap between code agents (verifiable) and spatial world models (fuzzy rewards)
7. **Tool-call steering**: Representation steering (2608.25198) enables tunable tool-call rates in LLM agents without retraining
