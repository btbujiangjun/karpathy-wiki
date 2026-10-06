---
title: ArXiv Paper Check - AI & CTR (2026-10-06)
type: synthesis
created: 2026-10-06
updated: 2026-10-06
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, auctions, generative-recommendation, post-training, evaluation, routing, safety]
---

# ArXiv Paper Check - AI & CTR (2026-10-06)

**Search**: `cat:cs.IR`, `cat:cs.AI`, `cat:cs.LG`, `cat:cs.CL`, `cat:cs.CV` restricted to `submittedDate:[202610050000 TO 202610072359]`, plus topical `abs:` passes on *click-through / CTR / recommendation / ranking / cold-start / ads*. Announced window = **2026-10-05 (all 464 harvested entries carry this date)**.

**Dedup baseline**: 7,964 unique arXiv IDs already claimed repo-wide → **462 of 464 window papers are unclaimed**. All 22 featured IDs re-verified 0-hit immediately before this write.

⚠️ **Window caveat, stated up front**: this is a *single-day* harvest (2026-10-05 submissions), not a rolling 24 hours. §8 explains why the "last 24 hours" framing and the announcement date diverge on arXiv and what that costs.

---

## Interesting Papers

### CTR / Ads / Recommender lane

The headline finding for this series' core specialty: **the CTR lane produced 11 papers, and 3 of them are from Google, Meta, and Criteo AI Lab** — this window is unusually industrial for an unreviewed arXiv block. Two papers are also directly on ads auctions, which this wiki has essentially no coverage of.

---

#### 1. [MIRT: Transformers for Truthful Generative Auctions with Whole-feed Permutation Externalities](https://arxiv.org/abs/2610.06559)

