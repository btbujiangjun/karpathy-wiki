---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-21 Daily Edition"
type: synthesis
created: 2026-11-21
updated: 2026-11-21
sources:
  - https://export.arxiv.org/api/query?search_query=all:ICML+AND+submittedDate%3A%5B202601010000+TO+202612312359%5D&max_results=40&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:AAAI+AND+submittedDate%3A%5B202601010000+TO+202612312359%5D&max_results=40&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:NeurIPS+AND+submittedDate%3A%5B202501010000+TO+202512312359%5D&max_results=40&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:ICLR+AND+submittedDate%3A%5B202601010000+TO+202612312359%5D&max_results=40&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:KDD+AND+submittedDate%3A%5B202601010000+TO+202612312359%5D&max_results=40&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:CVPR+AND+submittedDate%3A%5B202601010000+TO+202612312359%5D&max_results=40&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:ACL+AND+submittedDate%3A%5B202601010000+TO+202612312359%5D&max_results=40&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:EMNLP+AND+submittedDate%3A%5B202501010000+TO+202512312359%5D&max_results=40&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:SIGIR+AND+submittedDate%3A%5B202601010000+TO+202612312359%5D&max_results=40&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:WWW+AND+submittedDate%3A%5B202601010000+TO+202612312359%5D&max_results=40&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:CIKM+AND+submittedDate%3A%5B202501010000+TO+202512312359%5D&max_results=40&sortBy=submittedDate&sortOrder=descending
  - https://export.arxiv.org/api/query?search_query=all:RecSys+AND+submittedDate%3A%5B202501010000+TO+202512312359%5D&max_results=40&sortBy=submittedDate&sortOrder=descending
  - Topic queries (max 40 each, sorted by submittedDate desc): all:LLM, all:"AI agent", all:"agent system", all:"generative model", all:"diffusion model", all:"sequential modeling", all:sequential, all:benchmark, all:"code execution", all:"recommendation system", all:CTR, all:advertising, all:"video game", all:"game AI"
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, ICLR2026, KDD2026, CVPR2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, advertising, CTR, LLM, agents, generative-models, sequential-modeling, games, code-execution, benchmarks, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-21 Daily Edition
# 会议论文日报：2025-2026 顶级 ML/AI 会议（2026-11-21 每日版）

> Venues covered: **ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025** — plus general recent papers in AI, LLMs, recommendation systems, advertising/CTR, games, code execution prediction, agent systems, generative models, sequential modeling, and benchmarks. Focus organizations: Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, Baidu, Netflix, NVIDIA, Anthropic, Apple, Amazon and top labs.

## Method, data window & limitations (方法、数据窗口与限制)

- **Query date:** 2026-11-21. **Web search:** unavailable in this environment (`Web search cancelled`). **arXiv access:** arXiv Export API over HTTPS — 12 venue queries (`all:<Venue> AND submittedDate:[YYYY01010000 TO YYYY12312359]`, venue membership requires the venue name in the arXiv comments field, sorted by submittedDate desc, max 40 results each) + ~20 general topic queries (max 40 each, sorted by submittedDate desc) → ~1,500 candidates scanned, **30 papers selected** (3 venue + 27 topic), every ID grep-verified absent from the ~9.4k arXiv IDs referenced in `wiki/**`.
- **Venue papers:** zero new venue-tagged papers — venue coverage through the 2026-11-20 digest is current for all 12 venues.
- **Affiliations:** recovered from arXiv PDF page-1 author/affiliation blocks (pypdf). **Evidence:** all metrics/results/claims are **author-reported** from abstracts; no full-text review beyond PDF page 1; Chinese titles are translation aids; technical terms stay in English.

---

## 1. Venue digest — new venue-tagged papers (会议论文日报 — 新增 venue 标签论文)

### ICML 2026 — no new venue-tagged papers

Coverage through the 2026-11-20 digest (PMLR 306, Seoul): 2611.22557, 2611.20445, 2611.20405, 2611.18370, 2611.16361, 2611.10891, 2611.10684, 2611.07873. Papers like 2610.34625v1 / 2610.33644v1 / 2610.29289v1 mention ICML 2026 only in their abstracts as related work (no venue tag) and are not ICML 2026 papers.

### AAAI 2026 — no new venue-tagged papers

Coverage through the 2026-11-20 digest: 2611.23609, 2611.15538, 2611.10023, 2611.05979 (AAAI-2027 IAAI-tagged papers excluded per venue-exclusion predicates).

### NeurIPS 2025

#### 2512.22442v1 — HiFi-RAG: Hierarchical Content Filtering and Two-Pass Generation for Open-Domain RAG
**HiFi-RAG：分层内容过滤与两阶段生成 RAG**

