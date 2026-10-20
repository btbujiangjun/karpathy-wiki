---
title: "Game RL & Game AI Bot — Daily Survey (2026-10-20)"
type: synthesis
created: 2026-10-20
updated: 2026-10-20
tags: [game-rl, game-ai, foundation-models, pcg, benchmarks, industry, world-models, self-play, marl, nethack, starcraft, npc, llm-agents, credit-assignment, mapf, survey]
sources: [arxiv.org, neurips.cc]
---

# Game RL & Game AI Bot — Daily Survey (2026-10-20)

Covers 7 categories: Game RL, Game AI Bot, Game Foundation Models, Procedural Content Generation, Game Benchmarks, Industry Game AI, and Related Techniques (world models, credit assignment, self-play, lifelong MAPF).

> **Run note.** Tuesday survey-style pass (curated re-curation + fresh sweep) complementing the same-day siblings [`arxiv-daily`](../2026-10-20/arxiv-daily.md), [`arxiv-ai-search`](../2026-10-20/arxiv-ai-search.md) and [`arxiv-paper-check`](../2026-10-20/arxiv-paper-check.md), and the exhaustive Monday digest [`game-rl-daily` 2026-10-19](../2026-10-19/game-rl-daily.md). The arXiv export API was unavailable (HTTP 429 / empty responses), so metadata came from `/abs/{id}` pages fetched with a browser UA. **30 papers featured: 4 new-to-wiki** (`2604.22748`, `2602.00785`, `2610.14636`, `2610.18186`) **+ 1 proceedings-only item** (NetHack Checkpointed Exploration, NeurIPS 2026, no arXiv ID found) **+ 25 on-file cross-references** (re-curated for the survey, not re-claimed as new; IDs verified against the `wiki/` tree). Affiliations stated only where declared on the abs page — never inferred.

---

## 1. Game RL — Reinforcement Learning in Games

### GameSmith: Scaling Zero-Sum Self-Play with Synthesised Games
- **Authors**: Weixian Waylon Li, Jiaxin Zhang, Han Zhou, Chengzu Li, Ke Wang, Fengxiang He, Yiwen Guo
- **Affiliation**: —
- **Venue**: arXiv preprint, Sep 2026 (on file since 2026-10-15)
- **Link**: https://arxiv.org/abs/2610.13995
- **Abstract**: Scales both the *supply of games* and the *advantage estimate* for zero-sum self-play RL post-training of LLMs. An LLM synthesises games inside templates whose reward, observation, and hidden-information code is fixed; each game is verified by seed-paired replay and an independent re-implementation of its spec, then expanded into encoding/rule/size variants — **26 new games in 29 families, 336 verified variants from three SPIRAL templates**. Student distilled from Qwen3-32B teacher self-play, then trained by self-play RL.
- **Key innovations**: Program synthesis of verifiable zero-sum games at scale; dual verification (replay + re-implementation); closes both bottlenecks SPIRAL identified (hand-written games, per-game advantage estimators).

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques
- **Affiliation**: —
- **Venue**: arXiv Jun 2025; ICLR 2026 (on file since 2026-06-13)
- **Link**: https://arxiv.org/abs/2506.24119
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games against continuously improving versions of themselves — an automatic curriculum with no human supervision. Implements a fully online multi-turn multi-agent RL system and proposes **role-conditioned advantage estimation (RAE)** to stabilize training. Transfers broadly: up to **+10% across 8 reasoning benchmarks** on 4 model families.
- **Key innovations**: Fully online multi-turn multi-agent RL for LLMs; RAE for stable alternating-role training; complementary cognitive patterns from different games transfer to general reasoning. Parent line of GameSmith (above) and SPADE (§7).

### Self-Play RL under Imperfect Information in Big 2
- **Authors**: Aalok Patwa
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Link**: https://arxiv.org/abs/2605.28863
- **Abstract**: Controlled study of self-play RL in Big 2, a four-player imperfect-information card game (hidden information, sparse rewards, non-stationary opponents). Under a common environment/representation/budget/protocol, **PPO outperforms Monte Carlo Q approximation, SARSA and Q-learning** against random/greedy/heuristic opponents. Moderate entropy regularization helps PPO avoid overly deterministic policies; **current-policy self-play is a stronger finite-budget curriculum** than checkpoint self-play or fixed-opponent training.
- **Key innovations**: Fair algorithm comparison in a hard multiplayer imperfect-info game; practical curriculum finding (on-policy self-play > checkpoint self-play at finite budgets).

