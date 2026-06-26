---
title: "arXiv Paper Check — 2026-06-26"
type: synthesis
created: 2026-06-26
updated: 2026-06-26
sources: []
tags: [arxiv, ai, ctr, recommendation, llm, daily]
---

# arXiv Paper Check — 2026-06-26

> Scan of new listings for Thursday, 25 Jun 2026 across cs.IR, cs.LG, cs.AI. Total: 9 new cs.IR + 186 new cs.LG + 182 cs.AI entries.

---

## CTR / Recommendation / IR

### 1. TokenMinds: Pretrained User Tokens and Embeddings for User Understanding in Large Recommender Systems
- **Authors**: Qingyun Liu, Bo Yan, Yang Liu et al. (Google DeepMind, YouTube)
- **arXiv**: 2606.25147
- **Key contribution**: First large-scale deployment of Semantic ID (SID)-based discrete user tokens alongside dense embeddings at YouTube scale (billions of users). Shared SID vocabulary across long-form and short-form video unifies cross-scenario modeling. Validated via live launch on multiple YouTube surfaces.

### 2. Adaptive Re-Ranking
- **Authors**: Cinar Genc, Emir Kaan Korukluoglu, James Allan (UMass Amherst)
- **arXiv**: 2606.25249 | ICTIR 2026
- **Key contribution**: Utility-based query routing between BM25, MiniLM-L6-V2 dense, and BGE-v2-m3 heavy re-rankers. Achieves 1.15–53× lower median latency with nDCG@10 ranging from -17.5% to +4.0% vs always-using BGE. Learned router generalizes to unseen domains.

### 3. Graph-GRPO: Dependency-Aware Credit Assignment for Generative E-commerce Search Relevance
- **Authors**: (JD.com)
- **arXiv**: 2605.31003
- **Key contribution**: Extends GRPO with graph-structured credit assignment for CoT-based relevance reasoning. Models reasoning steps as dependency graph nodes, propagates outcome rewards for step-level credit. Deployed on JD e-commerce search serving hundreds of millions of users.

### 4. GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Authors**: (JD.com)
- **arXiv**: 2604.14878 | SIGIR 2026
- **Key contribution**: Decoder-only generative recommendation with Page-wise NTP training, asymmetric linear Token Merger for 2× input compression, and GRPO-SR (RL alignment with hybrid rewards). Deployed on JD App homepage: +9.5% clicks, +8.7% transactions in month-long A/B test.

### 5. GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction
- **Authors**: (WWW 2026)
- **arXiv**: 2601.18251
- **Key contribution**: Generative user intent framework using semantic interest cohorts for CTR. NTP-trained generative model produces candidate-agnostic intent representations; hierarchical cross-attention refines them. Addresses interest shift and point-wise ranking misalignment.

### 6. GenLI: Generative Long-term User Interest Modeling for CTR Prediction
- **Key contribution**: Interest generation module (target-independent), behavior retrieval (O(1) lookup), and interest fusion with gating. Deployed in real-world platform serving hundreds of millions of users. Avoids time-consuming pairwise matching in long-sequence retrieval.

### 7. Gryphon: A Unified Architecture for Semantic-ID Generation and Item-Level Scoring
- **Key contribution**: Encoder-decoder GR with item-level scoring to fix beam-search miscalibration and SID collisions. Replaced 15+ candidate generators in industrial music service A/B test with no significant listening-time change. Reduces candidate pipeline complexity.

### 8. DSIRM: Learning Query-Bridged Discrete Semantic Identifiers for E-commerce Relevance Modeling
- **Authors**: (CIKM 2026)
- **arXiv**: 2606.04374
- **Key contribution**: Relevance-aware quantization with query-item interaction supervision for SID learning. Hierarchical prefix matching between query and item SIDs for tail query handling. +1.54% UCTR, +0.25% UCTCVR on Alibaba production data.

### 9. Beyond Matching: Category-Guided Latent Intent Reasoning for Generative Retrieval in E-Commerce
- **Authors**: Fuwei Zhang et al. (Beihang Univ., Meituan)
- **arXiv**: 2606.07075
- **Key contribution**: Category-guided latent intent reasoning using chain-of-thought, with query-specific dynamic prefix trie and reasoning-aware constrained decoding. Improves generative retrieval on multilingual e-commerce search.

---

## AI / LLM / ML

### 10. Autodata: An Agentic Data Scientist to Create High Quality Synthetic Data
- **Authors**: (June 25, 2026)
- **arXiv**: 2606.25996
- **Key contribution**: AI agent that acts as a data scientist — generates synthetic data, evaluates with task-specific signals, and iteratively improves. Meta-optimization of the data scientist agent itself yields further gains. Tested on CS research, legal reasoning, and mathematical reasoning tasks.

