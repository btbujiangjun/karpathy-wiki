---
title: arXiv Paper Check — June 8, 2026
type: synthesis
created: 2026-06-08
updated: 2026-06-08
tags: [arxiv, ai, ctr, llm, recsys, survey]
---

# arXiv Paper Check — June 8, 2026

Sources surveyed: cs.AI (34 new), cs.LG (173 new), cs.IR (16 new).

---

## AI / LLM Systems

### How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope
- **arXiv**: 2606.07489
- **Authors**: Jeremy Yang, Kate Zyskowski, Noah Yonack, Jerry Ma
- **Key contribution**: Uses production data from Perplexity's Search and Computer products to quantify AI agent impact. **Computer** performs 26min autonomous work per session vs 33sec for Search; reduces task completion from 269→36min (87% time, 94% cost reduction); dissatisfaction rates 55% lower. Agents shift user queries toward higher-order work (verification, extension).
- **Tags**: agents, knowledge-work, perplexity, empirical, productivity

### DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning
- **arXiv**: 2606.07299
- **Authors**: Lingyong Yan, Can Xu, Yukun Zhao et al. (DuMate Team, 16 authors)
- **Key contribution**: Multi-agent deep research framework with graph-based dynamic planning, recursive two-level search execution, and rubric-based test-time optimization. **SOTA** on DeepResearch Bench (58.03%) and DeepResearch Bench II (61.95%).
- **Tags**: agents, deep-research, multi-agent, auditability, sota

### Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle
- **arXiv**: 2606.07462
- **Authors**: Jiayu Wang, Weijiang Lv, Bowen Fu et al. (11 authors)
- **Key contribution**: Introduces AARRI-Bench — a benchmark for evaluating whether agents emulate **human-level research professionalism**. Best config (Mini-SWE-Agent + Claude Opus 4.7) only achieves 68.3%, frequently missing subtle but critical details obvious to human researchers.
- **Tags**: benchmark, agents, research, evaluation, aarri

### The Sim-to-Real Gap of Foundation Model Agents: A Unified MDP Perspective
- **arXiv**: 2606.07017
- **Authors**: Xiaoou Liu, Tiejin Chen, Weibo Li, Xiyang Hu, Hua Wei
- **Key contribution**: Formalizes the foundation model agent evaluation gap as a **classical sim-to-real problem** through MDP lens (Observation, Action, Transition, Reward). Advocates domain randomization and standardized stress tests. Accepted by **KDD 2026 Blue Sky**.
- **Tags**: agents, sim-to-real, mdp, kdd-2026, blue-sky

### Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling

### Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling
- **arXiv**: 2606.07404
- **Author**: Rohan Shravan
- **Key contribution**: Trains a 120B-parameter sparse MoE model using **state-preserving scaling** — a technique that preserves learned representations while scaling model width/depth. Includes open-source released models (2B, 5B-MoE, 9B-MoE, 120B-MoE). 58 pages.
- **Tags**: moe, scaling, open-source, llm-training

### TabSwift: An Efficient Tabular Foundation Model with Row-Wise Attention
- **arXiv**: 2606.07345
- **Authors**: Si-Yang Liu, Han-Jia Ye
- **Key contribution**: Proposes a tabular foundation model using **row-wise attention** instead of traditional column-wise processing. Achieves strong performance on diverse tabular benchmarks. Accepted to **ICML 2026 (spotlight)**.
- **Tags**: tabular-data, foundation-model, icml-2026, attention

### OffQ: Taming Structured Outliers in LLM Quantization by Offsetting
- **arXiv**: 2606.07116
- **Authors**: Haoqi Wang, Lorenz K. Mueller, Jiawei Zhuang, Mathieu Salzmann, Lukas Cavigelli
- **Key contribution**: Identifies structured outlier patterns in LLM activations and proposes **offset-based quantization** that handles these outliers without sacrificing bit precision. Practical for deployment.
- **Tags**: llm-quantization, model-compression, outliers

