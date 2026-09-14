---
title: "arXiv Paper Check — AI & CTR (September 14, 2026)"
type: synthesis
created: 2026-09-14
updated: 2026-09-14
sources: [arxiv.org]
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, creative-optimization, agentic-web, retrieval, memory, ir, agents, judging, evaluation, verification, distillation, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 14, 2026)

> **Mailing**: Mon, 14 Sep 2026 — first fresh announcement since Fri 11 Sep. Covers the Wed 10 – Thu 11 Sep submission wave (IDs ~2609.11933–2609.13144).
> **Scan scope**: cs.AI (163 new/cross ≥ 2609.11900), cs.IR (19), cs.LG (177) from `arxiv.org/list/{cat}/new?show=500`.
> **Dedup**: Zero overlap with same-day [[arxiv-daily]] (09-14, 30 featured papers) and all 09-11→09-13 siblings (arxiv-paper-check / arxiv-ai-search / conference-digest / game-rl-daily / tech-report-digest). All 9 featured IDs + 4 runner-ups grep-verified 0 hits in `wiki/`.

## Summary

One genuinely new **ads/CTR production paper** this window: **PinDCO** (Pinterest) — dynamic creative optimization at scale with whole-page/pixel-aware scoring (creative scarcity is over; selection is the constraint now). The bigger structural signal is **recommendation theory turning agent-first**: two position papers argue the receiver of a recommendation is no longer always a (directly) human — PAMR (agent-mediated evidence mediation) and "Who Are We Recommending To?" (delegation spectrum). On the AI side, the payoffs cluster around **agent-quality measurement & repair**: a two-gap framework for agentic SWE verification failures, a contamination-controlled harness-vs-model isolation study, a label-free bias audit of LLM judges, an agentic memory retriever, and a compact-reasoner internalization recipe. 9 papers across 5 themes.

---

## ① Ads & CTR (1)

