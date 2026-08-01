---
title: "Game RL & Game AI Bot — Daily Synthesis (2026-08-01)"
type: synthesis
created: 2026-08-01
updated: 2026-08-01
tags: [game-rl, game-ai, game-foundation-models, pcg, game-benchmarks, self-play, world-models, multi-agent-rl, llm-agents]
sources: []
---

# Game RL & Game AI Bot — Daily Synthesis (2026-08-01)

> Curated papers on Game RL, Game AI Bots, Game Foundation Models, PCG, Benchmarks, Industry Game AI, and related techniques. Searched arXiv and recent proceedings.

---

## 1. Game RL — Reinforcement Learning in Games

### Belief-Guided Decision Making with Uncertainty Gating in the Game of Go
- **Authors**: Mehrad Yaghoubi, Azam Bastanfard, Abbas Jalilvand, Ashkan Rezaei
- **Affiliation**: —
- **Venue**: arXiv:2607.26946 (Jul 2026)
- **Key Innovation**: Injecting uncertainty (belief) estimates into Go agents via uncertainty gating — decision-making is conditioned on the model's belief about board state, improving play quality beyond pure position-based policies.
- **Link**: https://arxiv.org/abs/2607.26946

### DAGS: Data-Augmented Game Starts for Accelerating Self-Play Exploration in Imperfect-Information Games
- **Authors**: JB Lanier, Nathan Monette, Pierre Baldi, Roy Fox
- **Affiliation**: —
- **Venue**: arXiv:2605.14379 (May 2026)
- **Key Innovation**: Augments self-play rollouts with randomized mid-game starts (data-augmented game starts) to accelerate exploration and improve learning speed in imperfect-information games, without modifying the underlying SP algorithm.
- **Link**: https://arxiv.org/abs/2605.14379

### EMAgnet: Parameter-Space EMA Regularization for Policy Gradient Self-Play in Large Games
- **Authors**: Tristan Maidment, JB Lanier, Chase McDonald, Nathan Tsang, Eugene Vinitsky, Roy Fox, Albert Wang, Wesley N. Kerr
- **Affiliation**: —
- **Venue**: ICML 2026 NExT-Game Workshop / arXiv:2606.23995 (Jun 2026)
- **Key Innovation**: Regularizes policy-gradient self-play with parameter-space exponential moving averages (EMA), stabilizing training and improving equilibrium-finding performance in large games versus standard last-iterate methods.
- **Link**: https://arxiv.org/abs/2606.23995

### GARIP: A Running-Average Moving Reference for Last-Iterate Self-Play
- **Authors**: Can Savcı
- **Affiliation**: —
- **Venue**: arXiv:2606.22688 (Jun 2026)
- **Key Innovation**: Uses a running-average of past policies as the self-play reference. Analysis shows the running-average anchor uniquely minimizes peak lag against the best response, unlike snapshot-based references — a practical fix for self-play instability.
- **Link**: https://arxiv.org/abs/2606.22688

### From Imitation to Interaction: Mastering the Game of Schnapsen with Shallow RL
- **Authors**: Ján Klačan, Sizhong Zhang
- **Affiliation**: —
- **Venue**: arXiv:2605.17162 (May 2026)
- **Key Innovation**: Shallow (small-footprint) RL agent for the imperfect-information trick-taking game Schnapsen. Naive imitation learning fails against RdeepBot, but RL with deeper lookahead at decision time reaches strong play, showing RL beats behavior cloning when experts are unavailable/limited.
- **Link**: https://arxiv.org/abs/2605.17162

### A Gold-Standard Study of What Makes a Lightweight Game-Playing Agent Strong
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2607.06854 (Jul 2026)
- **Key Innovation**: Controlled study on Gin Rummy isolating which ingredients (search depth, information-set abstraction, opponent modeling) drive strength in a lightweight game agent, providing a rigorous baseline for deep-learning approaches.
- **Link**: https://arxiv.org/abs/2607.06854

### Deep Reinforcement Learning to Master the Asymmetric Strategy of Baghchal
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2607.18296 (Jul 2026)
- **Key Innovation**: DRL agent for Baghchal (a classic asymmetrical pursuit game from Nepal, tiger-vs-goats) learning both roles from self-play despite inherent asymmetry between sides.
- **Link**: https://arxiv.org/abs/2607.18296

