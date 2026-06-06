---
title: arXiv Daily — AI Research Survey (June 4, 2026)
type: synthesis
created: 2026-06-04
updated: 2026-06-04
sources: [arXiv cs.AI, cs.LG, cs.IR, cs.CL]
tags: [arxiv-daily, llm, reasoning, recommendation, ctr, advertising, games, rl, sequential-modeling]
---

# arXiv Daily — AI Research Survey (June 4, 2026)

> Coverage: recent submissions from arXiv (May 27 – June 3, 2026) across AI, LLMs, recommendation, CTR, advertising, sequential modeling, games, and RL. ~40 papers highlighted.

---

## 1. LLM Reasoning & RL Post-Training

### POPO: Group Prioritized Off-Policy Optimization for LLM Reasoning
- **arXiv**: [2606.01281](https://arxiv.org/abs/2606.01281)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: RLVR suffers from zero-variance rewards when response groups are all-correct or all-incorrect. POPO replaces ineffective on-policy groups with effective off-policy groups via recency-based replay; uses decoupled importance sampling for stable trust-region updates. Accelerates RL finetuning with significantly fewer rollouts.
- **Key Innovation**: Prioritized group replay + decoupled off-policy optimization eliminates ineffective samples without extra rollout cost.

### OmniOPD: Logit-Free On-Policy Distillation via Speculative Verification
- **arXiv**: [2606.01476](https://arxiv.org/abs/2606.01476)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Replaces brittle token-level logit matching with Monte Carlo rollouts and chunk-level semantic similarity. Peak-entropy scheduler audits only high-uncertainty reasoning forks. Dirichlet-Multinomial Bayesian prior + base-model KL anchor bound variance. Outperforms SFT by +45.31% on math, +18.52% on code; surpasses white-box OPD by +28.64%.
- **Key Innovation**: Black-box teacher compatible; chunk-level semantic verification extracts cleaner signal than token-level logits.

### KnowRL: Boosting LLM Reasoning via RL with Minimal-Sufficient Knowledge Guidance
- **arXiv**: [2604.12627](https://arxiv.org/abs/2604.12627)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Decomposes hints into atomic knowledge points (KPs), uses Constrained Subset Search (CSS) to construct compact interaction-aware subsets. Identifies pruning interaction paradox. KnowRL-Nemotron-1.5B reaches 74.16 average accuracy across 8 reasoning benchmarks, new SOTA at 1.5B scale.
- **Key Innovation**: Minimal-sufficient guidance via KP decomposition; CSS handles inter-KP dependencies.

### ScaleLogic: Expressiveness Is Key for Long-Horizon LLM Reasoning
- **arXiv**: [2605.06638](https://arxiv.org/abs/2605.06638)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Synthetic logical reasoning framework with independent control over proof depth and logical expressiveness. RL compute follows power law T ∝ D^γ (R²>0.99) where γ grows from 1.04 to 2.60 with expressiveness. More expressive training yields +10.66 pts downstream gains and better compute efficiency.
- **Key Innovation**: First controlled study isolating reasoning depth vs. expressiveness; shows LLM long-horizon limits are surmountable via training methodology.

### OAPL: LLMs Can Learn to Reason Via Off-Policy RL
- **arXiv**: [2602.19362](https://arxiv.org/abs/2602.19362)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Embraces off-policyness from asynchronous training. Derives KL-regularized closed-form objective that trains on lagged policy rollouts without importance sampling. Matches DeepCoder on LiveCodeBench with 3× fewer generations; stable with 400-step policy lag.
- **Key Innovation**: OAPL — first systematic demonstration that on-policy learning is unnecessary for RL post-training.

### GenAC: Generative Critic for Value Modeling in LLM RL
- **arXiv**: [2604.10701](https://arxiv.org/abs/2604.10701)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Revisits value models for LLM RL. Replaces one-shot scalar critic with generative critic doing chain-of-thought reasoning before value estimation. In-Context Conditioning keeps critic calibrated to evolving policy. Outperforms both value-based (PPO) and value-free (GRPO) baselines.
- **Key Innovation**: Generative Actor-Critic — first demonstration that stronger value modeling improves credit assignment in LLM RL.

### REAL: Regression-Aware RL for LLM-as-a-Judge
- **arXiv**: [2603.17145](https://arxiv.org/abs/2603.17145)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Principled RL framework optimizing regression rewards for LLM evaluators. Uses generalized policy gradient that decomposes into CoT exploration + prediction refinement. Qwen3-32B achieves significant gains over SFT and standard RL.
- **Key Innovation**: First integration of regression objectives into RL exploration for LLM evaluation.

### RLAD: Reinforcement-aware Knowledge Distillation for LLM Reasoning
- **arXiv**: [2602.22495](https://arxiv.org/abs/2602.22495)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Replaces static KL teacher regularization with Trust Region Ratio Distillation (TRRD). Integrates teacher guidance into advantage-weighted, trust-region policy updates. Consistent gains over GRPO and KDRL on logic/math reasoning.
- **Key Innovation**: Selective imitation — student follows teacher only when beneficial for RL objective.

### Reward Modeling for RL-Based LLM Reasoning (Survey)
- **arXiv**: [2602.09305](https://arxiv.org/abs/2602.09305)
- **Authors**: Pei-Chi Pan et al.
- **Affiliation**: —
- **Abstract**: Introduces Reasoning-Aligned Reinforcement Learning (RARL) framework systematizing reward paradigms. Analyzes reward hacking, evaluation bias, hallucination, distribution shift. Critically evaluates existing benchmarks for contamination and misalignment.
- **Key Innovation**: Unified taxonomy connecting reward design to core LLM reasoning challenges.

### LLM Reasoning Is Latent, Not the Chain of Thought (Position Paper)
- **arXiv**: [2604.15726](https://arxiv.org/abs/2604.15726)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Argues LLM reasoning should be studied as latent-state trajectory formation, not surface CoT. Formalizes three hypotheses (H0/H1/H2) separating latent states, surface traces, and serial compute. Recommends treating latent dynamics as default object of study.
- **Key Innovation**: Factorized, compute-audited evaluation design for disentangling surface traces, latent states, and compute budgets.

### Large Language Model Reasoning Failures (Survey)
- **arXiv**: [2602.06176](https://arxiv.org/abs/2602.06176)
- **Authors**: Peiyang Song et al.
- **Affiliation**: —
- **Abstract**: First comprehensive survey on LLM reasoning failures. Novel categorization: embodied vs. non-embodied (informal/formal). Failure axis: fundamental, application-specific, robustness. Systematic root cause analysis and mitigation strategies.
- **Key Innovation**: Unified framework for fragmented research on LLM reasoning weaknesses; public GitHub collection.

---

## 2. LLM Architecture & Theory

### Beyond the Black Box: Theory and Mechanism of LLMs (Survey)
- **arXiv**: [2601.02907](https://arxiv.org/abs/2601.02907)
- **Authors**: Zeyu Gan et al.
- **Affiliation**: —
- **Abstract**: Unified lifecycle-based taxonomy: Data Preparation → Model Preparation → Training → Alignment → Inference → Evaluation. Analyzes data mixtures theory, representational limits, alignment optimization dynamics. Identifies frontier challenges: synthetic data self-improvement limits, safety guarantees bounds, emergent intelligence origins.
- **Key Innovation**: Structured roadmap from engineering heuristics toward principled LLM science.

### Gecko: Efficient Neural Architecture for Arbitrary-Length Sequences
- **arXiv**: [2601.06463](https://arxiv.org/abs/2601.06463)
- **Authors**: Xuezhe Ma et al.
- **Affiliation**: —
- **Abstract**: Builds on Megalodon (EMA + gated attention). Introduces timestep decay normalization, sliding chunk attention, adaptive working memory. Gecko-7B reaches loss 1.68 (vs. Llama2-7B 1.75, Megalodon-7B 1.70). Handles up to 4M tokens without context-extension; retrieves from 4× longer than attention window.
- **Key Innovation**: Inherent long-context capability; no context-extension techniques needed.

### Tokenizer-Free LLMs via Hierarchical Autoregressive Transformer (HAT)
- **arXiv**: [2603.15953](https://arxiv.org/abs/2603.15953)
- **Authors**: Aleph Alpha
- **Affiliation**: Aleph Alpha
- **Abstract**: Byte-level encoder/decoder with pre-trained Llama backbone. Llama-3.1-8B-TFree-HAT and 70B-TFree-HAT reduce non-backbone params from 13% to <3%. Competitive with original Llama 3.1 on most benchmarks. Production vLLM serving with dual KV-cache management.
- **Key Innovation**: First scale demonstration of tokenizer-free LLMs up to 70B; shows embedding/head overparameterization.

### AA-SVD: Anchored and Adaptive SVD for LLM Compression
- **arXiv**: [2604.02119](https://arxiv.org/abs/2604.02119)
- **Authors**: Atul Kumar et al.
- **Affiliation**: —
- **Abstract**: Fast low-rank factorization compression without retraining. Anchors compressed layers to original outputs while modeling input distribution shifts from upstream compression. Block-level joint optimization. Survives aggressive ratios where ASVD/SVD-LLM collapse.
- **Key Innovation**: Dual constraint (output fidelity + distribution shift); block-level error compensation.

### Challenges for LLM Inference Hardware (Survey)
- **arXiv**: [2601.05047](https://arxiv.org/abs/2601.05047)
- **Authors**: Xiaoyu Ma et al.
- **Affiliation**: —
- **Abstract**: Identifies memory/interconnect (not compute) as primary LLM inference bottleneck. Proposes High Bandwidth Flash, Processing-Near-Memory, 3D stacking, low-latency interconnect. Covers both datacenter and mobile.
- **Key Innovation**: Architecture research roadmap for LLM Decode-phase memory wall.

### Sparse Activation for Accelerating LLM Pre-Training
- **arXiv**: [2602.06183](https://arxiv.org/abs/2602.06183)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: First method to sparsify all FFN matrix multiplications during training using 2:4 weight sparsity + Venom activation sparsity. Optimal sparse:dense step ratio (1:1 to 1:3.5). 1.37-1.7× end-to-end speedup on Llama 1B/7B while matching accuracy.
- **Key Innovation**: Novel activation function for Venom-format sparsity; hybrid sparse+dense training recipe.

---

## 3. Agentic Reasoning & Multi-Turn

### AXPO: Agent Explorative Policy Optimization for Multimodal Agentic Reasoning
- **arXiv**: [2605.28774](https://arxiv.org/abs/2605.28774)
- **Authors**: Byung-Kwan Lee et al.
- **Affiliation**: —
- **Abstract**: Identifies Thinking-Acting Gap: tool use on only ~30% rollouts, all-wrong on ~40% questions. AXPO fixes thinking prefix and resamples tool call + continuation. SFT+AXPO outperforms SFT+GRPO (+1.8pp Pass@1); 8B surpasses 32B Base on Pass@4.
- **Key Innovation**: Structural asymmetry-aware RL for agentic reasoning with tool use.

### ProactiveLLM: Active Interaction for Streaming LLMs
- **arXiv**: [2606.00523](https://arxiv.org/abs/2606.00523)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Mask-based streaming modeling + synchronized privileged self-distillation. Retains 97.16% offline quality with 78% context. Validated across text and speech streaming tasks (translation, summarization, QA).
- **Key Innovation**: Endogenous sufficiency cues without external teachers/annotations for interaction timing.

### KLong: Training LLM Agent for Extremely Long-Horizon Tasks
- **arXiv**: [2602.17547](https://arxiv.org/abs/2602.17547)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Framework for training LLM agents on extremely long-horizon tasks. (Details truncated but addresses key challenges in long-horizon agentic reasoning and planning.)
- **Key Innovation**: Systematic approach to extending LLM agent capabilities for extended task horizons.

### Extracting Books from Production Language Models
- **arXiv**: [2601.02671](https://arxiv.org/abs/2601.02671)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Two-phase procedure (probe + iterative continuation) extracts memorized copyrighted text from Claude 3.7 Sonnet, GPT-4.1, Gemini 2.5 Pro, Grok 3. Up to 95.8% nv-recall for Harry Potter from Claude. GPT-4.1 most resistant (requires 10-1000× more attempts).
- **Key Innovation**: Systematic memorization extraction from production LLMs; comparative resistance analysis.

---

## 4. Generative Recommendation & Advertising

### GR4AD: Generative Recommendation for Large-Scale Advertising
- **arXiv**: [2602.22732](https://arxiv.org/abs/2602.22732)
- **Authors**: Kuaishou
- **Affiliation**: Kuaishou
- **Abstract**: End-to-end generative recommender with UA-SID tokenization, LazyAR decoder, VSL + RSPO for value alignment. Dynamic Beam Serving adapts to load. Up to 4.2% ad revenue improvement. Deployed on Kuaishou (400M+ users), <100ms latency, 500+ QPS per L20.
- **Key Innovation**: Production-grade generative ad recommender co-designed across representation, learning, serving.

### GPR: Generative Pre-trained Recommender (Tencent Weixin)
- **arXiv**: [2511.10138](https://arxiv.org/abs/2511.10138)
- **Authors**: Tencent
- **Affiliation**: Tencent
- **Abstract**: First one-model framework replacing cascaded ad system with end-to-end generative task. HHD dual-decoder, MTP + VAFT + HEPO training. Deployed on Weixin Channels, significant GMV and CTCVR improvements.
- **Key Innovation**: First successful end-to-end generative ad recommendation deployment at scale.

### OneRanker: Unified Generation and Ranking (Tencent)
- **arXiv**: [2603.02999](https://arxiv.org/abs/2603.02999)
- **Authors**: Dekai Sun et al.
- **Affiliation**: Tencent
- **Abstract**: Value-aware multi-task decoupling, coarse-to-fine collaborative target awareness via Fake Item Tokens, KV pass-through + Distribution Consistency loss. Full deployment on Weixin Channels, GMV +1.34%.
- **Key Innovation**: Architectural-level deep integration of generation and ranking stages.

### RankUp: High-Rank Representations (Tencent Weixin)
- **arXiv**: [2604.17878](https://arxiv.org/abs/2604.17878)
- **Authors**: Xu Huang et al.
- **Affiliation**: Tencent
- **Abstract**: Mitigates representation collapse with randomized permutation splitting, multi-embedding, global token integration, crossed pretrained tokens. GMV lifts: Video Accounts +3.41%, Official Accounts +4.81%, Moments +2.12%.
- **Key Innovation**: First study showing parameter growth ≠ representation capacity; effective-rank-aware architecture.

### GRAB: Generative Ranking for Ads at Baidu
- **arXiv**: [2602.01865](https://arxiv.org/abs/2602.01865)
- **Authors**: Baidu
- **Affiliation**: Baidu
- **Abstract**: End-to-end generative ranking with Causal Action-aware Multi-channel Attention (CamA). STS training decouples dense/sparse optimization. Deployed on Baidu home feed: CTR +3.49%, CPM +3.05%.
- **Key Innovation**: Fuses DLRM sparse feature engineering with generative sequential modeling.

### UniSID: End-to-End Semantic ID Generation for Generative Ad Recommendation
- **arXiv**: [2602.10445](https://arxiv.org/abs/2602.10445)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Replaces two-stage RQ pipeline with end-to-end joint SID-embedding optimization. Multi-granularity contrastive learning + summary-based ad reconstruction. Up to 45.46% improvement on ad retrieval.
- **Key Innovation**: First end-to-end SID generation bypassing pre-trained embedding bottleneck.

### AsymRec: Asymmetric Generative Recommendation
- **arXiv**: [2605.14512](https://arxiv.org/abs/2605.14512)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Decouples input/output representations. Multi-expert Semantic Projection (MSP) for continuous input, Multi-faceted Hierarchical Quantization (MHQ) for structured discrete targets. Outperforms SOTA GenRec by avg 15.8%. Online A/B: total consumption +1.4%, GMV +1.9%.
- **Key Innovation**: Identifies dual-stage (input + output) information bottleneck in GenRec; asymmetric solution.

### GEM-Rec: One Model, Two Markets — Bid-Aware Generative Recommendation
- **arXiv**: [2603.22231](https://arxiv.org/abs/2603.22231)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Integrates monetization into generative recommendation. Control tokens decouple ad placement from item selection. Bid-Aware Decoding injects real-time bids into inference. Theoretical guarantee of allocation monotonicity.
- **Key Innovation**: First generative recommendation handling both organic and sponsored content with inference-time bid steering.

### LLM-HYPER: Generative CTR for Cold-Start Ad Personalization
- **arXiv**: [2604.12096](https://arxiv.org/abs/2604.12096)
- **Authors**: —
- **Affiliation**: Top US e-commerce platform
- **Abstract**: Treats LLM as hypernetwork to generate linear CTR model weights from multimodal ad content. Few-shot CoT over CLIP-retrieved campaigns. Cold-start NDCG@10 +55.9%. Competitive with warm-start in 30-day online A/B.
- **Key Innovation**: Decouples expensive LLM inference from low-latency serving; training-free cold-start ranking.

---

## 5. CTR Prediction

### CADET: Context-Conditioned Ads CTR (LinkedIn)
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Authors**: LinkedIn
- **Affiliation**: LinkedIn
- **Abstract**: Decoder-only transformer for ads CTR. Context-conditioned multi-tower decoding, self-gated attention, timestamp RoPE, session masking, custom Flash Attention. Deployed on LinkedIn homefeed sponsored updates. CTR +11.04% vs. LiRank.
- **Key Innovation**: Resolves CTR-position chicken-and-egg problem; first decoder-only transformer for ads CTR at LinkedIn scale.

### EST: Efficient Scaling Laws in CTR Prediction (Taobao)
- **arXiv**: [2602.10811](https://arxiv.org/abs/2602.10811)
- **Authors**: Alibaba
- **Affiliation**: Taobao (Alibaba)
- **Abstract**: Efficiently Scalable Transformer with Lightweight Cross-Attention and Content Sparse Attention. Unified sequence modeling without lossy aggregation. Deployed on Taobao display: RPM +3.27%, CTR +1.22%. Stable power-law scaling.
- **Key Innovation**: Domain-specific insights (asymmetric information density, modality priors) for efficient CTR scaling.

### HyFormer: Unified Sequence Modeling and Feature Interaction (ByteDance)
- **arXiv**: [2601.12681](https://arxiv.org/abs/2601.12681)
- **Authors**: ByteDance
- **Affiliation**: ByteDance
- **Abstract**: Unifies long-sequence modeling and feature interaction via alternating Query Decoding + Query Boosting. Replaces decoupled pipeline with bidirectional information flow. Superior scaling. Deployed in Douyin Search.
- **Key Innovation**: Global tokens as shared semantic interface; iterative optimization paradigm.

### FEDIN: Frequency-Enhanced Deep Interest Network
- **arXiv**: [2605.01726](https://arxiv.org/abs/2605.01726)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Discovery: user attention scores show distinct spectral entropy when conditioned on positive vs. negative targets. Target-aware spectrum filtering in frequency branch + time-domain branch. Robust against noise.
- **Key Innovation**: First application of target-aware frequency-domain analysis for sequential CTR.

### DAIAN: Deep Adaptive Intent-Aware Network for Trigger-Induced Recommendation
- **arXiv**: [2602.13971](https://arxiv.org/abs/2602.13971)
- **Authors**: Alibaba (Xianyu)
- **Affiliation**: Alibaba
- **Abstract**: Addresses "intent myopia" in trigger-induced recommendation. User Intent Modeling + Diverse Intent Extraction + Similarity-Enhanced Intent Network. Online: CTR +1.59%, diversity +1.73%, bills +2.37%.
- **Key Innovation**: Three-stage training strategy for intent-aware CTR in TIR scenarios.

### Memento: RAG-Style Long-Retention Data Scaling (Meta)
- **arXiv**: [2605.24051](https://arxiv.org/abs/2605.24051)
- **Authors**: Meta
- **Affiliation**: Meta
- **Abstract**: Treats history scaling as information retrieval. MMR-based retrieval from 365+ days of history. Representation Memento + Data Memento. 5-10× resource efficiency. Online: CTR +1%, CVR +1.2% on Facebook Feed/Reels.
- **Key Innovation**: RAG paradigm applied to long-retention recommendation; production-scale with sub-10ms latency.

### UniMixer: Unified Architecture for Scaling Laws in Recommendation
- **arXiv**: [2604.00590](https://arxiv.org/abs/2604.00590)
- **Authors**: Kuaishou
- **Affiliation**: Kuaishou
- **Abstract**: Unifies attention-based, TokenMixer-based, and factorization-machine-based scaling blocks. Parameterized rule-based TokenMixer bridges all approaches. UniMixing-Lite compresses parameters while improving performance.
- **Key Innovation**: Unified theoretical framework bridging three mainstream scaling paradigms.

### LoopCTR: Loop Scaling Paradigm for CTR
- **arXiv**: [2604.19550](https://arxiv.org/abs/2604.19550)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Recursive reuse of shared layers decouples computation from parameter growth. Sandwich architecture (Entry/Loop/Exit) + Hyper-Connected Residuals + MoE. Train-multi-loop, infer-zero-loop outperforms all baselines.
- **Key Innovation**: Computation scaling through recursive reuse rather than parameter stacking.

### Select-LLM: LLM Selection with Limited Annotations
- **arXiv**: [2605.24981](https://arxiv.org/abs/2605.24981)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: First active model selection framework for LLMs. Expected information gain from pairwise output similarities. Across 23 datasets, 156 models: annotation cost reduction up to 81.8% for best model selection.
- **Key Innovation**: Model-agnostic selection via output similarities; no architecture/weight access assumptions.

---

## 6. Games & Sequential Decision Making

### STRATAGEM: Transferable Reasoning via Trajectory-Modulated Game Self-Play
- **arXiv**: [2604.17696](https://arxiv.org/abs/2604.17696)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Selectively reinforces domain-agnostic, adaptive reasoning trajectories. Reasoning Transferability Coefficient (φ) + Reasoning Evolution Reward (ψ). From 3 text games (TicTacToe, Kuhn Poker, Negotiation): AIME24 10%→20%, AIME25 3.3%→13.3%, AMC23 50%→60%.
- **Key Innovation**: Addresses domain specificity and contextual stasis barriers in game-based reasoning transfer.

### SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **arXiv**: [2506.24119](https://arxiv.org/abs/2506.24119)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Fully online multi-turn multi-agent RL for LLMs. Role-conditioned advantage estimation stabilizes training. Up to +10% across 8 reasoning benchmarks on Qwen/Llama families. Multi-game training yields strongest transfer.
- **Key Innovation**: Distributed actor-learner for self-play LLM reasoning; RAE for multi-agent stability.

### Odysseus: Scaling VLMs to 100+ Turn Decision-Making via RL
- **arXiv**: [2605.00347](https://arxiv.org/abs/2605.00347)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Adapted PPO with lightweight turn-level critic + positive-advantage filtering for long-horizon game playing (Super Mario Land). 3× improvement over frontier models. Generalization to in/out-of-domain settings.
- **Key Innovation**: First systematic RL recipe for VLM long-horizon (100+ turn) embodied agents.

### CART: Robust Adversarial RL in Stochastic Games via Sequence Modeling
- **arXiv**: [2510.11877](https://arxiv.org/abs/2510.11877)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: Conservative Adversarially Robust Decision Transformer. Formulates stage games with expected maximum value over subsequent states. NashQ conditioning for policies that are simultaneously robust and conservative.
- **Key Innovation**: First DT-based adversarial robustness framework for stochastic games.

### Transformers as Game Players: Provable In-Context Game-Playing
- **arXiv**: [2410.09701](https://arxiv.org/abs/2410.09701)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: (ICLR 2026) First theoretical proof that Transformers can perform in-context no-regret learning in zero-sum matrix and Markov games, approximating Online Mirror Descent. Accuracy dependent on model size; longer trajectories improve game-playing.
- **Key Innovation**: First provable ICGP results; Lagrangian OMD reformulation for Transformer approximation.

### VINTIX II: Decision Pre-Trained Transformer as Scalable ICRL
- **arXiv**: [2604.05112](https://arxiv.org/abs/2604.05112)
- **Authors**: —
- **Affiliation**: —
- **Abstract**: (ICLR 2026) Scales in-context RL to multi-domain settings. Addresses generalization to unseen tasks beyond AD and DPT limitations.
- **Key Innovation**: Scalable ICRL with improved cross-task generalization.

---

## 7. Memento (Meta) — Long-Retention for Ads

Covered in Section 5 above. See [Memento entry](#memento-rag-style-long-retention-data-scaling-meta).

---

## Highlights of the Day

| Area | Top Pick | Why |
|------|----------|-----|
| RL Post-Training | **POPO** + **OAPL** | Off-policy learning is the emerging trend; both show dramatic efficiency gains |
| Distillation | **OmniOPD** | Black-box teacher distillation surpasses white-box; paradigm shift for proprietary model usage |
| CTR Architecture | **CADET** (+11.04% CTR), **GR4AD** (+4.2% rev) | Decoder-only transformers are displacing DLRMs in production |
| Generative Rec | **GPR**, **GR4AD**, **OneRanker** | Tencent/Kuaishou all pushing GenRec to full production deployment |
| Games → Reasoning | **SPIRAL**, **STRATAGEM** | Game self-play transfers to math reasoning; AIME25 4× improvement |
| Scaling Laws | **EST**, **UniMixer** | Domain-specific CTR scaling laws outpacing generic LLM-style scaling |
| LLM Theory | **Latent Reasoning** position | Challenges CoT-centric view; may reshape how we evaluate reasoning |
**
