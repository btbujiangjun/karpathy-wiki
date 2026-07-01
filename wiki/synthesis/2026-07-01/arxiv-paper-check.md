---
title: "arXiv Paper Check — AI & CTR (July 1, 2026)"
type: synthesis
created: 2026-07-01
updated: 2026-07-01
sources: []
tags: [arxiv, ai, ctr, paper-check, agents, llm, recsys]
---

# arXiv Paper Check — AI & CTR (July 1, 2026)

> Coverage: Latest submissions through Fri, Jun 26, 2026 (cs.AI: 277 entries, 74 new; cs.IR: 28 entries, 11 new; cs.LG: 249 entries, 95 new). Plus late-breaking Jun 30 paper.

## Top AI Picks

### 1. Agents-A1: Scaling the Horizon, Not the Parameters
- **arXiv**: [2606.30616](https://arxiv.org/abs/2606.30616) (Jun 30, 2026)
- **Key insight**: A 35B MoE agentic model that reaches trillion-parameter-level performance by scaling agent horizon (45K avg trajectory tokens) rather than model parameters. Three-stage recipe: full-domain SFT → domain teacher models → multi-teacher domain-routed on-policy distillation.
- **Results**: Outperforms DeepSeek-V4-pro, Kimi-K2.6, and GPT-5.5 on SEAL-0 (56.4), IFBench (80.6), HiPhO (46.4), FrontierScience-Olympiad (79.0). Competitive on BrowseComp (75.5), HLE with tools (47.6).
- **Significance**: Demonstrates that agentic capability scaling through trajectory length and heterogeneity can substitute for raw parameter count.

### 2. AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems
- **arXiv**: [2606.26859](https://arxiv.org/abs/2606.26859) (Jun 25, 2026)
- **Authors**: Changxin Lao, Fei Pan, Kun Gai, Ruiming Tang et al. (Kuaishou)
- **Key insight**: Multi-agent production system that autonomously generates, implements, evaluates, and learns from recommendation experiments in a closed loop. Brainstorm → Develop → Evaluate → Harness Evolution (SGPO).
- **Results**: 3-week Kuaishou deployment: 3 workers turned 374 ideas into 10 launchable rollouts, 8× concurrency, 3.7× business value vs human engineer, 0.561% user app-time gain, >RMB 100M annualized revenue.
- **Significance**: First production deployment of agent-driven, self-evolving RecSys iteration. Points toward compounding-returns R&D model.

### 3. KARLA: Knowledge-base Augmented Retrieval for Language Models
- **arXiv**: [2606.26807](https://arxiv.org/abs/2606.26807) (Jun 25)
- **Authors**: Francois Crespin, Fabian M. Suchanek, Nils Holzenberger
- **Key insight**: Trains LLM to produce special tokens that trigger knowledge base queries during generation. Enables factual updates without retraining, traceability, and smaller models matching larger accuracy.
- **Significance**: Practical approach to grounding LLM outputs in updatable KBs — addresses hallucination and knowledge staleness simultaneously.

### 4. On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
- **arXiv**: [2606.26091](https://arxiv.org/abs/2606.26091) (Jun 24)
- **Key insight**: Self-distillation with correct demonstrations amplifies existing probability gaps, reducing rollout diversity. Pass@k curves flatten. Theoretical analysis shows it tilts distribution by conditional mutual information, unlike optimal RL.
- **Significance**: Important cautionary result: self-distillation gains come at a hidden diversity cost that hurts OOD generalization.

### 5. Tmax: A Simple Recipe for Terminal Agents
- **arXiv**: [2606.23321](https://arxiv.org/abs/2606.23321) (Jun 22)
- **Authors**: Hamish Ivison et al.
- **Key insight**: Open RL recipe achieving 27% on Terminal-Bench 2.0 with only 9B parameters, outperforming much larger prior models. Novel data generation taxonomy with difficulty control, personas, and verifier diversification. 2.5× larger terminal dataset released.
- **Significance**: Strong open baseline for terminal agent RL training.

### 6. Reasoning Quality Emerges Early: Data Curation for Reasoning Models
- **arXiv**: [2606.26797](https://arxiv.org/abs/2606.26797) (Jun 25)
- **Authors**: Hongyi Henry Jin, Wenhan Yang, Meysam Ghaffari, Carlos Morato, Baharan Mirzasoleiman
- **Key insight**: Difficult problems can be detected from first 100 reasoning tokens at a perturbed checkpoint. Loss patterns over first 1k tokens across perturbed checkpoints predict example quality. 91% more token efficient than existing curation.
- **Significance**: Enables data-quality-driven SFT curation without expensive teacher models.

### 7. Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators
- **arXiv**: [2606.26294](https://arxiv.org/abs/2606.26294) (Jun 24)
- **Key insight**: Makes evaluation part of the recursive self-improvement loop with non-stationary utilities. Co-evolved writers reach 1.78–1.86× higher acceptance rates. Corrects AI-reviewer bias that over-accepts AI-generated papers at 1.91× human rate.
- **Significance**: Practical framework for adversarial, non-stationary self-improvement — addresses evaluation becoming stale as agents improve.

### 8. Abstract Representational Geometry Supports Inference in LLMs
- **arXiv**: [2606.23345](https://arxiv.org/abs/2606.23345) (Jun 22)
- **Key insight**: LLMs form hippocampal-like abstract representational geometry during inference. Lower layers encode stimulus identity, higher layers form functional bands for abstract context. Geometric regularization improves generalizable inference.
- **Significance**: Mechanistic alignment between LLM internals and neuroscience — sparse orthogonal manifolds as a general principle for reasoning.

## CTR & Recommendation Picks

### 9. DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction
- **arXiv**: [2606.07980](https://arxiv.org/abs/2606.07980)
- **Key insight**: Dual-path residual (Identity + Block Attention Residual) with vector-wise gating. SiLU-based Pointwise AttnRes enables parallel multi-interest patterns. 1.66× steeper compute–AUC scaling law than OneTrans. 8-layer DeRes matches 16-layer OneTrans.
- **Results**: +0.32% AUC at <5% FLOPs on 331M-interaction industrial dataset. Outperforms 12 baselines.
- **Significance**: Residual connections identified as bottleneck in Transformer-based CTR — architectural fix yields 2× compute savings.

### 10. AgentX (already covered above — also CTR/RecSys pick)

## Late-Breaking — Jun 30

### 11. Agents-A1 (above, #1)

### 12. Think Fast: Estimating No-CoT Task-Completion Time Horizons
- **arXiv**: [2606.07157](https://arxiv.org/abs/2606.07157) (Jun 5)
- **Key insight**: No-CoT 50% task-completion time horizon of frontier models has doubled yearly over 6 years. GPT-5.5 reaches 3+ minutes. Projections exceed 7 minutes by 2028, 25 minutes by 2030. If models can reason internally without explicit CoT, safety oversight via CoT monitoring is undermined.
- **Significance**: Quantifies the erosion of CoT-based safety oversight.

## Key Themes

1. **Agent-horizon scaling** — Agents-A1 shows that scaling trajectory length (45K tokens) and skill heterogeneity can substitute for raw parameter scaling (35B → 1T performance).
2. **Self-evolving systems** — AgentX and Red Queen Gödel Machine both demonstrate closed-loop self-improvement where agents modify their own evaluation/iteration pipeline.
3. **Hidden costs of self-distillation** — Diversity loss quantified; data quality early detection proposed as alternative.
4. **LLM–neuroscience convergence** — Abstract representational geometry provides mechanistic basis for LLM inference.
5. **CTR scaling law refinement** — DeRes shows residual connections as the bottleneck; dual-path design achieves 2× compute savings.
6. **CoT safety erosion** — No-CoT reasoning capabilities are improving exponentially, threatening CoT-based oversight.
