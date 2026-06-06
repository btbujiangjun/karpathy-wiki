---
title: "arXiv Daily Digest — 2026-05-26"
type: synthesis
created: 2026-05-26
updated: 2026-05-26
sources: []
tags: [arxiv, daily-digest, llm, reasoning, ctr, recommender-systems, interpretability, rl, agents]
---

# arXiv Daily Digest — 2026-05-26

> Papers submitted Tue 26 May 2026. Categories: cs.AI, cs.LG, cs.IR, cs.CL.
> ~1,500 new entries scanned; top picks below.

---

## 1. Large Language Models & Reasoning

### 1.1 Language Models Need Sleep
- **Authors:** Sangyun Lee, Sean McLeish, Tom Goldstein, Giulia Fanti
- **Affiliation:** —
- **arXiv:** 2605.26099
- **Abstract:** Proposes a biologically-inspired "sleep" consolidation mechanism for LLMs. The model periodically converts recent context into persistent fast weights inside SSM blocks, clears the KV cache, and runs offline recurrent passes during sleep. Shifts computation from inference-time to sleep-time, improving long-context reasoning on tasks where standard transformers and SSM-attention hybrids fail.
- **Key Contributions:**
  - Novel sleep-wake architecture combining SSM consolidation with transformer wake-time operation
  - Reduces inference-time memory pressure by deferring consolidation to offline periods
  - Improved long-context reasoning on challenging benchmarks
- **Link:** https://arxiv.org/abs/2605.26099

### 1.2 How Much Thinking is Enough? Quantifying and Understanding Redundancy in LLM Reasoning
- **Authors:** Zhiyuan Zhai, Xinkai You, Wenjing Yan, Xin Wang
- **Affiliation:** —
- **arXiv:** 2605.23926
- **Abstract:** Formalizes "reasoning redundancy" and quantifies it across four frontier reasoning models. Finds 61–93% of chain-of-thought steps are unnecessary (median critical prefix = 1 step in 6 of 8 conditions). Proves that over-thinking is a structural consequence of length-agnostic outcome rewards — mathematically guaranteed regardless of RL algorithm, base model, or distillation.
- **Key Contributions:**
  - First formalization and measurement of reasoning redundancy in LLMs
  - Proof that over-thinking is an inherent property of current training paradigms
  - Immediate practical implications for reducing inference cost in reasoning models
- **Link:** https://arxiv.org/abs/2605.23926

### 1.3 Iterative Finetuning is Mostly Idempotent
- **Authors:** Zephaniah Roe, Jack Sanderson, Dang Nguyen, Julian Huang, Todd Nief, Aryan Shrivastava, Chenhao Tan, Ari Holtzman
- **Affiliation:** —
- **arXiv:** 2605.01130
- **Abstract:** Investigates the effects of repeated fine-tuning cycles on LLMs. Finds that iterative fine-tuning often converges to similar performance regardless of intermediate checkpoints, suggesting diminishing returns from multi-turn alignment procedures.
- **Key Contributions:**
  - Empirically demonstrates idempotent behavior in iterative fine-tuning
  - Suggests practical limits on gains from repeated alignment cycles
- **Link:** https://arxiv.org/abs/2605.01130

### 1.4 Arithmetic in the Wild: Llama Uses Base-10 Addition to Reason About Cyclic Concepts
- **Authors:** Sheridan Feucht, Tal Haklay, Usha Bhalla, Daniel Wurgaft, Can Rager, Raphaël Sarfati, Jack Merullo, Thomas McGrath, Owen Lewis, Ekdeep Singh Lubana, Thomas Fel, Atticus Geiger
- **Affiliation:** —
- **arXiv:** 2605.01148
- **Abstract:** Mechanistic interpretability study revealing that Llama models implement base-10 addition circuits internally, demonstrating structured arithmetic reasoning rather than simple pattern matching.
- **Link:** https://arxiv.org/abs/2605.01148

---

## 2. Interpretability & Formal Verification

