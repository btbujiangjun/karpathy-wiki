---
title: "arXiv AI Search Report (2026-07-16)"
type: synthesis
created: 2026-07-16
updated: 2026-07-16
sources: []
tags: [arxiv, LLM, recommendation, CTR, sequential-modeling, games, reinforcement-learning]
---

# arXiv AI Research — Recent Papers (as of 2026-07-16)

---

## 1. LLM — Training & Architecture

### Scaling Laws Meet Model Architecture: Toward Inference-Efficient LLMs

- **Authors:** Song Bian, Tao Yu, Shivaram Venkataraman, Youngsuk Park
- **Institution:** Meta AI
- **Date:** Oct 2025 (v3 May 2026)
- **Key Innovation:** Introduces a conditional scaling law that augments the Chinchilla framework with architectural information (hidden size, MLP-to-attention ratio, GQA). Trains 200+ models (80M–3B params) and identifies architectures achieving up to 2.1% higher accuracy and 42% greater inference throughput vs LLaMA-3.2 under the same training budget.
- **Link:** https://arxiv.org/abs/2510.18245

---

### Efficient Scaling of LLM Training with Flexible Context Parallelism

- **Authors:** Yifan Niu, Han Xiao, Dongyi Liu, Wei Zhou, Jia Li
- **Institution:** Alibaba
- **Date:** Feb 2026 (v2 Jun 2026)
- **Key Innovation:** Proposes Flexible Context Parallelism (FCP) — an adaptive parallelism strategy that reconfigures communication groups per batch. Handles extreme data heterogeneity with near-optimal parallelism. Achieves 1.46× speedup over Megatron-LM/DeepSpeed, up to 2.24× on unbalanced batches.
- **Link:** https://arxiv.org/abs/2602.21788

---

### LLMs as High-Dimensional Nonlinear Autoregressive Models with Attention

- **Authors:** Vikram Krishnamurthy
- **Institution:** Cornell University
- **Date:** Jan 2026
- **Key Innovation:** Provides a concise mathematical reference framing LLMs as high-dimensional nonlinear autoregressive models. Covers pretraining, RLHF/DPO/RLVR alignment, and autoregressive generation. Self-attention emerges as repeated bilinear–softmax–linear composition. Includes nanoGPT code examples.
- **Link:** https://arxiv.org/abs/2602.00426

---

### Challenges and Research Directions for LLM Inference Hardware

- **Authors:** Xiaoyu Ma, David Patterson
- **Institution:** Google
- **Date:** Jan 2026
- **Key Innovation:** Identifies memory and interconnect (not compute) as the primary LLM inference bottleneck. Proposes four architecture research directions: High Bandwidth Flash (10× memory capacity), Processing-Near-Memory, 3D memory-logic stacking, and low-latency interconnect. Accepted by IEEE Computer.
- **Link:** https://arxiv.org/abs/2601.05047

---

### KV Cache Optimization Strategies for Scalable and Efficient LLM Inference

- **Authors:** Tejinder Singh et al.
- **Institution:** Not specified
- **Date:** Mar 2026
- **Key Innovation:** Survey of KV cache optimization strategies for LLM inference, covering token-level, layer-level, and head-level compression. Proposes HybridKV, a multimodal LLM inference system that adapts compression strategies per attention head based on heterogeneous behavior.
- **Link:** https://arxiv.org/abs/2603.20397

---

### Beyond Language Modeling: An Exploration of Multimodal Pretraining

- **Authors:** Bo Zheng, Théophane Vallaeys, Junlin Han, Rob Fergus, Yann LeCun, Saining Xie et al.
- **Institution:** Meta FAIR
- **Date:** Mar 2026
- **Key Innovation:** Controlled from-scratch multimodal pretraining using Transfusion (next-token for language + diffusion for vision). Four key insights: RAE is optimal unified visual representation; vision and language data are complementary; unified pretraining naturally yields world modeling; MoE enables efficient multimodal scaling. Discovers vision is significantly more data-hungry than language via IsoFLOP analysis.
- **Link:** https://arxiv.org/abs/2603.03276

---

## 2. CTR Prediction & Advertising

### CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer

- **Authors:** David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, et al. (23 authors)
- **Institution:** LinkedIn
- **Date:** Feb 2026
- **Key Innovation:** End-to-end decoder-only transformer for ads CTR prediction. Key contributions: (1) context-conditioned decoding with multi-tower prediction heads modeling post-scoring signals like ad position; (2) self-gated attention mechanism; (3) timestamp-based RoPE capturing temporal relationships from seconds to months; (4) session masking for train-serve skew. Achieves **11.04% CTR lift** over production DCNv2+sequential encoder baseline (LiRank). Deployed serving main traffic on LinkedIn's ad platform.
- **Link:** https://arxiv.org/abs/2602.11410

---

### Dual-Stream MLP is All You Need for CTR Prediction

