---
title: "arXiv AI/LLM/RecSys/Advertising Paper Search (2026-08-20)"
type: synthesis
created: 2026-08-20
updated: 2026-08-20
tags: [arxiv, llm, recommendation, advertising, ctr, sequential-modeling, games, reinforcement-learning]
---

# arXiv Recent Papers — AI, LLM, Recommendation, Advertising, Sequential Modeling, CTR, Games

## 1. Advertising & CTR Prediction

---

### 1.1 GRAB: Generative Ranking for Ads at Baidu

| Field | Detail |
|-------|--------|
| **Title** | GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm |
| **Authors** | Baidu Advertising Team |
| **Institution** | Baidu |
| **arXiv** | https://arxiv.org/abs/2602.01865 |
| **Date** | 2026-02 |

**Abstract:** GRAB is an end-to-end generative framework for CTR prediction inspired by LLM scaling laws. It introduces Causal Action-aware Multi-channel Attention (CamA) to capture temporal dynamics and action signals in user behavior sequences. Deployed in full production at Baidu.

**Key Innovations:**
- CamA mechanism for temporal dynamics + action-specific signals
- STS training paradigm to mitigate distribution shift
- Monotonic scaling: performance improves linearly with longer sequences and larger capacity
- **Online results:** +3.49% CTR, +3.05% CPM (revenue)
- Full production deployment on Baidu home feed

---

### 1.2 Long-History User Transformers for Real-Time Ad Ranking

| Field | Detail |
|-------|--------|
| **Title** | Long-History User Transformers for Real-Time Ad Ranking |
| **Authors** | Vyacheslav Ovchinnikov, G. G. Smirnov, Nikolai Savushkin, Veronika Ivanova, Maksim Kuzin |
| **Institution** | Yandex |
| **arXiv** | https://arxiv.org/abs/2607.14331 |
| **Date** | 2026-07 |

**Abstract:** Decouples history encoding from real-time inference in ad ranking. A high-capacity offline transformer encodes full cross-surface interaction history into cached representations; a lightweight runtime model combines cached embeddings with real-time context.

**Key Innovations:**
- Two-stage architecture: offline transformer (autoregressive pre-trained) + lightweight runtime model
- Dual objective: feedback prediction + next-item prediction
- Recovers 72-80% of full-history runtime transformer quality at fraction of latency
- **Online results:** +2.77% ranking metric (search ads), +2.1% (Yandex Ad Network), +2.26% revenue

---

### 1.3 OneRanker: Unified Generation and Ranking

| Field | Detail |
|-------|--------|
| **Title** | OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation |
| **Authors** | Dekai Sun et al. |
| **Institution** | Tencent |
| **arXiv** | https://arxiv.org/abs/2603.02999 |
| **Date** | 2026-03 |

**Abstract:** Achieves deep integration of generation and ranking in a single model for advertising. Uses task token sequences + causal mask to separate interest coverage and value optimization, with Fake Item Tokens for implicit target awareness during generation.

**Key Innovations:**
- Value-aware multi-task decoupling architecture
- Coarse-to-fine collaborative target awareness (Fake Item Tokens + ranking decoder)
- Key/Value pass-through + Distribution Consistency Constraint Loss
- **Online results (Tencent WeiXin Ads):** GMV Normal +1.34%

---

### 1.4 LLM Retrieval for Stable and Predictable Ad Recommendations

| Field | Detail |
|-------|--------|
| **Title** | LLM Retrieval for Stable and Predictable Ad Recommendations |
| **Authors** | Vinodh Kumar Sunkara, Satheeshkumar Karuppusamy, Heng Xu et al. |
| **Institution** | Amazon (AWS) |
| **arXiv** | https://arxiv.org/abs/2605.21969 |
| **Date** | 2026-05 |

**Abstract:** Introduces a new evaluation framework for quantifying stability and predictability of ads recommender systems. Uses fine-tuned LLMs to extract hierarchical semantic attributes from ad creatives for graph-based candidate expansion.

**Key Innovations:**
- Novel metrics for prediction stability and predictability (not just accuracy/recall)
- LLM-powered hierarchical semantic candidate generation
- **Online results:** +0.45% topline metric, +1.2% retrieval recall, 8.62% reduction in A/A' difference, 45% MAD improvement

---

### 1.5 Fine-Tuned LLM as Complementary Predictor for Ads

| Field | Detail |
|-------|--------|
| **Title** | Fine-Tuned LLM as a Complementary Predictor Improving Ads System |
| **Authors** | (Multiple authors) |
| **Institution** | (Industry — large-scale ads platform) |
| **arXiv** | https://arxiv.org/abs/2605.27856 |
| **Date** | 2026-05 |

