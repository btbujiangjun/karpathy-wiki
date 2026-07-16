---
title: "ArXiv Daily Report - 2026-07-16"
type: synthesis
created: 2026-07-16
updated: 2026-07-16
sources: []
tags: [arxiv, daily, AI, LLM, recommendation, advertising, CTR, sequential-modeling, games]
---

# ArXiv Daily Report - 2026-07-16

## Papers

### 1. Dual-Stream MLP is All You Need for CTR Prediction
- **Authors:** Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution/Company:** Renmin University of China, ByteDance, Meituan
- **Abstract:** Proposes DS-MLP, a novel feature interaction framework for CTR prediction that leverages knowledge distillation to consolidate explicit feature interaction into a main MLP network, while a parallel MLP captures implicit feature interactions. Designed with two alignment strategies for enhancing compatibility.
- **Key Innovations:** Knowledge distillation to consolidate explicit feature interaction into a main MLP, parallel MLP for implicit interactions, two alignment strategies, vanilla MLP structure achieving state-of-the-art performance.
- **arXiv Link:** https://arxiv.org/abs/2606.04944

### 2. CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors:** (From LinkedIn research team)
- **Institution/Company:** LinkedIn
- **Abstract:** End-to-end decoder-only transformer for ads CTR prediction with context-conditioned decoding mechanism that accounts for post-scoring signals like ad position. Combines self-gated attention, timestamp-based RoPE, and session-aware masking.
- **Key Innovations:** Context-conditioned decoding architecture with multi-tower prediction heads, self-gated attention mechanism, timestamp-based RoPE, session masking strategies, production engineering techniques for scalable training and low-latency serving.
- **arXiv Link:** https://arxiv.org/abs/2602.11410

### 3. EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling
- **Authors:** (Alibaba research team)
- **Institution/Company:** Alibaba Group (Taobao)
- **Abstract:** Efficiently Scalable Transformer (EST) for fully unified modeling of CTR prediction by processing all raw inputs in a single sequence without lossy aggregation. Integrates Lightweight Cross-Attention and Content Sparse Attention modules.
- **Key Innovations:** Fully unified modeling without lossy aggregation, Lightweight Cross-Attention (LCA) for pruning redundant self-interactions, Content Sparse Attention (CSA) for dynamic selection of high-signal behaviors, stable power-law scaling relationship.
- **arXiv Link:** https://arxiv.org/abs/2602.10811

### 4. Generative Long-term User Interest Modeling for Click-Through Rate Prediction
- **Authors:** Jiangli Shao, Kaifu Zheng, Hao Fang, Huimu Ye, Zhiwei Liu, Bo Zhang, Shu Han, Xingxing Wang
- **Institution/Company:** (Not specified in excerpt)
- **Abstract:** GenLI model for generative long-term user interest modeling with interest generation module (IGM), behavior retrieval module (BRM), and interest fusion module (IFM). IGM generates multiple interest distributions to indicate different aspects of real-time user interests.
- **Key Innovations:** Interest generation module (IGM) for target-independent interest generation, behavior retrieval module (BRM) with O(1) time complexity, interest fusion module (IFM), incorporation of interaction information among behaviors.
- **arXiv Link:** https://arxiv.org/abs/2605.15905

### 5. LoopCTR: Unlocking the Loop Scaling Power for Click-Through Rate Prediction
- **Authors:** Jiakai Tang, Runfeng Zhang, Weiqiu Wang, Yifei Liu, Chuan Wang, Xu Chen, Yeqiu Yang, Jian Wu, Yuning Jiang, Bo Zheng
- **Institution/Company:** Renmin University of China, Alibaba Group
- **Abstract:** Loop scaling paradigm for CTR models that increases training-time computation through recursive reuse of shared model layers, decoupling computation from parameter growth. Adopts sandwich architecture with Hyper-Connected Residuals and Mixture-of-Experts.
- **Key Innovations:** Loop scaling paradigm, sandwich architecture with Hyper-Connected Residuals, Mixture-of-Experts, process supervision at every loop depth, train-multi-loop infer-zero-loop strategy.
- **arXiv Link:** https://arxiv.org/abs/2604.19550

