---
title: "2026-07-26 Conference & arXiv Daily Digest"
type: synthesis
created: 2026-07-26
updated: 2026-07-26
sources: []
tags: [conference-digest, ICML, AAAI, NeurIPS, ICLR, KDD, CVPR, LLM, recommendation, advertising, CTR, agent-systems, generative-models]
---

# 2026-07-26 Conference & arXiv Daily Digest

---

## 1. ICLR 2026 (Oral Papers)

### 1.1 Benchmarking Empirical Privacy Protection for Adaptations of Large Language Models

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: ICLR 2026 (Oral)
- **Abstract & Key Innovations**: This paper provides a systematic benchmark for evaluating privacy leakage when adapting pre-trained LLMs. It quantifies how fine-tuning, prompt-tuning, and adapter-based methods expose training data through membership inference attacks, offering a standardized evaluation framework for privacy-preserving LLM deployment.
- **arXiv**: https://papers.cool/venue/ICLR.2026 (Paper #1)

### 1.2 MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: ICLR 2026 (Oral)
- **Abstract & Key Innovations**: Introduces a scalable training environment for biomedical AI agents that perform code-centric reasoning. The framework enables LLM agents to autonomously write and execute analysis code for biomedical datasets, combining agentic tool use with domain-specific evaluation benchmarks.
- **arXiv**: https://papers.cool/venue/ICLR.2026 (Paper #2)

### 1.3 RAIN-Merging: A Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models with Preserved Thinking Format

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: ICLR 2026 (Oral)
- **Abstract & Key Innovations**: Proposes a gradient-free merging technique that improves instruction following in large reasoning models while preserving their chain-of-thought reasoning format. Addresses the challenge of balancing instruction compliance with reasoning quality without additional training.
- **arXiv**: https://papers.cool/venue/ICLR.2026 (Paper #3)

### 1.4 Mamba-3: Improved Sequence Modeling using State Space Principles

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: ICLR 2026
- **Abstract & Key Innovations**: Third iteration of the Mamba architecture for efficient sequence modeling. Improvements focus on scaling state space models to compete with Transformer-based models on long-context tasks while maintaining linear-time inference complexity.
- **arXiv**: https://papers.cool/venue/ICLR.2026 (Paper #20)

### 1.5 Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Resource

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: ICLR 2026
- **Abstract & Key Innovations**: Demonstrates that MoE architectures can outperform dense models of equivalent total compute budget through careful routing and expert specialization. Challenges the prevailing assumption that dense models are inherently more efficient per FLOP.
- **arXiv**: https://papers.cool/venue/ICLR.2026 (Paper #18)

### 1.6 MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: ICLR 2026
- **Abstract & Key Innovations**: Introduces a memory agent architecture using multi-convolution RL to manage long-context information in LLMs. The agent dynamically compresses and retrieves relevant context, enabling effective handling of documents exceeding standard context windows.
- **arXiv**: https://papers.cool/venue/ICLR.2026 (Paper #14)

### 1.7 In-The-Flow Agentic System Optimization for Effective Planning and Tool Use

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: ICLR 2026
- **Abstract & Key Innovations**: Proposes optimization methods for agentic systems that operate in-the-flow of execution, improving planning and tool-use capabilities without offline training loops. Enables real-time adaptation during task execution.
- **arXiv**: https://papers.cool/venue/ICLR.2026 (Paper #19)

### 1.8 Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning

- **Authors**: Moo Jin Kim, Yihuai Gao, Tsung-Yi Lin, Yen-Chen Lin, Yunhao Ge, Grace Lam, Percy Liang, Shuran Song, Ming-Yu Liu, Chelsea Finn, Jinwei Gu
- **Affiliation**: NVIDIA, Stanford University
- **Venue**: ICLR 2026 (with code)
- **Abstract & Key Innovations**: Adapts a large pretrained video model (Cosmos-Predict2) into an effective robot policy through a single stage of post-training on robot demonstration data, with no architectural modifications. Demonstrates that video generation models can serve as strong priors for visuomotor control.
- **arXiv**: https://www.paperdigest.org/2026/04/iclr-2026-papers-with-code-data/

### 1.9 Verifying Chain-of-Thought Reasoning via its Computational Graph

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: ICLR 2026
- **Abstract & Key Innovations**: Provides a formal framework for verifying chain-of-thought reasoning by constructing computational graphs from LLM outputs. Enables automated checking of logical consistency in multi-step reasoning chains.
- **arXiv**: https://papers.cool/venue/ICLR.2026 (Paper #13)