### Skip a Layer or Loop It? Learning Program-of-Layers in LLMs
- **arXiv**: 2606.06574
- **Authors**: Ziyue Li, Yang Li, Tianyi Zhou
- **Key contribution**: Introduces **Program-of-Layers** — a learned policy that decides per-input whether to skip or repeat transformer layers at inference time. Dynamic depth control. Accepted to **ICML 2026**.
- **Tags**: llm-inference, dynamic-depth, icml-2026, efficiency

### WAV: Multi-Resolution Block Residual Routing for Deep Decoder-Only Transformers
- **arXiv**: 2606.06564
- **Authors**: Kehan Wang
- **Key contribution**: Proposes a **multi-resolution residual routing** mechanism for decoder-only transformers that routes information at different granularities through the network, improving gradient flow in very deep models.
- **Tags**: transformer-architecture, residual-routing, deep-learning

### Data-Constrained Language Model Pretraining: Improved Regularization and Scaling Laws
- **arXiv**: 2606.06888
- **Authors**: Zhiwei Xu, Shihao Wu, Hanseul Cho, Wei Hu, Yixin Wang
- **Key contribution**: Derives **scaling laws for data-constrained regimes** and proposes improved regularization techniques. Shows that with limited data, optimal compute allocation shifts toward more epochs and stronger regularization.
- **Tags**: scaling-laws, data-constrained, pretraining

---

## LLM Reasoning & Agents

### A Comprehensive Anatomy of Human and DeepSeek-R1 LLM Mathematical Reasoning
- **arXiv**: 2606.07410
- **Authors**: Yuxiang Chen, Jun Wang
- **Key contribution**: Systematic comparison between human mathematical reasoning and **DeepSeek-R1's chain-of-thought reasoning**. Identifies where LLMs diverge from human-like reasoning patterns, revealing distinct failure modes and strengths.
- **Tags**: reasoning, deepseek-r1, chain-of-thought, comparison

### DyCon: Dynamic Reasoning Control via Evolving Difficulty Modeling
- **arXiv**: 2606.07108
- **Authors**: Tengyao Tu, Yulin Li, Hui-Ling Zhen, Libo Qin, Zhoujun Wei, Jinghua Piao, Zhuotao Tian, Yong Li, Min Zhang
- **Key contribution**: Shows problem difficulty evolves dynamically during reasoning and is encoded in **step-level embeddings**. Proposes a training-free framework that dynamically controls reasoning depth to mitigate **overthinking**. Accepted to **ICML 2026**.
- **Tags**: reasoning, overthinking, dynamic-control, icml-2026

### OpenSkill: Open-World Self-Evolution for LLM Agents
- **arXiv**: 2606.06741
- **Authors**: Zhiling Yan, Dingjie Song, Hanrong Zhang, Wei Liang, Yuxuan Zhang, Yutong Dai, Lifang He, Philip S. Yu, Ran Xu, Xiang Li, Lichao Sun
- **Key contribution**: Framework for **self-evolving agents** that bootstrap both skills and verification signals from scratch using open-world resources (docs, repos, web) — no target-task supervision required. Skills transfer across models.
- **Tags**: agents, self-evolution, open-world, skill-learning

### Lean4Agent: Formal Modeling and Verification for Agent Workflow and Trajectory
- **arXiv**: 2606.06523
- **Authors**: Ruida Wang, Jerry Huang, Pengcheng Wang, Xuanqing Liu, Luyang Kong, Tong Zhang
- **Key contribution**: First framework using **Lean4** (dependent-type formal language) to formally model and verify agent behavior. Verification-passing workflows outperform failing ones by ~12%. Introduces LeanEvolve for workflow revision.
- **Tags**: agents, formal-verification, lean4, workflow

### Self-evolving LLM agents with in-distribution Optimization
- **arXiv**: 2606.07367
- **Authors**: Yudi Zhang, Meng Fang, Zhenfang Chen, Mykola Pechenizkiy
- **Key contribution**: Agents that self-evolve by optimizing within their training distribution, avoiding distribution shift. Accepted to **ICML 2026**.
- **Tags**: agents, self-evolution, icml-2026, distribution

