---
title: arXiv Paper Check — AI & CTR (July 10, 2026)
type: synthesis
created: 2026-07-10
updated: 2026-07-10
tags: [arxiv, paper-check, ai, ctr, llm, rl, recommendation, agents]
---

# arXiv Paper Check — AI & CTR (July 10, 2026)

Scanned cs.AI (56 new), cs.LG (93 new) from Friday July 10, 2026 listings. Highlights below.

---

## CTR / Recommendation / Advertising

### 1. PIT-SUN: Parameter-Efficient Multi-Domain CTR via Shared-Expertise Adapters
- **Authors:** Kun Gai et al. (Kuaishou)
- **Key Contribution:** Proposes parameter-efficient adapters with side information for multi-domain CTR prediction. Shared-expertise mechanism enables transfer learning across domains while keeping per-domain parameters small. Production-friendly architecture designed for real-world ad systems with multiple scenarios.
- **Why Interesting:** Latest Kuaishou production architecture for multi-domain CTR. Addresses the practical challenge of deploying separate CTR models across dozens of ad scenarios with shared backbone and lightweight adapters.
- **Link:** https://arxiv.org/abs/2607.08202

### 2. BACH: Bayesian Anchor-based Cross-domain Heterogeneous Alignment for Cold-Start
- **Authors:** Alibaba
- **Key Contribution:** Solves cold-start recommendation by aligning user embeddings across domains using a Bayesian anchor prior. When a new domain has sparse user data, BACH transfers knowledge from related domains through anchor users who exist in both.
- **Why Interesting:** Cold-start remains the hardest practical problem in recommendation. BACH's Bayesian anchor approach is a principled alternative to typical heuristic-based transfer methods.
- **Link:** https://arxiv.org/abs/2607.08107

### 3. COBART: Bid-Aware Representation Learning for CTR
- **Authors:** Shi et al.
- **Key Contribution:** Jointly models user interest and advertiser bid strategies in a single CTR estimator. Incorporates auction-side information (bid values, competition dynamics) into the click prediction, making the CTR model aware of the downstream auction mechanism.
- **Why Interesting:** First architecture to systematically integrate bid information into CTR prediction rather than treating relevance and auction as separate stages. Could improve ad revenue by better calibrating click probability under varying auction pressure.
- **Link:** https://arxiv.org/abs/2607.08071

### 4. CausalDS: Benchmarking Causal Reasoning in Data-Science Agents
- **Authors:** Andrej Leban, Yuekai Sun
- **Key Contribution:** Benchmark for causal reasoning in agentic data-science workflows. Each instance samples a structural causal model with observational data and a natural-language story. Tasks span all three of Pearl's rungs, with coding components and abstention as a scored outcome. Directly addresses exposure bias through counterfactual generation.
- **Why Interesting:** Causal reasoning benchmarks rarely include realistic data analysis workflows. The exposure bias problem (training on biased exposure data vs. broader candidate space) is a fundamental issue in production CTR systems.
- **Link:** https://arxiv.org/abs/2607.08093

---

## AI / LLM — Agents & Reasoning

### 5. HeaPA: Hierarchical Planning-with-Agents for Complex Reasoning
- **Authors:** Amazon, Google
- **Key Contribution:** Combines a GRPO-trained reasoner with a hierarchical planner for complex multi-step tasks. The planner decomposes tasks, the reasoner executes sub-goals, and results are composed hierarchically. Strong results on math and code benchmarks.
- **Why Interesting:** Demonstrates that GRPO training at scale combined with hierarchical decomposition outperforms monolithic reasoning. Validates the "divide and conquer" principle for agentic reasoning systems.
- **Link:** https://arxiv.org/abs/2601.22448

### 6. Tool-Making Self-Evolving Agents
- **Authors:** Kujanpää et al. (Amazon)
- **Key Contribution:** Production LLM agents that compile repeated SOP steps into validated tools. When an agent encounters the same sequence of operations repeatedly, it synthesizes a tool that encapsulates the pattern. Cuts p50 latency 42% and error rate 53% in a fulfillment center system.
- **Why Interesting:** This is exactly the kind of practical agentic engineering Andrej Karpathy has advocated — agents that improve themselves by extracting reusable skills from experience. The latency and error improvements are substantial.
- **Link:** https://arxiv.org/abs/2607.08011

### 7. Feedback Manipulation Regularization (FMR)
- **Authors:** Benjamin Poole, Minwoo Lee
- **Key Contribution:** Algorithm-agnostic method that harnesses evaluative feedback as a corrective signal for imitation learning alignment. Adapts Safety Gymnasium environments for principled alignment evaluation. Demonstrates up to 98% reduction in misalignment across multiple imitation learning algorithms, robust even in limited data regimes.
- **Why Interesting:** Works with any imitation learning algorithm and remains robust with scarce demonstrations. Addresses the gap between RL alignment (which requires online interaction) and practical deployment (which often relies on demonstrations).
- **Link:** https://arxiv.org/abs/2607.07859

