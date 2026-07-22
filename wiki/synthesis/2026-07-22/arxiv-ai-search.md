---
title: "arXiv AI Research Digest — 2026-07-22"
type: synthesis
created: 2026-07-22
updated: 2026-07-22
sources: []
tags: [arxiv, ai, llm, recommendation, ctr, sequential-modeling, game-ai, reinforcement-learning, survey]
---

# arXiv AI Research Digest — 2026-07-22

> Automated search across arXiv for recent papers in AI, LLMs, recommendation systems, advertising, sequential modeling, CTR prediction, and game AI.

---

## 1. LLMs & Foundation Models

### 1.1 Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models
- **Authors**: Patrik Wolf et al.
- **Institution/Company**: (Not specified in abstract)
- **Date**: 2026-07-16
- **Abstract**: Investigates whether LLM in-context learning adheres to basic probabilistic identities, specifically the law of total probability. Using binary trees as evaluation scaffolds, the authors recursively partition populations and aggregate LLM estimates across granularity levels. Finds widespread violations of self-consistency, but discovers the "macro fallacy" — fine-grained subpopulation estimates often align better with human reference data than direct population-level estimates.
- **Key Innovations**: Defines statistical self-consistency as a reference-free LLM evaluation criterion; reveals the macro fallacy pattern.
- **Link**: https://arxiv.org/abs/2607.15277

### 1.2 In-Place Tokenizer Expansion for Pre-trained LLMs
- **Authors**: Jimmy Smith et al.
- **Institution/Company**: (Not specified)
- **Date**: 2026-07-16
- **Abstract**: Presents a recipe for upgrading a pre-trained model's tokenizer in-place by continuing BPE merges on a multilingual corpus. New embeddings are initialized as mean of source sub-token embeddings. Applied to LFM2-8B-A1B, producing LFM2.5-8B-A1B with a 128K tokenizer. Achieves ~2.4–2.6x fewer tokens for Hindi/Vietnamese, up to 4x for Thai.
- **Key Innovations**: In-place tokenizer expansion without retraining from scratch; mean initialization of new token embeddings.
- **Link**: https://arxiv.org/abs/2607.15232

### 1.3 MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning
- **Authors**: Ruilin Tong et al.
- **Institution/Company**: (Not specified)
- **Date**: 2026-07-08
- **Abstract**: Proposes a framework that dynamically expands step-wise memory with asymmetric pairs of sub-goal embeddings and sub-instructions. A coarse-to-fine retrieval mechanism collects supervision for training selection heads from confident samples, while learned selection heads rerank candidates for uncertain samples. Consistently matches or outperforms prior methods.
- **Key Innovations**: Modular memory units with asymmetric sub-goal/sub-instruction pairs; correctness-optimized memory composition for test-time settings.
- **Link**: https://arxiv.org/abs/2607.06974

### 1.4 Belief-Reality Separation in Language Models
- **Authors**: Oliver Steele et al.
- **Institution/Company**: (Not specified)
- **Date**: 2026-07-11
- **Abstract**: Shows that the separation between character beliefs and reality in LLMs rests on two mechanisms: a generic value slot binding attributed values, and a router at the query position selecting which frame to read. Two routes fill the slot — asserted beliefs (directly from text) and derived beliefs (via visibility-gated lookback). Holds across three architectures and emerges between 3B–7B parameters.
- **Key Innovations**: Identifies the computational mechanism for belief-reality separation in LLMs; slot-and-router architecture for non-actual contexts.
- **Link**: https://arxiv.org/abs/2607.11945

### 1.5 Visual Pretraining for Language Intelligence
- **Authors**: Yiming Zhang, Zhonghan Zhao, Wenwei Zhang et al.
- **Institution/Company**: Shanghai AI Laboratory, USTC, Zhejiang University, SJTU
- **Date**: 2026-07-13
- **Abstract**: Challenges the default text-only pretraining assumption by showing that Visual Pretraining (VP) on raw documents consistently outperforms text-only pretraining on scientific reasoning. VP uses only 25% of the token budget while improving cross-modal alignment, without any image-text pair supervision.
- **Key Innovations**: Autoregressive visual pretraining on document patches in latent space; efficient alternative to text-only pretraining at 25% token budget.
- **Link**: https://arxiv.org/abs/2607.09657

