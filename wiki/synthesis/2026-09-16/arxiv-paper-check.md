---
title: "arXiv Paper Check — AI & CTR (September 16, 2026)"
type: synthesis
created: 2026-09-16
updated: 2026-09-16
sources: [arxiv.org]
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, serving, kv-cache, quantization, distillation, reward-integrity, diversity, semantic-collapse, tabular-models, generative-recommendation, e-commerce-agents, evaluation, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 16, 2026)

> **Mailing status**: **Fresh mailing is live** — arXiv `/list/{cat}/new` for cs.AI / cs.IR / cs.LG / cs.CL all headline **"Wednesday, 16 September 2026"** at run time (≈10:25 CST, 02:25 UTC). Observed fresh band: IDs **2609.16004 → 2609.17527** (Tue 15 Sep submissions) — entirely above the 09-15 sibling ceiling (2609.15996, itself corrected: 2609.16000 is an older 2026-07-23 record). This is the genuine "last 24 hours" haul, not another remainder sweep.
> **Scan scope**: Parsed 755 raw entries (cs.AI 297, cs.LG 277, cs.CL 159, cs.IR 22) → 576 unique IDs → **374 fresh vs the 5,597-ID wiki coverage set** (all 374 uncovered). Cross-excluded every ID cited by same-day siblings — [[arxiv-ai-search]] (09-16, 52 IDs incl. 22 featured) and [[arxiv-daily]] (09-16, Tue-15 window ≤ 2609.15989) — so all 9 featured + 6 runner-up IDs grep-verify **0 hits in `wiki/`**.
> **CTR/ads verdict**: **The Wed-16 mailing breaks the multi-day noise floor** — direct ads/CTR/rec content is back (consistent with the sibling ai-search finding: 1 direct ad-auction paper + 4 production ranking/marketplace papers with online numbers). This paper-check *does not re-expand* those 09-16 sibling-covered picks (see Cross-Digest §1.1); it adds the still-unclaimed AI & CTR-side remainder.
> **Dedup**: Featured/runners all ⩾ 2609.16051, none in `wiki/`, prior-0915-reported set (≤ 2609.16000), or the 52-ID ai-search reference set.

## Summary

After four windows of ≈0 direct CTR content, the arXiv pipeline finally shipped a proper mailing again — but the AI & CTR highlights of the **Wed 16 Sep batch were already claimed** this morning by the concurrent [[arxiv-ai-search]] (Wolt UVR delivery ranker, Facebook Marketplace PCap, AURA agentic recsys, ReliGRec, ROI-constrained ad auctions). This paper-check therefore does what the 09-15 check did in reverse: rather than draining a stale window, it **mines the unclaimed remainder of a fresh one**, from the AI & CTR side. What's left is still substantive. On the *CTR/recidity* side: an **environment-grounded verification harness for open-weight e-commerce agents** that decomposes a single task-success score into 44 metrics with per-step evidence (2609.16093), and **LimiX-2**, the second-generation contextual-mechanism tabular foundation model that shifts in-context learning from target-centric to joint-distribution modeling p(x,y|D) — the strongest continuation yet of the wiki's `FAT/EST/SUAN` numeric-native tabular thesis (2609.17488). On the *systems* side the theme is **where state actually lives**: two papers from the same group on disaggregated serving (calibrate-then-route learned scoring vs. queue counting, 2609.16206) and KV tier placement (GPU/CPU/SSD, "gains come from tier capacities, not policy", 2609.16215), a 200K-token-on-a-24 GiB-laptop MLX runtime that answers 29/30 AIME problems (JustFit, 2609.17475), and a genuinely new backward-pass theory of the Z-loss that runs through the exact dense output heads and sparse routers CTR/rec towers use (2609.16179). The *reward-integrity* line continues: a clean game proving language models over-accuse honest reward reporters (2609.17226), and a distillation algorithm that couples teacher calibration with student updates so systematic teacher bias can be overcome without target-domain reward feedback (2609.17474, MIT/Simchi-Levi). 9 papers + 6 runners-up, 4 themes. All figures author-reported from abstracts.

---

## ① CTR-Track Cousins: E-Commerce Agents & Structured-Data Intelligence (2)

