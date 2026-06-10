---
title: "arXiv Paper Check — AI & CTR (June 10, 2026)"
type: synthesis
created: 2026-06-10
updated: 2026-06-10
sources: [arxiv-api]
tags: [arxiv, ai, ctr, recommender-systems, llm, rl, survey]
---

# arXiv Paper Check — AI & CTR (June 10, 2026)

> Survey of recent submissions to cs.AI, cs.LG, cs.IR (Jun 9–10, 2026). 22 papers highlighted across AI/ML systems, LLM training/inference, agents, and CTR/Recommendation.

---

## AI / ML Systems & Theory

### [A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design](https://arxiv.org/abs/2606.11189)
- **Authors**: Tong Xie, Yuanhao Ban, Yunqi Hong, Sohyun An, Yihang Chen, Cho-Jui Hsieh
- **Key contribution**: Reinterprets SFT as target distribution design via the Q-target framework, unifying many SFT variants. Proposes Target-SFT which constructs the training objective directly from the desired target distribution, consistently outperforming across 10 reasoning dataset-model settings.

### [Piper: A Programmable Distributed Training System](https://arxiv.org/abs/2606.11169)
- **Authors**: Megan Frisella, Shubham Tiwari, Andy Ruan, Yi Pan, Parker Gustafson, Mat Jacob, Gilbert Bernstein, Stephanie Wang
- **Key contribution**: Decouples distributed training strategy from runtime implementation via a unified IR. Maintains parity with ZeRO while enabling advanced composed parallelism like DeepSeek-V3's DualPipe.

### [Unifying Local Communications and Local Updates for LLM Pretraining](https://arxiv.org/abs/2606.11081)
- **Authors**: Pietro Cagnasso, Eugene Belilovsky, Edouard Oyallon
- **Key contribution**: Communication-efficient pretraining for LLMs across lower-bandwidth links, reducing communication overhead during distributed training.

### [First-Order Trajectory Matching: Fast Ensemble Predictions of Chaotic, Turbulent, Stochastic Systems](https://arxiv.org/abs/2606.11138)
- **Authors**: Shreya Jha, Timo Schorlepp, Nicholas Geissler, Jules Berman, Benjamin Peherstorfer
- **Key contribution**: Surrogate modeling method that learns probability current velocity directly from trajectories, providing trajectory-aware ensemble predictions at low cost.

### [Algorithmic and Minimax Complexities in Kernel Bandits](https://arxiv.org/abs/2606.11171)
- **Authors**: Yunbei Xu
- **Key contribution**: Unifies GP-UCB and DEC methods under a common MAIR framework, showing algorithmic complexity can be more informative than class-wide minimax certificates in overparameterized models.

### [Flaws in the LLM Automation Narrative](https://arxiv.org/abs/2606.11166)
- **Authors**: George Perrett, Javae Elliott, Jennifer Hill, Marc Scott
- **Key contribution**: Critical study showing frontier LLMs underperform human experts on data analysis coding tasks with higher variance, questioning the narrative of LLM automation readiness.

### [What Fits (Into Few Tokens) Doesn't Overfit: Compression and Generalization in ML Research Agents](https://arxiv.org/abs/2606.11045)
- **Authors**: Martin Andres Bertran, Aaron Roth, Zhiwei Steven Wu
- **Key contribution**: Theoretically analyzes why adaptive benchmark reuse yields less overfitting than predicted — compression through limited token budget acts as a regularizer.

### [Overcoming Rank Collapse in Feedback Alignment](https://arxiv.org/abs/2606.11123)
- **Authors**: Gauthier Boeshertz, Razvan Pascanu, Claudia Clopath
- **Key contribution**: Identifies low-rank gradient dynamics as key obstacle to scaling Feedback Alignment; Muon optimizer and hidden activity normalization improve accuracy by 9pp on ResNet-18/CIFAR100.

---

## LLM Training, Inference & Reasoning

