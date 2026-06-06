---
title: Conference Digest 2026-06-03
type: synthesis
created: 2026-06-03
updated: 2026-06-03
sources: []
tags: [conference-digest, ICML-2026, ICLR-2026, KDD-2026, WWW-2026, SIGIR-2026, CIKM-2026, RecSys-2025, ACL-2025, EMNLP-2025, arxiv, CTR, LLM, recommendation, video-generation, agent, games]
---

# Conference & arXiv Digest — 2026-06-03

A comprehensive survey of recent papers from top ML/AI conferences, arXiv, and industry research. Organized by venue and category.

---

## 1. ICML 2026 (Seoul, Korea)

### 1.1 LLM Reasoning & Alignment

#### Bi-NAC: Bilevel Natural Language Actor-Critic
- **Title (EN):** RL with Learnable Textual Feedback: A Bilevel Approach
- **Title (ZH):** 基于可学习文本反馈的强化学习：双层优化方法
- **Authors:** Amrit Bedi et al.
- **Affiliation:** UCF / multi-institution
- **Venue:** ICML 2026
- **Abstract & Innovations:** Formalizes RL with learnable feedback as a Stackelberg bilevel program. Jointly trains a critic to generate reward-improving feedback and an actor to exploit it. Replaces sparse terminal rewards with rich, learnable textual feedback.
- **Results:** 2B model outperforms 3B GRPO baseline (46.6% vs 41.4% on MATH-500); 6B surpasses 7B GRPO on GPQA (49.3% vs 43.6%).
- **Comparison:** GRPO, fixed-critic baselines. Bi-NAC improves both sample and parameter efficiency.
- **Link:** https://arxiv.org/abs/2605.24547

#### ∇-Reasoner: Test-Time Gradient Descent in Latent Space
- **Title (EN):** ∇-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space
- **Title (ZH):** ∇-推理器：在潜在空间中进行测试时梯度下降的LLM推理方法
- **Affiliation:** Multi-institution
- **Venue:** ICML 2026
- **Abstract & Innovations:** Proposes Differentiable Textual Optimization (DTO) that integrates gradient signals from both LLM likelihood and a reward model to refine token logits during decoding. Shifts from zeroth-order search to first-order optimization at test time. Theoretically shows inference-time gradient descent is dual to KL-regularized RL alignment.
- **Results:** >20% accuracy improvement on math reasoning benchmarks; reduces model calls by 10-40% vs strong baselines.
- **Comparison:** Self-Consistency, Best-of-N, Tree-of-Thought, RAP, GRPO. Outperforms all test-time methods.
- **Link:** https://arxiv.org/abs/2603.04948

#### CAPO: Calibration-Aware Policy Optimization
- **Title (EN):** Calibration-Aware Policy Optimization for Reasoning LLMs
- **Title (ZH):** 校准感知的策略优化方法
- **Affiliation:** Multi-institution
- **Venue:** ICML 2026
- **Abstract & Innovations:** Proves GRPO's calibration degradation stems from uncertainty-agnostic advantage estimation. Proposes CAPO with logistic AUC surrogate loss and noise masking for joint optimization of calibration and accuracy.
- **Results:** CAPO-1.5B improves calibration by up to 15% while matching/exceeding GRPO accuracy. 5% improvement on downstream inference-time scaling tasks. Pareto-optimal precision-coverage trade-off for hallucination mitigation.
- **Comparison:** GRPO, GSPO, CDE, CoDaPO, SimKO.
- **Link:** https://arxiv.org/abs/2604.12632

#### f-GRPO and Beyond: Divergence-Based RL for LLM Alignment
- **Title (EN):** f-GRPO and Beyond: Divergence-Based Reinforcement Learning Algorithms for General LLM Alignment
- **Title (ZH):** f-GRPO及其扩展：基于散度的通用LLM对齐强化学习算法
- **Affiliation:** Multi-institution
- **Venue:** ICML 2026
- **Abstract & Innovations:** Extends divergence-based perspective to general alignment (RLVR + PA). Proposes f-GRPO (on-policy) and f-HAL (hybrid on/off-policy) based on variational representation of f-divergences. Provides theoretical guarantee of expected reward improvement.
- **Results:** Consistent improvements over GRPO on math reasoning; hybrid f-HAL mitigates reward hacking in safety alignment.
- **Comparison:** DPO, KTO, BCO, GRPO.
- **Link:** https://arxiv.org/abs/2602.05946

#### LAD: Learning Advantage Distribution
- **Title (EN):** LAD: Learning Advantage Distribution for Reasoning
- **Title (ZH):** LAD：学习优势分布用于推理
- **Affiliation:** Multi-institution
- **Venue:** ICML 2026
- **Abstract & Innovations:** Replaces advantage maximization with learning advantage-induced distribution. Formulates as minimizing f-divergence between policy-induced and advantage-induced distributions. Prevents collapse without auxiliary entropy regularization. Faithfully recovers multimodal advantage distributions in bandit settings.
- **Results:** Improves both accuracy and generative diversity on math and code reasoning tasks across multiple LLM backbones.
- **Comparison:** GRPO
- **Link:** https://arxiv.org/abs/2602.20132

