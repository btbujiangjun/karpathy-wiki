---
title: "arXiv Daily — June 8, 2026"
type: synthesis
created: 2026-06-08
updated: 2026-06-08
tags: [arxiv, daily, llm, recommendation, ctr, sequential-modeling, games, agents, scaling]
---

# arXiv Daily — June 8, 2026

Curated recent papers across AI, LLMs, recommendation, advertising, CTR, sequential modeling, games, and related areas. Compiled from arXiv new submissions (Jun 2–8, 2026).

---

## LLMs & Foundation Models

### 1. Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling
- **Authors**: Rohan Shravan
- **Institution**: Independent
- **Abstract**: Trains a 120B-parameter sparse MoE (LightningLM 0.1V) on a single 8-GPU node via recurrence backbone, reversible activations (flat memory), and state-preserving growth from a 2B dense seed through 5B MoE → 9B MoE → 120B MoE (460 routed experts, top-12 routing). Uses TQP strategy (quantized base weights + trained LoRA adapters) to cut optimizer memory ~45×.
- **Key Innovation**: Single-node training of 100B+ MoE; reversibility for activation memory; state-preserving scaling methodology.
- **Link**: https://arxiv.org/abs/2606.07404

### 2. Recursive Language Models (RLMs)
- **Authors**: Alex L. Zhang, Tim Kraska, Omar Khattab (MIT, Stanford)
- **Abstract**: An inference-time scaling paradigm enabling LLMs to process arbitrarily long prompts by recursively calling themselves over snippets. Outperforms GPT-5 by 26% (median) across long-context tasks. RLM-Qwen3-8B post-trained model approaches vanilla GPT-5 quality on 3 tasks.
- **Key Innovation**: Recursive inference for arbitrary-length context; programmatic prompt decomposition.
- **Link**: https://arxiv.org/abs/2512.24601 (updated May 2026)

### 3. DyCon: Dynamic Reasoning Control via Evolving Difficulty Modeling
- **Authors**: Tengyao Tu et al. (ICML 2026)
- **Abstract**: Training-free framework that models evolving difficulty during reasoning via latent step-level embeddings, dynamically controlling reasoning depth to mitigate LLM "overthinking" (redundant reasoning steps). Tested on 4 models (4B–32B) across 12 math/reasoning/coding benchmarks.
- **Key Innovation**: Dynamic reasoning depth control without training; difficulty is linearly encoded in step embeddings.
- **Link**: https://arxiv.org/abs/2606.07108

### 4. Position: Don't Just "Fix it in Post" — A Science of AI Must Study Training Dynamics
- **Authors**: Stella Biderman, Mohammad Aflah Khan, Niloofar Mireshghallah, Catherine Arnett, Fazl Barez, Naomi Saphra (EleutherAI, etc.)
- **Abstract**: Argues AI research must study training dynamics (not just post-hoc analysis) to achieve prediction, intervention, and design of model behaviors. Examines scaling laws, mechanistic interpretability, fairness, memorization, simplicity bias.
- **Key Innovation**: Oral at ICML 2026; lays out research agenda for training dynamics science.
- **Link**: https://arxiv.org/abs/2606.06533

### 5. OpenSkill: Open-World Self-Evolution for LLM Agents
- **Authors**: Zhiling Yan et al. (Lehigh, UIC, etc.)
- **Abstract**: A framework for agents to bootstrap skills and verification signals from scratch using open-world resources (docs, repos, web) without target-task supervision. Builds virtual tasks for self-practice. Attains best automated pass rate across 3 benchmarks.
- **Key Innovation**: Zero-supervision self-evolution; skill transfer across models.
- **Link**: https://arxiv.org/abs/2606.06741

---

## Agents & AI Systems

### 6. How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope
- **Authors**: Jeremy Yang, Kate Zyskowski, Noah Yonack, Jerry Ma (Perplexity AI)
- **Abstract**: Production study comparing Perplexity Search vs. Computer (autonomous agent). Computer performs 26 min autonomous work/session vs 33s for Search; reduces task completion time from 269→36 min (87% time reduction, 94% cost reduction); dissatisfaction rates 55% lower. Agents expand work scope and shift users toward higher-order tasks.
- **Key Innovation**: Real-world production data quantifying agent impact on knowledge work.
- **Link**: https://arxiv.org/abs/2606.07489

### 7. Act As a Real Researcher (AARR) — Benchmark Series
- **Authors**: Jiayu Wang et al.
- **Abstract**: Benchmarks evaluating LLMs and agentic systems on granular research professionalism, thoroughness, and nuanced reasoning. Best config (Mini-SWE-Agent + Claude Opus 4.7) achieves only 68.3% — frequently missing subtle details obvious to human researchers.
- **Key Innovation**: Focus on research behavior, not just task execution capability.
- **Link**: https://arxiv.org/abs/2606.07462