**Abstract:** Uses a fine-tuned open-source LLM not as a ranker, but as an ancillary predictor forecasting likely advertisers from user profiles. Predictions feed both early retrieval (advertiser-targeted candidate filtering) and late-stage conversion models as features.

**Key Innovations:**
- Complementary paradigm: LLM as advertiser predictor, not primary ranker
- Dual consumption: retrieval-level targeting + ranking features
- **Online results (US Shopping Ads):** RoAS +4.94% (all), +6.69% (opt-in users)

---

### 1.6 IDProxy: Cold-Start CTR at Xiaohongshu

| Field | Detail |
|-------|--------|
| **Title** | IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs |
| **Authors** | Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan, Ruiyan Han et al. |
| **Institution** | Xiaohongshu (RedNote) |
| **arXiv** | https://arxiv.org/abs/2603.01590 |
| **Date** | 2026-03 |

**Abstract:** Uses multimodal LLMs (InternVL) to generate proxy item embeddings from rich content signals (text + images) for cold-start CTR prediction. Coarse-to-fine alignment mechanism bridges multimodal semantic representations with collaborative ID embedding space.

**Key Innovations:**
- MLLM-based coarse proxy generation + end-to-end alignment stage
- Seamless integration into existing ID-centric CTR models
- **Online results (Content Feed):** Time Spent +0.22%, Reads +0.39%, Engagements +0.5%
- **Online results (Display Ads):** Impression +1.28%, ADVV +1.93%, CTR +0.23%
- Cold-start AUC gains ~2x larger than global traffic

---

### 1.7 LLM-HYPER: Generative CTR via Hypernetworks

| Field | Detail |
|-------|--------|
| **Title** | LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks |
| **Authors** | (Multiple authors) |
| **Institution** | Top US e-commerce platform |
| **arXiv** | https://arxiv.org/abs/2604.12096 |
| **Date** | 2026-04 |

**Abstract:** Treats LLMs as hypernetworks to directly generate CTR estimator parameters in a training-free manner. Uses few-shot Chain-of-Thought prompting over multimodal ad content to infer feature-wise model weights for a linear CTR predictor.

**Key Innovations:**
- Training-free weight generation via LLM prompting
- Decoupled: LLM inference offline, linear serving at low latency (0.14-0.17ms)
- Retrieval of semantically similar past campaigns as few-shot demonstrations
- **Offline results:** +55.9% NDCG@10 vs best cold-start baseline
- **Online A/B:** Competitive with warm-start model (p=0.62), successfully deployed

---

### 1.8 Building a User Foundation Model for the Open Web

| Field | Detail |
|-------|--------|
| **Title** | Building a User Foundation Model for the Open Web |
| **Authors** | (Multiple authors) |
| **Institution** | (Industry RTB platform) |
| **arXiv** | https://arxiv.org/abs/2607.28019 |
| **Date** | 2026-07 |

**Abstract:** Addresses the challenge of user foundation models in RTB where user identity is fragmented and non-persistent. Pre-trains a Transformer encoder with masked LM + contrastive objective on user browsing histories. Uses LLM-in-the-loop search for pipeline optimization.

**Key Innovations:**
- Self-supervised pre-training on fragmented, non-persistent browsing sessions
- LLM-as-optimizer for pipeline optimization (AlphaEvolve-style code-level edits)
- **Online results (7-day A/B):** +2.13% CTR, -1.13% eCPC
- Cross-task generalization: same representation improves bid win-rate (+1.197%) and CTR ranker (+1.354%)

---

## 2. Sequential Recommendation

---

### 2.1 Learning from the Future: Privileged Self-Distillation (PSD)

| Field | Detail |
|-------|--------|
| **Title** | Learning from the Future: Privileged Self-Distillation for Sequential Recommendation |
| **Authors** | (Multiple authors) |
| **Institution** | (Academic) |
| **arXiv** | https://arxiv.org/abs/2607.27055 |
| **Date** | 2026-07 |

**Abstract:** Uses future interactions in logged sequences as training-only privileged information. A single backbone serves dual roles: bidirectional attention mask (teacher) and causal mask (student), with KL distillation.

**Key Innovations:**
- Future-aware privileged teacher + causal student from same backbone (no extra params)
- Advantage-reachability gate to discard unreachable dark knowledge
- Momentum-averaged teacher for stable self-referential supervision
- Consistent gains across SASRec, BERT4Rec, UniSRec

