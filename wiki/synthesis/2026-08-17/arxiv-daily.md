---
title: "arXiv Daily — AI, LLM, Recommendation, Ad/CTR, Sequential Modeling, Games"
type: synthesis
created: 2026-08-17
updated: 2026-08-17
tags: [arxiv, daily-digest, llm, recommendation, ctr, sequential-modeling, games, time-series]
---

# arXiv Daily Digest — 2026-08-17

> Curated selection of recent papers across AI, LLMs, recommendation systems, advertising/CTR, sequential modeling, time series, and game AI.

---

## 1. Large Language Models (LLMs)

### 1.1 Kimi K3: Open Frontier Intelligence

- **Authors**: Moonshot AI Team
- **Institution**: Moonshot AI
- **Abstract**: Introduces Kimi K3, a 2.8T parameter MoE model with 104B activated parameters, native vision, and 1M-token context window. Built on Kimi Delta Attention (KDA), Attention Residuals, and Stable LatentMoE. Achieves ~2.5× scaling efficiency improvement over Kimi K2. Post-training includes RL across general, agentic, and coding domains with multi-level reasoning effort. Released as open weights.
- **Key Innovations**: KDA for efficient long-sequence mixing; Stable LatentMoE (896 routed experts, 16 active per token); multi-teacher on-policy distillation for RL consolidation; million-token agentic RL infrastructure with persistent sandbox states.
- **Link**: https://arxiv.org/abs/2607.24653v1

### 1.2 LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Systematic study of scaling behavior for MoE diffusion language models (dLLMs). Trains LLaDA MoE v2, a 30B-A3B dLLM, from scratch on 23.5T tokens. Approaches Qwen3 on several benchmarks while using ~65% fewer pretraining tokens. After SFT, outperforms SDAR Chat on 7/8 reasoning and coding benchmarks.
- **Key Innovations**: Optimal nominal batch size grows faster for dLLMs than AR models; larger scales favor larger expert pools at fixed activated capacity; establishes practical scaling laws and design principles for MoE dLLMs.
- **Link**: https://arxiv.org/abs/2608.03457v1

### 1.3 Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Builds P-Bench (425 hypothesis-testing tasks) and Fisher-R1, an open-weight LLM agent trained via SFT + RL with verified statistical reward. Fisher-R1-14B outperforms GPT-5.4 and DeepSeek-V4-Pro on hypothesis testing, achieving 21% average relative improvement in single-trial success over DeepSeek-V4-Pro.
- **Key Innovations**: Synthetic task generator with verified answer keys for statistical reasoning; RL with verified statistical reward; P-Bench benchmark for evaluating p-value validity.
- **Link**: https://arxiv.org/abs/2608.07437v1

### 1.4 Recursive Language Models (RLMs)

- **Authors**: Alex Zhang, Tim Kraska, Omar Khattab
- **Institution**: [See paper]
- **Abstract**: Proposes RLMs that treat long prompts as external environment, allowing the LLM to programmatically examine, decompose, and recursively call itself over prompt snippets. Handles inputs up to 100× beyond context windows. Outperforms base LLMs and common long-context scaffolds on 4 diverse tasks.
- **Key Innovations**: REPL environment for offloading context; recursive sub-calling for information-dense inputs; scales to 10M+ tokens at comparable or lower cost than direct calls.
- **Link**: https://arxiv.org/abs/2512.24601

### 1.5 Reference-Free Post-Training of Open LLMs for Multilingual MT

- **Authors**: [See paper]
- **Institution**: Xiaomi Research
- **Abstract**: Applies GRPO with reference-free quality estimation reward for multilingual MT across 46 languages. MiLMMT-46-v1.0 models consistently improve over SFT counterparts, outperforming Seed-X, HY-MT2, and TranslateGemma. Achieves leading reference-free scores against Google Translate, Gemini 3 Pro, and GPT-5.
- **Key Innovations**: Language-gated quality estimation rewards; SFT–RL checkpoint interpolation for controllable trade-off; on-policy distillation analysis.
- **Link**: https://arxiv.org/abs/2608.10812v2

