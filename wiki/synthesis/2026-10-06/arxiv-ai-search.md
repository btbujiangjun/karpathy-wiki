---
title: "arXiv AI Search 2026-10-06 — Semantic-ID Foundations, LLM Inference Efficiency, and Verifiable-Agent Environments (fresh-window sweep)"
type: synthesis
created: 2026-10-06
updated: 2026-10-06
sources: [arxiv-api-atom-xml, arxiv-html-author-blocks]
tags: [arxiv, recommendation, ctr, sequential-modeling, semantic-id, generative-recommendation, multimodal-recommendation, llm-inference, sparse-attention, kv-cache, moe, tokenizer, distillation, rlvr, agents, long-horizon, games, world-generation, serving]
---

# arXiv AI Search 2026-10-06 — fresh 2610 window sweep

> **Headline finding: this window inverts the previous one.** The 2026-10-05 report was entirely industrial production systems with live A/B numbers (7 of 8 papers). **This window is entirely academic / offline, and ZERO of the 16 featured papers report a completed online A/B test.** The affiliation mix makes the shift explicit: 10 of 16 are universities, and the two papers that mention A/B do so as a *motivating hypothetical* (LRPRec) and as *future work* (SCOUT). See §5.1 — this is the report's most load-bearing observation, not a stylistic note.

## 1. Search Metadata

| Field | Value |
|---|---|
| **Date of search** | 2026-10-06 (Tuesday) |
| **Search channel** | **arXiv export API** (`https://export.arxiv.org/api/query`), Atom XML — a **new channel for this wiki**; the 09-16 and 10-04/10-05 digests used web search and `/list` HTML scraping |
| **Window covered** | arXiv IDs **`2610.01533` → `2610.05748`**, i.e. submissions **2026-10-01 → 2026-10-05** |
| **Pool size** | **916 unique papers** parsed |
| **Candidates shortlisted** | 32 |
| **New to this wiki** | **16** (15 fresh + 1 with a **wrong title already on file**) |
| **Already in `wiki/`** | 16 (dedup ledger in §2) |
| **Affiliation recovery** | **16/16 (100%)** from arXiv HTML `ltx_authors` blocks. **Zero inferred.** |
| **Temp artifacts** | `/var/folders/.../T/opencode/arxiv/` (authorized scratch), deleted after writing |

### 1.1 Queries issued

| # | Query | Hits |
|---|---|---|
| 1 | `cat:cs.IR` (newest first) | 100 |
| 2 | `cat:cs.CL AND abs:"reinforcement"` | 60 |
| 3 | `abs:"scaling law" AND (cat:cs.LG OR cat:cs.CL)` | 60 |
| 4 | `abs:"reinforcement learning" AND abs:"game"` | 60 |
| 5 | `id:2610.*` pages 0–300 (enumeration, newest-first) | 400 |
| 6 | `id:2610.* AND (abs:"recommendation" OR abs:"CTR" OR abs:"click-through" OR abs:"ranking")` | **499** (100 fetched) |
| 7 | `id:2610.* AND (abs:"advertising" OR abs:"generative recommendation" OR abs:"semantic ID" OR abs:"user behavior sequence")` | **11** |
| 8 | `id:2610.* AND (abs:"game" OR abs:"RLVR" OR abs:"self-play" OR abs:"reinforcement learning")` | **299** (100 fetched) |
| 9 | `id:2610.* AND (abs:"scaling law" OR abs:"post-training" OR abs:"reasoning" OR abs:"long context")` | 100 fetched |
| 10 | `id:2610.* AND (abs:"LLM training" OR abs:"pretraining" OR abs:"mixture-of-experts" OR abs:"inference efficiency" OR abs:"KV cache")` | 100 fetched |

⚠️ **Coverage limitation, stated rather than hidden.** Query 5 enumerated only the **newest 400 of 5,873** `2610.*` papers, and those 400 all fall on **2026-10-04/05** — arXiv's announcement batches are back-loaded, so a newest-first enumeration over-represents the last two days. Coverage of **2026-10-01 → 10-03** therefore comes *only* from the topic-filtered queries 6–10, which are complete in their topic but not exhaustive in the month. **This sweep is topic-complete, not month-exhaustive.** A run that wants month exhaustiveness must page the whole `2610.*` range (~59 requests).

### 1.2 Rate limiting — mechanical note

The arXiv API returned **`Rate exceeded.`** (a bare 14-byte body, not an HTTP error) on the first two concurrent multi-clause attempts. Causes: the initial query used `http://` with an unencoded parenthesis, and subsequent calls were issued back-to-back. **Mitigation: `curl -G` with `--data-urlencode` for every clause, sequential requests, ≥4 s sleep between calls.** This reproduces the API-hostility finding in the [`../2026-10-05/game-rl-daily.md`](../2026-10-05/game-rl-daily.md) method disclosure — **arXiv punishes parallelism in this endpoint**, and a naive run will silently record empty result sets as "no papers found".

## 2. Dedup Ledger

32 shortlisted IDs were regex-checked against the whole of `wiki/` immediately before writing. **16 were already claimed** and are excluded from the featured sections:

