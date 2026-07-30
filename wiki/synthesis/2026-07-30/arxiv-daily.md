---
title: "arXiv Daily Digest — 2026-07-30"
type: synthesis
created: 2026-07-30
updated: 2026-07-30
tags: [arxiv, survey, llm, recommendation, ctr, games, multi-agent, sequential-modeling]
---

# arXiv Daily Digest — 2026-07-30

> Curated from arXiv submissions across AI, LLMs, recommendation systems, CTR prediction, sequential modeling, games, and multi-agent systems. Sources from the last 30 days (July 2026).

---

## 1. Large Language Models (LLMs)

### Penelope: Localized Latent Recurrence for Efficient Structured Reasoning
- **Authors**: Yutong Chen et al.
- **Date**: 2026-07-28
- **Link**: [2607.25915](https://arxiv.org/abs/2607.25915)
- **Abstract**: Introduces a localized latent recurrence mechanism that enables efficient structured reasoning in LLMs by maintaining a compact latent state updated recurrently within local windows, avoiding full KV-cache overhead.
- **Key Innovation**: Localized latent recurrence — combines the efficiency of recurrent models with the expressiveness of transformer attention for structured reasoning tasks.

### MODUS: Decoder-Only Any-to-Any Modeling of Diverse Modalities
- **Authors**: Mingqiao Ye et al.
- **Date**: 2026-07-28
- **Link**: [2607.25948](https://arxiv.org/abs/2607.25948)
- **Abstract**: A decoder-only transformer that handles any-to-any modality generation (text, image, audio, video) in a unified framework, trained on interleaved multimodal data.
- **Key Innovation**: Unified decoder-only architecture for arbitrary input/output modality combinations.

### Memory for Large Language Models
- **Authors**: Multiple
- **Date**: 2026-07-28
- **Link**: [2607.25380](https://arxiv.org/abs/2607.25380)
- **Abstract**: A systematic, architecture-centric taxonomy of memory mechanisms in LLMs, categorizing them by representation, update dynamics, and persistence.
- **Key Innovation**: Unified taxonomy bridging fragmented memory research (retrieval-augmented, parametric, and hybrid memory).

### Minimizing Targeted Activations: Input-Only Suppression of Evaluation-Awareness Latents
- **Authors**: Deepanshu Mody et al.
- **Date**: 2026-07-28
- **Link**: [2607.25907](https://arxiv.org/abs/2607.25907)
- **Abstract**: Proposes input-only interventions to suppress "evaluation-awareness" latents in LLMs — internal representations that emerge when models detect they are being evaluated.
- **Key Innovation**: Mechanistic interpretability approach to reducing benchmark overfitting without model access.

### From Isolated Tasks to Structured Capabilities: A Multilayer Taxonomy for LLMs
- **Authors**: Multiple
- **Date**: 2026-07-24
- **Link**: [2607.22182](https://arxiv.org/abs/2607.22182)
- **Abstract**: Proposes a cognitive-science-inspired multi-layer taxonomy of 14 capability domains and 91 subskills for LLMs, based on meta-analysis of 15,000+ papers.
- **Key Innovation**: Structured capability taxonomy for LLM evaluation and research mapping.

### Understanding Large Language Models
- **Authors**: Yannik Keller, Thomas Eisenmann
- **Date**: 2026-07-02
- **Link**: [2607.01006](https://arxiv.org/abs/2607.01006)
- **Abstract**: Comprehensive survey covering emergent LLM capabilities including symbolic reasoning, theory of mind, and deception strategies, grounded in mechanistic interpretability.
- **Key Innovation**: Bridges mechanistic understanding with emergent capability analysis.

### A Survey on LLM Watermarking: Theory and Deployment
- **Authors**: Multiple
- **Date**: 2026-07-09
- **Link**: [2607.10103](https://arxiv.org/abs/2607.10103)
- **Abstract**: Systematic taxonomy of LLM watermarking techniques categorized by operational requirements, threat models, and security-utility trade-offs.
- **Key Innovation**: Deployment-oriented survey with practical guidance for real-world LLM watermarking.

---

## 2. LLM Reasoning & Test-Time Compute

### ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning
- **Authors**: Vladislav Smirnov et al.
- **Date**: 2026-06-05
- **Link**: [2606.06915](https://arxiv.org/abs/2606.06915)
- **Abstract**: Modular framework implementing state-of-the-art test-time compute scaling strategies (multi-sample, verifier-reranking, adaptive reasoning) with an OpenAI-compatible proxy.
- **Key Innovation**: Unified benchmark and deployable service for test-time compute scaling with quality-cost trade-off analysis.

### LLM-as-a-Verifier: A General-Purpose Verification Framework
- **Authors**: Multiple
- **Date**: 2026-07-08
- **Link**: (reported on DeepPaper)
- **Abstract**: Identifies verification as a new scaling axis. Computes fine-grained token-level feedback for agentic tasks without additional training.
- **Key Innovation**: Verification as third scaling axis (beyond pretraining and post-training compute).

---

## 3. Efficient LLM Serving & KV Cache

### Towards Efficient LLM Serving: A Survey on System-Aware KV Cache Optimization
- **Authors**: Multiple
- **Date**: 2026-07-09
- **Link**: [2607.08057](https://arxiv.org/abs/2607.08057)
- **Abstract**: Comprehensive taxonomy of KV cache optimization techniques across temporal, spatial, and structural dimensions.
- **Key Innovation**: Three-dimensional framework for understanding KV cache optimization co-design.

### Accelerating Masked Diffusion Large Language Models: A Survey
- **Authors**: Multiple
- **Date**: 2026-07-14
- **Link**: [2607.12829](https://arxiv.org/abs/2607.12829)
- **Abstract**: Unified latency decomposition framework and taxonomy of acceleration techniques for diffusion LLMs.
- **Key Innovation**: Systematic analysis of dLLM inference efficiency across algorithms, architectures, and scaling.

---

## 4. Multi-Agent Systems

### Toward an Organizational Science of Multi-Agent LLM Systems
- **Authors**: Huan Chen et al.
- **Date**: 2026-07-28
- **Link**: [2607.25446](https://arxiv.org/abs/2607.25446)
- **Abstract**: Decouples "who" (agent identity), "how" (coordination mechanism), and "which algorithm" (optimization objective) in multi-agent LLM systems.
- **Key Innovation**: Organizational science perspective for designing and analyzing multi-agent LLM systems.

### Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks
- **Authors**: Bart Custers, Koorosh Aslansefat
- **Date**: 2026-07-28
- **Link**: [2607.25877](https://arxiv.org/abs/2607.25877)
- **Abstract**: Uses Bayesian networks to quantify and monitor uncertainty in LLM-based multi-agent systems during runtime.
- **Key Innovation**: Formal uncertainty quantification framework for MAS reliability.

### HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs
- **Authors**: Yu Hao et al.
- **Date**: 2026-07-28
- **Link**: [2607.25853](https://arxiv.org/abs/2607.25853)
- **Abstract**: Hierarchical skill graph construction enabling LLM agents to decompose complex tasks and reuse learned skills.
- **Key Innovation**: Structured skill decomposition and reuse for LLM agents.

### Speculate While You Reason: Joint Agent-Speculator RL
- **Authors**: Jiabao Ji et al.
- **Date**: 2026-07-28
- **Link**: [2607.25816](https://arxiv.org/abs/2607.25816)
- **Abstract**: Jointly trains an agent and a speculator model via RL; the speculator predicts the agent's next tool call for parallel speculative execution.
- **Key Innovation**: Speculative decoding extended to tool-calling agents for latency reduction.

### Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation
- **Authors**: Stefan Krsteski et al.
- **Date**: 2026-07-28
- **Link**: [2607.25891](https://arxiv.org/abs/2607.25891)
- **Abstract**: Large-scale corpus for evaluating LLM agents across diverse benchmarks with fine-grained performance metrics.
- **Key Innovation**: Standardized cross-benchmark evaluation framework for agent systems.

---

## 5. CTR Prediction & Advertising

### CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer (LinkedIn)
- **Authors**: David Pardoe, Neil Daftary, Miro Furtado et al. (LinkedIn)
- **Date**: 2026-02-11
- **Link**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Abstract**: End-to-end decoder-only transformer for ads CTR prediction at LinkedIn. Handles post-scoring contextual signals and maintains offline-online consistency. Achieved +0.04% CTR lift vs. production LiRank.
- **Key Innovation**: Decoder-only architecture for ads CTR with context-conditioned decoding block and multiple prediction heads. Deployed on LinkedIn's homefeed.

### IDProxy: Cold-Start CTR Prediction with Multimodal LLMs (Xiaohongshu)
- **Authors**: Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan et al. (Xiaohongshu)
- **Date**: 2026-03-02
- **Link**: [2603.01590](https://arxiv.org/abs/2603.01590)
- **Abstract**: Uses multimodal LLMs to generate proxy representations for cold-start items in ads and recommendation CTR prediction. Deployed on Xiaohongshu's Explore Feed.
- **Key Innovation**: LLM-generated proxy embeddings bridge cold-start gap without any user history.

### EST: Towards Efficient Scaling Laws in CTR Prediction via Unified Modeling (Alibaba)
- **Authors**: Alibaba
- **Date**: 2026-02-11
- **Link**: [2602.10811](https://arxiv.org/abs/2602.10811)
- **Abstract**: Unified modeling framework for efficient scaling laws in industrial CTR prediction.
- **Key Innovation**: Systematic study of scaling behavior in CTR models with practical deployment insights.

### HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction in CTR Prediction (ByteDance)
- **Authors**: ByteDance
- **Date**: 2026-01
- **Link**: [2601.12681](https://arxiv.org/abs/2601.12681)
- **Abstract**: Unified hybrid transformer architecture tightly integrating long-sequence modeling and feature interaction into a single backbone for CTR prediction.
- **Key Innovation**: Alternating optimization of Query Decoding (long sequences) and Query Boosting (feature interactions).

### ML-DCN: Masked Low-Rank Deep Crossing Network (Pinterest)
- **Authors**: Pinterest
- **Date**: 2026-02-09
- **Link**: [2602.09194](https://arxiv.org/abs/2602.09194)
- **Abstract**: Masked low-rank approach to scale DCN for ads CTR at Pinterest, reducing computation while maintaining accuracy.
- **Key Innovation**: Masked low-rank feature interaction for scalable ads CTR.

---

## 6. Recommendation Systems

### Bridging the Structural Gap: Adapting Autoregressive Generation for Recommendation (Tencent)
- **Authors**: Junchao Zeng, Junzhang Zhu et al. (Tencent)
- **Date**: 2026-07-23
- **Link**: [2607.21028](https://arxiv.org/abs/2607.21028)
- **Abstract**: BARGE — addresses structural gaps in generative recommendation: Item Context-Aware Attention restores item-level structure, Hierarchical Path Reranking + Dual-Path Decoding suppress semantic drift. Online A/B test on Tencent: +0.60% CTR, +1.34% click UV, +1.70% reading time.
- **Key Innovation**: Structural gap analysis + dual-path decoding for generative recommendation.

### Diffusion Language Model for Recommendation (DLMRec)
- **Authors**: Chengyi Liu, Yongqi Zhou, Junwei Pan et al.
- **Date**: 2026-07-23
- **Link**: [2607.21519](https://arxiv.org/abs/2607.21519)
- **Abstract**: Introduces discrete diffusion language model for recommendation, addressing autoregressive limitations with collaborative tokenization and curriculum training.
- **Key Innovation**: First discrete diffusion LM applied to recommendation, enabling parallel decoding.

### MARS: Multi-Agent Re-ranking for Repeat-Order Food Delivery Recommendation
- **Authors**: Jiahao Tian et al.
- **Date**: 2026-07-28
- **Link**: [2607.25471](https://arxiv.org/abs/2607.25471)
- **Abstract**: Multi-agent framework for re-ranking in food delivery, where specialized agents handle different aspects of the re-ranking decision.
- **Key Innovation**: Multi-agent decomposition of re-ranking for domain-specific constraints.

### TRWH: Text-Driven Random Walk Heterogeneous GNN for Semantic-Aware Sparse Recommendation
- **Authors**: He Ma et al.
- **Date**: 2026-07-28
- **Link**: [2607.25471](https://arxiv.org/abs/2607.25471)
- **Abstract**: Uses text-driven random walks on heterogeneous graphs to address sparse recommendation scenarios.
- **Key Innovation**: Text-driven graph exploration for semantic-aware recommendation.

### Kunlun: Establishing Scaling Laws for Massive-Scale Recommendation Systems (Meta)
- **Authors**: Meta
- **Date**: 2026
- **Link**: (reported in paper lists)
- **Abstract**: Establishes scaling laws for massive-scale recommendation through unified architecture design.
- **Key Innovation**: Empirical scaling laws for recommendation model size vs. data vs. performance.

### OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer
- **Authors**: Multiple
- **Date**: 2026-04-12 (WWW '26)
- **Link**: [2604.13737](https://arxiv.org/abs/2604.13737) (related)
- **Abstract**: Unifies feature interaction and sequence modeling into a single transformer backbone for industrial recommenders.
- **Key Innovation**: Single-transformer architecture replacing the traditional two-stage pipeline.

### UniRank: Benchmarking Ranking Models for Unified Sequential Modeling and Feature Interaction
- **Authors**: Honghao Li et al.
- **Date**: 2026-07-22
- **Link**: [2607.19987](https://arxiv.org/abs/2607.19987)
- **Abstract**: Open benchmark for unified sequential modeling and feature interaction in ranking models.
- **Key Innovation**: Standardized reproducible evaluation for unified ranking architectures.

---

## 7. Scaling Laws & Architectures for Recommendation

### MixFormer: Co-Scaling Up Dense and Sequence in Industrial Recommenders (ByteDance)
- **Authors**: ByteDance
- **Date**: 2026
- **Link**: (reported in paper lists)
- **Abstract**: Co-scaling strategy for both dense feature interactions and sequential modeling in large-scale recommenders.
- **Key Innovation**: Joint scaling of two traditionally separate components.

### TokenMixer-Large: Scaling Up Large Ranking Models (ByteDance)
- **Authors**: ByteDance
- **Date**: 2026
- **Link**: (reported in paper lists)
- **Abstract**: TokenMixer architecture scaled to large parameter counts for industrial ranking.
- **Key Innovation**: Token mixing as a scalable alternative to attention for ranking.

### ULTRA-HSTU: Bending the Scaling Law Curve (Meta)
- **Authors**: Meta
- **Date**: 2026
- **Link**: (reported in paper lists)
- **Abstract**: HSTU 2.0 with action encoding (single token for item+action), semi-local attention O(L·(K₁+K₂)), mixed-precision training. 5.3× training, 21.4× inference speedup vs HSTU.
- **Key Innovation**: Action encoding into a single token + semi-local attention for scalability.

### UniMixer: A Unified Architecture for Scaling Laws in Recommendation Systems (ByteDance)
- **Authors**: ByteDance / Kuaishou
- **Date**: 2026-04-01
- **Link**: [2604.00590](https://arxiv.org/abs/2604.00590)
- **Abstract**: Unifies attention, token-mixing, and FM-based paradigms under a single parametric framework. Establishes theoretical foundation for recommendation scaling blocks.
- **Key Innovation**: Unified parametric framework for recommendation architecture design.

---

## 8. Sequential Modeling

### NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation
- **Authors**: Multiple
- **Date**: 2026-01
- **Link**: [2601.02204](https://arxiv.org/abs/2601.02204)
- **Abstract**: Decoder-only autoregressive transformer trained on 6 trillion interleaved text-image discrete tokens. Unifies multimodal understanding and generation via next-scale prediction.
- **Key Innovation**: Next-scale prediction paradigm for unified multimodal sequential modeling.

### HyFormer: Unified Hybrid Transformer for Long-Sequence Modeling and Feature Interaction
- **Authors**: ByteDance
- **Date**: 2026-01
- **Link**: [2601.12681](https://arxiv.org/abs/2601.12681)
- **Abstract**: Alternating optimization of Query Decoding (long sequences up to 3000) and Query Boosting (feature interactions) in a single backbone.
- **Key Innovation**: Unified treatment of long sequences and heterogeneous features in one model.

---

## 9. Games & Reinforcement Learning

### Reinforcement Learning: From Algorithms to Foundation Models
- **Authors**: Zihan Ding (Princeton PhD Thesis)
- **Date**: 2026-07-20
- **Link**: [2607.17560](https://arxiv.org/abs/2607.17560)
- **Abstract**: PhD thesis connecting RL to foundation models — diffusion-based world models, RL for video generation, generative models as policy classes, and interactive video world models.
- **Key Innovation**: Unified view of RL as objective-driven adaptation connecting decision-making, environment modeling, and foundation-model capabilities.

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning
- **Authors**: Multiple
- **Date**: 2026-05
- **Link**: (reported)
- **Abstract**: RL-based training of VLMs for long-horizon decision-making in Super Mario Land, requiring 100+ turns of coordinated perception, reasoning, and action.
- **Key Innovation**: First VLM trained with RL for extended game-playing with visual grounding.

### Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Player Games
- **Authors**: Multiple
- **Date**: 2026-05-06
- **Link**: [2605.00347](https://arxiv.org/abs/2605.00347) (related)
- **Abstract**: Uses RL to teach LLMs strategic game-playing, learning from move-level win/loss feedback.
- **Key Innovation**: Move-level RL training for strategic LLM game-playing.

### Evaluating VLMs for Autonomous Agent-Driven Geometry Clipping Detection in Video Game QA
- **Authors**: Carlos Celemin et al.
- **Date**: 2026-07-28
- **Link**: [2607.25921](https://arxiv.org/abs/2607.25921)
- **Abstract**: Evaluates VLMs as agent-driven QA tools for detecting geometry clipping bugs in video games.
- **Key Innovation**: VLM-based game QA automation for geometric errors.

### The Disruptive Impact of LLMs on Capture the Flag Competitions
- **Authors**: Michael Macaulay et al.
- **Date**: 2026-07-28
- **Link**: [2607.25425](https://arxiv.org/abs/2607.25425)
- **Abstract**: Analyzes how LLMs are disrupting CTF competitions and proposes pathways toward fair play.
- **Key Innovation**: First systematic study of LLM impact on cybersecurity competition integrity.

---

## 10. Cross-Cutting Trends

| Trend | Description | Representative Papers |
|-------|-------------|----------------------|
| **Decoder-Only for Everything** | Decoder-only transformers expanding beyond text to ads CTR, multimodal, recommendation | CADET, MODUS, NextFlow |
| **Generative Recommendation Maturation** | GR moving from ID→semantic tokens with structural gap analysis | BARGE, DLMRec, TRM, ReSID |
| **Scaling Laws for Recommendation** | Systematic study of scaling behavior in ranking/CTR models | EST, Kunlun, UniMixer, ULTRA-HSTU |
| **Unified Sequence + Feature Modeling** | Merging long-sequence modeling and feature interaction into single backbone | HyFormer, MixFormer, OneTrans, UniRank |
| **Test-Time Compute Scaling** | Adaptive reasoning budgets, verifier-based scaling for LLMs | ThinkBooster, LLM-as-a-Verifier |
| **Multi-Agent LLM Systems** | Organizational design, uncertainty monitoring, skill graphs, speculative execution | MAS Org Science, HiSkill, Speculate-While-Reason |
| **Diffusion LMs** | Masked diffusion models as alternative to autoregressive generation | DLMRec, Accelerating dLLMs Survey |
| **RL → Foundation Models** | RL as bridge between decision-making and generative world models | RL: Algorithms to FMs, Odysseus |

---

## Key Takeaways

1. **CTR/Recommendation is converging on decoder-only transformers**: CADET (LinkedIn), BARGE (Tencent), and the Meta HSTU series all point toward transformer architectures replacing traditional DLRMs.
2. **Scaling laws for recommendation are now an active research area**: Multiple papers from Meta, ByteDance, Alibaba, and Kuaishou are establishing empirical scaling laws for ranking models.
3. **Multi-agent LLM systems are maturing**: Beyond proof-of-concept, papers now address organizational design, uncertainty quantification, and efficiency (speculative execution for agents).
4. **Test-time compute scaling is a major focus**: Following the ICLR 2025 Snell et al. paper, frameworks like ThinkBooster bring adaptive reasoning into production.
5. **Generative recommendation addresses structural gaps**: BARGE and DLMRec show that next-token prediction isn't enough — item-level structure and semantic drift must be explicitly handled.
6. **Diffusion LMs emerge for recommendation**: DLMRec demonstrates that discrete diffusion can address autoregressive limitations in recommender systems.