- **Authors / 作者:** Cattalyya Nuengsigkapian
- **Affiliation / 机构:** Google (PDF page 1)
- **Venue / 会议:** NeurIPS 2025 (MMU-RAGent Competition — winning closed-source system in the Text-to-Text static evaluation)
- **Problem:** Open-domain RAG suffers from irrelevant retrieved documents and generated answers that do not align with user intent; standard embedding-based retrieval is a bottleneck.
- **Methodology:** Multi-stage pipeline (HiFi-RAG): query formulation via Gemini 2.5 Flash (4-6× cheaper than Pro), hierarchical content filtering, citation attribution, then final answer by Gemini 2.5 Pro.
- **Key innovations:** Split compute between cheap Flash for filtering and expensive Pro for generation; hierarchical filtering reduces irrelevant passages before citation attribution.
- **Experimental results / 结果：** Validation set: ROUGE-L 0.274 (+19.6%), DeBERTaScore 0.677 (+6.2%) vs baseline. On Test2025 (questions requiring post-cutoff knowledge): +57.4% ROUGE-L and +14.9% DeBERTaScore vs the parametric baseline.
- **Comparison with prior methods / 对比：** Prior methods: plain embedding-based retrieval (HiFi-RAG's baseline). RAG pipelines without hierarchical filtering or with only Flash.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.22442v1) · [PDF](https://arxiv.org/pdf/2512.22442v1)

### ICLR 2026

#### 2611.26286v1 — Twice-Told Critiques: Claim-Level Homogenization of Peer Review in the LLM Era
**二重评审：LLM 时代同行评审的分子面同质化**

- **Authors / 作者:** Ilya Guseev
- **Affiliation / 机构:** Keenable, Amsterdam (PDF page 1)
- **Venue / 会议:** ICLR 2026/2027 (peer review of ICLR papers; no explicit ICLR venue tag on arXiv comments — evidence from abstract)
- **Problem:** LLM-generated text is increasingly used in peer review, and we need to measure whether critiques in reviews of the same paper are still diverse or collapsing to shared statements.
- **Methodology:** Measure critique overlap in conference/journal reviews. Apply MELD, a detector of LLM-generated text, to all reviews (inter-reviewer κ ≥ 0.75, validated on five human raters). Two reviews that MELD flags overlap more than two unflagged reviews.
- **Key innovations:** Corpus-level analysis of critique overlap in ICLR 2026–2027; evidence of LLM-assisted review degradation (measured overlap rose 12.0% → 21.3% at ICLR between 2026 and 2027); "a third ICLR review of a paper added 5.46 new problems to the other two in 2027, against 6.12 in 2026" (lower marginal diversity of later reviews).
- **Experimental results / 结果：** At ICLR in 2024-2025, MELD-flagged overlap: 3.0 points vs 2.7–2.8 unflagged; in 2026-2027: 4.5 points vs 2.7; across five journal sources: 5.4 points.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26286v1) · [PDF](https://arxiv.org/pdf/2611.26286v1)

### KDD 2026 — none
Coverage through the 2026-11-20 digest (2611.19330, 2611.12725, 2611.12219, 2611.00885, 2610.41368).

### CVPR 2026 — none
Coverage through the 2026-11-20 digest (2611.23887, 2611.22506, 2611.20625, 2611.09191, 2611.03438).

### ACL 2026 — none
Coverage through the 2026-11-20 digest (2611.23218, 2611.21232, 2611.20191, 2611.19220, 2611.19030).

### EMNLP 2025

#### 2511.14684v2 — SMRC: Aligning Large Language Models with Student Reasoning for Mathematical Error Correction
**SMRC：以学生推理对齐大模型的数学推理纠错**

- **Authors / 作者:** Biaojie Zeng, Min Zhang, Juan Zhou, Fengrui Liu, Ruiyang Huang, Yu Song, Xin Lin (Equal contribution; project leader Min Zhang, corresponding Xin Lin)
- **Affiliation / 机构:** East China Normal University (1); Southeast University (2) (PDF page 1)
- **Venue / 会议:** EMNLP 2025
- **Problem:** LLMs often make reasoning errors when solving math problems; existing self-correction methods ("mainly focus on self-correction within the model") fall short of teacher-style correction needed in education — systematically guiding and revising a student's process.
- **Methodology:** SMRC = Student Mathematical Reasoning Correction. Student reasoning is formulated as a multi-step sequential decision problem; Monte Carlo Tree Search (MCTS) explores optimal correction paths; BFS-guided by LLMs + final-answer evaluation generates annotation-level rewards, distributed across intermediate steps via back-propagation for fine-grained process supervision. Constructs MSEB benchmark (158 instances: problem statements, student solutions, correct reasoning steps). Dual evaluation: solution accuracy + correct-step retention.
- **Key innovations:** Teacher-style correction aligned with student reasoning; process-level rewards via reward back-propagation; benchmark for educational applicability (MSEB).
- **Experimental results / 结果：** SMRC significantly outperforms existing methods on ProcessBench and MR-GSM8K and on MSEB (processBench and MR-GSM8K) in effectiveness and (truncated — see abstract).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2511.14684v2) · [PDF](https://arxiv.org/pdf/2511.14684v2)

### SIGIR 2026 — none
Coverage through the 2026-11-20 digest (2611.14236, 2611.04619, 2611.03727, 2610.37231, 2610.33078).

### WWW 2026 — none
Coverage through the 2026-11-20 digest (2611.03090, 2610.36010, 2609.23405, 2609.10260, 2608.04883).

### CIKM 2025 — none
Coverage through the 2026-11-20 digest (2601.11954, 2603.21024, 2512.09260, 2511.20729, 2511.18816).

### RecSys 2025 — none
Coverage through the 2026-11-20 digest (2611.13972, 2511.14865, 2510.22865, 2510.13359, 2510.11402).

---

## 2. Topic digest — general recent papers (通用主题论文日报)

### 2.1 AI & LLMs — 4 papers

#### 2611.26480v1 — Held While Waiting: What LLM Agent Sessions Reserve on Serverless and Agent Runtimes
**等待期间挂起：LLM 智能体会话在 Serverless 与智能体运行时中的保留**

- **Authors / 作者:** Mekhala Hithyshini Sreenivasa (Amazon Web Services)
- **Affiliation / 机构:** Amazon Web Services (PDF page 1)
- **Problem:** On Amazon Bedrock AgentCore, LLM agents wait a median of 2.7 s per model reply (compute ≈ 5–40 ms) but each conversation holds a reserved environment (VM with own memory) until the conversation is closed — 1,000 conversations reserve 1,000 environments while only 2–15 processor cores are needed.
- **Methodology:** Survey of agent runtimes; three root causes analyzed: (a) environment stays reserved after conversation ends (customer-service benchmark: conversation 33 s, environment held 15 min more), (b) one environment serves only one conversation (64 conversations sharing one environment need 59× fewer environments; 99 of every 100 replies delayed by ≤ 40 ms), (c) hard-to-measure timing with stubbed models.
- **Key innovations:** Env-sharing design (64→1 conversations per environment); client-side closing for idempotent sharing; open problem: keep environments separate without reserving one per waiting conversation.
- **Experimental results / 结果：** 99/100 replies within 40 ms via simulation; median 2.7 s model-reply wait vs ~5–40 ms compute; 1,000 conversations → 1,000 VMs (2–15 cores).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26480v1) · [PDF](https://arxiv.org/pdf/2611.26480v1)

#### 2611.26432v1 — MaskPE: One Mask, Two Roles: Weight Placement and MAC Gating in Systolic Arrays
**MaskPE：符号面的双重角色——Systolic Arrays 中的权重位置与 MAC 门控**

- **Authors / 作者:** Shu-Lin Shih, Chandra Sekhar Mummidi, Aamir Gujral Elhaissouni, Sandip Kundu (PDF page 1: University of Massachusetts Amherst)
- **Affiliation / 机构:** University of Massachusetts Amherst (PDF page 1)
- **Problem:** Unstructured pruning reduces weight storage but not execution cost in conventional weight-stationary systolic arrays (packed nonzero weights must be restored to fixed PE positions; zero-weight positions must preserve data forwarding).
- **Methodology:** MaskPE — mask-directed systolic architecture: positional masks steer nonzero weights during preload; clock-gate arithmetic registers in zero-weight PEs during execution, reducing dynamic power while preserving systolic dataflow.
- **Key innovations:** Compression with unchanged execution: at 50% sparsity, 34.9% compressed weight storage (incl. metadata overhead).
- **Experimental results / 结果：** RTL validation: exact execution, no additional steady-state tile stalls; gate-level simulation: 12.5–14.4% lower execution energy across seven LLM projection samples.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26432v1) · [PDF](https://arxiv.org/pdf/2611.26432v1)

#### 2611.26450v1 — A CPU Inside an LLM: Zero-Gradient Compilation of Exact Circuits into Pretrained Weights
**LLM 内部的 CPU：把精确电路零微分编译进预训练权重**

- **Authors / 作者:** Tanmay Sah
- **Affiliation / 机构:** not stated on PDF page 1
- **Problem:** Pretrained LMs are unreliable on exact multi-digit arithmetic without gradient fine-tuning or external tool interpreters.
- **Methodology:** Closed-form zero-gradient circuit-grafting primitives that compile deterministic computation directly into pretrained LM weights — no training examples, no runtime hooks; Mellin-GLU quadrature over bias-free SwiGLU/GeGLU layers; cross-token scale cancellation via signed Chebyshev Indefinite-RoPE self-sink attention; axis-aligned width extension with norm compensation; automated 5-stage compiler synthesizes 4–8 digit signed {+,-,×} circuits in constant depth; 100% 3-literal Boolean and 5-bit Majority/Parity audits.
- **Key innovations:** In-weight arithmetic compilation; per-layer normalization drift bounded with IEEE 754 error bounds; weight memory 7.89/10.65 GiB (4.60/8.14 GiB under INT8/INT4 + FP32 sidecar).
- **Experimental results / 结果：** On 6-digit arithmetic (N=1,200, BF16): IBM Granite 4.2 3B — 99.17% ALU-prefix accuracy (100% with FP32 sidecar, N=1,728); Alibaba Qwen 3.5 4B — 100.00% (98% mid-sentence resumption).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26450v1) · [PDF](https://arxiv.org/pdf/2611.26450v1)

#### 2611.26312v1 — Static Analysis Guidance for Secure LLM Code Generation
**面向 LLM 代码生成的安全静态分析引导**

- **Authors / 作者:** Daniele Lunghi, Alberick Euraste Djiré, Zacharie Chenail-Larcher, Melissa Tessa, Quentin Stiévenart, Jacques Klein, Naouel Moha, Tegawendé F. Bissyandé (PDF page 1; University of Luxembourg, ÉTS Canada, Université catholique de Louvain)
- **Affiliation / 机构:** University of Luxembourg (PDF page 1)
- **Problem:** Analyzer reports are a candidate feedback signal for secure LLM code generation, but existing approaches use iterative repair loops (expensive, hard to isolate the report's effect).
- **Methodology:** Two strategies giving the finding to the model during generation: generation rollback + finding inserted as (a) code comment (Comment) or (b) user message (Steering); compared with two iterative approaches + a control without the analyzer, across three models × three Python benchmarks (oracle = benchmark security).
- **Key innovations:** Guidance cheaper than iterative: 0.9–1.9× output tokens vs up to 24.1×.
- **Experimental results / 结果：** With DeepSeek-V4.1-flash on RiskyPy: Steering raises functional+secure share from 52.5% to 64.4% (best iterative: 66.2%), using < 1/5 of tokens. Analyzers flag ≤ 5.6% of functional-but-insecure programs (SecEvalPlus) — limited guidance.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26312v1) · [PDF](https://arxiv.org/pdf/2611.26312v1)

### 2.2 Agents — 4 papers

#### 2611.26503v1 — JARVIS: An Agent That Designs, Builds, and Tests Circuit Boards on Its Own
**JARVIS：自主设计、构建并测试电路板的智能体**

- **Authors / 作者:** Shibo Zhou, Tianqi Hong, Zheng Yan, He Yang (PDF page 1: School of ECE, University of Georgia)
- **Affiliation / 机构:** University of Georgia (PDF page 1)
- **Problem:** Developing new power electronics still relies on human-led design, fabrication, testing, and iteration.
- **Methodology:** JARVIS = embodied agent closing the design–build–test–learn loop: machine-specific capabilities/constraints, 3D-scanner workspace, executable digital twin (robot-motion rehearsal, PCB printing, circuit behavior simulation), one text instruction → coordinate robot arm + PCB printer (silver ink, solder paste) + pick-and-place; verify via cameras/sensors; test via OPAL-RT real-time simulator + oscilloscope; revise design in KiCad, rehearse, iterate.
- **Key innovations:** First agent in power electronics closing physical design-build-test-learn loop for circuit boards (per paper).
- **Experimental results / 结果：** 60 Hz notch filter for grid-connected converter sensing: first-run experiment completed in 2 h 39 min without human intervention, 50.6 dB attenuation at 60 Hz; digital-twin rehearsal found five issues before fabrication (including a false-positive rejection criterion).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26503v1) · [PDF](https://arxiv.org/pdf/2611.26503v1)

#### 2611.26296v1 — SKILL.PNG: Learning Agent Skills in Pixel Space
**Skill.PNG：以像素空间学习智能体技能**

- **Authors / 作者:** Maximilian Seeth, Chengzhi Martin Hu, Marie Kempkes, Paul Röttger, Leo Schwinn (PDF page 1: TU Munich; Mbps/Hugging Face/Volkswagen Group Innovation)
- **Affiliation / 机构:** Technical University of Munich + Helmholtz AI + Volkswagen Group Innovation (Marie Kempkes) (PDF page 1)
- **Problem:** Textual skills are discrete; gradient-based approaches (finetuning) are model-specific, preventing skill transfer across agents.
- **Methodology:** Skill.png — image skills optimized with gradient descent through the vision encoder of a frozen VLM (pixels), compatible with any VLM, jointly optimizable for an ensemble; hybrid skills (text + image) further improve performance.
- **Key innovations:** First agent skill that is optimized with gradient descent while retaining transfer benefits of text skills; image skill uses 64–256 image tokens vs 900–2000 text tokens.
- **Experimental results / 结果：** Better than state-of-the-art textual skills in 9 of 16 settings (4 VLMs × 4 benchmarks); ensemble-optimized image skill transfers across VLMs in the ensemble.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26296v1) · [PDF](https://arxiv.org/pdf/2611.26296v1)

#### 2611.25705v1 — STARK: Moving towards Personalized Agents That Truly Learn and Remember
**STARK：迈向真正学习与记忆的个性化智能体**

- **Authors / 作者:** Aryan Jain, Abhishek Jha, Anish Nediyanchath, Promod Yenigalla (Amazon)
- **Affiliation / 机构:** Amazon / RBS Tech Sciences (PDF page 1)
- **Problem:** Long-term memory for personalized agentic systems captures events but leaves the reasoning of why they happened to later derivation; knowledge silos within users.
- **Methodology:** STARK dual-graph memory: Episodic Graph (interactions linked temporally, causally, semantically) + Insight Graph (LLM-extracted behavioral signals, scored by support count, connected by the events that led to them); at inference, behavioral knowledge retrieved from insight nodes grounded by event-as-edges; relational embedding space enables cross-user transfer.
- **Key innovations:** Event-as-edge structure enabling insight-graph nodes and cross-user transfer under shared contextual circumstances (cold-start user inference).
- **Experimental results / 结果：** +1.48 judge score on LongMemEval information extraction, +0.93 on LoCoMo open-domain questions over SOTA; LongLaMP cross-user: +0.7 judge score, +3.0 ROUGE-L at 5% graph sparsity.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25705v1) · [PDF](https://arxiv.org/pdf/2611.25705v1)

#### 2611.25599v1 — Tether: Verified Stateful Policy Engine for System-Level Monitoring of Agents
**Tether：面向系统级监控的可验证有状态策略引擎**

- **Authors / 作者:** Meghana Aparna Sistla, Alaia Solko-Breslin, Somesh Jha, Aditya Kanade, Krishnamurthy Dj Dvijotham (PDF page 1: Google DeepMind, Google, University of Pennsylvania, University of Wisconsin-Madison)
- **Affiliation / 机构:** Google DeepMind, Google, University of Pennsylvania, University of Wisconsin-Madison (PDF page 1)
- **Problem:** Autonomous agents execute arbitrary shell commands/programs — unauthorized network requests or persistent malicious changes to filesystem/processes/privileges; existing defenses rely on LLM monitors (no guarantees) or stateless policy layers (miss multi-step flows and side effects).
- **Methodology:** Tether — runtime enforcement of stateful security policies over observed side-effects: each action runs in an ephemeral isolated sandbox; abstract action semantics inferred from observed system calls; stateful policies over inferred semantics in an embedded Lean 4 DSL (expressible IFC, access control, network security).
- **Key innovations:** Formal verification of global security invariants (e.g., no network access after reading a sensitive file); single rule enforces fine-grained IFC across multi-step execution flows of arbitrary length.
- **Experimental results / 结果：** On realistic coding-agent benchmarks (benign + adversarial): blocks 100% of in-scope attacks with one shared policy; benign false-positive rate reduced to below a few percent.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.25599v1) · [PDF](https://arxiv.org/pdf/2611.25599v1)

### 2.3 Games — 3 papers

#### 2610.03953v1 — Characterizing Open-Source Video Games from a Software Engineering Perspective
**表征开源电子游戏：软件工程视角**

- **Authors / 作者:** Henrique Mandelli Canella, Yohan Duarte, Cristiano Politowski, Vinicius Durelli, Andre Takeshi Endo (PDF page 1: Universidade Federal de São Carlos / Ontario Tech)
- **Affiliation / 机构:** Universidade Federal de São Carlos, São Paulo, Brazil (PDF page 1)
- **Problem:** Open-source games are a corpus of empirical software engineering research, but many projects are dormant/abandoned and their development practices are not well documented.
- **Methodology:** Extract metadata from 491 games on itch.io (published as open-source on GitHub): genres, popularity, repository activity, implementation characteristics (game engine), testing practices.
- **Key innovations:** Quantified the state of open-source games: genres, engine usage, test-practice documentation gaps.
- **Experimental results / 结果：** 491 open-source games: predominantly Puzzle, Action, Platformer; Godot/Unity dominant engines; repositories largely dormant; ~majority of projects lack testing-related documentation.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2610.03953v1) · [PDF](https://arxiv.org/pdf/2610.03953v1)

#### 2610.36267v1 — Preserving rare-item recall under a storage budget: quantization, distillation, and the limits of teacher fidelity
**存储预算下的稀有物品召回保持：量化、蒸馏与教师保真的极限**

- **Authors / 作者:** Han Chen, Yingrui Li (PDF page 1: Han Chen unaffiliated, Yingrui Li at UT Austin)
- **Affiliation / 机构:** UT Austin (Yingrui Li) + unaffiliated (Han Chen) (PDF page 1)
- **Problem:** Recommenders must fit user/item embeddings in a fixed storage budget (e.g., memorization tradeoff); choices: small full-precision model, distilled student, or higher-rank low-precision model; which preserves rare-item recall (tail items) best?
- **Methodology:** 7 dataset-backbone cells: MF on Gowalla, Last.fm, Amazon Video Games, Steam, Goodbooks-10k, MovieLens-20M; LightGCN on Amazon Video Games. 7 candidates fit in 168 bytes/row: 40-d BPR, two 40-d UnKD students, rank-40/80/155/300 4-bit factorizations of a 300-d teacher.
- **Key innovations:** Judge by total tail recall (not teacher fidelity): rank-300 4-bit retained 95–103% of teacher tail recall@20 and 93–97% NDCG@20 in every cell; rank-40 worst; 4-bit had 1.2–12.7× rank-40 tail recall; bytes spent on rank > precision.
- **Experimental results / 结果：** Rank-300 4-bit factorization: 13% of teacher storage, 95–103% tail recall@20, 93–97% NDCG@20 in all cells; teacher-hit retention 23/147 candidate pairs differed (tail-recall leader identified wrong in 3 of 7 cells).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2610.36267v1) · [PDF](https://arxiv.org/pdf/2610.36267v1)

#### 2609.31810v2 — VIDEO-TO-MUSIC GENERATION FOR GAMEPLAY VIDEOS
**游戏玩法视频生成音乐**

- **Authors / 作者:** Felipe Marra, Lucas N. Ferreira (PDF page 1: Universidade Federal de Vicosa / UFMG)
- **Affiliation / 机构:** Universidade Federal de Vicosa, Vicosa, Minas Gerais, Brazil; Universidade Federal de Minas Gerais, Belo Horizonte (PDF page 1)
- **Problem:** Video-to-music models exist for film/music videos; the game domain adds challenges: rendered graphics frames, mostly-synthetic audio, soundtracks looping across whole levels.
- **Methodology:** New dataset: 217.6 h of Super Nintendo (SNES) gameplay video + 485 h of clean soundtracks (no SFX/voice; matched via audio fingerprinting). Encoder-decoder transformer: video features → MusicGen decoder; encoders: T5 text (frozen/finetuned), independent frames ViT, spatiotemporal ViViT.
- **Key innovations:** Frozen encoders match/beat finetuned on every metric; frozen ViViT best overall; 18% fewer parameters than baselines.
- **Experimental results / 结果：** Frozen ViViT: best on objective metrics; surpassed GVMGen in a listening study (N=96); comparable to OSSL.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2609.31810v2) · [PDF](https://arxiv.org/pdf/2609.31810v2)

### 2.4 Generative models — 2 papers

#### 2611.26586v1 — ProtoDiffusion: Token-per-Layer Generative Modeling of Multi-Layer Images
**ProtoDiffusion：多层图像的逐层 Token 生成建模**

- **Authors / 作者:** Adrià Ciurana Lanau, Harleen Hanspal, Lusine Abrahamyan, Emilio Tylson Baixauli, Yu Cao, Danai Triantafyllidou, Stefano Zorzi, Gustavo Zanoni Felipe, Peter Griger, Stefan Sietzen, Petru-Daniel Tudosiu (PDF page 1: 1Canva, 2Queen Mary University of London, 3Universidade Estadual de Maringá)
- **Affiliation / 机构:** Canva (PDF page 1)
- **Problem:** Graphic designs are ordered compositions of RGBA layers; existing layered models store full-canvas/region-sized spatial latents per layer, so size grows with cumulative extent.
- **Methodology:** ProtoDiffusion — latent-diffusion framework built on ProtoVAE: a multi-layer variational autoencoder encoding a design into one shared spatial prototype + one candidate vector per layer; a shared decoder reconstructs each RGBA layer from its candidate. Jointly denoises prototype and fixed candidate slots conditioned on image/text; optional layout guidance via boxes; model chooses the number of layers and (without boxes) their layout.
- **Key innovations:** Representation = HW+N tokens (vs NHW for full-grid-per-layer); empty slots allowed (layout learned without boxes).
- **Experimental results / 结果：** ProtoVAE: 40.43 dB PSNR on layer crops; LayerD image-to-design RGB L1: 0.040 with boxes / 0.057 without (box-guided alpha soft IoU 0.850 vs strongest fine-tuned baseline 0.871); text-to-design FID: 66.41 (vs 86.84 for FLUX.2 [klein]); 0.860 text-accuracy score; 19.1× faster than generation-then-decomposition cascade; merged images FID.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26586v1) · [PDF](https://arxiv.org/pdf/2611.26586v1)

#### 2611.26407v1 — Flow Matching from Non-Gaussian Sources: A Theory of Efficient Sampling
**非高斯源上的流匹配：高效采样理论**

- **Authors / 作者:** Yuchen Zhou, Lili Zheng, Yuxin Chen, Gen Li (PDF page 1: affiliations not stated on page 1)
- **Affiliation / 机构:** not stated on PDF page 1
- **Problem:** Flow matching offers flexible source distributions (heavy-tailed, multimodal) for generative modeling, but finite-step sampling guarantees for non-Gaussian sources are limited.
- **Methodology:** Nonasymptotic convergence theory for Euler discretization with linear interpolation: source on R^d with everywhere-positive Lipschitz density; total variance bounded; target satisfying mild second-moment condition → total variation error ≤ ε in Õ(Ld·TotVar/ε) iterations.
- **Key innovations:** Theory covers Student's t (df > 2) and finite Gaussian mixtures with shared covariance as sources; targets need neither smooth density nor bounded support.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26407v1) · [PDF](https://arxiv.org/pdf/2611.26407v1)

### 2.5 Sequential modeling — 2 papers

#### 2611.26537v1 — On the design of sequential quantum repeaters with error detection
**带错误检测的顺序量子中继器设计**

- **Authors / 作者:** Javier Rey-Domínguez, Koji Azuma, Mohsen Razavi (PDF page 1: University of Leeds; NTT Inc.)
- **Affiliation / 机构:** University of Leeds (UK) / NTT Inc. (Japan) (PDF page 1)
- **Problem:** Trust-free long-distance quantum communications need scalable quantum repeater schemes; sequential entanglement generation with error detection is promising (hop-by-hop, compatible with classical infrastructure).
- **Methodology:** Investigate design choices over a repeater chain using QKD as benchmark; quantum error-detecting codes (repetition/quantum parity codes) under near-term hardware assumptions; examine architectures for generating initial entanglement; quantify impact of hardware improvements.
- **Key innovations:** Two-qubit repetition codes may suffice in many practical scenarios.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26537v1) · [PDF](https://arxiv.org/pdf/2611.26537v1)

#### 2611.26232v1 — Time Series Structure Learning with Local Causal Parent Discovery
**局部因果父探索下的时间序列结构学习**

- **Authors / 作者:** Jacqueline Maasch, Shu Wan, Hank Zhu, Huan Liu, Zhiguang Wang (PDF page 1: Cornell Tech, Abel AI, Arizona State)
- **Affiliation / 机构:** Cornell Tech + Abel AI + Arizona State University (PDF page 1)
- **Problem:** Time series learning faces autocorrelation, distribution shift, and the curse of dimensionality — hardening causal discovery algorithms (already high sample/complexity).
- **Methodology:** Iterative Temporal Parent Discovery (ITPD): sound, complete constraint-based procedure for causal structure learning on multivariate time series with causal nonstationarity; local-to-global (discover parent set of each variable), exploiting temporal structural priors, graph partitioning, local Markov condition → swaps high-order CI tests for lower-order; validated empirically.
- **Key innovations:** Least number of CI tests vs baselines; smallest average conditioning sets.
- **Experimental results / 结果：** Benchmarks: ITPD on Pareto frontier of F1 vs wall-clock; on 2,000-node graphs: 2.3×, 9.1×, 40.9× faster than iterative IAMB, DF-PC, PCMCI; oracle setting: fewest tests, smallest conditioning sets.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26232v1) · [PDF](https://arxiv.org/pdf/2611.26232v1)

### 2.6 Recommendation systems — 3 papers

#### 2611.24426v1 — DyNA-Mixer: Decoupling Time and Topology for Scalable Dynamic Node Affinity Prediction
**DyNA-Mixer：解耦时间与拓扑的可扩展动态节点亲和预测**

- **Authors / 作者:** Yuanxing Zheng, Liping Wang, Xuemin Lin (PDF page 1: East China Normal University, Shanghai Jiao Tong University)
- **Affiliation / 机构:** East China Normal University (PDF page 1)
- **Problem:** Continuous-time dynamic graphs preserve ordering/timing/strength of interactions lost in snapshots (evolving recommender systems, trade networks, transaction platforms); dynamic node affinity (DNAP) needs intensity + full-candidate ranking (worse than dynamic link prediction).
- **Methodology:** DyNA-Mixer decouples temporal forecasting from collaborative structure: (a) multi-scale temporal predictor for pair-specific affinity evolution; (b) Virtual Collaborative Graph (infers query-time relationships, aggregates trends); (c) gated residual fusion; (d) sparsity-aware eval restricting forecasting to pairs with recent non-zero affinities.
- **Key innovations:** New SOTA on 4 TGB DNAP datasets; on tgbn-token: +17.8% relative test improvement over the strongest baseline.
- **Experimental results / 结果：** New SOTA NDCG@10 on every dataset (tgbn-token +17.8% vs strongest baseline).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.24426v1) · [PDF](https://arxiv.org/pdf/2611.24426v1)

#### 2611.23910v1 — MLE Agents: Autonomous ML Engineering in Large-scale Recommendation Systems
**MLE 智能体：大规模推荐系统的自主机器学习工程**

- **Authors / 作者:** Matthew Li, Albert Liang, Dilip Raj (PDF page 1: Meta Platforms)
- **Affiliation / 机构:** Meta Platforms (PDF page 1)
- **Problem:** Improving large-scale ranking/recommendation models is slow: engineer hypothesis → implement → train → evaluate (hours per experiment, offline-online gap, saturation after early wins).
- **Methodology:** Human-on-the-loop ML engineer (MLE) agents that propose, implement, train, evaluate model changes on large-scale search rankers; engineers control objective, direction, final review; three addressed obstacles: parallel training runs, objective calibrated to online impact, careful context engineering; natural campaign with optimization for product success.
- **Key innovations:** Automation of a large part of the model iteration loop on production-scale systems.
- **Experimental results / 结果：** Campaign: 1,097 completed candidate experiments, 325 accepted (29.6% acceptance, vs 15.6% under a different objective/constraint); best model +0.23% search volume in a large-scale A/B test; several tried-elsewhere architectural changes emerged.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.23910v1) · [PDF](https://arxiv.org/pdf/2611.23910v1)

#### 2611.22607v1 — DLS: Dual-Logic Graph Neural Networks with Chaos-Fuzzy Residuals for Robust Link Prediction
**DLS：用于鲁棒链接预测的双逻辑图神经网络（混沌模糊残差）**

- **Authors / 作者:** Mohammad Mehdi Keikha, Abolfazl Nadri (PDF page 1: University of Sistan and Baluchestan; University of Tehran)
- **Affiliation / 机构:** University of Sistan and Baluchestan, Zahedan, Iran (PDF page 1)
- **Problem:** MPNNs suffer over-smoothing (recursive aggregation suppresses high-frequency signals → indistinguishable node representations in deep layers); worse in heterophilous graphs (structural proximity ≠ feature similarity).
- **Methodology:** DLS (Dual-Logic SAGE): (a) Chaotic Injection Module — Logistic Map logistic map for feature-manifold diversity (exploiting sensitivity to initial conditions); (b) Fuzzy-Logic Gating — soft-thresholding to filter noise, retain high-confidence signals.
- **Key innovations:** Controlled instability mechanism for feature discrimination; fuzzy gating for aleatoric robustness.
- **Experimental results / 结果：** Better feature discrimination + robustness vs SOTA on heterophilous settings; competitive efficiency on homophilous.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.22607v1) · [PDF](https://arxiv.org/pdf/2611.22607v1)

### 2.7 CTR — 1 paper

#### 2611.22595v1 — Lost in the Funnel: Selection-Induced Miscalibration in Ranking and Decision Systems
**迷失在漏斗中：排序与决策系统的选择诱导性错校准**

- **Authors / 作者:** Aditya Somani, Rahul Ragesh, Vikas Joshi, Amit Singh (PDF page 1: Microsoft Ads)
- **Affiliation / 机构:** Microsoft Ads, Bangalore (PDF page 1)
- **Problem:** Scores calibrated at the model boundary are used as calibrated probabilities throughout the funnel (filtering, reranking, business rules, auctions), but calibration is validated only where the score is produced — its breakdown where the score is used is overlooked.
- **Methodology:** Boundary-wise diagnostic framework of residual identities; industry case study applying the diagnosis where calibration deteriorates at decision time, attributing degradation to selection rather than model error; Funnel-Aware Recalibration (FAR): post-hoc, selection-policy-aware recalibration at the boundary where scores drive decisions.
- **Key innovations:** 60–80% reduction of decision-time ECE in a live two-region production A/B test; improved auction efficiency.
- **Experimental results / 结果：** Live 2-region production A/B test: FAR cuts expected calibration error at decision time by 60–80% and improves auction efficiency; adapted public datasets corroborate the mechanism.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.22595v1) · [PDF](https://arxiv.org/pdf/2611.22595v1)

### 2.8 Advertising — 2 papers

#### 2611.21586v1 — Beyond Job Titles: Interpreting Early-Career Job Advertisements with Sparse Autoencoders and Semantic Clustering
**超越职位头衔：用稀疏自编码器与语义聚类解读早期职业招聘广告**

- **Authors / 作者:** Yisong (Ethan) Cao, Leah Kim, Brian Wright, Ali Rivera (PDF page 1: Active Learning Lab, School of Data Science, University of Virginia)
- **Affiliation / 机构:** University of Virginia Active Learning Lab (PDF page 1)
- **Problem:** Job titles/descriptions alone give limited insight into how technical roles differ in a changing job market; how roles differ in applications (e.g., Data Scientist vs Data Analyst).
- **Methodology:** 36,081 early-career LinkedIn job postings (U.S., Dec 2025–Oct 2026); PERC (Preprocessing/Embedding/Dimensionality Reduction/Clustering); GPT-6 Luna classifies passages into Team context, Role task, Qualifications; combinations of sections embedded/clustered; MMD ranks differences between embedding distributions; sparse autoencoder extracts features from Llama-3.1-8B-Instruct layer 19; GPT-6 Luna → role feature hypotheses; GPT-6.1 Terra validates hypotheses on held-out postings from unseen companies.
- **Key innovations:** Interpretable role-difference semantics via semantic clustering of SAE features on transformer representations.
- **Experimental results / 结果：** Findings: Data Scientist ads emphasize machine learning model development; Data Analyst ads emphasize reporting business performance; Machine Learning Engineer ads emphasize applying developed models in real-world settings; observed application differences between Data Analyst and Business Analyst ads across months.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.21586v1) · [PDF](https://arxiv.org/pdf/2611.21586v1)

#### 2611.23216v1 — Higher-Scoring Coding Models Did Not Get More Work Done
**分数更高的编码模型并未完成更多实际工作**

- **Authors / 作者:** Yining Hua
- **Affiliation / 机构:** not stated
- **Problem:** Coding models advertise benchmark score improvements, but does a higher score on benchmarks mean more real work done?
- **Methodology:** Natural experiment: June 12, 2026, U.S. export control banned Claude Fable 5 access for 19 days — users switched to Opus 4.8; tracked GitHub pull requests of 297 Fable 5 users before/during/after (5 model upgrades), and 8,908 control developers on Opus 4.8; difference-in-differences with developer + date fixed effects.
- **Key innovations:** Benchmark performance ≠ productivity; asks whether benchmark score advantages translate to user-level outcomes.
- **Experimental results / 结果：** 7-day merge rate: +1.4 percentage points [-1.4; +4.3] for Fable 5 vs control — not statistically significant; five upgrades before/after: weighted mean -0.9pp [-1.9; +0.2]; no increase in PRs merged per week (+2.4% [-4.9%; +10.2%]).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.23216v1) · [PDF](https://arxiv.org/pdf/2611.23216v1)

### 2.9 Benchmarks — 3 papers

#### 2611.26609v1 — Variants of Beam Search for DiskANN
**DiskANN 的 Beam Search 变体研究**

- **Authors / 作者:** Viraj Agrawal, Kirankumar Shiragur (PDF page 1: Microsoft Research India)
- **Affiliation / 机构:** Microsoft Research India (PDF page 1)
- **Problem:** Graph-based ANN search structures (DiskANN, HNSW, NSG) — building better beam search variants for α-reachable graphs and beyond.
- **Methodology:** Theory: ABS with relaxation γ on α-reachable graphs → approximation α+1/(α(γ+1)-1); tighter bound on sorted α-reachable graphs under ℓ2 (max(α/(α(γ+1)-1), (α²+1)/(α²(γ+1)-1))). Engineering: beam predictor (features from fine-grained ABS analysis; constrained objective minimizing mean distance computations subject to target recall).
- **Key innovations:** Unified/generalized ABS bounds; beam predictor lowering query latency at matched recall on 100M-point benchmarks.
- **Experimental results / 结果：** Up to 29.6% mean query latency reduction at matched recall on DiskANN-constructed 100M-point graphs; vs ABS faster in 11/15 settings (≤ 6.5%, ≤ 1.4% slower elsewhere); at 95% recall: 0.8–4.2% (100 neighbors) → 4.6–5.6% (500 neighbors) vs ABS.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26609v1) · [PDF](https://arxiv.org/pdf/2611.26609v1)

#### 2611.26598v1 — Active Feature Acquisition by Distilling an Oracle Teacher
**以 Oracle 教师蒸馏获得主动特征获取**

- **Authors / 作者:** Yang Meng, Zixin Ding, Robert L. Grossman, Yuxin Chen (PDF page 1: University of Chicago)
- **Affiliation / 机构:** University of Chicago (PDF page 1)
- **Problem:** AFA: under budget, decide per instance which features to acquire; prior methods optimize a self-constructed utility target; construct the teacher explicitly instead.
- **Methodology:** Oracle — at training time, labels + unobserved features available → closed-form teacher ranking every candidate by effect on downstream predictor's error; OracleImitator distills the ranking into a deployable policy via soft-target imitation; across multimodal medical diagnosis and AFABench benchmark.
- **Key innovations:** Explicit algorithmic teacher (ranking by marginal error) instead of implicit optimization target.
- **Experimental results / 结果：** OracleImitator matches/outperforms existing AFA methods across the budget range: recovers 90% of the attainable accuracy gain at under a quarter of the acquisition cost.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26598v1) · [PDF](https://arxiv.org/pdf/2611.26598v1)

#### 2611.26551v1 — GraphEP: A Calibrated Data System and Benchmark for Learning Cardiac Electrophysiology
**GraphEP：心脏电生理学习的可校准数据系统与基准**

- **Authors / 作者:** Matteo Baldan, Chiara D'Ercoli, James Rowbottom, Pietro Liò, Stefania Fresca (PDF page 1: University of Padova, Sapienza, Cambridge, UW)
- **Affiliation / 机构:** University of Padova, Sapienza University, University of Cambridge, University of Washington (PDF page 1)
- **Problem:** Simulated cardiac EP outputs (spatiotemporal on anatomy-dependent volumetric meshes) are hard to consume for scientific ML (anisotropic fields, multi-scale events, anisotropic tissue/material features, activation targets).
- **Methodology:** GraphEP data system: converts cardiac meshes/protocols to compact graph-native trajectories of Vm(t) (732 left-ventricular simulations, 20 anatomies, healthy + scarred substrates of varying severity × multiple pacing); benchmark four inductive biases: local message passing, neural operators, multi-scale hierarchical graph transformers, physiology-informed (HGT-Lag — separates activation timing from AP morphology; GAP2ODE — stateful autoregressive excitation/recovery with frame-wise stimulation).
- **Key innovations:** Physiology-informed HGT-Lag and GAP2ODE lead complementary metrics.
- **Experimental results / 结果：** HGT-Lag & GAP2ODE lead on complementary metrics; wider spatial communication (physiological structure) > local message passing.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26551v1) · [PDF](https://arxiv.org/pdf/2611.26551v1)

### 2.10 Code execution prediction — 3 papers

#### 2611.26558v1 — u3lib: An AI-Ready Computational Framework for U(3) Symmetry Algebra, Wigner Coupling, and Racah Recoupling Coefficients
**u3lib：面向 AI 的 U(3) 对称代数计算框架**

- **Authors / 作者:** Daniel Langr, Phong Dang, Tomas Dytrych, Michela Negro (PDF page 1: Czech Technical University in Prague, Czech Republic; Louisiana State University, USA)
- **Affiliation / 机构:** Czech Technical University in Prague + Louisiana State University (PDF page 1)
- **Problem:** U(3)/SU(3) representation-theory calculations for nuclear structure (Wigner/Racah coefficients, irreps, Casimirs, Gelfand–Tsetlin, SU(3)⊃SO(3)) are compute-heavy for AI assistants.
- **Methodology:** C++ library (U(3)/SU(3) calc, Wigner coupling/Racah recoupling via the 2024 Dang et al. procedure); Python bindings; AI "skills" so an AI assistant with code-execution access can call routines via natural language.
- **Key innovations:** u3lib's domain skills enable AI assistants to use the library directly.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.26558v1) · [PDF](https://arxiv.org/pdf/2611.26558v1)

#### 2611.23810v1 — Continual Tool-Space Extension Learning for Multimodal Agents
**多模态智能体的持续工具空间扩展学习**

- **Authors / 作者:** Jinbae Seo, Jungin Park, Hyunsung Jang, Namkoo Ha, Jiyoung Lee, Kwanghoon Sohn (PDF page 1: Yonsei University, DGIST, LIG Defense & Aerospace, Ewha Womans University, KIST)
- **Affiliation / 机构:** Yonsei University (PDF page 1)
- **Problem:** Multimodal agents rely on generic tools (crop, search, code execution); adding specialist vision models to the tool space is not straightforward; challenge: add new tools at efficient adapter-level cost while retaining existing tool use.
- **Methodology:** COTEX — continual tool-space extension learning: two sets of parameter directions: one triggers a tool call (opening a multi-turn reasoning trajectory), another chooses among tools; adapter of a new tool restricted to calling directions leaving earlier choices unaffected; protocol converts specialist models' task-specific annotations into verified tool-use trajectories.
- **Key innovations:** Adapter-level cost tool extension with provable earlier-tool-preservation.
- **Experimental results / 结果：** Two agents × three specialist tools, ten vision-language benchmarks: gains vs baselines with ≤ 0.3-point drop on existing tools.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.23810v1) · [PDF](https://arxiv.org/pdf/2611.23810v1)

#### 2611.19292v2 — Zero-Shot Weight-Space Programming for Prediction and Classification of Target Variables in Structured Datasets
**零样本权重空间编程：结构化数据集的预测与分类目标变量**

- **Authors / 作者:** Eduardo C. Garrido-Merchán (PDF page 1: Universidad Pontificia Comillas (IIT DIGNUM), Madrid)
- **Affiliation / 机构:** Universidad Pontificia Comillas (IIT DIGNUM) (PDF page 1)
- **Problem:** Weight-space programming fixes all parameters by hand (no gradient descent); supervised datasets withhold the specification — the procedure must infer the statistical specification itself and express it in the parameterization.
- **Methodology:** LLM writes out every weight/bias as a literal number (no optimizer, no gradient, no evaluation); graded suite: two toy + nine synthetic (hidden-rotation) + classical benchmarks + one real engineering regression; sealed constructions pre-register expected score.
- **Key innovations:** Zero-gradient zero-shot construction; LLM as the programmer; failures reveal structure-finding limits.
- **Experimental results / 结果：** Frozen network matches closed-form optimum on linear rungs, reaches irreducible error of the generating process on three nonlinear rungs; beats fitted baselines on two rungs; fails on two rungs (structure oblique to analyzed coordinates).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.19292v2) · [PDF](https://arxiv.org/pdf/2611.19292v2)

---

*End of digest — 30 papers. All metrics/results/claims author-reported; no full-text review; Chinese titles are translation aids; technical terms in English.*