### PLATO: Pointer Learner for Agent and Task Openness
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2607.25082 (Jul 2026)
- **Key Innovation**: Pointer-based policy learner designed for open-ended agent/task configurations, targeting generalization to new agent morphologies and task structures.
- **Link**: https://arxiv.org/abs/2607.25082

---

## 2. Game AI Bot — LLM-Powered Game Agents & NPC Intelligence

### Augmentations for Robust and Efficient Imitation Learning in Streamed Video Games
- **Authors**: Somjit Nath, Abdelhak Lemkhenter, Pallavi Choudhury, Chris Lovett, Katja Hofmann, Sergio Valcarcel Macua, Lukas Schäfer
- **Affiliation**: Microsoft
- **Venue**: arXiv:2607.14200 (Jul 2026)
- **Key Innovation**: Data-augmentation suite (visual and semantic) for imitation learning on streamed/temporal video-game data, improving robustness of game agents trained from videos and reducing the amount of demonstration data required.
- **Link**: https://arxiv.org/abs/2607.14200

### CaM-Wolf: Causal-Aware Multimodal Agents for Social Deduction Games
- **Authors**: Zheng Zhang, Nanjie Yao, Jiarui He, Deheng Ye
- **Affiliation**: —
- **Venue**: arXiv:2607.26393 (Jul 2026)
- **Key Innovation**: Multimodal LLM agents for Werewolf-style social deduction games with causal-aware reasoning (inference-time causal analysis of accusations, role claims, and votes) to improve deception detection and truthful play.
- **Link**: https://arxiv.org/abs/2607.26393

### TickingCollabBench: A Multi-Agent Framework for Time-Sensitive Complementary Collaboration in Minecraft
- **Authors**: Juheon Yi, Jinglu Wang, Xiaoyi Zhang, Yan Lu
- **Affiliation**: —
- **Venue**: arXiv:2606.15684 (Jun 2026)
- **Key Innovation**: New Minecraft benchmark (TickingCollab) where agents must perform time-critical, complementary (interdependent) collaborative tasks, evaluating scheduling, hand-off, and synchronization in multi-agent LLM systems.
- **Link**: https://arxiv.org/abs/2606.15684

### Spatial Reasoning in LLM Game Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2607.22732 (Jul 2026)
- **Key Innovation**: Analysis and interventions targeting spatial reasoning failures of LLM game agents, a known weak point identified by benchmarks like GVGAI-LLM.
- **Link**: https://arxiv.org/abs/2607.22732

### Cortex: Compact Behavior Cloning for Quake with Frozen Visual Features
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2607.22739 (Jul 2026)
- **Key Innovation**: Behavior-cloning agent for Quake-style fast-paced FPS using frozen visual feature extractors with a compact policy head — a low-compute recipe for high-frequency reactive game agents.
- **Link**: https://arxiv.org/abs/2607.22739

### Auditing Belief-Conditioned LLM Agents in Hidden-Information Social Deduction Games
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2607.10814 (Jul 2026)
- **Key Innovation**: Audit framework for hidden-information social deduction agents: how LLM agents form, update, and leak beliefs about hidden roles, and whether belief-conditioning actually improves their play.
- **Link**: https://arxiv.org/abs/2607.10814

### PEAM: Parametric Embodied Agent Memory Through Contrastive Internalization of Experience in Minecraft
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2605.27762 (May 2026)
- **Key Innovation**: Embodied agent memory as parametric parameters — experiences are internalized into model weights via contrastive learning rather than stored in an external retrieval buffer, improving long-horizon Minecraft task performance.
- **Link**: https://arxiv.org/abs/2605.27762

---

## 3. Game Foundation Models — Generalist Game Agents & World Models

