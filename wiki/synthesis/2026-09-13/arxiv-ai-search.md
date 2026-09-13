---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-09-13
updated: 2026-09-13
sources: [arxiv.org]
tags: [arxiv, AI, LLM, CTR, recommendation, advertising, sequential-modeling, game-AI]
---

# arXiv AI Research Paper Search Report — 2026-09-13

Generated: 2026-09-13 (Sunday). Freshest arXiv window = **Fri 11 Sep 2026 mailing** (submission wave Wed 9 – Thu 10 Sep 2026; no weekend announcements). 20 papers featured in full, all with **0 hits in wiki/ at grep-verification time**.

**Methodology**: Scanned `arxiv.org/list/{cat}/new?show=1000` for cs.AI, cs.LG, cs.CL, cs.IR, cs.GT, cs.MA, cs.CY, cs.NE, cs.SI (New + Cross submissions only; Replacement submissions excluded). 376 unique new+cross IDs scanned. All featured IDs grep-verified 0 hits in `wiki/` at selection time, including against same-day 09-13 siblings.

**Dedup notice**: This report is the AI/LLM-focused sibling of 09-13 [[arxiv-daily]] / [[arxiv-paper-check]] / [[game-rl-daily]] / [[tech-report-digest]]. Papers already covered there were deliberately excluded to avoid wiki duplication — see the Cross-Reference Index at the bottom and `wiki/log.md`.

## Summary Statistics

| Scope | Value |
|---|---|
| Mailing scanned | Fri 11 Sep 2026 (Wed 9 – Thu 10 Sep wave) |
| Unique new+cross IDs scanned | 376 |
| Fresh to the wiki (0 hits at selection) | 298 |
| Featured in full in this report | 20 |
| Cross-referenced to sibling reports | ~14 (see index below) |
| Direct CTR / advertising papers | **0** |

**Advertising/CTR note**: No fresh direct CTR or advertising papers this mailing; the closest reocommerce-adjacent finds (funnel auditing, session co-occurrence/embedding models, generative retrieval) are already covered by 09-12 arxiv-daily/paper-check and 09-13 arxiv-daily. 0 new CTR papers again this window.

---

## 1 LLM Reasoning, Post-Training & Reward Modeling

### 1.1 SOLID — Solver-Informed On-Policy Self-Distillation for OR Language Models (2609.09957)
- **Title**: Beyond Verified Answers: Solver-Informed Self-Distillation for Bootstrapping Operations Research Language Models
- **Authors**: Rui Zhu, Minglong Cao, Chenyu Zhou, Jianghao Lin, Dongdong Ge
- **Institution**: SUFE/SJTU-affiliated (tentative)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.09957
- **Abstract**: LLMs translate natural language into operations-research (OR) formulations. SOLID is a self-improvement framework that needs neither verified answers nor external evaluators: it executes candidate programs from multiple rollouts, clusters their *objectives*, and selects a majority-group artifact as a pseudo-reference, then updates with group-relative advantages plus dense self-supervision. Improves solution accuracy on OR benchmarks over outcome-only group-relative training, for both general-purpose and OR-tuned base models.
- **Key Innovations**: First "evaluator-free dense supervision" pipeline for OR formulation training; solver artifacts (not labels) as the pseudo-reference; addresses the three known limits of OR post-training (label scarcity, coarse credit assignment, style mismatch from privileged solver context).
- **Venue**: Preprint.

### 1.2 GenV — Generative Reward Models for Autoformalization (2609.11085)
- **Title**: Beyond Solver Verdicts: Generative Reward Models for Autoformalization
- **Authors**: Vikash Singh, Debargha Ganguly, Aman Goel, Ali Torkamani, Xiaoxue Han, Joseph Lilien, Ferhat Erata, Vipin Chaudhary
- **Institution**: Case Western Reserve / Yale-affiliated (tentative)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.11085
- **Abstract**: Solvers are blind to whether a formal translation preserves reference-equivalence — formalized as **Verdict-Preserving-Unfaithfulness (VPU)**. GenV distills an offline Z3-equivalence oracle into a reference-free continuous score using the LM's native vocabulary space. Mechanistic analysis (logit lenses + sparse autoencoders) shows the readout extracts spatial error coordinates without explicit localization training. GenV+HN reaches 0.961 AUROC on reference-equivalence verification, generalizes zero-shot across translators/styles, and yields +11.3 accuracy points in agentic test-time compute allocation.
- **Key Innovations**: Formalizes VPU failure mode and proves verdict-only heuristics are chance-limited; generative (embedding-level) verifier over a hard symbolic oracle; error-localization emerges for free.
- **Venue**: Preprint.

