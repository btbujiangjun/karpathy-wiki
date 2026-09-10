---
title: "arXiv Paper Check — AI & CTR (September 10, 2026)"
type: synthesis
created: 2026-09-10
updated: 2026-09-10
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, agents, reasoning, rl, llm, efficiency, evaluation, memory, cikm-2026, emnlp-2026, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 10, 2026)

**Scan date**: Thu, 10 Sep 2026 (arXiv Thu mailing)
**Categories scanned**: cs.AI (150 entries), cs.IR (11 entries), cs.LG (163 entries)
**CTR/recommendation papers today**: 0 direct CTR papers; 3 rec-adjacent papers (CIKM'26 feature transformation, PACE dialogue serving, ALIGN-HOLD ride-hailing)
**Dedup**: All IDs grep-verified 0 hits in `wiki/`. Excludes same-day siblings (arxiv-ai-search, arxiv-daily) — 0 overlap.

---

## LLM Agents & Memory (6 papers)

### 1. JarvisGUI: Cross-Device GUI Agents with Dynamic Task Composition
- **arXiv**: [2609.10451](https://arxiv.org/abs/2609.10451)
- **Authors**: Zixiang Chen, Yuheng Lu, Zihao Cheng, Zeming Liu, Jizeng Bai, Ziye Huang, Zhiyin Lin, Zihan Li, Yuhang Guo, Yunhong Wang, Haifeng Wang
- **Venue**: EMNLP 2026 Main Conference
- **Key contribution**: Dynamic task composition framework for cross-device GUI agents — enables seamless multi-app task execution across phone/tablet/desktop by decomposing complex goals into device-specific subtasks with cross-device state transfer.

### 2. ConvMem: Convolutional Memory for Long-Context Reasoning
- **arXiv**: [2609.10441](https://arxiv.org/abs/2609.10441)
- **Authors**: Hongming Zhang, Zhaozhen Gu, Fengshuo Bai, Ming Hao, Qingyang Zhang, Yuanyuan Wang, Shiyang Tang, Yanna Wang, Bo Xu
- **Subjects**: cs.AI; cs.CL
- **Key contribution**: Applies convolutional operations over memory representations for long-context reasoning — a novel architectural choice that localizes context aggregation via sliding-window convolutions over stored KV states, potentially offering better length generalization than attention-based memory.

### 3. Fortunate Recall: Ontology-Driven Memory Lifecycle Management for Persistent Coherence in LLMs
- **arXiv**: [2609.10413](https://arxiv.org/abs/2609.10413)
- **Authors**: Ansuman Mullick, Eray Tüzün
- **Key contribution**: Proposes ontology-driven lifecycle management for LLM agent memories — automatically decides when to consolidate, forget, or restructure stored memories based on an evolving ontology graph, maintaining coherence over long deployments.

### 4. What Should an Agent Forget? Separating What Is Stored from What Is Used
- **arXiv**: [2609.10263](https://arxiv.org/abs/2609.10263)
- **Authors**: Yuhang Li, Yuchen Li
- **Key contribution**: Formalizes the distinction between stored memory and actively used memory in LLM agents, proposing evaluation protocols that measure whether agents correctly selective-access relevant memories while suppressing irrelevant stale ones.

### 5. PRAGMA: Evaluating Personalized Guidance with Memory Alignment in Lifelong Conversations
- **arXiv**: [2609.09664](https://arxiv.org/abs/2609.09664)
- **Authors**: Hyojeong Yu, Hyukhun Koh, Minsung Kim, Yunah Jang, Kyomin Jung
- **Venue**: EMNLP 2026
- **Key contribution**: Benchmarks personalized guidance in lifelong conversations by measuring how well agents align their responses with user-specific memory, introducing alignment metrics for memory-grounded dialogue.

### 6. RobustSGPO: Search-Space Control for Agent Harness Evolution
- **arXiv**: [2609.09646](https://arxiv.org/abs/2609.09646)
- **Authors**: Zibo Zhao, Jijun Shi, Mo Zhou, Zhongyuan Wang, Shifu Bie, Yunfei Zhang, Xuanting Zhou, Xiangyu Wu, Bin Liu, Ruiming Tang, Wenwu Ou, Kun Gai
- **Key contribution**: Controls the search space during agent self-evolution, preventing skill space explosion while maintaining performance — addresses the practical problem that evolving agents accumulate redundant capabilities.

---

## Reasoning & Post-Training (3 papers)

### 7. Structural Process Supervision for Latent Chain-of-Thought Reasoning
- **arXiv**: [2609.09928](https://arxiv.org/abs/2609.09928)
- **Authors**: Yiqi Li, Xu Chen, Chen Ju, Jiangchao Yao, Zhaoyang Li, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Yu Wang
- **Key contribution**: Introduces structural process supervision (SPS) for latent-space chain-of-thought — trains models to produce structured reasoning traces in latent space rather than token space, enabling reasoning with lower inference overhead while maintaining logical consistency.

### 8. Which Tokens Should SFT Actually Learn? A Token-Trimming Perspective on Mathematical Reasoning
- **arXiv**: [2609.09707](https://arxiv.org/abs/2609.09707)
- **Authors**: Yaning Jia, Chunhui Zhang, Wenxuan Xu, Xingjian Diao, Xiaoyuan Wang, Soroush Vosoughi
- **Venue**: Findings of EMNLP 2026
- **Key contribution**: Demonstrates that SFT for mathematical reasoning should selectively focus on a small subset of "high-value" tokens rather than uniform supervision — proposes token-trimming strategies that identify which tokens carry actual learning signal.

### 9. RobustSGPO: Search-Space Control for Agent Harness Evolution
- *(Listed above under Agents)*

---

## LLM Efficiency & Infrastructure (4 papers)

### 10. UnitBoost: Managing Compound LLM Systems with a Merge Operator, Not a Model
- **arXiv**: [2609.09815](https://arxiv.org/abs/2609.09815)
- **Authors**: Xing Zhang, Guanghui Wang, Yanwei Cui, Mengdie Flora Wang, Peiyang He
- **Subjects**: cs.AI; cs.CL; cs.MA
- **Key contribution**: Proposes a merge operator for combining multiple specialized LLMs into compound systems without training a new joint model — enables dynamic composition of expert models at inference time, reducing the maintenance burden of model portfolios.

### 11. Fine-Tuning a KV Cache Concatenation-Aware Model or Recomputing KV Caches? Why Not Both?
- **arXiv**: [2609.09768](https://arxiv.org/abs/2609.09768)
- **Authors**: Fumihiko Tachibana, Daisuke Miyashita, Jun Deguchi
- **Key contribution**: Studies the trade-off between fine-tuning models to tolerate KV cache concatenation artifacts versus recomputing from scratch — proposes a hybrid approach that selectively recomputes for sensitive attention heads while concatenating for robust ones.

### 12. Forward-Free LLM Depth Pruning via Weight Redundancy
- **arXiv**: [2609.09883](https://arxiv.org/abs/2609.09883)
- **Authors**: Vincent-Daniel Yun, Woosang Lim
- **Key contribution**: Enables depth pruning of LLMs without any forward pass by analyzing weight redundancy patterns — identifies and removes redundant layers purely from weight statistics, offering a zero-cost pruning methodology.

### 13. Forgetting Only What Matters: Layer-Selective Unlearning toward Robust LLMs
- **arXiv**: [2609.10439](https://arxiv.org/abs/2609.10439)
- **Authors**: Ravi Ranjan, Olivera Kotevska, Agoritsa Polyzou
- **Venue**: AACL-IJCNLP 2026
- **Key contribution**: Layer-selective unlearning that targets specific knowledge layers while preserving general capabilities — demonstrates that unlearning is not uniform across layers, enabling surgical forgetting with minimal capability loss.

---

## Semigroup-JEPA: Latent Dynamics Consistency for Zero-Shot Physics Generalization

- **arXiv**: [2609.10464](https://arxiv.org/abs/2609.10464)
- **Authors**: Andy Zeyi Liu, Haoran Sun, Lucas Baker, Randall Balestriero, John Sous
- **Key contribution**: Applies semigroup theory to JEPA (Joint Embedding Predictive Architecture) for enforcing latent dynamics consistency — enables zero-shot generalization to unseen physics regimes by constraining the learned latent space to obey semigroup composition laws.

---

## Rec-Adjacent & Industrial (3 papers)

### 14. Hierarchical and Permutation-Invariant Feature Transformation Learning via Policy-Guided Embedding Search
- **arXiv**: [2609.10225](https://arxiv.org/abs/2609.10225)
- **Authors**: Rui Liu, Tao Zhe, Yanyong Huang, Sankha Narayan Guria, Xiao Luo, Wei Fan, Yanjie Fu, Dongjie Wang
- **Venue**: CIKM 2026
- **Key contribution**: Policy-guided embedding search for hierarchical feature transformation — addresses permutation-invariant feature processing in tabular/ranking settings, potentially applicable to CTR feature engineering.

### 15. PACE: Perceived-Latency-Aware Cascading Service Routing for QoE-Efficient Retrieval-Augmented Dialogue Serving
- **arXiv**: [2609.10372](https://arxiv.org/abs/2609.10372)
- **Authors**: Lin Huang, Yujuan Tan, Weisheng Li, Lixiang Zeng, Kun Yang, Suihan Xiao
- **Key contribution**: Cascading retrieval strategy that routes queries to different RAG backends based on perceived latency sensitivity — balances answer quality and response time for dialogue systems with QoE constraints.

### 16. ALIGN-HOLD: Experience Alignment for Real-Time Hold Control in Large-Scale Ride-Hailing Matching at DiDi
- **arXiv**: [2609.09685](https://arxiv.org/abs/2609.09685)
- **Authors**: Zuhao Zhang, Xu Liu, Kai Wan, Zihao Lu, Li Ma, Shuai Li
- **Key contribution**: Industrial-scale ride-hailing matching with hold control — aligns driver experience expectations with real-time demand, demonstrating large-scale online optimization techniques applicable to similar ranking/matching problems.

---

## LLM Self-Knowledge & Calibration (2 papers)

### 17. Strangers to Themselves: What Language Models Say About Themselves Is Generic
- **arXiv**: [2609.09899](https://arxiv.org/abs/2609.09899)
- **Authors**: Phil Blandfort, Urja Pawar
- **Key contribution**: Shows that LLM self-descriptions are generic and interchangeable across models — challenges the notion that models have unique self-knowledge, with implications for alignment and persona-based applications.

### 18. Can Foundation Models Moderate Online Content? Evaluating Instruction- vs. Example-Driven Policy Operationalization
- **arXiv**: [2609.10410](https://arxiv.org/abs/2609.10410)
- **Authors**: Ayan Majumdar, Shounak Paul, Pushpdeep Singh, Ines Abdelaziz, Sayeh Jarollahi, Seungeon Lee, Krishna P. Gummadi, Ingmar Weber, Abhisek Dash
- **Key contribution**: Compares instruction-driven vs. example-driven approaches for operationalizing content moderation policies in foundation models, finding significant performance gaps depending on policy presentation format.

---

## Summary & Key Themes

| Theme | Papers | Signal |
|-------|--------|--------|
| **Agent Memory Lifecycle** | 2609.10413, 2609.10263, 2609.09664 | Memory management (consolidation, forgetting, alignment) emerges as a first-class engineering concern for persistent agents |
| **Agent Evolution Control** | 2609.09646 | Preventing capability bloat during agent self-improvement |
| **Long-Context Memory** | 2609.10441 | Convolutional approaches to memory aggregation as alternative to attention |
| **Reasoning in Latent Space** | 2609.09928 | Moving CoT to latent space for efficiency |
| **SFT Token Selection** | 2609.09707 | Not all tokens are equal — selective supervision outperforms uniform |
| **Model Merging** | 2609.09815 | Compose specialized LLMs without retraining |
| **Zero-Shot Physics** | 2609.10464 | Semigroup-constrained JEPA for physical reasoning |
| **Rec-Adjacent** | 2609.10225 (CIKM'26), 2609.10372 | Feature transformation for ranking; QoE-aware retrieval routing |

**CTR-specific**: Zero new papers directly targeting CTR prediction in this window. The rec-adjacent papers (feature transformation, ride-hailing matching) share methodological overlap with CTR systems but do not address click-through rate explicitly.

**Notable absent**: No new scaling law papers, no new MoE architectures, no new RLVR post-training papers today — a relatively quiet day for CTR-specific research compared to the Sep 4–7 wave.

---

*Generated: 2026-09-10 | Source: arXiv list/cs.AI, cs.IR, cs.LG (Thu, 10 Sep 2026 mailing) | opencode-compiled*
