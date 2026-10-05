---
title: ArXiv Paper Check - AI & CTR (2026-10-05)
type: synthesis
created: 2026-10-05
updated: 2026-10-05
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, ir, lg]
---

# ArXiv Paper Check - AI & CTR (2026-10-05)

**Search**: cat:cs.IR OR cat:cs.AI OR cat:cs.LG AND (CTR OR "click-through rate") | Recent 2026 papers (last 24 hours - 2026-10-05 focus).

## Interesting Papers

### 1. [GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm](https://arxiv.org/abs/2602.01865)

- **ID**: `2602.01865` | **Cat**: cs.IR | **Submitted**: 2026-02-03
- **Authors**: Baidu team (multi-author)
- **PDF**: [Link](https://arxiv.org/pdf/2602.01865)

**Key Contributions:**
- Proposes GRAB, a generative framework for CTR prediction inspired by LLM scaling
- Introduces Causal Action-aware Multi-channel Attention (CamA) for user behavior sequences
- Full-scale online deployment shows +3.05% revenue, +3.49% CTR over DLRMs

**Notes:** Demonstrates scaling laws hold for CTR models (more params + longer sequences improve performance).

---

### 2. [Native Multimodal Representation Learning for Click-Through Rate Prediction in E-Commerce Scenarios](https://arxiv.org/abs/2608.24091)

- **ID**: `2608.24091v2` | **Cat**: cs.IR | **Submitted**: 2026-08-25 (v2 2026-09-12) | **Accepted at CIKM 2026**
- **Authors**: Chao Yi, Feifan Yang, Jiawei Feng, Sishuo Chen, Zhangming Chan, Xiang-Rong Sheng, Han Zhu
- **PDF**: [Link](https://arxiv.org/pdf/2608.24091)

**Key Contributions:**
- Addresses gap between multimodal pretraining and CTR objectives
- Proposes "Mine-Then-Train" to extract multimodally interpretable training samples from CTR data
- Aligns multimodal encoders with actual user click preferences

**Notes:** Highlights that raw CTR behavior mixes multimodal + non-multimodal factors causing ambiguous supervision.

---

### 3. [Selective Test-Time Compute Scaling for Click-Through Rate Prediction via Uncertainty-Triggered Feature Path Exploration](https://arxiv.org/abs/2605.24989)

- **ID**: `2605.24989v1` | **Cat**: cs.LG (cross-list cs.AI, cs.IR) | **Submitted**: 2026-05-24
- **Authors**: Moyu Zhang, Yun Chen, Yujun Jin, Jinxin Hu, Yu Zhang, Xiaoyi Zeng
- **PDF**: [Link](https://arxiv.org/pdf/2605.24989)

**Key Contributions:**
- First work exploring test-time compute scaling for CTR prediction
- UTTSI: uncertainty-triggered selective inference (only uncertain instances get extra compute)
- Dual-signal estimator (logit confidence + frequency prior) to distinguish epistemic vs aleatoric uncertainty
- Online A/B test: +5.3% relative CTR gain (p<0.01)

**Notes:** Training-free, model-agnostic; applies adaptive compute only when needed (~2.8x avg overhead).

---

### 4. [CTR-Sink: Attention Sink for Language Models in Click-Through Rate Prediction](https://arxiv.org/abs/2508.03668)

- **ID**: `2508.03668v4` | **Cat**: cs.CL | **Submitted**: 2025-08-05 (latest v4 2026-08-02)
- **Authors**: Zixuan Li et al. (Chinese Academy of Sciences, Ant Group, HKU, etc.)
- **PDF**: [Link](https://arxiv.org/pdf/2508.03668)

**Key Contributions:**
- Identifies semantic fragmentation when treating user behavior sequences as text for LMs
- Introduces behavior-level attention sinks tailored for CTR prediction
- Dynamically regulates attention aggregation via external information

**Notes:** Bridges gap between LM pretraining (coherent text) and recommendation sequences (discrete actions + separators).

---

### 5. [LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks](https://arxiv.org/abs/2604.12096)

- **ID**: `2604.12096v1` | **Cat**: cs.AI | **Submitted**: 2026-04-13
- **Authors**: Luyi Ma, Wanjia Sherry Zhang, Zezhong Fan, Shubham Thakur, Kai Zhao, Kehui Yao, Ayush Agarwal, Rahul Iyer, Jason Cho, Jianpeng Xu, Evren Korpeoglu, Sushant Kumar, Kannan Achan
- **PDF**: [Link](https://arxiv.org/pdf/2604.12096)

**Key Contributions:**
- Uses LLMs as hypernetworks to generate CTR estimator parameters in training-free manner
- Few-shot CoT over multimodal ad content (text+images) to infer feature weights
- CLIP-based retrieval of similar campaigns for demonstrations
- Deployed in production; strong cold-start performance

**Notes:** Innovative "parameter generation" approach for zero-feedback ads.

---

### 6. [EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling](https://arxiv.org/abs/2602.10811)

- **ID**: `2602.10811v1` | **Cat**: cs.IR | **Submitted**: 2026-02-11
- **Authors**: Multi-institutional team
- **PDF**: [Link](https://arxiv.org/pdf/2602.10811)

**Key Contributions:**
- Unified modeling of user behaviors, non-behavioral features, candidate behaviors in single sequence
- Efficient scaling for industrial CTR (sequences up to 10^3 tokens)
- Content Sparse Attention (CSA) for intra-sequence similarity + sparse attention

**Notes:** Focuses on efficient scaling (compute/storage) critical for deployment.

---

### 7. [LoopCTR: Unlocking the Loop Scaling Power for Click-Through Rate Prediction](https://arxiv.org/abs/2604.19550)

- **ID**: `2604.19550v1` | **Cat**: cs.IR | **Submitted**: 2026-04-21
- **Authors**: Anonymous/Team
- **PDF**: [Link](https://arxiv.org/pdf/2604.19550)

**Key Contributions:**
- Proposes looping (reusing layers/transformer blocks) for CTR scaling to reduce params
- Zero-loop inference + loop-wise supervision
- Achieves scaling benefits with lower memory footprint

**Notes:** Shares philosophy with GRAB (scaling CTR models) but via parameter sharing.

---

### 8. [CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer](https://arxiv.org/abs/2602.11410)

- **ID**: `2602.11410v2` | **Cat**: cs.LG | **Submitted**: 2026-02-16 (v2 2026-08-10)
- **Authors**: LinkedIn team
- **PDF**: [Link](https://arxiv.org/pdf/2602.11410)

**Key Contributions:**
- Decoder-only transformer for large-scale ads CTR at LinkedIn
- Context-conditioned decoding with multi-tower heads to handle post-scoring signals (ad position)
- Timestamp-based RoPE, self-gated attention, session masking for train-serve skew
- Online A/B: +11.04% CTR lift over production ensemble

**Notes:** Strong production results; tackles position bias via context conditioning.

---

## Summary

- **Trending**: LLM-inspired architectures (GRAB), test-time compute (UTTSI), multimodal native learning, hypernetworks for cold-start, efficient scaling (EST, LoopCTR), production transformers (CADET)
- **Focus shift**: Beyond pure accuracy - addressing cold-start, train-serve consistency, compute efficiency, uncertainty-aware inference
- **Industrial validation**: Multiple papers report significant online gains (+3-11% CTR)