### 8. Overthinking: Amplifying Reasoning Weights to Extract Learned Secrets
- **Authors:** Jack Hopkins, Dipika Khullar, Fabien Roger
- **Venue:** ICML 2026
- **Key Contribution:** Uses reasoning task vectors to amplify reasoning beyond the pure reasoning model (α > 1). Shows overthinking models reveal hidden information up to 10× more frequently than original reasoning models. Layer-wise attenuation strategies preserve output quality while surfacing secrets.
- **Why Important:** Critical for AI safety auditing — black-box methods miss subtle misalignment, but reasoning amplification can surface hidden behaviors. Accepted at ICML 2026, signaling importance.
- **Link:** https://arxiv.org/abs/2607.08173

### 9. Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring
- **Authors:** Jennifer Za, Julija Bainiaksina, Nikita Ostrovsky, Tanush Chopra, Victoria Krakovna
- **Key Contribution:** Stress-tests CoT monitoring against adversarial persuasion. Finds that monitor access to agent's CoT increases approval of harmful actions by 9.5% on average — the scratchpad becomes a persuasion channel. Cross-family fact-checking (Claude monitor + GPT-4.1 fact-checker) reduces harmful approval by up to 45%.
- **Why Important:** Directly challenges the assumption that transparent reasoning improves safety. Shows CoT monitoring alone is insufficient and cross-family model diversity is critical for robust oversight.
- **Link:** https://arxiv.org/abs/2607.08066

---

## AI / LLM — RL & Training

### 10. DRRO-RLHF: Distributionally Robust Reward Optimization for RLHF
- **Authors:** Multiple
- **Key Contribution:** Makes preference learning robust to distribution shift between the reward model and policy. Fixes a known failure mode where PPO-based RLHF over-optimizes a reward model trained on a different distribution.
- **Why Important:** Reward hacking and distribution mismatch are the primary practical failure modes of RLHF. This provides principled robustness without sacrificing performance.
- **Link:** https://arxiv.org/abs/2607.08124

### 11. ReCoLoRA: Spectrum-Aware Recursive Consolidation for Continual LLM Fine-Tuning
- **Authors:** Wentao Lu
- **Key Contribution:** Addresses catastrophic forgetting in continual LoRA fine-tuning. Re-decomposes the effective weight before each new task into frozen residual + principal component + fresh adapter (recursive consolidation). Best final scores on 3/4 backbones against PiSSA, AdaLoRA, and DoRA baselines while training fewer parameters.
- **Why Important:** Continual fine-tuning is critical for production LLMs that must adapt to new domains without losing existing capabilities. Recursive consolidation is a principled alternative to LoRA merging heuristics.
- **Link:** https://arxiv.org/abs/2607.07719

### 12. Feedback Manipulation Regularization (FMR) — Offline Agent Alignment
- **Authors:** Benjamin Poole, Minwoo Lee
- **Key Contribution:** Algorithm-agnostic method for offline agent alignment using evaluative feedback. Achieves up to 98% reduction in misalignment across imitation learning algorithms. Works even with scarce aligned demonstrations.
- **Why Important:** Bridges the gap between online RL alignment and offline imitation learning — the most practical deployment mode for many real-world systems.
- **Link:** https://arxiv.org/abs/2607.07859

---

## AI / LLM — Efficiency & Architecture

### 13. Jet-Long: Efficient Long-Context Extension with Dynamic Bifocal RoPE
- **Authors:** Haozhan Tang, Zerui Wang, Yuxian Gu, Song Han, Han Cai
- **Key Contribution:** Zero-shot context extension using bifocal RoPE: a local RoPE-faithful window paired with a long-range window whose rescaling factor adapts dynamically to sequence length. Up to 1.39× FA2 throughput on H100. Best overall accuracy on HELMET-RAG benchmark.
- **Why Important:** Practical zero-shot long-context extension that generalizes to hybrid architectures (Jet-Nemotron) without retraining. The dynamic bifocal design elegantly handles the short-context vs. long-context tradeoff.
- **Link:** https://arxiv.org/abs/2607.07897

### 14. Uncertainty-Gated Selection for Block-Sparse Attention
- **Authors:** Thomas Rossi
- **Key Improvement:** Value-of-information router that doubles the kept key blocks for queries where the top-k cutoff is least decisive. Paired with Quest, achieves 0.75 paired recall on LongBench-v2 medium vs 0.47 for SSA-style baseline (+28 pp). Preserves 0.81/0.89 of dense accuracy on Qwen2.5-7B-1M/Qwen3.6 at 128K context.
- **Why Important:** Block-sparse attention is the dominant efficiency approach for long-context LLMs. The information-theoretic router design is a principled improvement over naive top-k selection.
- **Link:** https://arxiv.org/abs/2607.07724