### 6. Trustworthy Recommendation in the Era of Large Language Models: Opportunities and Challenges
- **Authors:** Bohao Wang, Yu Cui, Zhenxiang Xu, Jujia Zhao, Chenxiao Fan, Jizhi Zhang, Weiqin Yang, Shengjia Zhang, Sirui Chen, Yang Zhang, Xiaoyan Zhao, Wenjie Wang, Chongming Gao, Fuli Feng, Xiangnan He, Jiawei Chen
- **Institution/Company:** (Not specified)
- **Abstract:** Systematic review of trustworthy LLM-empowered recommendation analyzing over 200 recent studies. Reveals that LLMs act as a double-edged sword, offering unprecedented opportunities to enhance trustworthiness while introducing new risks.
- **Key Innovations:** Systematic review of 13 opportunities and 18 challenges across six fundamental dimensions of trustworthiness, novel taxonomy for trustworthy LLM-empowered recommendation, comprehensive review of datasets and evaluation metrics.
- **arXiv Link:** https://arxiv.org/abs/2606.00540

### 7. Enriching Semantic Profiles into Knowledge Graph for Recommender Systems Using Large Language Models
- **Authors:** Seokho Ahn, Sungbok Shin, Young-Duk Seo
- **Institution/Company:** (Not specified)
- **Abstract:** SPiKE model that uses LLMs to generate semantic profiles for all KG entities and integrates them into the KG. Consists of entity profile generation, profile-aware KG aggregation, and pairwise profile preference matching.
- **Key Innovations:** Entity profile generation using LLMs to extract compressed rationales, profile-aware KG aggregation for extending profile reach, pairwise profile preference matching for aligning representations during training.
- **arXiv Link:** https://arxiv.org/abs/2601.08148

### 8. Sequence-aware Large Language Models for Explainable Recommendation
- **Authors:** Gangyi Zhang, Runzhe Teng, Chongming Gao
- **Institution/Company:** (Not specified)
- **Abstract:** SELLER framework that integrates explanation generation with utility-aware evaluation using a dual-path encoder capturing both user behavior and item semantics, with a Mixture-of-Experts adapter to align signals with LLMs.
- **Key Innovations:** Dual-path encoder for user behavior and item semantics, Mixture-of-Experts adapter, unified evaluation framework assessing explanations via textual quality and recommendation outcomes, sequence-aware approach.
- **arXiv Link:** https://arxiv.org/abs/2603.24136

### 9. Rec-R1: Bridging Generative Large Language Models and User-Centric Recommendation Systems via Reinforcement Learning
- **Authors:** Jiacheng Lin, Tian Wang, Kun Qian
- **Institution/Company:** (Not specified)
- **Abstract:** Rec-R1 framework that bridges LLMs with recommendation systems through closed-loop optimization using feedback from a fixed black-box recommendation model, without relying on synthetic SFT data from proprietary models.
- **Key Innovations:** Closed-loop optimization using feedback from fixed black-box recommendation model, avoids synthetic SFT data, preserves general-purpose capabilities of LLM, outperforms prompting- and SFT-based methods.
- **arXiv Link:** https://arxiv.org/abs/2503.24289

### 10. Augmenting Game AI with Deep Reinforcement Learning
- **Authors:** Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén
- **Institution/Company:** Electronic Arts (EA), Stockholm, Sweden
- **Abstract:** Vision paper proposing framework for training reinforcement learning models for game AI, addressing believability, sample efficiency, and deployment challenges. Presents examples of games with RL-augmented game AI.
- **Key Innovations:** Framework for RL game AI training with specific requirements for game development, genre-level readiness framework, identification of bottlenecks: sample efficiency, generalization, tension between optimal and believable behavior.
- **arXiv Link:** https://arxiv.org/abs/2606.20210

### 11. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning
- **Authors:** (Not fully specified)
- **Institution/Company:** (Not specified)
- **Abstract:** Self-play framework where models learn by playing multi-turn zero-sum games against continuously improving versions of themselves, generating automatic curriculum of stronger opponents. Produces reasoning capabilities that transfer broadly.
- **Key Innovations:** Self-play framework for automatic curriculum generation, role-conditioned advantage estimation (RAE) for stabilizing multi-agent training, multi-game training (TicTacToe, Kuhn Poker, Simple Negotiation), transferable reasoning capabilities.
- **arXiv Link:** https://arxiv.org/abs/2506.24119

