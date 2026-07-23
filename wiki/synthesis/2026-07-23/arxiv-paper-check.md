---
title: "arXiv Paper Check — 2026-07-23"
type: synthesis
created: 2026-07-23
updated: 2026-07-23
sources: []
tags: [arxiv, ai, ctr, recommendation, agents, reasoning, sequential-modeling]
---

# arXiv Paper Check — 2026-07-23

> Automated search across arXiv for recent papers in AI and CTR (Click-Through Rate) categories from the last 24 hours.

---

## 1. CTR Prediction & Ranking

### 1.1 Long-History User Transformers for Real-Time Ad Ranking
- **Authors**: (Yandex team)
- **Date**: 22 Jul 2026
- **Abstract**: Addresses the latency-quality trade-off in CTR prediction by decoupling heavy sequence computation from real-time inference. A large offline model asynchronously processes user history into cached representations, while a lightweight runtime model combines these with fresh events at serving time. Offline experiments show the split design recovers 72-80% of full-history quality. Production A/B tests demonstrate +2.77% improvement on search ads and +2.1% on Yandex Advertising Network, with revenue gains of +2.26% and +0.43% respectively, without increasing latency.
- **Key Innovations**: Offline-online architecture decoupling; cached history representations; latency-free long-history modeling.
- **Impact**: Demonstrates practical deployment of transformer-based CTR models under strict latency constraints.
- **Link**: (from web search results)

### 1.2 Dual-Stream MLP is All You Need for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Date**: 2026 (TKDD)
- **Abstract**: Proposes DS-MLP, a dual-stream MLP architecture for CTR prediction that achieves state-of-the-art performance while maintaining low latency. The model uses parallel MLP streams to capture different feature interaction patterns, outperforming complex architectures like DCN-v2, DeepFM, and transformer-based models on three benchmark datasets (Criteo, Avazu, Movielens).
- **Key Innovations**: Dual-stream MLP design; simplicity achieving SOTA; efficient inference for large-scale deployment.
- **Impact**: Shows that MLP-only architectures can be competitive with more complex CTR models.
- **Link**: https://github.com/RUCAIBox/DS-MLP

### 1.3 DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction
- **Authors**: (Industrial team)
- **Date**: 2026
- **Abstract**: Introduces DeRes, a dual-path inter-layer connector for CTR Transformers that routes each layer through two parallel paths: an Identity residual path for stability and a Block Attention path for cross-layer adaptivity. Pointwise AttnRes replaces Softmax with SiLU to activate multiple past blocks simultaneously, matching CTR's parallel multi-interest patterns. On industrial dataset (331M interactions), achieves +0.32% AUC with under 5% additional FLOPs, and demonstrates steeper scaling laws (γ=0.118 vs 0.071 for OneTrans).
- **Key Innovations**: Dual-path residual design; Pointwise SiLU attention; steeper compute-AUC scaling law.
- **Impact**: 8-layer DeRes matches 16-layer OneTrans performance, offering 2× compute savings.
- **Link**: (from web search results)

