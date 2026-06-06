---
title: arXiv Daily — May 23, 2026 (AI & CTR)
type: synthesis
created: 2026-05-23
updated: 2026-05-23
sources: []
tags: [arxiv, ai, ctr, recommendation, daily-report]
---

# arXiv Daily — May 23, 2026 (AI & CTR)

New submissions: cs.AI (78 entries), cs.IR (7 new + replacements). Highlights below.

## AI

### FLUID: Industrial-Scale Livestreaming Recommendation without Item IDs
**arXiv:2605.21832** | Xinhang Yuan et al. (Kuaishou)

First framework to fully retire candidate-side item IDs from a production livestreaming ranker. Uses cross-domain multimodal encoder (LUCID) producing discrete hierarchical codes, with staged warmup under online incremental training. Deployed on billion+ user cross-platform base. **Online gains: +0.55% Quality Watch Duration, +2.05% Cold-Start Room Views.**

### What Counts as AI Sycophancy? A Taxonomy and Expert Survey
**arXiv:2605.21778** | Meryl Ye et al.

Reviews 70 papers to build a taxonomy distinguishing sycophancy toward user beliefs vs. personal traits, via explicit vs. implicit language. Survey of 106 experts finds 94.3% agree sycophancy is a significant problem — but **substantial disagreement on which specific behaviors qualify**. Subtle/person-directed behaviors are understudied.

### Implicit Safety Alignment from Crowd Preferences
**arXiv:2605.21822** | Qian Lin, Daniel S. Brown | **ICML 2026**

Extracts shared safety criteria from crowd preference datasets via hierarchical RL framework (Safe Crowd Preference-based RL). Composes safety-aligned skills to enforce safety without explicit safety rewards. Works across safe RL environments and LLM-style tasks.

### The Log is the Agent: Event-Sourced Reactive Graphs
**arXiv:2605.21997** | Yohei Nakajima

Inverts the typical agent framework: the append-only event log is the source of truth, the working graph is a deterministic projection. Yields deterministic replay, cheap forking, and end-to-end lineage. Positioned as a substrate for self-improving agents. Open-source Apache-2.0.

### Search-E1: Self-Distillation for Search-Augmented Reasoning
**arXiv:2605.22511** | Zihan Liang et al.

Self-evolution method using vanilla GRPO + offline self-distillation (OFSD). No external supervision, process reward models, or hand-crafted rewards needed. Reaches 0.440 avg EM on 7 QA benchmarks with Qwen2.5-3B, surpassing all open-source baselines.

### Echo: Learning from Experience Data via User-Driven Refinement
**arXiv:2605.21984** | Hande Dong et al.

Framework that converts user refinement of agent proposals (noisy interaction logs) into high-quality training signals. Production code completion validation: **acceptance rate increased from 25.7% to 35.7%** by harvesting user-driven refinement sequences.

### Active Evidence-Seeking in LLMs for Clinical Decision Support
**arXiv:2605.22047** | Chen Zhan et al.

OSCE-inspired standardized patient simulator. Across 468 cases × 15 models: multi-turn evidence seeking **reduces diagnostic accuracy by 12.75%** and supporting-evidence quality by 24.36% vs. full-context evaluation. Static benchmarks overestimate interactive performance.

### Planning in the LLM Era: Building for Reliability and Efficiency
**arXiv:2605.21902** | Michael Katz et al. | **ICAPS 2026**

Argues for a shift from single-shot plan generation → generating symbolic solvers at construction time that can be verified and used efficiently at inference. Discusses three categories of planner-generation methods and their limitations.

## CTR / Recommendation

### RPORec: Reinforced Preference Optimization for Reasoning-Augmented Recommendations
**arXiv:2605.21967** | Jingtong Gao et al.

Two-stage framework: (1) LLM generates CoT reasoning to guide recommendation head (Rechead), (2) Rechead produces verifiable rewards to fine-tune LLM backbone via RL. Gains on public benchmarks **and large-scale online deployments**.

### Bridging the Cold-Start Gap: LLM Synthetic Data at Airbnb
**arXiv:2605.21812** | Wendy Ran Wei et al. (Airbnb)

Framework for generating synthetic queries + relevance labels using LLMs for natural language search cold-start. Seed-guided approach achieves **KL divergence 0.66 vs. 12.03 for InPars baseline** on query length distribution. Deployed in production pipelines for daily synthetic example generation.

### Generative Conversational Recommender System
**arXiv:2605.21987** | Sixiao Zhang et al.

Fully generative conversational recommender unifying recommendation and dialog in a single autoregressive framework. Items as discrete semantic IDs integrated into generation. **Up to 29% Recall@1 improvement** over strong baselines, with competitive dialog quality.

### ThinkGR: Chain-of-Thought for Generative Retrieval
**arXiv:2605.22358** | Wenhao Zhang et al.

First work integrating CoT into generative retrieval. Interleaves reasoning with docid generation via hybrid decoding (unconstrained thought ↔ constrained docid). **+6.86% average improvement** on multi-hop retrieval benchmarks.

### LLM Retrieval for Stable and Predictable Ad Recommendations
**arXiv:2605.21969** | Vinodh Kumar Sunkara et al. | SIGIR 2026 AgentSearch Workshop

Introduces evaluation framework for stability/predictability of ads recommender systems. Uses fine-tuned LLMs for semantic candidate generation via hierarchical attribute extraction + graph-based expansion. Online experiments demonstrate gains in both predictability and traditional metrics.

### Behavior-Guided Candidate Calibration for Multimodal Recommendation
**arXiv:2605.22073** | Zesheng Li et al.

Finds moderate cross-view agreement helps multimodal recommendation but strong agreement suppresses discriminative signal. Spectral analysis reveals low-frequency shared structure vs. high-frequency discriminative signal. Consistent gains on Amazon Baby, Sports, Electronics.

## Notable Trends

- **Item ID-free recommendation**: FLUID retires candidate item IDs entirely in livestreaming — expect more work on content-only ranking.
- **RL reasoning for recommendation**: RPORec uses RL to align LLM reasoning with recommendation objectives; signals convergence of RL for recsys.
- **Cold-start via synthetic data**: Airbnb shows LLM-generated synthetic queries can be production-grade for cold-start.
- **Generative retrieval goes deliberative**: ThinkGR adds CoT to generative retrieval — multi-hop reasoning + retrieval in one generative pass.
- **AI safety taxonomy tightening**: Sycophancy taxonomy paper shows the field lacks shared definitions — expect more conceptual work before reliable mitigation.
- **Event-sourced agent architectures**: Nakajima's ActiveGraph and broader pattern of log-as-source-of-truth for auditable agents.
