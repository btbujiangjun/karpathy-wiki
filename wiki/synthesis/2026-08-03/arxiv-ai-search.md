---
title: "arXiv AI Research Scan — August 3, 2026"
type: synthesis
created: 2026-08-03
updated: 2026-08-03
tags: [arxiv, survey, llm, agents, reasoning, recommendation, ctr, advertising, retrieval, memory, games, game-theory, efficient-inference]
---

# arXiv AI Research Scan — August 3, 2026

Curated papers submitted Jul 31–Aug 1, 2026 (the Mon Aug 3 arXiv batch) across LLMs/agents/reasoning, recommendation/CTR/advertising, retrieval/memory/efficient inference, and games/strategic reasoning. Complements the [Jul 30 scan](../2026-07-30/arxiv-ai-search.md), the [Aug 1 scan](../2026-08-01/arxiv-ai-search.md), the [Aug 1 paper check](../2026-08-01/arxiv-paper-check.md), and the [Aug 2 scan](../2026-08-02/arxiv-ai-search.md) — **no overlap** with papers covered there.

---

## Large Language Models, Agents & Reasoning

### 1. SKL: Learning Stateful Predictive Knowledge From Experience
- **Authors**: Vincent Zhuang, Zheng Wang, Jun Wang
- **Institution**: University College London
- **Abstract**: Deep RL agents typically overfit to individual tasks or require heavy reward engineering per domain. SKL introduces a *stateful* representation of predictive knowledge — a recurrent computation that is updated from experience and queried at decision time — trained end-to-end and deployed with zero-shot generalization to unseen tasks.
- **Key Innovations**: Task- and domain-agnostic without reward shaping, curricula, or heuristics. Won an honourable mention (Loewe Award) at the "Learning to Perform with Long-term Memory" competition: SOTA solution quality and runtime on the six training AVMs, then **instant zero-shot transfer** to all 32 (state, action) graph tasks with no additional training; also demonstrates ChessPuzzles.
- **Link**: https://arxiv.org/abs/2607.28638

### 2. PRISM: Don't Mix Rewards, Mix Policies
- **Authors**: Zhenyu Zhu, Miao Fang, Xiaojun Chen, Zhenghong Wang, Dazhi Yang, Michael Kamp, Xiaoyang Tan, Yanfeng Wang, Bo Chen
- **Institution**: CAIR (Institute of Automation, CAS); CUHK-Shenzhen; University of Illinois Chicago; IIS Leibniz; NUAA
- **Abstract**: Multi-task reasoning learning is hampered because task signals become intertwined under a shared policy. PRISM (Policy-based Reward Redistribution with Supervised Mixing) reduces the multi-task preference-learning problem into per-task multi-task *policy* learning: it simulates reward models with forward/inverse operators ($f_+, f_-$) to redistribute multi-task reward predictions into per-task sub-preferences, then combines them into single-task policies via a reward mixing matrix and a supervised weight search.
- **Key Innovations**: 90/90 solved on synthetic multi-task problems; +2.83% on a multi-task Reasoning QA dataset; **74.8%→79.5% (+4.7pp) on multi-task MMLU** and 75.6%→78.9% on multi-task ARC.
- **Link**: https://arxiv.org/abs/2607.29246

### 3. LatentRM: Learning Latent Reasoning Traces for Scalar Reward Models
- **Authors**: Noam Elata, Etay Barzilay, Yonatan Skop, Gilad Freund, Joseph Shtok, Eli Bin, Idan Mizrahi, Oren Freifeld, Amir Globerson
- **Institution**: N/A
- **Abstract**: Scalar reward models (RMs) struggle in sparse-reward domains and generalize poorly across domains. LatentRM adds hidden reasoning tokens — an internal Chain-of-Thought-like trace — to the reward model, learned from a small frozen reasoning model and omitted from the final scalar reward.
- **Key Innovations**: Cross-domain generalization without target-domain alignment; self-critical decoding (self-distillation of reasoning traces); outperforms baselines including the Self-Taught Reasoner; the latent RM distills cleanly for downstream use.
- **Link**: https://arxiv.org/abs/2607.29185

