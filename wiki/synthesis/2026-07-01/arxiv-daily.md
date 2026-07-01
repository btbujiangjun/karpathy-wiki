---
title: arXiv Daily — July 1, 2026
type: synthesis
created: 2026-07-01
updated: 2026-07-01
sources: []
tags: [arxiv, survey, llm, ctr, recommendation, advertising, rl, games, sequential-modeling]
---

# arXiv Daily — July 1, 2026

Recent papers across AI, LLMs, recommendation, advertising, CTR, sequential modeling, RL, and games.

---

## LLM Agents & RL

### 1. Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning
- **Authors**: Chengshuai Shi, Wenzhe Li, Xinran Liang, Yizhou Lu, Wenjia Yang, Ruirong Feng, Seth Karten, Ziran Yang, Zihan Ding, Gabriel Sarch, Danqi Chen, Karthik Narasimhan, Chi Jin
- **Affiliation**: Princeton University
- **Abstract**: Extends VLMs to long-horizon game playing (100+ turns) in Super Mario Land via RL. Proposes an adapted PPO with a lightweight turn-level critic that improves stability over GRPO/Reinforce++. Achieves 3x average game progress over frontier models with cross-game generalization.
- **Key Innovation**: Turn-level critic for long-horizon VLM RL; cross-game transfer without losing general capabilities.
- **Link**: https://arxiv.org/abs/2605.00347

### 2. Agentic Monte Carlo: Simulating Reinforcement Learning for Black-Box Agents
- **Authors**: Dae Yon Hwang, Raunaq Suri, Valentin Villecroze, Anthony L. Caterini, Jesse C. Cresswell, Noël Vouitsis, Brendan Leigh Ross
- **Affiliation**: Layer 6 AI
- **Abstract**: Treats black-box LLM agents as priors and uses Sequential Monte Carlo to sample from the optimal policy posterior without modifying model weights. Outperforms prompting baselines and matches/exceeds GRPO on AgentGym benchmarks as test-time compute scales.
- **Key Innovation**: Casts RL as Bayesian inference for API-only agents; SMC-based policy steering without parameter access.
- **Link**: https://arxiv.org/abs/2606.05296 (**ICML 2026**)

### 3. SPPO: Sequence-Level PPO for Long-Horizon Reasoning Tasks
- **Authors**: Tianyi Wang, Yixia Li, Long Li, Yibiao Chen, Shaohan Huang, Yun Chen, Peng Li, Yang Liu, Guanhua Chen
- **Abstract**: Reformulates reasoning as a Sequence-Level Contextual Bandit, collapsing the temporal horizon to eliminate bias of token-level credit assignment. Uses a decoupled scalar value function for low-variance advantage without multi-sampling. Matches GRPO's peak performance with 5.9x training speedup.
- **Key Innovation**: Sequence-level MDP → bandit reformulation; decoupled critic avoids value collapse.
- **Link**: https://arxiv.org/abs/2604.08865 (**ACL 2026 Main**)

### 4. SeeUPO: Sequence-Level Agentic-RL with Convergence Guarantees
- **Authors**: Tianyi Hu, Qingxu Fu, Yanxi Chen, Zhaoyang Liu, Bolin Ding
- **Abstract**: Analyzes convergence of RL algorithms in multi-turn agentic settings. Proposes SeeUPO, a critic-free approach modeling multi-turn interaction as sequentially executed multi-agent bandit problems with backward induction. Gains 43-54% on Qwen3-14B over baselines.
- **Key Innovation**: First critic-free method with proven convergence guarantees for multi-turn agent RL.
- **Link**: https://arxiv.org/abs/2602.06554

### 5. T-STAR: Reason in Chains, Learn in Trees — Self-Rectification and Grafting for Multi-turn Agent Policy Optimization
- **Authors**: Yu Li, Sizhe Tang, Tian Lan
- **Abstract**: Consolidates trajectories into a Cognitive Tree, merging functionally similar steps. Enables Introspective Valuation for variance-reduced step-level advantages and In-Context Thought Grafting that contrasts successful/failed branches for corrective reasoning.
- **Key Innovation**: Tree-structured credit assignment over chains; thought grafting for self-rectification.
- **Link**: https://arxiv.org/abs/2604.07165

### 6. GraphPO: Graph-based Policy Optimization for Reasoning Models
- **Authors**: Yuliang Zhan, Xinyu Tang, Jian Li, Dandan Zheng, Weilong Chai, Jingdong Chen, Jun Zhou, Ge Wu, Wenyue Tang, Hao Sun
- **Abstract**: Represents RL rollouts as a DAG with reasoning steps as edges and semantic states as nodes. Merges semantically equivalent paths into equivalence classes, reducing redundant exploration and providing process supervision from outcome.
- **Key Innovation**: Graph-structured rollouts over chain/tree; efficiency + correctness advantages per edge type.
- **Link**: https://arxiv.org/abs/2606.18954