### 1.3 NCP-ArchPreview — Latent-Space LM via Next Concept Prediction (2609.10715)
- **Title**: NCP-ArchPreview Technical Report: Moving towards Latent Space Language Models through Next Concept Prediction
- **Authors**: The Intern-NCP Team (28 authors incl. Dahua Lin, Zhouhan Lin, Bowen Zhou, Yifan Liu, Yalong* — see arXiv for full list)
- **Institution**: Shanghai AI Laboratory (InternLM team)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.10715
- **Abstract**: A latent-space LM that adds **Next Concept Prediction (NCP)** — predicting discrete multi-token concepts — alongside NTP. Builds a product-quantized concept vocabulary directly from hidden states, trains a Concept Module to predict future concepts, and feeds predictions back to token level; NTP+NCP trained jointly end-to-end. Scaled to 8.9B params / 5.73T tokens on Dolma-3 — the largest latent-space LM demonstration to date.
- **Key Innovations**: Reaches OLMo-3-7B's final pretraining loss with only 51.3% of training tokens; +2.45 macro-avg over OLMo-3-7B downstream (+5.99 on GSM8K). Updating only the 17M-param VQ module yields a lightweight domain-adaptation interface; injecting concept reps into a DFlash2 drafter improves mean accepted length +4.17%.
- **Venue**: Technical report.

## 2 Alignment, Safety & Cultural Bias

### 2.1 Off-Target Effects of Response-Style Alignment in a Korean 27B LM (2609.11291)
- **Title**: Off-Target Effects of Response-Style Alignment in a Korean 27B Language Model
- **Authors**: Hyojung Han
- **Institution**: — (single author)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.11291
- **Abstract**: Post-trains Qwen3.8-27B (27B) for Korean *response style* (verbosity, list/markdown usage, register) and measures two non-target behaviors: KoBBQ abstention rate and unprompted disclosure in securities guidance. Both move, primarily via **answer propensity (emission policy)**, not latent preference. Three style seeds give positive answer-rate point estimates (mean +0.82 pp), three neutral seeds negative (mean −1.53 pp); seed ranges don't overlap.
- **Key Innovations**: Careful experiment on style-only alignment (target text fixed, prompts/recipe/data/serving fixed) and clear negative methodological results: between-arm conditional-stereotype contrast does **not** identify preference change when answer status is treatment-dependent; two rule detectors for the same construct agree 0.44–0.99 depending on checkpoint.
- **Venue**: Preprint.

### 2.2 WORLDVIEW — Prompt Revision as Cultural Bias Source in T2I (2609.11532)
- **Title**: Prompt Revision as a Source of Cultural Bias in Text-to-Image Systems
- **Authors**: Aleksandra Urman, Elsa Lichtenegger, Salima Jaoua, Azza Bouleimen, Robin Forsberg, Corinna Hertweck, Stefania Ionescu, Nicolò Pagan, Ancsa Hannak, Joachim Baumann
- **Institution**: University of Zurich (tentative)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.11532
- **Abstract**: Commercial T2I systems revise prompts silently (invisible, undisablable). WORLDVIEW is a multilingual benchmark of 8,960 prompts, 15 languages, 31 language-context pairings, auditing the revision layer of DALL-E-3, Imagen-4, GPT-Image-1.5. US is least-marked; non-Western/non-Anglophone contexts are over-marked, flattened into narrow vocabularies across topically diverse prompts, and reduced to recognizable stereotypes. Comparing original vs revised prompts identifies the revision layer as a causal source of stereotyping.
- **Key Innovations**: Audits the *deployed pipeline* (revision layer), not the model in isolation; attributes cultural bias to a previously undocumented layer.
- **Venue**: **EMNLP 2026**.

## 3 LLM Interpretability & Mechanistic Analysis

