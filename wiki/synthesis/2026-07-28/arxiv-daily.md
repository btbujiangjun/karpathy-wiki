---
title: "arXiv Daily: AI, LLMs, Recommendation, CTR, Sequential Modeling, Games"
type: synthesis
created: 2026-07-28
updated: 2026-07-28
tags: [arxiv, daily, llm, recommendation, ctr, sequential-modeling, games, reinforcement-learning]
---

# arXiv Daily — 2026-07-28

Curated recent papers across AI, LLMs, recommendation systems, advertising/CTR, sequential modeling, and games.

---

## LLMs & Reasoning

### 1. MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning
- **Authors:** Ruilin Tong, Dong Gong
- **Institution:** Not specified
- **Abstract:** Proposes a framework that dynamically expands step-wise memory and applies correctness-optimized memory composition for test-time LLM reasoning. Maintains modular memory units with asymmetric pairs of sub-goal embeddings and sub-instructions, each associated with a learnable selection head. Achieves coarse-to-fine retrieval mechanism that enables memory expansion from confident samples and learned selection heads for uncertain samples.
- **Key Innovations:** Modular instruction memory with learnable selection heads; coarse-to-fine retrieval for test-time reasoning; correctness-optimized memory composition under realistic constraints.
- **Link:** [arXiv:2607.06974](https://arxiv.org/abs/2607.06974)

### 2. LaCache: Exact Caching and Precision-Adaptive Inference for Diffusion Large Language Models
- **Authors:** X. Chen, C. Wu, H. Zhang, S. Xue, Z. Liu, S. Diao, L. Zhu, P. Luo, S. Han, E. Xie
- **Institution:** Not specified
- **Abstract:** Training-free acceleration framework for semi-autoregressive diffusion LLMs. Introduces Lossless State Memoization (LSM) caching three types of intermediate results (EmbedCache, RoPECache, FACache) and per-group FP8 quantization for FFN layers. Achieves ~1.3x standalone speedup and up to 40.2x combined speedup.
- **Key Innovations:** Lossless caching of intermediate denoising states; step-dependent mixed-precision strategy; composable with existing acceleration methods.
- **Link:** [arXiv:2607.16339](https://arxiv.org/abs/2607.16339v2)

### 3. In-Place Tokenizer Expansion for Pre-trained LLMs
- **Authors:** Jimmy T.H. Smith, Tarek Dakhran, Alberto Cabrera, Simon S. Lee, Paul Pak, Aditya Tadimeti, Tim Seyde, Maxime Labonne, Alexander Amini, Mathias Lechner
- **Institution:** Not specified
- **Abstract:** Recipe for upgrading a pre-trained model's tokenizer in-place by continuing BPE merges on multilingual corpus. Applied to LFM2-8B-A1B to produce LFM2.5-8B-A1B with 128K tokenizer. Achieves ~2.4x and ~2.6x fewer tokens for Hindi and Vietnamese, with 2.2-3.7x per-character decode speedup.
- **Key Innovations:** In-place tokenizer expansion preserving source tokens; mean initialization of new embeddings from sub-token sources; two-stage adaptation recipe.
- **Link:** [arXiv:2607.15232](https://arxiv.org/abs/2607.15232v1)

### 4. Set Diffusion: Interpolating Token Orderings Between Autoregression and Diffusion
- **Authors:** Marianne Arriola, Volodymyr Kuleshov
- **Institution:** Not specified
- **Abstract:** New class of language models using set diffusion with likelihood parameterization over flexible-position, flexible-length token sets and set-causal diffusion architecture supporting KV cache updates. Enables arbitrarily-ordered decoding including sliding-window sets.
- **Key Innovations:** Set-based diffusion over token sets; set-causal architecture with KV cache; flexible any-order decoding.
- **Link:** [arXiv:2607.01775](https://arxiv.org/abs/2607.01775v1)

### 5. LatentMT: Machine Translation with Latent Reasoning
- **Authors:** Wei-Rui Chen, Samar M. Magdy, Chiyu Zhang, Wenhui Zhu, Zhipeng Wang, Muhammad Abdul-Mageed
- **Institution:** Not specified
- **Abstract:** First systematic study of latent-reasoning looped LMs for MT. Adapts a 2.6B backbone with lightweight training. Across 32 translation directions, achieves performance comparable to models 3-5x larger. Shows recurrent computation improves quality then saturates.
- **Key Innovations:** Latent-reasoning LoopLM applied to MT; demonstrates compute-performance saturation curve; efficient training with compact models.
- **Link:** [arXiv:2607.18618](https://arxiv.org/abs/2607.18618v1)

### 6. LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget
- **Authors:** Changhai Zhou, Kieran Liu, Yuhua Zhou, Qian Qiao, Jun Gao, Harry Zhang, Irvine Lu, Nolan Ho, Lucian Cheng, Zhigang Zeng, Pony Ma, Weizhong
- **Institution:** Not specified
- **Abstract:** Architecture-aware execution stack for million-token RL post-training (GRPO). Evaluates shared prompt without autograd, retains only model-specific state, and replays short response branches. On 8 H20 GPUs, completes grouped scoring at 2.1M positions; stress test reaches 4.46M positions.
- **Key Innovations:** Autograd-free shared prompt evaluation; replay-based gradient computation; practical million-token RL post-training.
- **Link:** [arXiv:2607.14952](https://arxiv.org/abs/2607.14952v1)

### 7. Hidden Decoding at Scale: Latent Computation Scaling for LLMs
- **Authors:** Aiwei Liu, Cheng Shi, Chuhan Wu, et al.
- **Institution:** Not specified
- **Abstract:** Sequence-length scaling method expanding each token into n streams with independent embeddings. Introduces Stream-Factorized Attention reducing attention cost to near-linear in n. Trains WeLM-HD4-80B and WeLM-HD4-617B at n=4, first demonstrated sequence-length scaling at 100B+ MoE scale.
- **Key Innovations:** Token-to-stream expansion with independent embeddings; Stream-Factorized Attention for near-linear scaling; validated at 100B+ scale.
- **Link:** [arXiv:2607.08186](https://arxiv.org/abs/2607.08186v1)

---

## Recommendation Systems

### 8. AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems
- **Authors:** Changxin Lao, Fei Pan, Guozhuang Ma, Han Li, et al. (Kuaishou team)
- **Institution:** Kuaishou
- **Abstract:** Production-deployed multi-agent system that autonomously generates, implements, evaluates, and learns from recommendation experiments. Orchestrates Brainstorm Agent, Developing Agent, Evaluation Agent, and Harness Evolution (SGPO). Deployed at Kuaishou: 374 ideas → 10 launchable rollouts in 3 weeks, 8x concurrency, 3.7x business value over manual engineer, 0.561% user app-time gain, >100M RMB annualized revenue.
- **Key Innovations:** Closed-loop agent-driven experiment iteration; SGPO for semantic-gradient prompt optimization; autonomous paper reproduction and module ablation; deployed at industrial scale.
- **Link:** [arXiv:2606.26859](https://arxiv.org/abs/2606.26859v1)

### 9. UniRec: Bridging Generative and Discriminative Recommendation via Chain-of-Attribute
- **Authors:** Not specified (Shopee team)
- **Institution:** Shopee
- **Abstract:** Formalizes that generative recommendation gap arises from feature coverage not modeling asymmetry. Proposes Chain-of-Attribute (CoA) prefixing SID sequences with attribute tokens (category, seller, brand). Capacity-constrained SID suppresses token collapse; CDC injects scenario signals. Online A/B: +5.37% PVCTR, +4.76% orders, +5.60% GMV.
- **Key Innovations:** Theoretical proof that GR gap is feature-coverage-based; Chain-of-Attribute speculation-then-refinement paradigm; exposure-weighted capacity penalties for SID; conditional decoding context for multi-scenario.
- **Link:** [arXiv:2604.12234](https://arxiv.org/abs/2604.12234v3)

### 10. Gryphon: Unified Architecture for Semantic-ID Generation and Item-Level Scoring
- **Authors:** Daria Tikhonovich, Oleg Sorokin, Vladislav Dodonov, Mariia Ulianova, Ilya Murzin
- **Institution:** Not specified (Music service)
- **Abstract:** Encoder-decoder architecture adding jointly trained item-level scoring alongside SID generation. Resolves generated SIDs to concrete items and re-ranks with item-level scores, sidestepping miscalibrated beam-likelihood scores. Deployed as sole candidate source replacing 15+ generators and preranking stage.
- **Key Innovations:** Joint SID generation + item-level scoring in shared-encoder architecture; eliminates beam-likelihood miscalibration; simplifies candidate-generation stack.
- **Link:** [arXiv:2606.08604](https://arxiv.org/abs/2606.08604)

### 11. GenRec: Preference-Oriented Generative Framework for Large-Scale Recommendation
- **Authors:** Yanyan Zou, Junbo Qi, Lunsong Huang, Yu Li, Kewei Xu, Jiabao Gao, et al.
- **Institution:** JD.com
- **Abstract:** Deployed on JD App. Page-wise NTP task supervises over entire interaction pages. Asymmetric linear Token Merger compresses multi-token SIDs. GRPO-SR combines Group Relative Policy Optimization with NLL regularization and Hybrid Rewards. Online A/B: +9.5% click count, +8.7% transaction count.
- **Key Innovations:** Page-wise NTP for denser gradient signal; asymmetric Token Merger for 2x input compression; GRPO-SR with Hybrid Rewards preventing reward hacking.
- **Link:** [arXiv:2604.14878](https://arxiv.org/abs/2604.14878)

### 12. R3-REC: Reasoning-Driven Recommendation via Retrieval-Augmented LLMs
- **Authors:** Not specified
- **Institution:** Not specified
- **Abstract:** Prompt-centric, retrieval-augmented framework unifying Multi-level User Intent Reasoning, Item Semantic Extraction, Long-Short Interest Polarity Mining, Similar User Collaborative Enhancement, and Reasoning-based Interest Matching. Up to +10.2% HR@1, +6.4% HR@5 on ML-1M, Games, Bundle datasets.
- **Key Innovations:** Multi-granular interest signals with reasoning-driven scoring; RAG-style similar-user retrieval; training-light modular pipeline.
- **Link:** [arXiv:2603.13730](https://arxiv.org/abs/2603.13730v1)

### 13. GLASS: Generative Recommender for Long-sequence Modeling via SID-Tier and Semantic Search
- **Authors:** Shiteng Cao, Junda She, Ji Liu, Bin Zeng, et al.
- **Institution:** Not specified
- **Abstract:** Integrates long-term user interests into generative recommendation via SID-Tier (maps long-term interactions to unified interest vector) and semantic hard search (uses generated coarse-grained SIDs as dynamic keys). Semantic neighbor augmentation and codebook resizing address data sparsity.
- **Key Innovations:** SID-Tier for long-sequence interest integration; semantic hard search with adaptive gated fusion; codebook resizing strategies.
- **Link:** [arXiv:2602.05663](https://arxiv.org/abs/2602.05663v1)

### 14. RecRec: Recursive Refinement for Sequential Recommendation
- **Authors:** Not specified
- **Institution:** Not specified
- **Abstract:** Lightweight model maintaining compact latent state updated through shared recursive module. Evidence-anchored correction mechanism stabilizes refinement. Matches or outperforms SOTA with only 3.9M-14M parameters. Optimal recursion depth ~7 steps.
- **Key Innovations:** Evidence-anchored correction preventing semantic drift; recursive latent inference as alternative to deeper architectures; extreme parameter efficiency.
- **Link:** [arXiv:2607.10541](https://arxiv.org/abs/2607.10541v3)

### 15. RecRec: Latent Interests Recursive Reasoning for Sequential Recommendation
- **Authors:** Not specified
- **Institution:** Not specified
- **Abstract:** Dual-state recursive reasoning framework decoupling reasoning from prediction. Context Compressor distills hidden states into latent interests; Recursive Reasoner refines in separate intermediate space. Deep supervision allows adjustable inference depth without retraining.
- **Key Innovations:** Decoupled reasoning/prediction states; Interest Diversity Regularizer; backbone-agnostic multi-vector recipe.
- **Link:** [arXiv:2607.12945](https://arxiv.org/abs/2607.12945v1)

### 16. SRPFN: One Sequential Recommendation Model Pretrained from Synthetic Priors
- **Authors:** Woosung Kang, Jiwon Jeong, Jonghyeok Shin, Jeongwhan Choi, Noseong Park
- **Institution:** KAIST
- **Abstract:** Prior-data Fitted Network pretrained on 25.6M sequences from synthetic prior (hierarchical degree-corrected stochastic block model). Predicts next item in single forward pass without gradient updates. Average +7.53% improvement over second-best across 5 benchmarks. ~1 minute inference per dataset.
- **Key Innovations:** Training-free adaptation via support-set conditioning; synthetic prior from hDCSBM; single forward-pass inference across domains.
- **Link:** [arXiv:2606.15752](https://arxiv.org/abs/2606.15752v1)

### 17. FuXi-Linear: Linear Attention for Long-term Time-aware Sequential Recommendation
- **Authors:** Yufei Ye, Wei Guo, Hao Wang, Luankang Zhang, Heng Chang, Hong Zhu, et al.
- **Institution:** Not specified
- **Abstract:** Linear-complexity model with Temporal Retention Channel (independent periodic attention weights) and Linear Positional Channel. Demonstrates power-law scaling at thousand-length scale. Up to 10x speedup in prefill and 21x in decode vs. competitive baselines.
- **Key Innovations:** Temporal retention channel preventing temporal-semantic crosstalk; linear positional encoding; demonstrated power-law scaling in linear attention for recommendation.
- **Link:** [arXiv:2602.23671](https://arxiv.org/abs/2602.23671)

### 18. GenAIR: Generative Archetype-Grounded Item Representations
- **Authors:** Yifan Li, Jiahong Liu, Xinni Zhang, Hao Chen, Yankai Chen, Wenhao Yu, Jianting Chen, Irwin King
- **Institution:** Not specified
- **Abstract:** Uses LLM to infer archetype (conceptual profile of item's ideal target audience) from metadata, then extracts embeddings. Behavioral calibration objective grounds representations in real interaction patterns. Model-agnostic, integrates with GRU4Rec, BERT4Rec, SASRec.
- **Key Innovations:** Archetype-grounded item representations targeting audience profiles; behavioral calibration bridging semantic-behavioral gap; zero inference overhead.
- **Link:** [arXiv:2606.11023](https://arxiv.org/abs/2606.11023)

### 19. Efficient Sequential Recommendation via Personalization (PerSRec)
- **Authors:** Not specified
- **Institution:** Meta (Facebook Research)
- **Abstract:** Compresses long user interaction histories into learnable "personalized expert" tokens. Combined with recent interactions for recommendations. Reduces inference cost >11% while maintaining full-sequence performance. Validated on HSTU and HLLM architectures.
- **Key Innovations:** Learnable compression tokens as "personalized experts"; segment-level history compression; applicable across transformer-based rec models.
- **Link:** [arXiv:2601.03479](https://arxiv.org/abs/2601.03479v1)

### 20. HyTRec: Hybrid Temporal-Aware Attention for Long Behavior Sequential Recommendation
- **Authors:** Not specified
- **Institution:** Not specified
- **Abstract:** Hybrid attention architecture decoupling long-term (linear attention) and short-term (softmax attention) branches. Temporal-Aware Delta Network (TADN) dynamically upweights fresh signals. 8%+ Hit Rate improvement for users with long sequences.
- **Key Innovations:** Hybrid linear+softmax attention architecture; TADN temporal gating; efficient modeling of 10K+ interaction sequences.
- **Link:** [arXiv:2602.18283](https://arxiv.org/abs/2602.18283v1)

---

## CTR Prediction & Advertising

### 21. CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer
- **Authors:** David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, Liuqing Li, et al.
- **Institution:** LinkedIn
- **Abstract:** End-to-end decoder-only transformer for ads CTR prediction. Multi-tower prediction heads model post-scoring signals (ad position). Self-gated attention stabilizes training. Timestamp-based RoPE captures temporal relationships. Session masking prevents train-serve skew. Online A/B: +11.04% CTR lift over LiRank production baseline.
- **Key Innovations:** Context-conditioned decoding resolving chicken-and-egg CTR/ranking problem; self-gated attention; timestamp RoPE across timescales; session-aware masking.
- **Link:** [arXiv:2602.11410](https://arxiv.org/abs/2602.11410)

### 22. GRAB: LLM-Inspired Sequence-First CTR Prediction at Baidu
- **Authors:** Not specified
- **Institution:** Baidu
- **Abstract:** End-to-end generative framework for CTR prediction with Causal Action-aware Multi-channel Attention (CamA). Captures temporal dynamics and action signals. Online deployment: +3.05% revenue, +3.49% CTR. Shows monotonic ~linear improvement with longer sequences.
- **Key Innovations:** CamA mechanism for temporal + action signal capture; demonstrated scaling behavior with sequence length; full-scale industrial deployment.
- **Link:** [arXiv:2602.01865](https://arxiv.org/abs/2602.01865v2)

### 23. EST: Efficiently Scalable Transformer for CTR Prediction
- **Authors:** Mingyang Liu, Yong Bai, Zhangming Chan, et al.
- **Institution:** Alibaba (Taobao)
- **Abstract:** Fully unified modeling of all raw inputs. Lightweight Cross Attention (LCA) prunes redundant self-interactions; Content Sparse Attention (CSA) uses content similarity for dynamic selection. Exhibits stable power-law scaling. Deployed on Taobao: +3.27% RPM, +1.22% CTR.
- **Key Innovations:** Fully unified token sequence without lossy aggregation; LCA and CSA for efficiency; demonstrated power-law scaling in industrial CTR.
- **Link:** [arXiv:2602.10811](https://arxiv.org/abs/2602.10811)

### 24. LLM-HYPER: Generative CTR Modeling via LLM-Based Hypernetworks
- **Authors:** Luyi Ma, Wanjia Sherry Zhang, Zezhong Fan, Shubham Thakur, Kai Zhao, K. C. Yao, et al.
- **Institution:** Not specified (top U.S. e-commerce)
- **Abstract:** Treats LLMs as hypernetworks generating CTR estimator parameters in training-free manner. Few-shot CoT prompting over multimodal ad content. +55.9% NDCG@10 over cold-start baselines. Competitive with warm-start model in 30-day online A/B. Deployed in production.
- **Key Innovations:** LLM-as-hypernetwork for training-free weight generation; multimodal CoT reasoning; label-independent normalization and calibration; decoupled offline generation from online serving.
- **Link:** [arXiv:2604.12096](https://arxiv.org/abs/2604.12096)

### 25. IDProxy: Cold-Start CTR Prediction with Multimodal LLMs at Xiaohongshu
- **Authors:** Yubin, Haiming Xu, Yan Han, Xiyang Xiao, Yang Luo, et al.
- **Institution:** Xiaohongshu (Little Red Book)
- **Abstract:** Leverages MLLMs to generate proxy embeddings from rich content signals for cold-start items. Proxies aligned with existing ID embedding space end-to-end under CTR objectives. Deployed in Content Feed and Display Ads serving hundreds of millions daily.
- **Key Innovations:** MLLM-generated proxy embeddings for cold start; end-to-end alignment with ID embedding space; seamless integration into large-scale ranking pipelines.
- **Link:** [arXiv:2603.01590](https://arxiv.org/abs/2603.01590v1)

### 26. GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning
- **Authors:** Not specified
- **Institution:** Not specified
- **Abstract:** Generative user intent framework leveraging semantic interest cohorts. NTP task produces candidate interest cohorts as explicit intent representations. Hierarchical candidate-aware network refines via cross-attention. End-to-end joint optimization with self-supervised regularization.
- **Key Innovations:** Semantic interest cohorts as dynamic intent representations; generative recall-aware ranking alignment; candidate-aware cross-attention refinement.
- **Link:** [arXiv:2601.18251](https://arxiv.org/abs/2601.18251v1)

### 27. Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)
- **Authors:** Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution:** Renmin University, ByteDance, Meituan
- **Abstract:** Knowledge distillation consolidates explicit interaction learning into main MLP, parallel MLP captures implicit interactions. Two alignment strategies optimize dual-stream architecture. SOTA on Criteo, Avazu, and KDD-Cup datasets with low latency.
- **Key Innovations:** Distillation-based explicit+implicit MLP framework; final model is vanilla MLP (efficient); alignment strategies for dual-stream optimization.
- **Link:** [arXiv:2606.04944](https://arxiv.org/abs/2606.04944v1)

### 28. SparseCTR: Sparse Attention on Long-term Behaviors for CTR Prediction
- **Authors:** Weijiang Lai, Beihong Jin, Di Zhang, Siru Chen, Jiongyan Zhang, Yuhang Gou, Jian Dong, Xingxing Wang
- **Institution:** Not specified
- **Abstract:** Personalized time-aware chunking (TimeChunking) segments behavior sequences. Three-branch sparse self-attention identifies global interests, interest transitions, and short-term interests. Composite relative temporal encoding. Exhibits scaling law over 3 orders of magnitude. Online A/B: +1.72% CTR, +1.41% CPM.
- **Key Innovations:** Personalized temporal chunking for sparse attention; three-branch attention for interest decomposition; demonstrated scaling law in industrial CTR.
- **Link:** [arXiv:2601.17836](https://arxiv.org/abs/2601.17836)

---

## Games & Reinforcement Learning

### 29. Augmenting Game AI with Deep Reinforcement Learning
- **Authors:** Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslen
- **Institution:** EA (Electronic Arts)
- **Abstract:** Framework for deploying RL-based game AI in AAA production. Tested on EA SPORTS FC 25 (goalkeeper positioning) and Battlefield 6 (ground infantry). Uses SAC with advanced techniques reducing training from 4 days to 12 hours. 300K parameter MLP with 170µs inference time. Identifies authenticity, short training time, modularity, bug detection, and runtime constraints as key requirements.
- **Key Innovations:** Production-deployed RL for AAA game AI; overnight training pipeline; strict runtime inference budget compliance; modular integration with existing game systems.
- **Link:** [arXiv:2606.20210](https://arxiv.org/abs/2606.20210)

### 30. Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL
- **Authors:** Not specified
- **Institution:** Not specified
- **Abstract:** Adapts PPO with lightweight turn-level critic for VLM training in Super Mario Land (100+ turn episodes). 3x average game progress over frontier models. Open training framework combining SFT initialization with multi-task RL. Emergent in-game and cross-game generalization.
- **Key Innovations:** Turn-level critic decoupling credit assignment from token generation; positive-advantage filtering; multi-task auto-curriculum; generalization across game levels.
- **Link:** [arXiv:2605.00347](https://arxiv.org/abs/2605.00347v1)

### 31. Multiplayer Interactive World Models with Representation Autoencoders
- **Authors:** Anthony Hu, Vaclav Volhejn, Adrien Ramanana, Chris Mulder, et al.
- **Institution:** Not specified
- **Abstract:** First multiplayer world model for highly dynamic environments. 5B-parameter latent diffusion model generating four-player Rocket League matches in real-time (20 FPS on B200). Trained on 10K hours of bot gameplay. Rollouts stable out to 5 minutes, in practice hours.
- **Key Innovations:** Multiplayer conditioning on action streams; attribution of scene changes to correct player; stable long-horizon rollouts far beyond training horizon; real-time generation.
- **Link:** [arXiv:2607.05352](https://arxiv.org/abs/2607.05352v1)

### 32. GIFT: Games as Informal Training for Generalizable LLMs
- **Authors:** Not specified
- **Institution:** Not specified
- **Abstract:** Nested training framework combining formal (math) and informal (game) learning. Games include Matrix Games, TicTacToe, and Who's the Spy. GRPO-based RL with nested tasks enforces explicit AND objective. 7B model general ability increases from 42.00% to 55.84%.
- **Key Innovations:** Nested training framework preventing task interference; game-based informal learning for strategic/creative abilities; demonstration that diverse game types enhance generalization.
- **Link:** [arXiv:2601.05633](https://arxiv.org/abs/2601.05633v1)

### 33. Discovering Multiagent Learning Algorithms with LLMs
- **Authors:** Zun Li, John Schultz, Daniel Hennes, Marc Lanctot
- **Institution:** Not specified (DeepMind-related)
- **Abstract:** Uses AlphaEvolve (LLM-powered evolutionary coding) to discover MARL algorithms. Evolves VAD-CFR with volatility-sensitive discounting and consistency-enforced optimism. Evolves SHOR-PSRO with hybrid meta-solver blending Optimistic Regret Matching with smoothed best-pure-strategy distribution.
- **Key Innovations:** LLM-driven evolutionary algorithm discovery for MARL; non-intuitive mechanisms outperforming hand-designed baselines; automated transition from diversity to equilibrium finding.
- **Link:** [arXiv:2602.16928](https://arxiv.org/abs/2602.16928)
