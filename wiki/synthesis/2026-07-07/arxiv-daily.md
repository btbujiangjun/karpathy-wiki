---
title: "arXiv Daily — 2026-07-07"
type: synthesis
created: 2026-07-07
updated: 2026-07-07
tags: [arxiv, survey, llm, reasoning, recommendation, ctr, games, rl, kv-cache, personalization, agent]
---

# arXiv Daily Report — 2026-07-07

A curated survey of recent papers across AI, LLMs, recommendation, advertising/CTR, games/RL, architectures, and efficiency. Covers submissions from late June through early July 2026.

---

## 1. LLM Reasoning & RL Post-Training

### GRPO, Dr. GRPO, and DAPO Are Three Operations on One Number: The Group-Standard-Deviation Identity
- **Link**: [2607.00152](https://arxiv.org/abs/2607.00152)
- **Authors**: Yong Yi Bay, Kathleen A. Yearick
- **Institution**: —
- **Key Innovation**: Proves that GRPO, Dr. GRPO, and DAPO are all settings of a single dial — the group standard deviation of correctness marks. A split group teaches most; a unanimous group teaches nothing. Confirmed on Big-Math.

### DemoPSD: Disagreement-Modulated Policy Self-Distillation
- **Link**: [2607.02502](https://arxiv.org/abs/2607.02502)
- **Authors**: Yunhe Li, Hao Shi, Wenhao Liu, Mengzhe Ruan, Hanxu Hou, Zhongxiang Dai, Shuang Qiu, Linqi Song
- **Institution**: —
- **Key Innovation**: Resolves privileged information leakage in on-policy self-distillation by steering student toward a reverse-KL barycenter target. Outperforms GRPO and SDPO on SciKnowEval with better generalization to GPQA.

### Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents
- **Link**: [2607.01120](https://arxiv.org/abs/2607.01120)
- **Authors**: Ran Yan, Wei Fu, Jiale Li, Shusheng Xu, Zhiyu Mei, Jiaxuan Gao et al. (24 authors)
- **Institution**: —
- **Key Innovation**: Argues enterprise self-evolving agents are bottlenecked by RL *systems*, not RL *algorithms*. Proposes 3 pillars: standardized trajectory data protocol, comprehensive data proxy, and unified evolution control plane. Instantiates via AReaL2.0.

---

## 2. Architecture & Efficiency

### A Hippocampus for Linear Attention (HOLA)
- **Link**: [2607.02303](https://arxiv.org/abs/2607.02303)
- **Authors**: Wanyun Cui
- **Institution**: —
- **Key Innovation**: Gives linear-attention models a bounded exact KV cache as hippocampal complement. At 340M/15B tokens, lowers Wiki PPL from 27.32→22.92 (below full-attention Transformer++ at 26.88). Robust RULER recall at 32k tokens (16x training length).

### MosaicKV: Dynamic Two-D KV Cache Compression
- **Link**: [2607.00760](https://arxiv.org/abs/2607.00760)
- **Authors**: Sheng Qiang, Ruiwei Chen, Yinpeng Wu, Jinyu Gu, Zhichao Hua, Yubin Xia, Binyu Zang, Haibo Chen
- **Institution**: SJTU
- **Key Innovation**: Jointly compresses both sequence and channel dimensions of KV cache with segment-granularity strategy selection. Up to 16x attention speedup, 4.8x lower decode latency, 7.3x higher throughput, 3x memory reduction, only 1.76% accuracy loss.

---

## 3. Recommendation & Personalization

### Bi-NAS: Bi-Level Neural Architecture Search for Recommender Explanations
- **Link**: [2607.01387](https://arxiv.org/abs/2607.01387)
- **Authors**: Longfeng Wu, Yao Zhou, Tong Zeng, Zhimin Peng, Bhanu Pratap Singh Rawat, Lecheng Zheng, Giovanni Seni, Dawei Zhou
- **Institution**: —
- **Key Innovation**: NAS-based framework optimizing cross-attention and feature interaction for explainable recommendations. Integrates LLM zero-shot prompting for personalized justification.

### CoPersona: Collaborative Persona Graphs for Robust LLM Personalization
- **Link**: [2607.01485](https://arxiv.org/abs/2607.01485)
- **Authors**: Yangtian Zhang, Leyao Wang, Hiren Madhu, Ngoc Bui, Walter Roznyatovskiy, Rex Ying
- **Institution**: Yale
- **Key Innovation**: Graph-based collaborative personalization using multiplex persona graphs to borrow signals from similar peers. Dual-branch architecture with non-parametric peer retrieval + parametric graph reasoning. Accepted at KDD '26.

### Prompt Optimization for User Simulation in Conversational Recommender Systems
- **Link**: [2607.00010](https://arxiv.org/abs/2607.00010)
- **Authors**: Nipun B Nair, Tongtong Wu, Weiqing Wang
- **Institution**: —
- **Key Innovation**: Multi-objective framework auto-optimizing LLM prompts for user simulators in CRSs. Mitigates positive bias, data leakage, and limited behavioral diversity. Accepted at IEEE ICDEW 2026.

### From "Strings" to "Things" for Personal Knowledge Graphs: Evaluating LLM Triple Extraction
- **Link**: [2607.00003](https://arxiv.org/abs/2607.00003)
- **Authors**: Abhirup Dasgupta, Fernando Spadea, Oshani Seneviratne
- **Institution**: RPI
- **Key Innovation**: Pipeline extracting RDF-compliant user-preference triples (linked to Wikidata) from conversational data using lightweight LLMs. Evaluates Qwen/Gemma models for downstream recommendation.

### DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized LLMs
- **Link**: [2607.02374](https://arxiv.org/abs/2607.02374)
- **Authors**: Xi Fang, Weijie Xu, Yingqiang Ge, Yuhui Xu, Stephanie Eckman, Chandan K. Reddy
- **Institution**: Virginia Tech
- **Key Innovation**: Ground-truth-free framework mapping reasoning steps to value categories. Shows user-attribute memory induces medium-to-large reasoning drift across 4 LLMs and 10 attribute categories. Evaluates GRPO/DPO for drift reduction.

---

## 4. Games, Agents & Interactive AI

### AI Native Games: A Survey and Roadmap
- **Link**: [2607.00527](https://arxiv.org/abs/2607.00527)
- **Authors**: Zhiyue Xu, Fandi Meng, Kaijie Xu, Clark Verbrugge, Simon Lucas, Jian Zhao
- **Institution**: University of Waterloo, Queen Mary University of London
- **Key Innovation**: Defines AI-native games by counterfactual criterion (core loop collapses if AI removed). Introduces dual-axis G/N taxonomy. Analyzes 53 games. Argues central design problem is organizing semantic openness into stable gameplay.

### Coachable Agents for Interactive Gameplay
- **Link**: [2607.00642](https://arxiv.org/abs/2607.00642)
- **Authors**: Roberto Capobianco et al. (49 authors, Sony AI)
- **Institution**: Sony AI (Zurich, North America, Tokyo)
- **Key Innovation**: Combines UVFAs with curated training scenarios, learning algorithms, and data augmentation to create AI agents that users can coach in real time with *styles*. Demonstrated in Horizon Forbidden West, Gran Turismo, and humanoid locomotion.

---

## 5. Information Retrieval & RAG

### SchemaRAG: Dynamic Large Schema Reduction for LLM-driven Structured Information Extraction
- **Link**: [2607.00008](https://arxiv.org/abs/2607.00008)
- **Authors**: Sin Yu Bonnie Ho, Arlie Coles, Erik Larsson, Eric Marshall, Nathan Bodenstab, Paul Vozila
- **Institution**: —
- **Key Innovation**: Reduces large schemas dynamically for LLM-based structured extraction. Published at ACL 2026 Industry Track.

### PRA-RAG: Provably Robust Aggregation in RAG against Retrieval Corruption
- **Link**: [2607.00012](https://arxiv.org/abs/2607.00012)
- **Authors**: Xue Tan, Yi Zheng, Chang Huo, Yunruo Zhang, Yu Liu, Hao Luan, Zhuyang Yu, Xiaoyan Sun, Ping Chen, Jun Dai
- **Institution**: —
- **Key Innovation**: Provides provable robustness guarantees for RAG aggregation under retrieval corruption.

### Diffusion-GR2: Diffusion Generative Reasoning Re-ranker
- **Link**: [2607.01170](https://arxiv.org/abs/2607.01170)
- **Authors**: Zhuoxuan Zhang, Kangqi Ni, Yuhang Chen, Mingfu Liang, Xiaohan Wei, Yunchen Pu, Fei Tian, Chonglin Sun, Frank Shyu, Adam (Yang) Song, Sandeep Pandey, Luke Simon, Tianlong Chen, Xi Liu
- **Institution**: —
- **Key Innovation**: Applies diffusion models to the re-ranking task for IR, combining generative reasoning with retrieval.

---

## 6. CTR & Advertising

### Dual-Stream MLP is All You Need for CTR Prediction
- **Link**: [2606.04944](https://arxiv.org/abs/2606.04944)
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution**: Renmin University of China
- **Key Innovation**: Knowledge distillation consolidates explicit feature interactions into a main MLP while a parallel MLP captures implicit interactions. SOTA across 3 benchmarks with vanilla MLP architecture. Accepted at TKDD.

### CADET: Context-Conditioned Ads CTR Prediction with a Decoder-Only Transformer
- **Link**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Authors**: Ruoyan Wang et al.
- **Institution**: LinkedIn
- **Key Innovation**: First end-to-end decoder-only transformer for ads CTR deployed at LinkedIn. Handles post-scoring contextual signals with offline-online consistency. +3.04% CTR vs. LiRank baseline.

### ML-DCN: Masked Low-Rank Deep Crossing Network for Scalable Ads CTR Prediction
- **Link**: [2602.09194](https://arxiv.org/abs/2602.09194)
- **Authors**: Jiacheng Li, Yixiong Meng, Yi Wu, Yun Zhao et al.
- **Institution**: Pinterest
- **Key Innovation**: Combines DCNv2's low-rank factorization with MaskNet's instance-guided masking. +1.89% platform-wide CTR improvement in production with neutral serving cost.

---

## 7. Time-Series & Sequential Modeling

### EVOTS: Evolutionary Transformer Search for Time Series Forecasting
- **Link**: [2607.00154](https://arxiv.org/abs/2607.00154)
- **Authors**: AbdElRahman ElSaid, Damir Pulatov
- **Institution**: —
- **Key Innovation**: Evolutionary architecture search for Transformer variants in time-series forecasting.

### StateFlow: Dual-State Recurrent Modeling for Long-Horizon Time Series Forecasting
- **Link**: [2607.00197](https://arxiv.org/abs/2607.00197)
- **Authors**: Haroon Gharwi, Yue Dai, Kai Shu
- **Institution**: —
- **Key Innovation**: Dual-state recurrent architecture for long-horizon forecasting, separating short-term and long-term dynamics.

---

## 8. Emerging Topics

### Scaling Up Thermodynamic AI Models
- **Link**: [2607.00170](https://arxiv.org/abs/2607.00170)
- **Authors**: Andrew G. Moore
- **Institution**: —
- **Key Innovation**: Explores scaling properties of thermodynamic (energy-based) AI computation.

### Program-as-Weights: A Programming Paradigm for Fuzzy Functions
- **Link**: [2607.02512](https://arxiv.org/abs/2607.02512)
- **Authors**: Wentao Zhang, Liliana Hotsko, Woojeong Kim, Pengyu Nie, Stuart Shieber, Yuntian Deng
- **Institution**: Harvard
- **Key Innovation**: Embeds programs as model weights for differentiable fuzzy computation.

### AutoMem: Automated Learning of Memory as a Cognitive Skill
- **Link**: [2607.01224](https://arxiv.org/abs/2607.01224)
- **Authors**: Shengguang Wu, Hao Zhu, Yuhui Zhang, Xiaohan Wang, Serena Yeung-Levy
- **Institution**: Stanford
- **Key Innovation**: Treats memory as a learnable cognitive skill for LLM agents rather than a fixed retrieval mechanism.

---

## Quick Stats

| Category | Papers Highlighted |
|----------|-------------------|
| LLM Reasoning & RL | 3 |
| Architecture & Efficiency | 2 |
| Recommendation & Personalization | 5 |
| Games & Interactive AI | 2 |
| IR & RAG | 3 |
| CTR & Advertising | 3 |
| Time-Series & Sequential | 2 |
| Emerging Topics | 3 |
| **Total** | **23** |
