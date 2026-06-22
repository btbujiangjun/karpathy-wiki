---
title: "arXiv Paper Check — AI & CTR (June 22, 2026)"
type: synthesis
created: 2026-06-22
updated: 2026-06-22
sources: []
tags: [arxiv, ai, ctr, recommendation, ir, llm, retrieval]
---

# arXiv Paper Check — AI & CTR (June 22, 2026)

> New submissions from Friday, June 19, 2026. cs.AI: 73 new (312 total) | cs.IR: 11 new (22 total).

## Top Picks

### 1. ITNet: A Learnable Integral Transform That Subsumes Convolution, Attention, and Recurrence
- **Authors**: Ashim Dhor, Rasel Mondal, Pin Yu Chen
- **arXiv**: 2606.19538
- **Key contribution**: Proposes a unified architecture (Integral Transform Network) built around a learnable kernel implemented as an MLP that models pairwise interactions. Shows convolution, self-attention (multi-head), and autoregressive recurrence (LSTM, GRU, S4, Mamba) arise as special cases. Develops tiled kernel fusion, importance-weighted Monte Carlo integration, and learned low-rank factorization for efficiency. Matches or exceeds specialized baselines on ImageNet-1K, GLUE, ModelNet40, VQA-v2, and NLVR2 with a single architecture.

### 2. Token Factory: Efficiently Integrating Diverse Signals into Large Recommendation Models
- **Authors**: Xilun Chen, Shao-Chuan Wang, Baykal Cakici, Lukasz Heldt, Lichan Hong, Raghu Keshavan, Aniruddh Nath, Li Wei, Xinyang Xi (Google)
- **arXiv**: 2606.19635
- **Key contribution**: Proposes a framework to transform traditional recommendation signals into "soft tokens" that LRMs can process directly. Prevents prompt length explosion while enhancing model performance in production-scale recommendation environments.

### 3. G2Rec: Structuring and Tokenizing Distributed User Interest Context for Generative Recommendation
- **Authors**: Ruizhong Qiu, Yinglong Xia, Dongqi Fu, Hanqing Zeng, Ren Chen, Xiangjun Fan, Hong Li, Hong Yan, Hanghang Tong
- **arXiv**: 2606.20554
- **Key contribution**: A scalable framework unifying holistic graph-based user co-engagement modeling with semantic tokenization for industrial-scale generative recommendation. Enables capturing holistic and semantically grounded user interest prototypes without ground-truth user interests. Online deployment across product surfaces demonstrates superiority.

### 4. DIF: Denoising Implicit Feedback for Cold-start Recommendation (KDD 2026 ADS)
- **Authors**: Gaode Chen, Shicheng Wang, Shikun Li, Rui Huang, Xinghua Zhang, Yunze Luo, Shipeng Li, Shiming Ge, Ruina Sun, Yinjie Jiang, Jun Zhang (Kuaishou)
- **arXiv**: 2606.19658
- **Key contribution**: Identifies that cold-start items are more prone to noisy implicit feedback. Proposes a model-agnostic denoising method that infers pseudo-labels via content-similar warm items, models pseudo-label confidence, and adaptively corrects noisy labels using relative entropy and cold-start status. Deployed on billion-user scale Kuaishou with significant commercial metric improvements.

### 5. ELVA: Exploring Ranking-Driven Universal Multimodal Retrieval (ECCV 2026)
- **Authors**: Yuhan Liu, Pei Fu, Hang Li, Yukun Qi, Chao Jiang, Jingwen Fu, Zhen Liu, Bin Qin, Zhenbo Luo, Jian Luan, Jingmin Xin
- **arXiv**: 2606.20280
- **Key contribution**: Extends RLVR (RL with Verifiable Rewards) to multimodal retrieval, addressing "grain blindness" in contrastive learning. Uses rule-based rewards to jointly optimize negative sample ranking while widening the positive-negative gap. Introduces MRBench benchmark for multi-grain query scenarios. SOTA across standard retrieval benchmarks, +13.1% on MRBench.

### 6. Which Pairs to Compare for LLM Post-Training?
- **Authors**: Jiangze Han, Vineet Goyal, Will Ma
- **arXiv**: 2606.19607
- **Key contribution**: Studies comparison curation for preference-based LLM post-training as a sampling-design problem. Provides matching upper/lower bounds on DPO-trained policy optimality gap, linking label allocation to parameter estimation error. Proposes practical sampling designs for selecting informative pairs from large completion pools.

### 7. Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning
- **Authors**: Xuanzhi Feng, Zhengyang Li, Zeyu Liu, Haoxi Li, Yuming Jiang, Bing Guo, Jingcai Guo, Jie Zhang, Song Guo
- **arXiv**: 2606.19771
- **Key contribution**: Proposes learning from token-level distributional deviations for LLM reasoning, extracting richer signals from model's internal token distributions beyond simple entropy-based methods.

### 8. VCG: Multimodal Retrieval for E-Commerce Video Feeds under Extreme Cold-Start
- **Authors**: Katya Mirylenka, Egor Malykh, Mahdyar Ravanbakhsh, Michael Gygli, Marco-Andrea Buchmann, Andrew Dzhoha, Svitlana Borzenko, Francesca Catino, Mohamed Gaafar, Maarten Versteegh, Thomas Kober, Dario d'Andrea, Ellie Langhans
- **arXiv**: 2606.19627
- **Key contribution**: Scales multimodal retrieval to e-commerce video feeds under extreme cold-start. Uses domain-adapted CLIP for zero-shot retrieval. Shows generative (LLM) embeddings suffer from space collapse for retrieval while CLIP excels. 50% uplift in deep video completion in online A/B tests.

