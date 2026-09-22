---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-22)"
type: synthesis
created: 2026-09-22
updated: 2026-09-22
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, self-play, marl, game-theory, pcg, benchmarks, industry-game-ai, imitation-learning, reward-shaping, model-based-rl, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-22)

> **Methodology note**: **Tue 22 Sep 2026** mailing (processes Mon-21 submissions). Fresh window = **IDs 2609.22087–2609.24555** (max observed 2609.25001 across categories). The `/list/{cat}/new` pages had begun refreshing to the Tue-22 batch mid-day, so unlike the 09-21 siblings' API-tail-sweep necessity this window was parsed **directly from live `/list/{cat}/new` parses** for **cs.AI / cs.LG / cs.GT / cs.MA / cs.CV / cs.CL / cs.RO / cs.NE / cs.HC** → **1,029 unique in-window IDs** (deduped across categories) → title + abstract keyword sweep → **82 unclaimed game-candidates** → targeted abs-depth screening → **20 curated + 3 runner-ups**. Every featured/runner-up ID was **grep-verified 0 hits in `wiki/`** and sits outside every 09-21 and 09-22 sibling-claimed set.
>
> **Continuity / already-covered by the 09-22 siblings (not re-featured):** the window's *world-model marquee* was taken hours ago by the same-day [arxiv-daily 09-22](../2026-09-22/arxiv-daily.md) — **CausalWM** 2609.23184 (16B embodied causal-CoT world model, TriWorldBench SOTA), **ARPS** 2609.23369 (action-relevant predictive states for WAMs, 99.2% LIBERO), **FireWorldBench** 2609.23064 (coupled-field fire-dynamics physical-intelligence benchmark), and the detective-game **Structured Knowledge Trees** LLM-narrative engine 2609.23043 (−64.78% critical hallucinations, 0% premature disclosure). This edition therefore mines the **unclaimed game-relevant remainder** — which this window shapes as a **game-theory proof day + world-model-robustness + LLM game-reasoning/PSA (programmatic synthetic agents)** digest.

---

## 1. Game RL, Multi-Agent Learning & Game Theory

### 1.1 A Horizon-Independent Regret Bound for Optimistic Hedge in General-Sum Games
- **Authors**: Junsoo Ha
- **Affiliation**: not stated (inferred — single-author game-theory analysis)
- **Venue**: arXiv preprint (2609.22839, cs.GT / cs.LG), fresh Tue 22 Sep window
- **Key Innovations**: Can the *canonical* learning rule get constant regret in self-play? Prior constant-regret results ("last-iterate" work by the MORM line) needed modified regularization and higher-order prediction; plain **Optimistic Hedge** was stuck at logarithmic. This paper proves **plain Optimistic Hedge with a constant step size attains O_{n,d}(1) individual regret** in general-sum games under expected loss-vector feedback — representing the dynamics as a real-analytic recurrence on a compact space whose exact finite-order difference relation eliminates horizon dependence.
- **Results**: Time-averaged play enjoys an **O_{n,d}(1/T) coarse correlated equilibrium (CCE) gap**. The proof uses a *nonconstructive* Noetherianity argument (Frisch 1967), so the (n,d) dependence remains implicit — an existentially-valid but non-explicit bound.
- **Significance**: Closes the canonical-method gap in the constant-regret self-play program — the theoretical baseline that practical game-RL exploiters (counterfactual-regret minimizers, Nash-convergence sanity checks) can now cite for the most standard no-regret algorithm.
- **Link**: https://arxiv.org/abs/2609.22839

### 1.2 Payoffs and Perception Mediate Environmental Feedback in an N-Player Trust Game with Q-Learning
- **Authors**: Ruqiang Guo, Zhaoyi Hu, Fangfang Wang, Linjie Liu
- **Affiliation**: not stated (inferred — RL + eco-evolutionary modeling group; math-ph domain)
- **Venue**: arXiv preprint (2609.24493, math-ph / behavioral game theory), fresh Tue 22 Sep window
- **Key Innovations**: Unites two normally separate modeling traditions — *RL adaptation* (tabular Q-learning agents) and *eco-evolutionary feedback* (behavior alters the environment for later decisions) — in a **fixed-role, two-population hierarchical trust game** coupled to a centered endogenous environment. Contrasts payoff-parameter vs observed-environment-tier variation from the *same learned baseline state* to control for prior learning.
- **Results**: Higher payoff multiplication shifts fixed-payoff trust from a low to a higher finite-horizon level, **led by risk-seeking investors**; environmental feedback promotes trust near perception-tier boundaries yet reinforces its decline at the high-return operating point, where stronger drive and longer horizons deepen the negative effect. Endogenous feedback carries past collective outcomes into future payoffs and observed states.
- **Significance**: A template for the "trust economy" branch of game-RL sociodynamics — formal evidence that **perceived state tiering, not just payoff magnitude, is a control knob** for cooperation collapse in multi-agent economies.
- **Link**: https://arxiv.org/abs/2609.24493

