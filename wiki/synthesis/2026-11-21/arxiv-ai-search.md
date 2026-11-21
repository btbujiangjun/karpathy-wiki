---
title: "arXiv AI Search Report — 2026-11-21"
type: synthesis
created: 2026-11-21
updated: 2026-11-21
sources: [arxiv.org]
tags: [arxiv, search, ai]
---

# arXiv AI Search Report — 2026-11-21

Query sweep via the arXiv Atom API (`export.arxiv.org/api/query`, sorted by `submittedDate`). Queries: `all:(LLM OR "large language model" OR "foundation model")`, `all:recommendation`, `all:advertising`, `all:"sequential modeling"`, `all:CTR`, `all:(games OR gaming OR "game AI" OR "game design")`. Papers sorted by recency (latest submissions 2026-11-19).

Institution/Company lines are best-effort extractions from the paper abstracts — arXiv's Atom API and HTML pages do not expose author affiliations. Papers without a stated institution/company are marked "Not listed in arXiv metadata." No dedicated CTR papers were found in this sweep; CTR-relevant coverage is in Section 2 (recommendation).

---

## 1. AI / Large Language Models

### 1.1 TideCache: Efficient Hybrid LLM Serving with Transparent Cache Management and Layer-Wise Streaming
- **arXiv:** [2611.26619](https://arxiv.org/abs/2611.26619) [cs.DC; cs.LG] — 19 Nov 2026
- **Authors:** Jinbin Luo, Xiaozhe Yao, Shang Yang, Zhijian Liu, Song Han, Qinghao Hu
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Hybrid architectures have become mainstream among open-weight language models. Their global-attention and bounded-state layers maintain heterogeneous caches whose demands vary with context length and concurrency. We present TideCache, a serving system on CPU--GPU superchips with three components for allocating GPU memory among caches and managing their residency across GPU and host memory. The Transparent Cache Pool redistributes physical pages among cache components behind fixed virtual addresses, preserving cache layouts and backend interfaces. The Cache Streamer uses computation intervals provided by bounded-state layers to prefetch the next global-attention layer's prefix into GPU slots shared across global-attention layers, reducing GPU residency while overlapping layer-wise transfers with computation. Generated KV remains resident. The Request Scheduler selects resident or streamed execution and triggers capacity adjustments according to request size and queue state. Together, they let HBM released by streaming accommodate other cache components and additional requests. Implemented in SGLang and evaluated on GB300 and GH200 across seven model/platform configurations, TideCache completes up to 2.04x as many agent turns, reduces overall P50 per-token latency by 20--59%, and improves agent P50 TTFT by 1.40--3.05x compared with SGLang with HiCache.
- **Key innovations:**
  - Transparent Cache Pool: physical pages redistributed among heterogeneous caches behind fixed virtual addresses, preserving cache layouts and backend interfaces.
  - Cache Streamer: prefetches the next global-attention layer's prefix into GPU slots shared across global-attention layers, using bounded-state layers' computation intervals; reduces GPU residency while overlapping layer-wise transfers with computation.
  - Request Scheduler: selects resident vs streamed execution per request and triggers capacity adjustments by request size/queue state.
  - Results: up to 2.04x more agent turns, P50 per-token latency −20–59%, agent TTFT 1.40–3.05x (vs SGLang + HiCache).

### 1.2 Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)
- **arXiv:** [2611.26553](https://arxiv.org/abs/2611.26553) [cs.CR; cs.AI; cs.MA] — 19 Nov 2026
- **Authors:** Mengxiao Wang, Mahbub Alam, Kalyan Nakka, Nitesh Saxena
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only says what went wrong and rarely (in)validates the incident or finds its root cause. Incident catalogs collect these reports, and benchmarks record whether agents fail, but neither replicates an incident nor tests the cause its report might identify. In this paper, we present ROGUE-AI (Replication of Agentic Security Events: Audit and Investigation), a multi-agent framework that closes the above gap and rebuilds each reported incident offline together with a matched control that lacks only the blamed cause, and runs agents on both. Our results suggest that ROGUE-AI is able to reproduce the reported harm in 89% of its 108 attempted replications. Agents built on five current GPT, Claude, Gemini and DeepSeek models made the reported mistake in 18% to 33% of runs, against at most 1% without the blamed cause. Of the 72 incidents with real-world harm, 62 had no underlying attacker, and in these, agents did what their task asked for but missed an ordinary hazard, such as a database shared with the live site. Replications without an attacker caused more harm than replications of prompt injection for all five models. Defenses against prompt injection look for injected instructions, but these replications contain none. Further, a warning after each tool output that names the hazard and its consequence lowered harm for all five models, whereas a note of the same length that does not mention the hazard left most of the harm in place. Built from real incidents, the ROGUE-AI replications form a reusable audit framework that vendors can rerun before each new release.
- **Key innovations:**
  - Multi-agent replication framework (ROGUE-AI) that rebuilds real-world agentic incidents offline with matched controls lacking the blamed cause, reproducing reported harm in 89% of 108 attempts.
  - 5 current LLM families tested: reported mistakes in 18–33% of runs vs ≤1% without the cause.
  - Diagnoses most real-world harm as ordinary hazards (e.g., database shared with the live site), not prompt injection; hazard-naming warnings lowered harm on all five models.

### 1.3 SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research
- **arXiv:** [2611.26601](https://arxiv.org/abs/2611.26601) [cs.CR; cs.AI; cs.SE] — 19 Nov 2026
- **Authors:** Amine Lbath, Manan Suri, Aurelien Delaitre, Vadim Okun, Massih-Reza Amini, Dinesh Manocha
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** LLM-based agents are becoming increasingly capable at discovering, validating and patching vulnerabilities in real software, and vendors and researchers report that this is already changing how vulnerabilities are found and fixed. These claims, however, are scattered across papers, vendor reports and disclosures and are rarely comparable. We introduce a framework that rates these capabilities on an autonomy scale modeled on the levels of driving automation, and qualifies each claim by its correctness, its availability and the strength of its evidence. We use this framework to systematize the published evidence on LLM capability in vulnerability research. We find that agents discovered, validated, and patched vulnerabilities in real-world software without human intervention before the restricted frontier models of 2026, and that open-weight models subsequently attained comparable autonomy for discovery and validation. We then measure the consequences of evolving LLM security capabilities in a decade of public vulnerability records, advisories and exploitation data. In 2026 the number of disclosed vulnerabilities more than doubled, with an increasing share rated critical or high, and severe bugs that had survived a decade or more in widely used code were reported several times more often than before. Yet the time between the stages of a vulnerability's life, from report to fix and from disclosure to attack, has not shifted noticeably so far. We grade the mitigations proposed in the literature with an explicit rubric and draw guidance for each group of stakeholders from the best-supported ones.
- **Key innovations:**
  - Autonomy-scale framework rating LLM agents on discover/validate/patch capability, qualified by correctness, availability and evidence strength.
  - Finds open-weight models attained discovery/validation autonomy comparable to pre-frontier models; 2026 saw >2x disclosed vulnerabilities.
  - Time from report to fix and from disclosure to attack unchanged over a decade of public records; rubric-graded mitigation guidance per stakeholder group.

### 1.4 Verify the Verifier: Specification-Grounded LLM Cross-Checking for Bugs That Escape UVM Scoreboards
- **arXiv:** [2611.26588](https://arxiv.org/abs/2611.26588) [cs.SE; cs.AI; cs.AR] — 19 Nov 2026
- **Authors:** Ana E. Sanchez Villalobos, Michael D. Quinn, Aakash Tyagi, Minh D. Luu, David Kebo Houngninou
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** A passing UVM regression shows the design agrees with the reference model on what the scoreboard checks, not that it meets the specification. Bugs that pass every test yet violate the specification, termed scoreboard escapes, survive mature testbenches. We present Verify the Verifier, to our knowledge the first framework whose LLM-based Anomaly Cross-Checker examines a passing regression's traces against the specification. Of 564 bugs inserted into four OpenTitan IPs, 68 are candidate scoreboard escapes: non-equivalent, exercised by the tests, yet passing. The framework confirmed 41 as scoreboard escapes with assertions failing on the buggy design and proven on the original.
- **Key innovations:**
  - First LLM-based Anomaly Cross-Checker: examines passing regression traces against the specification.
  - On 564 inserted bugs across 4 OpenTitan IPs: 68 candidates, 41 confirmed scoreboard escapes (assertions fail on the buggy design, proven on the original).

### 1.5 The Geometry of Lies: Knowledge and Persona Directions for Detecting Deception in Large Language Models
- **arXiv:** [2611.26545](https://arxiv.org/abs/2611.26545) [cs.AI] — 19 Nov 2026
- **Authors:** Md. Abdullah Al Zami, Suraiya Shanaz, Mahdi Hasan, Shoaib Ahmed Dipu, Farig Yousuf Sadeque, Md. Sabbir Ahmed
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Linear probes are the cheapest LLM lie detectors but often fail to transfer across kinds of lie. Label-free directions from honest and deceptive role-play are untested at 70B scale and on lies about knowledge, where a lie and an honest denial can be identical. We widen a published persona bank with roles that deny knowledge they have, plus honest counterparts. At each model's middle layer the resulting persona direction ranks lies across Liars' Bench better than single-dataset probes on three of its four models; it fails on Qwen, even when Qwen stays in role far more often. On Llama-3.3-70B-Instruct it beats directions from a random persona bank, but its gain over the published direction is within the range of random widenings. On lies about knowledge, persona directions mainly track a reply's wording: where lies and honest denials share their words, our three main contrasts stay inside the random-direction band on Llama and Qwen and reach only its edge on Gemma, though on Mistral one clears it. A knowledge direction contrasts questions the model can answer with ones nobody can, each followed by the same scripted denial. It separates lies from identical honest denials on two models and narrowly on a third, but not on the fourth; its other results partly depend on the benchmark's wording. On the Gender-Secret fine-tune it clears the band by a few hundredths on Llama and fails on Mistral. The sum of the two directions ranks lies better than a supervised probe at the same depth on all four models (on one, both near chance) but is level with the persona direction on Llama's average and behind that probe on held-out lies. More varied role-play questions do not help the persona direction on Liars' Bench.
- **Key innovations:**
  - Widened persona bank with knowledge-denial roles + honest counterparts; persona direction ranks lies better than single-dataset probes on 3/4 models (fails on Qwen).
  - Two-direction approach: persona + knowledge direction ranks lies better than a supervised probe at the same depth on all four models.

### 1.6 LLM GerryMandering: Separating Interactions from Additive Effects in LLM Audits
- **arXiv:** [2611.26538](https://arxiv.org/abs/2611.26538) [cs.AI] — 19 Nov 2026
- **Authors:** George Rahul, Ronit Jahilal, Bhaskara Hanuma Vedula, Ponnurangam Kumaraguru, Pushkar Shukla
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Intersectional bias arises when a model treats people who hold several marginalised identities at once differently from what their separate identities would predict. Auditing such intersectional subgroups remains a challenge: their number grows quadratically, and there is no agreed baseline for what independent attributes would predict. Without such a baseline, many existing audits flag a subgroup when it exceeds each attribute alone, a condition that attributes acting independently already satisfy. We test this standard criterion on 150 synthetic datasets built with no interaction. With the shuffle null, it flags 66.1 false subgroups per dataset on average, and at least one in every dataset. When we plant interactions of known size into these datasets, a repaired null lets the criterion recover only 32% of them. We introduce ADDIS (Additive Intersectional Screen), which fits an additive model over all attributes, scores each subgroup by its Additive Residual Distance (ARD) from that model's prediction, and tests it against a Freedman-Lane null. On our synthetic benchmark, ADDIS flags 0.09 false subgroups per dataset and recovers 84% of the same planted interactions. We then build IndiPersona, 10,000 synthetic Indian personas with six identity attributes, and audit 13 open language models. The standard criterion flags 7.1% of the 738 tested subgroups on average; ADDIS flags 3.0%. Gender identity crossed with sexual orientation is the largest pairing in every model, and counterfactual personas confirm it and additionally reveal a caste x class interaction in all but one model that the observational test lacked the data to detect. Much of what audits report as intersectional bias can thus arise from independent single-attribute effects alone, yet a small core of interactions survives.
- **Key innovations:**
  - ADDIS (Additive Intersectional Screen): additive model over all attributes; subgroups scored by Additive Residual Distance (ARD); Freedman–Lane null.
  - Synthetic benchmark: 0.09 false subgroups (vs 66.1 standard), recovers 84% of planted interactions; IndiPersona audit of 13 models finds gender×sexual orientation largest pairing and a caste×class interaction.

### 1.7 Client Exits - A Way to Increase LLM Transparency on the Client Side
- **arXiv:** [2611.26309](https://arxiv.org/abs/2611.26309) [cs.AI] — 19 Nov 2026
- **Authors:** Marc Jansen
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Textual recommendations generated by large language models (LLMs) can be difficult to inspect. This paper introduces \emph{Client Exits}, a lightweight mechanism for enriching LLM responses while separating semantic intent from client-specific presentation. The model inserts predefined, machine-interpretable markers into its output, and the receiving client decides whether and how to realize the corresponding enrichments. This allows supplementary information to be presented as graphics, text, speech, or other modalities without prescribing a concrete interface. We implement a prototype combining a finetuned Qwen model with a modified LibreChat client. Using the Question--Option--Criteria (QOC) approach including three XML-based client exits. We evaluate two QOC-oriented model variants trained on essentially the same examples, with client-exit annotations added for one variant. Across 100 test questions, the client-exit model includes all three markers in every response. An LLM judge, informed about the mechanism without being instructed to favor it, prefers this model's answers in 66\% of the comparisons. These results demonstrate successful marker generation on the evaluated test set and support the feasibility of client-controlled enrichment.
- **Key innovations:**
  - Client Exits: machine-interpretable markers inserted by the model; the client decides whether/how to realize enrichments (graphics, text, speech).
  - Prototype (finetuned Qwen + modified LibreChat, 3 XML-based exits); LLM judge prefers the client-exit model in 66% of comparisons.

### 1.8 BlockJack: Cross-Tenant Redirection Fault Attacks on Paged KV Cache Address Translation in LLM Serving
- **arXiv:** [2611.25945](https://arxiv.org/abs/2611.25945) [cs.CR] — 19 Nov 2026
- **Authors:** Qifan Wang, Jeremy Boy, Jonas Sander, Yansong Gao, Hongsheng Hu, Ye Dong, Thomas Eisenbarth, David Oswald
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Large language model (LLM) serving frameworks accelerate inference by retaining previously computed states in a key-value (KV) cache. Paged serving frameworks such as vLLM organize this cache through block tables analogous to OS page tables, which map each request's logical KV blocks to physical KV blocks, forming a software-managed address translation layer. Although fault attacks such as Rowhammer have exploited OS page tables to redirect memory accesses, prior fault attacks on LLMs have largely targeted the data plane, i.e., model weights or KV-cache contents, leaving KV-cache mapping unexplored. We present BlockJack (i.e., Block Hijack), the first KV cache address-translation fault attack in LLM inference. By corrupting block-table entries, BlockJack redirects a request's KV cache reads to blocks assigned to another tenant's request without modifying model parameters, prompts, or cached KV states. It achieves both confidentiality violation (victim information appears in attacker responses) and integrity violation (attacker-supplied context steers victim answers). We study paged KV cache mappings in vLLM and formally characterize when redirect targets are predictable. Across seven models spanning the Qwen, Llama, Gemma, and Phi families, a faulted mapping exposes victim context. For the integrity attack, we examine how topic proximity, intra-topic divergence, and model behavior shape redirected responses. On a 248-scene medical benchmark, the integrity attack causes up to 41.1% of responses to recommend less urgent care, while still appearing consistent with the victim's question. We demonstrate physical feasibility of BlockJack with Rowhammer and subsequently evaluate assignment validation as a defense. Following responsible disclosure, vLLM and Sonar confirmed the vulnerability and proposed patches that we reviewed and validated.
- **Key innovations:**
  - First KV-cache address-translation fault attack (BlockJack): corrupts vLLM block-table entries to redirect reads to another tenant's blocks.
  - Confidentiality + integrity: victim context appears in attacker responses; up to 41.1% of medical-bench responses recommend less urgent care on a 248-scene benchmark; Rowhammer feasibility.
  - Responsible disclosure followed; vLLM and Sonar confirmed + patched.

### 1.9 Multi-institutional grading of Barrett's esophagus dysplasia without stain normalization using a pathology foundation model and multiple instance learning
- **arXiv:** [2611.26562](https://arxiv.org/abs/2611.26562) [cs.CV; cs.AI] — 19 Nov 2026
- **Authors:** Amirali Khosravi, Jaidip M. Jagtap, D. Chamil Codipilly, Catherine E. Hagen, Jason T. Lewis, Rickey E. Carter, Shahriar Faghani, Vani J. A. Konda, Fouad Otaki, Shajan Peter, Nicholas Shaheen, Sachin Wani, Prasad G. Iyer, Bradley J. Erickson
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Barrett's esophagus dysplasia grading suffers substantial inter-observer variability, particularly for low-grade dysplasia, complicating clinical decision-making. We conducted a retrospective multi-institutional diagnostic accuracy study of a foundation model-based deep learning system for dysplasia grading, using 969 H\&E-stained whole slide images from four institutions. Patch-level classifiers trained on expert annotations identified diagnostically relevant regions, followed by attribute-aware multiple instance learning for slide-level classification as non-dysplastic Barrett's esophagus (NDBE), low-grade dysplasia, or high-grade dysplasia. On a held-out test set (n = 130), macro-averaged AUC was 0.96 (95\% CI 0.93--0.98). For binary dysplasia detection, sensitivity was 98\% (80/82) and specificity 81\% (39/48), with a negative likelihood ratio of 0.030 and quadratic-weighted \kap{} of 0.83 against expert consensus. No high-grade dysplasia case was misclassified as NDBE. Performance was consistent across institutions without stain normalization, indicating that stain-robust foundation-model representations may remove the site-specific preprocessing that has constrained prior systems to institution-specific deployment.
- **Key innovations:**
  - Foundation-model + attribute-aware MIL pipeline: patch-level classifiers on expert annotations → slide-level NDBE/LGD/HGD classifier.
  - Multi-institutional (4), stain-robust: macro-AUC 0.96 (95% CI 0.93–0.98), sensitivity 98%, specificity 81% on held-out set (n=130); performance consistent across institutions.

## 2. Recommendation

### 2.1 Beyond Covers and Titles: Evidence-First Ranking for Robust Cold-Start Recommendation
- **arXiv:** [2611.26249](https://arxiv.org/abs/2611.26249) [cs.CV] — 19 Nov 2026
- **Authors:** Fuyi Wang, Yuxin Cao, Yifan Liao, Renyang Liu, Lin Li, Wei Song
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Short-video platforms rank new uploads before anyone has watched them, using content towers that read a video's cover, title and frames. Existing attacks on content-aware recommenders perturb pixels or features and ignore platform re-encoding, and existing defenses train against norm-bounded perturbations that neither match real edits nor preserve recommendation quality. We show with REAP, a realizable attack through {a simulated platform channel (H.264 transcoding, rescaling, cropping and JPEG)}, that packaging edits raise a cold video by 32.0 rank-percentile points in unrelated audiences. We then observe that cold-start ranking does not need the packaging at all: a tower that sees only the video body ranks cold items best. Building on this, we propose Evidence-First Ranking (EFR), which scores cold videos from their body, admits packaging only through a support-gated residual bounded by $γ$, and merges cold and warm rankings by rank percentile, yielding an exact certificate against any packaging edit. On MicroLens-100K, EFR cuts the attack gain by 81% and raises cold-start Recall@100 from 0.1133 to 0.170, while keeping the merged NDCG@10 within 4% of the undefended system.
- **Key innovations:**
  - REAP attack: realizable through simulated platform channel (H.264, rescale/crop/JPEG); packaging raises cold video 32.0 rank-percentile points in unrelated audiences.
  - Evidence-First Ranking (EFR): cold videos scored from body only; packaging admitted via support-gated residual bounded by γ; merges cold/warm by rank percentile with an exact certificate against any packaging edit.
  - MicroLens-100K: attack gain cut 81%, cold-start Recall@100 0.1133 → 0.170, merged NDCG@10 within 4% of undefended.

### 2.2 From Sessions to Serving: Integrating LLM-Based Embeddings into Retrieval for Production Content Recommendation
- **arXiv:** [2611.26096](https://arxiv.org/abs/2611.26096) [cs.IR; cs.LG] — 19 Nov 2026
- **Authors:** Zhixiong Hu, Meng Li, Maggie Zhang, Deborshi Goswami, David Bailey, James Bradley
- **Institution/Company:** Autodesk
- **Abstract:** Personalized content recommendation on large marketplace websites must reconcile heterogeneous candidate content (e.g., customer stories, product pages, industry pages, and learning content) with sparse, fast-changing user behavior, placing increasing demands on the retrieval stage to represent user interest well, not just the downstream ranking stage. We present LSER (LLM Session Embedding Retrieval), a production content recommendation system for autodesk.com that derives session- and history-level embeddings from a pretrained large language model (LLM) and adds them as auxiliary user-side features in the retrieval-stage user tower alongside existing learned sequence encoders. To keep user-side embeddings fresh under real-time behavior, we build a nearline serving path that asynchronously refreshes sequential and LLM-derived user vectors for our main content recommendation server. We validate the incremental value of the LLM features through an ablation study across our full multi-content-type catalog. Our results indicate that integrating LLM-derived embeddings as additional retrieval signals, together with production-grade nearline serving, is technically feasible and can improve model performances.
- **Key innovations:**
  - LSER: session- and history-level LLM embeddings added as auxiliary retrieval user-side features.
  - Nearline serving path: async refresh of sequential + LLM-derived user vectors; ablation across Autodesk's multi-content-type catalog.

### 2.3 Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models
- **arXiv:** [2611.26531](https://arxiv.org/abs/2611.26531) [cs.IR; cs.AI; cs.LG] — 19 Nov 2026
- **Authors:** Chang Yang, Yao Xuan, Wendan Yan, Nhat Le, Jiang Liu, Longhao Jin, Zhen Peggy Yao, Alireza Vahdatpour, Djordje Gligorijevic
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Large Web platforms operate large fleets of ranking models, each selecting features from a shared pool of tens of thousands. We present an end-to-end agentic system that optimizes features across the fleet under resource constraints shared across models and those set per model, such as feature pipeline cost and serving throughput (QPS), respectively. In this system, LLM agents propose hypotheses, and deterministic tools execute experiments and verify them. For each model, an LLM generates and shortlists cross features from a combinatorial candidate space, and all features are then ranked by several importance methods. Feature blending mixes these rankings into a single selection, using Pareto fronts across tasks for multi-task models. An LLM Researcher agent then tunes the feature selection in 10--25 asynchronous trials under resource caps, and a trimming step keeps the pipeline cost within budget. Across production models, the system improves normalized entropy by 0.31% on average within each model's budget, and the trimming step cuts pipeline cost by 2.3% with no regression beyond measurement noise. The optimized models were launched, and in online A/B tests they improved a primary online metric by 0.20%.
- **Key innovations:**
  - Agentic feature selection: LLM agents propose cross features from combinatorial space; tools execute + verify; feature blending via Pareto fronts across tasks.
  - LLM Researcher agent tunes selection in 10–25 async trials under per-model resource caps + trimming step.
  - Results: +0.31% normalized entropy, −2.3% pipeline cost; A/B: +0.20% primary metric.

## 3. Advertising

### 3.1 Iterative Scarcity-Guided Exploration: Bootstrapping Generative Auto-bidding from Narrow Support
- **arXiv:** [2611.26060](https://arxiv.org/abs/2611.26060) [cs.LG] — 19 Nov 2026
- **Authors:** Qingmao Yao, Guangzheng Hu, Yusen Huo, Zhilin Zhang, Chuan Yu, Jian Xu, Xu Chu, Bo Zheng, Xiaotie Deng
- **Institution/Company:** alimama (github.com/alimama-tech)
- **Abstract:** Auto-bidding is a core algorithmic component in online advertising auctions. In practical cold-start settings, iterative training is commonly used to compensate for low-quality, narrowly supported historical data. Unfortunately, in iterative training, representative diffusion-based AI-Generated Bidding (AIGB) methods fail to sustain extrapolation beyond the narrow data support and stagnate at a suboptimal level. In this paper, we theoretically attribute this stagnation to Signal-to-Noise Ratio (SNR) collapse: the weak radial return signal is overwhelmed by a curvature-induced penalty. To break this stagnation, we propose \textbf{Iterative Scarcity-Guided Exploration (ISGE)}, which introduces a guidance handoff: as the return signal collapses, scarcity subsequently takes over as an exploratory signal to elevate the SNR above a critical threshold. Specifically, ISGE iteratively alternates between a \emph{Judger} that assigns scarcity scores to trajectories and an \emph{Explorer} that performs guided generation of high-scarcity and high-return trajectories, thereby bootstrapping from the narrow support with such self-generated trajectories. Extensive experiments on the industrial AuctionNet benchmark demonstrate that ISGE, starting from cold-start datasets, effectively surpasses the performance of the Full-Dataset baseline within three iterations. Code is available at https://github.com/alimama-tech/ISGE
- **Key innovations:**
  - ISGE: alternates Judger (scarcity scores for trajectories) and Explorer (guided generation of high-scarcity + high-return trajectories); bootstraps from narrow data support.
  - Addresses SNR collapse in cold-start AIGB; outperforms Full-Dataset baseline within 3 iterations on AuctionNet.

## 4. Sequential Modeling

### 4.1 RL Can Only Reinforce What It Sees Succeed
- **arXiv:** [2611.26084](https://arxiv.org/abs/2611.26084) [cs.LG; cs.CL] — 19 Nov 2026
- **Authors:** Ruben Sanchez-Corcuera, Unai Zulaika, Aritz Bilbao-Jayo, Miguel Fernandez-de-Retana
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** When a familiar rule stops working, an agent has to weigh what pre-training taught it against what it now observes. We ask how outcome-reward reinforcement learning (RL) changes this balance, in a puzzle world where both sides are known: small language models trained from scratch on games played by a Bayesian player, so that the prior and the right answer are exact. Base models hedge as their corpus did, and RL turns that hedging into decisions, in whichever direction the reward favours. But RL can only reinforce what it sees succeed. When the right action is rare, each run either learns it everywhere or not at all, and which runs take off is predicted before training by one count: the expected number of groups of attempts in which the action wins. About 35 such groups give even odds. The count holds for new and repeated problems and for groups of 4 to 256 attempts, and across learning rates, optimizers, GRPO variants and model sizes from 1.3M to 85M parameters, which move the threshold but not what is counted.
- **Key innovations:**
  - Shows RL only reinforces what it observes succeeding: rare actions either learn everywhere or not at all; predicted by expected count of attempt groups where the action wins (~35 → even odds).
  - Validated across optimizers, GRPO variants, model sizes 1.3M–85M.

### 4.2 How Much Should an Agent Remember? Deployment Lessons from Self-Distilled Memory for LLM Agents
- **arXiv:** [2611.26361](https://arxiv.org/abs/2611.26361) [cs.AI] — 19 Nov 2026
- **Authors:** K. R. Jayaram, Vatche Isahagian, Aswath Vaithinathan Aravindan, Vinod Muthusamy, Punleuk Oum, Gaodan Fang, Michal Ulewicz, Gegi Thomas, Evelyn Duesterwald
- **Institution/Company:** IBM
- **Abstract:** LLM agents on long-horizon tasks fail in recurring, procedural ways. They mis-paginate an API, resolve the wrong entity, or answer when no answer was asked. We built a pipeline that lets an agent learn from its own history. It first mines short \emph{lessons} from the agent's own trajectories, one to three per episode. It then consolidates those lessons into a smaller set of \emph{guidelines}, where each guideline records how many lessons it merged. At inference the agent receives either all guidelines or a selected subset. The pipeline ships in the open-source altk-evolve library and is deployed in IBM's CUGA agent and watsonx Orchestrate platform. We report what we learned building, measuring, and productizing it. Our primary instrument is the AppWorld benchmark, across models spanning 40--92\% baseline task completion. The central finding is that the right amount of memory is a property of the model, not the memory. A strong model keeps improving as guidelines are added. DeepSeek-V3.2 gains +9.5 points of task completion and +16.1 points of scenario completion with its full 191-guideline set. A weak model gains less from the same full set than from a small selected subset. gpt-oss-120b starts at 39.9\% task completion. It reaches 51.2\% with all 199 of its guidelines but 55.4\% (mean of two runs) with a selected subset of about 29. Around that result we report what went wrong: a high-support guideline that backfired, provenance silently dropped during consolidation, a swallowed API error that failed every task while producing a plausible log, and a baseline confound that nearly produced a misleading comparison with a prior method. We distill these into recommendations for teams deploying agent memory.
- **Key innovations:**
  - Pipeline: mines 1–3 lessons/episode from trajectories → consolidates into guidelines → inference selects all or subset; shipped in altk-evolve, deployed in IBM CUGA agent + watsonx Orchestrate.
  - Central finding: optimal memory amount is model-dependent; DeepSeek-V3.2 +9.5 task / +16.1 scenario completion with 191 guidelines.
  - Documents failure modes (backfired guideline, dropped provenance, swallowed API error, baseline confound) → deployment recommendations.

## 5. Games & Interactive Systems

### 5.1 PlayCraft: Designing Engaging Games from Agent Play Experience
- **arXiv:** [2611.26624](https://arxiv.org/abs/2611.26624) [cs.AI; cs.CV] — 19 Nov 2026
- **Authors:** Weihao Cheng
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Recent AI agents can generate playable games, but these games are not necessarily engaging. Mastery is a key source of engagement, yet designing for it requires extensive human play and tuning. We propose PlayCraft, an automated framework that uses a vision-based agent to play games and draws on its detailed play experience to revise them for mastery. Starting from an initial game, PlayCraft alternates between playing and crafting. In the playing stage, a player agent watches the game screen, uses the controls, and pursues the game objective over repeated episodes while retaining memory. After each episode, it reports its progress, outcomes, decisions, and reflections. In the crafting stage, a crafter agent uses these reports to revise the game. It estimates player abilities, predicts performance at different proficiency levels, and compares those predictions with a target learning progression. It diagnoses the game and addresses the gaps by giving players meaningful opportunities to improve through better decisions and execution. We evaluate games in fresh runs with player agents across three intelligence settings, measuring learning gain and learning slope. Compared with the initial games, PlayCraft yields larger learning gains and steeper learning slopes in most games. It also outperforms the baselines on the macro-average of each metric at every intelligence setting.
- **Key innovations:**
  - PlayCraft: alternates playing (vision-based agent: watches screen, uses controls, reports progress/outcomes/decisions/reflections) and crafting (estimates player abilities, predicts proficiency levels, diagnoses gaps, adds mastery opportunities).
  - Validated: larger learning gains and steeper learning slopes than baselines across 3 intelligence settings (macro-average).

### 5.2 When Agents Play Differently: Localizing Human--Agent Behavioral Divergence with Conditional Distributional Testing
- **arXiv:** [2611.26012](https://arxiv.org/abs/2611.26012) [cs.AI] — 19 Nov 2026
- **Authors:** Oleg Smirnov, John Pertoft, Sara Karimi
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Evaluating whether artificial agents behave like humans requires comparing not just average outcomes but entire behavioral distributions across diverse contexts. We propose a stratified framework that computes nonparametric discrepancy statistics within contextual cells, and discovers subgroup rules identifying where agent behavior departs from human play. We show that session-level metrics dominated by win/loss outcomes offer little signal beyond mean comparisons, whereas process-level metrics such as move efficiency reveal genuine behavioral differences. Applied to a commercial match-3 game, it uncovers patterns invisible to aggregate metrics: a playtesting bot is diverging substantially from humans in certain game modes, while showing no detectable divergence in others. We release our implementation as open source to support reproducibility and adoption.
- **Key innovations:**
  - Stratified nonparametric discrepancy statistics within contextual cells + subgroup discovery rules for agent-vs-human divergence.
  - Applied to a commercial match-3 game: playtesting bot diverges in certain modes, undetectable via outcome-level metrics; move-efficiency reveals the real differences.

### 5.3 Safe Subgame Resolving in Multiplayer Games
- **arXiv:** [2611.25981](https://arxiv.org/abs/2611.25981) [cs.GT; cs.AI] — 19 Nov 2026
- **Authors:** Boning Li, Longbo Huang
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Poker and other games with hidden information are too large to solve in one pass. Strong systems compute a complete blueprint strategy offline and refine it in real time inside the reached subgame. In 2p0s games, a safety theorem guarantees that subgame resolving never increases how much an adversary can gain by exploiting the resolved strategy relative to the blueprint strategy. With three or more players acting independently, no such guarantee exists yet, and heuristic resolving can increase the profile's best-response gap. We prove the first conditional safety theorem for uncorrelated multiplayer subgame resolving, a post-hoc certificate for any delivered update. The best-response gap of the resolved profile exceeds that of the blueprint by at most four terms. Two concern the resolver: the subgame value the blueprint promised without realizing ($A_i^{S}$) and the resolver's subgame solve error ($\varepsilon_i$). The other two are the opponents' best-response gains inside the subgame over their promised values ($\sum_q M_{q}$) and a structural tax ($Θ$), which measures how much the players' total utility can change. The tax is zero in constant-sum games, including every rake-free poker variant. Constructions attain each term with equality. On three-player Leduc poker and on Kuhn poker with up to six players, resolving without a certificate raises the gap beyond a small tolerance in 12% to 100% of the updates. The certificate flags every such update and accepts 41% (Kuhn) and 86% (Leduc) of the standard resolving updates. A resolver that keeps the blueprint whenever the certificate exceeds the tolerance delivers no harmful update. The certificate needs only one best-response pass per opponent inside the subgame, so real-time multiplayer solvers that refine a blueprint can attach it as a safety check. Code is available at https://github.com/lbn187/MultiPlayerSolver
- **Key innovations:**
  - First conditional safety certificate for multiplayer subgame resolving (MultiRENY): resolved profile's best-response gap ≤ blueprint + terms (A_i^S, ε_i, Σ M_q, structural tax Θ); tax zero in constant-sum games.
  - Certifies updates in 12–100% of cases where resolving raises the gap; accepts 41% (Kuhn) / 86% (Leduc) of standard updates.

### 5.4 ContextRenderer: Dynamic-Context Video Generation for Interactive Game Worlds
- **arXiv:** [2611.25838](https://arxiv.org/abs/2611.25838) [cs.CV; cs.GR] — 19 Nov 2026
- **Authors:** Runze Wang, Fei Zha, Bing He, Ke Xu, Zhongyuan Wu, Yuxuan Xie, Wenzheng Wu, Zhongyuan Liu, Youcheng Cai, Ligang Liu
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** Interactive game world models separate executable world evolution from visual generation, using video models to render engine-provided scene representations into detailed observations. During sustained gameplay, however, existing generative renderers struggle to follow changing conditions while preserving visual continuity across diverse proxies and target styles. We therefore introduce ContextRenderer, an autoregressive video diffusion framework designed for both dynamic conditioning and cross-proxy generalization. It couples Dynamic-Context Learning (DCL) for chunk-level interaction supervision with Recurrent History Compression (RHC) to follow condition updates while preserving visual continuity within a bounded token budget. Across proxy representations, Cross-Representation Flow Alignment (CRFA) connects proxy reconstruction with appearance and interaction variation through a shared high-fidelity reconstruction. WorldPrism, our interaction-centric dataset constructed from agent-built worlds, AAA gameplay, and open-source videos, supplies the corresponding renderings and chunk-level annotations for these learning tasks. Experiments on GWM-Bench and Solar-Bench show improved reconstruction and visual quality, while qualitative results demonstrate minute-long interactive rendering under changing prompts and subject references. Project page: https://rainzor.github.io/contextrenderer/
- **Key innovations:**
  - ContextRenderer: autoregressive video diffusion with DCL (chunk-level interaction supervision) + RHC (bounded token budget, preserves visual continuity while following condition updates).
  - Cross-Representation Flow Alignment (CRFA): shared high-fidelity reconstruction across proxy/appearance variants; WorldPrism dataset (agent-built worlds, AAA gameplay, open-source videos).

### 5.5 Optimal Patrol Widths in the Infinite-Corridor Barrier-Guarding Game
- **arXiv:** [2611.26140](https://arxiv.org/abs/2611.26140) [math.OC, math.MG] — 19 Nov 2026
- **Authors:** Kevin M. Boergens
- **Institution/Company:** Not listed in arXiv metadata
- **Abstract:** A guard of speed at most one and capture radius $r$ patrols an infinite corridor. An intruder knows the patrol and can follow any path of speed at most $q$ from one end to the other. We determine where the maximum width permitted by straight wall runners can be guarded against all such paths. Write $W_{\mathrm{opt}}(q)$ for the supremum over patrols with bounded longitudinal excursion and $F(q)=2r\sqrt{1+(3q^2+2q-1)^{-1}}$ for the wall ceiling on $1/3 < q < 1$. A four-leg bowtie attains $F(q)$ exactly for $q_a\le q < 1$, where $0.457892036651 < q_a < 0.457892036652$. For every $1/3 < q < q_a$ the supremum is strictly smaller. As $q$ approaches $q_a$ from below, $F(q)-W_{\mathrm{opt}}(q)$ is bounded above and below by positive constant multiples of $r(q_a-q)^2$. The lower estimate controls near-optimal patrols uniformly in their period. A rescaled bowtie gives the matching upper estimate. We also prove that periodic patrols give the same supremum as bounded-excursion patrols. For $q\ge1$ the one-way optimum is $r\sqrt{4+q^{-2}}$, a transverse sweep. This sweep is optimal against transit in both directions for $q\ge1/2$. At low speeds, $qW_{\mathrm{opt}}(q)/r$ tends to two, and an explicit ten-leg patrol guards width greater than $(2/q-1.235353)r$ throughout $0 < q\le1/40$. Rational spacetime and flux certificates give finite-speed bounds, including $6.944691333740r < W_{\mathrm{opt}}(1/4)\le8.10r$.
- **Key innovations:**
  - Characterizes optimal guardable width W_opt(q) and wall ceiling F(q) for an infinite-corridor guard (speed ≤1, radius r) vs intruder (speed q).
  - Four-leg bowtie attains F(q) exactly for q ∈ [q_a, 1); proves strict gap below q_a with gap bounded by r(q_a−q)² as q→q_a⁻; periodic patrols = bounded-excursion optimum.
  - Scalar bounds: 6.944691333740r < W_opt(1/4) ≤ 8.10r.

## Summary of Coverage

| Domain | Papers (count) |
|---|---|
| AI / LLMs | 1.1–1.9 (9) |
| Recommendation | 2.1–2.3 (3) |
| Advertising | 3.1 (1) |
| Sequential Modeling | 4.1–4.2 (2) |
| Games & Interactive Systems | 5.1–5.5 (5) |
| No dedicated CTR papers found in this sweep. | — |
