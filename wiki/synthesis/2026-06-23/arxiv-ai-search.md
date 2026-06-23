---
title: arXiv AI Search — June 23, 2026
type: synthesis
created: 2026-06-23
updated: 2026-06-23
sources: [arxiv.md]
tags: [arxiv-search, llm, ctr, recommendation, reasoning, games, attention, reinforcement-learning]
---

# arXiv AI Search — June 23, 2026

> Cross-domain scan of recent arXiv preprints (Feb–Jun 2026) across CTR prediction, recommendation systems, sequence modeling attention mechanisms, LLM reasoning, and game-based RL.

---

## Click-Through Rate (CTR) Prediction

### 1. GRAB: An LLM-Inspired Sequence-First CTR Prediction Modeling Paradigm

| Field | Detail |
|-------|--------|
| Authors | Shaopeng Chen, Chuyue Xie, Huimin Ren, Shaozong Zhang, Han Zhang, Ruobing Cheng, Zhiqiang Cao, Zehao Ju, Yu Gao, Jie Ding, Xiaodong Chen, Xuewu Jiao, Shuanglong Li, Liu Lin |
| Affiliation | Baidu |
| Date | Feb 2, 2026 |
| Link | https://arxiv.org/abs/2602.01865 |
| **Innovation** | Proposes GRAB, an end-to-end generative framework for CTR replacing traditional DLRMs. Introduces Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics. Demonstrates monotonic scaling with longer sequences. |
| **Key Results** | +3.05% revenue, +3.49% CTR in full-scale Baidu online deployment. |

### 2. DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction

| Field | Detail |
|-------|--------|
| Authors | Wenzhuo Cheng, Shipeng Nie, Qixin Guo, Xuefeng Sun, Jianguo Lou, Zhengwei Zheng |
| Affiliation | — |
| Date | Jun 6, 2026 |
| Link | https://arxiv.org/abs/2606.07980 |
| **Innovation** | Dual-path residual design (Identity path + Block Attention Residual path) for CTR Transformers. Proposes Pointwise AttnRes replacing Softmax with SiLU for multi-interest patterns. |
| **Key Results** | Up to +0.32% AUC at <5% extra FLOPs. 2× compute saving at equivalent AUC vs OneTrans. Scaling law γ=0.118 vs 0.071. |

### 3. GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation

| Field | Detail |
|-------|--------|
| Authors | Yanyan Zou, Junbo Qi, Lunsong Huang, Yu Li, Kewei Xu, Jiabao Gao, Binglei Zhao, Xuanhua Yang, Sulong Xu, Shengjie Li |
| Affiliation | JD.com |
| Date | Apr 16, 2026 (SIGIR 2026) |
| Link | https://arxiv.org/abs/2604.14878 |
| **Innovation** | Single decoder-only generative retrieval. Page-wise NTP task, asymmetric linear Token Merger for 2× prompt compression, GRPO-SR with Hybrid Rewards for preference alignment. |
| **Key Results** | +9.5% clicks, +8.7% transactions in JD.com online A/B test. |

### 4. Generative Archetype-Grounded Item Representations for Sequential Recommendation (GenAIR)

| Field | Detail |
|-------|--------|
| Authors | Yifan Li, Jiahong Liu, Xinni Zhang, Hao Chen, Yankai Chen, Wenhao Yu, Jianting Chen, Irwin King |
| Affiliation | — |
| Date | Jun 9, 2026 (WWW 2026 Oral) |
| Link | https://arxiv.org/abs/2606.11023 |
| **Innovation** | LLM generates "Archetype" (ideal target audience profile) for each item. Behavioral calibration objective grounds semantic representations in real interaction patterns. |
| **Key Results** | Significant improvement over SOTA on 3 real-world datasets; plug-and-play with existing sequential models. |

### 5. Sample Is Feature (SIF): Beyond Item-Level, Toward Sample-Level Tokens for Unified Large Recommender Models

| Field | Detail |
|-------|--------|
| Authors | — |
| Affiliation | Food delivery platform (industrial) |
| Date | Apr 2026 |
| Link | https://arxiv.org/abs/2604.15650 |
| **Innovation** | Elevates sequence tokens from item-level to sample-level (item + context). Unified Transformer backbone for sequence + feature interaction. |
| **Key Results** | +2.03% CTR, +1.21% CVR in online A/B test. Outperforms HyFormer, OneTrans. |

### 6. Kunlun: Establishing Scaling Laws for Massive-Scale Recommendation Systems through Unified Architecture Design

