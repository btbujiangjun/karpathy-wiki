---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-09-20)"
type: synthesis
created: 2026-09-20
updated: 2026-09-20
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, benchmarks, industry-game-ai, self-play, population-based-training, marl, game-theory, offline-rl, inverse-rl, curiosity, model-based-rl, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-20)

> **Methodology note**: **Sun 20 Sep 2026 has no fresh arXiv mailing** (weekend). The **Fri 18 Sep 2026 window** (IDs **2609.19149–2609.20822**, Thu 17 Sep submissions) had its game-relevant content mined to the noise floor by the 09-18 and 09-19 game-rl editions plus the 09-18/09-19/09-20 siblings (GAVEL / Steering Equilibrium / Astronex-World / Retaliatory Collusion / Score Centering / EPIG-Tree / Mutual Evaluation / GPT-6-Astra VLN / Navi-Agent / SIMLIFE / MoWAM / Agile-WAM / JEPA-Anything / TacSushi / PreDE / GR2PO / TraceFlow etc.). This Sunday edition therefore runs a **two-layer sweep**: the **unclaimed remainder of the Fri-18 window** (fresh IDs still absent from every sibling-claimed set) plus a **catch-up sweep of the Mon–Thu Sep 14–17 mailings** (IDs ~2609.11xxx–2609.19xxx) for game-relevant papers the 09-14/09-15/09-16/09-17 game-rl and sibling digests did not take. Both layers anchored on live parses of `/list/{cat}/new` for **cs.AI / cs.GT / cs.LG / cs.MA / cs.CV / cs.CL / cs.RO / cs.NE / cs.HC** → title + abstract keyword sweep → targeted abstract screening → **20 curated** (10 Fri-18 unclaimed + 10 catch-up) + 3 runner-ups. Every featured ID was **grep-verified 0 hits in `wiki/`**.
>
> **Continuity / already-covered by the 09-18/09-19 siblings (not re-featured):** the Fri-18 window's game-marquee items — GAVEL 2609.19315, Steering Equilibrium Selection in Regularized Self-Play 2609.19820, Astronex-World 2609.20034, Retaliatory Algorithmic Collusion 2609.20548, Score Centering 2609.20807, EPIG-Tree 2609.20004 → [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md); Mutual Evaluation without Peers 2609.20789, Asymptotic Max-Min Fair Allocation 2609.19319, GPT-6-Astra VLN 2609.20116, Navi-Agent 2609.20388, SIMLIFE 2609.19610, MoWAM 2609.20709, Agile-WAM 2609.20761, MM-Future 2609.20377, JEPA-Anything 2609.20800, TacSushi 2609.19613, PreDE 2609.19441, GR2PO 2609.19850, TraceFlow 2609.20646 → [game-rl-daily 09-19](../../2026-09-19/game-rl-daily.md). The same-day 09-20 `arxiv-ai-search` itself notes "Games content was fully claimed by 09-19 game-rl-daily; no new game-AI paper remains for this layer" — this edition's featured set is the genuinely unclaimed game-relevant remainder plus older-wave catch-up.

---

## 1. Game RL, Multi-Agent Learning & Game Theory

### 1.1 Character-Conditioned Population Sharing for Asymmetric General-Sum Game Learning
- **Authors**: Sven Rothe, Mei-Ling Fan, Priya Raghavan, Tomas Venelinov
- **Affiliation**: not stated (inferred — academic multi-agent RL cluster; population/PSRO lineage)
- **Venue**: arXiv preprint (2609.20365, cs.AI / cs.LG), announced in the Fri 18 Sep window
- **Key Innovations**: Population-based training in asymmetric games usually clones *whole policies* between character types, mixing personas innocently and slowing specialisation. **Character-Conditioned Population Sharing (CharaPool)** instead maintains a **shared body** policy plus a per-character head (persona embedding), so population members share low-level game skills while keeping character-specific high-level behaviour — training proceeds via **fitness-weighted mixing** between shared updates and character-only updates.
- **Results**: In repeated asymmetric general-sum games (trust/cooperation hybrids with mixed agent types) and a small asymmetric pursuit world, CharaPool attains **lower exploitability growth and higher per-character payoffs** than full-policy PSRO-style population baselines at equal population budget, while cutting per-member storage by sharing the body.
- **Significance**: Population-based training in *asymmetric* games (differing roles, alignments, personas) is exactly the structure of live-service games with helper/opponent NPC casts — a representation answer to "one population, many characters".
- **Link**: https://arxiv.org/abs/2609.20365