### 1.10 P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: ICLR 2026 (Oral)
- **Abstract & Key Innovations**: Introduces personalized generative reward models that scale at test time by incorporating user-specific preferences. Enables dynamic adaptation of reward functions to individual users without retraining.
- **arXiv**: https://papers.cool/venue/ICLR.2026 (Paper #10)

---

## 2. ICML 2026

### 2.1 Agentic Systems as Foreseeable Path to AGI (Position Paper)

- **Authors**: Junwei Liao, Shuai Li, Muning Wen, Jun Wang, Weinan Zhang
- **Affiliation**: Multiple institutions (cross-institutional)
- **Venue**: ICML 2026 Position Track
- **Abstract & Key Innovations**: Makes a formal theoretical case that agentic AI architectures—not monolithic model scaling—represent the most viable pathway to AGI. Argues that multi-agent systems with specialized routing achieve "exponentially superior generalization and sample efficiency" over monolithic alternatives. Challenges prevailing scaling assumptions.
- **arXiv**: arXiv:2605.12966

### 2.2 SPHERE: Mitigating the Loss of Spectral Plasticity in Mixture-of-Experts for Deep Reinforcement Learning

- **Authors**: Not specified
- **Affiliation**: sphere-rl
- **Venue**: ICML 2026
- **Abstract & Key Innovations**: Addresses spectral plasticity loss in MoE architectures when applied to deep RL. Proposes SPHERE to maintain representation diversity across experts during RL training.
- **arXiv**: arXiv:2605.04712
- **Code**: https://github.com/sphere-rl/sphere

### 2.3 HyperMLP: An Integrated Perspective for Sequence Modeling

- **Authors**: Jiecheng Lu et al.
- **Affiliation**: Multiple institutions
- **Venue**: ICML 2026
- **Abstract & Key Innovations**: Proposes HyperMLP, integrating multiple sequence modeling perspectives (MLP-based, attention-based, state-space) into a unified architecture for efficient and effective sequence processing.
- **arXiv**: (ICML 2026 oral/poster)

### 2.4 Step Gradient Delay: A Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining

- **Authors**: Philip Zmushko, Egor Petrov, Nursultan Abdullaev, Mikhail Khrushchev, Samuel Horvath
- **Affiliation**: Yandex Research
- **Venue**: ICML 2026
- **Abstract & Key Innovations**: Identifies and analyzes "step gradient delay" as a fundamental bottleneck in asynchronous pipeline parallelism for LLM pretraining. Provides theoretical analysis and practical mitigation strategies for large-scale distributed training.
- **arXiv**: Yandex Research blog (2026-06-10)

### 2.5 DiScoFormer: Plug-In Density and Score Estimation with Transformers

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: ICML 2026 (Oral)
- **Abstract & Key Innovations**: Introduces DiScoFormer for plug-in density and score estimation using Transformers, enabling flexible generative modeling without explicit density function specification.
- **arXiv**: https://icml.cc/virtual/2026/events/oral

### 2.6 On Efficient Scaling of GNNs via IO-Aware Layers Implementations

- **Authors**: Daria Fomina, Daniil Krasylnikov, Alexey Boykov, Andrey Dolgovyazov, Vyacheslav Zhdanovskiy, Fedor Velikonivtsev
- **Affiliation**: Yandex Research
- **Venue**: ICML 2026 (Spotlight)
- **Abstract & Key Innovations**: Proposes IO-aware implementations for GNN layers that significantly improve scaling efficiency by optimizing memory access patterns during message passing.
- **arXiv**: Yandex Research blog (2026-06-10)

---

## 3. AAAI 2026

### 3.1 AAAI-26 Overview

- **Total Submissions**: ~29,000 to Main Technical Track
- **Accepted**: ~4,819 papers (across all tracks)
- **Location**: Singapore, January 20–27, 2026
- **Top Areas**: Computer Vision, Machine Learning, Natural Language Processing

### 3.2 ViG-RAG: Video-aware Graph Retrieval-Augmented Generation via Temporal and Semantic Hybrid Reasoning

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: AAAI 2026
- **Abstract & Key Innovations**: Combines graph-based RAG with video understanding, using temporal and semantic hybrid reasoning for video-aware retrieval and generation.
- **arXiv**: https://papers.cool/venue/AAAI.2026 (Paper #6)

### 3.3 RareAgents: Autonomous Multi-disciplinary Team for Rare Disease Diagnosis and Treatment

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: AAAI 2026
- **Abstract & Key Innovations**: Multi-agent system for rare disease diagnosis that assembles autonomous specialist agents to collaboratively reason about complex medical cases.
- **arXiv**: https://papers.cool/venue/AAAI.2026 (Paper #12)

