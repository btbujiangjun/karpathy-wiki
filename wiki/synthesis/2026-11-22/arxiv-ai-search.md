---
title: arXiv AI Search Report — 2026-11-22
type: synthesis
created: 2026-11-22
updated: 2026-11-22
sources: [arxiv.org]
tags: [arxiv, search, ai, llm, recommendation, advertising, ctr, sequential-modeling, games]
---

# arXiv AI Search Report — 2026-11-22

Query sweep via the arXiv search pages (`arxiv.org/search/`, sorted by `-announced_date_first`) over `recommendation OR advertising OR CTR OR "click-through rate" OR "sequential modeling"` and `games OR gaming OR "game AI" OR "game design"` (follow-up sweeps: `LLM OR "large language model" OR "foundation model" OR "generative model"`, `CTR`, `recommendation`, `advertising`). Submissions in the window 2026-11-11–2026-11-19; 18 papers, latest first.

Institution/Company lines are best-effort extractions from the paper abstracts — arXiv's HTML pages do not expose author affiliations. Papers without a stated institution/company are marked "Not listed in arXiv metadata."

---

## 1. AI / LLMs

### 1.1 TideCache: Efficient Hybrid LLM Serving with Transparent Cache Management and Layer-Wise Streaming
- **arXiv:** [2611.26619](https://arxiv.org/abs/2611.26619) [cs.DC; cs.LG] — 19 Nov 2026
- **Authors:** Jinbin Luo; Xiaozhe Yao; Shang Yang; Zhijian Liu; Song Han; Qinghao Hu
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Hybrid architectures have become mainstream among open-weight language models. Their global-attention and bounded-state layers maintain heterogeneous caches whose demands vary with context length and concurrency. We present TideCache, a serving system on CPU--GPU superchips with three components for allocating GPU memory among caches and managing their residency across GPU and host memory. The Transparent Cache Pool redistributes physical pages among cache components behind fixed virtual addresses, preserving cache layouts and backend interfaces. The Cache Streamer uses computation intervals provided by bounded-state layers to prefetch the next global-attention layer's prefix into GPU slots shared across global-attention layers, reducing GPU residency while overlapping layer-wise transfers with computation. Generated KV remains resident. The Request Scheduler selects resident or streamed execution and triggers capacity adjustments according to request size and queue state. Together, they let HBM released by streaming accommodate other cache components and additional requests. Implemented in SGLang and evaluated on GB300 and GH200 across seven model/platform configurations, TideCache completes up to 2.04x as many agent turns, reduces overall P50 per-token latency by 20--59%, and improves agent P50 TTFT by 1.40--3.05x compared with SGLang with HiCache.
- **Key innovations:**
  - Transparent Cache Pool: redistributes physical pages among heterogeneous caches behind fixed virtual addresses, preserving cache layouts and backend interfaces.
  - Cache Streamer: prefetches the next global-attention layer's prefix into GPU slots shared across global-attention layers using bounded-state layers' computation intervals, reducing GPU residency while overlapping transfers with computation.
  - Request Scheduler: selects resident vs streamed execution per request and triggers capacity adjustments by request size/queue state.
  - Results: up to 2.04x more agent turns, P50 per-token latency −20–59%, agent TTFT 1.40–3.05x vs SGLang + HiCache.

### 1.2 SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research
- **arXiv:** [2611.26601](https://arxiv.org/abs/2611.26601) [cs.CR; cs.AI; cs.SE] — 19 Nov 2026
- **Authors:** Amine Lbath; Manan Suri; Aurelien Delaitre; Vadim Okun; Massih-Reza Amini; Dinesh Manocha
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** LLM-based agents are becoming increasingly capable at discovering, validating and patching vulnerabilities in real software, and vendors and researchers report that this is already changing how vulnerabilities are found and fixed. These claims, however, are scattered across papers, vendor reports and disclosures and are rarely comparable. We introduce a framework that rates these capabilities on an autonomy scale modeled on the levels of driving automation, and qualifies each claim by its correctness, its availability and the strength of its evidence. We use this framework to systematize the published evidence on LLM capability in vulnerability research. We find that agents discovered, validated, and patched vulnerabilities in real-world software without human intervention before the restricted frontier models of 2026, and that open-weight models subsequently attained comparable autonomy for discovery and validation. We then measure the consequences of evolving LLM security capabilities in a decade of public vulnerability records, advisories and exploitation data. In 2026 the number of disclosed vulnerabilities more than doubled, with an increasing share rated critical or high, and severe bugs that had survived a decade or more in widely used code were reported several times more often than before. Yet the time between the stages of a vulnerability's life, from report to fix and from disclosure to attack, has not shifted noticeably so far. We grade the mitigations proposed in the literature with an explicit rubric and draw guidance for each group of stakeholders from the best-supported ones.
- **Key innovations:**
  - Autonomy-scale framework rating LLM agents on discover/validate/patch capability, qualified by correctness, availability and evidence strength.
  - Finds open-weight models attained discovery/validation autonomy comparable to pre-frontier models; 2026 saw >2x disclosed vulnerabilities.
  - Time from report to fix and from disclosure to attack unchanged over a decade of public records; rubric-graded mitigation guidance per stakeholder group.

### 1.3 Verify the Verifier: Specification-Grounded LLM Cross-Checking for Bugs That Escape UVM Scoreboards
- **arXiv:** [2611.26588](https://arxiv.org/abs/2611.26588) [cs.SE; cs.AI; cs.AR] — 19 Nov 2026
- **Authors:** Ana E. Sanchez Villalobos; Michael D. Quinn; Aakash Tyagi; Minh D. Luu; David Kebo Houngninou
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** A passing UVM regression shows the design agrees with the reference model on what the scoreboard checks, not that it meets the specification. Bugs that pass every test yet violate the specification, termed scoreboard escapes, survive mature testbenches. We present Verify the Verifier, to our knowledge the first framework whose LLM-based Anomaly Cross-Checker examines a passing regression's traces against the specification. Of 564 bugs inserted into four OpenTitan IPs, 68 are candidate scoreboard escapes: non-equivalent, exercised by the tests, yet passing. The framework confirmed 41 as scoreboard escapes with assertions failing on the buggy design and proven on the original.
- **Key innovations:**
  - First LLM-based Anomaly Cross-Checker: examines passing regression traces against the specification.
  - On 564 inserted bugs across 4 OpenTitan IPs: 68 candidates, 41 confirmed scoreboard escapes (assertions fail on the buggy design, proven on the original).

### 1.4 Closing Performance Gap for Diffusion Language Models under Low Inference Budgets
- **arXiv:** [2611.25763](https://arxiv.org/abs/2611.25763) [cs.CL; cs.AI; cs.LG; stat.ML] — 19 Nov 2026
- **Authors:** Hao Wu; Sipeng Chen; Jingwen Fu; Yuwang Wang
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Diffusion language models offer an architectural route to low-budget generation by updating multiple tokens in parallel, which can reduce the number of sequential decoding steps relative to token-by-token autoregressive decoding. However, realizing this advantage at low budgets is challenging, as generation quality often declines when the number of denoising and refinement steps is reduced. Editable diffusion models address this quality loss through post-draft refinement, but useful intermediate results may still be lost before final submission. We introduce CaRR (Commitment-aware Refinement and Recovery), a training-free framework which improves submission quality from a fixed editable checkpoint through updated-context refill and trajectory-based recovery within its existing forward schedule. Token Commitment Remasking (TCR) remasks selected native pure replacements and refills them on the next scheduled edit forward using the updated context. Submission Commitment Recovery (SCR) uses the resulting refinement trajectory to recover supported candidates when the final response does not satisfy task-specific output requirements. Both modules operate within the native mask/edit schedule without additional backbone forwards. Experiments on code generation and mathematical reasoning show consistent gains in average accuracy over native ME-DLM across four inference budgets, with the largest gains under tight budgets. At one-eighth of the full scheduled forward budget, CaRR improves the six-metric average accuracy by 7.44 pp, including gains of 11.37 and 10.05 on MBPP and MBPP+.
- **Key innovations:**
  - CaRR (Commitment-aware Refinement and Recovery): training-free framework — Token Commitment Remasking (TCR) refills native replacements with updated context on the next scheduled edit forward; Submission Commitment Recovery (SCR) recovers supported candidates from the refinement trajectory when the final response fails task-specific output requirements; both operate within the native schedule.
  - Gains within the native mask/edit schedule without extra backbone forwards; +7.44 pp average accuracy at 1/8 of the full forward budget (MBPP +11.37, MBPP+ +10.05).

### 1.5 How Much Should an Agent Remember? Deployment Lessons from Self-Distilled Memory for LLM Agents
- **arXiv:** [2611.26361](https://arxiv.org/abs/2611.26361) [cs.AI] — 19 Nov 2026
- **Authors:** K. R. Jayaram; Vatche Isahagian; Aswath Vaithinavan Aravindan; Vinod Muthusamy; Punleuk Oum; Gaodan Fang; Michal Ulewicz; Gegi Thomas; Evelyn Duesterwald
- **Institution/Company:** IBM
- **Abstract:** LLM agents on long-horizon tasks fail in recurring, procedural ways. They mis-paginate an API, resolve the wrong entity, or answer when no answer was asked. We built a pipeline that lets an agent learn from its own history. It first mines short lessons from the agent's own trajectories, one to three per episode. It then consolidates those lessons into a smaller set of guidelines, where each guideline records how many lessons it merged. At inference the agent receives either all guidelines or a selected subset. The pipeline ships in the open-source altk-evolve library and is deployed in IBM's CUGA agent and watsonx Orchestrate platform. We report what we learned building, measuring, and productizing it. Our primary instrument is the AppWorld benchmark, across models spanning 40--92% baseline task completion. The central finding is that the right amount of memory is a property of the model, not the memory. A strong model keeps improving as guidelines are added. DeepSeek-V3.2 gains +9.5 points of task completion and +16.1 points of scenario completion with its full 191-guideline set. A weak model gains less from the same full set than from a small selected subset. gpt-oss-120b starts at 39.9% task completion. It reaches 51.2% with all 199 of its guidelines but 55.4% (mean of two runs) with a selected subset of about 29. Around that result we report what went wrong: a high-support guideline that backfired, provenance silently dropped during consolidation, a swallowed API error that failed every task while producing a plausible log, and a baseline confound that nearly produced a misleading comparison with a prior method. We distill these into recommendations for teams deploying agent memory.
- **Key innovations:**
  - Self-distilled agent memory pipeline: mines 1–3 lessons/episode, consolidates into guidelines (recording merge counts), deploys all guidelines or a selected subset.
  - Finding: optimal memory amount is a property of the model — DeepSeek-V3.2 +9.5 task completion / +16.1 scenario completion with full 191-guideline set; gpt-oss-120b: 39.9→51.2 with all 199 guidelines vs 55.4 with selected ~29.
  - Productized via altk-evolve library; deployed in IBM CUGA agent and watsonx Orchestrate; AppWorld benchmark as primary instrument.
  - Production lessons: high-support guideline that backfired, provenance drops during consolidation, swallowed API error failing every task with plausible logs, confounded baseline.

---

## 2. Recommendation

### 2.1 Beyond Covers and Titles: Evidence-First Ranking for Robust Cold-Start Recommendation
- **arXiv:** [2611.26249](https://arxiv.org/abs/2611.26249) [cs.CV] — 19 Nov 2026
- **Authors:** Fuyi Wang; Yuxin Cao; Yifan Liao; Renyang Liu; Lin Li; Wei Song
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Short-video platforms rank new uploads before anyone has watched them, using content towers that read a video's cover, title and frames. Existing attacks on content-aware recommenders perturb pixels or features and ignore platform re-encoding, and existing defenses train against norm-bounded perturbations that neither match real edits nor preserve recommendation quality. We show with REAP, a realizable attack through {a simulated platform channel (H.264 transcoding, rescaling, cropping and JPEG)}, that packaging edits raise a cold video by 32.0 rank-percentile points in unrelated audiences. We then observe that cold-start ranking does not need the packaging at all: a tower that sees only the video body ranks cold items best. Building on this, we propose Evidence-First Ranking (EFR), which scores cold videos from their body, admits packaging only through a support-gated residual bounded by γ, and merges cold and warm rankings by rank percentile, yielding an exact certificate against any packaging edit. On MicroLens-100K, EFR cuts the attack gain by 81% and raises cold-start Recall@100 from 0.1133 to 0.170, while keeping the merged NDCG@10 within 4% of the undefended system.
- **Key innovations:**
  - REAP attack: packaging edits realized through a simulated platform channel (H.264 transcoding, rescaling, cropping, JPEG) raise cold videos by 32.0 rank-percentile points.
  - Evidence-First Ranking (EFR): body-only tower for cold videos; support-gated residual; rank-percentile merge of cold/warm rankings → exact certificate against any packaging edit; cuts attack gain by 81%, Recall@100 0.1133→0.170, NDCG within 4% of undefended.

### 2.2 From Sessions to Serving: Integrating LLM-Based Embeddings into Retrieval for Production Content Recommendation (LSER)
- **arXiv:** [2611.26096](https://arxiv.org/abs/2611.26096) [cs.IR; cs.LG] — 19 Nov 2026
- **Authors:** Zhixiong Hu; Meng Li; Maggie Zhang; Deborshi Goswami; David Bailey; James Bradley
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Personalized content recommendation on large marketplace websites must reconcile heterogeneous candidate content (e.g., customer stories, product pages, industry pages, and learning content) with sparse, fast-changing user behavior, placing increasing demands on the retrieval stage to represent user interest well, not just the downstream ranking stage. We present LSER (LLM Session Embedding Retrieval), a production content recommendation system for this marketplace that derives session- and history-level embeddings from a pretrained large language model (LLM) and adds them as auxiliary user-side features in the retrieval-stage user tower alongside existing learned sequence encoders. To keep user-side embeddings fresh under real-time behavior, we build a nearline serving path that asynchronously refreshes sequential and LLM-derived user vectors for our main content recommendation server. We validate the incremental value of the LLM features through an ablation study across our full multi-content-type catalog. Our results indicate that integrating LLM-derived embeddings as additional retrieval signals, together with production-grade nearline serving, is technically feasible and can improve model performances.
- **Key innovations:**
  - LSER (LLM Session Embedding Retrieval): pretrained-LLM-derived session/history embeddings as auxiliary user-side features in the retrieval-stage user tower, extending learned sequence encoders.
  - Production-grade nearline serving path that asynchronously refreshes sequential and LLM-derived user vectors in real time.
  - Ablation across a full multi-content-type catalog (customer stories, product pages, industry pages, learning content) validates incremental value of the LLM retrieval features.

---

## 3. CTR

### 3.1 DNA: Unlocking Depth Scaling in CTR Models
- **arXiv:** [2611.25659](https://arxiv.org/abs/2611.25659) [cs.IR] — 19 Nov 2026
- **Authors:** Caiyuan Li; Wenjie Wu; Yuheng Huang; Xiao Zhou; Silu Zhou; Ke Chen; Zinan Zhao; Xinrui Zeng; Hanmo Xu; Chaoqun Song; Hua Zong; Zongyuan Wu; Hongbin Zhou; Huimin Yi; Zhixuan Zhang; Dan Ou; Haihong Tang
- **Institution/Company:** Taobao
- **Abstract:** Long user behavior sequences are among the strongest signals for click-through rate (CTR) prediction. Cross-attention makes these sequences practical for industrial ranking by keeping compute linear in sequence length. Yet the gains from stacking cross-attention layers taper off: on Taobao search, growing a cross-attention stack from 16 to 28 layers adds only 0.02 percentage points (pt) of AUC. We argue that the key-value side is the bottleneck. Each layer projects the same behavior sequence into keys and values, so adding depth gives the model more reads of a fixed sequence. We propose DNA (Dual-stream Nexus Attention), which lets the sequence itself evolve with depth. At each layer, the request representation (the search query, user features and scene) first reads the sequence. Each behavior token then attends to the updated request representation and uses what it reads to update itself, so the next layer reads a sequence shaped by the current request. The update runs once per request, all candidates share the resulting sequence, and both the reads and the update keep linear complexity in sequence length. At comparable forward FLOPs, DNA improves AUC over cross-attention stacks by 0.08 to 0.26 pt and keeps improving in the depth range where those stacks level off. DNA-4 is deployed in Taobao search. In an online A/B test against the production model, it improves CTR by 0.8% and GMV by 0.5%.
- **Key innovations:**
  - DNA (Dual-stream Nexus Attention): request representation reads the behavior sequence each layer; each token attends to the updated request and updates itself — the sequence evolves with depth, shaped by the current request; reads and update both linear in sequence length, run once per request, shared by all candidates.
  - Depth scaling: beats the cross-attention stack exactly where it tapers off (AUC +0.08–0.26 pt at comparable FLOPs).
  - DNA-4 deployed in Taobao search: online A/B CTR +0.8%, GMV +0.5%.

### 3.2 X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction
- **arXiv:** [2611.24283](https://arxiv.org/abs/2611.24283) [cs.IR] — 18 Nov 2026
- **Authors:** Alexander Ploshkin; Nikita Stepanov; Alexey Pismenny; Viacheslav Ovchinnikov; Nikolay Savushkin
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Accurate click-through rate (CTR) prediction depends on user representations that capture both persistent preferences and recent intent, yet processing extensive behavioral histories for every ranking request is costly under production compute and latency constraints. We present X-split ARGUS, a framework for ad ranking whose history compressor and online ranker are trained end to end. The compressor encodes past interactions into a compact set of tokens that are computed offline and reused across candidates, while the online ranker scores ads through cross-attention to these tokens and representations of recent events. Training combines an autoregressive loss for click feedback with distillation of candidate-specific click logits from a larger teacher that scores each candidate using the uncompressed history. The number of compressed history tokens and the length of recent history can be adjusted to fit serving compute and latency budgets. Offline evaluation shows a 0.81% relative reduction in normalized entropy (NE) compared with the production baseline. Deployment in a large-scale real-time bidding system increases online inference cost by 15% relative to the production baseline. An online A/B test against this baseline yields relative gains of 4.65% in a business metric reflecting the monetary value of conversions generated for advertisers and 2.96% in clicks.
- **Key innovations:**
  - X-split ARGUS: offline history compressor → reusable token set; online ranker cross-attends to compressed history + recent events; trained end-to-end (autoregressive click loss + teacher distillation).
  - Tunable compressed-token count and recent-history length to fit compute/latency budgets; offline NE −0.81% vs production.
  - Deployed in real-time bidding: online inference +15% cost; A/B: +4.65% advertiser-value, +2.96% clicks.

### 3.3 Serving-Aligned Entire-Space Conversion Modeling via Click-Through Rate Knowledge Distillation
- **arXiv:** [2611.15137](https://arxiv.org/abs/2611.15137) [cs.LG] — 11 Nov 2026
- **Authors:** Pavel Dolin; Xun Zou; Jiatian Wu; Deguang Kong
- **Institution/Company:** Ali-CCP
- **Abstract:** Recommendation systems may use predicted click-through conversion rate (pCTCVR), the product of predicted click-through rate (pCTR) and post-click conversion rate (pCVR), to guide ranking decisions. Many pCVR models build on the Entire Space Multi-Task Model (ESMM), which jointly trains pCVR and auxiliary pCTR towers using pCTR and pCTCVR losses, but deploys only the pCVR tower. At serving time, this tower may be paired with a separately trained pCTR model, creating a training-serving mismatch in pCTCVR when its predictions differ from those of the auxiliary pCTR tower. In this paper, we use knowledge distillation (KD) from logged serving pCTR scores to supervise ESMM's auxiliary pCTR tower and improve training-serving pCTCVR alignment. We denote variants by KD-α, where α controls the hard-label loss weight. On the Ali-CCP dataset, KD-0.3, the best variant on serving pCTCVR, increases ROC-AUC not only for serving pCTCVR but also for pCVR by 2.1% and 1.6%, respectively, and PR-AUC by 9.9% and 8.8%, respectively, relative to the ESMM baseline. We also test negative downsampling with 5% nonclick retention. Downsampled KD-0.3 increases mean AUC for serving pCTCVR and pCVR by 1.2% and 0.9%, respectively, -and PR-AUC by 8.5% and 4.5%, respectively, relative to downsampled ESMM.
- **Key innovations:**
  - KD-α: distills logged serving pCTR scores into ESMM's auxiliary pCTR tower to align training-serving pCTCVR when the auxiliary tower's predictions differ from the serving pCTR model.
  - KD-0.3 on Ali-CCP: serving pCTCVR AUC +2.1%, pCVR AUC +1.6%, PR-AUC +9.9%/+8.8% vs ESMM.
  - Downsampled variant retains gains (pCTCVR AUC +1.2%, PR-AUC +8.5% at 5% nonclick retention).

---

## 4. Sequential Modeling

### 4.1 Sequential Anytime Valid Tests for Efficient Inference-Time Alignment
- **arXiv:** [2611.26413](https://arxiv.org/abs/2611.26413) [cs.LG] — 19 Nov 2026
- **Authors:** Vishesh Kumar Singh; Sayak Ray Chowdhury
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Inference-time alignment methods, such as Best-of-N (BoN), improve language model outputs by generating multiple candidates per prompt and selecting among them using a reward model. Much of this cost is wasted: a fixed budget is applied to every prompt, although the computation required by prompts varies widely. Adaptive methods halt once sampled answers appear settled, but their thresholds are tuned heuristics with no statistical control over early-stopping errors. We instead seek an anytime-valid stopping rule that takes an error tolerance α as input and halts only once an answer is certified to hold a majority (θ_a > 1/2) under the generator's distribution. We aggregate candidates by final answer with a reward-weighted self-consistency (RWSC) score and treat stopping as a sequential test over the resulting clusters. Applying Wald's sequential probability ratio test to these clusters yields SPRT-RWSC, which performs well empirically, but its guarantee fails because the leading answer shifts during sampling, and the run is continuously monitored. Our main contribution, e-RWSC, replaces Wald's test with a betting supermartingale (an e-process) for every answer the policy produces, bounding the probability of ever certifying a non-dominant answer by α, uniformly over time and across all answers. The RWSC scores drive the bets, so they affect only how quickly a dominant answer a* is certified, not validity; certification takes O(log(1/α)/D_KL(θ_a*||1/2)) samples. Experiments across several language models, datasets, and reward models confirm the predicted 1/D_KL scaling of cost and show that accuracy improves over baselines at substantially lower token cost.
- **Key innovations:**
  - e-RWSC: reward-weighted self-consistency (RWSC) clusters as evidence base; betting supermartingale (e-process) per possible answer — bounds ever-certifying a non-dominant answer by α (anytime-valid, uniform over time and answers).
  - Certification cost O(log(1/α)/D_KL(θ_a*||1/2)) samples — empirically confirmed.
  - Improves accuracy over baselines at substantially lower token cost across LMs, datasets and reward models (SPRT-RWSC baseline's guarantee noted as failing).

### 4.2 Realized versus Population Reliability: Anytime-Valid Self-Consistency Certification under Correlated Reasoning
- **arXiv:** [2611.26592](https://arxiv.org/abs/2611.26592) [stat.ME; cs.AI; cs.LG] — 19 Nov 2026
- **Authors:** Terence D. Agbeyegbe; Toneukarin G. Agbeyegbe
- **Institution/Company:** Anthropic (via Claude Haiku 4.5 rollouts)
- **Abstract:** Self-consistency certification treats repeated sampling from a language model as sequential evidence accumulation and stops when an anytime-valid e-process crosses a threshold, guaranteeing finite-sample Type I error control by Ville's inequality. Prior constructions assume sampled rollouts are conditionally independent. We show this assumption fails in practice: reasoning streams are positively correlated through shared reasoning prefixes or across-prompt heterogeneity, changing not merely certificate efficiency but the hypothesis certified. Modeling dependence via a per-unit latent state (the random-effects / intraclass-correlation structure) induces exchangeable, equi-correlated increments with correlation ρ. Correlation splits the single null into a realized null about the drawn belief and a population null about average model behavior, which coincide only when ρ=0. We show: (i) the standard betting e-process remains anytime-valid for the realized null, not the population null; (ii) read as a population-null test, a suitable mixture has asymptotic crossing probability at least π=P(μ(Z)>0), potentially exceeding nominal ε; (iii) the within-unit mean's effective sample size saturates at 1/ρ, so extra within-unit rollouts cannot restore population validity; and (iv) a prompt-level e-process restores population validity, with optimal allocation at one rollout per prompt under a pure rollout budget. Simulations and Claude Haiku 4.5 rollouts confirm this regime dependence: on GSM8K (ρ̂=0.435, θ̂=+0.96) the gap is dormant, whereas on AIME (ρ̂=0.480, θ̂=−0.15) the single-unit rule crosses on 24% of prompts at nominal ε=0.05, while the prompt-level procedure declines (0.00). This correctness result identifies which reliability claim an anytime-valid certificate actually supports under dependence.
- **Key innovations:**
  - Splits anytime-valid certification into a realized null (drawn belief) vs population null (average behavior) — coincide only at ρ=0; standard e-process is valid for the realized null but not the population null (mixture crossing probability ≥ P(μ(Z)>0)).
  - Within-unit mean effective sample size saturates at 1/ρ — extra rollouts can't restore population validity.
  - Prompt-level e-process restores population validity, optimal allocation = one rollout per prompt under a pure rollout budget.
  - Simulations + Claude Haiku 4.5: on GSM8K gap dormant (ρ̂=0.435, θ̂=+0.96); on AIME single-unit crosses on 24% of prompts at ε=0.05, prompt-level 0.00.

---

## 5. Advertising / Auto-bidding

### 5.1 GEOHunter: Mapping a Generative Engine Optimization Network in the Wild
- **arXiv:** [2611.26564](https://arxiv.org/abs/2611.26564) [cs.CR; cs.AI; cs.SI] — 19 Nov 2026
- **Authors:** Sean Tang; Peiran Wang; Ying Li; Esha Shivakumar; Tao Meng; Yuan Tian
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Generative engines synthesize retrieved web pages into answers, recommendations, and rankings. Generative engine optimization (GEO) services sell visibility in these answers by publishing promotional articles on user-generated-content (UGC) platforms for paying clients. Such promotion raises concerns in medical and financial domains, where misleading advice can cause harm. To study the severity of this problem, we measure one such paid-content operation across three major Chinese UGC platforms, uncovering 1,985 accounts associated with the network comprising 466,357 inferred promotional placements. We find that the network promotes products across diverse categories through a growing pool of accounts, conducting coordinated campaigns spanning months across multiple platforms while evolving its listicle content over time. Across nine generative engines from both the US and China, we find that 4.5% to 20% of retrievable cited pages are attributable to the network, depending on how strictly attribution is drawn. On eight of these engines, its clients are named in 52% of answers, against 68% for category leaders. Our work demonstrates the effectiveness of UGC GEO placement at influencing generative engine outcomes, and reveals content-level defenses as insufficient against coordinated UGC placements, where account-level and platform-level signals are necessary for proper defense.
- **Key innovations:**
  - First large-scale characterization of a paid UGC GEO network: 1,985 accounts, 466,357 inferred placements across 3 Chinese UGC platforms over months.
  - Attribution methodology across 9 generative engines (US+China): 4.5–20% of retrievable cited pages attributable (strictness-dependent).
  - Clients named in 52% of answers on 8 engines vs 68% for category leaders — effectiveness of UGC GEO; reveals content-level defenses insufficient vs account/platform-level signals (medical/financial domains at risk).

### 5.2 Iterative Scarcity-Guided Exploration (ISGE): Bootstrapping Generative Auto-bidding from Narrow Support
- **arXiv:** [2611.26060](https://arxiv.org/abs/2611.26060) [cs.LG] — 19 Nov 2026
- **Authors:** Qingmao Yao; Guangzheng Hu; Yusen Huo; Zhilin Zhang; Chuan Yu; Jian Xu; Xu Chu; Bo Zheng; Xiaotie Deng
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Auto-bidding is a core algorithmic component in online advertising auctions. In practical cold-start settings, iterative training is commonly used to compensate for low-quality, narrowly supported historical data. Unfortunately, in iterative training, representative diffusion-based AI-Generated Bidding (AIGB) methods fail to sustain extrapolation beyond the narrow data support and stagnate at a suboptimal level. In this paper, we theoretically attribute this stagnation to Signal-to-Noise Ratio (SNR) collapse: the weak radial return signal is overwhelmed by a curvature-induced penalty. To break this stagnation, we propose Iterative Scarcity-Guided Exploration (ISGE), which introduces a guidance handoff: as the return signal collapses, scarcity subsequently takes over as an exploratory signal to elevate the SNR above a critical threshold. Specifically, ISGE iteratively alternates between a Judger that assigns scarcity scores to trajectories and an Explorer that performs guided generation of high-scarcity and high-return trajectories, thereby bootstrapping from the narrow support with such self-generated trajectories. Extensive experiments on the industrial AuctionNet benchmark demonstrate that ISGE, starting from cold-start datasets, effectively surpasses the performance of the Full-Dataset baseline within three iterations. Code is available at this https URL.
- **Key innovations:**
  - Theory of SNR collapse in iterative AIGB training: weak radial return signal overwhelmed by curvature penalty → stagnation below optimal cold-start support.
  - ISGE: Judger (scarcity scores) + Explorer (guided generation of high-scarcity/high-return trajectories); guidance handoff — scarcity takes over as exploratory signal when SNR drops below the critical threshold, lifting it above.
  - AuctionNet: ISGE from cold-start reaches Full-Dataset baseline performance within 3 iterations.

### 5.3 CutAgent: Creative-Gene-Driven Planning and Experience-Guided Self-Refinement for High-CTR E-commerce Advertising Video Creation
- **arXiv:** [2611.22418](https://arxiv.org/abs/2611.22418) [cs.CV] — 17 Nov 2026
- **Authors:** Xuyue Huang; Guanbo Huang; Jiasong Feng; Run Ling; Ao Ma; Xi Zhao; Yaoyu Li; Jie Gao; Ke Cao; Wei Feng; Zhanjie Zhang; Hao Wang; Jinghe Hu
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** E-commerce advertising video creation requires both high-level creative planning and reliable multi-modal production. However, existing methods often map product attributes directly to scripts or editing decisions without explicitly modeling advertising strategies, narrative structures, and production styles. They also have limited ability to reuse past production failures. To address these limitations, we propose CutAgent, a dual-agent framework that formulates advertising video creation as a Plan--Execute--Self-Evolve process. CutAgent comprises two collaborative agents, GeneAgent and VideoAgent, connected by a structured creative gene that bridges product understanding and video production. GeneAgent maps multi-modal product inputs---textual attributes together with product images---to creative genes that specify narrative units and production rules. To train GeneAgent, we construct CutAgent-70K with approximately 70K samples of product attributes/images, reverse-extracted creative genes, cleaned clip pools, and real-world CTR, and apply high-CTR supervised fine-tuning followed by CTR-guided GRPO. Guided by the generated gene, VideoAgent retrieves category-then-gene failure--correction experiences from a long-term memory as constraints for shot-script planning, then coordinates material retrieval, narration, subtitles, music, and timeline rendering. Independently, a reflection loop diagnoses quality defects, revises deficient production decisions, and writes verified corrections back to memory for later retrieval. Experiments on CutAgent-Eval show that CutAgent outperforms representative baselines in e-commerce advertising video creation, achieving the highest online CTR of 2.21%.
- **Key innovations:**
  - CutAgent: dual-agent Plan–Execute–Self-Evolve framework (GeneAgent + VideoAgent connected by a structured creative gene; real-world CTR in training data).
  - CutAgent-70K: ~70K product/image samples with reverse-extracted creative genes + cleaned clip pools + real CTR labels; high-CTR SFT + CTR-guided GRPO training.
  - VideoAgent: retrieves category-then-gene failure–correction experiences from long-term memory as shot-script planning constraints; reflection loop revises deficient decisions and writes verified corrections back to memory.
  - CutAgent-Eval: beats baselines, highest online CTR 2.21%.

---

## 6. Games

### 6.1 PlayCraft: Designing Engaging Games from Agent Play Experience
- **arXiv:** [2611.26624](https://arxiv.org/abs/2611.26624) [cs.AI; cs.CV] — 19 Nov 2026
- **Authors:** Weihao Cheng
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Recent AI agents can generate playable games, but these games are not necessarily engaging. Mastery is a key source of engagement, yet designing for it requires extensive human play and tuning. We propose PlayCraft, an automated framework that uses a vision-based agent to play games and draws on its detailed play experience to revise them for mastery. Starting from an initial game, PlayCraft alternates between playing and crafting. In the playing stage, a player agent watches the game screen, uses the controls, and pursues the game objective over repeated episodes while retaining memory. After each episode, it reports its progress, outcomes, decisions, and reflections. In the crafting stage, a crafter agent uses these reports to revise the game. It estimates player abilities, predicts performance at different proficiency levels, and compares those predictions with a target learning progression. It diagnoses the game and addresses the gaps by giving players meaningful opportunities to improve through better decisions and execution. We evaluate games in fresh runs with player agents across three intelligence settings, measuring learning gain and learning slope. Compared with the initial games, PlayCraft yields larger learning gains and steeper learning slopes in most games. It also outperforms the baselines on the macro-average of each metric at every intelligence setting.
- **Key innovations:**
  - Play–Craft alternation: vision-based player agent reports progress/outcomes/decisions/reflections → crafter agent estimates abilities, predicts performance across proficiency levels, diagnoses gaps, and gives players improvement opportunities via game revisions.
  - Evaluation across three intelligence settings measuring learning gain + learning slope; PlayCraft > initial games and baselines on macro-average at every setting.

### 6.2 Optimal Patrol Widths in the Infinite-Corridor Barrier-Guarding Game
- **arXiv:** [2611.26140](https://arxiv.org/abs/2611.26140) [math.OC; math.MG] — 19 Nov 2026
- **Authors:** Kevin M. Boergens
- **Institution/Company:** MIT
- **Abstract:** A guard of speed at most one and capture radius r patrols an infinite corridor. An intruder knows the patrol and can follow any path of speed at most q from one end to the other. We determine where the maximum width permitted by straight wall runners can be guarded against all such paths. Write W_opt(q) for the supremum over patrols with bounded longitudinal excursion and F(q)=2r√(1+(3q²+2q−1)⁻¹) for the wall ceiling on 1/3 < q < 1. A four-leg bowtie attains F(q) exactly for q_a≤q<1, where 0.457892036651 < q_a < 0.457892036652. For every 1/3 < q < q_a the supremum is strictly smaller. As q approaches q_a from below, F(q)−W_opt(q) is bounded above and below by positive constant multiples of r(q_a−q)². The lower estimate controls near-optimal patrols uniformly in their period. A rescaled bowtie gives the matching upper estimate. We also prove that periodic patrols give the same supremum as bounded-excursion patrols. For q≥1 the one-way optimum is r√(4+q⁻²), a transverse sweep. This sweep is optimal against transit in both directions for q≥1/2. At low speeds, q·W_opt(q)/r tends to two, and an explicit ten-leg patrol guards width greater than (2/q−1.235353)r throughout 0<q≤1/40. Rational spacetime and flux certificates give finite-speed bounds, including 6.944691333740r < W_opt(1/4) ≤ 8.10r.
- **Key innovations:**
  - Closed-form optimal patrol width W_opt(q) for the infinite-corridor barrier-guarding game (guard speed ≤1, capture radius r, intruder speed ≤q), with wall ceiling F(q)=2r√(1+(3q²+2q−1)⁻¹) for 1/3<q<1.
  - Four-leg bowtie patrol attains F(q) exactly for q_a≤q<1 (q_a≈0.457892036651–2); for q<q_a the supremum is strictly smaller; near-optimal gap F(q)−W_opt(q) ∈ Θ(r(q_a−q)²).
  - Periodic ≡ bounded-excursion sup; low-speed law q·W_opt(q)/r→2; ten-leg patrol guards >(2/q−1.235353)r for q≤1/40.
  - Rational spacetime/flux certificates giving finite-speed bounds (6.94–8.10r at q=1/4).

### 6.3 Control of Complex Social Systems via Committed Minorities and Opinion Broadcast
- **arXiv:** [2611.26092](https://arxiv.org/abs/2611.26092) [eess.SY; cs.SI; math.DS; math.OC] — 19 Nov 2026
- **Authors:** Roberta Raineri; Mengbin Ye; Lorenzo Zino
- **Institution/Company:** MIT
- **Abstract:** Complex social systems are often characterized by a deep interconnection between individuals' opinion formation and their decision-making processes. In this chapter, we show how these two dynamics can be incorporated within a unifying game-theoretic coevolutionary model for actions and opinions. We present the main theoretical results concerning the convergence of the coevolutionary model, and its recent extensions to incorporate further features of real-world social systems. Then, we focus on the problem of controlling such a coevolutionary model. In particular, we present two distinct approaches: i) introducing a committed minority in the population, and ii) broadcasting information to some target individuals. For both of these methods, we discuss their implementation and provide theoretical guarantees on their performance. Finally, we demonstrate the effectiveness of the proposed control methods on different case studies, illustrating their implementation on simple academic examples, as well as exploring their performance in realistic scenarios using network structures inferred from real-world data. In summary, this chapter provides an overview of the mathematical approaches developed to model a population of individuals with coevolving actions and opinions, providing effective tools to study and, ultimately, control this complex socio-technical system.
- **Key innovations:**
  - Unifying game-theoretic coevolutionary model of actions+opinions with convergence results and extensions for real-world features.
  - Two control methods — committed minority (i) and information broadcast (ii) — with theoretical performance guarantees.
  - Effectiveness demonstrated on academic case studies + realistic scenarios using data-inferred network structures.

---

Related: [[ctr-scaling-landscape]], [[affiliation-landscape]], [[technical-roadmap]].
