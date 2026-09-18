---
title: "arXiv Daily — AI / LLM / Recommendation / Advertising / CTR / Sequential Modeling / Games"
type: synthesis
created: 2026-09-18
updated: 2026-09-18
sources: [arxiv.org]
tags: [arxiv-daily, AI, LLM, recommendation, advertising, CTR, e-commerce, ranking, generative-recommendation, sequential-modeling, linear-RNN, MoE, routing, KV-cache, serving, speculative-decoding, tabular-FM, training-stability, safety, model-collapse, agents, memory, agent-governance, LLM-as-judge, RAG, retrieval, IR, world-models, RL, market-making, daily-digest]
---

# arXiv Daily Report — 2026-09-18

> **Mailing status**: No fresh Friday mailing at run time — every `/list/{cat}/new` page still announces "Thursday, 17 September 2026" (the Fri 18 Sep batch posts tonight ~20:00 ET). Today's report therefore mines the **unclaimed remainder** of the Thu-17 window, exactly as the 09-16 report treated the prior window.
> **Methodology**: Parsed `/list/{cat}/new` for cs.IR / cs.LG / cs.AI / cs.CL / cs.GT / cs.MA / cs.NE (495 unique IDs total, all inside the Thu-17 window, IDs **2609.17532–2609.19145** — the same window covered by the 09-17 sibling reports). Subtracted the entire 3,893-ID wiki coverage set *plus* all 91 IDs cited by the 09-17 siblings (arxiv-ai-search / conference-digest / game-rl-daily), leaving **363 unclaimed candidates**; screened titles inlined in the listing, then fetched 39 `abs/{id}` pages for the shortlist and featured **31 papers** — every featured ID grep-verified **0 hits in `wiki/`** at write time. The arXiv API remained rate-limited, so direct page fetch was used; probe HTML was cached under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/` and cleaned up after.
> **CTR/ads note**: The direct-CTR-content drought continues — this is the fifth consecutive window with ≈0 classic end-to-end CTR/pCVR ML papers flowing through the daily arXiv feed. But the still-fertile **recommendation/e-commerce periphery** produced a strong crop this time: **Behavior2Value** (consumer *value* measurement from Taobao logs, a distinct signal from interest), **Too Good to Be Real** (AI "logic overbinding" vs real engagement), and an **AI-referral audit** of local service markets (doctors/advisers). All are rec-adjacent, value/eval-layer work rather than CTR-model work.

---

## 1. Recommendation, E-commerce & Value Modeling

### 1.1 Behavior2Value: Benchmarking and Empowering LLMs for Consumer Value Measurement from E-commerce Behaviors

| Field | Detail |
|-------|--------|
| **Authors** | Peixuan Hou, Bin Chen, Li He, Jian Xu, Bo Zheng, Xiuli Ma, Guojie Song |
| **Institution** | Alibaba (inferred; Jian Xu / Bo Zheng) + academia |
| **Published** | 16 Sep 2026 (cs.IR) |
| **Abstract** | Human values are deep motivational orientations that shape behavior; in e-commerce they reveal the stable drivers behind purchase decisions, explaining how users evaluate products *before* purchase better than short-term interests. But consumer values are implicit in complex, fragmented behavioral trajectories. **B2V** casts value identification as a task over e-commerce behavioral episodes; the paper builds the **ECVT taxonomy**, introduces **B2V-Bench** (first B2V dataset, from anonymized **Taobao** behavioral logs: real purchase-decision episodes, 25 purchase-behavior types, corresponding value orientations per episode), and presents **B2V-Verifier**, a behavior→value measurement model based on *Value Verification* reasoning. |
| **Key Innovations** | (1) Names "consumer value" as a *stable* signal orthogonal to short-term interest — measured from behavior, not surveys; (2) first public-ish standard benchmark (ECVT + B2V-Bench) on real Taobao logs; (3) value-verification inference procedure for LLM measurement. |
| **Link** | [arXiv:2609.18203](https://arxiv.org/abs/2609.18203) |

### 1.2 Too Good to Be Real? Diagnosing and Reducing the Gap Between AI Preference and Real User Engagement

| Field | Detail |
|-------|--------|
| **Authors** | Xinglang Zhang, Yuanmeng Xiang, Yunyao Zhang, Zeliang Chen, Junqing Yu, Zikai Song |
| **Institution** | (inferred academic) |
| **Published** | 16 Sep 2026 (cs.CL) |
| **Abstract** | LLMs now generate and evaluate online content, but do the qualities they associate with engagement match what real users reward? Study on **1.17M answers to 25,978 questions** from Zhihu / Quora / Reddit, comparing real vs AI-generated answers across engagement levels. Introduces **Ontological Preference Measurement** (logic / affect / expression dimensions) and finds a systematic gap: as target engagement rises, LLMs add *more explicit logical structure* while real engagement tracks affective/expressive salience — **"logic overbinding."** Fix: **OMRA** (Ontology-Masked Reasoning Autoencoding) masks/reconstructs over-explained spans while preserving stance/facts/coherence; across four LLM families it reduces the measured gap substantially. |
| **Key Innovations** | (1) Large-scale (1.17M) diagnosis that AI's engagement model is structurally wrong (logic-obsessed, affect-blind); (2) a three-axis ontological measurement of "what makes content engaging"; (3) intervention (OMRA) that edits outputs to close the gap while preserving factual content. |
| **Link** | [arXiv:2609.18282](https://arxiv.org/abs/2609.18282) |

### 1.3 Understanding AI Provider Recommendations in Local Service Markets

| Field | Detail |
|-------|--------|
| **Authors** | Hazem Ibrahim, Yasir Zaki |
| **Institution** | NYU Abu Dhabi (inferred; Zaki) |
| **Published** | 16 Sep 2026 (cs.CY) |
| **Abstract** | When an AI assistant refers a doctor or financial adviser, the "recommendation" is a high-stakes referral. Audit of **four registry-backed service domains across the 100 largest US metros** (Medicare clinician/facility records, SEC adviser disclosures) under three conditions: open-weight model, proprietary model *without* web search, same model *with* search. Without search both models **largely fabricate** — only **4%** of the open-weight model's doctors and **11%** of the proprietary model's match a clinician in the queried city (matched open-weight cases are name coincidences). With search, 64–71% match real providers — and *who* gets recommended changes too (e.g. SEC-misconduct-record adviser firms get recommended without search). |
| **Key Innovations** | (1) Registry-grounded audit of AI *referrals* (a rec-adjacent domain with hard ground truth); (2) quantified fabrication rates (4–11%) under a thin-web condition + the search alters distribution finding; (3) practical evidence for a product-level implication: referral systems need search/enumeration gating. |
| **Link** | [arXiv:2609.18341](https://arxiv.org/abs/2609.18341) |

### 1.4 How Calibration Content Shapes Attention-Based Reranking

| Field | Detail |
|-------|--------|
| **Authors** | Petros Karypis, Hossein Rajaby Faghihi, Peter Chen, Rui Zhu, Noveen Sachdeva, Yan Zhu, Julian McAuley |
| **Institution** | UCSD (inferred; Julian McAuley) — authorship lineage strongly aligned |
| **Published** | 15 Sep 2026 (cs.IR) |
| **Abstract** | Attention-based rerankers score docs by aggregating query→document attention minus a **null-query calibration pass** intended to strip positional/structural bias. This assumes the null pass removes *irrelevant* signal — but modern prompt content (constraints, instructions, personas, demonstrations) can *enter the scoring readout*, making the null pass relevance-aware and thus destructive. Calibration is especially harmful for longer, more detailed instruction prompts. Fix: **interpolated null calibration** — a training-free knob controlling how much instruction content enters the null baseline. Recovers reranking performance on instruction-heavy tasks where standard calibration fails; on instruction-heavy tasks recovered rankings surpass generative re-rankers. |
| **Key Innovations** | (1) Identifies "calibration content bleed" — a subtle failure mode of a widely used reranking primitive; (2) a single training-free interpolation that fixes it; (3) evidence that the failure accelerates with instruction verbosity. |
| **Link** | [arXiv:2609.17764](https://arxiv.org/abs/2609.17764) |

### 1.5 F-DACE: Fuzzy Disagreement-Aware Causal Evidence Fusion for Conversational Retail Decision Support

| Field | Detail |
|-------|--------|
| **Authors** | Sourish Dey |
| **Institution** | (single author, inferred industrial) |
| **Published** | 16 Sep 2026 (cs.LG) |
| **Abstract** | Observational decision-support systems commonly expose one causal estimate even when plausible estimators disagree. F-DACE is the decision layer on a causal-ML engine (CATE via backdoor adjustment, estimated by EconML DML causal forest + DoWhy regression, checked by two-way FE). It represents precision, propensity overlap, placebo-refutation stability, interval overlap, and directional agreement as **fuzzy memberships**; hard vetoes force **abstention** on estimand mismatch, failed diagnostics, informative sign conflict, weak evidence. In 180 panel simulations across six identification conditions, F-DACE decides in 67.2% of runs and limits false recommendations to 17.2% (vs 33.3% causal forest / 35.6% backdoor regression); 30/31 false recommendations traced to one identification condition. |
| **Key Innovations** | (1) Causal-evidence *abstention* as a first-class decision (retail "say nothing" beats bad recommendation); (2) fuzzy membership aggregation over five disagreement signals; (3) falsification-layer gating (placebo/overlap checks) converted into crisp decision walls. |
| **Link** | [arXiv:2609.18238](https://arxiv.org/abs/2609.18238) |

### 1.6 Memory Has Geometry: Non-Uniform Geometric Memory for Long-Horizon Personalized AI

| Field | Detail |
|-------|--------|
| **Authors** | Jiahong Liu, Wenhao Yu, Zexuan Qiu, Menglin Yang, Irwin King |
| **Institution** | CUHK (inferred; Irwin King) |
| **Published** | 16 Sep 2026 (cs.IR) |
| **Abstract** | Long-term memory is the core substrate for personalized AI, yet personalization is usually stored as discrete records in a static latent space under one global similarity notion. Argument: for data mining the evidence is a **temporal event stream**, while the dominant abstraction is a searchable record set. Proposes modeling memory as a **user-specific dynamical state space with locally heterogeneous geometry** — geometry as computational language (stable vs volatile regions, variable-rate drift, heterogeneous neighborhoods, uncertainty about current state). Profiles/events remain useful as points, but interaction, feedback, and elapsed time induce **trajectories**; memory access becomes trajectory-conditioned reconstruction of the relevant user state, not just nearest-neighbor lookup. |
| **Key Innovations** | (1) Reframes personalization memory as a per-user *dynamical* geometry, not a record store; (2) unifies profile/event/trajectory views with a principled local-geometry vocabulary; (3) positions memory access as state reconstruction, opening an alternative to embedding-similarity retrieval. |
| **Link** | [arXiv:2609.17969](https://arxiv.org/abs/2609.17969) |

---

## 2. Sequential Modeling, MoE & Tabular FMs

### 2.1 The Automaton Underneath: The Additive Input Pathway Is a Parasitic Attractor for State Tracking in Householder Linear RNN

| Field | Detail |
|-------|--------|
| **Authors** | Gunner Levi Howe |
| **Institution** | (single author, inferred) |
| **Published** | 16 Jul 2026 (submission) / cs.LG |
| **Abstract** | Linear RNNs with input-dependent Householder-product transitions (DeltaNet/DeltaProduct-class) can *provably* represent hard state-tracking automata, yet trained models fail to length-generalize — recent work blames optimization. This paper gives a causal account via pre-registered within-architecture ablation: deleting the **additive input injection** `b_t = W_b e_t` while letting input act only through orthogonal transitions makes the same architecture learn exact automata (median accuracy **1.00 at 16× training length** on parity, S4, A5, S5 word problems; without the deletion, models fit length-32 and collapse OOD, 0.20 at position 512). States a representation law: minimal Householder factors per token = maximal reflection length of the task's generators (parity 1, S4 3, A5/S5 4); below it nothing fits. |
| **Key Innovations** | (1) Names "additive input pathway" as the *parasitic attractor* behind DeltaNet length-generalization failure — a mechanism, not just an optimization gap; (2) pre-registered causal ablation with 16× length-generalization recovery; (3) a testable representation law linking reflection length to required factors. |
| **Link** | [arXiv:2609.18966](https://arxiv.org/abs/2609.18966) |

### 2.2 Beyond the Previous Layer: Residual Predictive Structure in Sparse MoE Routing

| Field | Detail |
|-------|--------|
| **Authors** | Hao Li, Yasuyuki Tahara, Yuichi Sei |
| **Institution** | (inferred academic) |
| **Published** | 15 Sep 2026 (cs.LG) |
| **Abstract** | Sparse MoE routes each token through a sequence of expert selections; does the *immediately preceding* selection adequately summarize the trajectory for predicting the next router? On frozen OLMoE and JetMoE: extending history from one to eleven layers raises router-logit **R² from 0.59879 to 0.66544** in OLMoE; a preregistered JetMoE replication yields four-layer gains of 0.14275/0.20528. Gains survive nonlinear decoding (MLP: +0.17137/+0.21861, whereas nonlinear decoding of recent state alone adds ~0.0014–0.0094 over a linear probe). Parameter-matched controls preserve the advantage; cross-fitted history residuals predict target residuals (R² 0.20549/0.23556). |
| **Key Innovations** | (1) Quantified "residual predictive structure" — earlier expert selections carry router-predictive signal not contained in the last selection; (2) preregistered cross-model (OLMoE/JetMoE) replication discipline; (3) implication: router proxies/caching can exploit trajectory history instead of last-token state. |
| **Link** | [arXiv:2609.17940](https://arxiv.org/abs/2609.17940) |

### 2.3 HOPE: Higher-Order Pruning of Experts in Mixture-of-Experts Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Alex M. Tseng, Prannay Kaul, Luca Zancato, Wei Xia, Stefano Soatto |
| **Institution** | Amazon (inferred; Luca Zancato / Stefano Soatto) |
| **Published** | 16 Sep 2026 (cs.LG) |
| **Abstract** | MoE expert pruning is the most direct memory cut, but existing methods prune each expert independently, assuming purely additive contributions. HOPE (Higher-Order Pruning of Experts) derives a **second-order pruning objective provably minimizing an upper bound on pruning error**, treating expert usage as *inherently cooperative*. REAP (SOTA first-order) is shown to be a special case ignoring interaction terms. Across three frontier MoEs (up to **122B**), two calibration sets, and multiple benchmarks (math, instruction following, coding, agentic): better pruning decisions than existing methods, advantage most pronounced at high prune rates and on agentic workloads — at 50% pruning HOPE beats all baselines. |
| **Key Innovations** | (1) First second-order/cooperative formulation of expert pruning with an error-bound guarantee; (2) unification result (REAP = HOPE minus interactions); (3) empirical edge exactly where it matters (aggressive pruning + agentic routing). |
| **Link** | [arXiv:2609.18916](https://arxiv.org/abs/2609.18916) |

### 2.4 Colla-Q: Collaborative Experts in MoE Quantization via Minimax Precision Balancing

| Field | Detail |
|-------|--------|
| **Authors** | Eunju Shin, Jongbin Ryu |
| **Institution** | (inferred academic) |
| **Published** | 16 Sep 2026 (cs.LG) |
| **Abstract** | Quantization degrades MoE models especially hard because small per-expert parameter budgets are sensitive to low-bit representation, and MoE behaves as an **ensemble with collaborative routed experts** — one badly-quantized expert drags the whole model down. **Colla-Q** is a bit-allocation framework using an **activation-entropy-based bit-width allocation** to keep *per-expert* performance balanced (minimax-style), improving overall MoE quality and **reducing dependence on the calibration dataset** (uniform per-expert stability → robustness). |
| **Key Innovations** | (1) Treats expert quantization as a team-balancing (minimax) problem, not per-expert independent; (2) activation-entropy driven bit allocation; (3) calibration-sensitivity reduction as an explicit design goal. |
| **Link** | [arXiv:2609.18131](https://arxiv.org/abs/2609.18131) |

### 2.5 TabPFN-3.5: Technical Report

| Field | Detail |
|-------|--------|
| **Authors** | Benjamin Jäger, ..., Bernhard Schölkopf, Yann LeCun, ..., Frank Hutter (49 authors) |
| **Institution** | Prior Labs (inferred from project lineage) |
| **Published** | 15 Sep 2026 (cs.LG) |
| **Abstract** | Technical report for the **TabPFN-3.5** tabular foundation model: SOTA on **TabArena**, extended to practical data regimes — non-i.i.d./temporal/grouped splits, string/text/image columns, high-cardinality categoricals, wide tables. Matches task-specific harnesses (relational + time-series forecasting). Variants: **-Fast** (up to 3× faster than TabPFN-3, most gains kept), **-Plus** (text/date handling + inference optimizations), **-Thinking** (scales inference-time compute for further gains with the standard TabPFN pretrained-header reasoning setup). |
| **Key Innovations** | (1) Tabular pretraining now covers the *data regimes practitioners actually see* (non-i.i.d., messy columns), not just i.i.d. tables; (2) explicit inference-time-compute knob (Thinking mode) for tabular; (3) time-series/relational harness wins broaden the tabular-FM surface. |
| **Link** | [arXiv:2609.17895](https://arxiv.org/abs/2609.17895) |

---

## 3. LLM Serving, KV-Cache & Inference Efficiency

### 3.1 ASPIRE: Asynchronous Batched Self-Speculative Decoding for Long-Context LLM Inference

| Field | Detail |
|-------|--------|
| **Authors** | Amir Ziashahabi, Hossein Entezari Zarch, Lei Gao, Murali Annavaram, Salman Avestimehr |
| **Institution** | USC (inferred; Avestimehr / Annavaram) |
| **Published** | 16 Sep 2026 (cs.LG) |
| **Abstract** | Long-context inference is attention-bound; self-speculative decoding (draft with sparse attention, verify with full attention) helps, but existing batched methods stay **synchronized**: all requests share one draft-verify schedule even though optimal draft length varies across requests and over time. **ASPIRE** (1) uses a **unified mixed forward** so drafting and verifying requests coexist in one batched pass; (2) a **lightweight online speculation scheduler** with per-request acceptance-rate estimates and a batch-aware cost model, so each request independently chooses when to verify; (3) an **intra-draft refresh layer** running full attention at one designated layer during drafting to reduce stale sparse context. |
| **Key Innovations** | (1) Kills the global draft-verify phase lockstep — per-request pacing; (2) per-request acceptance-rate estimation as the scheduling cost model basis; (3) intra-draft refresh as an anti-staleness mechanism for long-context sparse drafting. |
| **Link** | [arXiv:2609.17943](https://arxiv.org/abs/2609.17943) |

### 3.2 Contiguity, Not Importance: Budgeted Repair of Stale KV Caches After Document Edits

| Field | Detail |
|-------|--------|
| **Authors** | Mingyang Mao, Wyatt Mackey, Xiaomin Lin |
| **Institution** | (inferred academic) |
| **Published** | 16 Sep 2026 (cs.LG) |
| **Abstract** | KV-cache reuse cuts inference cost in RAG/agentic systems, but caches go stale when retrieved knowledge, working memory, or user state is edited; under causal self-attention even a local edit affects downstream KV. Full re-prefill restores consistency but is costly; refreshing only the edited span leaves downstream deps stale. Formulates **in-place repair as budgeted recomputation**, comparing training-free position-selection policies on a factual RAG benchmark with matched direct/derived edits. All policies repair direct cases; **derived cases separate them** — a *contiguous edit-local window* recovers ≥0.94 of post-edit answer margin and beats attention-based / KV-deviation / structural selectors. Mechanistic: scattered positions succeed under clean-state transplantation but fail under real recomputation because they inherit surrounding staleness. |
| **Key Innovations** | (1) Formalizes stale-KV in-place repair as budgeted recomputation (a servable, well-scoped primitive); (2) demonstrates edit *derivations* (not just direct edits) as the hard case; (3) "contiguity beats importance" — a counterintuitive, mechanistically explained selector result. |
| **Link** | [arXiv:2609.17983](https://arxiv.org/abs/2609.17983) |

### 3.3 Token Latency Fairness: Performance Isolation for Multi-Tenant LLM Serving

| Field | Detail |
|-------|--------|
| **Authors** | Dev Bali, Soujanya Ponnapalli, Yichuan Wang, Natacha Crooks, Scott Shenker, Matei Zaharia |
| **Institution** | UC Berkeley (inferred; Shenker / Zaharia) |
| **Published** | 16 Sep 2026 (cs.DC) |
| **Abstract** | Shared multi-tenant LLM serving lets one client's load blow latency SLOs for others; existing isolation equalizes *throughput* (queueing/batching fairness) but not *latency*. **FairInference** provides the **δ-token fairness guarantee**: for a well-behaved client, if a token is generated in `d` time units in isolation, it is generated within `d + δ` in multi-tenant execution. The key challenge: bounding delays from shared GPU resources **without** fine-grained scheduling or resource allocation. The scheduler enforces per-token deadlines while bounding GPU-compute-sharing delays. |
| **Key Innovations** | (1) First *latency*-isolation guarantee (δ-token fairness) rather than throughput fairness for LLM serving; (2) deadline-based scheduling under shared-GPU constraints without fine-grained control; (3) a clean formal contract clients can SLO to. |
| **Link** | [arXiv:2609.18112](https://arxiv.org/abs/2609.18112) |

### 3.4 AutoTuneBench: Trustworthy Measurement for Agent Auto-Tuning of LLM Serving Engines

| Field | Detail |
|-------|--------|
| **Authors** | Li Chen |
| **Institution** | (inferred industrial/academic) |
| **Published** | 16 Sep 2026 (cs.DC) |
| **Abstract** | LLM agents tune GPU kernels/serving engines via propose-measure-keep loops, but the measurement behind them is not trustworthy. Four failure modes from a four-day pilot corpus (619 model calls): **strawman baselines** manufacture speedups, absolute times don't transfer across machines, **saturated tasks** nullify comparisons, and infrastructure defects impersonate science. **AutoTuneBench** makes trust architectural: protocol frozen as code with provenance, DB-level rejection of out-of-protocol results, anti-cheat checks outside the agent's modification surface, pre-registered readouts, anchors to externally published results, paired-seed stats with a 5% cross-run CV cap. Honest measurement rewrites headlines: best kernel is **10.6× vs a naive baseline but 2.03× vs an honest one**; one config delivers 1.174× on one machine and 1.0049× on another. |
| **Key Innovations** | (1) Turns "agent measured a speedup" into a formally audited claim (provenance-frozen protocol); (2) documents four concrete measurement-failure modes with real pilot corpus (619 calls); (3) provides the anti-cheat/anchoring machinery agents can't override. |
| **Link** | [arXiv:2609.18123](https://arxiv.org/abs/2609.18123) |

### 3.5 Ask the Tool, Don't Guess: Agent Tool Calls Hold Their Progress, and the Serving System Should Read It

| Field | Detail |
|-------|--------|
| **Authors** | Yipeng Liu, Yingqiang Zhang, Feifei Li, Huanchen Zhang |
| **Institution** | (inferred academic) |
| **Published** | 16 Sep 2026 (cs.DC) |
| **Abstract** | Agentic requests wait for tools while their KV caches pin GPU memory; serving systems decide cache stay/leave/come-back by *guessing* tool duration (name, history, declared duration, occupancy). But no fixed-before-call estimate can know duration. Proposal: **tool calls report progress explicitly while running**, and the harness should read it. Census of four public agent corpora: a readable signal exists in most tool time (fraction of work remaining, or an accurate "end is near" signal) at **no measurable cost to benchmark score**; at KV-decision points reported progress beats guesses by several times to an order of magnitude. |
| **Key Innovations** | (1) Replaces duration *guessing* with tool-reported *progress* as the KV/dedup input; (2) cross-corpus census (four agent corpora) quantifying how much tool time is actually predictable at decision points; (3) harness change that costs nothing to agent scores. |
| **Link** | [arXiv:2609.18849](https://arxiv.org/abs/2609.18849) |

---

## 4. LLM Training Stability, Alignment & Safety

### 4.1 Preventing Model Collapse: A Fisher–Rao Perspective on the Dynamics of Training with Synthetic Data

| Field | Detail |
|-------|--------|
| **Authors** | Matteo Marchi, João Pedro Silvestre, Bahman Gharesifard, Paulo Tabuada |
| **Institution** | UCLA (inferred; Tabuada) |
| **Published** | 16 Sep 2026 (cs.LG) |
| **Abstract** | Recursive training on synthetic data induces model collapse. Purpose: rigorous guarantees on the **minimum human-data rate needed to prevent collapse** when training on a human+synthetic mixture. Previous lower bounds rely on Euclidean geometry in ℝⁿ and are vacuous in high dimensions — inappropriate for the space of *categorical probability distributions*. This paper leverages the **information-geometric (Fisher–Rao) structure** of the probability simplex to establish new guarantees on the required human-data ratio (in the synthetic-data co-training setting). |
| **Key Innovations** | (1) Replaces the vacuous Euclidean lower bound with information-geometric guarantees on the human-data ratio; (2) drops unrealistic generative-model assumptions; (3) principled footing for the human↔synthetic data mixing ratio that industry now must pick in practice. |
| **Link** | [arXiv:2609.18878](https://arxiv.org/abs/2609.18878) |

### 4.2 Beyond Quadratic Loss: The Stability Phase Diagram of Adam

| Field | Detail |
|-------|--------|
| **Authors** | Gaoxiang Tang, Huanran Chen, Ziming Liu |
| **Institution** | MIT IAP (inferred; Ziming Liu) |
| **Published** | 16 Sep 2026 (cs.LG) |
| **Abstract** | Loss spikes in neural-net training have multiple mechanisms; for Adam they link to optimizer dynamics, but the role of the two momentum timescales (β1, β2) was unclear. Mapping dynamics across the **(β1, β2) plane** reveals an approximately linear boundary — **1−β2 = C(1−β1)** — separating spiky from non-spiky dynamics (vs ~cubic slope for 1-D quadratic loss). A 1-D superquadratic loss `L ∝ |x|ⁿ` recovers near-linear scaling and ties the boundary coefficient to the effective loss exponent n. Confident cross-entropy losses develop a **core–wall landscape** (narrow quadratic core + steep wall) producing effective superquadratic behavior at optimizer-update scale. |
| **Key Innovations** | (1) Empirically maps Adam's (β1,β2) stability phase diagram across model-task settings; (2) superquadratic-loss theory unifying the observed linear boundary; (3) "core–wall" landscape explanation linking entropy/loss curvature to spike susceptibility. |
| **Link** | [arXiv:2609.18314](https://arxiv.org/abs/2609.18314) |

### 4.3 Beyond Routine Compliance: Cunning Data Cultivates Safety Vigilance in Large Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Youjia Wang, Lin Xu, Yang Sun, Yuxiao Lu, Chengfang Fang, Jie Shi |
| **Institution** | (inferred industrial/academic) |
| **Published** | 16 Sep 2026 (cs.CR) |
| **Abstract** | Aligned LLMs fail when harmful intent is concealed inside benign-looking context; robust safety needs both boundary knowledge and **vigilance** (detecting unusual premises, misleading reasoning, latent risk). Introduces **cunning questions** — not necessarily safety-related, but containing misleading premises / atypical reasoning / subtle inconsistencies — and hypothesizes that learning to look past reasoning traps transfers to safety-critical scenarios. Training on cunning data improves robustness to **OOD jailbreaks** and strengthens subsequent safety fine-tuning; adding it to a SOTA alignment pipeline establishes a new SOTA across their benchmarks. |
| **Key Innovations** | (1) Recasts safety as *vigilance* (scrutiny of premises) rather than answer-time refusal knowledge; (2) self-supervised-able curriculum (cunning data ≠ jailbreak data); (3) positive transfer into existing alignment pipelines. |
| **Link** | [arXiv:2609.18515](https://arxiv.org/abs/2609.18515) |

### 4.4 STRETCH: A Unified Self-Taught Framework for Progressive LLM Evolution

| Field | Detail |
|-------|--------|
| **Authors** | Yajie Yu, Mark Lee, Yue Feng |
| **Institution** | University of Birmingham (inferred; Mark Lee) |
| **Published** | 16 Sep 2026 (cs.CL) |
| **Abstract** | Self-improvement training stalls because fixed difficulty fails to track evolving proficiency. **STRETCH** (Self-Taught Reasoning Evolution via Targeted CHallenge) adds a dynamic **Stretch Zone** aligning question difficulty with model capability. In one parameter space the model alternates between a **Scaffolder** (generates adaptive boundary-pushing challenges) and a **Learner** (RL-optimized solving trajectories) — dual-loop co-evolution that stabilizes training, mitigates reward hacking, and promotes progressive reasoning growth. Beats strong prompting and domain-specific baselines on negotiation + operations research benchmarks; ablation shows dynamic difficulty alignment is critical for sustained gains. |
| **Key Innovations** | (1) Cognitive-scaffolding gap as an explicit difficulty-adaptation loop inside self-improvement; (2) single parameter space co-evolution (no separate reference models); (3) reward-hacking mitigation via challenge alignment (interesting vs recent literature where harder data backfires). |
| **Link** | [arXiv:2609.18642](https://arxiv.org/abs/2609.18642) |

### 4.5 Voice of Reason: Reinforcement Learning for Spoken Math

| Field | Detail |
|-------|--------|
| **Authors** | Timothée Weisselberger, Edouard Graves, Alexandre Défossez |
| **Institution** | Meta / Université Paris-Saclay (inferred; Défossez) |
| **Published** | 16 Sep 2026 (cs.SD) |
| **Abstract** | Speech LMs enable richer spoken interaction but lag text models on math reasoning. Applies **RL with verifiable rewards** to the **GLM-4-Voice** speech model: SFT on synthesized spoken QA data, then RL — *even without extra reasoning tokens*, RL improves GSM8K accuracy beyond prior speech-only results achieved with supplementary reasoning traces; combined with streaming reasoning techniques reaches **74.8% free-form accuracy**, a new SOTA for spoken math. |
| **Key Innovations** | (1) Verifiable-reward RL transferred to *speech* reasoning (not just text); (2) shows reasoning-token-free RL gains (and further gains with streaming reasoning); (3) GSM8K SOTA for spoken math via a text-family recipe. |
| **Link** | [arXiv:2609.18677](https://arxiv.org/abs/2609.18677) |

---

## 5. LLM Agents, Memory & Governance

### 5.1 Reflections on Trusting Trust, Revisited: Contaminating Self-Modifying AI Coding Agents with Poisoned Benchmarks

| Field | Detail |
|-------|--------|
| **Authors** | Franziska Roesner, Tadayoshi Kohno |
| **Institution** | University of Washington (inferred; Roesner / Kohno) |
| **Published** | 15 Sep 2026 (cs.CR) |
| **Abstract** | Thompson's "Reflections on Trusting Trust" showed a compiler can be poisoned to reinsert its own backdoor. Today the "compiler" is a **self-modifying coding agent**. Can an adversary supply poisoned benchmarks to the agent's self-evaluation/self-improvement process so future versions write *vulnerable* code on clean held-out tasks? Instantiates the attack against three self-modifying coding agents (Darwin Gödel Machine with modifications; Self-Improving Coding Agent and Hyperagents, both substantively unmodified). Successful POCs — e.g., with Hyperagents powered by Sonnet 4.5, a poisoned benchmark drives self-evolution of instructions that **disable HTTPS certificate validation** on neutral URL-fetching tasks. Distills properties and countermeasures. |
| **Key Innovations** | (1) Brings Thompson's trusted-compiler threat model to self-modifying *agents* — evaluations are now attack surfaces; (2) identifies which self-improvement designs are poisonable (and which resist, informing agent architecture); (3) concrete vulnerability examples (TLS disabling) plus defense properties. |
| **Link** | [arXiv:2609.17817](https://arxiv.org/abs/2609.17817) |

### 5.2 Reflect, Revise, Reuse: Training-Free Skill Evolution for GUI Agents

| Field | Detail |
|-------|--------|
| **Authors** | Bofan Chen, Boxuan Zhang, Fei Tang, Zhengxi Lu, Yong Du, Tongbo Chen, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen |
| **Institution** | Zhejiang University (inferred; Weiming Lu / Yueting Zhuang) |
| **Published** | 15 Sep 2026 (cs.CL) |
| **Abstract** | GUI agents fail when pop-ups, delayed loads, and relocated widgets invalidate pre-made plans. Agent-skill frameworks exist, but treat skills as static pre-deployment artifacts. **EvoSkill-GUI** makes skills *living*: each skill is a multi-file package (retrieval metadata, executable plans, backup localization, failure-recovery rules, accessibility utilities, failure cases) revised from execution feedback **without training**. A **reflect–revise–reuse** loop: executor does instant in-rollout revisions; an isolated critic diagnoses failed trajectories under strict integrity gatekeeping; skills are versioned and re-indexed after revision so future runs reuse the fix. |
| **Key Innovations** | (1) Skills as structured versioned packages with a reflect-revise-reuse loop (training-free); (2) deployment-time maintenance built into the skill format (recovery/accessibility/backup fields); (3) critic + integrity gating to prevent self-reinforcing bad skills. |
| **Link** | [arXiv:2609.17653](https://arxiv.org/abs/2609.17653) |

### 5.3 Compositional Policy Violations: When Step-Level Compliance Fails in Agentic AI Workflows

| Field | Detail |
|-------|--------|
| **Authors** | Ashwini Kurady, Sri Sai Charith Grandhi, Rajesh Gupta, Sumit Mamoria |
| **Institution** | (inferred industrial) |
| **Published** | 16 Sep 2026 (cs.SE) |
| **Abstract** | Agentic governance is almost entirely **step-scoped** (input-output classifiers, per-turn rails, span-level evaluators) while the policies organizations hold (referral thresholds, authority limits, review requirements) are **properties of the whole execution**. Failure mode: **Compositional Policy Violation (CPV)** — every step passes its own check, the composed execution violates the policy. No single-step predicate can evaluate a property that step doesn't determine. Taxonomy: **Authority Creep, Threshold Laundering, Cumulative Sum Violation, Context Collapse**; the correct repair per class is dictated by where the guarded quantity mutates. Proposes a **provenance-aware runtime architecture** to catch CPVs. |
| **Key Innovations** | (1) Names/formalizes a governance blind spot distinct from step-level misbehavior (CPV); (2) four-class taxonomy with repair anchored to quantity-mutation location; (3) architectural prescription (provenance-aware runtime) rather than better single-step classifiers. |
| **Link** | [arXiv:2609.18820](https://arxiv.org/abs/2609.18820) |

### 5.4 CERA-MoA: Co-Evolving Routing Mechanisms with Continually Learning LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Jiaxuan Jiang, Liyuan He, Zhixuan Fang |
| **Institution** | Tsinghua (inferred; Zhixuan Fang) |
| **Published** | 16 Sep 2026 (cs.LG) |
| **Abstract** | Mixture-of-Agents (MoA) usually decouples query routing from agent fine-tuning, so routers can't adapt as agent capabilities evolve. **CERA-MoA** is an iterative RL framework where the **dynamic router and independent agent policies co-evolve**: a predictive **familiarity estimator** (mid-layer hidden states) scores agent competence without full-rollout cost, and a **cumulative-threshold adaptive routing** mechanism activates a minimal tailored agent subset (performance/efficiency trade-off). Training samples are allocated to agents by evolving competence → capability differentiation, + collaboration. |
| **Key Innovations** | (1) Co-evolution (router + agents in one RL loop) vs fixed routing; (2) hidden-state familiarity estimator to avoid rollout cost; (3) dynamic subset activation for a cost-quality Pareto improvement. |
| **Link** | [arXiv:2609.18779](https://arxiv.org/abs/2609.18779) |

### 5.5 Confidence Comes from Experience: Experiential Confidence Estimation from Reasoning to Agents

| Field | Detail |
|-------|--------|
| **Authors** | Caiqi Zhang, Xiaochen Zhu, Chengzu Li, Yulong Chen, Dharshan Kumaran, Nigel Collier |
| **Institution** | University of Cambridge (inferred; Collier / Kumaran) |
| **Published** | 15 Sep 2026 (cs.CL) |
| **Abstract** | Current confidence estimators share one premise: they only read the *current* inference (introspection, token probabilities, resampling). Argues current inference is not sufficient. **XConf** estimates confidence jointly with the model's accumulated **experience**: a record of graded past episodes (task, model reflection, stated confidence, outcome, post-grade lesson). Given a new task, XConf conditions confidence on both the current attempt and the accumulated experiential record — empirically transferring from reasoning/QA tasks into agentic settings. |
| **Key Innovations** | (1) Reframes confidence as a property of model+history, not just a single inference; (2) a concrete graded-episode memory format and inference procedure; (3) reasoning→agents transfer evidence for the "experience improves calibration" claim. |
| **Link** | [arXiv:2609.17708](https://arxiv.org/abs/2609.17708) |

---

## 6. Evaluation, IR, World Models & Market Dynamics

### 6.1 Who Judges Matters: Measuring Family-Conditioned Preference in LLM-as-Judge Panels

| Field | Detail |
|-------|--------|
| **Authors** | David Ababio Awuni, Luke E. K. Achenie, Benjamin Tei Partey, Elvis Gyasi Owusu, Nii-Nai Derrick Sowah |
| **Institution** | (inferred academic) |
| **Published** | 15 Sep 2026 (cs.CL) |
| **Abstract** | Who the judge is affects LLM-as-judge results, but measuring it without confounds is hard. Fully crossed pairwise design across four open-weight families (Llama 3.1, Qwen 2.5, Gemma 2, Yi 1.5), 9,312 judgments. A common per-family statistic is confounded with candidate quality (correlates with Bradley–Terry ability at r=0.95). A **corrected estimator** holding candidate family fixed reveals **positive same-family lift (3.4–8.4 pp)** in all four families (global FPS 0.067, permutation p=0.0002) — robust to panel quality controls, a human-consensus anchor, and float16 replication. **Position is a separate failure mode: 55.4% of AB/BA pairs reverse** — reversal above 50% is incompatible with stable preference. |
| **Key Innovations** | (1) Confound-corrected estimator isolating family-conditioned judge preference (r=0.95 naive confound exposed); (2) robust same-family-lift result across 4 families/9,312 judgments; (3) the >50% AB/BA reversal rate as a coordination/stability warning for judge panels. |
| **Link** | [arXiv:2609.17857](https://arxiv.org/abs/2609.17857) |

### 6.2 REPAIR: Resolving Long-Tail Confusion in Scientific Retrievers via Fact-Verified Iterative Refinement

| Field | Detail |
|-------|--------|
| **Authors** | Yerim Oh, Gunhee Kim |
| **Institution** | Seoul National University (inferred; Gunhee Kim) |
| **Published** | 16 Sep 2026 (cs.IR) |
| **Abstract** | Scientific retrieval is limited by long-tail concepts and fact-sensitivity. **REPAIR** is a self-evolving data augmentation framework that cycles through **diagnosis** of long-tail concept gaps, **API-guided evidence expansion**, and **differentiation via hard-negative mining** — grounding retrieval in factual reality. Outperforms 19 strong baselines on nine materials-science/biomedical benchmarks; diagnosing and factually augmenting long-tail deficits is essential for robust scientific retrieval. |
| **Key Innovations** | (1) Long-tail *diagnosis* as the driving signal (vs random augmentation); (2) fact-verified, API-grounded expansion (no hallucinated negatives); (3) self-evolving loop that improves the retriever's own data. |
| **Link** | [arXiv:2609.18262](https://arxiv.org/abs/2609.18262) |

### 6.3 EffiRAG: When Is Graph Structure Worth Its Cost? The Case for Structure Pricing in RAG

| Field | Detail |
|-------|--------|
| **Authors** | Yuzhong Zhang, Haoyang Ma, Chao Peng, Lionel Briand, Boxi Yu, Jialun Cao |
| **Institution** | University of Ottawa / spring-ml lineage (inferred; Briand / Cao) |
| **Published** | 16 Sep 2026 (cs.IR) |
| **Abstract** | Graph RAG helps question-answering requiring many documents, but building a graph costs many LLM calls at ingestion. **EffiRAG** asks whether quality gains justify the cost and designs for lightness: it uses the graph only to **locate relevant passages**, then generates answers from original text — preserving source info while keeping construction and querying cheap. On UltraDomain (120 open-ended questions, four domains): preferred over LightRAG-hybrid on 93 questions (vs 7, 20 splits), while cutting **total cost 57%** (USD 0.952 → 0.408); advantage persists as corpus grows, aided by a lightweight non-LLM filter skipping low-salience passages. |
| **Key Innovations** | (1) Explicit "structure pricing" (graph-value vs LLM-ingestion-cost accounting) for graph RAG; (2) eliminates graph-derived answer generation (graph = locator, text = source of truth); (3) 57% cost cut with preference-win evidence. |
| **Link** | [arXiv:2609.18099](https://arxiv.org/abs/2609.18099) |

### 6.4 CSWAM: Causal Semantic Representations for OOD Generalization in World Action Models

| Field | Detail |
|-------|--------|
| **Authors** | Tianbin Liu, Jian Zhu, Taiyi Su, Jianjun Zhang, Chong Ma, Zitai Huang, Weiyi Lu, Yi Xu |
| **Institution** | (inferred academic) |
| **Published** | 16 Sep 2026 (cs.LG) |
| **Abstract** | FastWAM-style world action models give efficient action-only inference but generalize poorly under visual distribution shift (reconstruction-oriented representations overfit appearance). **CSWAM** augments FastWAM with a **causal semantic expert built on V-JEPA 2.1** — temporally grounded semantic state-change/motion representations with less appearance dependence. The expert learns future evolution from a sparse history of current/past observations and shares history-derived context with both video and action streams via causal attention; at inference, action denoising conditions on current video state + observed semantic history while retaining action-only inference. |
| **Key Innovations** | (1) Causal-semantic (V-JEPA-style) representations to beat appearance-specific overfitting in world action models; (2) sparse history conditioning shared across video+action streams; (3) keeps FastWAM's efficient action-only inference at deploy. |
| **Link** | [arXiv:2609.18462](https://arxiv.org/abs/2609.18462) |

### 6.5 SAiFE-gym: Model-based Environments for Automated Market Making with Concentrated Liquidity

| Field | Detail |
|-------|--------|
| **Authors** | Georgios Chionas, Charalampos Kleitsikas, Stefanos Leonardos, Leandro Sánchez-Betancourt, Carmine Ventre |
| **Institution** | King's College London / QMUL (inferred; Leonardos / Ventre) |
| **Published** | 15 Sep 2026 (cs.GT / q-fin) |
| **Abstract** | Python module of simulation environments for automated market making in **Constant Product Markets with Concentrated Liquidity** (CL). Decomposes CPM-CL microstructure into interactive components (LPs control capital allocation, adjust liquidity ranges dynamically, dictate fee earning); vectorized for scalable high-dimensional RL workflows. Demonstrates by evaluating RL agents under market-parameter uncertainty — bringing the **market-maker gym** genre to concentrated-liquidity AMMs. |
| **Key Innovations** | (1) First RL-oriented environment suite for CL-AMM market making; (2) modular microstructure decomposition + vectorized RL-scalable design; (3) opens a testbed for DeFi automated market-making strategies under uncertainty. |
| **Link** | [arXiv:2609.17788](https://arxiv.org/abs/2609.17788) |

---

## Summary of Key Trends

| Trend | Notable Papers |
|-------|---------------|
| **E-commerce/recommendation value layer is where the rec research is** | Behavior2Value (consumer values from Taobao logs), Too Good to Be Real (AI "logic overbinding" vs real engagement), AI-referral audit (4–11% fabrication on local-service markets), F-DACE (abstention-safe causal retail decisions) — rec research continues to migrate from CTR-model tuning to *value/meaning/evaluation* layers |
| **KV-cache economics becomes a systems research area with distinct primitives** | ASPIRE (async batched self-speculation), Contiguity-Not-Importance (budgeted stale-KV repair), Ask-the-Tool (tool-progress signals for KV decisions), Token-Latency Fairness (δ-token SLO isolation at Berkeley) |
| **MoE papers cluster on cooperation-aware memory work** | HOPE (second-order cooperative expert pruning), Colla-Q (minimax expert bit allocation), Residual Predictive MoE routing (trajectory history, not last layer), CERA-MoA (co-evolving router↔agent routing) |
| **Sequential-state models get mechanistic accountability** | Householder-ΔRNN additive-pathway diagnosis (automaton paper) explains *why* DeltaNet length-generalization fails and fixes it at 16× length |
| **Training-stability theory matures** | Fisher–Rao human-data-ratio bounds for model-collapse prevention (UCLA), Adam's (β1,β2) stability phase diagram / superquadratic-loss theory |
| **Safety moves from "knowledge" to "vigilance & architecture"** | Cunning-data vigilance (belt-and-suspenders alignment), poisoned-benchmark threat model for self-modifying coding agents (Trusting-Trust revisited, UW), compositional policy violations (step-vs-workflow governance gap) |
| **Evaluation keeps diagnosing judge/measurement pathologies** | Family-conditioned judge preference (55.4% AB/BA reversal), AutoTuneBench (honest measurement for agent tuning), TabPFN-3.5 extending SOTA baselines into messy-data regimes |

(Runner-ups worth a look, grep-verified unclaimed: **2609.18123**'s sibling serving-measurement line above; **2609.18672** Selection Is Retrieval, Abstention Is Not (on-device tool routing over 70 actions); **2609.18417** Dependency-Aware Trajectory Refinement for multi-turn agent SFT (up to +5.7pp, fewer messages); **2609.17708** XConf experiential confidence; **2609.17688** CapMem episodic-memory-as-captions benchmark; **2609.18519** COMPASS-ABS GPU-cluster fragmentation scheduler; **2609.18909** DualViewEval process-aware agent benchmark compression; **2609.18328** GuardEn executable safety-rule entailment for VLMs; **2609.18861** PersonaPath knowledge-centric learning-path planner.)

(End of file — total 31 papers / 6 sections)