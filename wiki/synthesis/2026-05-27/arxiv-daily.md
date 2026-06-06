---
title: arXiv Daily — AI & CTR (May 27, 2026)
type: synthesis
created: 2026-05-28
updated: 2026-05-28
sources: [2605.15871, 2605.13687, 2605.19376, 2605.23067, 2604.19550, 2602.11410, 2604.12096, 2605.01726]
tags: [arxiv, daily-digest, ai, ctr, transformers, reasoning, recommendation]
---

# arXiv Daily — AI & CTR (May 27, 2026)

Daily scan of arXiv new submissions in cs.AI, cs.LG, and cs.IR. Picks the most interesting papers with a focus on relevance to LLMs, reasoning, and CTR prediction.

---

## 🧠 AI Research

### 1. Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design

**Authors:** Alberto Pepe, Chien-Yu Lin, Despoina Magka, Bilge Acun, Yannan Nellie Wu, Anton Protopopov, Carole-Jean Wu, Yoram Bachrach

**arXiv:** [2605.15871](https://arxiv.org/abs/2605.15871) | Submitted May 15, 2026

LLM agents autonomously design foundation models beyond standard Transformers. Two frameworks: AIRA-Compose (high-level architecture search with 11 agents, 24h budget) and AIRA-Design (low-level mechanistic implementation with up to 20 agents). Yields 14 architectures across AIRAformer and AIRAhybrid families. At 1B scale, AIRAformer-D and AIRAhybrid-D improve accuracy by 2.4% and 3.8% over Llama 3.2. [[autoresearch]] benchmark: Greedy Opus 4.5 achieves 0.968 validation BPB, surpassing published minimum. Step toward recursive self-improvement.

### 2. A Hierarchical Language Model with Predictable Scaling Laws and Provable Benefits of Reasoning

**Authors:** Jason Gaitonde, Frederic Koehler, Elchanan Mossel, Joonhyung Shin, Allan Sly

**arXiv:** [2605.13687](https://arxiv.org/abs/2605.13687) | Submitted May 13, 2026

Synthetic hierarchical languages via broadcast processes on trees. Proves that bounded-context autoregression requires Ω(n) context to faithfully sample length-n sequences, while a reasoning model with Θ(log n) working memory can sample exactly — exponential improvement. Empirically validated with trained transformers. Formal theoretical grounding for the value of reasoning tokens.

### 3. Generative Recursive Reasoning (GRAM)

**Authors:** Junyeob Baek, Mingyu Jo, Minsu Kim, Mengye Ren, Yoshua Bengio, Sungjin Ahn

**arXiv:** [2605.19376](https://arxiv.org/abs/2605.19376) | Submitted May 19, 2026

Probabilistic multi-trajectory recursive reasoning. Unlike deterministic RRMs that converge to a single prediction, GRAM models reasoning as stochastic latent trajectories, enabling multiple hypotheses and inference-time scaling through both depth and parallel sampling. Improves over deterministic baselines on structured reasoning and multi-solution constraint satisfaction.

### 4. What Training Data Teaches RL Memory Agents

**Authors:** Xinjie He, Zhiyuan Lin, Su Liu, Jialun Wu, Qiyang Xie, Weikai Zhou, Shuai Xiao

**arXiv:** [2605.23067](https://arxiv.org/abs/2605.23067) | Submitted May 21, 2026

Controlled study of curriculum effects for RL-trained memory agents in multi-session QA. Mixed curriculum (LoCoMo + LongMemEval) yields strongest overall F1. Out-of-domain training transfers temporal reasoning skill specifically. Practical lessons: GRPO on single GPU needs continuous rewards (binary exact-match collapses at group size G=4); cross-benchmark mixing requires format-noise filtering.

---

## 📊 CTR / Recommendation

### 5. LoopCTR: Unlocking the Loop Scaling Power for CTR Prediction

**Authors:** Jiakai Tang, Runfeng Zhang, Weiqiu Wang, Yifei Liu, Chuan Wang, Xu Chen, Yeqiu Yang, Jian Wu, Yuning Jiang, Bo Zheng

**arXiv:** [2604.19550](https://arxiv.org/abs/2604.19550) | Submitted Apr 21, 2026

Loop scaling paradigm: recursive reuse of shared model layers decouples computation from parameter growth. Sandwich architecture (Entry → Loop → Exit) with Hyper-Connected Residuals and MoE. Train-multi-loop, infer-zero-loop strategy — single forward pass already SOTA. Oracle analysis reveals 0.02-0.04 AUC untapped headroom. Opens a new scaling dimension for CTR.

### 6. CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer

**Authors:** David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, Liuqing Li, Tao Song, Lars Hertel, Young Jin Yun, Senthil Radhakrishnan, Zhiwei Wang, Tommy Li, Khai Tran, Ananth Nagarajan, Ali Naqvi, Yue Zhang, Renpeng Fang, Avi Romascanu, Arjun Kulothungun, Deepak Kumar, Praneeth Boda, Fedor Borisyuk, Ruoyan Wang

**arXiv:** [2602.11410](https://arxiv.org/abs/2602.11410) | Submitted Feb 11, 2026

Decoder-only transformer for ads CTR at LinkedIn. Context-conditioned decoding with multi-tower prediction heads resolves chicken-and-egg between predicted CTR and ranking. Self-gated attention, timestamp-based RoPE, session masking. Custom Flash Attention kernels for scale. 11.04% CTR lift vs LiRank baseline in online A/B. Deployed on LinkedIn homefeed sponsored updates.

### 7. LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks

**Authors:** Luyi Ma, Wanjia Sherry Zhang, Zezhong Fan, Shubham Thakur, Kai Zhao, Kehui Yao, Ayush Agarwal, Rahul Iyer, Jason Cho, Jianpeng Xu, Evren Korpeoglu, Sushant Kumar, Kannan Achan

**arXiv:** [2604.12096](https://arxiv.org/abs/2604.12096) | Submitted Apr 13, 2026

LLMs as hypernetworks to generate CTR estimator weights for cold-start ads. Few-shot CoT prompting over multimodal ad content (text + images) with CLIP-retrieved similar campaigns. Normalization + calibration for production stability. +55.9% NDCG@10 over cold-start baselines. Deployed on top US e-commerce platform; no statistical difference from warm-start model after 30 days.

### 8. FEDIN: Frequency-Enhanced Deep Interest Network for CTR Prediction

**Authors:** Zenan Dai, Jinpeng Wang, Junwei Pan, Dapeng Liu, Lei Xiao, Shu-Tao Xia

**arXiv:** [2605.01726](https://arxiv.org/abs/2605.01726) | Submitted May 3, 2026 | **SIGIR 2026**

Key observation: user attention scores have distinct spectral entropy for positive vs negative targets — true interests are low-entropy, concentrated spectral patterns. Target-aware spectrum filtering in frequency-domain branch. Dual-branch architecture (frequency + time domain). Outperforms SOTA sequential recommenders across three public datasets.

---

## Key Themes

1. **Agentic research automation**: AIRA shows LLM agents can discover architectures that beat hand-designed Transformers — a concrete step toward recursive self-improvement.
2. **Theoretical foundations for reasoning**: Gaitonde et al. prove reasoning tokens provide exponential sample efficiency over pure autoregression in hierarchical languages.
3. **CTR goes decoder-only**: CADET and LoopCTR both move away from traditional DLRMs toward Transformer-based generative architectures for CTR.
4. **LLM + CTR convergence**: LLM-HYPER uses LLMs as hypernetworks for cold-start CTR; several papers bridge the gap between LLM-style scaling and recommendation.
5. **Inference-time scaling**: GRAM and LoopCTR both explore compute-scaling at inference — through parallel latent trajectories and recursive loop depth respectively.