### 1.3 Subgame Perfection in Graph Games with ω-Recognizable Preference Relations
- **Authors**: Véronique Bruyère, Christophe Grandmont, Noémie Meunier, Jean-François Raskin
- **Affiliation**: not stated (inferred — Université de Mons game-theory/verification line; Bruyère/Raskin)
- **Venue**: arXiv preprint (2609.22906, cs.GT), fresh Tue 22 Sep window
- **Key Innovations**: Frames multiplayer graph-game strategy synthesis under a *generic* preference model — each player's preference relation over plays is **ω-recognizable** (equivalently: preferences over a finite payoff set, with equal-payoff play sets ω-regular), avoiding ad-hoc payoff-function-specific theorems.
- **Results**: The **constrained SPE existence problem is EXPTIME-complete**, and the same complexity holds for Nash equilibria — pinning the generic-preference version to the same hardness class as the concrete-payoff special cases.
- **Significance**: A single framework that subsumes most structured payoff models in the graph-game literature — the complexity anchor for anyone engineering bounded-memory equilibria in general-sum game graphs.
- **Link**: https://arxiv.org/abs/2609.22906

### 1.4 Subgame-Perfect Nash Equilibria of Plurality Voting with Abstention: PSPACE-Completeness for Restricted Ballots
- **Authors**: Edith Elkind
- **Affiliation**: not stated (inferred — University of Oxford; Elkind computational social choice lineage)
- **Venue**: arXiv preprint (2609.24292, cs.GT), fresh Tue 22 Sep window
- **Key Innovations**: Sequential Plurality elections where each voter may abstain or vote for a single candidate, ties resolved uniformly at random, small voting cost (prefer abstention when the vote is pivotal-free). Adds the **restricted-ballot variant** — each voter may only vote for candidates within a given prefix of her own ranking.
- **Results**: Deciding whether a designated candidate is a winner in some **subgame-perfect equilibrium is PSPACE-complete** — partially resolving an open problem from Desmedt and Elkind [2010].
- **Significance**: Refines the boundary between tractable and PSPACE-hard voting-game reasoning — relevant to any preference-aggregation game (multi-agent ranking, in-game bazaars/marketplaces) where strategic abstention and limited ballot menus interact.
- **Link**: https://arxiv.org/abs/2609.24292

---

## 2. Game AI Bots, LLM Agents & NPC Simulation

### 2.1 Synthesizing Reactive Character Behaviors for Continuous Games via Programmatic Policy Search
- **Authors**: Maxim Gumin, Hsueh-Ti Derek Liu, Victor Zordan, Daniel Ritchie
- **Affiliation**: not stated (inferred — Brown University interactive-graphics group; Ritchie/Zordan) *(tentative)*
- **Venue**: To be presented at **SIGGRAPH Asia 2026** (arXiv 2609.24025, cs.AI), fresh Tue 22 Sep window
- **Key Innovations**: Reconciles the two poles of game AI — hand-authored behavior trees/state machines vs opaque neural RL controllers — by searching directly over a **domain-specific language for continuous-space game policies**. The DSL is built on reactive geometric decisions with higher-order constructs (e.g. **direction maximization**) that discretize continuous behavior space into enumerable programs; a large set of **synthesis antipatterns** prunes redundant forms while preserving behavioral coverage; **agentic sketching** combines bottom-up symbolic enumeration with top-down structure proposals from a coding agent.
- **Results**: On a benchmark of **14 continuous games (classic control → multi-agent football)**: pure enumeration is often more efficient than a coding agent alone, while the combined method substantially outperforms both — discovering editable, portable, and "often surprising" behaviors that designers could not have authored by hand.
- **Significance**: Programmatic policy search as a *practical authoring tool*: designers specify rewards, the system returns human-readable game-AI programs — the missing middle between scripting pipelines and neural black boxes for shipped game characters.
- **Link**: https://arxiv.org/abs/2609.24025

