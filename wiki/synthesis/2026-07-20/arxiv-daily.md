---
title: "arXiv Daily Digest - 2026-07-20"
type: synthesis
created: 2026-07-20
updated: 2026-07-20
sources: []
tags: [arxiv, daily-digest, AI, LLM, recommendation, advertising, CTR, games, sequential-modeling]
---

# arXiv Daily Digest - July 20, 2026

## 1. Large Language Models (LLMs)

### 1.1 Understanding Large Language Models
- **Authors:** Yannik Keller, Thomas Eisenmann
- **Institution:** Not specified
- **Abstract:** Comprehensive chapter outlining current understanding of LLMs, discussing emerging capabilities and their mechanistic implementation within processing layers. Covers Transformer architecture, emergent capabilities resembling human cognition (symbolic reasoning, theory of mind, deception), and explainable AI approaches from neuron activation analysis to circuit tracing.
- **Key Innovations:** Reviews evidence on emergent capabilities, examines differences between human and LLM cognition, advocates for nuanced discussion of LLM cognition.
- **Link:** [arXiv:2607.01006](https://arxiv.org/abs/2607.01006)

### 1.2 LLM-Driven AutoML for Cross-Lingual Handwritten OCR
- **Authors:** Mobina Kashaniyan, Amirhossein Ghassemi, Nasser Mozayani
- **Institution:** Not specified
- **Abstract:** Closed-loop neural architecture search using GPT-5, GPT-4o, and Claude Sonnet 4 for cross-languages handwritten OCR. Achieves 98.1% accuracy with 41-44ms inference latency.
- **Key Innovations:** LLMs as effective AutoML agents for neural architecture search, enabling scalable, script-adaptive handwriting recognition.
- **Link:** [arXiv:2607.15509](https://arxiv.org/abs/2607.15509)

### 1.3 RecGPT-V3 Technical Report
- **Authors:** Bowen Zheng, Chao Yi, Dian Chen, et al.
- **Institution:** Not specified (likely Alibaba/Tmall based on context)
- **Abstract:** Technical report on RecGPT-V3, a generative recommendation system using LLMs.
- **Key Innovations:** Integration of LLMs with recommendation systems, generative approaches to recommendation.
- **Link:** [arXiv:2607.15591](https://arxiv.org/abs/2607.15591)

### 1.4 LLMs Encode Relevance as a Layer-Wise Cross-Lingual Signal
- **Authors:** Pietro Bernardelle, Samaneh Mohtadi, Stefano Civelli, Joel Mackenzie, Gianluca Demartini
- **Institution:** Not specified
- **Abstract:** Investigates how LLMs encode relevance information across languages at different layers.
- **Key Innovations:** Understanding of cross-lingual relevance encoding in LLMs.
- **Link:** [arXiv:2607.15555](https://arxiv.org/abs/2607.15555)

## 2. Recommendation Systems

### 2.1 RECAP: Feedback-Driven Streaming Semantic User Profiles for Short-Video Recommendation
- **Authors:** Ziyi Zhao, Xiaoyou Zhou, Xiao Lv, et al.
- **Institution:** Not specified
- **Abstract:** Accepted at RecSys 2026. Proposes feedback-driven streaming semantic user profiles for short-video recommendation.
- **Key Innovations:** Streaming semantic profiles, feedback-driven approach for dynamic user modeling.
- **Link:** [arXiv:2607.15730](https://arxiv.org/abs/2607.15730)

### 2.2 RecRec: Latent Interests Recursive Reasoning for Sequential Recommendation
- **Authors:** Wenhao Deng, Junchen Fu, Hanwen Du, et al.
- **Institution:** Not specified
- **Abstract:** Accepted at RecSys 2026. Proposes recursive reasoning over latent interests for sequential recommendation.
- **Key Innovations:** Recursive reasoning mechanism for capturing evolving user interests.
- **Link:** [arXiv:2607.12945](https://arxiv.org/abs/2607.12945)

### 2.3 Learning to Forget: Satiation-Aware Long-Sequence Transducers
- **Authors:** Yipin Dai, Ruocong Tang, Xing Fang, et al.
- **Institution:** Not specified (likely Alibaba based on context)
- **Abstract:** SIGIR '26 Industry Track. Addresses post-purchase redundancy in recommendation through satiation-aware transducers.
- **Key Innovations:** Modeling user satiation to improve recommendation diversity.
- **Link:** [arXiv:2607.12714](https://arxiv.org/abs/2607.12714)

### 2.4 SlimPer: Make Personalization Model Slim and Smart
- **Authors:** Siqi Wang, Xianjie Chen, Shaofeng Deng, et al.
- **Institution:** Not specified (likely large tech company given author list)
- **Abstract:** Proposes slim and smart personalization models for efficient recommendation.
- **Key Innovations:** Model compression techniques for personalization while maintaining performance.
- **Link:** [arXiv:2607.12281](https://arxiv.org/abs/2607.12281)

### 2.5 Not Only NTP: Extending Training Signal Coverage for Generative Recommendation
- **Authors:** Changhao Li, Shuli Wang, Junwei Yin, et al.
- **Institution:** Not specified
- **Abstract:** Extends training signals beyond next-token prediction for generative recommendation.
- **Key Innovations:** Broader training objectives for better generative recommendation models.
- **Link:** [arXiv:2607.12277](https://arxiv.org/abs/2607.12277)

### 2.6 Where Reasoning Matters: Rethinking Latent Reasoning in Semantic ID-based Generative Recommendation
- **Authors:** Shangxin Yang, Min Gao, Zongwei Wang, Junliang Yu
- **Institution:** Not specified
- **Abstract:** Examines the role of latent reasoning in semantic ID-based generative recommendation systems.
- **Key Innovations:** Analysis and improvement of reasoning mechanisms in generative recommenders.
- **Link:** [arXiv:2607.12425](https://arxiv.org/abs/2607.12425)

### 2.7 TMallGS: Scaling Unified Feature and Sequence Modeling for Generative E-commerce Search
- **Authors:** Zhentao Song, Yufeng Gao, Xing Fang, et al.
- **Institution:** Alibaba (TMall)
- **Abstract:** Proposes unified feature and sequence modeling for generative e-commerce search at scale.
- **Key Innovations:** Scaling generative models for e-commerce search with unified architecture.
- **Link:** [arXiv:2607.13398](https://arxiv.org/abs/2607.13398)

### 2.8 Can We Steer the Black-Box? Controllability-Centric Evaluation of Recommender Systems
- **Authors:** Jiwen Zhou, Xiang Liu, Mingming Li, et al.
- **Institution:** Not specified
- **Abstract:** Proposes controllability-centric evaluation framework for recommender systems using collaborative agents.
- **Key Innovations:** Novel evaluation paradigm focusing on controllability of recommendations.
- **Link:** [arXiv:2607.13418](https://arxiv.org/abs/2607.13418)

### 2.9 Cheaper is Better: Discount-Aware Network for Conversion Rate Prediction
- **Authors:** Ruocong Tang, Yang Huang, Xing Fang, et al.
- **Institution:** Not specified (likely Alibaba)
- **Abstract:** SIGIR '26 Industry Track. Proposes discount-aware network for CVR prediction in e-commerce.
- **Key Innovations:** Incorporating discount signals into conversion rate prediction.
- **Link:** [arXiv:2607.12578](https://arxiv.org/abs/2607.12578)

## 3. Click-Through Rate (CTR) Prediction

### 3.1 LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization
- **Authors:** Luyi Ma, Wanjia Sherry Zhang, Zezhong Fan, et al.
- **Institution:** Not specified (likely e-commerce company)
- **Abstract:** Uses LLMs as hypernetworks to generate CTR estimator parameters in training-free manner. Achieves 55.9% improvement in NDCG@10 for cold-start. Deployed in production on top US e-commerce platform.
- **Key Innovations:** LLM-based hypernetwork for zero-shot CTR prediction, few-shot Chain-of-Thought prompting over multimodal ad content.
- **Link:** [arXiv:2604.12096](https://arxiv.org/abs/2604.12096)

### 3.2 Dual-Stream MLP is All You Need for CTR Prediction
- **Authors:** Kesha Ou, Zhen Tian, Wayne Xin Zhao, et al.
- **Institution:** Renmin University of China
- **Abstract:** Accepted by TKDD. Proposes DS-MLP framework using knowledge distillation to consolidate explicit feature interaction learning into main MLP with parallel MLP for implicit interactions.
- **Key Innovations:** Simplified MLP-based architecture achieving SOTA on three benchmarks, knowledge distillation for feature interaction learning.
- **Link:** [arXiv:2606.04944](https://arxiv.org/abs/2606.04944)

### 3.3 Long-History User Transformers for Real-Time Ad Ranking
- **Authors:** Viacheslav Ovchinnikov, Georgii Smirnov, Nikolai Savushkin, et al.
- **Institution:** Not specified
- **Abstract:** Addresses handling long interaction histories in real-time ad ranking under latency constraints.
- **Key Innovations:** Efficient transformer architecture for long user histories in ad ranking.
- **Link:** [arXiv:2607.14331](https://arxiv.org/abs/2607.14331)

## 4. Advertising & Ad Generation

### 4.1 An LLM-powered Agentic Recommendation System for Connected TV Content Discovery
- **Authors:** Lei Shi, Di Wang, Harry Tran, et al.
- **Institution:** Meta
- **Abstract:** Presents LLM-powered agentic recommendation system for CTV that processes diverse contextual signals (trending topics, breaking news, cultural events) using LLM reasoning capabilities.
- **Key Innovations:** Agentic architecture orchestrating LLM and traditional ML components, handling unstructured contextual information.
- **Link:** [arXiv:2607.09988](https://arxiv.org/abs/2607.09988)

### 4.2 Uni-AdGen: Unified Advertisement Generative Model
- **Authors:** Not fully specified
- **Institution:** Not specified
- **Abstract:** Proposes unified framework incorporating images and texts into single autoregressive generation process for advertisement creation. Incorporates CTR signals for personalized generation.
- **Key Innovations:** Unified multimodal advertisement generation, CTR-aware personalized ad creation.
- **Link:** [arXiv:2605.12138](https://arxiv.org/abs/2605.12138)

### 4.3 CADET: Context-Conditioned Ads CTR Prediction
- **Authors:** Multiple authors including Fedor Borisyuk
- **Institution:** LinkedIn
- **Abstract:** End-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Addresses challenges of post-scoring contextual signals and offline-online consistency.
- **Key Innovations:** Transformer-based ads CTR prediction, context-conditioned scoring.
- **Link:** [arXiv:2602.11410](https://arxiv.org/abs/2602.11410)

### 4.4 NaiAD: Native Advertising Dataset
- **Authors:** Not fully specified
- **Institution:** Not specified
- **Abstract:** Creates dataset for native advertising with multi-dimensional decoupled generation pipeline. Shows Pareto optimality in balancing user and commercial utility.
- **Key Innovations:** Systematic dataset creation for native ads, decoupled controllable generation for ad-text alignment.
- **Link:** [arXiv:2605.09918](https://arxiv.org/abs/2605.09918)

### 4.5 Generative Click-through Rate Prediction with Applications to Search Advertising
- **Authors:** Lingwei Kong, Lu Wang, Changping Peng, et al.
- **Institution:** Not specified (likely e-commerce platform)
- **Abstract:** Two-stage training leveraging generative pre-training for next-item prediction to enhance discriminative CTR prediction. Deployed on world's largest e-commerce platform.
- **Key Innovations:** Generative-discriminative hybrid approach, two-stage training pipeline.
- **Link:** [arXiv:2507.11246](https://arxiv.org/abs/2507.11246)

## 5. Games & Reinforcement Learning

### 5.1 Augmenting Game AI with Deep Reinforcement Learning
- **Authors:** Alessandro Sestini et al.
- **Institution:** Not specified
- **Abstract:** Published at Conference on Games 2026. Proposes framework for training RL models suited for game AI and game development. Identifies bottlenecks and hard problems in deploying player-facing ML agents.
- **Key Innovations:** Framework for game AI training, practical considerations for ML deployment in games.
- **Link:** [arXiv:2606.20210](https://arxiv.org/abs/2606.20210)

### 5.2 LLM Semantic Signaling Game and Mechanism Design
- **Authors:** Quanyan Zhu
- **Institution:** Not specified
- **Abstract:** Studies LLM behavior in semantic signaling games, examining systematic blindness, awareness shaping, and mindset dynamics.
- **Key Innovations:** Game-theoretic analysis of LLM behavior, mechanism design for AI systems.
- **Link:** [arXiv:2606.29113](https://arxiv.org/abs/2606.29113)

### 5.3 Physics-enhanced Reinforcement Learning for Real-Time Optimal Control
- **Authors:** Matteo Tomasetto, Nicolò Botteghi, Gabriele Bruni, Andrea Manzoni
- **Institution:** Not specified
- **Abstract:** Combines physics knowledge with RL for real-time optimal control of dynamical systems.
- **Key Innovations:** Physics-informed RL for control systems.
- **Link:** [arXiv:2607.16177](https://arxiv.org/abs/2607.16177)

### 5.4 When Does Muon Help Agentic Reinforcement Learning?
- **Authors:** Kai Ruan, Jinghao Lin, Zihe Huang, et al.
- **Institution:** Not specified
- **Abstract:** Investigates when Muon optimizer helps in agentic RL settings.
- **Key Innovations:** Analysis of optimization techniques for agentic RL.
- **Link:** [arXiv:2607.16169](https://arxiv.org/abs/2607.16169)

### 5.5 DADiff: Diffusion-Driven Cross-Domain Policy Adaptation for Reinforcement Learning
- **Authors:** Hanyang Chen, Anirudh Satheesh, Longchao Da, Hua Wei
- **Institution:** Not specified
- **Abstract:** Accepted by IROS 2026. Uses diffusion models for cross-domain policy adaptation in RL.
- **Key Innovations:** Diffusion-based domain adaptation for RL policies.
- **Link:** [arXiv:2607.16090](https://arxiv.org/abs/2607.16090)

## 6. Sequential Modeling

### 6.1 Field-Aware RankMixer with Dual-Stream Bilinear Fusion for Tencent UNI-REC Challenge
- **Authors:** Yufeng Zhang, Zhengqi Xu, Jiajun Cui
- **Institution:** Not specified
- **Abstract:** KDD Cup 2026 Tencent UNIREC Challenge solution. Proposes field-aware rank mixing with dual-stream bilinear fusion.
- **Key Innovations:** Field-aware architecture for recommendation, dual-stream fusion mechanism.
- **Link:** [arXiv:2607.15590](https://arxiv.org/abs/2607.15590)

### 6.2 Do Generative Models Keep Time? Time-Aware Evaluation of Synthetic Sequential Tabular Data
- **Authors:** Kiwan Kwon, Kangmin Kim, Hojin Lee, et al.
- **Institution:** Not specified
- **Abstract:** Evaluates whether generative models preserve temporal properties in sequential tabular data.
- **Key Innovations:** Time-aware evaluation metrics for synthetic sequential data.
- **Link:** [arXiv:2607.15606](https://arxiv.org/abs/2607.15606)

## 7. AI Agents & Tool Use

### 7.1 ToolVerse: Unlocking Massive Environments and Long-Horizon Tasks for Agentic RL
- **Authors:** Shuaiyu Zhou, Fengpeng Yue, Zengjie Hu, et al.
- **Institution:** Not specified
- **Abstract:** Proposes framework for agentic RL with massive environments and long-horizon tasks.
- **Key Innovations:** Scalable environments for training agentic RL systems.
- **Link:** [arXiv:2607.15660](https://arxiv.org/abs/2607.15660)

### 7.2 Can Agents Generalize to the Open World? Unveiling Fragility of Static Training in Tool Use
- **Authors:** Song-Lin Lv, Weiming Wu, Rui Zhu, et al.
- **Institution:** Not specified
- **Abstract:** Accepted by ICML 2026. Examines generalization limitations of agents trained with static tool-use demonstrations.
- **Key Innovations:** Analysis of tool-use agent generalization, identification of fragility in static training.
- **Link:** [arXiv:2607.01084](https://arxiv.org/abs/2607.01084)

### 7.3 SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration
- **Authors:** Yuyao Zhang, Junjie Gao, Zhengxian Wu, et al.
- **Institution:** Not specified
- **Abstract:** Proposes framework for robust collaboration between information-seeking agents.
- **Key Innovations:** Multi-agent collaboration for open-domain search.
- **Link:** [arXiv:2607.15257](https://arxiv.org/abs/2607.15257)

## 8. Retrieval & Search

### 8.1 MESH: Scaling Up Retrieval with Heterogeneous Content Unification
- **Authors:** Jiaxing Qu, Yilin Chen, Junpeng Hou, et al.
- **Institution:** Not specified (likely Pinterest based on context)
- **Abstract:** Proposes unified retrieval across heterogeneous content types at scale.
- **Key Innovations:** Content-agnostic retrieval architecture.
- **Link:** [arXiv:2607.12392](https://arxiv.org/abs/2607.12392)

### 8.2 Deep-learning Causal Retrieval Optimization for Efficient e-commerce Distribution in Pinterest
- **Authors:** Junpeng Hou, XianXing Zhang, Sai Xiao, et al.
- **Institution:** Pinterest
- **Abstract:** Accepted at KDD '26. Proposes causal retrieval optimization for e-commerce distribution.
- **Key Innovations:** Causal inference for retrieval optimization.
- **Link:** [arXiv:2607.14161](https://arxiv.org/abs/2607.14161)

## 9. Multimodal & Vision-Language Models

### 9.1 S1-Omni: A Unified Multimodal Reasoning Model for Scientific Understanding, Prediction, and Generation
- **Authors:** Jiahao Zhao, Junyi Liu, Lifeng Xu, et al.
- **Institution:** Not specified
- **Abstract:** Unified multimodal model for scientific tasks including understanding, prediction, and generation.
- **Key Innovations:** Integration of multiple modalities for scientific applications.
- **Link:** [arXiv:2607.15686](https://arxiv.org/abs/2607.15686)

## 10. Foundation Models & Architecture

### 10.1 PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization
- **Authors:** Yuchen Yang, Yifan Zhao, Anisha Dasgupta, Sasa Misailovic
- **Institution:** Not specified
- **Abstract:** Proposes dynamic quality-aware quantization for efficient MoE LLM serving.
- **Key Innovations:** Quality-aware quantization, paged weight management for MoE models.
- **Link:** [arXiv:2607.16184](https://arxiv.org/abs/2607.16184)

### 10.2 Kolmogorov-Arnold Networks for Small Language Models
- **Authors:** Felippe Alves, Renato Vicente
- **Institution:** Not specified
- **Abstract:** Applies Kolmogorov-Arnold Networks to small language models.
- **Key Innovations:** Alternative architecture based on Kolmogorov-Arnold representation theorem.
- **Link:** [arXiv:2607.15525](https://arxiv.org/abs/2607.15525)

## Summary

Today's papers show strong trends in:
1. **LLM-powered recommendation systems** - Multiple papers integrating LLMs into recommendation pipelines (Meta, Alibaba/TMall)
2. **CTR prediction advances** - New architectures (DS-MLP, LLM-HYPER) and deployed systems (LinkedIn's CADET)
3. **Agentic AI** - Growing focus on tool-use agents, multi-agent systems, and agent collaboration
4. **Generative advertising** - Unified multimodal ad generation and personalized ad creation
5. **Game AI with RL** - Frameworks for deploying RL in games, game-theoretic analysis of LLMs
6. **Sequential modeling** - Time-aware evaluation, field-aware architectures for recommendation
7. **Efficient serving** - Quantization techniques for MoE models, lightweight architectures

Total papers cataloged: 35+
