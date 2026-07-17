---
title: "Game RL & Game AI Bot Daily Digest — 2026-07-17"
type: synthesis
created: 2026-07-17
updated: 2026-07-17
sources: []
tags: [game-rl, game-ai, self-play, multi-agent, foundation-models, pcg, benchmark, world-model, hierarchical-rl, industry]
---

# Game RL & Game AI Bot — Daily Paper Digest (2026-07-17)

A curated survey of recent arXiv papers and proceedings on reinforcement learning in games, LLM-powered game agents, game foundation models, procedural content generation, game benchmarks, industry game AI deployment, and related techniques.

---

## 1. Game RL — Self-Play & Multi-Agent Reinforcement Learning

### 1.1 COvolve: Adversarial Co-Evolution of LLM-Generated Policies and Environments

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Mar 2026
- **Link:** https://arxiv.org/abs/2603.28386
- **Abstract & Key Innovations:**
  Co-evolutionary framework where LLMs generate both environments and agent policies as executable Python code. Models interaction as a two-player zero-sum game ensuring adversarial co-evolution. Computes mixed-strategy Nash equilibrium (MSNE) to produce a meta-policy preventing catastrophic forgetting. Tested on urban driving, symbolic maze-solving, and geometric navigation. Achieves open-ended learning without predefined task distributions or manual intervention.

### 1.2 ResDreamer: Self-supervised Hierarchical Visual Reasoning with World Model

- **Authors:** XuYuanFei et al.
- **Venue:** arXiv preprint, May 2026
- **Link:** https://arxiv.org/abs/2605.17537
- **Abstract & Key Innovations:**
  Hierarchical world model where each higher layer learns to reconstruct residuals of the layer below, enabling progressive abstraction. Purely self-supervised under the "Bitter Lesson." Modulates lower-level predictions with upper-layer residuals. Achieves SOTA sample efficiency and parameter efficiency in 3D open-world environments (Minecraft combat). Only method with non-near-zero success on high-difficulty Shulker combat tasks. 50-200M parameters.

---

## 2. Game AI Bot — LLM-Powered Game Agents & NPC Intelligence

### 2.1 Bounded Autonomy: Controlling LLM Characters in Live Multiplayer Games

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Apr 2026 (updated Jul 2026)
- **Link:** https://arxiv.org/abs/2604.04703
- **Abstract & Key Innovations:**
  Control architecture for LLM characters in live multiplayer games with three interfaces: agent-agent, agent-world, and player-agent. Instantiated with probabilistic reply-chain decay, embedding-based action grounding with fallback, and "whisper" — a lightweight soft-steering technique letting players influence character next moves without overriding autonomy. Deployed in a live multiplayer social game. Frames controllability as a distinct runtime control problem for LLM game characters.

### 2.2 Psy-CoT & RAPO: Psychology-Grounded Reasoning for Game NPCs

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Jun 2026
- **Link:** https://arxiv.org/abs/2606.27025
- **Abstract & Key Innovations:**
  Psy-CoT is a psychology-grounded chain-of-thought framework decomposing pre-response reasoning into Interaction Perception, Psychological Empathy, and Logical Construction. RAPO (Role-Aware Policy Optimization) uses profile–token mutual information to weight gradients asymmetrically — amplifying role-specific tokens under positive advantage while attenuating under negative. Outperforms GRPO on CoSER, CharacterBench, and CharacterEval. Designed for general-purpose role-playing agents including game NPCs.

### 2.3 CASCADE: Cascading Architecture for Low-Cost Social Coordination

- **Authors:** Yizhi Xu
- **Venue:** arXiv preprint, Apr 2026
- **Link:** https://arxiv.org/abs/2604.03091
- **Abstract & Key Innovations:**
  Three-layer architecture for scalable game NPC social coordination. Macro State Director (Level 1) maintains world-state variables. Modular Coordination Hub (Level 2) decomposes state changes through domain-specific components and routes directives to tag-defined groups. Tag-Driven NPCs (Level 3) execute via behavior trees, invoking LLMs only for player-facing dialogue. Drastically reduces token cost vs. full per-agent prompting. Introduces Action-Dialogue Decoupling for prompt injection safety.

