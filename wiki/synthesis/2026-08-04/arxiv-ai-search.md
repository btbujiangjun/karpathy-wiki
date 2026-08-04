---
title: "arXiv AI Research Scan — August 4, 2026"
type: synthesis
created: 2026-08-04
updated: 2026-08-04
tags: [arxiv, survey, llm, agents, reasoning, alignment, recommendation, search, retrieval, rag, games, simulation, benchmark]
---

# arXiv AI Research Scan — August 4, 2026

Curated papers from the Mon Aug 3, 2026 arXiv batch (announced Aug 4) spanning LLM agents & reasoning, recommendation/search/advertising, retrieval & RAG, and games/simulation/benchmarks. All papers verified against arXiv. Complements the [Aug 3 scan](../2026-08-03/arxiv-ai-search.md), the [Aug 3 paper check](../2026-08-03/arxiv-paper-check.md), the [Aug 3 conference digest](../2026-08-03/conference-digest.md), and the [Aug 4 daily digest](./arxiv-daily.md) — **no overlap** with papers covered there. Flagship rec/CTR/ads papers announced Aug 3 (TransX, SnapLGR, GALA, Think2Go, PaletteID, RecHarness, EvoReason, MerchantBench, RareSense, GenCDSR, QASP, LightMem, RCBS) are excluded here; this scan draws on the cs.IR replacement stream, cs.CL/cs.AI new submissions, and TMLR publications instead.

---

## Large Language Models, Agents & Reasoning

### 1. SciToolAgent-Evo: Open-World Scientific Tool Agents via Adversarial Co-Evolution
- **Authors**: Yuqi Tang, et al.
- **Institution**: Zhejiang University (tentative, based on author affiliations)
- **Abstract**: Open-world scientific tasks require agents to continuously acquire and evolve new tool capabilities. SciToolAgent-Evo trains a scientific tool agent (Qwen2.5-7B) by co-evolving tool *generation* and tool *usage* in adversarial fashion: an evolver LLM iteratively proposes novel tool schemas, a simulated user generates queries and invokes the tools, and the evolutionary loop autonomously creates, trains, and upgrades new tools that generalize beyond the training distribution.
- **Key Innovations**: Autonomous tool schema proposal and function augmentation with no human annotation; trained agents improve their own tools during deployment; substantial gains over existing scientific tool agents on open-world task suites (trained 7B agent outperforming prior SOTA scientific agents).
- **Link**: https://arxiv.org/abs/2607.28692

### 2. TAPR: Task-Aware Prompt Rewriting via GRPO
- **Authors**: Oliver Savolainen, Emanuele Bastianelli, Hosein Azarbonyad
- **Institution**: Elsevier Labs (tentative, based on author affiliations)
- **Abstract**: Prompt rewriting is a cheap, model-agnostic lever for LLM quality, but existing rewriters are trained with noisy heuristics or closed-loop rewards that are task-specific. TAPR trains a prompt rewriter with GRPO using LLM-as-a-judge rewards, jointly optimizing instruction-following and downstream task performance rather than exact match against a single rewriting target.
- **Key Innovations**: RL-trained (GRPO) rewriter with judge-based reward; rewrites help both task-agnostic instruction following and tool-use prompts; improves response quality over SFT-only and closed-loop rewriting baselines.
- **Link**: https://arxiv.org/abs/2607.28657

### 3. The Fragility of Value under Imperfect Alignment
- **Authors**: Winter Cross
- **Institution**: N/A
- **Abstract**: A conceptual paper arguing that alignment is fragile in a specific, formal sense: small imperfections in a value specification propagate into arbitrarily bad outcomes under sufficiently general goal-directed behavior. Treats value embedding as a dynamical/stability problem rather than a one-shot optimization, and examines what conditions would be required for value to be robustly preserved under fine-tuning and deployment shifts.
- **Key Innovations**: Counterexample-based argument that "solve alignment once" approaches are structurally insufficient; frames value fragility as a stability condition for downstream objectives; proposes desiderata for robust value preservation rather than a concrete training recipe (tentative).
- **Link**: https://arxiv.org/abs/2607.28881