### 1.6 LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget
- **Authors**: Changhai Zhou et al.
- **Institution/Company**: (Not specified)
- **Date**: 2026-07-16
- **Abstract**: An architecture-aware execution stack for million-token RL post-training using GRPO. Evaluates shared prompts without autograd, replays short response branches one at a time. Achieves 2.1M positions on 8 H20 GPUs and reaches 4.46M positions in stress tests.
- **Key Innovations**: Decouples prompt evaluation from autograd for efficiency; achieves 2M+ token RL training on fixed GPU budgets.
- **Link**: https://arxiv.org/abs/2607.14952

---

## 2. Recommendation Systems

### 2.1 LBR: Length Bias Reduction for LLM-based Recommendation
- **Authors**: Li-Wei Pan et al.
- **Institution/Company**: (Hangzhou-based)
- **Date**: 2026
- **Abstract**: Identifies length bias as a fundamental issue in LLM-based recommendation — longer item descriptions receive disproportionately large attention. Proposes LBR with Length-Aware Attention Calibration (neutralizes attention skew) and Effective Information Length Normalization (uses prefix-tree branching factors for scoring). Achieves average 16.82% NDCG@5 improvement.
- **Key Innovations**: Information-theoretic length normalization based on trie branching factors; lightweight model-agnostic debiasing framework.
- **Link**: https://arxiv.org/abs/2607.04270

### 2.2 UniRec: Bridging Generative and Discriminative Recommendation via Chain-of-Attribute
- **Authors**: (Shopee team)
- **Institution/Company**: Shopee
- **Date**: 2026
- **Abstract**: Formalizes via Bayes' theorem that a generative model with full feature access matches its discriminative counterpart. Introduces Chain-of-Attribute (CoA) — prefixes SID sequences with attribute tokens (category, seller, brand). Achieves +22.6% HR@50 offline and +5.37% PVCTR, +4.76% orders, +5.60% GMV in online A/B on Shopee.
- **Key Innovations**: CoA speculate-then-refine paradigm; Capacity-constrained SID for exposure-weighted residual quantization; Conditional Decoding Context for multi-scenario stability.
- **Link**: https://arxiv.org/abs/2604.12234

### 2.3 SIDReasoner: Reasoning over Semantic IDs for Generative Recommendation
- **Authors**: Yingzhi He, Yan Sun et al.
- **Institution/Company**: (Not specified)
- **Date**: 2026-03
- **Abstract**: A two-stage framework that strengthens SID-language alignment via multi-task training on enriched SID-centered corpus, then uses GRPO for outcome-driven RL. Enables effective reasoning over itemic tokens even at academic-scale datasets. Shows strong cross-domain generalization and improved interpretability.
- **Key Innovations**: Teacher-assisted semantic expansion for SID-language alignment; outcome-driven RL for SID reasoning without large-scale reasoning traces.
- **Link**: https://arxiv.org/abs/2603.23183

### 2.4 R3-REC: Reasoning-Driven Recommendation via Retrieval-Augmented LLMs
- **Authors**: (Not specified in detail)
- **Institution/Company**: (Not specified)
- **Date**: 2026-03
- **Abstract**: Unifies Multi-level User Intent Reasoning, Item Semantic Extraction, Long-Short Interest Polarity Mining, Similar User Collaborative Enhancement, and Reasoning-based Interest Matching. Achieves +10.2% HR@1 on Bundle and +9.9% HR@1 on Games datasets.
- **Key Innovations**: Prompt-centric RAG framework for sequential recommendation; multi-granular interest signals with reasoning-based scoring.
- **Link**: https://arxiv.org/abs/2603.13730

### 2.5 Gryphon: Unified Architecture for Semantic-ID Generation and Item-Level Scoring
- **Authors**: Daria Tikhonovich, Oleg Sorokin et al.
- **Institution/Company**: (Music streaming service)
- **Date**: 2026-06
- **Abstract**: Adds jointly trained item-level scoring alongside SID generation in an encoder-decoder architecture. Re-ranks generated SIDs by resolving to concrete items. Deployed as sole candidate source in 7-day A/B test, replacing 15+ candidate generators and a preranking stage.
- **Key Innovations**: Joint item-level scoring with SID generation; replaces complex candidate generation pipelines in production.
- **Link**: https://arxiv.org/abs/2606.08604

