---
title: "arXiv Daily — June 19, 2026"
type: synthesis
created: 2026-06-19
updated: 2026-06-19
sources: []
tags: [arxiv-daily, llm, recommendation, ctr, games, rl, sequential-modeling]
---

# arXiv Daily — June 19, 2026

Recent papers across AI, LLMs, recommendation, advertising, CTR, sequential modeling, and games. Sourced from cs.LG, cs.AI, cs.IR, cs.CL recent submissions (Jun 15–19, 2026).

---

## LLMs & Reasoning

### 1. VIMPO: Value-Implicit Policy Optimization for LLMs
- **Authors**: Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song, Xuandong Zhao
- **Institution**: UC Berkeley, MIT
- **Abstract**: Introduces a critic-free policy optimization method that derives a policy-implied value function from KL-regularized RL optimality conditions. Separates reward incorporation (value loss) from policy improvement (PPO-style actor update). Improves over GRPO on MATH-500, AIME 2024/2025, OlympiadBench.
- **Key Innovation**: No critic network needed — value function is implicit from policy-reference log-ratios. Simpler than actor-critic, finer credit assignment than GRPO.
- **Link**: https://arxiv.org/abs/2606.20008

### 2. Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning
- **Authors**: Xuanzhi Feng, Zhengyang Li, Zeyu Liu, et al.
- **Institution**: PolyU, NTU
- **Abstract**: Proposes Independent Combinatorial Tokens (ICT) framework using JS divergence between token logit distributions to identify critical branching points for RLVR exploration. Proves dual regulation of Shannon and Rényi entropy. Updating top 10% unique tokens yields +4.58% avg pass@4 over GRPO across 7 benchmarks.
- **Key Innovation**: Moves from scalar uncertainty (entropy) to distributional properties of logits. Token-level selective update prevents both entropy collapse and explosion.
- **Link**: https://arxiv.org/abs/2606.19771

### 3. Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning
- **Authors**: Yanxi Chen, Weijie Shi, Yuexiang Xie, Boyi Hu, Yaliang Li, Bolin Ding, Jingren Zhou
- **Institution**: Alibaba Group
- **Abstract**: Framework for training LLMs as long-lifecycle agents that solve sequences of tasks while continuously exploring, learning from experience, and self-updating context. Uses GRPO-style RL with fine-grained credit assignment, interleaving solve-task and update-context episodes.
- **Key Innovation**: Meta-capability training for agents that must learn across tasks and domains over time, with OOD generalization demonstrated.
- **Link**: https://arxiv.org/abs/2606.20002

### 4. Rethinking Reward Supervision: Rubric-Conditioned Self-Distillation
- **Authors**: Siyi Gu, Jialin Chen, Sophia Zhou, Arman Cohan, Rex Ying
- **Institution**: Yale, MBZUAI
- **Abstract**: New reward modeling paradigm where LLMs self-distill from rubric-conditioned signals rather than scalar rewards, improving alignment without reward model training.
- **Key Innovation**: Rubric-based conditioning enables finer-grained supervision than scalar reward models.
- **Link**: https://arxiv.org/abs/2606.19327

---

## Recommendation Systems & Advertising (CTR)

### 5. Structuring and Tokenizing Distributed User Interest Context for Generative Recommendation (G2Rec)
- **Authors**: Ruizhong Qiu, Yinglong Xia, Dongqi Fu, et al.
- **Institution**: Meta (Xia, Fu, Chen, Fan, Li, Yan)
- **Abstract**: Scalable framework unifying holistic graph-based user co-engagement modeling with semantic tokenization for industrial generative recommendation. Captures holistic user interest prototypes without ground-truth labels. Deployed across Meta product surfaces.
- **Key Innovation**: Combines graph-based user modeling with semantic tokenization for generative rec at scale.
- **Link**: https://arxiv.org/abs/2606.20554

### 6. Token Factory: Efficiently Integrating Diverse Signals into Large Recommendation Models
- **Authors**: Xilun Chen, Shao-Chuan Wang, Baykal Cakici, Lukasz Heldt, Lichan Hong, Raghu Keshavan, Aniruddh Nath, Li Wei, Xinyang Xi
- **Institution**: Google (Mountain View)
- **Abstract**: Framework transforming traditional recommendation signals into "soft tokens" for LRMs. Prevents prompt length explosion while compressing heterogeneous features. Validated in production-scale recommendation environment.
- **Key Innovation**: Soft token transformation avoids textualizing signals, reducing memory/compute overhead in transformer-based recommenders.
- **Link**: https://arxiv.org/abs/2606.19635