### 11. Pigeonholing: Bad Prompts Hurt Models to Collapse and Make Mistakes
- **Authors**: Hyunji Alex Nam et al.
- **arXiv**: 2606.24267 | June 23
- **Key contribution**: Identifies "pigeonholing" — performance degradation from unintentionally bad contexts (user suggesting incorrect solutions, assistant repeating own errors). 38–40% performance drop. Proposes RLVR with synthetic errors as mitigation, improving robustness by 43–60%.

### 12. Abstract Representational Geometry Supports Inference in Large Language Models
- **Authors**: Yunan Zeng, Yuwang Wang
- **arXiv**: 2606.23345 | June 22
- **Key contribution**: LLMs form hippocampal-like abstract geometric representations in higher layers that support inference. Lower layers encode stimulus identity; higher layers show abstract context geometry. Geometric regularization of higher layers increases generalizable inference.

### 13. Active Inference as the Test-Time Scaling Law for Physical AI Agents
- **Authors**: Omar Hashash et al.
- **arXiv**: 2606.22813 | June 22
- **Key contribution**: Derives test-time scaling law for physical AI from active inference first principles. Variational inference minimizes free energy bounds. Outperforms Q-learning and Bayesian RL on autonomous driving, with 36% better inference efficiency in unforeseen scenarios.

### 14. An Introduction to Causal Reinforcement Learning
- **Authors**: Elias Bareinboim, Junzhe Zhang, Sanghack Lee
- **arXiv**: 2606.24160 | June 23
- **Key contribution**: Unifying framework connecting causal inference and RL. Introduces generalized policy learning, where-to-intervene, imitation learning, and counterfactual learning under a single causal lens. Foundational paper for the CRL field.

### 15. Words as Difference Makers: How Large Language Models Determine Causal Structure in Text
- **Authors**: Wolfgang Pietsch
- **arXiv**: 2606.22430 | June 21
- **Key contribution**: Argues LLMs use "variational induction" (difference-making logic) rather than Pearl's interventionist causality to learn causal structure. Analyzes token embeddings and self-attention's roles in variational induction.

### 16. Convergence of Gradient Descent for General Neural Network Architectures Beyond the NTK Regime
- **Authors**: Yuqing Wang et al.
- **arXiv**: 2606.23364 | June 22
- **Key contribution**: Convergence framework for GD on broad family of architectures (including pre-normalized transformers) beyond NTK regime. Learning rate depends on depth and bottleneck dimensions, not largest width. Covers residual connections and function composition.

### 17. Extreme Meta-Classification for Large-Scale Zero-Shot Retrieval
- **arXiv**: 2606.25237 | (KDD 2024 replacement)
- **Key contribution**: Meta-classification approach for zero-shot retrieval at scale.

### 18. Temporal Preference Optimization for Unsupervised Retrieval
- **Authors**: HyunJin Kim et al.
- **arXiv**: 2606.17664 | June 17
- **Key contribution**: TPOUR — preference optimization for temporal alignment in dense retrievers without explicit timestamps. 72.7× smaller than Qwen-Embedding-8B yet +4.04 nDCG@5 on temporal IR tasks.

### 19. Scalable Maximum Entropy RL for Diffusion Policies via Adjoint Matching
- **Authors**: Serge Thilges et al.
- **arXiv**: 2606.22630 | June 21
- **Key contribution**: Simulation-free training for diffusion policies in online RL via adjoint matching. Avoids costly backprop through diffusion process. Competitive performance with significantly reduced compute.

### 20. Closing the Indexing-Decoding Gap in Multimodal Generative Retrieval via Prefix Retention Optimization (PRO)
- **arXiv**: 2606.09241
- **Key contribution**: Formalizes indexing-decoding gap in MGR. Prefix ranking distillation, vocabulary scheduling, and geometric score fusion. Improves prefix survival and retrieval quality across 9 multimodal retrieval tasks.

---

## Key Themes

1. **GRPO/RL for recommendation**: Graph-GRPO (JD), GenRec GRPO-SR — RL alignment with structured credit assignment becoming standard in e-commerce generative retrieval.
2. **Semantic IDs dominate**: TokenMinds, Gryphon, DSIRM, GenRec — SID-based discrete representations spreading from items to users, with shared vocabularies across scenarios.
3. **Generative CTR models**: GenCI, GenLI — moving from discriminative matching to generative interest modeling with LLM-style objectives.
4. **Agentic AI safety**: Agentic surveillance evasion, pigeonholing (prompt robustness), Autodata (agentic data creation) — agent capabilities and failure modes are a growing focus.
5. **Mechanistic interpretability bridges neuroscience**: Abstract representational geometry in LLMs parallels hippocampal representations — cross-disciplinary convergence.
6. **Test-time compute scaling**: Active inference as scaling law for physical agents — extending the test-time compute paradigm beyond language.
