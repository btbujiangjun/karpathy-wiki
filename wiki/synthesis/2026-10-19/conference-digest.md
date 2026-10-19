---
title: "Conference Digest — Awards Update & Fresh Papers (2026-10-19)"
type: synthesis
created: 2026-10-19
updated: 2026-10-19
sources: [conference-web-searches, arxiv-abs-pages]
tags: [conference-digest, AAAI2026, SIGIR2026, ACL2026, EMNLP2025, WWW2026, CIKM2025, KDD2026, NeurIPS2025, recommendation, semantic-ids, agents, LLM, generative-retrieval, evaluation, benchmarks, daily-digest]
---

# Conference Digest — Awards Update & Fresh Papers (2026-10-19)

> **Date:** 2026-10-19 · **Type:** incremental conference / award edition
> **Window:** award announcements and accepted-paper news confirmed between **2026-10-17 and 2026-10-19**, plus arXiv papers (submitted Jan–Oct 2026) that are **new to the wiki**.
> **Relation to siblings:** the full venue-by-venue editions are [`2026-10-17/conference-digest.md`](../2026-10-17/conference-digest.md) and [`2026-09-11/conference-digest.md`](../2026-09-11/conference-digest.md). This edition only adds: **(a)** award suites the 10-17 run did not cover (AAAI 2026, SIGIR 2026, ACL 2026, EMNLP 2025, WWW 2026, CIKM 2025, KDD 2026 status), **(b)** nine arXiv papers grep-verified 0-hit, **(c)** explicit corrections to both siblings (§4). Games / code-execution lanes for today are owned by the same-day `arxiv-daily` and `arxiv-ai-search` siblings — cross-referenced, not repeated.
> **Method:** official award pages re-fetched this run (`blog.neurips.cc`, `archives.iw3c2.org/www2026`, `2025.emnlp.org/program/awards`, `2026.aclweb.org/program/best_papers/`, `sigir2026.org`, `kdd.org`, AAAI-26 announcements) + per-paper `arxiv.org/abs/{id}` metadata (`citation_title` / `citation_author` metas, 2 s spacing — export API rate-limited `429` all run).
> **Language:** sources English → body English; Chinese titles as `title-zh`.

---

## 1. Award updates since the 2026-10-17 edition

The 10-17 edition carried no award results for AAAI, SIGIR, ACL, EMNLP, WWW, or CIKM and reported no KDD 2026 award winners. Those gaps are filled below.

### 1.1 AAAI 2026 (Singapore, Jan 2026) — Outstanding Papers

