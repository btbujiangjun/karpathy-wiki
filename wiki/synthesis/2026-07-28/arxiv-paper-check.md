---
title: arXiv Paper Check — AI & CTR (July 28, 2026)
type: synthesis
created: 2026-07-28
updated: 2026-07-28
sources: [arxiv-cs.AI, arxiv-cs.IR, arxiv-cs.LG]
tags: [arxiv, ai, ctr, recommendation, agents, reasoning, scaling, daily-check]
---

# arXiv Paper Check — AI & CTR (July 28, 2026)

> Curated from cs.AI (51 new Jul 27), cs.IR (6 new Jul 27), cs.LG (75 new Jul 27), and replacement submissions.

## 🔥 Highlights

### AI Agents & Tools

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **FlowEvo: Self-Evolving Agents via Workflow-Skill Co-Evolution** (2607.21596) | Zeyu Ren, Ling Yue, Ran Li, et al. | Training-free framework that compiles successful agent traces into reusable skill records. Three coupled mechanisms: workflow-to-skill compilation, skill-to-workflow feedback, and skill curation. Achieves 82.8% on ALFWorld (+23.6pp over strongest baseline) with <50% token usage. |
| **HierFlow: Coupled Hierarchical Search for Agentic Workflow Synthesis** (2607.21609) | Dong Li, Yanchi Liu, Xujiang Zhao, et al. | Training-free hierarchical search that merges feedback-guided topology adjustments with MCTS-inspired tree search for workflow optimization. Intelligent gating module selectively triggers execution-level searches based on contextual necessity. |
| **Role Drift in Compound LLM Systems** (2607.21627) | Xiaoyang Cao, Siddarth Srinivasan, Michiel A. Bakker | Identifies a failure mode where modules deviate from assigned roles while preserving end-task accuracy. 86% of apparent RL gain vanishes when the decomposer shortcut is eliminated. Proposes Role Anchor regularizer for controllable role adherence. |
| **Procedural Knowledge Is Not Low-Rank: Why LoRA Fails** (2607.21612) | Simon Dennis, Kevin Shabahang, et al. | LoRA fails to match full fine-tuning for procedural tasks at all tested ranks (r=16-128). SVD analysis reveals mean effective rank of 761-1026; rank 128 captures only 43-51% of the Frobenius norm. Fundamental limitation for agentic applications. |

### CTR Prediction & Recommendation

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **RankGraph-2: Lifecycle Co-Design for Billion-Node Graph Learning** (2606.18379, replaced) | Meta | Co-designs graph construction, representation learning, and real-time serving for similarity-based retrieval. Co-learned cluster index reduces serving cost by 83%. Achieves 3.8× higher recall than GAT+DGI, delivers up to +0.96% CTR and +2.75% CVR. Deployed for 20+ retrieval launches. |
| **RecGPT-V3: Stateful Hybrid-Modal Recommender** (2607.15591, replaced) | Taobao | Memory Hub maintains structured, evolving user memory cutting computation by 55.8%. Hybrid-modal foundation model reasons over text tags + Semantic IDs. Latent Intent Reasoning internalizes CoT into latent tokens, reducing output token cost by 200×. Deployed: +1.28% IPV, +1.00% CTR, +3.97% GMV, -52.4% serving resources. |
| **BARGE: Bridging Structural Gap for Generative Rec** (2607.21028, replaced) | Tencent | Item Context-Aware Attention restores item-level structure; Hierarchical Path Reranking + Dual-Path Decoding suppress semantic drift. Online A/B: +0.60% CTR, +1.34% click unique visitors, +1.70% total reading time. |
| **PinEqualizer: Full Funnel Content Exploration** (2607.22518, accepted KDD 2026) | Pinterest | Addresses content cold-start across entire multi-stage funnel. Reduces bias favoring existing content, enabling accurate model prediction across content types. Evaluated with scalable measurement framework for fast experimentation. |
| **GRACE: Sustainable Personalized Recommendation** (2607.22341) | Yibowen Zhao, Yinan Zhang, et al. | Fine-tuning framework integrating sustainability signals (eco-scores) into pretrained rec models. Differentiable approximation for non-differentiable green values + gradient projection to mitigate accuracy-sustainability conflicts. |

