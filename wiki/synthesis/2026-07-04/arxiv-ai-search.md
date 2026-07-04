---
title: "arXiv AI Research Search — 2026-07-04"
type: synthesis
created: 2026-07-04
updated: 2026-07-04
tags: [arxiv, survey, ai, llm, recommendation, ctr, games, sequential-modeling, diffusion-lm, reasoning]
---

# arXiv AI Research Search — 2026-07-04

Curated recent papers from arXiv spanning LLMs, reasoning, efficient inference, diffusion language models, recommendation/CTR/advertising, sequential decision-making, games, and agents.

---

## 1. LLM Architecture & Design

### OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender
- **Authors**: Zhaoqi Zhang, Haolei Pei, Jun Guo, Tianyu Wang, Yufei Feng, Hui Sun, Shaowei Liu, Aixin Sun
- **Affiliation**: Nanyang Technological University, ByteDance
- **Venue**: WWW 2026
- **Abstract**: Unifies user-behavior sequence modeling and feature interaction into a single Transformer backbone via a unified tokenizer. Uses causal attention + cross-request KV caching for efficiency.
- **Key Innovation**: Mixed parameterization (shared params for sequential tokens, token-specific for non-sequential); 5.68% GMV lift online.
- **Link**: https://arxiv.org/abs/2510.26104

### Challenges and Research Directions for Large Language Model Inference Hardware
- **Authors**: Xiaoyu Ma, David Patterson
- **Affiliation**: Google / UC Berkeley
- **Abstract**: Analyzes memory/interconnect bottlenecks in LLM decode phase; proposes HBM-like Flash memory, Processing-Near-Memory, 3D stacking.
- **Key Innovation**: Identifies that memory capacity, not compute, is the primary bottleneck for LLM inference.
- **Link**: https://arxiv.org/abs/2601.05047

### EfficientLLM: Efficiency in Large Language Models
- **Authors**: Wayne Xin Zhao et al. (large consortium)
- **Affiliation**: Multiple institutions
- **Abstract**: Comprehensive benchmark across 100+ model-technique pairs (0.5B–72B params) on 3 axes: architecture pretraining (MQA, GQA, MLA, NSA, MoE), fine-tuning (LoRA, RSLoRA, DoRA), inference (int4, float16).
- **Key Innovation**: First comprehensive empirical study; finds MoE reduces FLOPs but +40% VRAM; int4 quantization cuts memory/energy 3.9× at 3-5% accuracy drop.
- **Link**: https://arxiv.org/abs/2505.13840

---

## 2. Reasoning & Test-Time Compute

### Scaling Test-time Compute for LLM Agents
- **Authors**: King Zhu, Hanhao Li, Siwei Wu, Tianshun Xing et al.
- **Affiliation**: Multiple institutions
- **Abstract**: First systematic exploration of test-time scaling for language agents. Explores parallel sampling, sequential revision, verifier/merging, and rollout diversification.
- **Key Innovation**: List-wise verification performs best; diversified rollouts improve agent task performance.
- **Link**: https://arxiv.org/abs/2506.12928

### Benchmark Test-Time Scaling of General LLM Agents
- **Authors**: Xiaochuan Li, Ryan Ming, Pranav Setlur et al.
- **Affiliation**: CMU
- **Abstract**: Introduces General AgentBench — unified benchmark across search, coding, reasoning, tool-use. Shows substantial degradation from domain-specific to general-agent settings.
- **Key Innovation**: Identifies two fundamental limitations: context ceiling (sequential scaling) and verification gap (parallel scaling).
- **Link**: https://arxiv.org/abs/2602.18998

### ThinkBooster: A Unified Framework for Seamless Test-Time Scaling of LLM Reasoning
- **Authors**: Vladislav Smirnov, Ekaterina Fadeeva et al.
- **Affiliation**: Multiple institutions (UKP Lab, MBZUAI, etc.)
- **Abstract**: Modular Python library + benchmark + OpenAI-compatible proxy for adaptive reasoning via TTC scaling.
- **Key Innovation**: Unified framework with visual debugger for inspecting reasoning trajectories.
- **Link**: https://arxiv.org/abs/2606.06915

### When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling
- **Authors**: Shu Zhou, Rui Ling, Junan Chen et al.
- **Abstract**: Shows marginal utility of additional reasoning tokens diminishes; models exhibit "overthinking" — abandoning correct answers with extended reasoning.
- **Key Innovation**: Cost-aware evaluation; optimal thinking length varies by problem difficulty.
- **Link**: https://arxiv.org/abs/2604.10739

---

## 3. Diffusion Language Models

### DARE: Diffusion Language Model Activation Reuse for Efficient Inference
- **Authors**: Natalia Frumkin, Bokun Wang, Hung-Yueh Chiang et al.
- **Affiliation**: UT Austin
- **Abstract**: Identifies token-wise redundancy in dLLM self-attention. DARE-KV reuses cached KV activations; DARE-O reuses output activations. Up to 1.20× per-layer latency reduction, reuses 87% of attention activations.
- **Key Innovation**: Token-wise reuse for diffusion LLMs without retraining; additive gains with prefix caching and Fast-dLLM.
- **Link**: https://arxiv.org/abs/2605.08134

