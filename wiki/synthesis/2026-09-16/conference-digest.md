---
title: "Conference Digest: Upcoming-Venue Acceptances + 2025-26 Award Retrospective — 2026-09-16"
type: synthesis
created: 2026-09-16
updated: 2026-09-16
sources: [conference-web-searches, arxiv-api]
tags: [conference-digest, ICML2026, ICLR2026, AAAI2026, NeurIPS2025, NeurIPS2026, KDD2026, CVPR2026, SIGIR2026, ACL2026, EMNLP2025, EMNLP2026, WWW2026, CIKM2025, CIKM2026, RecSys2025, RecSys2026, recommendation, LLM, advertising, CTR, agents, generative-models, sequential-modeling, games, code-execution, benchmarks]
---

# Conference Digest: Upcoming-Venue Acceptances + 2025-26 Award Retrospective (2026-09-16)

> Focus: the *new* acceptances that landed since the 09-11 full edition — EMNLP 2026 / CIKM 2026 / RecSys 2026 papers are freshly on arXiv with venue tags — plus the award sets for SIGIR 2026, ACL 2026, ICML 2026, and NeurIPS 2026 logistics. Every arXiv ID in this digest is grep-verified **0 hits** in `wiki/` (deduped against 09-15 / 09-16 siblings). Venues that were fully digested on 09-11 are summarized compactly as award retrospects with pointers to prior pages.

---

## 1. Venue Highlights — What's New This Cycle

| Venue | Date | Status | New in this digest |
|---|---|---|---|
| RecSys 2026 | Sep 28 – Oct 2 | Upcoming (in 12 days) | Acceptor list public; **WHALE** (Meta), **MPZCH** (Meta+OpenAI) accepted long papers — both new |
| CIKM 2026 (35th) | Oct 2026 | Upcoming, acceptances flowing | **FAE/REAL** evidence-grounded fact-checking — new |
| EMNLP 2026 | Nov 2026 | Acceptances just posted | 4 new papers (Main + Findings) — fact-grounding gap, Magnitude Mirage, Cognition on Graph, demographics in assessment |
| NeurIPS 2026 | Dec 6–12 (Sydney) + satellites | Author notifications **Sep 24** (8 days out) | Workshop slate (102), multi-site logistics, decision timeline |
| SIGIR 2026 | Jul 20–24 2026 | Held | Full award set (Best/Best Short/Best Student/ToT) |
| ACL 2026 | Jul 2–7 2026 | Held | Full award set incl. Outstanding papers |
| KDD 2026 | Aug 9–13 2026 | Held | Wrap-up of industrial GR/ads papers |
| ICML 2026 / ICLR 2026 / NeurIPS 2025 / CVPR 2026 / WWW 2026 / AAAI 2026 | various | Held | Compact award retrospect — see [[conference-digest 2026-09-11\|2026-09-11 Full Edition]] |

---

## 2. RecSys 2026 (Minneapolis, Sep 28 – Oct 2) — New Accepted Papers

### 2.1 WHALE: A Scalable Unified Model for Recommendation with Wukong-HSTU Architecture
- **英文 Title**: WHALE: A Scalable Unified Model for Recommendation with Wukong-HSTU Architecture
- **中文 Title**: WHALE：融合 Wukong-HSTU 架构的可扩展统一推荐模型
- **Authors**: Renqin Cai, Dawei Sun, Yuanjun Yao, Zhiyong Wang, Velvin Fu, Maggie Zhuang, Yu Shi, Zhongnan Fang, Xuan Cao, Jing Qian, Rui Li
- **Affiliation**: Meta (production-recommender systems team)
- **Venue**: RecSys 2026 Main Track, Long Paper. DOI 10.1145/3773078.3831927
- **arXiv**: https://arxiv.org/abs/2607.17017

**Problem background**: Industrial recommendation needs two complementary "sources of ranking signal": (a) non-sequence features (user/item/context/cross features) and (b) sequence features (long user-behavior histories). These are normally modeled on separate paths. Wukong has become the representative scalable backbone for high-order *non-sequence* feature interactions; HSTU (Meta, ICML 2024) is the representative scalable backbone for long *behavior-sequence* modeling. Architectures that unify both without sacrificing either remain underexplored.

**Methodology**: WHALE stacks layers where each layer contains three modules:
1. **Wukong module** — models n-order interactions of non-sequence features (produces `H_ns^(l) ∈ R^{N×D}`);
2. **HSTU module** — models behavior sequences (gated linear recurrence + attention, subquadratic);
3. **Attention-based fusion module** — Wukong-derived interaction representations *query* HSTU-derived behavior representations.

The progressive Wukong↔HSTU exchange keeps both backbones active through the whole network, so high-order feature crosses repeatedly retrieve fine-grained evidence from long user histories. Custom Triton kernels + model-systems co-design make it deployable.