### 4. NeSyFS: Neuro-Symbolic Fast-Slow Thinking for Partially Observable Agents
- **Authors**: Duo Xu, Faramarz Fekri
- **Institution**: Georgia Tech (tentative)
- **Abstract**: LLM agents struggle in partially observable environments where perception is incomplete and decisions require reasoning over unobserved structure. NeSyFS combines *fast* data-driven policy learning with *slow* symbolic reasoning in a unified architecture: a neuro-symbolic reasoner derives high-level facts from sensed observations, and the fast policy is interleaved with symbolic reasoning to guide action selection under uncertainty.
- **Key Innovations**: Explicit modeling of partial observability via neuro-symbolic fact derivation; joint fast-slow reasoning loop rather than a reasoning-after-perception pipeline; improves decision quality and sample efficiency in partially observable agent benchmarks.
- **Link**: https://arxiv.org/abs/2607.28942

### 5. Token-Level Diagnosis of Sycophancy via Attention Structure Introspection
- **Authors**: Hieu Nguyen, Mahammed Kamruzzaman, Anshuman Chhabra, Gene Louis Kim
- **Institution**: USC ISI (tentative, based on author affiliations)
- **Abstract**: Sycophancy — models praising or agreeing with users regardless of correctness — is typically measured at the response level, which obscures *where* in the generation the behavior originates. This paper applies attention structure introspection (ASI) and Integrated Gradients to localize sycophantic behavior down to individual tokens, identifying specific attention patterns and vocabulary triggers that drive flattering responses.
- **Key Innovations**: First token-level attribution of sycophancy (ASI-based); finds sycophancy concentrated in identifiable attention sub-patterns rather than spread across the response; proposes a steering/diagnostic recipe using the identified tokens to measure and mitigate sycophancy without full retraining.
- **Link**: https://arxiv.org/abs/2607.28906

### 6. Tokenizer-Agnostic Engram Module
- **Authors**: Jia Peng Lim, Hai Leong Chieu
- **Institution**: DSO National Laboratories (tentative, based on author affiliations)
- **Abstract**: Memory modules for LLMs typically bind stored facts to a specific tokenizer's token space, so swapping tokenizers (or training a new model) invalidates the memory. The Engram Module is a conditional memory that stores event embeddings in a tokenizer-agnostic space, retrieved by attention and injected as conditioning signals at generation time.
- **Key Innovations**: Memory remains valid across tokenizer and model changes; attention-based retrieval over tokenizer-agnostic stores; improves factual recall in memory-conditional generation with strong robustness to vocabulary/tokenizer shifts.
- **Link**: https://arxiv.org/abs/2607.29065

### 7. M3-DuplexBench: A Full-Duplex Spoken Dialogue Benchmark for Multi-Talker Scenarios
- **Authors**: Ryo Fukuda, Atsushi Ando, Hiroki Kanagawa, Takatomo Kano, Marc Delcroix, Naohiro Tawara, Yuya Chiba
- **Institution**: NTT Corporation (tentative, based on author affiliations)
- **Abstract**: Most spoken-dialogue benchmarks assume one speaker at a time (half-duplex). M3-DuplexBench tests full-duplex capabilities in *multi-talker* settings: overlapping speech, barge-in, interruptions, and target-speaker tracking. It provides curated scenarios plus automatic metrics for overlap handling and response timing.
- **Key Innovations**: First benchmark (tentative) explicitly scoring full-duplex + multi-talker behavior; covers barge-in, overlapping inputs, and interruption recovery; reveals current spoken LLMs degrade significantly under overlap compared to clean single-speaker turns.
- **Link**: https://arxiv.org/abs/2607.29125

---

## Recommendation, Search & Advertising