### StatePlay: State-Aware Game World Models for Mechanics-Consistent Generation
- **Authors**: Zijun Lin, Zeqing Wang, Cheston Tan, Bihan Wen, Yeying Jin
- **Affiliation**: NTU Singapore
- **Venue**: arXiv:2607.26754 (Jul 2026)
- **Key Innovation**: State-aware world model for game generation: explicitly tracks game state/mechanics so generated video remains mechanics-consistent (objects obey rules, interactions are physically coherent) rather than merely photorealistic.
- **Link**: https://arxiv.org/abs/2607.26754

### WanToFight: Real-Time Generative Game Engine for Multi-Player Combat Interaction
- **Authors**: Li Hu, Guangyuan Wang, Peng Zhang, Bang Zhang
- **Affiliation**: ByteDance
- **Venue**: arXiv:2607.12592 (Jul 2026)
- **Key Innovation**: Generative video game engine for the fighting game KOF '97 supporting real-time two-player interaction (player inputs steer generated frames at interactive rates), extending the diffusion-game-engine line to multi-player combat.
- **Link**: https://arxiv.org/abs/2607.12592

### When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2607.14169 (Jul 2026)
- **Key Innovation**: Shows that LLM-synthesized code world models can pass verification / achieve high prediction accuracy yet still underperform in policy rollouts — a "play-adequacy" gap, arguing prediction metrics are insufficient for world-model evaluation.
- **Link**: https://arxiv.org/abs/2607.14169

### DreamForge-World 0.1 Preview: Low-Compute Real-Time Controllable World Model
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2606.30292 (Jun 2026)
- **Key Innovation**: Preview of a low-compute real-time world model emphasizing controllability (action-conditional generation) at reduced parameter/flops budgets, targeting consumer-hardware game-world simulation.
- **Link**: https://arxiv.org/abs/2606.30292

### GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2605.20246 (May 2026)
- **Key Innovation**: Reinforces open-world VLM game agents (e.g., Minecraft) by aligning GRPO-style policy optimization with explicit state-action modeling, improving grounding and long-horizon planning.
- **Link**: https://arxiv.org/abs/2605.20246

### Reason to Play: Behavioral and Brain Alignment Between Frontier LRMs and Human Game Learners
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2605.08019 (May 2026)
- **Key Innovation**: Studies frontier reasoning LLMs against human game learners using both behavioral and brain-imaging (fMRI/EEG) alignment — finds reasoning models mirror human strategic learning patterns during gameplay.
- **Link**: https://arxiv.org/abs/2605.08019

---

## 4. Procedural Content Generation (PCG)

### Evolutionary Wave Function Collapse
- **Authors**: Dipika Rajesh, Ahmed Khalifa, Julian Togelius
- **Affiliation**: NYU / —
- **Venue**: IEEE CoG 2026 / arXiv:2607.02082 (Jul 2026)
- **Key Innovation**: Treats WFC pattern selection as a genotype-to-phenotype map and applies evolutionary search over WFC parameters/constraints to optimize generated levels for design objectives. Demonstrated on maze and Zelda-like domains.
- **Link**: https://arxiv.org/abs/2607.02082

### Representing and Generating Levels Over Time Through Playtrace Reconstructive Partitioning
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2607.12097 (Jul 2026)
- **Key Innovation**: Represents levels as playtraces (how players move through them) and reconstructively partitions those traces to generate new levels — a temporal/behavioral angle on level representation for PCG.
- **Link**: https://arxiv.org/abs/2607.12097

### An Exploration of Collision-Based Enemy Morphology Generation
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2606.02832 (Jun 2026)
- **Key Innovation**: PCG of enemy "morphologies" (body shapes/collision profiles) that alter how enemies interact with the player and environment, expanding content variety through physics-driven design.
- **Link**: https://arxiv.org/abs/2606.02832

### 3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2606.01057 (Jun 2026)
- **Key Innovation**: Benchmark for agentic procedural 3D asset modeling: LLM agents must write code (procedural generation) to produce 3D models, with structured evaluation of correctness and aesthetics.
- **Link**: https://arxiv.org/abs/2606.01057

### From LLM-Driven Trading Card Generation to Procedural Relatedness: A Pokémon Case Study
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2604.27972 (Apr 2026)
- **Key Innovation**: Uses LLM-driven trading-card generation to study procedural relatedness — how generated cards relate to canonical ones (typings, stats, flavor) — as a framework for evaluating semantic control in PCG.
- **Link**: https://arxiv.org/abs/2604.27972