### Reproducing AlphaZero on Tablut: Self-Play RL for an Asymmetric Board Game
- **Authors**: Tõnis Lees, Tambet Matiisen
- **Affiliation**: University of Tartu
- **Venue**: arXiv preprint, Apr 2026
- **Link**: https://arxiv.org/abs/2604.05476
- **Abstract**: Adapts AlphaZero to Tablut, an asymmetric historical board game (unequal piece counts; king capture vs king escape). A single policy/value head forces the network to learn two conflicting evaluation functions, so the architecture is modified to **separate per-role policy and value heads on a shared residual trunk**. Training surfaces catastrophic forgetting between attacker and defender roles, mitigated with C4-style data augmentation.
- **Key innovations**: Role-split heads for asymmetric games; diagnosis + fix for inter-role catastrophic forgetting in asymmetric self-play.

### Hierarchical RL in StarCraft Micromanagement with Influence Maps and Cluster-based Scripts (HRL-IM/CBS)
- **Authors**: Chunhui Bai, Changhe Li, Dequan Li, Xinye Cai, Shengxiang Yang
- **Affiliation**: —
- **Venue**: arXiv preprint, Jun 2026
- **Link**: https://arxiv.org/abs/2606.30092
- **Abstract**: Targets RTS micromanagement challenges — joint-action dimensionality explosion, sparse delayed win/lose rewards, and opaque deep policies. Proposes a hierarchical RL framework combining **influence maps** (spatial state abstraction) with **cluster-based scripts** (interpretable tactical modules) that adaptively decompose multi-unit coordination.
- **Key innovations**: Influence-map spatial abstraction + cluster-based hierarchical options; addresses interpretability/sample-efficiency trade-off in StarCraft combat.

### JEV-Star: Fast, Low-Cost StarCraft II Control with Language-Model Planning
- **Authors**: Weiyu Ma, Liangbing Zhao, Yongcheng Zeng, Jian Zhao
- **Affiliation**: —
- **Venue**: arXiv preprint, Sep 2026
- **Link**: https://arxiv.org/abs/2609.27331
- **Abstract**: Defeats the strongest non-cheating built-in SC2 AI (Lv7) by combining fast **JEV** action selection with persistent **GPT-6** planning. Wins four full games at Lv5–Lv7 (two Lv7 victories with different seeds) at a median JEV response time of **0.422 s** and mean estimated cost **≈ USD 3.71/game** (JEV 0.15 + GPT-6 3.56). On 35 battle maps the combined system raises mean enemy elimination from 16.50% to 37.69% and wins from 3 to 7 of 105.
- **Key innovations**: LLM as persistent macro-planner over a fast low-level controller; full-game defeats of Lv7 with per-game cost accounting; replay/decision-log documentation of resource reservation and eco-management.

