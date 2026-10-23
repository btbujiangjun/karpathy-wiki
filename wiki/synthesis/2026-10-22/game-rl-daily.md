---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-10-22)"
type: synthesis
created: 2026-10-22
updated: 2026-10-22
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, benchmarks, self-play, multi-agent-rl, game-theory, offline-rl, inverse-rl, industry, daily-digest]
sources: [arxiv.org]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-10-22)

Covers 7 categories: **Game RL**, **Game AI Bot**, **Game Foundation Models / World Models**, **Procedural Content Generation**, **Game Benchmarks**, **Industry Game AI**, and **Related Techniques** (self-play, curiosity/exploration, hierarchical RL, imitation/inverse RL, reward shaping, world models, model-based/offline RL).

> **Run note.** Fresh sweep of the **Thu, 22 Oct 2026** arXiv announcement block. Harvest: `/list/{cat}/recent?show=2000` for `cs.LG, cs.AI, cs.CL, cs.MA, cs.GT, cs.RO, cs.CV, cs.HC, cs.NE, cs.SE, cs.CY` → **635 unique IDs in the 10-22 block** (967 listing slots) plus **776 in the 10-21 block** for leftover coverage; **full title scan of all 635**, then targeted `arxiv.org/abs` + LaTeXML `arxiv.org/html` fetches for 22 candidates (the export API was intermittently `429`, so metadata came from direct abs pages where needed). Every featured ID was grep-checked against a **9,907-ID baseline** built from the whole `wiki/` tree and returned **0 hits**; all are **new-to-wiki**. Deduplicated against the same-day siblings [`arxiv-daily`](arxiv-daily.md), [`arxiv-ai-search`](arxiv-ai-search.md) and [`arxiv-paper-check`](arxiv-paper-check.md), and against [`game-rl-daily` 2026-10-21](../2026-10-21/game-rl-daily.md). Sibling-claimed game/world-model papers are **cross-referenced, not re-featured** (house rule). Affiliations are parsed from the paper's own author block — never inferred.

**Headline of the day.** The block's most consequential game paper is a **negative, pre-registered result**: a match-progress reward signal that is demonstrably *predictive* of winning GuanDan still fails to be a reliable *optimization target* — five preregistered seeds, zero positive. That is a rare and valuable data point for [[rl-is-terrible]] and [[reward-shaping]]. Around it: a game-environment behavior-elicitation harness (**Fig**), offline multi-agent **inverse RL** from fixed behavioural datasets, and a strong game-theory cluster (best-response cycle structure in random games, Dantzig strategy-iteration lower bounds, pursuit–evasion game value).

---

## 1. Game RL — Reinforcement Learning in Games

### The Predictive–Optimization Gap in GuanDan Self-Play ★
- **Authors**: Qicheng Zou, Biao Yuan, Siyu Song, Wentao Liu, Xiaokun Wang
- **Affiliation**: Q. Zou — University of California San Diego; B. Yuan, S. Song, W. Liu, X. Wang — **Chabiyue (Shanghai) Information Technology Co., Ltd.** (author block)
- **Venue**: arXiv preprint, 21 Oct 2026 (cs.LG, stat.ML); no venue in comments
- **Link**: https://arxiv.org/abs/2610.29411

**Abstract.** Outcome-predictive signals are often treated as promising optimization targets in RL, but *predictive validity* and *optimization utility* are different claims. The paper exposes this distinction in **GuanDan** (掼蛋), a multi-round imperfect-information card game in which the implication of a round outcome depends on the public match state. Held-out analysis shows that **state–gain interactions** carry incremental predictive value beyond a constant signed-gain effect — i.e. match progress is genuinely predictively meaningful. The authors then use changes in a **frozen match-win predictor**, ΔΦ, as a controlled round-level supervision intervention inside a matched **DanZero-style Monte Carlo self-play** protocol.

**Key innovations / findings.**
- **The intervention works in one lineage, then fails at method level.** A selected progress-augmented checkpoint substantially beats its matched baseline on a locked evaluation — yet **none of five preregistered replication seeds is positive**, the pooled ten-seed interval includes zero, and across-iteration effects **repeatedly change sign** with no common late-stage advantage.
- Names the failure mode a **predictive–optimization gap**: a signal can describe outcome-relevant progress while failing to supply a reliably beneficial optimization direction.
- Methodologically notable: a **preregistered, multi-seed replication protocol for a game-RL reward-shaping intervention**, which is still rare in this literature and is precisely what turns a cherry-picked win into a negative result.
- Practical reading: before wiring a win-probability proxy into self-play reward, check whether the proxy's *gradient* — not its correlation — is stable across seeds and iterations.

**Why it matters here.** Directly complicates the optimism of "predict outcome, use it as reward" pipelines that dominate game-RL reward shaping, and gives [[rl-is-terrible]] a clean empirical instance. (high confidence on the reported result; single-source, abstract-only.)

### MA-UITD: Offline Multi-Agent Reward Inference for Characterizing Continuous Social Behavior
- **Authors**: Zeyuan Zhang, Yiyun Yang, Yuan Cheng, Herbert Zheng Wu, Yusi Chen
- **Affiliation**: — (no affiliation block on the abs page; HTML render returns 404)
- **Venue**: arXiv preprint, 21 Oct 2026 (cs.LG, cs.MA)
- **Link**: https://arxiv.org/abs/2610.29237

