---
title: "Game RL & Game AI Bot — Daily Synthesis (2026-08-04)"
type: synthesis
created: 2026-08-04
updated: 2026-08-04
tags: [game-rl, game-ai, game-foundation-models, pcg, game-benchmarks, self-play, world-models, multi-agent-rl, llm-agents]
sources: []
---

# Game RL & Game AI Bot — Daily Synthesis (2026-08-04)

> Curated papers on Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques. Verified against the arXiv API (submitted May–Aug 2026; fresh window Jul 31 – Aug 3, 2026). Complements the 2026-08-01 and 2026-08-02 digests with **no overlap** — every paper below was confirmed absent from the wiki before inclusion.

---

## 1. Game RL — Reinforcement Learning in Games

### ARC-RL: A Reinforcement Learning Playground Inspired by ARC Raiders
- **Authors**: Carlo Romeo, Andrew D. Bagdanov
- **Affiliation**: University of Florence (MICC)
- **Venue**: arXiv:2605.19503 (May 2026, v2)
- **Key Innovation**: Four MuJoCo continuous-control environments whose morphologies are game NPCs (the 18-DoF hexapods Queen/Tick, 12-DoF armoured hexapod Bastion, 12-DoF quadruped Leaper from ARC Raiders), breaking the sim-to-real convention of deriving bodies from commercial hardware. A single closed-form multi-component reward (velocity tracking + gait-compliance + safety penalties, no mocap) plus Central Pattern Generator demonstrators as prior data. Benchmark study of online (SAC, SPEQ, SOPE-EO) vs prior-data (SACfD, SPEQ-O2O, SOPE) RL — SOPE-EO wins almost everywhere within 1M steps; first locomotion-RL playground mirroring a commercial game's bestiary.
- **Link**: https://arxiv.org/abs/2605.19503

### Chess on Ice: Curling Tactical Decision-Making via Backward Induction and Deep Reinforcement Learning
- **Authors**: Patrick Oberlin, Matteo Cederle, Aren Karapetyan, Saverio Bolognani, Gian Antonio Susto, Florian Dörfler
- **Affiliation**: ETH Zurich / University of Padova
- **Venue**: arXiv:2608.02379 (Aug 3, 2026)
- **Key Innovation**: DDPG actor-critic adapted to the finite-horizon structure of curling (continuous state/action, stochastic action outcomes from player skill, perturbation-sensitive transitions). Fully self-supervised (no human annotations): on a reduced four-rock variant the learned agent matches a hand-crafted expert heuristic where that heuristic is near-optimal, quantified against the hammer advantage. The learned critic doubles as a dense value surface for comparing tactical alternatives — aimed at post-game analysis and athlete decision support.
- **Link**: https://arxiv.org/abs/2608.02379

---

## 2. Game AI Bot — LLM-Powered Game Agents & NPC Intelligence

> **No new papers this cycle.** Recent NPC coverage lives in prior dailies: PCSP persona-conditioned shared RL ([[2026-08-01/game-rl-daily]] and [[2026-08-02/game-rl-daily]], 2605.23652), Psy-CoT/RAPO psychology-grounded role-playing (2606.27025), HeRoN mediated RL-LLM NPCs ([[2026-07-02/game-rl-daily]]), CaM-Wolf social deduction (2026-08-01). One adjacent new finding: **ReactiveGWM** (Section 3) treats NPCs as first-class entities in world models rather than background pixels.

---

## 3. Game Foundation Models — Generalist Game Agents & World Models

### Orca: The World is in Your Mind
- **Authors**: Yihao Wang, Yuheng Ji, Mingyu Cao, et al. (57 authors)
- **Affiliation**: —
- **Venue**: arXiv:2606.30534 (Jun 29 2026; v3 Jul 17 2026)
- **Key Innovation**: An initial instantiation of a **general world foundation model**. Learns one unified world latent space from multimodal world signals, exposed through multimodal readout interfaces, centered on **Next-State-Prediction** rather than isolated next-token/frame/action prediction. Two complementary learning paradigms: *unconscious* learning captures dense natural state transitions from continuous video; *conscious* learning models sparse, language-described state transitions + VQA supervision. Pretraining on 125K hours of video + 160M event annotations; frozen backbone with lightweight trainable modality-specific decoders (text / image prediction / embodied action). Shows stronger world latent ⇒ stronger downstream readouts; beats similar-sized specialized baselines.
- **Link**: https://arxiv.org/abs/2606.30534

### ReactiveGWM: Steering NPC in Reactive Game World Models
- **Authors**: Zeqing Wang, Danze Chen, Zhaohu Xing, Zizhao Tong, Yinhan Zhang, Xingyi Yang, Yeying Jin
- **Affiliation**: NTU Singapore
- **Venue**: arXiv:2605.15256 (May 2026)
- **Key Innovation**: Argues player-centric world models treat NPCs as background pixels (passive video renderers, not simulation engines). ReactiveGWM explicitly decouples player controls from NPC behaviors: player actions inject via a lightweight additive bias, high-level NPC responses (Offense/Control/Defense) are grounded through cross-attention modules that learn a **game-agnostic representation of interactive logic**. This enables zero-shot strategy transfer — the modules plug into off-the-shelf, unannotated world models of different games with no retraining. Validated on two Street Fighter games: fine-grain player controllability + prompt-aligned NPC strategy adherence.
- **Link**: https://arxiv.org/abs/2605.15256

---

## 4. Procedural Content Generation (PCG)