### 12. NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation
- **Authors:** Liao Qu, Yiheng Liu, Hang Chen, Yangyang Song, Yongsheng Dong, Shikun Sun, Xian Li, Xu Wang, Yi Jiang, Hu Ye, Bo Chen, Yiming Gao, Peng Liu, Akide Liu, Zhipeng Yang, Qili Deng, Linjie Xing, Jiyang Liu, Zhao Wang, Yang Zhou, Mingcong Liu, Yi Zhang, Qian He, Xiwei Hu, Zhongqi Qi, Jie Shao, Zhiye Fu, Shuai Wang, Fangmin Chen, Xuezhi Chai, Zhihua Wu, Yitong Wang, Zehuan Yuan, Daniel K. Du, Xinglong Wu
- **Institution/Company:** ByteDance, Tsinghua University, Monash University
- **Abstract:** Unified decoder-only autoregressive transformer trained on 6 trillion interleaved text-image discrete tokens. Natively activates multimodal understanding and generation capabilities with next-token prediction for text and next-scale prediction for visual generation.
- **Key Innovations:** Unified vision representation within unified autoregressive architecture, next-scale prediction for visual generation (orders of magnitude faster than raster-scan), prefix-tuning strategy for reinforcement learning, robust training recipe for multi-scale generation.
- **arXiv Link:** https://arxiv.org/abs/2601.02204

### 13. Efficient Sequential Recommendation for Long Term User Interest Via Personalization
- **Authors:** Qiang Zhang, Hanchao Yu, Ivan Ji, Chen Yuan, Yi Zhang, Chihuang Liu, Xiaolong Wang, Christopher E. Lambert, Ren Chen, Chen Kovacs, Xinzhu Bei, Renqin Cai, Rui Li, Lizhu Zhang, Xiangjun Fan, Qunshu Zhang, Benyu Zhang
- **Institution/Company:** Facebook Research
- **Abstract:** Personalization techniques to compress long user interaction histories into learnable tokens, which are combined with recent interactions to generate recommendations. Significantly reduces computational costs while maintaining high recommendation accuracy.
- **Key Innovations:** Compression of long histories into learnable tokens, combination with recent interactions, application to existing transformer models (HSTU, HLLM), personalization techniques for efficiency and performance.
- **arXiv Link:** https://arxiv.org/abs/2601.03479

### 14. Multi-Behavior Sequential Modeling with Transition-Aware Graph Attention Network
- **Authors:** (Alibaba research team)
- **Institution/Company:** Alibaba Group
- **Abstract:** Transition-Aware Graph Attention Network (TGA) for linear-complexity multi-behavior transition modeling. Constructs structured sparse graph by identifying informative transitions from item-level, category-level, and neighbor-level perspectives.
- **Key Innovations:** Structured sparse graph from three perspectives (item-level, category-level, neighbor-level), transition-aware graph attention mechanism, linear-complexity approach for modeling multi-behavior transitions.
- **arXiv Link:** https://arxiv.org/abs/2601.14955

### 15. Generative Click-through Rate Prediction with Applications to Search Advertising
- **Authors:** Lingwei Kong, Lu Wang, Changping Peng, Zhangang Lin, Ching Law, Jingping Shao
- **Institution/Company:** (Not specified, deployed on large e-commerce platform)
- **Abstract:** Two-stage training process leveraging generative pre-training for next-item prediction to enhance discriminative CTR prediction models. Model deployed on one of the world's largest e-commerce platforms.
- **Key Innovations:** Two-stage training (generative pre-training + discriminative fine-tuning), reconciliation of data aggregation needs for both model types, online A/B testing validation, industrial deployment.
- **arXiv Link:** https://arxiv.org/abs/2507.11246

---

## Summary

This report covers recent arXiv papers in the areas of:

1. **CTR Prediction:** Papers on dual-stream architectures, scaling laws, loop scaling, and generative approaches for click-through rate prediction in advertising and recommendation systems.

2. **Recommendation Systems:** Papers on trustworthy LLM-empowered recommendation, knowledge graph enrichment using LLMs, sequence-aware explainable recommendation, and bridging generative LLMs with recommendation systems via RL.

3. **Sequential Modeling:** Papers on efficient sequential recommendation, multi-behavior sequential modeling, and unified sequential modeling for multimodal understanding.

4. **Games:** Papers on augmenting game AI with deep reinforcement learning and self-play frameworks for reasoning.

5. **LLMs in Recommendation:** Multiple papers exploring how large language models can enhance recommendation systems through various approaches including reinforcement learning, knowledge graph integration, and explainability.

The papers demonstrate trends toward more efficient architectures (MLP-based, linear-complexity), integration of generative models with discriminative frameworks, and the growing role of LLMs in recommendation and advertising systems.