---

## 5. Game Benchmarks

### RTSGameBench: A Real-Time Strategy Benchmark for Strategic Reasoning by Vision-Language Models
- **Authors**: San Kim, Daechul Ahn, Reokyoung Kim, Hyeonbeom Choi, Seungyeon Jwa, Jonghyun Choi
- **Affiliation**: —
- **Venue**: arXiv:2606.18950 (Jun 2026)
- **Key Innovation**: RTS benchmark built on the open-source game Beyond All Reason, probing strategic reasoning (unit composition, economy, map control) of VLMs and multimodal agents, with structured task families and evaluation.
- **Link**: https://arxiv.org/abs/2606.18950

### PTCG-Bench: Can LLM Agents Master the Pokémon Trading Card Game?
- **Authors**: Dongdong Hua, Yifei Sun, Renhong Huang, Feng Gao, Chunping Wang, Yang Yang
- **Affiliation**: Alibaba
- **Venue**: arXiv:2605.29653 (May 2026)
- **Key Innovation**: Multi-agent benchmark for the Pokémon Trading Card Game. Finds sustained self-evolution (improving agents that keep improving against selves) is hard — harness design (search, memory, reflection scaffolding) matters more than raw LLM capability for long-term mastery.
- **Link**: https://arxiv.org/abs/2605.29653

### SMAC-Talk: Communicating Agents in StarCraft Multi-Agent Challenge
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2606.04202 (Jun 2026)
- **Key Innovation**: Extends SMAC to communication-constrained StarCraft micromanagement where agents coordinate via structured communication channels, evaluating how emergent communication affects MARL performance.
- **Link**: https://arxiv.org/abs/2606.04202

### GPTNT: Keep Talking And Nobody Explodes — Benchmarking LLM Agents on Multi-Modal Puzzle Collaboration
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2606.28514 (Jun 2026)
- **Key Innovation**: Cooperative benchmark based on the game Keep Talking and Nobody Explodes: an LLM "expert" with the manual must guide an LLM/agent "defuser" through multi-modal (text+image) puzzles, testing instruction-following, grounded communication, and uncertainty resolution.
- **Link**: https://arxiv.org/abs/2606.28514

### Same Game, Different Story: A Benchmark for Strategic Robustness in Board Games
- **Authors**: Seyed Pouyan Mousavi Davoudi et al.
- **Affiliation**: —
- **Venue**: arXiv:2607.19670 (Jul 2026)
- **Key Innovation**: Benchmark measuring whether agents preserve strategic competence under rule/variant perturbations of the same game (Same Game, Different Story), exposing brittle strategy adaptation in current agents.
- **Link**: https://arxiv.org/abs/2607.19670

### Evaluating VLMs for Autonomous Agent-Driven Geometry Clipping Detection in Video Game QA
- **Authors**: Carlos Celemin, Benedict Wilkins, Adrián Barahona-Ríos, Saman Zadtootaghaj, Nabajeet Barman
- **Affiliation**: —
- **Venue**: arXiv:2607.25921 (Jul 2026)
- **Key Innovation**: Uses VLMs to autonomously detect geometry clipping bugs (objects intersecting/penetrating) in game QA — an automation target for the games-industry QA pipeline.
- **Link**: https://arxiv.org/abs/2607.25921

---

## 6. Industry Game AI

### RAID: Reward-Adaptive Iterative Discovery for EA SPORTS NHL 26
- **Authors**: —
- **Affiliation**: EA
- **Venue**: arXiv:2607.07498 (Jul 2026)
- **Key Innovation**: Production reward-adaptive iterative RL pipeline used in EA SPORTS NHL 26 — iterative policy discovery with adaptive reward shaping to improve hockey AI behaviors in a shipped AAA title.
- **Link**: https://arxiv.org/abs/2607.07498

