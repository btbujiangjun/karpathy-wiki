---
title: "arXiv AI Search 2026-10-08 — The Recommendation Keyword Space Is Mined Out, and a Same-Day Sibling Race Cost This Run 9 Papers"
type: synthesis
created: 2026-10-08
updated: 2026-10-08
sources: [arxiv-api-atom-xml, arxiv-html-ltx-authors, arxiv-html-author-thanks]
tags: [arxiv, keyword-sweep, dedup, sibling-collision, llm-post-training, distillation, reward-design, rl-algorithm-search, speculative-decoding, agents, recommendation, pre-ranking, generative-pseudo-labeling, ctr, on-device, query-recommendation, retention, online-experiment, games, multi-agent, marl, negative-result]
---

# arXiv AI Search 2026-10-08 — keyword-sweep run

> **Two findings, one methodological and one procedural.**
>
> **① Methodological — the recommendation keyword space is mined out for this wiki.** The [`../2026-10-06/arxiv-ai-search.md`](../2026-10-06/arxiv-ai-search.md) report closed by recommending *"keep querying by ID range, not by keyword."* This run did the opposite — eight topic-keyword queries — and reproduced exactly the saturation that advice predicted: **175 in-lane IDs already on file**, and only **8 in-lane papers new**, half of them back-catalog. Queries 1 and 5 alone match **12,545** and **781** papers respectively, and the newest-100 of that space has been swept daily since June. **Further yield in that lane requires ID-range enumeration of the fresh window, not better keywords.** See §5.1.
>
> **② Procedural — a same-day sibling race cost this run 9 of its 23 papers.** While this report was being written, [`arxiv-paper-check.md`](arxiv-paper-check.md) landed in the same folder and independently claimed **9 of the 23 IDs featured here**, including the entire LLM post-training core. Following the wiki's established precedent (*"the collisions were swapped, not merged"* — [`../log.md`](../log.md), 2026-10-07), **those 9 were swapped out and replaced**, and the race is documented in §2.3. **This is now a recurring failure mode of parallel same-day runs, not an accident.** See §5.2 and the new follow-up #1 in §6.

## 1. Search Metadata

| Field | Value |
|---|---|
| **Date of search** | 2026-10-08 (Thursday) |
| **Search channel** | **arXiv export API** (`https://export.arxiv.org/api/query`), Atom XML — same channel as [`../2026-10-06/arxiv-ai-search.md`](../2026-10-06/arxiv-ai-search.md) |
| **Window covered** | Fresh IDs **`2610.03033` → `2610.10536`** (submissions **2026-10-02 → 2026-10-07**), plus **5 backfill** IDs from `2602`/`2606`/`2607`/`2608`/`2609` |
| **Pool size** | **800 entries fetched**, **717 unique papers** after cross-query dedup |
| **Candidates shortlisted** | 47 in-lane (title-level keyword filter, then ID-checked against all of `wiki/`) |
| **Shortlisted as new at write time** | **23** |
| **Lost to same-day sibling race** | **9** — see §2.3 |
| **Featured, final** | **23** (14 retained + 9 replacements) |
| **In-lane IDs already on file** | **175** (dedup ledger in §2, top rows shown) |
| **Affiliation recovery** | **23/23 (100%)** from arXiv HTML `ltx_authors` / `ltx_role_affiliation` / author `thanks` blocks. **Zero inferred.** |
| **Production / online-experiment numbers** | **5** — all backfill; **0 of 18 fresh `2610.*` papers report one** |
| **Temp artifacts** | `/var/folders/.../T/opencode/arxiv-ai-search-20261008/` (authorized scratch), deleted after writing |

### 1.1 Queries issued

| # | Query | Fetched | arXiv total |
|---|---|---|---|
| 1 | `cat:cs.IR AND (abs:recommendation OR abs:CTR OR abs:advertising OR abs:ranking)` | 100 | 12,545 |
| 2 | `cat:cs.IR AND (abs:"sequential" OR abs:"behavior sequence" OR abs:"generative recommendation")` | 100 | 2,039 |
| 3 | `(cat:cs.LG OR cat:cs.CL) AND (abs:"scaling law" OR abs:optimizer OR abs:"post-training" OR abs:"reinforcement learning" OR abs:distillation)` | 100 | 109,201 |
| 4 | `cat:cs.IR AND (abs:ad OR abs:ads OR abs:advertisement OR abs:click-through OR abs:advertiser)` | 100 | 2,086 |
| 5 | `abs:"click-through rate" OR abs:"CTR prediction"` | 100 | 781 |
| 6 | `abs:game AND (abs:"language model" OR abs:LLM) AND (cat:cs.AI OR cat:cs.CL)` | 100 | 1,708 |
| 7 | `abs:"self-play" OR abs:"multi-agent" AND abs:game` | 100 | 2,647 |
| 8 | `cat:cs.AI AND (abs:"language model agent" OR abs:agent OR abs:"tool use" OR abst:planning)` | 100 | 33,737 |

⚠️ **Two defects in the query design, stated rather than hidden.**

1. **Query 8 contains a typo: `abst:planning`** (should be `abs:planning`). arXiv **silently ignored the malformed clause** rather than erroring — the query returned 33,737 hits on the surviving clauses, so the typo cost recall on "planning" only, and **the run did not detect it until the query table was written up.** A malformed field name that fails *silently* is worse than one that fails loudly, because the run records a healthy hit count.
2. **Queries 1–5 are unbounded back-catalog sweeps.** Query 1 alone matches **12,545** papers; only the newest 100 were fetched, but that keyword space is the same one this wiki has swept daily since June. **This is the design defect that produced §5.1.** Queries 3, 6, 7, 8 are the ones with genuine remaining yield — and indeed all 8 LLM-post-training papers in this report came from queries 3 and 8.

### 1.2 Rate limiting — no incidents; HTML endpoint runs at 1 s

The arXiv API returned complete responses on all eight calls: `curl -sG --data-urlencode` for every clause, **sequential** requests, **6 s** sleep between calls. No `Rate exceeded.`, no empty bodies. **The mitigation recorded in [`../2026-10-06/arxiv-ai-search.md`](../2026-10-06/arxiv-ai-search.md) §1.2 worked as specified and should now be treated as settled practice rather than an open risk.**

Operational note: `arxiv.org/html/<id>v1` is a *different* endpoint with different tolerance. A 3 s sleep hit the tool timeout after 12 of 24 files; re-running at **1 s sleep with a 25 s per-file timeout completed all remaining files with zero failures.**

## 2. Dedup Ledger

Every shortlisted ID was regex-checked against the whole of `wiki/` for `\b\d{4}\.\d{4,5}\b` immediately before the first write. **175 in-lane IDs were already claimed.** The 21 most recent / most relevant are shown; the remainder are back-catalog canonical papers.

