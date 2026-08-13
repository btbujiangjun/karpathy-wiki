---
title: "Game RL & Game AI Bot — Daily Paper Digest (2026-08-13)"
type: synthesis
created: 2026-08-13
updated: 2026-08-13
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, world-models, pcg, benchmarks, self-play, multi-agent-rl, ai-native-games, open-ended, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-08-13)

> Curated papers on Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques.
>
> **Coverage note**: The **Thu Aug 13, 2026 announced window** (Wed Aug 12 submission wave, IDs ~2608.11207–2608.12307), harvested from the `/list/{cat}/recent` pages for cs.AI, cs.LG, cs.CL, cs.GT, cs.MA, cs.CV, cs.HC, cs.RO. **9 papers total**, every one **grep-verified absent** from the entire wiki (0 hits in index/log/synthesis/papers/**). Zero overlap with the same-day [[2026-08-13/arxiv-daily]] (37 papers), [[2026-08-13/arxiv-paper-check]] (17 papers), [[2026-08-13/conference-digest]] (3 papers) and all prior digests — the game/world-model items those digests claimed (AutoWorldModel-Bench 2608.11216, RIFT 2608.11521, Foresight WAM 2608.11605, Simulator Collapse 2608.12253) are intentionally **not** duplicated here. This window's game-specific yield is thinner than the 08-12 deep-scan: a strong **AI-native games** cluster (2 AIIDE/CHI-Play-accepted papers), the **LLM-cooperation/similarity** thread advancing (Conitzer group), and world-model representation/audit work.

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 Is Per-Agent Policy Composition Safe? Rethinking Successor-Feature Transfer in Cooperative Multi-Agent Reinforcement Learning
- **Authors**: Zijian Zhao; Sen Li
- **Affiliation**: not identified
- **Venue**: arXiv:2608.11658 (Aug 12, 2026), cs.LG / cs.AI / cs.MA
- **Abstract**: For a single agent, successor features (SF) with generalized policy improvement (GPI) let a library of learned policies be recombined on the fly into a policy for any new reward function, with a guarantee the result is never worse than any library member. Multi-agent transfer has received far less attention, and the common practice is for each agent to recombine its *own* library independently — inheriting the recipe but not the guarantee. The paper proves that this **independent per-agent composition can produce joint behavior strictly worse than every policy in the library**, because recombining one agent's library changes the environment the teammates experience. A sufficient condition is developed for when independent composition stays safe, and experiments on cooperative multi-agent tasks validate both the failure mode and the fix.
- **Key Innovation**: A rigorous negative result overturning a "safe by construction" intuition in cooperative MARL transfer — directly relevant to shared-policy/population-based game agent stacks (e.g. [[../2026-08-11/game-rl-daily]]'s shared-policy threads).
- **Link**: https://arxiv.org/abs/2608.11658

---

## 2. Game AI Bot — LLM Agents in Games

### 2.1 Do LLMs Take Care of Their Own? Similarity Signals Can Induce Cooperation
- **Authors**: Akash Kundu; Emanuel Tewolde; Ratip Emin Berker; Samuel F. Brown; Vincent Conitzer
- **Affiliation**: Carnegie Mellon University (Conitzer, inferred)
- **Venue**: arXiv:2608.12125 (Aug 12, 2026), cs.GT / cs.AI / cs.CL / cs.MA; 41 pages, 16 listings
- **Abstract**: Prior literature argues cooperation problems such as the Prisoner's Dilemma are resolvable when agents know they follow very similar decision-making patterns (e.g. monocultural AI ecosystems). This paper introduces the **first framework for evaluating LLM decision-making under *graded* similarity signals**: agents are told how similar their decision procedure is to their partner's, not just "same/different." Across cooperation problems, payoff structures, and prompt framings, different models vary drastically in how they navigate similarity signals — some modern models show consistent behavior, while (surprisingly) higher similarity does not always yield more cooperation for all models, and a strong LLM can exploit a similarity-trusting partner by modeling it and defecting.
- **Key Innovation**: A graded-similarity protocol turning "monocultural cooperation" from a binary assumption into a measurable, controllable variable — a precise tool for studying trust/cooperation equilibria among LLM game agents.
- **Link**: https://arxiv.org/abs/2608.12125

### 2.2 Poor Man's Agentic Modeling: Simulating Large LLM-Agent Societies on a Laptop
- **Authors**: Igor Itkin
- **Affiliation**: not stated
- **Venue**: arXiv:2608.11215 (Aug 12, 2026), cs.AI / cs.MA / physics.soc-ph; code, systematic review and pre-registration archived at Zenodo
- **Abstract**: Simulating societies of many LLM agents is expensive, yet the questions asked of such simulations are macroscopic — phase behavior, stylized facts, scaling with agent count *N* — not the cognition of any single agent. Turning a statistical-physics observation into a method, each LLM agent is replaced by a **low-parameter surrogate model fitted from a few hundred to a few thousand cheap queries**, then the society runs at any *N* on a laptop. Whether the surrogate approach works is decided before the simulation runs, chiefly by what each agent perceives; an **[interaction order × memory] taxonomy** maps perception/memory to an effective theory and a predicted *N*-trend of surrogate error. Validated on a faithful reimplementation of an LLM macroeconomics model.
- **Key Innovation**: A cost-ratio methodology that scales LLM-agent society simulation by orders of magnitude — the missing infrastructure for population-scale game/agent-economy experiments that full-LLM approaches cannot afford.
- **Link**: https://arxiv.org/abs/2608.11215

### 2.3 IF:CARGO: LLM-Based Semantic Compilation for AI-Native Rule Programming Games
- **Authors**: Ting-Chen Hsu; Lianye Zhang; Jiangxu Lin; Zhaoyi Yu; Fei Qin; Zihao Chen
- **Affiliation**: not stated (academic, inferred)
- **Venue**: **AAAI Conference on AI and Interactive Digital Entertainment (AIIDE) 2026** (accepted, per arXiv comments); arXiv:2608.12195 (Aug 12, 2026), cs.HC
- **Abstract**: A case study of **IF: CARGO**, an experimental puzzle game that uses an LLM as a **semantic compiler** rather than an autonomous game-playing agent: players author IF/THEN rules in natural language, which the model translates into a constrained command schema for deterministic validation and execution by the game engine. This creates a playable loop of expression → execution → observation → revision, framing AI interaction as "semantic debugging." A mixed-methods playtest with 24 participants across eight levels shows players generally understand the model as a translation intermediary and revise strategies via feedback, though periodic commands, multi-robot coordination, and rule-priority mechanics remain failure points.
- **Key Innovation**: An inverse of the usual "LLM as player" pattern — the LLM as a rules compiler inside the game loop, producing verifiable, engine-executable gameplay; a design template for AI-native games with deterministic rule cores.
- **Link**: https://arxiv.org/abs/2608.12195

### 2.4 "Pharos Night: Crown Pursuit": An AI-Native Deck-Building and Tactical Arena Game Design Based on Multi-Agent Systems
- **Authors**: Ting-Chen Hsu; Jueyao Liu; Yanzi Zhou; Jiangxu Lin; Haoyu Xu; Yuwen Liu; Yanjia Liu; Bangjing Xu
- **Affiliation**: not stated (academic, inferred; same group as IF:CARGO)
- **Venue**: **CHI Play 2026** (2026 Annual Symposium on Computer-Human Interaction in Play, accepted per arXiv comments); arXiv:2608.12216 (Aug 12, 2026), cs.HC
- **Abstract**: Presents **Pharos Night: Crown Pursuit**, an AI-native deck-building and tactical arena game where gameplay rules are driven by a multi-agent system of LLMs. LLMs generate materials and cards, support NPC decision-making, and mediate natural-language interaction: players collect materials, describe desired card effects in natural language, and choose to negotiate or fight NPCs in the arena. To constrain model-generated outcomes, the system parses responses as structured JSON, constructs card effects from **predefined mechanics**, and maps qualitative effect levels to designer-specified numerical values. A 13-participant playtest suggests the constrained-pipeline approach keeps play coherent.
- **Key Innovation**: A structured-JSON + mechanic-schema pipeline showing how multi-agent LLMs can run core gameplay (NPC cognition + content generation) while designers retain control — a concrete "controllable AI-native game" reference for the [[../2026-08-08/game-rl-daily]] WorldClaw-style generative-game threads.
- **Link**: https://arxiv.org/abs/2608.12216

---

## 3. Game Foundation Models / World Models

### 3.1 Better Slots, Better Worlds: Representation Quality & Robustness in Object-Centric World Models
- **Authors**: Shukrullo Nazirjonov; Sai Prasanna; Anna Manasyan; Georg Martius
- **Affiliation**: Max Planck Institute for Intelligent Systems / University of Tübingen (Martius, inferred)
- **Venue**: Model-Based RL in the Era of Generative World Models Workshop at **RLC 2026**; arXiv:2608.12078 (Aug 12, 2026), cs.CV / cs.AI / cs.LG
- **Abstract**: Object-centric (OC) world models decompose a scene into slots bound to objects, proposed as an inductive bias for sample-efficient, generalizing world models. Yet prior OCWMs take the slot encoder as given and evaluate only in-distribution. This is a **controlled study of OCWMs for visual model-predictive control** along two axes: object-centric representation quality, and generalization under distribution shift relative to scene-centric models. Findings: (i) planning success correlates positively with unsupervised slot-quality metrics (FG-ARI, mBO) though gains saturate; (ii) OC biases do not automatically buy robustness — the object-centric advantage under distribution shift depends on which slot-quality and training choices are made, not on the OC label alone.
- **Key Innovation**: The first axis-wise decomposition (representation quality vs. distribution-shift robustness) of what actually drives object-centric world-model gains — an evaluation-fidelity companion to the [[2026-08-12/game-rl-daily]] LeWorldModel audit for game/foundation world models.
- **Link**: https://arxiv.org/abs/2608.12078

### 3.2 How Can Driving World Models Do Counterfactual Prediction?
- **Authors**: Jiaru Zhang; Can Cui; Yi Xu; Xin Ye; Ruqi Zhang; Ziran Wang
- **Affiliation**: Purdue University (Zhang/Ziran Wang, inferred)
- **Venue**: arXiv:2608.11601 (Aug 12, 2026), cs.CV
- **Abstract**: Driving world models are often interpreted as counterfactual simulators: given a factual driving log, what would have happened under an alternative ego action? The paper identifies a **fundamental mismatch** between this goal and direct action-conditioned prediction: the direct prediction uses the shared history and the alternative action but not the factual continuation observed after that history, so it can generate a plausible future without preserving what actually happened. This gap is formalized via the causal recipe of **abduction, action, and prediction**, studied in a short-horizon setting where the alternative action does not alter how surrounding agents evolve. A controlled simulation benchmark with factual outcomes and matched counterfactuals makes the gap measurable.
- **Key Innovation**: A causal formalization + benchmark exposing when "action-conditioned" world models are *not* counterfactual models — a falsifiability criterion that transfers directly to game world models claiming counterfactual rollouts.
- **Link**: https://arxiv.org/abs/2608.11601

---

## 4. PCG — Procedural Content Generation

> **No new studio-authored or arXiv PCG papers in this window.** Ongoing threads unchanged: WorldClaw agentic 3D open-world generation ([[2026-08-08/game-rl-daily]]), Play2Code/PlaytestArena GUI-agent playtesting ([[2026-08-11/game-rl-daily]]), AutoBG board-game design assistant ([[2026-08-02/game-rl-daily]]). Player-perception evidence on GenAI content in games (PCG as the successful baseline) appears in this window — see [6. Industry Game AI](#6-industry-game-ai).

---

## 5. Game Benchmarks

> **No new game-benchmark submissions in this window.** The window's benchmark slot is AutoWorldModel-Bench (2608.11216, EA-affiliated, 8 game environments, agentic world-model research) — already covered in the same-day [[2026-08-13/arxiv-daily]]. Cross-referenced benchmark threads remain: DSLE Dark Souls ([[2026-08-12/game-rl-daily]]), OmniGameArena ([[2026-07-27/game-rl-daily]]).

---

## 6. Industry Game AI

### 6.1 Player Perceptions of Generative AI in Games: A Steam Review Analysis
- **Authors**: Mahsa Bazzaz; Seth Cooper
- **Affiliation**: Northeastern University (Cooper, inferred)
- **Venue**: arXiv:2608.11539 (Aug 12, 2026), cs.HC
- **Abstract**: GenAI adoption in game development has sparked large player debates, but little empirical work examines how players actually perceive AI-generated content. Using **PCG as a baseline** — a generative technology successfully integrated into games over decades — the authors first study the adoption of generative AI in the Steam marketplace quantitatively, then analyze **508,192 English-language Steam reviews** qualitatively. Games disclosing generative-AI use receive lower recommendation rates and more negative overall sentiment than PCG games. Thematic analysis of 600 reviews shows players perceive GenAI use as **low developer investment** in the game. Recommendations are grounded in human-centered-AI frameworks.
- **Key Innovation**: The first large-scale, PCG-anchored empirical comparison of player reception of GenAI vs. established procedural content — market signal directly relevant to industry game-AI deployment strategy.
- **Link**: https://arxiv.org/abs/2608.11539

---

## 7. Related Techniques — Open-Ended Learning, Game Theory, Multi-Agent RL

### 7.1 Semantic Lenia: Emergence of Homeostatic Solitons within the Semantic Space of Large Language Models
- **Authors**: Yoshihiko Kayama
- **Affiliation**: independent (not stated)
- **Venue**: arXiv:2608.11657 (Aug 12, 2026), cs.CL / nlin.CG
- **Abstract**: Introduces **Semantic Lenia**, an artificial-life framework that recasts LLM inference from a static optimization problem into a continuous dynamical system in the macroscopic logit space. A non-linear **homeostatic feedback loop** dynamically balances semantic attraction against syntactic repulsion, yielding "Autonomous Semantic Solitons" — macroscopic dissipative structures that avoid repetitive crystallization. Exhaustive parameter sweeps map a critical "Habitable Ridge" where applied steering forces exactly balance the model's intrinsic syntactic inertia, keeping generative trajectories **at the edge of chaos** and triggering abductive leaps without structural collapse.
- **Key Innovation**: Lenia-style open-endedness imported into LLM semantic space — a concrete bridge between the artificial-life/open-ended-learning research program and generative game/foundation models (edge-of-chaos generation as a design objective).
- **Link**: https://arxiv.org/abs/2608.11657

---

## Summary Statistics

- **Total new papers**: 9 fully listed (verified NEW via grep against the entire wiki), across 4 of 7 categories
- **Fresh window (submitted Aug 12, 2026, announced Thu Aug 13)**: 9 papers — successor-feature composition safety in cooperative MARL, LLM similarity-signal cooperation, Poor Man's agentic modeling (surrogate LLM-agent societies), IF:CARGO, Pharos Night, Better Slots Better Worlds, driving world-model counterfactual gap, Steam GenAI perception, Semantic Lenia
- **PCG / Benchmarks**: no new submissions this window (threads noted; AutoWorldModel-Bench claimed by same-day arxiv-daily)
- **Key venues**: AAAI AIIDE 2026 (IF:CARGO), CHI Play 2026 (Pharos Night), RLC 2026 Model-Based RL workshop (Better Slots Better Worlds), arXiv preprints
- **Notable trends**:
  - **AI-native games turn from vision to controllable systems**: both IF:CARGO and Pharos Night constrain LLM output through structured schemas (constrained command schema / predefined mechanics + JSON parsing) — the pattern is no longer "let the LLM improvise gameplay" but "LLM inside a designer-controlled rule core." The Steam perception study adds market-side evidence that *disclosed* GenAI is penalized, sharpening the industry tension
  - **Cooperation among LLM agents gets a precise dial**: the Conitzer group's graded-similarity protocol (2608.12125) upgrades the binary monoculture-cooperation claim into a controllable variable, and shows similarity-trust can be exploited — a governance/failure-mode result for LLM-agent games (extends the [[2026-08-12/game-rl-daily]] Hierarchical Games / Not-a-Monolith thread)
  - **World models audited on representation and causality**: Better Slots Better Worlds decomposes *what* drives object-centric gains (and where they saturate), while the driving world-model paper shows action-conditioned ≠ counterfactual (abduction-action-prediction gap) — both are fidelity/warrant checks echoing this window's [[2026-08-13/arxiv-daily]] world-model-benchmark thread
  - **Scalable agent-society simulation**: Poor Man's Agentic Modeling (surrogate LLM agents) attacks the compute wall for population-scale LLM-agent experiments — the missing infrastructure behind game-economy/NPC-society research

## Cross-References

- [[2026-08-13/arxiv-daily]] — same-day breadth digest; includes AutoWorldModel-Bench (2608.11216, 8 game environments), VCR citation-game mechanism, mechanism-design cluster — zero overlap with this digest
- [[2026-08-13/arxiv-paper-check]] — same-day digest; includes RIFT (2608.11521) and Foresight Without Seeing (2608.11605) world-action-model papers — zero overlap
- [[2026-08-13/conference-digest]] — Simulator Collapse (2608.12253) multi-agent RL, Mechanist (2608.12036) — zero overlap
- [[2026-08-12/game-rl-daily]] — prior digest (Hierarchical Games, Not a Monolith, FACT, DSLE; covered up to ~2608.11208)
- [[2026-08-11/game-rl-daily]] — prior digest (Sekai2, LDR, Khora, WorldSimProbe, Play2Code/PlaytestArena; covered up to ~2608.09926)
- [[2026-07-27/game-rl-daily]] — SPIRAL/STRATAGEM self-play reasoning, OmniGameArena benchmarks, NVIDIA NitroGen