### 1.4 GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning
- **Authors**: (WWW 2026)
- **Date**: 2026 (WWW '26)
- **Abstract**: Proposes a generative user intent framework that constructs semantic interest cohorts as explicit intent representations for CTR prediction. Uses hierarchical quantization to organize items into semantically coherent cohorts, then employs a Transformer-based generative model to produce candidate interest cohorts capturing immediate user intent.
- **Key Innovations**: Generative cohort-based intent modeling; end-to-end trained hierarchical candidate-aware network.
- **Impact**: Addresses limitations of discriminative paradigms in capturing rapid interest shifts.
- **Link**: https://arxiv.org/abs/2601.18251

### 1.5 An Epistemic Position-Based Click Model
- **Authors**: Oscar Rolando Ramirez Milian, Harrie Oosterhuis
- **Date**: 22 Jul 2026 (SIGIR '26)
- **Abstract**: Introduces the first epistemic click model that captures uncertainty in predictions through beta-distributions for relevance and position-bias variables. Proposes approximation and conditioning techniques for stable optimization. Experiments show the epistemic PBM captures uncertainty appropriately and converges faster than pointwise models.
- **Key Innovations**: Epistemic uncertainty modeling in click models; self-normalization and conditioning for gradient stability.
- **Impact**: Provides uncertainty estimates for click predictions, enabling better decision-making.
- **Link**: https://arxiv.org/abs/2607.18712

---

## 2. AI Agents & Safety

### 2.1 NEXUS: Structured Runtime Safety for Tool-Using LLM Agents
- **Authors**: Elias Hossain, Md Mehedi Hasan Nipu, Tasfia Nuzhat Ornee, Rajib Rana, Niloofar Yousefi
- **Date**: 23 Jul 2026
- **Abstract**: Presents NEXUS, a structured-plan safety monitor that applies formal intervention policies to tool-using LLM agents. Combines deterministic safety rules, argument-level inspection, and calibrated logistic-regression risk scoring for graded escalation. Achieves F1 score of 0.949 on synthetic benchmark with 0.205ms median latency (under 0.1% overhead).
- **Key Innovations**: Formal intervention policy framework; multi-level safety escalation; minimal runtime overhead.
- **Impact**: Enables safe deployment of tool-using agents in production environments.
- **Link**: arXiv:2607.19356

### 2.2 OpenEvoShield: Dual Non-Stationary Continual Defense for Multi-Agent Systems
- **Authors**: Litian Zhang, Chaozhuo Li, Yuting Zhang, Zejian Chen, Bingyu Yan, Qiwei Ye
- **Date**: 23 Jul 2026
- **Abstract**: Proposes a co-evolutionary continual defense framework for LLM-based multi-agent systems against evolving adversarial attacks. Uses asymmetric rate control, dynamic behavioral boundaries, and energy-based multi-granularity detection. Evaluated over 100 deployment rounds across five benchmarks.
- **Key Innovations**: Co-evolutionary defense against dynamic attacks; multi-granularity detection; catastrophic forgetting prevention.
- **Impact**: Addresses real-world deployment challenges where both attacks and normal behavior evolve.
- **Link**: arXiv:2607.19351

### 2.3 Stochastic Primal-Dual Decoding for Multiobjective Generative Recommender Systems
- **Authors**: Dmitrii Moor, Ben Carterette, Senthilkumar Krishnamoorthy, et al.
- **Date**: 23 Jul 2026
- **Abstract**: Proposes a lightweight inference-time decoding layer for autoregressive generative recommender systems to support multiobjective slate generation. Formulates decoding as online constrained optimization with dynamic trade-offs based on constraint slack. Provides theoretical guarantees and demonstrates +1.8% gain in auxiliary objectives at zero cost to user satisfaction.
- **Key Innovations**: Inference-time multiobjective optimization; stochastic primal-dual approximation; theoretical constraint violation bounds.
- **Impact**: Enables multi-objective recommendation without model retraining.
- **Link**: arXiv:2607.19357

---

## 3. Long-Context & Efficiency

### 3.1 LISA: Linear-Indexed Sparse Attention for Efficient Long-Context Reasoning
- **Authors**: Yu Zhao, Zekun Zhang, Fan Jiang, Bo Zeng, et al.
- **Date**: 23 Jul 2026
- **Abstract**: Proposes LISA, a plug-and-play attention replacement module that reduces inference complexity from O(n²) to O(nM) where M << n. Combines Linear Attention for long-range memory with a Lightning Indexer for selecting top-M important tokens. Two-stage training pipeline with knowledge distillation. Achieves 50% inference speedup under 16K-token context with +5.6% average performance improvement on reasoning benchmarks.
- **Key Innovations**: Linear-Indexed Sparse Attention; per-head KL divergence loss for indexer training; no pretraining required.
- **Impact**: Enables practical deployment of long-CoT reasoning models in production.
- **Link**: arXiv:2607.19358

### 3.2 FineServe: Fine-Grained Dataset and Characterization of Global LLM Serving Workloads
- **Authors**: Tiancheng Zhang, Shaoyuan Huang, Mingyuan Wang, et al.
- **Date**: 23 Jul 2026
- **Abstract**: Presents FineServe, an in-the-wild multi-model LLM serving workload dataset from a global commercial marketplace. Conducts comprehensive analysis of arrival dynamics and token behavior, revealing fundamentally different fluctuation regimes across model architectures, scales, and task intents.
- **Key Innovations**: Real-world multi-model workload characterization; fine-grained model-aware workload generator.
- **Impact**: Provides realistic foundation for evaluating routing, scheduling, and capacity-planning strategies.
- **Link**: arXiv:2607.19349

---

## 4. Reasoning & Mathematics

### 4.1 FormulaSPIN: Self-Play Fine-Tuning for Natural Language to Spreadsheet Formula Generation
- **Authors**: Cy Xie
- **Date**: 23 Jul 2026 (ACL 2026 Main Conference Oral)
- **Abstract**: Introduces FORMULASPIN, a self-play framework that breaks the ceiling of supervised fine-tuning for spreadsheet formula generation. Exploits binary executability as implicit supervision to separate semantic errors from valid stylistic variants. Achieves 74.9% exact match and 87.1% execution accuracy on NL2FORMULA benchmark.
- **Key Innovations**: Execution-guided self-play; adaptive curriculum from semantic to stylistic refinement; ExecVote semantic-level voting.
- **Impact**: Extends self-play paradigm beyond games to executable domains withscarce data.
- **Link**: arXiv:2607.19354

### 4.2 AdaRoPE: Not All Attention Heads Should Rotate and Scale Equally
- **Authors**: Shaowen Wang, Yuke Zheng, Tansheng Zhu, et al.
- **Date**: 23 Jul 2026 (ICML 2026)
- **Abstract**: Shows that different attention heads require distinct frequency ranges and scaling factors for optimal performance. Proposes AdaRoPE with learnable rotation frequencies and attention scaling factors per head. Outperforms existing RoPE variants including YaRN for context extension.
- **Key Innovations**: Per-head learnable rotary frequencies; head-specific attention scaling; better context extension while preserving short-context performance.
- **Impact**: Improves long-context performance in pretrained LLMs without architectural changes.
- **Link**: arXiv:2607.19363

---

## 5. Recommendation Systems

### 5.1 UniRank: Benchmarking Ranking Models for Unified Sequential Modeling and Feature Interaction
- **Authors**: Honghao Li, Xianquan Wang, Zibin Zhang, Yi Zhang, Kangyi Lin, Yiwen Zhang
- **Date**: 23 Jul 2026
- **Abstract**: Introduces a comprehensive benchmark for evaluating ranking models that unify sequential modeling and feature interaction capabilities.
- **Key Innovations**: Unified benchmark framework; systematic evaluation of sequential + feature interaction models.
- **Impact**: Provides standardized evaluation for next-generation recommendation architectures.
- **Link**: arXiv:2607.19987

### 5. Zero-Observation User Reactivation with Gap-Driven Dimensional Gating
- **Authors**: Jiandong Ding, Tianying Liu, Fuyuan Liu, Huijie Qin, Tiandeng Wu
- **Date**: 23 Jul 2026 (RecSys 2026)
- **Abstract**: Proposes a method for reactivating users with zero observation history using gap-driven dimensional gating mechanisms.
- **Key Innovations**: Zero-shot user reactivation; gap-driven feature selection for cold-start scenarios.
- **Impact**: Addresses cold-start problem in recommendation systems without requiring user interaction history.
- **Link**: arXiv:2607.19802

---

## 6. LLM Applications

### 6.1 Information Discernment in Large Language Models
- **Authors**: Joshua Ashkinaze, Laura Kurek, Alina Faisal, et al.
- **Date**: 23 Jul 2026
- **Abstract**: Studies how LLMs weigh information from external sources, formalizing information discernment along source and truth axes. Across 13 models and 670K trials, finds consistent failures: models perform near chance on discernment, rely on source popularity over reliability, and update roughly equally whether claims improve or worsen their position.
- **Key Innovations**: Learn2Discern experimental framework; three normative axioms with interpretable metrics; identification of inference-time interventions.
- **Impact**: Reveals fundamental limitations in LLM information integration with implications for search and retrieval.
- **Link**: arXiv:2607.19355

### 6. Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles
- **Authors**: Shengtong Zhu
- **Date**: 23 Jul 2026
- **Abstract**: Introduces MemHop, a multi-hop memory benchmark with 1,000 questions at hop depths 1-5. Proposes Profile-Graph Memory (ProGraph) combining profile expansion through substring-matched traversal with compression residuals. Achieves 80.1% on MemHop and 78.4% on LoCoMo, outperforming Mem0, A-Mem, HippoRAG, and RAG.
- **Key Innovations**: Multi-hop memory benchmark; profile expansion without explicit knowledge graphs; co-extracted compression residuals.
- **Impact**: Enables sophisticated multi-hop reasoning in LLM agent memory systems.
- **Link**: arXiv:2607.19359

---

## Summary

### Key Themes

1. **CTR Scaling Laws Continue**: Multiple papers demonstrate that CTR models benefit from scaling, with DeRes showing steeper compute-AUC curves and Long-History Transformers proving offline-online decoupling works in production.

2. **Simplicity Wins**: DS-MLP shows vanilla MLP architectures can achieve SOTA, challenging the trend toward increasingly complex models.

3. **Agent Safety Maturing**: NEXUS and OpenEvoShield address practical safety concerns for tool-using agents with minimal overhead.

4. **Long-Context Efficiency**: LISA achieves 50% speedup on long-context reasoning, making production deployment feasible.

5. **Uncertainty Matters**: Epistemic click models provide uncertainty estimates, moving beyond point predictions.

6. **Self-Play Beyond Games**: FormulaSPIN extends self-play to executable domains, showing promise for scarce-data tasks.

### Statistics
- **Total Papers Reviewed**: 25+
- **CTR/Recommendation**: 8 papers
- **AI Agents & Safety**: 5 papers
- **Long-Context & Efficiency**: 4 papers
- **Reasoning & Mathematics**: 3 papers
- **LLM Applications**: 5 papers

---

*Generated on 2026-07-23*