### 1.6 Learning When to Trust via Selective Context Preference Optimization (SCOPE)

- **Authors**: Xian Sun, Wei Chow, Yingshuo Wang, Junhao Liu, Wei Gao, Qing Wu, Lingdong Kong
- **Institution**: NUS, UC Berkeley, UC Irvine, Northeastern, NTU, Duke
- **Abstract**: Introduces MIST benchmark (4 matched conditions: clean, misleading, correct-context, irrelevant-context) and SC2W metric. SCOPE mines clean-correct/misleading-wrong failures and optimizes DPO over matched preference pairs. Roughly halves SC2W on Qwen3-4B and Llama-3.2-3B while preserving accuracy on clean/correct/irrelevant contexts.
- **Key Innovations**: Signal-counterfactual preference method; selective trust framing (vs. resistance alone); zero-shot transfer to 3 external benchmarks.
- **Link**: https://arxiv.org/abs/2608.06377v1

### 1.7 OctoLong: Mid-Training On Cross-Repository Code Contexts

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Context engineering pipeline using AST parser + language server for recursive retrieval of code references up to millions of tokens. OctoLong-Instruct suite (600M–14B params) trained on ~50B-token mixture. Supplanting just 12% of conventional context-extension corpora with OctoLong data yields gains in long-range retrieval, state tracking, and repository-level code understanding.
- **Key Innovations**: Dependency-rich cross-repository code contexts; model merging for generalization; 128K context window models based on Qwen3.
- **Link**: https://arxiv.org/abs/2608.05141v1

### 1.8 LaCache: Exact Caching and Precision-Adaptive Inference for Diffusion LLMs

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Training-free acceleration framework for SAR inference in DLLMs. Combines Lossless State Memoization (EmbedCache, RoPECache, FACache) with per-group FP8 quantization. Achieves ~1.3× standalone speedup, up to 40.2× combined with existing methods.
- **Key Innovations**: Lossless caching of unchanged tokens' intermediate states; online softmax statistics caching in FlashAttention; step-dependent FP8 quantization.
- **Link**: https://arxiv.org/abs/2607.16339v2

---

## 2. Recommendation Systems

### 2.1 GenRec: An LLM-Backed Recommendation Ranker at Netflix

- **Authors**: Netflix Team
- **Institution**: Netflix
- **Abstract**: LLM-backed recommendation ranker built on an in-house foundational LLM. Phase 2 post-trains with recommendation-specific data, labels, and reward signals. With ~40× less Phase-2 labeled training data and fewer input signals, achieves +1.6% relative MRR lift offline and statistically significant improvements in a 10%-traffic, 4-week A/B test on batch-compute surfaces.
- **Key Innovations**: Verbalized user histories and context engineering; catalog-aware ranking head; prefill-only inference approach for cost-constrained serving; paradigm shift from feature engineering to context engineering.
- **Link**: https://arxiv.org/abs/2608.10257v1

### 2.2 ConnectionMind: Social Networks + LLMs for Personalized Recommendation at Meta

- **Authors**: Meta Team
- **Institution**: Meta
- **Abstract**: Integrates social network structure with LLMs for recommendation. Constructs heterogeneous graph connecting users, items, friends, groups, and creator pages. Uses LLM-based policy for graph reasoning over personalized paths. Two-stage training: SFT + end-to-end RL. Deployed at Meta, achieving +0.43% video watch time and +88% Recall@10 improvement in online A/B tests.
- **Key Innovations**: Heterogeneous social–item interaction graph; path-based graph exploration for recommendation; LLM policy for structured graph reasoning; teacher–student hybrid inference design.
- **Link**: https://arxiv.org/abs/2608.10187v1

### 2.3 Hierarchical Residual Policy Optimization for Generative Recommendations (HRPO)