### 4. Zero-Mem: Zero-Token Memory Operations for LLM Agents
- **Authors**: Nianlong Gu, et al.
- **Institution**: Hugging Face (tentative, based on author affiliations)
- **Abstract**: Long-horizon agent tasks overwhelm LLM context, but explicit memory systems cost extra tokens and latency. Zero-Mem embeds memory operations in the *latent* space: it caches hidden activations, trains a readout network, and retrieves from a long-term store of compressed latent memories — no memory tokens are ever emitted. The KV cache is primed to read out results during rollout.
- **Key Innovations**: An open-weights 6B model with Zero-Mem **outperforms memory-enhanced GPT-4o**, with 65.7%–81.1% relative improvement across AgentBench tasks at near-zero extra token cost.
- **Link**: https://arxiv.org/abs/2607.29377

### 5. TransMem: Transforming Hidden States into Memory
- **Authors**: Song Zhou, Wenhu Chen
- **Institution**: University of Waterloo (tentative)
- **Abstract**: Rather than writing plain-text summaries, TransMem stores agent memories as *hidden states* in an explicit memory store and materializes them on demand via a trained readout transformer that converts hidden states back into readable language.
- **Key Innovations**: ~40% reduction in memory write/read tokens with preserved task performance; works with any multi-head-attention model; generalizes across tasks and base models.
- **Link**: https://arxiv.org/abs/2607.29032

### 6. ThinkReset: Bounded-Context Reset-Free Reasoning for Long-Horizon LLM Agents
- **Authors**: Joshua Warren, et al.
- **Institution**: MIT (tentative)
- **Abstract**: Long-horizon agents exhaust their context windows, and context-compaction methods quietly lose information. ThinkReset proposes compute-proportional, multi-armed resetting over bounded context windows: the agent splits a task into partial-solution episodes, checkpoints state, and resets context between episodes to claim a larger effective think budget without cross-episode interference.
- **Key Innovations**: Extended reasoning budget under fixed context; adversarial ablation shows **18.5% average improvement** over compaction and sliding-window baselines.
- **Link**: https://arxiv.org/abs/2607.28642

### 7. Mixture-of-Translators: KV Cache Translation and Sharing
- **Authors**: Jun-Seong Kim, Youngwan Lee, Yuhang Li, Gwan-Woo Kim, Yongin Kwon, Myungjoo Kang, Sunghoon Hong, Se Jung Kwon, Dongyoon Han
- **Institution**: NAVER AI Lab; SNU; KAIST (tentative)
- **Abstract**: Extended contexts bloat KV caches and raise cross-tenant privacy concerns, so caches cannot be shared. MoT trains a small per-tenant LoRA **Mixture-of-Translators** that translates one tenant's KV cache into another's distribution, enabling cross-tenant KV sharing.
- **Key Innovations**: **7.4× lower perplexity increase** at 65% memory savings; average 24% memory savings across 15 tasks and 5 LLMs.
- **Link**: https://arxiv.org/abs/2607.28979

### 8. ResKV: Adaptive Frequency-Division Compressed KV Cache
- **Authors**: Yuxuan Cheng, Tianpei Xie, et al.
- **Institution**: N/A
- **Abstract**: Sliding-window attention cannot cover all long-context patterns. ResKV compresses the KV cache in the frequency domain: it transforms attention-relevant information to frequency space, fuses frequency-domain query/key/value features to recover attention patterns, discards low-impact components, and merges low-frequency streams.
- **Key Innovations**: **8× compression with minimal accuracy loss**; up to 9.8× throughput gain over existing KV-compression methods and 6.7× over QServe.
- **Link**: https://arxiv.org/abs/2607.29591

### 9. TokTier: Stateful Tokenization Serving
- **Authors**: Shengzhong Liu, Boyuan Feng, Yu Feng, Kezhao Huang, Yufei Ding, Tarek Abdelzaher, Xiao-Chuan Wu, Avesta Sasan, Kamaljeet Singh, Jishen Zhao
- **Institution**: UC San Diego; University of Illinois (tentative)
- **Abstract**: Tokenization is a non-trivial fraction of LLM inference cost, yet mainstream tokenizers process tokens independently. TokTier is a stateful, tiered tokenization framework: a Token-Oriented Stateful Cache (TOSC) captures tokenization state, with fine-grained preprocessing, incremental state transitions, and dynamic prefix/output-buffer tuning.
- **Key Innovations**: **3.2× decoding throughput**, 50% lower time-to-first-token, 65% VRAM reduction versus strong baselines.
- **Link**: https://arxiv.org/abs/2607.29678

