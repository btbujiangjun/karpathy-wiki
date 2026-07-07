---
title: "arXiv Paper Check — AI & CTR (July 7, 2026)"
type: synthesis
created: 2026-07-07
updated: 2026-07-07
sources: []
tags: [arxiv, ai, ctr, paper-scan, july-2026]
---

# arXiv Paper Check — AI & CTR (July 7, 2026)

> New listings for **Friday, 3 July 2026** — the most recent arXiv batch. Scanned **cs.AI** (228 new), **cs.LG** (181 new), **cs.IR** (12 new). This report focuses on papers not covered in the July 6 scan.

## LLM Safety, Alignment & Theory

| Paper | ID | Key Contribution |
|-------|-----|-----------------|
| **How to Avoid Debate: Scalable AI Safety via Doubly-Efficient Interactive Proofs** | 2607.03561 | Single-prover interactive proofs for oracle-aided computations; ICML 2026. Shows verification is possible without debate under structured or noise-tolerant oracle access |
| **Teacher Supervision over Representation Equivalence Classes** | 2607.03572 | Knowledge distillation through equivalence classes, not absolute features. Restoration achieves CKA ~0.99 but doesn't recover capability — only logit matching drives it |
| **On the Convergence of Adam, Revisited** | 2607.03519 | Projected Adam can have average regret bounded away from zero (extending Reddi-Kale-Kumar 2018). Extends to AdamW, RMSProp, NAdam, Adan, AdaMax, Muon |
| **Co-Adaptive Multi-Task LoRA (CoDA)** | 2607.03522 | Transfer-aware label-free controller for multi-task LoRA. Solves QP on simplex to set per-domain participation. Improves over uniform mixing, learned mixtures, gradient surgery |
| **Aligning Language Models with Selective Prediction (RLSR)** | 2607.03528 | RL for area under risk-coverage curve (AURC) as alignment objective. Improves LLM reliability by balancing risk-coverage trade-off; ICML 2026 Workshop |
| **Online Safety Monitoring for LLMs** | 2607.02510 | Bayesian online monitoring framework for LLM outputs; detects distribution shift in safety-relevant dimensions |
| **Fast Multi-dimensional Refusal Subspaces via RFM-AGOP** | 2607.02396 | Identifies low-dimensional refusal subspaces in LLM activations; ICML 2026 Mech Interp Workshop |
| **Steerability via Constraints** | 2607.02389 | Constraint-based substrate for scalable oversight of coding agents; ICML 2026 DLC Workshop |

## LLM Agents & Systems

| Paper | ID | Key Contribution |
|-------|-----|-----------------|
| **Safety Testing LLM Agents at Scale** | 2607.01793 | End-to-end pipeline from risk discovery to evidence-grounded verification for LLM agents |
| **Atomic Task Graph** | 2607.01942 | Unified framework for agentic planning and execution using atomic task decomposition |
| **PACE: Proxy for Agentic Capability Evaluation** | 2607.02032 | Lightweight proxy evaluation for agentic capabilities without full task execution |
| **EvoPolicyGym** | 2607.02440 | Benchmark for evaluating autonomous policy evolution in interactive environments |
| **AgenticSTS: Bounded-Memory Testbed for Long-Horizon Agents** | 2607.02255 | Testbed designed specifically for long-horizon agent tasks with bounded memory constraints |
| **DRIFTLENS** | 2607.02374 | Measures memory-induced reasoning drift in personalized language models |
| **CAGE-1: Control, Assurance, and Governance Evaluation for Enterprise Agentic AI** | 2607.03510 | Evaluation framework for enterprise agent deployment: authority, policy, memory integrity, tool safety, auditability. Introduces Prebind Assurance concept |
| **AGL-1: Enterprise AI Governance Layer** | 2607.03516 | Vendor-neutral reference model for AI governance control plane across foundation models, retrieval, orchestration, enterprise memory |

## Architectures & Training Methods

| Paper | ID | Key Contribution |
|-------|-----|-----------------|
| **WeightCLIP: Aligning Datasets and Models for Weight Space Learning** | 2607.03551 | Dataset-aligned latent space for neural network weights using contrastive learning. Enables retrieval, generation, and refinement; **ICML 2026** |
| **MentalThink: Shaping Thoughts in Mental SVG World** | 2607.03530 | Visual-symbolic reasoning paradigm where MLLMs generate, render, and interpret SVG code as intermediate representation for multi-turn reasoning |
| **NDVM: Native Differentiable Virtual Machine** | 2607.03574 | Runtime representation for neuro-symbolic learning that differentiates programs without per-candidate graph compilation. 24× faster co-search in wall-clock time |
| **Expander Sparse Autoencoders** | 2607.01799 | Parameter-efficient dictionaries for mechanistic interpretability; expands number of features per parameter |
| **Bayesian Sparse Low-Rank Adaptation (BayesLoRA)** | 2607.02182 | Bayesian treatment of sparse LoRA for LLM uncertainty estimation; 16 pages |
| **Conditional Co-Ablation** | 2607.01940 | Recovers self-repair backups in transformer circuits by identifying co-ablated components |
| **G-RRM: Guiding Symbolic Solvers with Recurrent Reasoning Models** | 2607.02491 | Recurrent reasoning model that guides symbolic solvers; hybrid neuro-symbolic approach |
| **A Hippocampus for Linear Attention** | 2607.02303 | Exact memory mechanism for what linear attention recurrent states forget; bridges linear attention and exact recall |
| **Spec-AUF: Accept-Until-Fail Training** | 2607.01893 | Train-inference misalignment for masked block drafters in speculative decoding |

## Diffusion & Generative Models

