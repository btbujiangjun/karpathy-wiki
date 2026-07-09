---
title: arXiv Daily — July 9, 2026
type: synthesis
created: 2026-07-09
updated: 2026-07-09
tags: [arxiv, daily-report, llm, recommendation, ctr, games, rl, transformer, kv-cache]
---

# arXiv Daily Report — July 9, 2026

Curated papers from arXiv submissions (Jul 3–9, 2026) across AI, LLMs, recommendation, advertising, CTR, sequential modeling, games, and related areas.

---

## 1. Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning

- **Authors:** Vladislav Beliaev
- **Institution:** —
- **Abstract:** Introduces Agon, which makes two competing LLMs each other's graders. Both attempt the same problem; one drafts and the other reads while solving, and each is rewarded for out-solving the other. On DeepMath hard split with Qwen3, this doubles GRPO's pass@1 — roughly 8× the gain of an untrained Mixture-of-Agents baseline. No process labels or reward model needed.
- **Key Innovation:** Cross-model competitive RL where reasoning is judged implicitly during training via adversarial grading instead of verifiable reward.
- **Link:** https://arxiv.org/abs/2607.07690

---

## 2. The Key to Going Linear: Analysis-Driven Transformer Linearization

- **Authors:** Anna Kuzina, Paul N. Whatmough, Babak Ehteshami Bejnordi
- **Institution:** —
- **Abstract:** Isolates the effect of state update design in frozen-backbone transformer linearization. Shows softmax relies on key-dependent rank-1 orthogonal projections, explaining why delta-style networks outperform gated accumulation. Introduces sink tokens, short convolutions, and fixed-budget cache routing. Scales across LLaMA and Qwen up to 32B, matching long-context retrieval of complex adaptive-caching frameworks.
- **Key Innovation:** Analysis-driven identification of why certain linear attention designs work, with structural interventions that close the gap with full attention.
- **Link:** https://arxiv.org/abs/2607.07706

---

## 3. How Data Shapes RoPE Frequency Usage: From Positional Scale Matching to Length Generalization

- **Authors:** Xinyi Wu, Siyuan Liu, Ali Jadbabaie
- **Institution:** MIT / —
- **Abstract:** Proposes a data-centered explanation for non-uniform RoPE frequency usage: frequencies are selected to match the relative-distance structure of training data. Formalizes a field-resolution tradeoff showing optimal frequency scales as 1/W. Connects to position-interpolation-based length generalization and shows natural language exhibits approximate self-similarity across positional scales.
- **Key Innovation:** First principled explanation of why RoPE frequencies are used non-uniformly, linking frequency selection to data properties and length generalization.
- **Link:** https://arxiv.org/abs/2607.07678

---

## 4. Fractal KV-Cache Archives: Lossless Symbolic Storage with In-Place Retrieval for Long-Context LLM Inference

- **Authors:** Vladimir Gusev
- **Institution:** —
- **Abstract:** Revisits contractive iterated-map codes that serialize a symbol sequence into low-dimensional real vectors, forming a natural archive for quantized KV caches. Provides O(1) random access, O(1) amortized append, and lossless storage. Per-head residual VQ reduces cache by 36–54× vs fp16 at 11–15% perplexity cost. Shows key quantization is ~4× more damaging than value quantization. Archives double as search indexes — approximate substring queries execute directly on stored vectors.
- **Key Innovation:** Fractal codes for KV-cache storage that simultaneously serve as compressed archive and in-place search index with O(1) access.
- **Link:** https://arxiv.org/abs/2607.07144

---

## 5. DepthWeave-KV: Token-Adaptive Cross-Layer Residual Factorization for Long-Context KV Cache Compression

- **Authors:** Anna Cordoba et al.
- **Institution:** —
- **Abstract:** Token-adaptive cache compression factorizing KV states across neighboring layers using shared low-rank channel bases with lightweight token-specific residuals. Combines cross-depth residual factorization with a token-conditional depth router. Fused CUDA implementation achieves 8.3× KV memory reduction at 72.8 tokens/sec for 64K context with near-full-cache quality.
- **Key Innovation:** Cross-layer KV factorization with token-adaptive routing — allocates higher rank to instruction-bearing / retrieval-critical tokens.
- **Link:** https://arxiv.org/abs/2607.06523