### 2.2 Do Chess Explanations Reflect Model Decisions? Behavioral and Token-Level Tests of LLM Reasoning Faithfulness
- **Authors**: Angelina Parfenova
- **Affiliation**: not stated (inferred — single-author LLM-abstraction study)
- **Venue**: Accepted to **BlackboxNLP at EMNLP 2026** (arXiv 2609.22245, cs.CL / cs.AI), fresh Tue 22 Sep window
- **Key Innovations**: Tests whether fluent LLM chess explanations are faithful to the actual decision, using chess's ideal measurability (fully observable board, enumerable legal actions, independently evaluable move quality). Across **200 Lichess endgame puzzles** combines move recoverability, decoder-side controls, and **token-level scoring of legal candidates**.
- **Results**: Unmasked explanations make moves easy to recover, but the advantage collapses once explicit move hints are removed; under strict masking explanations yield only small, decoder-dependent gains. **Token-level scoring shows irrelevant-but-plausible explanations actually alter move preferences** (random explanations reduce correct-move probability), and recognizable motifs inflate recoverability without improving correctness.
- **Significance**: Separates *linguistic plausibility*, *action consistency*, and *solution correctness* as distinct properties — a caution for every LLM game-bot that narrates its moves: fluent game commentary is not evidence of faithful reasoning.
- **Link**: https://arxiv.org/abs/2609.22245

### 2.3 Increasing Skill Level Recruits Deeper Attention Layers in a Frozen Chess Transformer
- **Authors**: David Litman
- **Affiliation**: not stated (inferred — chess transformer interpretability; built on chessformer-lens)
- **Venue**: arXiv preprint (2609.23917, cs.AI / cs.LG), fresh Tue 22 Sep window
- **Key Innovations**: Uses **Maia-3's Elo input** as a *skill dial on frozen weights* (no training) and ablates every attention head at every Elo from 700→2500 to trace how conditioning input redistributes computation.
- **Results**: (1) Higher skill pushes the **causal center of mass of computation deeper, monotonically**, for every piece and move type; (2) the migration is *much larger* for specific tactics (especially **knight forks**); (3) the migration = deeper heads get recruited for specialized computation while one shared shallow head holds a roughly constant contribution.
- **Significance**: Mechanistic demonstration that **skill-conditioning re-routes computation through depth** in a frozen game transformer — the interpretability substrate for controllable-strength game bots and for speculative "computation routing" patterns in larger models.
- **Link**: https://arxiv.org/abs/2609.23917

### 2.4 Deep Persona: A Psychologically Grounded Architecture and Evaluation Framework for Role-Playing Agents and Simulations
- **Authors**: Rotem Dror, Zohar Elyoseph, Yuval Haber, Elad Refoua, Oshrat Ayalon, Adir Solomon
- **Affiliation**: not stated (inferred — psychological-agent-assistive-technology group)
- **Venue**: arXiv preprint (2609.22255, cs.CL / cs.AI), fresh Tue 22 Sep window
- **Key Innovations**: Addresses shallow-character persona collapse over long interactions via a **three-layered hierarchy** — observable expression, latent beliefs, core motivational drives — governed by *scripted determinism* and *bounded agency* (a reactive engine behind a structured internal script). Ships a **reference-free evaluation framework** benchmarking dialogue naturalness against empirical human distributions using clinical psychological instruments + adversarial stress tests.
- **Results**: LLMs hit high *pragmatic* fluency but show **systematic limitations in emotional expression and joint attention**; structured personas produce interactions closer to human conversational behavior in the Deep-Persona case study.
- **Significance**: The "persona as state hierarchy, NPC as bounded reactive engine" architecture for long-horizon role-play agents — the controllability scaffold game NPCs and social simulations need to avoid persona drift.
- **Link**: https://arxiv.org/abs/2609.22255

---

## 3. Game Foundation Models, World Models & Game Agents

> The window's world-model marquee (CausalWM 2609.23184, ARPS 2609.23369, FireWorldBench 2609.23064) is sibling-covered — see the Continuity note header. Featured below is the **unclaimed world-model remainder**, which reads as a robustness/efficiency/representation day for the WM line.

