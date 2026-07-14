---
title: "arXiv AI Search — Recent Papers Report"
type: synthesis
created: 2026-07-14
updated: 2026-07-14
tags: [arxiv, ai-search, llm, recommendation, ctr, sequential-modeling, game-theory, advertising]
---

# arXiv Recent Papers Report — 2026-07-14

Curated from arXiv submissions across AI, LLMs, Recommendation Systems, CTR Prediction, Sequential Modeling, Advertising, and Game Theory.

---

## 1. Large Language Models (LLMs)

### 1.1 MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning
- **Authors**: (not specified in abstract)
- **Institution**: —
- **Abstract**: Proposes a modular instruction memory with learnable selection mechanism to enable self-improving LLM reasoning. The system selectively retrieves and applies relevant instructions for improved reasoning performance.
- **Key Innovations**: Modular instruction memory architecture; learnable selection for self-improving reasoning.
- **Link**: [arXiv:2607.06974](https://arxiv.org/abs/2607.06974v1)
- **Date**: 2026-07-08

### 1.2 Language Models Guide Symbolic Equation Discovery by Controlling Search
- **Authors**: Xie, Man Luo, Jun et al.
- **Institution**: —
- **Abstract**: Tests a division of labor where LLMs shape hypothesis exploration via search control (specifying variables, operators, search depth) while symbolic regression enumerates and fits expressions. Implemented as LLM-PySR, search control achieved the strongest balance of accuracy, complexity, stability, and cost across 74 AI-Feynman equations and seven complex formula-recovery tasks.
- **Key Innovations**: LLM-PySR — LLM as search controller rather than equation proposer; deterministic metrics govern retention; discovered compact piecewise-linear relation on battery dataset.
- **Link**: [arXiv:2607.04156](https://arxiv.org/abs/2607.04156v1)
- **Date**: 2026-07-05

### 1.3 LLM-as-a-Verifier: A General-Purpose Verification Framework
- **Authors**: (multiple, not fully specified)
- **Institution**: —
- **Abstract**: Identifies verification as a new scaling axis for LLMs. Computes expectation over scoring token logits to generate continuous scores (vs. discrete scores). Scales along (1) score granularity, (2) repeated evaluation, (3) criteria decomposition. Achieves SOTA on Terminal-Bench V2 (86.5%), SWE-Bench Verified (78.2%), RoboRewardBench (87.4%), MedAgentBench (73.3%). Also usable as dense reward signal for RL.
- **Key Innovations**: Probabilistic scoring via logit expectations; multi-axis verification scaling; cost-efficient ranking algorithm; usable as trajectory reward model.
- **Link**: [arXiv:2607.05391](https://arxiv.org/abs/2607.05391)
- **Date**: 2026-07

### 1.4 Set Diffusion: Interpolating Token Orderings Between Autoregression and Diffusion
- **Authors**: (not specified in abstract)
- **Institution**: —
- **Abstract**: Proposes a diffusion-based approach that interpolates between autoregressive and diffusion decoding for fast and flexible token generation.
- **Key Innovations**: Hybrid autoregressive-diffusion decoding; flexible token ordering.
- **Link**: [arXiv:2607.01775](https://arxiv.org/abs/2607.01775v1)
- **Date**: 2026-07-02

### 1.5 Legible-by-Construction: Attention and End-to-End Transformers
- **Authors**: Oskin
- **Institution**: —
- **Abstract**: Makes transformer attention and FFN layers legible by construction via sigmoid-bounded values and Boolean attention. At 125M params, 44–62% of value channels become crisp, contextually selective detectors. End-to-end legible LM achieves parity with conventional baseline on LAMBADA and BLiMP while all feed-forward units are named set/quantifier operations.
- **Key Innovations**: Legible-by-construction attention via bounded values; Boolean attention with explicit logical operations; end-to-end legible LM where internal computation is directly interpretable.
- **Link**: [arXiv:2607.04319](https://arxiv.org/html/2607.04319)
- **Date**: 2026-07

### 1.6 Synthetic Consumer Insight Generation with Large Language Models
- **Authors**: Stephen L. France et al.
- **Institution**: —
- **Abstract**: Tests whether LLMs can generate synthetic consumer data for projective techniques (eliciting associations, emotions, wants). Compares human and LLM responses using linguistic measures, diversity metrics, topic models. Finds substantial overlap in broad topics but important differences in style and diversity generation.
- **Key Innovations**: LLM-generated synthetic consumer data for projective techniques; systematic evaluation across prompts, models, temperatures.
- **Link**: [arXiv:2607.05761](https://arxiv.org/abs/2607.05761v1)
- **Date**: 2026-07-07

---

## 2. Recommendation Systems

### 2.1 SaFeAU: Semantic Factor Learning for Collaborative Filtering
- **Authors**: Yajie Yu, Chenzhong Bin, Zhoubo Xu, Zhixin Zeng, Tongxin Xu, Cihan Xia et al.
- **Institution**: —
- **Abstract**: Proposes Semantic Factor enhanced Alignment and Uniformity (SaFeAU) that augments interacted instances with semantic factors to mitigate false negative labeling. Semantic Factor Routing disentangles items into independent semantic factors; Semantic Factor Matching identifies potential positive pairs; Semantic Pairs Alignment aligns and promotes uniformity. Outperforms GCN-based and MF-based SOTA on four sparse datasets.
- **Key Innovations**: Semantic factor routing for disentangled representations; mitigation of false negative samples via semantic matching; no graph neighborhood aggregation needed.
- **Link**: [arXiv:2605.31414](https://arxiv.org/html/2605.31414)
- **Date**: 2026-05-29

### 2.2 SIF: Sample Is Feature — Toward Sample-Level Tokens for Unified Large Recommender Models
- **Authors**: Shuli Wang
- **Institution**: —
- **Abstract**: Encodes each historical Raw Sample directly into a sequence token via Sample Tokenizer with hierarchical group-adaptive quantization (HGAQ). SIF-Mixer performs deep feature interaction over homogeneous sample representations. Deployed on industrial food delivery platform.
- **Key Innovations**: Sample-level tokenization (beyond item-level); HGAQ for efficient sample quantization; resolves heterogeneity between sequential and non-sequential features.
- **Link**: [arXiv:2604.15650](https://arxiv.org/abs/2604.15650)
- **Date**: 2026-04-17

### 2.3 Gryphon: Unified Semantic-ID Generation and Item-Level Scoring for Industrial Recommendations
- **Authors**: Daria Tikhonovich, Oleg Sorokin, Vladislav Dodonov, Mariia Ulianova, Ilya Murzin
- **Institution**: Industrial music service (likely Yandex)
- **Abstract**: Encoder-decoder generative recommendation that adds jointly trained item-level scoring alongside SID generation. Re-scores generated SIDs to resolve collisions and sidestep miscalibrated sequence scores. Deployed as sole candidate source in 7-day A/B test, replacing 15+ candidate generators.
- **Key Innovations**: Item-level scoring in generative retrieval; SID collision resolution; single forward pass for user representation; production deployment replacing complex pipeline.
- **Link**: [arXiv:2606.08604](https://arxiv.org/html/2606.08604)
- **Date**: 2026-06-07

### 2.4 STAR: Internalizing Multi-Agent Reasoning for LLM-based Recommendation
- **Authors**: Yang Wu, Hao Wang, Qian Li, Jun Zhang, Huan Yu, Jie Jiang
- **Institution**: —
- **Abstract**: Single-agent Trajectory-Aligned Recommender distills multi-agent reasoning (planning, tool usage, self-reflection) into a single efficient model via trajectory-driven distillation. Multi-Agent Recommender System (MARS) with Collaborative Signal Translation verbalizes latent behavioral patterns. STAR surpasses teacher by 8.7%–39.5% while eliminating iterative latency.
- **Key Innovations**: Collaborative Signal Translation (graph → natural language); trajectory-driven distillation (SFT + GRPO); internalizing agentic capabilities into single model.
- **Link**: [arXiv:2602.09829](https://arxiv.org/pdf/2602.09829)
- **Date**: 2026-02-10

### 2.5 Beyond Interleaving: Causal Attention Reformulations for Generative Recommender Systems
- **Authors**: (Meta/industry researchers)
- **Institution**: Major social network (likely Meta)
- **Abstract**: Reformulates generative recommendation by aligning sequence modeling with causal structure. Introduces AttnLFA (causal attention pooling) and AttnMVP (mixed-value early fusion) eliminating interleaved item-action tokens. Reduces sequence complexity by 50%, training time by 12–23%, with consistent loss/NE improvements.
- **Key Innovations**: Causal attention reformulation eliminating token interleaving; 50% sequence reduction; information-theoretic attention noise reduction; strict causal masking.
- **Link**: [arXiv:2603.10369](https://arxiv.org/pdf/2603.10369v1)
- **Date**: 2026-03

### 2.6 Deep Research for Recommender Systems
- **Authors**: Kesha Ou, Chenghao Wu, Xiaolei Wang, Bowen Zheng, Wayne Xin Zhao et al.
- **Institution**: Renmin University of China
- **Abstract**: Comprehensive survey/study on using LLMs for deep research in recommender systems, tracing progression from collaborative filtering to complex neural models.
- **Key Innovations**: Systematic framework for LLM-augmented recommendation research.
- **Link**: [arXiv:2603.07605](https://arxiv.org/abs/2603.07605)
- **Date**: 2026-03-08

### 2.7 VAE Recommenders: Collaborative Learning Mechanisms and PIA
- **Authors**: Vuong Tung-Long, Monteil Julien, Dang Hien et al.
- **Institution**: Amazon
- **Abstract**: Analyzes how collaboration arises in VAE-CF — governed by latent proximity with a sharing radius. Proposes Personalized Item Alignment (PIA) regularizer that stabilizes geometry under masking and promotes semantically grounded global mixing. Deployed on Amazon streaming platform.
- **Key Innovations**: Theoretical analysis of VAE-CF collaboration mechanisms; PIA regularizer with item anchors; successful online A/B test on Amazon.
- **Link**: [arXiv:2511.06781](https://arxiv.org/pdf/2511.06781)
- **Date**: 2025-11

### 2.8 Cold-Starts in Generative Recommendation: A Reproducibility Study
- **Authors**: Zhang Zhen et al.
- **Institution**: — (SIGIR 2026)
- **Abstract**: Systematic reproducibility study of generative recommendation under cold-start protocols. Finds: (i) cold-start is asymmetric (item cold-start much harder); (ii) scaling model size yields marginal gains; (iii) identifier design is decisive (textual IDs help item cold-start but hurt warm/user cold-start); (iv) RL does not consistently improve cold-start.
- **Key Innovations**: Controlled analysis isolating model scale, identifier design, training strategy; compositional semantic coding (OPQ) as robust middle ground.
- **Link**: [arXiv:2603.29845](https://arxiv.org/html/2603.29845v2)
- **Date**: 2026-03 (SIGIR 2026)

### 2.9 ProMax: LLM-derived Profiles with Distribution Shaping for Recommender Systems
- **Authors**: Yi Zhang, Yiwen Zhang, Kai Zheng, Tong Chen, Hongzhi Yin
- **Institution**: —
- **Abstract**: Explores using LLM-derived user profiles with distribution shaping techniques for improved recommendation.
- **Key Innovations**: LLM-derived profiles; distribution shaping for profile enhancement.
- **Link**: [arXiv:2604.26231](https://arxiv.org/html/2604.26231)
- **Date**: 2026-04-29

---

## 3. CTR Prediction & Advertising

### 3.1 CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer
- **Authors**: David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, Liuqing Li et al.
- **Institution**: LinkedIn
- **Abstract**: End-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Key innovations: context-conditioned decoding with multi-tower heads (resolving chicken-and-egg between CTR and ranking); self-gated attention; timestamp-based RoPE; session masking for train-serve skew; tensor packing and custom Flash Attention kernels. Achieves 11.04% CTR lift in online A/B test vs. LiRank baseline.
- **Key Innovations**: Context-conditioned multi-tower prediction heads; self-gated attention; temporal RoPE; session masking; production engineering (tensor packing, Flash Attention).
- **Link**: [arXiv:2602.11410](https://arxiv.org/pdf/2602.11410)
- **Date**: 2026-02-11

### 3.2 EST: Efficiently Scalable Transformer for CTR Prediction
- **Authors**: Mingyang Liu, Yong Bai, Zhangming Chan, Sishuo Chen, Xiang-Rong Sheng, Han Zhu et al.
- **Institution**: Alibaba/Taobao
- **Abstract**: Fully unified modeling processing all raw inputs in single sequence. Lightweight Cross Attention (LCA) prunes redundant self-interactions; Content Sparse Attention (CSA) dynamically selects high-signal behaviors. Exhibits stable power-law scaling. Deployed on Taobao display advertising: 3.27% RPM increase, 1.22% CTR lift.
- **Key Innovations**: Fully unified modeling without lossy aggregation; power-law scaling in CTR; LCA + CSA for efficiency; deployed on Taobao.
- **Link**: [arXiv:2602.10811](https://arxiv.org/pdf/2602.10811)
- **Date**: 2026-02-11

### 3.3 IDProxy: Cold-Start CTR Prediction at Xiaohongshu with Multimodal LLMs
- **Authors**: (Xiaohongshu team)
- **Institution**: Xiaohongshu
- **Abstract**: Leverages multimodal LLMs to generate proxy embeddings from content signals for cold-start CTR prediction. Proxies aligned with existing ID embedding space, optimized end-to-end. Deployed in Content Feed and Display Ads serving hundreds of millions daily.
- **Key Innovations**: MLLM-generated proxy embeddings; end-to-end alignment with ID embedding space; cold-start solution for new items.
- **Link**: [arXiv:2603.01590](https://arxiv.org/abs/2603.01590v1)
- **Date**: 2026-03-02

### 3.4 PRECTR-V2: Unified Relevance-CTR Framework
- **Authors**: Shuzhi Cao, Rong Chen, Ailong He, Shuguang Han, Jufeng Chen
- **Institution**: —
- **Abstract**: Unified framework for search relevance and CTR prediction. Cross-user relevance preference mining for cold-start; exposure bias correction via embedding noise injection and pairwise loss; lightweight transformer encoder distilled from LLM for CTR-aligned text encoding.
- **Key Innovations**: Cross-user relevance preference mining; exposure bias correction; LLM-distilled lightweight (2M param) CTR encoder.
- **Link**: [arXiv:2602.20676](https://arxiv.org/pdf/2602.20676)
- **Date**: 2026-02-24

### 3.5 DAIAN: Deep Adaptive Intent-Aware Network for Trigger-Induced Recommendation
- **Authors**: (Alibaba/Xianyu team)
- **Institution**: Alibaba/Xianyu
- **Abstract**: Addresses intent myopia in trigger-induced recommendation. Extracts personalized intent representations from trigger-click correlation; retrieves related historical behaviors; hybrid enhancer with ID and semantic info. Deployed on Xianyu TIR scenario: 1.59% CTR increase, 1.73% diversity increase.
- **Key Innovations**: Intent myopia mitigation; trigger-aware intent distribution modeling; hybrid ID+semantic similarity enhancement.
- **Link**: [arXiv:2602.13971](https://arxiv.org/pdf/2602.13971v1)
- **Date**: 2026-02

### 3.6 DS-MLP: Dual-Stream MLP is All You Need for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution**: Renmin University of China / ByteDance / Meituan
- **Abstract**: Leverages knowledge distillation to consolidate explicit feature interaction into a main MLP, while parallel MLP captures implicit interactions. Two alignment strategies for compatibility. Achieves SOTA on Criteo, Avazu, and a proprietary dataset.
- **Key Innovations**: Knowledge distillation from dual-stream to single MLP; dual alignment strategies; SOTA with vanilla MLP.
- **Link**: [arXiv:2606.04944](https://arxiv.org/pdf/2606.04944v1)
- **Date**: 2026-06

### 3.7 GR4AD: Generative Recommendation for Large-Scale Advertising
- **Authors**: (Kuaishou team)
- **Institution**: Kuaishou
- **Abstract**: Production-oriented generative recommender for advertising. UA-SID (Unified Advertisement Semantic ID) from fine-tuned MLLM; LazyAR decoder relaxing layer-wise dependencies; VSL + RSPO (Ranking-Guided Softmax Preference Optimization) for value-aligned online learning; Dynamic Beam Serving. Deployed on Kuaishou (400M+ users): up to 4.2% ad revenue improvement, 10.17% conversion rate improvement.
- **Key Innovations**: UA-SID from MLLM; LazyAR efficient decoder; RSPO list-wise RL; dynamic beam serving; full production deployment.
- **Link**: [arXiv:2602.22732](https://arxiv.org/abs/2602.22732v2)
- **Date**: 2026-02

### 3.8 GRAB: LLM-Inspired Sequence-First CTR Prediction
- **Authors**: (not specified)
- **Institution**: —
- **Abstract**: Proposes a sequence-first paradigm for CTR prediction inspired by LLM architectures.
- **Key Innovations**: Sequence-first CTR modeling paradigm.
- **Link**: [arXiv:2602.01865](https://arxiv.org/abs/2602.01865v2)
- **Date**: 2026-02

### 3.9 CDNet: Bridging Sequential and Contextual Features for CTR
- **Authors**: (not specified)
- **Institution**: —
- **Abstract**: Core-Behaviors and Distributional-Compensation Dual-View Interaction Network. Fine-grained interaction with most relevant behaviors + coarse-grained interaction modeling overall interest distribution.
- **Key Innovations**: Dual-view interaction: core-behavior fine-grained + distributional coarse-grained.
- **Link**: [arXiv:2603.12578](https://arxiv.org/abs/2603.12578v1)
- **Date**: 2026-03-13

---

## 4. Sequential Modeling

### 4.1 HyTRec: Hybrid Temporal-Aware Attention for Long Behavior Sequential Recommendation
- **Authors**: (not specified)
- **Institution**: —
- **Abstract**: Hybrid attention architecture decoupling long-term stable preferences (linear attention) from short-term intent spikes (softmax attention). Temporal-Aware Delta Network (TADN) upweights fresh signals and suppresses historical noise. 8% Hit Rate improvement for ultra-long sequences.
- **Key Innovations**: Hybrid attention (linear + softmax at 7:1 ratio); TADN with exponential gating; sequence decomposition for long sequences.
- **Link**: [arXiv:2602.18283](https://arxiv.org/pdf/2602.18283v1)
- **Date**: 2026-02-20

### 4.2 SRPFN: One Sequential Recommendation Model Pretrained from Synthetic Priors
- **Authors**: Woosung Kang, Jiwon Jeong, Jonghyeok Shin, Jeongwhan Choi, Noseong Park
- **Institution**: KAIST
- **Abstract**: Prior-data Fitted Network for sequential recommendation — predicts next item in single forward pass without gradient updates on target domain. Pretrained on 25.6M sequences from synthetic prior (hDCSBM). Conditions on support set of item-item transitions at inference. Average 7.53% improvement over second-best method across 5 benchmarks.
- **Key Innovations**: Update-free sequential recommendation; synthetic prior pretraining; single forward pass inference (~1 min per dataset).
- **Link**: [arXiv:2606.15752](https://arxiv.org/pdf/2606.15752v1)
- **Date**: 2026-06

### 4.3 MoS: Mixture of Sequence — Theme-Aware MoE for Long-Sequence Recommendation
- **Authors**: Xiao Lin, Zhicheng Tang, Weilin Cong, Mengyue Hang, Kai Wang, Yajuan Wang et al.
- **Institution**: —
- **Abstract**: Theme-aware MoE that extracts theme-specific multi-scale subsequences from noisy raw sequences. Theme-aware routing learns latent themes; multi-scale fusion uses global, short-term, and theme-specific experts. Addresses session hopping (interests stable within sessions but shift across).
- **Key Innovations**: Theme-aware MoE routing; multi-scale expert fusion; session hopping awareness.
- **Link**: [arXiv:2604.20858](https://arxiv.org/html/2604.20858)
- **Date**: 2026-03-01

### 4.4 AdaTTA: Adaptive Test-Time Augmentation for Sequential Recommendation
- **Authors**: Xibo Li, Liang Zhang
- **Institution**: —
- **Abstract**: RL-based adaptive inference that selects sequence-specific augmentation operators per user sequence. Actor-Critic policy with hybrid state representations and joint macro-rank reward. Up to 26.31% improvement on Home dataset.
- **Key Innovations**: RL-based per-sequence augmentation selection; addresses behavioral heterogeneity across users.
- **Link**: [arXiv:2604.16121](https://arxiv.org/abs/2604.16121)
- **Date**: 2026-04-17

### 4.5 MVCrec: Multi-View Contrastive Learning for Sequential Recommendation
- **Authors**: (not specified)
- **Institution**: —
- **Abstract**: Integrates ID-based sequential and graph-based views via three contrastive objectives (within sequential, within graph, across views). Multi-view attention fusion with global and local attention. Up to 14.44% NDCG@10 improvement.
- **Key Innovations**: Cross-view contrastive learning (ID ↔ graph); multi-view attention fusion.
- **Link**: [arXiv:2604.14114](https://arxiv.org/abs/2604.14114v1)
- **Date**: 2026-04-15

### 4.6 FLAME: Condensing Ensemble Diversity into Single Network for Efficient Sequential Rec
- **Authors**: (not specified)
- **Institution**: — (SIGIR 2026)
- **Abstract**: Frozen + Learnable networks with Aligned Modular Ensemble. Two networks simulate exponential diversity via modular combinations; contrastive alignment into unified space. Only learnable network used at inference. 7.69× faster convergence, 9.70% NDCG@20 improvement.
- **Key Innovations**: Modular ensemble from 2 networks; frozen anchor for stability; zero-overhead inference.
- **Link**: [arXiv:2604.04038](https://arxiv.org/html/2604.04038v1)
- **Date**: 2026-04 (SIGIR 2026)

### 4.7 Efficient Sequential Recommendation via Personalization (PerSRec)
- **Authors**: (Meta/Facebook Research)
- **Institution**: Meta
- **Abstract**: Compresses long interaction histories into learnable personalized expert tokens combined with recent interactions. Applied to HSTU and HLLM, maintains performance with dramatically reduced sequence length.
- **Key Innovations**: Personalized expert tokens for sequence compression; applicable to multiple SoTA architectures.
- **Link**: [arXiv:2601.03479](https://arxiv.org/abs/2601.03479v1)
- **Date**: 2026-01

### 4.8 GenLI: Generative Long-term User Interest Modeling for CTR
- **Authors**: (not specified)
- **Institution**: —
- **Abstract**: Interest generation module (IGM) generates multiple interest distributions; behavior retrieval module (BRM) uses simple lookup O(1); interest fusion module (IFM) uses gating mechanisms. Avoids complex matching-based retrieval.
- **Key Innovations**: Generative interest distribution modeling; O(1) behavior retrieval; target-independent interest generation.
- **Link**: [arXiv:2605.15905](https://pubdb.com/paper/2605.15905)
- **Date**: 2026-05

---

## 5. Game Theory & Multi-Agent Systems

### 5.1 Competition and Cooperation of LLM Agents in Games
- **Authors**: (not fully specified)
- **Institution**: —
- **Abstract**: Studies LLM agent interactions in network resource allocation and Cournot competition games. LLM agents tend to cooperate (not converge to Nash equilibria) when given multi-round prompts and non-zero-sum context. Fairness reasoning is central to this behavior. Proposes analytical framework capturing dynamics of LLM reasoning.
- **Key Innovations**: Discovery of LLM cooperation tendency; fairness as central reasoning mechanism; analytical framework for LLM strategic behavior.
- **Link**: [arXiv:2604.00487](https://arxiv.org/abs/2604.00487v1)
- **Date**: 2026-04

### 5.2 Regret Minimization with Adaptive Opponents in Repeated Games
- **Authors**: (not specified)
- **Institution**: — (COLT 2026)
- **Abstract**: Introduces Repeated Policy Regret (RP-Regret) for repeated games with adaptive opponents. Three minimization algorithms. Shows RP-Regret minimization leads to subgame perfect equilibria. Demonstrates more cooperative solutions with higher utility in Stag-Hunt.
- **Key Innovations**: RP-Regret metric for adaptive opponents; three provable minimization algorithms; equilibrium computation via regret minimization.
- **Link**: [arXiv:2606.06486](https://arxiv.org/html/2606.06486v1)
- **Date**: 2026-06 (COLT 2026)

### 5.3 Parametric Open Source Games
- **Authors**: Aleksandar Todorov, Jesse ten Napel, Alexander Müller
- **Institution**: —
- **Abstract**: Continuous analogue of program equilibria where players choose parameter vectors and semantics maps convert them to mixed actions. Derives exact cooperation threshold in symmetric 2×2 games; first-order cooperation condition governed by cross-player to self-player sensitivity ratio. Neural semantics class shows same organizing principle.
- **Key Innovations**: Parametric open-source games framework; analytical cooperation threshold; neural semantics with sensitivity-ratio criterion.
- **Link**: [arXiv:2606.27068](https://arxiv.org/pdf/2606.27068)
- **Date**: 2026-06

### 5.4 Learning to Recommend in Unknown Games
- **Authors**: Arwa Alanqary, Zakaria Baba, Manxi Wu, Alexandre M. Bayen
- **Institution**: UC Berkeley
- **Abstract**: Studies preference learning through recommendations in multi-agent games with unknown utilities. Shows quantal-response feedback enables learnability (logarithmic sample complexity); best-response feedback identifies a larger indistinguishable set. Designs online algorithm with O(nM log(T)) regret.
- **Key Innovations**: Learnability theory for recommendation in strategic settings; quantal-response vs best-response feedback characterization; cutting-plane algorithm with logarithmic regret.
- **Link**: [arXiv:2602.16998](https://arxiv.org/pdf/2602.16998)
- **Date**: 2026-02-19

### 5.5 NePPO: Near-Potential Policy Optimization for General-Sum MARL
- **Authors**: Addison Kalanther, Sanika Bharvirkar, Shankar P. Sastry, Chinmay Maheshwari
- **Institution**: —
- **Abstract**: Learns a player-independent potential function whose Nash equilibrium approximates that of the original general-sum game. Uses zeroth-order gradient descent. Outperforms MAPPO, IPPO, MADDPG.
- **Key Innovations**: Potential function approximation for general-sum Nash equilibria; zeroth-order optimization pipeline.
- **Link**: [arXiv:2603.06977](https://arxiv.org/pdf/2603.06977)
- **Date**: 2026-03-07

### 5.6 Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén
- **Institution**: —
- **Abstract**: Presents examples of games with RL-augmented game AI and describes practicalities of deploying player-facing machine learning in games.
- **Key Innovations**: Practical deployment of RL-augmented game AI.
- **Link**: [arXiv:2606.20210](https://arxiv.org/abs/2606.20210)
- **Date**: 2026-06-18

### 5.7 Differentiable Normative Guidance for Nash Bargaining Solution Recovery
- **Authors**: (not specified)
- **Institution**: —
- **Abstract**: Guided graph diffusion framework for generating individually rational utility vectors approximating NBS without frontier knowledge. Differentiable composite guidance loss penalizes IR violations and Nash product gaps. 100% IR compliance; 99.45% Nash efficiency on synthetic data.
- **Key Innovations**: Differentiable normative guidance for diffusion; graph attention for negotiation modeling; 100% IR compliance.
- **Link**: [arXiv:2603.29297](https://arxiv.org/abs/2603.29297v1)
- **Date**: 2026-03

---

## Summary Statistics

| Category | Papers | Deployed in Production |
|----------|--------|----------------------|
| LLMs | 6 | — |
| Recommendation | 9 | 4 (LinkedIn, Amazon, Xiaohongshu, industrial music) |
| CTR / Advertising | 9 | 5 (LinkedIn, Taobao, Xiaohongshu, Xianyu, Kuaishou) |
| Sequential Modeling | 8 | 2 (Meta) |
| Game Theory | 7 | — |
| **Total** | **39** | |

## Key Trends

1. **Generative Recommendation is Production-Ready**: Multiple papers (GR4AD, Gryphon, EST) demonstrate generative/transformer-based models deployed at scale with significant business impact.

2. **LLM Integration into RecSys**: LLMs used as encoders (IDProxy), reasoning teachers (STAR), profile generators (ProMax), and verifiers (LLM-as-a-Verifier).

3. **Scaling Laws for CTR**: EST demonstrates power-law scaling for CTR prediction, adapting LLM scaling insights to recommendation.

4. **Efficient Long-Sequence Modeling**: HyTRec, PerSRec, MoS address the quadratic cost of modeling long user behavior sequences through hybrid attention, compression, and MoE.

5. **Game Theory Meets LLMs**: Growing research on LLM strategic behavior (cooperation tendency, fairness reasoning) and game-theoretic frameworks for multi-agent systems.

6. **Cold-Start Solutions**: IDProxy (multimodal LLMs), SaFeAU (semantic factors), and cold-start reproducibility studies push the boundary of handling new items/users.