### 2.6 RecRec: Latent Interests Recursive Reasoning for Sequential Recommendation
- **Authors**: (Not specified in detail)
- **Institution/Company**: (Not specified)
- **Date**: 2026-07
- **Abstract**: Decouples reasoning from prediction using a Context Compressor and Recursive Reasoner. Deep supervision allows free adjustment of reasoning depth at inference without retraining. Outperforms state-of-the-art reasoning-enhanced methods with gains extending past training-time depth on 3/4 datasets.
- **Key Innovations**: Dual-state recursive reasoning with decoupled reasoning/prediction; Interest Diversity Regularizer for multi-aspect user modeling.
- **Link**: https://arxiv.org/abs/2607.12945

### 2.7 RecRec: Recursive Refinement for Sequential Recommendation (Lightweight)
- **Authors**: (Not specified)
- **Institution/Company**: (Not specified)
- **Date**: 2026-07
- **Abstract**: A lightweight (3.9M–14M params) model that maintains a compact latent state updated through recursive refinement with evidence-anchored correction. Matches or outperforms LLM-based recommenders with 99% fewer parameters.
- **Key Innovations**: Evidence-anchored correction mechanism to prevent semantic drift; recursive refinement as alternative to deeper architectures.
- **Link**: https://arxiv.org/abs/2607.10541

### 2.8 GLASS: Generative Recommender for Long-Sequence Modeling
- **Authors**: Shiteng Cao et al.
- **Institution/Company**: (Not specified)
- **Date**: 2026-02
- **Abstract**: Integrates long-term user interests into generative recommendation via SID-Tier (maps long-term interactions to unified interest vector for initial SID prediction) and semantic hard search (uses coarse-grained SID as dynamic keys to extract relevant history). Evaluated on TAOBAO-MM and KuaiRec.
- **Key Innovations**: SID-Tier for initial token prediction from long history; semantic hard search with adaptive gated fusion.
- **Link**: https://arxiv.org/abs/2602.05663

### 2.9 GenAIR: Generative Archetype-Grounded Item Representations
- **Authors**: Yifan Li et al.
- **Institution/Company**: (Not specified)
- **Date**: 2026-04
- **Abstract**: Leverages LLMs to infer archetype descriptions (ideal target audience profiles) for items, then extracts embeddings. Adds behavioral calibration to align semantic space with actual user behavior patterns. Integrates seamlessly with existing sequential models.
- **Key Innovations**: Archetype-based item representations bridging semantic and behavioral spaces; behavioral calibration objective.
- **Link**: https://arxiv.org/abs/2606.11023

### 2.10 CMSL: Constructive Multi-Sequence Learning for Recommendation Systems
- **Authors**: Meta team
- **Institution/Company**: Meta
- **Date**: 2026-07-10
- **Abstract**: Replaces monolithic history modeling with learned context construction, building multiple coherent latent sequences from raw interaction history. Each sequence undergoes self-attention separately, reducing cross-intent interference. Deployed across ranking and retrieval on four major surfaces at Meta.
- **Key Innovations**: Multi-sequence construction module with intent-aware cross-attention; scalable linear attention for multi-sequence modeling.
- **Link**: https://arxiv.org/abs/2606.28533

### 2.11 SRPFN: One Sequential Model Pretrained from Synthetic Priors
- **Authors**: Woosung Kang et al.
- **Institution/Company**: KAIST
- **Date**: 2026-06
- **Abstract**: Pretrains a single model on 25.6M synthetic sequences spanning diverse transition patterns. At inference, adapts to new domains via support set conditioning without any gradient updates. Achieves average 7.53% improvement over second-best method across five benchmarks.
- **Key Innovations**: Prior-data fitted network for zero-shot domain adaptation; hierarchical degree-corrected stochastic block model for synthetic prior generation.
- **Link**: https://arxiv.org/abs/2606.15752