**Key innovations**: (1) First practical unification of Wukong-style non-sequence interactions with HSTU-style sequence modeling inside one architecture; (2) attention cross-query fusion as a per-layer operation rather than a late merge; (3) Triton-kernelized training/inference so scaling does not collapse serving throughput.

**Experimental results** (Meta industrial data):
- Offline: consistent gains across model scales; normalized-entropy (NE) gains keep increasing with sequence length (0% @3K/9 GFLOPs → 0.32% @6K/16 GFLOPs → 0.65% @10K/26 GFLOPs → 0.95% @15K/38 GFLOPs) — i.e., WHALE shows consistent scaling with additional capacity for long sequences.
- Online A/B vs production baseline: **primary metric +0.113%**, Metric 1 **+0.824%**, Metric 2 **+1.820%**, at the cost of **5% inference QPS regression** (acceptable within serving budget). Deployed in production.

**Comparison with prior methods**: vs Wukong-only or HSTU-only models, WHALE unifies rather than selects; vs naive concurrent/parallel fusion, the attention query mechanism gives HSTU evidence a targeted role, and scaling behavior holds across model sizes.

### 2.2 MPZCH: Multi-Probe Zero Collision Hash — Mitigating Embedding Collisions and Enhancing Model Freshness in Large-Scale Recommenders
- **英文 Title**: Multi-Probe Zero Collision Hash (MPZCH): Mitigating Embedding Collisions and Enhancing Model Freshness in Large-Scale Recommenders
- **中文 Title**: MPZCH：面向大规模推荐系统的零碰撞哈希（缓解 Embedding 碰撞、提升模型新鲜度）
- **Authors**: Ziliang Zhao, Bi Xue, Emma Lin, Tianqi Lu, Mengjiao Zhou, Kaustubh Vartak, Shakhzod Ali-Zade, Tao Li, Bin Kuang, Rui Jian, Bin Wen, Dennis van der Staay, Yixin Bao, Eddy Li, Chao Deng, Henry Wei, Songbin Liu, Qifan Wang, Kai Ren
- **Affiliation**: Meta Platforms, Inc. + OpenAI
- **Venue**: RecSys 2026, Long Paper (9 pages), DOI 10.1145/3773078.3831927
- **arXiv**: https://arxiv.org/abs/2602.17050

**Problem background**: Large-scale recommenders (DLRM-class) dodge the *vocabulary-size* curse with **hash-based embedding slots**: many IDs share one slot. When a new ID collides with a stale/obsolete ID's slot, the new entity silently "inherits" an unrelated pre-trained embedding. Existing collision-avoidance work lacks any mechanism to *retire* obsolete IDs, so freshness and semantic fidelity degrade together.

**Methodology**: MPZCH is a GPU kernel + metadata extension (co-sharded with each embedding table):
1. **Lookup in two passes**: Pass 1 scans a range to find the target ID's slot; Pass 2 performs the read/write based on outcome — a SIMD-friendly zero-collision primitive.
2. **Per-ID lifecycle**: metadata carries expiration thresholds; on lookup, a slot holding an expired (stale) ID is marked and the incoming ID is **evicted-in / written anew**, breaking the "inherit unrelated embedding" failure.
3. **Different policies for users vs items**: user embeddings prioritize *collision elimination*; item embeddings prioritize *freshness and fast convergence* (new items must quickly learn, and must not reuse dead vectors).

**Key innovations**: (1) Zero-collision mapping without a true-hash dictionary (constant memory, GPU-native); (2) explicit ID retirement that re-opens slots instead of poisoning them; (3) per-ID-domain policy split.

**Significance**: Addresses the under-reported reliability gap between offline accuracy and long-lived production recommender health (staleness, cold-start, server drift). Experimental context covers large-scale Meta ranking pipelines.

### 2.3 RecSys 2026 context
- RecSys 2026 long-paper acceptance list is public (alphabetical). Emerging themes: sequential recommendation input–target pattern learning, LTR with implicit feedback + position handling, and *agent-native* retraining governance (RTagent: RL meta-policy for when to retrain under a global retraining-count budget).
- **Workshop collocated**: GenAIECommerce'26 (Agentic & Generative AI for E-Commerce) — its paper AURA (agentic production-rec diagnosis, **2609.16625**) was already featured in today's [[arxiv-ai-search 2026-09-16|arxiv-ai-search 2026-09-16]]; not re-covered here.
- Previously covered RecSys'26 work: **2609.13678** (cross-stage decoupling of semantic/collaborative signals in GR) and **LO-FAR** (2607.20873, Meituan cost-aware feature filter) — see 09-16 arxiv-daily / 08-19 conference-digest.

---

## 3. EMNLP 2026 (Nov 2026) — New Accepted Papers (fresh acceptances)

