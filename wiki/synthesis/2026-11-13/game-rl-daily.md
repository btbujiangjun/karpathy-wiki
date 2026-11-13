# Game RL & Game AI Bot — Daily Paper Digest (2026-11-13)

- **Date**: 2026-11-13
- **Window**: ~2026-11-08 → 2026-11-11 (recent arXiv submissions/revisions available at query time)
- **Scope**: Game RL and decision-making in games, LLM-powered game agents and NPC intelligence, game/world/foundation models, gameplay-data pretraining, game benchmarks and environments, industry game AI deployment, and related techniques (action representations, social coordination, ideation-as-game).
- **Method note**: Discovery used arXiv Export API queries and arXiv abstract pages via `webfetch`/`curl` in this run (`websearch` was unavailable). Metadata, abstracts, venues, affiliations, and reported results below are taken from arXiv pages/API responses fetched on 2026-11-13 and are **author-reported** unless otherwise noted. Affiliations are listed as "Not explicitly listed in arXiv metadata" when not present on the abstract page. Papers already covered in `wiki/synthesis/2026-11-12/game-rl-daily.md` and `wiki/synthesis/2026-11-11/game-rl-daily.md` were intentionally de-emphasized.

## Executive Summary

This window highlights **deployable and real-time game-agent systems**, **action/world representations extracted from foundation models**, and **game environments as probes of agent coordination and ideation**. On the systems side, **GARP** (2611.11064) brings generative NPC agents into a Godot game-engine loop on local 3B hardware, combining planning, memory, reflection, emotion, needs, and personality with latency-oriented scheduling. On the industry/deployment side, **SkinAdvisor** (2611.15023, accepted AAAI 2027 IAAI-27) operationalizes multimodal sales forecasting for in-game skin production planning in a live release cycle. For foundation/world models, **OnlyAct** (2611.14420) extracts scene-invariant action representations from pretrained V-JEPA 2 embeddings for action-conditioned world models, while **Game-Enhanced Embodied Learning** (2611.13819) uses 223+ hours of human gameplay recordings (events + foresight pretraining) to improve downstream robot-policy fine-tuning. Benchmark/probing work frames interaction as games: **Re-Search** (2611.14487) turns ICML 2026 idea rediscovery into a Twenty Questions-style two-player game to diagnose LLM ideation bottlenecks, and **Rational Use of Time** (2611.14766) uses the cooperative card game *The Mind* to study temporal social coordination in humans and AI agents.

## 1) Game AI Bots, LLM Agents, and NPC Intelligence

### GARP: Real-Time Generative Agents on Local Hardware in a Game Engine
- **Title (English)**: GARP: Real-Time Generative Agents on Local Hardware in a Game Engine
- **Authors**: Piero Molino, Patrick John Chia, Federico Bianchi, Jonathan P. Chen, Paul Szerlip
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue / status**: arXiv preprint, 2026-11-08 (13 pages, 13 figures)
- **Abstract (summary)**: GARP is a platform for real-time generative agents inside the Godot game engine. Its Character Behavior System runs the full planning/memory/reflection loop on local hardware with a 3B-parameter open-weight LLM and no cloud service, extending classic generative-agent components with LLM-appraised emotions, Big Five-inspired personality axes, time-growing needs, and pairwise relationships updated after conversations.
- **Key innovations**:
  - Local, real-time generative NPC stack in a production-style game engine (Godot) using 3B open-weight inference.
  - Rich agent state: emotion appraisal, graded personality parameters, needs urgency, and relationship updates coupled to decision prompts.
  - Practical inference/control pipeline: narrows 50+ candidate actions to ~3–8, constrains outputs with JSON schemas, surfaces important memories, and uses layered optimizations (adjustable game clock, decisions ahead of need, multi-tier caching, prompt compression, asynchronous execution).
