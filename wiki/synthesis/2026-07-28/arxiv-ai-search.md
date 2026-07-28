# arXiv AI/ML/RecSys/Ads Research Report — 2026-07-28

Generated from arXiv submissions (cs.IR, cs.LG, cs.AI, cs.CL) for the week of Jul 21–28, 2026.

---

## 1. Generative Recommendation

### 1.1 Diffusion Language Model for Recommendation (DLMRec)
| Field | Detail |
|---|---|
| **Title** | Diffusion Language Model for Recommendation |
| **Authors** | Chengyi Liu, Yongqi Zhou, Junwei Pan, Zhixiang Feng, Chengguo Yin, Haijie Gu, Jie Jiang, Yinghao Liu, Yujuan Ding, Qing Li, Wenqi Fan |
| **Institution** | Not explicitly stated (multiple authors) |
| **Abstract** | LLM-powered recommender systems leverage semantic reasoning for generative recommendation but autoregressive paradigms are suboptimal—next-token objectives emphasize sequential order over structural inter-item dependencies, and prefix-constrained generation causes error accumulation. DLMRec is a discrete diffusion language model tailored for recommendation, introducing a collaborative-aware stochastic tokenizer, curriculum-driven training strategy, and stability-aware voting mechanism. |
| **Key Innovations** | 1) Collaborative-aware stochastic tokenizer encoding multi-hop collaborative signals into discrete tokens for diffusion modeling. 2) Curriculum-driven training aligning denoising with preference recovery via progressive item- and token-level learning. 3) Stability-aware voting mechanism for consistent iterative predictions. |
| **Link** | [arXiv:2607.21519](https://arxiv.org/abs/2607.21519) |
| **Date** | 2026-07-23 |

### 1.2 Bridging the Structural Gap: Adapting Autoregressive Generation for Recommendation (BARGE)
| Field | Detail |
|---|---|
| **Title** | Bridging the Structural Gap: Adapting Autoregressive Generation for Recommendation |
| **Authors** | Junchao Zeng, Junzhang Zhu, Junyang Chen, Yudong Li, Wei Liu, Chengxiang Zhuo, Zang Li |
| **Institution** | Tencent |
| **Abstract** | Generative Recommendation encodes items into hierarchical semantic IDs via residual quantization but flattening multi-token IDs destroys item-level structure and causes semantic drift. BARGE employs Item Context-Aware Attention (ICA) and Hierarchical Path Reranking (HPR) with Dual-Path Decoding (DPD). Online A/B test on Tencent shows +0.60% CTR, +1.34% click-UV, +1.70% total reading time. |
| **Key Innovations** | 1) Item Context-Aware Attention restores item-level structure during encoding. 2) Hierarchical Path Reranking + Dual-Path Decoding suppress semantic drift from complementary angles. 3) Industrial-scale validation on Tencent platform. |
| **Link** | [arXiv:2607.21028](https://arxiv.org/abs/2607.21028) |
| **Date** | 2026-07-23 |

### 1.3 Controllable and Content-Based Recommendations (CCBR)
| Field | Detail |
|---|---|
| **Title** | Controllable and Content-Based Recommendations |
| **Authors** | Fırat Öncel, Jihoon Jeong, Emiliano Penaloza, Mirco Ravanelli, Laurent Charlin, Cem Subakan |
| **Institution** | Not explicitly stated |
| **Abstract** | CCBR builds recommendations from textual user profile representations instead of latent dense representations, plugging into collaborative filtering models with controllability via text bottlenecks. Enables text-based and multimodal interventions allowing users to steer the model. Works across image-, audio-, and video-based datasets, outperforming TEARS baseline. |
| **Key Innovations** | 1) Text bottleneck for interpretable, controllable recommendations. 2) Direct inference of text summaries from item contents (images, audio, video). 3) Multimodal user steering mechanism via systematic interventions. |
| **Link** | [arXiv:2607.20938](https://arxiv.org/abs/2607.20938) |
| **Date** | 2026-07-23 |

### 1.4 Personalized Recommendation Tool Learning via Autonomous Language Agents (PRTA)
| Field | Detail |
|---|---|
| **Title** | Personalized Recommendation Tool Learning via Autonomous Language Agents |
| **Authors** | Mingdai Yang, Zhiwei Liu, Weizhi Zhang, Yibo Wang, Hao Peng, Philip Yu |
| **Institution** | Not explicitly stated (accepted RecSys 2026) |
| **Abstract** | LLM-based agents suffer from hallucination and context-length limitations for full-ranking. PRTA has an LLM act as central planner interacting with multiple recommendation models as tools. The agent performs high-level reasoning and personalized tool selection, while traditional models handle full-ranking. Reflection mechanisms evaluate and compare tools per user. |
| **Key Innovations** | 1) Agent-based framework where LLM orchestrates multiple RecSys models as tools. 2) Reflection mechanisms for personalized tool selection per user. 3) Avoids hallucination by offloading scoring to traditional models. |
| **Link** | [arXiv:2607.19739](https://arxiv.org/abs/2607.19739) |
| **Date** | 2026-07-22 |

---

## 2. CTR Prediction & Ad Ranking

### 2.1 Long-History User Transformers for Real-Time Ad Ranking
| Field | Detail |
|---|---|
| **Title** | Long-History User Transformers for Real-Time Ad Ranking |
| **Authors** | Viacheslav Ovchinnikov, Georgii Smirnov, Nikolai Savushkin, Veronika Ivanova, Maksim Kuzin |
| **Institution** | Yandex |
| **Abstract** | Long interaction histories are informative for CTR but ads must be scored within hundreds of milliseconds. This paper decouples history encoding from real-time inference: a high-capacity offline transformer encodes full cross-surface interaction history into a compact cached representation, while a lightweight runtime model combines it with recent events and request context. Offline encoder pre-trained with dual objective (feedback + next-item prediction). Recovers 72-80% quality of full-history runtime transformer. Production A/B: +2.77% ranking metric in search ads, +2.1% on Yandex Ad Network, revenue gains +2.26% / +0.43%. |
| **Key Innovations** | 1) Decoupled offline/online architecture for long-history encoding. 2) Dual-objective pre-training (feedback + next-item prediction). 3) Cached representation robust to staleness, enabling cheap refresh. |
| **Link** | [arXiv:2607.14331](https://arxiv.org/abs/2607.14331) |
| **Date** | 2026-07-15 |

### 2.2 Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)
| Field | Detail |
|---|---|
| **Title** | Dual-Stream MLP is All You Need for CTR Prediction |
| **Authors** | Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen |
| **Institution** | Renmin University of China |
| **Abstract** | Existing dual-stream CTR architectures face high complexity and imbalance between explicit/implicit modules. DS-MLP uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP network, while a parallel MLP captures implicit interactions. Achieves SOTA across three benchmarks with a vanilla MLP structure. Accepted by TKDD. |
| **Key Innovations** | 1) Knowledge distillation to distill complex feature interactions into a simple MLP. 2) Dual parallel MLP streams for explicit + implicit interactions. 3) Two alignment strategies for MLP component compatibility. |
| **Link** | [arXiv:2606.04944](https://arxiv.org/abs/2606.04944) |
| **Date** | 2026-06-03 |

### 2.3 LO-FAR: A Cost-Aware Local Filter for Sparse Feature Ranking in Industrial Ad Recommendation
| Field | Detail |
|---|---|
| **Title** | LO-FAR: A Cost-Aware Local Filter for Sparse Feature Ranking in Industrial Ad Recommendation |
| **Authors** | Egemen Erbayat, Luis Duque, Sohini Roychowdhury, Mohammad Amin, Srihari Reddy |
| **Institution** | Not explicitly stated |
| **Abstract** | Industrial ad recommendation relies on sparse, high-cardinality ID-list features backed by dedicated embedding tables. LO-FAR is a CPU-only, model-agnostic workflow ranking each candidate feature from its stand-alone held-out predictive signal using lightweight local estimators. Completes ranking in ~2 CPU-hours on 1M+ logged interactions and 475 sparse features, preserving NE gains competitive with heavier methods. RecSys 2026. |
| **Key Innovations** | 1) CPU-only, model-agnostic feature ranking workflow. 2) Lightweight local estimators replacing GPU-bound retraining loops. 3) Practical production deployment with ~2 CPU-hour turnaround. |
| **Link** | [arXiv:2607.20873](https://arxiv.org/abs/2607.20873) |
| **Date** | 2026-07-23 |

### 2.4 UniRank: Benchmarking Ranking Models for Unified Sequential Modeling and Feature Interaction
| Field | Detail |
|---|---|
| **Title** | UniRank: Benchmarking Ranking Models for Unified Sequential Modeling and Feature Interaction |
| **Authors** | Honghao Li, Xianquan Wang, Zibin Zhang, Yi Zhang, Kangyi Lin, Yiwen Zhang |
| **Institution** | Not explicitly stated |
| **Abstract** | Modern ranking models increasingly unify sequential modeling and feature interaction, but advances rely on proprietary data and closed implementations. UniRank is an open benchmark for unified ranking models using chronological pointwise autoregressive supervision. Benchmarks 15 models on 5 large-scale public datasets (short-video, advertising, e-commerce), largest dataset 700M+ instances, longest behavior sequence 10^5+. PyTorch toolkit with DDP, mixed-precision, attention optimization. |
| **Key Innovations** | 1) Open benchmark standardizing evaluation for unified ranking models. 2) Scale: 700M+ instance dataset, 10^5+ length sequences. 3) Production-oriented evaluation with accessible implementations. |
| **Link** | [arXiv:2607.19987](https://arxiv.org/abs/2607.19987) |
| **Date** | 2026-07-22 |

### 2.5 Enhancing Generative Auto-Bidding with Offline Reward Evaluation and Policy Search (AIGB-Pearl)
| Field | Detail |
|---|---|
| **Title** | Enhancing Generative Auto-Bidding with Offline Reward Evaluation and Policy Search |
| **Authors** | Zhiyu Mou, Yiqin Lv, Miao Xu, Cheems Wang, Yixiu Mao, Jinghao Chen, Qichen Ye, Chao Li, Rongquan Bai, Chuan Yu, Jian Xu, Bo Zheng |
| **Institution** | Alibaba |
| **Abstract** | Auto-bidding (AIGB) learns a conditional generative planner from offline data but faces a performance bottleneck from inability to explore beyond static datasets. AIGB-Pearl constructs a trajectory evaluator and designs a KL-Lipschitz-constrained score-maximization scheme for safe and efficient exploration. Achieves SOTA on simulated and real-world advertising systems. ICLR 2026. |
| **Key Innovations** | 1) Trajectory evaluator for assessing generated bid scores. 2) KL-Lipschitz-constrained score maximization for safe off-policy exploration. 3) Synchronous coupling technique ensuring model regularity. |
| **Link** | [ICLR 2026 / OpenReview](https://openreview.net/forum?id=kMuQBgPIdg) |
| **Date** | 2026 (ICLR) |

---

## 3. Sequential Modeling & Recommendation

### 3.1 Zero-Observation User Reactivation with Gap-Driven Dimensional Gating (DeltaGate)
| Field | Detail |
|---|---|
| **Title** | Zero-Observation User Reactivation with Gap-Driven Dimensional Gating |
| **Authors** | Jiandong Ding, Tianying Liu, Fuyuan Liu, Huijie Qin, Tiandeng Wu |
| **Institution** | Not explicitly stated |
| **Abstract** | Returning users may have no interactions for months/years. DeltaGate is a lightweight output-layer plugin (backbone frozen) that routes each representation dimension between personalized history and a learned zero-initialized global prior, conditioned jointly on gap duration Δt and the personalized representation. RecSys 2026. In >365d Video Games: DG-SASRec 0.047 Hit@10 vs SASRec 0.031; DG-BERT4Rec 0.046 vs 0.025, with only 66K trainable parameters (2-4% overhead). |
| **Key Innovations** | 1) Defines Zero-Observation Reactivation setting for sequential recommendation. 2) Dimension-level gating conditioned on gap duration. 3) Frozen backbone with lightweight plugin (40x fewer params than end-to-end retraining). |
| **Link** | [arXiv:2607.19802](https://arxiv.org/abs/2607.19802) |
| **Date** | 2026-07-22 |

### 3.2 RecRec: Recursive Refinement for Sequential Recommendation
| Field | Detail |
|---|---|
| **Title** | RecRec: Recursive Refinement for Sequential Recommendation |
| **Authors** | Pervez Shaik, Prosenjit Biswas, Abhinav Thorat, Ravi Kolla et al. |
| **Institution** | Not explicitly stated |
| **Abstract** | Sequential recommender systems typically use single-pass encoding without iterative refinement. RecRec revisits recursive refinement—iteratively refining user preference representations through a fixed number of refinement passes without requiring deeper architectures. |
| **Key Innovations** | Recursive refinement mechanism for iterative preference modeling without deeper networks. |
| **Link** | [arXiv:2607.10541](https://arxiv.org/abs/2607.10541) |
| **Date** | 2026-07-12 |

### 3.3 Topology-Aware Tokenization for Generative Recommendation
| Field | Detail |
|---|---|
| **Title** | Topology-Aware Tokenization for Generative Recommendation |
| **Authors** | Yaokun Liu, Yifan Liu, Zhenrui Yue, Gyuseok Lee et al. |
| **Institution** | Not explicitly stated |
| **Abstract** | Generative recommendation reformulates sequential recommendation as autoregressive generation, but topology distortion in item tokenization is overlooked. This paper addresses the issue that hierarchical semantic IDs distort the underlying item similarity topology, proposing topology-aware tokenization. |
| **Key Innovations** | Topology-aware tokenization preserving item similarity structure in hierarchical semantic IDs. |
| **Link** | [arXiv:2607.18600](https://arxiv.org/abs/2607.18600) |
| **Date** | 2026-07-21 |

---

## 4. LLMs & Foundation Models

### 4.1 Understanding Large Language Models
| Field | Detail |
|---|---|
| **Title** | Understanding Large Language Models |
| **Authors** | Not fully listed (survey chapter) |
| **Institution** | Not explicitly stated |
| **Abstract** | Comprehensive overview of LLM mechanisms, emergent cognitive capabilities, and the debate regarding machine understanding vs. pattern memorization. Synthesizes research on architecture, emergent cognitive-like behaviors, and interpretability methods with philosophical arguments against reductionist views of AI cognition. |
| **Key Innovations** | Unified survey of LLM emergent capabilities, mechanistic interpretability, and cognitive science perspectives. |
| **Link** | [arXiv:2607.01006](https://arxiv.org/abs/2607.01006) |
| **Date** | 2026-07-01 |

### 4.2 Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning (GEAR)
| Field | Detail |
|---|---|
| **Title** | Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning |
| **Authors** | Not fully listed |
| **Institution** | Not explicitly stated |
| **Abstract** | Identifies "repetitive copying" as a critical failure mode in long-context LLMs, worsening with context length. Proposes GEAR using grounding rewards for key evidence and penalties for irrelevant context. Develops an automated pipeline for evidence-annotated training data. |
| **Key Innovations** | 1) Identifies repetitive copying failure mode. 2) Evidence-aware RL reward shaping. 3) Automated evidence annotation pipeline. |
| **Link** | [arXiv:2607.19345](https://arxiv.org/abs/2607.19345) |
| **Date** | 2026-07-28 |

### 4.3 NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation
| Field | Detail |
|---|---|
| **Title** | NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation |
| **Authors** | Huichao Zhang, Liao Qu, Yiheng Liu, Hang Chen, Yangyang Song, Yongsheng Dong, Shikun Sun et al. |
| **Institution** | ByteDance (ByteVisionLab) |
| **Abstract** | NextFlow is a unified decoder-only autoregressive transformer trained on 6T interleaved text-image tokens. Bridges understanding and generation in a single architecture via next-scale prediction. Generates 1024×1024 images in 5 seconds. SOTA on DPG (88.32) and ImgEdit (4.49). Supports CoT reasoning, in-context editing, and interleaved generation. |
| **Key Innovations** | 1) Unified decoder-only transformer for multimodal understanding + generation. 2) Next-scale prediction paradigm for fast image generation. 3) 6T token training scale. |
| **Link** | [arXiv:2601.02204](https://arxiv.org/abs/2601.02204) |
| **Date** | 2026-01-05 |

---

## 5. Games & Reinforcement Learning

### 5.1 Augmenting Game AI with Deep Reinforcement Learning
| Field | Detail |
|---|---|
| **Title** | Augmenting Game AI with Deep Reinforcement Learning |
| **Authors** | Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén |
| **Institution** | modl.ai |
| **Abstract** | Vision paper proposing a framework for training RL models with requirements suited for game AI: short training time, controllability, and modularity. Presents examples of RL-augmented game AI and describes practicalities of deploying ML agents in modern games. Published at Conference on Games 2026. |
| **Key Innovations** | 1) Framework with game-specific RL training requirements (short training, controllability, modularity). 2) Practical deployment guidance for player-facing ML agents. 3) Identification of bottlenecks for industry adoption. |
| **Link** | [arXiv:2606.20210](https://arxiv.org/abs/2606.20210) |
| **Date** | 2026-06-18 |

### 5.2 Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
| Field | Detail |
|---|---|
| **Title** | Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games |
| **Authors** | Not fully listed |
| **Institution** | Not explicitly stated |
| **Abstract** | Teaches language models to play strategic games through reinforcement learning, learning from feedback about move quality rather than generating the first answer. |
| **Key Innovations** | RL-based training for LLM strategic game-playing with quality feedback loops. |
| **Link** | [aimodels.fyi summary](https://www.aimodels.fyi/papers/arxiv/strat-reasoner-reinforcing-strategic-reasoning-llms-multi) |
| **Date** | 2026-05 |

### 5.3 LLM Semantic Signaling Game and Mechanism Design
| Field | Detail |
|---|---|
| **Title** | LLM Semantic Signaling Game and Mechanism Design: Systematic Blindness, Awareness Shaping, and Mindset Dynamics |
| **Authors** | Quanyan Zhu |
| **Institution** | NYU (likely) |
| **Abstract** | Game-theoretic framework analyzing systematic blindness, awareness shaping, and mindset dynamics in LLM-based signaling mechanisms. cs.GT, cs.AI, cs.MA. |
| **Key Innovations** | Formal game-theoretic analysis of LLM communication and mechanism design. |
| **Link** | [arXiv:2606.29113](https://arxiv.org/abs/2606.29113) |
| **Date** | 2026-06-27 |

---

## 6. Recommender Systems (Additional Recent)

### 6.1 Normative Alignment of Recommender Systems via Internal Label Shift (NAILS)
| Field | Detail |
|---|---|
| **Title** | Normative Alignment of Recommender Systems via Internal Label Shift |
| **Authors** | Johannes Kruse, Kasper Lindskow, Michael Riis Andersen, Ryotaro Shimizu et al. |
| **Institution** | Not explicitly stated |
| **Abstract** | Simple and scalable method for aligning recommendation outputs with target distributions over item-level attributes (e.g., categories) without retraining the full model. |
| **Key Innovations** | Internal label shift for normative alignment without full model retraining. |
| **Link** | [arXiv:2607.10915](https://arxiv.org/abs/2607.10915) |
| **Date** | 2026-07-12 |

### 6.2 ZoRRO: A Zero-Weight Personalized Recommender System for Scalable News Recommendation
| Field | Detail |
|---|---|
| **Title** | ZoRRO: A Zero-Weight Personalized Recommender System for Scalable News Recommendation |
| **Authors** | Johannes Kruse, Ryotaro Shimizu, Kasper Lindskow, Jon Tofteskov et al. |
| **Institution** | Not explicitly stated |
| **Abstract** | Zero-weight, training-free framework for personalized news recommendation. Outperforms strong neural baselines in offline ranking while being designed for scalable real-world deployment. |
| **Key Innovations** | Training-free, zero-weight recommendation framework achieving neural baseline performance. |
| **Link** | [arXiv:2607.10910](https://arxiv.org/abs/2607.10910) |
| **Date** | 2026-07-12 |

### 6.3 Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning
| Field | Detail |
|---|---|
| **Title** | Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning |
| **Authors** | Dingsu Wang, Filip Ryzner, Kelly He, Armando Ordorica et al. |
| **Institution** | Not explicitly stated |
| **Abstract** | Addresses shift from short-term behavioral signals to long-term user engagement/retention. Proposes model-agnostic downstream reward learning to optimize long-term objectives without directly optimizing them. |
| **Key Innovations** | Model-agnostic reward learning for long-term engagement optimization. |
| **Link** | [arXiv:2607.14192](https://arxiv.org/abs/2607.14192) |
| **Date** | 2026-07-15 |

### 6.4 Cardinality-Decomposed Loss for Heterogeneous Recommendation Graphs
| Field | Detail |
|---|---|
| **Title** | Cardinality-Decomposed Loss: Matching Training Objectives to Relation Structure in Heterogeneous Recommendation Graphs |
| **Authors** | Parul Maheshwari, Amulya Paruchuri, Yiqing Zou, Alireza Sahami Shirazi et al. |
| **Institution** | Not explicitly stated |
| **Abstract** | GNNs on heterogeneous bipartite graphs for recommendation face varying relation cardinality (e.g., one-to-many preferences vs one-to-one attributes). Proposes cardinality-decomposed loss to match training objectives to relation structure. |
| **Key Innovations** | Relation-aware loss decomposition for heterogeneous recommendation graphs. |
| **Link** | [arXiv:2607.20737](https://arxiv.org/abs/2607.20737) |
| **Date** | 2026-07-22 |

### 6.5 From Raw IDs to Semantic Planning: How Recommender Systems Utilize Information at Scale
| Field | Detail |
|---|---|
| **Title** | From Raw IDs to Semantic Planning: How Recommender Systems Utilize Information at Scale |
| **Authors** | Changhong Jin, Shiqiu Yang, Roger Zhe Li, Yingjie Niu et al. |
| **Institution** | Not explicitly stated |
| **Abstract** | Explores the evolution of recommender systems from raw ID-based to semantic planning approaches. Traces how information utilization has shifted across two decades of industrial systems. |
| **Key Innovations** | Historical analysis and taxonomy of information utilization evolution in industrial RecSys. |
| **Link** | [arXiv:2607.09540](https://arxiv.org/abs/2607.09540) |
| **Date** | 2026-07-10 |

---

## 7. Key Trends & Takeaways

1. **Generative Recommendation is Maturing**: Diffusion models (DLMRec) and autoregressive adaptations (BARGE) are pushing beyond simple next-token prediction, addressing structural gaps in how items are tokenized and decoded.

2. **LLM-Agent Integration in RecSys**: PRTA and similar works position LLMs as orchestrators over traditional models rather than replacements, avoiding hallucination by delegating scoring to purpose-built models.

3. **Industrial-Scale Validation**: Yandex (Long-History Transformers), Tencent (BARGE), and Alibaba (AIGB-Pearl) demonstrate that academic ideas translate to production gains (+0.5-2.8% metrics).

4. **Simpler Can Win**: DS-MLP shows a vanilla MLP with knowledge distillation can match SOTA complex feature interaction models. ZoRRO achieves strong results with zero training.

5. **Long-Context & Cold-Start**: DeltaGate addresses returning users with zero recent interactions; Long-History Transformers solve the latency-quality tradeoff for user history encoding.

6. **Sequential Modeling Unification**: UniRank benchmarks 15 unified ranking models, standardizing evaluation across the field. OneTrans (WWW 2026) unifies feature interaction and sequence modeling in a single Transformer backbone.

7. **RL in Games & Bidding**: RL techniques are transferring from game AI (strategic reasoning, NPC behavior) to advertising (auto-bidding with off-policy exploration), sharing core challenges around exploration, controllability, and real-time deployment.