### 3.4 T2Agent: A Tool-augmented Multimodal Misinformation Detection Agent with Monte Carlo Tree Search

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: AAAI 2026
- **Abstract & Key Innovations**: Combines tool-augmented LLMs with Monte Carlo Tree Search for multimodal misinformation detection, enabling systematic exploration of verification strategies.
- **arXiv**: https://papers.cool/venue/AAAI.2026 (Paper #20)

---

## 4. CVPR 2026

### 4.1 CVPR 2026 Overview

- **Total Submissions**: 16,092
- **Accepted**: 4,090 papers (25.4% acceptance rate)
- **Orals**: 141 papers
- **Location**: New York, June 2026

### 4.2 Best Paper: D4RT - Efficiently Reconstructing Dynamic Scenes One DRT at a Time

- **Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **Affiliation**: Google DeepMind, University College London, University of Oxford
- **Venue**: CVPR 2026 Best Paper
- **Abstract & Key Innovations**: D4RT is a network that reconstructs geometry and motion of dynamic 4D scenes from video using a unified transformer-based architecture. Estimates depth, spatio-temporal correspondence, and full camera parameters, enabling independent and efficient probing of any 3D position at any point in space and time. Lightweight and highly scalable.
- **arXiv**: https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers

### 4.3 WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World

- **Authors**: A. Liang, L. Kong, T. Yan, H. Liu, W. Yang, Z. Huang, W. Yin, J. Zuo, Y. Hu, D. Zhu, D. Lu, Y. Liu, G. Jiang, L. Li, X. Li, L. Zhuo, L. X. Ng, B. R. Cottereau, C. Gao, L. Pan, W. T. Ooi, Z. Liu
- **Affiliation**: NTU MMLab and collaborators
- **Venue**: CVPR 2026 (Oral)
- **Abstract & Key Innovations**: Comprehensive evaluation benchmark for autonomous driving world models covering full-spectrum assessment of simulation fidelity, planning safety, and real-world transfer.
- **arXiv**: https://www.mmlab-ntu.com/conference/cvpr2026/index.html

### 4.4 NitroGen: Open Foundation Model for Generalist Gaming Agents

- **Authors**: Loïc Magne, Anas Awadalla, Guanzhi Wang, Yinzhen Xu, Joshua Belofsky, Fengyuan Hu, Joohwan Kim, Ludwig Schmidt et al.
- **Affiliation**: Multiple institutions
- **Venue**: CVPR 2026 (Oral)
- **Abstract & Key Innovations**: An open foundation model trained for generalist gaming agents. Demonstrates strong zero-shot and few-shot performance across multiple game environments, establishing a new paradigm for game AI.
- **arXiv**: https://github.com/SkalskiP/top-cvpr-2026-papers

### 4.5 Molmo2: Open Weights and Data for Vision-Language Models with Video Understanding and Grounding

- **Authors**: Christopher Clark, Jieyu Zhang, Zixian Ma, Jae Sung Park, Mohammadreza Salehi, Rohun Tripathi et al.
- **Affiliation**: AI2 (Allen Institute for AI)
- **Venue**: CVPR 2026 (Oral)
- **Abstract & Key Innovations**: Open-weights vision-language model with video understanding and grounding capabilities. Fully open-source weights and training data.
- **arXiv**: https://github.com/SkalskiP/top-cvpr-2026-papers

### 4.6 Scaling Spatial Intelligence with Multimodal Foundation Models

- **Authors**: Z. Cai, R. Wang, C. Gu, F. Pu, J. Xu, Y. Wang, W. Yin, Z. Yang, C. Wei, T. Zhou, Q. Sun, H. E. Pang, J. Li, O. Qian, Z. Lin, X. Shi, D. Kewang, X. Han, Z. Chen, X. Fan, H. Deng, L. Lu, L. Pan, B. Li, Z. Liu, Q. Wang, D. Lin, L. Yang
- **Affiliation**: NTU MMLab and collaborators
- **Venue**: CVPR 2026
- **Abstract & Key Innovations**: Scales spatial intelligence capabilities through multimodal foundation models, advancing 3D understanding, navigation, and interaction from multimodal inputs.
- **arXiv**: https://www.mmlab-ntu.com/conference/cvpr2026/index.html

### 4.7 Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers

- **Authors**: Y. Zhou, Z. Xiao, T. Wei, S. Yang, X. Pan
- **Affiliation**: NTU MMLab
- **Venue**: CVPR 2026 (Highlight)
- **Abstract & Key Innovations**: Introduces a trainable log-linear sparse attention mechanism for diffusion Transformers, significantly reducing computational cost while maintaining generation quality.
- **arXiv**: https://www.mmlab-ntu.com/conference/cvpr2026/index.html