### PinDCO: Whole-Page Aware Dynamic Creative Optimization at Scale
- **arXiv**: [2609.11943](https://arxiv.org/abs/2609.11943) — cs.IR (also cross-listed cs.LG)
- **Authors**: Yu Hao, Yuchun Li, Peimeng Sui, Meilin Liu, Tianyuan Cui, Hao Li, Zicong Zhou, Akanksha Baid — **Pinterest**
- **Key contribution**: Generative AI has made ad-creative *supply* cheap; the binding constraint is now scalable **creative retrieval and selection** under latency/cost budgets. PinDCO is a production DCO system built around a **Creative Component Fusion Network (CCFN)**: each creative component (image, title, layout) gets a dedicated tower with component-specific hyperparameters (different modeling complexity), fused to predict a **creative-level score conditioned on the ad-level prediction**; training-data quality is improved via an exploration–exploitation strategy. To handle Pinterest's **waterfall grid layout**, a **Pixel-aware Adjustment Module (PAM)** adjusts scores based on a creative's rendered size and its effect on nearby content and session-level engagement.
- **Relevance**: The first big-platform DCO paper this window and the only direct CTR/ads contribution in the Mon mailing. Maps onto the generative-creative wave tracked in this wiki (AdMan-style pipelines make variants unbounded; ranking *among* creatives — whole-page aware — is where ad CTR value now hides).
- *(tentative: abstract truncated before eval numbers; contributions summarized from the method description)*

---

## ② Recommendation in the Agentic Web (2)

### Position: Recommender Systems Should Move Beyond Platform-Centric Ranking toward Personal Agent-Mediated Recommendation
- **arXiv**: [2609.11942](https://arxiv.org/abs/2609.11942) — cs.IR
- **Authors**: Haohan Yuan, Peng He, Dan Zhang, Jianpeng Liang, Junning Zhu
- **Key contribution**: Argues the next recommendation bottleneck is not preference modeling but **control over evidence acquisition and disclosure**. Platforms currently determine candidate access, evidence boundaries, explanations, and the path from need to output. Proposes **Personal Agent-Mediated Recommendation (PAMR)**: a user-facing agent discovers, filters, aggregates, and governs recommendation evidence across distributed sources — the shift is from *platform-side item ranking* to *user-side evidence mediation*. Defines PAMR's boundary criteria, core mediation decisions, and a **mediation-centered evaluation framework**; a proof-of-concept on hard Yelp restaurant tasks shows that, under a shared LLM ranker, source selection and controlled disclosure materially change outcomes.
- **Relevance**: Direct continuation of the [[byoai|BYOAI]] / agent-as-user thread the wiki tracks — if agents absorb the recommendation pipeline, ranking models become inputs to a mediation layer rather than final decision makers. Complements today's agentic-web papers and the chronicle of agentic rec in [[conference-digest]] (09-13).

### Who Are We Recommending To? Recommender Systems in the Agentic Web
- **arXiv**: [2609.11945](https://arxiv.org/abs/2609.11945) — cs.IR
- **Authors**: Himan Abdollahpouri, Kyle Kretschman, Sai Ravindranath, Jackie Doremus, Mounia Lalmas (Spotify, inferred)
- **Key contribution**: Recommenders were designed assuming a human consumes each recommendation directly; LLM agents increasingly browse/compare/negotiate/transact on the user's behalf. Argues the paradigm is **bifurcating**: in *delegable* contexts (routine purchases, travel, constrained transactions) the primary operational consumer becomes the **agent** — requiring new optimization objectives, interaction protocols, and evaluation criteria; in *experiential* contexts (entertainment, subjective/high-stakes choices) humans remain the final judge, with agents assisting via pre-filtering. Introduces a **delegation spectrum** characterized by factors such as preference specifiability, outcome value, and transaction reversibility.
- **Relevance**: Gives the agentic-Web debate a usable axis (delegation spectrum) and — with the PAMR position — both sides of the "who is the user" question facing rec/ads teams whose surface is increasingly agent-driven. Pairs with the [[agents]] theme and the "who are we recommending to?" worry raised for ad-auction agents in 09-14 arxiv-daily (pricing-collusion work).

---

## ③ IR: Memory Retrieval & Proactive Candidate Generation (2)

### MemRetriever: Learning to Search, Reflect, and Retrieve from Long-Term Memory
- **arXiv**: [2609.11951](https://arxiv.org/abs/2609.11951) — cs.IR
- **Authors**: Ruiyang Jiang, Chunyu Li, Zhiyu Li
- **Key contribution**: Static top-k memory retrieval misses evidence distributed across sessions and wastes context on multi-hop/temporal/knowledge-update questions. **MemRetriever** treats memory access as an **agentic multi-step search**: at each step it reasons over current evidence and selects **parallel search** (broad exploration), **serial search** (targeted completion), or **reflection/denoising** (filtering, evidence assessment), stopping once retained evidence suffices for the downstream answer. Warm-start supervised training on ReAct-style search-memory trajectories, then **GRPO**; the reward encourages evidence coverage, noise reduction, answer sufficiency, and efficient termination. Evaluated on LOCOMO, LongMemEval, HotpotQA, MuSiQue, and 2WikiMultiHopQA.
- **Relevance**: A retrieval-side answer to the memory-can-hurt results tracked this week (LifeFuse-Mem, mem-trap benchmarks): instead of recalling more, learn *when to stop searching and start answering*. Directly relevant to the long-term-memory agent line ([[mem1-agent]], RAG stacks) and to budget-sensitive production retrieval.

### InitGen: Candidate Generation for Interaction Initiation in Intelligent Assistants
- **arXiv**: [2609.11953](https://arxiv.org/abs/2609.11953) — cs.IR
- **Authors**: Ruize Shi, Jinhua Chen, Hong Huang, Ziniu Chen, Ruike Zhang, Jianxun Shi, Yitao Chen, Rui Zhang
- **Key contribution**: Production systems for **interaction initiation** (presenting clickable candidate queries when a user opens an assistant, before any in-session intent) face a *credit-assignment* problem: the generator produces more candidates than are displayed, and after downstream filtering/ranking only a subset is exposed — so observed feedback is **partial and cannot be reliably assigned to individual queries**. **InitGen** generates the candidate set **jointly** and aligns it with user feedback via **weighted preference optimization**: sample weights combine user-activity (reducing dominance of highly active users) and downstream ranking scores (as a practical estimate of feedback reliability), with a rolling-window update strategy. Deployed in OPPO's Xiaobu Assistant.
- **Relevance**: The "candidate generation under truncated exposure" problem is the search/rec mirror of CTR models trained on logged impressions — a directly reusable recipe for proactive-assistant surfaces and any generate-then-rank rec pipeline where only the head of the list is observed.

---

## ④ Agentic Software Engineering & Verification (2)

### Reality Is the Final Verifier: On Two Key Gaps in Agentic Software Engineering
- **arXiv**: [2609.12039](https://arxiv.org/abs/2609.12039) — cs.AI
- **Authors**: Alexander Krentsel, Shubham Agarwal, Mert Cemri, Shu Liu, Sidharth Sankhe, Ziming Mao, Matei Zaharia, Ion Stoica (UC Berkeley / Anyscale, inferred)
- **Key contribution**: Anyone iterating an agent on a static evaluator is chasing the **two-gap framework**: (1) **requirement gap** — requirements only approximate stakeholder intent; (2) **model gap** — the evaluator's model only approximates the real deployment environment. Reward hacking exploits omissions in either; hallucination widens the gaps by fabricating requirements or environment assumptions; and **neither gap can be generally certified closed in an open world**. So the objective shifts from closing gaps to **continuously narrowing them**: an **assurance-revision loop** that uses deployment evidence to revise requirements, model, or evaluator when stakeholders reject the resulting behavior.
- **Relevance**: Crystallizes the [[verification-gap]] intuition behind Software 3.0/agentic SWE into two testable failure channels — the same spirit as [[concepts/verification-gap]] and the agentic-coding hammer benchmarks tracked in recent digests. Useful frame for anyone building agent harnesses on this wiki's llm.c/nanochat-scale projects.

### Harness or Model? Isolating the Harness Effect in Agentic Coding with a Contamination-Controlled Private Suite
- **arXiv**: [2609.11987](https://arxiv.org/abs/2609.11987) — cs.AI
- **Authors**: Mohsen Arjmandi
- **Key contribution**: Controls for a confound everyone assumes away: vendors ship harnesses (tools/prompts/control flow) tuned to their own models. On a private, contamination-controlled suite of **256 repo + post-cutoff contest tasks**, pairs the same model under two harnesses — claude-agent-sdk vs deepagents on claude-opus-4-8; openai-codex SDK vs deepagents on gpt-5.5 (792/800 runs graded by an isolated oracle). **Neither contrast shows an average advantage**: −1.25pp for Opus 4.8 (48.8 vs 50.0; CI [−10.0,+7.5]) and +1.25pp for GPT-5.5 (55.6 vs 54.4; CI [−4.4,+6.9]). But the Opus average hides opposite strata: the native harness trails by **9.0pp on the 61 repository tasks** and leads by **23.7pp on the 19 contest tasks** (label-permutation p=0.003) — a post-hoc partition explicitly flagged as needing a designed replication.
- **Relevance**: A clean, falsifiable result for the harness-vs-model debate — vendor-native pairing is a *task-type* effect, not a universal edge. Directly relevant to the agentic-engineering line and to anyone benchmarking coding agents (mirrors the harness-engineering observations in autoResearch work).

---

## ⑤ Evaluation & LLM Judges (1)

### Can We Trust LLM Judges: A Study of Capability-Dependent Biases and Multi-Judge Ensemble for Bias Calibration
- **arXiv**: [2609.12002](https://arxiv.org/abs/2609.12002) — cs.LG / cs.AI
- **Authors**: Gemma Zhang, Prachi Badarayani, Asmi Kumar, Sadid Hasan, Sulaiman Vesal
- **Key contribution**: Studies **absolute scoring** (not the pairwise setting most prior work covers), across 4 benchmarks × 6 models (36 judge–examinee pairs). A model's task accuracy strongly predicts its judging accuracy (r ≥ 0.90 on most models) and inversely its directional bias (r ≤ −0.83) — **but accuracy alone does not ensure fairness**: more capable examinees consistently receive *more lenient* judgments from all judges (r ≥ 0.83). Proposes **calibrated weighted majority voting (WMV)**: an ensemble of judges weighted by *online estimates of false-positive/false-negative rates* derived purely from **inter-judge agreement patterns** (label-free, no ground-truth or task metadata) — tracked under shifting task distributions in a simulated experiment.
- **Relevance**: Tightens the LLM-judge reliability story the wiki has been tracking (tone shifts, benchmark audits, judge biases) with a **label-free bias-calibration recipe** — directly usable in rec/ads and agent evaluation loops where labels are scarce.

---

## ⑥ Efficiency: Distillation & Expert Consolidation (1)

### From Collaboration to Capability: Internalizing Routed LLM Experts into Compact Reasoners (RIVET)
- **arXiv**: [2609.12578](https://arxiv.org/abs/2609.12578) — cs.AI
- **Authors**: Frank Nie, Shuyao Wang, Ethan B. Liu
- **Key contribution**: A compact controller can coordinate stronger experts (selecting whom to consult, formulating requests, integrating answers) — this paper asks whether the controller **keeps the capability after the experts are removed**. **RIVET** ("collaboration internalization") uses (1) **expert-augmented RL** applying a shared outcome signal to both controller decisions and returned expert spans, and (2) **verified trajectory internalization** — format-aware supervised consolidation of complete successful interactions. The deployed controller runs code and interaction structure with **local Python execution and no external LLM**. On 7 competition-math benchmarks: RIVET-1.7B 28.25% / RIVET-4B 44.16% average accuracy; Stage II improves RIVET-4B **+6.49pp after expert removal**; GPQA-Diamond gives generalization evidence to scientific reasoning.
- **Relevance**: A route from expensive routed-expert systems (MoE, routed APIs) to **compact, self-contained reasoners** — the efficiency/distillation complement to the MoE-RL thread in [09-14 arxiv-daily](arxiv-daily.md) (ESRL). Matters for serving cost and for "can we distill the benefit of routing into a dense model" on the Karpathy distributed-compute line.

---

## Cross-Cutting Themes

1. **Creative abundance flips the CTR problem**: generative creative pipelines (AdMan last run; PinDCO today) make variant supply unbounded — the bottleneck moves to whole-page-aware creative *selection*. Flagging a persistent theme for the ad-tech pipeline in this wiki.
2. **The recommendation customer is now ambiguous**: two position papers in one mailing (PAMR, delegation spectrum) argue rec/ads must decide who the receiver is — agent or human — before optimizing anything. Expect agent-mediated advertising/rec measurement to be a recurring 2026Q4 theme.
3. **Verification is being made empirical**: two-gap framework + contamination-controlled harness isolation + label-free judge calibration all try to make "does the agent actually work" measurable rather than asserted — extending the [[concepts/verification-gap]] thread.
4. **"When to stop" returns as an efficiency lever**: MemRetriever (stop searching when evidence suffices) and InitGen (weight feedback by exposure reliability) both attack the information-waste end of retrieval — complements the token-budget pressure on long-context systems.

## Runner-Ups (verified 0 hits)

- **[*Personalized and Trust-Aware Health Recommendation Policies*](https://arxiv.org/abs/2609.12679)** (2609.12679, cs.IR) — health-recommendation policies over construction-workplace data; trust-aware framing; niche domain but a rare non-commerce rec paper this mailing.
- **[*A Historical Corpus Is Not a Historical System: Auditing Hindsight Leakage in Stateful Data Discovery*](https://arxiv.org/abs/2609.12766)** (2609.12766, cs.IR) — hindsight/state-leakage audit for data-discovery systems; a benchmark-validity-flavored negative-result engineering audit (companion to *Learning the Lake*, 2609.12754).
- **[*When Does AI Augment Work?*](https://arxiv.org/abs/2609.12482)** (2609.12482, cs.AI) — CIVIC-AI six-condition framework for workflow-level human-AI augmentation; no new results, but the cleanest statement of when augmentation counts (ties to the future-of-work thread).

## Method Note

Queries: `https://arxiv.org/list/{cs.AI,cs.IR,cs.LG}/new?show=500` (Mon 14 Sep mailing) — direct list pages (arXiv API returned HTTP 429 under rate limits; list pages expose the same abstracts). Candidate window ≥ 2609.11900; dedup via `rg '<id>' wiki/` (0 hits required) plus explicit exclusion of all IDs featured in same-day 09-14 arxiv-daily and 09-11→09-13 siblings. All abstract-level claims summarized from the arXiv list-page abstracts; numbers are author-reported. The 09-14 arxiv-daily already captured the window's Rec/LLM-train flagship papers (ChronicleRec, OneLA, MIMA, retriever-verifiers, RLHF-distortion, ESRL, byte models, family of attention/memory work) — this pass intentionally covers the orthogonal AI & CTR set.