### 3.1 Distribution-aware Language Neuron Identification (2609.10993)
- **Title**: Distribution-aware Language Neuron Identification in Multilingual Large Language Models
- **Authors**: Minjun Kim, Inho Won, Junghun Yuk, Dongyeon Kim, Jihyo Kim, KyungTae Lim
- **Institution**: Korea academia (tentative)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.10993
- **Abstract**: Existing language-neuron ID uses entropy over per-language *binary* activation probabilities (positive vs not). The paper proposes clustering languages by pairwise **overlap coefficients over full activation distributions** (including negative values). Across two mLLMs and two held-out corpora, the identifier yields up to **4.9× higher on-target language damage per neuron** while preserving off-target performance.
- **Key Innovations**: Distribution-aware (not activation-threshold) neuron selectivity; captures the fact that language representations are distributional and mutually related.
- **Venue**: **EMNLP 2026**.

### 3.2 MUtE — Concept Erasure + Counterfactual Interventions (2609.11253)
- **Title**: MUtE: A Dual Framework for Concept Erasure and Counterfactual Interventions
- **Authors**: Antoine Saillenfest
- **Institution**: — (not specified)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.11253
- **Abstract**: Revisits the optimal bounds of concept erasure to derive a class of erasure functions that naturally induce a *deterministic dual counterfactual mapping*. Imposes a translational bias on counterfactual trajectories — consistent with how concepts geometrically manifest in modern LMs — enabling seamless navigation between erasure and counterfactual generation. Improves downstream algorithmic fairness and generates counterfactual texts.
- **Key Innovations**: Bridges theoretical optimality and practical representation learning through one framework with a built-in dual mapping.
- **Venue**: Preprint.

## 4 Inference-Time Routing & Decoding Control

### 4.1 Routing by Reasoning Need: Trajectory-Aware Decoding Control (2609.11315)
- **Title**: Routing by Reasoning Need: Trajectory-Aware Decoding Control for Diffusion Vision-Language Models
- **Authors**: Yixiang Liu, Zhongxing Xu, Zhonghua Wang, Xiaoying Tang
- **Institution**: SUSTech (tentative)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.11315
- **Abstract**: Diffusion VLMs expose intermediate answer trajectories. A universal generation length causes "reasoning-budget mismatch": closed questions get over-refined; reasoning-sensitive questions get premature commitment. The training-free controller routes each example to early commitment / baseline / reasoning-supportive decoding using trajectory signals — answer closure, commitment evidence, representation revision pressure — no ground-truth answers. Big gains over fixed long/short decoding and single-rule interventions; gains are *not* explained by output length alone.
- **Key Innovations**: First trajectory-aware per-example decoding routing for diffusion VLMs (LLaDA-V); "route by trajectory state, not universal length".
- **Venue**: **Findings of EMNLP 2026**.

## 5 Scientific IR & Document Grounding

### 5.1 ReGround — Grounding Reviewer Comments in Multimodal Evidence (2609.11460)
- **Title**: ReGround: Grounding Reviewer Comments in Multimodal Evidence
- **Authors**: Serwar Basch, Lizhen Qu, Iryna Gurevych
- **Institution**: TU Darmstadt (UKP lab)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.11460
- **Abstract**: Reviewer comments relate to specific parts of a paper but grounding them is hard for long multimodal docs. ReGround links **10,267 reviewer comments to 16,274 evidence snippets in 3,656 papers** (from original anonymous submissions), using author rebuttal references as high-precision annotation source. Grounding as retrieval: whole-paper retrieval performs poorly, *evidence-type inference is the major bottleneck*, and multimodal evidence is complementary to text-only.
- **Key Innovations**: First large-scale rebuttal-as-annotation dataset for comment grounding; "PeerReview" grounding task with practical importance for scientific document understanding.
- **Venue**: **EMNLP 2026**.

## 6 Agents & Multi-Agent Systems

### 6.1 Defining AI Agents: Compendium of Criteria, Metrics, Benchmarks (2609.11018)
- **Title**: Defining AI Agents: A Compendium of Criteria, Metrics, and Benchmarks
- **Authors**: Mia Lassiter, Brinnae Bent
- **Institution**: Duke-affiliated (tentative)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.11018
- **Abstract**: A survey organized around five dimensions of **agenticness**: environmental interaction, learning and adaptation, autonomy, goal-directed behavior, temporal coherence — and the metrics/benchmarks/eval frameworks for each. Introduces the **Agent Compendium**, a public-facing digital resource.
- **Key Innovations**: Common vocabulary + structured eval taxonomy for agent research; openly maintained compendium resource (agent-compendium link in paper).
- **Venue**: Preprint.