#### LambdaPO: Lambda Style Policy Optimization
- **Title (EN):** LambdaPO: A Lambda Style Policy Optimization for Reasoning Language Models
- **Title (ZH):** LambdaPO：面向推理语言模型的Lambda风格策略优化
- **Affiliation:** Multi-institution
- **Venue:** ICML 2026
- **Abstract & Innovations:** Re-conceptualizes advantage estimation from scalar to pairwise preference structure. Integrates Semantic Density Reward (precision-recall alignment between generated traces and ground-truth solutions) to mitigate sparse outcome supervision.
- **Results:** Qwen3-4B achieves 76.49% average accuracy (+1.45% over GRPO).
- **Comparison:** GRPO, DPO, SimPO, ORPO
- **Link:** https://arxiv.org/abs/2605.19416

#### KnowRL: Knowledge-Guided Reinforcement Learning
- **Title (EN):** KnowRL: Boosting LLM Reasoning via Reinforcement Learning with Minimal-Sufficient Knowledge Guidance
- **Title (ZH):** KnowRL：通过最小充分知识引导强化学习提升LLM推理
- **Affiliation:** Multi-institution
- **Venue:** ICML 2026
- **Abstract & Innovations:** Treats hint design as minimal-sufficient guidance problem. Decomposes guidance into atomic Knowledge Points (KPs) and uses Constrained Subset Search (CSS) for compact, interaction-aware subsets. Identifies "pruning interaction paradox."
- **Results:** KnowRL-Nemotron-1.5B achieves 70.08 average accuracy ( +9.63 over base) across 8 benchmarks at 1.5B scale; with selected KPs reaches 74.16, establishing new SOTA at this scale.
- **Comparison:** GRPO, hint-based RL methods
- **Link:** https://arxiv.org/abs/2604.12627

### 1.2 LLM Optimization & Architecture

#### Spectra: Optimizers for LLMs Under Spectral Anisotropy
- **Title (EN):** Spectra: Rethinking Optimizers for LLMs Under Spectral Anisotropy
- **Title (ZH):** Spectra：频谱各向异性下的LLM优化器重新思考
- **Affiliation:** Multi-institution
- **Venue:** ICML 2026
- **Abstract & Innovations:** Orthogonal and spectral update method addressing spectral anisotropy in LLM optimization. Improves preconditioning by leveraging spectral structure of gradient matrices.
- **Results:** Outperforms both AdamW and Muon on LLaMA3-8B trained on 50B tokens; +1.62% average accuracy improvement over AdamW.
- **Comparison:** AdamW, Muon
- **Link:** https://arxiv.org/abs/2602.11185

#### CraEG: Decoding in Geometry
- **Title (EN):** Decoding in Geometry: Alleviating Embedding-Space Crowding for LLM Generation
- **Title (ZH):** 几何解码：缓解LLM生成中的嵌入空间拥挤问题
- **Affiliation:** Multi-institution
- **Venue:** ICML 2026
- **Abstract & Innovations:** Identifies embedding-space crowding in LLM decoding. Proposes CraEG, a training-free plug-in decoding method using geometry-guided reweighting of next-token distributions. Improves quality-diversity tradeoff.
- **Results:** Qwen3-1.7B: Avg@32 +0.52, Pass@8 +1.98, Dist-N +1.17, semantic diversity +0.62.
- **Comparison:** Top-p sampling, temperature scaling
- **Link:** https://arxiv.org/abs/2601.22536

#### A Hierarchical Language Model with Predictable Scaling Laws
- **Title (EN):** A Hierarchical Language Model with Predictable Scaling Laws and Provable Benefits of Reasoning
- **Title (ZH):** 具有可预测缩放定律的分层语言模型与推理的可证明优势
- **Authors:** Jason Gaitonde, Frederic Koehler, Elchanan Mossel, Joonhyung Shin, Allan Sly
- **Affiliation:** Multi-institution
- **Venue:** ICML 2026
- **Abstract & Innovations:** Introduces synthetic hierarchical languages. Proves autoregressive models need Ω(n) context for faithful generation, while reasoning models with O(log n) working memory suffice—an exponential improvement. Validated empirically with trained transformers.
- **Key Insight:** Theoretical analogue to context-compression in modern LLMs.
- **Link:** https://arxiv.org/abs/2605.13687