### [ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models](https://arxiv.org/abs/2606.11164)
- **Authors**: Wenhao Liu, Hao Shi, Yunhe Li, Weizhi Fei, Xiangyuan Wang, Mengzhe Ruan, Hanxu Hou, Peisong Wang, Linqi Song, Shuang Qiu
- **Key contribution**: Training-free KV cache compression with hierarchical budget allocation. Discovers "Reasoning Wave" pattern across layers. Plug-and-play with existing token-eviction policies.

### [Predicting Future Behaviors in Reasoning Models Enables Better Steering](https://arxiv.org/abs/2606.11172)
- **Authors**: Evgenii Kortukov, Piotr Komorowski, Florian Klein, Paula Engl, Gabriele Sarti, Seong Joon Oh, Sebastian Lapuschkin, Wojciech Samek
- **Key contribution**: Distinguishes detection vs prediction features in LRMs. Introduces Future Probe Controlled Generation (FPCG) — text-level steering with minimal output quality degradation.

### [The Role of Feedback Alignment in Self-Distillation](https://arxiv.org/abs/2606.11173)
- **Authors**: Semih Kara, Oğuzhan Ersoy
- **Key contribution**: ICML 2026 Workshop (RLxF). Step-aligned critique in self-distillation outperforms GRPO by 16.11 points. Shows structural alignment between feedback and solver reasoning is key.

### [EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents](https://arxiv.org/abs/2606.11182)
- **Authors**: Weixian Xu, Shilong Liu, Mengdi Wang
- **Key contribution**: First multi-dataset test-time prompt learning framework for LLM agents. Router-prompt co-evolution handles heterogeneous input streams. Improves multi-benchmark scores by 10.38 points over Qwen3-4B and 24.32 over DeepSeek-V3.2.

### [TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning](https://arxiv.org/abs/2606.11119)
- **Authors**: Heming Zou, Qi Wang, Yun Qu et al.
- **Key contribution**: Optimizes rollout budget allocation for RLVR training, improving sample efficiency in agentic RL.

### [Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation](https://arxiv.org/abs/2606.11127)
- **Authors**: Soham Bhattacharjee, Karun Sharma, Vinay Kumar Sankarapu, Pratinav Seth
- **Key contribution**: Controlled study of source-provenance filtering vs. adaptive recovery in synthetic data pipelines. Finds hallucination and reward gates reject disjoint samples — both needed. Downstream quality driven primarily by generator scale.

### [Itô maps for any-step SDEs](https://arxiv.org/abs/2606.11156)
- **Authors**: Zhengkai Pan, Peter Potaptchik, Wenxi Yao, Michael S. Albergo, Jakiw Pidstrigach
- **Key contribution**: Introduces Itô map — any-step stochastic flow map for SDEs. Enables exact distillation for stochastic dynamics and supports posterior sampling and steering.

---

## Agents & Benchmarks

### [ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity](https://arxiv.org/abs/2606.11150)
- **Authors**: Andrew Bo Liu, Samira Nedungadi, Bryce Cai, Alex Kleinman, Harmon Bhasin, Seth Donoughe
- **Key contribution**: ICML 2026. Evaluates LLM agents on wet-lab biology tasks. All tested agents outperformed median expert human baseliner. OpenAI o4-mini-high scripts successfully assembled DNA on OpenTrons robots.

### [τ-Rec: A Verifiable Benchmark for Agentic Recommender Systems](https://arxiv.org/abs/2606.10156)
- **Authors**: Bharath Sivaram Narasimhan, Karthik R Narasimhan
- **Key contribution**: Replaces subjective LLM-as-a-judge with verifiable rewards and reveal-tagged elicitation. Reveals steep reliability cliff: best model ~57% pass^1, ~38% pass^4. Tested across GPT-5.4, Claude Sonnet 4.6, Gemini 2.5 Flash, DeepSeek V4 Flash, Qwen3-32B.

### [T1-Bench: Benchmarking Multi-Scenario Agents in Real-World Domains](https://arxiv.org/abs/2606.11070)
- **Authors**: Genta Indra Winata, Amartya Chakraborty, Yuzhen Lin et al.
- **Key contribution**: Multi-scenario agent benchmark covering diverse real-world domains with tool-calling evaluation.

