---
title: "arXiv Paper Check — AI & CTR (August 31, 2026)"
type: synthesis
created: 2026-08-31
updated: 2026-08-31
sources: []
tags: [arxiv, daily-check, ai, ctr, recommendation, ir, retrieval, agentic-rl, credit-assignment, agent-safety, monitoring, efficiency, kv-cache, tabular-icl, llm-as-judge, rag, daily-digest]
---

# arXiv Paper Check — AI & CTR (August 31, 2026)

Complement to the same-day [arxiv-daily](./arxiv-daily.md) (featured 13 + 5 HM) and [arxiv-ai-search](./arxiv-ai-search.md) (featured 18 + 5 HM). **Last-24h check over the Monday 31 Aug 2026 mailing** (IDs `2608.27460–2608.28589`), focused on AI, agents, CTR/rec/IR, and agentic-RL training/serving. **12 verified-new papers + 5 honorable mentions**, all grep-verified absent (0 hits) from `wiki/` and not claimed by either sibling digest.

> Method: same as the 08-31 siblings — `arxiv.org/list/{cat}/new` fetched via curl plus live `arxiv.org/abs/...` pages. Dedup boundary: the sibling `arxiv-daily` claims `2608.27950/27960/27991/28065/28199/28393/28306/28308/27857/28421/27508/27757/27912/27840/27826/28491/28027/28359`; the `arxiv-ai-search` claims 18 further IDs + 5 HM (SG-UMP, TiGER, Beyond-the-Vacuum, CommerceVibe, LandingAgent, GOD, dLLM spec-decoding, Thinking-Costs-Tokens, energy model, attention-rank, HDC, KD noise-floor, BBExplorer, Refundable-Deposits, two LMP dialogue-game papers, Code-as-Worlds, GeoNeXt, + HM). None of the IDs below overlaps those sets.

---

## ① CTR / Rec / IR (4)

### SkillFeed: Personalized Skill Routing with Counterfactual Evaluation