| Paper | ID | Key Contribution |
|-------|-----|-----------------|
| **Mixture-of-Gaussians-Guided Schedule Design for BBDM** | 2607.03517 | Analytical framework for Brownian Bridge Diffusion Model schedule design; proves universal schedules exist independent of degradation and prior |
| **Optimizing Visual Generative Models via Distribution-wise Rewards** | 2607.02291 | RL-based optimization of generative models using distribution-level rewards; **ICML 2026** |
| **ART for Diffusion Sampling: Continuous-Time Control and Actor-Critic Learning** | 2607.02137 | Formulates diffusion sampling as continuous-time control problem; actor-critic framework for improved generation |
| **Subliminal Clocks: Latent Time Modelling in Diffusion LMs** | 2607.01774 | Learns implicit time representations within diffusion language model hidden states |

## Recommendation, CTR & IR

| Paper | ID | Key Contribution |
|-------|-----|-----------------|
| **Bringing Agentic Search to Earth Observation Data Discovery** | 2607.02387 | Agentic search system for earth observation data; multi-step retrieval over geospatial metadata |
| **Evaluating Chunking Strategies for RAG on Academic Texts** | 2607.01852 | Systematic evaluation of chunking strategies; empirical findings for RAG on academic corpora |
| **Relevance-Based Embeddings: Lightweight Candidate Retrieval** | 2607.03515 | Embeds queries/items via relevance scores from expensive rankers; theoretically proven to approximate any complex similarity model |
| **CoPersona: Collaborative Persona Graphs** | 2607.01485 | Collaborative persona graphs for robust LLM personalization; KDD '26 |
| **HNSW with Accuracy Guarantees Using Graph Spanners** | 2607.02338 | HNSW index with provable accuracy guarantees via graph spanner theory; VLDB 2027 (cross-list cs.DB) |

## Time Series, Graphs & Applications

| Paper | ID | Key Contribution |
|-------|-----|-----------------|
| **Zeus: Towards Tuning-Free Foundation Model for Time Series Analysis** | 2607.01918 | Tuning-free foundation model for time series analysis; SOTA across forecasting, imputation, anomaly detection; **ICML 2026** |
| **Self-Gating Attention for Efficient Time Series Forecasting** | 2607.02344 | Self-gating mechanism adaptively selects relevant temporal patterns; efficient forecasting |
| **Extreme Adaptive Transformer for Time Series Forecasting** | 2607.02437 | Transformer architecture optimized for extreme value prediction in time series |
| **Graph Classification via Network Usable Information (NetinfoGC)** | 2607.03587 | Training-free graph classification using centrality measures + NUI estimation; strong correlation with downstream accuracy |
| **AquaGen: All-Atom Generative Model for Molecular Dynamics** | 2607.03513 | First all-atom explicit solvent generative model producing Boltzmann-distributed configurations; 4-10× faster than MD for hydration free energy |
| **Generalization in offline RL: Structure > Amount of Pessimism** | 2607.02288 | Large-scale study showing structural properties of offline RL algorithms matter more than pessimism level |

## Other Notable Papers

| Paper | ID | Key Contribution |
|-------|-----|-----------------|
| **Grounded Autonomous Research: LLM Pipeline from Corpus to Manuscript** | 2607.02329 | Fault-tolerant LLM pipeline for computational physics; ICML 2026 AI4Science Workshop |
| **Hidden Forgetting in Continual Multimodal Learning** | 2607.02020 | Shows accuracy can survive while grounding fails — hidden forgetting undetected by standard metrics |
| **InduceKV: Fixed-Footprint Continual Adaptation of MLLMs** | 2607.02010 | KV-memory-based adaptation for multimodal LLMs without full fine-tuning |
| **Evidence-State Rewards for Long-Context Reasoning** | 2607.02073 | Reward modeling based on evidence state tracking for long-context reasoning tasks |
| **SUNTA: Hierarchical Video Prediction with Surprise-based Chunking** | 2607.02087 | Video prediction using surprise-driven hierarchical temporal chunking |
| **Pre-Flight: Benchmark for LLM Aviation Operational Knowledge** | 2607.01829 | First benchmark evaluating LLMs on aviation operational knowledge |
| **DecompRL: Learning Modular Code Generation** | 2607.02390 | RL-based approach to learn modular code decomposition for harder programming problems |
| **Gaming Consensus: Coordinated Manipulation in Crowdsourced Fact-Checking** | 2607.01824 | Analysis of coordinated manipulation attacks in crowdsourced fact-checking systems; ICML 2026 |
| **A More Accurate Algorithm Comparison through A/B Testing** | 2607.01958 | Offline evaluation methods for more reliable algorithm comparison; KDD 2026 |

## Key Themes

1. **Single-prover AI verification** — Doubly-efficient interactive proofs show safety verification is possible without adversarial debate, extending to oracle-aided computations (e.g. web, human judgment)
2. **Knowledge distillation theory** — Teacher Supervision paper shows absolute feature matching is ill-posed; only logit matching (output function) drives capability transfer
3. **Enterprise AI governance** — AGL-1 and CAGE-1 establish formal reference models and evaluation frameworks for governable agentic AI deployment
4. **Weight-space learning** — WeightCLIP opens a new paradigm: dataset-aligned latent spaces for neural network weights; enables retrieval, generation, and model refinement
5. **Multi-task co-adaptation** — CoDA solves the multi-task LoRA problem without labels; entropy-regularized QP for transfer-aware domain participation
6. **Neuro-symbolic runtimes** — NDVM differentiates programs without per-candidate compilation, achieving 24× faster co-search for scientific discovery
7. **No CTR-specific papers** in this batch — consistent with the slower cadence of cs.IR updates (only 12 entries on Friday)
