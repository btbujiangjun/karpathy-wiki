---
title: arXiv Daily — AI, LLMs, CTR, Games (May 31, 2026)
type: synthesis
created: 2026-05-31
updated: 2026-05-31
sources: [2605.30344, 2605.30337, 2605.30330, 2605.30288, 2605.30284, 2605.29940, 2605.29927, 2605.29919, 2605.29893, 2605.22138, 2605.19376, 2605.17570, 2605.15905, 2605.13496, 2605.06066, 2605.02028, 2602.08467, 2502.06823]
tags: [arxiv, daily-digest, ai, llm, ctr, recommendation, agents, reasoning, games, time-series]
---

# arXiv Daily — AI, LLMs, CTR, Games (May 31, 2026)

Daily scan of arXiv recent submissions in cs.AI, cs.LG, cs.IR, cs.CL, and cs.SE. Picks the most interesting papers across AI, LLMs, recommendation/CTR, sequential modeling, games, and related domains.

---

## 🧠 LLM Reasoning & Agents

### 1. Efficient Agentic Reasoning Through Self-Regulated Simulative Planning

**Authors:** Mingkai Deng, Jinyu Hou, Lara Sá Neves, Varad Pimpalkhute, Taylor W. Killian, Zhengzhong Liu, Eric P. Xing

**Institution:** Carnegie Mellon University (IFM)

