---
title: "arXiv Paper Check — AI & CTR (September 13, 2026)"
type: synthesis
created: 2026-09-13
updated: 2026-09-13
sources: [arxiv.org]
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, ir, llm, judges, evaluation, routing, serving, agents, multi-agent, model-collapse, unlearning, data-catalog, finance, personalization, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 13, 2026)

> **Mailing**: No new announcement since **Fri, 11 Sep 2026** (arXiv does not announce on Sat/Sun). This is a *third* dedup-verified pass over the Sep 11 window + catch-up over Thu 10 Sep window.
> **Scan scope**: cs.AI (171 new), cs.IR (15 new), cs.LG (171 new) in the Fri Sep 11 mailing.
> **Dedup**: Zero overlap with 09-11/09-12 siblings ([[arxiv-paper-check]] (09-11), [[arxiv-daily]] (09-11), [[arxiv-paper-check]] (09-12), [[arxiv-daily]] (09-12), [[arxiv-ai-search]] (09-12), [[game-rl-daily]] (09-12), [[conference-digest]] (09-09)) — all 12 featured IDs grep-verified 0 hits in `wiki/`.

## Summary

0 direct CTR papers in this window (all Sep-11-mailed CTR/ads work was captured by 09-11/09-12 digests). The standout signal this time is **LLM-as-judge validity under audit pressure**: tone shifts the severity operating point (RecSys'26 reproducibility paper), a living benchmark database exposes saturation (Benchmark Radar), and a pre-registered checkpoint audit shows unlearning numbers move per checkpoint. Secondary themes: **conversational/individualized recommendation** (politeness in judging, purchase-advice measurement limits, song embeddings, DoRA individualization), **agentic LLM serving economics** (multi-turn routing, tail-aware turn release), and **multi-agent + ecosystem dynamics** (Bayesian backward reasoning for disagreement, model-collapse concentration invariance). 12 papers across 5 themes.

---

## ① Recommendation, Conversational Rec & Judging (4)

### Should I Be Polite to My LLM Relevance Judge? Tone as a Severity Operating-Point Shift
- **arXiv**: 2609.09703
- **Authors**: Tian Zhang, Meng Li
- **Affiliation**: RecSys '26 (20th ACM Conference on Recommender Systems), Reproducibility and Practice Notes track
- **Key contribution**: Audits prompt *tone* on **3,498 TREC DL19/DL20 query-passage pairs**, across **8 judge models**, 5 classifier-calibrated politeness levels, and 3 paraphrases per level. Effects are strongly model-dependent (one judge shows a structured U-shaped response). Where tone changes agreement, it acts as a **severity operating-point shift** (overall scoring leniency) rather than improved judgment. A query-disjoint cross-fit retains the association (Spearman ρ = -0.683; exact model-block permutation p = 0.019). Tone affects calibration-based agreement more than ranking outcomes: max mean |ΔNDCG@10| = 0.011 across 32 model-tone contrasts, but Kendall's τ as low as 0.743 shows reordering is reduced, not absent.
- **Relevance**: Prompt tone is a validity threat when absolute relevance labels matter (e.g. thresholding, LLM-EC, recounting) but near-neutral for ranking. Reconciles prior contradictory "politeness hurts/helps" findings. Directly useful for LLM-judge pipelines in rec/ads ranking eval. (Closest thing to a CTR-adjacent paper in this window.)

### Purchase Advice and Observable Buyer Responses in Real AI Conversations
- **arXiv**: 2609.09878
- **Authors**: Benjamin Tannenbaum
- **Affiliation**: Aiso (proprietary, licensed, consent-based conversation database)
- **Key contribution**: Observational audit of **317 historical assistant conversations** (Aiso research database). Single-agent AI-assisted screening isolates **68 purchase-directed records** → **67 retained episodes** (Apr 2023 – Jul 2025). Assistant offers candidate options, acquisition channels, or conditional preferences in **52/67 (77.6%)**; only 1 episode shows conditional redirection. **No episode** codes as advice to abandon the purchase category. Only **18 (26.9%)** contain a subsequent user turn in the same purchase mission; using conversation depth alone overstates follow-up availability by 27.8%. Across 47 follow-ups, **no explicit post-advice purchase commitment / completed-purchase report / abandonment statement**. Central finding is a **measurement limitation**: recommendation content is observable far more often than the buyer's decision. Explicitly disclaims causal/population estimates.
- **Relevance**: Evidence base for "do generative assistants persuade people to buy?" — the honest answer is still unmeasurable from conversation logs alone. Relevant to ads/CTR teams evaluating LLM-driven sales/conversational commerce attribution.

### Project Qualia: Recovering Experiential Music Structure from Session Co-occurrence Data
- **arXiv**: 2609.10862
- **Authors**: Nizam Mohammed, Abu B. S. Rahman, Dimuthu D. K. Arachchige
- **Key contribution**: Large-scale listening dataset: **1.29B scrobbles / 9,396 users** via Last.fm API → **531.6M training scrobbles across 28.6M sessions**. Trains a skip-gram Song2Vec model (session = sentence, track = token); embedding space is dominated by **artist identity** (single-artist runs). Artist-residual procedure (subtract each artist's centroid) drops mean cross-artist cosine similarity from 0.2487 → **0.0005**, yet **4,577 cross-artist track pairs keep cosine ≥ 0.70**, forming coherent genre/era clusters (trip-hop, 1990s grunge, 2020 mainstream pop; cross-composer classical pairs up to 0.95). Establishes an empirical basis for learning an artist-independent "experiential" layer.
- **Relevance**: Session-co-occurrence embeddings for music rec — an artist-agnostic experiential similarity signal that metadata/genre taxonomies miss. Interesting co-occurrence methodology for rec systems generally.

### From Retrieval to Weights: Parametric Individualization of Small Language Models with Individual Text Corpora
- **arXiv**: 2609.10155
- **Authors**: Christoph Wigbels, Ali Abusaleh, Markus T. Jansen, Alexander Mehler, Markus J. Hofmann
- **Affiliation**: Goethe University Frankfurt group (cognitive simulation / text technology)
- **Key contribution**: Studies **episodic/semantic memory in SLMs** by writing each individual's text corpus (ITC, crawled search histories of **515 participants**, stratified subsample of 150) into the weights via DoRA adapters on an SLM whose baseline correctness is below the participants' lowest quartile. The adapter measurably writes the ITC into weights: fits its own participant's held-out text better than others' (dz = 1.27), and individuality grows with ITC size (rank order). On the generalized knowledge test, however, the adapter **adds knowledge rather than alignment**: log-loss match improves, match accuracy under bias-corrected PMI does not, and retrieval adds nothing on top.
- **Relevance**: Parametric individualization of SLMs (one small adapter per user) — basis for individualized tutoring/personal agents. For rec/ads: a "personal model" alternative to per-user retrieval pools.

---

## ② LLM Serving, Routing & Scheduling (2)

### SWRouter: Similarity-Contractive Window Routing for Multi-Turn Large Language Model Conversations
- **arXiv**: 2609.11414
- **Authors**: Yu Wang, Yuchen Li, Rui Kong, Xinran Chen, Jiamin Chen, Hengyi Cai, Shuaiqiang Wang, Jiashu Zhao, Yulun Zhang, Zhonghao Lyu, Haoyi Xiong, Linghe Kong, Jimmy Xiangji Huang, Dawei Yin
- **Affiliation**: Baidu-affiliated team (Dawei Yin) + SJTU / York University
- **Key contribution**: Multi-turn model routing. Argues single-turn routers don't transfer because routing performance depends on how historical context is segmented/retained (information loss or confusion) and because routing quality is conflated with prompt-construction quality. SWRouter = **similarity-based context segmentation** for prompt construction + a **dual-metric evaluation framework** that decouples construction accuracy from router performance. Beats best single LLM by **+16.26%** evaluation accuracy and the Conv-ID Context baseline by **+8.22%** on multi-turn dialogue benchmarks.
- **Relevance**: Multi-turn routing matters for assistant products and agent memory; the construction-vs-routing decoupling generalizes to agent context assembly. Rec-adjacent via Baidu/ads ecosystem.

### Decoupling Readiness from Release for Tail-Aware Scheduling of Agentic LLM Workflows
- **arXiv**: 2609.10964
- **Authors**: Bochao Feng, Jianjiang Li, Haojie Wang, Lin Qiao, Yinghui Li, Yukun Yan, Jidong Zhai
- **Affiliation**: Tsinghua University group
- **Key contribution**: Agentic workflows fail on tail latency because runtimes release turns **eagerly** on readiness; under contention, released-but-unfinished work queues up and can no longer be reordered. Proposes a tail-risk-aware **turn-release scheduler** that jointly decides which ready turn to release and how much released-unfinished work to maintain, using a **mean-CVaR** objective, online work estimates, and an adapted released-work budget. On real software-engineering agent execution traces across multiple LLMs/arrival rates: comparable to eager release at light load, **up to 3.50× P95 flow-time speedup** under contention.
- **Relevance**: Agent serving infra — controlling flow time of multi-turn agent workflows; complements the wiki's serving/efficiency themes (py-kvcache, LOCUS, power control).

---

## ③ Agents, Collective Decision-Making & Data Systems (2)

### When Agents Disagree: Bayesian Backward Reasoning as a Label-Free Anchor for Multi-Agent Collective Decision-Making
- **arXiv**: 2609.11709
- **Authors**: Ken Chen, Wei Wang, Sachith Seneviratne, Hansani Weeratunge, Saman Halgamuge
- **Affiliation**: University of Melbourne group
- **Key contribution**: Voting/judges aggregate forward (evidence→label) estimates that share a common factorization and can inherit **correlated errors**. Constructs a **reverse posterior** per instance via Bayesian backward reasoning from an explicit likelihood; forward and reverse factorizations rarely share errors symmetrically. Ranks agents by **cross-path consistency** using Jensen-Shannon divergence → three strategies: **MinJS** (hard selection), **FwdJS** (soft reweighting), **LogLin** (log-linear fusion). On **DDXPlus** across 5 LLM backbones: MinJS beats random selection everywhere; LogLin is best overall, with its largest gains on the disagreement subset. A lightweight two-stage calibration further refines the reverse anchor.
- **Relevance**: Label-free aggregation of disagreeing agents — directly applicable to ensemble judges, LLM-EC, multi-tower ranking fusion where correlated errors dominate.

### Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology Tagging of Enterprise Data Catalogs
- **arXiv**: 2609.10430
- **Authors**: Kostia Kudriavtsev, Parvez Rafi, Sha Sundaram
- **Key contribution**: Production system for data-catalog documentation debt: **Descriptor** grounds column descriptions in the *pipeline source code* that produces each column (retrieved on demand from enterprise GitHub via an active RAG reasoning-acting tool loop); **Tagger** labels columns from a governed **275-leaf Data Classification Ontology** using three parallel strategies (description tagger, line-of-business regex tagger, fine-tuned contrastive metadata encoder over a vector DB) fused by **Reciprocal Rank Fusion**. A 6-layer **MiniLM** metadata encoder fine-tuned with in-batch contrastive objective lifts same-tag retrieval NDCG@10 0.55 → **0.92** and MAP@100 0.19 → 0.90 on the in-distribution held-out split. Value-free, code-grounded, per-tag provenance, graceful degradation.
- **Relevance**: Multi-agent catalogue + governance tagging at production scale; the "tag data as it's created" approach matters for rec/ads feature stores and compliance.

---

## ④ Evaluation Infrastructure & Measurement Audits (2)

### Benchmark Radar: A Living Database and Search Engine for AI Benchmarks and Evaluation
- **arXiv**: 2609.11115
- **Authors**: Koutian Wu, Junjie Zhou, Ergan Shang, Jiayu Wang, Pengqian Han, Junkai Wang, Wanghan Xu
- **Key contribution**: Living database/discovery system for AI benchmarks (LLM eval, agentic/tool-use, coding, reasoning, safety, domain-specific). **Daily ingestion from 37 sources** (13 direct connectors + 24 first-party research/engineering feeds). Catalog: **1,283 source records** from 4 benchmark catalogs, **12,916 numeric observations** on 790 records. Retains source identities/citations for evidence inspection. Ships a **web dashboard** with leaderboard, **Pareto-frontier view of score vs. measured use**, saturation and trend views, daily feeds, downloadable evidence, CLI for offline queries. Audits benchmark saturation, adoption trends, and the limits of score comparison; includes a worked prior-art-search example.
- **Relevance**: Measurement-infrastructure trend: "which benchmark to use / is it spent" becomes a first-class tool; pairs with the wiki's benchmark-validity theme (Clean Engineering Unstable Measurement, grain-of-truth evals).

### Published Unlearning Numbers Move Per Checkpoint, and Not Because the Removed Data Survives: An Audit of 263 Released Batch-Normalized Checkpoints
- **arXiv**: 2609.11490
- **Authors**: Junlong Shen, Xingyu Li
- **Key contribution**: Pre-registered (29 Aug 2026) audit of **263 released batch-normalized checkpoints**, independent of/concurrent with arXiv:2609.08901. Refitting BN statistics on kept data at **bit-identical weights** moves **47/221** released checkpoints past their own release's seed spread — several inside a method whose *average* does not move. The mover is **not** surviving removed data: swapping kept↔removed records in a fixed fitting pool hardly moves a published cell; instead the checkpoint's drift from any refit tracks it. Practical impact: **12 verdicts cross**, 4 clear a measured recalibration budget, 2 clear it on every replicate; a population trained and sited near its own criterion yields none. Recommendation: a release should name the **fitting convention** beside the number.
- **Relevance**: Audit-culture paper for ML releases; directly challenges the stability of published (un)learning numbers. For rec/ads: same class of concern as unstable offline metrics (cf. Clean Engineering Unstable Measurement).

---

## ⑤ Ecosystem Dynamics & Finance (2)

### The Oligarch Barely Steers Model Collapse in Multi-Model Ecosystems
- **arXiv**: 2609.11146
- **Authors**: Yangze Liu, Zhongyi Han
- **Key contribution**: Controlled multi-model ecosystems: **13 open 1–4B models** form ecosystems of 3–13 players, plus an injected probe pushing the top share to **90%**; each generation every model's output is mixed into a shared pool by market share and all retrain from clean base weights, for **5 generations**. Result: an **invariance** — making the split more unequal barely changes collapse speed; destinations move even less (share/identity knobs shift 5-generation endpoints by only a few percent of the common drift). Extreme share + strongest injected bias still does not guarantee steering. What sets speed is **who supplies the pool**: fixed shares, swapping a K=3 ecosystem's members changes 5-generation drift **2.8×**; a share-weighted index of member susceptibility explains speed differences across 19 arms with **R² = 0.68**; replacing half the pool with human text roughly halves drift without changing its course (cf. the "distillation blues" document).
- **Relevance**: Data-ecology version of model collapse (cf. [[model-collapse]] theme). For LLM-data pipelines in rec/ads: who you buy/derive data from, not market concentration per se, governs synthetic-data drift.

### Making Alternative Data Work: Context-Augmented LLMs for Financial Forecasting
- **arXiv**: 2609.11607
- **Authors**: Jihoon Kwon, Lawrence Liu, Daekyung Park, Sumin Kim, Haverty Jack, Hoyoung Lee, Katherine Bjorkman, Josh McKenney, Peter Laurelli, Nicole Kagan, Zach Golkhou, Thorsten Neumann, Edward Tong, Pete Petersen, Yoon Kim, Alejandro Lopez-Lira, Yongjae Lee, Chanyeol Choi
- **Key contribution**: Two-agent framework for revenue forecasting with **alternative data** (consumer transactions, web traffic, prediction markets — channels that are sparse in history, firm-specific, and heterogeneous). Agent 1 identifies for which firms each channel is likely informative; Agent 2 predicts revenue using firm- and channel-specific in-context context. Across **4 commercial alternative-data channels**: adding alternative data *in context* beats either source alone, and beats standard forecasting baselines — all **without task-specific parameter updates** (in-context learning on a pretrained LLM).
- **Relevance**: ICL as the integration mechanism for heterogeneous/sparse data — a pattern that transfers to rec/ads predictor fusion; finance-adjacent for the wiki's market/factor research.

---

## Bottom line

- **0 direct CTR papers**; closest rec-adjacent signal = LLM-judge tone effects on relevance labels (2609.09703) and conversational purchase-advice measurement limits (2609.09878).
- **Validity pressure on LLM-as-judge is the meta-theme**: tone severity shifter (RecSys'26), living benchmark database w/ saturation views (Benchmark Radar), pre-registered checkpoint audit (BN-fitted unlearning numbers).
- **Serving economics for multi-turn agentic traffic**: routing (SWRouter) and turn-release scheduling (Tsinghua) both treat context/flow, not single-turn inference.
- **Ecosystem-level dynamics**: concentration invariance of model collapse + label-free disagreement aggregation — "who/what you average over" beats "how big the top player is".