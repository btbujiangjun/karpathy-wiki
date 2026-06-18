---
title: "arXiv Daily Digest — 2026-06-18"
type: synthesis
created: 2026-06-18
updated: 2026-06-18
sources: []
tags: [arxiv, daily-digest, llm, ctr, recommendation, agents, games, sequential-modeling]
---

# arXiv Daily Digest — 2026-06-18

> Curated recent papers across AI, LLMs, recommendation, CTR prediction, advertising, sequential modeling, games, and agents. Sourced from arXiv cs.AI, cs.LG, cs.CL, cs.IR, cs.MA (June 2026 submissions).

---

## 🧠 Large Language Models & Foundation Models

### 1. Variable-Width Transformers
- **Authors:** Zhaofeng Wu, Oliver Sieberling, Shawn Tan, Rameswar Panda, Yury Polyanskiy, Yoon Kim
- **Institution:** MIT, FAIR (Meta)
- **Link:** [arXiv:2606.18246](https://arxiv.org/abs/2606.18246)
- **Date:** 2026-06-17
- **Abstract:** Proposes `><former`, a transformer architecture with nonuniform width — wider early/late layers and narrower middle layers. Across 200M–2B dense and 3B MoE models, this consistently outperforms uniform-width baselines on language modeling loss while reducing FLOPs by 22% and KV cache memory by 15%. Shows bottleneck structure produces qualitatively different residual stream representations.
- **Key Innovation:** Parameter-free residual resizing mechanism enabling variable-width transformers; empirically demonstrates resource-optimal scaling via nonuniform capacity allocation.

### 2. Looped World Models
- **Authors:** Hongyuan Adam Lu et al.
- **Institution:** (Technical Report)
- **Link:** [arXiv:2606.18208](https://arxiv.org/abs/2606.18208)
- **Date:** 2026-06-17
- **Abstract:** A world model architecture with looped (recurrent) structure for sequential decision-making. Explores how iterative refinement through recurrent processing improves long-horizon planning and state estimation.
- **Key Innovation:** Looped/iterative architecture for world models applied to planning and RL.

### 3. VibeThinker-3B: Exploring Verifiable Reasoning in Small Language Models
- **Authors:** (Technical Report)
- **Institution:** (Undisclosed)
- **Link:** [arXiv (DeepPaper featured)](https://arxiv.deeppaper.ai/papers/weekly)
- **Date:** 2026-06-17
- **Abstract:** A 3B-parameter dense model using the Spectrum-to-Signal post-training paradigm. Employs curriculum-based SFT, multi-domain RL, and offline self-distillation. Achieves frontier-level performance on verifiable reasoning tasks despite small size.
- **Key Innovation:** Demonstrates that small models can approach frontier reasoning performance through optimized post-training pipelines.

### 4. Ternary Mamba: Grouped Quantization-Aware Training of W1.58A16 State Space Models
- **Authors:** Ramprasath Ganesaraja, Sahil Dilip Panse, Swathika N
- **Institution:** (Academic)
- **Link:** [arXiv:2606.18114](https://arxiv.org/abs/2606.18114)
- **Date:** 2026-06-17
- **Abstract:** Applies ternary weight quantization (W1.58) with 16-bit activations to Mamba state space models using grouped quantization-aware training. Significantly reduces model footprint while maintaining quality.
- **Key Innovation:** First application of extreme quantization (ternary weights) to SSM-based architectures like Mamba.

### 5. Agentic Reasoning for Large Language Models (Survey)
- **Authors:** Tianxin Wei et al.
- **Institution:** (Multiple)
- **Link:** [arXiv:2601.12538](https://arxiv.org/abs/2601.12538)
- **Date:** 2026-01-18 (updated)
- **Abstract:** Comprehensive survey organizing agentic reasoning along three dimensions: foundational single-agent capabilities (planning, tool use, search), self-evolving reasoning (feedback, memory, adaptation), and collective multi-agent reasoning (coordination, knowledge sharing). Distinguishes in-context reasoning from post-training reasoning via RL/SFT.
- **Key Innovation:** Unified roadmap bridging thought and action across agentic reasoning paradigms; benchmarks across science, robotics, healthcare, and mathematics.

---

## 🎯 CTR Prediction & Advertising

### 6. GenLI: Generative Long-term User Interest Modeling for CTR Prediction
- **Authors:** Jiangli Shao, Kaifu Zheng, Hao Fang, Huimu Ye, Zhiwei Liu, Bo Zhang, Shu Han, Xingxing Wang
- **Institution:** (Industry)
- **Link:** [arXiv:2605.15905](https://arxiv.org/abs/2605.15905)
- **Date:** 2026-05-15
- **Abstract:** Proposes GenLI (Generative Long-term user Interest) for CTR prediction, consisting of an Interest Generation Module (IGM), Behavior Retrieval Module (BRM), and Interest Fusion Module (IFM). Overcomes limitations of target-centered GSUs that ignore latent user interests and have O(n) time complexity for retrieval.
- **Key Innovation:** Generative approach to long-term user interest modeling that escapes the target-centered bias of traditional two-stage retrieval frameworks.

### 7. CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors:** (LinkedIn Team)
- **Institution:** LinkedIn
- **Link:** [arXiv:2602.11410](https://arxiv.org/abs/2602.11410)
- **Date:** 2026-02-11
- **Abstract:** End-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Key innovations include: (1) context-conditioned decoding with multi-tower prediction heads handling post-scoring signals like ad position (resolving the CTR-rank chicken-and-egg problem); (2) self-gated attention stabilizing training; (3) timestamp-based RoPE capturing temporal relationships; (4) session masking for train-serve consistency. Achieved 11%+ improvement in online A/B testing.
- **Key Innovation:** First large-scale deployment of decoder-only transformer architecture for ads CTR prediction; novel self-gated attention mechanism for adaptive information flow regulation.

### 8. GRAB: Generative Ranking for Ads at Baidu — LLM-Inspired Sequence-First CTR
- **Authors:** Chuyue Xie et al.
- **Institution:** Baidu
- **Link:** [arXiv:2602.01865](https://arxiv.org/abs/2602.01865)
- **Date:** 2026-02-02
- **Abstract:** Proposes GRAB, an LLM-inspired generative framework for CTR prediction with Causal Action-aware Multi-channel Attention (CamA). Online deployment at Baidu delivered 3.05% revenue increase and 3.49% CTR lift. Demonstrates monotonic and approximately linear improvement with longer interaction sequences, showing desirable scaling behavior.
- **Key Innovation:** End-to-end generative CTR framework with scaling laws showing monotonic improvement with sequence length; deployed at Baidu scale.

### 9. Field Matters: A Lightweight LLM-enhanced Method for CTR Prediction
- **Authors:** (Multiple)
- **Institution:** (Academic / Industry, published at WWW 2026)
- **Link:** [arXiv:2505.14057](https://arxiv.org/abs/2505.14057)
- **Date:** 2025-05 (WWW 2026)
- **Abstract:** Uses lightweight field-level knowledge from LLMs (rather than instance-level) to enhance CTR prediction. Surprisingly, field-level knowledge alone is competitive with heavier LLM-enhanced methods, challenging the assumption that instance-level knowledge is necessary.
- **Key Innovation:** Demonstrates that field-level LLM knowledge is sufficient for CTR improvement, offering a computationally cheaper alternative.

---

## 📊 Recommendation Systems

### 10. ChronoID: Infusing Explicit Temporal Signals into Semantic IDs for Generative Recommendation
- **Authors:** (Multiple)
- **Institution:** (Academic / Industry)
- **Link:** [arXiv:2606.14269](https://arxiv.org/abs/2606.14269)
- **Date:** 2026-06-12
- **Abstract:** Identifies a fundamental limitation in generative recommendation: semantic IDs are time-agnostic. Proposes ChronoID, a unified framework for time-aware semantic ID learning across three orthogonal temporal dimensions. Benchmarks show significant gains from explicit temporal infusion into semantic IDs.
- **Key Innovation:** First systematic investigation of temporal signals in semantic IDs for generative recommendation; identifies and solves the time-agnostic limitation of existing SID approaches.

### 11. Implicit Reasoning for LLM-based Generative Recommendation
- **Authors:** (Multiple)
- **Institution:** (Multiple)
- **Link:** [arXiv (DeepPaper featured)](https://arxiv.deeppaper.ai/papers/weekly)
- **Date:** 2026-06-17
- **Abstract:** Investigates how to reliably invoke LLMs' pretrained world knowledge for generative recommendation. Explores implicit reasoning mechanisms to improve recommendation quality without explicit prompting.
- **Key Innovation:** Analyzes the gap between LLMs' world knowledge and effective use in generative recommendation; proposes implicit reasoning methods to bridge this gap.

### 12. OneRetrieval: Unifying Multi-Branch E-commerce Retrieval with an Editable Generative Model
- **Authors:** Yupeng Li, Siyuan Wang, Kun Gai
- **Institution:** (Industry — Kun Gai is a well-known figure in Chinese recommendation/CTR)
- **Link:** [arXiv (cs.IR latest)](https://arxivlens.com/category/cs-ir)
- **Date:** 2026-06-11
- **Abstract:** Unifies multi-branch retrieval in e-commerce search using a single editable generative model, replacing hand-tuned fusion. Industrial-scale deployment.
- **Key Innovation:** Single generative model replacing the traditional multi-branch retrieval architecture with hand-tuned merging.

### 13. LLM-Based User Personas for Recommendations at Scale
- **Authors:** Yu Xia, Lichan Hong, Ed H. Chi
- **Institution:** Google Research
- **Link:** [arXiv (ArxivLens cs.IR)](https://arxivlens.com/category/cs-ir)
- **Date:** 2026-06-10
- **Abstract:** Uses LLMs to generate structured user personas from behavioral data for large-scale recommendation. Personas encode user preferences, intents, and context, serving as rich features for downstream rankers.
- **Key Innovation:** Scalable LLM-based persona generation replacing traditional feature engineering for user representation in recommendation.

---

## 🎮 Games, Agents & Multi-Agent Systems

### 14. Agents' Last Exam (ALE): Benchmarking Real-World AI Agent Performance
- **Authors:** Xinyang Han et al. (Dawn Song group)
- **Institution:** UC Berkeley
- **Link:** [arXiv:2606.05405](https://arxiv.org/abs/2606.05405)
- **Date:** 2026-06-03
- **Abstract:** Proposes ALE benchmark with 1,490 real professional tasks across 55 subfields and 13 industry clusters. Tasks are derived from real projects experts completed on the job. Frontier agent configurations average only 2.6% full pass rate on the hardest tier. OpenAI Codex with GPT-5.5 scores 82% on Terminal-Bench but 0% on Last-Exam tasks.
- **Key Innovation:** Real-world professional task benchmark that reveals massive gap between existing agent evaluations and actual workplace capability.

### 15. NeuroGame Transformer: Gibbs-Inspired Attention Driven by Game Theory and Statistical Physics
- **Authors:** Djamel Bouchaffra, Faycal Ykhlef, Hanene Azzag, Mustapha Lebbah, Bilal Faye
- **Institution:** (Academic)
- **Link:** [arXiv:2603.18761](https://arxiv.org/abs/2603.18761)
- **Date:** 2026-03-19
- **Abstract:** Replaces standard attention with game-theoretic and statistical physics concepts. Tokens are treated as players in a cooperative game and as interacting spins in an Ising system. Uses Shapley values and Banzhaf indices for token importance, with attention weights emerging as marginal probabilities under Gibbs distribution. Achieves 86.4% on SNLI, competitive with ALBERT-Base and RoBERTa-Base.
- **Key Innovation:** First attention mechanism grounded in cooperative game theory and Ising models; provides theoretical convergence guarantees and fairness-sensitivity characterization.

### 16. MARLIN: Multi-Agent Game-Theoretic RL for Sustainable LLM Inference
- **Authors:** (Multiple)
- **Institution:** (Academic)
- **Link:** [arXiv:2605.13496](https://arxiv.org/abs/2605.13496)
- **Date:** 2026-05-13
- **Abstract:** Proposes a multi-agent game-theoretic RL framework to co-optimize TTFT, carbon emissions, water usage, and energy costs for LLM inference in cloud datacenters.
- **Key Innovation:** Multi-objective optimization across sustainability metrics (carbon, water, energy) for LLM serving using game-theoretic RL.

### 17. From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents (Survey)
- **Authors:** Yiqi Wang et al.
- **Institution:** (Multiple)
- **Link:** [arXiv:2606.04990](https://arxiv.org/abs/2606.04990)
- **Date:** 2026-06-03 (updated 2026-06-14)
- **Abstract:** Comprehensive survey on evidence tracing and execution provenance for trustworthy LLM agents. Defines execution provenance as the typed graph of agent execution and evidence tracing as its projection onto evidence-support relations. Covers trace sources, provenance relations, granularity, representation, and trust functions.
- **Key Innovation:** Unified framework connecting retrieval grounding, claim support, tool-use safety, memory lineage, observability, debugging, and audit for LLM agents.

### 18. StraTA: Incentivizing Agentic RL with Strategic Trajectory Abstraction
- **Authors:** Xue et al.
- **Institution:** (Academic)
- **Link:** [arXiv:2605.06642](https://arxiv.org/abs/2605.06642)
- **Date:** 2026-05-07
- **Abstract:** Presents a new approach to RL training of LLM agents through explicit strategy planning before action execution. Uses strategic trajectory abstraction to incentivize better long-horizon reasoning.
- **Key Innovation:** Strategy-first approach to agentic RL where agents plan abstract strategies before generating detailed actions.

---

## 🔄 Sequential Modeling

### 19. NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation
- **Authors:** Huichao Zhang et al. (36 authors)
- **Institution:** ByteDance (ByteVisionLab)
- **Link:** [arXiv:2601.02204](https://arxiv.org/abs/2601.02204)
- **Date:** 2026-01-05
- **Abstract:** Unified decoder-only autoregressive transformer trained on 6T interleaved text-image discrete tokens. Uses next-token prediction for text but next-scale prediction for visual generation — enabling 1024x1024 images in 5 seconds, orders of magnitude faster than comparable AR models. Achieves SOTA among unified models and rivals specialized diffusion baselines.
- **Key Innovation:** Next-scale prediction (not raster-scan) for visual generation; prefix-tuning strategy for RL; robust training recipe for multi-scale generation instabilities.

### 20. Understanding Truncated Positional Encodings for Graph Neural Networks
- **Authors:** James Flora, Mitchell Black, Weng-Keen Wong et al.
- **Institution:** (Academic)
- **Link:** [arXiv:2606.13671](https://arxiv.org/abs/2606.13671)
- **Date:** 2026-06-13
- **Abstract:** Proves theoretical equivalence between spectral and walk-based positional encodings in GNNs, with practical guidance on truncation strategies.
- **Key Innovation:** Theoretical unification of two major positional encoding families in GNNs.

---

## 📈 Emerging Themes & Trends

| Theme | Key Papers | Signal |
|-------|-----------|--------|
| **Decoder-only for CTR/RecSys** | CADET, GRAB, GenLI | Industry moving from DLRM → decoder-only transformers for ads |
| **Generative Recommendation** | ChronoID, OneRetrieval, Implicit Reasoning GR | Semantic IDs + temporal awareness becoming mainstream |
| **Small Model Reasoning** | VibeThinker-3B, Ternary Mamba | Push toward reasoning-capable small models (3B and below) |
| **Agent Evaluation Maturity** | ALE (Berkeley), SIMMER, Agentic Reasoning Survey | Benchmarks shifting from toy tasks → real professional workflows |
| **Sustainable AI** | MARLIN, AI Index Report 2026 | Multi-objective optimization including carbon/water costs |
| **Game Theory + Neural Nets** | NeuroGame Transformer | Cross-pollination of cooperative game theory and attention mechanisms |
| **Nonuniform Architectures** | Variable-Width Transformers (`><former`) | Challenging the fixed-width-per-layer assumption |

---

## Key Surveys Noted

- **AI Index Report 2026** — Stanford HAI's ninth edition, tracking governance, evaluation, economic impact, and AI in science/medicine.
- **Agentic Reasoning for LLMs** — Survey of planning, tool use, multi-agent coordination, and RL for agents.
- **From Agent Traces to Trust** — Evidence tracing and execution provenance for trustworthy LLM agents.
- **World Models: A Comprehensive Survey** — Architectures, methodologies, reasoning paradigms, and applications.
