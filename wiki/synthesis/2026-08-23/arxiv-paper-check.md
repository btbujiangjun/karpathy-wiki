---
title: "arXiv Paper Check — AI & CTR (August 23, 2026)"
type: synthesis
created: 2026-08-23
updated: 2026-08-23
sources: []
tags: [arxiv, daily-check, ai, ctr, ir, search-corpus, quantization, agents, skills, memory, benchmark-validity, alignment, security, catch-up, daily-digest]
---

# arXiv Paper Check — AI & CTR (August 23, 2026)

**Weekend note**: Sunday run — arXiv announces nothing Sat/Sun, and the API shows zero cs.AI/cs.IR submissions dated Aug 21–23 as of ~02:20 UTC (last announcement = Fri Aug 21, covering the Thu Aug 20 wave). This issue is therefore a **catch-up sweep** over the Aug 18–20 submission waves, restricted to papers *not* claimed by any prior digest (08-19/08-20/08-21 dailies + the two 08-22 siblings). All 9 arXiv IDs below were grep-verified absent (0 hits) from the entire wiki.

**CTR status**: no genuinely new CTR/recommendation papers this window — every candidate (ERASE, SSR-GRPO, CoRRe, RecPFN, seq-rec probes, SCoRD, rEDMRec, SIDScope, TTP, GateDiffInt, Google AI-Search publisher-CTR RCT) was already captured by sibling digests of 08-20 through 08-22.

---

## ① Search / IR Infrastructure (2)

