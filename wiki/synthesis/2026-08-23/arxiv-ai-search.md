---
title: "arXiv AI/LLM/RecSys/Advertising Paper Search (2026-08-23)"
type: synthesis
created: 2026-08-23
updated: 2026-08-23
sources: []
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, generative-rec, world-models, agents]
---

# arXiv Recent Papers — AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

> Search date: 2026-08-23 · Scope: papers **not yet covered anywhere in the wiki** (every arXiv ID below grep-verified absent from all existing pages — including the same-day sibling digests arxiv-paper-check / game-rl-daily / tech-report-digest; zero overlap). Fresh window = Thu Aug 20 – Fri Aug 21 submissions (IDs ~2608.20xxx–2608.213xx), retrieved via arXiv API across cs.IR / cs.CL / cs.AI / cs.LG / cs.GT with topic-keyword sweeps (recommendation, CTR/click-through/advertising/ranking, sequential/user-behavior, games, LLM/agents/post-training). **12 new papers below across 4 categories.**
>
> Affiliations marked *(stated)* come from paper front matter or comments; those marked *(inferred)* are deduced from author identities and flagged accordingly; otherwise "not stated".

---

## ① Recommendation & Generative Rec (6)

### 1.1 Recommendation Quality and the Concentration of Consumption: Experimental Evidence from Netflix