### 3.1 Contrastive World Models
- **Authors**: Bonnie Li
- **Affiliation**: not stated (inferred — single-author model-based RL; Dreamer-family baseline)
- **Venue**: arXiv preprint (2609.22175, cs.LG / cs.AI / cs.CV), fresh Tue 22 Sep window
- **Key Innovations**: Pixel-reconstruction objectives drown in visually complex environments — irrelevant detail dominates the loss. **Contrastive World Models replace observation reconstruction with a Deep InfoMax-like lower bound** maximizing MI between state-action sequences and *local patch features* of future observations, keeping representations predictive of the future without reconstructing visually irrelevant details. Drops the pixel decoder entirely.
- **Results**: Matches Dreamer and a momentum-prediction baseline in the default setting, then **substantially outperforms both once distractors or natural video backgrounds are introduced**, while training more efficiently (no pixel decoder).
- **Significance**: Infomax-based dynamics learning as a principled route to *distractor-robust* model-based RL — a key property for transferring game/sim WM agents into visually noisy real or user-generated environments.
- **Link**: https://arxiv.org/abs/2609.22175

### 3.2 ConsistWorld: Evidence Routing for Consistent Multi-Agent World Models
- **Authors**: Qianxun Xu, Xianfang Zeng, Xinyao Liao, Wei Cheng, Gang Yu, Chi Zhang
- **Affiliation**: not stated (inferred — Tencent/VAST-aligned vision-world-model group; Zeng/Gang Yu) *(tentative)*
- **Venue**: arXiv preprint (2609.22641, cs.CV), fresh Tue 22 Sep window
- **Key Innovations**: Single-observer autoregressive video WMs break down for **multiple independent observers** — consistency must be maintained across controlled camera views and temporal gaps under causal streaming. **ConsistWorld generates camera-controlled video streams of a static scene from one shared image**; consistency = *evidence routing*: **Pose-Conditioned Memory Retrieval** picks relevant historical observations from all agents, **Visibility-Gated Peer Sharing** regulates concurrent peer-view info by historical coverage and view overlap.
- **Results**: Strong cross-time and cross-agent consistency with competitive generation quality across evidence-sharing cases and video-length / agent-number generalization; bounded active context for fixed agent count and retrieval budget.
- **Significance**: The first principled "split-screen world model" architecture — the multi-view NPC/periscope consistency mechanism needed when several game agents (or a spectator + players) must share one coherent generated world.
- **Link**: https://arxiv.org/abs/2609.22641

### 3.3 OnlineWM: Causality-Aware Active Online Learning for Effective World Modeling
- **Authors**: Yikun Miao, Fangqi Zhu, Quanxin Shou, Xiaoyi Pang, Zhengyang Yan, Junhao Li, Haodong Wang, Zicong Hong, Song Guo
- **Affiliation**: not stated (inferred — Hong Kong/China systems-AI group; Song Guo lineage) *(tentative)*
- **Venue**: arXiv preprint (2609.23753, cs.CV / cs.LG), fresh Tue 22 Sep window
- **Key Innovations**: Two structural failures in simulator-to-WM training: offline static data misaligns with the model's evolving error patterns, and observational-discrepancy objectives encourage **spurious correlations instead of action-effect causality**. **OnlineWM** introduces (1) **active online learning** — query the simulator for sequences targeting the model's current predictive weaknesses; (2) **causality-aware fine-tuning via counterfactual contrast** — same state, different actions, forcing the model to attribute transitions to the action rather than ambient drift.
- **Results**: Significantly improves action controllability and generalizes to unseen domains vs static-dataset baselines.
- **Significance**: Closes the loop between a WM's own error surface and its data supply — the online/self-improving pattern every game-world model trained on sim data should adopt to fight long-tail scenario blindness.
- **Link**: https://arxiv.org/abs/2609.23753

