---
title: "arXiv AI Search — July 2026"
type: synthesis
created: 2026-07-18
updated: 2026-07-18
sources: [arxiv.org]
tags: [arxiv, ai, llm, recommendation, ctr, sequential-modeling, games, rl]
---

# arXiv AI Search — July 2026

Curated selection of recent arXiv preprints across AI, LLMs, recommendation, CTR, games, and sequential modeling.

---

## LLM Training & Alignment

### 1. ScaleRL: Scaling Reinforcement Learning Compute for LLMs
- **Authors**: Devvrit Khatri, Lovish Madaan, et al.
- **Institution**: Google Research
- **Link**: [arXiv:2510.13786](https://arxiv.org/abs/2510.13786)
- **Key Innovations**: First large-scale systematic study (400K GPU-hours) defining predictive scaling curves for RL in LLMs. Proposes ScaleRL recipe — combines asynchronous Pipeline-RL, truncated importance-sampling, prompt-level loss averaging, batch-level advantage normalization.
- **Abstract**: Fits sigmoidal compute-performance curves; shows that loss aggregation, normalization, curriculum primarily affect compute efficiency not asymptote. Validated on a 100K GPU-hour run.

### 2. MIPU: Monotonic Inference Policy Update for LLM RL
- **Authors**: (anonymous)
- **Institution**: (anonymous)
- **Link**: [arXiv:2606.29526](https://arxiv.org/abs/2606.29526)
- **Key Innovations**: Identifies training-inference mismatch as an objective-level problem — not just system discrepancy. Proposes MIPI principle: optimize inference policy not training policy. Uses sampler-referenced candidate updates + inference-gap-aware acceptance.
- **Abstract**: Under FP8-quantized rollout (high mismatch), MIPU improves reasoning performance and training stability on Qwen3 models.

### 3. LLMZero: Discovering Adaptive Training Strategies for RL Post-Training
- **Authors**: (anonymous)
- **Institution**: (anonymous)
- **Link**: [arXiv:2606.18388](https://arxiv.org/abs/2606.18388)
- **Key Innovations**: LLM agents search over training trajectories via tree search, diagnose pathologies, propose coordinated hyperparameter transitions. Discovers structural principle: capacity params accumulate monotonically, regularization params oscillate.
- **Abstract**: On 4 GRPO tasks, improves base model by 9-140% relative. Transfers across tasks.

### 4. LLM-as-a-Verifier: General-Purpose Verification Framework
- **Authors**: (anonymous)
- **Institution**: (anonymous)
- **Link**: [arXiv:2607.05391](https://arxiv.org/abs/2607.05391)
- **Key Innovations**: Probabilistic verification — computes expectation over scoring token logits for continuous scores. Three scaling axes: score granularity, repeated evaluation, criteria decomposition. Training-free.
- **Abstract**: SOTA on Terminal-Bench V2 (86.5%), SWE-Bench Verified (78.2%), RoboRewardBench (87.4%), MedAgentBench (73.3%).

### 5. LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL
- **Authors**: Yujin Kim, Namgyu Ho, Sangmin Hwang, et al.
- **Institution**: KAIST
- **Link**: [arXiv:2607.04412](https://arxiv.org/abs/2607.04412)
- **Key Innovations**: Extends LLM role from judge to tutor — detects non-challenging prompts via pairwise comparison, appends atomic constraints to create self-calibrating curriculum.
- **Abstract**: Outperforms policy-unaware and policy-adaptive baselines on FollowBench, AdvancedIF, InfoBench.

### 6. MILES: Modular Instruction Memory with Learnable Selection
- **Authors**: Ruilin Tong et al.
- **Institution**: (anonymous)
- **Link**: [arXiv:2607.06974](https://arxiv.org/abs/2607.06974)
- **Key Innovations**: Dynamic step-wise memory with learnable selection heads. Coarse-to-fine retrieval for test-time reasoning improvement.
- **Abstract**: Matches or outperforms prior methods with superior accuracy-efficiency tradeoffs.

### 7. DPO Data Selection (BeeS)
- **Authors**: anonymous
- **Institution**: (anonymous)
- **Link**: [arXiv:2502.14560](https://arxiv.org/abs/2502.14560)
- **Key Innovations**: Margin-maximization principle for DPO dataset curation. Bayesian aggregation of multiple margin sources (external + implicit). 10% of Ultrafeedback data yields 3-8% improvement across Llama, Mistral, Qwen.
- **Abstract**: Extends to iterative DPO with 25% online data.

---

## Model Architecture & Efficiency

### 8. In-Place Tokenizer Expansion for Pre-trained LLMs
- **Authors**: Jimmy Smith et al.
- **Institution**: (anonymous)
- **Link**: [arXiv:2607.15232](https://arxiv.org/abs/2607.15232)
- **Key Innovations**: Continues BPE merges on multilingual corpus to expand tokenizer post-training. Copy embedding rows unchanged, initialize new rows as mean of sub-tokens. Two-stage adaptation.
- **Abstract**: LFM2-8B expanded to 128K tokenizer. Hindi/Vietnamese encode in ~2.4x/2.6x fewer tokens. 2.2-3.7x per-character decode speedup.

### 9. Set Diffusion: Interpolating Token Orderings
- **Authors**: Marianne Arriola et al.
- **Institution**: (anonymous)
- **Link**: [arXiv:2607.01775](https://arxiv.org/abs/2607.01775)
- **Key Innovations**: New class of language models factorizing over flexible-position, flexible-length token sets. Set-causal diffusion supports KV cache updates. Enables arbitrary-order decoding.
- **Abstract**: Better speed-quality tradeoffs on math reasoning, summarization, unconditional generation vs prior diffusion LMs.

### 10. Legible-by-Construction: Attention and End-to-End Transformers
- **Authors**: Oskin et al.
- **Institution**: (anonymous)
- **Link**: [arXiv:2607.04319](https://arxiv.org/abs/2607.04319)
- **Key Innovations**: Sigmoid-bounded attention values become readable "does this feature hold" detectors. Boolean variant with explicit within-token intersection and set-difference. End-to-end legible LM at 125M params.
- **Abstract**: 44-62% of value channels become crisp, contextual detectors. Restricts dead units; quality at parity with conventional baseline on LAMBADA and BLiMP.

### 11. Audex: Unified Audio Intelligence Without Regressing Text
- **Authors**: Wei Ping et al. (NVIDIA)
- **Institution**: NVIDIA
- **Link**: [arXiv:2607.05196](https://arxiv.org/abs/2607.05196)
- **Key Innovations**: Unified audio-text LLM (Nemotron-Labs-Audex-30B-A3B). Single Transformer decoder with audio inputs projected into text embedding space. Multi-stage supervised + Cascade RL + on-policy distillation.
- **Abstract**: SOTA audio understanding, ASR, TTS, speech translation, audio generation while preserving text LLM performance.

### 12. Visual Pretraining for Language Intelligence
- **Authors**: Yiming Zhang, Zhonghan Zhao, Wenwei Zhang et al.
- **Institution**: Shanghai AI Lab, USTC, Zhejiang Univ., SJTU
- **Link**: [arXiv:2607.09657](https://arxiv.org/abs/2607.09657)
- **Key Innovations**: Foundation model learns from visual documents directly without text extraction. Autoregressive pretraining predicting document patches in latent space.
- **Abstract**: VP outperforms text-only pretraining on same corpus using only 25% token budget. Cross-modal alignment improves.

### 13. MinT: Managed Infrastructure for Millions of LoRA Adapters
- **Authors**: MindLab
- **Institution**: MindLab
- **Link**: [arXiv:2605.13779](https://arxiv.org/abs/2605.13779)
- **Key Innovations**: Managed infrastructure for LoRA post-training and serving at million-adapter scale. Scale Up (1T+ params), Scale Down (adapter-only handoff <1% of model), Scale Out (10^6 addressable adapters).
- **Abstract**: Adapter-only handoff reduces step 18.3x (4B dense) and 2.85x (30B MoE). Packed MoE LoRA improves engine loading 8.5-8.7x.

### 14. LongStraw: Long-Context RL Beyond 2M Tokens
- **Authors**: Changhai Zhou et al.
- **Institution**: MindLab / Fudan
- **Link**: [arXiv:2607.14952](https://arxiv.org/abs/2607.14952)
- **Key Innovations**: Architecture-aware execution for million-token RL post-training under fixed GPU budget. Prompts evaluated once without autograd; response branches replayed one at a time.
- **Abstract**: On 8 H20 GPUs, completes GRPO at 2.1M positions (Qwen3.6-27B). Extends to 4.46M in stress test. GLM-5.2 validated at 2.1M on 32 H20s.

---

## Mechanistic Interpretability & Reasoning

### 15. Belief-Reality Separation in Language Models
- **Authors**: Oliver Steele et al.
- **Institution**: (anonymous)
- **Link**: [arXiv:2607.11945](https://arxiv.org/abs/2607.11945)
- **Key Innovations**: Identifies two mechanisms: a generic value slot binds attributed value; a router at query position selects belief vs reality frame. Dissociated routing subspaces flip query between frames.
- **Abstract**: Results hold across 3 architectures; behavior emerges between 3B and 7B across 5 model families.

### 16. Statistical Self-Consistency in Language Models
- **Authors**: Patrik Wolf, Thomas Kleine Buening, Andreas Krause, Celestine Mendler-Dünner
- **Institution**: ETH Zurich
- **Link**: [arXiv:2607.15277](https://arxiv.org/abs/2607.15277)
- **Key Innovations**: Tests if LLMs obey law of total probability via binary tree evaluation scaffold. Identifies "macro fallacy" — fine-grained subpopulation estimates more accurate than direct estimates.
- **Abstract**: Widespread consistency violations across frontier models. Proposes statistical self-consistency as reference-free evaluation criterion.

### 17. Outcome-Based RL Provably Leads Transformers to Reason
- **Authors**: Yuval Ran-Milo, Yotam Alexander, Shahar Mendel, Nadav Cohen
- **Institution**: Tel Aviv University
- **Link**: [arXiv:2601.15158](https://arxiv.org/abs/2601.15158)
- **Key Innovations**: Theoretical proof that gradient flow drives single-layer transformers to implement iterative graph traversal algorithm. Identifies critical role of "simple examples" in training distribution.
- **Abstract**: When simple examples have sufficient mass, model learns generalizable traversal. Training on OOD simple examples can boost in-distribution performance.

---

## CTR Prediction & Recommendation

### 18. GenCI: Generative User Intent for CTR Prediction
- **Authors**: anonymous
- **Institution**: Web Conference 2026
- **Link**: [arXiv:2601.18251](https://arxiv.org/abs/2601.18251)
- **Key Innovations**: Generative user intent framework with semantic interest cohorts. Transformer NTP generates candidate interest cohorts. Hierarchical candidate-aware network refines with cross-attention.
- **Abstract**: Outperforms SOTA on MovieLens, Amazon Fashion, Musical Instruments.

### 19. IDProxy: Cold-Start CTR at Xiaohongshu
- **Authors**: Guillaume Salha-Galvan et al.
- **Institution**: Xiaohongshu
- **Link**: [arXiv:2603.01590](https://arxiv.org/abs/2603.01590)
- **Key Innovations**: MLLMs generate proxy embeddings from rich content signals for cold-start items. Aligned with existing ID embedding space. End-to-end optimization under CTR objectives.
- **Abstract**: Successfully deployed in Explore Feed and Display Ads at Xiaohongshu.

### 20. SparseCTR: Sparse Attention for Long-term CTR
- **Authors**: W. Lai et al.
- **Institution**: Web Conference 2026
- **Link**: [arXiv:2601.17836](https://arxiv.org/abs/2601.17836)
- **Key Innovations**: TimeChunk segmentation + three-branch sparse attention (global/transition/local). RelTemporal encoding. Scaling law over 3 orders of FLOPs.
- **Abstract**: CTR +1.72%, CPM +1.41% in online A/B test. Outperforms dense attention baselines.

### 21. DAIAN: Deep Adaptive Intent-Aware Network for Trigger-Induced CTR
- **Authors**: Zhihao Lv, Longtao Zhang, Ailong He et al.
- **Institution**: Xianyu (Alibaba)
- **Link**: [arXiv:2602.13971](https://arxiv.org/abs/2602.13971)
- **Key Innovations**: Addresses "intent myopia" in Trigger-Induced Recommendation. Hybrid enhancer with ID + semantic info, adaptive selection based on varying intents.
- **Abstract**: CTR +1.59%, recommendation diversity +1.73% in online A/B test on Xianyu.

### 22. CTR-Sink: Attention Sink for LMs in CTR Prediction
- **Authors**: Zixuan Li, Binzong Geng, Jing Xiong et al.
- **Institution**: Ant Group / HKU
- **Link**: [arXiv:2508.03668](https://arxiv.org/abs/2508.03668)
- **Key Innovations**: Insert sink tokens between behaviors with recommendation-specific signals (temporal, semantic). Addresses semantic fragmentation in LM-based CTR.
- **Abstract**: AUC improvements 0.2-0.5% across industrial dataset, MovieLens, KuaiRec. Accepted KDD 2026.

### 23. GenRec: Preference-Oriented Generative Framework
- **Authors**: Yanyan Zou et al.
- **Institution**: JD.com
- **Link**: [arXiv:2604.14878](https://arxiv.org/abs/2604.14878)
- **Key Innovations**: Page-wise NTP task for generative retrieval. Token Merger compresses multi-token SIDs by ~2x. GRPO-SR with hybrid rewards.
- **Abstract**: 9.5% click count and 8.7% transaction count improvement on JD App. SIGIR 2026.

---

## Sequential / Generative Recommendation

### 24. RecRec: Recursive Reasoning for Sequential Recommendation
- **Authors**: (anonymous)
- **Institution**: (anonymous)
- **Link**: [arXiv:2607.12945](https://arxiv.org/abs/2607.12945)
- **Key Innovations**: Dual-state recursive reasoning — separates reasoning state from prediction state. Context Compressor + Recursive Reasoner. RL-free with deep supervision.
- **Abstract**: Outperforms reasoning-enhanced methods. Gains extend past training-time depth on 3/4 datasets.

### 25. RecRec (Refinement variant): Recursive Refinement
- **Authors**: (anonymous)
- **Institution**: (anonymous)
- **Link**: [arXiv:2607.10541](https://arxiv.org/abs/2607.10541)
- **Key Innovations**: Evidence-anchored correction mechanism prevents semantic drift. Only 3.9M-14M parameters.
- **Abstract**: Matches/outperforms SOTA sequential, graph-based, and LLM-based recommenders.

### 26. CMSL: Constructive Multi-Sequence Learning at Meta
- **Authors**: anonymous
- **Institution**: Meta
- **Link**: [arXiv:2606.28533](https://arxiv.org/abs/2606.28533)
- **Key Innovations**: Disentangles user history into "pure" thematic strands via latent sequence construction module. Linear attention for multi-sequence modeling. Addresses "context pollution" in monolithic sequences.
- **Abstract**: Deployed across ranking and retrieval across 4 major surfaces at Meta.

### 27. SRPFN: Single SR Model Pretrained from Synthetic Priors
- **Authors**: Woosung Kang, Jiwon Jeong, Jonghyeok Shin, Jeongwhan Choi, Noseong Park
- **Institution**: KAIST
- **Link**: [arXiv:2606.15752](https://arxiv.org/abs/2606.15752)
- **Key Innovations**: Pretrained on 25.6M synthetic sequences from hierarchical stochastic block model. Zero-gradient adaptation to target domains via support set conditioning.
- **Abstract**: 7.53% avg improvement over second-best across 5 benchmarks. Inference in ~1 min per dataset. KDD 2026.

### 28. UniRec: Chain-of-Attribute for Generative Recommendation
- **Authors**: anonymous
- **Institution**: unknown
- **Link**: [arXiv:2604.12234](https://arxiv.org/abs/2604.12234)
- **Key Innovations**: Bayesian analysis proving generative models with full feature access match discriminative. Chain-of-Attribute (CoA) prefixes SID with category/seller/brand tokens. Joint RFT and DPO.
- **Abstract**: CoA yields measurable per-step entropy reduction. Narrowing search space stabilizes beam search.

### 29. RecRec (GenRec variant): Generative Retrieval with RL
- **Authors**: anonymous
- **Institution**: (anonymous)
- **Link**: [arXiv:2607.02818](https://arxiv.org/abs/2607.02818)
- **Key Innovations**: Off-policy REINFORCE with multi-step importance weights. User feedback model for evaluation and test-time scaling. Trained on Yambda-5B.
- **Abstract**: RL agent improves cumulative session reward vs next-item prediction baselines.

### 30. FLAME: Frozen and Learnable Ensemble for Sequential Rec
- **Authors**: anonymous
- **Institution**: SIGIR 2026
- **Link**: [arXiv:2604.04038](https://arxiv.org/abs/2604.04038)
- **Key Innovations**: Simulates exponential ensemble diversity with only 2 networks. One frozen (semantic anchor), one learnable. Sub-module dynamic combination, contrastive alignment.
- **Abstract**: 4.55-7.69x faster convergence, 9.70% NDCG@20 improvement. Zero overhead at inference.

---

## Games, Agents & RL

### 31. Agentic Transformers Provably Learn to Search via RL
- **Authors**: anonymous
- **Institution**: (anonymous)
- **Link**: [arXiv:2606.00183](https://arxiv.org/abs/2606.00183)
- **Key Innovations**: Constructs two-head transformer implementing randomized DFS. Proves emergence from policy gradient under depth-wise curriculum. Depth generalization without expert demos.
- **Abstract**: Under imbalanced goals, discounting yields ranked DFS prioritizing higher-probability branches.

### 32. SPIRAL: Self-Play on Zero-Sum Games for Reasoning
- **Authors**: anonymous
- **Link**: [arXiv:2506.24119](https://arxiv.org/abs/2506.24119)
- **Key Innovations**: Fully online multi-agent RL for LLMs. Role-conditioned advantage estimation (RAE) stabilizes training. Multi-game training (TicTacToe, Kuhn Poker, Negotiation).
- **Abstract**: Up to 10% improvement across 8 reasoning benchmarks on Qwen and Llama. Benefits even DeepSeek-R1-Distill.

### 33. Stratagem: Learning Transferable Reasoning via Game Self-Play
- **Authors**: Xiachong Feng et al.
- **Link**: [arXiv:2604.17696](https://arxiv.org/abs/2604.17696)
- **Key Innovations**: Reasoning Transferability Coefficient + Reasoning Evolution Reward. Selectively reinforces abstract, domain-agnostic trajectories.
- **Abstract**: Strong gains on competition-level math, benchmarks across reasoning and code.

### 34. Odysseus: VLMs for 100+ Turn Game Decision-Making
- **Authors**: anonymous
- **Institution**: (anonymous)
- **Link**: [arXiv:2605.00347](https://arxiv.org/abs/2605.00347)
- **Key Innovations**: PPO with turn-level critic for long-horizon VLM agents. Tested on Super Mario Land (100+ turns). 3x game progress over frontier models.
- **Abstract**: Generalization in-game and cross-game while retaining general-domain capabilities.

### 35. CART: Robust Adversarial RL in Stochastic Games
- **Authors**: Xiaohang Tang et al.
- **Institution**: UCL
- **Link**: [OpenReview](https://openreview.net/pdf?id=pnUrJiHFwk)
- **Key Innovations**: Conservative Adversarially Robust Decision Transformer. Stage-game formulation with NashQ values. Handles stochastic transitions.
- **Abstract**: Better minimax value estimation, superior worst-case returns in adversarial stochastic games.

### 36. MARL-GPT: Foundation Model for Multi-Agent RL
- **Authors**: (anonymous)
- **Institution**: (Cognitive AI Systems Lab)
- **Link**: [arXiv:2604.05943](https://arxiv.org/abs/2604.05943)
- **Key Innovations**: Single GPT trained on 1.5B+ expert trajectories (SMACv2, GRF, POGEMA). Unified encoder across diverse MARL environments.
- **Abstract**: Competitive with specialized baselines on all environments. Foundation model approach to MARL.

### 37. Reward-Free Evolving Agents via Pairwise Validator
- **Authors**: Minghao Liu, Yue Wang, Wei Wei
- **Institution**: unknown
- **Link**: [arXiv:2607.14408](https://arxiv.org/abs/2607.14408)
- **Key Innovations**: Replaces scalar reward with pairwise validator (frozen LLM) for agent evolution. Two flavors: Adaptive Focus and Soft Elo.
- **Abstract**: Matches or exceeds full-reward baseline on prompt and code artifact substrates without labeling cost.

---

## Cross-Cutting Themes

| Theme | Key Papers |
|-------|-----------|
| **RL for LLM post-training** | ScaleRL, MIPI, LLMZero, LLM-as-a-Tutor, SPIRAL, Stratagem |
| **Verification as scaling axis** | LLM-as-a-Verifier |
| **Long-context RL training** | LongStraw |
| **Efficient LoRA infrastructure** | MinT |
| **CTR + generative models** | GenCI, GenRec, UniRec, SparseCTR |
| **Sequential recommendation** | CMSL (Meta), RecRec, SRPFN, FLAME |
| **Self-play games for reasoning** | SPIRAL, Stratagem, Agentic Transformers, CART |
| **VLM decision-making** | Odysseus, RxBrain |
| **Model interpretability** | Legible-by-Construction, Belief-Reality |
| **Data efficiency** | DPO-BeeS, SRPFN |
