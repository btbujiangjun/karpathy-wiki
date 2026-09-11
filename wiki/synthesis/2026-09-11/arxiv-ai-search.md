---
title: "arXiv Recent Papers: AI, LLMs, Recommendation, Ads, Sequential Modeling, CTR, Games"
type: synthesis
created: 2026-09-11
updated: 2026-09-11
sources: []
tags: [arxiv, LLM, recommendation, CTR, advertising, sequential-modeling, game-AI, reinforcement-learning]
---

# arXiv Recent Papers Search Report (2026-09-11)

Curated list of recent arXiv papers across AI, LLMs, recommendation systems, advertising, sequential modeling, CTR prediction, and game AI.

---

## 1. LLMs & Reasoning

### 1.1 Structural Process Supervision for Latent Chain-of-Thought Reasoning
- **arXiv**: [2609.09928](https://arxiv.org/abs/2609.09928)
- **Date**: 2026-09-09
- **Institution/Company**: Not specified
- **Authors**: Not fully listed in search results
- **Abstract**: Proposes Prototype-Mediated Process Supervision (PMPS), introducing learnable reasoning prototypes as semantic anchors to provide structural process-level supervision for latent reasoning. Projects latent embeddings into a shared prototype space via soft alignment. A Progressive Sequential Alignment (PSA) module guides training with positional priors that gradually relax. Compresses output token length to under 50% of explicit CoT on GSM8K-Aug, achieving average accuracy gains of 2.08% across model families.
- **Key Innovations**: Learnable reasoning prototypes, soft alignment between unequal-length representations, progressive relaxation from sequential to adaptive matching.
- **Tags**: [LLM, chain-of-thought, latent reasoning, process supervision]

### 1.2 The Answer Path and Grounding Instruction in LLM Question Answering over Knowledge Graphs
- **arXiv**: [2609.10237](https://arxiv.org/abs/2609.10237)
- **Date**: 2026-09-09
- **Institution/Company**: Not specified
- **Abstract**: Systematic study of four design choices in graph RAG pipelines for KGQA. Key findings: (1) the answer path (triples needed to reach the answer) is critical — removing it costs most of the graph's value; (2) grounding instruction telling models to answer from provided facts drops F1 by 8.63x when context is empty; (3) syntax, triple order, and subgraph size have no measurable effect at multi-hop depth.
- **Key Innovations**: Comprehensive ablation over four RAG pipeline dimensions, identification of answer path and grounding instruction as the two factors that move accuracy.
- **Tags**: [LLM, knowledge-graphs, RAG, question-answering]

### 1.3 Beliefs and Behavior in Language Models
- **arXiv**: [2609.07943](https://arxiv.org/abs/2609.07943)
- **Date**: 2026-09-07
- **Authors**: Alex Smolin, Bryan Wilder
- **Institution/Company**: Not specified
- **Abstract**: Proposes an approach for empirically testing whether concepts like "belief" are well-applied to LLMs. Infers a single latent variable (degree of belief) from LLM outputs and tests whether it allows interpretable predictions of responses to new prompts. Finds highly capable models are usefully described as holding beliefs, and predictability of outputs based on inferred belief tracks model capability trends.
- **Key Innovations**: Latent belief variable inference from LLM outputs, empirical framework for testing LLM "beliefs," connection between belief predictability and model capability.
- **Tags**: [LLM, interpretability, beliefs, alignment]

### 1.4 PARSER: Read in Parallel, Reason in Depth for Long-Context LLM Agents
- **arXiv**: [2609.06702](https://arxiv.org/abs/2609.06702)
- **Date**: 2026-09-06
- **Institution/Company**: Not specified
- **Abstract**: Decouples reading from reasoning in long-context processing. A bank of lightweight subagents read chunks in parallel while a lead agent reasons through iterative scatter-gather rounds. Subagents remain frozen; lead agent is optimized with RL. Outperforms strongest sequential baseline by 5.7 points on average (up to 12.0 points at 896K tokens). Scaling to 9B backbone surpasses DeepSeek-V4-Pro by 6.3 points. Reduces inference latency by up to 11x.
- **Key Innovations**: Parallel read + sequential reason architecture, frozen subagents with trainable lead agent via RL, scatter-gather iterative reasoning, robustness to evidence placement.
- **Tags**: [LLM, long-context, agents, RL]

### 1.5 From Rollouts to Recipes: Self-Contained Post-Training for LLMs
- **arXiv**: [2609.01422](https://arxiv.org/abs/2609.01422) (Accepted at EMNLP 2026)
- **Date**: 2026-09-01
- **Institution/Company**: Not specified
- **Abstract**: Proposes Self-Routing, a behavior-conditioned post-training framework that uses rollout correctness and confidence to decide per-sample optimization strategy. Samples are routed to GRPO, on-policy self-distillation, regularization, or skipping. Consistently improves over uniform GRPO and simpler routing baselines on mathematical reasoning with Qwen3 and Qwen3.5 backbones.
- **Key Innovations**: Behavior-conditioned sample routing, per-sample optimization strategy selection, no external teachers or extra annotations needed.
- **Tags**: [LLM, post-training, GRPO, self-distillation]

### 1.6 The Geometry of Ignorance: LLMs Know When to Temper Bayesian Priors
- **arXiv**: [2609.02959](https://arxiv.org/abs/2609.02959)
- **Date**: 2026-09-02
- **Institution/Company**: Not specified
- **Abstract**: Discovers a "direction of ignorance" in the unembedding matrix — a single direction encoding the unigram distribution of training data that serves as the Bayesian prior LLMs fall back on when uncertain. Found across Llama, Qwen, Gemma, and Pythia (0.4B–405B). Projects prediction state into prior loading factor λ that declines with more informative context. The direction is causally active.
- **Key Innovations**: Direction of ignorance in unembedding geometry, per-token prior loading factor, causal demonstration of prior reliance.
- **Tags**: [LLM, interpretability, Bayesian reasoning, scaling]

### 1.7 Do Large Language Models Capture the Diversity in their Training Data?
- **arXiv**: [2609.02275](https://arxiv.org/abs/2609.02275)
- **Date**: 2026-09-02
- **Authors**: Youqi Wu, Farzan Farnia
- **Institution/Company**: Not specified
- **Abstract**: Studies whether LLMs capture the full diversity of outputs in training data via conditional entropy comparison. Finds model-generated outputs consistently exhibit lower conditional entropy than training data across OLMo, Pythia, GPT-Neo. Proposes a post-hoc correction mechanism using matrix-entropy projection with mirror-descent algorithm to increase conditional diversity.
- **Key Innovations**: Information-theoretic conditional diversity gap measurement, matrix-entropy projection for diversity correction, scalable mirror-descent algorithm.
- **Tags**: [LLM, diversity, entropy, information-theory]

---

## 2. Recommendation Systems

### 2.1 ReST: Scaling Sequence Transformers for Industrial Recommendation Ranking with Rec-Native Designs
- **arXiv**: [2609.01240](https://arxiv.org/abs/2609.01240)
- **Date**: 2026-09-01
- **Institution/Company**: Not specified (production advertising platform)
- **Abstract**: Proposes ReST, a recommendation-native Transformer scaling framework addressing signal quality (dual-gated attention, rotary positional/temporal embedding, stabilized residual normalization) and computation asymmetry (factorized ranking with heavy reusable encoder + lightweight cross decoder). Compute-once, decode-many-times serving. Online A/B test: +1.31% AUC, +11.93% core revenue metric within 50ms P99. Fully deployed in production.
- **Key Innovations**: Dual-gated attention, Rec-native Transformer scaling, compute-once/decode-many-times architecture, behavior-sequence scaling axis.
- **Tags**: [recommendation, transformer, scaling, production, ads]

### 2.2 TGR: Tencent Generative Recommendation — Unified Generation and Reasoning
- **arXiv**: [2609.00986](https://arxiv.org/abs/2609.00986)
- **Date**: 2026-09-01
- **Institution/Company**: Tencent
- **Abstract**: Industrial framework advancing recommendation toward generative paradigm. TGR-GenRank: CCFormer with unified feature tokenization, feature-field separated cross attention, hierarchical sequence compression. TGR-GenRec: BARGE (hierarchical semantic-ID generation) and HiGR (whole-slate generation). TGR-Reason: offline-generated reason tokens for online reasoning. Deployed across Tencent production surfaces. CCFormer: +3.57% CTR, +1.71% ad revenue. BARGE: +0.60% CTR. HiGR: 15.9–21.3% slate quality improvement. TGR-Reason: +477.8% cold-start Hit@1.
- **Key Innovations**: Three coupled generative directions (ranking, generation, reasoning), hierarchical semantic-ID generation, whole-slate generation, offline reasoning tokens.
- **Tags**: [generative-recommendation, production, Tencent, CTR, ads]

### 2.3 CORAL: An LLM-Native Harness for Production Recommender Systems
- **arXiv**: [2609.02730](https://arxiv.org/abs/2609.02730)
- **Date**: 2026-09-02
- **Institution/Company**: Not specified (two large-scale social platforms)
- **Abstract**: LLM-native harness that closes the continual optimization loop: agent observes signals, reasons over memory of past decisions, invokes tools (including numerical optimizer with fixed budget) to reconfigure recommender. Formulated as partially observed, non-stationary, constrained optimization with in-context policy improvement. Improves engagement at no extra cost on one platform; reduces serving cost without degrading engagement on another.
- **Key Innovations**: LLM agent in continual closed-loop optimization, in-context policy improvement without parameter updates, constrained optimization with guardrails.
- **Tags**: [LLM-agent, recommendation, production, continual-optimization]

### 2.4 CGM-Rec: Continual Graph Memory for Adaptive Recommendation under Intent Drift
- **arXiv**: [2609.04651](https://arxiv.org/abs/2609.04651) (Accepted at Findings of EMNLP 2026)
- **Date**: 2026-09-04
- **Institution/Company**: Not specified
- **Abstract**: Treats KG state as writable memory with two components: Semantic Graph Memory (conservatively updated via quality-gated typed operations) and Episodic Lesson Memory (fast reactive memory for recent outcomes and failures). During testing, model parameters remain frozen; adaptation occurs only through memory writes. Improves HR@1 by up to 29.58% over strongest LLM baseline on Bundle.
- **Key Innovations**: Continual graph memory, quality-gated typed operations, frozen-parameter adaptation via memory writes only.
- **Tags**: [recommendation, knowledge-graph, continual-learning, memory]

### 2.5 EAGER: Enrich-and-Align Generative Query Recommendation from Clicked Items in E-commerce Search
- **arXiv**: [2609.07143](https://arxiv.org/abs/2609.07143) (Accepted at EMNLP 2026 Industry Track)
- **Date**: 2026-09-07
- **Institution/Company**: Major e-commerce platform (deployed)
- **Abstract**: Two-stage framework for generating query suggestions from clicked items. Enrichment stage: four-stage SFT curriculum scaling information richness and reasoning depth with rationale augmentation, diversity regularization, and self-distillation. Alignment stage: GRPO with hybrid rule-based and preference-aware click reward. Deployed in production.
- **Key Innovations**: Four-stage curriculum SFT, GRPO alignment with hybrid reward, rationale augmentation, deployed in production e-commerce.
- **Tags**: [e-commerce, query-recommendation, generative, SFT, GRPO]

### 2.6 AdaKG: Adaptive Node-Aware KG Fusion for Recommendation
- **arXiv**: [2609.05909](https://arxiv.org/abs/2609.05909) (Accepted at CIKM 2026)
- **Date**: 2026-09-05
- **Institution/Company**: Not specified
- **Abstract**: Addresses indiscriminate KG incorporation in KG-aware recommendation. AdaKG separately encodes interaction graph and KG with view-specific encoders, estimates per-node reliance on item knowledge via adversarial perturbation stability, and adaptively aligns and fuses embeddings based on node-wise reliance.
- **Key Innovations**: Per-node adaptive KG contribution, adversarial perturbation-based stability measurement, view-specific encoding.
- **Tags**: [recommendation, knowledge-graph, adaptive-fusion]

### 2.7 From Feature Interaction to Feature Transport — CRAFT
- **arXiv**: [2609.01655](https://arxiv.org/abs/2609.01655) (Accepted at KDDCUP 2026 Workshop)
- **Date**: 2026-08-31
- **Institution/Company**: Not specified
- **Abstract**: Introduces feature transport paradigm treating deep recommendation as discrete context-conditioned representation evolution. CRAFT block summarizes non-sequential features into reliability-aware contextual field that generates residual displacement and memory-preserving signals. Achieves test AUC 0.838090 in TAAC2026 advertising competition, surpassing previous leaderboard-best. Benefits from both depth and width expansion.
- **Key Innovations**: Feature transport paradigm (beyond feature interaction), reliability-aware contextual field, residual displacement, scalable to depth/width.
- **Tags**: [feature-transport, recommendation, CTR, competition]

### 2.8 MGDiff: Multi-Interest Sequence Recommendation with Masking GNN-Guided Diffusion
- **arXiv**: [2609.01619](https://arxiv.org/abs/2609.01619)
- **Date**: 2026-06-30
- **Institution/Company**: Not specified
- **Abstract**: Multi-interest sequence recommendation using masking GNN-guided diffusion model. Dual-layer Semantic Guidance (DSG) decomposes into item semantics extraction and multi-dimensional user intent decoupling. Weight-adaptive Masking GNN reconstructs missing links. Dynamic Multi-Expert Network projects preferences into semantic subspaces. Popularity-Aware Guidance (PAG) recalibrates similarity metrics for diversity.
- **Key Innovations**: GNN-guided diffusion for sequence recommendation, dual-layer semantic guidance, popularity-aware guidance for bias-free generation.
- **Tags**: [sequence-recommendation, diffusion, GNN, multi-interest]

---

## 3. CTR Prediction & Advertising

### 3.1 UniCon: A Unified Context-Centric Modeling Paradigm for CTR Prediction
- **arXiv**: [2609.03290](https://arxiv.org/abs/2609.03290)
- **Date**: 2026-09-03
- **Institution/Company**: Meituan (search advertising)
- **Abstract**: Treats request context as the basic modeling unit, organizing history and prediction targets as homogeneous context units. Intra-context attention captures local coupling; inter-context attention models dynamic evolution of decision states. Context-unit-level sequence compression reduces deployment overhead. Online on Meituan search: +3.09% RPM, +2.07% CTR, +2.95% revenue.
- **Key Innovations**: Context-centric unified architecture, homogeneous context units for history and targets, intra/inter-context attention, context-level compression.
- **Tags**: [CTR, unified-modeling, Meituan, production]

### 3.2 EST: Efficiently Scalable Transformer for CTR Prediction via Unified Modeling
- **arXiv**: [2602.10811](https://arxiv.org/abs/2602.10811)
- **Date**: 2026-02-10
- **Institution/Company**: Alibaba (Taobao display advertising)
- **Abstract**: Achieves fully unified modeling by processing all raw inputs in a single sequence without lossy aggregation. Lightweight Cross-Attention (LCA) prunes redundant self-interactions; Content Sparse Attention (CSA) uses content similarity for dynamic behavior selection. Exhibits stable power-law scaling. Deployed on Taobao: +3.27% RPM, +1.22% CTR in Guess scenario; +2.01% CTR, +2.66% RPM in Post-Purchase.
- **Key Innovations**: Fully unified CTR modeling, LCA for cross-feature dependencies, CSA for content-guided sparse attention, power-law scaling laws for CTR.
- **Tags**: [CTR, transformer, scaling-law, Taobao, production]

### 3.3 GRAB: LLM-Inspired Sequence-First CTR Prediction at Baidu
- **arXiv**: [2602.01865](https://arxiv.org/abs/2602.01865)
- **Date**: 2026-02-02
- **Institution/Company**: Baidu
- **Abstract**: End-to-end generative framework for CTR with Causal Action-aware Multi-channel Attention (CamA) capturing temporal dynamics and action signals. Sequence Then Sparse (STS) training paradigm mitigates distribution shift from sequence packing. Online in Baidu home feed: +3.49% CTR, +3.05% CPM. Shows monotonic AUC improvement with longer sequences and larger models.
- **Key Innovations**: CamA mechanism, STS training paradigm for distribution shift mitigation, action-aware temporal modeling, scaling gains from longer sequences.
- **Tags**: [CTR, generative-recommendation, Baidu, production]

### 3.4 CADET: Context-Conditioned Ads CTR Prediction at LinkedIn
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Date**: 2026-02-11
- **Institution/Company**: LinkedIn
- **Abstract**: End-to-end decoder-only transformer for ads CTR. Context-conditioned decoding with multi-tower prediction heads for post-scoring signals (ad position). Self-gated attention stabilizes training. Timestamp-based RoPE captures temporal relationships across seconds-to-months timescales. Session masking for offline-online consistency. Online: +11.04% CTR lift, CPC -10.9%.
- **Key Innovations**: Context-conditioned multi-tower decoding, self-gated attention, timestamp-based RoPE for ads, session masking for train-serve consistency.
- **Tags**: [CTR, ads, LinkedIn, decoder-only-transformer, production]

### 3.5 Long-History User Transformers for Real-Time Ad Ranking
- **arXiv**: [2607.14331](https://arxiv.org/abs/2607.14331)
- **Date**: 2026-07-15
- **Institution/Company**: Yandex
- **Abstract**: Multi-stage architecture decoupling history encoding from real-time inference. Large offline transformer encodes full cross-surface history into cached representation; lightweight runtime model combines cached representation with recent events. Autoregressive pre-training with feedback + next-item prediction. Recovers 72–80% of full-history quality. Online: +2.77% search ads, +2.1% YAN.
- **Key Innovations**: Offline/online split architecture, autoregressive pre-training for ad ranking, cross-surface timeline, staleness-robust caching.
- **Tags**: [CTR, ads, long-context, Yandex, production]

### 3.6 UniVA: Unified Value Alignment for Generative Advertising at Tencent
- **arXiv**: [2605.05803](https://arxiv.org/abs/2605.05803)
- **Date**: 2026-07-29
- **Institution/Company**: Tencent (WeChat Channels)
- **Abstract**: Aligns commercial value across SID construction, autoregressive decoding, and online serving. Commercial SID Tokenization injects business attributes and bid info. Generation-as-Ranking SID Decoder fuses generation scores with value estimates. Value-Aware Constrained Serving uses personalized trie for request-valid paths. Offline HR@100: +37.04%. Online GMV: +1.5%.
- **Key Innovations**: Pipeline-wide value alignment, commercial SID tokenization, generation-as-ranking fusion, value-aware constrained serving via trie.
- **Tags**: [generative-recommendation, ads, Tencent, value-alignment]

### 3.7 OneRanker: Unified Generation and Ranking for Advertising at Tencent
- **arXiv**: [2603.02999](https://arxiv.org/abs/2603.02999)
- **Date**: 2026-03-12
- **Institution/Company**: Tencent (WeiXin Channels)
- **Abstract**: Value-aware multi-task decoupling architecture separating interest coverage and value optimization via task tokens and causal mask. Coarse-to-fine target awareness with Fake Item Tokens. Input-output dual-side consistency via KV pass-through and Distribution Consistency Constraint Loss. HR@1: +44.7% over GPR baseline. Online GMV-Normal: +1.34%.
- **Key Innovations**: Value-aware task decoupling, Fake Item Tokens for target awareness, distribution consistency constraint, architectural-level generation-ranking fusion.
- **Tags**: [generative-recommendation, ads, Tencent, unified-modeling]

### 3.8 GR4AD: Generative Recommendation for Large-Scale Advertising at Kuaishou
- **arXiv**: [2602.22732](https://arxiv.org/abs/2602.22732)
- **Date**: 2026-02-22
- **Institution/Company**: Kuaishou
- **Abstract**: Production-oriented generative recommender with UA-SID (unified advertisement semantic ID from fine-tuned MLLM), LazyAR decoder (relaxed layer-wise dependencies for fast multi-candidate generation), VSL + RSPO (ranking-guided list-wise RL), and Dynamic Beam Serving. Online: up to +4.2% ad revenue. <100ms latency, 500+ QPS per L20. Deployed serving 400M+ users.
- **Key Innovations**: UA-SID from MLLM, LazyAR efficient decoder, RSPO list-wise RL, dynamic beam serving with traffic-aware adaptation.
- **Tags**: [generative-recommendation, ads, Kuaishou, production, RL]

### 3.9 PRIME: Plug-in Residual Input-Conditioned MoE for Shared CTR Top Networks
- **arXiv**: [2608.30449](https://arxiv.org/abs/2608.30449)
- **Date**: 2026-08-31
- **Institution/Company**: Not specified
- **Abstract**: Addresses subgroup optimization competition in shared CTR top networks. PRIME anchors original Dense prediction with zero-residual initialization and adds input-dependent low-rank experts for example-specific logit corrections. Median AUC gains: +0.0022 (Avazu), +0.0066 (Criteo). Outperforms APG with fewer parameters and lower latency.
- **Key Innovations**: Function-preserving residual MoE, zero-residual initialization, multi-bag aggregation and EMA load bias stabilization.
- **Tags**: [CTR, MoE, feature-interaction, plug-in]

### 3.10 Agentic ML Exploration (A-MLE) for Ads Ranking
- **arXiv**: [2609.08248](https://arxiv.org/abs/2609.08248)
- **Date**: 2026-09-08
- **Institution/Company**: Not specified
- **Abstract**: Autonomous LLM-agent system that systematically explores ML techniques across a portfolio of ads ranking models. Five stages: hypothesis generation, exploration strategy, experiment execution, result analysis, shared knowledge substrate. Human-in-the-loop checkpoints. Cross-LLM study comparing Claude Sonnet, Gemini, and GPT families.
- **Key Innovations**: LLM agent for automated ML iteration, portfolio-level exploration across models, tiered capability framework, cross-LLM comparison.
- **Tags**: [LLM-agent, ads, automated-ML, ranking]

### 3.11 Native Multimodal Representation Learning for CTR in E-Commerce
- **arXiv**: [2608.24091](https://arxiv.org/abs/2608.24091) (Accepted at CIKM 2026)
- **Date**: 2026-08-25
- **Institution/Company**: Not specified
- **Abstract**: Addresses limitations of two-stage multimodal pre-training for CTR. End-to-end joint training doesn't help due to ambiguous supervision from multimodal and non-multimodal factors. Proposes Mine-Then-Train: mines high-quality multimodally interpretable training samples from CTR data and uses them to fine-tune multimodal encoder for better alignment with user click preferences.
- **Key Innovations**: Mine-Then-Train paradigm, resolving ambiguous multimodal supervision, sample mining for encoder alignment.
- **Tags**: [CTR, multimodal, e-commerce]

---

## 4. Game AI & Reinforcement Learning

### 4.1 LLM-Guided RL for Adaptive NPC Behavior in Multi-Agent Combat Games
- **arXiv**: [2609.02931](https://arxiv.org/abs/2609.02931)
- **Date**: 2026-08-27
- **Institution/Company**: Not specified
- **Abstract**: Runtime strategy-selection framework where LLM (Mistral 7B via Ollama) guides trained PPO policy without modifying behavior. Against Balanced opponent, win rate doubled from 11% to 24%. However, LLM showed limited zero-shot strategic differentiation — 83.8% preference for Surround regardless of opponent type. Demonstrates both potential and limitations of LLM-guided strategy selection.
- **Key Innovations**: LLM-guided runtime strategy selection, PPO + LLM hybrid approach, demonstration of both capability and limitation at 7B scale.
- **Tags**: [game-AI, LLM, RL, multi-agent, NPC]

### 4.2 PlayTrain: Efficient RL Framework for LLM-Generated JavaScript Games
- **arXiv**: [2609.09059](https://arxiv.org/abs/2609.09059)
- **Date**: 2026-09-08
- **Institution/Company**: Not specified
- **Abstract**: Combines LLM ability to generate JS games from minimal prompts with standard gym environment for RL training. Trains pixel-based agents end-to-end at over 1M agent-decisions per second on a single GPU. Demonstrates cloning Atari/ProcGen games and creating modified versions. Reimagines RL game development: all you need is a single LLM-generated JS file.
- **Key Innovations**: LLM-to-JS-game generation pipeline, gym-compatible RL from JS games, 1M+ decisions/second training speed.
- **Tags**: [RL, game-AI, LLM, JavaScript, synthetic-environments]

### 4.3 LUGL: Playing Games with Non-Incremental Learners
- **arXiv**: [2609.03660](https://arxiv.org/abs/2609.03660)
- **Date**: 2026-09-03
- **Institution/Company**: Not specified
- **Abstract**: Framework enabling gradient-boosted trees (LightGBM) for RL self-play by decoupling data collection from model fitting. Alternates local updates (self-play games accumulating tabular values) and global learning (generalization to unseen states). Competitive with or superior to DQN and DeepCFR across 4 perfect-information and 5 imperfect-information games.
- **Key Innovations**: LUGL framework for non-incremental learners in RL, LightGBM-based game playing, competitive with neural network approaches.
- **Tags**: [RL, game-AI, LightGBM, self-play]

### 4.4 NashDreamer: Model-Based RL for Zero-Sum Imperfect-Information Games
- **arXiv**: [2609.01549](https://arxiv.org/abs/2609.01549)
- **Date**: 2026-09-01
- **Institution/Company**: Not specified
- **Abstract**: Principled MBRL framework for two-player zero-sum IIGs. Introduces centralized Multi-Agent Recurrent State-Space Model (MARSSM) that decouples environment dynamics from strategy effects. Inherits convergence guarantees toward Nash equilibria under idealized model. Substantially improves sample efficiency over model-free baselines early in training. Identifies Dreamer family vulnerability to posterior collapse.
- **Key Innovations**: Centralized MARSSM for IIGs, decoupled dynamics/strategy modeling, theoretical analysis of posterior collapse vulnerability.
- **Tags**: [RL, model-based, game-theory, Nash-equilibrium]

### 4.5 CoSkill: Joint RL of Reasoning and Meta-Skill Agents
- **arXiv**: [2609.04865](https://arxiv.org/abs/2609.04865)
- **Date**: 2026-09-04
- **Institution/Company**: Not specified
- **Abstract**: Unified multi-agent RL framework recasting static meta-skill workflow as learnable Meta-Skill Agent, jointly trained with Reasoning Agent over hierarchical skill library. Both share a single backbone for end-to-end co-adaptation. ALFWorld: 98.4% success (+3.5pp); WebShop: 90.6% success (+6.2pp). Superior early-stage sample efficiency and asymptotic performance.
- **Key Innovations**: Learnable Meta-Skill Agent, end-to-end co-adaptation via shared backbone, hierarchical skill library.
- **Tags**: [RL, agents, skill-learning, LLM]

### 4.6 TIGPO: Temporal Instance-Graph Policy Optimization for Long-Horizon LLM Agents
- **arXiv**: [2609.03383](https://arxiv.org/abs/2609.03383)
- **Date**: 2026-09-03
- **Institution/Company**: Not specified
- **Abstract**: Extends graph-based credit assignment across policy updates via persistent transition graph per task. Allocates rollout budget between Exploration and Revisit slots for delayed reattempts. Cross-temporal reference stabilizes advantage estimation under small rollout groups. Outperforms prior group-based and graph-based policy optimization on ALFWorld and WebShop.
- **Key Innovations**: Persistent cross-update transition graph, exploration/revisit budget allocation, cross-temporal advantage estimation.
- **Tags**: [RL, LLM-agents, credit-assignment, policy-optimization]

---

## 5. Summary of Trends

| Trend | Representative Papers |
|-------|----------------------|
| **Generative Recommender in Ads** | TGR, OneRanker, GR4AD, UniVA, GRAB, CADET |
| **Transformer Scaling for CTR** | ReST, EST, UniCon, FAT, GRAB |
| **LLM Agents for Systems** | CORAL, A-MLE |
| **Unified Generation + Ranking** | TGR-GenRank, OneRanker, GR4AD, CADET |
| **Value/Business Alignment** | UniVA, OneRanker, GR4AD (RSPO) |
| **Production Deployments** | All CTR/Ads papers (Meituan, Taobao, Baidu, LinkedIn, Tencent, Kuaishou, Yandex) |
| **Latent Reasoning / CoT** | PMPS, Self-Routing |
| **Game AI + RL** | NashDreamer, LUGL, PlayTrain |
| **LLM + RL Hybrid** | LLM-guided NPC, CoSkill, TIGPO |
| **Feature Transport (beyond Interaction)** | CRAFT |
| **Knowledge Graph + Recommendation** | AdaKG, CGM-Rec |
| **Continual/Adaptive** | CGM-Rec, CORAL |