### 3.4 NeuIDO: Neural Intrinsic Dynamics Operator for Physics-Informed 4D World Models
- **Authors**: Jiajing Lin, Xin Zhang, Jianhua Sun
- **Affiliation**: not stated (inferred — physics-informed-generation group)
- **Venue**: Accepted by **ECCV 2026** (arXiv 2609.24313, cs.CV), fresh Tue 22 Sep window
- **Key Innovations**: Physics-informed 4D generation still relies on *manually imposed* dynamical assumptions. **NeuIDO formulates world modeling as a neural operator learning problem** and learns a unified *intrinsic dynamics representation* from visual observations via a two-stage training strategy — a generalizable mapping from the observation distribution to the intrinsic-dynamics distribution.
- **Results**: **Zero-shot dynamics inference directly from video**; aligns with complex real-world dynamics via few-shot adaptation; unifies intrinsic dynamics across diverse visual observations into one shared representation.
- **Significance**: Moves physics-informed 4D/WM generation from "hand-specified but neural-rendered physics" toward "**dynamics learned as an operator**" — the representational upgrade for game VFX-level world models that must generalize across object behaviors.
- **Link**: https://arxiv.org/abs/2609.24313

### 3.5 Robot World Models Are Not Invariant to How the Actions Are Written
- **Authors**: Ahmed Karim, Leon Chlon
- **Affiliation**: not stated (inferred — robot-learning dynamics group)
- **Venue**: arXiv preprint (2609.23252, cs.RO / cs.LG), fresh Tue 22 Sep window
- **Key Innovations**: A WM conditioned on actions silently inherits the *action parameterization* — absolute joint targets vs deltas relative to current state. Shows the inheritance is **catastrophic**: hand the identical commanded trajectory in the other encoding and the latent dynamics model collapses. Gives a **test separating a valid re-parameterization from a lossy summary or sensor swap** (the two encodings are mutually reconstructible at R²=0.996, so no information is lost — the defect lives in the action channel, which invariance literature for visual models never audits).
- **Results**: Retrieval degrades **2.6–13.4×** across three robot datasets / two morphologies; goal-conditioned action selection falls **53% → 15%**; on PushT the two beliefs about the same future are near-orthogonal (cos ≈ 0.067). **Objective-averaging (not output-averaging) repairs task performance**; a disagreement penalty closes worst-case agreement 0.78 → 0.995, but on PushT averaging alone fails.
- **Significance**: A parameterization-auditing primitive for every latent world model — "same intent, different syntax" is a real failure axis for game/sim policy conditioning, not a benign code detail.
- **Link**: https://arxiv.org/abs/2609.23252

---

## 4. Procedural Content Generation & Automated Game Design

### 4.1 OpenBlock: Constructive and Verified Content Generation for Adaptive Tile-Matching Games
- **Authors**: Jiang Jun
- **Affiliation**: not stated (inferred — single-author game-content research)
- **Venue**: arXiv preprint (2609.22177, cs.LG / cs.GT), fresh Tue 22 Sep window
- **Key Innovations**: Tile-matching serves hundreds of millions of players but its piece-generation controllers are proprietary with **no open platform for adaptive-difficulty research**. OpenBlock's core is a **dual-track content-generation architecture**: a deterministic rule-based generator (always available) + an optional learned generator, both gated by a **common verification gate** (exhaustive sequential-placement search) so the learned track can *never* degrade the constructive-feasibility guarantee. A self-play RL placement agent with per-shape placeability supervision diagnoses the genre's dominant failure: **long-bar pieces lose most legal placements at high board fill**.
- **Results**: Across **234,000+ self-play episodes**, the agent reaches a **35.6% win rate / 4,200 median score**; controlled simulation shows **33–56% of long-bar pieces have no legal placement** at 70–75% fill while spawn-difficulty distributions are statistically indistinguishable between wins/losses — **board-state degeneration, not content difficulty, drives late-game failure**. A **14-day online rollout (48,000 players)** lifts **day-1 retention +1.8 pp and session duration +7%** (CUPED-adjusted) over the rule track alone.
- **Significance**: The first open, *verified* adaptive-PCG testbed for match-three — quantifies live-A/B upside of a neural PCG track and hands the genre's failure modes to the RL/PCG community, not a vendor's closed telemetry.
- **Link**: https://arxiv.org/abs/2609.22177

---

## 5. Game & Agent Benchmarks / Evaluation Suites

