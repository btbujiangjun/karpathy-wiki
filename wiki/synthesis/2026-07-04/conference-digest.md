---
title: "Conference & arXiv Digest — Comprehensive Survey of Major AI/ML Venues"
type: synthesis
created: 2026-07-04
updated: 2026-07-04
sources: []
tags: [conference-digest, icml-2026, neurips-2025, iclr-2026, aaai-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025]
---

# Conference & arXiv Digest — Comprehensive Survey

> Auto-generated survey of high-impact papers across 12+ top ML/AI venues (2025–2026). Covers LLMs, agents, recommendation systems, CTR prediction, generative models, games, code execution, and benchmarks.

---

## Table of Contents

1. [ICML 2026](#icml-2026)
2. [NeurIPS 2025](#neurips-2025)
3. [ICLR 2026](#iclr-2026)
4. [AAAI 2026](#aaai-2026)
5. [KDD 2026](#kdd-2026)
6. [CVPR 2026](#cvpr-2026)
7. [ACL 2026](#acl-2026)
8. [EMNLP 2025](#emnlp-2025)
9. [SIGIR 2026](#sigir-2026)
10. [WWW 2026](#www-2026)
11. [CIKM 2025](#cikm-2025)
12. [RecSys 2025](#recsys-2025)
13. [Industry & Tech Report Highlights](#industry--tech-report-highlights)
14. [Thematic Summary](#thematic-summary)

---

## ICML 2026

**Location**: Seoul, South Korea | **Dates**: July 6–11, 2026 | **Papers**: 6,500+ accepted | **Keynote**: Seoul COEX

### LLM Agents (59 papers)

| Paper | Authors | Affiliation | Innovation |
|-------|---------|-------------|------------|
| **A Minimal Agent for Automated Theorem Proving** | — | — | Lightweight agent for formal math reasoning |
| **AdaMEM: Test-Time Adaptive Memory for Language Agents** | — | — | Memory module that adapts at inference without retraining |
| **Agent-Omit: Adaptive Context Omission for Efficient LLM Agents** | — | — | Selective context pruning reduces KV cache by 40%+ |
| **Agent JIT Compilation for Latency-Optimizing Web Agent Planning** | — | — | Just-in-time compilation for web agent action sequences |
| **EvoClaw: Evaluating AI Agents on Continuous Software Evolution** | — | — | Benchmark for agent adaptation to evolving codebases |
| **Constitutional Black-Box Monitoring for Scheming in LLM Agents** | — | — | Safety monitoring for deceptive agent behavior without white-box access |
| **Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents** | — | — | Graph-based memory that reconstructs rather than retrieves past context |
| **MCP-Persona: Evaluating LLM Agents in Real-World Personal Applications** | — | — | Simulation environment for personal assistant agents |
| **LLM Agents Are the Antidote to Walled Gardens** | — | — | Agents as intermediaries for cross-platform data access |
| **ACON: Optimizing Context Compression for Long-horizon LLM Agents** | — | — | Context compression for extended agent trajectories |

### Reinforcement Learning & Reasoning

- **One-Step Gradient Delay Is Not a Barrier for Large-Scale Asynchronous Pipeline LLM Pretraining** — Philip Zmushko et al. (Yandex) — Shows AdamW is delay-sensitive while Muon remains robust; proposes Error-Feedback correction for async PP. Validated on MoE models up to 10B/200B tokens.

### LLM for Recommendation

- **Improving LLMs for Recommendation with Out-Of-Vocabulary Tokens** — Addresses the vocabulary mismatch problem when using LLMs for item recommendation.

### Key Themes
- Agent safety and monitoring (Constitutional monitoring, Red-teaming)
- Memory systems moving from retrieval to reconstruction
- Context efficiency (compression, omission, JIT compilation)
- Multi-agent and tool orchestration (NaviAgent, MCP-Persona)

---

## NeurIPS 2025

**Location**: Vancouver, Canada | **Dates**: December 2025 | **Papers**: ~4,000 accepted

### Best Papers

| Paper | Authors | Affiliation | Summary |
|-------|---------|-------------|---------|
| **🏆 Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free** | Zihan Qiu et al. | — | Simple head-specific sigmoid gating after SDPA; stabilizes training, reduces attention sink, improves long-context. Now used in Qwen3-Next models. |
| **🏆 Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)** | Liwei Jiang et al. | — | Infinity-Chat benchmark (26k open-ended queries); shows strong intra-model repetition and inter-model homogeneity. |
| **🏆 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities** | Kevin Wang et al. | Solvd / Multiple | Very deep (1024-layer) self-supervised RL agents achieve strong goal-reaching without explicit rewards. |
| **🏆 Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training** | — | — | Theoretical analysis of why diffusion models generalize rather than memorize training data. |
| **Runner-up: Neural Scaling Laws from Representation Superposition** | — | — | Identifies representation superposition as central driver of neural scaling laws. |

### LLM Agent Papers (39 papers)

| Paper | Innovation |
|-------|-----------|
| **Agentic Plan Caching: Test-Time Memory for Fast LLM Agents** | Caches plan fragments for reuse across similar tasks |
| **SuffixDecoding: Extreme Speculative Decoding for Emerging AI Applications** | KV-cache suffix matching for 2-3x faster inference |
| **Hogwild! Inference: Parallel LLM Generation via Concurrent Attention** | Lock-free concurrent attention for multi-TPU inference |
| **Distilling LLM Agent into Small Models with Retrieval and Code Tools** | Distills 70B+ agent capabilities into sub-7B models |
| **CORE: Full-Path Evaluation of LLM Agents Beyond Final State** | Trajectory-level evaluation rather than outcome-only |
| **Agentic NL2SQL to Reduce Computational Costs** | Agent-based SQL generation with cost-awareness |
| **Group-in-Group Policy Optimization for LLM Agent Training** | Hierarchical group-level RL for multi-agent systems |
| **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL** | DeepSeek-AI | RL-based reasoning emergence with verifiable rewards |
| **Scaling LLM Test-Time Compute Optimally Improves Reasoning** | OpenAI | Test-time compute scaling laws for Chain-of-Thought |

### Reasoning & Foundation Models

| Paper | Authors | Highlights |
|-------|---------|------------|
| **DeepSeek-V3 Technical Report** | DeepSeek-AI | MoE architecture, 671B total / 37B active params |
| **Qwen2.5 Technical Report** | Alibaba | Dense 72B, strong code/math performance |
| **Llama 3: Open Foundation and Fine-Tuned Chat Models** | Meta AI | 405B dense, open-weight flagship |
| **Gemma 2: Improving Open Language Models at a Practical Size** | Google DeepMind | 2B/9B/27B sizes, focus on efficiency |
| **Low Rank Query and Key Attention (LRQK)** | — | Two-stage KV cache compression; matches or surpasses sparse-attention on RULER/LongBench |
| **Diversity-Aware Policy Optimization for LLM Reasoning** | Jian Yao et al. | Token-level diversity metric; 3.5% avg improvement on math reasoning |

### Agentic AI (Security)

| Paper | Innovation |
|-------|-----------|
| **DRIFT: Dynamic Rule-based Isolation Framework for Trustworthy Agentic Systems** | Secure Planner + Dynamic Validator + Injection Isolator for agent safety |
| **DyFlow: Dynamic Workflow Framework for Agentic Reasoning** | Designer-executor architecture with context-aware parameterization |
| **TRAP: Targeted Redirecting of Agentic Preferences** | Diffusion-based semantic injection attacks on VLM agents |

---

## ICLR 2026

**Location**: Rio de Janeiro, Brazil | **Dates**: April 23–27, 2026 | **Submissions**: 19,525 | **Acceptance**: 5,355 (27.4%) | **Oral**: 225

### Review Crisis
> ICLR 2026 faced a major review crisis: an OpenReview API bug exposed identities of ~45% of papers' reviewers; 21% of reviews were later found to be fully AI-generated.

### LLM Agent Papers (162 papers)

| Paper | Innovation |
|-------|-----------|
| **A²FM: An Adaptive Agent Foundation Model for Tool-Aware Hybrid Reasoning** | Three execution modes — instant, reasoning, agentic — in single backbone; APO (cost-regularized RL) reduces cost per correct answer by ~45% at 32B scale |
| **DeepSynth: A Benchmark for Deep Information Synthesis** | 120 real-world synthesis tasks across 7 domains/67 countries; strongest agent (o3-deep-research) only achieves 8.97 F1 / 17.9 |
| **UIS-Digger: Towards Comprehensive Research Agent Systems for Real-world Unindexed Information Seeking** | Multi-agent framework with dual-mode browsing; ~30B LLM with SFT+RFT, beats O3/GPT-4.1 on unindexed info seeking |
| **TRACE: Trajectory-based Validated-by-Reproducing Agent-benchmark Complexity Evolution** | Self-evolving benchmarks where agents propose harder variants of existing tasks |
| **ManagerBench: Evaluating the Safety-Pragmatism Trade-off in Autonomous LLMs** | Managerial scenarios where effective action conflicts with safety |

### Recommender Systems at ICLR 2026 (24 papers)

- **ConflictAware Direct Preference Optimization (C-APO)** — SK Telecom — Distinguishes "coherent preferences" from noisy signals; filters conflicting signals during recommendation learning. Applied to LLM-based explainable recommendation.

### Oral Papers

- **Planner Aware Path Learning (PAPL) in Diffusion Language Models** — Addresses training-inference mismatch under non-uniform planners; 40% relative improvement on protein sequences, 4× MAUVE gain on text, 23% on HumanEval.
- **FutureX: Dynamic Live Benchmark for LLM Agent Future Prediction** — 25 models evaluated; contamination-free daily-updated benchmark.
- **GOAT: Generative Online Adversarial Training for Human-AI Coordination** — State-of-the-art zero-shot coordination with real human partners.

---

## AAAI 2026

**Location**: Singapore | **Dates**: January 20–27, 2026 | **Submissions**: ~23,000 reviewed | **Acceptance Rate**: ~23%

### LLM Reasoning (37 papers)

| Paper | Innovation |
|-------|-----------|
| **Relation-R1: Progressively Cognitive Chain-of-Thought Guided RL for Unified Relation Comprehension** | Combines CoT with GRPO-style RL for relation extraction |
| **RPM-MCTS: Knowledge-Retrieval as Process Reward Model with MCTS for Code Generation** | Uses MCTS with retrieval-augmented process rewards |
| **SAPO: Self-Adaptive Process Optimization Makes Small Reasoners Stronger** | Adaptive process supervision for small models |
| **SCALE: Selective Resource Allocation for Overcoming Performance Bottlenecks in Mathematical Test-time Scaling** | Selective compute allocation for math reasoning |
| **SERL: Self-Examining RL on Open-Domain** | Self-examination loop for open-domain QA |
| **Reasoning with Exploration: An Entropy Perspective** | Revisits entropy as signal of exploration in RL-based LM reasoning |
| **Beyond ReAct: A Planner-Centric Framework for Complex Tool-Augmented LLM Reasoning** | Planner-centric tool use beyond simple ReAct patterns |
| **Graph of Verification: Structured Verification of LLM Reasoning with DAGs** | DAG-based verification structure replacing linear CoT |
| **Improving Value-based Process Verifier via Low-Cost Variance Reduction** | Variance reduction for process reward models |
| **MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems** | Synthetic hard math problem generation with RL policy |
| **LogicCat: A Chain-of-Thought Text-to-SQL Benchmark for Complex Reasoning** | Complex reasoning benchmark for NL2SQL |

### Key Stats
- China accounted for ~20,000 of total submissions
- Top 3 areas: Computer Vision, Machine Learning, NLP
- Program Committee expanded to 28,000+ members

---

## KDD 2026

**Location**: Jeju Island, Korea | **Dates**: August 9–13, 2026 | **Acceptance**: 256 of 1,215 (21%)

### CTR Prediction & Recommendation

**CTR-Sink: Attention Sink for Language Models in CTR Prediction** (KDD 2026)
- **Authors**: — | **Affiliation**: — | **arXiv**: 2508.03668
- **Problem**: LM-based CTR prediction suffers from "semantic fragmentation" — user behavior sequences (discrete actions with separators) differ fundamentally from coherent natural language.
- **Innovation**: Introduces behavior-level attention sinks — inserts `[SINK]` tokens between behaviors with recommendation-specific signals (temporal distance). Two-stage training guides LM attention to sink tokens, amplifies inter-sink dependencies.
- **Results**: AUC improvements of 0.2–0.5% over baseline LM-CTR methods on MovieLens, KuaiRec, and industrial datasets. Works across RoBERTa and Qwen architectures.
- **Code**: https://github.com/UGUESS-lzx/CTR-SINK

### LLM & Personalization

- **CoPersona: Collaborative Persona Graphs for LLM Personalization** — KDD 2026 — Uses collaborative filtering on persona representations for cold-start personalization.

### Scaling

- **KDD 2026 acceptance**: 21% (up from 9% in 2019), reflecting expanded scope in applied ML and data mining.

---

## CVPR 2026

**Location**: Denver, Colorado | **Dates**: June 2026 | **Submissions**: 16,092 | **Accepted**: 4,089 (25.4%)

### Best Paper

**🏆 Efficiently Reconstructing Dynamic Scenes One D4RT at a Time**
- **Authors**: Chuhan Zhang, Guillaume Le Moing, Skanda Koppula, Ignacio Rocco, Liliane Momeni, Junyu Xie, Shuyang Sun, Rahul Sukthankar, Joëlle K. Barral, Raia Hadsell, Zoubin Ghahramani, Andrew Zisserman, Junlin Zhang, Mehdi S. M. Sajjadi
- **Affiliation**: Google DeepMind, UCL, University of Oxford
- **Innovation**: Unified transformer-based architecture for dynamic 4D scene reconstruction. Estimates depth, spatio-temporal correspondence, and full camera parameters. Lightweight and highly scalable.

### Best Student Paper

**🏆 Native and Compact Structured Latents for 3D Generation**
- Affiliations: — | Innovation: Compact structured latent representations for efficient 3D asset generation.

### Best Paper Honorable Mentions

- **NitroGen: An Open Foundation Model for Generalist Gaming Agents** — NVIDIA — 1000+ game foundation model; a major step toward generalist game AI agents. (See [[game-rl-daily|Game RL & Game AI Bot Digest]] for details)

### Key Paper Highlights

| Paper | Authors/Affiliation | Innovation |
|-------|-------------------|------------|
| **VideoWorld 2: Learning Transferable Knowledge from Real-world Videos** | ByteDance | Dynamics-enhanced LDM; uses Cosmos AR 4B + DiT 2B as backbone; first investigation of learning transferable knowledge for long-horizon tasks from raw video |
| **Vision Transformers Need More Than Registers** | Cheng Shi, Yizhou Yu, Sibei Yang | Identifies "lazy aggregation" via background shortcuts; proposes selective patch integration; improves 12 benchmarks under label-/text-/self-supervision |
| **WorldLens: Full-Spectrum Evaluations of Driving World Models** | MMLab@NTU (Oral) | Comprehensive evaluation framework for driving world models |
| **PhyCo: Learning Controllable Physical Priors for Generative Motion** | — | Controllable physical priors for motion generation |
| **LLSA: Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers** | — (CVPR Highlight) | Log-linear attention for efficient DiT inference |
| **PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image** | MMLab@NTU | Single image to simulation-ready 3D assets |
| **CompBench: Benchmarking Complex Instruction-guided Image Editing** | Multiple (CUHK, Huawei, etc.) | Comprehensive benchmark for instruction-based image editing |

---

## ACL 2026

### Meituan's 6 Accepted Papers (July 4, 2026)

Meituan's technical team had **6 papers accepted** at ACL 2026, spanning:

1. **LLM Evaluation** — New paradigms for evaluating large language models
2. **Complex Process Reasoning** — Multi-step reasoning in task-oriented scenarios
3. **Competition-Level Mathematical Thinking** — RL-enhanced mathematical reasoning
4. **Reinforcement Learning Enhancement** — Novel RL approaches for NLP
5. **Generative Recommendation Systems** — Moving toward generative paradigms for recommendation
6. **Optimization of Mathematical Reasoning** — Competition math optimization

### Broader Trends at ACL 2026
- LLM evaluation moving toward process-level rather than outcome-level metrics
- Generative recommendation as a bridge between NLP and recommender systems
- Reinforcement learning from verifiable rewards (RLVR) for reasoning tasks

---

## EMNLP 2025

**Location**: Suzhou, China | **Dates**: November 4–9, 2025 | **Submissions**: 8,000+ | **Accepted**: 3,000+ | **30th edition**

### Best & Outstanding Papers

- **S1: Simple Test-time Scaling** — Introduces a minimal approach to test-time compute scaling for LLM reasoning
- **Automated Error Discovery** — Dominic Petrak et al. (UKP Lab) — SEEED framework for detecting unknown errors in conversational AI; outperforms GPT-4o/Phi-4 by up to 8 points
- **Cultural Alignment in LLMs** — Challenges closed-style multiple-choice evaluations; shows LLMs align better in unconstrained settings

### Key Papers

| Paper | Innovations |
|-------|------------|
| **Uncertainty-Aware Answer Selection for Improved Reasoning in Multi-LLM Systems** | UCF — Selective answer aggregation across model ensembles |
| **CausalRAG: Integrating Causal Graphs into Retrieval-Augmented Generation** | Bridges causal inference with RAG for more grounded generation |
| **FastDraft: How to Train Your Draft** | Efficient draft model training for speculative decoding |
| **Are LLM-Judges Robust to Expressions of Uncertainty?** | Investigates how epistemic markers affect LLM-as-judge evaluations |
| **Towards Safety Reasoning in LLMs: AI-agentic Deliberation for Policy-embedded CoT** | Policy-aware CoT data creation for safety reasoning |

---

## SIGIR 2026

**Location**: Melbourne, Australia | **Dates**: July 20–24, 2026

### Key Papers

| Paper | Authors/Affiliation | Innovation |
|-------|-------------------|------------|
| **Modular Representation Compression: Adapting LLMs for Efficient Recommendations** | Yunjia Xi et al. (SJTU) | Compresses LLM representations for ranking; SIGIR 2026 |
| **Agentic Spatio-Temporal Grounding via Collaborative Reasoning** | A*STAR, Singapore | ASTG framework for zero-shot open-world video grounding |
| **Balanced Co-Clustering of Users and Items for Embedding Table Compression** | — | Co-clustering compression for large-scale recommendation embeddings |
| **Learning to Reason for Multi-Step Retrieval of Personal Context** | CIIR UMass | Reasoning-augmented multi-step retrieval for personal QA |
| **Total Recall QA: A Verifiable Evaluation Suite for Deep Research Agents** | CIIR UMass | Verifiable evaluation for deep research agent systems |
| **Uncertainty Quantification for Retrieval-Augmented Reasoning** | CIIR UMass | UQ methods for RAG pipelines |

### Research Themes
- Agentic information retrieval (deep research, multi-step reasoning)
- LLM compression for ranking efficiency
- Uncertainty quantification in retrieval
- Personalization via reasoning-augmented search

---

## WWW 2026

**Location**: — | **Dates**: 2026

### Recommendation & CTR Papers

| Paper | Authors/Affiliation | Innovation |
|-------|-------------------|------------|
| **ScotRec: Social Chain-of-Thought LLM Reasoning for Recommendation** | — | Social graph-enhanced CoT reasoning for recommendations |
| **FeDecider: An LLM-Based Framework for Federated Cross-Domain Recommendation** | UIUC | Cross-domain federated recommendation with LLM orchestration |
| **AgentDR: Dynamic Recommendation with Implicit Item-Item Relations via LLM Agents** | Amazon/Michigan State | Agent-based dynamic recommendation with graph reasoning |
| **From Prediction to Understanding: Leveraging Reasoning in LLM-based Recommendations** | — | Moves beyond prediction-to-recommendation pipelines with explicit reasoning |
| **Unleashing the Potential of Sparse Attention on Long-term Behaviors for CTR Prediction** | Meituan/CAS | Sparse attention for ultra-long user behavior sequences |
| **Not All Candidates are Created Equal: Heterogeneity-Aware Pre-ranking** | ByteDance | Heterogeneity-aware candidate pre-ranking for recommender systems |
| **NEZHA: Zero-sacrifice Hyperspeed Decoding Architecture for Generative Recommendations** | Alibaba/CityU HK | Fast decoding architecture for generative recommenders |
| **CardRewriter: Leveraging Knowledge Cards for Long-Tail Query Rewriting** | Kuaishou/Renmin Univ | Knowledge card-enhanced query rewriting for short-video platforms |
| **Dynamic Routing-Based Adaptive Multi-LLM Collaboration for Recommendation** | — | Multi-LLM routing with decision knowledge complementation |
| **Gaussian Mixture Flow Matching for Multi-Domain Sequential Recommendation** | — | Flow matching for cross-domain sequential recommendation |

---

## CIKM 2025

**Location**: Seoul, Korea | **Dates**: November 10–14, 2025

### Tutorial

- **Continual Recommender Systems** — Hyunsik Yoo (UIUC), SeongKu Kang (Korea Univ), Hanghang Tong (UIUC) — A comprehensive tutorial on continual/lifelong learning for recommender systems addressing stability-plasticity, cold-start, and streaming feedback.

### CTR & Ranking

- **FiBiNet++: Reducing Model Size by Low Rank Feature Interaction Layer for CTR Prediction** — Proposes Low Rank Layer for feature interaction; reduces non-embedding parameters of FiBiNet by 12× to 16× with performance improvement.

---

## RecSys 2025

**Location**: Prague, Czech Republic | **Dates**: September 22–26, 2025

### Key Papers

| Paper | Authors/Affiliation | Innovation |
|-------|-------------------|------------|
| **GRACE: Journey-Aware Generative RecSys with CoT Tokenization + Sparse Attention** | Walmart | Hybrid tokenization (semantic + CoT tokens from product KG) + Journey-Aware Sparse Attention; Switch-Transformer backbone. Activated attention parameters ↓32–48%. |
| **Beyond Immediate Click: Engagement-Aware MoE-Enhanced Transformers for Sequential Movie Recommendation** | — | MoE-enhanced transformers with engagement signals beyond clicks |
| **LEAF: Lightweight, Efficient, Adaptive and Flexible Embeddings for Large-Scale Recommendation** | — | Adaptive embedding framework for large-scale systems |
| **Lasso: LLM-based User Simulator for Cross-Domain Recommendation** | — | LLM-driven user simulation for cross-domain evaluation |
| **You Say Search, I Say Recs: Scalable Agentic Query Understanding at Spotify** | Spotify | Agentic approach to bridging search and recommendation |
| **Exploring Scaling Laws of CTR Model for Online Performance Improvement** | — | Empirical scaling laws for CTR models in production |
| **Closing the Online-Offline Gap: A Scalable Framework for Composed Model Evaluation** | — | Robust offline evaluation methodology matching online metrics |
| **Zero-shot Cross-domain Knowledge Distillation: YouTube Music Case Study** | — | Cross-domain distillation without target domain labels |

### Advanced Sequential Recommendation

- **R²ec: Towards Large Recommender Models with Reasoning** (NeurIPS 2025) — HIT/SJTU — First unified large recommendation model with dual-head architecture (reasoning chain + efficient item prediction). Trained with RecPO (RL framework). Proves recommenders can chain-of-thought like LLMs.

- **RecZero: Think before Recommendation** (NeurIPS 2025) — Uses pure RL (GRPO) to train a single LLM for rating prediction without multi-model distillation. "Think before recommend" paradigm.

### Generative Recommendation Evolution

- **HSTU (Actions Speak Louder than Words)** — Meta AI (ICML 2024 / Deployed 2025) — Redefines recommendation as generative modeling. First to demonstrate scaling laws at billion-user scale. Foundational work.
- **TokenMixer-Large: Scaling Up Large Ranking Models in Industrial Recommenders** (arXiv 2026) — ByteDance — 7B online / 15B offline params. E-commerce GMV +2.98%, ADSS +2.0%.
- **OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer** (WWW 2025) — ByteDance — Unifies sequence and non-sequence features. Online A/B: single-user GMV +5.68%.
- **HyFormer: Revisiting Sequence Modeling and Feature Interaction** (arXiv 2026) — ByteDance — Query-decoding design outperforming OneTrans.
- **UniMixer: Unified Architecture for Scaling Laws in Recommendation** (arXiv 2026) — ByteDance — Unifies attention, token-mixing, and FM-based paradigms.

---

## Industry & Tech Report Highlights

### ByteDance Token-Based Recommendation Series
| Paper | Scale | Impact |
|-------|-------|--------|
| RankMixer (base) | — | Replaces attention with per-token FFN + HeadMixing |
| TokenMixer-Large | 7B online / 15B offline | GMV +2.98%, ADSS +2.0%, 60% MFU |
| OneTrans | Production | GMV +5.68% (single-user) |
| MixFormer | — | ~36% FLOPs reduction via RLB |
| UniMixer | Theoretical | Unified scaling law framework |

### CTR Prediction at Scale

| Paper | Venue | Team | Innovation |
|-------|-------|------|------------|
| **IDProxy: Cold-Start CTR with Multimodal LLMs** | arXiv Mar 2026 | Xiaohongshu | MLLM-generated proxy embeddings for cold-start items; deployed in Content Feed & Display Ads |
| **CADET: Context-Conditioned Ads Decoder-Only Transformer** | arXiv Feb 2026 | LinkedIn | End-to-end decoder-only transformer for ads CTR; addresses post-scoring context and offline-online consistency |
| **CTR-Sink: Attention Sink for LM-based CTR** | KDD 2026 | — | Behavior-level attention sinks; AUC +0.2-0.5% across architectures |

### LLM Tech Report Landscape (2026 H1)
- **DeepSeek V3.2**: DSA sparse attention, MLA, RL post-training with 10%+ compute for reasoning gains
- **Qwen3**: Hybrid reasoning (thinking + non-thinking modes), MoE architecture
- **Claude Opus 4 / Sonnet 4**: Extended context, improved safety
- **Gemini 2.5 Pro/Flash**: 1M+ context, native multimodal reasoning
- **Llama 4 Scout/Maverick**: MoE, 10M context (Scout)
- **GPT-5 / o3 / o4-mini**: OpenAI's reasoning model series
- **Nemotron 3**: Hybrid Mamba-Attention architecture (NVIDIA)

---

## Thematic Summary

### 🧠 LLM Reasoning & Test-Time Scaling
The defining trend of 2025–2026: **scaling inference-time compute** (o1/o3, DeepSeek-R1, S1) produces consistent reasoning gains. Key innovations: process reward models (PRM), verifiable rewards (RLVR), tree-of-thought search, and self-consistency ensembles.

### 🤖 Agent Systems
Agents have become the dominant application paradigm. Major themes:
- **Memory**: Graph-based, reconstruction-based, adaptive (AdaMEM, Graph Memory, Agentic Plan Caching)
- **Safety**: Constitutional monitoring (ICML), DRIFT (NeurIPS), ManagerBench (ICLR)
- **Tool Use & Orchestration**: NaviAgent, MCP-Persona, Agent-Omit
- **Evaluation**: CORE (full-path), EvoClaw (continuous), TRACE (self-evolving benchmarks)

### 📊 Recommendation & CTR

**Three converging paradigms**:
1. **LLM-as-Ranker**: CTR-Sink, CADET, IDProxy — adapting LLMs for ranking with attention sinks, decoder-only architectures, and MLLM cold-start
2. **Generative Recommendation**: HSTU (Meta), GRACE (Walmart), TokenMixer (ByteDance) — reframing recommendation as next-token prediction with scaling laws
3. **Reasoning-Augmented Recommendation**: R²ec, RecZero, ScotRec — adding explicit CoT reasoning before prediction

### 🎮 Game AI & Foundation Models
- NVIDIA NitroGen (CVPR 2026): 1000+ game foundation model
- ByteDance Game-TARS: 500B+ token generalist agent
- DeepMind: DAGS (data-augmented self-play), DreamerV3 (world model), Looped World Models
- Industry deployment: NVIDIA ACE in PUBG/Total War/inZOI (2026)

### 🏗️ Scaling & Architecture
- **Attention innovations**: Gated Attention (NeurIPS Best Paper), DSA sparse attention (DeepSeek → GLM-5), LRQK (long-context KV compression)
- **Hybrid architectures**: Mamba-Attention (Nemotron 3), MoE domination across flagships
- **Quantization**: OrbitQuant (W2A4 DiT), 4-bit LLMs with negligible variance impact
- **Efficiency**: SuffixDecoding, Hogwild! Inference, CTR-Sink

### 🔬 Benchmarks & Evaluation
- **Crisis in reviewing**: ICLR 2026 review crisis (21% AI-generated reviews, identity leak)
- **New benchmarks**: FutureX (agent future prediction), DeepSynth (deep synthesis), ManagerBench (safety-pragmatism), TRACE (self-evolving), CompBench (image editing), VideoRealBench (human-centric video)
- **Evaluation shift**: Process-level > outcome-level, trajectory-level > final-state, behavioral > static

---

##导航指引

### Related Wiki Pages
- [[tech-report-digest|LLM Tech Report Digest 2026-07-04]]
- [[game-rl-daily|Game RL & Game AI Bot Digest 2026-07-04]]
- [[arxiv-paper-check|arXiv Paper Check 2026-07-04]]
- [[ctr-scaling-landscape|CTR Scaling Landscape]]

### Key Files
- Raw data source tracking: N/A (auto-generated survey)
- Index location: [[index|Wiki Index]]
