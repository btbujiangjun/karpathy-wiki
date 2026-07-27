---
title: "arXiv Paper Check — 2026-07-25"
type: synthesis
created: 2026-07-25
updated: 2026-07-25
sources: []
tags: [arxiv, ai, ctr, recommendation, agents, reasoning, sequential-modeling, rl]
---

# arXiv Paper Check — 2026-07-25

> Automated search across arXiv for recent papers in AI and CTR (Click-Through Rate) categories from the last 24 hours.
> Categories: cs.AI (260 new Jul 24), cs.IR (15 new Jul 24), cs.LG (169 new Jul 24), cs.CL (110 new Jul 24).

---

## 1. CTR Prediction & Recommendation

### 1.1 DLMRec: Diffusion Language Model for Recommendation
- **Authors**: Chengyi Liu, Yongqi Zhou, Junwei Pan, Zhixiang Feng, Chengguo Yin, Haijie Gu, Jie Jiang, Yinghao Liu, Yujuan Ding, Qing Li, Wenqi Fan
- **Date**: 24 Jul 2026
- **arXiv**: 2607.21519
- **Abstract**: Proposes DLMRec, a discrete diffusion language model for recommendation as an alternative to autoregressive generation. Introduces a collaborative-aware stochastic tokenizer encoding multi-hop collaborative signals, curriculum-driven training aligning denoising with preference recovery, and stability-aware voting for robust generation. Argues that next-token objectives emphasize sequential order over structural inter-item dependencies.
- **Key Innovations**: Discrete diffusion for generative recommendation; collaborative-aware tokenizer; curriculum denoising for preference recovery.
- **Impact**: Challenges the autoregressive dominance in generative recommendation; first diffusion-based approach for rec.

### 1.2 Can Generative Recommendation Reach Cold Items? A Temporal Perspective on Semantic-ID Generation
- **Authors**: Jie Peng, Yanping Zheng, Zhewei Zhe, Bin Tong, Guan Wang, Bo Zheng
- **Date**: 23 Jul 2026
- **arXiv**: 2607.21101
- **Abstract**: Revisits SID-based generative recommendation under an absolute-time temporal protocol that separates seen and unseen targets and diagnoses cold item reachability at the token level. Through seen/unseen-hit analysis, coldness taxonomy, and oracle-prefix probing, shows that current SID-based models can occasionally reach future items supported by observed tokens and prefixes, but struggle with unseen atomic tokens and unsupported SID paths. Interprets SID generation as hierarchical semantic bucketing.
- **Key Innovations**: Temporal protocol for cold item evaluation; coldness taxonomy; oracle-prefix probing; compositional-but-not-open-ended analysis.
- **Impact**: Reveals fundamental limitations of current Semantic-ID generative recommendation for cold-start scenarios.

### 1.3 CDL: Cardinality-Decomposed Loss for Heterogeneous Recommendation Graphs
- **Authors**: Parul Maheshwari, Amulya Paruchuri, Yiqing Zou, Alireza Sahami Shirazi, Farhad Farahani, Prakhar Mehrotra
- **Date**: 22 Jul 2026
- **arXiv**: 2607.20737
- **Abstract**: Identifies that BPR loss causes attribute embeddings to collapse to near-random geometry in heterogeneous bipartite graphs — a silent failure invisible to standard ranking metrics. Proposes Cardinality-Decomposed Loss (CDL) combining Cross Entropy and BPR to optimize across relation cardinalities. Lambda-sweep reveals dataset behavior governed by semantic alignment and topology leakage.
- **Key Innovations**: CE-BPR conflict diagnosis; CDL for cross-cardinality optimization; semantic alignment / topology leakage analysis.
- **Impact**: Exposes silent attribute embedding collapse in GNN-based rec; principled fix via loss decomposition.

### 1.4 RAMP: Robust Ad Recommendation Under Limited Personalized-Feature Availability
- **Authors**: Dairui Liu, Zhongyi Lu, Roger Zhe Li, et al.
- **Date**: 21 Jul 2026
- **arXiv**: 2607.17473
- **Abstract**: Proposes masking and alignment pathways for robust ad recommendation when personalized features are unavailable. Accepted at ICTIR 2026.
- **Key Innovations**: Masking-based robustness; alignment pathways for feature availability.
- **Impact**: Addresses practical production constraint of feature availability in ad recommendation.

### 1.5 Topology-Aware Tokenization for Generative Recommendation
- **Authors**: Yaokun Liu, Yifan Liu, Zhenrui Yue, Gyuseok Lee, Zelin Li, Ruichen Yao, Dong Wang
- **Date**: 22 Jul 2026
- **arXiv**: 2607.18600
- **Abstract**: Proposes topology-aware tokenization that incorporates graph structure into Semantic-ID generation for recommendation. Accepted at RecSys 2026.
- **Key Innovations**: Graph-structure-aware tokenization for generative rec.
- **Impact**: Bridges graph topology with generative recommendation tokenization.

