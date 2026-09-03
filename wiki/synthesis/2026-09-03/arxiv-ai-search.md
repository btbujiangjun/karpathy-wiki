---
title: "arXiv AI Search — 2026-09-03"
type: synthesis
created: 2026-09-03
updated: 2026-09-03
tags: [arxiv, ai, llm, ctr, recommendation, advertising, sequential-modeling, games, reinforcement-learning]
---

# arXiv AI Search — 2026-09-03

Daily scan covering recent papers on AI, LLMs, CTR prediction, recommendation, advertising, sequential modeling, and game AI.

---

## 1. LLMs & AI General

### REER-PT: Reverse-Engineered Reasoning for Perplexity-Guided Pre-training Data Augmentation

| Field | Detail |
|-------|--------|
| **Authors** | Haoran Que et al. |
| **Affiliation** | Not specified |
| **Date** | 2026-08-31 |
| **arXiv** | [2608.30627](https://arxiv.org/abs/2608.30627) |
| **Subject** | cs.CL |

**Abstract:** REER-PT extends Reverse-Engineered Reasoning (REER) to raw pre-training data. It identifies continuations that are difficult to predict but inferable from context, then inserts concise reasoning annotations to reconstruct the missing connection. Perplexity serves as the optimization signal. Augmented models gain up to 2.07 pp on knowledge and reasoning benchmarks.

**Key Innovations:**
- Sparse reasoning annotation that preserves original text
- Perplexity-driven offline generation and refinement
- Compatible with standard next-token pre-training

---

### LoGo: Token-Level Dynamic Local-Global Attention

| Field | Detail |
|-------|--------|
| **Authors** | Yuqi Pan et al. |
| **Affiliation** | Not specified |
| **Date** | 2026-08-30 |
| **arXiv** | [2608.29539](https://arxiv.org/abs/2608.29539) |
| **Subject** | cs.CL, cs.LG |

**Abstract:** As context lengths scale, attention becomes a bottleneck. LoGo proposes a token-level dynamic local-global attention mechanism where each layer has coupled local and global branches. A learned gate activates global attention only for tokens requiring long-range information. A threshold-based budget controller maintains target global ratio without auxiliary losses.

**Key Innovations:**
- Token-level dynamic attention span allocation
- Query-sparse Triton kernels for practical speedups
- Progressive masking schedule for stable training
- Interpretable span allocation patterns

---

### EVAR: Evidence-Validated Hypothesis Admission for Budget-Aware Narrative Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Peilin Liu et al. |
| **Affiliation** | Not specified |
| **Date** | 2026-08-30 |
| **arXiv** | [2608.29835](https://arxiv.org/abs/2608.29835) |
| **Subject** | cs.CL (Accepted at EMNLP 2026) |

**Abstract:** Addresses unsupported intermediate hypotheses contaminating LLM reasoning over long narratives. EVAR compiles narratives into immutable evidence stores, assigns instance-specific inference budgets, and verifies each candidate hypothesis against the locked store before admission.

**Key Innovations:**
- Evidence-validated hypothesis admission framework
- Sufficiency-based stopping mechanism
- Budget-aware inference cost control

---

### LLMpedia: Browsing, Verifying, and Comparing the Parametric Encyclopedic Knowledge of LLMs

| Field | Detail |
|-------|--------|
| **Authors** | M. Saeed, S. Razniewski |
| **Affiliation** | Not specified |
| **Date** | 2026-09 |
| **arXiv** | [2609.01182](https://arxiv.org/abs/2609.01182) |
| **Subject** | cs.CL |
| **Live** | [llmpedia.net](https://llmpedia.net) |

**Abstract:** Materialized ~1.3M articles from three model families' parametric memory (GPT-5-mini, DeepSeek-V3.2, Llama-3.3-70B) without retrieval. Audited a stratified sample of atomic claims against Wikipedia. True rate is 68.4%, 21pp below MMLU. 30.5% of claims insufficient (long-tail or plausible hallucination).

**Key Innovations:**
- First browsable CC-BY-4.0 encyclopedia from pure parametric memory
- Per-article cross-model and political-persona comparison
- Demonstrates that silence (unverifiability), not error, is the dominant failure mode

---

### Graph Evidence Is Not Enough: Diagnosing Native Decoder Use in Graph-Augmented LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Affiliation** | Not specified |
| **Date** | 2026-08-31 |
| **arXiv** | [2608.30437](https://arxiv.org/abs/2608.30437) |
| **Subject** | cs.CL |

**Abstract:** Tests whether graph evidence in input can be used by native decoders using HopQA diagnostic. Proposes an intervention triangle separating evidence inclusion, structural readability, and decoder-usable topology. S2GE achieves strict EM of 36.5–76.6% across four domains, +53.5pp average improvement.

**Key Innovations:**
- Intervention triangle diagnostic framework
- Query-aware sampling with structure-preserving alignment
- Identifies harmful-shuffle, shuffle-robust, and no-graph-saturated regimes

---

## 2. CTR Prediction & Feature Interaction

### GRAB: An LLM-Inspired Sequence-First CTR Prediction Modeling Paradigm

| Field | Detail |
|-------|--------|
| **Authors** | Shaopeng Chen, Chuyue Xie, Huimin Ren et al. |
| **Affiliation** | Baidu |
| **Date** | 2026-02 |
| **arXiv** | [2602.01865](https://arxiv.org/abs/2602.01865) |

**Abstract:** End-to-end generative framework for CTR prediction inspired by LLM scaling. Integrates Causal Action-aware Multi-channel Attention (CamA) to capture temporal dynamics and specific action signals. Online deployment: +3.05% revenue, +3.49% CTR. Model shows monotonic AUC improvement with longer sequences without saturation.

**Key Innovations:**
- CamA mechanism for temporal + action-specific signals
- Sequence-Then-Sparse (STS) training to resolve distribution skew
- Bridges DLRM sparse features with generative sequential modeling
- Demonstrates LLM-style scaling behavior in CTR

---

### DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Affiliation** | Major social-media platform |
| **Date** | 2026-06 |
| **arXiv** | [2606.07980](https://arxiv.org/abs/2606.07980) |

**Abstract:** Addresses residual connection bottleneck in CTR Transformers. DeRes routes each layer through Identity residual path + Block Attention Residual path. Pointwise AttnRes replaces Softmax with SiLU for parallel multi-interest patterns. Fits steeper compute-AUC scaling law (γ=0.118 vs 0.071 for OneTrans), achieving ~2x compute saving at equivalent AUC.

**Key Innovations:**
- Dual-path inter-layer connector (Identity + cross-layer attention)
- Pointwise SiLU attention (enables simultaneous activation + negative forgetting weights)
- Steeper compute-AUC scaling law than existing approaches
- 8-layer DeRes matches 16-layer OneTrans performance

---

### Dual-Stream MLP is All You Need for CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Kesha Ou, Zhen Tian, Wayne Xin Zhao et al. |
| **Affiliation** | Renmin University, ByteDance, Meituan |
| **Date** | 2026-06 |
| **arXiv** | [2606.04944](https://arxiv.org/abs/2606.04944) |
| **Published** | ACM TKDD 2026 |

**Abstract:** Proposes DS-MLP: a dual-stream MLP framework that distills explicit high-order feature interactions from teacher networks while using a parallel MLP for implicit interactions. Aligns hidden states and predictions across streams. Consistently outperforms baselines on Criteo, Avazu, MovieLens with low inference latency.

**Key Innovations:**
- Distillation → alignment → overall optimization pipeline
- Dual MLP streams for explicit vs implicit interactions
- Scalable with low latency suitable for production

---

### PRECTR-V2: Unified Relevance-CTR Framework with Cross-User Preference Mining

| Field | Detail |
|-------|--------|
| **Authors** | Shuzhi Cao, Rong Chen, Ailong He et al. |
| **Affiliation** | Xianyu (Alibaba) |
| **Date** | 2026-02 |
| **arXiv** | [2602.20676](https://arxiv.org/abs/2602.20676) |

**Abstract:** Enhances PRECTR for unified search relevance + CTR. Addresses low-activity user cold-start via cross-user relevance preference mining, exposure bias via hard negative construction, and representation misalignment via LLM-distilled lightweight encoder (2M params replacing frozen BERT). Deployed at Xianyu: +1.39% per capita orders, +3.18% GMV.

**Key Innovations:**
- Cross-user relevance preference mining for cold start
- Embedding noise injection for exposure bias correction
- LLM-distilled lightweight Transformer encoder (2M vs 110M BERT params)

---

### EST: Towards Efficient Scaling Laws in CTR Prediction via Unified Modeling

| Field | Detail |
|-------|--------|
| **Authors** | Mingyang Liu, Yong Bai, Zhangming Chan et al. |
| **Affiliation** | Alibaba (Taobao) |
| **Date** | 2026-02 |
| **arXiv** | [2602.10811](https://arxiv.org/abs/2602.10811) |

**Abstract:** Achieves fully unified modeling by processing all raw inputs in a single sequence without lossy aggregation. Integrates Lightweight Cross Attention (LCA) and Content Sparse Attention (CSA). Exhibits stable power-law scaling. Deployed at Taobao display ads: +3.27% RPM, +1.22% CTR.

**Key Innovations:**
- Fully unified modeling without information bottleneck
- LCA prunes redundant self-interactions
- CSA uses content similarity for dynamic behavior selection
- Stable power-law scaling relationship demonstrated

---

## 3. Recommendation Systems

### GenRec: An LLM-Backed Recommendation Ranker at Netflix

| Field | Detail |
|-------|--------|
| **Authors** | Netflix team |
| **Affiliation** | Netflix |
| **Date** | 2026-08 |
| **arXiv** | [2608.10257](https://arxiv.org/abs/2608.10257) |

**Abstract:** LLM-backed ranker built on internal foundation LLM. Two-phase: Phase 1 adapts LLM to Netflix data; Phase 2 post-trains with recommendation-specific data/labels/rewards. Uses prefill-only inference (single forward pass for full candidate set). Trained with 40x fewer Phase-2 labels than production model, achieves +1.6% relative MRR offline.

**Key Innovations:**
- Prefill-only inference avoids autoregressive decode cost
- Catalog-aware ranking head
- Verbalized user histories replacing engineered features
- From feature engineering to context engineering paradigm shift

---

### SCoRD: Semantic-Assisted Continual Retriever-Reranker Distillation for LLM-Based Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Affiliation** | Not specified |
| **Date** | 2026-08 |
| **arXiv** | [2608.19998](https://arxiv.org/abs/2608.19998) |
| **Published** | CIKM 2026 |

**Abstract:** Continual knowledge distillation framework for LLM-based reranking pipelines under non-stationary data streams. Introduces a semantic reasoning assistant that distills LLM's intent inference into reusable guidance. Selectively distills on low-confidence sequences, guides retriever-only updates without repeated LLM inference.

**Key Innovations:**
- Semantic reasoning assistant for reusable intent-level guidance
- Selective distillation (only low-confidence sequences)
- Asynchronous retriever-reranker co-adaptation

---

### GALLM: Making Collaborative Signals Count — Graph-Aware Large Language Models for Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Affiliation** | Not specified |
| **Date** | 2026-08 |
| **arXiv** | [2608.12184](https://arxiv.org/abs/2608.12184) |

**Abstract:** Constructs a collaborative graph over text tokens and item tokens modeling three relation types. Relations transformed into lightweight learnable attention biases injected into LLM attention. Average improvement of 9.76% in HR@5 over strongest baseline.

**Key Innovations:**
- Token-level collaborative graph with three heterogeneous relations
- Attention bias injection (no external graph encoder needed)
- Joint semantic + collaborative signal modeling in LLM

---

### IntuRec: Intuition-Guided Latent Reasoning for LLM-Based Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Affiliation** | Not specified |
| **Date** | 2026-06 |
| **arXiv** | [2606.27684](https://arxiv.org/abs/2606.27684) |
| **Published** | KDD 2026 |

**Abstract:** Two-stage framework inspired by cognitive neuroscience. Extraction stage generates top-K candidates as intuition source; injection stage encodes candidates into preference-aligned intuition embedding to initialize latent reasoning. Addresses unconstrained reasoning trajectory problem.

**Key Innovations:**
- Recommendation intuition as latent prior for reasoning
- Self + cross-attention for intuition embedding construction
- Semantically grounded reasoning start point

---

### KnowSA: Filling the Gaps — Selective Knowledge Augmentation for LLM Recommenders

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Affiliation** | Not specified |
| **Date** | 2026-04 |
| **arXiv** | [2604.07825](https://arxiv.org/abs/2604.07825) |
| **Published** | SIGIR 2026 |

**Abstract:** Addresses item-level knowledge gaps in LLM-based recommendation. Comparative Knowledge Probing (CKP) estimates LLM's internal knowledge by evaluating its capability to capture collaborative relationships. Selectively injects additional information only where most needed.

**Key Innovations:**
- CKP: knowledge scoring in comparative/collaborative setting
- Selective augmentation focusing on knowledge-poor items
- No fine-tuning required

---

### CoRRe: Training-Free LLM-Based Recommendation with Post-LLM Item Refinement

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Affiliation** | Not specified |
| **Date** | 2026-08 |
| **arXiv** | [2608.19665](https://arxiv.org/abs/2608.19665) |
| **Published** | CIKM 2026 |

**Abstract:** Injects collaborative signals into LLM-generated item representations in a post-LLM manner. Direction refinement via item-item co-purchase graph, magnitude refinement via item popularity. No model training required. Outperforms training-free baselines and achieves competitive performance with training-based methods.

**Key Innovations:**
- Post-LLM collaborative signal injection
- Direction + magnitude dual refinement
- Fully training-free framework

---

### Ask to Be Sure: Informative Interactions for Confident Multi-Turn LLM Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Affiliation** | Not specified |
| **Date** | 2026-08 |
| **arXiv** | [2608.15949](https://arxiv.org/abs/2608.15949) |
| **Published** | CIKM 2026 |

**Abstract:** Quantifies interaction effectiveness via entropy reduction over recommendations. Uses entropy reduction as reward for SFT and DPO fine-tuning without ground-truth labels. Improves both recommendation quality and conversational efficiency.

**Key Innovations:**
- Entropy reduction as interaction quality metric
- No ground-truth label required for reward computation
- SFT + DPO training for strategic interaction generation

---

## 4. Advertising & Auto-Bidding

### CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer

| Field | Detail |
|-------|--------|
| **Authors** | David Pardoe, Neil Daftary, Miro Furtado et al. |
| **Affiliation** | LinkedIn |
| **Date** | 2026-02 |
| **arXiv** | [2602.11410](https://arxiv.org/abs/2602.11410) |

**Abstract:** End-to-end decoder-only transformer for ads CTR at LinkedIn. Resolves chicken-and-egg problem between CTR prediction and post-scoring signals (ad position) via context-conditioned multi-tower heads. Self-gated attention stabilizes training. Timestamp-based RoPE captures temporal relationships across timescales. **+11.04% CTR lift** over production LiRank baseline.

**Key Innovations:**
- Context-conditioned multi-tower prediction heads
- Self-gated attention for training stability
- Timestamp-based RoPE (seconds to months)
- Session masking for offline-online consistency
- Custom FlashAttention kernels for production serving

---

### Long-History User Transformers for Real-Time Ad Ranking

| Field | Detail |
|-------|--------|
| **Authors** | Vyacheslav Ovchinnikov, G. Smirnov, N. Savushkin et al. |
| **Affiliation** | Yandex |
| **Date** | 2026-07 |
| **arXiv** | [2607.14331](https://arxiv.org/abs/2607.14331) |

**Abstract:** Decouples history encoding from real-time inference. Large offline transformer encodes full cross-surface history into cached representation; lightweight runtime model combines cached representation with recent events. Recovers 72–80% of full-history quality. Online: +2.77% search ads, +2.1% YAN ranking metric.

**Key Innovations:**
- Offline/online split for deployable long-history modeling
- Dual-objective autoregressive pre-training (feedback + next-item)
- Robust cached representation with inexpensive refresh

---

### Constrained Auto-Bidding via Generative Response Modeling (GRM)

| Field | Detail |
|-------|--------|
| **Authors** | Eunseok Yang, Xingdong Zuo, Kyung-Min Kim |
| **Affiliation** | Not specified |
| **Date** | 2026-05 |
| **arXiv** | [2605.27811](https://arxiv.org/abs/2605.27811) |
| **Published** | KDD 2026 |

**Abstract:** Shifts learning target from actions to responses. GRM predicts horizon-aggregate cost/value curves as functions of a single bid multiplier. Lightweight analytic controller enforces constraints via 1D root-finding. Outperforms best baseline by 7.8% on AuctionNet. Degrades less under distribution shift.

**Key Innovations:**
- Response curve prediction instead of action prediction
- Exact controller for single-multiplier via root-finding
- Bound: violations scale linearly with prediction error
- Efficiency dispersion bounds the single-multiplier gap

---

### LBM: Hierarchical Large auto-Bidding Model via Reasoning and Acting

| Field | Detail |
|-------|--------|
| **Authors** | Yewen Li, Zhiyi Lyu, Peng Jiang et al. |
| **Affiliation** | Not specified |
| **Date** | 2026-03 |
| **arXiv** | [2603.05134](https://arxiv.org/abs/2603.05134) |

**Abstract:** Hierarchical LLM-based auto-bidding: LBM-Think for high-level reasoning, LBM-Act for precise action generation. Dual embedding mechanism fuses language and numerical modalities. GQPO (Group relative-Q Policy Optimization) for offline reinforcement fine-tuning without simulation/real-world rollout.

**Key Innovations:**
- Hierarchical Think-Act architecture for bidding
- Dual embedding for language + numerical fusion
- GQPO: offline RL fine-tuning reducing LLM hallucinations
- LBM-Think generates CoT asynchronously ahead of decision timestep

---

### Practice on Long Behavior Sequence Modeling in Tencent Advertising

| Field | Detail |
|-------|--------|
| **Authors** | Hu Xian, Yue Ming, Feng Zhixiang et al. |
| **Affiliation** | Tencent |
| **Date** | 2025-09 (recent practice) |
| **arXiv** | [2510.21714](https://arxiv.org/abs/2510.21714) |

**Abstract:** Cross-domain unified commercial behavior trajectories for long-sequence advertising. Hierarchical hard search + decoupled soft search for retrieval. Decoupled Side Info TIN for inter-field conflicts. Target-Decoupled SASRec for target-wise interference. Stacked TIN for high-order correlations. Online: +4.22% GMV WeChat Channels, +1.96% GMV WeChat Moments.

**Key Innovations:**
- Cross-domain/scenario unified behavior trajectories
- Decoupled Side Info TIN (multiple TINs with separated feature fields)
- Target Decoupled Position Encoding + SASRec
- Stacked TIN for high-order (up to 4th order) interactions
- GPU acceleration engineering (multi-stream, Key-Collection)

---

## 5. Games & Reinforcement Learning

### CAST: Game Solvers as Turn-Level Teachers for LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Affiliation** | Not specified |
| **Date** | 2026-07 |
| **arXiv** | [2607.25308](https://arxiv.org/abs/2607.25308) |

**Abstract:** Converts solver state value changes into turn-level signals for RLVR. Proves that maximizing solver advantage is equivalent to on-policy distillation from solver, requiring only scalar values. Outperforms baselines on Sokoban, Minesweeper, Rush Hour. Zero-shot transfers to ALFWorld and WebShop. Reaches DAPO peak in 1.7–2.0x fewer steps.

**Key Innovations:**
- Logit-free on-policy distillation via scalar solver advantage
- Turn-level credit assignment for game RL
- Negligible solver overhead
- Learned value network retains much benefit of exact solver

---

### Continual Harness: Online Adaptation for Self-Improving Foundation Agents

| Field | Detail |
|-------|--------|
| **Authors** | Seth Karten et al. |
| **Affiliation** | Princeton |
| **Date** | 2026-08 |
| **arXiv** | [2605.09998](https://arxiv.org/abs/2605.09998) |
| **Website** | [sethkarten.ai/continual-harness](https://sethkarten.ai/continual-harness) |

**Abstract:** First AI to complete Pokémon Blue, Yellow (hard mode), and Crystal without a lost battle. Reset-free self-improving harness for embodied agents. Agent alternates between acting and refining its own prompt, sub-agents, skills, and memory. Online process-reward co-learning loop with frontier teacher relabeling.

**Key Innovations:**
- Reset-free online harness refinement (no episode resets)
- Model-harness co-learning pipeline
- CRUD edits to prompt/sub-agents/skills/memory during play
- Gemini frontier teacher relabeling for open-source model improvement

---

### Augmenting Game AI with Deep Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Alessandro Sestini, Joakim Bergdahl et al. |
| **Affiliation** | EA (Electronic Arts) |
| **Date** | 2026-06 |
| **arXiv** | [2606.20210](https://arxiv.org/abs/2606.20210) |

**Abstract:** Framework for deploying RL in AAA game production (EA SPORTS FC 25 goalkeeper AI, Battlefield 6 infantry). SAC with offline data + scenario-based training reduces training from 4 days to 12 hours. 300K-param MLP with 170µs inference time. Identifies key production constraints: authenticity, short training, modularity, bug fixing, runtime constraints.

**Key Innovations:**
- Production-ready RL framework for AAA games
- High update-to-data ratio with network resets
- Overnight training capability
- Modular integration into existing game AI pipelines

---

### LDM-v0: Towards Scalable Multi-Task Reinforcement Learning with Large Decision Models

| Field | Detail |
|-------|--------|
| **Authors** | Thibaut Kulak |
| **Affiliation** | Not specified |
| **Date** | 2026-06 |
| **arXiv** | [2606.24962](https://arxiv.org/abs/2606.24962) |

**Abstract:** Single transformer policy trained offline on trajectories from thousands of heterogeneous RL environments. LDM-v0 matches independently trained task-specific reference policies on ~1,000 environments spanning robotics, autonomous driving, inventory management, cybersecurity, trading, and video games.

**Key Innovations:**
- Single pretrained model across thousands of diverse environments
- Multi-task, multi-modal transformer policy
- Supervised next-action prediction over offline trajectories
- Demonstrates feasibility of cross-domain offline RL pretraining

---

### FreshPER: Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Weiyu Ma, Yongcheng Zeng et al. |
| **Affiliation** | Not specified |
| **Date** | 2026-04 |
| **arXiv** | [2604.16918](https://arxiv.org/abs/2604.16918) |

**Abstract:** First successful application of Prioritized Experience Replay to LLM/VLM RL. Addresses priority staleness via exponential age decay grounded in effective sample size analysis. +46% on NQ Search, +367% on Sokoban, +133% on VLM FrozenLake vs on-policy baselines. Standard PER without age decay consistently degrades.

**Key Innovations:**
- Exponential age decay for PER priority staleness
- Effective sample size analysis as theoretical grounding
- First successful PER application to LLM/VLM RL

---

### AHEAD: Adaptive Hindsight with Environment-Augmented Distillation for Agentic RL

| Field | Detail |
|-------|--------|
| **Authors** | Not specified |
| **Affiliation** | Not specified |
| **Date** | 2026-08 |
| **arXiv** | [2608.24114](https://arxiv.org/abs/2608.24114) |

**Abstract:** Step-aware framework for multi-turn agentic RL. Injects environment feedback on all steps + LLM-generated corrective hints on error steps. Successful trajectories bypass PI pipeline. +13.3 points on ALFWorld, +11.0 on WebShop at 7B over GRPO. Minimal changes to standard GRPO.

**Key Innovations:**
- Heterogeneous privileged information (environment feedback + corrective hints) by step type
- Step-aware supervision allocation
- Lightweight: minimal changes to standard GRPO
- No PI/LLM calls at inference time

---

## Summary of Trends

| Trend | Key Signals |
|-------|------------|
| **LLM scaling for CTR** | GRAB, EST, CADET all demonstrate LLM-style scaling laws in CTR; sequence-first architectures replacing DLRM |
| **Offline/online split** | Yandex and LinkedIn decouple heavy long-history encoding from real-time serving |
| **LLM-backed ranking** | Netflix GenRec, Xianyu PRECTR-V2 push LLM-native recommendation into production |
| **Graph + LLM fusion** | GALLM, SCoRD inject collaborative signals into LLMs via attention biases or distillation |
| **Selective augmentation** | KnowSA, CoRRe selectively inject knowledge where LLMs are weakest |
| **Agentic RL** | CAST, AHEAD, FreshPER, Continual Harness address credit assignment and sample efficiency for multi-turn agents |
| **Game AI production** | EA deploys RL in AAA games; LDM-v0 shows cross-domain RL transfer |
| **Auto-bidding with LLMs** | LBM uses LLM reasoning for bidding strategy; GRM shifts from action to response prediction |
