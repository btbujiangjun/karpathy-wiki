---
title: arXiv AI Research Scan — July 2026
type: synthesis
created: 2026-07-08
updated: 2026-07-08
tags: [arxiv, survey, llm, recommendation, ctr, sequential-modeling, rl, games, time-series]
---

# arXiv AI Research Scan — July 2026

> Cross-domain scan of recent arXiv preprints across LLMs, recommendation, CTR, advertising, sequential modeling, time series, and game-playing agents.

---

## 1. LLM Training, Inference & Architectures

### 1.1 LLM-as-a-Verifier: A General-Purpose Verification Framework
- **Link**: [2607.05391](https://arxiv.org/abs/2607.05391)
- **Authors**: Jacky Kwok, Shulu Li, Pranav Atreya, Yuejiang Liu, Yixing Jiang, Chelsea Finn, Marco Pavone, Ion Stoica, Azalia Mirhoseini
- **Affiliations**: Stanford University, UC Berkeley, NVIDIA Research
- **Abstract**: Identifies verification as a new scaling axis for LLMs. Proposes a probabilistic verification framework that computes expectation over scoring token logits to produce continuous scores. Scales along score granularity, repeated evaluation, and criteria decomposition.
- **Key Innovations**:
  - Continuous scoring via logit expectation (reduces tie rates vs discrete LM judges)
  - Three-axis verification scaling
  - Training-free, plug-and-play trajectory reward model
  - SOTA on Terminal-Bench V2 (86.5%), SWE-Bench Verified (78.2%), RoboRewardBench (87.4%), MedAgentBench (73.3%)
  - Dense reward signal for RL (SAC, GRPO)

### 1.2 MiniMax Sparse Attention (MSA)
- **Link**: [2606.13392](https://arxiv.org/abs/2606.13392)
- **Authors**: MiniMax AI
- **Affiliation**: MiniMax
- **Abstract**: Blockwise sparse attention built on GQA. Lightweight Index Branch selects Top-k KV blocks per GQA group; Main Branch computes exact block-sparse attention.
- **Key Innovations**:
  - Exp-free Top-k selection + KV-outer sparse attention kernel
  - 28.4× FLOPs reduction at 1M context
  - 14.2× prefill and 7.6× decoding wall-clock speedups on H800
  - Validated on 109B MoE model with native multimodal training
  - Open-source inference kernel and production model (MiniMax-M3)

### 1.3 LLMZero: Discovering Adaptive Training Strategies for RL Post-Training
- **Link**: [2606.18388](https://arxiv.org/abs/2606.18388)
- **Authors**: LLMZero Project Core Team (Amazon)
- **Affiliation**: Amazon
- **Abstract**: LLM agents search over training trajectories via tree search, diagnosing pathologies at checkpoints and proposing coordinated multi-parameter transitions for GRPO.
- **Key Innovations**:
  - Discovers structural principle: capacity params accumulate monotonically, regularization params oscillate
  - 9%–140% relative improvement over base model across 4 GRPO tasks
  - Outperforms grid search by 6%–15%
  - UCT-based tree search with agentic early stopping

### 1.4 Causal Perturbative Elicitation (CPE)
- **Link**: [2606.29604](https://arxiv.org/abs/2606.29604)
- **Authors**: Andrew Mack, Nina Panickssery, Alexander Matt Turner
- **Affiliations**: Principles of Intelligence, Anthropic, Independent
- **Abstract**: Unsupervised method for discovering interpretable LoRAs that elicit latent behaviors in LLMs via tensor decomposition of a transformer slice.
- **Key Innovations**:
  - Data-efficient: discovers behaviors from single example
  - Competes with GRPO on Countdown (85% vs 87%) for Qwen3-8B
  - Restores 85% of locked BigCodeBench performance (sandbagging)
  - Eliminates alignment-faking behavior in Llama3-70B
  - Operates in weight-space rather than token-space

### 1.5 Test-Time Training with Next-Token Prediction (TTT-NTP)
- **Link**: [2606.21803](https://arxiv.org/abs/2606.21803)
- **Authors**: Xuan Ouyang, Zefan Cai, Junjie Hu
- **Abstract**: Fast-weight adaptation method aligning inner-loop writes with NTP signal using next-position contextual hidden state as value target.
- **Key Innovations**:
  - Drop-in fast-weight adaptation for pretrained LLMs
  - Consistent improvement across Llama-3.1-8B (+3.9), Mistral-7B (+3.0), Qwen3-4B (+4.1), Qwen3-0.6B (+2.9) on RULER
  - +5.6 on LongBench-v2 for Llama-3.1-8B
  - Preserves commonsense/knowledge performance

### 1.6 TEMPO: Scaling Test-time Training for Large Reasoning Models
- **Link**: [2604.19295](https://arxiv.org/abs/2604.19295)
- **Authors**: Qingyang Zhang, Xinke Kong, Haitao Wu, Qinghua Hu, et al.
- **Abstract**: TTT framework interleaving policy refinement on unlabeled questions with periodic critic recalibration, formalized via EM algorithm.
- **Key Innovations**:
  - Identifies prior TTT methods as incomplete EM variants
  - Improves OLMO3-7B on AIME 2024 from 33.0% → 51.1%
  - Improves Qwen3-14B from 42.3% → 65.8%
  - Maintains high diversity vs prior TTT plateau

### 1.7 ThinkBooster: Unified Framework for Test-Time Scaling
- **Link**: [2606.06915](https://arxiv.org/abs/2606.06915)
- **Authors**: Vladislav Smirnov, Chieu Nguyen, Sergey Senichev, et al.
- **Abstract**: Modular Python library + benchmark + OpenAI-compatible proxy for TTC scaling strategies and reasoning scorers.
- **Key Innovations**:
  - Unified evaluation with quality-cost trade-offs
  - Drop-in adaptive reasoning for real-world apps
  - Visual debugger for reasoning trajectories

### 1.8 When More Thinking Hurts: Overthinking in LLM Test-Time Compute
- **Link**: [2604.10739](https://arxiv.org/abs/2604.10739)
- **Abstract**: Systematic study of diminishing marginal returns and "overthinking" where extended reasoning abandons correct answers.
- **Key Innovations**:
  - Flip event tracking for answer changes across budgets
  - Easy problems overthink at ~2K tokens, hard at ~8K
  - Cost-aware evaluation framework (λ parameter)
  - Early stopping achieves 97% peak accuracy at 60% compute

### 1.9 Test-Time Scaling Makes Overtraining Compute-Optimal (T² Scaling)
- **Link**: [2604.01411](https://arxiv.org/abs/2604.01411)
- **Authors**: Nicholas Roberts, Sungjun Cho, Zhiqi Gao, et al.
- **Abstract**: Joint scaling laws optimizing model size, training tokens, and inference samples under end-to-end budgets.
- **Key Innovations**:
  - Modernizes Chinchilla with pass@k modeling
  - Optimal pretraining shifts to overtraining regime when inference cost is accounted for
  - Validated with heavily overtrained models

---

## 2. Advertising & CTR Prediction

### 2.1 OneRanker (Tencent)
- **Link**: [2603.02999](https://arxiv.org/abs/2603.02999)
- **Authors**: Tencent
- **Affiliation**: Tencent (Weixin Channels)
- **Abstract**: Unified generation + ranking framework for advertising. Value-aware multi-task decoupling with coarse-to-fine target awareness and dual-side consistency guarantees.
- **Key Innovations**:
  - Task token sequences + causal mask for interest/value separation
  - Fake Item Tokens for implicit target awareness
  - Key/Value pass-through + Distribution Consistency loss
  - Deployed on Weixin Channels: GMV-Normal +1.34%

### 2.2 GR4AD (Kuaishou)
- **Link**: [2602.22732](https://arxiv.org/abs/2602.22732)
- **Authors**: Kuaishou
- **Affiliation**: Kuaishou
- **Abstract**: Production-oriented generative recommender for large-scale advertising with UA-SID tokenization, LazyAR decoder, and RSPO list-wise RL.
- **Key Innovations**:
  - UA-SID (Unified Advertisement Semantic ID) via fine-tuned MLLM
  - LazyAR: relaxed layer-wise dependencies for short multi-candidate generation
  - RSPO: Ranking-Guided Softmax Preference Optimization
  - Dynamic Beam Serving
  - Up to 4.2% ad revenue improvement; deployed for 400M+ users

### 2.3 DAIAN (Alibaba)
- **Link**: [2602.13971](https://arxiv.org/abs/2602.13971)
- **Authors**: Alibaba
- **Affiliation**: Alibaba (Xianyu)
- **Abstract**: Deep Adaptive Intent-Aware Network addressing "intent myopia" in Trigger-Induced Recommendation.
- **Key Innovations**:
  - User Intent Modeling as probability distribution
  - Hybrid enhancer with ID + semantic information
  - Three-stage training strategy
  - Online: CTR +1.59%, diversity +1.73%, bills +2.37%

### 2.4 DS-MLP: Dual-Stream MLP for CTR
- **Link**: [2606.04944](https://arxiv.org/abs/2606.04944)
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Affiliations**: Renmin University, ByteDance, Meituan
- **Abstract**: Knowledge distillation consolidates explicit feature interaction into main MLP; parallel MLP handles implicit interactions.
- **Key Innovations**:
  - Pure MLP architecture achieving SOTA
  - Distillation → alignment → overall optimization pipeline
  - SOTA on Criteo, Avazu, Movielens
  - Efficient inference comparable to lightweight models

### 2.5 RankUp (Tencent)
- **Link**: [2604.17878](https://arxiv.org/abs/2604.17878)
- **Authors**: Jin Chen, Shangyu Zhang, Bin Hu, Chao Zhou, Junwei Pan, et al.
- **Affiliation**: Tencent
- **Abstract**: Addresses representation collapse in deep recommender systems via randomized permutation splitting and multi-embedding paradigm.
- **Key Innovations**:
  - Identifies damped oscillatory effective rank trajectory
  - Global token integration + crossed pretrained embedding tokens
  - GMV: +3.41% (Video Accounts), +4.81% (Official Accounts), +2.12% (Moments)

### 2.6 GRAB (Baidu)
- **Link**: [2602.01865](https://arxiv.org/abs/2602.01865)
- **Authors**: Shaopeng Chen, Chuyue Xie, Huimin Ren, et al.
- **Affiliation**: Baidu
- **Abstract**: Generative Ranking for Ads — end-to-end generative CTR framework with Causal Action-aware Multi-channel Attention.
- **Key Innovations**:
  - CamA mechanism for temporal dynamics and action signals
  - Revenue +3.05%, CTR +3.49%
  - Monotonic linear improvement with longer sequences

### 2.7 GenCI (WWW 2026)
- **Link**: [2601.18251](https://arxiv.org/abs/2601.18251)
- **Abstract**: Generative user intent framework using semantic interest cohorts for CTR prediction.
- **Key Innovations**:
  - Next-item prediction for candidate interest cohort generation
  - Hierarchical candidate-aware network with cross-attention
  - End-to-end recall-ranking consistency
  - Self-supervised regularization

---

## 3. Sequential & Session-based Recommendation

### 3.1 HPGR (WWW 2026)
- **Link**: [2603.00980](https://arxiv.org/abs/2603.00980)
- **Abstract**: Hierarchical and Preference-aware Generative Recommender addressing "flat-sequence" limitation in HSTU-like models.
- **Key Innovations**:
  - Session-based Masked Item Modeling (MIM) pre-training
  - Preference-Guided Sparse Attention (PGSA)
  - Online A/B: eCPM +1.99%

### 3.2 CMSL (Meta)
- **Link**: [2606.28533](https://arxiv.org/abs/2606.28533)
- **Authors**: Meta
- **Affiliation**: Meta
- **Abstract**: Constructive Multi-Sequence Learning — disentangles user history into multiple coherent latent sequences to mitigate "context pollution."
- **Key Innovations**:
  - Learnable Sequence Construction Module via cross-attention
  - Linear-time attention for efficient multi-sequence modeling
  - Deployed across ranking and retrieval on 4 major surfaces at Meta

### 3.3 MVCrec
- **Link**: [2604.14114](https://arxiv.org/abs/2604.14114)
- **Abstract**: Multi-View Contrastive learning for sequential recommendation, integrating ID-based and graph-based views.
- **Key Innovations**:
  - Three contrastive objectives (within-seq, within-graph, cross-view)
  - Multi-view attention fusion (global + local)
  - Up to 14.44% NDCG@10 improvement over SOTA

### 3.4 LLM Distillation for Sequential Recommenders
- **Link**: [2604.21536](https://arxiv.org/abs/2604.21536)
- **Abstract**: Distills LLM-generated textual user profiles into sequential recommenders without LLM inference at serving time.
- **Key Innovations**:
  - Two-phase training (distillation → fine-tune)
  - No architectural modification needed
  - Up to 23.5% Recall@10 improvement
  - 60× faster inference vs LLM-based recommenders

### 3.5 MLTFR
- **Link**: [2604.18200](https://arxiv.org/abs/2604.18200)
- **Abstract**: Multi-LLM Token Filtering and Routing for corpus-free sequential recommendation.
- **Key Innovations**:
  - Interaction-guided token filtering to suppress noisy vocabulary
  - Mixture-of-Experts with Fisher-weighted semantic consensus
  - No textual input or backbone modification needed

### 3.6 Persona-Driven Session-Based with KG
- **Link**: [2604.06928](https://arxiv.org/abs/2604.06928)
- **Abstract**: Learns latent user personas from heterogeneous KG using HDGI, injected into SBRS.
- **Key Innovations**:
  - LLM-derived item embeddings for KG initialization
  - Two-stage: personalized extraction → utilization
  - Consistent gains on Amazon Books and Movies & TV

### 3.7 DiffSBR (KDD 2026)
- **Link**: [2601.03903](https://arxiv.org/abs/2601.03903)
- **Abstract**: Diffusion-based latent neighbor generation for session-based recommendation.
- **Key Innovations**:
  - Retrieval-augmented diffusion + self-augmented diffusion
  - Retriever learns from generator feedback
  - Multi-modal contrastive guidance

---

## 4. Time Series & Sequential Modeling

### 4.1 Time-TK (WWW 2026)
- **Link**: [2602.11190](https://arxiv.org/abs/2602.11190)
- **Abstract**: Multi-Offset Temporal Interaction combining Transformer and Kolmogorov-Arnold Networks for time series forecasting.
- **Key Innovations**:
  - Multi-Offset Time Embedding (MOTE)
  - Multi-Offset Interactive KAN (MI-KAN)
  - SOTA on 14 real-world benchmarks (traffic, BTC/USDT)

### 4.2 TimeSqueeze
- **Link**: [2603.11352](https://arxiv.org/abs/2603.11352)
- **Abstract**: Dynamic patching mechanism using SSM encoder for content-aware segmentation.
- **Key Innovations**:
  - Up to 20× faster convergence, 8× data efficiency
  - Variable-resolution compression preserving critical structure
  - Outperforms point-wise and fixed-patch tokenization

### 4.3 UniTok / UniTok-FM
- **Link**: [2606.09861](https://arxiv.org/abs/2606.09861)
- **Abstract**: Universal time series tokenizer and foundation model pretrained via NTP.
- **Key Innovations**:
  - Vector-quantized autoencoder with progressive-resolution causal architecture
  - Supports zero-shot/prompt-boosted forecasting + few-shot generation/classification
  - Training-free in-context inference across tasks
  - Off-the-shelf LLM architecture (no TS-specific modifications)

### 4.4 UniMamba
- **Link**: [2604.16325](https://arxiv.org/abs/2604.16325)
- **Abstract**: Unified spatial-temporal framework integrating Mamba state-space dynamics with attention.
- **Key Innovations**:
  - Mamba Variate-Channel Encoding with FFT-Laplace Transform + TCN
  - Spatial Temporal Attention Layer
  - SOTA on 8 public benchmarks

### 4.5 TimeFormer
- **Link**: [2510.06680](https://arxiv.org/abs/2510.06680)
- **Abstract**: Self-attention with Hawkes process modulation and causal masking for time series.
- **Key Innovations**:
  - MoSA (Modulated Self-Attention) with temporal priors
  - Multi-scale subsequence analysis
  - Up to 7.45% MSE reduction over SOTA

---

## 5. Games & Reinforcement Learning

### 5.1 Odysseus
- **Link**: [2605.00347](https://arxiv.org/abs/2605.00347)
- **Abstract**: Scaling VLMs to 100+ turn decision-making in Super Mario Land via PPO with lightweight turn-level critic.
- **Key Innovations**:
  - Turn-level critic substantially improves stability over GRPO/Reinforce++
  - SFT initialization + multi-task RL training
  - 3× average game progress vs frontier models
  - Cross-game generalization

### 5.2 SPIRAL
- **Link**: [2506.24119](https://arxiv.org/abs/2506.24119)
- **Abstract**: Self-play on zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) incentivizes transferable reasoning.
- **Key Innovations**:
  - Role-conditioned Advantage Estimation (RAE) for multi-agent stability
  - Up to 10% improvement across 8 reasoning benchmarks
  - Multi-game training yields complementary cognitive skills
  - Benefits even DeepSeek-R1-Distill-Qwen-7B

### 5.3 MARL-GPT
- **Link**: [2604.05943](https://arxiv.org/abs/2604.05943)
- **Abstract**: Single GPT-based model for multi-agent RL across SMACv2, Google Research Football, and POGEMA.
- **Key Innovations**:
  - Single transformer observation encoder (no task-specific tuning)
  - Trained on 1.5B expert trajectory tokens
  - Competitive with specialized MARL algorithms
  - Unified foundation model for diverse multi-agent problems

### 5.4 Stratagem
- **Link**: [2604.17696](https://arxiv.org/abs/2604.17696)
- **Abstract**: Learning transferable reasoning via trajectory-modulated game self-play.
- **Key Innovations**:
  - Reasoning Transferability Coefficient for domain-agnostic patterns
  - Reasoning Evolution Reward for adaptive development
  - Strong gains on competition-level mathematics

### 5.5 Agentic Transformers Provably Learn to Search
- **Link**: [2606.00183](https://arxiv.org/abs/2606.00183)
- **Abstract**: Theoretical analysis showing transformer-based policies learn DFS via RL training dynamics.
- **Key Innovations**:
  - Two-head transformer construction implementing randomized DFS
  - Depth-wise curriculum enables depth generalization
  - Ranked DFS emerges under imbalanced goal distributions

### 5.6 T-STAR
- **Link**: [2604.07165](https://arxiv.org/abs/2604.07165)
- **Abstract**: Tree-structured self-taught agent rectification for multi-turn agent policy optimization.
- **Key Innovations**:
  - Cognitive Tree consolidating trajectories via functionally similar steps
  - Introspective Valuation for variance-reduced step-level advantage
  - In-Context Thought Grafting from successful/failed branches
  - Surgical Policy Optimization at critical divergence points

### 5.7 RAPO
- **Link**: [2603.03078](https://arxiv.org/abs/2603.03078)
- **Abstract**: Retrieval-Augmented Policy Optimization — introduces off-policy step-level traces to expand exploration in agentic RL.
- **Key Innovations**:
  - Hybrid-policy Agentic Rollout with dynamic off-policy-conditioned reasoning
  - Retrieval-aware Policy Optimization with reward + importance shaping
  - +5.0% average gain across 14 datasets
  - 1.2× faster training efficiency

### 5.8 From Trainee to Trainer
- **Link**: [2606.17682](https://arxiv.org/abs/2606.17682)
- **Abstract**: LLM-as-Environment-Engineer framework where policy model redesigns its own RL training environment.
- **Key Innovations**:
  - MAPF-FrozenLake controllable testbed
  - Qwen3-4B outperforms GPT/Gemini as environment designer
  - RL training enhances model's self-diagnostic ability
  - Evidence-based adaptation outperforms naive difficulty scaling

---

## 6. Cross-Cutting Themes

| Theme | Papers |
|---|---|
| **Test-time compute scaling** | LLM-as-a-Verifier, TTT-NTP, TEMPO, ThinkBooster, Overthinking, T² Scaling, Compute Aligned Training |
| **Generative recommendation** | OneRanker, GR4AD, GRAB, GenCI, HPGR |
| **Sparse/efficient attention** | MiniMax MSA, HPGR (PGSA), CMSL (linear attention) |
| **RL for LLM post-training** | LLMZero, Odysseus, SPIRAL, RAPO, T-STAR |
| **Multi-agent systems** | MARL-GPT, SPIRAL, Trainee-to-Trainer |
| **Time series foundation models** | UniTok-FM, TimeSqueeze, Time-TK |
| **CTR architecture innovation** | DS-MLP, DAIAN, RankUp, ML-DCN |
| **Context pollution / disentanglement** | CMSL, HPGR, MVCrec |
