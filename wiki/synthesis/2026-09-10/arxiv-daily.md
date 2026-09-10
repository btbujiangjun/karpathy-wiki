---
title: "arXiv Daily Report - 2026-09-10"
type: synthesis
created: 2026-09-10
updated: 2026-09-10
sources: []
tags: [arxiv, daily, LLM, recommendation, CTR, advertising, sequential-modeling, games, AI]
---

# arXiv Daily Report — 2026-09-10

Search scope: AI, LLMs, Recommendation, Advertising, CTR, Sequential Modeling, Games

---

## 1. LLMs & Long-Context Reasoning

### 1.1 ConvMem: Convolutional Memory for Long-Context Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Hongming Zhang, Zhaozhen Gu, Fengshuo Bai, Ming Hao, Qingyang Zhang, Yuanyuan Wang, Shiyang Tang, Yanna Wang, Bo Xu |
| **Institution** | Not specified |
| **arXiv** | [2609.10441](https://arxiv.org/abs/2609.10441) |
| **Date** | 2026-09-09 |
| **Subjects** | cs.AI, cs.CL |

**Abstract:** ConvMem is a training-free, highly parallelizable framework that reformulates long-context reasoning as a hierarchical convolution. It treats an LLM prompted with a specific query as a convolutional kernel that summarizes text segments hierarchically, shortening the reasoning path from a linear chain into a logarithmic tree. It integrates Configurable Strides and Skip Connections for robust evidence capture, and Multi-Kernel Convolution to decompose complex queries into disentangled semantic channels. Experiments on RULER-HotpotQA and RULER-2WikiMultiHopQA show it outperforms training-free baselines and avoids overfitting to parametric priors.

**Key Innovations:**
- Reformulates long-context LLM reasoning as hierarchical convolution (CNN-inspired)
- Logarithmic-tree reasoning path instead of linear chain (log depth vs linear)
- Training-free; no RL required; fully parallelizable
- Multi-Kernel Convolution for disentangled semantic channels

---

### 1.2 Forgetting Only What Matters: Layer-Selective Unlearning toward Robust LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Ravi Ranjan, Olivera Kotevska, Agoritsa Polyzou |
| **Institution** | Not specified |
| **arXiv** | [2609.10439](https://arxiv.org/abs/2609.10439) |
| **Date** | 2026-09-09 |
| **Subjects** | cs.LG, cs.AI |
| **Venue** | AACL-IJCNLP 2026 |

**Abstract:** Proposes FOM-UL, a layer-level unlearning framework that selects transformer layers using a forget-to-retain significance score. This identifies layers with high influence on the forget set and low sensitivity to the retain set. The framework improves the forgetting-utility trade-off and provides quantization-resilient unlearning by reducing diffuse updates that are erased by low-bit rounding.

**Key Innovations:**
- Forget-to-retain significance score for layer selection in unlearning
- Quantization-resilient: maintains forgetting under 4-bit and 8-bit PTQ
- Outperforms GA, NPO, KLD, SURE, ReLearn, and LUNAR baselines

---

### 1.3 Maverick: Private and Verifiable LLM Inference via Matrix-Vector Multiplication Delegation

| Field | Detail |
|-------|--------|
| **Authors** | Ben Merbaum, Mohammad Amin Raeisi, Wenhao Wang, Charalampos Papamanthou, Katerina Sotiraki, Fan Zhang |
| **Institution** | Not specified |
| **arXiv** | [2609.10264](https://arxiv.org/abs/2609.10264) |
| **Date** | 2026-09-09 |
| **Subjects** | cs.CR, cs.LG |

**Abstract:** Maverick provides privacy and verifiability for LLM inference through a novel matrix-vector multiplication delegation protocol. It achieves the first information-theoretically sound verification with transparent preprocessing, efficient batch verification, and virtually no server overhead. Combined with LPN-based pseudorandom masking for input privacy, it achieves up to 44x throughput gains over local inference on Qwen3-4B.

**Key Innovations:**
- Information-theoretically sound verification for matrix-vector multiplication delegation
- LPN-based pseudorandom masking for input privacy
- Up to 44x throughput improvement over local inference

---

### 1.4 The Landscape of Agentic Reinforcement Learning for LLMs: A Survey

| Field | Detail |
|-------|--------|
| **Authors** | Guibin Zhang, Hejia Geng, Xiaohang Yu, Zhenfei Yin, et al. |
| **Institution** | Multiple (published in TMLR) |
| **arXiv** | [2509.02547v5](https://arxiv.org/abs/2509.02547) |
| **Date** | 2026-04-17 (v5) |
| **Subjects** | cs.AI, cs.CL |

**Abstract:** Comprehensive survey of Agentic RL for LLMs, formalizing the shift from conventional LLM-RL (degenerate single-step MDPs) to temporally extended POMDPs defining Agentic RL. Proposes a twofold taxonomy around core agentic capabilities (planning, tool use, memory, reasoning, self-improvement, perception) and their applications. Consolidates 500+ recent works.

**Key Innovations:**
- Formalizes Agentic RL as POMDP vs. degenerate single-step MDP of LLM-RL
- Comprehensive taxonomy of agentic capabilities and applications
- Curated compendium of open-source environments, benchmarks, and frameworks

---

## 2. Recommendation Systems

### 2.1 SequenceO1: End-to-End Ultra-Long (100K) Sequence Modeling in Recommendation with Low-Rank Caching

| Field           | Detail                                                                                                                                                                                                                      |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Authors**     | Lin Guan, Jia-Qi Yang, Zhishan Zhao, Jiaqi Huang, Hangyu Wang, Longbin Li, Beichuan Zhang, Haonan Jiang, Jinan Ni, Xiangyu Fan, Xiaowen Li, Ziyao Ren, Yuhang Qi, Xiaolong Zhu, Xuanyuan Luo, Qiwei Chen, Yi Cheng, Lele Yu |
| **Institution** | ByteDance / Douyin                                                                                                                                                                                                          |
| **arXiv**       | [2609.08443](https://arxiv.org/abs/2609.08443)                                                                                                                                                                              |
| **Date**        | 2026-09-08                                                                                                                                                                                                                  |
| **Subjects**    | cs.IR, cs.AI                                                                                                                                                                                                                |
| **Venue**       | RecSys'26 Industry Track (long oral)                                                                                                                                                                                        |

**Abstract:** SequenceO1 is an end-to-end framework for ultra-long user behavior sequence modeling deployed at full traffic on Douyin with histories of up to 100K interactions. It follows a compress-then-reason design: Sketch Attention (SA) uses learnable prototypes to compress raw history into a fixed-size, target-agnostic user representation; Stacked Target-to-History Cross Attention (STCA) models complementary time scales (recent 10K suffix + compact sketch). Combines low-rank user representation caching, multi-request user-level batching, pipeline lift, and a fused FlashSA kernel.

**Key Innovations:**
- 100K-scale end-to-end sequence modeling in production (Douyin)
- Sketch Attention with learnable prototypes for history compression
- Low-rank caching for user representation reuse across targets
- FlashSA fused kernel for efficient attention computation
- Deployed at full traffic in a billion-scale recommender system

---

### 2.2 Task-Blind No MORE: Multi-Task Information Flow in Unified Ranking Backbones (MORE)

| Field | Detail |
|-------|--------|
| **Authors** | Yuchen Wang, Feng Niu, Qing Tan, Junting Lu, Baoxin Wu, Jun Gao |
| **Institution** | Momo (Chinese social discovery platform) |
| **arXiv** | [2609.07273](https://arxiv.org/abs/2609.07273) |
| **Date** | 2026-09-07 |
| **Subjects** | cs.IR |
| **Venue** | CIKM 2026 |

**Abstract:** MORE embeds multi-task information flow inside the ranking backbone (not just post-backbone towers) using Anchor Tokens that persist across layers. Shared Anchors encode cross-task commonalities; Private Anchors capture task-specific priors. Deployed on Momo (tens of millions MAU), yielding 3% improvement in usage duration, 3.6% in interaction rate, and 2% in deep-chat rate, with 30% latency reduction.

**Key Innovations:**
- Anchor Tokens for task-aware information flow inside unified backbone
- Shared + Private Anchors for cross-task vs. task-specific representations
- Request-level shared computation reducing latency by ~30%
- Online A/B tested on a major social platform

---

### 2.3 Recommender System as Slow and Fast Thinkers (DS-Frame)

| Field | Detail |
|-------|--------|
| **Authors** | Zichen Yuan, Xiaoxuan Dong, Linkun Dai, Jinwei Yang, Jining Luan, Dexu Yu, Chunxiao Li, Joemon M. Jose, Youhua Li, Hanwen Du, Junchen Fu |
| **Institution** | Multiple |
| **arXiv** | [2609.02671](https://arxiv.org/abs/2609.02671) |
| **Date** | 2026-09-02 |
| **Subjects** | cs.IR |

**Abstract:** DS-Frame is an adaptive fast-slow inference framework for sequential recommendation inspired by dual-process theory. A Fast System handles efficient routine prediction; a Slow System performs iterative latent refinement; a learned selector routes each sample under a controllable computation budget. Larger gains on challenging user groups (long histories, non-mainstream items).

**Key Innovations:**
- Dual-process (fast/slow) adaptive inference for recommendation
- Learned routing selector with controllable computation budget
- Improved accuracy-efficiency trade-off on hard-to-serve user groups

---

### 2.4 From Feature Interaction to Feature Transport (CRAFT)

| Field | Detail |
|-------|--------|
| **Authors** | Zichen Luo, Jiachen Guo, Keming Gu, Jie Zhang |
| **Institution** | Not specified |
| **arXiv** | [2609.01655](https://arxiv.org/abs/2609.01655) |
| **Date** | 2026-08-31 |
| **Subjects** | cs.IR, cs.AI |
| **Venue** | KDDCUP2026 Workshop |

**Abstract:** CRAFT treats deep unified recommendation as a discrete context-conditioned representation evolution process ("feature transport"). Non-sequential context acts as an active controller of representation evolution via residual displacement and memory-preserving signals. Achieved leaderboard-best AUC of 0.838090 on TAAC2026 advertising recommendation competition.

**Key Innovations:**
- Feature transport paradigm: context as active controller of representation evolution
- CRAFT block: Contextual Residual Adaptive Feature Transport
- Benefits from both depth and width expansion (scaling laws for recommendation)

---

### 2.5 HypRQ-VAE: Hyperbolic Item Indexing for Long-Tail-Aware Generative Recommender Systems

| Field | Detail |
|-------|--------|
| **Authors** | Longfeng Wu, Tong Zeng, Giovanni Seni, Zhimin Peng, Bhanu Pratap Singh Rawat, Si Zhang, Yao Zhou, Lecheng Zheng, Bo Ji, Yujun Yan, Dawei Zhou |
| **Institution** | Not specified |
| **arXiv** | [2609.03369](https://arxiv.org/abs/2609.03369) |
| **Date** | 2026-09-03 |
| **Subjects** | cs.IR |
| **Venue** | ICDM 2026 |

**Abstract:** First framework to learn item indexing in hyperbolic space for generative recommendation. Leverages hyperbolic geometry's exponential volume expansion to naturally accommodate power-law user-item interactions. Significantly improves recommendation for tail items while encoding rich textual semantics.

**Key Innovations:**
- First hyperbolic item indexing for generative recommendation
- Natural accommodation of power-law long-tail distributions via hyperbolic geometry
- Improved representation fidelity for sparse, niche items

---

### 2.6 An Event is Worth One Token: Event Tokenization for Industrial-scale LLM Recommendation (AMBER)

| Field | Detail |
|-------|--------|
| **Authors** | Fan Xia, Zhaoheng Zheng, Iman Setayesh, Ruogu Lin, Yiqin Pan, Samarth Mittal, Wentao Bao, Vinti Pandey, Sachin Patil, Jianpeng Cheng, Jun Xiao, Zhuang Wang, Xiangjun Fan, Sri Reddy, Minghai Chen |
| **Institution** | Meta |
| **arXiv** | [2608.25546](https://arxiv.org/abs/2608.25546) |
| **Date** | 2026-08-26 (v3: 2026-09-04) |
| **Subjects** | cs.IR |

**Abstract:** Proposes event-centric paradigm that represents each interaction by its full temporal snapshot. Introduces AMBER (Autoregressive Modeling via Bottlenecked Event Representation) which compresses each temporal snapshot into a compact Event Token — a new LLM input modality. Event Tokens are pre-computed and cached for serving, decoupling snapshot resolution from real-time compute. Advances the compute-quality Pareto frontier on industrial-scale benchmarks.

**Key Innovations:**
- Event Token: compact representation of full temporal snapshot per interaction
- Snapshot resolution as a new scaling dimension for recommendation LLMs
- End-to-end learned representation with pre-computed caching for serving
- Transfers across model architectures (works in non-LLM rankers too)

---

## 3. Advertising / CTR Prediction

### 3.1 Native Multimodal Representation Learning for CTR Prediction in E-Commerce

| Field | Detail |
|-------|--------|
| **Authors** | Chao Yi, Feifan Yang, Jiawei Feng, Sishuo Chen, Zhangming Chan, Xiang-Rong Sheng, Han Zhu |
| **Institution** | Alibaba (Taobao & Tmall Group) + USTC |
| **arXiv** | [2608.24091](https://arxiv.org/abs/2608.24091) |
| **Date** | 2026-08-25 |
| **Subjects** | cs.IR |
| **Venue** | CIKM 2026 |

**Abstract:** Addresses the mismatch between multimodal pre-training objectives and CTR prediction tasks. Proposes Mine-Then-Train method that mines high-quality, multimodally interpretable training samples from CTR data and uses them to fine-tune the multimodal encoder for better alignment with user click preferences. Demonstrated effective in offline and online experiments.

**Key Innovations:**
- Mine-Then-Train: mining interpretable multimodal samples for encoder fine-tuning
- Addresses ambiguous supervision in end-to-end multimodal CTR training
- Deployed at Alibaba Taobao

---

### 3.2 GRAB: An LLM-Inspired Sequence-First CTR Prediction Modeling Paradigm

| Field | Detail |
|-------|--------|
| **Authors** | (Baidu team) |
| **Institution** | Baidu |
| **arXiv** | [2602.01865](https://arxiv.org/abs/2602.01865) |
| **Date** | 2026-02 |
| **Subjects** | cs.IR |

**Abstract:** End-to-end generative framework for CTR prediction inspired by LLM scaling success. Integrates a unified representation feeding into an MLP enhanced with gating network to model high-order feature interactions. Full A/B testing on Baidu home feed ads shows 3.49% CTR boost and 3.05% CPM boost, leading to full production deployment.

**Key Innovations:**
- LLM-inspired sequence-first paradigm for CTR
- End-to-end generative framework replacing traditional DLRM
- Production deployed at Baidu with significant CTR/CPM gains

---

### 3.3 PromptPack: Scaling LLM Annotation Agents for Online Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Sebastian Koralewski, Merwan Barlier, Yulia Stolin, Blaž Škrlj |
| **Institution** | Not specified |
| **arXiv** | [2607.20528](https://arxiv.org/abs/2607.20528) |
| **Date** | 2026-07-10 |
| **Subjects** | cs.AI |

**Abstract:** PromptPack is a scalable, high-throughput LLM annotation agent for online recommendation platforms. Achieves scale via in-context batching with shared system prompt, strict XML structural envelope, and output correction layer. At batch size 20, cuts LLM costs by 89% and accelerates throughput by 2.5x while fully preserving AUC.

**Key Innovations:**
- In-context batching for multi-creative LLM annotation
- 89% cost reduction with 2.5x throughput improvement
- Production-validated CTR improvement from LLM-extracted features

---

### 3.4 RAMP: Robust Ad Recommendation Under Limited Personalized-Feature Availability

| Field | Detail |
|-------|--------|
| **Authors** | Dairui Liu, Zhongyi Lu, Roger Zhe Li, et al. |
| **Institution** | University College Dublin + industry collaborators |
| **arXiv** | [2607.17473](https://arxiv.org/abs/2607.17473) |
| **Date** | 2026-07-19 |
| **Subjects** | cs.IR |
| **Venue** | ICTIR '26 |

**Abstract:** RAMP improves CTR/CVR prediction when personalized features (age, gender) are unavailable due to privacy regulations. Uses dual-tower architecture with output masking to separate personalized/non-personalized signals, a separate non-personalized pathway, and distillation-inspired prediction alignment between the two.

**Key Innovations:**
- Privacy-compliant CTR/CVR prediction without personalized features
- Dual-tower with output masking for signal separation
- Distillation-based prediction alignment between personalized and non-personalized pathways

---

## 4. Sequential Modeling

### 4.1 TM20K: Ultra-long Sequence Modeling for Ad E-Commerce Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Xinchun Li, Duoru Zheng, Wenlin Zhao, Haoran Ding, Ziyi Zhou, et al. |
| **Institution** | ByteDance |
| **arXiv** | [2608.07055](https://arxiv.org/abs/2608.07055) |
| **Date** | 2026-08-07 |
| **Subjects** | cs.IR |

**Abstract:** Balances effectiveness and efficiency for 20K-scale ultra-long sequence modeling via full transformer + two-stage knowledge distillation. Student models use simple yet well-motivated token merge approaches. Teacher model trained with full sequence tokens. Deployed in ByteDance's e-commerce advertising, extending sequence length to 20K with ADSS +1.036% and only +5.6% serving latency.

**Key Innovations:**
- 20K-scale ultra-long sequence modeling in production (ByteDance e-commerce)
- Token merge approaches for efficient student models
- Two-stage knowledge distillation from full-token teacher
- Minimal serving latency increase (+5.6%)

---

### 4.2 CRAMER: Control via Request-Aware Masking for Editing Recommenders

| Field | Detail |
|-------|--------|
| **Authors** | Zhiyuan Julian Su, Naihe Feng, Zhen Luther Qin, Ga Wu |
| **Institution** | Not specified |
| **arXiv** | [2608.25370](https://arxiv.org/abs/2608.25370) |
| **Date** | 2026-08-26 |
| **Subjects** | cs.IR, cs.AI, cs.LG |
| **Venue** | ICML 2026 |

**Abstract:** CRAMER takes users' natural-language requests to immediately change sequential recommendation models' behavior. Treats user requests as control signals to modulate frozen backbone parameters through masking, achieving instant adaptation to diverse requests without retraining. Outperforms four state-of-the-art baselines with minimal overhead.

**Key Innovations:**
- Request-aware masking for instant recommendation behavior editing
- No retraining required; modulation of frozen backbone parameters
- Cross-domain adaptability

---

### 4.3 UniDot: A Unified Network for Sequence Modeling and Feature Interaction

| Field | Detail |
|-------|--------|
| **Authors** | Rongcheng Lin, Yan Sun, Jamey Zhang, Guanglei Xiong, Ivan Ji, Xianjie Chen, Shujian Bu |
| **Institution** | Not specified |
| **arXiv** | [2608.16797](https://arxiv.org/abs/2608.16797) |
| **Date** | 2026-08-17 |
| **Subjects** | cs.IR, cs.AI |
| **Venue** | KDD 2026 UniRec Workshop |

**Abstract:** Unifies feature-interaction and sequential models through the insight that embedding inner product (collaborative filtering) is the same primitive as attention's query-key scoring. A single dot-product of tokens underlies both. Uses dual sparse/dense optimizer (Adagrad + Muon) and auxiliary conversion-delay head. Runner-up on TAAC KDD Cup 2026 Industrial track.

**Key Innovations:**
- Unified dot-product primitive for feature interaction and sequence modeling
- Dual sparse/dense optimizer (Adagrad + Muon)
- Conversion-delay auxiliary head for PCVR prediction

---

### 4.4 Decoupled Temporal Encoding (DTE) for Generative Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Pengfei Jia, Jingjian Wang, Jingmao Li, Ge Zhang, Feng Shi |
| **Institution** | Not specified |
| **arXiv** | [2608.16274](https://arxiv.org/abs/2608.16274) |
| **Date** | 2026-08-17 |
| **Subjects** | cs.IR, cs.AI |
| **Venue** | CIKM '26 |

**Abstract:** Separates temporal dynamics from order information through two complementary modules: a personalized macro-temporal module that injects compact temporal primitives into item embeddings, and a time-gated micro-sequential module that introduces relative-order bias only when interactions are temporally dense. Lightweight and deployment-friendly.

**Key Innovations:**
- Decoupled temporal encoding: macro-temporal dynamics vs. micro-sequential order
- Time-gated mechanism for context-dependent order bias
- Parameter-efficient and easy to integrate into existing systems

---

### 4.5 HypRQ-VAE for Generative Recommendation (also listed in Section 2)

See Section 2.5 above.

---

## 5. Games & AI Agents

### 5.1 Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution

| Field | Detail |
|-------|--------|
| **Authors** | Jannik Hösch, Alessandro Sestini, Florian Fuchs, Amir Baghi, Joakim Bergdahl, Konrad Tollmar, Jean-Philippe Barrette-LaPierre, Linus Gisslén |
| **Institution** | Not specified |
| **arXiv** | [2606.20014](https://arxiv.org/abs/2606.20014) |
| **Date** | 2026-06-18 |
| **Subjects** | cs.LG, cs.AI |

**Abstract:** Hierarchical architecture where a pretrained LLM acts as a centralized strategic controller selecting among specialized RL skill policies for a team of agents, while RL policies handle reactive low-level execution. Evaluated in competitive 2v2 King of the Hill. Achieves 46.4% win rate (vs 51.5% hand-crafted behavior tree, p=0.103). User study (n=15) shows 60% perceive LLM+RL agents as most human-like.

**Key Innovations:**
- LLM as strategic controller + RL as reactive executor architecture
- Competitive multi-agent coordination without manual rule engineering
- Superior perceived believability in human evaluation

---

### 5.2 Spatial Reasoning in LLM Game Agents: Impact of Causal Context and Multi-Step Planning

| Field | Detail |
|-------|--------|
| **Authors** | Mohit Jiwatode, Ronja Fuchs, Robin Schmöcker, Bodo Rosenhahn, Alexander Dockhorn |
| **Institution** | TU Braunschweig |
| **arXiv** | [2607.22732](https://arxiv.org/abs/2607.22732) |
| **Date** | 2026-07-22 |
| **Subjects** | cs.AI |
| **Venue** | COG 2026 |

**Abstract:** Examines LLM game agents' spatial reasoning using Qwen3 model family across varying scales, reasoning modes, and planning horizons. Introduces a focused GVGAI benchmark with three custom games and five difficulty levels. Shows that causal context integration improves success rates, and multi-step planning reduces mean per-step response times.

**Key Innovations:**
- Systematic evaluation of LLM spatial reasoning in games
- Causal prompt augmentation for improved game performance
- Multi-step planning as speed-accuracy trade-off

---

### 5.3 RAPOA: Reward-driven Automatic Prompt Optimisation for Agentic Systems

| Field | Detail |
|-------|--------|
| **Authors** | (TU Dortmund team) |
| **Institution** | TU Dortmund University |
| **arXiv** | [2606.17838](https://arxiv.org/abs/2606.17838) |
| **Date** | 2026-06-16 |
| **Subjects** | cs.CL |

**Abstract:** Combines an LLM-based agent with an automatic prompt-evolution loop for game playing. Alternates between a standard RL loop (agent + text-based environment) and evolutionary prompt refinement. Distributes load across multiple agents (descriptor + acting + reporter + planner) for improved capabilities.

**Key Innovations:**
- Evolutionary prompt optimization driven by environment rewards
- Multi-agent decomposition (descriptor, acting, reporter, planner)
- Alternating RL loop + prompt evolution phases

---

### 5.4 Cogito, Ergo Ludo (CEL): An Agent that Learns to Play by Reasoning and Planning

| Field | Detail |
|-------|--------|
| **Authors** | (Not fully specified) |
| **Institution** | Not specified |
| **Venue** | Submitted to ICLR 2026 |
| **OpenReview** | [w2vEo7NJ18](https://openreview.net/forum?id=w2vEo7NJ18) |

**Abstract:** Novel agent architecture leveraging an LLM to build an explicit, language-based understanding of environment mechanics and strategy. Learns to play by reasoning and planning rather than encoding knowledge opaquely in neural network weights.

**Key Innovations:**
- Explicit language-based environment model instead of opaque neural weights
- Reasoning and planning as primary learning mechanism
- Interpretable strategy representation

---

## 6. Emerging Themes & Trends

1. **100K+ Sequence Modeling in Production**: SequenceO1 (Douyin) and TM20K (ByteDance) demonstrate that ultra-long user behavior sequences (20K-100K) are now feasible in production with careful system-level optimizations (caching, compression, distillation).

2. **LLM-native CTR Architectures**: GRAB (Baidu) and EST (Alibaba) show the field is moving toward Transformer-based CTR models inspired by LLM scaling laws, with LoopCTR introducing recursive computation as a new scaling dimension.

3. **Event Tokenization as a New Scaling Dimension**: AMBER (Meta) introduces snapshot resolution — how much information per event — as a new axis for scaling LLM-based recommendation.

4. **Adaptive & Efficient Inference**: DS-Frame (fast/slow thinker), CRAMER (request-aware masking), and SequenceO1 (sketch attention) all explore ways to make inference adaptive and efficient rather than uniform.

5. **Privacy-Compliant Recommendation**: RAMP addresses CTR/CVR prediction without personalized features, while FedMM tackles multi-market CTR under federated privacy constraints.

6. **LLM + RL for Games**: Hierarchical LLM-RL architectures are showing competitive performance in multi-agent games with superior perceived human-likeness.

7. **Hyperbolic Geometry for Recommendation**: HypRQ-VAE brings hyperbolic space to item indexing, naturally modeling power-law distributions in real-world catalogs.

---

*Generated on 2026-09-10 by automated arXiv search.*
