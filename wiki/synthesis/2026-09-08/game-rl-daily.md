---
title: "Game RL & Game AI Bot — Daily Paper Digest (September 8, 2026)"
type: synthesis
created: 2026-09-08
updated: 2026-09-08
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, pcg, benchmarks, world-models, self-play, causal-induction, game-design, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-08)

> Survey of Game RL & Game AI Bot papers for **Tue Sep 8, 2026**. arXiv has **no new mailing since Mon 7 Sep 2026** (`list/*/recent` still anchored at the Mon 7 Sep window), which the 09-07/09-08 sibling digests (arxiv-daily, arxiv-ai-search, arxiv-paper-check, conference-digest) already mined. This report is therefore a **second/passes sweep** over the Sep 1-8 window + catch-up submissions, focused on **game-specific papers those digests did NOT feature.** Every numbered arXiv ID below is grep-verified **(0 hits)** across `wiki/`. Affiliations marked *(inferred)* where metadata is thin.

**Already covered elsewhere (for continuity, not re-featured):** 09-07 game-rl-daily featured `2608.31100` S3Gym self-improvement + curiosity trio (`2607.16858` / `2606.19476` / CIG-flagged); 09-07 arxiv-daily / arxiv-ai-search featured `2609.04303` Abstraction Agent (poker endgames), `2609.05298` MARL change-point detection, `2609.04394` drone swarm defense, `2609.04396` memoryless Nash; 09-05 game-rl-daily featured `2608.31166` constant regret, `2609.00504` MARL hardness, `2609.01838` differential games, `2608.28884` MineCEraft, `2609.02459` CivBench, `2608.29910` Matrix-Game 3.5, `2608.30819` self-play driving; 09-03/09-05 covered NitroGen `2601.02427`, GameWAM `2608.26200`, ABot-World-0 `2607.19191`, WanToFight `2607.12592`, DiG-bench `2608.12593`, GameXpert-Bench `2608.21833`, WorldMind `2608.21439`. Also in recent listing but already covered: `2608.29197` PokaiTrainer, `2609.03122` Turn-Based Combat Arena, `2609.02931` LLM-Guided NPC RL, `2609.02928` mean-field RL.

---

## 1. Game RL — Reinforcement Learning in Games