- **Authors**: [See paper]
- **Institution**: [See paper, published at KDD 2026]
- **Abstract**: Post-training framework for SID-based generative recommenders. Converts item-level outcomes into dense, token-aligned learning signals via hierarchical credit assignment. Uses Residual-Return Policy Optimization (RRPO) with clipped updates, group-normalized advantages, and KL regularization. Online A/B test in large-scale advertising system shows consistent Target Cost lifts.
- **Key Innovations**: SID prefix-level utility estimation via group-wise reward smoothing; residual token credits for layer-aware attribution; credit-to-go signals for stable optimization; deployed in production advertising.
- **Link**: https://arxiv.org/abs/2608.00750

### 2.4 SIGMA: Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress

- **Authors**: [See paper]
- **Institution**: Alibaba / AliExpress
- **Abstract**: Generative recommendation system grounding item entities in a unified latent space. Hybrid item tokenization for precise modeling and efficient generation. Large-scale multi-task SFT dataset for instruction-following recommendation. Three-step item generation with adaptive probabilistic fusion for accuracy and diversity.
- **Key Innovations**: Unified semantic-collaborative latent space; hybrid item tokenization; multi-task SFT for diverse recommendation demands; adaptive probabilistic fusion mechanism.
- **Link**: https://arxiv.org/abs/2602.22913v1

### 2.5 AgenticRec: End-to-End Tool-Integrated Policy Optimization for Ranking-Oriented Recommender Agents

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Ranking-oriented agentic recommendation framework optimizing entire decision-making trajectory (reasoning, tool invocation, ranking list generation) under sparse implicit feedback. Uses List-Wise GRPO for trajectory alignment and Progressive Preference Refinement (PPR) with hard negative mining.
- **Key Innovations**: Recommendation-specific tools in ReAct loop; list-wise GRPO for multi-step trajectory alignment; Progressive Preference Refinement with bidirectional alignment; zero extra annotations required.
- **Link**: https://arxiv.org/abs/2603.21613v1

### 2.6 Shape Your Feed (SYF): LLM-based Agentic System for Conversational Recommendation

- **Authors**: [See paper]
- **Institution**: [See paper, published at RecSys 2026]
- **Abstract**: Three-tier architecture (Perception, Serving, Self-Evolution) for real-time, multimodal co-curation of content. Uses DPO and LLM-as-a-Judge ensemble for alignment. Offline accuracy: 98.85%. Large-scale online A/B tests show improved feed relevance and user sentiment.
- **Key Innovations**: Real-time agentic re-ranking from text/voice/UI; persistent Semantic Profile; dual-feedback policy alignment (SFT + DPO from behavioral feedback).
- **Link**: https://arxiv.org/abs/2608.06632

### 2.7 GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation (JD)

- **Authors**: Yanyan Zou, Junbo Qi, Lunsong Huang, Yu Li, Kewei Xu, Jiabao Gao et al.
- **Institution**: JD.com
- **Abstract**: Generative retrieval framework deployed on JD App. Page-wise NTP for denser gradient signal; asymmetric linear Token Merger compressing multi-token SIDs (~2× input reduction); GRPO-SR (GRPO + NLL regularization) with Hybrid Rewards. Month-long A/B tests: +9.5% click count, +8.7% transaction count.
- **Key Innovations**: Page-wise NTP; asymmetric Token Merger for SID compression; GRPO-SR with dense reward model + relevance gate; validated at scale.
- **Link**: https://arxiv.org/abs/2604.14878

### 2.8 GARDRec: Decision-Level Graph Grounding for LLM Recommendation

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: [See full paper for details]
- **Link**: https://arxiv.org/abs/2608.00669

---

## 3. Advertising / CTR Prediction

### 3.1 Long-History User Transformers for Real-Time Ad Ranking (Yandex)