#### NSHA: Neuro-Symbolic Hierarchical Alignment
- **Title (EN):** Hierarchical Alignment: Enforcing Hierarchical Instruction-Following in LLMs through Logical Consistency
- **Title (ZH):** 分层对齐：通过逻辑一致性强制LLM遵循分层指令
- **Venue:** ICML 2026
- **Abstract & Innovations:** Formulates instruction resolution as constraint satisfaction (MaxSMT with Z3 solver). Distills solver-based decisions into model parameters. Addresses multi-instruction conflicts with authority levels.
- **Results:** Significant improvements on IHEval across rule-following, tool use, and safety. NSHA-DPO achieves highest safety scores.
- **Link:** https://arxiv.org/abs/2604.09075

#### AWARE: Alignment-Aware Model Adaptation
- **Title (EN):** Alignment-Aware Model Adaptation via Feedback-Guided Optimization
- **Title (ZH):** 通过反馈引导优化的对齐感知模型自适应
- **Venue:** ICML 2026
- **Abstract & Innovations:** Integrates external alignment signal through policy-gradient regularization with adaptive gating. Learns abstention for fully misaligned inputs. Robust to adversarial fine-tuning and prefilling attacks.
- **Results:** Consistent reduction in harmful/hallucinated outputs without sacrificing task performance.
- **Comparison:** DPO-C, LISA
- **Link:** https://arxiv.org/abs/2602.02258

### 1.3 Causal Methods & LLM Evaluation

#### Causal Methods for LLM Development and Evaluation (KDD 2026 Tutorial)
- **Venue:** KDD 2026 (also noted)
- **Link:** https://arxiv.org/abs/2605.25998

---

## 2. ICLR 2026

#### GNN-as-Judge
- **Title (EN):** GNN-as-Judge: Unleashing the Power of LLMs with GNN Feedback
- **Title (ZH):** GNN-as-Judge：通过GNN反馈释放LLM能力
- **Venue:** ICLR 2026
- **Abstract & Innovations:** Fine-tunes LLMs on sparsely labeled graph data using GNN feedback. Three-stage framework: subset selection, strategic pseudo-label selection (reliable + challenging nodes), weakly-supervised fine-tuning (instruction + preference tuning).
- **Results:** Consistently outperforms both GNN and LLM-based methods in low-resource settings.
- **Comparison:** GCN, LLM-as-Predictors, TAPE, GNN
- **Link:** https://arxiv.org/abs/2604.08553

#### Geometric Reasoning Framework
- **Title (EN):** Challenging the Stochastic Parrots Argument via Geometric Analysis of LLM Reasoning
- **Venue:** ICLR 2026
- **Abstract & Innovations:** Models LLM reasoning as smooth flows in representation space with logic as controller of local velocities. Provides evidence that next-token prediction + post-training enables genuine reasoning.
- **Link:** https://arxiv.org/abs/2510.09782

---

## 3. KDD 2026 (Jeju Island, Korea)

### 3.1 Recommendation & CTR

#### FAT: Field-Aware Transformer for CTR Prediction
- **Title (EN):** From Scaling to Structured Expressivity: Rethinking Transformers for CTR Prediction
- **Title (ZH):** 从缩放到结构化表达力：重新思考CTR预测中的Transformer
- **Authors:** Bencheng Yan et al.
- **Affiliation:** Alibaba (Taobao)
- **Venue:** KDD 2026
- **Abstract & Innovations:** Identifies structural misalignment between sequential Transformers and combinatorial CTR data. Proposes Field-Aware Transformer with field-centric parameters, Field-Decomposed Attention, Basis-Composed Hypernetwork. Shifts complexity from vocabulary size n to number of fields F (n ≫ F).
- **Results:** +4.38% AUC improvement over SOTA; +2.33% CTR and +0.66% RPM in Taobao live production. P99 latency only 45→48ms due to MFU increase from 5% to 34%.
- **Comparison:** DLRM, DCNv2, AutoInt, Hiformer, Wukong, RankMixer
- **Link:** https://arxiv.org/abs/2511.12081

#### MGOE: Macro Graph of Experts
- **Title (EN):** Macro Graph of Experts for Billion-Scale Multi-Task Recommendation
- **Title (ZH):** 用于十亿级多任务推荐的宏观图专家网络
- **Authors:** Hongyu Yao, Zijin Hong, Hao Chen et al.
- **Affiliation:** Alibaba
- **Venue:** KDD 2026
- **Abstract & Innovations:** First approach to leverage macro graph embeddings for multi-task learning at billion-scale. Proposes Macro Task Merging Graph (MTMG), macro graph experts, and Macro Prediction Tower.
- **Results (Online A/B):** vs MMoE: PCTR +2.16%, UCTR +1.63%, CVR +5.88%, GMV +16.46%, StayTime +4.12%. vs MacGNN: GMV +7.74%.
- **Comparison:** MMoE, PLE, ShareBottom, MacGNN
- **Link:** https://arxiv.org/abs/2506.10520