**Abstract.** Multi-agent inverse RL is useful not only for imitation but for understanding the computations behind social interaction. Inferring rewards from interacting agents is hard because observed choices reflect both **personal preferences** and **expectations about others**. Existing methods need extra environment interaction, repeated policy optimization as an inner loop, or restrictive assumptions on dynamics/action spaces — all blocking use on **fixed behavioural datasets**. **MA-UITD** (Multi-Agent Unilateral Inverse Temporal Difference) is an **offline** method that infers explicit agent-specific rewards from joint demonstrations, in continuous state with discrete or bounded continuous actions.

**Key innovations.**
- Represents the long-term consequences of each agent's own actions via **belief-conditioned successor features** that average over other agents' behaviour — a "unilateral" value that cleanly separates self-preference from partner expectation.
- Shared reward features + agent-specific preference vectors link unilateral values to the target reward; **inverse TD consistency** plus **noise-contrastive behavioural learning** remove the need for known dynamics or an inner policy-optimization loop.
- Beats baselines on simulated **cooperative, competitive, and general-sum** tasks in discrete-action settings; infers behaviourally compatible reward profiles for continuous actions.
- Applied to experimentally collected **social-foraging trajectories**, it recovers distinct spatial/interaction-dependent reward structures for **leaders vs followers** — a quantitative handle on latent social objectives.

**Why it matters here.** A practical offline multi-agent IRL recipe for game/social-simulation logs where re-running the environment is impossible. (tentative on the neuroscience claims; abstract-only.)

### Characterizing Oblivious Common-Reward Multi-Player Bandits: Universal Stationarity, Coordination Traps, and Certified Global Rates
- **Authors**: Mingxiao Li, Wenhai Lai, Hongyu Wang
- **Affiliation**: — (not stated on abs page; no affiliation block in HTML)
- **Venue**: arXiv preprint, 21 Oct 2026 (cs.LG); 20 pages + 11 pages supplement
- **Link**: https://arxiv.org/abs/2610.29673

**Abstract.** Studies the **oblivious common-reward multi-player multi-armed bandit** (OC-MPMAB): multiple players pull arms simultaneously and observe only a **shared reward**. Crucially the players are fully oblivious — they do not observe others' actions and **do not even know whether other players exist**. Three contributions: (i) independent gradient-bandit updates jointly form an **unbiased stochastic gradient estimator of a hidden product-policy objective**, giving a universal finite-time first-order stationarity guarantee for every instance; (ii) stationarity **cannot generally be strengthened to global optimality** — a **product-policy trap** obstruction rules that out; (iii) global optimality *is* recoverable under structural assumptions on the reward table.

**Key innovations.**
- **Finite-table certificates** that separately characterize **product-gradient dominance** and **self-bounding stochastic noise**; certificate-conditioned bounds on product-policy gap and pseudo-regret.
- Standard `O(1/t)` product-policy gap and `O(log T)` pseudo-regret rates follow when the certificates are uniform.
- A minimal model of **coordination without communication** — the cleanest formal statement this window of *why* independent learners can settle into a stable but collectively suboptimal product policy.