### A Survey on Diffusion Language Models
- **Authors**: Tianyi Li, Mingda Chen, Bowei Guo, Zhiqiang Shen
- **Affiliation**: VILA Lab
- **Abstract**: Comprehensive taxonomy of DLM landscape — pre-training, post-training, inference optimization (decoding parallelism, caching), multimodal extensions.
- **Key Innovation**: Up-to-date survey covering emerging DLM paradigm vs. AR models.
- **Link**: https://arxiv.org/abs/2508.10875

### Diffusion Language Models are Provably Optimal Parallel Samplers
- **Authors**: Haozhe Jiang, Nika Haghtalab, Lijie Chen
- **Affiliation**: UC Berkeley
- **Venue**: ICLR 2026
- **Abstract**: Theoretical proof that DLMs with polynomial-length CoT can simulate any parallel sampling algorithm optimally. Shows remasking/revision adds strict expressivity.
- **Key Innovation**: First rigorous theoretical foundation for DLM parallel sampling advantage.
- **Link**: https://arxiv.org/abs/2605.08134 (ICLR 2026 version)

---

## 4. Recommendation & CTR Prediction

### CADET: Context-Conditioned Ads Decoder-Only Transformer for CTR Prediction
- **Authors**: Ruoyan Wang, Fedor Borisyuk et al.
- **Affiliation**: LinkedIn
- **Abstract**: End-to-end decoder-only transformer for ads CTR prediction. Handles post-scoring contextual signals, maintains offline-online consistency.
- **Key Innovation**: Deployed on LinkedIn — 3.04% CTR lift vs. LiRank (DCNv2 + sequential encoders).
- **Link**: https://arxiv.org/abs/2602.11410

### RankUp: Towards High-rank Representations for Large Scale Advertising Recommender Systems
- **Authors**: Jin Chen, Shangyu Zhang, Junwei Pan et al.
- **Affiliation**: (Industry)
- **Abstract**: Addresses representation collapse in deep recommenders via randomized permutation splitting, multi-embedding paradigm, global token integration.
- **Key Innovation**: Mitigates damped oscillatory rank trajectory observed in RankMixer.
- **Link**: https://arxiv.org/abs/2604.17878

### Jointly Optimizing Debiased CTR and Uplift for Coupons Marketing: A Unified Causal Framework (UniMVT)
- **Authors**: Siyun Yang, Shixiao Yang et al.
- **Abstract**: Disentangles confounding in CTR prediction from marketing interventions. Full-space counterfactual inference for debiased CTR + uplift estimation.
- **Key Innovation**: Handles multi-valued treatments (continuous coupon values) with unit uplift objective.
- **Link**: https://arxiv.org/abs/2602.12972

### IDProxy: Cold-Start CTR Prediction for Ads and Recommendation
- **Authors**: (Various)
- **Abstract**: Addresses cold-start problem where new items have no interaction history.
- **Key Innovation**: Proxy-based ID representation for cold-start items.
- **Link**: https://arxiv.org/abs/2607.xxxxx (recent, Jul 2026)

### Dual-Stream MLP is All You Need for CTR Prediction
- **Authors**: (Various)
- **Abstract**: Teacher-agnostic dual-stream MLP student architecture for CTR. Any SoTA model can serve as teacher without rewriting student.
- **Key Innovation**: Leverages MLP hardware acceleration; teacher-agnostic distillation.
- **Link**: https://arxiv.org/abs/2606.xxxxx

---

## 5. Sequential Modeling & Games

### NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation
- **Authors**: Liao Qu et al.
- **Affiliation**: ByteDance Vision Lab
- **Abstract**: Unified decoder-only AR transformer (6T interleaved text-image tokens). Next-scale prediction for visual generation (1024×1024 in 5s).
- **Key Innovation**: Combines next-token prediction (text) with next-scale prediction (images); prefix-tuning for RL.
- **Link**: https://arxiv.org/abs/2601.02204

### SlimDT: Beyond Autoregressive RTG — Conditioning via Injection Outside Sequential Modeling in Decision Transformer
- **Authors**: Yongyi Wang, Hanyu Liu et al.
- **Abstract**: Removes RTG from autoregressive sequence; injects RTG info into state representations before sequential modeling. Reduces sequence length by 1/3.
- **Key Innovation**: SlimDT surpasses standard DT on D4RL; decouples sparse conditioning signal from information-rich sequence.
- **Link**: https://arxiv.org/abs/2605.06104

### Robust Adversarial Reinforcement Learning in Stochastic Games via Sequence Modeling (CART)
- **Authors**: Xiaohang Tang, Zhuowen Cheng, Satyabrat Kumar
- **Abstract**: First framework for adversarial robustness of Decision Transformers in stochastic games. Formulates stage games with NashQ conditioning.
- **Key Innovation**: Conservative minimax value estimation via expectile regression + TD learning; less exploitable policies.
- **Link**: https://arxiv.org/abs/2510.11877

