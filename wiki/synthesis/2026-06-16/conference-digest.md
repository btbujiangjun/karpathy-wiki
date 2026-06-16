---
title: Conference & arXiv Digest — June 2026
type: synthesis
created: 2026-06-16
updated: 2026-06-16
sources: []
tags: [conference-digest, icml-2026, neurips-2025, iclr-2026, aaai-2026, cvpr-2026, kdd-2026, sigir-2026, www-2026, cikm-2025, recsys-2025, acl-2026, emnlp-2025, llm, agents, ctr, recommendation]
---

# Conference & arXiv Digest — June 2026

> Comprehensive survey of recent top-tier conference papers (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, CVPR 2026, KDD 2026, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025, ACL 2026, EMNLP 2025) and recent arXiv preprints covering LLMs, agents, recommendation systems, CTR prediction, generative models, and benchmarks.
> Generated: 2026-06-16

---

## Table of Contents

1. [NeurIPS 2025 Highlights](#neurips-2025-highlights)
2. [ICLR 2026 Highlights](#iclr-2026-highlights)
3. [ICML 2026 Highlights](#icml-2026-highlights)
4. [AAAI 2026 Highlights](#aaai-2026-highlights)
5. [CVPR 2026 Highlights](#cvpr-2026-highlights)
6. [KDD 2026 Highlights](#kdd-2026-highlights)
7. [ACL 2026 & EMNLP 2025 Highlights](#acl-2026--emnlp-2025-highlights)
8. [SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025 Highlights](#sigir-2026-www-2026-cikm-2025-recsys-2025-highlights)
9. [CTR Prediction & Advertising](#ctr-prediction--advertising)
10. [Agent Systems](#agent-systems)
11. [Foundation Models & Architecture](#foundation-models--architecture)
12. [Industry Lab Releases (Google DeepMind, OpenAI, Meta, Microsoft, Anthropic, NVIDIA, ByteDance, Alibaba)](#industry-lab-releases)

---

## NeurIPS 2025 Highlights

NeurIPS 2025 saw ~15,671 submissions with ~4,035 accepted (25.75%). Four Best Papers and three Runner-Ups were awarded.

### Best Papers

#### 1. Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
- **Authors**: Qwen Team (Alibaba Cloud)
- **Affiliation**: Alibaba
- **Venue**: NeurIPS 2025 **Best Paper**
- **Abstract**: Systematically investigates how attention gating affects LLM performance. Compares 30+ gating variants across 15B MoE and 1.7B dense models trained on 3.5T tokens. The core finding: applying an element-wise, head-specific sigmoid gate after Scaled Dot-Product Attention (SDPA) consistently yields the most substantial improvement.
- **Key Innovations**:
  - Introduces non-linearity into the low-rank attention mapping
  - Generates input-dependent sparse gating scores
  - Eliminates the "attention sink" phenomenon
  - Enables larger learning rates (4.0×10⁻³ → 4.5×10⁻³)
  - Improves training stability and long-context extrapolation
- **Impact**: Already deployed in Qwen3-Next; <2% computational overhead
- **Links**: [OpenReview](https://openreview.net/pdf?id=1b7whO4SfY) | [GitHub](https://github.com/qiuzh20/gated_attention)

#### 2. Artificial Hivemind: LLM Diversity & Homogeneity in AI Outputs
- **Authors**: Liwei Jiang et al.
- **Venue**: NeurIPS 2025 **Best Paper** (Datasets & Benchmarks)
- **Abstract**: Investigates the "Artificial Hivemind" phenomenon where LLMs produce homogenous outputs. Introduces metrics: Type-Token Ratio (TTR), N-gram Diversity, Self-BLEU, Semantic Diversity (embedding distance). Reveals that even when prompted with open-ended questions, LLMs exhibit strong intra-model repetition and inter-model homogeneity.
- **Key Innovations**:
  - Formal framework for measuring LLM output diversity
  - Demonstrates societal implications of model monoculture
  - Proposes intervention strategies for increasing diversity

#### 3. Gated Attention Mechanisms for Long-Context LLMs
- **Venue**: NeurIPS 2025 **Best Paper**
- **Abstract**: Addresses attention sink and long-context degradation through gating. Demonstrates stable training at 128K+ context lengths.

#### 4. 1000-Layer Deep RL Networks
- **Venue**: NeurIPS 2025 **Best Paper**
- **Abstract**: Demonstrates that extreme depth (1000 layers) enables self-supervised RL agents to reach goals without explicit reward signals, challenging conventional wisdom about deep RL architectures.

#### 5. Diffusion Training Dynamics: Why Diffusion Models Generalize Instead of Memorizing
- **Venue**: NeurIPS 2025 **Best Paper**
- **Abstract**: Provides theoretical framework explaining why diffusion models generalize beyond training data, with implications for generative model design.

### Runner-Ups

#### RLVR & LLM Reasoning
- **Venue**: NeurIPS 2025 **Runner-Up**
- **Abstract**: Examines whether reinforcement learning with verifiable rewards (RLVR) truly expands LLM reasoning capabilities. Introduces CoT-Pass@K metric.

#### Transductive Online Learning
- **Venue**: NeurIPS 2025 **Runner-Up**
- **Abstract**: Solves a 30-year-old open problem about the value of unlabeled data in online learning.

#### Superposition & Neural Scaling
- **Venue**: NeurIPS 2025 **Runner-Up**
- **Abstract**: Explains how feature superposition drives neural scaling laws.

---

## ICLR 2026 Highlights

ICLR 2026 accepted 223 oral papers from thousands of submissions. The conference was held April 24-28, with dominant trends in agentic AI, multimodal models, and data-centric governance.

### Key Oral Papers

#### Reinforcement Learning & Reasoning

##### The Art of Scaling Reinforcement Learning Compute for LLMs (#154)
- **Authors**: Multiple institutions
- **Key insight**: Systematic study of how to allocate RL compute during LLM post-training. Provides scaling laws for RL training of reasoning models.
- **Links**: [OpenReview](https://openreview.net/forum?id=FMjeC9Msws)

##### LoongRL: Reinforcement Learning for Advanced Reasoning over Long Contexts (#22)
- **Key insight**: Extends RLVR to long-context reasoning tasks, demonstrating that RL training improves multi-turn reasoning quality.
- **Links**: [OpenReview](https://openreview.net/forum?id=o29E01Q6bv)

##### TROLL: Trust Regions Improve Reinforcement Learning for Large Language Models (#170)
- **Key insight**: Applies trust region optimization (inspired by TRPO) to LLM RL training, improving stability and sample efficiency.
- **Links**: [OpenReview](https://openreview.net/forum?id=X9D5MVpPJ9)

##### Why DPO is a Misspecified Estimator and How to Fix It (#7)
- **Key insight**: Shows DPO's theoretical shortcomings as a preference optimization method and proposes corrections.
- **Links**: [OpenReview](https://openreview.net/forum?id=btEiAfnLsX)

##### Token-Importance Guided Direct Preference Optimization (#164)
- **Key insight**: Weights DPO loss by token importance, improving alignment quality without extra supervision.
- **Links**: [OpenReview](https://openreview.net/forum?id=cMEnMVvMw9)

##### Multiplayer Nash Preference Optimization (#168)
- **Key insight**: Extends preference optimization to multi-agent settings using game-theoretic Nash equilibrium concepts.
- **Links**: [OpenReview](https://openreview.net/forum?id=x7aLhLMVn1)

##### Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling (#188)
- **Key insight**: Addresses the "overthinking" problem in reasoning models where models spend excessive compute on easy problems.
- **Links**: [OpenReview](https://openreview.net/forum?id=kdeiRledV6)

#### Agent Systems

##### AgentGym-RL: Open-Source Framework to Train LLM Agents for Long-Horizon Decision Making via Multi-Turn RL (#40)
- **Key insight**: Full-stack framework for training LLM agents with multi-turn RL, supporting complex long-horizon tasks.
- **Links**: [OpenReview](https://openreview.net/forum?id=ZgCCDwcGwn)

##### Reliable Weak-to-Strong Monitoring of LLM Agents (#167)
- **Key insight**: Uses weaker models to monitor stronger agent behavior, enabling scalable oversight.
- **Links**: [OpenReview](https://openreview.net/forum?id=WV7xIboTDK)

##### MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent (#130)
- **Key insight**: Combines RL with memory management for agents operating in long-context environments.
- **Links**: [OpenReview](https://openreview.net/forum?id=k5nIOvYGCL)

##### In-The-Flow Agentic System Optimization for Effective Planning and Tool Use (#70)
- **Authors**: Stanford
- **Key insight**: Optimizes agentic systems in-the-loop, improving planning and tool use through iterative feedback.
- **Links**: [OpenReview](https://openreview.net/forum?id=Mf5AleTUVK) | [arXiv](https://arxiv.org/abs/2510.05592)

##### ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data (#216)
- **Key insight**: Open-source computer-use agent trained on cross-platform GUI interaction data, competing with proprietary agents.
- **Links**: [OpenReview](https://openreview.net/forum?id=yBFUqdJFZn)

##### Agent Data Protocol (#34)
- **Key insight**: Standardized protocol for agent trajectory data, enabling better training and evaluation.
- **Links**: [OpenReview](https://openreview.net/forum?id=tG6301ORHd)

#### Model Architecture & Efficiency

##### Common Corpus: The Largest Collection of Ethical Data for LLM Pre-Training (#1)
- **Key insight**: Open-source dataset of ethically sourced training data, addressing data governance concerns.
- **Links**: [OpenReview](https://openreview.net/forum?id=0wSlFpMsGb)

##### Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Resource (#43)
- **Key insight**: Under equal FLOP budgets, MoE architectures can outperform dense models, challenging the "dense is better" assumption.
- **Links**: [OpenReview](https://openreview.net/forum?id=oIdzliJAeA)

##### ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (#192)
- **Key insight**: Adaptive KV cache compression that allocates more cache to important reasoning tokens.
- **Links**: [OpenReview](https://openreview.net/forum?id=M3CeHnZKNC)

##### MrRoPE: Mixed-radix Rotary Position Embedding (#173)
- **Key insight**: Extends RoPE to support mixed-radix positional encoding, improving length generalization.
- **Links**: [OpenReview](https://openreview.net/forum?id=1J63FJYJKg)

##### Intrinsic Entropy of Context Length Scaling in LLMs (#139)
- **Key insight**: Theoretical analysis of how context length affects model entropy and information capacity.
- **Links**: [OpenReview](https://openreview.net/forum?id=vnipyA8c9V)

##### How Learning Rate Decay Wastes Your Best Data in Curriculum-Based LLM Pretraining (#106)
- **Key insight**: Demonstrates that standard LR decay schedules mismatched with curriculum data ordering hurt pre-training efficiency.
- **Links**: [OpenReview](https://openreview.net/forum?id=T5wkZJqzkz)

##### ECF8: Exponent-Concentrated FP8 — Lossless Compression for LLMs
- **Authors**: Lambda Labs, Stanford, CMU
- **Key insight**: Exploits redundancy in FP8 exponent bits using Huffman coding. Up to 26.9% memory savings on diffusion models, 177.1% throughput gains. Lossless, scales to 671B parameters.

##### OpenThoughts: Data Recipes for Reasoning Models (#174)
- **Key insight**: Releases open-source data recipes and training pipelines for reasoning models, democratizing reasoning model development.
- **Links**: [OpenReview](https://openreview.net/forum?id=7xjoTuaNmN)

##### Mamba-3: Improved Sequence Modeling using State Space Principles (#96)
- **Key insight**: Advances in state space model design, improving upon Mamba-2 with better long-range dependency capture.
- **Links**: [OpenReview](https://openreview.net/forum?id=HwCvaJOiCj)

#### Benchmarks & Evaluation

##### GAIA-2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments (#62)
- **Key insight**: Extends GAIA benchmark to multi-turn, asynchronous agent tasks.
- **Links**: [OpenReview](https://openreview.net/forum?id=9gw03JpKK4)

##### LLMs Get Lost In Multi-Turn Conversation (#94)
- **Key insight**: Systematic study showing that even advanced LLMs struggle with long multi-turn conversations.
- **Links**: [OpenReview](https://openreview.net/forum?id=VKGTGGcwl6)

##### How Reliable is Language Model Micro-Benchmarking? (#88)
- **Key insight**: Reveals statistical unreliability of common micro-benchmarks, proposes corrections.
- **Links**: [OpenReview](https://openreview.net/forum?id=cReExMQLiK)

##### Verifying Chain-of-Thought Reasoning via Its Computational Graph (#105)
- **Key insight**: Uses computational graph analysis to verify CoT reasoning correctness.
- **Links**: [OpenReview](https://openreview.net/forum?id=CxiNICq0Rr)

##### Is it Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort (#97)
- **Key insight**: Detects reward hacking in RL-trained LLMs by analyzing reasoning effort patterns.
- **Links**: [OpenReview](https://openreview.net/forum?id=Gk7gLAtVDO)

---

## ICML 2026 Highlights

ICML 2026 accepted over 6,500 papers, held in Seoul. Key themes: RL for LLMs, synthetic data, efficient training, and trustworthy ML.

### Notable Papers

##### Nonparametric LLM Evaluation from Preference Data
- **Authors**: Dennis Frauen, Athiya Deviyani, Mihaela van der Schaar, Stefan Feuerriegel (LMU Munich)
- **Venue**: ICML 2026
- **Abstract**: Nonparametric framework for evaluating LLMs from preference data without parametric assumptions.

##### SurvDiff: A Diffusion Model for Generating Synthetic Data in Survival Analysis
- **Authors**: Marie Brockschmidt, Maresa Schröder, Stefan Feuerriegel (LMU Munich)
- **Venue**: ICML 2026 **(Spotlight)**
- **Abstract**: Diffusion model tailored for survival analysis data generation with censoring awareness.

##### Revenue Efficiency of Correlated Equilibria in First Price Auctions
- **Authors**: Anders Bo Ipsen, Stratis Skoulakis (Aarhus University)
- **Venue**: ICML 2026 **(Spotlight)**
- **Abstract**: Game-theoretic analysis of auction mechanisms with ML implications.

##### ProbeLLM: Automating Principled Diagnosis of LLM Failures
- **Authors**: Yue Huang, Zhengzhe Jiang, Pin-Yu Chen, Stefan Feuerriegel, Xiangliang Zhang et al.
- **Venue**: ICML 2026
- **Abstract**: Automated diagnostic framework for identifying root causes of LLM failures.

##### Position: ICML Should Treat Hosted LLM APIs as Versioned Dependencies
- **Venue**: ICML 2026 (Position Paper)
- **Abstract**: Argues for drift-audit artifacts when papers rely on hosted LLM APIs.

##### Position: Creating High-Fidelity Synthetic Training Data Should Employ Multi-level Optimization
- **Authors**: Pengtao Xie, Li Zhang, Ruiyi Zhang
- **Venue**: ICML 2026 (Position Paper)
- **Abstract**: Advocates for multi-level optimization approaches in synthetic data generation.

##### Generative Click-through Rate Prediction with Applications to Search Advertising
- **Authors**: Lingwei Kong, Lu Wang, Changping Peng, Zhangang Lin, Ching Law, Jingping Shao (Baidu)
- **Venue**: ICML 2026 / arXiv 2507.11246
- **Abstract**: Two-stage framework: (1) generative pre-training for next-item prediction, (2) fine-tuning within discriminative CTR framework. Deployed on major e-commerce platform; online A/B testing validated.

##### Direct Motion Models for Assessing Generated Videos
- **Authors**: Google DeepMind
- **Venue**: ICML 2025
- **Abstract**: Motion-based metrics for evaluating video generation quality.

##### M+Adam: Low-Precision Training via Mantissa-Exponent Optimization
- **Authors**: Aarhus University
- **Venue**: ICML 2026
- **Abstract**: Novel optimizer for low-precision training by separating mantissa and exponent optimization.

---

## AAAI 2026 Highlights

AAAI 2026 received 23,680 submissions, accepting 4,167 (17.6%). Held in Singapore, January 20-27.

### Outstanding Papers

##### COREA: Confidence-Calibrated Small-Large Language Model Collaboration for Cost-Efficient Reasoning
- **Authors**: Amazon Science
- **Venue**: AAAI 2026
- **Abstract**: Cascades SLM with LLM: SLM attempts queries and produces verbalized confidence scores, deferring to costlier LLM only when confidence is low. RL-based training jointly improves accuracy and calibration. ~21.5% inference cost reduction on out-of-domain math, within 2% of LLM-only performance.
- **Links**: [Amazon Science](https://www.amazon.science/publications/confidence-calibrated-small-large-language-model-collaboration-for-cost-efficient-reasoning)

##### CogniTrust: A Robust Hashing Method with Verifiable Supervision Based on Cognitive Memory
- **Authors**: Gu Yiyang, Zhang Ming et al. (Peking University)
- **Venue**: AAAI 2026
- **Abstract**: Inspired by human memory (episodic, semantic, reconstructive memory), proposes a framework for verifying supervision signals structurally with interpretable label decisions.

##### MPAS: A Parallel Multi-Agent System Based on Graph Message Passing
- **Authors**: Jia Xiaojun et al. (NTU Singapore)
- **Venue**: AAAI 2026 **(Oral)**
- **Abstract**: Breaks sequential communication limitation in multi-agent systems. Reduces communication time from 84.6s to 14.2s. Enhances robustness against backdoor attacks.

##### SECURE: A Fine-Tuning Security Constraint Method
- **Authors**: Jia Xiaojun et al. (NTU Singapore)
- **Venue**: AAAI 2026 **(Oral)**
- **Abstract**: Punishes orthogonal updates to keep models in a "narrow security basin". Reduces 7.6% harmful behaviors, improves performance by 3.4%.

##### LogicCat: A Chain-of-Thought Text-to-SQL Benchmark for Complex Reasoning
- **Venue**: AAAI 2026 (NLP Track)
- **Abstract**: Benchmark for evaluating CoT-based text-to-SQL reasoning with complex logic.

##### SORA: Skewed Orthogonal Rotation Adaptation for PEFT
- **Venue**: AAAI 2026
- **Abstract**: Parameter-efficient orthogonal rotation for feature space transformation, outperforming LoRA and DoRA on NLU/NLG tasks.

### Key Trends
1. Efficiency over scale (SLM+LLM cascades)
2. Mature RAG architectures with cognitive-inspired designs
3. Practical multi-agent coordination under resource constraints
4. Safety and alignment as first-class research concerns
5. AI for social impact moving beyond proof-of-concept

---

## CVPR 2026 Highlights

CVPR 2026 received 16,092 submissions, accepting 4,090 papers (25.4%). Held in Seattle, June 1-5.

### Best Paper

##### Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
- **Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **Affiliations**: Google DeepMind, University College London, University of Oxford
- **Venue**: CVPR 2026 **Best Paper**
- **Abstract**: Unified transformer architecture for 4D dynamic scene reconstruction from video. Jointly infers depth, spatio-temporal correspondence, and camera parameters. Novel query mechanism sidesteps dense per-frame decoding. Up to 300× more efficient than prior methods.
- **Key innovations**:
  - Single feedforward model replaces pipeline of specialized models
  - Query-based decoding interface probes 3D position of any point in space and time
  - Treats dynamic objects same as static ones — no special case
  - SOTA across all 4D reconstruction benchmarks
- **Links**: [arXiv](https://arxiv.org/abs/2512.08924) | [Project Page](https://d4rt-paper.github.io/)

### Best Student Paper

##### Native and Compact Structured Latents for 3D Generation
- **Authors**: Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang
- **Affiliations**: Tsinghua University, Microsoft Research, USTC, Microsoft AI
- **Venue**: CVPR 2026 **Best Student Paper**
- **Abstract**: New approach to 3D generative modeling that significantly improves quality and realism of AI-generated 3D assets through compact structured latent representations.

### Other Notable Papers

##### SAM 3D: 3Dfy Anything in Images
- **Authors**: Jianing Yang, Georgia Gkioxari et al. (Meta AI)
- **Venue**: CVPR 2026 **(Oral)**
- **Abstract**: Extends SAM to 3D, enabling segmentation and 3D reconstruction of any object from images.
- **Links**: [arXiv](https://arxiv.org/abs/2511.16624) | [Code](https://github.com/facebookresearch/sam-3d-objects)

##### SLARM: Streaming and Language-Aligned Reconstruction Model for Dynamic Scenes
- **Venue**: CVPR 2026
- **Abstract**: Unifies dynamic scene reconstruction, semantic understanding, and real-time streaming inference. Language-aligned representations enable semantic querying. Improves motion accuracy by 21%, PSNR by 1.6dB, segmentation mIoU by 20%.

##### Catalyst4D: High-Fidelity 3D-to-4D Scene Editing via Dynamic Propagation
- **Authors**: Shifeng Chen, Yihui Li, Jun Liao, Hongyu Yang, Di Huang
- **Venue**: CVPR 2026
- **Abstract**: Enables editing of dynamic 3D scenes across time dimensions.
- **Links**: [arXiv](https://arxiv.org/abs/2603.12766)

##### HybridDriveVLA: Vision-Language-Action Model with Visual CoT and ToT Evaluation for Autonomous Driving
- **Venue**: CVPR 2026
- **Abstract**: VLA model for autonomous driving with visual chain-of-thought reasoning and tree-of-thought evaluation.

##### Depth Anything 3: Recovering the Visual Space from Any Views
- **Venue**: CVPR 2026
- **Abstract**: Advances in monocular depth estimation from arbitrary viewpoints.

---

## KDD 2026 Highlights

KDD 2026 will be held in Jeju Island, Korea, August 9-13. 2,761 submissions to CIKM 2025 showed 11% increase.

### Notable Papers

##### Beyond Dense Connectivity: Explicit Sparsity for Scalable Recommendation
- **Authors**: Alibaba International Digital Commercial Group
- **Venue**: ArXiv 2604.08011 (KDD 2026 cycle)
- **Abstract**: Proposes explicit sparsity in recommendation model architecture for better scaling with massive behavioral data.

##### TokenFormer: Unify the Multi-Field and Sequential Recommendation Worlds
- **Authors**: Tencent Inc.
- **Venue**: ArXiv 2604.13737
- **Abstract**: Unifies feature interaction models (multi-field) and sequential models under a single transformer-based framework.

##### Retrieve-then-Adapt: Retrieval-Augmented Test-Time Adaptation for Sequential Recommendation
- **Venue**: ArXiv 2604.05379
- **Abstract**: Adapts sequential recommendation models at test time using retrieved relevant sequences.

##### Next-Scale Generative Reranking: A Tree-based Generative Rerank Method at Meituan
- **Authors**: Meituan
- **Venue**: ArXiv 2604.05314
- **Abstract**: Tree-based generative re-ranking system deployed at Meituan for large-scale recommendation.

##### TASR: Training-Free Adaptive Retrieval Stopping
- **Venue**: KDD 2026
- **Abstract**: Adaptive mechanism for determining when to stop retrieval in RAG systems without training.

---

## ACL 2026 & EMNLP 2025 Highlights

### ACL 2026 Key Trends
- 44 accepted papers in LLM Agent area
- Dominant themes: Agents, LLM, Adversarial Robustness, Alignment/RLHF, Reasoning, Code Intelligence
- Top topics: LLM (×20), Agents (×13)

### EMNLP 2025
- 8,174 submissions, 1,811 accepted (22.16%), 1,418 Findings (17.35%)
- Held in-person with 325 oral presentations

#### Notable Papers

##### Is the Top Still Spinning? Evaluating Subjectivity in Narrative Understanding
- **Authors**: Melanie Subbiah, Akankshya Mishra, Grace Kim, Liyan Tang, Greg Durrett, Kathleen McKeown
- **Venue**: EMNLP 2025
- **Abstract**: Introduces Ambiguity Rewrite Metric (ARM) for evaluating faithfulness in narrative summarization, handling subjectivity where binary labels fail.

##### How Many Labels Do Specialised Models Need to Outperform General LLMs?
- **Venue**: EMNLP 2025
- **Abstract**: Identifies performance break-even points across 8 text classification tasks. Shows specialized models need only ~100 samples on average to match general LLMs, with 4-bit quantization having negligible impact.

---

## SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025 Highlights

### SIGIR 2026
- Held in Melbourne, Australia, July 20-24
- Keynote speakers and technical program focused on IR + AI integration

### SIGIR 2025 (Padua)

##### LTP-MMF: Towards Long-Term Provider Max-Min Fairness Under Recommendation Feedback Loops
- **Authors**: Chen Xu, Xiaopeng Ye, Jun Xu, Xiao Zhang, Weiran Shen, Ji-Rong Wen
- **Abstract**: Addresses long-term fairness in recommendation feedback loops using max-min optimization.

##### Feature-Enhanced Neural Collaborative Reasoning for Explainable Recommendation
- **Authors**: Xiaoyu Zhang, Shaoyun Shi, Yishan Li, Weizhi Ma, Peijie Sun, Min Zhang
- **Abstract**: Neural-symbolic approach for explainable collaborative reasoning in recommendation.

### CIKM 2025
- Held in Seoul, November 10-14, 2,761 total submissions (11% increase YoY)

##### Generative Recommendation Models Tutorial
- **Organizers**: Yupeng Hou (UCSD), An Zhang (USTC), Xiang Wang (USTC), Tat-Seng Chua (NUS), Julian McAuley (UCSD)
- **Abstract**: Comprehensive tutorial on tokenization approaches for generative recommendation: item IDs, textual descriptions, semantic IDs.

### RecSys 2025
- Held in Prague, September 22-26

##### LLM-based Recommendation System Agents
- **Authors**: Multiple
- **Venue**: RecSys 2025
- **Abstract**: First LLM-based Recommendation System Agent combining TC and RAG techniques, with access to external RS, database, and vector store.
- **Links**: [ACM DL](https://dl.acm.org/doi/10.1145/3705328.3759334)

---

## CTR Prediction & Advertising

### DGenCTR: Towards a Universal Generative Paradigm for CTR Prediction via Discrete Diffusion
- **Authors**: Multiple
- **Venue**: arXiv
- **Abstract**: Applies discrete diffusion models to CTR prediction, enabling generative paradigm for recommendation.

### FEDIN: Frequency-Enhanced Deep Interest Network for CTR Prediction
- **Authors**: Tencent
- **Venue**: ArXiv 2605.01726
- **Abstract**: Captures latent periodic patterns in user interests using frequency-domain analysis, improving upon DIN architecture.

### Unified Value Alignment for Generative Recommendation in Industrial Advertising
- **Authors**: Tencent
- **Venue**: ArXiv 2605.05803
- **Abstract**: Addresses value alignment in generative recommendation systems for industrial advertising platforms.

### RecGPT-Mobile: On-Device LLMs for User Intent Understanding in Taobao Feed Recommendation
- **Authors**: Taobao & Tmall Group of Alibaba
- **Venue**: ArXiv 2605.04726
- **Abstract**: Deploys on-device LLMs on Taobao for real-time user intent prediction from recent behaviors.

### Generative Click-through Rate Prediction with Applications to Search Advertising
- **Authors**: Lingwei Kong, Lu Wang, Changping Peng, Zhangang Lin, Ching Law, Jingping Shao (Baidu)
- **Venue**: arXiv 2507.11246
- **Abstract**: Two-stage training: generative pre-training for next-item prediction, then fine-tuning in discriminative CTR framework. Deployed on major e-commerce platform. See ICML 2026 section above.

### Beyond Dense Connectivity: Explicit Sparsity for Scalable Recommendation
- **Authors**: Alibaba International
- **Venue**: ArXiv 2604.08011
- **Abstract**: Explicit sparsity pattern in deep recommendation models for better scaling.

### A General Framework for Multimodal LLM-Based Multimedia Understanding in Large-Scale Recommendation Systems
- **Authors**: Meta Platforms
- **Venue**: ArXiv 2605.09338
- **Abstract**: Leverages multimodal LLMs to extract high-dimensional semantic signals from multimedia content for large-scale recommendation.

---

## Agent Systems

### Key Papers from ICLR 2026

##### MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent
- **Abstract**: Multi-conversation RL-based memory management for LLM agents operating in long-context environments.

##### AgentGym-RL: Open-Source Framework to Train LLM Agents for Long-Horizon Decision Making
- **Abstract**: Complete framework for multi-turn RL training of LLM agents, supporting complex long-horizon tasks.

##### Reliable Weak-to-Strong Monitoring of LLM Agents
- **Abstract**: Uses weak models to monitor strong agent behavior for scalable oversight.

##### MCP-SafetyBench: Evaluating LLM Agents on MCP Safety
- **Abstract**: First benchmark for MCP (Model Context Protocol) safety, covering 20 attack types across server, host, and user sides. All evaluated LLMs remain vulnerable.

##### Hilbert: Recursively Building Formal Proofs with Informal Reasoning
- **Authors**: Sumanth Varambally, Thomas Voice, Yanchao Sun, Zhifeng Chen, Rose Yu, Ke Ye
- **Abstract**: Agentic framework combining informal reasoning (LLM) with formal verification (Lean 4). Achieves 99.2% on miniF2F, 70.0% on PutnamBench (422% improvement over best public baseline).

##### Parallel-Synthesis: Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows
- **Authors**: Shikun Liu, Mufei Li, Dongqi Fu, Haoyu Wang, Yinglong Xia, Hong Li, Hong Yan, Pan Li
- **Venue**: arXiv 2606.14672
- **Abstract**: Enables synthesizer to directly consume KV caches from parallel worker agents instead of concatenating text outputs. 2.5×-11× faster TTFT, matches or outperforms text-based synthesis on 7/9 datasets.

### Key Papers from AAAL 2026

##### COREA: Confidence-Calibrated Small-Large Language Model Collaboration
- **See AAAI 2026 section above.**

### Key Papers from NeurIPS 2025

##### A-MEM: Agentic Memory for LLM Agents
- **Abstract**: Zettelkasten-inspired agentic memory system. Each memory entry auto-generates structured notes with dynamic inter-memory links. Outperforms MemGPT on LoCoMo benchmark.

##### AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents
- **Abstract**: Training-free, memory-augmented reasoning framework for agent safety evaluation. Introduces ASSEBench with 2,293 records, 15 risk types, 29 scenarios.

##### AgentChangeBench: Multi-Dimensional Evaluation Framework for Goal-Shift Robustness
- **Abstract**: First benchmark for evaluating LLM agent adaptability when user goals shift mid-conversation. 2,835 sequences across 3 enterprise domains. GPT-4o achieves 92.2% airline recovery.

##### Hogwild! Inference: Parallel LLM Generation via Concurrent Attention
- **Abstract**: Multiple LLM workers run simultaneously with shared attention cache, accelerating rollout generation in RL training. Leverages RoPE properties to avoid recomputation.

##### Flow-GRPO: Training Flow Matching Models via Online RL
- **Authors**: Jie Liu, Gongye Liu, Jiajun Liang, Yangguang Li, Jiaheng Liu, Xintao Wang, Pengfei Wan, Di Zhang, Wanli Ouyang
- **Abstract**: Extends GRPO to flow matching models for efficient text-to-image generation RL training.

---

## Foundation Models & Architecture

### Key Model Releases & Reports

##### Nemotron 3 Super (NVIDIA)
- **Date**: April 2026
- **Abstract**: Open, efficient MoE hybrid Mamba-Transformer model (120B-A12B) for agentic reasoning. Alternates between attention and Mamba-2 layers. Detailed ablations on multi-token prediction, NVFP4 training, synthetic data. Also: Nemotron 3 Nano (4B) and Nemotron 3 Ultra (550B-A55B).
- **Links**: [arXiv](https://arxiv.org/abs/2604.12374)

##### Mamba-3 (NVIDIA / Community)
- **Date**: March 2026
- **Abstract**: Improved state space model design with better long-range dependency handling.
- **Links**: [arXiv](https://arxiv.org/abs/2603.15569)

##### Gated DeltaNet-2
- **Date**: May 2026
- **Abstract**: Decouples erase and write operations in linear attention, improving upon Gated DeltaNet.
- **Links**: [arXiv](https://arxiv.org/abs/2605.22791)

##### MiniMax-M2 Series
- **Date**: May 2026
- **Abstract**: New open-weight model series from MiniMax with strong performance-efficiency tradeoffs.
- **Links**: [arXiv](https://arxiv.org/abs/2605.26494)

##### GLM-5: From Vibe Coding to Agentic Engineering (Zhipu AI)
- **Date**: February 2026
- **Abstract**: Advances LLM capabilities from simple code generation to full agentic engineering workflows.
- **Links**: [arXiv](https://arxiv.org/abs/2602.15763)

##### Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters (StepFun)
- **Date**: February 2026
- **Abstract**: MoE model achieving frontier-level performance with only 11B active parameters.
- **Links**: [arXiv](https://arxiv.org/abs/2602.10604)

##### Ministral 3 (Mistral AI)
- **Date**: January 2026
- **Abstract**: Efficient 3B-class model optimized for on-device deployment.
- **Links**: [arXiv](https://arxiv.org/abs/2601.08584)

##### ERNIE 5.0 Technical Report (Baidu)
- **Date**: February 2026
- **Abstract**: Next-generation ERNIE model with advanced multimodal understanding.
- **Links**: [arXiv](https://arxiv.org/abs/2602.04705)

##### Scaling Embeddings Outperforms Scaling Experts in Language Models
- **Date**: January 2026
- **Abstract**: Shows that scaling embedding dimensions yields better returns than scaling expert count in MoE architectures.
- **Links**: [arXiv](https://arxiv.org/abs/2601.21204)

##### Attention Residuals & Delta Attention Residuals
- **Abstract**: Residual connections in attention layers improve gradient flow and training stability. Delta variant adds further improvements.
- **Links**: [arXiv 2603.15031](https://arxiv.org/abs/2603.15031) | [arXiv 2605.18855](https://arxiv.org/abs/2605.18855)

---

## Industry Lab Releases

### Google DeepMind
- **Gemini 3.5** (May 2026): Frontier intelligence with tool use and action capabilities
- **Gemini Omni** (May 2026): Create anything from anything, starting with video
- **DiffusionGemma** (June 2026): 4× faster text generation using diffusion
- **Gemma 4 12B** (June 2026): Unified, encoder-free multimodal model
- **Gemini for Science** (May 2026): AI experiments for scientific discovery
- **Co-Scientist**: Collaborative AI research partner

### OpenAI
- **ChatGPT Images 2.0**: Breakthrough in text generation within images; multilingual text support; autoregressive mechanisms
- **GPT-5 family**: Complex scientific question answering; 79× efficiency boost in molecular cloning

### Anthropic
- **Claude Fable 5** (June 9, 2026): Latest frontier model
- **Claude Opus 4.7**: Underlying model for Claude Design
- **Claude Design**: Visual creation tool

### Meta AI
- **SAM 3D**: 3D segmentation from images (CVPR 2026)
- **Agentic commerce**: AI-powered shopping agents on Instagram/Facebook/WhatsApp
- **Agentic AI**: Building personalized AI assistants

### NVIDIA
- **Nemotron 3**: Super (120B), Nano (4B), Ultra (550B-A55B) — Hybrid Mamba-Transformer
- **NitroGen**: Generalist gaming AI, ~52% higher success on unseen tasks
- **Isaac GR00T**: Humanoid robot foundation model
- **Alpamayo 2 Super**: New supercomputing architecture

### Alibaba (Qwen)
- **Qwen3-Next**: Gated Attention + Gated DeltaNet; 1M context window
- **Gated Attention** (NeurIPS 2025 Best Paper)
- **RynnBrain**: Open-source robot model

### ByteDance / Kuaishou
- **On the Equivalence Between Auto-Regressive Next Token Prediction and Full-Item-Vocabulary MLE in Generative Recommendation** (Kuaishou)
- **TokenFormer**: Multi-field + sequential recommendation unification

### Microsoft
- **Native and Compact Structured Latents for 3D Generation** (CVPR Best Student Paper)
- **Chain & Hash**: LLM fingerprinting technique

### DeepSeek
- **DeepSeek-V3.2**: Open-source model rivaling GPT-5 on reasoning (99.2% on elite math)
- Seeking $7B in new funding

### xAI
- Active frontier model development and deployment

---

## Recommendations & CTR — Industry Applications

| Paper | Company | Application | Key Results |
|-------|---------|-------------|-------------|
| Generative CTR Prediction (arXiv 2507.11246) | Baidu | Search Advertising | Deployed on world's largest e-commerce platform; online A/B validated |
| DGenCTR (Discrete Diffusion) | Research | CTR Prediction | Generative paradigm for CTR |
| RecGPT-Mobile (arXiv 2605.04726) | Alibaba (Taobao) | Feed Recommendation | On-device LLM for intent understanding |
| FEDIN (arXiv 2605.01726) | Tencent | CTR | Frequency-enhanced DIN |
| Unified Value Alignment (arXiv 2605.05803) | Tencent | Industrial Advertising | GR + alignment |
| Beyond Dense Connectivity (arXiv 2604.08011) | Alibaba International | Scalable Recommendation | Explicit sparsity for scaling |
| Multimodal LLM Understanding (arXiv 2605.09338) | Meta | Multimedia Recommendation | Multimodal LLM features |
| TokenFormer (arXiv 2604.13737) | Tencent | Unified Recommendation | Multi-field + sequential fusion |
| Next-Scale Generative Reranking (arXiv 2604.05314) | Meituan | Reranking | Tree-based generative rerank |
| HORIZON Benchmark (arXiv 2604.17259) | Microsoft | User Behavior | Cross-domain, long-horizon behavior benchmark |

---

## Key Trends Summary

1. **Gated Attention becomes standard**: NeurIPS 2025 Best Paper's gated attention (Alibaba Qwen) is being adopted across the industry (Qwen3-Next, future models)
2. **Hybrid architectures dominate**: Mamba-Transformer hybrids (Nemotron 3, Qwen3.6, Mamba-3) become the norm for long-context efficiency
3. **RL for LLM reasoning matures**: RLVR, GRPO, trust-region methods for LLMs; scaling laws for RL compute
4. **Agent systems go mainstream**: AgentGym, MCP safety, memory agents, parallel agent synthesis
5. **Generative recommendation consolidates**: Tokenization-based generative rec, discrete diffusion for CTR, value alignment in production
6. **On-device LLMs for recommendation**: RecGPT-Mobile, Ministral 3 deploy models at the edge for real-time personalization
7. **4D vision breakthroughs**: D4RT (CVPR Best Paper) unifies dynamic scene reconstruction in a single feedforward model
8. **Efficiency over scale**: SLM+LLM cascades (COREA), ECF8 quantization, ThinKV compression redefine cost-performance Pareto frontier
9. **Safety and alignment become first-class**: Weak-to-strong monitoring, reward hacking detection, security basins, MCP safety benchmarks
10. **Open-source reasoning models**: OpenThoughts, DeepSeek-V3.2 democratize reasoning model development
