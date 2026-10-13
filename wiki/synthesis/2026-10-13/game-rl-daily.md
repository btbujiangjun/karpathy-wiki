---
title: Game RL & Game AI Bot — Daily Digest (2026-10-13)
type: synthesis
created: 2026-10-13
updated: 2026-10-13
sources: []
tags: [game-rl, game-ai, llm-agents, reinforcement-learning, self-play, foundation-models, pcg, benchmarks, world-models, vlm, daily-digest]
---
# Game RL & Game AI Bot — Daily Digest (2026-10-13)

*This digest focuses on papers directly relevant to Game RL, Game AI Bots, Game Foundation Models, PCG, Game Benchmarks, and related techniques. Sources: arXiv "Games / Multi-Agent / Bandits / Mechanism Design" block (2026-10-09 submitted; harvested 2026-10-13).*

## Game RL, Multi-Agent RL & Self-Play

### The Distortion of Threshold Approval Multiwinner Voting
- **Title:** The Distortion of Threshold Approval Multiwinner Voting
- **Authors:** Mohamad Latifian, Marzieh Nilipour, Alexandros A. Voudouris
- **Affiliation:** not stated
- **Venue:** arXiv preprint (2026-10-09)
- **arXiv:** [https://arxiv.org/abs/2610.13725](https://arxiv.org/abs/2610.13725)
- **PDF:** [http://arxiv.org/pdf/2610.13725](http://arxiv.org/pdf/2610.13725)
- **Subjects:** cs.GT
- **Abstract:** Multiwinner voting with n voters and m candidates selects a committee of size k. Voters report approval sets induced by t utility thresholds (unit-sum cardinal utilities). Each voter's utility for a committee is a normalized monotone symmetric norm (additive welfare, best-representative, top-r, ℓ_p, normalized non-increasing OWAs). 
- **Key Innovations:** Deterministic rule distortion ≤ 2(2m)^{1/t}; randomized ≤ 2·min{m^{1/(t+1)}, m/k}. Single threshold gives O(m)/O(√m); O(log m) thresholds suffice for constant distortion; asymptotically matching lower bounds.
- **Relevance:** Multi-agent collective decision-making in competitive/cooperative settings; informs population-based training, voting/committee formation in game AI (e.g. team composition, meta-agents), and mechanism design for multi-agent systems.

### Collective Autonomous Vehicle Routing Needs Social Awareness for Coexistence with Human Drivers
- **Title:** Collective Autonomous Vehicle Routing Needs Social Awareness for Coexistence with Human Drivers
- **Authors:** Anastasia Psarou, Mikolaj Rams, Blazej Torbus, Rafal Kucharski
- **Affiliation:** not stated
- **Venue:** arXiv preprint (2026-10-09)
- **arXiv:** [https://arxiv.org/abs/2610.13439](https://arxiv.org/abs/2610.13439)
- **PDF:** [http://arxiv.org/pdf/2610.13439](http://arxiv.org/pdf/2610.13439)
- **Subjects:** cs.MA; cs.AI
- **Abstract:** Collective AV route choices can create externalities for human-driven vehicles (HDVs). Adding *marginal cost* (AV impact on others' travel times vs counterfactual without AV) to selfish travel-time reward; studied in mixed-autonomy via MARL.
- **Key Innovations:** Incorporating marginal cost limits HDV travel-time increases, shortens AV travel times, improves overall system performance (Ingolstadt 40% AVs: +1.7% HDV under selfish → +1.1% with social). Computing marginal cost only for most influential AVs achieves similar results at lower cost; over-weighting social term degrades system.
- **Relevance:** Mixed human-AI multi-agent systems; transferable to multi-agent game RL (social awareness, credit assignment to others' welfare, population-level objectives).

## Game AI Bots & LLM-Powered Game Agents

### CB-Orchestrator: Adaptive Workflow Optimization for LLM Agents via Contextual Bandits
- **Title:** CB-Orchestrator: Adaptive Workflow Optimization for LLM Agents via Contextual Bandits
- **Authors:** Jiahang Sun, Zhiwei Shang, Zhipiao Liu, Hongwei Yang, Guoqing Xie, Shuang Qiu, Zhongxiang Dai
- **Affiliation:** not stated (ICML 2026 Workshop on Compositional Learning)
- **Venue:** arXiv preprint (2026-10-09)
- **arXiv:** [https://arxiv.org/abs/2610.13064](https://arxiv.org/abs/2610.13064)
- **PDF:** [http://arxiv.org/pdf/2610.13064](http://arxiv.org/pdf/2610.13064)
- **Subjects:** cs.LG
- **Abstract:** Hand-designed LLM agent workflows are inflexible; automated optimization expensive. CB-Orchestrator decouples workflow generation (evolutionary search to build candidate pool) from selection (contextual bandit) for per-query adaptive selection with less feedback.
- **Key Innovations:** Sample-efficient learning with far less training-phase feedback; at inference adaptively selects optimal workflow per query. Beats baselines on five benchmarks; MATH reduces training-phase API token overhead ≥40.55% (total ≥29.73%).
- **Relevance:** Cost-performance tradeoffs critical for LLM-powered game agents (real-time inference, budget-constrained NPCs). Workflow orchestration transferable to agentic gameplay frameworks.

## Related Techniques (Bandits, Exploration, Mechanism Design)

### Gaussian-Width Bounds for Offline-to-Online Linear Bandits
- **Title:** Gaussian-Width Bounds for Offline-to-Online Linear Bandits
- **Authors:** Kushagra Chandak, Volodymyr Tkachuk, Xiaoqi Tan, Csaba Szepesvári
- **Affiliation:** not stated (DeepMind/Alberta-adjacent)
- **Venue:** arXiv preprint (2026-10-09)
- **arXiv:** [https://arxiv.org/abs/2610.12990](https://arxiv.org/abs/2610.12990)
- **PDF:** [http://arxiv.org/pdf/2610.12990](http://arxiv.org/pdf/2610.12990)
- **Subjects:** cs.LG
- **Abstract:** Offline data helps online learning in stochastic linear bandits under partial coverage (only k of d feature directions poorly covered). Phased-elimination/optimism give Õ(√(dkT)); tighter control via concentration of Lipschitz functions of Gaussian vectors yields phased-elimination with regret Õ(k√T). Matching lower/upper bounds; pure exploration with offline data also analyzed.
- **Key Innovations:** Gaussian-width based bounds improve dependence under partial coverage; tighter regret analysis.
- **Relevance:** Exploration-exploitation, efficient learning from prior data, curriculum/transfer — relevant to RL agents in games (leveraging replays, offline-to-online fine-tuning).

## Game Theory / Security (Contextual)

### The False Allure of "Security by Obscurity": A Game-Theoretic Approach
- **Title:** The False Allure of "Security by Obscurity": A Game-Theoretic Approach
- **Authors:** In-Uck Park, Sunoo Park
- **Affiliation:** not stated
- **Venue:** arXiv preprint (2026-10-09)
- **arXiv:** [https://arxiv.org/abs/2610.12858](https://arxiv.org/abs/2610.12858)
- **PDF:** [http://arxiv.org/pdf/2610.12858](http://arxiv.org/pdf/2610.12858)
- **Subjects:** cs.GT; cs.CR; cs.CY; econ.TH
- **Abstract:** Rigorous game-theoretic modeling shows that under realistic conditions, "obscured" systems are more likely to suffer successful attacks than "open" systems — supporting received wisdom.
- **Relevance:** Security considerations for game AI agents, anti-cheat, robustness in adversarial multi-agent games.

## Notes

- This batch (2026-10-09 submitted) contains limited directly game-specific RL (Atari/StarCraft/Minecraft/etc.) papers in the harvested section; the strongest game-relevant items are multi-agent/social routing, multiwinner voting (mechanism design), and LLM-agent workflow optimization.
- All items extracted from the 2026-10-13 arXiv daily digest's "Games / Multi-Agent / Bandits / Mechanism Design" section. Affiliations omitted in arXiv metadata; marked as `not stated`.