| arXiv ID | Paper | Files citing |
|---|---|---|
| [`2610.08732`](https://arxiv.org/abs/2610.08732) | Semantic ID Spaces for Generative IR | 4 |
| [`2610.08407`](https://arxiv.org/abs/2610.08407) | Image-Derived Contextual Signals for RecSys | 4 |
| [`2610.08245`](https://arxiv.org/abs/2610.08245) | Contribution-Aware Fair Recommendation | 3 |
| [`2610.08136`](https://arxiv.org/abs/2610.08136) | Adapting Generative Recommenders for Multi-Turn Interaction | 5 |
| [`2610.08076`](https://arxiv.org/abs/2610.08076) | SpeedrunBench | 5 |
| [`2610.07402`](https://arxiv.org/abs/2610.07402) | SimHash Semantic ID Construction | 3 |
| [`2610.07105`](https://arxiv.org/abs/2610.07105) | State Retention for Recursive Self-Improvement in Rec | 3 |
| [`2610.06590`](https://arxiv.org/abs/2610.06590) | SPRIG | 3 |
| [`2610.06050`](https://arxiv.org/abs/2610.06050) | MATE long/short-term user memory | 3 |
| [`2610.05670`](https://arxiv.org/abs/2610.05670) | CreGR content credibility | 5 |
| [`2610.05559`](https://arxiv.org/abs/2610.05559) | CutBCE large-vocabulary loss | 4 |
| [`2610.05432`](https://arxiv.org/abs/2610.05432) | OpticalRec | 4 |
| [`2610.04253`](https://arxiv.org/abs/2610.04253) | Spec2Game | 2 |
| [`2610.03923`](https://arxiv.org/abs/2610.03923) | LRPRec personalized prompts | 3 |
| [`2610.02425`](https://arxiv.org/abs/2610.02425) | XiangqiBench | 5 |
| [`2610.02057`](https://arxiv.org/abs/2610.02057) | Effective training time for industrial rec | 4 |
| [`2610.01705`](https://arxiv.org/abs/2610.01705) | AgentWebRec | 4 |
| [`2610.01533`](https://arxiv.org/abs/2610.01533) | GrIS | 5 |
| [`2609.39828`](https://arxiv.org/abs/2609.39828) | KUAISHOU Explorer LLM-Rec Challenge 2026 | 5 |
| [`2609.39327`](https://arxiv.org/abs/2609.39327) | Generative End-to-end Ad Retrieval at Douyin | 5 |
| [`2609.39007`](https://arxiv.org/abs/2609.39007) | RouteRec | 5 |

### 2.1 ⚠️ Name collision caught by title-level dedup — `MASBench`

Grep for `MASBench` returns **1 hit that is a different paper**. [`../2026-09-05/conference-digest.md:452`](../2026-09-05/conference-digest.md) records "**Introduces MASBENCH (Dim-5 axes: Depth/Horizon/Breadth/Parallel/Robustness)**" as part of **MAS-Orchestra** — a serial, code-level automatic MAS-design system.

The paper featured here as [`2610.04672`](https://arxiv.org/abs/2610.04672) is also called **MASBench**, is from **BUPT + SJTU + Tsinghua**, and evaluates **Protocol / Memory / Routing collaboration mechanisms under partial observability** across Reasoning / Scheduling / Game tasks. **Same acronym, different paper, different institutions, different contribution.**

**ID-only dedup would have passed this silently.** This is now the **fourth time in five days** that ID-only dedup would have produced a duplicate ([`../2026-10-06/arxiv-ai-search.md`](../2026-10-06/arxiv-ai-search.md) §2 logged three: two `SCOUT`, one `MOLT`). **Acronym/title-level dedup is no longer optional in this wiki** — see follow-up #2.

### 2.2 Affiliation repeats

- **Nubank**, now twice: [`2610.04302`](https://arxiv.org/abs/2610.04302) (DA-RSIR, recursive self-improvement for sequential rec) and [`2609.30137`](https://arxiv.org/abs/2609.30137) (Snowglobe CX-agent evaluation, recorded in [`../2026-09-25/arxiv-ai-search.md`](../2026-09-25/arxiv-ai-search.md)). Two unrelated papers, one recurring industrial entity — a candidate for an `wiki/entities/` page. **(tentative)**
- **Alibaba**, now three times across two papers/affiliations: [`2602.20995`](https://arxiv.org/abs/2602.20995) (Alibaba Group, Taobao) and [`2606.05671`](https://arxiv.org/abs/2606.05671) (Alibaba International Digital Commerce), plus prior Alibaba entries in [`../log.md`](../log.md). **Not flagged further — recorded only so the entity graph can be built later.**

### 2.3 ⚠️⚠️ Same-day sibling race — 9 IDs lost to `arxiv-paper-check.md`

`wiki/synthesis/2026-10-08/arxiv-paper-check.md` was written at **10:43** while this report was in progress; its own log entry records that it **verified its 20 featured IDs as 0-hit "with no ID overlap with the same-day sibling"** — a claim that was true against `arxiv-daily.md` but **could not have been true against this file, which did not exist yet**. Both runs independently converged on the same fresh window, and both were correct at the moment they checked.

**9 of this report's original 23 IDs were claimed by the sibling:**

| arXiv ID | Paper here | Now covered in |
|---|---|---|
| [`2610.10536`](https://arxiv.org/abs/2610.10536) | ExpDis — decoupling exploration from optimization in RLVR | [`arxiv-paper-check.md`](arxiv-paper-check.md) §② |
| [`2610.10460`](https://arxiv.org/abs/2610.10460) | Δ-MOPD — teacher-minus-base logit shift | [`arxiv-paper-check.md`](arxiv-paper-check.md) §② |
| [`2610.10422`](https://arxiv.org/abs/2610.10422) | BehaviorTrace — limits of rollout attribution | [`arxiv-paper-check.md`](arxiv-paper-check.md) §② |
| [`2610.09679`](https://arxiv.org/abs/2610.09679) | CERO — rollout budget scheduling | [`arxiv-paper-check.md`](arxiv-paper-check.md) |
| [`2610.09639`](https://arxiv.org/abs/2610.09639) | OPD teaches skills, not knowledge | [`arxiv-paper-check.md`](arxiv-paper-check.md) §② |
| [`2610.09597`](https://arxiv.org/abs/2610.09597) | COPC — coupled off-policy correction | [`arxiv-paper-check.md`](arxiv-paper-check.md) §② |
| [`2610.10062`](https://arxiv.org/abs/2610.10062) | Loud Failures, Quiet Failures | [`arxiv-paper-check.md`](arxiv-paper-check.md) §② |
| [`2610.10124`](https://arxiv.org/abs/2610.10124) | Missed Targets in Generative Recommendation | [`arxiv-paper-check.md`](arxiv-paper-check.md) §① |
| [`2610.09985`](https://arxiv.org/abs/2610.09985) | Marrying Pricing and Advertising with LLMs | [`arxiv-paper-check.md`](arxiv-paper-check.md) §① |

**Resolution: swapped, not merged** — matching the precedent set on 2026-10-07 (*"the 23 collisions were swapped, not merged"*). The 9 were removed from §3 and §4 and replaced with 9 other in-lane papers that were verified 0-hit **after** the sibling landed. §5.3 and §5.4 below now report across both files rather than duplicating the content.

**Why this matters beyond this run**: two independent runs on the same day, using different harvest strategies (this run: topic-keyword queries; the sibling: date-range category queries), **converged on 9/23 ≈ 39% overlap** of the fresh-window papers. That is a very high intersection and it means **parallel same-day runs on the same window are structurally wasteful unless they coordinate.** See follow-up #1.

## 3. Master Table

| # | Paper | arXiv | Date | Affiliation (verified) | Lane | Headline result |
|---|---|---|---|---|---|---|
| 1 | GPL | [2602.20995](https://arxiv.org/abs/2602.20995) | 02-24 | **Alibaba Group** (Taobao) + **Renmin** | Pre-ranking | production **CTR +3.07%**, long-tail lift |
| 2 | ToolRec | [2606.08466](https://arxiv.org/abs/2606.08466) | 06-07 | **HUST** + **OPPO AI Center** | On-device query rec. | **online A/B**, OPPO Xiaobu **150M MAU** |
| 3 | QueryAgent-R1 | [2606.05671](https://arxiv.org/abs/2606.05671) | 06-04 | **Alibaba International** | E-commerce query rec. | **+2.9% query CTR / +3.1% guided CVR** |
| 4 | OrDA | [2607.13420](https://arxiv.org/abs/2607.13420) | 07-15 | **Ant Group** | CTR / marketing block | **online A/B +5.64% UCTR** (Zhima) |
| 5 | PATH | [2608.29179](https://arxiv.org/abs/2608.29179) | 08-29 | **HIT Weihai** | Gen. recommendation | joint 2-token prefix alignment |
| 6 | Retention-Focused Rec. | [2609.01652](https://arxiv.org/abs/2609.01652) | 08-31 | **Hanjuku Kaso** + **Wantedly** | Online experiment | **directional, not significant** ⚠️ |
| 7 | DA-RSIR | [2610.04302](https://arxiv.org/abs/2610.04302) | 10-03 | **Nubank** | Rec. self-improvement | beats retain-all in **24/24** |
| 8 | When Rank Rises | [2610.09647](https://arxiv.org/abs/2610.09647) | 10-07 | **USC** | Post-training monitor | RankMe **inverts**: +13.5 SD while loss +75% |
| 9 | EDR | [2610.10411](https://arxiv.org/abs/2610.10411) | 10-07 | **University of Michigan** | Draft-model training | exact EDR objective, no aux. hyperparams |
| 10 | TPD | [2610.10332](https://arxiv.org/abs/2610.10332) | 10-07 | **CityU Hong Kong** + **Shenzhen Loop** | Agent distillation | ALFWorld **48.3% → 72.4%** (1.7B) |
| 11 | RewardWeaver | [2610.10120](https://arxiv.org/abs/2610.10120) | 10-07 | **Yoolee.ai** + **USTC** + **PKU** + **Tianjin** | Reward design | SOTA on SOTOPIA / bargaining / sales |
| 12 | AnchorLoop | [2610.09856](https://arxiv.org/abs/2610.09856) | 10-07 | **Waseda** + **Adelaide** | Self-evolving agents | **+2.5 / +2.8pp** over Agent0 (13 benchs) |
| 13 | RLDiscover | [2610.09218](https://arxiv.org/abs/2610.09218) | 10-06 | **UCAS** + **Baidu** + **Tsinghua** + CASIA + PKU + Shanghai + Bristol | RL algorithm search | median return gains **32–84%** per family |
| 14 | BoT-GRPO | [2610.09804](https://arxiv.org/abs/2610.09804) | 10-07 | **Amazon AGI** + **Virginia Tech** | RL algorithm | 80% compile **1.9× faster**; AIME **+8.1pp** |
| 15 | Base-model screens | [2610.10478](https://arxiv.org/abs/2610.10478) | 10-07 | **NVIDIA** + **UMN** + **UC Berkeley** | Checkpoint selection | 3 screens rank 10 pairs ≈ post-trained SWE-bench |
| 16 | CoTrace | [2610.10426](https://arxiv.org/abs/2610.10426) | 10-07 | **UCSD** + **Salesforce AI Research** + **UW** | Agents | Qwen3.5-9B **78 → 88 → 90** solved (Tmax) |
| 17 | Tool-call vector | [2610.09624](https://arxiv.org/abs/2610.09624) | 10-07 | **MBZUAI** + **UESTC** | Mechanistic | one verb flips tool-calling via causal vector μ_Δ |
| 18 | MAScope | [2610.10126](https://arxiv.org/abs/2610.10126) | 10-07 | **Beihang University** | Multi-agent diag. | topology raises Macro-F1 **0.173 → 0.350** |
| 19 | GameGo | [2610.06910](https://arxiv.org/abs/2610.06910) | 10-02 | **CAS Inst. of Automation** + **Baidu** | Games / agents | **55,060** trajectories; 124-query bench |
| 20 | MASBench ⚠️ | [2610.04672](https://arxiv.org/abs/2610.04672) | 10-03 | **BUPT** + **SJTU** + **Tsinghua** | Benchmarks | partial-observable MAS; 3 mechanisms × 3 tasks |
| 21 | Deceptive Bandit | [2610.09120](https://arxiv.org/abs/2610.09120) | 10-06 | **UC San Diego** + **SUNY Buffalo** | Game theory / RL | leak-correlated exploration → deceptive Nash eq. |
| 22 | Numerical Signalling | [2610.03033](https://arxiv.org/abs/2610.03033) | 10-02 | **LIST** + **U Trento** + **Teesside** + **Cambridge** | LLM game play | structured messages shift payoffs, **no pattern** |
| 23 | MoSDOT | [2610.10087](https://arxiv.org/abs/2610.10087) | 10-07 | **KAIST** | Offline MARL | mode-support OT fixes teacher between-mode samples |

**Window composition:** 18 fresh `2610.*` papers (10-02 → 10-07) + **5 backfill** (`2602`, `2606` ×2, `2607`, `2609`). Backfill was admitted deliberately, not filtered — **§5.3 shows that all 5 production / field-experiment numbers in this report come from the backfill.**

## 4. Per-Paper Detail

### Lane A — Recommendation / CTR / Advertising / Sequential Modeling (8)

---

#### 1. GPL: Generative Pseudo-Labeling for Pre-Ranking

- **arXiv**: [`2602.20995`](https://arxiv.org/abs/2602.20995) · submitted 2026-02-24
- **Authors**: Junyu Bi, Xinting Niu, Daixuan Cheng, Kun Yuan, Tao Wang, Binbin Cao, Jian Wu
- **Institution**: **Alibaba Group**, Beijing (Taobao) + **Renmin University**
- **Problem — the pre-ranking train-serving discrepancy**: pre-ranking models are trained **only on exposed interactions** but must score **all recalled candidates, including unexposed ones**, at serving time. This induces severe **sample selection bias** and degrades generalization **especially for long-tail content**. Existing debiasing leans on heuristics (negative sampling) or distillation from biased rankers — both of which either **mislabeled plausible unexposed items as negatives** or **propagated exposure bias into the pseudo-labels**.
- **Method**: use **LLMs to generate unbiased, content-aware pseudo-labels for unexposed items**, aligning the training distribution with the online serving space. Offline generation of **user-specific interest anchors**, matched against candidates in a **frozen semantic space** → high-quality supervision with **no added online latency**.
- **Results**: **deployed in a large-scale production system; CTR +3.07%**, with significant gains in **recommendation diversity and long-tail item discovery**.
- **Why it matters**: it attacks exposure bias at the *label* stage rather than the *loss* stage, and the diversity/long-tail improvement is the expected second-order effect of fixing the label distribution rather than reweighting it.

---

#### 2. ToolRec: calibrated preference alignment for on-device query recommendation

- **arXiv**: [`2606.08466`](https://arxiv.org/abs/2606.08466) · submitted 2026-06-07 · under review
- **Authors**: Zihan Luo, Lingkui Chen, Ruike Zhang, Hong Huang, Boyang Zhang, Ziniu Chen, Lizhong Wang, Chao Chen
- **Institution**: **Huazhong University of Science and Technology** + **OPPO AI Center** (Beijing / Shenzhen)
- **Two problems stacked**:
  1. Alignment methods are built for **chatbot scenarios**, but on-device assistant users mostly want **fast invocation of system-level tools** — a different objective than conversational quality.
  2. Aligning directly on real **click logs** injects severe noise: **varying user activity levels** dominate the signal, and **execution-oriented queries are under-emphasized**.
- **Method**:
  - **SysToolKit** — a repository of **708 system tools** paired with a **context-aware tool retrieval mechanism**, so the tools extracted for a query genuinely match user intent.
  - **Dual-level calibration** of raw click data — **user-level** calibration against user activity, **system-level** up-weighting of clicks on tool-invoking queries.
  - Align with **sample-level weighted Kahneman-Tversky Optimization (KTO)** using the refined preference signals.
- **Results**: **online A/B tests on OPPO Xiaobu, >150 million monthly active users** — significant improvement in **CTR and total click volume** over strong baselines **while maintaining high query relevance**.
- **Why it matters**: it is one of only two papers here that calibrates *the reward signal itself* before alignment, rather than changing the alignment algorithm.

---

#### 3. QueryAgent-R1: query generation grounded in inventory retrieval

- **arXiv**: [`2606.05671`](https://arxiv.org/abs/2606.05671) · submitted 2026-06-04
- **Authors**: Dike Sun, Zheng Zou, Jingtong Zang, Qi Sun, Huaipeng Zhao, Tao Luo, Xiaoyi Zeng
- **Institution**: **Alibaba International Digital Commercial Group**
- **Problem**: e-commerce query recommendation optimizes **query-level relevance** while ignoring whether retrieved products match downstream preference — producing **high query CTR but low product CVR**. **The metric being optimized is not the metric that matters.**
- **Method**: memory-augmented agentic framework with **chain-of-retrieval optimization**; query generation is grounded in **real inventory retrieval** so the agent validates and refines queries against actual retrieved products; a **consistency reward** inside agentic RL jointly optimizes relevance and downstream engagement; a memory abstraction module handles user profiling.
- **Results**: two new datasets (proprietary industrial + public), consistent offline wins; **production online A/B: query CTR +2.9%, guided CVR +3.1%**.

---

#### 4. OrDA: orthogonal disentanglement of access habits

- **arXiv**: [`2607.13420`](https://arxiv.org/abs/2607.13420) · submitted 2026-07-15
- **Authors**: Lingxiao Zhang, Xiaobo Li, Tao Xu
- **Institution**: **Ant Group**, Hangzhou
- **Problem**: clicks on homepage marketing blocks are driven by a **dual mechanism — content interest and access habit**. Habitual clicks create **Pseudo-Positives** in marketing slots, where position advantage masks mediocre content quality, producing a biased recommendation ecosystem.
- **Method**: dual-tower structure with a **gated allocation layer** routing features adaptively; **orthogonal regularization** constraining the latent *interest* and *habit* manifolds to be geometrically perpendicular; **do-calculus causal intervention at inference** to rank items by the purified interest score alone.
- **Results**: **online A/B test +5.64% user click-through rate (UCTR)** on the **Zhima homepage marketing block, Zhima rent-floor recommendation**.

---

#### 5. PATH: history-conditioned joint-prefix alignment

- **arXiv**: [`2608.29179`](https://arxiv.org/abs/2608.29179) · submitted 2026-08-29
- **Authors**: Hongliang Sun, Lianjie Li, Bolin Zhang, Dianbo Sui, Dianhui Chu, Zhiying Tu
- **Institution**: **HIT Weihai** — Dept. of CS + Weihai & Qingdao Research Institute
- **Observation first, method second**: across three benchmarks, **most missed targets in generative recommendation are pruned within the first two decoding steps**. But retaining only the first-token branch does not help — if the *continuation* is pruned at step two, first-token survival improves while **complete-path retention does not**. Aligning only the first-token distribution is therefore a **local improvement with no end-to-end effect**.
- **Method**: aggregate transition statistics from the training corpus over recent interactions **with exponential decay** → history-conditioned **two-token** prefix targets; align the model's joint prediction to them with forward KL via a chain-rule decomposition admitting an **unbiased Monte Carlo estimate**. At inference the *same* statistics give **PMI calibration** to rerank completed candidates against global prefix frequency.
- **Results**: consistent gains on Beauty, Instruments, Yelp, plus higher **full-SID survival rates**.
- **A backfill paper, admitted because the causal diagnosis (first-token-only alignment is insufficient) was recorded nowhere in this wiki.**

---

#### 6. Retention-Focused Recommendation in Job Matching — a null result worth recording

- **arXiv**: [`2609.01652`](https://arxiv.org/abs/2609.01652) · submitted 2026-08-31
- **Venue**: RecSys in HR '26 (6th Workshop on Recommender Systems for Human Resources), ACM RecSys 2026
- **Authors**: Tatsuya Ute, Chiaki Ichimura, Yuta Saito · **Hanjuku Kaso** + **Wantedly** (emails `@hanjuku-kaso.com`, `@wantedly.com`)
- **Observation**: on a real job-matching platform, **users with very few recent matches are much more likely to leave**, while **additional matches for already-successful users provide limited marginal retention value** — so maximizing match count is **misaligned with churn and revenue**.
- **Method**: formulate **retention-aware recommendation** and implement a deliberately simple **post-processing score boost** for churn-risk users on top of the baseline match-focused ranking.
- **Results ⚠️**: the treatment group showed **directionally lower user churn than control, but the estimated effect was NOT statistically significant at conventional levels**; company-side churn showed **no evidence of deterioration**.
- **Why it is featured anyway**: it is, by the authors' own statement, **among the first online experimental studies of retention-focused recommendation in a real reciprocal job-matching platform** — and it **publishes the null**. A field experiment that reports a non-significant primary outcome is materially more useful to this wiki than another offline benchmark win, because it calibrates how hard the engagement-vs-retention trade-off is in practice.

---

#### 7. DA-RSIR: post-verification acquisition

- **arXiv**: [`2610.04302`](https://arxiv.org/abs/2610.04302) · 15 pages
- **Authors**: Tonmoy Hasan, Taylor Foust, Shao Tang, Leonardo Neves, Aman Gupta, Hiroto Udagawa, Helder Dias, Daniel Silva, Rohan Ramanath
- **Institution**: **Nubank**
- **Problem**: recursive self-improvement loops for sequential recommenders generate synthetic interaction sequences, verify them against real interactions, and retrain. Verification answers *which sequences pass*. It does **not** answer *which verified sequences should train the next model* — and current practice trains on all of them, so **source sequences that yield more verified sequences or longer continuations exert more influence**, neither of which indicates usefulness.
- **Method**: name the gap **post-verification acquisition**. DA-RSIR **caps each source sequence's contribution** and ranks its verified descendants by **disagreement of the model's predictions over the augmented interactions** — a BALD score estimated with MC dropout. Requires **no extra labels, no teacher model, no quality scorer**.
- **Results**: 4 datasets × 3 recommender models × 2 metrics = **24 comparisons; beats retain-all in 24/24**, highest mean in 23/24, aggregate improvement significant on both metrics. **A single DA-RSIR round exceeds retain-all's best gain over five recursive rounds.**
- **Why it matters**: reframes recursive self-improvement as having **two independent control points** — verification, then selection. A filter is not a selector.

---

#### 8. When Rank Rises as LLMs Degrade

- **arXiv**: [`2610.09647`](https://arxiv.org/abs/2610.09647) · 8 pages + appendix
- **Venue**: NeurIPS 2026 Workshop on Continual Learning for Foundation Models and Agents (CL4FMAgents)
- **Author**: Zhaohui Geoffrey Wang · **University of Southern California**
- **The claim under attack**: practitioners monitor representation health with **RankMe** and related spectral statistics, **assuming rank falls when representations degrade**.
- **Result**: on Qwen3-0.6B, 4 degradation modes, 3 seeds — **data duplication worsens held-out loss by 75%** while *increasing* both original and centred RankMe; the centred version moves by **13.5 pooled standard deviations**, and covariance effective rank rises to **~2× its healthy value**. The failure mode is **spectral dispersion, not collapse**, so **a one-sided monitor rates the worst checkpoint as the healthiest**.
- **A second, subtler finding**: the two statistics are routinely conflated. **RankMe normalizes singular values; covariance effective rank normalizes eigenvalues.** On raw intermediate-layer pretrained states, massive activations pin the covariance version near 1 out of dimension *d* while RankMe retains usable range. *"Direction is therefore a property of the regime–statistic pair and cannot be fixed by recalibration alone."*
- **The proposed fix, and its honest limits**: a two-sided, multichannel sequential monitor with separate calibration/test data detects all three damage regimes **10–60 steps after the fork** in a pre-registered leave-one-seed-out evaluation, and separates dispersion from downward-rank damage by firing direction. **But it never precedes held-out probe loss**, and calibration on two seeds produces false alarms on the held-out healthy seed.
- **Verdict**: *"Spectral monitoring can diagnose failure regimes, but it does not warn earlier than held-out loss, and validity claims require held-out healthy data."*
- **See §5.4** — this is this report's contribution to a cautionary cluster that also spans the same-day sibling.

---

### Lane B — LLM Post-Training: Draft Models, Reward Design, Agent Distillation, Algorithm Search (7)

---

#### 9. EDR: training parallel draft models by directly minimizing expected decoding rounds

- **arXiv**: [`2610.10411`](https://arxiv.org/abs/2610.10411) · submitted 2026-10-07
- **Authors**: Yunxiao Zhao, Changxiao Cai · **University of Michigan**, Dept. of Industrial and Operations Engineering
- **The coupling prior objectives miss**: parallel and semi-autoregressive drafters propose a whole block in one forward pass, but **the draft distribution at a given position depends on where the decoding round starts — and where rounds start depends on how many tokens earlier rounds accepted.** Existing training objectives use **block-local surrogates that ignore this cross-round coupling**, so they do not directly optimize global decoding efficiency.
- **Method**: represent speculative decoding as a **Markov reward process** → the **Expected Decoding Rounds (EDR)** objective, which weights local rejection costs by **state occupancies** and **exactly equals the expected number of decoding rounds**. It introduces **no auxiliary hyperparameters**. From it the authors derive an **exact temporal-difference gradient** supporting unbiased stochastic optimization from target-model rollouts, plus an **exact offline evaluator for round counts**, enabling paired drafter comparisons on shared target rollouts **without running speculative decoding**.
- **Results**: fine-tuning two state-of-the-art drafters (**DSpark, DFly**) with EDR **consistently improves mean accepted length and outperforms existing training objectives across nine benchmarks** spanning math reasoning, code generation, and chat.
- **Why it stands out**: it replaces a surrogate with the **exact quantity of interest**, and hands back an exact *offline* evaluator — the rare case where the theory removes a knob rather than adding one.

---

#### 10. TPD: Task-Progress Distillation

- **arXiv**: [`2610.10332`](https://arxiv.org/abs/2610.10332) · submitted 2026-10-07
- **Author**: Wenxi Gan · **City University of Hong Kong** + **Shenzhen Loop Area Institute**
- **Question**: when distilling a large model's demonstrations into a small agent, **what should be retained — reasoning, actions, or task progress?**
- **Method**: **Task-Progress Distillation (TPD)** pairs each demonstrated action with a **short label describing the current task stage**. The student learns these **compact targets** and selects actions by **jointly scoring admissible stage–action pairs**, executed by a deterministic harness in the environment.
- **Results on ALFWorld (1.7B student)**:
  | Demonstrations | Best result |
  |---|---|
  | 404 | **72.4%** mean unseen success (TPD *or* action-only) vs **48.3%** for a reasoning-trained student with constrained action selection |
  | 200 | explicit stages give **48.0% → 67.7%** over action-only |
  | 808 | **both reach 76.9%** — the gap closes |
- **The interesting limit**: **explicit task progress helps at an intermediate demonstration budget and stops helping once demonstrations are plentiful.** Shared-history analysis localizes TPD's advantage to **decisions at subgoal transitions**, particularly object acquisition → processing.
- **Takeaway the authors state plainly**: compact supervision can train effective small task agents; *explicit progress is a scarce-data aid, not a free win.*

---

#### 11. RewardWeaver: self-evolving reward adaptation for long-horizon agents

- **arXiv**: [`2610.10120`](https://arxiv.org/abs/2610.10120) · 23 pages, 4 figures
- **Authors**: Hengbo Xiao, Boyao Zhang, Purui Liu, Yuxuan Zheng, Haoran Yin, Haibo Liu, Fan Zhang
- **Institution**: **Yoolee.ai** + **USTC** + **Peking University** + **Tianjin University**
- **Diagnosis**: RLVR works where outcomes are verifiable, but long-horizon interaction has **sparse terminal feedback and hard credit assignment**. Process rewards add density — yet **the capabilities most relevant for training change as the policy evolves**: *a behavior that is easy to evaluate or frequently deficient need not be the bottleneck currently limiting task success.* Static process-reward suites therefore train against a moving target with a fixed map.
- **Method**: RewardWeaver maintains a **validated capability space in which the semantics of admitted rubrics stay fixed**, and closes the loop **policy optimization → task evaluation → failure attribution → reward adaptation**:
  1. after each training stage, run **outcome-grounded backward attribution** on low-outcome trajectories;
  2. aggregate **recurrent** and **policy-controlled** capability bottlenecks;
  3. **dynamically select the corresponding process rewards** for the next stage;
  4. recurrent failures outside the existing capability space trigger a **separate, controlled expansion procedure** — so the rubric vocabulary grows without destabilizing what is already admitted.
- **Results**: SOTOPIA, Amazon-HistoryPrice, and a newly constructed Sales Benchmark — **new state of the art** across **social interaction, bilateral bargaining, and domain-specific sales**. Ablations confirm the contributions of dynamic reward allocation, failure-grounded attribution, and **stable semantics for admitted capabilities**.
- **Why it belongs in this report**: it treats **the reward function as the thing being optimized over time**, with an explicit stability constraint on its own vocabulary — the sharpest version of "reward design is the new fine-tuning" in this window.

---

#### 12. AnchorLoop: anchored training of self-evolving tool-integrated agents

- **arXiv**: [`2610.09856`](https://arxiv.org/abs/2610.09856) · submitted 2026-10-07
- **Authors**: Wenjie Liao, Liangjie Zhao, Zehong Cao · **Waseda University** + **Adelaide University**
- **Two failure modes of self-evolving agent loops**:
  - **group-relative advantages vanish under full consensus** — when the Executor agrees with itself, there is no signal left;
  - **uncertainty-based curriculum rewards favor disagreement** without showing whether the generated tasks actually support further learning.
- **Method**: **AnchorLoop** introduces a **frozen copy of the previous iteration's Executor as a historical reference**, reused on **both sides** of the loop:
  - *Executor side* — a **cross-reference advantage** evaluating current outputs against both current and historical majority answers;
  - *Curriculum side* — an **agreement-based reference** derived from differences in sampled majority agreement.
- **An explicit caveat the authors state**: during Curriculum training the Executor and anchor have **identical parameters**, so this comparison is **a proxy for task selection, not evidence of inter-version improvement or correctness.** (Recording the caveat verbatim — it is the kind of scope claim this wiki should not launder.)
- **Results**: across **13 reasoning benchmarks**, **+2.5% mathematical reasoning and +2.8% general reasoning over Agent0**; maintains **higher effective-advantage variance** and **keeps improving in later iterations while the unanchored baseline's gains diminish**.
- **Claim**: benefit achieved **without external task or answer supervision**.

---

#### 13. RLDiscover: LLM-driven co-evolution of RL algorithms

- **arXiv**: [`2610.09218`](https://arxiv.org/abs/2610.09218) · submitted 2026-10-06
- **Authors**: Haoran Li, Zengle Ge, Xiaomin Yuan, Yui Lo, Songlin Zhou, Jiahua Ying, Haoxin Li, Qianhui Liu, Yuanhang Liu, Jiaqun Liu, Guokai Chen, Mingju Chen, Ruinan Wang, Annan Li, Jianmin Wu, Dawei Yin, Dou Shen (17)
- **Institution**: **University of Chinese Academy of Sciences** + **Baidu** + **Tsinghua** + **Institute of Automation, CAS** + **Peking University** + **Shanghai University** + **University of Bristol**
- **Two obstacles to self-evolving RL algorithms**:
  1. **joint search over coupled components doesn't scale** — simultaneous changes disrupt learning, isolated changes overlook their dependencies;
  2. **evaluation is costly and fitness stays uncertain across random seeds.**
- **Method**: (i) **Progressive Co-Evolution** — advance from targeted component edits to joint evolution; (ii) **Progressive Probabilistic Evaluation** — balance search breadth against evaluation fidelity through **staged training and repeated evaluation**.
- **Results**: SAC, PPO, DQN across four benchmark suites — **per-family median return gains of 32%–84%**, and a **peak return ratio of ~363× over a near-zero baseline** (⚠️ the denominator is near-zero; read this as "failed → successful", not as a 363× improvement over a working method). Gains include **transitions from failed learning to successful task completion**, and **persist when evolution starts from stronger open-source implementations**.
- **Efficiency claim**: on measured SAC locomotion runs, evaluation uses **~1/15 the estimated compute** required to fully evaluate the same candidate pool.
- **The result that matters most**: independent searches **repeatedly discover the same interpretable combinations** — adaptive robust losses, progress-dependent value targets, running statistics — and **the selected programs transfer to unseen tasks.** Reproducible discovery, not a one-off lucky program.

---

#### 14. BoT-GRPO: process rewards without a critic

- **arXiv**: [`2610.09804`](https://arxiv.org/abs/2610.09804)
- **Venue**: COLM 2026 Workshop on Efficient Reasoning
- **Authors**: Yingxiang Yang, Weihang Xiao, Zhunxuan Wang, Joshua Flashner, Niresh Agarwal
- **Institution**: **Amazon AGI** + **Virginia Tech**
- **Gap**: GRPO gives **every token in a rollout the same advantage**. Process supervision normally costs a value network.
- **Method — Bag-of-Tokens GRPO**: extend GRPO to token-level reward models with a **length-invariant "bag of tokens" aggregation** — collect all token-level rewards across rollouts, weight each by the **inverse of its source sequence length**, compute per-token advantages relative to **weighted group statistics**. **Critic-free**, and a **drop-in replacement anywhere GRPO is used** when token-level reward is available.
- **Results**:
  - React front-end code generation: **80% compile rate up to 1.9× faster than GRPO**, converging faster than GSPO, DAPO, and PURE while reaching higher final compile and VLM-judged win rates.
  - AIME: **absolute Pass@$k$ gains up to +8.1% over GRPO in half the steps**.
  - Across reasoning and non-reasoning base families (Qwen2.5-3B, SmolLM3-3B, Phi-4-mini-reasoning).
- **The practical recipe it extracts**: **reward stability matters more than richness** — clean, bounded, stable fine-grained signals accelerate learning where noisier, richer alternatives stall.

---

#### 15. Predicting agentic post-training payoff from the base model

- **arXiv**: [`2610.10478`](https://arxiv.org/abs/2610.10478)
- **Authors**: Tan Yu, Alexander Bukharin, Khushi Bhardwaj, Jennifer Williams, Zirui Liu, Jonathan Lingjie Li, Soumye Singhal, Joseph Jennings, Sanjeev Satheesh, Yash Jain, Ashish Vaswani, Venkat Krishna Srinivasan, Matthew Papakipos, Hyunwoo Kim, Jian Zhang, Oleksii Kuchaiev, Markus Kliegl, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jonathan Cohen, Jiantao Jiao (22 authors)
- **Institution**: **NVIDIA** + **University of Minnesota – Twin Cities** + **UC Berkeley** (corresponding: `jiantaoj@nvidia.com`)
- **Question**: **which base checkpoint is worth an expensive round of agentic post-training?**
- **Why existing proxies fail**: end-to-end pass@$K$ tests whether successful behavior already *appears* in the base distribution, but is a poor fit for agentic coding — **many base checkpoints cannot reliably produce the well-formed tool invocation needed to finish a task at all**. Single-shot / short-horizon tasks dodge those failures by collapsing a multi-step interaction into one prompt and one patch, **but sidestep exactly the capability in question**: maintaining coherent state over many tool-using steps as the repository evolves.
- **Method — use the post-trained trajectories as a lookahead signal**:
  1. Replay each successful post-trained trajectory, **rerunning tests after every code-changing step**, to find the **decisive step**: the first step whose cumulative patch flips the repository from failing to passing, certifying that the recorded action solves the task *given the prior context*.
  2. Build three screens **at that step**, none of which requires the base checkpoint to drive the harness from cold start: **Decisive-Action BPB** (probability mass on the certified action), **Patch MCQ** (that action vs. alternatives rejected by the same verifier), and **prefix-conditioned pass@$K$** (support for functionally-correct continuations).
- **Results**: across **ten pairs of public base and post-trained models**, **all three screens rank the cohort in close agreement with post-trained SWE-bench Verified pass@$1$**.
- **Generalization claim**: because the method needs only *a benchmark's successful trajectories and its verifier*, **any future agentic coding benchmark with a verifier becomes a base-model evaluation.**

---

### Lane C — Agents (3)

---

#### 16. CoTrace: a harness-aware data recipe

- **arXiv**: [`2610.10426`](https://arxiv.org/abs/2610.10426) · preprint, 32 pages, 17 tables
- **Authors**: Jixuan Chen, Jiaxin Zhang, Qinyuan Ye, Yada Pruksachatkun, Haoxiang Zhang, Jingming Zhuo, Yifan Zhang, Yutong Dai, Juntao Tan, Xiangyu Peng, Silvio Savarese, Zeyuan Chen, Lianhui Qin, Chien-Sheng Wu
- **Institution**: **UC San Diego** + **Salesforce AI Research** + **University of Washington**
- **Core claim**: terminal-agent capability depends jointly on **model weights and the runtime harness** (prompt formatting, tool binding, error recovery). Existing harness–model co-evolution treats trajectories from harness search as an **undifferentiated replay buffer**, which **overlooks that a trajectory's value for training depends on the harness it was produced under**.
- **Method**: an **alternating co-evolution framework** decoupling harness search from policy training via **component-wise promotion decisions**. Within it, **CoTrace** is a harness-aware data recipe governing **trajectory routing, provenance matching, and curriculum refresh**:
  - recurring execution failures → **harness synthesis**;
  - policy training strictly conditioned on **verified rollouts matched to the adopted runtime** (SFT) or **fresh online interactions** (RL).
- **Results**: on the **Tmax promotion split**, CoTrace advances **Qwen3.5-9B from 78 → 88 solved tasks** under SFT, while an online RL variant reaches **90**. **A compact harness-matched corpus produces steady gains at substantially lower compute than much larger corpora pooled across sibling harnesses.**
- **Transfer finding**: on Terminal-Bench 2.1 and SWE-bench Lite, **out-of-distribution transfer depends fundamentally on harness compatibility** — keeping train and eval runtimes consistent prevents the **procedural execution breakdown** seen under foreign scaffolds.

---

#### 17. A Tool-Call Vector Shaped by Suppression

- **arXiv**: [`2610.09624`](https://arxiv.org/abs/2610.09624) · **NeurIPS 2026 Main Poster** · [code](https://github.com/XijieGo/MI4ToolCalling)
- **Authors**: Xijie Gong, Tingxu Han, Jiahao Zhang, Wei Song, Ziqi Ding, Hanqi Yan, Youcheng Sun, Lijie Hu
- **Institution**: **Mohamed bin Zayed University of Artificial Intelligence** + **University of Electronic Science and Technology of China**
- **Problem**: agentic prompts are long and heavily scaffolded — role instructions, tool schemas, format templates, request — across hundreds of tokens, so there is **no single controllable variable for mechanistic analysis**.
- **Trick that creates one**: convert complex agentic prompts into **minimal contrastive pairs where a single request verb determines the tool-call decision**. Replacing an execution verb (*write*) with an analysis verb (*discuss*) **reliably flips the decision**, implying mediation by a **compact internal state**.
- **Scale**: 500 paired prompts across Python, Java, C++ (300 mechanistic, 200 held out).
- **Finding**: the decision is traced to a vector **μ_Δ** that is **causally necessary and sufficient**, and generalizes to native multi-turn **τ²-Bench** trajectories and verb-free requests.
- **Mechanism**: the **scaffold establishes a tool-call prior**; **Transcoder decomposition** shows analysis verbs **suppress that prior** via features signaling tool use is unnecessary, while execution verbs leave it largely intact. Downstream **scaffold-reading attention heads and MLP features** read out the resulting state. **The same mechanism recurs across seven models from Qwen, Mistral, and Granite.**

---

#### 18. MAScope: topology-conditioned diagnosis of multi-agent failures

- **arXiv**: [`2610.10126`](https://arxiv.org/abs/2610.10126)
- **Authors**: Xinwen Liu, Zhuocheng Pan, Isabella Zhu, Jawei Zhang, Xudong Liu, Tianyu Wo
- **Institution**: **Beihang University**, Beijing
- **Problem**: in multi-agent LLM systems, **similar symptoms in execution traces reflect different problems** in how information is passed, used, or verified. **Communication topology** carries structural cues — but real traces carry **no explicit topology labels**.
- **Method, two stages**: (i) **Trace Structural Extractor (TSE)** recovers the communication topology by grounding an interaction graph in message evidence; (ii) **Topology-Conditioned Judge (TC-Judge)** classifies failures using trace + predicted topology + an **empirical failure prior** from separate labeled traces + a short description of topology-specific failure patterns. Under a fixed orchestration, the recovered topology is **reused across executions**.
- **Results**: statistically significant topology↔failure association, **χ² = 409.9, p = 1.2 × 10⁻⁷⁰**. On **851 MAST-clean traces**, ground-truth topology context raises gpt-mini **Macro-F1 0.173 → 0.350**; with *predicted* topology the pipeline reaches **0.346**, approaching the trace-only gpt-5.4 baseline of **0.372**.
- **Cost claim**: for 1,000 traces under fixed orchestration, projected pipeline cost (including one topology extraction) is **~6% of repeated gpt-5.4 diagnosis cost**.

---

### Lane D — Games, Multi-Agent Strategy, Offline MARL (5)

---

#### 19. GameGo: game-dev agents with synthetic trajectories

- **arXiv**: [`2610.06910`](https://arxiv.org/abs/2610.06910) · submitted 2026-10-02
- **Authors**: Haoyue Yang, Jingyao Li, Zhengfan Wu, Jing Liu, Xuanle Zhao, Kang Liu
- **Institution**: **Institute of Automation, Chinese Academy of Sciences** + **Baidu Inc.**, Beijing
- **Diagnosis**: coding agents asked to generate complex games directly from **sparse user queries** make **underspecified assumptions**, yielding incomplete mechanics, disconnected gameplay flows, and limited visual aesthetics. Prior work either uses complex multi-turn workflows or only builds static evaluation benchmarks.
- **Method**: GameGo transforms brief game seeds into **comprehensive Product Requirements Documents grounded in industry game-development practice**, using **task-specific dynamic compression** to maximize information density **while preserving instruction following** — keeping core gameplay constraints without restricting design exploration.
- **Artifacts**: **GameGoData — 55,060 development trajectories** across 2D, 2.5D, and 3D games; **GameGoBench — 124 diverse game queries**. Training **GameGoCoder** on GameGoData yields a model that **outperforms matched baselines and is comparable to frontier models** across gamedev benchmarks. Code, datasets, models to be released.
- **Positioning**: targets **end-to-end real-world game synthesis** rather than static game-code evaluation — explicitly against the benchmark-only tradition.

---

#### 20. MASBench — under partial observability ⚠️ name collision, see §2.1

- **arXiv**: [`2610.04672`](https://arxiv.org/abs/2610.04672) · submitted 2026-10-03
- **Authors**: Qizhi Chu, Zekai Yu, Sijie Wen, Yang Liu, Chen Qian, Cheng Yang, Chuan Shi, Zhiyuan Liu
- **Institution**: **Beijing University of Posts and Telecommunications** + **Shanghai Jiao Tong** + **Tsinghua University** (correspondence: `yangcheng@bupt.edu.cn`) · [code](https://github.com/BUPT-GAMMA/MASBench)
- **Gap**: real-world collaboration is **typically partially observable** — each agent sees only part of the environment because of physical or privacy constraints — yet **most multi-agent benchmarks assume global observability** and offer little support for systematically evaluating collaboration *mechanisms*.
- **Design**: three progressive task categories — **Reasoning, Scheduling, Game** — used to evaluate three representative mechanisms — **Protocol, Memory, Routing**. Deterministic metrics: **performance score, communication cost, cost effectiveness** (both outcome *and* communication overhead).
- **Output**: empirical guidance for effective MAS design across diverse LLM backbones and mechanism configurations.
- **⚠️ Not to be confused with the `MASBENCH` recorded in [`../2026-09-05/conference-digest.md`](../2026-09-05/conference-digest.md) as part of MAS-Orchestra — see §2.1.**

---

#### 21. The Deceptive Bandit Problem

- **arXiv**: [`2610.09120`](https://arxiv.org/abs/2610.09120) · submitted 2026-10-06
- **Authors**: Michael Tang, Mahmoud Abdelgalil, Jorge I. Poveda
- **Institution**: **UC San Diego** (ECE) + **SUNY Buffalo** (Mechanical and Aerospace Engineering) · funded in part by NSF DGE-2545911, CMMI 2228791, DARPA HR0011-25-03225
- **Reframe**: the **independence and privacy of randomized exploration** are usually treated as *technical assumptions* in bandit learning, multi-agent RL, and zeroth-order policy search. This paper shows they are **security-critical**.
- **Setup**: a **deceiver–victim pair** in the minimal two-player strongly monotone setting, where the deceiver obtains **leaked signals merely *correlated* with the victim's exploration** — not the exploration itself.
- **Result**: by **coupling its own exploratory action** to those signals, the deceiver **injects an externality** that steers the learning dynamics to a new steady state, the **deceptive Nash equilibrium (DNE)**. Deceptive bandit learning (DBL) converges to an **arbitrarily small neighborhood of the DNE at optimal convergence rates**, while **relaxing the second-order smoothness conditions** standard in the bandit-optimization literature.
- **Characterization**: conditions under which deception **strictly shifts the steady state**, and its effect on the deceiver's cost, illustrated in a **resource-allocation game**.
- **Relevance**: a formal result with a concrete security reading — **a correlated leak is enough**; you do not need to read the victim's randomness.

---

#### 22. When Numbers Start Talking

- **arXiv**: [`2610.03033`](https://arxiv.org/abs/2610.03033) · submitted 2026-10-02
- **Authors**: Alessio Buscemi, Daniele Proverbio, Alessandro Di Stefano, The Anh Han, German Castignani, Pietro Liò
- **Institution**: **Luxembourg Institute of Science and Technology** + **University of Trento** + **Teesside University** (SCEDT) + **University of Cambridge** (Computer Science and Technology)
- **Design**: **four popular LLMs × four games with different cooperation equilibria**, varying message type — **natural language, numerical signals, random sequences** — and assigned agent personalities.
- **Finding 1**: **structured messages alter final payoffs for most games and LLMs, but without a predictable pattern**. The authors read this as challenging *"the assumption that AI agents can converge to stable equilibria regardless of additional capabilities."*
- **Finding 2**: agent-generated **numerical messages depart from randomness** — most strongly and consistently **when agents are explicitly instructed to communicate**. Their symbol distributions track the **payoff structure**, **concentrate with repetition**, and are **overall difficult for humans to interpret**.
- **Recommendation**: monitoring coordination among AI agents through restricted channels should **prioritise message-level fingerprints, which generalise across models, over behavioural decisions, which do not**.
- **Why it stands out**: it is the only paper here measuring **what LLM agents actually do with a restricted signalling channel** — relevant to anyone reasoning about multi-agent protocols or communication audits.

---

#### 23. MoSDOT: support-preserving distillation for offline MARL

- **arXiv**: [`2610.10087`](https://arxiv.org/abs/2610.10087) · **NeurIPS 2026 Main Track, Poster**
- **Authors**: Sangmin Lee, Youngju Na, Chanmi Lee, Sung-eui Yoon · **School of Computing, KAIST**
- **Failure mode located at the teacher, not the student**: offline MARL distills a centralized teacher into decentralized one-step actors under CTDE. Standard **flow-based teachers pair noise with replay targets independently**, so **nearby noise samples can be routed toward conflicting coordination modes**. The teacher then samples **between** valid modes — and because the distillation loss **regresses each local actor onto the conditional mean** of the teacher's output given local input, **this error is not absorbed but propagated to the student.**
- **Method**: **Mode-Support Semi-Discrete Optimal Transport (MoSDOT)** — summarize multimodal replay into a **finite mode support with prescribed capacities**, then use **conditional semi-discrete optimal transport to assign each noise sample to a single mode before teacher training**, removing the artifact at the source. Additionally a **shared-randomness variant** uses a shared noise component at execution to **expose the residual gap intrinsic to strict-product execution**.
- **Results**: on controlled diagnostics and offline MARL benchmarks, MoSDOT **improves endpoint quality and routing consistency**, particularly on datasets with **multimodal joint behavior**.
- **Why it is in the games lane**: it is a *distillation* paper whose failure mode is fundamentally about **coordination modes** — the multi-agent analogue of the between-mode sampling problem, and a clean instance of "the error is created upstream and laundered downstream by a conditional-mean loss."

---

## 5. Cross-Cutting Observations

### 5.1 The keyword sweep confirmed the 10-06 advice — by counterexample

| Metric | [`../2026-10-06/arxiv-ai-search.md`](../2026-10-06/arxiv-ai-search.md) (ID-range, fresh window) | **This run (keyword sweep, unbounded)** |
|---|---|---|
| Pool | 916 unique, **all** `2610.*` fresh | 717 unique, **mixed age**, keyword-filtered |
| New papers found | **16** | **23 shortlisted**, but only **8 in-lane** |
| New in the **recommendation/CTR** lane | **6** | **8**, of which **5 are backfill** from Feb–Sep |
| In-lane IDs already on file | not applicable (fresh window) | **175** |
| Production / field numbers | 0 | **5 — all in backfill** |

Queries 1 and 5 match **12,545** and **781** papers respectively; only the newest 100 of each were fetched, and the retrievable top of that space has been swept daily since June — hence **175 already-claimed in-lane IDs**. Meanwhile **5 of the 8 fresh `2610.*` recommendation-lane papers that this report could have featured were already on file**, and the survivors are thin.

**The conclusion to carry forward**: the recommendation-lane keyword space is **mined out for this wiki**, not because arXiv has stopped publishing there, but because **keyword sweeps retrieve the same canonical top-100 every day**. Further yield in that lane requires **ID-range enumeration of the fresh window** — not better keywords. Keywords remain the right tool for lanes *not* on a daily cadence, which is exactly where this report's Lane B and Lane D content came from (queries 3, 6, 7, 8).

### 5.2 Same-day sibling races are now a structural waste, not an accident

`arxiv-paper-check.md` and this report were written in parallel on 2026-10-08 using **different harvest strategies** — the sibling used **date-range + category queries** (`submittedDate:[202610070000 TO 202610082359]` across cs.IR/cs.CL/cs.AI/cs.LG, 416 unique), this run used **topic-keyword queries** across the same period. Both independently shortlisted the fresh window. **They overlapped on 9 papers — 39% of this report's original 23.**

Neither run was wrong: each verified its picks against `wiki/` immediately before writing, and each was correct *at the moment it checked*. The failure is **temporal, not analytical** — two agents taking a read-modify-write cycle on the same target without a lock.

Note also that the sibling's own log claims *"no ID overlap with the same-day sibling"* — true against `arxiv-daily.md`, **unverifiable against this file, which did not exist at its write time.** A dedup claim scoped to "siblings I can see" will be wrong whenever runs overlap. **This is the second consecutive day on which same-day sibling coordination has been a documented problem** ([`../log.md`](../log.md), 2026-10-07: *"the run's defining event was a sibling dedup collision"*). See follow-up #1.

### 5.3 Every production / field-experiment number in this report is backfill

| Paper | Date | Institution | Evidence |
|---|---|---|---|
| [`2602.20995`](https://arxiv.org/abs/2602.20995) GPL | 02-24 | Alibaba Group (Taobao) | production, **CTR +3.07%**, long-tail/diversity lift |
| [`2606.05671`](https://arxiv.org/abs/2606.05671) QueryAgent-R1 | 06-04 | Alibaba International | online A/B, **query CTR +2.9% / guided CVR +3.1%** |
| [`2606.08466`](https://arxiv.org/abs/2606.08466) ToolRec | 06-07 | HUST + OPPO AI Center | online A/B, **OPPO Xiaobu, >150M MAU**, CTR + click volume ↑ |
| [`2607.13420`](https://arxiv.org/abs/2607.13420) OrDA | 07-15 | Ant Group | online A/B, **+5.64% UCTR** (Zhima) |
| [`2609.01652`](https://arxiv.org/abs/2609.01652) Retention-Focused Rec. | 08-31 | Hanjuku Kaso + Wantedly | online experiment, **directional but not significant** ⚠️ |

**Zero of the 18 fresh `2610.*` papers report a completed online A/B test or field experiment.** Combined with the 10-05 finding (7 of 8 papers industrial-with-A/B) and the 10-06 finding (0 of 16 with A/B), this is now **three consecutive runs**: *A/B density in a report is a function of query design and window choice, not of the week's publishing.*

Two things worth carrying forward:
- **A fresh-window-only report contains no deployable evidence.** That is why backfill was admitted here rather than filtered.
- **The one field experiment in the set reports a null** (§4.6). If this wiki's evidence base for "engagement metrics vs. retention" rests on positive offline results, [`2609.01652`](https://arxiv.org/abs/2609.01652) is the corrective.

### 5.4 A cross-run cautionary cluster — four papers, two files, one shape

Four papers across this report and the same-day sibling argue that a widely-adopted practice **measures something adjacent to what it claims to measure**:

| Paper | File | Trusted practice | What it shows |
|---|---|---|---|
| [`2610.09647`](https://arxiv.org/abs/2610.09647) When Rank Rises | **here** | RankMe as representation-health monitor | **inverts**: +13.5 SD while held-out loss worsens 75%; one-sided monitor rates worst checkpoint healthiest |
| [`2610.09639`](https://arxiv.org/abs/2610.09639) OPD ≠ knowledge | [`arxiv-paper-check.md`](arxiv-paper-check.md) | on-policy distillation as knowledge transfer | reverse-KL OPD transfers **skill but essentially no facts** |
| [`2610.10422`](https://arxiv.org/abs/2610.10422) BehaviorTrace | [`arxiv-paper-check.md`](arxiv-paper-check.md) | rollout-level training-data attribution | a **gradient-size control with no behavior target** matches/beats the best targeted estimator on 2/3 seeds |
| [`2610.10062`](https://arxiv.org/abs/2610.10062) Loud/Quiet Failures | [`arxiv-paper-check.md`](arxiv-paper-check.md) | prompting agents to verify tool output | the prompt line **did not move detection**; reasoning models notice *less* than instruct siblings |

**All four ship a usable substitute** — a two-sided monitor, a forward-KL swap, an attribution checklist, a fault-injection harness — rather than only a refutation. That combination (*the metric misleads; here is a replacement you can run*) is the signature of a **methodologically maturing lane**, and it is now visible across **two independently-written same-day reports**, which is weak evidence that the pattern is in the field rather than in one run's selection bias. **Flagging for trend: if the ratio holds over the next three runs, this deserves its own synthesis page.**

**Related, and originally this report's §5.4**: the sibling independently recorded the same convergence I had drafted — [`2610.10460`](https://arxiv.org/abs/2610.10460) Δ-MOPD (*"target construction is an independent design axis … complementary to teacher selection"*) and [`2610.09639`](https://arxiv.org/abs/2610.09639) OPD (*"does not expand parametric knowledge … teaches it to organize and compose the knowledge it already possesses"*), both posted 2026-10-07, neither citing the other, **both locating the distillation lever in the target/loss rather than in teacher selection.** Two independent groups, same day, same axis. Recorded here as cross-referenced rather than duplicated — see follow-up #4 for promoting it to a claim page.

### 5.5 Affiliation composition

Of 23 papers: **13 university / public-research lead affiliations** (counting multi-institution papers by lead), **9 industry affiliations across 8 papers** (Alibaba ×2 distinct units, OPPO, Ant, Nubank, Amazon AGI, NVIDIA, Salesforce, Meituan, Baidu, Yoolee.ai, Wantedly), **1 industry lab as co-author on a university-led paper**.

**The industrial papers cluster in exactly two places**: **RL / agent post-training at scale** (Amazon AGI, NVIDIA, Salesforce, Yoolee.ai, Baidu, Meituan via the sibling) and **recommendation with production numbers** (Alibaba ×2, Ant, OPPO, Wantedly). **The games lane remains university-led** — CAS+Baidu on GameGo is the sole industry-adjacent case, with Baidu as a co-author rather than the deployment setting.

## 6. Follow-Up Actions

| # | Action | Priority | Status |
|---|---|---|---|
| 1 | **Coordinate same-day runs.** Two same-day reports collided on 9/23 IDs (§5.2); the 10-07 run logged the same problem. Either serialize same-day synthesis jobs, or adopt a shared "claimed IDs" lock file written before drafting and re-checked immediately before commit. **A dedup claim scoped to visible siblings is structurally unsafe.** | **high** | proposed |
| 2 | **Add acronym/title-level dedup as a mandatory step.** `MASBench` (§2.1) is the fourth name collision in five days; ID-only dedup missed all four. | **high** | proposed |
| 3 | **Switch the next `arxiv-ai-search` run to ID-range enumeration of the fresh window**, demoting keyword queries to a separately-labelled backfill section — implementing the 10-06 recommendation this run violated (§5.1). | **high** | proposed |
| 4 | Promote the §5.4 OPD convergence to a **claim page**: *"In on-policy distillation, target construction is the primary design axis, teacher selection secondary"* — 2 sources, same-day, mutually uncited, independently found by two runs. | medium | proposed |
| 5 | Correct the 2026-09-05 conference digest's `MASBENCH` entry to disambiguate it from [`2610.04672`](https://arxiv.org/abs/2610.04672). | medium | proposed |
| 6 | Fix the `abst:planning` typo in query 8 before reuse, and **audit the standing query set for other silently-malformed field names** (§1.1 — arXiv returns a healthy hit count either way). | medium | proposed |
| 7 | Consider an **entity page for Nubank** (2 unrelated papers) and for **Alibaba** (now 2 distinct units across 2 papers plus prior entries). | low | proposed |
| 8 | Track the §5.4 cautionary-result ratio over the next 3 runs; if it holds near 17%, spin out a synthesis page. | low | proposed |

## 7. Method Disclosure

- **Channel**: arXiv export API, Atom XML, `curl -sG --data-urlencode`, sequential, 6 s between calls; `arxiv.org/html/<id>v1` for affiliations at 1 s spacing, 25 s per-file timeout.
- **Affiliations**: 23/23 recovered from `ltx_authors` / `ltx_role_affiliation` blocks, falling back to author `thanks` footnotes (`2610.03033`, `2610.09120`, `2610.10411`) and `ltx_creator` email domains (`2610.10120`, `2609.01652`, `2610.10087`) where affiliation spans were absent. **No affiliation in this report is inferred from an author's known prior affiliation.**
- **Dedup, two passes**: (i) every shortlisted ID regex-checked against `wiki/**/*.md` for `\b\d{4}\.\d{4,5}\b` before the first write; (ii) **re-checked after `arxiv-paper-check.md` landed, which surfaced the 9-ID race in §2.3** — the 9 were removed and 9 replacements verified 0-hit *after* the sibling existed; (iii) acronym-level title grep on all 23 featured names (produced §2.1).
- **Backfill policy**: 5 `2602`–`2609` IDs admitted because they carry the only production / field-experiment evidence retrieved (§5.3) or an unduplicated causal diagnosis (PATH).
- **Defects disclosed**: query-8 field typo; unbounded keyword queries (§1.1); HTML endpoint timeout at 3 s spacing (§1.2); **the 9-ID sibling race (§2.3)**.
- **Temp**: all scratch under `/var/folders/.../T/opencode/arxiv-ai-search-20261008/`, removed after writing. No writes outside that directory and the wiki.
