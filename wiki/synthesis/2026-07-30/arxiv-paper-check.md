---
title: "arXiv Paper Check — AI & CTR (July 30, 2026)"
type: synthesis
created: 2026-07-30
updated: 2026-07-30
tags: [arxiv, ai, ctr, recommendation, agents, reasoning, rl, llm]
sources: []
---

# arXiv Paper Check — AI & CTR (July 30, 2026)

Covering papers submitted Jul 29–30, 2026 across cs.LG, cs.IR, and cs.AI.

---

## Reinforcement Learning & LLM Post-Training

### 1. Do You Really Need to Pretrain Q-Functions for Online RL Fine-Tuning?
- **Authors**: Perry Dong, Ron Polonsky, Dorsa Sadigh, Chelsea Finn
- **Key Contribution**: Systematically shows naive Q-function pretraining provides little benefit over random initialization when fine-tuning on top of a pretrained policy. Identifies a fundamental mismatch: the pretrained Q targets the pretrained policy's Q, not the converged Q of online fine-tuning. Proposes **IPE (Initialization via Policy Ensemble)** — trains multiple diverse policies and uses pooled rollouts to bootstrap Q-function learning, yielding **1.26x average improvement** over naive Q-pretraining on continuous control.
- **Link**: https://arxiv.org/abs/2607.27203

### 2. ReCo: Reweighting GRPO Against Distributional Concentration
- **Authors**: Junoh Park, Junseo Hwang, Wonguk Cho, Taesup Kim
- **Key Contribution**: Identifies that GRPO concentrates on responses the base model already generates with high probability, reducing coverage (Pass@k). Traces this to two mechanisms: response-level (high-prob responses dominate through repeated occurrence) and token-level (importance ratio gradients reinforce likely tokens). Proposes **ReCo** which normalizes response contributions by expected occurrence and replaces token-level importance ratio with a variance-based ratio. Improves Pass@k on Qwen2.5-Math/Llama-3.1-8B across 5 math reasoning benchmarks.
- **Link**: https://arxiv.org/abs/2607.26862

### 3. SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution
- **Authors**: Zhiyuan Yao et al. (15 authors)
- **Key Contribution**: Unified RL framework that organizes related tasks into progressive sequences, using a single policy to alternate between task solving and curating an evolving skill document. Decoupled credit assignment supervises solving with current reward and curation with discounted downstream outcomes. Outperforms baselines by **2.3–8.5pp** on ALFWorld, WebShop, ScienceWorld. Shows test-time scaling: longer task sequences improve performance even with single attempts per task.
- **Link**: https://arxiv.org/abs/2607.26784

### 4. Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM Agents
- **Authors**: Yicheng Feng, Yan Zhang, Yan Cheng, Wei Qi
- **Key Contribution**: Proposes cost-aware stopping criteria for LLM agents acquiring tools during task execution. Addresses the gap between confidence scores and optimal stopping decisions.
- **Link**: https://arxiv.org/abs/2607.27083

### 5. Two Calls Beat Five Agents: Evaluating Multi-Agent Pipelines Against Self-Refinement for Local LMs
- **Authors**: Ashish Prajapati, Om Mohite
- **Key Contribution**: Surprisingly finds that a single LLM with 2 calls (initial + self-refinement) outperforms multi-agent pipelines with 5 agents when using local language models. Challenges the assumption that multi-agent architectures are always beneficial for small models.
- **Link**: https://arxiv.org/abs/2607.26922

---

## Recommendation Systems & CTR

### 6. WhisperRec: Latent Reasoning for Efficient Foundation Recommendation Models
- **Authors**: Hao Jiang et al. (12 authors; Kuaishou)
- **Key Contribution**: Proposes **latent reasoning tokens** that compress teacher-generated Chain-of-Thought into learnable latent representations, enabling reasoning without verbose rationale generation. Introduces Multi-View Adaptive CoT (MV-ACoT) for diverse supervision and three-stage Latent Reasoning Alignment. Improves SID@64 by 17.44% over explicit CoT methods and achieves **>10x online inference throughput**. Industrial-scale Kuaishou dataset.
- **Link**: https://arxiv.org/abs/2607.26621

### 7. Beyond Action Imitation: Learning a Decision-Aware User Simulator for Online Advertising (DASH)
- **Authors**: Zipeng Chen et al. (17 authors; Tencent)
- **Key Contribution**: Proposes a decision-aware user simulator that jointly generates thinking traces and predicts behavioral actions from heterogeneous cross-domain histories. Uses a rubric-based reward model evaluating thinking traces along form, content, and logic. Evaluated on real-world Tencent advertising data across 5 domains.
- **Link**: https://arxiv.org/abs/2607.26893

### 8. TWICE: Two-Clock, Two-Window Learning for Long-Horizon Conversion Prediction in Online Advertising
- **Authors**: Kaiyuan Li, Kun Wang, Zhongbo Wang, Teng Sha, Ming Yan, Yanhua Cheng, Xialong Liu (Kwai)
- **Key Contribution**: Factorizes long-horizon CVR into target-window conversion probability + grouped elapsed-delay CDF, using separate click-clock and conversion-clock supervision. Deployed at Kwai with **+2.486% revenue**, **+1.858% revenue**, **+2.061% conversions** in online A/B test. Single learned CDF produces monotone predictions for all horizons up to target window.
- **Link**: https://arxiv.org/abs/2607.25404

