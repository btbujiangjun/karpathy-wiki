---
title: "arXiv Daily Digest — 2026-09-08"
type: synthesis
created: 2026-09-08
updated: 2026-09-08
sources: []
tags: [arxiv, ai, llm, recommendation, personalization, games, game-ai, sports-analytics, rl, reward-hacking, agents, unlearning, benchmark, hybrid-lm, moe, quantization, finance, predictive-maintenance, sequential-modeling, daily-digest]
---

# arXiv Daily Digest — AI, LLMs, Recommendation, Sequential Modeling, Games

> Search date: 2026-09-08 · Scope: **no new mailing** since 09-07 (arXiv lists announced through **Mon 7 Sep 2026**), so this is a **second pass over the Mon 7 Sep 2026 mailing**, sweeping papers the 09-07 and 09-08 sibling digests did *not* feature. Every featured arXiv ID below was **grep-verified absent from `wiki/`** (20/20 candidates clean; 0 featured overlaps with [[arxiv-daily]]/[[arxiv-ai-search]]/[[game-rl-daily]]/[[conference-digest]] 09-07 and [[arxiv-ai-search]]/[[arxiv-paper-check]] 09-08). Retrieved via `arxiv.org/list/{cs.IR,cs.CL,cs.LG,cs.AI,cs.GT,cs.MA,cs.CV}/recent` + individual `/abs/` pages (arXiv Atom API still rate-limited). **20 new papers below across 6 categories.**
>
> Affiliations marked *(inferred)* are deduced from author identities and flagged accordingly; otherwise "not stated". Some listed venues (EMNLP'26 Findings, CIKM'26, WISE 2026, Neurocomputing) are printed on the arXiv pages themselves.

---

## ① Recommendation, LLM Personalization & Adapters (3)

> This report's rec/personalization cluster is the second-pass dividend: the pure cs.IR Mon 7 Sep mailing was fully mined on 09-07, but three personalization/adaptation papers surfaced in cs.AI. Two of them (Aplaud, PLUME) come from the same Kent State group and form a coherent low-rank user-modulation line.

### 1.1 Continual Graph Memory for Adaptive Recommendation under Intent Drift (CGM-Rec)

