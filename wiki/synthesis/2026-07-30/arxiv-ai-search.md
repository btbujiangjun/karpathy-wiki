---
title: "arXiv AI Research Scan — July 2026"
type: synthesis
created: 2026-07-30
updated: 2026-07-30
tags: [arxiv, survey, llm, recommendation, ctr, sequential-modeling, games, reinforcement-learning]
---

# arXiv AI Research Scan — July 2026

Curated recent papers across LLMs, recommendation/CTR/advertising, sequential modeling, games/RL, and AI agents.

---

## Large Language Models & Multimodal

### 1. Scaling Native Multimodal Pre-Training From Scratch
- **Authors**: Haoyuan Wu, Aoqi Wu, Hai Wang, Jiajia Wu, Jinxiang Ou, Bei Yu
- **Institution**: N/A
- **Abstract**: Investigates scaling properties of native multimodal pre-training (training from scratch on multimodal inputs). Finds that compute-optimal model sizes and token counts scale as power laws, with language and multimodal objectives exhibiting distinct scaling behaviors. Data composition significantly affects multimodal allocation law.
- **Key Innovations**: First systematic characterization of scaling laws for native multimodal pre-training; derives efficiency frontier for model size/token count/data mixture; shows positive cross-modal transfer to pure-text spatial reasoning.
- **Link**: https://arxiv.org/abs/2607.22043

### 2. Statistical Inference for Rank Allocation in Low-Rank Adaptation (StatLoRA)
- **Authors**: Yihang Gao, Vincent Y. F. Tan
- **Institution**: NUS (National University of Singapore)
- **Abstract**: Formulates LoRA rank allocation as a statistical hypothesis testing problem. Associates each LoRA component with a test statistic and uses estimated p-values to determine which components should be retained or pruned under a prescribed rank budget. Establishes asymptotic normality for optimizers including AdamW.
- **Key Innovations**: First principled statistical inference framework for LoRA rank allocation; central limit theory for stochastic optimizer trajectories; outperforms vanilla LoRA, AdaLoRA on NLU/NLG/QA tasks.
- **Link**: https://arxiv.org/abs/2607.20205

### 3. Decision-Level Hijacking: Injecting Cognitive Bias into LLMs via Bit-Flip Attacks
- **Authors**: Yu Yan, Jiahao Chen, Siqi Lu et al.
- **Institution**: N/A
- **Abstract**: Proposes CogBias, a cognitive bias injection framework that uses bit-flip attacks (BFAs) to manipulate LLM stances on target topics without triggering prohibited content or degrading functionality. Achieves significant stance shifts on Llama-3.2-3B, Mistral-7B, Qwen2.5-14B with minimal bit flips.
- **Key Innovations**: First demonstration of decision-level hijacking via BFAs; multi-objective loss for cognitive manipulation; BitScout for critical bit localization; highlights new security vulnerability in open-source model ecosystems.
- **Link**: https://arxiv.org/abs/2607.25227

### 4. Cognitive Convergence: Deep Similarities Between Large Language Models and Human Cognition
- **Authors**: Chandra Sripada, Richard Lewis
- **Institution**: University of Michigan
- **Abstract**: Argues that contemporary LLMs converge with human cognition on principles of cognitive organization across five dimensions: inferential organization, computational architecture, representational structure, prediction-driven learning, and RL-like mechanisms for goal-directed action.
- **Key Innovations**: Systematic mapping of LLM internals to established cognitive science principles; challenges the "alien intelligence" framing of LLMs.
- **Link**: https://arxiv.org/abs/2607.26179

### 5. Beyond Shapley: An Influence-Based Data Auditing Pipeline for LLM Alignment and Evaluation
- **Authors**: Yunting Song, Matthew Watson, Peter Grabowski, Jun Qin
- **Institution**: N/A
- **Abstract**: Introduces a scalable inference-only data valuation pipeline that approximates Shapley values without iterative retraining. Reduces manual audit search space by 99.1% on HelpSteer2; uncovers thousands of hidden safety and factual preference inversions in HH-RLHF. Exposes benchmark integrity vulnerabilities.
- **Key Innovations**: Zero-shot/one-shot conditional log-likelihood shifts for data valuation; localized advantage metrics for gradient-conflicting records; exposes flawed labels in widely-used alignment benchmarks.
- **Link**: https://arxiv.org/abs/2607.22766

