---
title: Conference Digest - Top ML/AI Conferences & Recent Papers (2025-2026)
type: synthesis
created: 2026-09-10
updated: 2026-09-10
sources: [arxiv, conference-proceedings]
tags: [ICML, AAAI, NeurIPS, ICLR, KDD, SIGIR, ACL, EMNLP, recommendation-systems, CTR, LLM-agents, generative-models, sequential-modeling]
---

# Conference Digest: Top ML/AI Conferences & Recent Papers (2025-2026)

> Daily compilation of notable papers from major ML/AI conferences and arXiv, focusing on recommendation systems, CTR prediction, LLM agents, generative models, sequential modeling, and benchmarks.

---

## 1. ICLR 2026 (Rio de Janeiro, April 2026)

**Statistics**: 19,525 submissions → 5,355 accepted (27.4% acceptance rate)

### Outstanding Papers

| Paper | Authors | Key Innovation |
|-------|---------|----------------|
| Transformers are Inherently Succinct | Pascal Bergsträßer, Ryan Cotterell, Anthony Widjaja Lin | Proves transformers have inherent succinctness in concept representation |
| LLMs Get Lost In Multi-Turn Conversation | Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville | Identifies and diagnoses LLM performance degradation in multi-turn settings |
| The Polar Express: Optimal Matrix Sign Methods and Muon Algorithm | Noah Amsel, David Persson, Christopher Musco, Robert M. Gower | Advances optimization algorithms for training |

### Key Technical Papers