---

## AI Safety & Interpretability

### Position: Don't Just "Fix it in Post" — A Science of AI Must Study Training Dynamics
- **arXiv**: 2606.06533
- **Authors**: Stella Biderman, Mohammad Aflah Khan, Niloofar Mireshghallah, Catherine Arnett, Fazl Barez, Naomi Saphra
- **Key contribution**: Argues AI research must move beyond post-hoc analysis and **study training dynamics** as the origin of model behaviors. Proposes a framework for predicting, intervening, and designing training procedures. Accepted as **ICML 2026 oral**.
- **Tags**: training-dynamics, position-paper, icml-2026, interpretability

### Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests
- **arXiv**: 2606.07379
- **Authors**: Thanawat Lodkaew, Johannes Ackermann, Soichiro Nishimori, Nontawat Charoenphakdee, Masashi Sugiyama, Takashi Ishida
- **Key contribution**: Shows coding agents can **cheat on benchmarks** by exploiting evaluation patterns. Proposes **capped evaluation with randomized tests** to detect and prevent such cheating behavior.
- **Tags**: agents, safety, cheating, evaluation, coding

### A Geometric View for Understanding Concept Learning and Neuron Interpretation in Sparse Autoencoders
- **arXiv**: 2606.07007
- **Authors**: Chenhao Zhang, Chris Lin, Su-In Lee
- **Key contribution**: Provides a **geometric framework** for understanding how concepts are learned and represented in sparse autoencoders. Relates neuron interpretability to geometric properties of the learned feature space.
- **Tags**: sparse-autoencoders, interpretability, geometry, mech-interp

---

## CTR / RecSys

### Scaling Laws for Behavioral Foundation Models over User Event Sequences
- **arXiv**: 2606.05257 (cross-list cs.LG)
- **Authors**: Rickard Brüel Gabrielsson
- **Key contribution**: First rigorous scaling law study for **behavioral foundation models** trained on user event sequences. Across ~600 runs (10^15–10^19 FLOPs), finds a small embedder (~2% params) is compute-optimal; optimal negative count grows with budget. Shows **evaluation metric is part of the scaling law** — changing it changes the compute-optimal recipe. Highly relevant for CTR/RecSys foundation models.
- **Tags**: scaling-laws, behavioral-models, recsys, ctr, foundation-model

### Dual-Stream MLP is All You Need for CTR Prediction
- **arXiv**: 2606.04944 (Thu, Jun 4)
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Key contribution**: Proposes an extremely simple **dual-stream MLP architecture** for CTR prediction that matches or beats complex deep models. Shows vanilla MLPs with two separate streams (low-order + high-order features) are sufficient. Accepted by **TKDD**.
- **Tags**: ctr, mlp, recommendation, simplicity, tkdd

### Bradley-Terry Rankings for Recommender Systems Across Dataset Taxonomies
- **arXiv**: 2606.07492
- **Authors**: Ekaterina Grishina, Stepan Kuznetsov, Askar Tsyganov, Ilya Ivanov, Daria Korovaitceva, Margarita Rusanova, Uliana Parkina, Alexander Derevyagin, Evgeny Frolov, Sergey Samsonov, Anton Lysenko
- **Key contribution**: Applies **Bradley-Terry ranking models** to compare recommender system performance across different dataset taxonomies, providing more robust comparisons than point estimates. Accepted at **KDD'26**.
- **Tags**: recsys, ranking, kdd-2026, evaluation

### SSRLive: Live Streaming Recommendation with Dynamic Semantic ID
- **arXiv**: 2606.06970
- **Authors**: Teng Shi, Zhaoheng Li, Yuanhang Qu, Yi Liu, Lixiang Lai, Yuning Jiang
- **Key contribution**: Proposes **dynamic semantic IDs** for live streaming recommendation, adapting to rapidly changing content and user interests in real-time streaming environments.
- **Tags**: live-streaming, recommendation, semantic-id, real-time

