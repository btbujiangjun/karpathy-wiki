# arXiv AI Research Report - July 17, 2026

## Summary
Recent advances in AI, LLMs, recommendation systems, advertising, sequential modeling, CTR prediction, and game AI. This report covers papers from the last few months, focusing on industrial applications and novel architectures.

---

## 1. Large Language Models (LLMs)

### 1.1 MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning
**Authors**: Ruilin Tong et al.
**Institution**: Unknown
**Abstract**: MILES is a framework that dynamically expands step-wise memory and applies correctness-optimized memory composition under realistic test-time constraints. It maintains modular memory units consisting of asymmetric pairs of sub-goal embeddings and sub-instructions, each associated with a learnable selection head. The memory structure enables a coarse-to-fine retrieval mechanism for self-improving LLM reasoning.
**Key Innovations**: Modular memory units with learnable selection heads, coarse-to-fine retrieval mechanism, test-time memory expansion.
**arXiv Link**: https://arxiv.org/abs/2607.06974

### 1.2 LLM-as-a-Verifier: A General-Purpose Verification Framework
**Authors**: Unknown
**Institution**: Unknown
**Abstract**: Introduces a verification framework that provides fine-grained feedback for agentic tasks without requiring additional training. Computes the expectation over the distribution of scoring token logits to generate continuous scores. Enables verification scaling across multiple dimensions: score granularity, repeated evaluation, and criteria decomposition.
**Key Innovations**: Probabilistic verification using scoring token logits, cost-efficient ranking algorithm, multi-dimensional verification scaling.
**arXiv Link**: https://arxiv.org/abs/2607.05391

### 1.3 KARLA: Knowledge-base Augmented Retrieval for Language Models
**Authors**: Unknown
**Institution**: Unknown
**Abstract**: Allows an LLM to automatically pull in factual knowledge from a knowledge base during token generation. Enables factual knowledge updates without retraining, tracing facts to knowledge bases for transparency, and smaller models achieving same factual accuracy as larger models.
**Key Innovations**: Special tokens triggering KB queries, separation of linguistic competence from factual knowledge, post-training factual grounding.
**arXiv Link**: https://arxiv.org/abs/2606.26807

### 1.4 Belief-reality separation in language models
**Authors**: Unknown
**Institution**: Unknown
**Abstract**: Shows that capable language models hold what a character believes apart from what is true through two separable mechanisms: a generic value slot that binds attributed value and a router at query position selecting which frame (belief or reality) a query reads out.
**Key Innovations**: Identification of belief-reality separation mechanisms, slot-and-router architecture for non-actual contexts.
**arXiv Link**: https://arxiv.org/abs/2607.11945

### 1.5 POPS: Recovering Unlearned Multi-Modality Knowledge in MLLMs
**Authors**: Jianing Zhu et al.
**Institution**: Unknown
**Abstract**: Proposes an adversarial strategy to recover supposedly unlearned multi-modality knowledge from MLLMs. Uses prompt-suffix optimization to elicit potential private examples, then fine-tunes models to disclose true private information.
**Key Innovations**: Prompt-optimized parameter shaking, recovery of supposedly unlearned knowledge, exposing vulnerabilities in machine unlearning.
**arXiv Link**: https://arxiv.org/abs/2607.06649

---

## 2. Recommendation Systems

### 2.1 GLASS: Generative Recommender for Long-sequence Modeling
**Authors**: Shiteng Cao, Junda She, Ji Liu, Bin Zeng, Chengcheng Guo et al.
**Institution**: Unknown
**Abstract**: Integrates long-term user interests into generative recommendation via SID-Tier and Semantic Search. Maps long-term interactions into unified interest vector to enhance prediction of initial SID token. Uses semantic hard search with generated coarse-grained semantic ID as dynamic keys.
**Key Innovations**: SID-Tier for interest mapping, semantic hard search with dynamic keys, adaptive gated fusion module.
**arXiv Link**: https://arxiv.org/abs/2602.05663