### 1.6 PRL: Probabilistic Residual Learning for Online Recommendations
- **Authors**: Wenyuan Wang, Yusong Zhao, Zihao Xu, et al.
- **Date**: 24 Jul 2026
- **arXiv**: 2607.20863
- **Abstract**: Causal Bayesian recommendation model that models the residual between ground-truth and base predictions. Probabilistically groups users for localized residual modeling, models domain-level confounders, and aggregates cluster-specific residual predictions using do-calculus. Plug-and-play compatible with various base deep learning recommender systems. Accepted at RecSys 2026.
- **Key Innovations**: Causal residual modeling; probabilistic user clustering; do-calculus aggregation.
- **Impact**: Principled causal approach to improving existing recommender systems without architectural changes.

---

## 2. AI Agents & Training

### 2.1 OpenForgeRL: Train Harness-native Agents in Any Environment
- **Authors**: Xiao Yu, Baolin Peng, Ruize Xu, Hao Zou, Qianhui Wu, Hao Cheng, Wenlin Yao, Nikhil Singh, Zhou Yu, Jianfeng Gao
- **Date**: 23 Jul 2026
- **arXiv**: 2607.21557
- **Abstract**: Open-source framework for training harness-based agents end-to-end in diverse environments. Uses a lightweight proxy to serve the harness's model calls while recording them as training data for a standard RL codebase (evel), and a Kubernetes orchestrator that runs each rollout in its own remote container. OpenForgeClaw reaches 31.7 pass^3 and 55.9 pass@3 on ClawEval. OpenForgeGUI reaches 37.7 on OSWorld-Verified, 63.0 on Online-Mind2Web, and 72.3 on WebVoyager. Finds that some harnesses are substantially harder to learn than others, and RL improves agentic reliability (self-verification, tool coverage, multi-step plans), though error recovery remains weak.
- **Key Innovations**: Decoupled training/inference for harness-based agents; Kubernetes-orchestrated rollouts; multi-harness compatibility.
- **Impact**: Makes end-to-end RL training practical for production agent harnesses (Claude Code, Codex, OpenClaw).

### 2.2 AREX: Recursively Self-Improving Agent for Deep Research
- **Authors**: Shuqi Lu, Chaofan Li, Kun Luo, et al. (24 authors)
- **Date**: 23 Jul 2026
- **arXiv**: 2607.21461
- **Abstract**: Introduces a family of Recursively Self-Improving (RSI) deep research agents. Alternates between inner research loop (evidence gathering, provisional answer) and outer self-improvement loop (constraint-wise audit, targeted follow-up). Learns an autonomous context-update tool compressing interaction history into improvement state. Trains 4B dense and 122B-A10B MoE models. Outperforms comparable-scale baselines on BrowseComp, WideSearch, DeepSearchQA, and HLE.
- **Key Innovations**: Inner/outer RSI loops; autonomous context compression; key-step emphasis for long-horizon RL.
- **Impact**: Advances deep research agent paradigm with recursive self-improvement; competitive with much larger models.

### 2.3 Agentic Context Management: Solving Agent Memory and Cost
- **Authors**: Gaurav Dadhich
- **Date**: 24 Jul 2026
- **arXiv**: 2607.21503
- **Abstract**: Treats agent memory and cost as lifecycle and architecture problems rather than prompt engineering challenges. 23 pages with evaluation harness and study data.
- **Key Innovations**: Lifecycle-based agent memory management; architecture-level cost optimization.
- **Impact**: Reframes agent memory/cost from prompt-level to systems-level engineering.

### 2.4 GuardianAgentBench: Where Agents Fail and How to Guard Them
- **Authors**: Vishal Ishwar Naik, Chenyu Xu, Donna Dong, Hussein Hassan, Abhishek Pradhan, Ofer Mendelevitch, Tallat Shafat, Humayun Irshad
- **Date**: 24 Jul 2026
- **arXiv**: 2607.20982
- **Abstract**: Benchmark identifying where agents fail and proposing guardrail mechanisms.
- **Key Innovations**: Systematic agent failure analysis; guardrail design framework.
- **Impact**: Provides actionable failure taxonomy for production agent deployment.

### 2.5 AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning
- **Authors**: Qinfeng Li, Yuntai Bao, Xinyan Yu, Hongze Chen, Wenqi Zhang, Xuhong Zhang
- **Date**: 24 Jul 2026
- **arXiv**: 2607.21106
- **Abstract**: Attribution-guided process feedback mechanism for learning from agent memory.
- **Key Innovations**: Attribution-based memory learning; process-level feedback.
- **Impact**: Improves agent memory utilization through attribution-guided signals.