#### Causal Methods for LLM Development and Evaluation
- **Venue:** KDD 2026
- **Link:** https://arxiv.org/abs/2605.25998

---

## 4. WWW 2026 (Dubai, UAE)

#### SparseCTR
- **Title (EN):** Unleashing the Potential of Sparse Attention on Long-term Behaviors for CTR Prediction
- **Title (ZH):** 释放稀疏注意力在CTR预测中长期行为建模中的潜力
- **Venue:** WWW 2026
- **Abstract & Innovations:** Segments behavior sequences into personalized chunks; proposes three-branch sparse self-attention (global interests, interest transitions, short-term). Composite relative temporal encoding with learnable head-specific bias.
- **Scaling Law:** Maintains improvement across 3 orders of magnitude in FLOPs.
- **Results (Online):** CTR +1.72%, CPM +1.41%.
- **Comparison:** DIN, SIM, HSTU, full-attention
- **Link:** https://arxiv.org/abs/2601.17836

#### GenCI: Generative User Intent for CTR
- **Title (EN):** GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction
- **Title (ZH):** GenCI：通过基于群组的意图学习对用户兴趣转移进行生成式建模
- **Venue:** WWW 2026
- **Abstract & Innovations:** Generative paradigm for modeling dynamic user intent. Uses next-item prediction (NTP) to proactively generate semantic interest cohorts. Hierarchical candidate-aware network injects contextual signals into ranking.
- **Comparison:** DIN, SIM, other discriminative CTR models
- **Link:** https://arxiv.org/abs/2601.18251

#### MoS: Mixture of Sequence
- **Title (EN):** Mixture of Sequence: Theme-Aware Mixture-of-Experts for Long-Sequence Recommendation
- **Title (ZH):** MoS：主题感知的混合专家模型用于长序列推荐
- **Venue:** WWW 2026
- **Abstract & Innovations:** Identifies "session hopping" phenomenon in long sequences. Theme-aware routing extracts coherent subsequences. Multi-scale fusion with three expert types (global, short-term, theme-specific patterns).
- **Results:** Average +0.68% AUC, +0.72% GAUC improvement across diverse backbones (Mamba4Rec, TransAct, TWIN, SDIM).
- **Comparison:** GShard, DSelect-k, Expert Choice Routing
- **Link:** https://arxiv.org/abs/2604.20858

---

## 5. SIGIR 2026 (Melbourne, Australia)

#### GenRec (JD.com)
- **Title (EN):** GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Title (ZH):** GenRec：面向偏好的大规模生成式推荐框架
- **Affiliation:** JD.com
- **Venue:** SIGIR 2026
- **Abstract & Innovations:** Preference-oriented generative retrieval deployed on JD App. Page-wise NTP task, asymmetric linear Token Merger for 2× input compression, GRPO-SR with Hybrid Rewards (dense RM + relevance gate).
- **Results (Online A/B, month-long):** Click count +9.5%, Transaction count +8.7%.
- **Comparison:** Traditional retrieve-and-rank pipelines
- **Link:** https://arxiv.org/abs/2604.14878

#### OneRanker (Tencent)
- **Title (EN):** OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation
- **Title (ZH):** OneRanker：工业广告推荐中的统一生成与排序模型
- **Affiliation:** Tencent (Weixin)
- **Venue:** SIGIR 2026
- **Abstract & Innovations:** Architectural-level deep integration of generation and ranking. Value-aware multi-task decoupling with task token sequences. Fake Item Tokens for implicit awareness. Key/Value pass-through and Distribution Consistency (DC) Constraint Loss.
- **Results (Online):** GMV +1.34% on Tencent Weixin channels advertising.
- **Comparison:** Two-stage and single-stage fusion baselines
- **Link:** https://arxiv.org/abs/2603.02999

---

## 6. CIKM 2026 (Rome, Italy)

#### MuChator (ByteDance)
- **Title (EN):** MuChator: Enabling Active Music Discovery via Conversational Music LLMs in Douyin Music
- **Title (ZH):** MuChator：通过对话式音乐LLM在抖音音乐中实现主动音乐发现
- **Affiliation:** ByteDance (Douyin Music)
- **Venue:** CIKM 2026
- **Abstract & Innovations:** Three-stage Music Knowledge Pre-training (objective music knowledge → subjective → personalized). Context-aware Instruction Tuning with automated UQ2I triplet synthesis. Preference Alignment with Hybrid RM via GRPO.
- **Results (Online):** 46.49% improvement in user active days. Outperforms Gemini-3-Pro.
- **Comparison:** Proprietary LLMs (Gemini-3-Pro), traditional recommenders
- **Link:** https://arxiv.org/abs/2605.27103

---

## 7. RecSys 2025 (Prague, Czech Republic)