### 6. SERPO: Self-Evolving Rubric Policy Optimization for Open-Ended Test-Time Reinforcement Learning
- **Authors**: Jianze Wang, Kunwang Zheng, Ying Liu et al.
- **Institution**: N/A
- **Abstract**: Proposes a self-evolving rubric framework for test-time RL that enables LLMs to improve their own evaluation criteria during inference, allowing open-ended generation refinement without human annotations.
- **Key Innovations**: Dynamic rubric evolution during test time; bridges gap between RLHF and self-improvement paradigms.
- **Link**: https://arxiv.org/abs/2607.26873

### 7. Metis: Memory Foundation Model
- **Authors**: Zeyu Zhang, Ziliang Guo, Yihang Sun et al.
- **Institution**: Multiple (Shanghai AI Lab, et al.)
- **Abstract**: Proposes a foundation model specialized for memory-augmented LLM inference, with 42 pages detailing architecture for long-term parametric memory management.
- **Key Innovations**: Specialized foundation model for memory tasks; structured parametric memory with retrieval mechanisms.
- **Link**: https://arxiv.org/abs/2607.26760

### 8. Constitutional Midtraining: Content Presence Drives Alignment Gains
- **Authors**: Desiree Cho, Cameron Tice, Bernie Hogan et al.
- **Institution**: University of Oxford et al.
- **Abstract**: Investigates whether alignment gains from constitutional training come from constitutional principles or simply from exposure to certain content during continued training. Finds that content presence is the primary driver.
- **Key Innovations**: Controlled experiments isolating content vs. constitution effects; challenges assumptions about source of alignment in constitutional AI.
- **Link**: https://arxiv.org/abs/2607.26654

---

## Recommendation, CTR & Advertising

### 9. TMallGS: Scaling Unified Feature and Sequence Modeling for Generative E-commerce Search
- **Authors**: Zhentao Song, Yufeng Gao, Xing Fang et al.
- **Institution**: Tmall / Alibaba
- **Abstract**: Scalable ranking architecture for Tmall search combining hierarchical distribution-calibrated tokenization, field-adaptive gated transformer backbone, decoupled FiLM late fusion, context-aware bias net, and error-aware progressive training. Improves training throughput and online UCTCVR/GMV.
- **Key Innovations**: Field-wise Saliency Reweighting + Distribution-Calibrated Projection for heterogeneous features; per-field QKV projections; deployed and A/B tested on live Tmall Search traffic.
- **Link**: https://arxiv.org/abs/2607.13398

### 10. DASH: Beyond Action Imitation — Decision-Aware User Simulator for Online Advertising
- **Authors**: Zipeng Chen, Jiaer Zheng, Xiangyang Xu et al.
- **Institution**: Tencent
- **Abstract**: Proposes DASH, a decision-aware user simulator that jointly generates thinking traces and predicts actions from heterogeneous cross-domain histories for advertising evaluation. Uses rubric-based reward model for RL training of thinking traces.
- **Key Innovations**: First user simulator that models cognitive decision process (not just action imitation); rubric-based reward evaluation for thinking trace quality; deployed on Tencent advertising data across 5 domains.
- **Link**: https://arxiv.org/abs/2607.26893

### 11. WhisperRec: Latent Reasoning for Efficient Foundation Recommendation Models
- **Authors**: Hao Jiang, Peiru Du, Pengfei Yao et al.
- **Institution**: Kuaishou
- **Abstract**: Proposes latent reasoning framework for foundation recommendation models that compresses teacher Chain-of-Thought into learnable latent reasoning tokens, avoiding verbose rationale generation. Achieves 10x higher online inference throughput vs. explicit CoT, with 17.44% SID@64 improvement.
- **Key Innovations**: Latent-Reason-then-Answer paradigm; Multi-View Adaptive CoT; three-stage latent reasoning alignment; deployed on Kuaishou industrial-scale data.
- **Link**: https://arxiv.org/abs/2607.26621

### 12. Learning from the Future: Privileged Self-Distillation for Sequential Recommendation
- **Authors**: Jiakai Tang, Yang Zhang, See-Kiong Ng et al.
- **Institution**: NUS / Zhejiang University
- **Abstract**: Uses future item information as privileged knowledge during training to distill into a deployable model that sees only past interactions. Teacher uses bidirectional sequence; student is unidirectional.
- **Key Innovations**: Privileged information distillation in sequential recommendation; bridges gap between bidirectional training and unidirectional inference.
- **Link**: https://arxiv.org/abs/2607.27055