### 2.2 SIDReasoner: Reasoning over Semantic IDs for Generative Recommendation
**Authors**: Yingzhi He, Yan Sun, Junfei Tan, Yuxin Chen et al.
**Institution**: Unknown
**Abstract**: Two-stage framework that elicits reasoning over SIDs by strengthening SID-language alignment. Uses multi-task training on enriched SID-centered corpus and GRPO for outcome-based feedback to steer effective reasoning trajectories.
**Key Innovations**: SID-language alignment via multi-task training, teacher-assisted semantic expansion, outcome-driven reinforcement for reasoning.
**arXiv Link**: https://arxiv.org/abs/2603.23183

### 2.3 GenRec: Preference-Oriented Generative Framework for Large-Scale Recommendation
**Authors**: Yanyan Zou, Junbo Qi, Lunsong Huang, Yu Li et al.
**Institution**: JD.com
**Abstract**: Addresses challenges in scaling generative retrieval to industrial systems. Proposes Page-wise NTP task, asymmetric linear Token Merger, and GRPO-SR for preference alignment. Deployed on JD App with 9.5% improvement in click count and 8.7% in transaction count.
**Key Innovations**: Page-wise NTP, Token Merger for compression, GRPO-SR with hybrid rewards, production deployment at scale.
**arXiv Link**: https://arxiv.org/abs/2604.14878

### 2.4 AgentX: Agent-Driven Self-Iteration of Industrial Recommender Systems
**Authors**: AgentX Team (Kuaishou)
**Institution**: Kuaishou
**Abstract**: Multi-agent system that autonomously generates, implements, evaluates, and learns from recommendation experiments. Orchestrate four stages: Brainstorm Agent, Developing Agent, Evaluation Agent, and Harness Evolution layer (SGPO). Deployed with 3 workers turning 374 ideas into 10 launchable rollouts.
**Key Innovations**: Self-evolving development engine, SGPO for semantic-gradient updates, closed-loop experiment automation.
**arXiv Link**: https://arxiv.org/abs/2606.26859

### 2.5 Gryphon: Unified Architecture for Semantic-ID Generation and Item-Level Scoring
**Authors**: Daria Tikhonovich, Oleg Sorokin, Vladislav Dodonov et al.
**Institution**: Unknown (Industrial music service)
**Abstract**: Encoder-decoder generative recommendation architecture that adds jointly trained item-level scoring component alongside SID generation. Resolves generated SIDs to concrete items and re-scores them directly, sidestepping miscalibrated sequence scores.
**Key Innovations**: Item-level scoring alongside SID generation, collision resolution for identical SIDs, production deployment in music service.
**arXiv Link**: https://arxiv.org/abs/2606.08604

---

## 3. Advertising & CTR Prediction

### 3.1 CADET: Context-Conditioned Ads CTR Prediction With Decoder-Only Transformer
**Authors**: David Pardoe, Neil Daftary, Miro Furtado et al.
**Institution**: LinkedIn
**Abstract**: End-to-end decoder-only transformer for ads CTR prediction. Introduces context-conditioned decoding with multi-tower prediction heads, self-gated attention, timestamp-based RoPE, and session masking strategies. Achieves 11.04% CTR lift in online A/B testing.
**Key Innovations**: Context-conditioned decoding architecture, self-gated attention, timestamp-based RoPE, session masking for train-serve consistency.
**arXiv Link**: https://arxiv.org/abs/2602.11410

### 3.2 GRAB: LLM-Inspired Sequence-First CTR Prediction
**Authors**: Shaopeng Chen, Chuyue Xie, Huimin Ren et al.
**Institution**: Baidu
**Abstract**: End-to-end generative framework for CTR prediction with Causal Action-aware Multi-channel Attention (CamA). Demonstrates scaling behavior with monotonic improvement as longer interaction sequences are used. Deployed at Baidu with 3.05% revenue increase and 3.49% CTR rise.
**Key Innovations**: CamA mechanism for temporal dynamics, sequence-first paradigm, scaling laws for CTR models.
**arXiv Link**: https://arxiv.org/abs/2602.01865