### Projecting BrowseComp-Plus onto ClimbMix: Toward More Realistic Corpora for Agentic Search
- **Authors**: Sahel Sharifymoghaddam, Lingwei Gu, Yijun Ge, Jimmy Lin (Waterloo / Castorini)
- **arXiv**: [2608.20317](https://arxiv.org/abs/2608.20317) — cs.IR
- **Key contribution**: BrowseComp-Plus's fixed 100K-doc corpus was assembled from each query's own supporting documents plus mined hard negatives — evidence and distractors were both selected per-query. The projection pipeline relocates evidence into ClimbMix (NVIDIA's 400B-token, 553M-doc pretraining mix built with zero benchmark awareness): questions decompose into atomic reasoning hops, each hop re-grounded in the new corpus, retained only when automatic verification + an independent agent + human review all confirm support. Of 830 test questions only 57 fully survive. Effect: strongest agent loses ~5 pts answer accuracy while evidence recall collapses **84.3% → 21.4%** with 63% more search calls.
- **Why it matters**: ⚠️ Benchmark-validity alarm #1 this week — agentic-search results on benchmark-derived corpora systematically overstate retrieval quality. The dataset-agnostic projection pipeline is reusable on any decomposable benchmark.

### Quantization Beyond Uniform Bit Allocation
- **Authors**: K. S. Sreeramji, Sabyasachi Basu, Ravishankar Krishnaswamy, Kirankumar Shiragur, Yujia Wang
- **arXiv**: [2608.19388](https://arxiv.org/abs/2608.19388) — cs.IR, cs.DB · VLDB 2026 VecDB Workshop
- **Key contribution**: Existing PQ/SQ schemes allocate bits uniformly across embedding dimensions, ignoring geometric structure. Partitioning an embedding into contiguous buckets with greedy non-uniform allocation beats uniform baselines at identical storage budgets — up to **+8% recall (PQ)** and **+18% recall (SQ)** in the low-bit regime, where uniform allocation wastes bits on low-variance dimensions of Matryoshka (MRL) embeddings.
- **Why it matters**: Free retrieval accuracy at fixed memory for the embedding-heavy stacks this wiki tracks ([[dimensionality-barrier-retrieval]]); structure-aware compression is a cheap add-on to any MRL-trained production encoder.

---

## ② Agents, Skills & Memory (4)

### AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement
- **Authors**: Yizhe Chi, Wenyi Li, Deyao Hong, Xiaoqiu Wang, Mingju Gao, Kaisen Yang, Bingxiang He, Youjie Zheng, Calvin Xiao, Qinhuai Na
- **arXiv**: [2608.20318](https://arxiv.org/abs/2608.20318) — cs.AI, cs.CL, cs.LG
- **Key contribution**: First benchmark isolating whether agents can design **training algorithms** (not collect data or tune hyperparameters): 10 frozen research repos × 10 algorithm families; agent gets 4h on one B300 to rewrite the training code, which is then rerun from scratch ≤12h and scored by a hidden evaluator against the shipped algorithm on a common scale (0 = uninformative model, 0.1 = shipped algo, 1.0 = task optimum). Across 29 configs of 6 systems: mean score **0.166**, best **0.250** — even the strongest closes under a fifth of the distance to optimum. Most submissions never change how the model learns; the minority that do average 0.226 vs 0.126. More reasoning effort mostly buys the *willingness* to modify learning (8% → 64% of submissions).
- **Why it matters**: Turns the vague RSI debate into a measurable quantity. Pairs with yesterday's Phantom Gains audit ([2608.20290](https://arxiv.org/abs/2608.20290), in the [08-21 report](../2026-08-21/arxiv-paper-check.md)): current self-improvement claims are weak *and* often measurement artifacts.

### Inducing Task Models from Computer-Use Traces (TMI)
- **Authors**: Yucheng Jiang, Zora Zhiruo Wang, Ruishi Chen, Diyi Yang
- **arXiv**: [2608.20319](https://arxiv.org/abs/2608.20319) — cs.CL, cs.AI
- **Key contribution**: Passively recorded screenshots + mouse/keyboard traces are latent task models waiting to be extracted — but real work is multi-threaded with interleaved goals. TMI discovers latent tasks in unconstrained traces (0.974 agreement vs ground-truth groupings) and induces per-task models pairing a hierarchical objective model (recursive goal decomposition) with a procedure model (execution control flow), reconstructing 74.9% of observed steps. Extrinsically, skills derived from TMI task models improve held-out task accuracy by **+30%** over the strongest workflow-induction baseline.
- **Why it matters**: Auditable, symbolic procedural knowledge as a reusable artifact — the supply side for the agent-skill line ([[skillopt-agent-skills]]) and a natural fit for Karpathy-style "teams of agents" workflows.

### Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection
- **Authors**: Atsuyuki Miyai, Kiyoharu Aizawa, Toshihiko Yamasaki (UTokyo)
- **arXiv**: [2608.20169](https://arxiv.org/abs/2608.20169) — cs.CL, cs.AI, cs.LG
- **Key contribution**: Harness optimization (iteratively rewriting agent scaffolding code against validation performance) wastes budget re-evaluating tasks that stopped discriminating between harness variants. Task-CoEvolve co-evolves the validation set with the harness: variance-weighted sampling concentrates evaluation on tasks near the agent's capability frontier, importance-weighted estimates keep full-set scores comparable across iterations. Matches full-set search final performance on online text classification and Terminal-Bench 2.1 with **80% fewer evaluations**.
- **Why it matters**: Makes harness-level self-improvement economically tractable — evaluation cost, not rewrite cost, is the bottleneck in scaffold search.

### MemTrapBench: Benchmarking Cognitive Traps in LLM Memory Use
- **Authors**: Mengru Wang, Haozhe Luo, Zhenqian Xu, Zhixiang Cui, Haoming Xu, Qu Yang, Jizhan Fang, Junfeng Fang, Ningyu Zhang
- **arXiv**: [2608.20202](https://arxiv.org/abs/2608.20202) — cs.AI, cs.CL, cs.CY, cs.DB, cs.LG · work in progress
- **Key contribution**: Memory benchmarks test storage/retrieval; this one tests how retrieved memories **reshape reasoning**. Two failure modes — Reasoning Fixation and Belief Distortion — show that faithfully recorded, semantically relevant memories can still corrupt current-task performance. Across two model families and five memory frameworks, **every evaluated strategy underperforms the no-memory setting**, drops >10% for the strongest. AdaptiveMem (inference-time instruction to avoid memory traps) mitigates damage while preserving standard-benchmark scores.
- **Why it matters**: Second memory-harm paper in 48h (cf. StateMemBench's stale-state failures, same 08-21 report) — together they argue memory systems need reasoning-safety guarantees, not just recall. Directly relevant to [[mem1-agent]]-style designs.

---

## ③ Training, Alignment & Security (3)

### Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge Internalization (IAR)
- **Authors**: Qian Kou, Xiaofeng Shi, Xiaosong Qiu, Hua Zhou
- **arXiv**: [2608.20281](https://arxiv.org/abs/2608.20281) — cs.CL, cs.AI
- **Key contribution**: Converting a fixed document corpus into parametric knowledge without runtime retrieval usually wrecks general ability via naive continued pretraining. IAR separates concerns into three stages: **Inject** (continuation/rewrite/instruction-conditioned reconstruction objectives over source docs) → **Align** (answer-only QA supervision) → **Recover** (merge domain-adapted model back with base instruction model). Across CC/CCI datasets and Llama/Phi/Qwen/SmolLM families: wins 7 of 8 dataset-model settings vs Vanilla SFT, averaging **+3.6pp domain QA** and **+12.1pp general performance** (IFEval/MMLU/MSBench).
- **Why it matters**: A clean recipe for the "personal corpus in weights" vision behind this very wiki's BYOAI thread — internalize the docs, keep the general model.

### Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking (ThermoDPO)
- **Authors**: Yansen Han, Shengyi Liao, Yuanxing Zhang, Pengfei Wan, Tao Lin
- **arXiv**: [2608.20011](https://arxiv.org/abs/2608.20011) — cs.AI, cs.CV
- **Key contribution**: Formalizes why reward-driven preference updates on flow-matching generative models cause reward hacking: updates modify transport trajectories with nothing constraining samples to the pretrained data manifold ("manifold drift") — any terminal displacement with nonzero normal component leaves the support. ThermoDPO anchors pairwise preference optimization on preferred samples with a temperature-controlled objective spanning rejection-sampling FT and FlowDPO; ThermoDPO-weighted reaches StrictScore 0.899 vs 0.629 for FlowDPO, and on SD3.5-M improves OCR +47.5% and avg metrics +16.0%.
- **Why it matters**: Gives the reward-hacking discussion (so far dominated by RLVR/text) a precise geometric mechanism on the diffusion side — anchoring to preferred samples ≈ staying on-manifold.

### EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models
- **Authors**: Yiting Qu, Ziqing Yang, Chi Cui, Ye Leng, Junjie Chu, Yang Zhang
- **arXiv**: [2608.20055](https://arxiv.org/abs/2608.20055) — cs.CR, cs.AI
- **Key contribution**: Identifies a previously overlooked **reasoning-replay surface between tool calls** and builds a multi-step attack that iteratively extracts hidden CoTs using API-returned fidelity signals, plus an LLM-based optimizer searching for universal injection trajectories. Up to **66.4% near-verbatim extraction** on open-source LRMs (≥90% exact token match, length within 10%); trajectories generalize to unseen datasets at up to 80%. On frontier proprietary LRMs, substantial fractions align with provider-reported reasoning lengths; on Gemini-2.5 it extracts a 33,463-token trace matching a 32,948-token target.
- **Why it matters**: Hidden CoT is treated as a protected asset by major providers — this establishes extraction as a practical security risk and gives labs a concrete red-team target (the tool-call boundary).

---

## Cross-Cutting Themes

1. **Self-improvement gets its measurement discipline**: AI4AI-Bench (can agents design learners? barely) + Task-CoEvolve (make the eval loop affordable) complete, with Saturday's Phantom Gains, a coherent arc: capability claims → controls → cost engineering.
2. **Procedural knowledge becomes an artifact class**: TMI (induce auditable task models from raw computer-use traces) and Task-CoEvolve (harness-as-optimizable-code) push toward skills/scaffolds as first-class, inspectable objects — echoing [[skillopt-agent-skills]].
3. **Memory can hurt**: MemTrapBench joins StateMemBench in showing faithful memory still degrades reasoning (fixation/belief distortion; stale state). Memory design needs adversarial evaluation.
4. **Benchmark realism audits continue**: BrowseComp-Plus→ClimbMix projection shows evidence-recall collapsing 84%→21% once corpora aren't reverse-engineered from the benchmark itself — third benchmark-validity alarm this week alongside seq-rec probes and Phantom Gains.
5. **Reasoning assets under attack**: EchoCoT's tool-call replay surface is a concrete threat model for the CoT-hiding practices every frontier lab now ships.

---

## Method Note

Queries: arXiv API `cat:cs.AI` and `cat:cs.IR` with `submittedDate:[202608180000–202608240000]` sorted descending (~145 unique candidates screened), plus a keyword sweep (`"click-through rate"` OR `"CTR prediction"`). Dedup: every reported ID grep-verified against all wiki pages; exclusions listed above with their claiming digests. Weekend schedule means the next fresh announcement window is Mon Aug 24 (covering Fri Aug 21 submissions).
