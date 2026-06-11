---
title: "arXiv Daily — 2026-06-11"
type: synthesis
created: 2026-06-11
updated: 2026-06-11
sources: []
tags: [arxiv-daily, llm, recommendation, ctr, games, sequential-modeling, reinforcement-learning, diffusion]
---

# arXiv Daily — 2026-06-11

Recent papers spanning AI, LLMs, recommendation systems, CTR prediction, sequential modeling, games, and related areas. Papers are primarily from June 2026 submissions.

---

## LLMs & Architectures

### 1. Redesign Mixture-of-Experts Routers with Manifold Power Iteration
- **Authors**: Songhao Wu, Ang Lv, Ruobing Xie, Yankai Lin
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.12397
- **Abstract**: Proposes aligning each router row with the principal singular direction of its associated expert in MoE models. Introduces a "Power-then-Retract" paradigm (Manifold Power Iteration) that drives router rows toward principal singular directions. Pretrained MoE models from 1B to 11B show consistent gains.
- **Key Innovations**: Theoretical alignment principle for MoE routers; power iteration + retraction for stable training.

### 2. nD-RoPE: A Generalized RoPE for n-Dimensional Position Embedding
- **Authors**: Boyang Li, Yulin Wu, Sizhe Xu, Nuoxian Huang, Zhonghang Yuan, Shangyi Guo, Shu Yang, Takahiro Yabe
- **Institution**: — (ICML 2026)
- **Link**: https://arxiv.org/abs/2606.12146
- **Abstract**: Extends Rotary Position Embedding (RoPE) to arbitrary dimensions with a decomposition-free formulation. Proposes multi-scale regular-simplex wave-vector design for isotropic, directionally balanced position encoding. Consistent gains across images, videos, and point clouds.
- **Key Innovations**: Unified n-dimensional RoPE; spectral condition for isotropy; simplex wave-vector design.

### 3. Breaking Entropy Bounds: Accelerating RL Training via MTP with Rejection Sampling (Bebop)
- **Authors**: Yucheng Li, Huiqiang Jiang, Yang Xu, Jianxin Yang, et al. (Alibaba/Qwen team)
- **Institution**: Alibaba
- **Link**: https://arxiv.org/abs/2606.12370
- **Abstract**: Reveals that MTP acceptance rate in RL training is bounded by model entropy with a negative linear relationship. Proposes probabilistic rejection sampling and end-to-end TV loss to achieve up to 95% acceptance rate and 1.8x end-to-end acceleration on Qwen3.5/3.6/3.7 models.
- **Key Innovations**: Entropy-bound analysis of MTP in RL; TV loss for multi-step rejection sampling; pre-RL MTP training eliminates online MTP updating.

### 4. Re-evaluating Confidence Remasking in Masked Diffusion Language Models
- **Authors**: Stipe Frkovic, Metod Jazbec, Dan Zhang, Christian A. Naesseth, Ilija Bogunovic, Eric Nalisnick
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.12232
- **Abstract**: Revisits WINO (post-hoc confidence-based remasking for masked diffusion LLMs). Finds that under standard decoding (shorter block lengths), remasking brings little benefit over confidence-based unmasking alone, and can exacerbate diversity collapse under non-greedy decoding.
- **Key Innovations**: Critical evaluation of diffusion LLM remasking; highlights setting-dependent nature of benefits.

### 5. Architecture-Aware Reinforcement Learning Makes Sliding-Window Attention Competitive in Math Reasoning (SWARR)
- **Authors**: Kai Liu, Peijie Dong, Xinchen Xie, Jianfei Gao, Qipeng Guo, Xiaowen Chu, Shaoting Zhang, Kai Chen
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.11634
- **Abstract**: Shows that on-policy RL can close the accuracy gap between sliding-window attention (SWA) and full self-attention (SA) for math reasoning. SWA underperforms after SFT due to data-architecture mismatch, but RL adaptation recovers most lost accuracy while preserving linear-complexity benefits.
- **Key Innovations**: Empirical finding that RL changes viability conclusion for SWA; two-stage SFT+RL recipe.

### 6. Position: Hippocampal Explicit Memory Is the Cornerstone for AGI
- **Authors**: Sangjun Park
- **Institution**: — (ICML 2026 Position Paper)
- **Link**: https://arxiv.org/abs/2606.11245
- **Abstract**: Argues that LLMs' learning mechanism is analogous to human implicit memory, but AGI requires hippocampal explicit memory for long-term planning, metacognition, and symbolic reasoning. Draws on neuroscience to propose computational requirements for artificial explicit memory.
- **Key Innovations**: Neuroscientific framing of LLM limitations; explicit memory as necessary condition for AGI.