### 2.4 WISE: Long-Horizon Minecraft Agent with Why-Which Reasoning

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Jun 2026
- **Link:** https://arxiv.org/abs/2606.12852
- **Abstract & Key Innovations:**
  Long-horizon Minecraft agent with Causal Event Graph augmenting episodic memory with explicit causal structure (e.g., cow → CAN_OBTAIN → beef). Opportunistic Task Scheduler dynamically re-prioritizes subtasks when causally relevant opportunities are detected. Multi-scale progressive exploration (global → regional → local). 30% increase in sequential sparse task success with 26.4% lower completion time vs. MrSteve. 44% increase in adaptive non-sequential task success with 42.5% less time.

### 2.5 ProPlay: Procedural World Models for Self-Evolving LLM Agents

- **Authors:** Yijun Ma, Zehong Wang, et al.
- **Venue:** arXiv preprint, Jun 2026
- **Link:** https://arxiv.org/abs/2606.12780
- **Abstract & Key Innovations:**
  Procedural world model supporting procedure-level preplay — agents rehearse future procedural paths using learned world knowledge. Abstracts successful trajectories into procedures organized in a procedure graph with causal transitions. Reliability record embeddings estimate task-specific contribution. Before each episode, simulates future procedural trajectories; after execution, refines graph using environment feedback. Consistently improves over strong baselines on public benchmarks.

### 2.6 Orchestrated Reality: LLM-Driven World Simulation as Parameterized-Action POMDP

- **Authors:** Y Huang, Chenmiao Li, Chaowei Fang
- **Venue:** arXiv preprint, Jun 2026
- **Link:** https://arxiv.org/abs/2606.16014
- **Abstract & Key Innovations:**
  Formalizes an LLM-driven game world as a Parameterized-Action POMDP: state is a tree of canonical JSON entities, actions decompose as (kind, structured parameters), observations are narrative projections. Uses a Plan-Diff-Validate-Apply (PDVA) pipeline committing schema-validated JSON deltas. Singleton orchestration agent analogous to tabletop-RPG Game Master. 15 illustrative incidents from real deployment.

### 2.7 OPINE-World: Programmatic World Modeling for ARC-AGI-3

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Jul 2026
- **Link:** https://arxiv.org/abs/2607.01531
- **Abstract & Key Innovations:**
  LLM agent learns object-centric programmatic world model online from interaction. Two cooperating agents: action agent hypothesizes dynamics, synthesizer agent writes code with replay verification. Bayesian "ontology error" steers exploration toward objects whose behavior isn't yet explained. Solves 20 of 25 ARC-AGI-3 games without per-game training, surpassing baseline1 (leading single-agent coding baseline). Action-efficiency score 78.4 against human baseline.

### 2.8 RWML: Reinforcement World Model Learning for LLM-based Agents

- **Authors:** Xiao Yu, Baolin Peng, et al.
- **Venue:** arXiv preprint, Feb 2026
- **Link:** https://arxiv.org/abs/2602.05842
- **Abstract & Key Innovations:**
  Self-supervised method learning action-conditioned world models using sim-to-real gap rewards. Aligns simulated next states with observed states in pre-trained embedding space. More robust than next-token prediction (which prioritizes token fidelity over semantics). Combined with task-success rewards, outperforms direct RL by 6.9 and 5.7 points on ALFWorld and τ² Bench. Matches expert-data training performance.

---

## 3. Game Foundation Models — Generalist Game-Playing Models

### 3.1 Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents

- **Authors:** ByteDance / Seed team
- **Venue:** arXiv preprint, Oct 2025
- **Link:** https://arxiv.org/abs/2510.23691
- **Abstract & Key Innovations:**
  Generalist game agent with unified, scalable action space anchored to native keyboard–mouse inputs (not API/GUI). Pre-trained on 500B+ tokens across game trajectories, OS, web, and simulation. Key techniques: decaying continual loss to reduce causal confusion and Sparse-Thinking strategy balancing reasoning depth vs. inference cost. Achieves ~2× success rate over previous SOTA on open-world Minecraft, outperforms GPT-5, Gemini-2.5-Pro, and Claude-4-Sonnet on FPS benchmarks. Three model versions: MoE-mini, MoE-Large, and Dense (Qwen2.5-VL-7B).

