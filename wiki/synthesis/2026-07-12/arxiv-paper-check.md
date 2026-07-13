---
title: "arXiv Paper Check — AI & CTR (July 12, 2026)"
type: synthesis
created: 2026-07-12
updated: 2026-07-12
sources: [arxiv-ai, arxiv-ctr]
tags: [arxiv, daily-digest, ai, ctr, recommendation, agents, safety]
---

# arXiv Paper Check — AI & CTR (July 12, 2026)

> Daily scan of cs.AI and cs.IR submissions for AI and CTR papers.
> Generated: 2026-07-12 16:00 UTC

## Summary Statistics

- **cs.AI**: 1,053 total entries, 116 new submissions (July 13, 2026)
- **cs.IR**: 70 total entries, 5 new submissions (July 13, 2026)
- **cs.LG**: ~93 new submissions (estimated)
- **Curated papers**: 22 selected across 6 categories

## 1. LLM Agent Reasoning & Safety

### Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation
- **arXiv**: 2607.09600
- **Authors**: Kaiji Zhou, Ales Leonardis, Yue Feng
- **Key Contribution**: Novel auction-based task allocation mechanism for multi-agent LLM systems, optimizing resource distribution for complex reasoning tasks.
- **Significance**: Introduces economic theory principles to agent coordination, potentially enabling more efficient multi-agent collaboration.

### TrustX Agent Risk Classification Framework (ARC)
- **arXiv**: 2607.09586
- **Authors**: Hannah M. Liu, Rhea Saxena, Shiv Asthana
- **Key Contribution**: Risk-tiering framework for internally created agentic AI systems, providing structured safety classification methodology.
- **Significance**: Addresses growing need for standardized risk assessment in enterprise AI deployment.

### ProofCouncil: An LLM Agent for Solving Open Mathematical Problems
- **arXiv**: 2607.09474
- **Authors**: Johannes Schmitt, Tim Gehrunger, Jasper Dekoninck, et al.
- **Key Contribution**: Multi-agent system for collaborative mathematical problem-solving, appearing in IMProofBench evaluation.
- **Significance**: Advances state-of-the-art in automated theorem proving with 25 pages of detailed methodology.

### ARCANA: A Reflective Multi-Agent Program Synthesis Framework for ARC-AGI-2 Reasoning
- **arXiv**: 2607.09059
- **Authors**: Kunbo Zhang, Lei Fu, Zeyu Wang, et al.
- **Key Contribution**: Reflective multi-agent approach specifically designed for ARC-AGI-2 benchmark, pushing boundaries in artificial general intelligence evaluation.
- **Significance**: Directly targets one of the most challenging AI benchmarks with novel agent architecture.

## 2. Multimodal & Medical AI

### SAGEAgent: A Self-Evolving Agent for Cost-Aware Modality Acquisition in Multimodal Survival Prediction
- **arXiv**: 2607.09521
- **Authors**: Chongyu Qu, Can Cui, Zhengyi Lu, et al.
- **Key Contribution**: Self-evolving agent that dynamically selects cost-effective modalities for survival prediction tasks.
- **Significance**: Addresses practical deployment concerns where modality availability and cost vary significantly.

### Multimodal Reward Hacking in Reinforcement Learning
- **arXiv**: 2607.09492
- **Authors**: Jiayu Yao, Yiwei Wang, Anmeng Zhang, et al.
- **Key Contribution**: First systematic study of reward hacking phenomena in multimodal RL systems.
- **Significance**: Critical safety research as multimodal agents become more prevalent.

### LongMedBench: Benchmarking Medical Agents for Long-Horizon Clinical Decision-Making
- **arXiv**: 2607.09322
- **Authors**: Yanzhen Chen, Zihan Xu, Xiaocheng Zhang, et al.
- **Key Contribution**: Comprehensive benchmark for evaluating medical agents on extended clinical scenarios.
- **Significance**: Fills gap in medical AI evaluation beyond single-turn diagnostics.

## 3. Memory & Context Management

### Shared Selective Persistent Memory for Agentic LLM Systems
- **arXiv**: 2607.09493
- **Authors**: Sanjana Pedada, Aditya Dhavala, Neelraj Patil
- **Key Contribution**: Novel memory architecture enabling selective persistence across agent sessions while maintaining efficiency.
- **Significance**: Addresses critical bottleneck in long-running agent systems where memory management impacts performance.

### KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling
- **arXiv**: 2607.09153
- **Authors**: Peng Kuang, Haibo Jin, Xiaoyu Han, et al.
- **Key Contribution**: Leverages KV-cache transfer for efficient reward modeling in multi-agent settings, reducing computational overhead.
- **Significance**: Practical optimization for scaling test-time compute in production agent systems.

## 4. CTR & Recommendation

### CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **arXiv**: 2602.11410
- **Authors**: David Pardoe, Neil Daftary, et al. (LinkedIn)
- **Key Contribution**: End-to-end decoder-only transformer for ads CTR prediction, deployed at LinkedIn with 11.04% CTR lift.
- **Significance**: Major shift from traditional DLRM architectures, demonstrating transformer scalability in ads ranking.

### DPIFrame: A Dual-Level Parallelism Acceleration Framework for CTR Model Inference
- **arXiv**: 2606.21101
- **Authors**: Dezhi Yi, Huifeng Guo, et al.
- **Key Contribution**: First dual parallelizable framework achieving 23.0× embedding latency reduction and 5.83× overall speedup vs PyTorch.
- **Significance**: Critical infrastructure paper for deploying large-scale CTR models efficiently.

### Dual-Stream MLP is All You Need for CTR Prediction
- **arXiv**: 2606.04944
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, et al.
- **Key Contribution**: Simple MLP architecture with knowledge distillation achieves SOTA on three benchmarks, challenging complex model designs.
- **Significance**: Demonstrates that architectural simplicity can outperform complexity when properly optimized.

### Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Enhanced Sequential User Modeling
- **arXiv**: 2606.15252
- **Authors**: Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang
- **Key Contribution**: Mixed-polarity behavior sequences (+1.9% to +9.6% AUC) outperform positive-only sequences across five architectures.
- **Significance**: Paradigm shift in how user behavior sequences are constructed for CTR prediction.

## 5. Scientific & Mathematical AI

### A Formalization of the Mean-Field Derivation of the Vlasov Equation
- **arXiv**: 2607.08986
- **Authors**: Joseph K. Miller
- **Key Contribution**: AI-assisted Lean formalization of complex physics equations, demonstrating "strategy game" approach to mathematical verification.
- **Significance**: Novel methodology for combining AI assistance with formal verification in computational physics.

### PHINN-EEG: Topological Time-Series Analysis of Dream-State EEG
- **arXiv**: 2607.09662
- **Authors**: Ren Takahashi, Emre Yusuf, Jayabrata Bhaduri
- **Key Contribution**: Dynamic Betti curves for dream content classification using topological data analysis.
- **Significance**: Innovative application of algebraic topology to neuroscience and AI-driven signal processing.

## 6. Safety & Robustness

### Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift
- **arXiv**: 2607.09175
- **Authors**: Dan C. Hsu, Luke Lu
- **Key Contribution**: Formal verification framework for maintaining agent reliability under distribution shift in long-horizon tasks.
- **Significance**: Addresses critical safety gap in production agent deployments.

### Neuro-Agentic Control: A Deep Learning-based LLM-Powered Agentic AI Framework for Controlling Security Controls
- **arXiv**: 2607.09076
- **Authors**: Saroj Gopali, Bipin Chhetri, et al.
- **Key Contribution**: Novel framework using LLM agents to dynamically control cybersecurity defenses.
- **Significance**: Pioneering application of agentic AI to active security operations.

## Key Themes

1. **Agent Safety Maturing**: Multiple papers address risk classification, verification, and reward hacking — indicating field maturation beyond capability demonstrations.

2. **Memory Architecture Innovation**: Shared persistent memory and KV-cache optimization papers suggest memory management as critical bottleneck for production agents.

3. **CTR Simplicity Wins**: DS-MLP shows simple MLP with distillation can outperform complex architectures, while CADET demonstrates decoder-only transformers viable for ads CTR.

4. **Multi-Agent Coordination**: Auction-based and reflective multi-agent approaches push beyond simple debate/consensus patterns.

5. **Formal Verification Integration**: AI-assisted mathematical formalization (Vlasov equation) and scoped verification for agents show growing intersection of AI and formal methods.

## Comparison with Recent Days

| Date | cs.AI New | cs.IR New | Curated | Key Innovation |
|------|-----------|-----------|---------|----------------|
| Jul 12 | 116 | 5 | 22 | Auction-based agent reasoning |
| Jul 11 | ~157 | ~3 | 18 | Backtrack reasoning recovery |
| Jul 10 | 56 | 0 | 18 | Multi-domain CTR adapters |
| Jul 9 | 95 | 4 | 22 | Continuous-query language models |

## Recommendations for Further Reading

1. **For Agent Researchers**: ARCANA (ARC-AGI-2), ProofCouncil (mathematical reasoning), Agora (auction-based allocation)
2. **For CTR Engineers**: CADET (LinkedIn deployment), DS-MLP (simple SOTA), DPIFrame (inference acceleration)
3. **For Safety Researchers**: Multimodal reward hacking, TrustX risk classification, Scoped verification
4. **For Medical AI**: SAGEAgent (multimodal survival), LongMedBench (clinical decision-making)

---

*Generated by karpathy-wiki daily arXiv scan.*
*Next update: 2026-07-13*
