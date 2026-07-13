# arXiv Daily Report — 2026-07-12

---

## AI / Large Language Models

### 1. LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL
- **Authors**: Yujin Kim, Namgyu Ho, Sangmin Hwang, Joonkee Kim, Yongjin Yang, Sangmin Bae, Seungone Kim, Jaehun Jung, Se-Young Yun, Hwanjun Song
- **Institution**: KAIST
- **Abstract**: Reinforcement learning for non-verifiable instruction following increasingly relies on LLM judges with prompt-specific rubrics as reward signals. This paper introduces LLM-as-a-Tutor, a framework that extends the LLM's role from judge to tutor: a single model serves as an examiner that pairwise compares policy rollouts to detect non-challenging prompts, and as a generator that appends atomic constraints to them. This append-only design monotonically raises difficulty in step with the policy's capability, producing a self-calibrating training signal without external difficulty schedules.
- **Key Innovations**:
  - Identifies policy-prompt mismatch as a precondition that limits rubric-equipped reward judges in non-verifiable RL.
  - Proposes prompt adaptation as a missing axis of policy-awareness, complementary to rubric adaptation.
  - Self-calibrating curriculum via pairwise comparison to detect non-challenging prompts.
- **Link**: https://arxiv.org/abs/2607.04412

### 2. LLM-as-a-Verifier: A General-Purpose Verification Framework
- **Authors**: Not specified in search
- **Institution**: Not specified
- **Abstract**: A general-purpose verification framework leveraging LLMs for structured verification tasks across domains.
- **Key Innovations**:
  - General-purpose LLM verification framework.
  - Applicable across diverse verification domains.
- **Link**: https://arxiv.org/abs/2607.05391

### 3. Set Diffusion: Interpolating Token Orderings Between Autoregression and Diffusion for Fast and Flexible Decoding
- **Authors**: Not specified in search
- **Institution**: Not specified
- **Abstract**: Proposes a method interpolating between autoregressive and diffusion-based token generation, offering fast and flexible decoding for language models.
- **Key Innovations**:
  - Bridges autoregressive and diffusion decoding paradigms.
  - Enables flexible token ordering interpolation.
- **Link**: https://arxiv.org/abs/2607.01775

### 4. Legible-by-Construction: Attention and End-to-End Transformers
- **Authors**: Not specified in search
- **Institution**: Not specified
- **Abstract**: Explores building legibility into transformer architectures by construction through attention mechanisms.
- **Key Innovations**:
  - Architectural approach to ensuring interpretability.
  - End-to-end transformer design for legibility.
- **Link**: https://arxiv.org/abs/2607.04319

---

## Recommendation Systems

### 5. UniRec: Bridging the Expressive Gap between Generative and Discriminative Recommendation via Chain-of-Attribute
- **Authors**: Not specified (Shopee team)
- **Institution**: Shopee
- **Abstract**: Formalizes the expressive gap between generative and discriminative recommendation via Bayes' theorem, proving the gap arises from feature coverage rather than fundamental modeling asymmetry. Proposes Chain-of-Attribute (CoA) which prefixes SID sequences with structured attribute tokens (category, seller, brand) before decoding. Deployed on Shopee's e-commerce platform with significant online gains.
- **Key Innovations**:
  - First information-theoretic analysis showing the expressive gap between generative and discriminative recommendation arises from feature coverage.
  - Chain-of-Attribute mechanism: speculate-then-refine generation paradigm with provable per-step entropy reduction.
  - Capacity-constrained SID and Conditional Decoding Context for production deployment.
  - Online A/B test results: +5.37% PVCTR, +4.76% orders, +5.60% GMV on Shopee.
- **Link**: https://arxiv.org/abs/2604.12234

### 6. GEMs: Breaking the Long-Sequence Barrier in Generative Recommendation with a Multi-Stream Decoder
- **Authors**: Not specified
- **Institution**: Not specified (industrial deployment)
- **Abstract**: Proposes GEMs, a multi-stream decoder framework that partitions user behaviors into Recent, Mid-term, and Lifecycle streams with tailored inference schemes for each. The first lifelong GR framework successfully deployed in a high-concurrency industrial environment, processing user sequences of over 100,000 interactions.
- **Key Innovations**:
  - Multi-stream architecture (Recent/Mid-term/Lifecycle) with dedicated encoders.
  - Parameter-free fusion strategy for multi-stream integration.
  - Handles ultra-long sequences (100K+ interactions) with low inference cost.
  - Achieves +21.14% Recall@100 improvement over best baseline.