### 2.1 Verified SHAP: Provable Bounds for Exact Shapley Values of Neural Networks
- **Authors:** David Boetius, Shahaf Bassan, Guy Katz, Stefan Leue, Tobias Sutter
- **Affiliation:** — (ICML 2026)
- **arXiv:** 2605.24084
- **Abstract:** First algorithm to compute provably tight bounds on exact SHAP values for neural networks using neural network verification techniques. Scales to orders-of-magnitude larger search spaces than prior exact methods.
- **Key Contributions:**
  - First exact SHAP computation method using verification
  - Provably tight lower and upper bounds
  - Surpasses prior exact methods in scalability by orders of magnitude
- **Venue:** ICML 2026
- **Link:** https://arxiv.org/abs/2605.24084

### 2.2 Feature Lottery? A Bifurcation Theory of Concept Emergence
- **Authors:** Fuming Yang
- **Affiliation:** —
- **arXiv:** 2605.24057
- **Abstract:** Derives a universal, label-free phase coordinate β(t)/β_c(t) that detects when neural networks acquire structured representations in real time. Validated on SAEs (Pythia), SSL (CIFAR), and grokking. At only 5% of training, a feature's terminal interpretability is already predictable — top-decile early atoms achieve 12× baseline purity.
- **Key Contributions:**
  - Unified dynamical systems theory for concept emergence in neural nets
  - Real-time detection of representation learning milestones
  - Early prediction of feature interpretability in SAE training
- **Link:** https://arxiv.org/abs/2605.24057

### 2.3 Towards Verifiable Transformers: Solver-Checkable Circuit Explanations
- **Authors:** Neel Somani
- **Affiliation:** —
- **arXiv:** 2605.24033
- **Abstract:** Framework for converting task-localized transformer circuits into bounded, solver-checkable claims. Direct verification via SMT encoding of extracted circuits; surrogate-mediated verification for hard-to-encode operators. Demonstrates on GPT-style architecture with verified projected functional equivalence and edge necessity.
- **Key Contributions:**
  - Formal verification framework for mechanistic interpretability claims
  - Direct + surrogate-mediated SMT verification of transformer circuits
  - Counterexample generation when circuits fail verification
- **Link:** https://arxiv.org/abs/2605.24033

---

## 3. AI Safety, Agents & Evaluation

### 3.1 Automated Benchmark Auditing for AI Agents and Large Language Models
- **Authors:** Junlin Wang, Federico Bianchi, Shang Zhu, Fan Nie, Yongchan Kwon, Bhuwan Dhingra, James Zou
- **Affiliation:** —
- **arXiv:** 2605.26079
- **Abstract:** Agentic framework (ABA) that systematically audits 168 benchmarks across 9 domains. Finds critical issues (ambiguous design, incorrect ground truth, hidden dependencies) in >25.7% of tasks. Removing problematic tasks shifts model rankings and boosts SWE-bench Verified by +9.9% and Terminal-Bench 2 by +9.6%.
- **Key Contributions:**
  - Large-scale systematic audit of LLM/agent benchmarks
  - >25% of benchmark tasks have critical flaws
  - Removing flawed tasks significantly changes model rankings
- **Link:** https://arxiv.org/abs/2605.26079

### 3.2 Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning
- **Authors:** Nesreen K. Ahmed, Nima Nafisi
- **Affiliation:** —
- **arXiv:** 2605.24216
- **Abstract:** Frames agent monitoring as a Theory-of-Mind problem — the monitor infers beliefs, intent hypotheses, and goal alignment from trajectories. Uses a Reason-Verify-Refine pipeline with persistent semantic guardrail memory. Outperforms ensemble methods on SHADE-Arena benchmarks.
- **Key Contributions:**
  - Novel ToM-inspired agent monitoring framework
  - Persistent semantic guardrail memory across episodes
  - Strong results on adversarial agent monitoring benchmarks
- **Link:** https://arxiv.org/abs/2605.24216

### 3.3 To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling
- **Authors:** Qinyuan Wu, Soumi Das, Mahsa Amani, Arijit Nag, Seungeon Lee, Krishna P. Gummadi, Abhilasha Ravichander, Muhammad Bilal Zafar
- **Affiliation:** —
- **arXiv:** 2605.00737
- **Abstract:** Systematic framework for evaluating when LLMs should or should not invoke tools. Provides optimization strategies for tool-calling decisions in agentic workflows.
- **Link:** https://arxiv.org/abs/2605.00737