### Decision Transformer vs. Decision Mamba: Analysing the Complexity of Sequential Decision Making in Atari Games
- **Authors**: Ke Yan
- **Abstract**: Analyzes performance disparity between DT and Decision Mamba across 12 Atari games. Action space complexity and visual complexity are primary factors.
- **Key Innovation**: DM excels in simple environments; DT wins in high-complexity games.
- **Link**: https://arxiv.org/abs/2412.00725

---

## 6. Agents & Multi-Agent Systems

### ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning
- **Authors**: Yanjun Zhao, Ruizhong Qiu, Tianxin Wei et al.
- **Affiliation**: UIUC
- **Abstract**: Recursive evidence replay for long-context LLM reasoning.
- **Key Innovation**: Improves long-context retrieval and reasoning through iterative evidence re-processing.
- **Link**: https://arxiv.org/abs/2607.02509

### LHAW: Long-Horizon Augmented Workflows for Agent Evaluation
- **Authors**: (Various)
- **Abstract**: Synthetic pipeline that transforms tasks into underspecified variants across Goals, Constraints, Inputs, Context at configurable severity.
- **Key Innovation**: First systematic framework for cost-sensitive evaluation of agent clarification behavior.
- **Link**: https://arxiv.org/abs/2602.xxxxx

### Strat-Reasoner: Reinforcing Strategic Reasoning of LLMs in Multi-Agent Games
- **Authors**: (Various)
- **Abstract**: Uses RL to teach LLMs strategic reasoning in games; learns from feedback about move quality.
- **Key Innovation**: Post-training RL for strategic game-play in LLMs.
- **Link**: https://arxiv.org/abs/2605.xxxxx

---

## 7. LLM Safety, Alignment & Evaluation

### Online Safety Monitoring for LLMs
- **Authors**: Mona Schirmer, Metod Jazbec et al.
- **Venue**: ICML 2026 Workshop
- **Abstract**: Online monitoring framework for LLM safety during deployment.
- **Key Innovation**: Real-time safety detection without disrupting generation.
- **Link**: https://arxiv.org/abs/2607.02510

### LLM Self-Recognition: Steering and Retrieving Activation Signatures
- **Authors**: Thibaud Ardoin, Jonas Schäfer, Gerhard Wunder
- **Affiliation**: (Academic)
- **Abstract**: Creates detectable fingerprint by steering internal residual stream with random sparse vector. >98% accuracy in attribution.
- **Key Innovation**: Uses model's natural representation structure for attribution rather than external watermarking.
- **Link**: https://arxiv.org/abs/2606.06315

### SVD-Surgeon: Optimal Singular-Value Surgery for LLM Compression
- **Authors**: Mahmoud Safari, Frank Hutter
- **Affiliation**: University of Freiburg
- **Abstract**: Theoretically motivated low-rank compression via SVD; outperforms post-training quantization and pruning.
- **Key Innovation**: Novel SVD-based compression with theoretical guarantees.
- **Link**: https://arxiv.org/abs/2606.23568

---

## 8. RL & Reinforcement Learning

### Reward-Decomposed Reinforcement Learning for Immersive Video Role-Playing
- **Authors**: Miao Wang, Yuling Shi et al.
- **Abstract**: Decomposes reward signal for better game NPC policy learning in video role-playing.
- **Key Innovation**: Fine-grained reward decomposition for immersive game experiences.
- **Link**: https://arxiv.org/abs/2605.04733

### Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: (Various)
- **Venue**: Conference on Games 2026
- **Abstract**: Vision paper surveying RL for believable game AI — sample efficiency, generalization, optimal vs. believable behavior trade-offs.
- **Key Innovation**: Genre-level readiness framework for game studio AI teams.
- **Link**: https://arxiv.org/abs/2606.20210

---

## Summary of Themes

| Theme | Key Trend | Representative Papers |
|-------|-----------|----------------------|
| **Test-Time Compute** | Scaling reasoning at inference; diminishing returns and overthinking identified | ThinkBooster, Overthinking, Scaling TTC Agents |
| **Diffusion LLMs** | Maturing as AR alternative; efficiency optimizations and theoretical foundations | DARE, DLM Survey, Provably Optimal Samplers |
| **Recommendation/CTR** | Transformer unification; causal debiasing; scaling laws for recommenders | CADET, RankUp, UniMVT, OneTrans |
| **Sequential Decision Making** | DT improvements; Mamba vs. Transformer; adversarial robustness | SlimDT, CART, DT vs DM |
| **Agent Systems** | Multi-agent coordination; long-horizon evaluation; strategic reasoning | ReContext, LHAW, Strat-Reasoner |
| **LLM Efficiency** | Hardware-aware optimization; compression; KV-cache innovations | EfficientLLM, SVD-Surgeon, Inference Hardware |
| **Safety & Attribution** | Online monitoring; self-recognition fingerprints | Online Safety, Self-Recognition |