### 5.1 GameReplica: A Benchmark for Black-Box Visual Game Replication by Vision-Language Agents
- **Authors**: Boyu Qiao, Zixin Tang, Xiaoshuai Hao, Wenbo Li
- **Affiliation**: not stated (inferred — vision-agent benchmark group) *(tentative)*
- **Venue**: arXiv preprint (2609.22308, cs.CV / cs.AI), fresh Tue 22 Sep window
- **Key Innovations**: Coding-agent benchmarks always hand over textual specs; **GameReplica asks a VLA coding agent to induce an entire game's rules black-box** — from screenshots + an action interface only — then produce a self-contained, runnable game replica verified by an external program. **125 tasks, 25 games, 5 core mechanism families**, each at five difficulty levels, covering the full perception → exploration → induction → reproduction → verification pipeline.
- **Results**: Current agents still struggle end-to-end: **best model (Claude Opus 4.8) 71.6% overall score, all others 4.0–42.9%**. Consistent pattern: **visual-fidelity scores ≫ implementation/rule-consistency** — agents faithfully copy pixels but fail mechanics; the L1→L5 gap crushes weaker agents while barely denting the best.
- **Significance**: The "looks right, plays wrong" failure quantified at benchmark scale — the evaluation scaffold for game-cloning, game-analytics, and visual rule-induction agents, plus a crisp statement that visual appearance is the easy 60% and played rules are the hard 40%.
- **Link**: https://arxiv.org/abs/2609.22308

### 5.2 Deciphering the Babel of Play: A Human-AI Collaborative Approach for Large-Scale Cross-Language Analysis of Game Reviews
- **Authors**: Zixiaofan Yang, Chang Xiao
- **Affiliation**: not stated (inferred — HCI/games-data group)
- **Venue**: arXiv preprint (2609.23104, cs.HC), fresh Tue 22 Sep window
- **Key Innovations**: First large-scale **cross-language** game-review analysis: from **17M Steam reviews across 30 languages and 2,000 top-selling titles**, selects 28 games with notable cross-language rating patterns, then applies LLM-assisted content analysis to **442,162 reviews in 17 languages** with human-guided codebook + interpretation.
- **Results**: Community language groups prioritize and evaluate *different aspects* — narrative expectations, mechanics/stability, localization quality, cultural proximity, perception of devs/publishers — plus rare cases of cross-language consensus.
- **Significance**: An empirical map of why the same game scores differently across regions — the data foundation for player-modeling and cross-market game-design decisions, and a reusable human-AI multilingual content-analysis protocol.
- **Link**: https://arxiv.org/abs/2609.23104

---

## 6. Industry Game AI, Sim-to-Real & On-Device Inference

### 6.1 AquaOrbit: Sim-to-Real Reinforcement Learning for Underwater Target Orbiting under Intermittent Visual Feedback
- **Authors**: Kanzhong Yao, Jinyi Leng, Hao Zhang, Zhe Sun, Xuelong Li
- **Affiliation**: not stated (inferred — Xuelong Li industrial/academic RL line) *(tentative)*
- **Venue**: arXiv preprint (2609.24054, cs.RO), fresh Tue 22 Sep window
- **Key Innovations**: Intermittent visual loss wrecks target-relative feedback during underwater orbiting. **AquaOrbit** = an RL controller + **recovery module** that latches line-of-sight/roll/depth references during detection loss to stabilize and reacquire; trained in Isaac Sim with dynamics/observation/vision-loss randomization, deployed **without retraining**.
- **Results**: **20/20 trial completions** (static and moving targets) zero-shot in Gazebo/ROS2 under a different physics engine and perception perturbations; **−46% mean line-of-sight error** vs PID visual-servoing with recovery at comparable path accuracy; removing the recovery module drops completion to 9/20. Zero-shot physical deployment demonstrates elliptical/figure-eight/variable-depth paths (latter two **absent from training**), survives 8s manual occlusions, and reacquires within 2.5s.
- **Significance**: Sim-to-real deceptions (unseen trajectories, unseen physics engine) handled by a *recovery-memory* design — the robustness playbook for any game/sim policy that must keep performing through sensor dropout and latent-vision failures.
- **Link**: https://arxiv.org/abs/2609.24054

---

## 7. Related RL Techniques (Model-Based, Reward Shaping, Imitation)

