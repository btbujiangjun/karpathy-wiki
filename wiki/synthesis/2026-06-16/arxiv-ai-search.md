---
title: arXiv AI Search — Comprehensive Survey (June 16, 2026)
type: synthesis
created: 2026-06-16
updated: 2026-06-16
sources: [arxiv.org]
tags: [arxiv, survey, LLM, CTR, recommendation, advertising, games, sequential-modeling, RL, agents]
---

# arXiv AI Search — Comprehensive Survey

> Date: 2026-06-16 | Scope: LLM Architecture, Reasoning & Agents, CTR Prediction, Advertising & Generative Recommendation, Sequential Recommendation, Games & RL, Multi-Agent Systems

---

## 1. LLM Architecture & Efficiency

### 1.1 MiniMax Sparse Attention (MSA)
| Field | Detail |
|-------|--------|
| **Title** | MiniMax Sparse Attention |
| **Authors** | MiniMax AI Research |
| **Institution** | MiniMax |
| **arXiv** | [2606.13392](https://arxiv.org/abs/2606.13392) |
| **Abstract** | Blockwise sparse attention built upon GQA. A lightweight Index Branch scores KV blocks and selects a Top-k subset per GQA group; the Main Branch performs exact block-sparse attention over selected blocks. Co-designed GPU kernel with exp-free Top-k selection and KV-outer sparse attention. |
| **Key Innovations** | 28.4× per-token attention compute reduction at 1M context; 14.2× prefill and 7.6× decoding speedups on H800; matches GQA quality on 109B MoE model trained on 3T tokens; open-source inference kernel and production multimodal model released. |

### 1.2 Parallel Causal Associative Fields (PCAF)
| Field | Detail |
|-------|--------|
| **Title** | Parallel Causal Associative Fields: Gated Sparse Memory for Long-Context Language Modeling |
| **Authors** | — |
| **Institution** | Google Cloud TPU v4-32 |
| **arXiv** | [2606.10435](https://arxiv.org/abs/2606.10435) |
| **Abstract** | Replaces dense token-to-token attention with hash-bucket successor-token cache + local causal convolutional path + learned gate. Writes local records into hash buckets, retrieves bounded candidate set, forms sparse cache distribution, mixes with parametric local LM. |
| **Key Innovations** | 303M param PCAF beats matched dense Transformer on WikiText-103 (36.31 vs 47.49 PPL) and PG-19 (52.45 vs 53.84 PPL); 0.61–0.62M tokens/s throughput vs 0.43M; associative cache and learned gate both essential. |

### 1.3 Sliding-Window Transformers without PE Remain Turing Complete
| Field | Detail |
|-------|--------|
| **Title** | Rethinking the Role of Positional Encoding: Sliding-Window Transformers without PE Remain Turing Complete |
| **Authors** | A. Kozachinskiy, T. Steifer, P. Wałęga |
| **Institution** | — |
| **arXiv** | [2606.01532](https://arxiv.org/abs/2606.01532) |
| **Abstract** | Proves sliding-window transformers without positional encoding remain Turing complete. Introduces HIST model (token-count histogram within window) and shows window sliding itself breaks permutation symmetry. |
| **Key Innovations** | Separates two conflated notions: PE gives permutation-invariance inside a window, but FIFO window motion provides sequential structure sufficient for universal computation. |

### 1.4 Accelerating Speculative Diffusions via Block Verification
| Field | Detail |
|-------|--------|
| **Title** | Accelerating Speculative Diffusions via Block Verification |
| **Authors** | Alexander Soen, Hisham Husain, Valentin De Bortoli, Arnaud Doucet |
| **Institution** | University of Oxford |
| **arXiv** | [2606.13426](https://arxiv.org/abs/2606.13426) |
| **Abstract** | Adapts speculative sampling to continuous diffusion models. Introduces block verification for diffusions, provably improving acceptance rate. Free Drafter heuristic (self-speculative, no training) yields up to 6.3% speedup. |
| **Key Innovations** | First efficient block verification for diffusion models; formal analysis of Free Drafter; bridges LLM speculative decoding to diffusion domain. |

---

## 2. LLM Reasoning & Efficient Inference

### 2.1 Agentic Chain-of-Thought Steering (ACTS)
| Field | Detail |
|-------|--------|
| **Title** | Agentic Chain-of-Thought Steering for Efficient and Controllable LLM Reasoning |
| **Authors** | Yu Xia et al. |
| **Institution** | — |
| **arXiv** | [2606.03965](https://arxiv.org/abs/2606.03965) |
| **Abstract** | Formulates reasoning steering as MDP where a controller agent adaptively steers a frozen reasoner via reasoning strategy + steering phrase. Controller initialized from synthetic steering trajectories with multi-budget augmentation, optimized via RL with budget-conditioned reward shaping. |
| **Key Innovations** | Budget-aware strategy control; matches full-thinking performance with substantial token savings; enables controllable accuracy-efficiency trade-offs across different reasoners and tasks. |

### 2.2 TARPO: Token-Wise Latent-Explicit Reasoning via Action-Routing Policy Optimization
| Field | Detail |
|-------|--------|
| **Title** | TARPO: Token-Wise Latent-Explicit Reasoning via Action-Routing Policy Optimization |
| **Authors** | — |
| **Institution** | NKU (Nankai University) |
| **arXiv** | [2606.05859](https://arxiv.org/abs/2606.05859) |
| **Abstract** | Pure RL framework that adaptively switches between discrete token generation and continuous latent reasoning at each step. Lightweight action head router samples routing decision from binary mode-selection space. LLM backbone and router jointly optimized with shared group-relative advantage. |
| **Key Innovations** | Token-wise switching between discrete and latent reasoning; tested on Qwen2.5 (1.5B–7B) and Llama-3.1-8B; adaptive switching behavior with stable training dynamics. |

### 2.3 MemRefine: LLM-Guided Compression for Long-Term Agent Memory
| Field | Detail |
|-------|--------|
| **Title** | MemRefine: LLM-Guided Compression for Long-Term Agent Memory |
| **Authors** | Minjae Kim, Jinheon Baek, Soyeong Jeong, Sung Ju Hwang |
| **Institution** | KAIST |
| **arXiv** | [2606.13177](https://arxiv.org/abs/2606.13177) |
| **Abstract** | Formulates storage-budgeted memory management. Uses similarity only to propose candidate pairs; defers delete/merge/preserve decisions to an LLM judge based on factual content. Iterates until budget is met. |
| **Key Innovations** | Addresses unbounded memory growth in LLM agents; consistently meets target budgets while preserving downstream performance; outperforms rule-based baselines under tight budgets. |

### 2.4 Reward Modeling for Multi-Agent Orchestration (OrchRM)
| Field | Detail |
|-------|--------|
| **Title** | Reward Modeling for Multi-Agent Orchestration |
| **Authors** | Haizhou Shi et al. |
| **Institution** | — |
| **arXiv** | [2606.13598](https://arxiv.org/abs/2606.13598) |
| **Abstract** | Self-supervised framework evaluating orchestration quality without human annotations. Leverages intermediate artifacts to construct win-lose pairs for Bradley-Terry reward model training. Operates at orchestration level, avoiding costly sub-agent rollouts. |
| **Key Innovations** | Up to 10× token efficiency improvement; up to 8% accuracy gain in MAS test-time scaling; transfers across math reasoning, web QA, and multi-hop reasoning. |

---

## 3. LLM Agents & RL for Agents

### 3.1 Agentic Monte Carlo (AMC)
| Field | Detail |
|-------|--------|
| **Title** | Agentic Monte Carlo: Simulating Reinforcement Learning for Black-Box Agents |
| **Authors** | — |
| **Institution** | Layer6 AI |
| **arXiv** | [2606.05296](https://arxiv.org/abs/2606.05296) |
| **Abstract** | Uses Sequential Monte Carlo to sample from optimal policy of black-box LLM agents. Treats optimal policy as posterior over trajectories, prior = fixed black-box LLM agent. Learns value function to steer agent without modifying underlying model. |
| **Key Innovations** | First principled RL-style optimization of black-box agents; outperforms GRPO baselines with test-time compute scaling; validated on AgentGym benchmark (WebShop, SciWorld, TextCraft). |

### 3.2 HiPER: Hierarchical RL with Explicit Credit Assignment
| Field | Detail |
|-------|--------|
| **Title** | HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents |
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2602.16165](https://arxiv.org/abs/2602.16165) |
| **Abstract** | Factorizes policy into high-level planner (proposes subgoals) and low-level executor. Introduces Hierarchical Advantage Estimation (HAE) for credit assignment at both planning and execution levels. |
| **Key Innovations** | 97.4% success on ALFWorld, 83.3% on WebShop with Qwen2.5-7B-Instruct (+6.6% and +8.3% over best prior); provably reduced variance vs flat GAE. |

### 3.3 Reinforcement World Model Learning (RWML)
| Field | Detail |
|-------|--------|
| **Title** | Reinforcement World Model Learning for LLM-based Agents |
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2602.05842](https://arxiv.org/abs/2602.05842) |
| **Abstract** | Self-supervised method learning action-conditioned world models using sim-to-real gap rewards. Aligns simulated next states with realized next states in pre-trained embedding space. |
| **Key Innovations** | Avoids token-level fidelity collapse; +6.9 and +5.7 points over direct task-success RL on ALFWorld and τ² Bench; matches expert-data training performance. |

### 3.4 Beyond Semantic Organization: Memory as Execution State Management
| Field | Detail |
|-------|--------|
| **Title** | Beyond Semantic Organization: Memory as Execution State Management for Long-Horizon Agents |
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2606.06090](https://arxiv.org/abs/2606.06090) |
| **Abstract** | Proposes Mage, which structures memory as a two-layer hierarchical state tree: Grow/Compress/Maintain/Revise operations. Maintains active execution path, reuses inactive branches, prevents contamination. |
| **Key Innovations** | Average success rate +7.8–26.3% over baselines on MemoryArena benchmark; treats memory as active state manager, not passive semantic store. |

### 3.5 Joint Agent Memory and Exploration Learning (JAMEL)
| Field | Detail |
|-------|--------|
| **Title** | Joint Agent Memory and Exploration Learning via Novelty Signals |
| **Authors** | — |
| **Institution** | MobileLLM |
| **arXiv** | [2606.01528](https://arxiv.org/abs/2606.01528) |
| **Abstract** | Trains agentic memory and exploration policy together through novelty-driven interaction (code coverage as novelty signal in GUI domain). Memory and exploration form mutually dependent loop. |
| **Key Innovations** | Generalizes to unseen environments; rivals closed-source model exploration depth while reducing token consumption; annotation-free supervision via deterministic novelty signals. |

---

## 4. Games & RL with VLMs/LLMs

### 4.1 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games
| Field | Detail |
|-------|--------|
| **Title** | Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning |
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2605.00347](https://arxiv.org/abs/2605.00347) |
| **Abstract** | RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Proposes adapted PPO with lightweight turn-level critic, substantially improving stability over GRPO/Reinforce++. |
| **Key Innovations** | 3× average game progress vs frontier models; consistent cross-game generalization; VLM action priors significantly improve sample efficiency vs classical deep RL. |

### 4.2 MemoPilot: Test-Time Learning in Games via RL over Memory
| Field | Detail |
|-------|--------|
| **Title** | From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory |
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2606.08656](https://arxiv.org/abs/2606.08656) |
| **Abstract** | Plug-in memory copilot training memory update process via multi-turn GRPO. Introduces turn-wise reward signal and context-independent turn-level advantage estimation across rollouts. |
| **Key Innovations** | Ranked 1st in Elo on both Limit Texas Hold'em (1762) and Rock-Paper-Scissors (1590); outperforms all baseline memory methods and proprietary models including DeepSeek-V3.2. |

### 4.3 Sensi: Curriculum-Based Test-Time Learning for LLM Game Agents
| Field | Detail |
|-------|--------|
| **Title** | Sensi: Learn One Thing at a Time — Curriculum-Based Test-Time Learning for LLM Game Agents |
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2603.17683](https://arxiv.org/abs/2603.17683) |
| **Abstract** | LLM agent architecture for ARC-AGI-3 with two-player architecture (perception vs action), curriculum-based learning with external state machine, and database-as-control-plane. |
| **Key Innovations** | 50–94× sample efficiency (32 vs 1,600–3,000 interactions); identifies self-consistent hallucination cascade as bottleneck shifting from learning to perception. |

### 4.4 Think in Games (TiG)
| Field | Detail |
|-------|--------|
| **Title** | Think in Games: Learning to Reason in Games via Reinforcement Learning with Large Language Models |
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2508.21365](https://arxiv.org/abs/2508.21365) |
| **Abstract** | Empowers LLMs to develop procedural understanding through direct game interaction. Reformulates RL-based decision-making as language modeling: LLMs generate language-guided policies refined via online RL (GRPO). |
| **Key Innovations** | Bridges declarative vs procedural knowledge gap; competitive with dramatically lower data/compute vs conventional RL; provides step-by-step natural language explanations. |

### 4.5 Next-Token Prediction and Regret Minimization
| Field | Detail |
|-------|--------|
| **Title** | Next-Token Prediction and Regret Minimization |
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2603.28499](https://arxiv.org/abs/2603.28499) |
| **Abstract** | Formalizes training next-token predictors to play repeated games. Shows transformer models can efficiently represent low-regret distributions. Provides empirical evidence with small transformers. |
| **Key Innovations** | Connects LLM next-token prediction to online learning/regret minimization; theoretical construction + empirical validation with NanoDO. |

---

## 5. CTR Prediction

### 5.1 DeRes: Decoupling Residual Stability and Adaptivity
| Field | Detail |
|-------|--------|
| **Title** | DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction |
| **Authors** | — |
| **Institution** | Major social-media platform (331M interactions) |
| **arXiv** | [2606.07980](https://arxiv.org/abs/2606.07980) |
| **Abstract** | Dual-path residual: Identity path (first-order feature reuse) + Block Attention Residual path (cross-layer attention over earlier blocks). Pointwise AttnRes replaces Softmax with SiLU for parallel multi-interest patterns. |
| **Key Innovations** | +0.32% AUC at <5% additional FLOPs; 1.66× steeper compute-AUC scaling law (γ=0.118 vs 0.071); 8-layer DeRes matches 16-layer OneTrans (~2× compute saving). |

### 5.2 DS-MLP: Dual-Stream MLP for CTR
| Field | Detail |
|-------|--------|
| **Title** | Dual-Stream MLP is All You Need for CTR Prediction |
| **Authors** | — |
| **Institution** | RUCAIBox, Renmin University |
| **arXiv** | [2606.04944](https://arxiv.org/abs/2606.04944) |
| **Abstract** | Knowledge distillation consolidates explicit feature interaction into main MLP; parallel MLP captures implicit interactions. Two alignment strategies for dual-stream compatibility. |
| **Key Innovations** | Vanilla MLP structure achieves SOTA across Criteo, Avazu, MovieLens; highly scalable and efficient for large-scale systems. |

### 5.3 EST: Efficient Scaling Laws for CTR
| Field | Detail |
|-------|--------|
| **Title** | EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling |
| **Authors** | — |
| **Institution** | Alibaba (Taobao Display Advertising) |
| **arXiv** | [2602.10811](https://arxiv.org/abs/2602.10811) |
| **Abstract** | Unified transformer architecture for heterogeneous CTR inputs. LCA (focused on informative interactions) + CSA (content similarity for sparse long-behavior modeling). Clear power-law scaling trend. |
| **Key Innovations** | Online A/B: +1.22% CTR and +3.27% RPM (Guess), +2.01% CTR and +2.66% RPM (Post); SOTA offline + production deployment. |

### 5.4 LoopCTR: Recursive Computation Scaling
| Field | Detail |
|-------|--------|
| **Title** | LoopCTR: A Loop Scaling Paradigm for CTR Prediction |
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2604.19550](https://arxiv.org/abs/2604.19550) |
| **Abstract** | Sandwich design: Embedding → Loop Block (iterative reasoning) → Score Prediction. Hyper-Connected Residuals + MoE layer. Process supervision at every loop depth. Train-multi-loop, infer-zero-loop strategy. |
| **Key Innovations** | Zero-loop inference already surpasses all baselines; oracle analysis reveals 0.02–0.04 AUC headroom; more loops in training → consistently better performance. |

### 5.5 DAIAN: Deep Adaptive Intent-Aware Network
| Field | Detail |
|-------|--------|
| **Title** | DAIAN: Deep Adaptive Intent-Aware Network for CTR Prediction in Trigger-Induced Recommendation |
| **Authors** | Zhihao Lv, Longtao Zhang, Ailong He, Shuzhi Cao, Shuguang Han, Jufeng Chen |
| **Institution** | Xianyu (Alibaba) |
| **arXiv** | [2602.13971](https://arxiv.org/abs/2602.13971) |
| **Abstract** | Addresses "intent myopia" in trigger-induced recommendation. Reinforces similarity and adaptive selection for varying intents based on user behavior. |
| **Key Innovations** | Online A/B (20% traffic, June 2025): +1.59% CTR, +1.73% recommendation diversity, +2.37% bills increase. |

### 5.6 CDNet: Core-Behaviors Dual-View Interaction Network
| Field | Detail |
|-------|--------|
| **Title** | CDNet: Bridging Sequential and Contextual Features via Core-Behaviors and Global Interest-Distribution |
| **Authors** | — |
| **Institution** | Large-scale e-commerce platform |
| **arXiv** | [2603.12578](https://arxiv.org/abs/2603.12578) |
| **Abstract** | Fine-grained core-behavior interaction + coarse-grained global interest-distribution compensation. Selects 100 core behaviors from 1,600-length sequences. |
| **Key Innovations** | 10-day online A/B: +2.24% CTR lift with zero additional inference latency. |

### 5.7 GenCI: Generative User Intent for CTR
| Field | Detail |
|-------|--------|
| **Title** | GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction |
| **Authors** | — |
| **Institution** | WWW 2026 |
| **arXiv** | [2601.18251](https://arxiv.org/abs/2601.18251) |
| **Abstract** | Generative model trained with NTP to produce candidate interest cohorts. Hierarchical candidate-aware network refines cohorts via cross-attention. End-to-end with self-supervised regularization. |
| **Key Innovations** | Addresses overfitting to historically dominant features and information chasm from point-wise ranking; uses semantic ID representations for enhanced interest modeling. |

### 5.8 IDProxy: Cold-Start CTR with MLLMs
| Field | Detail |
|-------|--------|
| **Title** | IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs |
| **Authors** | Guillaume Salha-Galvan et al. |
| **Institution** | Xiaohongshu (RedNote) |
| **arXiv** | [2603.01590](https://arxiv.org/abs/2603.01590) |
| **Abstract** | MLLMs generate proxy embeddings from rich content signals for cold-start items. Explicitly aligned with existing ID embedding space, optimized end-to-end under CTR objectives. |
| **Key Innovations** | Successfully deployed on both Content Feed and Display Ads; serves hundreds of millions of users daily. |

---

## 6. Advertising & Generative Recommendation

### 6.1 GRAB: Generative Ranking for Ads at Baidu
| Field | Detail |
|-------|--------|
| **Title** | GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm |
| **Authors** | Chuyue Xie et al. |
| **Institution** | Baidu |
| **arXiv** | [2602.01865](https://arxiv.org/abs/2602.01865) |
| **Abstract** | End-to-end generative CTR framework with Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics and action signals. |
| **Key Innovations** | Full deployment on Baidu: +3.05% revenue, +3.49% CTR; monotonic improvement with longer sequences; inference cost on par with DLRM baseline. |

### 6.2 OneRanker: Unified Generation and Ranking at Tencent
| Field | Detail |
|-------|--------|
| **Title** | OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation |
| **Authors** | Dekai Sun et al. |
| **Institution** | Tencent (WeiXin Channels) |
| **arXiv** | [2603.02999](https://arxiv.org/abs/2603.02999) |
| **Abstract** | Value-aware multi-task decoupling architecture with task tokens and causal masks. Coarse-to-fine target awareness (Fake Item Tokens + ranking decoder). Key/Value pass-through + Distribution Consistency loss. |
| **Key Innovations** | Full deployment on WeiXin Channels: GMV +1.34%; resolves optimization tension between generation and ranking stages. |

### 6.3 GR4AD: Generative Recommendation for Large-Scale Advertising
| Field | Detail |
|-------|--------|
| **Title** | GR4AD: Generative Recommendation for ADvertising |
| **Authors** | — |
| **Institution** | Kuaishou (400M+ users) |
| **arXiv** | [2602.22732](https://arxiv.org/abs/2602.22732) |
| **Abstract** | Production-oriented generative recommender with UA-SID tokenization, LazyAR (lazy autoregressive decoder), VSL + RSPO (ranking-guided preference optimization), and dynamic beam serving. |
| **Key Innovations** | Up to 4.2% ad revenue improvement over DLRM baseline; model scaling + inference-time scaling both contribute; fully deployed in Kuaishou advertising. |

### 6.4 GenRec: Preference-Oriented Generative Framework at JD
| Field | Detail |
|-------|--------|
| **Title** | GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation |
| **Authors** | — |
| **Institution** | JD App |
| **arXiv** | [2604.14878](https://arxiv.org/abs/2604.14878) |
| **Abstract** | Page-wise NTP task supervising entire interaction pages; asymmetric linear Token Merger for ~2× input compression; GRPO-SR (GRPO + NLL regularization + hybrid rewards). |
| **Key Innovations** | Online A/B: +9.5% click count, +8.7% transaction count; long-tail exposure +10%, click +16%, transaction +13%. |

### 6.5 DeGRe: Dense-supervised Generative Reranking
| Field | Detail |
|-------|--------|
| **Title** | DeGRe: Dense-supervised Generative Reranking for Recommendation |
| **Authors** | — |
| **Institution** | KDD 2026 |
| **arXiv** | [2605.25749](https://arxiv.org/abs/2605.25749) |
| **Abstract** | Dense-supervised generative reranking addressing position bias and credit assignment problems. Offline-online decoupled design. |
| **Key Innovations** | Online A/B: +2.85% CTR, +2.14% ORDER, +3.75% GMV; only +14.8ms inference latency. |

### 6.6 RankUp: High-rank Representations for Large Scale Advertising
| Field | Detail |
|-------|--------|
| **Title** | RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems |
| **Authors** | — |
| **Institution** | Tencent (WeChat Video Accounts, Moments, Official Accounts) |
| **arXiv** | [2604.17878](https://arxiv.org/abs/2604.17878) |
| **Abstract** | Mitigates embedding collapse and enhances latent representation diversity. Multi-task learning over 32 CVR objectives. |
| **Key Innovations** | Online A/B (20% traffic): up to 0.367% AUC gain; GMV lifts: +3.41% (Video Accounts), +4.81% (Moments), +2.12% (Official Accounts). |

### 6.7 UniRec: Chain-of-Attribute Generative Recommendation
| Field | Detail |
|-------|--------|
| **Title** | UniRec: Bridging the Expressive Gap between Generative and Discriminative Recommendation via Chain-of-Attribute |
| **Authors** | — |
| **Institution** | Shopee |
| **arXiv** | [2604.12234](https://arxiv.org/abs/2604.12234) |
| **Abstract** | Chain-of-Attribute (CoA) prefixes SID sequences with structured attribute tokens. Capacity-constrained SID with exposure-weighted penalties. Conditional Decoding Context. Joint RFT + DPO. |
| **Key Innovations** | Offline: +22.6% HR@50 overall, +15.5% high-value orders. Online: +5.37% PVCTR, +4.76% orders, +5.60% GMV. |

### 6.8 LLM Retrieval for Stable Ad Recommendations
| Field | Detail |
|-------|--------|
| **Title** | LLM Retrieval for Stable and Predictable Ad Recommendations |
| **Authors** | — |
| **Institution** | — |
| **arXiv** | [2605.21969](https://arxiv.org/abs/2605.21969) |
| **Abstract** | Semantic candidate generation framework using fine-tuned LLMs for ad retrieval. Extracts hierarchical semantic attributes from ad creatives, graph-based expansion for semantic variants. |
| **Key Innovations** | +0.45% topline online metric; +1.2% final stage recall; improves stability and predictability vs accuracy-only optimization. |

---

## 7. Sequential Recommendation

### 7.1 GenAIR: Generative Archetype-Grounded Item Representations
| Field | Detail |
|-------|--------|
| **Title** | GenAIR: Generative Archetype-Grounded Item Representations for Sequential Recommendation |
| **Authors** | — |
| **Institution** | WWW 2026 |
| **arXiv** | [2606.11023](https://arxiv.org/abs/2606.11023) |
| **Abstract** | LLM analyzes item metadata to infer textual description of Archetype (ideal target audience). Behavioral calibration objective adjusts embedding space to reflect empirical patterns. |
| **Key Innovations** | Plug-and-play with existing sequential models; significantly outperforms SOTA on 3 real-world datasets; bridges LLM semantic representations with behavioral patterns. |

---

## 8. Cross-Lingual & Safety

### 8.1 The Shibboleth Effect
| Field | Detail |
|-------|--------|
| **Title** | The Shibboleth Effect: Auditing the Cross-Lingual Distributional Skew of Large Language Models |
| **Authors** | Hakan Mehmetcik et al. |
| **Institution** | — |
| **arXiv** | [2606.11082](https://arxiv.org/abs/2606.11082) |
| **Abstract** | Multi-agent geopolitical wargame (Cerulean Sea Crisis) testing 6 frontier models in English vs Turkish. Llama-4 shows increased coercive rhetoric under Turkish (+0.800), Gemini-3.1-Pro and DeepSeek-R1 show decreases. |
| **Key Innovations** | Identifies two buffering mechanisms: chain-of-thought institutional anchoring and multilingual RLHF alignment; cross-lingual behavioral skew is model-specific, not universal. |

---

## 9. Key Trends Summary

| Trend | Papers | Implication |
|-------|--------|-------------|
| **Sparse/Long-Context Attention** | MSA, PCAF, Sliding-Window PE | Quadratic attention is being replaced by block-sparse/hash-based mechanisms; 1M+ context feasible for production |
| **Black-Box Agent RL** | AMC, ACTS, MemoPilot, OrchRM | Test-time compute and memory-based optimization for proprietary models |
| **Hierarchical Agent RL** | HiPER, RWML, Mage, JAMEL | Moving beyond flat policies; explicit subgoal decomposition for long-horizon tasks |
| **Game-Playing LLMs/VLMs** | Odysseus, MemoPilot, Sensi, TiG | RL + LLMs for games is rapidly maturing; 100+ turn horizons; cross-game generalization |
| **Generative CTR/Rec** | GRAB, OneRanker, GR4AD, GenRec, UniRec, DeGRe | End-to-end generative paradigm replacing cascaded pipelines across Baidu/Tencent/Kuaishou/JD/Shopee |
| **CTR Scaling Laws** | DeRes, EST, LoopCTR | Clear compute-AUC scaling trends; recursion and cross-layer attention as new scaling dimensions |
| **LLM-Enhanced Representations** | GenAIR, IDProxy, GenCI | LLMs used for item representation via archetypes, cold-start proxies, and interest cohorts |