### 3.1 Diagnosing the Fact-Grounding Gap in Multi-Hop Question Answering [Main]
- **英文 Title**: Diagnosing the Fact-Grounding Gap in Multi-Hop Question Answering
- **中文 Title**: 诊断多跳问答中的事实锚定缺口
- **Authors**: Kevin Mo, Nathan Mo, Richard Zhu
- **Affiliation**: —
- **Venue**: EMNLP 2026 Main Conference
- **arXiv**: https://arxiv.org/abs/2609.17043

**Problem background**: Multi-hop QA systems fail, and the field usually blames **retrieval** ("the right document wasn't found"). Whether this is true at the level of *individual reasoning hops* was unexamined.

**Key finding — the fact-grounding gap**: Across three standard multi-hop benchmarks, per-hop failures decompose into (a) **retrieval failures** (passage not retrieved) and (b) **extraction failures** (passage retrieved but the needed fact cannot be extracted). Extraction failures account for **~50%** of per-hop deficiencies and are *invisible to standard retrieval metrics* (Recall/RR). Every retrieval intervention tested fails to fix them → a hard **ceiling for retrieval-only improvements**. Severity varies by benchmark and question type, but extraction failures appear on every dataset.

**Significance**: Prescribes a two-track fix agenda (better *reasoning/extraction*, not more retrieval), and argues current evaluation conflates two different bottlenecks.

### 3.2 The Magnitude Mirage: Rethinking Confidence for Reasoning-Intensive Retrieval [Main]
- **英文 Title**: The Magnitude Mirage: Rethinking Confidence for Reasoning-Intensive Retrieval
- **中文 Title**: 幅度幻象：重新审视推理型检索的置信度
- **Authors**: Jamie Holdcroft, Abdelrahman Abdallah, Adam Jatowt
- **Affiliation**: University of Innsbruck (tentative)
- **Venue**: EMNLP 2026
- **arXiv**: https://arxiv.org/abs/2609.15578

**Problem background**: Production RAG does *retrieval abstention* ("don't answer if the evidence is weak") by thresholding raw similarity scores — treating **score magnitude as confidence**. This degrades as queries need reasoning beyond token/semantic matching.

**Key finding**: Across **11 retrieval architectures and 28 datasets**, neural retrievers consistently give *high* similarity to semantically-related-but-constraint-violating documents (logical/temporal constraints), collapsing magnitude-thresholds toward **near-random abstention** on BRIGHT (logical) and TEMPO (temporal) — the **Magnitude Mirage**.

**Fix (zero-cost)**: Large-scale study of six **QPP metrics** across three cognitive tiers (BEIR / BRIGHT / TEMPO). The dominant gain comes from *abandoning magnitude for score-distribution signals*; the distributional-family choice matters 5–10× less. **Score Gap (s₁−s_k)** and **LSMV** (adapted Score Magnitude & Variance) improve abstention AUROC by **up to +0.16** where magnitude has little discriminative power — with no extra inference/retraining/latency, so it drops into deployed RAG unchanged.

### 3.3 Cognition on Graph: Navigating Massive Knowledge Space via Cognitive Cycles and Bidirectional Graph-Text [Main]
- **英文 Title**: Cognition on Graph: Navigating Massive Knowledge Space via Cognitive Cycles and Bidirectional Graph-Text Alignment
- **中文 Title**: 图上的认知：通过认知循环与双向 Graph-Text 对齐导航海量知识空间
- **Authors**: Gengxian Zhou, Jian Xu, Zichen Tang, Shiming Xiang, Haihong E, Cheng-Lin Liu
- **Affiliation**: Institute of Automation, Chinese Academy of Sciences (CASIA) / Beijing Univ. of Posts & Telecom (tentative)
- **Venue**: EMNLP 2026 Main Conference
- **arXiv**: https://arxiv.org/abs/2609.12791

**Problem background**: RAG lets LLMs tackle knowledge-intensive tasks, but navigating *global, heterogeneous knowledge bases* with scattered, sparsely-connected facts breaks both plain vector retrieval and flat graph retrieval.

**Methodology**: "Cognition on Graph" — an agentic graph-RAG loop with two pillars:
1. **Cognitive cycles**: iterate sensing (retrieve from graph neighborhood) → reasoning (LLM deliberation over subgraph) → acting (grow/redirect search frontier), driven by cognitive-cycle routing rather than single-hop lookups;
2. **Bidirectional Graph-Text alignment**: a model that maps text ↔ graph structure in both directions so evidence from either modality grounds the other.

**Significance**: Positions graph-RAG as an *agentic navigation* problem over massive knowledge spaces (cross-domain enterprise graphs), in the same family as the earlier WWW'26 GraphRAG-R1 trend ([[conference-digest 2026-09-11|09-11 digest §9]]).

