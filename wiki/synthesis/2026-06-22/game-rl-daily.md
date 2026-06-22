---
title: "Game RL & Game AI Bot — Daily Survey (2026-06-22)"
type: synthesis
created: 2026-06-22
updated: 2026-06-22
tags: [game-rl, game-ai, game-foundation-models, pcg, game-benchmarks, self-play, world-models, arxiv]
---

# Game RL & Game AI Bot — Daily Survey (2026-06-22)

> Comprehensive survey of recent papers across Game RL, Game AI Bots, Game Foundation Models, Procedural Content Generation, Game Benchmarks, Industry Game AI, and related techniques. Compiled 2026-06-22.

---

## Table of Contents

1. [Game RL — Reinforcement Learning in Games](#1-game-rl--reinforcement-learning-in-games)
2. [Game AI Bot — LLM-Powered Game Agents](#2-game-ai-bot--llm-powered-game-agents)
3. [Game Foundation Models](#3-game-foundation-models)
4. [Procedural Content Generation](#4-procedural-content-generation)
5. [Game Benchmarks](#5-game-benchmarks)
6. [Industry Game AI](#6-industry-game-ai)
7. [Related Techniques — Self-Play, Curiosity, World Models](#7-related-techniques)

---

## 1. Game RL — Reinforcement Learning in Games

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning

- **Authors**: (NVIDIA / academia)
- **Affiliation**: NVIDIA, academia
- **Venue**: arXiv 2026
- **Abstract**: Studies RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Proposes adapted PPO with lightweight turn-level critic that substantially improves training stability over critic-free methods (GRPO, Reinforce++). Pretrained VLMs provide strong action priors improving sample efficiency vs classical deep RL. Achieves 3× average game progress vs frontier models. Demonstrates cross-game generalization.
- **Link**: [arXiv:2605.00347](https://arxiv.org/abs/2605.00347)

---

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning

- **Authors**: B. Liu, L. Guertler, S. Yu, Z. Liu, P. Qi, D. Balcells, M. Liu, C. Tan, W. Shi, M. Lin et al.
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026
- **Abstract**: Introduces SPIRAL, a self-play framework where models learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving versions of themselves. Uses role-conditioned advantage estimation (RAE) to stabilize multi-agent training. Up to 10% improvement across 8 reasoning benchmarks on Qwen and Llama models. Multi-game training yields strongest results.
- **Link**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119)

---

### Think in Games: Learning to Reason in Games via Reinforcement Learning with Large Language Models

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2025
- **Abstract**: Proposes Think-In Games (TiG), bridging declarative and procedural knowledge by reformulating RL decision-making as language modeling. Uses GRPO to refine LLM-generated language-guided policies through environmental feedback. Achieves competitive performance with dramatically lower data and compute demands vs conventional RL. Provides step-by-step natural language explanations.
- **Link**: [arXiv:2508.21365](https://arxiv.org/abs/2508.21365)

---

### Augmenting Game AI with Deep Reinforcement Learning

- **Authors**: A. Sestini, J. Bergdahl, J. Barrette-LaPierre, F. Fuchs, B. Chen, M. Jones, L. Gisslén
- **Affiliation**: European Union / academia / industry
- **Venue**: IEEE Conference, 2026
- **Abstract**: Proposes a framework for training RL models for game AI deployment in AAA production. Analyzes runtime inference constraints, describes practicalities of deploying player-facing ML agents, and identifies bottlenecks including efficient networks, fast training turnaround, and integration with game engines.
- **Link**: [arXiv:2606.20210](https://arxiv.org/abs/2606.20210)

---

### Learning Transferable Skills in Action RPGs via Directed Skill Graphs and Selective Adaptation

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Investigates lifelong learning in Dark Souls III by modeling combat as a directed skill graph with 5 reusable skills (camera, lock-on, movement, dodge, heal-attack). Hierarchical curriculum improves sample efficiency. Selective fine-tuning of 2 skills recovers performance under domain shift with limited interaction budget.
- **Link**: [arXiv:2601.17923](https://arxiv.org/abs/2601.17923)

---

### AlphaExploitem: Going Beyond the Nash Equilibrium in Poker by Learning to Exploit Suboptimal Play

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Extends AlphaHoldem with hierarchical transformer encoder over hand histories and diverse exploitable opponents. Trained via PPO. Captures 2× per-hand EV vs league-only baseline in Kuhn Poker and Leduc Hold'em while remaining close to Nash equilibrium. Generalizes to out-of-distribution opponents.
- **Link**: [arXiv:2605.09150](https://arxiv.org/abs/2605.09150)

---

### SpinGPT: A Large-Language-Model Approach to Playing Poker Correctly

- **Authors**: (Multiple)
- **Affiliation**: LAMSADE, Université Paris-Dauphine
- **Venue**: ACG 2025
- **Abstract**: First LLM tailored to Spin & Go (3-player online poker). Two-stage training: SFT on 320k expert decisions + RL on 270k solver-generated hands. Matches solver actions in 78% of decisions. Achieves 13.4 ± 12.9 BB/100 vs Slumbot in heads-up.
- **Link**: (LAMSADE Dauphine)

---

### Robust Deep Monte Carlo Counterfactual Regret Minimization

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2025
- **Abstract**: Comprehensive analysis of neural MCCFR risks (non-stationary target shifts, action support collapse, variance explosion) with scale-dependent manifestation. Robust Deep MCCFR framework achieves 60% improvement on Kuhn Poker (0.0628 exploitability) and 23.5% on Leduc Poker (0.2386).
- **Link**: [arXiv:2509.00923](https://arxiv.org/abs/2509.00923)

---

### Real-Time Parallel Counterfactual Regret Minimization

- **Authors**: B. Li, L. Huang
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: First parallelization framework for real-time depth-limited CFR solving. Decomposes iteration into 7-stage pipeline with CPU-GPU heterogeneous execution. 3.3–3.4× speedup on Heads-Up NLH, 47–54ms per iteration on trees with 1B+ histories. Desktop-class device (NVIDIA DGX Spark).
- **Link**: [arXiv:2605.19928](https://arxiv.org/abs/2605.19928)

---

### Deep (Predictive) Discounted Counterfactual Regret Minimization

- **Authors**: H. Xu et al.
- **Affiliation**: Academia
- **Venue**: arXiv 2025
- **Abstract**: Efficient model-free neural CFR algorithm. Collects variance-reduced sampled advantages via value network, fits cumulative advantages by bootstrapping, applies discounting/clipping simulating advanced CFR variants. Faster convergence in imperfect-information games.
- **Link**: [arXiv:2511.08174](https://arxiv.org/abs/2511.08174)

---

### Implicit Strategic Optimization: Long-Horizon Decision-Making in Adversarial Poker Environments

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Introduces ISO (Implicit Strategic Optimization) with Strategic Reward Model (SRM) estimating long-run strategic value, and iso-grpo context-conditioned optimistic learning. Proves sublinear contextual regret and equilibrium convergence. Improves long-term return in 6-player NLH and competitive Pokémon.
- **Link**: [arXiv:2602.08041](https://arxiv.org/abs/2602.08041)

---

### Beyond Static Evaluation: Co-Evolutionary Mechanisms for LLM-Driven Strategy Evolution in Adversarial Games

- **Authors**: (Multiple, FAMOU framework)
- **Affiliation**: Academia
- **Venue**: arXiv 2026; AAMAS 2026 MCTF Competition (1st in hardware, 3rd in simulation)
- **Abstract**: Proposes evaluator co-evolution, hierarchical deep evaluation, and weakness pressure for LLM-driven code evolution in adversarial multi-agent games. FAMOU achieves 68% win rate on MCTF 3v3 naval capture-the-flag. Generates tactical structures absent from seed strategies.
- **Link**: [arXiv:2606.10389](https://arxiv.org/abs/2606.10389)

---

### Combining Code Generating LLMs and Self-Play to Iteratively Refine Strategies in Games

- **Authors**: Y. Bachrach, E. Toledo, K. Hambardzumyan, D. Magka, M. Josifoski, M. Jiang, J. Foerster, R. Raileanu, T. Shavrina, N. Cancedda, A. Ruderman, K. Millican, A. Lupu, R. Hazra
- **Affiliation**: Multiple institutions
- **Venue**: IJCAI 2025
- **Abstract**: Uses PSRO framework with LLM code generation for self-play in multi-player games. LLM generates candidate code, bots play in tournaments, Nash equilibrium over population of strategies. Iteratively refines strategies toward game-theoretic optimality.
- **Link**: [IJCAI 2025 Proceedings](https://www.ijcai.org/proceedings/2025/1249)

---

## 2. Game AI Bot — LLM-Powered Game Agents

### Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with Large Language Models

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Extends Shannon's taxonomy of game-playing machines using LLMs. Nemobot environment enables creating, customizing, deploying LLM-powered game agents across 4 game classes (dictionary, solvable, heuristic, learning-based). Integrates RL with human feedback, self-critique, imitation learning, and crowdsourced data.
- **Link**: [arXiv:2604.21896](https://arxiv.org/abs/2604.21896)

---

### PORTAL: Agents Play Thousands of 3D Video Games (Policy Optimization and Reasoning for Tactical Artificial Learning)

- **Authors**: (Multiple)
- **Affiliation**: Industry / Academia
- **Venue**: arXiv 2025
- **Abstract**: LLM generates behavior trees (BTs) in DSL to create game-playing AI across thousands of 3D video games. Decouples tactical planning from execution. Hybrid architecture integrating rule-based nodes with neural networks. First unified approach demonstrated across thousands of distinct 3D games.
- **Link**: [arXiv:2503.13356](https://arxiv.org/abs/2503.13356)

---

### Bounded Autonomy: Controlling LLM Characters in Live Multiplayer Games

- **Authors**: (Multiple)
- **Affiliation**: Academia / Industry
- **Venue**: arXiv 2026
- **Abstract**: Frames bounded autonomy as a control architecture for LLM characters in live multiplayer games. Three interfaces: agent-agent, agent-world, player-agent steering. Instantiates with probabilistic reply-chain decay, embedding-based action grounding, and whisper soft-steering. Deployed in live multiplayer social game.
- **Link**: [arXiv:2604.04703](https://arxiv.org/abs/2604.04703)

---

### Echoes of Others: Real-Time LLM Dialogue Generation for Immersive NPC Interaction

- **Authors**: J. McGrath, M. Lorandi, A. Belz
- **Affiliation**: Academia
- **Venue**: INLG 2025 (Demos)
- **Abstract**: Unreal Engine 5 prototype integrating GPT-4o Mini, OpenHermes-7B, and LoRA-tuned 4-bit variant. Runs on consumer hardware maintaining 60 FPS. Evaluates latency (1.9s, 12.3s, 3.0s) and dialogue quality across RPG scenarios. Demonstrates viability of low-latency NPC conversations on consumer hardware.
- **Link**: [ACL Anthology 2025.inlg-demos.1](https://aclanthology.org/2025.inlg-demos.1.pdf)

---

### Sensi: Learn One Thing at a Time — Curriculum-Based Test-Time Learning for LLM Game Agents

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: LLM agent for ARC-AGI-3 with two-player architecture separating perception from action, curriculum-based learning via external state machine, and database-as-control-plane. Sensi v2 achieves 50–94× sample efficiency (32 interactions vs 1600–3000). Diagnoses self-consistent hallucination cascade in perception.
- **Link**: [arXiv:2603.17683](https://arxiv.org/abs/2603.17683)

---

### Continual Harness: Online Adaptation for Self-Improving Foundation Agents (Gemini Plays Pokémon)

- **Authors**: (Multiple, Google DeepMind)
- **Affiliation**: Google DeepMind
- **Venue**: arXiv 2026
- **Abstract**: Automates manual harness refinement for LLM game agents. Gemini Plays Pokémon system beat Pokémon Blue (May 2025), Yellow Legacy hard mode (Aug 2025), and Crystal (Nov 2025) — first AI to complete multiple Pokémon RPGs. Continual Harness framework enables mid-episode self-improvement without restarts.
- **Link**: [arXiv:2605.09998](https://arxiv.org/abs/2605.09998)

---

### PokéChamp: An Expert-level Minimax Language Agent

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2025
- **Abstract**: Minimax agent powered by LLMs for Pokémon battles. LLMs replace action sampling, opponent modeling, and value function estimation. GPT-4o achieves 76% win rate vs best LLM bot, 84% vs rule-based bot. Llama 3.1 8B still beats GPT-4o-powered Pokéllmon (64%). Projected Elo 1300–1500 (top 30%–10% human). Releases 3M+ battle dataset.
- **Link**: [arXiv:2503.04094](https://arxiv.org/abs/2503.04094)

---

### CrossHA: Training One Model to Master Cross-Level Agentic Actions via Reinforcement Learning

- **Authors**: (Multiple, CraftJarvis)
- **Affiliation**: Academia / Open source
- **Venue**: arXiv 2025
- **Abstract**: Unified agentic model mastering heterogeneous action spaces (API/GUI/robotic) with Multi-Turn GRPO for adaptive action switching. In Minecraft, trained on 30 tasks generalizes to 800+ tasks. Emergent optimization of trajectory efficiency alongside task success.
- **Link**: [arXiv:2512.09706](https://arxiv.org/abs/2512.09706)

---

## 3. Game Foundation Models

### NitroGen: An Open Foundation Model for Generalist Gaming Agents

- **Authors**: L. Magne, A. Awadalla, G. Wang, Y. Xu, J. Belofsky, F. Hu, J. Kim, L. Schmidt, G. Gkioxari, J. Kautz, Y. Yue, Y. Choi, Y. Zhu, L. Fan
- **Affiliation**: NVIDIA, MineDojo
- **Venue**: CVPR 2026 (pp. 21511–21521)
- **Abstract**: Vision-action foundation model trained on 40,000 hours of gameplay across 1000+ games. Large-scale behavior cloning with internet-scale video-action dataset. Fine-tunes to unseen games with up to 52% relative improvement over from-scratch models. Open-source: dataset, evaluation suite, model weights.
- **Link**: [arXiv:2601.02427](https://arxiv.org/abs/2601.02427) | [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Magne_NitroGen_An_Open_Foundation_Model_for_Generalist_Gaming_Agents_CVPR_2026_paper.html)

---

### Game-TARS: Pretrained Foundation Models for Scalable Generalist Multimodal Game Agents

- **Authors**: Z. Wang, X. Li, Y. Ye, J. Fang, H. Wang, L. Liu, S. Liang, J. Lu, Z. Wu, J. Feng et al.
- **Affiliation**: (SEED / Tencent / academia)
- **Venue**: arXiv 2025
- **Abstract**: Generalist game agent with unified keyboard-mouse action space. Pre-trained on 500B+ tokens across OS/web/simulation. Decaying continual loss + Sparse-Thinking strategy. 2× SOTA in Minecraft, near-human generalization in unseen web 3D games, outperforms GPT-5/Gemini-2.5-Pro/Claude-4-Sonnet in FPS.
- **Link**: [arXiv:2510.23691](https://arxiv.org/abs/2510.23691)

---

### Pixels to Play (P2P0.1): A Foundation Model for 3D Gameplay

- **Authors**: Y. Yue, C. Green, S. Hunt, I. Salia, W. Shi, J.J. Hunt
- **Affiliation**: Industry / Academia
- **Venue**: IEEE CoG 2025
- **Abstract**: Foundation model learning to play 3D video games from raw pixels. Behavior cloning on labeled demonstrations + imputed actions from unlabeled videos via inverse dynamics. Decoder-only transformer with autoregressive action output. Competent play on Roblox and MS-DOS titles on single consumer GPU.
- **Link**: [arXiv:2508.14295](https://arxiv.org/abs/2508.14295)

---

### Scaling Behavior Cloning Improves Causal Reasoning: An Open Model for Real-Time Video Game Playing

- **Authors**: (Elefant AI)
- **Affiliation**: Elefant AI
- **Venue**: arXiv 2026
- **Abstract**: Open recipe for game-playing foundation model. Releases 8300+ hours human gameplay, training/inference code, pretrained checkpoints. 1.2B parameter model competitive with humans across 3D games. Investigates scaling laws of BC, finding increasing data and depth leads to more causal policy.
- **Link**: [arXiv:2601.04575](https://arxiv.org/abs/2601.04575)

---

### OpenGame: Open Agentic Coding for Games

- **Authors**: (Multiple)
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026
- **Abstract**: First open-source agentic framework for end-to-end web game creation. Game Skill (Template + Debug) + GameCoder-27B code LLM (3-stage: CPT, SFT, execution-grounded RL). OpenGame-Bench evaluates build health, visual usability, intent alignment. SOTA across 150 diverse game prompts.
- **Link**: [arXiv:2604.18394](https://arxiv.org/abs/2604.18394)

---

### Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Comprehensive survey tracing generalist game players across 4 pillars (Dataset, Model, Harness, Benchmark) and 5 fundamental trade-offs. Five-level roadmap from single-game mastery to creator stage. First systematic investigation of Large Foundation Models as generalist game players through end-to-end lifecycle.
- **Link**: [arXiv:2605.09965](https://arxiv.org/abs/2605.09965)

---

### CreativeGame: Multi-Agent System for Iterative HTML5 Game Generation

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: 7-logical-agent system with CreativeProxyReward (programmatic signals over LLM judgment), lineage-scoped memory, runtime validation, and mechanic-guided planning. MemRL-style runtime RL over episodic memory. Supports interpretable version-to-version evolution.
- **Link**: [arXiv:2604.19926](https://arxiv.org/abs/2604.19926)

---

## 4. Procedural Content Generation

### PCGRLLM: Large Language Model-Driven Reward Design for Procedural Content Generation Reinforcement Learning

- **Authors**: I.-C. Baek, S.-H. Kim, S. Earle, Z. Jiang, N. Jin-Ha, J. Togelius, K.-J. Kim
- **Affiliation**: Academia
- **Venue**: arXiv 2025
- **Abstract**: Extended architecture using LLM feedback and reasoning-based prompting for reward generation in PCGRL. Self-alignment + feedback to iteratively refine reward functions. Achieves performance comparable to humans on story-to-reward generation in 2D environment. Reduces human dependency in game AI development.
- **Link**: [arXiv:2502.10906](https://arxiv.org/abs/2502.10906)

---

### Learning Local Constraints for Reinforcement-Learned Content Generators

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Combines Wave Function Collapse (WFC) local constraints with PCGRL for global properties. Constrains PCGRL action space with WFC-learned constraints. Produces visually satisfying and playable Lode Runner levels. Studies input data size, diversity, and collapse strategies.
- **Link**: [arXiv:2605.13570](https://arxiv.org/abs/2605.13570)

---

### VIPCGRL: Human-Aligned Procedural Level Generation via Text-Level-Sketch Shared Representation

- **Authors**: I.-C. Baek et al.
- **Affiliation**: Academia
- **Venue**: arXiv 2025
- **Abstract**: Vision-Instruction PCGRL with 3 modalities (text, level, sketches). Shared embedding space via quadruple contrastive learning. Auxiliary reward based on embedding similarity. Outperforms baselines in human-likeness via quantitative metrics and human evaluation.
- **Link**: [arXiv:2508.09860](https://arxiv.org/abs/2508.09860)

---

### MultiGen: Level-Design for Editable Multiplayer Worlds in Diffusion Game Engines

- **Authors**: R. Po et al.
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Introduces explicit external memory for diffusion game engines, enabling editable environment structure. Decomposes generation into Memory, Observation, Dynamics modules. Supports real-time multiplayer rollouts with coherent viewpoints and consistent cross-player interactions.
- **Link**: [arXiv:2603.06679](https://arxiv.org/abs/2603.06679)

---

### High-quality Generation of Dynamic Game Content via Small Language Models

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Proposes aggressive fine-tuning of SLMs on deliberately scoped tasks for real-time game content generation. DAG-based synthetic training data. Retry-until-success strategy reaches adequate quality with predictable latency (2.4–9.7s depending on quantization). Practical for offline/single-player deployment.
- **Link**: [arXiv:2601.23206](https://arxiv.org/abs/2601.23206)

---

## 5. Game Benchmarks

### OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics

- **Authors**: M. Lin, S. Qian, Y. Liu, Y.-H. Huang, Y. Wang, W. Huang, Y. Li, F. Zhang, Z. Hu, L. Zhu, X. Wang, X. Qi
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: 12 custom Unreal Engine 5 games (7 Solo, 3 PvP, 2 Coop) with unified action interfaces. Improvement Dynamics Curve (IDC) — agentic-reflection harness with tool-using reflector LLM across multiple rounds. Evaluates 12 VLM agents on cold-start + 4 top agents under IDC.
- **Link**: [arXiv:2606.09826](https://arxiv.org/abs/2606.09826)

---

### GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents

- **Authors**: M. Ouyang, S. Hu, K.Q. Lin, H.T. Ng, M.Z. Shou
- **Affiliation**: NUS (National University of Singapore)
- **Venue**: arXiv 2026
- **Abstract**: 34 browser games across 5 genres (Runner, Arcade, Platformer, Puzzle, Simulation) with 170 tasks. Decouples inference latency from gameplay. State-verifiable evaluators over serialized gameAPI. 18 model–interface pairs evaluated. GameWorld-RT variant for real-time.
- **Link**: [arXiv:2604.07429](https://arxiv.org/abs/2604.07429) | [GitHub](https://github.com/gameworld-project/gameworld)

---

### The PokeAgent Challenge: Competitive and Long-Context Learning at Scale

- **Authors**: (Multiple)
- **Affiliation**: NeurIPS 2025 Competition
- **Venue**: arXiv 2026
- **Abstract**: Large-scale benchmark with Battling Track (20M+ trajectories, 100+ teams) and Speedrunning Track (standardized RPG evaluation). Identifies 3 open challenges: VLM-SLAM for speedrunning, LLM–RL gap in battling, full-game completion with open-source models. NeurIPS 2025 competition.
- **Link**: [arXiv:2603.15563](https://arxiv.org/abs/2603.15563)

---

### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games

- **Authors**: (KRAFTON AI)
- **Affiliation**: KRAFTON AI
- **Venue**: arXiv 2026
- **Abstract**: Benchmark across 12 popular video games covering all major genres. MCP-based plug-and-play interface. Releases fine-tuning dataset of expert LLM gameplay trajectories. Includes game leaderboards, LLM battle arenas, and analyses of input modality, agentic strategies, fine-tuning effects.
- **Link**: [arXiv:2506.03610](https://arxiv.org/abs/2506.03610) | [GitHub](https://github.com/krafton-ai/Orak)

---

### DSGBench: A Diverse Strategic Game Benchmark for Evaluating LLM Agents

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2025/2026
- **Abstract**: Suite of complex strategy games evaluating 5 core capabilities: planning, real-time decision-making, social reasoning, team collaboration, adaptive learning. Unified Gym-based interface. Fine-grained metrics and decision-tracking mechanisms.
- **Link**: [arXiv:2503.06047](https://arxiv.org/abs/2503.06047)

---

### lmgame-Bench: How Good are LLMs at Playing Games?

- **Authors**: (Multiple, lmgame-org)
- **Affiliation**: Academia / Industry
- **Venue**: arXiv 2025
- **Abstract**: Suite of platformer, puzzle, narrative games with Gym-style API. Perception/memory scaffolds to stabilize prompt variance and remove contamination. 13 leading models evaluated. RL on a single game transfers to unseen games and external planning tasks. 86.7% of harnessed runs beat random baseline.
- **Link**: [arXiv:2505.15146](https://arxiv.org/abs/2505.15146)

---

### GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?

- **Authors**: T. Luo, R. Wang, J. Bi, C. Xu, Z. Tang, J. Chen, J. Liang, K. Ji, S. Guo, Y. Du, F. Bu, W. Du, X. Zhang, K. Li, S. Wang, L. Zhang, Y. Liu, X. Lai, C. Li, Y. Guo, Z. Zhang, X. Wang, T. Bai, Z. Li, B. Wang
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026
- **Abstract**: 140 tasks across 15 game families. Agents must produce complete Godot projects with replayable traces. Verifier launches project, replays traces, scores with hidden rubric + multimodal judge. Measures engine grounding, artifact completeness, interactive verification.
- **Link**: [arXiv:2606.17861](https://arxiv.org/abs/2606.17861)

---

### Agentick: A Unified Benchmark for General Sequential Decision-Making Agents

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Gymnasium-native benchmark for evaluating frontier model capabilities with multi-modal observations, procedural generation, per-category diagnostic scoring. Supports RL post-training for sequential decision-making. Vectorizable, oracle trajectories for warm-starting.
- **Link**: [arXiv:2605.06869](https://arxiv.org/abs/2605.06869)

---

### MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: User-authored benchmark for memory-aware LLM agents in Minecraft. 44 tasks / 216 subtasks elicited from expert co-play. Bounded-knowledge policy. Machine-checkable validators. 33% subtask failure rate for GPT-4o with common recoveries catalogued.
- **Link**: [arXiv:2601.05215](https://arxiv.org/abs/2601.05215)

---

## 6. Industry Game AI

### KRAFTON AI PUBG Teammate 'Ally' — Development Story

- **Affiliation**: KRAFTON
- **Venue**: Media coverage (Inven Global), 2026-06
- **Abstract**: A.X K1 500B-parameter model powers PUBG AI teammate 'Ally.' Trained on 40,000 matches at internet cafes with 1000+ players. Real-time voice dialogue + action control with System 1/System 2 architecture. On-device inference via proprietary compression (fine-tuning, distillation, KV cache optimization). Single GPU for 3D rendering + AI agent.
- **Link**: [Inven Global](https://www.invenglobal.com/lol/articles/22987/ai-pubg-teammate-raised-through-tens-of-thousands-of-matches-at-internet-cafes-krafton-reveals-development-story)

---

### Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory

- **Authors**: (Multiple)
- **Affiliation**: Industry / Academia
- **Venue**: arXiv 2026
- **Abstract**: Memory-augmented interactive world model for 720p real-time long-form video generation at up to 40 FPS (5B model). Infinite data engine (UE synthetic + AAA game + real-world). Multi-segment autoregressive DMD distillation + model quantization + VAE pruning. Minute-long memory consistency.
- **Link**: [arXiv:2604.08995](https://arxiv.org/abs/2604.08995)

---

### Matrix-Game 2.0: An Open-Source Real-Time and Streaming Interactive World Model

- **Authors**: (Multiple)
- **Affiliation**: Industry / Academia
- **Venue**: arXiv 2025
- **Abstract**: Interactive world model generating long videos on-the-fly via few-step autoregressive diffusion. 25 FPS on H100. 1200-hour UE/GTA5 dataset with mouse/keyboard annotations. Self-Forcing-based distillation for causal architecture. Open-source model weights and codebase.
- **Link**: [arXiv:2508.13009](https://arxiv.org/abs/2508.13009)

---

### Matrix-Game: Interactive World Foundation Model

- **Authors**: (Multiple)
- **Affiliation**: Industry / Academia
- **Venue**: arXiv 2025
- **Abstract**: Diffusion-based image-to-world generation model for Minecraft world modeling. Matrix-Game-MC dataset. GameWorld Score benchmark for visual/temporal/controllability/physical consistency evaluation.
- **Link**: [arXiv:2506.18701](https://arxiv.org/abs/2506.18701)

---

## 7. Related Techniques

### Self-Play & Population-Based Training

#### PopuLoRA: Co-Evolving LLM Populations for Reasoning Self-Play

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Population-based asymmetric self-play with LoRA adapters (frozen base). Teacher proposes problems, matched students solve. LoRA weight-space evolution operators (mutations/crossovers) as PBT replacement. Population outperforms single-agent on 3 code + 7 math benchmarks. Avoids mode-collapse.
- **Link**: [arXiv:2605.16727](https://arxiv.org/abs/2605.16727)

---

#### Stratagem: Learning Transferable Reasoning via Trajectory-Modulated Game Self-Play

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Addresses game-specificity and strategy stasis in self-play reasoning transfer. Reasoning Transferability Coefficient selectively reinforces abstract trajectories. Reasoning Evolution Reward incentivizes adaptive reasoning. Strong gains on competition-level mathematics.
- **Link**: [arXiv:2604.17696](https://arxiv.org/abs/2604.17696)

---

#### Foundation Model Self-Play: Open-Ended Strategy Innovation via Foundation Models

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2025
- **Abstract**: Three FMSP variants: Vanilla (vFMSP), Novelty-Search (NSSP), Quality-Diversity (QDSP). Evaluated in Car Tag and Gandalf (jailbreak simulation). QDSP discovers diverse high-quality policies combining RL, tree search, heuristics. Automatically red-teams and patches LLM vulnerabilities.
- **Link**: [arXiv:2507.06466](https://arxiv.org/abs/2507.06466)

---

#### SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Co-evolves Challenger (generates tasks) and Solver (multi-turn retrieval). Frozen self-judge writes rubrics and scores. Up to +10.4 points on 8 open-ended benchmarks across Qwen2.5, Qwen3, OLMo-3. Also improves held-out short-form QA (+13.8). Co-evolution is necessary to keep tasks on frontier.
- **Link**: [arXiv:2605.31433](https://arxiv.org/abs/2605.31433)

---

#### MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2025
- **Abstract**: End-to-end RL framework for multi-agent reasoning via self-play. Turn-level advantage estimator + agent-specific advantage normalization. Qwen3-4B shows up to 28.7% improvement in held-out games. Transfers to reasoning: up to +10.0% on AIME, +7.6% on GPQA-Diamond.
- **Link**: [arXiv:2510.15414](https://arxiv.org/abs/2510.15414)

---

#### OMAR: One Model, All Roles — Multi-Turn, Multi-Agent Self-Play for Conversational Social Intelligence

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Single model role-playing all participants in multi-agent conversations. End-of-episode rewards in SOTOPIA environments. Social behaviors (empathy, persuasion, compromise) emerge from self-play. Competitive scenarios (Werewolf) also incent collaborative behaviors.
- **Link**: [arXiv:2602.03109](https://arxiv.org/abs/2602.03109)

---

#### COvolve: Adversarial Co-Evolution of LLM-Generated Policies and Environments via Two-Player Zero-Sum Game

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: LLMs generate both environments and policies as Python code. Two-player zero-sum game formulation. Mixed-strategy Nash equilibrium meta-policy prevents forgetting. Experiments in urban driving, symbolic maze, geometric navigation. Open-ended learning without predefined task distributions.
- **Link**: [arXiv:2603.28386](https://arxiv.org/abs/2603.28386)

---

#### G-Zero: Self-Play for Open-Ended Generation from Zero Data

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Verifier-free co-evolutionary framework. Hint-δ intrinsic reward measures predictive shift with/without self-generated hint. Proposer trained via GRPO to target Generator blind spots. Generator optimized via DPO. Proves best-iterate suboptimality guarantee. Bypasses external judge capability ceilings.
- **Link**: [arXiv:2605.09959](https://arxiv.org/abs/2605.09959)

---

#### CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Autonomous multi-agent evolution with shared persistent memory, asynchronous execution, heartbeat-based interventions. SOTA on 8 of 11 mathematical/systems optimization tasks. 2.5× improvement rate with 10× fewer evaluations. 4 co-evolving agents improved kernel engineering from 1363 to 1103 cycles.
- **Link**: [arXiv:2604.01658](https://arxiv.org/abs/2604.01658)

---

#### Discovering Multiagent Learning Algorithms with Large Language Models (AlphaEvolve)

- **Authors**: (Multiple)
- **Affiliation**: DeepMind / Academia
- **Venue**: arXiv 2026
- **Abstract**: Uses LLM-driven evolutionary search to automate design of multi-agent RL algorithms (CFR and PSRO). Discovers VAD-CFR and SHOR-PSRO. Distills to minimal solvers (WOP-CFR, PM-PSRO). Human-in-the-loop pipeline with train-test ablation. Evaluated across 18-game suite (OpenSpiel).
- **Link**: [arXiv:2602.16928](https://arxiv.org/abs/2602.16928)

---

#### π-Play (Privileged Information Self-Play)

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Multi-agent self-evolution framework. Examiner generates tasks with question construction paths (QCP). Teacher uses QCP as privileged context for dense student supervision via self-distillation. Data-free, surpasses fully supervised search agents. 2–3× efficiency over conventional self-play.
- **Link**: [arXiv:2604.14054](https://arxiv.org/abs/2604.14054)

---

### World Models & Model-Based RL

#### Reinforcement World Model Learning (RWML) for LLM-based Agents

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Self-supervised RL-based world model learning. Trains LLMs to minimize discrepancy between simulated and realized next states in pretrained embedding space. 19.6 / 6.9 point improvements on ALFWorld and τ² Bench without expert data. Outperforms direct task-success RL when combined.
- **Link**: [arXiv:2602.05842](https://arxiv.org/abs/2602.05842)

---

#### WorldCompass: Reinforcement Learning for Long-Horizon World Models

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: RL framework for world model post-training. Clip-level rollout for autoregressive video generation. Complementary rewards for action following + visual quality. Negative-aware fine-tuning. Significantly enhances WorldPlay on compositional action sequences.
- **Link**: [arXiv:2602.09022](https://arxiv.org/abs/2602.09022)

---

#### Dual-Scale World Models (GLoW) for LLM Agents towards Hard-Exploration Problems

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2025
- **Abstract**: Global-Local World Models for hard-exploration. Trajectory frontier at global scale + Multi-path Advantage Reflection for local exploration. SOTA for LLM-based agents on Jericho (text-based games). Comparable to RL methods with 100–800× fewer interactions.
- **Link**: [arXiv:2509.24116](https://arxiv.org/abs/2509.24116)

---

#### PriorZero: Bridging Language Priors and World Models for Decision Making

- **Authors**: (Multiple, OpenDILab)
- **Affiliation**: Academia / OpenDILab
- **Venue**: arXiv 2026
- **Abstract**: Integrates LLM priors into world-model-based planning via MCTS. Root-prior injection for search focus while preserving deep lookahead. Decoupled world model learning from LLM adaptation via alternating optimization. Improves exploration efficiency on Jericho and BabyAI.
- **Link**: [arXiv:2605.12289](https://arxiv.org/abs/2605.12289)

---

#### Hierarchical Planning with Latent World Models (HWM)

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Hierarchical MPC on visual world models via next-latent prediction. Multiple temporal scales in shared latent space. Latent matching serves as subgoals without task-specific rewards. 70% vs 0% success on real-world Franka pick-&-place. Up to 3× less planning compute.
- **Link**: [arXiv:2604.03208](https://arxiv.org/abs/2604.03208)

---

#### AgentOWL: Joint Learning of Hierarchical Neural Options and Abstract World Model

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Jointly learns abstract world model + hierarchical neural options. Symbolic code + non-parametric distributions for sample efficiency. On OCAtari games (Montezuma's Revenge, Pitfall, Private Eye): acquires most skills, demonstrates zero-shot generalization to novel situations.
- **Link**: [arXiv:2602.02799](https://arxiv.org/abs/2602.02799)

---

#### ProPlay: Procedural World Models for Self-Evolving LLM Agents

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Procedure graph world model where nodes are procedures and edges are procedural transitions. Reliability records for each transition. Preplay constructs task-specific procedural trajectories as soft guidance. Refines graph via environment feedback.
- **Link**: [arXiv:2606.12780](https://arxiv.org/abs/2606.12780)

---

#### Internalizing World Models via Self-Play Finetuning for Agentic RL (SPA)

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2025
- **Abstract**: Self-play fine-tuning for world model internalization before policy learning. Decomposes world modeling into state representation + transition dynamics. Supervised finetuning on transitions. Exploration before exploitation yields robust scaffold raising Pass@k. No external knowledge or teacher models needed.
- **Link**: [arXiv:2510.15047](https://arxiv.org/abs/2510.15047)

---

#### ActWorld: From Explorable to Interactive World Model via Action-Aware Memory

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Extends navigation-centric world models to object interaction. 100K interaction video dataset with per-chunk COT captions. Hierarchical action-aware memory with persistent memory bank for event-update tokens. Supports navigation + rich object interaction without sacrificing viewpoint control.
- **Link**: [arXiv:2606.17730](https://arxiv.org/abs/2606.17730)

---

#### Curious Causality-Seeking Agents in Open-ended Worlds

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2025
- **Abstract**: Meta-Causal Graph as world model for open-ended environments. Causality-Seeking Agent with curiosity-driven intervention policy to discover meta states and causal subgraphs. Experiments on synthetic tasks and robot arm manipulation. Captures shifts in causal dynamics and generalizes to unseen contexts.
- **Link**: [arXiv:2506.23068](https://arxiv.org/abs/2506.23068)

---

### Minecraft Agents

#### Optimus-3: Towards Generalist Multimodal Minecraft Agents with Scalable Task Experts

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2025
- **Abstract**: Knowledge-enhanced data generation pipeline + MoE architecture with task-level routing + Multimodal Reasoning-Augmented RL (IoU-Density Reward with GRPO). Surpasses both generalist MLLMs and existing SOTA agents across wide range of Minecraft tasks. 42% gain on Embodied QA, 36% on Grounding.
- **Link**: [arXiv:2506.10357](https://arxiv.org/abs/2506.10357)

---

#### Echo: Experience Transfer for Multimodal LLM Agents in Minecraft

- **Authors**: C. Li et al.
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Transfer-oriented memory framework with 5 knowledge dimensions (structure, attribute, process, function, interaction). In-Context Analogy Learning (ICAL) retrieves and adapts experiences. 1.3–1.7× speed-up on object-unlocking tasks. Emergent burst-like chain-unlocking phenomenon.
- **Link**: [arXiv:2604.05533](https://arxiv.org/abs/2604.05533)

---

#### MineEvolve: Self-Evolution with Accumulated Knowledge for Long-Horizon Embodied Minecraft Agents

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Knowledge-driven self-evolution converting execution feedback into reusable skills (success) and remedies (failure). Inducer, curator, and executor modules. Consistently outperforms baselines on MCU benchmark. Transforms trajectory feedback into planning-level knowledge.
- **Link**: [arXiv:2603.13131](https://arxiv.org/abs/2603.13131)

---

#### WISE: A Long-Horizon Agent in Minecraft with Why-Which Reasoning

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Causal Event Graph augmenting episodic memory with causal structure. Opportunistic Task Scheduler for dynamic subtask re-prioritization. Multi-scale progressive exploration strategy. Improves long-horizon sparse task success, especially under viewpoint changes.
- **Link**: [arXiv:2606.12852](https://arxiv.org/abs/2606.12852)

---

#### PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft

- **Authors**: Y. Guo, J. Gong, W. Wang, H. Cai, Y. Cheung, W. Su
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Parametric memory framework transforming agent memory into parameter-resident skills. Multimodal MoE LoRA with per-category isolated adapters. Failure-correction trajectory pairs internalized via BC + contrastive objective. Parameterization worthiness score + self-triggered consolidation. Mitigates catastrophic forgetting.
- **Link**: [arXiv:2605.27762](https://arxiv.org/abs/2605.27762)

---

### Game AI for Other Domains

#### GEM (General Experience Maker): A Gym for Agentic LLMs

- **Authors**: (Multiple, Axon)
- **Affiliation**: Industry / Academia
- **Venue**: arXiv 2025
- **Abstract**: OpenAI-Gym equivalent for LLM agents. Suite of environments (tool use, reasoning games, multi-turn text games, terminal, math, code). Asynchronous vectorized execution. Validated baselines + training scripts for 5 RL frameworks (Oat, Verl, OpenRLHF, ROLL, RL2).
- **Link**: [arXiv:2510.01051](https://arxiv.org/abs/2510.01051)

---

#### No-Regret Strategy Solving in Imperfect-Information Games via Pre-Trained Embedding (Embedding CFR)

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2025
- **Abstract**: Pre-trains information set embeddings in low-dimensional continuous space. Embedding CFR drives regret accumulation and strategy updates in embedding space. Faster exploitability convergence than cluster-based abstraction algorithms on poker.
- **Link**: [arXiv:2511.12083](https://arxiv.org/abs/2511.12083)

---

#### How Far Are LLMs from Professional Poker Players? (ToolPoker, BC-RIRL)

- **Authors**: (Multiple)
- **Affiliation**: Academia
- **Venue**: arXiv 2026
- **Abstract**: Two-stage BC + regret-inspired RL (RIRL). Step-level regret-guided reward from CFR solver. Improves strategic reasoning in Kuhn/Leduc/Texas Hold'em. Reduces heuristic flaws and knowing-doing gap. Factual misunderstandings remain main limitation.
- **Link**: [arXiv:2602.00528](https://arxiv.org/abs/2602.00528)

---

### Benchmarks Infrastructure

#### OpenGame-Bench (part of OpenGame)

- **Venue**: arXiv 2026
- **Abstract**: Evaluation pipeline for agentic game generation scoring Build Health, Visual Usability, Intent Alignment via headless browser execution + VLM judging. 150 diverse game prompts.
- **Link**: [arXiv:2604.18394](https://arxiv.org/abs/2604.18394)

---

## Paper Count Summary

| Category | Papers |
|----------|--------|
| Game RL | 12 |
| Game AI Bot | 8 |
| Game Foundation Models | 7 |
| Procedural Content Generation | 5 |
| Game Benchmarks | 9 |
| Industry Game AI | 4 |
| Self-Play & Population-Based Training | 12 |
| World Models & Model-Based RL | 11 |
| Minecraft Agents | 5 |
| Other Related | 4 |
| **Total** | **~77** |