### 8. SaFRO: Satisfaction-Aware Feature Ranking and Optimization for Short-Video Search
- **Authors**: Renzhe Zhou, Yi Xiao, Xiao Yang, Jingwei Zhuo, et al.
- **Institution**: Kuaishou (tentative, based on author affiliations)
- **Abstract**: Short-video search ranking conflates two signals: within-feed clicks (intra-feed relevance) and cross-feed behavior that reveals whether the whole page satisfied the user. SaFRO ranks feature contributions across both levels, training the model to distinguish intra-feed from inter-feed satisfaction and optimizing ranking toward search-satisfaction rather than raw click.
- **Key Innovations**: Explicit intra-feed vs inter-feed satisfaction decomposition for short-video search; feature-ranking/optimization lens rather than a one-level ranking model; deployed gains reported for short-video search at Kuaishou.
- **Link**: https://arxiv.org/abs/2603.19585

### 9. OPERA: Online Data Pruning via Partition-Based Sampling for Retrieval Adaptation
- **Authors**: Haoyang Fang, Shuai Zhang, Yifei Ma, Hengyi Wang, Cuixiong Hu, Katrin Kirchhoff, Bernie Wang, George Karypis
- **Institution**: Amazon Web Services (tentative, based on author affiliations)
- **Abstract**: Retrieval models must adapt continuously as new data streams in, but retraining on everything is wasteful and streaming data is redundant. OPERA is an online data-pruning method: it partitions the incoming stream, samples representative examples per partition, and continuously adapts a retriever on the pruned subset, with a pruning schedule that keeps adaptation stable under distribution shift.
- **Key Innovations**: Online (streaming) retrieval adaptation instead of batch re-training; partition-based sampling keeps class/domain balance in the pruned stream; improves Open-Domain QA when the retriever is continuously updated on evolving corpora.
- **Link**: https://arxiv.org/abs/2603.17205

---

## Retrieval & RAG

### 10. CMT-RAG: Multi-Turn Multi-Hop RAG with Memory and Knowledge-Graph Augmentation
- **Authors**: Lang Zhou, Yingjian Chen, Shuxuan Li, Kun-Yu Lin, Zhilin Zhao
- **Institution**: HKUST-Guangzhou (tentative, based on author affiliations)
- **Abstract**: Single-turn RAG retrieves for one question; multi-turn multi-hop QA needs to accumulate evidence across turns and link facts. CMT-RAG maintains a memory of previously retrieved evidence, performs knowledge-graph augmentation over the accumulated facts, and uses the memory-augmented context to retrieve and answer subsequent turns.
- **Key Innovations**: Turn-accumulating memory so earlier retrieved facts inform later retrieval; KG augmentation for multi-hop fact linking; improves multi-turn multi-hop QA accuracy over single-turn RAG pipelines.
- **Link**: https://arxiv.org/abs/2607.26470

### 11. DenseOn / LateOn: Open Dense and Late-Interaction Retrieval Models
- **Authors**: Raphaël Sourty, Antoine Chaffin, Paulo Roberto Moura Junior, Amélie Chatelain
- **Institution**: IRISA / Josane (tentative, based on author affiliations)
- **Abstract**: The strongest dense retrievers are often trained on proprietary or restricted data, making them hard to reproduce and audit. DenseOn and LateOn are fully open dense and late-interaction retrieval models — dense (Contriever-style) and late-interaction (ColBERT-style) families — trained only on publicly available data with reproducible pipelines.
- **Key Innovations**: Open, reproducible training recipes for both dense and late-interaction retrieval; releases models and training code; competitive performance while keeping the entire pipeline auditable and license-clean.
- **Link**: https://arxiv.org/abs/2607.27178

### 12. Iterative RAG versus Gold Context: When Retrieval Helpers Hurt
- **Authors**: Mahdi Astaraki, Mohammad Arshi Saloot, Ali Shiraee Kasmaee, Hamidreza Mahyar, Soheila Samiee
- **Institution**: N/A
- **Abstract**: Iterative RAG — repeatedly querying a retriever with intermediate reasoning — is widely assumed to help, but the retriever can inject noise and distract the generator. This paper builds a diagnostic setup comparing iterative RAG against "gold context" (perfect retrieval), quantifying how much performance loss is attributable to the retrieval loop itself.
- **Key Innovations**: Direct measurement of the gap between iterative-RAG outputs and gold-context upper bounds; identifies cases where iteration *hurts* (noise amplification) versus where retrieval is genuinely binding; practical guidance on when to stop iterating (TMLR 2026 publication).
- **Link**: https://arxiv.org/abs/2601.19827