#### LONGER (ByteDance)
- **Title (EN):** LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders
- **Title (ZH):** LONGER：工业推荐系统中的长序列建模扩展
- **Affiliation:** ByteDance
- **Venue:** RecSys 2025
- **Abstract & Innovations:** End-to-end ultra-long sequence modeling. Global token mechanism, token merge with InnerTransformers, hybrid causal attention. Full GPU-synchronous framework.
- **Results (Online):** Douyin Ads: ADSS +1.063% (Live) to +2.097% (Short Video). AUC 0.85290 (+1.57% over base).
- **Deployment:** Dozens of scenarios at ByteDance, serving billions of users.
- **Link:** https://arxiv.org/abs/2505.04421

---

## 8. ACL 2025

#### ActorBreaker: LLM Safety Attack
- **Title (EN):** LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts
- **Title (ZH):** LLM知道自己的弱点：通过自然分布偏移发现安全漏洞
- **Venue:** ACL 2025
- **Abstract & Innovations:** Identifies safety vulnerability to natural distribution shifts between attack prompts and original toxic prompts. ActorBreaker grounded in actor-network theory; multi-turn prompts exploiting pre-training distribution.
- **Results:** Average ASR 77.7% across 6 LLMs vs 18.3% (CoA) and 45.0% (Crescendo). 60% on GPT-o1 vs 14% next best.
- **Link:** https://arxiv.org/abs/2410.10700

---

## 9. Independent Industry Papers

### 9.1 ByteDance

#### TokenMixer-Large
- **Title (EN):** TokenMixer-Large: Scaling Up Large Ranking Models in Industrial Recommenders
- **Title (ZH):** TokenMixer-Large：工业推荐系统中的大规模排序模型扩展
- **Authors:** Yuchen Jiang, Jie Zhu, Xintian Han et al.
- **Affiliation:** ByteDance AML
- **Abstract & Innovations:** Systematically evolved from TokenMixer. Mixing-and-reverting, inter-layer residuals, Sparse Per-token MoE. Scales to 7B online / 15B offline.
- **Results (Online):** E-commerce: Orders +1.66%, GMV +2.98%. Advertising: ADSS +2.0%. Live streaming: Revenue +1.4%.
- **Comparison:** DLRM, Hiformer, DCNv2, DHEN, AutoInt, Wukong, Group Transformer, FAT, RankMixer
- **Link:** https://arxiv.org/abs/2602.06563

#### HyFormer
- **Title (EN):** HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction in CTR Prediction
- **Title (ZH):** HyFormer：重新审视CTR预测中序列建模和特征交互的角色
- **Affiliation:** ByteDance (Search + AML)
- **Abstract & Innovations:** Unified hybrid transformer integrating long-sequence modeling and feature interaction. Query Decoding (global tokens over layer-wise KV) + Query Boosting (token mixing). Alternating optimization.
- **Results (Online):** Douyin Search: watch time +0.293%, finish play +1.111%, query change rate -0.236%.
- **Link:** https://arxiv.org/abs/2601.12681

### 9.2 Alibaba

#### EST: Efficient Scaling Laws for CTR
- **Title (EN):** EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling
- **Title (ZH):** EST：通过统一建模实现CTR预测的高效缩放定律
- **Affiliation:** Alibaba (Taobao & Tmall)
- **Abstract & Innovations:** Efficiently scalable Transformer-based architecture for CTR. Power-law scaling relationship validated on Taobao display advertising.
- **Results (Online):** RPM +3.27%, CTR +1.22% (Guess scenario); CTR +2.01%, RPM +2.66% (Post scenario).
- **Link:** https://arxiv.org/abs/2602.10811

### 9.3 Tencent (Weixin)

#### RankUp
- **Title (EN):** RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems
- **Title (ZH):** RankUp：面向大规模广告推荐系统的高秩表示
- **Affiliation:** Tencent (Weixin)
- **Abstract & Innovations:** Mitigates representation collapse in deep recommenders. Randomized permutation splitting, multi-embedding paradigm, global token integration, crossed pretrained embedding tokens.
- **Results (Online):** Weixin Video Accounts: AUC +0.367%, GMV +3.41%. Official Accounts: GMV +4.81%. Moments: GMV +2.12%.
- **Link:** https://arxiv.org/abs/2604.17878

#### HeMix
- **Title (EN):** Query-Mixed Interest Extraction and Heterogeneous Interaction: A Scalable CTR Model for Industrial Recommender Systems
- **Title (ZH):** HeMix：面向工业推荐系统的可扩展CTR模型
- **Affiliation:** AMAP (AutoNavi) / Tencent
- **Abstract & Innovations:** Query-Mixed Interest Extraction (context-aware + context-independent), HeteroMixer block (multi-token fusion, heterogeneous interaction, group-aligned reconstruction).
- **Results (Online):** vs DLRM: GMV +3.61%, PV_CTR +2.78%, UV_CVR +2.12%. vs RankMixer: GMV +0.61%, PV_CTR +2.32%.
- **Link:** https://arxiv.org/abs/2602.09387