- **Authors**: Vyacheslav Ovchinnikov, G. G. Smirnov, Nikolai Savushkin, Veronika Ivanova, Maksim Kuzin
- **Institution**: Yandex
- **Abstract**: Decouples history encoding from real-time inference for CTR. Offline transformer encodes full cross-surface history into cached representation; lightweight runtime model combines cached rep with recent events. Pre-trained with dual objective (feedback + next-item prediction). Recovers 72–80% of full-history quality. Production A/B: +2.77% search ad ranking, +2.1% Yandex Ad Network, revenue gains +2.26% and +0.43%.
- **Key Innovations**: Offline/online architecture split; autoregressive pre-training on interaction logs; staleness-robust cached representations; no latency increase.
- **Link**: https://arxiv.org/abs/2607.14331

### 3.2 CADET: Context-Conditioned Ads CTR Prediction with Decoder-Only Transformer (LinkedIn)

- **Authors**: David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, Liuqing Li et al.
- **Institution**: LinkedIn
- **Abstract**: End-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Self-gated attention for stable training; timestamp-based RoPE for multi-scale temporal relationships; session masking for offline-online consistency; context-conditioned decoding for position modeling. Online A/B: +11.04% CTR lift over LiRank baseline.
- **Key Innovations**: Self-gated attention; timestamp RoPE (seconds to months); session-aware masking; context-conditioned multi-tower prediction heads; custom FlashAttention kernels.
- **Link**: https://arxiv.org/abs/2602.11410

### 3.3 GRAB: LLM-Inspired Sequence-First CTR Prediction at Baidu

- **Authors**: [See paper]
- **Institution**: Baidu
- **Abstract**: End-to-end generative framework for CTR with Causal Action-aware Multi-channel Attention (CamA). Captures temporal dynamics and action signals in user behavior sequences. Full-scale deployment: +3.05% revenue, +3.49% CTR. Shows monotonic, approximately linear improvement with longer sequences (scaling behavior).
- **Key Innovations**: CamA for temporal dynamics + action signals; end-to-end generative CTR; demonstrated scaling behavior with sequence length.
- **Link**: https://arxiv.org/abs/2602.01865v2

### 3.4 DS-MLP: Dual-Stream MLP is All You Need for CTR Prediction

- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution**: Renmin University, ByteDance, Meituan
- **Abstract**: Proposes Dual-Stream MLP (DS-MLP) via distillation → alignment → overall optimization. Main MLP learns from teacher models via knowledge distillation; parallel MLP captures implicit interactions. Achieves SOTA on Criteo, Avazu, and KDD benchmarks with low latency.
- **Key Innovations**: Distillation-alignment-optimization pipeline for MLP; effective high-order feature interaction learning without complex architectures; efficient inference.
- **Link**: https://arxiv.org/abs/2606.04944

### 3.5 RAMP: Robust Ad Recommendation Under Limited Personalized-Feature Availability

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Addresses privacy-constrained CTR/CVR prediction where personalized features are unavailable. Dual-tower personalized pathway + separate non-personalized pathway + distillation-inspired alignment. Improves non-personalized performance while maintaining competitive personalized performance. A/B tested in industry: TAV improved >3%.
- **Key Innovations**: Output masking for personalized/non-personalized separation; cross-pathway distillation alignment; model-agnostic architecture across backbones.
- **Link**: https://arxiv.org/abs/2607.17473v1

### 3.6 IDProxy: Cold-Start CTR Prediction at Xiaohongshu with Multimodal LLMs

- **Authors**: [See paper]
- **Institution**: Xiaohongshu
- **Abstract**: Uses multimodal LLMs to generate proxy embeddings for new items without usage data. Proxy embeddings explicitly aligned with ID embedding space and optimized end-to-end under CTR objectives. Deployed in Content Feed and Display Ads serving hundreds of millions of users daily.
- **Key Innovations**: MLLM-generated proxy embeddings; explicit alignment with ID embedding space; end-to-end CTR optimization; deployed at scale.
- **Link**: https://arxiv.org/abs/2603.01590v1

### 3.7 LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization

- **Authors**: [See paper]
- **Institution**: [Top e-commerce platform, US]
- **Abstract**: Treats LLMs as hypernetworks to generate CTR estimator parameters in a training-free manner. Few-shot CoT prompting over multimodal ad content (text + images). Outperforms cold-start baselines by 55.9% in NDCG@10. 30-day A/B test shows competitive CTR with warm-start model. Successfully deployed in production.
- **Key Innovations**: LLM as hypernetwork for weight generation; label-independent normalization and calibration; training-free cold-start ranking; production-deployed.
- **Link**: https://arxiv.org/abs/2604.12096v1

### 3.8 FEDIN: Frequency-Enhanced Deep Interest Network for CTR Prediction

- **Authors**: [See paper]
- **Institution**: [See paper, published at SIGIR 2026]
- **Abstract**: Introduces frequency-domain branch with target-aware spectrum filtering to isolate periodic interest signals. Key observation: user attention scores show distinct spectral entropy distributions for positive vs. negative items. Consistently outperforms SOTA sequential recommendation baselines on 3 public datasets.
- **Key Innovations**: Target-conditioned spectral filtering; frequency-domain user interest modeling; empirical observation of spectral entropy as positive/negative discriminator.
- **Link**: https://arxiv.org/abs/2605.01726

---

## 4. Sequential Modeling / Time Series

### 4.1 Timer-S1: Billion-Scale Time Series Foundation Model

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: 8.3B parameter MoE time series foundation model (0.75B activated per token). Introduces Serial-Token Prediction (STP) respecting serial nature of forecasting. Pre-trained on TimeBench (1 trillion time points). SOTA on GIFT-Eval (CRPS: 0.485, MASE: 0.693). Validates scaling law up to billion-scale.
- **Key Innovations**: Serial-Token Prediction (STP) with TimeSTP blocks; TimeBench corpus; post-training stage for short-term and long-context; flexible context length with single forward pass.
- **Link**: https://arxiv.org/abs/2603.04791v2

### 4.2 KReF: Training-Free Retrieval for Long-Term Time-Series Forecasting

- **Authors**: Yang Zhang et al.
- **Institution**: [See paper]
- **Abstract**: Training-free retrieval framework treating historical futures as query-local empirical predictive distributions. Embeds lookbacks via handcrafted statistics or frozen random Fourier features. Lowest CRPS in all 12 dataset-embedding settings across 6 LTSF benchmarks. Point forecasts match/surpass trained baselines on 2/6 datasets without gradients.
- **Key Innovations**: Retrieval as inductive bias for LTSF; probability-integral-transform map; zero training required; archive-oracle analysis revealing headroom.
- **Link**: https://arxiv.org/abs/2608.06748v1

### 4.3 Reverso: Efficient Time Series Foundation Models

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Small hybrid models (0.2M–2.6M params) interleave long convolutions and DeltaNet layers, matching performance of TSFMs 100× larger. Reverso-Small (550K params) outperforms Super-Linear, FlowState, and TTM-R2-Finetuned on GIFT-Eval.
- **Key Innovations**: Convolution + linear RNN hybrid; data augmentation and inference strategies; pushes performance-efficiency Pareto frontier; demonstrates large-scale transformers unnecessary for TSFMs.
- **Link**: https://arxiv.org/abs/2602.17634v1

### 4.4 TiRex-2: Recurrent xLSTM-based Multivariate Time Series Foundation Model

- **Authors**: Patrick Podest, Marco Pichler, Elias Bürger et al.
- **Institution**: [See paper]
- **Abstract**: Generalizes univariate TiRex to multivariate forecasting with past and future covariates. Memory-centric recurrent design with constant per-patch cost under streaming. Bidirectional time mixer + asymmetric grouped-attention variate mixer. SOTA zero-shot on GIFT-Eval and fev-bench.
- **Key Innovations**: Constant-cost streaming inference; bidirectional time mixer + variate mixer; future-known covariates with strict causality; synthetic coupling pipeline for multivariate pretraining.
- **Link**: https://arxiv.org/abs/2607.01204

### 4.5 UniTok: Universal Tokenizer for General-Purpose Time Series Foundation Models