| Field | Detail |
|-------|--------|
| Authors | Bojian Hou, Xiaolong Liu, Xiaoyi Liu, Jiaqi Xu, Yasmine Badr, Mengyue Hang, Sudhanshu Chanpuriya, Junqing Zhou, Yuhang Yang, Han Xu, Qiuling Suo, Laming Chen, Yuxi Hu, Jiasheng Zhang, Huaqing Xiong, Yuzhen Huang, Chao Chen, Yue Dong, Yi Yang, Shuo Chang, Xiaorui Gan, Wenlin Chen, Santanu Kolay, Darren Liu, Jade Nie, Chunzhi Yang, Ellie Wen, Jiyan Yang, Huayu Li |
| Affiliation | Meta Ads |
| Date | Feb 10, 2026 (updated Jun 5) |
| Link | https://arxiv.org/abs/2602.10016 |
| **Innovation** | Generalized Dot-Product Attention (GDPA), Hierarchical Seed Pooling (HSP), Sliding Window Attention. Computation Skip (CompSkip) and Event-level Personalization. |
| **Key Results** | MFU increased from 17% to 37% on NVIDIA B200. 2× scaling efficiency. Deployed in major Meta Ads models. |

### 7. Field-Aware Transformer (FAT): From Scaling to Structured Expressivity

| Field | Detail |
|-------|--------|
| Authors | Bencheng Yan, Yuejie Lei, Zhiyuan Zeng, Zheye Deng, Di Wang, Kaiyi Lin, Pengjie Wang, Chuan Yu, Jian Xu, Bo Zheng |
| Affiliation | Alibaba (likely) |
| Date | Nov 15, 2025 (updated May 31, 2026, KDD 2026) |
| Link | https://arxiv.org/abs/2511.12081 |
| **Innovation** | Field-Aware Tokenization, Field-Decomposed Attention, Basis-Composed Hypernetwork. Shifts complexity from vocabulary size n to field count F. Formal scaling law via Rademacher complexity. |
| **Key Results** | +4.38% AUC offline, +2.33% CTR and +0.66% RPM in production. |

### 8. Principled Synthetic Data Enables Scaling Laws for LLMs in Recommendation

| Field | Detail |
|-------|--------|
| Authors | Benyu Zhang, Qiang Zhang, Jianpeng Cheng, Hong-You Chen, Qifei Wang, Wei Sun, Shen Li, Jia Li, Jiahao Wu, Qunshu Zhang, Neeraj Bhatia, Xiangjun Fan, Hong Yan |
| Affiliation | — |
| Date | Feb 7, 2026 (ICML 2026) |
| Link | https://arxiv.org/abs/2602.07298 |
| **Innovation** | First demonstration of robust power-law scaling for LLMs continually pre-trained on recommendation-specific synthetic data. Layered curriculum with CF + interaction history. |
| **Key Results** | +130% recall@100 for SASRec vs real data. Predictable perplexity reduction across 0.6B–8B models on 163B tokens. |

### 9. SparseCTR: Unleashing Sparse Attention on Long-term Behaviors

| Field | Detail |
|-------|--------|
| Authors | (Lai Weijiang et al.) |
| Affiliation | — |
| Date | Jan 2026 |
| Link | https://arxiv.org/abs/2601.17836 |
| **Innovation** | TimeChunking for personalized sequence segmentation. Three-branch sparse attention (global, transition, local). Relative temporal encoding. Scaling law across 3 OOM FLOPs. |
| **Key Results** | +1.72% CTR, +1.41% CPM in online A/B test. |

### 10. LoopCTR: Loop Scaling Paradigm for CTR Prediction

| Field | Detail |
|-------|--------|
| Authors | — |
| Affiliation | — |
| Date | Apr 21, 2026 |
| Link | https://arxiv.org/abs/2604.19550 |
| **Innovation** | Reuses same layers recursively (train-multi-loop, infer-zero-loop). Hyper-Connected Residuals + MoE. Process supervision at every loop depth. |
| **Key Results** | 0.02–0.04 AUC untapped headroom in oracle analysis. |

### 11. EST: Efficient Scaling Laws in CTR via Unified Modeling

| Field | Detail |
|-------|--------|
| Authors | — |
| Affiliation | — |
| Date | Feb 11, 2026 |
| Link | https://arxiv.org/abs/2602.10811 |
| **Innovation** | Efficiently Scalable Transformer with Lightweight Cross-Attention (LCA) and Content Sparse Attention (CSA). All raw inputs in a single unified sequence. |
| **Key Results** | Power-law scaling ΔGAUC with model capacity. |

