---
title: "Conference Digest: Venue Acceptances + Fresh-Window Papers — 2026-09-17"
type: synthesis
created: 2026-09-17
updated: 2026-09-17
sources: [conference-web-searches, arxiv-api]
tags: [conference-digest, ICML2026, EMNLP2026, CIKM2026, RecSys2026, KDD2026, COLM2026, ACM-MM2026, recommendation, LLM, agents, generative-models, sequential-modeling, code-execution, benchmarks, retrieval, RAG, evaluation, daily-digest]
---

# Conference Digest: Venue Acceptances + Fresh-Window Papers (2026-09-17)

> Focus: **new venue acceptances observed this cycle** (EMNLP 2026 Main/Findings/workshops, RecSys 2026, CIKM 2026 Resource, COLM 2026, ACM MM 2026, KDD 2026 workshop, ICML 2026 MechInterp workshop) **+ fresh Thu 17 Sep 2026 arXiv window** (Wed 16 Sep submissions, IDs **2609.17532–2609.19145**). Every arXiv ID in this digest is **grep-verified 0 hits** in `wiki/` and disjoint from same-day sibling [[arxiv-ai-search 2026-09-17|arxiv-ai-search 2026-09-17]] (26 claimed IDs). Venues fully digested previously (SIGIR/ACL/ICML/ICLR/CVPR/WWW/KDD main) are referenced but not re-detailed.

---

## 1. Venue Highlights — What's New This Cycle

| Venue | Status | New in this digest |
|---|---|---|
| EMNLP 2026 (Nov) | Acceptances posted | **6 new**: Main — Re2A, Gated-Memory Routing, ME-Decoding; Findings — SOVER, Low-Resource feature transfer; GroundLM workshop — PageRecall; plus rubric-artifact audit (EMNLP 2026) |
| RecSys 2026 (Sep 28–Oct 2, Minneapolis) | Upcoming (in 11 days) | **MODE** (reciprocal rec mutual optimality) — accepted |
| COLM 2026 | Acceptances posted | **MoRE** (Mixture of Reused Experts) — accepted |
| CIKM 2026 (35th, Oct) | Acceptances flowing | **SIDInspector** (Semantic-ID tokenizer diagnostics, Resource Track) |
| ACM MM 2026 | Acceptances posted | **MAGER** (multi-agent genetic meta-path discovery, Oral) |
| KDD 2026 (Aug, held) | Workshop papers | **AgentWorld** (Agent4IR workshop: personality-aware agentic-IR reliability) |
| ICML 2026 (Jul, held) | Workshop acceptances | **Relation Before Entity** (MechInterp workshop) |
| NeurIPS 2026 | Decisions **Sep 24** (7 days out) | Watch for post-decision preprint flood (next digest lookout) |
| ICASSP 2027 | In review | ERPBench (computer-use agents in ERP) — submitted, not yet accepted |

---

## 2. EMNLP 2026 — New Accepted Papers

### 2.1 Re2A: Situated Conversational Recommendation via Rubric-based Preference Reasoning [Main]
- **英文**: Re2A: Situated Conversational Recommendation via Rubric-based Preference Reasoning and Alignment
- **中文**: Re2A：基于 Rubric 偏好推理与对齐的场景化会话推荐
- **Authors**: Dongding Lin, Jian Wang, Xiaoyan Zhao, Wenjie Li
- **Affiliation**: Hong Kong Polytechnic University (tentative)
- **Venue**: EMNLP 2026 Main Conference
- **arXiv**: https://arxiv.org/abs/2609.18249

**Problem background**: Real-world recommendation is often **grounded in a shared physical environment** during the interaction — the assistant and user co-observe a scene (e.g., a store). This defines the *situated conversational recommendation* (SCR) task: jointly reason over dialogue history, co-observed scenes, and in-scene item attributes. Existing methods fail because (a) situated user preferences are hard to extract from mixed signals, and (b) responses must satisfy both user needs *and* grounded-situation constraints.

**Methodology**: Re2A formulates SCR as a structured **reason-then-align** process:
1. **Rubric-based preference reasoning** — automated rubrics guide the model to emit an explicit, structured preference state from dialogue + scene evidence;
2. **Preference-conditioned alignment** — a dual-objective optimization aligns response generation with user-preference satisfaction and situation consistency.

**Results**: Consistently outperforms SOTA on **two SCR datasets**, delivering more precise, context-aware conversational recommendations. Code: github.com/DongdingLin/Re2A.

**Comparison with prior methods**: vs pipeline methods that treat dialogue and vision separately, Re2A makes the preference state an *explicit checkpoint* the response must satisfy, closing the "understands but doesn't act on" gap typical of end-to-end multimodal recommender assistants.

### 2.2 Gated-Memory Routing: Efficient Multi-Agent LLM Orchestration [Main]
- **英文**: Learning What to Retain: Gated-Memory Routing for Efficient Collaboration in Multi-Agent LLM Systems
- **中文**: Gated-Memory Routing：为多 Agent LLM 系统学习"该保留什么"
- **Authors**: Rakibul Hasan Rajib, Mengxin Zheng, Qian Lou
- **Affiliation**: University of Central Florida (tentative)
- **Venue**: EMNLP 2026 Main Conference
- **arXiv**: https://arxiv.org/abs/2609.00237

**Problem background**: LLM-based multi-agent systems must adapt orchestration to evolving collaboration state. Routing from the *query alone* ignores intermediate progress/errors; routing from the *full execution history* incurs cost and redundancy (execution-history overload).

**Methodology**: **Gated-Memory Routing** introduces a learned execution memory:
- **Memory Write Gate** — commits only *non-redundant* reasoning steps to memory;
- **Retrieval Gate** — serves each agent a compact, relevant memory subset;
- **Adaptive Halting Controller** — stops execution once memory holds enough evidence.

**Results**: Across five reasoning + code benchmarks: **best average accuracy, exceeding strongest baseline by +2.44 points**, while cutting HumanEval inference cost by **31.9%** vs that baseline. Code: github.com/rajibrhasan/gated-memory-routing.