### 7. OneRank: Unified Transformer-Native Ranking Architecture for Multi-Task Recommendation
- **Authors**: Jiakai Tang, Sunhao Dai, Kun Wang, et al.
- **Institution**: Renmin University, Kuaishou
- **Abstract**: Single transformer-native ranking architecture unifying multiple recommendation tasks. Accepted at KDD 2026.
- **Key Innovation**: Shared transformer backbone for multi-task ranking without separate towers.
- **Link**: https://arxiv.org/abs/2606.16838

### 8. Harmonizing Semantic and Collaborative in LLMs: Reasoning-based Embedding Generator for Sequential Recommendation
- **Authors**: Qidong Liu, Mingyao Huang, Moranxin Wang, et al.
- **Institution**: —
- **Abstract**: Uses LLM reasoning to generate embeddings that harmonize semantic and collaborative signals for sequential recommendation.
- **Key Innovation**: LLM-based reasoning bridges semantic item understanding with collaborative filtering patterns.
- **Link**: https://arxiv.org/abs/2606.16703

### 9. Memorization Behavior of LLMs in Generative Recommendation
- **Authors**: Sunwoo Kim, Sunkyung Lee, Clark Mingxuan Ju, et al.
- **Institution**: KAIST, Snap Inc.
- **Abstract**: Studies memorization in generative recommenders — observations, implications, and training strategies to mitigate over-memorization while maintaining utility.
- **Key Innovation**: First systematic study of memorization in generative recommendation, with mitigation strategies.
- **Link**: https://arxiv.org/abs/2606.17276

### 10. Denoising Implicit Feedback for Cold-start Recommendation
- **Authors**: Gaode Chen, Shicheng Wang, Shikun Li, et al.
- **Institution**: Kuaishou Technology
- **Abstract**: Denoising approach for implicit feedback in cold-start scenarios. Accepted at KDD 2026 ADS Track.
- **Key Innovation**: Cold-start specific denoising that distinguishes genuine preferences from noisy interactions.
- **Link**: https://arxiv.org/abs/2606.19658

### 11. VCG: Multimodal Retrieval for E-Commerce Video Feeds under Extreme Cold-Start
- **Authors**: Katya Mirylenka, Egor Malykh, Mahdyar Ravanbakhsh, et al.
- **Institution**: Zalando
- **Abstract**: Multimodal retrieval framework for e-commerce video feeds that handles items with no historical interaction data.
- **Key Innovation**: Extreme cold-start in video-first e-commerce via multimodal content understanding.
- **Link**: https://arxiv.org/abs/2606.19627

### 12. SAERec: Fine-grained Interpretable Intents Priors via Sparse Autoencoders for Recommendation
- **Authors**: Jiangnan Xia, Xuansheng Wu, Yu Yang, Xin Wang, Ninghao Liu
- **Institution**: University of Georgia, Texas A&M
- **Abstract**: Uses sparse autoencoders to discover fine-grained interpretable user intents as priors for recommendation.
- **Key Innovation**: SAE-based interpretable intent discovery for transparent recommendation.
- **Link**: https://arxiv.org/abs/2606.18897

### 13. Do Generative Recommenders Deepen the Information Cocoon?
- **Authors**: Jiyuan Yang, Gengxin Sun, Mengqi Zhang, et al.
- **Institution**: Shandong University
- **Abstract**: Closed-loop simulation with LLM-powered user simulators to study whether generative recommenders exacerbate filter bubbles.
- **Key Innovation**: User simulator-based evaluation framework for information cocoon effect in generative rec.
- **Link**: https://arxiv.org/abs/2606.17707

---

## Games & Multi-Agent RL

### 14. Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution
- **Authors**: Jannik Hösch, Alessandro Sestini, Florian Fuchs, et al.
- **Institution**: Embracer Games, KAUST, KTH
- **Abstract**: LLM acts as centralized strategic controller selecting among specialized RL skill policies for a team of agents in 2v2 King of the Hill. 60% of users perceive LLM+RL agents as most human-like.
- **Key Innovation**: Hybrid LLM (planning) + RL (execution) hierarchy outperforms Flat RL and matches hand-crafted behavior trees.
- **Link**: https://arxiv.org/abs/2606.20014

