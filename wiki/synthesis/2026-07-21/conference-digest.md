---
title: "Conference & arXiv Digest — 2026-07-21"
type: synthesis
created: 2026-07-21
updated: 2026-07-21
sources: [arxiv, proceedings]
tags: [conference-digest, icml, iclr, aaai, neurips, kdd, cvpr, acl, emnlp, sigir, www, cikm, recsys, llm, recommendation, ctr, agents, generative-models, code-execution, benchmark]
---

# Conference & arXiv Digest — 2026-07-21

> Curated digest of recent papers from top ML/AI conferences and arXiv. Structured by venue/category.

---

## 1. ICLR 2026 (Rio de Janeiro, Apr 23–27)

**Stats**: 19,525 submissions → 5,355 accepted (27.4%) → 225 Oral

### 1.1 LLM Reasoning & Alignment

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **TROLL: Trust Regions Improve RL for LLMs** | — | — | Replaces PPO clip with discrete differentiable trust region projection; token-level KL constraints on sparse important logits. Consistently outperforms PPO clipping in training speed, stability, and success rates across math reasoning and code generation. |
| 2 | **Why DPO is a Misspecified Estimator and How to Fix It** | — | — | Exposes fundamental statistical flaw in DPO; proposes corrected estimator. |
| 3 | **SafeDPO: Safe Direct Preference Optimization** | — | — | Constrained alternative balancing helpfulness and safety. |
| 4 | **In-The-Flow Agentic System Optimization for Effective Planning and Tool Use** | — | — | Agentic system optimization for planning and tool use. |
| 5 | **MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent** | — | — | Multi-convolution RL memory agent for long-context LLMs. |
| 6 | **Verifying Chain-of-Thought Reasoning via its Computational Graph** | — | — | Verification of CoT reasoning through computational graph analysis. |
| 7 | **P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling** | — | — | Personalized reward model scaling at test-time per user. |
| 8 | **EigenBench: A Comparative Behavioral Measure of Value Alignment** | — | — | Behavioral benchmark for value alignment measurement. |

### 1.2 Agent Systems & Tool Use

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **ToolTree: Efficient LLM Agent Tool Planning via Dual-Feedback MCTS** | Shuo Yang et al. | — | MCTS-based planning with pre-execution scoring + post-execution utility. ~10% improvement over SOTA on GTA (66.95 F1) and ToolBench (69.04 pass rate). |
| 2 | **MedAgentGym: Scalable Agentic Training for Biomedical Data Science** | — | — | Scalable agentic training environment for code-centric biomedical reasoning. |
| 3 | **Optimistic Task Inference for Behavior Foundation Models** | — | — | Task inference for behavior foundation models. |

### 1.3 Sequence Modeling & Architecture

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **Mamba-3: Improved Sequence Modeling using State Space Principles** | — | — | Improved SSM architecture for sequence modeling. |
| 2 | **Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Resource** | — | — | MoE surpassing dense models under equal compute. |
| 3 | **TileLang: Bridge Programmability and Performance in Modern Neural Kernels** | — | — | Programmable high-performance neural kernel language. |

### 1.4 Safety & Alignment

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **AlphaAlign** | — | — | Incentivizes explicit safety reasoning via RL with verifiable rewards; deep safety alignment vs shallow token-level alignment. |
| 2 | **WaltzRL** | Meta FAIR + Johns Hopkins | — | Multi-agent RL safety: conversation agent + feedback agent; reduces unsafe responses from 39% to 4.6% on WildJailbreak, overrefusals from 45.3% to 9.9% on OR-Bench. |
| 3 | **Benchmarking Empirical Privacy Protection for LLM Adaptations** | — | — | Privacy protection benchmark for LLM adaptations. |

### 1.5 Robotics & Embodied AI

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **Mean Flow Policy with Instantaneous Velocity Constraint** | — | — | Generative policy for one-step action generation; SOTA on Robomimic and OGBench. |
| 2 | **Emergent Dexterity via Diverse Resets** | — | — | Scalable dexterous manipulation via simulator resets; single reward function. |

