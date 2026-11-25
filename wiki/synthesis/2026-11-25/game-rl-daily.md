---
title: "Game RL & Game AI Bot — Daily Digest (2026-11-25)"
type: synthesis
created: 2026-11-25
updated: 2026-11-25
sources: []
tags: [game-rl, game-ai, reinforcement-learning, multi-agent-rl, self-play, foundation-models, pcg, benchmarks, world-models, npc, industry-game-ai, vlm, daily-digest, game-benchmarks, procedural-content-generation, offline-rl]
---

# Game RL & Game AI Bot — Daily Digest (2026-11-25)

- **Date**: 2026-11-25
- **Window**: new papers via arXiv Export API (`export.arxiv.org/api/query`, sorted by `submittedDate`), queries covering the 7 topics + related techniques; window ≈ 2026-11-21 → 2026-11-25; abstracts/authors/dates from Atom feed; venue from arXiv comments where present (most are plain arXiv preprints); all metrics/claims author-reported.

## Executive Summary

This window shows continued maturation of LLM/VLM-powered game agents (** gamer / Ram **): papers on LLM-based NPCs, executable game-playing program synthesis (PlayScriptBench), self-improvement benchmarks (AstronautBench), and game-AI benchmarks (Off-the-Shelf Autonomous Agents for Playtesting). Classic **Game RL** papers keep flowing — AlphaDefect (Expert-Level AI for Slay the Spire 2), Think Offline Act in Real Time (self-improving visual agents), multi-player social games as verifiable training grounds for LLMs, and chess via VLA adaptation. On the foundations side, generalist vision-language-action game models (Gamer, NitroGen) and state-aware world action models for multi-agent 3D environments (SWAM) move toward agent generality. Industry remains thin — no major studio papers found; the closest are AutoPILOT (UnityBench mentions) and a CPU-only bot-mining framework for MMORPGs.

---

## 1) Game RL — Atari, StarCraft, Dota, Chess, Poker, Minecraft, NetHack, etc.; Multi-Agent RL in Games; Self-Play; Population-Based Training; Open-Ended Learning

