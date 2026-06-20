---
title: "arXiv Paper Check — AI & CTR (June 20, 2026)"
type: synthesis
created: 2026-06-20
updated: 2026-06-20
sources: []
tags: [arxiv, ai, ctr, recommendation, ir, llm]
---

# arXiv Paper Check — AI & CTR (June 20, 2026)

> New submissions from Friday, June 19, 2026. cs.AI: 73 new (312 total) | cs.IR: 11 new (22 total).

## Top Picks

### 1. ITNet: A Learnable Integral Transform That Subsumes Convolution, Attention, and Recurrence
- **Authors**: Ashim Dhor, Rasel Mondal, Pin Yu Chen
- **arXiv**: 2606.19538
- **Key contribution**: Proposes a unified architecture (Integral Transform Network) built around a learnable kernel implemented as an MLP that models pairwise interactions. Shows convolution, self-attention (multi-head), and autoregressive recurrence (LSTM, GRU, S4, Mamba) arise as special cases. Develops tiled kernel fusion, importance-weighted Monte Carlo integration, and learned low-rank factorization for efficiency. Matches or exceeds specialized baselines on ImageNet-1K, GLUE, ModelNet40, VQA-v2, and NLVR2 with a single architecture.

### 2. Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning
- **Authors**: Xuanzhi Feng, Zhengyang Li, Zeyu Liu, Haoxi Li, Yuming Jiang, Bing Guo, Jingcai Guo, Jie Zhang, Song Guo
- **arXiv**: 2606.19771
- **Key contribution**: Proposes learning from token-level distributional deviations for LLM reasoning beyond simple entropy-based methods. Addresses how to extract richer signals from the model's internal token distributions during reasoning.

### 3. Token Factory: Efficiently Integrating Diverse Signals into Large Recommendation Models
- **Authors**: Xilun Chen, Shao-Chuan Wang, Baykal Cakici, Lukasz Heldt, Lichan Hong, Raghu Keshavan, Aniruddh Nath, Li Wei, Xinyang Xi (Google)
- **arXiv**: 2606.19635
- **Key contribution**: Proposes a framework to transform traditional recommendation signals into "soft tokens" that LRMs can process directly. Prevents prompt length explosion while enhancing model performance in production-scale recommendation environments.

### 4. G2Rec: Structuring and Tokenizing Distributed User Interest Context for Generative Recommendation
- **Authors**: Ruizhong Qiu, Yinglong Xia, Dongqi Fu, Hanqing Zeng, Ren Chen, Xiangjun Fan, Hong Li, Hong Yan, Hanghang Tong
- **arXiv**: 2606.20554
- **Key contribution**: A scalable framework unifying holistic graph-based user co-engagement modeling with semantic tokenization for industrial-scale generative recommendation. Enables capturing holistic and semantically grounded user interest prototypes. Demonstrates superiority in online deployment and public datasets.

### 5. Which Pairs to Compare for LLM Post-Training?
- **Authors**: Jiangze Han, Vineet Goyal, Will Ma
- **arXiv**: 2606.19607
- **Key contribution**: Studies comparison curation for preference-based LLM post-training as a sampling-design problem. Provides matching upper/lower bounds on DPO-trained policy optimality gap, linking label allocation to parameter estimation error. Proposes practical sampling designs for selecting informative pairs from large completion pools.

### 6. ELVA: Exploring Ranking-Driven Universal Multimodal Retrieval
- **Authors**: Yuhan Liu, Pei Fu, Hang Li, Yukun Qi, Chao Jiang, Jingwen Fu, Zhen Liu, Bin Qin, Zhenbo Luo, Jian Luan, Jingmin Xin
- **arXiv**: 2606.20280 (ECCV 2026)
- **Key contribution**: Introduces RLVR (RL with Verifiable Rewards) to retrieval tasks. Mitigates "grain blindness" in contrastive learning by treating negatives differently based on similarity. Jointly optimizes ranking of negative samples while enlarging positive-negative gap. Introduces MRBench for multi-grain query scenarios. SOTA on standard retrieval + 13.1% on MRBench.

### 7. DIF: Denoising Implicit Feedback for Cold-start Recommendation
- **Authors**: Gaode Chen, Shicheng Wang, Shikun Li, Rui Huang, Xinghua Zhang, Yunze Luo, Shipeng Li, Shiming Ge, Ruina Sun, Yinjie Jiang, Jun Zhang
- **arXiv**: 2606.19658 (KDD 2026 ADS Track, deployed at Kuaishou)
- **Key contribution**: Identifies that cold items are more prone to noisy implicit feedback. Proposes model-agnostic denoising using pseudo-labels from content-similar warm items and uncertainty estimation via relative entropy and cold-start status. Deployed at Kuaishou (billion-user scale) with significant commercial metric improvements.

### 8. VCG: A Multimodal Retrieval Framework for E-Commerce Video Feeds under Extreme Cold-Start Conditions
- **Authors**: Katya Mirylenka, Egor Malykh, Mahdyar Ravanbakhsh, Michael Gygli, Marco-Andrea Buchmann et al.
- **arXiv**: 2606.19627
- **Key contribution**: Domain-adapted CLIP-based multimodal retrieval engine for e-commerce video feeds. Shows generative models excel at attribute prediction but suffer from embedding space collapse in retrieval. Online A/B testing shows 50% uplift in deep video completion via engagement bias mitigation.