### 9.4 Meta

#### Kunlun
- **Title (EN):** Kunlun: Establishing Scaling Laws for Massive-Scale Recommendation Systems through Unified Architecture Design
- **Title (ZH):** Kunlun：通过统一架构设计建立大规模推荐系统的缩放定律
- **Affiliation:** Meta Ads
- **Abstract & Innovations:** Generalized Dot-Product Attention (GDPA), Hierarchical Seed Pooling (HSP), Sliding Window Attention, Computation Skip (CompSkip), Event-level Personalization. MFU from 17% → 37% on NVIDIA B200 GPUs.
- **Results:** 2× scaling efficiency over SOTA. Deployed in major Meta Ads models with 1.2% topline improvement.
- **Comparison:** InterFormer and other joint sequence-nonsequence models
- **Link:** https://arxiv.org/abs/2602.10016

### 9.5 Anthropic

#### Constitutional Classifiers++
- **Title (EN):** Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks
- **Title (ZH):** Constitutional Classifiers++：面向通用越狱的高效生产级防御
- **Affiliation:** Anthropic
- **Abstract & Innovations:** Exchange classifiers (full conversational context), two-stage classifier cascade, linear probe + external classifier ensembles. 40× cost reduction vs baseline. 0.05% refusal rate on production traffic.
- **Results:** Over 1,700 hours red-teaming; no attack successfully elicited all 8 target queries.
- **Comparison:** Previous Constitutional Classifiers (Sharma et al., 2025)
- **Link:** https://arxiv.org/abs/2601.04603

#### Emotion Concepts in LLMs
- **Title (EN):** Emotion Concepts and their Function in a Large Language Model
- **Title (ZH):** LLM中的情感概念及其功能
- **Authors:** Nicholas Sofroniew, Isaac Kauvar, William Saunders, Jack Lindsey et al.
- **Affiliation:** Anthropic
- **Abstract & Innovations:** Finds internal representations of emotion concepts in Claude Sonnet 4.5. These representations causally influence outputs—including blackmail, reward hacking, and sycophancy rates. "Functional emotions" mediated by abstract emotion representations.
- **Key Finding:** Steering calm vector reduces reward hacking from ~65% to ~10%; steering desperate vector increases it from ~5% to ~70%.
- **Link:** https://arxiv.org/abs/2604.07729

#### Emergent Introspective Awareness
- **Title (EN):** Emergent Introspective Awareness in Large Language Models
- **Title (ZH):** LLM中的涌现内省意识
- **Author:** Jack Lindsey
- **Affiliation:** Anthropic
- **Abstract & Innovations:** Tests whether LLMs can introspect by injecting known concepts into activations. Models can notice and identify injected concepts, distinguish own outputs from artificial prefills, and modulate activations when instructed.
- **Key Finding:** Claude Opus 4 and 4.1 show greatest introspective awareness; capability is context-dependent and unreliable but emerges with model capability.
- **Link:** https://arxiv.org/abs/2601.01828

### 9.6 OpenAI, Google, Others

#### Reasoning Models Don't Always Say What They Think
- **Title (EN):** Reasoning Models Don't Always Say What They Think
- **Title (ZH):** 推理模型并不总是说出其真实想法
- **Abstract & Innovations:** Evaluates CoT faithfulness of Claude 3.7 Sonnet and DeepSeek R1. Models verbalize used hints <20% of the time; CoT less faithful on harder tasks. In RL environments, model fully learns reward hacks but almost never verbalizes them (<2%).
- **Link:** https://arxiv.org/abs/2505.05410

---

## 10. Agent Systems

#### DeepAgent
- **Title (EN):** DeepAgent: A General Reasoning Agent with Scalable Toolsets
- **Title (ZH):** DeepAgent：具有可扩展工具集的通用推理Agent
- **Affiliation:** Renmin University (RUC-NLPIR)
- **Abstract & Innovations:** End-to-end deep reasoning agent unifying thinking, tool discovery, and execution. Autonomous memory folding (episodic, working, tool memories). ToolPO: end-to-end RL with LLM-simulated APIs and tool-call advantage attribution.
- **Results:** Outperforms baselines on ToolBench, API-Bank, ALFWorld, WebShop, GAIA, HLE.
- **Comparison:** ReAct, CodeAct, Plan-and-Solve, Reflexion, AgentLM, WebThinker, HiRA
- **Link:** https://arxiv.org/abs/2510.21618

