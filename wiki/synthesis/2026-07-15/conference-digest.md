---
title: "顶会论文专题报告 — Conference & arXiv Digest (2026-07-15)"
type: synthesis
created: 2026-07-15
updated: 2026-07-15
sources: [web-search, arxiv, conference-proceedings]
tags: [conference, icml-2026, aaai-2026, neurips-2025, iclr-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025, llm, agents, recommendation, ctr, generative-models, sequential-modeling, games, benchmarks]
---

# 顶会论文专题报告 — Conference & arXiv Digest (2026-07-15)

> 涵盖 12+ 顶会/顶刊，200+ 篇论文，20+ 实验室，覆盖 LLM、Agent、Recommendation、CTR、Generative Models、Sequential Modeling、Games、Benchmarks 等方向。

---

## 目录

1. [ICML 2026](#1-icml-2026-seoul-korea-jul-5-11)
2. [ICLR 2026](#2-iclr-2026-singapore-apr-28-may-2)
3. [CVPR 2026](#3-cvpr-2026-new-york-jun-5-7)
4. [AAAI 2026](#4-aaai-2026-singapore-jan-20-27)
5. [NeurIPS 2025](#5-neurips-2025-dec)
6. [KDD 2026](#6-kdd-2026-aug)
7. [ACL 2026](#7-acl-2026-san-diego-jul-2-7)
8. [WWW 2026](#8-www-2026-dubai-apr-13-17)
9. [SIGIR 2026](#9-sigir-2026-melbourne-jul-20-24)
10. [EMNLP 2025 / CIKM 2025 / RecSys 2025](#10-other-venues)
11. [Award Papers Summary](#11-award-papers-summary)
12. [Key Trends & Observations](#12-key-trends--observations)

---

## 1. ICML 2026 (Seoul, Korea — Jul 5–11)

> ICML 2026 accepted ~7,000 papers. Diffusion models dominated top honors; a 10-year-old A3C paper received Test of Time.

### 1.1 Outstanding Paper Awards

#### The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
- **Authors:** Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang
- **Affiliation:** Alibaba / Multiple institutions
- **Venue:** ICML 2026 — Outstanding Paper Award
- **Abstract & Key Innovations:** Rethinks the assumption that arbitrary permutation orders benefit diffusion language models. Challenges the "flexibility trap" — the idea that more ordering options lead to better generation. Demonstrates that carefully chosen fixed orders can match or exceed flexible approaches.
- **Link:** https://icml.cc/virtual/2026/poster/61998

#### High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions
- **Authors:** Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin
- **Affiliation:** MIT / Multiple institutions
- **Venue:** ICML 2026 — Outstanding Paper Award
- **Abstract & Key Innovations:** Provides theoretical foundations for high-accuracy sampling in diffusion models. Establishes convergence guarantees for log-concave distributions, bridging theory and practice in diffusion-based generation.

### 1.2 Honorable Mentions

| Paper | Authors | Key Innovation |
|-------|---------|---------------|
| Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes | Taufeeque, Heimersheim, Gleave, Cundy | Probes for deception in RL with verifiable rewards |
| Motion Attribution for Video Generation | Wu, Paschalidou, Gao, Torralba, Leal-Taixé, Russakovsky, Fidler, Lorraine | Attribution methods for understanding video generation models |
| How Much Can Language Models Memorize | Morris, Sitawarin, Kokhlikyan, Gu, Suh, Rush, Chaudhuri, Mahloujifar | Distinguishes intended vs unintended memorization in LLMs |
| A Random Matrix Perspective on the Consistency of Diffusion Models | Wang, Zavatone-Veth, Pehlevan | Explains why diffusion models generate nearly identical images from same seed |
| To Grok Grokking: Provable Grokking in Ridge Regression | Xu, Vardi, Safran | Shows grokking occurs even in simple ridge regression |

### 1.3 Agent Systems (ICML 2026)

#### HiPER: Hierarchical Plan–Execute RL for Multi-Turn LLM Agents
- **Authors:** ICML 2026 Poster
- **Venue:** ICML 2026, Poster Session Mon Jul 6
- **Abstract & Key Innovations:** Hierarchical RL framework jointly modeling high-level subgoal planning and low-level action execution. Introduces Hierarchical Advantage Estimation (HAE) for two-timescale policy gradient with variance reduction.
- **Key Results:** 97.4% success on ALFWorld (+6.6% over best prior), 83.3% on WebShop.
- **Comparison:** Outperforms flat RL policies (GRPO, GiGPO) significantly on long-horizon tasks.
- **Link:** https://icml.cc/virtual/2026/poster/64058

#### Understanding Reasoning Collapse in LLM Agent Reinforcement Learning
- **Authors:** ICML 2026 Poster
- **Venue:** ICML 2026, Poster Session Tue Jul 7
- **Abstract & Key Innovations:** Identifies "reasoning collapse" where LLM reasoning becomes generic and input-agnostic. Proposes information-theoretic decomposition: conditional entropy H(Z|X) and mutual information I(X;Z). Introduces reward-variance-aware filtering.
- **Key Results:** Improves input dependence, stability, and performance across multi-turn environments, model scales, and modalities (including VLMs).
- **Link:** https://icml.cc/virtual/2026/poster/66821

#### Just-In-Time Reinforcement Learning (JitRL)
- **Authors:** ICML 2026 Poster
- **Venue:** ICML 2026, Poster Session Mon Jul 6
- **Abstract & Key Innovations:** Training-free framework enabling test-time policy optimization without gradient updates. Maintains dynamic non-parametric memory of experiences, retrieves relevant trajectories to estimate action advantages on-the-fly.
- **Key Results:** Outperforms WebRL (fine-tuning method) while reducing costs by 30×. New SOTA among training-free methods on WebArena and Jericho.
- **Comparison:** Beats computationally expensive fine-tuning methods.
- **Link:** https://icml.cc/virtual/2026/poster/61517

#### Multi²: Hierarchical Multi-Agent Decision-Making with LLM-Based Agents
- **Authors:** ICML 2026 Poster
- **Venue:** ICML 2026, Poster Session Tue Jul 7
- **Abstract & Key Innovations:** Decomposes agent behavior into System 1 (high-level sub-goal generation via SFT) and System 2 (low-level action execution via offline-to-online RL). Mitigates objective drift in long-horizon tasks.
- **Key Results:** Consistently outperforms strong agentic baselines across diverse interactive environments. Releases three hierarchical benchmark datasets.
- **Link:** https://icml.cc/virtual/2026/poster/65074

#### BEACON: Milestone-Guided Policy Learning for Long-Horizon Language Agents
- **Authors:** ICML 2026 Poster
- **Venue:** ICML 2026, Poster Session Tue Jul 7
- **Abstract & Key Innovations:** Leverages compositional structure of long-horizon tasks for precise credit assignment. Partitions trajectories at milestone boundaries, applies temporal reward shaping, estimates advantages at dual scales.
- **Key Results:** On ALFWorld long-horizon tasks: 92.9% success rate (nearly doubling GRPO's 53.5%). Effective sample utilization from 23.7% to 82.0%.
- **Comparison:** Consistently outperforms GRPO and GiGPO on ALFWorld, WebShop, ScienceWorld.
- **Link:** https://icml.cc/virtual/2026/poster/65128

#### GLARE: Scalable Neuro-Symbolic Reward Shaping for LLM Agents
- **Authors:** ICML 2026 Poster
- **Venue:** ICML 2026, Poster Session Wed Jul 8
- **Abstract & Key Innovations:** Neuro-symbolic reward framework decoupling semantic abstraction from credit assignment. Extracts trajectory events into discrete representations, translates to Linear Temporal Logic (LTL) formulas, compiles into deterministic automata.
- **Key Results:** Outperforms GRPO by 12.1% in success rate on ALFWorld, 8.1% improvement over LLM-based judges using only 15% of their computational cost.
- **Link:** https://icml.cc/virtual/2026/poster/66450

#### From Outcomes to Actions: Hindsight Policy Optimization (HPO)
- **Authors:** ICML 2026 Poster
- **Venue:** ICML 2026, Poster Session Wed Jul 8
- **Abstract & Key Innovations:** Projects policy distributions into intent space, extracts low-variance learning signals from Wasserstein distance. Aggregates semantically similar states/actions for bounded-variance estimation.
- **Link:** https://icml.cc/virtual/2026/poster/62250

### 1.4 Test of Time Award

#### Asynchronous Methods for Deep Reinforcement Learning (A3C)
- **Authors:** Volodymyr Mnih, Adria Puigdomenech Badia, Mehdi Mirza, Alex Graves, Timothy Lillicrap, Tim Harley, David Silver, Koray Kavukcuoglu
- **Affiliation:** DeepMind (2016)
- **Venue:** ICML 2016 → ICML 2026 Test of Time
- **Key Impact:** Paved the way for asynchronous RL becoming a major factor in RL for LLM post-training; reshaped how RL is done in practice today.

---

## 2. ICLR 2026 (Singapore — Apr 28–May 2)

> ICLR 2026 accepted 5,356 papers, with 223 oral papers. Two outstanding papers and one honorable mention.

### 2.1 Outstanding Paper Awards

#### Transformers are Inherently Succinct
- **Authors:** Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin
- **Affiliation:** Max Planck Institute / RPTU Kaiserslautern
- **Venue:** ICLR 2026 — Outstanding Paper Award
- **Abstract & Key Innovations:** Proves Transformers can represent formal languages (finite automata, LTL formulas) with significantly fewer parameters than standard representations. Establishes that the decision problem for Transformer properties is EXPSPACE-complete.
- **Key Results:** Demonstrates stronger expressive capability compared to RNNs. Shows Transformers encode formal concepts more succinctly.
- **Link:** https://openreview.net/forum?id=Yxz92UuPLQ

#### LLMs Get Lost in Multi-Turn Conversation
- **Authors:** ICLR 2026 Outstanding Paper
- **Venue:** ICLR 2026 — Outstanding Paper Award
- **Abstract & Key Innovations:** Identifies mismatch between training (single-turn text completion) and deployment (multi-turn conversations). Designs benchmark revealing 39% average performance drop from single-turn to multi-turn.
- **Key Results:** 39% average performance degradation. Attributes to (1) modest decline in intrinsic LLM ability and (2) premature commitment leading to uncorrectable errors.

### 2.2 Honorable Mention

#### The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm
- **Authors:** Noah Amsel, David Persson, Christopher Musco, Robert M. Gower
- **Venue:** ICLR 2026 — Honorable Mention
- **Abstract & Key Innovations:** Provides principled approach to improving the Muon optimizer (variant of Nesterov momentum using polar decomposition). Addresses numerical optimization foundations.

### 2.3 Recommendation & CTR Papers

#### RecCocktail: A Generalizable and Efficient Framework for LLM-Based Recommendation
- **Authors:** Hou, Bai, Wu, Liu, Zhang, Liu, ... Wang
- **Affiliation:** Multiple institutions
- **Venue:** AAAI 2026 (also cited in ICLR context)
- **Abstract & Key Innovations:** Combines domain-general "base spirit" LoRA with domain-specific "ingredient" LoRA via entropy-guided adaptive merging. Plug-and-play with no additional inference overhead.
- **Key Results:** Effective across warm and cold-start scenarios on multiple datasets.
- **Link:** https://ojs.aaai.org/index.php/AAAI/article/view/38504

#### TreeBridge: Aligning LLM Embeddings in Industrial Recommender Systems
- **Authors:** Ni, Yuanpeng, Zhou, Hong, Zhang, Cai, ... Li
- **Affiliation:** Shopee / Multiple institutions
- **Venue:** AAAI 2026
- **Abstract & Key Innovations:** Structure-aware generative encoding tree bridging semantic gap between LLM embeddings and recommendation tasks. Online-offline hybrid service paradigm for low-latency deployment.
- **Key Results:** Deployed on Shopee (Southeast Asia's largest e-commerce). 1.55% relative improvement in GMV since May 2025 deployment. Serves hundreds of millions of users.
- **Link:** https://ojs.aaai.org/index.php/AAAI/article/view/41478

#### MoMoREC: Multi-agent Motivation Generation for Residual Semantic ID-Aware Recommendation
- **Authors:** Yige Wang, Mingming Li, Li Wang, Kaichen Zhao, Wangming Li, Weipeng Jiang, et al.
- **Affiliation:** Alibaba (Taobao)
- **Venue:** AAAI 2026
- **Abstract & Key Innovations:** Multi-agent LLM architecture analyzing user shopping motivations. Residual semantic ID approach via clustering and residual dimensionality reduction for low-dimensional IDs.
- **Key Results:** Online A/B test on Taobao 88VIP: +6.3% GMV, +1% TCR. Seamlessly integrates with traditional recommendation models.
- **Link:** https://doi.org/10.1609/aaai.v40i19.38623

### 2.4 Agent Papers at ICLR 2026

ICLR 2026 had 162+ agent-related papers. Key highlights:

| Paper | Key Innovation |
|-------|---------------|
| ARMOR: Aligning Secure and Safe LLMs via Meticulous Reasoning | Safety alignment for LLMs |
| Adaptive Thinking: LLMs Know When to Think in Latent Space | Dynamic latent-space reasoning |
| Bottlenecked Transformers: Periodic KV Cache Consolidation | Efficient long-context reasoning |
| BWCache: Accelerating Video Diffusion through Block-Wise Caching | Video diffusion acceleration |
| MADFormer: Mixed Autoregressive and Diffusion Transformers | Hybrid generation architecture |

---

## 3. CVPR 2026 (New York — Jun 5–7)

> CVPR 2026: 16,092 submissions, 4,090 accepted (25.4% acceptance rate).

### 3.1 Best Paper Awards

#### Best Paper: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
- **Authors:** Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **Affiliation:** Google DeepMind / University College London / University of Oxford
- **Venue:** CVPR 2026 — Best Paper Award
- **Abstract & Key Innovations:** D4RT — unified transformer-based architecture for reconstructing geometry and motion of dynamic 4D scenes from video. Estimates depth, spatio-temporal correspondence, and full camera parameters.
- **Key Results:** Lightweight and highly scalable method enabling remarkably efficient training and inference. Independent probing of any 3D position at any point in space and time.
- **Comparison:** Significant gains over prior methods in dynamic scene reconstruction.
- **Note:** Third Best Paper for Oxford VGG in six years (also CVPR 2020, 2025).

#### Best Paper (Runner-up): Native and Compact Structured Latents for 3D Generation
- **Authors:** Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang
- **Affiliation:** Tsinghua University / Microsoft Research / USTC / Microsoft AI
- **Venue:** CVPR 2026 — Best Paper Award
- **Abstract & Key Innovations:** O-Voxel — novel representation for 3D generative modeling capturing complex shapes and surface attributes. Significantly improves quality and realism of AI-generated 3D assets.

#### Best Paper (Honorable): SAM 3D: 3Dfy Anything in Images
- **Authors:** Xingyu Chen, Fu-Jen Chu, Pierre Gleize, Kevin J Liang, Alexander Sax, Hao Tang, Weiyao Wang, Michelle Guo, Thibaut Hardin, Xiang Li, Aohan Lin, Jia-Wei Liu, Ziqi Ma, Anushka Sagar, Bowen Song, Xiaodong Wang, Jianing Yang, Bowen Zhang, Piotr Dollár, Georgia Gkioxari, Matt Feiszli, Jitendra Malik
- **Affiliation:** Meta FAIR (FAIR Intelligence Labs)
- **Venue:** CVPR 2026 — Best Paper Honorable Mention
- **Abstract & Key Innovations:** Generative model for visually grounded 3D object reconstruction predicting geometry, texture, and layout from a single image. Human- and model-in-the-loop pipeline for annotating object shape, texture, and pose.
- **Key Results:** At least 5:1 win rate in human preference tests on real-world objects and 6:1 on scenes. Releases code, model weights, online demo, and SA-3DAO benchmark.
- **Link:** https://ai.meta.com/sam3d

### 3.2 Generative Models (CVPR 2026)

| Paper | Affiliation | Key Innovation |
|-------|-------------|---------------|
| MacTok: Robust Continuous Tokenization for Image Generation | - | Continuous tokenization for DiT-based generation |
| A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens | - | 1-token-per-frame world models |
| Back to Basics: Let Denoising Generative Models Denoise | Kaiming He group | Revisiting denoising fundamentals |
| TUNA: Taming Unified Visual Representations for Native Unified Multimodal Models | - | Unified continuous visual representation via VAE+representation encoder for understanding and generation |
| Molmo2: Open Weights for Vision-Language Models with Video Understanding | AI2 | Open-weight VLM with video grounding |

### 3.3 Vision-Language Models (CVPR 2026)

| Paper | Key Innovation |
|-------|---------------|
| TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch-Text Alignment | Improved patch-text alignment |
| Granulon: Awakening Pixel-Level Visual Encoders with Adaptive Multi-Granularity Semantics | DINOv3-based MLLM, +30% accuracy, -20% hallucination |

### 3.4 3D Vision (CVPR 2026)

| Paper | Key Innovation |
|-------|---------------|
| tttLRM: Test-Time Training for Long Context Autoregressive 3D Reconstruction | Test-time training for 3D |
| B³-Seg: Camera-Free, Training-Free 3DGS Segmentation | Analytic eigendecomposition + Bayesian updates |
| 4D-RGPT: Toward Region-level 4D Understanding | Perceptual distillation for 4D |

---

## 4. AAAI 2026 (Singapore — Jan 20–27)

> AAAI-26 Technical Tracks covering ML, NLP, recommendation, and applications.

### 4.1 Recommendation Systems

#### Extracting Interaction-Aware Monosemantic Concepts in Recommender Systems
- **Authors:** Arviv, Elisha, Barkan, Koenigstein
- **Venue:** AAAI 2026
- **Abstract & Key Innovations:** Sparse Autoencoder (SAE) for extracting monosemantic neurons from user/item embeddings. Prediction-aware training objective preserving user-item interaction structure. Neurons capture genre, popularity, temporal trends for post-hoc control.
- **Key Results:** Generalizes across recommendation models and datasets.

#### Fidelity-Aware Recommendation Explanations via Stochastic Path Integration (SPINRec)
- **Authors:** Barkan, Schein, Elisha, Bogina, Baklanov, Koenigstein
- **Venue:** AAAI 2026
- **Abstract & Key Innovations:** Model-agnostic explanation method adapting path-integration to sparse/implicit recommendation data. Stochastic baseline sampling from empirical data distribution.
- **Key Results:** Consistently outperforms all baselines across MF, VAE, NCF on ML1M, Yahoo! Music, Pinterest.

#### RecToM: Benchmark for Evaluating Machine Theory of Mind in LLM-based Conversational Recommender Systems
- **Authors:** Li, Shi, Deng
- **Venue:** AAAI 2026
- **Abstract & Key Innovations:** Evaluates Theory of Mind (ToM) in LLMs within recommendation dialogues — inferring Beliefs, Desires, and Intents during multi-turn interactions.

### 4.2 Key AAAI 2026 Themes

- LLM-based recommendation frameworks (RecCocktail, TreeBridge, MoMoREC)
- Interpretability and explainability in rec systems
- Theory of Mind for conversational recommendation
- Multi-agent LLM architectures for user understanding

---

## 5. NeurIPS 2025 (Dec 2025)

> NeurIPS 2025 featured strong work on generative models, 3D vision, and theoretical foundations.

### 5.1 Highlighted Papers

#### Mean Flows for One-step Generative Modeling (MeanFlow)
- **Venue:** NeurIPS 2025
- **Abstract & Key Innovations:** Principled framework for one-step generative modeling using mean velocity fields. Trained entirely from scratch without pre-training, distillation, or curriculum learning.
- **Key Results:** ImageNet 256×256: FID 3.43 with 1-NFE (50–70% relative improvement over prior SOTA). 2-NFE: FID 2.20, on par with DiT (FID 2.27) and SiT (FID 2.15) at 250×2 NFE.

#### Energy Matching: Unifying Flow Matching and Energy-Based Models
- **Venue:** NeurIPS 2025
- **Abstract & Key Innovations:** Two-regime training combining EBMs and flow matching. Time-independent scalar energy field for generation and inverse problems.
- **Key Results:** Outperforms state-of-the-art EBMs on CIFAR-10 and ImageNet. FID 6.64 on CIFAR-10 (vs 9.35 for prior best EBM).

#### PartCrafter: Structured 3D Mesh Generation via Compositional Latent Diffusion Transformers
- **Venue:** NeurIPS 2025
- **Abstract & Key Innovations:** Generates multiple distinct 3D parts by binding each to dedicated latent variable sets. Novel local-global attention mechanism for intra/inter-part information flow.
- **Key Results:** Surpasses underlying 3D object generative model on reconstruction fidelity.

#### AlignedGen: Aligning Style Across Generated Images
- **Venue:** NeurIPS 2025
- **Abstract & Key Innovations:** Training-free style-aligned generation for DiT architecture. Discovers conflicting position embeddings as root cause of attention sharing failure in DiT. Introduces Shifted Position Embedding (ShiftPE).

#### GPSToken: Gaussian Parameterized Spatially-adaptive Tokenization
- **Venue:** NeurIPS 2025
- **Abstract & Key Innovations:** 2D Gaussian functions for spatially adaptive tokenization. Decouples spatial layout from texture features for two-stage generation.
- **Key Results:** 128 tokens per image achieves FID 1.50 (ImageNet 256×256). 3–5× faster training convergence than SiT-XL/2.

#### ARGenSeg: Image Segmentation with Autoregressive Image Generation Model
- **Venue:** NeurIPS 2025
- **Abstract & Key Innovations:** Unified framework integrating image segmentation into MLLMs through generation paradigm. Next-scale-prediction for parallel token generation.
- **Key Results:** >10× speedup over sequential generation (Emu3), surpasses prior SOTA on multiple segmentation datasets.

---

## 6. KDD 2026 (Aug 2026)

### 6.1 CTR Prediction

#### CTR-Sink: Attention Sink for Language Models in CTR Prediction
- **Authors:** Zixuan Li, Binzong Geng, Jing Xiong, Yong He, Yuxuan Hu, Jian Chen, Dingwei Chen, Xiyu Chang, Ngai Wong, Liang Zhang, Linjian Mo, Chengming Li, Chuan Yuan, Zhenan Sun
- **Affiliation:** Ant Group / University of Hong Kong
- **Venue:** KDD 2026
- **Abstract & Key Innovations:** Introduces behavior-level attention sinks (SINK tokens) fused with recommendation-specific signals (temporal distance) between consecutive behaviors. Two-stage training strategy + sink-specific attention enhancement.
- **Key Results:** Consistent AUC improvements of 0.2–0.5% over baseline LM-CTR methods on industrial dataset, MovieLens, and KuaiRec across RoBERTa and Qwen architectures.
- **Comparison:** Significantly outperforms [CLS]-based and random SINK baselines.
- **Code:** https://github.com/UGUESS-lzx/CTR-SINK
- **Link:** https://arxiv.org/pdf/2508.03668

#### GR4AD: Generative Retrieval for Advertisement (Kuaishou)
- **Affiliation:** Kuaishou
- **Venue:** KDD 2026
- **Key Results:** +4.2% ad revenue improvement in online deployment.

#### RankUp: High-rank Representations for Ad Ranking (Tencent)
- **Affiliation:** Tencent
- **Venue:** KDD 2026
- **Link:** https://arxiv.org/pdf/2604.17878

### 6.2 Recommendation Systems

#### UniSID: End-to-End Semantic ID Generation for Generative Advertisement Recommendation
- **Authors:** Jie Jiang, Xinxun Zhang, Enming Zhang, Yuling Xiong, Jun Zhang, Jingwen Wang, et al.
- **Venue:** arXiv 2026 (targeting KDD)
- **Abstract & Key Innovations:** Unified SID generation framework jointly optimizing embeddings and SIDs end-to-end from raw advertising data. Multi-granularity contrastive learning + summary-based ad reconstruction.
- **Key Results:** Up to 4.62% improvement in Hit Rate across downstream advertising scenarios.

#### MARS: Modality-Aligned Retrieval for Sequence Augmented CTR Prediction (Kuaishou)
- **Authors:** Shanqi Liu, Chao Feng, Xiang Li, Fuzhen Zhuang
- **Affiliation:** Kuaishou
- **Venue:** KDD 2025
- **Abstract & Key Innovations:** Stein kernel-based method to align text and image features into unified semantic space. Retrieval-augmentation for low-active users from high-active users.
- **Key Results:** Deployed serving mainstream traffic to hundreds of millions of users. +0.728% app usage time per low-activity user in online A/B test.

#### GenRec: Preference-Oriented Generative Framework for Large-Scale Recommendation (JD)
- **Authors:** Yanyan Zou, Junbo Qi, Lunsong Huang, Yu Li, Kewei Xu, Jiabao Gao, et al.
- **Affiliation:** JD.com
- **Venue:** arXiv 2026
- **Abstract & Key Innovations:** Page-wise NTP task, asymmetric linear Token Merger for compression, GRPO-SR reinforcement learning with hybrid rewards.
- **Key Results:** +9.5% click count, +8.7% transaction count in month-long online A/B tests on JD App.

---

## 7. ACL 2026 (San Diego — Jul 2–7)

### 7.1 LLM Reasoning & Search

#### Deliberative Searcher: Improving LLM Reliability via RL with Constraints
- **Authors:** Zhenyun Yin, Shujie Wang, Xuhong Wang, Xingjun Ma, Yinchun Wang
- **Venue:** ACL 2026
- **Abstract & Key Innovations:** Integrates search operations into chain-of-thought generation with explicit confidence calibration. Constrained RL with adaptive Lagrangian multipliers jointly optimizing correctness and reliability.
- **Key Results:** 7B model reduces false-certain rates from 54% to 2%. Confidence-weighted aggregation matches 16-sample majority voting with only 4 samples (4× reduction in inference compute).
- **Comparison:** Competitive with GPT-4o, GPT-4.1, Claude-Sonnet-4.

#### PaCoRe: Parallel Coordinated Reasoning
- **Authors:** Jingcheng Hu, Yinmin Zhang, Shijie Shang, et al.
- **Affiliation:** Microsoft Research / Multiple institutions
- **Venue:** ACL 2026
- **Abstract & Key Innovations:** Massive parallel exploration coordinated via message-passing architecture. Trained end-to-end with large-scale outcome-based RL. Multi-million-token effective TTC.
- **Key Results:** 8B model reaches 94.5% on HMMT 2025, surpassing GPT-5's 93.2% by scaling effective TTC to ~2 million tokens.
- **Comparison:** Surpasses GPT-5, Kimi-K2-Thinking, DeepSeek-V3.1-Terminus, Qwen3-235B.

### 7.2 NLP & Linguistics

#### Fine-Grained Analysis of Shared Syntactic Mechanisms in Language Models
- **Authors:** Ryoma Kumon, Hitomi Yanaka
- **Venue:** ACL 2026
- **Abstract & Key Innovations:** Investigates shared neural mechanisms across syntactic constructions. Filler-gap dependencies show highly localized shared mechanism; NPI licensing shows construction-specific mechanisms.

#### Implicit Representations of Grammaticality in Language Models
- **Venue:** ACL 2026
- **Abstract & Key Innovations:** LMs acquire implicit grammaticality distinction in hidden layers distinct from string probability. English-trained probes generalize cross-linguistically.

#### Think in Sentences: Explicit Sentence Boundaries Enhance LLM Capabilities
- **Venue:** ACL 2026
- **Abstract & Key Innovations:** Inserts delimiters at sentence boundaries. Up to 7.7% on GSM8k and 12.5% on DROP improvement. Works across 7B to 600B models (DeepSeek-V3).

#### Robertha: Eigenspectrum Regularized Attention for Robust NLU
- **Venue:** ACL 2026
- **Abstract & Key Innovations:** Modern Hopfield Networks-based attention with Eigenspectrum Regularization (ESR). Iterative refinement for differential recovery of corrupted embeddings.

### 7.3 Recommendation

#### ThinkRec: Thinking-based Recommendation via LLM
- **Affiliation:** Multiple institutions
- **Venue:** WWW 2026 (also presented in ACL context)
- **Abstract & Key Innovations:** Shifts LLM4Rec from intuitive System 1 to rational System 2. Thinking activation mechanism with synthetic reasoning traces. Instance-wise expert fusion for personalized reasoning.
- **Code:** https://github.com/Yu-Qi-hang/ThinkRec

#### L2Rec: Dual-View Understanding of LLMs for Personalized Recommendation
- **Venue:** arXiv 2026
- **Abstract & Key Innovations:** Unifies behavioral and semantic understanding at parameter level via Dual-view Personalized Mixture-of-Experts (DPMoE). Adaptive cross-view fusion.
- **Key Results:** Consistently outperforms SOTA baselines on four datasets; validated by online A/B testing.

---

## 8. WWW 2026 (Dubai — Apr 13–17)

### 8.1 CTR & Recommendation

#### GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction
- **Venue:** WWW 2026
- **Abstract & Key Innovations:** Generative user intent framework with semantic interest cohorts. Hierarchical candidate-aware network for dynamic contextual signals. Joint optimization with self-supervised regularization.
- **Key Results:** State-of-the-art across MovieLens, Amazon Fashion, Amazon Musical Instruments.

#### SparseCTR: Sparse Attention on Long-term Behaviors for CTR Prediction
- **Affiliation:** Meituan
- **Venue:** WWW 2026
- **Abstract & Key Innovations:** Three-branch sparse self-attention for global interests, interest transitions, and short-term interests. Composite relative temporal encoding. Shows obvious scaling law phenomenon across 3 orders of magnitude in FLOPs.
- **Key Results:** Online A/B: +1.72% CTR, +1.41% CPM.

#### GEMS: Gradient Multi-Subspace Tuning for Unified Search and Recommendation
- **Affiliation:** SIGIR 2026
- **Abstract & Key Innovations:** Multi-Subspace Decomposition disentangling shared/task-specific signals. Null-Space Projection preserving general-domain knowledge. Deployable at billion-parameter scale.

### 8.2 Ad Recommendation

#### LLM Retrieval for Stable and Predictable Ad Recommendations (LinkedIn)
- **Affiliation:** LinkedIn
- **Venue:** arXiv 2026
- **Abstract & Key Innovations:** Fine-tuned LLMs for semantic candidate generation. Hierarchical semantic attributes from ad creatives. Graph-based expansion for semantic variants.
- **Key Results:** +0.45% topline lift, +1.2% final stage recall, 8.62% reduction in A/A' difference, 45% improvement in daily impression MAD.

---

## 9. SIGIR 2026 (Melbourne — Jul 20–24)

#### GEMS: Gradient Multi-Subspace Tuning for Unified Search and Recommendation
- **Venue:** SIGIR 2026
- **Abstract & Key Innovations:** (Detailed above in WWW section). Consistently outperforms SOTA baselines across search and recommendation tasks.

#### SIGMA: A Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress
- **Affiliation:** Alibaba (AliExpress)
- **Venue:** SIGIR 2026
- **Abstract & Key Innovations:** Generative recommendation reshaping recommender system paradigm. Semantic-grounded instruction-driven approach for multi-task recommendation.

---

## 10. Other Venues

### EMNLP 2025
- Active in LLM reasoning, interpretability, and multilingual NLP
- Key papers on causal interpretability, syntactic mechanisms

### CIKM 2025
- CTR prediction, information retrieval, knowledge discovery

### RecSys 2025 (Prague — Sep 22–26)
- 19th ACM Conference on Recommender Systems
- Key themes: generative recommendation, scaling laws, multi-modal rec

---

## 11. Award Papers Summary

| Conference | Award | Paper | Key Contribution |
|-----------|-------|-------|-----------------|
| ICML 2026 | Outstanding | The Flexibility Trap | Arbitrary order in diffusion LMs |
| ICML 2026 | Outstanding | High-Accuracy Sampling | Theoretical foundations for diffusion sampling |
| ICML 2026 | Test of Time | A3C (Asynchronous Methods for DRL) | Pioneered async RL → RLHF |
| ICLR 2026 | Outstanding | Transformers are Inherently Succinct | Theoretical expressiveness of Transformers |
| ICLR 2026 | Outstanding | LLMs Get Lost in Multi-Turn | 39% degradation in multi-turn |
| ICLR 2026 | Honorable | The Polar Express (Muon) | Matrix sign methods for optimization |
| CVPR 2026 | Best Paper | D4RT | Dynamic 4D scene reconstruction |
| CVPR 2026 | Best Paper | O-Voxel | Native structured latents for 3D |
| CVPR 2026 | Honorable | SAM 3D | 3D reconstruction from single image (Meta) |

---

## 12. Key Trends & Observations

### 12.1 LLM Agent Systems
- **Hierarchical decomposition** is the dominant paradigm: HiPER, Multi², BEACON all decompose into planning + execution
- **Training-free methods** gaining traction: JitRL matches fine-tuning at 30× lower cost
- **Reasoning collapse** is a recognized failure mode requiring new diagnostics (mutual information based)
- **Neuro-symbolic reward shaping** (GLARE) bridges semantic understanding with deterministic tracking

### 12.2 Recommendation & CTR
- **Generative recommendation** is the new frontier: UniSID, GenRec, IntSR all use next-token prediction
- **Attention sink** theory applied to CTR (CTR-Sink) addresses fundamental LM-recommendation mismatch
- **Multi-agent LLM** architectures for user understanding (MoMoREC) gaining traction at Taobao scale
- **Scaling laws** confirmed for CTR: SparseCTR shows scaling across 3 orders of magnitude
- **LLM embeddings** in production: TreeBridge deployed at Shopee (+1.55% GMV)

### 12.3 Generative Models
- **One-step diffusion** making strong progress: MeanFlow FID 3.43 (50–70% improvement)
- **Unified multimodal** models: TUNA, Molmo2 push understanding+generation in single framework
- **3D generation** at scale: SAM 3D (Meta), O-Voxel (Microsoft) achieving production quality
- **DiT architecture** dominance continues: AlignedGen discovers RoPE conflicts as root cause of attention sharing failure

### 12.4 Theoretical Foundations
- **Transformers' expressiveness** formally characterized (succinctness, EXPSPACE-completeness)
- **Muon optimizer** gets principled improvement (Polar Express)
- **Multi-turn LLM degradation** quantified at 39% average drop
- **Memorization** in LLMs distinguished into intended vs unintended

### 12.5 Industry Deployments

| Company | Paper | Deployment Scale | Impact |
|---------|-------|-----------------|--------|
| Meta | SAM 3D | Production model | 5:1 human preference |
| Shopee | TreeBridge | Hundreds of millions users | +1.55% GMV |
| Taobao | MoMoREC | 88VIP Best-seller List | +6.3% GMV |
| Kuaishou | MARS | Mainstream traffic | +0.728% app usage |
| Kuaishou | GR4AD | Ad system | +4.2% ad revenue |
| LinkedIn | LLM Retrieval | Ads system | +0.45% topline |
| JD.com | GenRec | JD App | +9.5% clicks, +8.7% transactions |
| Meituan | SparseCTR | Production | +1.72% CTR, +1.41% CPM |

---

## Appendix: Conference Coverage Matrix

| Category | ICML'26 | ICLR'26 | CVPR'26 | AAAI'26 | NeurIPS'25 | KDD'26 | ACL'26 | WWW'26 | SIGIR'26 |
|----------|---------|---------|---------|---------|------------|--------|--------|--------|----------|
| LLM Agents | ★★★★★ | ★★★★ | ★★ | ★★★ | ★★ | ★★ | ★★★★ | ★★★ | ★★★ |
| Recommendation | ★★ | ★★★ | ★ | ★★★★ | ★★ | ★★★★★ | ★★★ | ★★★★★ | ★★★★ |
| CTR/Ads | ★ | ★★ | ★ | ★★★ | ★ | ★★★★★ | ★★ | ★★★★ | ★★★ |
| Generative Models | ★★★★★ | ★★★ | ★★★★★ | ★★ | ★★★★★ | ★ | ★ | ★ | ★ |
| 3D Vision | ★ | ★★ | ★★★★★ | ★ | ★★★★ | ★ | ★ | ★ | ★ |
| Sequential Modeling | ★★★ | ★★★ | ★★ | ★★ | ★★ | ★★★ | ★★★ | ★★★ | ★★ |
| Games | ★★ | ★★ | ★ | ★ | ★ | ★ | ★★ | ★ | ★ |
| Benchmarks | ★★★ | ★★★ | ★★ | ★★ | ★★ | ★★★ | ★★★ | ★★ | ★★ |