### 3.3 GR4AD: Generative Recommendation for Large-Scale Advertising
**Authors**: Unknown
**Institution**: Kuaishou
**Abstract**: Production-oriented generative recommender for real-time advertising. Introduces UA-SID for advertisement tokenization, LazyAR decoder for efficiency, VSL and RSPO for value alignment, and dynamic beam serving. Achieves up to 4.2% ad revenue improvement.
**Key Innovations**: UA-SID tokenization, LazyAR decoder, RSPO for ranking-guided optimization, dynamic beam serving.
**arXiv Link**: https://arxiv.org/abs/2602.22732

### 3.4 AdNanny: One Reasoning LLM for All Offline Ads Recommendation Tasks
**Authors**: Nan Hu, Han Li, Jimeng Sun et al.
**Institution**: Microsoft (Bing Ads)
**Abstract**: Single unified LLM serving as reasoning-centric backbone for offline ads tasks. Built by fine-tuning 671B-parameter DeepSeek-R1 checkpoint with Megatron-based trainer. Deployed in Bing Ads for query-ad relevance labeling, keyword generation, and user profiling.
**Key Innovations**: Unified reasoning LLM for multiple offline tasks, Megatron-based training for large hybrid models, reasoning-augmented corpora.
**arXiv Link**: https://arxiv.org/abs/2602.01563

### 3.5 OneRanker: Unified Generation and Ranking in Industrial Advertising
**Authors**: Unknown
**Institution**: Tencent (WeChat)
**Abstract**: Achieves architectural-level deep integration of generation and ranking. Uses value-aware multi-task decoupling, coarse-to-fine collaborative target awareness with Fake Item Tokens, and input-output dual-side consistency guarantees. Deployed on WeChat channels with +1.34% GMV improvement.
**Key Innovations**: Value-aware multi-task decoupling, Fake Item Tokens for target awareness, distribution consistency constraint.
**arXiv Link**: https://arxiv.org/abs/2603.02999

---

## 4. Sequential Modeling

### 4.1 Mamba-3: Improved Sequence Modeling using State Space Principles
**Authors**: Aakash Lahoti, Kevin Y. Li, Berlin Chen et al.
**Institution**: Unknown
**Abstract**: Introduces three core improvements: more expressive recurrence from SSM discretization, complex-valued state update rule, and MIMO formulation. Achieves significant gains across retrieval, state-tracking, and language modeling tasks with comparable perplexity to Mamba-2 using half the state size.
**Key Innovations**: SSM discretization improvements, complex-valued state updates, MIMO formulation for better performance.
**arXiv Link**: https://arxiv.org/abs/2603.15569

### 4.2 Oryx: Hybrid Model with Flexible Sequence Modeling
**Authors**: Kevin Y. Li, Asher Trockman, Ananda Theertha Suresh et al.
**Institution**: Unknown
**Abstract**: Hybrid model that flexibly switches between different mixers throughout a sequence. Ties at least 90% of parameters across mixers, enabling attention and recurrent modes to operate over shared internal representations. Outperforms baselines by at least 0.7 percentage points on averaged language modeling tasks.
**Key Innovations**: Sequence-axis hybridization, shared representations across mixers, flexible switching between attention and recurrence.
**arXiv Link**: https://arxiv.org/abs/2605.28769

### 4.3 MuonSSM: Orthogonalizing State Space Models
**Authors**: Unknown
**Institution**: Unknown
**Abstract**: Stabilizes SSM training by explicitly conditioning geometry of memory updates. Augments SSMs with momentum-based pathway and lightweight Newton-Schulz transformation on low-rank input injections. Shows consistent gains across language, vision, and time-series benchmarks.
**Key Innovations**: Momentum-based pathway, Newton-Schulz transformation for spectral conditioning, bounded updates while preserving parallel scan.
**arXiv Link**: https://arxiv.org/abs/2606.30461

