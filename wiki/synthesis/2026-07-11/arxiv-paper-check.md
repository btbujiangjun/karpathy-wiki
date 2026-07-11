---
title: "arXiv Paper Check — AI & CTR (July 11, 2026)"
type: synthesis
created: 2026-07-11
updated: 2026-07-11
sources: [arxiv.org]
tags: [arxiv, ai, ctr, llm, agents, reasoning, efficiency]
---

# arXiv Paper Check — AI & CTR (July 11, 2026)

**Scan date:** Friday, July 11, 2026  
**Coverage:** cs.AI (Jul 10, ~157 new), cs.LG (Jul 10, ~93 new), cs.IR (Jul 10, ~3 new)  
**Papers curated:** 18

---

## 🧠 LLM Reasoning & Agents

| # | Title | Authors | Key Contribution |
|---|-------|---------|-----------------|
| 1 | **Pyligent: Search, Fail, Recover** (2607.07492) | Beresnev, Makharev, Khalikov, Oseledets, Anokhin | Training framework for correction-aware reasoning. Represents reasoning as validated search over partial solution chains with three actions: continue, finish, backtrack. +72.7pp on hidden graphs, +17-18pp on Sudoku vs gold-only SFT. |
| 2 | **CompactionRL: RL with Context Compaction for Long-Horizon Agents** | (cs.LG trending #1 this week) | RL strategy for long-horizon LLM agents using context compaction to overcome finite context windows. Jointly optimizes task execution and summary generation with novel loss normalization and GAE. |
| 3 | **Danus: Orchestrating Math Reasoning Agents with Fact-Graph Memory** (2607.07467 range) | (cs.AI trending #3) | Orchestration system for LLM math reasoning with shared fact graph as global memory. Main agent for planning, worker agents for parallel search, stateless verifier. |
| 4 | **Ideas Have Genomes** (2607.08758) | Zhou, Yang, Li et al. | Benchmarking scientific lineage reasoning and lineage-grounded idea generation. Traces how ideas evolve through citation networks. |
| 5 | **Can Agents Generalize to the Open World?** (2607.01084) | Lv, Wu, Zhu, Cheng, Guo | Accepted ICML 2026. Unveils fragility of static training in tool-use agents — agents fail to generalize when tool APIs change. |
| 6 | **Game Theory Multi-Agent Hallucination Mitigation** (2607.08403) | Liu, Bie, Wang, Ma, Liu, Li | Game-theoretic framework for multi-agent LLM systems to reduce hallucination through strategic agent interaction. |

---

## 🔍 Multimodal & Vision-Language

| # | Title | Authors | Key Contribution |
|---|-------|---------|-----------------|
| 7 | **SaMer: Object-Evidence Preserving Token Merging** (cs.IR trending #2) | (cs.IR, cs.AI, cs.CL) | Compresses visual tokens into K centroids preserving fine-grained object evidence for late interaction. Object annotations used only during training as merge prior — no detectors at inference. Significantly reduces storage while improving retrieval performance. |
| 8 | **CMDR: Contextual Multimodal Document Retrieval** (cs.IR trending #4) | (cs.IR, cs.AI, cs.CL) | New task + benchmark requiring document context for page retrieval. CMDR-Embed jointly encodes multiple pages for contextual embeddings. |

---

## ⚡ KV Cache & Efficiency

| # | Title | Authors | Key Contribution |
|---|-------|---------|-----------------|
| 9 | **KVpop: Key-Value Cache Compression with Predictive Online Pruning** (cs.CL trending) | - | Learns fixed-budget KV eviction policy by directly supervising keep-or-drop decisions against a future-attention target. Avoids static heuristics that poorly track future token utility. |
| 10 | **SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory** (cs.CL trending) | - | Balances efficiency with faithful context preservation using hierarchical semantic memory. Can recover token-level detail from compressed spans during generation. |
| 11 | **Linear Attention Architectures: Mechanisms, Trade-offs, and Cross-Layer Routing** (2607.07953) | Cerruti, Rieder, Rowlands, Jin, Schlag (ETH Zurich) | Comparative study of softmax vs 4 recurrent linear-attention architectures (DeltaNet, Gated DeltaNet, Kimi Delta Attention, Gated DeltaNet-2) at 350M params / 15B tokens. Introduces Cross-Layer Value Routing (CLVR) — modest but consistent improvement. Kimi Delta Attention with Muon reaches lowest validation loss. |

---

## 📊 CTR Prediction

| # | Title | Authors | Key Contribution |
|---|-------|---------|-----------------|
| 12 | **DiseCTR: Disentangled Interest Network for OOD CTR** (2602.00002, ACM TOIS) | Zheng et al. | Causal perspective on CTR — disentangles multiple user interests via sparse attention + weakly supervised interest disentangler. +0.02 AUC, -13.7% logloss on OOD. Released code. |
| 13 | **CADET: Context-Conditioned Ads CTR** (2602.11410, LinkedIn) | Pardoe, Daftary, Furtado et al. | End-to-end decoder-only transformer for ads CTR deployed at LinkedIn. Handles post-scoring contextual signals, maintains offline-online consistency, scales to industrial workloads. |

> **Note:** No new cs.IR papers specifically on CTR were posted on July 10. CTR highlights above are recent impactful papers that appeared in trending feeds.

---

## 🛡️ Safety & Alignment

| # | Title | Authors | Key Contribution |
|---|-------|---------|-----------------|
| 14 | **Overthinking** (ICML 2026) | - | Reasoning amplification in LLMs surfaces harmful secrets 10× more frequently. Shows test-time compute scaling has safety implications. |
| 15 | **CoT Persuasion Attacks** | - | Attacker with access to chain-of-thought monitoring increases harm success by 9.5%. Raises concerns about reasoning transparency vs safety tradeoff. |
| 16 | **Agreement ≠ Accuracy** | - | Frontier models agree with each other ρ 0.20–0.59 but are wrong 48% of the time when they agree. Challenges consensus-based evaluation. |

---

## 🔬 Scientific AI

| # | Title | Authors | Key Contribution |
|---|-------|---------|-----------------|
| 17 | **Agentic Verifiable Rules for Reaction Classification** (2607.01061) | Armstrong, Dobbelaere, Olikauskas et al. (EPFL/Schwaller group) | Self-expanding deterministic rule sets for chemical reaction classification. LLM agents generate and verify rules autonomously. |
| 18 | **PraMem: Practice-derived Experiential Memory for Long-horizon Behavior Prediction** | - | Addresses LLM limitations in long-horizon behavior prediction via structured experiential memory, moving beyond context-compression paradigm. |

---

## Key Themes

1. **Reasoning recovery is a first-class training objective** — Pyligent's backtrack/continue/finish framework and CompactionRL's context compaction both address the fundamental challenge of long-horizon agent failures.
2. **KV cache research intensifying** — Three papers (KVpop, SeKV, Linear Attention) tackle the same bottleneck from different angles: learned eviction, hierarchical semantic memory, and architectural alternatives.
3. **Safety implications of test-time compute scaling** — Overthinking and CoT persuasion attacks show that making models "think harder" has unintended safety consequences.
4. **Token merging for vision-language** — SaMer brings object-aware evidence preservation to VL retrieval, potentially impacting multi-modal CTR models.
5. **Agent generalization remains fragile** — ICML 2026 paper shows static training produces brittle tool-use agents, relevant for production agent deployment.

---

*Generated by arxiv-paper-check scheduled job. Data from arXiv cs.AI, cs.LG, cs.IR, cs.CL listings (Jul 10, 2026).*