- **Authors:** Kesha Ou et al.
- **Institution:** Renmin University (RUCAIBox)
- **Date:** Jun 2026
- **Key Innovation:** DS-MLP uses knowledge distillation to consolidate explicit feature interaction into a main MLP, with a parallel MLP capturing implicit interactions. Two alignment strategies optimize dual-stream compatibility. Achieves state-of-the-art on three benchmarks with a vanilla MLP final model — scalable and efficient for large-scale systems.
- **Link:** https://arxiv.org/abs/2606.04944

---

### Generative Long-term User Interest Modeling for CTR Prediction

- **Authors:** Jiangli Shao, Kaifu Zheng, Hao Fang, Huimu Ye, et al.
- **Institution:** Alibaba / Ant Group
- **Date:** May 2026
- **Key Innovation:** GenLI addresses the limitation of target-centered retrieval that ignores latent user interests. Interest Generation Module (IGM) generates multiple interest distributions (target-independent), Behavior Retrieval Module (BRM) does O(1) lookup selection, and Interest Fusion Module (IFM) combines signals. Overcomes time-consuming pairwise similarity scoring.
- **Link:** https://arxiv.org/abs/2605.15905

---

### IDProxy: Cold-Start CTR Prediction at Xiaohongshu with Multimodal LLMs

- **Authors:** Xiaohongshu team
- **Institution:** Xiaohongshu (Little Red Book)
- **Date:** Mar 2026
- **Key Innovation:** Two-stage coarse-to-fine alignment framework using multimodal LLM hidden representations to generate proxy ID embeddings for cold-start items. Addresses the gap between content encoders and industrial ID embeddings, which exhibit irregular non-clustered distributions unlike public benchmarks.
- **Link:** https://arxiv.org/html/2603.01590

---

## 3. Self-Evolving / LLM-Agent-Driven Systems

### Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents

- **Authors:** Haochen Wang, Yi Wu, Daryl Chang, Li Wei, Lukasz Heldt
- **Institution:** Google DeepMind / YouTube
- **Date:** Feb 2026
- **Key Innovation:** LLM agents (Gemini) autonomously generate, train, and deploy recommendation model changes. Offline Agent (Inner Loop) does high-throughput hypothesis generation with proxy metrics; Online Agent (Outer Loop) validates against delayed business metrics in live production. Agents discover novel optimizer improvements, architecture changes, and reward functions. Multiple successful production launches at YouTube.
- **Link:** https://arxiv.org/abs/2602.10226

---

## 4. Sequential Modeling & User Behavior

### OneTrans: Unified Feature Interaction and Sequence Modeling With One Transformer

- **Authors:** TAAC 2026 authors
- **Institution:** Industry (not specified)
- **Date:** 2026
- **Key Innovation:** Unifies sequence modeling and feature interaction into a single Transformer backbone. A unified tokenizer maps behavior sequences into sequential tokens and user/item/context attributes into non-sequential tokens. Addresses the limitation of encode-then-interaction pipelines that decouple sequence modeling from feature interaction, enabling direct benefit from LLM optimizations (KV caching, mixed precision). Follows scaling law insights from Wukong, RankMixer, and LONGER.
- **Link:** https://puiching-memory.github.io/TAAC_2026/papers/onetrans

---

### Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Sequential User Modeling

- **Authors:** Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang
- **Institution:** Not specified
- **Date:** Jun 2026
- **Key Innovation:** Demonstrates that mixed-polarity behavior sequences (interleaving positive and negative tokens) consistently outperform positive-only sequences. Proposes Target-Aware Polarity Fusion (TAPF) — a lightweight target-conditioned gating mechanism. Achieves +1.9% to +9.6% relative AUC across five architectures with negligible additional compute. Identifies the semantic indistinguishability problem in naive polarity embeddings.
- **Link:** https://arxiv.org/abs/2606.15252

---

### Efficient Sequential Recommendation for Long Term User Interest Via Personalization

- **Authors:** Qiang Zhang, Hanchao Yu, Ivan Ji, et al.
- **Institution:** Meta / Facebook Research
- **Date:** Jan 2026
- **Key Innovation:** Compresses long user interaction histories into learnable tokens combined with recent interactions. Reduces computational costs while maintaining accuracy. Applicable to existing transformer-based models (HSTU, HLLM). Open-source code available. Addresses the quadratic scaling bottleneck of transformers for long behavior sequences.
- **Link:** https://arxiv.org/abs/2601.03479

---

### SeqUDA-Rec: Sequential User Behavior Enhanced Recommendation via Global Unsupervised Data Augmentation

- **Authors:** Not specified
- **Institution:** Not specified
- **Date:** 2025 (recent preprint)
- **Key Innovation:** Integrates GAN-based data augmentation with global user-item graph contrastive learning. GANs generate realistic user sub-sequences; global interaction graph captures cross-user relationships; Transformer-based encoder models temporal interest evolution. Addresses sparse supervised signals and noisy behavior.
- **Link:** https://arxiv.org/pdf/2509.17361

---

### Sequence-aware LLMs for Explainable Recommendation (SELLER)