#### Mamba-3: Improved Sequence Modeling using State Space Principles
- **Innovation**: Enhanced state space model architecture for efficient long-range sequence modeling
- **Significance**: Continues the Mamba line of work on selective state spaces as alternatives to Transformers
- **Link**: [arXiv](https://arxiv.org/abs/2505.mamba3)

#### MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent
- **Innovation**: RL-based memory agent for managing long-context interactions in LLMs
- **Key**: Addresses the challenge of maintaining coherent memory across extended conversations

#### Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Resource
- **Innovation**: Proves MoE architectures can outperform dense models with equivalent computational resources
- **Impact**: Challenges the assumption that dense models are inherently superior

#### In-The-Flow Agentic System Optimization for Effective Planning and Tool Use
- **Innovation**: Real-time optimization framework for agentic systems
- **Application**: Improves planning and tool utilization in LLM-based agents

#### P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling
- **Innovation**: Personalized reward modeling that scales at test time based on user preferences
- **Application**: Enables more personalized AI assistants

#### Verifying Chain-of-Thought Reasoning via its Computational Graph
- **Innovation**: Formal verification of CoT reasoning through computational graph analysis
- **Impact**: Provides theoretical foundations for reasoning verification

#### Benchmarking Empirical Privacy Protection for Adaptations of Large Language Models
- **Key Finding**: Evaluates privacy risks when adapting pre-trained LLMs to downstream tasks
- **Significance**: Important for responsible AI deployment

#### MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science
- **Innovation**: Scalable training environment for biomedical AI agents
- **Application**: Enables development of AI assistants for medical research

---

## 2. ICML 2026 (Seoul, July 2026)

**Statistics**: 23,918 submissions → 6,352 accepted (26.5% acceptance rate)

### Notable Papers

#### Variance Driven Exploration: A Provable and Efficient Methodology for Pure Exploration in Highly Stochastic Environments
- **arXiv**: [2608.21995](https://arxiv.org/abs/2608.21995)
- **Innovation**: Provably efficient exploration strategy for stochastic environments
- **Key**: Addresses the fundamental challenge of exploration in RL

#### Induction Heads Interpolate N-Grams
- **Authors**: Francesco D'Angelo, Oğuz Kaan Yüksel, Swathi Shree Narashiman, Nicolas Flammarion (EPFL, IIT Madras)
- **Innovation**: Theoretical analysis showing how induction heads in transformers interpolate n-gram behavior
- **Significance**: Bridges theoretical understanding of in-context learning

#### SPHERE: Mitigating the Loss of Spectral Plasticity in Mixture-of-Experts for Deep Reinforcement Learning
- **arXiv**: [2605.04712](https://arxiv.org/abs/2605.04712)
- **Innovation**: Addresses spectral plasticity degradation in MoE architectures for RL
- **Code**: [GitHub](https://github.com/sphere-rl/sphere)

#### Causal Representation Learning with Optimal Compression under Complex Treatments
- **Innovation**: Optimal compression framework for causal representation learning
- **Application**: Improved treatment effect estimation

### Reproducibility Initiative
ICML 2026 launched a massive reproduction effort:
- 1,221 community members participated
- 6,816 reproduction logbooks published
- 2,226 papers attempted (34% of conference)
- 35,908 claims judged

---

## 3. AAAI 2026 (Singapore, February 2026)

**Statistics**: ~29,000 submissions → 4,167 accepted (17.6% acceptance rate)

### LLM Reasoning & Safety

#### In-Token Rationality Optimization (InTRO): Towards Accurate and Concise LLM Reasoning via Self-Feedback
- **Authors**: Zhu et al.
- **Innovation**: Token-level exploration with self-generated feedback for accurate and concise reasoning
- **Results**: Up to 20% relative improvement on math-reasoning benchmarks
- **Key**: Addresses the verbosity problem in chain-of-thought reasoning

#### When Safe Unimodal Inputs Collide: Optimizing Reasoning Chains for Cross-Modal Safety in MLLMs
- **Innovation**: Safety-aware Reasoning Path Optimization (SRPO) for multimodal LLMs
- **Dataset**: SSUI - first dataset with interpretable reasoning paths for cross-modal safety
- **Results**: State-of-the-art on RSBench safety benchmark

#### Mitigating Hallucinations in Large Language Models via Causal Reasoning
- **Authors**: Various
- **Innovation**: Causal-DAG construction and reasoning (CDCR-SFT) framework
- **Results**: 95.33% accuracy on CLADDER (surpassing human performance of 94.8%), 10% improvement on HaluEval
- **Dataset**: CausalDR - 25,368 samples with causal DAGs

#### Bonsai: Interpretable Tree-Adaptive Grounded Reasoning
- **Authors**: Kate Sanders, Benjamin Van Durme (Johns Hopkins University)
- **Innovation**: Compositional probabilistic reasoning system with interpretable inference trees
- **Key**: Handles multiple modalities (transcripts, photos, videos, audio, databases)

### AI Alignment

#### SMiLE: Provably Enforcing Global Relational Properties in Neural Networks
- **Authors**: Francobaldi, Lombardi, Lodi
- **Innovation**: Framework for provably enforcing global properties (monotonicity, robustness, fairness)
- **Significance**: Provides full satisfaction guarantees for neural network properties

### Scientific Applications

#### ViG-RAG: Video-aware Graph Retrieval-Augmented Generation
- **Innovation**: Temporal and semantic hybrid reasoning for video understanding
- **Application**: Enhanced video retrieval and question answering

#### RareAgents: Autonomous Multi-disciplinary Team for Rare Disease Diagnosis
- **Innovation**: Multi-agent system for rare disease diagnosis combining multiple medical specialties
- **Impact**: Addresses the challenge of diagnosing rare conditions

---

## 4. NeurIPS 2025 (San Diego, December 2025)

**Statistics**: ~5,526 papers accepted

### Notable Papers

#### TTRL: Test-Time Reinforcement Learning
- **Innovation**: Reinforcement learning approach that operates at test time
- **Key**: Enables model improvement without retraining

#### Perception Encoder: The Best Visual Embeddings Are Not at The Output of The Network
- **Authors**: Daniel Bolya, Po-Yao Huang, et al. (Meta AI)
- **Innovation**: Two alignment methods - language alignment for multimodal modeling, spatial alignment for dense prediction
- **Code**: [GitHub](https://github.com/facebookresearch/perception_models)
- **Impact**: Released models, code, and novel synthetic/human-annotated video dataset

#### EraseFlow: Learning Concept Erasure Policies via GFlowNet-Driven Alignment
- **Status**: Spotlight paper
- **Innovation**: GFlowNet-based approach for concept erasure in neural networks

#### Inference-Time Reward Hacking in Large Language Models
- **Authors**: Hadi Khalaf, et al. (Harvard)
- **Innovation**: Framework for understanding and mitigating reward hacking during inference
- **Significance**: Important for safe deployment of RLHF-trained models

---

## 5. KDD 2026 (Jeju Island, August 2026)

### Recommendation Systems

#### GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Authors**: JD.com team
- **Venue**: SIGIR 2026
- **Innovation**:
  - Page-wise NTP task for denser gradient signals
  - Asymmetric Token Merger for 2× input length reduction
  - GRPO-SR: RL method with hybrid rewards combining dense reward model and relevance gate
- **Results**: 9.5% improvement in click count, 8.7% in transaction count (JD App production deployment)
- **Link**: [arXiv](https://arxiv.org/abs/2604.14878)

#### OneRank: Unified Transformer-Native Ranking Architecture for Multi-Task Recommendation
- **Authors**: Jiakai Tang, Sunhao Dai, Kun Wang, et al. (Alibaba/Peking University)
- **Innovation**:
  - Eliminates encoder-predictor decoupling
  - Task-private channels for forward and backward optimization
  - Dynamic matching-based scoring replacing static MLPs
- **Results**: Consistently outperforms MMoE, PLE, DCMT, ResFlow across all tasks
- **Significance**: New architectural paradigm for multi-task recommendation

#### MixFormer: Co-Scaling Up Dense and Sequence in Industrial Recommenders
- **Authors**: Xu Huang, Hao Zhang, et al.
- **Innovation**:
  - Unified Transformer using shared parameters for sequence and dense feature interactions
  - User-item decoupling strategy for computational efficiency
  - Addresses the fundamental tension between sequence and dense scaling
- **Application**: Industrial-scale recommendation systems

#### IntuRec: Intuition-Guided Latent Reasoning for LLM-Based Recommendation
- **Innovation**: Two-stage framework extracting and injecting recommendation intuition for latent reasoning
- **Key**: Uses beam search for candidate generation, then cross-attention for intuition embedding
- **Comparison**: Outperforms ReaRec, LatentR3, OnePiece baselines

#### Climber-Pilot: A Non-Myopic Generative Recommendation Model
- **Authors**: Da Guo, Shijia Wang, et al.
- **Innovation**:
  - Distills long-horizon foresight into model parameters during training
  - Attention-level control for retrieval instruction following
- **Application**: Large-scale industrial recommendation with single-step inference efficiency

#### From Scaling to Structured Expressivity: Rethinking Transformers for CTR Prediction
- **Innovation**: Field-Aware Transformer (FAT) with field-centric parameters
- **Key Insight**: CTR data demands combinatorial reasoning, not sequential compositionality
- **Results**: +4.38% AUC improvement, +2.33% CTR in live production (Taobao)
- **Theoretical**: Formal scaling law based on Rademacher complexity

#### MergeRec: Model Merging for Data-Isolated Cross-Domain Sequential Recommendation
- **Innovation**: Model merging framework for cross-domain recommendation without data sharing
- **Key**: Privacy-preserving approach using only model parameters
- **Results**: 17.21% improvement in Recall@10

---

## 6. SIGIR 2026 (Melbourne, July 2026)

### Generative Recommendation

#### GenRec (JD.com) - See KDD section above
- **Deployment**: JD App production system
- **Scale**: 560 million user interaction sequences

#### L2Rec: Dual-View Understanding of LLMs for Personalized Recommendation
- **Innovation**: Leverages both item-centric and user-centric views in LLM-based recommendation

---

## 7. ACL 2026

### Agent Systems

#### COMPASS: Enhancing Agent Long-Horizon Reasoning with Evolving Context
- **Authors**: Guangya Wan, et al. (Google Cloud AI, UVA)
- **Innovation**: Hierarchical framework separating tactical execution, strategic oversight, and context organization
- **Components**:
  1. Main Agent for reasoning and tool use
  2. Meta-Thinker for monitoring and strategic interventions
  3. Context Manager for maintaining relevant progress briefs
- **Results**: Up to 20% relative improvement on GAIA, BrowseComp, and Humanity's Last Exam
- **Comparison**: Matches established DeepResearch agents with test-time scaling

#### FlowSearch: Advancing Deep Research with Dynamic Structured Knowledge Flow
- **Innovation**: Multi-agent coordination with dynamic structured knowledge flow
- **Results**: Outperforms OpenAI-DR, Gemini-DR, Manus on GAIA (82.42% vs 73.30% for Manus)
- **Key**: Structured task decomposition more critical than model size alone

---

## 8. EMNLP 2025/2026

### Sequential Modeling

#### PILL: Probing-based InfiLling with preset-Length-free decoding for Diffusion Language Models
- **Status**: Accepted at EMNLP 2026
- **Innovation**: Efficient infilling method for DLMs requiring no preset initial length
- **Results**: +4.8 average pass rate on code, +6.0 BLEU-2 on text, 1.82× faster than baselines
- **Code**: Available on GitHub

---

## 9. WWW 2026 (Dubai, June-July 2026)

### Large-Scale Sequence Modeling

#### Make It Long, Keep It Fast: End-to-End 10k-Sequence Modeling at Billion Scale on Douyin
- **Authors**: Lin Guan, et al. (ByteDance)
- **Innovation**: End-to-end sequence modeling at 10k length for billion-scale recommendation
- **Application**: Douyin (TikTok China) production system
- **Significance**: Demonstrates feasibility of long-sequence modeling in production

---

## 10. RecSys 2025 / CIKM 2025

### Cross-Domain & Sequential Recommendation

#### LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders
- **Authors**: Zheng Chai, et al.
- **Innovation**: Scaling long sequence modeling in production recommendation systems
- **Application**: Industrial deployment

---

## 11. CTR Prediction & Advertising

### EST: Efficiently Scalable Transformer for CTR Prediction
- **Authors**: Mingyang Liu, Yong Bai, et al. (Alibaba)
- **Innovation**:
  - Fully unified modeling without lossy aggregation
  - Lightweight Cross Attention (LCA) pruning redundant self-interactions
  - Content Sparse Attention (CSA) for dynamic behavior selection
- **Results**: Power-law scaling relationship, +3.27% RPM, +1.22% CTR (Taobao production)
- **Significance**: First practical pathway for scalable industrial CTR prediction

### IDProxy: Cold-Start CTR Prediction with Multimodal LLMs
- **Authors**: Yubin Zhang, et al. (Xiaohongshu/RedNote)
- **Innovation**: MLLM-based proxy embeddings for cold-start items
- **Deployment**: Content Feed and Display Ads on Xiaohongshu (300M+ MAU)
- **Results**: +0.22% time spent, +0.39% reads, +1.93% impressions in online A/B tests

### CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer
- **Authors**: David Pardoe, et al. (LinkedIn)
- **Innovation**:
  - Multi-tower prediction heads for post-scoring signals
  - Self-gated attention for training stability
  - Timestamp-based RoPE for temporal relationships
  - Session masking for train-serve consistency
- **Results**: +11.04% CTR lift over production LiRank baseline
- **Deployment**: LinkedIn advertising platform main traffic

### Dual-Stream MLP is All You Need for CTR Prediction
- **Authors**: Kesha Ou, et al. (Renmin University, ByteDance, Meituan)
- **Innovation**: Knowledge distillation from dual-stream teacher to simple MLP student
- **Key**: Achieves SOTA with vanilla MLP structure
- **Code**: [GitHub](https://github.com/RUCAIBox/DS-MLP)

### UniCon: Unified Context-Centric Modeling for CTR Prediction
- **Innovation**: Context-unit-level organization bridging history and prediction targets
- **Results**: +3.09% RPM, +2.07% CTR (Meituan production)

### Generative CTR Prediction with Applications to Search Advertising
- **Innovation**: Two-stage generative pre-training + discriminative fine-tuning
- **Deployment**: Major e-commerce platform production system
- **Results**: +1.32% CTR, +1.66% RPM over baseline

---

## 12. LLM Agent Systems

### Google DeepMind

#### A Subgoal-driven Framework for Improving Long-Horizon LLM Agents
- **Authors**: Taiyi Wang, Sian Gooding, Florian Hartmann, Oriana Riva, Edward Grefenstette
- **Innovation**:
  - SGO: Real-time subgoal decomposition for planning
  - MiRA: Milestone-based RL training framework
- **Results**:
  - Gemini enhanced by ~10% on WebArena-Lite
  - Gemma3-12B: 6.4% → 43.0% success rate
  - Surpasses GPT-4-Turbo (17.6%), GPT-4o (13.9%), WebRL (38.4%)

### Meta AI

#### ChronoMem: Version Control and Semantic Rollback for LLM Agent Memory
- **Innovation**: Semantic version-control layer for agentic memory in Google's Agent Development Kit
- **Features**:
  - Whole-memory snapshots at each write
  - Natural-language rollback requests
  - Post-exposure evaluation protocol
- **Significance**: First open-source system for systematic semantic global memory rollback

### Multi-Agent Systems

#### Eureka: Task-Conditioned Meta-Agent Orchestration for Scientific Discovery
- **Innovation**: Dynamic obligation graph with acceptance semantics for long-horizon tasks
- **Results**:
  - 170/170 recursive long-horizon tasks completed
  - 3,948 acceptance certificates
  - Median model-input context reduced from 9,490 to 4,005 tokens

#### Procedural Graphs: Self-Evolving Execution Structures for LLM Agents
- **Innovation**: Organizes procedural knowledge into (procedure, relation, procedure) triplets
- **Key**: Self-evolving through LLM refiner comparing failed vs successful trajectories
- **Significance**: Addresses planning hallucination, drift, and repetitive loops

---

## 13. Generative Models & Sequential Modeling

### Set Diffusion: Interpolating Token Orderings Between Autoregression and Diffusion
- **Innovation**: Framework for interpolating between AR and diffusion decoding
- **Key**: Supports flexible-position, flexible-length token sets
- **Advantages**: Better speed-quality tradeoffs, KV cache updates after every step

### ARPG: Autoregressive Image Generation with Randomized Parallel Decoding
- **Innovation**: Decoupled two-pass decoding for random-order training
- **Results**: FID 1.83 with 32 steps (30× speedup over raster-order)
- **Application**: ImageNet-1K 256×256 benchmark

### Evo: Duality Latent Flow Model for Unified AR and Diffusion Generation
- **Innovation**: Theoretical unification of AR and diffusion as discretizations of shared probabilistic flow
- **Scale**: 8B parameter model
- **Results**: SOTA or competitive on 15 benchmarks including GSM8K, ARC-C, HumanEval, MBPP

### Variational Learning for Insertion-based Generation
- **Innovation**: Insertion Process (IP) learning where to insert, what to insert, and when to terminate
- **Application**: Goal-conditioned planning and molecular string generation

---

## 14. Benchmarks & Evaluation

### NeurIPS 2025 E2LM Competition: Early Training Evaluation of Language Models
- **Innovation**: Evaluation methodology for measuring early training progress
- **Scale**: 0.5B, 1B, and 3B parameter models with checkpoints up to 200B tokens
- **Significance**: Makes LLM research more systematic from earliest development phases

### EigenBench: A Comparative Behavioral Measure of Value Alignment
- **Innovation**: Benchmark for measuring AI value alignment through behavioral comparison

### PhyWorldBench: Physical Realism in Text-to-Video Models
- **Innovation**: Comprehensive evaluation of physical realism in video generation

---

## 15. Key Trends & Observations

### 1. Generative Recommendation Goes Mainstream
- Multiple production deployments (JD.com, Meituan, Taobao, LinkedIn, Xiaohongshu)
- Shift from retrieval-based to generation-based item recommendation
- GRPO/RLHF alignment becoming standard

### 2. Transformer-Native CTR Prediction
- Moving beyond encoder-predictor decoupling
- Unified sequence and feature interaction modeling
- Power-law scaling relationships discovered

### 3. Agent Systems Mature
- Hierarchical architectures (COMPASS, Eureka)
- Memory management innovations (ChronoMem)
- Subgoal-based planning (MiRA)

### 4. Diffusion-AR Hybrids
- Theoretical unification of AR and diffusion
- Practical benefits: infilling, parallel decoding, quality-efficiency tradeoffs

### 5. Production Scale Deployments
- Almost every major paper includes online A/B test results
- Focus on inference efficiency and latency
- End-to-end optimization replacing multi-stage pipelines

### 6. Reproducibility & Open Science
- ICML 2026 reproduction initiative (34% of papers attempted)
- Growing emphasis on code release
- Standardized benchmarks enabling comparison

---

## References

### Conference Proceedings
- ICLR 2026: https://iclr.cc/virtual/2026/
- ICML 2026: https://icml.cc/virtual/2026/
- AAAI 2026: https://aaai.org/proceeding/aaai-40-2026/
- NeurIPS 2025: https://neurips.cc/virtual/2025/
- KDD 2026: https://kdd2026.org/
- SIGIR 2026: https://sigir2026.org/

### Paper Collections
- RecSys Papers 2025-2026: https://huggingface.co/datasets/yufan/recsys-papers-2025-2026
- Paper Digest: https://www.paperdigest.org/
- Papers With Code: https://paperswithcode.com/

---

*Generated on 2026-09-10 by karpathy-wiki*
