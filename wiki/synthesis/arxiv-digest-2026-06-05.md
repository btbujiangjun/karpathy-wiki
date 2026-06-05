---
title: "arXiv Digest — AI & CTR (June 5, 2026)"
type: synthesis
created: 2026-06-05
updated: 2026-06-05
sources: []
tags: [arxiv, digest, ai, ctr, recommendation, scaling-laws, agents, benchmarks]
---

# arXiv Digest — AI & CTR (June 5, 2026)

Surveyed: cs.AI (418 entries), cs.IR (28 entries), cs.LG (376 entries) from Friday, 5 June 2026.

---

## Top Picks

### 1. Scaling Laws for Behavioral Foundation Models over User Event Sequences (`2606.05257`)
**Rickard Brüel Gabrielsson**

~600 runs on real interaction data, $10^{15}$–$10^{19}$ FLOPs. A small embedder (~2% of parameters) is compute-optimal at every budget. The evaluation metric is itself part of the scaling law — changing it changes the compute-optimal recipe. **Essential reading** for anyone building foundation models for recommendation/payments/commerce.

### 2. Agents' Last Exam (ALE) (`2606.05405`)
**Yiyou Sun et al. (250+ industry experts)**

Benchmark for long-horizon, economically valuable real-world tasks. 55 subfields, 13 industry clusters, 1K+ tasks mapped to O\*NET/SOC 2018. Current pass rate on hardest tier: **2.6%**. Designed as a living benchmark to close the gap between benchmark success and GDP-relevant impact.

### 3. The Evaluation Blind Spot: A Stereological Theory of Benchmark Coverage (`2606.05169`)
**Jason Z Wang**

Rigorous theory showing benchmark effective dimensionality in [2.86, 4.80] on Open LLM v2/LiveBench. Structural blind spot exceeds runner-up score gap by **two orders of magnitude**. 92% of trials swap top-1 on random held-out split. A submodular algorithm finds a stable core of 4 benchmarks — 7 of 12 suffice for 90% coverage. **Foundational critique of benchmark culture.**

### 4. Trust, But Don't Verify: Epistemic Blind Spots in LLM Source Evaluation (`2606.05403`)
**Rohan N. Pradhan, Steve Goley**

Models detect fabricated statistics (0.76–1.00 accuracy in isolation) but **don't recruit this capability** during multi-source synthesis. Mechanistic analysis: numeric-validity signals suppressed to chance during synthesis. Prompt mitigations produce blanket skepticism, not selective discernment.

### 5. State Commitment Learning / CERL (`2606.05201`)
**Fei Ding et al.**

Reasoning LMs don't distinguish computation tokens from persistent state. Counterfactual Erasure RL: trains models to distinguish erasable scratch work from committed state. Reduces answer dependence on hidden thoughts without sacrificing accuracy.

---

## CTR / Recommendation / Ranking

| Paper | arXiv | Key Contribution |
|-------|-------|-----------------|
| OneReason | `2606.06260` | Think-before-answer reasoning for generative recommendation (Kuaishou/OneRec team). Three-level cognition-enhanced CoT addresses why thinking mode hasn't helped rec models. |
| ANCHOR | `2606.05621` | Paradigm shift in recommendation denoising: proactively creates labeled noisy interactions via LLM-as-User simulation → supervised denoising instead of heuristic filtering. |
| PHKT | `2606.05537` | Personalized Hypergraph + KAN-Transformer for multi-behavior sequential recommendation. Outperforms 9 baselines on Tmall, RetailRocket, IJCAI. |
| Shallow-RHS (Tubi) | `2606.06225` | Inductive graph-completion for cold-start recommendation. Intentionally shallow content tower forces learning from intrinsic features only. Online improvements at Tubi. |
| BAHSD | `2606.03091` | Black-box adaptive distillation for sequential recommendation. Multi-scale consistency probing. Up to 4.98% gain over teacher, 80%+ improvement on tail users. |
| ColBERTSaR | `2606.05568` | ColBERT index turned into true inverted index via embedding quantization. 50–70% smaller than PLAID while retaining retrieval effectiveness. |
| SAGE (LinkedIn) | `2602.07840` | Production framework at LinkedIn: LLM Surrogate Judge with teacher-student distillation at 92× cost reduction. Drove 0.25% lift in LinkedIn DAU. |

