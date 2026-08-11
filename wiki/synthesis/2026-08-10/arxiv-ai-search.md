---
title: arXiv AI Research Search — August 10, 2026
type: synthesis
created: 2026-08-10
updated: 2026-08-10
sources: [arxiv-listing, arxiv-abstract-pages]
tags: [arxiv, ai, llm, kv-cache, quantization, calibration, distillation, agents, coding, advertising, attention-markets, online-learning, game-theory, autoregressive, oversight, daily-digest]
---

# arXiv AI Research Search — 2026-08-10

> Search window: **Mon, Aug 10, 2026** arXiv announcement batch (new submissions submitted Aug 7–9, IDs ~2608.06394–2608.07460). arXiv announces Mon–Fri; this is the first fresh batch since Fri Aug 7. Streams scanned: cs.LG (144 new), cs.CL (76 new), cs.GT (10 new), cs.SE (25 new), cs.MA (11 new), cs.IR (16 new — fully covered by the same-day [arXiv Paper Check](./arxiv-paper-check.md)). Metadata verified against individual abstract pages.
>
> 12 papers curated, **all NEW** (grep-verified 0 hits on arXiv ID across wiki/index.md, wiki/log.md, and wiki/synthesis/**). **Zero overlap** with the same-day [arXiv Paper Check](../2026-08-10/arxiv-paper-check.md) (36 papers, cs.AI+cs.IR), [Game RL Daily](../2026-08-10/game-rl-daily.md) (13 papers), [Conference Digest](../2026-08-10/conference-digest.md) (8 big-company arXiv picks), or any prior digest/scan. Papers already covered today (Skaling 2608.07222, Autonomy-of-Heads 2608.06849, CoinRAG 2608.07458, CreativeInstruct 2608.07460 in the conference digest; TRIAL 2608.07371 in game-rl-daily) are excluded and cross-referenced below.

## Overview table

| # | Paper | Domain | Institution / Company | arXiv | Status |
|---|-------|--------|----------------------|-------|--------|
| 1 | GraceKV: Global Allocation of Resolution and Coverage for KV Cache Compression | LLM efficiency / KV cache | (not stated) | 2608.07001 | **new** |
| 2 | CubicQuant: Parametric Non-Uniform Codebooks for 1–8-Bit LLM Weights | LLM efficiency / quantization | (not stated) | 2608.06763 | **new** |
| 3 | Is SwiGLU's Open Positive Tail Necessary? MemGLU | LLM architecture / FFN gating | (not stated) | 2608.07323 | **new** |
| 4 | Beyond Post-Hoc Temperature Scaling: Bilevel Optimization for LLM Calibration | LLM calibration | (not stated; COLM 2026) | 2608.07419 | **new** |
| 5 | Simple-OPD: Demystifying Warm-up for On-policy Distillation | LLM post-training | Tsinghua (tentative) | 2608.06802 | **new** |
| 6 | LivePlan: Online Monitoring and Corrective Steering of Programming Agents | Coding agents | IBM Research / UIUC (high confidence for IBM) | 2608.06701 | **new** |
| 7 | From Test-Time Scaling to Reusable Memory: Measuring Crystallization in Text-to-SQL | Reasoning / reusable memory | Xidian University / Shanghai Jiao Tong University | 2608.07213 | **new** |
| 8 | Sharding Prevents LLM Oversight Failures and Adversarial Exploitation | Oversight / safety | CMU / Apple (high confidence) | 2608.06422 | **new** |
| 9 | Auctioning Attention on Social Networks | Advertising / attention markets | University of Illinois Urbana-Champaign (high confidence) | 2608.06665 | **new** |
| 10 | Progressive Content Refinement with Decaying Reward Joint LinUCB | Online learning / content refinement | IBM Research (tentative) | 2608.06750 | **new** |
| 11 | Ex-Post Equilibria: Structure and Computation | Game theory / mechanism design | Columbia / CNRS (high confidence for Kroer) | 2608.07025 | **new** |
| 12 | Stochastic Autoregressive Learning | LLM learning theory | MIT (high confidence) | 2608.07224 | **new** |

---

## 1. LLM Efficiency & Inference

### 1.1 GraceKV: Every Cache Entry Earns Its Place — Global Allocation of Resolution and Coverage for KV Cache Compression

- **arXiv**: [2608.07001](https://arxiv.org/abs/2608.07001) (cs.LG; submitted 2026-08-07) — **NEW**
- **Authors**: Haolin Tian, Yuzhe Liu, Tonghan Wang
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: As LLMs process increasingly long contexts, KV cache storage and repeated access have become a major bottleneck. Existing KV cache compression methods rely on predefined, fixed compression rules and are typically developed around either token eviction or merging, so cache resources can neither flow freely across layers, heads, and context slots, nor be jointly allocated to balance **local resolution** against **information coverage**. GraceKV reformulates compression as a **global resource-allocation problem under a fixed cache budget**: each layer–KV head–slot combination is an atomic unit built into a prototype tree, where leaf nodes are token-level KV entries and internal nodes use a single prototype to compress the KV space covered by their children. A set of non-overlapping tree nodes forms an atomic unit's representation; adding a tree's root expands information coverage, while splitting a selected node improves local resolution. All candidate actions compete globally for a shared cache budget, and the retained nodes form the compressed cache — adaptively deciding both cross-unit allocation and the resolution-vs-coverage balance. GraceKV needs **no additional training** and runs the whole compression+inference on GPU. Across diverse long-context tasks and compression ratios it ranks first in **24 of 32 settings** and stays robust up to **128× compression**.
- **Key innovations**: (1) Global, budgeted allocation across layers/heads/slots instead of fixed per-layer rules; (2) an explicit resolution-vs-coverage trade-off under a single shared budget; (3) training-free, fully GPU-resident compression with 128× robustness.

### 1.2 CubicQuant: Parametric Non-Uniform Codebooks for High-Throughput LLM Inference with 1–8-Bit Weights

- **arXiv**: [2608.06763](https://arxiv.org/abs/2608.06763) (cs.LG / cs.DC; submitted 2026-08-07) — **NEW**
- **Authors**: Xuetian Gao
- **Institution**: Not stated on abstract page (technical report).
- **Abstract (faithful summary)**: Weight quantization for LLM inference must balance adaptive reconstruction levels with representations regular enough for efficient GPU execution. Uniform integers constrain each group to a linear grid; low-bit floats use a fixed exponent–mantissa structure; learned codebooks gain flexibility at the cost of irregular decoding and extra metadata. **CubicQuant** is a parametric non-uniform scalar format that keeps a dense integer code stream while adapting reconstruction levels within each weight group: a monotonic cubic curve, specified by two shape parameters and one scale, maps uniformly spaced magnitude codes to non-uniform levels. The family spans **1–8-bit weight payloads**, contains symmetric uniform integer quantization as an exact special case, and has effective width B + 64/G bits per weight (payload width B, group size G). The paper derives population distortion under Uniform/Gaussian/Laplace distributions, formulates continuous and Dynamic-A8-carrier-aware fitting objectives, and describes direct packed-weight GPU execution. For G=128 with 15,360 samples per distribution, W4 CubicQuant cuts reconstruction RMSE vs optimally-clipped 4-bit uniform integers by 3.90% (Uniform), 13.49% (Gaussian), 28.14% (Laplace); vs the best enumerated 4-bit finite float format by 3.90%/9.44%/6.27%. Preliminary H200 kernels show a workload-dependent crossover between model-dtype and Dynamic-A8 execution.
- **Key innovations**: (1) A parametric (3-parameter) non-uniform scalar format that stays a dense integer code stream — regular enough for direct GPU execution; (2) exact recovery of uniform integer quantization as a special case; (3) closed-form distortion analysis and carrier-aware fitting objectives.

---

## 2. LLM Architectures & Calibration

### 2.1 Is SwiGLU's Open Positive Tail Necessary? Evidence from Closed-Tail Gating with MemGLU

- **arXiv**: [2608.07323](https://arxiv.org/abs/2608.07323) (cs.LG; submitted 2026-08-07) — **NEW**
- **Authors**: Yuting Ge, Pengju Yang, Mingkai Nie
- **Institution**: Not stated on abstract page.
- **Abstract (faithful summary)**: Tests whether decoder-only language-model FFNs actually require SwiGLU's open positive tail. The authors introduce **MemGLU** as a closed-tail comparator derived from a memristive branch geometry. Across paired 9M and 30M pretraining runs with three seeds each, MemGLU stays within about **0.1% of SwiGLU in validation NLL**. Trained SwiGLU checkpoints are sensitive to positive-tail suppression, while mechanism diagnostics show the two models use their gates differently despite similar losses. Conclusion: models adapt to the gate geometry available during pretraining, and **at the tested scales SwiGLU's open positive tail is not necessary** for decoder-only FFNs.
- **Key innovations**: (1) A closed-tail gating comparator (memristive-geometry-inspired) that matches SwiGLU NLL within ~0.1%; (2) mechanistic evidence that models adapt gate use to the geometry they are trained with; (3) a direct challenge to a standard architectural assumption, with implications for hardware-friendly (memristive) FFN designs.

### 2.2 Beyond Post-Hoc Temperature Scaling: Bilevel Optimization for LLM Calibration

- **arXiv**: [2608.07419](https://arxiv.org/abs/2608.07419) (cs.LG; COLM 2026; submitted 2026-08-07) — **NEW**
- **Authors**: Ruochen Jin, Zhanliang Wang, Zongyu Dai, Jiancong Xiao, Bojian Hou
- **Institution**: Not stated on abstract page (COLM 2026).
- **Abstract (faithful summary)**: Preference alignment often makes LLMs overconfident and poorly calibrated. Traditional post-hoc temperature scaling is inherently domain-dependent — a temperature fitted on one domain does not generalize across domains — motivating modifying model parameters during training. The paper proposes **maximizing the entropy of predictive distributions** as the calibration objective, directly targeting overconfidence by discouraging overly concentrated predictions. Realized via a **bilevel optimization** formulation: the lower level trains the model under a parametric loss, the upper level selects loss hyperparameters to maximize entropy. An efficient first-order approximation avoids explicit second-order computation at LLM scale. Across multiple-choice and open-ended generative QA, the method yields well-calibrated LLMs with particular advantages in **out-of-domain generalization**.
- **Key innovations**: (1) Entropy-as-objective calibration during training rather than post-hoc scaling; (2) bilevel loss-hyperparameter selection (temperature-inspired) with a first-order approximation that scales to LLMs; (3) OOD-calibration advantages over fitted temperature scaling.

### 2.3 Simple-OPD: Demystifying Warm-up for On-policy Distillation

- **arXiv**: [2608.06802](https://arxiv.org/abs/2608.06802) (cs.CL; submitted 2026-08-07) — **NEW**
- **Authors**: Tao Liu, Taiqiang Wu, Mao Zheng, Xuan Luo, Runming Yang, Xuewei Yang, Junjie Wang, Yujiu Yang
- **Institution**: Not stated on abstract page. Co-author Yujiu Yang is affiliated with Tsinghua Shenzhen International Graduate School (tentative; single-source).
- **Abstract (faithful summary)**: On-policy distillation (OPD) trains a student on its own rollouts with token-level teacher supervision, but its effectiveness can depend strongly on the warm-up stage. The paper demystifies warm-up from both data and training perspectives. **Data**: effective warm-up relies on teacher-compatible chain-of-thought (CoT) supervision — and even **incorrect teacher rollouts** provide comparable benefit to correct ones — suggesting warm-up primarily transfers a *teacher-compatible thinking pattern* rather than correct answers. **Training**: LoRA with near-saturation training duration balances in-domain adaptation and out-of-distribution generalization better than full-parameter SFT. Based on these findings, **Simple-OPD** is a plug-and-play initialization that warms up the student on teacher-generated CoT with LoRA before OPD. Experiments across diverse settings demonstrate effectiveness and robustness.
- **Key innovations**: (1) A mechanistic account of what warm-up actually transfers (thinking pattern, not answers); (2) surprising evidence that incorrect teacher rollouts are as useful as correct ones; (3) a simple LoRA-based warm-up recipe that improves OPD robustness.

---

## 3. Agents & Coding

### 3.1 LivePlan: Online Monitoring and Corrective Steering of Programming Agents

- **arXiv**: [2608.06701](https://arxiv.org/abs/2608.06701) (cs.SE / cs.AI / cs.CL / cs.LG; submitted 2026-08-07) — **NEW**
- **Authors**: Shuyang Liu, Saman Dehghan, Ji Young Kim, Jatin Ganhotra, Martin Hirzel, Reyhaneh Jabbarvand
- **Institution**: IBM Research (Ganhotra, Hirzel — high confidence, well-known affiliations) / University of Illinois Urbana-Champaign (Jabbarvand).
- **Abstract (faithful summary)**: Fixing GitHub issues in large-scale projects is long-horizon, especially when a fix requires multi-location changes or the issue description lacks localization/repair information. Agents traverse long trajectories prone to inefficiency and drift: they stray from the plan, repeat failed actions, or terminate without a working patch. **LivePlan** monitors, detects, and corrects such behavioral inefficiencies in real time by **decoupling judging from advising**: a deterministic, rule-based monitor examines general trajectory signals to detect issues *without invoking an LLM*, and only when an issue is detected does it consult an advisor LLM for a high-level next-step correction. This avoids the misleading re-planning and costly interventions of prior approaches. Built on SWE-agent and evaluated with five LLMs (three executors, two advisors) across SWE-bench Verified and SWE-bench Pro: LivePlan improves resolution rates by up to **15.2% (average 9.9%)** over vanilla SWE-agent at only **+$0.08 per instance**, with gains concentrated on medium/hard instances and new successes on problems no baseline solves.
- **Key innovations**: (1) Deterministic rule-based monitoring gating LLM advising (cheap, non-interventionist); (2) corrective steering instead of full re-planning; (3) consistent resolution gains (+9.9% avg) at negligible cost.

---

## 4. Reasoning, Reusable Memory & Oversight

### 4.1 From Test-Time Scaling to Reusable Memory: Measuring Crystallization in Text-to-SQL

- **arXiv**: [2608.07213](https://arxiv.org/abs/2608.07213) (cs.CL; submitted 2026-08-07) — **NEW**
- **Authors**: Jiaqian Wang, Yutao Qi, Wenjin Hou, Yuanxi Che (Xidian University); Muning Wen (Shanghai Jiao Tong University)
- **Institution**: Xidian University / Shanghai Jiao Tong University (stated in abstract page).
- **Abstract (faithful summary)**: Test-time scaling can correct difficult text-to-SQL queries, but the extra computation is normally discarded after each answer. Systems increasingly retain verified repair episodes, yet evaluations still report a single end-to-end score that cannot distinguish replay on recurring questions from help on unseen questions, or identify the responsible memory choice. The paper calls measuring this future value the **crystallization problem** and designs a controlled evaluation that holds the single-shot solver fixed while varying one memory choice at a time, separately measuring **replay, cross-question retention, and held-out same-database transfer**. On BIRD, storing verified corrected queries improves held-out first-attempt accuracy by **4.34 pp**, capturing **44.4% of the accuracy headroom** provided by on-demand repair on the same questions. Controlled interventions identify **database-specific content** as the main operating ingredient; reliable verification and broader retrieval coverage yield supported gains, while richer formats and elaborate retrievers do not.
- **Key innovations**: (1) A controlled evaluation protocol (crystallization) separating replay, retention, and transfer effects of test-time memory; (2) evidence that verified-query memory meaningfully transfers to held-out first attempts; (3) ablation isolating content vs format/retriever design choices.

### 4.2 Sharding Prevents LLM Oversight Failures and Adversarial Exploitation

- **arXiv**: [2608.06422](https://arxiv.org/abs/2608.06422) (cs.LG; submitted 2026-08-05) — **NEW**
- **Authors**: Victor Akinwande, J. Zico Kolter, Aran Nayebi
- **Institution**: Carnegie Mellon University (Kolter; high confidence) / Apple (Nayebi; high confidence).
- **Abstract (faithful summary)**: Giving an LLM judge more compute does not necessarily make it check more requirements: when one call must return many verdicts, some decisions become weakly grounded in evidence, even with the same token/tool budget as a panel of separate calls. Across expert-graded research replications, legal work, and clinical-trial assessments, **agreement with experts falls as the number of verdicts per call grows**. **Sharding** — partitioning requirements into smaller groups, assigning each to a separate call, and aggregating verdicts — mitigates this model-based-oversight failure. Against a single call with the panel's full budget, sharding improves agreement while holding model, evidence, total budget, and per-decision budget fixed; a **sharded weaker judge can outperform a more capable holistic judge** and match it even when the latter receives the full panel budget. Sharding is also robust to adversaries: a best-of-N adversary can hold work fixed, vary only presentation, and multiply an overloaded judge's acceptance of genuinely unmet criteria; wherever sharding reduces baseline error it removes this adversarial advantage. For attacks that persuade the judge per-criterion rather than exploiting overload, debate-style opposition on top of sharding withstands adaptive re-optimization.
- **Key innovations**: (1) Documents overload-induced oversight degradation as verdicts-per-call grows; (2) sharding as a free-ish budget-preserving intervention that can make weaker judges beat holistic judges; (3) adversarial robustness analysis (presentation-based exploitation) plus debate-style opposition for the residual attack class.

---

## 5. Advertising & Attention Markets

### 5.1 Auctioning Attention on Social Networks

- **arXiv**: [2608.06665](https://arxiv.org/abs/2608.06665) (cs.GT; submitted 2026-08-07) — **NEW**
- **Authors**: Andy Lee, Hari Sundaram
- **Institution**: University of Illinois Urbana-Champaign (high confidence — well-known affiliation of Hari Sundaram).
- **Abstract (faithful summary)**: Social media recommendation systems create conflict among content producers, consumers, platform operators, and social pressures — producers optimize for algorithms, consumers face negative-externality content (polarization, misinformation), platforms maximize engagement at the cost of over-consumption. Instead of constructing feeds purely by recommendation, the paper proposes a (to their knowledge) novel **auction-based feed construction where users bid for the attention of other users**, systematically accounting for producers, consumers, platform operators, and social welfare. The mechanism is **weakly incentive compatible under budget constraints**, and a **tax policy** increases the cost of content with negative externalities to balance producer and consumer welfare. Simulations over common social network topologies and an empirically observed network show different feed algorithms prioritize different stakeholders: the auction produces **36.3% higher producer welfare** than comparison algorithms on the empirical network and **31.4% higher** on synthetic networks, plus more equitable attention distributions across all network types.
- **Key innovations**: (1) Feed construction as an attention auction rather than a recommendation problem; (2) budget-constrained weak incentive compatibility plus an externality tax; (3) explicit multi-stakeholder welfare (producers/consumers/platform/society) with equity gains across network topologies.

---

## 6. Online Learning & Content Refinement

### 6.1 Progressive Content Refinement with Decaying Reward Joint LinUCB

- **arXiv**: [2608.06750](https://arxiv.org/abs/2608.06750) (cs.CL / cs.AI; submitted 2026-08-07) — **NEW**
- **Authors**: Shion Ishikawa, Pablo Loyola, Young-joo Chung, Yun Ching Liu
- **Institution**: Not stated on abstract page. Co-author Pablo Loyola is affiliated with IBM Research (tentative; single-source).
- **Abstract (faithful summary)**: Iterative refinement significantly improves LLM performance, but existing methods from feedback-based Self-Refine to traditional bandits often rely on static options or overlook the **saturation effect**, leading to over-exploitation where reusing identical prompts/arms yields diminishing rewards. The paper proposes a contextual bandit algorithm that **explicitly incorporates reward decay modeling**: an EM algorithm jointly estimates arm-specific and decay parameters, and by embedding prompts as arms, the approach supports **joint learning of arm values** — distinguishing it from disjoint LinUCB. On Sentiment Reversal and GSM8K benchmarks the method beats strong baselines, and an ablation confirms reward-decay modeling is crucial for mitigating over-exploitation and optimizing iterative refinement.
- **Key innovations**: (1) Explicit reward-decay (saturation) modeling in a contextual bandit for iterative LLM refinement; (2) EM-based joint estimation of arm and decay parameters; (3) joint (vs disjoint) LinUCB formulation with prompts as arms.

---

## 7. Games, Mechanism Design & Game Theory

### 7.1 Ex-Post Equilibria: Structure and Computation

- **arXiv**: [2608.07025](https://arxiv.org/abs/2608.07025) (cs.GT; submitted 2026-08-07) — **NEW**
- **Authors**: Francesco Giordano, Julien Grand-Clément, Christian Kroer
- **Institution**: Columbia University (Kroer; high confidence) / CNRS & HEC Paris (Grand-Clément; high confidence).
- **Abstract (faithful summary)**: Studies **ex-post equilibria (EPEs)** in simultaneous-move games with parameter uncertainty. Compares EPEs with existing robust-equilibrium notions and provides a foundation for EPEs as a solution concept, showing EPEs are **fully characterized by two game-theoretic properties: monotonicity and set-consistency**. Since EPEs may fail to exist, the paper introduces **optimal approximate EPEs**, where players use approximate best responses while minimizing suboptimality. It studies computation of EPEs and optimal approximate EPEs for two important classes — **zero-sum games and concave potential games** — giving several hardness results plus a general family of computational approaches based on auxiliary minimax formulations.
- **Key innovations**: (1) A clean axiomatic characterization (monotonicity + set-consistency) of ex-post equilibria under parameter uncertainty; (2) optimal approximate EPEs for non-existence cases; (3) complexity results and minimax-based algorithms for zero-sum and concave-potential games.

---

## 8. LLM Learning Theory

### 8.1 Stochastic Autoregressive Learning

- **arXiv**: [2608.07224](https://arxiv.org/abs/2608.07224) (cs.LG; submitted 2026-08-07) — **NEW**
- **Authors**: Ilan Doron-Arad, Idan Mehalel, Elchanan Mossel
- **Institution**: MIT (high confidence — well-known affiliation of Elchanan Mossel).
- **Abstract (faithful summary)**: Motivated by LLMs that generate outputs by iteratively sampling from next-token distributions, introduces a PAC-learning model for **binary stochastic autoregressive learning**, generalizing the deterministic autoregressive framework of Joshi et al. (COLT 2025). One fixed generator assigns a Bernoulli next-token distribution to every prompt string; sampling appends tokens for M steps. Three supervision forms are considered: **base one-step samples**, **chain-of-thought (CoT)** samples revealing full length-M random trajectories, and **end-to-end (e2e)** samples revealing only the final token. The paper studies the sample complexity m_base(ε), m_CoT(ε), m_e2e(ε) under squared loss. Key finding: stochastic autoregressive learning **fundamentally differs from the deterministic theory** — at scale ε there is no universal comparison among the three tasks (both m_CoT/m_base and m_e2e/m_CoT can be made arbitrarily larger than M/ε). Nevertheless, CoT learning at scale ε is upper-bounded by base learning at scale ε/M², and e2e learning by (M/ε)·m_CoT(Θ(ε)) up to log factors; these dependencies are essentially tight. Complements with dimension-d logistic-function analysis.
- **Key innovations**: (1) First PAC sample-complexity framework for stochastic (next-token) autoregressive generation; (2) surprising non-comparability of base/CoT/e2e supervision at matched scale; (3) essentially tight reductions connecting the three supervision regimes.

---

## Cross-cutting trends

- **KV cache and quantization economics mature into *global optimization* problems** — GraceKV frames compression as budgeted resource allocation across layers/heads/slots (resolution vs coverage), while CubicQuant's parametric non-uniform codebooks keep dense integer streams for direct GPU execution; both push inference efficiency beyond per-layer fixed rules, parallel to the digest's DBLAST/DBLAST-adjacent inference-speedup thread. (Related: CoinRAG nugget-level KV reuse was covered in the same-day conference digest.)
- **Supervision keeps decoupling from labels and from the model's own answers** — Simple-OPD shows warm-up transfers a teacher-compatible thinking pattern (even from incorrect teacher rollouts); the bilevel calibration paper replaces post-hoc temperature with entropy-maximizing loss hyperparameters; both extend the OPSD/distillation cluster from Aug 7–10 (U-OPSD, OPD², MemOPD).
- **Oversight is being engineered as a *process* problem, not a capability problem** — Sharding shows verdict-count overload degrades LLM judges and that budget-neutral sharding lets weaker judges beat stronger holistic ones (and survives presentation-based adversaries); LivePlan decouples deterministic monitoring from LLM advising for coding agents. This parallels the paper-check's Niyam-AI / StepJack and the Aug 8 auditability theme.
- **Advertising economics reaches for institutional design** — Auctioning Attention treats feed construction as a multi-stakeholder auction with budget-constrained incentive compatibility and an externality tax, matching the conference-digest's game-theory×FM thread (Google's embedded-Bayesian-agent work) and the fair-division/governance cluster from Aug 7–8.
- **Test-time compute is being *reinvested* rather than discarded** — Crystallization (Text-to-SQL) quantifies how verified repair episodes transfer to held-out first attempts (44.4% of repair headroom), connecting test-time scaling to memory; the decaying-reward LinUCB treats iterative LLM refinement as a bandit with saturation — the same "spend once, reuse, don't over-exploit" theme.
- **Autoregressive learning gets a stochastic theory** — the first PAC sample-complexity analysis of next-token autoregressive generation shows base/CoT/e2e supervision are not universally comparable — a grounding result for the post-training-supervision debates running through this week's digests.

## Methodology & caveats

- Papers selected from the Mon Aug 10, 2026 arXiv announcement batch across the requested domains (AI, LLM, agents, coding, recommendation-adjacent online learning, advertising/attention markets, games, mechanism design). Not exhaustive — the batch spans cs.LG 144 / cs.CL 76 / cs.GT 10 / cs.SE 25 / cs.MA 11 / cs.IR 16 new; cs.AI (88) and cs.IR (16) were fully curated by the same-day [arXiv Paper Check](../2026-08-10/arxiv-paper-check.md) and are not re-covered here. Ranked by novelty, industrial signal, and domain coverage. All 12 are **new** to the wiki (grep-verified, 0 hits).
- **Zero-overlap verification**: every candidate arXiv ID grep-checked across wiki/index.md, wiki/log.md, and wiki/synthesis/** before inclusion. Papers covered by same-day outputs (Skaling 2608.07222, Autonomy-of-Heads 2608.06849, CoinRAG 2608.07458, CreativeInstruct 2608.07460 — conference digest; TRIAL 2608.07371 — game-rl-daily; Tower of Hanoi world models 2608.07077, ADIAS 2608.06410, SkillProx 2608.07449, IB-RL 2608.06735, ResidencyRL 2608.07418 — arxiv-paper-check) were excluded to preserve the report's "uncovered papers" role.
- Institution/company attribution: **high confidence** where stated in the abstract (author affiliation line) or a well-known affiliation; **tentative** marks where only inferred from a single co-author's known affiliation. No affiliation should be treated as authoritative without checking the paper.
- arXiv export/listing APIs were used for discovery; all selected-paper metadata (authors, submit dates, abstracts) verified against individual abstract pages. Submission-date caveat: arXiv lists 2608.06422 (Sharding) as submitted Aug 5; it sits in the Mon Aug 10 listing (IDs are not strictly ordered by submission time), and it is new to the wiki.

## Related pages
- [arXiv Paper Check — AI & CTR (August 10, 2026)](./arxiv-paper-check.md) — same-day CTR/Rec/Ads curation from cs.AI + cs.IR (36 papers)
- [Game RL & Game AI Bot — Daily Synthesis (August 10, 2026)](./game-rl-daily.md) — same-day game RL/world-model curation (13 papers)
- [Conference Digest (August 10, 2026)](./conference-digest.md) — KDD 2026 in progress + big-company arXiv picks (incl. Skaling, Autonomy-of-Heads, CoinRAG)
- [arXiv AI Research Search (August 8, 2026)](../2026-08-08/arxiv-ai-search.md) — prior AI scan (Fri Aug 7 batch)