- **Authors**: Yunhao Zhang, Ruiying Qi, Jiale Zheng, Jianfeng Zhang, Lujia Pan, Junchi Yan
- **Institution**: [See paper]
- **Abstract**: Vector-quantized autoencoder transforming time series into discrete tokens for NTP pretraining. UniTok-FM supports zero-shot forecasting, prompt-boosted forecasting, few-shot generation, and few-shot classification via training-free in-context inference — first TSFM to support generation and classification this way.
- **Key Innovations**: Prefix normalization; progressive-resolution causal autoencoder; structure-preserving reconstruction loss; multi-series context windows for shared dynamics.
- **Link**: https://arxiv.org/abs/2606.09861

### 4.6 TS-ICL: Time-Indexed Foundation Model via In-Context Learning

- **Authors**: Etienne Le Naour, Tahar Nabil, Adrien Petralia
- **Institution**: EDF Lab
- **Abstract**: Probabilistic encoder-regressor Transformer unifying forecasting and imputation. Operates on timestamped observations (not fixed grids), handling missing/irregular data natively. SOTA in imputation, competitive in forecasting. Strong under partially observed lookback windows.
- **Key Innovations**: Time-indexed in-context regression; DAG-based synthetic data prior for covariate integration; irregular sampling support; probabilistic predictions.
- **Link**: https://arxiv.org/abs/2606.05878

---

## 5. Game AI / Decision-Making

### 5.1 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games

- **Authors**: Chengshuai Shi, Wenzhe Li, Xinran Liang et al.
- **Institution**: [See paper]
- **Abstract**: Studies RL-based training of VLMs for long-horizon decision-making in Super Mario Land (100+ turns). Adapted PPO with lightweight turn-level critic substantially improves over critic-free methods (GRPO, Reinforce++). Pretrained VLMs provide strong action priors, 3× game progress over frontier models. Emergent generalization to in-game and cross-game settings.
- **Key Innovations**: Turn-level critic for PPO stability; VLM as action prior for sample efficiency; multi-task RL across game levels; general-domain capability preservation.
- **Link**: https://arxiv.org/abs/2605.00347

### 5.2 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Self-play framework where models learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Negotiation) against improving versions of themselves. Role-conditioned advantage estimation (RAE) stabilizes multi-agent training. Up to 10% improvement across 8 reasoning benchmarks on 4 models. Different games develop complementary cognitive patterns.
- **Key Innovations**: RAE for multi-agent RL stability; zero-sum games as reasoning curriculum; complementary cognitive skill transfer; works on base and instruction-tuned models.
- **Link**: https://arxiv.org/abs/2506.24119v3

### 5.3 CAST: Game Solvers as Turn-Level Teachers for LLM Agents

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Uses game solver state-value changes as turn-level credit signals for RLVR. Under soft-optimal solver assumption, maximizing solver advantage is equivalent to on-policy distillation without teacher logits. Outperforms all baselines on Sokoban, Minesweeper, Rush Hour; highest zero-shot on ALFWorld and WebShop.
- **Key Innovations**: Solver advantage as logit-free distillation; turn-level credit from state-value changes; negligible training overhead; works with approximate learned value networks.
- **Link**: https://arxiv.org/abs/2607.25308

### 5.4 MTG-Causal-RL: Causal Reinforcement Learning for Complex Card Games

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Gymnasium benchmark on Magic: The Gathering with 3,077-dim partial observation, 478-action masked space, 5 archetypes, and explicit Structural Causal Model. Proposes CGFA-PPO using SCM parents as factor-aligned critic targets. Exposes diagnostic structure beyond scalar win rate.
- **Key Innovations**: SCM over strategic variables; per-factor credit traces; leave-one-out cross-archetype transfer; paired-seed evaluation protocol with statistical corrections.
- **Link**: https://arxiv.org/abs/2605.06066v1