### 13. Sharpness-aware Model Merging with Salience Recovery for LLM-based Cross-Domain Sequential Recommendation
- **Authors**: Huwei Ji, Jiajie Su, Yuyuan Li et al.
- **Institution**: N/A (published at KDD '26)
- **Abstract**: Applies sharpness-aware minimization to model merging for cross-domain sequential recommendation with LLM backbones; introduces salience recovery to prevent information loss during merging.
- **Key Innovations**: Sharpness-aware merging for recommendation domain adaptation; salience recovery mechanism for LLM-based recommenders.
- **Link**: https://arxiv.org/abs/2607.25366

### 14. Multi-Decoder OneRec: Controllable Generative Retrieval for Multi-Objective Industrial Recommendation
- **Authors**: You Wang, Zhao Liu, Guoping Tang et al.
- **Institution**: Huawei
- **Abstract**: Single generative retrieval model with multiple decoders for different objectives (CTR, engagement, diversity). Enables controllable trade-offs at inference time without retraining.
- **Key Innovations**: Multi-decoder architecture for controllable generative recommendation; deployed in industrial system.
- **Link**: https://arxiv.org/abs/2607.26500

### 15. Memory Layer: Train the In-Model Cache for Recommendation Models
- **Authors**: Liangyuan Na, Gufan Yin, Yixin Bao et al.
- **Institution**: N/A
- **Abstract**: Proposes a trainable in-model memory cache layer for recommendation models, enabling models to explicitly store and retrieve user-item interaction patterns.
- **Key Innovations**: Differentiable memory layer for recommendations; bridges in-memory caching with learned model parameters.
- **Link**: https://arxiv.org/abs/2607.25110

### 16. The Case Against Generation for Retrieval: Discriminative Language Models as Effective Retrievers
- **Authors**: Zhe Xu, Prachi Agrawal, Kavosh Asadi et al.
- **Institution**: Amazon
- **Abstract**: Argues that discriminative approaches outperform generative ones for retrieval tasks in recommendation systems. Shows that discriminative LMs are simpler, faster, and more effective than generative retrieval models.
- **Key Innovations**: Systematic comparison of generative vs. discriminative retrieval; challenges prevailing trend toward generative recommendation.
- **Link**: https://arxiv.org/abs/2607.25346

### 17. Grevo: A Unified Generative Recommendation Framework with Evolutionary Item Indexing
- **Authors**: Huanjie Wang, Liwei Guan, Zekai Sun et al.
- **Institution**: N/A
- **Abstract**: Proposes evolutionary item indexing that adapts item ID assignments over time to reflect changing item relationships, improving generative recommendation quality.
- **Key Innovations**: Dynamic/evolutionary item indexing for generative recommendation; addresses cold-start and item drift issues.
- **Link**: https://arxiv.org/abs/2607.25329

### 18. IMFuse: Instance-Aware Multi-Layer Fusion for LLM-Enhanced Sequential Recommendation
- **Authors**: Yuheng Zheng, Yu Cui, Bin Wu et al.
- **Institution**: Zhejiang University / Zhengzhou University / USTC
- **Abstract**: Instance-aware multi-layer fusion mechanism for integrating LLM knowledge into sequential recommendation models, with adaptive fusion at different semantic levels.
- **Key Innovations**: Layer-wise adaptive fusion of LLM knowledge with ID-based collaborative signals.
- **Link**: https://arxiv.org/abs/2607.27002

### 19. Ranked by Position: Order Sensitivity as an Exploitable Attack Surface in LLM Listwise Recommenders
- **Authors**: Ge Zhang, Jingru Cheng, Huiyuan Chen
- **Institution**: N/A
- **Abstract**: Demonstrates that LLM-based listwise recommenders are highly sensitive to input order, and this sensitivity can be exploited as an attack surface to manipulate recommendations.
- **Key Innovations**: Security analysis of LLM recommender systems; identifies order sensitivity vulnerability.
- **Link**: https://arxiv.org/abs/2607.24869

---

## Sequential Modeling & State Space Models

### 20. Forget Attention: Importance-Aware Attention Is All You Need (SISA)
- **Authors**: Suhyeong Shin, Yeongwook Yang
- **Institution**: N/A
- **Abstract**: Proposes SISA (SSM-Informed Softmax Attention), which adds an SSM-derived importance term inside the attention score, realized as a single SDPA call on augmented query/key vectors. Achieves NIAH 100% from step 1K (7x faster than Transformer) while maintaining stock-SDPA execution.
- **Key Innovations**: Score-level fusion of SSM importance with attention (vs. block-level/head-level hybrids); defines third design axis for SSM-attention hybrids; no custom kernel needed.
- **Link**: https://arxiv.org/abs/2606.02332

### 21. Kalman Linear Attention: Parallel Bayesian Filtering for Efficient Language Modelling
- **Authors**: Vaisakh Shaj, Cameron Barker, Aidan Scannell et al.
- **Institution**: University of Edinburgh
- **Abstract**: Casts sequence mixing as exact Bayesian filtering with Kalman filter as core primitive. Reparameterizes in information form to enable associative scan. KLA layer performs time-parallel probabilistic inference with explicit belief-state uncertainty, strictly more expressive than GLA at same cost. Accepted at ICML 2026.
- **Key Innovations**: First Kalman-filter-based attention layer; solves permutation-composition (A5) tasks that linear SSMs and attention cannot; explicit uncertainty tracking in sequence modeling.
- **Link**: https://arxiv.org/abs/2602.10743

### 22. Vision Non-Causal Trapezoidal Mamba (VNCT)
- **Authors**: Anvitha Ramachandran, Dhruv Parikh, Haoyang Fan et al.
- **Institution**: USC / Army Research Lab
- **Abstract**: First second-order non-causal vision SSM that eliminates directional scanning. All image tokens interact in a single pass. Improves Boundary IoU by up to 3.7 points over directional SSMs.
- **Key Innovations**: Elimination of directional scanning bias in vision SSMs; second-order dynamics for non-causal processing; orientation-robust representations.
- **Link**: https://arxiv.org/abs/2607.03589

### 23. MARS: Multi-rate Aggregation of Recency Signals for Sequential Recommendation
- **Authors**: Zhenyu Yu, Shuigeng Zhou
- **Institution**: N/A
- **Abstract**: Encoder-agnostic aggregation operator that consumes real timestamps and produces K summaries emphasizing distinct recency scales. Automatically selects between Transformer (sparse data) and Mamba (dense data) instantiations. Mean relative gain +19.7% HR@10 over content-only Transformer baselines.
- **Key Innovations**: Multi-rate temporal aggregation for sequential recommenders; adaptive encoder selection based on data density; Pareto-optimal accuracy/efficiency.
- **Link**: https://arxiv.org/abs/2606.03718

### 24. Scalable Sequential Recommendation under Latency and Memory Constraints (HoloMambaRec)
- **Authors**: Adithya Parthasarathy et al.
- **Institution**: N/A
- **Abstract**: Lightweight sequential recommendation combining holographic reduced representations for attribute-aware embedding with a selective state space encoder. Surpasses SASRec with substantially lower memory complexity.
- **Key Innovations**: Holographic embeddings + Mamba backbone for recommendation; linear-time constant-memory inference.
- **Link**: https://arxiv.org/abs/2601.08360

### 25. Progressive Split Mamba: Effective State Space Modelling for Image Restoration
- **Authors**: Mohammed Hassanin, Nour Moustafa, Weijian Deng, Ibrahim Radwan
- **Institution**: N/A
- **Abstract**: Topology-aware hierarchical state-space framework that performs geometry-consistent partitioning before SSM processing. Progressive split hierarchy (halves, quadrants, octants) enables multi-scale modeling. Symmetric cross-scale shortcuts counteract long-range decay.
- **Key Innovations**: Geometry-preserving partitioning for 2D SSMs; progressive multi-scale hierarchy; solves locality distortion in Mamba-based image processing.
- **Link**: https://arxiv.org/abs/2603.09171

---

## Games & Reinforcement Learning

### 26. Cortex: Compact Behavior Cloning for Quake with Frozen Visual Features
- **Authors**: Dzmitry Malyshau
- **Institution**: N/A
- **Abstract**: Compact 10.98M parameter six-layer transformer policy with frozen DINOv3 encoder, trained on 474.7 hours of Quake gameplay. Reaches the opening door, button room, and gate descent in every episode; 19/20 episodes record at least one kill.
- **Key Innovations**: Minimalist behavioral cloning without RL or explicit memory; demonstrates ceiling of simple BC in complex FPS games; open-source release.
- **Link**: https://arxiv.org/abs/2607.22739

### 27. Play Like Champions: Counterfactual Feedback Generation in Latent Space
- **Authors**: Andrzej Białecki, Adam Mastalerz, Han Zhou
- **Institution**: N/A
- **Abstract**: Trains Guided VAE on 23,305 professional StarCraft II replays to enable counterfactual traversal between losing and winning gameplay profiles. Four traversal strategies (linear, optimal transport, density-regularized, neural flow matching) generate actionable improvement trajectories.
- **Key Innovations**: Counterfactual path generation in learned latent space for RTS games; first framework for translating expert RL policy knowledge into human-actionable feedback.
- **Link**: https://arxiv.org/abs/2607.00190

### 28. A Gold-Standard Study of What Makes a Lightweight Game-Playing Agent Strong
- **Authors**: Nima Kelidari, Mohammadsaeed Haghi, Mahdi Salmani
- **Institution**: N/A
- **Abstract**: Builds fixed rule-based expert for Gin Rummy as yardstick. Isolates factors: trust region updates, well-aimed reward, curriculum, warm starting, best checkpoint. MLP/conv/attention/RNN encoders compared — finds limit is information, not network size.
- **Key Innovations**: Gold-standard expert-based evaluation methodology for imperfect-information games; reproducible lightweight agent recipe; demonstrates information ceiling in game-playing agents.
- **Link**: https://arxiv.org/abs/2607.06854

### 29. Coachable Agents for Interactive Gameplay
- **Authors**: Roberto Capobianco, Harm van Seijen et al.
- **Institution**: Microsoft Research / Sony AI
- **Abstract**: Combines UVFAs with selected training scenarios to create coaching framework for agents in AAA video games (Horizon Forbidden West, Gran Turismo). Agents exhibit real-time controllable "styles" while satisfying main task objectives.
- **Key Innovations**: Real-time style control for game agents; UVFA-based coaching framework; demonstrated on commercial AAA titles.
- **Link**: https://arxiv.org/abs/2607.00642

### 30. Physics Models for Sim-to-Real Transfer in Professional-Level Robot Table Tennis
- **Authors**: Christian Conti, Bilan Yang et al.
- **Institution**: Sony AI
- **Abstract**: Physics models for aerodynamic ball flight, ball-table, and ball-racket contact capturing behavior across vast range of speeds/spins. 59% reduction in landing-position error. First robot table tennis AI capable of competing against professional players.
- **Key Innovations**: High-fidelity physics models for extreme-speed ball dynamics; residual neural network component for racket contact; real-world deployment against professional human players.
- **Link**: https://arxiv.org/abs/2606.28805

### 31. MindGames Arena Generalization Track: Delayed Per-Step Reward Attribution
- **Authors**: Aliaksei Korshuk, Alexander Buyantuev, Ilya Makarov
- **Institution**: N/A
- **Abstract**: Introduces delayed per-step reward attribution with eligibility gating for multi-agent RL. Single 8B model trained with this method matched or surpassed GPT-5 in head-to-head play, winning both Open and Efficient tracks at NeurIPS 2025 MindGames Arena.
- **Key Innovations**: Eligibility-gated delayed reward attribution; curriculum opponent sampling; demonstrates open-source 8B model matching frontier proprietary systems in competitive gameplay.
- **Link**: https://arxiv.org/abs/2606.00017

### 32. Playing with Words, Improving with Rewards: Training LLMs for Creative Association
- **Authors**: Vijeta Deshpande et al.
- **Institution**: N/A
- **Abstract**: Trains LLMs on Codenames word-association game using RLVR. 8B model shows creativity gains on 8/10 benchmarks. Smaller models (1.7B, 4B) gain reasoning precision at creativity cost.
- **Key Innovations**: Verifiable rewards for creativity training without human judgment; scale-dependent precision-creativity trade-off characterization.
- **Link**: https://arxiv.org/abs/2605.27832

### 33. FootsiesGym: A Fighting Game Benchmark for Two-Player Zero-Sum Imperfect-Information Games
- **Authors**: Chase McDonald, Nathan Tsang, Wesley N. Kerr
- **Institution**: Como Research
- **Abstract**: Open-source environment built on HiFight's Footsies, isolating cyclic, non-transitive strategic interactions of fighting game neutral play. Vectorized simulator enables high-throughput training.
- **Key Innovations**: Standardized benchmark for imperfect-information fighting game RL; isolates neutral-game interaction dynamics.
- **Link**: https://arxiv.org/abs/2607.06514

### 34. Beyond Bayesian Nash: Learning Minimax-Regret Equilibria for Adversarial Team Games
- **Authors**: Naman Aggarwal, Jonathan P. How
- **Institution**: MIT
- **Abstract**: Introduces PR-MRE, combining distribution-free minimax-regret reasoning with probabilistic information. PRMRE-PSRO enables population-based learning via deep RL best responses. Substantially improved worst-case performance across hidden types.
- **Key Innovations**: New equilibrium concept for adversarial team games; robust double-oracle framework; bridge between robust optimization and game theory.
- **Link**: https://arxiv.org/abs/2607.09993

### 35. Verifiable Rewards for Calibrated Probabilistic Forecasting (NFL Win Probability)
- **Authors**: Sadanand Singh, Allam Reddy, Manan Chopra
- **Institution**: N/A
- **Abstract**: Uses RL with verifiable rewards to train a 7B model for NFL in-game win probability that matches betting market calibration. Introduces verifiable label-free reward from state-conditioned empirical win rate. Trained without human labels or SFT.
- **Key Innovations**: Label-free verifiable reward for probabilistic forecasting; gradient masking preserves reasoning; matches market calibration with 7B model.
- **Link**: https://arxiv.org/abs/2607.00164

---

## AI Agents & Multi-Agent Systems

### 36. SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution
- **Authors**: Zhiyuan Yao, Yuxin Chen et al.
- **Institution**: N/A
- **Abstract**: RL framework where agents evolve skills across tasks through compositional skill transfer. Agents learn to decompose novel tasks into known sub-skills and acquire new skills when needed.
- **Key Innovations**: Cross-task skill evolution without task-specific reward engineering; compositional skill transfer for agentic RL.
- **Link**: https://arxiv.org/abs/2607.26784

### 37. Digital Pantheon: Simulating and Auditing Coalition Formation with LLM Agents
- **Authors**: Dylan Van Mulders, Matthias Bogaert, Dirk Van den Poel
- **Institution**: Ghent University
- **Abstract**: Multi-agent framework combining SFT, DPO, and RAG for political coalition simulation. Introduces MILT (Multi-Layered Information Lineage Topology) for tracing agreement clauses to manifesto origins, and Coalition Influence Score (CIS).
- **Key Innovations**: DPO-based partisan personas; traceable provenance for LLM negotiation outputs; validated against real-world 2019 Flemish coalition agreement.
- **Link**: https://arxiv.org/abs/2607.15095

### 38. Filesystem-Based Memory for LLM Agents
- **Authors**: Sizhe Zhou, Sheldon Yu et al.
- **Institution**: University of Illinois / N/A
- **Abstract**: Proposes filesystem-inspired hierarchical memory organization for LLM agents, supporting organization, evolution, and sustainability of agent memory.
- **Key Innovations**: Filesystem metaphor for agent memory; hierarchical organization with evolutionary updates.
- **Link**: https://arxiv.org/abs/2607.26637

### 39. AgentGUI: An Interface for Observing and Steering Long-Running AI Agents
- **Authors**: Xuan Zhao, Jiwoong Sohn, Qinyue Zheng, Michael Moor
- **Institution**: N/A
- **Abstract**: GUI for real-time observation and intervention in long-running autonomous AI agent execution, enabling human-in-the-loop steering.
- **Key Innovations**: Real-time agent monitoring and intervention interface; human-in-the-loop steering for multi-step agent tasks.
- **Link**: https://arxiv.org/abs/2607.26300

---

## Key Themes

| Theme | Papers | Trend |
|-------|--------|-------|
| **Generative Recommendation** | TMallGS, Grevo, SPARC, WhisperRec | Industry adoption of LLM architectures for ranking/retrieval |
| **SSM-Attention Hybrids** | SISA, KLA, MARS | Score-level fusion emerges as new design axis beyond block/head-level |
| **LLM Security** | CogBias (bit-flip), Position Sensitivity | New attack surfaces in LLM inference and recommendation |
| **RL with Verifiable Rewards** | Codenames RLVR, NFL Win Prob, SERPO | Scaling RL without human preferences for objective tasks |
| **Human-in-Loop Agents** | Coachable Agents, AgentGUI, DASH | Real-time steering and interpretability for deployed agents |
| **Game Playing** | Cortex, MindGames, FootsiesGym | Open-source models closing gap with proprietary systems |
| **Data Auditing & Alignment** | Shapley Audit, Constitutional Midtraining | Scrutiny of benchmark integrity and alignment mechanisms |
