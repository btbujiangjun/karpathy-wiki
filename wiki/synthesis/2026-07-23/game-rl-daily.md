---
title: Game RL & Game AI Bot — Daily Paper Digest (July 23, 2026)
type: synthesis
created: 2026-07-23
updated: 2026-07-23
sources: [arxiv, proceedings]
tags: [game-rl, game-ai, self-play, llm-agents, game-foundation-models, pcg, benchmarks, world-models, hierarchical-rl, procedural-generation]
---

# Game RL & Game AI Bot — Daily Paper Digest (July 23, 2026)

**Generated:** 2026-07-23

---

## 1. Game RL / Multi-Agent / Self-Play

### DEPT: Breaking the Impasse in Self-Play RL for Social Language Games
- **Authors:** (ACL 2026)
- **Venue:** ACL 2026 (Long Paper)
- **Key Innovation:** Proposes Dual-scale Evolutionary Policy Training (DEPT) to break evolution impasse in self-play RLVR for open-ended social language games. Introduces time-scaled evolutionary perception with fast/slow value baselines to detect stagnation, and asymmetric advantage reshaping to restore gradient signals. Outperforms SPIRAL, MARS, GRPO, SPAG on multiple social language games while preventing policy degeneration.
- **Link:** [ACL Anthology 2026](https://aclanthology.org/2026.acl-long.2096/)

### Seed: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning
- **arXiv:** [2607.14777](https://arxiv.org/abs/2607.14777)
- **Affiliation:** (July 2026)
- **Key Innovation:** SEED converts completed on-policy trajectories into hindsight skills and distills behavioral effects back into the policy via self-evolving on-policy distillation. The policy simultaneously serves as rollout actor and trajectory analyzer, creating a co-evolving supervision loop. Joint optimization with GRPO provides dense token-level signals from sparse trajectory rewards. Tested on embodied interaction, web navigation, search-based QA, visual reasoning.
- **Link:** [arXiv 2607.14777](https://arxiv.org/abs/2607.14777)

### Multiplayer Interactive World Models with Representation Autoencoders
- **arXiv:** [2607.05352](https://arxiv.org/abs/2607.05352)
- **Affiliation:** (July 2026)
- **Key Innovation:** First multiplayer world model for highly dynamic environments governed by complex physical interactions. Conditions on action streams of multiple agents, attributing scene changes to the correct player. 5B-parameter latent diffusion model trained on 10K hours of Rocket League gameplay generates four-player matches at 20 fps on single Nvidia B200. Rollouts stay stable far beyond training horizon (5 minutes measured, hours in practice with no collapse). Releases dataset, training/inference codebase, and live demo.
- **Link:** [arXiv 2607.05352](https://arxiv.org/abs/2607.05352)

### CORAL: Autonomous Multi-Agent Evolution for Open-Ended Discovery
- **arXiv:** [2604.01658](https://arxiv.org/abs/2604.01658)
- **Key Innovation:** First framework for autonomous multi-agent evolution on open-ended problems. Replaces rigid heuristics with long-running agents that explore, reflect, and collaborate through shared persistent memory and asynchronous execution. 4 co-evolving agents improve best known score from 1363→1103 cycles on Anthropic's kernel engineering task. 3–10× higher improvement rates than fixed evolutionary search baselines.
- **Link:** [arXiv 2604.01658](https://arxiv.org/abs/2604.01658)

### Group-Evolving Agents (GEA): Open-Ended Self-Improvement via Experience Sharing
- **arXiv:** [2602.04837](https://arxiv.org/abs/2602.04837)
- **Key Innovation:** Treats a group of agents as fundamental unit of evolution with explicit intra-group experience sharing. Best GEA agent integrates experiences from 17 unique ancestors (28.3% of population). Achieves 71.0% on SWE-bench Verified and 88.3% on Polyglot, significantly outperforming state-of-the-art open-ended self-evolving methods (56.7% and 68.3%). Improvements stem from workflow/tool enhancements that transfer across GPT and Claude models.
- **Link:** [arXiv 2602.04837](https://arxiv.org/abs/2602.04837)

---

## 2. LLM / VLM Game Agents & NPC AI

### Psy-CoT: Psychology-Grounded Reasoning and Role-Aware Policy Optimization for Game NPCs
- **arXiv:** [2606.27025](https://arxiv.org/abs/2606.27025)
- **Key Innovation:** Psychology-grounded chain-of-thought framework for role-playing game agents with three role-specific reasoning steps: Interaction Perception, Psychological Empathy, Logical Construction. Role-Aware Policy Optimization (RAPO) uses profile–token mutual information to weight gradients asymmetrically—amplifying role-specific tokens under positive advantage while attenuating under negative advantage. Outperforms GRPO by 39% on CharacterEval Behavior sub-metric. Tested on CoSER, CharacterBench, CharacterEval.
- **Link:** [arXiv 2606.27025](https://arxiv.org/abs/2606.27025)

### HeRoN: Mediated RL-LLM Framework for Adaptive NPC Behavior
- **Venue:** Neural Computing and Applications (Springer, 2026)
- **Key Innovation:** Helper-Reviewer-NPC framework integrating RL and LLMs through functional separation and critique-based refinement. LLM "Helper" generates context-aware action proposals, lightweight "Reviewer" refines proposals to enforce consistency, RL-controlled "NPC" retains full action execution control. Achieves up to 81% improvement in task success rate over standard RL baselines while substantially reducing constraint-violating actions. Two-phase Reviewer training (supervised + RL alignment).
- **Link:** [Springer](https://link.springer.com/article/10.1007/s00521-026-12275-w)

### Orchestrated Reality: LLM-Driven World Simulation as Parameterized-Action POMDP
- **arXiv:** [2606.16014](https://arxiv.org/abs/2606.16014)
- **Key Innovation:** Formalizes LLM-driven game world for human player as Parameterized-Action POMDP: state is canonical JSON entity tree, actions decompose as (discrete intent kind + structured JSON parameters), agent observes only narrative projection of state. Plan-Diff-Validate-Apply (PDVA) pipeline commits schema-validated JSON deltas. Catalogue of 15 real deployment incidents. Future work: multi-NPC concurrent agency and RL environment deployment.
- **Link:** [arXiv 2606.16014](https://arxiv.org/abs/2606.16014)

### AutoWorldBuilder: Multi-Agent LLM Collaboration for Fictional Worldbuilding
- **arXiv:** [2607.09403](https://arxiv.org/abs/2607.09403)
- **Venue:** JAIR (2026)
- **Key Innovation:** Multi-agent system for game worldbuilding with five integrated components: structured concept network with conflict detection, DAG-based hybrid batch scheduler, four-layer context compression (90% token reduction), iterative review with 8 specialized Auditor agents (pass rates 42%→85%+), skill-driven architecture with differentiated temperature (fantasy:0.9/geography:0.3/race:0.7). 95% success rate across 20 tasks using GPT-OSS 120B and DeepSeek v3.2.
- **Link:** [arXiv 2607.09403](https://arxiv.org/abs/2607.09403)

---

## 3. Game Foundation Models

### NitroGen: Open Foundation Model for Generalist Gaming Agents
- **Venue:** CVPR 2026
- **Affiliation:** NVIDIA / MineDojo
- **Key Innovation:** Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Internet-scale video-action dataset extracted from gameplay videos with input overlays. Unified vision-action model with Gymnasium API wrapper for multi-game evaluation. When fine-tuned, achieves up to 52% relative improvement in task success rates over models trained from scratch. Single round of self-iteration learning boosts 2D metroidvania boss success from 18.7%→53.9%; three rounds →90.5%. Releases dataset, evaluation suite, and model weights.
- **Link:** [NitroGen](https://nitrogen.minedojo.org/)

### Pixels2Play (P2P): Scaling Behavior Cloning for Real-Time Video Game Playing
- **arXiv:** [2601.04575](https://arxiv.org/abs/2601.04575)
- **Key Innovation:** Open recipe for training video game playing foundation model with 8,300+ hours of human gameplay data, 1.2B parameter decoder-only transformer. Real-time inference (20 Hz) on consumer GPU. Systematic study of behavior cloning scaling laws: larger/deeper models achieve higher causality scores in data-abundant regimes, suggesting scaling is one approach to causality in behavior cloning. Custom image tokenization, action decoder, and ground-truth action token conditioning.
- **Link:** [arXiv 2601.04575](https://arxiv.org/abs/2601.04575)

---

## 4. World Models for Games

### AlayaWorld: Interactive Long-Horizon World Modeling
- **arXiv:** [2607.18367](https://arxiv.org/abs/2607.18367) (Full Report)
- **Affiliation:** (July 2026)
- **Key Innovation:** 15B video diffusion transformer generating 24-fps at 540p/720p with bounded visual context (persistent sink frame, compressed temporal history, geometry-aligned spatial memory, recent-frame conditioning). Autoregressive DiT with prompt-switching mechanism, AdaLN camera-control, 3D cache, history-compression, error bank, and discrete autoregressive distillation (30→4 steps per chunk). Best performance on iWorld-Bench for long-horizon generation. Full open-source framework.
- **Link:** [arXiv 2607.18367](https://arxiv.org/abs/2607.18367)

### From Pixels to States: Rethinking Interactive World Models as Game Engines
- **arXiv:** [2607.14076](https://arxiv.org/abs/2607.14076)
- **Key Innovation:** Unified framework examining interactive game world modeling along 4 dimensions: player action control, game state dynamics, state-observation persistence, real-time interactive generation. Categorizes approaches into representative families. Builds scalable data engine for Black Myth: Wukong with 90+ hours of gameplay, frame-aligned actions, ground-truth game states, and structured annotations. Identifies explicit game state integration as key remaining challenge.
- **Link:** [arXiv 2607.14076](https://arxiv.org/abs/2607.14076)

### LingBot-World 2.0 (Infinity): Infinite Worlds with Versatile Interactions
- **arXiv:** [2607.07534](https://arxiv.org/abs/2607.07534)
- **Key Innovation:** Open causal video generation model for interactive world modeling. Achieves unbounded interaction horizon with 720p at 60 fps (distilled from 14B backbone; 1.3B lightweight variant for single GPU). Rich action space (combat, archery, spell-casting, shooting) + on-the-fly environmental changes. Director-Pilot Co-Simulation Framework: VLM "Director" handles macroscopic semantic rules/causal reasoning, Video Generator "Pilot" handles physical dynamics/rendering. Multi-player interface. Only system sustaining hours of generation without degradation.
- **Link:** [arXiv 2607.07534](https://arxiv.org/abs/2607.07534)

### ABot-World-0: Real-Time Interactive World Simulator
- **arXiv:** [2607.19191](https://arxiv.org/abs/2607.19191)
- **Affiliation:** (July 2026)
- **Key Innovation:** Single RTX 5090 GPU as real-time interactive world simulator at 720P up to 16 FPS with 1.2s action-to-first-frame latency, ~19 GiB peak VRAM. Multi-source data (AAA games, simulation engines, internet videos). WorldExplorer agent-driven collection with training feedback. Progressive distillation with LongForcing for long-horizon stability. Reference-character memory for persistent identity. Streaming inference stack with low-bit DiT. Competitive on WorldRoamBench.
- **Link:** [arXiv 2607.19191](https://arxiv.org/abs/2607.19191)

---

## 5. Procedural Content Generation (PCG)

### PCGRLLM: Large Language Model-Driven Reward Design for PCGRL
- **arXiv:** [2502.10906](https://arxiv.org/abs/2502.10906)
- **Key Innovation:** Feedback-based reward generation framework using LLMs for PCGRL. Employs reasoning-based prompt engineering (ToT, GoT) for reward space exploration. Self-alignment and feedback loop: LLM generates reward function → PCGRL trains agent → LLM evaluates content and refines reward. 415.5% improvement over zero-shot generation (0.031→0.187). Tested with two LLMs across four scenarios.
- **Link:** [arXiv 2502.10906](https://arxiv.org/abs/2502.10906)

### HDPCG: High-Dimensional Procedural Content Generation
- **arXiv:** [2602.18943](https://arxiv.org/abs/2602.18943)
- **Key Innovation:** General representation augmenting spatial nodes with additional gameplay dimensions (layers, time, locomotion modes). Dimensional Expanded Graph (DEG) enables planners to reason about geometry and dynamics in single expanded graph. Mechanical feasibility checked during generation via graph search, making geometry and mechanics co-evolve. Multi-scale experiments with unified metrics for controllability, robustness, efficiency, composite quality.
- **Link:** [arXiv 2602.18943](https://arxiv.org/abs/2602.18943)

### VIPCGRL: Human-Aligned PCGRL via Text-Level-Sketch Shared Representation
- **arXiv:** [2508.09860](https://arxiv.org/abs/2508.09860)
- **Key Innovation:** Deep RL framework incorporating three modalities (text, level, sketches) for human-aligned level generation. Shared embedding space trained via quadruple contrastive learning across modalities and human-AI styles. Policy aligned using auxiliary reward based on embedding similarity. Outperforms baselines in human-likeness validated by both metrics and human evaluations.
- **Link:** [arXiv 2508.09860](https://arxiv.org/abs/2508.09860)

---

## 6. Game Benchmarks & Evaluation

### CODE-SHARP: Open-Ended Skill Discovery for Generalist Game Agents
- **arXiv:** [2602.10085](https://arxiv.org/abs/2602.10085)
- **Key Innovation:** Framework leveraging foundation models to autonomously grow and evolve an archive of Skills as Hierarchical Reward Programs (SHARPs)—Python programs encoding success conditions and prerequisite dependencies. Recursive transition operator dynamically routes agent through prerequisite chain at runtime. On Craftax-Classic and XLand, outperforms previous works by 6× and 2.6× in median performance. Only agents capable of crafting iron tools and mining diamonds. Scaled to Craftax-Extended with 90+ discovered SHARPs.
- **Link:** [arXiv 2602.10085](https://arxiv.org/abs/2602.10085)

### AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Continual Learning
- **arXiv:** [2606.24893](https://arxiv.org/abs/2606.24893)
- **Key Innovation:** Open-ended text game generation system for test-time continual learning agents. Generates diverse, long-horizon game environments that challenge agents to learn and adapt continuously during evaluation. Addresses limitation of static benchmarks by providing evolving difficulty and novel scenarios.
- **Link:** [arXiv 2606.24893](https://arxiv.org/abs/2606.24893)

---

## 7. Related Techniques

### HRL-IM/CBS: Hierarchical RL in StarCraft Micromanagement
- **arXiv:** [2606.30092](https://arxiv.org/abs/2606.30092)
- **Key Innovation:** Hierarchical RL with influence map hashing and cluster-based scripts for StarCraft micromanagement. Influence map hashing encodes global battlefield into compact hex codes capturing spatial control. Cluster-based scripts enable dynamic local coordination through adaptive unit partitioning. Hierarchical multi-Q-table architecture decomposes into upper-level clustering strategy selection and lower-level tactical execution. Competitive with deep RL baselines while offering superior sample efficiency and interpretability through transparent Q-table representations.
- **Link:** [arXiv 2606.30092](https://arxiv.org/abs/2606.30092)

### Seirênes: Adversarial Self-Play with Evolving Distractions for LLM Reasoning
- **arXiv:** [2605.11636](https://arxiv.org/abs/2605.11636)
- **Key Innovation:** Shared-parameter self-play RL framework that transforms contextual interference from failure mode into internal training signal. Single policy co-evolves as both Adversary (generates distracting contexts) and Reasoner (recovers core logic). Achieves +10.2, +9.1, +7.2 point average gains across 7 math benchmarks at 4B/7B/30B scales. 4B model's distracting contexts reduce GPT and Gemini accuracy by ~4–5 points, revealing ability to uncover reasoning blind spots.
- **Link:** [arXiv 2605.11636](https://arxiv.org/abs/2605.11636)

### Reward-Free Evolving Agents via Pairwise Validator
- **arXiv:** [2607.14408](https://arxiv.org/abs/2607.14408)
- **Key Innovation:** Replaces scalar reward at accept/reject gate with pairwise validator (frozen LLM comparing parent/child candidates). No training required for validator. Integrates into three published self-evolving engines (GEPA, ADRS, ShinkaEvolve). Adaptive Focus and Soft Elo variants. Matches or exceeds full-reward baseline on majority of settings without labeling cost.
- **Link:** [arXiv 2607.14408](https://arxiv.org/abs/2607.14408)

### Recursive Harness Self-Improvement (RHI)
- **arXiv:** [2607.15524](https://arxiv.org/abs/2607.15524)
- **Key Innovation:** Represents agent harness as prompt-level specification and iteratively refines using pairwise feedback over revision history. Few RHI iterations raise performance ceiling of low-reasoning-effort agents, exceeding max-reasoning-effort while reducing inference cost by up to 60%. Gains arise from improved task-specific context management through more effective inter-agent information flow.
- **Link:** [arXiv 2607.15524](https://arxiv.org/abs/2607.15524)

---

## Key Themes & Trends

1. **Self-Play Evolution Matures:** DEPT breaks evolution impasse in open-ended social games; CORAL achieves autonomous multi-agent evolution; GEA consolidates diversity into sustained progress; SEED creates co-evolving hindsight supervision loops

2. **Interactive World Models at Real-Time:** AlayaWorld (15B DiT, 24fps), LingBot-World-Infinity (hours of 720p/60fps), ABot-World-0 (16fps on single RTX 5090), Multiplayer World Models (5B, 4-player Rocket League 20fps)—all pushing toward real-time game engines

3. **Multiplayer World Models Emerging:** First multiplayer world models condition on multiple agent action streams; LingBot-World introduces Director-Pilot co-simulation; multi-player interface for shared world experience

4. **LLM Game Agents Specialize:** Psy-CoT brings psychology-grounded NPC reasoning; HeRoN's mediated RL-LLM achieves 81% task success improvement; Orchestrated Reality formalizes LLM game worlds as POMDPs

5. **Foundation Models Scale:** NitroGen (CVPR 2026) at 40K hrs/1000+ games with 90.5% boss success via self-imitation; Pixels2Play scales BC laws to 1.2B params; CODE-SHARP discovers 90+ hierarchical skills autonomously

6. **PCG Integrates Multiple Modalities:** PCGRLLM achieves 415% improvement via LLM reward design; HDPCG generalizes beyond geometry to time/dynamics; VIPCGRL unifies text/level/sketch for human alignment

7. **Hierarchical RL for Complex Games:** HRL-IM/CBS brings interpretable hierarchical decomposition to StarCraft; CODE-SHARP discovers hierarchical reward programs; influence maps enable compact battlefield encoding

---

*Next digest: Continue monitoring arXiv cs.AI, cs.GT, cs.LG for new Game RL and Game AI papers.*