---

### 2.2 CAST: Semantic-Level Transitions for Complementary-Aware SR

| Field | Detail |
|-------|--------|
| **Title** | CAST: Modeling Semantic-Level Transitions for Complementary-Aware Sequential Recommendation |
| **Authors** | Qian Zhang, Lech Szymanski, Haibo Zhang, Jeremiah D. Deng |
| **Institution** | (Academic) |
| **arXiv** | https://arxiv.org/abs/2604.19414 |
| **Date** | 2026-04 |

**Abstract:** Models dynamic transitions directly in discrete semantic code space instead of aggregated item representations, combined with LLM-verified complementary priors injected into self-attention.

**Key Innovations:**
- Semantic-level transition module in discrete code space (via Optimized Product Quantization)
- LLM-verified complementary prior injection into attention
- Up to 17.6% Recall and 16.0% NDCG gains, 65x training acceleration

---

### 2.3 GenAIR: Generative Archetype-Grounded Item Representations

| Field | Detail |
|-------|--------|
| **Title** | Generative Archetype-Grounded Item Representations for Sequential Recommendation |
| **Authors** | (Multiple authors) |
| **Institution** | (Academic) |
| **arXiv** | https://arxiv.org/abs/2606.11023 |
| **Date** | 2026-06 |

**Abstract:** Uses LLMs to generate "archetypes" — conceptual profiles of an item's ideal target audience — from metadata, then grounds these in real interaction patterns via behavioral calibration.

**Key Innovations:**
- Archetype = conceptual representation of target audience (STP framework)
- Single forward pass through LLM for efficient embedding extraction
- Behavioral calibration objective bridges semantic knowledge with behavioral patterns
- Model-agnostic: integrates with GRU4Rec, BERT4Rec, SASRec

---

### 2.4 SRPFN: One Model Pretrained from Synthetic Priors

