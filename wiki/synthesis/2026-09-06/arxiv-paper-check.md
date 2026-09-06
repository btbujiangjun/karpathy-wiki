---
title: arXiv Paper Check — AI & CTR (September 6, 2026)
type: synthesis
created: 2026-09-06
updated: 2026-09-06
sources: [arxiv.org]
tags: [arxiv, ai, ctr, recommendation, agents, reasoning, rl, pretraining, evaluation, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 6, 2026)

> **Weekend catch-up window.** arXiv does not run new listings on Saturday/Sunday (RSS `skipDays` confirmed; `arxiv.org/list/*/new` still points at **Fri, 4 Sep 2026**). The Friday mailing was already heavily mined by the 09-05 sibling digests — [[arxiv-daily]] (Uno, Minima, Sequential Beats Joint, SelfDR, EPIC, HypRQ-VAE, UniCon, meCPM, …) and [[arxiv-ai-search]] (DRACO, Rethinking OPD II, Free Pause Tokens, DoPR, LLM4AIGQ, Environment Evolution, Terminal-Universe, TAHI, Emergent Cheating Swarms, …). This check therefore covers the **unclaimed remainder of the Fri 4 Sep wave**. Every featured arXiv ID is grep-verified absent from `wiki/` (0 hits). Source: arXiv Atom API + `arxiv.org/list/cs.IR/new`, `cs.AI`, `cs.LG`.

---

## Top Papers by Relevance

### 🧠 LLM Training & Pretraining