| Field | Detail |
|-------|--------|
| **Authors** | Hao Nguyen Ngoc, Tung Nguyen, Nguyen Thi Hanh, Hoang Thai Dinh, Nguyen Xuan Tung |
| **Institution** | Not stated |
| **Submitted** | 2026-09-04 · [2609.04651](https://arxiv.org/abs/2609.04651) · cs.AI · Findings of EMNLP 2026 |
| **Abstract** | Adaptive recommendation under intent drift, where feedback from each outcome can reveal whether the relational evidence used for ranking is useful, missing, or misleading. Knowledge Graphs provide semantic structure but are typically treated as a *static retrieval substrate*. CGM-Rec treats the graph state as a **writable memory** with two components: a Semantic Graph Memory updated conservatively through quality-gated typed operations (stable, high-confidence relational knowledge) plus an Episodic Lesson Memory acting as a fast reactive store for recent outcomes, failure cases and corrective hints. During testing, model parameters stay frozen; adaptation happens only through memory writes under a one-pass reranking protocol. |
| **Key innovations** | Frozen-parameter adaptation via memory writes (no encoder/prompt updates at test time); quality-gated conservative KG updates + episodic failure memory; up to **+29.58% HR@1** vs. strongest LLM baseline on Bundle, and HR@5 0.5941 vs. 0.4746 over K-RagRec on metadata-rich ML-100K. |
| **Why it matters** | Runs parallel to this week's memory-as-writable-artifact theme (cf. 2609.04915 compact agent memory, 2609.05339 memory portability) but applies it to KG-enhanced reranking — a train-time-free way to keep graph recommenders responsive to evolving intents. |

### 1.2 Aplaud: Adaptive Personalized Low-Rank Decomposition for User-Specific LLM

| Field | Detail |
|-------|--------|
| **Authors** | Xinyu Li, Ruoming Jin, Jianfeng Zhu, Ruixin Guo, Zhi Liu |
| **Institution** | Kent State University *(inferred: Ruoming Jin)* |
| **Submitted** | 2026-09-04 · [2609.04738](https://arxiv.org/abs/2609.04738) · cs.AI |
| **Abstract** | Personalized survey response prediction with fine-tuned LLMs: limited per-user data, storage scalability, and shared structure across survey questions. Aplaud extends the LoRA paradigm by splitting adaptation into a **frozen, shared low-rank basis** plus a **compact user-specific correction**, augmented with a rank-one residual for finer personalization; the correction matrix can be factorized into an even lower-rank form to cut per-user cost and overfitting further. |
| **Key innovations** | Separates shared-basis vs. user-specific correction so per-user parameters shrink without losing personalization; beats SOTA LoRA-based personalized-LLM approaches on generalization and inference efficiency. |
| **Why it matters** | Per-user storage is the economic bottleneck of LLM personalization at platform scale — the same storage-cost problem the wiki tracks in CTR (user towers) and per-profile serving. |

### 1.3 PLUME: Parameter-Efficient Personalization via Low-Rank User Modulation in Shared Subspaces

| Field | Detail |
|-------|--------|
| **Authors** | Xinyu Li, Hao Zhou, Jianfeng Zhu, Julina Maharjan, Ruixin Guo, Feodor Dragan, Ruoming Jin |
| **Institution** | Kent State University *(inferred: Ruoming Jin / Feodor Dragan)* |
| **Submitted** | 2026-09-04 · [2609.04715](https://arxiv.org/abs/2609.04715) · cs.AI |
| **Abstract** | Per-user fine-tuning improves LLM personalization but imposes parameter/storage overhead. PLUME first learns a **global task subspace** from aggregated user data, then personalizes by training only a lightweight *small square matrix* inside that subspace per user, with cross-layer shared parameters and rank-1 residual terms to cut redundancy. |
| **Key innovations** | Shared-subspace modulation with minimal residuals: comparable/superior results to strong baselines while cutting **per-user parameters by >95%**; semantically grounded low-rank adaptation. |
| **Why it matters** | Same-week companion to Aplaud from the same lab — the two papers independently chip away at the storage-expressiveness trade-off of per-user LLM adaptation; directly relevant to multi-tenant LLM serving lines in this wiki. |

---

## ② Games, Game AI & Sports Analytics (2)

### 2.1 CHAMP: Cross-domain Hybrid Architecture for Matchmaking and Prediction in Online Multi-Player Games

| Field | Detail |
|-------|--------|
| **Authors** | Kai Wang, Ge Fan, Chaoyun Zhang, Yuyang Jiang, Yuze Liu |
| **Institution** | Not stated (large-scale MOBA, industrial setting) |
| **Submitted** | 2026-09-04 · [2609.04870](https://arxiv.org/abs/2609.04870) · cs.AI · CIKM 2026 Applied Research Track |
| **Abstract** | Follows the authors' prior CUPID (matchmaking as assignment re-optimization with a single-mode win-rate predictor). Deploying across a full ladder exposes cold-start (queueing players lack in-mode match history), distribution inconsistency (skill shifts across rank tiers), and data starvation at extreme segments. CHAMP replaces the target-mode-only player profile with a **hybrid domain feature collection** — a timestamp-ordered cross-mode short-term sequence annotated with target-domain features, plus per-mode breakdowns of long-term, real-time and team statistics. The **DAWN** network (Domain-Aware Win-rate Network) couples a Domain-aware Knowledge Extractor (DAKE) with Temporal/Spatial/Permutation OmniNet encoders (DATOE/DASOE/DAPOE) so mode-conditioned representations and per-mode debiasing are learned jointly in one shared network. Online, one trained DAWN serves every mode with per-mode position-satisfaction thresholds as the only mode-specific knob. |
| **Key innovations** | Cross-domain matchmaking that resolves cold-start and distribution shift without per-mode models; **67.73% win-rate prediction accuracy** offline (beats attention/sequence baselines); online A/B on the entire League ladder up to Elite Mode cuts imbalanced matches, with the **5-minute kill-crushing rate down by up to 20.73%** for lower-tier players. |
| **Why it matters** | A mature industrial continuation of the matchmaking-as-optimization line in this wiki; the cross-mode transfer recipe (shared network + per-mode thresholds) is the same shape as cold-start fixes in rec/CTR — worth pairing with the wiki's cold-start papers. |

### 2.2 Hierarchical Possession-Aware Graph Pointer Network for Pass Receiver Selection (HPGPN)

| Field | Detail |
|-------|--------|
| **Authors** | Jingyi Wang, Da Li, Kaixin Wang, Zhangqin Huang |
| **Institution** | Not stated |
| **Submitted** | 2026-09-04 · [2609.04803](https://arxiv.org/abs/2609.04803) · cs.AI · WISE 2026 |
| **Abstract** | Pass receiver selection in football analytics under broadcast-like freeze-frame observations: partial, variable visibility of anonymous players, no complete trajectories or stable identities. The model must reason over anonymous visible candidates, opponent pressure, and recent context. HPGPN formulates receiver selection as **variable-size candidate prediction over visible teammates**, jointly modeling current player interactions (graph), local event context, and possession-level temporal dynamics via dynamic possession history. A **glimpse pointer head** scores the receiver candidates after hierarchical refinement (spatial × contextual × historical evidence). |
| **Key innovations** | Possession-aware dual-branch dynamic-history modeling for sports analytics under partial observation; glimpse-pointer scoring over anonymous candidates; ablations confirm graph interaction + fixed event context + possession history each contribute. |
| **Why it matters** | Sports-analytics decision prediction is a niche the wiki's game/agent coverage rarely touches; the partial-observation + pointer-head setup is directly transferable to game bots and sequential-decision settings in this report's §2.1/§4 range. |

---

## ③ RL, Post-Training & Eval-Driven Optimization (4)

> This cluster clusters around a single question the wiki has tracked all week in GRPO/OPD coverage: **what actually transfers when you change the training recipe, and how do you measure it honestly?** Three of the four papers are explicitly controlled/audited studies rather than "new SOTA" claims.

### 3.1 What Does Multi-Harness RL Learn? Credit Assignment and Portability in Coding Agents

| Field | Detail |
|-------|--------|
| **Authors** | Chenqian Le, Jiayi Cheng, Qijia He, Runhao Li, Yinghao Li, Xupeng Chen |
| **Institution** | Not stated |
| **Submitted** | 2026-09-03 · [2609.04518](https://arxiv.org/abs/2609.04518) · cs.AI |
| **Abstract** | Agent RL increasingly runs through full execution harnesses; a "multi-harness recipe" mixes two choices — exposing the policy to several harnesses, and comparing their rewards inside one relative-advantage group. The paper **isolates the second choice (grouping rule)** in repository-level coding: from one Qwen3-8B warm start, it replays the same frozen task-harness records from Aider, OpenHands, Qwen Code, and SWE-agent under two GRPO grouping rules (Within vs. Cross pooled within a task), scoring every checkpoint with a sealed SWE-bench Verified oracle. Across 24,000 sealed evaluations, the **evaluation harness is the dominant variable** — it moves mean solve rate from 2.14% to 9.27% (4.3×) while the training recipe moves it by 1.16. The grouping rule is not: Cross−Within is +0.25pp (95% CI [−0.48, +1.02]); each rule's own seed range (0.42–0.45pp) exceeds the difference; pooled advantage carries the harness, not new capability. Re-collecting half the training data on-policy does not change this. |
| **Key innovations** | Clean causal isolation of the grouping rule with a sealed oracle across 4+1 harnesses; shows cross-harness credit = configuration adaptation, not portable capability; a concrete reporting obligation ("state the grouping boundary, test under an unseen harness"). |
| **Why it matters** | Directly useful to every GRPO/multi-harness recipe the wiki tracks (ERPO, GRPO variants): it argues harness variance dominates recipe variance — a strong caution against over-attributing gains to grouping-rule innovations. |

### 3.2 Harness-agnostic Detection and Immunization of Reward Hacking in Self-Evolving LMs (HackProbe)

| Field | Detail |
|-------|--------|
| **Authors** | Rongxin Yang, Yang Liu, Shang Luo, Haoxuan Jia, Chongyang Zhang, Hao Zheng, Yingguang Yang, Yulin Huang, Jianshen Zhang, Yongzhi Qi, Kefu Xu, Congjing Ran, Bin Chong |
| **Institution** | Not stated |
| **Submitted** | 2026-09-04 · [2609.04665](https://arxiv.org/abs/2609.04665) · cs.AI |
| **Abstract** | Self-evolving LMs keep whichever candidate update raises a visible score; when that proxy is imperfect, sustained selection widens the gap to real capability — reward hacking. HackProbe is a **black-box monitor** that attaches to any self-evolving loop through two hooks, with no access to weights or activations. It keeps a secret, distribution-fixed comparison core (comparable capability proxy across generations) plus a rotated fresh layer that hardens the bank against co-adaptation. Four tests (level gap, scale-aligned divergence with online change-point detection, capability stagnation, conditional confidently-wrong rate) get a Šidák-corrected family-wise p-value. A risk-aware immunization layer reselects an honest candidate from the proposal pool, disclosing at most `log₂ Pi` bits per generation. Proves a detectability bound converting target error rate into an explicit probe-size budget. |
| **Key innovations** | Harness-agnostic reward-hacking detection (no weights/activations); frozen-core + rotation design; 0.763 AUROC vs. 0.663 strongest baseline and FPR 0.706→0.434; bandwidth-limited reselection is the only immunization level that returns more true capability under hacking (+5.2 avg) than it forfeits on clean runs (4.7). |
| **Why it matters** | Fills a gap the wiki's reward-hacking line (debate training, RecEvolve self-discovered hacking) has: a detect-and-immunize monitor that doesn't require white-box access — the realistic serving constraint for hosted self-evolving agents. |

### 3.3 Extremely Sparse Supervision Incentivizes Reasoning Ability

| Field | Detail |
|-------|--------|
| **Authors** | Zhishuai Liu, Xingzi Xu, Mehmet Saygin Seyfioglu, Pan Xu, Karim Bouyarmane |
| **Institution** | University of Illinois Chicago *(inferred: Bouyarmane group)* |
| **Submitted** | 2026-09-03 · [2609.04565](https://arxiv.org/abs/2609.04565) · cs.AI |
| **Abstract** | Post-training implicitly assumes token-intensive learning. In on-policy distillation (OPD), which admits dense teacher supervision at every generated token, the authors find the opposite: **as few as 1–2 tokens per reasoning trajectory (~0.05% of tokens) matches or surpasses full-token training** on reasoning ability. Consistent across nine teacher–student configs on math, validated on coding reasoning, Llama models, and PPO-based RL with verifiable rewards (RLVR). Argument: sparse supervision resembles natural reflection — a few critical reasoning steps revisited rather than word-by-word correction. |
| **Key innovations** | Quantifies a token-efficiency floor for post-training supervision; generalizes across distillation and RLVR; directly challenges the token-intensive assumption of modern post-training economics. |
| **Why it matters** | Lands on the same data-efficiency frontier as this week's 1-shot OPD (8 examples ≈ 17K) and RISE (self-generated teachers) — a coherent "post-training is wildly over-fed" narrative now backed by a controlled token-ablation result. |

### 3.4 Discovery Loop: LLM-Guided Program Evolution (Breaking 10 Packomania Records for $28)

| Field | Detail |
|-------|--------|
| **Authors** | Wes Sander |
| **Institution** | Not stated (code at `github.com/ucsandman/discovery-loop`) |
| **Submitted** | 2026-09-04 · [2609.05093](https://arxiv.org/abs/2609.05093) · cs.AI |
| **Abstract** | A lightweight system that uses an LLM to iteratively evolve optimization algorithms: from a simple seed solver, the LLM proposes algorithmic improvements guided by a scoreboard of results and a history of prior ideas; each candidate is evaluated against an **independent verifier**, improvements kept, failures discarded. On the Packomania circle-packing benchmark (maximize sum of radii of N variable-radius circles in the unit square), it improved best-known solutions for **10 values of N in 101–114 by 2.4–5.4%**, within 15 iterations and at **$27.72 total LLM cost**; results independently accepted by Packomania. Includes an adaptive plateau-detection mechanism. |
| **Key innovations** | Scoreboard-driven LLM program evolution with verifier-gated acceptance; cost-efficiency dynamics of LLM-based scientific discovery; democratized-discovery economics ($28 beats human-record-breaking). |
| **Why it matters** | Concrete evidence for the "LLM in the optimization loop" claims the wiki tracks (cf. AutoLR's deterministic evidence-weighted selector, RecEvolve's autonomous research); also a clean miniature of the verification-gap problem central to agentic papers here. |

---

## ④ Agents & Agent Infrastructure (4)

### 4.1 From Interaction Traces to Persistent Skills: Online Evolution for Computer-Use Agents

| Field | Detail |
|-------|--------|
| **Authors** | Longtao Hu, Xiao Liang, Linchao Zhu |
| **Institution** | University of Sydney *(inferred: Linchao Zhu)* |
| **Submitted** | 2026-09-04 · [2609.04869](https://arxiv.org/abs/2609.04869) · cs.AI |
| **Abstract** | Computer-use agents execute increasingly complex GUI tasks, but their interaction experience is transient — procedural knowledge from one rollout isn't systematically retained, refined, and reused. The paper presents an **online skill-evolution framework** that converts interaction trajectories and evaluator feedback into a persistent, versioned library of reusable procedures. Each iteration executes against a **frozen library snapshot**; evidence-guided skill updates become available in subsequent iterations **without changing model parameters**. Compared against a configuration-matched empty-library control across four OSWorld application domains, the full evolving library attains higher post-warm-up mean evaluator scores in all four runs (+5.7 to +18.6 pp). In GIMP, provenance-aware analysis reveals retrieval across task-of-origin boundaries and **revision churn** — repeated accepted edits fail to recover the originating task. |
| **Key innovations** | Frozen-snapshot versioned skill library (no parameter updates); auditable, provenance-aware procedural memory; characterizes conditional benefit and repeated-revision failures rather than claiming unconditional gains. |
| **Why it matters** | The wiki tracks the skill-library line (WikiSkill, skill transfer, BPS skill selection). This paper's negative result — *revision churn, retrieval across task boundaries* — is a valuable counterpoint to unconditional "skills always help" narratives. |

### 4.2 Forgetting Without Restarting: Execution-State Unlearning for Stateful LLM Agents

| Field | Detail |
|-------|--------|
| **Authors** | Chao Yao, Yangbo Wei, Zhen Huang, Junhong Qian, Chenle Chen, Shaoqiang Lu, Chen Wu, Lei He |
| **Institution** | Not stated |
| **Submitted** | 2026-09-04 · [2609.04875](https://arxiv.org/abs/2609.04875) · cs.CR |
| **Abstract** | Long-running LLM agents are stateful: beyond the transcript, they accrete compressed summaries, plaintext memory, pending tool plans, and a KV cache. Today's "forget" ops delete a memory record and stop — leaving every derived artifact intact. The paper **formalizes execution-state unlearning**: after a forget request, the agent must behave as if it had never observed the target. Modeling the runtime as a deterministic transition system, it proves the pre-target prefix is shared with the counterfactual world for free, the post-target suffix is irreducibly tainted without token-level attribution, and exact unlearning requires at least `T−τ+1` recomputed transitions. **Provenance-Guided Selective Replay** attains this bound as a cross-layer contract spanning prompt, compressed memory, and cache: a provenance graph locates the injection point, checkpoint restoration reduces to cropping the KV cache, and sanitized replay regenerates the counterfactual suffix. |
| **Key innovations** | First formal treatment of agent-execution-state unlearning with tight recompute bound; KV-cache cropping as a checkpoint-restore primitive; audited with elicitation/stochastic/string-free tests across 3 agent suites, 9 baselines, 3 model families — memory deletion leaves leakage unchanged, instruction-based forgetting collapses (Leak@probes = 1.00), while selective replay is indistinguishable from a full reset at up to **9× fewer recomputed tokens**. |
| **Why it matters** | Bridges unlearning (a wiki-tracked safety topic) with agent memory + KV-cache engineering. The provenance/cropping idea is likely to inform future memory-management and retention products. |

### 4.3 ττ-Bench: An Environment for End-To-End, Realistic Agent Construction

| Field | Detail |
|-------|--------|
| **Authors** | Quan Shi, Keshav Dhandhania, Karthik Narasimhan, Victor Barres |
| **Institution** | Princeton University *(inferred: Karthik Narasimhan)* |
| **Submitted** | 2026-09-04 · [2609.04611](https://arxiv.org/abs/2609.04611) · cs.AI |
| **Abstract** | The work of building production agents is increasingly handed to coding agents, yet benchmarks say little about whether an AI system can deliver one under real client-engagement conditions. ττ-bench (hyper-tau-bench) **makes agent construction the task**: a developer agent gets the records a business actually keeps, a client holding requirements, a production API, a codebase to inherit, and serving-cost/model limits, and must deliver a complete customer-service agent — scored by deploying it against held-out simulated users. Across 53 tasks / 4 domains, the strongest configuration (Claude Opus 5 under Claude Code) passes just **23.9%** of evaluation simulations vs. an expert-authored reference ceiling of **82.2%**. Failure modes mirror human agent developers: shallow queries instead of deep record comprehension, minimal client communication, and too little experimentation — shipping the first design that runs. |
| **Key innovations** | End-to-end engagement realism (records + client + API + codebase + cost limits); deploy-and-score evaluation; quantitative gap to an expert reference ceiling. |
| **Why it matters** | Benchmark-validity is a running wiki theme (GameXpert-Bench, StartupBench, UniRank). The 59-pt gap between best agent and reference ceiling is one of the starkest agent-construction results yet — and the failure taxonomy doubles as a roadmap. |

### 4.4 ICM-Bench: Person-Level Identity Reasoning in Multimodal Agents with Long-Term Memory

| Field | Detail |
|-------|--------|
| **Authors** | Shidu Ren, Yunze Liu, Xing Liu, Chi-Hao Wu, Enmin Zhou, Junxiao Shen |
| **Institution** | Not stated |
| **Submitted** | 2026-09-03 · [2609.04438](https://arxiv.org/abs/2609.04438) · cs.CV |
| **Abstract** | Long-horizon multimodal agents should remember *who* participated, not just *what* happened — linking recurring faces, voices, names, objects, events, and social relations to consistent identities over time. ICM-Bench is the first benchmark isolating **identity-centric reasoning over long video memory**: 839 synthetic clips (141 min) and 1,217 open-ended questions about six recurring adults in a one-year life album, with a theme-configurable generation pipeline associating each question with target identities and traceable supporting evidence. Gemini 3.1 Pro tops out at **74.0%** overall but falls to **60.3%** on questions requiring long-term identity profiles; graph-retrieval and memory-augmented baselines lag further. |
| **Key innovations** | First identity-centric long-video memory benchmark; synthetic-but-traceable evidence; quantifies the identity-accumulation gap (event memory recovers, person-profile memory does not). |
| **Why it matters** | Complements the week's agent-memory papers (2609.04915, 2609.05339) and MemTrapBench from earlier digests with a *person-level* axis; the profiles-vs-events gap is a concrete failure mode for agent memory designs. |

---

## ⑤ LLM Architecture, Efficiency & Memory (3)

### 5.1 What Attention Recalls and Recurrence Controls in Hybrid Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Kirill Afendulev, Alexey Dontsov, Elena Tutubalina, Anton Korznikov |
| **Institution** | Kazan Federal University / AIRI *(inferred: Elena Tutubalina, Anton Korznikov)* |
| **Submitted** | 2026-09-03 · [2609.04434](https://arxiv.org/abs/2609.04434) · cs.CL · Findings of EMNLP 2026 |
| **Abstract** | Hybrid LMs combine attention with a fixed-size recurrent state, but each channel's role was unclear. Two cache-level interventions: **split-prefill** (keep only the KV cache or only the recurrent state from a prefilled context, then generate) and **state-swap** (pair one context's KV cache with another's recurrent state in a single forward pass). On Qwen3.5 and Falcon-H1, the channels split sharply by function: **exact retrieval survives only through attention** (64–98% of full accuracy; collapses to zero via recurrence), while output language and persona reverse the pattern (recurrence preserves 70–80% and 3–5×; KV-only drops to ~1% language accuracy). State-swap confirms causality: the answer takes its value from the KV side, its language from the recurrent side. |
| **Key innovations** | First causal, cache-level decomposition of hybrid-LM memory channels; "attention = lookup over what was said; recurrent state = shapes how it says it next"; code released (`kirillTerra/split-prefill`). |
| **Why it matters** | Gives hybrid architectures (NVIDIA's Mamba-Attention MoE, DeepSeek's CSA/HCA, Kimi's KDA) an interpretability handle on what to route where — useful both for architecture design and for the wiki's hybrid-LM coverage. |

### 5.2 Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models

| Field | Detail |
|-------|--------|
| **Authors** | Xing Chen, Hengshuai Yao |
| **Institution** | Not stated |
| **Submitted** | 2026-09-04 · [2609.04575](https://arxiv.org/abs/2609.04575) · cs.LG |
| **Abstract** | Fine-grained MoEs route each token to a small top-k and **renormalize** router probabilities — implicitly calibrating expert output gain to the training top-k. Reducing k at inference changes both which experts are used *and* the strength of the expert branch. The authors separate these effects by activating the top k₁ experts while normalizing by the probability mass of the top k₂ experts — **one integer, no parameters, training, or measurable compute overhead**. On Qwen3.6-35B-A3B, 8→4 experts costs 4.65 MMLU points under standard renormalization but only 0.35 with k₂=16, halving routed-expert compute; replicated on Qwen3.5-397B-A17B (10→5: −0.55 pts). Removing renormalization entirely is catastrophic. Perplexity and accuracy favor different k₂ — don't tune MoE compression on unlabeled text alone. |
| **Key innovations** | Reference-mass normalization (`k₂`) as a zero-cost inference knob for MoE; evidence that expert *identity* matters more than expert *weighting*; balanced/domain-specialized routing leaves limited pruning room. |
| **Why it matters** | Sits exactly on this week's inference-cost line (ACE expert skipping, KVMem, layer-dropout revival): another inference-only lever that halves routed compute with ~0 accuracy loss. |

### 5.3 When Quantization Breaks Memory: Recurrent-State Write-Back in Low-Precision Temporal Inference

| Field | Detail |
|-------|--------|
| **Authors** | Ismail Erbas, Xavier Intes, Vikas Pandey |
| **Institution** | Rensselaer Polytechnic Institute *(inferred: Xavier Intes)* |
| **Submitted** | 2026-09-03 · [2609.04490](https://arxiv.org/abs/2609.04490) · cs.AI |
| **Abstract** | In quantized recurrent networks the quantized state is stored and returned at the next time step, so the storage rule can alter subsequent computation. The paper names this **recurrent-state write-back** and isolates it in a compact GRU encoder-decoder for fluorescence lifetime imaging (estimating short- and long-lifetime parameters τ1/τ2 from high-noise signals). Holding the trained model fixed, deterministic 4-bit state storage increases estimation errors ~70× and ~300×. Failure mode: repeated small updates below the write threshold leave the stored state nearly fixed while the network keeps proposing change. **Error feedback, residual memory, and direction memory** carry suppressed-update information across time and recover accuracy without retraining; the pattern repeats in an LSTM (cell state more sensitive than hidden state). |
| **Key innovations** | Formalizes the state-storage interface as a primary design consideration for quantized recurrent inference; post-training interventions (error feedback etc.) that recover accuracy without retraining; precision sweeps show *more* precision can worsen a fixed solution while compatibility can be learned. |
| **Why it matters** | Quantized-then-deployed sequence models are everywhere in this wiki's efficiency/edge lines; "the write-back rule is part of the model" is a subtle failure mode most quantization papers never check. |

---

## ⑥ Finance, Risk & Industrial Systems (4)

### 6.1 Why Better Models Can Create Riskier Systems: Evidence from LLM Agents in Financial Markets

| Field | Detail |
|-------|--------|
| **Authors** | Jillian Ross, Eric So, Zoe De Simone, Charles Pozniak, Andrew W. Lo |
| **Institution** | MIT Sloan *(inferred: Lo / So)* |
| **Submitted** | 2026-09-03 · [2609.04373](https://arxiv.org/abs/2609.04373) · cs.AI |
| **Abstract** | LLMs are deployed at scale in consequential systems, from markets to moderation to hiring. This paper shows **improving individual capability can degrade rather than improve system-level outcomes**: shared training and architectures may make more capable LLMs behave *more* similarly, creating correlated actions that don't diversify away. A general framework derives how this correlation creates a **non-diversifiable risk floor**, tested in an agent-based simulation with LLM traders of varying capability. Findings: (1) frontier LLMs show correlated behavior that increases with capability; (2) when shared reasoning is accurate, more agents reduce market risk; (3) under a shared misinformation environment, the same correlation becomes a liability — the "capability paradox". |
| **Key innovations** | First formalization of non-diversifiable risk floor from correlated LLM behavior; capability-correlation hypothesis tested in financial-market simulations; raises a new evaluation axis (system-level, not model-level). |
| **Why it matters** | Pairs naturally with 6.2 (below) and the wiki's multi-agent co-failure line (Agent Behavioral Contracts II). The "better models, riskier systems" framing is likely to generalize beyond finance. |

### 6.2 When Financial Fine-tuning Fails: A Three-Level Detectability Analysis of Numerical Hallucination in Domain-Adapted Language Models

| Field | Detail |
|-------|--------|
| **Authors** | Xiaodong Li, Peiwei Liu |
| **Institution** | Not stated |
| **Submitted** | 2026-09-04 · [2609.04806](https://arxiv.org/abs/2609.04806) · cs.AI · Neurocomputing (DOI 10.1016/j.neucom.2026.135011) |
| **Abstract** | Financial LLMs are deployed to summarize reports/disclosures where **numerical hallucination** is risky. Prior work blames insufficient numerical reasoning, untested under controlled fine-tuning. This controlled study compares a base instruction-tuned model, a domain language-adapted model (FT-A), and a numeracy-enhanced model (FT-A+B+C), using a three-level detectability taxonomy — overt (currency fabrication), covert-explicit (professional-convention numbers), covert-implicit (ungrounded quantitative claims). Domain fine-tuning **substantially degrades numerical restraint at every level**: Base stays near-zero (5.4%), FT-A hits 82.5% overt hallucination, FT-A+B+C 98%. Numeracy supervision *amplifies* rather than mitigates hallucination. The primary mechanism is **template injection** — memorized canonical values inserted regardless of input. |
| **Key innovations** | Counter-intuitive controlled result (numeracy supervision worsens hallucination); template-injection mechanism; three-level detectable taxonomy as an evaluation protocol; recommends grounding-aware generation/abstention in deployment. |
| **Why it matters** | A caution for every finance/survey LLM line in this wiki: domain adaptation can trade away restraint even as reasoning improves — and the template-injection mechanism likely transfers to other regulated domains. |

### 6.3 REACT: Tuning Collective Patterns to Alleviate Congestion in Shared AI Clusters

| Field | Detail |
|-------|--------|
| **Authors** | Eashan Gupta, Yongzhou Chen, Apoorve Mohan, Pavlos Maniotis, Abdullah Kayi, Radhika Mittal |
| **Institution** | University of Illinois Urbana-Champaign *(inferred: Radhika Mittal)* |
| **Submitted** | 2026-09-03 · [2609.04417](https://arxiv.org/abs/2609.04417) · cs.NI |
| **Abstract** | Distributed AI training does recurring rounds of GPU-node data exchange; a slowdown in one flow can stall a whole round. Current congestion fixes assume global workload control or infrastructural support (adaptive switch routing), which don't hold in shared clouds where other tenants' jobs create external congestion. REACT works at the **application/communication-library layer**: it detects congestion at runtime from available flow stats and *tunes the collective pattern* — changing the set of incident flows while preserving the semantics of information exchange (e.g., which node aggregates data in an AllReduce tree). No network-infrastructure support needed; deployable unilaterally by individual users. |
| **Key innovations** | First congestion-avoidance at the collective-pattern level with unilateral deployment; NCCL shim prototype improves communication performance (algorithm bandwidth) **13–38%** on a shared academic GPU cluster under congestion, up to **75%** in simulations. |
| **Why it matters** | Training-infrastructure efficiency is a wiki-tracked systems theme; "unilateral, infra-free" is a meaningful differenliator vs. scheduler-centric or switch-centric approaches — directly actionable for LLM pretraining shops on shared fleets. |

### 6.4 Long Horizon Transformer Quantile Fault Prediction for Multi-Site Industrial Predictive Maintenance (TQRNN30d)

| Field | Detail |
|-------|--------|
| **Authors** | David J Poland, Daniele Ravi, Na Helian |
| **Institution** | University of Hertfordshire *(inferred: Na Helian)* |
| **Submitted** | 2026-09-04 · [2609.04840](https://arxiv.org/abs/2609.04840) · cs.AI |
| **Abstract** | Long-horizon predictive maintenance (planning windows in days, not hours) must distinguish slowly evolving degradation from normal operating-regime variation. TQRNN30d couples a **dual-stage quantile regression neural network (QRNN) feature extractor** with a multi-stream temporal fusion classifier: each hourly word of 81-channel machine behavior maps to a 324-dim quantile-state representation, and 720 hourly words form a 30-day document. The classifier fuses quantile states with dynamic covariates, channel-level static metadata, and a 168-hour latent-history stream via gated residual processing, causal recurrent encoding, and metadata-conditioned cross-modal attention; a bounded instability-aware signal (from one-word-ahead prediction-error divergence) modulates memory at the longest horizon. |
| **Key innovations** | Explicit conditional-quantile representation as an informative classifier interface for 30-day fault prediction; machine-disjoint 43/14/15 split across 72 machines in 9 facilities; at 30 days achieves **79.97% F1 / 82.39% acc / 0.820 AUROC**, leading all 18 baselines at 7/14/30 days — while honestly refusing unseen-site or cross-equipment generalization claims. |
| **Why it matters** | A distinctive quantile-interface design for long-horizon temporal forecasting — connects the wiki's sequential-modeling line (PRICE, MomentQuant, RCBNB-MB) to industrial predictive maintenance with rigorous held-out-machine evaluation. |

---

## Cross-Cutting Themes (2026-09-08)

1. **Memory is the new design surface — across every subfield this week.** Writable graph memory for KG-based rec (CGM-Rec), provenance-selective replay for agent unlearning (2609.04875), versioned skill libraries (2609.04869), identity-centric long-term memory benchmarks (ICM-Bench), recurrent-state write-back (2609.04490), KV-vs-recurrent channel roles in hybrids (2609.04434). The shared move: treat memory as an explicit, writable, queryable artifact — not just implicit in weights.
2. **"Better" is being re-audited at the system level.** Better financial models can create riskier markets (6.1); better numeracy supervision amplifies financial hallucination (6.2); multi-harness recipe differences vanish against harness variance (3.1); reward-proxy improvement *is* the hacking vector (3.2); skill libraries work but their benefits are conditional (4.1). A coherent correction to naive "improve the component, improve the system."
3. **Evaluation-harness discipline is the new correctness gate.** Sealed SWE oracle variance (4.3×, 3.1), ττ-bench's 82% expert ceiling vs. 23.9% best agent, machine-disjoint verification with openly-declared non-generalization (6.4), and leak-tested unlearning audits (4.2) all insist: measure through the deployment interface, not the training metric.
4. **Inference-only / training-free levers keep compounding.** 0.05%-token supervision (3.3), single-integer `k₂` reference mass halving MoE routed compute (5.2), >95% per-user parameter cuts (1.3), $27.72 of LLM budget breaking human records (3.4), test-time-only memory-write adaptation (1.1). "Free lunch" results are stacking up across post-training, serving, and personalization.
5. **Cold start / data starvation is a shared bottleneck across domains** — game matchmaking (CHAMP), user-centric LLM personalization (Aplaud/PLUME), KG rec under intent drift (CGM-Rec), and industrial fault prediction (6.4). Cross-domain transfer / shared structure is the recurring answer.

---

## Methodology Notes

- Sources: `arxiv.org/list/{cs.IR,cs.CL,cs.LG,cs.AI,cs.GT,cs.MA,cs.CV}/recent` pages (lists announced through **Mon 7 Sep 2026**) + individual `/abs/` pages for full abstracts. arXiv Atom API remains unavailable (HTTP 429 rate-limiting).
- Dedup: ~187 candidate IDs from the Mon 7 Sep wave were screened for wiki coverage; every featured ID was **grep-verified absent from `wiki/**`** (20/20), and 0 featured overlaps exist with sibling digests 09-06/09-07 (arxiv-daily, arxiv-ai-search, game-rl-daily, conference-digest, arxiv-paper-check) or 09-08 (arxiv-ai-search, arxiv-paper-check).
- Institutions are stated only when printed on the paper itself; inferences are flagged as *(inferred)* and kept conservative. Some venue attributions (EMNLP'26 Findings, CIKM'26, WISE 2026, Neurocomputing) are as printed on the arXiv metadata.