### 2.6 MemTools: A Unified Research Framework for Interoperable Agent Memory
- **Authors**: Chengfeng Zhao, Jinhui Chen, Sirui Liang, Shizhu He, Yequan Wang, Jun Zhao, Kang Liu
- **Date**: 24 Jul 2026
- **arXiv**: 2607.21404
- **Abstract**: Unified framework for interoperable agent memory systems.
- **Key Innovations**: Interoperable memory architecture; unified research framework.
- **Impact**: Standardizes agent memory interfaces for cross-system compatibility.

### 2.7 CAMeR: Keyword-Gated Hybrid Activation for Adaptive Memory Retention in LLM Agents
- **Authors**: Haowen Lai
- **Date**: 24 Jul 2026
- **arXiv**: 2607.20458
- **Abstract**: Keyword-gated hybrid activation mechanism for adaptive memory retention.
- **Key Innovations**: Keyword gating for memory activation; hybrid retention mechanism.
- **Impact**: Enables selective memory retention without full-context overhead.

---

## 3. RL & LLM Training

### 3.1 The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents
- **Authors**: Yu Wang
- **Date**: 23 Jul 2026
- **arXiv**: 2607.21273
- **Abstract**: Shows that dense per-step prediction rewards destroy GRPO-trained LLM agents. Across Qwen3-1.7B/4B/8B on ALFWorld, potential-based prediction reward drives every run into a degenerate "dark room" state (prediction accuracy -> 1.0, task success -> 0, episode length pinned at horizon). A single-factor ablation localizes the cause — removing GRPO's std normalization turns the same reward from catastrophic (0%) into baseline parity. In all-fail groups the z-scored advantage is invariant to the shaping coefficient, so bounded rewards become unbounded pressure. Proposes a variance-profile criterion that retrodicts collapses and makes preregistered predictions.
- **Key Innovations**: "Dark room" pathology characterization; GRPO std-normalization failure mode; variance-profile criterion; auxiliary-loss channel as alternative.
- **Impact**: Critical warning for GRPO-based agent training: dense rewards + z-scoring = policy destruction.

### 3.2 Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context
- **Authors**: Alagappan Valliappan
- **Date**: 24 Jul 2026
- **arXiv**: 2607.21535
- **Abstract**: Addresses the KV cache overhead in multi-token prediction at million-token context lengths. 25 pages, 2 figures, 11 tables.
- **Key Innovations**: Windowed draft-KV management for long-context MTP.
- **Impact**: Enables practical MTP deployment at million-token scales.

### 3.3 Token Budget Saturation and Mechanistic Early Detection of Reasoning Non-Convergence
- **Authors**: Renuka Oladri, Niveda Jawahar, Abdirisak Mohamed
- **Date**: 24 Jul 2026
- **arXiv**: 2607.21433
- **Abstract**: Studies when chain-of-thought reasoning models saturate their token budgets and how to detect non-convergence early.
- **Key Innovations**: Token budget saturation analysis; mechanistic early detection.
- **Impact**: Enables efficient resource allocation for reasoning-intensive inference.

### 3.4 Multi-turn RL with Structural and Performance Aware Rewards for CUDA Kernel Generation
- **Authors**: Quazi Ishtiaque Mahmud, Nesreen K. Ahmed, Ali Jannesari
- **Date**: 24 Jul 2026
- **arXiv**: 2607.20908
- **Abstract**: Multi-turn RL approach for generating CUDA kernels with structural and performance aware rewards.
- **Key Innovations**: Structural + performance aware rewards; multi-turn RL for code generation.
- **Impact**: Advances automated CUDA kernel optimization via RL.

---

## 4. LLM Efficiency & Architecture

### 4.1 Error Certificates for KV-Cache Eviction via Randomized Design
- **Authors**: Peng Xie
- **Date**: 24 Jul 2026
- **arXiv**: 2607.21475
- **Abstract**: Provides error certificates for KV-cache eviction strategies using randomized design.
- **Key Innovations**: Formal error bounds for KV-cache eviction; randomized design for provable guarantees.
- **Impact**: Enables reliable KV-cache eviction with worst-case guarantees.

### 4.2 Progressive Cramming: Reliable Token Compression and What It Reveals
- **Authors**: Dmitrii Tarasov, Timofei Lashukov, Elizaveta Goncharova, Andrey Kuznetsov
- **Date**: 24 Jul 2026
- **arXiv**: 2607.21231
- **Abstract**: Studies reliable token compression techniques and their implications for understanding model behavior.
- **Key Innovations**: Progressive compression framework; reliability analysis.
- **Impact**: Improves understanding of what survives compression.