### 12. MLCC: Multi-Level Compression Cross Networks for Efficient Scaling

| Field | Detail |
|-------|--------|
| Authors | Jie Xia et al. |
| Affiliation | Bilibili |
| Date | Feb 12, 2026 |
| Link | https://arxiv.org/abs/2602.12041 |
| **Innovation** | Hierarchical compression + dynamic composition for feature crosses. Multi-Channel extension for parallel subspaces. |
| **Key Results** | Up to +0.52 AUC with 26× fewer params/FLOPs. Deployed in Bilibili ad system. |

---

## Sequence Modeling & Attention Mechanisms

### 13. Recurrent Transformer

| Field | Detail |
|-------|--------|
| Authors | — |
| Affiliation | — |
| Date | Apr 23, 2026 |
| Link | https://arxiv.org/abs/2604.21215 |
| **Innovation** | Layerwise recurrent attention: each layer attends to KV pairs from own activations. Tiling algorithm reduces HBM traffic from Θ(N²) to Θ(N log N). |
| **Key Results** | Improved cross-entropy on 300M-param C4 pretraining vs baseline. |

### 14. LUCID: Attention with Preconditioned Representations

| Field | Detail |
|-------|--------|
| Authors | — |
| Affiliation | — |
| Date | Feb 2026 |
| Link | https://arxiv.org/abs/2602.10410 |
| **Innovation** | Preconditioner from exponentiated key-key similarities decorrelates keys in RKHS. Bypasses softmax temperature/vanishing gradient trade-off. |
| **Key Results** | Up to 18% improvement on BABILong, 14% on RULER multi-needle at 128K context. |

### 15. Sessa: Selective State Space Attention

| Field | Detail |
|-------|--------|
| Authors | Liubomyr Horbatko |
| Affiliation | — |
| Date | Apr 20, 2026 |
| Link | https://arxiv.org/abs/2604.18580 |
| **Innovation** | Places attention inside recurrent feedback path. Proves power-law memory tails O(ℓ^{-β}) and flexible selective retrieval (non-decaying influence with distance). |
| **Key Results** | Strongest on long-context benchmarks; competitive on short-context LM. |

### 16. Latent Recurrent Transformer (LRT)

| Field | Detail |
|-------|--------|
| Authors | — |
| Affiliation | — |
| Date | May 2026 |
| Link | https://arxiv.org/abs/2605.26797 |
| **Innovation** | Lightweight: reuses source-layer hidden state from previous token as recurrent memory. Interleaved parallel training avoids sequential unrolling. ~2× baseline compute cost. |
| **Key Results** | Adds only 0.3% params. Improves LM loss and ICL under matched compute. |

### 17. MiniMax Sparse Attention (MSA)

| Field | Detail |
|-------|--------|
| Authors | Xunhao Lai, Weiqi Xu, Yufeng Yang, Qiaorui Chen, Yang Xu, Lunbin Zeng, Xiaolong Li, Haohai Sun, Haichao Zhu, Vito Zhang, Jinkai Hu, Jiayao Li, Rui Gao, Zekun Li, Songquan Zhu, Jingkai Zhou, Pengyu Zhao |
| Affiliation | MiniMax |
| Date | Jun 11, 2026 |
| Link | https://arxiv.org/abs/2606.13392 |
| **Innovation** | Blockwise sparse attention on GQA. Lightweight Index Branch selects Top-k blocks per GQA group. Exp-free TopK kernel + KV-outer sparse attention. |
| **Key Results** | 28.4× attention compute reduction at 1M context on 109B model. 14.2× prefill, 7.6× decoding speedup on H800. Public release. |

### 18. Sparse Feature Attention (SFA) / FlashSFA

| Field | Detail |
|-------|--------|
| Authors | Yan Xie, Tiansheng Wen, Tangda Huang, Bo Chen, Chenyu You, Stefanie Jegelka, Yifei Wang |
| Affiliation | MIT, etc. |
| Date | Mar 17, 2026 (ICLR 2026) |
| Link | https://arxiv.org/abs/2603.22300 |
| **Innovation** | Feature-axis sparsity instead of sequence-axis. k-sparse Q/K codes; attention cost Θ(n²k²/d). FlashSFA IO-aware kernel. |
| **Key Results** | Up to 2.5× speedup, ~50% FLOPs and KV-cache reduction. Matches dense baselines on GPT-2 and Qwen3. |

### 19. Phasor Transformer / Large Phasor Model (LPM)