**Comparison with prior methods**: vs query-only routing (no adaptivity) and full-history routing (costly), Gated-Memory Routing is the third option — *state-conditional, compact, learned*; the write-gate is the mechanism novelty that prevents memory poisoning by redundant steps.

### 2.3 ME-Decoding: Decoding as Ensemble Pruning [Main]
- **英文**: Beyond Truncation: Rethinking LLM Decoding as Ensemble Pruning
- **中文**: 超越截断：将 LLM 解码重新思考为集成剪枝
- **Authors**: Dunyao Xue, Chengshuo Du, Zhengbo Wang, Wenlin Dai, Cheng Meng
- **Affiliation**: Rensselaer Polytechnic Institute (tentative)
- **Venue**: EMNLP 2026 Main Conference
- **arXiv**: https://arxiv.org/abs/2609.18723

**Problem background**: Token-selection decoding relies on scalar probabilities, ignoring geometry/semantics among candidates, causing redundancy; while geometry-aware alternatives require expensive optimization or destabilize probability weighting.

**Methodology**: **Mahalanobis-Ensemble Decoding (ME-Decoding)** frames token selection as **subset optimization**:
- Mahalanobis-distance objective maximizes semantic diversity while keeping high probability;
- A token-similarity matrix (adaptive-bandwidth kernel over embeddings) dynamically discounts redundant generation paths;
- Greedy selection with **near-linear complexity** under early stopping + theoretical approximation guarantees ⇒ a **plug-and-play module with negligible overhead**.

**Results**: Consistent strong gains across diverse reasoning and generation tasks.

**Comparison with prior methods**: vs naive truncation/top-k (redundancy-blind) and geometry-aware reranking (heavy), ME-Decoding is the middle ground: geometric diversity reasoning at near-zero inference overhead, with formal approximation bounds.

### 2.4 Judging LLM-as-a-Judge: Rubric Artifacts [EMNLP 2026]
- **英文**: Judging LLM-as-a-Judge: Concerning Rubric Artifacts in LLM-based Automated Text Generation Evaluation
- **中文**: 审判断审者：LLM 自动评估中的 Rubric 伪影
- **Authors**: Anshul Bagaria, Sowmya S Sundaram, Gokul S Krishnan, Balaraman Ravindran
- **Affiliation**: Indian Institute of Technology Madras (tentative)
- **Venue**: EMNLP 2026
- **arXiv**: https://arxiv.org/abs/2609.02942

**Problem background**: LLM-as-a-Judge pipelines assume judgments come from *reasoning over candidate responses w.r.t. a rubric*. This paper attacks that assumption.

**Findings**:
1. Classifiers trained **only on rubric text** (no response seen) achieve nontrivial predictive performance on judge outputs ⇒ rubrics encode recoverable evaluative signals, so scores can be anticipated *independently of outputs*;
2. **Counterfactual perturbations**: judges often fail to update decisions when the candidate response *or* the rubric criterion is reversed.

