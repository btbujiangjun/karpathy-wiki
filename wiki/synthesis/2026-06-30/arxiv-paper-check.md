---
title: "arXiv Paper Check — AI & CTR (June 30, 2026)"
type: synthesis
created: 2026-06-30
updated: 2026-06-30
sources: [arxiv.org]
tags: [arxiv, ai, ctr, recommender-systems, llm, rlhf, diffusion, world-models]
---

# arXiv Paper Check — AI & CTR (June 30, 2026)

> Scanned new listings for **Mon, 29 Jun 2026** across cs.LG (232 total, 75 new), cs.IR (17 total, 8 new), cs.AI (277 total, 74 new). Weekend submissions consolidated into Monday's listing.

---

## AI / LLM / ML Highlights

### 1. R2LM: Bifocal Diffusion Language Models — Asymmetric Bidirectional Context for Parallel Generation
- **Authors**: Yuhang Chen, Xianfeng Wu, Jinhao Duan, Mingfu Liang, Xiaohan Wei, Yunchen Pu, Fei Tian, Chonglin Sun, Parish Aggarwal, Frank Shyu, Luke Simon, Sandeep Pandey, Xi Liu, Tianlong Chen
- **arXiv**: [2606.27732](https://arxiv.org/abs/2606.27732) (cs.IR/cs.AI/cs.LG)
- **Key Contribution**: Resolves the bidirectional vs causal attention dilemma in discrete diffusion LMs. Proposes R2LM (Right-to-Left Mamba): combines causal attention (KV-cache compatible) with a lightweight reverse Mamba SSM sidecar for compressed right-side context. Achieves **2.4×–12.9× higher throughput** than bidirectional dLLMs and **1.9×–2.9× speedup** over AR baselines via parallel decoding with KV caching, while exceeding both causal and bidirectional baselines in quality. Continued pretraining of Qwen3-1.7B with 60B tokens.

### 2. L2A: End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference
- **Authors**: Yuhang Chen, Jinhao Duan, Ruichen Zhang, Mingfu Liang, Xiaohan Wei, Yunchen Pu, Fei Tian, Chonglin Sun, Parish Aggarwal, Frank Shyu, Luke Simon, Sandeep Pandey, Tianlong Chen, Xi Liu
- **arXiv**: [2606.27743](https://arxiv.org/abs/2606.27743) (cs.IR/cs.AI/cs.LG)
- **Key Contribution**: Formulates LLM inference as a constrained allocation problem conditioned on both input difficulty and runtime resource budget. Lightweight budget-conditioned gates jointly optimize layer skipping, head pruning, and reasoning-token reduction. Single model traces the entire compute-accuracy Pareto frontier: at **34% layer sparsity**, stays within **0.6% of dense baseline** on GSM8K, while static baselines drop 5-10%.

### 3. COOPA: A Modular LLM Agent Architecture for Operations Research Problems
- **Authors**: Chuanhao Li, Xiaoan Xu, Dirk Bergemann, Ethan X. Fang, Yehua Wei, Zhuoran Yang
- **arXiv**: [2606.27611](https://arxiv.org/abs/2606.27611) (cs.LG)
- **Key Contribution**: Modular LLM-agent for OR decision support with iterative confidence-based modeling, element-level provenance explanations, and multi-solver routing. Achieves best macro-average accuracy on 6/8 LLM backbones across 3 OR benchmarks, improving over strongest baseline by up to **6.7 pp**.

### 4. PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration
- **Authors**: Arnav Raj
- **arXiv**: [2606.27578](https://arxiv.org/abs/2606.27578) (cs.LG/cs.AI)
- **Key Contribution**: Closed-form per-rater empirical-Bayes shrinkage estimator for RLHF reward models. Fits per-rater affine calibrators with James-Stein shrinkage toward population mean. Reduces within-user held-out RMSE by **8.58%** on PRISM and **9.66%** on PluriHarms, without retraining the reward model. (ICML 2026 Pluralistic Alignment Workshop)

### 5. Retroactive Advantage Correction (RAC): Closed-Form V-Trace Bias Correction for Delay-Aware RLHF
- **Authors**: Arnav Raj
- **arXiv**: [2606.27580](https://arxiv.org/abs/2606.27580) (cs.LG/cs.AI)
- **Key Contribution**: Addresses asynchronous reward signals in production RLHF (slow code executors, human review). Proposes RAC: queues pending slow completions, ages them through a non-negative kernel, and reinjects as clipped residual advantages. Reduces closed-form policy bias by **up to 47.9×** in tabular MDP. Integrates with PPO/GRPO via a two-line patch.

### 6. Textual Belief States for World Models: Identifiable Representation Learning Under Strict Mediation
- **Authors**: Xiang Gao, Kaiwen Dong, Yuguang Yao, Padmaja Jonnalagedda, Kamalika Das
- **arXiv**: [2606.27681](https://arxiv.org/abs/2606.27681) (cs.LG/cs.CL)
- **Key Contribution**: Shows how to enforce strict latent state mediation in text-based world models. Introduces discrete, interpretable, variable-length textual latent states and factorized GRPO (fGRPO), a tree-structured RL method. Achieves up to **57% gains in representation quality** and **98% improvements in rollout performance** on TextWorld and ScienceWorld.

### 7. KARLA: Knowledge-base Augmented Retrieval for Language Models
- **Authors**: Francois Crespin, Fabian M. Suchanek, Nils Holzenberger
- **arXiv**: [2606.26807](https://arxiv.org/abs/2606.26807) (cs.AI/cs.CL)
- **Key Contribution**: Trains LLM to produce special tokens that trigger KB queries during generation. Enables factual updates without retraining, traceable outputs, and smaller models matching larger ones in factual accuracy.

### 8. Self-Compacting Language Model Agents (SelfCompact)
- **Authors**: Tianjian Li et al.
- **arXiv**: [2606.23525](https://arxiv.org/abs/2606.23525) (cs.CL)
- **Key Contribution**: Scaffold allowing the model itself to decide when/how to compact context via a compaction tool + lightweight rubric. Matches or exceeds fixed-interval summarization at **30-70% lower token cost**, improving up to **18.1 points on math** and 5-9 on agentic search.

### 9. Prism Transformer: Progressive Head Schedules for Hierarchical Attention Processing
- **Authors**: Shubham Aggarwal
- **arXiv**: [2606.27449](https://arxiv.org/abs/2606.27449) (cs.LG)
- **Key Contribution**: Replaces static uniform head allocation with progressive head schedule (fewer wide heads in early layers, many narrow heads in deep layers). Parameter-neutral and compute-neutral. Consistent improvements across 124M-757M scales on PIQA, HellaSwag, ARC-Easy, WinoGrande.

### 10. Class-frequency Guided Noise Schedule (CFRG) for Diffusion Models
- **Authors**: Jiequan Cui, Beier Zhu, Qingshan Xu, Xiaojuan Qi, Bei Yu, Hanwang Zhang
- **arXiv**: [2606.27696](https://arxiv.org/abs/2606.27696) (cs.LG/cs.AI/cs.CV)
- **Key Contribution**: First to examine correlations between class frequency and multi-scale noise schedules. Proposes class-frequency guided schedule giving larger-scale noises to low-frequency classes. Substantial improvements on CIFAR-100-LT and ImageNet-LT for generation, classification, and text-to-image.

---

## CTR / Recommendation / IR Highlights

### 11. IntuRec: Intuition-Guided Latent Reasoning for LLM-Based Recommendation
- **Authors**: Chang Liu, Yimeng Bai, Xiaoyan Zhao, Yang Zhang, Qifan Wang, Fuli Feng, Wenge Rong
- **arXiv**: [2606.27684](https://arxiv.org/abs/2606.27684) (cs.IR)
- **Key Contribution**: Two-stage framework that anchors latent reasoning with "recommendation intuition." Extraction stage generates top-K candidate set; injection stage transforms it into preference-aligned intuition embedding via self-/cross-attention. Consistently outperforms SOTA baselines on multiple real-world datasets.

### 12. GLAN: Generative Landing-page Adaptive Navigator (Kuaishou)
- **Authors**: Fan Li, Chang Meng, Jiaqi Fu, Shuchang Liu, Tianke Zhang, Xueliang Wang, Xiaoqiang Feng, Yongqi Liu, Kaiqiao Zhan
- **arXiv**: [2606.27865](https://arxiv.org/abs/2606.27865) (cs.IR)
- **Key Contribution**: Replaces CQL-based RL for personalized landing-page modeling with Decision Transformer-based sequence modeling. Captures non-Markovian temporal dependencies. Online experiments at Kuaishou show **+0.158% DAU** and **+0.108% user Lifetime** improvements.

### 13. NOVA: A Verification-Aware Agent Harness for Architecture Evolution in Industrial Recommender Systems
- **Authors**: Shaohua Liu, Liang Fang, Yilong Sun, Shudong Huang, Qingsong Luo, Shaoxin Liu, et al.
- **arXiv**: [2606.27243](https://arxiv.org/abs/2606.27243) (cs.IR/cs.SE)
- **Key Contribution**: SGD-inspired "architecture gradient" for automated RecSys architecture evolution. Four-level verification cascade (structure→executability→offline→online). Highest effective pass rate on L2/L3 tasks (54.5%/60.0%), **13× reduction** in literature-to-production cycle. Online A/B improves GMV by **+1.25% to +2.02%** on 3 pCVR objectives.

### 14. PermR: Fast Permutation-based Constrained Reranking for Revenue Maximization
- **Authors**: Svetlana Shirokovskikh, Anastasiia Soboleva, Ekaterina Solodneva, Aleksandr Katrutsa, Roman Loginov, Egor Samosvat
- **arXiv**: [2606.28059](https://arxiv.org/abs/2606.28059) (cs.IR/math.OC)
- **Key Contribution**: Lightweight permutation-based ILP approximation for e-commerce reranking. Achieves **~63% of ILP revenue gain** within production latency, preserving all relevance constraints. 14-day online A/B over 56M queries yields **+2% revenue**.

### 15. LLM-Powered Semantic Alignment Framework for Journal Recommendation
- **Authors**: Yanglin Yan, Zicheng Xie, Tianchen Gao, Rui Pan, Hansheng Wang
- **arXiv**: [2606.27930](https://arxiv.org/abs/2606.27930) (cs.IR/stat.AP)
- **Key Contribution**: Formulates journal recommendation as semantic matching between manuscript content and journal scope via LLMs (DeepSeek-V3). Training-free. Top-3/5/10 accuracies of 40.23%/53.67%/70.05% on 23,609 articles from 49 journals.

### 16. Sensitivity-Aware Search Test Collection (Enron SAS)
- **Authors**: Jack McKechnie, Graham McDonald, Craig Macdonald
- **arXiv**: [2606.27559](https://arxiv.org/abs/2606.27559) (cs.IR)
- **Key Contribution**: First test collection for Sensitivity-Aware Search, built on Enron corpus. 150 queries, 11,471 relevance assessments, sensitivity labels. Baseline performances for relevance, sensitivity classification, and SAS. (SIGIR 2026 Resource Paper)

---

## Summary of Key Themes

| Theme | Papers |
|-------|--------|
| **Diffusion Language Models** | R2LM (bifocal asymmetric context), SelfCompact |
| **Resource-Adaptive LLM Inference** | L2A (dynamic sparsity), Prism Transformer |
| **RLHF Alignment** | PEBS (per-rater calibration), RAC (delayed reward) |
| **World Models & Reasoning** | Textual Belief States + fGRPO, COOPA (OR agents) |
| **Knowledge Grounding** | KARLA (KB-augmented generation) |
| **CTR & RecSys Architecture** | IntuRec (latent reasoning), NOVA (agent-driven evolution), GLAN (Kuaishou) |
| **E-commerce Optimization** | PermR (revenue reranking), Journal Rec (LLM semantic alignment) |
| **Search & IR** | Enron SAS test collection |
| **Diffusion Fundamentals** | CFRG (class-frequency noise schedule) |

Notable: Significant progress in **resource-adaptive inference** (L2A, Prism Transformer) and **RLHF tooling** (PEBS, RAC). **Agent-driven RecSys iteration** (NOVA, GLAN) continues to mature at major Chinese platforms. **Diffusion LMs** (R2LM) show path to practical parallel generation with KV caching.
