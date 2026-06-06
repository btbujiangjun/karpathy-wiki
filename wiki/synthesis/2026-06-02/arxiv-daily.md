---
title: arXiv Daily — AI Research Survey (June 2, 2026)
type: synthesis
created: 2026-06-02
updated: 2026-06-02
sources: [arXiv cs.AI, cs.LG, cs.IR, cs.CL]
tags: [arxiv-daily, llm, recommendation, ctr, games, rl, generative-rec, ir]
---

# arXiv Daily — AI Research Survey (June 2, 2026)

> Coverage: recent submissions from arXiv (May 26 – June 1, 2026) across AI, LLMs, recommendation, CTR, advertising, sequential modeling, games, and information retrieval. ~30 papers highlighted.

---

## 1. Generative Recommendation & RecSys

### TurboGR: Accelerated Training System for Large-Scale Generative Recommendation
- **arXiv**: [2605.13433](https://arxiv.org/abs/2605.13433)
- **Authors**: Huichao Chai, Zhixin Wu, Xuemiao Li, Shiqing Fan et al.
- **Affiliation**: — (Ascend NPU ecosystem)
- **Abstract**: Presents an Ascend-affinity training system for generative recommendation (GR) addressing jagged operator acceleration, distributed communication optimization, and negative sampling optimization. Achieves 54.71% MFU with near-linear scalability (0.97) on KuaiRand-27K.
- **Key Innovation**: Fusion operators eliminating padding redundancy; hierarchical sparse parallelism; intra-batch logit sharing for negative sampling.

### RAGR: Review-Augmented Generative Recommendation
- **arXiv**: [2605.17267](https://arxiv.org/abs/2605.17267)
- **Authors**: Sixiao Zhang, Mingrui Liu, Cheng Long
- **Affiliation**: Nanyang Technological University
- **Abstract**: Incorporates review feedback directly into generative user sequences by interleaving item semantic IDs and review semantic IDs. Uses DPO-based Item-Centric Task Generation Alignment.
- **Key Innovation**: Mixed behavioral-semantic sequence construction; review signals participate directly in autoregressive next-token generation.

### Generative Conversational Recommender System (GCRS)
- **arXiv**: [2605.21987](https://arxiv.org/abs/2605.21987)
- **Authors**: Sixiao Zhang, Mingrui Liu, Cheng Long
- **Affiliation**: Nanyang Technological University
- **Abstract**: Fully generative CRS unifying recommendation and dialog in a single autoregressive framework using discrete semantic IDs. Structured generation factorizes into intent prediction, target selection, then response generation.
- **Key Innovation**: Up to 29% Recall@1 improvement via constrained decoding and end-to-end optimization.

### PROMISE: Process Reward Models for Test-Time Scaling in Generative Recommendations
- **arXiv**: (2026)
- **Authors**: Chengcheng Guo, Kuo Cai, Yu Zhou, Qiang Luo et al.
- **Affiliation**: —
- **Abstract**: Applies process reward models to unlock test-time scaling laws in generative recommendation.
- **Key Innovation**: Step-level reward signals for beam search during recommendation decoding.

### FOSTER: First-Order Dataset Distillation for Text-based Sequential Recommendation
- **arXiv**: [2605.30772](https://arxiv.org/abs/2605.30772)
- **Authors**: Hung Vinh Tran, Tong Chen, Xinyi Gao, Junliang Yu, Julien Monteil, Hongzhi Yin
- **Affiliation**: University of Queensland
- **Abstract**: First-order dataset distillation framework for sequential recommendation.
- **Key Innovation**: Distills large training sets into compact synthetic sequences while preserving recommendation performance.

### MixRAGRec: Mixture-of-Experts KG-RAG for Multi-Agent LLM Recommendation
- **arXiv**: [2605.28175](https://arxiv.org/abs/2605.28175)
- **Authors**: Shijie Wang, Chengyi Liu, Yujuan Ding, Shanru Lin, See-Kiong Ng, Xu Xin, Wenqi Fan
- **Affiliation**: — (Accepted KDD 2026)
- **Abstract**: Cooperative multi-agent framework for KG-RAG recommendation with MoE retrieval agent, knowledge preference alignment agent, and contrastive learning-reinforced recommendation agent.
- **Key Innovation**: MMAPO (Mixture-of-Experts Multi-Agent Policy Optimization) trains all three agents under a unified objective.

### LoopFM: Learning from Historical Representations of Foundation Model for Recommendation
- **arXiv**: [2605.29280](https://arxiv.org/abs/2605.29280)
- **Authors**: Shali Jiang, Hua Zheng, Boyang Liu et al.
- **Affiliation**: —
- **Abstract**: Leverages historical representations from foundation models for recommendation without full model re-training.
- **Key Innovation**: Efficient reuse of frozen foundation model embeddings with lightweight adapters.

### Rec-Distill: Industrial Distillation Pipeline for Large-Scale Recommendation Models
- **arXiv**: [2605.29755](https://arxiv.org/abs/2605.29755)
- **Authors**: Haoran Ding, Wenlin Zhao, Yuchen Jiang et al.
- **Affiliation**: Industry
- **Abstract**: End-to-end distillation pipeline for compressing large-scale recommendation models in production.
- **Key Innovation**: Multi-stage distillation with online/offline coordination.

### ACE: Anisotropy-Controllable Embedding for LLM-enhanced Sequential Recommendation
- **arXiv**: [2605.29322](https://arxiv.org/abs/2605.29322)
- **Authors**: Dongcheol Lee, Hye-young Kim, Jongwuk Lee
- **Affiliation**: (Accepted SIGIR 2026)
- **Abstract**: Controls anisotropy in LLM embeddings for sequential recommendation tasks.
- **Key Innovation**: Anisotropy calibration aligns LLM embedding spaces with recommendation objectives.

### Generative Spatiotemporal Intent Sequence Recommendation via Implicit Reasoning in Amap
- **arXiv**: [2605.28888](https://arxiv.org/abs/2605.28888)
- **Authors**: Sicong Wang, Ruiting Dong, Yue Liu et al.
- **Affiliation**: Amap (Alibaba)
- **Abstract**: Generative recommendation for spatiotemporal intents in map-based services.
- **Key Innovation**: Implicit reasoning over user mobility patterns for next-POI prediction.

### Self-Evolving Recommendation System with LLM Agents
- **arXiv**: [2602.10226](https://arxiv.org/abs/2602.10226)
- **Authors**: Haochen Wang, Yi Wu, Daryl Chang, Li Wei, Lukasz Heldt
- **Affiliation**: Google (YouTube)
- **Abstract**: Uses Gemini LLM agents to autonomously generate, train, and deploy recommendation model improvements in an end-to-end automated workflow. Deployed at YouTube.
- **Key Innovation**: Offline Agent (Inner Loop) + Online Agent (Outer Loop); LLM discovers novel optimizers, architectures, and reward functions.

---

## 2. CTR Prediction & Advertising

### Generative Long-term User Interest Modeling for CTR (GenLI)
- **arXiv**: [2605.15905](https://arxiv.org/abs/2605.15905)
- **Authors**: Jiangli Shao, Kaifu Zheng, Hao Fang et al.
- **Affiliation**: —
- **Abstract**: Proposes GenLI with Interest Generation Module (IGM), Behavior Retrieval Module (BRM), and Interest Fusion Module (IFM) for target-independent, diverse long-term user interest modeling.
- **Key Innovation**: O(1) behavior retrieval; target-independent interest generation avoids bias from candidate-centric attention.

### CADET: Context-Conditioned Ads CTR with Decoder-Only Transformer
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Authors**: David Pardoe, Neil Daftary et al.
- **Affiliation**: LinkedIn
- **Abstract**: End-to-end decoder-only transformer for ads CTR prediction deployed on LinkedIn's advertising platform.
- **Key Innovation**: Decoder-only architecture unifies feature processing and prediction; deployed in production.

### On the Practice of Scaling Search Conversion Rate Prediction
- **arXiv**: [2605.29232](https://arxiv.org/abs/2605.29232)
- **Authors**: James Pak, Jyun-Yu Jiang, Fan Zhang et al.
- **Affiliation**: —
- **Abstract**: Industrial practice of scaling conversion rate prediction models for search advertising.
- **Key Innovation**: Practical scaling strategies and lessons from production deployment.

### Graph-GRPO: Dependency-Aware Credit Assignment for Generative E-commerce Search Relevance
- **arXiv**: [2605.31003](https://arxiv.org/abs/2605.31003)
- **Authors**: Jiarui Che, Yifei Chen, Zhixing Tian, Chenyang Wang, Ziguang Cheng
- **Affiliation**: (Submitted CIKM 2026)
- **Abstract**: Applies GRPO (Group Relative Policy Optimization) with graph-based credit assignment for search relevance ranking.
- **Key Innovation**: Graph-structured reward propagation addresses credit assignment in multi-step relevance judgments.

---

## 3. LLM Reasoning & Reinforcement Learning

### Beyond Reasoning: RL Unlocks Parametric Knowledge in LLMs
- **arXiv**: [2605.07153](https://arxiv.org/abs/2605.07153)
- **Authors**: Wanli Yang, Hongyu Zang, Junwei Zhang et al.
- **Affiliation**: —
- **Abstract**: Studies whether RL can improve direct recall of parametric knowledge (zero-shot QA). RL yields ~27% average relative gains across 3 model families.
- **Key Innovation**: Demonstrates RL primarily redistributes probability mass over existing knowledge; hardest ~18% of examples drive ~83% of gains.

### Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key
- **arXiv**: [2605.06638](https://arxiv.org/abs/2605.06638)
- **Authors**: Tianle Wang et al.
- **Affiliation**: —
- **Abstract**: Investigates the expressiveness requirements for RL to successfully teach long-horizon reasoning capabilities to LLMs.
- **Key Innovation**: Identifies critical bottlenecks where RL fails due to insufficient reward signal expressiveness.

### LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards
- **arXiv**: [2605.31584](https://arxiv.org/abs/2605.31584)
- **Authors**: Nianyi Lin, Jiajie Zhang, Lei Hou, Juanzi Li
- **Affiliation**: Tsinghua University
- **Abstract**: Uses search agent trajectories to build tiered distractors (high/low confusability) for training long-context reasoning via RL with rubric rewards.
- **Key Innovation**: Tiered distractor construction from real search agent behavior; rubric-based reward for intermediate reasoning steps.

### GRAM: Generative Recursive Reasoning Models
- **arXiv**: [2605.19376](https://arxiv.org/abs/2605.19376)
- **Authors**: Junyeob Baek, Mingyu Jo, Minsu Kim, Mengye Ren, Yoshua Bengio, Sungjin Ahn
- **Affiliation**: KAIST / Mila / NYU
- **Abstract**: Extends recursive reasoning models with probabilistic latent trajectories, enabling multiple hypotheses and test-time scaling through depth and parallel sampling.
- **Key Innovation**: First generative (stochastic) recursive reasoning model; supports conditional reasoning and unconditional generation.

### SLAT: Segment-Level Adaptive Trimming for Efficient CoT Reasoning
- **arXiv**: [2605.30832](https://arxiv.org/abs/2605.30832)
- **Authors**: Jian Yao, Xiongcai Luo, Ran Cheng, Kay Chen Tan
- **Affiliation**: —
- **Abstract**: RL framework that selectively suppresses redundant reasoning segments. Reduces reasoning length by 50% while maintaining competitive accuracy.
- **Key Innovation**: Theoretical characterization of segment suboptimality under correctness-length trade-off; segment-aware Pareto frontier.

### DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM RL
- **arXiv**: [2605.30859](https://arxiv.org/abs/2605.30859)
- **Authors**: Yujie Wang, Siwei Chen, Longzan Luo et al.
- **Affiliation**: (Accepted ICML 2026)
- **Abstract**: Shapes rollout distribution towards conciseness and certainty, up to 1.77x acceleration without performance loss.
- **Key Innovation**: Intra-prompt long-tail analysis revealing ineffective verbosity; adaptive redundancy allocation.

### LaTER: Latent-Then-Explicit Reasoning for Efficient Test-Time Compute
- **arXiv**: [2605.07315](https://arxiv.org/abs/2605.07315)
- **Authors**: Xuan Li, Yining Wang, Yuchen Liu et al.
- **Affiliation**: —
- **Abstract**: Two-stage paradigm: bounded exploration in continuous latent space, then switch to explicit CoT for verification.
- **Key Innovation**: Training-free instantiation using latent KV cache preservation; entropy-based switching.

### TRACE: Efficient Test-Time Scaling via Temporal Reasoning Aggregation
- **arXiv**: [2604.17304](https://arxiv.org/abs/2604.17304)
- **Authors**: Jiakun Li, Xingwei He, Kefan Li et al.
- **Affiliation**: —
- **Abstract**: Determines reasoning convergence via temporal aggregation of answer consistency + confidence trajectory. Reduces tokens by 25-30%.
- **Key Innovation**: Multi-step evidence aggregation, not single-step confidence; training-free.

---

## 4. Information Retrieval & Search

### SPECTRA: Synthetic IR Test Collections with Relevance Oracles
- **arXiv**: [2605.31575](https://arxiv.org/abs/2605.31575)
- **Authors**: Eric Liang
- **Affiliation**: —
- **Abstract**: Framework for generating synthetic IR test collections with controlled relevance judgments and distractor difficulty.
- **Key Innovation**: Programmatic relevance oracles enable controlled experimentation with retrieval difficulty.

### No More K-means: Single-Stage Sparse Coding for Efficient Multi-Vector Retrieval
- **arXiv**: [2605.30120](https://arxiv.org/abs/2605.30120)
- **Authors**: Lixuan Guo, Yifei Wang, Tiansheng Wen et al.
- **Affiliation**: (Accepted ICML 2026)
- **Abstract**: Replaces K-means clustering in multi-vector retrieval with single-stage sparse coding.
- **Key Innovation**: End-to-end sparse code learning eliminates the clustering bottleneck.

### Inference-Free Multimodal Learned Sparse Retrieval for Production-Scale Visual Document Search
- **arXiv**: [2605.30917](https://arxiv.org/abs/2605.30917)
- **Authors**: Gyu-Hwung Cho, Youngjune Lee et al.
- **Affiliation**: NAVER Corp. / Seoul National University / Naver Labs Europe
- **Abstract**: Inference-free multimodal sparse retrieval for production visual document search.
- **Key Innovation**: Pre-computed sparse representations eliminate online inference overhead.

### GrepSeek: Training Search Agents for Direct Corpus Interaction
- **arXiv**: [2605.29307](https://arxiv.org/abs/2605.29307)
- **Authors**: Alireza Salemi, Chang Zeng et al.
- **Affiliation**: UMass Amherst
- **Abstract**: Trains LLM agents to directly interact with search corpora (grep-style) instead of via traditional retrieval pipelines.
- **Key Innovation**: Agent learns when and how to scan corpus directly; bypasses index overhead.

### DynaTree: Dynamic Agentic Retrieval Tree for Time-Sensitive News Retrieval
- **arXiv**: [2605.31377](https://arxiv.org/abs/2605.31377)
- **Authors**: Siyuan Qi, Xinyuan Wang, Yingxuan Yang et al.
- **Affiliation**: —
- **Abstract**: Dynamic tree-structured retrieval for time-sensitive news queries with agentic expansion.
- **Key Innovation**: Agent decides when to expand/contract retrieval tree based on query timeliness.

### Beyond Instance-Level Alignment: Semantic Factor Learning for Collaborative Filtering
- **arXiv**: [2605.31414](https://arxiv.org/abs/2605.31414)
- **Authors**: Yajie Yu, Chenzhong Bin et al.
- **Affiliation**: (Accepted KDD 2026)
- **Abstract**: Moves beyond instance-level alignment/uniformity to semantic factor learning for collaborative filtering.
- **Key Innovation**: Disentangled semantic factors enable better generalization in CF.

---

## 5. Games & Multi-Agent RL

### MARLIN: Multi-Agent Game-Theoretic RL for Sustainable LLM Inference
- **arXiv**: [2605.13496](https://arxiv.org/abs/2605.13496)
- **Authors**: H. Moore, S. Qi, D. Milojicic, C. Bash, S. Pasricha
- **Affiliation**: HP Labs / Colorado State
- **Abstract**: Game-theoretic MARL framework co-optimizing TTFT, carbon emissions, water usage, and energy costs for LLM inference serving.
- **Key Innovation**: 18% TTFT reduction, 33% carbon, 43% water reduction vs SOTA; multi-objective game formulation.

### Procedural Generation of FPS Maps using MAP-Elites
- **arXiv**: [2605.30570](https://arxiv.org/abs/2605.30570)
- **Authors**: Simone de Donato, Pier Luca Lanzi, Daniele Loiacono
- **Affiliation**: Politecnico di Milano
- **Abstract**: Applies MAP-Elites quality diversity algorithm to generate FPS game levels with novel map representations.
- **Key Innovation**: Point-Line and Spatial-Layout representations; diversity + quality optimization.

### Fluid-Agent Reinforcement Learning
- **arXiv**: [2602.14559](https://arxiv.org/abs/2602.14559)
- **Authors**: Shishir Sharma, Doina Precup, Theodore J. Perkins
- **Affiliation**: McGill / Mila
- **Abstract**: Framework where agents can dynamically create/spawn other agents; game-theoretic solution concepts for fluid-agent environments.
- **Key Innovation**: First formalization of agent spawning in MARL; Predator-Prey and Level-Based Foraging variants.

### SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks
- **arXiv**: [2605.31433](https://arxiv.org/abs/2605.31433)
- **Authors**: Wai-Chung Kwan et al.
- **Affiliation**: —
- **Abstract**: Co-evolving policies via self-play for open-ended task generation and mastery.
- **Key Innovation**: Population-based training with automatic curriculum generation.

---

## 6. LLM Agents & Systems

### AdaCoM: Adaptive Context Management for Long-Horizon Tasks
- **arXiv**: [2605.30785](https://arxiv.org/abs/2605.30785)
- **Authors**: Lu Yi, Runlin Lei, Liuyi Yao et al.
- **Affiliation**: —
- **Abstract**: Trains external LLM to manage context of a frozen agent via RL-based modification actions (summarization, pruning).
- **Key Innovation**: Reveals Fidelity-Reliability Trade-off: high-performing agents need high-fidelity context; lower-performing need aggressive compression.

### MAVEN: Modular Agentic Verification and Execution Network
- **arXiv**: [2605.30738](https://arxiv.org/abs/2605.30738)
- **Authors**: Omkar Ghugarkar, Vishvesh Bhat, Muhammad Ahmed Mohsin, Asad Aali
- **Affiliation**: —
- **Abstract**: Lightweight symbolic reasoning scaffold for tool calling, achieving 71% accuracy on MAVEN-Bench with 1/10 cost of frontier models.
- **Key Innovation**: Verification-centered scaffold improves GPT-OSS-120b from 48% to 71% without training.

### Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities
- **arXiv**: [2605.30621](https://arxiv.org/abs/2605.30621)
- **Authors**: Minhua Lin, Juncheng Wu et al.
- **Affiliation**: —
- **Abstract**: Analyzes harness self-evolution in LLM agents; finds harness-updating is flat across model tiers, harness-benefit is non-monotonic.
- **Key Innovation**: Mid-tier models benefit most from harness updates; weak/strong models benefit less.

### UniScale: Adaptive Unified Inference Scaling
- **arXiv**: [2605.30898](https://arxiv.org/abs/2605.30898)
- **Authors**: Kaiyu Huang et al.
- **Affiliation**: (Accepted ICML 2026)
- **Abstract**: Unifies model routing and test-time scaling via contextual multi-armed bandit (LinUCB).
- **Key Innovation**: First joint optimization of routing and TTS; fine-grained quality-cost trade-off.

### COMPASS: Cognitive MCTS-Guided Process Alignment for Safe Search Agents
- **arXiv**: [2605.30838](https://arxiv.org/abs/2605.30838)
- **Authors**: Wenkai Shen et al.
- **Affiliation**: —
- **Abstract**: MCTS-guided safety alignment for LLM search agents; cognitive tree exploration synthesizes stealthy attack trajectories.
- **Key Innovation**: Introspective step-wise alignment isolates risky intermediate actions for process supervision.

### SEPO: Strategic Equilibrium Policy Optimization for Agent Safety
- **arXiv**: [2605.30859](https://arxiv.org/abs/2605.30859)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Game-theoretic safety alignment using per-rollout exploit computation; avoids zero-gradient issues in GRPO.
- **Key Innovation**: Per-rollout exploit penalty (not shared) preserves gradient signal.

---

## 7. Sequential Modeling & Transformers

### Parallax: Parameterized Local Linear Attention for Language Modeling
- **arXiv**: (June 1, 2026)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Upgrades local constant estimate in softmax attention to local linear estimate for provably better bias-variance trade-off.
- **Key Innovation**: Local linear attention derived from nonparametric statistics; compatible with existing LLM architectures.

### Beyond Instance-Level Alignment and Uniformity (CF)
- **arXiv**: [2605.31414](https://arxiv.org/abs/2605.31414)
- **Authors**: Yajie Yu et al.
- **Affiliation**: (KDD 2026)
- **Abstract**: Semantic factor learning for collaborative filtering beyond alignment/uniformity.
- **Key Innovation**: Factor-level disentanglement improves long-tail recommendation.

---

## Summary of Key Themes

| Theme | Papers | Trend |
|-------|--------|-------|
| **Generative Recommendation** | 10+ papers | GR is becoming mainstream; scaling laws, process rewards, distillation, and MoE agents |
| **CTR + Advertising** | 4 papers | Decoder-only transformers, generative interest modeling, scaling practice |
| **LLM Reasoning + RL** | 8 papers | RL for knowledge recall; test-time scaling; overthinking detection and mitigation |
| **IR & Search** | 6 papers | Synthetic collections, agentic search, inference-free retrieval |
| **Games & MARL** | 4 papers | Quality diversity, fluid agents, game-theoretic LLM scheduling |
| **LLM Agents** | 6 papers | Context management, modular verification, safety alignment |