### 2.12 Efficient Sequential Recommendation via Personalization
- **Authors**: (Meta/Facebook Research)
- **Institution/Company**: Meta
- **Date**: 2026-01
- **Abstract**: Compresses long user interaction histories into learnable tokens ("personalized experts"), combined with recent interactions for recommendation. Reduces inference cost by >11% while matching full-sequence performance. Validated on HSTU and HLLM architectures.
- **Key Innovations**: Learnable token compression of historical segments; generalized framework applicable across model architectures.
- **Link**: https://arxiv.org/abs/2601.03479

### 2.13 HyTRec: Hybrid Temporal-Aware Attention for Long Behavior Sequences
- **Authors**: (Not specified)
- **Institution/Company**: (Not specified)
- **Date**: 2026-02
- **Abstract**: Decouples long-term stable preferences from short-term intent spikes using a hybrid attention architecture (predominantly linear with interleaved softmax layers). TADN dynamically upweights fresh behavioral signals. Achieves >8% Hit Rate improvement for ultra-long sequences.
- **Key Innovations**: Temporal-Aware Delta Network (TADN) with exponential gating; hybrid linear/softmax attention at 7:1 ratio.
- **Link**: https://arxiv.org/abs/2602.18283

---

## 3. CTR Prediction & Advertising

### 3.1 GRAB: Generative Ranking for Ads at Baidu
- **Authors**: (Baidu team)
- **Institution/Company**: Baidu
- **Date**: 2026-02
- **Abstract**: An end-to-end generative framework for CTR prediction with Causal Action-aware Multi-channel Attention (CamA) to capture temporal dynamics. Full-scale deployment shows 3.05% revenue increase and 3.49% CTR rise. Demonstrates monotonic, approximately linear scaling with longer interaction sequences.
- **Key Innovations**: CamA mechanism for action-aware temporal modeling; first deployed generative CTR model at Baidu scale.
- **Link**: https://arxiv.org/abs/2602.01865

### 3.2 Long-History User Transformers for Real-Time Ad Ranking
- **Authors**: (Yandex team)
- **Institution/Company**: Yandex
- **Date**: 2026-07-15
- **Abstract**: Decouples history encoding from real-time inference — large offline transformer encodes full cross-surface history asynchronously into cached representation, lightweight runtime model combines with fresh events. Recovers 72–80% of full-history quality. Online A/B shows +2.77% primary metric on search ads, +2.1% on YAN.
- **Key Innovations**: Offline/online split architecture for latency-constrained ad ranking; autoregressive pre-training with dual objective.
- **Link**: https://arxiv.org/abs/2607.14331

### 3.3 CADET: Context-Conditioned Ads CTR Prediction at LinkedIn
- **Authors**: David Pardoe, Neil Daftary et al.
- **Institution/Company**: LinkedIn
- **Date**: 2026-02
- **Abstract**: Decoder-only transformer for ads CTR with context-conditioned decoding, self-gated attention, timestamp-based RoPE, and session masking. Achieves 11.04% CTR lift vs. production baseline in online A/B testing. Deployed on LinkedIn's main ad traffic.
- **Key Innovations**: Multi-tower prediction heads modeling post-scoring signals; self-gated attention for training stability; timestamp RoPE capturing multi-scale temporal relationships.
- **Link**: https://arxiv.org/abs/2602.11410

### 3.4 EST: Efficiently Scalable Transformer for CTR Prediction
- **Authors**: Mingyang Liu et al.
- **Institution/Company**: Alibaba/Taobao
- **Date**: 2026-02
- **Abstract**: Achieves fully unified modeling of all raw inputs without lossy aggregation. Introduces Lightweight Cross Attention (LCA) and Content Sparse Attention (CSA). Exhibits stable power-law scaling. Deployed on Taobao display advertising: +3.27% RPM, +1.22% CTR.
- **Key Innovations**: Unified sequence modeling of heterogeneous features; Content Sparse Attention leveraging content similarity for efficient behavior modeling.
- **Link**: https://arxiv.org/abs/2602.10811