### 7. From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning
- **Authors**: Chao Chen, Chengzu Li, Zhiwei Li, Yinhong Liu, Zhijiang Guo
- **Affiliation**: HKUST (GZ), University of Cambridge
- **Abstract**: Proposes LLM-as-Environment-Engineer where the policy model analyzes failures and proposes next-stage environment configurations. Introduces MAPF-FrozenLake testbed. Qwen3-4B as engineer outperforms GPT/Gemini and fixed-environment baselines.
- **Key Innovation**: Self-improving curriculum via LLM-designed environments; current RL checkpoint is a better engineer than base model.
- **Link**: https://arxiv.org/abs/2606.17682

### 8. GIFT: Games as Informal Training for Generalizable LLMs
- **Authors**: Nuoyan Lyu, Bingbing Xu, Xueyun Tian, Weihao Meng, Yige Yuan, Yang Zhang, Zhiyong Huang, Tat-Seng Chua, Huawei Shen
- **Abstract**: Introduces informal learning via games (Matrix Games, TicTacToe, Who's the Spy) into LLM training. Proposes Coordinated Subtask Training (CST) with sequential subtask-specific updates to replace naive task mixing.
- **Key Innovation**: Games as annotation-free, feedback-driven informal training environments; CST separates heterogeneous RL signals.
- **Link**: https://arxiv.org/abs/2601.05633

### 9. Self-Compacting Language Model Agents
- **Authors**: Tianjian Li et al.
- **Abstract**: SelfCompact — a scaffold where the model decides when/how to compact its context via a compaction tool + lightweight rubric. Matches/exceeds fixed-interval summarization at 30-70% lower token cost.
- **Key Innovation**: Adaptive model-driven context compaction; reveals meta-cognitive gap in unprompted models.
- **Link**: https://arxiv.org/abs/2606.23525

---

## CTR Prediction & Advertising Recommendation

### 10. GR4AD: Generative Recommendation for Large-Scale Advertising
- **Authors**: Ben Xue, Dan Liu, Lixiang Wang, et al. (30 authors, Kuaishou)
- **Affiliation**: Kuaishou
- **Abstract**: Production-oriented generative recommender with UA-SID tokenization, LazyAR decoder, Value-Aware Supervised Learning, and Ranking-Guided Softmax Preference Optimization (RSPO). Fully deployed at Kuaishou (400M+ users). Up to 4.2% ad revenue improvement over DLRM.
- **Key Innovation**: First full-scale generative recommender in advertising; LazyAR relaxes layer-wise dependencies for short multi-candidate generation; dynamic beam serving.
- **Link**: https://arxiv.org/abs/2602.22732

### 11. GRAB: An LLM-Inspired Sequence-First CTR Prediction Modeling Paradigm
- **Authors**: Shaopeng Chen, Chuyue Xie, Huimin Ren, et al. (14 authors)
- **Affiliation**: Baidu
- **Abstract**: End-to-end generative CTR framework with Causal Action-aware Multi-channel Attention (CamA). Deployed at Baidu. 3.05% revenue increase, 3.49% CTR lift. Expressive power scales linearly with longer sequences.
- **Key Innovation**: LLM-style sequence-first paradigm for CTR; CamA captures temporal dynamics + action signals.
- **Link**: https://arxiv.org/abs/2602.01865

### 12. DAIAN: Deep Adaptive Intent-Aware Network for CTR Prediction in Trigger-Induced Recommendation
- **Authors**: Alibaba Group (Xianyu)
- **Abstract**: Addresses intent myopia in trigger-induced recommendation. Extracts personalized intent representations from user click-trigger correlations. Hybrid enhancer with ID + semantic information overcomes sparse collaborative behaviors.
- **Key Innovation**: Dynamic intent adaptation beyond trigger-only focus; three-stage training for fusion convergence.
- **Link**: https://arxiv.org/abs/2602.13971

### 13. Dual-Stream MLP is All You Need for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Affiliation**: Renmin University of China, ByteDance, Meituan
- **Abstract**: Uses knowledge distillation to consolidate explicit feature interaction into a main MLP while a parallel MLP captures implicit interactions. Final model is a vanilla MLP achieving SOTA across three benchmarks.
- **Key Innovation**: Distillation-based dual-stream fusion collapses to single MLP at inference; alignment strategies prevent module imbalance.
- **Link**: https://arxiv.org/abs/2606.04944 (**TKDD**)

### 14. GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Hongyu Lu, Ji-Rong Wen
- **Affiliation**: Renmin University of China
- **Abstract**: Generative framework using NTP-trained model to produce candidate interest cohorts as explicit representations of immediate user intent. Hierarchical candidate-aware network injects cohort context into ranking via cross-attention.
- **Key Innovation**: Generative interest cohorts bridge recall and ranking; addresses interest shift beyond historical matching.
- **Link**: https://arxiv.org/abs/2601.18251 (**WWW 2026**)

### 15. IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs
- **Authors**: Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan, et al.
- **Affiliation**: Xiaohongshu
- **Abstract**: Leverages MLLMs to generate proxy embeddings for cold-start items from rich content signals, aligned with existing ID embedding space. Deployed in Xiaohongshu's Explore Feed (Content Feed + Display Ads).
- **Key Innovation**: MLLM-generated proxy embeddings aligned end-to-end with CTR objectives for cold-start.
- **Link**: https://arxiv.org/abs/2603.01590

### 16. RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems
- **Authors**: Jin Chen, Shangyu Zhang, Bin Hu, et al. (19 authors)
- **Affiliation**: Tencent (Weixin)
- **Abstract**: Addresses representation collapse in deep MetaFormer-based recommenders. Proposes randomized permutation splitting, multi-embedding paradigm, global token integration, and crossed pretrained embeddings. Deployed in Weixin Video Accounts, Official Accounts, Moments — GMV lifts of 3.41%, 4.81%, 2.12%.
- **Key Innovation**: Mitigates damped oscillatory effective rank across layers with multi-embedding + global token integration.
- **Link**: https://arxiv.org/abs/2604.17878

### 17. OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation
- **Authors**: Tencent (Weixin Channels)
- **Abstract**: Achieves architectural-level deep integration of generation and ranking via value-aware multi-task decoupling, coarse-to-fine target awareness, and input-output dual-side consistency. Deployed in Weixin Channels advertising. GMV-Normal +1.34%.
- **Key Innovation**: Single model for generation + ranking; task token sequences + causal mask separate interest/value optimization.
- **Link**: https://arxiv.org/abs/2603.02999

---

## Emerging AI & Methods

### 18. CELEUS: Certifiable and Efficient LLM Evaluation via E-Processes
- **Authors**: Zhijian Zhou et al.
- **Abstract**: Uses e-processes for anytime-valid confidence intervals in LLM evaluation. Uncertainty-guided sampling + surrogate approximations reduce evaluated samples by 54-62% while preserving coverage guarantees.
- **Key Innovation**: First anytime-valid CIs for LLM evaluation with near-parametric shrinkage rate.
- **Link**: https://arxiv.org/abs/2606.20820

### 19. MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery
- **Authors**: Enze Ma et al.
- **Abstract**: Benchmarks memory systems by recovering hidden user-state from agent memory artifacts. 50 simulated users, 31 hidden dimensions each (1,550 targets). Finds task completion and recoverable memory are distinct capabilities.
- **Key Innovation**: Direct memory recovery benchmark rather than downstream-task evaluation.
- **Link**: https://arxiv.org/abs/2606.24595

### 20. Language-Based Digital Twins for Elderly Cognitive Assistance
- **Authors**: Mohammad Mehdi Hosseini, Mohammad H. Mahoor, Hiroko H. Dodge
- **Abstract**: LLM-based digital twins mimicking conversational behavior of elderly using stylometric cues. Multi-head cVAE evaluates reconstruction quality and cognitive scores (MoCA). Outperforms GPT-generated responses on I-CONECT dataset.
- **Key Innovation**: Language biomarkers + digital twin for non-invasive cognitive health monitoring.
- **Link**: https://arxiv.org/abs/2606.27334 (**PETRA 2026**)

---

## Themes & Trends

1. **Generative CTR/Recommendation**: 2026 saw the full-scale deployment of generative paradigms in advertising (GR4AD at Kuaishou, GRAB at Baidu, OneRanker at Tencent), displacing traditional DLRM cascades.
2. **RL for Reasoning/Agents**: Sequence-level and graph-structured policy optimization methods (SPPO, GraphPO, T-STAR) replace token-level PPO and GRPO for long-horizon tasks.
3. **Black-Box Agent Optimization**: AMC and SeeUPO tackle the problem of optimizing API-only agents without parameter access.
4. **Games as Training**: Odysseus and GIFT treat games as rich, annotation-free environments for training generalizable VLM/LLM agents.
5. **Representation Quality**: RankUp and DS-MLP highlight the importance of feature interaction quality and representational rank in deep recommenders.