| Field | Detail |
|-------|--------|
| **Authors** | Tianle Wang, Yanghe Zou, Xiang Liu, Ziyao Huang, Chenchen Fu, Weiwei Wu |
| **Institution** | Not stated (Southeast University pattern, WW group) |
| **Submitted** | 2026-08-28 · [2608.28241](https://arxiv.org/abs/2608.28241) · cs.AI |
| **Key contribution** | Routing is usually **task-only semantic matching** — but when users with incompatible constraints issue the identical request, a task-only router picks a semantically plausible skill the requesting user cannot use. Reformulates **personalized skill routing as profile-conditioned retrieval** (relevance = f(task, user profile)), builds a profile-counterfactual benchmark (task held fixed, profile changes the reference skill), and proposes **SkillFeed**: a progressive retrieve-and-rerank stack (task–skill alignment first, then profile-conditioned discrimination on body-level evidence). On SkillFeed-Bench: **75.1% top-1** (+23.1 pp over the pretrained router); **+35.1 pp** on queries where the profile changes the reference skill. |
| **Why it matters** | Rec-adjacent restatement of the wiki's matching/ranking thread: "relevance" splits into query-side and user-side factors. The counterfactual split (profile *changes* ground truth) measures when conditioning matters, not just when it's possible — the benchmark-validity instinct applied to routing. |

### LINE Conversation History Retrieval for Personal Memory RAG

| Field | Detail |
|-------|--------|
| **Authors** | Akito Hattori |
| **Institution** | Sony *(inferred)* |
| **Submitted** | 2026-08-27 · [2608.27809](https://arxiv.org/abs/2608.27809) · cs.IR |
| **Key contribution** | First retrieval-only study over one user's LINE chat history as personal-memory ground truth. 358,896 messages → 22,329 temporally coherent chunks; three representations (raw_text, summary, **embedding_text** = summary + raw excerpt + fixed text) tested across BM25 / dense / linear hybrid over 100 annotator-verified questions. Best solo: embedding_text_BM25 (Recall@5 0.584); best hybrid: embedding_text_BM25 + embedding_text_vector at β=0.45 → **Recall@5 0.697 / MRR@5 0.595 / nDCG@5 0.575** (+0.113 vs solo, bootstrap 95% CI [0.048, 0.184]). Honest caveats: single-user/single-annotator, config chosen on the same questions; **aggregate questions spanning many times/conversations retrieve poorly** — flat chunking can't fuse distributed evidence. |
| **Why it matters** | The agent-memory/BYOAI thread gets a single-user corpus with real provenance. The "distributed evidence across time" failure is a concrete diagnostic for memory-RAG: flat retrievers can't fuse episodes the way memory-augmented agents are supposed to. |

### PULSAR: Pooled Unified Late-Interaction Search for Enterprise Visual Document RAG

| Field | Detail |
|-------|--------|
| **Authors** | Benjamin Constable, Anup Roy, Vishal Sharma, Rishabh Upadhyay, Robin Mills, Aidan Millar |
| **Institution** | Mubadala Investment Company *(stated)* |
| **Submitted** | 2026-08-28 · [2608.28572](https://arxiv.org/abs/2608.28572) · cs.IR |
| **Key contribution** | **Production vision-first retrieval** for visually dense pitch decks / board packs / diligence materials (deployed at Mubadala). Indexes page images with a frozen ColPali-style backbone + **pooled two-stage late-interaction index**: compact page summaries for first-pass retrieval, exact MaxSim rescoring over a finer pooled representation. On ViDoRe V3: pooled index cuts median vector-search latency **15.1×** vs unpooled at <0.01 NDCG@10/Recall@10 loss; production median latency 156 ms, ~**88× higher QPS** under load; ingestion ~20× cheaper per page than the OCR+verbalisation baseline. Since Mar 2026: 78K documents / ~2.4M pages / 3,000+ deals; **>2× answer-fact recall** over the OCR baseline at production top-K. |
| **Why it matters** | A rare production byline for late-interaction retrieval, and the exact two-stage structure (cheap coarse pre-retrieve + exact rescore) that ads/rec serving uses for candidate-gen→rank. Strong reference implementation for the wiki's retrieval/efficiency line. |

### NormasTCU: A pt-BR IR Dataset and LLM-as-a-Judge for Relevance

| Field | Detail |
|-------|--------|
| **Authors** | Leandro Carísio Fernandes, Marcus Vinícius Borela de Castro, Leandro dos Santos Ribeiro, Leonardo Augusto da Silva Pacheco, Edans Flávius de Oliveira Sandes |
| **Institution** | University of Brasília / UFCG *(inferred)* |
| **Submitted** | 2026-08-28 · [2608.27746](https://arxiv.org/abs/2608.27746) · cs.IR |
| **Key contribution** | Portuguese IR lacks public datasets; LLM relevance labelling in non-English specialized domains is unvalidated. **NormasTCU**: 14,469 legal documents, 46 queries, 3,048 human judgments over 812 q–d pairs. LLM-as-a-judge (3 models × 2 prompts): **positive scoring bias** (MAE 0.46–0.66 on 0–2), fair-to-moderate pair-level agreement with humans (κ 0.32–0.53). **Yet** LLM qrels yield highly similar system *rankings* for nDCG@10/MRR (Kendall τ ≥ 0.90, sometimes > individual human annotators) — but unreliable for P@10/R@10. |
| **Why it matters** | Direct evidence for the wiki's LLM-as-judge / eval-reliability thread: judge bias at pair level ≠ utility at ranking level. The nDCG-vs-P@10 dissociation is a reusable diagnostic for any judge-based IR/rec evaluation. |

---

## ② Agentic RL & Credit Assignment (4)

### VICT: Verifier-Instrumented Credit Tracing for Long-Horizon Agent RL

| Field | Detail |
|-------|--------|
| **Authors** | Pengcheng Li, Zhengyang Zhang, Dongxu Zhang, Sui Huang, Shaohua Ma |
| **Institution** | Not stated (industry research) |
| **Submitted** | 2026-08-28 · [2608.28128](https://arxiv.org/abs/2608.28128) · cs.LG |
| **Key contribution** | Fine-grained credit assignment in long-horizon agent RL usually broadcasts the terminal outcome to every action, and fix-attempts add rollout-side signals. **VICT** moves credit to the **verifier side**: many verifiable tasks already encode their checks inside the terminal verifier (evidence-backed atoms + dependency-valid proof edges). VICT traces those atoms back to responsible actions and redistributes group-relative advantage **only along proof edges**. Preserves the original terminal reward, abstains on ambiguous evidence, needs no critic / process labels / branch rollouts / inference-time verifier — only the training-time advantage tensor changes. Substantial gains over outcome-only training on ALFWorld/WebShop, at par with recent fine-grained credit methods; ablations rule out dense atom rewards, final-commit credit, temporal proximity, and sparsity as sufficient explanations. |
| **Why it matters** | Complements the OPD-reliability / reward-engineering thread from the *credit* side: instead of distrusting teacher signals, it mines the verifier's own structure — a third axis (verifier-tracing) alongside today's RA-OPD filter / VISTA adapt / SpikeOPD stabilize. "Credit assignment being re-engineered end to end" is the week's storyline. |

### DA3PO: Difficulty-Aware Advantage Amplification in Dynamic Sampling

| Field | Detail |
|-------|--------|
| **Authors** | Siyuan Gan, Yuhan Li, Xiran Wang, Linjian Meng, Boyan Wang, Zhen Zhao, Jing Huo, Lei Bai, Yang Gao |
| **Institution** | SJTU / Shanghai AI Lab *(inferred — Yang Gao's group, cf. RA-OPD same wave)* |
| **Submitted** | 2026-08-28 · [2608.27982](https://arxiv.org/abs/2608.27982) · cs.AI |
| **Key contribution** | DAPO's **Dynamic Sampling** (filter prompts whose samples are all-correct/all-incorrect → zero-advantage removal) is its biggest single gain over GRPO. Theory shows it **asymmetrically amplifies** advantages on hard prompts: incorrect responses get amplified more than correct ones, so the model learns to avoid observed bad outputs instead of exploiting hard-to-sample correct ones — low training efficiency. **DAA (Direct Advantage Amplification)** reweights the hard-to-sample correct responses; **DA3PO** = DAPO + DAA (~30 lines). Significantly outperforms GRPO, DAPO, and other GRPO variants. |
| **Why it matters** | Same lineage as RA-OPD — the group's "inspect the *advantage*, not the rollout" thesis. For the RLVR/OPD cluster it's a precision tool: prompt-level filtering (Dynamic Sampling) hides a prompt-level class bias that cheap advantage reweighting fixes. |

### HARTS: Efficient Agentic RL for Hybrid-Attention Models over Arbitrary Rollout Trees

| Field | Detail |
|-------|--------|
| **Authors** | Boyuan Meng, Peihua Bao, Hong Liu, Xiaowei Zhu, Chao Wang, Gen Li, Zhenxuan Pan |
| **Institution** | Ant Group *(stated)* |
| **Submitted** | 2026-08-28 · [2608.28158](https://arxiv.org/abs/2608.28158) · cs.LG |
| **Key contribution** | Agentic RL produces irregular rollout trees with shared histories; training root-to-leaf paths independently recomputes shared prefixes, and existing systems target full-attention only. **HARTS** jointly plans microbatches, DP replica assignment, and microbatch-slot schedules using non-replay compact-token work after prefix compression; for chunkwise linear attention it coordinates chunk-boundary state recovery/replay with a linear-time algorithm that produces the minimal sequential linear-attention call count under a packed execution model. Preserves chunkwise state partitioning of trajectory-wise training (no repeated projections / MLP/MoE / outputs; bounded state replay only), batches branches into one packed call, and restores per-token log-probabilities. **First** arbitrary-rollout-tree prefix-sharing speedup on a real hybrid-attention model: **4.81–4.87×** fwd/bwd/grad speedup (with activation recomputation) on an SWE-bench-derived agentic-RL workload; numerical diffs ≈ baseline self-rerun variance. |
| **Why it matters** | Systems-side enabler for agentic RL on *trees* not *trajectories* — dense prefix-sharing is where the win is. Directly relevant to the wiki's hybrid-attention architecture track (Gated DeltaNet / Mamba family): this is how you *train* those models agentically without exploding compute. |

### ReToolSQL: Agentic RL for Robust Text-to-SQL

| Field | Detail |
|-------|--------|
| **Authors** | Pratik Kakkar, Chandra Dhir, Ravi Shankar, Pareekshit Reddy Gaddam, Anup Shirgaonkar |
| **Institution** | Not stated (industry) |
| **Submitted** | 2026-08-28 · [2608.27796](https://arxiv.org/abs/2608.27796) · cs.AI |
| **Key contribution** | Most execution-feedback SQL work is single-turn, blocking iterative repair. **ReToolSQL**: (i) SFT warm-start on rejection-sampled reasoning traces + (ii) **agentic RFT over multi-turn tool-use trajectories** with execution-correctness rewards. The stages act on complementary axes — SFT from verified teacher traces *expands solvable coverage* (raises pass@k on hardest cases), RFT *converts* that into single-pass accuracy (when to verify, what to retrieve, how to repair faulty SQL). On Gemma 4 IT (31B): RFT alone 73.66% EX (BIRD-dev); SFT→RFT best at **74.32% EX single-pass / 74.77% self-consistency**, #1 on the BIRD single-model dev-set leaderboard at time of writing. No human annotation beyond the benchmark; single dense 31B. |
| **Why it matters** | Cleanest industrial-grade demo of the SFT-expand → RL-convert staging (cf. RA-OPD/OPD-reliability cluster) in text-to-SQL, and the verify→retrieve→repair tool loop generalizes agentic-RFT into a core enterprise scenario. |

---

## ③ Agent Safety & Monitoring (2)

### CURA: Certified Runtime Alarms for Computer-Use Agents

| Field | Detail |
|-------|--------|
| **Authors** | Divake Kumar, Sina Tayebati, Devashri Naik, Amanda Sofie Rios, Nilesh Ahuja, Omesh Tickoo, Ranganath Krishnan, Amit Ranjan Trivedi |
| **Institution** | University of Illinois Chicago + Intel Labs *(stated)* |
| **Submitted** | 2026-08-28 · [2608.27808](https://arxiv.org/abs/2608.27808) · cs.AI |
| **Key contribution** | Self-report (the cheapest oversight channel) fails where oversight matters: a capable CUA pipeline on 361 OSWorld tasks scores 82.9 (vs 72.4 human) yet **64/71 failures (90%) end in a success claim**, 61 acknowledge no blocker, and the failure affordance is never used in ~9,100 calls. **CURA** is an external monitor over only harness-visible telemetry (no model internals / extra LLM calls / prompt changes) that turns the trajectory into a **sequential test with certified false-alarm control**: CUSUM at α=0.10 detects 42.3% of failures a median 31 steps before termination at realized FPR 0.066. Alarm-gated mid-execution oversight recovers **23/70 failures** spending a frontier overseer on 38 → deployable cascade at mean score 86.8 / 84.5% full-solve. Certificate bounds false alarms only; also reports where behavioral monitoring is uninformative. |
| **Why it matters** | Quantitative anchor for the agent-safety thread: self-report is *provably* unreliable, but a cheap certified monitor + gated human oversight is deployable now — an alternative to trust-freezing or per-step frontier supervision. |

### Speculative Probing: LLM Monitoring at Speculative-Decoding Cost

| Field | Detail |
|-------|--------|
| **Authors** | Collin Zhang, Tingwei Zhang, Vitaly Shmatikov |
| **Institution** | Cornell Tech *(stated: Shmatikov)* |
| **Submitted** | 2026-08-28 · [2608.28099](https://arxiv.org/abs/2608.28099) · cs.AI |
| **Key contribution** | Real-time classification during inference (safety, behavior, monitoring) trades accuracy vs cost: hidden-state probes are fast but not context-aware; dedicated classifier LLMs / all-token pooling (MultiMax) are accurate but expensive. **Repurposes the spec-decoding module as a sequence classifier**: append a trained soft prompt at sequence end; classification runs on the KV cache already resident in GPU during speculative decoding → **negligible overhead**. Across 4 tasks × 4 models (Qwen3.5-4B/9B/27B, MiniCPM4.1-8B): small probes consistently beat zero-shot GPT-5.4-mini, and on multilingual prompt safety match/slightly beat specialized 8B safety classifiers (Qwen3Guard-Gen-8B, Llama-Guard-3-8B) without running a full LLM. |
| **Why it matters** | Turns a serving-stage detail (spec-decoding KV reuse) into an intelligent-monitoring primitive — "front-loading intelligence" (SparseRead/AgentWeave, 08-26) from the inference side: safety classification at ~zero marginal cost. |

---

## ④ Serving / Efficiency (2)

### PASK: Parser-Aware Structural KV Persistence for Structured Generation

| Field | Detail |
|-------|--------|
| **Authors** | Linze Wu, Xinrui Chen |
| **Institution** | Not stated |
| **Submitted** | 2026-08-28 · [2608.28276](https://arxiv.org/abs/2608.28276) · cs.LG |
| **Key contribution** | Structured generation (JSON/SQL/function calls) fails on one wrong field, yet KV compression ignores the parser's schema signals: constrained decoding *already* tracks parser transitions exposing which tokens matter for required fields / arguments / boundaries. **PASK** turns parser structure into **layer-group-specific KV persistence decisions** (task-error sensitivity → protection floors; attention-output distortion → residual budget allocation), compiled offline into a policy with a light structure-conditioned lookup online. At 0.33 total KV budget: **+17.39 pp average** over the strongest compressed baseline across 8 BFCL subcategories (Qwen3-4B); end-to-end up to **2.2× throughput, 3.3× lower TPOT, 0.53× peak GPU memory** vs Full KV. |
| **Why it matters** | KV compression normally pits budget vs reuse; PASK adds *task-structure* as a third axis. For the serving line (FlashPrefill, CacheRoute, TwinKV) it's schema-first persistence — exactly the tool/JSON calling load ranking sheets produce. |

### SOMTab: Set-Order Mamba for Efficient Tabular In-Context Learning

| Field | Detail |
|-------|--------|
| **Authors** | Hao Wang, Siyu Zhang, Wei Ma |
| **Institution** | Not stated |
| **Submitted** | 2026-08-28 · [2608.27882](https://arxiv.org/abs/2608.27882) · cs.LG |
| **Key contribution** | Tabular ICL foundation models are strong, but the frontier is attention-heavy — **is attention needed at every stage?** SOMTab separates representation construction from query-conditioned retrieval: row/column representations map unordered table tokens into stable latent slots + **Mamba state-space mixing** (compact, order-invariant); final prediction keeps attention-based ICL for query-conditioned retrieval. A synthetic prior **DCH-TailMix** (degree-corrected graph heterogeneity × heavy-tailed regimes) diversifies pretraining dependency structures. Approaches Transformer tabular-FM accuracy at **faster inference / lower GPU memory** — a favorable efficiency–accuracy trade-off. |
| **Why it matters** | Answers the hybrid-attention question for tabular/ICL: state-space for representation, attention only for retrieval. Feeds both the tabular-rec line and the wiki's linear/hybrid attention thread (LIME, Infinity, Gated-DeltaNet). |

---

## Honorable mentions (scanned, not featured)

| arXiv ID | Title | Category | One-line takeaway |
|----------|-------|----------|-------------------|
| [2608.27953](https://arxiv.org/abs/2608.27953) | The Illusion of What If: Evaluating the Breakdown of Counterfactual Reasoning in LLMs | cs.AI | WhatIfBench (220 open-domain causal questions) + PRISM causal-graph metrics; strongest frontier LLM hits only 64.62% — fluent counterfactual narratives mask fragile causal processes (premise drift, topology fragmentation). |
| [2608.28482](https://arxiv.org/abs/2608.28482) | How Proper Scoring Rules Shape LLM Forecasting | cs.LG | Five "equivalent" proper scoring rules as training objectives train visibly different LLM forecasters (calibration vs discrimination vs bias/information/noise profiles); Brier-trained lowest Brier/ROC, log-trained lowest calibration error — reward choice shapes not just performance but error structure. |
| [2608.28447](https://arxiv.org/abs/2608.28447) | Learning to Use Tools: RL for Tool-Integrated Mathematical Reasoning | cs.AI | Calculator tool calls for Countdown math: tool integration lifts both SFT and RL baselines ~10 pp; Tool-DAPO best (pass@1 35.8→66.0%), RL encourages tool use even under final-answer-only rewards. |
| [2608.28555](https://arxiv.org/abs/2608.28555) | QUEST: A Query and Extraction System for Topics in Asylum Law Applications | cs.IR | IR framing for credibility-factor extraction in Danish asylum appeals; credibility-based relevance assessment is significantly harder to measure than standard relevance. |
| [2608.27629](https://arxiv.org/abs/2608.27629) | LitCurate: AI-Assisted Scientific Database Construction | cs.IR | Stage-wise auditable LLM curation workflow; built a 1,334-entry lower-mantle equation-of-state database from 205 papers with provenance-aware labels. |

---

## Cross-Cutting Themes (2026-08-31 AI & CTR pass)

1. **Credit assignment is being re-engineered end to end.** VICT traces verifier atoms to responsible actions (structure inside the reward); DA3PO repairs a hidden class bias in DAPO's advantage; today's daily logged RA-OPD/VISTA/SpikeOPD on the distillation side. The week's shared claim: *raw scalars (terminal rewards, teacher likelihoods, group advantages) all leak credit, and each is being replaced by their internal structure.*
2. **Agent oversight goes certified & free-ish.** CURA gives provable false-alarm control on trajectory telemetry; Speculative Probing reuses the already-resident spec-decoding KV for classification. Both say "you can monitor agents at negligible marginal cost" — a deployment-ready alternative to judge-on-every-step.
3. **Retrieval/ranking keeps rediscovering two-stage structure.** PULSAR (pooled late-interaction: coarse pre-retrieve + exact rescore, 15× latency cut), SkillFeed (retrieve→rerank with profile-conditioned discrimination), and PASK (schema-aware KV floors) all exploit "cheap first pass, expensive precise pass" — the candidate-gen→rank pattern the ads/CTR line has used for a decade, now resurfacing in document RAG, skill routing, and KV serving.
4. **"Selectivity over fusion" extends to representation choice.** SOMTab keeps attention only for retrieval and Mamba for representation; NormasTCU shows judge *ranking* utility can diverge from pair-level fidelity. The shared move across multimodal-rec (HubMixer/AMUR), routing (SkillFeed), and tabular ICL: decide *where* to spend the expensive operation.

---

## Methodology

- **Listing source**: `arxiv.org/list/{cs.AI, cs.LG, cs.IR, cs.GT, cs.MA, cs.CL}/new` (Monday 31 Aug 2026 mailing), fetched via curl; per-paper metadata from live `arxiv.org/abs/...` pages.
- **Dedup**: every featured/HM ID grep-verified **absent** from `wiki/**` and cross-checked against the same-day `arxiv-daily` and `arxiv-ai-search` claimed-ID sets (listed in the header blockquote).
- **Window**: papers in the fresh `2608.27460–2608.28589` range whose submission dates fall on/before the Monday 31 Aug 2026 mailing (i.e. the last-24h to last-72h wave), excluding everything already claimed by siblings.
- **Temp files**: listings and abs pages under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/`; cleaned up when this report lands.
- **Coverage disclaimer**: proceedings/DOI-page citations rather than arXiv IDs could theoretically overlap; candidates were manually cross-checked against the 08-30/08-31 sibling reports and the known-ID set.

*Affiliations marked *(stated)* come from paper front matter; *(inferred)* = deduced from author identities / prior papers and remain tentative.*