| arXiv ID | Paper | Files citing | Already covered in |
|---|---|---|---|
| [`2609.39327`](https://arxiv.org/abs/2609.39327) | Generative End-to-end Ad Retrieval at Douyin | 5 | — |
| [`2609.37183`](https://arxiv.org/abs/2609.37183) | HELIX | 7 | — |
| [`2610.02144`](https://arxiv.org/abs/2610.02144) | Faynt: Competitive Melee | 5 | — |
| [`2610.02039`](https://arxiv.org/abs/2610.02039) | CARM | 5 | — |
| [`2609.39828`](https://arxiv.org/abs/2609.39828) | KUAISHOU Explorer LLM-Rec Challenge | 3 | — |
| [`2609.39007`](https://arxiv.org/abs/2609.39007) | RouteRec | 5 | — |
| [`2609.37119`](https://arxiv.org/abs/2609.37119) | Unlocking the Critic | 3 | — |
| [`2609.37311`](https://arxiv.org/abs/2609.37311) | ReMem | 2 | — |
| [`2610.01705`](https://arxiv.org/abs/2610.01705) | AgentWebRec | 2 | — |
| [`2610.02600`](https://arxiv.org/abs/2610.02600) | Asymmetric Margin Supervision | 3 | — |
| [`2609.38455`](https://arxiv.org/abs/2609.38455) | AdaM-Rec | 1 | — |
| [`2609.38999`](https://arxiv.org/abs/2609.38999) | LLM-Inferred User Context (production streaming) | 1 | — |
| [`2609.40241`](https://arxiv.org/abs/2609.40241) | Decision-Oriented Reranking | 1 | — |
| [`2609.40316`](https://arxiv.org/abs/2609.40316) | Scaling Laws for Looped MoE | 1 | — |
| [`2609.39043`](https://arxiv.org/abs/2609.39043) | Serving-Time Routing Gate | 1 | — |
| `2610.01533` | **GrIS — see §4, title on file is wrong** | 1 | [`../2026-10-03/conference-digest.md`](../2026-10-03/conference-digest.md) |

⚠️ **Two name-collision traps caught by title-level dedup.** Grepping `SCOUT` returns 3 files and `MOLT` returns 3 — **all false positives for different papers**: `SCOUT` in [`../2026-10-04/arxiv-ai-search.md`](../2026-10-04/arxiv-ai-search.md) is *Student-COnditioned Updates of the Teacher*, an on-policy-distillation framework, and `MOLT` is *MOLTBOOK*, a 30,076-agent social-network study. **ID-only dedup would have passed both; title dedup did not.** This is the **third time in four days** that ID-only dedup would have produced duplicates.

**This lane is not saturated.** The 2026-10-05 report recommended dropping this lane to a lower cadence on the grounds that keyword sweeps "can only re-surface canonical industrial systems". **That recommendation was wrong for this window** — a full fresh window yielded 15 genuinely new papers, 6 of them squarely in this wiki's core recommendation/CTR lane. The 10-05 saturation was an artifact of a *backfill* query hitting canonical papers, not of the lane. **Keep daily cadence; keep querying by ID range, not by keyword.**

## 3. Master Table

| # | Paper | arXiv | Date | Affiliation (verified) | Type | Headline result |
|---|---|---|---|---|---|---|
| 1 | GrIS | [2610.01533](https://arxiv.org/abs/2610.01533) | 10-01 | **Huawei Ireland Research Centre** | Semantic IDs | up to **+52% Hit@10** |
| 2 | LRPRec | [2610.03923](https://arxiv.org/abs/2610.03923) | 10-02 | **Zhejiang University** | LLM sequential rec | beats matched diagonal; template-free |
| 3 | SAGA + Atop-N | [2610.04753](https://arxiv.org/abs/2610.04753) | 10-03 | **Technion** + Crusoe AI + Corma | Attention | **>2× decoding** at long ctx |
| 4 | Social Deduction RFT | [2610.04261](https://arxiv.org/abs/2610.04261) | 10-03 | **PKU** + Alibaba + UIC | Game/RL | terminal reward fails; social reading works |
| 5 | HarA | [2610.04344](https://arxiv.org/abs/2610.04344) | 10-03 | **UIUC** + **Meta** | RLVR | FGW-barycenter credit assignment |
| 6 | DiffGate | [2610.04596](https://arxiv.org/abs/2610.04596) | 10-03 | **IISc** + **Snap Inc.** | Distillation | code pass@8 **+1.6 / +5.7** |
| 7 | ASCENT | [2610.05303](https://arxiv.org/abs/2610.05303) | 10-04 | **UNSW Sydney** | Agents | test-time weight updates, no memory |
| 8 | WorkForge | [2610.04906](https://arxiv.org/abs/2610.04906) | 10-04 | **Tencent** LLM Dept + **Fudan** (26 authors) | Agents/RLVR | GDPVal **45.5 → 73.6** |
| 9 | CutBCE | [2610.05559](https://arxiv.org/abs/2610.05559) | 10-04 | **Google Cloud** | RecSys infra | **−65.7% HBM, 225.9% throughput** |
| 10 | OpticalRec | [2610.05432](https://arxiv.org/abs/2610.05432) | 10-04 | **UCSD** + Alibaba + UIUC + TAMU + PolyU + CUHK | Multimodal rec | renders text as glyphs |
| 11 | SCOUT | [2610.05619](https://arxiv.org/abs/2610.05619) | 10-04 | **Airbnb** | Search/cold-start | IMR@18 **+12.3%** |
| 12 | CoBPE | [2610.05597](https://arxiv.org/abs/2610.05597) | 10-04 | **Hebrew University of Jerusalem** | Tokenizer | **−30% sequence length** |
| 13 | Code2Games | [2610.05033](https://arxiv.org/abs/2610.05033) | 10-04 | **La Trobe** + **Peking University** | Games | Blender → UE5, GameCode4D |
| 14 | MOLT | [2610.05748](https://arxiv.org/abs/2610.05748) | 10-05 | **Seoul National University** | Serving | SLO **≥99.7%**, **1.9–3.3×** tuning |
| 15 | CIPHER-MoE | [2610.05744](https://arxiv.org/abs/2610.05744) | 10-05 | **Tongji** + **Cornell** + HIT-Shenzhen + Shenzhen Loop | MoE training | **−64.9pp** expert imbalance |
| 16 | CreGR | [2610.05670](https://arxiv.org/abs/2610.05670) | 10-05 | **UTS** + **NYU Abu Dhabi** | Generative rec | credibility-aware SIDs |

## 4. ⚠️ Metadata Discrepancy — `2610.01533` GrIS has the wrong title on file

[`../2026-10-03/conference-digest.md`](../2026-10-03/conference-digest.md) §GrIS records this paper as:

> "**GrIS: Scaffolded Generation with Item-Specific Representations for Slate Recommendation**"

**The actual title on arXiv is:**

> "**Neither Black nor White: Balancing Semantic and Collaborative Signals with Graph-Informed Semantic IDs (GrIS)**"

These are **different papers sharing an acronym and an ID**. The digest's version describes *item-specific representation scaffolding for slate recommendation*; the real paper is about **reframing Semantic ID construction as recursive clustering over a graph** carrying semantic nodes and collaborative edges. The digest's surrounding analysis is also affected: it places `2610.01533` in a lineage with `2610.01139` (unified semantic-ID embedding space, Amazon) and `2610.01967` (context-qualified IDs, ByteDance), concluding that "context-qualified IDs are strictly more expressive than item-specific scaffolding" is an open question. **The real paper answers a different question**, and its answer is that the two axes (graph construction, partition algorithm) are **orthogonal and composable** — which weakens that lineage claim.

✅ **The digest's *affiliation* was right**: the HTML author block confirms all six authors (Aleksei Medvedev, Alejandro Ariza-Casabona, Steven Derby, Gonzalo Fiz Pontiveros, Xinyang Shao, Florian Spiess) at **Huawei Ireland Research Centre, Dublin** — matching the "Huawei" the digest recorded, with `aleksei.medvedev@huawei.com`.

**Recommendation**: correct the title in the 2026-10-03 digest, and re-examine the three-paper lineage claim in its §10.4.

## 5. Per-Paper Detail

### Lane A — Recommendation / CTR / Sequential Modeling

---

#### 1. GrIS: Neither Black nor White — Graph-Informed Semantic IDs

- **arXiv**: [`2610.01533`](https://arxiv.org/abs/2610.01533) — *see §4: the title on file elsewhere in this wiki is wrong*
- **Submitted**: 2026-10-01 · **Authors**: Aleksei Medvedev, Alejandro Ariza-Casabona, Steven Derby, Gonzalo Fiz Pontiveros, Xinyang Shao, Florian Spiess · **Institution**: **Huawei Ireland Research Centre, Dublin, Ireland** (verified from HTML author block)

**Abstract (verbatim):**
> Existing work on Semantic IDs (SIDs) for generative recommendation treats SID construction as a representation learning problem: encode items into a quantised latent space and read off codes. We argue this view is incidental. SID construction is, at heart, a recursive clustering problem, and once stated this way the natural object to cluster is a graph whose nodes carry semantic content and whose edges carry collaborative signal; SID assignment becomes a hierarchical graph partition. This reframing yields a unified framework, Graph-Informed Semantic IDs (GrIS), that subsumes prior approaches rather than displacing them. RQ-VAE and RQ-KMeans are recovered as the special case where the graph is empty, exposing content-only quantisation as one corner of a larger design space along two so-far-collapsed axes: graph construction and recursive partition algorithm. We explore two contrasting instantiations: RecDMoN, which performs hierarchical assignment via differentiable graph pooling, and RQ-GAE, which extends RQ-VAE with graph-aware item representations and a graph reconstruction objective. On multiple real-world datasets, GrIS consistently improves over CF-aware SOTA, with gains of up to +52% Hit@10. Because graph construction and partition are explicit, separately configurable components, improvements on either axis can be combined and evaluated systematically.

**Key innovations:**
- **The reframing is the contribution, and it is a *unification*, not a competitor.** GrIS's strongest structural move is that **RQ-VAE and RQ-KMeans are recovered as special cases** (empty graph). This is the same "subsume, don't displace" framing that [[OneRanker]] and GR4AD used architecturally, applied to Semantic ID construction.
- **Two previously-collapsed design axes are made explicit and separately configurable**: (1) *graph construction*, (2) *recursive partition algorithm*. Because they are separable, **gains on either axis compose** — which is a testable claim the field has been unable to make about competing SID schemes.
- **Two contrasting instantiations probe the axis**: **RecDMoN** (differentiable graph pooling for hierarchical assignment) and **RQ-GAE** (RQ-VAE + graph-aware item representations + graph reconstruction objective).
- **Result**: up to **+52% Hit@10** over CF-aware SOTA on multiple real-world datasets. Offline only.
- ⚠️ **Directly relevant to this wiki's Semantic ID thread** — pairs with the `2610.01139` / `2610.01967` lineage flagged in the 2026-10-03 digest, and with the UA-SID channel in [[GR4AD]]. This is the strongest candidate in this window for a `wiki/papers/recommendation/` page.

---

#### 2. CreGR: Generate What You Can Trust — Content Credibility in Generative Recommenders

- **arXiv**: [`2610.05670`](https://arxiv.org/abs/2610.05670)
- **Submitted**: 2026-10-05 · **Authors**: Zhuo Cai, Guanghao Wu, Shoujin Wang, Peilin Zhou, Victor W. Chu · **Institutions**: **Data Science Institute, University of Technology Sydney, Australia** (Cai, Wu, Wang, Chu) + **New York University Abu Dhabi** (Zhou) — verified from HTML author block

**Abstract (verbatim):**
> Generative recommendation (GR) represents items with semantic IDs (i.e., discrete token sequences) and generates target item tokens as recommendations. Despite its promising results, existing methods predominantly optimize for accuracy while neglecting the credibility of the recommendations they generate. This oversight inevitably exposes users to uncredible content (e.g., fake news) with serious societal consequences, including user distrust, reputation harm to platforms, and broader social instability. To address this critical yet underexplored challenge, we propose CreGR, the first credible GR model that jointly tackles content credibility across the two core stages of GR: tokenization and generation. In the tokenization stage, we design a new credibility-aware tokenizer that explicitly encourages the model to learn discriminative tokens respectively for credible and uncredible items, thereby disentangling credibility signals at the token level. Building on this, in the generation stage, we propose a novel accuracy-preserving and credibility-oriented generator grounded in discrete diffusion. Specifically, we introduce an asymmetric masking probability reduction strategy that selectively diminishes the contribution of tokens associated with uncredible content to the generation process, while leaving tokens encoding user preference signals unaffected so as to preserve recommendation accuracy. Experiments on three real-world datasets demonstrate the effectiveness of CreGR.

**Key innovations:**
- **First paper in this window to treat generative recommendation as a *content-safety* problem rather than an accuracy problem.** The framing — accuracy-optimized GR "inevitably exposes users to uncredible content" — is an argument that the field's dominant objective function is incomplete, not merely improvable.
- **Attacks both GR stages**, which almost no paper does: **tokenization** (a credibility-aware tokenizer that learns *discriminative* tokens separately for credible and uncredible items, disentangling credibility at the token level) and **generation** (grounded in **discrete diffusion**, not autoregressive decoding).
- **The accuracy/credibility decoupling is the clever part.** An **asymmetric masking probability reduction** selectively down-weights tokens carrying uncredible content *while leaving user-preference tokens untouched* — i.e. credibility is enforced on a **different channel** than relevance, so the two objectives do not fight. This is the same architectural-separation instinct as OneRanker's decoupled task tokens, applied to safety rather than business value.
- ⚠️ **No numbers in the abstract.** "Experiments on three real-world datasets demonstrate the effectiveness" — no metrics, no magnitudes, no baselines named. **Datasets are unnamed.** Treat as a directional claim, not a measured result.
- ⚠️ **Author-name trap**: the author list contains **Shoujin Wang** and **Peilin Zhou**, names associated with industrial ads teams elsewhere in this wiki's corpus. **Both are here at UTS/NYU Abu Dhabi.** Had the affiliation been inferred from names, this paper would have been badly misattributed. Recorded because this wiki has made exactly that inference error before (§4.1 of the 2026-10-05 report).

---

#### 3. CutBCE: Cut Binary Cross Entropy — Loss & Gradient Kernels for Sequential Recommendation

- **arXiv**: [`2610.05559`](https://arxiv.org/abs/2610.05559) · **Code**: `github.com/AI-Hypercomputer/RecML`
- **Submitted**: 2026-10-04 · **Authors**: Yaoyiran Li, Haowen Ning, Mohamed Hammad · **Institution**: **Google Cloud** (London, UK + Mountain View, USA) — verified from HTML author block

**Abstract (verbatim):**
> Industrial sequential recommender systems operate over massive item catalogs (e.g., 10^5--10^7 items). Multi-label recommendation models are trained with Binary Cross-Entropy (BCE) loss over the full vocabulary, but standard BCE materializes a dense [B, N, V] logits tensor in High Bandwidth Memory (HBM), incurring prohibitive $O(BNV)$ memory and fatal Out-Of-Memory (OOM) errors. While chunked loss optimizations exist for Softmax Cross-Entropy in LLMs, large-scale multi-label BCE optimization remains unexplored across deep learning ecosystems. We propose CutBCE, an exact, hardware-accelerated BCE loss and gradient operator implemented in JAX and Pallas for large-vocabulary workloads. CutBCE introduces (1) an exact fused reformulation evaluating dense background loss and sparse target corrections; (2) a custom Vector-Jacobian Product (VJP) with a dedicated Pallas TPU backward kernel computing logit tiles on-chip in both passes so logits and their gradients never reside in HBM; (3) dynamic VMEM budgeting and sharding-aware collective hoisting for distributed meshes; and (4) count-based zero-overhead training metrics. On single-chip TPU v5e/v6e mini-benchmarks, CutBCE eliminates OOM errors with up to 91.9% speedup. On 8-chip TPU slice training for multi-label SASRec with 876k items (Yambda-50M), CutBCE reduces peak HBM by 65.7% (>14 GiB saved per chip) and increases training speed by 225.9% with comparable accuracy. CutBCE is open-sourced at https://github.com/AI-Hypercomputer/RecML/blob/main/recml/core/ops/binary_cross_entropy_ops.py.

**Key innovations:**
- **Names an exact gap that recsys and LLM work have ignored in opposite directions**: *"While chunked loss optimizations exist for Softmax Cross-Entropy in LLMs, large-scale multi-label BCE optimization remains unexplored."* **The LLM community's memory-efficient loss tricks have not been ported back to recommendation**, where BCE-over-full-vocabulary is the standard multi-label objective. This is a genuine technology-transfer gap, not a novel-algorithm gap.
- **The mechanism is exact, not approximate.** Dense background loss + sparse target corrections, fused; plus a custom VJP with a **Pallas TPU backward kernel that computes logit tiles on-chip in both passes**, so **logits and gradients never reside in HBM**. Worth noting for the "one model, several stages" thread in §5.3: this is a *memory* analogue — move the expensive thing off the critical resource.
- **Measured on real industrial scale**: multi-label **SASRec, 876k items, Yambda-50M, 8-chip TPU slice**. **−65.7% peak HBM (>14 GiB/chip)**, **225.9% training speedup**, accuracy comparable. Single-chip TPU v5e/v6e: OOM eliminated, **up to 91.9% speedup**.
- **Open-sourced** — a rare instance in this corpus where the industrial artifact is actually reachable.
- ⚠️ **Hardware-bound.** TPU/JAX/Pallas only; no GPU/CUDA path is claimed. "Comparable accuracy" is the accuracy claim — **no accuracy improvement, and no online/business metric.** This is a pure cost paper and should be read as one.

---

#### 4. OpticalRec: Unified Optical Vision-Language Representation for Multimodal Recommendation

- **arXiv**: [`2610.05432`](https://arxiv.org/abs/2610.05432)
- **Submitted**: 2026-10-04 · **Authors**: Yueqi Wang†, Zitian Guo, Yupeng Hou, Yifei Wang, Kibum Kim, Zhenrui Yue, Shuo Xing, Haodong Li, Heming Xia, Renrui Zhang, Zhengzhong Tu, Julian McAuley (12) · **Institutions**: **UC San Diego** (Wang†, Guo, Hou, Kim, Li, McAuley), **Alibaba Group** (Yifei Wang), **UIUC** (Yue), **Texas A&M** (Xing, Tu), **HK PolyU** (Xia), **CUHK** (Zhang) — verified from HTML author block

**Abstract (verbatim):**
> Recent advances in vision-language modeling have substantially improved multimodal encoding, retrieval and reasoning. Yet for multimodal recommendation, encoding rich item vision-language semantic interactions remains a long-standing bottleneck, which hampers accurate item representation learning and user-item matching. Mainstream approaches primarily adopt independent encoding of vision and language modality followed by rigid late fusion such as concatenation, inherently omitting native vision-language interactions and introducing cross-modal semantic distortion. To address this challenge, we propose OpticalRec, the first visual-space unified encoding paradigm for multimodal collaborative filtering, a fundamental recommendation setting. Instead of isolated modality-specific encoding, OpticalRec renders item textual metadata as visual glyphs, enabling native image-text interaction within the visual encoder - the perceptual encoding level. The resulting representations are further processed by the language decoder - the semantic encoding level, allowing OpticalRec to exploit the dual-attention mechanism of modern vision-language models that previous encoding methods omitted. OpticalRec's efficacy is theoretically supported by mutual information analysis and empirically demonstrated through superior performance across strong baselines and benchmarks. As a plug-and-play module, OpticalRec (1) introduces minimal cost, (2) is robust against rendered text font, color and layout, etc., and (3) integrates seamlessly into existing multimodal collaborative filtering models.

**Key innovations:**
- **The move is genuinely unexpected and worth the paper: render the text as pixels.** Instead of encoding image and text separately and late-fusing (concatenation), OpticalRec **renders item textual metadata as visual glyphs** so that native image-text interaction happens *inside* the visual encoder. Modality unification by **abandoning the text modality at the encoder**, not by adding a fusion layer.
- **The claimed cost of the status quo is specific**: separate encoding + rigid late fusion "inherently omits native vision-language interactions and introduces **cross-modal semantic distortion**". The contribution is framed as removing a *structural* deficiency, not chasing a benchmark delta.
- **Explicitly recovers VLM capability that recsys had been leaving on the table** — the **dual-attention** mechanism of modern VLMs, which "previous encoding methods omitted". The argument is that multimodal *recommendation* has been reimplementing a weaker encoder than multimodal *understanding* already provides.
- **Two-level encoding story**: visual encoder = perceptual level; language decoder = semantic level.
- **Deliberately defended on robustness, which is the obvious objection to glyph rendering** — "robust against rendered text font, color and layout". If that claim is soft, the method is brittle; this is the first thing to check in the full text.
- ⚠️ **The abstract states no numbers** — "superior performance across strong baselines and benchmarks", supported by "mutual information analysis". Datasets and metrics are unnamed here.

---

#### 5. SCOUT: Supply-Aware Cold-Start Proactive Query Suggestion for Travel Search

- **arXiv**: [`2610.05619`](https://arxiv.org/abs/2610.05619) · **Venue**: **CIKM 2026 Workshop on Generative, Retrieval-augmented, and Agentic Intelligence for Personalization**
- **Submitted**: 2026-10-04 · **Authors**: Hao Li, Shashank Reddy, Kedar Bellare, Ashish Jain, Stephanie Moyerman · **Institution**: **Airbnb, Inc., USA** (all five, verified from HTML author block)

**Abstract (verbatim):**
> Generative query suggestion, powered by Large Language Models (LLMs), has become increasingly popular in search and conversational systems to reduce user friction and guide intent formulation. Existing approaches align suggestions with user preferences (e.g., clicks or conversions). This works for open-ended applications like chatbots and personal assistants, where the result space is unconstrained or historical user free-text queries are abundant. However, applying these methods to travel search presents two limitations. First, travel search is fundamentally constrained by physical inventory; a query (e.g., "romantic beachfront villa") may yield abundant results in Bali but few in Tokyo, so aligning with user preferences is not by itself grounded in what can be offered. Second, travel platforms traditionally rely on faceted search interfaces with no free-text queries. This creates a cold-start problem: without historical query logs there is no demand-side data for alignment, and without a seed query at request time, suggestions must be generated proactively from structured context alone. To address these challenges, we propose SCOUT, a bootstrapping framework for supply-aware proactive query suggestion. SCOUT overcomes the data gap by substituting missing demand-side user feedback with supply-side system feedback. It treats the search engine as a reinforcement learning environment, deriving a dense reward from the production reranker's query-listing match scores, and optimizes the policy with Group Relative Policy Optimization (GRPO). SCOUT improves inventory match rate (IMR@18) by 12.3% while preserving diversity, matching a compute-intensive best-of-8 policy at zero marginal inference cost and making supply-aware suggestion deployable on a real-time travel search path.

**Key innovations:**
- **The supply/demand substitution is the idea.** Demand-side alignment (clicks, conversions) is the standard objective for generative query suggestion and it **cannot bootstrap** a faceted-search platform with no query logs. SCOUT **substitutes supply-side system feedback for missing demand-side feedback** — the reranker's own query-listing match score becomes a dense reward.
- **Production reranker as reward oracle** — a nice systems trick: the component that *ranks* becomes the *grader*, so no new labeling infrastructure is needed.
- **RL where the environment is the search engine itself**, optimized with **GRPO**. Notable that GRPO has migrated out of reasoning-RL into a production search loop.
- **Efficiency claim is the strongest part**: IMR@18 **+12.3%** while **preserving diversity**, and — the headline — **matching a compute-intensive best-of-8 policy at zero marginal inference cost**. Cost-parity-with-8×-sampling is a more useful production claim than the +12.3% itself.
- ⚠️ **CRITICAL: the online A/B is future work, not a result.** The limitations section of the paper states: *"As the interface rolls out, our **ongoing work** focuses on **large-scale online A/B testing**... This data will drive our transition from pure supply-awareness to a balanced, multi-objective alignment strategy."* The system is **deployed on a real-time travel search path** but **supply-only**; demand-side validation has not happened. **Read IMR@18 +12.3% as an offline/proxy result.**

---

#### 6. LRPRec: Learning Robust Personalized Prompts for LLM-Driven Sequential Recommendation

- **arXiv**: [`2610.03923`](https://arxiv.org/abs/2610.03923)
- **Submitted**: 2026-10-02 · **Authors**: Xiaolin Zheng, Qiyong Zhong, Jiajie Su, Xiang Chen · **Institution**: **Zhejiang University, Hangzhou, China** (all four, verified from HTML author block)

**Abstract (verbatim):**
> LLM-driven sequential recommendation formulates next-item prediction as autoregressive generation conditioned on natural-language prompts. However, minor wording changes in semantically equivalent prompts can cause substantial performance fluctuations, undermining robustness and requiring costly manual prompt engineering. Continuous prompt learning reduces template dependence but faces two interacting challenges: shared task-level instructions lack user-specific reasoning guidance, while gradient updates can push continuous prompts outside the LLM's effective semantic space. Injecting personalized signals can further amplify this semantic drift. To address these challenges, we propose LRPRec, a learnable prompting framework that initializes continuous instruction prompts from discrete templates and introduces two complementary mechanisms. Personalized prompt injection encodes user behavior into a preference embedding and additively injects it into shared prompts, enabling parameter-efficient user-level adaptation. A semantic drift constraint regularizes the shared prompts within a trust region around their initialization anchors to preserve semantic validity during optimization. By constraining the shared component while allowing additive personalization, LRPRec decouples stability from expressiveness. Extensive experiments on three benchmark datasets demonstrate consistent improvements over strong baselines while eliminating the need for manual tuning of background and task inference templates.

**Key innovations:**
- **Frames prompt sensitivity as a *correctness* problem, not a nuisance.** "Minor wording changes in semantically equivalent prompts can cause substantial performance fluctuations" — for a system where the prompt is part of the deployed artifact, this is a robustness bug with operational cost.
- **Diagnoses two interacting failure modes of continuous prompt learning**: (a) shared task-level instructions carry no user-specific reasoning guidance; (b) **gradient updates push continuous prompts outside the LLM's effective semantic space**. It then notes that adding personalization *amplifies* (b) — so the two fixes are in tension.
- **The resolution is an asymmetric constraint**: **constrain the shared component, leave the personalized component free.** A trust region around initialization anchors for shared prompts + **additive** preference-embedding injection. **Stability and expressiveness are decoupled by construction** — the shared part cannot drift, so all expressiveness has to come through the additive channel.
- **Initialization from discrete templates** is a small but load-bearing detail: the trust region is anchored at a *semantically validated* point rather than at random.
- ⚠️ **No numbers in the abstract.** Three benchmark datasets, "consistent improvements over strong baselines", unnamed.
- ⚠️ **The paper's "A/B test" mention is not an A/B test.** It appears only in the *motivation* for deployment robustness: *"in real-world deployment, the inference prompt may need to be modified (e.g., for A/B testing, multilingual adaptation, or system updates)"*. **This is a hypothetical about deployment fragility, not a reported experiment.** No online result is claimed anywhere in the paper.

---

### Lane B — LLM Training, Scaling, and Inference Efficiency

---

#### 7. SAGA + Atop-N: More Value per Key — Asymmetric Sparse Attention for Faster LLM Decoding

- **arXiv**: [`2610.04753`](https://arxiv.org/abs/2610.04753) · **Venue**: **NeurIPS 2026**
- **Submitted**: 2026-10-03 · **Authors**: Noam Elata†, Itay Lamprecht, Mikey Shechter, Daniel Ohayon, Itay Hubara, Daniel Soudry (6) · **Institutions**: **Technion – Haifa, Israel** (Elata, Lamprecht, Shechter, Ohayon), **Crusoe AI**, **Corma**, **one "Stealth Startup"** — verified from HTML author block

**Abstract (verbatim, note the dropped leading "A" in the source rendering):**
> utoregressive generation in Large Language Models (LLMs) is constrained by the memory and computational demands of attention mechanisms. Sparse attention methods mitigate this cost by selecting only high-probability entries of the attention matrix. We observe that in many such methods, this renders the probability-value multiplication negligible, shifting the bottleneck to the query-key step. Key heads can therefore be reduced to accelerate inference, while retaining more value heads preserves capacity with limited additional decoding cost. We introduce Sparse Asymmetric Group-Query Attention (SAGA), which decouples key and value head counts to exploit this principle, and pair it with approximate top-N (Atop-N) attention, a simple sparse attention method designed to study the interaction between sparsity and head-count asymmetry. We formalize the benefits of this asymmetry theoretically and validate them empirically through latency measurements and quality evaluations on models up to 1.5B parameters. Together, SAGA and Atop-N achieve end-to-end decoding speedups exceeding $2\times$ over our full-attention GQA baseline at long contexts. Models trained from scratch with SAGA nearly match the quality of comparable GQA variants on the evaluated benchmarks. To facilitate adoption, we introduce an efficient fine-tuning method that converts pretrained models to the SAGA architecture, enabling practitioners to benefit from our approach without costly retraining.

**Key innovations:**
- **The observation is the contribution, and it is a bottleneck-diagnosis argument.** Sparsifying the attention matrix (keeping only high-probability entries) makes the **probability–value multiplication negligible**, which **shifts the bottleneck to the query–key step**. Consequence: **key heads are the expensive part and can be cut; value heads are cheap and preserve capacity.**
- **SAGA decouples key-head count from value-head count** — an asymmetry GQA cannot express, because GQA ties them. This is a *new degree of freedom in the GQA design space*, and it follows from the bottleneck shift rather than from a heuristic search.
- **Atop-N** is deliberately a **simple** sparse attention method, framed as a *controlled instrument* for isolating the sparsity × head-asymmetry interaction rather than as a new sparse-attention method in itself.
- **Result**: **>2× end-to-end decoding speedup** over a full-attention GQA baseline at long contexts; models trained from scratch with SAGA **"nearly match"** GQA quality on evaluated benchmarks, up to **1.5B parameters**.
- **Migration path matters for adoption claims**: an efficient **fine-tuning conversion** from pretrained GQA to SAGA, so no retraining from scratch is required.
- ⚠️ **Scale ceiling is 1.5B.** The 2× claim is measured at ≤1.5B; there is no evidence here about frontier-scale behaviour, and head-count asymmetry interacts with model scale in ways not tested.

---

#### 8. CoBPE: More Than Words — Compositional Tokenization for Efficient Language Models

- **arXiv**: [`2610.05597`](https://arxiv.org/abs/2610.05597) · **Venue**: **COLM 2026**
- **Submitted**: 2026-10-04 · **Authors**: Yuval Reif, Guy Kaplan, Roy Schwartz · **Institution**: **The Hebrew University of Jerusalem** (all three, verified from HTML author block)

**Abstract (verbatim):**
> Language models process and generate text sequentially in token units, and the tokenizer determines how much text each inference step covers. Under standard tokenization, a short English phrase such as "On the table." is usually produced as four separate predictions for the preposition (On), article (the), noun (table), and punctuation (.), where each consumes a sequence position and adds inference cost. We introduce CoBPE, a compositional tokenization approach that represents such phrases as a lexical base token (table) attached with a small set of reusable surface modifiers, composed in embedding space at input and predicted jointly at output. In controlled pretraining from scratch at 780M and 1.3B scales, CoBPE shortens sequences by 30% and improves average downstream performance by 1.2 points relative to standard BPE under matched training compute. Our results suggest that part of what is now expressed through token sequences can instead be modeled through structured representations, opening a broad design space for more token-efficient and capable language models.

**Key innovations:**
- **Attacks inference cost at the tokenizer, not the architecture.** The motivating observation is that function words (prepositions, articles, punctuation) each **consume a sequence position** — i.e. a large fraction of decode steps carry almost no semantic content.
- **CoBPE = lexical base token + small set of reusable surface modifiers**, **composed in embedding space at input and predicted jointly at output.** The composition is learned and continuous, not a lookup table — which is what makes it different from naive factorized tokenization.
- **Controlled comparison, which is the right experiment**: pretraining **from scratch** at **780M and 1.3B**, **matched training compute**, against standard BPE. Result: **−30% sequence length, +1.2 average downstream points**.
- **The framing is the interesting part**: "part of what is now expressed through token sequences can instead be modeled through **structured representations**" — tokenizer design as a *representation* decision, not a compression heuristic.
- ⚠️ **English-centric by construction.** The worked example is English morphology ("On the table."). The abstract makes no claim about morphologically rich or non-space-delimited languages, where the base-token/modifier split would need to be re-derived. **A "token-efficient" result measured only on English is a narrow claim.**
- ⚠️ **Scale ceiling 1.3B**, from-scratch only; no interaction with multilingual vocabularies or existing pretrained checkpoints.

---

#### 9. DiffGate: Difficulty-Gated Teacher Guidance for On-Policy Distillation

- **arXiv**: [`2610.04596`](https://arxiv.org/abs/2610.04596) · **Status**: *Preprint Under Review*
- **Submitted**: 2026-10-03 · **Authors**: Karn Tiwari, Varnith Chordia, Prathosh A P · **Institutions**: **Indian Institute of Science, Bengaluru, India** + **Snap Inc.** — verified from HTML author block

**Abstract (verbatim):**
> On-policy distillation (OPD) has emerged as a widely used paradigm for post-training large language models, reducing the train--test mismatch of conventional distillation by supervising the student on its own generated trajectories. However, existing OPD objectives remain largely token-local and outcome-agnostic, optimizing teacher--student agreement at each prefix despite reasoning quality being determined at the trajectory level. Reinforcement learning with verifiable rewards (RLVR), particularly Group Relative Policy Optimization (GRPO), provides complementary outcome-level supervision but suffers from sparse rewards and coarse credit assignment. We show that OPD and RLVR exhibit complementary blind spots: teacher signals provide dense local guidance but are weakly aligned with rollout correctness, whereas group-relative rewards capture task success but provide coarse token-level credit and vanish on all-failure groups. We introduce DiffGate, an outcome-gated objective that combines GRPO with selective, bounded teacher guidance. Teacher supervision is applied only to failed trajectories, scaled by group difficulty, and smoothly bounded to prevent extreme teacher--student discrepancies from dominating optimization. The verifier therefore determines *which trajectories* receive teacher guidance, while the teacher provides dense token-level update directions within those trajectories. Across Qwen3-0.6B and Qwen3-1.7B students, DiffGate improves code avg@8 over matched GRPO by $+1.7$ and $+1.8$ points and pass@8 by $+1.6$ and $+5.7$ points, respectively. On mathematics, avg@8 remains within $0.5$ points of GRPO while pass@8 improves by $+1.1$ and $+3.9$ points. Overall, DiffGate improves pass@8 across all four model--domain settings, demonstrating improved solution coverage under our evaluation protocol.

**Key innovations:**
- **This is the same argument as [[SCOUT]] (`../2026-10-04/arxiv-ai-search.md`, the on-policy-distillation teacher paper) — arrived at independently, and it now has the empirical backing.** The 10-04 SCOUT paper claimed OPD teachers degrade on student-generated prefixes; DiffGate establishes the complementary half: **OPD and RLVR have complementary blind spots** and should be combined rather than chosen between.
- **The blind-spot statement is crisp and is the contribution**: teacher signals are **dense but weakly aligned with rollout correctness**; group-relative rewards **capture success but give coarse token credit and vanish on all-failure groups**. Neither is sufficient.
- **Gating design: the verifier decides *which* trajectories get teacher guidance; the teacher decides *how* to move tokens within them.** A clean division of labor between two signals with different failure modes.
- **Three guards, each aimed at a specific pathology**: supervision **only on failed trajectories** (don't overwrite what already worked), **scaled by group difficulty** (harder groups get more teacher signal), and **smoothly bounded** (so extreme teacher–student discrepancies cannot dominate optimization).
- **Results**: code avg@8 **+1.7 / +1.8** and pass@8 **+1.6 / +5.7** over matched GRPO (Qwen3-0.6B / 1.7B); math avg@8 within **0.5** of GRPO while pass@8 **+1.1 / +3.9**.
- **Read the two metrics differently**: the **avg@8 ≈ neutral, pass@8 clearly up** pattern is the signature of *coverage* rather than *quality* — DiffGate finds more distinct correct solutions without raising the mean. The paper says as much ("improved solution coverage"). For reasoning, **higher pass@k with flat avg@k is often what you want** (more attempts succeed), but it is not the same as a better model.
- ⚠️ **pass@k is coverage-sensitive to sampling budget**, and the paper is explicit that this is "under our evaluation protocol". Do not compare these pass@8 numbers against papers using different k or different sampling counts.

---

#### 10. CIPHER-MoE: Balancing Efficiency and Routing Fidelity in Trillion-Scale MoE Training

- **arXiv**: [`2610.05744`](https://arxiv.org/abs/2610.05744) · **Status**: *code "will be released soon"*
- **Submitted**: 2026-10-05 · **Authors**: Jing Li, Jian Meng*, Yingmeng Gao, Suming Qiu, Linyuan Qiu, Dongfang Li, Baotian Hu, Binfan Zheng, Rongqian Zhao, Weijian Sun, Xin Chen (11) · **Institutions**: **Tongji University**, **Cornell University**, **Harbin Institute of Technology, Shenzhen**, **AI Training Platform Team, Shenzhen Loop Area Institute** — verified from HTML author block

**Abstract (verbatim):**
> Mixture-of-Experts (MoE) has been widely adopted in recent large language model (LLM) architectures. However, scaling up MoE in LLM training introduces system-level challenges on training, where non-uniform token routing can lead to highly imbalanced workloads across experts and devices, further destabilizing the training process. With trillion-scale LLMs, imbalanced expert workloads further amplify the resource cost of MoE training, resulting in degraded training efficiency and hardware utilization for underloaded experts, while hot experts require additional resources to accommodate excessive workloads. Recent studies address imbalanced MoE training through intricate parallelism strategies or resource reallocation. However, these system-level approaches often introduce additional resource requirements and considerable orchestration complexity, which become increasingly difficult to afford when training trillion-parameter LLMs under constrained computational resources. This work introduces CIPHER-MoE, which mitigates MoE workload imbalance while keeping the router's token-side Top-K selection unchanged. CIPHER-MoE applies affinity-aware Expert-to-Token filtering with explicit capacity control to reduce hotspot expert workloads without additional hardware resources or complex runtime design. The proposed method has been evaluated on large-scale MoE models, including DeepSeek-V4-Pro, showing up to 64.9 percentage points Top-1 expert workload reduction and 1.10×-1.94× training acceleration, while preserving the training quality. The source code will be released soon.

**Key innovations:**
- **The constraint is the contribution: the router's token-side Top-K selection is left unchanged.** Every prior fix for MoE imbalance (per the paper) changes parallelism strategy or reallocates resources. CIPHER-MoE intervenes on the **Expert-to-Token** side instead — "without additional hardware resources or complex runtime design". **Preserving routing fidelity while fixing balance** is a genuinely different trade-off point.
- **Affinity-aware Expert-to-Token filtering with explicit capacity control** — reduce hotspot expert load while routing decisions stay intact.
- **The named problem is precise**: underloaded experts waste hardware, hot experts need *more* resources; at trillion-parameter scale this "further amplifies the resource cost" and destabilizes training.
- **Results**: up to **−64.9 percentage points** Top-1 expert workload, **1.10×–1.94×** training acceleration, training quality preserved. Evaluated on large-scale MoE models **including DeepSeek-V4-Pro**.
- ⚠️ **Third-party verification is not possible from this paper.** "Evaluated on DeepSeek-V4-Pro" means *on that checkpoint*, not *by that team*. Combined with unreleased code and a `will be released soon` commitment, **the headline numbers are currently unverifiable outside the paper.**

---

#### 11. MOLT: Fine-Grained GPU Memory Sharing for LLM Serving with Opportunistic Fine-Tuning

- **arXiv**: [`2610.05748`](https://arxiv.org/abs/2610.05748)
- **Submitted**: 2026-10-05 · **Authors**: Jaehoon Yang, Yongbeom Kim, Hojoon Kim, Seung Yul Lee, Jae W. Lee · **Institution**: **Seoul National University, Seoul, Republic of Korea** (all five, verified from HTML author block)

**Abstract (verbatim):**
> Large language model (LLM) serving scales its replica count with the request load, yet GPU memory still stands idle inside the replicas. Adding a replica takes minutes, while the memory that a replica needs changes within seconds. Even instant autoscaling could not return this idle memory, because the smallest unit that it can remove is a whole replica. Colocating parameter-efficient fine-tuning (PEFT) with inference can use this memory, but inference must be able to reclaim it within seconds, before requests that wait for memory exceed their latency service-level objective (SLO). Existing colocation systems either keep the tuning memory resident or let inference reclaim it at the coarse granularity of a whole training sample. Each such reclamation also discards the running tuning step. To address these limitations, we present MOLT, a fine-grained memory sharing system that lets inference reclaim the memory of individual activations that a running tuning step has saved for its backward pass. The step continues, and its backward pass recomputes those activations. Inference reclaims only memory that no in-flight GPU work can still access, even under CPU--GPU asynchrony and tensor parallelism. On four model deployments (24B--70B) across H100 SXM and B200 GPUs under trace-driven workloads, MOLT keeps inference SLO attainment at or above 99.7% and completes 1.9--3.3x the tuning work of discard-based memory sharing.

**Key innovations:**
- **The framing is a granularity mismatch, stated crisply**: "Adding a replica takes **minutes**, while the memory that a replica needs changes within **seconds**... Even instant autoscaling could not return this idle memory, because **the smallest unit it can remove is a whole replica**." Autoscaling's quantum is too coarse for the memory that is actually idle.
- **The mechanism is activation-level, not sample-level.** Existing colocation either keeps tuning memory resident, or reclaims at **whole-training-sample granularity — and discards the running step**. MOLT lets inference reclaim **individual activations** a running tuning step saved for backward; **the step continues and backward recomputes those activations**. Trading recomputation for memory is the enabling idea.
- **Safety condition is the hard part and is stated explicitly**: inference reclaims only memory that **no in-flight GPU work can still access**, "even under CPU–GPU asynchrony and tensor parallelism". Correctness under async TP is the thing that makes or breaks this design.
- **Results**: 4 deployments (**24B–70B**) on **H100 SXM and B200**, trace-driven workloads; **SLO attainment ≥ 99.7%**, **1.9–3.3× the tuning work** of discard-based sharing.
- **Note the paper is about a *memory-sharing substrate*, not a fine-tuning method.** PEFT is the occupant that makes the idle memory useful; MOLT is the mechanism. Read accordingly.

---

### Lane C — Long-Horizon Agents and Verifiable Environments

---

#### 12. ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience

- **arXiv**: [`2610.05303`](https://arxiv.org/abs/2610.05303) · **Status**: *Preprint* · **Project page**: `artificer-ai-lab.github.io/ASCENT`
- **Submitted**: 2026-10-04 · **Authors**: Haodong Lu, Dong Gong · **Institution**: **University of New South Wales (UNSW Sydney)** (both, verified from HTML author block)

**Abstract (verbatim):**
> A large language model (LLM) agent solves long-horizon tasks through many reasoning-action turns, with one verification signal at termination. Deployed agents face streams of related tasks, making their trajectories a natural resource for improvement. In-context adaptation agents store reflections, memories, or skills as text, so reuse depends on retrieving the right experience and on a frozen policy executing it. We study Online Agentic Test-Time Training (OaTTT), which trains the LLM's weights on its own execution trajectories during deployment. The agent executes each task once, in one pass over the stream, and the executed trajectory with its verification result is the only learning signal for weight updates that persist across tasks. Directly imitating or reinforcing the generated tokens of this single attempt destabilizes the policy. We introduce ASCENT (Agentic Self-distillation for Cross-task EvolutioN at Test-time), which instead self-distills verified experience. A stable version of the LLM, its frozen initial copy, receives the verified trajectory as privileged information and predicts next-token distributions along it with this hindsight. Distilling them into persistent LoRA fast weights updates the agent for later tasks, without an external reference solution or stronger teacher. By further removing invalid-action turns, ASCENT distills enhanced privileged experience for more efficient execution. We characterize its population target and the limits of sparse outcome selection. Across ALFWorld, WebShop, and AppWorld at varied model scales, ASCENT improves task success and interaction efficiency as experience accumulates, outperforms online adaptation methods, and transfers to held-out scenes, showing that an agent can consolidate verified experience into its weights without a separate training phase or memory retrieval.

**Key innovations:**
- **Names and defines a new setting: OaTTT (Online Agentic Test-Time Training).** The defining constraint is severe and clearly stated: the agent executes each task **once, in one pass over the stream**, and its own verified trajectory is **the only learning signal** for weights that persist across tasks. No replay, no external data, no stronger teacher.
- **States the failure mode of the obvious approach before replacing it**: *"Directly imitating or reinforcing the generated tokens of this single attempt destabilizes the policy."* This is the paper's motivating negative result.
- **The fix is hindsight privileged-information distillation**: a **frozen initial copy** of the LLM is shown the verified trajectory and predicts next-token distributions **along it with hindsight**. Because it is frozen and initialized identically, it is a *stable* reference rather than a trained-up teacher. **LoRA fast weights** absorb the updates.
- **Invalid-action turns are removed** before distillation — "enhanced privileged experience", i.e. the teacher signal is cleaned, not just re-targeted.
- **The clearest thesis in this window**: an agent can consolidate verified experience **into its weights**, needing **neither a separate training phase nor memory retrieval**. That is a direct attack on the in-context-adaptation paradigm (memories/reflections/skills as text), whose weakness the paper names: "reuse depends on retrieving the right experience".
- **Two things a careful reader should want**: the paper "characteri[zes] its population target and **the limits of sparse outcome selection**". Self-distilling only verified successes means the update target is conditioned on a **biased population** (successful trajectories only) — the paper says it characterizes this, and that characterization is the part to read.
- **Benchmarks**: ALFWorld, WebShop, AppWorld, varied scales; improves success **and interaction efficiency** as experience accumulates; **transfers to held-out scenes** (the transfer claim is what distinguishes weight-consolidation from memorization).
- ⚠️ **No numbers in the abstract**; "outperforms online adaptation methods" is unquantified here.

---

#### 13. WorkForge: Scaling Verifiable Environments for Long-horizon Work Agents

- **arXiv**: [`2610.04906`](https://arxiv.org/abs/2610.04906)
- **Submitted**: 2026-10-04 · **Authors**: Jiazheng Zhang, Long Ma, Yunxian Yang, Zhiheng Xi, Zhikai Lei†, Yajie Yang, Chenyang Liao, Enyu Zhou, Yang Nan, Yuchen Tian, Senjie Jin, Yibo Wang, Boyang Liu, … (**26 total**) · **Institutions**: **LLM Department, Tencent** + **Fudan University** — verified from HTML author block

**Abstract (verbatim):**
> Work agents operate over digital artifacts to execute professional knowledge-intensive work, requiring training environments that support long-horizon interaction and trustworthy verification. However, hand-crafted environments incur prohibitive engineering overhead that prevents environment scaling, whereas synthesis methods sacrifice workspace complexity, realism, or grounded verifiability. To bridge this gap, we introduce WorkForge, a scalable synthesis framework for constructing verifiable work-agent environments from real-world resources. Starting from expert workflows, WorkForge first identifies the resources, decisions, and deliverables required by each workflow. It then retrieves relevant real-world files and organizes them into a workspace. WorkForge inspects the workspace to extract concrete, checkable facts about its content. These factual anchors fix which task types the workspace can support and how their outcomes can be verified. Therefore, WorkForge derives each task's instructions, solution plan, and complementary programmatic and semantic verifiers directly from these factual anchors, keeping verification traceable to observable workspace evidence. Furthermore, we construct 16.7K verifiable environments across 40 professional domains, with workspaces collectively covering 60 file types. Post-training Qwen3.5-35B-A3B-Base improves GDPVal from 45.5 to 73.6 and APEX Score from 5.0 to 21.3, while enabling Qwen3.5-27B to achieve highly competitive performance and outperform strong competitors. Our analyses confirm the efficacy of the proposed method and reveal consistent scaling behaviors across both data volume and interaction horizons.

**Key innovations:**
- **This is the strongest paper in the window by the wiki's own criterion** — the 2026-10-05 report observed that "a CTR paper that reports offline AUC without a serving envelope is now visibly incomplete". WorkForge is the opposite failure mode: it reports **the single largest absolute jump in a frontier-adjacent professional benchmark this wiki has recorded** (GDPVal **45.5 → 73.6**, +28.1 points; APEX **5.0 → 21.3**, 4.3×) and explains *why the environments are trustworthy* rather than asserting it.
- **The pipeline is the contribution, and its order is the argument**: expert workflow → (resources, decisions, deliverables) → retrieve real files → **build a workspace** → **inspect the workspace to extract concrete checkable facts** → use those **"factual anchors"** to derive instructions, solution plan, and verifiers. **Verification is derived from the artifact, not from the task label.** This is the anti-pattern of writing a verifier and then inventing a task to check.
- **Directly answers the named failure of prior synthesis methods**: they "sacrifice workspace complexity, realism, or **grounded verifiability**". WorkForge's bet is that grounding verifiers in extracted workspace facts recovers all three.
- **Complementary verifiers per task** — programmatic *and* semantic, both traceable to the same anchors.
- **Scale**: **16.7K environments**, **40 professional domains**, **60 file types**.
- **Results**: Qwen3.5-35B-A3B-Base post-trained → GDPVal **45.5 → 73.6**, APEX **5.0 → 21.3**; Qwen3.5-**27B** (dense) becomes competitive and **outperforms strong competitors**. Reports **consistent scaling in both data volume and interaction horizon** — i.e. it is not a one-shot data dump.
- ⚠️ **The number to interrogate is APEX 5.0 → 21.3.** A 4.3× relative jump from environment construction alone is large enough that the *starting* score of 5.0 should be checked against what APEX's floor means for an un-post-trained base model. Low baselines make large relative gains cheap.
- ⚠️ **26 authors and no venue** — preprint status.

---

### Lane D — Games and RL

---

#### 14. Social Deduction Games with Reinforcement-Fine-Tuned LLMs

- **arXiv**: [`2610.04261`](https://arxiv.org/abs/2610.04261)
- **Submitted**: 2026-10-03 · **Authors**: Lingzhe Zhang, Yunpeng Zhai, Tong Jia, Kening Zheng, Chiming Duan, Minghua He, Zhaoyang Liu, Bolin Ding, Philip S. Yu, Ying Li (10) · **Institutions**: **Peking University** (Zhang, Jia, Duan, He), **Alibaba Group, China** (Zhai, Zhaoyang Liu, Ding), **University of Illinois Chicago** (Zheng, Yu), **CUHK** (Li) — verified from HTML author block

**Abstract (verbatim):**
> Reinforcement fine-tuning (RFT) is increasingly used in applications where large language models (LLMs) interact with humans and other agents. Here we use social deduction games to study how RFT changes LLMs' social behaviour. We let fine-tuned and base LLM agents play hidden-role games that require hidden-state inference, social reading and vote steering. Our results show that LLM agents do not reliably acquire social-deduction ability by directly optimizing terminal win--loss outcomes, suggesting that final game results provide a sparse and noisy signal for socially interactive learning. However, RFT is particularly effective at improving social reading, including tasks that require agents to infer hidden roles from public discussion, update beliefs over time and predict other agents' future decisions. We further show that RFT can also improve social influence, including tasks that require agents to steer votes, team approvals and collective decisions, although these gains depend more strongly on behaviourally specific rewards and structured interaction settings. Finally, we show that LLMs' ability to play social deduction games can be further improved through multi-agent social-cognitive reinforcement fine-tuning, which combines social-reading and social-influence signals during same-side multi-agent training. These learned behaviours also receive more favourable human evaluations of strategic competence, persuasiveness and social usefulness. Together, these results enrich our understanding of how RFT changes LLMs' social behaviour and provide a step toward a behavioural learning theory for machine social intelligence.

**Key innovations:**
- **A clean negative result with a clean mechanism, and it is the most transferable finding in the games lane**: *"LLM agents do not reliably acquire social-deduction ability by directly optimizing terminal win–loss outcomes"*, because final game results are "a sparse and noisy signal for socially interactive learning". **Terminal-outcome RL fails on socially interactive tasks** — while succeeding on the *component* skills.
- **The decomposition is what makes the paper useful**: **social reading** (infer hidden roles from public discussion, update beliefs, predict others' decisions) improves reliably under RFT; **social influence** (steering votes, approvals, collective decisions) improves **only with behaviourally specific rewards and structured interaction settings**. Two different reward regimes for two different skills.
- **Asymmetric with DiffGate and HarA in this same window**: three papers independently conclude that **terminal-outcome or uniform-advantage signals are insufficient** and propose shaping them. The convergence across recommendation-adjacent RL, LLM post-training, and social games is §5.2's main thread.
- **Human evaluation as a third leg**: learned behaviours receive more favourable ratings of **strategic competence, persuasiveness and social usefulness** — behaviour metrics, not just win rate.
- ⚠️ **Hidden-role games are a narrow slice of "social intelligence."** The authors are careful ("a step toward a behavioural learning theory"), and the finding should be read as scoped to hidden-state social inference, not general collaboration.

---

#### 15. HarA: Hierarchical Credit Assignment for RLVR on Fused Gromov-Wasserstein Geometry

- **arXiv**: [`2610.04344`](https://arxiv.org/abs/2610.04344)
- **Submitted**: 2026-10-03 · **Authors**: Qi Yu, Ruizhong Qiu, Zhichen Zeng, Xuying Ning, Yanjun Zhao, Dongqi Fu, Yinglong Xia, Hong Li, Hanghang Tong (9) · **Institutions**: **UIUC** (Yu, Qiu, Zeng, Ning, Zhao, Tong), **Meta** (Fu, Xia, Li) — verified from HTML author block

**Abstract (verbatim):**
> Reinforcement learning with verifiable rewards (RLVR) has been shown to improve the reasoning capability of large language models (LLMs) across diverse reasoning tasks. However, group-based RLVR methods, such as GRPO, assign a uniform advantage to all tokens within rollouts of the same outcome. While existing works refine credit assignment of GRPO based on local signals such as token locations or entropy, they often fail to capture the global semantic novelty of a reasoning behavior relative to the current policy. In this work, we propose a hierarchical credit assignment approach for group-based RLVR methods, called HarA, which identifies and encourages semantically novel reasoning behaviors during RLVR. HarA represents each sampled rollout as a distribution over the hidden states and locations of tokens, and computes the Fused Gromov-Wasserstein (FGW) barycenters of all rollouts with the same outcome, capturing the internal reasoning patterns in the latent space under the current policy. The semantic novelty of a reasoning element can then be measured by its contribution to the FGW distance between the current rollout and the barycenter. While solving the FGW formulation is expensive, we introduce an anchor-guided linearization that turns it into a Wasserstein formulation solvable via the Sinkhorn algorithm efficiently. By reweighing token-level advantage of group-based RLVR methods based on the novelty signals, HarA highlights novel reasoning behaviors at flexible granularities to encourage fine-grained LLM exploration. Extensive experiments across three group-based RLVR methods show that our plug-and-play method effectively enhances the exploration of LLMs, outperforming existing methods across diverse reasoning benchmarks.

**Key innovations:**
- **The critique of prior credit-assignment work is the framing**: existing refinements use **local** signals (token position, entropy) and therefore "fail to capture the **global semantic novelty** of a reasoning behavior **relative to the current policy**". Novelty is defined against *the policy's own distribution*, not against a fixed heuristic — which is why it must be recomputed during training.
- **Representation choice is what enables the global measure**: each rollout is represented as a **distribution over the hidden states and locations of tokens**, then the **Fused Gromov-Wasserstein barycenter** of all same-outcome rollouts is computed. A token's semantic novelty = **its contribution to the FGW distance between the current rollout and that barycenter**. Novel behaviour = behaviour that pulls the rollout away from the centroid of its outcome group.
- **The engineering contribution is the linearization**: FGW is expensive, so an **anchor-guided linearization** reduces it to a plain Wasserstein problem solvable by **Sinkhorn**. Without this, the method is a curiosity; with it, it is usable.
- **Plug-and-play across three group-based RLVR methods**, with gains "across diverse reasoning benchmarks". Note the claim is about **exploration**, and the objective is to "encourage fine-grained LLM exploration" — i.e. the mechanism is diversity-seeking by construction.
- ⚠️ **No model scale, no benchmark names, and no numbers in the abstract.** "Outperforming existing methods across diverse reasoning benchmarks" is the whole empirical claim as stated. Since the method is an exploration booster, **improvements in pass@k should be read as coverage, not accuracy** — the same caveat as DiffGate (§5 entry 9).
- ⚠️ **Layered onto GRPO, so it inherits GRPO's known failure mode** — vanishing group-relative signal on all-failure groups, which DiffGate explicitly targets and HarA does not mention addressing.

---

#### 16. Code2Games: Enabling Coding Agents for Gaming World Generation

- **arXiv**: [`2610.05033`](https://arxiv.org/abs/2610.05033) · **Code**: `github.com/AIGeeksGroup/Code2Games` · **Site**: `aigeeksgroup.github.io/Code2Games`
- **Submitted**: 2026-10-04 · **Authors**: Wei Wu, Ziyang Xu, Zeyu Zhang, Yang Zhao, Hao Tang · **Institutions**: **La Trobe University** + **School of Computer Science, Peking University** — verified from HTML author block

**Abstract (verbatim):**
> Generating a high-quality gaming world from a natural-language game intent requires joint reasoning about scene structure, spatial layout, gameplay objectives, interactive entities, and executable gameplay logic. Existing coding agents can generate individual assets, scenes, or scripts, but often struggle to maintain consistency across these components. We propose Code2Games, an agentic framework that builds a structured gaming world upon a base Blender world generated from the same game intent. Code2Games coordinates scene analysis, gameplay planning, constrained gaming-world generation, and gaming-engine customization through a shared scene-gameplay representation with persistent element correspondence. After world generation, Code2Games adapts the generated world to Unreal Engine 5 and employs an execution-guided reconstruction process that uses compilation diagnostics, runtime feedback, and gameplay test results to resolve inconsistencies arising during engine adaptation. To systematically evaluate gaming-world generation, we introduce the GameCode4D benchmark, which comprises ten fixed game prompts spanning different levels of scene and gameplay complexity. We evaluate the generated results across four dimensions: visual quality, interactive fidelity, multimodal artifact quality, and playable-game quality. Experiments demonstrate that, compared with direct gaming-world generation by coding agents and existing baseline methods, Code2Games consistently improves the visual quality and interactive fidelity of generated gaming worlds, as well as the quality of the resulting games after engine adaptation.

**Key innovations:**
- **Names the failure precisely: cross-component consistency.** "Existing coding agents can generate individual assets, scenes, or scripts, but often struggle to **maintain consistency across these components**." Generation quality is not the bottleneck; *coherence* is.
- **The mechanism is a shared intermediate representation with persistent element correspondence** — a single scene-gameplay representation that keeps track of which generated element corresponds to which across scene analysis, gameplay planning, generation, and engine customization. That is the answer to consistency.
- **Engine adaptation is treated as a repair loop, not a conversion step.** After generating in Blender, the world is adapted to **Unreal Engine 5**, and an **execution-guided reconstruction process** uses **compilation diagnostics, runtime feedback, and gameplay test results** to resolve inconsistencies. The engine's own error signals drive the fix.
- **GameCode4D** benchmark: **10 fixed game prompts**, graded on **four dimensions** — visual quality, interactive fidelity, multimodal artifact quality, playable-game quality.
- **Games-lane signal for this wiki's PCG thread**: paired with **RuleSweeper** (gameplay *mechanics* generation, cited in the 2026-10-05 game digest) and **Beyond Playability** (persistent spatial intent). Three papers in one week now treat *mechanically correct, engine-verified worlds* as the target rather than visual quality.
- ⚠️ **Ten prompts is a very small benchmark.** Consistent improvement on 10 prompts is evidence of a working pipeline, not of general capability; per-prompt variance is likely large. **Read the four-dimension evaluation as a rubric, not as a reliable score.**

## 5. Cross-Cutting Observations

### 5.1 The window inverts: zero completed online A/B tests

**The single most important finding in this report.** All 16 featured papers were checked for live-business-metric evidence (full-text search for `A/B test`, `online A/B`, `online experiment`, `deployed in production`, `online lift/gain` across all 16 HTML renders):

| Paper | "A/B" evidence found | Verdict |
|---|---|---|
| LRPRec `2610.03923` | 1 hit | **False positive** — a *hypothetical* about prompt fragility under deployment |
| SCOUT `2610.05619` | 1 hit | **Future work** — "our **ongoing work** focuses on large-scale online A/B testing" |
| GrIS `2610.01533` | "online gain" hit | **Citation to other papers'** online gains, not its own |
| All other 13 | none | — |

**Result: 0/16 report a completed online A/B.** Compare the [2026-10-05 window](../2026-10-05/arxiv-ai-search.md): **7 of 8** papers reported live business metrics (conversion, CTR/CPM, revenue, GMV, RPM).

The cause is visible in the affiliation column: **10 of 16 are universities**, and the two industrial papers (CIPHER-MoE at Tongji/Cornell/HIT-Shenzhen, MOLT at SNU) are **systems** papers reporting cost and SLO rather than business impact. **This is a window composition effect, not a field-wide trend** — industrial systems papers land in bursts, and the previous window was one such burst. Two consequences:

1. **Do not read "no A/B" as weak evidence.** These papers are answering different questions with appropriate instruments; SCOUT's own limitations section is *more* valuable for saying so explicitly than a paper reporting a business number would have been.
2. **The wiki's own grading of evidence needs the distinction made explicit.** An offline-only paper and a hypothetical-A/B paper are not the same. Both SCOUT and LRPRec would have been miscounted by a naive keyword grep.

### 5.2 Three papers in one window independently conclude that terminal-outcome signals are insufficient

- **DiffGate** (`2610.04596`, IISc + Snap): OPD is dense-but-misaligned, RLVR is aligned-but-coarse. Combine them, gated on failure.
- **HarA** (`2610.04344`, UIUC + Meta): GRPO's uniform per-token advantage destroys the global semantic-novelty signal. Reweight by contribution to an FGW barycenter distance.
- **Social Deduction RFT** (`2610.04261`, PKU + Alibaba + UIC): optimizing terminal win–loss "provide[s] a sparse and noisy signal for socially interactive learning". Component skills improve; the composite does not.

**This is the strongest convergence signal in the window, and it is cross-domain** — LLM post-training, group-based RLVR, and multi-agent social behaviour arrived at "the reward you have is not the signal you need" independently, with different mechanisms. Note also that **DiffGate's blind-spot analysis is essentially the formal statement of what the other two observe empirically.** A wiki-level [[claims]] page on this would be well-supported; it is currently a three-source pattern with no contradicting source in this window.

### 5.3 The "one model, several stages" thread has a new member — and it is now a memory argument

The 2026-10-05 report observed five independent industrial teams converging on *separate expensive reusable computation from cheap per-request computation*. **MOLT (`2610.05748`) is the same shape applied to memory rather than model stages**: the expensive thing (activation storage for a training step's backward pass) is decoupled from the latency-critical thing (inference), and the saving is **recomputation**. CutBCE (`2610.05559`) is the same logic against HBM: keep logits and gradients **off** the critical resource entirely by computing tiles on-chip. **The through-line across LLaTTE / ReST / GR4AD / MOLT / CutBCE is not "staged models" — it is "identify the scarce resource and refuse to pay for it on the critical path."** That is a more portable formulation than the architecture one.

### 5.4 Semantic ID construction is being re-founded as a clustering problem, and the field noticed within three weeks

GrIS (`2610.01533`, Huawei Ireland) reframes SID construction from representation learning to **recursive graph partitioning**, and — importantly — **recovers RQ-VAE and RQ-KMeans as the empty-graph special case**. Two consequences for this wiki's existing Semantic ID material:

- The GrIS framing makes [[GR4AD]]'s UA-SID claim (semantic channel + business channel via MGMR quantization) legible as an instance of "two collapsed axes, made explicit".
- Because GrIS claims its axes are **orthogonal and composable**, it offers a testable structure that the 2026-10-03 digest's three-paper lineage (`2610.01139` → `2610.01533` → `2610.01967`) could not — that lineage compared three *systems* and found no head-to-head. **A framework that shows two prior methods are its special cases is a better citation than a third data point.** See §4 — the digest's entry for this ID has the wrong title and its lineage conclusion needs revisiting.

### 5.5 Peer review arrived in this window; three papers carry venue evidence

| Paper | Venue | Status |
|---|---|---|
| SAGA `2610.04753` | **NeurIPS 2026** | accepted |
| CoBPE `2610.05597` | **COLM 2026** | accepted |
| SCOUT `2610.05619` | **CIKM 2026 Workshop** on Generative, RAG & Agentic Intelligence for Personalization | accepted (workshop) |
| DiffGate `2610.04596` | — | *Preprint Under Review* |
| ASCENT `2610.05303` | — | *Preprint* |
| CIPHER-MoE `2610.05744` | — | code "will be released soon" |

This matters for grading: **SAGA's >2× claim and CoBPE's −30%/+1.2 have been through review; CutBCE's 225.9% and CIPHER-MoE's 64.9pp have not.** The 2026-10-05 game digest made the same point when three provisional preprints turned out to have acceptances.

### 5.6 Inference cost is being attacked from four different layers in one window

The window contains four papers that reduce LLM cost by attacking a *different layer each*, which together read as a decomposition of where inference cost lives:

| Layer | Paper | Mechanism | Reported gain |
|---|---|---|---|
| **Tokenization** | CoBPE `2610.05597` | compose function words into reusable modifiers | −30% sequence length |
| **Attention structure** | SAGA `2610.04753` | decouple key/value head counts; cut the expensive side | >2× decoding |
| **Memory placement** | CutBCE `2610.05559` | compute logit tiles on-chip; never in HBM | +225.9% training throughput |
| **Scheduling / co-location** | MOLT `2610.05748` | reclaim activation memory mid-step; recompute in backward | 1.9–3.3× tuning work at ≥99.7% SLO |

⚠️ **These are not additive and were not measured together.** CoBPE's shorter sequences would change SAGA's operating point; CutBCE is *training* throughput, not decoding; MOLT needs spare memory that the others consume. Any synthesis claiming a combined speedup would be fabricated.

### 5.7 Reliability remains unreported, and one paper's benchmark is too small to bear weight

Two quality signals that belong in any window summary:

- **No reliability/safety evaluation appears in any of the 16 papers.** Not one reports calibration, hallucination rate, or robustness under distribution shift as a primary metric. For a window that trains agents (WorkForge, ASCENT), deploys RL policies into social interaction (social deduction RFT), and modifies decoding (SAGA, CoBPE), that is a conspicuous absence.
- **Code2Games' benchmark is 10 prompts.** Consistent improvement is not capability. Every other quantitative claim in this report rests on ≥3 datasets or multiple model scales; this one does not.

## 6. Method & Discipline

**Channel.** arXiv export API (Atom XML), 10 queries, HTTPS with `curl -G --data-urlencode`, sequential, ≥4 s between calls. This is a **new channel for this wiki** — previous digests used web search and `/list` scraping, and the 2026-10-05 game digest recorded persistent `HTTP 429` against this same endpoint. **It is usable when requests are serialized and spaced**; the failure mode is a bare `Rate exceeded.` body that a naive parser reads as "zero results."

**Coverage.** 916 unique papers pooled; window `2610.01533`–`2610.05748` (2026-10-01 → 2026-10-05). ⚠️ **Topic-complete, not month-exhaustive** — see §1.1. The 400-paper ID enumeration reached only 2026-10-04/05.

**Dedup.** 32 candidates ID-grepped against the whole of `wiki/` → 16 duplicates, 16 fresh. Then **title-level dedup on the 15 fresh**, which caught **two name-collision false positives** (`SCOUT` → the 10-04 distillation paper; `MOLT` → MOLTBOOK). **Third occurrence in four days of ID-only dedup being insufficient.**

**Affiliations — 16/16 recovered, zero inferred.** Every featured paper's arXiv HTML `ltx_authors` block was parsed for `Affiliation:` fields. This run is a direct response to the open item in §4.1 of the [2026-10-05 report](../2026-10-05/arxiv-ai-search.md) (ReST/ByteDance) and to the "unrecoverable affiliations" theme of the [2026-10-05 game digest](../2026-10-05/game-rl-daily.md): **LaTeXML did not strip a single author block this time.** Two results show the discipline mattered:

- **CreGR `2610.05670`** contains authors named **Shoujin Wang** and **Peilin Zhou** — names this wiki associates with industrial ads teams. **Both are at UTS / NYU Abu Dhabi.** Name-based inference would have misattributed the paper.
- **SCOUT `2610.05619`** is **Airbnb**, not a search-advertising property — the "supply-aware" framing reads as travel inventory, not ad inventory.

Two affiliations are partially opaque and are reported as printed: **CIPHER-MoE** lists "**AI Training Platform Team, Shenzhen Loop Area Institute**" as an affiliation string, and **SAGA** lists one author as "**Stealth Startup**" with no name. Neither is guessed at.

**Abstracts.** Quoted verbatim from the arXiv API Atom `<summary>`. Where the source rendering drops a leading character (SAGA's abstract begins `utoregressive generation`), this is flagged inline rather than silently repaired.

**⚠️ Two version-drift / metadata issues recorded rather than resolved:** (1) `2610.01533`'s title on file in this wiki is **wrong** — see §4; (2) every paper here is **v1** and the API reports the v1 `updated` date, so any wiki page created from this report should record the ID **without** implying a later version was reviewed.

**No new paper pages created** — only this synthesis file, matching the precedent of the 2026-10-04 and 2026-10-05 reports. §7 lists the ingest candidates.

**Not done.** No full-text read of any PDF; all claims above are from API metadata, HTML author blocks, and targeted full-text regex over the HTML renders. Results tables, ablations, and dataset identities beyond those named in the abstracts were not extracted.

## 7. Recommended Ingests

Ordered by fit to this wiki's stated interests (recommendation / ads / sequential modeling first).

| Priority | Paper | arXiv | Suggested page | Why |
|---|---|---|---|---|
| **1** | **GrIS** | [`2610.01533`](https://arxiv.org/abs/2610.01533) | `wiki/papers/recommendation/gris-graph-informed-semantic-ids.md` | Best Semantic ID paper in the window; **subsumes** RQ-VAE/RQ-KMeans; composes with the [[GR4AD]] UA-SID thread. Also forces a correction to the 10-03 digest. |
| **2** | **CutBCE** | [`2610.05559`](https://arxiv.org/abs/2610.05559) | `wiki/papers/recommendation/cutbce.md` | Only industrial-grade recsys *infrastructure* paper in the window; open-sourced; names a concrete LLM→recsys technology-transfer gap. |
| **3** | **DiffGate** | [`2610.04596`](https://arxiv.org/abs/2610.04596) | `wiki/papers/llm-training/diffgate.md` | Companion to the 10-04 SCOUT distillation entry; completes that argument. |
| **4** | **WorkForge** | [`2610.04906`](https://arxiv.org/abs/2610.04906) | `wiki/papers/agents/workforge-verifiable-environments.md` | GDPVal 45.5→73.6 with verification traced to artifacts; Tencent + Fudan. |
| **5** | **SAGA** | [`2610.04753`](https://arxiv.org/abs/2610.04753) | `wiki/papers/llm-training/saga-asymmetric-attention.md` | NeurIPS 2026; a new degree of freedom in GQA. |
| 6 | Social Deduction RFT | [`2610.04261`](https://arxiv.org/abs/2610.04261) | `wiki/papers/games/social-deduction-rft.md` | PKU + Alibaba; clean negative result on terminal-outcome RL. |
| 7 | SCOUT | [`2610.05619`](https://arxiv.org/abs/2610.05619) | `wiki/papers/recommendation/scout-supply-aware-query-suggestion.md` | **Airbnb**; the supply-side-substitutes-demand-side idea transfers to ad inventory. |

**Candidate [[claims]] page:** *"Terminal-outcome and uniform-advantage rewards are insufficient for behaviors whose credit spans a trajectory."* Supporting sources: DiffGate, HarA, social-deduction RFT, and (from an earlier window) the 10-04 SCOUT. **Confidence: high on the negative claim, low on the generality** — all four sources are recent and no contradicting source has been found.

## 8. Related Pages

- [`../2026-10-05/arxiv-ai-search.md`](../2026-10-05/arxiv-ai-search.md) — the industrial burst this window inverts; also the ReST/ByteDance attribution to resolve (§4.1 there)
- [`../2026-10-05/game-rl-daily.md`](../2026-10-05/game-rl-daily.md) — the games lane in full; RuleSweeper and Beyond Playability are Code2Games' peers (§5 entry 16)
- [`../2026-10-05/game-rl-daily.md`](../2026-10-05/game-rl-daily.md) — arXiv `429`/`Rate exceeded` history for this API endpoint (§1.2 here)
- [`../2026-10-04/arxiv-ai-search.md`](../2026-10-04/arxiv-ai-search.md) — SCOUT (the distillation paper, not this report's Airbnb SCOUT); §5.2's fourth supporting source
- [`../2026-10-03/conference-digest.md`](../2026-10-03/conference-digest.md) — **§4's correction target**: wrong title for `2610.01533` and a lineage conclusion to revisit
- [`../ctr-scaling-landscape.md`](../ctr-scaling-landscape.md) — cross-window synthesis of the CTR scaling thread
- [`../../papers/ctr/llatte.md`](../../papers/ctr/llatte.md) — §5.3's anchor for the "expensive vs. cheap computation" thread