| Field | Detail |
|-------|--------|
| **Title** | One Sequential Recommendation Model Pretrained from Synthetic Priors Predicts Multiple Datasets |
| **Authors** | (Multiple authors) |
| **Institution** | (Academic, published at KDD '26) |
| **arXiv** | https://arxiv.org/abs/2606.15752 |
| **Date** | 2026-06 |

**Abstract:** A Prior-data Fitted Network for sequential recommendation — predicts next item in a single forward pass without gradient-based updates on target domain. Pretrained on 25.6M synthetic sequences.

**Key Innovations:**
- Update-free: single forward pass, no fine-tuning on target domain
- Synthetic prior based on hierarchical degree-corrected stochastic block model
- Conditions on support set of item-item transitions at inference
- Average +7.53% improvement over second-best method; ~1 minute inference per dataset

---

### 2.5 RecRec: Recursive Reasoning for Sequential Rec

| Field | Detail |
|-------|--------|
| **Title** | RecRec: Latent Interests Recursive Reasoning for Sequential Recommendation |
| **Authors** | Wenhao Deng, Fu J, Hanwen Du, Alexandros Karatzoglou, Ioannis Arapakis et al. |
| **Institution** | (Academic/Industry) |
| **arXiv** | https://arxiv.org/abs/2607.12945 |
| **Date** | 2026-07 |

**Abstract:** Decouples reasoning from prediction in sequential recommendation. Context Compressor distills hidden states into latent interests; Recursive Reasoner refines them in a separate intermediate latent space.

**Key Innovations:**
- Dual-state: reasoning state (scratchpad) separate from prediction latent interests
- Interest Diversity Regularizer for capturing distinct behavior aspects
- Deep supervision allows freely adjusting reasoning depth at inference
- RL-free: trained in two simple supervised stages
- Backbone-agnostic framework

---

### 2.6 RoTE: Coarse-to-Fine Multi-Level Rotary Time Embedding

| Field | Detail |
|-------|--------|
| **Title** | RoTE: Coarse-to-Fine Multi-Level Rotary Time Embedding for Sequential Recommendation |
| **Authors** | Haolin Zhang, Longtao Xiao, Guohao Cai, Ruixuan Li, Xiu Li |
| **Institution** | (Academic, published at SIGIR '26) |
| **arXiv** | https://arxiv.org/abs/2604.13389 |
| **Date** | 2026-04 |

**Abstract:** Decomposes timestamps into year/month/day levels and injects multi-level temporal signals into item embeddings via rotary embedding mechanism. Plug-and-play module.

**Key Innovations:**
- Hierarchical temporal decomposition (year → month → day)
- Rotary embedding mechanism for time-aware signals in attention
- Lightweight, plug-and-play: no backbone modification
- Up to 20.11% NDCG@5 improvement (on RPG baseline, Toys & Games)

---

### 2.7 ACE: Anisotropy-Controllable Embedding for LLM-enhanced SR

| Field | Detail |
|-------|--------|
| **Title** | ACE: Anisotropy-Controllable Embedding for LLM-enhanced Sequential Recommendation |
| **Authors** | Dongcheol Lee, Hye-young Kim, Jongwuk Lee |
| **Institution** | (Academic) |
| **arXiv** | https://arxiv.org/abs/2605.29322 |
| **Date** | 2026-05 |

**Abstract:** Addresses strong anisotropy in LLM-generated embeddings where vectors concentrate in similar directions. Uses a linear autoencoder with L2 regularization to reshape embedding distribution while preserving semantic structure.

**Key Innovations:**
- Linear autoencoder (LAE) to control anisotropy of LLM embeddings
- L2 regularization controls dispersion; reconstruction loss preserves semantics
- Balances geometric uniformity and semantic preservation
- Up to 12.4% Recall@20 and 11.8% NDCG@20 improvements

---

## 3. LLM Agents in Games

---

### 3.1 Strat-Reasoner: Strategic Reasoning in Multi-Agent Games

| Field | Detail |
|-------|--------|
| **Title** | Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games |
| **Authors** | Yidong He, Yutao Lai, Pengxu Yang, Jiarui Gan, Jiexin Wang, Yi Cai et al. |
| **Institution** | (Academic) |
| **arXiv** | https://arxiv.org/abs/2605.04906 |
| **Date** | 2026-05 |

**Abstract:** RL framework for improving LLM strategic reasoning in multi-agent games. Uses recursive reasoning (agent reasoning integrates other agents' reasoning), centralized CoT comparison for reward, and hybrid advantage estimation.

**Key Innovations:**
- Recursive reasoning paradigm: "thinking about what others think"
- Centralized CoT comparison module for fine-grained reasoning reward
- Hybrid advantage estimation (CoT scores + return-based)
- 22.1% average improvement across multi-agent games
- Code: https://github.com/ydhe1012/Strat-Reasoner

---

### 3.2 Odysseus: Scaling VLMs to 100+ Turn Decision-Making

| Field | Detail |
|-------|--------|
| **Title** | Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning |
| **Authors** | Chengshuai Shi, Wenzhe Li, Xinran Liang, Yizhou Lu et al. |
| **Institution** | (Academic/Industry) |
| **arXiv** | https://arxiv.org/abs/2605.00347 |
| **Date** | 2026-05 |

**Abstract:** Studies RL training of VLMs for long-horizon decision-making in Super Mario Land. Proposes adapted PPO with lightweight turn-level critic for stable training over 100+ interaction turns.

**Key Innovations:**
- Adapted PPO with lightweight turn-level critic (outperforms GRPO/Reinforce++)
- Pretrained VLMs provide strong action priors vs training from scratch
- Open training framework combining SFT initialization + multi-task RL
- 3x average game progress vs frontier models
- Generalizes across levels and retains general-domain capabilities

---

### 3.3 CAST: Game Solvers as Turn-Level Teachers

| Field | Detail |
|-------|--------|
| **Title** | CAST: Credit Assignment from Solver Teachers for LLM Game Agents |
| **Authors** | (Multiple authors) |
| **Institution** | (Academic) |
| **arXiv** | https://arxiv.org/abs/2607.25308 |
| **Date** | 2026-07 |

**Abstract:** Uses game solver state-value changes as turn-level credit signals in RLVR. Under soft-optimal solver assumption, maximizing solver advantage is equivalent to on-policy distillation without teacher logits.

**Key Innovations:**
- Solver advantage = turn-level process signal from game solver state values
- Logit-free on-policy distillation: scalar advantage suffices
- 1.7-2.0x fewer training steps to reach DAPO's peak performance
- Zero-shot transfer to ALFWorld and WebShop

---

### 3.4 Hierarchical Control: LLM Planning + RL Execution

| Field | Detail |
|-------|--------|
| **Title** | Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution |
| **Authors** | (Multiple authors) |
| **Institution** | (Academic) |
| **arXiv** | https://arxiv.org/abs/2606.20014 |
| **Date** | 2026-06 |

**Abstract:** LLM (Gemma 3 27B) acts as centralized strategic controller selecting among pretrained RL skill policies in a 2v2 competitive environment. Achieves performance equivalent to hand-crafted behavior trees.

**Key Innovations:**
- Two-layer hierarchy: LLM (slow timescale, strategic) + RL skills (fast, reactive)
- Statistically equivalent to hand-crafted BT (46.4% vs 51.5% win rate, p=0.103)
- 60% of human players perceive LLM+RL agents as most human-like (p=0.027)
- No manual rule engineering required

---

### 3.5 From Player to Master: MEMOPILOT

| Field | Detail |
|-------|--------|
| **Title** | From Player to Master: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory |
| **Authors** | Yishuo Cai, Xingyu Guo, Xuancheng Huang et al. |
| **Institution** | (Academic) |
| **arXiv** | https://arxiv.org/abs/2606.08656 |
| **Date** | 2026-06 |

**Abstract:** Treats memory updating as a trainable multi-turn decision process optimized via multi-turn GRPO. Turn-wise rewards and turn-level advantage estimation enable stable credit assignment.

**Key Innovations:**
- Memory update as trainable decision process (not hand-designed prompts)
- Multi-turn GRPO with turn-wise rewards
- Ranks #1 in Elo on both Rock-Paper-Scissors (1590) and Limit Texas Hold'em (1762)
- Outperforms DeepSeek V3.2 and all baseline memory methods
- Generalizes to unseen opponents and larger models

---

### 3.6 MEMO: Memory-Augmented Model Context Optimization

| Field | Detail |
|-------|--------|
| **Title** | MEMO: Memory-Augmented Model Context Optimization for Robust Multi-Turn Multi-Agent LLM Games |
| **Authors** | (Multiple authors) |
| **Institution** | (Academic) |
| **arXiv** | https://arxiv.org/abs/2603.09022 |
| **Date** | 2026-03 |

**Abstract:** Self-play framework optimizing inference-time context without weight updates. Couples exploration (tournament-style prompt evolution via TrueSkill) with retention (persistent memory bank with CRUD operations).

**Key Innovations:**
- Persistent memory bank distills self-play trajectories into reusable insights
- Tournament-style prompt evolution + prioritized replay of rare states
- **GPT-4o-mini:** Mean win rate from 25.1% → 49.5%
- **Qwen-2.5-7B:** Mean win rate from 20.9% → 44.3%
- Uses 19x fewer games than RL baselines
- Memory is the dominant mechanism (ablation confirmed)

---

## Summary Table

| # | Paper | Category | Organization | Key Result |
|---|-------|----------|-------------|------------|
| 1 | GRAB | CTR/Ads | Baidu | +3.49% CTR, +3.05% CPM |
| 2 | Long-History Transformers | Ad Ranking | Yandex | +2.77% ranking, +2.26% revenue |
| 3 | OneRanker | Gen+Rank Ads | Tencent | GMV +1.34% |
| 4 | LLM Retrieval | Ad Stability | Amazon | +0.45% metric, 8.62% less variance |
| 5 | Fine-Tuned LLM Predictor | Ads | Industry | RoAS +4.94% |
| 6 | IDProxy | Cold-Start CTR | Xiaohongshu | +1.93% ADVV, deployed |
| 7 | LLM-HYPER | Cold-Start CTR | US E-commerce | +55.9% NDCG@10 offline, deployed |
| 8 | User Foundation Model | RTB/Open Web | Industry | +2.13% CTR, -1.13% eCPC |
| 9 | PSD | Sequential Rec | Academic | Consistent gains, no extra params |
| 10 | CAST (SR) | Sequential Rec | Academic | +17.6% Recall, 65x speedup |
| 11 | GenAIR | Sequential Rec | Academic | Model-agnostic, LLM archetypes |
| 12 | SRPFN | Sequential Rec | Academic (KDD) | +7.53%, update-free |
| 13 | RecRec | Sequential Rec | Academic | RL-free recursive reasoning |
| 14 | RoTE | Sequential Rec | Academic (SIGIR) | +20.11% NDCG@5, plug-and-play |
| 15 | ACE | Sequential Rec | Academic | +12.4% Recall@20 |
| 16 | Strat-Reasoner | LLM Games | Academic | +22.1% in multi-agent games |
| 17 | Odysseus | VLM Games | Academic | 3x game progress vs frontier |
| 18 | CAST (Games) | LLM Games | Academic | 1.7-2x faster training |
| 19 | Hierarchical LLM+RL | Multi-Agent Games | Academic | Matches BT, 60% human-like |
| 20 | MEMOPILOT | LLM Games | Academic | #1 Elo in RPS & LHE |
| 21 | MEMO | LLM Games | Academic | 25% → 49.5% win rate |
