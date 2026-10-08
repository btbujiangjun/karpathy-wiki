---
title: ArXiv Paper Check — AI & CTR (2026-10-08)
type: synthesis
created: 2026-10-08
updated: 2026-10-08
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, advertising, retrieval, relevance-judging, generative-recommendation, on-policy-distillation, opr, rlvr, catastrophic-forgetting, continual-learning, kv-cache, looped-transformers, quantization, llm-judges, measurement-validity, self-improvement, agents, daily-digest]
---

# ArXiv Paper Check — AI & CTR (2026-10-08)

**Search**: arXiv export API over HTTPS, 4 category queries (`cat:cs.AI` ×178, `cat:cs.LG` 2 pages ×251, `cat:cs.CL` ×79, `cat:cs.IR` ×12) restricted to `submittedDate:[202610070000 TO 202610082359]`, `sortBy=submittedDate desc`, plus 20 topical passes (`advertising`, `recommender system`, `recommendation`, `sponsored search`, `ranking`, `ad` + `LLM`, `advertiser`, `click-through`, `click through`, `sequential recommendation`, `short video`, `feature interaction`, `multi-interest`, `generative recommendation`, `counterfactual` + recommender, `item recommendation`, `search ranking`, `user response prediction`, `ad auction`, `embedding bag`). **520 harvested raw entries → 416 unique papers, all `published = 2026-10-07`**.

⚠️ **Window framing, stated up front**: this is the **2026-10-07 submission/announcement block**, a **single-day window**, not a rolling 24 hours — arXiv announced on a Wednesday and no 2026-10-08 submissions existed in the API at run time. All 416 unique entries carry `published = 2026-10-07`.

**Dedup baseline**: 8,133 unique arXiv IDs regex-extracted from `wiki/**/*.md` (including the same-day sibling `2026-10-08/arxiv-daily.md`, written earlier) → **416 / 416 window papers are unclaimed**. **20 papers featured** (8 CTR/ads/recsys/IR + 12 core AI); all 20 IDs re-verified 0-hit against the baseline immediately before writing. **No overlap with the same-day `arxiv-daily` sibling** — that digest harvested a different, mostly-`2609.*`/earlier-`2610.*` pool and explicitly recorded a "no direct CTR papers" gap that this report fills.

⚠️ **Topical sweeps were necessary, not optional**: 3 of the 8 CTR-lane papers (`2610.10173` primary `cs.SI`; `2610.09985` primary `cs.GT`; `2610.10047` primary `cs.CV`) live **outside** the four harvested categories and were found only via `all:` abstract queries. A category-only harvest would have missed them. See *Method disclosure*.

---

## Interesting Papers

### CTR / Ads / Recommender / IR lane

Eight papers. The headline is a **methodology-audit day, not an architecture day**: no new CTR-prediction model, no online-deployed ranker. Instead the lane delivers (a) an ad-copy/prepare LLM pricing paper, (b) the first **evidence-grounded audit of the "preference → exposure → click" pipeline**, (c) a controlled dissection of a widely-used generative-recommendation training trick, (d) a NeurIPS paper on a fundamental sampling primitive used in retrieval/softmax training, (e) a **placebo-controlled retrieval ablation**, (f) the first systematic "does a newer backbone make a better relevance judge?" study, (g) a production reading-product baseline that argues personalization-in-document should be evaluated in time order, and (h) a large-scale e-commerce ad-video generation dataset.

---

#### 1. [Marrying Pricing and Advertising with LLMs](https://arxiv.org/abs/2610.09985)