---

## 2. AAAI 2026 (Jan 20–27)

**Stats**: ~29,000 submissions → 4,300+ accepted

### 2.1 LLM Reasoning & Hallucination

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **Mitigating Hallucinations in LLMs via Causal Reasoning** | Li, Shen, Nian et al. | — | CDCR-SFT: constructs variable-level DAG then reasons over it. 95.33% accuracy on CLADDER (surpassing human 94.8%), 10% hallucination reduction on HaluEval. 25,368 sample dataset CausalDR. |
| 2 | **In-Token Rationality Optimization (InTRO)** | Zhu, Liu, Fu et al. | — | Token-level exploration with self-feedback for accurate and concise reasoning. Up to 20% relative improvement on 6 math benchmarks; cross-domain transfer. |
| 3 | **MetaAct-RL: Meta-Action-Based RL for LM Reasoning** | — | — | Frames LMs' thinking as sequential decision making over meta-actions. |
| 4 | **LENS: Learning to Segment Anything with Unified Reinforced Reasoning** | Lianghui Zhu et al. (includes Xinggang Wang, Huazhong UST) | — | Scalable RL framework jointly optimizing CoT reasoning and segmentation end-to-end. |

### 2.2 Multimodal & Vision-Language

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **MME-SCI: Benchmarking Scientific Reasoning for MLLMs** | — | — | Multilingual + multimodal scientific reasoning benchmark. |
| 2 | **Mechanistic Dissection of Cross-Attention Subspaces in Text-to-Image Diffusion** | — | — | Mechanistic interpretability of cross-attention in diffusion models. |

### 2.3 Federated Learning & Privacy

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **FedGRPO: Privately Optimizing Foundation Models with Group-Relative Rewards** | — | — | Federated learning with group-relative rewards from domain clients. |

---

## 3. NeurIPS 2025 (San Diego, Dec 2–7)

**Stats**: 21,575 submissions → 5,275 accepted (24.5%) → 77 Oral, 683 Spotlight

### 3.1 Best Papers

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **Gated Attention for LLMs: Non-linearity, Sparsity, and Attention-Sink-Free** 🏆 | Zihan Qiu, Zekun Wang, Bo Zheng et al. | Alibaba (Qwen team) | Simple head-specific sigmoid gate after SDPA consistently improves performance. Tested on 15B MoE and 1.7B dense, 3.5T tokens. Enhances stability, tolerates larger learning rates, mitigates attention sink. |
| 2 | **1000 Layer Networks for Self-Supervised RL** 🏆 | Kevin Wang et al. | — | Depth up to 1024 layers boosts self-supervised RL 2×–50×; qualitatively changes behaviors. |
| 3 | **Why Diffusion Models Don't Memorize** 🏆 | — | — | Implicit dynamical regularization in training prevents memorization. |
| 4 | **Artificial Hivemind: Open-Ended Homogeneity of Language Models** 🏆 (DB track) | Liwei Jiang et al. | — | First systematic study of LLM mode collapse in open-ended generation; "hivemind" effect. |

### 3.2 Runner-Ups

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?** | Yang Yue et al. | — | RLVR does NOT produce fundamentally new reasoning; mainly amplifies existing correct behaviors. pass@k at large k shows base models match RL-trained models. |
| 2 | **Superposition Yields Robust Neural Scaling** | Yizhou Liu et al. | — | Strong superposition → loss scales inversely with model dimension. Confirms open-source LLMs operate in strong superposition regime. |

### 3.3 Other Notable

| # | Title | Affiliation | Key Innovation |
|---|-------|-------------|----------------|
| 1 | **Faster R-CNN** (Test-of-Time Award, 2015 paper) | MSRA (Kaiming He) | 56,700+ citations; region proposal networks. |
| 2 | **Learning Linear Attention in Polynomial Time** | MIT | Optimal multi-head linear attention via RKHS kernel predictor. |