### AI Native Games: A Survey and Roadmap
- **Authors**: Zhiyue Xu, Fandi Meng, Kaijie Xu, Clark Verbrugge, Simon Lucas, Jian Zhao
- **Affiliation**: McGill / QMUL / Waterloo
- **Venue**: arXiv:2607.00527 (Jul 2026)
- **Key Innovation**: Proposes a counterfactual definition of "AI-native games" (games that could not exist without AI) and surveys the landscape of game + AI integration with a roadmap for research and industry.
- **Link**: https://arxiv.org/abs/2607.00527

### Multi-Task Learning for Heterogeneous Prediction from Video Game State
- **Authors**: —
- **Affiliation**: TU Graz
- **Venue**: arXiv:2607.21290 (Jul 2026)
- **Key Innovation**: Multi-task learning architecture predicting heterogeneous game-state quantities (positions, health, scores, match outcome) from gameplay observations — building blocks for analytics and adaptive game systems.
- **Link**: https://arxiv.org/abs/2607.21290

### SPEAR: Simulator for Photorealistic Embodied AI Research
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2607.06701 (Jul 2026)
- **Key Innovation**: Photorealistic game-engine simulator purpose-built for embodied AI research, balancing real-time interaction, rendering fidelity, and rich action/observation interfaces.
- **Link**: https://arxiv.org/abs/2607.06701

---

## 7. Related Techniques — Self-Play, World Models, Multi-Agent RL

### Open-Ended Multi-Agent Autocurricula via Visual Inspection of Policies with MLLMs
- **Authors**: —
- **Affiliation**: Sony AI
- **Venue**: arXiv:2607.08193 (Jul 2026)
- **Key Innovation**: Uses multimodal LLMs to visually inspect agent policies and automatically propose new training environments/counter-agents — an open-ended autocurriculum loop that closes the gap between open-ended evolution and RL.
- **Link**: https://arxiv.org/abs/2607.08193

### Can Agents Deceive? Evaluating Reasoning and Deception in ParliamentBench
- **Authors**: Niklas Bauer, Lars Benedikt Kaesberg, Akiko Aizawa, Jan Philip Wahle
- **Affiliation**: —
- **Venue**: arXiv:2607.28146 (Jul 2026)
- **Key Innovation**: Social-deduction benchmark probing whether LLM agents can reason about and deploy deception in a parliamentary (Werewolf-style) game, separating reasoning ability from deceptive behavior.
- **Link**: https://arxiv.org/abs/2607.28146

### Asymmetric Communication: LLMs and Language Games
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2607.28137 (Jul 2026)
- **Key Innovation**: Studies asymmetric communication setups in LLM language games — e.g., one agent sees more, or communicates in a constrained channel — and how it shifts emergent coordination and strategy.
- **Link**: https://arxiv.org/abs/2607.28137

### Strategy, Not Payoffs: A Behavioural Embedding of Normal-Form Games
- **Authors**: —
- **Affiliation**: —
- **Venue**: arXiv:2607.27536 (Jul 2026)
- **Key Innovation**: Builds a behavioural embedding of normal-form games based on strategy structure rather than payoff matrices — a representation theory for grouping "strategically similar" games, useful for game classification and agent evaluation.
- **Link**: https://arxiv.org/abs/2607.27536

---

## Summary Statistics

- **Total papers**: ~38
- **Categories covered**: 7
- **Key venues**: IEEE CoG 2026, ICML 2026 NExT-Game Workshop, arXiv (Jul 2026 batch)
- **Notable trends**:
  - World models moving from prediction to *interaction*: mechanics-consistent generation (StatePlay), real-time multi-player generative engines (WanToFight), and play-adequacy vs prediction-accuracy critiques
  - Self-play stabilization as a first-class problem (EMAgnet, GARIP running-average references, DAGS game-start augmentation)
  - Social deduction / hidden-information games as the new LLM-agent stress test (CaM-Wolf, ParliamentBench, belief-conditioned auditing)
  - RTS and card-game strategic benchmarks for VLMs/LLMs (RTSGameBench, PTCG-Bench) with sobering findings on self-evolution
  - Industry QA automation with VLMs (geometry clipping detection) and shipped production RL (EA SPORTS NHL 26)
  - Behavioral/structural representations of games and policies (behavioural game embedding, playtrace-based PCG, visual-inspection autocurricula)
