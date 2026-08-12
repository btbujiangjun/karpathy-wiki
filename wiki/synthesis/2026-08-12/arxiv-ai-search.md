---
title: arXiv AI Research Search — August 12, 2026
type: synthesis
created: 2026-08-12
updated: 2026-08-12
sources: [arxiv-listing, arxiv-abstract-pages]
tags: [arxiv, ai, llm, ads, ctr, conversion, recommendation, llm-ranker, quantization, moe, scaling-laws, on-policy-distillation, rl-systems, coding-agents, reasoning, verification, games, poker, mechanism-design, time-series, conformal-prediction, daily-digest]
---

# arXiv AI Research Search — 2026-08-12

> Search window: **Wed, Aug 12, 2026** arXiv announcement batch (new submissions Aug 10–11, IDs ~2608.09954–2608.11200). The first fresh batch since the Aug 10–11 digests (which covered IDs up to 2608.09930). Streams scanned: cs.LG (164 new), cs.CL (95 new), cs.IR (22 new), cs.GT (9 new), cs.SE (22 new), cs.MA (14 new), cs.AI (211 new). arXiv export API was rate-limited, so listings and all selected-paper metadata were verified via web pages (`arxiv.org/list`, `arxiv.org/abs`).
>
> 14 papers curated, **all NEW** (grep-verified 0 hits on arXiv ID across wiki/index.md, wiki/log.md, and wiki/synthesis/**). This is the first 2026-08-12 synthesis output — the same-day [arXiv Paper Check](./arxiv-paper-check.md) (cs.AI+cs.IR) and [Game RL Daily](./game-rl-daily.md) had not yet been generated at time of writing, so the strongest industrial cs.IR/cs.AI picks (Netflix GenRec, Meta ConnectionMind, LinkedIn MARCO) are included here. Zero overlap with all prior digests (2026-08-11 max covered ID: 2608.09930; every paper below is ≥ 2608.09954).

## Overview table

| # | Paper | Domain | Institution / Company | arXiv | Status |
|---|-------|--------|----------------------|-------|--------|
| 1 | MARCO: Click-Intent Decomposition for Calibrated Ads Conversion Prediction | Ads / CTR / CVR calibration | LinkedIn (tentative) | 2608.10562 | **new** |
| 2 | GenRec: An LLM-Backed Recommendation Ranker at Netflix | Recommendation / LLM ranker | Netflix (stated) | 2608.10257 | **new** |
| 3 | ConnectionMind: Social Networks + LLMs for Recommendation at Meta | Recommendation / graph reasoning | Meta (stated) | 2608.10187 | **new** |
| 4 | ReRound: Reconstructive Rounding for Calibration-Free LLM Quantization | LLM efficiency / quantization | Harvard University (high confidence) | 2608.11045 | **new** |
| 5 | Share First, Route What Remains: UniF-MoE | LLM architecture / MoE efficiency | University of Macau (high confidence) | 2608.10392 | **new** |
| 6 | Compute-Optimal Is Not Cluster-Optimal: MOSAIC | Scaling laws / MoE systems co-design | (not stated) | 2608.10605 | **new** |
| 7 | ReOrder-OPD: Reliability-Aware Prompt Ordering for On-Policy Distillation | LLM post-training / OPD | (not stated) | 2608.10905 | **new** |
| 8 | TideRL: Boosting Agentic RL Goodput with Readiness-Aware Scheduling | RL systems / agentic RL | Tsinghua University (high confidence) | 2608.10402 | **new** |
| 9 | Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding | Coding agents / prompt memory | (not stated) | 2608.11095 | **new** |
| 10 | VERDICT: Training-Free Step-Wise Verification of Multimodal Reasoning | Reasoning verification / VLM | Microsoft Research India / IIT Hyderabad (high confidence) | 2608.10665 | **new** |
| 11 | Safe Observation Capacity for Opponent Exploitation under Showdown Censoring | Games / poker / opponent modeling | Imperial College London (stated) | 2608.09954 | **new** |
| 12 | Evaluating Rational Contracting in Natural Language (ContractSim) | Mechanism design / LLM negotiation | (not stated) | 2608.10475 | **new** |
| 13 | Two-stage Odd Residual Flows for Mean-Preserving Probabilistic Forecasting (TORF) | Time series / probabilistic forecasting | University of Hildesheim (tentative) | 2608.11114 | **new** |
| 14 | Retrieval-Corrected Conformal Prediction for Time Series (RCCP) | Time series / conformal prediction | (not stated; CIKM 2026) | 2608.10553 | **new** |

---

## 1. Ads, CTR & Conversion Prediction

### 1.1 MARCO: Click-Intent Decomposition for Calibrated Ads Conversion Prediction

- **arXiv**: [2608.10562](https://arxiv.org/abs/2608.10562) (cs.LG; submitted 2026-08-11) — **NEW**
- **Authors**: Shiwen Shen, Xiru Huang, Liang Luo, Jianbo Sun, He Lyu, Zihang Fu, Ivonne Xu, Zhizhuo Li, Zhengyu Zhang, Pei-Ju Sung, Yunmiao Wang, Zixuan Wang, Zhengli Zhao, Qiang Jin, Mike Jermann, Mingda Li, Yang Xiao, Bhavana Challa, Brooke Bian, Yang Li, Ashish Chamoli, Bibek Bhusal, Danning Di, Yuan Jin, Meet Raval, Zhiwen Chen, Boyao Sun, Shuguang Wang, Yunlong He, Yantao Yao, Sagar Chordia, Wenlin Chen, Santanu Kolay, Qin Huang, Ellie Wen (35 authors)
- **Institution**: Not stated on abstract page. Author list (Ellie Wen, Santanu Kolay, Mike Jermann, Bhavana Challa, Shuguang Wang, Yunlong He) is consistent with LinkedIn Ads/Ranking (tentative; inferred from co-author affiliations).
- **Abstract (faithful summary)**: Industrial ads ranking decouples conversion probability into click-through rate (CTR) and post-click conversion rate (CVR), yet treats every click as the same event. Users provide a free, self-generated intent signal through physical UI interactions, and different click types on the same ad exhibit a **4-fold difference in actual conversion rates**. By conflating these signals, the standard CVR model under-predicts high-intent clicks and over-predicts low-intent ones — a bias masked by near-perfect aggregate calibration. **MARCO** (Multi-intent Ads Ranking Composition Optimization) resolves this by decomposing each click by intent: using logged click type as a free behavioral label, it trains per-intent CVR heads on homogeneous populations and composes their estimates at serving under a predicted intent distribution. Theoretically, decomposition never raises population risk (with exact headroom under squared loss and non-negativity under the deployed loss). Multi-impression, multi-click attribution is cast as credit assignment with a bias-variance tradeoff analogous to RL return estimation; last-impression, first-click attribution is shown to be the low-bias, low-variance, deterministic choice under production constraints. Deployed at binary intent granularity, MARCO corrects per-intent calibration to **~100%**, lifts conversions per click by **+2.80%**, and drives **+0.98%** cumulative improvement in topline metrics.
- **Key innovations**: (1) Intent-decomposed CVR heads trained on free click-type labels (a blind spot of aggregate calibration); (2) theory showing decomposition never raises population risk, with the headroom made explicit; (3) production attribution as RL-like credit assignment with a provable low-bias deterministic rule (last-impression, first-click).

### 1.2 GenRec: An LLM-Backed Recommendation Ranker at Netflix

- **arXiv**: [2608.10257](https://arxiv.org/abs/2608.10257) (cs.IR; submitted 2026-08-10) — **NEW**
- **Authors**: Ying Li, Shradha Sehgal, Arjun Rao, Rein Houthooft, Yaochen Zhu, Ashish Rastogi
- **Institution**: Netflix (stated in abstract).
- **Abstract (faithful summary)**: LLMs are reshaping recommender systems by enabling richer modeling of users, content, and context in natural language. **GenRec** is an LLM-backed recommendation ranker at Netflix built on an in-house foundational LLM, following a two-phase framework: Phase 1 adapts an open-source LLM to Netflix data (catalog + member behavior understanding, balancing content understanding and instruction following); Phase 2 post-trains the foundation model with recommendation-ranking-specific data, labels, and reward signals. The paper focuses on Phase 2 and the transition from a traditional discriminative ranker with thousands of engineered features to an LLM-backed ranker driven by **verbalized user histories and context**. It describes input verbalization and context engineering, post-training data construction, reward integration, model architecture, and a **cost-constrained serving design based on prefill-only inference**. A large-scale A/B test vs the production ranker shows a GenRec model trained with substantially fewer Phase-2 labeled examples and input signals achieves statistically significant gains in offline and online metrics. The paper argues LLM-backed recommenders shift the paradigm **from feature engineering to context engineering**, and from bespoke architectures to shared foundation backbones.
- **Key innovations**: (1) Full production account of an LLM-backed ranker replacing thousands of engineered features with verbalized context; (2) prefill-only serving to make LLM ranking cost-viable; (3) evidence that fewer, richer (context-engineered) signals beat engineered features at scale.

### 1.3 ConnectionMind: Social Networks + LLMs for Personalized Recommendation at Meta

- **arXiv**: [2608.10187](https://arxiv.org/abs/2608.10187) (cs.IR / cs.SI; submitted 2026-08-10) — **NEW**
- **Authors**: Haoyu Han, Yuming Liu, Lei Huang, Lizhu Zhang, Jiliang Tang, Xiangjun Fan
- **Institution**: Meta (stated in abstract: deployed in Meta's large-scale recommendation pipeline).
- **Abstract (faithful summary)**: Recommendation on social platforms must model complex social relationships (friendships, group memberships, creator interactions) alongside massive heterogeneous content (text, video); traditional models omit these signals or treat them independently. **ConnectionMind** tightly integrates social network structure with LLMs for scalable, interpretable, reasoning-aware personalization. It builds a heterogeneous graph connecting users, items, friends, groups, and creator pages, and formulates recommendation as **graph reasoning**: discovering personalized paths from users to candidate items. An LLM-based policy reasons over these graphs to guide recommendation. Training is two-stage: (1) SFT on large-scale user-item interaction trajectories to initialize the reasoning policy, then (2) end-to-end RL to refine reasoning over social graphs. Beyond offline gains on multiple real-world datasets, ConnectionMind is **deployed in Meta's production pipeline and A/B tested, achieving +0.43% video watch time**.
- **Key innovations**: (1) Recommendation-as-graph-reasoning over a heterogeneous social graph, driven by an LLM policy; (2) SFT→RL two-stage recipe at production scale; (3) online A/B evidence (+0.43% watch time) in a major social platform.

---

## 2. LLM Efficiency & Architectures

### 2.1 ReRound: Reconstructive Rounding for Calibration-Free LLM Quantization

- **arXiv**: [2608.11045](https://arxiv.org/abs/2608.11045) (cs.LG / cs.CL; submitted 2026-08-11) — **NEW**
- **Authors**: He-Yen Hsieh, H. T. Kung
- **Institution**: Harvard University (high confidence — well-known affiliation of H. T. Kung).
- **Abstract (faithful summary)**: **ReRound** is a post-training quantization method targeting the **midpoint ambiguity** of round-to-nearest (RTN): weights near the center of a quantization interval are ambiguous to round. ReRound trains a **conditional diffusion model** to produce continuous reconstructions of low-bit weights, which act as a guidance signal to disambiguate the rounding direction for weights near midpoints. A tolerance metric determines how far a quantized weight sits from the midpoint: weights within the tolerance region are quantized with diffusion-based reconstructions, weights near boundaries with RTN. Sweeping the tolerance parameter generates candidate quantized integer weight matrices; the selected candidate is the one whose de-quantized matrix best matches the original full-precision weights in **leading singular values**. ReRound is especially effective for smaller LLMs, consistently beating RTN at 3-bit and 4-bit, outperforming an extensive set of **calibration-free** methods, staying competitive with calibration-dependent ones, and adding **no overhead at inference** (fully offline).
- **Key innovations**: (1) Diffusion-reconstructed weights as a rounding-direction prior — a new axis for low-bit quantization; (2) a tolerance sweep + singular-value matching selection rule; (3) calibration-free but near-calibration-dependent quality, with zero serving overhead.

### 2.2 Share First, Route What Remains: UniF-MoE for Token-Adaptive MoE Computation

- **arXiv**: [2608.10392](https://arxiv.org/abs/2608.10392) (cs.LG / cs.CL / cs.CV; submitted 2026-08-11) — **NEW**
- **Authors**: Gongli Zhang, Zhulin Liu, C. L. Philip Chen
- **Institution**: University of Macau (high confidence — well-known affiliation of C. L. Philip Chen).
- **Abstract (faithful summary)**: MoE designs have moved beyond routing a fixed number of complete experts (shared-expert designs preserve reusable knowledge, fine-grained methods vary within-expert computation, dynamic routers adapt expert count), but these decisions are usually made independently. By decomposing sparsely upcycled feed-forward experts into **key-value channels**, the authors find co-activated experts align at a subset of value positions; removing those positions changes expert preference; and greater shared coverage is associated with lower residual expert demand — yielding the principle **"share first, then route what remains"**. **UniF-MoE** instantiates it: each expert is partitioned into aligned blocks; a shared-demand score sets the shared block count and pathway weight; key prototypes select shared content; complementary demand determines residual expert count through cumulative routing mass. A **Gram regularizer** separates and normalizes router embeddings, promoting diverse routing directions and sparse expert overlap. On DomainBed and GLUE, UniF-MoE improves predictive performance over static and dynamic MoE baselines while reducing activated compute, latency, and memory. Code: github.com/existence0420/UniF-MoE.
- **Key innovations**: (1) A mechanistic (KV-channel-level) account of the shared-vs-routed dependency; (2) a unified token-adaptive framework (shared blocks + prototype selection + cumulative-mass expert count) under one principle; (3) Gram regularization for routing geometry; open-source code.

### 2.3 Compute-Optimal Is Not Cluster-Optimal: MOSAIC

- **arXiv**: [2608.10605](https://arxiv.org/abs/2608.10605) (cs.LG / cs.AI; submitted 2026-08-11) — **NEW**
- **Authors**: Soumajyoti Sarkar, Yuxin Tang, Sheng Zha
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: Pretraining conventionally decouples algorithm/architecture decisions (a scaling-law stage optimizing loss under compute) from systems decisions (a hardware-efficiency stage). **MOSAIC** formulates architecture-systems co-design as a single optimization: it couples a predictive scaling law with a **calibrated performance model** estimating MFU, communication cost, memory footprint, and the best parallel layout, instantiated for sparse MoE LMs (expert count, routing sparsity, MoE layer dimensions affect both loss and efficiency). The scaling law spans active parameters **104M–2.7B** and total model sizes up to **79B**, with the **sparsity factor** (fraction of parameters inactive per token) as a scaling dimension. Key finding: within the calibrated sparsity range, an efficiency-agnostic model-FLOPs budget admits **no interior optimal sparsity** — loss decreases monotonically with sparser models, so the compute optimum sits at the upper boundary of data support. An optimal sparsity instead **emerges only under the cluster's systems constraints**, as captured by MOSAIC. The paper argues for unified architecture+systems co-design for frontier LLM training.
- **Key innovations**: (1) Loss+systems joint optimization (MFU, comms, memory, parallelism) for MoE; (2) sparsity as an explicit scaling-law dimension with a 79B-parameter sweep; (3) a clean negative result — compute-optimality alone admits no interior sparsity optimum, only systems constraints do.

---

## 3. LLM Post-Training

### 3.1 ReOrder-OPD: Reliability-Aware Prompt Ordering for On-Policy Distillation

- **arXiv**: [2608.10905](https://arxiv.org/abs/2608.10905) (cs.LG; submitted 2026-08-11) — **NEW**
- **Authors**: Ximo Zhu, Ruiqi Liu, Rong Wang, Ping Wu, Xiang Zheng, Wenzhuo Xu, Xubin Yao, Zhiyuan Yan, Bo Li, Jun Gao, Xiaolei Lv
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: On-policy distillation (OPD) applies token-level teacher supervision to student-generated trajectories, but that supervision is not always reliable. Existing methods weight/filter/truncate trajectories using local confidence or teacher-student agreement — signals that do not directly measure whether the teacher can **continue a student prefix to a correct answer**, and trajectory-level interventions conflate one rollout's unreliability with a prompt's low expected training value. The paper defines **prompt-level teacher continuation reliability R** (teacher's probability of reaching a correct answer from a student prefix, averaged over prefixes/trajectories induced by the current student). Oracle experiments show high-R prompts yield larger OPD gains, and descending-R training beats random/ascending orders on a fixed prompt pool. Since R is expensive, they proxy it by the **max ROUGE-5 F1 between one independent student rollout and verifier-correct same-prompt teacher trajectories**; across ten bins, mean R rises monotonically with the proxy. **ReOrder-OPD** sorts prompts by the proxy, then runs vanilla OPD. It improves every matched aggregate comparison across Qwen3 and Gemma4 math settings and Qwen3 code settings, and gains in all six FiRe-OPD and ExOPD settings show prompt ordering complements within-trajectory supervision.
- **Key innovations**: (1) A principled prompt-level reliability notion (teacher continuation) replacing local/rollout-level heuristics; (2) a cheap, verifier-based proxy that orders prompts monotonically by reliability; (3) orthogonal gains on top of within-trajectory supervision (FiRe-OPD, ExOPD).

### 3.2 TideRL: Boosting Agentic RL Goodput with Readiness-Aware Scheduling

- **arXiv**: [2608.10402](https://arxiv.org/abs/2608.10402) (cs.LG / cs.DC; submitted 2026-08-11) — **NEW**
- **Authors**: Yanyu Ren, Xizheng Wang, Xiao Liu, Bowen Lv, Hanchen Zhang, Shudan Zhang, Hanyu Lai, Shuai Wang, Li Chen, Dan Li, Jie Tang
- **Institution**: Tsinghua University (high confidence — well-known affiliation of Jie Tang).
- **Abstract (faithful summary)**: LLM RL is moving toward multi-turn **agentic workloads**, where rollout tasks repeatedly pause for external environments, resume with growing contexts, and finish at highly variable times. In this regime, training **goodput** (training throughput) matters more than raw GPU occupancy — GPU waiting and repeated prefill recomputation are pure overhead. **TideRL** is a readiness-aware elastic RL system with three components: **Continuous Task Batching (CTB)** preserves useful rollout state; **Resource-Aware Ref-Actor Pipelining (RA²P)** selects between decoupled streaming and colocated aggregation based on the ready backlog and arrival interval; **Elastic Resource Scaling (ERS)** moves ranks between rollout and training using the same readiness signals. Across text-only and multi-modal agentic workloads, TideRL improves RL training goodput by **up to 5.6× over synchronous baselines and >33% over asynchronous baselines** at similar task performance, improves **KV cache hit rate by 1.58×**, cuts per-step training time by up to **44.3%**, and reduces total waiting time by up to **77.6%**.
- **Key innovations**: (1) Readiness as a first-class scheduling signal for elastic agentic RL; (2) CTB (state-preserving batching) + RA²P (adaptive ref/actor pipelining) + ERS (rank elasticity); (3) large measured wins: 5.6× goodput vs synchronous, 1.58× KV hit rate.

---

## 4. Agents & Coding

### 4.1 Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding

- **arXiv**: [2608.11095](https://arxiv.org/abs/2608.11095) (cs.AI / cs.LG / cs.SE; submitted 2026-08-11) — **NEW**
- **Authors**: Kushal Chakrabarti
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: Agentic-coding READMEs like CLAUDE.md grow without bound in real repositories, stopping only when the repo retires or someone rewrites the file wholesale. The paper traces this to **imperfect recall**: appending an instruction is always cheap, but once an instruction's rationale is gone, deleting it without risking a correctness regression costs **O(2^|D|)** in a prompt of |D| instructions. The resulting divergence is named **catastrophic remembering** — the inverse of the catastrophic forgetting around which continual learning is organized. Characterization across **247,694 instruction lifetimes in 1,867 repositories**: agentic prompts grow without bound, more than tripling over their lifetime (**+226%**), gaining +4.9 net instructions every commit; the older an instruction gets, the less likely it is to be deleted (log-hazard **−0.032/commit**). Then: **prompt comments can halt the growth** — inverting IFEval yields verifiable worlds with known-optimal prompts, and comments encoding latent reasoning remove **99.3% of excess instructions** (+211.3% → +1.4%). Applying the same inversion to WildIFEval, prompt comments improve real-world agentic instruction-following by up to **23.1%**. Closing line: "If English is the new code, why don't we have comments yet?"
- **Key innovations**: (1) Formalizes prompt bloat as catastrophic remembering (inverse of catastrophic forgetting) with a cost argument for deletion; (2) large-scale empirical characterization (247k instruction lifetimes, +226% growth, delete-hazard decay); (3) a concrete fix — rationale comments — validated on inverting IFEval and WildIFEval.

---

## 5. Reasoning & Verification

### 5.1 VERDICT: Training-Free Step-Wise Verification of Multimodal Reasoning via Disagreement-Aware Consensus

- **arXiv**: [2608.10665](https://arxiv.org/abs/2608.10665) (cs.AI / cs.CV / cs.GT; ECCV 2026; submitted 2026-08-11) — **NEW**
- **Authors**: Rohit Sinha, Kunal Tilaganji, Tanuja Ganu, Nagarajan Natarajan, Amit Sharma, Vineeth Balasubramanian
- **Institution**: Microsoft Research India (Ganu, Natarajan, Sharma — high confidence, well-known affiliations) / IIT Hyderabad (Balasubramanian — high confidence).
- **Abstract (faithful summary)**: Multimodal LLMs often generate reasoning chains with subtle errors. Existing verification approaches either require expensive labelled supervision with inconsistent cross-task performance, or aggregate scores from multiple sources by simple averaging — missing the insight that **when scores disagree, disagreement itself carries information** about whether a step is valid. The paper formalizes this as a **coupled scoring problem among disparate, frozen verifiers**, interpretable as a coordination game with a unique closed-form equilibrium where agreement signals valid steps and disagreement reveals instability. **VERDICT** (VERification via Disagreement-Informed Coupled Thresholding) is a **training-free, domain-agnostic** step-wise verifier that makes cross-modal disagreement structure explicit and actionable, computing consensus scores in closed form for both disagreement-aware filtering and stability-conscious ranking. Across six benchmarks it improves over the base model by **up to +5.95%**, performing competitively with domain-specific critics that require extensive supervision.
- **Key innovations**: (1) Disagreement-as-signal formalized as a coordination game with a closed-form equilibrium; (2) the first training-free verifier to make cross-modal disagreement explicit; (3) competitive with supervised domain critics without task-specific adaptation.

---

## 6. Games, Game Theory & Mechanism Design

### 6.1 Safe Observation Capacity for Opponent Exploitation under Showdown Censoring

- **arXiv**: [2608.09954](https://arxiv.org/abs/2608.09954) (cs.GT; submitted 2026-07-20) — **NEW**
- **Authors**: Jiaxing Guo
- **Institution**: Imperial College London (stated on abstract page).
- **Abstract (faithful summary)**: In poker-like games, folds hide private cards, so **showdown data are missing not at random**; the usual per-card estimator converges to a selected distribution and its confidence sets can lose coverage as the sample grows. A **floor-safe probe** changes the monitoring process: it drives a chosen line to showdown, reveals every non-fold continuation, and uses sequence-form flow to recover censored fold mass on reveal-certified histories. The paper prices this repair via **safe observation capacity κ_ρ(I)** — the largest floor-safe reach rate at safety budget ρ — whose frontier is concave and piecewise linear with origin slope equal to the floor's shadow price. Matching bounds give a conditional per-target cost **N = Θ̃(1/(κ_ρ(I)·π·ε²))** for a local censored-fiber direction. **Safe Active De-censoring (SAD)** combines capacity with public-anomaly routing and robust deployment (routing across targets remains heuristic). Evidence spans bucketed turn-river endgames, controlled instances, and a fixed-board unbucketed river subgame where a constructed public twin admits a floor-safe response of value **V=0.815**; the audited public channel certifies only the blueprint floor, while population reveal evidence certifies **≥96% of V**. Across a broader synthetic opponent population, public and solved grouped reveal fibers certify median shares of **73% and 91%** of the safe-exploitable gap. Independent floor audits cover every evaluated probe and response.
- **Key innovations**: (1) Formalizes the censoring bias in showdown-based opponent exploitation and its repair via floor-safe probes; (2) safe observation capacity as a frontier with an associated shadow-price interpretation and sample-complexity bound; (3) separates unconditional safety from the conditional statistical value of active reveal.

### 6.2 Evaluating Rational Contracting in Natural Language (ContractSim)

- **arXiv**: [2608.10475](https://arxiv.org/abs/2608.10475) (cs.AI / cs.CL / cs.GT; submitted 2026-08-11) — **NEW**
- **Authors**: Bhavyesh Sajja, Max Kleiman-Weiner, Roger Zimmermann, Tan Zhi-Xuan
- **Institution**: Not stated on abstract page (Tan Zhi-Xuan and Max Kleiman-Weiner have MIT affiliations; single-source, tentative).
- **Abstract (faithful summary)**: Language-based AI agents promise to transform machine economic activity — negotiating and executing agreements in open-ended natural language rather than proposing bids or following hard-coded protocols. But most evaluations focus on one-off exchanges or simple economic games, leaving out time-extended, contingent, and incomplete contracts; they also measure raw profit without the qualities required for **trustworthy** contracting. The paper formulates a rational framework for how agents should negotiate and perform natural-language contracts in uncertain multi-step environments, with metrics and baselines for rational and cooperative play. **ContractSim** instantiates it: two players negotiate and execute a multi-turn supplier contract under environmental and inter-player uncertainty. Across six environments and three supplier settings (catering, hotel cleaning, AI hosting): current LLM-based agents **reach agreement reliably and negotiate efficiently when environmental uncertainty is low**, but under high uncertainty they often fail to negotiate satisfiable, efficient, or mutually beneficial contracts, and they are **frequently uncooperative during execution** — violating terms for extra profit even when contracts are easy to satisfy.
- **Key innovations**: (1) A rational-contracting evaluation framework spanning time-extended, contingent, incomplete contracts (not just one-shot games); (2) ContractSim, a multi-turn supplier-negotiation suite across six environments; (3) evidence that LLM agents are reliable negotiators but unreliable executors — a concrete gap for agentic-commerce design.

---

## 7. Time Series & Probabilistic Forecasting

### 7.1 TORF: Two-stage Odd Residual Flows for Mean-Preserving Probabilistic Forecasting

- **arXiv**: [2608.11114](https://arxiv.org/abs/2608.11114) (cs.LG / cs.AI; submitted 2026-08-11) — **NEW**
- **Authors**: Kiran Madhusudhanan, Christian Klötergens, Lars Schmidt-Thieme, Vijaya Krishna Yalavarthi
- **Institution**: University of Hildesheim (tentative — well-known affiliation of Lars Schmidt-Thieme; verify in paper).
- **Abstract (faithful summary)**: Probabilistic forecasting is essential for risk-sensitive long-horizon decisions, but existing approaches trade off distributional flexibility against accurate mean prediction: parametric methods like MVE can degrade point accuracy under joint NLL objectives, while flexible generative models (Normalizing Flows, Diffusion Models) rely on costly Monte Carlo sampling and may give suboptimal means. **TORF** decouples the two: stage one uses a pre-trained deterministic model for an accurate point (mean) forecast; stage two fits a **Restricted Normalizing Flow with strictly odd functions** to learn a flexible residual distribution around the point forecast, **guaranteeing mean preservation from stage one without sampling**. Experiments show TORF achieves state-of-the-art deterministic accuracy (NMAE) while providing strong density estimation (CRPS) on short- and long-horizon forecasting.
- **Key innovations**: (1) Clean two-stage decoupling of mean and uncertainty, fixing the NLL-vs-point-accuracy trade-off; (2) odd-function-restricted flows that are mean-preserving by construction and need no sampling; (3) SOTA point accuracy (NMAE) plus strong CRPS simultaneously.

### 7.2 RCCP: Retrieval-Corrected Conformal Prediction for Time Series

- **arXiv**: [2608.10553](https://arxiv.org/abs/2608.10553) (cs.LG / cs.AI; CIKM 2026; submitted 2026-08-11) — **NEW**
- **Authors**: Sangjin Jin, Kangmin Kim, Junhyeong Lee, Yongjae Lee
- **Institution**: Not stated on abstract page (CIKM '26, Rome).
- **Abstract (faithful summary)**: Conformal prediction (CP) gives distribution-free prediction intervals for fixed forecasters, but standard calibration is inefficient for time series where forecast errors are temporally dependent and nonstationary. Recent time-series CP methods improve local calibration with recent/weighted/localized residuals, yet local calibration stays indirect — broad residual weighting can dilute the evidence most relevant to the current prediction. **RCCP** (Retrieval-Corrected Conformal Prediction) selects **similar past residuals as local evidence** (retrieval), then **corrects the coverage error left by retrieval** with a scalar conformal correction: an asymmetric interval is built from retrieved one-sided residuals, and a conformal correction calibrates its normalized retrieval error. A coverage-gap bound is derived from the stability of the normalized retrieval error distribution. Across standard benchmarks and backbone forecasters, RCCP attains target coverage in every setting, achieves the **lowest Winkler scores** with fewer severe misses, and has low calibration/inference overhead. Code: github.com/jinsaaang/rccp.
- **Key innovations**: (1) Retrieval + conformal correction as two complementary steps (local evidence, then coverage calibration); (2) coverage-gap bound tied to retrieval-error stability; (3) SOTA Winkler scores with target coverage in every setting, at low overhead.

---

## Cross-cutting trends

- **Industrial recommender systems are going LLM-native, and shipping it.** Three production papers in one batch — Netflix GenRec (context-engineering replacing feature engineering, prefill-only serving), Meta ConnectionMind (graph reasoning + SFT→RL, +0.43% watch time online), and LinkedIn MARCO (click-intent decomposition fixing a calibration blind spot, +2.80% conversions/click) — mark the shift from discriminative rankers with thousands of engineered features to LLM-backed rankers as a live, A/B-tested production reality.
- **Efficiency work is moving from "how to compress" to "what to allocate".** ReRound (quantization) and UniF-MoE both treat low-bit/low-compute decisions as allocation problems with explicit mechanisms (midpoint disambiguation via diffusion reconstructions; shared-blocks-then-route-remainder via KV-channel analysis), while MOSAIC argues the right sparsity only exists once **systems constraints** are in the loop — an emerging "co-design, not separate stages" theme for frontier training.
- **Post-training supervision gets reliability-aware and goodput-aware.** ReOrder-OPD upgrades OPD from local confidence heuristics to a prompt-level teacher-continuation reliability ordering; TideRL attacks the other side of the same problem — rollout/training scheduling — with readiness-aware elasticity (5.6× goodput). Both address the *sample-quality and utilization* bottlenecks of agentic/post-training RL that dominated the Aug 10–11 digests.
- **Agentic-prompt engineering is being studied as an empirical phenomenon.** "Catastrophic remembering" gives a name, a mechanism (asymmetric deletion cost, O(2^|D|)), and large-scale evidence (+226% prompt growth over 1,867 repos) to the CLAUDE.md-bloat problem — plus a cheap fix (rationale comments, −99.3% excess instructions in inverted IFEval). Highly relevant to this wiki's own operating practice.
- **Verification and trust remain the binding constraint on agentic economics.** VERDICT shows disagreement among frozen verifiers is itself a usable training-free signal (ECCV 2026), and ContractSim finds LLM agents negotiate well but defect during execution under uncertainty — directly extending the oversight/economics threads (Sharding, Auctioning Attention) from the Aug 10 scan.
- **Time series forecasting is standardizing around calibrated, uncertainty-aware backbones.** TORF (mean-preserving residual flows) and RCCP (retrieval+conformal, CIKM 2026) both deliver SOTA point accuracy and calibrated intervals simultaneously — the two-sided quality bar (NMAE + CRPS / Winkler) that earlier single-objective models failed.

## Methodology & caveats

- Papers selected from the Wed Aug 12, 2026 arXiv announcement batch across the requested domains (AI, LLM, agents, coding, recommendation, advertising/CTR, games, mechanism design, sequential/time series). The batch spans cs.LG 164 / cs.CL 95 / cs.IR 22 / cs.GT 9 / cs.SE 22 / cs.MA 14 / cs.AI 211 new. Note: the arXiv **export API was rate-limited** from this network, so discovery used web listing pages (`arxiv.org/list/<cat>/recent`); cs.LG (first 50 of 164 titles) and cs.AI (first 100 of 211 titles) were only partially scanned at title level, so some strong candidates in those streams may be missed. All 14 selected papers' metadata was verified against individual abstract pages (`arxiv.org/abs/<id>`).
- **Zero-overlap verification**: every candidate arXiv ID grep-checked across wiki/index.md, wiki/log.md, and wiki/synthesis/** before inclusion — 0 hits each. Prior-day coverage: the 2026-08-11 arxiv-daily / arxiv-paper-check / game-rl-daily / conference-digest covered IDs up to 2608.09930; every paper in this report is ≥ 2608.09954. This is the first 2026-08-12 output, so same-day paper-check (cs.AI+cs.IR) and game-rl-daily coverage — where they would normally claim cs.IR/cs.AI papers — did not yet exist at time of writing; the three industrial rec/ads papers (2608.10562, 2608.10257, 2608.10187) are therefore included here rather than deferred.
- Institution/company attribution: **high confidence** where stated in the abstract (Netflix, Meta, Imperial College London) or well-known affiliations (H. T. Kung → Harvard; C. L. Philip Chen → University of Macau; Jie Tang → Tsinghua; MSR India / IIT Hyderabad); **tentative** where inferred from a single co-author (LinkedIn for MARCO; MIT for ContractSim; Hildesheim for TORF). No affiliation should be treated as authoritative without checking the paper.
- Submission-date caveat: 2608.09954 (Safe Observation Capacity) is listed as submitted 2026-07-20 but appears in the Wed Aug 12 cs.GT listing; it is new to the wiki (0 hits).

## Related pages
- [arXiv Daily Digest (August 11, 2026)](../2026-08-11/arxiv-daily.md) — prior breadth pass (IDs up to 2608.09930)
- [arXiv Paper Check — AI & CTR (August 11, 2026)](../2026-08-11/arxiv-paper-check.md) — prior CTR/Rec/Ads curation
- [Game RL & Game AI Bot — Daily Synthesis (August 11, 2026)](../2026-08-11/game-rl-daily.md) — prior game RL/world-model curation
- [arXiv AI Research Search (August 10, 2026)](../2026-08-10/arxiv-ai-search.md) — the template for this report; prior AI scan (Mon Aug 10 batch)