- **Link**: https://arxiv.org/abs/2602.13631

### 7. Gryphon: A Unified Architecture for Semantic-ID Generation and Item-Level Scoring in Industrial Recommendations
- **Authors**: Daria Tikhonovich, Oleg Sorokin, Vladislav Dodonov, Mariia Ulianova, Ilya Murzin
- **Institution**: Yandex Music
- **Abstract**: Introduces Gryphon, an encoder-decoder generative recommendation architecture that adds jointly trained item-level scoring alongside SID generation. Instead of ranking SIDs by accumulated token likelihood, Gryphon resolves each generated SID to concrete items and re-scores them directly. Deployed as the sole candidate source in a 7-day A/B test.
- **Key Innovations**:
  - Item-level scoring reuses encoder's user representation in a single forward pass.
  - Resolves SID collision and miscalibrated sequence score issues.
  - Replaced 15+ candidate generators and separate preranking stage in production.
  - +3.7% over vanilla GR, +2.5% over collision-resolved GR.
- **Link**: https://arxiv.org/abs/2606.08604

### 8. R3-REC: Reasoning-Driven Recommendation via Retrieval-Augmented LLMs over Multi-Granular Interest Signals
- **Authors**: Not specified
- **Institution**: Not specified
- **Abstract**: A prompt-centric, retrieval-augmented framework unifying Multi-level User Intent Reasoning, Item Semantic Extraction, Long-Short Interest Polarity Mining, Similar User Collaborative Enhancement, and Reasoning-based Interest Matching and Scoring. Achieves up to +10.2% HR@1 and +6.4% HR@5 improvements.
- **Key Innovations**:
  - Unifies five complementary modules in a training-light, modular pipeline.
  - Multi-granular user interest reasoning with long/short horizon polarity mining.
  - RAG-style similar-user retrieval to mitigate cold-start sparsity.
  - Statistically significant gains across ML-1M, Games, and Bundle datasets.
- **Link**: https://arxiv.org/abs/2603.13730

### 9. CMSL: Constructive Multi-Sequence Learning for Recommendation Systems
- **Authors**: Not specified (Meta team)
- **Institution**: Meta
- **Abstract**: Proposes Constructive Multi-Sequence Learning (CMSL), a paradigm shift from passive sequence ingestion to active "context engineering" that constructs multiple coherent sequences in latent space. Addresses the "Context Pollution" problem where unrelated behaviors compete for the same attention budget. Deployed across ranking and retrieval tasks on four major surfaces at Meta.
- **Key Innovations**:
  - Identifies and addresses "Context Pollution" problem in sequential recommendation.
  - Learnable Sequence Construction Module for intent-aware latent sequence construction.
  - Scalable linear attention mechanism for multi-sequence modeling.
  - Production deployment across multiple Meta surfaces.
- **Link**: https://arxiv.org/abs/2606.28533

### 10. AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems
- **Authors**: AgentX Team (60+ authors from Kuaishou)
- **Institution**: Kuaishou
- **Abstract**: A production-deployed multi-agent system that autonomously generates, implements, evaluates, and learns from recommendation experiments. Features four tightly coupled stages: Brainstorm Agent, Developing Agent, Evaluation Agent, and Harness Evolution layer (SGPO). Deployed in Kuaishou App for three weeks.
- **Key Innovations**:
  - Complete closed-loop system from idea generation to production deployment.
  - Self-iterative flywheel: trajectories from experiments feed back to improve agents.
  - 374 ideas → 10 launchable rollouts in 3 weeks.
  - 3.7× business value over manual engineer, 0.561% user app-time gain.
  - Over RMB 100M annualized revenue impact.
- **Link**: https://arxiv.org/abs/2606.26859