### 4.3 Adaptive Depth Sparse Framework: Similarity-Driven Resource Allocation for Pre-Trained LLMs
- **Authors**: Yidu Wu, Xiang Wang, Kejie Zhao, Zhangchi Wang, Qinghai Guo, Xiaoying Tang
- **Date**: 24 Jul 2026
- **arXiv**: 2607.21291
- **Abstract**: Similarity-driven resource allocation that adaptively adjusts computation depth for pre-trained LLMs. Accepted at ICIC 2026.
- **Key Innovations**: Adaptive depth sparsity; similarity-driven routing.
- **Impact**: Reduces LLM inference cost via input-adaptive computation.

### 4.4 KroQuant: Kronecker-Structured Block Transforms for Efficient Post-Training Quantization of Diffusion Transformers
- **Authors**: Yann Bouquet, Alireza Khodamoradi, Kristof Denolf, Mathieu Salzmann
- **Date**: 24 Jul 2026
- **arXiv**: 2607.21446
- **Abstract**: Kronecker-structured block transforms for post-training quantization of diffusion transformers.
- **Key Innovations**: Kronecker-structured quantization; diffusion transformer compatibility.
- **Impact**: Enables efficient deployment of diffusion transformers on resource-constrained hardware.

---

## 5. Safety & Evaluation

### 5.1 Robust Critics: Defending LLMs Against Multi-Turn Attacks
- **Authors**: Roman Belaire, Arunesh Sinha, Pradeep Varakantham
- **Date**: 24 Jul 2026
- **arXiv**: 2607.21557 (cross-list)
- **Abstract**: Proposes Dialogue Critic Guided Sampling (DCGS) for inferring user intent at every turn of adversarial dialogue. Models adversarial dialogue as MDP with value and regret-based critics at token and utterance levels. Proves inference-time reweighting approximates exponential tilting, guaranteeing improvement for any finite candidate pool. Transfers to frontier models without fine-tuning.
- **Key Innovations**: Per-turn intent inference; dual-level critics; theoretical improvement guarantee; transferability.
- **Impact**: Moves beyond contextual bandit safety to full trajectory-level adversarial defense.

### 5.2 AI Assistants Overassist
- **Authors**: Verona Teo, Raghav Jain, Tobias Gerstenberg, Max Kleiman-Weiner
- **Date**: 24 Jul 2026
- **arXiv**: 2607.21306
- **Abstract**: Studies when AI assistants provide excessive help that undermines user learning and autonomy.
- **Key Innovations**: Over-assistance characterization; human-AI interaction balance analysis.
- **Impact**: Highlights important UX/safety concern for AI assistant deployment.

### 5.3 Position Bias is Hidden Behind Ceiling Effects: A Permutation Diagnostic for LLM Benchmarks
- **Authors**: Hiroki Tamba
- **Date**: 24 Jul 2026
- **arXiv**: 2607.20864
- **Abstract**: Reveals that position bias in LLM benchmarks is masked by ceiling effects. Proposes permutation diagnostic. 25 pages, companion to arXiv:2606.26185.
- **Key Innovations**: Permutation-based bias detection; ceiling-effect masking diagnosis.
- **Impact**: Exposes hidden evaluation bias in widely-used LLM benchmarks.

---

## Summary

### Key Themes

1. **Diffusion for Generative Recommendation**: DLMRec introduces discrete diffusion as an alternative to autoregressive generation for recommendation, challenging the dominant paradigm while DLMRec's collaborative-aware tokenizer addresses the structural gap.

2. **Cold-Start Limits of Semantic-IDs**: The temporal analysis of SID-based generative recommendation reveals that while compositional, current approaches are not fully open-ended for cold items — a fundamental limitation for production deployment.

3. **GRPO Dense Reward Pathology**: The "dark room" paper delivers a critical warning: dense prediction rewards + GRPO's z-score normalization = policy destruction. This has immediate implications for anyone training LLM agents with GRPO.

4. **Agent Memory as Architecture**: Three papers (Agentic Context Management, MemTools, CAMeR) converge on the insight that agent memory is an architecture-level problem, not a prompt engineering challenge.

5. **Harness-Native Agent Training**: OpenForgeRL decouples training from inference harnesses, enabling end-to-end RL for production agent systems (Claude Code, Codex) — a practical engineering advance for the agent era.

6. **Recursive Self-Improvement for Research**: AREX demonstrates that inner/outer RSI loops with autonomous context compression can make deep research agents competitive with much larger models.

### Statistics
- **Total Papers Reviewed**: 25+
- **CTR/Recommendation**: 6 papers (2 with RecSys 2026 acceptance, 1 with ICTIR 2026)
- **AI Agents & Training**: 7 papers
- **RL & LLM Training**: 4 papers
- **LLM Efficiency & Architecture**: 4 papers
- **Safety & Evaluation**: 3 papers

---

*Generated on 2026-07-25*
