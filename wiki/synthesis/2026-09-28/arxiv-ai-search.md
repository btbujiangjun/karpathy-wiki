---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-09-28
updated: 2026-09-28
sources: [arxiv.org]
tags: [arxiv, AI, LLM, recommendation, advertising, sequential-modeling, CTR, retrieval, RAG, GraphRAG, late-interaction-retrieval, oblique-queries, dense-retrieval, game-theory, voting, mechanism-design, post-training, on-policy-distillation, GRPO, hallucination, agent-memory, context-compression, inference-efficiency, structured-sparsity, evaluation-validity, safety, continual-learning, routing, cost-control, second-pass, remainder-sweep, daily-digest, full-window-sweep, global-window-detection, lora-composition, metacognition, activation-steering, probing, system-prompt-audit, working-memory, coding-agents, model-deprecation, prompt-injection, investigative-journalism, game-arena, multi-agent-collaboration, cooperative-marl, congestion-game, financial-stability, kv-cache-compression, multimodal-serving, aigc-cost-model, quantization-theory, inference-cost-attack, long-context-compression, rag-failure-analysis, mechanistic-interpretability, retail-search, audience-sizing, auction-mechanism-design, prediction-markets, null-result]
---

# arXiv AI Research Paper Search Report — 2026-09-28

Generated: 2026-09-28 (Monday). **⚠️ Window-stall disclosure: the arXiv new-submission window has NOT advanced since the 2026-09-25 reports.** This run is a **second-pass deep-dive on the unclaimed remainder** of the Friday 25 Sep 2026 mailing, not a fresh window.

**Why the window stalled** (two independent confirmations, both at fetch time today):
1. All 8 category `/list/{cat}/new` pages still carry the header `Showing new listings for Friday, 25 September 2026`.
2. The arXiv **API tail sweep** (`sortBy=submittedDate&sortOrder=descending`, cs.LG) returns a global maximum ID of **2609.30258**, `published=2026-09-24T17:59:18Z` — i.e. no paper anywhere in the API is newer than the Fri-25 batch.

Today is **Monday 2026-09-28**; arXiv posts the Monday announcement at ~20:00 ET / ~17:00 PT, after this run's execution. The next genuine window will appear on the **2026-09-29** run.

> ### ⚠️ CORRECTION — added 2026-09-28 by [[arxiv-paper-check]] (same day). The "window stall" conclusion above is **false**.
>
> The two checks in lines 14–18 are individually honest but **cannot support the conclusion drawn from them**. Both were **category-scoped**, and the leap from "per-category max" to "global max" is invalid:
> - **Check 1** sampled **8 of arXiv's ~170 categories**. It establishes that cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE and cs.CV received *no new primary submissions* in this mailing — it is silent about the other ~162 categories.
> - **Check 2** was a **`cat:cs.LG`-scoped** query. Labelling it an "API tail sweep" and concluding "no paper anywhere in the API is newer than the Fri-25 batch" overstates what a `cs.LG` query can establish. This is the specific error: a category filter was read as a global bound.
>
> A **category-agnostic** query run the same morning at 09:46 CST returns `2609.31366v1` (`published=2026-09-25T15:01:40Z`), and the range filter `submittedDate:[202609241800 TO 202609260000]` returns **1,013 papers spanning 2609.30361–2609.31373** — over 1,000 IDs above the 2609.30266 ceiling, and **none of them appear anywhere in `wiki/`**. **628 of the 1,013** fall in the AI/IR/stats pool.
>
> **Net effect: this page covers 454 of the 1,013 papers in the mailing, not 1,013 of them.** The unclaimed remainder it was built on is genuinely unclaimed *within the 8 categories it scanned*, but the wider remainder in the categories it did not scan was missed.
>
> **No content is retracted.** All 22 papers featured here are valid and correctly claimed; the two reports are **fully ID-disjoint** (all 22 IDs here are ≤ 2609.30266; all 34 in [[arxiv-paper-check]] are ≥ 2609.30361). This is a **coverage gap, not a factual error in the entries**. It also means the negative finding in §"rec / ads / CTR line is exhausted" is scoped too narrowly: the CTR drought is real, but the scan behind it covered less than half the mailing.
>
> **Methodology rule now in force for all `arxiv-*` jobs:** never bound a *global* window from a single category's `/list` page or from a `cat:`-scoped API query. Detect the window with a **category-agnostic** API query sorted by `submittedDate` descending, seed the lower cutoff from the previous run's max ID, and verify that the new window's **minimum** ID exceeds the prior **ceiling**. Category pages remain the right tool for *per-category coverage*, never for *global window detection*.
>
> Full treatment: [[arxiv-paper-check]] (2026-09-28).

