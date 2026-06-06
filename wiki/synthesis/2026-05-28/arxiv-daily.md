---
title: arXiv Daily — AI & CTR (May 28, 2026)
type: synthesis
created: 2026-05-29
updated: 2026-05-29
sources: [2605.28807, 2605.28742, 2605.28713, 2605.28699, 2605.28655, 2605.28405, 2605.28493, 2605.27856, 2605.27704, 2605.27450, 2605.26717]
tags: [arxiv, daily-digest, ai, ctr, agents, reasoning, recommendation, agi]
---

# arXiv Daily — AI & CTR (May 28, 2026)

Daily scan of arXiv new submissions in cs.AI, cs.LG, and cs.IR (Thu, May 28, 2026). 372 cs.AI + 39 cs.IR entries. Picks the most interesting papers.

---

## 🧠 AI Research

### 1. CORE: Contrastive Reflection Enables Rapid Improvements in Reasoning

**Authors:** Linas Nasvytis, Simon Jerome Han, Ben Prystawski, Satchel Grant, Noah D. Goodman, Judith E. Fan

**arXiv:** [2605.28742](https://arxiv.org/abs/2605.28742) | Submitted May 27, 2026

Non-parametric learning algorithm for rapid reasoning improvement. Compares past reasoning traces to generate compact natural-language "insights" — descriptions of strategies and constraints. Outperforms GRPO, GEPA, and MemRL on 4 reasoning tasks with far fewer rollouts. Works with as few as 5 training samples. More interpretable and context-efficient than weight-update or prompt-optimization approaches.

### 2. Thinking as Compression: Your Reasoning Model is Secretly a Context Compressor

**Authors:** Guoxin Ma, Yibing Liu, Chengzhengxu Li, Yu Liang, Yan Wang, Yueyang Zhang, Kecheng Chen, Zhaohan Zhang, Zhiyuan Sun, Daiting Shi

**arXiv:** [2605.28713](https://arxiv.org/abs/2605.28713) | Submitted May 27, 2026 | Under Review

Reveals that thinking models naturally compress long contexts by organizing task-relevant info. TaC (Thinking as Compression) prompts the model to generate thinking traces as shortened context, outperforming most dedicated compression methods. TaC-C adds reward-driven optimization for budget control, achieving 17.4% and 23.4% average F1 gains at 4x and 8x compression over strongest competitors.

### 3. TRACER: Turn-level Regret Matching with Inner Reinforcement Credit for Cooperative Multi-LLM Reasoning

**Authors:** Chusen Li, Zhou Liu, Shuigeng Zhou, Wentao Zhang

**arXiv:** [2605.28699](https://arxiv.org/abs/2605.28699) | Submitted May 27, 2026

Turn-level RL framework for cooperative multi-LLM reasoning. Separates decision-making into a controller-regret layer (when to speak/skip via regret matching) and a generation-credit layer (optimizing utterances with role-specific GSPO rewards). Avoids free-riding and sparse rewards. Extends game theory to deep learning with mathematically rigorous convergence.

### 4. AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation

**Authors:** Shanghua Gao, Ada Fang, Marinka Zitnik

**arXiv:** [2605.28655](https://arxiv.org/abs/2605.28655) | Submitted May 27, 2026

Decentralized agent teams for autonomous scientific discovery. Agents share experimental state, self-organize around promising hypotheses, critique proposals, and share failures. On BioML-Bench achieves 74.4% mean leaderboard percentile (+8.33% over prior best). On GPT training optimization, discovers improvements 1.9x faster than AutoResearch. On ProteinGym, discovers ACE2-Spike binding method improving SOTA by +12.5% Spearman.

### 5. Calibrating Conservatism for Scalable Oversight

**Authors:** William Overman, Mohsen Bayati

**arXiv:** [2605.28807](https://arxiv.org/abs/2605.28807) | Submitted May 27, 2026

Introduces Calibrated Collective Oversight (CCO) for controlling misaligned agentic AI. Aggregates diverse auxiliary scoring functions into a conservatism penalty, calibrated online via Conformal Decision Theory with finite-time bounds and no distributional assumptions. On SWE-bench, weaker overseers constrain adversarial agents; on MACHIAVELLI, CCO reduces ethical violations while preserving reward.

### 6. Measuring Progress Toward AGI: A Cognitive Framework

**Authors:** Ryan Burnell, Yumeya Yamamori, Orhan Firat, Kate Olszewska, Steph Hughes-Fitt, Oran Kelly, Isaac R. Galatzer-Levy, Meredith Ringel Morris, Allan Dafoe, Alison M. Snyder, Noah D. Goodman, Matthew Botvinick, Shane Legg (DeepMind)

**arXiv:** [2605.28405](https://arxiv.org/abs/2605.28405) | Submitted May 27, 2026

DeepMind proposes a Cognitive Taxonomy deconstructing general intelligence into 10 key faculties from psychology/neuroscience. Evaluation protocol generates a "cognitive profile" across targeted held-out tasks. Aims to bring rigorous empirical measurement to the otherwise subjective AGI debate.

---

## 📊 CTR / Recommendation

### 7. Looking Farther with Confidence: Uncertainty-Guided Future Learning for Sequential Recommendation

**Authors:** Ziqiang Cui, Xing Tang, Peiyang Liu, Xiaokun Zhang, Shiwei Li, Xiuqiang He, Chen Ma

**arXiv:** [2605.28493](https://arxiv.org/abs/2605.28493) | Submitted May 27, 2026

Adaptive future learning framework (UFRec) for sequential recommendation. Uncertainty-Guided Future Supervision dynamically weights multi-step future supervision based on model confidence. Future-Aware Contrastive Learning treats the future trajectory as a holistic entity. Training-only auxiliary modules — zero inference overhead. Outperforms SOTA on 4 benchmarks.

### 8. Fine-Tuned LLM as a Complementary Predictor Improving Ads System

**Authors:** Hui Yang, Daiwei He, Kevin Jiang, Taejin Park, Kungang Li, Jiajun Luo, Yuying Chen, Xinyi Zhang, Sihan Wang, Haoyu He, Yu Liu, Lakshmi Manoharan, David Xue, Shubham Barhate, Runze Su, Duna Zhan, Ling Leng, Siping Ji, Jinfeng Zhuang, Alice Wu, Leo Lu, Han Sun, Zhifang Liu

**arXiv:** [2605.27856](https://arxiv.org/abs/2605.27856) | Submitted May 27, 2026

Novel paradigm: fine-tuned open-source LLM as an ads-specific ancillary predictor (not a ranker). Forecasts likely advertisers from user profiles, augmenting conventional candidate generation and providing informative priors to downstream ranking. Deployed in a large-scale production ads system with measurable online business impact.

### 9. Joint Optimization of Relevance and Engagement in Multi-Task Ranking for E-Commerce with Efficient LLM Supervision

**Authors:** Luming Chen, Jiaqi Xi, Raghav Saboo, Kenny Chi, Martin Wang, Sudeep Das, Danny Nightingale, Aditya Dodda, Elyse Winer, Akshad Viswanathan

**arXiv:** [2605.27704](https://arxiv.org/abs/2605.27704) | Submitted May 26, 2026

Production-scale multi-task ranking system integrating semantic relevance as a primary optimization objective. Ordinal relevance head predicting over relevance thresholds. Fine-tuned lightweight LLMs generate 3-level ordinal relevance labels for 100M+ query-item pairs. Significant improvements in semantic alignment while preserving engagement objectives.

### 10. Context Features Are Cheap: Rank-Aware Decomposition for Efficient Feature Interaction in Recommender Systems

**Authors:** Yevgeny Tkach

**arXiv:** [2605.27450](https://arxiv.org/abs/2605.27450) | Submitted May 24, 2026

Rank-aware decomposition applicable to FM pairwise products, DCNv2 cross layers, self-attention, and FC projections. Moves context-only computation from once-per-candidate to once-per-request — identity-equivalent to original model. Applied to production DLRM without architectural change: 87.5% per-pod throughput increase (47% peak pod reduction). Also introduces rDCN architectural variant matching DCNv2 accuracy at 67% fewer FLOPs.

### 11. L2Rec: Towards Dual-View Understanding of LLMs for Personalized Recommendation

**Authors:** Pingjun Pan, Tingting Zhou, Peiyao Lu, Tingting Fei, Hongxiang Chen, Chuanjiang Luo

**arXiv:** [2605.26717](https://arxiv.org/abs/2605.26717) | Submitted May 26, 2026 | **SIGIR 2026**

Unifies behavioral and semantic understanding at the parameter level of LLMs for recommendation. Dual-view Personalized Mixture-of-Experts (DPMoE) applies view-specific low-rank perturbations to a shared LLM backbone. Adaptive cross-view fusion integrates outputs. Outperforms SOTA on 4 datasets with online A/B testing validated on a large-scale industrial platform.

---

## Key Themes

1. **Agent autonomy and safety**: AutoScientists, CCO, and LACUNA all tackle the challenge of making agents more autonomous while keeping them safe and aligned — a central tension in the field.
2. **Reasoning efficiency**: CORE and TaC both find ways to get more reasoning capability with fewer resources — CORE through contrastive insight extraction, TaC by repurposing thinking as compression.
3. **Cooperative multi-agent reasoning**: TRACER brings game-theoretic rigor to multi-LLM collaboration with regret matching and credit assignment.
4. **AGI measurement**: DeepMind's cognitive framework for AGI progress attempts to bring empirical rigor to the conversation.
5. **CTR + LLM convergence accelerates**: 3 of the 5 CTR/RecSys papers use LLMs (as predictors, supervisors, or unified backbones). The line between LLM research and recommendation research is blurring rapidly.
6. **Inference efficiency in RecSys**: The rank-aware decomposition paper shows there's still low-hanging fruit in production inference optimization — 87.5% throughput gain with zero accuracy loss.