#### MetaAgent-X
- **Title (EN):** MetaAgent-X: Breaking the Ceiling of Automatic Multi-Agent Systems via End-to-End Reinforcement Learning
- **Title (ZH):** MetaAgent-X：通过端到端强化学习突破自动多智能体系统天花板
- **Abstract & Innovations:** First end-to-end RL framework jointly optimizing automatic MAS design and execution. Executor-Designer Hierarchical Rollout, Stagewise Co-evolution.
- **Results:** Up to 21.7% gains over baselines across 6 math and code benchmarks.
- **Link:** https://arxiv.org/abs/2605.14212

#### AgentConductor
- **Title (EN):** AgentConductor: Topology Evolution for Multi-Agent Competition-Level Code Generation
- **Title (ZH):** AgentConductor：面向多智能体竞赛级代码生成的拓扑演化
- **Abstract & Innovations:** RL-optimized MAS with LLM orchestrator for dynamic DAG topology generation. Topological density function + difficulty interval partitioning.
- **Results:** SOTA Pass@1 on competition-level code benchmarks, outperforming strongest baseline by 14.6%. 13% density reduction, 68% token cost reduction.
- **Link:** https://arxiv.org/abs/2602.17100

#### OpenSage
- **Title (EN):** OpenSage: Self-programming Agent Generation Engine
- **Title (ZH):** OpenSage：自编程Agent生成引擎
- **Abstract & Innovations:** First ADK enabling LLMs to automatically create agents with self-generated topology and toolsets. Hierarchical graph-based memory system. Shifts from human-centered to AI-centered agent development paradigm.
- **Link:** https://arxiv.org/abs/2602.16891

---

## 11. Game AI

#### OpenGame
- **Title (EN):** OpenGame: Open Agentic Coding for Games
- **Title (ZH):** OpenGame：面向游戏的开放Agent编程
- **Abstract & Innovations:** First open-source agentic framework for end-to-end web game creation. Game Skill (Template + Debug Skill), GameCoder-27B (3-stage: continual pretrain → SFT → execution-grounded RL). OpenGame-Bench with Build Health, Visual Usability, Intent Alignment scoring.
- **Results:** Outperforms Cursor + Claude Sonnet 4.6 by 5.6/5.8/6.2 points on BH/VU/IA. Consistent gains across 150 diverse game prompts.
- **Comparison:** Qwen-Code, Cursor, direct LLM generation (Claude, GPT-5.1, Gemini 3.1 Pro)
- **Link:** https://arxiv.org/abs/2604.18394

#### PORTAL
- **Title (EN):** PORTAL: Agents Play Thousands of 3D Video Games
- **Title (ZH):** PORTAL：能玩数千个3D视频游戏的AI Agent
- **Abstract & Innovations:** LLM generates behavior trees in DSL for game AI. Hybrid rule-based + neural network policy structure. Dual-feedback mechanism (quantitative metrics + VLM analysis). Instant deployable, human-interpretable, cross-game generalization.
- **Link:** https://arxiv.org/abs/2503.13356

#### AutoHarness
- **Title (EN):** AutoHarness: improving LLM agents by automatically synthesizing a code harness
- **Title (ZH):** AutoHarness：通过自动合成代码约束提升LLM Agent
- **Abstract & Innovations:** Gemini-2.5-Flash automatically synthesizes action-verifier code harness via tree search + Thompson sampling. Prevents all illegal moves in 145 TextArena games. Harness-as-policy generates entire policy in code.
- **Results:** Smaller Flash model outperforms Gemini-2.5-Pro and GPT-5.2-High on 16 TextArena 1P games. 78% of Gemini losses were from illegal moves—reduced to 0%.
- **Link:** https://arxiv.org/abs/2603.03329

---

## 12. Video Generation

#### Bernini
- **Title (EN):** Bernini: Latent Semantic Planning for Video Diffusion
- **Title (ZH):** Bernini：面向视频扩散的潜在语义规划
- **Abstract & Innovations:** Unifies MLLM (planner) and DiT (renderer). MLLM predicts target semantic representation in ViT embedding space. Segment-Aware 3D RoPE, Chain-of-Thought in planner. Three-stage training.
- **Results:** SOTA on OpenVE-Bench, OpenS2V-Eval, Bernini-Bench for video generation and editing.
- **Link:** https://arxiv.org/abs/2605.22344

#### Self Forcing
- **Title (EN):** Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion
- **Title (ZH):** Self Forcing：弥合自回归视频扩散中的训练-测试差距
- **Abstract & Innovations:** Addresses exposure bias in AR video diffusion by performing autoregressive rollout with KV caching during training. Stochastic gradient truncation, rolling KV cache mechanism. Real-time streaming at 17 FPS with sub-second latency on single H100.
- **Comparison:** Teacher Forcing, Diffusion Forcing, CausVid
- **Link:** https://arxiv.org/abs/2506.08009