### 3.5 DeRes: Decoupling Residual Stability for Scalable CTR Prediction
- **Authors**: (Not specified)
- **Institution/Company**: (TikTok-related baselines referenced)
- **Date**: 2026-06
- **Abstract**: Routes each layer through dual paths — Identity residual (first-order reuse) and Block Attention Residual (cross-layer recall). Pointwise AttnRes replaces Softmax with SiLU for parallel multi-interest activation. Fits steeper compute–AUC scaling law (γ=0.118 vs 0.071 for OneTrans). 8-layer DeRes matches 16-layer OneTrans.
- **Key Innovations**: Dual-path inter-layer connector combining DPN and cross-layer attention; Pointwise SiLU for multi-interest patterns.
- **Link**: https://arxiv.org/abs/2606.07980

### 3.6 Dual-Stream MLP is All You Need for CTR Prediction
- **Authors**: Kesha Ou et al.
- **Institution/Company**: Renmin University, ByteDance, Meituan
- **Date**: 2026-06
- **Abstract**: Uses knowledge distillation to consolidate explicit feature interactions into a main MLP, while a parallel MLP captures implicit interactions. Achieves SOTA across three benchmarks with vanilla MLP structure only.
- **Key Innovations**: KD-based dual-stream MLP framework; simple MLP achieving comparable performance to complex architectures.
- **Link**: https://arxiv.org/abs/2606.04944

### 3.7 IDProxy: Cold-Start CTR Prediction at Xiaohongshu
- **Authors**: (Xiaohongshu team)
- **Institution/Company**: Xiaohongshu
- **Date**: 2026-03
- **Abstract**: Uses multimodal LLMs to generate proxy embeddings from content signals for new items without usage data. Proxies are explicitly aligned with existing ID embedding space and optimized end-to-end. Deployed in Content Feed and Display Ads.
- **Key Innovations**: MLLM-generated proxy embeddings aligned to ID space; end-to-end training under CTR objectives.
- **Link**: https://arxiv.org/abs/2603.01590

### 3.8 GenCI: Generative Modeling of User Interest Shift for CTR
- **Authors**: (Not specified)
- **Institution/Company**: (Published at WWW 2026)
- **Date**: 2026-01
- **Abstract**: Leverages semantic interest cohorts as explicit intent representations. A generative model produces candidate interest cohorts via NTP, injected into ranking via hierarchical candidate-aware cross-attention. Bridges recall-ranking gap by making CTR aware of retrieval context.
- **Key Innovations**: Candidate-agnostic intent representation via generative modeling; hierarchical candidate-aware network for recall-ranking alignment.
- **Link**: https://arxiv.org/abs/2601.18251

### 3.9 CDNet: Core-Behaviors and Distributional-Compensation Dual-View Interaction
- **Authors**: Yi Xu et al.
- **Institution/Company**: (Not specified)
- **Date**: 2026-03
- **Abstract**: Bridges sequential and contextual feature interactions from two complementary angles: fine-grained interaction with most relevant behaviors, and coarse-grained interaction modeling overall interest distribution. Addresses the aggregation information loss problem.
- **Key Innovations**: Dual-view interaction network; fine-grained core-behavior identification with distributional compensation.
- **Link**: https://arxiv.org/abs/2603.12578

---

## 4. Sequential Modeling

### 4.1 Multi-Behavior Sequential Modeling with TGA
- **Authors**: Gaoming Yang et al.
- **Institution/Company**: (Not specified)
- **Date**: 2026-01
- **Abstract**: Proposes Transition-Aware Graph Attention Network (TGA) for multi-behavior transitions with linear complexity. Constructs structured sparse graphs from item-level, category-level, and neighbor-level transitions. Deployed in large-scale industrial production.
- **Key Innovations**: Linear-complexity multi-behavior transition modeling; three-perspective graph construction for behavior transitions.
- **Link**: https://arxiv.org/abs/2601.14955

---

## 5. Game AI & Reinforcement Learning

### 5.1 Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini, Joakim Bergdahl et al.
- **Institution/Company**: EA (Electronic Arts)
- **Date**: 2026-06
- **Abstract**: Vision paper proposing a framework for training RL models suited for game AI and game development. Presents experiments in EA SPORTS FC 25 (goalkeeper AI) and Battlefield 6 (ground infantry). Identifies bottlenecks and hard problems for RL adoption in game production.
- **Key Innovations**: Production-oriented framework for RL-based game AI; practical requirements for deploying ML agents in commercial games.
- **Link**: https://arxiv.org/abs/2606.20210

