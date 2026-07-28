---
title: "AI/ML Conference Digest 2026-07-28"
type: synthesis
created: 2026-07-28
updated: 2026-07-28
tags: [conference, arxiv, ICML, AAAI, ICLR, NeurIPS, CVPR, KDD, SIGIR, WWW, EMNLP, CIKM, RecSys, recommendation, CTR, agents, code-generation, diffusion, generative-models]
---

# AI/ML Conference Digest - 2026-07-28

> Comprehensive digest of recent papers from top ML/AI conferences (2025-2026) and arXiv, covering LLMs, recommendation systems, advertising, CTR, agents, code generation, generative models, and benchmarks.

---

## 1. ICML 2026 (Seoul, July 6-11, 2026)

### Conference Stats
- **Submissions**: 23,918 (record, doubled 2025's 12,107)
- **Accepted**: 6,352 (26.6% acceptance rate)
- **Spotlight**: 536 (2.2%), **Oral**: 168 (0.7%)
- **Outstanding Paper Awards**: 2 winners (diffusion language model reasoning; log-concave sampling theory)
- **Test of Time Award**: "Asynchronous Methods for Deep Reinforcement Learning" (Mnih et al., ICML 2016)

### Key Papers

#### 1.1 Diffusion Language Models (Outstanding Paper)
- **Title**: Outstanding Paper on Diffusion Language Model Reasoning
- **Venue**: ICML 2026 Outstanding Paper Award
- **Innovation**: Demonstrates reasoning capabilities in diffusion language models, showing they can match or exceed autoregressive models on reasoning tasks while enabling parallel decoding.
- **Significance**: Validates diffusion as a competitive paradigm for LLMs beyond simple generation.

#### 1.2 Mixture-of-Experts Scaling
- **Title**: Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Resource
- **Venue**: ICLR 2026 / ICML 2026
- **Authors**: Multiple institutions
- **Innovation**: Shows MoE architectures can outperform dense models with equal computational budget, challenging conventional wisdom about MoE efficiency.
- **Link**: https://openreview.net/group?id=ICLR.cc/2026/Conference

#### 1.3 Reinforcement Learning with Discrete Diffusion Policies
- **Title**: Reinforcement Learning with Discrete Diffusion Policies for Combinatorial Action Spaces
- **Venue**: ICML 2026 Poster
- **Innovation**: Combines discrete diffusion models with RL for combinatorial optimization problems, enabling efficient exploration of large action spaces.

#### 1.4 Multi-Objective RL
- **Title**: Near-Minimax Multi-Objective RL under Predictable Adversarial Preferences
- **Venue**: ICML 2026 Poster
- **Authors**: Multiple institutions
- **Innovation**: Protocol-safe reward interface for multi-objective RL with hypervolume-aware evaluation, connecting online learning with preference-free deployment.

---

## 2. AAAI 2026 (Singapore, January 20-27, 2026)

### Conference Stats
- **Submissions**: ~29,000 (nearly double AAAI-25)
- **Accepted**: ~4,300 papers
- **Program Committee**: 28,000 members (3x previous year)
- **Largest research areas**: Computer Vision, Machine Learning, NLP

### Key Papers

#### 2.1 Multi-Agent Systems
- **Title**: Various multi-agent papers including:
  - "Agent Debate for Efficient and Accurate LLM Inference"
  - "Multi-Agent Chain-of-Draft Reasoning for RL-Enhanced LLMs"
  - "Learning to Deliberate: Meta-policy Collaboration for Agentic LLMs"
- **Venue**: AAAI-26 Technical Track on Multiagent Systems
- **Innovation**: Advances in multi-agent coordination, debate mechanisms, and meta-policy learning for LLM agents.

#### 2.2 CTR Prediction
- **Title**: Length-Adaptive Interest Network for Balancing Long and Short Sequence Modeling in CTR Prediction
- **Venue**: AAAI-26
- **Innovation**: Adaptive architecture that dynamically balances long-term and short-term user interest modeling for CTR prediction.

#### 2.3 Search and Recommendation
- **Title**: Dual-Horizon Interest Model for Unified Search and Recommendation
- **Venue**: AAAI-26
- **Innovation**: Unifies search and recommendation tasks with dual-horizon interest modeling.

#### 2.4 Federated Learning
- **Title**: FedSEA-LLaMA: A Secure, Efficient and Adaptive Federated Splitting Framework for Large Language Models
- **Venue**: AAAI-26
- **Innovation**: Federated learning framework for LLMs with adaptive splitting and security guarantees.

---

## 3. ICLR 2026 (Rio de Janeiro, Brazil)

### Conference Stats
- **Submissions**: 19,525 valid (23,918 total before desk rejects)
- **Accepted**: 5,355 papers (27.4% acceptance rate)
- **Oral**: 223 (1.13%)
- **Reviewers**: 18,054 reviewers, 76,139 reviews

### Outstanding Papers

#### 3.1 Mamba-3: Improved Sequence Modeling
- **Title**: Mamba-3: Improved Sequence Modeling using State Space Principles
- **Authors**: Multiple institutions
- **Innovation**: Advances state space models for efficient long-sequence modeling, improving on Mamba-2 with better scaling and performance.
- **Link**: https://openreview.net/group?id=ICLR.cc/2026/Conference

#### 3.2 MemAgent: Long-Context Memory
- **Title**: MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent
- **Authors**: Multiple institutions
- **Innovation**: RL-based memory agent for LLMs that enables effective long-context processing through multi-convolution memory operations.

#### 3.3 P-GenRM: Personalized Reward Models
- **Title**: P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling
- **Authors**: Multiple institutions
- **Innovation**: Personalized reward models that scale at test-time based on user preferences, enabling better alignment with individual user needs.

#### 3.4 In-The-Flow Agentic System
- **Title**: In-The-Flow Agentic System Optimization for Effective Planning and Tool Use
- **Authors**: Multiple institutions
- **Innovation**: Framework for optimizing agentic systems during inference, improving planning and tool use capabilities.

#### 3.5 Benchmarking Privacy Protection
- **Title**: Benchmarking Empirical Privacy Protection for Adaptations of Large Language Models
- **Venue**: ICLR 2026 Oral
- **Innovation**: Comprehensive benchmark for evaluating privacy protection when adapting LLMs to downstream tasks.

---

## 4. NeurIPS 2025 (San Diego, December 2-7, 2025)

### Conference Stats
- **Submissions**: 21,575 (61% increase over 2024)
- **Accepted**: 5,290 (24.52% acceptance rate)
- **Reviewers**: 20,518 reviewers, 1,663 ACs, 199 SACs
- **New tracks**: Position Paper Track, Journal Track (34 papers from JMLR/AoS)
- **Best Paper**: "Gated Attention for Large Language Models" (Qiu et al.)
- **Test of Time**: "Faster R-CNN" (Ren et al., 2015) with 56,700+ citations

### Key Papers

#### 4.1 Gated Attention (Best Paper)
- **Title**: Gated Attention for Large Language Models
- **Authors**: Qiu et al.
- **Innovation**: Novel gating mechanism for attention in LLMs, improving efficiency and performance.
- **Link**: https://papers.nips.cc/

#### 4.2 Perception Encoder
- **Title**: Perception Encoder: The Best Visual Embeddings Are Not at The Output of The Network
- **Authors**: Facebook Research (Meta AI)
- **Innovation**: New alignment methods for visual embeddings that outperform standard network outputs, with language and spatial alignment for multimodal tasks.
- **Code**: https://github.com/facebookresearch/perception_models

#### 4.3 Gated Attention Variants
- **Title**: Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
- **Authors**: Multiple institutions
- **Innovation**: Systematic investigation of gated attention mechanisms showing improvements in efficiency and reduction of attention sinks.

---

## 5. CVPR 2026 (New York, June 2026)

### Conference Stats
- **Submissions**: 16,092
- **Accepted**: 4,089 (25.4% acceptance rate)
- **Oral papers**: 141
- **Best Paper Awards**: 2 winners

### Best Papers

#### 5.1 D4RT: Dynamic 4D Scene Reconstruction (Best Paper)
- **Title**: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
- **Authors**: Google DeepMind, UCL, University of Oxford
- **Innovation**: Unified transformer-based architecture for reconstructing geometry and motion of dynamic 4D scenes from video, estimating depth, spatio-temporal correspondence, and camera parameters.
- **Significance**: Lightweight and scalable method for dynamic scene reconstruction.

#### 5.2 O-Voxel: 3D Generation (Best Paper)
- **Title**: Native and Compact Structured Latents for 3D Generation
- **Authors**: Tsinghua University, Microsoft Research, USTC, Microsoft AI
- **Innovation**: Novel O-Voxel representation for 3D generative modeling that captures complex shapes and surface attributes, significantly improving quality and realism of AI-generated 3D assets.

#### 5.3 SAM 3D: 3D Segmentation
- **Title**: SAM 3D: 3Dfy Anything in Images
- **Authors**: Georgia Tech, Meta AI
- **Innovation**: Extends SAM to 3D segmentation capabilities, enabling 3D understanding from 2D images.

#### 5.4 NitroGen: Gaming Agents
- **Title**: NitroGen: An Open Foundation Model for Generalist Gaming Agents
- **Authors**: Multiple institutions
- **Innovation**: Open foundation model for generalist gaming agents, achieving strong performance across diverse game environments.

#### 5.5 Molmo2: Vision-Language Models
- **Title**: Molmo2: Open Weights and Data for Vision-Language Models with Video Understanding and Grounding
- **Authors**: Multiple institutions
- **Innovation**: Open-source vision-language model with video understanding capabilities, providing weights and data for reproducibility.

#### 5.6 Apple CVPR Papers
- **AMUSE**: Audio-Visual Benchmark for Agentic Multi-Speaker Understanding
- **AToken**: Unified Tokenizer for Vision
- **SO-Bench**: Structural Output Evaluation of Multimodal LLMs
- **STARFlow-V**: End-to-End Video Generative Modeling with Normalizing Flows
- **Link**: https://machinelearning.apple.com/updates/apple-at-cvpr-2026

---

## 6. KDD 2026 (Jeju Island, Korea, August 9-13, 2026)

### Conference Stats
- **Two submission cycles**: February and July
- **Research Track and Applied Data Science Track**

### Key Papers

#### 6.1 Generative Recommendation for Advertising
- **Title**: GR4AD: Generative Recommendation for ADdvertising
- **Authors**: Kuaishou
- **Innovation**: Production-oriented generative recommender for real-time advertising with:
  - UA-SID (Unified Advertisement Semantic ID) for complex business information
  - LazyAR decoder for efficient multi-candidate generation
  - VSL and RSPO for value-aware optimization
  - Dynamic Beam Serving for adaptive computation
- **Results**: +4.2% ad revenue improvement, deployed in Kuaishou (400M+ users)
- **Link**: https://arxiv.org/abs/2602.22732

#### 6.2 CTR Prediction Scaling Laws
- **Title**: EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling
- **Authors**: Alibaba (Taobao)
- **Innovation**: Efficiently Scalable Transformer for CTR prediction with:
  - Lightweight Cross Attention (LCA) for high-impact cross-feature dependencies
  - Content Sparse Attention (CSA) for content similarity-based behavior selection
  - Power-law scaling behavior demonstrated
- **Results**: +3.27% RPM, +1.22% CTR on Taobao display advertising
- **Link**: https://arxiv.org/abs/2602.10811

#### 6.3 LLM-Inspired CTR Prediction
- **Title**: GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm
- **Authors**: Baidu
- **Innovation**: End-to-end generative framework for CTR with Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics and action signals.
- **Results**: +3.05% revenue, +3.49% CTR on Baidu home feed ads
- **Link**: https://arxiv.org/abs/2602.01865

#### 6.4 Sequential Recommendation
- **Title**: SRPFN: One Sequential Recommendation Model Pretrained from Synthetic Priors
- **Authors**: KAIST
- **Innovation**: Training-free sequential recommendation using Prior-data Fitted Networks, achieving competitive performance without gradient updates on target data.
- **Results**: Outperforms all training-free baselines by substantial margin across 5 benchmarks

#### 6.5 Knowledge Graph Enrichment
- **Title**: Enriching Semantic Profiles into Knowledge Graph for Recommender Systems Using Large Language Models
- **Authors**: Multiple institutions
- **Innovation**: LLM-based enrichment of knowledge graphs for recommendation systems.

#### 6.6 Popularity Bias in Transformers
- **Title**: The Pitfall of Scaling Up: Uncovering and Mitigating Popularity Bias Amplification in Scaling Transformer-based Recommenders
- **Authors**: Zhejiang University
- **Innovation**: Identifies and mitigates popularity bias amplification when scaling Transformer-based recommenders, with spectral regularization solution.
- **Code**: https://github.com/Tiny Snow/GenRec

---

## 7. SIGIR 2026 (Melbourne, Australia, July 20-24, 2026)

### Key Papers

#### 7.1 Unified Search and Recommendation
- **Title**: GEMS: Unifying Search and Recommendation in LLMs via Gradient Multi-Subspace Tuning
- **Authors**: Multiple institutions
- **Innovation**: Framework that unifies search and recommendation within LLMs while:
  - Multi-Subspace Decomposition reduces gradient conflicts
  - Null-Space Projection preserves general-domain knowledge
- **Results**: Outperforms state-of-the-art baselines across both tasks
- **Code**: https://github.com/Polaris-JZ/GEMS

#### 7.2 Dual-View LLM Recommendation
- **Title**: L2Rec: Towards Dual-View Understanding of LLMs for Personalized Recommendation
- **Authors**: Multiple institutions
- **Innovation**: Parameter-level dual-view adaptation via Dual-view Personalized MoE (DPMoE), enabling single LLM backbone to produce complementary behavioral and semantic adaptations.
- **Results**: +9.24% CTR, +3.15% reply rate in online A/B testing
- **Link**: https://arxiv.org/abs/2605.26717

#### 7.3 Dynamic Multimodal Recommendation
- **Title**: TimeMM: Time-as-Operator Spectral Filtering for Dynamic Multimodal Recommendation
- **Authors**: Multiple institutions
- **Innovation**: Time-conditioned spectral filtering framework that maps interaction recency to parametric temporal kernels for dynamic multimodal preference modeling.

---

## 8. WWW 2026 (Dubai, April 13-17, 2026)

### Key Papers

#### 8.1 Thinking-Based Recommendation
- **Title**: ThinkRec: Thinking-based recommendation via LLM
- **Authors**: Multiple institutions
- **Innovation**: Shifts LLM4Rec from System 1 (intuitive) to System 2 (rational) reasoning:
  - Thinking activation mechanism with synthetic reasoning traces
  - Instance-wise expert fusion for personalized reasoning paths
- **Code**: https://github.com/Yu-Qi-hang/ThinkRec

#### 8.2 Industrial Retrieval
- **Title**: GRank: Towards Target-Aware and Streamlined Industrial Retrieval with a Generate-Rank Framework
- **Authors**: Kuaishou
- **Innovation**: Target-aware retrieval framework that bridges accuracy-efficiency gap in large-scale retrieval without structured index.
- **Results**: Significant improvements over tree-based and generative approaches

---

## 9. EMNLP 2025 (Suzhou, China, November 4-9, 2025)

### Conference Stats
- **Proceedings**: 1,810 long papers, 78 system demonstrations, 194 industry track papers
- **Review system**: ACL Rolling Review (ARR)

### Key Topics
- AI/LLM Agents
- Safety and Alignment in LLMs
- Retrieval-Augmented Language Models
- Code Models
- Interpretability and Model Editing

---

## 10. ACL 2026 (San Diego, July 2-7, 2026)

### Key Papers

#### 10.1 Robust NLP
- **Title**: Robertha: Eigenspectrum Regularized Attention for Robust Natural Language Understanding
- **Authors**: Multiple institutions
- **Innovation**: Eigenspectrum Regularization (ESR) for attention mechanisms, improving robustness to embedding corruption while maintaining clean performance.
- **Results**: Competitive performance on 13 GLUE and SuperGLUE tasks

#### 10.2 Structured Text Generation
- **Title**: Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities
- **Authors**: Multiple institutions
- **Innovation**: Teaching models to generate explicit sentence boundaries, improving reasoning by up to 7.7% on GSM8k and 12.5% on DROP.

#### 10.3 Discourse-Aware RAG
- **Title**: Disco-RAG: Discourse-Aware Retrieval-Augmented Generation
- **Authors**: Multiple institutions
- **Innovation**: Incorporates discourse structure into RAG pipeline for improved coherence and relevance.

---

## 11. CIKM 2025 (Seoul, November 10-14, 2025)

### Conference Stats
- **Submissions**: 2,761 (11% increase over previous year)
- **Accepted**: 810 papers (29% acceptance rate)

### Key Papers

#### 11.1 Multi-behavior Recommendation
- **Title**: MEMBER: A Self-Supervised Mixture of Experts Framework for Multi-behavior Recommendation
- **Authors**: Multiple institutions
- **Innovation**: Self-supervised MoE framework for modeling multiple user behaviors in recommendation.
- **Code**: https://github.com/K-Kyungho/MEMBER
- **Link**: https://arxiv.org/abs/2508.19507

#### 11.2 Federated Continual Recommendation
- **Title**: F3CRec: Federated Continual Recommendation
- **Authors**: Multiple institutions
- **Innovation**: First framework jointly addressing federated and continual recommendation with:
  - Client-side: Adaptive Replay Memory
  - Server-side: Item-wise Temporal Mean
- **Code**: https://github.com/Jaehyung-Lim/F3CRec-CIKM-25
- **Link**: https://arxiv.org/abs/2508.04792

#### 11.3 Search-Enhanced Recommendation
- **Title**: GSERec: Benefit from Rich: Tackling Search Interaction Sparsity in Search Enhanced Recommendation
- **Authors**: Renmin University
- **Innovation**: Addresses sparsity in search-enhanced recommendation by leveraging users with rich search interactions to improve representations for sparse users.

---

## 12. AAAI 2026 - Advertising & CTR Focus

### Key Papers

#### 12.1 Tencent Advertising
- **Title**: OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation
- **Authors**: Tencent
- **Innovation**: Architectural-level deep integration of generation and ranking for advertising:
  - Value-aware multi-task decoupling architecture
  - Coarse-to-fine collaborative target awareness
  - Input-output dual-side consistency guarantees
- **Results**: +1.34% GMV-Normal on WeChat Channels advertising
- **Link**: https://arxiv.org/abs/2603.02999

#### 12.2 Tencent RankUp
- **Title**: RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems
- **Authors**: Tencent
- **Innovation**: Mitigates representation collapse in MetaFormer-based recommenders through:
  - Randomized permutation splitting
  - Multi-embedding representations
  - Global token integration
- **Results**: +3.41% GMV (Video Accounts), +4.81% GMV (Moments), +2.12% GMV (Official Accounts)
- **Link**: https://arxiv.org/abs/2604.17878

#### 12.3 Tencent HyFormer
- **Title**: HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction in CTR Prediction
- **Authors**: ByteDance
- **Innovation**: Unified hybrid transformer for CTR prediction:
  - Query Decoding: expands non-sequential features into Global Tokens
  - Query Boosting: enhances cross-query and cross-sequence interactions
  - Bidirectional co-evolutionary paradigm
- **Results**: Fully deployed at ByteDance, serving billions of users daily
- **Link**: https://arxiv.org/abs/2601.12681

---

## 13. Agent Systems & Code Execution

### Key Papers

#### 13.1 Multi-Agent Algorithm Discovery
- **Title**: Discovering Multiagent Learning Algorithms with Large Language Models
- **Authors**: Google DeepMind
- **Innovation**: Uses AlphaEvolve (LLM-powered evolutionary system) to discover multi-agent learning algorithms:
  - VAD-CFR and SHOR-PSRO competitive with state-of-the-art
  - Distilled into minimal solvers: WOP-CFR and PM-PSRO
- **Link**: https://arxiv.org/abs/2602.16928

#### 13.2 Subgoal-Driven LLM Agents
- **Title**: A Subgoal-driven Framework for Improving Long-Horizon LLM Agents
- **Authors**: Google DeepMind
- **Innovation**: Combines inference-time planning with milestone-based RL rewards:
  - Automated failure analysis for web navigation
  - MiRA (Milestoning RL Agent) with dense reward signals
- **Results**: Gemma3-12B achieves 43.0% SR on WebArena-Lite (vs. GPT-4o's 13.9%)
- **Link**: https://arxiv.org/abs/2603.19685

#### 13.3 Agentic Reasoning
- **Title**: AXPO: Agent Explorative Policy Optimization for Multimodal Agentic Reasoning
- **Authors**: NVIDIA, KAIST
- **Innovation**: Tool-call resampling technique to narrow the Thinking-Acting Gap in agentic RL:
  - Fixes thinking prefix and resamples tool calls
  - 8B model surpasses 32B Base on Pass@4
- **Link**: https://arxiv.org/abs/2605.28774

#### 13.4 Deep Reasoning Agent
- **Title**: DOLORES: Deep Reasoning in General Purpose Agents via Structured Meta-Cognition
- **Authors**: Multiple institutions
- **Innovation**: Formal language for structured meta-reasoning that enables just-in-time scaffold construction:
  - 8B version surpasses all evaluated 32B baselines
  - 24.8% improvement over strongest baseline
- **Code**: https://github.com/DeanLight/dolores

#### 13.5 AutoHarness: Code Generation for Games
- **Title**: AutoHarness: improving LLM agents by automatically synthesizing a code harness
- **Authors**: Google DeepMind
- **Innovation**: LLM synthesizes its own code harness to prevent illegal moves in games:
  - Gemini-2.5-Flash outperforms Gemini-2.5-Pro
  - Code-as-Policy achieves higher average reward than GPT-5.2-High
- **Link**: https://arxiv.org/abs/2603.03329

---

## 14. Diffusion Models & Code Generation

### Key Papers

#### 14.1 Stable-DiffCoder
- **Title**: Stable-DiffCoder: Pushing the Frontier of Code Diffusion Large Language Model
- **Authors**: Multiple institutions
- **Innovation**: Block diffusion code model that outperforms autoregressive counterparts:
  - Block diffusion continual pretraining with tailored warmup
  - Block-wise clipped noise schedule
  - Any-order modeling benefits structured code
- **Results**: New SOTA among 8B-scale diffusion code models

#### 14.2 AnCoder: Anchored Code Generation
- **Title**: AnCoder: Anchored Code Generation via Discrete Diffusion Models
- **Authors**: Multiple institutions
- **Innovation**: AnchorTree framework using AST to guide diffusion process:
  - Prioritizes syntactically and semantically salient tokens
  - +65.7% relative improvement in Pass@1 on HumanEval
- **Link**: https://arxiv.org/abs/2602.17688

#### 14.3 Diffusion LLMs for Code
- **Title**: An Empirical Study of Diffusion Large Language Models for Code Generation
- **Authors**: Multiple institutions
- **Innovation**: First comprehensive empirical study of diffusion LLMs for code:
  - Gemini-Diffusion achieves 89.6% on HumanEval (vs. 84.8% for best AR)
  - Stronger length extrapolation ability than AR models
  - Better performance on long code understanding
- **Code**: https://github.com/zhangyitonggg/dllm4code

#### 14.4 IndustryCode Benchmark
- **Title**: IndustryCode: A Benchmark for Industry Code Generation
- **Authors**: Multiple institutions
- **Innovation**: First comprehensive benchmark spanning multiple industrial domains:
  - 579 sub-problems from 125 industrial challenges
  - Covers finance, automation, aerospace, remote sensing
  - Languages: MATLAB, Python, C++, Stata
- **Results**: Claude 4.5 Opus achieves 68.1% accuracy

#### 14.5 RealBench
- **Title**: RealBench: A Repo-Level Code Generation Benchmark Aligned with Real-World Software Development Practices
- **Authors**: Multiple institutions
- **Innovation**: Benchmark aligned with real-world development:
  - UML diagrams as system design input
  - Best test pass rate: 19.39% (significant room for improvement)
  - Detailed design crucial for repo-level generation

#### 14.6 DiffBench & DiffAgent
- **Title**: DiffBench Meets DiffAgent: End-to-End LLM-Driven Diffusion Acceleration Code Generation
- **Authors**: Multiple institutions
- **Innovation**: Benchmark and agent for diffusion model acceleration:
  - 604 prompts covering diverse diffusion architectures
  - DiffAgent achieves 54-82% improvement over direct LLM generation
  - Genetic algorithm-based selector for code refinement

---

## 15. Recommendation Systems - Cross-Conference

### Key Trends

#### 15.1 LLM for Recommendation
- **ThinkRec** (WWW 2026): System 2 reasoning for recommendation
- **L2Rec** (SIGIR 2026): Dual-view LLM understanding
- **GEMS** (SIGIR 2026): Unified search and recommendation
- **CoLLM**: Integrating collaborative embeddings into LLMs

#### 15.2 Generative Recommendation
- **GR4AD** (Kuaishou): Production deployment for advertising
- **OneRec**: Transformer-based sequential transducers
- **TIGER**: Semantic IDs for generative retrieval
- **HSTU**: Trillion-parameter sequential transducers

#### 15.3 CTR Prediction
- **EST** (Alibaba): Efficient scaling laws for CTR
- **GRAB** (Baidu): LLM-inspired sequence-first paradigm
- **HyFormer** (ByteDance): Unified sequence modeling and feature interaction
- **RankUp** (Tencent): High-rank representations for advertising

#### 15.4 Multi-Modal Recommendation
- **TimeMM** (SIGIR 2026): Time-as-Operator spectral filtering
- **MEMBER** (CIKM 2025): Mixture of Experts for multi-behavior

---

## 16. Conference Comparison Summary

| Conference | Year | Submissions | Accepted | Rate | Key Focus |
|-----------|------|-------------|----------|------|-----------|
| ICML 2026 | 2026 | 23,918 | 6,352 | 26.6% | ML theory, RL, diffusion |
| AAAI 2026 | 2026 | ~29,000 | ~4,300 | ~15% | AI broadly, agents, NLP |
| ICLR 2026 | 2026 | 19,525 | 5,355 | 27.4% | Learning representations |
| NeurIPS 2025 | 2025 | 21,575 | 5,290 | 24.5% | ML, deep learning |
| CVPR 2026 | 2026 | 16,092 | 4,089 | 25.4% | Computer vision |
| KDD 2026 | 2026 | TBD | TBD | TBD | Data mining, advertising |
| SIGIR 2026 | 2026 | TBD | TBD | TBD | Information retrieval |
| WWW 2026 | 2026 | TBD | TBD | TBD | Web, recommendation |
| EMNLP 2025 | 2025 | TBD | ~1,810 | TBD | NLP, agents |
| ACL 2026 | 2026 | TBD | TBD | TBD | NLP, language |
| CIKM 2025 | 2025 | 2,761 | 810 | 29% | Knowledge management |

---

## 17. Key Research Directions

### 17.1 LLMs as Foundation for Everything
- LLMs powering recommendation (ThinkRec, L2Rec, GEMS)
- LLMs discovering algorithms (AlphaEvolve, WOP-CFR)
- LLMs generating code (Stable-DiffCoder, AnCoder)
- LLMs as agents (MiRA, AXPO, DOLORES)

### 17.2 Scaling Laws Beyond LLMs
- CTR prediction scaling (EST, GRAB)
- MoE scaling (ICLR 2026 paper)
- Recommendation model scaling (RankUp, HyFormer)

### 17.3 Diffusion Models Renaissance
- Diffusion LLMs for text (ICML 2026 Outstanding Paper)
- Diffusion for code generation (Stable-DiffCoder, AnCoder)
- Diffusion for 3D (CVPR 2026 best papers)
- Diffusion for video generation

### 17.4 Agent Systems
- Multi-agent coordination (AAAI 2026)
- Tool-use optimization (AXPO)
- Long-horizon planning (MiRA)
- Meta-cognition (DOLORES)

### 17.5 Industrial Deployment
- Tencent: OneRanker, RankUp, HyFormer
- Alibaba: EST for Taobao
- Baidu: GRAB for home feed
- Kuaishou: GR4AD for advertising
- ByteDance: HyFormer for Douyin

---

## References

### Conference Proceedings
- ICML 2026: https://icml.cc/virtual/2026/
- AAAI 2026: https://aaai.org/proceeding/aaai-40-2026/
- ICLR 2026: https://openreview.net/group?id=ICLR.cc/2026/Conference
- NeurIPS 2025: https://neurips.cc/virtual/2025/
- CVPR 2026: https://cvpr.thecvf.com/
- KDD 2026: https://kdd2026.kdd.org/
- SIGIR 2026: https://sigir2026.org/
- WWW 2026: https://www2026.thewebconf.org/
- EMNLP 2025: https://2025.emnlp.org/
- ACL 2026: https://2026.aclweb.org/
- CIKM 2025: https://cikm2025.org/

### Paper Sources
- Paper Copilot: https://papercopilot.com/
- Paper Digest: https://www.paperdigest.org/
- OpenReview: https://openreview.net/
- arXiv: https://arxiv.org/

---

*Generated: 2026-07-28*
*Next update: 2026-07-29*