### 3.4 The Role of Implicit and Explicit Demographic Signals in LLM-based Student Assessment [Findings]
- **英文 Title**: The Role of Implicit and Explicit Demographic Signals in Large Language Model-based Student Assessment
- **中文 Title**: 隐式与显式人口学信号在 LLM 学业评估中的作用
- **Authors**: Donya Rooein, Luca Benedetto, Dirk Hovy
- **Affiliation**: Bocconi University (tentative)
- **Venue**: EMNLP 2026 Findings
- **arXiv**: https://arxiv.org/abs/2609.16993

**Problem background**: LLM-based Automated Essay Scoring, formative feedback, and metalinguistic QA are going live in classrooms; whether (and how) demographics leak into scores is unknown.

**Findings** (6 SOTA LLMs × 2 cue types × 3 tasks): **(a)** Explicit demographic mentions drive systematic behavior — e.g., feedback readability adapts to declared education level. **(b)** *Implicit* signals (conversation history) produce **unpredictable biases** — e.g., responses for lower-education users receive lower sentiment scores in QA. Sensitivity to demographics is real in both modes; implicit bias is the more dangerous and the less controllable.

**Significance**: Evidence base for fairness regulation of AI grading; "explicit-and-controllable vs implicit-and-uncontrollable" framing is portable to other high-stakes LLM-human interfaces.