### 5.2 Think in Games (TiG): Learning to Reason via RL with LLMs
- **Authors**: (Not specified)
- **Institution/Company**: (Not specified)
- **Date**: 2025-08
- **Abstract**: Empowers LLMs to develop procedural understanding through direct game interaction. Reformulates RL decision-making as a language modeling task using GRPO. Qwen-3-14B achieves 90.91% accuracy in Honor of Kings, outperforming DeepSeek-R1 (86.67%).
- **Key Innovations**: Bridging declarative and procedural knowledge in LLMs; language-guided RL policies with natural language explanations.
- **Link**: https://arxiv.org/abs/2508.21365

### 5.3 Mean Field Reinforcement Learning
- **Authors**: Mathieu Laurière et al.
- **Institution/Company**: (Not specified)
- **Date**: 2026-07-01
- **Abstract**: Comprehensive monograph on mean field RL through the lens of large-population stochastic control. Covers dynamic programming principles, propagation-of-chaos limits, tabular Q-learning, policy-gradient methods, and deep RL methods (DDPG). Bridges mean field control theory and RL methodology.
- **Key Innovations**: Mathematical framework connecting multi-agent RL with mean field control; theoretical analyses of tabular and deep methods.
- **Link**: https://arxiv.org/abs/2607.01525

### 5.4 Reward-Free Evolving Agents via Pairwise Validator
- **Authors**: Minghao Liu et al.
- **Institution/Company**: (Not specified)
- **Date**: 2026-07-15
- **Abstract**: Replaces scalar reward with a pairwise validator (frozen LLM comparing parent and child candidates) in self-evolving agentic loops. Integrates into three published engines (GEPA, ADRS, ShinkaEvolve). Matches or exceeds full-reward baselines without labeling cost.
- **Key Innovations**: Pairwise validation as drop-in replacement for reward design; contrastive judgment for agent self-improvement.
- **Link**: https://arxiv.org/abs/2607.14408

### 5.5 Long-Horizon-Terminal-Bench
- **Authors**: (Not specified)
- **Institution/Company**: (Not specified)
- **Date**: 2026-07-13
- **Abstract**: Benchmark of 46 long-horizon terminal tasks spanning 9 categories. Tasks require hundreds of episodes, 9.8M tokens, ~89 minutes on average. Grok 4.5 achieves only 28.3% pass rate at 0.95 threshold; mean across models is 6.4%. Includes interactive games (2048, chess, Snake, Super Mario).
- **Key Innovations**: Dense intermediate reward grading for partial credit; long-horizon task decomposition for evaluating agent persistence.
- **Link**: https://arxiv.org/abs/2607.08964

---

## Summary Statistics

| Category | Papers |
|----------|--------|
| LLMs & Foundation Models | 6 |
| Recommendation Systems | 13 |
| CTR Prediction & Advertising | 9 |
| Sequential Modeling | 1 |
| Game AI & RL | 5 |
| **Total** | **34** |

## Key Trends Observed

1. **Generative Recommendation Maturation**: Semantic IDs (SIDs) are becoming the dominant paradigm for unifying retrieval and ranking, with production deployments at Shopee, music services, and Taobao.

2. **Reasoning in Recommendation**: Multiple papers apply LLM-style reasoning to sequential recommendation — recursive refinement, retrieval-augmented generation, and chain-of-attribute approaches are all gaining traction.

3. **Long-Sequence Efficiency**: Hybrid attention architectures (linear + softmax), learned compression tokens, and offline/online splits are the primary strategies for handling million-scale user histories in production.

4. **CTC Scaling Laws**: Industrial CTR models are following LLM-inspired scaling patterns — EST at Taobao, GRAB at Baidu, and CADET at LinkedIn all demonstrate monotonic performance gains with model/compute scaling.

5. **Game AI with RL**: Production game studios (EA) are actively exploring RL augmentation for NPC behavior, while LLM-based approaches (TiG) bridge declarative and procedural knowledge for strategic reasoning.

6. **Cold-Start Solutions**: MLLM-based proxy embeddings (IDProxy at Xiaohongshu) and archetype representations (GenAIR) address the item cold-start challenge in industrial systems.