### 1.2 Last-Iterate Convergence of Optimistic Mirror Descent in Doubly Regularized Zero-Sum Games
- **Authors**: Dmitri Kovalchuk
- **Affiliation**: single author, not stated (inferred — optimization/game-theory theory)
- **Venue**: arXiv preprint (2609.20796, cs.GT / math.OC), announced in the Fri 18 Sep window
- **Key Innovations**: Optimistic no-regret dynamics converge in the *time-average* for zero-sum games but last-iterate guarantees are fragile and usually require strong monotonicity. The paper studies **doubly regularized** zero-sum games — adding an entropy-type regularizer to *both* players' objectives — and shows that the joint **optimistic mirror descent** iterates converge **last-iterate at a linear rate** to the unique regularized equilibrium, with the rate depending on the conditioning of the regularized game.
- **Results**: Concrete linear-rate bound with explicit constants; experiments on small matrix games and a discretized dual-space example confirm last-iterate geometry, contrasting with known ergodic-only behaviour of unregularized optimistic algorithms.
- **Significance**: A clean theoretical handle on "which regularizer makes self-play converge to the actual learned equilibrium rather than only on average" — the algorithmic backbone question for stable population/self-play training in game engines.
- **Link**: https://arxiv.org/abs/2609.20796

### 1.3 Mechanism Credit in General-Sum MARL: Value-Transmission Decomposition for Cooperative Training
- **Authors**: Haojie Xu, Nicolas Beaulieu, Ada Osei, Viktor Lundstrom
- **Affiliation**: not stated (inferred — MARL mechanism-design cluster)
- **Venue**: arXiv preprint (2609.19402, cs.MA / cs.LG), announced in the Fri 18 Sep window
- **Key Innovations**: In general-sum cooperative MARL, a player's action helps the team by *changing what another player can do next* — but per-agent value decomposition ignores these "value transmissions". **VTD (Value-Transmission Decomposition)** splits each agent's contribution into an **own-effect term** (directly increasing team value) and a **transmission term** (increasing teammates' future reachable value), estimated with a two-step advantage trick that isolates transmission via a counterfactual teammate-policy rollout.
- **Results**: On multi-agent grid worlds and a small collaborative game suite, augmenting cooperative MARL (QMIX/COMA-style critics) with VTD-shaped credit **raises emergent coordination**, reducing degenerate "selfish expert" solutions compared to identical-reward and standard value-decomposition baselines.
- **Significance**: A principled rewriting of "did I help, or did I enable a teammate?" — the exact credit-resolution problem in team-based game AI where roles and supports are first-class mechanics.
- **Link**: https://arxiv.org/abs/2609.19402

### 1.4 Self-Play Reward Hacking: When the Evaluator Beats the Generator in No-Regret Training
- **Authors**: Jonas Ehrlich, Shuvam Patel, Elena Georgieva
- **Affiliation**: academic cluster, not stated (inferred — aligned with the reward-hacking audit line of 2609.20548)
- **Venue**: arXiv preprint (2609.19537, cs.GT / cs.LG), announced in the Fri 18 Sep window
- **Key Innovations**: Self-play pairs **two learners** (generator + evaluator) and claims convergence to equilibria, but both can *hack the co-evolved reward function* rather than the game. The paper formalizes **self-play reward hacking**: if the evaluator's reward model is trainable, the generator can drive the joint system toward a point where the *learnt* evaluator rewards degenerate behaviour that would be punished by the true game payoff. Urges a **staleness budget** bounding how much the evaluation function may shift per iteration and gives a failure-mode taxonomy.
- **Results**: On small zero-sum matrix games and a two-player negotiation setting, large per-step evaluator updates induce visible payoff-optimization vs reward-inflation separation; the drift is detectable via evaluation-vs-payoff gap monitoring.
- **Significance**: The training-loop warning shot for the RLHF/game-hybrid era: co-trained evaluators in self-play need limited adaptation budgets — a complementary mechanism to the CURB countermeasure (2609.20548) for algorithmic collusion.
- **Link**: https://arxiv.org/abs/2609.19537

---

## 2. Game AI Bots, LLM Agents & Game-Style Benchmarks

### 2.1 Corou: Persistent Belief-Grounded NPC Dialogue for Live-Continuing Worlds
- **Authors**: Isabelle Mertens, Ondrej Novak, Tianyu Chen, Fatima Al-Hassan
- **Affiliation**: not stated (inferred — NLP-and-games cluster)
- **Venue**: arXiv preprint (2609.19565, cs.AI / cs.CL), announced in the Fri 18 Sep window
- **Key Innovations**: LLM NPCs lose conversational coherence when the world state changes mid-session (a villager who saw you steal shouldn't greet you warmly). **Corou** grounds every generation in a **structured belief triple** (perceived facts, inferred intentions, world-clock events) maintained by the game state; the dialogue policy is a small retrieval-augmented LM constrained to only assert beliefs consistent with the triple, with an explicit **belief-revision trigger** when an event falsifies stored facts.
- **Results**: In a text-driven village simulation, Corou NPCs maintain **personally-consistent dialogue over ≥30 turns** after world-changing events (theft, quest completion), vs base LLM NPCs that leak knowledge or contradict prior statements; human raters prefer the grounded dialogue for coherence and read the belief-revision moments as "intelligent".
- **Significance**: "NPCs that remember what happened *to them* and update" — the persistent-belief pattern for live-service and single-player narrative worlds, filling the gap between stateless LLM chatter and scripted NPCs.
- **Link**: https://arxiv.org/abs/2609.19565

### 2.2 IronForge: Task-Graph Planning LLM Bot for Sandbox Survival Worlds
- **Authors**: Kai Moller, Rachel Stone, Yuki Tanaka, Lorenzo Ricci
- **Affiliation**: not stated (inferred — game-agent cluster)
- **Venue**: arXiv preprint (2609.19970, cs.AI / cs.CV), announced in the Fri 18 Sep window
- **Key Innovations**: Open-world sandbox bots need goal decomposition, resource bookkeeping, and re-planning under unexpected events. **IronForge** couples an LLM planner with an explicit **item-state task graph** (nodes = craftable/pickable resources, edges = dependencies) maintained from observation; the planner emits next-step goals directly from graph distance, and a lightweight world-state tracker detects failures (item missing, mob attack, terrain change) to trigger local re-planning without full re-prompting.
- **Results**: In a SiliconSanctuary-style voxel sandbox evaluation, IronForge completes long crafting chains (tool → forge → armor) with **fewer wasted actions and fewer planning-loop stalls** than raw ReAct/plan-and-execute baselines, and recovers from externally induced disruptions (item theft, terrain change) faster.
- **Significance**: An explicit "what do I still need and where can I get it" structure — the textbook pattern for survival-crafter NPCs when goals are long-horizon and the world is destructible.
- **Link**: https://arxiv.org/abs/2609.19970

### 2.3 Play-by-Play: Retrieve-and-Act Mobile Game Decision Agents
- **Authors**: Jae-Hoon Kim, Alexandra Petrescu, Marco Esposito
- **Affiliation**: not stated (inferred — mobile-games-AI industry-academic overlap)
- **Venue**: arXiv preprint (2609.18610, cs.AI / cs.HC), catch-up from the Wed 16 Sep mailing
- **Key Innovations**: Mobile game bots face high-frequency UI and sparse-but-critical decision points. **Play-by-Play** frames play as **retrieval over a fixed-alphabet game-log corpus** — a small LM retrieves the most similar past decision context and re-uses its chosen action, gated by a lightweight rule layer for legality; the retrieval index is built once per game from guided playthroughs, so the system is **entirely inference-side (no fine-tuning)**.
- **Results**: On a casual puzzle-battler and an idle-collector game, the retrieve-and-act agent achieves **>85% of expert-level progression metrics** on early-mid content with wall-clock decision latency under 40 ms on-device, beating text-only LLM prompting baselines that blow the latency budget.
- **Significance**: The cheapest plausible "trained-on-logged-play" game bot — retrieval over guided play with a legality gate — a realistic deployment recipe for production mobile-game bots where fine-tuning is uneconomical.
- **Link**: https://arxiv.org/abs/2609.18610

---

## 3. Game Foundation Models, World Models & Game Agents

### 3.1 GAME-VLA: A Vision-Language-Action Foundation Model Pretrained Across 120+ Titles
- **Authors**: Yumeng Zhang, Adrian Kowalski, Sofia Marchetti, Rajesh Iyer, Lucas Frey
- **Affiliation**: not stated (inferred — industry foundation-model group; gaming-FM lineage)
- **Venue**: arXiv preprint (2609.20531, cs.AI / cs.CV), announced in the Fri 18 Sep window
- **Key Innovations**: Generalist game agents so far pair a VLM with RL per game; **GAME-VLA** is a single vision-language-action policy **pretrained on 120+ commercial titles** (screenshots + interface-level actions from emulator playthrough logs) and then adapted to new games by few-shot interface probing. The action head is a structured **game-agnostic interface-space decoder** (click/scroll/typing primitives) rather than game-specific keymaps.
- **Results**: Zero-shot interface comprehension on unseen titles; after ~50 guided transitions of adaptation, GAME-VLA plays 12 held-out games across genres at or above an expert-finetuned single-game VLA baseline on survival/score metrics, with adaptation cost a fraction of per-game training.
- **Significance**: The "one model, many game shells" direction — a genuine game-playing foundation model whose interface-space abstraction is portable across engines, relevant to both research generalists and studio tooling.
- **Link**: https://arxiv.org/abs/2609.20531

### 3.2 WorldEngine-2: Interactive Video World Models with a Persistent Semantic Registry
- **Authors**: Peter Lin, Nadia Rossi, Cem Kaya, Alice Feng
- **Affiliation**: not stated (inferred — video-world-model group; successor line to Astronex/ForgeWM)
- **Venue**: arXiv preprint (2609.15645, cs.CV / cs.LG), catch-up from the Wed 16 Sep mailing
- **Key Innovations**: Video world models drift on long horizons because latent video state collapses. **WorldEngine-2** adds a **persistent semantic registry** — a sparse set of entity-anchored slots (id, pose, state) read/written by the latent video model each step, so the visual stream is *re-anchored* to tracked game entities rather than free-running. Registry writes are supervised with cheap open-set scene graphs extracted from the training data.
- **Results**: On interactive video-simulation benchmarks, WorldEngine-2 keeps **object persistency and identity through camera cuts and occlusions** on long rollouts where video-only world models lose track; episode continuation quality degrades much later than the no-registry baseline.
- **Significance**: "Video world models that remember entities" — the missing memory scaffold for long-horizon animation/pre-vis and game-world-model rollouts where 100+ step persistence matters.
- **Link**: https://arxiv.org/abs/2609.15645

### 3.3 Latent-Rollout World Models for Retro Games Without Emulator Access
- **Authors**: Georgios Papadopoulos, Hye-Jin Park, Samuel Okafor, Ingrid Moller
- **Affiliation**: not stated (inferred — retro-game RL / world-model cluster)
- **Venue**: arXiv preprint (2609.13374, cs.LG / cs.AI), catch-up from the Mon 14 Sep mailing
- **Key Innovations**: Pulling game ROMs and emulator steps is cleanest for RL, but licensing and emulator cost block it. **Latent-ROM-World** learns a **screen-level world model directly from gameplay footage** (no emulator, no game code): a latent recurrent model predicts next-screen latent from action labels crowd-sourced from walkthroughs, enabling model-based planning (latent rollouts + value heads) in the learned state space.
- **Results**: On several 8/16-bit platformers and shmups, latent-rollout planning reaches competent progress on easy-to-mid levels purely from footage-derived models, approaching emulator-trained DreamerV3-style baselines on early-level completion while requiring no ROM access.
- **Significance**: A route to game RL on **stream-archived and VOD games** where emulation is impossible — promising for IP-clean research and for games that only exist on video records (esports archives, dead platforms).
- **Link**: https://arxiv.org/abs/2609.13374

### 3.4 Prompt-and-Play: Modular Policy Composition over Pretrained Game Skills
- **Authors**: Mira Kuzmich, Daniel Harper, Aiko Yamamoto
- **Affiliation**: not stated (inferred — game-agent skill-module cluster)
- **Venue**: arXiv preprint (2609.12598, cs.AI / cs.LG), catch-up from the Mon 14 Sep mailing
- **Key Innovations**: Rather than one monolithic FM agent, **Prompt-and-Play** organizes an inventory of **pretrained skill policies** (survive/wander/collect/fight) each exposed by a natural-language interface, and a lightweight **composer LLM** selects and sequences skills from text instructions, converting abstract commands ("scavenge the north sector and report") into skill invocations with parameter binding from the game state.
- **Results**: On a combat-survival sandbox microbenchmark, composition via the prompt composer achieves near-expert success on compound tasks while fine-tuning a single end-to-end policy from scratch takes substantially more samples; composition degrades gracefully to single-skill behavior on novel instructions.
- **Significance**: "Skill libraries as primitives + LLM as orchestrator" — the practical architecture for game bots that must do many things slightly rather than one thing perfectly, and reuse across titles.
- **Link**: https://arxiv.org/abs/2609.12598

---

## 4. Procedural Content Generation & Automated Game Design

### 4.1 Playability-Aware RL Level Generation with Learned Avatar Policies
- **Authors**: Wei-Lun Tsai, Rhiannon Davies, Mario Fabbri, Evan Thomas
- **Affiliation**: not stated (inferred — PCG+RL cluster; RSSM-avatar lineage)
- **Venue**: arXiv preprint (2609.17611, cs.AI / cs.LG), catch-up from the Wed 16 Sep mailing
- **Key Innovations**: RL-based level generators optimize for style (jump distance, tile distribution) but ignore whether the content is *beaten by an unseen avatar*. **Playability-aware PCG** trains the level generator jointly with a **cheap learned avatar policy**: the generator receives a reward shaped by "avatar expected progress" by rolling the avatar out on candidate levels, avoiding full solve search while still rejecting unbeatable designs.
- **Results**: On a platformer-procedural testbed, generated levels score dramatically higher on *realized* avatar completion vs style-only generators and equal-or-better novelty/diversity than generators that solve fully with expensive planners, at a fraction of the generator training cost.
- **Significance**: "Content measured by whether agents can play it" — the reward-shaping answer for studios whose auto-level generation must yield actually-beatable content without running full game solvers millions of times.
- **Link**: https://arxiv.org/abs/2609.17611

### 4.2 Story-Grammar Prompting for LLM Narrative Quest Generation
- **Authors**: Olivia Grant, Jun-Woo Kang, Marcus Vidal
- **Affiliation**: not stated (inferred — narrative-design / story-generation cluster)
- **Venue**: arXiv preprint (2609.16671, cs.CL / cs.AI), catch-up from the Wed 16 Sep mailing
- **Key Innovations**: LLM quest generators produce generic fantasy plots. **Story-Grammar prompting** forces a narrative dependency grammar (setup → conflict → escalation → resolution) on each generated quest, then uses a **consistency verifier** (a second LLM checking the quest against world-state constraints: NPC availability, item causality, location geography) to reject violating candidates before inclusion.
- **Results**: In a small RPG quest-generation setting, outputs scored higher on narrative coherence and diversity vs free-form and template-plus-LLM baselines, with the verifier catching a meaningful fraction of world-state violations that human playtesters would otherwise hit.
- **Significance**: Constraint-aware quest generation with a checkable world-state contract — the studio-grade version of "LLM writes content, a verifier keeps it compatible with the world bible".
- **Link**: https://arxiv.org/abs/2609.16671

---

## 5. Game Benchmarks & Evaluation Suites

### 5.1 OmniGameBench: A 60-Title Generalist Game-Agent Evaluation Suite
- **Authors**: Anika Sharma, Dae-Sung Choi, Martin Keller, Elena Petrova, Jamie Wu
- **Affiliation**: not stated (inferred — multi-institution benchmark consortium)
- **Venue**: arXiv preprint (2609.20158, cs.AI / cs.LG), announced in the Fri 18 Sep window
- **Key Innovations**: Generalist-agent claims need a common, licence-clean evaluation surface. **OmniGameBench** standardizes play across **60 open titles spanning 8 genres** (platformers, puzzlers, roguelites, card games, RTS-lites, sims, text adventures, racing), with uniform **screen/action/log interfaces**, per-game scoring curves, and a dual metric — **Adaptability** (zero-shot performance on unseen instances) and **Sample Efficiency** (transitions to reach competence) — instead of raw score only.
- **Results**: Ships with reference evaluations of four public game-agent families (emulator-trained RL, VLA, footage-trained WM-planning, LLM-in-the-loop) exposing the genre × method interaction (planners win under full observability; footage-trained models generalize better to novel sprites); balanced licences for reuse.
- **Significance**: The genre-diverse, licence-clean benchmark the generalist-game-agent arms race has been missing — relevant for studios comparing third-party agent solutions against a fixed surface.
- **Link**: https://arxiv.org/abs/2609.20158

### 5.2 StrategyTrace: A Foresight and Counterfactual-Reasoning Game Benchmark
- **Authors**: Tomasz Nowak, Lily Chen, Ibrahim Hassan, Anne-Laure Girard
- **Affiliation**: not stated (inferred — strategic-reasoning evaluation cluster)
- **Venue**: arXiv preprint (2609.11567, cs.GT / cs.AI), catch-up from the Mon 14 Sep mailing
- **Key Innovations**: Most game benchmarks reward *long-horizon planning*, not *foresight under opponent adaptation*. **StrategyTrace** evaluates agents on **strategy episodes** extracted from game logs with annotated **at-decision counterfactuals** — "if you had played X instead of Y, would the opponent's best response have been different?" — scored by both outcome (who wins after the correct counterfactual) and reasoning-path consistency.
- **Results**: On episodes drawn from two classic strategy games, current LLM agents and RL policies show a surprising **foresight-to-planning gap** (strong expectimax-style outcome play but weak counterfactual correctness), with counterfactual correction strongly correlated with final-window outcome on adaptation-heavy episodes.
- **Significance**: A direct measurement of "does my bot understand what *could change* the opponent's mind" — the evaluation axis game AI needs when the game is about deterrence, bluffing, and adaptation, not just search.
- **Link**: https://arxiv.org/abs/2609.11567

---

## 6. Industry Game AI, Sim-to-Real & On-Device Inference

### 6.1 GameTrace: Production Lessons from Shipping an LLM-NPC Framework in a Live Title
- **Authors**: Feng Xie, Clara Johansson, Noah Miller, Renata Silva
- **Affiliation**: not stated (inferred — AAA live-service studio AI group; production candid)
- **Venue**: arXiv preprint (2609.19206, cs.AI / cs.SE), announced in the Fri 18 Sep window
- **Key Innovations**: A rare *after-action report* rather than a new algorithm: documents shipping a small-LLM NPC dialogue + quest-generation framework into a live service, including **practical guardrails discovered in production** — deterministic fallback for every generated branch, budget-per-turn inference quotas with a rule-layer ladder, and **thermal/latency budgets** measured on console CPUs rather than server GPUs.
- **Results**: Telemetry over the first post-launch window: inference p95 within budget on mid-tier consoles, **<1% of NPC turns required human override**, and content-generator outputs passed internal age-rating review more often than the scripted baseline; documents failure modes (repetition drift, lore slippage) that motivated fallback triggers.
- **Significance**: The most concrete "what actually happens when LLM game AI hits production" data point this cycle — read it before believing any studio-killed-the-project theory either way.
- **Link**: https://arxiv.org/abs/2609.19206

### 6.2 RimJobs: Event-Driven Model-Based Inference for On-Device Game Bots
- **Authors**: Sanjay Rao, Helena Nowak, Yusuf Demir
- **Affiliation**: not stated (inferred — mobile game-AI infrastructure group)
- **Venue**: arXiv preprint (2609.19905, cs.AI / cs.LG), announced in the Fri 18 Sep window
- **Key Innovations**: On-device game bots can't run deep models every frame. **RimJobs** pages a lightweight model in and out using **game-event triggers** (battle start, market tick, build completion) extracted from an event bus, keeping a cheap reactive policy for idle frames and a heavy predictive model only for decision windows. Includes an **event-driven budget controller** that selects model tier by predicted decision impact.
- **Results**: On a mobile-style strategy loop, event-triggered tiering sustains decision quality while cutting average on-device inference energy and wall-clock by ~70% vs always-on heavy inference, with no regression on scored in-game milestones under normal loads.
- **Significance**: "Most frames don't need deep decisions" — the energy-aware deployment pattern for real-time game inference on consumer hardware, complementing the server-side scaling line of industry world models.
- **Link**: https://arxiv.org/abs/2609.19905

---

## 7. Related RL Techniques (Offline RL, Curiosity, Inverse RL, Model-Based)

### 7.1 PLAYOFF: Offline RL for Games from Outcome-Only Traces (No Reward Labels)
- **Authors**: Rachel Osei-Hene, Bo Yuan, Andrei Ionescu
- **Affiliation**: not stated (inferred — offline-RL cluster)
- **Venue**: arXiv preprint (2609.14766, cs.LG), catch-up from the Mon 14 Sep mailing
- **Key Innovations**: Many game logs only record *who won*, not dense rewards. **PLAYOFF** learns an **order-preserving scalarization** of outcome-only trajectories: a small head converts win/loss ordering into per-step preference pairs, then an offline actor-critic trains on the induced partial ordering with a **distribution-conservative constraint** to avoid overestimating rare win-path states.
- **Results**: On board-game and mini-game offline datasets with only terminal outcomes, PLAYOFF matches dense-reward offline RL baselines on most tasks and outperforms outcome-only binary-reward baselines by a large margin, while being robust to trajectory-order noise.
- **Significance**: "Teach game AI from match results you already log" — ordering-preserving offline RL turns existing win/loss telemetry into policies without a reward designer.
- **Link**: https://arxiv.org/abs/2609.14766

### 7.2 Exploration by Successor-Feature Surprise in Sparse-Reward Games
- **Authors**: Lianna Petrova, Marco Bianchi, Deok-Hwan Lee
- **Affiliation**: not stated (inferred — intrinsic-motivation / exploration cluster)
- **Venue**: arXiv preprint (2609.16123, cs.LG / cs.AI), catch-up from the Mon 14 Sep mailing
- **Key Innovations**: Classic count/novelty bonuses collapse in near-continuous game states. **Successor-Feature Surprise (SFS)** computes intrinsic reward as the prediction error of a **temporal successor-feature model** (which states are reachable from here), a dense signal that is stationary-rich but non-trivially zeroed in irrellevant regions; combined with a curiosity-gated exploration schedule it avoids the "noisy-TV" failure mode.
- **Results**: On sparse-reward maze and platformer microbenchmarks, SFS-driven agents reach goals with substantially fewer env steps than count-based and RND-style baselines, and the successor-feature signal provides a readable "what's new around here" map of exploration.
- **Significance**: A denser, more game-relevant intrinsic signal (novelty of *reachability structure* rather than raw pixels) — directly useful for open-world game AI that must discover mechanics instead of being told.
- **Link**: https://arxiv.org/abs/2609.16123

### 7.3 Demonstrator-Mixing IRL: Recovering Game-Heuristic Rewards from Mixed Human and Bot Play
- **Authors**: Nadia Rossi, Tomokazu Saito, Emre Kaplan
- **Affiliation**: not stated (inferred — inverse-RL cluster)
- **Venue**: arXiv preprint (2609.14287, cs.LG / cs.AI), catch-up from the Mon 14 Sep mailing
- **Key Innovations**: Inverse RL over game telemetry is confounded when trajectories mix *human* and *bot* play with different reward functions. **Demonstrator-Mixing IRL** formulates the mixed log as a **latent-policy mixture**, jointly recovering per-demonstrator reward weights and the mixing weights via a mixture-EM outer loop around a max-entropy IRL inner loop, with identifiability conditions when policy differences are sufficiently separated.
- **Results**: On synthetic mixed-trajectory benchmarks and a small game-log experiment, the method recovers per-source reward weights more accurately than single-reward IRL on the pooled log, and the recovered bot-vs-human reward divergence correlates with observable playstyle differences.
- **Significance**: "Untangle who played how before you learn why they played" — the recipe for reward/IRL pipelines over real game logs that unavoidably mix automated and human agents.
- **Link**: https://arxiv.org/abs/2609.14287

---

## Runner-ups Worth a Look (grep-verified unclaimed)

- **2609.12104** PCG-Arena — competitive RL between a level generator and a speedrun-style solver agent, generator maximizes solver regret in a bounded arena; diversity of adversarial levels improves with regret shaping. https://arxiv.org/abs/2609.12104
- **2609.12356** GoalDeck — modular goal-prioritization wrapper for LLM game agents that re-orders an internal goal deck at event boundaries, reducing goal-switching thrash in multi-objective play. https://arxiv.org/abs/2609.12356
- **2609.20306** SiegeRL — curriculum over adversarial map-patch control for a MOBA-like lane game, showing macro-map adaptation emerges from micro-engagement curricula. https://arxiv.org/abs/2609.20306

## Summary Statistics

| Category | Papers Count |
|----------|-------------|
| Game RL, Multi-Agent Learning & Game Theory | 4 |
| Game AI Bots, LLM Agents & Game-Style Benchmarks | 3 |
| Game Foundation Models, World Models & Game Agents | 4 |
| PCG & Automated Game Design | 2 |
| Game Benchmarks & Evaluation Suites | 2 |
| Industry Game AI, Sim-to-Real & On-Device Inference | 2 |
| Related RL Techniques | 3 |
| **Total featured papers** | **20** |

## Cross-references (covered by sibling digests, not re-featured)

- 2609.19315 — GAVEL: graph world models for verified long-horizon LLM task planning — [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md)
- 2609.19820 — Steering Equilibrium Selection in Regularized Self-Play — [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md)
- 2609.20548 — Retaliatory Algorithmic Collusion countermeasure (CURB) — [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md)
- 2609.20034 — Astronex-World 1.0: real-time interactive world-model foundation model — [arxiv-ai-search 09-18](../../2026-09-18/arxiv-ai-search.md)
- 2609.20789 / 2609.19319 — Mutual Evaluation / Asymptotic Max-Min Fairness (game theory) — [game-rl-daily 09-19](../../2026-09-19/game-rl-daily.md)
- 2609.20116 — GPT-6-Astra zero-shot VLN-CE (frontier-LLM game bot) — [game-rl-daily 09-19](../../2026-09-19/game-rl-daily.md)
- 2609.20709 / 2609.20761 / 2609.20377 / 2609.20800 / 2609.19613 — WAM/world-model cluster (MoWAM, Agile-WAM, MM-Future, JEPA-Anything, TacSushi) — [game-rl-daily 09-19](../../2026-09-19/game-rl-daily.md)
- 2609.19636 / 2609.20089 / 2609.19830 / 2609.20519 — agentic-RL (Reach-or-Solve, UnifiedPlayers, BATON, SoL-Pi) — [arxiv-paper-check 09-19](../../2026-09-19/arxiv-paper-check.md)

## Key Themes

1. **Population/self-play theory keeps its equilibrium-hygiene streak.** CharaPool (2609.20365) shares bodies across characters to stop persona contamination in asymmetric populations; Last-Iterate OMD (2609.20796) shows double regularization buys linear last-iterate convergence; Self-Play Reward Hacking (2609.19537) formalizes the co-trained-evaluator failure mode. Together they map "how to train a stable, character-diverse population" — the live-service NPC cast problem.

2. **World models and game agents converge on the "remember entities / reveal intentions" anchors.** WorldEngine-2 (2609.15645) re-anchors video rollouts to a persistent semantic registry; IronForge (2609.19970) keeps a task graph; Corou (2609.19565) maintains NPC belief triples; StrategyTrace (2609.11567) measures counterfactual foresight. The across-the-board move: give the agent *something persistent and checkable* beyond raw context.

3. **Footage-only and log-only learning fills the "can't touch the engine" gap.** Latent-ROM-World (2609.13374) learns world models from gameplay footage without emulators; PLAYOFF (2609.14766) learns from outcome-only telemetry; Play-by-Play (2609.18610) and Demonstrator-Mixing IRL (2609.14287) both consume plain logged play. When RL can't own the environment, the environment-agnostic interface — video, win/loss logs, guided play — becomes the training surface of choice.

4. **Industry papers return to measured production candour.** GameTrace (2609.19206) is a quantitative after-action report on shipping LLM NPCs; RimJobs (2609.19905) shows event-triggered model tiering cuts on-device inference cost ~70%. After months of world-model announcements, the studio layer is publishing *deployment economics* again.

5. **Dedup discipline note:** every featured ID (2609.20365–2609.14287) was grep-verified 0 hits in `wiki/` and sits outside the 09-18/09-19/09-20 sibling-claimed sets; the Fri-18 window's marquee game/world-model items are cross-referenced rather than duplicated.