### 4.4 NextFlow: Unified Sequential Modeling for Multimodal Understanding
**Authors**: Huichao Zhang, Liao Qu, Yiheng Liu et al.
**Institution**: Unknown
**Abstract**: Unified decoder-only autoregressive transformer trained on 6 trillion interleaved text-image discrete tokens. Uses next-scale prediction for visual generation instead of raster-scan, enabling 1024x1024 image generation in 5 seconds. Achieves state-of-the-art performance among unified models.
**Key Innovations**: Next-scale prediction for images, unified text-image tokenization, prefix-tuning for reinforcement learning.
**arXiv Link**: https://arxiv.org/abs/2601.02204

### 4.5 Sparse Delta Memory: Scaling Linear RNNs through Sparsity
**Authors**: Loïc Cabannes, Pierre-Emmanuel Mazaré et al.
**Institution**: Meta FAIR, Inria Paris
**Abstract**: Extends Gated DeltaNet architecture by replacing dense key-value outer product with sparse reads/writes to large explicit memory. Scales hidden state to orders of magnitude higher capacity while maintaining same compute budget. Achieves lower training loss than full attention at 8B scale.
**Key Innovations**: Sparse addressing scheme for memory scaling, learned initial state as parametric memory, constant compute with larger state.
**arXiv Link**: https://arxiv.org/abs/2607.07386

---

## 5. CTR Prediction Models

### 5.1 DS-MLP: Dual-Stream MLP for CTR Prediction
**Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao et al.
**Institution**: Renmin University, ByteDance, Meituan
**Abstract**: Novel feature interaction framework using knowledge distillation to consolidate explicit feature interaction learning into main MLP network, while parallel MLP captures implicit interactions. Achieves state-of-the-art performance with simple MLP structure.
**Key Innovations**: Dual-stream MLP architecture, knowledge distillation for feature interactions, simple yet effective design.
**arXiv Link**: https://arxiv.org/abs/2606.04944

### 5.2 SparseCTR: Sparse Attention for Long-term Behaviors
**Authors**: Weijiang Lai, Beihong Jin et al.
**Institution**: Unknown
**Abstract**: Efficient model for long-term user behaviors with three-branch sparse self-attention mechanism. Segments behavior sequences in personalized manner, proposes composite relative temporal encoding. Shows scaling law phenomenon across three orders of magnitude in FLOPs.
**Key Innovations**: Three-branch sparse attention, personalized behavior segmentation, scaling laws for CTR models.
**arXiv Link**: https://arxiv.org/abs/2601.17836

### 5.3 DeRes: Decoupling Residual Stability and Adaptivity
**Authors**: Unknown
**Institution**: Unknown
**Abstract**: Dual-path inter-layer connector for CTR Transformers with Identity residual path and Block Attention Residual path. Uses Pointwise AttnRes with SiLU activation instead of Softmax. Achieves +0.32% AUC on industrial dataset with steeper compute-AUC scaling law.
**Key Innovations**: Dual-path design, Pointwise AttnRes with SiLU, improved scaling efficiency.
**arXiv Link**: https://arxiv.org/abs/2606.07980

### 5.4 LoopCTR: Loop Scaling for CTR Prediction
**Authors**: Jiakai Tang, Runfeng Zhang et al.
**Institution**: Unknown
**Abstract**: Introduces loop scaling paradigm that increases training-time computation through recursive reuse of shared model layers. Decouples computation from parameter growth. Train-multi-loop, infer-zero-loop strategy where single forward pass outperforms all baselines.
**Key Innovations**: Loop scaling paradigm, recursive layer reuse, process supervision at every loop depth.
**arXiv Link**: https://arxiv.org/abs/2604.19550