### 3.5 EMNLP 2026 coverage notes
- Previously featured in sibling digests (deduped here): **RAG-Safety-Bench** (2609.11758, Main — safety impact of RAG; 09-12), **ReGround** (2609.11460, reviewer-comment grounding; 09-13), **When Synthetic Data Hurts** (2609.10750, Industry — skill-retrieval catastrophic forgetting; 09-11/12/13), and **Mo' Models, Mo' Problems** (2609.17306, REALM 2026 workshop — multi-agent model-pool selection; today's arxiv-paper-check).

---

## 4. CIKM 2026 (35th ACM CIKM) — New Accepted Paper

### 4.1 FAE + REAL: Evidence-Grounded Fact-Checking in LLMs via Multi-Round Evidence Ablation
- **英文 Title**: Evaluating and Improving Evidence-Grounded Fact-Checking in LLMs via Multi-Round Evidence Ablation
- **中文 Title**: 经由多轮证据消融评估与改进 LLM 的证据锚定事实核查
- **Authors**: Xingyu Deng, Mingzi Cao, Nikolaos Aletras, Xi Wang, Mark Stevenson
- **Affiliation**: University of Sheffield / University of Glasgow (tentative)
- **Venue**: CIKM 2026 (35th ACM International Conference on Information and Knowledge Management)
- **arXiv**: https://arxiv.org/abs/2609.08943

**Problem background**: LLM fact-checkers score high accuracy — but do they *faithfully use the provided evidence*, or lean on parametric memory? Standard accuracy metrics cannot tell.

**Methodology**:
1. **FAE (Fact-Ablated Evaluation)** — a framework that iteratively *ablates the cited evidence* and checks whether predictions move accordingly. If veracity flips when the counter-claim evidence is removed, the model is genuinely evidence-dependent; if it stays, it is parametric-knowledge-driven.
2. **REAL (Rigorous Evidence Ablation Learning)** — a training objective using *counterfactual evidence supervision* (train the LLM-as-verifier on evidence-perturbed examples so predictions track the available support).

**Results**: Off-the-shelf LLMs **rely more on parametric knowledge than on provided evidence**; strong fact-checking accuracy coexists with weak evidence dependency. Models trained with REAL achieve superior evidence-dependent verification vs standard fine-tuned baselines on **four fact-checking datasets** across different domains.

**Comparison with prior methods**: vs standard SFT verifiers / calibrated-role models, REAL explicitly couples prediction to evidence availability — the "evidence-dependency" axis that accuracy benchmarks miss (same critique as §3.1's fact-grounding gap).

---

## 5. NeurIPS 2026 (Dec 6–12, Sydney + Dec 9–13, Atlanta & Paris satellites)

- **Paper timeline**: abstract submission closed **May 4 2026**; full papers **May 6 2026**; reviews released Jul 22; author discussion Jul 27–Aug 10; **final decisions announced Sep 24 2026 (AoE)** — 8 days from this digest.
- **Workshops**: 477 submissions (454 valid) → **102 accepted**: 48 Sydney / 28 Paris / 26 Atlanta. Workshop CFPs mostly used Aug 29 2026 submission date; mandatory accept/reject notification **Sep 29**.
- **Position-paper track** runs in parallel (decisions same Sep 24 window).
- **Novelty for the digest**: NeurIPS 2026 is the *decision point* venue this month — the Sep 24 notification will be the next big arXiv dump of accepted-work preprints (a key lookout for the next conference-digest editions).

---

## 6. SIGIR 2026 (Melbourne, Jul 20–24) — Award Retrospective

**Stats**: 4526 submissions → 900 accepted (~20% overall).

| Award | Paper | Authors | Key point |
|---|---|---|---|
| **Best Paper** | Why Advanced Encoders Lag on Sparse Retrieval? The Answer and an Approach to Bridging Vocabulary Gaps | Zhichao Geng, Yang Yang | Diagnosis + method for the sparse-retrieval vocabulary-gap failure of advanced dense/bi-encoders; unifies sparse+encoding strengths |
| Best Short Paper | When RAG Disagrees: Detecting Latent Epistemic Conflict via Logit Interactions | Saisab Sadhu, Dwaipayan Roy, Tanmay Basu | Detects "models disagree internally" via logit-interaction signals instead of answer sampling |
| Best Student Paper | Topic-Specific Classifiers are Better Relevance Judges than Prompted LLMs | Lukas Gienapp, Martin Potthast, Andrew Yates, Harrisen Scells, Eugene Yang | Narrow per-topic classifiers beat zero-shot LLM judges on relevance annotation (cost/efficiency) |
| Test of Time Award | Learning to Rank with Selection Bias in Personal Search (SIGIR 2016) | Xuanhui Wang, Michael Bendersky, Donald Metzler, Marc Najork | Position-bias (selection bias) treatment in personal search LTR — a decade of production impact |
| ToT Honorable Mention | Entity Query Feature Expansion Using Knowledge Base Links (SIGIR 2014) | Jeffrey Dalton, Laura Dietz, James Allan | — |
| Industry highlight | **GenRec** (JD.com; SIGIR'26 camera-ready, **2604.14878** — [[papers/recommendation|recommendation papers]]) | Yanyan Zou et al. | Decoder-only GR: Multimodal SIDs + Token Merger (~2× prefilling cut) + Page-wise NTP + GRPO-SR; month-long online **+9.5% clicks, +8.7% transactions** (already covered 06-xx digests — cited for completeness) |

---

## 7. ACL 2026 (San Diego, Jul 2–7) — Award Retrospective

**Stats**: 12,148 submissions → 2,296 Main (18.9%) + 2,163 Findings; 504 orals. 158 papers nominated for awards.

| Award | Paper | Authors | Key point |
|---|---|---|---|
| **Best Paper** | The Imperfective Paradox in Large Language Models | Bolei Ma, Yusuke Miyao (NII/U-Tokyo) | LLMs hallucinate *completion* for goal-oriented events — see [[conference-digest 2026-09-11|09-11 digest §7]] |
| Best Paper | Memory Efficiency and Resource-Rational Encoding in Sentence Processing | Weijie Xu, Brian Dillon, Richard Futrell | Linguistic memory allocation follows resource-rational (information-theoretic) encoding |
| Best Paper | Characterizing the Expressivity of Local Attention in Transformers | Jiaoda Li, Ryan Cotterell | Formal expressivity limits of local attention |
| **Outstanding** | MauBERT: Universal Phonetic Inductive Biases for Few-Shot Acoustic Units Discovery | Tandazo et al. | Acoustic-unit discovery with phonetic inductive bias |
| **Outstanding** | Evolutionary Guided Decoding: Iterative Value Refinement for LLMs | Liu et al. | Population-based value-refinement decoding |
| **Outstanding** | Beyond the Final Actor: Creator and Editor Dual Roles for LLM-Text Detection | Li et al. | Fine-grained AI-text detection with creator/editor decomposition |
| **Outstanding** | Lying with Truths: Open-Channel Multi-Agent Collusion for Belief Manipulation via Generative Montage | Hu et al. | Multi-agent belief manipulation: collusion that stays truthful per-utterance |
| **Outstanding** | Mind the (DH) Gap! A Contrast in Risky Choices Between Reasoning and Conversational LLMs | Luise Ge, Ryan Zhang, Yevgeniy Vorobeychik (WashU) | Reasoning models ≈ risk-neutral rational agents; conversational models show human-like risk sensitivity & framing effects |
| **Outstanding** | CxMP: Constructional Minimal-Pair Benchmark (constructional understanding) | Miyu Oba, Saku Sugawara (NAIST/NII) | Construction grammar benchmark for LMs |
| **Outstanding** | ViLL-E: Video LLM Embeddings for Retrieval | Gupta, Unnikrishnan, …, Mubarak Shah (UCF IAI) | Adaptive "think longer" embeddings; +7% temporal localization, +4% video retrieval vs dual encoders |
| **Outstanding** | From Local to Global: Revisiting Structured Pruning Paradigms for LLMs (GISP) | Wang et al. | Global iterative structured pruning (attention heads + MLP channels), first-order loss-based importance |
| Best Theme | CoSToM: Causal-oriented Steering for Theory-of-Mind Alignment | Li et al. | Causal steering for intrinsic ToM |
| Best Resource | VeriTaS: First Dynamic Benchmark for Multimodal Automated Fact-Checking | Rothermel et al. | Dynamic fact-checking benchmark |
| Best Social | Afri-MCQA: Multimodal Cultural QA for African Languages | Tonja et al. | OCR/multimodal cultural QA for 20+ African languages |

---

## 8. KDD 2026 (Jeju, Aug 9–13) — Recommendation/Ads Wrap-up

**Stats** (Vol.1): 1,215 submissions → 256 accepted (21%). Full conference ~1,400+ papers.

Industrial generative-recommendation & CTR track, all previously digested ([[conference-digest 2026-08-30|08-30 digest]] / [[conference-digest 2026-07-26|07-26 digest]]):

| Paper | Company | Key numbers | Earlier coverage |
|---|---|---|---|
| **DeGRe** — Dense-supervised Generative Reranking (**2605.25749**, ADS Track) | Alibaba/Taobao (Shan Gu) | Lookahead evaluator (cumulative regression) + dense-supervision distillation into greedy online generator; Taobao Flash Shopping online **+2.85% CTR / +2.14% ORDER / +3.75% GMV**; offline HR@1% +29.9/+28.95/+53.19 pts vs SOTA (ML-1M / TaobaoAd / Flash) | 06-30 → 08-05 conference-digests |
| **Atomic Intent Reasoning** (**2606.10357**) | Kuaishou | LLM intents generated offline (atomic intent pairs) + online intent-tree assembly; millisecond serving, SOTA on public benchmarks | 06-10/06-17 digests |
| **TSGR** — Taobao Search Generative Retrieval (**2607.18796**) | Alibaba/Taobao | QP-SID value-aware codebooks + Value-aware Ranking Module (retriever=pre-ranker); **+9.16% HR@1000**, online **+0.43% IPV / +1.12% Transactions / +1.64% GMV**, fully deployed | 07-22/07-31 digests |
| GR4AD (Kuaishou) / HOBA (Kuaishou) / OneRank (Alibaba) / RankUp (Tencent) / UniVA (Tencent) | Kuaishou, Alibaba, Tencent | +4.2% rev / +3.6% cost / unified ranking / +11.93% / +1.5% GMV | 09-11 Full Edition §5 |
| Reasoning Over Semantic IDs Enhances Generative Recommendation | — | New SID-reasoning supervision direction (@KDD'26 program) | new in Paper-Digest KDD'26 listing |

---

## 9. ICML 2026 / ICLR 2026 / NeurIPS 2025 / CVPR 2026 / WWW 2026 — Compact Award Retrospect

Full details in [[conference-digest 2026-09-11|2026-09-11 Full Edition]].

- **ICML 2026** (Seoul, Jul 6–11; 23,918 subs → 6,352 acc, 26.6%): Outstanding Papers — *The Flexibility Trap* (diffusion-LM token-order critique) + *High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions* (δ-error in polylog(1/δ)); Outstanding Position — *A Censor's Toolkit*; HM — *To Grok Grokking in Ridge Regression*; ToT — *A3C* (Mnih et al., DeepMind).
- **ICLR 2026** (Rio, Apr 28–May 2; 19,525 subs → 5,355 acc, 27.4%): Outstanding — *Transformers are Inherently Succinct* + *LLMs Get Lost in Multi-Turn Conversation*; HM — *The Polar Express* (Muon theory); notable — Mamba-3, MoE-vs-dense equal-resource proof, P-GenRM, SPIRAL.
- **NeurIPS 2025** (San Diego+Mexico City, Dec 2025): Best Papers — *Gated Attention for LLMs* (Qwen/Alibaba; attention-sink-free), *1000 Layer Networks for Self-Supervised RL*, *Artificial Hivemind* (open-ended behavioral homogeneity).
- **CVPR 2026** (Denver, Jun 3–7; 16,092 subs → 4,089 acc, 25.4%): Best — *D4RT* (DeepMind dynamic 4D reconstruction); Best Student — *Native and Compact Structured Latents for 3D Generation* (Tsinghua/Microsoft); HMs — *NitroGen* (NVIDIA generalist gaming agents, 40K hrs/1000+ games) and *SAM 3D* (Meta). Multimodal share jumped 4.9%→10.6% YoY.
- **WWW 2026** (Dubai, Apr 13–17; 3,370 subs → 676 acc, 20%): notable — GraphRAG-R1, GenCI (CTR), CRS, PLUM (Spotify); plus **LSIG: Long Semantic IDs for Generative Recommendation** (pp. 7779–7788, DOI 10.1145/3774904.3792834) — demonstrated that *longer* SIDs improve GR item reconstruction/generation fidelity without the usual decode-cost blowup.

---

## 10. General Recent Papers (newly verified, category-organized)

All IDs below grep-verified **0 hits** in `wiki/` before inclusion.

### 10.1 LLM Memory & Knowledge (LLM)
#### Where Should a Document Live: Context, Representations, or Parameters?
- **英文/中文**: Where Should a Document Live: Context, Representations, or Parameters? / 文档应驻留何处：上下文、表征还是参数？
- **Authors**: Nathanaël Carraz Rakotonirina, Momchil Hardalov, Gonzalo Iglesias, Adrià de Gispert · **Affiliation**: Google DeepMind (tentative)
- **arXiv**: https://arxiv.org/abs/2609.17346
- **Abstract/innovation**: Answers the now-central RAG-vs-finetuning-vs-context question as a *controlled comparison* of three ways to inject documents (context window encoding; retrieval-oriented representation memory; parameter fine-tuning). Positioned as a systematic allocation study: which regime wins for out-of-domain follow-up questions, and under what cost/update rate. (high confidence intro, tentative affiliation)

#### LSREP + ICE v2: A Longitudinal State-Replay Protocol for Evaluating Conversational Memory
- **英文/中文**: LSREP: A Longitudinal State-Replay Protocol for Evaluating Conversational Memory, with ICE v2 as an Audited Local-First Architecture / LSREP：会话记忆的纵向状态重放评测协议（含被审计的本地优先架构 ICE v2）
- **Author**: Deepesh Sonar · **Affiliation**: —
- **arXiv**: https://arxiv.org/abs/2609.16730
- **Abstract/innovation**: Endpoint QA cannot reveal how conversational memory *accumulates, ages, or revises*. LSREP = ordered replay + lifecycle schedules + repeated probes + evolving reference answers + mechanism-fidelity checks. Case study ICE v2: on ordinary-density sets ≈ vector-RAG quality while selecting **32% fewer fragments** (but +6.6% prompt tokens); on a dense dataset the unbudgeted baseline **catastrophically fails**. Audited public diagnostic vs LongMemEval: ICE v2 loses decisively to pure vector-RAG (**50.8 vs 72.8** evidence-oracle; **43.0 vs 69.5** full-S), i.e., a *quality–cost tradeoff*, not a win. Key methodological lesson: fidelity auditing + replay + public endpoints expose failure modes aggregate scores hide. (tentative ABs numbers verified from abstract)

### 10.2 Recommendation / Ads & CTR (rec)
#### When Synthetic Data Hurts (EMNLP Industry) / OneLA Scaling Linear-Attention GR — see sibling dedup
- **OneLA** (2609.12399) and **Preference-Drift GR** (2609.12556) were covered 09-14 (arxiv-daily); **ReliGRec** (2609.16560) covered today (arxiv-ai-search). Not re-detailed. 
- **2609.16304** "Evaluating Brand Retrieval and Ranking in LLM Recommendations" (today's arxiv-ai-search) — evaluation-angle LLM-rec work.

### 10.3 IR / Retrieval & RAG (retrieval)
#### Route Me If You Can: QueryRoute — Benchmark for Query Reformulation Selection
- **英文/中文**: Route Me If You Can: A Benchmark for Query Reformulation Selection / QueryRoute：查询改写选择的基准（“路由我做不做得了”）
- **Authors**: Hai Son Le, Negar Arabzadeh, Amin Bigdeli, Radin Hamidi Rad, Sajad Ebrahimi, Charles L. A. Clarke, Ebrahim Bagheri
- **Affiliation**: University of Toronto / University of Waterloo (tentative) · **arXiv**: https://arxiv.org/abs/2609.14885
- **Abstract/innovation**: Freezes expensive artifacts (original queries, variants, ranked lists across retrievers, per-query oracle labels): **3,757 queries, 11 candidate systems, 5 reformulator backbones, 3 retrievers** across TREC DL / BEIR / BRIGHT → **619,905 retrieval outcomes**. Benchmark of supervised classifiers, routers, QPP, LLM-judges: large *oracle headroom* exists, but current selectors capture only part of it; selector rankings are retriever-dependent. Reproducible decision layer for query-reformulation routers.

#### ORDER: Task-Conditioned Routing for Dynamic Evidence Retrieval
- **英文/中文**: ORDER: Optimal Routing for Dynamic Evidence Retrieval / ORDER：面向动态证据检索的任务条件路由
- **Authors**: Aurélien Pellet, Julien Perez, Marie Puren · **Affiliation**: IRIHS / CEA Paris-Saclay (tentative) · **arXiv**: https://arxiv.org/abs/2609.17012
- **Abstract/innovation**: Domain-expert RAG: per-cluster chunking/metadata/reranking configs learned offline over semantic clusters of a corpus's questions; inference routes queries via nearest-centroid; supervised **QRe** router + **UMS** uniform multi-source sampler. Beats fixed-config baselines and strong SOTA RAG on heterogeneous historical archives.

### 10.4 Multimodal & Vision-Language (multimodal)
#### RegRet: Region-Level Retrieval in Large Multimodal Models (ECCV 2026)
- **英文/中文**: RegRet: Enhancing Region-Level Retrieval in Large Multimodal Models / RegRet：增强大多模态模型的区域级检索
- **Authors**: Xun Liang, Honghui Yang, Weihang Pan, Ruisi Zhao, Boyuan Pan, Yao Hu, Wenxiao Wang, Binbin Lin, Deng Cai
- **Affiliation**: Zhejiang University / Alibaba (Yao Hu, Alibaba) (tentative) · **Venue**: ECCV 2026 · **arXiv**: https://arxiv.org/abs/2609.16847
- **Abstract/innovation**: LMMs nail global retrieval but fail *region-level* retrieval (e-commerce product search, region RAG). RegRet = Region-Aware Encoder (region + global-background balance) + multi-stage training (detailed localized captioning → regional contrastive learning). New **REGBMB** benchmark: 225k contrastive pairs across 4 retrieval tasks. >20% average gain on REGMB + public benchmarks in zero-shot→fine-tuned, with parity on global tasks.

### 10.5 Benchmarks & Evaluation (benchmarks)
- **QueryRoute** (§10.3) doubles as the benchmark entry this cycle — plus **Benchmark Radar** (2609.11115, living DB/search for AI benchmarks; covered 09-13) and **Coding Agents Have Converged** (2609.17394, SWE-bench ordering audit; covered today in arxiv-ai-search).

---

## 11. Category Signals Across the Digest

| Category | Signal this cycle | Headline |
|---|---|---|
| **Recommendation** | RecSys'26/CIKM'26 acceptances | WHALE unifies Wukong+HSTU (Meta); MPZCH fixes embedding-collision staleness (Meta); generative reranking now a KDD production standard (DeGRe +3.75% GMV) |
| **Ads & CTR** | Asset-heavy industrial GR plateau | GR-for-ads matured at KDD'26 (TSGR/UniVA/GR4AD); auction-theory & value-alignment remain open edges |
| **LLM & reasoning** | Evidence-faithfulness paired studies | Fact-grounding gap ≈50% of multi-hop failures; LLM fact-checkers over-rely on parametric memory (FAE/REAL) — *two independent 2026 acceptances* reach the same conclusion (flag: convergent evidence) |
| **Agents** | EMNLP'26/RAG agentics | Agentic RAG partial-answer quality (CIKM'26), skill-retrieval synthetic-data forgetting (EMNLP'26 Industry), agentic societies governance (arxiv) |
| **Retrieval** | Abstention & routing | Magnitude Mirage → distribution-based QPP (Score Gap/LSMV); QueryRoute benchmark; ORDER per-queryconfig |
| **Generative models** | ICML'25-26 retrospect | High-Accuracy Sampling (polylog steps), Flexibility Trap, Set Diffusion |
| **Sequential modeling** | RecSys'26 + arXiv | Long-sequence GR + linear-attention decoding (OneLA, 09-14); Wukong-HSTU sequence fusion |
| **Games / world models** | CVPR'26 retrospect | NitroGen (NVIDIA, gaming agents FM); GenieDrive/ARCache trends — see 09-14 game-rl-daily |
| **Code execution** | SWE-bench audit trend | "Coding Agents Have Converged" leaderboard-ordering critique (covered 09-16) |
| **Benchmarks** | Standardization wave | QueryRoute freezes reusable artifacts; REGMB (region retrieval); FAE (evidence ablation) |

> ⚠️ **Convergence flag (2 independent sources)**: §3.1 (fact-grounding gap, EMNLP'26) and §4.1 (FAE, CIKM'26) independently show LLMs under-perform when truth must come from *retrieved evidence rather than parametric knowledge* — different tasks, same diagnosis. Worth a [[claims]]-style claim page if reinforced by a third source.

---

## References

- RecSys 2026 contributions & instructions: https://recsys.acm.org/recsys26/ · https://recsys.acm.org/recsys26/contributions
- SIGIR 2026 awards: https://sigir2026.org/en-AU/pages/program/awards
- ACL 2026 awards: https://2026.aclweb.org/program/best_papers
- EMNLP 2025 awards: https://2025.emnlp.org/program/awards
- NeurIPS 2026 (CFP, workshops, timelines): https://neurips.cc/Conferences/2026/ · https://blog.neurips.cc/category/2026-conference
- ICML 2026 awards blob: https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards
- KDD 2026 proceedings Vol.1/Vol.2: https://dl.acm.org/doi/proceedings/10.1145/3770854
- Prior full edition: [[conference-digest 2026-09-11|wiki/synthesis/2026-09-11/conference-digest.md]]