### 10. Data Turnstile: High-Yield Function-Calling Data Generation
- **Authors**: Siao Chen, Zhenyu Lin, Zhiyuan Lu, Chen He, Yongdong Zhang, Hao Zhao
- **Institution**: N/A
- **Abstract**: Function-calling data generation typically needs heavy human curation. Data Turnstile applies *process supervision*: it derives pseudo-intermediates from deterministic simulations, verifies final results, and lets the LLM re-derive intermediates from correct answers (deductive inference) — enabling iterative self-refinement without ground-truth training data.
- **Key Innovations**: **96.2% completeness / 88.2% correctness** with human verification rates as low as 0.2% across benchmarks.
- **Link**: https://arxiv.org/abs/2607.29250

---

## Recommendation, CTR & Advertising

### 11. SnapLGR: LLM-based Generative Retrieval for Snapchat
- **Authors**: Yue Wang, Suhyeon Lee, Lizhen Fu, Jingjing Wang, Shivam Verma, Andrew Gatto, Josh Chen, Shuyang Liu, Seungwon Hwang, Andrew Zhai
- **Institution**: Snap Inc.
- **Abstract**: Semantic generative retrieval (SGR) reframes ranking as generation — the model emits the target item's ID — with up to 20× better memorization on million-scale corpora. SnapLGR deploys a multi-stage SGR pipeline using LLMs in the *candidate* stage of Snapchat's large-scale content recommender.
- **Key Innovations**: Step-by-step SGR curriculum delivering **3× training efficiency** at no quality loss; multi-stage curriculum over targeted ID vocabularies; validated at million-scale corpus size in production.
- **Link**: https://arxiv.org/abs/2607.28895

### 12. TransX: Transformer-based Recommendation
- **Authors**: Xuan Lin, Xiaoying Gao, Hao Li, Xiaofeng Zhu, Xinlei Lv, Long Liu, Weiwei Ye, Zhaojie Luo, Yuchuan Zhou, Xiang Zhang, Xingyuan Bu, Shuqing Wu
- **Institution**: LinkedIn
- **Abstract**: Modern recommendation faces composite user-item relevance — multi-interest, recency, contacts, and historical events jointly matter. TransX is a transformer-based unified framework for next-item recommendation and CTR modeling that fuses correlation-aware multi-interest modeling with cross-attention.
- **Key Innovations**: Correlation-aware multi-interest user encoders; cross-entity alignment (people, content, skills); **+6.0% offline CTR** and **15.5% time saved** over strong baselines in LinkedIn production.
- **Link**: https://arxiv.org/abs/2607.28940

### 13. GALA: Global-to-Local Adaptive Fusion for Food-Delivery Recommendation
- **Authors**: Weixin Chen, Jiahao Liu, et al.
- **Institution**: Alibaba Group (Taobao Shangou food delivery)
- **Abstract**: Industrial recommenders combine heterogeneous modules whose embeddings are poorly aligned in scale and semantics. GALA is a global-to-local adaptive fusion framework that jointly integrates heterogeneous module representations with item-correlation signals for large-scale food-delivery recommendation.
- **Key Innovations**: Global-local adaptive fusion with explicit module alignment; A/B test on Taobao Shangou traffic shows **+5.5% CTR and +2.9% order conversion**.
- **Link**: https://arxiv.org/abs/2607.29213

### 14. RecHarness: Bandit-Routed Agentic Harness for Recommender Systems
- **Authors**: Cheng Wang, Sheng Guan, Jun Wu, Yinghong Liu, et al.
- **Institution**: Kuaishou
- **Abstract**: In-context learning (ICL) generalizes well for recommendation, but a single prompt must serve conflicting data distributions and per-domain expert models are costly. RecHarness is an agentic harness in which a generalist agent and domain-expert agents collaborate under a bandit router that also drives inference-time model intervention.
- **Key Innovations**: Generalist + domain-expert decomposition; bandit router integrated with inference-time intervention; **+2.084% average daily view volume (ADVV)** in a Kuaishou main-scene A/B test.
- **Link**: https://arxiv.org/abs/2607.29241

