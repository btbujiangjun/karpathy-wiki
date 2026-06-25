---
title: "arXiv AI Research Search — June 2026"
type: synthesis
created: 2026-06-25
updated: 2026-06-25
sources: []
tags: [arxiv, survey, llm, recommendation, ctr, games, reinforcement-learning, world-models, agents]
---

# arXiv AI Research Search — June 2026

A curated collection of recent arXiv papers across AI, LLMs, recommendation systems, advertising/CTR, sequential modeling, games, and reinforcement learning.

---

## Large Language Models & Agents

### 1. Your Mouse and Eyes Secretly Leak Your Preference: LLM Alignment using Implicit Feedback from Users
- **Authors:** Haw-Shiuan Chang, Jeffrey Gomez, Mehul Patwari, Aryan Sajith, Hamed Zamani
- **Institution:** University of Massachusetts Amherst (Zamani group)
- **Date:** Jun 18, 2026 | **arXiv:** [2606.20482](https://arxiv.org/abs/2606.20482)
- **Abstract:** Collects 1,336 multi-turn questions from 59 MTurk workers with mouse trajectories and eye-gaze data. Shows implicit feedback boosts text-based reward model accuracy from 55% to 64% and nearly triples relative DPO improvement across 8 LLMs.
- **Key Innovations:** IFLLM dataset (first to pair webcam eye-tracking + mouse traces with LLM preferences); reward model fusing implicit behavioral signals; demonstrates economic value of implicit feedback for alignment.

### 2. StylisticBias: A Few Human Visual Cues Drive Most Social Biases in MLLMs
- **Authors:** Shaghayegh Kolli, Timo Cavelius, Nafiseh Nikeghbal, Samantha Dalal, Jana Diesner
- **Institution:** University of Illinois Urbana-Champaign (Diesner lab)
- **Date:** Jun 18, 2026 | **arXiv:** [2606.20527](https://arxiv.org/abs/2606.20527)
- **Abstract:** Generates 500 photorealistic base faces with ~50 single-attribute variations (~25K images). Evaluates 6 MLLMs across 25 social judgment scenarios. Finds ~15 attributes account for ~80% of bias variation.
- **Key Innovations:** Controlled benchmark isolating attribute-level bias from identity effects; age and body type dominate identity-level effects; fashion/style drive largest attribute-level shifts. Accepted at ICML 2026 workshops.

### 3. On Effectiveness and Efficiency of Agentic Tool-calling and RL Training
- **Authors:** Tong Liu, Cheng Qian, Matej Cief, Yuan He, Daniele Dan, Nikolaos Aletras, Gabriella Kazai
- **Institution:** Yahoo Research / University of Sheffield
- **Date:** May 28, 2026 | **arXiv:** [2606.00135](https://arxiv.org/abs/2606.00135)
- **Abstract:** Shows tool-calling evaluation is highly sensitive to implementation choices (seed, prompt, template). Identifies two sources of RL training waste: uninformative rollouts and high-cost policy updates. Proposes acceleration techniques.
- **Key Innovations:** Systematic sensitivity analysis of tool-calling pipelines; two efficiency techniques for RL-based tool-calling training. Accepted at ICML 2026.

### 4. World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications
- **Authors:** Arif Hassan Zidan et al. (26 authors)
- **Institution:** University of Georgia, multi-institutional
- **Date:** May 28, 2026 | **arXiv:** [2606.00133](https://arxiv.org/abs/2606.00133)
- **Abstract:** Multi-axis taxonomy across architecture, methodology, reasoning strategy, and application domain. Covers PlaNet, Dreamer family, MuZero, Sora, Cosmos, Genie. Traces chain-of-thought convergence with world-model imagination.
- **Key Innovations:** Unified framework integrating diverse world model families; identifies compounding prediction errors, sim-to-real transfer, and fragmented evaluation as persistent challenges.

---

## Recommendation, Advertising & CTR

### 5. Dual-Stream MLP is All You Need for CTR Prediction
- **Authors:** Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution:** Renmin University of China (RUCAIBox)
- **Date:** Jun 3, 2026 | **arXiv:** [2606.04944](https://arxiv.org/abs/2606.04944)
- **Abstract:** Proposes DS-MLP using knowledge distillation to consolidate explicit feature interaction learning into a main MLP while a parallel MLP captures implicit interactions. Achieves SOTA across three benchmarks.
- **Key Innovations:** Vanilla MLP structure matches/exceeds complex dual-stream architectures; two alignment strategies for dual-MLP compatibility. Accepted at TKDD.

### 6. IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs
- **Authors:** Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan, Ruiyan Han, Feiyang Xiao, Yanhua Huang, Li Lin, Yang Luo, Yao Hu
- **Institution:** Xiaohongshu Inc. / Apple (Salha-Galvan)
- **Date:** Mar 2, 2026 | **arXiv:** [2603.01590](https://arxiv.org/abs/2603.01590)
- **Abstract:** Leverages MLLMs to generate proxy embeddings from content signals for cold-start items. Proxies aligned with existing ID embedding space, optimized end-to-end under CTR objectives. Deployed on Xiaohongshu's Explore Feed serving hundreds of millions of users.
- **Key Innovations:** MLLM-based proxy embeddings replacing ID embeddings for cold-start; seamless integration into existing large-scale ranking pipelines; validated via online A/B tests.

### 7. Unified Value Alignment for Generative Recommendation in Industrial Advertising
- **Authors:** Xinxun Zhang et al. (16 authors)
- **Institution:** Tencent (WeChat Channels)
- **Date:** May 7, 2026 | **arXiv:** [2605.05803](https://arxiv.org/abs/2605.05803)
- **Abstract:** Proposes UniVA framework with Commercial SID tokenizer (value-injected item representations), Generation-as-Ranking SID Decoder with eCPM-aware RL, and value-guided personalized beam search. Achieves 37% offline HitRate@100 improvement and 1.5% GMV lift online.
- **Key Innovations:** First framework to explicitly align commercial value in generative recommendation for advertising; fuses value scores into next-item generation in one decoding process.

### 8. Token Factory: Efficiently Integrating Diverse Signals into Large Recommendation Models
- **Authors:** Xilun Chen, Shao-Chuan Wang, Baykal Cakici, Lukasz Heldt, Lichan Hong, Raghu Keshavan, Aniruddh Nath, Li Wei, Xinyang Yi
- **Institution:** Google (likely)
- **Date:** Jun 17, 2026 | **arXiv:** [2606.19635](https://arxiv.org/abs/2606.19635)
- **Abstract:** Transforms traditional recommendation signals into "soft tokens" for LRMs, enabling efficient integration and compression of heterogeneous features without prompt length explosion.
- **Key Innovations:** Soft token approach for signal integration into Transformer-based LRMs; demonstrated in production-scale recommendation environment.

---

## Games, Reinforcement Learning & Sequential Modeling

### 9. MindGames Arena Generalization Track: In2AI Solution with Delayed Per-Step Reward Attribution
- **Authors:** Aliaksei Korshuk, Alexander Buyantuev, Ilya Makarov
- **Institution:** In2AI / Independent
- **Date:** Apr 13, 2026 | **arXiv:** [2606.00017](https://arxiv.org/abs/2606.00017)
- **Abstract:** Introduces delayed per-step reward attribution with eligibility gating for multi-agent RL. An 8B open-source model matched/surpassed GPT-5 in head-to-head play. First place in both Open and Efficient tracks at NeurIPS 2025 MindGames Arena.
- **Key Innovations:** Episode lifecycle with end-of-episode reward backpropagation; asynchronous rollouts via vLLM continuous batching; curriculum opponent sampling; 8B model beats GPT-5 in strategic games.

### 10. Beyond Autoregressive RTG: Conditioning via Injection Outside Sequential Modeling in Decision Transformer
- **Authors:** Yongyi Wang, Hanyu Liu, Lingfeng Li, Bozhou Chen, Ang Li, Qirui Zheng, Xionghui Yang, Chucai Wang, Wenxin Li
- **Institution:** Multiple Chinese institutions
- **Date:** May 7, 2026 | **arXiv:** [2605.06104](https://arxiv.org/abs/2605.06104)
- **Abstract:** SlimDT removes Return-to-Go from the autoregressive sequence, injecting it into state representations instead. Reduces sequence length by 1/3, improving inference efficiency. Surpasses standard DT on D4RL.
- **Key Innovations:** Decouples sparse conditioning signal from information-rich sequence; demonstrates both computational gains and higher task performance.

### 11. Augmenting Game AI with Deep Reinforcement Learning
- **Authors:** Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén
- **Institution:** Embark Studios / Multiple
- **Date:** Jun 18, 2026 | **arXiv:** [2606.20210](https://arxiv.org/abs/2606.20210)
- **Abstract:** Vision paper on deploying player-facing RL agents in modern games. Proposes a training framework with requirements suited for game AI. Identifies bottlenecks and research directions for industry adoption.
- **Key Innovations:** Practical framework for game AI RL deployment; identifies hard problems limiting cross-genre adoption. Published at Conference on Games 2026.
