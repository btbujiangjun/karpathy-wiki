---
title: arXiv Daily - 2026-09-03
type: synthesis
created: 2026-09-03
updated: 2026-09-03
tags: [arxiv, daily, LLM, recommendation, CTR, advertising, sequential-modeling, games, AI]
---

# arXiv Daily Report — 2026-09-03

> Curated selection of recent arXiv papers across LLMs, recommendation systems, CTR prediction, advertising, sequential modeling, and games.

---

## Large Language Models (LLMs)

### 1. Kimi K3: Open Frontier Intelligence

| Field | Detail |
|-------|--------|
| **Authors** | Moonshot AI Team |
| **Institution** | Moonshot AI (Kimi) |
| **arXiv** | [2607.24653](https://arxiv.org/abs/2607.24653) |
| **Published** | Jul 2026 |

**Abstract:** Introduces Kimi K3, a 2.8T-parameter MoE model with 104B activated parameters, native vision, and a 1M-token context window. Built on Kimi Delta Attention (KDA) and Attention Residuals, with Stable LatentMoE activating 16 of 896 routed experts per token, achieving ~2.5x scaling efficiency over K2. Post-training includes RL across general, agentic, and coding domains with multiple reasoning-effort levels.

**Key Innovations:**
- 2.8T MoE with 896 routed experts (16 active), ~2.5x scaling efficiency gain
- Kimi Delta Attention for efficient long-sequence mixing
- Attention Residuals allowing selective multi-layer cross-attention
- Million-token agentic RL with persistent rollout and sandbox states
- Open-source release of full model weights

---

### 2. Matryoshka Language Model Suites

| Field | Detail |
|-------|--------|
| **Authors** | Not specified (likely industry/academic team) |
| **Institution** | Not specified |
| **arXiv** | [2608.09703](https://arxiv.org/abs/2608.09703) |
| **Published** | Aug 2026 |

**Abstract:** Proposes stacking sub-models of increasing size into a single nested architecture trained end-to-end, reducing total parameter count and enabling low-cost distillation from the largest to all smaller sub-models at every training step. Validates on 500M/1.5B/3B suite with 36% less training compute and 14-26% improved speculative decoding throughput.

**Key Innovations:**
- Single training run produces entire model suite (not independent training)
- Natural online distillation from largest to smallest sub-model
- Draft model contained within verifier for speculative decoding
- 36% less training compute vs independent baselines
- Near-parity performance with significantly fewer resources

---

### 3. LoGo: Token-Level Dynamic Local-Global Attention

| Field | Detail |
|-------|--------|
| **Authors** | Yuqi Pan et al. |
| **Institution** | Not specified |
| **arXiv** | [2608.29539](https://arxiv.org/abs/2608.29539) |
| **Published** | 2026-08-30 |

**Abstract:** Token-level dynamic local-global attention mechanism using attention span as a proxy for budget allocation. Each layer has coupled local and global branches; all tokens get local attention while a learned gate activates global attention only for tokens requiring long-range information. Preserves scaling behavior of full-attention Transformers.

**Key Innovations:**
- Token-level adaptive attention span allocation (not static per layer/head)
- Threshold-based budget controller maintaining target global ratio
- Progressive masking schedule stabilizing training before sparse routing
- Query-sparse Triton kernels for practical speedups
- Interpretable learned span allocation patterns

---

### 4. REER-PT: Reverse-Engineered Reasoning for Pre-training Data Augmentation

| Field | Detail |
|-------|--------|
| **Authors** | Haoran Que et al. |
| **Institution** | Not specified |
| **arXiv** | [2608.30627](https://arxiv.org/abs/2608.30627) |
| **Published** | 2026-08-31 |

**Abstract:** Scalable framework extending Reverse-Engineered Reasoning to raw pre-training data. Identifies continuations that are difficult to predict but inferable from context, inserts concise reasoning annotations. Perplexity reductions of 0.42-7.29; 680M models gain up to 2.07 pp on knowledge and reasoning benchmarks.

**Key Innovations:**
- Sparse reasoning annotation that preserves source text integrity
- Perplexity as optimization signal for annotation quality
- Compatible with standard next-token pre-training objective
- ~0.05% annotation 13-grams appear verbatim (no data leakage)
- Up to 2.07 pp gain on knowledge/reasoning benchmarks

---

### 5. EVAR: Evidence-Validated Hypothesis Admission for Narrative Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Peilin Liu et al. |
| **Institution** | Not specified |
| **arXiv** | [2608.29835](https://arxiv.org/abs/2608.29835) |
| **Published** | 2026-08-30 |
| **Venue** | EMNLP 2026 Main Conference |

**Abstract:** Framework for budget-aware narrative reasoning that compiles narratives into immutable evidence stores, assigns instance-specific inference budgets, and validates hypotheses against locked evidence before admission. Improves both task performance and evidence faithfulness.

**Key Innovations:**
- Immutable evidence store with source-linked atomic claims
- Instance-specific inference budget from uncertainty signals
- Hypothesis-conditioned validation challenges before admission
- Sufficiency-based stopping mechanism avoiding unnecessary refinement
- Accepted at EMNLP 2026

---

### 6. Evaluating and Improving LLM Self-Modeling

| Field | Detail |
|-------|--------|
| **Authors** | Safety Research Team |
| **Institution** | Not specified |
| **arXiv** | [2608.30980](https://arxiv.org/abs/2608.30980) |
| **Published** | Aug 2026 |

**Abstract:** Studies self-modeling: an LLM's ability to answer questions about its own behavior. Introduces a benchmark for verifiable behavioral self-modeling questions and develops a scalable synthetic-data pipeline with RL post-training. Shows gains across three open-source model families but questions whether this constitutes genuine introspection.

**Key Innovations:**
- Benchmark for diverse self-modeling question types (binary, MC, numerical, free-text)
- Scalable synthetic training data pipeline from behavioral interventions
- RL post-training improves self-modeling across model families
- Cross-model transfer suggests behavioral self-modeling (not privileged introspection)
- Released evaluation and training code on GitHub

---

### 7. Do Large Language Models Favour Any Research Topics?

| Field | Detail |
|-------|--------|
| **Authors** | Mike Thelwall |
| **Institution** | University of Wolverhampton |
| **arXiv** | [2609.00323](https://arxiv.org/abs/2609.00323) |
| **Published** | 2026-08-31 |

**Abstract:** Explores topic biases in LLM-based research evaluation across 73,489 articles from 15 health/life sciences journals. Finds GPT-OSS-120B favors viruses/genes/cells and disfavors surveys/patients/students; Gemma 3 27B favors ML research. Demonstrates systematic inter-model topic biases.

**Key Innovations:**
- Large-scale analysis (73,489 articles) of LLM research evaluation bias
- Evidence of systematic topic biases across two LLMs
- Methodology using title/abstract word analysis for bias detection
- Shows LLMs exhibit AI bias for at least one input type (full-text vs. abstract)
- Practical implications for using LLMs in research evaluation

---

## Recommendation Systems

### 8. GenRec: An LLM-Backed Recommendation Ranker at Netflix

| Field | Detail |
|-------|--------|
| **Authors** | Netflix Team |
| **Institution** | Netflix |
| **arXiv** | [2608.10257](https://arxiv.org/abs/2608.10257) |
| **Published** | Aug 2026 |

**Abstract:** LLM-backed recommendation ranker built on an in-house foundational LLM. Phase 1 adapts an open-source LLM to Netflix data; Phase 2 post-trains with recommendation-specific data and reward signals. Achieves statistically significant improvements over production baseline with 40x less Phase-2 labeled training examples.

**Key Innovations:**
- Verbalized user histories replacing engineered features
- Catalog-aware ranking head ensuring no out-of-catalog recommendations
- Prefill-only inference approach for cost-constrained serving
- +1.6% offline MRR lift with 40x less training data
- Statistically significant gains in large-scale online A/B test (10% traffic, 4 weeks)
- Paradigm shift from feature engineering to context engineering

---

### 9. SCoRD: Semantic-Assisted Continual Retriever-Reranker Distillation

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2608.19998](https://arxiv.org/abs/2608.19998) |
| **Published** | Aug 2026 |
| **Venue** | CIKM 2026 |

**Abstract:** Continual knowledge distillation framework for LLM-based reranking pipelines under non-stationary data streams. Introduces a semantic reasoning assistant that distills LLM's intent inference into reusable guidance, enabling efficient retriever-reranker co-adaptation without repeated LLM inference.

**Key Innovations:**
- Semantic Reasoning Assistant for reusable intent-level guidance
- Selective distillation on low-confidence sequences only
- Retriever-to-reranker feedback using up-to-date representations
- Addresses first-formulated problem of continual KD for ID-retriever + LLM-reranker
- Reduces LLM inference and update costs for practical deployment

---

### 10. CoRRe: Training-Free LLM Recommendation with Post-LLM Refinement

| Field | Detail |
|-------|--------|
| **Authors** | K. Kyungho et al. |
| **Institution** | Not specified |
| **arXiv** | [2608.19665](https://arxiv.org/abs/2608.19665) |
| **Published** | Aug 2026 |
| **Venue** | CIKM 2026 |

**Abstract:** Training-free framework injecting CF signals into LLM-generated item representations post-LLM. Refines item embedding directions via co-purchase graph and magnitudes via popularity. Outperforms training-free methods in 12/12 cases and training-based methods in 8/12 cases.

**Key Innovations:**
- Post-LLM paradigm: CF signals injected after LLM inference
- Direction refinement via item-item co-purchase graph propagation
- Magnitude refinement via item popularity normalization
- Fully training-free: no model training or fine-tuning needed
- Competitive with training-based methods (LightGCN, SASRec, etc.)

---

### 11. GALLM: Graph-Aware LLMs for Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Fenglin Yan, Bohao Wang et al. |
| **Institution** | Not specified |
| **arXiv** | [2608.12184](https://arxiv.org/abs/2608.12184) |
| **Published** | Aug 2026 |

**Abstract:** Constructs collaborative graph over text tokens and item tokens modeling three relation types (Text-Text, Item-Text, Item-Item). Relations transformed into lightweight learnable attention biases in LLM attention mechanism. Improves over strongest baseline by 9.76% on HR@5.

**Key Innovations:**
- Token-level collaborative graph with three relation types
- Lightweight learnable attention biases (not additional graph encoder)
- Joint modeling of semantic and global collaborative signals
- 9.76% average improvement on HR@5 across four benchmarks
- No structural modifications to LLM backbone

---

### 12. Semantic Codebook for Generative Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2608.21012](https://arxiv.org/abs/2608.21012) |
| **Published** | Aug 2026 |

**Abstract:** Replaces multi-level residual Semantic ID representation with single-level large semantic codebook + collaborative disambiguation token. Introduces exposure-aware dynamic codebook update. Reduces AR decoding FLOPs by ~48%, improves QPS by 28-47%, and achieves 0.792% primary consumption metric improvement in online A/B test.

**Key Innovations:**
- Single-level SID replacing multi-level residual codes
- Exposure-aware dynamic codebook with temporal decay
- 47-48% FLOPs reduction in AR decoding
- 28-47% single-card QPS improvement
- 0.792% online consumption metric lift (2.5% traffic, 5-day A/B)

---

### 13. RecPFN: Prior-Fitted Networks for In-Context Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | SAP Research Team |
| **Institution** | SAP |
| **arXiv** | [2608.19735](https://arxiv.org/abs/2608.19735) |
| **Published** | Aug 2026 |
| **Venue** | SIGIR 2026 |

**Abstract:** First embedding-based PFN-style ICL approach for sequential recommendation. Pretrained entirely on synthetic clickstream environments from a structural causal prior. Achieves SOTA zero-shot performance across 8 benchmarks without weight updates.

**Key Innovations:**
- First PFN-style in-context learning for sequential recommendation
- Pretrained solely on synthetic data (no real interaction logs needed)
- Single forward pass inference with support set conditioning
- SOTA zero-shot performance across 8 benchmarks
- Competitive with supervised methods in low-data regimes

---

### 14. Feedback-Grounded Policy Discovery for Generative Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2607.27789](https://arxiv.org/abs/2607.27789) |
| **Published** | Jul 2026 |

**Abstract:** Proposes a feedback-driven agent framework bridging the "Understanding-Action Gap" in generative recommendation. Separates intent knowledge from policy knowledge; policies evaluated by incremental utility over intent-only baseline. Transfers knowledge into two latent tokens via dual-space relational distillation for LLM-free inference.

**Key Innovations:**
- Understanding-Action Gap formalization
- Intent knowledge vs. policy knowledge separation
- Feedback-driven policy discovery with incremental utility evaluation
- Dual-space relational distillation into lightweight SID generator
- Large-scale online A/B: +4.506% Revenue, +4.621% ADVV

---

### 15. RecRec: Recursive Refinement for Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2607.10541](https://arxiv.org/abs/2607.10541) |
| **Published** | Jul 2026 |

**Abstract:** Lightweight model (3.9M-14M params) maintaining compact latent state updated through shared recursive module with evidence-anchored correction. Matches or outperforms SOTA sequential, graph-based, and reasoning-enhanced recommenders while being 99% smaller than LLM-based approaches.

**Key Innovations:**
- Recursive latent inference as alternative to deeper architectures
- Evidence-anchored correction preventing semantic drift
- Competitive with LLM recommenders at 99% fewer parameters
- Peak performance at T=7 recursion steps
- Demonstrates recursive refinement > increasing network depth

---

### 16. GOD: Graft-Oriented Distillation for Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2608.16073](https://arxiv.org/abs/2608.16073) |
| **Published** | Aug 2026 |
| **Venue** | CIKM 2026 |

**Abstract:** Component-level distillation framework replacing selected frozen-teacher components with trainable student counterparts to build hybrid source models. Provides component-level feedback for enhanced generalization. Outperforms baselines by up to 13.92%.

**Key Innovations:**
- Grafting: replacing teacher components with student counterparts in hybrid models
- Embed-Grafted and Encoder-Grafted Teacher models
- Graft-aware Contrastive Learning
- Component-level feedback (not just output-level KD)
- Zero additional inference cost

---

## Click-Through Rate (CTR) Prediction

### 17. EST: Efficiently Scalable Transformer for CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Mingyang Liu, Yong Bai, Zhangming Chan et al. |
| **Institution** | Alibaba (Taobao) |
| **arXiv** | [2602.10811](https://arxiv.org/abs/2602.10811) |
| **Published** | 2026-02-11 |

**Abstract:** Fully unified modeling for CTR prediction processing all raw inputs in a single sequence without lossy aggregation. Integrates Lightweight Cross Attention (LCA) pruning redundant self-interactions and Content Sparse Attention (CSA) using content similarity for dynamic behavior selection. Exhibits stable power-law scaling.

**Key Innovations:**
- Fully unified modeling: all raw inputs in single token sequence
- LCA: cross-attention between non-behavioral (query) and behavioral (KV) only
- CSA: content-similarity-guided dynamic behavior selection
- Power-law scaling relationship for predictable performance gains
- Online: +3.27% RPM, +1.22% CTR (Taobao display advertising)

---

### 18. GRAB: LLM-Inspired Sequence-First CTR at Baidu

| Field | Detail |
|-------|--------|
| **Authors** | Chuyue Xie et al. |
| **Institution** | Baidu |
| **arXiv** | [2602.01865](https://arxiv.org/abs/2602.01865) |
| **Published** | 2026-02-02 |

**Abstract:** End-to-end generative framework for CTR prediction inspired by LLM scaling. Integrates Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics and action signals. Monotonic, approximately linear improvement with longer interaction sequences.

**Key Innovations:**
- Generative ranking framework for CTR (LLM-inspired)
- CamA mechanism capturing temporal dynamics + action signals
- Scaling behavior: monotonic improvement with longer sequences
- Online: +3.05% revenue, +3.49% CTR
- End-to-end deployment at Baidu scale

---

### 19. Native Multimodal Representation Learning for CTR (Taobao)

| Field | Detail |
|-------|--------|
| **Authors** | Taobao Team |
| **Institution** | Alibaba (Taobao) |
| **arXiv** | [2608.24091](https://arxiv.org/abs/2608.24091) |
| **Published** | Aug 2026 |
| **Venue** | CIKM 2026 |

**Abstract:** Shows that end-to-end multimodal training (E2EM) fails for CTR because user behaviors are driven by both multimodal and non-multimodal factors, causing ambiguous supervision. Proposes Mine-Then-Train: mines high-quality multimodally interpretable samples, then fine-tunes encoder on them.

**Key Innovations:**
- First controlled demonstration that E2EM fails for CTR multimodal
- Mine-Then-Train paradigm: annotation model → sample mining → encoder fine-tuning
- Overcomes ambiguous supervision from non-multimodal behavior factors
- Online: +1.5% CTR, +0.5% RPM (Taobao display advertising)

---

### 20. PRIME: Plug-in Residual MoE for Shared CTR Top Networks

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2608.30449](https://arxiv.org/abs/2608.30449) |
| **Published** | Aug 2026 |

**Abstract:** Addresses semantic subgroup optimization competition in shared CTR top networks. PRIME retains Dense mapping as anchor with input-dependent routing for low-rank logit corrections. Reduces subgroup competition gap by 34.3%, improves mean AUC for 11/13 architectures.

**Key Innovations:**
- First controlled study of semantic subgroup competition in shared Top-NN
- Function-preserving conditional residual experts
- Zero-residual initialization matching Dense baseline at onset
- 34.3% relative reduction in optimization competition gap
- Improved AUC for 11 of 13 CTR architectures across two datasets

---

### 21. Long-History User Transformers for Real-Time Ad Ranking (Yandex)

| Field | Detail |
|-------|--------|
| **Authors** | Yandex Team |
| **Institution** | Yandex |
| **arXiv** | [2607.14331](https://arxiv.org/abs/2607.14331) |
| **Published** | Jul 2026 |

**Abstract:** Multi-stage architecture decoupling long-history encoding from real-time inference. Large offline transformer asynchronously encodes full cross-surface history into cached representation; lightweight runtime model combines with recent events. Recovers 72-80% of full-history quality ceiling.

**Key Innovations:**
- Offline/online split resolving latency-quality trade-off
- Autoregressive pre-training with dual objective (feedback + next-item)
- Two-tower CTR fine-tuning with DCNv2 backbone
- 72-80% quality recovery vs impractical full-history runtime model
- Online: +2.77% (search ads), +2.1% (YAN) with no latency increase

---

### 22. CRRN: Cascading Relevance for Trigger-Introduced Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2608.22973](https://arxiv.org/abs/2608.22973) |
| **Published** | Aug 2026 |

**Abstract:** Addresses Trigger-Introduced Recommendation (TIR) where users click trigger items with instant interest. CRRN extracts trigger-target interactions via personalized gating, fuses instant/personalized interests via cascading attention, and enhances relevance with category-assisted pairwise loss.

**Key Innovations:**
- Trigger-Target Interaction layer (explicit + implicit cross features)
- Cascading Interest Fusion with trigger intention prediction
- Category-assisted Pairwise Loss for trigger relevance
- Online (Tmall): +3.87% pCTR improvement

---

## Sequential Modeling

### 23. TSPORec: Token Selection via Preference Optimization for LLM-Based SR

| Field | Detail |
|-------|--------|
| **Authors** | Wenqiao Zhu, Chao Xu et al. |
| **Institution** | Not specified |
| **arXiv** | [2608.09605](https://arxiv.org/abs/2608.09605) |
| **Published** | Aug 2026 |

**Abstract:** Three-stage pipeline selecting informative tokens from item text for LLM-based sequential recommendation. Uses proxy reward function for chunk-oriented token selection. Achieves up to 31.25% improvement and 63.4% inference overhead reduction.

**Key Innovations:**
- Differentiable proxy reward for token subset utility approximation
- Chunk-oriented policy training with frozen LLM backbone
- 64 selected tokens match 256-token HLLM performance
- Up to 31.25% NDCG improvement, 63.4% cost reduction
- Generalizes across LLM backbones (Qwen3, TinyLlama)

---

### 24. RecRec: Recursive Reasoning for Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2607.12945](https://arxiv.org/abs/2607.12945) |
| **Published** | Jul 2026 |
| **Venue** | RecSys 2026 |

**Abstract:** Decouples reasoning from prediction in sequential recommendation. Context Compressor distills backbone hidden states into R latent interests; Recursive Reasoner refines interests in separate intermediate latent space. Deep supervision allows freely adjustable reasoning depth at inference.

**Key Innovations:**
- Decoupled reasoning state from prediction state (breaking d-dim bottleneck)
- Multi-vector prediction from R latent interests (not single vector)
- Interest Diversity Regularizer for distinct behavior aspects
- RL-free: two simple supervised stages
- Inference-time depth adjustable without retraining

---

### 25. MIRAGE: Manifold-Informed Flow Matching for Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2607.23762](https://arxiv.org/abs/2607.23762) |
| **Published** | Jul 2026 |
| **Venue** | KDD 2027 |

**Abstract:** Identifies "Euclidean void" failure in continuous generative recommendation where straight interpolation paths cross unsupported regions. Rectifies embedding geometry around unchanged probability path using item co-occurrence graph as semantic manifold proxy. Enables accurate one-step inference.

**Key Innovations:**
- Euclidean void formalization for generative recommendation
- Manifold-informed rectification without changing probability path
- Co-occurrence graph as discrete manifold proxy (training only)
- One-step efficient inference with graph-free deployment
- Particular effectiveness for long-tail/sparse items

---

## LLM-Native Advertising

### 26. LLM-OSDA: Optimal-Stopping Dynamic Auction for LLM Advertising

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2608.00123](https://arxiv.org/abs/2608.00123) |
| **Published** | 2026-07-31 |

**Abstract:** Dynamic CPC auction integrating Bellman optimal stopping, winner allocation, and envelope pricing for multi-turn LLM conversations. Bid-independent LLM layer estimates contextual click quality. Under Bellman oracle, truthful bidding is weakly dominant.

**Key Innovations:**
- First CPC auction combining conversational intent estimation with endogenous stopping
- Bellman optimal stopping for bid-dependent timing
- Truthful bidding guaranteed via envelope pricing
- Learned StopNet approximating Bellman values
- +11% net revenue vs fixed-timing baselines

---

### 27. PILA: Plug-and-Play Insertion for LLM-Native Advertising

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2607.25590](https://arxiv.org/abs/2607.25590) |
| **Published** | Jul 2026 |

**Abstract:** Reformulates ad insertion as conditional response rewriting, decoupled from upstream LLM as a lightweight sidecar module. Model-agnostic, works with API-only systems. Provides controllable trade-off via PKM-grounded intensity controller.

**Key Innovations:**
- Sidecar architecture: ad insertion decoupled from content generation
- Model-agnostic: compatible with GPT-5.4, Gemini 3.1, Claude 4.5, etc.
- 25k high-quality training corpus with quality-controlled synthesis
- Intensity controller for naturalness-exposure trade-off
- +17-18% improvement across 7 frontier commercial models

---

### 28. LAMA: Token-Level Advertising via Latent Advertiser Mixture Auction

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2608.27382](https://arxiv.org/abs/2608.27382) |
| **Published** | Aug 2026 |
| **Venue** | KDD 2027 |

**Abstract:** Token-level advertising mechanism embedding advertiser influence directly into generation process. Advertisers report local continuation values inducing advertiser-specific next-token policies; platform decodes through latent mixture while updating allocation posterior.

**Key Innovations:**
- Token-level granularity for advertiser influence
- Bayesian allocation posterior evolving with observed tokens
- Markov DSIC and IR satisfaction
- Near-optimal KL-regularized welfare
- First proof-of-concept for generation-native advertising

---

### 29. Evaluating and Pricing Advertisements in AI-Generated Responses

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2607.27686](https://arxiv.org/abs/2607.27686) |
| **Published** | 2026-07-30 |

**Abstract:** Constructs click-through intent supervision via psychologically grounded agent simulation, distills into parameter-efficient evaluator. Evaluator surpasses frontier zero-shot judges (79% vs 60-67% relevance sensitivity). Builds pricing layer with truthful payment rule.

**Key Innovations:**
- Persona-agent simulation for CTI label construction
- Shared-bottleneck architecture over frozen Qwen3-4B
- EMD objective respecting ordinal scale geometry
- Surpasses frontier LLM judges on relevance sensitivity
- Truthful payment rule with best-of-k allocation

---

### 30. Neuron Auctions for LLM Advertising

| Field | Detail |
|-------|--------|
| **Authors** | Peiran Yun, Wenxin Xu et al. |
| **Institution** | Not specified |
| **arXiv** | [2605.08326](https://arxiv.org/abs/2605.08326) |
| **Published** | 2026-05-08 |

**Abstract:** Shifts auction object from surface text to LLM internal representations. Identifies brand-specific FFN neurons activating in approximately orthogonal subspaces. Defines continuous intervention budgets (neuron counts, amplification factors) as auctionable commodities.

**Key Innovations:**
- Auction paradigm shift: text space → internal representation space
- Brand-specific FFN neurons in orthogonal subspaces
- Continuous menu-based auction guaranteeing strategy-proofness
- Dynamic pricing of overly aggressive interventions via user utility penalty
- Preserves natural discourse quality

---

## Games & Reinforcement Learning

### 31. Twin: Test-Time Digital Twin for Playing Unknown Games

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2608.14490](https://arxiv.org/abs/2608.14490) |
| **Published** | Aug 2026 |

**Abstract:** Test-time world-model inference system for ARC-AGI-3. Coding agent writes executable world model from simulation and interaction alone. Harness enforces model matches all previous transitions before every action. Clears 179/183 levels (97.8%), more efficient than humans on 158/179 levels.

**Key Innovations:**
- Test-time written world model (not hand-engineered)
- Validate-explore-plan loop with mismatch-as-counterexample
- Goal hypothesis before any reward (87.2% correct pre-reward)
- 93.3/100 action-efficiency score (vs 7.8% direct, 61.1% standard harness)
- Solves 23/25 games, reaches 100.0 on 18 games

---

### 32. CAST: Game Solvers as Turn-Level Teachers for LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2607.25308](https://arxiv.org/abs/2607.25308) |
| **Published** | Jul 2026 |

**Abstract:** Converts game solver state-value changes into turn-level signals for RLVR. Under soft-optimal solver assumption, maximizing solver advantage equals on-policy distillation from solver. Achieves best performance across Sokoban, Minesweeper, Rush Hour.

**Key Innovations:**
- Turn-level credit assignment from solver state-value changes
- Logit-free on-policy distillation (scalar advantage suffices)
- 1.7-2.0x fewer training steps to reach DAPO's peak
- Zero-shot transfer to ALFWorld and WebShop
- Negligible solver overhead; learned value network retains most benefit

---

### 33. Augmenting Game AI with Deep RL (EA SPORTS FC / Battlefield)

| Field | Detail |
|-------|--------|
| **Authors** | Alessandro Sestini, Joakim Bergdahl et al. |
| **Institution** | EA (Electronic Arts) |
| **arXiv** | [2606.20210](https://arxiv.org/abs/2606.20210) |
| **Published** | 2026-06-18 |

**Abstract:** Framework for deploying RL in AAA game production. Applied to goalkeeper AI in EA SPORTS FC 25 and infantry in Battlefield 6. Uses SAC with network resets, offline data, scenario-based training to reduce training from 4 days to 12 hours. 300K param MLP with 170µs inference.

**Key Innovations:**
- Production-ready RL framework for AAA games
- Training time reduction from 4 days to 12 hours (overnight training)
- Modular integration with existing game AI systems
- Strict 200µs inference budget for real-time deployment
- Demonstration in two major commercial titles

---

### 34. Sensi: Curriculum-Based Test-Time Learning for Game Agents

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Institution** | Not specified |
| **arXiv** | [2603.17683](https://arxiv.org/abs/2603.17683) |
| **Published** | 2026-03-17 |

**Abstract:** Two-player LLM agent architecture for ARC-AGI-3 separating perception from action. v2 adds curriculum learning via state machine, database-as-control-plane, and LLM-as-judge evaluation. Completes learning curriculum in ~32 interactions (50-94x more sample-efficient).

**Key Innovations:**
- Separation of perception (Observer) and action (Actor)
- Curriculum-based learning via external state machine
- Database-as-control-plane for programmable context injection
- 50-94x more sample-efficient than comparable systems
- Precise failure diagnosis: self-consistent hallucination cascade

---

### 35. Self-Play RL under Imperfect Information in Big 2

| Field | Detail |
|-------|--------|
| **Authors** | Aalok Patwa |
| **Institution** | Not specified |
| **arXiv** | [2605.28863](https://arxiv.org/abs/2605.28863) |
| **Published** | 2026-05-21 |

**Abstract:** Self-play RL framework for Big 2, a four-player imperfect-information card game. Compares policy-gradient and value-approximation agents. PPO outperforms Monte Carlo Q, SARSA, and Q-learning. Moderate entropy regularization prevents overly deterministic policies.

**Key Innovations:**
- Controlled RL comparison framework for imperfect-information games
- PPO superiority over value-based methods in multiplayer card games
- Entropy regularization as anti-determinism mechanism
- Current-policy self-play > checkpoint self-play for curriculum
- Big 2 as useful testbed for delayed rewards and variable action sets

---

## Summary Statistics

| Category | Papers |
|----------|--------|
| Large Language Models | 7 |
| Recommendation Systems | 9 |
| CTR Prediction | 6 |
| Sequential Modeling | 3 |
| LLM-Native Advertising | 5 |
| Games & RL | 5 |
| **Total** | **35** |

## Key Trends

1. **LLM-Native Recommendation Goes Production**: Netflix (GenRec), Taobao (EST, Native Multimodal), Baidu (GRAB), and Yandex demonstrate LLM-scale models achieving real online gains in CTR/rec systems
2. **Token-Level Advertising**: Multiple papers explore advertising at generation-token granularity (LAMA, Neuron Auctions), moving beyond slot-based paradigms
3. **Recursive/Iterative Refinement**: Both in recommendation (RecRec) and sequential modeling (TSPORec), iterative refinement outperforms single-pass approaches
4. **Test-Time World Models**: Twin and Sensi demonstrate that writing world models at test time is viable for complex game-playing tasks
5. **Scaling Laws Transfer to CTR**: EST shows LLM-inspired scaling laws apply to CTR prediction with proper architectural adaptations (LCA, CSA)
6. **Training-Free Methods Closing Gap**: CoRRe and RecPFN achieve competitive performance without any model training, relying on LLM embeddings + structural priors