### Learning to Play: Reinforcement Learning and Games
- **Authors**: Aske Plaat
- **Affiliation**: —
- **Venue**: arXiv preprint (textbook manuscript), Oct 2026
- **Link**: https://arxiv.org/abs/2610.17391
- **Abstract**: A book treatment of RL-in-games, from the breakthroughs in Backgammon, Checkers, Chess, Atari, Go, Poker and StarCraft to the breadth of underlying techniques — exact planning, adaptive sampling, deep function approximation and self-play — positioned as a mainstream route toward general AI.
- **Key innovations**: Unified pedagogical account of the game-RL lineage (on file in earlier dailies; listed here for completeness of the survey's §1).

## 2. Game AI Bot — NPCs, LLM Characters, Game Agents

### LLM-Guided Reinforcement Learning for Adaptive NPC Behavior in Multi-Agent Combat Games
- **Authors**: Hrithika Deepu Nair, Kayvan Karim
- **Affiliation**: —
- **Venue**: arXiv preprint, Aug 2026 (cs.MA)
- **Link**: https://arxiv.org/abs/2609.02931
- **Abstract**: Addresses predictable scripted NPCs and frozen post-training RL policies. Trains five NPC agents with a shared PPO policy in Unity, then at runtime a locally hosted **Mistral 7B** (via Ollama) reads the live game state every five seconds and assigns one of four tactical tags — guiding the trained policy without modifying its underlying behavior. Evaluated against three scripted opponent types across 600 episodes.
- **Key innovations**: Runtime LLM-as-strategy-selector over a frozen RL policy; cheap local model (7B, Ollama) for live adaptation; separation of "which tactic" (LLM) from "how to act" (PPO).

### Bounded Autonomy: Controlling LLM Characters in Live Multiplayer Games
- **Authors**: Yunjia Guo, Jinghan Zhu, Siyu Wang, Haixin Qiao
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026 (v2 Jul 2026; cs.HC); deployed in a live commercial game
- **Link**: https://arxiv.org/abs/2604.04703
- **Abstract**: Frames the control problem for LLM characters in live multiplayer games — executable in the shared game world, socially coherent with other characters, steerable by players — as **bounded autonomy**, a three-interface architecture: agent–agent interaction, agent–world action execution, and player–agent steering. Instantiates **probabilistic reply-chain decay**, an embedding-based action grounding pipeline with fallback, and **whisper**, a lightweight soft-steering technique letting players influence the next move without fully overriding autonomy.
- **Key innovations**: Production-oriented control architecture for live LLM NPCs; soft player steering (whisper) between free generation and hard override; live commercial-game deployment.

### One Policy, Infinite NPCs: Persona-Traceable Shared RL Policies for Scalable Game Agents (pcsp)
- **Authors**: Yoosung Hong
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Link**: https://arxiv.org/abs/2605.23652
- **Abstract**: Life-simulation games need hundreds-to-thousands of NPCs that are persona-consistent, controllable from free-form designer text, and real-time. **pcsp** is a single RL policy conditioned on frozen LLM embeddings of persona descriptions, trained with PPO + InfoNCE consistency + KL diversity. On a 300-persona benchmark: compositional zero-shot persona identification up to **17× above chance**, Spearman ρ ≈ **0.73** semantic–behavioral alignment, **22× faster inference** than an LLM-as-policy baseline.
- **Key innovations**: Once-per-NPC persona encoding + low-rank projection + neural conditioning; one shared policy scales to thousands of NPCs; traceability from behavior back to persona text.

### Spatial Reasoning in LLM Game Agents: Impact of Causal Context and Multi-Step Planning
- **Authors**: Mohit Jiwatode, Ronja Fuchs, Robin Schmöcker, Bodo Rosenhahn, Alexander Dockhorn
- **Affiliation**: —
- **Venue**: CoG 2026; arXiv Jul 2026
- **Link**: https://arxiv.org/abs/2607.22732
- **Abstract**: Examines whether LLM game-agent failures stem from limited spatial reasoning, and whether causal prompt augmentation and multi-step planning improve win-rates under latency constraints. Uses the Qwen3 family across scales/reasoning modes/planning horizons on a custom **GVGAI** benchmark (three games × five difficulty levels) isolating spatial navigation, with a positioning (coordinate) experiment plus gameplay study. Larger models with thinking mode localize better, but coordinate matching remains limited for smaller models.
- **Key innovations**: Controlled GVGAI spatial-navigation suite; separates localization ability from planning depth; latency/win-rate trade-off measurement.

### Empowering NPC Dialogue with Environmental Context Using LLMs and Panoramic Images
- **Authors**: Grega Radež, Ciril Bohak
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026 (cs.GR)
- **Link**: https://arxiv.org/abs/2604.19192
- **Abstract**: Enhances NPC dialogue with environmental awareness: capture a panoramic image of the NPC's surroundings, apply semantic segmentation to identify objects and positions, and compile a structured JSON (object locations + scene-graph data within the NPC's bounding sphere, encoded as directional vectors) fed to the LLM — giving NPCs spatial knowledge of what they "see" when conversing.
- **Key innovations**: Panorama → segmentation → structured spatial JSON pipeline for dialogue grounding; directional-vector scene encoding; no training required (inference-time augmentation).

## 3. Game Foundation Models

### NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt, Georgia Gkioxari, Jan Kautz, Yisong Yue, Yejin Choi, Yuke Zhu, Linxi "Jim" Fan
- **Affiliation**: NVIDIA / Stanford / Caltech / UChicago / UT Austin (as stated on paper)
- **Venue**: CVPR 2026; arXiv Jan 2026
- **Link**: https://arxiv.org/abs/2601.02427
- **Abstract**: Vision-action foundation model for generalist gaming agents trained on **40,000 hours of gameplay video across 1,000+ games**. Three ingredients: an internet-scale video-action dataset (actions auto-extracted from public gameplay videos), a multi-game benchmark environment measuring cross-game generalization, and a unified vision-action model trained with large-scale behavior cloning. Transfers to unseen games with up to **+52% relative** task success vs from-scratch models. Dataset, evaluation suite, and weights released.
- **Key innovations**: First open video→action gaming foundation model at this scale; automated action extraction from passive video; cross-game transfer benchmark.

### Towards Generalist Game Players: An Investigation of Foundation Models in the Game Multiverse
- **Authors**: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Tianyu Xin, Yue Su, Haisheng Wang, Han Yin, Hongbo Ma, Peize Li, Tianjun Gu, Xiangnan Wu, Xinran Zhang, Yongxuan Li, Zirong Chen, Yiming Li
- **Affiliation**: —
- **Venue**: arXiv preprint, May 2026
- **Link**: https://arxiv.org/abs/2605.09965
- **Abstract**: Positions the game multiverse as the ultimate ground for training and evaluating AGI — games as alternative physics/rulesets exercising omni-reality adaptability. Traces four eras: environment-specific symbolic/RL agents → large foundation models as generalist players → a future "creator" stage where agents both create new game worlds and continually evolve within them; surveys the full lifecycle of a generalist game player across these eras.
- **Key innovations**: Field-organizing taxonomy (four eras, creator stage as target); lifecycle framing of foundation-model game players; survey anchor for the game-foundation-model lane.

### Player-1: Learning to Play from Synthetic Experience
- **Authors**: Mingyu Ouyang, Yiran Wang, Siyuan Hu, Xingyilang Yin, Huiqiang Sun, Guangzhi Wang, Junfu Pu, Cheng Cheng, Honghao Chen, Ying Shan, Mike Zheng Shou, Hwee Tou Ng
- **Affiliation**: —
- **Venue**: arXiv preprint, Oct 2026 (on file since same-day sibling coverage)
- **Link**: https://arxiv.org/abs/2610.20584
- **Abstract** *(condensed — cross-referenced, not re-claimed)*: Post-training framework for game control beyond demonstrations via **synthetic experience**. Extends the computer-use action space (relative pointer motion, sustained inputs, composite actions); SFT on 6,044 curated gameplay trajectories; **Player-1-Gym** = 16 synthetic 2D/3D environments with programmatically verifiable rewards for multi-environment PPO. Player-1-9B improves MineDojo-300 success by **+27.8 pp** over its SFT policy (38.33% vs 12.63% best baseline), with gains on ViZDoom-10 and GameWorld.
- **Key innovations**: Synthetic RL environments for game control; composite action space; first covered by sibling [`arxiv-daily` 2026-10-20](../2026-10-20/arxiv-daily.md) — see that page for full detail.

## 4. Procedural Content Generation

### PCGRLLM: Large Language Model-Driven Reward Design for PCGRL
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Sam Earle, Zehua Jiang, Jin-Ha Noh, Julian Togelius, Kyung-Joong Kim
- **Affiliation**: —
- **Venue**: arXiv Feb 2025 (v2 May 2026)
- **Link**: https://arxiv.org/abs/2502.10906
- **Abstract**: Extends earlier PCGRL reward-generation work with a feedback mechanism and reasoning-based prompt engineering. Evaluated on story-to-reward generation for a 2D environment with two state-of-the-art LLMs across reasoning prompting methods, providing evaluations of LLM capability for content-generation reward design.
- **Key innovations**: Feedback loop + reasoning prompts for LLM-written PCGRL rewards; sits on the PCGRLLM lineage (with IPCGRL below) that anchors the wiki's PCG lane.

### IPCGRL: Language-Instructed Reinforcement Learning for Procedural Level Generation
- **Authors**: In-Chang Baek, Sung-Hyun Kim, Seo-Young Lee, Dong-Hyeon Kim, Kyung-Joong Kim
- **Affiliation**: —
- **Venue**: CoG 2025; arXiv Mar 2025
- **Link**: https://arxiv.org/abs/2503.12358
- **Abstract**: Instruction-based PCG via RL: incorporates a sentence embedding model and fine-tunes task-specific embeddings to compress game-level conditions. In a 2D level-generation task, beats a general-purpose embedding method with up to **+21.4% controllability** and **+17.2% generalizability** for unseen instructions.
- **Key innovations**: Task-fine-tuned text embeddings as PCGRL conditioning; measurable controllability/generalizability gains for unseen natural-language instructions.