### 6.2 But How Would AI Agents Run a Town's Economy? (2609.11108)
- **Title**: But How Would AI Agents Run a Town's Economy?
- **Authors**: Sajal Regmi, Siddhartha Pudasaini, Chetan Phakami Pun
- **Institution**: Nepal academia (tentative)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.11108
- **Abstract**: 100 memory-equipped LLM agents run a closed, money-conserving spatial economy on real Pokhara Lakeside geography for up to **26 simulated weeks** (2.44M agent decisions, 21.5B tokens, 91 validated runs). Findings: money stops moving — a 12× tourist shock raises revenue 4.62× (extensive 1.50× / intensive 3.07×) but wages move only 1.03× (p=0.42); only 0.3% of 3,981 menu items ever repriced. A randomized cash transfer shows MPC ≈ 3–4%, indistinguishable from zero. Wealth stays near-frozen (ρ=0.964 at 2 weeks) but *not* frozen (ρ=0.832 at 12, 0.752 at 26 weeks). Backing LLM swap moves every outcome (p=0.0039); deleting memory moves nothing detectable.
- **Key Innovations**: Monetary-transmission decomposition (extensive/intensive margin); horizon-dependence of agent-society results; ablation isolation of the "real" knobs (model > memory); full run corpus released with double verification.
- **Venue**: Preprint.

### 6.3 Agent Resilience & Considerate Participation (2609.10724)
- **Title**: Finishing the Task Is Not Enough: Evaluating Agent Resilience and Considerate Participation under Accumulating Challenge
- **Authors**: Yuanchen Bai, Zijian Ding, Angelique Taylor
- **Institution**: Cornell (tentative)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.10724
- **Abstract**: Evaluates 120 simulated healthcare trajectories across 2 generative-AI models and 12 stakeholder-derived tasks under light/medium/heavy accumulating challenge. Two proposed constructs: **operational resilience** (recovering from blocked work, preserving progress, communicating limits) and **considerate participation** (adaptation accounting for affected people, role boundaries, surrounding workflow). Agents shift from self-directed recovery toward human dependence under load, broaden from task-focused to task-reframing/coordination, report strain in structured reports but not in text.
- **Key Innovations**: Proposes the two eval constructs + five "deployment dilemmas" (persistence, attention, role boundaries, state disclosure, escalation); goal is stakeholder-specifiable evaluation.
- **Venue**: Preprint.

### 6.4 Reproducibility in the Age of Agentic AI (2609.11728)
- **Title**: Reproducibility in the Age of Agentic AI: Context Engineering at the Timescale of a Codebase
- **Authors**: Lorena A. Barba
- **Institution**: George Washington University
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.11728
- **Abstract**: Argues reproducible-research practices (tests, commit history, repo structure, instructions, decision records) ARE **context engineering for AI coding agents**. Agents lower the maintenance cost of these artifacts while making benefits immediate — it's a timescale gap (codebase-scale context vs paper-scale context). Researchers remain responsible for verification and the scientific judgments encoded.
- **Key Innovations**: Repos positioning: the paper ties reproducibility practice to agent context engineering; kew word: "context engineering at the timescale of a codebase".
- **Venue**: Preprint.

### 6.5 MAPLE — Memory-Augmented Planning with Language and Evolution (2609.11636)
- **Title**: MAPLE: Memory-Augmented Planning with Language and Evolution
- **Authors**: Kesheng Chen, Yamin Hu, Wenjian Luo
- **Institution**: USTC (tentative)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.11636
- **Abstract**: LLM-based optimization agents translate NL requirements into solver programs, but real ops-world demands ongoing updates. MAPLE is an agent that **maintains optimization problems through successive NL requests**: retains the optimization program, accepted plans, earlier updates, and candidate solutions. Introduces **NLDO** benchmark (15 trajectories, 180 updates: selection, scheduling, rostering, routing, cloud-placement). Completes all trajectories, online scalar quality 0.951, Pareto hypervolume ratio 0.875.
- **Key Innovations**: Memory-augmented continuing optimization; executable-state maintenance improves update validity and preserves useful search info across revisions.
- **Venue**: Preprint.

