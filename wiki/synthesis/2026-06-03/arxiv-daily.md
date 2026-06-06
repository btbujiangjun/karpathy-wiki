---
title: arXiv Daily — AI Research Survey (June 3, 2026)
type: synthesis
created: 2026-06-03
updated: 2026-06-03
sources: [arXiv cs.AI, cs.LG, cs.IR, cs.CL]
tags: [arxiv-daily, llm, recommendation, ctr, games, rl, sequential-modeling, advertising]
---

# arXiv Daily — AI Research Survey (June 3, 2026)

> Coverage: recent submissions from arXiv (May 22 – June 2, 2026) across AI, LLMs, recommendation, CTR, advertising, sequential modeling, games, and RL. ~28 papers highlighted.

---

## 1. LLM Architecture & Training

### FLARE: Diffusion for Hybrid Language Model
- **arXiv**: [2606.01774](https://arxiv.org/abs/2606.01774)
- **Authors**: Yuchen Zhu, Jing Shi, Chongjian Ge, Hao Tan, Yiran Xu, Wanrong Zhu, Jason Kuen, Koustava Goswami, Rajiv Jain, Yongxin Chen, Molei Tao, Jiuxiang Gu
- **Affiliation**: —
- **Abstract**: Systematic recipe for converting hybrid-attention (softmax + linear) AR LLMs into serving-efficient diffusion LLMs. Identifies transfer-data quality as dominant factor over loss/mask design. Hardware-aware algorithms for linear attention under diffusion visibility patterns. Unified inference supporting both AR verified decoding and diffusion parallel denoising from same checkpoint. FLARE-2B/4B/9B based on Qwen3.5.
- **Key Innovation**: First systematic study of AR-to-diffusion transfer for hybrid backbones; unified checkpoint supporting two generation regimes.

### ProactiveLLM: Learning Active Interaction for Streaming LLMs
- **arXiv**: [2606.00523](https://arxiv.org/abs/2606.00523)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Shifts LLM generation from passive "read-then-generate" to proactive interaction in streaming scenarios. Uses mask-based streaming modeling + synchronized privileged self-distillation (SPSD) to cultivate intrinsic semantic sufficiency signals without external alignment annotations. Plug-and-play decision heads.
- **Key Innovation**: Endogenous timing decisions without external teachers/annotations; validated across text and speech streaming.

### Causal Methods for LLM Development and Evaluation
- **arXiv**: [2605.25998](https://arxiv.org/abs/2605.25998)
- **Authors**: Konstantin Hess, Haorui Ma, Yuchen Ma, Sonali Parbhoo, Stefan Feuerriegel et al.
- **Affiliation**: LMU Munich, Imperial College London, CMU Pittsburgh
- **Abstract**: Argues causal inference is underutilized in LLM pipeline. Maps opportunities across pretraining, alignment, routing, agentic workflows, and evaluation (LLM-as-a-judge, arenas). Proposes practical principles for causal identification from observational logs.
- **Key Innovation**: Unifying perspective connecting LLM development decisions to causal intervention estimation (KDD 2026).

### Scale Vectors in Large Language Models
- **arXiv**: [2605.26895](https://arxiv.org/abs/2605.26895)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Systematic study of normalization-layer scale vectors in LLMs. Proves they don't increase expressivity but improve optimization via self-amplifying preconditioning. Shows weight decay beneficial for Input-Norm but harmful for Output-Norm. Proposes branch-specific heterogeneity, improved placement, magnitude-direction reparameterization. Validated on 0.12B–2B dense/MoE models.
- **Key Innovation**: First principled analysis of scale vector design; lightweight improvements with consistent gains across scales/optimizers.

### Generative Recursive Reasoning (GRAM)
- **arXiv**: [2605.19376](https://arxiv.org/abs/2605.19376)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Turns recursive latent reasoning into probabilistic multi-trajectory computation. Models reasoning as stochastic latent trajectory enabling multiple hypotheses and inference-time scaling through both depth and parallel trajectory sampling. Outperforms deterministic recursive baselines on Sudoku (97%), ARC-AGI, N-Queens.
- **Key Innovation**: Width-based inference-time scaling via parallel trajectory sampling; 10M params vs 671B DeepSeek-R1 scoring 0% on Sudoku-Extreme.

### Convergence Theory for Iterative LLM-Based NAS
- **arXiv**: [2605.30103](https://arxiv.org/abs/2605.30103)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Proves iterative LLM-NAS is a parametric Cross-Entropy method. Six results: CE equivalence, monotonic quality improvement, geometric convergence, delta-generation advantage, MinHash-Jaccard mode-collapse prevention, closed-form proxy reliability. Empirically validated across 22 cycles, 3 LLMs, 6 datasets, 3300 architectures.
- **Key Innovation**: First formal convergence theory for LLM-based NAS; closed-form proxy reliability diagnostic.

---

## 2. Sequence Modeling & Architecture

### Recurrent Transformer: Greater Effective Depth and Efficient Decoding
- **arXiv**: [2604.21215](https://arxiv.org/abs/2604.21215)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Simple architectural change where each layer attends to KV pairs computed off its own activations (layerwise recurrent memory). Can emulate both Transformer and RNN behaviors. Exact tiling algorithm reduces HBM traffic from Θ(N²) to Θ(N log N). 6-layer RT matches 12-layer Transformer at fixed params, reducing KV cache ~30%.
- **Key Innovation**: Layerwise recurrence with IO-aware tiling algorithm; subsumes both Transformers and RNNs.

### Latent Recurrent Transformer (LRT)
- **arXiv**: [2605.26797](https://arxiv.org/abs/2605.26797)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Lightweight recurrent augmentation reusing source-layer hidden state from previous token as recurrent memory. Adds cross-layer recurrent latent pathway across positions without pause tokens. Interleaved parallel training enables pretraining at ~2× baseline compute. Improves LM loss and ICL with only 0.3% parameter overhead.
- **Key Innovation**: Inference-time zero-cost recurrence; interleaved parallel training avoids sequential unrolling.

### Sessa: Selective State Space Attention
- **arXiv**: [2604.18580](https://arxiv.org/abs/2604.18580)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Places attention inside recurrent feedback path, creating multiple attention-based routing paths. Proves power-law memory tails (O(ℓ^{-β}), β<1) — slower decay than Transformer or Mamba. Only model class realizing flexible selective retrieval with non-decaying influence profiles. Strongest long-context benchmarks while competitive on short-context.
- **Key Innovation**: Theoretically proven power-law memory vs exponential in SSMs; qualitative retrieval advantage.

### Mamba-3: Improved Sequence Modeling using State Space Principles
- **arXiv**: [2603.15569](https://arxiv.org/abs/2603.15569)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Three core innovations: (1) exponential-trapezoidal discretization for more expressive SSM dynamics; (2) complex-valued state update enabling state tracking (equivalent to data-dependent RoPE); (3) MIMO formulation for better FLOP utilization during memory-bound decoding. Improves downstream accuracy by 1.8pp at 1.5B vs Gated DeltaNet.
- **Key Innovation**: Complex-valued SSM state for state-tracking; MIMO for inference efficiency.

### Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models
- **arXiv**: [2603.08859](https://arxiv.org/abs/2603.08859)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Proves fundamental limitations for pure SSMs and pure Transformers on a function-composition task family. Constructs provably successful shallow hybrids with logarithmic size and sublinear memory. Empirically: hybrids outperform non-hybrids with up to 6× fewer params; stronger length generalization and OOD robustness.
- **Key Innovation**: Provable separation between hybrid and pure architectures on expressivity-efficiency Pareto front.

### Hierarchical Kernel Transformer (HKT)
- **arXiv**: [2604.08829](https://arxiv.org/abs/2604.08829)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Multi-scale attention processing input at multiple resolution levels via trainable causal downsampling. Total cost ≤ 4/3 × standard attention regardless of levels. Information-theoretic approximation bounds. +4.77pp on ListOps, +7.47pp on IMDB character sentiment at 1.31× compute overhead.
- **Key Innovation**: PSD kernel interpretation of multi-scale attention; explicit error decomposition with non-Gaussian correction.

### Ouroboros: Dynamic Weight Generation for Recursive Transformers
- **arXiv**: [2604.02051](https://arxiv.org/abs/2604.02051)
- **Authors**: —
- **Affiliation**: RightNow AI
- **Abstract**: Controller hypernetwork generates per-step diagonal modulation vectors applied to frozen SVD-initialized LoRA bases, making each recurrence step input-dependent. On Qwen2.5-3B (17 of 36 layers retained): reduces training loss 43.4%, recovers 51.3% of layer-removal gap with only 9.2M trainable params (0.6%).
- **Key Innovation**: Dynamic per-step weight modulation via tiny hypernetwork; gated recurrence essential for stability.

---

## 3. Recommendation, CTR & Advertising

### Memento: Personalized RAG-Style Long-Retention Data Scaling for Online Ads
- **arXiv**: [2605.24051](https://arxiv.org/abs/2605.24051)
- **Authors**: —
- **Affiliation**: Meta (Facebook)
- **Abstract**: Treats user engagement history as document corpus and ad requests as queries; retrieves relevant interactions via MMR (Maximal Marginal Relevance). Two apps: Representation Memento (feature augmentation) and Data Memento (training rehearsal). 5–10× resource efficiency over linear scaling. Sub-10ms latency. Production: 1% CTR lift on Facebook Feed/Reels, 1.2% CVR lift scaling to 365+ days.
- **Key Innovation**: RAG paradigm applied to recommendation history scaling; deployed at Meta scale.

### CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Authors**: —
- **Affiliation**: LinkedIn
- **Abstract**: End-to-end decoder-only transformer for ads CTR. Context-conditioned decoding with multi-tower heads resolving chicken-and-egg CTR/position problem. Self-gated attention, timestamp RoPE, session masking. Custom FlashAttention kernels. 11.04% CTR lift over LiRank hybrid baseline. Deployed on LinkedIn homefeed sponsored updates.
- **Key Innovation**: Multi-tower context-conditioned decoding resolving position chicken-and-egg; timestamp RoPE.

### GR4AD: Generative Recommendation for Large-Scale Advertising
- **arXiv**: [2602.22732](https://arxiv.org/abs/2602.22732)
- **Authors**: Shaoyun Shi et al.
- **Affiliation**: Kuaishou
- **Abstract**: Production generative recommender with UA-SID (Unified Ad Semantic ID), LazyAR (lazy autoregressive decoder relaxing layer-wise dependencies), VSL (Value-Aware Supervised Learning), RSPO (Ranking-Guided Softmax Preference Optimization). Dynamic beam serving. 4.2% ad revenue improvement over DLRM stack. Deployed serving 400M+ users.
- **Key Innovation**: Full-stack production generative recommender; LazyAR for efficient multi-candidate decoding.

### OneRanker: Unified Generation and Ranking for Advertising
- **arXiv**: [2603.02999](https://arxiv.org/abs/2603.02999)
- **Authors**: Dekai Sun et al.
- **Affiliation**: Tencent (WeChat Channels)
- **Abstract**: Architectural-level deep integration of generation and ranking. Value-aware multi-task decoupling via task tokens + causal mask. Coarse-to-fine collaborative target awareness. KV pass-through + Distribution Consistency (DC) constraint. Deployed on WeChat Channels ads. GMV +1.34%.
- **Key Innovation**: Unified gen/ranking architecture solving optimization tension between interest and value.

### RankUp: High-rank Representations for Large-Scale Advertising
- **arXiv**: [2604.17878](https://arxiv.org/abs/2604.17878)
- **Authors**: —
- **Affiliation**: Tencent (WeChat)
- **Abstract**: Addresses representation collapse in deep recommenders via randomized permutation splitting, multi-embedding paradigm, global token integration, crossed pretrained embedding tokens. GMV +3.41% (Video Accounts), +4.81% (Official Accounts), +2.12% (Moments). Cold-start GMV +9.67%.
- **Key Innovation**: First systematic study of effective rank degradation in deep recommenders; practical mitigation.

### GRAB: LLM-Inspired Sequence-First CTR Prediction (Baidu)
- **arXiv**: [2602.01865](https://arxiv.org/abs/2602.01865)
- **Authors**: —
- **Affiliation**: Baidu
- **Abstract**: End-to-end generative ranking combining DLRM and GR strengths. Causal Action-aware Multi-channel Attention (CamA) capturing temporal dynamics and action signals. Sequence-Then-Sparse (STS) training. Online: 3.49% CTR lift, 3.05% CPM lift. Scaling: monotonic improvement with longer sequences.
- **Key Innovation**: CamA mechanism for multi-channel action-aware attention; STS training for distribution shift.

### EST: Efficient Scaling Laws in CTR Prediction (Taobao)
- **arXiv**: [2602.10811](https://arxiv.org/abs/2602.10811)
- **Authors**: —
- **Affiliation**: Alibaba (Taobao)
- **Abstract**: Unified modeling of feature interactions and user sequences for efficient scaling. Power-law scaling relationship validated. Deployed on Taobao display advertising: RPM +3.27%, CTR +1.22% (Guess); CTR +2.01%, RPM +2.66% (Post-Purchase).
- **Key Innovation**: Practical scaling law verification in industrial CTR; unified sequence + feature interaction.

### LLM-HYPER: Generative CTR for Cold-Start via LLM Hypernetworks
- **arXiv**: [2604.12096](https://arxiv.org/abs/2604.12096)
- **Authors**: —
- **Affiliation**: Top US e-commerce platform
- **Abstract**: LLMs (Gemini-2.5/GPT-4o/GPT-5.1) as hypernetworks generating linear model weights for cold-start ads. Few-shot CoT prompting over multimodal ad content. Normalization + calibration for production. NDCG@10 +55.9% over baselines. Competitive with warm-start in 30-day online A/B.
- **Key Innovation**: Training-free weight generation via LLM reasoning; deployed production cold-start ranking.

### IDProxy: Cold-Start CTR at Xiaohongshu with Multimodal LLMs
- **arXiv**: [2603.01590](https://arxiv.org/abs/2603.01590)
- **Authors**: —
- **Affiliation**: Xiaohongshu (小红书)
- **Abstract**: MLLM-generated proxy embeddings aligned with item ID embedding space. End-to-end under CTR objectives. Deployed in Content Feed and Display Ads, serving hundreds of millions daily users.
- **Key Innovation**: Proxy embedding alignment with ID space for seamless cold-start integration.

---

## 4. Games & Reinforcement Learning

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **arXiv**: [2605.00347](https://arxiv.org/abs/2605.00347)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Studies RL-based VLM training for long-horizon (100+ turns) game playing in Super Mario Land. Adapted PPO with lightweight turn-level critic substantially improves over GRPO/Reinforce++. Pretrained VLMs provide strong action priors. Odysseus achieves 3×+ game progress over frontier models, with in-game and cross-game generalization.
- **Key Innovation**: Turn-level critic for long-horizon VLM RL; SFT + multi-task RL recipe; 100+ turn decision-making.

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **arXiv**: [2506.24119](https://arxiv.org/abs/2506.24119)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Self-play in multi-turn zero-sum language games (TicTacToe, Kuhn Poker, Simple Negotiation) develops transferable reasoning. Role-conditioned Advantage Estimation (RAE) stabilizes multi-agent training. Up to 10.5% improvement across 8 reasoning benchmarks across Qwen and Llama families. TicTacToe → spatial reasoning, Poker → probabilistic, Negotiation → strategic.
- **Key Innovation**: Zero-sum self-play as autonomous reasoning curriculum without human data; transferable cognitive patterns.

### Optimistic Policy Regularization (OPR)
- **arXiv**: [2603.06793](https://arxiv.org/abs/2603.06793)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Lightweight mechanism anchoring PPO to historically successful trajectories via directional log-ratio reward shaping + auxiliary behavioral cloning. Highest score in 22/49 Atari games at 10M-step budget (baselines at 50M). Generalizes to CAGE Challenge 2 cyber-defense, surpassing competition winner.
- **Key Innovation**: Dynamic buffer of high-performing episodes for exploration stabilization; 5× sample efficiency.

### EAPO: Mitigating Tool Abuse in Agentic RL
- **arXiv**: [2606.02132](https://arxiv.org/abs/2606.02132)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Framework teaching agents when not to use tools. Tool-free rollouts provide signal distinguishing necessary vs. abusive tool use. Difficulty-aware reward shaping penalizes tools only on easy queries. Confidence-aware token reweighting. +10.45% accuracy over GRPO while reducing tool calls 18-24% on Qwen2.5-3B/7B and Llama3.1-8B.
- **Key Innovation**: Tool-free trajectories as evidence for necessity; difficulty-aware selective penalization.

### Siri: Self-Internalizing RL with Intrinsic Skills for LLM Agents
- **arXiv**: [2606.02355](https://arxiv.org/abs/2606.02355)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Three-phase framework: warmup with GiGPO, self-skill mining from own successful rollouts, then advantage-weighted distillation into plain policy. No skill bank at inference. Improves GiGPO from 0.908→0.930 on ALFWorld and 0.728→0.813 on WebShop. Outperforms memory-augmented RL baselines.
- **Key Innovation**: Self-generated skills distilled into inference-free policy; training-time-only skill utilization.

### Learning Transferable Skills in Action RPGs (Dark Souls III)
- **arXiv**: [2601.17923](https://arxiv.org/abs/2601.17923)
- **Authors**: —
- **Affiliation**: — (ICLR 2026 Lifelong Agent Workshop)
- **Abstract**: Models combat as directed skill graph (camera, lock-on, movement, dodge, heal-attack) trained via hierarchical curriculum. Selective fine-tuning under domain shift: adapting only 2/5 downstream skills recovers performance. ~230k steps for competitive policy vs monolithic baseline.
- **Key Innovation**: Structured skill factorization enables sample-efficient lifelong adaptation in real-time games.

### NePPO: Near-Potential Policy Optimization for General-Sum MARL
- **arXiv**: [2603.06977](https://arxiv.org/abs/2603.06977)
- **Authors**: Kalanther et al.
- **Affiliation**: —
- **Abstract**: Learns player-independent potential function such that cooperative game NE approximates original game NE. Zeroth-order gradient descent. Outperforms MAPPO, IPPO, MADDPG in mixed cooperative-competitive environments.
- **Key Innovation**: Markov Near-Potential Function framework for general-sum MARL convergence.

---

## 5. Additional Highlights

### A Hierarchical Language Model with Predictable Scaling Laws
- **arXiv**: [2605.13687](https://arxiv.org/abs/2605.13687)
- **Authors**: Jason Gaitonde, Frederic Koehler, Elchanan Mossel, Joonhyung Shin, Allan Sly
- **Affiliation**: —
- **Abstract**: Synthetic hierarchical languages (Ising/coloring broadcast processes) for precise analysis of context length and reasoning. Proves any bounded-context autoregressive model requires Ω(n) context; reasoning model with Θ(log n) working memory samples exactly. Transformer experiments track theoretical predictions quantitatively.
- **Key Innovation**: Clean theoretical separation between autoregressive and reasoning-augmented generation; k-gram ansatz validated.

---

## Quick Stats

| Category | Papers | Notable Institutions |
|----------|--------|---------------------|
| LLM Architecture | 7 | Qwen, LMU Munich |
| Sequence Modeling | 7 | RightNow AI |
| RecSys / CTR / Ads | 9 | Meta, LinkedIn, Kuaishou, Tencent(×2), Baidu, Alibaba, Xiaohongshu |
| Games / RL | 7 | — |
| Theory | 1 | MIT, CMU |
| **Total** | **28** | |

**Trending themes**: Diffusion LLMs (FLARE), hybrid SSM-Transformer architectures, generative recommendation deployment at scale (6 industry papers), long-horizon RL for VLMs, self-play as reasoning curriculum, cold-start solutions via LLMs.
