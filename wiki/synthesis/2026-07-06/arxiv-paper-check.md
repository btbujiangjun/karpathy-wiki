---
title: "arXiv Paper Check — AI & CTR (July 6, 2026)"
type: synthesis
created: 2026-07-06
updated: 2026-07-06
sources: []
tags: [arxiv, ai, ctr, paper-scan, july-2026]
---

# arXiv Paper Check — AI & CTR (July 6, 2026)

> New listings for **Friday, 3 July 2026** (announced Monday, July 6). Scanned **cs.AI** (353 entries), **cs.IR** (23 entries) with cross-list filtering.

## LLM Training, Reasoning & Alignment

| Paper | ID | Key Contribution |
|-------|-----|-----------------|
| **Procedural Memory Distillation (PMD)** | 2607.01480 | Cross-episode procedural memory distillation for self-improving LMs; +3.8–13.6% over SDPO on SCIKNOWEVAL and LIVECODEBENCH |
| **DemoPSD: Disagreement-Modulated Policy Self-Distillation** | 2607.02502 | On-policy self-distillation alternative to GRPO; disagreement modulation improves reasoning distillation |
| **Scaling Trends for Lie Detector Oversight (SOLiD)** | 2607.01567 | Scaling lie detector oversight in preference learning; deception 34%→14% at 405B scale |
| **Staleness-Learning Rate Scaling Laws for Asynchronous RLHF** | 2607.01083 | Study of stale rollout effects in async GRPO; behavior policy analysis for throughput-scaling |
| **Scaling with Confidence: Calibrating LLM Confidence for Adaptive Test-Time Scaling** | 2607.01612 | RL reward design for confidence calibration; adaptive test-time compute scaling |
| **ReContext: Recursive Evidence Replay** | 2607.02509 | Training-free long-context reasoning via model-internal relevance signals; best avg rank on Qwen3/Llama3-8B across 8 datasets |
| **LACUNA: LLM Unlearning Localization Testbed** | 2607.02513 | First parameter-level unlearning benchmark with ground-truth localization; existing methods imprecise against resurfacing attacks |
| **Reasoning effort, not tool access, buys first-try reliability** | 2607.02436 | Observational study: xHigh reasoning effort achieves 89% first-try success in agentic code gen |
| **Active Few-Shot Learning for LLM Specialization** | 2607.02404 | Identifying most valuable unlabeled samples for few-shot adaptation; reduces annotation cost |
| **Neuron-Aware Data Selection for Annotation-Free LLM Self-Distillation** | 2607.02460 | Neuron-level data selection for self-distillation without human labels |

## LLM Agents & Tool Use

| Paper | ID | Key Contribution |
|-------|-----|-----------------|
| **Beyond Next-Token Prediction: RLVR for Tool-Use Agents** | 2607.01465 | RLVR proof of concept on Atlassian enterprise workflows; tool-use agents via RL |
| **World Feedback for Clinical Agents** | 2607.01470 | Diagnosing RL in FHIR environments; capability ceiling (10/20 task types at 0%) and format-knowledge barrier |
| **What LLM Agents Say When No One Is Watching** | 2607.02507 | Dual-channel debate: public-OTR divergence rises from 3%→40% in alignment-inducing settings |
| **Janus: User-Involved Agentic Permission Management** | 2607.01510 | Playground for agent permission management; user-in-the-loop access control |
| **ClawArena-Team: Subagent Orchestration Benchmark** | 2606.31174 | Benchmark for subagent delegation and dynamic workflows |
| **Distributed Attacks in Persistent-State AI Control** | 2607.02514 | Gradual attacks across PRs evade monitors; 4-monitor ensemble reduces evasion 93%→47% |
| **Program-as-Weights (PAW)** | 2607.02512 | 0.6B fuzzy function compiler matches 32B prompting; 50× less memory, 30 tok/s on M3 MacBook |

## Efficient Architectures & Inference