### 5.5 MEMOPILOT: Memory-Augmented Model Context Optimization for Multi-Agent LLM Games

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Plug-in memory copilot trained end-to-end via multi-turn GRPO. Turn-wise reward + turn-level advantage estimation. Evaluated on Rock–Paper–Scissors and Limit Texas Hold'em. Ranks first in Elo on both games (1762 LHE, 1590 RPS), outperforming DeepSeek V3.2.
- **Key Innovations**: Trainable memory update via multi-turn GRPO; turn-level credit assignment; persistent memory bank with structured insights; works with frozen LLMs.
- **Link**: https://arxiv.org/abs/2606.08656

### 5.6 MEMO: Memory-Augmented Model Context Optimization for Robust Multi-Turn Multi-Agent LLM Games

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Self-play framework optimizing inference-time context via retention (persistent memory bank) and exploration (tournament-style prompt evolution with TrueSkill). Raises mean win rate from 25.1% to 49.5% for GPT-4o-mini and 20.9% to 44.3% for Qwen-2.5-7B-Instruct across 5 text-based games.
- **Key Innovations**: Retention + exploration coupling; TrueSkill-based prompt evolution; prioritized replay for rare states; significant variance reduction.
- **Link**: https://arxiv.org/abs/2603.09022v2

### 5.7 Distilling Game Code World Model Generation into Lightweight LLMs

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Two-stage pipeline (SFT + RLVR with GRPO) to distill game environment generation into Qwen2.5-3B-Instruct. Hierarchical verification framework for structural and semantic game properties. 30-game dataset spanning perfect and imperfect information games.
- **Key Innovations**: Execution-based verification as RL reward; hierarchical verification for game-theoretic properties; SFT+RLVR pipeline outperforms either alone.
- **Link**: https://arxiv.org/abs/2605.24375v1

---

## 6. Diffusion Models

### 6.1 Simulation-Free and Finite-Time Diffusion Model

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Framework achieving both simulation-free training and finite-time generation simultaneously. Prescribes tractable time-dependent conditional distributions first, then constructs reference SDE realizing them. Reveals score matching emerges naturally through time reversal. Recovers conditional flow matching as small-noise limit.
- **Key Innovations**: Reversed design procedure (prescribe distributions → construct SDE); unifies score matching and CFM under one framework; Gaussian and non-Gaussian prior support.
- **Link**: https://arxiv.org/abs/2608.03117v1

### 6.2 Provably Learning Multi-Head Attention with Queries

- **Authors**: [See paper]
- **Institution**: [See paper]
- **Abstract**: Recovers canonical multi-head attention parameters from black-box input-output access. Merges heads with same W_h, sums v_h, discards zero sums — no subspace assumptions needed. 4Hd² − 2H + 1 value queries for H heads. Extends to one-layer Transformer with ReLU FFN.
- **Key Innovations**: Canonical head recovery without subspace assumptions; rational function interpolation for head separation; exact and approximate recovery guarantees.
- **Link**: https://arxiv.org/abs/2608.03294v1

---

## Summary of Key Trends

| Trend | Highlights |
|-------|-----------|
| **LLM Scaling** | Kimi K3 (2.8T MoE), LLaDA MoE v2 establish scaling laws for MoE dLLMs |
| **RL for LLMs** | Fisher-R1 (statistical reasoning), SPIRAL (self-play reasoning), CAST (solver-guided credit) |
| **Generative RecSys** | GenRec (Netflix/JD), SIGMA (AliExpress), HRPO — LLM-backed rankers entering production |
| **CTR + LLMs** | CADET (LinkedIn), GRAB (Baidu), IDProxy (Xiaohongshu), LLM-HYPER — decoder-only transformers and LLM embeddings for ad ranking |
| **Privacy-Aware Ads** | RAMP handles missing personalized features via dual-pathway distillation |
| **Time Series Foundation** | Timer-S1 (8.3B MoE), Reverso (efficient), UniTok (universal tokenizer), TiRex-2 (streaming) |
| **Game AI + RL** | Odysseus (VLM in games), SPIRAL (self-play reasoning), MEMOPILOT (memory-augmented) |
| **Diffusion LLMs** | LaCache (40× speedup), LLaDA MoE v2 scaling laws, simulation-free finite-time construction |