### 3.2 Odysseus: Scaling VLMs to 100+ Turn Decision-Making via RL

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, May 2026
- **Link:** https://arxiv.org/abs/2605.00347
- **Abstract & Key Innovations:**
  Studies RL-based training of VLMs for long-horizon (>100 turns) decision-making in Super Mario Land. Proposes adapted PPO with lightweight turn-level critic substantially improving training stability over GRPO/Reinforce++. Pretrained VLMs provide strong action priors improving sample efficiency. Odysseus framework achieves at least 3× average game progress vs. frontier models. Exhibits in-game and cross-game generalization while maintaining general-domain capabilities.

### 3.3 Towards Generalist Game Players: Foundation Models in the Game Multiverse

- **Authors:** Kuan Zhang, Dongchen Liu, et al.
- **Venue:** arXiv preprint, May 2026
- **Link:** https://arxiv.org/abs/2605.09965
- **Abstract & Key Innovations:**
  Comprehensive survey tracing generalist game player lifecycle across Dataset, Model, Harness, and Benchmark. Identifies five fundamental trade-offs bounding the system. Charts a five-level roadmap from single-game mastery to the "creator stage" where agents simultaneously create and evolve within theoretical game multiverse. Argues game multiverse is the ultimate ground for training and evaluating AGI.

### 3.4 Pixels2Play (P2P): Open Behavior Cloning for 3D Gameplay

- **Authors:** Yuguang Yue, Irakli Salia, et al.
- **Venue:** arXiv preprint, Jan 2026
- **Link:** https://arxiv.org/abs/2601.04575
- **Abstract & Key Innovations:**
  Open recipe for training a video game foundation model from 8300+ hours of human gameplay data, all released under open license. Decoder-only transformer with auto-regressive action output, operating at 20Hz on consumer GPU (RTX 5090). Systematically studies scaling laws of behavior cloning — larger models achieve lower test loss and higher causality scores. Shows increasing model depth and data size improves causal reasoning in gameplay policies. Up to 1.2B parameters.

### 3.5 GameVerse: Can Vision-Language Models Learn from Video-based Reflection?

- **Authors:** Kuan Zhang, Dongchen Liu, et al.
- **Venue:** arXiv preprint, Mar 2026
- **Link:** https://arxiv.org/abs/2603.06656
- **Abstract & Key Innovations:**
  Comprehensive video game benchmark enabling a reflective visual interaction loop. Novel "reflect-and-retry" paradigm assesses how VLMs internalize visual experience. Cognitive hierarchical taxonomy spanning 15 globally popular games with dual action space (semantic + GUI control). Best results combining failure trajectories and expert tutorials — a training-free analogue to RL + SFT.

---

## 4. Procedural Content Generation — RL & LLM for Level/Content Design

### 4.1 WCRL: Learning Local Constraints for RL Content Generators

- **Authors:** (Research team)
- **Venue:** arXiv preprint, 2026
- **Link:** https://arxiv.org/abs/2605.13570
- **Abstract & Key Innovations:**
  Combines Wave Function Collapse (WFC) with PCGRL by constraining the action space of an RL generator with constraints learned by WFC. Enables global properties (playability) while adhering to local visual constraints. Applied to Lode Runner levels. Best generators produce visually satisfying and playable puzzle-platform levels. Demonstrates that random partial collapse during training yields more robust, generalizable policies.

### 4.2 MultiGen: Level-Design for Editable Multiplayer Worlds in Diffusion Game Engines

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Mar 2026
- **Link:** https://arxiv.org/abs/2603.06679
- **Abstract & Key Innovations:**
  Introduces explicit external memory (persistent state independent of model context window) into video world models. Decomposes generation into Memory, Observation, and Dynamics modules. Gives users direct, editable control over environment structure via editable memory. Naturally extends to real-time multiplayer rollouts with coherent viewpoints and consistent cross-player interactions. Addresses key interactivity limitations in diffusion game engines.

### 4.3 High-Dimensional PCG (HDPCG): Beyond Geometry-Only Generation

- **Authors:** (Research team)
- **Venue:** arXiv preprint, Feb 2026
- **Link:** https://arxiv.org/abs/2602.18943
- **Abstract & Key Innovations:**
  Framework elevating non-geometric gameplay dimensions (layers, time, locomotion modes) to first-class coordinates. Direction-Space augments geometry with layer dimension and validates reachability in 4D. Direction-Time uses time-expanded graphs capturing action semantics. Shared four-stage pipeline: skeleton generation → controlled grounding → high-dimensional validation → multi-metric evaluation. Validated via Unity case studies recreating VVVVVV-style and Dishonored-style mechanics.