*(This window's cs.GT/cs.MA game-RL papers — `2609.00504` independent RL in Markov games, `2608.31166` constant regret, `2609.01838` differential-game control, `2608.30635` test-time RL in imperfect-info games — were all already featured by 09-05/09-01 digests. No brand-new 0-hit game-RL algorithm paper surfaced in this second pass; see §7 for the closest related-technique finds.)*

### 1.1 (Continuity) Game RL landscape, Sep 2026

The sibling digests established the current game-RL frontier: constant-individual-regret algorithms in general games (MIT `2608.31166`), PPAD-hardness + first sub-exponential CCE for discounted Markov games (UIUC `2609.00504`), and test-time RL in imperfect-information games (`2608.30635`). This window adds no new core-RL-algorithm paper; the genuinely-new signal this scan found sits in **game understanding** (§2), **world-model inference** (§7), and **game design/HCI** (§6).

## 2. Game AI Bot — LLM / VLM Game Agents & Game Understanding

### 2.1 From Gameplay Traces to Game Mechanics: Causal Induction with Large Language Models

- **Authors**: Mohit Jiwatode, Alexander Dockhorn, Bodo Rosenhahn
- **Affiliation**: Leibniz University Hannover / SDU Metaverse Lab, University of Southern Denmark
- **Venue**: submitted to ICPR 2026
- **arXiv**: [2602.00190](https://arxiv.org/abs/2602.00190)
- **Abstract & Key Innovations**: Investigates **Causal Induction** — inferring governing laws from observational data — by tasking LLMs with reverse-engineering **Video Game Description Language (VGDL)** rules directly from gameplay traces. Selects 9 representative games from the **GVGAI** framework via semantic embedding clustering (S-BERT + K-Means++) to cut redundancy. Compares two VGDL-generation routes: (1) **direct code generation** from observations vs (2) a **two-stage neuro-symbolic pipeline** that first infers a **Structural Causal Model (SCM)** then translates it to VGDL. Evaluated across prompting strategies and controlled context regimes (raw observations → partial VGDL spec). The SCM-mediated route wins blind preference evaluations **up to 81%** and yields **fewer logically inconsistent rules**, better separating hallucinated/memorized mechanics from genuinely learned ones. Positioned for downstream **causal RL, interpretable agents, and procedurally generating logically consistent games.**

## 3. Game Foundation Models / World Models

### 3.1 Can LLM Agents Infer World Models? Evidence from Agentic Automata Learning

- **Authors**: Reef Menaged, Gili Lior, Shauli Ravfogel, Roee Aharoni, Gabriel Stanovsky
- **Affiliation**: *(inferred — Hebrew University / AI2 lineage)*
- **Venue**: arXiv preprint (2026-06)
- **arXiv**: [2606.16576](https://arxiv.org/abs/2606.16576)
- **Abstract & Key Innovations**: Proposes **Agentic Automata Learning** — an evaluation of whether tool-calling LLM agents can *uncover hidden environments through interaction*, formalized as discovering a hidden **deterministic finite automaton (DFA)** via (1) membership queries ("does this string belong to the target language?") and (2) equivalence queries ("is this the target DFA?"). Provides a scalable testbed with controlled complexity, measurable interaction efficiency, and classic automata-learning baselines (L*, TTT). Findings: performance **drops sharply as DFA size grows**; **reasoning models are markedly stronger** than non-reasoning ones; trajectory analysis reveals recurring failures in **query planning, evidence integration, and hypothesis construction**. Directly relevant to game agents that must reconstruct world dynamics from pro-active queries — the interactive "world-model inference" counterpart to §2.1's passive gameplay-trace induction.

### 3.2 TourPhysics: Bringing Physics to World Models for Exploration and Manipulation from a Single Image

- **Authors**: Xin Zhang, Yabo Chen, Zixuan Duan, Haibin Huang, Chi Zhang, Feng Xu, Xuelong Li
- **Affiliation**: *(inferred — multi-institution, incl. Tsinghua/BMV lineage)*
- **Venue**: arXiv preprint (2026-09)
- **arXiv**: [2609.04911](https://arxiv.org/abs/2609.04911)
- **Abstract & Key Innovations**: Addresses the world-model honesty problem directly (cf. 09-05 "Intervention Gap in latent WMs"): interactive visual world models must **distinguish observation from physical intervention** — camera motion reveals surfaces, intervention changes object motion/contact/deformation. Extends **PhysOmni** (ACM MM 2026) from finite physics-grounded video synthesis to **persistent exploration and manipulation**. Combines deterministic simulation with video generation, assigning **separate roles to simulator state, geometric evidence, generator controls, and appearance memory**: for each action the simulator first computes a finite physical + camera trajectory, then the observation is generated; accepted observations publish terminal state and update appearance memory while **committed state and simulator geometry stay fixed** beyond generator control. Relevant for game world models that must survive long-horizon interaction without drifting from physics.

## 4. Procedural Content Generation (PCG)

*(Direct PCG-generation novelty this window is thin — 09-03 covered DiG-bench `2608.12593` + PCG metageneration CAD `2608.17947`; 09-05 covered feasibility-aware PCG `2609.00527`. The strongest genuinely-new PCG-adjacent contribution is §2.1's causal-induction route to generating *logically consistent* new games via learned SCMs — a metageneration method with an explicit consistency guarantee, which is the direct successor line to CAD. Continuity noted here.)*

## 5. Game Benchmarks

*(No brand-new standalone game benchmark verified 0-hit this window — GameXpert-Bench `2608.21833`, DiG-bench `2608.12593`, CivBench `2609.02459`, GameWorld `2604.07429`, OmniGameArena `2606.09826` were all covered in 09-03/09-05. The benchmark-relevant novelty this window lives in §3.1's Agentic Automata Learning — a *controllable-complexity* interactive inference benchmark, applicable as a world-modeling testbed for game agents.)*

## 6. Industry Game AI & Game Design

### 6.1 Signal-Driven Pervasive Game Design: The LifeSync-Games Framework as a Player Experience Integration Layer

- **Authors**: J. Macías-Cáceres, F. Gutiérrez-Vela, P. Paderewski-Rodriguez, R. González-Ibáñez
- **Affiliation**: *(inferred — University of Granada HCI group)*
- **Venue**: arXiv preprint (2026-09)
- **arXiv**: [2609.03169](https://arxiv.org/abs/2609.03169)
- **Abstract & Key Innovations**: A game-design paper adjacent to adaptive game AI: **LifeSync-Games (LSG)** operationalizes the player's physiological/cognitive state as a **Player Experience Integration Layer (PEIL)** acting *transversally* across pervasive gaming's spatial/temporal/social dimensions, rather than as one more input channel. Ground-truth signals: physical activity, sleep quality, memory, decision speed. Introduces a gamified integration artifact (LSG portal) mediating real↔virtual exchange via redeemable points, real-world missions, and structural gamification. Five HCI design principles grounded in **Self-Determination Theory + Flow Theory**, instantiated across six commercial video games, with a quasi-experimental study protocol (n=70–80). Reports the design stage; rule thresholds/portal parameters remain open design decisions. Relevant to industry adaptive-difficulty/AI-director systems as a signal-fusion reference.

### 6.2 SimSkill: A Lifelong Learning AI Agent for Autonomous Mastery of Traffic Simulation

- **Authors**: Qi Liu, Qinzheng Wang, Yiming Bie
- **Affiliation**: *(inferred — Harbin/HUST traffic lineage)*
- **Venue**: arXiv preprint (2026-09)
- **arXiv**: [2609.03753](https://arxiv.org/abs/2609.03753)
- **Abstract & Key Innovations**: A **self-evolving agent** over the **SUMO traffic simulator** — a large-scale interactive simulation (the same class of driver/agent training ground as game traffic simulators). SimSkill **identifies capability gaps, generates and solves environment-grounded tasks, verifies solutions through an action–critic loop, and consolidates experience into episodic/procedural/semantic memory without updating the backbone** model. Over autonomous exploration it builds a reusable workflow library. On two held-out benchmarks with three backbone LLMs and independent artifact-based verification it improves **verified completion by up to 25pp**; ablations show procedural + semantic memory are complementary. Honest caveat: benefits are **backbone- and budget-dependent** — memory does not help every model or uniformly reduce cost. Relevant to game NPC/agent frameworks that must accrue durable competence (cf. PCSP, WorldMind, HeRoN lineage) under enterprise-adjacent simulation workloads.

## 7. Related Techniques — World-Acting Systems, Self-Play, Curiosity

### 7.1 From Language Models to World-Acting Systems: Progress and Limits of Agentic AI across Digital, Social, Virtual, and Physical Environments

- **Authors**: Linsen Zhu, Mengqing Cai
- **Affiliation**: *(inferred)*
- **Venue**: Review article, 29 pp., literature cutoff 31 August 2026
- **arXiv**: [2609.04894](https://arxiv.org/abs/2609.04894)
- **Abstract & Key Innovations**: A critical review framing LLMs as becoming **"consequential agents"** only when surrounding systems let outputs change external state — including **"inhabit generated worlds"** and persistent simulations. Organizes evidence along **delegated authority, temporal persistence, and environmental coupling**, separating model / harness / environment. Findings: **action-interface expansion is documented more convincingly than robust completion, recovery, authorization, or independent verification**; MCP and A2A improve interoperability but do not establish trustworthy delegation; **persistent simulations and world models support training and planning but do not themselves demonstrate agency**. Proposes **"justified delegation"** as an analytical/normative heuristic (not a law): expand action scope only where evidence supports provenance, bounded authority, failure detection, safe recovery, and calibrated human control. Useful as a framework for game-agent deployment claims (what a game bot does vs. has authority to do).

---

## Key Themes This Window

1. **From playing games to *understanding* games.** The strongest genuinely-new signal this scan — causal induction of VGDL mechanics via SCMs (`2602.00190`) and agentic automata learning for world-model inference (`2606.16576`) — is about game *understanding* rather than game *playing*: inferring hidden rules from traces or queries, then reusing them for causal RL and consistent PCG. This is the "world-model honesty" thread (09-05) applied to the *inference* side, not just the *prediction* side.
2. **Physics-aware world models for interaction.** TourPhysics (`2609.04911`) operationalizes observation-vs-intervention separation with committed simulator geometry — the interaction-honesty requirement that pure video world models fail at over long horizons.
3. **Agentic capability is bounded and must be argued honestly.** The "justified delegation" review (`2609.04894`) and SimSkill's backbone/budget-dependent gains (`2609.03753`) both resist "one march toward autonomy" narratives — directly applicable to how game-bot and NPC research reports generalizable competence.
4. **Industry game AI leans on player signal fusion.** LifeSync-Games (`2609.03169`) treats physiological/cognitive state as a transversal layer for adaptive experiences — a design-side complement to RL-based adaptive difficulty.

## Scan & Dedup Notes

- Method: arXiv `list/{cs.AI,cs.LG,cs.GT,cs.MA,cs.CV,cs.SD,cs.HC}/recent` parsed for the Sep 1–8 window + targeted web searches (game RL, game AI, world models, PCG, benchmarks, industry, self-play). arXiv API still rate-limited (HTTP 429 "Rate exceeded") → scraped listing + `/abs/` pages directly.
- **No new arXiv mailing since Mon 7 Sep 2026**; this is a second-pass sweep over that window + catch-up submissions. Every featured numbered arXiv ID grep-verified **0 hits** in `wiki/` (both ID and title-based).
- Papers already covered by 09-03/09-05/09-07 game-rl-daily or 09-07/09-08 sibling digests are excluded from featured status and listed in the header for continuity.
- Affiliations marked *(inferred)* where metadata is thin; `2606.16576` venue unconfirmed (no Comments field), `2609.03169`/`2609.03753`/`2609.04911` affiliations inferred from author lineage.