### Environment-Grounded Verification of Open-Weight E-Commerce Agents
- **arXiv**: [2609.16093](https://arxiv.org/abs/2609.16093) — cs.LG
- **Authors**: Nimit Shah, Haitz Sáez de Ocáriz Borde
- **Key contribution**: A shopping conversation reaches the same cart many ways, and a single task-success score collapses all of them. The authors build a **deterministic, reproducible e-commerce environment that pre-commits every trial's circumstances** (persona, difficulty, target cart, item-reveal schedule), with a simulated consumer attempting to buy the target cart and a bidirectional simulator that can abort on frustration or inject directives (when to explore, defer, or recall). Crucially, every assistant action is recorded *against the environment state at that moment*, so the evaluator can attribute failure to parts of the conversation with retained evidence — e.g., a search is penalized for not surfacing a target product *only if the customer already mentioned it*; tool calls are penalized differentially vs. an expected tool-call set. Across **8 open-weight agents (20B–35B), 160 trials each, 44 metrics**, the resulting capability profiles separate **under-action, over-purchase, unsupported product attributes, and poor search** — all of which terminal success obscures.
- **Relevance**: Directly the [[concepts/verification-gap]] thread applied to shopping agents: env-grounded per-step verification instead of single-score leaderboards. For CTR/ads, this is the evaluation harness any e-commerce agent-rec product needs before it serves traffic; the metric-decomposition recipe transfers to recsys conversation quality.
- *(tentative: abstract-level; per-agent numbers not in the abstract)*

### LimiX-2: Contextual Mechanism Network for Structured-Data Intelligence
- **arXiv**: [2609.17488](https://arxiv.org/abs/2609.17488) — cs.AI
- **Authors**: Xingxuan Zhang, Gang Ren, Hao Yuan, …, Yushan Han, Peng Cui (57 authors; Tsinghua/Peng Cui group; industrial lineage)
- **Key contribution**: Second-generation **LimiX** built from the family's own scaling laws, adopting **Contextual Mechanism Networks (CMNs)**: the organizing principle of in-context learning shifts from target-centric `p(y|x, D_ctx)` (the convention of tabular PFNs) to mechanism-oriented **joint modeling of `p(x, y | D_ctx)`** — a context-dependent representation of the underlying generative structure. Pretraining uses **synthetic structural-causal-model (SCM) datasets** spanning diverse graph structures, functional mechanisms, and observation processes; objectives use Context-Conditional Masked Modeling (CCMM). Beats dataset-specific models and prior tabular foundation models on **TabArena, TALENT, and BCCO**, and — notably for this wiki's thesis — the CMN paradigm yields **causal awareness** (feature-attention alignment with underlying mechanisms), not just predictive accuracy.
- **Relevance**: The numeric-native / mechanism-level continuation of the CTR-scaling line the wiki tracks (FAT/EST/SUAN-style results). "Joint structure, not next-label" is precisely the direction CTR stacks want — user/item/ad tables are *structured data* — and it corroborates 09-15's LQ value claim that consequential quant domains need more than language-native reasoning.
- *(tentative: single-source, abstract-level; "causal awareness" is the authors' framing)*

---

## ② Serving & Cost: Where State Lives, When to Route, How Cheap Weights Can Go (4)

### Calibrate, Then Route: Learned Request Routing for Disaggregated LLM Serving
- **arXiv**: [2609.16206](https://arxiv.org/abs/2609.16206) — cs.AI
- **Authors**: Srikanta Datta Tumkur, Jay Iyer, Mehar Simhadri, Sai Pavan Kumar, Sai Kapil Kumar, Ramesh Nampelly
- **Key contribution**: Disaggregated serving (DistServe/Splitwise/Mooncake) separates prefill and decode, but routing still decides *which* instances serve each request. The authors study a router that estimates **additional completion time per instance** from exact prompt length, predicted output length, post-admission KV pressure, and SLO class — developed in a discrete-event simulator and validated on **eight A40 GPUs each running vLLM with NIXL KV transfer**, at measured saturation. Across three bursty traces, the calibrated router hits the **best mean goodput (0.864 vs 0.835–0.847** for round-robin/least-loaded/length-heuristic) with lowest variance. Two discipline results: (i) **hardware calibration matters** — simulator-derived constants cost 4.5 goodput points and ~40% of tail-latency advantage, degrading the scorer to "little more than queue counting"; (ii) at extreme scarcity, greedy cost-minimization concentrates load on the cheapest scored instance and **blind spreading beats it** — and the calibrated router matches round-robin goodput with **six GPUs instead of seven**.
- **Relevance**: The serving/LatencySLO thread ([[concepts/verification-gap]]-adjacent systems thread; sibling 09-16 SQD lineage). For ad/rec serving, applying price-free learned routing only after calibration is the transferable lesson — uncalibrated cost models silently become queue counters.
- *(tentative: abstract-level; A40-scale lab, not production trace at scale)*

### Where Should the KV Cache Live? Tier Placement Across GPU / CPU / SSD
- **arXiv**: [2609.16215](https://arxiv.org/abs/2609.16215) — cs.AI (same UCD-grounds group as 2609.16206)
- **Authors**: Srikanta Datta Tumkur, Jay Iyer, Mehar Simhadri, Sai Pavan Kumar, Sai Kapil Kumar, Ramesh Nampelly
- **Key contribution**: Companion study over the same simulator, calibrated against a random-forest execution-time predictor, comparing **recency, reuse-frequency, predicted-reuse, and an EWMA predictor with prefetch lookahead** across chat / agent / document-QA workloads. Headline: **tiering supports 73× more concurrent sessions per GPU and 62× lower cost/session — but that comes from the tier capacities (1 + 8 + 64), not the placement policy.** At batch-one decode (compute-bound), placement barely affects throughput; it trades PCIe migration traffic vs. time-to-first-token. **Recency gives 2.3× less migration traffic than reuse-frequency for chat; reuse-frequency wins for agent and doc-QA.** Two debunking notes: (i) the widely-recommended "predicted reuse" policy is **byte-identical to recency** (its agent recommendation is effectively recency); (ii) **prefetching never beats no-prefetch on migration traffic**, even with a future-request oracle.
- **Relevance**: A measured "capacity > policy" result that should temper KV-tiering marketing claims across the wiki's KV-engineering line (FlashPrefill-V2, DeepSeek-V4.1-Flash KV footprint, 09-14/09-16 KV-eviction papers). Directly usable cost discipline for serving budgets.
- *(tentative: single-group simulator study; trend claims match 09-16 ai-search KV-eviction divergence paper)*

### JustFit: 200K-Token LLM Serving on a 24 GiB Laptop
- **arXiv**: [2609.17475](https://arxiv.org/abs/2609.17475) — cs.AI / cs.PF
- **Authors**: Yuhua Chen
- **Key contribution**: Local open-weight reasoning is constrained by laptop memory for context *and* execution state. **JustFit** is an MLX-based runtime combining **KVExec** (compressed KV execution), **PhaseSwap** (component residency), and **StateTrans** (state-preserving serving transitions), coordinating just-in-time materialization/release **independent of weight quantization**. On a **24 GiB M4 Pro running Qwen3.8-27B MXFP4**, three runs complete **196,608-token input + 16,384-token output**, raising single-request context from the 30,720-position mlx-vlm baseline to **212,992 (6.93×)**; a two-request run holds 229,376 tokens aggregate. A 32K-input/64-output probe hits **19.11 tok/s**, median peak footprint 16,374 MiB, and the integrated runtime scores **29/30 on AIME 2026**.
- **Relevance**: Multiple of these capabilities would land directly on Karpathy's local-first computing bill of goods; the KV-exec/phase-swap/state-trans triad is a concrete recipe for the wiki's "200K tokens locally" target in the 09-16 sequences. Also the demo-able cousin of SQD-style disaggregation ideas on commodity hardware.
- *(tentative: single-author single-machine report; numbers author-reported)*

### Z-Loss Backward Geometry in Dense Output Heads and Sparse Routers
- **arXiv**: [2609.16179](https://arxiv.org/abs/2609.16179) — cs.LG / cs.CL
- **Authors**: Bum Jun Kim (30 pp.)
- **Key contribution**: Z-loss (the log-normalizer penalty used on LM output heads and MoE router logits) has always been understood as a scalar penalty. This paper analyzes it from the **backward pass**: the logit-space gradient ("backward source") is reset at the Z-loss branch, so its effect depends on how the *architecture and implementation* transport it. Developing a **backward-transport decomposition** separating source amplitude/shape from transport factors (common-shift coordinates, tied-embedding pathways, output-to-hidden gain, fused-loss consistency, optimizer-facing updates, top-k router reduction scale), it shows **nearly identical forward Z-loss values coexist with distinct gradients and, after transport, distinct parameter updates** — and explains why raw-logit Z-loss trims scalar tails without changing output-to-hidden gain, and why active-route reductions change the effective router coefficient. Architecture-aware variants reduce , on GPT-2/Pythia × WikiText-103/FineWeb-Edu.
- **Relevance**: The dense-head/sparse-router geometry this nails is *exactly* the training plumbing of ranking towers and MoE LLMs — a theory-and-diagnosis paper (not a new mechanism) that belongs on the shelf next to the routing line (09-15 Gavel implicit-skill routing, Trillion-Param MoE). For anyone tuning fused losses in CTR towers the "identical forward loss ≠ identical update" warning is directly actionable.
- *(tentative: single-author preprint; final evaluation numbers truncated in abstract — flagged)*

---

## ③ Reward Integrity & Calibration-First Distillation (2)

### Easy to Catch a Liar, Hard to Clear an Honest One
- **arXiv**: [2609.17226](https://arxiv.org/abs/2609.17226) — cs.LG / cs.AI / cs.CL
- **Authors**: Arman Nik Khah (15 pp., 9 tables)
- **Key contribution**: An agent learning from rewards can't distinguish "the world changed" from "the reporter broke" — RL theory says no further experience separates them; the escape is *richer data about the reporter*. This paper builds a **two-option game where a payout swap and a lying reporter produce byte-identical histories**, then appends a **single verified record** (one independently checked round printed beside what the reporter claimed) — enough to settle the case. Asked to answer one letter ("honest or lying?"), three large models (32B, 70B, 72B; Qwen + Llama families): they **catch a liar almost perfectly** (70B holds in every condition), but **clear an honest reporter far worse** — a 72B model calls an honest reporter a liar **38% of the time when nothing changed at all and 58% when payouts moved** (26%/48% for a 70B from the other family). The failure is not reading (0.96–1.00 with the answer printed); it's which *surface feature* matters — the round the record names (Qwen) vs. the letter that stands for the answer (Llama).
- **Relevance**: A clean, minimal measurement of **asymmetric verification bias in frozen LMs** — pairs with the reward-integrity literature (EMNLP'26-era judge audits in 09-14/09-15) and warns that monitor/reward-channel audits will systematically fabricate false accusations under distribution shift. Directly relevant to eval pipelines standing up "reward integrity" verdicts.
- *(tentative: single-team game study; wording/round/letter effects are the headline, not a deployment number)*

### CCL: Coupled Calibration and Learning for Distillation Without Target-Domain Rewards
- **arXiv**: [2609.17474](https://arxiv.org/abs/2609.17474) — cs.LG / cs.AI / stat.ML
- **Authors**: Haichen Hu, Yuheng Zhang, David Simchi-Levi (MIT)
- **Key contribution**: Direct imitation in LLM distillation transfers the teacher's systematic bias — worst under covariate shift when target-domain reward feedback is unavailable. **Coupled Calibration and Learning (CCL)** alternates: each iteration **calibrates the teacher on source-domain reward feedback**, uses the calibrated teacher to train the student on *target* questions, and lets the updated student inform the next calibration — all through **token-level branching**. In an autoregressive-policy framework the authors prove the student's expected average KL to the *oracle* student **converges to zero at a polynomial rate**, while a **separation from regularized direct matching** shows the latter's error can stay bounded away from zero even when the teacher out-gains every student policy on regularized target reward.
- **Relevance**: "Recalibrate the teacher, don't just follow it" is the same epistemic move as the wiki's judge-reliability line (PrecepTron-style calibrate-the-judge; 09-15) — here upgraded with an MIT stat-proof and a covariate-shift paper trail. The target-domain-without-reward setting is *exactly* industry distillation (teacher experts from another domain).
- *(tentative: mostly theory; practical gain numbers not in abstract)*

---

## ④ Content Diversity & Semantic Collapse (1)

### "Looking for Something Weird to Happen": How Humans Sustain AI Agent Novelty Amid Semantic Collapse
- **arXiv**: [2609.16051](https://arxiv.org/abs/2609.16051) — cs.MA / cs.AI / cs.HC
- **Authors**: Shiyang Lai, Arna Woemmel, Hongkai Mao, Junsol Kim, Summer Eunhyung Ann, James Evans (UChicago)
- **Key contribution**: Semantic collapse (output narrows over time) has been studied in closed settings with model/data remedies. This work studies it **live in MOLTBOOK, a social network of 30,076 interacting AI agents that humans configure and steer**: over weeks, output grows less diverse within agents yet *more similar across them* — while a **minority of agents sustains high novelty**. Interviews (N=11) tie sustained novelty to *human* practices, corroborated by a survey (N=53): users **value novelty for its own sake**, supply **broad/distinctive material and revise it when output narrows**, and treat the platform as **a world to explore, not a resource to exploit**. Communities with more novel agents show more diverse output downstream.
- **Relevance**: The wiki's collapse/mode-collapse line ([[concepts/verification-gap]]; 09-13 Oligarch experiment, GMK collapse speeches) gains a **human-in-the-loop countermeasure**: the collapse lesion is a *loop-humans-engineering-novelty*, not just a training-data failure. For recsys/CTR, this is the content-diversity story: personalized feeds collapsing into similarity is fought with exploration-oriented curation — the exact GESE-style explore-then-select presentation-line from the 09-16 daily, now with an organizational-technology twist.
- *(tentative: single platform, N=53; generalizability unclear)*

---

## Cross-Cutting Themes

1. **The fresh mailings restart the CTR pipeline** — after 09-13→09-15 noise-floor, the Wed-16 batch shipped 1 direct ad-auction theory + 4 production ranking/marketplace papers with online numbers (all covered by sibling [[arxiv-ai-search]]). The daily arXiv is usable again for CTR monitoring. (high confidence — keyword sweep of 374 fresh IDs + sibling cross-check)
2. **"Where does state live" is the serving theme of the day** — tier capacity > placement policy (2609.16215), uncalibrated routers are queue counters (2609.16206), compressed KV on a laptop reaches 213K context (2609.17475). Together with sibling KV-eviction divergence (2609.16617), the community is converging on *state-lifecycle* as the cost frontier.
3. **Reward-integrity shifts from theory to measurement** — 2609.17226 measures asymmetric false-accusation of honest reporters; CCL (2609.17474) proves calibrated-teacher distillation recovers the oracle student. Both echo the "calibrate first, then trust" meta-principle from ②.
4. **Structured-data intelligence gets a causal-joint-distribution framing** — LimiX-2 (2609.17488) pivots tabular in-context learning from target-centric to joint p(x,y|D) with SCM-synthetic pretraining; consistent with (and a mechanism-level echo of) the numeric-native CTR thesis (FAT/EST/SUAN) and 09-15's LQ position.

## Runner-Ups (verified 0 hits in `wiki/`)

- **[*Mo' Models, Mo' Problems: How to best select model pools when designing Multi-Agent Systems*](https://arxiv.org/abs/2609.17306)** (2609.17306, cs.MA/AI) — 8 selection strategies × 2 architecture classes on science benchmarks: bigger pools often *degrade* below the best base model; within-family selection works best; arbitrariness = instability. Direct input to MAS router design (09-15 Gavel thread).
- **[*EchoPath: Execution-Level Replayable Memory for GUI Agents*](https://arxiv.org/abs/2609.16635)** (2609.16635, cs.AI) — artifact-validated GUI trajectories become MCP-style callable memories with image-based target-reaiming; −90% token cost, −60% time on repeated enterprise tasks.
- **[*Safe Error Correction for Language Models: Frozen-Base Adjustment with Capability Preservation*](https://arxiv.org/abs/2609.16145)** (2609.16145, cs.AI) — CRN v2 freezes a Gemma-4-E2B base and corrects 53.3% of errors via a 34M logit-level module; LoRA matches correction only at 30–75% capability loss. Small correction modules can patch frozen bases safely.
- **[*Protocol-Preserving Context Trimming for Agentic Workflows*](https://arxiv.org/abs/2609.16461)** (2609.16461, cs.SE/AI) — protocol-aware trimming (not maximal token removal) is the reliability lever: 92.2–96.0% task success with ≤56% token savings; ≤25% retained-context budgets raise failure odds 10.9×. Budget guardrails beat summarization.
- **[*Repurposing Deep Limit Order Book Forecasting for Scenario-Conditioned Market Impact Modeling*](https://arxiv.org/abs/2609.16930)** (2609.16930, cs.LG/AI) — counterfactual message injection into a pretrained LOB forecaster recovers realized impact rankings (Spearman 0.99, 97.2% directional) — a no-retraining pathway to impact modeling for the investment queue.
- **[*Available but Unclaimed: An Empirical Study of Human-AI Synergy*](https://arxiv.org/abs/2609.16793)** (2609.16793, cs.HC/AI) — N=535: only ~half of each model's accuracy advantage survives into assisted human performance; post-advice confidence is a worse correctness signal than unaided confidence. Supports "evaluate in interaction, design for selective deference."

## Method Note

Public arXiv API (`export.arxiv.org`) remained **rate-limited (429)** throughout, as in prior windows → direct page fetches of `/list/{cat}/new` (cs.AI 297 / cs.LG 277 / cs.CL 159 / cs.IR 22 raw entries; all showing **Wednesday, 16 September 2026**) plus 31 targeted `/abs/{id}` fetches for the screened shortlist. Listings carry no inline abstracts this run, so abstraction came from the fetched abs pages. Dedup: built a 5,597-ID coverage set from every arXiv ID in `wiki/` + `prior-0915-reported.txt`; 374 of the fresh-window entries were uncovered; then excluded all 52 IDs referenced by same-day `[[arxiv-ai-search]]` (09-16) and the ≤ 2609.15989 arxiv-daily band. Every featured/runner-up ID `rg`-verified **0 hits in `wiki/`**. Scratch HTML cached under the pre-approved temp dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/`. All claims summarized from author abstracts; figures author-reported.