**arXiv:** [2605.22138](https://arxiv.org/abs/2605.22138) | Submitted May 21, 2026

Proposes decomposing agentic reasoning into three systems: simulative reasoning (System II) for deliberation via world model, self-regulation (System III) deciding when/how deeply to plan, and reactive execution (System I). SR²AM uses LLM as world model with learned configurator. v1.0-30B achieves Pass@1 competitive with 685B–1T parameter systems while using 25.8–95.3% fewer reasoning tokens. RL increases average planning horizon by 22.8% while planning frequency grows only 2.0%, showing it learns to plan further ahead rather than more often.

### 2. Generative Recursive Reasoning (GRAM)

**Authors:** Junyeob Baek, Mingyu Jo, Minsu Kim, Mengye Ren, Yoshua Bengio, Sungjin Ahn

**Institution:** Université de Montréal, Mila

**arXiv:** [2605.19376](https://arxiv.org/abs/2605.19376) | Submitted May 19, 2026

Introduces Generative Recursive reAsoning Models — turns recursive latent reasoning into probabilistic multi-trajectory computation. Models reasoning as a stochastic latent trajectory, enabling multiple hypotheses and inference-time scaling through both recursive depth and parallel trajectory sampling. Supports conditional reasoning p(y|x) and unconditional generation p(x). Trained with amortized variational inference, GRAM improves over deterministic baselines on structured reasoning and multi-solution constraint satisfaction tasks.

### 3. Language Models Fail at Extended Rule Following

**Authors:** Tianxiang Dai, Jonathan Fan

**Institution:** Stanford University

**arXiv:** [2605.02028](https://arxiv.org/abs/2605.02028) | Submitted May 3, 2026

Evaluates 126 leading model variants on counting repeated characters — all fail above a model-dependent, syntax-sensitive counting capacity threshold. Failures are abrupt and persist even with increasing model size, inference time compute, and external tools. Mechanistic probing reveals models use a finite number of internal states to mimic counting as a rule and fail once these states are exhausted. Argues fundamentally new architectures are needed for truly reliable rule following.

### 4. Mu-GRPO: How Off-Policy Can GRPO Be?

**Authors:** Minghao Tian, Yunfei Xie, Chen Wei

**arXiv:** [2605.17570](https://arxiv.org/abs/2605.17570) | Submitted May 17, 2026

Shows GRPO-style algorithms tolerate substantially larger rollout staleness than assumed. Mu-GRPO organizes training into large sequential generation-optimization stages, combining relaxed clipping with negative-advantage veto. Across five language models and multiple math reasoning benchmarks, matches or exceeds standard GRPO while achieving ~2x speedup in wall-clock training time.

### 5. Agentic Code Reasoning

**Authors:** Shubham Ugare, Satish Chandra

**Institution:** Meta

**arXiv:** [2603.01896](https://arxiv.org/abs/2603.01896) | Submitted Mar 2, 2026

Introduces semi-formal reasoning — structured prompting requiring agents to construct explicit premises, trace execution paths, and derive formal conclusions. For patch equivalence, accuracy improves from 78% to 88% on curated examples and reaches 93% on real-world agent-generated patches. For code QA on RubberDuckBench, achieves 87% accuracy. Demonstrates structured agentic reasoning enables semantic code analysis without execution, opening applications in RL training pipelines.

---

## 📊 CTR / Recommendation / Advertising

### 6. GenLI: Generative Long-term User Interest Modeling for CTR Prediction

**Authors:** Jiangli Shao, Kaifu Zheng, Hao Fang, Huimu Ye, Zhiwei Liu, Bo Zhang, Shu Han, Xingxing Wang

**arXiv:** [2605.15905](https://arxiv.org/abs/2605.15905) | Submitted May 15, 2026

Addresses limitations of target-centered GSU in two-stage CTR frameworks. GenLI's interest generation module generates multiple target-independent interest distributions incorporating interaction information among behaviors. Behavior retrieval module selects related behaviors via simple lookup (O(1) complexity). Interest fusion module uses gating mechanisms. Improves diversity of user interests while avoiding complex matching-based behavioral retrieval.

### 7. CTR-Driven Advertising Image Generation with Multimodal Large Language Models

**Authors:** (from arXiv:2502.06823)

**arXiv:** [2502.06823](https://arxiv.org/abs/2502.06823)

Proposes using MLLMs for vision-based CTR prediction and advertising image generation. Instruction function integrates diverse product attributes into semantically rich descriptions. CTR-Driven Preference Optimization fine-tunes prompt model using DPO + PCPO loss. Reward model trained on user feedback data optimizes alignment between generated advertising images and online user preferences.

### 8. CADET: Context-Conditioned Ads CTR Prediction With Decoder-Only Transformer

**Authors:** David Pardoe, Neil Daftary, et al. (20+ authors)

**Institution:** LinkedIn

**arXiv:** [2602.08467](https://arxiv.org/abs/2602.08467) | Published Feb 11, 2026

Presents CADET — an end-to-end decoder-only transformer for ads CTR prediction. Successfully deployed on LinkedIn's advertising platform. Replaces traditional two-stage feature-interaction architectures with a unified transformer, demonstrating production feasibility of decoder-only models for ad ranking.

---

## 🎮 Games & Multi-Agent Systems

### 9. MARLIN: Multi-Agent Game-Theoretic RL for Sustainable LLM Inference

**Authors:** H. Moore, S. Qi, D. Milojicic, C. Bash, S. Pasricha

**arXiv:** [2605.13496](https://arxiv.org/abs/2605.13496) | Submitted May 13, 2026

Multi-agent game-theoretic RL framework to co-optimize TTFT, carbon emissions, water usage, and energy costs for LLM inference in cloud datacenters. Reduces TTFT by 18%, carbon emissions by 33%, water usage by 43%, and energy costs by 11% compared to state-of-the-art frameworks.

### 10. Causal RL for Complex Card Games: MTG-Causal-RL Benchmark

**Authors:** Cristiano da Costa Cunha, Ajmal Mian, Tim French, Wei Liu

**Institution:** University of Western Australia

**arXiv:** [2605.06066](https://arxiv.org/abs/2605.06066) | Submitted May 7, 2026

Gymnasium benchmark built on Magic: The Gathering with 3,077-dimensional partial observation, 478-action masked discrete action space, five competitive archetypes, and hand-specified Structural Causal Model. Exposes causal variables, SCM-predicted intervention effects, and per-factor credit traces. Proposes CGFA-PPO reference agent using SCM parents of win probability as factor-aligned critic targets.

### 11. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent RL

**Authors:** (ICLR 2026 Poster)

**Venue:** ICLR 2026

Self-play framework where models learn by playing multi-turn, zero-sum language games against continuously improving versions of themselves. Generates automatic curriculum of stronger opponents, eliminating need for human supervision. Implements fully online, multi-turn, multi-agent RL system for LLMs with role-conditioned advantage estimation. Improves mathematical and general reasoning benchmarks by up to 10% without domain-specific training data.

### 12. On the Geometry of Games and their Solvers

**Authors:** Yaqi Sun, Julian Ma, David Mguni

**arXiv:** [2605.29919](https://arxiv.org/abs/2605.29919) | Submitted May 29, 2026

Studies the geometric structure of game-theoretic solution concepts and their solvers, providing theoretical insights into multi-agent optimization dynamics.

---

## 📈 Sequential Modeling & Time Series

### 13. ALoRa-T: Low Rank Transformer for Multivariate Time Series Anomaly Detection

**Authors:** Charalampos Shimillas, Kleanthis Malialis, Konstantinos Fokianos, Marios M. Polycarpou

**Institution:** University of Cyprus

**arXiv:** [2602.08467](https://arxiv.org/abs/2602.08467) | Submitted Feb 9, 2026

Reveals connections between Transformer learning and statistical time series methods. Proposes Attention Low-Rank Transformer applying low-rank regularization to self-attention, plus ALoRa-Loc for anomaly localization via quantifying interrelationships among time series. Significantly outperforms SOTA in both detection and localization tasks.

### 14. Tiny but Trusted: Vision-Language Reasoning for Time-Series Anomaly Detection

**Authors:** Xiaona Zhou, Muntasir Wahed, Tianjiao Yu, Constantin Brif, Ismini Lourentzou

**arXiv:** [2605.30344](https://arxiv.org/abs/2605.30344) | Submitted May 29, 2026

Lightweight vision-language model for time-series anomaly detection, demonstrating that small multimodal models can achieve reliable performance while maintaining trustworthiness.

---

## 🛠️ LLM Training & Optimization

### 15. Efficient Test-Time Finetuning of LLMs via Convex Reconstruction and Gradient Caching

**Authors:** Alaa Khamis, Alaa Maalouf

**arXiv:** [2605.30337](https://arxiv.org/abs/2605.30337) | Submitted May 29, 2026

Novel test-time finetuning approach using convex reconstruction and gradient caching to improve LLM performance on specific tasks without full retraining.

### 16. Demystifying Data Organization for Enhanced LLM Training

**Authors:** (ACL 2026 Main Conference)

**arXiv:** [2605.30334](https://arxiv.org/abs/2605.30334) | Submitted May 29, 2026

ACL 2026 paper investigating how data organization strategies impact LLM training efficiency and final model quality.

### 17. MIRA: Mid-training Rubric Anchoring for Source-Aware Data Selection

**Authors:** (from arXiv listing)

**arXiv:** [2605.30288](https://arxiv.org/abs/2605.30288) | Submitted May 29, 2026

Introduces mid-training rubric anchoring for source-aware data selection, improving data efficiency during LLM training.

---

## 🤖 Agent Benchmarks & Evaluation

### 18. DSGBench: Strategic Game Benchmark for LLM Agents

**Authors:** (arXiv:2503.06047, revised May 9, 2026)

Evaluates LLM-based agents across six complex strategic games (StarCraft II, Civilization, Street Fighter III, etc.) with five evaluation dimensions and automated decision-tracking. Reports evaluations of six popular LLM agents (open-source and closed-source). Listed in ICASSP 2026 workshops.

### 19. Redundant or Necessary? A Benchmark for Detecting Redundant Steps in Agent Trajectories

**Authors:** Minyang Hu, Bo Yang, Zhinuo Zhou, Jiachen Liang, Guo Jiahao, Yiyang Yin et al.

**arXiv:** [2605.29893](https://arxiv.org/abs/2605.29893) | Submitted May 29, 2026

Proposes a benchmark for evaluating whether agent trajectory steps are necessary or redundant, addressing efficiency concerns in agentic systems.

### 20. Does The Way You Plan Matter? Planning Representations for LLM Web Agents

**Authors:** Alejandra Zambrano, Sara Vera Marjanovic, Imene Kerboua, Xing Han Lù, Leila Kosseim

**arXiv:** [2605.29927](https://arxiv.org/abs/2605.29927) | Submitted May 29, 2026

Introduces PlanAhead, a static planner-executor framework evaluating impact of plan representation on agent performance. Automatically categorizes WebArena tasks into 3 difficulty levels. Extended version submitted to EMNLP.

---

## 🔬 Multimodal & Cross-Modal

### 21. Safety Geometry Collapse in Multimodal LLMs and Adaptive Drift Correction

**Authors:** (from arXiv TLDR weekly)

Identifies "Safety Geometry Collapse" in MLLMs, where multimodal inputs degrade safety by compressing refusal directions. Shows modality-induced drift causally leads to this collapse. Introduces ReGap — a training-free, inference-time method that adaptively corrects modality drift.

### 22. Text Knows What, Tables Know When: Clinical Timeline Reconstruction via Retrieval-Augmented Multimodal Alignment

**Authors:** (from arXiv TLDR weekly)

Retrieval-augmented multimodal framework combining text narratives ("what") and structured EHR data ("when") for clinical timeline reconstruction. Formulates as graph-based multistep process with external calibration.

---

## 🎯 Key Themes

1. **Agent self-regulation**: SR²AM and GRAM both address the question of *when* and *how much* to plan — moving beyond uniform chain-of-thought toward adaptive computation budgets.

2. **LLM count/capacity limits**: Stanford's counting paper (2605.02028) reveals fundamental limitations in LLMs' ability to maintain exact state — implications for all agentic tasks requiring reliable procedural execution.

3. **Generative CTR modeling**: GenLI (2605.15905) and CADET (LinkedIn) both push toward more expressive CTR models — generative interest modeling and decoder-only transformers, respectively.

4. **Game-theoretic RL maturing**: MARLIN, MTG-Causal-RL, and SPIRAL show game theory moving from theoretical to practical — applied to LLM inference sustainability, causal credit assignment in card games, and self-play reasoning improvement.

5. **Off-policy GRPO viable**: Mu-GRPO demonstrates that GRPO can tolerate much more staleness than assumed, with 2x training speedup — important for scaling RL for LLMs.

6. **Safety geometry collapse**: ReGap identifies that multimodal inputs degrade safety in MLLMs by compressing refusal directions — a novel failure mode with practical implications.

7. **Sequential modeling + LLMs converge**: Time-series anomaly detection (ALoRa-T, Tiny but Trusted) increasingly borrows from Transformer/LLM architectures, while CTR papers adopt LLM-based supervision and generative modeling.