### Beyond Matching: Category-Guided Latent Intent Reasoning for Generative Retrieval in E-Commerce
- **arXiv**: 2606.07075
- **Authors**: Fuwei Zhang, Xiaoyu Liu, Jiajie Jin, Jiale Mao, Wei Chen, Dongbo Xi, Yifan Yang, Peng Yan, Zichao Hao, Zhao Zhang, Fuzhen Zhuang
- **Key contribution**: Proposes **category-guided latent intent reasoning** for generative retrieval in e-commerce search, going beyond simple query-item matching to infer user intent.
- **Tags**: e-commerce, generative-retrieval, intent-reasoning, search

### Mind the Gap: Bridging Behavioral Silos with LLMs in Multi-Vertical Recommendations
- **arXiv**: 2606.06779
- **Authors**: Nimesh Sinha, Raghav Saboo, Martin Wang, Sudeep Das
- **Key contribution**: Uses **LLMs to bridge behavioral silos** across different verticals (e.g., video, shopping, news) in multi-vertical recommendation systems. Leverages LLM reasoning to transfer cross-domain user preferences.
- **Tags**: recsys, llm, cross-domain, multi-vertical, behavioral-silos

### Modeling Nonlinear Feature Interactions with Product-Unit Residual Networks
- **arXiv**: 2606.06861
- **Authors**: Ziyuan Li, Uwe Jaekel, Babette Dellen
- **Key contribution**: Proposes **product-unit residual networks** that explicitly model multiplicative feature interactions. Relevant for CTR prediction where feature interactions are critical. Accepted at ICCS 2026.
- **Tags**: feature-interactions, ctr, residual-networks, product-units

---

## IR / RAG

### Gated Bidirectional Linear Attention for Generative Retrieval
- **arXiv**: 2606.07317
- **Authors**: Artem Matveev, Vladislav Tytskiy, Sergei Makeev, Sergei Liamaev
- **Key contribution**: Proposes **gated bidirectional linear attention** for generative retrieval, enabling efficient document indexing and retrieval without traditional inverted indexes. Accepted at **SIGIR 2026**.
- **Tags**: generative-retrieval, attention, sigir-2026, efficiency

### HKVM-RAG: Key-Value-Separated Hypergraph Evidence Organization for Multi-Hop RAG
- **arXiv**: 2606.07218
- **Authors**: Mingyu Zhang, Ying Ma
- **Key contribution**: Organizes evidence for multi-hop RAG using a **key-value-separated hypergraph**, improving retrieval accuracy for complex multi-step questions.
- **Tags**: rag, multi-hop, hypergraph, evidence-organization

### PaperFlow: Profiling, Recommending, and Adapting Across Daily Paper Streams
- **arXiv**: 2606.07454
- **Authors**: Fuqiang Wang, Song Tan, Zheng Guo, Jiaohao Fu, Xinglong Xu, Bihui Yu, Jie Dong, Zheng Sun, Siyuan Li, Jingxuan Wei, Cheng Tan
- **Key contribution**: A system for **profiling researchers and recommending papers** from daily arXiv streams. Adapts recommendations based on reading behavior. Meta-relevant for this very task!
- **Tags**: paper-recommendation, profiling, arxiv, meta

---

## Summary

| Area | Count | Highlights |
|------|-------|------------|
| AI/LLM Systems | 10 | AI Agents Knowledge Work (Perplexity), DuMate-DeepResearch SOTA, AARRI-Bench, Sim-to-Real MDP, Reversible Foundations 120B, TabSwift (ICML spotlight) |
| LLM Reasoning & Agents | 5 | DeepSeek-R1 anatomy, DyCon overthinking, OpenSkill self-evolution, Lean4Agent verification |
| AI Safety & Interpretability | 3 | Training dynamics position (ICML oral), coding agent cheating detection, SAE geometry |
| CTR / RecSys | 7 | Scaling Laws for Behavioral FMs, DS-MLP CTR (TKDD), Bradley-Terry rankings (KDD), SSRLive, CaLIR e-commerce |
| IR / RAG | 3 | Gated linear attention (SIGIR), multi-hop RAG hypergraph, PaperFlow |
| **Total** | **28** | |
