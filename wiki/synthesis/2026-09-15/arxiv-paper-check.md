---
title: "arXiv Paper Check — AI & CTR (September 15, 2026)"
type: synthesis
created: 2026-09-15
updated: 2026-09-15
sources: [arxiv.org]
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, serving, efficiency, open-models, agents, credit-assignment, evaluation, judges, retrieval, rag, tabular, relational-learning, interpretability, positions, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 15, 2026)

> **Mailing status**: No fresh announcement inside the last 24 h. arXiv's `/new` listings for cs.AI / cs.IR / cs.LG all still show **Monday, 14 September 2026** (IDs ≤ 2609.13134) as of run time (02:20 UTC). The Tue 15 Sep batch posts ~20:00 ET tonight. This check therefore mines the **unclaimed remainder** of the Mon-14 window that the 09-14 siblings ([[arxiv-paper-check]], [[arxiv-daily]], [[arxiv-ai-search]], [[game-rl-daily]], [[tech-report-digest]], [[conference-digest]]) did not feature.
> **Scan scope**: cs.AI (270 parsed), cs.IR (23), cs.LG (260) — 553 total entries; 445 unclaimed vs the 5,419-ID wiki coverage set; **285 entries from the 2609 window**.
> **CTR/ads verdict**: **0 unclaimed ads/CTR/recommendation papers** in the entire 2609 remainder (strong-keyword sweep: click-through, ad auction, ad ranking, creative, recommender, CTR, conversion, exposure bias, sponsored search). The mailing's CTR column was fully drained by the 09-14 runs (PinDCO was the window's only ads/CTR paper; all 12 cs.IR new submissions were already covered).
> **Dedup**: All 9 featured + 6 runner-up IDs grep-verified **0 hits** in `wiki/`, including same-day and 09-14 siblings.

## Summary

Fifteen hours after yesterday's triple arXiv pass, the wiring of the feed means there is **still only one substantive window to read** — so this paper-check adds the papers the 09-14 runs skipped, rather than a new day's haul. The structural signal from the unclaimed tail: **the cost frontier has moved from peak accuracy to delivered-value-per-dollar accounting** — SQD (serving subquadratic-attention LLMs on heterogeneous disaggregated systems, +53% tokens/J), Occamy-1.0 (a 35B open "co-work" model that claims the low-cost knee of the Pareto frontier), and BlueLM-GUI (a real-device flywheel that farms real-phone rollouts into agentic-RL supervision) all price intelligence in *utility per spent dollar/episode*, not benchmark tops. On the CTR side the mailbox is empty again — **zero ads/CTR papers to report for the third consecutive check the feed has made available** — and the most CTR-track-relevant paper is a tabular one (InRTL models PK–FK relational-table joins, the same multi-table structure ad/rec CTR stacks face). Evaluation stays in its empirical-verification groove: a distilled physician-judge that reproduces five published clinical-LLM findings without re-grading, a geometry-agnostic steering benchmark whose headline is "prompting still beats steering," and a matched-control negative result on retrieval-state RAG routing. 9 papers across 5 themes.

---

## ① Serving, Efficiency & Cost Frontiers (2)

