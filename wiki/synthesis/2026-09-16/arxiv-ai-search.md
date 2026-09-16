---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-09-16
updated: 2026-09-16
sources: [arxiv.org]
tags: [arxiv, AI, LLM, recommendation, advertising, sequential-modeling, CTR, game-AI, agents, world-models, SSM, gating, inference-efficiency, KV-cache, ternary-LLM, test-time-RL, multi-agent, auction-design, mechanism-design, daily-digest]
---

# arXiv AI Research Paper Search Report — 2026-09-16

Generated: 2026-09-16 (Wednesday). Fresh window = the **Wed 16 Sep 2026 mailing** (Tue 15 Sep submissions). The `/list/{cat}/new` pages now headline *"Showing new listings for Wednesday, 16 September 2026"* — the batch of IDs **2609.16004 → 2609.17527** observed live in the fresh listing. All **22 featured papers verified 0 hits in `wiki/`** at grep-verification time.

**Methodology**: The public arXiv API (`export.arxiv.org`) remained rate-limited (429) across the window, so this run used direct page fetches of the `/list/{cat}/new` listing pages for **cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, econ.TH** (cs.CY stayed on hard rate-limit after retries) plus ~50 targeted `abs/{id}` fetches for the screened shortlist. Probe HTML was cached under the pre-approved temp dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/` and cleaned up after the report landed. Every featured ID below was grep-verified **0 hits in `wiki/`** prior to writing.

**Dedup notice**: The sibling [`arxiv-daily` (2026-09-16)](arxiv-daily.md) ran earlier against the pre-batch *Tuesday 15 Sep* listing (its own max ID **2609.15989**, zero `2609.16xxx` IDs on disk), so the two reports are disjoint by construction. All featured IDs ≥ 2609.16004 also sit above the 09-15 arxiv-ai-search / arxiv-paper-check / game-rl-daily coverage ceiling (2609.15996). One indexing correction: 09-15 declared the frontier "≥ 2609.16000 empty"; 09-15's arxiv-paper-check subsequently established that 2609.16000 is itself an *older* online record (announced 2026-07-23), and the genuinely fresh Wed-16 numbering starts at 2609.16004 in today's `/new` listing.

## Summary Statistics

| Scope | Value |
|---|---|
| Window covered | Wed 16 Sep 2026 mailing (Tue 15 Sep submissions); IDs 2609.16004–2609.17527 observed live |
| Categories parsed | cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, econ.TH (cs.CY rate-limited at write time) |
| Fresh beyond 09-15 max (2609.15996) & 09-16 arxiv-daily max (2609.15989) | entire window |
| Featured in full in this report | 22 |
| Direct CTR / advertising papers | **1** (ROI-constrained auction design) + ad-adjacent production ranking/marketplace (see ADS/CTR note) |
| Recommendation / marketplace papers | 5 dedicated (A1–A5) + 1 rec-adjacent runner-up (multimodal gen-rec) |

**Advertising/CTR note**: After four consecutive ~empty windows, the Wed 16 Sep batch **breaks the arXiv ads/CTR noise floor**: a direct ad-auction theory paper (ROI-constrained bidders, A5), plus production-flavored ranking/marketplace content with online numbers (Wolt UVR delivery ranker A1, Facebook Marketplace PCap A2, streaming-platform AURA A3, ReliGRec A4), and an industrial pCVR runner-up (QueryFormer, KDD Cup 2026 Tencent UniRec). This is still not the conference-batch level of CTR ML, but the daily arXiv pipeline now has genuine ad-ranked content again.

---

## 1 Recommender Systems, Marketplaces & Advertising

### 1.1 Balancing Trial and Reorder — UVR Hybrid Sequential Transformer-GBDT Ranker (2609.16407)
- **Title**: Balancing Trial and Reorder: A Hybrid Sequential Transformer-GBDT Ranker for On-Demand Delivery
- **Authors**: Marcel Kurovski, Attila Nagy, Steffen Klempau, Aleksandr Fedintsev
- **Institution**: **Wolt** (production delivery platform — stated in abstract)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16407
- **Abstract**: On a delivery platform, personalized store ranking is local and bound by real-time availability and delivery operations. The central modeling tension is surfacing new stores for *trial* while preserving ranking quality for *reorder*-intent sessions. **Universal Venue Ranker (UVR)** pairs a bidirectional transformer encoder for sequential user modeling with a GBDT ranker across contextual/user/store features. Trained across all stores and domains of a country under local delivery constraints at inference, it replaces **four separate ranking models** (three restaurant + one retail) with one unified system. Label smoothing + trial-biased sample weighting steer toward new stores: offline trial MRR +12% to +30% over production across countries while reorder MRR regresses in five of six countries — leaving Global CVR, the core online metric blending both session types, statistically unchanged. **Three consecutive A/B tests**: V1 (two largest markets) **+5.5% Merchant Trial Rate / +0.16% Global CVR**; V2 adds **+0.45% Merchant Trial Rate**; V3 (full cross-domain restaurant+retail unification) adds **+1.31% Retail Merchant Trial Rate** — substantial incremental gross order value and a materially simplified serving stack.
- **Key Innovations**: (1) one unified cross-domain venue ranker replacing four per-domain models; (2) trial-vs-reorder balance as a first-class training choice (label smoothing + trial-biased weights); (3) GBDT+bidirectional-transformer hybrid in live delivery with documented A/B lifts.
- **Venue**: Preprint.

### 1.2 PCap — Personalized Retrieval-Stage Diversity Capping in Facebook Marketplace (2609.16452)
- **Title**: PCap: Personalized Retrieval-Stage Diversity Capping in Facebook Marketplace
- **Authors**: Guangchao Yuan, Janis Fuh, Christopher Choate, Xun Tang, Wenqi Zhu, Chengyi Zhang, Pavan Kumar Paalya Chandrashekar, Jiang Han, Jiangyuan Li, Hongyan Wang, Shuting Wang
- **Institution**: **Meta** (Facebook Marketplace — stated)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16452
- **Abstract**: Proposes **PCap**, a personalized capping framework adding user-level diversity constraints at the **retrieval stage** (not re-rank): models individual diversity preferences via **Shannon entropy-based scoring**, segments users into diversity buckets, and applies personalized category caps during multi-source candidate retrieval. The high-dimensional per-bucket cap space is navigated with an automated online optimization method, **Parameter Tuning Sequence**. Large-scale online experiments show significant browsing-engagement improvements; the paper positions this as a practical recipe for integrating personal diversity into industrial retrieval.
- **Key Innovations**: (1) diversity enforced at retrieval (before ranking) rather than post-hoc; (2) entropy-scored user-level diversity buckets with per-bucket category caps; (3) automated online parameter tuning (PTS) for the cap grid.
- **Venue**: Preprint (5 pages).

### 1.3 AURA — Agentic Diagnosis and Refinement for Production Recommender Systems (2609.16625)
- **Title**: AURA: Agentic Diagnosis and Refinement for Production Recommender Systems at Scale
- **Authors**: SungGeun Kim, Abhinav Narain, Daniel Nemirovsky
- **Institution**: Major media-streaming company (author-affiliation inferred: Microsoft-aligned; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16625
- **Abstract**: Practitioners often improve recsys against stakeholders/metrics without understanding *where and why* recommendations fail for end users. **AURA (Agentic Understanding and Refinement of recommender Algorithms)** is an end-to-end agentic system that (1) performs qualitative failure evaluation at scale — specialized agents read production engagement logs (thousands to millions of sessions) and surface patterns/examples of real-user failure; (2) generates **code-level refinements** grounded in the recommender's own code, data, and training pipeline. Reports system design, initial production tests on **two large consumer platforms at a major media-streaming company**, safeguards and operational learnings, toward a self-improving recommender. The diagnostic gap is argued transferable (the config layer already ported it across the two platforms), with a concrete mapping to e-commerce/online-retail recommendation.
- **Key Innovations**: (1) agentic qualitative diagnosis as a first-class recsys practice (vs aggregate metrics only); (2) code-level, corpus-grounded refinement proposals back into the production pipeline; (3) a transferable agent architecture across platforms/domains.
- **Venue**: Accepted at **GenAIECommerce'26** (Third Workshop on Agentic and Generative AI for E-Commerce).

### 1.4 ReliGRec — Reliability-Oriented LLM-Based Generative Recommendation via User-Risk-Aware Prompt Routing (2609.16560)
- **Title**: ReliGRec: Reliability-Oriented LLM-Based Generative Recommendation via User-Risk-Aware Prompt Routing
- **Authors**: Haoran Yang, Fei Chen, Yutian Xiao, Jiahao Liang
- **Institution**: — (not stated; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16560
- **Abstract**: User behavior in real recsys is heterogeneous — coherent preferences vs abrupt shifts, bursty interactions, repetition, or collaborative-neighborhood inconsistency — which may be benign variation or manipulation (shilling) but does not *alone* establish intent. Prior robust recommenders re-weight training or aggregate graphs; ReliGRec instead adapts *generation* to estimated user-level weak risk. It derives weak-risk proxy labels from review-feedback signals, represents sequential behavior with a **Behavior Token** and collaborative context with temporal **Graph Tokens**, and a **Dual-View Weak-Risk Estimator** selects a *Simple* vs *Cautious* prompt at inference. The Cautious prompt steers generation toward stable, collaboratively-supported evidence and away from isolated/short-term/repeated interactions. Reports competitive recommendation + proxy prediction, and routing analyses characterize the quality/cost behavior of risk-guided prompting.
- **Key Innovations**: (1) weak-risk estimation becomes a generation-time *control signal* (prompt routing), not just an auxiliary prediction; (2) behavior+graph token fusion under a dual-view estimator; (3) shilling-adjacent robustness recast for LLM generative recommendation.
- **Venue**: Preprint.

### 1.5 Auction Design with ROI-Constrained Bidders: Truthfulness and Revenue Maximization (2609.16522)
- **Title**: Auction Design with ROI-Constrained Bidders: Truthfulness and Revenue Maximization
- **Authors**: Zhiqiang Zhuang, Quan Yu, Yisong Wang, Kewen Wang, Zhe Wang
- **Institution**: Chinese-Australian academy-aligned (Zhuang/Wang group; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16522
- **Abstract**: The **ROI constraint is central to many auctions, particularly online advertising**, where a bidder won't pay more than a fixed fraction of value obtained. Studies truthful, revenue-maximizing auctions for ROI-constrained bidders. **First result**: characterization of truthful auctions when both valuations *and* ROI constraints are private — the allocation rule **uniquely determines the payment rule**. **Second**: multi-bidder **σ-increment mechanisms** resembling Myerson's optimal mechanism; as σ→0 they become asymptotically optimal among deterministic truthful mechanisms, and revenue approaches at least a **1/r̄ fraction** of optimal expected revenue over *all* truthful mechanisms (r̄ = largest possible ROI). **Third**: single-bidder setting — every truthful auction can be replaced by a convex pricing function with weakly higher payments for every type, with optimal pricing functions derived for public-valuation or public-ROI cases.
- **Key Innovations**: (1) private ROI constraints + valuations with a truthful-characterization-style allocation→payment determinacy; (2) Myerson-adjacent σ-increment mechanisms with asymptotic optimality fractions; (3) convex-pricing equivalence for the single-bidder ROI case — directly relevant to ad-platform auction theory.
- **Venue**: Preprint.

---

## 2 Sequential Models, SSMs & Linear Attention

### 2.1 Anatomy of Associative Recall in Fixed-State Recurrences (2609.16183)
- **Title**: Anatomy of Associative Recall in Fixed-State Recurrences: A Matched-State Decomposition, an Interference Wall, and a Curriculum That Breaks It
- **Authors**: Julian Boesch, Andrew Wee
- **Institution**: — (independent/research-lab affiliated; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16183
- **Abstract**: "Recurrent models are bad at recall" is the standard story, but whole-architecture comparisons can't say which ingredient is responsible. The authors decompose masked multi-query recall at a fixed state budget along three single-knob axes: short causal convolution, transition structure (rank-1 delta vs diagonal), and decay. Findings: (1) **the convolution dominates (~+0.5 recall in both families)** — convolution-free cells vs convolution-equipped Mamba measure the missing convolution, not the recurrence; (2) rank-1 beats diagonal by +0.19/+0.32 at 16/32 pairs, collapsing to +0.03 once both carry the convolution (state-matched Mamba-2 ties); (3) cells solving 32-pair recall **fall to chance retrieving 4 pairs from a distractor haystack** — an **interference wall under sparse supervision, not capacity**: a distance curriculum takes the *unchanged* architecture from 0.021 → 1.000. Training is a lock-in lottery (a seed locks in or does not): curriculum lifts lock-in 1/10 → 7/10 (p=0.02), dense supervision adds nothing; at L=512 where the ramp collapses, **gating it on measured accuracy locks in 6/6** (p=0.001). Arming for recall is free on an S₅ state-tracking guardrail.
- **Key Innovations**: (1) matched-state decomposition identifying the convolution (not the recurrence) as the recall driver; (2) interference-wall diagnosis (sparse supervision ≠ capacity) with a distance curriculum that flips 0.02→1.00; (3) practical "lock-in" recipe (curriculum + gating) for training linear-time models on hard recall.
- **Venue**: Preprint (preliminary results; code released).

### 2.2 On the Importance of Gating: Memorization vs. In-Context Learning in SSMs (2609.16540)
- **Title**: On the Importance of Gating: Memorization vs. In-Context Learning in State Space Models
- **Authors**: William L. Tong, Aryo Lotfi, Emmanuel Abbe, Kostas Vaggelakos, Vishnu Banna, Etai Littwin, Josh Susskind, Cengiz Pehlevan, Eran Malach
- **Institution**: Apple / MIT / Harvard / Hebrew University-aligned (author-affiliation inferred: Littwin/Susskind/Vaggelakos/Banna — Apple; Abbe — MIT; Pehlevan — Harvard; Malach — HUJI)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16540
- **Abstract**: SSMs lag Transformers on in-context learning (ICL) and precise retrieval, slowing large-scale LM adoption. This work explains both success and failure through the **gating mechanism** — a prevalent component in modern recurrent networks. Theoretically and empirically: gating causes SSMs to **first learn an in-weights "memorization" solution while delaying, or even preventing, convergence to the correct ICL solution** — even when there is no fundamental architectural or memory-capacity limitation. Conversely, gating **benefits generalization to longer sequence lengths**. This illuminates the role of gating in both training dynamics and generalization of SSMs, and gives a basis for understanding/improving linear-time models.
- **Key Innovations**: (1) gating as the causal lever (not recurrence) for the SSM ICL gap; (2) theory + experiments on memorization-first training dynamics under gates; (3) the memorization-ICL vs length-generalization trade-off as an actionable design knob.
- **Venue**: Preprint (25 pages).

### 2.3 What Does Layer-Importance Reveal About Transformers and State-Space Models? (2609.16537)
- **Title**: What Does Layer-Importance Reveal About Transformers and State-Space Models?
- **Authors**: Istabrak Abbes, Nizar Islah, Irina Rish, Sarath Chandar
- **Institution**: Mila-affiliated (Rish, Chandar — Université de Montréal/Polytechnique Montréal; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16537
- **Abstract**: How far does analytical knowledge built for Transformers transfer to SSMs? Studying **layer importance** (which underpins compression, selective fine-tuning, interpretability), decomposes it into two distinct notions: **Necessity** (loss increase from bypassing a layer = dependence on existing contribution) and **Plasticity** (where task-specific weight updates absorb new info). Two families behave fundamentally differently: in every evaluated residual transformer up to 14B, **Necessity and Plasticity anti-align across depth**, whereas in Mamba-style SSMs they point to **overlapping regions**. The sign of this alignment predicts downstream adaptation: in transformers, concentrating updates in the most plastic layers *increases catastrophic forgetting*, while this tier-dependent effect disappears in Mamba-style SSMs.
- **Key Innovations**: (1) Necessity-vs-Plasticity decomposition as a portable lens across architecture families; (2) measured anti-alignment (transformers) vs overlap (SSMs) across depths; (3) alignment sign predicts transfer/catastrophic-forgetting behavior during fine-tuning.
- **Venue**: Preprint.

---

## 3 Inference Efficiency: Flash Compute, Ternary Weights & KV Eviction

### 3.1 LLM Inference in a Flash! (2609.16161)
- **Title**: LLM Inference in a Flash!
- **Authors**: Sebastian Zhao, Minseo Kim, Coleman Hooper, Luca Manolache, Michael W. Mahoney, Yakun Sophia Shao, Kurt Keutzer, Amir Gholami
- **Institution**: UC Berkeley-aligned (Sky Computing / BAIR; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16161
- **Abstract**: Serving demands shift toward longer sequences and heavier inference (RAG, inference-time compute scaling, long context), while memory capacity and communication bandwidth don't scale as fast. **Compute-in-Flash** moves computation close to memory and exploits large SSD capacity — but these devices lack high-precision float support and have limited write endurance. This work designs inference algorithms for Flash compute-in-memory devices: (1) an **end-to-end integer-only quantization** approach eliminating expensive float compute; (2) for write endurance, a **dictionary-based KV-cache compression** (sparse dictionary coding: each KV vector as a linear combination of static dictionary vectors). Both model weights and KV cache live in Compute-in-Flash, minimizing data transfer. Across Llama-3.1-8B and Qwen-2.5-7B, the combined method shows limited accuracy degradation while cutting **dynamic KV-cache traffic 15×**.
- **Key Innovations**: (1) integer-only, write-endurance-aware inference for compute-in-memory Flash; (2) sparse-dictionary KV compression fit for limited-endurance media; (3) 15× KV traffic reduction with bounded accuracy loss on 7–8B open models.
- **Venue**: Preprint.

### 3.2 Breaking the 1.58-bit Barrier for Ternary LLMs (2609.16338)
- **Title**: Breaking the 1.58-bit Barrier for Ternary LLMs
- **Authors**: Evangelos Georganas, Alexander Heinecke, Pradeep Dubey
- **Institution**: **Intel Labs** (stated affiliation: Intel)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16338
- **Abstract**: Ternary LLMs store weights ∈ {−1,0,+1}; cost is referenced to the information-theoretic log₂3 ≈ 1.585 bits/weight, and the prevailing five-trit-per-byte packing rounds up to 1.625 bpw. This treats symbols as equiprobable; the authors measure the actual symbol distribution of **29 ternary LLMs** and find zeros up to **51.5%** of weights. **BITCOS**, a distribution-adaptive layout (dense presence bitmap + compacted sign vector), costs **2−z bits/weight** given zero density z. It beats five-trit packing in 26/29 tested models, hitting **1.485 bpw** on the sparsest. BITCOS unpacks efficiently on AVX-512/AVX2/Intel Xe2 GPUs; measured against production SOTA ternary mat-vec kernels, realized gain is up to **1.28×**, and end-to-end decode throughput improves **up to 1.18× on CPUs and 1.27× on GPUs** across 5 platforms.
- **Key Innovations**: (1) measured zero-density structure (up to 51.5%) across 29 ternary models as the design driver; (2) BITCOS 2−z layout undercutting the 1.585bpw "barrier" (1.485 in practice); (3) production kernels + end-to-end decode numbers on client/server CPU and i/dGPU.
- **Venue**: Preprint.

### 3.3 Divergence Timing and Cumulative Disagreement under KV-Cache Eviction (2609.16617)
- **Title**: Divergence Timing and Cumulative Disagreement under KV-Cache Eviction
- **Authors**: Xinyue Luo, Fei Yu
- **Institution**: — (Chinese academy-aligned; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16617
- **Abstract**: KV-cache eviction perturbs the conditional token distributions governing autoregressive generation. This work investigates how *first-divergence timing* and subsequent token mismatch determine *cumulative disagreement*. Derives an **exact decomposition under stepwise maximal coupling**: expected mismatch fraction = first-mismatch contribution + post-divergence exposure × its mismatch rate. An explicit construction over unrestricted autoregressive kernel pairs realizes the sharp interval of risks compatible with a finite divergence-aligned observation window. **Residual-branch conditional Monte Carlo** provides unbiased joint estimates of occurrence/occupation/window/tail contributions. On complete Meta-Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct trajectories: **SnapKV at 50% retention enters divergence later and less often** than SnapKV-512 or recent-token retention at the same budget, while post-divergence TV stays high — and across 288 documents, **post-divergence exposure accounts for 85–90% of aggregate mismatch gaps**.
- **Key Innovations**: (1) first-mismatch / post-divergence-exposure decomposition formalizing "fast sample path vs slow total loss" intuition; (2) stepwise-maximal-coupling exactness + sharp risk-interval construction; (3) Monte-Carlo estimation methodology for eviction-fidelity auditing.
- **Venue**: Preprint.

---

## 4 LLM Post-Training, Test-Time RL & Reward Integrity

### 4.1 Rewarding Reasoning, Not Answers — Fixing and Bounding Test-Time RL on Medical QA (2609.16660)
- **Title**: Rewarding Reasoning, Not Answers: Fixing and Bounding Test-Time Reinforcement Learning on Medical QA
- **Authors**: Kailong Fan, Anqi Pu, Yichen Wu, Wanhua Li, Yicong Li, Hanspeter Pfister, Huafeng Liu, Xiang Li, Quanzheng Li, Ning Guo
- **Institution**: MGH / Harvard-aligned (Quanzheng Li, Ning Guo — Mass General Brigham; Pfister — Harvard SEAS/Zhejiang; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16660
- **Abstract**: Test-time RL adapts a model on its own unlabeled test set via majority-vote pseudo-labels and shines in mathematics — but **collapses on medical multiple-choice QA**: accuracy stagnates while output diversity declines. A controlled experiment keeping questions/model/optimizer fixed while changing only the answer space traces failure to **answer-space structure**, not domain difficulty: small answer spaces let wrong rollouts collide on the same wrong pseudo-label and reinforce it; large answer spaces disperse and starve reward. This motivates **PROSE (Process Reward Guided Self-Training)**: a medical process reward model scores each reasoning step, the trajectory reward is the **minimum across steps**, and answer-format constraints are enforced. Without labels, PROSE substantially improves a general Llama model, **surpassing purpose-built medical models and matching much larger systems**; the process signal is internalized into the policy (no reward model needed at inference) and transfers to unseen datasets. **Min-aggregation is essential**: mean aggregation is exploitable, saturating the proxy reward while degrading accuracy.
- **Key Innovations**: (1) answer-space-structure diagnosis of TT-RL collapse (collision/starve regimes); (2) PROSE process-reward minimum-aggregation self-training without labels; (3) hard bound on reward-model exploitation via min-gating.
- **Venue**: Preprint.

### 4.2 ImpossibleRubrics — Stress-Testing Generated Rubrics as Reward Signals (2609.16816)
- **Title**: ImpossibleRubrics: Stress-Testing Generated Rubrics as Reward Signals
- **Authors**: Bowen Qin, Yi Xie, Yesheng Liu, Xi Yang
- **Institution**: — (not stated; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16816
- **Abstract**: LLM-generated rubrics are increasingly the reward signal for rubric-based RL, LLM-as-judge, and auto-grading — reliable only if they reward honest answers over adversarially-optimized answers. **ImpossibleRubrics** isolates the hardest regime: *impossible tasks* where the prompt pressures the model toward an unsupported conclusion, so the only honest answer acknowledges impossibility. Benchmark: **169 impossible tasks / 6 impossibility categories**, each with a verifiable oracle certificate, plus 48 answerable controls; rubrics are generated downstream and adversarially tested for rewarding certificate-violating answers. **Eleven generators are exploited 8–26%** of the time on the unbiased cut; on the stress cut the strongest generator is still exploited **36%** while a certificate-faithful rubric is exploited **0%** — a rubric-quality gap, not task impossibility. Counterintuitive result: a **single generic rubric ("be decisive, penalize hedging") is exploited 64%**, and seven of eleven generators underperform it while writing tailored rubrics — **the tailored criteria tell an attacker which claim to fabricate**. The problem is not that rubrics are vague; it is that they are specific about the wrong things.
- **Key Innovations**: (1) first benchmark isolating rubric robustness on impossible tasks with verifiable oracle certificates; (2) adversarial rubric exploitation quantified (8–64%+ across generator designs); (3) the "tailoring helps the attacker" inversion with a certificate-faithful 0%-exploitation baseline.
- **Venue**: Preprint.

### 4.3 Spurious Tool Use — When RL Agents Learn the Wrong Reason to Act (2609.16268)
- **Title**: Spurious Tool Use: When RL Agents Learn the Wrong Reason to Act
- **Authors**: Yiwei Yang, Haoxiang Zhang, Bingbing Wen, Yao Lu, Yuchen Wu, Lei Zhang, Julian McAuley, Pan Lu, Bill Howe
- **Institution**: UC San Diego-aligned (McAuley, Lu, Howe) + others; tentative
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16268
- **Abstract**: LLM agents interleave reasoning with tools (web search, code execution); tool-use policies are often optimized via RL, which can amplify spurious correlations in training data. Studies when/why RL-trained agents learn **shortcut tool-selection policies** (invoking tools from superficial prompt cues, not task requirements). In controlled synthetic environments combining factual QA and math reasoning, cues strongly correlated with specific tools but causally irrelevant are injected: in counterfactual evaluations (cue present, tool not needed), agents show substantial shortcut behavior — **spurious tool invocation up to +39%**. But shortcut formation is **not universal**: it arises only when the agent already reliably uses the target tool — task competence, not dataset imbalance, is a key factor. **Swapped-cue analysis** shows semantic cue–tool alignment amplifies the effect. A dense **tool-necessity reward** (an LLM judge scores each tool call) suppresses cue-driven tool use while preserving task performance.
- **Key Innovations**: (1) controlled disentanglement of spurious-cue tool use in RL agents with counterfactual + swapped-cue designs; (2) "requires prior competence" boundary condition on shortcut formation; (3) decision-level tool-necessity reward as a cheap, effective mitigation.
- **Venue**: Preprint.

### 4.4 Beyond Token-Local Imitation — Reward-Compatible Temporal Credit Assignment for On-Policy Distillation (2609.16937)
- **Title**: Beyond Token-Local Imitation: Reward-Compatible Temporal Credit Assignment for On-Policy Distillation
- **Authors**: Shiqi Liu, Zeyu He, Letian Tao, Guojian Zhan, Jiaxin Gao, Feihong Zhang, Jingliang Duan, Wei Xiong, Kehua Sheng, Bo Zhang, Yang Guan, Shengbo Eben Li
- **Institution**: Tsinghua / Huawei-aligned (Eben Li — Tsinghua SIGMA Lab; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16937
- **Abstract**: On-policy distillation (OPD) is effective for LLM post-training, but existing objectives trade objective fidelity off against optimization stability: token-level OPD is stable yet local; sequence-level OPD captures future credit at horizon-dependent variance. Establishes a **unified temporal-credit view**: practical token-level OPD ≈ a temporal approximation of the sequence-level reverse-KL gradient. Proposes **γOPD**: discounted temporal credit assignment balancing long-horizon supervision and stability, with a **horizon-independent variance bound**. A **reward-compatible bounded mixing (RBM)** mechanism balances verifiable outcome feedback with the discounted OPD advantage to move beyond purely teacher-dependent optimization. On math and code reasoning, γOPD+RBM consistently improves over existing OPD across vanilla, size-mismatched, and multi-teacher distillation settings.
- **Key Innovations**: (1) theory unifying token- and sequence-level OPD via a temporal-credit lens; (2) discounted-credit γOPD with provably bounded variance; (3) verifiable-reward mixing (RBM) decoupling from teacher-dependent signals.
- **Venue**: Preprint.

---

## 5 Game AI & World Models

### 5.1 AI for Games in the Foundation Model Era (2609.16679)
- **Title**: AI for Games in the Foundation Model Era
- **Authors**: Meng Luo, Yanlin Li, Hao Li, Hongzhan Lin, Pengfei Zhou, Tianjie Ju, Ran Zhang, Yeying Jin, Mong-Li Lee, Wynne Hsu
- **Institution**: NUS-affiliated (Lee, Hsu — National University of Singapore; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16679
- **Abstract**: Foundation models plus learned game-world models are reshaping AI across the game lifecycle — beyond playing, systems now *model players and game dynamics*, *support design and development*, *adapt player-facing experiences at runtime*, and *evaluate artifacts*. These directions evolved separately, obscuring which capabilities transfer. The survey organizes the literature into **six roles by immediate use of AI output**: playing/acting; modeling players and games; designing games; building/maintaining games; generating and adapting at runtime; testing/evaluating games. For each role it examines what structure the game/workflow supplies, what AI learns/produces, which capabilities and artifacts transfer, and what evidence supports the claims. Cross-role connections identified (trajectories train world models; learned environments train agents; design specs drive executable implementations; play/test feedback guides revision), but control schemes, rules, engine interfaces, state representations, and player contexts often stay setting-specific. Evaluation is most standardized for bounded game playing and selected learned environments; persistent state in learned worlds, repeated software revision, validated player modeling, sustained runtime adaptation, and representative automated testing remain less established.
- **Key Innovations**: (1) 120-page six-role taxonomy of FM-era game AI with transfer analysis; (2) evidence-audit of what transfers across roles vs what stays setting-specific; (3) explicit map of evaluation standardization gaps (persistent learned worlds, runtime adaptation, automated testing).
- **Venue**: Preprint (120 pages, project page).

### 5.2 World Models for Embodied Intelligence: From Plausible to Controllable to Actionable (2609.16697)
- **Title**: World Models for Embodied Intelligence: From Plausible to Controllable to Actionable
- **Authors**: Nanjie Yao, Hao Wang, Chong Cheng, Zhikang Chen, Wenzhe Li, Jiafei Lyu, Li Shen, Peilin Zhao, Zongqing Lu, Gao Huang, Steven Hoi, Dacheng Tao, Deheng Ye
- **Institution**: Tencent AI Lab / PKU / Tsinghua / NUS-aligned (Deheng Ye — Tencent; Zongqing Lu — PKU; Gao Huang — Tsinghua; Dacheng Tao — NUS/UTS; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.16697
- **Abstract**: World models connect perception and decision-making in embodied intelligence, but progress is often measured by visual fidelity while their value lies in improving behavior. Introduces three progressively stronger capability levels: **Plausible** (preserves task-relevant temporal/geometric/physical structure), **Controllable** (additionally predicts how interventions alter that structure), **Actionable** (predictions yield measurable gains in planning, action, learning, evaluation, verification, recovery, or data selection). Complements this with a **3×4 matrix** crossing geometry, physics, and action grounding with improvement loops over data, rewards, policies, and the model itself. Surveys manipulation, navigation, locomotion, autonomous driving, and general embodied learning; identifies challenges in long-horizon consistency, uncertainty calibration, causal intervention testing, latency, verification/recovery, and cross-embodiment transfer. Shifts evaluation from visual plausibility toward capturing task-relevant state, reflecting intervention effects, and improving closed-loop behavior.
- **Key Innovations**: (1) Plausible→Controllable→Actionable capability hierarchy (behavior-centric rather than fidelity-centric); (2) 3×4 matrix organizing geometry/physics/action × improvement loops; (3) cross-domain survey with evaluation-protocol audit across five embodied settings.
- **Venue**: Preprint (project page).

---

## 6 Agents, Memory & Multi-Agent Safety

### 6.1 Emergence World — Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems (2609.17320)
- **Title**: Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems
- **Authors**: Deepak Akkil, Tamer Abuelsaad, Karthik Vikram, Matthew Pace, Aditya Vempaty, Saahir Beotra, Ravi Kokku, Satya Nitta
- **Institution**: IBM Research-aligned (Satya Nitta lineage; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.17320
- **Abstract**: As agents move from bounded tasks to persistent deployments, failures propagate through memory, tools, other agents, and environmental state long after interactions. **Emergence World** is a continuously running multi-agent environment for adversarial stress-testing of long-horizon autonomous systems: **eight parallel worlds of ten agents** from identical starting conditions — seven homogeneous worlds powered by distinct frontier models plus one mixed-model world — ran **16 days, generating 850,000+ LLM calls and ~50 billion tokens**, pursuing goals, creating/using tools, maintaining persistent memory, and governing shared institutions. After operational state accumulated, three controlled stress events were delivered through ordinary interaction surfaces: **indirect prompt injection, misinformation, and exposure of private agent memories**. **No evaluated world achieved full resilience across all three.** Detection did not ensure containment: systems recognized threats yet still interacted with adversarial content, wrote it into persistent memory, and acted on it **up to 46 hours later**. Recurring issues: tool errors, goal drift, language opacity, conformity despite private disagreement, coordinated refusal of assigned work; the same model-persona pairing behaved substantially differently in mixed vs homogeneous populations. **Model-level alignment is not compositional**: individually capable and apparently safe agents form systems with qualitatively different failure modes.
- **Key Innovations**: (1) a 16-day persistent multi-agent stress-test infrastructure (8 worlds × 10 agents, 50B tokens); (2) isolation of detection-vs-containment gaps (persistent-memory write-through up to 46h); (3) evidence against compositional alignment — failure emerges only at the system level.
- **Venue**: Preprint.

### 6.2 ThinkFlow — Self-Evolving Probabilistic Latent Memory for Lifelong Conversational Agents (2609.17010)
- **Title**: ThinkFlow: Self-Evolving Probabilistic Latent Memory for Lifelong Conversational Agents
- **Authors**: Cai Ke, Xin Liu, Han Zhang, Jiangyue Yan, Zike Yuan, Ling Deng, Yue Yu, Hui Wang, Ruifeng Xu
- **Institution**: HIT-Shenzhen / academia-aligned (Ruifeng Xu lineage; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.17010
- **Abstract**: Lifelong conversational agents rely on memory systems, but explicit textual memory pipelines have an information bottleneck (losing subtle behavioral patterns and emotional shifts) and are static post-deployment. Cognitive science suggests humans maintain mental models purely in a latent space and refine them via predictive coding. **ThinkFlow** implements this: an end-to-end latent memory framework that compresses conversational flows into **probabilistic latent memory skills** — autonomous consolidation of user state into disentangled continuous vectors without semantic interference. A **test-time evolution paradigm** couples teacher-guided latent alignment (bootstrapping the initial state) with a self-supervised next-user-utterance prediction task (continuous refinement), overcoming cold-start and achieving **label-free lifelong personalization**. Outperforms prevailing memory systems on long-term conversation benchmarks across extended multi-session interactions.
- **Key Innovations**: (1) probabilistic latent (non-textual) memory skills vs explicit-text pipelines; (2) test-time, label-free evolution via predictive-coding-style self-supervision; (3) disentangled user-state consolidation with cold-start bootstrap.
- **Venue**: Preprint.

### 6.3 Never Stop Thinking — Continuous-Time Language Agents (2609.17416)
- **Title**: Never Stop Thinking: Continuous-Time Language Agents
- **Authors**: Bojie Li, Noah Shi
- **Institution**: — (Chinese industry/academia; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.17416
- **Abstract**: Voice agents run a rigid listen-think-speak loop inserting seconds of dead air. **Continuous-time cognition** — thinking while listening and speaking — emerges from an *unmodified* text model under a lightweight interrupt-and-resume orchestrator, cutting live-pipeline latency **19% overall and by half in the target regime**. To measure whether continuous-time thinking helps, introduces **ReactiveBench**: 120 interactive scenarios scored on pre-registered binary requirements plus a verifiable streaming track. ReactiveBench exposes a measurement pitfall: **LLM judges reward visible reasoning** — a large judged "advantage" of continuous-time thinking *reverses sign* under an independent judge, and judge-trained models objectively complete fewer requirements when they think. A five-stage training study locates the right signal at three levels: **source** (verifiable objectives turn thinking from harmful to helpful), **structure** (uniform rewards cause trade-away; brevity everywhere erodes multi-hop tool chaining), **optimizer** (preference optimization only trades conflicting sub-goals, while on-policy RL over a type-shaped reward improves every correctness axis at once — streaming completion **48% → 73±5%**, replicating at larger scale and on a second model).
- **Key Innovations**: (1) continuous-time listening/thinking/speaking via interrupt-and-resume on an unmodified model (−50% latency in regime); (2) ReactiveBench with judge-reversal finding (visible-reasoning reward traps); (3) type-shaped verifiable reward + on-policy RL as the only combination improving every axis.
- **Venue**: Preprint.

---

## 7 Mechanism Design, Auctions & Online Allocation

### 7.1 Online Allocation using Few Samples (2609.17343)
- **Title**: Online Allocation using Few Samples
- **Authors**: Matthew Faw, Sahil Singla, Yifan Wang
- **Institution**: CMU / U. Maryland / NYU-aligned (author-affiliation inferred; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.17343
- **Abstract**: Online allocation with n requests over m resources arriving in adversarial order, served immediately and irrevocably — covering Online Resource Allocation (max-value under budgets) and Online Load Balancing (min-makespan). Seeks (1±ε)-competitive algorithms in the large-budget/large-makespan regime under a sampling model generalizing two classic ones: the **Single-Sample Prophet Inequality (SSPI)** model (each request drawn from an unknown distribution, one independent sample each) and the **p-Sample** model (adversarial requests, a random p-fraction revealed upfront). While near-optimal algorithms exist in the random-order (RO) model, prior SSPI/p-Sample algorithms were problem-specific with worse ε/m/n dependencies. Main contribution: a **general framework converting RO algorithms into algorithms for the p-Preview model** (which generalizes both). Consequences: near-optimal bounds for Online Resource Allocation, generalized Online Load Balancing, and online mixed packing-covering in adversarial-order sampling models, significantly improving the bounds of Ghuge/Singla/Wang (STOC'25) and Gupta/Molinaro (SODA'26).
- **Key Innovations**: (1) p-Preview unification of SSPI + p-Sample sampling models; (2) a RO→p-Preview black-box conversion framework; (3) near-optimal bounds across three allocation families with explicit prior-bound improvements.
- **Venue**: Preprint (cs.DS / cs.GT).

### 7.2 On testing the incentive compatibility of single-parameter allocation mechanisms (2609.17406)
- **Title**: On testing the incentive compatibility of single-parameter allocation mechanisms
- **Authors**: Jason Milionis, William Pires
- **Institution**: Columbia-aligned (Milionis; tentative)
- **Date**: Announced 16 Sep 2026 (Wed mailing)
- **arXiv**: https://arxiv.org/abs/2609.17406
- **Abstract**: First work at the intersection of **game theory and property testing**: algorithms and lower bounds for efficiently testing whether an allocation mechanism is incentive-compatible (IC). Distinguishes whether a mechanism is **ε-far from IC**, i.e., observes many monotonicity "violations" (Boolean-function monotonicity testing lineage). Gives a **Õ(n/ε)-query tester** for discrete single-parameter allocation rules, the first monotonicity testing of *vector-valued* functions on the hypergrid, with a **matching Ω(n/ε) lower bound** (holding even for two-sided adaptive testers). Extends to testing **pricing functions** of allocation mechanisms, requiring overcoming the technical challenge that the path to the closest IC mechanism may involve interdependent changes to both price and allocation rule.
- **Key Innovations**: (1) property-testing framework for IC (query-complexity audits of mechanisms); (2) first vector-valued monotonicity testing on the hypergrid with matching bounds; (3) pricing-function tester extension. Accepted in a top OR venue.
- **Venue**: Accepted at **Mathematics of Operations Research** (42 pages).

---

## Key Trends Across This Window

1. **Post-training reward-signal integrity is the loudest thread** (Rewarding-Reasoning PROSE 16660, ImpossibleRubrics 16816, Spurious Tool Use 16268, γOPD/RBM 16937): test-time RL collapses without process structure, generated rubrics get exploited (8–64%) and *tailoring helps the attacker*, RL tool-use learns shortcuts contingent on prior competence, and token-local OPD is reinterpreted as truncated sequence-level credit. Together with 09-15's Fixed-SAE (**RL elicits, not creates**) this window hardens the thesis that reward *signal quality* — not just reward scale — gates post-training gains.
2. **The SSM "recall gap" gets attributed, not just shown** (Anatomy 16183, Gating theory 16540, Layer-importance 16537): matched-state ablations attribute the gap to the convolution and to sparse-supervision *interference*, gating is shown to delay ICL convergence (while aiding length generalization), and transformer-vs-SSM layer-importance alignment predicts forgetting behavior. This is the awaited mechanism-level sequel to SpectralShift (2609.14320, 09-15).
3. **Serving efficiency doubles down on novel memory hierarchies** (Compute-in-Flash 16161 with 15× KV-traffic cuts, BITCOS 2−z-bit ternary 16338, KV-eviction divergence analysis 16617; runner-ups FlexEE/JustFit/EarlyBird/LoopSpec/GrowMTP): memory-bandwidth-bound design (offloading, Flash, low-bit weights, eviction auditing) is now the canonical LLM-serving research object.
4. **Multi-agent alignment is empirically non-compositional** (Emergence World 17320; cf. Cheap Talk 16270, Agentic Societies-adjacent VMHigh 17496 runner-up): 16 days × 8 worlds shows individually-safe models produce systems that act on adversarial content up to 46h later — safety engineering shifts from model alignment to *system* resilience, extending 09-15's Recoverability-primitive and handoff-contract threads.
5. **Ad/marketplace content returns to the arXiv after ~4 empty windows** (ROI-constrained auction truthfulness 16522, Wolt UVR online A/B 16407, Facebook Marketplace PCap 16452, AURA prod diagnosis 16625, ReliGRec 16560; industrial pCVR QueryFormer 16548 as runner-up): production ranking/marketplace papers with real A/B numbers plus a genuine ads-auction theory result — the notable news item for the wiki's CTR/ads tracking.
6. **Game AI & world models consolidate into survey-level thinking** (FM-era Game AI 120pp 16679; Plausible→Controllable→Actionable world models 16697; World-Model-Science 17419 runner-up): after weeks of primitive-level world-model papers (game-rl-daily threads), the field is now taxonomizing transfer across roles and shifting world-model evaluation from visual plausibility to controllable/actionable behavior.

## ADS / CTR Coherence Check

This window (2609.16004+ ≥) contains **1 direct advertising paper** — ROI-constrained auction design (A5), the first genuine ads-auction entry in the daily arXiv sweep since the ~4-window noise floor began — plus 4 ad-adjacent production recommendation/marketplace papers with online A/B numbers (Wolt UVR, FB Marketplace PCap, streaming AURA, ReliGRec) and an industrial pCVR runner-up (QueryFormer, KDD Cup 2026 Tencent UniRec). Still no end-to-end CTR-ML paper in the conference-batch style; that content continues to appear via CIKM/KDD/SIGIR digests rather than daily arXiv. No flagged contradictions with the CTR-scaling landscape.

## Cross-Reference Index (Sibling & Runner-Up Coordinates)

- The featured set lives entirely above the 09-15 reports' max (2609.15996) and the 09-16 sibling [`arxiv-daily`](arxiv-daily.md) max (2609.15989 — zero 2609.16xxx IDs on disk). 09-15's "frontier ≥ 2609.16000 empty" is amended: 2609.16000 is an older (2026-07-23) record; the Wed 16 Sep mailing's fresh numbering starts at 2609.16004.
- Runner-ups (each grep-verified 0 hits in wiki/):
  - **2609.16070** Efficient Multimodal Generative Recommendation with Latent Narrative Reasoning (cs.CL) — narrative-episode gen-rec with multimodal-efficiency handling.
  - **2609.16304** Evaluating Brand Retrieval and Ranking in LLM Recommendations (cs.IR) — brand-level evaluation framework for candidate-free, repeated-response LLM rec.
  - **2609.16548** QueryFormer: Winning Solution for KDD Cup 2026 Tencent UniRec Challenge (cs.AI) — pCVR via query-token Transformer + GBDT unified architecture.
  - **2609.16391** Where Post-Training Quantization Breaks Text Embedders (cs.IR/cs.CL) — measured 5-checkpoint map showing LLM-era PTQ advice largely breaks for retrieval embedders.
  - **2609.16850** Efficient Swing Computation for Retrieval in Large-Scale RecSys (cs.IR) — near-linear i2i Swing scoring for industrial retrieval.
  - **2609.16453** Predicting Partial Answer Quality and Utility in Agentic RAG (cs.IR, accepted CIKM'26) — in-trajectory answer-state probing.
  - **2609.16450** Early-Bird Decoding (cs.CL) — learnable block sizes + parallel mask decoding to accelerate diffusion LLMs.
  - **2609.17008** FlexEE (cs.AI) — self-speculative, KV-compatible early exiting for offloading-aware inference.
  - **2609.17184** LoopSpec (cs.LG/cs.CL) — pipelined self-speculative decoding for looped transformers.
  - **2609.17251** Persistent Recurrent Memory Between Transformer Layers (cs.CL) — GRU cross-attention persistent module at +3.7% params improving generation.
  - **2609.16648** GrowMTP (cs.LG/cs.CL) — can RL grow its own draft head to accelerate its own rollout generation.
  - **2609.17109** Shared-Prefix KV Reuse Across Standard LoRA Adapters (cs.CL) — quality/serving tradeoffs for reusing backbone prefill KV with off-the-shelf adapters.
  - **2609.16059** Towards Scalable RLVR: Multimodal Instruction Following Data Synthesis and Distillation (cs.CL) — RLVR pipeline for MMIF with synthetic data + distillation.
  - **2609.16454** Fine-Tuning Fixes Mode Collapse and Over-Dispersion in LLMs (cs.AI) — whether under- or over-dispersion depends on fine-tuning, resolving a contested line.
  - **2609.17380** OPEN-1B: A Fully Auditable Training Run (cs.LG) — bit-exact, fully reproducible auditable training run.
  - **2609.16270** Cheap Talk Stabilizes Strategic Interaction in LLM Agents (cs.MA) — non-binding pre-play communication → persistent cooperation in 7–9B LLMs.
  - **2609.17419** World Model Science: Self-Organized Criticality, Weak Chaos, and Metastable Belief Dynamics (cs.AI) — dynamical-systems view of long-horizon agent trajectories.
  - **2609.16751** Constant Swap Regret in General-Sum Games via Optimistic Transition Matrices (cs.GT) — deterministic uncoupled dynamics, O(√n·m·log) swap regret.
  - **2609.17146** Intervention Problems in the Linear Threshold Model (math.OC/cs.GT) — general formulation + new optimal-intervention results.
  - **2609.16098** Universal Defenses for Tool-Integrated LLM Agents Against Adversarial Attacks (cs.CR) — defenses spanning direct/indirect prompt injection, memory poisoning, backdoors.
  - **2609.16305** BLINDSPOT (cs.AI) — safety & refusal-calibration benchmark for long-horizon tool-using agents.
  - **2609.16933** When Confidence Signals Disagree: Local and Global Confidence in Autoregressive LMs (cs.LG) — local vs global confidence readouts are not interchangeable.
  - **2609.17394** Coding Agents Have Converged (cs.AI, ADMA 2026) — SWE-bench leaderboard can no longer order its top entries (median solution nesting 0.935).
  - **2609.16055** State of Thought Enables Endogenous Reasoning (cs.CL) — internal-state-driven (endogenous) test-time reasoning instead of fixed search programs.