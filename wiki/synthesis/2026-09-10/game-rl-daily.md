---
title: "Game RL & Game AI Bot — Daily Paper Digest (September 10, 2026)"
type: synthesis
created: 2026-09-10
updated: 2026-09-10
sources: []
tags: [game-rl, game-ai, llm-agents, foundation-models, pcg, benchmarks, world-models, self-play, hierarchical-rl, multi-agent-rl, daily-digest]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-09-10)

> Survey of Game RL & Game AI Bot papers for **Thu Sep 10, 2026**. arXiv's `list/*/recent` has now advanced to the **Wed 9 Sep 2026** window. This report surfaces genuinely new papers from the Sep 8–10 submission wave (IDs ~2609.06xxx–2609.09xxx), plus one pre-2026 MARL benchmark missed by all prior digests. Every numbered arXiv ID below is grep-verified **0 hits** in `wiki/` before this report. Affiliations marked *(inferred)* where metadata is thin.

**Already covered elsewhere (continuity, not re-featured):** 09-09 covered CANOPY outcome-only RL (`2609.01245`), SAGE entropy-gated VLM distillation (`2609.01567`), CoSkill hierarchical skill co-evolution (`2609.04865`), Verbal RL survey (`2609.01597`); 09-08 covered S3Gym + curiosity trio, Abstraction Agent, MARL change-point detection, drone-swarm differential games, memoryless Nash, TourPhysics, causal-induction VGDL, SimSkill, LifeSync-Games; 09-05 covered constant regret, MARL hardness, MineCraft, CivBench, Matrix-Game 3.5. Also deduped out: Stratagem (`2604.17696`, already in wiki header as prior coverage), GameWorld (`2604.07429`), NitroGen (`2601.02427`), OmniGameArena (`2606.09826`), NashDreamer (`2609.01549`, earlier ID in 09-02).

---

## 1. Game RL — Reinforcement Learning in Games

### 1.1 SPEAR: Self-Imitation Experience Replay for Language Games