**Significance**: Rubric-based LLM evaluation may be partly a **rubric artifact**, not evidence of candidate-quality reasoning — joins the growing critique line (see 09-16: Magnitude Mirage, FAE) about what LLM judges actually measure. (convergent evidence with 09-16 digest's evaluation-trust theme)

### 2.5 SOVER: Formal Certification of Optimization Reformulations [Findings]
- **英文**: SOVER: Formal Certification of Optimization Reformulations via LLM-Assisted SMT Verification
- **中文**: SOVER：经 LLM 辅助 SMT 验证的优化问题改写形式化认证
- **Authors**: Swapnil Bhattacharyya, Mayank Baranwal
- **Affiliation**: COMET Lab / Tata Consultancy Services Research (tentative)
- **Venue**: EMNLP 2026 Findings
- **arXiv**: https://arxiv.org/abs/2609.00728

**Problem background**: LLMs translate/reformulate math-optimization problems across modeling languages, but *empirical solver validation is unreliable* (local minima, timeouts, numerical artifacts, semantic divergence).

**Methodology**: **SOVER** separates semantic mapping from formal certification:
- **Z3** checks domain cross-feasibility + global objective-order preservation for MILP formulations;
- **dReal** gives tolerance-aware feasibility/range + ε-argmin checks for continuous nonlinear formulations;
- New benchmark **NLEquiv-150**: 100 equivalent + 50 deliberately hard non-equivalent nonlinear reformulation pairs.

**Results**: With LLM-extracted mappings, SOVER classifies **149/150 pairs (99.33%)**, including all 50 hard negatives; the sole error is incomplete mapping extraction.

**Comparison with prior methods**: vs empirical solver-execution validation, SOVER adds *mathematical certification* — the "prove-not-probe" upgrade for LLM codegen in optimization.

### 2.6 Enhancing Low-Resource Language Reasoning via HRL Feature Transfer [Findings]
- **英文**: Enhancing Low-Resource Language Reasoning via High-Resource Language Feature Transfer
- **中文**: 借道高资源语言特征迁移增强低资源语言推理
- **Authors**: Minju Song, Hyeon Hwang, Junhyun Lee, Jaewoo Kang
- **Affiliation**: Korea University (tentative)
- **Venue**: EMNLP 2026 Findings
- **arXiv**: https://arxiv.org/abs/2608.30462

**Problem background**: LLMs vary wildly in performance across languages on semantically equivalent tasks. Prior work treats this as an observational disparity (pretraining/tokenization/benchmark coverage). This paper tests a *mechanistic* hypothesis: **high-resource languages (HRLs) elicit task-relevant latent computations more reliably**; low-resource languages (LRLs) under-activate them.

**Methods & results**: Sparse-autoencoder feature analysis over residual-stream activations identifies features enriched in successful HRL task-specific reasoning, filters out source-language/generic features, then **steers** LRL inference with those directions. Causal checks: suppressing features impairs HRL reasoning; activating them partially recovers LRL reasoning beyond random/non-task controls. Reframes cross-lingual gaps as **failures of mechanism elicitation, not capability absence** — transfer without translation/fine-tuning.

**Comparison with prior methods**: vs data-level transfer (translation, synthetic bilingual data) and model-level transfer (LoRA, MT), this is *feature-level / representation-level* transfer with causal validation — a distinct and controllable intervention tier.

### 2.7 PageRecall: Literature-Grounded QA — a GroundLM Shared-Task System
- **英文**: PageRecall: Measuring Page Selection in Literature-Grounded Question Answering
- **中文**: PageRecall：文献锚定问答中的页级选择度量
- **Authors**: Aaditya Chauhan
- **Affiliation**: — (team Everest, GroundLM 2026)
- **Venue**: 1st Workshop on Grounding Language Models (GroundLM 2026), co-located with EMNLP 2026 (system description, LitTraceQA shared task)
- **arXiv**: https://arxiv.org/abs/2609.18154

**Problem background**: LitTraceQA: given a research question, retrieve relevant papers from a pool of 27,487, cite the page + table/figure, answer in a requested format.

**Key finding**: **evidence grounding is limited by retrieval, not reading.** The page selector hits the gold page only ~52.6% of the time; the locator model, given the right page, cites correctly 94% of the time. When the page was missing, the pipeline **failed quietly ~2× more often than visibly** (14 silent + 24 wrong-page vs 7 correct).

**Jury-rigged fix**: since each retrieved paper fits in context, **stop choosing** — show the whole paper; gold-page recall → **100%** on parseable papers. Position-based questions are served by bibliography parsing (addressable reference list). Final held-out scores: **0.762 paper F1, 0.441 evidence F1, 0.920 MCQ accuracy**.

**Takeaway**: same diagnosis as §2.4/09-16 convergent theme — evaluation quality is limited by a *selection layer*, and "retrieval headroom" is often the real bottleneck in RAG.

---

## 3. RecSys 2026 — New Accepted Paper

### 3.1 MODE: Mutual Optimality in Reciprocal Recommendations (Matching Markets)
- **英文**: MODE: Mutual Optimality in Direct Effects of Reciprocal Recommendations in Matching Markets
- **中文**: MODE：匹配市场中互惠推荐的直接效应互最优性
- **Authors**: Yoji Tomita
- **Affiliation**: NTT DOCOMO (tentative)
- **Venue**: RecSys 2026
- **arXiv**: https://arxiv.org/abs/2608.01731

**Problem background**: Matching platforms (jobs, dating) rely on **reciprocal recommendation systems (RRS)** that consider both sides' preferences and avoid concentrating opportunities on a few popular users. But pushing concentration mitigation too hard yields undesirable recommendations for individual users → dissatisfaction.

**Methodology**: Formalizes **"optimality of direct effects"** of one user's recommendation list *given the recommendations to everyone else*, then proposes **MODE** to compute **mutually optimal recommendations in direct effects** (joint consideration of what is good for the individual and what is good for the counterpart population).

**Results**: On synthetic + real-world data, MODE beats existing methods on mutual optimality, is **faster**, and enables **higher expected number of matches**.

**Comparison with prior methods**: standard RRS focus on per-side relevance or global fairness; MODE operationalizes the *interdependence* of recommendation lists (what I'm shown changes what you're shown), a game-theoretic upgrade for two-sided marketplaces. (Theoretically aligned with the 09-16 mechanism-design line: ROI-constrained auctions, incentive-compatible marketplaces.)

---

## 4. COLM 2026 — New Accepted Paper

### 4.1 MoRE: Mixture of Reused Experts
- **英文**: MoRE: Mixture of Reused Experts
- **中文**: MoRE：复用专家混合（MoE 专家共享）
- **Authors**: Eric S. Qiu, Utku Umur Acikalin, Justin Lovelace, Christian Belardi, Arjun B. Mulchandani, Carla P. Gomes, Kilian Q. Weinberger
- **Affiliation**: Cornell University (tentative)
- **Venue**: Conference on Language Modeling (COLM) 2026
- **arXiv**: https://arxiv.org/abs/2609.18176

**Problem background**: MoE decouples capacity from compute but memory grows linearly with expert count; **weight-sharing (recurrent) Transformers** reuse layer weights for parameter efficiency but lack capacity for competitive LM.

**Methodology**: **MoRE** shares expert pools across *groups of adjacent layers*: each layer keeps its own router but selects from a larger shared pool → more routing combinations without new parameters. Lightweight learnable **depth embeddings** condition each layer's input before routing so shared experts can differentiate layers.

**Results**: Across 3 scales (114M–1.15B params), MoRE achieves **lower perplexity and stronger downstream performance** than standard MoEs and SOTA weight-sharing architectures at matched compute/parameter budgets, with minimal changes to existing MoE code.

**Comparison with prior methods**: vs per-layer-expert MoE (memory grows) and full weight-sharing recurrent LM (capacity-starved), MoRE sits between: shared-but-depth-conditioned expert pool. Related family: 09-14 linear-attention GR (OneLA), 09-16 auto-regressive-SSM weight-transfer (Agora §7.3).

---

## 5. CIKM 2026 — New Accepted Paper (Resource Track)

### 5.1 SIDInspector: Mapping-First Diagnostics for Semantic-ID Tokenizers
- **英文**: SIDInspector: A Mapping-First Diagnostic Resource for Semantic-ID Tokenizers
- **中文**: SIDInspector：面向 Semantic-ID Tokenizer 的"映射优先"诊断资源
- **Authors**: Jiandong Ding, Heng Chang, Huijie Qin, Tianying Liu
- **Affiliation**: Tsinghua University (tentative)
- **Venue**: CIKM 2026 Resource Track
- **arXiv**: https://arxiv.org/abs/2606.10375

**Problem background**: **Semantic-ID (SID) tokenizers** are increasingly reused as *standalone artifacts* in generative recommendation — an exported item-to-code mapping becomes the address space a later sequence generator must use. These mappings lack a common inspection interface; coverage gaps, code aliasing, weak prefixes, tail compression, and prefix fan-out surface only *after* downstream training.

**Methodology**: **SIDInspector** — a mapping-first diagnostic resource: defines an adapter contract over item mappings/metadata/interactions/generator traces; validates it; reports mapping-level probes for **utilization, aliasing, neighborhood alignment, popularity allocation, structural cost**, with hooks for temporal churn and generator traces — *independent of downstream leaderboard scores*. Covers GRID-style RQ-KMeans (2 capacities), bounded ReSID/GAOQ, LETTER, LC-Rec artifacts.

**Results**: D2 aliasing drops 0.977 → 0.779 under added GRID capacity and → 0.000 for ReSID/GAOQ; D3 stays below a category-prefix control (0.055–0.154 vs 0.447).

**Significance**: Positions SID *artifact quality* as a distinct, testable property before method-level evaluation — a standardization step for generative retrieval (ties to SID-reasoning direction noted at KDD'26, and GR line in arxiv-ai-search 09-17).

---

## 6. ACM MM 2026 — New Accepted Paper (Oral)

### 6.1 MAGER: Multi-Agent Genetic Meta-Path Discovery for Fake-News Detection
- **英文**: Reasoning through Evolution: Automatic Meta-path Discovery for LLM-based Fake News Detection
- **中文**: 通过演化进行推理：面向 LLM 假新闻检测的自动 Meta-path 发现
- **Authors**: Ziyi Zhou, Xiaoming Zhang, Hui Pang, Yuting Zhang, Tiesunlong Shen, Bingyu Yan, Erik Cambria, Litian Zhang
- **Affiliation**: Beihang University / NTU (Cambria) (tentative)
- **Venue**: ACM MM 2026, **Oral**
- **arXiv**: https://arxiv.org/abs/2609.18597

**Problem background**: Propagation structure is critical for fake-news detection, but supervised GNNs need heavy labels + generalize poorly; LLMs can't ingest raw propagation graphs (modality mismatch, information overload).

**Methodology**: **MAGER** — a multi-agent **genetic evolution** framework:
- Evolves **meta-paths** that compress huge propagation graphs into informative subgraphs, enabling frozen LLMs to do structure-aware veracity reasoning;
- **Graph in-context learning** retrieves semantically+structurally similar demonstrations.

**Results**: Substantially improves frozen LLMs as standalone fake-news detectors in data-efficient (zero/few-shot) settings. Code: github.com/SenticNet/MAGER.

**Comparison with prior methods**: vs supervised GNNs (label-hungry, low generalization) and direct LLM-on-graphs (overload), MAGER evolves *compact structure primitives* the LLM can actually reason over — a program-synthesis-like angle on graph-LLM integration (distinct from the agentic graph-RAG of Cognition-on-Graph, 09-16).

---

## 7. KDD 2026 Workshop — New Accepted Paper

### 7.1 AgentWorld: Personality-Aware Reliability Evaluation for Agentic IR
- **英文**: AgentWorld: Personality-Aware Reliability Evaluation for Agentic Information Retrieval
- **中文**: AgentWorld：面向 Agentic 信息检索的人格感知可靠性评测
- **Authors**: Gunja Agarwal, Arup Kumar Das, Arun Menon, Jitesh Chandra Mishra, Vignesh Divakaran
- **Affiliation**: Microsoft (tentative)
- **Venue**: Agent4IR @ KDD 2026 (workshop)
- **arXiv**: https://arxiv.org/abs/2608.24076

**Problem background**: Agentic-IR evaluation is stuck on **scripted interactions with uniform users** — missing natural personality diversity and adversarial brittleness.

**Methodology**: **AgentWorld** = simulation framework with:
1. **Big Five (OCEAN) personality-driven user populations** + stateful tool-use environments;
2. **pass^k consistency metric** with structured fault classification, partial credit, dual-control handoff verification;
3. thresholded training-data export (6 fine-tuning formats);
4. **adversarial Risk Analyser**: snapshots required-intermediate-state spines, Monte-Carlo rollouts under 4 perturbation types, risk via ΔP/ΔT scoring + Dempster–Shafer fusion + Shapley attack attribution.

**Results**: 3 experiments — conversational analytics agent across 10 personas (240 judgments); customer-support agent 5×4; adversarial stress of 5 tasks finding pre-existing brittleness (V_min=0.375), with tool/infra-layer attack dominance (Shapley: 46% system / 38% action). Personality variation surfaces failure modes uniform testing can't: cross-domain leakage, contextual drift, a 0.27-point quality gap, and **50% vs 100% pass-rate across personas on the same task**.

**Comparison with prior methods**: vs uniform-user pass@k leaderboards, AgentWorld's Risk Analyser quantifies *trajectory-level brittleness* that pass^k alone cannot measure — extending the agent-reliability evaluation theme of 09-16 (Emergence World, Enforcement Gap).

---

## 8. ICML 2026 Workshop + Under-Review

### 8.1 Relation Before Entity: Deferred Commitment in Factual Recall [ICML 2026 MechInterp WS]
- **英文**: Relation Before Entity: Deferred Commitment in Language Model Factual Recall
- **中文**: 先关系后实体：语言模型事实召回中的延迟承诺
- **Author**: Divyansh Agarwal
- **Affiliation**: Carnegie Mellon University (tentative)
- **Venue**: Mechanistic Interpretability Workshop, ICML 2026
- **arXiv**: https://arxiv.org/abs/2609.17537

**Finding** (4 decoder-only models, 8 prompt families, 4 causal diagnostics): relation-type info (e.g., *capital-of*) becomes generation-controlling **10–16 layers BEFORE entity info** (31–44% of network depth at threshold 0.4), robust across all 16 model×threshold combos. Critically, entity info is *not absent* early (patching succeeds 90–100% in early layers) — instead **entity commitment is deferred**: the entity token is computed early but routed to the final token only later.

**Significance**: refines the "conjunctive recall" picture of ROME-style mechanisms into a *two-phase gate* (relation gate → delayed entity gate); implications for targeted editing and hallucination (deferred but wrong commitment). (tentative-interpretation)

### 8.2 ERPBench: Computer-Use Agents in Enterprise Software [under review, ICASSP 2027]
- **英文**: ERPBench: A State-Grounded Evaluation Paradigm for Computer-Use Agents in Enterprise Software
- **中文**: ERPBench：企业软件中 Computer-Use Agent 的状态锚定评测范式
- **Authors**: Kratika Bhagtani, Kusha Sridhar, Maziyar Baran Pouyan, Yuying Zhao, Eugene Siow
- **Affiliation**: SAP Labs (tentative)
- **Venue**: *submitted* to ICASSP 2027 (not yet accepted)
- **arXiv**: https://arxiv.org/abs/2609.17885

**Problem**: Computer-use agents are evaluated on general desktop/web tasks, but **ERP systems** (finance, procurement, inventory) are dense-interface, multi-step, and errors silently corrupt persistent business records. Existing enterprise benchmarks use proprietary platforms or simulated approximations.

**Method**: **ERPBench** evaluates screenshot-only agents on a *live, reproducible* ERP system, scoring each task against **ground-truth values in the database**; plus a production-grade harness that gates agent actions behind human approval.

**Results**: Evaluating 6 closed+open agents: **strong general GUI performance does not transfer** — some agents save in up to 85% of runs but write the correct value in as few as **3%**.

**Significance**: Enterprise computuer-use needs *state-grounded* (DB-verified) evaluation, not screenshot-level task success — same lesson as StableEval Arena (§9.6) on state-vs-syntax trustworthiness.

---

## 9. General Recent Papers (fresh window, category-organized)

All IDs grep-verified **0 hits** in `wiki/`, outside sibling-claimed sets.

### 9.1 LLM Architecture & Adaptation (LLM)
#### Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data
- **英文/中文**: Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data / 无限参数量 LLM：从实时数据生成与适配权重
- **Authors**: Jinli Hu, Ross M. Clarke, Yichuan Zhang, José Miguel Hernández-Lobato
- **Affiliation**: University of Cambridge / MAX-AI (tentative) · **arXiv**: https://arxiv.org/abs/2609.18842
- **Abstract/innovation**: The scaling-law success of MoE depends on *static pretraining data*, but a deployed model faces live interaction (user facts, corrections) it cannot write into frozen weights — today such knowledge lives in the prompt and is re-read then discarded. The **Infinite-Parameter LLM** answers "how could an architecture learn from live interaction *in its weights*": a compact **hypernetwork** turns runtime data into a *low-rank modulation* of a shared base network (like MoE, but weights are *generated*, not stored). Unlike prior weight-generators that read context once then freeze, it keeps a **Bayesian belief over the generator's latent code, updated online**, so the effective weight re-derives from an evolving belief across the session. Fixed storage, effectively infinite weights; #knowledge-in-weights amortizes compute, frees context, persists across turns, and can generalize better than in-context use. Includes an evaluation protocol pitting it against ICL and retrieval.

#### Nemotron-SEA-LION-v4.8 (NVIDIA) — Technical Report
- **英文/中文**: Nemotron-SEA-LION-v4.8: A Technical Report / Nemotron-SEA-LION-v4.8 技术报告
- **Authors**: SEA-LION team (NVIDIA + AI Singapore ecosystem, ~60 authors listed)
- **Affiliation**: NVIDIA / AI Singapore · **arXiv**: https://arxiv.org/abs/2609.18310
- **Abstract/innovation**: SEA-LION built on NVIDIA Nemotron 3: **30B-A3B and 120B-A12B**, continued-pretrained + SFT + online on-policy distillation. Adapted on Southeast Asian, reasoning, code, and multilingual-parallel data. On SEA-HELM: 30B-A3B overall SEA score **46.06→51.57**; 120B-A12B **49.30→63.44**; biggest gains in instruction following, natural-language reasoning, and NLU across 7 SEA languages. Regional LLM play, NVIDIA-branded — adds to multilingual-model track (cf. AnglaBharat etc. elsewhere).

### 9.2 Decoding & Sampling (inference)
#### Accelerating Diffusion Sampling via Speculative Draft Trees
- **英文/中文**: Accelerating Diffusion Sampling via Speculative Draft Trees / 经投机草稿树加速扩散采样
- **Authors**: Marcello Bullo, Yanxiao Liu, Öykü Sıla Güner, Arpan Mukherjee, Deniz Gündüz
- **Affiliation**: Imperial College London (tentative) · **arXiv**: https://arxiv.org/abs/2609.17691
- **Abstract/innovation**: Speculative sampling accelerates diffusion by drafting cheap candidate states corrected under a distribution-preserving coupling. Existing samplers (reflection maximal coupling) are **topologically constrained to a linear chain** of lookahead drafts, limiting acceptance per target eval. Connecting speculative sampling to **relative entropy coding (REC)** shows the lookahead need not be linear → **draft trees**: richer candidate sets per round, fewer target FEs. Greedy-rejection-sampling coupling (an REC algorithm) improves acceptance while preserving exactness. Up to **8.3% acceleration over reflection coupling** across diverse target/draft models. (Generative-models + sampling-efficiency line; cf. 09-16 SpecDel.)

### 9.3 Retrieval / RAG (retrieval)
#### DRAG: One Size Does Not Fit All — Dynamic Retriever+Generator Selection for RAG
- **英文/中文**: One Size Does Not Fit All! Dynamic Retriever and Generator Selection for RAG / RAG 中检索器与生成器的动态联合选择
- **Authors**: Neeraj Anand, Payel Santra, Partha Basuchowdhuri, Debasis Ganguly, Sumit Bhatia
- **Affiliation**: IBM Research India (Ganguly: tartu?) (tentative) · **arXiv**: https://arxiv.org/abs/2609.17709
- **Abstract/innovation**: RAG pipelines fix retriever+generator configs across queries despite wildly different complexity. Shows retriever complexity dominates gains but both exhibit **diminishing and non-monotonic returns** — bigger isn't uniformly better. **DRAG** = joint adaptive selection: **DRAG-QPP** (training-free; QPP for retrievers, perplexity over retrieved context for generators) and **DRAG-SFT** (LLM fine-tuned to jointly predict retriever-generator configs). Across 3 LLM families × 4 QA benchmarks: DRAG-QPP ≈ static strong baselines at substantially lower latency; DRAG-SFT **consistently beats static and adaptive baselines**. Joint adaptation beats static on the efficacy/cost frontier. (Same theme as 09-16 QueryRoute/ORDER — routing signals, now on the *retriever-generator pair*.)

#### Time-Aligned Evolving Concept Graphs for Scientific Relation Forecasting
- **英文/中文**: Time-Aligned Evolving Concept Graphs for Scientific Relation Forecasting / 时间对齐的演化概念图用于科研关系预测
- **Authors**: Fred Sun, Jingze Wang, Minkun Xu, Shangqi Guo · **Affiliation**: Rice University (tentative) · **arXiv**: https://arxiv.org/abs/2609.18163
- **Abstract/innovation**: Existing scientific-relation-forecasting methods model concept semantics and graph structure separately or coarsely. Proposal: treat **dated papers as shared update events**, reconstructing semantic + structural states from the *same* publication history at each prediction time, then **pair-level fusion** forecasts first co-occurrence / relation formation / conditional relation type. Refreshing context alongside graph updates improves mean relation AUPRC **+16.6%** over frozen context; full framework: mean relation AUROC **0.9290→0.9722** on a 187,848-paper / 270,687-concept / 7.45M-link graph.

#### DUPAR: Dual-Path Conversational Retrieval via Speech Retriever with Cross-Turn Caching
- **英文/中文**: DUPAR: Dual-Path Conversational Retrieval via Speech Retriever with Cross-Turn Evidence Caching / 带跨轮证据缓存的语音检索器双路径会话检索
- **Authors**: Yuanjun Li, Yiwen Liu, Dapeng Li, Zhiwei Xu, Bin Zhang, Shengtao Zhang, Rong Shen · **Affiliation**: Shanghai Jiao Tong University (tentative) · **arXiv**: https://arxiv.org/abs/2609.18042
- **Abstract/innovation**: Voice assistants do ASR→text-retrieve; the cascade adds latency + propagates ASR errors, while direct speech retrieval suffers cross-modal misalignment. **DUPAR** = slow+fast paths: fast path aligns a task-adapted audio encoder with frozen BGE-M3 text embeddings over a **cross-turn evidence cache**; on low confidence, slow path fuses full-index retrieval (audio + ASR-transcript embeddings), and the result refreshes next-turn cache via **one-hop graph expansion**. Trained audio encoder approaches text-retrieval accuracy on clean speech at **3.75× query-side speedup** over ASR+Text; noise-benchmark Recall@10 **0.771→0.875**; Recall@1 **+4.2pp** across speaking styles; cache significantly cuts errors on one-hop follow-ups.

### 9.4 Agents & Autonomous Research (agents)
#### PrimeScientist: Strategic Allocation of Research Effort
- **英文/中文**: PrimeScientist: Strategic Allocation of Research Effort in Autonomous Research / PrimeScientist：自主科研中的研究投入策略分配
- **Authors**: Xinle Yu, Fan Bai, Kaiser Sun, Hengshuo Miao, Abhay Anand, Zhongyan Luo, Kun Zhou, Zhen Wang
- **Affiliation**: Nanjing University / Bytedance Seed (tentative) · **arXiv**: https://arxiv.org/abs/2609.17846
- **Abstract/innovation**: Autonomous research agents can propose more directions than resources allow, and each attempt is costly — so *when to stop and re-invest* is the defining skill. **PrimeScientist** formulates effort allocation as a sequential decision problem where *remaining resources explicitly guide the policy*: an **executable plan tree** preserves competing plans/results across attempts, and an **adaptive MCTS** policy balances exploration/exploitation with feedback + remaining budget. Across AI research, systems/code-optimization, and ML-engineering tasks: **+10.3% average reward with 50.6% fewer research attempts** than AutoResearch under the same budget (12 AI-research tasks). Positions resource-use efficiency as a first-class research capability (cf. Agora below, and 09-16 agent budgetization line — LIMBO/PolicyMem).

#### Agora: Git as Shared Memory for Collective AutoResearch
- **英文/中文**: Agora: Git as Shared Memory for Collective AutoResearch / Agora：把 Git 当作集体自主科研的共享记忆
- **Authors**: Yifan Zhang, Yunheng Zou, Shaokun Zhang, Jian Hu, Hao Zhang, Binfeng Xu, Jan Kautz, Yi Dong
- **Affiliation**: University of California San Diego / NVIDIA (Kautz) (tentative) · **arXiv**: https://arxiv.org/abs/2609.18094
- **Abstract/innovation**: Parallel AutoResearch sessions start from scratch → duplicated search, not discovery. **Agora** = shared memory over Git: research is stored as an **append-only DAG** where every claim is a commit anyone can check out/rerun; derived index exposes frontier, neglected branches, verification status; diversity-aware selection avoids monoculture collapse. Sustained first use: **~12 days, 13 LLM workers, no central planner**, on a weight-transfer problem (141 donor models → frozen 119.6M attention-SSM hybrid). Workers published **1,703 contributions**, moved the evaluator **3.39 → 1.899 bits/byte** (closing 62% of gap to trained GPT-2 124M), with a 145-commit winning ancestry across 15 accounts and 165 independent non-failing reproductions. One mid-run human intervention pulled the community out of monoculture. Companion read for §9.11 (Agora) — and connects to 09-17's [[arxiv-ai-search 2026-09-17|sibling]] weight-transfer theme contexts.

#### RideWay: Efficiency-Centered Benchmark for Tool-Using Agents
- **英文/中文**: RideWay: Benchmarking Efficient Task Completion for Tool-Using Language Agents / RideWay：工具型语言 Agent 的效率化任务完成基准
- **Authors**: Qingnuan Han, Boli Fang, Mingzhi Hou, Claire Liu · **Affiliation**: Uber (Fang) / Stanford (tentative) · **arXiv**: https://arxiv.org/abs/2609.17985
- **Abstract/innovation**: Agents are scored on *completion*, but successful agents can still frustrate users with repeated questions or redundant searches. **RideWay** = efficiency-centered benchmark (ridehailing agents, stateful tool-calling) + **Efficiency Utility** = success-gated metric discriminating excess tool calls and user-facing turns relative to task-specific reference effort, calibrated by human paired preferences. Fitted penalty for **excess turns ≈ 2× that for excess tool calls** (58 tasks, 24 models); held-out: 78.7% accuracy overall — **90.6% when turns differ, chance-level when only tool calls differ** (the axis annotators disagree on). Makes interaction efficiency measurable alongside success and exposes the boundary of count-based tool-use evaluation.

#### BekchiAI: Measure + Observe + Control LLM Agents
- **英文/中文**: BekchiAI: Measuring, Observing, and Controlling LLM Agents in One Click / BekchiAI：一键测量、观测与控制的 LLM Agent 平台
- **Author**: Mesut Toruk · **Affiliation**: — · **arXiv**: https://arxiv.org/abs/2608.26867
- **Abstract/innovation**: Agent skill (correctly sequencing tools, planning under dependencies, judging untrusted inputs, grounding claims) is hard to measure with accuracy-only leaderboards. **BekchiAI** = benchmark + platform: 13 tool-using ReAct agents / 7 task categories / **2,057 verifier-checkable committed tasks** (canonical SQL against real DB, exact DAG scheduling, lambda evaluation incl. adversarial security samples with deliberately imperfect scanners). Behavioral metrics beyond accuracy: tool-call adherence, URL hallucination & source-match, per-model token cost; 4-model comparison (Qwen3.7-Max, gemma-4-31B-it, gemma4:26b, gpt-oss-120b). Platform: token/latency telemetry + remote run termination. (Same "agent skill ≠ accuracy" thesis as ERPBench/StableEval.)

### 9.5 Reasoning & Hallucination (reasoning)
#### Recursive Reasoning or Statistical Extrapolation? ICL in Multi-Agent Games
- **英文/中文**: Recursive Reasoning or Statistical Extrapolation? In-Context Learning in Multi-Agent Interdependent Decision-Making / 递归推理还是统计外推？多 Agent 相互依赖决策中的 ICL
- **Authors**: Yu Liu, Wenwen Li, Yifan Dou, Guangnan Ye (Equilibrium Research) · **Affiliation**: — · **arXiv**: https://arxiv.org/abs/2609.18591
- **Abstract/innovation**: Does ICL improve LLM-agent decisions via refined *internal reasoning* or mere *statistical extrapolation*? Public-goods game with manipulated feedback structure + history-independent **rational-expectations-equilibrium (REE)** benchmark: when historical statistical patterns are disrupted, longer-context benefits largely vanish (degrading to no-context baseline), sharply amplified by stronger strategic interdependence. Verdict: in strategic environments, ICL ≈ **statistical extrapolation, not recursive reasoning**. Introduces REE as a diagnostic to distinguish the two; reusable framework for probing recursive-belief limits. (Multi-agent/game-theory strand — connects to 09-16 MARL congestible-markets line.)

#### Attention Dispersion as a Hallucination Signal
- **英文/中文**: Attention Dispersion as a Diagnostic Signal for Hallucination in Large Language Models / 注意力分散作为 LLM 幻觉的诊断信号
- **Authors**: Shardul P. More, Tanuja S. Pawar · **Affiliation**: — · **arXiv**: https://arxiv.org/abs/2609.18320
- **Abstract/innovation**: Logit-based confidence is miscalibrated by alignment; proposes **attention dispersion** (unsupervised metric) as a calibration-independent hallucination signal: spikes in attention entropy mark reasoning breakdowns in intermediate layers. On GSM8K + MATH-500 with Qwen2.5 (1.5B/3B): **AUC +0.076 over output-based baselines** across all tested conditions. (Cheap internal-state doctor; cf. 09-16 Z-Loss reverse-geometry for a different intermediate-signal angle.)

### 9.6 Benchmarks & Evaluation (benchmarks)
#### StableEval Arena: Cost-Aware Benchmark for Stablecoin Peg-Risk Agents
- **英文/中文**: StableEval Arena: A Cost-Aware Agentic Benchmark for Stablecoin Price Stability Prediction / StableEval Arena：稳定币价格稳定性预测的成本感知 Agentic 基准
- **Authors**: Sean Wan, Dongping Liu, Luyao Zhang · **Affiliation**: Duke Kunshan University (tentative) · **arXiv**: https://arxiv.org/abs/2609.18949
- **Abstract/innovation**: Evaluates LLM-backed agents on stablecoin peg-stress diagnosis + 7-day peg-deviation forecasts via **leakage-safe historical replay** (exchange price-volume + market-context features). 120-case stress block + 507-case full arena; 6 agent configs + baselines. Treats trustworthiness as joint (quality, calibration/label behavior, structured-output reliability, latency, tokens, cost): agents give **reliable structured outputs at modest cost but miss most rare severe-stress / sustained-depeg cases** — a protocol-vs-financial reliability gap. Dataset on Hugging Face, code on GitHub.

#### MUSE: LVLMs on Artistic Image Understanding in Education
- **英文/中文**: MUSE: Benchmarking Large Vision-Language Models on Multi-Modal Understanding in Situated Education / MUSE：评测大视觉语言模型在场景化教育中的多模态理解
- **Authors**: Luyao Zhu, Xun Wei Yee, Wei Li, Mun Thye Mak, Wee Siong Ng · **Affiliation**: Nanyang Technological University (tentative) · **arXiv**: https://arxiv.org/abs/2609.19088
- **Abstract/innovation**: LVLM benchmarks cover real-world images or domain-specific reasoning but not *artistic educational* content. **MUSE** decouples image annotation from question generation (controllable difficulty, less annotation): 12 tasks over perception, semantic/affective interpretation, culture understanding, compositional reasoning; curated to center Singaporean/Southeast-Asian multicultural contexts + Western art. Open + proprietary models show substantial disparities, especially **affective interpretation and compositional reasoning**; documents failure modes for trustworthy multimodal education AI.

### 9.7 Code Execution & Systems (code-execution)
#### CompileRover: LLM-Driven VM Compiler Optimization
- **英文/中文**: CompileRover: Revolutionizing Virtual Machine Compiler Optimization with a Tri-Role LLM-Driven Framework / CompileRover：三角色 LLM 驱动的 VM 编译器优化框架
- **Authors**: Mingqiao Mo, Yunlong Tan, Hao Zhang · **Affiliation**: — · **arXiv**: https://arxiv.org/abs/2609.19004
- **Abstract/innovation**: VM compiler outputs exhibit redundant computations, inefficient loops, suboptimal functions. **CompileRover** = tri-role collaboration (**referee / advisor / operator**) using control-flow analysis, structure transformations, and dynamic execution-pattern recognition. Consistently surpasses SOTA VM compilers on various benchmarks, reducing execution overhead and improving dataflow consistency.

#### ScienceIDE: Turning the World's Scientific Codebase into Agent Environments
- **英文/中文**: ScienceIDE: Turning World's Scientific Codebase into Agent Learnable Environments / ScienceIDE：把全球科研代码库变成 Agent 可学习环境
- **Authors**: Hejia Geng, Zesen Huang, Haoyang Li, ... (50+ authors incl. Lanqing Yuan, Zhenlin Zhu ...) · **Affiliation**: AITOF (Zhengzhou University) (tentative) · **arXiv**: https://arxiv.org/abs/2609.19134
- **Abstract/innovation**: Scientific code encodes decades of knowledge, but fragmented toolchains/implicit conventions/specialized correctness criteria block machine learning on it (the **scientific experience bottleneck**). **ScienceIDE** = infrastructure to convert repositories into programmable, verifiable agent environments (task generation, execution, scientific verification via expert-defined acceptance criteria). Using verified trajectories, trains **PhAI-IDE-72B / 9B / 4B**, which gain on held-out scientific-code repair *and* general code/reasoning/knowledge — evidence of positive transfer from scientific experience. Code: github.com/aitofound/ScienceIDE. (The "AI Scientist infrastructure" line — joins PrimeScientist/Agora in a systems framing.)

---

## 10. Category Signals Across the Digest

| Category | Signal this cycle | Headline |
|---|---|---|
| **Recommendation** | RecSys'26 + EMNLP'26 | MODE adds reciprocal/game-theoretic mutual optimality to two-sided matching; Re2A grounds conversational rec in situated scenes via explicit rubrics |
| **LLM & reasoning** | EMNLP'26 Main | Decoding-as-ensemble-pruning (ME-Decoding); multi-agent state gating (Gated-Memory Routing); early relation-late entity recall mechanism |
| **Evaluation** | Convergent audit wave | LLM-as-judge rubric artifacts + PageRecall show "selection layer" is the real bottleneck; ERPBench + StableEval make state/ground-truth the scoring object |
| **Retrieval / RAG** | Routing + standards | DRAG jointly routes retriever+generator; SIDInspector standardizes Semantic-ID artifact QA; PageRecall says "stop choosing, show the page" |
| **Agents / Auto-research** | Resource-governed research | PrimeScientist (budget-driven MCTS), Agora (Git-DAG shared memory, 62% gap closed), RideWay (efficiency-gated success), BekchiAI (one-click observability) |
| **Generative models** | Diffusion sampling theory | Draft trees + REC coupling: >linear lookahead, up to 8.3% acceleration, exact samples |
| **Sequential modeling** | — | MoRE reuses expert pools across layers with depth embeddings (COLM'26) |
| **Games / multi-agent** | ICL critique + workshop | Statistical-extrapolation interpretation of ICL in strategic games (REE diagnostic); AgentWorld personality-aware agentic-IR tests |
| **Code execution** | Compilers as agent targets | CompileRover (VM optimization tri-role), ScienceIDE (scientific-code environments → 72B agent family) |
| **Benchmarks** | Cost/audit-aware | StableEval Arena (cost-aware, protocol-vs-financial gap), MUSE (artistic multimodal), NLEquiv-150 (formal equivalence of rewrite), RideWay (efficiency utility) |

> ⚠️ **Convergence flag**: §2.4 (rubric artifacts) + §2.7 (PageRecall selection bottleneck) + §9.6 (StableEval protocol-vs-financial gap) + ERPBench (§8.2) all converge on "*evaluation reliability is a property of the selection/state layer, not the model*" — a third/fourth reinforcing source behind the 09-16 fact-grounding / judge-trust theme. (multiple-source convergence, worth a [[claims]]-style page if a benchmark paper formalizes it.)

> ⚠️ **Cross-window note**: several featured IDs (2608.01731 MODE, 2606.10375 SIDInspector, 2608.24076 AgentWorld, 2608.30462, 2609.00237/00728/02942) sit in *earlier* arXiv windows but were verified **0 hits** in wiki/ before inclusion (previously uncovered venue-tagged papers, not part of any sibling claim).

---

## References

- RecSys 2026 contributions: https://recsys.acm.org/recsys26/contributions
- EMNLP 2026 program (accepted main papers): https://2026.emnlp.org/program/main_papers
- NeurIPS 2026 timeline: https://neurips.cc/Conferences/2026/
- COLM 2026: https://colmweb.org/
- Prior full edition: [[conference-digest 2026-09-11|wiki/synthesis/2026-09-11/conference-digest.md]] · Prior incremental: [[conference-digest 2026-09-16|wiki/synthesis/2026-09-16/conference-digest.md]]
- Same-day sibling (dedup source): [[arxiv-ai-search 2026-09-17|wiki/synthesis/2026-09-17/arxiv-ai-search.md]]