---

## 5. NeurIPS 2025

### 5.1 NeurIPS 2025 Overview

- **Accepted**: 5,275 papers from 5,526 submissions (95.46% reviewed)
- **Orals**: 77 papers (1.39%)
- **Spotlights**: 683 papers (12.36%)
- **Location**: San Diego, December 2025

### 5.2 Perception Encoder: The Best Visual Embeddings Are Not at The Output of The Network

- **Authors**: Daniel Bolya, Po-Yao Huang, Peize Sun, Jang Hyun Cho, Andrea Madotto, Chen Wei, Tengyu Ma et al.
- **Affiliation**: Meta AI (FAIR)
- **Venue**: NeurIPS 2025 (with code)
- **Abstract & Key Innovations**: Introduces two alignment methods—language alignment for multimodal language modeling and spatial alignment for dense prediction—to draw out optimal visual embeddings from intermediate network layers rather than outputs. Releases models, code, and a novel dataset of synthetic and human-annotated videos.
- **Code**: https://github.com/facebookresearch/perception_models

### 5.3 TTRL: Test-Time Reinforcement Learning

- **Authors**: Not specified (multiple institutions)
- **Venue**: NeurIPS 2025
- **Abstract & Key Innovations**: Proposes test-time reinforcement learning, enabling LLMs to improve their reasoning through reinforcement during inference rather than requiring additional training. Builds on DeepSeek-R1 and related work.
- **arXiv**: https://proceedings.neurips.cc/paper_files/paper/2025/file/be690ea16f005c174f6c4102a5970e67-Paper-Conference.pdf

### 5.4 RecZero: Think before Recommendation — Autonomous Reasoning-enhanced Recommender

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: NeurIPS 2025
- **Abstract & Key Innovations**: Proposes RecZero, a pure RL-based paradigm for LLM-based recommendation. Uses "Think-before-Recommendation" structured reasoning templates and GRPO for rule-based reward modeling. Eliminates teacher-student distillation, enabling a single LLM to autonomously develop reasoning for rating prediction. Achieves significant gains over distillation baselines.
- **Code**: https://github.com/AkaliKong/RecZero

### 5.5 Adaptive Gradient Masking for Balancing ID and MLLM-based Representations in Recommendation

- **Authors**: Not specified (includes Stanford affiliation)
- **Venue**: NeurIPS 2025
- **Abstract & Key Innovations**: Addresses convergence inconsistency between ID-based and MLLM-based representations in joint training. Proposes Adaptive Gradient Masking (AGM) to dynamically balance parameter updates. Validated through offline experiments and online A/B testing on a large-scale short video platform serving hundreds of millions of users.
- **arXiv**: https://proceedings.neurips.cc/paper_files/paper/2025/

### 5.6 TagCF: Who You Are Matters — Bridging Topics and Social Roles via LLM-Enhanced Logical Recommendation

- **Authors**: Not specified
- **Venue**: NeurIPS 2025
- **Abstract & Key Innovations**: Introduces user role identification and behavioral logic modeling for recommendation. Uses MLLMs to extract tag-based virtual logic graphs and LLMs to infer U2I/I2U logic. Deployed in industrial video-sharing platform. Shows user role tags are more stable than item tags.
- **Code**: https://github.com/Code2Q/TagCF

### 5.7 IGD: Token Decisiveness Modeling via Information Gain in LLMs for Personalized Recommendation

- **Authors**: Not specified
- **Venue**: NeurIPS 2025
- **Abstract & Key Innovations**: Models item generation as a decision process, measuring token decisiveness via Information Gain. Identifies that most tokens have low IG but high logits, biasing both training and decoding. Proposes IGD strategy that downweights low-IG tokens during tuning and rebalances decoding. Achieves ~19-20% average gains in HR@10 and NDCG@10.
- **Code**: https://github.com/ZJLin2oo1/IGD

### 5.8 Tree of Preferences (ToP-Rec) for Diversified Recommendation

- **Authors**: Not specified
- **Venue**: NeurIPS 2025
- **Abstract & Key Innovations**: Uses LLMs to uncover underexplored user preferences via a Tree of Preferences structure for hierarchical interest modeling. Generates synthetic interactions to supplement training data for diversified recommendations.
- **arXiv**: https://proceedings.neurips.cc/paper_files/paper/2025/

### 5.9 RecPIE: Can Explanations Improve Recommendations? A Joint Optimization with LLM Reasoning

