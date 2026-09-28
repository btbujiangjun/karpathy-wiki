---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-09-28
updated: 2026-09-28
sources: [arxiv.org]
tags: [arxiv, AI, LLM, recommendation, advertising, sequential-modeling, CTR, retrieval, RAG, GraphRAG, late-interaction-retrieval, oblique-queries, dense-retrieval, game-theory, voting, mechanism-design, post-training, on-policy-distillation, GRPO, hallucination, agent-memory, context-compression, inference-efficiency, structured-sparsity, evaluation-validity, safety, continual-learning, routing, cost-control, second-pass, remainder-sweep, daily-digest]
---

# arXiv AI Research Paper Search Report — 2026-09-28

Generated: 2026-09-28 (Monday). **⚠️ Window-stall disclosure: the arXiv new-submission window has NOT advanced since the 2026-09-25 reports.** This run is a **second-pass deep-dive on the unclaimed remainder** of the Friday 25 Sep 2026 mailing, not a fresh window.

**Why the window stalled** (two independent confirmations, both at fetch time today):
1. All 8 category `/list/{cat}/new` pages still carry the header `Showing new listings for Friday, 25 September 2026`.
2. The arXiv **API tail sweep** (`sortBy=submittedDate&sortOrder=descending`, cs.LG) returns a global maximum ID of **2609.30258**, `published=2026-09-24T17:59:18Z` — i.e. no paper anywhere in the API is newer than the Fri-25 batch.

Today is **Monday 2026-09-28**; arXiv posts the Monday announcement at ~20:00 ET / ~17:00 PT, after this run's execution. The next genuine window will appear on the **2026-09-29** run.

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

**Sibling-job handoff**: treat all 22 IDs above as claimed by this report. The next `arxiv-ai-search` / `arxiv-daily` / `arxiv-paper-check` run should target the **2026-09-29 window** (the first genuinely new mailing), not this remainder.