---

## Agentic RL & Reasoning

### 7. APPO: Agentic Procedural Policy Optimization
- **Authors**: Xucong Wang, Ziyu Ma, Yong Wang, Yuxiang Ji, Shidong Yang, Guanhua Chen, Pengkun Wang, Xiangxiang Chu
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.12384
- **Abstract**: Shifts branching and credit assignment in agentic RL from coarse interaction units to fine-grained decision points. Uses a Branching Score combining token uncertainty with policy-induced likelihood gains. Introduces procedure-level advantage scaling. Improves strong baselines by ~4 points on 13 benchmarks.
- **Key Innovations**: Fine-grained branching locations beyond tool-call boundaries; Branching Score for targeted exploration.

### 8. SVoT: State-aware Visualization-of-Thought for Spatial Reasoning via Reinforcement Learning
- **Authors**: Chao Lei, Yanbei Jiang, Markus Hiller, Zhijian Zhou, Xunye Tian, Krista A. Ehinger, Nir Lipovetzky
- **Institution**: — (Preprint)
- **Link**: https://arxiv.org/abs/2606.11770
- **Abstract**: RL framework generating interleaved, verifiable intermediate states and visualizations for multi-hop spatial reasoning. Trained via GRPO with transition-aware supervision. Introduces Pacman and Gather domains. Up to 65% absolute accuracy gain on OOD test sets.
- **Key Innovations**: State-aware Visualization-of-Thought; transition-aware reward design; new spatial reasoning benchmarks.

---

## CTR Prediction & Advertising

### 9. CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors**: David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, et al. (LinkedIn)
- **Institution**: LinkedIn
- **Link**: https://arxiv.org/abs/2602.11410
- **Abstract**: End-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Key innovations: context-conditioned decoding with multi-tower prediction heads (resolving CTR-ranking chicken-and-egg), self-gated attention, timestamp-based RoPE, session masking. 11.04% CTR lift vs production LiRank baseline. Deployed on LinkedIn's main feed.
- **Key Innovations**: First decoder-only transformer for ads CTR at scale; post-scoring signal modeling; production engineering for industrial workloads.

---

## Recommendation Systems

### 10. Atomic Intent Reasoning: Bringing LLM Semantics to Industrial Cross-Domain Recommendations (AIR)
- **Authors**: Zhuohang Jiang, Yuxin Chen, Shijie Wang, Haohao Qu, Zhou Jindong, Wenqi Fan, Li Qing, Dongxu Liang, Jun Wang
- **Institution**: Kuaishou / The Hong Kong Polytechnic University
- **Link**: https://arxiv.org/abs/2606.10357
- **Abstract**: LLM-driven cross-domain recommendation framework for content-to-e-commerce. Migrates LLM inference to offline phase with dynamic online retrieval/composition, achieving ~400x inference acceleration. +3.446% GMV in Kuaishou online A/B test. Accepted at KDD 2026.
- **Key Innovations**: Offline LLM inference + online retrieval for cross-domain rec; industrial-scale deployment with significant GMV lift.

### 11. DiffCold: A Diffusion-based Generative Model for Cold-Start Item Recommendation
- **Authors**: Kangning Zhang, Yingjie Qin, Weinan Zhang, Yong Yu, Jianghao Lin
- **Institution**: Shanghai Jiao Tong University
- **Link**: https://arxiv.org/abs/2606.12245
- **Abstract**: Resolves the seesaw dilemma (improving cold items harms warm items) via conditional diffusion that reconstructs warm item embeddings from content. Uses Retrieval-enhanced Aggregator and Simulation-based Representation Alignment. Accepted at ECML-PKDD 2026.
- **Key Innovations**: Diffusion model for unified warm/cold representations; seesaw dilemma analysis; retrieval-enhanced diffusion initialization.

### 12. Mult-DPO: Multinomial Direct Preference Optimization for Recommender Systems
- **Authors**: Yaochen Zhu, Harald Steck, James McInerney, Aditya Sinha, Yinhan He, Nathan Kallus, Jundong Li
- **Institution**: Netflix / University of Virginia
- **Link**: https://arxiv.org/abs/2606.10078
- **Abstract**: Extends DPO from pairwise to set-wise preferences (multiple positive items per context) using a Plackett-Luce model. Proposes tractable multinomial surrogate likelihood with closed-form DPO-style objective. Proves it upper-bounds marginalized PL-DPO loss.
- **Key Innovations**: Set-wise preference alignment for recsys; tractable multinomial DPO; theoretical bound analysis.