### 9. MonaVec: A Training-Free Embedded Vector Search Kernel for Edge and Offline AI Systems
- **Authors**: Oğuzhan Yenen
- **arXiv**: 2606.19458
- **Key contribution**: Training-free, data-oblivious vector search with Randomized Hadamard Transform conditioning + precomputed Lloyd-Max quantization (4-bit, 8× smaller). Targets SQLite-like deployment profile. Achieves 0.960 Recall@10 in 27 MB on AG News (45K × 1024-dim). Byte-identical determinism across architectures.

### 10. Diffusion Language Models: An Experimental Analysis
- **Authors**: Thomas Bertolani, Davide Bucciarelli, Leonardo Zini, Marcella Cornia, Lorenzo Baraldi
- **arXiv**: 2606.19475
- **Key contribution**: Systematic experimental analysis of 8 state-of-the-art DLMs across 8 benchmarks (reasoning, coding, translation, knowledge, structured problem solving). Analyzes impact of denoising steps, context length, block size, and parallel unmasking. Shows DLM behavior is strongly influenced by generation-time design choices with distinct performance-efficiency trade-offs.

### 11. Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents
- **Authors**: Dhaval C. Patel et al. (large collaborative study)
- **arXiv**: 2606.19704
- **Key contribution**: Largest coordinated deep-dive of one MCP-based industrial agent benchmark (14 parallel implementation studies). Argues aggregate-score leaderboards systematically underspecify deployed-agent evaluation. Proposes ranking by predictive validity (correlation between in-sample and out-of-sample rank) rather than in-sample mean.

### 12. Benchmarking Agentic Review Systems
- **Authors**: Dang Nguyen, Wanqing Hao, Yanai Elazar, Chenhao Tan
- **arXiv**: 2606.19749
- **Key contribution**: Evaluates two open-source and one proprietary AI review systems across 6 LLMs. Best system (OpenAIReview + GPT-5.5) achieves 83.0% pairwise accuracy for tracking paper quality and catches 71.6% of injected errors. Union across 6 models reaches 83.3% recall. Real-user deployment shows positive skew (1.44:1 positive-to-negative vote ratio).

### 13. SLARouter: Cost-Optimal LLM Routing with Limited User Feedback
- **Authors**: Herbert Woisetschläger, Arastun Mammadli, Ryan Zhang, Shiqiang Wang
- **arXiv**: 2606.19376 (cross-list cs.LG → cs.IR)
- **Key contribution**: Online routing algorithm learning cost-optimal policy from sparse, one-sided user feedback with theoretical guarantees for cost optimality and strict SLA compliance. Reduces operating cost by up to 2.2× over baselines without per-benchmark tuning.

### 14. ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search
- **Authors**: Tingyue Pan, Mingyue Cheng, Daoyu Wang, Yitong Zhou, Jie Ouyang, Qi Liu, Enhong Chen
- **arXiv**: 2606.20235
- **Key contribution**: Large-scale benchmark from 1,000+ CS topics with 4 research intents (method-oriented, setting-anchored, comparison-based, scope-controlled). Provides shared retrieval backend ScholarBase. Best agent only achieves 0.314 Recall@100, showing substantial room for improvement.

### 15. Closing the Calibration Gap in Semantic Caching
- **Authors**: Aditeya Baral, Radoslav Ralev, Iliya Sotirov Zhechev, Srijith Rajamohan, Jen Agarwal
- **arXiv**: 2606.19719
- **Key contribution**: Shows PR-AUC is misleading for semantic caching evaluation. Introduces P-CHR AUC (cache-aware precision across utilization levels) and Calibration Retention Rate. Decomposes offline-to-deployed quality gap into recoverable calibration vs irreducible structural components.

## Summary Statistics

| Category | New | Highlight |
|----------|-----|-----------|
| LLM Architecture & Training | 10+ | ITNet (unified integral transform), Diffusion LMs experimental analysis |
| LLM Reasoning & Alignment | 5+ | Beyond Entropy, Which Pairs to Compare, Emergent Alignment |
| Recommendation & CTR | 7+ | Token Factory, G2Rec, DIF (Kuaishou), VCG |
| Retrieval & IR | 6+ | ELVA (RLVR for retrieval), MonaVec, Stellar, ScholarQuest |
| Agent Systems | 8+ | Predictive Validity benchmark, Agentic Review Systems, Deontic Policies |
| LLM Inference & Routing | 3+ | SLARouter, Semantic Caching Calibration |
| Domain Applications | 5+ | Clinical IE with Agentic RAG, Brain MRI generation, Quranic ASR |

## Key Themes

- **Unified architectures**: ITNet subsumes conv/attention/recurrence under a single learnable integral transform — a potential paradigm-shifting insight
- **Generative recommendation productionization**: Token Factory (Google) and G2Rec show the industrial path from research to deployment
- **RLVR extends to retrieval**: ELVA applies verifiable-reward RL to multimodal retrieval, achieving SOTA
- **Cold-start & denoising**: DIF (Kuaishou, KDD 2026) addresses the overlooked cold-start denoising problem in production
- **Agent evaluation rethought**: Beyond Static Leaderboards and Agentic Review Systems both challenge how we measure agent capabilities
- **Cost-aware LLM inference**: SLARouter and Semantic Caching Calibration address the growing inference-cost problem with principled approaches
- **Diffusion LMs under scrutiny**: First systematic comparison of 8 DLM architectures across diverse benchmarks