---

## AI / LLM: Scaling, Training, Reasoning, Alignment

| Paper | arXiv | Key Contribution |
|-------|-------|-----------------|
| ERRORQUAKE | `2606.05170` | Heavy-tailed error severity distributions in open-weight LLMs. Non-Reducibility Theorem: severity profile and error rate are informationally non-redundant (1.56 bits). |
| Safety Paradox | `2606.05614` | Posterior Attack: single-query jailbreak exploiting a model's own safety classifier. Models with superior safety judgment are disproportionately more vulnerable. Tested on 30 open-weight LLMs + GPT-5, Claude 4.6. |
| SHALA-LLM | `2606.05376` | RL framework (Picard group) for learning from annotator distributions. Reduces JSD by up to 62.1% on ChaosNLI while improving F1 by up to 16.7%. |
| PPI Ranking Evaluation | `2606.05308` | Bias-corrected ranking metrics via Prediction-Powered Inference. +407 bps daily sales in production A/B test. |
| PJ-RoPE | `2606.05345` | Unifies RoPE Fourier phase, Jordan-RoPE finite jets, and ALiBi affine recency into a single learnable relative-position space. |
| SAGE-PTQ | `2606.05429` | Ultra-low-bit LLM quantization (1.03 avg weight bits, 0.004 scaling bits). LLaMA-3-8B: 6.74 perplexity vs 55.8 for BiLLM, <50% GPU memory. |

---

## Agents & Multi-Agent Systems

| Paper | arXiv | Key Contribution |
|-------|-------|-----------------|
| SentinelBench | `2606.05342` | Microsoft Research: 100 monitoring tasks across 10 synthetic web environments. Default continuous-action model is wrong for monitoring — sustained attention beats constant action. |
| Agentic Monte Carlo (AMC) | `2606.05296` | Samples from optimal policy of black-box LLM agents via SMC. No parameter updates. Outperforms GRPO on AgentGym as test-time compute scales. **ICML 2026** |
| AdaMEM | `2606.05684` | Test-time adaptive memory: long-term trajectory + dynamic short-term strategy. Up to 13% gain on ALFWorld, 11% on WebShop. New scaling dimension for agentic memory. **ICML 2026** |
| Coding with "Enemy" | `2606.05647` | First large-scale human study: 94% of developers fail to detect agent sabotage. Safety monitor helps but 56% still accept malicious code. |
| PACT | `2606.05304` | Protocolized Action-state Communication — treats inter-agent communication as state-update. Lifts OpenHands' resolve rate at -10% tokens/resolved. |
| DiG-Plan | `2606.05728` | Diffusion guidance for tool-graph planning. Masked denoising raises Pass@10 from 0.320 to 0.943. **IJCAI-ECAI 2026** |
| Continual Learning Bench | `2606.05661` | First difficult, expert-validated benchmark for measuring whether LLM-based systems genuinely improve with experience. Naive ICL outperforms dedicated memory systems. |

---

## Key Themes

1. **Scaling laws for behavioral/recommendation models** — the evaluation metric is part of the law
2. **Brain-inference-time reasoning** for generative recommendation (OneReason)
3. **Agent benchmarks going real-world**: ALE (economically valuable tasks), SentinelBench (monitoring), CL-Bench (continual learning)
4. **Benchmark evaluation crisis**: theoretical proof that blind spots are structurally inevitable
5. **Black-box agent optimization**: AMC and AdaMEM show you don't need weight access
6. **LLM safety paradoxes**: better safety judgment → more vulnerable to posterior attack; models can detect lies but don't use the ability
7. **Recommendation denoising as supervised learning** (ANCHOR paradigm shift)
