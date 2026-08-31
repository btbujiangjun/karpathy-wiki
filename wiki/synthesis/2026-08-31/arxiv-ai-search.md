---
title: "arXiv AI/LLM/RecSys/Advertising Paper Search (2026-08-31)"
type: synthesis
created: 2026-08-31
updated: 2026-08-31
sources: []
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, agents, ml-systems, inference, efficiency, retrieval, world-models, game-balance, creative-generation, daily-digest]
---

# arXiv Recent Papers — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

> Search date: 2026-08-31 (Monday) · Scope: papers **not yet covered anywhere in the wiki** (every arXiv ID below grep-verified absent from `wiki/` and not claimed by the same-day [arxiv-daily](arxiv-daily.md)). **Fresh Monday 31 Aug 2026 mailing** — IDs `2608.27460–2608.28589` (top listed ID ~2608.28589 in cs.LG). 718 unique IDs parsed across 14 categories (cs.AI/LG/CL/IR/GT/MA/CV/SE/NE/SY + stat.ML/cs.HC/econ.GN/cs.CY); 423 in-wave fresh candidates vs the wiki's known-ID set; **19 featured + 5 honorable mentions** below, all verified-new. The same-day `arxiv-daily` absorbed the 13 most-cited rec/ads/OPD/world-model papers of this wave (HubMixer, incentivized-ad RL, GRPO autobidders, survival models, RA-OPD/VISTA/SpikeOPD, PLVR, WM-R1, chess, ITER) — this report is the **complementary deeper pass** over the same wave for the under-covered middle/long tail.
>
> Method: **direct arXiv access worked this session** (unlike 08-30's blocked environment). Listings fetched via `arxiv.org/list/{category}/new` (Monday 31 Aug 2026 mailing) with curl; per-paper metadata pulled live from `arxiv.org/abs/...`; affiliations recovered from HTML full-text front matter where present. Affiliations marked *(stated)* come from paper front matter; *(inferred)* = deduced from author identities (websites, GitHub, prior papers); otherwise "not stated". Temp files under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/`, to be cleaned up after this report lands.
>
> Dedup boundary: prior digests (08-27 → 08-30) covered the Fri Aug 28 mailing up to **2608.27455**; the 08-31 `arxiv-daily` covers the featured 13 + 5 HMs of `2608.27460–28589`. Every ID below is outside both sets.

---

## ① Recommendation, IR & Search (4)

### 1.1 SG-UMP: Sequence-Guided Universal Multimodal Prioritization Calculation Framework

| Field | Detail |
|-------|--------|
| **Authors** | Xinyi Zhang, Yutong Li, Peijie Sun |
| **Institution** | Imperial College London / University College London / Nanjing University of Posts and Telecommunications *(stated in HTML front matter)* · **MM 2026 Full Paper** |
| **Abstract** | Multimodal sequential recommendation (MSR) improves recommendation by fusing text, images, and user interactions, but existing MSR methods fail to capture **user-level preference heterogeneity** and **dataset-level modality bias**, limiting cross-user / cross-dataset adaptability. SG-UMP is a plug-and-play plugin that won't retrain the backbone: a **Module Combiner** enables flexible multimodal processing and a **Module Router** produces dynamic module ordering, so that both user preferences and dataset characteristics adapt at runtime. |
| **Key innovations** | Plug-and-play MSR enhancement (no backbone retraining); module-ordering as a *learned* decision (dynamic routing, not fusion-only); explicitly targets the two failure modes most rec papers ignore — per-user modality preference and per-dataset modality bias. |
| **arXiv** | [2608.28503](https://arxiv.org/abs/2608.28503) · cs.IR (28 Aug 2026) |
| **Why it matters** | MSR has been a supply-side story (keep adding modalities); SG-UMP flips to the demand side (which module order fits *this user / this dataset*). Directly extends the wiki's multimodal-rec thread ([AMUR, 08-31 daily](arxiv-daily.md)) — both are "selectivity over fusion" bets. |

### 1.2 TiGER: A Versioned Unified Graph Index for Dynamic Timestamp-Aware Nearest Neighbor Search

| Field | Detail |
|-------|--------|
| **Authors** | Jun Woo Chung, Weijie Zhao |
| **Institution** | Rochester Institute of Technology, NY, USA *(stated)* |
| **Abstract** | Real-world vector datasets evolve over time; queries often target a *time window* (e.g., "similar to items from last 30 days"). Standard ANN indexes either query the whole dataset then filter (wastes work on invalid vectors) or build a separate sub-graph per time segment (storage/complexity blow-up). **TiGER** builds **one unified graph with integrated versioned connectivity**, letting an arbitrary time interval be queried directly without post-search filtering, merging, or per-segment graphs. |
| **Key innovations** | Unifies time-aware ANN into a single versioned graph (no segment partitioning); arbitrary-interval queries traverse only valid vectors; up to ~5× QPS vs. filtering / per-segment baselines at equal accuracy. |
| **arXiv** | [2608.27663](https://arxiv.org/abs/2608.27663) · cs.IR (27 Aug 2026) |
| **Why it matters** | Timestamp-awareness is the silent requirement of real rec/ad serving (freshness beats raw similarity). TiGER is a clean infra-side answer for the wiki's retrieval/rec-engineering thread — cf. misi's index-engineering angle ([08-30 arxiv-ai-search](../2026-08-30/arxiv-ai-search.md#31-misi-a-metric-inverted-sample-index)). |

### 1.3 Beyond the Vacuum: Combinatorial Strategy Selection for Competitor-Aware Generative Engine Optimization

| Field | Detail |
|-------|--------|
| **Authors** | Vaibhav Sourirajan, Yao Zhang, Himanshu Kumar, Sahil Wadhwa, Mann Patel, Amirfarrokh Iranitalab |
| **Institution** | Capital One, AI Foundations *(stated)* |
| **Abstract** | Generative Engine Optimization (GEO) rewrites content to appear in LLM answers. Prior GEO works pick rewriting strategies *in isolation*, ignoring a key externality: **as more competing content gets optimized, the optimal strategy changes** (GEO is a competitive game, not a vacuum). The authors formalize competitor-aware GEO as a combinatorial strategy-selection problem: **(1)** Bayesian Optimization of Combinatorial Structures (BOCS) searches the strategy-combination space efficiently; **(2)** preference pairs + grounded reasoning traces mined from BOCS observations fine-tune an LLM to reason over a document corpus and propose optimal combinations. |
| **Key innovations** | Framing GEO as an interaction/competition problem (strategies are substitutes/complements); BOCS-to-LLM distillation loop (black-box search → interpretable policy); SOTA over existing agentic and single-heuristic GEO on geo-bench and a synthetic competitive variant `geo-bench_comp`, plus transfer to out-of-distribution datasets. |
| **arXiv** | [2608.27631](https://arxiv.org/abs/2608.27631) · cs.IR (27 Aug 2026) |
| **Why it matters** | Red-fields a domain the wiki hasn't tracked (GEO), and does it with an "optimize under competition" lens that mirrors auction/CTR thinking — for rec/ad practitioners, GEO is the sponsored-search of the LLM-output frontier. |

### 1.4 GeBDA: Building Damage Assessment as Text-Based Sequence Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Olivier Dietrich, Krishna Sapkota, Konrad Schindler, Genady Beryozkin |
| **Institution** | (stated byline: Schindler — ETH Zürich IGP; not confirmed for the full author set) |
| **Abstract** | Building damage assessment (BDA) from satellite imagery is usually trained as a per-image classification/segmentation task, treating each image independently. **GeBDA reformulates it as text-based sequence prediction**: satellite images are tokenized, and damage is predicted autoregressively over a mixed sequence of image + label tokens — i.e., a generative sequence model over visual damage "language". This lets the model use neighborhood context (building interiors, block-level patterns) and one generative pipeline replace the classic segmentation→decision stack. |
| **Key innovations** | Damage assessment as sequence prediction over tokenized satellite imagery (neighborhood context flows through token context); generative unified model instead of per-image classifiers; new lens on how "sequential modeling" transfers from text/video to structured EO tasks. |
| **arXiv** | [2608.28567](https://arxiv.org/abs/2608.28567) · cs.CV (28 Aug 2026) |
| **Why it matters** | A refreshing example of *sequence-modeling-as-general-substrate*: the same "tokenize the input, predict the label autoregressively" recipe the wiki tracks in rec/creative/video applied to disaster-response imagery. Bridges the wiki's sequential-modeling and multimodal-generation tracks. |

---

## ② Advertising, Creative & E-Commerce (2)

### 2.1 CommerceVibe: Learning to Design E-Commerce Creatives as Executable Visual Code via Dual-Feedback Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Yajiao Xu, Jin Zhang, Jiangbo Ai, Tao Jiang, Mo Xu, Lina Huang, Chengfu Huo |
| **Institution** | Front matter lists a university + Alibaba Group; Alibaba / Ali-Express advertising-creative group *(inferred: Chengfu Huo is a long-time Alibaba ads/creative algorithm lead; co-authors publish under Alibaba)* |
| **Abstract** | E-commerce creatives from diffusion models are visually attractive but *flat rasters*: distorted text, inconsistent product details, hard to edit or reuse, and hard to supervise for structured design requirements. **CommerceVibe treats creative design as conditional HTML/CSS program synthesis** — the output is renderable, editable, and reusable code, not pixels. Training is a two-step recipe: SFT of **Qwen3.5-9B on 28K+ e-commerce examples**, then **dual-feedback RL**: rule-based feedback checks rendered programs for text readability, product visibility, layout validity, while a VLM scores the rendered creative against the spec across six perceptual/commercial dimensions. |
| **Key innovations** | Creative-as-executable-code (HTML/CSS) instead of raster output — editable/reusable by construction; dual-feedback RL (deterministic rules for constraints + VLM preference for perception-dependent quality); expert-validated. On a 1,300-case benchmark the RL model hits **94.0/100** (vs. 87.3 SFT-only), outperforming strong external models. |
| **arXiv** | [2608.27893](https://arxiv.org/abs/2608.27893) · cs.CV (28 Aug 2026) |
| **Why it matters** | The "structured, verifiable creative output" bet: rec/ads systems increasingly need outputs that are *checks* not vibes (rule feedback = cheap verifiable reward — the wiki's [verifiability](../../concepts/verifiability.md) thread applied to creative generation; cf. CommerceVibe online RL in ①). |

### 2.2 LandingAgent: A Reference-Annotated Dataset and Agentic Generation Framework for Landing Pages

| Field | Detail |
|-------|--------|
| **Authors** | Injun Baek, HyeongSeok Lee, Yearim Kim, Junhoo Lee, Nojun Kwak |
| **Institution** | Seoul National University + Samsung Electronics *(inferred: Kwak's group is SNU AI; Samsung Electronics listed in front matter)* |
| **Abstract** | Landing pages must communicate a target-specific value proposition while organizing information flow, visual hierarchy, and CTAs. Direct LLM generation yields generic templates and unsupported persuasive claims. **LandingBench** abstracts real landing pages into section sequences, layout patterns, tone descriptors, visual emphasis, and CTA structure (reference profiles). **LandingAgent** then runs a three-phase agentic loop: profile the target → construct a reference-guided wireframe → refine with critique-guided polishing. |
| **Key innovations** | Reference-profile dataset built from real pages (patterns, not copy); target-grounded, reference-guided generation preventing unsupported claims; agentic profile→wireframe→critique-refine pipeline; measurable gains in target grounding, presentation quality, and layout diversity. |
| **arXiv** | [2608.27902](https://arxiv.org/abs/2608.27902) · cs.CL/cs.AI (28 Aug 2026) |
| **Why it matters** | The creative/ads side of agentic generation the wiki tracks ([vibe-coding](../../concepts/vibe-coding.md)); LandingAgent's "reference-profiling before generation" is a concrete pattern for *grounded* ad creatives vs. hallucinated copy. |

---

## ③ LLM Decoding, Inference & Efficiency (3)

### 3.1 Trajectory-Level Speculative Decoding for Diffusion Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Tianxiang Pan, Baitao Gong, Mo Guang, Hongwei Yong, Tianpeng Jiang, Yaqian Li, Zheng Cao, Kaiwen Long |
| **Institution** | Li Auto Inc., Shanghai, China *(stated — all 8 authors)* |
| **Abstract** | Diffusion LMs (dLLMs) generate tokens in parallel via iterative denoising, but existing decoding collapses to single-token generation under low confidence — killing throughput. Speculative decoding for autoregressive LMs operates on left-to-right token sequences; dLLMs instead require **speculating over denoising trajectories** (sequences of multi-token updates with explicit positions and unmasking orders). The authors build a trajectory-level speculative framework: confidence-stratified tree exploration builds draft trajectories, blockwise parallel evaluation verifies them with bidirectional attention masks, and **inter-block speculation** exploits the bidirectional structure for cross-block lookahead. They formalize when the approach is exact and isolate **trajectory drift** as the cost of parallelism. |
| **Key innovations** | First speculative-decoding treatment that operates over denoising *trajectories* not token strings; inter-block (cross-position) speculation unique to bidirectional models; exactness characterization; built on Fast-dLLM's dual-cache infra: **30–40% fewer denoising iterations, 2.6→4.3 tokens/step, 7–14× over vanilla dLLMs / 1.3× over Fast-dLLM** with <1% accuracy change on reasoning + code. |
| **arXiv** | [2608.27514](https://arxiv.org/abs/2608.27514) · cs.CL/cs.AI (27 Aug 2026) |
| **Why it matters** | The parallel-generation efficiency frontier of the wiki's LLM-serving track: if dLLMs are to compete with autoregressive decoders, decoding-side speculation (not just weights) is where throughput is won. |

### 3.2 Thinking Costs Tokens: When More Structure is Worth the Price

| Field | Detail |
|-------|--------|
| **Authors** | Thomas Nolasque, John Grey, Calista Pham, Ankit Vani |
| **Institution** | Royal Bank of Canada (RBC) *(stated)* |
| **Abstract** | Adding inference structure (planning, verification, repair) to an LLM consumes the very token budget it is meant to use well. Is there a **token-budget crossover** below which structured overhead *hurts* and above which it *helps*? On FinQA and TAT-QA financial reasoning with GPT-5.4 mini across **14 budget tiers (250 → 42,000 output-equivalent tokens)**, they compare a single-call monolith vs. a verified-search architecture (planning + label-blind checking + repair). At 1,000 tokens the monolith reaches 18% while verified search scores ~0% (overhead eats the answer budget); from ~1,500 tokens on, verified search overtakes and holds a margin (~44% vs. ~40% at top tiers). Crossover confirmed by strict intersection-union test (p ≤ 0.001). |
| **Key innovations** | First clean *budget-curve* characterization of reasoning structure (not just "verified search better"); shows planning/verification has a *negative* regime below threshold — an inverse of the "reasoning tax" narrative; rigorous crossover test. |
| **arXiv** | [2608.27506](https://arxiv.org/abs/2608.27506) · cs.AI (27 Aug 2026) |
| **Why it matters** | Direct evidence for the wiki's [galaxy-brain-reasoning](../../concepts/galaxy-brain-reasoning.md) / budget-aware reasoning interest: overhead ≠ free, and the "reason more" intuition has a measurable floor. Balances 08-25's Reasoning-Tax work from the opposite direction. |

### 3.3 Characterization of Request and Token Energy Costs for LLM Inference Workloads on GPU Platforms

| Field | Detail |
|-------|--------|
| **Authors** | Prabhu Vellaisamy, Vanessa Lam, Shawn Blanton, John Paul Shen |
| **Institution** | Carnegie Mellon University (Electrical & Computer Engineering) *(stated)* · **IISWC 2026** |
| **Abstract** | LLM serving is priced by tokens, but GPUs burn energy over inference *windows* — an accounting mismatch that makes token-normalized metrics misleading (average output-token energy can fall even as total request energy rises). The authors propose a **decomposed energy model**: fixed one-time prefill + fixed generation setup cost, plus per-output-token marginal step energy. Measured on H100/H200 across dense and MoE models, varying model/phase/batch/context/output length. Example: Llama-3.2-1B on H200 batch-16 ctx-4K — raising output length 10→512 tokens drops token energy 7.46→0.72 J/token while *total* window energy rises 1.19→5.93 kJ; batching gains are context-bounded (batch-16 vs 1 shrinks from 6.31× at ctx-512 to 1.17× at ctx-4K); MoE amplifies fixed-cost effects at low concurrency. |
| **Key innovations** | Explicit request-vs-token energy decomposition (setup + marginal); first dense-vs-MoE token-energy gap characterization across H100/H200; actionable guidance: energy-aware serving must jointly optimize both metrics. |
| **arXiv** | [2608.28044](https://arxiv.org/abs/2608.28044) · cs.PF/cs.DC/cs.LG (28 Aug 2026) |
| **Why it matters** | Grounds the wiki's inference-efficiency thread in *measured energy*, not just latency/KV — batching and MoE's power profile are exactly the lever rec/ad serving stacks care about. |

---

## ④ Sequential Modeling & Attention (2)

### 4.1 The Approximation Rank of Softmax Attention: Sharp Geometric Laws and Robust Interaction Dimension

| Field | Detail |
|-------|--------|
| **Authors** | Yuhe Sui, Jianing Zhang |
| **Institution** | Nanyang Technological University (Sui) + Carnegie Mellon University (Zhang) *(stated)* |
| **Abstract** | Which geometry controls the minimum rank of the softmax-attention operator needed to preserve all bounded vector-valued outputs? The paper studies the **maximum-row-ℓ₁ approximation rank** and derives two sharp worst-case laws: spherical self-attention has rank Θ(min{n,(1+β)^((d−1)/2)}); full-ball geometry adds a radial degree and, for large β, gives Θ(β^(d/2)). Per-head, row-softmax "quotients out" row-scalar logit directions, leaving a visible query–key interaction dimension r with an r/2 per-instance upper law that is minimax sharp; approximate interaction subspaces yield an explicit residual-error trade-off and a tolerance-indexed SVD dimension. |
| **Key innovations** | First sharp rank laws separating *support geometry* (worst-case temperature scaling) from *softmax-visible interaction geometry* (per-head complexity); minimax-tight r/2 exponent; calibration on 84-head BERT-base shows modest effective-dimension reductions with positive links to rank certificates. |
| **arXiv** | [2608.28150](https://arxiv.org/abs/2608.28150) · cs.LG/cs.AI (28 Aug 2026) |
| **Why it matters** | Feeds the wiki's attention/sequence-modeling theory track with *provable* capacity bounds — the rank of attention with finite support geometry is a lever for both expressivity and linear-attention-style compression arguments tracked since the attention-is-all-you-need era. |

### 4.2 Real-Valued Hyperdimensional Sequence Representations with Hadamard Product Binding and Shift Equivariance

| Field | Detail |
|-------|--------|
| **Authors** | Kenny Schlegel, Dmitri A. Rachkovskij, Denis Kleyko, Amy Loutfi, Stefan Streif, Evgeny Osipov |
| **Institution** | Chemnitz University of Technology / Luleå University of Technology / Örebro University / RISE / Linköping University + Institute of Information Technologies and Systems, Ukraine *(stated)* |
| **Abstract** | Hyperdimensional computing (HDC) encodes sequences via position vectors, classically using Fractional Power Encoding (FPE) with circular-convolution or complex binding — incompatible with the Hadamard-product binding that real-valued HDC prefers. The authors derive three real-valued position encodings from Random Fourier Features: an inverse-FFT baseline, and Sinusoid / Cosine-only variants. The **Sinusoid variant yields an exact algebraic shift operator** — a temporal shift is applied directly to the already-encoded sequence vector without re-encoding. |
| **Key innovations** | Bridges FPE's shift-equivariance to real-valued Hadamard binding (the hardware-friendly HDC path); algebraic shift operator (no re-encode); comparable sequence-classification accuracy to FPE at lower compute. |
| **arXiv** | [2608.28334](https://arxiv.org/abs/2608.28334) · cs.AI (28 Aug 2026) |
| **Why it matters** | A niche but principled addition to the wiki's sequence-representation track: explicit shift-equivariance in *one pass over the encoded sequence* is the kind of property that anchors efficient (linear / HD) sequence machinery. |

---

## ⑤ LLM Post-Training & Distillation Reliability (1)

### 5.1 Below the Noise Floor: Bimodal Seed Collapse and Distinct Failure Modes in Small-Model Knowledge Distillation

| Field | Detail |
|-------|--------|
| **Authors** | Dipto Sumit, Sakib Ul Haque, Farig Sadeque |
| **Institution** | BRAC University, Bangladesh (Dept. of CS & Engineering) *(stated)* |
| **Abstract** | Function routing (pick the right API from a fixed catalog) is where small student models shine — but KD gains are usually reported **single-seed**, where seed variance is invisible. On a 740-instance healthcare API-routing task (1.5B Qwen student, 20B teacher), comparing 8 KD variants with 3–6 seeds each: **(i)** per-seed σ ranges **2.8–48.7 pp** — swallowing every reported gain <5 pp; **(ii)** 3 of 7 KD variants show **bimodal collapse** (≥1 seed in 3–5 lands <55% while others train fine); **(iii)** collapse has *distinct modes* — wrong-function selection for CE variants and a newly documented **output-truncation mode** for `reasoning_kd` (emits reasoning, never prints the function name — 0.9% accuracy); **(iv)** only `progressive_kd` and `rank_kd` avoid collapse (σ ≤ 3.9 pp); **(v)** a naive cross-split +3.78 pp gain *reverses* to −2.70 pp under controlled multi-seed retest. |
| **Key innovations** | First multi-seed KD reliability study in LLM function routing; names bimodal seed collapse and an undocumented output-truncation failure mode; shows single-seed evaluation is structurally blind to central KD failure modes. |
| **arXiv** | [2608.27729](https://arxiv.org/abs/2608.27729) · cs.CL (27 Aug 2026) |
| **Why it matters** | Sharp methodological counterweight to the wiki's OPD/distillation cluster (RA-OPD/VISTA/SpikeOPD today, SOPD/R2-OPD on 08-25): if teacher signals are unreliable, *so is the evaluation's seed count*. Strong rec for adding "multi-seed variance as a reporting requirement" to the wiki's methodology guidance. |

---

## ⑥ Games, Game Balance & Game Agents (4)

### 6.1 Where Does Balance Break? Boundary Discovery for Game Balance Testing under a Finite Simulation Budget

| Field | Detail |
|-------|--------|
| **Authors** | Hiroki Mukai, Yusaku Kato, Norihiro Yoshida, Erina Makihara, Katsuro Inoue |
| **Institution** | Ritsumeikan University, Osaka, Japan *(stated)* · **ASE 2026 Research Track** |
| **Abstract** | Competitive multiplayer games resist classic software testing: non-deterministic executions, huge behavior spaces, and no stable correctness oracle. Balance regressions (one strategy dominating after a small parameter change) only show up across repeated simulations. The authors **recast balance regression testing as boundary discovery under a finite simulation budget**: efficiently find inputs near the boundary between balanced and unbalanced parameter regions. **BBExplorer** combines multi-directional candidate generation, budget-aware two-stage screening, and adaptive step-size shrinkage for boundary refinement. |
| **Key innovations** | New problem formulation (DBD: detect the *boundary*, not a pass/fail oracle); budget-aware two-stage screening under non-determinism; stable boundary behavior across unseen seeds/thresholds; effective in low-dim and degrades gracefully in higher dims. |
| **arXiv** | [2608.28364](https://arxiv.org/abs/2608.28364) · cs.SE (28 Aug 2026) |
| **Why it matters** | The wiki's games track is heavy on self-play/bots; this is the *engineering* side — how to regression-test game balance at all. Pairs naturally with simulated-budget evaluation in [MARL/games resources](../2026-08-14/game-rl-daily.md). |

### 6.2 Refundable Deposits: How to Restore Cooperation in Finitely Repeated Games

| Field | Detail |
|-------|--------|
| **Authors** | Giulio Salizzoni, Domenico Mergoni Cecchelli, Edward Plumb, Maryam Kamgarpour, Galit Ashkenazi-Golan |
| **Institution** | EPFL — SYCAMORE Lab (Lausanne) / London School of Economics (Mathematics) / CUNEF Universidad (Madrid) *(stated)* |
| **Abstract** | Infinitely repeated games support rich Nash/folk-theorem cooperation; *finitely* repeated games shrink to a much smaller, often inefficient equilibrium set (backward induction). The authors enlarge it with **refundable deposits**: each period a player may deposit a refundable sum with a neutral intermediary, returned at game end and forfeited on deviation. Deposits are **voluntary and stage-by-stage incentive-compatible** (no player commitment assumed; only the intermediary commits to a refund rule fixed before play). The mechanism sustains strictly more efficient payoff profiles — demonstrated in the prisoner's dilemma, congestion games, and public goods games (none cooperative under the standard finite formulation), plus a dynamic common-pool resource. |
| **Key innovations** | Mechanism-design route to cooperation in finite repetitions via voluntary, self-financing deposits (a Nash-threat folk theorem with deposits); no transfers between players; optimal-deposit design; works where horizon is *known*, unlike incomplete-information/uncertain-horizon fixes. |
| **arXiv** | [2608.27536](https://arxiv.org/abs/2608.27536) · cs.GT/econ.TH (27 Aug 2026) |
| **Why it matters** | A neat answer to "why can't finite-horizon agents cooperate" relevant to the wiki's game-theory/multi-agent-self-play thread (self-play + finitely repeated agent games are exactly the finite-repetition regime): a clean mechanism for sustaining cooperation in agent societies. |

### 6.3 First Make It Playable, Then Make It Good: Staged Interaction Learning for Small Dialogue-Game Agents

| Field | Detail |
|-------|--------|
| **Authors** | Syed Mahbubul Huq, Pranava Madhyastha |
| **Institution** | City, University of London + The Alan Turing Institute *(stated)* · EMNLP 2026 (LMP Challenge) |
| **Abstract** | Small models for interactive dialogue games (carrying state across turns, mapping feedback→valid actions) need more than static-benchmark finetuning. **Qwen-GuidePlay-2B** finetunes Qwen3.5-2B in three stages: **(a)** SFT on only *successful* game trajectories from Playpen; **(b)** *weighted turn-level* SFT (value-aware per-turn weighting); **(c)** *teacher-guided* SFT — a larger teacher only fixes formatting and evaluates, never fabricates gold actions. Final: **57.12 clemscore / 42.68 statscore** on public Playpen validation; second-highest Playpen clemscore *delta* (+36 over base) among challenge entries. |
| **Key innovations** | Stage ordering matters ("playable before good"): trajectory-imitation builds playability, turn-level/teacher-guidance builds decision quality; "teacher as reviewer, not oracle" constraint; negative results (replay-repair, hard-example mining didn't help) — curation beats aggressive procedural changes for small models. |
| **arXiv** | [2608.27672](https://arxiv.org/abs/2608.27672) · cs.CL/cs.AI (27 Aug 2026) |
| **Why it matters** | Empirically confirms the wiki's small-model dialogue-game thread with a SOTA-competitive recipe, and its "supervise, then let the student drive" ordering matches the [RL is terrible / careful data] lean of the OPD-reliability cluster. |

### 6.4 Acquire, Repair, Preserve: A Diagnosis-Guided Post-Training Recipe for Small-Model Dialogue Game Agents

| Field | Detail |
|-------|--------|
| **Authors** | Nan Li |
| **Institution** | Department of Information and Computing Sciences, Utrecht University, The Netherlands *(stated)* · EMNLP 2026 (LM Playschool Workshop) |
| **Abstract** | Frozen static accurac doesn't transfer to interactive dialogue games: a 2B model must carry state, interpret feedback, and pick valid actions under shifting constraints. Diagnosing the LM Playschool Challenge runs shows failures aren't only broad-knowledge gaps but **local decision failures**: repeated guesses, malformed actions, violations of just-seen feedback. This motivates a three-step post-training recipe: **acquire** broad game participation via SFT; **repair** mechanically verifiable failures *within one dialogue-game family* using turn-local preference pairs; **preserve** general capabilities outside the games. |
| **Key innovations** | Failure *diagnosis* before recipe (not "just SFT better"); turn-local preference pairs for mechanically verifiable failure classes; official final eval: public clemscore 10.67→38.92, closed in-domain 13.41→41.17, static performance preserved (44.14 vs 44.24); honest limits — OOD clemscore stays low (7.88), gains concentrate in-family. |
| **arXiv** | [2608.28458](https://arxiv.org/abs/2608.28458) · cs.CL/cs.LG (28 Aug 2026) |
| **Why it matters** | Complements 6.3 with a *diagnosis-first* recipe and the same core lesson (broad SFT is most of the win; targeted turn-local supervision works only with precise failure detection). The two LMP papers together are the wiki's best evidence base for "post-train small dialogue agents from failures, not just data." |

---

## ⑦ World Models, Physical Grounding & Agent Societies (3)

### 7.1 Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Hanyang Wang, Yimo Cai, Weiliang Chen, Jiawei Chi, Haowen Sun, Qiyu Dai, Yi-Hsin Hung, Xingzhuo Guo, Jinshan Ren, Runmao Yao, Ziwei Liu, Mingsheng Long, Yueqi Duan, Jun Gao, Jiangran Lyu, Fangfu Liu, Jialong Wu |
| **Institution** | MirroS, Tsinghua University, Peking University, Nanyang Technological University *(stated: "Affiliations MirroS, Tsinghua University, Peking University, Nanyang Technological University")* |
| **Abstract** | VLMs recognize and narrate physical scenes but lack explicit representation of underlying mechanisms (object states, physical parameters, governing dynamics) needed to reason about how the world evolves under intervention. **Code-as-World** represents physical worlds as *executable programs*: physical composition, dynamic evolution, and visual appearance all encoded as runnable code. An **agentic discovery loop** (propose → execute → render → verify → refine), inspired by abductive reasoning, builds these worlds from multimodal observations (language or video). A concrete payoff: verified executable worlds generate scalable *physical supervision* for training VLMs on quantitative physical reasoning. |
| **Key innovations** | Executable world representations (code as the substrate for dynamic physics, not latent/neural); abductive agentic discovery loop with *render-and-verify* grounding; Code-as-World-VL sets SOTA on QuantiPhy, surpassing leading proprietary models. |
| **arXiv** | [2608.27549](https://arxiv.org/abs/2608.27549) · cs.CV (27 Aug 2026) |
| **Why it matters** | The strongest recent articulation of the wiki's [world-models] thread as *executable certifiable programs* rather than learned simulators — the same "verifiable-reward / verification-gap" instinct applied to physical reasoning. Pairs with the wiki's Code-World-Model line (2608.25927, 08-28). |

### 7.2 GeoNeXt: Video Generative Models as Geometry Learner

| Field | Detail |
|-------|--------|
| **Authors** | Haosen Yang, Jifei Song, Zhensong Zhang, Xiatian Zhu, Jiankang Deng |
| **Institution** | University of Surrey (Yang, Song, Zhu) + Independent Researcher (Zhang) + Imperial College London (Deng) *(stated)* |
| **Abstract** | Geometry estimation (depth / surface normals) has been "adapt image diffusion to generate the map" — task-specific heads on image backbones, or joint fine-tuning of altered image backbones that needs lots of labeled data. **GeoNeXt** repurposes a pretrained *video generation* model as a unified, data-efficient geometry learner by reformulating estimation as **next-frames prediction** (image ↔ geometry joint modeling). Video models carry structured motion/consistency priors that a frozen image backbone lacks; fine-tuning the video prior yields zero-shot monocular depth + surface normals that beat prior task-specific *and* unified generative competitors with far less data, and rival discriminative SOTA trained on 100× more data. |
| **Key innovations** | First repurposing of *video* generative priors (not image) for geometry via next-frame framing; joint image↔geometry modeling in one frozen-prior framework; order-of-magnitude data efficiency vs. discriminative geometry baselines. |
| **arXiv** | [2608.28549](https://arxiv.org/abs/2608.28549) · cs.CV/cs.AI (28 Aug 2026) |
| **Why it matters** | Modern scalability evidence for "preference-transfer: image→video→geometry": a video-world-model prior as a spatial-geometry learner. Connects the wiki's video-generation and world-model tracks (cf. video-diffusion scaling [08-31 scan: How Far Can 5,500 Hours of Driving Take You?]). |

### 7.3 GOD: Govern, Observe, and Direct — A Real-Time Control Room for Agent Societies

| Field | Detail |
|-------|--------|
| **Authors** | Yige Luo, Ran Guan |
| **Institution** | *(not stated in abs page; see §6 methodology provenance flag)* · **EMNLP 2026 System Demonstrations Track** |
| **Abstract** | Generative-agent societies are easier to start than to inspect: a run holds many agents, locations, messages, commands, and model calls, yet the operator gets either a finished replay or raw logs — making it hard to ask why an agent moved, test a small intervention, or package a run for sharing. **GOD** is a *local-first* control room for agent societies: from one browser workflow an operator issues targeted questions or interventions and inspects the resulting replay state. It combines a setup wizard, Agent Studio, Map Studio, a spatial replay interface, Ask and Intervene commands, and portable experiment/map/agent packs. The technical core is a **command-and-artifact loop**: live controls and replay evidence share the same operator command model, while package contracts separate scenario, map, and profile data from local runtime state. Public release includes hosted Smallville-style and PKU replays, an OSS repository, and downloadable packs. Evaluated on 15 completed run slots: across 14 intervention runs, 78 of 84 target-agent checks recorded the commanded destination, and 169 of 182 state answers matched a saved location/action string. |
| **Key innovations** | An operationalizing of the wiki's agent-societies thread as a *debugger/control-room* (not a training recipe): live→replay unified under a single command model; portable, reproducible agent-run packaging (OSM experiment/map/agent packs). |
| **arXiv** | [2608.27992](https://arxiv.org/abs/2608.27992) · cs.AI/cs.MA (27 Aug 2026) |
| **Why it matters** | Fills a real gap in the wiki's agents thread: *inspectability* of multi-agent runs. Complements Code-as-Worlds' "executable, verifiable world representations" — here the "world" is an agent society and GOD is the verification/debug plane. |

---

## Honorable mentions (scanned, not featured)

| arXiv ID | Title | Category | One-line takeaway |
|----------|-------|----------|-------------------|
| [2608.28399](https://arxiv.org/abs/2608.28399) | RetailAgent: Structured Adverse Timing in Self-Conditioned Multimodal LLM Trading Agents | cs.AI / q-fin.TR | UW–Madison/MSU/Rochester LLM trading agents show *persistent negative timing* (exposure-matched long-vs-flat returns) robust across modality/horizon/model — a behavioral signal that LLM financial policies are predictable to adversaries. |
| [2608.27980](https://arxiv.org/abs/2608.27980) | The Race for Elite Destinations: Education Competition and Low Fertility in Korea | econ.GN / cs.CY | Structural/generative analysis of education competition as a fertility driver in Korea — social-science crossover for the wiki's markets-and-behavior interest. |
| [2608.28008](https://arxiv.org/abs/2608.28008) | Visual Token Coding for Video Multimodal Large Language Models | cs.CV | Token-compression coding for video MLLM inputs — the "tokens, not frames" accounting the wiki tracks for long-context video LLMs. |
| [2608.27945](https://arxiv.org/abs/2608.27945) | Cross-Session Decomposition Attacks: Scaling Risk and Intent-Aligned Retrieval Defense | cs.AI | Session-level composition attacks against retrieval (many non-suspicious sessions secretly forming one attack) + defense using intent-aligned retrieval. |
| [2608.28102](https://arxiv.org/abs/2608.28102) | What Will This Copper Look Like Later? Forecasting Surface Appearance ... PBR Material | cs.CV | Learned forecasting of surface aging encoded as PBR materials — appearance dynamics as a generative forecasting task (world-model-adjacent). |

---

## Cross-cutting observations (2026-08-31 wave)

1. **The Monday wave's story is post-training reliability & dist-profiling.** Today's daily already logged the OPD-reliability cluster (RA-OPD/VISTA/SpikeOPD). This deeper pass adds the *evaluation-side* half of that story: Below-the-Noise-Floor shows single-seed KD gains are unmeasurable when seed σ is 2.8–48.7 pp — i.e., "reliable reporting" must include multi-seed variance before we can even talk about reliable distillation. The pair of LMP dialogue-game papers ([6.3], [6.4]) turn the same instinct into a recipe: diagnose failures, then repair them precisely.
2. **"Structured output" is spreading from code to creatives and worlds.** CommerceVibe generates ads as *HTML/CSS programs you can check*, Code-as-Worlds represents physics as *executable programs you can run and verify*, GeoNeXt reformulates geometry as *next-frame video prediction* — all manifestations of the wiki's [verifiable-rewards](../../concepts/verifiable-rewards.md)-for-nonnumeric-outputs thesis.
3. **Efficiency now has a *budget curve*, not just a point estimate.** Thinking-Costs-Tokens finds a crossover (structure hurts <~1,500 tokens, helps above); the LLM-energy paper distinguishes request-level vs token-level energy; dLLM spec-decoding quantifies trajectory drift as parallelism's cost. All three reward *joint* optimization over a wide operating range rather than a single "is X fast?" metric.
4. **GEO is becoming a research area with real infra.** The competitor-aware GEO paper from Capital One is the second GEO entry the wiki has seen — expect this domain (LLM-output optimization as a competitive game) to keep maturing alongside the [ads/auction] thread.
5. **Selectivity-over-fusion is the shared stick across multimodal rec, creative, and retrieval.** SG-UMP (router picks module order per user/dataset), TiGER (query time window as first-class index dimension), and the daily's HubMixer/AMUR all reject "just add more signal" — the design axis is *what to attend to, when*, which is the [attention] thesis restated for infra.

---

## Methodology

- **Listing source**: `arxiv.org/list/{cs.AI,cs.LG,cs.CL,cs.IR,cs.GT,cs.MA,cs.CV,cs.SE,cs.NE,cs.SY}/new` + `stat.ML/cs.HC/econ.GN/cs.CY` cross-listings, fetched directly via curl this session (Monday 31 Aug 2026 mailing). 718 unique IDs; 423 in-wave (≥2608.27460) fresh vs. wiki known-set.
- **Dedup**: every featured/honorable ID grep-verified **absent** from `wiki/**` and from the same-day `arxiv-daily` featured+HMs (claimed IDs: 2608.27950/27960/27991/28065/28199/28393/28306/28308/27857/28421/27508/27757/27912/27840/27826/28491/28027/28359).
- **Metadata**: per-paper `arxiv.org/abs/...` + HTML full-text `arxiv.org/html/{id}` fetched via curl; authors/abstracts/comments extracted programmatically; affiliations taken from HTML front matter where printed (marked *(stated)*).
- **Temp files**: listings, abs pages, and parsed JSON under the pre-authorized temp path `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/`; cleaned up after this report lands.
- **Coverage disclaimer**: papers cited via DOI/conference page only (not as arXiv IDs in wiki text) could theoretically overlap; flagged candidates were manually cross-checked against the 08-30/08-31 sibling reports. Initial shortlist omitted GOD ([7.3], agent-societies control room); its featured entry was added after a live abs-page fetch to place it correctly under ⑦. Nothing below was read in full PDF text.

*All affiliations above are stated only when the paper front matter says so; "(inferred)" entries are deduced from author identities / prior papers and remain tentative.*