### 11. GenAIR: Generative Archetype-Grounded Item Representations for Sequential Recommendation
- **Authors**: Yifan Li, Jiahong Liu, Xinni Zhang, Hao Chen, Yankai Chen, Wenhao Yu, et al.
- **Institution**: Not specified
- **Abstract**: Leverages LLMs to analyze item metadata and infer textual descriptions of the Archetype (conceptual profile of the item's ideal target audience), then introduces behavioral calibration to ground generative archetypes in real-world behavior.
- **Key Innovations**:
  - Archetype concept: LLM-inferred target audience profile for item representation.
  - Behavioral calibration objective to align semantic space with empirical patterns.
  - Seamless integration with most existing sequential recommendation models.
- **Link**: https://arxiv.org/abs/2606.11023

### 12. SIDReasoner: Reasoning over Semantic IDs Enhances Generative Recommendation
- **Authors**: Yingzhi He, Yan Sun, Junfei Tan, Yuxin Chen, Xiaoyu Kong, Chunxu Shen, et al.
- **Institution**: Not specified
- **Abstract**: Proposes a two-stage framework that elicits reasoning over SIDs by strengthening SID-language alignment to unlock transferable LLM reasoning. Uses multi-task training with enriched SID-centered corpus and GRPO for outcome-based feedback.
- **Key Innovations**:
  - SID-language alignment via teacher-assisted semantic expansion.
  - GRPO-based reinforcement to self-explore reasoning patterns.
  - Strong cross-domain generalization capability.
  - Data-efficient: achieves effective reasoning at academic-scale datasets.
- **Link**: https://arxiv.org/abs/2603.23183

### 13. Beyond Interleaving: Causal Attention Reformulations for Generative Recommender Systems
- **Authors**: Not specified (Meta team)
- **Institution**: Meta
- **Abstract**: Proposes principled reformulation of generative recommendation by aligning sequence modeling with causal structure. Introduces AttnLFA and AttnMVP architectures that eliminate interleaved dependencies, reducing sequence complexity by 50%.
- **Key Innovations**:
  - Explicitly encodes i_n → a_n causal dependency without interleaving.
  - AttnLFA: attention-based late fusion for actions.
  - AttnMVP: mixed-value early fusion for progressive action integration.
  - 50% reduction in sequence complexity with consistent accuracy improvements.
- **Link**: https://arxiv.org/abs/2603.10369

### 14. FAVE: Flow-based Average Velocity Establishment for Sequential Recommendation
- **Authors**: Ke Shi, et al.
- **Institution**: Not specified
- **Abstract**: A one-step flow matching generative recommendation framework that constructs a direct trajectory from an informative prior to the target user preference distribution. Achieves state-of-the-art performance with order-of-magnitude inference efficiency improvement.
- **Key Innovations**:
  - Semantic anchor prior replaces uninformative Gaussian noise.
  - Global average velocity with JVP-based straightness constraint.
  - One-step generation for practical deployment efficiency.
  - +9.90% NDCG@20 on ML-100k over best baseline.
- **Link**: https://arxiv.org/abs/2604.04427

### 15. PRISM: Purified Representation and Integrated Semantic Modeling for Generative Sequential Recommendation
- **Authors**: Fang Dong, Jingtong Gao, Yu Li, Xiangyu Zhao, Yi Chang
- **Institution**: Not specified
- **Abstract**: Addresses noise and semantic drift in generative sequential recommendation through purified representation learning and integrated semantic modeling.
- **Key Innovations**:
  - Purified representation learning for noise reduction.
  - Integrated semantic modeling for better item understanding.
- **Link**: https://arxiv.org/abs/2601.16556

### 16. Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents
- **Authors**: Haochen Wang, Yi Wu, Daryl Chang, Li Wei, Lukasz Heldt
- **Institution**: Not specified
- **Abstract**: Proposes an end-to-end autonomous model optimization framework using LLM agents for self-evolving recommendation systems.
- **Key Innovations**:
  - LLM-driven autonomous model optimization.
  - End-to-end self-evolution pipeline.
- **Link**: https://arxiv.org/abs/2602.10226

---

## Advertising / CTR Prediction

### 17. EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling
- **Authors**: Mingyang Liu, Yong Bai, Zhangming Chan, Sishuo Chen, Xiang-Rong Sheng, Han Zhu, et al.
- **Institution**: Alibaba (Taobao)
- **Abstract**: Proposes the Efficiently Scalable Transformer (EST) that achieves fully unified modeling by processing all raw inputs in a single sequence without lossy aggregation. Integrates Lightweight Cross Attention (LCA) and Content Sparse Attention (CSA) modules. Deployed on Taobao's display advertising platform.
- **Key Innovations**:
  - Fully unified modeling without lossy aggregation.
  - Information density analysis guiding interaction priority.
  - Content signals as relational priors rather than token embeddings.
  - Stable power-law scaling relationship.
  - Online: +3.27% RPM, +1.22% CTR in Guess scenario.
- **Link**: https://arxiv.org/abs/2602.10811

### 18. GR4AD: Generative Recommendation for Large-Scale Advertising
- **Authors**: Not specified (Kuaishou team)
- **Institution**: Kuaishou
- **Abstract**: A production-oriented generative recommender for real-time, large-scale advertising. Introduces UA-SID (Unified Advertisement Semantic ID), LazyAR decoder, VSL (Value-Aware Supervised Learning), and RSPO (Ranking-Guided Softmax Preference Optimization). Fully deployed serving 400M+ users.
- **Key Innovations**:
  - UA-SID: MLLM-based advertisement semantic ID capturing multimodal content.
  - LazyAR: lazy autoregressive decoder reducing inference cost.
  - RSPO: ranking-guided list-wise RL for business value alignment.
  - Dynamic Beam Serving with traffic-aware adaptive beam search.
  - +4.2% ad revenue improvement, fully deployed at scale.
- **Link**: https://arxiv.org/abs/2602.22732

### 19. OneRanker: Unified Generation and Ranking with One Model in Industrial Advertising Recommendation
- **Authors**: Not specified (Tencent team)
- **Institution**: Tencent (Weixin Channels)
- **Abstract**: Achieves architectural-level deep integration of generation and ranking through value-aware multi-task decoupling architecture, coarse-to-fine collaborative target awareness, and input-output dual-side consistency guarantees. Fully deployed on Tencent's Weixin Channels advertising system.
- **Key Innovations**:
  - Value-aware multi-task decoupling architecture with task token sequences.
  - Fake Item Tokens for implicit target awareness during generation.
  - Key/Value pass-through and Distribution Consistency Constraint Loss.
  - GMV-Normal +1.34% on Weixin Channels advertising.
- **Link**: https://arxiv.org/abs/2603.02999

### 20. GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm
- **Authors**: Not specified (Baidu team)
- **Institution**: Baidu
- **Abstract**: Proposes Generative Ranking for Ads at Baidu (GRAB), an end-to-end generative framework for CTR prediction integrating Causal Action-aware Multi-channel Attention (CamA). Fully deployed online.
- **Key Innovations**:
  - Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics.
  - End-to-end generative CTR prediction framework.
  - Monotonic scaling with longer interaction sequences.
  - +3.05% revenue, +3.49% CTR in production.
- **Link**: https://arxiv.org/abs/2602.01865

### 21. LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks
- **Authors**: Luyi Ma, Wanjia Sherry Zhang, Zezhong Fan, Shubham Thakur, Kai Zhao, K. C. Yao, et al.
- **Institution**: Not specified (top US e-commerce platform)
- **Abstract**: Treats LLMs as hypernetworks to directly generate CTR estimator parameters in a training-free manner. Uses few-shot Chain-of-Thought prompting over multimodal ad content. Successfully deployed in production.
- **Key Innovations**:
  - LLM as hypernetwork for parameter generation (training-free).
  - Multimodal Chain-of-Thought prompting over text and images.
  - Normalization and calibration for production-ready CTR distributions.
  - +55.9% NDCG@10 over cold-start baselines.
- **Link**: https://arxiv.org/abs/2604.12096

### 22. IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs
- **Authors**: Yubin Zhang, Haiming Xu, et al.
- **Institution**: Xiaohongshu
- **Abstract**: Leverages multimodal LLMs to generate proxy embeddings from rich content signals for cold-start CTR prediction. Proxies are explicitly aligned with existing ID embedding space and optimized end-to-end. Deployed in Content Feed and Display Ads.
- **Key Innovations**:
  - MLLM-generated proxy embeddings for cold-start items.
  - Explicit alignment with existing ID embedding space.
  - End-to-end optimization under CTR objectives.
  - Deployed serving hundreds of millions of users daily.
- **Link**: https://arxiv.org/abs/2603.01590

### 23. GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction
- **Authors**: Not specified
- **Institution**: Not specified
- **Abstract**: Proposes a generative user intent framework leveraging semantic interest cohorts to model dynamic user preferences for CTR prediction. Uses generative sequential model for next-item prediction to produce candidate interest cohorts.
- **Key Innovations**:
  - Generative interest cohort prediction as intent representation.
  - Hierarchical candidate-aware network for context injection.
  - End-to-end training with self-supervised regularization.
- **Link**: https://arxiv.org/abs/2601.18251

### 24. SparseCTR: Unleashing the Potential of Sparse Attention on Long-term Behaviors for CTR Prediction
- **Authors**: Weijiang Lai, Beihong Jin, Di Zhang, Siru Chen, Jiongyan Zhang, Yuhang Gou, et al.
- **Institution**: Not specified
- **Abstract**: Proposes SparseCTR for efficient long-term behavior modeling in CTR prediction. Features personalized behavior sequence segmentation, three-branch sparse self-attention, and composite relative temporal encoding. Exhibits scaling law across three orders of magnitude in FLOPs.
- **Key Innovations**:
  - Personalized behavior sequence segmentation.
  - Three-branch sparse self-attention for global/transition/short-term interests.
  - Learnable head-specific temporal bias coefficients.
  - Scaling law across three orders of magnitude in FLOPs.
  - +1.72% CTR, +1.41% CPM in online A/B testing.
- **Link**: https://arxiv.org/abs/2601.17836

### 25. CaliCausalRank: Calibrated Multi-Objective Ad Ranking with Robust Counterfactual Utility Optimization
- **Authors**: Xikai Yang, Sebastian Sun, Yilin Li, Yue Xing, Ming Wang, Yang Wang
- **Institution**: Not specified
- **Abstract**: A unified framework integrating training-time scale calibration, constraint-based multi-objective optimization, and robust counterfactual utility estimation for ad ranking.
- **Key Innovations**:
  - Score calibration as first-class training objective.
  - Lagrangian relaxation for multi-objective constraint satisfaction.
  - Variance-reduced counterfactual estimators.
  - +1.1% AUC, 31.6% calibration error reduction.
- **Link**: https://arxiv.org/abs/2602.18786

---

## Games / Multi-Agent RL

### 26. CausalGame: Benchmarking Causal Thinking of LLM Agents in Games
- **Authors**: Zhenhao Chen, et al.
- **Institution**: MBZUAI, HKBU, CMU
- **Abstract**: A benchmark evaluating causal thinking capabilities of LLM agents through interactive games with 14 scenarios incorporating selection bias, measurement error, and hidden confounders. Evaluates 30 frontier LLMs.
- **Key Innovations**:
  - Interactive game-based benchmark for causal reasoning.
  - 14 scenarios with realistic observational challenges.
  - Evaluation of 30 frontier LLMs (GPT-5.5, Claude-Opus-4.5, Gemini-3.5, etc.).
  - Best model reaches only 68% survival vs. 78-85% analytical optima.
  - ICML 2026 Oral presentation.
- **Link**: https://arxiv.org/abs/2607.04293

### 27. ACPO: Agent-Chained Policy Optimization for Multi-Agent Reinforcement Learning
- **Authors**: Not specified
- **Institution**: Not specified
- **Abstract**: Shows the joint policy gradient admits an exact decentralized decomposition of per-agent terms. Develops Agent-Chained Policy Optimization (ACPO) where actors are trained independently, with updates together constituting a single step on the joint policy gradient.
- **Key Innovations**:
  - Exact decomposition of cooperative MMDP policy gradient.
  - Agent-Chained Belief MDP for serialization with belief augmentation.
  - Converges to optimal joint policy (not just Nash Equilibria).
  - Outperforms baselines with gap widening as agent count grows.
- **Link**: https://arxiv.org/abs/2606.30072

### 28. UnityMAS-O: A General RL Optimization Framework for LLM-Based Multi-Agent Systems
- **Authors**: Not specified
- **Institution**: Not specified
- **Abstract**: A general RL optimization framework for LLM-based multi-agent systems that treats complete multi-agent workflows as the unit of optimization. Represents workflows through four first-class objects: logical agent roles, graph-structured trajectories, reward functions, and agent–model mappings.
- **Key Innovations**:
  - Workflow-as-optimization-unit abstraction.
  - Decouples logical agents from physical model parameters.
  - Role-specific reward assignment at role, turn, and trajectory levels.
  - Task-agnostic framework extensible to diverse multi-agent workflows.
- **Link**: https://arxiv.org/abs/2605.26646

### 29. NePPO: Near-Potential Policy Optimization for General-Sum Multi-Agent Reinforcement Learning
- **Authors**: Not specified
- **Institution**: Not specified
- **Abstract**: Proposes learning a player-independent potential function such that the Nash equilibrium of a cooperative game with this potential approximates a Nash equilibrium of the original general-sum game. Uses zeroth-order gradient descent.
- **Key Innovations**:
  - Potential function learning for general-sum games.
  - Modular framework leveraging existing MARL solvers (HAPPO, PPO).
  - Outperforms MAPPO, IPPO, and MADDPG baselines.
- **Link**: https://arxiv.org/abs/2603.06977

### 30. Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems
- **Authors**: Lang Feng, Longtao Zheng, Shuo He, Fuxiang Zhang, Bo An
- **Institution**: Not specified
- **Abstract**: Theoretically identifies key reasons for training instability when extending group-based RL to multi-agent LLM systems and proposes stabilization techniques.
- **Key Innovations**:
  - Theoretical analysis of GRPO-style training instability in multi-agent settings.
  - Agent-wise advantage normalization for gradient stabilization.
- **Link**: https://arxiv.org/abs/2602.08847

### 31. MEMO: Memory-Augmented Model Context Optimization for Robust Multi-Turn Multi-Agent LLM Games
- **Authors**: Not specified
- **Institution**: Not specified
- **Abstract**: A self-play framework that optimizes inference-time context without updating model weights. Uses persistent memory bank with structured insights, tournament-style prompt evolution, and prioritized replay.
- **Key Innovations**:
  - Weight-free self-play optimization via persistent memory.
  - CRUD operations on structured insights from self-play trajectories.
  - Raises win rate from 25.1% to 49.5% for GPT-4o-mini.
  - 19× fewer games than RL baselines with 7× reduced variance.
- **Link**: https://arxiv.org/abs/2603.09022

### 32. Cognitive Training for Language Models: Towards General Capabilities via Cross-Entropy Games
- **Authors**: Not specified
- **Institution**: Not specified
- **Abstract**: Proposes a framework for building general capabilities through a curriculum of Cross-Entropy (Xent) Games. Derives a unique meta-objective formula balancing sparsity, quality, diversity, and external relevance.
- **Key Innovations**:
  - Cross-Entropy Games as universal task space for skill discovery.
  - Principled derivation of meta-objective for greedy curriculum learning.
  - Transfer value structure for measuring skill transfer between games.
- **Link**: https://arxiv.org/abs/2603.22479

### 33. AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual Learning Agents
- **Authors**: Not specified
- **Institution**: Not specified
- **Abstract**: A novel evaluation framework that procedurally generates open-ended text games for studying five key abilities of test-time continual learning agents. Includes multifaceted diagnostics beyond task rewards.
- **Key Innovations**:
  - First game generation engine for test-time continual learning evaluation.
  - LLM-based entity and rule synthesis grounded in ontology.
  - Multifaceted metrics: world knowledge, episodic memory, exploration, diversity.
  - Reveals critical limits even in frontier models (GPT-5).
- **Link**: https://arxiv.org/abs/2606.24893

---

## Multi-Agent Systems (LLM-based)

### 34. From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning
- **Authors**: Chao Chen, et al.
- **Institution**: Not specified
- **Abstract**: Proposes the LLM-as-Environment-Engineer framework where the current policy model analyzes failure trajectories and proposes modifications to the next-stage training environment configuration. Introduces MAPF-FrozenLake as a controllable testbed.
- **Key Innovations**:
  - Automated environment redesign via LLM analysis of failure trajectories.
  - MAPF-FrozenLake: controllable multi-dimensional environment testbed.
  - RL checkpoint serves as better environment engineer than base model.
  - Outperforms larger proprietary LLMs (GPT, Gemini).
- **Link**: https://arxiv.org/abs/2606.17682

### 35. Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces
- **Authors**: Chenchen Zhang
- **Institution**: Not specified
- **Abstract**: Explores reinforcement learning for LLM-based multi-agent systems using orchestration traces for training signal.
- **Key Innovations**:
  - Orchestration traces as training signal for MAS.
- **Link**: https://arxiv.org/abs/2605.02801

---

## Summary Statistics

| Category | Papers Listed |
|----------|--------------|
| AI / LLMs | 4 |
| Recommendation Systems | 12 |
| Advertising / CTR | 9 |
| Games / Multi-Agent RL | 8 |
| Multi-Agent Systems (LLM) | 2 |
| **Total** | **35** |

---

*Report generated: 2026-07-12*
*Sources: arXiv preprints from July 2026*