### 13. Generative Archetype-Grounded Item Representations for Sequential Recommendation (GenAIR)
- **Authors**: Yifan Li, Jiahong Liu, Xinni Zhang, Hao Chen, Yankai Chen, Wenhao Yu, Jianting Chen, Irwin King
- **Institution**: The Chinese University of Hong Kong
- **Link**: https://arxiv.org/abs/2606.11023
- **Abstract**: Uses LLMs to infer "Archetype" text (ideal target audience profile for each item), extracts embeddings, then calibrates with behavioral signals. Seamless integration with existing sequential rec models. Accepted as WWW 2026 Oral.
- **Key Innovations**: Archetype-grounded item representations; behavioral calibration bridging semantic-behavioral gap.

### 14. Gryphon: A Unified Architecture for Semantic-ID Generation and Item-Level Scoring in Industrial Recommendations
- **Authors**: Daria Tikhonovich, Oleg Sorokin, Vladislav Dodonov, Mariia Ulianova, Ilya Murzin
- **Institution**: — (industrial music service)
- **Link**: https://arxiv.org/abs/2606.08604
- **Abstract**: Encoder-decoder generative retrieval architecture with jointly trained item-level scoring. Replaces beam-likelihood ranking with direct item re-scoring, sidestepping miscalibrated sequence scores. +3.7% Recall@1000 over vanilla GR. Replaced 15+ candidate generators + preranking in A/B test with no significant listening time change.
- **Key Innovations**: Item-level scoring for generative retrieval; resolves SID collision problem; simplifies industrial candidate generation pipeline.

---

## Ranking & Allocation

### 15. Representation Curriculum: Stagewise Training for Robust Ranking and Allocation
- **Authors**: Ehsan Ebrahimzadeh, Sina Baharlouei, Abraham Bagherjeiran
- **Institution**: — (KDD 2026)
- **Link**: https://arxiv.org/abs/2606.09891
- **Abstract**: Training-time intervention that stages feature utilization: foregrounds content-based merit signals first, then introduces exposure-dependent belief signals while anchoring the content pathway. Closed-form solutions in Gaussian linear ridge setting. Gains on cold-start populations with controlled head trade-off.
- **Key Innovations**: Curriculum learning for ranking systems; mitigates shortcut reliance on exposure-confounded signals; theoretical guarantees.

---

## Games

### 16. Nonslop: A Gamified Experiment in Human-AI Collaborative Writing
- **Authors**: Maria Edwards, Julian Togelius
- **Institution**: New York University
- **Link**: https://arxiv.org/abs/2606.12350
- **Abstract**: Gamified writing experiment (74 participants, 214 responses) where AI suggestions are available but disincentivized. Studies when users maintain creative autonomy vs. accept AI assistance. Accepted at IEEE CoG 2026.
- **Key Innovations**: Gamified framework for studying authentic human-AI interaction; inversion of "helpful assistant" paradigm.

### 17. RePAIR: Predictive Self-Supervised Representation Learning in Chess
- **Authors**: Christoph Koller, Johannes Fürnkranz, Timo Bertram
- **Institution**: Johannes Kepler University Linz
- **Link**: https://arxiv.org/abs/2606.11860
- **Abstract**: Combines MAE, JEPA, and BERT into a self-supervised architecture for sequential game states. Masks portions of latent state sequences and repairs gaps in embedding space. Meaningful chess concepts emerge in latent space without RL. Accepted as oral at IEEE CoG 2026.
- **Key Innovations**: Hybrid MAE+JEPA+BERT for sequential game states; self-supervised chess representation learning without RL.

---

## Summary of Trends

1. **MoE architectures** continue to mature — principled router design via manifold methods.
2. **Position encoding** gets a unified theoretical treatment (nD-RoPE).
3. **RL for LLMs** is a major focus: accelerating RL training (Bebop), improving agentic RL (APPO), and adapting architectures (SWARR).
4. **Diffusion models** enter recommendation (DiffCold) and are critically evaluated for language (WINO remasking).
5. **CTR/Advertising** sees decoder-only Transformer architectures deployed at scale (CADET at LinkedIn).
6. **Cross-domain recommendation** increasingly leverages LLM semantics offline + fast retrieval online (AIR at Kuaishou).
7. **Set-wise preference alignment** (Mult-DPO) generalizes DPO beyond pairwise for recsys.
8. **Generative retrieval** in recommendation moves toward hybrid approaches combining SID generation with item-level scoring (Gryphon).
9. **Games research** explores self-supervised representation learning (RePAIR) and human-AI collaborative creativity (Nonslop).
10. **AGI theory** draws from neuroscience — explicit memory as a missing piece (ICML 2026 Position Paper).
