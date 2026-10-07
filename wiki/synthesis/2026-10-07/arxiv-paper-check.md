---
title: ArXiv Paper Check — AI & CTR (2026-10-07)
type: synthesis
created: 2026-10-07
updated: 2026-10-07
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, generative-retrieval, generative-recommendation, reranking, fairness, looped-transformers, on-policy-distillation, safety, agents, alignment, formalization, world-models, daily-digest]
---

# ArXiv Paper Check — AI & CTR (2026-10-07)

**Search**: `cat:cs.IR`, `cat:cs.AI`, `cat:cs.LG`, `cat:cs.CL`, `cat:cs.CV` restricted to `submittedDate:[202610060000 TO 202610072359]`, `sortBy=submittedDate desc`, `max_results=200` (second pages fetched for `cs.AI` and `cs.LG`). Announced window = **2026-10-06** — every one of the **472 harvested entries** carries `published = 2026-10-06`.

**Dedup baseline**: 7,985 unique arXiv IDs already claimed repo-wide → **472 / 472 window papers are unclaimed**. **20 papers featured** (8 CTR/ads/recsys + 12 core AI); all 20 IDs re-verified 0-hit against the baseline immediately before writing.

⚠️ **Window caveat, stated up front**: this is a **single-day announcement block (2026-10-06 submissions), not a rolling 24 hours**. arXiv announces on weekdays and the announcement date lags submission by roughly a day, so a run on 2026-10-07 sees the 2026-10-06 submission wave. No 2026-10-07 submissions exist in the API at run time. The *Method disclosure* section explains this and what it costs in coverage.

⚠️ **Sibling note**: unlike the 2026-10-06 run — where the same-day `arxiv-ai-search` digest claimed three papers **after** this job's dedup baseline was built — **no 2026-10-07 sibling digest existed when this report was written**, so there was no post-write collision pass to run. Dedup is ID-level only; see *Method disclosure*.

---

## Interesting Papers

### CTR / Ads / Recommender lane

Eight papers. The lane is **unusually production-heavy** this window: two papers report **online A/B lifts on deployed systems** (SIFT at Airbnb; RLCP on KuaiRand), one is an **industrial B2B negative-sampling study** (Intuit + Michigan State), and two are a **matched generative-retrieval methodology pair from the same Artefact Research Center group**. The single most striking result is SIFT — a transformer replacing hand-engineered ETL features in Airbnb's *filter* ranking, fully deployed, with double-digit online engagement lifts.

---

#### 1. [SIFT: Search Intent-to-Filter Transformer for Multi-Task Personalized Filter Ranking at Airbnb](https://arxiv.org/abs/2610.07810)

