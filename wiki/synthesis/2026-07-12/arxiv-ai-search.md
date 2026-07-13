---
title: "arXiv AI Search Report"
type: synthesis
created: 2026-07-12
updated: 2026-07-12
sources: []
tags: [arxiv, ai, llm, recommendation, ctr, sequential-modeling, advertising, games, search]
---

# arXiv AI Search Report — 2026-07-12

Curated selection of recent arXiv papers across AI, LLMs, recommendation systems, advertising/CTR prediction, sequential user modeling, and games.

---

## 1. Recommendation Systems

### 1.1 SCOReD: Student-Aware CoT Optimization for Recommendation Distillation
- **Authors:** Haz Sameen Shahgir, Yufei Li, Frank Shyu, Luke Simon, Sandeep Pandey, Xi Liu, Yue Dong
- **Date:** 2026-07-07
- **Link:** [arXiv:2607.05734](https://arxiv.org/abs/2607.05734)
- **Abstract:** Chain-of-thought (CoT) distillation in the recommendation domain is a necessary precursor to RL training, but raw teacher traces are ill-suited to this task. Large teachers approach the recommendation task with unusually high reasoning uncertainty, repeatedly rechecking their answers without revising them; supervised fine-tuning on such traces produces verbose students that never revise their initial guess. SCOReD parses each teacher trace into typed segments and uses the student LLM's attention to score segment importance, then dynamically selects a per-segment edit (KEEP/REWRITE/FUSE/PRUNE) based on output length and comparative log probability lift. Training on SCOReD-optimized CoTs improves over baseline SFT by 1.56% NDCG and 1.9% Recall@5, while reducing reasoning length by 27.3%.
- **Key Innovations:** Student-aware CoT optimization framework for recommendation distillation; attention-based segment importance scoring; dynamic per-segment edit selection (KEEP/REWRITE/FUSE/PRUNE); 27.3% reasoning length reduction with improved accuracy.

### 1.2 Autonomous Information Seeking: A Roadmap for Agentic Recommender Systems
- **Authors:** Xinyu Lin, Yashar Deldjoo, Sunhao Dai, Honghui Bao, Xiaopeng Ye, Fatemeh Nazary, Wenjie Wang, Tommaso Di Noia, Jun Xu, Tat-Seng Chua
- **Date:** 2026-07-05
- **Link:** [arXiv:2607.04433](https://arxiv.org/abs/2607.04433)
- **Abstract:** Comprehensive survey of LLM-based agents in recommender systems, introducing a unified taxonomy grounded in autonomy level and three core paradigms: agent-assisted recommendation, agent-as-recommender, and agent-as-user-simulator. Analyzes agentic architectures and how agents enhance profiles, memory, tool use, workflows, and optimization. Discusses evaluation methodologies (automated metrics, LLM-based judging, simulation-based assessment) and open challenges in lifelong user modeling, contextual abstraction, multimodal alignment, controllability, trustworthiness, privacy, scalability, and efficiency.
- **Key Innovations:** Unified taxonomy of agentic recommender systems along autonomy dimensions; three paradigm framework (agent-assisted, agent-as-recommender, agent-as-user-simulator); comprehensive evaluation methodology analysis; roadmap of open challenges for agentic recommendation.

### 1.3 Bi-NAS: Towards Effective and Personalized Explanation for Recommender Systems via Bi-Level Neural Architecture Search
- **Authors:** Longfeng Wu, Yao Zhou, Tong Zeng, Zhimin Peng, Bhanu Pratap Singh Rawat, Lecheng Zheng, Giovanni Seni, Dawei Zhou
- **Date:** 2026-07-01
- **Link:** [arXiv:2607.01387](https://arxiv.org/abs/2607.01387)
- **Abstract:** Proposes a Bi-level Neural Architecture Search (Bi-NAS) framework to optimize recommendation explanations by simultaneously refining cross-attention mechanisms and feature interaction functions across intra-layer and inter-layer design spaces. Integrates LLMs via zero-shot prompting to produce effective and personalized justifications, aligning user feature preferences with item quality scores. Evaluated on four real-world datasets.
- **Key Innovations:** Bi-level NAS for explanation optimization; LLM-integrated zero-shot explanation generation; joint optimization of cross-attention and feature interaction functions.

### 1.4 Diffusion-GR2: Diffusion Generative Reasoning Re-ranker
- **Authors:** Zhuoxuan Zhang, Kangqi Ni, Yuhang Chen, Mingfu Liang, Xiaohan Wei, Yunchen Pu, Fei Tian, Chonglin Sun, Frank Shyu, Adam Song, Sandeep Pandey, Luke Simon, Tianlong Chen, Xi Liu
- **Date:** 2026-07-01
- **Link:** [arXiv:2607.01170](https://arxiv.org/abs/2607.01170)
- **Abstract:** Converts an autoregressive (AR) reasoning re-ranker into a block-diffusion re-ranker for faster inference. Addresses structural gap (invalid rankings from parallel denoising) via Conversion Fine-Tuning (CFT) and distributional gap via On-Policy Distillation (OPD) with an RL stage. Achieves near-parity with AR re-ranker while raising decode throughput by 2.4–3.5x at the model's reasoning output length on Amazon Beauty.
- **Key Innovations:** Block-diffusion conversion of AR re-rankers; CFT for valid permutation denoising; on-policy distillation with dense per-token targets; 2.4-3.5x throughput improvement.

### 1.5 Planning over Matrix-Factorization MDPs for Candidate Generation
- **Authors:** Mikhail Trapeznikov, Maksim Utushkin
- **Date:** 2026-07-02
- **Link:** [arXiv:2607.02115](https://arxiv.org/abs/2607.02115)
- **Abstract:** Casts top-K retrieval as an MDP over the implicit-ALS posterior, where an action is an item and the transition is a closed-form rank-one fold-in. Compares static retrieval, one-step planning, and horizon-K MCTS across five datasets. Dynamics-aware planning overcomes static retrieval under leave-last-n, with a single step of lookahead capturing most gains — no retraining or representation change required.
- **Key Innovations:** MDP formulation over implicit-ALS posterior for retrieval; fold-in transition as rank-one update; one-step lookahead planning improving static top-K scoring without retraining.

### 1.6 Multi-Level Graph Attention Network Contrastive Learning for Knowledge-Aware Recommendation
- **Authors:** Zhifei Hu, Feng Xia
- **Date:** 2026-05-08
- **Link:** [arXiv:2605.08499](https://arxiv.org/abs/2605.08499)
- **Abstract:** Addresses sparse labels, insufficient graph structure learning, and noisy entities in knowledge graphs for recommendation using multi-level graph attention networks with contrastive learning.
- **Key Innovations:** Multi-level graph attention with contrastive learning for knowledge-aware recommendation; addresses sparse labels and noisy entities in KG.

### 1.7 URecJPQ: Memory-efficient Multimodal Recommendation Models through RecJPQ in Large-Scale Scenarios
- **Authors:** Zixuan Yi, Iadh Ounis, Craig Macdonald
- **Date:** 2026-06-22
- **Link:** [arXiv (cs.IR)](https://arxiv.org/abs/2607.02115)
- **Abstract:** Addresses memory challenges in training state-of-the-art recommendation models on large-scale industrial datasets with high numbers of users and items represented through ID embeddings.
- **Key Innovations:** Memory-efficient multimodal recommendation for large-scale scenarios; RecJPQ compression technique.

---

## 2. CTR Prediction & Advertising

### 2.1 Generative Long-term User Interest Modeling for Click-Through Rate Prediction (GenLI)
- **Authors:** Jiangli Shao, Kaifu Zheng, Hao Fang, Huimu Ye, Zhiwei Liu, Bo Zhang, Shu Han, Xingxing Wang
- **Date:** 2026-05-15
- **Link:** [arXiv:2605.15905](https://arxiv.org/abs/2605.15905)
- **Abstract:** Proposes GenLI, a generative long-term user interest model for CTR prediction. Addresses limitations of target-centered GSU (general search unit) which ignores latent user interests and becomes time-consuming as behaviors grow. GenLI consists of an Interest Generation Module (IGM) generating multiple target-independent interest distributions, a Behavior Retrieval Module (BRM) using O(1) lookup, and an Interest Fusion Module (IFM).
- **Key Innovations:** Target-independent generative interest modeling; O(1) behavior retrieval via simple lookup; multiple interest distributions capturing diverse user aspects; interaction information among behaviors.

### 2.2 IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs
- **Authors:** Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan, Ruiyan Han, Feiyang Xiao, Yanhua Huang, Li Lin, Yang Luo, Yao Hu
- **Date:** 2026-03-02
- **Link:** [arXiv:2603.01590](https://arxiv.org/abs/2603.01590)
- **Abstract:** Leverages multimodal large language models (MLLMs) to generate proxy embeddings from rich content signals for cold-start CTR prediction. Proxy embeddings are explicitly aligned with existing ID embedding space and optimized end-to-end under CTR objectives. Deployed at Xiaohongshu serving hundreds of millions of users daily in Content Feed and Display Ads.
- **Key Innovations:** MLLM-based proxy embedding generation for cold-start; explicit alignment with ID embedding space; end-to-end optimization under CTR objectives; production deployment at Xiaohongshu.

### 2.3 GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm
- **Authors:** Shaopeng Chen, Chuyue Xie, Huimin Ren, Shaozong Zhang, Han Zhang, Ruobing Cheng, Zhiqiang Cao, Zehao Ju, Yu Gao, Jie Ding, Xiaodong Chen, Xuewu Jiao, Shuanglong Li, Lin Liu
- **Date:** 2026-02-04
- **Link:** [arXiv:2602.01865](https://arxiv.org/abs/2602.01865)
- **Abstract:** End-to-end generative framework for CTR prediction inspired by LLM scaling laws. Integrates a novel Causal Action-aware Multi-channel Attention (CamA) mechanism to capture temporal dynamics and specific action signals within user behavior sequences. Full-scale online deployment at Baidu shows 3.05% revenue increase and 3.49% CTR rise, with monotonic and approximately linear improvement as longer interaction sequences are utilized.
- **Key Innovations:** LLM-inspired generative CTR framework; Causal Action-aware Multi-channel Attention (CamA); scaling behavior with longer sequences; 3.05% revenue increase in production at Baidu.

### 2.4 Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)
- **Authors:** Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Date:** 2026-06-03
- **Link:** [arXiv:2606.04944](https://arxiv.org/abs/2606.04944)
- **Abstract:** Proposes DS-MLP, a feature interaction framework using knowledge distillation to consolidate explicit feature interaction learning into a main MLP network, while a parallel MLP captures implicit feature interactions. Achieves state-of-the-art performance across three benchmarks with a vanilla MLP structure, offering a scalable and efficient solution.
- **Key Innovations:** Dual-stream MLP architecture with knowledge distillation; consolidation of explicit interactions into single MLP; parallel implicit interaction capture; SOTA with vanilla MLP.

### 2.5 CTR-Sink: Attention Sink for Language Models in Click-Through Rate Prediction
- **Authors:** Zixuan Li, Binzong Geng, Yong He, Jing Xiong, Jian Chen, Yuxuan Hu, Dingwei Chen, Liang Zhang, Xiyu Chang, Chenming Li, Chuan Yuan, Linjian Mo, Zhenan Sun
- **Date:** 2025/2026
- **Link:** [arXiv:2508.03668](https://arxiv.org/abs/2508.03668)
- **Abstract:** Addresses the structural gap between user behavior sequences (discrete actions with semantically empty separators) and coherent natural language in LMs. Proposes behavior-level attention sinks with sink tokens between consecutive behaviors incorporating recommendation-specific signals. Two-stage training guides LM attention toward sink tokens, and an attention sink mechanism amplifies inter-sink dependencies.
- **Key Innovations:** Behavior-level attention sinks for recommendation; sink tokens between behaviors with temporal distance signals; two-stage training strategy; addresses semantic fragmentation in LM-based CTR.

### 2.6 CELA: Cost-Efficient Language Model Alignment for CTR Prediction
- **Authors:** (Multiple authors)
- **Date:** 2025/2026 (Accepted)
- **Link:** [arXiv:2405.10596v3](https://arxiv.org/abs/2405.10596v3)
- **Abstract:** Model-agnostic framework incorporating item textual features and language models while preserving collaborative filtering capabilities of ID-based models. Online A/B test on industrial advertising recommender system shows +1.48% eCPM, +0.93% DTR, -19.41% training time.
- **Key Innovations:** Cost-efficient cross-modal alignment; plug-and-play textual features; item-level alignment preserving CF capabilities; production validated with significant eCPM gains.

### 2.7 Against Opacity: Explainable AI and Large Language Models for Effective Digital Advertising
- **Authors:** (Multiple authors)
- **Date:** 2025
- **Link:** [arXiv:2504.20064](https://arxiv.org/abs/2504.20064)
- **Abstract:** Uses explainable AI and LLMs to provide transparent CTR prediction for digital advertising. Introduces SoWide-v2 model incorporating campaign, ad set, and multiple creative features with Vision Transformer for image processing.
- **Key Innovations:** XAI for advertising transparency; SoWide-v2 multi-granularity feature incorporation; ViT-based ad creative processing.

---

## 3. Sequential User Behavior Modeling

### 3.1 Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Enhanced Sequential User Modeling
- **Authors:** Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang
- **Date:** 2026-06-13
- **Link:** [arXiv:2606.15252](https://arxiv.org/abs/2606.15252)
- **Abstract:** Demonstrates that mixed-polarity behavior sequences (interleaving positive and negative tokens within a fixed length budget) consistently outperform positive-only sequences across diverse model architectures. Proposes Target-Aware Polarity Fusion (TAPF), a lightweight target-conditioned gating mechanism. Experiments on three public benchmarks show +1.9% to +9.6% relative AUC across five architectures.
- **Key Innovations:** Mixed-polarity behavior sequence paradigm (positive + negative interactions); Target-Aware Polarity Fusion (TAPF) gating; +1.9% to +9.6% AUC improvement; negative behavior signals as underutilized data source.

### 3.2 Multi-Behavior Sequential Modeling with Transition-Aware Graph Attention Network (TGA) for E-Commerce Recommendation
- **Authors:** Hanqi Jin, Gaoming Yang, Zhangming Chan, Yapeng Yuan, Longbin Li, Fei Sun, Yeqiu Yang, Jian Wu, Yuning Jiang, Bo Zheng
- **Date:** 2026-01-21
- **Link:** [arXiv:2601.14955](https://arxiv.org/abs/2601.14955)
- **Abstract:** Linear-complexity approach for modeling multi-behavior transitions using a structured sparse graph from three perspectives: item-level, category-level, and neighbor-level transitions. Transition-aware graph attention jointly models user-item interactions and behavior transition types, significantly reducing computational cost while outperforming state-of-the-art models.
- **Key Innovations:** Linear-complexity multi-behavior transition modeling; three-perspective structured sparse graph construction; transition-aware graph attention mechanism; scales to long user sequences.

### 3.3 HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction
- **Authors:** (Multiple authors)
- **Date:** 2026-01-20
- **Link:** [arXiv (cs.IR)](https://arxiv.org/abs/2403.17729v2)
- **Abstract:** Revisits the roles of sequence modeling and feature interaction in CTR prediction, examining how to jointly process sequential and non-sequential features.
- **Key Innovations:** Unified framework for sequence modeling and feature interaction; revisits architectural choices for CTR.

---

## 4. LLMs (General & Architecture)

### 4.1 Understanding Large Language Models
- **Authors:** Yannik Keller, Thomas Eisenmann
- **Date:** 2026-07-01
- **Link:** [arXiv:2607.01006](https://arxiv.org/abs/2607.01006)
- **Abstract:** Chapter-style survey outlining current understanding of LLMs, covering Transformer architecture, emergent capabilities (symbolic reasoning, theory of mind, deception), explainable AI approaches (neuron activation analysis, circuit tracing), and debates about LLM cognition vs. pattern memorization. Advocates for a nuanced discussion that neither dismisses differences between humans and LLMs nor precludes AI cognition through overly simplistic reductionist arguments.
- **Key Innovations:** Comprehensive survey of LLM mechanisms and capabilities; analysis of emergent cognitive-like behaviors; review of XAI approaches for LLMs; nuanced framework for discussing LLM cognition.

### 4.2 Geometry Conflict: Explaining and Controlling Forgetting in LLM Continual Post-Training (GCWM)
- **Authors:** Yuanyi Wang et al.
- **Date:** 2026-05-10
- **Link:** [arXiv:2605.09608](https://arxiv.org/abs/2605.09608)
- **Abstract:** Addresses forgetting in LLM continual post-training through task geometry analysis. Proposes Geometry-Conflict Wasserstein Merging (GCWM), a data-free update-integration method using Gaussian Wasserstein barycenters and geometry conflict gating. Consistently outperforms data-free baselines across Qwen3 0.6B-14B on domain-continual and capability-continual settings.
- **Key Innovations:** Geometry conflict as explanatory signal for forgetting; Wasserstein metric-based update integration; data-free continual learning for LLMs; geometry-aware correction gating.

### 4.3 Edge Deployment: Multi-LoRA One-for-All Foundational LLM on Samsung Devices
- **Authors:** Sravanth Kodavanti et al.
- **Date:** 2026-04-20
- **Link:** [arXiv:2604.18655v2](https://arxiv.org/abs/2604.18655v2) (Accepted at ACL 2026)
- **Abstract:** Hardware-aware framework for efficient on-device LLaMA inference supporting multiple use cases via application-specific LoRAs on Samsung Galaxy S24/S25 with Qualcomm chipsets. Multi-stream decoding generates stylistic variations within a single forward pass (up to 6x latency reduction). Dynamic Self-Speculative Decoding yields up to 2.3x decode speedup. Combined with INT4 quantization, achieves 4-6x memory/latency improvements across 9 languages and 8 tasks.
- **Key Innovations:** Multi-LoRA runtime switching without recompilation; multi-stream decoding for parallel style variations; Dynamic Self-Speculative Decoding (DS2D); 4-6x overall improvement on edge devices.

---

## 5. Games & Game AI

### 5.1 Superhuman AI for Generals.io Using Self-Play Reinforcement Learning
- **Authors:** Matej Straka, Viliam Lisý, Martin Schmid
- **Date:** 2026-06-22
- **Link:** [arXiv:2606.23348](https://arxiv.org/abs/2606.23348)
- **Abstract:** Superhuman AI agent for Generals.io, a real-time strategy game requiring long-horizon planning and short-term tactics under imperfect information. Trained for 4 days on 4x NVIDIA H200 GPUs, reaches #1 on the 5,000+ player leaderboard, beats top-ranked humans 199-70 in 269 ladder matches. Key enabler: JAX-native simulator reaching tens of millions of FPS on a single GPU (~10,000x speedup). Uses ViT policy trained end-to-end by self-play with policy-gradient and sparse win/loss reward.
- **Key Innovations:** 10,000x faster JAX-native simulator; ViT policy with self-play policy-gradient; top-advantage sample filtering; superhuman performance in imperfect-information RTS.

### 5.2 Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with Large Language Models
- **Authors:** Yuchen Wang et al.
- **Date:** 2026-04-23
- **Link:** [arXiv:2604.21896](https://arxiv.org/abs/2604.21896)
- **Abstract:** Interactive agentic engineering environment enabling users to create, customize, and deploy LLM-powered game agents. Demonstrates capabilities across four game classes: dictionary-based (compressed state-action mappings), rigorously solvable (mathematical reasoning for optimal strategies), heuristic-based (minimax + crowd-sourced data), and learning-based (RL with human feedback and self-critique).
- **Key Innovations:** Programmable LLM game agent environment; four-class game strategy taxonomy; tool-augmented generation for strategic agents; self-programming AI concept via crowdsource learning and human creativity.

### 5.3 Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Player Games
- **Authors:** (Multiple authors)
- **Date:** 2026-05-06
- **Link:** [arXiv](https://arxiv.org/abs/2606.23348)
- **Abstract:** Teaches language models to play strategic games better through reinforcement learning, moving beyond greedy next-token generation to learn from move quality feedback.
- **Key Innovations:** RL-based strategic reasoning for LLMs in game settings; move quality feedback training.

### 5.4 Game Theory Driven Multi-Agent Framework Mitigates Language Model Hallucination
- **Authors:** Runzhe Liu, Biquan Bie, Zihao Wang et al.
- **Date:** 2026-07-10
- **Link:** [arXiv:2607.08403](https://arxiv.org/abs/2607.08403)
- **Abstract:** Uses game-theoretic multi-agent framework to mitigate LLM hallucination.
- **Key Innovations:** Game theory applied to LLM hallucination mitigation; multi-agent verification framework.

---

## 6. Cross-cutting Themes

### Key Trends Identified

1. **Generative paradigms in CTR/recommendation**: Multiple papers (GenLI, GRAB, Diffusion-GR2) move from discriminative scoring to generative modeling for ranking, leveraging LLM-inspired scaling and reasoning.

2. **LLM integration into production systems**: IDProxy (Xiaohongshu), GRAB (Baidu), CELA (advertising) show production-grade LLM integration for CTR with measured business impact.

3. **Mixed-polarity and negative signal modeling**: Beyond Positive Signals demonstrates that negative behaviors (skips, scroll-past) contain significant signal, with +1.9-9.6% AUC improvements.

4. **Efficient inference for reasoning**: Diffusion-GR2 and DS-MLP address the computational cost of reasoning-heavy recommendation, achieving 2.4-3.5x throughput gains.

5. **Edge deployment of LLMs**: Samsung/ACL 2026 paper demonstrates practical multi-LoRA deployment on mobile with 4-6x improvements.

6. **Self-play and superhuman game AI**: Generals.io paper shows that fast simulators + ViT self-play can achieve superhuman performance in complex imperfect-information games.

7. **Agentic recommendation**: The agentic recommender systems survey marks a paradigm shift from static pipelines to autonomous, interactive recommendation agents.