### 7.1 Prioritized Rollouts for Efficient World Model-based Vision-Language-Action Policy Optimization
- **Authors**: Yifei Sheng, Haoxiang Ren, Zhilong Zhang, Haonan Wang, Runjie Xu, Yihao Sun, Nan Tang, Zhichao Wu, Lei Yuan, Haoxin Lin, Yang Yu
- **Affiliation**: not stated (inferred — Nanjing University deep-RL group; Yang Yu lineage) *(tentative)*
- **Venue**: arXiv preprint (2609.22879, cs.LG), fresh Tue 22 Sep window
- **Key Innovations**: WM-based VLA RL treats all rollout states as equal, but **policy uncertainty concentrates at a small subset of decision-sensitive states**. **U-GROW** is a lightweight, plug-and-play sampling layer that redirects model rollouts to high-uncertainty (high-improvement-potential) states by changing only the branched-start distribution — no objective change.
- **Results**: Efficiency/effectiveness gains on simulated and real-world manipulation tasks across existing MBRL pipelines.
- **Significance**: "Spend your imagination budget where the policy is unsure" — a zero-friction inside-investment pattern every world-model RL post-training loop (including game-bot skill-refinement) can adopt for cheaper policy gains.
- **Link**: https://arxiv.org/abs/2609.22879

### 7.2 Imagine-RL: Residual-Confidence-Guided Cross-Attention for World-Model-Augmented VLA Reinforcement Learning
- **Authors**: Kejia Hu, Wentong Zhai, Bo Zhao, Shuai Liang
- **Affiliation**: not stated (inferred — VLA post-training group)
- **Venue**: arXiv preprint (2609.24033, cs.RO), fresh Tue 22 Sep window
- **Key Innovations**: Noise-space VLA RL critics ignore future consequences of contact. **Imagine-RL** augments them with a frozen **visual-torque latent world model (VTLWM)** that autoregressively predicts compact future representations per candidate action chunk; a current image-state-action query attends to observed history + predicted futures, with **previous-window prediction residuals as token-wise confidence priors** suppressing unreliable future tokens. VLA and VTLWM both remain frozen.
- **Results**: Across four real-robot tasks (50 trials each), using only **100 RL trajectories**, improves average success by **+23.6% over DSRL and +60% over VLA baselines**.
- **Significance**: The "imagine before you judge" pattern for RL critics — future-imagination as critic input is generalizable to game agents that must evaluate the *downstream consequences* of long action chunks (combo chains, strategy sequences).
- **Link**: https://arxiv.org/abs/2609.24033

### 7.3 BEACON: Belief-Enabled Adaptive CONtrol for Imitation Learning under Uncertainty
- **Authors**: Moonyoung Lee, Soumojit Bhattacharya, George Kantor, Oliver Kroemer
- **Affiliation**: not stated (inferred — Carnegie Mellon Robotics Institute; Kantor/Kroemer)
- **Venue**: arXiv preprint (2609.22730, cs.RO), fresh Tue 22 Sep window
- **Key Innovations**: In partially observable IL, conditioning on raw history produces **state aliasing** (identical observations from different hidden states → conflicting action labels). **BEACON** replaces raw history with a structured representation of the hidden state via **Bayesian belief** that exposes both the most-likely estimate and residual uncertainty, conditioning a diffusion policy on it — letting the policy **implicitly modulate exploration vs exploitation from belief uncertainty** with no explicit mode-switching or reward shaping.
- **Results**: On a continuous tactile cornstalk-alignment belief and a discrete latched-door categorical belief, the belief-conditioned policy **substantially outperforms the observation-only baseline and approaches privileged ground-truth**; ablations show exploration adapts to belief uncertainty at inference.
- **Significance**: "Structured doubt as policy input" — the receivable pattern for NPCs/bots that must act decisively in partially observed environments, and for IL pipelines that currently throw raw noisy histories at policies.
- **Link**: https://arxiv.org/abs/2609.22730

---

## Runner-ups Worth a Look (grep-verified unclaimed)