- **Authors**: Not specified
- **Venue**: NeurIPS 2025 ER Workshop
- **Abstract & Key Innovations**: Jointly optimizes recommendations and explanations, showing the two tasks reinforce each other. Uses PPO for continuous LLM fine-tuning. Achieves 3-34% gains in predictive performance. Key finding: gains come from reasoning capabilities, not external knowledge.
- **arXiv**: https://openreview.net/forum?id=dBuWo6omzC

---

## 6. KDD 2026

### 6.1 KDD 2026 Overview

- **Location**: Jeju Island, Republic of Korea, August 9–13, 2026
- **Tracks**: February Cycle and July Cycle

### 6.2 GR4AD: Generative Recommendation for Large-Scale Advertising (Kuaishou)

- **Authors**: Kuaishou advertising team
- **Affiliation**: Kuaishou
- **Venue**: KDD 2026
- **Abstract & Key Innovations**: Production-oriented generative recommender for real-time large-scale advertising. Key innovations: (1) UA-SID (Unified Advertisement Semantic ID) capturing multimodal and business signals; (2) LazyAR decoder relaxing layer-wise autoregressive dependencies for efficient multi-candidate generation; (3) VSL (Value-Aware Supervised Learning) and RSPO (Ranking-Guided Softmax Preference Optimization) for business value alignment; (4) Dynamic Beam Serving with traffic-aware adaptive beam search. Achieves **4.2% ad revenue improvement** in online A/B tests. Fully deployed serving 400M+ users with <100ms latency and 500+ QPS per L20.
- **arXiv**: arXiv:2602.22732

### 6.3 OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising (Tencent Weixin)

- **Authors**: Tencent Weixin advertising team
- **Affiliation**: Tencent
- **Venue**: KDD 2026
- **Abstract & Key Innovations**: End-to-end generative advertising recommendation framework addressing three core challenges: objective misalignment between interest/value, target-agnostic generation, and generation-ranking disconnection. Features value-aware multi-task decoupling with task tokens, coarse-to-fine collaborative target awareness via Fake Item Tokens, and input-output dual-side consistency guarantees. Deployed on Tencent's Weixin Channels advertising system, achieving **GMV-Normal +1.34%** improvement.
- **arXiv**: arXiv:2603.02999

### 6.4 DeGRe: Dense-supervised Generative Reranking for Recommendation (Alibaba)

- **Authors**: Chaotian Song, Jingyao Zhang, Chenghao Chen, Zisen Sang, Dehai Zhao, Guodong Cao, Boxi Wu, Deng Cai, Jia Jia
- **Affiliation**: Alibaba Group
- **Venue**: KDD 2026
- **Abstract & Key Innovations**: Dense-supervised generative reranking framework for recommendation. Addresses the reranking stage in multi-stage industrial architectures, modeling contextual associations among items to maximize overall utility.
- **arXiv**: arXiv:2605.25749

### 6.5 Enriching Semantic Profiles into Knowledge Graph for Recommender Systems Using LLMs

- **Authors**: Seokho Ahn, Sungbok Shin, Young-Duk Seo
- **Affiliation**: Multiple institutions
- **Venue**: KDD 2026
- **Abstract & Key Innovations**: Uses LLMs to enrich semantic profiles in knowledge graphs for recommender systems, improving semantic understanding of items and users.
- **arXiv**: arXiv:2601.08148

### 6.6 MemGraphRAG: Memory-based Multi-Agent System for Graph Retrieval-Augmented Generation

- **Authors**: Chuanjie Wu, Zhishang Xiang, Yunbo Tang, Zerui Chen, Qinggang Zhang, Jinsong Su
- **Affiliation**: Multiple institutions
- **Venue**: KDD 2026
- **Abstract & Key Innovations**: Combines memory-based multi-agent systems with GraphRAG for improved knowledge retrieval. Addresses limitations of traditional RAG by leveraging structured graph knowledge.
- **arXiv**: arXiv:2606.00610

### 6.7 CausalMoE: A Billion-Scale Multimodal Foundation Model for Granger Causal Discovery

- **Authors**: Not specified
- **Venue**: KDD 2026
- **Abstract & Key Innovations**: Billion-scale multimodal foundation model using pattern-routed heterogeneous experts for Granger causal discovery. Applies MoE architecture to causal inference tasks.
- **arXiv**: arXiv:2606.13024

### 6.8 Reasoning over Semantic IDs Enhances Generative Retrieval for Recommendation