**Why it matters here.** The "coordination trap" is the theoretical shadow of the multi-agent self-play pathologies seen empirically in MARL; useful as a reference result for population-based/independent-learner analyses. (high confidence on the abstract's claims; abstract-only.)

### Learning Dynamic Games for Cooperative Iterative Tasks
- **Authors**: Mark Pustilnik, Francesco Borrelli
- **Affiliation**: University of California, Berkeley (author block)
- **Venue**: arXiv preprint, 21 Oct 2026 (cs.RO)
- **Link**: https://arxiv.org/abs/2610.28901

**Abstract.** Cooperative iterative tasks with multiple agents are modelled as a **dynamic game with shared constraints**. The proposed framework handles nonlinear, nonconvex dynamic games by using **previously executed feasible trajectories** to build a sampled **joint safe set** and player-specific **cost-to-go** functions. At each step agents jointly pick a previously sampled terminal state plus a **Generalized Nash equilibrium** used to reach it; a new solution is adopted only if it passes a **cooperative acceptance rule** agreed by the players. Supports individual non-degradation requirements and selection criteria (weighted costs, Nash bargaining).

**Key innovations.**
- Sampling-based **generalized-Nash** planning that inherits safety from executed trajectories rather than from a learned model.
- **Recursive feasibility guarantee** plus conditions under which each player's cost is non-increasing across iterations.
- Bridges game-theoretic equilibrium computation and safe multi-robot/agent control — the "cooperative game as a controller" pattern.

**Why it matters here.** Relevant to cooperative multi-agent control games; a rigorous alternative to learned MARL policies when feasibility matters more than throughput. (tentative for game-AI applicability — domain is robotics.)

---

## 2. Game AI Bot — LLM/VLM Game Agents, NPCs, Play

### Fig: Automated Multiagent Behavior Elicitor ★
- **Authors**: Anrui Gu, Zhichao Wang, Nicolai Ouporov
- **Affiliation**: **Fleet AI, San Francisco** (author block)
- **Venue**: arXiv preprint, 21 Oct 2026 (cs.AI, cs.MA); code released
- **Link**: https://arxiv.org/abs/2610.28891

**Abstract.** Social evaluations of multi-agent systems usually study behaviours *as they emerge* from an environment instead of **systematically intervening** to elicit them. **Fig** (*Finding Interactions in Games*) is an agentic system that performs targeted **elicitation interventions on game environments**: given a natural-language behaviour description it decomposes it into sub-behaviours, **generates new social games or selects existing ones**, and executes single or combined interventions on the games' **engine, opponents, instructions, and context**. Evaluation combines built-in mechanical checks with synthetic rubric judgments; interventions, generated games and evaluation mechanisms were validated by human review.

**Key innovations.**
- Reframes **games as programmable test beds** for intentional, controllable, reproducible behaviour evaluation — the inverse of "let it emerge and hope".
- Six target behaviours: **cooperation, exploitation, deception, covert coordination, betrayal, sabotage**. Models attempt the target behaviour in **45.2%** of episodes on average across valid Fig-generated scenarios; for game–behaviour pairs with available controls, Fig's interventions raise attempt rates by **+10.9%** versus matched control games.
- Decomposes the hard part of agent evaluation into **environment authoring + intervention design**, not just scoring.

**Why it matters here.** A direct contribution to the **game-as-benchmark** lane: behavioural safety/coordination evaluation of LLM agents with *causal* control over the environment. (high confidence; single-source, abstract-only.)

### Sibling-claimed game agents — cross-references only
These are game/agent papers from the same window already written up by `arxiv-daily` 2026-10-22; listed for completeness, **not re-featured**:
- **TARSphere** ([2610.30043](https://arxiv.org/abs/2610.30043), Zhejiang University) — full-stack sim + embodied NPCs + constrained dialogue + event-driven FSM + frozen-MLLM harness + **TARSphere-Bench** (360 episodes / 30 indoor scenes, paired robustness & disruption conditions).
- **AW-0 / Agentic World Action Models** ([2610.30136](https://arxiv.org/abs/2610.30136), UC Berkeley / Stanford / NVIDIA et al.) — code, future video and robot actions as three coupled streams; code doubles as planner structure and reusable skill library.
- **Scaling in Games** ([2610.28698](https://arxiv.org/abs/2610.28698)) — continued pre-training across data/diversity/model size in virtual worlds; competitive with specialists in 3D.

---

## 3. Game Foundation Models & World Models

### Causal World Models under Physical Parameter Shifts
- **Authors**: Chu Lin, Yi Sun
- **Affiliation**: The City College of New York (Dept. of Computer Science; Dept. of Electrical Engineering)
- **Venue**: arXiv preprint, 21 Oct 2026 (cs.LG, cs.RO)
- **Link**: https://arxiv.org/abs/2610.29088

**Abstract.** World models predict how embodied systems evolve under actions, but accuracy degrades when physical conditions leave the training distribution. The paper separates two components of causal modelling: **which inputs a predictor may use**, and **how its mechanism computes their effects**. In a synthetic benchmark with shortcut features, a **frozen dependency mask derived from paired interventions** cuts mean OOD RMSE from **1.769** (fully connected predictor) to **0.697**, close to the generator-oracle mask (**0.694**). For robot link-mass extrapolation in **CausalWorld** (disjoint train/test mass ranges) they build **finger-local world models** in which link masses enter inertia and dynamics-bias terms through **explicit affine coefficients**.

**Key innovations.**
- Actions act either through a learned torque network or the **known PD controller**; learned residuals capture contact effects.
- With the known-PD model, out-of-range masses become a **consistent predictive gain**: median time-averaged joint R² over 150-step rollouts rises **0.609 → 0.727**, improving in all ten task-seed runs (sign test p = 0.002).
- A learned-torque model is competitive with the strongest recurrent robotic world model (median joint R² 0.755–0.768 vs 0.752) in a shared 100-step forecast — whereas feeding out-of-range masses sharply degrades MLP and recurrent predictors.
- Takeaway: **how** a physical parameter enters the dynamics mechanism decides whether an out-of-range value helps or hurts.

**Why it matters here.** A CausalWorld (game-style physics benchmark) result that speaks to **world-model generalization under distribution shift** — the regime that matters for procedural/varied game environments. (tentative; abstract-only.)

### Pair-Free Coarse-to-Real Video Generation via Real-to-Coarse Image Supervision
- **Authors**: Gonzalo Gómez-Nogales, Daohan Lu, Peiye Zhuang, Tinghui Zhou, Yi Zhou
- **Affiliation**: Universidad Rey Juan Carlos; New York University; **Roblox**; **Adobe** (author block)
- **Venue**: arXiv preprint, 21 Oct 2026 (cs.CV)
- **Link**: https://arxiv.org/abs/2610.28954

**Abstract.** Coarse-to-real (C2R) video generation converts **coarse animation, simulation, or game-rendered videos** into photorealistic video while preserving layout, camera motion and dynamics. Training such models needs aligned (coarse, realistic) video pairs, which are expensive and confine prior systems to narrow synthetic domains. The paper exploits an asymmetry: paired *videos* are hard, but paired **real-to-coarse images** are easy to construct with editing and 3D reconstruction tools. **DINO-R2C** learns to map realistic images to coarse images in DINO feature space and is applied frame-wise to real videos to synthesize **pseudo-coarse videos**; **C2R#** then learns to generate each real video from its pseudo-coarse counterpart, needing **no (coarse, realistic) video pairs**. At inference DINO-R2C is discarded and real coarse videos drive C2R# directly.

**Key innovations.**
- **Pair-free training** that scales with any real-video corpus rather than with paired synthetic video.
- Decouples "what makes an image look coarse" (image-level, cheap) from "how coarse motion becomes photoreal" (video-level, learned).
- Industrial relevance: **Roblox + Adobe** co-authorship makes this the window's clearest **game-industry** presence in the rendering/world-model lane.

**Why it matters here.** The rendering half of the **playable-world-model** stack (engine proxy → photoreal), complementary to the engine/renderer-separation line (Matrix-Game 4.0, 2026-10-21). (tentative; abstract-only, no numbers in abstract.)

### Sibling-claimed world models — cross-references only
- **LiveAct** ([2610.29408](https://arxiv.org/abs/2610.29408), Tsinghua × Kuaishou) — real-time **multi-agent** world model with a Heterogeneous Action Interface; 0.898/0.942 agent-attribution accuracy; 17.70 FPS at 512×448.
- **CADRE / Rethinking Video Autoencoders** ([2610.30129](https://arxiv.org/abs/2610.30129), Kyutai × Google × LIGM) — causal diffusion representation autoencoders across spatio-temporal compressions; manipulation/navigation need opposite compression regimes.
- **ALPS** ([2610.30120](https://arxiv.org/abs/2610.30120)) and **PhysiCalWorld** ([2610.30125](https://arxiv.org/abs/2610.30125)) — visual state encoders and in-context physics calibration for world models.
- **Events, Not Pixels** ([2610.29435](https://arxiv.org/abs/2610.29435)) — event transitions carry ~70% of return error on **Atari-100k**; 39/44 model–collection pairs beat random patches (median +44 pp, p = 1.4e-7). Featured by `arxiv-paper-check`; the closest thing this window has to a **game-world-model reward-diagnosis** paper.

---

## 4. Procedural Content Generation (PCG)

**Empty for this window** (no unclaimed classic PCG / level-generation / automated game design paper in the 10-22 block). Nearest adjacencies: **Fig** (§2) generates new *social game* rules and contexts programmatically, and **Pair-Free C2R** (§3) generates photoreal game visuals from engine proxies — both content-generation-adjacent but neither is level/asset PCG. Continuing to monitor.

---

## 5. Game Benchmarks

### P2NPCBench: Paired P vs NP-Complete Problems Hardened by Adversarial Multi-Agent Rewriting
- **Authors**: Nurul Labib Sayeedi, Md. Faiyaz Abdullah Sayeedi, Zabir Al Nazi, Mahbub E Sobhani, Shubhashis Roy Dipta
- **Affiliation**: United International University; BRAC University; University of California, Riverside; University of Maryland, Baltimore County (author block)
- **Venue**: arXiv preprint, 21 Oct 2026 (cs.CL); code released
- **Link**: https://arxiv.org/abs/2610.30103

**Abstract.** Many NP-complete problems have a polynomial-time twin differing in a single structural detail (3- vs 2-colouring). A model that *reasons* rather than *recalls* should notice which side of the boundary a problem sits on, but existing benchmarks either fix wording or ignore complexity class. **P2NPCBench** has **12 problem families**, each NPC problem paired with a P twin over the same surface. To strip textbook cues the authors build it with **AgentGAN**, an adversarial multi-agent framework: a generator rewrites each statement until a panel of frozen code models fails, while an **executable validity gate** keeps every rewrite answer- and class-preserving. Result: **2,114 hardened statements** with hand-verified reference human solvers.

**Key innovations.**
- Every model scores lower on NPC statements than on their P twins (**35.4% vs 63.8%** pass@1); **95.1%** of model-family pairs fail more often on the NPC side.
- A tenfold time limit lifts NPC accuracy only **28.5% → 31.9%**, so failures are wrong/crashing programs rather than slow ones.
- Hardening **narrows** the class gap from 24.8 to 14.6 points — part of the apparent gap is familiarity with textbook phrasing, not complexity class.
- The **adversarial multi-agent rewriting + executable oracle** recipe is itself reusable for any benchmark that wants to defeat memorization.

**Why it matters here.** Not a game benchmark, but the best example this window of **agentic multi-agent benchmark construction** (generate → adversarially harden → verify executably) — the same loop game-agent benchmarks increasingly need. (high confidence; abstract-only.)

### Other benchmark-relocated items
- **Fig** (§2) is simultaneously a game-behaviour **benchmark generator** with mechanical + rubric checks over 6 social behaviours.
- **TARSphere-Bench** ([2610.30043](https://arxiv.org/abs/2610.30043), sibling-claimed) — 360 episodes / 30 scenes with paired perturbation conditions.
- **Cycle structure** ([2610.29153](https://arxiv.org/abs/2610.29153), §7) is not a benchmark, but its random-game cycle statistics are a ready-made **testbed generator** for equilibrium-learning claims.

---

## 6. Industry Game AI

- **Chabiyue (Shanghai) Information Technology Co., Ltd.** — co-authors of the GuanDan self-play study ([2610.29411](https://arxiv.org/abs/2610.29411), §1). The window's only *game-company-authored* paper, and notably a **negative/replication** result rather than a capability claim.
- **Roblox** and **Adobe** — co-affiliations on the pair-free coarse-to-real video generator ([2610.28954](https://arxiv.org/abs/2610.28954), §3), i.e. game-platform rendering + creative tooling converging on C2R video.
- **ByteDance** — co-affiliation (with Duke and UMD) on RL-based black-box red-teaming of multi-agent systems ([2610.28966](https://arxiv.org/abs/2610.28966), §7).
- **Kuaishou** — co-affiliation on LiveAct ([2610.29408](https://arxiv.org/abs/2610.29408), sibling-claimed).
- No papers from EA / Ubisoft / Epic / Unity / Riot / Tencent IEG / NetEase / Krafton surfaced unclaimed in this block.

---

## 7. Related Techniques

### Cycle Structure of Best-Response Dynamics in Random Bimatrix Games ★
- **Authors**: Georgios Nikolaos Karelas, **Gábor Lugosi**, Rui-Ray Zhang
- **Affiliation**: Pompeu Fabra University / Barcelona School of Economics; ICREA; Monash University (author block)
- **Venue**: arXiv preprint, 21 Oct 2026 (cs.GT)
- **Link**: https://arxiv.org/abs/2610.29153

**Abstract.** Studies **best-response dynamics** in two-player bimatrix games with `n` strategies each and payoffs from a continuous distribution, under structural assumptions: **symmetric, antisymmetric, common-interest, zero-sum, and independent-payoff** games. When players alternate best responses they eventually cycle through the same action sequence. The paper characterizes the **cycle structure** of large random games — number of cycles, number of cycles of a given length, length of the longest cycle, and related quantities — showing that game structure strongly shapes typical cycle structure. Arguments represent best-response dynamics as **directed bipartite graphs** and use their cycle structure.

**Key innovations.**
- First systematic **distributional** theory of best-response cycles across the five canonical game classes (previous work mostly bounded worst-case cycle length or studied specific constructions).
- A bipartite-graph dictionary that maps "which equilibrium-learning pathologies are typical" onto random-graph cycle statistics.
- Direct relevance to **self-play / fictitious-play / no-regret** analyses: cycle length distribution is exactly what governs whether alternating updates converge, orbit, or wander.

**Why it matters here.** Supplies the typical-case backdrop to the worst-case game-theory results this wiki has been tracking (smoothed complexity, strategy-iteration lower bounds). (tentative — abstract-only, no explicit rate statements quoted.)

### Simple Strategy-Iteration with Dantzig's Rule is not Strongly Polynomial on Turn-Based Deterministic Games ★
- **Authors**: Sanyou Mei
- **Affiliation**: Department of Industrial Engineering and Decision Analytics, **Hong Kong University of Science and Technology**
- **Venue**: arXiv preprint, 19/21 Oct 2026 (cs.GT, cs.CC, math.OC)
- **Link**: https://arxiv.org/abs/2610.27386

**Abstract.** For turn-based deterministic zero-sum games with discounted and long-run average costs: for **discounted** costs, exponential and superpolynomial **iteration lower bounds** for simple strategy iteration with **Dantzig's rule**, under unrestricted costs and unit weights respectively. To the authors' knowledge this is the first proof that the method is **not strongly polynomial even when all action costs are in {−1, 0, 1}**. For **long-run average** costs, an exponential iteration lower bound for termination of a Dantzig counterpart under unrestricted costs, plus a **strongly polynomial implementation with unit weights**.

**Key innovations.**
- Closes a "is Dantzig's rule the good pivot rule?" question negatively for discounted games, at the strongest possible cost restriction.
- Sharp separation between **discounted** (bad) and **average-cost with unit weights** (good) regimes for the same pivot rule.
- Complements the recent wave of strategy-iteration/VI smoothed-complexity and lower-bound results already on file (2026-10-17/18 digests).

**Why it matters here.** Game-solving complexity is the ceiling on any RL claim of "we solve this game class". (high confidence; abstract-only.)

### Minimum-Time Escape from the Conic Field of View of a Reeds–Shepp Pursuer ★
- **Authors**: Ubaldo Ruiz
- **Affiliation**: CICESE, Ensenada, Baja California, Mexico
- **Venue**: arXiv preprint, October 2026 (cs.RO, math.OC); 30 pages
- **Link**: https://arxiv.org/abs/2610.27629

**Abstract.** Minimum-time escape of an omnidirectional evader from the **forward conic field of view** of a **Reeds–Shepp pursuer** with minimum turning radius `r`. For speed ratio `ν` and cone half-angle `α`, the paper proves a **global escape/holding classification**: straight reversal holds the whole cone for `ν ≤ sin α`; escape is confined to a **barrier-bounded dart** for `sin α < ν ≤ 1`; escape is possible from every state for `ν > 1`. For the slower-or-equal case the solution is constructed with **Isaacs' characteristics** and verified in feedback form (Filippov pursuer relay + one-sided evader branch).

**Key innovations.**
- The finite escape time is the **first root of one scalar equation**; the holding region is bounded by nonusable ray parts and a barrier closing with a convex corner on the front axis.
- **Value-of-the-game at every state except the corner**: there the two strategy values differ — the pursuer's is infinite, while an evader that chooses which barrier branch to cross from the initial germ escapes before the barrier time `τ_I`, which is the evader's exact strategy value.
- An independent **level-set solver** agrees with the closed-form escape time and reproduces the holding region.

**Why it matters here.** A clean, fully-solved **pursuit–evasion differential game** with a genuine value discontinuity — the kind of ground truth that RL pursuit-evasion benchmarks rarely have. (tentative; abstract-only.)

### Value-Rectified Distillation for Flow-based Offline Reinforcement Learning ★
- **Authors**: Ke Jiang, Wen Jiang, Yoshinobu Kawahara, Xiaoyang Tan
- **Affiliation**: College of Computer Science and Technology, **Nanjing University of Aeronautics and Astronautics** (author block); journal ref lists Kawahara (Kyoto/RIKEN lineage)
- **Venue**: arXiv preprint, 21 Oct 2026 (cs.LG, cs.AI); journal-ref present
- **Link**: https://arxiv.org/abs/2610.29075

**Abstract.** Addresses **Out-of-Distribution Mode Averaging**, which appears when distilling **Flow Matching**-based behaviour policies in offline RL: over multi-modal datasets, standard distillation forces the policy to interpolate across behavioural modes, collapsing generated actions into invalid OOD regions. **VRD (Value-Rectified Distillation)** reformulates offline policy distillation as a **value-guided generative trajectory alignment** problem; a **dynamic coupling mechanism** rectifies flow dynamics to explicitly decouple modes and isolate high-value actions.

**Key innovations.**
- Two instantiations: **VRD-Q** (value-quantile behaviour distillation, statistically filtering low-value behaviours) and **VRD-R** (reorganizes the latent space to geometrically isolate high-value generative trajectories from the FM behaviour policy).
- Improves generative offline-RL baselines across continuous control and planning on **D4RL, OGBench, Minari** — with the largest gains on **multi-modal, non-expert** datasets.
- Attacks the specific failure mode (mode averaging → OOD actions) that makes flow/diffusion policies fragile in offline game/control data.

**Why it matters here.** Offline RL from logged gameplay is the realistic deployment path for games; mode averaging is its most common silent failure. (tentative; abstract-only.)

### SAFTER: Safety-Aware Filtering Through Explicit Recoverability
- **Authors**: Benedictus C. G. Cinun, Bin Hu
- **Affiliation**: Department of Electrical and Computer Engineering (author block; institution not named in the affiliation line)
- **Venue**: arXiv preprint, 21 Oct 2026 (eess.SY, cs.LG); 24 pages
- **Link**: https://arxiv.org/abs/2610.29149

**Abstract.** Learning safe policies that generalize under **bounded actuation** is hard: an unsafe decision may become **unrecoverable**. Conventional **control barrier function** filters enforce only *instantaneous* safety and ignore future recoverability. **SAFTER** embeds a differentiable, **closed-form backup-CBF** filter into **Soft Actor-Critic**, unifying current safety, finite-horizon backup safety, terminal recoverability and input admissibility into a single differentiable certificate; the CBF condition yields an **exact minimum-intervention projection** without iterative online optimization.

**Key innovations.**
- Quadruped navigation: **90%** training success with **30.6% fewer** transitions than vanilla SAC and **34.1–35.1% fewer** than current-state CBF-filtered SAC.
- Unseen simulated environments: up to **+42.4 pp** over CBF-RL and **+61.4 pp** over SEA-Nav; 73.3% / 76.7% success on two real-world maps.
- Ablations show differentiating *through* the safety filter matters: replacing the projection Jacobian with the identity drops a High-Shift environment from **61.4% → 6.2%**.
- Recoverability-aware filtering doubles as a **learning** mechanism (sample efficiency), not just a runtime shield.

**Why it matters here.** Shielding/recoverability for game agents in irreversible states (permadeath, resource exhaustion) is an under-explored safety lane. (tentative; abstract-only.)

### Is In-Context Reinforcement Learning a Posterior Sampler? An Empirical Study
- **Authors**: Weiqin Chen, Xinlong Du, Gesualdo Scutari, Harsha Honnappa
- **Affiliation**: Edwardson School of Industrial Engineering, **Purdue University** (author block)
- **Venue**: arXiv preprint, 21 Oct 2026 (stat.ML, cs.LG)
- **Link**: https://arxiv.org/abs/2610.28977

**Abstract.** In-context RL exploits LLM in-context learning to zero-shot generalize to unseen tasks without parameter updates. The **Decision-Pretrained Transformer (DPT)** is appealing for its theoretical grounding: under idealized assumptions (sufficiently expressive model, infinite pretraining data) DPT can perform **Bayesian posterior sampling**. Whether that survives in practice is open. The paper derives two **necessary conditions** for a posterior sampler — **sufficient-statistic invariance** and the **martingale property** — builds statistical hypothesis tests for them, and applies them in Gaussian, Bernoulli and linear-bandit settings.

**Key innovations.**
- **Both conditions are consistently violated** — evidence that ICRL/DPT does **not** behave as a Bayesian posterior sampler in practice.
- Converts an idealized-theory claim into a **testable, falsifiable** property, and ships the tests as a toolkit for any ICRL method.
- Relevant to game/decision agents built on DPT-style in-context learners: their exploration is not the principled posterior sampling their theory advertises.

**Why it matters here.** Undercuts a common justification for DPT-based game agents; complements the GuanDan negative result as a second "the theory's guarantee doesn't survive contact" paper. (high confidence; abstract-only.)

### Black-Box Red-Teaming of Multi-Agent Systems via RL (ReMAS)
- **Authors**: Yuqi Jia, Hangsheng Zhang, Chenxi Liu, Junjie Liang, Xun Chen
- **Affiliation**: **Duke University**; **ByteDance**; University of Maryland, College Park (author block)
- **Venue**: arXiv preprint, 20/21 Oct 2026 (cs.CR, cs.AI)
- **Link**: https://arxiv.org/abs/2610.28966

**Abstract.** LLM agents are increasingly deployed as multi-agent systems (MAS). Prior black-box red-teaming targets single agents and is **far less effective in MAS**, where sub-agents may not directly interact with the user. **ReMAS** is the first RL-based red-teaming framework tailored to MASs: it fine-tunes attacker LLMs to generate adversarial prompts for **system-prompt extraction**, in two stages — a **rewrite** stage refining base attack prompts, and a **template generation** stage constructing attack templates that raise the likelihood of invoking specific sub-agents and revealing their prompts.

**Key innovations.**
- Substantially higher attack success than existing black-box attacks, with **transferability across backend LLMs and MAS structures**.
- Models the MAS as an **attack-surface routing problem** (which sub-agent can you reach?) rather than a single-model jailbreak.
- Industrial co-authorship (ByteDance) signals production relevance of MAS prompt confidentiality.

**Why it matters here.** For game bots built as multi-agent crews/NPC orchestrators, sub-agent system prompts are the new secret to protect. (tentative; abstract-only.)

### Near Minimax Rate for Quantile Distributional Reinforcement Learning
- **Authors**: Zijie Cheng, Zhihua Zhang
- **Affiliation**: School of Mathematical Sciences, **Peking University** (author block)
- **Venue**: arXiv preprint, 21 Oct 2026 (stat.ML, cs.LG)
- **Link**: https://arxiv.org/abs/2610.29595

**Abstract.** Studies **quantile distributional policy evaluation** under the quantile Bellman fixed point `η_m`, across quantile resolutions, in **Wasserstein** distances, with a generative model. The authors construct `η_m^(n)` from an empirical MDP and prove non-asymptotic error bounds.

**Key innovations.**
- When reward densities are bounded away from zero, a **root-`n` high-probability bound simultaneously over all resolutions `m` and all Wasserstein orders `1 ≤ p ≤ ∞`**.
- When densities vanish at support endpoints, continuity + endpoint monotonicity preserve the same resolution-independent rate for `1 ≤ p ≤ 2`; for `p > 2`, a root-`n` bound with coefficient `m^(1/2−1/p)` plus a slower resolution-independent `n^(−1/p)` bound.
- Resolution-independent `W_∞` consistency governed by the continuity modulus of reward quantile functions.
- Characterizes the **exact local asymptotic minimax risk** per resolution as the expected Wasserstein-coordinate norm of the efficient Gaussian limit, proves the estimator attains it, and shows a one-state instance has resolution-independent risk while a two-state endpoint-vanishing instance grows as `m^(1/2−1/p)`.

**Why it matters here.** Distributional RL is the default for risk-sensitive game agents (variance-averse poker/bidding); this gives the sharp statistical limit for quantile-based value estimation. (high confidence on the theorem statements as abstracted; abstract-only.)

### Brittle by Design? Multi-Scenario Reinforcement Learning for Robust Mission Coordination
- **Authors**: İbrahim Oğuz Çetinkaya, Sajad Khodadadian, Taylan Topcu
- **Affiliation**: Grado Department of Industrial and Systems Engineering, **Virginia Tech** (author block)
- **Venue**: arXiv preprint, 21 Oct 2026 (eess.SY, cs.AI, cs.LG)
- **Link**: https://arxiv.org/abs/2610.28818

**Abstract.** Integrates high-fidelity digital mission models with RL for adaptive task allocation. Using a Digital Engineering infrastructure (digital mission model + agent-based simulation), the paper formulates mission-tactics management as an **MDP** and trains a **PPO coordinator** mapping mission states to tactical actions, on an aerial firefighting mission with three scenarios.

**Key innovations.**
- All trained coordinators beat random/heuristic baselines.
- **Single-scenario coordinators are brittle**: the one trained on the *more forgiving* scenario degrades to **random-level tactics** in more demanding scenarios, whereas the demanding-scenario coordinator retains most of its advantage when transferred.
- For the same budget, a coordinator trained on **both** scenarios concurrently matches scenario-specific coordinators in their own scenarios and significantly beats every other policy.
- Sensitivity analyses on ignition location, weather, scenario and curriculum: **the variability represented during training shapes post-deployment performance**.

**Why it matters here.** A clean demonstration of the **training-distribution brittleness** that plagues game AI curriculum design (and a counterpoint to "scale one scenario harder"). (tentative; abstract-only, non-game domain.)

### JaxMARL-BC: Multi-Agent RL for Macroeconomic Modelling, in Seconds
- **Authors**: Daniele Montagnani, Andrea Coletta, Antonietta Mira, Aldo Glielmo
- **Affiliation**: Università di Pavia (author block); 9 pages
- **Venue**: arXiv preprint, 21 Oct 2026 (cs.LG, cs.MA)
- **Link**: https://arxiv.org/abs/2610.28907

**Abstract.** MARL offers a principled way to populate simulated economies with heterogeneous decision makers. Adoption in macroeconomics has been slow for two reasons: lack of a shared frame of reference connecting MARL systems to macroeconomic models, and (implied) computational cost. **JaxMARL-BC** provides a JAX-based MARL environment for macro modelling that runs **in seconds**.

**Key innovations.**
- JAX-native vectorized MARL environment for many heterogeneous agents (the same architectural pattern as JaxMARL/JAXtari for games).
- Aimed at making MARL macro experiments as cheap to iterate as game-RL benchmarks.

**Why it matters here.** Not a game per se, but the **JAX-vectorized multi-agent environment** pattern is exactly what game-MARL benchmarking has been adopting (see JAXtari, 2026-10-19). (tentative; abstract-only.)

### Cross-referenced game-theory items (sibling-claimed)
- **When Are We Near Nash? Certifying Solutions in General-Sum Games** ([2610.29300](https://arxiv.org/abs/2610.29300)) — zero-best-response certificate from regret accumulators for extensive-form games.
- **Computing the Nucleon of Matching Games** ([2610.29731](https://arxiv.org/abs/2610.29731)) — polynomial for non-negative rational weights; NP-hard for unit-weight b-matching with capacity ≤ 3; resolves three open problems.
- **Is Anyone Enforcing the Cartel?** ([2610.28787](https://arxiv.org/abs/2610.28787)) — counterfactual audit separating *deterred* from *matching* collusion in RL/LLM agent markets; outcome measures cannot distinguish them.

### Nearest-miss, not game AI
- **An Exact 93-Move Solution to a Nonlocal Crystal-Exchange Puzzle** ([2610.29493](https://arxiv.org/abs/2610.29493), unclaimed by siblings) — a combinatorial puzzle solver; surfaced by the title sweep for the word "puzzle", dropped as out-of-lane.

---

## Coverage & flags

| Lane | Featured (new-to-wiki) | Cross-referenced (sibling-claimed) |
|------|------------------------|------------------------------------|
| Game RL | GuanDan `2610.29411` ★, MA-UITD `2610.29237`, OC-MPMAB `2610.29673`, Dynamic Games `2610.28901` | Scaling in Games `2610.28698` |
| Game AI Bot | Fig `2610.28891` ★ | TARSphere `2610.30043`, AW-0 `2610.30136` |
| Foundation / World Models | Causal WM `2610.29088`, Pair-Free C2R `2610.28954` | LiveAct `2610.29408`, CADRE `2610.30129`, ALPS `2610.30120`, PhysiCalWorld `2610.30125`, Events-Not-Pixels `2610.29435` |
| PCG | — (empty) | — |
| Benchmarks | P2NPCBench `2610.30103` | TARSphere-Bench (in `2610.30043`) |
| Industry | Chabiyue `2610.29411`, Roblox/Adobe `2610.28954`, ByteDance `2610.28966` | Kuaishou (LiveAct) |
| Related | BR cycles `2610.29153` ★, Dantzig lower bound `2610.27386` ★, Pursuit–evasion `2610.27629` ★, VRD `2610.29075` ★, SAFTER `2610.29149`, ICRL test `2610.28977`, ReMAS `2610.28966`, Quantile DRL `2610.29595`, Brittle RL `2610.28818`, JaxMARL-BC `2610.28907` | Nash cert `2610.29300`, Nucleon `2610.29731`, Cartel `2610.28787` |

**Flags**
- ⚠️ **Abstract-only** for every paper — no PDF full text was read; all numbers are as the authors report them and are not independently reproduced.
- ⚠️ **Affiliations are parsed, never inferred**: taken from the paper's author block / `thanks` notes in the LaTeXML render. Where no block exists, the entry reads "—" (`2610.29237` HTML 404; `2610.29673` no affiliation block; `2610.29149` names a department only).
- ⚠️ **Window definition**: the fresh **Thu 22 Oct 2026** announcement block (covering the 10-20/10-21 submission wave) is the primary target; the 10-21 block was scanned only for leftovers. Two featured items (`2610.27386`, `2610.27629`) were submitted 19 Oct and announced in the 10-21 block — flagged as such.
- ⚠️ **PCG lane empty** — no unclaimed procedural-content paper in the block; sustained gap noted.
- ⚠️ **No named commercial studio** (EA/Ubisoft/Epic/Unity/Riot/Tencent IEG/NetEase/Krafton) papers surfaced unclaimed; industry presence is via Chabiyue, Roblox, Adobe, ByteDance and Kuaishou.
- ⚠️ **Sibling overlap managed by cross-reference, not duplication**: 13 game/world-model papers claimed by `arxiv-daily` / `arxiv-ai-search` / `arxiv-paper-check` on 2026-10-22 are listed with links but not re-written.
- ⚠️ No contradictions with existing wiki pages. The GuanDan negative result is consistent with — and strengthens — the existing [[rl-is-terrible]] thesis; no page asserts the contrary claim.