| # | Paper / title-zh | Authors (lead) | Scope (title-level unless noted) |
|---|------------------|----------------|----------------------------------|
| 1 | **Model Change for Description Logic Concepts** / 描述逻辑概念的模型变更 | Ana Ozaki, Jandson S Ribeiro | Concept learning under evolving models (description-logic setting). *(single-source; abstract not re-read this run)* |
| 2 | **CaDyT: Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis** / 动力系统因果结构学习与理论评分分析 | Nicholas Tagliapietra, Katharina Ensinger, Christoph Zimmer, Osman Mian | Causal structure learning for dynamical systems with a theoretical score-analysis contribution — [arXiv 2512.14361](https://arxiv.org/abs/2512.14361). |
| 3 | **ReconVLA** / 重构式视觉-语言-动作 | Wenxuan Song et al. | Reconstructive vision-language-action model: reconstructive supervision (attended scene region) as an auxiliary signal for action learning; Zhejiang University lineage (inferred). |
| 4 | **LLM2CLIP: Multi-Temporal Representation Learning** (LLM2CLIP lineage) | Weiquan Huang et al. | LLM-derived **caption-to-caption contrastive** fine-tuning injects LLM knowledge into CLIP's text encoder, unlocking zero-shot cross-modal understanding; Microsoft — [arXiv 2411.04997](https://arxiv.org/abs/2411.04997). |
| 5 | **High-pass matters: sheaflet-based hypergraph neural networks** / 高通滤波与 sheaflet 超图神经网络 | Ming Li, Yujie Fang, …, Pietro Liò | Sheaflet-based hypergraph neural networks with a high-pass perspective on the filter-bank analogy. *(single-source)* |

**Other AAAI-26 awards announced:** AI- for-Safety-Initiative recognition — **PlantTraitNet** and **GRAM**; **AI for Humanity** — Shakir Mohamed (Google DeepMind); **Engelmore Award** — Ashok Goel; **Educator** — Mackworth & Poole; **Classic Paper** — Bordes et al. (KB embedding lineage) and Tellex et al.; **Dissertation Awards** — Akari Asai (University of Washington) and Noah Golowich (MIT). *(Career/classic listings are single-source; titles not all re-verified this run.)*

### 1.2 SIGIR 2026 (Melbourne, Jul 20-24, 2026) — Awards

- **Best Paper: "Why Advanced Encoders Lag on Sparse Retrieval? The Answer and an Approach to Bridging Vocabulary Gaps"** — Zhichao Geng, Yang Yang (**Amazon Web Services Shanghai**). Finding: sparse-only fine-tuned encoders (e.g. ModernBERT lineage) trail strong ensemble baselines because of **vocabulary mismatch**, not architecture; vocabulary tuning recovers the gap and reaches **BEIR nDCG 52.4 (+4.7)** — [arXiv 2607.00004](https://arxiv.org/abs/2607.00004). A "boring-but-fixable infrastructure bug beats a new model" result.
- **Best Student Paper: "Topic-Specific Classifiers are Better Relevance Judges than Prompted LLMs"** — Lukas Gienapp, Martin Potthast, Andrew Yates, Harrisen Scells, Eugene Yang. Small topic-specific classifiers outperform prompted LLMs as relevance raters.
- **Best Short Paper: "When RAG Disagrees: Detecting Latent Epistemic Conflict via Logit Interactions"** — Saisab Sadhu, Dwaipayan Roy, Tanmay Basu. RAG disagreement as a signal — detecting latent epistemic conflict from logit interactions instead of answer text.
- **Test of Time: "Learning to Rank with Selection Bias in Personal Search"** (SIGIR 2016) — Xuanhui Wang, Michael Bendersky, Donald Metzler, Marc Najork (Google).
- **Test of Time Honorable Mention: "Entity Query Feature Expansion Using Knowledge Base Links"** (SIGIR 2014) — Jeff Dalton, Laura Dietz, James Allan.

### 1.3 ACL 2026 (official best-papers page) — Awards

**Best Papers (3):**
1. **The Imperfective Paradox in Large Language Models** / LLM 的未完成体悖论 — Bolei Ma, Yusuke Miyao. Linguistic-theory probe of LLM grammatical knowledge.
2. **Memory Efficiency and Resource-Rational Encoding in Sentence Processing** — Weijie Xu, Brian Dillon, Richard Futrell. Sentence processing through the lens of memory efficiency / resource rationality.
3. **Characterizing the Expressivity of Local Attention in Transformers** — Jiaoda Li, Ryan Cotterell (**ETH Zurich**). Formal expressivity characterization of local-attention Transformers.

**Best Theme Paper:** **CoSToM** — Mengfan Li, Xuanhua Shi, Yang Deng.
**Best Resource Paper:** **Mapping the Circumplex of Affect** — Yamauchi, Aizawa.
**Best Social Impact Paper:** **ViLL-E**, **CxMP**, **CIG** (three awards).
**Best Demo Paper:** **olmOCR** — Jake Poznanski, Kyle Lo, Luca Soldaini (**Ai2**); open-source PDF → text pipeline behind Olmo 3-scale data work.

### 1.4 EMNLP 2025 (Suzhou, Nov 2025) — official awards page (re-fetched this run)

> ⚠️ Correction input: the 10-17 edition's §7.1 "**Awards:** 7 Outstanding Papers" table contains **R2I-Bench** as an "Outstanding Paper Award" entry and does **not** mention the Best Paper at all. The official page (`2025.emnlp.org/program/awards`) says otherwise — see §4.

- **Best Paper: "Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index"** — Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, Hannaneh Hajishirzi (**UW + Ai2**). Parallelized FM-index: **18× indexing speedup, 3.2× less memory**, index = 44% of corpus size; **83 TB of Internet text indexed in 99 days on one 128-core node** (19 h on 137 nodes); benchmark-contamination audit finds core LM benchmarks **up to 74.2% contaminated** (GSM8K on CC-2025-21) + public contamination bulletin and API — [arXiv 2506.12229](https://arxiv.org/abs/2506.12229), [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1268/).
- **Outstanding Papers (7, official):** ① LingGym (Yang, Ma, Shi, Zhu — Waterloo/UBC) ② Mind the Value-Action Gap (Shen, Clark, Mitra — UW) ③ DiscoSG (Lin et al. — RMIT/Monash) ④ Generative or Discriminative? Revisiting Text Classification (Kasa et al.) ⑤ Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps (Tutek et al. — UKP/Technion) ⑥ MiCRo personalized preference learning (Shen et al.) ⑦ **Causal Interventions Reveal Shared Structure Across English Filler-Gap Constructions** — Sasha Boguraev, Christopher Potts, Kyle Mahowald. *(R2I-Bench is not on this list.)*
- **Best Special Theme:** InterIDEAS (Yang, Xu, Huang, Jurgensen, Hu, Wang).
- **Best Resource:** Autoformalization in the Wild (Zhang, Valentino, Freitas).
- **Social Impact:** AccessEval — disability bias benchmark (Panda, Agarwal, Patel).
- **People's Choice:** Randomly Removing 50% of Dimensions in Text Embeddings (Takeshita et al.).

### 1.5 WWW 2026 (The Web Conference — Dubai, UAE, **Jun 29 – Jul 3, 2026**) — Awards

Official archive (`archives.iw3c2.org/www2026/`, re-fetched this run) — all three confirmed:

- **Best Paper: "From Retrieval to Generation: Unifying External and Parametric Knowledge for Medical Question Answering"** — Lei Li, Xiao Zhou, Yingying Zhang, Xian Wu. Retrieval + parametric knowledge unification for medical QA.
- **Best Short Paper: "DualGR: Generative Retrieval with Long and Short-Term Interests Modeling"** — Zhongchao Yi, Kai Feng, Xiaojian Ma, Yalong Wang, Yongqi Liu, Han Li, Zhengyang Zhou, Yang Wang — [arXiv 2511.12518](https://arxiv.org/abs/2511.12518). Generative retrieval jointly modeling long- and short-term interests; A/B on a production video platform (**+0.527% video views, +0.432% watch time**).
- **Test of Time: "LINE: Large-scale information network embedding"** — Jian Tang, Meng Qu, Mingzhe Wang, Ming Zhang, Jun Yan, Qiaozhu Mei.

### 1.6 CIKM 2025 (Seoul, Nov 2025) — Awards *(restated from the 2026-09-11 edition; not re-verified this run — single-source)*

- **Best Full Paper:** "Reconsidering the Performance of GAE in Link Prediction" (negative/re-evaluation result).
- **Best Student Paper:** "A Cost-Effective Framework to Evaluate LLM-Generated Relevance Judgements".
- **Best Applied Research Paper:** **Climber** (NetEase).
- **Best Resource Paper:** **SID Practitioner's Handbook** (GRID lineage).

### 1.7 KDD 2026 (Jeju Island, Aug 9-13, 2026) — award status

- **Best-paper awards: not published as of 2026-10-19.** `kdd.org`'s best-paper index lists winners only **through KDD 2025**; SIGKDD's announcement feed shows no KDD 2026 paper awards. Either unannounced or unpublished — **treat third-party "KDD 2026 best paper" claims as unverified** (see ⚠️ in §4).
- **SIGKDD career awards (announced Aug 2026):** **Innovation Award** — Wei Wang (UCLA); **Service Award** — Ankur Teredesai.
- Three of this run's fresh papers are KDD-2026-accepted by their own arXiv comments fields: Nubank support agents (§2.3.1), STATIC (§2.2.3), MLT-Dedup (§2.3.2).

### 1.8 NeurIPS 2025 — official award list (re-fetched this run)

Official blog (`blog.neurips.cc`, Nov 26 2025): **seven honored papers — four Best Papers + three runners-up**, in alphabetical order:

| Tier | Paper | Lead authors |
|------|-------|--------------|
| Best | **Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)** (D&B) | Liwei Jiang et al. (UW/Duet AI lineage; Yejin Choi senior) |
| Best | **Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free** | Zihan Qiu et al. (Qwen; adopted in Qwen3-Next) — wiki page [[papers/llm-training/gated-attention|gated-attention]] |
| Best | **1000 Layer Networks for Self-Supervised RL** | Kevin Wang et al. |
| Best | **Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training** | Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mézard |
| Runner-up | **Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?** | Yang Yue et al. (Tsinghua Gao Huang group) |
| Runner-up | **Optimal Mistake Bounds for Transductive Online Learning** | Zachary Chase, Steve Hanneke, Shay Moran, Jonathan Shafer |
| Runner-up | **Superposition Yields Robust Neural Scaling** | Yizhou Liu, Ziming Liu, Jeff Gore |

Corrections to the siblings this implies are in §4 (both prior editions mis-stated this list).

---

## 2. Fresh arXiv papers — new to the wiki (9)

Every ID below was `grep`-verified against `wiki/**/*.md` at **0 hits** before writing; titles and author lists were re-fetched from each paper's own `abs` page this run.

### 2.1 Agents & agent systems (3)

#### 2.1.1 Building LLM Agent Systems the Deep Learning Way: From Modular Design to Architecture Search
- **Title (zh):** 用深度学习的方式构建 LLM Agent 系统：从模块化设计到架构搜索
- **Authors:** Tao Feng, Pengrui Han, Zhongjie Dai, Jiaxuan You
- **Affiliation:** not printed on abs page; senior author Jiaxuan You — Purdue (inferred)
- **Venue:** arXiv preprint, submitted 4 Oct 2026 (cs.CL)
- **Abstract & key innovations:** argues LLM-agent stacks should be engineered like deep-learning model zoos: agent components (retrieval, memory, prompting) map to DL-style modules, feedback-based prompt optimization plays the role of backpropagation, and **architecture search over agent topologies** plays the role of NAS. A shared vocabulary for designing, comparing, and searching agent systems instead of hand-assembling frameworks.
- **Comparison with prior methods:** vs hand-engineered agent frameworks assembled by intuition — reports **+5% from prompt optimization** and **+11% from agent architecture search over random search** on agent workloads.
- **Links:** https://arxiv.org/abs/2610.04961

#### 2.1.2 Agentic Cognitive Depth: Operational Criteria for Evaluating LLM Agents
- **Title (zh):** Agentic 认知深度：评估 LLM Agent 的可操作性准则
- **Authors:** Nijesh Upreti, Chris Sypherd, Vaishak Belle
- **Affiliation:** University of Edinburgh (inferred — Vaishak Belle)
- **Venue:** The 5th International Conference on Human and Artificial Rationalities (IHCAR 2026); arXiv submitted 3 Oct 2026
- **Abstract & key innovations:** replaces single success rates with a **trajectory-level profile over five operational criteria — Comprehension (C), Temporal reasoning (T), Memory (M), Adaptability (A), Metacognition (Mc)** — plus perturbation procedures that attribute failures to specific criteria. Extends GAIA / SWE-bench / WebArena-style evaluation with per-criterion diagnostics rather than one scalar.
- **Comparison with prior methods:** aggregate-pass-rate benchmarks conflate failure modes; the profile separates "can't plan" from "forgot context" from "didn't notice it failed".
- **Links:** https://arxiv.org/abs/2610.04168

#### 2.1.3 Agent Behavior as Code: Efficient and Robust LLM Agents with Programmatic Specifications (ABCAgent)
- **Title (zh):** Agent 行为即代码：以程序化规约实现高效稳健的 LLM Agent
- **Authors:** Peng Qi, Chunliang Lyu, Gang Li, Fabian Chan, Cheng Chang, Ignacio Cases, Will Lu
- **Affiliation:** not stated on abs page (industry lab; evaluated on GAIA and τ²-bench)
- **Venue:** arXiv preprint, submitted 4 Oct 2026
- **Abstract & key innovations:** specifies agent behavior as an **executable program** (Python plus neural functions) that a foundation-model agent *edits* instead of emitting opaque trajectories — deterministic execution, inspectable state, staged variable binding (no premature commitment), and FM calls amortized at edit time rather than per step.
- **Comparison with prior methods:** vs model-only end-to-end neural agents — **GSM-Symbolic 98.3% vs 97.3% (p = 0.001)** and **τ²-bench telecom Pass⁴ 71.9% vs 47.4%**, while matching the neural agent on GAIA; robustness gains come from the program scaffold, not a bigger model.
- **Links:** https://arxiv.org/abs/2610.04824

### 2.2 Semantic IDs & generative recommendation (3)

> One coherent thread across these three: **semantic IDs are representations and serving structures — not generation targets.**

#### 2.2.1 From Token Generation to Item Ranking: Direct Generative Recommendation with Semantic IDs (DiGR)
- **Title (zh):** 从 token 生成到 item 排序：用 Semantic ID 做直接生成式推荐
- **Authors:** Yuanbo Zhao, Ruochen Liu, Senzhang Wang, Jun Yin, Yuxin Dong, Huan Gong, Hao Chen, Shirui Pan, Chengqi Zhang
- **Affiliation:** not printed; senior authors Senzhang Wang (Southeast University), Shirui Pan, Chengqi Zhang — lineage inferred
- **Venue:** arXiv preprint (v2, 16 Aug 2026; cs.IR)
- **Abstract & key innovations:** theoretical **ranking-sufficiency dichotomy** — if the SID interface is *ranking-insufficient* (multiple items collide on generated tokens) no decoder can recover the true ranking; if *ranking-sufficient*, item-level scoring collapses into decoding. DiGR therefore uses SIDs **as item representations with a unified item-level scoring head** instead of autoregressive generation targets.
- **Comparison with prior methods:** against TIGER-style token-decoding generative recommenders and ID-based baselines — outperforms both across multiple datasets with LLM backbones of different scales; gives an information-theoretic account of *when* generation can't equal ranking.
- **Links:** https://arxiv.org/abs/2602.07847

#### 2.2.2 Understanding Semantic IDs: From Item Representation to Item Selection in Generative Recommendation
- **Title (zh):** 理解 Semantic ID：生成式推荐中从 item 表示到 item 选择
- **Authors:** Junting Wang, Xinrui He, Yunzhe Li, Hari Sundaram
- **Affiliation:** University of Illinois Urbana-Champaign (inferred — Hari Sundaram)
- **Venue:** arXiv preprint, submitted 27 Jul 2026
- **Abstract & key innovations:** decomposes the SID's three conflated roles (**identifier / semantic neighborhood / generation target**) and audits **8 SID constructions across 3 Amazon domains**. Findings: SID neighborhoods recover only **32.2%** of the encoder's top-10 neighbors; alternate item descriptions retrieve the right item first **99.57%** of the yet change **38.4%** of exact SIDs (stability problem); after the final semantic token, TIGER retains only **29.9%** of previously plausible targets (conditional collapse).
- **Comparison with prior methods:** construction papers (TIGER, FORGE-style) propose encodings; this is a **diagnostic** showing what each encoding actually preserves — directly relevant to DiGR's ranking-sufficiency framing (§2.2.1).
- **Links:** https://arxiv.org/abs/2607.24995

#### 2.2.3 Vectorizing the Trie: Efficient Constrained Decoding for LLM-based Generative Retrieval on Accelerators (STATIC)
- **Title (zh):** 向量化 Trie：加速器上 LLM 生成式检索的高效约束解码
- **Authors:** Zhengyang Su, Isay Katsman, Yueqi Wang, Ruining He, Lukasz Heldt, Raghunandan Keshavan, Shao-Chuan Wang, Xinyang Yi, Mingyan Gao, Onkar Dalal, Lichan Hong, Ed Chi, Ningren Han (13 authors, per abs page)
- **Affiliation:** Google / DeepMind YouTube-recommendation lineage (inferred from author block)
- **Venue:** arXiv comments field: **"KDD 2026 camera-ready"**; v3, 7 Oct 2026
- **Abstract & key innovations:** flattens the constrained-decoding prefix trie into a **static CSR sparse matrix**, so each decoding step is one vectorized sparse matmul on TPU/GPU instead of per-step trie traversal — exact trie constraints preserved, **0.033 ms/step overhead**.
- **Comparison with prior methods:** vs per-token trie-walk constrained decoders whose latency grows with candidate structure; **deployed on a large-scale video recommendation platform serving billions of users** with significant product-metric impact.
- **Links:** https://arxiv.org/abs/2602.22647

### 2.3 KDD 2026 industry deployments (2)

#### 2.3.1 Building Customer Support AI Agents at 100M-User Scale
- **Title (zh):** 在 1 亿+ 用户规模构建客服 AI Agent
- **Authors:** Aman Gupta et al. (multi-author Nubank team)
- **Affiliation:** **Nubank (stated in abstract)**
- **Venue:** **KDD '26** (stated in arXiv comments field)
- **Abstract & key innovations:** an **eval-driven development loop** for production support agents: context engineering + human-in-the-loop prompt iteration + **LLM-judge evaluation with inter-rater agreement checks** + **GEPA prompt optimization** + ideation-to-production validation, feeding **five production deployments** (exemplified by card-delivery flows).
- **Comparison with prior methods:** vs siloed train/eval/deploy pipelines — offline judge metrics are shown to track online outcomes. A/B: **+37 pp AI transactional NPS and +29 pp self-service rate** in card delivery; AI satisfaction within a few points of expert human agents.
- **Links:** https://arxiv.org/abs/2606.08867

#### 2.3.2 MLT-Dedup: Efficient Large-Scale Online Video Deduplication via Multi-Level Representations and Spatial-Temporal Matching
- **Title (zh):** MLT-Dedup：多层级表示与时空匹配的大规模在线视频去重
- **Authors:** David Yuchen Wang, Haoying Li, Hailun Xu, Wei Chee Yew, Zirui Zhu, Sanjay Saha, Hao Hei, Kanchan Sarkar, Kun Xu
- **Affiliation:** not stated on abs page (industry team)
- **Venue:** arXiv comments field: **"Accepted by KDD-2026 ADS track"**; submitted 10 Jun 2026
- **Abstract & key innovations:** **multi-level video encoder** — sparse clip-level representations for candidate retrieval plus fine frame-level representations for matching — and **DiF-SiM**, a differential feature-similarity module that locates duplicated *temporal segments* rather than whole-video identity.
- **Comparison with prior methods:** vs single-level embedding dedup pipelines under a fixed index budget — the cascade keeps recall while cutting the false-positive cost of near-duplicate detection in online feeds.
- **Links:** https://arxiv.org/abs/2606.12215

### 2.4 Agent memory (1)

#### 2.4.1 Heavy-Tailed Memory Traces in Long-Horizon Language Agents
- **Title (zh):** 长程语言 Agent 中的重尾记忆痕迹
- **Authors:** Xinyuan Song, Zekun Cai
- **Affiliation:** not stated on abs page
- **Venue:** arXiv preprint, submitted 1 Oct 2026
- **Abstract & key innovations:** audits long-horizon agent behavior and finds a **core–tail concentration** (truncated power-law) in semantic-LLM policies — a small set of recurring states carries most of the mass; proposes **CTWM**, a rank-based memory controller with an exponent τ that allocates retention to the tail. Reported effects: **−5.9% prompt tokens, −13.6% bottom-half tail prediction error** (Synthetic Graph World), and **−24.48% token consumption** on LongMens-style long-horizon workloads.
- **Comparison with prior methods:** vs graph/text memory append-everything baselines — the tail, not the head, is where memory policy pays off; connects to the wiki's agent-memory thread ([[papers/agents/mem1-agent|Mem1]], JointCore `2610.23266` in today's `arxiv-ai-search`).
- **Links:** https://arxiv.org/abs/2610.00010

---

## 3. Cross-report observations

1. **Awards lens favors "fix the boring thing" and "measure the thing"** — SIGIR's Best Paper closes a vocabulary-gap bug; EMNLP's Best Paper is Internet-scale exact search + contamination auditing; ACL's Best Papers are linguistic analysis and formal expressivity; WWW's Best Paper unifies retrieval with generation for a vertical (medical QA). Capability-scaling papers took no top award in these four suites.
2. **Semantic IDs have a mature critique cycle.** DiGR (theory: when generation ≠ ranking), Understanding Semantic IDs (diagnostics: what SIDs preserve), and STATIC (serving: how constrained decoding actually runs in production) form a pipeline from theory → audit → deployment — a natural continuation of the wiki's generative-recommendation thread ([[papers/recommendation/hstu-generative-recommendation|HSTU]], [[papers/recommendation/thinkrec|ThinkRec]]).
3. **Agents are being pushed off prompts and onto structure**: programs as behavior specs (ABCAgent), DL-style architecture search (§2.1.1), and multi-criterion cognitive evaluation (§2.1.2) — echoing [[agentic-engineering]]; the Nubank deployment (§2.3.1) shows the eval-first version of the same shift in production.
4. **Constrained decoding is now a serving problem, not a research curiosity** — STATIC's KDD 2026 camera-ready with a 0.033 ms/step number at billions-of-users scale is the kind of receipt the wiki's rec-serving thread has been collecting.
5. **Games/code-execution lanes** for today's window are owned by same-day siblings: `2026-10-19/arxiv-daily.md`, `2026-10-19/arxiv-ai-search.md` (games IDs `2610.22882`, `2610.20200`, `2610.19422`, `2610.17895` cross-referenced there), and the 10-18 `game-rl-daily`.

---

## 4. Flags & corrections

> ⚠️ **CONTRADICTION (KDD 2026 best paper):** third-party event recap pages (e.g. Relve's "KDD 2026" recap) credit **Ye/Zheng/Zhang (UVA) group-robustness** as a KDD *2026* best paper; it is the **KDD 2025** Best Paper (confirmed by its IJCAI-2026 extended-abstract footnote: "Full version appears in KDD 2025, recipient of the Best Paper Award in Research"). `kdd.org` lists best papers only through 2025 — **no KDD 2026 paper awards are published as of this run.**

> ⚠️ **CORRECTION (EMNLP 2025):** the 10-17 edition's §7.1 lists **R2I-Bench** among the 7 Outstanding Papers. The official awards page does **not** include it; official Outstanding #7 is **"Causal Interventions Reveal Shared Structure Across English Filler-Gap Constructions" (Boguraev, Potts, Mahowald)**. The 10-17 edition also never mentions the **Best Paper (Infini-gram mini)**. Rows 1–6 of that table match the official list.

> ⚠️ **CORRECTION (NeurIPS 2025):** official list = **4 Best Papers** (Artificial Hivemind, Gated Attention, 1000 Layer Networks, **Why Diffusion Models Don't Memorize**) + **3 runners-up** (RLVR-negative "Does Reinforcement Learning Really Incentivize…", Optimal Mistake Bounds, Superposition). Sibling errors: **09-11** places *Why Diffusion Models Don't Memorize* in its runners-up table (it is a Best Paper) and omits the RLVR-negative runner-up entirely; **10-17** omits both *Why Diffusion…* (Best) and *Optimal Mistake Bounds* (runner-up). This section supersedes both.

> ⚠️ **CORRECTION (Infinity-Chat scale):** the 10-17 edition describes the Artificial Hivemind dataset as "**2M+ user queries**". The official abstract says **26K** diverse open-ended queries with **31,250 human annotations** (25 per example) across **70+ models**. The 2M+ figure is unsupported.

> ⚠️ **CORRECTION (WWW 2026 dates):** the 09-11 edition's §9 header says "Dubai, UAE — **Apr 13-17, 2026**". The official IW3C2 archive says **June 29 – July 3, 2026** (re-fetched this run).

- **Single-source / not re-verified:** AAAI-26 career/classic/dissertation award listings (§1.1, aside from the five Outstanding Papers); CIKM 2025 award suite (§1.6, restated from 09-11); affiliation inferences marked *(inferred)* throughout §2.
- **Not covered here by design:** KDD 2026 paper awards (none published); games, code-execution prediction, and video-generation lanes (owned by same-day siblings — see §3.5).

---

## 5. Sources

**Re-fetched this run:**
- NeurIPS 2025 Best Paper Awards — https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/
- The Web Conference 2026 (awards + dates) — https://archives.iw3c2.org/www2026/
- EMNLP 2025 Awards — https://2025.emnlp.org/program/awards ; ACL Anthology https://aclanthology.org/2025.emnlp-main.1268/
- ACL 2026 Best Papers — https://2026.aclweb.org/program/best_papers/
- SIGIR 2026 Awards — https://sigir2026.org/ (awards announcement)
- KDD / SIGKDD best-paper index and 2026 career-award announcements — https://www.kdd.org/
- AAAI-26 outstanding-paper and AI-hub award announcements
- Per-paper arXiv abs pages: `2610.04961`, `2610.04168`, `2610.04824`, `2602.07847`, `2607.24995`, `2602.22647`, `2606.08867`, `2606.12215`, `2610.00010`

**Sibling digests used as dedup/correction baselines:**
- [`synthesis/2026-10-17/conference-digest.md`](../2026-10-17/conference-digest.md), [`synthesis/2026-09-11/conference-digest.md`](../2026-09-11/conference-digest.md), same-day [`arxiv-ai-search.md`](arxiv-ai-search.md) / [`arxiv-daily.md`](arxiv-daily.md), [`2026-10-18/game-rl-daily.md`](../2026-10-18/game-rl-daily.md)