> **No new papers this cycle.** Fresh-window PCG searches surfaced only already-tracked work: MAGIC multi-scene transition-aware generation (2607.11594), HDPCG high-dimensional PCG (2602.18943), Multiverse cross-game blending (2603.26782), Garden of Forking Paths narrative-arc PCG (2605.01245), Agentic PCG via tool-using LLMs (SSRN), GameDevBench (2602.11103). See [[2026-08-01/game-rl-daily]] and [[2026-07-26/game-rl-daily]].

---

## 5. Game Benchmarks

> **No new papers this cycle.** The two freshest benchmark entries (DungeonBench for D&D rules-rich tactical reasoning, 2607.29577; MirrorCraft for hidden rule changes in Minecraft, 2607.29218; both Jul 31 2026) were already captured in [[2026-08-03/arxiv-ai-search]]. Earlier benchmark coverage: OmniGameArena (2606.09826), GameWorld (2604.07429), FootsiesGym (2607.06514), MTG-Causal-RL (2605.06066) — see [[2026-08-02/game-rl-daily]].

---

## 6. Industry Game AI

> **No new papers this cycle.** Ongoing industry threads tracked elsewhere: KRAFTON PUBG ALLIE on-device agents ([[2026-07-17/game-rl-daily]]), NVIDIA ACE/NVIGI SDK ([[2026-07-13/game-rl-daily]]), PCSP UE5 deployment at 64 agents (2605.23652), EA SPORTS NHL 26 production RL (2607.07498, [[2026-08-01/game-rl-daily]]), TerraZero procedural driving sim (2607.13028, [[2026-08-02/game-rl-daily]]). ARC-RL (Section 1) is the notable new games-adjacent industry contribution: game-style stylistic constraints as a first-class RL benchmark property.

---

## 7. Related Techniques — Self-Play, World Models, Multi-Agent RL

### Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills
- **Authors**: Siyuan Huang, Pengyu Cheng, Haotian Liu, Tao Chen, Yihao Liu, Jingwei Ni, Shijie Zhou, Ziyi Yang, Gangwei Jiang, Mengyu Zhou, Yu Cheng, Xiaoxi Jiang, Guanjun Jiang
- **Affiliation**: —
- **Venue**: arXiv:2607.22529 (Jul 24, 2026)
- **Key Innovation**: Skill-SP reconciles the self-evolution dilemma between task diversity (open-ended generation, unreliable verification) and verification reliability (environment-bound, narrow domains) by treating **agent skills** as the middle ground — each skill gives deep verifiable execution in a scenario, while dynamic routing across skills keeps task variety open-ended. Co-evolutionary loop of a proposer (generates tasks conditioned on sampled skills), a solver (pushes capability boundaries), and a dynamic skill controller (updates/expands the skill library from execution feedback), orchestrated by RL. Consistently raises the ceiling of competent backbones and catalyses turnarounds for initially misaligned models on tool-use and reasoning benchmarks. Distinct from SESA (2607.29468, search-agent self-play) tracked 2026-08-03: Skill-SP routes across a growing skill library rather than co-evolving task/skill memory inside a search agent.
- **Link**: https://arxiv.org/abs/2607.22529

### Training Small LLMs as Spatial Multi-Agent Policies
- **Authors**: Yi Mao, Andrew Perrault
- **Affiliation**: Ohio State University
- **Venue**: arXiv:2608.01425 (Aug 2, 2026)
- **Key Innovation**: In spatial cooperative games, small frozen LLMs prompted with low-level actions earn zero reward — so each game gets a library of **symbolic options** (typed, state-feasible, short-horizon behaviors) drafted by a frontier coding model and executed by a symbolic planner; feasibility guards are synthesized mechanically from random-policy burn-in rollouts (no hand-authored/reward-tuned guards). Per-agent LoRA adapters trained with per-agent multi-agent GRPO (PA-MAGRPO) lift frozen bases from zero to competent play across three games and four small backbones. **Behavioral-audit finding**: reward and cooperation decouple — a rising reward curve can just mean one agent learned to do the whole task while its partner idles; behavioral evaluation must sit alongside reward. Macro-action Dec-POMDP framing for asynchronous options.
- **Link**: https://arxiv.org/abs/2608.01425

---

## Summary Statistics

- **Total new papers**: 6 (all verified via arXiv abs pages; confirmed absent from wiki before writing)
- **Categories with new papers**: 3 of 7 (Game RL, Game Foundation Models, Related Techniques); 4 categories had no new papers this window and cross-reference prior dailies
- **Key venues**: arXiv (May–Aug 2026; freshest window Jul 24 – Aug 3, 2026)
- **Notable trends**:
  - **World foundation models unify perception/action**: Orca's Next-State-Prediction over a shared world latent (125K hrs video + 160M event annotations) extends the game-world-model line from task-specific engines toward a general world model
  - **NPCs promoted from background pixels to first-class entities**: ReactiveGWM decouples player controls from NPC behavior and transfers NPC interaction logic zero-shot across games
  - **Game-derived RL benchmarks**: ARC-RL breaks the "robots only from real hardware" norm by benchmarking locomotion RL on game bestiary morphologies with stylistic reward constraints
  - **Self-evolution consolidates around skills**: Skill-SP (skill library + dynamic routing) joins PopuLoRA and SESA as the skill-memory answer to self-play/self-improvement instability
  - **Multi-agent LLM training matures but needs behavior audits**: PA-MAGRPO + symbolic options rescues small frozen LLMs in spatial games, while showing reward alone misreports cooperation (echoes PTCG-Bench self-evolution findings)
  - **Sports/tactical niches**: curling gets its first ML treatment (DDPG on continuous stochastic actions, critic as tactical-decision support)