### 4.4 PCGRL+: Scaling, Control and Generalization in RL Level Generators

- **Authors:** Sam Earle, Zehua Jiang, Julian Togelius
- **Venue:** arXiv preprint, Aug 2024
- **Link:** https://arxiv.org/abs/2408.12525
- **Abstract & Key Innovations:**
  Implements PCGRL environments in JAX for GPU-parallel training. Replicates prior results and trains for 1 billion timesteps. Introduces randomized level sizes and frozen "pinpoints" to counter overfitting. Partial observation sizes learn more robust design strategies for OOD generalization. Demonstrates that additional agents in multi-agent PCGRL provide performance, generalization, and efficiency gains.

### 4.5 Playtrace Reconstructive Partitioning (PRP) — Cake Representation

- **Authors:** (Research team)
- **Venue:** arXiv preprint, Jul 2026
- **Link:** https://arxiv.org/abs/2607.12097
- **Abstract & Key Innovations:**
  Novel "cake" representation encoding game levels over time as discrete timesteps. PRP performs binary space partitioning across time matching dynamic entities. Achieves 100% playability without hand-authored Sokoban dynamics knowledge. Matches or outperforms six baselines (including PCGRL) in playability and solution diversity. Domain-agnostic representation that implicitly encodes dynamic information.

---

## 5. Game Benchmarks — Evaluation Suites & Agent Benchmarks

### 5.1 OmniGameArena: Unified UE5 Benchmark for VLM Game Agents with IDC

- **Authors:** Mingxian Lin, Shengju Qian, et al.
- **Venue:** arXiv preprint, Jun 2026
- **Link:** https://arxiv.org/abs/2606.09826
- **Abstract & Key Innovations:**
  Real-time benchmark of 12 newly built Unreal Engine 5 games spanning Solo (7), PvP (3), and Coop (2). Improvement Dynamics Curve (IDC) — an agentic-reflection harness where a tool-using reflector LLM autonomously refines a bounded skill prompt across multiple rounds. Beyond cold-start scores, exposes how scores evolve across reflection rounds and how learned skills behave on held-out variants. Evaluates 12 VLM agents on leaderboard and 4 under IDC.

### 5.2 GameWorld: Standardized Evaluation of Multimodal Game Agents

- **Authors:** (NUS team)
- **Venue:** arXiv preprint, Apr 2026
- **Link:** https://arxiv.org/abs/2604.07429
- **Abstract & Key Innovations:**
  Benchmark with 34 browser games (5 genres) and 170 tasks. Two interfaces: Computer-Use Agents (raw keyboard/mouse) and Generalist Multimodal Agents (semantic action space). Outcome-based state-verifiable evaluation — injects JavaScript bridge exposing serialized gameAPI state for deterministic, fully verifiable signals. Evaluates 18 model-interface pairs. Even best agents far from human capabilities (overall progress 12.4–21.2% success rate). Includes real-time variant GameWorld-RT.

### 5.3 MineExplorer: Open-World Exploration Benchmark in Minecraft

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, May 2026
- **Link:** https://arxiv.org/abs/2605.30931
- **Abstract & Key Innovations:**
  Evaluates MLLM agents' sustained open-world exploration in Minecraft. Multi-agent synthesis workflow (task selector, scene designer, milestone agent, Minecraft expert, validator) produces significantly more reliable instances than single-agent baseline. 1,497 knowledge-controlled atomic tasks and 813 human-validated composite instances (1-hop to 4-hop). Strong models handle single-hop but degrade sharply on multi-hop tasks. Larger models and thinking modes don't consistently improve performance.

### 5.4 TextAtari: 100K-Frame Game Playing with Language Agents

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, 2025
- **Link:** https://arxiv.org/abs/2506.04098
- **Abstract & Key Innovations:**
  Benchmark for evaluating language agents on 100,000-step decision-making tasks. Translates Atari visual states into rich text descriptions. 23 classic Atari games spanning Action, Puzzle/Strategy, Sports, and Arcade genres. Evaluates Qwen2.5-7B, Gemma-7B, Llama3.1-8B across zero-shot, few-shot CoT, and reflection. >90% of scenarios fall below 10% human capability. Prior knowledge integration (manuals, demonstrations) yields >100% average improvement. CoT and reflection show inconsistent benefits.