### 15. Think2Go: Generative Next-POI Recommendation with LLM Reasoning
- **Authors**: Di Yao, Yuchuan Song, Bihui Yu, et al.
- **Institution**: Institute of Software, Chinese Academy of Sciences (tentative); KDD 2026 oral
- **Abstract**: Next-POI models optimize accuracy but lack coherent human-readable reasoning, while LLMs hallucinate without data grounding. Think2Go unifies self-evolving latent reasoning with retrieval-augmented generation in a plug-in architecture.
- **Key Innovations**: Dual-level RL — rule-level (symbolic) and step-level (neural) alignment — to evolve reasoning chains; consistent gains across 4 public POI datasets; KDD 2026 oral.
- **Link**: https://arxiv.org/abs/2607.28997

### 16. PaletteID: Prototype-Composed Semantic Identifiers for Multimodal CTR
- **Authors**: Shuai Yang, Jinghe Wang, et al.
- **Institution**: N/A
- **Abstract**: Semantic IDs in generative recommendation encode rich features, but multimodal features are semantically heterogeneous, creating domain gaps and unstable training. PaletteID decomposes multimodal features into learnable *prototypes* — like a color palette — composed into an item identifier.
- **Key Innovations**: Prototype-composed IDs with learnable identity vectors and temporal gating; hierarchical feature-subspace alignment; a sharpness-aware optimization view of long-term training stability; strong results on 3 real-world datasets.
- **Link**: https://arxiv.org/abs/2607.29000

### 17. RCBS: Region-Constrained Contrastive User Modeling for Under-Engagement Prediction
- **Authors**: Li Zhou, Jingtao Ding, Yong Li, Zhan Zhang, Ming Zhou
- **Institution**: Tsinghua University; Karrot (SIGIR 2026 industry track)
- **Abstract**: Community platforms must predict under-engagement, but naive contrastive learning can pull genuinely negative users toward positive ones. RCBS constrains both positive and negative augmentation to sample users *within* a bounded feature region.
- **Key Innovations**: Region-constrained positive/negative augmentation; multi-aspect augmentation selection; strong gains in-market and cross-market; deployed at Karrot.
- **Link**: https://arxiv.org/abs/2607.28971

### 18. EvoReason: Self-Evolving Latent Reasoning for Generative Recommendation
- **Authors**: Yang Zhang, Wenlin Zhu, et al.
- **Institution**: N/A
- **Abstract**: Generative recommendation over semantic IDs lacks transparent reasoning. EvoReason embeds internal reasoning traces directly in the latent semantic space with a two-phase evolution: RL for coarse chain structure, then self-consistency-guided refinement for fine-grained steps.
- **Key Innovations**: Self-evolving latent reasoning; supports both forward (cause→effect) and backward (effect→cause) zero-shot reasoning; beats strong baselines including LLM-based methods on 3 real-world datasets.
- **Link**: https://arxiv.org/abs/2607.29010

### 19. GenCDSR: Generative Cross-Domain Sequential Recommendation
- **Authors**: N/A
- **Institution**: N/A
- **Abstract**: Cross-domain sequential recommendation (CDSR) is data-sparse, and generative methods rarely transfer across domains. GenCDSR pairs VQ-VAE deep semantic IDs with an *anchor token* that stitches cross-domain semantic information into a single generative CDSR model.
- **Key Innovations**: Anchor-token semantic IDs for cross-domain stitching; generative model architecture over discrete semantics; strong gains over SOTA CDSR baselines on 2 domains.
- **Link**: https://arxiv.org/abs/2607.28659

### 20. Reproducing LightMem: Naive RAG is Competitive for Agent Memory Management
- **Authors**: N/A
- **Institution**: Queensland; CSIRO; Google (tentative)
- **Abstract**: LightMem compresses LLM memories into quantized hidden states for long-horizon agents. This reproduction study finds that a far simpler "naive RAG" pipeline — plain-text summaries plus retrieval — matches or beats LightMem on 6 benchmarks, and performs an instruction-following failure analysis to explain why.
- **Key Innovations**: Rigorous reproducibility result with an actionable failure taxonomy; cautions that memory-compression gains must be measured against cheap baselines.
- **Link**: https://arxiv.org/abs/2607.29104

---

## Retrieval, Memory & Efficient Inference

### 21. QASP: Query-Adaptive Shared Prompts for Dense Retrieval
- **Authors**: N/A
- **Institution**: N/A
- **Abstract**: Dense retrievers degrade when queries are heterogeneous in type, length, and task. QASP shares one global prompt across all queries while a small set of query-adaptive experts specialize prompts per query cluster, with dynamic gating selecting the right expert.
- **Key Innovations**: **+12.4% average MRR on MS MARCO** and +2.2% average nDCG on BEIR over strong baselines; beats prior prompt-based and PEFT approaches.
- **Link**: https://arxiv.org/abs/2607.29606