- **2609.23875** VISTA — attention-based MARL for space-situational-awareness sensor tasking with catalogue-size-independent observation/action spaces (entity-centric attention + pointer decoding): 31.2% faster catalogue recovery, **−97.5% five-hour uncertainty** vs strongest classical baseline, zero-shot scaling to 20,000 objects. The "variable-scale MARL tasking" architecture reusable for fleet/allocation games. https://arxiv.org/abs/2609.23875
- **2609.22588** Seeing is not Enough — distinguishes *perceptual failure* (evidence unrecognized) from *process failure* (recognized evidence doesn't constrain the decision) in VLMs via **VPAC-Bench** (9 real-image process families) with State-Relevance-Target interventions; process failure is widespread even in models that enumerate evidence correctly. The "sees but won't act" metric for game/agent VLMs. https://arxiv.org/abs/2609.22588
- **2609.23118** Verti-WM — physics-aided *exteroceptive* off-road world model fuses frozen rigid-terrain Transformer + neuro-symbolic terramechanics for deformable terrain; **−34.6% prediction error** over data-driven and −21.7% over physics baselines, RL within the WM matches simulator training at **23.6× lower compute**, real-world 80% success vs 40% sim-to-real. The "hybrid data+physics world model" blueprint for off-road/terrain simulation. https://arxiv.org/abs/2609.23118

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL, Multi-Agent Learning & Game Theory | 4 |
| Game AI Bots, LLM Agents & NPC Simulation | 4 |
| Game Foundation Models, World Models & Game Agents | 5 |
| PCG & Automated Game Design | 1 |
| Game & Agent Benchmarks / Evaluation Suites | 2 |
| Industry Game AI, Sim-to-Real & On-Device Inference | 1 |
| Related RL Techniques | 3 |
| **Total featured papers** | **20** |

## Cross-references (covered by 09-22 sibling digests, not re-featured)

- 2609.23184 — CausalWM: 16B embodied causal-CoT world model, TriWorldBench Top-1 — [arxiv-daily 09-22](../2026-09-22/arxiv-daily.md)
- 2609.23369 — ARPS: action-relevant predictive states for generation-free world action models, 99.2% LIBERO — [arxiv-daily 09-22](../2026-09-22/arxiv-daily.md)
- 2609.23064 — FireWorldBench: coupled-field fire-dynamics physical-intelligence benchmark — [arxiv-daily 09-22](../2026-09-22/arxiv-daily.md)
- 2609.23043 — Structured Knowledge Trees: LLM-driven detective-game narrative reliability, −64.78% critical hallucinations — [arxiv-daily 09-22](../2026-09-22/arxiv-daily.md)

## Key Themes

1. **Game theory had a proof day.** Optimistic Hedge gets a horizon-independent (constant) individual regret bound with a Nonconstructive-Noetherianity argument (2609.22839); generic ω-recognizable preferences pin SPE existence to EXPTIME-complete (2609.22906); restricted-ballot sequential plurality voting joins PSPACE-complete (2609.24292). This window's GT layer is about *certifying what no-regret and equilibrium reasoning can and cannot compute* — exactly the guarantees game-RL needs before it relies on them in production exploiters.

2. **Trust's environment binds.** The N-player Q-learning trust game (2609.24493) shows environmental feedback carries past collective outcomes into future payoffs, and that *perceived state tiering* is a control knob for cooperation collapse — connecting "reward is learned, environment is endogenous" into a single testbed, the social-economies cousin of last window's cooperation line (2608.20016).

3. **World-model science moved to robustness auditing.** WMs are not invariant to action parameterization (2609.23252 — a 2.6–13.4× silent collapse + a repair test); Contrastive WMs remove pixel-reconstruction nuisance (2609.22175); multi-observer consistency becomes evidence-routing (2609.22641); OnlineWM learns from its own error surface over fixed datasets (2609.23753); NeuIDO turns dynamics into a learned operator (2609.24313, ECCV). The field is auditing *what the WM actually trained on* rather than adding scale.

4. **Programmatic and explainable game AI is ascendant.** Reactive continuous-game behaviors as human-readable programs via programmatic policy search + agentic sketching (2609.24025, SIGGRAPH Asia 2026) gives designers editable, surprising characters; on the LLM side, chess becomes the arena for both *unfaithful* explanations (2609.22245, BlackboxNLP) and *depth-routed* computation (2609.23917). Game AI is converging on auditable, editable, mechanism-transparent controllers.

5. **Black-box induction is the new hard benchmark.** GameReplica (2609.22308) documents that VLAs clone visual appearance far better than played rules (71.6% best, rule-consistency the binding constraint) — the precise failure report for game-cloning/rule-induction agents and a benchmark to watch.

6. **Dedup discipline note:** all 23 IDs (20 featured + 3 runner-ups, 2609.22175–2609.24493) were grep-verified **0 hits in `wiki/`** and sit outside every 09-21 and 09-22 sibling-claimed set; the window's world-model marquee and detective-game LLM-NPC engine are cross-referenced rather than duplicated.