### 9. Kairos: Numerically Robust News Recommendation under Item Cold-Start via Cholesky-based LinUCB
- **Authors**: Finn Hertsch
- **Key Contribution**: Cholesky decomposition-based LinUCB for numerically stable cold-start news recommendation. Addresses numerical instability in standard LinUCB for high-dimensional news features.
- **Link**: https://arxiv.org/abs/2607.26832

### 10. Learning from the Future: Privileged Self-Distillation for Sequential Recommendation
- **Authors**: Jiakai Tang, Yang Zhang, See-Kiong Ng, Xu Chen, Wen Chen, Jian Wu, Han Zhu
- **Key Contribution**: Uses future item information as privileged knowledge during training, distilled into the model via self-distillation for sequential recommendation. No privileged info needed at inference time.
- **Link**: https://arxiv.org/abs/2607.27055

### 11. IMFuse: Instance-Aware Multi-Layer Fusion for LLM-Enhanced Sequential Recommendation
- **Authors**: Yuheng Zheng et al. (Zhejiang University)
- **Key Contribution**: Instance-aware multi-layer fusion framework combining LLM representations with traditional sequential recommendation models. 12 pages, evaluated on multiple benchmarks.
- **Link**: https://arxiv.org/abs/2607.27002

### 12. Improving Item Discoverability in e-Commerce Search via Related Intent Generation
- **Authors**: Ji Xin et al. (Accepted to KDD 2026 TSMO)
- **Key Contribution**: Generates related search intents to improve item discoverability in e-commerce search. Practical approach for expanding user intent coverage.
- **Link**: https://arxiv.org/abs/2607.27172

### 13. CaIRec: Calibrated Modality Imputation for Incomplete Multimodal Recommendation
- **Authors**: Ruiyu Liu et al.
- **Key Contribution**: Handles missing modalities in multimodal recommendation via calibrated imputation. Addresses the practical challenge of incomplete modality data.
- **Link**: https://arxiv.org/abs/2607.26720

### 14. Multi-Decoder OneRec: Controllable Generative Retrieval for Multi-Objective Industrial Recommendation
- **Authors**: You Wang et al. (Huawei)
- **Key Contribution**: Multi-decoder architecture for controllable generative retrieval supporting multiple objectives in industrial recommendation. 9 pages, 11 tables.
- **Link**: https://arxiv.org/abs/2607.26500

---

## LLM Efficiency & Systems

### 15. From Tokens to Watt-hours: Analytical Energy Estimation for LLM Inference on Modern GPUs
- **Authors**: Tina Vartziotis et al. (Accepted ECML-PKDD 2026 GREEN-AI)
- **Key Contribution**: Provides an analytical model for estimating LLM inference energy consumption on modern GPUs. Enables energy-aware deployment decisions.
- **Link**: https://arxiv.org/abs/2607.26571

### 16. Budget-Aware LLM Discovery via Cost-Calibrated Frontier Utility
- **Authors**: Yansen Zhang et al.
- **Key Contribution**: Framework for selecting optimal LLMs under budget constraints using cost-calibrated frontier utility analysis. Practical for cost-sensitive deployment scenarios.
- **Link**: https://arxiv.org/abs/2607.26828

---

## Reasoning & Uncertainty

### 17. Thinking Under Uncertainty: Evidence Use and Information-Seeking in Language Models
- **Authors**: Hua-Dong Xiong et al.
- **Key Contribution**: Studies how LLMs use evidence and seek information under uncertainty. Analyzes evidence integration strategies and information-seeking behavior during reasoning under varying uncertainty levels.
- **Link**: https://arxiv.org/abs/2607.26845

### 18. Uncertainty-Guided LLM Semantic Augmentation for Heterogeneous Treatment Effect Estimation
- **Authors**: Jialu Xu et al.
- **Key Contribution**: Uses LLM-based semantic augmentation guided by uncertainty estimates to improve heterogeneous treatment effect estimation. Bridges causal inference and LLM-generated features.
- **Link**: https://arxiv.org/abs/2607.26599

---

## Generative Models

### 19. Amortized Moment Matching for Visual Generation
- **Authors**: Wenze Liu, Xintao Wang, Pengfei Wan, Xiangyu Yue
- **Key Contribution**: New visual generation approach based on amortized moment matching. 30 pages, 11 figures. Offers an alternative to diffusion-based generation.
- **Link**: https://arxiv.org/abs/2607.26860

---

## Key Themes

1. **GRPO improvement** is an active area — ReCo addresses distributional concentration, joining recent work on GRPO reward pathology.
2. **Latent reasoning** for recommendation (WhisperRec) shows that CoT can be compressed into latent tokens, enabling reasoning-quality recommendations at 10x throughput.
3. **User simulation** is evolving from action imitation to decision-aware thinking (DASH), incorporating LLM thinking traces + rubric rewards.
4. **Long-horizon conversion** prediction gets a principled factorization (TWICE) with real deployed gains at Kwai.
5. **RL fine-tuning** fundamentals are being re-examined — the Q-pretraining paper challenges conventional wisdom about offline pretraining for RL.
6. **Multi-agent vs self-refinement**: counterintuitive finding that 2-call self-refinement beats 5-agent pipelines on local LMs.