---

## 6. FourierQK: Spectral Preprocessing of Query-Key Projections Improves Transformer Attention

- **Authors:** Athanasios Zeris
- **Institution:** —
- **Abstract:** FFT-based spectral preprocessing of Q/K projections substantially improves character-level language modeling. Four learned frequencies spanning paragraph-to-word scales achieve 79% reduction in validation loss over standard dot-product attention. Frequencies converge to a near-geometric multi-scale ordering (49, 27, 10, 6 tokens/cycle). Benefit is specific to spectral preprocessing — random projections produce no improvement.
- **Key Innovation:** First demonstration that applying Fourier transform to Q/K projections (not token embeddings) significantly improves attention — spectrally distinct from FNet.
- **Link:** https://arxiv.org/abs/2607.07478

---

## 7. Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning

- **Authors:** Zhenyu Hou, Yujiang Li, Jie Tang, Yuxiao Dong
- **Institution:** Tsinghua University / Zhipu AI / GLM Team
- **Abstract:** Presents SAO (Single-rollout Asynchronous Optimization) to address stability and off-policy challenges in asynchronous RL for LLMs. Replaces group-wise GRPO sampling with single-rollout per prompt. Introduces strict double-side token-level clipping. Consistently outperforms GRPO on SWE-Bench Verified, BeyondAIME, IMOAnswerBench. Deployed in GLM-5.2 (750B-A40B) agentic RL pipeline.
- **Key Innovation:** Single-rollout sampling + double-side token-level clipping for stable asynchronous RL at scale, deployed in a 750B production model.
- **Link:** https://arxiv.org/abs/2607.07508

---

## 8. Entropy Pacing Policy Optimization for Multi-Task Agentic RL

- **Authors:** Zetian Hu, Shunyu Liu, Junjie Zhang, Yongcheng Jing, Ting-En Lin, Yongbin Li, Dacheng Tao
- **Institution:** JD / —
- **Abstract:** Identifies exploration-exploitation pace mismatch in multi-task agentic RL: easier tasks converge to low-entropy policies that hinder harder tasks. Proposes EPPO which replaces GRPO's fixed clipping threshold with task entropy-aware adaptive bounds. Tightens updates for over-confident tasks, relaxes for under-explored ones.
- **Key Innovation:** Task-wise dynamic clipping that addresses inter-task entropy crossover in multi-task LLM agent RL.
- **Link:** https://arxiv.org/abs/2607.07178

---

## 9. Predicting LLM Safety Before Release by Simulating Deployment

- **Authors:** Marcus Williams, Hannah Sheahan, Cameron Raymond et al.
- **Institution:** OpenAI / —
- **Abstract:** Studies simulating deployment by seeding from de-identified conversations of a prior model, regenerating responses with a candidate model. Evaluated across four GPT-5-series deployments. Produces informative estimates of post-deployment misbehavior rates, outperforming adversarial baselines. Shows simulation can be seeded from public chat datasets while remaining informative.
- **Key Innovation:** Practical methodology for forecasting real-world LLM misbehavior rates pre-deployment using conversation replay.
- **Link:** https://arxiv.org/abs/2607.07184

---

## 10. Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors

- **Authors:** Oliver Makins, Orazio Angelini, Zohreh Shams, Mary Phuong
- **Institution:** DeepMind / —
- **Abstract:** Initiates empirical study of multi-agent AI control, formalizing distributed attacks where several agents jointly aim for a malicious goal. Develops FakeLab (9 services, 86 benign tasks, 4 attack objectives). Central finding: fragmentation effect — as more agents coordinate, per-agent monitoring becomes less likely to catch attackers. An explicit planner amplifies this effect up to 7×.
- **Key Innovation:** First empirical study of multi-agent distributed attacks against AI control measures, revealing fragmentation vulnerability.
- **Link:** https://arxiv.org/abs/2607.07368

---

## 11. Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)