### 9. Emergent Alignment
- **Authors**: Martin Kolář
- **arXiv**: 2606.19527
- **Key contribution**: Endows LLM with a "conscience step" that reviews its own reasoning, using DPO to steer away from unethical outputs. Requires no external judge — relies on a frozen copy of itself. Shows a single high-level introspective question steers training toward ethical behavior under code-hacking scenarios, demonstrating "Emergent Alignment" as counterpoint to Emergent Misalignment.

### 10. Diffusion Language Models: An Experimental Analysis
- **Authors**: Thomas Bertolani, Davide Bucciarelli, Leonardo Zini, Marcella Cornia, Lorenzo Baraldi
- **arXiv**: 2606.19475
- **Key contribution**: Systematic experimental analysis of 8 state-of-the-art DLMs across 8 benchmarks (reasoning, coding, translation, knowledge, structured problem solving). Analyzes impact of denoising steps, context length, block size, and parallel unmasking strategies. Shows DLM behavior is strongly influenced by generation-time design choices, producing distinct performance-efficiency trade-offs.

### 11. Stellar: Scalable Multimodal Document Retrieval for Natural Language Queries
- **Authors**: Yuxiang Guo, Zhonghao Hu, Yuren Mao, Yuhang Liu, Congcong Ge, Xiaolu Zhang, Jun Zhou, Yunjun Gao
- **arXiv**: 2606.19960
- **Key contribution**: Scalable multimodal document retrieval framework that stores token-level document embeddings on disk and loads only candidate embeddings for late interaction. Combines Lexical Representation-based Filtering (LRF) with Efficient Disk-backed Late Interaction (DLI). Reduces memory overhead and query latency by 1-2 orders of magnitude without compromising effectiveness.

### 12. Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents
- **Authors**: Dhaval C. Patel et al.
- **arXiv**: 2606.19704
- **Key contribution**: Aggregates 14 parallel implementation studies of one MCP-based industrial agent benchmark. Argues aggregate-score leaderboards systematically underspecify deployed-agent evaluation — rankings don't transfer to OOD settings. Proposes ranking by predictive validity (in-sample vs out-of-sample rank correlation) over in-sample mean. Presents 12-tier measurement apparatus.

### 13. LLM Doesn't Know What It Doesn't Know: Detecting Epistemic Blind Spots on Clinical Tabular Data
- **Authors**: Akshat Dasula, Prasanna Desikan, Jaideep Srivastava (accepted EIML@ICML 2026)
- **arXiv**: 2606.19509
- **Key contribution**: Shows LLM verbalized confidence on structured clinical data is epistemically vacuous (near-constant 0.856-0.937 regardless of accuracy). Proposes cross-model attribution divergence with XGBoost to detect blind spots. Few-shot + SHAP feature evidence super-additively reduces Attribution Disagreement Score from 1.54 to 0.38 and improves accuracy from 49% to 75.3%.

### 14. PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents
- **Authors**: Manu Ghulyani, Arunabh Singh, Karan Bharadwaj, Ankit Nath, Suranjan Goswami
- **arXiv**: 2606.20047
- **Key contribution**: Treats context window management as a submodular selection problem over pooled context (memory, conversation turns, tool outputs). Addresses recency truncation blindness by selecting content by relevance at prompt assembly time rather than FIFO eviction.

### 15. ScholarQuest: A Taxonomy-Guided Benchmark for Agentic Academic Paper Search
- **Authors**: Tingyue Pan, Mingyue Cheng, Daoyu Wang, Yitong Zhou, Jie Ouyang, Qi Liu, Enhong Chen
- **arXiv**: 2606.20235
- **Key contribution**: Large-scale benchmark for agentic academic paper search built from 1,000+ CS topics and 4 research intents (method-oriented, setting-anchored, comparison-based, scope-controlled). Best agent only achieves 0.314 Recall@100 and 0.355 Recall@All, highlighting substantial room for improvement.

## Key Themes

| Theme | Papers |
|-------|--------|
| **Unified Architectures** | ITNet (conv/attn/rnn unified) |
| **Generative Recommendation Production** | G2Rec (graph tokenization), Token Factory (Google soft tokens) |
| **Cold-start & Denoising** | DIF (Kuaishou, KDD 2026), VCG (e-commerce video) |
| **RLVR for Retrieval** | ELVA (ECCV 2026) |
| **LLM Reasoning & Alignment** | Beyond Entropy, Emergent Alignment, Which Pairs to Compare |
| **Agent Evaluation** | Beyond Static Leaderboards, Agentic Review Systems, PACMS |
| **Efficient Retrieval** | Stellar (disk-backed late interaction), MonaVec (edge vector search) |
| **LLM Calibration & Uncertainty** | LLM Doesn't Know, Semantic Caching Calibration |
| **Agentic Search** | ScholarQuest |
| **Diffusion LMs** | Systematic analysis of 8 DLMs × 8 benchmarks |
