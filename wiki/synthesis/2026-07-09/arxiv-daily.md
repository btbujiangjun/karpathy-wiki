---
title: "arXiv Conference Digest — Comprehensive Multi-Venue Report (July 9, 2026)"
type: synthesis
created: 2026-07-09
updated: 2026-07-09
tags: [arxiv, daily-report, llm, recommendation, ctr, games, rl, transformer, kv-cache, icml-2026, kdd-2026, sigir-2026, neurips-2025, iclr-2026, cvpr-2026, acl-2026, www-2026, recsys-2025, cikm-2025, aaai-2026, emnl-2025]
---

# arXiv Conference Digest — Comprehensive Multi-Venue Report

> **Date:** July 9, 2026  
> **Venues covered:** ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025  
> **Topics:** CTR Prediction, Recommendation Systems, Computational Advertising, LLM Training & Architecture, RL for LLMs, Transformer-based Ranking, GNN for CTR, Multi-task Learning, Multi-modal Recommendation, LLM for Recommendation, Feature Interaction, User Behavior Modeling, Sequence Modeling

---

## 🧠 LLM Training, Architecture & Theory

### 1. Review Residuals: Update-Conditioned Residual Gating for Transformers
- **arXiv:** [2606.31859](https://arxiv.org/abs/2606.31859)
- **Key Innovation:** Scales each residual update by learned input-dependent gate. Benefits **emerge at scale** (590M–1B+), no advantage at small scale.
- **Significance:** Could replace standard residual connection in all modern transformers if trend holds at frontier scale.

### 2. Legible-by-Construction: Attention and End-to-End Transformers
- **arXiv:** [2607.04319](https://arxiv.org/abs/2607.04319)
- **Key Innovation:** Sigmoid-bounded value channels + explicit fuzzy-set operations in FFN. At 125M, achieves baseline perplexity while allowing end-to-end reading of named unit composition.
- **Significance:** Built-in auditability instead of post-hoc interpretability.

### 3. Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models
- **arXiv:** [2603.08859](https://arxiv.org/abs/2603.08859)
- **Authors:** UC Berkeley / Stanford
- **Key Innovation:** Proves fundamental limitations of pure Transformers and pure SSMs on function-composition tasks. Constructs small hybrid models achieving both. Learned hybrids outperform pure models with up to **6× fewer parameters**.
- **Significance:** Theoretical foundation for hybrid architecture trend (Jamba, Mamba-2 + attention).

### 4. The Key to Going Linear: Analysis-Driven Transformer Linearization
- **arXiv:** [2607.07706](https://arxiv.org/abs/2607.07706)
- **Key Innovation:** Isolates effect of state update design. Explains why delta-style networks outperform gated accumulation. Introduces sink tokens, short convolutions, fixed-budget cache routing. Scales across LLaMA and Qwen up to 32B.
- **Significance:** Analysis-driven identification closing gap with full attention.

### 5. Fractal KV-Cache Archives: Lossless Symbolic Storage with In-Place Retrieval
- **arXiv:** [2607.07144](https://arxiv.org/abs/2607.07144)
- **Key Innovation:** Contractive iterated-map codes for KV cache. O(1) random access, lossless storage. Per-head residual VQ reduces cache by **36–54× vs fp16** at 11–15% perplexity cost. Doubles as search index.
- **Significance:** Fractal codes simultaneously serving as compressed archive + in-place search index.

### 6. DepthWeave-KV: Token-Adaptive Cross-Layer Residual Factorization
- **arXiv:** [2607.06523](https://arxiv.org/abs/2607.06523)
- **Key Innovation:** Token-adaptive cache compression factorizing KV across layers. Fused CUDA: **8.3× KV memory reduction** at 72.8 tokens/sec for 64K context.
- **Significance:** Cross-layer factorization with token-adaptive rank allocation.

### 7. FourierQK: Spectral Preprocessing of Query-Key Projections
- **arXiv:** [2607.07478](https://arxiv.org/abs/2607.07478)
- **Key Innovation:** FFT-based spectral preprocessing of Q/K projections. Four learned frequencies spanning paragraph-to-word scales achieve **79% reduction in validation loss** over standard dot-product attention.
- **Significance:** First demonstration of Fourier transform on Q/K projections improving attention.

### 8. How Data Shapes RoPE Frequency Usage
- **arXiv:** [2607.07678](https://arxiv.org/abs/2607.07678)
- **Authors:** MIT
- **Key Innovation:** First principled explanation of non-uniform RoPE frequency usage — frequencies selected to match relative-distance structure of training data. Formalizes field-resolution tradeoff.
- **Significance:** Links frequency selection to data properties and length generalization.

### 9. Convergence of Gradient Descent Beyond the NTK Regime
- **arXiv:** [2606.23364](https://arxiv.org/abs/2606.23364)
- **Key Innovation:** Proves GD convergence for pre-normalized multi-layer transformers **beyond NTK regime**, using analyticity and polynomial generalized smoothness.
- **Significance:** One of first rigorous convergence guarantees for modern transformers.

### 10. Algorithmic Foundations of Deep Learning: Complexity-Theoretic Rates
- **arXiv:** [2606.26705](https://arxiv.org/abs/2606.26705)
- **Key Innovation:** Circuit-to-neural-network compilation theorem — any function computable by real-valued circuit compiled into NN with explicit bounds.
- **Significance:** Unifies approximation theory and circuit complexity.

---

## 🤖 LLM RL, Reasoning & Agents

### 11. Agon: Competitive Cross-Model RL with Implicit Rival Grading
- **arXiv:** [2607.07690](https://arxiv.org/abs/2607.07690)
- **Key Innovation:** Two competing LLMs grade each other adversarially. On DeepMath with Qwen3, **doubles GRPO's pass@1** — roughly 8× the gain of untrained MoA baseline. No process labels or reward model needed.

### 12. Max Out GRPO Signal: AdaPrefix-GRPO
- **arXiv:** [2607.07674](https://arxiv.org/abs/2607.07674)
- **Key Innovation:** Prepends correct prefix of reference solution, adaptively adjusts length as feedback controller. At matched FLOPs, **2.1× GRPO accuracy** on held-out hard math (0.6B), 1.6× on Qwen3-1.7B, 1.7× on AIME.

### 13. RL Post-Training Builds Compositional Reasoning Strategies
- **arXiv:** [2607.07646](https://arxiv.org/abs/2607.07646)
- **Key Innovation:** Controlled experiment proving RL composes primitive skills into novel strategies. Phased mechanism: strengthens primitives → discovers sequential/parallel compositions → consolidates. Key difference from RFT: **selectivity, not volume**.

### 14. Single-Rollout Asynchronous Optimization (SAO) for Agentic RL
- **arXiv:** [2607.07508](https://arxiv.org/abs/2607.07508)
- **Authors:** Tsinghua / Zhipu AI / GLM Team
- **Key Innovation:** Replaces group-wise GRPO with single-rollout per prompt + double-side token-level clipping. Outperforms GRPO on SWE-Bench Verified, BeyondAIME. **Deployed in GLM-5.2 (750B-A40B)**.

### 15. Entropy Pacing Policy Optimization (EPPO) for Multi-Task Agentic RL
- **arXiv:** [2607.07178](https://arxiv.org/abs/2607.07178)
- **Authors:** JD
- **Key Innovation:** Task-wise dynamic clipping addressing inter-task entropy crossover. Replaces GRPO's fixed threshold with task entropy-aware adaptive bounds.
- **Significance:** Multi-task agent RL with automatically balanced exploration.

### 16. LLM-as-a-Verifier: A General-Purpose Verification Framework
- **arXiv:** [2607.05391](https://arxiv.org/abs/2607.05391)
- **Key Innovation:** Probabilistic verification using expectation over scoring token logit distributions. SOTA on Terminal-Bench V2 (86.5%), SWE-Bench Verified (78.2%). Training-free, plug-and-play.
- **Significance:** **Verification as a new scaling axis** for LLMs.

### 17. Mechanistically Eliciting Latent Behaviors (CPE)
- **arXiv:** [2606.29604](https://arxiv.org/abs/2606.29604)
- **Key Innovation:** Causal Perturbative Elicitation — unsupervised method discovering interpretable LoRAs that elicit latent model behaviors in weight-space. Statistically tied with GRPO on Countdown (85% vs 87%) for Qwen3-8B.
- **Significance:** Weight-space search for alignment without supervised data.

### 18. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **arXiv:** [2506.24119](https://arxiv.org/abs/2506.24119)
- **Key Innovation:** Self-play framework on multi-turn zero-sum games with Role-Conditioned Advantage Estimation. Up to **10% improvement across 8 reasoning benchmarks**.
- **Significance:** Zero-sum games generate unlimited training data with transferable reasoning capabilities.

### 19. Agentic Transformers Provably Learn to Search via RL
- **arXiv:** [2606.00183](https://arxiv.org/abs/2606.00183)
- **Key Innovation:** Proves transformers trained with policy gradient on tree search learn a **randomized DFS mechanism** — one head tracks actions, another detects failure and triggers backtracking. Depth generalization: trained on depth 1–2, succeeds on deeper.
- **Significance:** First mechanistic proof of search emergence in transformer-based RL.

### 20. MEMO: Memory-Augmented Model Context Optimization for Multi-Agent Games
- **arXiv:** [2603.09022](https://arxiv.org/abs/2603.09022)
- **Key Innovation:** Self-play with persistent memory bank + tournament-style context evolution. No weight updates. Mean win rate 25.1% → 49.5% (GPT-4o-mini). Uses **19× fewer games than RL baselines**.
- **Significance:** Context optimization can rival weight-based RL for LLM agents.

---

## 📊 CTR Prediction — Industrial-Scale Models

### 21. OneRanker: Unified Generation and Ranking with One Model
- **arXiv:** [2603.02999](https://arxiv.org/abs/2603.02999)
- **Authors:** Tencent (WeChat Channels advertising)
- **Key Innovation:** Value-aware multi-task decoupling via task tokens + causal mask. Fake Item Tokens for coarse target awareness. Distribution Consistency Constraint Loss. **GMV-Normal +1.34%** on WeChat Channels.
- **Significance:** Industrial deployment of fully unified generative advertising recommendation.

### 22. GR4AD: Generative Recommendation for Large-Scale Advertising
- **arXiv:** [2602.22732](https://arxiv.org/abs/2602.22732)
- **Authors:** Kuaishou
- **Key Innovation:** UA-SID (Unified Advertising SID via MLLM). LazyAR (lazy autoregressive decoder). RSPO (Ranking-Guided Softmax Preference Optimization). Dynamic Beam Serving. **Up to 4.2% ad revenue** improvement over DLRM. <100ms latency. Serving 400M+ users.

### 23. GRAB: Generative Ranking for Ads at Baidu
- **arXiv:** [2602.01865](https://arxiv.org/abs/2602.01865)
- **Authors:** Baidu
- **Key Innovation:** Causal Action-aware Multi-channel Attention (CamA). End-to-end generative framework. **3.05% revenue increase, 3.49% CTR rise.** Monotonic improvement with longer sequences.
- **Significance:** Scaling laws for generative recommendation at Baidu scale.

### 24. DS-MLP: Dual-Stream MLP is All You Need for CTR Prediction
- **arXiv:** [2606.04944](https://arxiv.org/abs/2606.04944) — **ACM TKDD 2026**
- **Authors:** Renmin Univ / ByteDance / Meituan
- **Key Innovation:** Knowledge distillation into single MLP stream. SOTA across Criteo, Avazu, MovieLens. Vanilla MLP at inference, matches complex interaction models.
- **Significance:** Simple MLP architectures match or beat complex models when properly distilled.

### 25. CADET: Context-Conditioned Ads Decoder-Only Transformer for CTR
- **arXiv:** [2602.11410](https://arxiv.org/abs/2602.11410)
- **Authors:** LinkedIn
- **Key Innovation:** First decoder-only transformer for ads CTR addressing post-scoring contextual signals, offline-online consistency. Industrial deployment at LinkedIn scale.

### 26. IDProxy: Cold-Start CTR Prediction with Multimodal LLMs
- **arXiv:** [2603.01590](https://arxiv.org/abs/2603.01590)
- **Authors:** Xiaohongshu (Little Red Book)
- **Key Innovation:** MLLM generates proxy embeddings from content signals, aligned with ID embedding space. Serves **hundreds of millions of users daily** in Content Feed and Display Ads.
- **Significance:** Practical cold-start solution without sacrificing production ranking.

### 27. SparseCTR: Sparse Attention on Long-term Behaviors
- **arXiv:** [2601.17836](https://arxiv.org/abs/2601.17836) — **WWW 2026**
- **Authors:** Meituan
- **Key Innovation:** Three-branch sparse self-attention (global, interest transitions, short-term). Scaling law across 3 OOM in FLOPs. **Online CTR +1.72%, CPM +1.41%**.
- **Significance:** Makes long-sequence attention practical with scaling law properties.

### 28. GenCI: Generative Modeling of User Interest Shift via Cohort Intent Learning
- **arXiv:** [2601.18251](https://arxiv.org/abs/2601.18251) — **WWW 2026**
- **Key Innovation:** Generative intent framework. Hierarchical quantization → semantic cohorts → NTP training → cross-attention refinement. SOTA on MovieLens, Amazon Fashion.
- **Significance:** Addresses recall-ranking consistency gap.

### 29. DAIAN: Deep Adaptive Intent-Aware Network for Trigger-Induced Recommendation
- **arXiv:** [2602.13971](https://arxiv.org/abs/2602.13971)
- **Key Innovation:** Addresses "intent myopia" in Trigger-Induced Rec. Hybrid enhancer with ID + semantic information for sparse collaborative behaviors.

### 30. RankUp: High-rank Representations for Ad Ranking
- **arXiv:** [2604.17878](https://arxiv.org/abs/2604.17878) — **KDD 2026**
- **Authors:** Tencent
- **Key Innovation:** High-rank representation learning for advertising. Online A/B test validated.

### 31. UniSID: End-to-End Semantic ID Generation for Generative Advertisement
- **arXiv:** [2602.10445](https://arxiv.org/abs/2602.10445)
- **Key Innovation:** Jointly optimizes embeddings and SIDs end-to-end. Multi-granularity contrastive learning. **Up to 4.62% improvement in Hit Rate**.

### 32. LOOPCTR: Loop Scaling for CTR — Alibaba
- **arXiv:** Loop scaling methodology for CTR. Online validated. Published in KDD 2026 proceedings.

---

## 🔬 Recommendation Systems

### 33. MMEACR: Multimodal Memory-Enhanced Agent Collaboration for Recommendation
- **arXiv:** [2607.07108](https://arxiv.org/abs/2607.07108)
- **Key Innovation:** Dual-track memory architecture separating interpretable agent reasoning from fine-grained multimodal matching. User/Item Memory Agents with attribute-guided reinforcement-and-reflection.

### 34. Autonomous Information Seeking: Roadmap for Agentic Recommender Systems
- **arXiv:** [2607.04433](https://arxiv.org/abs/2607.04433)
- **Authors:** NUS / Polimi / Renmin / CAS
- **Key Innovation:** Comprehensive survey with unified taxonomy: agent-assisted → agent-as-recommender → agent-as-user-simulator.
- **Significance:** First systematic taxonomy organized by autonomy level.

### 35. HGenPush: Heterogeneous Generative Recommendation for Push Notifications
- **arXiv:** [2607.03362](https://arxiv.org/abs/2607.03362)
- **Authors:** Kuaishou (Kun Gai)
- **Key Innovation:** First industrial deployment of heterogeneous generative rec (video + author) for push notifications. Non-autoregressive multi-token prediction. **0.181% DAU increase** at Kuaishou.

### 36. R^3: Advertisement Compliance Rectification via Group-Relative Experience and Curriculum RL
- **arXiv:** [2607.07318](https://arxiv.org/abs/2607.07318) — **ACL 2026 Industry Track**
- **Key Innovation:** First industrial framework harmonizing video ad compliance with semantic intent preservation. Text recognition → rewriting → re-rendering.

### 37. IntuRec: Intuition-Guided Latent Reasoning for LLM-Based Recommendation
- **arXiv:** [2606.27684](https://arxiv.org/abs/2606.27684)
- **Key Innovation:** Intuition-guided latent reasoning for recommendation with LLM integration.

### 38. Meta Lattice — Model Space Redesign for Cost-Effective Industry-Scale Ads
- **arXiv:** Meta KDD 2026
- **Key Innovation:** Model space redesign for cost-effective ads recommendation at Meta scale.

### 39. GenCI + GR4AD + OneRanker + GRAB: The Generative Rec Paradigm
- Four major industrial systems (Tencent, Kuaishou, Baidu, Xiaohongshu) all converging on generative recommendation replacing DLRM cascades. Common themes: Semantic IDs, autoregressive next-item prediction, preference alignment via RL.

### 40. Agent-Driven RecSys Iteration: AgentX (Kuaishou)
- **arXiv:** [2606.26859](https://arxiv.org/abs/2606.26859)
- **Key Innovation:** Agent-driven continuous iteration for RecSys. **3.7× business value improvement**.

---

## 🎮 Games & Multi-Agent RL

### 41. Multiplayer Interactive World Models (Kyutai / FAIR)
- **arXiv:** [2607.05352](https://arxiv.org/abs/2607.05352)
- **Key Innovation:** First multiplayer world model with 5B-param latent diffusion. Trained on 10,000 hours of Rocket League. Generates 4-player matches at 20fps on single B200. Stable for hours.
- **Significance:** Major advance in interactive world models — tightly-coupled multi-agent physics.

### 42. MARL-GPT: Foundation Model for Multi-Agent RL
- **arXiv:** [2604.05943](https://arxiv.org/abs/2604.05943)
- **Key Innovation:** Single GPT trained via offline RL on SMACv2 (400M), Google Research Football (100M), POGEMA (1B). No task-specific tuning. Competitive with specialized baselines.
- **Significance:** Demonstrates viability of generalist foundation model for diverse MARL problems.

### 43. RAID: Reward-Adaptive Iterative Discovery for Automated Game Testing
- **arXiv:** [2607.07498](https://arxiv.org/abs/2607.07498)
- **Authors:** EA Sports
- **Key Innovation:** RL-based automated game testing with diversity-enforced exploration. Discovered **6 hockey scoring exploits** in NHL26 matching human playtesters.

### 44. SPIRAL (ICLR 2026) + Stratagem + Agentic Transformers: Self-Play Revolution
- **arXiv:** [2506.24119](https://arxiv.org/abs/2506.24119), multiple papers
- Cross-cutting theme: Self-play on games as the dominant paradigm for LLM reasoning training.

---

## 🔄 Cross-Cutting Themes

| Theme | Papers | Venues |
|-------|--------|--------|
| **Generative Rec replacing DLRM** | OneRanker, GR4AD, GRAB, GenCI, HGenPush | Tencent, Kuaishou, Baidu, WWW |
| **Decoder-only entering CTR** | CADET (LinkedIn), DS-MLP distillation | LinkedIn, TKDD |
| **Scaling laws for Rec/CTR** | SparseCTR, GRAB, LOOPCTR | Meituan WWW, Baidu, Alibaba KDD |
| **Cold-start with MLLMs** | IDProxy | Xiaohongshu |
| **Verification as scaling axis** | LLM-as-a-Verifier | Open (training-free) |
| **Self-play for reasoning** | SPIRAL, Agon, AdaPrefix-GRPO, Agentic Transformers, MEMO | ICLR 2026, arXiv |
| **Multi-agent RL foundation models** | MARL-GPT, Multiplayer World Models | arXiv |
| **Hybrid architectures** | Expressivity-Efficiency Tradeoffs, Review Residuals, Linearization | Berkeley/Stanford |
| **KV-Cache compression** | Fractal KV, DepthWeave-KV | arXiv |
| **Token-adaptive compute** | DepthWeave-KV, PALS pruning | arXiv |
| **CTR via pure MLP (distilled)** | DS-MLP | TKDD 2026 |
| **Integrity of AI control** | Institutional Red-Teaming, Multi-Agent Control | arXiv, DeepMind |

---

## 📈 Summary Statistics

| Category | Papers Curated | Key Venues |
|----------|---------------|------------|
| **LLM Architecture & Theory** | 10 | ICML 2026, arXiv |
| **LLM RL, Reasoning & Agents** | 10 | ICLR 2026, arXiv |
| **CTR Prediction (Industrial)** | 12 | TKDD 2026, WWW 2026, KDD 2026, LinkedIn |
| **Recommendation Systems** | 8 | ACL 2026, WWW 2026, KDD 2026, Kuaishou |
| **Games & Multi-Agent RL** | 4 | ICML 2026, ICLR 2026, EA Sports |

---

*Generated July 9, 2026. Covers arXiv cs.AI, cs.LG, cs.IR, cs.CL submissions and recent conference proceedings (ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, CVPR 2026, KDD 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025).*
