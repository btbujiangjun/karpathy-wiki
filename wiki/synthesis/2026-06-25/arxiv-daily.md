---
title: "arXiv Daily — 2026-06-25"
type: synthesis
created: 2026-06-25
updated: 2026-06-25
sources: []
tags: [arxiv, daily, llm, recommendation, advertising, ctr, games, sequential-modeling]
---

# arXiv Daily Report — 2026-06-25

Curated recent submissions across AI, LLMs, recommendation, advertising, CTR, sequential modeling, and games. Spanning submissions from 2026-06-20 to 2026-06-24.

---

## Table of Contents

1. [LLM Training & Alignment](#llm-training--alignment)
2. [LLM Reasoning & Agents](#llm-reasoning--agents)
3. [LLM Inference & Efficiency](#llm-inference--efficiency)
4. [Recommendation & Advertising](#recommendation--advertising)
5. [E-Commerce & IR](#e-commerce--ir)
6. [Reinforcement Learning & Games](#reinforcement-learning--games)
7. [World Models & Multi-Agent](#world-models--multi-agent)
8. [Sequential Modeling & Architectures](#sequential-modeling--architectures)

---

## LLM Training & Alignment

### 1. Holistic Data Scheduler for LLM Pre-training via Multi-Objective Reinforcement Learning

**Authors:** Chenhao Dang, Jing Ma, Mingjie Liao  
**Institution:** —  
**Published:** 2026-06-23 | **Venue:** KDD 2026  
**Link:** https://arxiv.org/abs/2606.24133

**Abstract:** Introduces HDS, an online data mixing framework that formulates data scheduling as an RL problem in continuous control space using Soft Actor-Critic. A multi-objective reward function integrates data-driven quality, loss-driven inter-domain influence, and model-driven weight-norm perspectives. Reaches baseline perplexity with 44% fewer iterations and achieves 7.2% improvement on MMLU 0-shot.

**Key Innovation:** First framework to formulate online data mixing as a multi-objective RL problem with a holistic reward spanning data quality, inter-domain transfer, and model-state signals.

---

### 2. SCPO: Semantic Consistency Policy Optimization for RL of LLM Agents

**Authors:** Peng Xu, Sijia Chen, Junzhuo Li, Xuming Hu  
**Institution:** —  
**Published:** 2026-06-24 | **Venue:** Under review at EMNLP 2026  
**Link:** https://arxiv.org/abs/2606.25852

**Abstract:** Addresses semantic credit inconsistency in group-based RL for LLM agents. Proposes SCPO, a value-free reward-shaping method that recovers step-level credit from successful siblings in the same rollout group. Reaches 93.7% success on ALFWorld and 74.8% on WebShop at 1.5B parameters.

**Key Innovation:** Matches semantically similar steps across successful/failed trajectories to provide consistent gradient signals, avoiding wasted partially-correct progress.

---

### 3. Grad Detect: Gradient-Based Hallucination Detection in LLMs

**Authors:** Anand Kamat, Daniel Blake, Brent M. Werness  
**Institution:** —  
**Published:** 2026-06-23 | **Venue:** ICML 2026 Workshop  
**Link:** https://arxiv.org/abs/2606.24790

**Abstract:** Predicts hallucinations by analyzing layer-wise gradient patterns from a single forward-backward pass during inference. Finds the final five layers concentrate over 97% of discriminative gradient signal across 11 models from 4 architectural families. Outperforms confidence-based and sampling-based baselines on Q&A benchmarks.

**Key Innovation:** First gradient-based hallucination detection that requires only one additional backward pass and provides interpretable layer-level insights into failure origins.

---

### 4. OpenThoughts-Agent: Data Recipes for Agentic Models

**Authors:** Negin Raoof et al. (50 co-authors)  
**Institution:** UT Austin, NYU, etc.  
**Published:** 2026-06-23  
**Link:** https://arxiv.org/abs/2606.24855

**Abstract:** Fully open data curation pipeline for training agentic LLMs. Conducts 100+ controlled ablations. Assembles a 100K-example training set, fine-tunes Qwen3-32B to achieve 44.8% average accuracy across 7 agentic benchmarks (+3.9pp over prior SOTA). Shows strong scaling properties.

**Key Innovation:** Systematic investigation of task sources and diversity for agentic training data; publicly releases full pipeline, training sets, and models.

---

### 5. CALIBER: Calibrating Confidence Before and After Reasoning in Language Models

**Authors:** Conor Finlay, Joshua Kurien, Saurabh Dash, Marzieh Fadaee, Beyza Ermis  
**Institution:** —  
**Published:** 2026-06-23  
**Link:** https://arxiv.org/abs/2606.24281

**Abstract:** Calibrates LLM confidence both before and after chain-of-thought reasoning, providing better uncertainty estimates for model outputs.

**Key Innovation:** Two-stage calibration framework separating pre-reasoning and post-reasoning confidence.

---

### 6. Can Scale Save Us From Plasticity Loss in Large Language Models?

**Authors:** J. Fernando Hernandez-Garcia, Tomas Figliolia, Beren Millidge  
**Institution:** —  
**Published:** 2026-06-23  
**Link:** https://arxiv.org/abs/2606.24752

**Abstract:** Investigates whether scaling model size can mitigate plasticity loss (the inability to learn from new data after pretraining). Provides theoretical and empirical analysis.

**Key Innovation:** Systematic study of plasticity loss in LLMs at scale, examining the interplay between model size and continued learning capacity.

---

### 7. Scaling Laws for Task-Specific LLM Distillation

**Authors:** Lavinia Ghita, Dhruv Desai, Ioana Boier  
**Institution:** —  
**Published:** 2026-06-23  
**Link:** https://arxiv.org/abs/2606.24747

**Abstract:** Derives scaling laws for distilling LLMs to task-specific smaller models, characterizing the trade-off between teacher size, student size, and task performance.

**Key Innovation:** First systematic scaling law analysis for the distillation setting, enabling optimal resource allocation for task-specific model deployment.

---

## LLM Reasoning & Agents

### 8. Qwen-AgentWorld: Language World Models for General Agents

**Authors:** Yuxin Zuo, Zikai Xiao, Li Sheng, Fei Huang, et al.  
**Institution:** Alibaba/Qwen Team  
**Published:** 2026-06-23  
**Link:** https://arxiv.org/abs/2606.24597

**Abstract:** Language world models that enable agents to plan and reason about environments using natural language as the representation medium. Built on the Qwen architecture.

**Key Innovation:** Bridges language models and world models by using language as the state representation for agent planning.

---

### 9. Nous: A Predictive World Model for Long-Term Agent Memory

**Authors:** Pranav Singh  
**Institution:** —  
**Published:** 2026-06-20  
**Link:** https://arxiv.org/abs/2606.22030

**Abstract:** Predictive world model designed for long-term agent memory, enabling agents to maintain coherent state across extended interactions.

**Key Innovation:** World model architecture specifically designed for persistent agent memory across long horizons.

---

### 10. Reasoning as Attractor Dynamics: Latent Memory Retrieval via Gibbs-Weighted Energy Minimization

**Authors:** Kanishk Awadhiya  
**Institution:** —  
**Published:** 2026-06-24 | **Venue:** ICLR Workshop 2026  
**Link:** https://arxiv.org/abs/2606.24543

**Abstract:** Frames reasoning as energy minimization in a latent attractor space, connecting transformer reasoning to dynamical systems theory.

**Key Innovation:** Formal connection between chain-of-thought reasoning and attractor dynamics in energy-based models.

---

## LLM Inference & Efficiency

### 11. RoPE-Aware Bit Allocation for KV-Cache Quantization

**Authors:** Fengfeng Liang, Yuechen Zhang, Jiaya Jia  
**Institution:** —  
**Published:** 2026-06-23  
**Link:** https://arxiv.org/abs/2606.24033

**Abstract:** Proposes Block-GTQ, a RoPE-aware bit allocator for key-cache quantization. Recognizes that under RoPE, key contributions decompose into position-dependent sums over 2D frequency blocks, making quantization a block-wise problem. At K2V2 on Llama-3.1-8B, raises NIAH from 70.6 to 97.4 and LongBench from 36.87 to 53.31. Achieves 3.24x compression at K3V3 with fp16-comparable quality, 1.34x faster inference at 128K context.

**Key Innovation:** First quantization scheme that accounts for RoPE's block-wise frequency structure rather than treating keys as flat vectors.

---

### 12. Harmonic: Hierarchical State Space Models for Efficient Long-Context Language Modeling

**Authors:** Petr Nyoma  
**Institution:** —  
**Published:** 2026-05-30  
**Link:** https://arxiv.org/abs/2606.24650

**Abstract:** Stacks three recurrent SSM levels at progressively slower timescales; each level receives the prediction error of the level below. Outperforms Transformer and Mamba at all tested lengths (1K–32K). At 64K tokens, trains successfully on an 80GB H100 where both Mamba and Transformer OOM. At 1B scale, replaces attention in TinyLlama 1.1B to eliminate RoPE position limit.

**Key Innovation:** Hierarchical prediction-error SSM architecture that achieves O(L) compute per forward pass with superior long-context scaling.

---

### 13. Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets

**Authors:** Duc Duong, Hoang Anh Duy Le, Jianwen Xie, Anshumali Shrivastava, Zhaozhuo Xu  
**Institution:** —  
**Published:** 2026-06-22  
**Link:** https://arxiv.org/abs/2606.23961

**Abstract:** Streaming KV-cache eviction method that samples tokens for eviction using a nexus-based importance scoring mechanism, maintaining output quality under strict memory budgets.

**Key Innovation:** Principled eviction strategy for long-context LLM inference that preserves retrieval quality.

---

### 14. CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference

**Authors:** Xiaolin Lin, Jingcun Wang, Olga Kondrateva, Yiyu Shi, Bing Li, Grace Li Zhang  
**Institution:** —  
**Published:** 2026-06-23  
**Link:** https://arxiv.org/abs/2606.24467

**Abstract:** Semantic-retrieval-guided KV-cache compression that identifies and retains semantically important cache entries for long-context inference.

**Key Innovation:** Uses semantic retrieval signals rather than heuristic importance scores for KV-cache eviction decisions.

---

## Recommendation & Advertising

### 15. ScaleToT: Generalizing Structured LLM Reasoning for Billion-Scale Low-Activity User Modeling

**Authors:** Tianbao Ma, Chang Xi, Yichuan Zou, Chengen Li, Linxun Chen, Zilong Lu, Yanan Niu, Zhaojie Liu, Han Li, Kun Gai  
**Institution:** Kuaishou / —  
**Published:** 2026-06-23  
**Link:** https://arxiv.org/abs/2606.24605

**Abstract:** Learns structured Tree-of-Thought reasoning from a small LLM-processed subset and extends it to billions of low-activity users. Uses entropy-guided ToT refinement, then distills to a student model via SFT and OSIPO (Outcome-Driven Segment-Aware Implicit Reward Policy Optimization). Transfers reasoning representations to a lightweight profile encoder. Online A/B test increased LT30 by 6.738% in billion-scale advertising deployment.

**Key Innovation:** First system to generalize expensive LLM reasoning (Tree-of-Thought) to billion-scale user modeling for advertising, with a teacher-student distillation pipeline.

---

### 16. LLM-as-a-Judge for Reliable and Explainable Offline Evaluation in Top-K Recommendation

**Authors:** Yue Que, Junyi Zhou, Xiaokun Zhang, Haiming Jin, Qiao Xiang, Chen Ma  
**Institution:** —  
**Published:** 2026-06-22 | **Venue:** KDD 2026  
**Link:** https://arxiv.org/abs/2606.22961

**Abstract:** Proposes an LLM-as-a-Judge framework for offline recommendation evaluation. Replaces rigid ID matching with semantic proxy matching from user textual behaviors. The LLM Judge performs reasoning-then-scoring with explicit rationale, aggregated into global Top-K metrics.

**Key Innovation:** Semantic-level preference matching via LLM judge instead of traditional ID-based evaluation; provides explainable justification for each recommendation hit/miss.

---

### 17. The Pitfall of Scaling Up: Uncovering and Mitigating Popularity Bias Amplification in Scaling Transformer-based Recommenders

**Authors:** Weiqin Yang, Yue Pan, Chongming Gao, Sheng Zhou, Xiang Wang, Can Wang, Jiawei Chen  
**Institution:** —  
**Published:** 2026-06-20 | **Venue:** KDD 2026  
**Link:** https://arxiv.org/abs/2606.21911

**Abstract:** Identifies that scaling transformer-based sequential recommenders amplifies popularity bias. Root cause: attention aggregation and feed-forward projections jointly induce spectral collapse in predictions. Proposes SPRINT regularization constraining attention column-sums and feed-forward spectral norms. Tested from 0.05M to 0.34B parameters.

**Key Innovation:** First theoretical and empirical demonstration that scaling transformers for recommendation systematically worsens popularity bias, with a principled spectral regularization solution.

---

### 18. URecJPQ: Memory-efficient Multimodal Recommendation Models through RecJPQ in Large-Scale Scenarios

**Authors:** Giuseppe Spillo, Zixuan Yi, Aleksandr Petrov, Cataldo Musto, Craig Macdonald, Iadh Ounis  
**Institution:** University of Bari / University of Glasgow  
**Published:** 2026-06-22  
**Link:** https://arxiv.org/abs/2606.23291

**Abstract:** Joint Product Quantization for multimodal top-k recommendation. Represents users/items as concatenations of shared learned sub-embeddings, reducing trainable parameters by 98-99% while maintaining accuracy (8.5% recall drop on average, sometimes improving up to 85%).

**Key Innovation:** Extends product quantization to multimodal recommendation settings, dramatically cutting memory for large-scale deployments.

---

## E-Commerce & IR

### 19. Unified Multi-Task Relevance Modeling for E-Commerce: Comparing Task Routing Architectures Across LLMs and Cross-Encoders

**Authors:** Md Omar Faruk Rokon, Jhalak Nilesh Acharya, Shasvat Desai, Hong Yao, Kuang-chih Lee  
**Institution:** —  
**Published:** 2026-06-22 | **Venue:** SIGIR 2026 E-Commerce Workshop  
**Link:** https://arxiv.org/abs/2606.23919

**Abstract:** Compares three task routing architectures for multi-task e-commerce relevance: text prefix, multi-head classification, and multi-head with private transformer layers. MHP Ensemble achieves 89.96% accuracy on 453K test examples across 6 entity-pair tasks. Multi-task training yields up to 14% improvement on low-resource tasks.

**Key Innovation:** Systematic comparison revealing asymmetric effects of task routing on encoder-only vs. decoder-only models for e-commerce relevance.

---

### 20. INSPIRE: Intent-aware Neural Sponsored Product Retrieval for E-commerce

**Authors:** Shasvat Desai, Hong Yao, Utkarsh Porwal, Kuang-chih Lee  
**Institution:** —  
**Published:** 2026-06-22 | **Venue:** SIGIR 2026 E-Commerce Workshop  
**Link:** https://arxiv.org/abs/2606.23889

**Abstract:** Intent-aware retrieval model for sponsored products that incorporates user search intent signals into the retrieval pipeline.

**Key Innovation:** Explicit intent modeling for sponsored product retrieval, bridging search intent and advertising relevance.

---

### 21. Scaling Dense Retrieval with LLM-Annotated Training Data for E-Commerce Sponsored Search

**Authors:** Md Omar Faruk Rokon, Shasvat Desai, Jhalak Nilesh Acharya, Isha Shah, et al.  
**Institution:** —  
**Published:** 2026-06-22 | **Venue:** SIGIR 2026 E-Commerce Workshop  
**Link:** https://arxiv.org/abs/2606.23911

**Abstract:** Structured mining and progressive curriculum for training dense retrieval models using LLM-annotated training data in e-commerce sponsored search.

**Key Innovation:** Curriculum learning strategy with LLM-generated annotations for dense retrieval in sponsored search.

---

## Reinforcement Learning & Games

### 22. EMAgnet: Parameter-Space EMA Regularization for Policy Gradient Self-Play in Large Games

**Authors:** Tristan Maidment, JB Lanier, Chase McDonald, Nathan Tsang, Eugene Vinitsky, Roy Fox, Albert Wang, Wesley N. Kerr  
**Institution:** —  
**Published:** 2026-06-22 | **Venue:** ICML 2026 Workshop (NExT-Game)  
**Link:** https://arxiv.org/abs/2606.23995

**Abstract:** Replaces uniform policy regularization in self-play with EMA of last-iterate policy parameters, providing an adaptive regularization target. Achieves lower exploitability than PPO with uniform-magnet regularization across two-player zero-sum benchmarks, especially in games with strictly dominated strategies.

**Key Innovation:** Parameter-space EMA as an adaptive regularization target for policy gradient self-play, improving on uniform-distribution regularization.

---

### 23. LaGO: Latent Action Guidance for Online Reinforcement Learning

**Authors:** Kuan-Yen Liu, Ren-Jyun Huang, Ti-Rong Wu  
**Institution:** —  
**Published:** 2026-06-23 | **Venue:** ICML 2026 Workshop (LM4Plan)  
**Link:** https://arxiv.org/abs/2606.24669

**Abstract:** Uses latent actions to guide online RL exploration, improving sample efficiency by operating in a learned latent action space.

**Key Innovation:** Latent action guidance that abstracts the action space for more efficient RL exploration.

---

### 24. ASALT: Adaptive State Alignment for Lateral Transfer in Multi-agent Reinforcement Learning

**Authors:** Anurag Akula, Satheesh K. Perepu, Abhishek Sarkar, Kaushik Dey  
**Institution:** —  
**Published:** 2026-06-23 | **Venue:** RLC 2026  
**Link:** https://arxiv.org/abs/2606.24601

**Abstract:** Adaptive state alignment for transfer learning across different tasks in multi-agent RL, enabling lateral knowledge transfer between agents operating in different state spaces.

**Key Innovation:** State-alignment mechanism that enables transfer between heterogeneous multi-agent tasks.

---

### 25. Themis: An Explainable AI Framework for Reinforcement Learning with Human Feedback

**Authors:** Andreas Chouliaras, Luke Connolly, Dimitris Chatzpoulos  
**Institution:** —  
**Published:** 2026-06-23 | **Venue:** IEEE CAI 2026  
**Link:** https://arxiv.org/abs/2606.24622

**Abstract:** Explainable RLHF framework that provides interpretability for reward models and policy decisions in human-feedback-based RL.

**Key Innovation:** Bridges explainability and RLHF, enabling auditability of reward model decisions.

---

### 26. Reinforcement Learning for Computer-Use Agents with Autonomous Evaluation

**Authors:** Marta Sumyk, Oleksandr Kosovan  
**Institution:** —  
**Published:** 2026-06-23 | **Venue:** IJCAI 2026 Workshop (GLOW)  
**Link:** https://arxiv.org/abs/2606.24515

**Abstract:** RL-based training for agents that interact with computer GUIs, with autonomous evaluation metrics replacing human annotation.

**Key Innovation:** Self-supervised evaluation for computer-use agent RL training, reducing human annotation burden.

---

## World Models & Multi-Agent

### 27. World Models in Pieces: Structural Certification for General Agents

**Authors:** Yikai Lu, Yifei Wu, Xinyu Lu, Tongxin Li  
**Institution:** —  
**Published:** 2026-06-23 | **Venue:** ICML 2026  
**Link:** https://arxiv.org/abs/2606.24842

**Abstract:** Structural certification framework for world models, decomposing them into certified components that guarantee safety properties for general agents.

**Key Innovation:** First formal certification approach for world model components in general agent architectures.

---

### 28. The Latent Bridge: A Continuous Slow-Fast Channel for Real-Time Game Agents

**Authors:** Bojie Li, Noah Shi  
**Institution:** —  
**Published:** 2026-06-23  
**Link:** https://arxiv.org/abs/2606.24470

**Abstract:** Dual-timescale architecture for real-time game agents: a slow (deliberative) channel and a fast (reactive) channel bridged through a continuous latent space. Enables agents to react in real-time while maintaining strategic planning.

**Key Innovation:** Continuous latent bridge between slow and fast processing channels for real-time game AI with strategic depth.

---

### 29. SAFARI: Scaling Long Horizon Agentic Fault Attribution via Active Investigation

**Authors:** Chenyang Zhu et al.  
**Institution:** —  
**Published:** 2026-06-23 | **Venue:** ICML 2026 Workshop (AIWILD)  
**Link:** https://arxiv.org/abs/2606.24626

**Abstract:** Active investigation framework for fault attribution in long-horizon agent tasks, enabling agents to identify root causes of failures across extended trajectories.

**Key Innovation:** Active learning approach to fault attribution that scales to long-horizon agent tasks.

---

### 30. Age of LLM: A Strategic 1v1 Benchmark for Reasoning, Diplomacy and Reliability under Fog of War

**Authors:** Arnaud Ricci  
**Institution:** —  
**Published:** 2026-06-23  
**Link:** https://arxiv.org/abs/2606.24391

**Abstract:** Benchmark evaluating LLMs in a strategic 1v1 game setting with imperfect information (fog of war), testing reasoning, diplomacy, and reliability under uncertainty.

**Key Innovation:** Game-theoretic benchmark for LLMs that combines strategic reasoning, negotiation, and handling of imperfect information.

---

## Sequential Modeling & Architectures

### 31. Cyclic Denoising Reveals Ultrastable Memories in Diffusion Models

**Authors:** Rishabh Sharma, Stefano Martiniani  
**Institution:** —  
**Published:** 2026-06-22  
**Link:** https://arxiv.org/abs/2606.24000

**Abstract:** Discovers that diffusion models contain ultrastable memory patterns revealed through cyclic denoising, with implications for model interpretability and memorization.

**Key Innovation:** Cyclic denoising as a probe for discovering persistent memory structures in diffusion models.

---

### 32. Data Augmentation: A Fourier Analysis Perspective

**Authors:** Behrooz Tahmasebi, Melanie Weber, Stefanie Jegelka  
**Institution:** MIT / TU Munich  
**Published:** 2026-06-23 | **Venue:** COLT 2026  
**Link:** https://arxiv.org/abs/2606.24418

**Abstract:** Provides a Fourier analysis framework for understanding how data augmentation affects learning, with implications for sequence and image model generalization.

**Key Innovation:** Theoretical framework connecting data augmentation to spectral properties of the learning problem.

---

### 33. A Rank-One Popularity Component in Dot-Product Recommender Scores

**Authors:** Yang Cheng  
**Institution:** —  
**Published:** 2026-06-19  
**Link:** https://arxiv.org/abs/2606.21275

**Abstract:** Identifies a rank-one popularity component inherent in dot-product recommendation scores, showing that popular items receive an additive popularity bonus independent of user preference.

**Key Innovation:** Theoretical decomposition of recommendation scores revealing an inherent popularity bias term.

---

## Summary Statistics

| Category | Papers | Notable Venues |
|----------|--------|----------------|
| LLM Training & Alignment | 7 | KDD 2026, EMNLP 2026, ICML 2026 |
| LLM Reasoning & Agents | 3 | ICLR Workshop 2026 |
| LLM Inference & Efficiency | 4 | — |
| Recommendation & Advertising | 4 | KDD 2026 |
| E-Commerce & IR | 3 | SIGIR 2026 |
| Reinforcement Learning & Games | 5 | ICML 2026 Workshop, RLC 2026 |
| World Models & Multi-Agent | 4 | ICML 2026 |
| Sequential Modeling & Architectures | 3 | COLT 2026 |
| **Total** | **33** | |

---

## Emerging Themes

1. **LLM ↔ Recommender Systems convergence** — LLMs are being used for recommendation evaluation (LLM-as-a-Judge), user modeling (ScaleToT), and relevance modeling. This is the dominant trend in KDD 2026 and SIGIR 2026.

2. **KV-cache compression explosion** — Three concurrent papers on KV-cache quantization/eviction (RoPE-Aware, Nexus Sampling, CompressKV), reflecting the urgent need to serve long-context LLMs efficiently.

3. **Agentic LLM training** — OpenThoughts-Agent and SCPO represent a growing open-source push for training data and methods for agentic capabilities beyond chat.

4. **Scaling pitfalls** — Two papers (popularity bias in recommenders, plasticity loss in LLMs) reveal that naive scaling introduces qualitative degradation that requires specialized mitigation.

5. **SSMs as Transformer alternatives** — Harmonic demonstrates SSMs achieving superior long-context scaling vs. both Transformer and Mamba, keeping the post-attention architecture race active.