| Field | Detail |
|-------|--------|
| **Authors** | Guy Aridor, Winston Chou, Nathan Kallus, Antoine Scheid, Allen Tren, Kevin Zielincki |
| **Institution** | Netflix + Northwestern Kellogg / Cornell (inferred: Kallus is Cornell, Aridor Kellogg; experiment run on Netflix) |
| **Abstract** | An 8.5M-user field experiment on Netflix's recommender system measuring how recommendation-technology improvements reshape what gets consumed. Improvements raise total consumption and users' reliance on recommendations while diffusing consumption away from superstars toward a larger set of moderately popular "middle-tail" titles; niche long-tail barely moves. |
| **Key innovations** | Largest published recommender A/B experiment of its kind; reframes the classic "recommenders polarize consumption into head+tail" claim — evidence points to **middle-tail thickening** instead. Returns to investing in mid-popularity content grow as algorithms improve and platforms scale. |
| **arXiv** | [2608.21274](https://arxiv.org/abs/2608.21274) · econ.GN, cs.IR |
| **Why it matters** | Directly contradicts the folk wisdom (and some academic modeling) that better recommenders concentrate attention. Strategic implication for any content platform: middle-tail catalog investment compounds with recommender quality. |

### 1.2 Adapting Knowledge Graphs for Behavior Denoising in Sequential Recommendation (AdaptedKG)

| Field | Detail |
|-------|--------|
| **Authors** | Zichun Jin, Zihan Zhou, Yinan Liu, Bin Wang, Xiaochun Yang |
| **Institution** | Northeastern University (China) (inferred: Xiaochun Yang's group) |
| **Abstract** | Sequential rec logs mix persistent preferences with temporary needs and incidental behavior; noisy interactions distort history representations. Existing denoisers judge interactions only via co-occurrence/order/model predictions. AdaptedKG derives calibrated KG-based evidence per training example — correcting for item popularity, graph degree, uneven coverage, and widely shared entities that inflate connectivity — without adding graph representations to the rec model itself. |
| **Key innovations** | Uses the KG purely as an external *denoising signal* rather than a model input channel; calibrates relation evidence against degree/popularity bias before trusting it. |
| **arXiv** | [2608.21243](https://arxiv.org/abs/2608.21243) · cs.IR, cs.AI |
| **Why it matters** | Complements recent distillation-based seq-rec denoising (GOD, [2608.16073](../2026-08-22/arxiv-ai-search.md)): here the noise prior comes from structured knowledge, orthogonal to interaction statistics. |

### 1.3 From a Static Multi-Level Small Semantic Codebook to a Dynamic Single-Level Large Semantic Codebook

| Field | Detail |
|-------|--------|
| **Authors** | Tianlu Xie, Xin Ku, Mingjie Sun, Yunhao Sha, Lixiang Wang, Peng Wang, Yiyu Wang, Wenjin Wu et al. |
| **Institution** | Not stated (industrial-scale traffic data suggests an industrial lab; unconfirmed) |
| **Abstract** | Generative recommenders typically encode items as multi-level residual Semantic IDs, which inflates autoregressive decoding cost and leaves the hierarchical space sparsely occupied; static codebooks also drift out of alignment with evolving traffic. Proposes replacing multi-level residual codes with **one large single-level codebook** plus a separate collaborative disambiguation token, with exposure-aware dynamic updates (temporal weight decay, EMA center updates, exposure-weighted penalty on SID changes). |
| **Key innovations** | Flattens the SID hierarchy (1 token vs RQ chains) while controlling item collisions via a dedicated collaborative token; keeps the codebook aligned with live traffic through exposure-weighted dynamic refresh. |
| **arXiv** | [2608.21012](https://arxiv.org/abs/2608.21012) · cs.IR, cs.LG |
| **Why it matters** | Pushes back on the dominant RQ-stack design (cf. [[hstu-generative-recommendation]]); if single-level large codebooks hold up industrially, generation cost and SID-refresh pipelines both simplify. Pairs naturally with yesterday's SIDScope diagnostics ([2608.18779](../2026-08-22/arxiv-ai-search.md)). |

### 1.4 One Hierarchy, Two Systems: Semantic Product IDs for Discovery-Surface Ranking and Search-Page Query Reformulation

| Field | Detail |
|-------|--------|
| **Authors** | Steven Xu, Sanjyot Thete, Saathvick Dirisala, Raghav Saboo, Nimesh Sinha, Leo Shao, Elyse Winer, Sudeep Das et al. |
| **Institution** | eBay *(stated via author team — Sudeep Das leads applied ML at eBay)* |
| **Abstract** | Multi-merchant catalogs fragment behavioral evidence for equivalent products across merchant-scoped IDs, while expert taxonomies are too coarse for fine-grained discovery. Learns one hierarchical Semantic ID representation from product-content embeddings, then reuses it in two different production systems: (a) personalized discovery ranking — aggregating consumer affinity and product performance over SID prefixes into sequence features; (b) search-page query reformulation. Offline relevance improves under controlled ablations; online ranking evaluation positive. |
| **Key innovations** | Single learned hierarchy serving both ranking features and query rewriting — SID prefixes act as a shared product-concept vocabulary across surfaces; addresses merchant-ID fragmentation endemic to marketplaces. |
| **arXiv** | [2608.20640](https://arxiv.org/abs/2608.20640) · cs.IR, cs.AI |
| **Why it matters** | Industrial confirmation that SIDs are becoming platform-wide infrastructure (ranking + search), not just a generative-retrieval trick — extends the Semantic-ID story beyond recommendation (see [[hstu-generative-recommendation]], [[netflix-generative-recommender-scaling]]). |

### 1.5 Profiling What Matters: Context-Aware Item Profiles from Large-Scale Metadata for LLM Recommenders (CAIRO)

| Field | Detail |
|-------|--------|
| **Authors** | Dojun Hwang, Seunghan Lee, Cheonyoung Park, Sara Yu, SeongKu Kang |
| **Institution** | Not stated (KAIST/UIUC-affiliated researchers, inferred) · **CIKM 2026** *(stated)* |
| **Abstract** | For LLM-based rerankers, item metadata is vast, heterogeneous and unstructured, and feature salience varies by both item and user context. Static summaries or titles lose decision-relevant signals. CAIRO structures raw metadata + reviews into objective features and subjective traits, then a lightweight profiler selects the most relevant facets conditioned on the user's context before prompting the LLM. |
| **Key innovations** | User-conditioned *item profiling* as a pre-rerank stage: salience-aware compression of item-side text per request rather than one static item description for all users. |
| **arXiv** | [2608.20801](https://arxiv.org/abs/2608.20801) · cs.IR, cs.AI, cs.CL |
| **Why it matters** | Third recent wiki-tracked pattern of putting cheap adaptive machinery *around* a frozen LLM (cf. CoRRe post-LLM CF refinement, SCoRD intent caching — both in [2026-08-21 digest](../2026-08-21/arxiv-paper-check.md)); profiling is the item-side analog. |

### 1.6 EviRank: Structured Relevance Evidence for Multimodal Image Re-ranking

| Field | Detail |
|-------|--------|
| **Authors** | Enjun Du, Siyi Liu, Zirong Chen, Xinyu Zuo, Jinwen Luo, Ruiwen Tao, Lisheng Duan, Haijin Liang et al. |
| **Institution** | Not stated |
| **Abstract** | Real image-search queries are compositional ("find this shirt in pink": entity to keep, attribute to modify, context to ignore). Existing re-rankers compress this into opaque embeddings or hallucination-prone free-form CoT. Recasts multimodal re-ranking as **semantic constraint satisfaction**: parse any query (text/image/composed) into typed criteria across six semantic slots labeled required/forbidden/ignorable; rank by evidence-conditioned verification combining deterministic rubric scoring with model judgment. |
| **Key innovations** | Rubric/checklist evaluation methodology imported from NLP into image retrieval; verifiable, auditable relevance decisions instead of a single similarity score. |
| **arXiv** | [2608.20886](https://arxiv.org/abs/2608.20886) · cs.CV, cs.LG |
| **Why it matters** | Same checklist-as-verifier move now hitting ranking stacks — echoes rubric-aligned reward learning (G-CARL, [2608.20331](https://arxiv.org/abs/2608.20331)) and AdsWorldEngine's label-grounded judging ([2026-08-22 digest](../2026-08-22/arxiv-ai-search.md)). |

---

## ② LLM Post-Training, Agents & Efficiency (3)

### 2.1 Beyond LLM-Based Reasoning: Lightweight GNNs for Agent Failure Attribution

| Field | Detail |
|-------|--------|
| **Authors** | Ting-Wei Li, Yuanchen Bei, Xiao Lin, Hanghang Tong |
| **Institution** | University of Illinois Urbana-Champaign (inferred: Hanghang Tong's group) |
| **Abstract** | Agent Failure Attribution — given a failed multi-agent trajectory, identify the faulty agents and their error types. Current approaches lean on LLMs (direct prompting, synthetic-data fine-tuning, agentic pipelines), incurring long-context and post-training costs, while even SOTA models show limited benchmark accuracy. Revisits the task with **lightweight GNNs** over a graph representation of the trajectory, questioning whether expensive generative backbones are necessary at all. |
| **Key innovations** | Reformulates trajectory attribution as graph learning; shows small discriminative models can rival much larger LLM pipelines on the task. |
| **arXiv** | [2608.18575](https://arxiv.org/abs/2608.18575) · cs.CL |
| **Why it matters** | Sets up a cost axis for the attribution literature that AgenticRAG-FP (2.2 below) stress-tests causally: cheap structural attribution first, expensive causal verification second. |

### 2.2 When Failures Propagate: Causal Failure Attribution in Agentic Retrieval-Augmented Generation (AgenticRAG-FP)

| Field | Detail |
|-------|--------|
| **Authors** | Lauren Pothuru |
| **Institution** | Not stated (single-author) |
| **Abstract** | Interventional benchmark for causal failure attribution in multi-hop agentic RAG: inject a certified fault at a specified hop, re-execute the downstream trajectory, and score diagnosers against the known intervention — does a post-hoc trace still localize the injected hop after the suffix has changed? On strict dense Claude Haiku 4.5 sweeps over 80 three-hop MuSiQue questions, coverage-based diagnosis hits 0.91 at hop 1 but 0.00 at hops 2–3. |
| **Key innovations** | Certified fault injection + counterfactual re-execution as ground truth for attribution; exposes that trace-based diagnosis collapses beyond the first hop because later steps rewrite the evidence trail. |
| **arXiv** | [2608.20627](https://arxiv.org/abs/2608.20627) · cs.CL, cs.AI |
| **Why it matters** | Hardens recent failure-attribution entries (step-credit audit in [2026-08-21 digest](../2026-08-21/arxiv-paper-check.md), GNN attribution in 2.1 above): attribution methods validated on static traces may not survive actual trajectory dynamics. |

### 2.3 Quantization-Aware Healing (QAH): Recovering Structurally Compressed, 4-Bit LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Bakbergen Ryskulov, Iker García-Ferrero, David Montero, David Jansen, Ali Hashemi, Jezabel R. Garcia, Antonio Tiene, Román Orús |
| **Institution** | Multiverse Computing (inferred: Orús is Multiverse co-founder; European patent no. listed) *(patent application stated)* |
| **Abstract** | Structural compression + 4-bit quantization jointly degrade reasoning/math/code/long-context enough to need recovery before deployment. Default QAT refits against hard labels and was observed to converge slowly and collapse past peak. QAH instead distills the 4-bit student **directly from the original uncompressed teacher** — reasoning that a compressed model's bf16 checkpoint is itself merely a distillation-recovered approximation, making it a poor target. Demonstrated on GPT-OSS 120B→60B→MXFP4. |
| **Key innovations** | Teacher choice insight: heal from the pristine original, never the compressed intermediate; positions healing as a standard pipeline stage for ship-cheap-models economics. |
| **arXiv** | [2608.20953](https://arxiv.org/abs/2608.20953) · cs.CL, cs.AI, cs.LG |
| **Why it matters** | Practical recipe for the deployment-cost curve the wiki tracks via its quantization/efficiency entries; also a caution against chained lossy artifacts — errors compound through compression pipelines. |

---

## ③ Sequential Modeling & Memory (1)

### 3.1 Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Simeng Zhang, Yilong Chen, Wenyuan Zhang, Zhenyu Zhang, Yao Chen, Junyuan Shang, Tingwen Liu |
| **Institution** | Institute of Software, Chinese Academy of Sciences (inferred: Tingwen Liu's group) |
| **Abstract** | Formalizes CoT compression as a **Context-Generation Substitution Law**: explicit reasoning context substitutes for decode-time generation. Proposes training-free Memory-Augmented Compression — build reusable reasoning memories from historical traces (patterns, key constraints, critical operations), retrieve them as prefill-side scaffolds, then generate much shorter CoT without breaking logical coherence. |
| **Key innovations** | Reframes CoT compression from "shorten the chain" to "move computation from decoding into prefill via retrieved memory" — trading cheap prefill tokens for expensive generated tokens. |
| **arXiv** | [2608.21265](https://arxiv.org/abs/2608.21265) · cs.CL |
| **Why it matters** | Connects two wiki threads: agent memory (Router-Mem, StateMemBench) and inference efficiency (adaptive reasoning budgets, speculative decoding). The substitution law is a clean economic framing for where tokens should be spent. |

---

## ④ Games & World Models (2)

### 4.1 CIVA: Critic-Induced Value-Subspace Attacks on Visual World-Model Agents

| Field | Detail |
|-------|--------|
| **Authors** | Jiancheng Wang, Mingli Zhu, Tong Zhang, Jiaqi Ruan, Wei Wang, Siyuan Liang, Dacheng Tao |
| **Institution** | Not stated (team incl. Dacheng Tao — NUS/NTU-affiliated, inferred) |
| **Abstract** | Visual world-model agents (e.g., DreamerV3) act through recurrent latent state, so frame-wise observation attacks weaken and their perturbations vary sharply over time under per-frame constraints. Key observation: along a rollout, critic-guided perturbations concentrate in a **low-dimensional subspace induced by the victim's own critic**. CIVA probes the frozen victim offline with critic-guided PGD, extracts a low-rank value-subspace via SVD, then at test time optimizes only subspace coefficients (EMA-smoothed) mapped back to pixels. Attacks value estimation directly rather than perception. |
| **Key innovations** | Attack surface = the critic's value subspace, not raw pixels; low-rank coefficient optimization makes online white-box attacks stable and temporally smooth against latent-state agents. |
| **arXiv** | [2608.21114](https://arxiv.org/abs/2608.21114) · cs.CV, cs.AI |
| **Why it matters** | Robustness angle for the world-model-agent stack the wiki tracks (DreamerV3, ForgeWM, PlayWorld benchmarks): latent-action agents inherit new, structurally narrow vulnerabilities invisible to frame-wise threat models. |

### 4.2 Graph-Operator World Models for Morphology-Parameter Generalization in Continuous Control (GraphOp-WM)

| Field | Detail |
|-------|--------|
| **Authors** | Xu Yang, Yiqin Yang, Qianchuan Zhao |
| **Institution** | Tsinghua University (inferred: Qianchuan Zhao, Tsinghua automation) |
| **Abstract** | World models trained for a fixed physical system degrade when morphology parameters (link lengths, masses, damping, actuation) change; conditioning on parameters leaves unspecified what part of the transition stays reusable. Represents bodies and kinematic relations as an attributed graph and factorizes each transition into a **morphology-independent local dynamics basis** plus a **morphology-conditioned structured operator** (node-local modulation + kinematic-truncation). Targets generalization to unseen morphologies within related articulated-robot families. |
| **Key innovations** | Explicit factorization of physics: invariant basis × parameterized operator, so changing morphology edits the operator without touching learned local dynamics — structure rather than scale for sim-to-varied-physics transfer. |
| **arXiv** | [2608.20936](https://arxiv.org/abs/2608.20936) · cs.AI, cs.RO |
| **Why it matters** | World-model robustness line adjacent to game agents (physics variation ≈ game-engine parameter sweeps); complements ForgeWM/AlayaWorld entries — here structure, there distillation, carries generalization. |

---

## Cross-Cutting Themes

1. **Semantic IDs become platform infrastructure.** eBay's dual-surface hierarchy (1.4) and the single-level codebook proposal (1.3) show SIDs graduating from generative-rec internals to cross-system vocabularies — while SIDScope (yesterday) supplies the audit tooling.
2. **Cheap adaptive machinery around frozen LLMs.** CAIRO profiling (1.5), EviRank checklists (1.6), memory-scaffold CoT (3.1): the recurring win is moving computation into prefill/profiling/verification stages around a fixed backbone, echoing CoRRe/SCoRD from the 08-21 digest.
3. **Attribution goes structural, then causal, then adversarial.** Lightweight GNNs make failure diagnosis cheap (2.1); certified-fault injection with counterfactual re-execution makes it valid (2.2); CIVA (4.1) shows the attack surface itself lives in the critic's latent subspace. The wiki's audit thread (executed-replay step-credit audits, 08-21) extends from evaluation into security.
4. **Recommender-effects empirics at scale.** Netflix's 8.5M-user study (1.1) brings econometric field-experiment rigor to the "do algorithms polarize?" debate — answer for the middle-tail: no, they fatten it.

---

## Coverage Notes (dedup)

All 12 arXiv IDs in this report were grep-verified absent from every wiki page at write time. Already covered elsewhere and therefore excluded today: SCoRD/CoRRe/RecPFN/seq-benchmark-probes/ERASE/OneModel/SIDScope/rEDMRec/OGR-slate/Netflix-multimodal/GOD/SAGA/pacing-throttling ([2026-08-22 arxiv-ai-search](../2026-08-22/arxiv-ai-search.md), [2026-08-21 arxiv-paper-check](../2026-08-21/arxiv-paper-check.md)); MemTrapBench/Cross-task skill transfer/[What is Missing from AI Post-Training AI] ([2026-08-22 conference-digest](../2026-08-22/conference-digest.md)); Router-Mem/EFCA ([2026-08-21 conference-digest](../2026-08-21/conference-digest.md)); PRP playtrace PCG ([earlier game digests](../../index.md)); **same-day siblings**: IAR + AI4AI-Bench ([2026-08-23 arxiv-paper-check](./arxiv-paper-check.md)), streamed-games IL augmentations + VLM-conditioned game agent ([2026-08-23 game-rl-daily](./game-rl-daily.md)).