| Field | Detail |
|-------|--------|
| Authors | — |
| Affiliation | — |
| Date | Mar 2026 |
| Link | https://arxiv.org/abs/2603.17433 |
| **Innovation** | Represents states on unit-circle manifold S¹. DFT token coupling for global O(N log N) mixing without attention maps. |
| **Key Results** | Competitive forecasting vs attention baselines with compact parameter budget. |

---

## LLM Reasoning & Reinforcement Learning

### 20. Stratagem: Learning Transferable Reasoning via Game Self-Play

| Field | Detail |
|-------|--------|
| Authors | Xiachong Feng, Deyi Yin, Xiaocheng Feng, Yi Jiang, Libo Qin, Yangfan Ye, Lei Huang, Weitao Ma, Qiming Li, Yuxuan Gu, Bing Qin, Lingpeng Kong |
| Affiliation | — |
| Date | Apr 20, 2026 (ACL 2026) |
| Link | https://arxiv.org/abs/2604.17696 |
| **Innovation** | Reasoning Transferability Coefficient φ measures abstraction level. Reasoning Evolution Reward ψ incentivizes progressive reasoning across game turns. |
| **Key Results** | Strong gains on competition-level math; ablation confirms both components critical. |

### 21. GIFT: Games as Informal Training for Generalizable LLMs

| Field | Detail |
|-------|--------|
| Authors | Nuoyan Lyu, Bingbing Xu, Xueyun Tian, Weihao Meng, Yige Yuan, Yang Zhang, Zhiyong Huang, Tat-Seng Chua, Huawei Shen |
| Affiliation | — |
| Date | Jan 9, 2026 (updated Jun 3) |
| Link | https://arxiv.org/abs/2601.05633 |
| **Innovation** | Introduces "informal learning" from games into LLM training. Coordinated Subtask Training (CST) replaces mixed RL updates with sequential subtask-specific ones. Matrix Games, TicTacToe, Who's the Spy. |
| **Key Results** | Game-based informal learning improves generalization beyond formal training alone. |

### 22. Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL

| Field | Detail |
|-------|--------|
| Authors | Chengshuai Shi, Wenzhe Li, Xinran Liang, Yizhou Lu, Wenjia Yang, Ruirong Feng, Seth Karten, Ziran Yang, Zihan Ding, Gabriel Sarch, Danqi Chen, Karthik Narasimhan, Chi Jin |
| Affiliation | Princeton University |
| Date | May 1, 2026 |
| Link | https://arxiv.org/abs/2605.00347 |
| **Innovation** | PPO with lightweight turn-level critic for long-horizon VLM agents. Tested on Super Mario Land (100+ turns). Systematic comparison of PPO vs GRPO vs Reinforce++. |
| **Key Results** | ≥3× average game progress vs frontier models. Cross-game generalization maintained. |

### 23. RA-RFT: Learning to Reason by Analogy via Retrieval-Augmented Reinforcement Fine-Tuning

| Field | Detail |
|-------|--------|
| Authors | Zilin Xiao, Qi Ma, Chun-cheng Jason Chen, Xintao Chen, Avinash Atreya, Hanjie Chen, Vicente Ordonez |
| Affiliation | — |
| Date | Jun 11, 2026 |
| Link | https://arxiv.org/abs/2606.13680 |
| **Innovation** | Gold-relevance distilled retriever ranks by reasoning utility (not semantic similarity). GRPO + retrieved analogous demonstrations. |
| **Key Results** | AIME 2025 avg@32: +7.1 points (Qwen3-1.7B), +2.8 points (Qwen3-4B) over GRPO. |

### 24. GraphPO: Graph-based Policy Optimization for Reasoning Models

| Field | Detail |
|-------|--------|
| Authors | Yuliang Zhan, Xinyu Tang, Jian Li, Dandan Zheng, Weilong Chai, Jingdong Chen, Jun Zhou, Ge Wu, Wenyue Tang, Hao Sun |
| Affiliation | — |
| Date | Jun 17, 2026 |
| Link | https://arxiv.org/abs/2606.18954 |
| **Innovation** | Rollouts as DAG: reasoning steps → edges, semantic states → nodes. Merges equivalent paths, efficiency + correctness advantages. Reduces advantage-estimation variance. |
| **Key Results** | Consistently outperforms chain- and tree-based baselines under same token/reponse budgets. |

### 25. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning

| Field | Detail |
|-------|--------|
| Authors | (SPIRAL team) |
| Affiliation | — |
| Date | Jun 2026 |
| Link | https://arxiv.org/abs/2506.24119 |
| **Innovation** | Fully online multi-agent multi-turn RL with self-play. Role-conditioned Advantage Estimation (RAE) stabilizes training. TicTacToe + Kuhn Poker + Simple Negotiation. |
| **Key Results** | Up to 10% improvement across 8 reasoning benchmarks on Qwen/Llama. Benefits even DeepSeek-R1-Distill. |

### 26. SWARR: Sliding-Window Attention with Reinforced Adaptation for Math Reasoning

| Field | Detail |
|-------|--------|
| Authors | Kai Liu et al. |
| Affiliation | — |
| Date | Jun 10, 2026 |
| Link | https://arxiv.org/abs/2606.11634 |
| **Innovation** | RL adapts SWA models for math reasoning. On-policy RL recovers accuracy lost during SWA conversion from SA. |
| **Key Results** | RL changes the conclusion about SWA viability for math reasoning (substantially narrows gap). |

### 27. RACES: Recursive Composition for Environment Scaling

| Field | Detail |
|-------|--------|
| Authors | Hao Xiang et al. |
| Affiliation | — |
| Date | Jun 10, 2026 |
| Link | https://arxiv.org/abs/2606.12373 |
| **Innovation** | Verifiable environments as composable LEGO bricks. SEQUENTIAL, PARALLEL, SORT, SELECT operators. 300 base → combinatorial environments. |
| **Key Results** | +3.1 pts on DeepSeek-R1-Distill-Qwen-14B, +2.3 pts on Qwen3-14B (6 unseen benchmarks). 50 envs match 300. |

### 28. GameTalk: Training LLMs for Strategic Multi-Turn Dialogue

| Field | Detail |
|-------|--------|
| Authors | — |
| Affiliation | — |
| Date | Jan 25, 2026 |
| Link | https://arxiv.org/abs/2601.16276 |
| **Innovation** | Adapts GRPO, DPO, and STaR for multi-turn conversational game theory. DPO most effective for persuasion tasks. |
| **Key Results** | Significantly outperforms baselines; learned conversational strategies transfer. |

### 29. MEMO: Memory-Augmented Model Context Optimization via Self-Play

| Field | Detail |
|-------|--------|
| Authors | — |
| Affiliation | — |
| Date | Mar 9, 2026 |
| Link | https://arxiv.org/abs/2603.09022 |
| **Innovation** | Weight-free self-play: tournament-style context evolution + persistent memory bank (CRUD operations). 19× fewer games than RL. |
| **Key Results** | GPT-4o-mini win rate 25.1%→49.5%; Qwen2.5-7B 20.9%→44.3% across 5 text games. |

### 30. LangMARL: Natural Language Multi-Agent Reinforcement Learning

| Field | Detail |
|-------|--------|
| Authors | — |
| Affiliation | — |
| Date | Apr 2026 |
| Link | https://arxiv.org/abs/2604.00722 |
| **Innovation** | MARL credit assignment in language space. Agent-level language credit + gradient evolution in language. Reframes HumanEval, HotPotQA, MATH as multi-agent tasks. |
| **Key Results** | Improved sample efficiency, interpretability, generalization across diverse cooperative tasks. |

---

## Emerging Themes

1. **CTR Scaling Laws Are Becoming a Reality**: Multiple papers (Kunlun, DeRes, FAT, EST, MLCC) now demonstrate predictable power-law scaling in CTR/recommendation — a domain that previously struggled with diminishing returns.

2. **Generative Recommendation Goes Production**: GenRec (JD), GRAB (Baidu), and UniRec show that generative retrieval is moving from research to deployment, with GRPO-based preference alignment becoming standard.

3. **Recurrence Is Back**: Recurrent Transformer, Sessa, and Latent Recurrent Transformer revisit recurrence as a complement (not replacement) to attention, achieving better long-context memory at lower cost.

4. **Attention Efficiency Explored from All Angles**: Sequence sparsity (MSA), feature sparsity (SFA), geometric constraints (Phasor), preconditioning (LUCID) — attention efficiency is being attacked on multiple orthogonal fronts.

5. **Games as RL Sandbox for Reasoning**: Stratagem, GIFT, Odysseus, SPIRAL, GameTalk, MEMO, LangMARL — the trend of using game environments to train transferable reasoning in LLMs/VLMs is accelerating rapidly.

6. **RL for Reasoning Beyond GRPO**: GraphPO (DAG-based), RA-RFT (retrieval-augmented), RACES (environment composition), SWARR (architecture-aware RL) — the RL-for-reasoning toolkit is diversifying quickly.