- **Authors:** Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution:** Renmin University of China / —
- **Abstract:** Proposes DS-MLP for CTR prediction. Uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP network while a parallel MLP captures implicit interactions. With two alignment strategies for compatibility. Despite being a vanilla MLP structure at inference, achieves SOTA across three benchmarks — scalable and efficient for large-scale recommendation.
- **Key Innovation:** Distills explicit feature interactions into a single MLP stream, eliminating complex dual-stream architectures at inference while matching SOTA.
- **Link:** https://arxiv.org/abs/2606.04944 (Accepted by TKDD)

---

## 12. Autonomous Information Seeking: A Roadmap for Agentic Recommender Systems

- **Authors:** Xinyu Lin, Yashar Deldjoo, Sunhao Dai et al.
- **Institution:** NUS / Polimi / Renmin / CAS / —
- **Abstract:** Comprehensive survey of LLM-agent-based recommender systems. Introduces unified taxonomy grounded in autonomy level: agent-assisted recommendation, agent-as-recommender, and agent-as-user-simulator. Covers profiles, memory, tool use, workflows, and optimization. Discusses evaluation methodologies and open challenges.
- **Key Innovation:** First systematic taxonomy of agentic recommender systems organized by autonomy level.
- **Link:** https://arxiv.org/abs/2607.04433

---

## 13. Seeing and Reflecting: Multimodal Memory-Enhanced Agent Collaboration for Recommendation

- **Authors:** Hao Cong, Huizu Lin, Zihan Wang, Chengkai Huang, Quan Z. Sheng, Lina Yao
- **Institution:** UNSW / —
- **Abstract:** Proposes MMEACR, a multimodal memory-enhanced agent collaboration framework. Dual-track memory separates interpretable agent reasoning from fine-grained multimodal matching. User/Item Memory Agents maintain persistent multimodal memories updated via attribute-guided reinforcement-and-reflection. Decoupled multimodal embedding memory preserves cross-modal signals.
- **Key Innovation:** Dual-track memory architecture separating reasoning from multimodal matching for LLM-based recommender agents.
- **Link:** https://arxiv.org/abs/2607.07108

---

## 14. HGenPush: Heterogeneous Generative Recommendation for Industrial Push Notification Systems

- **Authors:** Xiao Liang, Jiali Feng, Xin Feng et al. (Kun Gai)
- **Institution:** Kuaishou
- **Abstract:** End-to-end heterogeneous generative recommendation architecture for push notifications. Integrates video + author recommendation in a unified framework. Uses lightweight multi-token prediction (non-autoregressive) for efficiency and preference alignment via user feedback as reward signals. Deployed at Kuaishou, achieved 0.181% DAU increase.
- **Key Innovation:** First industrial deployment of heterogeneous generative recommendation (video + author) for push notifications with non-autoregressive generation.
- **Link:** https://arxiv.org/abs/2607.03362

---

## 15. Reward-Adaptive Iterative Discovery: Automated Game Testing for NHL26

- **Authors:** Florian Fuchs, Jessy Gosselin-Grant, Boris Skuin et al.
- **Institution:** EA Sports / —
- **Abstract:** Proposes RAID (Reward-Adaptive Iterative Discovery) for automated game testing using iterative RL with a population of goal-scoring agents. Introduces extension on top of existing RL algorithms to find multiple diverse high-quality solutions. Found 6 hockey scoring exploits in NHL26 qualitatively similar to those from hours-long manual testing.
- **Key Innovation:** RL-based automated game testing with diversity-enforced exploration that discovers exploits matching human playtester findings.
- **Link:** https://arxiv.org/abs/2607.07498

---

## Summary of Themes

| Theme | Papers |
|-------|--------|
| **KV Cache / Long Context** | #4 Fractal KV, #5 DepthWeave-KV |
| **Transformer Architecture** | #2 Linearization, #6 FourierQK, #3 RoPE |
| **LLM RL / Reasoning** | #1 Agon, #7 SAO, #8 EPPO |
| **AI Safety / Control** | #9 Deployment Simulation, #10 Multi-Agent Control |
| **Recommendation / CTR** | #11 DS-MLP, #12 Agentic RS Survey, #13 MMEACR, #14 HGenPush |
| **Games** | #15 RAID for NHL26 |

---

*Generated from arXiv cs.AI, cs.LG, and cs.IR recent submissions (Jul 3–9, 2026).*