---

## 4. ICML 2026 (Seoul, Jul 6–11)

**Stats**: 23,918 submissions → 6,352 accepted (26.6%) → 536 Spotlight

### 4.1 Reinforcement Learning

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **Maximum Likelihood Reinforcement Learning (MaxRL)** | — | — | Compute-indexed family of sampling-based objectives interpolating between RL and exact maximum likelihood. Unbiased policy-gradient estimator; consistently outperforms GRPO on pass@1 and pass@k. |
| 2 | **High-accuracy Sampling for Diffusion Models** | — | — | δ-error in polylog(1/δ) steps with O(δ)-accurate score estimates. Exponential improvement over prior results. |

### 4.2 Theory

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **To Grok Grokking: Provable Grokking in Ridge Regression** | — | — | First rigorous quantitative bounds on "grokking time" in terms of hyperparameters. Shows grokking is a consequence of training conditions, not inherent failure mode. |

---

## 5. CVPR 2026 (New York, Jun 5–7)

**Stats**: 16,092 submissions → 4,089 accepted

### 5.1 Best Papers

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **Efficiently Reconstructing Dynamic Scenes One D4RT at a Time** 🏆 | Chuhan Zhang et al. | Google DeepMind + UCL + Oxford | Unified transformer estimating depth, spatio-temporal correspondence, full camera params for 4D scene reconstruction. Lightweight and scalable. |
| 2 | **Native and Compact Structured Latents for 3D Generation** 🏆 | Jianfeng Xiang et al. | Tsinghua + Microsoft Research + USTC + Microsoft AI | O-Voxel representation for 3D generative modeling; far exceeds existing models in geometry/quality. |
| 3 | **SAM 3D: 3Dfy Anything in Images** 🏆 | Jianing Yang et al. | Meta FAIR | Generative model for 3D reconstruction from single image; 5:1 win rate in human preference. |

### 5.2 Vision-Language Models

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **Molmo2: Open Weights and Data for VLMs with Video Understanding** 🏆 | Christopher Clark et al. | AI2 | Open-weight VLM with video understanding and grounding. |
| 2 | **TUNA: Taming Unified Visual Representations for Native UMMs** | Zhiheng Liu et al. | — | Unified continuous visual representation via VAE encoder + representation encoder; SOTA in understanding, generation, and editing. |

### 5.3 Generative Models

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **Back to Basics: Let Denoising Generative Models Denoise** | Tianhong Li, Kaiming He | MIT | Return to fundamental denoising principles. |
| 2 | **MacTok: Robust Continuous Tokenization for Image Generation** 🏆 | Hengyu Zeng et al. | — | Continuous tokenization for image generation. |
| 3 | **A Frame is Worth One Token: Efficient Generative World Modeling** 🏆 | Tommie Kerssies et al. | — | Delta tokens for efficient world modeling. |

### 5.4 Apple at CVPR 2026

Notable Apple papers: AMUSE (audio-visual multi-speaker), AToken (unified tokenizer), STARFlow-V (video generative modeling), UniGen-1.5 (image generation/editing via RL reward unification), Velox (4D geometry/appearance).

---

## 6. KDD 2026 (Jeju Island, Aug 9–13)

### 6.1 CTR Prediction & Recommendation

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **CTR-Sink: Attention Sink for Language Models in CTR Prediction** | Zixuan Li et al. | HKU + Ant Group | Behavior-level attention sinks between consecutive behaviors with recommendation signals (temporal distance, semantic similarity). 0.2–0.5% AUC improvement on MovieLens, KuaiRec across RoBERTa and Qwen. Code: github.com/UGUESS-lzx/CTR-SINK |
| 2 | **Field-Aware Transformer (FAT) for CTR Prediction** | — | — | Field-centric parameters + Basis-Composed Hypernetwork. +4.38% AUC improvement, +2.33% CTR, +0.66% RPM in live production. Theoretical scaling law via Rademacher complexity. |
| 3 | **Dual-Stream MLP (DS-MLP) is All You Need for CTR Prediction** | Kesha Ou et al. | Renmin U + ByteDance + Meituan | Knowledge distillation consolidating explicit interactions into main MLP; vanilla MLP achieves SOTA on Criteo, Avazu, MovieLens. |
| 4 | **LLM-as-a-Judge for Reliable Offline Evaluation in Top-K Recommendation** | Yue Que et al. | — | LLM Judge using semantic proxy for user preferences; 85.70% NDCG correlation with unbiased test sets. |
| 5 | **A/B Agent: Multi-Modal LLM Agent for A/B Testing** | — | CityU + — | Recommendation sandbox environment for simulated A/B testing with multimodal user agents. |