### AI Safety & Robustness

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **FlowGuard: Securing Multimodal AI** (2607.21600, ICML 2026 Spotlight) | Jehyeok Yeon, et al. | Monitors internal multimodal consistency via FlowVectors (Partial Information Decomposition). Reduces Attack Success Rates from >90% to <15% on unseen attacks, <3% utility loss, up to 6× latency reduction. |
| **SIREN: Adversarial Manipulation of Web-RAG Recommenders** (2607.21951) | Evan Caville, et al. | Automated attacker that manipulates LLM web-RAG recommendations via 23 content-poisoning techniques. Reaches rank-1 in 62/124 trials with 80.5% reproduction rate. Demonstrates vulnerability of production LLM recommender systems. |
| **Lost in Context: Context Anxiety in LLMs** (2607.21616, ICML 2026) | Ifueko Igbinedion, Jillian Ross, et al. | Frontier reasoning models fail from premature self-doubt when they possess the necessary capabilities. Arises from inability to accurately estimate tokens needed. Performance gains achievable by improving self-assessment, not scaling capabilities. |
| **Red-Team Evidential Ceiling** (2607.21735) | Bandana Kaur | Derives closed-form evidential ceiling for AI evaluations. Current benchmarks adequate for high-frequency harms but several orders of magnitude short for rare, catastrophic ones. |

### LLM Inference & Efficiency

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **AgentKVShift: KV Cache Reuse for Agentic Memory** (2607.21604) | Nilesh Prasad Pandey, et al. | Per-memory KV reuse residual decomposes into shared offset + token-wise fluctuations. Corrects all tokens (not just recomputed ones). Near-full recompute performance at 10-30% refresh, delivering 2-3.5× prefill speedups on A100. |
| **Molt: PyTorch-Native Framework for Agentic RL** (2607.21653) | Jian Hu, et al. | Compact PyTorch-native framework for agentic RL research. Agent as ordinary program, never trains on tokens it didn't generate. Statistically comparable to Megatron-based stack at matched protocol. Open source. |
| **Compression-Based Sparse Attention** (2607.21752) | Debarshi Kundu, et al. | Uses classical gzip compression ratios as masking signal for adaptive sparse attention — no additional parameters. Achieves 1.71 BPB on PG-19 (vs 2.89 dense, 2.34 BigBird), with 3.3× faster convergence. |
| **RED-PIM: Processing-in-Memory for Transformers** (2607.21731) | Zahra Yousefijamarani, et al. | Reduces inter-bank data movement from O(N²) to O(N) via algorithm-architecture co-design. Up to 99.99% inference time reduction vs baseline PIM, geometric mean 66.42%. |

### Multimodal & VLMs

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **Do VLMs Read or Rewrite?** (2607.21617) | Gwang Gook Lee, et al. | VLMs rewrite imperfect text into plausible forms instead of faithful transcription. General-purpose VLMs degrade up to 4.5 WER points under perturbation. Short words (4-6 chars) rewritten up to 10% of the time; cutoff at 8 chars. |

## 📊 Summary Statistics

- **Total curated**: 18 papers
- **AI Agents & Tools**: 4 papers
- **CTR Prediction & Recommendation**: 5 papers
- **AI Safety & Robustness**: 4 papers
- **LLM Inference & Efficiency**: 4 papers
- **Multimodal & VLMs**: 1 paper

## 🔑 Key Trends

1. **Agent Self-Evolution Goes Training-Free**: FlowEvo and HierFlow demonstrate that agents can accumulate capabilities through workflow-skill compilation and hierarchical search without parameter updates. Skill curation mechanisms suppress negative transfer.
2. **Compound System Failure Modes**: Role Drift reveals that RL-trained compound LLM systems can achieve accuracy through shortcuts that bypass module responsibilities. 86% of apparent gains can be spurious — system-level evaluation alone is insufficient.
3. **LoRA Hits Procedural Knowledge Ceiling**: For multi-step procedures, LoRA fails at all tested ranks. Effective rank of weight updates (761-1026) far exceeds LoRA's capacity (r≤128). Critical limitation for agentic fine-tuning.
4. **CTR Recommendation Infrastructure Matures**: RankGraph-2 (Meta), RecGPT-V3 (Taobao), and BARGE (Tencent) all show production-deployed systems with significant gains. Lifecycle co-design and hybrid-modal reasoning are the common themes.
5. **Context Anxiety as Efficiency Bottleneck**: Frontier reasoning models underperform not due to capability limits but premature self-doubt. Improving self-assessment yields gains without scaling model size.
6. **Adversarial Vulnerability of LLM Recommenders**: SIREN demonstrates production LLM recommenders are susceptible to content-poisoning attacks with 80.5% reproduction rate. The recommendation community needs adversarial robustness evaluation.
7. **KV Cache as Agentic Infrastructure**: AgentKVShift shows agentic memory systems have different reuse patterns than RAG — shared offsets dominate residuals. This opens a new optimization surface for agent serving.
