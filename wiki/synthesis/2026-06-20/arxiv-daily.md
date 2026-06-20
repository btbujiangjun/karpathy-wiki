---
title: "arXiv Daily — 2026-06-20"
type: synthesis
created: 2026-06-20
updated: 2026-06-20
sources: []
tags: [arxiv-daily, llm, recommendation, ctr, games, sequential-modeling, agents]
---

# arXiv Daily Report — 2026-06-20

> Recent papers in AI, LLMs, recommendation, advertising, CTR, sequential modeling, games, and agents. Covers submissions from ~Jun 15–19, 2026.

---

## LLM Architecture & Training

### 1. Variable-Width Transformers
- **Authors**: Zhaofeng Wu, Oliver Sieberling, Shawn Tan, Rameswar Panda, Yury Polyanskiy, Yoon Kim
- **Institution**: MIT, MIT-IBM Watson AI Lab
- **arXiv**: [2606.18246](https://arxiv.org/abs/2606.18246) (Jun 16, 2026)
- **Key Innovation**: Proposes ><former, a ×‑shaped architecture with wider early/late layers and narrower middle layers using a parameter-free residual resizing mechanism. Achieves 22% FLOP reduction and 15% KV cache savings at matched parameter counts (200M–3B).
- **Abstract**: Challenges the constant-width assumption in Transformers. Nonuniform width allocation outperforms parameter-matched uniform baselines on language modeling loss, and the bottleneck structure produces qualitatively different residual-stream representations.

### 2. Toward Calibrated Mixture-of-Experts Under Distribution Shift
- **Authors**: Gina Wong, Drew Prinster, Suchi Saria, Rama Chellappa, Anqi Liu
- **Institution**: Johns Hopkins University
- **arXiv**: [2606.20544](https://arxiv.org/abs/2606.20544) (Jun 18, 2026)
- **Conference**: ICML 2026
- **Key Innovation**: Proves expert calibration is sufficient for hard-routed MoE under distribution shift but insufficient for soft-routed. Introduces adversarial reweighting that penalizes calibration errors of the routed aggregate.
- **Abstract**: Studies how routing mechanisms interact with expert-level calibration under distribution shift, improving the accuracy-calibration tradeoff across model classes and tasks.

### 3. Rethinking the Role of Efficient Attention in Hybrid Architectures
- **Authors**: (various)
- **Institution**: —
- **arXiv**: (Jun 18, 2026 — featured on DeepPaper weekly)
- **Key Innovation**: Systematic analysis of hybrid architectures combining full attention with sliding-window attention (SWA) and recurrent sequence mixers. Finds efficient-attention design primarily affects how fast long-context capability emerges.
- **Abstract**: Analyzes scaling behavior, mechanism, and architecture design across hybrid models, showing efficient modules shape model capabilities in distinct ways.

### 4. OPUS: Towards Efficient and Principled Data Selection in LLM Pre-training
- **Authors**: (various)
- **Institution**: —
- **arXiv**: [2602.05400](https://arxiv.org/abs/2602.05400) (Feb 2026, updated)
- **Key Innovation**: Optimizer-induced Projected Utility Selection (OPUS) — dynamic data selection in the optimizer-induced update space. Outperforms full 200B-token training with only 30B tokens for GPT-2 Large/XL.
- **Abstract**: Defines utility in the optimizer update space using Ghost technique + CountSketch for efficiency. Achieves remarkable data efficiency gains in both pre-training and continued pre-training.

---

## Recommendation, CTR & Advertising

### 5. CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors**: Ruoyan Wang et al.
- **Institution**: LinkedIn
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410) (Feb 11, 2026)
- **Key Innovation**: End-to-end decoder-only transformer for ads CTR. Introduces context-conditioned decoding with multi-tower heads, self-gated attention, timestamp-based RoPE, and session masking for train-serve skew.
- **Abstract**: Achieves 11.04% CTR lift vs. production LiRank (DCNv2 + sequential encoder hybrid). Deployed on LinkedIn's main sponsored feed traffic.

### 6. Fine-Tuned LLM as a Complementary Predictor Improving Ads System
- **Authors**: Hui Yang et al.
- **Institution**: (large-scale production ads platform)
- **arXiv**: [2605.27856](https://arxiv.org/abs/2605.27856) (May 27, 2026)
- **Key Innovation**: Uses a fine-tuned open-source LLM not as a ranker but as an ancillary predictor that forecasts likely advertisers from user profiles, augmenting conventional candidate generation.
- **Abstract**: Complementary paradigm for ads — LLM-driven advertiser prediction provides informative priors to downstream ranking, with measurable online business impact.

### 7. Structuring and Tokenizing Distributed User Interest Context for Generative Recommendation
- **Authors**: Hong Li, Hong Yan, Hanqing Zeng
- **Institution**: —
- **arXiv**: (Jun 18, 2026)
- **Key Innovation**: Structures distributed user interest context into tokenized sequences for generative recommendation, aiming to predict users' next interactions from historical behaviors.
- **Abstract**: Addresses the core challenge of how to represent and tokenize user interest context for autoregressive next-item prediction.

### 8. One Sequential Recommendation Model Pretrained from Synthetic Priors Predicts Multiple Datasets
- **Authors**: Woosung Kang, Jiwon Jeong, Jonghyeok Shin, Jeongwhan Choi, Noseong Park
- **Institution**: —
- **arXiv**: [2606.15752](https://arxiv.org/abs/2606.15752)
- **Conference**: KDD 2026
- **Key Innovation**: A single sequential recommendation model pretrained on synthetic priors that generalizes across multiple real-world datasets without dataset-specific fine-tuning.
- **Abstract**: Demonstrates that synthetic pre-training can produce a universal sequential recommender transferable to diverse domains.

### 9. Unified Value Alignment for Generative Recommendation in Industrial Advertising
- **Authors**: (various)
- **Institution**: Tencent
- **arXiv**: [2605.05803](https://arxiv.org/abs/2605.05803) (May 7, 2026)
- **Key Innovation**: Aligns generative recommendation models with business values (CTR, revenue, user experience) in industrial advertising settings. Reformulates recommendation as next-token generation with multi-objective alignment.
- **Abstract**: Shows GR can be effectively aligned to multiple business metrics in production.

### 10. FEDIN: Frequency-Enhanced Deep Interest Network for CTR Prediction
- **Authors**: (various)
- **Institution**: Tencent
- **arXiv**: [2605.01726](https://arxiv.org/abs/2605.01726) (May 3, 2026)
- **Key Innovation**: Enhances DIN with frequency-domain analysis to capture latent periodic patterns in user interests, addressing noise in time-domain behavioral data.
- **Abstract**: Sequential recommendation models often struggle with periodic patterns; FEDIN uses spectral methods to extract frequency features.

---

## Sequential Modeling & Decision Transformers

### 11. Beyond Autoregressive RTG: Conditioning via Injection Outside Sequential Modeling in Decision Transformer
- **Authors**: Yongyi Wang, Hanyu Liu, Lingfeng Li et al.
- **Institution**: —
- **arXiv**: [2605.06104](https://arxiv.org/abs/2605.06104) (May 7, 2026)
- **Key Innovation**: SlimDT removes Return-to-Go tokens from the autoregressive sequence, injecting RTG into state representations before sequential modeling. Reduces sequence length by 1/3, improving inference efficiency.
- **Abstract**: Decouples the sparse conditioning signal from the information-rich sequence, achieving both computational gains and higher task performance on D4RL.

### 12. Action-Aware Generative Sequence Modeling for Short Video Recommendation
- **Authors**: (various)
- **Institution**: Kuaishou
- **arXiv**: [2604.25834](https://arxiv.org/abs/2604.25834) (Apr 28, 2026)
- **Key Innovation**: Models user actions (watch time, skip, like, share) as part of the generative sequence, not just item IDs. Improves next-action prediction in short-video feeds.
- **Abstract**: Extends generative sequence models to incorporate heterogeneous action types for better user modeling.

---

## Games & Reinforcement Learning

### 13. Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **Authors**: Yidong He, Yutao Lai, Pengxu Yang, Jiarui Gan, Jiexin Wang, Yi Cai, Mengchen Zhao
- **Institution**: —
- **arXiv**: [2605.04906](https://arxiv.org/abs/2605.04906) (May 6, 2026, updated May 25)
- **Key Innovation**: Novel RL framework with recursive reasoning (agent reasons about other agents' reasoning), centralized CoT comparison module for intermediate rewards, and group-relative RL optimization.
- **Abstract**: Achieves 22.1% average performance improvement across various multi-agent games by improving LLMs' strategic reasoning ability.

### 14. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: (various)
- **Institution**: —
- **arXiv**: [2506.24119](https://arxiv.org/abs/2506.24119) (Jun 2025, revised Mar 2026)
- **Key Innovation**: Self-play framework where LLMs learn by playing multi-turn zero-sum games against continuously improving versions of themselves. Proposes role-conditioned advantage estimation (RAE) for multi-agent training stability.
- **Abstract**: Improves reasoning by up to 10% across 8 benchmarks on Qwen and Llama families, outperforming SFT on 25K expert trajectories. Multi-game training (TicTacToe, Kuhn Poker, Negotiation) yields strongest results.

### 15. MindGames Arena Generalization Track: In2AI Solution
- **Authors**: Aliaksei Korshuk, Alexander Buyantuev, Ilya Makarov
- **Institution**: —
- **arXiv**: [2606.00017](https://arxiv.org/abs/2606.00017) (Jun 2026)
- **Conference**: NeurIPS 2025 Competition (1st place)
- **Key Innovation**: Delayed per-step reward attribution method for generalizing game-playing agents across unseen game variations.
- **Abstract**: Technical report on the winning solution for the MindGames Arena Generalization Track.

---

## LLM Agents & Tool Use

### 16. LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents
- **Authors**: Md Nayem Uddin, Amir Saeidi et al.
- **Institution**: —
- **arXiv**: [2606.20529](https://arxiv.org/abs/2606.20529) (Jun 18, 2026)
- **Key Innovation**: Introduces a structured "ledger" state that tracks tool-calling context and policy compliance, enabling agents to adhere to organizational policies during tool use.
- **Abstract**: Addresses the challenge of maintaining policy adherence in multi-tool agentic workflows.

### 17. SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model
- **Authors**: (various)
- **Institution**: —
- **arXiv**: (Jun 2026 — featured on ArXiv TLDR)
- **Key Innovation**: New benchmark using a human-curated symbolic world model (kitchen domain) to detect "latent failures" in LLM-generated plans. Finds up to 56% of LLM plans contain latent failures.
- **Abstract**: Identifies and mitigates latent failures in LLM planning for autonomous agents before they cause irreversible consequences.

### 18. On Effectiveness and Efficiency of Agentic Tool-calling and RL Training
- **Authors**: Tong Liu, Cheng Qian, Matej Cief et al.
- **Institution**: —
- **arXiv**: [2606.00135](https://arxiv.org/abs/2606.00135)
- **Conference**: ICML 2026
- **Key Innovation**: Systematic study of how RL training improves tool-calling agent effectiveness, exploring the trade-offs between training efficiency and task performance.
- **Abstract**: Analyzes the interplay between RL training strategies and tool-calling capabilities in LLM agents.

---

## Methodology & Benchmarks

### 19. ForecastBench-Sim: A Simulated-World Forecasting Benchmark
- **Authors**: Jaeho Lee, Nick Merrill, Ezra Karger
- **Institution**: —
- **arXiv**: [2606.18686](https://arxiv.org/abs/2606.18686) (Jun 2026)
- **Conference**: ICML 2026 Workshop (Spotlight)
- **Key Innovation**: Simulated-world environment for evaluating LLM forecasting capabilities with controlled causal structure and ground-truth outcomes.
- **Abstract**: Provides a benchmark for measuring how well models can forecast in environments where the data-generating process is known.

### 20. The Deterministic Horizon: When Extended Reasoning Fails and Tool Delegation Becomes Necessary
- **Authors**: Dongxin Guo, Jikun Wu, Siu Ming Yiu
- **Institution**: —
- **arXiv**: [2606.00376](https://arxiv.org/abs/2606.00376)
- **Conference**: ICML 2026
- **Key Innovation**: Formalizes the "deterministic horizon" concept — tasks where additional reasoning steps cease to improve accuracy, and tool delegation is provably necessary.
- **Abstract**: Characterizes the boundary where extended test-time compute stops helping and external tool use becomes required.

---

## Summary

| Area | Count | Notable Trends |
|------|-------|----------------|
| LLM Architecture | 4 | Variable-width transformers, MoE calibration, efficient attention, data selection |
| CTR / Ads | 4 | Decoder-only CTR models, LLM-as-ancillary-predictor, generative recommendation alignment |
| Recommendation | 2 | Generative rec tokenization, synthetic pretrained sequential models |
| Sequential / DT | 2 | SlimDT, action-aware generative modeling |
| Games & RL | 3 | Self-play reasoning, strategic multi-agent RL, competition solutions |
| Agents & Tools | 3 | Policy-adherent tool-calling, latent failure benchmarking, RL for tool use |
| Benchmarks | 2 | Forecasting, reasoning horizon |

**Key themes**: (1) Shift toward generative/decoder-only architectures in CTR and recommendations. (2) Self-play and game-based training for reasoning improvement. (3) Growing focus on calibration, alignment, and safety in deployment. (4) Variable-width and hybrid architectures for efficiency. (5) LLMs being used as complementary/ancillary components rather than replacing entire systems.
