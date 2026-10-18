---
title: "arXiv AI Search 2026-10-18 — LLM Agents Keep Absorbing Recsys; TransX/WeGR/Lazada Ship Industrial Sequence-Transduction Gains; Explicit CTR Papers Still Absent"
type: synthesis
created: 2026-10-18
updated: 2026-10-18
sources: [arxiv-org-listing, arxiv-abs-pages, arxiv-export-api, web-search]
tags: [arxiv, listing-harvest, recommendation, generative-recommendation, semantic-ids, sequential-modeling, sequence-transduction, ctr, advertising, multi-agent, memory-agents, agent-memory, long-context, data-curation, honesty-alignment, moe, personalization, quantization, data-strategy, survey, games, llm-game-playing, game-master]
---

# arXiv AI Search 2026-10-18 — the industrial recsys stack keeps scaling out

> **Sunday run over the Friday 2026-10-16 block** (arXiv posts no weekend announcements). The export API again returned **`Rate exceeded.`** on the first burst (same wall the 10-15/10-16/10-17 runs logged), so this harvest combines: one successful API query (`cat:cs.CL AND "large language model"`, 20 entries with full abstracts), the **`/list/cs.{CL,IR}/recent` listing pages**, per-paper **`abs` pages**, and a targeted web search for the games lane. **20 papers** are featured below across the requested lanes (AI / LLMs / recommendation / advertising / sequential modeling / CTR / games). **5 are new-to-wiki**; 15 were already filed by sibling reports (cross-refs in §4).
>
> **Three threads run through the harvest.**
>
> **① Industrial recommendation is now a full-stack "sequence-transduction" engineering discipline — and it reports A/B numbers.** [`2610.20913`](https://arxiv.org/abs/2610.20913) (**TransX**) decomposes encoding / behavior memory / candidate-conditioned fusion into independently scalable components, disaggregates prefill vs. online prediction, and reports production **CTR +6.02% / CVR +4.45%** at **~80% lower serving cost** vs a colocated HSTU-style baseline (~5× per-request FLOPs at equal cost). WeChat's [`2610.16979`](https://arxiv.org/abs/2610.16979) (**WeGR**) pairs a collaborative-signal Semantic-ID tokenizer with progressively-horizon RL, reporting **orders +2.54% / CTR +1.51%** and **−25% CPU/GPU** in a two-month live A/B. Lazada's [`2610.16132`](https://arxiv.org/abs/2610.16132) (**UniSGR-V2/TacGR**) reconstructs continuous target-side features *inside* decoding, reporting online **GMV +3.09% / Orders +5.55%**. The lane is no longer "propose an architecture" — it is **architecture + training-throughput + serving-cost co-design with online A/B proof**. See §4.A.
>
> **② On the LLM side, memory and workspace curation absorb more of the recsys-style "what to store / what to surface" problem.** [`2610.22273`](https://arxiv.org/abs/2610.22273) (**Librarian Agents**, Finn/Kumar group) trains an RL *builder* agent to pre-organize corpora into hierarchical workspaces that **anticipate future queries** (+33 pts BrowseComp-Plus over retrieval baselines). [`2610.21900`](https://arxiv.org/abs/2610.21900) (**TEM**) versions facts temporally and beats session-aware RAG at ~half the evidence tokens. [`2610.16137`](https://arxiv.org/abs/2610.16137) (**ReMind**, already on file) reranks memories *recurrently* with compound cueing + a sufficiency stopper. The retrieval/ranking machinery of RecSys is migrating into the agent-memory stack paper by paper. See §4.B.
>
> **③ Explicit CTR-prediction papers remain absent — again.** Despite TransX and WeGR reporting live CTR deltas, **no pure CTR-model paper** (feature interaction, CTR scaling laws, etc.) surfaced in this window — consistent with the empty-CTR pattern the 10-15/10-16/10-17 runs documented. The only explicit advertising-systems paper is [`2610.19454`](https://arxiv.org/abs/2610.19454) (**AdCoEvo**), a co-evolving multi-agent *delivery-operations* system (advertiser value +14.02% vs rule baseline) — automation of the ops loop, not of the click model. See §4.A (item 9).

## 1. Search Metadata

| Field | Value |
|---|---|
| **Date of search** | 2026-10-18 (Sunday) |
| **Search channel** | Export API (partially throttled) + `arxiv.org/list/{cs.CL,cs.IR}/recent` + per-paper `abs` pages + web search (games lane) |
| **Window covered** | Fri **2026-10-16** announcement block (fresh; no weekend block), Thu 10-15, Wed 10-14, plus one v2 revision from 10-14 (SAGE) |
| **Queries issued** | API: LLM (`cs.CL AND "large language model"`, success, 20 entries), cs.IR / CTR / sequential / games (all `Rate exceeded.`); listing: `cs.CL/recent` (50 of 177 on 10-16), `cs.IR/recent` (118 total, 14 on 10-16); web: "game AI LLM agents" (SAGE v2, CriticaLLM found) |
| **Rate limiting** | Export API: 5 consecutive `Rate exceeded.` / empty responses on parallel burst; succeeded once after 60 s cooldown. Listing pages and `abs` pages: no throttle. |
| **Featured, final** | **20** (5 LLM core + 8 Rec/Ads/Sequential/CTR-adjacent + 2 Games + 5 already-on-file cross-references consolidated into lanes) |
| **Dedup** | Grep against all arXiv IDs in `wiki/**/*.md`: **5 new** (`2610.22324`, `2610.22273`, `2610.22292`, `2610.21900`, `2610.21681`) / **15 already on file** (cross-referenced in §4) |
| **Affiliation honesty** | arXiv `abs` pages carry **no affiliation fields**. Affiliations below are either stated inside abstracts (WeChat, Lazada), linked orgs (code/model URLs), author-lineage inferences marked **(inferred)**, or **"not listed"**. No affiliation is asserted as verified. |
| **Temp artifacts** | `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv_*.xml` (authorized scratch), deleted after this write-up |

## 2. Master Table

| # | Paper | arXiv | Submitted | Institution | Lane | New? | Headline |
|---|---|---|---|---|---|---|---|
| 1 | TransX: Scaling Sequence Transduction for Recommendation | [2610.20913](https://arxiv.org/abs/2610.20913) | 10-14 | not listed (HSTU-lineage authors, **inferred** industry lab) | Rec / CTR production | on file (`conference-digest` 10-16) | prod **CTR +6.02%**, CVR +4.45%, serving cost −80% |
| 2 | WeGR: Unified Generative Retrieval in WeChat | [2610.16979](https://arxiv.org/abs/2610.16979) | 10-12 | **WeChat / Tencent** (stated) | Rec / generative retrieval | on file (10-15/10-17 paper-checks) | 2-mo A/B: **orders +2.54%**, CTR +1.51%, CPU/GPU −25% |
| 3 | UniSGR-V2 (TacGR): Target-Side Feature Anticipation | [2610.16132](https://arxiv.org/abs/2610.16132) | 10-12 | **Lazada** (stated via dataset) | Rec / generative rec | on file (10-17 paper-check) | online A/B: **GMV +3.09%**, Orders +5.55% |
| 4 | Personalized LLM Rec with Semantic IDs: Beam Search vs MTP | [2610.15864](https://arxiv.org/abs/2610.15864) | 10-11 | streaming-industry, not listed (Netflix+Microsoft authors, **inferred**) | Rec / LLM semantic IDs | on file (10-17 paper-check) | beam search beats MTP; cold-start **+77%** |
| 5 | HASTE: Hierarchical Supervision for Generative Rec | [2610.17368](https://arxiv.org/abs/2610.17368) | 10-12 | not listed (retail coauthors, **inferred**) | Rec / semantic IDs | on file (10-15 paper-check) | hierarchical loss: **2× faster convergence** |
| 6 | RecSoup: Model Merging for Multi-Objective Rec | [2610.21220](https://arxiv.org/abs/2610.21220) | 10-15 | not listed | Rec / multi-objective | on file (10-16 digest) | **165–228×** faster than param-generation; CIKM 2026 |
| 7 | OT-FlowRec: OT-Guided Multi-Bridge Flow for Multimodal Seq. Rec | [2610.16038](https://arxiv.org/abs/2610.16038) | 10-12 | not listed (single author) | Sequential rec | on file (10-16 paper-check) | parallel interest-specific transport flows, no mode collapse |
| 8 | Popularity Bias Mitigation in Sequential Rec (Sparse Prior) | [2610.17823](https://arxiv.org/abs/2610.17823) | 10-11 | not listed (Noah's Ark-affiliated authors, **inferred**) | Sequential rec | on file (10-15 dailies) | sparse prior-regularized objective *(abstract not retrieved this run)* |
| 9 | AdCoEvo: Co-Evolving Multi-Agent Advertising Delivery | [2610.19454](https://arxiv.org/abs/2610.19454) | 10-14 | not listed (ICT-CAS lineage, **inferred**) | Ads / multi-agent | on file (10-15 ai-search) | advertiser value **+14.02%** vs rules; CPA −7.07% |
| 10 | Librarian Agents: Curating Workspaces that Anticipate Queries | [2610.22273](https://arxiv.org/abs/2610.22273) | 10-15 | Stanford (Finn/Kumar group, **inferred**) | LLM / long-context curation | **NEW** | RL builder: **+33 pts** BrowseComp-Plus, +31 zero-shot BRIGHT |
| 11 | TEM: Temporal State Tracking Memory for LLM Agents | [2610.21900](https://arxiv.org/abs/2610.21900) | 10-15 | not listed | LLM / agent memory | **NEW** | versioned facts; beats session-RAG with **~50% fewer tokens** |
| 12 | Training Reasoning Models to Generate Diverse Scientific Ideas | [2610.22324](https://arxiv.org/abs/2610.22324) | 10-15 | not listed (Salesforce-lineage author, **inferred**) | LLM / RL ideation | **NEW** | set-level RL; 8B beats Claude Opus 4.8 & GPT-6 Astra on creative utility |
| 13 | CATCH: Continuous Adversarial Training for LLM Honesty | [2610.22292](https://arxiv.org/abs/2610.22292) | 10-15 | not listed (Mila-lineage authors, **inferred**) | LLM / alignment | **NEW** | hundreds of targets → transferable honesty, utility preserved |
| 14 | Data Strategies for LLMs: Training-Lifecycle Survey | [2610.21681](https://arxiv.org/abs/2610.21681) | 10-15 | not listed | LLM / data strategy | **NEW** | unified policy framing of selection/weighting/scheduling |
| 15 | MLExpert: Generalist Agentic Model for ML Engineering | [2610.22344](https://arxiv.org/abs/2610.22344) | 10-15 | **InternScience** (code/model links) | LLM / agents | on file (10-17/18 paper-checks) | MLE-Bench Lite medal rate **37.9%→72.7%** (35B MoE) |
| 16 | MoE Experts for Personalization | [2610.22127](https://arxiv.org/abs/2610.22127) | 10-15 | **University of Copenhagen** (lineage) | Rec × LLM interpretability | on file (10-17 ai-search) | crosscoders localize personalization experts in MoE |
| 17 | N-Gram Memories at Two Bits (Conditional Program) | [2610.21810](https://arxiv.org/abs/2610.21810) | 10-15 | not listed | LLM / efficiency | on file (10-18 paper-check) | 2-bit trellis codes: DeepSeek table **203GB→51GB** |
| 18 | Grid-Bench: Predicting How Discrete Worlds Change | [2610.22312](https://arxiv.org/abs/2610.22312) | 10-15 | UCLA-affiliated authors (**inferred**) | LLM / world modeling | on file (10-17/18) | executable grid-state benchmark, 8 op families |
| 19 | SAGE: Structured Strategic Reasoning for LLM Game Playing | [2609.34342v2](https://arxiv.org/abs/2609.34342) | v2 10-14 | not listed | Games / LLM agents | on file (09-30 game-rl-daily) | anchor–adapt–recalibrate: **+127.6%** payoff (Liar's Dice), −80/90% tokens |
| 20 | CriticaLLM: Autonomous Game Master for TTRPGs | [2610.21525](https://arxiv.org/abs/2610.21525) | 10-15 | **UCLouvain** (via alphaXiv, tentative) | Games / LLM GM | on file (10-16/17 game-rl-dailies) | fully automated GM evaluated with real TTRPG players |

**CTR lane result: 0 explicit CTR-prediction papers** (6th consecutive empty October window). CTR improvements appear only as *reported outcomes* inside industrial recsys papers (TransX, WeGR).

## 3. New-to-Wiki Spotlight (5)

| Paper | arXiv | Why it stands out |
|---|---|---|
| Librarian Agents | [2610.22273](https://arxiv.org/abs/2610.22273) | reframes long-context handling as **anticipatory workspace construction** optimized by RL against downstream QA accuracy — retrieval is reactive; curation can be proactive |
| TEM | [2610.21900](https://arxiv.org/abs/2610.21900) | training-free **versioned fact memory** with explicit temporal labels; +17–56 pts hit rate from historical labeling alone |
| Diverse Scientific Ideation | [2610.22324](https://arxiv.org/abs/2610.22324) | **set-level RL** where each idea's reward is weighted by distance from previous ideas — quality *and* diversity in one objective |
| CATCH | [2610.22292](https://arxiv.org/abs/2610.22292) | adversarial training (hundreds of targets) learns honesty that **transfers across benchmarks** and survives multi-agent deception pressure |
| Data Strategies Survey | [2610.21681](https://arxiv.org/abs/2610.21681) | unifies pretraining/post-training data selection as **budget-allocation policies** over examples, organized by granularity × model-dependence × temporal adaptivity |

## 4. Per-Paper Detail

### Lane A — Recommendation / CTR / Advertising / Sequential Modeling (9)

---

#### 1. TransX Technical Report: Scaling Sequence Transduction for Recommendation

- **arXiv**: [`2610.20913`](https://arxiv.org/abs/2610.20913) · cs.IR · 14 Oct 2026
- **Authors**: Da Xu, Liyan Fang, Divya Venugopalan, Sunny Hsu, Xukai Wang, Rishav Roy Chowdhury, Cindy Liang, Nishant Satya Lakshmikanth
- **Institution**: not listed on arXiv. Author overlap with the HSTU line of work suggests an industry lab (**inferred**, tentative).
- **Abstract (condensed)**: a sequence-transduction framework + co-designed infrastructure for industrial recommendation with explicit control over model-compute allocation. Components — sequence encoding, behavior memory, candidate-conditioned fusion — scale independently; training amortizes causal trajectory computation across behavioral prefixes; serving disaggregates bulk prefill, nearline refresh, and online prediction via compact behavior-memory KV. Reports **anisotropic scaling returns**: encoder scaling saturates beyond moderate depth; more supervision shifts capacity toward fusion; needed memory resolution stays roughly stable as models grow.
- **Key innovations**:
  - Disaggregated serving (prefill / nearline / online) with a compact behavior-memory KV: **~80% total serving-cost reduction** vs colocated serving; enables **~5× per-request FLOPs** of an HSTU-style baseline at equal cost; **~4× throughput per H200** at matched FLOPs.
  - Production A/B: core model **CTR +6.02%, conversion +4.45%**; post-trained retrieval / preference-ranking variants +2.96% / +1.33% CTR.
  - Training infrastructure: **+84% supervised-target throughput**.
- **Why it matters**: the strongest public evidence yet that online serving cost need not scale proportionally with rec-model capacity — the scaling laws of recsys are *systems* laws, not just architecture laws.

---

#### 2. WeGR: Unified Generative Retrieval for Industrial Search Systems in WeChat

- **arXiv**: [`2610.16979`](https://arxiv.org/abs/2610.16979) · cs.IR · 12 Oct 2026
- **Authors**: Jiajun Han, Guoxin Ma, Felix, Liangsheng Xu, Ruiqi Yu, Yingdi Guo, Zongbing Wang, Xinhua Ye, Chenyan Hua, Xin Xie, Pengcheng Yang, Haijun Wu
- **Institution**: **WeChat / Tencent** (stated in title and abstract).
- **Abstract (condensed)**: generative retrieval (GR) is promising for industrial search but suffers from (i) Semantic-ID tokenizers that fail to incorporate collaborative signals without codebook collapse, and (ii) RL with sparse rewards under exact SID matching. WeGR adds **CoCo-VAE** (Collaborative and Collapse-free Tokenizer: query-to-item + item-to-item signals, codebook refresh, complementary regularization) and **DHPO** (Dynamic Horizon Policy Optimization: progressively expands reward-evaluation and policy horizons across the SID hierarchy, no auxiliary reward model).
- **Key innovations**:
  - Collaborative-signal SIDs without codebook collapse.
  - Hierarchical, progressively-horizon RL for sparse SID-matching rewards.
  - Two-month online A/B in WeChat E-commerce Search: **orders +2.539%, CTR +1.508%, conversion +1.381%**, CPU −25.5% / GPU −26.1%; deployed at billion-user scale, tens of millions of PVs daily.
- **Why it matters**: generative retrieval is production-ready when tokenizer design and RL reward horizon are co-designed — and it *reduces* serving cost while improving ranking.

---

#### 3. UniSGR-V2: Stepwise Target-Side Feature Anticipation and Crossing for Generative Recommendation (TacGR)

- **arXiv**: [`2610.16132`](https://arxiv.org/abs/2610.16132) · cs.IR · 12 Oct 2026
- **Authors**: Jun Yang, Jiasi Chen, Jiawei Sun, Ziyue Guo, Jianan Yan, Tao Luo, Xiaoyi Zeng
- **Institution**: **Lazada** (stated via the large-scale Lazada dataset; Alibaba SEA).
- **Abstract (condensed)**: Semantic-ID generative recommendation compresses item attributes into a finite codebook and cannot look up target-side features during decoding — a "target-side feature vacuum" that raises conditional entropy and cascades errors. TacGR **anticipates a continuous target-side feature vector before decoding each codeword** and crosses it with the semantic prefix and user sequence inside the decoder; the crossed representation both conditions generation and serves ranking.
- **Key innovations**:
  - Continuous target-side feature anticipation + in-decoder feature crossing.
  - Semantic-anchoring auxiliary tower (anti-collapse) and unidirectional visibility mask (anti noise-propagation).
  - Gated convolutional denoising + pyramid memory funnel for extremely long industrial behavior histories.
  - Offline gains over OneRec/UniRec/UniSGR; online A/B: **IPV +0.79%, Orders +5.55%, GMV +3.09%**.
- **Why it matters**: closes the last structural gap between discriminative and generative recommenders — target-side features *inside* autoregressive decoding.

---

#### 4. Personalized LLM Recommendation with Semantic IDs: Autoregressive Beam Search vs. Multi-Token Prediction

- **arXiv**: [`2610.15864`](https://arxiv.org/abs/2610.15864) · cs.IR · 11 Oct 2026 · NeurIPS 2026 PALM Workshop
- **Authors**: Sejoon Oh, Fernando Amat Gil, Evan Smothers, Dan Iter, Mark Thornburg, Dawit Mureja Argaw, Sourabh Medapati, Thea Wang, Ria Verma, Qiuling Xu, Harshit Syal, Ehsan Gholami, Moumita Bhattacharya, Ashish Rastogi
- **Institution**: not listed; streaming-media catalog + author lines suggest **Netflix × Microsoft** collaboration (**inferred**, tentative).
- **Abstract (condensed)**: industry-scale apples-to-apples comparison of single-head autoregressive SID decoding (constrained beam search) vs multi-token prediction (MTP) inside a multi-task LLM doing personalized retrieval, content QA, and instruction following over a large streaming catalog. New auxiliary ranking loss over the joint SID score trains the MTP objective.
- **Key innovations**:
  - Beam search **consistently beats MTP** on product-critical metrics (ranking, content QA) and trains at **~2.6× lower dollar cost** (Qwen3-8B scale); MTP wins only raw inference throughput.
  - End-to-end vs previous non-SID baseline: **+77% item cold-start ranking, +22% content-QA accuracy, +2.8× faster training**; language regression from SID vocabulary growth fixed by RL post-training.
- **Why it matters**: a rare negative-ish result for the MTP fashion at industrial scale — decode-paradigm choice in SID generation is an empirical product trade-off, not a settled design.

---

#### 5. HASTE: Hierarchical and Attribute-aware Supervision for Generative Recommendation

- **arXiv**: [`2610.17368`](https://arxiv.org/abs/2610.17368) · cs.IR · 12 Oct 2026
- **Authors**: Tripti Shukla, Shwetha Somasundaram, Akshat Gupta, Rohit Garg, Paul Duff, Ian Anderson
- **Institution**: not listed (retail/fashion-industry coauthor lineage, **inferred**).
- **Abstract (condensed)**: standard causal cross-entropy under-uses the hierarchical structure of Semantic IDs and leaves tail items under-trained. HASTE adds **Hierarchical Loss** (supervision at each SID level) and **Attribute-Specific Losses** (preserve fine-grained attributes via the LM's semantic knowledge).
- **Key innovations**: hierarchical loss → **~2× faster convergence**; attribute losses improve long-tail representations; gains across fashion benchmark and multi-domain Amazon datasets.
- **Why it matters**: training-efficiency and tail-quality gains from exploiting SID structure for free — no architecture change.

---

#### 6. RecSoup: Efficient Model Merging Approach for Controllable Multi-Objective Recommendation

- **arXiv**: [`2610.21220`](https://arxiv.org/abs/2610.21220) · cs.IR · 15 Oct 2026 · CIKM 2026
- **Authors**: Zidong Jia, Guofu Xie, Xiao Zhang
- **Institution**: not listed.
- **Abstract (condensed)**: Controllable Multi-Objective Recommendation (CMOR) wants inference-time trade-off control without retraining. RecSoup is a two-stage lightweight approach: prune parameters with a joint objective-importance × cross-objective-relevance criterion, then **adaptive merging via a learnable preference-to-coefficient mapping**.
- **Key innovations**: provably navigates the full Pareto front without smoothness constraints; **165–228× faster** inference-time control than parameter-generation CMOR; no joint retraining.
- **Why it matters**: model merging as the cheap CMOR substrate — control at merge-coefficient granularity instead of reranking or generative modules.

---

#### 7. OT-FlowRec: Optimal Transport-Guided Multi-Bridge Flow for Multimodal Sequential Recommendation

- **arXiv**: [`2610.16038`](https://arxiv.org/abs/2610.16038) · cs.IR · 12 Oct 2026
- **Authors**: Miao Sun (single author)
- **Institution**: not listed.
- **Abstract (condensed)**: e-commerce session preferences are concurrent and multi-centric; global attention collapses them into a unimodal average. OT-FlowRec builds a **mixture of parallel interest-specific transport flows**, each preserving one interest cluster via an OT plan, with geometric minimum-cost paths to target preference prototypes and a progressive time-sampling warmup aligning continuous flow matching to top-k ranking.
- **Key innovations**: explicit multi-interest disentanglement via OT-guided flow matching; SOTA gains on three public multimodal sequential-rec datasets.
- **Why it matters**: generative sequential rec without mode collapse — multi-modality handled in the *transport*, not in heuristics.

---

#### 8. Mitigating Popularity Bias in Sequential Recommendations with Sparse Prior-Regularized Objective

- **arXiv**: [`2610.17823`](https://arxiv.org/abs/2610.17823) · cs.IR · 11 Oct 2026
- **Authors**: Anton Pembek, Anton Klenitskiy, Alexander Savchenko, Alexey Vasilev
- **Institution**: not listed (Huawei Noah's Ark-affiliated author lineage, **inferred**).
- **Abstract**: not retrieved this run (abs page fetch timed out; listed from the cs.IR recent page).
- **Key idea (from title/listing)**: sparse prior-regularized training objective to reduce popularity bias in sequential recommenders.
- **Cross-ref**: already covered by [2026-10-15/arxiv-ai-search](../2026-10-15/arxiv-ai-search.md) and [2026-10-15/arxiv-daily](../2026-10-15/arxiv-daily.md).

---

#### 9. AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System

- **arXiv**: [`2610.19454`](https://arxiv.org/abs/2610.19454) · cs.AI / cs.IR / cs.MA · 14 Oct 2026
- **Authors**: Tianzhu Hu, Hang Yu, Zeyuan Zhao, Zeyu Pan, Huan Luo, Chun Gan, Mingzhe Cao, Liubin Wang, Mingming Li, Jiao Dai, Jizhong Han, Songlin Hu
- **Institution**: not listed (ICT-CAS author lineage — Dai/Han/Hu — **inferred**, tentative).
- **Abstract (condensed)**: ad delivery ops automate individual tasks (bidding, budget allocation) but need human coordination; individual experience doesn't become reusable capability, and strategies lag market shifts. AdCoEvo connects delivery decisions across timescales via **role specialization** (planning / adjustment / diagnosis); diagnostic results feed next-period planning; parameters update from real delivery outcomes so the multi-agent system **co-evolves**.
- **Key innovations**: closed-loop co-evolution across planning–adjustment–diagnosis; vs rule-based ops: **advertiser value +14.02%, CPA −7.07%**; vs fixed-parameter multi-agent: +3.96% / −1.24%.
- **Why it matters**: the advertising lane's frontier here is *ops-loop automation with self-updating strategy*, not CTR-model architecture.

---

### Lane B — LLM Core: Agents, Memory, Alignment, Data (5 new + 3 on-file)

---

#### 10. Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries — **NEW**

- **arXiv**: [`2610.22273`](https://arxiv.org/abs/2610.22273) · cs.CL · 15 Oct 2026
- **Authors**: Anikait Singh, Teresa Zhang, Yoonho Lee, Roshen Sanjay Nair, Aviral Kumar, Chelsea Finn
- **Institution**: not listed; Finn/Kumar groups (**Stanford**, inferred).
- **Abstract (condensed)**: retrieval is reactive; knowledge graphs are rigid. Can an agent *proactively* reorganize unstructured corpora before inference to serve diverse future queries? A **builder agent** transforms raw documents into a hierarchical filesystem of synthetic files and reference links; workspace construction is an MDP optimized by RL against downstream answering accuracy.
- **Key innovations**: anticipatory directed curation as a trained capability; **+33 pts over strongest retrieval/precomputation baselines on BrowseComp-Plus**; amortizes construction cost over repeated queries; zero-shot **+31 pts average on BRIGHT**.
- **Why it matters**: recsys-flavored "index construction as learning problem" inside the LLM-agent stack — the workspace *is* the index, and it is trained end-to-end with the consumer.

---

#### 11. TEM: Temporal State Tracking Memory for Large Language Model Agents — **NEW**

- **arXiv**: [`2610.21900`](https://arxiv.org/abs/2610.21900) · cs.CL · 15 Oct 2026
- **Authors**: Pengfeng Song, Yunkai Zhuang, Liye Shi
- **Institution**: not listed.
- **Abstract (condensed)**: a new fact replaces an earlier value without making the old value irrelevant. TEM stores facts as **versioned records linked to sources**, retrieves relevant versions, orders them by source, and labels historical records before answering. Training-free.
- **Key innovations**: explicit fact versioning + temporal-status labels; key-entity hit rates **75.7–97.6%**; adding historical labels alone **+17.1–56.0 pts**; evidence compactness **48.8–56.7% fewer tokens** than session-aware RAG; beats session-aware RAG on LoCoMo by 7.9–10.6 pts under fixed budget.
- **Why it matters**: temporal structure — the sequential-modeling instinct — applied to agent memory, nearly for free.

---

#### 12. Training Reasoning Models to Generate Diverse Scientific Ideas — **NEW**

- **arXiv**: [`2610.22324`](https://arxiv.org/abs/2610.22324) · cs.CL · 15 Oct 2026
- **Authors**: Manya Wadhwa, Pranav Narayanan Venkit, Hiroaki Hayashi, Yu Li, Tuhin Chakrabarty, Chien-Sheng Wu
- **Institution**: not listed (Salesforce-lineage author, **inferred**).
- **Abstract (condensed)**: document-grounded ideation optimized for *diversity* as well as quality. In one generation the model writes K structured idea cards; the **set is scored jointly**, each idea's quality weighted by its distance from previous ideas — a set-level RL objective teaching the model to steer away from its own earlier ideas.
- **Key innovations**: set-level diversity-aware RL; trained 8B model exceeds Claude Opus 4.8 and GPT-6 Astra on contamination-free creative utility; human experts judge sets as promising as Opus 4.8's; coding-agent proof-of-concept success@k preserved (diversity doesn't cost executability).
- **Why it matters**: RL objectives can encode *set-level* product metrics (novelty), not just single-response correctness.

---

#### 13. CATCH: Continuous Adversarial Training for Transferable LLM Honesty — **NEW**

- **arXiv**: [`2610.22292`](https://arxiv.org/abs/2610.22292) · cs.CL · 15 Oct 2026
- **Authors**: Yuan-Chen Chang, Niklas Herbster, Gauthier Gidel, Tommaso Tosato
- **Institution**: not listed (Mila-lineage authors, **inferred**).
- **Abstract (condensed)**: alignment-trained LLMs still output unsupported or knowledge-contradicting claims under pressure. CATCH trains toward honest answers and away from dishonest ones with continuous adversarial training, on Llama-3.3-70B-Instruct and Qwen3-3.6-27B.
- **Key innovations**: only **hundreds of self-report targets** needed; honesty generalizes across benchmarks (MASK, Among Us multi-agent deception, AuditBench hidden-behavior discovery); beats prompting and SFT; parity with activation steering on honesty **but better utility retention** via a novel utility-data choice.
- **Why it matters**: honesty as a *robustness* property learned adversarially, not a prompt-time behavior — relevant to game/agent settings where deception is rewarded.

---

#### 14. Data Strategies for Large Language Models: A Unified Perspective on the Training Lifecycle — **NEW**

- **arXiv**: [`2610.21681`](https://arxiv.org/abs/2610.21681) · cs.CL · 15 Oct 2026
- **Authors**: Yuanjian Xu, Jianing Hao, Tianze Sun, Yongyao Duan, Sam Chen, Jinyi Han, Wanbo Zhang, Yuxuan Sun, Guang Zhang, Zhong Li
- **Institution**: not listed.
- **Abstract (condensed)**: survey unifying data strategy across pretraining and post-training as **policies allocating a training budget over candidate examples**; high-quality data = high *training-dependent* utility (depends on objective, model, and training state). Methods organized by decision granularity, model dependence, temporal adaptivity; compares compute costs and empirical support.
- **Key takeaways**: fine-grained/state-dependent policies give control but add scoring/search/rollout cost; cross-scale transfer of data policies remains under-evidenced. Living paper list at `github.com/xuyj233/data_strategy_survey`.
- **Why it matters**: the vocabulary unification this fast-moving area lacked — useful scaffolding for wiki [[data-strategy]]-type pages.

---

#### 15–18. Already on file (condensed cross-references)

| Paper | arXiv | Already covered in | One-line note |
|---|---|---|---|
| MLExpert | [2610.22344](https://arxiv.org/abs/2610.22344) | [10-18/arxiv-paper-check](../2026-10-18/arxiv-paper-check.md), [10-17/arxiv-daily](../2026-10-17/arxiv-daily.md) | 35B MoE agentic MLE model; WIRL windowed RL; MLE-Bench Lite medal rate 37.9%→72.7% |
| MoE Experts for Personalization | [2610.22127](https://arxiv.org/abs/2610.22127) | [10-17/arxiv-ai-search](../2026-10-17/arxiv-ai-search.md) §Lane A-2 | crosscoders localize personalization latents → causal expert boosting |
| N-Gram Memories at Two Bits | [2610.21810](https://arxiv.org/abs/2610.21810) | [10-18/arxiv-paper-check](../2026-10-18/arxiv-paper-check.md) | Gaussian-trellis 2-bit row codes; 41–63% lower output KL; DeepSeek table 203GB→51GB |
| Grid-Bench | [2610.22312](https://arxiv.org/abs/2610.22312) | [10-17/arxiv-daily](../2026-10-17/arxiv-daily.md), [10-18/arxiv-paper-check](../2026-10-18/arxiv-paper-check.md) | executable discrete-world state-prediction benchmark for LLMs |
| Hy-Memory-30B-A3B | [2610.22196](https://arxiv.org/abs/2610.22196) | [10-17/arxiv-ai-search](../2026-10-17/arxiv-ai-search.md) | Tencent memory writer; OPD+GRPO; 55.49% vs Claude Opus 5 54.62% — sibling of TEM's problem space |

### Lane C — Games (2, both on file)

---

#### 19. SAGE: Structured Strategic Reasoning for Efficient LLM Game Playing

- **arXiv**: [`2609.34342v2`](https://arxiv.org/abs/2609.34342) · cs.AI · v1 28 Sep, **v2 14 Oct 2026**
- **Authors**: Zhiwei Chen, Tianchun Wang, Zhongtao Rao, Haiming Zhu, Ding Cao, Tianxiang Zhao
- **Institution**: not listed.
- **Abstract (condensed)**: free-form strategic reasoning yields unsupported assumptions, inconsistent opponent estimates, and noise from irrelevant history. SAGE is training-free, structured around **anchor–adapt–recalibrate**: anchor to an equilibrium policy (strategically valid prior); condition deviations on a soft belief over opponent tendencies; distill past interactions into counterfactual hypotheses that recalibrate reasoning.
- **Key innovations**: up to **+127.6% payoff** vs Suspicion-Agent/ReTA/Agent-Pro/EMO/Hypothetical Minds in Liar's Dice while cutting input/output tokens by **up to 80%/90%**; non-negative mean payoff vs 5/10, 8/10, 8/10 opponents in Leduc Hold'em, Liar's Dice, Goofspiel.
- **Why it matters**: equilibrium priors + opponent beliefs as *structured, token-cheap* complements to raw reasoning-token scaling in imperfect-information games.
- **Cross-ref**: [2026-09-30/game-rl-daily](../2026-09-30/game-rl-daily.md).

---

#### 20. CriticaLLM: Using LLMs as Autonomous Game Master for Tabletop Role-Playing Games

- **arXiv**: [`2610.21525`](https://arxiv.org/abs/2610.21525) · cs.AI · 15 Oct 2026
- **Authors**: Gaëtan Berlaimont, Justin Vanwichelen, Benoît Ronval, Hélène Verhaeghe
- **Institution**: **UCLouvain** (via alphaXiv metadata, tentative).
- **Abstract (condensed)**: TTRPGs like D&D require story craft, rule adherence, and player freedom simultaneously. CriticaLLM is a fully automated Game Master framework covering story creation, exploration, and combat phases; evaluated with actual TTRPG players; plot/antagonist diversity examined across four LLMs of varying sizes.
- **Key innovations**: end-to-end GM loop (not just combat or dialogue); human-player evaluation protocol; cross-size diversity analysis.
- **Why it matters**: the games lane's other pole beyond strategic play — *facilitative* game AI — is getting proper human-subject evaluation.
- **Cross-ref**: [2026-10-16/game-rl-daily](../2026-10-16/game-rl-daily.md), [2026-10-17/game-rl-daily](../2026-10-17/game-rl-daily.md).

## 5. Trend Notes

1. **Industrial recsys = systems papers with A/B receipts.** TransX, WeGR, and UniSGR-V2 all lead with serving-cost/throughput engineering and close with online A/B deltas in the 1–6% range on CTR/orders/GMV. The architecture-only paper is disappearing from the top of the lane.
2. **Semantic IDs are the shared substrate.** WeGR (CoCo-VAE tokenizer), HASTE (hierarchical + attribute losses), UniSGR-V2 (target-side continuous features over SIDs), and the Microsoft×Netflix SID comparison all assume autoregressive item generation over discrete hierarchical codes. Open questions narrowing fast: tokenizer collaboration-signal injection, decode paradigm (beam vs MTP — beam currently winning at industrial scale), and where continuous features re-enter.
3. **The "memory/ranking" toolkit is being ported into LLM agents.** TEM (versioned temporal facts), ReMind (recurrent reranking with sufficiency stopping), Librarian Agents (RL-trained anticipatory curation) — all apply RecSys primitives (ranking loops, index construction, freshness/versioning) to agent context management.
4. **Explicit CTR modeling is a research vacuum; CTR is a deployment metric.** 6th consecutive empty window for CTR-architecture papers. The live CTR numbers now arrive embedded in sequence-transduction / generative-retrieval systems reports.
5. **Ads = multi-agent ops automation** (AdCoEvo's plan–adjust–diagnose co-evolution), not bid-model innovation, in this window.
6. **Games lane splits** between token-efficient strategic reasoning with structured priors (SAGE) and facilitative/evaluative LLM game masters with human studies (CriticaLLM).

## 6. Operational Notes

- **Export API rate limits** remain the binding constraint (same wall as 10-15/16/17): parallel bursts → `Rate exceeded.`; single query after ~60 s cooldown succeeds. Listing pages + `abs` pages are the robust fallback; web search recovered the games lane when both API and search-UI timed out.
- **Affiliation recovery** this run is weaker than the 10-17 run (which used LaTeXML author blocks): abstracts state affiliations only for WeChat and Lazada; others are author-lineage inferences explicitly marked **(inferred)** or left as "not listed". A future run should restore `arxiv.org/html/{id}v1` author-block parsing.
- **Temp files**: `arxiv_llm.xml` (48 KB, successful API response), listing/abs fetch scratch — all under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/`, removed after this write-up.