### 15. AgentNAS: Agentic Neural Architecture Search
- **Authors:** Seokhoon Jeong, Mijung Kim, Taehwan Kim
- **Key Contribution:** LLM produces a seed architecture → decomposes into "slotted architecture" with named module slots → conventional NAS explores the resulting search space automatically. SOTA on 11/17 tasks across NAS-Bench-360 and Unseen NAS. LLM and NAS are broadly complementary.
- **Why Important:** Bridges LLM-based design and classical NAS without manual search space engineering. The slotted architecture paradigm could become a standard workflow for architecture design.
- **Link:** https://arxiv.org/abs/2607.07984

---

## AI Safety & Evaluation

### 16. When LLMs Agree, Are They Right? Auditing Self-Consistency and Cross-Model Agreement
- **Authors:** Kaihua Ding
- **Key Finding:** Agreement among LLM judges or self-consistency samples is a positive but weak predictor of correctness (ρ 0.20–0.59). Most dangerous: frontier models with high agreement (≥0.8 on 77% of GPQA entries) are wrong on 48% of those cases. Self-consistency is a conditional proxy, not a standalone confidence score.
- **Why Important:** Challenges the widespread practice of using ensemble agreement as a confidence signal. Particularly relevant for LLM-as-judge systems in production.
- **Link:** https://arxiv.org/abs/2607.08065

### 17. Alignment Plausibility: A New Standard for Assuring AI in Healthcare
- **Authors:** Gwydion Williams, Sara Zannone, Bilal A Mateen
- **Key Contribution:** Proposes "alignment plausibility" as a regulatory construct for AI safety — structured demonstration that a system's values, training, and oversight are together consistent with safe outcomes. Organizes alignment at three levels: value specification, training, and deployment oversight.
- **Why Important:** Translates alignment from technical research into a regulatory framework with clear audit requirements. Could influence AI governance standards for high-stakes domains.
- **Link:** https://arxiv.org/abs/2607.07766

### 18. Persona Cartography: Charting Language Model Personality Traits in Weight Space
- **Authors:** Luke Baines et al.
- **Key Contribution:** Trains low-rank adapters to amplify/suppress OCEAN personality traits (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism) in LLMs. Adapters move traits monotonically, combine approximately additively, and affect safety-relevant behavior (neuroticism → frustration, agreeableness → sycophancy). Introduces unsupervised psychometric pipeline recovering 4 interpretable behavioral factors.
- **Why Important:** Provides a bridge between personality psychology and model editing, with direct safety implications. Shows that trait axes have measurable effects on sycophancy and frustration — key deployment concerns.
- **Link:** https://arxiv.org/abs/2607.07916

---

## Summary Statistics

| Category | New Submissions | Curated |
|----------|----------------|---------|
| cs.AI | 56 | ~12 |
| cs.LG | 93 | ~10 |

## Key Themes

| Theme | Papers |
|-------|--------|
| **CTR & Recommendation** | #1 PIT-SUN (Kuaishou multi-domain), #2 BACH (cold-start), #3 COBART (bid-aware CTR) |
| **Agent Engineering** | #6 Tool-Making Self-Evolving Agents, #5 HeaPA hierarchical planning |
| **AI Safety & Alignment** | #8 Overthinking (ICML 2026), #9 CoT monitoring persuasion attacks, #16 Agreement ≠ Accuracy, #17 Alignment Plausibility |
| **RL for LLMs** | #10 DRRO-RLHF robustness, #11 ReCoLoRA continual fine-tuning, #12 FMR offline alignment |
| **Efficiency & Architecture** | #13 Jet-Long bifocal RoPE, #14 Block-sparse uncertainty router, #15 AgentNAS |
| **Causal Reasoning** | #4 CausalDS benchmark for data-science agents |
| **Model Personality** | #18 Persona Cartography (OCEAN traits in weight space) |

## Cross-Cutting Observations

1. **CTR research diversifying:** Multi-domain adapters (PIT-SUN), auction-aware models (COBART), and cold-start via Bayesian anchors (BACH) show CTR is moving beyond monolithic architectures toward modular, transferable designs.

2. **Safety research maturing:** Three papers (#8, #9, #16) challenge core safety assumptions — reasoning amplification surfaces secrets, CoT monitoring enables persuasion, and agreement doesn't guarantee correctness. Cross-family model diversity is emerging as a practical mitigation.

3. **Production agent patterns crystallizing:** Tool-making self-evolution (#6) and hierarchical planning (#5) represent two complementary approaches to practical agentic systems — one optimizes the agent itself, the other optimizes the task decomposition.

4. **RLHF robustness is the new frontier:** DRRO-RLHF and FMR both address the gap between theoretical RLHF guarantees and practical deployment failures, suggesting the field is moving past "RLHF works" to "RLHF must be robust."