### 6.2 LLM Agents

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **HTAA: Hybrid Toolset Agentization & Adaptation** | Chengrui Huang et al. | — | Hierarchical framework grouping co-used tools into agent tools; reduces manual validation effort by 84.5% in production (ride-hailing platform). |
| 2 | **INTENT: Budget-Constrained Agentic LLMs** | Hanbing Liu et al. | — | Intention-aware hierarchical world model for budget-constrained tool use; robust to price changes and budget scaling. |

---

## 7. ACL 2026 (San Diego, Jul 2–7)

**Stats**: 12,148 submissions → 2,296 main accepted (18.9%) → 2,163 Findings. Theme: Interpretability of NLP Models.

### 7.1 Key Trends

- **LLM Reasoning, Agents, Tool Use**: 366 papers (up from 142 in 2025, +224/+8.2pp) — biggest growth area
- **Model Training, Fine-tuning, Alignment, RL**: 295 papers (+99)
- **RAG, QA, Knowledge Editing**: 244 papers (+70)
- **Safety, Privacy, Robustness**: 125 papers
- **Multimodal**: 116 papers

### 7.2 Notable Papers

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **Deliberative Searcher: Improving LLM Reliability via RL with Constraints** | Zhenyun Yin et al. | — | Reduces false-certain rates by 96% (54%→2%) on search-augmented tasks; constrained policy optimization for calibrated confidence. |
| 2 | **MemSearch-o1: Reasoning-Aligned Memory Growth in Agentic Search** | — | — | Agent-based memory search with reasoning-aligned growth. |
| 3 | **ReasonEmbed: Enhanced Text Embeddings for Reasoning-Intensive Retrieval** | — | — | Embeddings optimized for reasoning-intensive document retrieval. |

---

## 8. EMNLP 2025 (Suzhou, Nov 4–9)

**Stats**: 1,810 main papers + 1,406 Findings + 194 Industry

### 8.1 Notable Papers

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **LLMsPark: Benchmarking LLMs in Strategic Gaming Contexts** | Junhao et al. | — | Benchmark for evaluating LLMs in strategic game playing. |
| 2 | **DivLogicEval: Benchmarking Logical Reasoning in LLMs** | Tsz Ting Chung et al. | — | Framework for benchmarking logical reasoning evaluation. |

---

## 9. WWW 2026 (Dubai, Apr 13–17)

### 9.1 Recommendation & CTR

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **ThinkRec: Thinking-based Recommendation via LLM** | Keqin Bao et al. | — | Shifts LLM4Rec from System 1 to System 2; thinking activation with synthetic reasoning traces + instance-wise expert fusion. Significant improvements in accuracy and interpretability. |
| 2 | **GenCI: Generative Modeling of User Interest Shift for CTR Prediction** | — | — | Generative user intent framework with semantic interest cohorts; next-item prediction for candidate interest generation. |
| 3 | **Enhancing Generative Auto-bidding with Offline Reward Evaluation** | — | — | Oral at ICLR 2026; auto-bidding via offline RL. |

---

## 10. SIGIR 2026 (Melbourne, Jul 20–24)