### SQD: Rethinking Heterogeneous System Disaggregation for Subquadratic Attention
- **arXiv**: [2609.13134](https://arxiv.org/abs/2609.13134) — cs.AI
- **Authors**: Arya Tschand, Yaosheng Fu, Vikram Sharma Mailthody, Nicolai Oswald, Po-An Tsai, Ritchie Zhao, Oreste Villa, Vijay Janapa Reddi, Karu Sankaralingam
- **Key contribution**: Frontier LLMs are increasingly subquadratic, but existing disaggregated-serving systems still make *dense-attention-centric* decisions. **SQD** splits decode by the **arithmetic intensity and memory footprint of quadratic vs subquadratic attention**, not by operator type: for sparse-attention LLMs it splits top-k selection (must index the full KV) from top-k attention + FFN (static-memory); for linear/sliding-window it splits dense layers from subquadratic layers + FFN. On an adjusted 8×B200 heterogeneous proxy: **+53% tokens/J (GLM 5.2), +31% (Nemotron 3 Ultra), +56% (Gemma 4 31B)** vs GPU-only baselines; in an analytical fixed-power Rubin + LPX model, **1.2–1.5× tighter achievable latency and up to 3.6× higher throughput** over attention-FFN disaggregation. Ends with chip/interconnect provisioning insight for next-gen heterogeneous systems.
- **Relevance**: Directly extends the serving/LatencySLO track this wiki tracks (FlashPrefill-V2 KV compression lineage, DeepSeek-V4.1-Flash 890B/t KV engineering in 09-14 tech-report-digest). For ad/rec serving — whose reshank latencies are budget-bound — subquadratic-attention disaggregation is the systems-side cousin of the CTR-scaling agenda.
- *(tentative: abstract-level; headline claims are author-reported from the adjusted/analytical proxies)*

### Occamy-1.0: Open Pareto-frontier 35B Intelligence for Co-work
- **arXiv**: [2609.11977](https://arxiv.org/abs/2609.11977) — cs.AI
- **Authors**: Wenhui Chen, Shiwen Cheng, …, Jialong Zhu, Zijian Zou (45 authors, multi-institution)
- **Key contribution**: Framing: co-work agents pay cost/latency over the *whole episode* (tool use, coding, file manipulation, state-tracking, recovery), so practical value = peak capability **÷ episode cost**, and many steps don't need frontier-scale reasoning. Occamy-1.0 further trains the **Qwen3.6-35B-A3B** checkpoint on execution-grounded data with replayable long-horizon trajectories across several harnesses, using staged post-training to consolidate complementary execution skills. Claims to sit at the **low-cost knee of the cost–performance Pareto frontier** across four co-work benchmarks, competitive with much larger frontier systems, with broad agentic capability preserved (tool calling, coding, instruction following). Weights + partial training data released.
- **Relevance**: The open-weights efficiency line this wiki has been charting (FrugalGT-PTO-style cheap training, open Pareto spans in 09-14 tech-report-digest: GLM-5.3, Intern-S2-Mobius) — now extended to *agentic "co-work"* and measured on cost-curve placement rather than a single bench. Tailored to the [[byoai]] / build-for-agents thread.

---

## ② Agentic Engineering: The Real-Device Flywheel (1)

### BlueLM-GUI: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents
- **arXiv**: [2609.12394](https://arxiv.org/abs/2609.12394) — cs.AI
- **Authors**: Tong Ye, Kunyang Han, Guozhi Wang, …, Min Chen, Guanjing Xiong, Xiaohu Ruan, Xiaoxin Chen (43 authors)
- **Key contribution**: Industrial mobile GUI agents face three gaps — sandbox/production distribution mismatch, wasted real-device failures, and fixed-benchmark saturation. **BlueLM-GUI** (35B-A3B) closes them with three principles. **Every Sample Matters**: a dual-track pipeline with Heterogeneous Triple-System Consensus evaluation + an Error-Correction & Derivation Module salvages every trajectory into usable supervision. **Every Rollout Is Real**: continual pretraining → SFT → agentic RL on hundreds of real phones, so learned capability transfers to deployment. **Every Query Evolves**: a quota-driven benchmark with three orthogonal attribution axes that is upgraded systematically as the model improves. Achieves **87.4 MobileGUI-VBench** (beats best closed-source by 5.1) and **84.9 AndroidWorld** (best open-source, competitive with closed-source).
- **Relevance**: The "flywheel + growing benchmark" recipe is a concrete execution of the [[concepts/verification-gap]] and agentic-engineering threads — the benchmark becomes part of the training loop and its saturation is engineered away, which is exactly the anti-[[byoai|leaderboard-illusion]] move Karpathy's evals critique asks for. BlueLM also extends the Chinese open-LLM line (BlueLM = vivo-family lineage tracked alongside GLM/Intern in the 09-14 tech-report-digest).

---

## ③ Credit Assignment & Long-Horizon Training (1)

### Large Distant Gradients Need Not Be Reliable: reliability-weighted credit assignment for long-horizon autoregressive forecasting
- **arXiv**: [2609.12890](https://arxiv.org/abs/2609.12890) — cs.LG / cs.AI
- **Authors**: Junhao Zhao, David Michael Simberg, Jacob Kang, Colin Connor Kurniawan, Nan Xu
- **Key contribution**: In autoregressive forecasting, BPTT carries distant-supervision gradients across many steps; repeated Jacobian products let **distant gradients dominate the update while amplifying predictable signal and unpredictable noise together** — a large distant gradient need not be a reliable learning signal. **Internal-DW (Internal Dual-Wiener routing)** is a *backward-only* intervention: full forward rollout and all horizon losses preserved, but internal gradient routes are reliability-weighted with bounded Wiener gains derived from route-level gradient statistics + an explicit noise model. In a controlled SNR system, distant gradients demonstrably grow while their SNR falls; on four history-dominated testbeds Internal-DW cuts forecast error **5.2–13.8% vs full BPTT**, beats gradient clipping and Jacobian regularization on all four, and beats validation-selected truncated BPTT (TBPTT) on three — with a stated applicability boundary when usable history is thin.
- **Relevance**: A principled, cheap alternative to TBPTT for long-horizon targets — including long user-behavior sequences (the CFA/sequence side of CTR) and RL-from-long-rollouts (GACA-style credit assignment was featured in 09-14 arxiv-ai-search). "Trust gradients only where they're reliable" sharpens the wiki's learning-dynamics thread.

---

## ④ Evaluation, Judges & Interpretability (3)

### PrecepTron + GRAND-ROUNDS: Scaling Clinical Judgment to Evaluate Medical AI
- **arXiv**: [2609.12822](https://arxiv.org/abs/2609.12822) — cs.AI
- **Authors**: Thomas A. Buckley, Zahir Kanjee, …, Raja-Elie E. Abdulnour, Adam Rodman, Arjun K. Manrai (17 authors; BIDMC/Stanford-affiliated; medical multi-site)
- **Key contribution**: Blinded physician panels are the gold standard for clinical-reasoning eval but don't scale; small single-institution panels make reproducibility doubtful. **PrecepTron** is a 32B LLM LoRA-finetuned on a small set of physician examples to score open-ended responses at physician level; **GRAND-ROUNDS** releases 9,217 scores by 11 physicians across seven studies. Agent framing: frontier LLMs as judges disagree with physicians *and each other*, but the finetuned judge achieves physician-level consistent scoring — enabling **reproduction of headline findings from five influential clinical-LLM studies (JAMA / Science / Nature Medicine) without new human grading**, plus new infeasible-before questions (e.g., frontier-LLM diagnostic accuracy when cases are revealed token-by-token). Code/data/labels released.
- **Relevance**: The judges-reliability track (09-14's label-free calibrated WMV; this wiki's EVE-Agent verifiers) gets a *distill-the-panel, retire-the-panel* recipe — the evaluator is now a trained artifact with auditable consistency. Direct analog for rec/ads quality evaluation where human rater panels are the costly bottleneck.

### MAxBench: A Multinomial Concept Recovery Benchmark
- **arXiv**: [2609.13072](https://arxiv.org/abs/2609.13072) — cs.LG / cs.AI / cs.CL
- **Authors**: Divya Appapogu, Freya Behrens, Yonatan Belinkov, Aaron Mueller
- **Key contribution**: Steering/interpretability has focused on binary concepts (refusal → one direction); concepts like Animals/Countries are **multinomial** with a far larger geometry search space. **MAxBench** is a geometry-agnostic evaluation framework that *samples from the recovered concept representation* to score steering, then compares **10 localization methods × 5 geometry types × 6 concepts × 4 models**. Findings: (i) **affine subspaces steer more reliably and with greater recall** than rank-one/linear; (ii) the advantage largely comes from better **non-zero offsets**, not the choice of bases; (iii) manifold steering is competitive when applicable; (iv) **no method consistently beats prompting** — extending the binary-concept result that steering still trails prompting.
- **Relevance**: A meta-evaluation design (sample-from-recovery, geometry-agnostic) plus a sobering prompting-vs-steering control result — directly relevant to any attempt to *steer* recommender/user-interest representations, and to the interpretability rigor track.

### Beyond the Query: Do Retrieval Signals Improve Adaptive Multimodal RAG Routing?
- **arXiv**: [2609.12437](https://arxiv.org/abs/2609.12437) — cs.LG / cs.AI
- **Authors**: Qiaomu Li, Qiuyuan Zhang, Nong Ming
- **Key contribution**: Adaptive RAG routers conventionally use retrieval-time signals to decide whether to run another retrieval/rerank/multimodal step. This paper asks the matched-control question: **do those signals add routing value once the query itself is known?** Across document/audio/video RAG, with actions, router family, training, and eval held fixed and ONLY the signal set varied, query+retrieval routers give **no reliable held-out improvement over a query-only baseline**; some signals predict whether a later step will help, but that predictability does not convert into better RUN/SKIP decisions. The lesson is methodological: **retrieval-state features must beat a matched query-only control to be credited**.
- **Relevance**: Clean negative-result methodology — one more instance of the empirical-verification wave (09-14's two-gap SWE framework and harness-vs-model study). For the wiki's IR/RAG track: don't report "retrieval signal helps routing" without the query-only control.

---

## ⑤ Position & CTR-Track Cousins (2)

### Language Is an Insufficient Substrate for Quantitative Reasoning, and Consequential Domains Need Large Quantitative Models (LQM)
- **arXiv**: [2609.12105](https://arxiv.org/abs/2609.12105) — cs.AI / cs.LG
- **Authors**: Reuben Vandeventer, David Imrem, David J. Wild
- **Key contribution**: Position/claim: LLMs train on a *description* of the world, and description is a **lossy, irreversible encoding** of the quantitative record — no downstream model at any scale can recover what the description didn't encode. This is a property of the *representation*, not model capacity. Three properties consequential quantitative domains demand and a language substrate cannot supply **by construction**: reproducibility, **lineage** from every output back to source records, and **calibrated uncertainty**. Together these define a distinct model class: the **Large Quantitative Model (LQM)**.
- **Relevance**: A claim-level position (tentative — preprint, single-source) that speaks directly to the wiki's tabular/CTR thesis: pricing, risk, and ad-placement scoring are LQM-flavored, which is consistent with FAT/EST/SUAN/LlattE CTR-scaling results being built on numeric-native rather than language-native representations. Candidate for a tracked claim.

### InRTL: Intra-Inter Interaction Learning for Relational Tables
- **arXiv**: [2609.12712](https://arxiv.org/abs/2609.12712) — cs.LG / cs.AI
- **Authors**: Weichen Li, Ken Zhong, Zheng Wang, Li Pan, Jianhua Li
- **Key contribution**: Relational-table learning (models over multiple tables connected via primary-key/foreign-key joins) is under-explored as a unified modeling framework. **InRTL** formalizes two complementary interaction patterns — **intra-table** (associations among rows within a table) and **inter-table** (dependencies across PK–FK-linked tables) — implemented with a column-aware table encoder, Transformer self-attention (intra) and cross-attention (inter), scaled via **linearized attention + heterogeneous GNNs** for the expensive attention steps. Validated on **10 datasets / 24 real-world tasks**.
- **Relevance**: The CTR-track cousin this mailing actually offers: ad/rec CTR stacks *are* relational-table learning — user/item/ad tables joined on PK–FK — so the intra/inter decomposition is the same one unified feature-interaction models (Haﬁfor/OneTrans/Hiformer) apply within one table, generalized to multi-table joins. Growing tabular-FM attention (09-14: Attention Q) makes this timely.
- *(tentative: abstract-level; per-task numeric gains not enumerated in the abstract)*

---

## Cross-Cutting Themes

1. **Third consecutive check with zero ads/CTR to report**: after yesterday's triple pass drained the window (PinDCO = only CTR paper), this paper-check finds the 2609 remainder is CTR-empty and all 12 cs.IR new submissions are already claimed. The next chance for stock CTR content is tonight's Tue-15 batch. (high confidence — keyword sweep over all 285 unclaimed 2609 entries, 0 hits)
2. **The cost frontier redefines "state of the art"**: SQD counts tokens/J, Occamy-1.0 places itself on a cost–performance Pareto knee, BlueLM-GUI maximizes episode-level utility from real hardware. Peak-accuracy accounting is being displaced by *utility-per-dollar* accounting — the same lens as the wiki's CTR-scaling and Karpathy's compute-cost framing.
3. **Evaluation is now itself a training artifact**: PrecepTron (distill a physician panel into a judge), MAxBench (recovery-by-sampling meta-eval with a prompting control), and Beyond-the-Query (matched controls to stop over-crediting signals) all make "does the model actually work" a measurable, auditable engineering discipline rather than an assertion.
4. **Position papers as signal**: LQM (representation, not capacity, is the limit) joins 09-14's PAMR and delegation-spectrum positions as third-position-paper-in-two-days — the field is producing more *framing* than new mechanisms, worth tracking in the claims ledger.

## Runner-Ups (verified 0 hits)

- **[*Confidence-Gated Transductive Test Generation for Code Reranking (CoTT)*](https://arxiv.org/abs/2609.12489)** (2609.12489, cs.AI/CL/SE) — run transductive test generation only when an inductive pass is low-confidence; better efficiency-effectiveness trade-off for LLM code reranking on a single model. Directly relevant to test-time-compute allocation in ranking pipelines.
- **[*Diffusion Models and Concept Formation*](https://arxiv.org/abs/2609.13047)** (2609.13047, cs.AI/LG) — diffusion score fields as implicit Cobweb-style concept hierarchies; an elegant theory paper with MNIST/Fashion-MNIST evidence for a *basic level* at an intermediate noise step.
- **[*Tracing and Coordinating Cross-Layer Influence for Multimodal Model Merging (TAC-Merge)*](https://arxiv.org/abs/2609.12897)** (2609.12897, cs.AI) — Ricci-curvature graph of update effects + coupled merge control to consolidate multimodal task experts that interact across layers.
- **[*MedRoundsQA: Persona and Difficulty Aware Multi-Turn Medical Consultations*](https://arxiv.org/abs/2609.12851)** (2609.12851, cs.AI) — 1,387 board cases → 24-slot clinical records → dual-agent dialogues; single-turn→multi-turn drops diagnosis 13–39 pts, persona moves accuracy 7–8 pts — multi-turn is the honest eval.
- **[*A Hybrid LSTM-XGBoost Framework for Multi-Horizon Stock Return Prediction*](https://arxiv.org/abs/2609.13125)** (2609.13125, cs.AI) — two-stage LSTM-embedding + XGBoost; 97.6% long-horizon directional accuracy honestly shown to mostly track the positive base rate (the short-horizon gap is the signal) — a nice methodological honesty note for the investment queue.
- **[*GLARE: Generative Learning via Adversarial Reward Estimation for Social Dynamics Forecasting*](https://arxiv.org/abs/2609.12165)** (2609.12165, cs.AI) — adversarial imitation learning applied to conditional dialogue generation + Meeting Dynamic Forecasting Benchmark (2,207 meetings / 24,794 queries); avg human win-rates 0.66 (utility) / 0.70 (human-likeness).

## Method Note

Queries: `arxiv.org/list/{cs.AI,cs.IR,cs.LG}/new` (arXiv API still returns HTTP 429, as in 09-14). All three pages show **"Showing new listings for Monday, 14 September 2026"** — no Tuesday announcement published at run time (10:20 CST, 02:20 UTC; Tue-15 batch posts ~20:00 ET). Parsed 553 entries (cs.AI 270, cs.IR 23, cs.LG 260); built a 5,419-ID coverage set by extracting every arXiv ID from `wiki/`; **445 of 553 unclaimed, 285 from the 2609 window**. Strong-keyword ads/CTR/rec sweep of all 285 → 0 hits. Featured/runner-up selection further deduped against same-day-absent and 09-14 sibling coverage by explicit ID check (`rg '<id>' wiki/` = 0 hits). All claims summarized from arXiv abstracts; figures author-reported. This pass intentionally covers only the *unclaimed remainder*, orthogonal to the 09-14 arxiv-paper-check/daily/ai-search.