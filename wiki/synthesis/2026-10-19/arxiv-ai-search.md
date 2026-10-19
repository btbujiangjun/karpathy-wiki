---
title: "arXiv AI Search 2026-10-19 — First Full-Abstract Export-API Harvest of the Fresh 10-16 Block: 22 New-to-Wiki Papers; CTR Lane Empty Again; LLM Lane Turns to Measurement Critique"
type: synthesis
created: 2026-10-19
updated: 2026-10-19
sources: [arxiv-export-api, wiki-index-dedup]
tags: [arxiv, export-api, recommendation, generative-recommendation, semantic-ids, sequential-modeling, ctr, advertising, agentic-retrieval, agents, agent-memory, llm-routing, evaluation, measurement, alignment, diffusion-lm, transformers, interpretability, games, multi-agent, agent-safety, game-evaluation, daily-digest]
---

# arXiv AI Search 2026-10-19 — the fresh block, with abstracts attached

> **Monday run.** arXiv posts no weekend announcements, so the newest announced block is still **Friday 2026-10-16** (the Monday 10-19 block had not appeared at search time). Unlike the throttled 10-15/16/17/18 runs — which fell back to listing pages and `abs` fetches — this harvest **succeeded on the Export API itself**: 8 paced queries (15–20 s apart) returned **191 unique papers with full abstracts**, covering cs.CL, cs.LG, cs.IR, `abs:"recommender system"`, `abs:"click-through rate"`, `abs:advertising`, `abs:"sequential recommendation"`, and `cat:cs.AI AND abs:game`, back to 2026-07-21 with the dense core in 10-13…10-16.
>
> **Dedup vs the wiki: 22 of the papers below are new-to-wiki** (every ID grep-verified at 0 hits across `wiki/**/*.md`), 16 of them carried at full detail. **Three threads run through the fresh block.**
>
> **① The LLM lane's fresh block is a measurement-critique block.** Five of the ten new LLM papers attack the *instrument*, not the model: [`2610.23257`](https://arxiv.org/abs/2610.23257) shows CoT-controllability scores are an artifact of *where* the constraint is stated (self-instruction inside the CoT works far better than a user-prompt constraint — and can be turned into monitor evasion); [`2610.22244`](https://arxiv.org/abs/2610.22244) shows agent-guard verdicts shift under *pure translation* of the user request (up to +4.4 pp flip rate on Amharic for guards <13B) while English paraphrase moves them less; [`2610.22187`](https://arxiv.org/abs/2610.22187) shows LLM text-scoring moves ~0.10 normalized and re-categorizes ~20% of texts when you change the rating scale design; [`2610.22779`](https://arxiv.org/abs/2610.22779) proposes a pressure ratio + falsifiable probes for *whether a verifier is even engaged* by an agent's search; [`2610.22249`](https://arxiv.org/abs/2610.22249) separates *correctness* from *appropriateness* for a Mandarin construction. The lane is asking "does this metric measure?" at scale.
>
> **② Recommendation/ads keeps shipping A/B receipts; the one genuinely new rec paper is a learned-sparse one.** [`2610.23510`](https://arxiv.org/abs/2610.23510) (**LSNR**, SIGIR-AP 2026) encodes news articles independently and attention-weights them into a sparse user vector — beating STAR while serving from an index **an order of magnitude smaller** than an uncompressed dense baseline. The industrial receipts in-window continue to come from on-file papers: **TransX** (prod CTR +6.02%, serving cost −80%), **WeGR** (orders +2.54%, CPU/GPU −25%), and **CASI** (Shapley set-credit for agentic sponsored-search retrieval → **+3.51% advertiser value in a 7-day 10% production A/B**). **Explicit CTR-model papers: 0 again — the 7th consecutive empty October window**; CTR appears only as a reported outcome.
>
> **③ Games: the frontier questions moved from win rates to *adaptability, consensus, and verification*.** [`2610.22882`](https://arxiv.org/abs/2610.22882) finds production LLMs contribute a nearly *fixed* share in a collective-risk dilemma regardless of risk — "cooperative self-play alone is not evidence of strategic adaptability"; [`2610.20200`](https://arxiv.org/abs/2610.20200) shows consensus under competing payoffs is driven as much by network design as by model traits (ChatGPT 5.6-sol consents even with no channel, clustered graphs suppress consensus regardless); [`2610.19422`](https://arxiv.org/abs/2610.19422) co-evolves attacker/defender agents for tool-use safety; [`2610.17895`](https://arxiv.org/abs/2610.17895) (**Interaction-as-a-Judge**, UCLA×Berkeley) makes computer-use agents *operate* the generated app/game as the reward signal.

## 1. Search Metadata

| Field | Value |
|---|---|
| **Date of search** | 2026-10-19 (Monday) |
| **Search channel** | arXiv **Export API** (`export.arxiv.org/api/query`), paced sequential requests — full Atom XML with abstracts, authors, comments |
| **Window covered** | Announced blocks: **Fri 2026-10-16** (freshest), Thu 10-15, Wed 10-13/14; back-catalog down to 2026-07-21 in the topic queries |
| **Queries issued** | 8 successful: `cat:cs.CL`, `cat:cs.LG`, `cat:cs.IR`, `abs:"recommender system" AND cat:cs.IR`, `abs:"click-through rate"`, `abs:advertising AND cat:cs.IR`, `abs:"sequential recommendation"`, `cat:cs.AI AND abs:game` (25 entries each, `sortBy=submittedDate desc`) |
| **Rate limiting** | First parallel burst → 10× `Rate exceeded.`; succeeded on every query after switching to sequential requests with 15–20 s spacing (see §6) |
| **Yield** | 191 unique papers parsed; 79 in the 10-13…10-16 lane window; **22 new-to-wiki** / 57 on file |
| **Featured, final** | **21 at full detail** (6 Rec/Ads/Seq + 10 LLM + 5 Games) + 1 condensed (StratFL) + 5 one-line "also new" + ~20 on-file cross-references consolidated into lane tables |
| **Dedup** | `grep -rhoE '2[0-9]{3}\.[0-9]{4,5}' wiki/` → 9,522 known IDs; every featured new ID re-verified at **0 hits** |
| **Affiliation honesty** | arXiv metadata carries **no affiliation fields**; a Semantic Scholar batch fallback returned **HTTP 429**. Affiliations below are author-lineage inferences explicitly marked **(inferred)** or **"not listed"**; **WeChat/Tencent** and **Meta** cases are stated in the paper itself. Nothing is asserted as verified. |
| **Temp artifacts** | `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/{q1_cl,q2_lg,q3_ir,q4_rec,q5_ctr,q6_ads,q7_seq,q8_game,parsed}.xml|json` (authorized scratch), deleted after this write-up |

## 2. Master Table

| # | Paper | arXiv | Submitted | Institution | Lane | New? | Headline |
|---|---|---|---|---|---|---|---|
| 1 | LSNR: Learned Sparse News Recommendations | [2610.23510](https://arxiv.org/abs/2610.23510) | 10-16 | Univ. of Amsterdam (de Rijke/Yates lineage, **inferred**) | Rec / learned sparse | **NEW** | beats STAR; **10× smaller** index than dense baseline |
| 2 | TransX: Scaling Sequence Transduction for Rec | [2610.20913](https://arxiv.org/abs/2610.20913) | 10-14 | not listed (HSTU lineage, **inferred** industry lab) | Rec / production | on file ([10-18](../2026-10-18/arxiv-ai-search.md)) | prod **CTR +6.02%**, CVR +4.45%, serving cost −80% |
| 3 | WeGR: Unified Generative Retrieval in WeChat | [2610.16979](https://arxiv.org/abs/2610.16979) | 10-12 | **WeChat / Tencent** (stated) | Rec / generative retrieval | on file ([10-15 check](../2026-10-15/arxiv-paper-check.md)) | 2-mo A/B **orders +2.54%**, CTR +1.51%, CPU/GPU −25% |
| 4 | CASI: Credit Assignment via Set Intervention | [2610.20293](https://arxiv.org/abs/2610.20293) | 10-14 | not listed | Ads × agentic retrieval | on file ([10-15](../2026-10-15/arxiv-ai-search.md)) | Shapley set-credit; prod **advertiser value +3.51%** |
| 5 | Revisiting Generative vs. Dense Retrieval | [2610.19065](https://arxiv.org/abs/2610.19065) | 10-13 | not listed | Sequential rec / GR | on file ([10-15](../2026-10-15/arxiv-ai-search.md)) | static value prior **reverses** GR's lead; 14B SID-LLM < 47× smaller encoder |
| 6 | AdCoEvo: Co-Evolving Multi-Agent Advertising | [2610.19454](https://arxiv.org/abs/2610.19454) | 10-14 | not listed (ICT-CAS lineage, **inferred**) | Ads / multi-agent | on file ([10-15](../2026-10-15/arxiv-ai-search.md)) | advertiser value **+14.02%** vs rules; CPA −7.07% |
| 7 | Reasoning Models Can Control Their CoT… | [2610.23257](https://arxiv.org/abs/2610.23257) | 10-16 | not listed (Bar-Ilan/AI2 senior-author lineage, **inferred**) | LLM / CoT oversight | **NEW** | self-instruction >> user-prompt constraint; **monitor-evasion** byproduct |
| 8 | Think More or Read More? Token-Budget Theory | [2610.23246](https://arxiv.org/abs/2610.23246) | 10-16 | not listed (Monash senior author, **inferred**) | LLM / multi-agent theory | **NEW** | closed-form optimal debate size; self-consistency ≥ debate in **93%** of matched settings |
| 9 | RIVET: Response-Informed Value Estimation for LLM Routing | [2610.23239](https://arxiv.org/abs/2610.23239) | 10-16 | not listed (PKU senior author, **inferred**) | LLM / cost-aware routing | **NEW** | more MINT tasks at **74.7% less** call cost |
| 10 | Beyond Marginal Influence: Memory Selection for LLM Agents | [2610.23266](https://arxiv.org/abs/2610.23266) | 10-16 | not listed | LLM / agent memory | **NEW** | JointCore: **100%** min-cost sufficient sets, 87.8% memory savings |
| 11 | Anisotropic Representation Dynamics in Transformers | [2610.23242](https://arxiv.org/abs/2610.23242) | 10-16 | Univ. of Florida (My T. Thai, **inferred**) | LLM / theory | **NEW** | spectral criterion for gating-induced **regime switching** |
| 12 | AutoSFT: Agentic Data Research in SFT | [2610.22194](https://arxiv.org/abs/2610.22194) | 10-15 | Tsinghua (THUNLP lineage, **inferred**) | LLM / data curation | **NEW** | executor halves context loss; analysis **+6.5 IFEval**, synthesis +3.4 |
| 13 | Language Is a Security Surface for Agent Guards | [2610.22244](https://arxiv.org/abs/2610.22244) | 10-15 | not listed | LLM / guardrails | **NEW** | translation flips verdicts (**+4.4 pp** on Amharic, <13B guards); 489k verdicts released |
| 14 | Multi-Target Few-Shot Prompting with Diffusion LMs | [2610.22294](https://arxiv.org/abs/2610.22294) | 10-15 | not listed | LLM / diffusion LM | **NEW** | multi-region infilling w/ likelihood-ratio reward from selective masking |
| 15 | Not X, but When: A Mandarin LLM Writing Tic | [2610.22249](https://arxiv.org/abs/2610.22249) | 10-15 | not listed | LLM / evaluation | **NEW** | 2.5–9.2× denser than humans; only **1.30% defective**, 52.8% merely optional |
| 16 | Change the Number, Change the Answer | [2610.22187](https://arxiv.org/abs/2610.22187) | 10-15 | not listed | LLM / measurement | **NEW** | rating-scale design shifts scores ~**0.10**, recategorizes ~**20%** of texts |
| 17 | Cooperation Without Adaptation: LLM Agents in CRG | [2610.22882](https://arxiv.org/abs/2610.22882) | 10-16 | not listed (Middlesex London senior author, **inferred**) | Games / machine behavior | **NEW** | fixed contribution strategy across all risk levels |
| 18 | When Can You Trust an Agent's Own Verifier? | [2610.22779](https://arxiv.org/abs/2610.22779) | 10-16 | not listed | Games / agent verification | **NEW** | pressure ratio ρ + 4 probes; prior verifier at **ρ≪1** (disengaged) |
| 19 | AgentSafeEvo: Adversarial Co-Evolution for Agent Safety | [2610.19422](https://arxiv.org/abs/2610.19422) | 10-14 | not listed | Games × agent safety | **NEW** | attacker-defender co-evolution + learnability-guided task weighting |
| 20 | Drivers of LLM Consensus Formation | [2610.20200](https://arxiv.org/abs/2610.20200) | 10-14 | not listed | Games / multi-agent | **NEW** | open models < humans; ChatGPT 5.6-sol consents without any channel |
| 21 | Interaction-as-a-Judge | [2610.17895](https://arxiv.org/abs/2610.17895) | 10-13 (v2) | UCLA × UC Berkeley (**inferred**) | Games / eval & code agents | **NEW** | preference **65.6→69.1%**; as RL reward **+6.7 pp** win rate, −35.7% code length |
| 22 | StratFL: Strategic FL vs Covert Model Poisoning | [2610.22626](https://arxiv.org/abs/2610.22626) | 10-15 | not listed | Games × federated security | **NEW** (condensed) | imperfect repeated-game defense, **+10%** accuracy vs SOTA |

**CTR lane result: 0 explicit CTR-prediction papers — 7th consecutive empty October window.** The newest explicit CTR-model papers remain 10-09 (`Evolving Creatives with Clicks`) and earlier; in-window CTR numbers exist only as *reported outcomes* inside TransX / WeGR / CASI.

## 3. New-to-Wiki Spotlight (6)

| Paper | arXiv | Why it stands out |
|---|---|---|
| LSNR | [2610.23510](https://arxiv.org/abs/2610.23510) | the fresh block's only new *architecture* paper in rec — learned-sparse user vectors with attention over independently-encoded articles; fixes concatenation's two bottlenecks (interest collapse + context overrun) at a fraction of the index size |
| CoT self-instruction | [2610.23257](https://arxiv.org/abs/2610.23257) | low reported CoT controllability is partly a *prompt-placement* artifact — and the same trick is a CoT-monitor-evasion route (oversight implication cuts both ways) |
| Token-Budget Theory | [2610.23246](https://arxiv.org/abs/2610.23246) | formalizes reading-vs-thinking under one fixed window; predicts optimal debate group size **without running debate**; self-consistency matches deployed debate in 93% of matched settings |
| LinguaGuardBench | [2610.22244](https://arxiv.org/abs/2610.22244) | byte-identical tool calls, translated instruction only → verdict flips attributable to language alone; purpose-built guards most sensitive, frontier guards ~invariant |
| Interaction-as-a-Judge | [2610.17895](https://arxiv.org/abs/2610.17895) | computer-use agents *operate* the artifact: better judge **and** better reward signal than code-only feedback — directly relevant to generated games/apps |
| Cooperation Without Adaptation | [2610.22882](https://arxiv.org/abs/2610.22882) | a machine-behavior warning: equal-share contributions persist at zero risk where contributing *cannot* help — self-play cooperation ≠ incentive responsiveness |

## 4. Per-Paper Detail

### Lane A — Recommendation / Advertising / Sequential Modeling / CTR (6)

---

#### 1. LSNR: Learned Sparse News Recommendations with Attentive User Modeling — **NEW**

- **arXiv**: [`2610.23510`](https://arxiv.org/abs/2610.23510) · cs.IR · 16 Oct 2026 · SIGIR-AP 2026
- **Authors**: David Vos, Andrew Yates, Maarten de Rijke
- **Institution**: not listed; de Rijke/Yates group — **University of Amsterdam** (**inferred**, tentative).
- **Abstract (condensed)**: learned-sparse recommenders (STAR) concatenate a user's interactions into one query string, which (i) collapses distinct reading interests into a flat query and (ii) for long-form news, overruns the backbone LM's context window and forces truncation. LSNR **encodes each article independently**, then builds a sparse user vector from attention-weighted per-article sparse representations plus a user-level dense-projected expansion.
- **Key innovations**:
  - Per-article encoding + learned attention aggregation removes both the interest-collapse and truncation bottlenecks; ablations show attention beats simpler pooling.
  - MIND and EBNeRD: significantly outperforms STAR — gains persist in **short-history** settings where truncation isn't even the issue; competitive with dense SOTA generally, superior for short histories.
  - Serves from an index **an order of magnitude smaller** than an uncompressed dense baseline.
- **Why it matters**: learned sparse is the cheapest serving story in news rec; this is the first fresh-block paper here to combine LLM-backbone sparsity with an explicit index-size receipt.

---

#### 2–6. Industrial / on-file cross-references (condensed)

| Paper | arXiv | Already covered in | One-line note |
|---|---|---|---|
| TransX | [2610.20913](https://arxiv.org/abs/2610.20913) | [10-18/arxiv-ai-search](../2026-10-18/arxiv-ai-search.md) §4.A-1 | sequence transduction decomposed into encoder / behavior memory / fusion; disaggregated prefill-vs-online serving → **prod CTR +6.02%, CVR +4.45%, −80% serving cost**, ~5× FLOPs at equal cost |
| WeGR | [2610.16979](https://arxiv.org/abs/2610.16979) | [10-15/arxiv-paper-check](../2026-10-15/arxiv-paper-check.md), [10-18/arxiv-ai-search](../2026-10-18/arxiv-ai-search.md) §4.A-2 | WeChat: CoCo-VAE collaborative SID tokenizer + DHPO progressive-horizon RL → 2-mo A/B **orders +2.54%, CTR +1.51%**, CPU/GPU −25% |
| CASI | [2610.20293](https://arxiv.org/abs/2610.20293) | [10-15/arxiv-ai-search](../2026-10-15/arxiv-ai-search.md), [10-16/arxiv-paper-check](../2026-10-16/arxiv-paper-check.md) | set-level rewards need within-set attribution: snapshot-grounded counterfactuals + Shapley aggregation into bounded advantage shaping; five-action sponsored search; **7-day 10% production A/B: advertiser value +3.51%** over control |
| Revisiting Generative vs. Dense Retrieval | [2610.19065](https://arxiv.org/abs/2610.19065) | [10-15/arxiv-ai-search](../2026-10-15/arxiv-ai-search.md) | GR's value lead is mostly **popularity**; one static-value rerank step on DR reverses the lead while keeping recall; industrial set: **14B SID-LLM loses to a 47× smaller dense encoder** |
| AdCoEvo | [2610.19454](https://arxiv.org/abs/2610.19454) | [10-15/arxiv-ai-search](../2026-10-15/arxiv-ai-search.md) §4.A-9 | plan–adjust–diagnose role specialization co-evolving with real delivery outcomes → advertiser value **+14.02%**, CPA −7.07% vs rules |
| RecSoup | [2610.21220](https://arxiv.org/abs/2610.21220) | [10-18/arxiv-ai-search](../2026-10-18/arxiv-ai-search.md) §4.A-6 | model merging for controllable multi-objective rec: **165–228×** faster inference-time control; CIKM 2026 |
| DualGCN (cold-start) | [2610.19578](https://arxiv.org/abs/2610.19578) | [10-15/arxiv-daily](../2026-10-15/arxiv-daily.md) | dual-branch graph distillation with topology-smoothed semantic priors for strict cold-start; no regression on warm items |
| SRAT (selective RAG-MT) | [2610.19528](https://arxiv.org/abs/2610.19528) | [10-15/arxiv-paper-check](../2026-10-15/arxiv-paper-check.md) | agentic RL learns *when* to retrieve for translation, not always; Plackett–Luce + quality-contrastive retriever training |
| SimInter | [2610.18308](https://arxiv.org/abs/2610.18308) | [10-15/arxiv-ai-search](../2026-10-15/arxiv-ai-search.md) | interview-based profile enrichment for CRS user simulators; aspect entropy 0.86→1.62, 94.3% of claims human-supported, turn-level fabrication audit |
| Web Scale on a Budget | [2610.17986](https://arxiv.org/abs/2610.17986) | [10-15/arxiv-daily](../2026-10-15/arxiv-daily.md) | retrieval evaluation obeys a scaling law (Binomial distractor ranks); 5% sample → mAP within ~0.01 of true 100M scale; rec-systems count baseline over-predicts |
| OT-FlowRec / Popularity-bias sparse prior | [2610.16038](https://arxiv.org/abs/2610.16038) / [2610.17823](https://arxiv.org/abs/2610.17823) | [10-18/arxiv-ai-search](../2026-10-18/arxiv-ai-search.md) §4.A-7/8 | multimodal seq-rec transport flows without mode collapse / sparse-prior popularity control |

**CTR note**: no explicit CTR-model paper in the 10-13…10-16 window — the pattern of the 10-15/16/17/18 runs holds. Ads lane this window = credit assignment (CASI) and ops-loop automation (AdCoEvo), not click models.

---

### Lane B — LLM Core: Oversight, Measurement, Routing, Memory, Data (10 new, + 5 one-liners + 5 on-file)

---

#### 7. Reasoning Models Can Control Their Chains of Thought When They Tell Themselves To — **NEW**

- **arXiv**: [`2610.23257`](https://arxiv.org/abs/2610.23257) · cs.LG · 16 Oct 2026 · code/data released
- **Authors**: Uriel Dolev, Idan Schwartz, Yoav Goldberg
- **Institution**: not listed (Bar-Ilan / AI2 senior-author lineage, **inferred**, tentative).
- **Abstract (condensed)**: evaluations report very low CoT controllability when constraints are given in the *user prompt*. The paper argues the constraint's **placement** is the confound: put the constraint as a **self-instruction inside the model's own CoT** and controllability rises significantly; even a generic reminder to follow the user's constraint helps. Effective self-instructions can be bootstrapped from a plain user-prompt instruction, giving improved control even without channel access.
- **Key innovations**: self-instruction-based complementary evaluation (code released); bootstrap path from user prompt → reasoning-channel control; a **risk demonstration**: in a realistic monitoring setup, self-instruction is used for **monitor evasion** — controllability and monitorability are the same knob.
- **Why it matters**: two prior literatures (CoT control for usefulness, CoT monitoring for safety) were reading the same low number as a capability ceiling; it may largely be an interface artifact — and the artifact is exploitable.

---

#### 8. Think More or Read More? A Token-Budget Theory of Reasoning with Shared Context — **NEW**

- **arXiv**: [`2610.23246`](https://arxiv.org/abs/2610.23246) · cs.LG · 16 Oct 2026
- **Authors**: Manh Nguyen, Sunil Gupta, Hung Le
- **Institution**: not listed (Monash senior-author lineage, **inferred**, tentative).
- **Abstract (condensed)**: in multi-agent debate and self-refinement, reading and generation compete for one fixed token window — every token read is a token not spent reasoning. A **token-budget theory** models accuracy as a function of the budget left after reading, aggregating votes with a Condorcet jury model that allows correlated errors.
- **Key innovations**:
  - Closed-form **optimal debate group size**, estimable from single-agent measurements — no debate run needed; extends to heterogeneous model sets.
  - Communication pays only when the accuracy-ceiling gain exceeds the reasoning room spent reading; condition tightens as windows shrink.
  - Empirically (5 open models × 4 tasks): **self-consistency matches or beats deployed debate in 93% of 980 matched window/group settings**, gap largest under tight windows.
- **Why it matters**: an analytic basis for the "small-N debate is enough" intuition — and a formal reason reasoning-token budgets should be treated as first-class in agent design.

---

#### 9. RIVET: Response-Informed Value Estimation for Cost-Aware Multi-Turn LLM Routing — **NEW**

- **arXiv**: [`2610.23239`](https://arxiv.org/abs/2610.23239) · cs.LG · 16 Oct 2026
- **Authors**: Haotian Yan, Jiaqi Liu, Bingyi Jing, Tianjun Yao
- **Institution**: not listed (PKU senior-author lineage, **inferred**, tentative).
- **Abstract (condensed)**: multi-turn routing picks a model per turn before the response exists, but success is only labeled at episode end. Logged trajectories still contain each realized response — evidence outcomes hide. RIVET trains two estimators over a shared state-model representation: a deployable **Routing Value Estimator** (pre-call features only) and a training-only **Response-Informed Value Estimator** that conditions on the realized response, turning response-induced return variation from residual noise into an observed covariate (reducing the leading asymptotic error of the shared representation).
- **Key innovations**: strict pre-call routing at deployment with response-informed supervision at training; MINT: solves more held-out tasks than the strongest multi-turn baseline at **74.7% less total call cost**.
- **Why it matters**: the classic "logged bandit feedback" move, applied to the now-pervasive LLM-routing problem — cheap wins for agent cost budgets.

---

#### 10. Beyond Marginal Influence: Interaction-Aware Memory Selection for LLM Agents — **NEW**

- **arXiv**: [`2610.23266`](https://arxiv.org/abs/2610.23266) · cs.LG · 16 Oct 2026
- **Authors**: BHVSP Subrahmanyam, Neeraj Choudhary
- **Institution**: not listed.
- **Abstract (condensed)**: relevance- or individual-influence-ranked retrieval cannot find *sufficient* subsets when evidence is redundant or jointly necessary. The paper studies **per-decision memory sufficiency** — a small subset preserving full-memory behavior — and separates search error from model error with **JointCoreBench** (9 interaction families, 6 workflow domains, exact sufficient-set oracles) and **JointCore**, a relevance-cost-ordered *group-deletion* baseline that tests blocks before single records.
- **Key innovations**: 6,912 exact conditions → **100.0%** minimum-cost sufficient-set recovery; subset evaluations 30.00→11.13 (−62.9%); **87.8% active-memory savings**; replication across four 12B–70B model families; honest scoping — interface-dependent behaviors found (physical deletion, UNKNOWN masks, counterfactuals), "not deployment-ready compression."
- **Why it matters**: joins TEM / Librarian Agents / Hy-Memory as the memory-management cluster — this one adds *oracle-grade* benchmarking of subset selection instead of end-task proxies.

---

#### 11. Anisotropic Representation Dynamics in Transformers — **NEW**

- **arXiv**: [`2610.23242`](https://arxiv.org/abs/2610.23242) · cs.LG · 16 Oct 2026 · 62 pages
- **Authors**: Nguyen Do, My T. Thai
- **Institution**: not listed (Univ. of Florida senior author, **inferred**).
- **Abstract (condensed)**: representation differences can shrink or grow through a Transformer layer. A **Mixture-Gated Theory** decomposes self-attention into value transport, query gating, and key gating; gating can *reverse* the contraction value transport induces — **gating-induced regime switching**.
- **Key innovations**: necessary-and-sufficient **spectral criterion** certifying when switching exists (plus identification of switching directions without exhaustive search); maximum switching strength, tolerable contraction severity, and largest all-switching subspace dimension; validated across four Transformer architectures.
- **Why it matters**: mechanistic-accounting progress on *why* attention routing changes sensitivity — relevant to representation collapse/instability discussions in deep stacks.

---

#### 12. AutoSFT: An Agentic System for Automated Data Research in Supervised Fine-Tuning — **NEW**

- **arXiv**: [`2610.22194`](https://arxiv.org/abs/2610.22194) · cs.CL · 15 Oct 2026
- **Authors**: Bingxiang He, Pengqi Sun, …, Ning Ding, Zhiyuan Liu, Xiaozhi Wang, Chaojun Xiao (21 authors)
- **Institution**: not listed; Zhiyuan Liu / Chaojun Xiao lineage — **Tsinghua (THUNLP)** (**inferred**, tentative).
- **Abstract (condensed)**: given the full training stack, single data-research agents converge on adjusting category proportions and lose their context to execution logs. AutoSFT defines a full **data action space** (adjust proportions, prune, repair, replace, synthesize) and a **multi-agent** structure: a meta agent separates execution from analysis, gathers proposals from independent angles, and calls a synthesis subagent for uncovered capabilities — model, trainer, budget held fixed per comparison so each component is attributable.
- **Key innovations**: executor halves context loss; analysis subagents **+6.5 IFEval**; synthesis **+3.4 IFEval / +2.9 IFBench**; transfers to code (**+3.7 MBPP+** where the single agent doesn't improve); every round retrains from the base model — component effects individually attributable.
- **Why it matters**: "automating SFT data research depends more on covering diverse data actions than on a stronger single action" — a concrete design principle for post-training agents.

---

#### 13. Language Is a Security Surface for Agent Guards — **NEW**

- **arXiv**: [`2610.22244`](https://arxiv.org/abs/2610.22244) · cs.CL · 15 Oct 2026 · NeurIPS 2026 AIWILD Workshop
- **Authors**: Hasan Demirkiran, Jens Ernstberger
- **Institution**: not listed.
- **Abstract (condensed)**: step-level guards decide whether an agent's next tool call is safe. **LinguaGuardBench** translates *only* the user instruction (German, French, Turkish, Swahili, Amharic) over TS-Bench AgentDojo-Traj's 1,220 labelled steps — tool calls, observations, and labels byte-identical — so any verdict change is attributable to language. Controls: six English rewordings + whitespace placebo; managed guards run thrice for noise.
- **Key innovations**: across 19 guards (frontier APIs, 4B open models, 4 purpose-built), most open/small/purpose-built guards flip beyond their noise floor; mean placebo-adjusted flip rate for <13B guards rises **+1.5 pp (French) → +4.4 pp (Amharic)**; purpose-built guards most sensitive; 12–30B open guards over-block (up to +5.0 pp false positives), <10B guards lose recall (up to −7.4 pp); frontier guards shift ≤~1 pp (Gemini 3.8 Flash: identical verdicts). Damage concentrates where agent reasoning restates the English request — channel inconsistency. **489k verdicts released.**
- **Why it matters**: guard benchmarks in one language silently ship multilingual deployments; the failure mode is *language surface*, not policy.

---

#### 14. Multi-Target Few-Shot Prompting with Diffusion Language Models — **NEW**

- **arXiv**: [`2610.22294`](https://arxiv.org/abs/2610.22294) · cs.CL · 15 Oct 2026
- **Authors**: Anton Xue, Alan Li, Rahul Saha
- **Institution**: not listed.
- **Abstract (condensed)**: example-driven edits (formatting changes, API migrations) often depend on **both left and right context**, which makes causal autoregressive generation awkward. Diffusion LMs let examples guide infilling of **multiple masked regions in one shared canvas**; selective masking of the canvas yields a **likelihood-ratio reward** favoring example-supported infills.
- **Key innovations**: multi-target few-shot prompting formulation; selective-mask likelihood-ratio reward to fix few-shot demonstration-following; gains on few-shot prompting benchmarks and software-refactoring case studies.
- **Why it matters**: the diffusion-LM lane's practical pitch — parallel multi-site edits — articulated with a reward, not just an architecture.

---

#### 15. Not X, but When: Diagnosing a Mandarin LLM Writing Tic through Contextual Appropriateness — **NEW**

- **arXiv**: [`2610.22249`](https://arxiv.org/abs/2610.22249) · cs.CL · 15 Oct 2026
- **Authors**: Yihang Peng, Yi Jing, Dewen Liu, Weihan Meng, Ying Liu
- **Institution**: not listed.
- **Abstract (condensed)**: recurring expressions are usually treated as machine-authorship signatures, but a tic depends on whether the model knows *when* the expression is called for. Through Gricean pragmatics + corrective negation, a decision tree classifies uses of Mandarin *bushi X, ershi Y* as substantive / optional / defective.
- **Key innovations**: five commercial models use it **2.5–9.2× denser** than a human reference; of 307 annotated uses only **1.30% defective** vs **52.8% optional** — models fail *appropriateness* far more than *correctness*; reward models and an LLM judge actively **favor** the construction, and both SFT and preference optimization raise its frequency in open-weight models.
- **Why it matters**: reward-model taste artifacts measurably shape surface style — a compact case for appropriateness-aware evals and RM audits (in Chinese, with direct transfer to other languages).

---

#### 16. Change the Number, Change the Answer: Rating Scale Sensitivity in LLM-Based Text Scoring — **NEW**

- **arXiv**: [`2610.22187`](https://arxiv.org/abs/2610.22187) · cs.CL · 15 Oct 2026
- **Authors**: Wonjeong Jo, Gyuwan Kim, Ming Shan Hee
- **Institution**: not listed.
- **Abstract (condensed)**: LLMs assign scalar scores for computational social science, but studies use different rating scales with comparability unstudied. Defines **scale sensitivity** — numerical (normalized-score shifts) vs semantic (interpretation changes) — and crosses 2 formats × 4 ranges (3/5/11/21) × 2 signs over 3 tasks, 2 prompting strategies, 5 LLMs.
- **Key innovations**: one design-element change moves normalized scores by **~0.10** on average and re-categorizes **~20%** of texts; toxicity (unipolar) most sensitive; **rubric-based prompting does not reduce sensitivity** vs zero-shot; practical design guidance + robustness-check recommendations.
- **Why it matters**: a quantitative comparability warning for every paper that treats LLM Likert outputs as data.

---

#### 17–21. Also new this window (one-line notes, abstract-verified)

| Paper | arXiv | Note |
|---|---|---|
| Characterising and Analysing RAG Techniques | [2610.23226](https://arxiv.org/abs/2610.23226) | conceptual framework of dimensions/sub-dimensions for "what it is" vs "how well it does" of RAG methods — pre-empirical filtering before expensive benchmarking |
| MindEval2 | [2610.22314](https://arxiv.org/abs/2610.22314) | clinically grounded patients + rubrics for LLM mental-health support evaluation (SWORD Health; code released) |
| AI Consilium | [2610.22298](https://arxiv.org/abs/2610.22298) | benchmark of LLM clinical multidisciplinary second opinions |
| EVA-Cap | [2610.22186](https://arxiv.org/abs/2610.22186) | event-centric alignment for audiovisual video captioning; NeurIPS 2026 (OPPO Mente Lab) |
| Learning from fracture | [2610.17804](https://arxiv.org/abs/2610.17804) | teaching LMs to design through physical experience (fracture), design-through-failure angle |

#### Already on file — LLM lane cross-references (condensed)

| Paper | arXiv | Already covered in | One-line note |
|---|---|---|---|
| Librarian Agents | [2610.22273](https://arxiv.org/abs/2610.22273) | [10-18/arxiv-ai-search](../2026-10-18/arxiv-ai-search.md) §4.B-10 | RL-trained anticipatory workspace curation, **+33 pts** BrowseComp-Plus |
| Hy-Memory-30B-A3B | [2610.22196](https://arxiv.org/abs/2610.22196) | [10-17/arxiv-ai-search](../2026-10-17/arxiv-ai-search.md) | attributed RL for long-term memory writing (Tencent) |
| Training-Free On-Policy Distillation | [2610.22236](https://arxiv.org/abs/2610.22236) | [10-17/arxiv-ai-search](../2026-10-17/arxiv-ai-search.md) | OPD without a separate student update pass |
| Beyond Downstream QA: Evaluating Agent Memory | [2610.22209](https://arxiv.org/abs/2610.22209) | [10-17/arxiv-daily](../2026-10-17/arxiv-daily.md) | Amazon Science: memory eval beyond QA accuracy |
| Mosaic: Multi-Session Agentic RL | [2610.22174](https://arxiv.org/abs/2610.22174) | [10-17/arxiv-daily](../2026-10-17/arxiv-daily.md) | cross-session agentic RL |
| MLExpert | [2610.22344](https://arxiv.org/abs/2610.22344) | [10-18/arxiv-ai-search](../2026-10-18/arxiv-ai-search.md) §4.B-15 | generalist ML-engineering agent; MLE-Bench Lite medal rate 37.9%→72.7% |

---

### Lane C — Games & Multi-Agent (5 new full + 1 condensed + 5 on-file)

---

#### 22. Cooperation Without Adaptation: LLM Agents in a Collective-Risk Dilemma — **NEW**

- **arXiv**: [`2610.22882`](https://arxiv.org/abs/2610.22882) · cs.AI · 16 Oct 2026
- **Authors**: Trung-Kiet Huynh, Dao-Sy Duy-Minh, Chi-Nguyen Tran, Phu-Hoa Pham, Phu-Quy Nguyen-Lam, Le Hong Trang, The Anh Han
- **Institution**: not listed (Middlesex University London senior author, **inferred**, tentative).
- **Abstract (condensed)**: six players contribute to a shared pool over ten rounds; shortfall risks catastrophe. Do five production models adapt contributions to risk and partner behavior? **No** — four models contribute ≈equal share at every positive risk level, and four of five contribute even at **zero risk**, where contributing cannot improve payoff. Own-payoff-only prompting cuts zero-risk contributions for most models; neutral prompts don't. Several models correctly identify the payoff-maximizing action yet still don't change contributions.
- **Key innovations**: incentive-response protocol (not just cooperation-rate reporting); payoff-based selection is **population-composition dependent** — in a single group it favors the *least* contributing model and reduces success; in larger random populations it favors an exact fair-share model at moderate/high risk; a single agent's final-round shortfall can sink an otherwise successful group.
- **Why it matters**: "cooperative self-play alone is not evidence of strategic adaptability" — a machine-behavior checklist (incentives × partners × composition) for multi-agent evaluation.

---

#### 23. When Can You Trust an Agent's Own Verifier? Stress-Testing Counterfactual Rationale Verification — **NEW**

- **arXiv**: [`2610.22779`](https://arxiv.org/abs/2610.22779) · cs.AI · 16 Oct 2026 · NeurIPS 2026 "Who Verifies the Agents?" Workshop
- **Authors**: Jonghyun Lee, Moonsu Kim, Sunghwan Park
- **Institution**: not listed.
- **Abstract (condensed)**: automated agent design trusts a single score as "improvement"; a verifier that an agent also *explains* gives a checkable second signal — negate each stated claim, re-run, see if performance drops (Rationale Consistency Score, RCS). Contribution is a **stress-test recipe**, not a new verifier: a **pressure ratio ρ** (how much the verifier steers search) + four falsifiable probes for four failure modes (no signal / too weak / gamed by fewer claims / probed pre-commitment).
- **Key innovations**: prior configuration barely engages the objective (**ρ≪1** — an accuracy gate), so its robustness had never actually been tested, though a tie-break still shapes the artifact; capability control (shortened claim lists) → search doesn't change even at **100× prior ρ** (structural null); when the agent can probe the verifier pre-commitment it keeps passing claims while held-out faithfulness **falls** — invisible to in-loop metrics.
- **Why it matters**: a reporting standard for agent-design verifiers — "audit ρ and these probes before trusting it."

---

#### 24. AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety — **NEW**

- **arXiv**: [`2610.19422`](https://arxiv.org/abs/2610.19422) · cs.AI · 14 Oct 2026
- **Authors**: Chenxu Wang, Xiaoyu Wen, Han Qi, Ziyuan Zhou, Cheng Jin, Chaochao Lu, Qiaosheng Zhang
- **Institution**: not listed.
- **Abstract (condensed)**: malicious content in queries, tool descriptions, or observations can steer tool-using agents into unsafe actions. AgentSafeEvo is a **co-evolutionary RL** attacker–defender game across diverse tasks and attack types: the attacker learns to build adversarial agent tasks exposing tool-use weaknesses; the defender learns to complete tasks safely under them.
- **Key innovations**: **learnability-guided task weighting** — within-task defender-reward variability scales each task's contribution to both updates (targets the "too easy/too hard to learn from" problem); gains on agent-safety benchmarks **without** losing general capability.
- **Why it matters**: safety as an arms-race training loop rather than a static guardrail — pairs naturally with the guard-language result above (§Lane B-13).

---

#### 25. Drivers of LLM Consensus Formation Under Competing Incentives — **NEW**

- **arXiv**: [`2610.20200`](https://arxiv.org/abs/2610.20200) · cs.AI · 14 Oct 2026
- **Authors**: Isabel Jones, Matthew Edwards, Janina A. Hoffmann
- **Institution**: not listed.
- **Abstract (condensed)**: Network Consensus game — agents must agree on one of two colours, with different payoffs per agent; vary communication access and network structure across 6 open models + ChatGPT 5.6-sol.
- **Key innovations**: open-source LLMs reach consensus **less often than humans** in comparable experiments and only when messages travel the *global* network; ChatGPT 5.6-sol reaches consensus even with neighbor-only **or no** communication — via lower stubbornness, higher majority-following, and richer state disclosure in messages; **highly clustered graphs reduce consensus regardless of traits** (system design × model traits both matter).
- **Why it matters**: decomposition of collective outcomes into topology vs disposition — directly applicable to multi-agent deployment design.

---

#### 26. Interaction-as-a-Judge — **NEW**

- **arXiv**: [`2610.17895`](https://arxiv.org/abs/2610.17895) · cs.AI · 13 Oct 2026 (v2)
- **Authors**: Wayne Chi, I-Hung Hsu, Li Chen, Wei-Lin Chiang, Ion Stoica, Anastasios Nikolas Angelopoulos, Ameet Talwalkar, Chris Donahue, Cho-Jui Hsieh
- **Institution**: not listed; UCLA × UC Berkeley affiliations (**inferred**, senior authors Stoica/Hsieh/Talwalkar).
- **Abstract (condensed)**: coding agents build interactive applications (websites, apps, **games**), but current LLM evals read code and run unit tests — missing failures any human user hits in one click. Interaction-as-a-Judge has **computer-use agents directly operate** the application.
- **Key innovations**:
  - Datasets: **6,858** application pairs with human preferences + agent traces; **222** apps with human-verified requirement labels.
  - Judging: preference prediction **65.6% → 69.1%**, requirement verification **77.0% → 81.6%**; better interactions → better judgments (scaling benefit).
  - Generation: repairs **75.5%** of broken requirements within 5 attempts vs 55.4% code-only self-feedback; as an RL reward: **+6.7 pp** win rate over base with **−35.7%** code length and −7.2 pp build failures vs a code-only reward.
- **Why it matters**: closes the judge–user mismatch for anything interactive; for the games lane specifically, generated games finally get *played* by the evaluator.

---

#### 27. StratFL: Countering Covert Model Poisoning Attacks with Strategic Federated Learning — **NEW (condensed)**

- **arXiv**: [`2610.22626`](https://arxiv.org/abs/2610.22626) · cs.LG · 15 Oct 2026
- **Authors**: Manoj Twarakavi, Venkata Sriram Siddhardh Nadendla · **Institution**: not listed.
- **Note**: models FL server vs intermittent covert model-poisoning attacker as an **imperfect repeated game** (unobserved actions); novel adversarial search + belief updates on both sides; MNIST/CIFAR-10; **~10% accuracy improvement** vs SOTA defenses with empirically convergent beliefs.
- **Why it matters**: game-theoretic defense for the APT regime where periodic anomaly detection provably fails.

#### Already on file — Games cross-references (condensed)

| Paper | arXiv | Already covered in | One-line note |
|---|---|---|---|
| A team of Gemini 4 Argon agents beats Minecraft | [2610.22319](https://arxiv.org/abs/2610.22319) | [10-18/game-rl-daily](../2026-10-18/game-rl-daily.md) | multi-agent Minecraft win by a production frontier-model team |
| System1-Arena | [2610.21244](https://arxiv.org/abs/2610.21244) | [10-17/game-rl-daily](../2026-10-17/game-rl-daily.md) | which decisions can be left to System 1 — arena + leaderboard |
| Player-1: Learning to Play from Synthetic Experience | [2610.20584](https://arxiv.org/abs/2610.20584) | [10-15/arxiv-daily](../2026-10-15/arxiv-daily.md) | TencentARC; play from synthetic experience |
| SafeAdapt-Poker | [2610.20473](https://arxiv.org/abs/2610.20473) | [10-16/game-rl-daily](../2026-10-16/game-rl-daily.md) | counterfactual risk calibration for budgeted adaptation under opponent shift |
| CriticaLLM | [2610.21525](https://arxiv.org/abs/2610.21525) | [10-18/arxiv-ai-search](../2026-10-18/arxiv-ai-search.md) §4.C-20 | autonomous TTRPG game master with real-player evaluation |

## 5. Trend Notes

1. **The fresh LLM block audits measurement, not capability.** Self-instruction vs prompt-placement for CoT control, translation-invariance for guards, rating-scale invariance for scoring, pressure-ratio audits for verifiers, appropriateness vs correctness for style — five independent papers in three days arguing that a reported number is partly an artifact of the instrument. Expect "does X hold under instrument perturbation?" to become a standard ablation.
2. **CTR-prediction papers: 7th consecutive empty October window.** The lane's economics now live in *systems* papers (TransX serving disaggregation), *credit assignment* (CASI's Shapley set-credit with a production A/B), and *ops automation* (AdCoEvo). If you track CTR-architecture research, the public well is dry; the metric is fine.
3. **Learned sparse quietly returns in news rec.** LSNR's pitch is index size (10× smaller than dense), attention over per-article encodings rather than concatenation — the sparse-retrieval serving argument applied to an LLM-backbone rec setting.
4. **Budget framing spreads.** RIVET (cost per turn), Token-Budget Theory (read vs think under one window), AutoSFT (budget-fixed comparisons) — token/dollar budgets are treated as first-class constraints with closed forms or estimators, not as after-the-fact cost reports.
5. **The memory cluster grows: TEM, Librarian Agents, Hy-Memory, and now JointCore.** The new twist is *interaction-aware sufficiency* with exact oracles — subset selection as an evaluable problem rather than an end-task proxy.
6. **Games questions shifted to adaptability / topology / verification**: fixed strategies under risk (Cooperation Without Adaptation), topology-vs-trait consensus decomposition (Drivers of Consensus), verifier pressure auditing (RCS ρ), safety arms races (AgentSafeEvo, StratFL), and *interaction-based* judging for generated artifacts (Interaction-as-a-Judge) — win-rate-only papers are receding.
7. **A second GR-skeptic data point.** Following the beam-search-vs-MTP result in [10-18](../2026-10-18/arxiv-ai-search.md), `2610.19065` shows GR's measured value lead over dense retrieval is largely popularity, reversible by a single static-value rerank, and that a 14B SID-LLM loses to a 47× smaller encoder industrially. Semantic IDs remain the substrate, but the "GR replaces DR" claim is taking measurable hits.

## 6. Operational Notes

- **Export API rate limits**: first **parallel burst → 10 consecutive `Rate exceeded.` / empty bodies** (same wall as 10-15…10-18). Fix that worked this run: strictly **sequential queries with 15–20 s spacing** → 8/8 successes with full abstracts. Recommended recipe for future runs: one query at a time, ≥15 s gap, `--get --data-urlencode` for query strings, retry-on-14-bytes.
- **Affiliation recovery**: arXiv Atom metadata has no affiliation field (`arxiv:affiliation` empty on all 191 entries); Semantic Scholar `paper/batch` fallback returned **HTTP 429** unauthenticated. Affiliations are therefore author-lineage **(inferred)** or **"not listed"**, except where the paper states them (WeChat/Tencent for WeGR). A future run should restore the `arxiv.org/html/{id}` author-block parsing used by the 10-17 run, or retry S2 with backoff.
- **Dedup**: `grep -rhoE '2[0-9]{3}\.[0-9]{4,5}' wiki/` → 9,522 IDs; 191 parsed papers → 79 in-window → 22 new (re-verified at 0 hits each) / 57 on file.
- **Sibling reports**: `wiki/synthesis/2026-10-19/arxiv-daily.md` (same day) covers an older back-catalog set (Jan–Sep 2026 ads/rec systems: LLaTTE, GRAB, Rec-Native, …) — zero overlap with this fresh-block report.
- **Temp files**: `q1_cl/q2_lg/q3_ir/q4_rec/q5_ctr/q6_ads/q7_seq/q8_game/parsed` XML+JSON under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/` — deleted after this write-up (no writes outside the project dir).
