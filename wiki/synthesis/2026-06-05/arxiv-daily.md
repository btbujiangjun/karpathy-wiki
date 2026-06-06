---
title: arXiv Daily — AI Research Survey (June 5, 2026)
type: synthesis
created: 2026-06-05
updated: 2026-06-05
sources: [arXiv cs.AI, cs.LG, cs.IR, cs.CL]
tags: [arxiv-daily, llm, reasoning, recommendation, ctr, advertising, games, rl, sequential-modeling, diffusion-llm, agentic-rl]
---

# arXiv Daily — AI Research Survey (June 5, 2026)

> Coverage: recent submissions from arXiv (May 27 – June 4, 2026) across AI, LLMs, recommendation, CTR, advertising, sequential modeling, games, and RL. ~25 papers highlighted.

---

## 1. LLM Reasoning & Post-Training

### LEPO: Latent Reasoning Policy Optimization for Large Language Models
- **arXiv**: [2604.17892](https://arxiv.org/abs/2604.17892)
- **Authors**: Yuyan Zhou et al.
- **Affiliation**: —
- **Abstract**: Injects controllable stochasticity into latent reasoning via Gumbel-Softmax, restoring exploration capacity. Proposes LEPO, an RL framework applying policy optimization directly to continuous latent representations. Extends gradient estimation from discrete tokens to latent reasoning steps. Significantly outperforms existing RL methods for both discrete and latent reasoning on math/general benchmarks.
- **Key Innovation**: First RL framework for stochastic latent reasoning; unifies gradient estimation over latent representations and discrete tokens.

### LLM Reasoning Is Latent, Not the Chain of Thought
- **arXiv**: [2604.15726](https://arxiv.org/abs/2604.15726)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Position paper arguing LLM reasoning should be studied as latent-state trajectory formation (H1) rather than surface chain-of-thought (H2). Formalizes three competing hypotheses and reorganizes empirical/mechanistic evidence. Recommends treating latent-state dynamics as default object of study and evaluating reasoning with factorized designs.
- **Key Innovation**: Sharp distinction between latent trajectories, surface CoT, and generic serial compute — with compute-audited exemplars.

### OmniOPD: Logit-Free On-Policy Distillation via Speculative Verification
- **arXiv**: [2606.01476](https://arxiv.org/abs/2606.01476)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Replaces token-level logit matching with Monte Carlo rollouts and chunk-level semantic similarity. Peak-entropy scheduler audits only high-uncertainty reasoning forks. Dirichlet-Multinomial Bayesian prior + base-model KL anchor bound variance. Outperforms SFT by +45.31% on math, +18.52% on code; surpasses white-box OPD by +28.64%.
- **Key Innovation**: Black-box teacher compatible; chunk-level semantic verification extracts cleaner signal than token-level logits.

### Generative Recursive Reasoning (GRAM)
- **arXiv**: [2605.19376](https://arxiv.org/abs/2605.19376)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Turns recursive latent reasoning into probabilistic multi-trajectory computation. GRAM models reasoning as stochastic latent trajectories via amortized variational inference. Supports width-based inference-time scaling (parallel trajectory sampling). On Sudoku-Extreme achieves 97.0% (vs. 87.4% TRM, 55.0% HRM), on ARC-AGI-1 52.0%.
- **Key Innovation**: Probabilistic multi-trajectory recursion with unconditional generation capability; strong on constraint-propagation reasoning.

### SeeUPO: Sequence-Level Agentic-RL with Convergence Guarantees
- **arXiv**: [2602.06554](https://arxiv.org/abs/2602.06554)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Models multi-turn interactions as sequentially-executed multi-agent bandit problems. Turn-by-turn sequential policy updates in reverse execution order ensure monotonic improvement and convergence to global optimum via backward induction. On AppWorld and BFCL v4, achieves 43.3%–54.6% relative gains on Qwen3-14B.
- **Key Innovation**: First critic-free agentic RL algorithm with convergence guarantees for multi-turn scenarios.

### AXPO: Agent Explorative Policy Optimization for Multimodal Agentic Reasoning
- **arXiv**: [2605.28774](https://arxiv.org/abs/2605.28774)
- **Authors**: Byung-Kwan Lee et al.
- **Affiliation**: —
- **Abstract**: Identifies the Thinking-Acting Gap in agentic reasoning — tool use attempted on only ~30% of rollouts, all-wrong on ~40% of questions. AXPO fixes the thinking prefix and resamples tool call + continuation for all-wrong subgroups. 8B SFT+AXPO surpasses 32B Base on Pass@4 with 4× fewer parameters.
- **Key Innovation**: Targeted resampling of failed tool-using rollouts resolves structural asymmetry between thinking and acting.

### HGPO: Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks
- **arXiv**: [2602.22817](https://arxiv.org/abs/2602.22817)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Addresses context inconsistency in stepwise advantage estimation. Assigns steps to multiple hierarchical groups by historical context consistency; aggregates with adaptive weighting. On ALFWorld and WebShop with Qwen2.5-1.5B/7B, significantly outperforms existing agentic RL methods.
- **Key Innovation**: Hierarchical grouping + adaptive weighting solves biased advantage estimation in long-horizon agentic tasks.

### MR-Search: Meta-Reinforcement Learning with Self-Reflection for Agentic Search
- **arXiv**: [2603.11327](https://arxiv.org/abs/2603.11327)
- **Authors**: Tengxiao et al.
- **Affiliation**: —
- **Abstract**: Formulates agentic search as in-context meta-RL with self-reflection. Conditions policy on past episodes, generates explicit self-reflections after each episode, uses multi-turn RL with dense relative advantages. 9.2%–19.3% relative improvement across eight multi-hop QA benchmarks.
- **Key Innovation**: Cross-episode exploration via self-reflection; no reward feedback needed at inference time.

---

## 2. Diffusion LLMs (dLLMs)

### FLARE: Diffusion for Hybrid Language Model
- **arXiv**: [2606.01774](https://arxiv.org/abs/2606.01774)
- **Authors**: Yuchen Zhu, Jing Shi, Chongjian Ge, Hao Tan, Yiran Xu, Wanrong Zhu, Jason Kuen, Koustava Goswami, Rajiv Jain, Yongxin Chen, Molei Tao, Jiuxiang Gu
- **Affiliation**: —
- **Abstract**: Systematic recipe for converting hybrid-attention AR LLMs into capable dLLMs. Identifies transfer-data quality as dominant factor for capability preservation. Develops hardware-aware linear attention under diffusion visibility patterns. One checkpoint supports both AR speculative decoding and diffusion parallel denoising. FLARE-2B/4B/9B achieves competitive dLLM quality from Qwen3.5 hybrid checkpoints.
- **Key Innovation**: First to join hybrid-attention backbones with diffusion-style generation; unified inference system for both AR and diffusion paths.

### dMoE: dLLMs with Learnable Block Experts
- **arXiv**: [2605.30876](https://arxiv.org/abs/2605.30876)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Addresses fundamental mismatch between block parallel decoding (dLLMs) and token-level expert selection (MoE). Aggregates token-level expert distributions into unified block-level distributions. Reduces uniquely activated experts from 69.5 to 14.6 while retaining 99.11% performance; 76.64%–79.84% memory reduction; 1.14×–1.66× latency speedup.
- **Key Innovation**: Block-level expert routing for MoE dLLMs; self-distillation training paradigm.

---

## 3. CTR Prediction / Advertising / Recommendation

### DS-MLP: Dual-Stream MLP for CTR Prediction
- **arXiv**: [2606.04944](https://arxiv.org/abs/2606.04944)
- **Authors**: —
- **Affiliation**: RUCAIBox
- **Abstract**: Uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP; parallel MLP captures implicit interactions. Two alignment strategies (hidden state + prediction) integrate the streams. Despite vanilla MLP structure, achieves SOTA across Criteo, Avazu, Movielens with low latency.
- **Key Innovation**: Simple dual-MLP with distillation achieves SOTA — challenges the need for complex interaction architectures.

### CADET: Context-Conditioned Ads CTR Prediction with a Decoder-Only Transformer
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Authors**: LinkedIn
- **Affiliation**: LinkedIn
- **Abstract**: End-to-end decoder-only transformer for ads CTR. Multi-tower prediction heads model post-scoring signals (e.g., ad position); self-gated attention stabilizes training; timestamp-based RoPE captures temporal relationships; session masking prevents train-serve skew. Achieves 11.04% CTR lift over LiRank production baseline. Deployed on LinkedIn homefeed sponsored updates.
- **Key Innovation**: Context-conditioned decoding resolves chicken-and-egg problem between predicted CTR and ranking position.

### GR4AD: Generative Recommendation for Large-Scale Advertising
- **arXiv**: [2602.22732](https://arxiv.org/abs/2602.22732)
- **Authors**: —
- **Affiliation**: Kuaishou
- **Abstract**: Production-oriented generative recommender with UA-SID (Unified Advertisement Semantic ID), LazyAR decoder (relaxes layer-wise dependencies), VSL + RSPO (ranking-guided list-wise RL). Dynamic beam serving adapts beam width across levels and load. Up to 4.2% ad revenue improvement over DLRM stack. Deployed on Kuaishou with 400M+ users, <100ms latency, 500+ QPS per L20.
- **Key Innovation**: Full-stack generative recommender co-designed across tokenization, architecture, learning, and serving for advertising.

### Memento: Personalized RAG-Style Long-Retention Data Scaling for Online Ads
- **arXiv**: [2605.24051](https://arxiv.org/abs/2605.24051)
- **Authors**: —
- **Affiliation**: Meta (Facebook)
- **Abstract**: Treats user history as document corpus, ad requests as queries. Uses Maximal Marginal Relevance (MMR) for retrieval. Two applications: Representation Memento (retrieves historical embeddings for feature augmentation) and Data Memento (retrieves past training examples for rehearsal). Achieves 1% CTR lift, 1.2% CVR lift at Facebook Feed/Reels with 5–10× resource efficiency over linear scaling.
- **Key Innovation**: RAG-style long-retention scaling (365+ days) replaces linear Last-N scaling with retrieval.

### RankUp: High-rank Representations for Large Scale Advertising Recommender Systems
- **arXiv**: [2604.17878](https://arxiv.org/abs/2604.17878)
- **Authors**: —
- **Affiliation**: Tencent (Weixin)
- **Abstract**: Reveals that effective rank of token representations degrades in deeper MetaFormer layers. Proposes randomized permutation splitting, multi-embedding paradigm, global token integration, and crossed pretrained embedding tokens. Deployed on Weixin Video Accounts (+3.41% GMV), Official Accounts (+4.81%), Moments (+2.12%).
- **Key Innovation**: Identifies and mitigates representation collapse in deep recommendation models — scaling requires not just more parameters but better representation diversity.

### EST: Efficiently Scalable Transformer for CTR Prediction
- **arXiv**: [2602.10811](https://arxiv.org/abs/2602.10811)
- **Authors**: —
- **Affiliation**: Alibaba (Taobao)
- **Abstract**: LLM-inspired scaling for CTR prediction with unified modeling. Demonstrates stable power-law scaling relationship on Taobao display advertising. Online A/B: +3.27% RPM, +1.22% CTR on "Guess" scenario; +2.01% CTR, +2.66% RPM on "Post" scenario.
- **Key Innovation**: Empirical demonstration of controlled scaling laws in industrial CTR; native integration of sparse/dense/sequence features.

### GRAB: LLM-Inspired Sequence-First CTR Prediction at Baidu
- **arXiv**: [2602.01865](https://arxiv.org/abs/2602.01865)
- **Authors**: —
- **Affiliation**: Baidu
- **Abstract**: End-to-end generative ranking framework with Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics and action signals. STS training paradigm mitigates distribution shift. Full deployment: +3.49% CTR, +3.05% CPM on Baidu home feed. AUC improves monotonically with model capacity and sequence length without saturation.
- **Key Innovation**: Action-aware multi-channel attention + sequence-first training bridges DLRM and generative recommenders.

---

## 4. Reinforcement Learning & Games

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **arXiv**: [2605.00347](https://arxiv.org/abs/2605.00347)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Studies RL training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns/episode). Adapted PPO with lightweight turn-level critic outperforms GRPO/Reinforce++. Pretrained VLMs provide strong action priors, improving sample efficiency. Achieves at least 3× average game progress than frontier models with cross-game generalization.
- **Key Innovation**: Systematic ablation of RL components for VLM-based game agents; auto-curriculum via inverse trajectory weighting for multi-level training.

### Optimistic Policy Regularization (OPR)
- **arXiv**: [2603.06793](https://arxiv.org/abs/2603.06793)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Lightweight mechanism anchoring policy optimization to historically successful trajectories. Dynamic buffer of high-performing episodes + directional log-ratio reward shaping + auxiliary BC objective. Achieves highest score in 22/49 Atari games at 10M-step budget (baselines at 50M). Generalizes to CAGE Challenge 2 cyber-defense.
- **Key Innovation**: Dynamic memory of successful trajectories prevents premature entropy collapse; extremely sample-efficient.

### PromptPO: When are LLMs Sufficient Policy Optimizers for Sequential RL Tasks?
- **arXiv**: [2605.30719](https://arxiv.org/abs/2605.30719)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Iterative method prompting LLM with state/action/reward descriptions in Python, generating executable policies from rollout feedback. Matches/exceeds PPO/SAC/DQN on hard-exploration tasks and Meta-World robotics with fewer interactions. Underperforms on MuJoCo fine-grained control. Generated policies range from proportional controllers to value iteration algorithms.
- **Key Innovation**: LLM as black-box policy optimizer replaces traditional RL algorithms for many tasks with better sample efficiency.

### RCDT: Conditional Sequence Modeling for Safe RL
- **arXiv**: [2602.08584](https://arxiv.org/abs/2602.08584)
- **Authors**: Wensong Bai et al.
- **Affiliation**: —
- **Abstract**: First CSM-based offline safe RL algorithm supporting zero-shot deployment across multiple cost thresholds. Lagrangian-style cost penalty with auto-adaptive coefficient; reward-cost-aware trajectory reweighting + Q-value regularization. Outperforms prior art on DSRL benchmark.
- **Key Innovation**: Single policy handles multiple safety cost thresholds via conditional sequence modeling.

### CART: Robust Adversarial RL in Stochastic Games via Sequence Modeling
- **arXiv**: [2510.11877](https://arxiv.org/abs/2510.11877)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: First framework enhancing robustness of Decision Transformer in adversarial stochastic games. Formulates protagonist-adversary interaction as stage game with NashQ value. Conditions Transformer policy on NashQ for less exploitable, conservative policies. Accurate minimax value estimation and superior worst-case returns.
- **Key Innovation**: NashQ-conditioned Decision Transformer for adversarial game settings.

---

## 5. LLM Safety & Interpretability

### When Self-Reference Fails to Close: Matrix-Level Dynamics in LLMs
- **arXiv**: [2604.12128](https://arxiv.org/abs/2604.12128)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Studies self-referential inputs across 4 models (Qwen3-VL-8B, Llama-3.2/3.3, Gemma-2-9B). 106 scalar metrics, 300 prompts, 14-level hierarchy. Identifies Non-Closing Truth Recursion (NCTR) as primary destabilizer — attention effective rank Cohen's d=3.14, variance kurtosis d=3.52. NCTR prompts produce +34–56pp more contradictory output.
- **Key Innovation**: Large-scale mechanistic study showing grounded self-reference is stable; recursive truth evaluation without finite-depth resolution causes matrix-level disruption.

### NANOZK: Layerwise Zero-Knowledge Proofs for Verifiable LLM Inference
- **arXiv**: [2603.18046](https://arxiv.org/abs/2603.18046)
- **Authors**: Zhaohui Wang et al.
- **Affiliation**: —
- **Abstract**: Makes LLM inference verifiable — users cryptographically confirm specific model was used. Layerwise proof framework with constant-size proofs (5.5KB/layer) regardless of model width. 24ms verification time. 70× smaller proofs and 5.7× faster proving than EZKL at d=128. Zero accuracy loss via lookup table approximations.
- **Key Innovation**: Practical zero-knowledge proofs for transformer inference; Fisher information-guided selective verification.

### Shifting the Gradient: Defensive Training Methods Protect Language Model Integrity
- **arXiv**: [2604.16423](https://arxiv.org/abs/2604.16423)
- **Authors**: Satchel Grant et al.
- **Affiliation**: —
- **Abstract**: Behavioral and mechanistic comparison of Positive Preventative Steering (PPS) and Inoculation Prompting (IP). PPS shifts gradient towards attenuating direction along trait axis; IP "explains away" trait expression in training data. IP reduces next-token loss on trait-expressing data; PPS need not. Distinct mechanisms with different failure modes.
- **Key Innovation**: Mechanistic decomposition shows PPS vs. IP operate through fundamentally different gradient dynamics.

---

## Summary & Trends

| Area | Notable Trend | Representative Papers |
|------|--------------|----------------------|
| **LLM Reasoning** | Latent-state reasoning replacing surface CoT; RL directly on continuous representations | LEPO, "LLM Reasoning Is Latent", GRAM |
| **Diffusion LLMs** | Hybrid-attention + diffusion convergence; MoE for dLLMs | FLARE, dMoE |
| **CTR/Advertising** | Generative recommenders replacing DLRM stacks across all major platforms (Meta, Kuaishou, Taobao, Baidu, LinkedIn, Tencent) | CADET, GR4AD, Memento, RankUp, EST, GRAB |
| **Agentic RL** | Convergence-guaranteed algorithms; meta-RL with self-reflection; VLM game agents | SeeUPO, AXPO, HGPO, MR-Search, Odysseus |
| **Safety** | Mechanistic understanding of self-reference failures; verifiable inference via ZKPs | Self-Reference Dynamics, NANOZK |

~25 papers surveyed. All papers sourced from arXiv cs.AI, cs.LG, cs.IR, cs.CL (submissions through June 4, 2026).