### [Superficial Beliefs in LLM Decision-Making](https://arxiv.org/abs/2606.11016)
- **Authors**: Gabriel Freedman, Francesca Toni
- **Key contribution**: Investigates whether LLMs genuinely reason or just imitate rationales in decision-making using synthetic binary choice tasks.

---

## CTR Prediction & Recommendation

### [Atomic Intent Reasoning (AIR): Bringing LLM Semantics to Industrial Cross-Domain Recommendations](https://arxiv.org/abs/2606.10357)
- **Authors**: Zhuohang Jiang, Yuxin Chen, Shijie Wang, Haohao Qu, Zhou Jindong, Wenqi Fan, Li Qing, Dongxu Liang, Jun Wang
- **Key contribution**: KDD 2026. Kuaishou E-commerce LLM-driven cross-domain recommendation framework. 400× inference acceleration via offline LLM migration + online retrieval. +3.446% GMV in production A/B test.

### [GenAIR: Generative Archetype-Grounded Item Representations for Sequential Recommendation](https://arxiv.org/abs/2606.11023)
- **Authors**: Yifan Li, Jiahong Liu, Xinni Zhang, Hao Chen, Yankai Chen, Wenhao Yu, Jianting Chen, Irwin King
- **Key contribution**: WWW 2026 Oral. Uses LLM to generate archetype descriptions of ideal target audiences, then behavioral calibration grounds them in real interaction patterns. Seamless integration with existing models.

### [Mult-DPO: Multinomial Direct Preference Optimization for Recommender Systems](https://arxiv.org/abs/2606.10078)
- **Authors**: Yaochen Zhu, Harald Steck, James McInerney, Aditya Sinha, Yinhan He, Nathan Kallus, Jundong Li
- **Key contribution**: Extends DPO from pairwise to set-wise preferences for LLM-based recommenders. Tractable multinomial surrogate loss with theoretical bound on PL DPO. Extends to multiple preference levels.

### [STORM: Stepwise Token Optimization with Reward-Guided Beam Search](https://arxiv.org/abs/2606.10621)
- **Authors**: Arthur Satouf, Giulio D'Erasmo, Yuxuan Zong, Habiboulaye Amadou Boubacar, Pablo Piantanida, Benjamin Piwowarski
- **Key contribution**: Self-supervised framework for lexical query expansion using retrieval metrics as token-level reward signal. 0.6B-8B models match LLM rewriters while retrieving as fast as BM25. Zero-shot to 18 languages.

### [Effective Reinforcement Learning for Agentic Search by Recycling Zero-Variance Queries](https://arxiv.org/abs/2606.10709)
- **Authors**: João Coelho, João Magalhães, Bruno Martins, Chenyan Xiong
- **Key contribution**: Query recycling for GRPO-style training — zero-variance queries are returned to a mutable pool for resampling as policy evolves. 1.7B model reaches 66.0 Pass@1 across 7 multi-hop QA benchmarks.

### [From Prompt to Purchase: How AI Brand Recommendations Move Consumers on the Open Web](https://arxiv.org/abs/2606.10907)
- **Authors**: Michael Iannelli, Alan Ai
- **Key contribution**: Causal measurement of brand mention effects in AI assistants. Brand names in assistant responses drive +4.3pp Google search increase. Pre-trend event study with stance classification and non-customer conditioning.

---

## Key Themes

1. **SFT Theory Unification** — Target-SFT Q-target framework unifies diverse SFT variants under a common distribution design lens.
2. **KV Cache Optimization** — ReasonAlloc discovers "Reasoning Wave" patterns for hierarchical budget allocation in reasoning models.
3. **LLM Agent Reliability** — ABC-Bench and τ-Rec both show frontier LLMs can match/exceed human experts in narrow domains but fail at consistency.
4. **CTR → LLM Convergence** — AIR (Kuaishou, +3.446% GMV), GenAIR (WWW'26 Oral), Mult-DPO show recommender systems increasingly adopting LLM architectures.
5. **Set-wise Preference Learning** — Mult-DPO extends DPO to the natural set-wise feedback setting in recommenders.
6. **Training Efficiency** — Piper, local communications unification, and query recycling all address the growing cost of LLM training and RL.