- **Authors:** Gangyi Zhang, Runzhe Teng, Chongming Gao
- **Institution:** Not specified
- **Date:** Mar 2026
- **Key Innovation:** Dual-path encoder captures user behavior and item semantics, with Mixture-of-Experts adapter aligning these signals with LLMs. Unified evaluation framework assesses explanations via textual quality and effect on recommendation outcomes. Addresses the gap where existing LLM-based explanation methods overlook sequential dynamics.
- **Link:** https://arxiv.org/abs/2603.24136

---

## 5. AI + Games

### AI Native Games: A Survey and Roadmap

- **Authors:** Zhiyue Xu, Fandi Meng, Kaijie Xu, Clark Verbrugge, Simon Lucas, Jian Zhao
- **Institution:** McGill University
- **Date:** Jul 2026
- **Key Innovation:** Defines "AI-native games" using a counterfactual criterion: if the AI component were removed, the core play loop would collapse. Analyzes 53 publicly available AI-native games. Introduces a G/N dual-axis taxonomy (game type × AI mechanic). Identifies that current corpus is concentrated around language-forward designs, with multi-agent simulation and generative construction underrepresented.
- **Link:** https://arxiv.org/abs/2607.00527

---

### Augmenting Game AI with Deep Reinforcement Learning

- **Authors:** Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén
- **Institution:** Electronic Arts (EA), Stockholm
- **Date:** Jun 2026 (Conference on Games 2026)
- **Key Innovation:** Vision paper proposing a framework for deploying RL-based game AI in production games. Addresses bottlenecks: believability of agent behavior, deployment at scale, and integration with existing game development pipelines. Presents examples from EA games and identifies research directions for ML-augmented NPCs.
- **Link:** https://arxiv.org/abs/2606.20210

---

### MARLIN: Multi-Agent Game-Theoretic RL for Sustainable LLM Inference

- **Authors:** H. Moore, S. Qi, D. Milojicic, C. Bash, S. Pasricha
- **Institution:** HP Labs
- **Date:** May 2026
- **Key Innovation:** Multi-agent game-theoretic RL framework co-optimizing TTFT, carbon emissions, water usage, and energy costs for LLM inference in cloud datacenters. Reduces TTFT by 18%, carbon by 33%, water by 43%, energy by 11% vs state-of-the-art. Applies game theory to infrastructure-level optimization of LLM serving.
- **Link:** https://arxiv.org/abs/2605.13496

---

### Nemobot Games: Strategic AI Gaming Agents with LLMs

- **Authors:** Chee Wei Tan, Yuchen Wang, Shangxin Guo
- **Institution:** Not specified
- **Date:** Apr 2026
- **Key Innovation:** Interactive agentic environment for creating LLM-powered game agents. Extends Shannon's taxonomy of game-playing machines across four game classes: dictionary-based, solvable, heuristic-based, and learning-based. Demonstrates self-programming AI through crowdsourced learning and human creativity.
- **Link:** https://arxiv.org/abs/2604.21896

---

### Watermarking Game-Playing Agents in Perfect-Information Extensive-Form Games

- **Authors:** Not specified
- **Institution:** Not specified
- **Date:** May 2026
- **Key Innovation:** Adapts KGW watermark (from LLM literature) to watermark game-playing strategies. Shows watermark can be detected with a handful of games while quality degradation is negligible. Applications: anti-cheating in online chess, IP protection for chess engines (relevant to the Stockfish vs Houdini lawsuit), data cleaning to remove AI-contaminated game datasets.
- **Link:** https://arxiv.org/html/2605.14283v1

---

### Reinforcement Learning in Strategy-Based and Atari Games: A Survey

- **Authors:** Not specified
- **Institution:** Not specified
- **Date:** Feb 2026
- **Key Innovation:** Comprehensive survey of RL in gaming from AlphaGo through MuZero. Covers model-based RL, self-play, and generalization. Discusses limitations: long-term planning in Montezuma's Revenge, scalability challenges from limited input spaces in Atari.
- **Link:** https://arxiv.org/html/2502.10303

---

## Summary of Key Trends

| Trend | Notable Papers |
|-------|---------------|
| **LLM inference efficiency** | Scaling Laws + Architecture, KV Cache Optimization, FCP, Hardware for LLM Inference |
| **Unified architectures for RecSys** | OneTrans (single Transformer for sequence + features), CADET (decoder-only for ads CTR) |
| **LLM agents as ML engineers** | Self-Evolving RecSys (YouTube/Gemini agents) |
| **Negative behavior modeling** | Beyond Positive Signals (mixed-polarity sequences) |
| **AI-native game design** | AI Native Games survey (53 games analyzed) |
| **Game AI + RL deployment** | EA vision paper (Augmenting Game AI), Watermarking game agents |
| **Multimodal pretraining** | Beyond Language Modeling (Transfusion + MoE scaling) |
| **Cold-start via MLLMs** | IDProxy (Xiaohongshu) |