- **ID**: `2610.07810v1` | **Cat**: cs.LG | **Submitted**: 2026-10-06 | **Comment**: 9 pages, 5 figures, 6 tables. **Accepted at GRAIL 2026** (Workshop on Generative, Retrieval-augmented, and Agentic Intelligence for Personalization, co-located with CIKM 2026, Rome)
- **Authors**: Shashank Dabriwal, Tanya Piplani, Hao Li, Yiwei Wang, Ashish Jain, Kedar Bellare, Stephanie Moyerman
- **Affiliation**: **Airbnb**, San Francisco, USA
- **PDF**: [Link](https://arxiv.org/pdf/2610.07810)

**Key contributions:**
- Attacking a concrete production problem: search *filters* (bedrooms, amenities, hotel-intent) are ranked by **hand-engineered, pre-aggregated ETL features**, which is expensive to maintain and hard to extend to new filter types or contextual dimensions (trip length, group size)
- SIFT is a transformer that learns a **unified guest representation directly from raw behavioral sequences**, feeding multiple prediction heads: booking likelihood, filter engagement, and **ordinal capacity thresholds** (e.g. "2+ bedrooms")
- A general filter-ranking framework that handles **both boolean and numeric-range filter types**; adding a filter requires only a **new head, not a new feature pipeline**
- Guest representation computed **offline on a daily cadence** rather than at request time, keeping serving fast
- **Offline**: +51.9% booking PR-AUC, +62.8% amenity-engagement PR-AUC over the production baseline
- **Online A/B**: +20.0% engagement with recommended filters, +0.72% overall filter usage, and +3.9% / +10.7% / +0.52% usage on newly-supported bedroom / bathroom / bed filters
- Extensibility demonstrated by shipping a **novel hotel-intent filter** on the same shared representation: **+3.8% uncancelled hotel bookings**, +0.76% overall marketplace bookings
- **Deployed in production**, serving millions of guests

**Notes:** The strongest industrial result this window and the closest thing to the CTR/ranking-scaling thread in [[ctr-scaling-landscape]]. The reusable idea is the **deployment shape**, not the architecture: precompute the user representation offline, attach task heads, add filters as heads. This is the same "reuse a shared representation across business tasks" pattern as HSTU and the Netflix/Kunlun scaling line, applied to a *two-sided marketplace filtering* surface rather than the feed.

---

#### 2. [A Systematic Investigation of Bias in Large Language Models for Advertising Relevance](https://arxiv.org/abs/2610.07544)

- **ID**: `2610.07544v1` | **Cat**: cs.AI | **Submitted**: 2026-10-06
- **Authors**: Weiwei Wang, Yinchuan Xu, Jialu Gao, Youkow Homma, Jian Jiao
- **Affiliation**: **Microsoft**
- **PDF**: [Link](https://arxiv.org/pdf/2610.07544)

**Key contributions:**
- LLMs increasingly **judge ad–query relevance**, yet the fairness of those judgments is largely unmeasured
- A **counterfactual framework** over query–ad pairs sampled from **real advertising logs**, varying advertiser identity / popularity, input language, and demographic wording
- Two judges studied: **GPT-4o** as a categorical relevance judge and a **Qwen-7B trained specifically for relevance prediction**
- Finding: for both models, **changing advertiser identity or input language can alter the relevance assessment**; selected demographic comparisons show patterns consistent with common stereotypes, particularly gender × occupation
- Studies mitigation at **inference time and training time**; effectiveness **depends on whether advertiser information is relevant to the query and how advertiser labels are distributed in training**

**Notes:** Directly relevant to the ads-relevance systems this wiki's CTR pages increasingly lean on as **label sources and evaluators**. The finding that advertiser identity alone moves a relevance judge is a measurement-integrity caution for anyone using an LLM as an offline relevance/CTR proxy — the same "reported capability ≠ verified capability" theme as papers 12, 18, 19 below.

---

#### 3. [Adapting Generative Recommenders for Multi-Turn Interaction (INTEGER)](https://arxiv.org/abs/2610.08136)

- **ID**: `2610.08136v1` | **Cat**: cs.IR | **Submitted**: 2026-10-06
- **Authors**: Yu-Chen Den, Zhi Rui Tam, Yung-Yu Shih, Shih-Hsin Wang, Yun-Nung Chen, Pu-Jen Cheng, Eugene Yang
- **Affiliations**: National Taiwan University (Taipei); **Johns Hopkins University**
- **PDF**: [Link](https://arxiv.org/pdf/2610.08136)

**Key contributions:**
- States the gap in generative recommenders: they decode items from interaction history but offer **no way to correct a miss within the interaction**, and naively adding conversation risks **overwriting the history-to-item mapping**
- **INTEGER** extends generative recommendation to multi-turn interaction with three components: (i) a **learned routing token** that decides *when* to recommend; (ii) **history re-anchoring** conditioning each item on both behavior and dialogue; (iii) **behavioral replay + instruction-data rehearsal** preventing forgetting during adaptation
- Items and words share the same output space, so conversation and recommendation are one sequence task
- On Amazon Beauty and Toys: matches or beats the strongest baselines on accuracy with competitive conversation quality, **+13.3% Hit@10 on Amazon Beauty**; significantly beats the generative recommender it starts from
- Analysis: INTEGER recommends **once intent is clear** and stays attentive to behavior at the recommendation moment; learns an **intent-agnostic replacement over the item space** that suppresses rejected items (attribute-aware feedback flagged as next step)

**Notes:** Part of the ongoing **conversational / agentic generative-recommendation** line (cf. `2610.08136`'s sibling themes and the RPORec / ThinkRec entries in [[rporec-reasoning-recommendation]] and [[thinkrec]]). The "training to converse overwrites the item mapping, so replay + rehearsal" framing is the same **catastrophic-forgetting constraint** that dominates this window's core-AI OPD papers.

---

#### 4. [Reinforcement Learning with Conformal Action Sets: An Application to Sequential Recommendation (RLCP)](https://arxiv.org/abs/2610.08743)

- **ID**: `2610.08743v1` | **Cat**: cs.LG, cs.AI | **Submitted**: 2026-10-06
- **Authors**: Wenwen Si, Honghao Wei
- **Affiliation**: ⚠️ **not stated** on the posted abs/HTML block
- **PDF**: [Link](https://arxiv.org/pdf/2610.08743)

**Key contributions:**
- Observation: sequential recommenders use a **fixed slate size** even though the number of useful alternatives **changes within a session**
- **RLCP (Reinforcement Learning with Calibrated Pruning)** adapts the retained action set using critic scores and an **online threshold** updated from binary feedback indicating whether the set contains a proxy-target action
- Proves a **deterministic bound on the observed proxy miss rate** along adaptive trajectories
- Derives an **exact decomposition of value loss** into *filtering* loss and *selection* loss; under explicit proxy/critic approximation conditions this yields a **finite session-reward bound** accounting for imperfect selection and set truncation, **without requiring convergence** of the learning parameters
- Experiments on **KuaiRand-Pure** and **MovieLens 1M**, two RLCP implementations vs four RL baselines: in **each of 19 configurations** at least one RLCP variant achieves the **highest catalog diversity (1.11×–5.21×** the strongest baseline), with competitive session depth and **no larger retained sets**

**Notes:** The contribution is the **calibrated variable-size slate** — most CTR/recsys work fixes top-K and tunes the ranker; this makes K itself an adaptive, guaranteed object. KuaiRand is an industrial short-video log, so this is a directly comparable offline recsys result for [[ctr-scaling-landscape]]. ⚠️ Affiliation not printed; not inferred.

---

#### 5. [Evidence Before Sampling: Interpretable Implicit Negative Candidate Discovery for Recommendation](https://arxiv.org/abs/2610.07708)

- **ID**: `2610.07708v1` | **Cat**: cs.AI | **Submitted**: 2026-10-06
- **Authors**: Shreya Rajpal, Sonia Sharma, Swapnil Parekh, Lisa Li, Jeyendran Balakrishnan, Nagaraj Janardhana, Andrew Mattarella-Micke
- **Affiliations**: 1 Michigan State University; 2 **Intuit**
- **PDF**: [Link](https://arxiv.org/pdf/2610.07708)

**Key contributions:**
- Negative sampling usually treats selected unobserved interactions as negatives, but **a missing interaction does not explain why** a user is uninterested, nor whether there is enough **evidence** to label it negative — especially in **business recommendation**, where negative signals must be interpretable and aligned with objectives
- Formulates the task as **implicit negative candidate discovery**: identify unobserved interactions *supported by observed customer behavior*
- Encodes behavior patterns as **symbolic rules**, scores them on support, informativeness, and product relevance, and **ranks retained rules by evidence**
- An **LLM interprets the retained rules** using business objectives and domain knowledge, combined with statistical evidence in a final report
- Industrial B2B evaluation plus five public datasets: higher candidate precision than baselines; symbolic selection improves downstream test **PR-AUC by 12.5%** over random selection (four negatives per positive)
- Core claim: **negative candidate validity can be evaluated separately from downstream recommendation performance**

**Notes:** A genuinely different negative-sampling philosophy for the CTR lane: **evidence-gated, rule-based, LLM-interpreted** negatives rather than sampled ones. The "validity is separable from downstream performance" claim is a useful measurement primitive, echoing this series' recurring focus on *auditing the training signal* rather than the model.

---

#### 6. [Personal-Agent Mediated Recommendation with Cross-Platform User History (MediateRec / PAMO)](https://arxiv.org/abs/2610.07588)

- **ID**: `2610.07588v1` | **Cat**: cs.AI, cs.LG | **Submitted**: 2026-10-06
- **Authors**: Yu Xia, Jiangfan Zhang, Jun Xiao, Julian McAuley, Xiangjun Fan
- **Affiliations**: **University of California San Diego**; **Meta AI** (work done during Yu Xia's internship at Meta)
- **PDF**: [Link](https://arxiv.org/pdf/2610.07588)

**Key contributions:**
- Formalizes **Personal-Agent Mediated Recommendation**: a platform recommender ranks a candidate set using **platform-local** information, then a **personal LLM agent** uses user-authorized **cross-platform history** to mediate the ranking into the final top-K slate
- Names the central tension: the platform ranking encodes strong **population evidence** the personal agent cannot observe, so mediation must balance **beneficial rescues vs harmful overrides**
- Introduces **MediateRec**, a benchmark with scalable proxy cross-platform environments and a **real cross-platform test** under a controlled platform–agent information boundary
- Proposes **PAMO (Personal Attribution Mediation Optimization)**: counterfactually **masks cross-platform history** to estimate personal mediation support and **reallocates rank-aware advantage mass** under a platform-relative value floor
- Proves PAMO preserves **cutoff-level advantage mass** and is **locally optimal** among first-order mass-preserving reallocations that do not lower average platform-relative value
- Result: personal-agent mediation enables meaningful platform corrections, **but even strong proprietary LLMs introduce non-negligible harmful overrides**; PAMO beats matched outcome-only RL across seen/unseen target platforms and the real cross-platform test

**Notes:** Connects directly to Karpathy's **BYOAI / personal-agent** arc ([[byoai]], [[karpathy-x-2026-llm-wiki]],
[[personal-agent-mediated-recommendation]]) — a *user-governed* personalization layer that sits **on top of** platform rankers rather than replacing them. The benchmark's explicit rescue/harm decomposition is the honest part: mediation is not free.

---

#### 7. [Disentangling Paradigm, Identifier, and Decoding in Generative Retrieval](https://arxiv.org/abs/2610.08716)

- **ID**: `2610.08716v1` | **Cat**: cs.IR, cs.CL | **Submitted**: 2026-10-06 | **Comment**: 13 pages, 7 figures, 11 tables
- **Authors**: Hicham Randrianarivo, Logan Renaud, Alexia Allal
- **Affiliation**: **Artefact Research Center**, France
- **PDF**: [Link](https://arxiv.org/pdf/2610.08716)

**Key contributions:**
- Methodological critique of generative retrieval: recent work replaces the autoregressive decoder with **diffusion** but changes **identifier, training recipe, and decoding at once**, so differences cannot be credited to the paradigm
- Controlled study on NQ320K and MS300K: trains **autoregressive, masked-diffusion, and block-diffusion** models with **residual-quantized, product-quantized, and random** identifiers, holding identifier length and training budget fixed, then decodes each model several ways
- **Decoding alone moves a diffusion model's Hit@1 by 6.6–13.7 points**
- Introduces **one-pass scoring** decoding: the model reads a fully masked identifier once and scores each document by its codes' probabilities; **matches or beats "generate-and-match" in 11 of 12 settings**
- Autoregressive models **still lead in Hit@1** — and on NQ320K the lead comes from the model, **not beam search**
- ⚠️ On NQ320K, **every paradigm largely memorizes** which identifier answers which query: **random identifiers keep 83–90% of the Hit@1** of residual-quantized ones

**Notes:** The last point is the most consequential for this lane — if arbitrary random DocIDs retain 83–90% of Hit@1, then a large share of generative-retrieval "semantic ID gains" is the model **memorizing query→DocID**, not the identifier's semantic structure. A direct measurement caution for the semantic-ID boom; pair with paper 8.

---

#### 8. [A Systematic Study of Semantic ID Spaces for Generative Information Retrieval](https://arxiv.org/abs/2610.08732)

- **ID**: `2610.08732v1` | **Cat**: cs.IR, cs.CL | **Submitted**: 2026-10-06 | **Comment**: 8 pages, 3 figures, 1 table
- **Authors**: Alexia Allal, Hicham Randrianarivo, Sylvain Lamprier
- **Affiliations**: **Artefact Research Center**, Paris, France; **LERIA, Angers University**, Angers, France
- **PDF**: [Link](https://arxiv.org/pdf/2610.08732)

**Key contributions:**
- Asks the under-explored question behind generative IR: **what makes a good DocID?** — current approaches rely on expensive downstream evaluation, hindering systematic analysis
- Proposes a **unified framework** that subsumes **Product Quantization (PQ), Residual Quantization (RQ), and their hybrid variants** in a single design space
- Systematically studies DocID properties — **hierarchy vs parallelism**, DocID **length**, **codebook size**
- Defines a suite of **training-free, intrinsic metrics** quantifying DocID quality and **structural fidelity** without full model training
- Extensive experiments on **MS MARCO 300K** and **NQ320K** linking structural properties to retrieval effectiveness

**Notes:** The companion to paper 7 from the same group: paper 8 provides the **training-free intrinsic metrics** to predict what paper 7 shows must be measured carefully. Together they form a rare **methodology-pair** — one says "you are crediting the paradigm for the decoder," the other says "here is how to score the identifier without training." Relevant to any CTR/recsys **semantic-ID** scheme (see [[vql]], [[chime]], the sibling `2610.05670` CreGR noted in the 10-06 digest).

---

### Core AI lane

Twelve papers in three clusters: **(a) looped / recurrent-depth and memory architectures** (four papers converging on "depth or memory that scales with sequence, not parameters"); **(b) on-policy distillation** (four papers, including a genuine safety threat model); **(c) measurement and alignment** (agents, scaling laws, formalization, world-model simulation).

---

#### 9. [Recurrent Looped Transformer](https://arxiv.org/abs/2610.07591)

- **ID**: `2610.07591v1` | **Cat**: cs.CL, cs.AI, cs.LG | **Submitted**: 2026-10-06 | **Comment**: Project page [github](https://github.com/yifanzhang-pro/recurrent-looped-tranformer)
- **Authors**: Yifan Zhang, Jichen Feng, Shihan Qin
- **Affiliation**: ⚠️ **not stated** on the posted HTML block
- **PDF**: [Link](https://arxiv.org/pdf/2610.07591)

**Key contributions:**
- Motivation: **state tracking requires an update at every input**, but a Transformer applies fixed depth per token regardless of sequence length
- **RLT** splits its layers between a **parallel causal encoder** and a **recurrent decoder**; at each token the decoder **merges the encoder output with the previous token's final decoder state**, so the computation path grows with sequence length at fixed per-token cost
- On six algorithmic tasks, compares five 8-layer splits against an 8-layer Transformer over three seeds
- **Parity**: trained on ≤40 bits, two RLT splits generalize to **256 bits at 100% accuracy in every seed**, while the Transformer stays at **chance**
- **Swap-based S₅ permutation tracking** at 8× training length: RLT reaches **97%** final-state accuracy vs **under 1%** for the Transformer; accuracy increases with decoder depth
- **Modular arithmetic** beyond training lengths: up to **93%** vs 33%
- Ablations: gains **depend on the feedback** — removing it drops parity and swap-S₅ to chance; **chunking the feedback** (once per four tokens) keeps 64-bit parity at 99% but drops length-64 swap-S₅ from 100% to 20% (permutation tracking needs **per-token** feedback)

**Notes:** The cleanest length-generalization result in this window. The key variable is **feedback granularity**: parallelizable chunked recurrence suffices for arithmetic/parity but not for state-tracking permutation. Relevant to the wiki's existing looped-transformer entries ([[training-free-looped-transformers]], `2610.07940` below, and the "hidden depth" thread in the 10-06 sibling).

---

#### 10. [SanSi: A Looped Typed Decision Model for System 1.5 Thinking](https://arxiv.org/abs/2610.07730)

- **ID**: `2610.07730v1` | **Cat**: cs.CL, cs.AI, cs.LG | **Submitted**: 2026-10-06 | **Comment**: 43 pages, 15 figures, 42 tables. Project page [minnesotanlp.github.io/Sansi](https://minnesotanlp.github.io/Sansi/)
- **Authors**: Shuyu Gan, Young-Jun Lee, Dongyeop Kang
- **Affiliation**: **University of Minnesota**
- **PDF**: [Link](https://arxiv.org/pdf/2610.07730)

**Key contributions:**
- Defines **System 1.5 thinking**: between a single-pass "typed decision" (System 1) and generated reasoning, **looping** the same layers several times before one typed readout lets the model revise its hidden state **without generating a token**
- **SanSi** turns a pre-trained looped LM into a typed decision model: option probabilities read after **every loop**, every loop trained with a **proper scoring rule**, so **one model serves every budget from 1 to 8 loops in a single run**
- On **10,027 test decisions from 59 sources**: **72.0%** accuracy — **+13.5 points** over a non-looped model of the same shape/recipe, **+5.3** over a newer non-looped model of its size, **−1.8** vs one with **3× parameters**
- On two **depth-controlled** tasks, loops extend the solvable depth **beyond depths seen in training**, where the larger single-pass model fails
- Used as the judge for policy optimization **without gold answers**, SanSi raises the generator's **F1 by 7.7 points**

**Notes:** The "one model, every loop budget" property is the reusable idea — **test-time compute as loop count without retraining**. The RL-judge application (no gold labels) connects to this wiki's verifier/RLVR thread ([[verifiable-rewards]], [[rlvr]]).

---

#### 11. [Hybrid Latent Attention for Looped Language Models (HLA)](https://arxiv.org/abs/2610.07940)

- **ID**: `2610.07940v1` | **Cat**: cs.CL, cs.AI | **Submitted**: 2026-10-06
- **Authors**: Yuhan Chen, Siyuan Zhang, Nan Wang, Feiyang Kang, Ruoxi Jia
- **Affiliations**: **Virginia Tech**; Independent Researcher
- **PDF**: [Link](https://arxiv.org/pdf/2610.07940)

**Key contributions:**
- States the looped-LM cost: applying the same layer stack **T times** deepens the model without parameters, but **multiplies the KV cache by T**, limiting concurrent sequences and slowing decode
- **HLA** keeps exact keys/values within a **sliding window of W recent tokens** and stores each older token as a **compact latent** that each loop's query reads **directly, without reconstructing keys/values**
- Up-trained on **Ouro looped models (T=4)**, 1.4B and 2.6B parameters, with **pretrained weights frozen** and only added parameters trained to reproduce the original attention
- **Cache shrinks 10.7× per token**, fits **4.0–8.8×** as many concurrent sequences per GPU, decode throughput **+2.5× at 1K** and **up to 7.4× at 16K** context
- Retains **>97%** accuracy on math/knowledge/reasoning and **96–100%** on long-context retrieval up to 16K; after SFT, on par with the fine-tuned original on competition math

**Notes:** The serving-side counterpart to paper 9 — if looped/recurrent-depth models become standard, their KV-cache multiplication is a hard serving constraint and HLA is a direct fix. Engineering-relevant to this wiki's KV-cache / long-context line.

---

#### 12. [Continuous Memory Machines (CMM)](https://arxiv.org/abs/2610.07907)

- **ID**: `2610.07907v1` | **Cat**: cs.AI | **Submitted**: 2026-10-06 | **Comment**: NeurIPS 2026 Workshop *Personalized, Aligned, Long-Term Memory for AI Systems (PALM)*
- **Authors**: Ciaran Regan, Kai Arulkumaran, Luke Darlow, Stefania Druga, Sebastian Risi, Llion Jones
- **Affiliations**: **University of Tsukuba**; **Sakana AI**
- **PDF**: [Link](https://arxiv.org/pdf/2610.07907) | **Code**: [SakanaAI/continuous-memory-machines](https://github.com/SakanaAI/continuous-memory-machines)

**Key contributions:**
- Diagnosis: RNNs compress information into a **single vector-valued recurrent state**, forcing **short-term computation and long-term retention to share one representation**
- **CMM** is a recurrent architecture with **matrix-valued short- and long-term memory states** serving distinct functional roles, built on the **Continuous Thought Machine (CTM)**
- Short-term memory tracks **recent neural activity**, with uniquely parameterized **neuron-level models** learning to use activity patterns for computation; a **persistent long-term memory** stores information for later use
- A **Transformer jointly updates both stores**, providing an expressive **bidirectional read–write** mechanism so each store can reorganize its own contents and read from / write to the other
- Across algorithmic, in-context-learning, and recurrent-reasoning tasks, CMM beats a broad baseline suite with **stronger generalization** than prior memory-augmented networks, **while preserving CTM's interpretable attention patterns**

**Notes:** ⚠️ Workshop paper (NeurIPS workshops, not main track). The **matrix-valued + separated-timescale** design echoes this wiki's existing memory work ([[mem1-agent]], the "continuous memory" direction). The "interpretable attention patterns preserved" claim is notable given how often memory capacity hurts interpretability.

---

#### 13. [Does On-Policy Distillation for Safety Pose Backdoor Risks?](https://arxiv.org/abs/2610.07654)

- **ID**: `2610.07654v1` | **Cat**: cs.LG, cs.AI | **Submitted**: 2026-10-06
- **Authors**: Jian Luo, Kehan Qi, Qingqiao Hu, Meilong Xu, Jiacheng Qiu, Weimin Lyu, Jiawei Zhou, Chao Chen
- **Affiliations**: **Stony Brook University**; **Amazon**
- **PDF**: [Link](https://arxiv.org/pdf/2610.07654)

**Key contributions:**
- Threat model: OPD is increasingly used to transfer **safety** from teacher to student, but assumes teacher and data are **trustworthy**
- Shows a **safety-aligned but backdoored teacher** can propagate hidden malicious behavior to an initially clean student; a poisoning rate as low as **3% yields up to 70% attack success rate (ASR)** on the distilled student
- Two amplifiers: (i) **more training epochs** — with only **10 poisoned samples**, ASR reaches **67% after 16 epochs**; (ii) **top-k KL** (vs sampled-token KL) **accelerates** trigger-conditioned harmful behavior in most settings
- Proposes a simple mitigation, **Lazy Defense**, clipping KL rewards to make student updates less aggressive — **delays** backdoor transfer at low poisoning rates

**Notes:** A distinct and under-covered **threat model for post-training**: the risk is not the data or the student but the **teacher as a supply-chain vector**. Directly relevant to this wiki's OPD cluster (papers 14–16) and to [[supply-chain-attacks]]. The "top-k KL is worse than sampled-token KL" result is a concrete recipe hazard.

---

#### 14. [Privileged Context as Drift in On-Policy Self-Distillation](https://arxiv.org/abs/2610.07842)

- **ID**: `2610.07842v1` | **Cat**: cs.LG | **Submitted**: 2026-10-06 | **Comment**: 18 pages, 4 figures, 5 tables
- **Authors**: Ravenor Davion, Nick Rui
- **Affiliation**: **Stanford University**
- **PDF**: [Link](https://arxiv.org/pdf/2610.07842)

**Key contributions:**
- OPSD trains a model to match a copy of itself conditioned on **privileged context**; existing work varies *what* the context contains and *how* it is produced while also changing models/data/setup, making the effect of context design **hard to isolate**
- Varies two axes: **content** (demonstration / feedback / rephrase) × **source** (external / self-generated with verifier / self-generated without verifier) → **nine combinations × three datasets**, training **Qwen2.5-7B**
- Finding: holding source fixed, **changing content spans a wider median-KL range than changing source** — **5.1×** for per-token KL and **2.2×** for per-sequence KL
- Parameter-update geometry agrees: adapters sharing **content** are more aligned (mean cosine **0.571**) than those sharing **source** (**0.255**)
- Implication for continual learning: **privileged context should be treated as part of OPSD's stability design**

**Notes:** The measurement that matters: it says the **content of the privileged context**, not its provenance, governs how far the policy drifts — which reframes "self-generated vs external" debates. Directly relevant to the 10-06 report's unresolved three-way OPD tension ([[arxiv-paper-check]] 2026-10-06): this paper supplies the variable that row was missing.

---

#### 15. [On-Policy Distillation with Negative-Policy Rollouts (NP-OPD)](https://arxiv.org/abs/2610.07874)

- **ID**: `2610.07874v1` | **Cat**: cs.LG | **Submitted**: 2026-10-06 | **Comment**: 25 pages, 7 figures, 24 tables
- **Authors**: Jaehui Hwang, Dongyoon Han, Sangdoo Yun, Byeongho Heo
- **Affiliation**: **NAVER AI Lab**
- **PDF**: [Link](https://arxiv.org/pdf/2610.07874) | **Code**: [naver-ai/np-opd](https://github.com/naver-ai/np-opd)

**Key contributions:**
- Observation: OPD supervision is centered on **mimicking the teacher**; when a stronger teacher has **limited distributional overlap** with the student, positive guidance provides **insufficient learning signal**
- **NP-OPD** complements teacher supervision with rollouts from a **lower-performing, lower-capability negative policy**, used as a negative reference
- Rather than changing the distillation reward, NP-OPD introduces the negative policy at the **rollout stage**, continuously supplying tokens preferred by the negative policy **over the teacher**, keeping them exposed to teacher supervision throughout training
- Improves OPD across **model scales, generation modes, reasoning domains, and OPD variants**
- Analysis: NP-OPD **suppresses tokens preferred by the negative policy** and moves the student away from it

**Notes:** A clean "add the missing negative class" idea for distillation: OPD has only positive labels, and NP-OPD manufactures contrast from a weaker model rather than a better one. ⚠️ No absolute numbers in the abstract; improvements are reported relative to OPD variants.

---

#### 16. [Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability](https://arxiv.org/abs/2610.08448)

- **ID**: `2610.08448v1` | **Cat**: cs.CL, cs.AI | **Submitted**: 2026-10-06
- **Authors**: Bingxi Hou, Guochao Jiang, Guofeng Quan, Weiqing Li, Wenfeng Feng, Guohua Liu, Yuewei Zhang
- **Affiliation**: **Alibaba Cloud Computing**
- **PDF**: [Link](https://arxiv.org/pdf/2610.08448)

**Key contributions:**
- Cross-tokenizer OPD must align teacher/student at both sequence and vocabulary levels; this paper asks whether **expanding alignment coverage improves learning**
- Across **three heterogeneous teacher–student pairs** on math reasoning and code generation: **strict 1:1 groups already cover most student-generated tokens** despite substantial vocabulary mismatch; the shared vocabulary retains nearly all probability mass at strictly aligned positions
- Restricting **reverse KL to a student-selected top-16 subset** of the shared vocabulary at each strict position achieves accuracy **comparable to full shared-vocabulary OPD**, beating evaluated cross-tokenizer baselines
- **Counterintuitive negative result**: adding MSE supervision on span log-probabilities in mismatch groups gives **complete coverage yet reduces accuracy**; span gradients show weak or negative directional agreement with strict gradients and grow in magnitude
- Conclusion: shift from maximizing **alignment coverage** to prioritizing **supervision reliability** — compact supervision at strict positions beats broader coverage that injects weakly aligned/conflicting signals

**Notes:** The "more supervision made it worse, and here is the gradient diagnostic why" result is the kind of mechanism-level negative finding this series has been tracking since the 10-06 report. Relevant to any distillation across heterogeneous tokenizers (increasingly common as student/teacher vocabularies diverge).

---

#### 17. [Stateless Language Agents: Scaling Long-Horizon Automated Research (SLA)](https://arxiv.org/abs/2610.07625)

- **ID**: `2610.07625v1` | **Cat**: cs.LG, cs.AI, cs.CL | **Submitted**: 2026-10-06 | **Comment**: 32 pages
- **Authors**: Qizheng Zhang, Changxiu Ji, Isaac Sun, Yuetai Li, Shubhangi Upasani, Sherry Ruan, Boyuan Ma, Fenglu Hong, Vamsidhar Kamanuru, Yoonho Lee, Yuzhen Mao, Genghan Zhang, Rulin Shao, Qiuyang Mang, Andy Dimnaku, Changran Hu, Radha Poovendran, Kunle Olukotun
- **Affiliations**: **Stanford University**; **Carnegie Mellon University**; **University of Washington**; **SambaNova Systems**
- **PDF**: [Link](https://arxiv.org/pdf/2610.07625) | **Code**: [Alex-q-z/stateless-language-agents](https://github.com/Alex-q-z/stateless-language-agents)

**Key contributions:**
- States the failure mode of long-horizon automated research: more inference does not produce more progress — agents **replay growing histories, duplicate work, or stop experimenting while tokens keep burning**; most evaluations use short budgets or saturating benchmarks that hide this
- Traces failures to **where research state lives** and **who decides what to try next**
- **Stateless Language Agents (SLAs)**: the principle of **stateful search with stateless agents** — no agent carries its conversation across invocations; the **harness owns the research state** and reconstructs a **fresh, role-specific context** per invocation
- Implemented in the SLA framework: a **stateless Advisor** reads harness-summarized evidence across search directions and assigns concrete experiments to **parallel Workers**
- Evaluated against three recent frameworks on **software engineering, kernel optimization, and algorithm design**, budgets up to **one billion tokens**: SLA achieves the **best final result on every task** and reaches the strongest kernel baseline's final performance with **>84% fewer tokens**
- Ablations from shared checkpoints: focused contexts and explicit assignments each contribute; the **Advisor consumes <0.6% of tokens**

**Notes:** Deeply relevant to this wiki's **agentic-engineering / autoresearch** arc ([[autoresearch]], [[claws]], [[karpathy-x-2026-autoresearch-and-claws]]). The core proposal — keep durable research state **out of agent conversations** — is a direct counter to the "ever-growing context window" convention, and the >84% token reduction is the strongest efficiency number of the window.

---

#### 18. [Toward Alignment Scaling Laws: A Framework and First Preregistered Measurements](https://arxiv.org/abs/2610.08540)

- **ID**: `2610.08540v1` | **Cat**: cs.AI, cs.CL, cs.LG | **Submitted**: 2026-10-06 | **Comment**: 34 pages, 24 figures, 8 tables. Games: [aisafety.fun](https://www.aisafety.fun); preregistrations: [osf.io/wda8q](https://osf.io/wda8q), [osf.io/q2j3y](https://osf.io/q2j3y), [osf.io/8kreb](https://osf.io/8kreb)
- **Authors**: Jeremy Canale (sole author)
- **Affiliation**: independent (personal site `jeremycanale.com`)
- **PDF**: [Link](https://arxiv.org/pdf/2610.08540)

**Key contributions:**
- Treats alignment as **a family of measurable scaling relations**, not one property: for each risk category r, the **alignment burden** to hold a fixed safety target is modeled as **B_r(N)=a_r·N^α_r**, with N a capability proxy; against a budget ∝ N, scaling **helps if α_r<1**, **keeps pace if α_r≈1**, and **accumulates alignment debt if α_r>1**
- Distinguishes **observed, audited, and true** alignment; a toy model in which corrections consume capability headroom
- **Proofs**: the **largest exponent among corrected risks** (not an average) sets the long-run regime; above 1, any policy holding headroom above a floor must grow **super-exponentially**; for burdens that are **positive mixtures of power laws**, fits on small models **underestimate** large-scale exponents; an audit with no false positives **never underestimates** true alignment
- **Preregistered measurement 1** (reanalysis of public adversarial-training data, Pythia classifiers): compute needed to bring attack success under 10% grows as **N^0.60** (scaling helps)
- **Preregistered pilot 2** (Qwen2.5 0.5B–72B, replicated on Qwen3 0.6B–14B): **α = −0.05 for truthfulness** and **0.48 for stated dispositions** (both scaling helps under the reduced rule, though local slopes approach 1 at the top); **sycophancy 0.89** (0.83 with two extra seeds) and a **planted backdoor** are **undetermined** — the backdoor is removed quickly when its trigger is known but **survives blind safety training at four of five sizes**
- Explicitly makes **no claim** about which regime current frontier models occupy

**Notes:** The frame — **per-risk exponents, and the max exponent governs** — is the reusable contribution; it turns "does alignment get easier?" into a **pre-registrable** measurement with a stated falsifiability boundary. Relevant to [[verifiable-rewards]], [[verification-gap]], and the wiki's scaling-law line. ⚠️ Sole-author preprint; the "undetermined" backdoor result is reported honestly rather than spun.

---

#### 19. [An AI-Assisted Formalization of the Poincaré Conjecture](https://arxiv.org/abs/2610.08329)

- **ID**: `2610.08329v1` | **Cat**: cs.AI, math.GT | **Submitted**: 2026-10-06 | **Comment**: 15 pages, 2 figures. Code: [frenzymath/PoincareConjecture](https://github.com/frenzymath/PoincareConjecture)
- **Authors**: Zhiyuan Zhang, Axel Delaval, Leheng Chen, Jinxuan Chen, Jie Xu, Yuxuan Liao, Jiedong Jiang, Chunlei Liu, Bin Dong
- **Affiliation**: ⚠️ **not stated** on the posted HTML block
- **PDF**: [Link](https://arxiv.org/pdf/2610.08329)

**Key contributions:**
- Presents an **AI-assisted Lean 4 formalization of the Poincaré conjecture**, starting from **limited reusable formal infrastructure** for the geometric analysis behind the proof
- Organizes the work with a **proof blueprint** prepared by mathematicians plus **explicit milestone statements**, which enabled **parallel agent work** and gave mathematicians clear points to locate blockers and give guidance
- The paper's real content is the analysis of **human interventions and organizational choices** behind the workflow, not the AI capability alone
- Frames the output as a **starting point toward reusable infrastructure** for future formalization in geometric analysis

**Notes:** The most prominent formalization artifact this window, and a companion to the wiki's existing Anthropic Riemann-zeta entry ([[anthropic-riemann-zeta]]) — the recurring lesson across both is that the **human-curated milestones and blueprint** are the load-bearing part, not raw agent throughput. ⚠️ No numeric success metrics in the abstract; affiliation not printed.

---

#### 20. [WorldSolver: Can LLM Agents Simulate the Physical Dynamics via Solver Generation?](https://arxiv.org/abs/2610.08720)

- **ID**: `2610.08720v1` | **Cat**: cs.AI | **Submitted**: 2026-10-06
- **Authors**: Siru Jiang, Yongzhe Lyu, Shuo Lu, Yubin Wang, Yuxiang Zhang, Yue Liao, Bin Wang, Jian Liang, Tieniu Tan
- **Affiliations**: NLPR & MAIS, **CASIA**; **PKU**; **Huawei Noah's Ark Lab**
- **PDF**: [Link](https://arxiv.org/pdf/2610.08720) | **Code**: [sirujiang/WorldSolver](https://github.com/sirujiang/WorldSolver)

**Key contributions:**
- Frames **physics-solver generation** as a hard, practical testbed for LLM agents: solver construction requires **physical understanding** (choose the model), **mathematical reasoning** (formulate the dynamics), and **software engineering** (implement as code)
- **WorldSolver** is a benchmark of **168 simulation tasks** derived from physical phenomena in **61 classic computer-graphics papers**, spanning **7 physical domains**; each task ships a **fixed simulation code scaffold** with the solver left for the agent to complete
- Three evaluation dimensions: **Execution Checks**, **Visual Fidelity** (reproduce intended dynamic behavior), and **Physical Plausibility** (physics-grounded verification of generated dynamics)
- Frontier agents: producing **executable** solvers is itself difficult, and visual/physical correctness is harder; **GPT-5.6-Sol (48.7%)** and **Claude-Opus-5 (46.7%)** lead but remain below half

**Notes:** A **saturation-resistant, verifiable** benchmark — the physical-plausibility dimension is grounded in the graphics literature, not a learned judge. The sub-50% frontier scores make it a useful counterpoint to world-model papers that report convincing-looking rollouts (cf. the world-model line in [[game-rl-daily]]).

---

## Cross-cutting observations

1. **The CTR lane's best results are production results, not architecture results.** SIFT is *deployed* with online A/B lifts (paper 1); RLCP reports 19/19 configurations on an industrial log (paper 4); Evidence Before Sampling is a live **B2B** study (paper 5). The window's most reusable CTR artifact is the **deployment pattern** (offline shared representation + task heads + filters-as-heads), not a new attention block. Contrast with the 10-06 window, whose CTR lane was industrial in *authorship* but had no online numbers.
2. **Generative-retrieval methodology is under audit — and the two papers come from the same group.** Papers 7 and 8 (Artefact Research Center) attack the field from both sides: paper 7 shows **decoding and identifier choices alone move Hit@1 by 6.6–13.7 points** and that **random DocIDs keep 83–90%** of semantic-DocID Hit@1; paper 8 provides **training-free intrinsic metrics** to score DocIDs without training. This is the sharpest "is the semantic-ID gain real?" challenge this wiki has recorded.
3. **On-policy distillation is the window's densest cluster (papers 13–16), and it splits into four orthogonal concerns:** *security* (13 — a backdoored teacher poisons the student), *stability/continual learning* (14 — privileged-context **content** governs drift), *signal insufficiency* (15 — add a negative policy), and *alignment reliability* (16 — more supervision coverage **hurts**). Together they make a strong case that OPD's design space is not "distill harder" but "distill more carefully."
4. **"Depth/memory should scale with sequence, not parameters" is a four-paper convergence (papers 9–12).** RLT (recurrent depth), SanSi (looped typed decisions), HLA (looped-KV serving fix), and CMM (separated timescale memory) all attack the fixed-per-token-compute constraint from different layers. Two of the four are explicitly **serving-aware** (HLA) or **budget-flexible** (SanSi), which is where this line becomes deployable.
5. **Measurement/negative results again outnumber method wins in the AI lane.** Paper 2 (advertiser identity moves relevance judges), paper 7 (random IDs retain most of the gain), paper 14 (content, not source, governs drift), paper 16 (more supervision reduces accuracy), paper 18 (sycophancy/backdoor **undetermined**), and paper 20 (frontier agents **below 50%** on executable physics). This series' recurring finding — reported capability and verified capability diverge in the same direction — holds for a third consecutive window.
6. **Agent architecture is turning against the ever-growing context.** SLA (paper 17) explicitly keeps durable state **out of agent conversations** and reconstructs fresh contexts per invocation, reaching >84% token savings — the same "context engineering over context accumulation" theme in Karpathy's **build-for-agents / BYOAI** arc ([[build-for-agents]], [[context-engineering]], [[byoai]]). Paired with the wiki's existing personal-agent entry (paper 6), this window makes the personal/multi-agent *state* question — **who owns it, where it lives** — the cross-cutting agent theme.
7. **Nothing in this window is a new CTR-prediction *architecture* paper.** As in the 10-06 report, the CTR-scaling thread in [[ctr-scaling-landscape]] — GRAB, LoopCTR, EST, CADET — gains **no new entrant**. The lane's contributions are in **filter ranking** (SIFT), **fairness of LLM relevance judges** (paper 2), **conversational generative rec** (INTEGER), **variable-size slates** (RLCP), and **evidence-gated negatives** (paper 5). Recorded explicitly so a gap is not read as an absence of interest.

---

## Also worth recording (not detailed above)

- **`2610.08407`** — *Seeing the Context: Enhancing Recommender Systems with Image-Derived Contextual Signals* (Tal Cordova, Tomer Geva, Moshe Unger; **Tel Aviv University**, Coller School of Management). **Accepted at the CARS workshop, RecSys 2026.** Proposes image-derived context (physical / social / modal categories from a VLM) and the **ICE-Fuse** pipeline on TripAdvisor data. ⚠️ Image context **does not beat established signals standalone** but helps **combined** — an honest complementarity result, not a win.
- **`2610.08245`** — *Aligning Performance with Contribution: Towards Contribution-Aware Fair Recommendation* (Shuai Zhang, Hui Fang, Zun Sun; **Shanghai University of Finance and Economics**; **Singapore University of Technology and Design**). Proposes **Contribution-Performance Fairness** and **CPFR**; a game-theoretic analysis argues the alignment strengthens contribution incentives. Applied to three datasets × three backbones.
- **`2610.07731`** — *Learning to Retrieve via Reinforcement Learning in Embedding Space (RELER)* (Qi Liu, Fengming Liang, Yiqun Chen, Erhan Zhang, Jiaxin Mao; **Renmin University of China**). RL over embedding actions sampled from **von Mises–Fisher** distributions with RLOO and **conditional-mean projection** to cut sampling noise; beats InfoNCE and LambdaLoss on **BRIGHT** nDCG@10 with BGE-M3 / Qwen3-Embedding, and improves RAG answer quality on seven QA datasets.
- **`2610.08132`** — *Beyond Marginal Monitoring: Distributed Joint-Distribution Testing for Data Concept Drift in Large Scale E-Commerce Operations* (Cagdas Pullu et al.; **Trendyol Group**; **Istanbul Technical University**). Evaluates five multi-column two-sample tests on a **137.5-million-row Trendyol collection-ranking feature table**; distributed **MMD with Random Fourier Features on Spark** achieves **r=0.940** with expected drift magnitude, **80.4% TPR / 3.2% FPR**, while per-dimension **KS failed** from statistic saturation on ID-like columns.
- **`2610.07960`** — *From Delivery to Stateful Exploration: Rethinking the Index for Agentic Search (IndexAct)* (Deogyong Kim, Sunghwan Kim, Sangam Lee, Wonjae Lee, Dongha Lee; **Yonsei University**). Separates **candidate-set refinement from text inspection** — agents manipulate persistent candidate sets over an inverted index, receiving state references and counts rather than passages; outperforms baselines on five agentic-search/multi-hop benchmarks.
- **`2610.07663`** — *Joint Workflow and Prompt Optimization for User Behavior Simulation (SWORD)* (Nipun B Nair, Tongtong Wu, Hongzhi Yin, Hui Li, Weiqing Wang; **Monash University**; **University of Queensland**; **Xiamen University**). Jointly optimizes multi-agent **workflow topology + natural-language prompts** guided only by a scalar task metric; **$4–$6 API cost per dataset**; autonomously discovers review-sentiment mapping rules and epidemiological decay priors from scalar error alone.
- **`2610.08076`** — *SpeedrunBench: Challenging LLM Agents with Video Game Speedrunning* (Yoshinari Fujinuma et al.; **Patronus AI**; **University of Washington**; **Institute of Science Tokyo**). Nine games; agents approach human world records on simple platformers but **fall behind on longer, more complex games** under practical budgets. Saturation-resistant by construction (a faster time always exists).
- **`2610.08033`** — *Learning in Dreams, Winning in Reality: A Continuous Dyna Loop for a Ten-Hero MOBA* (Jordy Kieto). A structured multi-agent world model of a 10-hero MOBA (206 units, up to 6,000 ticks); a policy trained **only in imagination** wins **70.2% of real games** as radiant (up from 0% for dream-only and 33.7% before the loop). ⚠️ **Wins none as dire** (and neither does the shipped opponent). The honest finding: **model exploitation is invisible from inside the dream**.
- **`2610.08691`** — *ScienceClaw: Benchmarking Continual Self-Evolution of AI-for-Science Agents* (Mingda Zhang et al.; **CUHK-Shenzhen**; **NTU**; **Duke-NUS**). Formalizes **fixed-parameter program self-evolution**; ScienceClaw-Eval spans 23 disciplines and measures correctness, **evolutionary gain, retention, cross-dataset transfer, and evolution cost**.
- **`2610.07979`** — *Learning from Revision Consequences: Hindsight Meta-Experience Distillation (HMED)* (Qianhan Feng, Zhongzhen Huang, Yakun Zhu, Xiaofan Zhang, Qi Dou). Separates **Task-Skills** from **Meta-Skills**; re-executes incumbent and revised Meta-Skills from the same restored discovery state to isolate what a revision changed, distilling a reusable **Meta-Experience**. Directly relevant to the 10-06 window's Agent-Skill line.

---

## Method disclosure, dedup, and cautions

**Harvest**: arXiv API over HTTPS, 5 category queries (`cs.IR`, `cs.AI`, `cs.LG`, `cs.CL`, `cs.CV`) restricted by `submittedDate:[202610060000 TO 202610072359]`, `sortBy=submittedDate desc`, `max_results=200`, with a **second page** fetched for `cs.AI` (221 total) and `cs.LG` (204 total) when the first page filled → **472 unique entries, all published 2026-10-06**.

⚠️ **Two limits are recorded because they bound the yield**:
- **No `abs:` topical passes were run this time.** Selection was by **primary category + title/abstract scanning** of the common categories only, so a CTR/ads paper filed **outside cs.IR/AI/LG/CL/CV** (e.g. cs.GT, cs.MA, econ.EM) or dated outside the window was **not seen**. Today's yield is a **lower bound**.
- **ID-level dedup only, no title-level pass.** The 2026-10-06 and 2026-10-05 runs both record that **ID-only dedup has already produced duplicate papers** in this series; the sibling-collision risk is real and mitigated here only by the fact that no sibling digest existed at write time.

⚠️ **Window framing**: "last 24 hours" is not what arXiv exposes. All 472 harvested entries carry `published = 2026-10-06`, the newest announcement block available at run time (no 2026-10-07 submissions exist in the API). This report therefore covers the **2026-10-06 announcement (submission date 2026-10-06)** — a **single-day** window, explicitly *not* a rolling 24 hours.

⚠️ **Dedup**: baseline built by regex-extracting every `NNNN.NNNNN` pattern from all `wiki/**/*.md` → **7,985 unique arXiv IDs**. **472 of 472 window entries unclaimed.** **All 20 featured IDs re-verified 0-hit against that baseline immediately before writing** — no sibling-claimed overlap to report because no 2026-10-07 sibling digest existed at write time.

⚠️ **Affiliation discipline**: institutions read **only** from each paper's own LaTeXML author block / institutional address block, **never inferred from author surnames, email domains, or reputation**. **Affiliations recovered for 13 of 20 featured papers**; the remainder (papers 4, 9, 19, and the author affiliation of paper 18) are marked **"not stated on arXiv"** rather than inferred. One correction of note: **paper 6** carries **both UC San Diego and Meta AI** — the arXiv block states the work was done during the first author's **Meta internship**, so both are recorded. Paper 16 resolves to **Alibaba Cloud Computing** (a paper with an industry provenance that is worth flagging for the CTR/IR lane). Paper 12 resolves to **University of Tsukuba + Sakana AI** (the Sakana provenance is only visible in the LaTeXML author block, not the abs page).

⚠️ **Venue discipline**: **4 of 20 carry a venue** — `2610.07810` (**GRAIL 2026 workshop**, co-located with CIKM 2026), `2610.08407` (**CARS workshop, RecSys 2026**), `2610.07907` (**NeurIPS 2026 *Workshop* PALM**), and the workshop classification of any others are **not** main-track. **The remaining featured papers are unreviewed preprints.** **No result in this report was independently replicated**, and none was replicated by a second group.

⚠️ **Claim-level cautions carried inline**: paper 4's affiliation is unstated; paper 7's "random identifiers keep 83–90% of Hit@1" is a single-dataset (NQ320K) finding; paper 11's retention figures are on the Ouro looped backbones only; paper 12 and paper 15 report no absolute numbers in the abstract; paper 13's mitigation **delays** rather than prevents backdoor transfer; paper 18 explicitly declares sycophancy and backdoor regimes **undetermined**; paper 19 reports no numeric success metric; paper 20's benchmark is new and has no external reproduction yet.

⚠️ **This report is a candidate for the next lint**: the recurring OPD tension flagged in the **2026-10-06** report (OPSD collapse vs OPSD no-forgetting) now has a candidate reconciling variable — paper 14's **privileged-context content**, and paper 13's demonstration that **teacher trustworthiness** is a separate axis entirely. Both should be cross-checked when the 10-06 papers' follow-ups appear.

---

## Sources / Links

All 20 featured papers link directly to `https://arxiv.org/abs/{ID}`; PDFs are `https://arxiv.org/pdf/{ID}`. Window = `submittedDate:[202610060000 TO 202610072359]`, announced **2026-10-06**.