### 6.6 BenchShield — Formal Instrumentation for Reward Integrity (2609.11028)
- **Title**: BenchShield: Formal Model-Backed Instrumentation for Reward Integrity in LLM-Agent Evaluation Infrastructure
- **Authors**: Shenghan Zheng, Zonglin Di, Yimin Liu, Kyoung Whan Choe, Jiankai Sun, ... Dawn Song, Christophe Hauser
- **Institution**: UC Berkeley (Dawn Song) / USC-ISI (Christophe Hauser) (tentative)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.11028
- **Abstract**: LM-agent benchmarks are interactive eval infrastructure, vulnerable to reward hacking. BenchShield is a model-backed instrumentation layer grounding detection in a finite lifecycle model of reward-relevant events: static phase-aware taint analysis (pre-run) + runtime attribution with evidence-backed claims. New corpus **BenchShield Trajectories** — 456 adjudicated trajectories from 31,000+ public runs across 3 benchmarks. Improves full-chain recall 23-94% → 77-100%, same-vector coverage 16-56% → 43-78%, −65% per-task cost; 96% runtime reward-hacking detection accuracy.
- **Key Innovations**: First reusable, formal lifecycle-model-based reward-integrity layer (vs task-specific patches/post-hoc detectors).
- **Venue**: Preprint.

## 7 Cooperative AI, Games & RL

### 7.1 The Convention Gap — Implicit Communication in Cooperative AI (2609.11489)
- **Title**: The Convention Gap: Towards Measuring Implicit Communication in Cooperative AI Evaluation
- **Authors**: Makoto Fukushima, Hua-Dong Xiong, Ehsan Moradi Pari
- **Institution**: — (not specified)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.11489
- **Abstract**: Human cooperation relies on **implicit conventions** (shared protocols beyond literal message meaning), which AI-AI benchmarks may not capture. Proposes the *convention gap* = predicted failure probability from literal content − observed failure rate. In Hanabi, gap = +26.2 pp for human pairs, −0.7 pp for AI pairs, +16.4 pp human-AI, concentrated on unhinted plays (+46 pp). Within human-AI play, literal info was similar across 3 AI partners (38–41%) but human failure ranged 14.4–34.4% and gap +24.1 → +6.2 pp. Known-answer check with Off-Belief Learning agents: +1.6 pp convention-free → +21.7 pp as conventions appear.
- **Key Innovations**: First quantifiable implicit-communication metric for cooperative AI; suggests convention compatibility — not AI-AI score — predicts AI effectiveness with humans.
- **Venue**: Preprint.

### 7.2 G2QDR — Dense Reward Learning with Directed State Graphs (2609.10781)
- **Title**: From Connectivity to Rewards: Dense Reward Learning with Directed State Graphs
- **Authors**: Shuyuan Zhang, Zihan Wang, Xiao-Wen Chang, Doina Precup
- **Institution**: McGill / Mila (tentative)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.10781
- **Abstract**: Graph-based Goal-Conditioned Hierarchical RL (GCHRL) methods typically use the graph as a stochastic sampler, ignoring connectivity/state-accessibility intrinsic in quasimetric (asymmetric-transition) environments. G2QDR introduces a state connectivity model predicting pairwise connectivity strength in asymmetric envs, converts these into **scalar auxiliary dense rewards** across hierarchical levels (theory: integrates into any GCHRL). Empirically boosts baseline GCHRL on sparse-reward envs at acceptable compute cost.
- **Key Innovations**: Quasimetric-dense-reward framing; connectivity model trained on a directed state graph built during exploration.
- **Venue**: Preprint.

## 8 Video Generation & World Models

### 8.1 Vidu S2 — Real-Time Interactive, Editable, Spatial Video (2609.11638)
- **Title**: Vidu S2: Real-Time Interactive, Editable, and Spatial Video Generation
- **Authors**: Jintao Zhang, Kai Jiang, Jintao Chen, Xu Wang, ... Jun Zhu (BAAI/ShengShu lineage)
- **Institution**: ShengShu / Tsinghua (tentative)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.11638
- **Abstract**: Two real-time models: **Vidu S2-Avatar** (interactive digital character; 720p real-time generation, dynamic references updated at any moment, stronger instruction following incl. dancing) and **Vidu S2-Editing** (real-time editing: style rendering, clothing/character/background replacement), plus exploration of real-time *spatial* video generation for both. Outperforms all baselines; playable online demo.
- **Key Innovations**: Real-time interactive/editable video at 720p; per-frame dynamic reference updates; real-time editing of a *stream*.
- **Venue**: Preprint.

## 9 Reasoning Benchmarks