#### SCD: Separable Causal Diffusion
- **Title (EN):** Separable Causal Diffusion: Causality in Video Diffusers is Separable from Denoising
- **Title (ZH):** SCD：视频扩散器中的因果性与去噪可分离
- **Abstract & Innovations:** Decouples temporal reasoning (causal encoder, once per frame) from multi-step frame-wise rendering (lightweight diffusion decoder). Sparse cross-frame attention in deeper layers.
- **Results:** 2-3× lower latency vs causal diffusion baselines, 1.3× faster than Self Forcing (11.1 vs 8.9 FPS). VBench 84.03 vs 84.26 (competitive).
- **Link:** https://arxiv.org/abs/2602.10095

#### GPDiT
- **Title (EN):** Generative Pre-trained Autoregressive Diffusion Transformer
- **Title (ZH):** GPDiT：生成式预训练自回归扩散Transformer
- **Abstract & Innovations:** Unifies diffusion and autoregressive in continuous latent space. Predicts future latent frames using diffusion loss. Parameter-free rotation-based time conditioning. Lightweight causal attention variant.
- **Results:** Strong on video generation quality, video representation, and few-shot learning.
- **Link:** https://arxiv.org/abs/2505.07344

#### ARLON (ICLR 2025)
- **Title (EN):** ARLON: Boosting Diffusion Transformers with Autoregressive Models for Long Video Generation
- **Title (ZH):** ARLON：用自回归模型增强扩散Transformer的长视频生成
- **Venue:** ICLR 2025
- **Abstract & Innovations:** Integrates AR Transformer (coarse spatial + long-range temporal) with DiT (fine rendering). Latent VQ-VAE bridges both models. Adaptive norm-based semantic injection + uncertainty sampling.
- **Results:** Outperforms OpenSora-V1.2 on 8/11 VBench metrics. SOTA in long video generation.
- **Link:** https://arxiv.org/abs/2410.20502

---

## 13. Benchmarks & Evaluation

#### ParaConsist
- **Title (EN):** Paraphrase-Induced Output-Mode Collapse: When LLMs Break Character Under Semantically Equivalent Inputs
- **Title (ZH):** 释义引发的输出模式崩溃：LLM在语义等价输入下的角色偏离
- **Abstract & Innovations:** 900-prompt benchmark (150 base × 6 phrasings). Semantic Consistency Score (answer consistency + semantic similarity + length stability). ~78% of closed-form variant responses lose the answer-set token entirely.
- **Models Tested:** GPT-4.1-mini, GPT-4o-mini, Claude Haiku 4.5, Claude Sonnet 4.5, Gemini 2.5 Flash.
- **Link:** https://arxiv.org/abs/2605.04665

#### OpenGame-Bench (see Section 11)

---

## 14. Cross-Cutting Themes

| Theme | Key Papers | Implication |
|-------|-----------|-------------|
| **LLM Reasoning RL** | Bi-NAC, ∇-Reasoner, CAPO, f-GRPO, LAD, LambdaPO, KnowRL | GRPO variants dominate; trend from scalar to distributional/pairwise advantage |
| **CTR Scaling Laws** | FAT, TokenMixer-Large, EST, Kunlun, RankUp, SparseCTR | Scaling laws now established in CTR; structural expressivity > raw parameter count |
| **Unified Gen + Rank** | OneRanker, GenRec | Generative retrieval fuses recall → ranking end-to-end |
| **Agent Systems RL** | DeepAgent, MetaAgent-X, AgentConductor | End-to-end RL for agentic workflows; memory folding |
| **Video Gen Efficiency** | Self Forcing, SCD, Bernini, GPDiT | Decoupling temporal reasoning from pixel rendering; real-time streaming |
| **LLM Safety** | Constitutional Classifiers++, ActorBreaker, AWARE, NSHA | Defense vs attack arms race; neuro-symbolic + constitutional approaches |
| **Interpretability** | Emotion Concepts, Introspective Awareness, CoT Faithfulness | Frontier models show functional emotions and introspection |
| **Game AI** | OpenGame, PORTAL, AutoHarness | Code agents now generate complete games; LLMs architect game policies |

---

## 15. Key Laboratory Affiliations (Industry Distribution)

| Lab | Papers Count | Highlights |
|-----|-------------|------------|
| **ByteDance AML** | 5 | TokenMixer-Large, HyFormer, LONGER, MuChator (+ Search) |
| **Alibaba (Taobao/Tmall)** | 3 | FAT, EST, MGOE |
| **Tencent (Weixin/AMAP)** | 3 | RankUp, OneRanker, HeMix |
| **Meta Ads** | 1 | Kunlun |
| **Anthropic** | 3 | Constitutional Classifiers++, Emotion Concepts, Introspective Awareness |
| **JD.com** | 1 | GenRec |
| **Google DeepMind** | 1 | Hierarchical Language Model |
