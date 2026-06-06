---
title: arXiv Daily — AI, LLMs, CTR, Games (June 1, 2026)
type: synthesis
created: 2026-06-01
updated: 2026-06-01
sources: [2605.28732, 2605.24856, 2605.26086, 2605.21987, 2605.19376, 2605.13496, 2605.07926, 2605.07825, 2605.06548, 2605.06390, 2605.03142, 2605.01865, 2605.00751, 2605.00421, 2604.13389, 2604.12298, 2604.04457, 2603.18761, 2602.16928, 2602.10226]
tags: [arxiv, daily-digest, ai, llm, ctr, recommendation, agents, reasoning, games, multi-agent, multimodal]
---

# arXiv Daily — AI, LLMs, CTR, Games (June 1, 2026)

Daily scan of arXiv recent submissions in cs.AI, cs.LG, cs.IR, cs.CL, cs.MA, and cs.GT. Covers the week of May 25–June 1, 2026.

---

## 🧠 LLM Reasoning, Alignment & Interpretability

### 1. MemTrace: Tracing and Attributing Errors in LLM Memory Systems

**Authors:** Zjunlp et al.

**Institution:** Zhejiang University

**arXiv:** [2605.28732](https://arxiv.org/abs/2605.28732) | Submitted May 27, 2026

Transforms memory pipelines into executable memory evolution graphs for fine-grained tracing of information flow. Constructs MemTraceBench covering Long-Context, RAG, Mem0, and EverMemOS. Reveals memory failures are systematic (information loss, retrieval misalignment). Uses attribution signals to guide prompt optimization in a closed loop, boosting end-task performance up to 7.62%.

**Key innovation:** First systematic error tracing framework for LLM memory systems with automated root-cause attribution.

### 2. The Concept Allocation Zone (CAZ)

**Authors:** James Henry

**Institution:** Independent Researcher

**arXiv:** [2605.24856](https://arxiv.org/abs/2605.24856) | Submitted May 24, 2026

Introduces the Concept Allocation Zone — a contiguous region of Transformer residual stream depth where concepts become geometrically separable. Tracks concept lifecycle (emergence → allocation → settling) via layer-wise metrics and velocity-based detection. Proposes multi-layer concept extraction and sub-representation analysis. Makes 8 testable predictions about cross-architecture CAZ ordering, abstraction depth, and post-CAZ degradation.

**Key innovation:** Replaces "best layer" heuristic with a dynamic CAZ framework showing concept formation is a depth-extended process, not a single-layer event.

### 3. Probabilistic Attribution for Large Language Models

**Authors:** Shilpika Shilpika, Carlo Graziani, Bethany Lusch, Venkatram Vishwanath, Michael E. Papka

**Institution:** Argonne National Laboratory

**arXiv:** [2605.21726](https://arxiv.org/abs/2605.21726) | Submitted May 20, 2026

Uses next-token log-probabilities to situate LLMs within stochastic process theory. Designs a model-agnostic probabilistic attribution measure via Bayes rule inversion to capture internal distribution over token sequences. Attribution score is log-ratio of conditional probabilities with/without a marginalized token. Evaluates 8 models across 7 prompts, investigating anomalies, token sensitivity, response stability, and training convergence.

**Key innovation:** First principled probabilistic attribution framework grounded in stochastic process theory rather than gradient-based or attention-based methods.

### 4. Automated Alignment is Harder Than You Think

**Authors:** Aleksandr Bowkis, Marie Davidsen Buhl, Jacob Pfau, Geoffrey Irving

**Institution:** Anthropic

**arXiv:** [2605.06390](https://arxiv.org/abs/2605.06390) | Submitted May 7, 2026

Argues that even non-scheming AI research agents could produce compelling but catastrophically misleading safety assessments, leading to unintentional deployment of misaligned AI. Analyzes failure modes in automated alignment research pipelines and shows fundamental limitations in self-supervised safety verification.

**Key innovation:** Formal treatment of deceptive alignment risks in automated research pipelines, separate from deliberate scheming.

### 5. AgentEscapeBench: Evaluating Out-of-Domain Tool-Grounded Reasoning

**Authors:** Multiple

**Institution:** Multiple

**arXiv:** [2605.07926](https://arxiv.org/abs/2605.07926) | Submitted May 8, 2026

Escape-room-style benchmark testing LLM agents' ability to infer, execute, and revise novel tool-use procedures under explicit long-range dependency constraints. 270 instances across 5 difficulty tiers with DAG-based dependency graphs. Humans decline from 98.3% to 80.0% while best model drops from 90.0% to 60.0% with depth. Failures attributed to long-range state tracking breakdown and clue adherence.

**Key innovation:** First benchmark isolating long-range dependency tracking in tool-use, showing sharp performance decay with depth.

---

## 📚 Generative Models & Architecture

### 6. Continuous Latent Diffusion Language Model (Cola DLM)

**Authors:** Hongcan Guo, Qinyu Zhao, Yian Zhao, Shen Nie, Rui Zhu, et al.

**Institution:** Multiple

**arXiv:** [2605.06548](https://arxiv.org/abs/2605.06548) | Submitted May 7, 2026

Hierarchical latent diffusion LM: Text VAE → block-causal DiT in continuous latent space → conditional decoding. Separates global semantic organization from local textual realization. ~2B parameters, 8 benchmarks, scaling up to ~2000 EFLOPs. Establishes continuous latent prior modeling as a principled alternative to autoregressive token-level modeling.

**Key innovation:** First comprehensive demonstration that hierarchical latent diffusion can scale competitively with autoregressive LMs at ~2B parameter scale.

### 7. AnisoAlign: Anisotropic Modality Gap Alignment

**Authors:** Xiaomin Yu et al.

**Institution:** Multiple

**arXiv:** [2605.07825](https://arxiv.org/abs/2605.07825) | Submitted May 8, 2026

Reveals the modality gap is not a simple global shift but an anisotropic residual structure concentrated along a few dominant directions. Proposes anisotropic geometric correction (AnisoAlign) that aligns with target-modality distribution while preserving source-modality semantic structure. Demonstrates benefits in geometric diagnostics and text-only MLLM training.

**Key innovation:** Reformulates modality gap as a correctable structured geometric phenomenon rather than an irreducible empirical observation.

### 8. NeuroGame Transformer: Game-Theoretic Attention

**Authors:** Djamel Bouchaffra, Faycal Ykhlef, Hanene Azzag, Mustapha Lebbah, Bilal Faye

**Institution:** Multiple

**arXiv:** [2603.18761](https://arxiv.org/abs/2603.18761) | Submitted March 19, 2026

Reconceptualizes attention through cooperative game theory (Shapley/Banzhaf values) and statistical physics (Ising Hamiltonian with Gibbs distribution). Tokens treated as players/spins; attention weights emerge as marginal probabilities under Gibbs distribution computed via mean-field equations. Achieves 86.4% on SNLI, surpassing ALBERT-Base and competitive with RoBERTa-Base.

**Key innovation:** First principled fusion of game-theoretic value allocation and statistical physics for Transformer attention, escaping pairwise limitations.

---

## 🎯 Recommendation & CTR

### 9. Self-Evolving Recommendation System with LLM Agents (YouTube)

**Authors:** Haochen Wang, Yi Wu, Daryl Chang, Li Wei, Lukasz Heldt

**Institution:** Google / YouTube

**arXiv:** [2602.10226](https://arxiv.org/abs/2602.10226) | Submitted February 10, 2026

LLM-driven (Gemini family) autonomous system that generates, trains, and deploys model changes. Two-loop architecture: Offline Agent (Inner Loop, high-throughput hypothesis gen with proxy metrics) and Online Agent (Outer Loop, validation against live north star metrics). Demonstrates production launches at YouTube with discovered novel optimizers, architectures, and reward functions.

**Key innovation:** First end-to-end autonomous ML system using LLMs as machine learning engineers, validated in production at YouTube scale.

### 10. RoTE: Coarse-to-Fine Multi-Level Rotary Time Embedding for Sequential Recommendation

**Authors:** Multiple

**Institution:** Multiple (SIGIR 2026)

**arXiv:** [2604.13389](https://arxiv.org/abs/2604.13389) | Submitted April 2026

Rotary Time Embedding captures temporal patterns at multiple granularities in sequential recommendation. Coarse-to-fine architecture enabling the model to distinguish between short-term and long-term temporal dynamics. Outperforms prior time-aware recommenders on multiple benchmarks.

**Key innovation:** Multi-level rotary position encoding adapted for temporal recommendation, replacing absolute/relative time embeddings.

### 11. Deep Situation-Aware Interaction Network for CTR Prediction

**Authors:** Multiple

**Institution:** Multiple (RecSys 2026)

**arXiv:** [2604.12298](https://arxiv.org/abs/2604.12298) | Submitted April 2026

Models situational context in user-item interactions for CTR prediction using a situation-aware interaction module. Captures how the same user-item pair may have different click probabilities depending on situational factors. Demonstrates significant gains over existing CTR models on both public and industrial datasets.

**Key innovation:** Explicitly models situational context as a first-class signal in CTR prediction, moving beyond user/item feature interactions.

### 12. Retrieval Augmented Conversational Recommendation with RL

**Authors:** Zhenrui Yue et al.

**Institution:** Multiple

**arXiv:** [2604.04457](https://arxiv.org/abs/2604.04457) | Submitted April 6, 2026

Two-stage framework: retriever generates candidates from a 300K+ movie corpus → LLM refines with conversational context. Novel RL method using LLM feedback to iteratively update the retriever, creating a collaborative feedback loop that mitigates retrieval-generation misalignment. Reduces hallucinations by grounding in factual metadata.

**Key innovation:** First framework to dynamically bridge retrieval and generation via RL feedback in conversational recommendation.

### 13. Generative Conversational Recommender System

**Authors:** Sixiao Zhang, Mingrui Liu, Cheng Long

**Institution:** Nanyang Technological University

**arXiv:** [2605.21987](https://arxiv.org/abs/2605.21987) | Submitted May 21, 2026

Unifies recommendation and dialog generation within a single autoregressive framework, replacing decoupled or retrieval-based pipelines. End-to-end generative approach for conversational recommendation that jointly models user intent and response generation.

**Key innovation:** Purely generative paradigm for conversational recommendation without separate retrieval components.

---

## 🎮 Multi-Agent & Game Theory

### 14. MARLIN: Multi-Agent Game-Theoretic RL for Sustainable LLM Inference

**Authors:** H. Moore, S. Qi, D. Milojicic, C. Bash, S. Pasricha

**Institution:** Hewlett Packard Labs, Colorado State University

**arXiv:** [2605.13496](https://arxiv.org/abs/2605.13496) | Submitted May 13, 2026

Novel multi-agent game-theoretic RL framework that co-optimizes TTFT, carbon emissions, water usage, and energy costs for LLM inference in cloud datacenters. Reductions: 18% TTFT, 33% carbon, 43% water, 11% energy vs. SOTA. Addresses the fact that LLM inference accounts for up to 90% of total LLM lifecycle energy.

**Key innovation:** First framework to jointly optimize sustainability metrics (carbon, water, energy) alongside latency for LLM inference serving via MARL.

### 15. NonZero: Interaction-Guided Exploration for Multi-Agent MCTS

**Authors:** Sizhe Tang, Zuyuan Zhang, Mahdi Imani, Tian Lan

**Institution:** George Washington University

**arXiv:** [2605.00751](https://arxiv.org/abs/2605.00751) | Submitted May 1, 2026

Keeps cooperative multi-agent MCTS tractable by running surrogate-guided selection over a low-dimensional nonlinear representation using interaction-guided proposal rules. Addresses the exponential blowup in joint-action space that plagues standard MCTS in multi-agent settings.

**Key innovation:** Interaction-guided surrogate selection that makes multi-agent MCTS practical by avoiding exhaustive joint-action expansion.

### 16. Quality-Aware Exploration Budget Allocation for Cooperative MARL

**Authors:** Dahyun Oh, Minhyuk Yoon, H. Jin Kim

**Institution:** Seoul National University

**arXiv:** [2605.01865](https://arxiv.org/abs/2605.01865) | Submitted May 3, 2026

Intrinsic motivation for MARL exploration faces a critical tradeoff — too large a novelty bonus overwhelms task reward (coordination collapse), too small prevents rare strategy discovery. Proposes quality-aware adaptive exploration budget that dynamically adjusts based on coordination quality.

**Key innovation:** Identifies and quantifies the exploration intensity tradeoff in cooperative MARL; provides adaptive mechanism to balance novelty vs. task reward.

### 17. Discovering Multiagent Learning Algorithms with LLMs

**Authors:** Zun Li et al.

**Institution:** Multiple

**arXiv:** [2602.16928](https://arxiv.org/abs/2602.16928) | Submitted February 18, 2026

Uses LLMs to automatically discover novel multiagent learning algorithms in an automated programming framework. Generates and evaluates algorithm candidates that outperform hand-designed baselines in cooperative, competitive, and mixed settings. Bridges LLM code generation with multiagent systems research.

**Key innovation:** LLM-driven automated discovery of multiagent learning algorithms, outperforming human-designed counterparts.

### 18. MARS-DA: Hierarchical RL for Risk-Aware Multi-Agent Bidding

**Authors:** Jiayi Chen, Xuan Zhang, Guiling Wang

**Institution:** New Jersey Institute of Technology

**arXiv:** [2605.03142](https://arxiv.org/abs/2605.03142) | Submitted May 4, 2026

Hierarchical RL framework for day-ahead electricity markets: a Meta-Controller dynamically blends a Safe Agent (reliable DA allocation) and a Speculator Agent (volatile RT arbitrage). Open-sources a high-fidelity gymnasium environment grounded in PJM Interconnection data.

**Key innovation:** First open-source multi-agent RL testbed for two-settlement electricity markets with hierarchical risk management.

---

## 🦾 Applications & Systems

### 19. Claw-Anything: Benchmarking Always-On Personal Assistants

**Authors:** LiberCoders et al.

**Institution:** Multiple

**arXiv:** [2605.26086](https://arxiv.org/abs/2605.26086) | Submitted May 2026

Benchmark for always-on LLM agents with broad access to user's digital world. Simulates months of user activity via multi-round event injection with realistic noise (irrelevant events, conflicting signals). GPT-5.5 achieves only 34.5% pass@1, far below prior benchmarks. Automated data-generation pipeline yielding 2,000 training environments improves base model by 23.7%.

**Key innovation:** First benchmark specifically targeting the "always-on" personal assistant setting with realistic noise and proactive assistance evaluation.

### 20. RadLite: Multi-Task LoRA Fine-Tuning of SLMs for CPU-Deployable Radiology AI

**Authors:** Pankaj Gupta, Kartik Bose

**Institution:** Independent

**arXiv:** [2605.00421](https://arxiv.org/abs/2605.00421) | Submitted May 1, 2026

Trains Qwen2.5-3B and Qwen3-4B on 162K samples spanning 9 radiology tasks using LoRA. Achieves CPU-deployable models (~1.8-2GB quantized) with +53% RADS accuracy, +60% NLI, +89% N-staging over zero-shot. Few-shot prompting hurts fine-tuned model performance, demonstrating LoRA > ICL for specialized domains.

**Key innovation:** Demonstrates that small language models (3-4B) with LoRA can match or exceed large model performance on specialized radiology tasks while running on consumer CPUs.

---

## 📊 Trends & Analysis

This week's arXiv submissions reveal several strong trends:

1. **LLM-as-MLE paradigm maturing** — YouTube's self-evolving recommendation system (2602.10226) shows LLM agents autonomously improving production ML systems. Expect this to expand to search, ads, and ranking pipelines.

2. **Memory and attribution becoming first-class concerns** — MemTrace (2605.28732) and Probabilistic Attribution (2605.21726) both tackle the brittleness of LLM reasoning from complementary angles (system tracing vs. probabilistic decomposition).

3. **Multi-agent sustainability** — MARLIN (2605.13496) addresses the growing energy crisis of LLM inference serving. With 90% of LLM lifecycle energy at inference time, sustainability-aware scheduling is becoming critical.

4. **Generative recommendation goes native** — Fully generative approaches (2605.21987) without separate retrieval are emerging for conversational recommendation. Combined with LLM-driven self-evolution (2602.10226), the traditional DNN-based RecSys stack is being re-architected.

5. **Cooperative MARL still has fundamental challenges** — Papers on exploration budgets (2605.01865), MCTS scaling (2605.00751), and risk-aware bidding (2605.03142) show the community is actively addressing the coordination collapse / rare strategy discovery tradeoff.

6. **Concept interpretability moves beyond single layers** — CAZ (2605.24856) replaces the "best layer" heuristic with a dynamic region-based framework, aligning with the trend toward process-based (not outcome-based) interpretability.