#### 1. Compile by Training: Turning Natural-Language Specifications into Local Neural Functions
- **arXiv**: [2609.04199](https://arxiv.org/abs/2609.04199) (EMNLP 2026 System Demonstrations)
- **Authors**: Yuntian Deng, Pengyu Nie, Stuart Shieber
- **Key Contribution**: "Compile by training" turns a natural-language specification into a reusable, self-contained neural function. Teacher models synthesize task-specific examples at compile time; those train a small adapter over a compact interpreter, so the resulting function runs **without the teachers** and can be stored, versioned, and composed like ordinary software. On FuzzyBench-Hard (a subset where the Program-as-Weights fast compiler found zero exact matches) it reaches **83.6% semantic accuracy**, at higher compile cost (~1 min vs seconds). Deployed in a public service with a multi-site website helper, a language-controlled 3D avatar, and a bidirectional English→Claudish translator.
- **Why Interesting**: Extends the Program-as-Weights line (code-as-weights in [[concepts/bacterial-code]] spirit) into "compile NL specs into local neural functions" — directly relevant to agent tooling and on-device personalized models. (high confidence)

#### 2. Knowledge Acquisition During Pre-training? Large Language Models Learn Better With Auxiliary Views
- **arXiv**: [2609.04180](https://arxiv.org/abs/2609.04180) (Findings of EMNLP 2026)
- **Authors**: Joseph Lee, Yidi Huang, Dokyoon Kim, Shu Yang, Li Shen
- **Key Contribution**: Controlled pre-training experiments isolating the role of *auxiliary views* (reformulations of knowledge). Findings: (1) repetition is necessary for acquisition, and paraphrasing helps only at smaller batch sizes; (2) holding token budget fixed, reallocating tokens from document repetition to auxiliary views **improves learning, even for factual recall**; (3) gains are not contingent on teacher-model strength; (4) identifies contextual and foundational knowledge forms that aid acquisition when prior knowledge is missing; (5) mechanistically traced via layer-wise biases and compression.
- **Why Interesting**: Gives a causal explanation for *why data diversity matters* in pre-training — a live question in Karpathy's scaling/pretraining wheelhouse, and a testable knob for data-mix design. (high confidence)

#### 3. ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize
- **arXiv**: [2609.04197](https://arxiv.org/abs/2609.04197) (EMNLP 2026)
- **Authors**: Lihao Liu, Peng Tang, Kunwar Yashraj Singh, Shabnam Ghadar
- **Key Contribution**: Fixes "prompt bloat" in evolutionary prompt optimizers like GEPA (prompts up to 3× longer, no accuracy gain). Three phases: **Diagnose** clusters all training errors into structural patterns in one round; **Propose** generates candidates via four complementary strategies with independent biases; **Select** applies bootstrap stability selection. On 7 public NLP benchmarks (MMLU, GSM8K, HotpotQA, etc.) ESPO improves average accuracy **+3.76 pp** over SOTA (74.67% vs 70.91% for GEPA) while producing **47% shorter prompts** (1,004 vs 1,878 chars). Ablation confirms diversity-without-stabilized-selection actually hurts (−1.20%).
- **Why Interesting**: Prompt engineering is still the cheapest lever in agent systems; "diagnose-diversify-separate-stabilize" is a reusable recipe, with a generalization bound grounding each phase. (high confidence)

#### 4. Probabilistic Causal Impact (PCI): A Computationally Feasible Framework for Causal Probabilistic Explanation
- **arXiv**: [2609.04177](https://arxiv.org/abs/2609.04177)
- **Authors**: Rafal Urbaniak, Sam Witty, Daniel Waxman, Andy Zane, Poorva Garg, Emily Bunnapradist, Sankaran Vaidyanathan, Jack Feser, Drew Lehe, Eli Bingham
- **Key Contribution**: Closes the gap between *actual causality* (principled but toy-scale, counterfactual-exhaustive) and *SHAP-style attribution* (scalable but partially ignoring causal structure). PCI recasts explanation as Monte-Carlo estimation over a probabilistic causal model with a distribution over candidate explanations, counterfactuals, and a scoring function — generalizing AC and Pearl's probability of causation as degenerate cases. Validated on synthetic cases, continuous dynamical systems, and a deployed causal ML model trained on millions of datapoints.
- **Why Interesting**: For CTR/ad explainability (already cited against Causal Foundation Models `2609.03003` last check), PCI is a practical path to causally-grounded, graded per-impression attribution at industrial scale. (high confidence)

---

### 📊 Evaluation & Measurement

#### 5. Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints
- **arXiv**: [2609.04198](https://arxiv.org/abs/2609.04198)
- **Authors**: Haoyaun Zhu, Jie Zhang
- **Key Contribution**: A preregistered audit of the assumption that "same request → same model name → same readout tomorrow" holds for LLM-judges gates. Across **52,988 audited request attempts**: same-window repeat rankings agreed at Spearman **0.400 vs a required 0.90**; byte-identical next-day replays at **0.78 vs 0.99** — each time with execution logging at ceiling. Mechanisms: label-to-meaning bias as strong as the signal; candidate gaps seven orders of magnitude below the instrument's noise floor; byte-identical inputs returning different rankings. Switching providers doesn't help (4 providers share the floor, medians 0.74–0.88); self-hosting helps only while quiet. Distills into a three-level *snapshot-identity ladder*, 8 design rules, and a reporting checklist; a 2%-volume pilot would have exposed both failed gates in advance.
- **Why Interesting**: Evidence-based attack on leaderboard/judge reliability — pairs with the wiki's existing eval-reliability thread (Contamination Inflates Scores `2609.02899`, benchmark-rigging analysis). A model name on a shared endpoint is **not** a frozen instrument. (high confidence)

#### 6. SWE-Gate: Passing Functional Tests Is Not Enough for Software Engineering Agents
- **arXiv**: [2609.04167](https://arxiv.org/abs/2609.04167)
- **Authors**: Xin He, Yanlin Wang, Mingwei Liu, Jiachi Chen, Hongyu Zhang, Guanbin Li
- **Key Contribution**: Repository-level benchmark that evaluates **review-constraint compliance** alongside functional correctness. Review constraints are mined from real PR review comments; each of **303 repair instances across 75 Python repos** ships separate functional and constraint tests plus non-compliant and gold patches. On 4 LLM backends under one scaffold, among **644 functional-passing repairs, 221 (34%) violate the review constraints** — functional-only evaluation overestimates agents' repo-level repair capability.
- **Why Interesting**: Answers `SWE-bench ProMax`-style "funny tests" critiques with a real gap measurement — coding-agent evals must test what reviewers would reject, not just green tests. (high confidence)

#### 7. Inferred Generative-Process Diversity Predicts Correlated Failure Across Language Models *(honorable mention)*
- **arXiv**: [2609.03422](https://arxiv.org/abs/2609.03422)
- **Authors**: Evan Markou, et al.
- **Key Contribution**: Models the *generative process* behind each LM rather than just its outputs; inferred process diversity predicts when two models fail in correlated fashion.
- **Why Interesting**: A committee/cascade design principle — pick partners with decorrelated generative processes to reduce correlated failure. Metadata thin; *(tentative)*.

---

### 🤖 Agents, Memory & Research Automation

#### 8. SENTINEL-RL: Offloading Topological Reasoning from LLM Agents in the Security Operations Center
- **arXiv**: [2609.04159](https://arxiv.org/abs/2609.04159)
- **Authors**: Uday Vallabhaneni, Cassie L. Cagwin, David J. Wild
- **Key Contribution**: An agentic-SOC architecture that decouples **topological reasoning from semantic reasoning**: a heterogeneous graph-attention encoder summarizes the live authentication subgraph into a fixed state; a PPO policy maps it to constrained investigative actions; an LLM loop is restricted to turning the policy's recommendations into analyst-readable narratives gated by a critic. On LANL (24M-edge auth subgraph) + Indiana University Quartz HPC: CREATE ingestion 14.2 min (24× faster than MERGE pipeline), alert engine trips 25-event/10s threshold in ≤2.5s, PPO converges to precision 0.91 / recall 0.87 on red-team events, and a **full detect–investigate–recommend–human-approve cycle median 6.3 s**.
- **Why Interesting**: A concrete division-of-labor pattern — RL does the structured reasoning, LLM does the narrative — that sidesteps context-window and hallucination limits; directly applicable to any large-graph agent task (fraud, infra, research). (high confidence)

#### 9. RuleMem: Active Rule Memory for Long-Term Conversational Agents
- **arXiv**: [2609.03915](https://arxiv.org/abs/2609.03915)
- **Authors**: Xingyuan Zeng, Zuohan Wu, Quanming Yao, Yue Wang, Wei Liu, Libin Zheng, Jiuke Wang, Jian Yin
- **Key Contribution**: Treats long-term dialogue memory as *active rules* rather than passively stored facts. Induces natural-language **Horn clauses** from history, validates them via a Rule Perplexity Consistency (RPC) mechanism, and uses the rules to retrieve semantically distant evidence while giving explicit logical structure to generation. Beats 14 baselines on LoCoMo (top accuracy, **+27.47 pts = +54.3% relative** vs baseline average).
- **Why Interesting**: Connects to the wiki's memory/context thread (MEM1, context-engineering): rules-as-memory is a cheap, interpretable upgrade path for long-horizon agents over raw vector recall. (high confidence)

#### 10. SciLENS: RL-Driven Autonomous Agents for Scientific Localized Evidence Navigation and Synthesis
- **arXiv**: [2609.03338](https://arxiv.org/abs/2609.03338)
- **Authors**: Leqi Zheng, Jinbo Su, Yuying Li, Chaokun Wang, Weiping Wang, Haitao Li, Jiajun Zhang, Shannan Yan, Zhaolu Kang, Rong Fu, Jie Wu, Fang Niu, Hang Zhang
- **Key Contribution**: A fully local autonomous agent over a dual-tier index of ~12M academic records. Pioneers **structural visualization as an actionable tool inside the reasoning loop**, compressing citation topologies into validated charts to fight context exhaustion. Trained without human annotation via an automated multi-hop subgraph synthesis pipeline verified by 20-frontier-model cross-consensus; aligned with a reverse-decomposition rubric giving fine-grained process rewards for planning and evidence grounding. Outperforms open-source baselines and is comparable to GPT-5.2 and Gemini-3.0-pro across QA/citation-accuracy/factual-reasoning/structural-synthesis benchmarks.
- **Why Interesting**: Autoresearch-style (matches [[concepts/autoresearch]]) but fully local and RL-aligned — evidence grounding is the differentiator, not model size. (high confidence)

---

### 🔎 Retrieval, Ranking & Rec-Adjacent

#### 11. CLEAR: From Topical Relevance to Answerability — Entailment Distillation for Conversational Retrieval
- **arXiv**: [2609.03482](https://arxiv.org/abs/2609.03482) (Findings of EMNLP 2026)
- **Authors**: Shuai Qin, Guojia An, Weikang Guo, Pei Ke, Jiwei Wei, Yang Yang, Jie Zou
- **Key Contribution**: Identifies a systematic **answerability gap**: topical-matching passages are not necessarily the ones supporting the correct answer. CLEAR transfers passage-answer entailment supervision into a cross-encoder reranker (so it discriminates answer-supporting passages from topical distractors at inference, answers-free) plus an abductive recall module that infers answerable queries from passages to expand the candidate pool. Consistent top-ranked precision gains on TopiOCQA, QReCC, and out-of-domain TREC CAsT, largest under heavy topical noise; composes with LLM query-rewriters.
- **Why Interesting**: For recommendation/search there's an analog of the same failure — ranking by topical match vs what actually satisfies the intent. An actionable reranker recipe. (high confidence)

#### 12. CORE: Improving Compositional Reasoning in MLLM Embedding via Reranker Distillation
- **arXiv**: [2609.04083](https://arxiv.org/abs/2609.04083)
- **Authors**: Tingyu Song, Mingxin Li, Yanzhao Zhang, Dingkun Long, Chu Liu, Pengjun Xie, Yilun Zhao, Shu Wu
- **Key Contribution**: Same MLLM backbone resolves attribute-object bindings fine as a cross-attentive reranker but fails as an embedding model — so CORE **distills the reranker's compositional judgments into the embedder**. Synthesizes candidate lists spanning 5 compositional matching levels and trains with a listwise Rank-KL objective. Across COLA, SUGARCREPE++, NEGBENCH: CORE-RERANKER-8B **82.7% avg (+10.7 over Jina-Reranker)**; CORE-EMBED-8B best total average among evaluated embedders (0.666), transferring to MCMR without sacrificing COCO/Flickr30K retrieval.
- **Why Interesting**: A clean "embedder ← reranker self-distillation" pattern that upgrades multimodal retrieval for shop-by-description and compositional ad creative matching without new data. (high confidence)

#### 13. Spruce: Scalable Private Outsourced Retrieval Using Compact Embeddings *(systems bonus)*
- **arXiv**: [2609.03376](https://arxiv.org/abs/2609.03376)
- **Authors**: Peichun Hua, Yunming Xiao
- **Key Contribution**: Co-designs representations with MPC for private vector-search over outsourced corpora: learns compact binary codes that preserve full-precision reranking candidates, replaces corpus-wide embedding scoring with Hamming-distance under two-server MPC, adds corpus-calibrated fixed-radius search, private cluster pruning, and a one-core designated-dealer to remove OT preprocessing bottlenecks. Across 383K–5.42M docs: full scans 0.21–2.97s (**4.8–6.7× faster** than prior work), pruning 0.06–1.09s (**13.1–22.9×**, retaining 93.9–97.3% NDCG); 31.5× sustained-throughput gain at 1 Gbps.
- **Why Interesting**: Privacy-preserving retrieval is becoming production-feasible — relevant to regulated-ad and personalization stacks that must outsource embeddings without leaking queries. (high confidence)

---

## Summary Statistics

- **Total papers scanned**: ~35 screened from Fri 4 Sep 2026 mailing (cs.AI top-20 via Atom API + cs.IR `list/new` full page) + sibling-digest dedup of the wider wave
- **Papers selected**: 13 (12 featured + 1 honorable mention)
- **Window note**: arXiv publishes no new listings Sat–Sun; this is the fresh remainder of the last mailing, which the 09-05 digests already covered extensively (see [[arxiv-daily]] / [[arxiv-ai-search]] for that coverage)
- **Key themes**:
  - Compiling/specifying → neural functions; data diversity explained via auxiliary views (pretraining science)
  - Evals: judges are unstable instruments; functional tests ≠ repo-level acceptance; generative-process diversity for correlated failure
  - Agents: RL topologies + LLM narratives (SENTINEL-RL), rules-as-memory (RuleMem), local RL research agents (SciLENS)
  - Retrieval: answerability-over-topicality grading; reranker→embedder self-distillation; private vector retrieval via MPC + binary codes

## Tags

`arxiv` `ai` `ctr` `recommendation` `agents` `reasoning` `rl` `pretraining` `evaluation` `daily-digest` `2026-09-06`