- **ID**: `2610.09985v1` | **Cat**: cs.GT, cs.LG | **Submitted**: 2026-10-07
- **Authors**: Alessandro Barro, Francesco Bacchiocchi, Francesco Emanuele Stradi, Alberto Marchesi
- **Affiliation**: **Politecnico di Milano**
- **PDF**: [Link](https://arxiv.org/pdf/2610.09985)

**Key contributions:**
- Sequential pricing with **jointly optimized price + LLM-generated advertisement** under unknown demand that depends on both, observing only purchase/no-purchase
- An **online actor-critic**: a LoRA-tuned pretrained LLM is the advertisement-generating actor; a demand model is the critic, estimating purchase probabilities that guide price selection and provide a policy-gradient baseline for the actor
- Evaluation framework with **three synthetic demand models + a demand simulator built from real-world marketplace data**
- Expected revenue gains over a reference that does not jointly optimize: **+5.69% / +5.18% / +55.96%** under the three synthetic models and **+5.81%** under the marketplace simulator

**Notes:** The most directly advertising-focused paper in the window, and a genuinely different one: the ad is a decision variable *generated on the fly* and priced against simultaneously. The strength is the problem setup (untangling demand's dependence on price vs ad copy); the weakness is the evaluation (synthetic + one in-house simulator, no real deployment). Relevant to the wiki's ads/CTR line as an **LLM-as-ads-agent** datapoint.

---

#### 2. [When Exposure Is Not Attention: Auditing the Preference-Exposure-Consumption Gap in Personalized News Recommenders](https://arxiv.org/abs/2610.10173)

- **ID**: `2610.10173v1` | **Cat**: cs.SI | **Submitted**: 2026-10-07 | **Comment**: 16 pages, 5 figures, 14 tables; submitted to ICWSM 2027
- **Authors**: Woojin Park
- **Affiliation**: ⚠️ **not printed on the arXiv author block**
- **PDF**: [Link](https://arxiv.org/pdf/2610.10173)

**Key contributions:**
- Names the collapsing assumption in recommender governance: **stated preference, logged exposure, and click consumption are treated as one coherent pipeline**, which can make a platform look more aligned or more diverse than its observed consumption supports
- **Preference-Exposure-Consumption (PEC) audit framework** separating five strata (stated preference, weighted profile state, logged exposure, app-surface pathways, click consumption) under explicit observability boundaries
- Audit on **six months of a deployed mobile news app**: 1,583 user profiles, **95,143 logged recommendation items, 17,512 click events**
- Logged lists contain clicked articles more often than a date-matched candidate-pool baseline (**11.29% vs 9.13%**; top-5 lift 1.47×), yet **many clicks arrive through other app surfaces**; preference–consumption alignment exceeds chance but captures only part of the top-consumed set
- Raw exposure–consumption diversity gaps shrink under count matching, but **concentration mismatch persists (HHI gap 0.082)** in the audit-eligible cohort
- Central claim: **audit conclusions change depending on whether you measure stated preference, logged exposure, or click consumption** — none substitutes for another

**Notes:** A measurement-integrity audit for recsys evaluation, directly relevant to this wiki's recurring "reported ≠ verified" theme and to the evaluation-logy of [[ctr-scaling-landscape]]-adjacent work. The reusable artifact is the **trace-type decomposition** — a governance tool, not a model.

---

#### 3. [Training with Missed Targets in Generative Recommendation: Separating Supervision from Probability Competition](https://arxiv.org/abs/2610.10124)

- **ID**: `2610.10124v1` | **Cat**: cs.IR, cs.LG | **Submitted**: 2026-10-07 | **Comment**: 12 pages, 4 figures, 8 tables
- **Authors**: Xuesi Wang, Yangbin Shi, Xiaolin Zheng
- **Affiliations**: **Zhejiang University**; ⚠️ Independent Researcher (Shanghai) — first author
- **PDF**: [Link](https://arxiv.org/pdf/2610.10124)

**Key contributions:**
- Dissects the common GenRec training trick "append targets missed by the generator's candidate set to the reranker's training list": it **simultaneously** changes retrieved-target weight, adds supervision over appended targets, and makes the two groups **compete for probability mass** — an append/no-append comparison is therefore confounded
- Builds **three matched losses** that hold retrieved-target weight fixed and introduce appended-target supervision and group competition *separately*; the intermediate loss normalizes the two groups independently so training-only targets cannot compete with inference candidates
- On a released **OneRec model** and locally trained **Amazon** generators: that competition can **harm returned-item ranking**; removing it improves full-target NDCG (FT-NDCG) by **7.8–22.2%** in four pre-specified Amazon Video Games comparisons (95% CIs over users and 3-of-4 CIs over runs excluded zero)
- A conservative development-set rule accepted appended-target training for 2-of-3 generators on one held-out category and rejected it for all three on another (avoiding a 1.7% loss) → **candidate completion should be evaluated per generator, not applied automatically**

**Notes:** A clean, controlled take-down of an ad-hoc training practice — precisely the "separate the confounded variables" method in the generative-recommendation lane that this series has been tracing (cf. the 10-07 semantic-ID/decoding audits). The lesson generalizes: **in a GenRec training recipe, supervision location and probability competition are distinct design axes**.

---

#### 4. [Two-Level Softmax Sampling Done Right: Correcting Bias from Size Imbalance and Dispersion](https://arxiv.org/abs/2610.10483)

- **ID**: `2610.10483v1` | **Cat**: cs.LG, cs.IR, stat.ML | **Submitted**: 2026-10-07 | **Comment**: **NeurIPS 2026**
- **Authors**: Walid Bendada, Guillaume Salha-Galvan
- **Affiliations**: **Spotify**; **SJTU Paris Elite Institute of Technology**
- **PDF**: [Link](https://arxiv.org/pdf/2610.10483)

**Key contributions:**
- Two-level softmax (2LS) sampling — sample a cluster, then an item in it — enables sublinear exact-ish sampling for huge softmaxes, but is **systematically biased**: it misweights clusters by ignoring **cluster size imbalance** and **intra-cluster similarity dispersion**
- **S-2LS** (size-corrected) and **SD-2LS** (size- and dispersion-corrected), with **provably better softmax approximation** at negligible-to-nonexistent computational overhead
- Validated on **five large-scale datasets**; recommends replacing standard 2LS outright

**Notes:** A fundamentals paper from Spotify that matters for any training loop that samples negatives/items from a softmax at scale (contrastive retrieval, negative sampling in rec/CTR towers, Gumbel-softmax pipelines). Small skew-corrections like this sit under every industrial recommender; the "provably better, near-zero cost" framing is the deployable part.

---

#### 5. [Does Document Structure Help Dense Retrieval? A Placebo-Controlled Ablation of Four Mechanisms Across Two Corpora](https://arxiv.org/abs/2610.10170)

- **ID**: `2610.10170v1` | **Cat**: cs.IR, cs.AI | **Submitted**: 2026-10-07 | **Comment**: initial draft
- **Authors**: Andrey Kuehlkamp, Priscila Correa Saboia Moreira, Samuel Rund
- **Affiliation**: **University of Notre Dame** (Center for Research Computing)
- **PDF**: [Link](https://arxiv.org/pdf/2610.10170)

**Key contributions:**
- Isolates the unresolved shared confound in retrieval-augmentation structure treatments: **any text prepended to a chunk perturbs its embedding**, so per-treatment studies (chunking, LLM chunk contexts, heading-path metadata, hierarchical two-stage retrieval) cannot attribute effects
- **Placebo-controlled protocol**: matches chunk sizes across conditions and adds a **semantically null placebo — heading paths structurally valid but shuffled across documents**; scores with coverage-aware nDCG; four pre-registered contrasts via document-clustered bootstrap with Holm correction
- On 200 Wikipedia Featured Articles (951 queries) and **1,585 QASPER papers (4,303 questions)**: structure-aligned chunks with real headings beat contextualized fixed windows (**+0.022 / +0.012 cov-nDCG@10**) and the placebo (**+0.010 / +0.016**) → **organization helps, and the cause is content, not token count**
- **Naive two-stage hierarchical retrieval hurts** (**−0.033 / −0.015**), traceable to first-stage section recall; gold structure beats LLM-induced structure on Wikipedia but not QASPER
- Effects are small (Cohen's d_z 0.06–0.11) but Holm-significant and consistent across corpora

**Notes:** The placebo design is the contribution — it converts "structure helps" from a folk result into a falsifiable point. For any RAG product this is a direct "how much of our chunking work is real?" answer, and the meta-lesson (prepend-anything perturbs embeddings) is worth carrying into this wiki's RAG pages.

---

#### 6. [The Impact of Backbone Evolution on LLM-Based Relevance Assessments](https://arxiv.org/abs/2610.09820)

- **ID**: `2610.09820v1` | **Cat**: cs.IR | **Submitted**: 2026-10-07 | **Comment**: 12 pages main content
- **Authors**: Chuting Yu, Guido Zuccon, Teerapong Leelanupab
- **Affiliation**: **The University of Queensland**
- **PDF**: [Link](https://arxiv.org/pdf/2610.09820)

**Key contributions:**
- Tests the assumption that **newer, more capable LLMs** make better relevance judges under a fixed prompt
- Fixes prompts (UMBRELA single-prompt, EXAM rubric-based) and evaluates **sequential model versions** of commercial (Gemini, GPT) and open-weight (Qwen, Llama) backbones
- **No consistent evidence that newer versions improve judging**: similar-or-better aggregate performance does **not** imply judgment stability — **correct judgements from an earlier version are not necessarily preserved by later versions**, even within one model family
- Investigates drivers of the regressions; warns against assuming a prompt validated on one backbone transfers to its successor

**Notes:** The direct continuation of yesterday's ad-relevance-fairness finding ([2610.07544](2026-10-07 report)): LLM judgment migration is **not monotone** with model quality. Any evaluation stack that pins an LLM judge to a pinned prompt *and* rolls the backbone needs this caution. Pairs with `2610.09693` in the AI lane (automated-judge errors).

---

#### 7. [Reading Position Is the Baseline to Beat: A Time-Ordered Evaluation of Personalised Highlight Prediction](https://arxiv.org/abs/2610.09262)

- **ID**: `2610.09262v1` | **Cat**: cs.IR, cs.HC | **Submitted**: 2026-10-07 | **Comment**: 13 pages, 1 figure, 5 tables
- **Authors**: Kazuki Nakayashiki, Keisuke Watanabe
- **Affiliation**: **Glasp Inc.**
- **PDF**: [Link](https://arxiv.org/pdf/2610.09262)

**Key contributions:**
- A reader's **first highlight on a page is the cheapest personal signal a reading product has**; the natural baseline is *reading position*, not popularity or "similar readers"
- Time-ordered evaluation on a social highlighting platform (**7,343 reader-page pairs** on 1,511 pages post-first-highlight): ranking sentences just below the first highlight puts the next highlight in the top 5 **47% of the time vs 26% popularity / 29% best-similarity**
- The right baseline depends on the target: over all later highlights, that ranking loses to popularity; **distance-discounted popularity** beats popularity and both similarity methods on both targets
- Pre-specified comparison: **neither similarity method shows a gain over popularity on later highlights** (a +0.01 gain is excluded); and a gain alone would not prove preference-fitting — synthetic preference-share readers produce one, and out-of-time-order evaluation shows where the reader *was*, not where they *go*
- Verdict: **personalization inside a document should be evaluated in time order and against reading position**

**Notes:** A production reading-product paper (Glasp) that is also a sharp evaluation-critique: **a personalization method must beat cheap positional structure, and out-of-order evaluation artificially inflates it**. Reusable measurement principle for the IR/recsys lane.

---

#### 8. [AdSpark: A Large-Scale Dataset and Benchmark for Product-Centric Advertisement Video Generation](https://arxiv.org/abs/2610.10047)

- **ID**: `2610.10047v1` | **Cat**: cs.CV | **Submitted**: 2026-10-07
- **Authors**: Zhifei Yang, Zhao Jiang, Keyang Lu, Honghe Zhu, Zheng Zhang, Jingjing Lv, Changping Peng, Ching Law, Zhen Xiao
- **Affiliations**: **Peking University**; **JD.com**
- **PDF**: [Link](https://arxiv.org/pdf/2610.10047)

**Key contributions:**
- Frames **product-centric ad-video generation** (fine-grained product identity + selling points + coherent multi-shot narrative) as an unders explored task missing large ad-specific datasets and evaluation
- **AdSpark-300K**: ~300K reference-image–prompt–video triplets (real-world + synthetic subsets) from a major e-commerce platform, each with structured ad annotations — product-identity, selling-point descriptions, creative plans, aligned audio scripts
- **AdSpark-Bench**: diagnostic evaluation across six dimensions (visual quality, product fidelity, instruction adherence, temporal coherence, audio alignment, ad effectiveness)
- Evaluates representative models, exposing challenges in product preservation, multi-shot storytelling, and selling-point visualization; AdSpark-300K fine-tuning improves models. Release pending acceptance

**Notes:** Ads-adjacent but squarely generative-media: an e-commerce-industry dataset (JD.com) for ad video models. Its relevance to the CTR lane is **downstream creative supply** — the "generate the creative, rank it with a CTR model" pipeline. ⚠️ Dataset not yet released; numbers are benchmark-internal.

---

### Core AI lane

Twelve papers in four clusters: **(a) on-policy distillation matures — what transfers, how teacher signals are composed, and where the training signal is collected** (papers 9–11, with paper 12 as a serving-motivated application); **(b) RL post-training methodology — staleness, exploration, attribution** (papers 13–15); **(c) scaling/continual-learning/forgetting** (papers 16–17); **(d) measurement & serving** (papers 18–20).

---

#### 9. [On-Policy Distillation Teaches New Skills but Not New Knowledge](https://arxiv.org/abs/2610.09639)

- **ID**: `2610.09639v1` | **Cat**: cs.CL | **Submitted**: 2026-10-07
- **Authors**: Yixuan Tang, Yi Yang
- **Affiliation**: **The Hong Kong University of Science and Technology (HKUST)**
- **PDF**: [Link](https://arxiv.org/pdf/2610.09639)

**Key contributions:**
- Separates two things OPD could transfer: **new factual knowledge vs compositional multi-step skill**, via a controlled synthetic framework that measures the student's initial abilities and independently gives the teacher additional facts, skill, or both
- Across **four models from three families**: reverse-KL OPD **reliably transfers compositional skill across unseen reasoning structures but transfers minimal factual knowledge**
- Decoupling the recipe locates the mechanism: **forward KL restores factual transfer**; student rollouts specifically improve multi-step execution
- Real-data confirmation (factual QA + competition math) shows the same asymmetry: **notable reasoning gains without factual memory expansion**
- Conclusion: OPD does **not** expand parametric knowledge — it teaches the model to **organize and compose knowledge it already possesses**

**Notes:** The sharpest OPD capability-dissection in the wiki's OPD cluster (cf. 10-07: security/stability/signal/reliability axes). Practical implication for anyone using OPD to "add knowledge": it will not — you need targeted corpus/forward-KL. **"Skills, not facts" should be the default prior for an OPD paper's claims.**

---

#### 10. [Composing What Each Teacher Learned: Multi-Teacher On-Policy Distillation through Teacher-Relative Shifts (Δ-MOPD)](https://arxiv.org/abs/2610.10460)

- **ID**: `2610.10460v1` | **Cat**: cs.LG, cs.AI | **Submitted**: 2026-10-07
- **Authors**: Hejian Sang, Zhengze Zhou, Shayan Mohajer Hamidi, Xiaomin Li, Rohit Jain, Alborz Geramifard
- **Affiliations**: **Iowa State University**; **LinkedIn**; **Harvard University**
- **PDF**: [Link](https://arxiv.org/pdf/2610.10460)

**Key contributions:**
- Names the hidden confound in multi-teacher OPD: transferring **endpoint policies** mixes *what post-training changed* with *preferences inherited from each teacher's base model*
- **Δ-MOPD** instead transfers each teacher's **teacher-minus-base logit shift**, re-anchored at the student's frozen initialization
- Mechanism evidence: **inherited base pull can exceed the post-training shift**, which is what impedes endpoint transfer (reduces teacher-term norm ratio and target–student KL)
- With three composed teachers on a common domain, Δ-MOPD beats endpoint composition by **+4.11 Math / +1.95 five-benchmark points**; with two it matches; under **phased routing** it wins in both phase orders and cuts the order gap from 10.50 to 6.42 points
- Target construction is therefore an **independent design axis** in MOPD, complementary to teacher selection

**Notes:** Gives the OPD cluster a concrete new axis — **what exactly you transfer** (endpoint policy vs re-anchored delta). The "base pull" mechanism is a falsifiable, checkable quantity. LinkedIn authorship makes this a genuinely industrial OPD datapoint alongside the wiki's others.

---

#### 11. [OnlineQAT: On-Policy Distillation for Ultra-Low-Bit Large Language Models](https://arxiv.org/abs/2610.09346)

- **ID**: `2610.09346v1` | **Cat**: cs.CL, cs.AI, cs.LG | **Submitted**: 2026-10-07
- **Authors**: Wenjun Wang, Heng Li, Yanggan Gu, Hongxia Yang
- **Affiliations**: **The Hong Kong Polytechnic University**; **Sun Yat-sen University**; **PolyU-Daya Bay Technology and Innovation Research Institute**
- **PDF**: [Link](https://arxiv.org/pdf/2610.09346)

**Key contributions:**
- Diagnosis: quantized models get their recovery signal from **fixed/teacher-generated completions** but at deployment condition on **self-generated prefixes** → quantization errors move the model into states absent from offline recovery data
- **Two-stage OnlineQAT**: block-wise QAT initialization, then **on-policy distillation on student-generated responses**, with a frozen full-precision teacher providing sampled reverse-KL at each visited prefix
- On Qwen3-1.7B: **57.28 avg at W3A16, 32.52 at W2A16**, +2.90 / +0.44 over ReasoningQAT
- Takeaway: **student-visited states provide a recovery signal beyond fixed-completion training**, particularly at 3 bits

**Notes:** Applies the OPD-on-student-states idea (which this wiki's OPD cluster has been circling since 10-06) to an underserved, deployment-critical setting: sub-4-bit quantization. Ties the OPD thread to the KV/quantization serving thread (papers 18, and `2610.09827` in "also").

---

#### 12. [Decoupling Exploration from Optimization in RLVR (Exploration-Distillation, ExpDis)](https://arxiv.org/abs/2610.10536)

- **ID**: `2610.10536v1` | **Cat**: cs.LG, cs.AI, cs.CL | **Submitted**: 2026-10-07 | **Comment**: 20 pages, 16 figures, 9 tables; code/checkpoints public
- **Authors**: Saif Punjwani, Micah Goldblum
- **Affiliation**: **Columbia University**
- **PDF**: [Link](https://arxiv.org/pdf/2610.10536) | **Code**: [SaifPunjwani/Exploration-Distillation](https://github.com/SaifPunjwani/Exploration-Distillation)

**Key contributions:**
- Diagnosis: RLVR's promise is discovering new strategies, but **adding novelty incentives to a verifiable-reward objective degrades quality** — verifiable rewards supervise a narrow slice of behavior and degradations are hard to recover from
- **ExpDis decouples exploration from optimization**: explorer policies get the novelty bonus; their correct/quality trajectories are **filtered and distilled into a separate student** trained *without* a novelty bonus; alternated over rounds
- Aggressive exploration without degrading the student; **outperforms DAPO** at matched wall-clock budget across seven math benchmarks and two model families; improves **pass@k scaling** (more diverse correct solutions)

**Notes:** A clean architectural answer to the exploration-vs-quality trade-off in RLVR — relevant to this wiki's [[verifiable-rewards]] / GRPO line and to the "reward is a narrow supervision slit" theme of the 10-07 alignment report. The "separate models, distill the good rollouts" shape is the reusable idea.

---

#### 13. [COPC: Coupled Off-Policy Correction for Asynchronous LLM Reinforcement Learning](https://arxiv.org/abs/2610.09597)

- **ID**: `2610.09597v1` | **Cat**: cs.LG | **Submitted**: 2026-10-07
- **Authors**: Zicheng Hu, Zhijian Zhou, Xuan Zhang, Yuchen Liu, Cheng Chen, Yuan Li, Qi Gu, Yan Feng, Hongyan Hao, Chao Qu
- **Affiliations**: **Fudan University**; **Meituan**; **East China Normal University** (⚠️ affiliations recovered from LaTeXML block; some authors interleaved)
- **PDF**: [Link](https://arxiv.org/pdf/2610.09597)

**Key contributions:**
- Asynchronous LLM RL trains on **stale trajectories**; existing fixes correct token-level policy mismatch only — COPC shows **advantage estimates also inherit mismatch** ("advantage staleness")
- Exact bias/variance decompositions of a two-channel actor update reveal **nonseparable coupling** between policy-weight and advantage errors (multiplicative bias terms; squared policy weights amplify advantage uncertainty in the gradient variance) → policy- and advantage-side correction should be **coordinated**
- **COPC** = token-level ratio masking + **two-sided clipped-ratio weighting of TD residuals** for return/advantage estimation; joint parameter sweeps confirm the coupling hypothesis (the effect of one correction parameter depends on, and can reverse with, the other)
- Highest reported performance on **tool-integrated math reasoning and search**, stable where most async baselines **collapse late in training**; gains persist at **64-step staleness**; ~1.7× step-time speedup over synchronous PPO

**Notes:** The "staleness must be corrected on both channels, and the corrections interact" result is a mechanism-level finding in the RL-from-LLM post-training lane. Meituan provenance (internship) anchors it to a production-scale async training stack.

---

#### 14. [Which Rollout Taught It That? BehaviorTrace and the Limits of Training-Data Attribution in Online RL](https://arxiv.org/abs/2610.10422)

- **ID**: `2610.10422v1` | **Cat**: cs.LG, cs.CL | **Submitted**: 2026-10-07 | **Comment**: 11 pages, 2 figures, 4 tables
- **Authors**: Amit Nautiyal
- **Affiliation**: ⚠️ **Independent Researcher** (per author block)
- **PDF**: [Link](https://arxiv.org/pdf/2610.10422) | **Code**: [AmitoVrito/BehaviorTrace](https://github.com/AmitoVrito/BehaviorTrace)

**Key contributions:**
- Can we attribute an RL-taught behavior to the rollouts that taught it — **and how do we know an attribution method's answer is real?** Uses GRPO on Qwen2.5-1.5B with a **planted behavior of known cause**
- Releases **BehaviorTrace**: an open harness combining full-gradient sketching, the planted-behavior setup, and controls for gradient magnitude, fluency, headroom, and seed/draw variation
- **Most apparent attribution signal is confounded**: a control ranking steps by gradient size *alone* (no behavior target) reaches **4.2–4.5× chance** and matches/beats the best targeted estimator on 2-of-3 seeds; model **fluency predicts the behavior label** at least as well as every gradient method at saturated checkpoints
- Once fluency is controlled, per-rollout results flip seed-to-seed and draw-to-draw — **a single run cannot settle the question**
- One signal holds across all three seeds: the gradient of the **trigger tokens** aligns with a target built where the behavior actually occurs. Ends with an evaluation checklist; tests GAS and a TRAK-style estimator, proposes none

**Notes:** A textbook measurement-audit for the "DML attribution in RL" genre, in this wiki's third-consecutive-window pattern of *negative/confound results outperforming method wins* (cf. 10-07 paper 14's content-vs-source, 10-06 drift results).

---

#### 15. [The Winner's Curse in LLM Self-Improvement Loops: Selection Noise, Lock-in, and Acceptance Rules](https://arxiv.org/abs/2610.09239)

- **ID**: `2610.09239v1` | **Cat**: cs.AI, cs.LG | **Submitted**: 2026-10-07 | **Comment**: 34 pages, 4 figures, 18 tables; code + saved records in ancillary
- **Authors**: Litao Hu, Yutong Tang
- **Affiliations**: **Meta**; **Microsoft**
- **PDF**: [Link](https://arxiv.org/pdf/2610.09239)

**Key contributions:**
- Treats the keep-if-better step of self-improving looped LLMs as **selection under measurement noise** on a small reused evaluation set
- Empirical (Qwen self-instruction rewrites, candidates also scored on **600 held-out items**): **most proposals after the first are harmful**, and the model gives the size of the winner's curse of a generation's best candidate
- Pre-registered study: final selection-set score of greedy loops **exceeded held-out accuracy by 13–20 points with 16 selection items** and **1–5 points with 256**; held-out gains grew with set size on TREC but **not GSM8K**; tested acceptance rules did **not** beat greedy acceptance
- Scoring both start and current instructions on 64 never-used items removes the average bias of a loop's reported gain, but **single estimates remain off by ~6 points**
- Implication: **self-improvement studies should report held-out gains with uncertainty**

**Notes:** Directly relevant to this wiki's recursive-self-improvement lineage and to Karpathy's loops/self-improvement arc. The 13–20 point selection-set `overstatement` is a number every "self-improving loop improved itself" headline should be checked against. Meta+Microsoft authorship gives it weight.

---

#### 16. [Sequential Pretraining Favors Large Models](https://arxiv.org/abs/2610.09611)

- **ID**: `2610.09611v1` | **Cat**: cs.LG | **Submitted**: 2026-10-07
- **Authors**: Mohnish Harwani, Yujia Zheng
- **Affiliations**: **Purdue University**; **University of Illinois Urbana–Champaign**
- **PDF**: [Link](https://arxiv.org/pdf/2610.09611)

**Key contributions:**
- Reframes "large models become capable" with a confound: **robustness to adverse training effects vs learning more representative features**
- Defines **primacy bias**: how much exposure to early data distributions impairs later learning; **small models allocate capacity inefficiently toward early distributions**; sufficiently overparameterized models are robust to it
- Consequential in pretraining, where foundation models meet **heterogeneous data sequentially** — small models struggle on late distributions (code/math/reasoning late-in-curriculum data harm)
- **Exposure Therapy (ET)**: a simple regularization for more efficient capacity allocation; improves late-data and overall capability up to the billion-parameter scale
- Thesis: part of large-model advantage is **robustness to adverse training effects, not better features** — and training algorithms can recover some of it for small models

**Notes:** A "scaling-law interpretation" paper with concrete small-model payoff. For this wiki's CTR-scaling debate ([[ctr-scaling-landscape]]), it is a caution that observed size-scaling gains conflate representational capacity with training robustness — directly relevant to claims that "bigger CTR/rec models win because of capacity."

---

#### 17. [A Deafening Silence: Catastrophic Forgetting Lives in the Output Embeddings of Tokens the Data Never Speaks](https://arxiv.org/abs/2610.09835)

- **ID**: `2610.09835v1` | **Cat**: cs.CL, cs.AI | **Submitted**: 2026-10-07
- **Authors**: Jonghyun Han, Younghoon Song, Jongyoul Park
- **Affiliations**: **Seoul National University of Science and Technology**; **Korea Institute of Land & Infrastructure Safety Technology**
- **PDF**: [Link](https://arxiv.org/pdf/2610.09835)

**Key contributions:**
- In data-free continual pretraining/fine-tuning, locates *where* forgetting happens: it **concentrates in the output embeddings of tokens rarely seen in the new corpus**, while the same body band is inert and new learning lives elsewhere
- The localization is set by **corpus-vocabulary deficiency, not the training mode** → forgetting risk can be ranked *pre-training* from token counts alone
- Mechanism: absent tokens get persistent **one-sided softmax gradients** that **Adam's `sqrt(v_hat)` second-moment normalization amplifies** into full updates
- A **one-line fix — raise Adam's epsilon on the output projection only** — removes **39.4–67.9% of forgetting across eight settings, 160M–12B params, four model families**, without degrading target learning or per-model tuning; composes with replay (79.8% on Qwen/Korean) and rescues released-head LoRA from a **23-fold** forgetting surge
- Post-hoc editing of drifted rows recovers under 5% of remembering → **the intervention must operate during training**

**Notes:** A concrete, cache-proof, deployable anti-forgetting intervention whose mechanism is spelled out. Connects to the wiki's forgetting/continual-learning thread (10-07 INTEGER's replay rationale; the `09835` finding explains *why* replay is needed — the output layer is the fragile part).

---

#### 18. [ResidualQuant: KV Cache Quantization for Looped Transformers with 2-Bit Residuals](https://arxiv.org/abs/2610.10381)

- **ID**: `2610.10381v1` | **Cat**: cs.LG | **Submitted**: 2026-10-07
- **Authors**: Heejun Kim, Junyoung Lee, SangLyul Cho, Dongsu Han, Insu Han, Sehoon Kim
- **Affiliations**: **KAIST**; **Yonsei University**; **Seoul National University**
- **PDF**: [Link](https://arxiv.org/pdf/2610.10381)

**Key contributions:**
- Looped Transformers multiply **compute depth**, not parameters — but the **KV cache still scales with loop count**, a memory bottleneck on batch size and throughput
- Key observation: **KV states across loops are highly similar** → encode the *final-loop* KV as reference and store the other loops as **low-precision residuals**
- Combines least-squares scaling + rotations on residuals and **loop-wise mixed precision**, quantizing down to **INT2** with faithful reconstruction
- Accuracy close to BF16 under mixed precision with **80.7% less theoretical KV storage**; up to **+13.0% accuracy** over rotation-based quantization at equal memory; on an RTX 5090, **2.73× fixed-batch decode, up to 4.15× peak throughput** via 2× batches

**Notes:** The serving-side payoff for the looped-transformers / recurrent-depth cluster this series has tracked for two windows (10-07's RLT/SanSi/HLA/CMM). "Inter-loop KV is redundant, so compress the residual" is a loop-aware idea generation wouldn't discover — a genuinely architecture-specific optimization.

---

#### 19. [Certified by Abstention: Distribution-Free Guarantees for Chain-of-Thought Verifiers at Small Calibration Budgets](https://arxiv.org/abs/2610.09541)

- **ID**: `2610.09541v1` | **Cat**: stat.ML, cs.CL, cs.LG | **Submitted**: 2026-10-07 | **Comment**: 22 pages, 7 figures, 12 tables; under submission at AISTATS 2027
- **Authors**: Arjun Balaji
- **Affiliation**: **Columbia University**
- **PDF**: [Link](https://arxiv.org/pdf/2610.09541)

**Key contributions:**
- At realistic calibration budgets (tens–hundreds of labels; 7 models, 5 verifier signals, **37,000 graded traces**), what do distribution-free selective guarantees actually deliver?
- Central pathology — **validity by abstention**: an `(α,δ)`-valid certificate that fires with probability P_fire bounds failure only by **δ/P_fire** → **a certificate that rarely fires can be valid and wrong every time it is used** (in simulation it fails ≤0.3% of calibration draws but in **up to 69% of fired draws**)
- A certification floor and a lattice condition for BH-conformal selection explain the abstention; at these budgets the standard certificate returns **nothing or a large accepted set**
- An unreadable residual-stream probe buys **2–3× the coverage** of readable signals — an edge a cross-fitted reconstruction cannot recover `linearly`
- A **floor-started fixed-sequence certificate** (valid without monotonicity) covers more than Bonferroni on every model–signal pair; under benchmark shift, **errors among accepted traces track the new task's base error**, and under best-of-n against the verifier failure rises past target while **empirical frequency stays below δ — because abstention absorbs the failures**

**Notes:** The "valid-by-abstention" failure mode is a genuinely disturbing result for any conformal/selective guarantee used as a release gate on a reasoning verifier — it makes a very strong paper for the wiki's verifier/[[verifiable-rewards]] line. The rest of the "certificate cannot see what matters after deployment" results is the same theme the series keeps hitting from different angles.

---

#### 20. [Loud Failures, Quiet Failures: Fault Detection and Recovery in Tool-Using Language Model Agents](https://arxiv.org/abs/2610.10062)

- **ID**: `2610.10062v1` | **Cat**: cs.AI | **Submitted**: 2026-10-07
- **Authors**: Obada Kraishan
- **Affiliation**: **Texas Tech University**
- **PDF**: [Link](https://arxiv.org/pdf/2610.10062)

**Key contributions:**
- Fault-injects a function-calling benchmark's executable env with **four typed faults** (explicit error, plausible wrong value, timeout, schema drift) at a controlled trajectory point; **6 models × 3 families, 1,920 trials, 24 multi-step tasks**
- Agents treat a failure as a problem in **91.3% of trials on explicit errors but only 58.8% on plausible wrong values** (vs a 26.8% "problem reported" rate when nothing was wrong)
- Reasoning variants are **not better placed**: paired against instruct siblings they *notice less* (−9.3 pts) and *change plan more* (+10.4 pts), with **unchanged recovery**
- Against the agent-stochasticity baseline (fault-free runs end in the same state only 63.3% of the time), **only a missing tool clearly lowers recovery (39.9%)**; timeouts/schema-drift/corruption sit within run-to-run variation; agents re-call the same faulted tool 3+ times in up to 22.2% of trials
- **A prompt asking to check each result did not move detection** → agents respond to the error *channel*, not the content of what a tool returns; failures that stay in-format pass through

**Notes:** "Agents respond to the error channel, not the content" is the quotable finding — a mechanism-level statement about why tool agents under-loop on soft corruption. Connects to yesterday's "When Tools Lie"-adjacent line (10-07) and to the tool-use reliability thread in the agents pages.

---

## Cross-cutting observations

1. **Third consecutive window with no new CTR-prediction architecture.** As in the 10-06/10-07 reports, the [[ctr-scaling-landscape]] thread (GRAB, LoopCTR, EST, CADET…) gains **no entrant**. Today's CTR lane is instead *training-recipe and measurement audits*: a GenRec training trick dissected (paper 3), a softmax sampling primitive corrected (paper 4), a placebo-controlled retrieval ablation (paper 5), relevance-judge drift across backbones (paper 6), and a recsys audit-trace decomposition (paper 2). The absence is recorded explicitly so it is not read as an absence of interest.
2. **"LLM-as-judge integrity" is now a two-consecutive-window cross-lane theme.** 10-07 gave advertiser-identity bias in ad-relevance judges ([2610.07544]); today gives **backbone-evolution non-monotonicity** (`2610.09820`, IR lane) and judge-error/evaluation-reliability harms in UQ evaluation (`2610.09693`, "also worth recording"). A fixed prompt on a rolling backbone is not a stable measurement instrument.
3. **The OPD cluster keeps splitting into new axes.** 10-07: security / stability / signal / reliability. Today: **what transfers** (skills-not-knowledge, paper 9), **how teacher signals are composed** (endpoint vs re-anchored delta, paper 10), and **where the signal is collected** (student-visited states for low-bit recovery, paper 11). The unifying correction: OPD's design space is *not* "distill harder."
4. **RL post-training methodology converged on "whose signal, and how stale."** ExpDis (paper 12) decouples exploration from optimization; COPC (paper 13) corrects both policy- and advantage-side staleness *multiplicatively coupled*; BehaviorTrace (paper 14) shows most training-data attribution in online RL is fluent confounding. Three papers, three different layers of the same stack — consistent with this series' "reported ≠ verified, and the training signal is the thing to audit." 
5. **Serving/quantization again carries the deployable wins — and two of them are loop-aware.** ResidualQuant (paper 18) exploits **inter-loop KV similarity** for looped-transformers; `2610.09827` Dual-QK (also worth recording) enables 2-bit + pruning; `2610.09307` vLLM-Omni generalizes the serving runtime to omni-modality; `2610.10118` YANchor-4B pushes O(N)/O(1) long-horizon reasoning. The 10-07 looped-depth cluster (RLT/SanSi/HLA/CMM) now has **two serving-layer companions** — the line is becoming deployable.
6. **Catastrophic forgetting gets a mechanism and a one-line fix.** `2610.09835` localizes forgetting to output embeddings of corpus-absent tokens, explains it via Adam's second-moment amplification, and removes 39.4–67.9% of forgetting by raising epsilon on one projection. It is the strongest "single intervention, spelled-out mechanism" continual-learning result of the window — and it explains *why* the 10-07 INTEGER's replay (and OPD rollouts generally) are needed.
7. **Measurement/negative results dominate the AI lane again (4th window in a row).** Winner's Curse (paper 15), BehaviorTrace (14), Certified-by-Abstention (19), Loud/Quiet Failures (20), backbone-drift (`09820`), and the GenRec appendix-trick harm (3) all end in "the apparent effect/guarantee was smaller, confounded, or flips." The series' standing finding — **reported capability and verified capability diverge** — held again, and this time several papers brought the *instrument* under audit, not just the models.

---

## Also worth recording (not detailed above)

- **`2610.10179`** — *Beyond Outcome Rewards: Constructing and Assigning Retrieval Credit for Search Agents* (Wenyu Huang, Xinyu Hou, Pavlos Vougiouklis, Ruofei Lai, Jeff Z. Pan). Systematically compares intermediate reward-shaping / credit-assignment signals for search agents and combines them with final outcome rewards; both **signal choice and where credit is assigned** change training behavior. Directly relevant to the wiki's RLVR/search-agent thread.
- **`2610.09944`** — *AgentTime: Can Agents Estimate and Control Their Own Runtime?* (Michael Ofengenden, Maksym Andriushchenko). First benchmark for **duration-following + runtime prediction + elapsed-time estimation** (222 tasks / 18 sources). A single duration instruction is followed with typical factor-1.2× (GPT-6 Astra in Codex) to 2.9× (Fable 5.1 in Claude Code) deviation; **completing a task ≠ controlling your own time**; 14 of 158 reviewed runs explicitly slept after appearing to finish.
- **`2610.10091`** — *ExperienceIndex: Artifact-Grounded Memory* (Peter Baile Chen et al.; **MIT / UChicago / Northwestern… / Allen AI**). An experience layer capturing **artifact-level knowledge from prior reasoning traces** (single-artifact + artifact-pair experiences); middleware retrieval guidance raises answer quality up to **+11.0 pts** and cuts online dollar cost up to **50.5%**; cross-task transfer and teacher→weaker-student transfer demonstrated.
- **`2610.09484`** — *MIMESIS: Learning User Simulators as Training Environments for Interactive Agents* (Hoang Phan et al.; **Google**). Purpose-built user simulator trained on human conversations with 13 realistic behavior patterns; SOUL-Index 65.7 beats frontier models; agents trained against frozen MIMESIS **generalize to all nine unseen user simulators**. Plus **Coached On-Policy Self-Distillation** for dense token-level feedback. Connects to the personal-agent / simulation line.
- **`2610.10394`** — *Kernel Autoresearch for Open-Ended Model Discovery (Kernaut)* (Richard Cornelius Suwandi et al.). LLM coding agents write kernels as programs under **construction contracts** (22–58% of LLM kernels that pass numerical checks fail at other scales/dims), quality-diversity archive + novelty screening; discovered kernels **outperform a meta-learned deep kernel** on held-out BO families and beat ARD/deep baselines on unseen enzyme-kinetic mechanisms; human-refinable.
- **`2610.10468`** — *A Society of Researchers: Designing Institutions for Populations of Autonomous Research Agents* (Ali Asaria et al.; CSAIL-adjacent workshop short paper). Ten-thousand-researcher society with RFPs, grants, a human "mayor"; one lab reported ~30% less compute for same pretraining quality. **Institutions, not more agents per project** — relevant to the autoresearch arc.
- **`2610.09827`** — *Dual-QK: Sharp Queries and Flat Keys for Prunable 2-bit KV Caches* (Sunjoo Whang et al.). Paired non-orthogonal query/key transforms: partial key whitening for INT2 + a query-aligned basis to concentrate energy for pruning; **6.8× KV compression at 128K context, up to 3.75× decoding throughput**. Companion to paper 18.
- **`2610.09307`** — *vLLM-Omni Technical Report* (vLLM-Omni Team). A unified multi-stage serving runtime for **text/audio/image/video/action** workloads — a single orchestrator over per-stage engines with session-shaped control for duplex/world-model/robot loops. Positions "serving as a heterogeneous multi-stage workflow," not a single decode loop.
- **`2610.09679`** — *CERO: Where and When to Allocate Rollouts for RL Post-Training* (Yiming Zong et al.). Online primal-dual scheduler for prompt admission + budget pacing across the whole training horizon (concave surrogate utility of cumulative prompt exposure); best avg@16 macro-average on each of three backbones across five math benchmarks under matched budgets.
- **`2610.09693`** — *A Tale of Two Error Categories … Automated Judges in UQ Evaluation* (Evgenia Ilia, Wilker Aziz; **INLG 2026**). A judge's performance only coarsely predicts the impact of its errors on UQ-evaluation reliability; **judgment errors tend to misrepresent the informative UQs most**. Pairs with `2610.09820` and paper 19.
- **`2610.09858`** — *Training Advisors for LLM Agents from Task Outcomes (Caddie)* (Sergei Polezhaev et al.). RL-trained critic (outcome-only supervision, base frozen) that improves success across **four base models including three unseen** — +25 pts on MuSiQue for Qwen3-4B, beats Kimi K3 without critic; transfers to τ³ and DeepDive.
- **`2610.09416`** — *Efficient Reasoning with Flow Language Models* (Hanru Bai et al.). Theoretical (superposition) + empirical case that continuous FLM states let **evidence for multiple candidates persist during denoising before a discrete answer**; FLMs beat discrete-diffusion baselines in the few-step regime — on Maze15 the FLM hits 95% accuracy at 64 steps with **36.5% fewer parameters** than MDLM.
- **`2610.10118`** — *YANchor-4B: Long-Horizon Reasoning in O(N) Time with O(1) Memory* (Huishan Ji et al.). Recurrent model with anchor-based retrieval; **82.93% pass@1 AIME 2024–26, 63.64% HMMT**, beating linear-time/constant-state counterparts incl. larger models; higher batched long-generation throughput than Transformer/hybrid on H100.
- **`2610.09296`** — *The AI Evaluation Ecosystem* (Yash Dave, Sang T. Truong, Serena Wang, Sanmi Koyejo; **Stanford**; 70pp). GABM simulation of benchmarks/providers/users/regulators; case study: **private holdouts shrink the benchmark–user-satisfaction gap on most benchmarks but widen it on a few**, depending on where holdout weights shift credit. Treats evaluation as an ecosystem dynamic, not a static criterion.

---

## Method disclosure, dedup, and cautions

**Harvest**: arXiv export API over HTTPS. Four category queries in `submittedDate:[202610070000 TO 202610082359]`, `sortBy=submittedDate desc`: `cs.IR` (12), `cs.CL` (79), `cs.AI` (178), `cs.LG` (200+51 across two pages) → **520 raw entries → 416 unique papers, all `published = 2026-10-07`**. Twenty `all:` topical passes (listed in the header) added a small number of entries outside the four categories; **3 of 8 CTR-lane picks live outside the harvested categories** (`2610.10173` cs.SI, `2610.09985` cs.GT, `2610.10047` cs.CV) and were surfaced by topical sweeps — a category-only harvest would have under-sampled the CTR lane. Seven topical queries (`click-through`, `click through`, `user response prediction`, `sequential recommendation`, `short video`, `feature interaction`, `multi-interest`, `item recommendation`, `search ranking`, `sponsored search`) returned **zero** entries in-window after this run's earlier `2610.07xxx–08xxx` coverage — the current block's CTR supply is genuinely thin, consistent with the 10-07 report.

⚠️ **Window semantics**: "last 24 hours" is not what arXiv exposes. All 416 harvested entries carry `published = 2026-10-07`, the newest block available at run time (no 2026-10-08 submissions exist in the API). This report covers the **2026-10-07 announcement block — a single day, not a rolling 24 hours**.

⚠️ **Dedup**: baseline = 8,133 unique arXiv IDs regex-extracted from `wiki/**/*.md`, taken before writing and **including** the same-day sibling `2026-10-08/arxiv-daily.md`. **416 / 416 window entries unclaimed**; **all 20 featured IDs re-verified 0-hit** against that baseline immediately before writing. ID-level dedup only, no title-level pass; the 10-07 run already recorded that ID-only dedup has produced duplicate titles in this series, so title-uniqueness is asserted albeit not machine-checked.

⚠️ **Affiliation discipline**: institutions read **only** from each paper's own LaTeXML author block / institutional address block, **never inferred** from surnames, emails, or reputation. **Affiliations recovered for 18 / 20** featured papers; the two exceptions are `2610.10173` (single author Woojin Park — **no affiliation printed**) and `2610.10422` (author states **Independent Researcher**). Notable recoveries only visible in LaTeXML, not the abs page: paper 10 (`10460`) has **LinkedIn** + Iowa State + Harvard; paper 13 (`09597`) has **Meituan** (Fudan/ECNU) with the Meituan tie explicit; paper 15 (`09239`) has **Meta** + **Microsoft**; paper 18 (`10381`) spans KAIST/Yonsei/SNU. Paper 1 (`09985`) is entirely Politecnico di Milano.

⚠️ **Venue discipline**: **3 of 20 carry a venue** — `2610.10483` (**NeurIPS 2026**), `2610.09693` (recorded, **INLG 2026**), `2610.10173` (submitted to **ICWSM 2027**, unaccepted), `2610.09541` (under submission at **AISTATS 2027**). **No result in this report was independently replicated, and none was replicated by a second group.** Venue tags are self-reported via `comment`/`journal_ref`.

⚠️ **Claim-level cautions carried inline**: paper 1's revenue numbers are synthetic/simulator only; paper 2's effects are audit-descriptive, no causal claim; paper 5 reports effect sizes this small (d_z 0.06–0.11); paper 6 finds non-monotonicity without full mechanism; paper 13's affiliation block interleaves authors and the Meituan note came from an ‡-footnote; paper 14 is single-driver GRPO attribution and disclaims general claims; paper 15 `scoring` vs held-out gaps are Qwen-specific; paper 18's gains are against rotation-based quantization baselines on Ouro-class looped backbones; paper 19's "up to 69% fired-failure" is a simulation finding; papers 6/20 measure one setting family each.

⚠️ **Cross-window note for the next lint**: the OPD cluster now spans two windows and **five named axes** (10-07: security, stability-content, signal-insufficiency, reliability; 10-08: skills-not-knowledge, target-construction, signal-collection-site) — a synthesis page consolidating them is a candidate, as is adding a 2026-10-08 row to the looped-transformers thread (ResidualQuant + Dual-QK are the first *serving-layer* entries in that cluster).

---

## Sources / Links

All 20 featured papers link directly to `https://arxiv.org/abs/{ID}`; PDFs are `https://arxiv.org/pdf/{ID}`. Window = `submittedDate:[202610070000 TO 202610082359]`, announced **2026-10-07**. Sibling digest for the same day: `wiki/synthesis/2026-10-08/arxiv-daily.md` (declared a "no direct CTR papers" gap that this report fills).