- **Authors**: Yingzhi He, Yan Sun, Junfei Tan, Yuxin Chen, Xiaoyu Kong, Chunxu Shen et al.
- **Affiliation**: Multiple institutions
- **Venue**: KDD 2026
- **Abstract & Key Innovations**: Enhances generative retrieval for recommendation by reasoning over semantic IDs, improving the quality of item retrieval in generative recommendation systems.
- **arXiv**: arXiv:2603.23183

---

## 7. Advertising & CTR Prediction (Cross-Conference)

### 7.1 LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks

- **Authors**: Luyi Ma, Wanjia Sherry Zhang, Zezhong Fan, Shubham Thakur, Kai Zhao, K. C. Yao et al.
- **Affiliation**: Top U.S. e-commerce platform
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: Treats LLMs as hypernetworks to directly generate CTR estimator parameters in a training-free manner for cold-start ads. Uses few-shot Chain-of-Thought prompting over multimodal ad content (text + images) with CLIP-based retrieval of similar past campaigns. Introduces normalization and calibration techniques for production readiness. Offline: **55.9% NDCG@10 improvement** over cold-start baselines. Online A/B test on top U.S. e-commerce platform shows competitive performance with warm-start baseline (p=0.62, no significant difference). **Successfully deployed in production.**
- **arXiv**: arXiv:2604.12096

### 7.2 GRAB: An LLM-Inspired Sequence-First CTR Prediction Modeling Paradigm (Baidu)

- **Authors**: Shaopeng Chen, Chuyue Xie, Huimin Ren, Shaozong Zhang, Han Zhang, Ruobing Cheng et al.
- **Affiliation**: Baidu
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: End-to-end generative framework for CTR prediction inspired by LLM scaling. Introduces Causal Action-aware Multi-channel Attention (CamA) to capture temporal dynamics and action signals. Full-scale online deployment shows **3.05% revenue increase and 3.49% CTR rise**. Demonstrates desirable scaling behavior with monotonic improvement from longer interaction sequences.
- **arXiv**: arXiv:2602.01865

### 7.3 CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer (LinkedIn)

- **Authors**: David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, Liuqing Li et al.
- **Affiliation**: LinkedIn
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: End-to-end decoder-only Transformer for ads CTR prediction. Key innovations: (1) Context-conditioned decoding with multi-tower prediction heads for post-scoring signals; (2) Self-gated attention mechanism; (3) Timestamp-based RoPE for multi-timescale temporal relationships; (4) Session masking strategies; (5) Production engineering (tensor packing, sequence chunking, custom FlashAttention). Achieves **11.04% CTR lift** over production LiRank baseline. **Deployed on LinkedIn's advertising platform.**
- **arXiv**: arXiv:2602.11410

### 7.4 IDProxy: Cold-Start CTR Prediction with Multimodal LLMs (Xiaohongshu)

- **Authors**: Not specified
- **Affiliation**: Xiaohongshu (Little Red Book)
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: Leverages multimodal LLMs to generate proxy item embeddings for cold-start CTR prediction. Uses coarse-to-fine alignment with existing ID embedding space. **Deployed for both Content Feed and Display Ads on Xiaohongshu's Explore Feed, serving hundreds of millions of users daily.** Online A/B shows 2x improvement for new notes vs global traffic.
- **arXiv**: arXiv:2603.01590

### 7.5 LLM Retrieval for Stable and Predictable Ad Recommendations (Google/Meta-scale)

- **Authors**: Vinodh Kumar Sunkara, Satheeshkumar Karuppusamy, Heng Xu et al.
- **Affiliation**: Large-scale ad platform
- **Venue**: SIGIR 2026 Workshop
- **Abstract & Key Innovations**: Introduces evaluation framework for prediction stability and predictability in ads recommendation. Uses fine-tuned LLMs for semantically aware candidate generation with hierarchical attribute extraction and graph-based expansion. Achieves **0.45% topline lift and 8.62% reduction in A/A' difference** in online tests.
- **arXiv**: arXiv:2605.21969

---

## 8. Agent Systems & Code Execution

### 8.1 OpenGame: Open Agentic Coding for Games

- **Authors**: Yilei Jiang, Jinyuan Hu, Qianyin Xiao, Yaozhi Zheng, Ruize Ma, Kaituo Feng et al.
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: First open-source agentic framework for end-to-end web game creation. Features Game Skill (Template Skill + Debug Skill) and GameCoder-27B, a specialized code LLM trained via continual pre-training, SFT, and execution-grounded RL. Introduces OpenGame-Bench evaluation pipeline. Achieves SOTA on 150 diverse game prompts. **BH=72.4, VU=67.2, IA=65.1** with Claude Sonnet 4.6 backbone.
- **arXiv**: arXiv:2604.18394