### Video Game Level Design as Multi-Agent Reinforcement Learning
- **Authors**: Sam Earle et al.
- **Affiliation**: —
- **Venue**: AIIDE 2025 (proceedings; no arXiv ID tracked in this run)
- **Link**: proceedings (AIIDE 2025)
- **Abstract** *(single-source, proceedings summary)*: Frames video game level design as multi-agent RL, extending the PCGRL line from single-generator agents to multiple cooperating/competing generators over a shared level.
- **Key innovations**: Multi-agent formulation of level design (PCG lane's AIIDE anchor; listed for survey completeness alongside PCGRLLM/IPCGRL).

## 5. Game Benchmarks

### MINDGAMES: A Live Arena for Evaluating Social and Strategic Reasoning in Multi-Agent LLMs
- **Authors**: Kevin Wang, Anna Thöni, Benjamin Kempinski, Bobby Cheng, Jianzhu Yao, Benjamin Finch, Leon Guertler, Viraj Nadkarni, Yihan Jiang, Aliaksei Korshuk, Alexander Buyantuev, Ilya Makarov, Siyuan Wu, Yu-Chi Cheng, Yan-Ru Ju, Ti-Rong Wu, I-Hsuan Chu, Yu-Yu Hsu, et al. (53 authors)
- **Affiliation**: — (incl. Atlas Wang group per earlier coverage)
- **Venue**: arXiv preprint, May 2026
- **Link**: https://arxiv.org/abs/2605.29512
- **Abstract**: A multi-game live arena for LLM agents operationalizing theory-of-mind demands: belief attribution under hidden information, opponent modeling through repeated strategic interaction, cooperative inference under knowledge asymmetries, and sustained deception in social deduction. Built on **TextArena** with a unified interaction interface, **TrueSkill-based rating**, and full trajectory logging across four game environments.
- **Key innovations**: Live multi-game arena vs static vignettes; TrueSkill Elo for multi-agent LLMs; four complementary ToM reasoning axes in one platform.

### Checkpointed Exploration for Benchmarking Long-Horizon NetHack Agents
- **Authors**: (NeurIPS 2026 paper; authors not retrieved this run)
- **Affiliation**: —
- **Venue**: NeurIPS 2026 (accepted; no arXiv ID found in this run's searches)
- **Link**: NeurIPS 2026 virtual site (title search; arXiv ID pending/unpublished)
- **Abstract** *(single-source, from NeurIPS listing search)*: Introduces a NetHack benchmark built around **checkpointed exploration**, evaluating long-horizon agent behavior at fixed checkpoints (NetHack scores 0–15) with matched fresh games across lineages; includes frontier-LLM comparisons (Claude Opus 5.5 / Sonnet 5) measuring self-improvement per checkpoint.
- **Key innovations**: Checkpoint-conditional protocol for comparable long-horizon NetHack evaluation; extends the NLE lineage (on-file BAL/prime-agent-explore and related NetHack items in earlier dailies). ⚠️ arXiv ID not found — treat venue/abstract as single-source until camera-ready located.

### AAArena: Heuristic Learning in a Long-Running Game Agent Competition
- **Authors**: Kaisen Yang, Qingle Liu, Kejin Wang, Yicheng Zhao, Jieming Li, Shenghan Zheng, Ruize Yang, Bojun Yang, Heng Gong, Xiang Gao, Lanyue Zhang, Kaiyu Zhong, Zhuo Liu, Shaoxuan Li, Chengxi Li, Yong Yan, Weixuan Zhang, Tianwei Luo, Situ Wang, Youjie Zheng, Sihan Zhao, Shengyuan Wang, Huan-ang Gao, Jiazheng Xu, Xiaohui Xie, Wentao Han, Hongning Wang
- **Affiliation**: —
- **Venue**: arXiv preprint, Oct 2026 (on file since 2026-10-09/11)
- **Link**: https://arxiv.org/abs/2610.12341
- **Abstract** *(condensed — cross-referenced)*: Formalizes **Adversarial Heuristic Learning (AHL)**: AI agents as learning engines that refine executable game policies and supporting software with frozen model weights. **AAArena** = 12 authentic adversarial games + 1,920 archived human programs with a real-competition protocol (interpret rules, choose opponents, analyze replays, revise agents within budget). Opus 5.5 + Claude Code earns 6 gold medals; no configuration tops the remaining 6 human ladders; performance drops on more complex rule specifications.
- **Key innovations**: Agents-as-program-refiners (not weight trainers) for game AI; competition-faithful benchmark; first covered in [`game-rl-daily` 2026-10-11](../2026-10-11/game-rl-daily.md) — re-curated here for the benchmarks survey.

## 6. Industry Game AI

### AI for Games in the Foundation Model Era
- **Authors**: Meng Luo, Yanlin Li, Hao Li, Hongzhan Lin, Pengfei Zhou, Tianjie Ju, Ran Zhang, Yeying Jin, Mong-Li Lee, Wynne Hsu
- **Affiliation**: —
- **Venue**: arXiv preprint, Sep 2026
- **Link**: https://arxiv.org/abs/2609.16679
- **Abstract**: Surveys how foundation models and learned game-world models reshape AI across the game lifecycle. Organizes the literature into **six roles by immediate use of AI output**: playing and acting; modeling players and games; designing games; building and maintaining games; generating and adapting at runtime; testing and evaluating games. For each role examines what structure the game/workflow supplies, what AI learns/produces, and which capabilities transfer across games, engines, interfaces, and player populations.
- **Key innovations**: Six-role taxonomy unifying player-facing and production-facing game AI; explicit transfer analysis (which capabilities generalize vs stay game-tied); industry-era survey counterpart to the Game Multiverse academic survey (§3).

### Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén
- **Affiliation**: — (studio authors; Embark/Ubisoft per earlier tentative notes — not stated on abs page)
- **Venue**: CoG 2026; arXiv Jun 2026
- **Link**: https://arxiv.org/abs/2606.20210
- **Abstract**: Argues believable game AI remains a challenge for hand-coded systems and that ML models — learning from the game or from player data — open the door to human-like character behavior. Envisions future RL applications for game AI and surveys current research limitations that must clear for production adoption.
- **Key innovations**: Studio-perspective position/vision paper on deep RL for production game AI (behavioral complexity, believability, deployment limits).

## 7. Related Techniques

### Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
- **Authors**: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, et al.
- **Affiliation**: —
- **Venue**: arXiv preprint, Apr 2026 (v3 Jun 2026) — **new-to-wiki this run**
- **Link**: https://arxiv.org/abs/2604.22748
- **Abstract**: As AI systems move from generating text to accomplishing goals through sustained interaction, environment-dynamics modeling becomes the central bottleneck. Introduces a **"levels × laws" taxonomy**: three capability levels — **L1 Predictor** (one-step local transition operators), **L2 Simulator** (multi-step action-conditioned rollouts respecting domain laws), **L3 Evolver** (autonomously revises its own model when predictions fail against new evidence) — crossed with four governing-law regimes: **physical, digital, social, and scientific**.
- **Key innovations**: Levels×laws axes disambiguate the overloaded "world model" term across communities; L3 Evolver as the self-revision target state; organizing reference for the world-model/game-simulation lane.

### Code World Models for General Game Playing
- **Authors**: Wolfgang Lehrach, Daniel Hennes, Miguel Lazaro-Gredilla, Xinghua Lou, Carter Wendelken, Zun Li, Antoine Dedieu, Jordi Grau-Moya, Marc Lanctot, Atil Iscen, John Schultz, Marcus Chiam, Ian Gemp, Piotr Zielinski, Satinder Singh, Kevin P. Murphy
- **Affiliation**: Google DeepMind
- **Venue**: ICLR 2026; arXiv Oct 2025
- **Link**: https://arxiv.org/abs/2510.04542
- **Abstract**: Replaces prompting LLMs for direct move generation (frequent illegal moves, strategically shallow play) with translating natural-language rules and trajectories into a **formal executable world model in Python** — state transition, legal-move enumeration, termination checks — used as a verifiable simulation engine for high-performance planning (MCTS). Also prompts the LLM for heuristic value functions (MCTS efficiency) and inference-time improvements.
- **Key innovations**: LLM-as-compiler of game rules into verifiable Python simulators; separates world-model authoring from policy search; bridges LLMs and classical game-tree search.

### SPADE: Self-Play in Adaptive Synthetic Executable Environments
- **Authors**: Bo Liu, Simon Yu, Yiding Jiang, Ao Qu, Andrew Zhao, Zichen Liu, Junsu Kim, Zijian Zhou, Seungone Kim, Tongzheng Ren, Mickel Liu, Hanfei Yu, Zhaorun Chen, Weiyan Shi, Paul Pu Liang, Luke Zettlemoyer, Yejin Choi, Natasha Jaques
- **Affiliation**: —
- **Venue**: arXiv preprint, Aug 2026 (v3 Aug 2026; on file since Aug)
- **Link**: https://arxiv.org/abs/2608.19197
- **Abstract**: A single LLM plays two roles: **Environment Designer** (writes complete long-horizon training environments as executable code with a Gym-style `reset()`/`step()` interface) and **Reasoning Agent** (learns to act in them). Each is a stateful multi-turn environment (state transitions, rewards, verification code), so one interface spans reasoning problems and multi-step agentic tool use. The Reasoning Agent's regret is estimated from the reward gap with/without privilege information.
- **Key innovations**: Environment-generation self-play (designer/agent dual role); executable-code environments with built-in verifiers; SPIRAL-lineage extension from fixed templates (GameSmith §1) to open-ended environment synthesis.

### Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills
- **Authors**: Siyuan Huang, Pengyu Cheng, Haotian Liu, Tao Chen, Yihao Liu, Jingwei Ni, Shijie Zhou, Ziyi Yang, Gangwei Jiang, Mengyu Zhou, Yu Cheng, Xiaoxi Jiang, Guanjun Jiang
- **Affiliation**: Qwen Business Unit (per earlier coverage)
- **Venue**: arXiv preprint, Jul 2026
- **Link**: https://arxiv.org/abs/2607.22529
- **Abstract**: Identifies a dilemma in LLM self-evolution: environment-bound methods give precise feedback but narrow domains; open-ended self-generation broadens tasks but lacks reliable verification. **Agent skills** reconcile this — each skill ensures deep verifiable execution in a scenario, while dynamic routing maintains open-ended variety. **Skill-SP** = proposer + solver + dynamic skill controller, orchestrated via an RL loop.
- **Key innovations**: Skills as the verification/diversity middle ground; co-evolutionary proposer-solver-controller loop; RL-orchestrated skill economy.

### World Models as an Intermediary between Agents and the Real World
- **Authors**: Sherry Yang
- **Affiliation**: —
- **Venue**: arXiv preprint, Jan 2026 — **new-to-wiki this run**
- **Link**: https://arxiv.org/abs/2602.00785
- **Abstract**: LLM agents trained with RL are superhuman in low-cost environments (games, math, coding) but these gains haven't transferred to domains where interaction is expensive (robotics physical cost, ML-engineering time, scientific resource cost). Argues the bottleneck is the expense of executing actions to acquire reward signals, and proposes **world models as an intermediary between agents and the real world** — models of dynamics, rewards, and task distributions overcoming fundamental barriers of high-cost actions such as extreme off-policy learning and sample inefficiency.
- **Key innovations**: Position paper locating world models as the cost-amortization layer for high-stakes domains; extends the game-RL success story into the transfer argument for physical/scientific agents.

### PEARL: Process-Experience Aware Reinforcement Learning for Multi-Turn Agents
- **Authors**: Jie Yang, Mianqiu Huang, Yiwei Zhao, Bo Wang, Yang Liu, Yuxin Wang
- **Affiliation**: —
- **Venue**: arXiv preprint, Oct 2026 — **new-to-wiki this run**
- **Link**: https://arxiv.org/abs/2610.14636
- **Abstract**: Terminal rewards make multi-turn agents trainable without step labels, but group-relative advantages say little about *which* intermediate decisions to adjust; failed trajectories still contain reasonable actions, and bad patterns recur. PEARL improves local credit assignment **without an extra critic**: given two continuations from the same history with different outcomes, it locates their first divergence, builds a feature representation of each branch's local decision, and clusters decision features in recent failure/success memories to find recurring patterns — selectively strengthening negative advantages at lower-reward decisions.
- **Key innovations**: Divergence-point local decision features + pattern memory for critic-free credit assignment; negative-advantage sharpening only where failure patterns recur; relevant to game/multi-turn agent RL lanes.

### RL for Large-Scale Lifelong Multi-Agent Path Finding with Shared Spatial Fields
- **Authors**: Jean Seong Bjorn Choe
- **Affiliation**: —
- **Venue**: arXiv preprint, Oct 2026 — **new-to-wiki this run**
- **Link**: https://arxiv.org/abs/2610.18186
- **Abstract**: Lifelong MAPF needs cheap movement decisions under changing traffic and varied layouts. A CNN computes a **shared spatial field over the map once per timestep**; a compact goal-conditioned operator derives each agent's movement preferences. Trained end-to-end with **average-reward RL** (throughput as reward, no planner demonstrations, no separate online planner). One policy per layout class, trained on small maps, deploys without retraining on larger unseen layouts — across six 10,000-agent layouts, throughput comparable to or above the strongest baselines, execution **< 10 ms/step** (>10× faster than several established planners).
- **Key innovations**: Shared per-map spatial field amortizes computation across 10k agents; average-reward lifelong formulation; zero-shot transfer to larger maps/populations.

---

## §0 Dedup and Cross-References

| arXiv ID | Item | Status in this run |
|----------|------|--------------------|
| 2604.22748 | Agentic World Modeling | **new-to-wiki, featured** (§7) |
| 2602.00785 | World Models as Intermediary | **new-to-wiki, featured** (§7) |
| 2610.14636 | PEARL | **new-to-wiki, featured** (§7) |
| 2610.18186 | LMAPF Shared Spatial Fields | **new-to-wiki, featured** (§7) |
| — | NetHack Checkpointed Exploration | **proceedings-only** (NeurIPS 2026; no arXiv ID found) (§5) |
| 2610.13995 | GameSmith | on file (10-15, 10-20 arxiv-daily siblings) — re-curated §1 |
| 2506.24119 | SPIRAL | on file (many dailies; ICLR 2026) — re-curated §1 |
| 2605.28863 | Big 2 self-play | on file — re-curated §1 |
| 2604.05476 | Tablut AlphaZero | on file — re-curated §1 |
| 2606.30092 | HRL-IM/CBS StarCraft | on file — re-curated §1 |
| 2609.27331 | JEV-Star | on file — re-curated §1 |
| 2610.17391 | Learning to Play (book) | on file (10-15, 10-20) — re-curated §1 |
| 2609.02931 | LLM-Guided NPC combat | on file — re-curated §2 |
| 2604.04703 | Bounded Autonomy | on file — re-curated §2 |
| 2605.23652 | pcsp | on file — re-curated §2 |
| 2607.22732 | Spatial Reasoning GVGAI | on file — re-curated §2 |
| 2604.19192 | NPC dialogue panorama | on file — re-curated §2 |
| 2601.02427 | NitroGen | on file (CVPR 2026) — re-curated §3 |
| 2605.09965 | Game Multiverse survey | on file — re-curated §3 |
| 2610.20584 | Player-1 | **claimed by same-day sibling** [`arxiv-daily` 10-20](../2026-10-20/arxiv-daily.md) — condensed cross-ref §3 |
| 2502.10906 | PCGRLLM | on file — re-curated §4 |
| 2503.12358 | IPCGRL | on file (CoG 2025) — re-curated §4 |
| 2605.29512 | MINDGAMES | on file — re-curated §5 |
| 2610.12341 | AAArena | on file (10-09/10-11) — re-curated §5 |
| 2609.16679 | AI for Games (FM era) | on file — re-curated §6 |
| 2606.20210 | Augmenting Game AI (CoG 2026) | on file — re-curated §6 |
| 2510.04542 | Code World Models | on file (ICLR 2026) — re-curated §7 |
| 2608.19197 | SPADE | on file — re-curated §7 |
| 2607.22529 | Skill Self-Play | on file — re-curated §7 |

**Flags**: ⚠️ All claims abstract-only (no full-text/code verification this run). Affiliations "not stated" unless declared on the abs page — never inferred (exceptions marked inline: NitroGen, Code World Models). ⚠️ NetHack Checkpointed Exploration is single-source from search results; no arXiv ID located — verify at camera-ready. Player-1 first-covered by same-day sibling `arxiv-daily` 10-20 → cross-referenced, not re-claimed. No contradictions against existing wiki pages; several entries (SPIRAL, GameSmith, NitroGen, pcsp) continue threads already tracked in prior dailies.