### 5.5 GenCI: Generative Modeling of User Interest Shift
**Authors**: Unknown
**Institution**: Unknown
**Abstract**: Generative user intent framework leveraging semantic interest cohorts. Uses next-item prediction to produce candidate interest cohorts, hierarchical candidate-aware network for refinement. Trained end-to-end with joint optimization scheme.
**Key Innovations**: Generative user intent framework, semantic interest cohorts, hierarchical candidate-aware modeling.
**arXiv Link**: https://arxiv.org/abs/2601.18251

---

## 6. Game AI & Reinforcement Learning

### 6.1 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games
**Authors**: Unknown
**Institution**: Unknown
**Abstract**: Open training framework for VLM agents using adapted PPO with lightweight turn-level critic. Trains on Super Mario Land requiring 100+ turns of interaction. Outperforms frontier models by at least 3x average game progresses.
**Key Innovations**: Turn-level critic for stability, multi-task RL training, open framework for practical agentic tasks.
**arXiv Link**: https://arxiv.org/abs/2605.00347

### 6.2 Multiplayer Interactive World Models
**Authors**: Unknown
**Institution**: Unknown
**Abstract**: First multiplayer world model for highly dynamic environments. 5-billion-parameter latent diffusion model generates four-player matches in real time at 20 FPS on single Nvidia B200. Rollouts stay stable far beyond training horizon, continuing for hours.
**Key Innovations**: Multiplayer conditioning scheme, real-time generation at scale, long-horizon stability.
**arXiv Link**: https://arxiv.org/abs/2607.05352

### 6.3 GIFT: Games as Informal Training for Generalizable LLMs
**Authors**: Unknown
**Institution**: Unknown
**Abstract**: Proposes using games as environment for LLM informal learning. Introduces Nested Training Framework that transforms implicit OR objective into explicit AND objective. Demonstrates that game-based informal learning improves generalization across ability-oriented benchmarks.
**Key Innovations**: Nested training framework, game-based informal learning, multi-task RL across game environments.
**arXiv Link**: https://arxiv.org/abs/2601.05633

### 6.4 From Trainee to Trainer: LLM-Designed Training Environment
**Authors**: Chao Chen, Chengzu Li et al.
**Institution**: HKUST (GZ), Cambridge
**Abstract**: Framework where current policy model analyzes failure trajectories and proposes modifications to next-stage training environment. Introduces MAPF-FrozenLake as controllable testbed. 4B Qwen3 model outperforms larger proprietary LLMs as environment designer.
**Key Innovations**: LLM-as-Environment Engineer, environment redesign from failure analysis, RL improves self-diagnostic ability.
**arXiv Link**: https://arxiv.org/abs/2606.17682

### 6.5 T-STAR: Tree-structured Self-Taught Agent Rectification
**Authors**: Yu Li, Sizhe Tang, Tian Lan
**Institution**: Unknown
**Abstract**: Framework that recovers latent correlated reward structure across trajectories by consolidating them into unified Cognitive Tree. Enables variance-reduced advantage estimation and thought grafting at critical divergence points. Shows consistent improvements across embodied, interactive, reasoning, and planning tasks.
**Key Innovations**: Cognitive Tree construction, Introspective Valuation, In-Context Thought Grafting, Surgical Policy Optimization.
**arXiv Link**: https://arxiv.org/abs/2604.07165

---

## Key Trends

1. **Generative Recommendation**: Shift from traditional DLRMs to autoregressive generation over semantic IDs, with production deployments at JD, Kuaishou, and LinkedIn.

2. **LLM Integration**: LLMs being used for verification, reasoning, and as backbones for recommendation/advertising tasks.

3. **Scaling Laws**: Evidence of scaling laws in CTR models and recommendation systems, similar to LLM scaling.

4. **Production Deployment**: Many papers report successful industrial deployment with significant business metrics improvements.

5. **Hybrid Architectures**: Combination of attention and state-space models for efficient sequence modeling.

6. **Self-Improvement**: Frameworks enabling models to improve themselves through self-play, environment design, or recursive self-improvement.

7. **Sparse Efficiency**: Sparse attention and memory mechanisms enabling efficient long-sequence modeling.

---

*Report generated on July 17, 2026*