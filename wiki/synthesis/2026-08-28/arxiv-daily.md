---
title: "arXiv Daily — 2026-08-28: Token-Level Advertising Auctions, Causal Incremental Recommendation at Spotify, Collaborative Vector Memory for Agentic Rec, Evolution Strategies > GRPO for Reasoning Coverage, Cross-Embodiment World Models, $7K LLM Pretraining"
type: synthesis
created: 2026-08-28
updated: 2026-08-28
tags: [arxiv, daily, llm, recommendation, ctr, advertising, sequential-modeling, agents, games, world-models, token-level-advertising, generative-ads, gnn, causal-rec, agent-memory, evolution-strategies, dpo, pretraining, generative-image-retrieval, daily-digest]
---

# arXiv Daily — 2026-08-28

Scanned 567 unique arXiv entries from the fresh Fri Aug 28 announcement wave (Thu Aug 27 submission window, IDs ~2608.26480–2608.27454) across cs.IR / cs.AI / cs.LG, plus 209 new cs.AI + 63 cs.IR entries by date sweep. Focus: LLMs, recommendation, CTR, advertising, sequential modeling, agents, games, world models. Every paper ID grep-verified absent from wiki index and all prior sibling digests (arxiv-daily / arxiv-paper-check / game-rl-daily / conference-digest / tech-report-digest), including same-day coverage.

---

## 🎯 CTR Prediction & Advertising