### 5.5 SciCrafter: Minecraft Discovery-to-Application Benchmark

- **Authors:** Zhou Ziheng et al.
- **Venue:** arXiv preprint, Apr 2026
- **Link:** https://arxiv.org/abs/2604.24697
- **Abstract & Key Innovations:**
  Minecraft-based benchmark operationalizing the discovery-to-application loop through parameterized redstone circuit tasks. Frontier models (GPT-5.2, Gemini-3-Pro, Claude-Opus-4.5) plateau at ~26% success rate. Decomposes loop into four capacities: knowledge gap identification, experimental discovery, knowledge consolidation, application. Reveals that bottleneck is shifting from "solving problems right" to "raising the right problems."

---

## 6. Industry Game AI — Deployment & Real-Time Systems

### 6.1 KRAFTON AI for Games: Three Fronts (ICML 2026)

- **Authors:** Kangwook Lee (KRAFTON CAIO)
- **Venue:** ICML 2026 Social Event, Jul 2026 (COEX Seoul)
- **Link:** https://www.invenglobal.com/articles/23482/ai-for-games-krafton-highlights-three-fronts
- **Abstract & Key Innovations:**
  Industry keynote outlining three fronts for game AI: (1) In-game agents that cooperate/compete with players, (2) Interactive world models challenging traditional game engines, (3) Production AI transforming development pipeline. KRAFTON's 150-person AI research org launched "PUBG ALLIE" — an in-game AI agent that talks, teams up, and fights alongside players. Fully on-device LLM with three-layer memory (in-context, retrieval, cross-session). Data collected from thousands of players in internet cafes. First game with on-device LLM agents (inZOI, 1M+ copies sold).

### 6.2 Sony AI GT Sophy: Coachable Agent for Horizon Forbidden West

- **Authors:** Peter Stone (Sony AI)
- **Venue:** ICML 2026 Social Event, Jul 2026
- **Link:** (Conference presentation)
- **Abstract & Key Innovations:**
  GT Sophy was the first AI to defeat human champions in real-time control (Nature 2022). Now expanded: a single RL policy handles diverse playstyles (long-range, CQC) with a real-time style slider. Applied to Horizon Forbidden West QA — every possible action path can be explored. Key breakthrough: learns from just 10–15 human demonstrations (down from 30). 30ms inference latency for real-time 30fps. World's largest commercial deployment of end-to-end RL agent (Gran Turismo 7 on PS5).

### 6.3 NC AI: Generative AI Production Pipeline Lessons

- **Authors:** Kim Min-jae (NC AI CTO)
- **Venue:** ICML 2026 Social Event, Jul 2026
- **Link:** (Conference presentation)
- **Abstract & Key Innovations:**
  Shared lessons from applying generative AI to game production. Deeply integrated text/image generation into planning and concept art. Proprietary tools for 3D mesh, texture, sound generation. Localization tool generating multilingual voice + lip-sync from Korean text. Motion search for game-ready animations. Key finding: AI NPCs were technically capable but players preferred dense, human-written narratives. Players wanted idealized characters, not real-life likenesses. Built "Monkey Test" agents for automated QA.

### 6.4 PCSP: One Policy, Infinite NPCs — Persona-Traceable Shared RL for UE5

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, May 2026
- **Link:** https://arxiv.org/abs/2605.23652
- **Abstract & Key Innovations:**
  Single RL policy conditioned on frozen LLM embeddings of persona descriptions for scalable NPC control. InfoNCE trajectory-consistency + KL diversity training. On 300-persona life-sim: 17× above chance for compositional zero-shot persona identification, Spearman ρ≈0.73 semantic-behavioral alignment, 22× faster inference than LLM-as-policy. UE5 deployment: 64 concurrent agents, 1.7% failure rate, sub-frame inference. InfoNCE objective is load-bearing — removing it collapses persona identification to chance.

---

## 7. Related Techniques — World Models, Hierarchical RL, Curiosity, Imitation Learning