### 8. The Sim-to-Real Gap of Foundation Model Agents: A Unified MDP Perspective
- **Authors**: Xiaoou Liu et al. (KDD 2026 Blue Sky)
- **Abstract**: Formalizes sim-to-real gap for foundation model agents using MDP framework, identifying key factors causing deployment failures.
- **Link**: https://arxiv.org/abs/2606.07017

---

## Recommendation & Advertising Systems

### 9. Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen (Renmin University, TKDD 2026)
- **Abstract**: Proposes a dual-stream MLP with knowledge distillation — consolidates explicit feature interaction into main MLP while a parallel MLP captures implicit interactions. Two alignment strategies for compatibility. Achieves SOTA on 3 benchmarks with vanilla MLP structure.
- **Key Innovation**: Simplifies CTR to pure MLP; resolves explicit/implicit imbalance via distillation.
- **Link**: https://arxiv.org/abs/2606.04944

### 10. SSRLive: Live Streaming Recommendation with Dynamic Semantic ID
- **Authors**: Teng Shi et al.
- **Abstract**: Generative+discriminative unified architecture for live streaming recommendation. Dynamic semantic IDs capture rapidly changing live room content; combines user-streamer interaction signals. Online A/B: watch time +3.38%, GMV +0.72%, followers +3.12%. Serving hundreds of millions of users.
- **Key Innovation**: Dynamic semantic IDs for live content; hybrid generative-discriminative pipeline.
- **Link**: https://arxiv.org/abs/2606.06970

### 11. Bradley-Terry Rankings for Recommender Systems Across Dataset Taxonomies
- **Authors**: Ekaterina Grishina et al. (KDD 2026)
- **Abstract**: Novel data-driven ranking methodology using Bradley-Terry model for fair algorithm comparison across datasets. Introduces ranking consistency metric and BT trees/covariates for predicting rankings on unseen datasets.
- **Key Innovation**: BT-based recommender ranking robust to dataset characteristics; predictive without running models.
- **Link**: https://arxiv.org/abs/2606.07492

### 12. Gated Bidirectional Linear Attention (GBLA) for Generative Retrieval
- **Authors**: Artem Matveev et al. (SIGIR 2026)
- **Abstract**: Linear-time bidirectional attention layer for generative retrieval. Extends kernelized linear attention with Conv1D mixing, key gating, gated RMSNorm. 8.2× speedup at 32K history vs FlashAttention-v3. Matches bidirectional self-attention quality on Yandex Music + Amazon datasets.
- **Key Innovation**: First sub-quadratic bidirectional attention for generative retrieval encoders.
- **Link**: https://arxiv.org/abs/2606.07317

### 13. Scaling Laws for Behavioral Foundation Models over User Event Sequences
- **Authors**: Rickard Brüel Gabrielsson
- **Abstract**: First systematic scaling law study for behavioral foundation models (recommendation/payments/fraud). Across ~600 runs spanning 10^15–10^19 FLOPs. Finds: small embedder (~2% params) is compute-optimal; objective-evaluation metric disagreement scales with compute; optimal negative count grows with budget.
- **Key Innovation**: Comprehensive scaling laws for user-event-sequence models; evaluation metric is part of the scaling law.
- **Link**: https://arxiv.org/abs/2606.05257

### 14. PHKT: Personalized Dynamic Hypergraph-enhanced KAN-Transformer for Multi-behavior Sequential Recommendation
- **Authors**: Ruijie Du et al.
- **Abstract**: Combines personalized dynamic hypergraph (user-specific heterogeneous relationships) with KAN-Transformer (KAN replaces MLP in FFN for nonlinear modeling) for multi-behavior sequential recommendation. Outperforms 9 baselines on Tmall, RetailRocket, IJCAI.
- **Key Innovation**: Hybrid hypergraph + KAN + Transformer for multi-behavior recommendation.
- **Link**: https://arxiv.org/abs/2606.05537

### 15. Beyond Matching: Category-Guided Latent Intent Reasoning for Generative Retrieval in E-Commerce
- **Authors**: Fuwei Zhang et al.
- **Abstract**: Generative retrieval with category-guided latent intent reasoning for e-commerce search. Integrates category hierarchy into generative ranking pipeline.
- **Link**: https://arxiv.org/abs/2606.07075

### 16. Mind the Gap: Bridging Behavioral Silos with LLMs in Multi-Vertical Recommendations
- **Authors**: Nimesh Sinha et al.
- **Abstract**: Uses LLMs to bridge behavioral data silos across multiple recommendation verticals, enabling cross-domain knowledge transfer.
- **Link**: https://arxiv.org/abs/2606.06779

