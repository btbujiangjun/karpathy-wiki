---
title: "Game RL Daily - 2026-10-27"
type: synthesis
created: 2026-10-27
updated: 2026-10-27
sources: []
tags: [game-rl, game-ai, llm-agents, reinforcement-learning, self-play, foundation-models, procedural-content-generation, benchmarks, world-models, vlm, multi-agent-rl]
---

# Game RL Daily - 2026-10-27

## 1) Game RL (Atari/StarCraft/Dota/Go/chess/poker/Minecraft/NetHack, multi-agent, self-play, PBT, open-ended)

- **Title:** Modular Discovery of General Game-Playing Algorithms with Large Language Models
- **Authors:** Zun Li, John Schultz, Marc Lanctot, Daniel Hennes
- **Affiliation:** Google DeepMind
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2609.33115](https://arxiv.org/abs/2609.33115)
- **PDF:** [https://arxiv.org/pdf/2609.33115](https://arxiv.org/pdf/2609.33115)
- **Abstract:** General Game Playing across arbitrary games from rules alone remains challenging due to differing algorithmic requirements across game classes and strict decision-time compute limits. This work explores using large language models to modularly discover general game-playing algorithms by composing search, learning, and heuristics from first principles given game rules.
- **Key Innovations:**
  - **LLM-driven modular discovery:** Uses LLMs to synthesize and compose algorithmic components for general game playing from rule descriptions.
  - **Cross-game generality:** Targets algorithm discovery that adapts across diverse game classes rather than tuning per-game heuristics.
  - **Compute-aware design:** Emphasizes decision-time efficiency for practical GGP settings.

- **Title:** MARL-BattleGrounds: A Novel JAX-native Benchmark for Heterogeneous and Competitive Multi-agent RL
- **Authors:** Ulixes Tariq Hawili, Subramanian Ramamoorthy, Yoann Altmann, Ignacio Carlucho
- **Affiliation:** University of Edinburgh
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.14883](https://arxiv.org/abs/2610.14883)
- **PDF:** [https://arxiv.org/pdf/2610.14883](https://arxiv.org/pdf/2610.14883)
- **Abstract:** We present MARL-BattleGrounds (MARL-BGs), an easy-to-use JAX-native benchmark for heterogeneous and competitive multi-agent RL. The benchmark provides fast, vectorized environments designed for scalable evaluation of modern MARL algorithms under heterogeneity and competition.
- **Key Innovations:**
  - **JAX-native speed:** Vectorized environments enable high-throughput training/evaluation for competitive MARL.
  - **Heterogeneous agents:** Explicit support for asymmetric roles/abilities across agents in competitive settings.
  - **Benchmarking focus:** Structured evaluation suite targeting heterogeneous competitive multi-agent RL.

## 2) Game AI Bot (LLM game agents, NPC intelligence, bot frameworks, autonomous gameplay)

- **Title:** HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games
- **Authors:** Zecong Tang, Zian Guan, Yuncheng Guo, Zhanqiu Zhang, Yiwen Guo, Bo Dai
- **Affiliation:** The University of Hong Kong, Zhejiang University, Fudan University, LIGHTSPEED, Independent Researcher
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.31162](https://arxiv.org/abs/2610.31162)
- **PDF:** [https://arxiv.org/pdf/2610.31162](https://arxiv.org/pdf/2610.31162)
- **Abstract:** Building virtual embodied agents that operate in open-ended games like human players is a long-standing goal requiring both long-horizon autonomy and reliable native-interface control. We propose HiSTEVE, a hierarchical VLA agent with a capability-aware agent harness for Minecraft with vision-only perception and native keyboard-and-mouse actions.
- **Key Innovations:**
  - **Hierarchical VLA + harness:** Orchestration level with structured memory and VLM planner; control level with single VLA executing subtasks via native interface.
  - **Policy-coupled completion detection:** Task completion state detector conditioned on VLA policy context for reliable subtask completion.
  - **Regime-specific architecture:** Regime-specific RMSNorm branches and separate mouse-movement token embeddings to mitigate GUI/non-GUI interference; trained with world knowledge injection, IL, and RL with environment feedback.
  - **Strong results:** 85.0% on MineStudio Bench, 37.4% average success on OpenHA, and successful long-horizon iron pickaxe crafting from scratch.

- **Title:** Learn2Play Bench: How Well Do LLM Agents Learn from Experience in Unfamiliar Environments?
- **Authors:** Yibo Li, Jinhang Qiu, Zhi Zheng, Qianyun Guo, Jiaying Wu, Shuo Ji, Bryan Hooi
- **Affiliation:** National University of Singapore
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.08215](https://arxiv.org/abs/2610.08215)
- **PDF:** [https://arxiv.org/pdf/2610.08215](https://arxiv.org/pdf/2610.08215)
- **Abstract:** Learning from experience is essential for LLM agents to adapt to unfamiliar and dynamic environments. We introduce Learn2Play Bench, a benchmark for evaluating how well LLM agents learn from experience in unfamiliar game environments.
- **Key Innovations:**
  - **Experience-learning focus:** Evaluates in-context/adaptive learning from interaction history rather than just zero-shot task performance.
  - **Unfamiliar environments:** Tests generalization to novel games/tasks where prior knowledge alone is insufficient.
  - **Benchmark design:** Provides controlled settings to measure improvement over experience across agent strategies.

- **Title:** SpeedrunBench: Challenging LLM Agents with Video Game Speedrunning
- **Authors:** Yoshinari Fujinuma, Keisuke Kamahori, Ryuto Koike, Abdelrahman Madkour, Varun Prashant Gangal, Monty Bichouna, Martyna Markiewicz, Shivani Jain, Duncan Curtis, Rebecca Qian, Anand Kannappan
- **Affiliation:** Scale AI
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.08076](https://arxiv.org/abs/2610.08076)
- **PDF:** [https://arxiv.org/pdf/2610.08076](https://arxiv.org/pdf/2610.08076)
- **Abstract:** Frontier LLM agents are capable of solving increasingly complex tasks with measurable human solutions. SpeedrunBench evaluates LLM agents on video game speedrunning tasks that require precise sequence execution, optimization of routes/strategies, and efficient use of game mechanics.
- **Key Innovations:**
  - **Speedrunning as evaluation:** Frames tasks around achieving optimal/fast completion times, testing planning, execution precision, and strategy optimization.
  - **Measurable objectives:** Uses time-to-completion/sequence optimality as concrete metrics tied to human speedrun baselines.
  - **Challenging long-horizon tasks:** Targets games where mastery requires discovering efficient strategies and executing them reliably.

- **Title:** Finding the Move Is Not Winning the Game: XiangqiBench for Closed-Loop Evaluation of LLM Agents
- **Authors:** Yekun Chai, Qiwei Peng, Haoyi Xiong
- **Affiliation:** Baidu Inc.
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.02425](https://arxiv.org/abs/2610.02425)
- **PDF:** [https://arxiv.org/pdf/2610.02425](https://arxiv.org/pdf/2610.02425)
- **Abstract:** Static evaluations credit a language model for naming the right move, but an agent must carry a plan through to a verified outcome while an opponent responds. XiangqiBench provides executable closed-loop evaluation of LLM agents in Xiangqi (Chinese chess).
- **Key Innovations:**
  - **Closed-loop evaluation:** Tests full game play with adversarial responses rather than single-move prediction accuracy.
  - **Outcome-based metrics:** Measures win/draw/loss and game-theoretic performance under opponent play.
  - **Strategic depth:** Evaluates long-horizon planning and adaptation in a classical perfect-information game.

## 3) Game Foundation Models (generalist/VLM game agents)

- **Title:** SpireBench: Evaluating Long-Horizon Strategic Play of Agentic Models with Slay the Spire
- **Authors:** Scott C. Lowe, Sander W. Keemink
- **Affiliation:** Independent Researcher
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.12596](https://arxiv.org/abs/2610.12596)
- **PDF:** [https://arxiv.org/pdf/2610.12596](https://arxiv.org/pdf/2610.12596)
- **Abstract:** Agentic large language models now tackle complex tasks, yet strategic reasoning over long horizons is under-studied. SpireBench evaluates long-horizon strategic play using Slay the Spire, a deck-building roguelike with stochasticity, resource management, and multi-turn planning.
- **Key Innovations:**
  - **Long-horizon strategic benchmark:** Targets planning across many turns with uncertain outcomes and evolving state.
  - **Deck-building domain:** Tests synergy discovery, risk management, and adaptive strategy.
  - **Agentic model evaluation:** Focuses on models capable of tool/agentic interaction with the game environment.

- **Title:** PlaySuite: A Large-Scale Benchmark for Interactive Visual Intelligence
- **Authors:** Dheeraj Varghese, Anna Vettoruzzo, Walter Simoncini, Michelle Lorena Acevedo Callejas, Mohammad Mahdi Derakhshani, Kristof Meding, Joaquin Vanschoren, Cees G. M. Snoek
- **Affiliation:** University of Amsterdam
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.07127](https://arxiv.org/abs/2610.07127)
- **PDF:** [https://arxiv.org/pdf/2610.07127](https://arxiv.org/pdf/2610.07127)
- **Abstract:** Recent advances in multimodal foundation models yield strong performance on static perception and reasoning benchmarks, yet such evaluations largely overlook acting in interactive environments. PlaySuite is a large-scale benchmark for interactive visual intelligence across diverse games/tasks.
- **Key Innovations:**
  - **Interactive visual intelligence:** Evaluates perception+action loops rather than static VQA.
  - **Large-scale suite:** Covers diverse interactive scenarios to test generalist capabilities.
  - **Foundation model focus:** Designed for benchmarking VLM/vision-language agents in interactive settings.

## 4) Procedural Content Generation (PCG)

- **Title:** GAMEGO: Training Game-Dev Agents with Synthetic Trajectories Anchored in Real-World Assets
- **Authors:** Haoyue Yang, Jingyao Li, Zhengfan Wu, Jing Liu, Xuanle Zhao, Kang Liu
- **Affiliation:** Shanghai Artificial Intelligence Laboratory, Shanghai Jiao Tong University
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.06910](https://arxiv.org/abs/2610.06910)
- **PDF:** [https://arxiv.org/pdf/2610.06910](https://arxiv.org/pdf/2610.06910)
- **Abstract:** Recent advances in Large Language Models (LLMs) have demonstrated remarkable capabilities in web front-end execution; extending to game development remains challenging. GAMEGO trains game-dev agents with synthetic trajectories anchored in real-world assets to improve game content/code generation.
- **Key Innovations:**
  - **Synthetic trajectory generation:** Creates training data for game development agents grounded in real assets.
  - **Asset-anchored learning:** Improves realism and usability of generated game content.
  - **Game-dev agent training:** Targets end-to-end game creation tasks beyond static code generation.

## 5) Game Benchmarks

- **Title:** Learn2Play Bench: How Well Do LLM Agents Learn from Experience in Unfamiliar Environments? (also listed in §2)
- **Authors:** Yibo Li et al.
- **Affiliation:** National University of Singapore
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.08215](https://arxiv.org/abs/2610.08215)
- **PDF:** [https://arxiv.org/pdf/2610.08215](https://arxiv.org/pdf/2610.08215)
- **Abstract:** Evaluates experience-based learning of LLM agents in unfamiliar environments.
- **Key Innovations:**
  - **Learning-from-experience metric:** Measures adaptation over interaction rather than static accuracy.
  - **Unfamiliarity:** Tests transfer to novel games with minimal prior exposure.

- **Title:** SpeedrunBench: Challenging LLM Agents with Video Game Speedrunning (also listed in §2)
- **Authors:** Yoshinari Fujinuma et al.
- **Affiliation:** Scale AI
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.08076](https://arxiv.org/abs/2610.08076)
- **PDF:** [https://arxiv.org/pdf/2610.08076](https://arxiv.org/pdf/2610.08076)
- **Abstract:** Speedrunning provides objective, optimizable metrics for agent evaluation.
- **Key Innovations:**
  - **Objective optimization:** Time-to-completion as clear reward/metric.
  - **Sequence-level planning:** Requires precise action sequences and route optimization.

- **Title:** SpireBench: Evaluating Long-Horizon Strategic Play of Agentic Models with Slay the Spire (also listed in §3)
- **Authors:** Scott C. Lowe, Sander W. Keemink
- **Affiliation:** Independent Researcher
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.12596](https://arxiv.org/abs/2610.12596)
- **PDF:** [https://arxiv.org/pdf/2610.12596](https://arxiv.org/pdf/2610.12596)
- **Abstract:** Long-horizon strategic evaluation in a stochastic deck-building game.
- **Key Innovations:**
  - **Stochastic long-horizon:** Tests planning under uncertainty across runs.
  - **Synergy/strategy discovery:** Evaluates adaptive decision-making.

- **Title:** PlaySuite: A Large-Scale Benchmark for Interactive Visual Intelligence (also listed in §3)
- **Authors:** Dheeraj Varghese et al.
- **Affiliation:** University of Amsterdam
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.07127](https://arxiv.org/abs/2610.07127)
- **PDF:** [https://arxiv.org/pdf/2610.07127](https://arxiv.org/pdf/2610.07127)
- **Abstract:** Large-scale interactive benchmark for VLM agents.
- **Key Innovations:**
  - **Perception-action loops:** Unified evaluation of visual understanding and control.

- **Title:** MARL-BattleGrounds: A Novel JAX-native Benchmark for Heterogeneous and Competitive Multi-agent RL (also listed in §1)
- **Authors:** Ulixes Tariq Hawili et al.
- **Affiliation:** University of Edinburgh
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.14883](https://arxiv.org/abs/2610.14883)
- **PDF:** [https://arxiv.org/pdf/2610.14883](https://arxiv.org/pdf/2610.14883)
- **Abstract:** JAX-native benchmark for heterogeneous competitive MARL.
- **Key Innovations:**
  - **Scalable vectorized envs:** Enables large-scale competitive evaluation.
  - **Heterogeneity focus:** Tests coordination/competition with asymmetric agents.

- **Title:** XiangqiBench for Closed-Loop Evaluation of LLM Agents (also listed in §2)
- **Authors:** Yekun Chai et al.
- **Affiliation:** Baidu Inc.
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.02425](https://arxiv.org/abs/2610.02425)
- **PDF:** [https://arxiv.org/pdf/2610.02425](https://arxiv.org/pdf/2610.02425)
- **Abstract:** Closed-loop adversarial evaluation for board game agents.
- **Key Innovations:**
  - **Opponent-in-the-loop:** Measures outcome-based performance under response.

## 6) Industry Game AI (studios, deployment, real-time inference)

- **Title:** HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games (also listed in §2)
- **Authors:** Zecong Tang et al.
- **Affiliation:** The University of Hong Kong, Zhejiang University, Fudan University, LIGHTSPEED, Independent Researcher
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.31162](https://arxiv.org/abs/2610.31162)
- **PDF:** [https://arxiv.org/pdf/2610.31162](https://arxiv.org/pdf/2610.31162)
- **Abstract:** Targets human-like native-interface control in open-world games like Minecraft, relevant to in-game NPC/assistant agents and automation.
- **Key Innovations:**
  - **Native interface control:** Keyboard/mouse vision-only control suitable for deployment without heavy API instrumentation.
  - **Capability-aware orchestration:** Practical harness design for reliable long-horizon execution.
  - **Production-relevant evaluation:** Tests on MineStudio Bench/OpenHA with long-horizon tasks.

- **Title:** GAMEGO: Training Game-Dev Agents with Synthetic Trajectories Anchored in Real-World Assets (also listed in §4)
- **Authors:** Haoyue Yang et al.
- **Affiliation:** Shanghai Artificial Intelligence Laboratory, Shanghai Jiao Tong University
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.06910](https://arxiv.org/abs/2610.06910)
- **PDF:** [https://arxiv.org/pdf/2610.06910](https://arxiv.org/pdf/2610.06910)
- **Abstract:** Addresses game development automation with asset-grounded synthetic data.
- **Key Innovations:**
  - **Industry-relevant task:** Targets practical game-dev workflows.
  - **Asset anchoring:** Improves applicability to real content pipelines.

## 7) Related techniques (self-play RL, curiosity, HRL, IL, IRL, reward shaping, world models, model-based/offline RL)

- **Title:** Modular Discovery of General Game-Playing Algorithms with Large Language Models (also listed in §1)
- **Authors:** Zun Li et al.
- **Affiliation:** Google DeepMind
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2609.33115](https://arxiv.org/abs/2609.33115)
- **PDF:** [https://arxiv.org/pdf/2609.33115](https://arxiv.org/pdf/2609.33115)
- **Abstract:** Combines LLMs with algorithmic search/learning components for general play.
- **Key Innovations:**
  - **LLM+search synthesis:** Modular composition of planning/learning/heuristics.
  - **Self-play/competitive generality:** Targets algorithm discovery across game classes.

- **Title:** HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games (also listed in §2,§6)
- **Authors:** Zecong Tang et al.
- **Affiliation:** The University of Hong Kong, Zhejiang University, Fudan University, LIGHTSPEED, Independent Researcher
- **Venue:** arXiv 2026
- **arXiv:** [https://arxiv.org/abs/2610.31162](https://arxiv.org/abs/2610.31162)
- **PDF:** [https://arxiv.org/pdf/2610.31162](https://arxiv.org/pdf/2610.31162)
- **Abstract:** Hierarchical VLA with IL+RL, policy-coupled completion detection, regime-specific architecture.
- **Key Innovations:**
  - **Hierarchical control:** VLM planner + VLA policy with capability-aware harness.
  - **Robust execution:** Regime-specific normalization and separate mouse embeddings for mixed GUI/non-GUI actions.
  - **Learning mixture:** Combines world knowledge injection, imitation learning, and RL with environment feedback.