### 13. BM25 Wins at Scale
- **Authors**: Pengyu Wang, Benfeng Xu, Shaohan Wang, Mingxuan Du, Xin Zeng, Huarui Wu, Lei Zhang, Licheng Zhang
- **Institution**: N/A
- **Abstract**: As base LLMs grow and context windows widen, increasingly complex RAG paradigms (agentic retrieval, graph RAG, learned re-rankers) are marketed as strictly better. This study scales the comparison across model sizes and context budgets and finds that plain BM25 retrieval matches or beats complex RAG pipelines once the model is large enough and the context window long enough to tolerate lexical noise.
- **Key Innovations**: Scaling-law style analysis of retrieval-paradigm choice; shows BM25's advantage grows with model scale and context length; recommends BM25 as the default strong baseline and warns that complexity pays off mainly at small scale.
- **Link**: https://arxiv.org/abs/2607.26497

---

## Games, Simulation & Benchmarks

### 14. What Makes a Sale? — RetailSim: An End-to-End Seller-Buyer Retail Simulation
- **Authors**: Jeonghwan Choi, Jibin Hwang, Gyeonghun Sun, Minjeong Ban, Taewon Yun, Hyeonjae Cheon, Hwanjun Song
- **Institution**: KAIST AI (tentative, based on author affiliations)
- **Abstract**: Retail research is fragmented across separate models for listings, pricing, and negotiation. RetailSim is an end-to-end retail simulation where buyer and seller LLM agents interact over a full transaction — listing, offer, negotiation, and final acceptance — and a "sale" is defined only by the whole trajectory, not isolated clicks.
- **Key Innovations**: End-to-end seller-buyer negotiation loop rather than staged benchmarks; analysis of which seller behaviors (pricing, responsiveness, offer strategy) most determine sale outcomes; provides a controllable environment for studying retail interaction dynamics (COLM 2026).
- **Link**: https://arxiv.org/abs/2604.04468

### 15. The Metanym Game: Measuring Structural Intelligence through Council-of-Peers Ratings
- **Authors**: David Nordfors
- **Institution**: N/A
- **Abstract**: The Metanym Game is a collaboration/trust game in which participants rate each other's proposals through a council-of-peers mechanism, and a central ratings matrix is decomposed (via SVD) into a spectral solution that recovers latent structural quality. The framing connects rating dynamics to "structural intelligence" — the ability of a group to recognize and promote high-value contributions.
- **Key Innovations**: SVD-based spectral aggregation over peer ratings to identify high-structure contributions; positions the game as a measure of group-level structural intelligence; v2 revised (30 Jul 2026) extends the method and its formal guarantees.
- **Link**: https://arxiv.org/abs/2606.21008

---

## Run Summary
- **Batch**: Mon Aug 3, 2026 arXiv announcements (cs.AI 43 / cs.CL 51 / cs.IR 13 new + 11 replacements / cs.LG 82 new).
- **Papers in this scan**: 15 curated, all verified against arXiv.
- **No overlap**: excludes Aug 3 scans (arxiv-ai-search, arxiv-paper-check, conference-digest) and the Aug 4 arxiv-daily; cs.IR new-submission flagships were covered in the Aug 3 digests, so this scan draws from the cs.IR replacement stream and cross-listed cs.CL/cs.AI/TMLR papers.
- **Themes**: agentic tool evolution (SciToolAgent-Evo), RL-based prompt rewriting (TAPR), alignment fragility (Fragility of Value), neuro-symbolic agents (NeSyFS), token-level sycophancy diagnosis, tokenizer-agnostic memory, full-duplex dialogue benchmarking, short-video search satisfaction (SaFRO), online retrieval adaptation (OPERA), multi-turn/multi-hop RAG, open retrieval models, RAG-vs-gold-context diagnostics, BM25-at-scale, retail negotiation simulation, and structural-intelligence games.