### 17. SAILRec: Steering LLM Attention to Dual-Side Semantically Aligned Collaborative Embeddings
- **Authors**: Xi Wu et al.
- **Abstract**: LLM-based recommendation leveraging dual-side (user+item) semantically aligned collaborative embeddings steered via attention.
- **Link**: https://arxiv.org/abs/2606.04514

### 18. Beyond Retrieval: Learning Compact User Representations for Scalable LLM Personalization
- **Authors**: Heng Cao et al.
- **Abstract**: Compact user representations for scalable LLM personalization in recommendation, enabling efficient user modeling without full history retrieval.
- **Link**: https://arxiv.org/abs/2606.04547

### 19. Bridging Short Videos and Live Streams: Reasoning-Guided Multimodal LLMs for Cross-Domain Representation Learning
- **Authors**: Le Zhang et al. (Kuaishou)
- **Abstract**: Cross-domain recommendation bridging short video and live streaming using reasoning-guided multimodal LLMs.
- **Link**: https://arxiv.org/abs/2606.04448

---

## Sequential Modeling & Transformers

### 20. NeuroGame Transformer: Gibbs-Inspired Attention Driven by Game Theory and Statistical Physics
- **Authors**: Djamel Bouchaffra et al.
- **Abstract**: Replaces standard pairwise attention with game-theoretic (Shapley/Banzhaf) + Ising model framework. Attention weights emerge as Gibbs distribution marginals via mean-field. SNLI 86.4%, competitive with RoBERTa-Base.
- **Key Innovation**: Higher-order token dependencies via cooperative game theory + statistical physics; no explicit O(2^n) complexity.
- **Link**: https://arxiv.org/abs/2603.18761

### 21. Online Pandora's Box for Contextual LLM Cascading
- **Authors**: Alexandre Belloni, Yan Chen, Yehua Wei
- **Abstract**: Theoretical framework for dynamically deciding which LLM to call in a cascade, balancing cost vs. quality.
- **Link**: https://arxiv.org/abs/2606.07392

### 22. Sparsely Gated Tiny Linear Experts
- **Authors**: Simon Schug
- **Abstract**: Tiny linear expert models with sparse gating — efficient alternative to dense models for on-device deployment.
- **Link**: https://arxiv.org/abs/2606.07414

---

## Games & Game Theory

### 23. How reliable are LLMs when it comes to playing dice?
- **Authors**: Luca Avena, Gianmarco Bet, Bernardo Busoni
- **Abstract**: Evaluates LLM reliability in probabilistic/game settings (dice games), probing understanding of randomness and probability.
- **Link**: https://arxiv.org/abs/2606.07515

### 24. AEGIS: A Backup Reflex for Physical AI
- **Authors**: Josef Chen
- **Abstract**: A backup safety mechanism (reflex layer) for physical AI systems including game agents and robotics, providing fail-safe behaviors.
- **Key Innovation**: Hardware-agnostic safety reflex for embodied/game agents.
- **Link**: https://arxiv.org/abs/2606.06660

---

## Evaluation & Benchmarks

### 25. A Comprehensive Anatomy of Human and DeepSeek-R1 LLM Mathematical Reasoning
- **Authors**: Yuxiang Chen, Jun Wang
- **Abstract**: Deep comparison of human vs. DeepSeek-R1 mathematical reasoning processes, identifying differences in strategy and error patterns.
- **Link**: https://arxiv.org/abs/2606.07410

### 26. Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests
- **Authors**: Thanawat Lodkaew et al.
- **Abstract**: Detects cheating in coding agents via randomized test capping; proposes evaluation methodology to prevent overfitting to test cases.
- **Link**: https://arxiv.org/abs/2606.07379

### 27. SABER: Benchmarking Operational Safety of LLM Coding Agents in Stateful Project Workspaces
- **Featured on**: alphaXiv (Jun 1–7, 2026)
- **Abstract**: Safety benchmark for coding agents operating in persistent project environments.
- **Link**: https://arxiv.deeppaper.ai/papers/weekly (featured)

---

## Summary

| Area | Papers |
|------|--------|
| LLMs & Foundation Models | Reversible Foundations 120B MoE, Recursive Language Models, DyCon, Training Dynamics Position, OpenSkill |
| Agents | Perplexity Agent Study, AARR Researcher Benchmark, Sim-to-Real MDP |
| Recommendation & CTR | DS-MLP (pure MLP CTR), SSRLive (live streaming), BT Rankings, GBLA (linear attention), Behavioral Scaling Laws, PHKT (KAN-Transformer), SAILRec, cross-domain LLM recommenders |
| Sequential Modeling | NeuroGame Transformer, GBLA, PHKT |
| Games & Game Theory | LLM dice reliability, AEGIS safety reflex |
| Benchmarks & Evaluation | AARR, Coding agent cheating detection, SABER safety, Math reasoning anatomy |