### 7.1 HWM: Hierarchical Planning with Latent World Models

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Apr 2026 (updated Jun 2026)
- **Link:** https://arxiv.org/abs/2604.03208
- **Abstract & Key Innovations:**
  Hierarchical MPC framework coupling world models at multiple temporal scales in a shared latent space. Long-horizon model predictions serve as subgoals for short-horizon model via latent matching — no task-specific rewards, skills, or hierarchical policies needed. Learns action encoder compressing primitive actions into latent macro-actions. On real Franka robot: 70% success on pick-and-place from single goal image (vs. 0% for flat planning). 3× less planning compute on long-horizon tasks.

### 7.2 WorldCompass: RL for Long-Horizon Video World Models

- **Authors:** Zehan Wang, Tengfei Wang, et al.
- **Venue:** arXiv preprint, Feb 2026
- **Link:** https://arxiv.org/abs/2602.09022
- **Abstract & Key Innovations:**
  RL post-training framework for interactive video-based world models. Clip-level rollout strategy for autoregressive generation — generates and evaluates multiple samples at a single target clip. Complementary reward functions for interaction-following accuracy and visual quality (suppressing reward hacking). Negative-aware finetuning. On WorldPlay: improves complex composite action accuracy from ~20% to 55%.

### 7.3 AgentOWL: Joint Learning of Hierarchical Neural Options and Abstract World Model

- **Authors:** Wasu Top Piriyakulkij, et al.
- **Venue:** arXiv preprint, Feb 2026
- **Link:** https://arxiv.org/abs/2602.02799
- **Abstract & Key Innovations:**
  Jointly learns abstract world model (abstracting across states and time) and hierarchical neural options in a sample-efficient way. Applied to Object-Centric Atari games. Learns more skills using less data than model-free hierarchical baselines. Possesses learning and generalization capabilities that baselines lack.

### 7.4 AgentOdyssey: Open-Ended Text Game Generation for Continual Learning

- **Authors:** (Multi-institution)
- **Venue:** arXiv preprint, Jun 2026
- **Link:** https://arxiv.org/abs/2606.24893
- **Abstract & Key Innovations:**
  Framework for procedurally generating open-ended text games to evaluate test-time continual learning. Evaluates five key abilities: effective exploration, world knowledge acquisition, episodic memory, long-horizon planning, and adaptive decision-making. Multifaceted diagnostic metrics beyond game progress. Top agents remain far below human performance. Short-term memory benefits multiple agent paradigms. Stronger base models scale performance but even GPT-5 class models struggle.

---

## Summary

**Total papers: 25** across 7 categories.

**Key themes this cycle:**

1. **World models as NPC infrastructure:** CASCADE (coordination-centric, not agent-centric), Orchestrated Reality (POMDP formalization), ProPlay (procedural preplay), and PCSP (shared RL policies) represent four distinct architectural approaches to scalable game AI — from pure coordination to full world simulation.

2. **On-device LLM agents reach production:** KRAFTON's PUBG ALLIE and inZOI demonstrate that on-device LLM agents with three-layer memory are commercially viable. Sony AI's GT Sophy expansion to Horizon Forbidden West shows RL agents learning from just 10-15 human demonstrations.

3. **Self-play for transferable reasoning matures:** COvolve introduces adversarial co-evolution with MSNE meta-policies; ResDreamer shows hierarchical residual world models solving 3D open-world combat with 50-200M parameters.

4. **Foundation model scaling in games:** Game-TARS (500B tokens, keyboard-mouse native) outperforms GPT-5/Gemini-2.5-Pro on FPS; Odysseus scales VLM RL to 100+ turns; Pixels2Play releases 8300+ hours of open gameplay data.

5. **Benchmark explosion:** 6 new benchmarks this cycle — OmniGameArena (UE5, 12 games, IDC), GameWorld (34 browser games, state-verifiable), MineExplorer (multi-hop exploration), TextAtari (100K steps), SciCrafter (redstone circuits), AgentOdyssey (open-ended text games).

6. **LLM agents still far from human:** Even frontier models plateau at 26% on SciCrafter, <10% human on TextAtari, and drop sharply on multi-hop MineExplorer tasks. The bottleneck shifts from "solving problems right" to "raising the right problems."