### 22. HyPE: Hypothetical Prompt Embeddings
- **Authors**: Jinyu Zhang, Haotian Su, et al.
- **Institution**: N/A
- **Abstract**: Instead of embedding raw prompts, HyPE first synthesizes *hypothetical prompt embeddings* that capture a prompt's core content in the same semantic space as the model, then uses them for representation, controllable generation, and RAG candidate filtering.
- **Key Innovations**: Same-space hypothetical embeddings improve user-intent representation and retrieval relevance; plug-in compatible with existing generation pipelines.
- **Link**: https://arxiv.org/abs/2607.29402

### 23. RareSense: Rarity-Aware Similarity for Anomaly Retrieval
- **Authors**: N/A
- **Institution**: N/A
- **Abstract**: Anomaly retrieval — given an anomalous query, pulling similar anomalies from a repository for incident triage — fails for *rare* anomaly types under plain pairwise similarity. RareSense augments similarity with rarity weighting and contributes a new RareBench benchmark.
- **Key Innovations**: Rarity-aware similarity combing frequency and similarity; **+19.9% AP over pairwise-similarity baselines**; releases RareBench.
- **Link**: https://arxiv.org/abs/2607.28879

### 24. GoldenRetriever: Adaptive Retrieval in the Service Mesh
- **Authors**: N/A
- **Institution**: Aura (tentative)
- **Abstract**: Retrieval lives inside a multi-function service cluster; GoldenRetriever adaptively routes each query to a lightweight or heavy retrieval model based on function context, shares one retrieval index across functions, and uses expert-matching embeddings.
- **Key Innovations**: **+10% p50 latency** (≈2.9s→2.6s) and **+23% throughput**; adaptive model routing with a shared cross-function index.
- **Link**: https://arxiv.org/abs/2607.29019

---

## Games & Strategic Reasoning

### 25. DungeonBench: Benchmarking LLM Tactical Reasoning in Tabletop Dungeons
- **Authors**: N/A
- **Institution**: N/A
- **Abstract**: Tabletop games like D&D demand sustained multi-step tactical reasoning. DungeonBench builds 600 scenarios from 6 D&D-style modules across 3 task-complexity tiers and evaluates 15 LLMs.
- **Key Innovations**: Identifies **spatial reasoning and health/resource planning as the principal bottlenecks**; fine-grained tiered difficulty enables scaling-law-style analysis of reasoning capability.
- **Link**: https://arxiv.org/abs/2607.29577

### 26. MirrorCraft: Minecraft Agents in a Changing World
- **Authors**: Songwei Wu, Shaoqi Luo, et al.
- **Institution**: N/A
- **Abstract**: RL-trained Minecraft agents collapse when hidden rule changes invalidate learned behavior. MirrorCraft equips agents with a *belief-conditioned world model*: agents maintain a belief over world states and reason inside imagination under that belief.
- **Key Innovations**: Belief-conditioned imagination for distribution shift; retains performance across hidden rule changes where policy-only and standard world-model agents fail.
- **Link**: https://arxiv.org/abs/2607.29218

### 27. Learning Optimal Dynamic Matching Policies via Graph Neural Networks
- **Authors**: N/A
- **Institution**: N/A
- **Abstract**: Dynamic matching (ride-hailing, platform assignment) under stochastic arrivals over an infinite horizon. The paper learns matching policies from GNN embeddings of system state and provides a theoretical guarantee framework tied to deadline/queue structures.
- **Key Innovations**: GNN-state-embedded policies approaching optimality; **~2.5× improvement over greedy matching baselines** in simulation.
- **Link**: https://arxiv.org/abs/2607.28925

### 28. OCA: Organizational Consensus Algorithm for Multi-Agent LLM Systems
- **Authors**: N/A
- **Institution**: N/A
- **Abstract**: Majority voting fails in heterogeneous multi-agent LLM settings. OCA is a consensus algorithm inspired by team decision-making: individual opinion formation, formal debate, then consensus decision under an organizational structure.
- **Key Innovations**: Three-stage organizational consensus; statistically significant gains in both accuracy and answer stability over voting and debate baselines.
- **Link**: https://arxiv.org/abs/2607.28957