### 9.1 MindTopo — Foundation Models Reasoning in Topological Space (2609.11900)
- **Title**: MindTopo: Can Foundation Models Reason in Topological Space?
- **Authors**: Yunfei Ge, Anbang Liu, Qineng Wang, Johnalbert Garnica, Jianwen Lyu, Zihan Wang, Reuben Tan, Jianfeng Gao, Ruohan Zhang, Yining Hong, Jiajun Wu, Manling Li
- **Institution**: UIUC (Manling Li) + multi-institution (tentative)
- **Date**: Announced 11 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.11900
- **Abstract**: Spatial reasoning also needs **topological relations** (invariant under continuous deformation): continuity, separation, order, enclosure, knots. MindTopo = 11,030 instances, 13 procedurally-generated task types, two levels (reasoning vs closed-loop planning with FMs as agents). Benchmarking 14 MLLMs + agent configs with image/video generators: every model better at reasoning than planning; best model far below humans. On Qwen3-VL-2B, SFT+RL improves reasoning more than planning; generated observations keep local cues but audited rollouts don't reliably preserve environment dynamics/topology.
- **Key Innovations**: First topological-reasoning benchmark grounded in cognitive science; exposes planning gap + unreliable topology-preservation in generated world-model rollouts.
- **Venue**: Preprint.

---

## Key Trends Across This Window

1. **Verifiable-rewards / solver-grounded self-improvement** (SOLID, GenV): instead of judging by LLM judges, ground LLM training/eval in *solver artifacts* (objective clusters, Z3 equivalence oracles). Complements the judge-validity skepticism elsewhere on the wiki (e.g. 09-13 arxiv-paper-check, 09-12 arxiv-paper-check).
2. **Post-training side effects, measured carefully** (Off-Target Alignment): response-style alignment moves *emission policy* (abstention, disclosure rate), with constructive negative results about what naive conditional comparisons can/cannot identify.
3. **Latent-space LM / NCP**: 8.9B-param NCP result (OLMo-3-7B match at 51.3% tokens) is the largest data point yet for "beyond next-token" pretraining — tie-in to Intern-NCP / Intern-S2 on this wiki.
4. **Evaluation infrastructure as a first-class security problem** (BenchShield): reward hacking now gets formal lifecycle-model-based instrumentation, with a 456-trajectory adjudicated corpus.
5. **Convention gap / human compatibility for cooperative AI** (Convention Gap): AI-AI eval ≠ human compatibility; measure implicit conventions, not just score.
6. **From model audit to deployed-pipeline audit** (WORLDVIEW): cultural bias can be *introduced* by private pipeline layers (revision), invisible when auditing the model alone.
7. **Power-aware AI infrastructure** (Power Flexibility Index): first systematic *characterization* of training-job power elasticity; new metric for grid-responsive AI (ties to this week's energy/AI-infra investment threads).

## Ads / CTR Coherence Check

0 direct CTR/ads papers this mailing. The 09-12 and 09-13 siblings cover the rec-adjacent finds (funnel auditing, embedding-based session co-occurrence, retrospective self-consistency in recommender MDPs, bidding-game collusion). No new ads material to flag.

## Cross-Reference Index (Sibling-Covered IDs)

Notable IDs from this mailing covered elsewhere, not re-listed here:
- **2609.11414** SWRouter (LLM serving) → 09-13 [[arxiv-paper-check]]
- **2609.10862** Project Qualia (Song2Vec music embedding) → 09-13 [[arxiv-paper-check]]
- **2609.11709** When Agents Disagree → 09-13 [[arxiv-paper-check]]
- **2609.11115** Benchmark Radar (living benchmark DB) → 09-13 [[arxiv-paper-check]]
- **2609.11490** Published-unlearning-numbers audit → 09-13 [[arxiv-paper-check]]
- **2609.11607** ClimateLLM-alt-data agents → 09-13 [[arxiv-paper-check]]
- **2609.11234** NovGauge → 09-13 [[arxiv-daily]]
- **2609.11655** Musec → 09-13 [[arxiv-daily]]
- **2609.11020** K/V-cache trajectory interventions → 09-13 [[arxiv-daily]]
- **2609.10996** Verbalized Confidence shift → 09-13 [[arxiv-paper-check]] / study also appeared in 2609.10996 scan
- **2609.11067** Noise Fabricates Bias → 09-13 [[arxiv-paper-check]]
- **2609.11548** World in World (video WM interface) + PMMS/fair-division & NSD game theory wave (2609.06282/08954/10493/07062/07136...) → 09-13 [[game-rl-daily]]