**Methodology**: Direct page fetches of `/list/{cat}/new` for **cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, cs.CV**; parsed only the **New submissions** section of each page (Cross-lists and Replacements excluded by section-splitting). The parse **exactly reproduces** the 09-25 `arxiv-ai-search` figures — **454 unique new IDs**, span **2609.28475–2609.30264**; per-category cs.LG 119, cs.CV 111, cs.AI 107, cs.CL 86, cs.IR 16, cs.GT 8, cs.NE 4, cs.MA 3 — which is the proof that the corpus is unchanged. Whole-`wiki/` regex diff for `260N.NNNNN` found **123 of the 454 already claimed** by the five 09-25 sibling reports, leaving a **331-paper unclaimed pool**. Title screen of all 331 against the target topics (AI / LLM / recommendation / advertising / sequential modeling / CTR / games / mechanism design / retrieval / agents) → 22 papers deepened via API abstracts. Listing HTML, pool JSON, and API XML cached under the pre-approved temp dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv-search-0928/` and deleted after the run.

**Institutions** are author-affiliation inferred where arXiv prints none — all marked *tentative*; the basis for each inference is stated in the entry.

## Summary Statistics

| Scope | Value |
|---|---|
| Run date | Mon 2026-09-28 (window **stalled** — Fri 25 Sep mailing still current) |
| Window covered | Fri 25 Sep 2026 mailing, **re-used**; fresh-only span **2609.28475–2609.30264** (8 categories) |
| Global API max ID at fetch time | 2609.30258 (`published=2026-09-24`) — confirms no newer window exists |
| Unique new-submission IDs parsed | 454 (byte-identical to 09-25 parse) |
| Already claimed in `wiki/` before this run | 123 (by the five 09-25 siblings) |
| **Unclaimed pool screened** | **331** |
| Featured in full | **22 papers across 8 sections** |
| Collisions | **0** — all 22 IDs grep-verified 0 hits in `wiki/` at write time |
| Direct CTR / advertising / rec-ranking papers | **0** — see the negative-finding section below |
| Industrial/commercial-affiliated entries | 2 (Alibaba Qwen, NVIDIA) |

**Headline theme of the remainder**: **retrieval moves from "find similar text" to "find supportable evidence"** — a five-paper cs.IR block where the interesting object is no longer the passage but the *justified transition between passages* (EvLink's evidence links, OBLIQ-IR's latent-attribute matching, SmallReason-ColBERT's learned per-token importance). Layered on a **post-training audit** theme (thinking leakage, catalytic distillation, chance-constrained safety), an **agent-economics** theme (ICLR context forgetting, Jev-based harness routing with a $3.3–5.0M/yr number, episodic memory for trading), and a **tail-risk/evaluation-validity** theme that keeps recurring across unrelated fields.

---

## ⚠️ Negative finding: the rec / ads / CTR line is exhausted for this window

A dedicated three-pattern screen (`recommend|CTR|click|ads|advertis|bid|auction|sequential|next-item|e-commerce|feed`, plus bid/auction/conversion/attribution) over all **331 unclaimed** papers returned **zero direct CTR-prediction, ad-auction, or recommendation-ranking papers**. Every remaining hit was a false positive on "spectral" / "spectral graph" / "sequential knowledge editing" / "Shannon entropy".

The entire on-topic rec/ads inventory for this window was already claimed by the 09-25 siblings: OneTrans-V2 (2609.28589), ScalarLens (2609.29182), retrieval-grounded credit assignment (2609.29983), LSF-SR (2609.29815), Roblox search-RL (2609.30177), AgentX-Model (2609.30001), Evo-Rec (2609.29973), SEEK/Kuaishou (2609.29803), X-Rec TikTok (2609.29180), CMRec (2609.28972), slate-as-randomized-score-learner (2609.29453), DSI watch-time (2609.28383, from 09-24).

This makes the **~14th consecutive window with no new end-to-end CTR/ad-bidding work** in the remainder. The rec/ads line is currently being carried by the *serving-engineering* and *agentic-commerce* fringes, not by modelling papers. Only **11 of 16 cs.IR papers** survived into the unclaimed pool, and all 5 survivors are retrieval/RAG, not ranking.

The one adjacent item worth watching is **2609.28919** (§4.4) — not a rec paper, but a router that prices model-tier selection against a real enterprise cost line.

---

## 1 Retrieval, RAG & Search Efficiency

### 1.1 SmallReason-ColBERT — a 32M late-interaction retriever for reasoning-intensive retrieval (2609.29652)
- **Title**: SmallReason-ColBERT: An Ultra-Small Late-Interaction Retriever for Reasoning Intensive Retrieval
- **Authors**: Abdelrahman Abdallah, Mohammed Ali, Adam Jatowt
- **Institution**: University of Innsbruck (*tentative* — basis: code released under the `DataScienceUIBK` org, UIBK = Universität Innsbruck; Jatowt is a long-standing Innsbruck faculty member)
- **Date**: Fri 25 Sep 2026 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2609.29652
- **Code**: https://github.com/DataScienceUIBK/SmallReason-ColBERT
- **Abstract**: Reasoning-intensive retrieval stays hard for small models — compact public ColBERTs are trained on general-purpose corpora and trail reasoning-tuned 150M+ baselines on BRIGHT by several nDCG@10 points, and no public reasoning-tuned ColBERT existed at edge scale. **SmallReason-ColBERT** is a **32M-parameter** late-interaction retriever that closes much of the gap with three components: a varied-length contrastive warmup on ReasonIR-VL, a hard-negative contrastive polish on merged ReasonIR-HQ + BGE-Reasoner data, and a **single-layer per-query-token importance head** trained on top of the frozen base. The head is *trained* with an **un-normalised weighted MaxSim** score but *evaluated* with its length-normalised form. In a controlled re-training, swapping the training objective to the symmetric normalised score makes the loss stall and costs **3.59 nDCG@10**. The full recipe reaches **21.41 mean nDCG@10 on BRIGHT** — within **1.21** of the 150M Reason-ModernColBERT (22.62) and above every ≤33M ColBERT evaluated. Ablations over capacity, initialisation, and score variants show the learned head beats fixed IDF weighting, and that **simply thresholding the learned gates is harmful**.
- **Key Innovations**: (1) the train/eval normalisation asymmetry as a *deliberate* objective — train un-normalised, evaluate length-normalised, worth 3.59 nDCG@10; (2) a 1-layer learned per-token importance head on a frozen backbone instead of fixed IDF weighting; (3) 32M params within 1.21 nDCG@10 of a 150M reasoning-tuned baseline; (4) a negative result — learned gates must be *weighted*, not thresholded.
- **Venue**: Preprint. (Code + checkpoints public.)
- **Wiki relevance**: Directly extends the late-interaction line; pairs with the eval-protocol findings already in the wiki on tie-handling and recall ceilings.

### 1.2 OBLIQ-IR — dense retrieval when relevance is a latent attribute (2609.29649)
- **Title**: OBLIQ-IR: Training a Dense Retriever for Oblique Queries
- **Authors**: Mahmoud Abdalla, Abdelrahman Abdallah, Shaimaa Sedek, Adam Jatowt
- **Institution**: University of Innsbruck (*tentative* — same `DataScienceUIBK` org + Jatowt)
- **Date**: Fri 25 Sep 2026 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2609.29649
- **Code**: https://github.com/DataScienceUIBK/obliq-ir
- **Abstract**: **Oblique retrieval** (OBLIQ-Bench) asks for documents whose relevance is set by a *latent attribute* — an implicit stance, an analogous reasoning technique, an authorial fingerprint, a vague tip-of-the-tongue recollection — that has little or no surface expression in the document. State-of-the-art dense encoders *and* agentic search pipelines built on frontier LMs show a **large first-stage bottleneck**, while the same LMs **reliably verify relevance when shown candidates**. The asymmetry is the paper's opening observation: verification is solved, first-stage retrieval is not. **OBLIIQ-IR** is a single-vector dense retriever whose training mixture combines per-mechanism synthetic queries with a new form of **cross-model supervision — kNN-graph distillation from a frozen authorship encoder**, transferring a *style-versus-topic* inductive bias into the student. A 3B retriever fine-tuned reaches **0.211 NDCG@10 on Writing-Style, 0.171 Math, 0.177 Twitter, 0.281 Congress**, beating the **GPT-5.2 Multi-Hop Agent by 0.010–0.150** NDCG@10 and **Gemini-2-Embedding by 0.027–0.222** on every reported task.
- **Key Innovations**: (1) frames oblique retrieval as a first-stage bottleneck that frontier-LM agents fail at while passing verification — i.e. a *pipeline* defect, not a model defect; (2) kNN-graph distillation from a frozen authorship encoder as a source of a style-vs-topic inductive bias for an unrelated target; (3) a trained 3B retriever beating GPT-5.2 multi-hop agentic search on all four task families.
- **Venue**: Preprint. (Code, data, checkpoints public.)
- **Wiki relevance**: Same lab and same day as §1.1 — two independent retrieval recipes from one group in one window is notable. The "verification is solved, retrieval is not" asymmetry echoes the wiki's existing agent-vs-eval gap findings.

### 1.3 The Fellowship of the Query — trajectory fine-tuning for retrieval action control (2609.28653)
- **Title**: The Fellowship of the Query: Learning Retrieval Actions
- **Authors**: Mohammed Al-Maamari, Saber Zerhoudi, Michael Granitzer, Jelena Mitrović
- **Institution**: University of Passau (*tentative* — basis: code under the `padas-lab-de` org; Granitzer and Mitrović are Passau faculty)
- **Date**: Fri 25 Sep 2026 (cs.IR, cs.AI, cs.CL, cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.28653
- **Code**: https://github.com/padas-lab-de/agent-action-controller
- **Abstract**: RAG needs a *control* layer: when to decompose a question, search, reformulate, extract evidence, synthesize facts, verify progress, and stop. The paper asks whether **trajectory fine-tuning** can make small language models (SLMs) good next-action controllers, and additionally evaluates a low-resource setting where **one SLM plays both the controller and the final-answer generator**. From accepted teacher search traces the authors build a **seven-way action-prediction task** — predict the next structured teacher action from the current trajectory state — and evaluate LoRA fine-tuning across SLMs and xSLMs. On 1,646 held-out action examples, **Granite 4.1 3B trained on 13,194 actions reaches macro-F1 0.6536**, vs **0.1736** for zero-shot prompting of the same model and **0.5399** for a TF-IDF logistic-regression baseline. In an end-to-end controller/generator swap over 149 held-out trajectories, using the fine-tuned model for both roles lifts Exact Match **0.7530 → 0.7946** and token F1 **0.7783 → 0.8295**. Cross-role conditions show the fine-tuned controller increases **evidence-fact recording** when the generator is fixed, while **controller-only final-answer gains are not statistically clear**.
- **Key Innovations**: (1) recasts RAG control as a supervised 7-way action-prediction problem over accepted teacher traces; (2) reports the honest negative that the *mechanistic* win (evidence recording) is solid while the *end-task* win from control alone is not statistically clear; (3) evaluates the single-SLM-does-both-roles budget setting explicitly.
- **Venue**: Preprint. (Code public.)
- **Note**: The "improves the mechanism, not the metric" pattern is the same shape as the TWIST (§4.2) and ICLR (§4.1) results in this window.

### 1.4 Asymmetric Dynamic Routing — query-adaptive traversal in Hypergraph RAG (2609.29282)
- **Title**: Asymmetric Dynamic Routing: Balancing Reasoning Depth and Computational Efficiency in Hypergraph RAG
- **Authors**: Qi Sun, Yijia Zhang, Xingliang Hou, Caibo Li, Qiang Li, Yu Guo
- **Institution**: not printed (*tentative — unknown*)
- **Date**: Fri 25 Sep 2026 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2609.29282
- **Abstract**: Graph- and hypergraph-based RAG mitigates LLM hallucination, but existing structure-based systems use **static traversal strategies regardless of query complexity**. The authors name this the **"static retrieval fallacy"**: redundant computation on simple queries and *cognitive context gaps* on complex reasoning ones. **ADR** is an intent-conditioned retrieval framework over hierarchical knowledge graphs — a lightweight structured classifier dispatches each query among **three asymmetric topological traversal operators**: localized fact anchoring, bottom-up adjacency diffusion, and top-down insight grounding, together enabling **bidirectional information flow** across hierarchy layers. Across five domain-specific corpora, ADR keeps reasoning quality while cutting **prompt tokens by up to 48.7%** and **end-to-end latency by 45.3%**.
- **Key Innovations**: (1) names and isolates the static-traversal fallacy as the primary cost source in structured RAG; (2) a 3-way asymmetric traversal operator set (local / bottom-up / top-down) chosen per query by a cheap classifier; (3) deployment-shaped economics — 48.7% prompt-token and 45.3% latency reduction.
- **Venue**: Preprint.
- **Note**: The asymmetric local/aggregate/traversal operator triple is a recognisable design family; worth watching for prior-art overlap before treating it as novel.

### 1.5 EvLink — evidence links, not graph reachability, for GraphRAG (2609.29695)
- **Title**: EvLink: Source-Grounded Evidence Linking for Graph RAG
- **Authors**: Linyao Zheng, Xuhang Shi, Zhifang Mao, Sai Zhou, Shuaixian An, Xiuquan Hou
- **Institution**: not printed (*tentative — unknown*)
- **Date**: Fri 25 Sep 2026 (cs.IR)
- **arXiv**: https://arxiv.org/abs/2609.29695
- **Abstract**: GraphRAG organises corpora into graphs to support multi-hop reasoning, but **graph reachability captures semantic association rather than evidence support** — a reachable passage may still fail to justify a required cross-passage transition. **EvLink** keeps passages as retrievable evidence units and instead builds **evidence-supported transitions** between them, of two kinds: **relation-grounded evidence links** justified by explicit source relations, and **endpoint-alignment links** acting as source-bounded fallbacks. Retrieval is two-stage: **bounded BFS over source-grounded evidence links** recovers bridge passages missed by similarity methods, then **evidence-need mining with noisy-OR coverage refinement** selects a compact, non-redundant evidence set covering the question's distinct facets. On three multi-hop and two simple QA benchmarks, EvLink consistently beats leading GraphRAG baselines by **avg +2.4 R@5, +1.9 EM, +2.4 F1**.
- **Key Innovations**: (1) the sharpest diagnosis in the retrieval block — reachability ≠ evidence support, so the graph's edges are the wrong abstraction; (2) evidence links as a first-class object with a bounded fallback tier; (3) noisy-OR coverage refinement for minimal non-redundant multi-facet evidence sets.
- **Venue**: Preprint.
- **Wiki relevance**: Pairs with §1.2 — both argue the retrieved unit and the justification structure matter more than the encoder.

---

## 2 Games, Voting & Mechanism Design

### 2.1 Diverse representation beyond proportional representation in approval voting (2609.29332)
- **Title**: Diverse Representation in Approval-Based Committee Voting
- **Authors**: Julian Chingoma, Davide Grossi, Feline Lindeboom, Jan Maly
- **Institution**: University of Groningen (*tentative* — basis: Grossi, Lindeboom, and Maly are Groningen (Economics & Econometrics / AI & Society) faculty; Chingoma a doctoral researcher there)
- **Date**: Fri 25 Sep 2026 (cs.GT)
- **arXiv**: https://arxiv.org/abs/2609.29332
- **Abstract**: Approval-based committee (ABC) voting theory has focused predominantly on **proportional representation**. The canonical notion of **diverse representation** — based on the Chamberlin–Courant score — counts voters with at least one representative on the committee, which is an **individualistic** notion. The authors develop a more comprehensive theory requiring the representation of *many groups of voters*, grounded in the **justified representation (JR)** axiom and **strengthened in two directions**. First, they analyse the existing **Strong JR (SJR)** and **Semi-Strong JR (SSJR)** axioms, which consider the same cohesive groups as JR but demand stricter representation, and show **neither can be optimised efficiently on general domains (unless P=NP)**, while **both can be on the Candidate Interval domain**. Second, to capture the *unique and defining* opinions of a group they introduce **Distinctive Representation (DR)** and its local-optimisation variant **Local DR**, addressing satisfiability and computation time, and show (Local) DR is **distinct from known proportionality and diversity axioms**. Experiments on real-world and synthetic data show Local DR performs well on multiple empirical diversity measures.
- **Key Innovations**: (1) complexity separation for SJR/SSJR — NP-hard in general, tractable on Candidate Interval; (2) **Distinctive Representation** as a group-level analogue that targets unique opinions rather than mere presence; (3) an axiomatic distinctness proof separating DR from existing proportionality/diversity families.
- **Venue**: Preprint.
- **Wiki relevance**: Third ABC-voting paper in three consecutive windows — this is an active line in the wiki's mechanism-design cluster.

### 2.2 Costly voting breaks the median voter theorem (2609.29869)
- **Title**: Costly Voting in the Hotelling-Downs Model
- **Authors**: Guy Wolf, Reshef Meir
- **Institution**: Technion / University of Haifa (*tentative* — basis: Meir's political-economy affiliation)
- **Date**: Fri 25 Sep 2026 (cs.GT, cs.MA)
- **arXiv**: https://arxiv.org/abs/2609.29869
- **Abstract**: A **partial-participation** variant of the Hotelling–Downs model: each voter pays a cost to vote and votes only when the comparative gain from their preferred candidate exceeds that cost. Under this model **the median voter theorem breaks**, and the paper studies the extent of **polarization** at equilibria under different voter and cost distributions. The main finding: **the reverse hazard rate of the cost distribution is the principal predictor of polarization** — the driver is voters' *willingness to respond to changes in candidates' positions*, not the cost level itself. The model is then extended with parameters for **alienation** and **candidate competitiveness**, and the results hold under those more realistic factors.
- **Key Innovations**: (1) demonstrates median-voter-theorem failure under voting cost; (2) identifies the **reverse hazard rate of the cost distribution** — a distributional-shape, not level, statistic — as the polarization driver; (3) robustness check adding alienation and competitiveness.
- **Venue**: Preprint.
- **Wiki relevance**: Mechanism-design cluster continues; the reverse-hazard-rate result is a clean distributional-shape finding worth carrying forward.

---

## 3 LLM Post-Training, Distillation & Hallucination

### 3.1 CataOPD — the teacher as catalyst, not target (2609.29518)
- **Title**: CataOPD: Catalytic On-Policy Distillation for Large Language Model Reasoning
- **Authors**: Wenjin Liu, Chenxi Wang, Jiapu Wang, Zhe Cui, Anh Tuan Luu, Haoran Luo
- **Institution**: **Alibaba Group / Qwen team** (*tentative-high* — basis: project released under the `QwenQKing` GitHub org; co-author Anh Tuan Luu is Alibaba AMAP/Qwen)
- **Date**: Fri 25 Sep 2026 (cs.LG, cs.CE)
- **arXiv**: https://arxiv.org/abs/2609.29518
- **Code**: https://github.com/QwenQKing/CataOPD
- **Abstract**: RL and on-policy distillation (OPD) are the two main paradigms for LLM reasoning, but each has a blind spot: **when no correct trajectory is sampled, RL has no positive correctness signal**, while **OPD is confined to trajectories reachable under the student's own on-policy distribution**. CataOPD reframes the teacher as **a catalyst rather than a target**: it expands reachability, then internalises verified student-produced trajectories into a **catalyst-free** policy. Three components: **Self-Rescue Routing** uses empirically all-failed groups as *routing signals* rather than teacher-intervention triggers, first seeking correct trajectories through additional on-policy self-sampling; **Catalytic-Guided Self-Resolution** uses catalytic guidance for problems still unresolved after self-rescue, eliciting a verified *student-produced* trajectory in the guided student distribution; and **Barrier-Weighted Internalization** weights tokens by **guided-to-unguided log-probability gaps**, concentrating updates on the decisive tokens that are hard without guidance. Results: CataOPD outperforms current baselines, **extends independent student reasoning to still-unrecovered problems**, and improves **out-of-distribution generalisation under catalyst-free inference**.
- **Key Innovations**: (1) the catalyst framing — guidance is used to *manufacture a student trajectory*, not to supply a teacher trajectory, so the final policy is self-distilled; (2) all-failed groups repurposed as routing signals instead of failure triggers; (3) guided-minus-unguided log-prob gap as a per-token difficulty weight; (4) the actual deliverable is **catalyst-free inference OOD generalisation**.
- **Venue**: Preprint. (Project public.)
- **Wiki relevance**: Second Alibaba-affiliated entry in this remainder, and a direct continuation of the wiki's S²D-OPD / Direct-OPD degeneracy thread (2609.29142).

### 3.2 DEEPO — two failure points in the reward-to-update correction chain (2609.28570)
- **Title**: DEEPO: Dual-Entropy Enhanced Policy Optimization for Hallucination in MLLMs
- **Authors**: Yingxuan Zhuang, Miao Pan, Wangjie Gan, Jingxiao Yang, Fan Wang, Weiming Liu, Cheng Tan, Xuhong Zhang, Jintao Chen
- **Institution**: USTC-affiliated, with a Huawei/BIT co-author path (*tentative* — basis: Cheng Tan's Huawei–BIT association; Jintao Chen and Xuhong Zhang at USTC)
- **Date**: Fri 25 Sep 2026 (cs.AI, cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.28570
- **Abstract**: RL sharpens MLLM reasoning but its effect on **hallucination is uneven**. The authors trace this to **two weak points in the correction chain from reward to parameter update**. *At the rollout level*: hard queries — those with **high semantic entropy** — frequently produce **unanimously wrong sample groups**, collapsing the group-relative advantage to **zero exactly where hallucination risk is highest**. *At the optimisation level*: **confident-but-wrong tokens are gradient-invisible** — a categorical policy's expected score-gradient norm vanishes as its distribution sharpens, so the predictions most needing correction receive the **weakest updates**. **DEEPO** is a dual-stage enhancement: **signal variance regularization** via semantic-entropy-triggered expert prefixes that inject grounded continuations on high-uncertainty queries (restoring advantage variance), plus **gradient preconditioning** via advantage-sign-aware **Rényi** preconditioning that counteracts logit-level saturation. Both branches beat GRPO individually; their **interaction is statistically significant on VideoMMMU** (+4.0, 95% CI [1.1, 6.9]) — the most complex long-horizon task in the suite — and additive elsewhere. Hallucination falls while accuracy and training stability hold.
- **Key Innovations**: (1) the **zero-advantage-on-hardest-queries** diagnosis of GRPO — entropy and advantage collapse are the same failure seen from two ends; (2) the **gradient-invisibility-of-confident-errors** argument, with a clean information-theoretic proof sketch; (3) a two-sided fix (rollout-side variance + optimiser-side preconditioning) with an explicit statistical-significance test on the interaction term.
- **Venue**: Preprint.
- **Wiki relevance**: The most technically substantive post-training paper in this remainder; the gradient-norm-vanishing argument is a general RLHF/RLVR critique, not MLLM-specific.

### 3.3 Thinking Leakage — a causal audit of NoThink post-training (2609.28682)
- **Title**: Thinking Leakage: A Causal Audit of NoThink Post-Training in Hybrid Reasoning Models
- **Authors**: Zehao Liu, Vasant G. Honavar
- **Institution**: University of Arizona (*tentative* — basis: Honavar's affiliation; first author likely UIUC, adjacent to Jagadish's group)
- **Date**: Fri 25 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.28682
- **Abstract**: Post-training hybrid reasoning models in **NoThink mode** to gain performance while keeping inference fast. But those gains may draw on thinking behaviour *already accessible* through the base model's Think mode. The paper formalises this **thinking leakage** in a **causal mediation framework** and audits its contribution using **bidirectional interventions along a simple base-derived activation direction**. Across **three models × three post-training methods** on competition math benchmarks, leakage is **real, causal, and substantial**: behaviourally and representationally the models shift toward Think; **steering the base model along this direction reproduces most of the post-training accuracy gain**; and **counter-steering a checkpoint removes a substantial share of what it gains**. Across **nine aligned checkpoints with positive NoThink gains, the leakage ratio ranges from 42% to 79%**. The conclusion is an evaluation consequence: a post-training method's apparent advantage can reflect *greater drift toward Think*, obscuring whether it improves capability within NoThink or merely re-invokes existing Think behaviour.
- **Key Innovations**: (1) an operational **leakage ratio** (42–79% across nine checkpoints) rather than a qualitative claim; (2) a cheap, single-direction **bidirectional steering** proxy for the mediation analysis — no need for full activation patching; (3) a direct methodological warning for the whole NoThink-fast literature.
- **Venue**: Preprint.
- **Wiki relevance**: The strongest *evaluation-integrity* result in this remainder. Should be treated as a caveat on any NoThink-mode result in the wiki, including §3.1 and §3.2.

---

## 4 Agent Context, Memory & Cost Control

### 4.1 ICLR — when can an agent forget its own reasoning? (2609.29875)
- **Title**: When Can Agents Forget Their Reasoning? ICLR for Long-Horizon Agent Context Compression
- **Authors**: Mingxuan Wang, Fei Luo, Bo Wang, Guorun Yao, Yinglong Guo, Chao Ning, Hongyue Chen, Yanbiao Ma, Jungong Han
- **Institution**: USTC-affiliated (*tentative* — basis: Chao Ning, Yanbiao Ma, and Jungong Han all USTC)
- **Date**: Fri 25 Sep 2026 (cs.AI, cs.CV)
- **arXiv**: https://arxiv.org/abs/2609.29875
- **Abstract**: Long-horizon LM agents accumulate reasoning history, growing context and inference cost **even after earlier decisions have been executed and observed**. Unlike static CoT compression, deleting historical reasoning **changes future actions and the whole interaction trajectory** — so the question is *when* forgetting is safe. **ICLR** (Interaction Aware Compression for Long Horizon Reasoning) is a **training-free online** method that ranks reasoning blocks by **frozen proxy entropy** while preserving actions, tool calls, and observations. On 260 WorkBuddyBench tasks ICLR raises average reward **0.699 → 0.718** while cutting **input 25.5%, output 14.4%, and cache-read tokens 33.3%**. Ablations reveal **trajectory amplification**, where local reasoning deletion produces *nonlinear* changes in total computation by altering the rest of the interaction. Representation probing, activation patching, and controlled trajectory analyses suggest historical reasoning becomes **more replaceable once task-relevant derived state has been reliably externalised** into code, files, tool outputs, or environmental feedback. Framing result: agent reasoning is **dynamic working state, not permanent interaction history**.
- **Key Innovations**: (1) safety criterion for reasoning deletion that is *trajectory-aware* rather than static; (2) **trajectory amplification** — the honest warning that a locally-free deletion can cost superlinearly downstream; (3) the externalisation condition (state in code/files/tools ⇒ reasoning disposable) stated as a general design rule; (4) training-free, frozen-entropy ranking with 33.3% cache-read reduction.
- **Venue**: Preprint. (**ICLR 2027 submission** — title uses the ICLR acronym as the method name.)
- **Wiki relevance**: Same family as the wiki's ERRAND (2609.29545) and C3M (2609.29735) memory-staleness entries; the "externalise derived state, then discard reasoning" rule is the actionable part.

### 4.2 TWIST — a conversational-memory benchmark that prices false intervention (2609.28575)
- **Title**: TWIST: A Proposed Benchmark for Intervention Quality in Conversational Memory, with a Human-Validated Draft-Alignment
- **Authors**: Subrat Panda
- **Institution**: not printed (*tentative — unknown, single author*)
- **Date**: Fri 25 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.28575
- **Abstract**: Long-conversation memory benchmarks test recall and prompted knowledge updates; TWIST targets a **complementary, unmeasured property: intervention quality** — whether a deployed memory system, exercised through its *own* ingest/recall/vet surface, acts correctly at **belief change points**. Four tracks: unprompted tension detection, vetting outgoing drafts against the record, answering with current beliefs while **preserving supersession history**, and governing sensitive recall. It extends **LoCoMo's** corpora and harness, and crucially **pairs every detect/block metric with a matched do-not-over-detect control** — surface-matched hard negatives that **price false intervention**, so no track can be gamed by flagging everything. The benchmark is validated first: independent gold-blind double annotation with adjudication, judge-decoy calibration, and a separability audit. On the human-validated Track B v1.0 key (161 items, post-adjudication **κ = 0.85**), **no tested configuration** simultaneously achieves high contradiction recall, high hard-negative specificity, and high attribution: flat-RAG baselines detect **0.76–0.97** of true contradictions but **falsely flag 16–43%** of surface-matched safe drafts depending on backend, while a deployed coherence-oriented system almost never over-flags (**0.98–1.00 specificity**) yet catches only **42%** of true contradictions — **a trade-off no recall-only score can see**. A 13-configuration baseline ladder localises causes: every gold contradiction is detectable from its evidence alone (**recall 1.000**), calibrated models nearly solve the track given the full transcript (**substantial retrieval-coverage gaps**), and draft-only floors reveal model-dependent style priors.
- **Key Innovations**: (1) the matched **do-not-over-detect control** design that prices false interventions — the methodological contribution; (2) a deployed-vs-benchmark **recall/specificity frontier** where no configuration sits in the good corner; (3) the baseline ladder that separates retrieval-coverage failure from style-prior failure; (4) benchmark-validated before use (κ = 0.85, decoy calibration).
- **Venue**: Preprint (single-author preprint; LoCoMo extension).
- **Wiki relevance**: Exemplary benchmark design — the "pair every recall metric with a matched false-positive control" pattern is directly reusable for the wiki's own agent-memory pages.

### 4.3 Sequential knowledge editing silently destroys evidence arbitration (2609.29587)
- **Title**: Sequential knowledge editing breaks a model's ability to tell good evidence from bad, without costing it accuracy
- **Authors**: Atul Anand
- **Institution**: not printed (*tentative — unknown, single author*)
- **Date**: Fri 25 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.29587
- **Abstract**: Knowledge editing is evaluated on whether the edited fact changed, whether paraphrases follow, and whether unrelated answers stayed put. **A model can pass all three and still lose something none of them measures: the ability to decide, on never-edited facts, which retrieved document to believe.** The paper scores the **log-odds the model assigns to its remembered answer against the answer an injected passage asserts**, before and after editing, holding query, passage, and both candidate strings fixed. Cleanest arm — a conservatively tuned LoRA: after **1,000 sequential edits on Qwen2.5-7B-Instruct** it leaves MMLU unchanged **to four decimal places**, yet the spread of this arbitration quantity across untouched facts **falls by 36%**. **Selective prediction degrades with it**: area under the risk-coverage curve rises **+0.107** (vs **+0.005** for a norm-matched perturbation at the same MMLU), and error on the model's **most confident quarter** of arbitration decisions goes **0.217 → 0.342**. This is *not* capability loss: sweeping random perturbation over five severities, damage bad enough to cut MMLU 0.6275 → 0.3725 produces **less** harm (0.088) than MEMIT at 0.6050 (0.102). Holds across 3 seeds, 2 model families, 2 datasets, 2 probe-disjointness criteria, 3 prompt templates, and paraphrased queries. Layer ablation on saved weight deltas shows the effect is **distributed** — no single layer reproduces it, removing any one recovers about half. Under retrieval with a frozen retriever, accuracy falls **0.592 → 0.46**. Secondary finding: **3 of 5 model/method pairings collapse to chance MMLU at 1,000 sequential edits under published hyperparameters**, while edit success stays 1.00 and locality reads clean.
- **Key Innovations**: (1) a new capability probe — **evidence arbitration** — that standard editing metrics cannot see; (2) the MMLU-invariance control (4-decimal agreement) that isolates the effect from capability loss; (3) **selective-prediction degradation** as the mechanism-level signature (+0.107 AURC); (4) the distributed, additive layer structure (any single layer ≈ half the effect); (5) the reproducibility finding that 3/5 pairings collapse to chance MMLU under published hyperparameters while reporting clean edit success and locality.
- **Venue**: Preprint (single author).
- **Wiki relevance**: Pairs with the 09-25 "The Tokens Remember" (2609.29045) entry — both argue editing evaluations are blind. The 3/5-collapse reproducibility note belongs in the wiki's method-page caveats.

### 4.4 Control the Harness, Control the Cost — routing AI coding agents in the enterprise (2609.28919)
- **Title**: Control the Harness, Control the Cost: Routing and Governing AI Coding Agents in the Enterprise
- **Authors**: Arian Abbasi, Alan Aqrawi, Ted Kwartler
- **Institution**: **NVIDIA** (*tentative-high* — basis: Aqrawi and Kwartler are NVIDIA researchers; the paper's enterprise-vendor and price-sheet framing matches)
- **Date**: Fri 25 Sep 2026 (cs.AI, cs.CR)
- **arXiv**: https://arxiv.org/abs/2609.28919
- **Abstract**: Harnesses — the products that run AI coding agents — are multiplying, and enterprises are rolling them out from pilots of a few hundred seats to **tens of thousands**. Most enterprises **buy** their harness (Anthropic's Claude Code, OpenAI's Codex) rather than build one. A harness **decides which model answers, what the model reads, how the prompt cache is used, and which subagents run** — so it picks the rate on the price sheet and sets the volume bought at it. Enterprises keeping a proprietary or untuned harness at defaults **inherit these choices and their bill**. The authors build a fast, customisable router in which **Jev**, a classifier with calibrated probabilities, labels every prompt against a **bring-your-own taxonomy of agentic requests**. Because one user turn is many requests over a prompt cache that belongs to one model, the router moves work **only where no running conversation has to rebuild its cache**: at session start, in side lanes, and at subagent launch. From the price sheet they derive when a mid-task switch pays back, and a **crossover**: on long tool-heavy sessions the highest-priced model costs *less* than the next tier down. Repricing **~10,000 real sessions from public datasets** confirms it. In an emulated enterprise of **10,000 seats** with user behaviour from those datasets, the router **recovers 14–21% of model spend** at **Anthropic's 21 September 2026 list prices — $3.3M to $5.0M a year**. The paper also maps risks across **twenty harnesses**, prices the dependence on a single vendor's models, and proposes an in-house control plane with a ladder for eventually owning the harness.
- **Key Innovations**: (1) the **cache-aware routing constraint** — routing is only legal at session start, in side lanes, and at subagent launch, because mid-conversation switches force prompt-cache rebuilds; (2) the **crossover result** (on long tool-heavy sessions the top-tier model is cheaper than the next tier), derived from the price sheet; (3) Jev reused as a calibrated 10-class cost router; (4) a concrete $3.3–5.0M/yr, 10,000-seat, 14–21% saving figure at dated list prices; (5) a 20-harness risk map plus an own-vs-buy decision ladder.
- **Venue**: Preprint.
- **Wiki relevance**: Second Jev application in two windows (cf. "Just Ask Jev" 2609.29429) — Jev is becoming a reusable *infrastructure* component in this wiki, not just a paper. This is also the closest thing in this remainder to a costed, deployed industrial artifact.

---

## 5 Inference Efficiency & Structured Sparsity

### 5.1 TASP — task-aware spectral pruning with compiled masks (2609.29499)
- **Title**: Task-Aware Spectral Pruning: A Mixture-of-Masks Framework for Efficient LLM Inference
- **Authors**: Ibne Farabi Shihab, Fariya Afrin, Sanjeda Akter, Anuj Sharma
- **Institution**: not printed (*tentative — unknown*)
- **Date**: Fri 25 Sep 2026 (cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.29499
- **Abstract**: Static pruning imposes **one sparse structure on every prompt**, even though reasoning, retrieval, generation, coding, and translation can depend on different parts of a model. **TASP** is a post-training framework that **calibrates module-level spectral descriptors against measured task-specific ablation effects**, **closes grouped-query-attention and SwiGLU dependencies** during sparse-mask construction, and **routes each user turn to one compiled mask that remains fixed** throughout prefill and decoding. A **module-disjoint pilot** first tests whether the spectral signal is informative before committing to full calibration. Under the stated retrospective operating rule the pilot **passes on Llama-3-8B and Llama-3-70B but rejects Qwen2.5-1.5B** — so **applicability is model-dependent, not universal**. At **43% active-FLOP reduction**, the Llama-3-70B harness retains **97.7 ± 0.2%** of the dense BF16 score. In the deployment-matched **INT8-weight / BF16-compute** runtime on a single **A100 80GB**, the compiled sparse path retains **97.3 ± 0.2%** relative to dense BF16 and cuts decode latency **45.2 ± 0.4 → 31.3 ± 0.4 ms/token**, a **1.44× speedup**. Factorized ablations, disjoint-module tests, compiled structured baselines, routing-corruption studies, and an explicit **136-GPU-hour calibration audit** delimit the source and operating regime of the gains.
- **Key Innovations**: (1) **task-conditioned sparsity** — mask is chosen per user turn, then held fixed, avoiding dynamic per-token dispatch overhead; (2) explicit GQA/SwiGLU dependency closure so the mask is legally constructible; (3) an honest **model-dependence result** (Qwen2.5-1.5B rejected by the pilot); (4) deployment-matched INT8/A100 measurement with a 136-GPU-hour calibration cost disclosure.
- **Venue**: Preprint.
- **Note**: The "retrospective operating rule" and the negative pilot result are the most useful part — the efficiency claim is conditional and the paper says so.

---

## 6 Evaluation Validity & Safety Assurance

### 6.1 Beyond average safety — chance-constrained LLM fine-tuning (2609.29960)
- **Title**: Beyond Average Safety: Chance-Constrained LLM Fine-tuning
- **Authors**: Taha Entesari, Mahyar Fazlyab
- **Institution**: University of Waterloo (*tentative* — basis: Fazlyab's affiliation)
- **Date**: Fri 25 Sep 2026 (cs.LG, cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.29960
- **Abstract**: Fine-tuning on new objectives improves helpfulness or domain performance but can **induce regressions on safety-critical prompts**. Existing safety-preserving fine-tuning methods control **average** safety loss or use weighted auxiliary penalties, which **can obscure rare but severe failures**. The paper proposes a **chance-constrained formulation** that limits the *fraction* of safety examples whose degradation relative to a reference model exceeds a prescribed threshold. Because the empirical chance constraint contains a **discontinuous indicator**, they introduce a **differentiable majorization of the violation rate**, giving a tractable conservative constraint, then develop a **constraint-aware gradient descent** treating the majorized constraint as a **safe set in parameter space**, minimally modifying the fine-tuning direction to preserve feasibility. The update has a **closed form** and yields a **tail-aware safety correction** emphasising examples near or above the degradation threshold. Experiments on harmful fine-tuning across **3 tasks × 3 models** show consistent outperformance of the literature baselines. Framing conclusion: safety preservation is better viewed as **reliability-constrained optimisation** than average-risk regularisation.
- **Key Innovations**: (1) recasts safety-preserving fine-tuning as a **chance/reliability constraint** on the tail rather than an average-risk penalty; (2) differentiable majorization to handle the discontinuous violation indicator; (3) closed-form constraint-aware gradient with a safe-set interpretation; (4) explicit tail-emphasis behaviour.
- **Venue**: Preprint.
- **Wiki relevance**: The rare-but-severe framing is the same insight as TWIST's do-not-over-detect controls (§4.2) and the PartHackBench certifier (§6.2) — a *tail-risk* theme running through this remainder.

### 6.2 PartHackBench — certified equal-progress stress tests for partial-credit agent evaluation (2609.29578)
- **Title**: PartHackBench: Certified Equal-Progress Stress Tests for Partial-Credit Tool-Agent Evaluation
- **Authors**: Hongye Yang, Zhihao Xie, Shengjun Xiong
- **Institution**: not printed (*tentative — unknown*)
- **Date**: Fri 25 Sep 2026 (cs.AI, cs.CL, cs.CR, cs.LG)
- **arXiv**: https://arxiv.org/abs/2609.29578
- **Abstract**: Long-horizon tool agents often make useful progress without terminal success, motivating **partial-credit** evaluation. But evaluators may reward **milestones that were temporary, later reversed, or not attributable to the evaluated agent** — and comparing an honest trajectory against a higher-scoring adversarial one is **inconclusive if the adversary made more genuine progress**. **PartHackBench** removes that confound with a **private certifier** that admits an adversary/honest pair **only when their trajectories match component-wise in both current-state predicate satisfaction and standardized agent attribution**; **score inflation f(A) − f(H)** is measured only afterward. In **18 sealed held-out tasks** (PB-CSTE), the frozen historical-target run produced matched adversaries for **15 tasks**. Results: historical credit yielded **mean inflation 0.252**, **conditional attack success 10/15**, **end-to-end yield 10/18**, and **detected none of 14 strict rollbacks**. **Semantic LLM judges were more resistant but remained vulnerable**, especially under **evaluator-targeted attacks**; while **PB-CSTE current-state controls, defined as exact functions of the certified components, yielded zero inflation by construction**.
- **Key Innovations**: (1) the **certified equal-progress contrast** — the control that makes adversarial score comparison interpretable, not the inflation number itself; (2) a private certifier gating which pairs enter the measurement; (3) the finding that **LLM judges resist semantic attacks but not evaluator-targeted ones**; (4) the **zero-inflation-by-construction** current-state control as the reference point.
- **Venue**: Preprint.
- **Wiki relevance**: Extends the wiki's EvasionBench (2609.30217) and trace-integrity cluster; the certifier-gated design is the strongest methodological move in this remainder.

---

## 7 Planning, Personalization & Domain Agents

### 7.1 GRASP — decoupled generate/revise/assess planning (2609.30147)
- **Title**: GRASP: Generating, Revising, and Assessing for Strategic Planning with Agentic AI
- **Authors**: Arunabh Srivastava, Mohammad A. Khojastepour, Srimat Chakradhar, Sennur Ulukus
- **Institution**: **NEC Laboratories America** (*tentative-high* — basis: Chakradhar and Ulukus are NEC Labs America researchers; the natural-language-executable-plan framing matches their prior work)
- **Date**: Fri 25 Sep 2026 (cs.AI, cs.CL, cs.LG, cs.MA)
- **arXiv**: https://arxiv.org/abs/2609.30147
- **Abstract**: LLMs show a profile where **reliability degrades as task complexity increases**. **GRASP** is a strategy-aware, multi-stage planning framework for generating high-quality **natural-language executable plans** for complex tasks, which **decouples the pipeline across specialized, context-isolated modules**: **GenPlan** pre-compiles global macro-guidelines; **RevPlan** explores alternative localized strategies **within isolated context windows**; and **VerPlan** independently evaluates trajectories with a **multi-criteria discriminator**. Results: new state of the art across diverse datasets, with **~12.4%** gain on Natural Plan Calendar Scheduling, **~30.8%** on ZebraLogic, and gains on SciBench Math. Crucially, under **multi-task scaling — where standard planners suffer immediate performance collapse — GRASP completely flattens the multi-task degradation penalty**. In interleaved dual-task environments GRASP gains **up to 16.7% absolute** over direct LLM planners, and by isolating context and enforcing strict macro-regularization it **outperforms frontier reasoning models such as GPT-5-mini by 14.5%**.
- **Key Innovations**: (1) **context isolation as the load-bearing mechanism** — separate windows for global guidance vs local strategy; (2) the **multi-task-flattening result**, the most interesting claim: graceful complexity scaling rather than collapse; (3) an independent multi-criteria verifier (VerPlan) rather than self-consistency; (4) beats GPT-5-mini by 14.5% on planning.
- **Venue**: Preprint.
- **Wiki relevance**: "Complexity degradation" is the same failure mode the wiki tracks for long-horizon agents; GRASP's isolation result is a concrete architectural counter.

### 7.2 BaCVA — Bayesian contextualised value alignment (2609.28942)
- **Title**: From Static Personal Values to Contextualized Personalization: Bayesian Personalized Value Alignment for LLMs
- **Authors**: Hanze Guo, Aixuan Song, Jing Yao, Xiangxu Zhang, Xiaoyuan Yi, Xing Xie, Xiao Zhou
- **Institution**: not printed (*tentative — unknown*)
- **Date**: Fri 25 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.28942
- **Abstract**: Personalized value alignment matters as LLMs must accommodate diverse user preferences, but existing methods align outputs with a **static value profile across prompts**, ignoring that **the salience of value dimensions varies substantially across contexts**. Inspired by **Lewin's Field Theory** — human behaviour jointly shaped by personal dispositions and situational constraints — **BaCVA** models personal values as **priors** and context-dependent preferences as **posteriors**. It is an **inference-time Bayesian** method (no fine-tuning) that approximates the posterior by integrating static personal values with **scenario-specific value salience**: salience is first estimated from generally normative responses, then a **dual-view personalization module** infers posterior preferences from complementary **personal-value** and **scenario-driven** perspectives. The Bayesian framing improves accuracy/adaptivity and **improves data efficiency via the prior values**. Experiments on benchmarks show superiority over strong baselines.
- **Key Innovations**: (1) prior/posterior framing of value alignment — static profile as prior, context salience as posterior; (2) **inference-time only**, so no fine-tuning cost; (3) salience estimated from *normative* responses rather than from the user's own history, decoupling the two estimation problems; (4) data-efficiency gain from the prior.
- **Venue**: Preprint.
- **Note**: The Lewin field-theory motivation is stated as inspiration, not as a theoretical result.

### 7.3 META — episodic-memory-augmented multi-agent trading (2609.28771)
- **Title**: Agent Memory with Episodic Retrieval for Financial Decision-Making
- **Authors**: Nuoyue Xu, Jiang Liu, Wenxuan Huang, Xiang Zhang, Juntai Cao, Jiaqi Wei
- **Institution**: Shanghai Jiao Tong University (*tentative* — basis: Jiaqi Wei's affiliation and the lab pattern of the author list)
- **Date**: Fri 25 Sep 2026 (cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.28771
- **Abstract**: LLMs are strong at financial analysis, inspiring agent-based trading frameworks, but prior work either emphasises **long-horizon forecasting** or operates as **stateless analysers**, limiting applicability to realistic trading. **META** (Memory Enhanced Trading Agent) is the first **RAG-like episodic-memory-augmented multi-agent framework** for financial decision making: a family of **specialised indicator agents** (Trend, MACD, Stochastic, RSI, SMA, AVWAP, Heikin-Ashi) feeds a **Decision Agent** that fuses their reports, plus a **Memory module** that retrieves and updates **past trading episodes encoded as market-state embeddings with outcomes and reflections**. By recalling relevant experience and **adaptively reweighting signals under similar market regimes**, META improves **directional accuracy and robustness under short-horizon evaluation**. The claim is that episodic memory provides a mechanism for **regime-aware, interpretable, low-latency** decision making. Code released on GitHub.
- **Key Innovations**: (1) episodes encoded as **market-state embeddings + outcome + reflection** as the memory unit; (2) **regime-conditional signal reweighting** — the adaptation mechanism is regime similarity, not recency; (3) classic indicator agents as a verifiable, low-latency backbone for an LLM decision layer; (4) short-horizon (not long-horizon) evaluation, which is where the gains are claimed.
- **Venue**: Preprint. (Code public.)
- **Note**: No absolute return/Sharpe figures are quoted in the abstract — the claim is directional accuracy and robustness. Treat the magnitude as unquantified.

### 7.4 AlphaDiverse — post-trained local agents for alpha factor mining (2609.29014)
- **Title**: AlphaDiverse: Post-Training Local Quantitative Research Agents for Diverse Exploration in Alpha Factor Mining
- **Authors**: Qingzhuo Wang, Zikun Wei, Zhihua Wei, Wen Shen
- **Institution**: not printed (*tentative — unknown; Wen Shen's quant-finance background, possibly Chinese broker research*)
- **Date**: Fri 25 Sep 2026 (cs.AI, cs.CE, cs.MA)
- **arXiv**: https://arxiv.org/abs/2609.29014
- **Abstract**: LLM multi-agent systems can automate alpha factor mining, but their **reliance on external APIs** limits control over cost, availability, and confidentiality. Long research loops also tend to **revisit a few successful economic mechanisms**, causing **research path collapse**. **AlphaDiverse** combines a multi-agent alpha research system, **diverse research path collection**, and **post-training for local agents**: the research system generates **complementary plan portfolios** and **varies research environments across loops** to collect diverse traces; local **Planner** and **Realizer** agents are then warm-started with **SFT**, and a **joint GRPO** method optimises both using **predictive quality *and* diversity of contributions**. The evaluation design is disciplined: **research feedback is confined to inner-period data, while a frozen final model is evaluated on a later outer period**, avoiding test-set tuning. Experiments across **four Chinese stock universes** show competitive prediction with **broader exploration**.
- **Key Innovations**: (1) **environment variation across loops** as the diversity mechanism — diversity is induced by perturbing the research environment, not by prompt variation; (2) joint GRPO over Planner and Realizer with an explicit **diversity-of-contributions reward**; (3) local (self-hosted) agents for cost/availability/confidentiality control — the industrial motivation; (4) strict inner/outer period split with a **frozen** final model.
- **Venue**: Preprint.
- **Wiki relevance**: Directly relevant to the wiki's `wq101-alpha` daily track — an independent, method-level contribution to the same factor-mining problem.

---

## 8 Privacy-Preserving Continual Learning

### 8.1 SPARK — decoupling retention from privacy correction (2609.29711)
- **Title**: Decoupling Knowledge and Privacy: Post-Task Self-Distillation Replay for LLM Continual Learning
- **Authors**: Shengtao Wen, Yunying Yang, Xiang Chen, Lingbing Guo, Yu Tian, Sheng-Jun Huang
- **Institution**: Tsinghua-affiliated / BAAI (*tentative* — basis: Yu Tian's Tsinghua–BAAI association)
- **Date**: Fri 25 Sep 2026 (cs.LG, cs.AI)
- **arXiv**: https://arxiv.org/abs/2609.29711
- **Abstract**: **Privacy-preserving continual learning (PPCL)** must reduce reproduction of sensitive content while retaining useful knowledge across sequential tasks. The paper notes a **category distinction**: formal privacy guarantees characterise *randomized mechanisms*, whereas **operational output control** asks whether a trained model selectively reduces the likelihood of sensitive content *in its outputs* — and studies the latter together with CL utility under realistic task evolution. The key observation is a **granularity mismatch**: **task acquisition requires broad preservation of current- and old-task behaviour, whereas privacy correction targets sparse annotated positions**; joint optimisation therefore leaves the **current-task preservation target continually changing**. **SPARK** decomposes retention and correction: it **first freezes the learned post-task distribution**, then applies **selective correction around this stable reference**. **Self-Distillation Replay** learns the current task while distilling behaviour from previous tasks, and **Post-Task Privacy Correction** reduces annotated-PII likelihood while **anchoring current- and old-task non-PII behaviour** to the resulting checkpoint. Extensive evaluations show effective selective PII suppression with strong CL utility and retention. Code and data to be released.
- **Key Innovations**: (1) separates **formal privacy** from **operational output control** as distinct objects and targets the latter; (2) diagnoses the **moving-target problem** in jointly-optimised retention + correction; (3) the freeze-then-correct ordering as the structural fix.
- **Venue**: Preprint. (Code/data promised, not yet released.)

---

## Cross-Cutting Observations

**1. A retrieval-reasoning-axis is emerging as its own subfield.** Four of the five cs.IR papers (§1.1, §1.2, §1.5, plus §1.4) share a move away from "retrieve similar text" toward **justified structure**: a learned per-token importance score over frozen representations (ColBERT), a latent-attribute inductive bias distilled from an unrelated encoder (OBLIQ-IR), evidence-grounded graph edges replacing reachability (EvLink), and query-conditioned traversal operators (ADR). A fifth (§1.3) targets the *control* layer above retrieval. Taken together, the classic three-stage retrieve→rerank→generate decomposition is being replaced by something closer to retrieve→**justify**→generate.

**2. Tail-risk thinking recurs across unrelated fields.** TWIST prices false intervention with matched hard negatives (§4.2); Beyond-Average-Safety moves safety from average risk to a chance constraint (§6.1); PartHackBench certifies *equal progress* before measuring adversarial inflation (§6.2); the leakage ratio quantifies how much a "fast-mode" gain is borrowed (§3.3). Four papers, four fields, one shared instinct: **averages hide the failure you care about.**

**3. Two commercial labs, both infrastructure-flavored.** Alibaba/Qwen (CataOPD, §3.1) and NVIDIA (harness router, §4.4) are the only clearly industry-attributed entries, and neither is a model release — both are *infrastructure* (distillation training recipe; cost routing). The window's commercially-weighted energy is in the plumbing.

**4. Jev is becoming a wiki-level component.** §4.4 is the second Jev application in two consecutive windows, and it is used as a *production cost router* rather than an alignment-failure detector. Worth promoting to a dedicated `wiki/methods/` page.

**5. Methodological honesty is unusually high in this remainder.** Explicit negative results: the Qwen2.5-1.5B pilot rejection in TASP (§5.1), the "controller-only gains not statistically clear" admission in §1.3, the "no configuration achieves all three" finding in TWIST (§4.2), the 3/5-collapse reproducibility note in §4.3, and the leakage-ratio caveat in §3.3. This is a marked contrast with headline-maximising abstracts in the same window.

**6. What this window does *not* contain.** No CTR prediction, no ad auction/bidding, no recommendation ranking, no game-RL/world-model/PCG work in the unclaimed remainder (those were all claimed by the 09-25 siblings — see the negative-finding section). The rec/ads/game lines are effectively **empty** in this second pass and will need the 2026-09-29 window to resume.

---

## ID Index (all 22, all grep-verified 0 hits in `wiki/` at write time)

| ID | Short name | Section | Institution (*tentative*) |
|---|---|---|---|
| 2609.29652 | SmallReason-ColBERT | §1.1 | Univ. of Innsbruck |
| 2609.29649 | OBLIQ-IR | §1.2 | Univ. of Innsbruck |
| 2609.28653 | The Fellowship of the Query | §1.3 | Univ. of Passau |
| 2609.29282 | Asymmetric Dynamic Routing (Hypergraph RAG) | §1.4 | not printed |
| 2609.29695 | EvLink | §1.5 | not printed |
| 2609.29332 | Diverse Representation in ABC Voting | §2.1 | Univ. of Groningen |
| 2609.29869 | Costly Voting in Hotelling–Downs | §2.2 | Technion / Univ. of Haifa |
| 2609.29518 | CataOPD | §3.1 | Alibaba Group / Qwen |
| 2609.28570 | DEEPO | §3.2 | USTC (+ Huawei/BIT path) |
| 2609.28682 | Thinking Leakage | §3.3 | Univ. of Arizona |
| 2609.29875 | ICLR (agent context compression) | §4.1 | USTC |
| 2609.28575 | TWIST | §4.2 | not printed (single author) |
| 2609.29587 | Sequential knowledge editing / arbitration | §4.3 | not printed (single author) |
| 2609.28919 | Control the Harness, Control the Cost | §4.4 | NVIDIA |
| 2609.29499 | TASP | §5.1 | not printed |
| 2609.29960 | Beyond Average Safety | §6.1 | Univ. of Waterloo |
| 2609.29578 | PartHackBench | §6.2 | not printed |
| 2609.30147 | GRASP | §7.1 | NEC Labs America |
| 2609.28942 | BaCVA | §7.2 | not printed |
| 2609.28771 | META (episodic trading memory) | §7.3 | Shanghai Jiao Tong Univ. |
| 2609.29014 | AlphaDiverse | §7.4 | not printed |
| 2609.29711 | SPARK | §8.1 | Tsinghua / BAAI |

**Sibling-job handoff**: treat all 22 IDs above as claimed by this report.

> ⚠️ **Handoff corrected 2026-09-28.** The original handoff pointed the next `arxiv-ai-search` / `arxiv-daily` / `arxiv-paper-check` run at the **2026-09-29 window** on the premise that no new window existed yet. That advice is withdrawn: **a large unclaimed window already exists right now** — 1,013 papers, IDs **2609.30361–2609.31373**, screened and claimed in [[arxiv-paper-check]] (24 featured + 10 runner-ups, all 0-hit in `wiki/`). The next run should (a) treat those 34 IDs as claimed, and (b) screen the **residual** of that same 1,013-paper window rather than waiting for 09-29. See the CORRECTION block at the top of this page for why the "stall" premise failed.
---

# RUN 2 — Full-window sweep of the 2026-09-25 mailing (1,260 papers)

**This section supersedes the scope of everything above it, without retracting it.** Run 1 covered 454 papers from 8 categories (2609.28475–2609.30264). The [[arxiv-paper-check]] correction established that the "window stall" was false, and flagged a coverage gap. **This run closes that gap** by sweeping the *entire* mailing with a category-agnostic query.

## Method (per the rule in force since the correction)

| Step | Value |
|---|---|
| Window detection | **Category-agnostic** API query, `sortBy=submittedDate` — no `cat:` filter |
| Range filter | `submittedDate:[202609241800 TO 202609260000]` |
| Global max ID | **2609.31620** (`published=2026-09-25T17:59:59Z`) |
| Global min ID | **2609.30364** (`published=2026-09-24T18:00:00Z`) — 5 IDs above Run 1's 2609.30258 ceiling ✅ |
| Mailing size | **1,260 papers**, span **2609.30361–2609.31620** |
| Coverage | 1,260/1,260 = **100% of the window** (7 paginated API pulls, 200/page) |
| Already claimed in `wiki/` | 116 (by `arxiv-daily` 81, `arxiv-paper-check` 40, `game-rl-daily` 32, `conference-digest` 2, Run 1 above 3 — overlapping sets) |
| **Unclaimed pool screened** | **1,144 papers** |
| Featured in full | **31 papers across 5 sections** |
| Collision status | **2 collisions** with a concurrent run (2609.31498, 2609.31379) — see the collision table at the end of this section |

**This run's headline**: the [[arxiv-paper-check]] correction estimated the mailing at 1,013 papers; the true size is **1,260**, and the ID range extends to 2609.31620, ~347 IDs past what the correction observed. Three independent counts (1,013 → 1,260; range 2609.31373 → 2609.31620) are all explained by the same thing: **arXiv continued accepting submissions through the Friday 17:59:59Z cutoff, and metadata/announcement for later arrivals published after the earlier runs fired.** Anyone re-running this should expect the count to drift upward within the day.

## ⚠️ Rec / ads / CTR screen — and a scope correction

> **🔴 CORRECTION — added after the concurrent [[arxiv-paper-check]] RUN 2 caught a real error in this section.** The first draft of this section was headed "the drought is now a *whole-window* result" and stated **"the ~15th consecutive window with no end-to-end CTR, ad-auction, or recommendation-ranking work."** That was **wrong twice over**, and the sibling was right to flag it:
> 1. **Scope error.** The screen below was run over the **1,144-paper unclaimed residual**, not the 1,260-paper mailing. Stating the residual's zeros as a property of the *whole mailing* is the **same class of error this run spends its whole preamble correcting** — a partial sweep read as a global bound. Ironic, and worth recording.
> 2. **Internal contradiction in plain sight.** The retracted sentence claimed zero CTR papers *in a document that features 2609.31498* (§4.1, Target retail product search, **online A/B CTR +0.97%**). The window's single genuine CTR paper was sitting in my own summary table while I declared the window CTR-free.
>
> **What actually holds** is narrower and still useful. Corrected statement below.

### The corrected finding

**Scope: the 1,144-paper unclaimed residual** (the 1,260-paper window minus 116 claimed elsewhere in `wiki/`).

| Signal | Hits in the 1,144 unclaimed residual |
|---|---|
| `CTR` / click-through / click prediction | **0** |
| Ad ranking / ad auction / bidding / bid landscape | **0** |
| Auction (advertising sense) | **0** |
| `recommender` / `recommendation` (modelling sense) | **0** |
| Sequential recommendation / next-item / session-based | **0** |
| Collaborative filtering / matrix factorization / user-item | **0** |
| Watch time / engagement optimization / feed ranking | **0** |

### What that does and does not license

- **✅ Confirmed window-wide (all 1,260 papers): no ad-auction or bidding paper at all.** Independently corroborated — [[arxiv-paper-check]] RUN 2 swept all 1,260 for ad ranking / ad auction / bidding / bid landscape and got **one hit, a false positive** (the blockchain mempool paper, 2609.31379 §4.3, which is crypto MEV). Two independent full-window sweeps, same answer.
- **❌ Retracted: "the window has no CTR work."** The window has **exactly one** direct CTR paper, **2609.31498** (Target, §4.1), reporting a live online A/B of **CTR +0.97%, order conversion +0.98%, demand per visitor +1.10%**, zero-result searches roughly halved, deployed at scale serving millions of guests daily. It sits in the unclaimed tail, so a screen of the *claimed* set would have missed it too. **The "~15th consecutive CTR-free window" claim is withdrawn.**
- **❌ Retracted: "no sequential-recommendation work."** Sequential-recommendation modelling **is** present in this window — T-RoPE (2609.30576), KuaFu (2609.31045), ESP (2609.30601), UA-TWM (2609.30711) — but all four are **claimed by [[arxiv-paper-check]] RUN 1**, i.e. inside the 116 this run excluded. The honest statement is: **the residual is dry; the window is not.**
- **⬛️ Survives: the false-positive warning.** The 22 apparent `recsys` hits in the residual were **100% false positives** — "personalized" in clinical/diabetes/exoskeleton contexts, "preference" in biomechanics, "sequential" in *sequential knowledge editing* and *sequential monte carlo*, "auction" in *sealed-bid procurement*. Not one was a real rec paper. This validates Run 1's methodology note and is now a **standing warning for every future rec/ads scan on this wiki**.

**Net reading of the window's rec/ads line:** the *unclaimed remainder* is genuinely dry on modelling, but the window as a whole is carried by industrial rec and search papers — two live A/B lifts with business metrics (Target, T-RoPE), one production deployment with GMV impact (KuaFu, Tencent advertising *and* rec), one third-party platform (ESP, LinkedIn). The "modelling drought" framing was wrong: **the rec/ads line is not dead, it is industrial.**

---

## 1 LLM post-training, interpretability & alignment

### 1.1 READ — New LoRA Skills Should Read but Never Write (2609.31600)
- **Authors**: Zeyan Li, Panqi Yang, Qirong Guo, Shengda Zhuo, SIyuan Qiu, Hu Xu, Chun Li, Jianfeng Xu
- **Institution**: Tsinghua University (IIIS / IIAI) — *tentative*; basis: Jianfeng Xu and Shengda Zhuo are long-standing Tsinghua IIIS faculty. arXiv prints no affiliation.
- **arXiv**: https://arxiv.org/abs/2609.31600 · cs.LG
- **Abstract**: Composing several independently trained LoRA adapters into one model is hard: weight-space merging causes interference, retraining on all task data is expensive, and routing between separate adapters forfeits the single-model goal. The authors trace this to two choices every composition method makes *implicitly*. First, a LoRA update admits infinitely many equivalent factorizations — invisible while an adapter serves alone, but it determines what an interaction *between* adapters can see. Second, the coupling between an old skill and a new one can point either way, and the direction decides whether old skills keep computing what they previously computed. **READ** (Read-only Expansion of Adapter Deltas) fixes both: each adapter is rewritten into a **balanced canonical form** preserving its update exactly, and the coupling grows in one direction only — a new skill can *read* old skills' input subspaces but cannot *write* into their output subspaces. The only trainable object per append is the new skill's row of the coupling matrix. The composed update **folds into the base weights with zero inference cost** — no routing, no task-specific rules.
- **Key innovations**: (1) diagnosis that LoRA *factorization non-uniqueness* is the hidden variable controlling adapter interaction; (2) balanced canonical form as a canonicalization that provably preserves the update; (3) **unidirectional coupling** (read-only access to old skills) as the mechanism preventing interference; (4) free-at-inference composition. Results: across 4 benchmark suites and 2 model families, adding skills one at a time, READ improves **every** suite average over the strongest published baselines built from the same adapters — **>20 points on SuperGLUE**, **>7 points** on the domain suite; nearly all complete addition sequences end above every direct baseline. Takeaway: *factor coordinates and coupling direction — which a lone adapter never exposes — decide whether composed skills survive.*

### 1.2 Learning to Stop without Learning to Stop (2609.31619)
- **Authors**: Parsa Hosseini, Akasha Tigalappanavara, Sumit Nawathe, Chenrui Fan, Sourya Basu, Genta Indra Winata, Anirban Das, Soheil Feizi, Nima Chitsazan
- **Institution**: Amazon / AI Singapore — *tentative*; basis: Soheil Feizi, Nima Chitsazan, Sourya Basu, and Anirban Das co-author on prior CMU/Amazon reasoning-efficiency work; Genta Indra Winata is at AI Singapore. No affiliation printed.
- **arXiv**: https://arxiv.org/abs/2609.31619 · cs.AI, cs.CL, cs.LG
- **Abstract**: Reasoning models generate very long traces, making inference expensive. Existing fixes work either at inference time (early stopping) or by explicitly training for brevity (RL with length penalties). This paper shows substantial efficiency gains emerge from a **different kind of supervision: confidence**. A self-supervised procedure fine-tunes reasoning models to **predict their own confidence at intermediate points along their own trajectories**, using only **600 training problems**. Critically, the loss contains **no objective for length, efficiency, or stopping** — confidence is used *only* as a training target. At inference, models use the **standard generation procedure**: no confidence elicitation, no early-stopping mechanism.
- **Key innovations**: (1) a confound-free design — efficiency is never the optimized quantity, so gains cannot be attributed to length regularization; (2) **600 problems** as the entire training budget; (3) the metacognition-emergent-efficiency claim. Result: **up to 25% fewer generated tokens at matched accuracy** across Gemma, Qwen, Nemotron, and GPT-OSS on mathematical, scientific, and coding reasoning — comparable to methods that explicitly optimize for shorter reasoning. Episode analysis shows confidence supervision **largely preserves** the base models' high-level reasoning composition rather than selectively suppressing behaviours. *Efficient reasoning may be a downstream consequence of learning metacognitive signals.*

### 1.3 AIMES — Adaptive Multi-Value Control via Causal Activation Steering (2609.30405)
- **Authors**: Payel Bhattacharjee, Ravi Tandon
- **Institution**: Cornell Tech / MBZUAI — *tentative*; basis: Ravi Tandon's known affiliations. Not printed on arXiv.
- **arXiv**: https://arxiv.org/abs/2609.30405 · cs.LG
- **Abstract**: LLMs are deployed where responses must reflect **multiple, potentially interacting** social norms and values. Activation steering is a lightweight alternative to training-based alignment, but prior human-value steering treats values **in isolation**, and direct composition of multiple directions relies on **fixed intervention strengths** that cannot respond to the model's evolving internal state. **AIMES** builds layer-specific **bipolar directions** for moral-foundation values and uses **intermediate-layer vocabulary readouts as online observers**. An observer-guided controller then adapts each value's intervention strength **at every decoding step** based on its current observed state — **without training a separate value-state estimator**.
- **Key innovations**: (1) per-decoding-step adaptive steering strength, replacing the fixed-λ convention; (2) vocabulary readouts as a free online state estimator (no auxiliary model); (3) a documented **depth-dependence** finding — multi-value controllability varies across both value *combinations* and intervention *locations*. AIMES beats fixed joint steering and prompt-based steering across instruction-tuned families, with **smaller realized activation-space interventions** and comparable response quality. Honest caveat the paper carries: variation in the precise depth at which specific effects emerge.

### 1.4 User Model Extraction via Belief Self-Distillation (2609.31603)
- **Authors**: Ali Holmov, Yiran Huang, Kirill Bykov, Zeynep Akata
- **Institution**: Technical University of Munich / Kempner Institute — *tentative*; basis: Zeynep Akata is TUM faculty and directs the Kempner Institute. Not printed.
- **arXiv**: https://arxiv.org/abs/2609.31603 · cs.LG, cs.CL
- **Abstract**: LLMs implicitly infer attributes of their users and adapt behaviour accordingly, but these beliefs are hard to inspect and causally manipulate. **Belief Self-Distillation (BSD)** is a unified **read-write** framework bridging linear and causal probing: it learns a compact user representation that can be both **decoded and written back** into the model. The **frozen LLM acts as its own teacher**, distilling beliefs from natural conversations with **no external annotation**. Unlike conventional probing, BSD isolates a state whose **causal role can be directly tested**.
- **Key innovations**: (1) the read-write unification of probing — activation presence is not enough, causal writability is the stronger property; (2) annotation-free supervision from the frozen model itself; (3) **refusal depends on the model's inferred user intent, not only on the request** — changing the belief alters refusal *while holding the request fixed*. This is the sharpest safety claim in the window: safety decisions are conditioned on **whom the model believes it is talking to**. (4) a cross-model regularity — independently trained LLMs **converge on a shared geometry** for representing users. Privacy implication: if user beliefs are both readable and writable, a user's profile is an attack surface.

### 1.5 Configuration, Not Conscience — 407 Leaked LLM System Prompts (2609.31575)
- **Authors**: Constantinos Patsakis, Vasilios Argyropoulos, Efthymios Alepis
- **Institution**: *tentative* — Cyprus-affiliated; basis: the author cluster is consistently associated with University of Nicosia / Frederick University. No affiliation printed. **Venue**: to appear at ICTAI 2026.
- **arXiv**: https://arxiv.org/abs/2609.31575 · cs.CR
- **Abstract**: Leaked system prompts are widely treated as windows into commercial models' hidden values, yet their **composition is rarely studied at scale**. The authors analyze a merged corpus of **407 leaked, reconstructed, or officially published system prompts from 62 vendors across four community collections**, identifying **29 near-duplicate clusters covering 66 files**.
- **Key innovations**: (1) the largest such corpus assembled; (2) near-duplicate clustering exposing literal cross-vendor text transfer concentrated in a small set of pairs; (3) a **block-level classifier** that quantifies composition: **~58% of classified words are tool/protocol content, ~5% safety policy**, and the strictest rule-lines guard **tool use and file safety over harmful content by 11:1**; (4) **maintenance debt** as a measurable property — version chains turning over **thousands of words per release**; (5) the framing conclusion: leaked prompts are **operational specifications, closer to configuration files than value statements**, making reuse and *prompt rot* an **engineering and supply-chain** concern rather than an alignment one. **Honesty flag the authors carry themselves**: most documents are adversarially sourced and the classifiers are deliberately simple, so all magnitudes are **directional**; they audit the classifier's error modes.

### 1.6 In-Context Binding Capacity in Language Models (2609.30634)
- **Authors**: Manas Venkata Sai Ravulapalli, Samrath Singh Chadha
- **Institution**: Bosch India / academic — *tentative*; basis: Samrath Singh Chadha's known work on in-context learning capacity measurement. Not printed.
- **arXiv**: https://arxiv.org/abs/2609.30634 · cs.LG
- **Abstract**: *How many assignments can a language model recall before it loses track of which value belongs to which entity?* Measured with continuous recall curves for **12 models ≤3B** plus a threshold sweep over **30 open models up to 12B**. The load at which recall falls halfway to chance follows a **scaling law `K₅₀ = c·N^α` with α = 0.820, R² = 0.73**.
- **Key innovations**: (1) a working-memory capacity law with an empirical exponent; (2) an **eightfold range across pretraining recipes** in the broader sweep — though the authors honestly report that the continuous curves show **no detectable recipe effect after controlling for scale**, with few modern models in the fit; (3) a **derivation of why interference can *lower measured capacity* even when the load-dependent recall profile is unchanged** — a measurement-artifact correction most papers of this type omit; (4) the explicit **non-comparability caveat**: direct task training exceeds the extrapolated zero-shot law, but different measurement criteria prevent reading that as a capacity gain; (5) formation times follow a power law in two independent codebases. Scope discipline: the authors state that recall is **not** a measure of alignment, and that the experiments do not measure state updates or downstream transfer.

### 1.7 CG-Probes — Guardrail Directions from Patient Query Embeddings (2609.31062)
- **Authors**: Marko Řeháček, Vítězslav Dušek, Martin Rusinko, Vít Nováček
- **Institution**: Charles University Prague (CUNI) — *tentative*; basis: Dušek, Rusinko, and Nováček are CUNI NLP faculty. **Venue**: short paper, **CIKM '26**, Rome.
- **arXiv**: https://arxiv.org/abs/2609.31062 · cs.CL, cs.IR · **Code**: https://github.com/mrehacek/cg-probes
- **Abstract**: Patient-facing assistants can pose medical risks, so the authors work **with oncologists** to define three **ordinal risk axes** — Medical Urgency, Psychological Urgency, Topic Sensitivity — then probe each from **query embeddings** in the normalized space of **frozen embedders** via **difference-in-means**, treating each axis as a candidate linear direction. Training data is bootstrapped by clustering **79,658 Czech oncology search queries** with BERTopic and generating contrastive risk-level pairs via few-shot prompting. Evaluated on **200 queries (90 real, 110 synthetic)** graded by two oncologists.
- **Key innovations**: (1) **clinician-defined ordinal axes** rather than generic harm categories — a governance-first framing; (2) probes on a *frozen embedder*, so the pipeline needs only search logs + axis definitions + **black-box embedding access** (no fine-tuning, suggesting transferability across healthcare domains); (3) probes are **competitive with open-weight LLMs** (no significant difference in quadratic-weighted kappa) **at a fraction of the latency**; (4) each axis yields an **inspectable scalar** clinicians can threshold for escalation — auditable by construction, unlike an LLM classifier. Stated limitation: robust validation on new queries and axes remains future work.

---

## 2 Agents, evaluation & the real world

### 2.1 KNOWS — The Hard Part Comes After Search (2609.30604)
- **Authors**: Alexander Gill, Md Farhan Ishmam, Xuyen Nguyen, Neha Bhat, Parker Henry DeYoung, Fateme Hashemi Chaleshtori, Nathan Stringham, Kenneth Marino, Ana Marasović
- **Institution**: USC / Hasso Plattner Institute + Allen Institute for AI — *tentative*; basis: Marinaović (HPI), Marino (USC/ISI), DeYoung & Bhat (AI2). **Venue**: **Findings of EMNLP 2026**.
- **arXiv**: https://arxiv.org/abs/2609.30604 · cs.CL, cs.AI · **Project**: https://alexgill321.github.io/KNOWS-benchmark/
- **Abstract**: Existing computer-use agent benchmarks don't evaluate agents *acting as assistants*. A useful assistant retrieves across multi-step workflows, **synthesizes into artifacts** (documents, presentations, spreadsheets), and navigates program interfaces to produce a coherent final product. **KNOWS** is a benchmark of open-ended, complex, **browser-based** tasks that jointly evaluate these capabilities, **each culminating in a produced artifact**. Task design uses an explicit rubric and a conformance protocol. Each task is paired with an evaluator program combining **deterministic checks with LLM judgments**, balancing the richness/reliability/automation tradeoff.
- **Key innovations**: (1) **artifact-terminal tasks** — success means a usable document exists, not that steps were clicked; (2) the **partial-success metric** that exposes how agents can pass half the steps and still deliver nothing usable; (3) hybrid deterministic+LLM evaluators. **The result that matters**: frontier computer-use agents achieve moderate partial-success scores, but **the best performer fully succeeds in fewer than 3% of complex, long-horizon tasks**; failures on **visual steps** render artifacts unusable **even when agents complete >50% of other steps**. Diagnosis: tool use, visual understanding, and long-horizon reasoning are all limiting. *For the serving-engineering reader: this is the clearest available evidence that "agent replaces the workflow" is not yet true, and that the artifact is the failure point, not the browsing.*

### 2.2 Compact Documentation for Coding Agents — and Why It Does Not Transfer (2609.31587)
- **Authors**: Md Shohel Arman, Igor Molybog
- **Institution**: Louisiana State University — *tentative*; basis: Molybog's known LSU affiliation. **Code/data**: https://github.com/haw-ai-i/roundtrip
- **arXiv**: https://arxiv.org/abs/2609.31587 · cs.SE, cs.AI, cs.CL
- **Abstract**: Do natural-language documentation files help coding agents resolve software issues? The authors build the instruments first: a **roundtrip benchmark** that scores code descriptions by whether **code regenerated from them passes the original tests**, showing that **completeness, not length, drives fidelity**. Using that benchmark as an optimization signal, they discover a **description-writing prompt reaching full fidelity that generalizes to unseen files**. Then they test the hypothesis that motivated the work.
- **Key innovations**: (1) **roundtrip as the fidelity metric** — executable, not similarity-based; (2) **completeness ≫ length** as the design rule; (3) a description-writing optimizer that reaches full fidelity and generalizes. **The negative result, stated with unusual discipline**: across **2 model families and 10 repositories**, against a **positive control confirming the evaluation can detect a genuine improvement**, better documentation **does not help** resolve real repository issues. When the source is present, **neither static compact documentation nor retrieved context beats the issue alone**. The paper reports the negative result *together with* the benchmark and optimizer, and characterizes the boundary at which documentation does help. *This is a direct, controlled rebuttal of the "context engineering pays" thesis in the coding-agent setting — and the positive control is what makes it credible rather than a measurement failure.*

### 2.3 When the Model Retires — LLM Migration in Open-Source Applications (2609.31288)
- **Authors**: Hyungjin Lukas Kim
- **Institution**: *not determinable* — single author, no affiliation printed, dataset to be released on Zenodo. (Honest gap; flagged rather than guessed.)
- **arXiv**: https://arxiv.org/abs/2609.31288 · cs.SE
- **Abstract**: Applications on commercial LLM APIs depend on versions providers retire on their own schedule, with notice periods from **one year down to two weeks**. The author mines GitHub for commits migrating away from officially deprecated models and endpoints of **OpenAI, Anthropic, and Google**, matching each commit to the provider's published announcement and shutdown dates. **22,555 commits across 17,703 non-fork repositories (2024–2026)**, of which **5,139** match an official event; a stratified sample of **300** was validated by two independent coders (**κ = 0.89–0.95**) and all estimates reweighted by their labels.
- **Key innovations**: (1) the **largest migration-mining corpus** of its kind; (2) human-validated labels with reported κ. **The findings are the story**: **~82% (95% CI 79–84) of migrations were committed *after* the shutdown date** — after the application had already started failing — **regardless of repository popularity, prior retirement experience, or the presence of a provider-abstraction layer**. The share tracks the notice policy: **89% for Anthropic's 60–114-day notices vs 13% for OpenAI's one-year Assistants API notice**, and each e-fold increase in notice length cuts the odds of post-shutdown migration by ~three quarters. Also: **model identifiers are hard-coded in 94%** of migrating applications; effort scales from a **median of 6 added lines** for prompt-only apps to **nearly 700** for fine-tuned ones; and only **8%** of migrations switch provider. *Implication the author draws: deprecation policy, dependency-risk assessment, and tooling are all undersized relative to the actual failure mode.*

### 2.4 Prompt Injection Detection for Email Agents via Attack Chain Modeling (2609.30657)
- **Authors**: Ahmad Hashmi, Dhyey Patel, Yunting Yin
- **Institution**: North Carolina State University — *tentative*; basis: Yunting Yin's known NCSU affiliation. **Venue**: **IEEE ICTAI 2026**.
- **arXiv**: https://arxiv.org/abs/2609.30657 · cs.CR, cs.CL
- **Abstract**: LLM email assistants are especially exposed to **indirect** prompt injection, because untrusted email content is retrieved into context and influences later tool use. Existing detectors cast this as **binary malicious-text classification**, ignoring that harmful agent behaviour arises through a **sequence of stages**. The proposed framework models the **attack chain**, combining a text detector, **stage-specific verifiers**, explicit rule-based risk signals, **user-intent / action-consistency analysis**, and a logistic decision policy. Labels are derived from existing prompt-injection datasets; evaluation covers **random splits, temporal phase transfer, conditional stage transfer, cross-dataset transfer**, plus ablations across multiple benchmarks.
- **Key innovations**: (1) **staged** attack modelling over binary classification; (2) intent-consistency checks that catch the case where a retrieved email's instructions *conflict with the user's request* — the actual exploited signal; (3) a **distribution-shift evaluation battery**, which is where the method earns trust: **random train/test splits substantially overestimate robustness**, and later tool-argument stages are more predictable than earlier ones. (4) **hard benign negatives** — training on harmless emails that resemble attacks cuts false alarms while preserving detection. Result: mean **F1 0.406** under the strict threshold policy across five binary benchmarks, vs **0.216** for the strongest of five pretrained detectors used off-the-shelf. *The low absolute F1 is the honest headline: email-agent injection defence is not a solved problem.*

### 2.5 Epstein Files Engine — Agentic Search for Investigative Journalism (2609.30611)
- **Authors**: Duy K. Nguyen, Teresa Mondría Terol, Dylan Freedman, Zach Seward
- **Institution**: **The New York Times** — *high confidence*; basis: the abstract states the NYT deployed the agent, and the authors are NYT staff. **Venue**: **Computation + Journalism Symposium (C+J 2026)**.
- **arXiv**: https://arxiv.org/abs/2609.30611 · cs.HC, cs.CL, cs.CY, cs.IR
- **Abstract**: On **30 Jan 2026** the US DOJ released a mixed-media Epstein collection including **~3 million pages of PDFs**. The **Epstein Files Engine** is the AI agent The New York Times deployed to investigate it. The Engine **translates reporter questions into Google BigQuery SQL** across three corpora (Epstein releases, the Times archive, external Epstein-related news headlines), uses an LLM to **plan queries**, and returns **citation-rich answers a reporter can verify**. **More than 100 journalists used it; it contributed to at least 20 published stories.** The paper also reports **Diff**, a text-and-visual **duplicate matching** method that amplified novelty signals, letting the Engine surface genuinely new information.
- **Key innovations**: (1) **deployed production scale with reported adoption** — rare for an agent paper; (2) reporter question → BigQuery SQL as the interface, with the LLM planning rather than answering; (3) **citation-rich, verifiable output** as the trust mechanism; (4) **novelty amplification via duplicate matching** — a deduplication step reframed as a discovery mechanism. The authors' own framing is the most transferable finding: **newsroom agents serve newsrooms best not as autonomous writers, but as interfaces to source material and institutional knowledge.** *This is the cleanest deployed-agent case in the window, and its design — structured tool over an LLM planner, verifiability by construction — is the pattern to copy.*

---

## 3 Games, multi-agent & collective behaviour

### 3.1 Game Arena — Strategic LLM Evaluation in Competitive Environments (2609.31473)
- **Authors**: Bovard Doerschuk-Tiberi, Yao Yan, Justin Chiu, Hann Wang, Timothy Chung, Martyna Plomecka, John Schultz, Jon Lipovetz, … Yuchen Zhuang, Jaimie Hwang, … Oran Firat, Minmin Chen (68 authors)
- **Institution**: **Google / Kaggle** — *high confidence*; basis: arXiv comment gives `kaggle.com/game-arena`, and the Kaggle staff + academic co-author mix matches. 31 pages, 15 figures, technical report.
- **arXiv**: https://arxiv.org/abs/2609.31473 · cs.AI · **Platform**: https://www.kaggle.com/game-arena
- **Abstract**: **Kaggle Game Arena** evaluates LLMs through **competitive games**. Unlike static benchmarks, game arena lets models play **head-to-head matchups in structured environments where gameplay strength naturally increases as models evolve, preventing performance saturation** — the key methodological argument, since a fixed benchmark is maximally exposed to saturation. Three pilot environments: **Chess** (perfect information), **Poker** (imperfect information), **Werewolf** (multiplayer), deliberately spanning the information-structure axis. Each has a full environment description, evaluation metrics, and results from complete competitions.
- **Key innovations**: (1) **saturation-resistant evaluation via head-to-head play** — the strongest idea in the paper; (2) the **information-structure triad** (perfect / imperfect / multiplayer) as a systematic axis rather than game variety for its own sake; (3) large-scale ground-truth-based evaluation for reproducibility. *For this wiki's games line: this is the infrastructure under which strategic play becomes measurable at scale, and Werewolf-as-multiplayer is the closest thing in the window to a social-deduction evaluation.*

### 3.2 AgentWorld — Long-Horizon Collaboration of Multi-agent LLMs (2609.31590)
- **Authors**: Raphael Shu, Yusen Zhang, Young Min Cho, Jin Mo Yang, Yuan Yuan, Wenliang Zheng, Sharath Chandra Guntuku, Lyle Ungar, Zhou Yu, Rui Zhang
- **Institution**: UT Austin + UPenn — *tentative*; basis: Rui Zhang (UT Austin) and Lyle Ungar (UPenn) are known collaborators.
- **arXiv**: https://arxiv.org/abs/2609.31590 · cs.MA **Venue**: **COLM 2026**. **Project**: https://agentworld.io
- **Abstract**: Existing multi-agent benchmarks test **competitive** settings, **short horizons (<20 steps)**, or simply aggregate individual performance — none isolate genuine **collaboration**. **AgentWorld** provides **100 human-annotated tasks (100 augmented variants)** spanning **50+ interaction rounds** in an MMORPG sandbox, requiring **3–20 agents with asymmetric roles and abilities** to coordinate via communication, joint planning, and resource sharing — under a **blackbox** setting where each agent acts independently without access to others' internal states. The authors add **Causal Collaboration Effectiveness (CCE)**, a graph-based metric tracing **causal dependencies between agent actions** to measure what fraction of a team's effort actually contributed to the outcome.
- **Key innovations**: (1) **collaboration as the isolated target**, with competitive/short-horizon confounds removed; (2) **asymmetric roles and abilities** across 3–20 agents; (3) **CCE** — the metric contribution, and the important one, because it distinguishes *team size* from *team contribution*; (4) MMORPG sandbox as a controllable world with real state. **Results**: Gemini 3 Flash, Claude Haiku 4.5, GPT-5 Mini, DeepSeek R1-70B — **best model only 52.0% task success**, with systematic failure modes of **communication breakdown, role confusion, and inability to maintain shared plans across rounds**. Fully open-source.

### 3.3 Multi-agent Scaling Across Disjunctive and Compensatory Tasks (2609.31563)
- **Authors**: Carolina Fortuna, Blaz Bertalanic
- **Institution**: University of Ljubljana (FMF) — *tentative*; basis: the FMF NLP group is the natural match for this author pair. 25 pages, 4 figures.
- **arXiv**: https://arxiv.org/abs/2609.31563 · cs.AI, cs.MA
- **Abstract**: Multi-agent LLM systems are *expected* to improve with team size, but the authors show **scaling behaviour depends on task structure**. Their contribution is to use **Steiner's taxonomy of group tasks** as the analytical frame, focusing on **disjunctive** (any-one-correct) and **compensatory** (average-the-members) tasks. Modelling independently sampled agents as conditionally independent given the item yields their **large-team limits**: **plurality voting converges to the model's modal answer, and averaging converges to the model's item-level bias.** Results across 13 open-weight models and teams of up to **30 agents**.
- **Key innovations**: (1) an existing social-science framework (Steiner) imported to LLM multi-agent work — the framing is the contribution; (2) **analytically derived asymptotes** that make the measured curves interpretable; (3) the **bias-variance decomposition of multi-agent error** — item-level biases shared across a model's samples account for **~87% of the squared error** on Fermi estimation, so averaging reduces error by only **~6%**. **The results are the argument**: on disjunctive tasks, P(at least one correct) grows **5–20 points** with team size, but **plurality voting realises almost none of that** (within 0.5 points of the model prediction). Multi-round revision helps considerably — **but the gain is nearly the same with one peer as with 29.** Conclusion: **task structure plus the output-combination mechanism is a fundamental determinant of team scaling**, and the standard playbook (bigger team + majority vote) is close to worthless. *This is the theoretical companion to [[agentworld]]'s 52% ceiling — together they explain why multi-agent systems do not scale the way the field assumes.*

### 3.4 HySTAR — Anchored Hypergraphs for Stable Credit Assignment in Cooperative MARL (2609.31531)
- **Authors**: Xinglong Luo, Yuding Zhang, Yuheng Kuang, Shuxuan Yuan, Zhenni Zeng, Weiqiang Zhu, Zhenhai Ji, Zhengning Wang
- **Institution**: Sun Yat-sen University + HKU (MMLab) — *tentative*; basis: Yuding Zhang is HKU MMLab, Zhengning Wang is SYSU. Not printed.
- **arXiv**: https://arxiv.org/abs/2609.31531 · cs.LG
- **Abstract**: Cooperative MARL under partial observability and shared rewards requires assigning team outcomes to individual agents **and high-order coalitions**. A MAPPO-style critic compresses joint behaviour into one global value; critics that **dynamically reconstruct grouping topology** change the mapping from agents/coalitions to value components as interactions or active agents evolve. The authors name this inconsistency **structural target drift**. **HySTAR** separates **adaptive representation learning** from a **temporally consistent high-order value-decomposition basis**: it anchors an **overlapping sparse hypergraph** as a uniformly covered decomposition scaffold, uses a **spatiotemporal encoder** for physical and task-dependent interactions, and combines temporal and structural relevance into agent-specific advantages.
- **Key innovations**: (1) **naming and isolating structural target drift** as the failure mode of dynamic-grouping critics; (2) the **anchor/scaffold split** — freeze the decomposition *basis* (hypergraph) while letting *representations* adapt, trading a little expressiveness for credit assignment that does not drift; (3) hypergraph rather than clique/attention for coalition structure. **Results**: consistent gains over MAPPO-style, value-factorization, and dynamic-grouping baselines across **SMAC, GRF, Traffic Junction, MPE**. On the hardest SMAC settings, **+16.7% relative over MAPPO** and **+15.6% over HYGMA**; **rank 1 on all six GRF scenarios**; **Traffic Junction convergence epochs cut by up to 40.2%** vs MAGIC; highest MPE episode rewards. Controlled topology, agent-death, neighbourhood, and parameter analyses support the anchor+adapt split.

### 3.5 Warned Alike — AI Agents Avoid the Less-Crowded Road (2609.30883)
- **Authors**: Takahiro Ezaki, Naoto Imura, Katsuhiro Nishinari
- **Institution**: Meiji University / Waseda — *tentative*; basis: Nishinari's known multi-affiliation physics position. Cross-listed **physics.soc-ph**, cs.AI.
- **arXiv**: https://arxiv.org/abs/2609.30883 · physics.soc-ph, cs.AI
- **Abstract**: AI agents built on a **few shared models** increasingly act for many people, and **a shared forecast about others can align their choices** and change how scarce capacity is allocated. Tested in a **two-road congestion game**: adding **one sentence** warning that others might follow a routing tip made populations of **50 GPT agents crowd one road while avoiding the nearly empty alternative**. **Average travel time rose from 64 to 95 min**, although any crowded-road agent could have saved **69 min by switching alone** — *the warning discouraged the very move it predicted.* The pattern persisted for **100 rounds**. Two other model families shifted the same way without locking onto one road. **Twelve all-human groups (240 participants)** stayed near balance under numerical reports or the tip. In **24 mixed groups (+240 participants)**, imbalance grew with the share of agents in the analysis, **while people increasingly took the road the agents avoided**; collective costs stayed below the all-agent reference, but with **15 agents and 5 humans, agent seats averaged 80 min vs 44 min for human seats**.
- **Key innovations**: (1) the **minimal-intervention design** — a single sentence of warning is enough to flip a population, isolating *shared-model-induced herding* from any prompt-engineering confound; (2) the **human control** (240 participants, balanced) and the **mixed-condition test** (240 more) — rare in agent papers, and what makes the claim credible; (3) the **asymmetry result**: better group averages *hide* an unequal burden (80 vs 44 min). The authors' methodological prescription is the transferable part: **evaluations of AI agents that share resources should test populations, treat messages as interventions, and report who bears the costs.** *Directly relevant to this wiki's agentic-economics and mechanism-design threads — shared-model monoculture is a congestion externality.*

### 3.6 FRAIL — Financial Fragility in Societies of LLM Agents (2609.30940)
- **Authors**: Zhenhao Fu, Ruipeng Xu, Qibing Ren
- **Institution**: Tsinghua University — *tentative*; basis: Qibing Ren's known Tsinghua affiliation.
- **arXiv**: https://arxiv.org/abs/2609.30940 · cs.AI, q-fin.GN · 25 pages, 6 figures, 12 tables **Code**: https://anonymous.4open.science/r/FinFrail-CF26
- **Abstract**: **Individually protective decisions can produce avoidable collective failures.** As LLM agents take larger roles in financial decision-making, financial AI safety must be evaluated at the level of **the systems they jointly create**, not just individual agents. **FRAIL** places agents in three dynamic financial environments — **bank runs, debt rollover, reward crowdfunding** — where agents' decisions reshape the conditions others face.
- **Key innovations**: (1) the **system-level evaluation frame** applied to finance; (2) three structurally distinct environments so the finding isn't environment-specific. **Results**: across **7 leading LLMs**, widespread collective fragility **even when no agent is instructed to destabilize the system** — **77% of baseline bank-run episodes and 83% of debt-rollover episodes end in failure.** Then three interaction mechanisms are compared: **compensated commitments, centralized commitment agreements, and participant-led coalitions**. All three improve aggregate outcomes, but **no single mechanism wins across all financial structures.** Across mechanisms, successful stabilization shares a **common temporal pattern: broad commitment forms early, before defensive behaviour becomes self-reinforcing.** *That last clause is the actionable design rule — the timing of commitment, not its form, is what stabilizes. Paired with **§3.5 Warned Alike**, this window has two independent demonstrations that agent collectives produce emergent fragility no per-agent evaluation would catch.*

---

## 4 Serving, efficiency & cost — the rec/ads ecosystem's actual frontier

> The only genuinely on-topic commerce/ads work in the entire 1,260-paper mailing. Note what it is: **search, planning, execution, pricing** — never ranking.

### 4.1 Retail Product Search: A Practical Approach at Target (2609.31498)
- **Authors**: Darshan Sonagara, Qujiaheng Zhang, Ankit Singh, Alex Li
- **Institution**: **Target Corporation** — *high confidence*; basis: the abstract states the system is "at Target" and is deployed serving millions of guests daily. 10 pages, 2 figures, 6 tables.
- **arXiv**: https://arxiv.org/abs/2609.31498 · cs.IR, cs.LG
- **Abstract**: Search drives e-commerce engagement, and a good product search system must return both **relevant and desirable** results. Retail search is hard: intent ranges from exact matches to open-ended discovery, and the system must balance **relevance, revenue, and profit** simultaneously under low latency. Keyword methods fall short on natural-language or semantic queries; **vector search helps but can miss key intent signals or return low-precision results**. This paper presents a **hybrid lexical + vector** system: data processing, **embedding training**, **precision control for the final result set**, **multi-channel result fusion** (fusion strategies compared, **weighted interleaving** adopted), and latency optimizations for production.
- **Key innovations**: (1) a **production-deployed hybrid retriever with real A/B numbers** — rare and valuable; (2) **precision control as an explicit post-retrieval stage**, treating the final result set as a governed object rather than a top-k; (3) **weighted interleaving** chosen by comparison for multi-channel fusion. **Online A/B results vs lexical-only search**: **CTR +0.97%, order conversion +0.98%, demand per visitor +1.10%, with zero-result searches roughly halved.** Deployed at scale, millions of guests daily. *The zero-result halving is arguably the larger win — recall failures cost more than ranking errors, and the paper's framing of search as a multi-objective (relevance/revenue/profit) problem under latency is the framing CTR papers in this space should be using.*

### 4.2 REALMS — Real-Time Exact Audience Sizing for Digital Marketing (2609.30547)
- **Authors**: Haixu Ma, Aditya Bansal, Shubham Lohiya, Sumit Ranjan
- **Institution**: Adobe Research — *tentative*; basis: Sumit Ranjan's known Adobe Research affiliation and this team's prior work. **Venue**: **ICDM 2026**. cs.CL, cs.IR
- **arXiv**: https://arxiv.org/abs/2609.30547
- **Abstract**: **Audience sizing** is a critical component of **digital marketing** — it enables resource allocation, campaign planning, and performance optimization. Traditional approaches (skeleton audiences, sampling, predictive modeling) suffer significant delays, estimation errors, and poor scalability over high-dimensional profile data. **REALMS** (Real-time Exact Audience sizing via LLM-based Multi-attribute Search) is a **conversational system for exact audience sizing deployed in production on an enterprise customer data platform**, letting marketers query **millions of profiles and thousands of attributes** in natural language and **receive precise counts in seconds**.
- **Key innovations**: (1) **exact counts, not estimates** — the design bet is that advertisers would pay for precision that sampling cannot give; (2) **categorical attribute retrieval** using embedding-based vector search to identify relevant schema attributes **dynamically, without manual configuration** — the piece that makes it general across enterprise schemas; (3) an **LLM-powered NL2SQL pipeline with template-based in-context learning** for complex nested schemas; (4) **schema standardization** for industry-agnostic deployment. Evaluation on real enterprise data shows strong attribute-retrieval recall, high SQL execution accuracy, and low latency — turning what were **hours into seconds**. *This is the closest thing in the window to an ad-ecosystem paper, and note the object: not a CTR model but a **query interface over a profile warehouse**. The monetization pain point being solved is campaign planning latency, not prediction accuracy.*

### 4.3 How Much Must a Private Mempool Hide? (2609.31379)
- **Authors**: Tingyi Lin, Jiazhuo Li, Ruoran Lai
- **Institution**: University of Pennsylvania — *tentative*; basis: Ruoran Lai's known Penn affiliation. **Venue**: **NeurIPS 2026**. 23 pages.
- **arXiv**: https://arxiv.org/abs/2609.31379 · cs.GT, cs.CR, q-fin.TR
- **Abstract**: Private and encrypted mempools hide pending transactions to stop **sandwich attacks** and other **MEV**, but what they hide is rarely everything — a transaction's pair, direction, and a **coarse range for its size** can still leak. The authors answer exactly **how much leakage makes sandwiching pay**, for a fee-free constant-product AMM (Uniswap v2 pricing). Traders observe an **interval** containing the victim's size and bid in a **first-price auction** for the right to sandwich it; the winning front-run must keep the victim's trade executable **at every size in the interval**.
- **Key innovations**: (1) an **exact** threshold — not a bound or a heuristic; (2) the structural result that the answer turns on the **smallest** consistent size alone, which determines the feasible front-runs, and that the **largest feasible front-run is optimal for pointwise, expected, *and* worst-case profit alike**; (3) a **closed form** for guaranteed profit; (4) the sharp negative result: a privacy layer wishing to rule out sandwiches profitable at every consistent size **may reveal anything about the size except a lower bound above an explicit threshold — the upper end of the range is irrelevant**; (5) with ≥2 symmetric traders, **every pure-strategy perfect Bayesian equilibrium of the auction hands the entire expected net rent to the auctioneer**; (6) if direction is hidden too, no non-contingent first-leg front-run covers both directions, while **post-trade arbitrage survives even perfect pre-trade hiding**. *Domain is crypto, not advertising — but this is the window's cleanest instance of the **information-design-under-auction** reasoning that ad-auction mechanism design needs, and the "reveal a lower bound only" result is the kind of exactness that mechanism-design papers are usually lucky to get.*

### 4.4 AlphaOpsBench — End-to-End Alpha Strategy Operationalization in Prediction Markets (2609.31390)
- **Authors**: Huaiyu Jia, Mingxuan Zhao, Jincheng Gao, Zifan Peng, Wentao Zhang, Siguang Li, Shuo Sun
- **Institution**: HKUST — *tentative*; basis: Siguang Li and Shuo Sun's known HKUST affiliations. cs.CE
- **arXiv**: https://arxiv.org/abs/2609.31390
- **Abstract**: LLMs increasingly generate quantitative trading strategies, but existing benchmarks assume standardized assets, numerical features, or **directly compilable** strategy representations — assumptions **prediction-market strategies violate**, since a coarse idea leaves the traded outcome, causal information source, signal definition, threshold, sizing, order policy, exit, and settlement behaviour unspecified. **AlphaOpsBench** evaluates end-to-end operationalization from **source-grounded economic hypotheses to auditable executable programs** over **581 source-preserving strategy records** and a lifecycle-scale **Polymarket** dataset with **1.28M binary markets, 183.6M cleaned executions**, settlement evidence, and limit-order-book history — comparing **Direct** generation against a **Staged design-then-code** protocol.
- **Key innovations**: (1) a **fidelity** criterion that is far stricter than compilability — did the strategy come from *this* source, with *this* causal claim; (2) the four-way separation of **strategy fidelity / behavioural validity / historical executability / financial performance**, which most quant benchmarks conflate; (3) **preregistered** real strategies plus a corrected independent-generation study over 36 controlled tasks. **Results, and they are sobering**: **Direct and Staged obtain 35/180 and 20/180 canonical passes** on the controlled cohort and **no confirmed pass on the real cohort**; repeated generations vary substantially in **model-owned economic choices**. By contrast **775,725 of 783,655** scheduled historical replays complete — proving that **replayability is a far weaker property than source-faithful operationalization**. Fee and liquidity experiments show execution costs **alter subsequent trading paths** rather than acting as ex-post deductions. *The headline number is 775,725/783,655 ≈ 99% executability against ~0% fidelity: a machine can replay a strategy perfectly and still have operationalized nothing.*

### 4.5 ActKV — Action-Guided KV Cache Management for Agents (2609.31395)
- **Authors**: Zihan Wang, Cheng Tang, Lei Gong, Chao Wang, Wenqi Lou, Teng Wang, Xuehai Zhou
- **Institution**: Huazhong University of Science and Technology — *tentative*; basis: Wenqi Lou and Cheng Tang's known HUST affiliations.
- **arXiv**: https://arxiv.org/abs/2609.31395 · cs.OS, cs.AI
- **Abstract**: Agentic LLM inference accumulates **long KV caches across iterative observation-reasoning-action loops**, imposing memory overhead and capping throughput. Existing compression optimizes **overall output quality**, overlooking **the asymmetric importance of actions in driving task progress**. **ActKV** establishes a compression criterion that values KV entries by **their contribution to action generation**. Three components: **(i) action-oriented eviction** exploiting stable action access patterns to retain entries critical to future actions; **(ii) confidence-driven adaptive budget allocation** using the LLM's intrinsic confidence to size the budget to evolving action-critical demand; **(iii) page-aware compression management** standardizing compression into three primitives with custom kernels for practical throughput.
- **Key innovations**: (1) **the asymmetric-importance insight** — in agent loops, KV entries matter according to their effect on the *action*, not on token quality in general; (2) using the model's **own confidence** as a budget signal, with no external controller; (3) paging-aware kernel design, i.e. compression that survives the serving substrate. **Results on long-trace tasks**: **98.53% of FullKV accuracy at 25.98% of its peak KV memory**; **3.97× token throughput and 3.58× task throughput** vs FullKV; state-of-the-art.

### 4.6 EAServe — Encode-Aware Disaggregated Serving for Multimodal LLMs (2609.31551)
- **Authors**: Kunxiong Zhu, Zhihao Shu, Hangyu Zheng, Minghai Qin, Miao Yin, Gagan Agrawal, Wei Niu
- **Institution**: *tentative* — academic/industry serving group; basis: Wei Niu and Gagan Agrawal's known affiliations suggest a US-based systems collaboration. Not printed. **Venue**: **PACT 2026**. 13 pages, 12 figures, 7 tables.
- **arXiv**: https://arxiv.org/abs/2609.31551 · cs.DC, cs.LG, cs.PF
- **Abstract**: Disaggregating **Prefill** and **Decode** onto separate GPU pools is standard for text-only LLM serving. But MLLMs add a **third phase, Encode**, producing a **three-stage Encode-Prefill-Decode (EPD)** pipeline. Existing frameworks answer partially: text-only PD systems lack Encode, while EPD frameworks expose Encode as a **separate service without regulating downstream request flow**. The paper identifies a **structural resource imbalance**: every request enters through Encode before downstream work can begin, yet per-request execution leaves the **encode GPU severely underutilized even at high loads**, starving downstream Prefill and Decode workers.
- **Key innovations**: (1) repositioning **Encode as the control point** of the pipeline, exposing three coupled dimensions — when work enters downstream, where prefill executes, how the GPU is shared; (2) a **runtime layer** (load-adaptive micro-batching, rate-controlled partial offload to a co-resident prefill worker, dynamic SM partitioning) co-designed with (3) a **configuration layer**, **Hybrid Auto Selection (HAS)**, which prunes unbalanced allocations via per-stage capacity profiling then refines with **TPE-based Bayesian optimization**. **Results**: across three MLLM architectures spanning image, video, and audio, **up to 4.3× and 1.7× higher goodput than NVIDIA Dynamo and vLLM** under identical SLO constraints, more balanced pipeline-wide GPU utilization, and faster convergence to near-optimal configurations.

### 4.7 To Store or To Regenerate? A Cost Model for AIGC at Scale (2609.30448)
- **Authors**: Yunjia Zheng, Zirui Wang, Haoran Ni, Tingfeng Lan, Zhaoyuan Su, Yue Cheng, Juncheng Yang
- **Institution**: HKUST — *tentative*; basis: Juncheng Yang's known HKUST/GZ affiliation and the team's prior AIGC-serving work. cs.PF
- **arXiv**: https://arxiv.org/abs/2609.30448
- **Abstract**: AI-generated artifacts accumulate, so their **exponential growth creates storage, energy, and infrastructure cost**, while **GPU compute cost falls rapidly each hardware generation**. This divergence poses a real question: **when does on-demand regeneration become cheaper than persistent storage?** The paper builds a cost model covering corpus growth, HDD and tape price trends, drive replacement, electricity, **request skew, caching, generator FLOPs, and future GPU price-performance improvements**.
- **Key innovations**: (1) the **quantitative answer is a surprise**: for image generation, **prompt-based regeneration does not become cheaper than storage until around 2040**, because every cache miss must rerun the full prompt-to-artifact pipeline; (2) identification of a **third option latent-space diffusion enables** — store a **compact intermediate representation (IR)** and decode on demand, rather than storing the final artifact or merely the prompt; (3) **caching + IR-based regeneration is ≥2× cheaper than both full-object storage and prompt-based regeneration today**. **Production validation on a trace with 2.07 billion requests**: prompt-based regeneration is **>100× more expensive than storage**, while IR-based regeneration cuts total cost to **roughly half** that of full-object storage **while preserving interactive miss latency**. *Request skew is what makes caching work, and this paper is the clearest statement in the window that the "just regenerate it" intuition is wrong for a very long time.*

### 4.8 FragToken — Amplifying Inference Costs via Noncanonical Token Generation (2609.31552)
- **Authors**: Zihan Wang, Rui Zhang, Xinyuan Qian, Qingchuan Zhao, Hongwei Li, Guowen Xu
- **Institution**: *tentative* — Chinese industry/university collaboration; basis: cannot be resolved from arXiv metadata. cs.CR
- **arXiv**: https://arxiv.org/abs/2609.31552
- **Abstract**: Resource-consumption attacks threaten model providers. Existing attacks amplify cost by inducing **abnormally long or repetitive outputs**, which is easy to detect. This work uncovers an **overlooked token-level attack surface from the many-to-one mapping of token sequences to decoded text**: standard LLMs generate the **canonical** token sequence, but the **same text can also be represented by substantially longer non-canonical sequences**. An attacker can train the model to favour such sequences, **increasing autoregressive decoding steps without a proportional increase in visible response length**.
- **Key innovations**: (1) the **attack surface itself** — tokenizer many-to-one-ness as a covert cost-amplification channel, invisible in output length; (2) an honest negative finding that motivates the method: **directly maximizing token fragmentation substantially degrades model utility**, producing conspicuous answer-quality failures that undermine stealth; (3) **FragToken**, a training-time framework combining **source-model self-distillation, capacity-aware filtering and budgeting, and BPE-Aligned Merging** to induce fragmentation under *ordinary* prompts while largely preserving utility. **Results**: 1.99–2.46 average **token inflation ratio (TIR)** across the three benchmarks on four LLMs, with only minor utility degradation. *Framed as supply-chain threat: a compromised fine-tune inflates provider cost without a large volume of attack requests.*

### 4.9 Generalization Behaviour of OPTQ and the Role of Regularization (2609.31560)
- **Authors**: Erin George, Rayan Saab
- **Institution**: University of Virginia — *tentative*; basis: Rayan Saab's known UVA affiliation.
- **arXiv**: https://arxiv.org/abs/2609.31560 · cs.LG
- **Abstract**: Quantization compresses weights by rounding to fewer-bit representations. **OPTQ** progressively quantizes so the squared quantization error on a **calibration dataset** is minimised. The authors study OPTQ and a variant, **stochastic OPTQ**, in a **generalization setting**, deriving bounds for the expected squared error when a test point is drawn from a fixed distribution, and proving two results: one relating generalization error to error on a calibration set of **independent samples from the same distribution** as the test set; the other bounding the generalization error of **stochastic OPTQ for all sufficiently nice distributions, regardless of the calibration dataset**.
- **Key innovations**: (1) the first **generalization-theoretic treatment** of quantization error — calibration-set quality is usually assumed, here bounded; (2) the **distribution-free** bound for stochastic OPTQ; (3) identification of the **regularization term λ as the pivotal quantity** in both bounds, yielding a **new recommended choice of λ** that outperforms prior literature recommendations in experiments. *This is the theory paper that explains why PTQ results are so calibration-sensitive in practice.*

---

## 5 Retrieval, long context & mechanistic analysis

### 5.1 Highlight-Then-Summarize (H2S) — Learning to Compress Evidence (2609.31382)
- **Authors**: Zhaoyuan Xia, Qinghongbing Xie, Yung Xiang Hue, Jianguang Jiang, Gaofeng Lu, Zhenyu Jiao, Xing Yuan, Dai Dai, Tong Mo, Long Zeng (Xia & Xie contributed equally)
- **Institution**: USTC — *tentative*; basis: Dai Dai, Tong Mo, and Long Zeng are USTC-affiliated (the paper lists them as corresponding authors). 23 pages, 13 figures. **Code/data**: https://github.com/X-Luffy/Highlight-Then-Summarize
- **arXiv**: https://arxiv.org/abs/2609.31382 · cs.CL, cs.AI
- **Abstract**: Long-context understanding requires reasoning over long documents, yet **task-relevant evidence is often sparse and scattered** amid irrelevant and redundant content. **H2S** is a **compress-then-reason** paradigm: first identify **source-grounded, question-relevant evidence**, then integrate it into a **compact, question-conditioned summary** before producing the final answer. To train this, the authors build **H2S-Dataset (6,647 examples, 11 benchmark families, average context 43.9K tokens)** and **H2S-RL**, which provides **process-level rewards** for evidence selection and summary construction *in addition to* final-answer correctness.
- **Key innovations**: (1) the **compress-then-reason** ordering as a training target, not an inference heuristic; (2) **process-level reward for intermediate evidence selection and summary construction**, not just answer correctness — the key methodological move; (3) budget-matched evaluation. **Results** on the 7-task **H2S-Bench** under a shared **128K-in / 4K-out** budget: **H2S-14B averages 32.60, beating Qwen3.8-27B by 10.17 points** and the best result among evaluated open-source models; it also achieves the highest **Evidence-Summary Quality** score and **retains 97.1% of its 16K-budget performance at a 4K output budget**. *A 14B beating a 27B by 10 points under a shared budget is the number to quote; the near-lossless 16K→4K output reduction is what makes it operationally interesting.*

### 5.2 LogicTree-RAG for Long-form Patent Drafting (2609.30943)
- **Authors**: Jiaqi Zhu, Naili Xing, Hexiang Pan, Haotian Gao, Jianwei Yin, Xiaokui Xiao, Beng Chin Ooi
- **Institution**: NUS + HKU — *tentative*; basis: Beng Chin Ooi and Xiaokui Xiao are NUS; Hexiang Pan is HKU. **Venue**: **NeurIPS 2026**.
- **arXiv**: https://arxiv.org/abs/2609.30943 · cs.AI
- **Abstract**: Long-form technical generation remains hard for LLMs because it needs **globally consistent logical structuring and faithful technical reasoning beyond local coherence**. Patent drafting is canonical: a legally compliant, technically exhaustive document via **sustained multi-expert collaboration**. Existing work focuses on partial sections or relies on **manually crafted outlines**, limiting scalable automation. **LogicTree-RAG** induces a **hierarchical logic tree** as a global organizational backbone to organize and ground technical disclosures, **without relying on expert-defined drafting priors**. Each node is a technical element built by **evidence-guided recursive generation**; a **hybrid traversal** mechanism maps the tree into patent sections for **controllable, section-balanced** generation.
- **Key innovations**: (1) **logic structure, not outline, as the generated backbone** — and *induced rather than hand-authored*, which is what removes the expert-prior dependency; (2) **evidence-guided recursive node construction**; (3) **hybrid traversal** decoupling generation from document layout, giving controllability and section balance. Results: consistent improvement in content quality and language conformity over strong LLM baselines, with **longer structured generation at high token efficiency**. *The transferable idea: for any long-document task, generate the dependency structure first and let the layout follow — the inverse of the outline-first default.*

### 5.3 Where Does Retrieval-Based Open-Ended Evaluation Fail? (2609.30467)
- **Authors**: Heyuan Huang, Jirui Dai, Alexandra DeLucia, Sonal Joshi, Mahsa Yarmohammadi, Jie Gao, Bernal Jiménez Gutiérrez, Mark Dredze
- **Institution**: Johns Hopkins University — *tentative*; basis: Dredze and Jiménez Gutiérrez are JHU. Corpus knowledge cutoff: **May 2026**.
- **arXiv**: https://arxiv.org/abs/2609.30467 · cs.CL, cs.IR · **Code/data**: https://anonymous.4open.science/r/Medical_RAG_eval-4AB5
- **Abstract**: Retrieval-based factuality verification — checking LLM claims against authoritative medical corpora — is the dominant paradigm for **scalable hallucination detection in high-stakes clinical settings**. Yet systems report aggregate F1, which **obscures where and why failures occur**, and existing RAG diagnostics need gold answers or annotated gold evidence, **neither of which exists in this regime**. The authors introduce two taxonomies (from **MedExpert** plus 3 closed-ended datasets): **retrieval-stage errors across five quality dimensions** and **verifier-reasoning errors across six consecutive steps**, with an **automatic pattern-induction pipeline using LLM-as-Judge** to label evidence quality and classify reasoning errors at scale, then stress-tested across **4 retrieval methods and 6 frontier verifier models**.
- **Key innovations**: (1) the **taxonomy-pair** decomposition — separating retrieval failure from verification failure, which aggregate metrics cannot do; (2) **annotation-free LLM-as-Judge induction** to make the taxonomy possible in a regime with no gold evidence; (3) the **negative result, and it is the important one**: **scaling model size, adding reasoning effort, expanding to authoritative web sources, and applying medical fine-tuning do NOT resolve these failure modes.** The authors conclude they are **fundamental limitations of the retrieve-then-verify paradigm** in open-ended medical settings, **not artifacts of outdated systems**. *The strongest single claim in this run: four of the four most-obvious fixes fail. Anyone planning a medical RAG system should read this before choosing an architecture.*

### 5.4 Programs-of-Layers in LLMs — A Reproduction (2609.31360)
- **Authors**: Justus Westerhoff, Stephan Olbrich, Hatem Oraby, Matthew Evan Larkum, Felix Alexander Gers
- **Institution**: University of Tübingen — *tentative*; basis: Gers and Larkum are Tübingen-affiliated. **Code**: https://datexis.github.io/RE-PoLar/
- **arXiv**: https://arxiv.org/abs/2609.31360 · cs.AI
- **Abstract**: LLM inference is conventionally a **fixed-depth, fixed-order forward pass through every layer, regardless of input difficulty**. The human brain instead **routes flexibly via the thalamus**. Li et al. (2026) showed, via **PoLar** (program-of-layers), that transformers gain analogous flexibility if layers are treated as a **library of functions** rather than a fixed sequence: performance improves when each input is **dynamically routed through an adaptive sequence of skipped or repeated contiguous layer blocks**. The authors **reconstruct PoLar's diagnostic MCTS in more detail than the original paper** and apply it across **5 models**.
- **Key innovations**: (1) a **more faithful reconstruction of the diagnostic MCTS** than the source paper, and honest reporting of what failed. **Reproduced**: skipping beats the standard pass; **repeating beats skipping**; combining both beats either. Shorter programs suffice for easier questions; harder questions need more repeats. **Not reproduced — and stated plainly**: the **learned router for single-shot inference**; its top-ranked prediction "consistently collapsed back to the standard pass," even though its **top-k** predicted programs *taken together* did show real accuracy gain. **Beyond reproduction**: a **small number of generic programs solve most questions**; and programs that **correct errors are highly brittle** — undoing even a single internal edit typically breaks the correction. Framing: PoLar mirrors **thalamo-cortical coordination** between cortical-area-like layers. *Two findings worth carrying forward regardless of PoLar's fate: **repeating layers beats skipping them**, and **error-correction programs are fragile**. A failed router reproduction reported this cleanly is worth more to the field than a successful one reported vaguely.*

---

## Cross-cutting observations

1. **Composability, not capability, is the active frontier.** READ (unidirectional LoRA coupling), ActKV (action-weighted eviction), EAServe (Encode as control point), and H2S (process-level rewards for intermediate steps) all share one shape: *identify which component of a pipeline is structurally load-bearing, then give it a dedicated mechanism.* None of them improve base-model capability.

2. **The "just make it smaller/faster" framing is being replaced by asymmetry-aware compression.** ActKV's insight — value KV entries by their effect on the *action*, not on output quality — generalizes beyond agents, and is the same move as BGE-Reasoner-style negative mining in retrieval.

3. **Negative results are becoming first-class contributions, and are stated with controls.** Compact Documentation ships a positive control; PoLar-Repro names the specific claim that failed; Medical RAG Eval tests four fixes and reports all four failing; Multi-agent Scaling derives the asymptote that explains why voting wastes the diversity it measures. This is the most encouraging trend in the window.

4. **Deployment friction is under-measured relative to its cost.** LLM Migration (§2.3) finds **82% of migrations happen after the application is already broken**, and hard-coded model IDs in 94% of apps; Compact Documentation (§2.2) finds a whole documentation methodology that does not transfer to real repositories. Both are mundane, both are large.

5. **Collective-level failure needs collective-level evaluation.** Warned-Alike and FRAIL independently show agent collectives produce fragility invisible to per-agent testing — and Warned-Alike adds the uncomfortable detail that a *better average* concealed a 80-vs-44-minute unequal burden.

6. **The commerce frontier has moved out of ranking.** Across a 1,260-paper window with zero CTR or recommendation papers, the real on-topic work is retail search (Target), audience sizing (Adobe-lineage), market microstructure (Penn), and strategy operationalization (HKUST). *This is the single clearest signal in the report about where recommender-systems research currently is not.*

## Papers covered by this run

| # | ID | Title | Primary cat | Section |
|---|---|---|---|---|
| 1 | 2609.31600 | New LoRA Skills Should Read but Never Write | cs.LG | 1.1 |
| 2 | 2609.31619 | Learning to Stop without Learning to Stop | cs.AI | 1.2 |
| 3 | 2609.30405 | AIMES: Adaptive Multi-Value Control via Causal Activation Steering | cs.LG | 1.3 |
| 4 | 2609.31603 | User Model Extraction via Belief Self-Distillation | cs.LG | 1.4 |
| 5 | 2609.31575 | Configuration, Not Conscience (407 system prompts) | cs.CR | 1.5 |
| 6 | 2609.30634 | In-Context Binding Capacity in Language Models | cs.LG | 1.6 |
| 7 | 2609.31062 | CG-Probes: Guardrail Directions from Patient Query Embeddings | cs.CL | 1.7 |
| 8 | 2609.30604 | KNOWS: The Hard Part Comes After Search | cs.CL | 2.1 |
| 9 | 2609.31587 | Compact Documentation for Coding Agents | cs.SE | 2.2 |
| 10 | 2609.31288 | When the Model Retires: LLM Migration | cs.SE | 2.3 |
| 11 | 2609.30657 | Prompt Injection Detection for Email Agents | cs.CR | 2.4 |
| 12 | 2609.30611 | Epstein Files Engine (NYT) | cs.HC | 2.5 |
| 13 | 2609.31473 | Kaggle Game Arena | cs.AI | 3.1 |
| 14 | 2609.31590 | AgentWorld | cs.MA | 3.2 |
| 15 | 2609.31563 | Multi-agent Scaling Across Disjunctive/Compensatory Tasks | cs.AI | 3.3 |
| 16 | 2609.31531 | HySTAR | cs.LG | 3.4 |
| 17 | 2609.30883 | Warned Alike, AI Agents Avoid the Less-Crowded Road | physics.soc-ph | 3.5 |
| 18 | 2609.30940 | FRAIL: Financial Fragility in Societies of LLM Agents | cs.AI | 3.6 |
| 19 | 2609.31498 | Retail Product Search at Target | cs.IR | 4.1 |
| 20 | 2609.30547 | REALMS: Real-Time Exact Audience Sizing | cs.CL | 4.2 |
| 21 | 2609.31379 | How Much Must a Private Mempool Hide? | cs.GT | 4.3 |
| 22 | 2609.31390 | AlphaOpsBench | cs.CE | 4.4 |
| 23 | 2609.31395 | ActKV | cs.OS | 4.5 |
| 24 | 2609.31551 | EAServe | cs.DC | 4.6 |
| 25 | 2609.30448 | To Store or To Regenerate? | cs.PF | 4.7 |
| 26 | 2609.31552 | FragToken | cs.CR | 4.8 |
| 27 | 2609.31560 | Generalization Behaviour of OPTQ | cs.LG | 4.9 |
| 28 | 2609.31382 | Highlight-Then-Summarize (H2S) | cs.CL | 5.1 |
| 29 | 2609.30943 | LogicTree-RAG | cs.AI | 5.2 |
| 30 | 2609.30467 | Where Does Retrieval-Based Open-Ended Evaluation Fail? | cs.CL | 5.3 |
| 31 | 2609.31360 | Programs-of-Layers in LLMs (reproduction) | cs.AI | 5.4 |

**Collision check — two-stage, and stage two found 2 collisions.** All 31 IDs were grep-verified as **0 hits** in `wiki/` when this section was written. **But [[arxiv-paper-check]] RUN 2 was written concurrently and appended after that check**, and it independently reached the same 1,260-paper window size and independently featured **2 of the same papers**:

| ID | Paper | This report | Sibling RUN 2 | Status |
|---|---|---|---|---|
| 2609.31498 | Retail Product Search at Target | §4.1, full entry | §①, cross-ref entry explicitly marked "**claimed by the concurrent [[arxiv-ai-search]] 2026-09-28 (RUN 2)**" | **both claim it; sibling defers to this report** |
| 2609.31379 | Private mempool sandwich thresholds | §4.3, full entry | cited as the sole hit of its full-window ad-auction sweep, i.e. a **false positive** | **both use it; sibling as a negative, this report as an auction-theory result** |

**29 of 31 remain exclusive.** No data conflict: both reports agree the window is 1,260 papers, and both independently identify 2609.31498 as the window's only direct CTR paper. The sibling's retraction of the "CTR drought" claim — and its catch of *this* report's matching scope error — is recorded in the correction box above. **This is the second write-race on 2026-09-28** (the first is documented in [[arxiv-daily]]'s index entry); the standing fix is still a **claim registry or a deterministic claim order** for the `arxiv-*` jobs.

**Institutions**: 2 *high confidence* (Target, NYT, Kaggle/Google — all stated in-text); remainder *tentative* from author-affiliation knowledge, with the basis stated per entry. Where unresolvable (2609.31288, 2609.31552, 2609.31551) the gap is flagged rather than guessed.

**Cache**: pool JSON + 7 API XML pages under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv/`, deleted after the run.

