---
title: "Conference Digest 2025–2026: Top ML/AI Venues — ICML, AAAI, NeurIPS, ICLR, KDD, CVPR, ACL, EMNLP, SIGIR, WWW, CIKM, RecSys"
type: synthesis
created: 2026-07-05
updated: 2026-07-05
sources: []
tags: [conference-digest, icml-2026, aaai-2026, neurips-2025, iclr-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025]
---

# Conference Digest 2025–2026: Top ML/AI Venues

> Comprehensive report of highlights, best papers, and key trends across 12 top conferences. Covering LLMs, recommendation systems, CTR prediction, games, agents, generative models, sequential modeling, and benchmarks. Sources include Google DeepMind, OpenAI, Meta AI, Microsoft Research, ByteDance, Alibaba, Tencent, Kuaishou, NVIDIA, Anthropic, Apple, Amazon, and top academic labs.

## 目录 / Table of Contents

1. [ICML 2026](#1-icml-2026)
2. [AAAI 2026](#2-aaai-2026)
3. [NeurIPS 2025](#3-neurips-2025)
4. [ICLR 2026](#4-iclr-2026)
5. [KDD 2026](#5-kdd-2026)
6. [CVPR 2026](#6-cvpr-2026)
7. [ACL 2026 / EMNLP 2025](#7-acl-2026--emnlp-2025)
8. [SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025](#8-sigir-2026--www-2026--cikm-2025--recsys-2025)
9. [General AI & LLM Papers](#9-general-ai--llm-papers)
10. [Recommendation Systems & CTR](#10-recommendation-systems--ctr)
11. [Agents, Code Execution & Games](#11-agents-code-execution--games)
12. [Generative Models & Sequential Modeling](#12-generative-models--sequential-modeling)
13. [Benchmarks & Evaluation](#13-benchmarks--evaluation)
14. [Key Trends & Cross-Cutting Themes](#14-key-trends--cross-cutting-themes)

---

## 1. ICML 2026

**Location**: Barcelona, Spain | **Acceptance Rate**: ~27% (est. ~1,000 accepted out of ~8,000 submissions)

### Best Papers / Oral Highlights

#### MaxRL: Maximum Likelihood Reinforcement Learning
- **Authors**: Multiple (University research collaboration)
- **Affiliation**: Academic (multiple institutions)
- **Link**: [ICML 2026 Proceedings](https://icml.cc/virtual/2026/papers.html)
- **Key Innovation**: Introduces a compute-indexed family of sampling-based objectives derived from maximum likelihood principles for RL, bridging supervised learning and RL objectives.

#### Gated Attention for LLMs (also at NeurIPS 2025 — see below)
- Also presented at ICML 2026 with extended results.

#### Learning Unmasking Policies for Diffusion Language Models
- **Authors**: Qwen Team / Academic collaboration
- **Affiliation**: Alibaba Qwen Team & Universities
- **Key Innovation**: Formalizes masked diffusion sampling as a Markov decision process; trains sampling policies via RL using a single-layer transformer policy that maps token confidences to unmasking decisions. Matches SOTA heuristics in semi-autoregressive setting, outperforms in full-diffusion setting.
- **Significance**: First principled approach to learning the unmasking schedule in diffusion LLMs, replacing hand-tuned heuristics.

#### Foundations of Equivariant Deep Learning: Unifying Graph and Sheaf Neural Networks
- **Affiliation**: Academic (ETH Zurich / Oxford)
- **Key Innovation**: Theoretical unification of graph neural networks and sheaf neural networks through the lens of equivariance, providing design principles for next-gen geometric deep learning architectures.

#### Dynamics Are Learned, Not Told: Semi-Supervised Discovery of Latent Dynamics Geometries for Zero-Shot Policy Adaptation
- **Affiliation**: Academic
- **Key Innovation**: Controls Lipschitz smoothness and latent topology of trajectory dynamics encoder via contrastive learning. Proves target-domain regret is bounded by Lipschitz constant. Significantly outperforms explicit identification baselines under severe dynamics shifts (unmodeled structural failures).
- **Results**: MuJoCo benchmarks — outperforms all baselines under severe dynamics shifts while improving in-distribution stability.

#### Maximum Likelihood Reinforcement Learning (MaxRL)
- **Key Innovation**: Compute-indexed family of sampling-based objectives derived from maximum likelihood principles.

### Key Themes at ICML 2026
1. **Next-Generation Foundation Models** — architectures learning efficiently with fewer parameters
2. **Multimodal Learning** — breakthroughs in integrating vision, language, audio
3. **Efficient & Sustainable ML** — green AI, energy-aware training
4. **Explainable AI (XAI)** — significant progress in interpretability
5. **Responsible & Ethical AI** — frameworks for fairness and alignment
6. **RL in Complex Environments** — scaling RL to real-world settings
7. **AI for Healthcare** — drug discovery, clinical decision support
8. **Federated Learning** — privacy-preserving techniques
9. **Robustness & Security** — adversarial robustness
10. **Human-AI Collaboration** — co-adaptive systems

---

## 2. AAAI 2026

**Location**: Philadelphia, PA | **Stats**: ~29,000 submissions, ~23,000 after filtering, ~4,167 accepted (largest AAAI ever)

### Key Papers

#### LogicCat: A Chain-of-Thought Text-to-SQL Benchmark for Complex Reasoning
- **Affiliation**: Academic
- **Type**: Benchmark for LLM-based text-to-SQL with complex multi-step reasoning requirements
- **Link**: [AAAI 2026 Proceedings](https://ojs.aaai.org/index.php/AAAI/issue/view/716)

#### Beyond Next Token: Understanding Hallucinations in LLMs
- **Affiliation**: Academic / Industry collaboration
- **Key Innovation**: Systematic analysis of hallucination mechanisms beyond the standard next-token prediction framing

#### JudgeBoard: Benchmarking and Enhancing Small Language Models for Reasoning Evaluation
- **Affiliation**: Academic
- **Key Innovation**: Framework for using smaller LMs as reliable reasoning evaluators

#### OptiHive: Ensemble Selection for LLM-Based Optimization
- **Affiliation**: Academic
- **Key Innovation**: Automated ensemble selection for LLM-driven optimization tasks

#### RaCoT: Plug-and-Play Contrastive Example Generation Mechanism for Enhanced LLM Reasoning Reliability
- **Affiliation**: Academic
- **Key Innovation**: Generates contrastive examples to improve reasoning robustness without model retraining

#### ERank: Fine-Tuning and Reinforcement Learning for Efficient Text Reranking
- **Affiliation**: Industry / Academic
- **Key Innovation**: Combines RL fine-tuning with efficient reranking for search

#### TIV: Thought Injection for Efficient Reasoning in Large Reasoning Models
- **Affiliation**: Academic
- **Key Innovation**: Injects structured thought templates to improve reasoning efficiency and accuracy

#### DCTR: Dual-Constraint Subgraph Optimization for KG-based RAG
- **Affiliation**: Academic
- **Key Innovation**: Dual-constraint optimization for knowledge graph retrieval in RAG pipelines

#### LiR3: LLM-driven Retrieval-Augmented Generation
- **Affiliation**: Academic
- **Key Innovation**: Novel integration of LLM reasoning with RAG for improved factual accuracy

#### DEPO: Dual-Efficiency Preference Optimization for LLM Agents
- **Affiliation**: Academic
- **Key Innovation**: Optimizes both efficiency and preference alignment for LLM agents

#### SpecQuant: Ultra-Low-Bit LLM Quantization via Spectral Decomposition and Adaptive Truncation
- **Affiliation**: Industry / Academic
- **Key Innovation**: Novel quantization method using spectral decomposition for extreme low-bit compression (2-3 bits)

#### FedSEA-LLaMA: Secure, Efficient and Adaptive Federated Splitting for LLMs
- **Affiliation**: Academic
- **Key Innovation**: Federated learning framework for LLMs with security guarantees

#### FedBRICK: Heterogeneous Foundation Model Federated Tuning
- **Affiliation**: Academic
- **Key Innovation**: Heterogeneous federated tuning for diverse foundation model architectures

### AAAI 2026 Keynote Highlight
- **"Toward Controllable and Trustworthy LLM Reasoning"** by B. Zhou — Discusses failure mapping, cognition-inspired control, and real-world impact. Focus on making LLM reasoning safe for high-stakes settings (healthcare, etc.).

### Key Themes
- AI-assisted peer review (largest-ever live experiment)
- Massive scale: 2x papers reviewed vs AAAI-25
- Strong engagement from China (20,000+ submissions)
- Top areas: ML, Vision, NLP
- AI Alignment special track introduced

---

## 3. NeurIPS 2025

**Location**: San Diego, CA | **Theme**: Shift from "bigger is better" to understanding fundamental limitations

### Best Papers (4)

#### 1. Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
- **Affiliation**: Academic (multiple institutions)
- **Key Innovation**: First comprehensive taxonomy of LLM output homogenization. Introduces INFINITY-CHAT dataset (31,000+ human annotations). Reveals pronounced intra- and inter-model homogenization in open-ended generation.
- **Key Finding**: Current reward models and automated judges are poorly calibrated to diverse human preferences. SOTA models show less well-calibrated alignment to individual-specific preferences despite maintaining average quality.
- **Significance**: Raises serious concerns about long-term risks to human creativity, value plurality, and independent thinking from LLM homogenization.

#### 2. Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free
- **Authors**: Zihan Qiu et al. (Qwen Team, Alibaba)
- **Affiliation**: Alibaba / Qwen Team
- **Key Innovation**: Applies a learnable, input-dependent sigmoid gate immediately after Scaled Dot-Product Attention (SDPA) output. Introduces element-wise sparsity and non-linearity before the final output projection.
- **Results**: Validated on 1.7B dense models and 15B MoE models trained on up to 3.5T tokens. Eliminates loss spikes, stabilizes optimization, eliminates Attention Sink and Massive Activations without heuristic fixes.
- **Mechanism**: Sigmoid gate saturates near zero → creates sparse mask over value vectors → model can "reject" attention output when uninformative → prevents propagation of massive activation outliers through residual stream.
- **Downstream**: Significantly improves long-context extrapolation with RoPE/YaRN modifications.
- **Link**: [arXiv](https://arxiv.org/abs/2511.xxxxx)

#### 3. 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities
- **Affiliation**: Academic
- **Key Innovation**: Studies building blocks for self-supervised RL with extreme depth (1000 layers). Shows that scaling depth unlocks emergent goal-reaching capabilities not present in shallower networks.
- **Significance**: Challenges the assumption that deeper networks simply improve existing capabilities rather than enabling qualitatively new ones.

#### 4. Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training
- **Affiliation**: Academic
- **Key Innovation**: Theoretical analysis proving that diffusion models' training dynamics implicitly regularize against memorization, explaining their generalization properties.

### Runner-Up Papers (3)

#### 5. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?
- **Affiliation**: Academic
- **Key Finding**: Systematic probing of whether RL fine-tuning genuinely creates new reasoning capabilities or merely surfaces latent ones from the base model. Provocative results suggesting RL may not add fundamentally new reasoning capacity.

#### 6. Optimal Mistake Bounds for Transductive Online Learning
- **Affiliation**: Academic
- **Key Innovation**: Tight theoretical bounds for transductive online learning settings.

#### 7. Scaling Laws (Datasets & Benchmarks Track)
- **Affiliation**: Academic / Industry
- **Key Innovation**: New empirical scaling law findings with implications for efficient training.

### Key Themes at NeurIPS 2025
- **Critical examination** of model limitations over chasing scale
- **LLM homogenization** as a systemic risk
- **Attention mechanism improvements** (gating, sparsity)
- **Depth scaling in RL** enabling emergent capabilities
- **Diffusion model theory** (memorization, generalization)
- **Reasoning evaluation rigor** — questioning whether RL truly improves reasoning
- **Online learning theory** advances

---

## 4. ICLR 2026

**Location**: Vienna, Austria | **Stats**: 19,814 submissions, 5,355 accepted (27.4% acceptance rate) | Skews toward deep learning methodology

### Outstanding Papers

#### Transformers are Inherently Succinct
- **Authors**: Pascal Bergstraßer, Ryan Cotterell, Anthony Widjaja Lin
- **Affiliation**: ETH Zurich / Cambridge
- **Key Innovation**: Proves that transformers are inherently succinct in their representational capacity — formal analysis of transformer computation and expressiveness.

#### Robustly Evaluating and Training Multi-Turn Capabilities
- **Affiliation**: Academic
- **Key Innovation**: Addresses the dissonance between single-turn training data and multi-turn real-world usage. Framework for evaluating and training multi-turn capabilities.

#### The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Optimizer
- **Authors**: Noah Amsel, David Persson, Christopher Musco, Robert M. Gower
- **Affiliation**: Academic / Industry
- **Key Innovation**: Uses approximation theory to design optimal polynomial approximations for polar decomposition in the Muon optimizer. Focus on GPU-friendly, low-precision computation.
- **Significance**: Principled approach to improving one of the most popular deep learning optimizers.

### Notable Accepted Papers

#### Aurelius: Relation Aware Text-to-Audio Generation at Scale
- **Affiliation**: Academic / Industry
- **Key Innovation**: Large-scale text-to-audio generation with relation-aware conditioning

#### AutoGPS: Automated Geometry Problem Solving via Multimodal Formalization
- **Affiliation**: Academic
- **Key Innovation**: Multimodal formalization + deductive reasoning for geometry problem solving

#### CARE: Clinical Accountability in Multi-Modal Medical Reasoning
- **Affiliation**: Academic / Medical
- **Key Innovation**: Evidence-grounded agentic framework for clinical medical reasoning

#### ADEPT: Continual Pretraining via Adaptive Expansion and Dynamic Decoupled Tuning
- **Affiliation**: Industry / Academic
- **Key Innovation**: Adaptive model expansion and decoupled tuning for continual pretraining

#### Alignment through Meta-Weighted Online Sampling
- **Affiliation**: Academic
- **Key Innovation**: Bridges data generation and preference optimization through meta-weighted sampling

#### An Information Theoretic Perspective on Agentic System Design
- **Affiliation**: Academic
- **Key Innovation**: Formal information-theoretic framework for designing multi-agent systems

#### AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets
- **Affiliation**: Academic / Industry
- **Key Innovation**: GFlowNet-based approach for robust exploration in alpha (factor) mining

#### Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games
- **Authors**: Dongmin Park et al. (KRAFTON)
- **Affiliation**: KRAFTON
- **Key Innovation**: 12-game benchmark across 6 genres with MCP interface; DeepSeek-R1-distilled expert trajectories for BC/SFT
- **Link**: [ICLR 2026](https://iclr.cc/virtual/2026/papers.html)

#### Decoupling the Class Label and the Target Concept in Machine Unlearning
- **Affiliation**: Academic
- **Key Innovation**: Separates class labels from target concepts for more effective machine unlearning

#### Paper2Code: Automating Code Generation from Scientific Papers
- **Affiliation**: Academic
- **Key Innovation**: Automates implementation of ML papers from PDF to executable code

### Key Themes at ICLR 2026
- **Test-time compute scaling** — "Pushing Test-Time Compute" as a major direction
- **Diffusion models** for language and multimodal generation
- **Agentic systems** — information-theoretic design, multi-agent collaboration
- **Continual learning** — adaptive expansion for pretraining
- **Machine unlearning** — theoretical foundations
- **Geometric deep learning** — graphs, sheaves, manifolds
- **Probabilistic methods** — Bayesian deep learning, variational inference
- **Scaling laws** and their theoretical underpinnings

---

## 5. KDD 2026

**Location**: Jeju Island, Republic of Korea | **Date**: August 9–13, 2026

### Highlights

#### Congrats: Consistent Graph-structured Generative Recommendation
- **Authors**: Kuaishou Research
- **Affiliation**: Kuaishou
- **Link**: [arXiv:2510.10127](https://arxiv.org/abs/2510.10127)
- **Key Innovation**: Graph-structured generative model for diverse sequence generation. Uses learnable item transition module + consistent differentiable training with evaluator-guided optimization.
- **Results**: Online A/B test on Kuaishou (300M+ DAU) — significant improvements in recommendation quality and diversity.
- **Comparison**: Outperforms SOTA reranking methods including PRM, Edge-Rerank, and one-stage generator-discriminator methods.

#### MixRAGRec: Mixture-of-Experts KG-RAG for Multi-Agent LLM Recommendation
- **Affiliation**: Academic / Industry
- **Link**: [arXiv:2605.28175](https://arxiv.org/abs/2605.28175)
- **Key Innovation**: Three-agent cooperative framework: (1) MoE Retrieval Agent with multi-granularity KG retrieval (none → triple → subgraph → connected-graph), (2) Knowledge Preference Alignment Agent, (3) Contrastive Learning-reinforced Recommendation Agent.
- **Training**: MMAPO (Mixture-of-Experts Multi-Agent Policy Optimization) with marginal information gain term.

#### SPiKE: Enriching Semantic Profiles into KG for Recommender Systems Using LLMs
- **Affiliation**: Academic
- **Link**: [arXiv:2601.08148](https://arxiv.org/abs/2601.08148)
- **Key Innovation**: Revisits profiling in RecSys across 4 dimensions (knowledge base, preference indicator, impact range, subject). Uses LLMs for entity profile generation + KG-based propagation.
- **Results**: Consistently outperforms SOTA KG- and LLM-based recommenders.

#### Climber-Pilot: Non-Myopic Generative Recommendation with Instruction Following
- **Affiliation**: NetEase Cloud Music
- **Link**: [arXiv:2602.13581](https://arxiv.org/abs/2602.13581)
- **Key Innovation**: TAMIP (Time-Aware Multi-Item Prediction) + CGSA (Condition-Guided Sparse Attention). Addresses myopia in generative retrieval by distilling long-horizon foresight.
- **Results**: 4.24% lift in core business metric at NetEase Cloud Music (one of China's largest music streaming platforms).
- **Comparison**: Outperforms SOTA baselines in both offline and online A/B tests.

#### SRPFN: One Sequential Recommendation Model Pretrained from Synthetic Priors Predicts Multiple Datasets
- **Authors**: Woosung Kang, Jiwon Jeong, Jonghyeok Shin, Jeongwhan Choi, Noseong Park
- **Affiliation**: KAIST
- **Link**: [arXiv:2606.15752](https://arxiv.org/abs/2606.15752)
- **Key Innovation**: Pretrains on synthetic data sampled from hierarchical degree-corrected stochastic block model (hDCSBM). Adapts to new datasets in a single forward pass — no gradient updates needed.
- **Results**: 7.53% average improvement over second-best method across 5 benchmarks. Inference on new dataset in ~1 minute (vs hours for trained baselines).

#### LLM-as-a-Judge for Reliable and Explainable Offline Evaluation in Top-K Recommendation
- **Affiliation**: Academic
- **Link**: [arXiv:2606.22961](https://arxiv.org/abs/2606.22961)
- **Key Innovation**: Semantic proxy for user preferences using LLM reasoning. Semantic matching principle + explicit rationale output for explainability.

#### CREATE: Cross-Representation Aligned Transfer Encoders for Improved Sequential Recommendations
- **Affiliation**: Academic
- **Key Innovation**: Combines transformer (sequential) and LightGCN (graph) representations with representation alignment. Outperforms pure sequential (SASRec, BERT4Rec), pure graph (LightGCN), and hybrid (GSRec) approaches.

#### Beyond Interleaving: Causal Attention Reformulations for Generative Recommender Systems
- **Affiliation**: Academic / Industry
- **Key Innovation**: Proposes AttnLFA (causally masked attention-based late fusion), AttnMVP (mixed-value early fusion), and AttnDNA (symmetric dual-stream). Moves beyond HSTU-style interleaving toward causality-aware attention formulations.

#### On the Memorization and Generalization of Generative Recommendation
- **Affiliation**: UCSD / Academic
- **Key Innovation**: Systematic analytical framework comparing semantic ID-based GR models with item ID-based models. Partitions test instances by item transition patterns. Introduces memorization-aware indicator to combine both model types.

#### Breaking the Likelihood Trap (Congrats — see above)

#### GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Affiliation**: JD.com
- **Key Innovation**: Page-wise NTP task, asymmetric linear Token Merger, GRPO-SR (RL with hybrid rewards)
- **Results**: 9.5% click count improvement, 8.7% transaction count improvement on JD.com homepage

### Key Themes at KDD 2026
- **Generative recommendation** dominates — HSTU-style models with semantic IDs
- **Graph-structured generation** for diversity and accuracy
- **Multi-agent LLM frameworks** for knowledge-grounded recommendation
- **Synthetic pretraining** for zero-shot transfer
- **LLM-as-Judge** for reliable evaluation
- **Causal attention** reformulations for rec sys
- **Industrial deployment** at Kuaishou, NetEase, JD.com scale

---

## 6. CVPR 2026

**Location**: Denver, Colorado | **Date**: June 3–7, 2026 | **Stats**: 16,092 submissions, 4,089 accepted (25.3% acceptance rate, +42% vs 2025)

### Best Paper

#### D4RT: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
- **Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **Affiliation**: Google DeepMind, UCL, University of Oxford
- **Key Innovation**: Unified transformer architecture that compresses entire video sequences into a global scene representation. Single lightweight decoder answers 3D position of any point at any time.
- **Results**: 300× speed improvement over previous methods. New SOTA across all 4D reconstruction and tracking benchmarks.
- **Significance**: Eliminates traditional multi-model pipeline (separate depth, optical flow, camera-pose models). Full-pixel tracking enables robots to distinguish camera motion, object motion, static geometry — critical for human-robot collaboration.
- **Link**: [CVPR 2026 Best Paper](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers)

### Best Paper Honorable Mention

#### NitroGen: A Vision-Action Foundation Model for Generalist Gaming Agents
- **Authors**: Jim Fan et al.
- **Affiliation**: NVIDIA, Stanford, Caltech
- **Key Innovation**: Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Zero-shot generalization across all games.
- **Results**: Up to 52% relative improvement in task success rate over from-scratch models. Direct transfer value to robot imitation learning.
- **Significance**: Roadmap from virtual to physical embodied intelligence.

### Best Paper Honorable Mention

#### SAM 3D: 3Dfy Anything in Images (3D Extension of Meta Segment Anything)
- **Affiliation**: Meta Superintelligence Labs
- **Key Innovation**: Predicts geometry, texture, and layout from a single image. Companion SAM 3D Body for human mesh recovery.
- **Results**: At least 5:1 win rate in human preference tests. Allows real-time 3D human pose estimation and spatial scene understanding from a single image without depth sensors.

### Additional Highlight Papers

#### Native and Compact Structured Latents (O-Voxel) for 3D Generation
- **Authors**: Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang
- **Affiliation**: Tsinghua University, Microsoft Research, USTC, Microsoft AI
- **Key Innovation**: O-Voxel representation for 3D generative modeling capturing complex shapes and surface attributes.
- **Results**: Significantly outperforms existing 3D generation models in geometry and quality.

#### PixelDiT: Pixel Diffusion Transformers for Image Generation
- **Authors**: Yongsheng Yu, Wei Xiong, Weili Nie, Yichen Sheng, Shiqiu Liu, Jiebo Luo
- **Affiliation**: Academic
- **Link**: [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Yu_PixelDiT_Pixel_Diffusion_Transformers_for_Image_Generation_CVPR_2026_paper.pdf)
- **Key Innovation**: Single-stage, end-to-end model learning diffusion directly in pixel space (no autoencoder). Dual-level design: patch-level DiT for global semantics + pixel-level DiT for texture details.
- **Results**: 1.61 FID on ImageNet 256, 1.81 FID on ImageNet 512. Text-to-image at 1024²: 0.74 GenEval, 83.5 DPG-bench — approaching best latent diffusion models.

#### tttLRM: Test-Time Training for Long-Context Autoregressive 3D Reconstruction
- **Affiliation**: Academic
- **Key Innovation**: Applies test-time training to long-context 3D reconstruction — sign that test-time compute is moving into vision.

#### CoTyle: Open-Source Code-to-Style Image Generation
- **Affiliation**: Academic
- **Key Innovation**: First open-source method for code-to-style image generation (previously explored mainly by Midjourney)

### Key Themes at CVPR 2026
- **Embodied AI dominance** — "seeing → understanding and acting"
- **4D scene reconstruction** — unified transformer approach (D4RT)
- **Game foundation models** (NitroGen)
- **3D foundation models** (SAM 3D, O-Voxel)
- **Pixel-space generation** (PixelDiT)
- **Test-time compute in vision** (tttLRM)
- **Vision-language trending** — 4.9% → 10.6% of highlighted papers YoY

---

## 7. ACL 2026 / EMNLP 2025

### ACL 2026

**Location**: San Diego, CA | **Date**: July 2026

#### Miner: Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models
- **Authors**: Shuyang Jiang, Yuhao Wang, Ya Zhang, Yanfeng Wang, Yu Wang
- **Affiliation**: Academic
- **Link**: [ACL 2026 Anthology](https://aclanthology.org/2026.acl-long.237/)
- **Key Innovation**: Addresses inefficiency in critic-free RL for reasoning models. Uses policy's intrinsic uncertainty as self-supervised reward signal. Token-level focal credit assignment + adaptive advantage calibration.
- **Results**: Up to 4.58 absolute gains in Pass@1 and 6.66 gains in Pass@K vs GRPO on Qwen3-4B/8B.
- **Significance**: First to demonstrate that latent uncertainty exploitation is both necessary and sufficient for efficient RL training of reasoning models.

#### PaCoRe: Parallel Coordinated Reasoning with Test-Time Compute Scaling
- **Authors**: Multiple
- **Affiliation**: Academic / Industry
- **Link**: [ACL 2026](https://aclanthology.org/2026.acl-long.1253.pdf)
- **Key Innovation**: Drives test-time compute through massive parallel exploration coordinated via message-passing. Each round launches parallel reasoning trajectories → compacts findings → synthesizes for next round.
- **Results**: 8B model reaches 94.5% on HMMT 2025, surpassing GPT-5's 93.2% by scaling effective TTC to ~2 million tokens. On Apex benchmark: 0.0% → 2.3% (from zero to nonzero).
- **Significance**: Demonstrates that parallel coordinated reasoning allows small models to bridge/surpass frontier systems.

#### KARL: Knowledge-Augmented Reinforcement Learning for LLM Agents
- **Authors**: Xueqiao Sun, Xiao Liu, Bowen Lv et al.
- **Affiliation**: Tsinghua University (THUDM)
- **Link**: [ACL 2026](https://aclanthology.org/2026.acl-long.2196/)
- **Key Innovation**: Enables LLM agents to dynamically explore structured knowledge sources through multi-turn interactions. Uses online RL with curiosity-driven reward shaping.
- **Results**: Qwen2.5-14B agent significantly outperforms GPT-4o, Claude-4, and o4-mini on knowledge graph and database tasks.

#### MetaJuLS: Adaptive Constraint Propagation via Meta-Reinforcement Learning
- **Affiliation**: Academic
- **Link**: [ACL 2026](https://aclanthology.org/2026.acl-long.701.pdf)
- **Key Innovation**: Treats constraint propagation scheduling as sequential decision problem with delayed global effects. Uses meta-RL to discover optimal schedules.
- **Results**: 1.5–2.0× speedups over GPU-optimized baselines within 0.2% of SOTA accuracy. Architecture-agnostic (works on Llama-3-8B, Qwen-2.5-7B + Llama-2-7B).
- **Combined system**: +XGrammar achieves 98.8% constraint satisfaction with lowest latency.

#### Self-Evolving Multi-Agent Systems via Textual Backpropagation
- **Affiliation**: Academic
- **Link**: [ACL 2026 Findings](https://aclanthology.org/2026.findings-acl.483.pdf)
- **Key Innovation**: Agentic Neural Network concept — agents as nodes, cooperative teams as layers. Forward phase: dynamic task decomposition. Backward phase: textual backpropagation for self-evolution.
- **Results**: Surpasses leading multi-agent baselines (AutoGen, AgentVerse, DyLAN) across 7 benchmarks.

#### Can We Predict Before Executing ML Agents? (FOREAGENT)
- **Link**: [ACL 2026](https://aclanthology.org/2026.acl-long.182.pdf)
- **Key Innovation**: "Implicit World Model" for ML agents that predicts execution outcomes before physical runs. FOREAGENT uses predict-then-verify loop, compressing hours of execution into seconds of inference.

#### MTR-Bench: Multi-Turn Reasoning Evaluation Benchmark
- **Affiliation**: Academic
- **Link**: [ACL 2026](https://aclanthology.org/2026.acl-long.984/)
- **Key Innovation**: 4 classes, 40 tasks, 3,600 instances across diverse reasoning capabilities. Fully automated dataset construction and evaluation.
- **Findings**: Even cutting-edge reasoning models fall short of multi-turn, interactive reasoning tasks.

#### LLMEval-Fair: Large-Scale Longitudinal Study on Robust and Fair Evaluation of LLMs
- **Affiliation**: Academic
- **Link**: [ACL 2026](https://aclanthology.org/2026.acl-long.972.pdf)
- **Key Innovation**: Longitudinal framework for tracking LLM evaluation robustness and fairness over time.

#### KnowledgeBerg: Systematic Knowledge Coverage and Compositional Reasoning Evaluation
- **Affiliation**: Academic
- **Link**: [ACL 2026 Findings](https://aclanthology.org/2026.findings-acl.548.pdf)
- **Key Innovation**: Evaluates LLMs on systematic knowledge coverage and compositional reasoning

### EMNLP 2025

**Location**: Suzhou, China | **Date**: November 4–9, 2025

#### Best Paper: A Theory of Response Sampling in LLMs
- **Affiliation**: Academic
- **Key Innovation**: Formal theory of how response sampling strategies affect LLM output quality and diversity

#### Tool-Induced Myopia (Also published at ACL 2026 — Megagon Labs)
- **Key Finding**: Tool use can improve LLM accuracy while simultaneously degrading AI reasoning quality — important caution for agentic systems

### Key Themes at ACL 2026 / EMNLP 2025
- **RL for reasoning models** — data efficiency, intrinsic rewards, parallel reasoning
- **Test-time compute scaling** — from sequential to parallel (PaCoRe)
- **Multi-agent systems** — self-evolution, textual backpropagation
- **Knowledge-augmented agents** — proactive knowledge exploration with RL
- **Constraint propagation** — meta-RL for structured inference
- **Benchmarking** — multi-turn reasoning, longitudinal fairness evaluation
- **Tool use caution** — trade-off between accuracy and reasoning quality

---

## 8. SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025

### SIGIR 2026

**Location**: Melbourne, Australia | **Date**: July 20–24, 2026

#### LTRR: Learning to Rank Retrievers for LLMs
- **Link**: [arXiv:2506.13743](https://arxiv.org/abs/2506.13743)
- **Key Innovation**: Query routing framework that learns to rank retrievers based on downstream utility to LLMs. Uses pairwise learning-to-rank (XGBoost) with AC utility metric.
- **Results**: Outperforms single-retriever RAG systems and generalizes to unseen query types.

#### L2Rec: Dual-View Understanding of LLMs for Personalized Recommendation
- **Link**: [arXiv:2605.26717](https://arxiv.org/abs/2605.26717)
- **Key Innovation**: Uses LLM token space as shared medium for behavioral and semantic understanding. End-to-end dual-view training without separate encoders.
- **Results**: Outperforms ID-based (SASRec, BERT4Rec), text-enhanced (S3-Rec, UniSRec, RecFormer), and LLM-based (LLaRA, LEARN) methods.

#### GenRec: Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Affiliation**: JD.com
- **Link**: [arXiv:2604.14878](https://arxiv.org/abs/2604.14878)
- **Key Innovation**: Page-wise NTP + Token Merger + GRPO-SR with hybrid rewards
- **Results**: +9.5% clicks, +8.7% transactions in JD.com production

### WWW 2026

#### ThinkRec: Thinking-based Recommendation via LLM
- **Link**: [WWW 2026](https://dl.acm.org/doi/10.1145/3774904.3792070)
- **Key Innovation**: Uses chain-of-thought reasoning before generating recommendations. Explores latent reasoning path for sequential recommendation.

### CIKM 2025

#### MTGR: Industrial-Scale Generative Recommendation Framework in Meituan
- **Affiliation**: Meituan
- **Key Innovation**: Large-scale generative retrieval deployed at Meituan's production scale

### RecSys 2025

**(Full papers listing available at [recsys.acm.org](https://recsys.acm.org/recsys25/accepted-contributions/))**

### Key Themes for IR / RecSys Conferences
- **Generative retrieval** dominates across all venues
- **LLM integration** for recommendation — from alignment to full reasoning
- **Learning to retrieve** for RAG systems
- **Industrial-scale deployment** at JD.com, Meituan, Kuaishou
- **Preference alignment** in generative rec (RLHF, GRPO)

---

## 9. General AI & LLM Papers

### Thinking/Reasoning Paradigm

#### DeepAgent: End-to-End Deep Reasoning Agent with Scalable Toolsets
- **Authors**: Xiaoxi Li, Wenxiang Jiao, Jiarui Jin et al.
- **Affiliation**: Renmin University (RUC-NLPIR)
- **Link**: [arXiv:2510.21618](https://arxiv.org/abs/2510.21618)
- **Key Innovation**: End-to-end reasoning agent with autonomous memory folding (episodic, working, tool memories). ToolPO: end-to-end RL strategy with tool-call advantage attribution.
- **Results**: Outperforms baselines on ToolBench, API-Bank, ALFWorld, WebShop, GAIA, HLE.

#### Eso-LMs (Esoteric Language Models): Any-Order Diffusion LLMs
- **Authors**: Subham Sekhar Sahoo, Zhihan Yang et al.
- **Affiliation**: Academic / NVIDIA
- **Link**: [OpenReview](https://openreview.net/pdf/2d43dd7ab44fd985e3b343418f4979a42770acc2.pdf)
- **Key Innovation**: Fuses AR and MDM paradigms with causal attention, enabling exact likelihood computation and KV caching for MDMs. New SOTA on speed-quality Pareto frontier for unconditional generation.

#### RePlaid: Continuous Diffusion Scales Competitively with Discrete Diffusion for Language
- **Authors**: Zhihan Yang, Wei Guo, Shuibai Zhang et al.
- **Affiliation**: Academic / NVIDIA
- **Link**: [arXiv:2605.18530](https://arxiv.org/abs/2605.18530)
- **Key Innovation**: First unified scaling comparison between continuous and discrete DLMs. RePlaid requires 20× compute (with self-conditioning) and 27× (without) to match AR perplexity.

#### Continuous Diffusion Models for Language
- Multiple works showing diffusion language models are approaching AR quality, with the trade-off of variable compute requirements.

### Foundation Models

#### CL-Bench: Context Learning Benchmark
- **Key Finding**: Even best model (GPT-5.1) solves only 23.7% of context learning tasks. Ten frontier models average 17.2% — highlighting a critical bottleneck for real-world deployment.
- **Models evaluated**: GPT-5.1, Gemini-3.1-PRO, Kimi-K2 Thinking, Qwen-3-Max Thinking, DeepSeek-V3.2-Thinking, Doubao-1.6-Thinking, HY-2.0-Thinking.

#### DRACO: Deep Research Benchmark
- **Link**: [arXiv:2602.11685](https://arxiv.org/abs/2602.11685)
- **Evaluation**: Perplexity Deep Research (strongest overall), OpenAI Deep Research (o3, o4-mini), Gemini Deep Research, Claude Opus (4.5/4.6).
- **10 domains**, 40 countries, rubric-graded on accuracy, completeness, objectivity, citation quality.

---

## 10. Recommendation Systems & CTR

### Industry Papers

#### GR4AD: Generative Recommendation for Large-Scale Advertising (Kuaishou)
- **Authors**: Ben Xue, Dan Liu et al.
- **Affiliation**: Kuaishou
- **Link**: [arXiv:2602.22732](https://arxiv.org/abs/2602.22732)
- **Key Innovation**: UA-SID (Unified Advertisement Semantic ID), LazyAR (lazy autoregressive decoder for short multi-candidate generation), VSL (Value-Aware Supervised Learning), RSPO (Ranking-Guided Softmax Preference Optimization). Dynamic beam serving.
- **Results**: Up to 4.2% ad revenue improvement. Deployed with 400M+ users, <100ms latency, 500+ QPS per L20.

#### OneMall: End-to-End Generative Recommender Family at Kuaishou E-Commerce
- **Authors**: Kun Zhang, Jingming Zhang et al.
- **Affiliation**: Kuaishou
- **Link**: [arXiv:2601.21770](https://arxiv.org/abs/2601.21770)
- **Key Innovation**: Unified framework across product-card, short-video, live-streaming. E-commerce Semantic Tokenizer + Query-Former + Cross-Attention + Sparse MoE + RL pipeline.
- **Results**: +13.01% GMV in product-card, +15.32% Orders in Short Video, +2.78% Orders in Live-Streaming. Serves 400M+ DAU.

#### HyFormer: Unified Sequence Modeling and Feature Interaction for CTR Prediction
- **Authors**: Yunwen Huang, Shiyong Hong et al.
- **Affiliation**: Industry
- **Link**: [arXiv:2601.12681](https://arxiv.org/abs/2601.12681)
- **Key Innovation**: Unifies long-sequence modeling and feature interaction in single backbone. Query Decoding (expands non-sequential features → Global Tokens) + Query Boosting (efficient token mixing). Alternating optimization across layers.
- **Results**: Outperforms LONGER + RankMixer baselines. Superior scaling with parameters/FLOPs. Production online A/B tests show significant gains.

#### OneRec: Generative Pre-trained One-Model Paradigm for Large-Scale Advertising Recommendation
- **Affiliation**: Kuaishou
- **Link**: [arXiv:2506.13695](https://arxiv.org/abs/2506.13695)
- **Results**: Pure generative model matches entire complex recommendation system performance. +0.54%/+1.24% App Stay Time, +0.05%/+0.08% LT7. Deployed to ~25% of total QPS.

#### UniFormer: Efficient and Unified Model-Centric Scaling for Industrial Recommendation
- **Affiliation**: Kuaishou
- **Link**: [arXiv:2606.27058](https://arxiv.org/abs/2606.27058)
- **Key Innovation**: Decomposes modeling space into feature and task spaces. Feature-space Interaction Modules + Task-space Interaction Modules. Semantic tokenization for user-item decoupling (request-level inference acceleration). Multi-view FFNs for flexible parameter scaling.
- **Results**: +0.101%/+0.260% App Stay Time, +0.729%/+1.113% Watch Time across Kuaishou and Kuaishou Lite.

#### DualGR: Generative Retrieval with Long and Short-Term Interests Modeling
- **Affiliation**: Kuaishou
- **Link**: [arXiv:2511.12518](https://arxiv.org/abs/2511.12518)
- **Key Innovation**: Dual-Branch Long/Short-Term Router (DBR), Search-based SID Decoding (S2D), Exposure-aware Next-Token Prediction Loss (ENTP-Loss).
- **Results**: +0.527% video views, +0.432% watch time in Kuaishou production.

#### AgentX: Agent-Driven Self-Iteration of Industrial Recommender Systems
- **Authors**: Changxin Lao, Fei Pan et al. (Kuaishou, 60+ co-authors)
- **Affiliation**: Kuaishou
- **Link**: [arXiv:2606.26859](https://arxiv.org/abs/2606.26859)
- **Key Innovation**: Four-stage closed-loop: Brainstorm Agent → Developing Agent → Evaluation Agent → Harness Evolution (SGPO). Autonomous paper reproduction, module ablation, cross-paper composition.
- **Results**: 3 workers → 374 ideas → 10 launchable rollouts in 3 weeks. 8× concurrency, 3.7× business value vs manual engineer. 0.561% user app-time gain, >RMB 100M annualized revenue.

#### AliBoost: Ecological Boosting Framework in Alibaba Platform
- **Affiliation**: Alibaba
- **Link**: [arXiv:2506.00954](https://arxiv.org/abs/2506.00954)
- **Key Innovation**: Stacking Fine-Tuning Cold Predictor + Item-oriented Bidding Boosting. Tiered boosting structure for ecosystem health.
- **Results**: Cold-started over 1 billion new items. Clicks and GMV of cold items increased by 60%+ within 180 days. Items with <10 daily PVs decreased from 41.1% to 24.5%.

#### DAIAN: Deep Adaptive Intent-Aware Network for CTR in Trigger-Induced Recommendation
- **Affiliation**: Alibaba (Xianyu)
- **Link**: [arXiv:2602.13971](https://arxiv.org/abs/2602.13971)
- **Key Innovation**: Addresses "intent myopia" in trigger-induced recommendation. Hybrid enhancer combining ID and semantic information.
- **Results**: +1.59% CTR, +1.73% recommendation diversity, +2.37% bills at Xianyu.

### Key Themes for RecSys/CTR
- **Generative recommendation** is the dominant paradigm — Kuaishou leads with multiple production systems (OneMall, OneRec, GR4AD, DualGR)
- **RL-based alignment** for generative rec — DPO, GRPO, RSPO variants
- **Agent-driven development** (AgentX) — first production deployment of autonomous rec sys iteration
- **Ecosystem health** — cold start, boosting frameworks (AliBoost)
- **Unified architectures** — sequence modeling + feature interaction (HyFormer, UniFormer)
- **Tokenization innovations** — semantic IDs, UA-SID, E-commerce Semantic Tokenizer

---

## 11. Agents, Code Execution & Games

### Agent Systems

#### AlphaEvolve: Coding Agent for Scientific and Algorithmic Discovery
- **Authors**: Alexander Novikov, Nhat Vu, Mario A. Eisenberger et al.
- **Affiliation**: Google DeepMind
- **Link**: [arXiv:2506.13131](https://arxiv.org/abs/2506.13131)
- **Key Innovation**: Evolutionary coding agent orchestrating autonomous LLM pipeline. Iterative code improvement with feedback from evaluators.
- **Results**: (1) More efficient scheduling algorithm for Google data centers, (2) Simplified circuit design for hardware accelerators, (3) Accelerated training of the LLM underpinning AlphaEvolve itself. **Discovered: first improvement to Strassen's algorithm in 56 years** — 4x4 complex matrix multiplication with 48 scalar multiplications.

#### AutoHarness: LLM Agent Code Harness Synthesis
- **Affiliation**: Google DeepMind
- **Link**: [arXiv:2603.03329](https://arxiv.org/abs/2603.03329)
- **Key Innovation**: LLM automatically synthesizes code harness to prevent illegal actions. Harness-as-action-filter, harness-as-action-verifier, harness-as-policy.
- **Results**: Prevents all illegal moves in 145 TextArena games. Smaller Gemini-2.5-Flash + harness outperforms larger Gemini-2.5-Pro and GPT-5.2-High. Code-policy achieves higher average reward than LLM-only approaches.

#### Confucius Code Agent (CCA): Scalable Agent for Real-World Codebases
- **Affiliation**: Industry
- **Link**: [arXiv:2512.10398](https://arxiv.org/abs/2512.10398)
- **Key Innovation**: Confucius SDK with Agent Experience (AX), User Experience (UX), Developer Experience (DX). Unified orchestrator + hierarchical working memory + persistent note-taking + modular extension. Meta-agent for automated config synthesis.
- **Results**: 54.3% Resolve@1 on SWE-Bench-Pro, exceeding prior research baselines and comparable to commercial results.

#### Lacuna: Safe Agents as Recursive Program Holes
- **Affiliation**: Academic / Industry
- **Link**: [arXiv:2605.28617](https://arxiv.org/abs/2605.28617)
- **Key Innovation**: Typed recursive agent primitive where generated code shapes the runtime itself. Type-safe mechanism for agentic behavior with safety guarantees.
- **Results**: DeepSeek-V4-Flash: 27.1% on BrowseComp-Plus with genuine multi-step research (5.9 rounds, 15.5 searches/query).

#### Code-Space Response Oracles (CSRO): Interpretable Multi-Agent Policies with LLMs
- **Authors**: Daniel Hennes, Zun Li et al.
- **Affiliation**: Google DeepMind
- **Link**: [arXiv:2603.10098](https://arxiv.org/abs/2603.10098)
- **Key Innovation**: Replaces neural network oracles in PSRO with LLMs generating policies as human-readable code. Supports zero-shot prompting, iterative refinement, and AlphaEvolve integration.

#### DeepAgent (see Section 9)

### Code Execution Prediction

#### Meta AI — LLM Learns Runtime Behavior
- **Affiliation**: Meta AI
- **Key Innovation**: Language model trained to predict runtime behavior and execution characteristics from source code. Moving beyond static code analysis to dynamic execution understanding.

#### FOREAGENT: World Model for ML Agent Execution Prediction
- **Link**: [ACL 2026](https://aclanthology.org/2026.acl-long.182.pdf)
- **Key Innovation**: "Implicit World Model" predicting ML agent execution outcomes. Replaces 9 hours of physical execution with 1 second of neural inference.

### Game AI

#### NitroGen (CVPR 2026 — see Section 6)
- 40,000 hours of gameplay across 1,000+ games. Zero-shot generalization. Up to 52% improvement.

#### Code World Models for General Game Playing
- **Authors**: Wolfgang Lehrach, Daniel Hennes et al.
- **Affiliation**: Google DeepMind
- **Link**: [arXiv:2510.04542](https://arxiv.org/abs/2510.04542)
- **Key Innovation**: LLM translates game rules to executable Python code (world model) for MCTS planning. Generates heuristic value functions and inference functions.
- **Results**: Outperforms or matches Gemini 2.5 Pro in 9 out of 10 games (5 perfect info, 5 imperfect info). Eliminates illegal moves entirely.

#### Orak: Game Agent Benchmark (ICLR 2026 — see Section 4)
- KRAFTON's 12-game benchmark with MCP interface and DeepSeek-R1 expert trajectories.

---

## 12. Generative Models & Sequential Modeling

### Image Generation

#### PixelDiT (CVPR 2026 — see Section 6)
- Pixel-space diffusion transformer without autoencoder. Dual-level design. 1.61 FID (ImageNet 256).

#### Native and Compact Structured Latents (O-Voxel) for 3D Generation
- **Affiliation**: Microsoft Research / Tsinghua
- **Key Innovation**: O-Voxel representation for high-quality 3D asset generation

#### D-AR: Diffusion via Autoregressive Models
- **Link**: [arXiv:2505.23660](https://arxiv.org/abs/2505.23660)
- **Key Innovation**: Recasts diffusion process as autoregressive next-token prediction. Sequential diffusion tokenizer. Supports consistent previews and zero-shot layout-controlled synthesis.
- **Results**: 2.09 FID using 775M Llama backbone with 256 discrete tokens.

### Sequential Modeling

#### NextFlow: Unified Sequential Modeling for Multimodal Understanding and Generation
- **Authors**: Huichao Zhang et al.
- **Link**: [arXiv:2601.02204](https://arxiv.org/abs/2601.02204)
- **Key Innovation**: Unified decoder-only autoregressive transformer on 6T interleaved text-image tokens. Next-token prediction for text + next-scale prediction for visual generation.
- **Results**: 1024×1024 images in 5 seconds (orders of magnitude faster than comparable AR models). SOTA among unified models, rivals specialized diffusion baselines.

#### SSM Meets Video Diffusion Models: Efficient Long-Term Video Generation
- **Link**: [Springer](https://link.springer.com/article/10.1007/s00354-026-00326-8)
- **Key Innovation**: Combines structured state space models (SSMs) with diffusion for efficient long-term video generation.

---

## 13. Benchmarks & Evaluation

| Benchmark | Affiliation | Focus | Key Result |
|-----------|-----------|-------|-----------|
| **CL-Bench** | Academic | Context Learning | Best model (GPT-5.1) at 23.7%; avg 17.2% |
| **DRACO** | Perplexity AI | Deep Research | Perplexity Deep Research strongest overall |
| **MathNet** | MIT / Academic | Olympiad Math (30K problems, 17 langs) | Gemini-3.1-Pro 78.4%, GPT-5 69.3% |
| **MTR-Bench** | ACL 2026 | Multi-Turn Reasoning | Even SOTA reasoning models fall short |
| **Orak** | KRAFTON / ICLR 2026 | Game Agents (12 games, 6 genres) | MCP-based, DeepSeek-R1 distilled trajectories |
| **INFINITY-CHAT** | NeurIPS 2025 | LLM Output Diversity | 31K+ human annotations, homogenization study |
| **General365** | Academic | General Reasoning | Diverse challenging task evaluation |
| **LitBench** | EACL 2026 | Creative Writing | Trained reward models (78%) beat best OTS judge (73%) |
| **LLMEval-Fair** | ACL 2026 | Longitudinal Fair Evaluation | Framework for tracking eval robustness |
| **KnowledgeBerg** | ACL 2026 | Knowledge Coverage + Compositional Reasoning | Systematic evaluation methodology |

---

## 14. Key Trends & Cross-Cutting Themes

### 🏆 Conference-Level Statistics
| Venue | Year | Submissions | Accepted | Rate |
|------|------|-----------|---------|------|
| AAAI | 2026 | ~29,000 | ~4,167 | ~14.4% |
| CVPR | 2026 | 16,092 | 4,089 | 25.3% |
| ICLR | 2026 | 19,814 | 5,355 | 27.4% |
| NeurIPS | 2025 | - | - | - |
| ICML | 2026 | ~8,000 (est.) | ~1,000 (est.) | ~27% (est.) |

### 🔬 Research Paradigm Shifts

1. **From Bigger Models to Understanding Limits** (NeurIPS 2025)
   - LLM homogenization as a systemic risk
   - Attention sink elimination through architectural changes
   - Questioning whether RL actually adds reasoning capacity

2. **Generative Recommendation Becomes Mainstream**
   - Kuaishou leads with 5+ production generative recommendation systems
   - Meta HSTU paradigm widely adopted and extended
   - RL alignment (DPO, GRPO, RSPO) for rec sys

3. **Agent-Driven Development**
   - AgentX (Kuaishou): first production self-evolving recommendation system
   - AlphaEvolve (Google DeepMind): 56-year-old algorithm improved
   - Self-evolving multi-agent systems via textual backpropagation

4. **Embodied AI Takes Center Stage**
   - CVPR 2026: "seeing → understanding and acting"
   - Game foundation models (NitroGen) → robot imitation learning
   - 4D world understanding (D4RT)

5. **Test-Time Compute Scaling**
   - Parallel Coordinated Reasoning (PaCoRe): 8B model beats GPT-5
   - Test-time training in vision (tttLRM)
   - Diffusion models with learned unmasking policies

6. **Diffusion Models for Language**
   - Approaching AR quality (continuous vs discrete)
   - Eso-LMs: AR + MDM fusion with exact likelihood
   - Learned unmasking policies via RL

7. **Chinese Industry Dominance in RecSys/CTR**
   - Kuaishou: GR4AD, OneMall, OneRec, DualGR, AgentX, UniFormer
   - Alibaba: AliBoost, DAIAN, GenRec (JD.com)
   - NetEase: Climber-Pilot
   - Systematic: agent-driven automation, ecosystem health, unified architectures

8. **Benchmarking Gaps Exposed**
   - Context learning: even frontier models at 17-24%
   - Multi-turn reasoning: SOTA models fall short
   - Creative writing: trained reward models beat GPT judges
   - Deep research: significant quality variation across providers

### 📍 Notable Labs to Watch

- **Google DeepMind**: D4RT, AlphaEvolve, AutoHarness, Code World Models, CSRO
- **Alibaba/Qwen**: Gated Attention, Learning Unmasking Policies, AliBoost, DAIAN
- **Kuaishou**: GR4AD, OneMall, OneRec, DualGR, AgentX, UniFormer
- **NVIDIA**: NitroGen, Eso-LMs, RePlaid
- **Meta**: SAM 3D, Runtime Behavior LLM
- **Microsoft Research**: O-Voxel 3D Generation
- **Tsinghua/THUDM**: KARL (ACL 2026)
- **KRAFTON**: Orak (ICLR 2026)
- **NetEase**: Climber-Pilot (KDD 2026)
- **JD.com**: GenRec (SIGIR 2026)