### 15. Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini, Joakim Bergdahl, Amir Baghi, et al.
- **Institution**: Embracer Games
- **Abstract**: Vision paper proposing a framework for deploying RL-augmented game AI. Identifies bottlenecks in player-facing ML agents and promising research directions. Published at Conference on Games 2026.
- **Key Innovation**: Practical deployment framework for RL in commercial game production.
- **Link**: https://arxiv.org/abs/2606.20210

---

## Sequential Modeling & Architecture

### 16. Direct Advantage Estimation for Scalable Deep RL
- **Authors**: Hsiao-Ru Pan, Bernhard Schölkopf
- **Institution**: MPI for Intelligent Systems, Tübingen
- **Abstract**: New advantage estimation method for scalable and sample-efficient deep RL. Accepted at RLC 2026.
- **Key Innovation**: More efficient advantage estimation without requiring full trajectory rollouts.
- **Link**: https://arxiv.org/abs/2606.20411

### 17. The Token Is a Group Element: Lie-Algebra Attention over Matrix Lie Groups
- **Authors**: Przemyslaw Musialski
- **Institution**: NJIT
- **Abstract**: Reformulates attention where tokens are elements of matrix Lie groups, enabling geometric structure-aware sequence modeling.
- **Key Innovation**: Geometric deep learning meets attention — tokens as group elements for structured sequence modeling.
- **Link**: https://arxiv.org/abs/2606.20547

### 18. Marginal Advantage Accumulation for Memory-Driven Agent Self-Evolution
- **Authors**: Mingyu Yang, Keye Zheng, Congchao Cheng, et al.
- **Institution**: —
- **Abstract**: Agents that accumulate marginal advantages from memory to drive self-evolution without external supervision.
- **Key Innovation**: Self-evolution mechanism driven by accumulated advantage signals from episodic memory.
- **Link**: https://arxiv.org/abs/2606.20475

### 19. What Makes Effective Supervision in Latent Chain-of-Thought: An Information-Theoretic Analysis
- **Authors**: Xinghao Chen, Chak Tou Leong, et al.
- **Institution**: —
- **Abstract**: Information-theoretic analysis of supervision signals in latent CoT reasoning, identifying what makes supervision effective.
- **Key Innovation**: Theoretical framework linking supervision quality to mutual information in latent reasoning chains.
- **Link**: https://arxiv.org/abs/2606.20075

### 20. On the Redundancy of Timestep Embeddings in Diffusion Models
- **Authors**: José A. Chávez
- **Abstract**: Shows timestep embeddings in diffusion models are largely redundant and can be heavily compressed or removed.
- **Key Innovation**: Challenges a core design assumption of diffusion models.
- **Link**: https://arxiv.org/abs/2606.20416

---

## RAG & Information Retrieval

### 21. ScoreGate: Adaptive Chunk Selection for RAG via Dual-Score Statistical Fusion
- **Authors**: Karamvir Singh, Arvind Jain
- **Abstract**: Lightweight score-space mechanism controlling retrieval cardinality at inference time using bi-encoder similarity and cross-encoder reranker scores — no extra model calls.
- **Key Innovation**: Adaptive K selection from existing pipeline scores.
- **Link**: https://arxiv.org/abs/2606.14269

### 22. LLM-Based User Personas for Recommendations at Scale
- **Authors**: Yu Xia, Lichan Hong, Ed H. Chi
- **Institution**: Google
- **Abstract**: LLM-generated user personas for enhancing recommendation at scale.
- **Key Innovation**: Scalable persona generation from behavioral data using LLMs.
- **Link**: https://arxiv.org/abs/2606.16952

### 23. Multi-Agent Transactive Memory
- **Authors**: To Eun Kim, Xuhong He, et al.
- **Institution**: University of Waterloo
- **Abstract**: Multi-agent system where agents develop shared transactive memory — knowing what other agents know.
- **Key Innovation**: Transactive memory for distributed LLM agent systems.
- **Link**: https://arxiv.org/abs/2606.19911

---

## Summary
This week's arXiv highlights: **RLVR optimization** continues to be a hot topic (VIMPO, ICT, Rubric-Conditioned Self-Distillation). **Generative recommendation** sees production deployments from Meta (G2Rec) and Google (Token Factory). **Games + AI** papers from Embracer Games show practical LLM+RL hierarchies for believable NPCs. **Long-lifecycle agents** emerge as a new training paradigm (Connect the Dots by Alibaba). On the theory side, Lie-algebra attention and the redundancy of diffusion timestep embeddings challenge established architectural assumptions.