### 10.1 Generative Recommendation

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **MVIGER: Multi-View Variational Integration for Generative Recommender** | Tongyoung Kim et al. | Yonsei U | Probabilistic framework with learned prior estimating view-level contribution as latent variable. T5-small outperforms Llama 7B-based models (LC-Rec, EAGER-LLM). |
| 2 | **SIGMA: Semantic-Grounded Instruction-Driven Generative Multi-Task Recommender at AliExpress** | — | Alibaba | Semantic-grounded instruction-driven generative recommendation for multi-task settings. |

---

## 11. RecSys 2025 (RecSys 2026 in Minneapolis)

### 11.1 Notable Papers

| # | Title | Authors | Affiliation | Key Innovation |
|---|-------|---------|-------------|----------------|
| 1 | **Beyond Immediate Click: Engagement-Aware MoE-Enhanced Transformers for Sequential Movie Recommendation** | Haotian Jiang et al. | Amazon Prime Video | MoE-enhanced transformer for engagement-aware sequential recommendation. |
| 2 | **Enhancing Online Video Recommendation via Coarse-to-Fine Uplift Modeling** | — | Kuaishou | Coarse-to-fine uplift modeling for video recommendation. |
| 3 | **Enhancing Sequential Recommender with LLMs for Joint Video and Comment Recommendation** | Bowen Zheng et al. | Renmin U + Kuaishou | LLM-enhanced sequential recommendation for joint video-comment recommendation. |
| 4 | **Heterogeneous User Modeling for LLM-based Recommendation** | Honghui Bao et al. | NUS + USTC + NUS | Heterogeneous user modeling for LLM-based recommendation. |
| 5 | **RECAP: GRPO Reward Streaming Profiles for RecSys** | — | Kuaishou | GRPO-based reward streaming for recommendation systems. |

---

## 12. Agent Systems & Tool Use (Cross-Venue)

| # | Title | Venue/Source | Key Innovation |
|---|-------|-------------|----------------|
| 1 | **The Evolution of Tool Use in LLM Agents** | arXiv survey (2026) | Comprehensive review: single-call → multi-tool orchestration; six core dimensions. |
| 2 | **Demystifying RL for Long-Horizon Tool-Using Agents (STAR)** | arXiv (2026) | Systematic RL recipe: reward/model scaling/data/algorithm/environment stability. ~1K balanced samples optimal; scale-dependent reward choices. |
| 3 | **ParaManager: Small Model as Master Orchestrator** | arXiv (2026) | Agent-as-Tool unified paradigm; lightweight orchestrator with parallel subtask decomposition; 70.48 avg across benchmarks. |

---

## 13. Code Execution Prediction & Program Synthesis (Cross-Venue)

| # | Title | Venue/Source | Key Innovation |
|---|-------|-------------|----------------|
| 1 | **ProgramBench: Can Language Models Rebuild Programs From Scratch?** | arXiv (2026) | 200 tasks from CLI tools to FFmpeg/SQLite/PHP; best model passes 95% tests on only 3% of tasks. Models favor monolithic single-file implementations. |
| 2 | **CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation** | arXiv (2026) | Specification generation harder than code generation; best repo-level pass rate only 20.2% (Claude-4.5-Sonnet). 15 LLMs evaluated. |
| 3 | **MirrorCode: AI Rebuilds Entire Programs from Behavior Alone** | Epoch Research (2026) | 25 target programs across 6 languages; Claude Opus 4.7 scores 56%. Single attempt can cost $2,600 over 19 days. |
| 4 | **ExecVerify: White-Box RL with Verifiable Stepwise Rewards** | arXiv (2026) | RL with execution-trace rewards (next-statement, variable value/type prediction). 7B model matches 32B models on reasoning; +5.9% pass@1 on code generation. |
| 5 | **Self-Execution Simulation Improves Coding Models** | arXiv (2026) | Trains LLMs to simulate program execution step-by-step; self-verification and iterative self-fix via predicted execution feedback. |
| 6 | **DryRUN: You Don't Need Public Tests** | arXiv (2026) | LLM autonomously synthesizes inputs and simulates execution; matches CodeSIM without any public tests or external execution. |
| 7 | **EvoCodeBench: Human-Performance Benchmark for Self-Evolving Coding** | arXiv (2026) | Tracks self-evolution dynamics; 10–27% relative improvement from within-inference refinement. |