### 1. Token-Level Advertising (LAMA — Latent Advertiser Mixture Auction)
| | |
|---|---|
| **Authors** | Hanbing Liu, Bowei Zhang, Changyuan Yu, Yinyu Ye, Qi Qi |
| **Institution** | Alibaba Group *(inferred from author affiliation)* |
| **arXiv** | [2608.27382](https://arxiv.org/abs/2608.27382) |

**Abstract:** Generative AI is transforming how people access information, challenging traditional advertising mechanisms built around predefined slots. Towards generation-native advertising, the paper proposes the Latent Advertiser Mixture Auction (LAMA), a token-level advertising mechanism that embeds advertiser influence directly into the generation process. Advertisers report local continuation values that induce advertiser-specific next-token policies, from which the platform decodes through a latent mixture while updating an allocation posterior.

**Key Innovations:**
- First mechanism to move advertising from slot-level to **token-level**: advertiser influence is injected directly into the LLM generation decode
- **Markov DSIC and IR** satisfied, with near-optimal KL-regularized welfare guarantees
- Learning-based implementation reconstructs the required reports online from learned local advantages and root values (no explicit report function needed)
- Proof-of-concept on real-world commercial-search query splits improves platform welfare and revenue while maintaining user-facing response quality

---

### 2. MaskRec: Topology-Masked Unified Backbone for Joint Feature Interaction and Multi-Domain Sequence Modeling
| | |
|---|---|
| **Authors** | Zhihao Zhu, Dezheng Han, Jikang Xia, Shuaishuai Guo |
| **Institution** | — |
| **arXiv** | [2608.27005](https://arxiv.org/abs/2608.27005) |

**Abstract:** Large-scale post-click conversion rate (CVR) prediction requires jointly modeling heterogeneous feature interactions and dependencies over multi-domain user behavior sequences. Existing industrial ranking models usually handle these two aspects with separate modules; recent unified architectures attempt to incorporate them into a single framework, but such unification often relies on coordination between modules and does not fully organize all information sources within the same interaction space.

**Key Innovations:**
- **Unified token space**: transforms heterogeneous features, multi-domain behavior sequences, and contextual signals into unified token representations, plus learnable global memory tokens and domain-level memory tokens as aggregation nodes
- **TopoMask**: a structured attention mask that selectively enables/blocks attention connections according to structural differences and modeling requirements of each information source — heterogeneous feature interaction and multi-domain sequence modeling run inside the same topology-constrained attention process
- **Dual-path interactive query generation** injects candidate-conditioned user-item interaction signals before the unified backbone
- Validated on the Tencent Advertising Algorithm Competition dataset with stable gains over the official CVR baseline

---

### 3. Stageboost: Recommending Signals Based on Counterfactual Estimation
| | |
|---|---|
| **Authors** | Darpan Singhal, Matan Mandelbrot, Tal Franji, Manasa Kolla, Vipul Gaba, Yuri Brovman |
| **Institution** | eBay |
| **arXiv** | [2608.27366](https://arxiv.org/abs/2608.27366) |

**Abstract:** Signals are short textual or visual snippets displayed on the eBay View-Item (VI) page, providing additional, contextual information for users about the viewed item. The aim of displaying these signals is to facilitate intelligent purchase and to incentivize engagement.

**Key Innovations:**
- Two-stage xgboost-based model that **optimally populates the VI page with signals** using counterfactual estimation of each signal's contribution
- Online experiment: +0.08% lift in overall GMB (Gross Merchandise Bought) and +0.58% in Parts and Accessories GMB, driven mainly by conversion gains on high-average-price items

---

### 4. LiveSim: Simulating Environment-Shaped Users in Multi-Agent Live-Stream Ecosystems
| | |
|---|---|
| **Authors** | Jiaqi Xu, Yiran Qiao, Jing Chen, Qiwei Zhong, Xiang Ao, Xueqi Cheng |
| **Institution** | Institute of Computing Technology, CAS *(inferred)* |
| **arXiv** | [2608.26849](https://arxiv.org/abs/2608.26849) |

**Abstract:** User behavior simulation with LLMs is increasingly used to support multi-agent ecosystem simulation. Existing simulators typically rely on static user profiles inferred from historical observations, which become inadequate in socially intensive environments such as live streaming where interaction dynamics continuously reshape user behavior.

**Key Innovations:**
- Represents users as **editable behavioral hypotheses** progressively refined through trajectory-grounded interactions
- Discrepancies between simulated and observed trajectories reveal missing **environmental shaping effects**
- Extracts transferable **environment-behavior patterns** stored in a collective behavioral memory, improving both user-level fidelity and ecosystem-level simulation
- Validated on real-world live-stream **risk-control data** (risk evolution analysis + platform intervention effects)

---

## 📊 Recommendation Systems

### 5. Incremental Recommendation via Causal Models
| | |
|---|---|
| **Authors** | Athanasios Vlontzos, David Gustafsson, Michael O'Riordan, Ciarán M. Gilligan-Lee |
| **Institution** | Spotify |
| **arXiv** | [2608.26804](https://arxiv.org/abs/2608.26804) |

**Abstract:** Recommendation impressions are a finite resource; delivering a recommendation to a user who would discover the content organically yields no incremental value and displaces other recommendations that could. The paper extends an existing production recommendation model to a causal architecture using holdback data already collected as part of routine experimentation infrastructure, requiring no new data collection.

**Key Innovations:**
- **Causal treatment-effect targeting** uses holdback (organic-discovery) observations already in the experimentation stack — zero new data collection
- Solves the **attribution-window mismatch** problem (short direct-response treated window vs multi-day organic holdback window) via a **dual-threshold targeting policy**: recommend only when P(treated stream) is high and P(organic stream) is low
- Production-scale A/B on millions of Spotify users: **−7% recommendation impressions with no statistically significant reduction** in overall recommended-content consumption
- Joint training with holdback data improves calibration of the treated head, evidence that causal models learn more generalizable representations

---

### 6. Scaling Graph Neural Networks for Friend Recommendation: Multi-Hash User Embeddings and Temporal Neighbor Sampling
| | |
|---|---|
| **Authors** | Maksim Utushkin, Andrei Ovsiannikov, Alexander D'yakonov |
| **Institution** | — |
| **arXiv** | [2608.27413](https://arxiv.org/abs/2608.27413) |

**Abstract:** Friend recommendation is inherently graph-structured: relevance depends on multi-hop social context rather than user attributes alone. However, deploying message-passing GNNs on a production-scale social graph with hundreds of millions of users and tens of billions of edges requires addressing numerous modeling and systems challenges.

**Key Innovations:**
- **Multi-hash ID embeddings** as primary node representation cut the ID-embedding table by **>98%** (from ~200 GB+) while preserving ranking quality
- **Timestamp-sorted CSR + binary-search temporal neighbor sampling** reduces per-node cost from O(deg(v) + k) to O(log(deg(v)) + k), enabling sampling for users with tens of thousands of friends
- Scales to **194M users / 28B edges**; online A/B: **+16% friend additions and +11.5% unique friend adders** over a strong production baseline
- Releases framework for distributed training/inference on large temporal graphs

---

### 7. PrismRec: Preference Flow Matching with Spectral Factorization for Micro-video Recommendation
| | |
|---|---|
| **Authors** | Xinxin Dong, Haokai Ma, Fei Hu, YuZe Zheng, Bin Wu, Yonghui Yang, Xiaodong Wang |
| **Institution** | — |
| **arXiv** | [2608.26579](https://arxiv.org/abs/2608.26579) |

**Abstract:** Micro-video recommendation aims to infer user preferences from historical interactions and multimodal video content. Prevailing methods compress frame sequences into a single holistic representation, entangling stable visual semantics and evolving dynamics; meanwhile flow-matching-based recommenders condition generation solely on coarse behavioral context, leaving internal temporal structure outside preference formation.

**Key Innovations:**
- **Spectral Semantic Factorization (SSF)**: like a prism dispersing white light, derives complementary static-semantic and dynamic factors from frame-level representations via a prior-guided learnable frequency mask in the temporal frequency domain
- **Context-Calibrated Preference Matching (CPM)**: weighs static/dynamic factors by each user's sensitivity and injects calibrated context as a structured condition steering the flow-matching trajectory — makes video content an intrinsic driver of preference formation, not side information
- Up to **+22.65% over SOTA** on four datasets from two platforms, with lowest inference cost and peak memory among compared methods

---

### 8. Conversational Recommendation over Live E-Commerce Catalogues with Self-Refreshing Retrieval
| | |
|---|---|
| **Authors** | Ante Kapetanovic, Tomislav Duricic, Dionizije Fa, Andro Mercep, Emanuel Lacic |
| **Institution** | Infobip / Institute for Data-Driven Marketing *(inferred)* |
| **arXiv** | [2608.27006](https://arxiv.org/abs/2608.27006) |

**Abstract:** Conversational recommender systems based on LLMs are usually evaluated on static, pre-indexed item collections, yet e-commerce catalogues change continuously as products are added, removed, repriced, and restocked.

**Key Innovations:**
- **Self-refreshing retriever** ingests merchant product feeds, enriches records, and syncs them into a vector index; per-item hashes detect new/changed/deleted/unchanged so only the **delta** is processed each run
- LLM used only for intent classification and preference elicitation — retrieval, reranking, and diversity selection run as deterministic functions (cost control)
- Merchant-agnostic, multi-turn assistant demonstrated as a **WhatsApp shopping agent**; open-sourced

---

### 9. CoVeMem: When Memory Takes Gradients — Collaborative Vector Memory for Agentic Recommender Systems
| | |
|---|---|
| **Authors** | Hanchong Chen, Xing Tang, Lingjie Li, Xiongfeng Shan, Xiuqiang He |
| **Institution** | Huawei Noah's Ark Lab *(inferred from author affiliation)* |
| **arXiv** | [2608.26895](https://arxiv.org/abs/2608.26895) |

**Abstract:** Agentic recommender systems ground each LLM decision in a persistent memory of the user, and in existing agents that memory is text — a narrative written and maintained by further LLM calls. Text limits memory two ways: it is updated one rewrite at a time (exploiting full interaction history becomes prohibitively expensive), and collaborative evidence (graded similarity over an entire catalog) does not survive translation into sentences.

**Key Innovations:**
- **Collaborative Vector Memory (CoVeMem)**: vectorizes the collaborative core of agent memory — frozen LightGCN user/item states form the memory bank; the candidate set itself retrieves relevant historical states as **soft tokens** injected into the LLM context alongside a light textual profile
- Contrastive alignment to item-semantic anchors + **listwise co-training with masked candidates** teaches the LLM to read and rank through vector states
- **Zero additional LLM calls** for memory maintenance (vs per-interaction calls for text memory) while matching/exceeding the strongest collaborative text-memory agent on 19 of 20 metric cells across four instruction-grounded benchmarks
- Memory now takes *gradients*: the full interaction history becomes trainable signal for what the agent remembers and how it reads it

---

### 10. MOSAIC: Meta-Reviewing Sparse and Incomplete User-generated Contents for Recommendation
| | |
|---|---|
| **Authors** | Hongren Wang, Tianjun Wei, Yingpeng Du, Jie Zhang, Yin-Leng Theng |
| **Institution** | Nanyang Technological University / Stony Brook *(inferred)* |
| **arXiv** | [2608.26728](https://arxiv.org/abs/2608.26728) |

**Abstract:** Data sparsity is a long-standing challenge in recommender systems, and becomes more severe for methods relying on user-generated content (UGC) such as textual reviews. UGC exhibits two failure modes: missing reviews (interactions lack any review) and incomplete reviews (available reviews cover only a subset of relevant attributes).

**Key Innovations:**
- **Meta-review construction**: borrows the academic peer-review meta-review idea — aggregates attribute–sentiment evidence from neighbor users' reviews into a per-target-user meta-review
- **MMoE architecture** jointly optimizes rating prediction and meta-review attribute-sentiment prediction; attention module personalizes aggregated signals per target user
- Delivers both refined rating predictions and **attribute-level explanations**; consistent gains for users with limited interaction history across four real-world datasets

---

### 11. Equal Ranking Quality, Different Decisions: Training Order-Consistent LLM Scorers (OC-SFT)
| | |
|---|---|
| **Authors** | Markus Frohmann, Mahdiyar Alavi, Elizabeth Lingg, Navid Rekabsaz |
| **Institution** | Thomson Reuters / University of Saskatchewan *(inferred)* |
| **arXiv** | [2608.26762](https://arxiv.org/abs/2608.26762) |

**Abstract:** Rerankers, reward models, and multi-document QA scorers score candidates within one LLM prompt, so each score depends on candidate order. Such scorers are selected on ranking quality, but their scores determine a decision: what a score threshold retains, a reader answers, or a preference model selects. However, equal ranking quality does not imply equal decisions.

**Key Innovations:**
- Documents a systemic blind spot: five trained scorers within 0.010 nDCG@10 share retain sets overlapping only 0.66–0.84 when reordered; no prompt-time trick removes order dependence
- **Order-Consistency SFT (OC-SFT)**: trains a candidate's score to be invariant to presentation order — attenuates order dependence in the weights, not the prompt
- Holds ranking quality while leading every decision-stability measure on all three tasks (retainer sets, reader answers, preference selection); beats order-averaged distillation across 12 base models
- Recommendation: evaluation must report what a threshold retains and what a reader answers, not ranking quality alone

---

### 12. PailitaoGR: Latent Think-with-Images for Generative Image Retrieval
| | |
|---|---|
| **Authors** | Xiaomeng Fan, Yueran Liu, Shengyu Zhou, Chenghan Fu, Wanxian Guan, Feng Li, Chuan Yu, Jian Xu, Bo Zheng |
| **Institution** | Alibaba Group (Taobao) *(inferred from author affiliation)* |
| **arXiv** | [2608.26658](https://arxiv.org/abs/2608.26658) |

**Abstract:** Generative retrieval has demonstrated strong performance by directly generating product semantic identifiers (SIDs). Extending this to image search is nontrivial because real-world query images contain diverse information — search target, useful auxiliary evidence, and irrelevant visual content — requiring the model to focus on the target while selectively using auxiliary evidence.

**Key Innovations:**
- **Latent Think-with-Images** internalizes target-focused perception and selective auxiliary-evidence use into the generative retrieval model: "Zooming without Cropping" and "Reading without OCR"
- **Target Enhancer** + on-policy distillation with an attention-guided loss focuses the model on search-target regions
- **Auxiliary Enhancer** + in-capacity incremental contrastive distillation exploits auxiliary evidence
- Trained on real online image-search logs; **+13.8% average over baselines**

---

## 🔍 Retrieval & Search

### 13. ProRetrieval: Learning to Orchestrate Hybrid Search via Executable Program Synthesis
| | |
|---|---|
| **Authors** | Chengsong You, Zhen Sun, Yunhai Hu, Junwei Zhou, Xiaoyu Cao, Binyu Li, Ziyan Zhao, Weiyao Wang, Liren Lu, Zhijie Ye, Yumo Cao, Yitao Long |
| **Institution** | — |
| **arXiv** | [2608.27017](https://arxiv.org/abs/2608.27017) |

**Abstract:** Real-world retrieval composes structured constraints with semantic intents over text and images through arbitrary Boolean logic. Existing hybrid pipelines (reciprocal rank fusion, self-querying retrievers) admit only fixed composition forms, and RL retrievers train the LM as query generator for a single backend, leaving orchestration of heterogeneous paths outside its action space.

**Key Innovations:**
- Recasts the LM as a **retrieval orchestrator**: synthesizes an executable program in a hybrid DSL that interleaves SQL operators over structured fields with vector-retrieval primitives over text and images
- Trained with **GRPO + DAPO under a hierarchical four-term reward** on Qwen3-4B
- 4B model surpasses **GPT-5.5** (Hit@1 0.81 vs 0.69 on e-commerce; 0.91 vs 0.86 on email) and Claude Opus 4.7 plus retrieval/LLM-augmented/structured-query/graph baselines

---

## 🤖 Agents & Multi-Agent Systems

### 14. Astar: Learning to Propose Evolution Directions for Self-Evolving Industrial AI Systems
| | |
|---|---|
| **Authors** | Jinxin Hu, Hao Deng, Haibo Xing, Lingyu Mu, Muyu Zou, Weiqin Yang, Sirui Chen, Bohao Wang, Zhezheng Hao, Hao Zhang, Zulong Chen, Shizhun Wang |
| **Institution** | Alibaba Group — Lazada Advertising |
| **arXiv** | [2608.27287](https://arxiv.org/abs/2608.27287) |

**Abstract:** Modern AI systems advance through continuous iteration: proposing evolution directions, implementing code, training, evaluation. While the latter three stages are increasingly automated, the starting point — proposing effective evolution directions — remains a bottleneck relying on senior experts. General-purpose LLMs (even GPT-5.5) offer only generic, misaligned suggestions: the required expertise is accumulated through experience rather than codified.

**Key Innovations:**
- **Astar-8B**: a training-based evolution-guiding model learned from abundant industrial iteration histories (mid-training → SFT → RL with reward-model surrogate evaluation)
- Noise-to-corpus pipeline turns noisy historical commits into a large clean evolutionary corpus via pairwise sample expansion and noise filtering; hierarchical hints guide direction generation
- **Single-proposal success rate 0.6786** in real-execution evaluation vs human experts 0.3229 and GPT-5.5-class LLM 0.3071
- Deployed in Alibaba Lazada advertising: drove **20 consecutive automatic iterations over two weeks**, +23.6% offline Hitrate@200, +4.86% GMV and +1.82% advertising revenue online — the evolution loop is now fully automatic

---

### 15. WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution
| | |
|---|---|
| **Authors** | Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu |
| **Institution** | Google |
| **arXiv** | [2608.27454](https://arxiv.org/abs/2608.27454) |

**Abstract:** Agent skills package specialized knowledge and workflows into reusable resources that extend AI agent capabilities. Recent work automatically discovers skills from agent experience, but the insights guiding skill development typically remain scattered across optimization histories, limiting systematic reuse across iterations.

**Key Innovations:**
- **Wiki-framework co-evolution**: separates raw execution experience, accumulated knowledge, and executable skills; continuously consolidates experience into a persistent **wiki knowledge base** that subsequent skill updates build on
- Skill evolution **complements model scaling**: larger models benefit more from evolved skills; smaller models with skills can outperform substantially larger models without them
- Evolved skills **transfer across models and model families**; skills evolved by other models can outperform self-evolved skills
- Ablations confirm persistent knowledge accumulation is critical for effective skill evolution; consistently beats SOTA skill-evolution methods across diverse benchmarks/models

---

### 16. GraphMemix: Query-Aware Evidence Forests for Long-Term Multimodal Agent Memory
| | |
|---|---|
| **Authors** | Geng Li, Yuhao Wang, Dong Li, Jianye Hao, Yuxin Peng |
| **Institution** | Peking University / Huawei *(inferred)* |
| **arXiv** | [2608.26983](https://arxiv.org/abs/2608.26983) |

**Abstract:** Organizing long-term memory for multimodal agents remains challenging: existing methods either suffer from expensive question-agnostic offline summaries or naive embedding-similarity matching that introduces incomplete and redundant context.

**Key Innovations:**
- Models memory organization as **query-aware evidence-forest construction** under combinatorial optimization
- Candidate graph construction expands multi-view seed memories through schema and semantic relations; **evidence utility vs activation cost** decoupling suppresses redundant/conflicting info
- Forest optimization jointly selects a forest-format memory context under a maximum evidence budget with reliable relational structure
- Recovers **low-similarity complementary evidence** without heavy lifecycle cost; establishes a new accuracy-vs-lifecycle-cost Pareto frontier across four long-term multimodal memory benchmarks

---

### 17. PILOT in the Loop: Live Self-Improvement for Long-Horizon Agents
| | |
|---|---|
| **Authors** | Yang Xiao, Yusong Sun, Haoyi Wu, Wenyang Hui, Wen Da, Zhaokai Luo, Mu Chuan, Yao Hu, Wenjie Li, Chengyue Jiang |
| **Institution** | — |
| **arXiv** | [2608.26530](https://arxiv.org/abs/2608.26530) |

**Abstract:** Long-horizon agent runs generate experience that can improve both the current run and future work. Most self-improvement methods process this experience only after execution ends, so they cannot redirect the active run or immediately validate lessons learned from it. Self-improvement should instead be **live**, using emerging experience both to redirect the active run and update the persistent harness.

**Key Innovations:**
- **Live steering**: a separate supervisor redirects or aborts the active worker mid-execution (fixes single-agent and subagent-delegation blind spots)
- **Live self-evolution**: distils procedures and failure modes revealed during execution into reusable skills and memory
- Across two frozen backbones and three benchmarks, ranks first in 5 of 6 configurations; on Terminal-Bench 2.0 up to +9.8 pp over counterpart harnesses
- Self-improvement gains: +14.6 pts (GLM-5.1) and +12.4 pts (Kimi-K2.6), while output tokens drop ~43–47% and **successful evals per million output tokens rise ~110–134%**

---

### 18. A Contract-Centered Architecture for Scalable and Manageable Agentic Runtimes
| | |
|---|---|
| **Authors** | Yaxiao Liu, Pengbo Liu, Yiwen Liu, Yihua Guan, Zhenghe Hou, Jiaxing Song |
| **Institution** | — |
| **arXiv** | [2608.27086](https://arxiv.org/abs/2608.27086) |

**Abstract:** Enterprise AI deployment is a coordination problem across business units, application/AI teams, testing, platform engineering, infrastructure, security, operations, and data governance. Use-case benchmarks show whether one agent completes one task, but not how changing capabilities, models, runtime mechanisms, capacity, and enterprise data should be owned, changed, admitted, or evidenced together.

**Key Innovations:**
- Four **responsibility objects as shared organizational contracts**: Skill (reusable versioned capability), Harness (runtime compiler/governor), Scaffold (execution/control boundary + NFR owner), and a stack-external CIO-governed data substrate
- One bounded falsifiable hypothesis, **P1 (cost-aware capability–capacity separability)** with a preregistered equivalence margin, turned into six measured obligations
- Proposes a cluster-period randomized crossover experiment with a four-state verdict (supported / falsified / conditional-engineering / inconclusive) — a measurement protocol, not a shipped implementation (explicitly self-declared)

---

### 19. Persona-Execution Separation: An Architecture Pattern for Evolving LLM Agents under Execution Audit
| | |
|---|---|
| **Authors** | Yisen Xi |
| **Institution** | — |
| **arXiv** | [2608.27427](https://arxiv.org/abs/2608.27427) |

**Abstract:** LLM agents in governed organizations must let the persona (instructions, tone, self-presentation) evolve freely while keeping execution (stateful, audited work) traceable. A single trust domain does not satisfy both cheaply.

**Key Innovations:**
- **Persona-Execution Separation (PES)**: persona (singly-homed, may drift) and execution (faceless, audited) live in different trust domains connected by a governed contract bridge
- Uses **representational indistinguishability** to prove any single-domain mechanism meeting all three goals (free drift, execution traceability, decoupling) must reintroduce typed change objects, external gate, and stable audit anchor — i.e. PES rebuilt at higher coupling cost
- Development/pilot in a regulated digital-employee platform; mechanism check found no execution-side re-validation under persona perturbation (five model configs)

---

### 20. What Makes Good Agentic Data? An ACE Lens on Data Generation for LLM Agents
| | |
|---|---|
| **Authors** | Xingshan Zeng, Zishan Xu, Boju Zhang, Yuzhou Wu, Lingzhi Wang, Jianghao Lin, Liangyou Li, Yasheng Wang, Lifeng Shang, Xin Jiang, Weinan Zhang, Yong Yu |
| **Institution** | SJTU / Huawei Noah's Ark *(inferred)* |
| **arXiv** | [2608.27260](https://arxiv.org/abs/2608.27260) |

**Abstract:** LLM agents increasingly rely on generated interaction data to learn how to interact with external environments. Agentic data generation must maintain consistency among environments, tasks, interactions, and success signals while producing experience that is useful rather than merely abundant.

**Key Innovations:**
- Factorized data representation **(E, q, τ, v)** — environment spec, task signal, interaction realization, optional verifier — with generation paradigms organized by anchor and dependency structure
- **ACE lens (Accuracy–Complexity–divErsity)**: accuracy sets the feasible support; complexity places learning mass relative to a declared learner; diversity controls coverage and redundancy
- Documents the field's shift toward execution-grounded accuracy, learner-relative complexity, and diversity beyond surface variation — a useful survey/shaping-theory contribution for agentic training data

---

## 🎮 Games & World Models

### 21. CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators
| | |
|---|---|
| **Authors** | Kechen Liu, Ola Shorinwa |
| **Institution** | Stanford University *(inferred from author affiliation)* |
| **arXiv** | [2608.27406](https://arxiv.org/abs/2608.27406) |

**Abstract:** State-of-the-art action-conditioned video models are typically restricted to a single robot embodiment, preventing them from leveraging the vast corpus of heterogeneous video data that contains rich signals for learning generalizable physics.

**Key Innovations:**
- **Cross-embodiment action-conditioned video generation** trained on internet-scale heterogeneous human/robot video, grounded in the insight that universal physical laws govern spatiotemporal dynamics regardless of actor
- Reconciles disparate action spaces via **end-effector poses + language instructions + latent actions**
- **Curriculum-based recipe**: learns foundational physical priors over unlabeled video (latent actions), then grounds them in end-effector action spaces for **zero-shot deployment** to real-world tasks
- Approaches/surpasses single-embodiment SOTA (e.g. DROID); spans diverse action-conditioning spaces and robot morphologies (DROID, Bridge, bimanual YAM, G1 humanoids); open-sourced

---

### 22. PAWBench: How Far Are We from Probabilistically Aligned World Modeling?
| | |
|---|---|
| **Authors** | Yuandong Pu, Le Zhuo, Sayak Paul, Gabriel Jorge Menezes, Avram Đorđević, Shiyang Li, Yifan Zhou, Bin Fu, Wenlong Zhang, Junjun He, Yu Qiao, Yihao Liu |
| **Institution** | AgiBot / SHIR / Hugging Face — multi-institution |
| **arXiv** | [2608.27345](https://arxiv.org/abs/2608.27345) |

**Abstract:** Recent video generation models are increasingly framed as world models. Many physical processes unfold in more than one valid way, so a world model should reproduce not only a plausible trajectory but the **distribution** of possible behaviors under the same initial observation and action — distribution-level *probabilistic alignment*.

**Key Innovations:**
- Formalizes probabilistic alignment as a distributional criterion for world models and introduces **PAWBench** (50 scenarios) + **PAWEval**, an outcome-level protocol converting repeated video rollouts into empirical distributions over physical behaviors
- **Negative result**: across 50 scenarios and eleven current systems, no model consistently matches reference probabilities while recovering the full range of valid behaviors
- Probes whether language prompts, initial noise sampling, or training can reshape the predictive distribution — a foundation for probabilistically aligned world modeling

---

### 23. LEON: Operator-Structured Transitions for World Action Models
| | |
|---|---|
| **Authors** | Xiaoxiao Lu, Yunlong Dong, Jiahao Shi, Ye Yuan |
| **Institution** | — |
| **arXiv** | [2608.27259](https://arxiv.org/abs/2608.27259) |

**Abstract:** World Action Models (WAMs) augment robot policies by predicting how task-relevant scene states evolve under interaction. Recent WAMs predict in latent representation spaces, avoiding full appearance-level generation. Yet latent transitions are commonly realized with Transformer predictors whose inductive structure centers on token interaction rather than temporal evolution.

**Key Innovations:**
- **Latent Evolution Operator Network (LEON)**: models latent evolution in a learned observable space through **context-modulated operator-based propagation + additive forcing**, grounded in the controlled Koopman-generator view
- Studies *transition realization* as an architectural choice distinct from predictive representation, on par with representation and prediction–policy coupling in WAM design
- Improves closed-loop performance and robustness across two WAM formulations and remains effective under full transition replacement

---

## 🧠 LLM Training & Reasoning

### 24. Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO
| | |
|---|---|
| **Authors** | Yunpeng Ba, Zhi Zheng, Yue Xie, Jiaqing Li, Xialiang Tong, Tao Zhong, Mingxuan Yuan, Zhichao Lu, Xuyang Wu, Zhenkun Wang |
| **Institution** | Huawei Noah's Ark Lab / SUSTech *(inferred)* |
| **arXiv** | [2608.27351](https://arxiv.org/abs/2608.27351) |

**Abstract:** Evolution Strategies (ES) have emerged as a memory-efficient post-training paradigm for LLM reasoning, but their optimization behavior remains understudied. By systematically investigating ES dynamics and mechanisms, the paper identifies a performance advantage of ES over GRPO: ES leads to broader reasoning coverage, better exploiting pretrained LLM capabilities.

**Key Innovations:**
- Theoretical result: **verifier-projected Jensen-Shannon diversity** across the ES population is helpful for higher Pass@K
- Empirically, GRPO exhibits **entropy collapse**, while ES improves Pass@1 *and* attains higher Pass@K; a sequential **GRPO→ES strategy** combines GRPO's Pass@1 strength with ES's Pass@K gains
- Despite substantial whole-model parameter drift, ES task gains come from a **sparse subset of larger-magnitude updates** — large parameter movement need not imply functional change and does not necessarily cause catastrophic forgetting
- ES requires a **smaller population size in larger LLMs** — positions ES as a distinct post-training paradigm, not merely a memory-efficient GRPO alternative

---

### 25. Disentangling Optimization Scale from Preference Scale in DPO
| | |
|---|---|
| **Authors** | Ivan Kruzhilov |
| **Institution** | — (independent) |
| **arXiv** | [2608.27032](https://arxiv.org/abs/2608.27032) |

**Abstract:** The DPO coefficient β is commonly interpreted as controlling the KL constraint to a reference policy. The paper shows β entangles two distinct roles: it governs the effective inverse preference-noise scale and simultaneously rescales the optimization dynamics, coupling this scale with the effective step size.

**Key Innovations:**
- At a fixed learning rate, achieved policy deviation is **non-monotone in β** (dead zone at small β → peak → decline), and DPO loss values are not comparable across β (nearly identical loss curves can differ several-fold in KL divergence)
- This entanglement obscures β's role, increases hyperparameter sensitivity, and complicates LR scheduling
- Proposes a **centered-softplus reformulation**, argmin-equivalent to DPO for β>0, making the inverse preference-noise-scale and learning-rate effects explicit and independently tunable; admits a continuous β→0 endpoint reducing to a linear preference-margin objective

---

### 26. Puro-2B: Poor Lab's Qwen2-1.5B Trained on RTX 5090 within $5090
| | |
|---|---|
| **Authors** | Kairong Luo, Jiarui Cui, Yaorui Yin, Shengqi Chen, Yiming Yang, Linxiang Gao, Yanmohan Wang, Mingzhe Zhang, Kaiyue Wen, Kaifeng Lyu, Wenguang Chen |
| **Institution** | Tsinghua University (THU-PacMan Lab) |
| **arXiv** | [2608.27370](https://arxiv.org/abs/2608.27370) |

**Abstract:** Language model pretraining has become almost synonymous with prohibitive cost. Even at small scale, training Llama-3.2-3B costs over $1.5M and reproducing SmolLM3-3B needs over $700K.

**Key Innovations:**
- An open, hardware-accessible pretraining recipe: **Puro-2B** pretrained from scratch on up to **1.4T tokens in FP8 on consumer RTX 5090 GPUs** — best model under ~$6.9K compute cost, approaching Qwen2.5-1.5B performance
- Combines hardware selection, low-precision training, hyperball optimization, curriculum model averaging, and a data recipe; fully open-sourced (data, code, weights, Apache 2.0)
- **Puro Cost Scaling Law** relating training cost to average performance: ~$4.4K (< $5,090) suffices to reach Qwen2-1.5B-level quality
- End-to-end case study of how pretraining data curricula shape post-training downstream performance (possible because the full pipeline is accessible)

---

### 27. When Does Supervised Fine-Tuning Reduce Instruction Sensitivity?
| | |
|---|---|
| **Authors** | Jaekeol Choi |
| **Institution** | — |
| **arXiv** | [2608.26661](https://arxiv.org/abs/2608.26661) |

**Abstract:** LLMs can exhibit substantial performance variation across alternative formulations of the same task instruction, yet it remains unclear how conventional task-specific SFT changes this instruction sensitivity. Instruction sensitivity is defined as the standard deviation of task performance across paraphrased instructions.

**Key Innovations:**
- Controlled scale analysis (Qwen3 1.7B/4B/8B on MS MARCO + cross-family checks on Mistral-7B, Gemma-2-9B): before SFT, instruction sensitivity decreases sharply with model scale
- At 1.7B/4B, SFT consistently reduces sensitivity (~54–71%); at 8B the effect is statistically indistinguishable from zero — **SFT does not uniformly reduce instruction sensitivity**
- Evaluation protocol itself matters: free-generation vs likelihood-based forced-choice can yield qualitatively different robustness conclusions even at near-perfect valid-label generation

---

### 28. Beyond Parallel Blindness: Information Floors and Model Gaps in Block Drafting
| | |
|---|---|
| **Authors** | Xinwei Qiang, Xiang Fang, Chang Chen, Yue Guan, Yufei Ding |
| **Institution** | UT Austin / UCSD *(inferred)* |
| **arXiv** | [2608.27339](https://arxiv.org/abs/2608.27339) |

**Abstract:** Block drafters propose several tokens in one forward pass before earlier target tokens are realized. Their rejection mixes two losses: missing within-block path information and imperfect modeling of observable information. Accepted length cannot distinguish them.

**Key Innovations:**
- Separates the two with an **information floor** — the minimum expected rejection at a specified conditioning order; rejection above the floor is the **model gap**
- The all-parallel floor reaches **0.286 at the final slot** on Qwen3-4B, capping even the best proposal at 71% per-slot acceptance; one realized token removes 86–100% of the floor (confirmed by an independent mutual-information analysis)
- Current drafters stay far above their floors: final-slot model gap accounts for 43–64% of DFlash rejection and 85–92% of DSpark's oracle-conditioned rejection — isolating the value of short-range conditioning from proposal quality per se

---

## 📌 Key Trends Today

1. **Token-level advertising**: LAMA (2608.27382) moves ad mechanism design inside the LLM decode — advertisers report continuation values that shape next-token policies under a Markov-DSIC/IR auction with near-optimal KL-regularized welfare. Direct follow-on to yesterday's generation-native advertising thread.
2. **Causal incremental recommendation goes production**: Spotify (2608.26804) reuses routine holdback data to suppress recommendations users would get organically — −7% impressions with no consumption loss, with a clean fix for attribution-window mismatch.
3. **Agentic recommender memory leaves text**: CoVeMem (2608.26895) makes collaborative signals differentiable soft tokens (zero extra LLM calls for memory); complements text-memory agents. Agent memory co-evolution remains a hot theme (WikiSkill 2608.27454, GraphMemix 2608.26983).
4. **Closed-loop self-evolving industrial AI**: Astar (2608.27287) at Alibaba Lazada Advertising now proposes its own evolution directions — 20 autonomous iterations, +4.86% GMV — effectively automating the "propose" step of the iterate loop that human experts previously owned.
5. **ES emerges as a distinct LLM reasoning paradigm**: Evolution Strategies (2608.27351) give broader reasoning coverage (higher Pass@K) than GRPO without entropy collapse, and combine with GRPO sequentially — while theoretical analysis ties ES population diversity to Pass@K.
6. **World models face a distributional test**: PAWBench (2608.27345) finds no current video generator is probabilistically aligned (worst 11 systems, 50 scenarios), as CLAP (2608.27406) pushes cross-embodiment video world models toward zero-shot physical simulation.
7. **Pretraining cost keeps collapsing**: Puro-2B (2608.27370) shows ~$4.4K consumer-hardware pretraining approaching Qwen2-1.5B quality — plus a cost scaling law.

*Report generated on 2026-08-28. Source: arXiv API sweep across cs.IR / cs.AI / cs.LG (Fri Aug 28 announcement wave, Thu Aug 27 submissions). 567 unique entries scanned; 28 papers covered. All IDs verified absent from wiki (grep across wiki/), zero overlap with sibling digests.*