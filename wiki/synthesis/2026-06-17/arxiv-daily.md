---
title: "arXiv Daily | 2026-06-17"
type: synthesis
created: 2026-06-17
updated: 2026-06-17
sources: []
tags: [arxiv, survey, llm, ctr, recommendation, games, sequential-modeling, advertising]
---

# arXiv Daily Report — 2026-06-17

Curated recent papers across AI, LLMs, recommendation, advertising, CTR, games, and sequential modeling.

---

## 1. LLMs & Foundation Models

### 1.1 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
| Field | Detail |
|-------|--------|
| **Authors** | Bo Liu, Leon Guertler, Simon Yu, Zichen Liu, Penghui Qi, Daniel Balcells, Mickel Liu, Cheston Tan, Weiyan Shi, Min Lin, Wee Sun Lee, Natasha Jaques |
| **Institution** | NUS, CFAR A*STAR, Northeastern, Sea AI Lab, Plastic Labs, UW |
| **Published** | Jun 2025 (updated Mar 2026) — **ICLR 2026 Poster** |
| **Link** | [arxiv.org/abs/2506.24119](https://arxiv.org/abs/2506.24119) |
| **Abstract** | Self-play framework where LLMs learn reasoning by playing multi-turn zero-sum games (Kuhn Poker, TicTacToe, Simple Negotiation) against themselves. Proposes Role-conditioned Advantage Estimation (RAE) to stabilize multi-agent training. Training Qwen3-4B on Kuhn Poker alone yields +8.6% math, +8.4% general reasoning — beats SFT on 25K expert trajectories. |
| **Key Innovations** | Fully online multi-agent multi-turn RL for LLMs; RAE for training stability; zero-sum games as automatic curriculum; reasoning transfer across 8 benchmarks. Code: [github.com/spiral-rl/spiral](https://github.com/spiral-rl/spiral) |

### 1.2 FLARE: Diffusion for Hybrid Language Model
| Field | Detail |
|-------|--------|
| **Authors** | (Hugging Face / academic collaboration) |
| **Institution** | Hugging Face |
| **Published** | Jun 1, 2026 |
| **Link** | [arxiv.org/abs/2606.01774](https://arxiv.org/abs/2606.01774) |
| **Abstract** | Systematic framework to convert hybrid-attention AR LLMs into diffusion LMs. Identifies transfer data quality as key factor. Enables one checkpoint to support both AR verified decoding and diffusion parallel denoising. Competitive with leading open-source dLLMs. |
| **Key Innovations** | Joint AR+diffusion objective; hardware-aware kernels; unified inference for hybrid models; identifies data quality > loss formulation for dLLM conversion. |

### 1.3 NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation
| Field | Detail |
|-------|--------|
| **Authors** | Huichao Zhang, Liao Qu, Yiheng Liu, Hang Chen et al. (35 authors) |
| **Institution** | ByteDance, Tsinghua University, Monash University |
| **Published** | Jan 5, 2026 |
| **Link** | [arxiv.org/abs/2601.02204](https://arxiv.org/abs/2601.02204) |
| **Abstract** | Unified decoder-only AR transformer trained on 6T interleaved text-image tokens. Next-token prediction for text, **next-scale prediction** for images (hierarchical, not raster-scan). Generates 1024×1024 images in 5 seconds — orders of magnitude faster than comparable AR models. SOTA among unified models, rivals specialized diffusion. |
| **Key Innovations** | Next-scale visual prediction within AR LM; dual-codebook tokenizer; prefix-tuning RL; image editing + video generation in one decoder-only model. |

### 1.4 Sequential Diffusion Language Model (SDLM)
| Field | Detail |
|-------|--------|
| **Authors** | Yue Cao, Tong Lu, Yu Qiao, Jifeng Dai, Wenhai Wang |
| **Institution** | OpenGVLab, Shanghai AI Lab |
| **Published** | Sep 28, 2025 |
| **Link** | [arxiv.org/abs/2509.24007](https://arxiv.org/abs/2509.24007) |
| **Abstract** | Introduces Next Sequence Prediction (NSP) to unify next-token and next-block prediction. SDLM retrofits pre-trained AR models into diffusion models at minimal cost. Uses fixed-size mask blocks with adaptive subsequence decoding. Matches AR baselines with only 3.5M training samples; 2.1× higher throughput than Qwen-2.5. |
| **Key Innovations** | NSP objective bridging token/block prediction; KV-cache compatible diffusion; adaptive-length decoding; scalable to 32B. |

---

## 2. Recommendation Systems & Advertising

### 2.1 IDProxy: Cold-Start CTR Prediction with Multimodal LLMs
| Field | Detail |
|-------|--------|
| **Authors** | Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan, Ruiyan Han, Feiyang Xiao, Yanhua Huang, Li Lin, Yang Luo, Yao Hu |
| **Institution** | Xiaohongshu (RedNote) Inc., Shanghai Jiao Tong University, Fudan University |
| **Published** | Mar 2, 2026 |
| **Link** | [arxiv.org/abs/2603.01590](https://arxiv.org/abs/2603.01590) |
| **Abstract** | Uses MLLMs (InternVL) to generate proxy embeddings from text+image for cold-start items. Coarse-to-fine alignment: contrastive learning pulls content representations toward ID embeddings of high-frequency items; then Structural Reuse injects proxy into Atomic ID Slots of the ranking model. **+1.93% Advertiser Value**, 2× AUC improvement for new items. Deployed on Xiaohongshu's Explore Feed. |
| **Key Innovations** | Semantic ID proxy via MLLM hidden states; Structural Reuse into existing ranking slots; deployed at scale (300M+ MAU). |

### 2.2 CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer
| Field | Detail |
|-------|--------|
| **Authors** | David Pardoe, Praneeth Boda, et al. |
| **Institution** | LinkedIn |
| **Published** | Feb 11, 2026 |
| **Link** | [arxiv.org/abs/2602.11410](https://arxiv.org/abs/2602.11410) |
| **Abstract** | End-to-end decoder-only transformer for ads CTR prediction. Treats CTR as a generation problem rather than classification. Context-conditioned decoding accounts for post-scoring signals (e.g., ad position). Deployed on LinkedIn's advertising platform. |
| **Key Innovations** | Generative framing for CTR; context-conditioned decoding; production deployment at LinkedIn scale. |

### 2.3 Fine-Tuned LLM as a Complementary Predictor Improving Ads System
| Field | Detail |
|-------|--------|
| **Authors** | (Pinterest Ads team) |
| **Institution** | Pinterest |
| **Published** | May 27, 2026 |
| **Link** | [arxiv.org/abs/2605.27856](https://arxiv.org/abs/2605.27856) |
| **Abstract** | Lightweight paradigm: fine-tuned open-source LLM predicts likely advertisers from user profiles/histories. Used as ancillary signal (not primary ranker) to supplement collaborative and feature-engineered signals. End-to-end improvements in production ads system. |
| **Key Innovations** | Complementary LLM predictor (not replacement ranker); cost-effective alternative to LLM-as-ranker; production deployment. |

### 2.4 FEDIN: Frequency-Enhanced Deep Interest Network for CTR Prediction
| Field | Detail |
|-------|--------|
| **Authors** | (Tencent) |
| **Institution** | Tencent |
| **Published** | May 3, 2026 |
| **Link** | [arxiv.org/abs/2605.01726](https://arxiv.org/abs/2605.01726) |
| **Abstract** | Discovers that true user interests show concentrated spectral patterns (low entropy) in frequency domain; noise appears as high-entropy. Proposes FEDIN with frequency-domain branch for periodic interest extraction. Complements time-domain modeling. |
| **Key Innovations** | Spectral entropy analysis of user behavior; frequency-enhanced interest network; target-aware spectral filtering. |

### 2.5 OneRetrieval: Unifying Multi-Branch E-commerce Retrieval with Editable Generative Model
| Field | Detail |
|-------|--------|
| **Authors** | Xuxin Zhang, Ben Chen, Yue Lv, Siyuan Wang, Yupeng Li, Kun Gai et al. |
| **Institution** | Kuaishou Technology |
| **Published** | Jun 11, 2026 |
| **Link** | [arxiv.org/abs/2606.13533](https://arxiv.org/abs/2606.13533) |
| **Abstract** | First editable generative retrieval model unifying multi-branch e-commerce search. Keyword-Aligned Encoding (KAE) ties identifier positions to interpretable attribute words. Reserved slots bind to new terms post-deployment without retraining. Matches best generative baseline on recall; intervention hit rate 10× above closed-codebook. Deployed at Kuaishou. |
| **Key Innovations** | Editable generative retrieval; Keyword-Aligned Encoding; reserved codebook slots for zero-retraining term injection; four-stage fine-tuning pipeline. |

### 2.6 UniVA: Unified Value Alignment for Generative Recommendation in Industrial Advertising
| Field | Detail |
|-------|--------|
| **Authors** | Xinxun Zhang, Yuling Xiong, Jiale Zhou, Zhengkai Guo et al. |
| **Institution** | Wuhan University, Tencent, Peking University |
| **Published** | May 7, 2026 |
| **Link** | [arxiv.org/abs/2605.05803](https://arxiv.org/abs/2605.05803) |
| **Abstract** | Unifies commercial value alignment across tokenization, decoding, and serving for generative advertising. Commercial SID tokenizer injects value attributes; Generation-as-Ranking decoder with eCPM-aware RL; value-guided personalized beam search. **37.04% Hit Rate@100 improvement**, **1.5% GMV lift** on WeChat Channels. |
| **Key Innovations** | Value-aligned tokenization; eCPM-aware RL decoding; personalized trie-constrained beam search; deployed at Tencent scale. |

### 2.7 Generative Click-through Rate Prediction with Applications to Search Advertising
| Field | Detail |
|-------|--------|
| **Authors** | Lingwei Kong, Lu Wang, Changping Peng, Zhangang Lin, Ching Law, Jingping Shao |
| **Institution** | (Major e-commerce platform) |
| **Published** | Jul 15, 2025 |
| **Link** | [arxiv.org/abs/2507.11246](https://arxiv.org/abs/2507.11246) |
| **Abstract** | Two-stage model: (1) generative pre-training for next-item prediction in user sequences, (2) fine-tuning within discriminative CTR framework. Deployed on one of the world's largest e-commerce platforms. |
| **Key Innovations** | Hybrid generative+discriminative CTR; two-stage training reconciles different data aggregation needs; online A/B validated. |

---

## 3. Games & Reinforcement Learning

### 3.1 Game-RL: Synthesizing Multimodal Verifiable Game Data to Boost VLMs' General Reasoning
| Field | Detail |
|-------|--------|
| **Authors** | Jingqi Tong, Jixin Tang, Hangcheng Li, Yurong Mou et al. |
| **Institution** | Fudan University, Shanghai AI Lab |
| **Published** | May 20, 2025 — **ICLR 2026** |
| **Link** | [arxiv.org/abs/2505.13886](https://arxiv.org/abs/2505.13886) |
| **Abstract** | Proposes Code2Logic to synthesize visual reasoning data from 30 video games (158 verifiable tasks). GameQA dataset. RL training on game data alone generalizes to 7 out-of-domain VL benchmarks. Game diversity and volume scale consistently. Used by Shanghai AI Lab, ByteDance Seed, THUML. |
| **Key Innovations** | Code2Logic synthesis pipeline; GameQA dataset; RL-on-games for general multimodal reasoning; shows scaling game diversity improves VLM reasoning. |

### 3.2 Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
| Field | Detail |
|-------|--------|
| **Authors** | Yidong He, Yutao Lai, Pengxu Yang, Jiarui Gan, Jiexin Wang, Yi Cai, Mengchen Zhao |
| **Institution** | (China — CCF-Kuaishou Explorer Fund) |
| **Published** | May 6, 2026 — **ICML 2026** |
| **Link** | [arxiv.org/abs/2605.04906](https://arxiv.org/abs/2605.04906) |
| **Abstract** | RL framework that integrates recursive reasoning (agent reasons about other agents' reasoning). Centralized CoT comparison module evaluates reasoning quality. Hybrid advantage with group-relative RL optimization. **22.1% average improvement** across ConnectFour, LeducHoldem, SimpleHanabi. |
| **Key Innovations** | Recursive reasoning paradigm for multi-agent LLMs; centralized CoT comparison (reward-model-free); hybrid advantage estimation. |

### 3.3 MARSHAL: Multi-Agent Reasoning via Self-Play with Strategic LLMs
| Field | Detail |
|-------|--------|
| **Authors** | (THU-NICS) |
| **Institution** | Tsinghua University |
| **Published** | Oct 2025 — **ICLR 2026** |
| **Link** | [arxiv.org/abs/2510.15414](https://arxiv.org/abs/2510.15414) |
| **Abstract** | End-to-end RL for multi-agent reasoning via self-play in competitive/cooperative games. Turn-level advantage estimator for fine-grained credit assignment; agent-specific advantage normalization. Qwen3-4B achieves **28.7% improvement** on held-out games; transferred to MAS yields +10.0% on AIME, +7.6% on GPQA-Diamond. |
| **Key Innovations** | Turn-level credit assignment in multi-agent self-play; agent-specific advantage normalization; cross-game generalization to reasoning benchmarks. |

---

## 4. Sequential Modeling

### 4.1 Diffusion Models for Adaptive Sequential Data Generation
| Field | Detail |
|-------|--------|
| **Authors** | Haoyang Cao, Minshuo Chen, Yinbin Han, Renyuan Xu |
| **Institution** | (Academic) |
| **Published** | Jun 4, 2026 |
| **Link** | [arxiv.org/abs/2606.06007](https://arxiv.org/abs/2606.06007) |
| **Abstract** | Sequential forward-backward diffusion framework for adapted time series generation. Progressively injects/removes noise along sequence conditioned on generated history. Novel score-matching objective for parallel training. Rigorous statistical guarantees. Validated on ARMA, GPs, and portfolio optimization. |
| **Key Innovations** | Adapted (non-anticipating) sequential diffusion; score-matching for parallel training; statistical guarantees for time series generation. |

---

## Summary by Domain

| Domain | Papers | Notable Trend |
|--------|--------|---------------|
| **LLMs & Foundation Models** | 4 | AR↔Diffusion convergence; self-play for reasoning; unified multimodal AR |
| **CTR / Advertising** | 4 | LLM/MLLM for cold-start; generative framing for CTR; frequency-domain interest modeling |
| **Recommendation / IR** | 3 | Editable generative retrieval; value alignment in GenRec; LLM as complementary signal |
| **Games & RL** | 3 | Self-play→reasoning transfer (major theme); multi-agent strategic RL; game data for VLM reasoning |
| **Sequential Modeling** | 1 | Adapted diffusion for time series with guarantees |

**Theme of the month**: Self-play and game-based RL as a scalable, human-supervision-free path to reasoning — applied to both language models (SPIRAL, MARSHAL, Strat-Reasoner) and vision-language models (Game-RL). Meanwhile, CTR/advertising continues to converge with generative LLM paradigms (CADET, UniVA, OneRetrieval, IDProxy).