---

## 14. Games & Game AI (Cross-Venue)

Referenced from [[wiki/synthesis/2026-07-18/game-rl-daily]]:

| # | Title | Venue/Source | Key Innovation |
|---|-------|-------------|----------------|
| 1 | **NitroGen** | CVPR 2026 (NVIDIA) | 40K hours training on 1000+ games for game-playing foundation model. |
| 2 | **MARL-GPT** | arXiv (2026) | Unified transformer for multi-agent RL across games. |
| 3 | **Stratagem** | arXiv (2026) | Transferable reasoning from self-play to new games. |
| 4 | **Sensi** | arXiv (2026) | 50–94× sample efficiency on ARC-AGI-3. |

---

## 15. Generative Models & Diffusion (Cross-Venue)

| # | Title | Venue/Source | Key Innovation |
|---|-------|-------------|----------------|
| 1 | **Why Diffusion Models Don't Memorize** | NeurIPS 2025 🏆 | Implicit dynamical regularization prevents memorization. |
| 2 | **High-accuracy Sampling for Diffusion Models** | ICML 2026 | Polylog(1/δ) step sampler; exponential improvement. |
| 3 | **Back to Basics: Let Denoising Generative Models Denoise** | CVPR 2026 (Kaiming He) | Return to fundamental denoising principles. |
| 4 | **MacTok: Robust Continuous Tokenization for Image Generation** | CVPR 2026 🏆 | Continuous tokenization for generation. |
| 5 | **TUNA: Unified Visual Representations for Native UMMs** | CVPR 2026 | Unified continuous visual space for understanding + generation. |

---

## Key Themes Across Conferences

1. **Agentic AI is the dominant paradigm**: Tool planning (ToolTree, HTAA, INTENT), multi-agent orchestration (ParaManager), and budget-aware agents dominate ICLR, KDD, ACL.
2. **RL for LLM training mature but limited**: NeurIPS runner-up shows RLVR doesn't produce new reasoning; ICML's MaxRL and TROLL propose better RL objectives.
3. **Safety alignment going deep**: WaltzRL (multi-agent), AlphaAlign (explicit reasoning) at ICLR; 70%+ of RL/alignment submissions involve LLMs.
4. **CTR prediction: LLM meets field-aware design**: CTR-Sink (attention sinks), FAT (field-aware transformer) at KDD; DS-MLP simplifies to vanilla MLP.
5. **Code generation: execution simulation emerging**: ExecVerify, Self-Execution, DryRUN show LLMs can simulate execution for self-verification.
6. **Generative recommendation maturing**: MVIGER (variational multi-view), SIGMA (AliExpress), ThinkRec (System 2 reasoning) at SIGIR/RecSys/WWW.
7. **3D vision breakthroughs at CVPR**: D4RT (Google DeepMind), O-Voxel (Microsoft), SAM 3D (Meta) — best papers.
8. **Gated attention becomes mainstream**: NeurIPS best paper (Alibaba Qwen); likely to be widely adopted.

---

## Source Links

- ICLR 2026: https://iclr.cc/virtual/2026/papers.html
- AAAI 2026: https://aaai.org/proceeding/aaai-40-2026/
- NeurIPS 2025: https://neurips.cc/virtual/2025/papers.html
- ICML 2026: https://icml.cc/virtual/2026/papers.html
- CVPR 2026: https://cvpr.thecvf.com/
- KDD 2026: https://kdd2026.kdd.org/
- ACL 2026: https://2026.aclweb.org/
- EMNLP 2025: https://2025.emnlp.org/
- SIGIR 2026: https://sigir2026.org/
- WWW 2026: https://www2026.acm.org/
- RecSys 2025: https://recsys.acm.org/recsys25/