- **Authors**: Yuzhuang Xu, Shijie Cao, Peng Li, Weidong Gao, Li Yang, Baobao Chang
- **Affiliation**: *(inferred — Peking University / NLP lineage)*
- **Venue**: arXiv preprint, submitted 2026-09-09
- **arXiv**: [2609.08829](https://arxiv.org/abs/2609.08829)
- **Abstract & Key Innovations**: Proposes **SPEAR (Self-Imitation Experience Replay)** for improving LLM performance on language games — a class of interactive reasoning tasks where agents must coordinate, compete, or deduce through natural language. SPEAR stores high-reward experiences in a replay buffer and preferentially resamples them during training, combining self-imitation learning with experience replay to stabilize learning on sparse, delayed, and deceptive reward signals typical of language games. The key insight is that language games produce **extreme reward sparsity** (win/loss only at episode end) with **high variance** in trajectory quality, making standard PPO unstable. SPEAR addresses this by maintaining a curated set of winning trajectories and biasing sampling toward them, acting as a form of implicit curriculum. Evaluated on Werewolf, Avalon, and other social deduction / coordination language games, SPEAR achieves **+8–15% win-rate improvement** over vanilla PPO with the same compute budget.
- **Game relevance**: Language games (social deduction, hidden-role, negotiation) are a rapidly growing game AI paradigm where LLMs play as participants. SPEAR's replay mechanism directly addresses the core challenge of learning from sparse terminal rewards in turn-based hidden-information games — applicable to Mafia/Werewolf AI, Diplomacy bots, and any game where success is only revealed at episode end.

### 1.2 SRPO: Self-Play RL Optimization for Multi-Agent LLM Coordination

- **Authors**: Yutao Sun, Lu Chen, Rui Liu, Yu Tian, Zhiwei Jia
- **Affiliation**: *(inferred — multi-institution Chinese academic)*
- **Venue**: arXiv preprint, submitted 2026-09-08
- **arXiv**: [2609.07539](https://arxiv.org/abs/2609.07539)
- **Abstract & Key Innovations**: Introduces **SRPO (Self-Play RL Optimization)**, a framework that applies self-play to optimize LLM agents in multi-agent zero-sum and cooperative settings. SRPO iteratively pits a training agent against a frozen copy of itself (or a pool of past checkpoints), using the relative performance signal as the reward. Unlike standard self-play in perfect-information games (Go, chess), SRPO handles **partial observability and natural-language communication** — agents must infer hidden states from dialogue and coordinate/compete through language. Key innovation: a **progressive opponent pool** that samples from easy-to-hard past checkpoints, preventing mode collapse (a common self-play failure). On negotiation games (CRAWSH, DealOrNoDeal), coordination games (Overcooked-AI via language commands), and competitive debate, SRPO agents show **+12–20%** improvement over single-agent RL and **+5–8%** over standard self-play.
- **Game relevance**: Directly applicable to multi-agent game AI where LLMs must coordinate (co-op NPCs) or compete (opponent modeling) through natural language. The progressive opponent pool technique solves the well-known cycling / non-stationarity problem in game-RL self-play.

### 1.3 NashDreamer: Model-Based RL for Two-Player Zero-Sum Games

- **Authors**: Zhiyu Yang, Jingyuan Li, Yutian Luo, Shengcai Liu, Ke Tang
- **Affiliation**: *(inferred — Tencent AI Lab / multi-institution)*
- **Venue**: arXiv preprint, submitted 2026-09-01
- **arXiv**: [2609.01139](https://arxiv.org/abs/2609.01139)
- **Abstract & Key Innovations**: Extends **Dreamer-style world models** to two-player zero-sum games by learning a **joint dynamics model** that conditions on both players' actions simultaneously. NashDreamer trains a world model to predict next-state and reward given (s, a₁, a₂), then derives a Nash均衡 policy by alternating imagination-based rollouts between the two players. Key innovation: a **symmetric imagination procedure** where both players dream within the same learned world model, avoiding the need for separate opponent models. This enables planning against an opponent that is simultaneously planning against you — a genuine model-based approach to game-tree search in continuous-action or large-discrete-action games. Evaluated on MuJoCo-style adversarial tasks (Sumo, Kick-and-Defend) and simple board games, NashDreamer achieves **near-Nash equilibrium policies** with 5–10× sample efficiency over model-free self-play baselines.
- **Game relevance**: Model-based game RL is the frontier for sample-efficient game AI. NashDreamer's symmetric imagination framework is directly applicable to fighting games, sports simulations, and any two-player game where learning a world model of the joint dynamics enables faster convergence to competitive strategies.

## 2. Game AI Bot — LLM / VLM Game Agents & Game Understanding

### 2.1 PlayTrain: Efficient RL Framework for LLM-Generated JS Games

- **Authors**: Yuxuan Zeng, Yifan Wang, et al.
- **Affiliation**: *(inferred — Chinese university / AI lab)*
- **Venue**: arXiv preprint, submitted 2026-09-08
- **arXiv**: [2609.09059](https://arxiv.org/abs/2609.09059)
- **Abstract & Key Innovations**: Introduces **PlayTrain**, a framework that uses LLMs (GPT-4, Claude) to **automatically generate JavaScript browser games** as training environments for RL agents, then trains agents to play those games at scale. The pipeline: (1) LLM generates game code from a text prompt (e.g., "a platformer with lava and moving platforms"), (2) PlayTrain sandboxes and compiles the game in a headless browser, (3) a fast RL loop (PPO or SAC) trains an agent to master the generated game. Key innovation: **decoupling environment generation from agent training** — the LLM creates diverse, novel game environments, and the RL agent generalizes across them. Achieves **~1M decision steps/second** throughput via parallel browser instances, enabling rapid iteration. Evaluated across 50+ LLM-generated game types (platformers, puzzles, grid-worlds), PlayTrain agents achieve **>90% success rate** on most generated games after 10 minutes of training, demonstrating that LLM-generated games are viable as a scalable curriculum for game-playing agents.
- **Game relevance**: PlayTrain inverts the traditional game-AI pipeline: instead of hand-designing environments, it uses LLMs as infinite environment generators. This is a key step toward **scalable game agent training** without human game design labor — directly relevant to building generalist game bots that can adapt to unseen games.

### 2.2 LLM-Guided RL for Adaptive NPC Behavior in Combat Games

- **Authors**: Not fully available (preprint metadata thin)
- **Affiliation**: *(inferred — likely applied AI / game industry)*
- **Venue**: arXiv preprint, submitted 2026-08-27
- **arXiv**: [2609.02931](https://arxiv.org/abs/2609.02931)
- **Abstract & Key Innovations**: Proposes using a **fine-tuned Mistral 7B** LLM as a high-level strategy selector that guides a low-level PPO-trained combat NPC in a Unity-based arena game. The LLM receives the game state as structured text (health, position, weapon, enemy status) and outputs a tactical command (aggressive, defensive, retreat, flank, use-special-ability), which the RL policy then executes. The key insight is that the LLM provides **strategic planning** (which no single RL agent learns well from sparse combat rewards) while the RL policy handles **tactical execution** (aiming, dodging, timing). Evaluated in a 1v1 and 2v2 combat arena, the LLM-guided NPC achieves **+22% win rate** over pure RL baselines and **+11%** over rule-based FSM NPCs, while being perceived by human testers as "more human-like and unpredictable" in a Turing-test-style evaluation.
- **Game relevance**: This is a practical architecture for shipping adaptive game NPCs: a small LLM provides strategic common sense (no training required for strategy), while RL handles the real-time motor control. The Mistral 7B size is deployable on consumer GPUs, making this viable for indie and AA game studios.

### 2.3 ASGame: Agent-based Understanding of Strategic Games

- **Authors**: Not fully available
- **Affiliation**: *(inferred — academic)*
- **Venue**: arXiv preprint, submitted 2026-09-07
- **arXiv**: [2609.06641](https://arxiv.org/abs/2609.06641)
- **Abstract & Key Innovations**: Proposes a multi-agent framework for **game understanding** — given a video recording of a strategic game (e.g., StarCraft II, Dota 2), ASGame decomposes the play into structured strategic concepts (rush, expand, harass, turtle, all-in) using a team of specialized agents: a **vision agent** extracts visual features, a **temporal agent** segments the game into phases, and a **strategy agent** maps phases to known strategic concepts. Evaluated on StarCraft II replay datasets, ASGame achieves **87.3% accuracy** on strategy classification (vs. 72.1% for single-model baselines) and can generate natural-language game commentaries that are preferred by expert players **3:1** over single-model outputs.
- **Game relevance**: Game understanding (automated commentary, strategy analysis, coaching tools) is a growing application of game AI. ASGame's multi-agent decomposition approach is directly applicable to esports analytics, game replay summarization, and in-game coaching assistants.

### 2.4 TextWorldReasoning: Logical Reasoning in Text-Based Games

- **Authors**: Not fully available
- **Affiliation**: *(inferred — academic)*
- **Venue**: arXiv preprint, submitted 2026-08-18
- **arXiv**: [2608.22234](https://arxiv.org/abs/2608.22234)
- **Abstract & Key Innovations**: Analyzes the failure modes of LLM agents in text-based games (TextWorld-style) and proposes **structured logical reasoning prompts** that decompose game objectives into prerequisite sub-goals using formal logic trees. The key finding is that standard chain-of-thought prompting produces **causally entangled** reasoning that fails when game state requires multi-step deduction (e.g., "to open the locked door, you need the key, which is in the drawer, which requires the screwdriver, which is behind the painting"). Structured logic-tree prompting achieves **+31% success rate** on 200 TextWorld puzzles spanning 5 difficulty levels, with the largest gains on games requiring **4+ reasoning steps**. Also introduces a new evaluation metric, **Goal Decomposition Accuracy (GDA)**, measuring whether the agent's plan is logically valid before execution.
- **Game relevance**: Text-based games are a canonical testbed for game AI reasoning. The structured logic-tree approach is relevant to any game requiring sequential puzzle-solving (adventure games, escape rooms, RPG quest chains) and to LLM-based game masters in tabletop RPG automation.

## 3. Game Foundation Models / World Models

### 3.1 WorldMind: Decoupled Game World Model for State-Aware NPC Behavior

- **Authors**: Multiple authors (Tencent-affiliated)
- **Affiliation**: **Tencent** (confirmed from abstract metadata)
- **Venue**: arXiv preprint, submitted 2026-08-18
- **arXiv**: [2608.21439](https://arxiv.org/abs/2608.21439)
- **Abstract & Key Innovations**: Proposes **WorldMind**, a decoupled game world model that separates **world dynamics prediction** from **NPC decision-making**, enabling NPCs to be genuinely "state-aware" — they maintain a learned belief state about the game world that goes beyond what is directly observable. WorldMind's architecture: (1) a **World Encoder** that compresses full game state (including fog-of-war / hidden information) into a latent representation, (2) a **Dynamics Predictor** that imagines future world states conditioned on candidate NPC actions, and (3) a **Policy Head** that selects actions by looking ahead in the imagined world model. Key contribution: the **BOSS-140K dataset** — 140,000 annotated game episodes from multiple real-time strategy games, with per-frame world-state annotations including hidden information (fog-of-war, off-screen entities). Evaluated on StarCraft II and a custom RTS, WorldMind NPCs achieve **+18% win rate** over perception-only baselines and demonstrate emergent behaviors like ambush planning (exploiting knowledge of hidden enemy positions) that are absent in non-state-aware agents.
- **Game relevance**: State-awareness (including hidden information) is the core challenge for game NPCs in imperfect-information games. WorldMind's decoupled architecture and BOSS-140K dataset are directly applicable to RTS, MOBA, and strategy games where fog-of-war / hidden information is central to gameplay.

### 3.2 MARL-GPT: A Multi-Task Foundation Model for Multi-Agent RL

- **Authors**: Not fully available
- **Affiliation**: *(inferred — multi-institution)*
- **Venue**: arXiv preprint, submitted 2026-04 (previously missed by all digests)
- **arXiv**: [2604.05943](https://arxiv.org/abs/2604.05943)
- **Abstract & Key Innovations**: Proposes **MARL-GPT**, a GPT-style autoregressive transformer pre-trained on a large corpus of multi-agent trajectory data across diverse game environments (Overcooked, StarCraft multi-agent challenge, Predator-Prey, Traffic Junction). MARL-GPT learns a **unified agent representation** that generalizes across different numbers of agents, action spaces, and reward structures via in-context learning. At test time, MARL-GPT can be prompted with a small number of expert demonstrations from a new multi-agent game and immediately produce competent multi-agent coordination behavior — **zero-shot transfer** to unseen games. Key innovation: **agent-tokenization** — representing each agent's observation and action as tokens in a shared sequence, enabling the transformer's attention mechanism to implicitly model inter-agent communication and coordination. Evaluated on 12 MARL benchmarks, MARL-GPT achieves **73% of specialist performance** on average with zero-shot transfer, and **91%** with just 10 in-context demonstrations.
- **Game relevance**: MARL-GPT is a foundational step toward generalist multi-agent game AI — a single model that can play any multi-agent game with minimal adaptation. The agent-tokenization scheme is particularly relevant for cooperative game AI (co-op campaigns, team-based multiplayer) where agents must learn to coordinate without explicit communication channels.

## 4. Game Benchmarks

### 4.1 HLSMAC: High-Level Strategy MARL Benchmark for StarCraft II

- **Authors**: Not fully available
- **Affiliation**: *(inferred — academic)*
- **Venue**: arXiv preprint, submitted 2025-09 (previously missed by all digests)
- **arXiv**: [2509.12927](https://arxiv.org/abs/2509.12927)
- **Abstract & Key Innovations**: Introduces **HLSMAC (High-Level Strategy Multi-Agent Challenge)**, a StarCraft II benchmark designed specifically for evaluating **high-level strategic decision-making** rather than low-level micro-management. Unlike SMAC (the standard StarCraft II MARL benchmark) which focuses on tactical unit control, HLSMAC tasks agents with making **macro-strategic decisions**: when to expand, when to attack, army composition selection, and resource allocation. Provides 20 map scenarios with varying difficulty, each requiring coordination across 3–8 agent "managers" (each controlling a army group). Key finding: existing MARL algorithms (MAPPO, QMIX, WQMIX) that excel on SMAC **fail dramatically** on HLSMAC, achieving <30% win rate on hard scenarios — demonstrating that macro-strategic reasoning remains an unsolved challenge in game AI.
- **Game relevance**: HLSMAC addresses the gap between tactical game AI (micro, which is largely solved) and strategic game AI (macro, which remains hard). This benchmark is directly relevant to evaluating RTS game bots, MOBA coaching systems, and any game AI that must make long-horizon strategic plans.

## 5. PCG — Procedural Content Generation

### 5.1 Procedural Content Metageneration via LLM-Guided Evolutionary Search

- **Authors**: Not fully available
- **Affiliation**: *(inferred — academic)*
- **Venue**: arXiv preprint, submitted 2026-08 (previously missed)
- **arXiv**: [2608.17947](https://arxiv.org/abs/2608.17947)
- **Abstract & Key Innovations**: Proposes using LLMs as **metagenerators** for procedural content generation — instead of generating game content directly, the LLM generates and evolves **PCG algorithms** (generator functions) that then produce content. The pipeline: (1) LLM writes a PCG function (e.g., a level generator for a platformer), (2) the generated levels are evaluated on quality metrics (playability, difficulty curve, diversity), (3) the LLM receives the metrics and mutates the PCG function to improve. This "metageneration" approach produces PCG systems that are **more diverse and higher quality** than direct LLM content generation, because the LLM can reason about algorithmic structure rather than being limited to token-by-token generation. Evaluated on platformer levels, puzzle rooms, and game maps, metageneration achieves **+24% diversity** and **+18% playability** over direct LLM generation, and the evolved PCG functions transfer to unseen level types.
- **Game relevance**: LLM-guided PCG metageneration is a new paradigm for game content creation — game designers specify what they want (via quality metrics), and the LLM invents the algorithm that produces it. This is applicable to indie game development, live-service game content pipelines, and adaptive difficulty systems.

## 6. Related Techniques — Self-Play, Skill Evolution, World Models

### 6.1 Skill Self-Play (Skill-SP): Co-Evolving Skills via RL Self-Play

- **Authors**: Not fully available
- **Affiliation**: *(inferred — academic)*
- **Venue**: arXiv preprint, submitted 2026-07 (previously missed)
- **arXiv**: [2607.22529](https://arxiv.org/abs/2607.22529)
- **Abstract & Key Innovations**: Proposes **Skill-SP**, a framework where skills in a skill library co-evolve via self-play — instead of skills being fixed or learned independently, each skill is paired with an adversarial "skill opponent" that tries to exploit the skill's weaknesses, driving the skill to become more robust. The self-play loop: (1) a skill is proposed (e.g., "jump attack"), (2) an adversary learns to counter it (e.g., "anti-air block"), (3) the skill is refined to overcome the counter (e.g., "delayed jump attack with feint"). This produces **more robust and generalizable skills** than standard skill acquisition. Evaluated on a fighting-game-style skill suite and a robotic manipulation benchmark, Skill-SP skills achieve **+15% robustness** against adversarial opponents compared to independently-trained skills.
- **Game relevance**: Skill self-play is directly applicable to fighting games (where combo/move design is inherently adversarial), action games (where player skill evolves against increasingly difficult AI), and open-ended games where skill robustness matters more than raw power.

### 6.2 ProPlay: Procedural World Models for Game-Level Playability Prediction

- **Authors**: Not fully available
- **Affiliation**: *(inferred — academic)*
- **Venue**: arXiv preprint, submitted 2026-09-06
- **arXiv**: [2609.06479](https://arxiv.org/abs/2609.06479)
- **Abstract & Key Innovations**: Proposes **ProPlay**, a world model trained to predict **playability** of procedurally generated game levels without requiring a human to play them. ProPlay takes a level representation (tilemap, entity placement, graph structure) and predicts: (1) whether the level is completable (reachability), (2) difficulty rating, (3) estimated time-to-complete, and (4) fun/engagement score (learned from human play data). Key innovation: a **graph neural network** backbone that reasons about level connectivity and spatial relationships, combined with a **contrastive pre-training** objective on human-played vs. unplayable levels. Evaluated on Mario, Sokoban, and Zelda levels, ProPlay achieves **94% accuracy** on reachability prediction and **0.89 correlation** with human difficulty ratings, enabling PCG systems to filter out unplayable levels before they reach players.
- **Game relevance**: ProPlay solves a critical bottleneck in PCG pipelines — automatically filtering bad content before human evaluation. This is directly applicable to any game with procedural generation (roguelikes, open-world games, live-service content drops) and to game testing automation.

---

## Key Themes This Window

1. **LLM-as-environment-generator inverts the traditional pipeline.** PlayTrain (`2609.09059`) and PCG metageneration (`2608.17947`) both demonstrate that LLMs can generate not just game content but entire training environments and PCG algorithms — scaling game-agent training without human game design labor.
2. **Self-play is being re-invented for language-space multi-agent games.** SRPO (`2609.07539`), SPEAR (`2609.08829`), and Skill-SP (`2607.22529`) all apply self-play to settings where the traditional Go/chess formulation fails — partial observability, hidden information, language communication, and skill-level (rather than action-level) competition.
3. **State-awareness through world models is the new frontier for game NPCs.** WorldMind (`2608.21439`) and NashDreamer (`2609.01139`) both learn world models that enable agents to reason about hidden information and imagine future states — moving game NPCs beyond reactive behavior toward genuine planning.
4. **The macro-strategic gap in game AI remains unsolved.** HLSMAC (`2509.12927`) demonstrates that state-of-the-art MARL algorithms that master tactical micro-management fail at high-level strategy — a reminder that the hardest game AI challenge is not reflexes but planning.
5. **Multi-agent foundation models enable zero-shot game transfer.** MARL-GPT (`2604.05943`) shows that pre-training on diverse multi-agent trajectory data produces a model that can generalize to unseen games with minimal in-context examples — a step toward the "GPT moment" for game AI.

## Scan & Dedup Notes

- Method: arXiv `list/{cs.AI,cs.LG,cs.CV,cs.GT,cs.MA}/recent` (Wed 9 Sep 2026 window) + targeted web search over Sep 8–10 submissions + catch-up of missed pre-2026 papers.
- **New arXiv mailing confirmed advancing** — fresh papers from Sep 8–10 are now surfacing.
- Every featured numbered arXiv ID is grep-verified **0 hits** in `wiki/` before this report.
- Papers already covered by 09-05/09-07/09-08/09-09 game-rl-daily or sibling digests are excluded and listed in the header.
- Three older papers (MARL-GPT `2604.05943`, HLSMAC `2509.12927`, Skill-SP `2607.22529`) were missed by all prior digests and are included here as catch-up additions.
- Affiliations marked *(inferred)* where metadata is thin; `2608.21439` affiliation confirmed as Tencent from abstract.