- **Reported results**: In a nine-scenario evaluation, 25 of 27 runs passed log-based checks; both failures occurred in a birthday-party scenario where a guest omitted the event from a daily plan (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.11064) | [PDF](https://arxiv.org/pdf/2611.11064)
- **Topics**: LLM-powered game agents, NPC intelligence, autonomous gameplay, game bot framework, real-time inference.

## 2) Game Foundation Models, World Models, and Action Representations

### OnlyAct: Extracting Action Representations from Foundation Models for World Models
- **Title (English)**: OnlyAct: Extracting Action Representations from Foundation Models for World Models
- **Authors**: Runjia Li, Minghao Chen, Junyu Xie, Philip Torr, Andrea Vedaldi, Tomas Jakab
- **Affiliation**: Not explicitly listed in arXiv metadata (authors include researchers publicly associated with University of Oxford/VGG; verify full affiliations from PDF)
- **Venue / status**: arXiv preprint, 2026-11-10
- **Abstract (summary)**: OnlyAct targets label-scarce action supervision for video world models by extracting action information from pretrained foundation-model embeddings (V-JEPA 2) rather than learning latent actions from scratch. A label-free contrastive adaptation reshapes frame-pair geometry to preserve motion/action while discarding scene content, avoiding reconstruction-bottleneck trade-offs.
- **Key innovations**:
  - Uses V-JEPA 2 pretrained frame-pair embeddings as an action-rich starting point.
  - Contrastive adaptation pulls together same-motion/different-scene pairs and pushes apart same-scene/different-motion pairs for scene-invariant action extraction.
  - Unified evaluation across action expressiveness, scene invariance, and action-conditioned video generation on robot manipulation, camera navigation, game, and driving benchmarks (many unseen during adaptation).
- **Reported results**: Compared with annotation-free latent-action methods, representations are substantially more expressive while matching scene invariance and yield world models that transfer demonstrated actions to new scenes more faithfully (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.14420) | [PDF](https://arxiv.org/pdf/2611.14420)
- **Topics**: Game/world foundation models, action representations, action-conditioned video world models, generalization.

### Game-Enhanced Embodied Learning with Event and Foresight Pretraining
- **Title (English)**: Game-Enhanced Embodied Learning with Event and Foresight Pretraining
- **Authors**: Lianlei Shan, Han Jin, Yaunchao Ma, Xinpeng Chen, Linhao Zhou, Xin Bin
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue / status**: arXiv preprint, 2026-11-10 (25 pages; cs.RO)
- **Abstract (summary)**: Studies whether human gameplay recordings can supplement robot-policy training via event-and-foresight pretraining for InternVLA-A1.5. The method predicts recorded keyboard/mouse events and adds history-conditioned visual foresight supervision through a frozen video model, using coverage-preserving one-second anchors and attention masking to prevent future-action leakage.
- **Key innovations**:
  - Gameplay-as-supervision pretraining combining discrete event prediction and visual foresight.
  - Data/target construction details: 394 recordings across 20 games, 223.36 recorded hours, 2,072,084 training anchors.
  - Leakage-aware training design (attention mask blocks teacher-forced future actions from foresight queries).
- **Reported results**: After 12,400 pretraining updates and same suite-specific robot fine-tuning, aggregate LIBERO success improves from 85.90% (1,718/2,000) to 90.55% (1,811/2,000), with suite gains +9.2/+6.8/+0.2/+2.4 on Spatial/Object/Goal/Long; task-level outcomes are heterogeneous (24 improvements, 10 declines, 6 ties). Authors note the comparison does not isolate effects of game data, objectives, or training variability (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.13819) | [PDF](https://arxiv.org/pdf/2611.13819)
- **Topics**: Gameplay data, foundation-model pretraining, world/foresight modeling, imitation/behavior learning from games, transfer.

## 3) Game Benchmarks, Environments, and Agent Evaluation

### Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game
- **Title (English)**: Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game
- **Authors**: Muhan Gao, Hangxiao Zhu, Xinqi Su, Yu Zhang, Daniel Khashabi, Kuan-Hao Huang
- **Affiliation**: Not explicitly listed in arXiv metadata (Daniel Khashabi is publicly associated with Johns Hopkins University; verify full affiliations from PDF)
- **Venue / status**: arXiv preprint, 2026-11-10 (15 figures, 10 tables)
- **Abstract (summary)**: Re-Search adapts Twenty Questions into a research-ideation game: given only a published paper's problem, a model must rediscover the core idea by asking yes/no questions. Built from 200 ICML 2026 papers, it tracks idea evolution under binary oracle feedback to isolate ideation from execution.
- **Key innovations**:
  - Game-based evaluation protocol for iterative LLM ideation/search over hypothesis space.
  - Controlled interventions separating question/hypothesis generation from judgment.
  - Trace analysis of exploration/exploitation failure modes in multi-turn questioning.
- **Reported results**: Across six recent LLMs, nearly all progress occurs within the first ~30 of 100 questions; models often recognize good ideas/questions when offered but struggle to generate them, indicating a generation bottleneck (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.14487) | [PDF](https://arxiv.org/pdf/2611.14487)
- **Topics**: Game-based benchmark, two-player/questioning game, agent evaluation, decision-making/search behavior.

### Rational Use of Time for Social Coordination in Humans and AI
- **Title (English)**: Rational Use of Time for Social Coordination in Humans and AI
- **Authors**: Xiulin Yang, Sirisha Gudavalli, Jennifer Hu
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF)
- **Venue / status**: arXiv preprint, 2026-11-10 (30 pages, 16 figures)
- **Abstract (summary)**: Uses the cooperative card game *The Mind*—where players cannot communicate explicitly and must coordinate via timing—to study how humans and AI systems use temporal cues for fine-grained social coordination. Evaluates 150 humans, computer-use agents, and text-prompted LLMs.
- **Key innovations**:
  - Game environment isolating implicit temporal signaling as the coordination channel.
  - Comparative human/AI analysis under identical no-communication cooperative constraints.
  - Bayesian framing of timing as belief inference for partner coordination.
- **Reported results**: Human behavior and frontier-model behavior are both well-captured by a Bayesian timing-based inference strategy, but tested models do not efficiently adapt to partners over repeated interactions as humans do (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.14766) | [PDF](https://arxiv.org/pdf/2611.14766)
- **Topics**: Cooperative game benchmark, multi-agent coordination, implicit communication, decision-making under temporal signals.

## 4) Industry Game AI

### SkinAdvisor: An AI-Driven Decision Framework for Skin Production Planning via Multi-Modal Transformer Sales Forecasting
- **Title (English)**: SkinAdvisor: An AI-Driven Decision Framework for Skin Production Planning via Multi-Modal Transformer Sales Forecasting
- **Authors**: Ge Fan, Kai Wang, Chaoyun Zhang, Yingjie Li, Yuze Liu, Junyang Chen
- **Affiliation**: Not explicitly listed in arXiv metadata (verify from PDF; deployed production system context suggests industry involvement)
- **Venue / status**: Accepted to AAAI 2027 (IAAI-27), arXiv preprint 2026-11-11 (10 pages, 4 figures)
- **Abstract (summary)**: SkinAdvisor supports in-game cosmetic skin production decisions (what to make, when to release, how to price) using SkinCast, a multimodal Transformer that forecasts 180-day per-day sales trajectories for unreleased skins and feeds a Select→Fill→Infer→Sales→ROI→Ranking pipeline.
- **Key innovations**:
  - Multimodal forecasting architecture combining pretrained Informer player-preference time series, Player-Hero-Skin graph embeddings, and lightweight Transformers for skin attributes/release context.
  - Single non-autoregressive 180-day trajectory decoder with local-plus-global day-x positional encoding.
  - End-to-end deployed decision pipeline ranking candidates by forecast-based ROI with multi-candidate comparison.
- **Reported results**: In production for a full release cycle; offline RMSE reduced ~20% vs strongest baseline (Informer) and ~60% vs classical methods; stress tests on 16-core CPU report p99 latency < 8ms and peak throughput > 1100 rps. Authors report deployment lessons on sufficient accuracy granularity and temporal leakage from pretrained embeddings (author-reported).
- **Links**: [arXiv](https://arxiv.org/abs/2611.15023) | [PDF](https://arxiv.org/pdf/2611.15023)
- **Topics**: Industry game AI, deployment, forecasting/decision systems, live-ops planning.

## 5) Coverage Gaps and Follow-ups

- **Game RL / self-play / MARL / PBT / open-ended learning**: No clearly new, high-signal Atari/StarCraft/Dota/Go/chess/poker/NetHack/Minecraft RL or self-play training paper surfaced in this fetch window beyond items likely covered in 11-11/11-12 digests; follow up with broader `cs.LG`/`cs.MA` listings and proceedings (NeurIPS/CoG/AAAI workshops, IEEE ToG) in the next run.
- **Procedural content generation**: No strong new PCG-for-levels/content paper identified in this window from queried arXiv slices; continue targeted queries (`procedural content generation`, `level generation`, `LLM game design`, `PCGML`).
- **Affiliations/venues**: Several arXiv pages lack structured affiliations; verify from PDFs/project pages for camera-ready or institutional attribution when needed.