---

## 4. Scientific Discovery & Applications

### 4.1 LLM-AutoSciLab: Closed-Loop Scientific Discovery via Active Experimentation with LLMs
- **Authors:** Sanchit Kabra, Nikhil Abhyankar, Saaketh Desai, Prasad Iyer, Chandan K Reddy
- **Affiliation:** —
- **arXiv:** 2605.24043
- **Abstract:** Closed-loop framework where LLMs generate hypotheses, select informative experiments adaptively, and refine mechanisms. Introduces ActiveSciBench (enzyme kinetics + gene regulatory networks). Achieves 2–5× sample efficiency over baselines.
- **Key Contributions:**
  - Active experimentation paradigm for LLM-driven science
  - New benchmark (ActiveSciBench) for closed-loop discovery
  - 2–5× sample efficiency vs static fitting baselines
- **Link:** https://arxiv.org/abs/2605.24043

### 4.2 Algometrics: Forecasting Under Algorithmic Feedback
- **Authors:** Marc Schmitt
- **Affiliation:** —
- **arXiv:** 2605.23978
- **Abstract:** Formal framework for time series where the forecasting algorithm itself changes the data-generating process (e.g., algorithmic trading, recommender systems). Proves three theorems: (1) deployment risk is not identifiable from passive historical data, (2) historical model rankings invert under crowding, (3) randomized actions identify short-horizon feedback.
- **Key Contributions:**
  - Foundational theory for feedback-aware forecasting
  - Non-identifiability of deployment risk from passive data
  - Proof that model rankings can invert under adoption
- **Link:** https://arxiv.org/abs/2605.23978

---

## 5. CTR Prediction & Recommendation Systems

### 5.1 Generative Long-term User Interest Modeling for CTR Prediction (GenLI)
- **Authors:** Jiangli Shao, Kaifu Zheng, Hao Fang, Huimu Ye, Zhiwei Liu, Bo Zhang, Shu Han, Xingxing Wang
- **Affiliation:** —
- **arXiv:** 2605.15905
- **Abstract:** GenLI replaces matching-based behavioral retrieval in CTR with a generative interest approach — multiple target-independent interest distributions with O(1) retrieval complexity, avoiding the information loss and latency of two-stage matching frameworks.
- **Key Contributions:**
  - Generative interest modeling replaces matching-based retrieval
  - O(1) retrieval complexity vs traditional two-stage systems
  - Addresses the core efficiency bottleneck in industrial CTR systems
- **Link:** https://arxiv.org/abs/2605.15905

### 5.2 Valley3: Scaling Omni Foundation Models for E-commerce
- **Authors:** Zeyu Chen, Guanghao Zhou, Qixiang Yin, Ziwang Zhao, Huanjin Yao, Pengjiu Xia, Min Yang, Cen Chen, Minghui Qiu
- **Affiliation:** —
- **arXiv:** 2605.01278
- **Abstract:** Vally3 foundation model designed for e-commerce, integrating multimodal understanding across product descriptions, images, and user behavior for improved recommendation and CTR prediction.
- **Link:** https://arxiv.org/abs/2605.01278

> *Note: No new CTR-specific papers were posted in the last 24 hours. The most recent CTR paper is GenLI (2605.15905, May 15).*

---

## Highlights Summary

| Paper | Venue / Status | Theme |
|-------|---------------|-------|
| Language Models Need Sleep | new | Bio-inspired architecture |
| How Much Thinking is Enough | new | Reasoning redundancy |
| Verified SHAP | ICML 2026 | Formal verification for XAI |
| Automated Benchmark Auditing | new | Benchmark quality |
| Agent-ToM | new | Agent safety |
| LLM-AutoSciLab | new | AI for science |
| Algometrics | new | Feedback-aware forecasting |
| GenLI | May 15 | CTR / generative interest |
| Feature Lottery (Bifurcation Theory) | new | Interpretability theory |