### 2611.31821v1 — "Exploring Multi-Player Social Games as Verifiable Training Grounds for Large Language Models" (2026-11-24)
- **Authors**: Keyu He; Michael Li; Jiarui Liu; Mingqian Zheng; Koichi Onoue; Tongshuang Wu; Maarten Sap
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-24)
- **Abstract**: Multi-player social games provide open-ended communication while yielding an objective outcome — a natural verifiable reward for RLVR. Using three social games, we explore how much social intelligence Qwen3 models can acquire through SFT and RLVR.
- **Key innovations**: Verifiable social games as RLVR training grounds (17–54 pp win-rate lift over a much stronger Gemma-3-27B); paired SFT/RLVR protocols separating skill from memory; a 3.3M-game evaluation spanning win rates.
- **Links**: [arXiv](https://arxiv.org/abs/2611.31821v1)

### 2611.31076v1 — "AlphaDefect: Expert-Level AI for Slay the Spire 2" (2026-11-23)
- **Authors**: Qiyue Chen; Taian Yu; Junpei Komiyama; Haobo Huang
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-23)
- **Abstract**: AlphaDefect is expert-level AI for Slay the Spire 2, a single-player deck-building game requiring long-term planning under heavy randomness.
- **Key innovations**: Expert-level deck-building game AI; self-play-ish training on its own play traces.
- **Links**: [arXiv](https://arxiv.org/abs/2611.31076v1)

### 2611.26012v1 — "When Agents Play Differently: Localizing Human--Agent Behavioral Divergence with Conditional Distributional Testing" (2026-11-19)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-19)
- **Abstract**: Evaluating whether artificial agents behave like humans requires comparing not just average outcomes but entire behavioral distributions across game states.
- **Key innovations**: Conditional distributional testing to localize human-agent divergence in games.
- **Links**: [arXiv](https://arxiv.org/abs/2611.26012v1)

### 2611.24590v1 — "Think Offline, Act in Real Time: Self-Improving Visual Game Agents through Code" (2026-11-18)
- **Authors**: Zipeng Qiu; Shusheng Xu; Jiale Li; Yukun Zhou; Chenyue Li; Wenshuang Li; Tongkai Yang; Binhang Yuan
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-18)
- **Abstract**: Pre-trained models can read screens and reason about games, yet on an unfamiliar game an agent still has to learn to play. We ask how an agent can bootstrap itself to play a new game with minimal interaction.
- **Key innovations**: Code-as-policy self-improvement for visual game agents on unseen games.
- **Links**: [arXiv](https://arxiv.org/abs/2611.24590v1)

### 2611.26910v1 — "AstronautBench: Measuring Agent Self-Improvement Across Episodes Through Knowledge, Evidence, and Progress" (2026-11-19)
- **Authors**: Congyuan Yu; Runping Tian
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-19)
- **Abstract**: LLM agents are expected to improve themselves from their own experience across episodes, with fixed weights. Self-improvement in an embodied environment is hard to measure; AstronautBench provides a measurable scenario.
- **Key innovations**: Benchmark for agent self-improvement measurement; episodic knowledge/evidence/progress accounting.
- **Links**: [arXiv](https://arxiv.org/abs/2611.26910v1)

### 2611.12676v1 — "VLA Adaptation with Real and Simulated Data: A Case Study on Robotic Chess" (2026-11-09)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-09)
- **Abstract**: Vision-language-action models are trained as general-purpose foundation models for robot learning and require fine-tuning for each specific task. This paper presents a case study adapting a VLA model to chess, mixing real and simulated data.
- **Key innovations**: Real+sim data mixture for VLA chess fine-tuning; adaptation recipe on chess.
- **Links**: [arXiv](https://arxiv.org/abs/2611.12676v1)

### 2611.11136v2 — "From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models" (2026-11-08)
- **Authors**: Changran Liu; Qi Wu; Wenchao Ma; Sharon X. Huang; Haomiao Jiang
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-08)
- **Abstract**: Training vision-language-action (VLA) models to follow gameplay instructions across diverse games is limited by the cost of collecting demonstrations. We propose a fully automated ability-training pipeline from game generation.
- **Key innovations**: Fully automated ability training via procedurally generated games; VLA models for game playing.
- **Links**: [arXiv](https://arxiv.org/abs/2611.11136v2)

---

## 2) Game AI Bot — LLM/VLM Game Agents, NPC Intelligence, Game Bot Frameworks, Autonomous Gameplay, Decision-Making in Games

### 2611.28202v1 — "AutoPILOT: A Visual Agent Harness for Real-Time Gameplay" (2026-11-20)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-20)
- **Abstract**: Existing harnesses turn each model call into ≤1 action, so the agent acts only as often as the model thinks. AutoPILOT changes this: per model call the model can send a primitive, start an open-loop macro, or write a closed-loop controller that keeps playing from the screen without further calls until it hands control back. Evaluated in AFK-Bench: 120 browser games grouped by how they respond to inaction.
- **Key innovations**: Three-level control interface (primitive / open-loop macro / closed-loop controller with handback); AFK-Bench (120 diverse real-time/clock-paused browser games); gains over VISTA: +30.3 pts real-time, +35.1 pts GameWorld.
- **Links**: [arXiv](https://arxiv.org/abs/2611.28202v1)

### 2611.29372v1 — "Emotion-Aware and Context-Grounded Dialogue Agents for Personalized Video Game Interactions" (2026-11-22)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-22)
- **Abstract**: We present ChatNPC, a game companion that dynamically personalizes its responses in real time based on players' emotional shifts to enhance interaction.
- **Key innovations**: Emotion-aware, context-grounded dialogue agents for personalized game experiences.
- **Links**: [arXiv](https://arxiv.org/abs/2611.29372v1)

### 2611.28812v1 — "The Humming Revachol: A Dialogue Network Analysis of Narrative Power in Disco Elysium" (2026-11-21)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-21)
- **Abstract**: This study applies social network analysis to the narrative RPG *Disco Elysium*, examining how narrative power is distributed among the characters.
- **Key innovations**: Dialogue-network analysis of narrative power in a game; connects to NPC behavior modeling.
- **Links**: [arXiv](https://arxiv.org/abs/2611.28812v1)

### 2611.05427v1 — "LLM-based NPCs in Video Games: A Systematic Mapping Study" (2026-11-02)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-02)
- **Abstract**: For decades, non-player characters (NPCs) have been driven by rule-based systems whose personalities and interactions are scripted before gameplay; LLM-based NPCs are now an active research area. This systematic mapping study catalogs recent work on LLM-based NPCs in video games.
- **Key innovations**: Systematic mapping of LLM-based NPC research; trends/gaps in NPC intelligence.
- **Links**: [arXiv](https://arxiv.org/abs/2611.05427v1)

### 2611.14431v1 — "Demonstration of MANA: Multi-perspective Alignment of NPC Agents" (2026-11-10)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-10)
- **Abstract**: We present MANA (Multi-perspective Alignment of NPC Agents), an interactive approach for authoring NPC behavior through embodied demonstration.
- **Key innovations**: Multi-perspective alignment of NPC agents for authored behavior.
- **Links**: [arXiv](https://arxiv.org/abs/2611.14431v1)

---

## 3) Game Foundation Models — Generalist Game Models, Game-Playing FMs, Vision-Language Game Agents

### 2611.18397v3 — "Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent" (2026-11-13)
- **Authors**: Run Luo; Kuan Zhang; Qi Deng; Yukun Chen; Zhihao Yang; Yufei Zhang; Renrong Hu; Yi Zhang; Guiyu Ma; Tianyu Fan; Longze Chen; Hao Sun
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-13)
- **Abstract**: gamer is a generalist agent framework built for long-horizon tasks in complex interactive environments. Its end-to-end architecture plays games from raw visual frames and user instructions without intermediate game-state APIs.
- **Key innovations**: Generalist VLA foundation model for long-horizon real-time game play.
- **Links**: [arXiv](https://arxiv.org/abs/2611.18397v3)

### 2611.23140v1 — "GameRealm: Grounding Visual Learning in Interactive Games" (2026-11-17)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-17)
- **Abstract**: Visual foundation models are central to physical intelligence, yet their development remains constrained by fragmented training datasets. GameRealm grounds visual learning in interactive games, unifying environments for training.
- **Key innovations**: Visual game grounding as foundation-model pretraining substrate.
- **Links**: [arXiv](https://arxiv.org/abs/2611.23140v1)

### 2611.26807v1 — "NitroGen: Observations on the Action Dynamics, Visual Instruction Following, and Spatial Exploration" (2026-11-19)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-19)
- **Abstract**: NitroGen is an open vision-action foundation model for game control, trained by behavior cloning on online gameplay videos; the paper presents observations on its action dynamics, visual instruction following, and spatial exploration.
- **Key innovations**: Open vision-action foundation model for game control.
- **Links**: [arXiv](https://arxiv.org/abs/2611.26807v1)

---

## 4) Procedural Content Generation — RL for Level Generation, LLM for Game Content, Automated Game Design

- **2611.11136v2** (Section 1, Game RL): "From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models" (2026-11-08) — procedural game generation as the ability-training substrate for VLA models.
- **2611.04241v2** — "AceAction-5M: Hierarchical Goals for Generalist Action Learning Across 3D Game Worlds" (2026-11-03) — 3D game worlds as a goal-learning environment.

---

## 5) Game Benchmarks — New Game-Based Evaluation Suites, Agent Benchmarks in Game Environments

### 2611.31570v1 — "Off-the-Shelf Autonomous Agents for Game Playtesting" (2026-11-23)
- **Authors**: Ayush Maniar; Eryk Banatt
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-23)
- **Abstract**: Off-the-shelf autonomous agents for game playtesting — studying how ready-made agents can perform playtesting tasks, reducing reliance on human operators.
- **Key innovations**: Off-the-shelf agent benchmarks for game playtesting.
- **Links**: [arXiv](https://arxiv.org/abs/2611.31570v1)

### 2611.17681v1 — "OCTAVE: A Capability-Resolved Benchmark for End-to-End HTML5 Game Generation" (2026-11-13)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-13)
- **Abstract**: Complete game generation requires agents to coordinate rules, interactions, states, and presentation over a long development process; OCTAVE is a capability-resolved benchmark for end-to-end HTML5 game generation.
- **Key innovations**: Capability-resolved benchmark for end-to-end game generation.
- **Links**: [arXiv](https://arxiv.org/abs/2611.17681v1)

### 2611.30989v1 — "WorldLeague: Benchmarking Physical Agency" (2026-11-23)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-23)
- **Abstract**: AI systems can now operate Blender, follow instructions in complex video games, and manipulate objects with robot arms — WorldLeague benchmarks this "physical agency" across environments.
- **Key innovations**: Benchmark for physical agency of AI systems.
- **Links**: [arXiv](https://arxiv.org/abs/2611.30989v1)

### 2611.28368v1 — "Schedule, Rank, Profile: Continuous Evaluation of LLM Agents in Games" (2026-11-20)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-20)
- **Abstract**: Games are a robust test for LLM agents: they require sequential decisions, adversarial or cooperative interaction, and state tracking; continuous evaluation of LLM agents in games.
- **Key innovations**: Continuous evaluation framework for LLM agents in games.
- **Links**: [arXiv](https://arxiv.org/abs/2611.28368v1)

---

## 6) Industry Game AI — Papers from Major Game Studios, Game AI Deployment, Real-Time Game Inference

### 2611.30502v1 — "A CPU-Only Framework for Mining Collectively-Behaving Bots in MMORPGs" (2026-11-23)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-23)
- **Abstract**: MMORPGs continually face automated programs (bots) that disrupt gameplay balance and in-game economies; we present a CPU-only framework based on an unsupervised Transformer to detect collectively-behaving bots.
- **Key innovations**: CPU-only bot detection framework for MMORPGs.
- **Links**: [arXiv](https://arxiv.org/abs/2611.30502v1)

### 2611.28202v1 — "AutoPILOT: A Visual Agent Harness for Real-Time Gameplay" (2026-11-20)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-20)
- **Abstract**: Existing harnesses turn each model call into ≤1 action; AutoPILOT adds three-level control (primitive / open-loop macro / closed-loop controller). Evaluated in AFK-Bench (120 browser games).
- **Key innovations**: AFK-Bench; real-time agent harness; mentions UnityBench in related work.
- **Links**: [arXiv](https://arxiv.org/abs/2611.28202v1)

---

## 7) Related Techniques — Self-Play RL, Curiosity-Driven Exploration, Hierarchical RL, Imitation Learning, Inverse RL, Reward Shaping, World Models for Games, Model-Based RL, Offline RL for Games

### 2611.30042v1 — "SWAM: State-aware World Action Model for Multi-Agent 3D Environments" (2026-11-23)
- **Authors**: Not stated on arXiv metadata (see PDF p.1)
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-23)
- **Abstract**: Interactive world models generate virtual environments autoregressively from player actions and visual history; SWAM extends this to multi-agent 3D environments.
- **Key innovations**: State-aware world action model for multi-agent 3D envs.
- **Links**: [arXiv](https://arxiv.org/abs/2611.30042v1)

### 2611.24590v1 — "Think Offline, Act in Real Time: Self-Improving Visual Game Agents through Code" (2026-11-18)
- **Authors**: Zipeng Qiu; Shusheng Xu; Jiale Li; Yukun Zhou; Chenyue Li; Wenshuang Li; Tongkai Yang; Binhang Yuan
- **Affiliation**: Not stated on arXiv metadata (see PDF p.1)
- **Venue/conference**: arXiv preprint (2026-11-18)
- **Abstract**: Self-improving visual game agents that learn by writing code; acts in real time against unfamiliar games.
- **Key innovations**: Offline/self-improving agents via code synthesis for real-time gameplay.
- **Links**: [arXiv](https://arxiv.org/abs/2611.24590v1)