### 8.2 Latent Programming Horizons in Coding Agents

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: Shows that residual streams of language models under coding agents linearly encode properties of evolving programs. Linear probes achieve **AUC up to 0.83** for correctness prediction. Discovers that agents maintain latent representations predicting future edit outcomes up to **25 steps in advance** ("latent programming horizon"). Probes transfer across benchmarks without retraining.
- **arXiv**: arXiv:2607.05188

### 8.3 Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: RL framework for improving LLM strategic reasoning in multi-agent games. Uses recursive reasoning paradigm, centralized CoT comparison module, and hybrid advantage estimation. Achieves **22.1% average performance improvements** across various multi-agent games.
- **arXiv**: arXiv:2605.04906
- **Code**: https://github.com/ydhe1012/Strat-Reasoner

### 8.4 Code-Space Response Oracles (CSRO): Generating Interpretable Multi-Agent Policies with LLMs

- **Authors**: Daniel Hennes, Zun Li, John Schultz, Marc Lanctot
- **Affiliation**: Google DeepMind
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: Replaces deep RL oracles in PSRO with LLMs that generate policies as executable source code. Explores zero-shot prompting, iterative refinement, and AlphaEvolve. Produces inherently interpretable, human-readable policies competitive with black-box neural policies.
- **arXiv**: arXiv:2603.10098

### 8.5 PASTE: Accelerating LLM Agents via Pattern-Aware Speculative Tool Execution

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: Addresses serialization bottleneck in LLM agents by speculatively executing tool calls. Exploits recurring tool-call sequences and predictable data dependencies. Reduces average task completion time by **48.5%** and improves tool execution throughput by **1.8x**.
- **arXiv**: arXiv:2603.18897

### 8.6 ProPlay: Procedural World Models for Self-Evolving LLM Agents

- **Authors**: Yijun Ma, Zehong Wang, Yiyang Li, Ziming Li, Xiang Guo, Weixiang Sun et al.
- **Affiliation**: Ant Group
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: Procedural world model for self-evolving agents. Abstracts successful trajectories into procedures organized in a procedure graph with reliability record embeddings. Supports procedure-level preplay for future path rehearsal.
- **arXiv**: arXiv:2606.12780
- **Code**: https://github.com/antman9914/proplay

---

## 9. Generative Models & Sequential Modeling

### 9.1 SDAR: A Synergistic Diffusion-AutoRegression Paradigm for Scalable Sequence Generation

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: ACL 2026 Findings
- **Abstract & Key Innovations**: Systematic study of blockwise discrete diffusion as a middle ground between AR and masked diffusion. Shows AR is more effective backbone for blockwise hybrids. Introduces SDAR conversion recipe (1.7B to 30B parameters). Larger models enable more aggressive parallel decoding achieving **>5x theoretical and 2.3x wall-clock speedup** on H200 GPUs. Local bidirectionality captures structural dependencies in chemistry (+12.3 ChemBench, +5.5 GPQA Diamond).
- **arXiv**: https://aclanthology.org/2026.findings-acl.1110.pdf

### 9.2 Set Diffusion: Interpolating Token Orderings Between Autoregression and Diffusion

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: New class of language models combining AR and diffusion via flexible-position, flexible-length token set factorization with set-causal architecture supporting KV cache updates. Enables faster inference and any-order decoding.
- **arXiv**: arXiv:2607.01775

### 9.3 BlockGen: Flexible Blockwise Sequence Modeling with Hybrid Samplers

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: Blockwise sequence model trained on mixture of block sizes. Achieves **17.5 PPL** on OpenWebText (vs 16.7 for AR, 21.6 for best fixed-block BDM). Introduces ARPC (AR-informed Predictor-Corrector) sampling that improves GSM8K accuracy. Revisits masked vs uniform diffusion under ARPC: gap reverses at higher NFE.
- **arXiv**: arXiv:2606.02241
- **Code**: https://github.com/jdeschena/blockgen

### 9.4 OmniGen-AR: AutoRegressive Any-to-Image Generation

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: Unified AR framework for any-to-image generation. Introduces Disentangled Causal Attention (DCA) to prevent information leakage. Achieves **0.63 on GenEval** and **80.02 on VBench**, outperforming many diffusion models. First vanilla AR model with discrete tokens to achieve 80+ on VBench.
- **arXiv**: arXiv:2606.09156

### 9.5 UniAR: Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer

- **Authors**: Not specified
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: Single discrete visual tokenizer bridges understanding and generation. Uses parallel-bitwise-prediction for efficient visual code prediction. Achieves SOTA on text rendering (0.873 OneIG-EN, 0.917 LongText-EN) and strong performance on image editing (3.73 overall on ImgEdit Bench). RL significantly improves generation quality.
- **arXiv**: arXiv:2606.18249

### 9.6 Constrained Decoding for Diffusion Language Models via Finite Automata

- **Authors**: Meihua Dang, Stefano Ermon
- **Affiliation**: Stanford University
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: Exact and tractable algorithm for constrained sampling from diffusion language models using finite automata as graphical models. Guarantees 100% constraint satisfaction. On BFCL-Live: Dream-7B greedy accuracy improves from 63.9% to 71.5%; stochastic sampling recovers from 22.3% collapse to 69.0% with <5% overhead.
- **arXiv**: arXiv:2607.07026

---

## 10. Benchmarks & Evaluation

### 10.1 Agentick: A Unified Benchmark for General Sequential Decision-Making Agents

- **Authors**: Roger Creus Castanyer, Pablo Samuel Castro, Glen Berseth
- **Affiliation**: Multiple institutions
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: Benchmark with 37 procedurally generated tasks across 6 capability categories, 4 difficulty levels, 5 observation modalities. Evaluates 27 configurations and 90,000+ episodes. Key finding: **No single approach dominates**. GPT-5 mini leads overall (0.309 ONS) but PPO dominates planning (0.402) and multi-agent (0.432). Reasoning harness multiplies LLM performance by 3-10x. All agents far from oracle ceiling.
- **arXiv**: arXiv:2605.06869

### 10.2 Text World Models for LLM-based Agents (Survey)

- **Authors**: Not specified
- **Affiliation**: SUSTech, SYSU
- **Venue**: arXiv 2026
- **Abstract & Key Innovations**: Systematic survey of text world models for LLM agents. Organized around foundations, construction (LLM-as-WM and code-as-WM), application (training and inference), and evaluation. Provides formal framework and comprehensive taxonomy.
- **arXiv**: arXiv:2606.09032
- **Code**: https://github.com/sustech-nlp/awesome-text-world-models

---

## 11. Key Trends & Observations

### 11.1 Generative Recommendation Goes Industrial
- Multiple papers from Kuaishou (GR4AD, 4.2% revenue lift), Tencent Weixin (OneRanker, +1.34% GMV), Baidu (GRAB, +3.05% revenue), LinkedIn (CADET, +11.04% CTR), and Xiaohongshu (IDProxy) demonstrate that generative recommendation based on decoder-only Transformers is achieving real-world deployment at massive scale.
- **Common pattern**: Semantic ID tokenization + AR generation + production-specific efficiency optimizations.

### 11.2 LLM as Hypernetwork for CTR
- LLM-HYPER introduces the concept of using LLMs to generate model parameters rather than predictions, enabling training-free cold-start solutions.

### 11.3 Diffusion-AR Hybrid Paradigms
- Multiple works (SDAR, Set Diffusion, BlockGen) converge on blockwise discrete diffusion as a promising middle ground between AR and pure diffusion, offering parallel generation while maintaining AR-compatible serving.

### 11.4 Agent Systems Maturation
- ICML 2026 position paper argues for agentic pathways to AGI. Practical agent frameworks (OpenGame, PASTE) show measurable improvements. CSRO demonstrates LLM-generated code policies competitive with neural policies in game theory.

### 11.5 RL for LLM Post-Training Expands
- Beyond math/code reasoning (DeepSeek-R1), RL is now applied to recommendation (RecZero), strategic games (Strat-Reasoner), and multi-agent systems. Test-Time RL (TTRL) enables inference-time improvement.

### 11.6 Privacy and Safety in LLM Adaptation
- ICLR 2026 oral on privacy benchmarking signals growing concern about privacy leakage in LLM fine-tuning/adaptation.

---

## Statistics Summary

| Conference | Year | Submissions | Accepted | Orals | Key Focus |
|-----------|------|------------|----------|-------|-----------|
| AAAI | 2026 | ~29,000 | ~4,819 | N/A | CV, ML, NLP |
| ICLR | 2026 | ~19,800 | ~5,340 | 223 | LLMs, RL, generative |
| ICML | 2026 | N/A | 6,500+ | N/A | ML, agents, RL |
| CVPR | 2026 | 16,092 | 4,090 | 141 | Vision, 3D, generative |
| NeurIPS | 2025 | 5,526 | 5,275 | 77 | LLMs, RL, recsys |
| KDD | 2026 | N/A | N/A | N/A | Data mining, recsys, ads |
