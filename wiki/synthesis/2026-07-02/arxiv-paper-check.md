---
title: "arXiv Paper Check — AI & CTR (July 2, 2026)"
type: synthesis
created: 2026-07-02
updated: 2026-07-02
sources: [arxiv-api]
tags: [arxiv, paper-check, ai, ctr, llm, rl, transformer, reasoning]
---

# arXiv Paper Check — AI & CTR (July 2, 2026)

> Sampled 30 new submissions from cs.AI / cs.IR / cs.LG (July 1, 2026). Curated 10 most interesting.

## AI / LLM Highlights

### 1. Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training
- **Authors**: Zijian Zhang, Rizhen Hu, Athanasios Glentis, Dawei Li, Chung-Yiu Yau, Hongzhou Lin, Mingyi Hong
- **Link**: [2607.01232](https://arxiv.org/abs/2607.01232)
- **Key contribution**: Systematic layer-wise study of RL post-training reveals RL gains are concentrated in a small subset of middle transformer layers. Training a single layer can recover most (sometimes all) of full-parameter RL gains across Qwen3/Qwen2.5, three RL algorithms (GRPO/GiGPO/Dr.GRPO). Layer rankings are stable across datasets, tasks, and model families.

### 2. AutoMem: Automated Learning of Memory as a Cognitive Skill
- **Authors**: Shengguang Wu, Hao Zhu, Yuhui Zhang, Xiaohan Wang, Serena Yeung-Levy
- **Link**: [2607.01224](https://arxiv.org/abs/2607.01224)
- **Key contribution**: Treats memory management as a trainable skill via a two-loop framework. First loop: strong LLM revises memory structure from agent trajectories. Second loop: good memory decisions used as training signal. Improves 32B open-weight model ~2-4x on long-horizon tasks (Crafter, MiniHack, NetHack), competitive with Claude Opus 4.5 and Gemini 3.1 Pro Thinking.

### 3. Theoria: Rewrite-Acceptability Verification over Informal Reasoning States
- **Authors**: Ben Slivinski, Michael Saldivar
- **Link**: [2607.01223](https://arxiv.org/abs/2607.01223)
- **Key contribution**: Verification architecture that rewrites candidate solutions into typed state transitions with explicit justifications. 91.4% strict precision on HLE-Verified Gold (185 problems), catches 94.7% of adversarial poisoned proofs vs 83.2% for holistic judging. Hidden premises: 90.6% vs 62.5%.

### 4. The State-Prediction Separation Hypothesis
- **Authors**: Giovanni Monea, Nathan Godey, Kianté Brantley, Yoav Artzi
- **Link**: [2607.01218](https://arxiv.org/abs/2607.01218)
- **Key contribution**: Proposes disentangling Transformer's next-token prediction and state-storage roles into two computation streams. Outperforms standard Transformers by 2-3pp on downstream tasks with better data/compute efficiency. Extensive confounder analysis.

### 5. Right in the Right Way: LM Training with Verifiable Rewards and Human Demonstrations
- **Authors**: Mehul Damani, Isha Puri, Idan Shenfeld, Jacob Andreas
- **Link**: [2607.01181](https://arxiv.org/abs/2607.01181)
- **Key contribution**: Adversarial generator-discriminator framework that augments RLVR with learned human-like style signal. Improves non-verifiable properties (edit distance, diversity) while preserving accuracy. Nearly eliminates reward hacking.

### 6. QuasiMoTTo: Quasi-Monte Carlo Test-Time Scaling
- **Authors**: Michael Y. Li, Anthony Zhan, Kanishk Gandhi, Noah D. Goodman, Emily B. Fox
- **Link**: [2607.01179](https://arxiv.org/abs/2607.01179)
- **Key contribution**: Uses quasi-Monte Carlo to generate correlated but exact samples for test-time compute scaling. Matches i.i.d. pass@k with 25-47% fewer samples. Also accelerates GRPO RL training by 50%.

### 7. Measuring the Gap Between Human and LLM Research Ideas
- **Authors**: Ziyu Chen, Yilun Zhao, Arman Cohan
- **Link**: [2607.01233](https://arxiv.org/abs/2607.01233)
- **Key contribution**: Builds evaluation framework comparing LLM vs human research ideas. LLM ideas clustered around bridge-like opportunities and synthesis methods; human ideas spread more broadly. Systematic taste gap persists across LLMs.

## CTR / IR Highlights

### 8. Diffusion-GR2: Diffusion Generative Reasoning Re-ranker
- **Authors**: Zhuoxuan Zhang, Kangqi Ni, Yuhang Chen, Mingfu Liang, Xiaohan Wei, Yunchen Pu, Fei Tian, Chonglin Sun, Frank Shyu, Adam Song, Sandeep Pandey, Luke Simon, Tianlong Chen, Xi Liu
- **Link**: [2607.01170](https://arxiv.org/abs/2607.01170)
- **Key contribution**: Converts autoregressive reasoning re-ranker into block-diffusion model for 2.4-3.5x decode throughput. Conversion fine-tuning + on-policy distillation + RL stage closes accuracy gap to near-parity with AR teacher. Validated on Amazon Beauty.

### 9. DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction
- **Authors**: Wenzhuo Cheng, Shipeng Nie, Qixin Guo, Xuefeng Sun, Jianguo Lou, Zhengwei Zheng
- **Link**: [2606.07980](https://arxiv.org/abs/2606.07980)
- **Key contribution**: Dual-path residual design (Identity + Block Attention Residual) with SiLU-gated cross-layer attention for CTR. Outperforms 12 baselines on 331M-interaction industrial dataset. 1.66x steeper compute-AUC scaling law — 8-layer DeRes matches 16-layer OneTrans.

### 10. Trie-based Experiment Plans for Efficient IR Pipeline Experiments
- **Authors**: Irene Anu, Craig Macdonald
- **Link**: [2607.01162](https://arxiv.org/abs/2607.01162)
- **Key contribution**: Trie-based experiment plan for cascading IR pipelines reduces repeated computation. 26% reduction in experiment duration on MSMARCO v2 with BM25+MonoT5+DuoT5. Accepted at ReNeuIR'26 @ SIGIR 2026.

## Key Themes
- **RL post-training efficiency**: Single/middle layers carry most RL gains — major implication for LoRA/adapter fine-tuning
- **Memory as a trainable skill**: AutoMem shows memory management is independently learnable, separate from task policy
- **Test-time compute scaling**: QMC correlated sampling beats i.i.d. at same compute budget
- **Verification architectures**: Theoria's structured proof verification outperforms holistic LLM judges, especially on hidden premises
- **Diffusion for ranking**: Block-diffusion re-rankers achieve near-AR quality at 2.4-3.5x speed
- **CTR residual design**: DeRes shows residual bottleneck is a key limiting factor in Transformer-based CTR models