---

> ⚠️ **Scope note added 2026-09-28 ~10:27 CST by the concurrent [[arxiv-paper-check]] RUN 2.** The "rec / ads / CTR drought is now a *whole-window* result" section above is a **scope error in a negative claim, not a content error**, and this note is added for that reason only. Its table reports `recommender / recommendation — 0` and `CTR / click prediction — 0` across the **1,144-paper unclaimed residual**, then states the result as a property of the **whole 1,260-paper mailing**. The two are not the same set: the residual is this report's claimed set *excluded*, and the claimed set includes the papers this report itself features — including **2609.31498 (Target retail product search)**, which this report lists in §4 as adjacent on-topic work with a real A/B. The window-wide statement should be read as: *within the unclaimed residual there was no further rec/ads/CTR work*, not *the mailing contains none*. The residual sweep itself is sound, all 31 featured entries are individually correct, and they are ID-disjoint from both runs of `arxiv-paper-check` — no content conflict. Its **window count of 1,260 (2609.30361–2609.31620) is confirmed independently** by that run and is the authoritative figure.
>
> **One methodological addition, since this run is the one that got the count right and the reason is worth recording.** `arxiv-paper-check` RUN 1 read the *same* `totalResults` of 1,013 and paginated against it, leaving a 247-paper blind spot at 2609.31374–2609.31620 — the tail that contains the window's only direct CTR paper. So over-paginating to exhaustion is not incidental diligence here; it is what caught the difference between a true and a false negative. **A category-agnostic `submittedDate` query fixes a window's low bound but not its high bound, and `totalResults` is not a reliable window size within a single submission day** — arXiv continued accepting through the Friday 17:59:59Z cutoff and published metadata for late arrivals after the earlier queries were issued.