| Paper | ID | Key Contribution |
|-------|-----|-----------------|
| **Wiola Architecture for Efficient SLMs** | 2607.01394 | Fully original SLM architecture from first principles; no structural lineage to GPT/LLaMA/Mistral |
| **Discrete Diffusion Language Models for Radiology** | 2607.01436 | Diffusion LMs for interactive radiology report drafting; bidirectional denoising alternative to AR |
| **OrbitQuant: Data-Agnostic Quantization for DiTs** | 2607.02461 | W2A4 post-training quantization for diffusion transformers |
| **Hawk: Hardware-Aware NPU Kernel Generation** | 2607.01590 | Automated high-performance kernel generation for NPUs |

## Recommendation & CTR

| Paper | ID | Key Contribution |
|-------|-----|-----------------|
| **CoPersona: Collaborative Persona Graphs** | 2607.01485 | Collaborative persona graphs for robust LLM personalization; addresses sparse/sparse user history |
| **IntentTune: Query Intent Resolution for E-Commerce** | 2607.01530 | User demand + personalization to resolve "unknown" query intents; user-specific > population signals |
| **Bi-NAS: Bi-Level NAS for RecSys Explanations** | 2607.01387 | Neural architecture search for personalized explanation generation in RecSys |
| **Monosemanticity in Recommender Systems** | 2606.29341 | Sparse autoencoders for interpreting embedding dimensions in matrix factorization |
| **GR2 Technical Report** | 2606.31984 | Generative reasoning re-ranker for industrial recommendation funnels |
| **Planning over Matrix-Factorization MDPs** | 2607.02115 | Customer journey as chain of recommendations; MF-MDP for candidate generation |
| **Optimizing RAG Rerankers with RL** | 2607.02091 | LLM feedback via RL for reranker optimization; bridges gap between relevance and generation |

## Other Notable Papers

| Paper | ID | Key Contribution |
|-------|-----|-----------------|
| **Auto-FL-Research** | 2607.01366 | Agentic search for federated learning algorithms; NVIDIA agentic FL research |
| **PACE: Neuro-Symbolic Counterfactual Explanations** | 2607.01306 | Plausible and actionable counterfactual explanations with neuro-symbolic framework |
| **TestEvo-Bench** | 2607.02469 | Live benchmark for test-code co-evolution; 746+509 tasks |
| **The Agentic Garden of Forking Paths** | 2607.01507 | m-value framework for analysis credibility in agentic research |
| **Diverse Evidence, Better Forecasts** | 2607.01661 | Multi-agent deliberation under information asymmetry; 12–18% Brier improvement |
| **EO-Agents: EO Hypothesis Generation** | 2607.01584 | Three-agent LLM pipeline for earth observation hypothesis generation |
| **Beyond Adam: SOAP and Muon for MLIP Training** | 2607.02499 | Optimizer advances for machine learning interatomic potentials |
| **OPINE-World: Programmatic World Modeling** | 2607.01531 | Ontology-error-prioritized interactive exploration for world model learning |
| **Learning to Move Before Learning to Do** | 2607.02466 | VLA task-agnostic pretraining; matches 1M+ demos (ICML 2026) |

## Key Themes

1. **Procedural memory as training paradigm** — PMD shows cross-episode signals can be captured and distilled; co-evolution of memory and policy drives gains
2. **On-policy self-distillation maturing** — DemoPSD as GRPO alternative; disagreement modulation reduces reward hacking
3. **Agent safety in persistent codebases** — Distributed attacks across PRs evade monitors; need for stateful monitoring
4. **RLVR for enterprise tool-use** — Beyond synthetic benchmarks: Atlassian workflows, clinical FHIR environments
5. **LLM unlearning needs parameter localization** — LACUNA reveals existing methods imprecise; simple gradient method works when localization succeeds
6. **Agent social structure matters** — Public-OTR divergence in multi-agent debates; emergent objectives beyond explicit prompts
7. **Fuzzy function compilation** — PAW compiles NL spec → compact neural artifact; 50× memory savings over API-based approaches
8. **LLM+RecSys convergence** — CoPersona, IntentTune, Bi-NAS, GR2 all leverage LLM capabilities for recommendation
9. **Interpretability for RecSys** — Monosemanticity analysis applied to recommender embeddings
10. **Reasoning effort > tool access** — High reasoning effort dominates reliability in agentic code generation