- **ID**: `2610.06559v1` | **Cat**: cs.GT, cs.LG | **Submitted**: 2026-10-05 | **Comment**: 24 pages (10 main + 14 appendix), 6 figures
- **Authors**: Ali Elahi, Ermis Soumalias, Jason Cheuk Nam Liang, Daniel Yao, Michael J. Curry
- **Affiliations**: University of Illinois Chicago; **Meta**
- **PDF**: [Link](https://arxiv.org/pdf/2610.06559)

**Key contributions:**
- States the externality problem directly: an item's CTR depends on its surrounding content, not only its own position, yet platforms rank ads and organic content separately before blending
- Introduces **Maximal-in-Range Transformer** (MIRT): a transformer generates a *range* of candidate feeds jointly ordering ads + organic; the welfare-maximizing feed in the range is selected
- Resolves the mechanism's central tension — strategyproofness demands a **bid-independent** range even though feed welfare depends linearly on bids — with an RL objective covering both candidate generation and bid-aware selection
- Bounds the pseudo-dimension of MIRT under hard attention: near-optimal expected welfare learnable with sample complexity polynomial in transformer size, **logarithmic in range size**
- Beats the previous *non-strategyproof* state of the art on welfare while remaining **exactly** strategyproof

**Notes:** The most theoretically substantive ads paper this wiki holds. Directly comparable to the CTR literature recorded in [[ctr-scaling-landscape]] but orthogonal — it optimizes *feed composition under incentive compatibility* rather than *single-model accuracy*. See §9 for a caution on the welfare metric.

---

#### 2. [BRANCH-MoE: Balance-Aware Tree Routing for Large Embedding Models](https://arxiv.org/abs/2610.06725)

- **ID**: `2610.06725v1` | **Cat**: cs.LG, cs.AI | **Submitted**: 2026-10-05 | **Comment**: 26 pages, 7 tables, 2 figures
- **Authors**: Gang Fu, Adel Javanmard, MohammadHossein Bateni, Vahab Mirrokni
- **Affiliations**: **Google Research**; University of Southern California (Javanmard)
- **PDF**: [Link](https://arxiv.org/pdf/2610.06725)

**Key contributions:**
- Places $E$ experts at the leaves of a binary decision tree of depth $\log_2 E$; branching probability at each internal node is centred on the **arrival-weighted mean score** of traffic reaching that node
- That mean is tracked by an **exponential moving average**, which promotes utilization of both child subtrees **without an auxiliary load-balancing loss** (the usual DeepSeek-V3 dynamic-bias / Switch-softmax aux loss is exactly what this removes)
- Derives an explicit **noise-lag trade-off** for the EMA estimate; proves that for linear node maps and log-concave arrival distributions the mechanism **prevents routing-mass collapse**
- Proves two operational corollaries: under a frozen router an expert's execution frequency controls its stochastic-gradient convergence rate; and confident near-root decisions **bound cross-device communication** when experts are placed by tree prefix
- **Evaluated on Criteo click-through-rate prediction** plus Forest Covertype, HIGGS, YearPredictionMSD; $E=16$, top-4 routing, 5 seeds

**Notes:** ⚠️ The Criteo CTR run is one of four benchmarks and the paper reports no effect sizes in the abstract — this is an **embedding-scaling** contribution, not a CTR-prediction contribution. Its relevance to this lane is that CTR is the load-bearing industrial test case for the routing claim. Pairs with [[cipher-moe-workload-imbalance]]'s finding below (that workload imbalance is a system problem, not a router problem) — two papers, same week, opposite solutions.

---

#### 3. [MatrixFormer: A Foundation Model for Matrix Completion](https://arxiv.org/abs/2610.06751)

- **ID**: `2610.06751v1` | **Cat**: cs.LG, cs.AI | **Submitted**: 2026-10-05 | **Comment**: 17 pages, 5 figures
- **Authors**: Dwaipayan Saha, Jacob Feitelberg, Kyuseong Choi, Raaz Dwivedi, Anish Agarwal
- **Affiliations**: Columbia University; **Cornell Tech**
- **PDF**: [Link](https://arxiv.org/pdf/2610.06751)

**Key contributions:**
- Argues existing tabular foundation models **discard the matrix's 2-D structure** by treating completion as entry-by-entry prediction with repeated context
- A **matrix-native transformer** predicts a full distribution for *every* missing entry in a **single forward pass**
- Trained **entirely on synthetic** low-rank and latent-factor matrices under diverse missingness patterns
- Applied **zero-shot with identical weights** to causal-inference panel data, LM benchmark-score completion, tabular imputation, and recommendation matrix completion

**Notes:** The single-pass full-missing-set prediction is the interesting primitive — a CTR model over a candidate slate is exactly a matrix-completion-shaped problem, so this is a plausible backbone for slate-level modeling rather than pointwise scoring. ⚠️ No CTR/slate benchmark is reported; the recsys application is one of four evaluation settings and no numbers appear in the abstract.

---

#### 4. [SPRIG: Semantic-ID-enhanced Paths for Knowledge Graph-based Generative Recommendation](https://arxiv.org/abs/2610.06590)

- **ID**: `2610.06590v1` | **Cat**: cs.IR | **Submitted**: 2026-10-05 | **Comment**: **Accepted as a short paper at CIKM 2026**; 5 pages, 1 figure, 2 tables
- **Authors**: Justin Hangöbl, Marta Moscati, Alessandro B. Melchiorre, Shah Nawaz, Markus Schedl
- **Affiliations**: Institute of Computational Perception, Johannes Kepler University (Linz); **Albatross AI**; **Criteo AI Lab** (Paris)
- **PDF**: [Link](https://arxiv.org/pdf/2610.06590) | **Code**: [github](https://github.com/justinhangoebl/semantic-id-knowledge-graph-recommender)

**Key contributions:**
- Formalizes the two generative-recommendation tracks as having **complementary blind spots**: Semantic-ID (SID) models lack relational grounding; KG-path generative recommenders still represent items as opaque tokens tied to large embedding tables, blocking parameter sharing and generalization
- SPRIG trains on **information-rich KG paths that terminate in items represented as discrete, content-derived tokens**
- Competitive performance on movie and music datasets against sequential-LM, KG-augmented, and SID baselines, with **fewer parameters and lower compute cost**
- Code released

**Notes:** Peer-reviewed (CIKM 2026 short) and from **Criteo AI Lab** — the second Criteo-linked paper in this window, which is why the ads lane looks strong today. Note the honest framing: "competitive … while using fewer parameters" is an **efficiency claim, not a quality claim**.

---

#### 5. [MATE: Adaptive Long- and Short-Term User Memory for LLM-Based Recommendation](https://arxiv.org/abs/2610.06050)

- **ID**: `2610.06050v1` | **Cat**: cs.IR | **Submitted**: 2026-10-05
- **Authors**: Yu Hou (sole author)
- **Affiliation**: School of Mathematics and Computing (Computational Science and Engineering), **Yonsei University**, Seoul
- **PDF**: [Link](https://arxiv.org/pdf/2610.06050)

**Key contributions:**
- Identifies the unresolved question in LLM recommenders: semantics alone don't tell you **which historical behaviors are persistent preferences vs. recent interests**
- Each new interaction gets scored on two temporal axes — is it **repeatedly supported by history**, and is it **consistent with recent interactions**
- That "temporal evidence" gates two user memories: **long-term** conservatively preserves persistent preferences, **short-term** rapidly adapts
- A recent-context representation **dynamically weights** the two memories per request
- Offline: next-item prediction jointly optimized with temporal supervision. Online: **shared model frozen, only the two user memories update** — i.e. personalization without any weight update, which is the production-friendly part
- **+7.0–13.2% mean NDCG@10** over the strongest external baseline on MovieLens-10M, Amazon Luxury Beauty, and **KuaiRec**

**Notes:** KuaiRec is an industrial short-video log, so this is one of the few papers this window with a real online-distribution test. Single-author paper — see §9.

---

#### 6. [Beyond States: Investigating the Effects of Context on User Modeling with Feature-Conditioned Markov Models](https://arxiv.org/abs/2610.06060)

- **ID**: `2610.06060v1` | **Cat**: cs.IR | **Submitted**: 2026-10-05
- **Authors**: Jana Isabelle Friese, Andreas Konstantin Kruff, Timo Breuer, Philipp Schaer, Norbert Fuhr
- **Venue**: **CIKM '26** (definitive version of record, DOI `10.1145/3799682.3840602`)
- **PDF**: [Link](https://arxiv.org/pdf/2610.06060)

**Key contributions:**
- Classical state-based user models (Markov) can't incorporate decision-relevant context; a **feature-conditioned Markov model** makes transition probabilities functions of positional, content-based, and interaction-derived features
- Keeps the structural simplicity and computational efficiency of state-based models (the stated constraint)
- A **multi-level framework** assessing both predictive fit *and* behavioral fidelity, decomposed across datasets, search settings, and feature configurations
- Result: contextual features **do** improve reproduction of real user interaction, but effectiveness **hinges on search scenario and modeling objective** — there is no one-size-fits-all feature set

**Notes:** Explicitly a *user-simulation* paper for IR evaluation, not a ranker. Relevant to this lane because user simulators are how offline CTR evaluation is bootstrapped — and this paper's finding is that simulator fidelity is **setting-specific**, which is a direct caution against reusing one simulator across search scenarios.

---

#### 7. [Generate What You Can Trust: Content Credibility in Generative Recommenders](https://arxiv.org/abs/2610.05670)

- **ID**: `2610.05670v1` | **Cat**: cs.IR | **Submitted**: 2026-10-05
- **Authors**: Zhuo Cai, Guanghao Wu, Shoujin Wang, Peilin Zhou, Victor W. Chu
- **Affiliations**: Data Science Institute, **University of Technology Sydney**; **New York University Abu Dhabi**
- **PDF**: [Link](https://arxiv.org/pdf/2610.05670)

**Key contributions:**
- Names the gap: generative recommendation optimizes accuracy while neglecting **credibility** of what it generates, exposing users to uncredible content (fake news) with trust and reputational consequences
- **CreGR** attacks both GR stages. *Tokenization*: a **credibility-aware tokenizer** learns discriminative tokens for credible vs. uncredible items, disentangling credibility at token level. *Generation*: an **accuracy-preserving credibility-oriented generator** on discrete diffusion
- The generation stage uses **asymmetric masking probability reduction** — selectively down-weights tokens associated with uncredible content while leaving **user-preference signal tokens untouched**, so accuracy is preserved by construction
- Three real-world datasets

**Notes:** The "leave preference tokens alone" mechanism is the transferable idea — it means credibility intervention does not have to trade off against relevance. ⚠️ **No effect sizes, no dataset names, and no metric definitions appear in the abstract**; recorded as a mechanism contribution (single-source).

---

#### 8. [Cut Binary Cross Entropy: Efficient Large-Vocabulary Loss and Gradient Kernels for Sequential Recommendation](https://arxiv.org/abs/2610.05559)

- **ID**: `2610.05559v1` | **Cat**: cs.LG, cs.AI, cs.AR, cs.IR | **Submitted**: 2026-10-04 (in the 10-05 announcement)
- **Authors**: Yaoyiran Li, Haowen Ning, Mohamed Hammad
- **Affiliation**: **Google Cloud** (London UK; Mountain View USA)
- **PDF**: [Link](https://arxiv.org/pdf/2610.05559) | **Code**: [open-sourced](https://github.com/AI-Hypercomputer/RecML/blob/main/recml/core/ops/binary_cross_entropy_ops.py)

**Key contributions:**
- The concrete systems problem: industrial sequential recommenders run over 10⁵–10⁷ items and train multi-label models with BCE over the **full vocabulary**, which materializes a dense $[B,N,V]$ logits tensor in HBM → $O(BNV)$ memory and **fatal OOM**
- Notes the gap precisely: chunked loss optimizations exist for **Softmax** CE in LLMs, but large-scale **multi-label BCE** optimization "remains unexplored across deep learning ecosystems"
- **CutBCE**: an *exact* fused reformulation evaluating dense background loss plus sparse target corrections; a custom **VJP with a dedicated Pallas TPU backward kernel** computing logit tiles on-chip in both passes so **logits and their gradients never reside in HBM**; dynamic VMEM budgeting and sharding-aware collective hoisting; count-based zero-overhead training metrics
- **Single-chip TPU v5e/v6e**: eliminates OOM, up to **91.9% speedup**
- **8-chip slice, multi-label SASRec with 876k items on Yambda-50M**: **−65.7% peak HBM (>14 GiB saved per chip)**, **+225.9% training speed**, comparable accuracy

**Notes:** The most concretely reusable artifact in this report — it is **open-sourced**, exact (not approximate), and the gap it identifies is one this wiki's CTR corpus has never covered. The 876k-item Yambda-50M setup is a real production recommender workload. ⚠️ The Yambda dataset is Google's, so this is not an independently replicated result.

---

#### 9. [Reading the Mood: Emotion-Guided Book-to-Music Recommendation via CGANs and LLMs](https://arxiv.org/abs/2610.06703)

- **ID**: `2610.06703v1` | **Cat**: cs.IR, cs.CL, cs.LG | **Submitted**: 2026-10-05 | **Comment**: **Accepted at SENTIRE 2026 (ICDM 2026 Workshops)**; 9 pages
- **Authors**: Manousos Linardakis, Georgios Alexandridis
- **Affiliations**: National Technical University of Athens; National & Kapodistrian University of Athens
- **PDF**: [Link](https://arxiv.org/pdf/2610.06703)

**Key contributions:**
- Task: recommend background music matching a book's mood, to improve reading immersion
- Two phases. *Phase 1*: transformer-based **sentiment embeddings** from user reviews, mapped across domains by a **Conditional GAN** whose **mask-conditioned generator handles missing sentiment components** and injects stochasticity; a compact rating network fuses sentiment-specific scores with a CF prior
- *Phase 2*: LLMs classify each book into a **valence-arousal quadrant**; candidate tracks are filtered to match
- **Amazon (English) RMSE 0.98**, **Douban (Chinese) RMSE 0.91** (best / lowest respectively), ranking competitive with the strongest sentiment-aware baseline **even cross-lingually**

**Notes:** Included for one reason only: it is a **cross-lingual** recsys result with reported numbers on both an English and a Chinese platform, which is rare in this lane. ⚠️ Workshop paper (ICDM workshops, not main track); the RMSE figures are ~0.9–1.0 on a 1–5 rating scale, i.e. modest absolute error, and "competitive" on ranking is a hedge, not a win.

---

### Core AI lane

Ten papers, selected for signal. Three clusters: (a) **post-training and continual learning** — three independent papers this window converge on the same negative result about on-policy distillation; (b) **measurement** — four papers auditing whether our instruments work; (c) **efficiency/routing**.

---

#### 10. [Off-Policy Merging Beats On-Policy Self-Distillation for Continual Learning](https://arxiv.org/abs/2610.05872)

- **ID**: `2610.05872v1` | **Cat**: cs.LG, cs.AI, cs.CL | **Submitted**: 2026-10-05
- **Authors**: Chen Henry Wu, Thomas Zhang, Aditi Raghunathan
- **Affiliation**: **Carnegie Mellon University** (all three; recovered from the PDF title block — arXiv serves **no HTML** for this ID)
- **PDF**: [Link](https://arxiv.org/pdf/2610.05872) | **Code**: [github](https://github.com/ar-forum/grafting)

**Key contributions:**
- Directly challenges a standing belief: conventional wisdom holds **on-policy training is a prerequisite for continual learning** on post-trained models
- Separates two facts normally conflated: **SFT does learn a useful signal from new data**, but naively applying its update interferes with existing capabilities
- **Grafting** fixes this by changing *where* the update is learned and *how* it is applied: (1) learn the update on an earlier **donor checkpoint**, ideally before end of pretraining, then apply it to the post-trained model; (2) **scale** the weight update (equivalent to a form of model merging); (3) optionally **mask the most sensitive update directions** when the new data distribution is far from the post-trained model
- **Pareto-dominates both SFT and OPSD** on new-task *and* old-task performance across three settings: distilling expert traces, self-improvement with STaR and Pedagogical RL, and injecting knowledge after the pretraining cutoff
- Avoids expensive on-policy sampling entirely

**Notes:** ⚠️ **The most consequential paper in this report for this wiki's post-training entries.** See §7 — this *contradicts* the direction of `2610.05200` and `2610.04978` in the same window.

---

#### 11. [Learning without Overwriting: A Theory of Self-Distillation and Supervised Fine-Tuning in Continual Reasoning](https://arxiv.org/abs/2610.05200)

- **ID**: `2610.05200v1` | **Cat**: cs.LG | **Submitted**: 2026-10-04 (in the 10-05 announcement)
- **Authors**: Shinichi Uemura, Taiji Suzuki
- **Affiliations**: Center for Advanced Intelligence Project, **RIKEN** (Tokyo); Department of Mathematics Informatics, **The University of Tokyo**
- **PDF**: [Link](https://arxiv.org/pdf/2610.05200)

**Key contributions:**
- Models LLM reasoning as **search over a DAG** and gives a unified theory of both OPSD and SFT dynamics in continual learning, plus the effect of pretraining
- Three findings with an optimization guarantee: **(i)** OPSD with hints from correct outputs enables continual learning **without forgetting**, via sparse-yet-effective gradient updates induced by the hint structure; **(ii)** SFT on correct reasoning paths can cause **catastrophic forgetting**, via dense updates along the training path that overwrite prior information; **(iii)** **pretraining diversity is crucial** for a post-trained model to reach a correct output when a rollout starts from an intermediate state

**Notes:** Finding (ii) is the theoretical counterpart of paper 10's empirical claim that "naively applying its update interferes with existing capabilities." ⚠️ Note that 52-page total / 11-page main — the theory is in the main text, experiments largely in appendix.

---

#### 12. [What Will Post-Training Fix? Per-Problem Gains Are Shared Across Independent RL Runs](https://arxiv.org/abs/2610.04978)

- **ID**: `2610.04978v1` | **Cat**: cs.LG | **Submitted**: 2026-10-04 (in the 10-05 announcement) | **Comment**: 10 pages, 2 figures
- **Authors**: Xiaoxian Duan (sole author)
- **PDF**: [Link](https://arxiv.org/pdf/2610.04978)

**Key contributions:**
- Tests the assumption underpinning data selection, curricula, and recipe evaluation: that you can tell *before training* which problems a model will improve on
- Setup: two base models (DeepSeek-R1-Distill-Qwen-1.5B, Qwen2.5-Math-1.5B), **18 post-training runs**, up to 1532 competition math problems, many samples per problem
- Introduces a **noise ceiling** from agreement between disjoint run subsets, as the correct reference scale
- Three findings holding on both base models: **(a)** independent runs agree on which rarely-solved problems improve, noise ceiling ≈ **0.9**, yet the two base models agree with each other at only **ρ = 0.25** — *the shared component belongs to the base model, not the problem*; **(b)** a priori signals (base pass rate, likelihood of a correct solution, a larger model's pass rate, and combinations) explain only **0.30 and 0.24** of explainable variance; **(c)** **existing checkpoints are the better predictor** — a single checkpoint from another family predicts a new run better than every a priori signal (**0.52 vs 0.33**; **0.34 vs 0.17** against combined signals)
- Robust to 2025–2026 competition problems and to independently-estimated baselines; proposes the noise ceiling as a standard companion to per-problem signals

**Notes:** Finding (a) is the sharpest: it says "what post-training fixes" is **not a property of the problem**, which undercuts problem-difficulty-based curricula. ⚠️ Two of the three selected papers in this report are single-author (`2610.04978`, `2610.06050`); see §9.

---

#### 13. [Judged Useless, Queried Anyway: Tool-Using Agents Rarely Turn Their Own Evidence Judgments into Stopping Decisions](https://arxiv.org/abs/2610.06191)

- **ID**: `2610.06191v1` | **Cat**: cs.AI, cs.CL | **Submitted**: 2026-10-05 | **Comment**: 37 pages, 6 figures, 28 tables
- **Authors**: Chubin Zhang, Zhenglin Wan, Xingrui Yu, Jingxuan Wu, Yaxin Zhou, Ivor Tsang, Bo An
- **Affiliations**: Nanyang Technological University; National University of Singapore; CFAR, A*STAR; UNC-Chapel Hill; Carnegie Mellon University
- **PDF**: [Link](https://arxiv.org/pdf/2610.06191) | **Code**: [github](https://github.com/bennidict23/judged-useless-queried-anyway)

**Key contributions:**
- The dissociation: agents **judge** a failing tool's results useless **97–100%** of the time, yet **rarely stop** on that judgment
- Method that isolates it: comparing stopping at the same step after longer vs. shorter runs of agent-judged-useless results — this contrast is **zero** for clock- or deadline-driven stopping, which rules out those as explanations
- Prompt cues change *when* agents stop but not *what* they stop on. Permission to answer from memory and a reasoning mode bring early stops **regardless of evidence**; a stated budget just moves 7–8B models' stops to the deadline; an explicit stopping rule or call cost is followed at most partly
- The one thing that works is **harness-level**: enforce an integration step requiring an answer after five consecutive agent-judged-useless results. This raises failing-source success for every model, **keeps the stopping point fixed when the budget doubles**, and needs no extra judgment call when the agent already states its judgments
- **Pre-registered replication on 300 fresh questions** confirms both the dissociation and the rule's effect

**Notes:** The best-designed negative result in this window. Pre-registration + a matched control that zeroes out the trivial explanation + a replication is the standard this lane of agent papers usually misses.

---

#### 14. [Copies or Sources? Measuring How LLM Aggregators Count Restated Evidence in Multi-Agent Systems](https://arxiv.org/abs/2610.06192)

- **ID**: `2610.06192v1` | **Cat**: cs.AI | **Submitted**: 2026-10-05
- **Authors**: Jianxin Gao, Runze Li, Tianyi Yu, Liangwei Ren, Bohan Chen, Zining Wang
- **Affiliations**: China Agricultural University; Jilin University; Tianjin University of Finance and Economics; Tianjin University of Science and Technology
- **PDF**: [Link](https://arxiv.org/pdf/2610.06192)

**Key contributions:**
- Multi-agent systems restate observations as a matter of course (relays forward them, shared boards repeat them, discussion rounds echo them). **An aggregator should count sources, not statements** — this paper quantifies the gap
- The instrument: converts a reported probability into **units of independent readings**, assigning every restatement a **copy weight** — 0 for an aggregator counting sources, 1 for one counting every statement — yielding the implied decision under any cost structure
- Three testbeds holding evidence fixed while varying *how* it is restated: message logs with an **exact Bayesian oracle**, web documents with appended copies, and logs written by LLM agent teams under four communication protocols
- Across four models from three providers, a forwarded copy counts for **0.06 to 0.42** of a new reading — mostly because some replies count every statement
- On **5–40% of logs stating one reading three times**, the reported belief implies an **early commitment the oracle never makes**
- **Fixes are cheap and measured**: a one-paragraph declaration of what a copy contributes brings copy weight to **≤ 0.08** on controlled logs; a rule that has agents **refer to readings instead of restating them** cuts belief-implied early commitment from **11.2% → 1.1%** while preserving genuine corroboration

**Notes:** The copy-weight framing is a genuinely reusable measurement — it converts a vague complaint ("multi-agent systems over-count evidence") into a scalar on [0,1] with a known oracle value.

---

#### 15. [Can Language Models Learn to Reject Their Own Bad Reasoning Steps?](https://arxiv.org/abs/2610.05976)

- **ID**: `2610.05976v1` | **Cat**: cs.CL | **Submitted**: 2026-10-05
- **Authors**: Siheng Xiong, Xiaoze Liu, Yiqiao Jin, Xiaoqian Wang, Jing Gao
- **Affiliations**: Georgia Institute of Technology; Purdue University
- **PDF**: [Link](https://arxiv.org/pdf/2610.05976)

**Key contributions:**
- Verifier-guided decoding normally needs an **external learned verifier**; this asks whether the generator can reject its own bad steps
- Defines a prefix's **recoverability** = probability the frozen generator can complete it correctly. Diagnostics: adjacent recoverability changes are often **unresolvable at practical Monte Carlo budgets**, while same-prefix candidates show a **sparse low-recoverability tail** — i.e. the signal is sparse, not continuous
- **Self-Step Rejection (SSR)**: a lightweight LoRA **acceptance gate** on the generator backbone, base model frozen
- Training signal is **confidence-qualified first-passage supervision**: steps before the first *resolved* crossing of a root-relative recoverability barrier are accepted, the crossing step rejected, and unresolved steps and suffixes are **excluded** — deliberately training only where the label is trustworthy
- Combines pointwise classification, same-prefix pairwise learning, and group-relative policy refinement using final-answer correctness
- Across **three reasoning models and five math benchmarks**: **+5.4–10.1 points macro-average accuracy** over single-pass decoding at **1.21–1.40× tokens**; highest macro-average among evaluated step-level methods, **without an external verifier**

**Notes:** The first-passage exclusion rule is the load-bearing design choice and is the kind of detail that distinguishes a paper that will replicate from one that won't. ⚠️ Math-only evaluation.

---

#### 16. [Evolving in Thought Space: Training a Small Model at Test Time Unlocks Better Discoveries](https://arxiv.org/abs/2610.06269)

- **ID**: `2610.06269v1` | **Cat**: cs.AI, cs.LG | **Submitted**: 2026-10-05 | **Comment**: 35 pages incl. references and appendices
- **Authors**: Chonghe Jiang, Ao Qu, Siyuan Liu, Ruoyun Ma, Zijian Zhou, Dingyi Zhuang, Bo Liu, Han Zheng, Hanfei Yu, Baichuan Mo, Jinhua Zhao, Paul Pu Liang
- **Affiliations**: MIT; Hong Kong Polytechnic University; ByteDance; National University of Singapore; Stanford; University of Washington; UC Berkeley; Tsinghua; SMART
- **PDF**: [Link](https://arxiv.org/pdf/2610.06269)

**Key contributions:**
- Context: methods like TTT-Discover update the solution-generating LLM from verifier feedback, but this is expensive when reliable *execution* needs a large model — gradients, optimizer states, and policy statistics must be maintained while generating long structured outputs
- **Credit assignment problem stated cleanly**: outcome-level verifier feedback must jointly evaluate high-level strategy and low-level implementation
- **Guidance-TTT** separates the roles: a **compact guidance model is trained at test time** to propose high-level strategic changes; a **frozen execution model** implements them as complete executable solutions
- Each step: select a promising previously-discovered solution → propose a change → execute and verify → update **only the guidance model** via an adaptive group-relative RL objective
- Concentrates test-time learning on **short strategic decisions** while retaining the implementation capability of a much stronger unadapted model
- **Without web access**, produces strong solutions across **four distinct domains** (combinatorial…; the abstract is truncated at the domain list)

**Notes:** The "small model trained, large model frozen" inversion is the reusable idea, and it generalizes beyond discovery to any setting where a strong model is expensive to update. ⚠️ The abstract truncates before naming the four domains and before any numbers; recorded as a framing contribution.

---

#### 17. [CIPHER-MoE: Balancing Efficiency and Routing Fidelity in Trillion-Scale MoE Training](https://arxiv.org/abs/2610.05744)

- **ID**: `2610.05744v1` | **Cat**: cs.LG, cs.AI | **Submitted**: 2026-10-05
- **Authors**: Jing Li, Jian Meng, Yingmeng Gao, Suming Qiu, Linyuan Qiu, Dongfang Li, Baotian Hu, Binfan Zheng, Rongqian Zhao, Weijian Sun, Xin Chen
- **Affiliations**: Tongji University; **Cornell University**; Harbin Institute of Technology, Shenzhen; AI Training Platform Team, Shenzhen Loop Area Institute
- **PDF**: [Link](https://arxiv.org/pdf/2610.05744)

**Key contributions:**
- Frames MoE workload imbalance as a **system** problem: non-uniform token routing → imbalanced expert workloads across experts *and devices* → destabilized training; at trillion-scale the cost of underloaded experts and hot experts both rise
- Notes existing fixes (intricate parallelism strategies, resource reallocation) **add resource requirements and orchestration complexity** — unaffordable under constrained compute
- **CIPHER-MoE** mitigates imbalance while keeping the router's **token-side Top-K selection unchanged** — the key constraint, since prior work changes routing semantics
- Mechanism: **affinity-aware Expert-to-Token filtering with explicit capacity control**, no additional hardware resources, no complex runtime design
- Evaluated on large-scale MoE models including **DeepSeek-V4-Pro**: up to **64.9 percentage points Top-1 expert workload reduction** and **1.10×–1.94× training acceleration**, preserving training quality

**Notes:** ⚠️ **"DeepSeek-V4-Pro" could not be independently verified** — see §9. Pairs with paper 2 (BRANCH-MoE, same window) as a clean contrast: BRANCH changes the router to fix balance *without* an aux loss; CIPHER keeps the router untouched and filters downstream. If both hold, they compose.

---

#### 18. [On Hyperparameter Tuning on the Test Set](https://arxiv.org/abs/2610.05902)

- **ID**: `2610.05902v1` | **Cat**: cs.LG, cs.AI, cs.CV | **Submitted**: 2026-10-05
- **Authors**: Matteo Fregonara, Tom Viering, Jan van Gemert
- **Affiliation**: **Delft University of Technology**
- **PDF**: [Link](https://arxiv.org/pdf/2610.05902)

**Key contributions:**
- Attacks a piece of received wisdom directly: "don't tune hyperparameters on the test set" is called a cardinal sin, yet evidence says it happens, so the question is **how bad is it, really**
- Systematic study of the performance inflation on **MNIST-1D, CIFAR-10, and three GLUE tasks**
- Findings: the effect is **real and significant but frequently small relative to other sources of noise**; in many cases tuning on the test set recovers **exactly the same model** as tuning on the validation set; and **model rankings are essentially preserved**
- Conclusion: consistent test-set tuning may **not invalidate benchmarks or model selection**; argues for openly *reporting* test tuning rather than policing it

**Notes:** ⚠️ **Controversial and small-scale** — MNIST-1D, CIFAR-10, and 3 GLUE tasks do not support a general claim about large-scale benchmarks, and "same model recovered exactly" is a strong statement I could not verify beyond the abstract. Recorded as a challenge to a convention, not as a refutation. Relevant to this wiki because several of its CTR pages record leaderboard gains; if the inflation is small in these regimes, cross-paper CTR comparisons are less corrupted than assumed — **but this is not established for CTR**.

---

#### 19. [Byte Language Models: Scaling, Emergent Abstractions, and Information Allocation](https://arxiv.org/abs/2610.05978)

- **ID**: `2610.05978v1` | **Cat**: cs.CL, cs.LG | **Submitted**: 2026-10-05
- **Authors**: Jie Wang, Shiwei Luo, Qi Zhang, Yuanbin Wu
- **Affiliations**: School of Computer Science, **East China Normal University**; School of Computer Science, **Fudan University**
- **PDF**: [Link](https://arxiv.org/pdf/2610.05978)

**Key contributions:**
- Tokenizer-free LMs remove fixed-tokenizer inductive bias by modeling text as bytes, at the cost of longer sequences and **loss of explicit text abstractions**; the question is whether the extra compute is useful and whether standard Transformers can learn what tokenization provides
- Uses **token-superposition training and hash embeddings** on Transformers with **no specialized tokenization-related architecture**
- Byte Transformers **consistently outperform subword Transformers as model size scales**
- **They build local text abstractions as external tokenizers**: a set of segmentation-like positions collects local context representations, and **restricting up to 25% of intermediate layers to these local representations preserves downstream performance**
- Those learned structures induce **highly non-uniform generation difficulty**, with uncertainty concentrated near local structure boundaries; exploiting them for speculative decoding yields **3.4× more accepted tokens** than subword Transformers

**Notes:** The "segmentation-like positions as an emergent external tokenizer" finding is the interesting one — it argues tokenization's benefit is recoverable by architecture-free learning. ⚠️ ⚠️ **The abstract reports no absolute model sizes, no benchmark scores, and no perplexities** — all comparisons are relative. Also relevant to this lane indirectly: a tokenizer is exactly what CTR work uses for IDs (semantic IDs, see papers 4 and 7).

---

#### 20. [The Optimization Landscape of Learning Compacted Context Models](https://arxiv.org/abs/2610.05885)

- **ID**: `2610.05885v1` | **Cat**: cs.LG | **Submitted**: 2026-10-05
- **Authors**: Thomas Villeneuve, Alex Sandomirsky, Charles O'Neill, Max Kirkby, Michael Psenka
- **Affiliation**: **Base Labs** (all five)
- **Venue**: **NeurIPS 2026 Workshop** — *Continual Learning in the Era of Foundation Models and Embodied Agents*
- **PDF**: [Link](https://arxiv.org/pdf/2610.05885)

**Key contributions:**
- Continual learning framed through **infinite context windows**: as an agent puts more observation into the KV cache, compacting that context is **direct memory manipulation without touching base-model weights** — an alternative to weight-space continual learning
- The setup: learn a smaller set of KV vectors that matches the full cache's behaviour. This preserves base-model behaviour but makes the optimization problem **nontrivial, with a brittle and flat loss landscape** — and the paper's contribution is characterizing *why*
- A heavily simplified **Perceiver-based architecture matches a full Perceiver transformer** on continuous context compaction and **outperforms baselines on compaction utility**
- Evaluated on MCQ tasks across **Finance, Legal, Gutenberg, and Code**

**Notes:** The framing is the transferable part — KV compaction as a *weights-preserving* continual-learning channel, which is a third option alongside paper 10's grafting and `2610.05200`'s theory. ⚠️ Workshop paper (NeurIPS workshops, not main track); no numeric table appears in the abstract, and "outperforms baselines on compaction utility" names no margin. MCQ-only evaluation on four text domains.

---

## Comparison: the three post-training papers in this window

This window contains an unusually clean three-way disagreement, recorded rather than reconciled:

| | `2610.05872` (CMU) | `2610.05200` (RIKEN/UTokyo) | `2610.04978` (single author) |
|---|---|---|---|
| **Claim type** | Empirical, Pareto-dominance | Theoretical (optimization guarantee) | Empirical, measurement |
| **On OPSD** | **Beats it** — OPSD causes reasoning collapse; use off-policy **grafting** instead | **Works** — OPSD with hints enables continual learning without forgetting | Not the subject; measures what post-training fixes |
| **On SFT** | Learns useful signal, but naively applied it interferes with existing capabilities | **Catastrophic forgetting** via dense updates along the training path | Not the subject |
| **Why no contradiction** | Grafting changes *where* the update is learned (donor checkpoint) and *scales/masks* it | The no-forgetting result is for OPSD *with hints from correct outputs* — a supervised signal OPSD papers of the collapse type often lack | Independent question (predictability of per-problem gains) |

⚠️ **The genuine tension**: `2610.05872` reports OPSD causing **reasoning collapse**; `2610.05200` proves OPSD **enables** continual learning. These are not reconciled by the papers. The most likely reconciling variable is the **hint signal** — `2610.05200`'s guarantee is conditional on correct-output hints, and `2610.05872`'s collapse claim concerns the self-distillation setups (STaR, Pedagogical RL) where the "correct" outputs are the model's own and may be wrong. **This is my inference, not a claim either paper makes.** Flagged for the next lint to re-check when either group posts a rebuttal.

---

## Cross-cutting observations

1. **The CTR lane is unusually industrial this window — 3 papers from Google (Cloud, Research ×2), Meta, and Criteo AI Lab.** Two separate Google papers (paper 2 routing for embeddings, paper 8 loss kernels for large-vocabulary recsys) plus a Google billion-scale thumbnail bandit in the 10-04 batch is the highest industrial density this series has recorded in one window.
2. **The unifying theme across papers 2, 3, 8, 17 is "stop treating the vocabulary/candidate set as a flat thing."** Paper 8 stops materializing the dense logits tensor; paper 2 imposes a topology on experts; paper 3 makes the model matrix-native so the 2-D structure is used rather than flattened. Same underlying realization in four different layers.
3. **Measurement papers outnumber method papers in the AI lane** (13, 14, 18, plus `2610.05830` and `2610.06251` in §8). Four of them find that **reported capability and verified capability diverge in the same direction — over-crediting**. Paper 13: judges correct, acts wrong. Paper 14: counts copies as sources. Paper 18: challenges the test-set convention. `2610.05830`: the reproduction scorer **failed its validation gate** and the contamination gap came back **inconclusive**. `2610.06251`: 170/384 four-bit answers changed when only a *companion* request changed.
4. **Three papers report negative or null results and are the most reusable items here** — 12 (a priori signals explain ~0.3 of variance; checkpoints predict better), 18 (test-set tuning inflates less than feared), 13 (judgments don't drive stopping).
5. **A new measurement primitive appeared that is worth stealing: the "copy weight" scalar in paper 14** — restated evidence converted to units of independent readings, with an exact Bayesian oracle, on [0,1]. This is the same shape as this wiki's existing pass@k vs pass^k distinction (see `2609.38121` in the game-RL lane) and would apply to any multi-agent aggregation.
6. **Nothing in this window is a strong CTR-prediction architecture paper.** The closest are papers 2 and 3 (Criteo used as a benchmark) and paper 5 (KuaiRec, +7.0–13.2% NDCG@10). The CTR-scaling thread in [[ctr-scaling-landscape]] — GRAB, LoopCTR, EST, CADET — **had no new entrant in this window**. Recorded explicitly so a gap is not mistaken for an absence of interest.

---

## Also worth recording (not detailed above)

- **`2610.05830`** — *Measurement-First Auditing of Agentic Leaderboards* (Dishu Yang, Qi Su, Hongbo Qin, Hansong Zhang; Northeastern / GWU / UC Berkeley). Across **nine HAL configurations, none of 27 channel assessments was coded closed**, though incidents were confirmed in four. On a SWE-bench Verified file-localization gap: GPT-4.1 showed a **+10.0-point** pair-weighted Top-3 benchmark-associated gap, but **both the prespecified paired-bootstrap and the post-hoc repository-balanced 95% intervals included zero** → inconclusive. ⚠️ **The reproduction scorer failed its validation gate** (insufficient sensitivity for either model; both DeepSeek-V4-Flash firings on correct-gold comparisons were false positives). Explicitly does *not* establish training-data membership, contamination prevalence, or score inflation.
- **`2610.06251`** — *Shared Stopping Decisions Change Answers in HQQ Cache Quantization* (Seunghui Jwa, Minsu Oh, Chanjun Park, Yeo-Chan Yoon). Changing **only which unrelated question was batched** with the target changed four-bit HQQ answers in **170/384** comparisons across two models; replaying the companion's update counts reproduced the changed answer in **every** pair, both directions. Native HQQ also changed confirmed numerical correctness in **8** arithmetic pairs. Conclusion: request-independence audits must cover **stopping decisions**, not just quantization groups.
- **`2610.04860`** — *Invisible Ink, Visible Lies: How Production Watermarking Causes LLMs to Hallucinate* (Haocheng Ye, Aoting Hu, Xinwei Zhang, Xunzhu Tang, Shuchao Pang, Jason Xue; NJUST / Anhui Univ. of Technology / HKPolyU / Univ. of Luxembourg / CSIRO). **Accepted at NeurIPS 2026.** Across **six** watermarking methods (KGW, SWEET, DiPmark, GumbelSoft, Gumbel-Max, SynthID) watermark-induced hallucination appears **even when the evidence is present and the unwatermarked model answers correctly**. Two mechanisms: current-step token perturbation and **prefix-induced attention drift accumulating through autoregressive decoding**. Two plug-in interventions cut factual errors ~**90%** at matched TPR 0.90 @ 1% FPR. **In the 10-04 batch, not the 10-05 window** — recorded here because it is the strongest peer-reviewed item adjacent to this lane.
- **`2610.05685`** — *Spend Bytes on Breadth: Precision-Count Trade-offs for Decode-Time KV Compression in Long Chain-of-Thought Reasoning*.
- **`2610.05686`** — *Do Time-Series QA Systems Read the Time Series?* (Zhuomin Chen et al.; FIU / U. Houston / NEC Labs America / SMU). Introduces **COMMON-TSQA**; finds rationales "often contain time-series claims unsupported by the input," and that rationale–answer agreement coexists with incorrect numerical descriptions.
- **`2610.05550`** — *When Low Prediction Error Misleads Planning* (Rui Min, Xianyao Li, Fang Xu, Eric Jing Du; under review, 40 pages). **Center error dominates MSE in 14/16** model-task cells, yet in **six** of them an oracle correcting only action-relative responses beats one correcting only the center on physical rank correlation. Careful split of error magnitude from decision effect. ⚠️ **Closed-loop planning gains remain unconfirmed** by the paper's own admission.
- **`2610.05833`** — *Request Order Matters: Cache-History Sensitivity in Selective KV-Cache Reuse for Rolling Agents*. Same family as `2610.06251`, independently: unchanged prompt, different answer depending on preceding requests; document-aligned recomputation cuts answer variation **69.0% → 26.1%** at a matched 5% budget.
- **`2610.06347`** — *ImproveAnyTask* (Xingbo Yao et al.). Autonomous post-training harness: **+18.29 / +11.97 pp** mean gains on Base/Instruct, max **+41.96 pp**, 11 tasks, 24-hour budget on 8×H20.
- **`2610.06105`** — *Flash-OPD*. Reframes on-policy-distillation acceleration from rollout-horizon control to **adaptive trajectory-level boundary verification** — the reliability boundary need not be predicted, only detected from the observed prefix.
- **`2610.06116`** — *ORCA* (Yuanshi Liu, Boyuan Jiang, Liang Hou, Xin Tao, Pengfei Wan, Zhouchen Lin, Cong Fang; Peking University / Kling Team). Strong **temporary** soft orthogonality regularization early in training, then removed. Lower final validation loss than Muon across LLaMA, Qwen3, and MoE models from 130M–8B.
- **`2610.06050`'s datasets (MovieLens-10M, Amazon Luxury Beauty, KuaiRec)** and **`2610.05432`** OpticalRec (UC San Diego / Alibaba / UIUC / Texas A&M / HKPolyU / CUHK) and **`2610.05670`** are noted for the index only.

---

## Method disclosure, dedup, and cautions

**Harvest**: arXiv API over HTTPS, 5 category queries (`cs.IR`, `cs.AI`, `cs.LG`, `cs.CL`, `cs.CV`) restricted by `submittedDate:[202610050000 TO 202610072359]`, `sortBy=submittedDate desc`, `max_results=200`, with a second page fetched for `cs.LG` when the first page filled → **464 unique entries**, all dated 2026-10-05. Plus 4 topical `abs:` passes (click-through / sequential recommendation / generative recommendation / cold-start) and an earlier 10-04 batch harvest (**344 entries, all unclaimed**) covering the preceding announcement.

⚠️ **Two mechanical failures are recorded because they changed the yield**:
- **The `id_list` sweep over guessed ID ranges returned `HTTP 400 Bad Request` persistently** (18 consecutive failures across chunks). An enumeration-based strategy over the ID ceiling therefore **failed entirely**. The `submittedDate`-ranged category query was used instead, which is *not* exhaustive — it is a category-and-date slice, so **any paper outside cs.IR/AI/LG/CL/CV or with a submission date outside the window was not seen.** Today's yield is a **lower bound**.
- **The temp working directory was garbage-collected mid-run** (`/var/folders/.../T/opencode/arxiv` vanished between two commands), losing the first pool. Re-created and the affected queries re-run; **no selection depended on the lost data**, but the 10-04 pool had to be re-fetched from a later query.

⚠️ **Window framing**: "last 24 hours" is not what arXiv exposes. The API's newest `published` timestamp at run time was 2026-10-05T05:07Z, and **all 464 harvested entries carry submittedDate 2026-10-05**. arXiv does not announce on weekends and the announcement date lags submission by ~24h, so a run on 2026-10-06 sees a window whose newest papers were *submitted* 2026-10-05. This report covers **2026-10-05 announcements (plus the unclaimed 10-04 batch)**, and the two batches are labelled separately. **No 2026-10-06 submissions exist in the API yet.**

⚠️ **Dedup**: baseline built by regex-extracting every `NNNN.NNNNN` pattern from all `wiki/**/*.md` → **7,964 unique arXiv IDs**. 462 of 464 window entries unclaimed. **All 20 featured IDs re-verified 0-hit against that baseline immediately before writing.** ⚠️ **ID-level dedup only, no title-level pass** — and the 2026-10-05 `game-rl-daily` digest explicitly records that **ID-only dedup has already produced duplicate papers twice in three days**. Treat overlap risk as nonzero.

⚠️ **Affiliation discipline**: institutions read **only** from each paper's own LaTeXML author block or an explicit institutional address block, **never inferred from author surnames, email domains, or reputation**. **19 of 20 numbered papers fully resolved; 1 partial** — `2610.05872` (arXiv serves **no HTML** for this ID; recovered from the **PDF title block**, Carnegie Mellon University). **Two entries elsewhere in this report are unresolved and recorded as such** rather than guessed: `2610.06060` (author-posted Version of Record notice, **no affiliation block in the posted version**) and `2610.05550` (**no affiliation markup in the PDF**). `2610.04978`'s author block carries a single shared affiliation (TU Delft) without per-author mapping, so it is recorded as one rather than attributed per author.

⚠️ **Venue discipline**: **4 of 20 carry a venue** — `2610.06590` (**CIKM 2026 short paper**, 5 pages), `2610.06060` (**CIKM '26**, DOI `10.1145/3799682.3840602`), `2610.06703` (**SENTIRE 2026 — an ICDM 2026 *Workshop***, not main track), `2610.05885` (**NeurIPS 2026 *Workshop***, not main track). Only the first two are main-track. `2610.04860`, **NeurIPS 2026 main track**, sits in the 10-04 batch rather than this window. **The remaining 16 numbered papers are unreviewed preprints.** **No result in this report was independently replicated**, and none was replicated by a second group.

⚠️ **Claim-level cautions carried inline**:
- **"DeepSeek-V4-Pro"** (`2610.05744`) could **not be independently verified** — no arXiv listing, no release note, nothing in the fetched metadata. The 64.9pp / 1.10–1.94× figures are the paper's own claim about a model this report cannot confirm exists in that configuration. Treat as **single-source and unverified on its central artifact**.
- `2610.05902` reports **no absolute effect sizes** in the abstract and is argued on MNIST-1D / CIFAR-10 / 3 GLUE tasks — **small-scale, and does not transfer to large-scale CTR leaderboards without evidence**.
- `2610.06269`'s abstract **truncates before naming its four domains or reporting any numbers**.
- `2610.05670` reports **no effect sizes, no dataset names, no metrics**.
- `2610.06590` claims "competitive performance … while using fewer parameters" — an **efficiency claim, not a quality claim**; no quality margin is stated.
- `2610.05550`'s headline "low prediction error misleads planning" is qualified by its own text: **closed-loop planning gains remain unconfirmed**.
- `2610.06192`'s copy weights (**0.06–0.42**) are the paper's own measurement against its own oracle; the fixes' effect sizes (11.2% → 1.1%) come from the authors' own protocol.
- `2610.04931` (Google, billion-scale thumbnail bandit, 10-04 batch) claims "statistically significant improvements" in **no named metric with no numbers** — deliberately excluded from the numbered sections.

⚠️ **Two scope stretches are flagged rather than buried**: `2610.06216` (cross-lingual success-probe calibration for LLM routing — routed-model selection, not CTR) and `2610.05982` (cluster-aware LLM routing) are LLM-routing papers that pattern-match this lane's keywords but are not recommender work; they are **not** included in the numbered sections. `2610.06703`'s book-to-music task is adjacent-to-CTR rather than CTR.

---

## Related wiki pages

- [[ctr-scaling-landscape]] — the CTR scaling thread (GRAB / LoopCTR / EST / CADET) that had **no new entrant** in this window
- [[arxiv-paper-check]] (2026-10-05 edition) — prior run. ⚠️ **Its "last 24 hours" scope claim does not hold:** all eight papers it listed carry original submission dates between 2025-08-05 and 2026-08-25, and only two had been *revised* recently (v4 2026-08-02, v2 2026-09-12). It is therefore a **re-survey of the CTR literature**, not a daily window, and should not be read as a 24-hour digest. Today's report scopes strictly to the announcement window and labels its two batches separately.
- `2610.05872` / `2610.05200` / `2610.04978` — the three-way post-training disagreement, tabulated in §6 above