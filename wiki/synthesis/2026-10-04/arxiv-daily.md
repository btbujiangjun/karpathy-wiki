---
title: arXiv Daily 2026-10-04 — AI / LLM / Recommendation / Ads / Sequential / CTR / Games
type: synthesis
created: 2026-10-04
updated: 2026-10-04
sources: [arxiv-api]
tags: [arxiv, arxiv-daily, llm, post-training, agents, inference, recsys, ctr, advertising, sequential-modeling, rl, games, multimodal, evaluation]
---

# arXiv Daily — AI / LLM / Recommendation / Ads / Sequential Modeling / CTR / Games (2026-10-04)

**Window.** arXiv submissions dated **2026-09-30 → 2026-10-01** (IDs `2609.388xx`–`2609.403xx` and `2610.003xx`–`2610.022xx`). 2026-10-04 is a Sunday, and arXiv's newest indexed submission date is still **2026-10-01** — verified directly: a `submittedDate:[202609280000 TO 202610020000 / 202610030000 / 202610040000]` query on `cs.LG` returns an identical `totalResults=1602` for all three end dates, i.e. **no 10-02, 10-03 or 10-04 submission block is indexed**. This is therefore the same freshest block the 2026-10-03 sibling mined, re-swept across a wider category set.

**Contents.** 59 papers in 8 sections. Every entry carries title, authors, institution/company, abstract, key innovations and an arXiv link, as requested.

**Dedup.** The pool was pulled from 14 categories (`cs.AI`, `cs.CL`, `cs.CV`, `cs.CY`, `cs.GR`, `cs.GT`, `cs.HC`, `cs.IR`, `cs.LG`, `cs.MA`, `cs.RO`, `cs.SI`, `eess.SP`, `stat.ML`) sorted by `submittedDate desc`, 1,318 records parsed. A whole-`wiki/` sweep — every `\d{4}\.\d{4,5}` token in every `.md` under `wiki/`, excluding only the file being written — found **7,738 unique arXiv IDs already claimed**, leaving **1,030 unclaimed candidates**. All 59 IDs below were re-verified **0-hit against that baseline**, so no paper here had been written up previously. ⚠️ **This check was initially wrong and was corrected.** A first-pass baseline swept only part of `wiki/`, so it under-counted claimed IDs as 7,669, and an early draft of this report carried **8 papers that were already full entries in `wiki/synthesis/2026-10-02/arxiv-daily.md`** (`2610.02191`, `2610.02039`, `2610.02015`, `2610.02193`, `2610.02057`, `2610.02202`, `2610.02066`, `2610.02022`). All 8 were replaced with fresh unclaimed papers and re-verified. A dedup claim that was not re-checked against the tree it claims to describe is worse than no claim, because it is checkable and wrong.

**Affiliation discipline.** Institutions are read from each paper's own LaTeXML author block (`ltx_contact ltx_role_affiliation`) in the arXiv HTML full text, or failing that from an explicit institutional address block in the front matter. They are **never** inferred from author names or email domains. **13 of the 59** papers could not be resolved and are marked inline with the reason and the contact that was deliberately not used — five render bare `Affiliation:` labels with the institution text dropped, three carry no affiliation markup at all, one lists only a collective team name, one renders no author block, one states its institution only in an address block with an empty author block (kept, since the paper says so outright), and two have no arXiv HTML rendition.

---

## LLM Post-Training, Credit Assignment & Reward Design (9)

### 1. Diagnosing On-Policy Self-Distillation for Reasoning Language Models

- **arXiv:** [2609.39118](https://arxiv.org/abs/2609.39118) · submitted 2026-09-30 · primary category `cs.CL` · all categories: `cs.CL`
- **Authors:** Yang Li; Gongle Xue; Yuheng Yuan; Yijia Guo; Shizhe Zhang; Liwen Hu; Lei Ma
- **Institution / company:** Peking University
- **Affiliation evidence:** verified from author block — all seven authors list the same affiliation

**Abstract.** On-policy self-distillation (OPSD) has attracted growing interest as a promising approach to improve the reasoning ability of language models. Without external rewards nor a separate stronger teacher, the self-teacher with privileged information could provide dense signals on student's trajectories. However, its behavior in language reasoning remains unclear, with reported outcomes ranging from modest gains to behavioral collapse. In this work, we diagnose OPSD for mathematical reasoning across models spanning 0.6B--8B parameters. We conduct controlled experiments and token-level analyses to fully delve into OPSD. We point out that teacher's signal is shaped by reasoning-mode alignment and the complete teacher prefix, rather than by privileged semantics alone. OPSD improves reasoning only in narrow compatibility regimes. Otherwise, it produces ineffective length growth, stable degradation, or behavioral collapse. Token-level analysis shows that teacher's signal is not stable and does not predict downstream performance. Based on these results, we argue that OPSD is a sensitive algorithm rather than a generally reliable reasoning-improvement post-training method.

**Key innovations.**

- OPSD gets a **negative verdict** here. Reported outcomes in the literature span modest gains to outright behavioral collapse, and this paper attributes that spread to the *setup* rather than to luck.
- The mechanism claim is the load-bearing part: the teacher's signal is shaped by **reasoning-mode alignment plus the complete teacher prefix**, not by privileged semantics alone — so the "privileged information" framing is not by itself what makes OPSD work.
- Consequence: OPSD improves reasoning **only in narrow compatibility regimes**. Elsewhere it produces ineffective length growth, stable degradation, or collapse.
- Token-level analysis finds the teacher's signal is **not stable and does not predict** downstream performance, which explains why the failure mode looks arbitrary from the outside.
- Scale of the diagnosis: 0.6B–8B models under controlled experiments. The authors' own summary calls OPSD "a sensitive algorithm rather than a generally reliable reasoning-improvement post-training method."

---

### 2. Exploring More, Reasoning Better: Stepwise Risk-Sensitive GRPO for Diffusion Language Models

- **arXiv:** [2610.00661](https://arxiv.org/abs/2610.00661) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`
- **Authors:** Yue YU; Bowen Zuo; David Crandall; Yinglun Zhu; Dongruo Zhou
- **Institution / company:** Indiana University; University of California, Riverside
- **Affiliation evidence:** verified from author block
- **Author comment:** 40 pages, 12 figures, 2 tables. The first two authors contributed equally

**Abstract.** Diffusion large language models (dLLMs) generate text by denoising a sequence or successive blocks, allowing several tokens to be revealed in parallel. Reinforcement learning with verifiable rewards (RLVR) reuses terminal feedback across these decisions, even as their conditioning context changes. We propose stepwise risk-sensitive GRPO (StepRS-GRPO), which varies the risk coefficient of the group-advantage transformation across denoising states while retaining the underlying trainer. For binary rewards, we show that this transformation is exactly a prompt- and state-dependent rescaling of centered outcome advantages. A capability-based calibration suggests a coefficient scale, while endpoint and interpolation ablations guide schedule selection. Across multiple dLLM backbones and mathematical reasoning benchmarks, StepRS-GRPO improves both pass@1 accuracy and pass@k coverage over centered GRPO, while increasing answer diversity. In our ablation studies, mass-matched controls support the contributions of state allocation and schedule direction, and the gains persist after matching the root mean square (RMS) of the advantages to that of centered GRPO. Reasoning-trace diagnostics further show that the diversity gains from StepRS-GRPO extend beyond final-answer strings.

**Key innovations.**

- The mismatch is named precisely: RLVR **reuses terminal feedback across denoising decisions whose conditioning context keeps changing**, so one binary signal supervises many unlike states.
- StepRS-GRPO varies only the **risk coefficient of the group-advantage transformation across denoising states** and keeps the underlying trainer — a deliberately narrow change surface.
- There is a clean theoretical handle: for binary rewards the transformation is **exactly** a prompt- and state-dependent rescaling of centered outcome advantages, which makes the schedule interpretable rather than merely tuned.
- Schedule selection is made auditable — a capability-based calibration suggests the coefficient scale, and endpoint and interpolation ablations pin down the direction.
- The controls are unusually strong: **mass-matched** and **RMS-matched** comparisons against centered GRPO, plus evidence that the diversity gain extends into reasoning traces and not just final-answer strings.

---

### 3. Better Supervision Is Nearby: Neighborhood On-Policy Self-Distillation

- **arXiv:** [2609.39687](https://arxiv.org/abs/2609.39687) · submitted 2026-09-30 · primary category `cs.CL` · all categories: `cs.CL`, `cs.LG`
- **Authors:** Xincheng Wei; Yifan Ding; Yoshua Li; Yuquan Lu; Ziheng Li; Yi Lu; Dongsheng Ma; Rongxiang Weng; Xunliang Cai
- **Institution / company:** ⚠️ **not stated.** arXiv serves **no HTML rendition** for this submission, so no author block could be read. The abs page lists authors only. **Not inferred.**
- **Affiliation evidence:** abs page authors only — no HTML author block available

**Abstract.** On-policy self-distillation (OPSD) trains mathematical reasoning models using a privileged teacher that sees a reference solution and supervises student-sampled prefixes. Standard OPSD uses one fixed parameter setting at every state, but nearby settings may offer additional supervision. We find that local parameter perturbations reveal complementary reference-aligned corrections under the same reference context. Different experts supply these corrections at different reference positions. Their pool covers more such positions than the unperturbed privileged teacher. We introduce Neighborhood OPSD (N-OPSD) to turn these corrections into supervision at student-visited states. Offline, greedy selection builds a compact pool of frozen experts by rewarding filtered reference-token gains beyond the pool's current best at each position. The highest-peak expert need not provide the best training target. Online routing therefore separates the anchor direction from its level of support. MaxPeak selects the anchor token, and quantile selection chooses among experts whose top token matches it. The student learns from the chosen expert's full next-token distribution through the clipped forward-KL objective inherited from OPSD. We evaluate on AIME 2024, AIME 2025, and HMMT February 2025. Across three independent runs per method, Neighborhood OPSD improves the three-benchmark Average@12 over OPSD by 2.75, 1.67, and 1.94 points on Qwen3-1.7B, 4B, and 8B, respectively. Student-prefix continuations support using the pool beyond the reference trajectories used for selection. Matched ablations support filtered reference-token gains as a selection criterion. Accounting for overlap within the pool and routing by state further improve student accuracy. Inference uses only the distilled student.

**Key innovations.**

- The driving observation is that standard OPSD uses **one fixed parameter setting at every state**, while *nearby* settings turn out to carry additional, complementary supervision under the same reference context.
- Offline: greedy selection builds a compact pool of frozen experts, rewarded by **filtered reference-token gains beyond the pool's current best at each position**.
- The sharp point is that the **highest-peak expert is not necessarily the best training target**, so online routing deliberately **separates the anchor direction from its level of support** — MaxPeak for the anchor token, then quantile selection among experts whose top token agrees with it.
- The student trains on the chosen expert's **full next-token distribution** through the clipped forward-KL objective inherited from OPSD; inference still uses only the distilled student.
- Numbers, averaged over three independent runs: Average@12 across AIME 2024 / AIME 2025 / HMMT February 2025 improves over OPSD by **+2.75, +1.67, and +1.94** points on Qwen3-1.7B, 4B, and 8B.
- Worth pairing with §1, which reaches the opposite verdict on the same algorithm: two papers in one window disagree about whether on-policy self-distillation is reliable. The plausible reconciliation is that Neighborhood OPSD replaces the single unstable teacher with a *diverse* pool, and pays for that stability with explicit expert-selection machinery.

---

### 4. Range-GRPO: Policy Optimization via Pairwise Relations among Reward Intervals

- **arXiv:** [2610.01548](https://arxiv.org/abs/2610.01548) · submitted 2026-10-01 · primary category `cs.LG` · all categories: `cs.LG`
- **Authors:** Ryunyi Lee; Kangjun Noh; Somin Kim; Heedong Kim; Kyungwoo Song
- **Institution / company:** Yonsei University
- **Affiliation evidence:** verified from author block

**Abstract.** As the use of large language models (LLMs) expands, post-training has become increasingly important for adapting them to downstream tasks. However, obtaining reliable supervision remains costly, especially in domains without reference answers or executable verifiers. LLM-as-a-Judge provides scalable pseudo-rewards for unlabeled responses, but a single point score does not explicitly represent reward uncertainty. This motivates representing pseudo-rewards as conformally calibrated reward ranges. We propose Range-GRPO, a semi-supervised post-training framework that combines limited labeled data with unlabeled prompts. In Group Relative Policy Optimization (GRPO), learning signals depend on relative reward comparisons within each rollout group. The proposed objective compares reward ranges pairwise rather than reducing them to point rewards, allowing interval uncertainty to affect both the magnitude and direction of these signals. Our theoretical analysis characterizes this distinction and shows that the proposed objective recovers the standard advantage when all reward ranges collapse to points. Empirically, Range-GRPO achieves the highest in-distribution and out-of-distribution average performance among the evaluated semi-supervised methods while requiring fewer training resources.

**Key innovations.**

- Reframes LLM-as-a-Judge pseudo-rewards as **conformally calibrated intervals** rather than point scores, so reward uncertainty is carried explicitly into the objective.
- The key move: GRPO's learning signal is a *relative comparison*, so Range-GRPO compares **reward ranges pairwise**, letting interval uncertainty change both the magnitude *and* the direction of the signal.
- Proves the objective **recovers the standard GRPO advantage in the degenerate case** where every range collapses to a point — a clean sanity property.
- Best in-distribution and out-of-distribution averages among evaluated semi-supervised methods, with fewer training resources.

---

### 5. Rethinking Probability-Based Reinforcement Learning From Posterior Concentration

- **arXiv:** [2610.01458](https://arxiv.org/abs/2610.01458) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`
- **Authors:** Shiu-Hong Kao; Yubo Zhao; Zhenyu Tian; Pengzhan Sun; Yicong Li; Angela Yao
- **Institution / company:** National University of Singapore; The Hong Kong University of Science and Technology; University of Science and Technology of China
- **Affiliation evidence:** verified from author block

**Abstract.** Verifier-free reinforcement learning with probability-based rewards offers a promising way to train LLMs on general reasoning tasks where external verifiers are unavailable. Yet the reliability of these rewards, especially in long-horizon reasoning, remains underexplored. This work identifies a length-dependent failure mode of probability rewards, which we call the Posterior Concentration Phenomenon (PCP). We show that the probability of a reference answer conditioned on a reasoning trace often collapses to a low-variance interval as the trace becomes lengthy. This phenomenon results in nearly indistinguishable rewards, which, under GRPO-based settings, makes probability-based policy optimization unstable and inefficient. Motivated by this, we propose Reinforcement Learning with Concentration-aware Posterior Rewards (RLCPR), a verifier-free RL framework to explicitly account for PCP for better optimization stability and token efficiency. It has two components: uncertainty-aware data sampling, which reduces concentration-prone rollouts before generation, and concentration-aware regularization, which penalizes unnecessarily long traces when posterior rewards collapse. Extensive experiments show that, alongside higher token efficiency, RLCPR outperforms the state-of-the-art verifier-free RL baseline by up to 4.0% on six of seven benchmarks, including general-domain and mathematical reasoning challenges.

**Key innovations.**

- Names a failure mode of probability-based rewards that is a *function of trace length*: **Posterior Concentration Phenomenon** — as a reasoning trace grows, the posterior probability of the reference answer collapses into a low-variance interval, so rewards become nearly indistinguishable.
- The consequence is spelled out: under GRPO, near-identical rewards destroy the group-relative signal, making optimization both unstable and token-inefficient.
- RLCPR attacks it from both ends — **uncertainty-aware sampling** drops concentration-prone rollouts before generation, and **concentration-aware regularization** penalizes needless trace length once rewards collapse.
- Up to **+4.0%** over the SOTA verifier-free RL baseline on six of seven benchmarks, with higher token efficiency.

---

### 6. Advancing Entropy-Level Credit Assignment in RLVR via Proximal Entropy Policy Optimization

- **arXiv:** [2609.39402](https://arxiv.org/abs/2609.39402) · submitted 2026-09-30 · primary category `cs.AI` · all categories: `cs.AI`, `cs.LG`
- **Authors:** Yun Kim; Nojun Kwak
- **Institution / company:** Seoul National University
- **Affiliation evidence:** verified from author block
- **Author comment:** 21 pages, 4 figures. **Accepted at NeurIPS 2026**

**Abstract.** Value-model-free RLVR methods such as GRPO assign uniform advantages to all tokens in a rollout, ignoring that tokens contribute unequally. Recent methods use token entropy as an importance proxy but compute it globally across the batch, conflating importance with prompt difficulty and positional trends. We argue that importance should instead be measured relative to the local context of each token. We introduce proximal entropy, a local measure of token importance relative to neighboring tokens, and prove it is invariant to both confounders. Proximal Entropy Policy Optimization (PEPO) uses it to weight per-token advantages and outperforms GRPO and entropy-based baselines on mathematical reasoning across Qwen3-1.7B, Qwen3-4B, and Llama-3.2-3B-Instruct. We also show the formulation generalizes to other algorithms where substituting proximal entropy into existing methods improves, and applying it to single-stream RL succeeds where global entropy fails.

**Key innovations.**

- Diagnoses a **confound** in existing entropy-based credit assignment: entropy computed globally across the batch mixes token importance with prompt difficulty and positional trends.
- **Proximal entropy** measures importance relative to a token's *neighbors*, with a proof that it is invariant to both confounders.
- PEPO uses it to weight per-token advantages; beats GRPO and entropy-based baselines on math reasoning across three models (Qwen3-1.7B, Qwen3-4B, Llama-3.2-3B-Instruct).
- The generality claim is the interesting part: substituting proximal entropy into *other* algorithms also helps, and single-stream RL succeeds where global entropy fails.

---

### 7. Learning Process Rewards via Reasoning State Propagation

- **arXiv:** [2609.39220](https://arxiv.org/abs/2609.39220) · submitted 2026-09-30 · primary category `cs.AI` · all categories: `cs.AI`, `cs.LG`
- **Authors:** Kai Gan; Zi-Hao Zhou; Bo Ye; Jian Zhao; Min-Ling Zhang; Tong Wei
- **Institution / company:** School of Computer Science and Engineering, Southeast University (Nanjing); Key Laboratory of Computer Network and Information Integration (Southeast University), Ministry of Education, China
- **Affiliation evidence:** verified from author block

**Abstract.** Process reward models (PRMs) have demonstrated notable effectiveness in test-time scaling and reinforcement learning by providing fine-grained signals for evaluating intermediate reasoning states, but their training relies heavily on costly process annotations. A natural way to alleviate this dependence is to complement limited process supervision with scalable outcome supervision. However, existing PRMs often model reasoning prefixes independently, providing no explicit mechanism for effectively using final outcome to guide the learning of intermediate reasoning states. We introduce Reasoning State Propagation (RSP), which represents each reasoning prefix with a binary validity state and models transitions between successive states across the reasoning trajectory. Specifically, RSP predicts a break probability that a valid state becomes invalid and a repair probability that an invalid state returns to valid. By propagating these transitions, RSP connects intermediate states to the final state, allowing process annotations to supervise intermediate states while outcome labels supervise the final state and can provide learning signals to preceding steps. Across reasoning search, response selection, and reinforcement learning, RSP consistently outperforms representative PRM baselines, with average improvements over Qwen2.5-Math-PRM of 5.6% in beam search and 2.1% in reinforcement learning.

**Key innovations.**

- Attacks the PRM cost problem structurally: existing PRMs model reasoning prefixes **independently**, so cheap outcome labels cannot teach intermediate states.
- **RSP** gives each prefix a binary validity state and models *transitions* — a **break probability** (valid → invalid) and a **repair probability** (invalid → valid) — so outcome supervision at the end propagates backward.
- The recover/repair framing is what makes it more than a smoothing trick: it models the fact that reasoning goes bad *and comes back*.
- Average gains over Qwen2.5-Math-PRM of **5.6% in beam search** and **2.1% in RL**, consistently across reasoning search, response selection and RL.

---

### 8. Scoring Higher, Answering Worse: Mitigating Reward Hacking in Rubric-Based RL via Protocol-Level Rubrics

- **arXiv:** [2609.38847](https://arxiv.org/abs/2609.38847) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`
- **Authors:** Maoqi Liu; Junwei He; Bowen Zhang; Feiran Li; Wentao Ma; Rongyi Lin; Shuhan Zhong; Quan Fang
- **Institution / company:** Beijing University of Posts and Telecommunications; ByteDance
- **Affiliation evidence:** verified from author block
- **Author comment:** Under Review

**Abstract.** Rubric-based reinforcement learning (Rubric-RL) trains language models where no verifier exists. A judge checks each criterion of a rubric, and the verdicts are aggregated into a reward, most often by a weighted sum. We show that this additive aggregation is the weak point. Under a sum, criteria compensate for one another: a policy that misses the one decision that matters can buy the points back with advice nobody asked for. On clinical consultation, such a policy scores higher and answers worse. Rubric coverage rises while appropriateness on held-out physician criteria falls below the untrained model. The medical criteria are not to blame. Grouped so that they must hold together, the same criteria, unchanged to the word, recover a third of the loss; shorter answers recover almost none. We therefore propose Protocol-level Rubrics (ProRubric), which keeps what the criteria ask for and changes how they are aggregated. It groups a checklist into a few protocol-level dimensions. A dimension counts only when all of its criteria hold and its failure clause does not fire. The grouping is done once, offline, and leaves the optimizer unchanged. ProRubric raises appropriateness by 10.8 points without losing coverage and has the best seven-benchmark average at both scales.

**Key innovations.**

- Isolates the weak point of Rubric-RL as the **aggregation function**, not the criteria: under a weighted sum, criteria *compensate*, so a policy can miss the one decision that matters and buy the points back with unrequested advice.
- The demonstration is a genuine reward-hacking case: on clinical consultation the hacked policy **scores higher and answers worse** — coverage rises while appropriateness on held-out physician criteria falls *below the untrained model*.
- The decisive control rules out the obvious alternative explanation: the criteria are not at fault, since the **same criteria, unchanged to the word**, recover a third of the loss when grouped; shorter answers recover almost none.
- **ProRubric** changes only aggregation (offline grouping into protocol-level dimensions; a dimension counts only if all its criteria hold *and* its failure clause does not fire), leaving the optimizer untouched: **+10.8 appropriateness points** with no coverage loss and the best seven-benchmark average at both scales.
- The stated lesson generalizes past rubrics: *reward validity is set not only by what a rubric verifies, but by how it aggregates.*

---

### 9. Explicit Trajectory Diversity for RL-Based Post-Training of LLM Agents

- **arXiv:** [2609.38805](https://arxiv.org/abs/2609.38805) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`
- **Authors:** Huaiyu Fu; Heng Cao; Hao Wang; Jian Yao; Tao Chen
- **Institution / company:** Microsoft; tuyoogame
- **Affiliation evidence:** verified from author block (one author carries `Affiliation: Microsoft`, four carry `Affiliation: tuyoogame`)

**Abstract.** LLM agents often admit multiple high-quality solutions to the same task, differing in reasoning structure, tool-use pattern, or interaction trajectory. Yet existing notions of diversity in LLM post-training are mostly implicit, arising from general stochasticity and regularization mechanisms rather than explicitly targeting task-relevant behavioral variation. While such implicit diversity can be useful, it does not directly specify which forms of behavioral variation should be encouraged for a given task. In this work, we study explicit trajectory diversity in RL-based post-training for LLMs. Our key idea is to define diversity through user-specified, task-specific trajectory descriptors, which map each sampled trajectory to an interpretable behavioral representation, and then measure diversity as a set-level functional over the resulting descriptor matrix. Building on this formulation, we introduce Trajectory-guided Joint Policy Optimization (TJPO), a single-policy framework that optimizes explicit diversity over sampled trajectory groups, avoiding the need for population-based policy training, and instantiate it within group-based policy optimization through trajectory-level learning signals. This design makes the diversity objective both interpretable and controllable. Experiments on Sokoban and ALFWorld show that TJPO improves task-specific trajectory diversity while maintaining competitive task performance. Descriptor and trajectory analyses show that the learned variation follows the specified behavioral dimensions and includes distinct successful strategies.

**Key innovations.**

- Argues that diversity in LLM post-training is normally **implicit** — a byproduct of stochasticity and regularization — so it never specifies *which* behavioral variation a given task actually wants.
- Makes it explicit and user-controllable: task-specific **trajectory descriptors** map each sampled trajectory to an interpretable behavioral representation, and diversity becomes a set-level functional over the descriptor matrix.
- **TJPO** is a *single-policy* framework, deliberately avoiding population-based policy training — a practical constraint, since most diversity-regularized methods need a population.
- Verified on **Sokoban and ALFWorld**: improved task-specific trajectory diversity at competitive task performance, and descriptor analysis confirms the learned variation actually follows the specified behavioral dimensions and contains *distinct successful strategies* — not just noise.

---

## Agents: Credit Assignment, Memory & Selective Reliance (9)

### 10. T2SPO: Trajectory-to-Step Policy Optimization for Agentic Reinforcement Learning

- **arXiv:** [2610.00388](https://arxiv.org/abs/2610.00388) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`
- **Authors:** Bo-Wen Zhang; Junwei He; Maoqi Liu; Feiran Li; Song-Lin Lv; Wentao Ma; Rongyi Lin; Shuhan Zhong; Lan-Zhe Guo
- **Institution / company:** State Key Laboratory of Novel Software Technology, Nanjing University; School of Intelligence Science and Technology, Nanjing University; ByteDance
- **Affiliation evidence:** verified from author block (numbered front-matter institution list)

**Abstract.** Reinforcement learning enables large language model (LLM) agents to learn multi-step behaviors through interaction with their environments. However, rewards in many interactive tasks reflect only the final outcome, providing limited guidance on which intermediate decisions advance the task. Successful training trajectories contain intermediate states that can provide supervision for subsequent interactions. We introduce Trajectory-to-Step Policy Optimization (T2SPO), a method that uses past interaction trajectories to provide step-level feedback for policy learning. T2SPO derives remaining-distance targets from successful trajectories and pairs them with representations of the states visited along the way. Conditioned on these examples, a pretrained TabPFN regressor estimates the remaining distance to success at each state of a new rollout. Changes in this distance estimate across consecutive states yield auxiliary credit for agent steps alongside task-level supervision. As training proceeds, newly completed trajectories refresh the estimator's context, incorporating new experience without updating its parameters. Experiments with 1.5B and 7B language models on ALFWorld and WebShop show that T2SPO consistently improves overall task success over GRPO.

**Key innovations.**

- Turns the agent's own **successful past trajectories into a step-level supervision signal** — remaining-distance targets paired with the representations of states along the way.
- A pretrained **TabPFN regressor** estimates remaining distance-to-success at each state of a new rollout; the *change* between consecutive states becomes auxiliary per-step credit alongside task-level reward.
- Neat trick: new completed trajectories **refresh the regressor's in-context examples without updating its parameters**, so the estimator improves as the agent does, with no extra training.
- Consistent task-success improvement over GRPO at both 1.5B and 7B on ALFWorld and WebShop.

---

### 11. My FAULT: Self-Diagnosis as Credit Assignment in Self-Evolving Agentic Reinforcement Learning

- **arXiv:** [2610.01161](https://arxiv.org/abs/2610.01161) · submitted 2026-10-01 · primary category `cs.CL` · all categories: `cs.CL`
- **Authors:** Yihua Zhu; Qianying Liu; Weixu Qiao; Xuan Ren; Weiwei Xu; Wenbo Li; Wei Wang; Ruijia Chen; Xinmiao Luan; Yin Luo; Hao Huang; Xiang Zheng; Hidetoshi Shimodaira
- **Institution / company:** ⚠️ **not stated.** The HTML author block renders nine bare `Affiliation:` labels with empty institution text (LaTeXML dropped it). Author emails in the block are `ying@nii.ac.jp` and `qiaoweixu.qwx@alibaba-inc.com`. **Not inferred from email domains.**
- **Affiliation evidence:** abs page authors only — the nine `Affiliation:` labels render with empty institution text
- **Author comment:** Preprint

**Abstract.** Agentic reinforcement learning (RL) has emerged as a powerful approach for training large language model agents on multi-step tasks, yet reliance on terminal outcome rewards creates two credit-assignment problems, particularly in long-horizon tasks. First, same-outcome rollout groups provide no learning signal from terminal rewards. Second, terminal rewards provide only trajectory-wide feedback, making it difficult to identify which decisions caused a failure. Recent work supplements terminal rewards with finer-grained information from trajectory analysis, such as natural-language reflections on intermediate decisions and errors. However, natural-language diagnoses are difficult to use directly for credit assignment: their error claims may be unreliable, and they do not quantify how much each error should affect learning. We propose Self-Diagnosis-guided Terminal Credit Redistribution (FAULT), which turns diagnosed errors into explicit step-level credit anchored by terminal outcomes. FAULT checks diagnostic evidence and learns relative error costs from task outcomes. During training, the policy and self-diagnoser co-evolve, while error costs are updated online from recent outcomes. On ALFWorld, FAULT recovers learning signal from same-outcome groups, reaching 95% signal coverage versus 41% for GRPO and 72% for GiGPO, while better localizing credit to specific error steps.

**Key innovations.**

- Names the two credit-assignment failures of terminal-reward agentic RL precisely: **same-outcome rollout groups yield zero signal**, and trajectory-wide feedback cannot say *which* decision failed.
- Critiques the obvious fix — natural-language self-reflections — on two grounds: the error claims may be unreliable, and they carry **no magnitude**.
- FAULT converts diagnoses into **step-level credit anchored by terminal outcomes**, checking diagnostic evidence and learning *relative error costs* from outcomes, updated online.
- The headline number is a coverage metric, not an accuracy metric: **95% signal coverage on ALFWorld vs. 41% for GRPO and 72% for GiGPO** — i.e. FAULT mostly rescues the groups that GRPO throws away entirely.
- Policy and self-diagnoser **co-evolve** during training rather than the diagnoser being frozen.

---

### 12. SHARPO: Segment-Level Credit Assignment for Agentic Reinforcement Learning

- **arXiv:** [2610.00838](https://arxiv.org/abs/2610.00838) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`
- **Authors:** Xinchen Du; Zhengze Zhou; Wenhui Zhu; Han Yu; Sen Na; Rohit Jain; Alborz Geramifard
- **Institution / company:** Georgia Institute of Technology; LinkedIn Corporation
- **Affiliation evidence:** verified from author block (first author notes work done during an internship at LinkedIn)
- **Author comment:** 13 pages, 3 tables, 2 figures

**Abstract.** Agentic reinforcement learning (RL) trains a large language model (LLM) to act over long, multi-step interactions. However, a single localized error can cause task failure, while trajectory-level rewards provide limited guidance for assigning credit to individual decisions. To address this limitation, we introduce Segment-level Hindsight Advantage Reweighting for Policy Optimization (SHARPO), a credit-assignment mechanism that refines Group Relative Policy Optimization (GRPO) at the level of environment-facing segments. Inspired by the existing on-policy self-distillation (OPSD) method, SHARPO computes teacher-student log-probability gaps within each segment and uses the resulting signal to compute a bounded multiplier on the GRPO advantage. This multiplier is shared by all tokens within the segment, allowing credit to vary across different segments. With Qwen2.5-7B-Instruct, SHARPO outperforms existing baselines on the ALFWorld and WebShop benchmarks, including GRPO, SDAR, RLSD, and StepOPSD.

**Key innovations.**

- Chooses the **segment** — the environment-facing unit of interaction — as the granularity of credit assignment, on the observation that one localized error kills the whole trajectory.
- Mechanistically reuses on-policy self-distillation: teacher–student log-probability gaps *within each segment* produce a **bounded multiplier on the GRPO advantage**.
- The multiplier is shared across all tokens in a segment, so credit varies *across* segments but stays coherent *within* one — avoiding per-token credit noise.
- Outperforms GRPO, SDAR, RLSD and StepOPSD on ALFWorld and WebShop with Qwen2.5-7B-Instruct.

---

### 13. PG-SFT: Balancing Capability Acquisition and Retention in Offline Agent Fine-Tuning

- **arXiv:** [2610.00949](https://arxiv.org/abs/2610.00949) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`
- **Authors:** Ronghua Li; Zi Liang; Zhishan Li; Shinan Liu
- **Institution / company:** ⚠️ **not stated.** The HTML rendition contains no author block at all, and a PDF text extraction surfaced no institution string. **Not inferred from author names.**
- **Affiliation evidence:** abs page authors only — no author block present in the HTML rendition
- **Author comment:** Preprint

**Abstract.** Supervised fine-tuning (SFT) on offline agent trajectories is the standard approach for training specialized tool-using agents, but forcing models to imitate reasoning and actions token by token may harm other capabilities (e.g., general reasoning, tool calling, code generation) of the base model. In this work, we focus on studying how to better balance the trade-off between acquiring new capabilities and preserving existing ones during agent trace SFT. By comparing several baselines in our setup, standard SFT improves the target benchmark while lowering several non-target benchmark scores; meanwhile, simply constraining distributional drift using KL penalty or limiting the update magnitude did not avoid this regression trend. Motivated by recent token-wise adaptive learning objectives, this work proposes Privilege-Guided SFT (PG-SFT) to leverage turn-level information gain of agent trajectories as an indicator to adjust supervision strength. PG-SFT yields a more favorable observed trade-off on the evaluated benchmarks, substantially reducing distributional drift and broad capability degradation at the cost of slight degradation in target-task performance.

**Key innovations.**

- Frames agent trace SFT as an **acquisition-vs-retention trade-off**: standard SFT lifts the target benchmark while *lowering* general reasoning, tool calling and code generation.
- The negative control matters most: simply constraining distributional drift with a **KL penalty, or limiting update magnitude, does not avoid the regression** — so the usual anchoring tricks are insufficient.
- **PG-SFT** uses **turn-level information gain** of the trajectory as the indicator that sets supervision strength, i.e. *where* and *how strongly* to depart from base behavior.
- States the trade honestly: substantially less distributional drift and capability degradation, at the cost of **slight** target-task degradation.
- Concludes that the trade-off depends not only on *whether* the model is anchored to its base behavior but on **where and how strongly** supervision should depart.

---

### 14. MemFit: Efficient Long-Term Agentic Memory

- **arXiv:** [2610.00872](https://arxiv.org/abs/2610.00872) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`
- **Authors:** Mitchell Piehl; Muchao Ye
- **Institution / company:** ⚠️ **not stated.** arXiv serves **no HTML rendition** for this submission (`HTML is not available for the source`), so no author block could be read. **Not inferred.**
- **Affiliation evidence:** abs page authors only

**Abstract.** Long-term memory systems for large language models (LLMs) have gained popularity for extending reasoning capabilities across applications. Current memory systems rely on LLM agents to organize and consolidate memory, resulting in costly, inefficient write operations. To address this limitation, we propose MemFit, a long-term memory system for conversational agents that reduces the cost and latency of memory operations. Unlike existing systems that rely on expensive LLM calls for memory construction or discard surface-level details through compression, MemFit stores each turn verbatim in an append-only store with near-instantaneous, LLM-free insertion, indexing turns with segment summaries rather than replacing them. Additionally, MemFit uses an LLM-free, multi-path retrieval strategy that combines lexical and semantic signals with cross-encoder reranking over caption-augmented episodes in both textual and multimodal settings. Empirical results on three widely used benchmarks, LoCoMo, MemGallery, and LongMemEval-S, show that MemFit achieves state-of-the-art performance while reducing memory construction time and cost several-fold.

**Key innovations.**

- Targets the **write path**, which most memory-system papers ignore: current systems use LLM agents to organize and consolidate memory, making writes costly and slow.
- **Non-destructive by construction** — every turn is stored *verbatim* in an append-only store with near-instantaneous LLM-free insertion; segment summaries *index* turns rather than replacing them, so surface detail is not discarded by compression.
- Retrieval is LLM-free too: multi-path combination of lexical and semantic signals plus cross-encoder reranking over caption-augmented episodes, covering textual and multimodal settings.
- State-of-the-art on LoCoMo, MemGallery and LongMemEval-S while cutting memory construction time and cost several-fold.
- Sits in the same lineage as [[mem-non-destructive-memory]]-style designs (cf. the 10-03 sibling's `Mem++`, which makes the analogous non-destructive argument for organizational documents).

---

### 15. Causal Memory Policy: Making Memory Utility Identifiable by Intervening on Retrieval

- **arXiv:** [2610.02070](https://arxiv.org/abs/2610.02070) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`
- **Authors:** Arman Behnam; Binghui Wang
- **Institution / company:** Department of Computer Science, Illinois Institute of Technology (Chicago, IL)
- **Affiliation evidence:** verified from author block

**Abstract.** Memory-augmented large language models must decide which memories to retain, and recent systems do so by estimating each memory's effect on task performance. However, these estimates rely entirely on retrieved memories. When a memory is never retrieved, store-level interventions produce identical outcomes, leaving its utility unidentified. This is a retrieval-level positivity violation, invisible to diagnostics that examine only memory operations. We introduce Causal Memory Policy (CMP), a causal framework that restores identification by intervening on retrieval itself, reserving a fixed number of context slots for memories sampled with known propensities. CMP estimates memory utility by self-normalized inverse propensity weighting under a balanced assignment design. We prove the causal factorization of memory utility through retrieval, the unbiasedness and exact variance of the estimator, and the optimal decision rule under irreversible operations. Empirically, identification fails for 54% of required memories on LongMemEval and 67% on LoCoMo, and the failure persists in a deployed memory system. CMP improves discrimination between required and non-required memories from 0.54 to 0.66 AUC.

**Key innovations.**

- Finds a **positivity violation at the retrieval level**: if a memory is never retrieved, interventions on the store produce identical outcomes, so its utility is *unidentified* — and this is invisible to diagnostics that only inspect memory operations.
- The fix is to intervene **on retrieval itself**, reserving a fixed number of context slots for memories sampled with known propensities, then estimating utility by self-normalized inverse propensity weighting under balanced assignment.
- Proves the causal factorization of memory utility through retrieval, the estimator's unbiasedness and exact variance, and the optimal decision rule under irreversible operations.
- The measured scale of the problem is the real finding: identification **fails for 54% of required memories on LongMemEval and 67% on LoCoMo**, and it fails in a *deployed* system too; discrimination improves 0.54 → 0.66 AUC.
- Adds a sharp negative result: identified per-query utility reaches 0.78 AUC on the query it was estimated for, yet **no aggregation available to a retention policy predicts a memory's value on unseen queries**.

---

### 16. LatentHarness: Learning Latent Actions for Memory and Reasoning via Counterfactual Policy Distillation

- **arXiv:** [2609.39740](https://arxiv.org/abs/2609.39740) · submitted 2026-09-30 · primary category `cs.CL` · all categories: `cs.CL`
- **Authors:** Xiaoqiang Wang; Suyuchen Wang; Bang Liu
- **Institution / company:** ⚠️ **not stated.** The HTML author block renders two bare `Affiliation:` labels with empty institution text; the only contact rendered is `bang.liu@umontreal.ca`. **Not inferred from the email domain.**
- **Affiliation evidence:** abs page authors only — both `Affiliation:` labels render with empty institution text
- **Author comment:** Work in progress

**Abstract.** Long-context reasoning faces two complementary bottlenecks: retaining evidence across long inputs and sustaining computation across many reasoning steps. Existing approaches largely address them separately, with external memory extending access to distant evidence and latent reasoning compressing multi-step computation. We introduce LatentHarness, which unifies memory access and latent reasoning as sequential latent action selection. At each internal step, the model chooses THINK for further computation, RECALL from a fast-weight memory of input evidence and intermediate reasoning states, or EXIT to emit the next token. We train this policy with counterfactual policy distillation, which branches every action for one step and scores its effect on the emitted token. These gains teach the policy when memory is more useful than further reasoning, while gradients through counterfactual recall teach which intermediate states should be retained in memory for future use. Across six general and long-context reasoning benchmarks, LatentHarness at 1.4B improves on the strongest baselines by 2.8% and 10.0% relative, respectively, and runs 5.9x faster than the strongest long-context baseline.

**Key innovations.**

- Argues memory access and latent reasoning are **two halves of one bottleneck**, and unifies them as a single choice among three latent actions: **THINK** (more computation), **RECALL** (fetch from a fast-weight memory of input evidence and intermediate reasoning states), **EXIT** (emit the next token).
- Training signal is **counterfactual policy distillation**: branch every action for one step and score its effect on the emitted token — one method simultaneously teaches *when memory beats more thinking* (from the action gains) and *what is worth remembering* (from gradients through counterfactual recall).
- At 1.4B: **+2.8%** and **+10.0%** relative over the strongest baselines on general and long-context reasoning benchmarks respectively, and **5.9× faster** than the strongest long-context baseline.
- Notable as a 1.4B result — the memory/compute routing policy is cheap enough to train at small scale.

---

### 17. Not All Experience Belongs in the Weights: Component Routing for Self-Improving GUI Agents

- **arXiv:** [2610.01787](https://arxiv.org/abs/2610.01787) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`, `cs.GR`
- **Authors:** Beining Wu; Zihao Ding; Jun Huang
- **Institution / company:** Department of Electrical Engineering and Computer Science, South Dakota State University
- **Affiliation evidence:** verified from author block

**Abstract.** Self-improving GUI agents keep the trajectories they produce and return them to the agent, by fine-tuning or by retrieval into the prompt, and studies that compare the two destinations disagree. We attribute this to the unit of experience: a trajectory bundles items with different properties, so a conclusion about the bundle depends on its mix. To address this, (i) we introduce component routing, which splits the experience into locators, procedures, state facts and lessons and sends each component to the context or to the weights, compared on the same items across three backbone families, two environments and three seeds. One pool has two destinations: locators and lessons win in the weights, procedures and state facts in the context. (ii) We fit a rule in two properties measured before any training, recurrence and state-conditionality; it recovers the destination of a held-out backbone family in 24 of 24 cells, two interventions move a component toward the boundary, and routing by the rule beats every whole-trajectory baseline and, by +3.5 points on average, the better single destination of each backbone. (iii) We identify how training and producer-consumer differences change the value of the two destinations.

**Key innovations.**

- Diagnoses why the fine-tune-vs-retrieval literature disagrees: **the unit of experience is wrong**. A trajectory bundles items with different properties, so any conclusion about the bundle depends on its mix.
- **Component routing** splits experience into four types — **locators, procedures, state facts, lessons** — and sends each to the *context* or the *weights*, holding the items fixed across three backbone families, two environments and three seeds.
- The empirical answer is a clean split: **locators and lessons win in the weights; procedures and state facts win in the context.** One pool, two destinations.
- Then it fits a *predictive rule* from two pre-training-measurable properties — **recurrence** and **state-conditionality** — that recovers a held-out backbone family's destination in **24 of 24 cells**, with two interventions that move a component toward the boundary (a genuine causal check, not just a correlational fit).
- Routing by the rule beats every whole-trajectory baseline and beats the better single destination of each backbone by **+3.5 points on average**.

---

### 18. Thinking Outside the Box: Can Language Models Rely on External Guidance Selectively?

- **arXiv:** [2609.39578](https://arxiv.org/abs/2609.39578) · submitted 2026-09-30 · primary category `cs.CL` · all categories: `cs.CL`
- **Authors:** Minghan Wang; Boyuan Wang; Jinhang Zuo; Yuxin Tao; Fang Kong
- **Institution / company:** ⚠️ **not stated.** The HTML author block renders no affiliation text for any author. **Not inferred.**
- **Affiliation evidence:** authors listed with no affiliation markup

**Abstract.** Agent harnesses often improve language models with human-designed workflows, but as models grow more capable, unreliable guidance can increasingly constrain their execution. We call the ability to benefit from useful guidance while overriding unreliable guidance *thinking outside the box*. We introduce Box²-Bench, which holds the model and task fixed while varying workflow reliability to isolate how models regulate their reliance on guidance. On Box²-Bench, frontier models often benefit from reliable guidance but remain vulnerable when it is misleading or becomes unreliable. To test whether this capability can be learned, we train two open-weight models using bad workflows, reserving good workflows for evaluation. We explore two complementary training strategies: counterfactual supervised fine-tuning improves robustness, while outcome-based reinforcement learning can shift the balance toward greater use of helpful workflows. We further find that this behavior extends beyond workflows to other forms of external information, improving peer correction and robustness to corrupted memory.

**Key innovations.**

- Identifies a harness-era inversion: as models get more capable, **unreliable human-designed workflows increasingly *constrain* them** — the standard justification for scaffolding inverts as models improve.
- Names the missing capability: benefiting from useful guidance *while overriding unreliable guidance*, and builds **Box²-Bench** to isolate it by holding model and task fixed while **varying only workflow reliability**.
- Finding: frontier models benefit from reliable guidance but **remain vulnerable when guidance is misleading or degrades** — they do not regulate reliance.
- Tests learnability with an elegant train/test split: train two open-weight models on **bad** workflows, evaluate on **good** ones. Counterfactual SFT improves robustness; outcome-based RL shifts the balance toward *more* use of helpful workflows.
- Generalizes beyond harnesses: the same behavior improves **peer correction** and robustness to **corrupted memory**.
- Frames selective reliance on fallible external information as a dimension of agent reliability that **task performance alone does not capture**.

---

## Inference, Serving, Compression & Scaling Laws (10)

### 19. DRelay: Global Draft Context for Prefix-Aware Parallel Speculative Decoding Repair

- **arXiv:** [2610.01439](https://arxiv.org/abs/2610.01439) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`
- **Authors:** Zhuoyu Wang; Junnan Huang; Xinyu Chen
- **Institution / company:** The Hong Kong University of Science and Technology (Guangzhou)
- **Affiliation evidence:** verified from author block

**Abstract.** Parallel drafting reduces the drafting overhead of speculative decoding for large language models (LLMs), but its gains remain limited by the accepted prefix length. Even when the correct token is present in the candidate pool, a single early selection error prevents subsequent predictions from being used. We propose DRelay, which uses global information from the entire draft block to perform prefix-aware selective repair of candidate selections before target-model verification. DRelay bases its decisions on candidate correlations and the selected path: a global reader extracts predictive information across positions for each candidate. While a causal selector combines candidate-level information extracted by the global read with the tokens selected at preceding positions to determine whether the native choice at the current position is consistent with the global evidence and the selected prefix. It then decides whether to retain or replace the token, thereby repairing early errors and extending the accepted prefix. We further jointly train the draft backbone and the selector, combining candidate-support learning with a repair objective, while weighting the repair loss according to each block position's potential contribution to the consecutive accepted prefix. Across eight diverse benchmarks on an H800 GPU, DRelay consistently improves both average acceptance length and end-to-end decoding performance over DFlash, Domino, and DSpark. Under SGLang serving, DRelay improves average end-to-end speedup over DFlash, Domino, and DSpark by 14.7%-16.8%, 8.7%-9.3%, and 8.1%-9.3%, respectively.

**Key innovations.**

- Names the actual bottleneck of parallel drafting: gains are capped by **accepted prefix length**, and *one early selection error wastes everything after it* — even when the correct token is already in the candidate pool.
- **DRelay repairs before verification** rather than after: a global reader extracts cross-position predictive information per candidate, and a causal selector checks whether the native choice is consistent with the global evidence *and* the already-selected prefix, then retains or replaces.
- Joint training of draft backbone and selector, with the repair loss **weighted by each block position's potential contribution to the consecutive accepted prefix** — the loss follows the bottleneck.
- Measured under real serving, not just kernels: eight benchmarks on H800, and under **SGLang** the end-to-end speedup over DFlash / Domino / DSpark improves by **14.7–16.8%**, **8.7–9.3%** and **8.1–9.3%** respectively.

---

### 20. EchoPress: Query-Agnostic KV Cache Pruning via Virtual Context Reconstruction

- **arXiv:** [2610.00412](https://arxiv.org/abs/2610.00412) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`
- **Authors:** Jiawei Lin; Saibo Geng; Thomas Bourgeat
- **Institution / company:** EPFL
- **Affiliation evidence:** verified from author block

**Abstract.** KV cache pruning reduces long-context inference memory usage by evicting less important key–value pairs. KVzip estimates importance through context reconstruction: prompting a model to repeat the context chunk by chunk. This achieves strong compression quality at the cost of additional forward passes. Learned approximations reduce this cost but require model-specific training. We analyze how KVzip identifies important cached information and show how to approximate its reconstruction scores using information already computed during prefill. These findings motivate EchoPress, a training-free method that approximates reconstruction attention using queries and keys from standard prefill. For each request, it reconstructs only the first chunk to calibrate importance scores for the remaining context. Experiments on LongBench and RULER with Qwen3-8B and Llama-3.1-8B-Instruct show that EchoPress matches KVzip in task accuracy across eviction ratios from 50% to 90%, while reducing compression overhead by a factor of 1.7-19.6 and total prefill time by a factor of up to 2.9.

**Key innovations.**

- Sits between two unsatisfying options: **KVzip** gets compression quality from context reconstruction but pays extra forward passes; **learned approximations** cut that cost but need model-specific training.
- The contribution is an *analysis* first — how KVzip identifies important cached information — which shows reconstruction scores can be **approximated from information already computed during prefill**.
- **EchoPress** is therefore training-free *and* query-agnostic: it reconstructs only the **first chunk** per request to calibrate importance scores for the rest.
- Matches KVzip's task accuracy at eviction ratios from **50% to 90%** on LongBench and RULER (Qwen3-8B, Llama-3.1-8B-Instruct), while cutting compression overhead **1.7–19.6×** and total prefill time up to **2.9×**.

---

### 21. TopK-Guided: Adaptive, Budget-Aware Activation Sparsity for Efficient LLM Inference

- **arXiv:** [2610.01763](https://arxiv.org/abs/2610.01763) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`
- **Authors:** Mukund Agarwalla; Chih-Jen Lin
- **Institution / company:** MBZUAI; National Taiwan University
- **Affiliation evidence:** verified from author block

**Abstract.** Activation sparsity speeds up large language model (LLM) inference by setting unimportant activations to zero so that the corresponding computations can be skipped. Existing training-free methods, however, make different trade-offs: threshold-based methods such as TEAL adapt the sparsity level to each token but do not tightly control the realised sparsity, while TopK-based methods such as WINA enforce a fixed sparsity level but use the same sparsity budget for every token. Both also apply the same budget across transformer blocks, despite large differences in block sensitivity. We introduce TopK-Guided, a training-free method that addresses both limitations by combining bounded token-level sparsity adaptation with sensitivity-aware block-level budget allocation. Across Llama-2 and Llama-3 models, TopK-Guided consistently improves perplexity and downstream accuracy over TEAL and WINA while preserving essentially the same sparsity-dependent projection compute as WINA, with the largest gains at high sparsity. Ablations show that both components provide complementary improvements.

**Key innovations.**

- Sharp two-sided critique of existing training-free activation sparsity: **threshold methods (TEAL)** adapt per token but do not control realised sparsity; **TopK methods (WINA)** control it but use one budget for every token.
- Adds a third, less-noticed flaw: both apply the **same budget across transformer blocks** despite large differences in block sensitivity.
- **TopK-Guided** combines *bounded* token-level sparsity adaptation with *sensitivity-aware* block-level budget allocation — getting adaptivity without losing control.
- Consistent perplexity and downstream-accuracy gains over TEAL and WINA on Llama-2 and Llama-3 at essentially the same sparsity-dependent projection compute as WINA, largest gains at high sparsity; ablations show both components contribute complementarily.

---

### 22. RapidMoE: Exploiting Cross-Asymmetry via Adaptive Residual Offloading for Large-Scale MoE Inference

- **arXiv:** [2610.01265](https://arxiv.org/abs/2610.01265) · submitted 2026-10-01 · primary category `cs.DC` · all categories: `cs.DC`
- **Authors:** Wenxun Wang; Likai Ma; Zongle Huang; Chen Tang; Yongpan Liu
- **Institution / company:** Tsinghua University, Beijing (incl. BNRist)
- **Affiliation evidence:** verified from author block
- **Author comment:** **Accepted by EuroSys 2027.** 17 pages

**Abstract.** The widespread adoption of Mixture-of-Experts (MoE) has created a growing need for deployment on heterogeneous platforms. However, it exposes a fundamental mismatch between the algorithmic demands of large-scale MoE and the disparate characteristics of CPU-GPU hybrid inference systems fail to resolve as they either encounter PCIe bandwidth bottlenecks when loading experts to GPUs, or rely heavily on CPU computation. Consequently, this leads to low resource utilization and inevitable violations of fixed latency budgets as parameters scale. In this paper, we identify and exploit Cross-Asymmetry — a structural alignment between the algorithmic workload skew of MoE routing and the physical disparity of heterogeneous hardware. To this end, we introduce RapidMoE, a residual offloading system for efficient large-scale MoE inference. We propose how RapidMoE leverages a residual-split framework to enable offloading paradigm shift from expert-level to bit-level, unfolding across three key dimensions: data representation, routing strategy, partitioning computation into dual paths aligned with hardware capabilities; and execution parallelism, scheduling a balanced storage-compute workload across devices. We further employ a novel Unified Multi-Level Importance Arbitration to adaptively adjust the critical expert set at runtime, ensuring the accuracy-latency Pareto frontier. Experimental results show that RapidMoE achieves up to 3.5x speedup in decoding and 2.1x speedup in prefill compared to state-of-the-art (SOTA) offloading systems.

**Key innovations.**

- Diagnoses the deployment failure mode honestly: CPU–GPU hybrid MoE inference either hits **PCIe bandwidth bottlenecks** loading experts to GPU, or leans on CPU compute — so utilization is low and **fixed latency budgets break as parameters scale**.
- The unifying idea is **Cross-Asymmetry**: a structural alignment between MoE routing's *workload skew* and heterogeneous hardware's *physical disparity*. Neither side is treated as the problem to fix.
- The mechanism is an offloading **paradigm shift from expert-level to bit-level** via residual splitting, across data representation, routing (dual compute paths aligned to hardware capability) and execution parallelism.
- **Unified Multi-Level Importance Arbitration** adjusts the critical expert set at runtime, protecting the accuracy–latency Pareto frontier rather than trading one for the other.
- Up to **3.5× decode** and **2.1× prefill** speedup over SOTA offloading systems; EuroSys 2027 acceptance.

---

### 23. The Devil Is in the Reconstruction Loss Scale: Rethinking Optimization in LLM Quantization

- **arXiv:** [2610.00983](https://arxiv.org/abs/2610.00983) · submitted 2026-10-01 · primary category `cs.CL` · all categories: `cs.CL`, `cs.AI`
- **Authors:** Chao Li; Shigeng Wang; Anbang Yao
- **Institution / company:** Intel Labs China
- **Affiliation evidence:** verified from author block

**Abstract.** Post-training quantization (PTQ) methods typically use sequential quantization that partitions a pre-trained LLM into a series of units (e.g., transformer blocks), with one unit quantized at each stage. State-of-the-art PTQ methods are predominantly learning-based, optimizing auxiliary quantization parameters (e.g., scaling factors, rotation matrices, clipping thresholds, and adapters) via gradient descent to minimize a reconstruction loss. A common practice is to use mean squared error (MSE) as the reconstruction loss function, yet its induced optimization behavior remains largely unexplored. In this work, we take a holistic view of sequential quantization and systematically investigate how optimization evolves from the first quantization stage to the last, aiming for a deep understanding of optimization in learning-based PTQ schemes. Through extensive empirical studies spanning representative learning-based PTQ methods, LLM families, model scales, architectures, quantization settings and various tasks, we consistently uncover Optimization Imbalance: reconstruction loss magnitudes vary dramatically across stages, accompanied by highly uneven gradient magnitudes and parameter updates under MSE. We term the cross-stage range of loss magnitudes the reconstruction loss scale, and reveal that MSE translates the unexpectedly large reconstruction loss scale into highly uneven gradient magnitudes, which in turn lead to uneven optimization strength across quantization stages. This finding suggests a general principle for improving learning-based PTQ: optimization strength across stages should be decoupled from the reconstruction loss scale. Theoretically, we show that root mean squared error (RMSE) variants defined at the sample, channel, token, and element levels naturally realize this principle through implicit gradient normalization, outperforming MSE significantly as a drop-in replacement.

**Key innovations.**

- Studies the part of PTQ nobody instruments: **how optimization evolves from the first quantization stage to the last**, under the near-universal default of MSE as the reconstruction loss.
- Finds **Optimization Imbalance** consistently across methods, model families, scales, architectures, quantization settings and tasks: reconstruction-loss magnitudes vary dramatically across stages, and MSE converts that into highly uneven gradient magnitudes and parameter updates.
- Coins the mechanism — the cross-stage range of loss magnitudes is the **reconstruction loss scale** — and turns it into a design principle: *optimization strength across stages should be decoupled from the reconstruction loss scale*.
- The fix is nearly free: **RMSE variants at the sample, channel, token and element levels** realize the decoupling through implicit gradient normalization, outperforming MSE as a **drop-in replacement**.
- Practical upshot for anyone reproducing a PTQ baseline: switching the loss function may matter more than the method.

---

### 24. How Divergence Becomes Decision Flips in Compressed Language Models

- **arXiv:** [2610.00694](https://arxiv.org/abs/2610.00694) · submitted 2026-09-30 · primary category `cs.CL` · all categories: `cs.CL`, `cs.AI`, `cs.LG`, `stat.ML`
- **Authors:** Beatriz Almeida Felicio
- **Institution / company:** Instituto de Informática (INF), Universidade Federal de Goiás (UFG)
- **Affiliation evidence:** verified from author block
- **Author comment:** Preprint

**Abstract.** Compression reports summarize how far a compressed language model moved from the dense one, usually by a KL divergence; a deployment that relies on the dense model's outputs needs to know how many of its decisions changed. We show that total variation, not KL, answers this directly. Across 802 compressed and perturbed copies of 19 open models on five corpora and nine mechanically unrelated perturbation families, the rate at which the arg-max token changes (the flip rate) tracks total variation at a ratio with median 1.05, with no fitted constant. KL converts into flips only through its square root and a factor that varies fourfold across models and corpora, because KL averages over tokens before the root is taken; first-order statistics averaged per token, such as Hellinger distance, avoid this, but reports rarely give them. As a result, of two compressors reported on different models and corpora whose flip rates differ by at least 10%, KL assigns the smaller divergence to the one that changes more decisions in 11% of cases, total variation in 1%. Two pre-registered tests mark the limits: on a held-out code corpus the ratio held for all eight models while three predictions about KL each failed for half of them or more, and on three new models with real kernels it stayed in its band for 37 of 38 checkpoints but fell below one on code for two models. In vLLM speculative decoding, total variation measured under teacher forcing predicts greedy draft acceptance with a mean relative error of 1.1%-2.4%, without the task-specific calibration that KL needs.

**Key innovations.**

- Argues the field is reporting the **wrong divergence for the question deployments ask**: KL answers "how far did it move", but a deployment needs "how many *decisions* changed".
- Massive empirical basis: **802 compressed and perturbed copies of 19 open models**, five corpora, nine mechanically unrelated perturbation families. The flip rate tracks **total variation** with median ratio **1.05 and no fitted constant**; KL only converts into flips through its *square root* times a factor that varies **fourfold** across models and corpora.
- Concrete consequence: of two compressors on different models/corpora whose flip rates differ by ≥10%, **KL ranks the more-changed model as less divergent in 11% of cases; total variation in 1%**.
- Methodological quality worth copying: **two pre-registered tests mark the limits** — the TV ratio held for all eight models on a held-out code corpus (while three KL predictions each failed for half or more), and stayed in band for **37 of 38 checkpoints** on new models with real kernels.
- Closes the loop with a live use: under vLLM speculative decoding, **teacher-forced TV predicts greedy draft acceptance with 1.1–2.4% mean relative error, with none of the task-specific calibration KL requires**.

---

### 25. Sequential Functional Structured Tucker Compression for Large Language Model Attentions

- **arXiv:** [2610.00717](https://arxiv.org/abs/2610.00717) · submitted 2026-09-30 · primary category `cs.CL` · all categories: `cs.CL`, `cs.AI`, `stat.ML`
- **Authors:** Jiangfeng Chen; Xinyu Wang; Tianshuo Yan; Hanwei Wu; Xiao-Wen Chang; Yang Zhang; Lei Ding
- **Institution / company:** University of Manitoba; McGill University; Simpleway; The University of Hong Kong; McMaster University
- **Affiliation evidence:** verified from author block

**Abstract.** Post-training compression of LLM attention is often formulated as independent matrix approximation, ignoring both the shared structure among attention projections and the representation shift introduced by earlier compression. We propose FTC, a sequential structured compression framework that adapts the approximation to the current compressed model while jointly exploiting the native Q/K/V head structure under a fixed storage budget. The output projection is handled separately to account for the changed post-attention representation. FTC requires neither fine-tuning nor gradient-based recovery. Across seven decoder-only LLMs from 6B to 32B parameters, FTC achieves the lowest WikiText-2 perplexity among the compared methods at every tested keep ratio on five modern GQA models, with the largest gains under aggressive compression. The improvements transfer to downstream tasks and remain substantial at the 32B scale.

**Key innovations.**

- Critiques the standard framing of attention compression as **independent matrix approximation**, which ignores two things: structure *shared among* the attention projections, and the **representation shift introduced by earlier compression** in a sequential pipeline.
- **FTC** adapts each approximation to the *current already-compressed* model while jointly exploiting native Q/K/V head structure under a fixed storage budget; the output projection is handled separately to account for the changed post-attention representation.
- Requires **neither fine-tuning nor gradient-based recovery** — a meaningful constraint, since gradient-based recovery is the usual cost of structured compression.
- Lowest WikiText-2 perplexity among compared methods at **every tested keep ratio** on five modern GQA models, largest gains under aggressive compression; gains transfer downstream and remain substantial at 32B.

---

### 26. LampAttention: Look-Ahead Mixed-Precision FlashAttention for Dedicated Accelerators

- **arXiv:** [2609.39361](https://arxiv.org/abs/2609.39361) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`, `math.NA`
- **Authors:** Stanislav Budzinskiy; Marian Gloser; Tolunay Yilmaz; Ying Hong Tham; Yuanyi Lin; Wenyi Fang; Fan Wu; Philipp Petersen
- **Institution / company:** Faculty of Mathematics, University of Vienna (Austria); Huawei Heisenberg Research Center, Munich; Huawei Technologies Co. Ltd
- **Affiliation evidence:** verified from author block

**Abstract.** While most attention logits can be computed in low precision without degrading numerical stability, current attention kernels fail to exploit this phenomenon. We introduce a novel hardware-algorithm co-design in the form of mixed-precision FlashAttention. Our method accumulates key-query products and evaluates their exponentials in 8-bit formats, then adaptively identifies sensitive sub-blocks and recomputes them in 16-bit formats. We propose the specifications for a dedicated accelerator capable of executing this pipeline efficiently. Simulated experiments with Qwen3 and Gemma 3 show that rerouting a selective minority of sub-blocks to high precision is sufficient to recover the baseline model performance.

**Key innovations.**

- Exploits an observation that **current attention kernels leave on the table**: most attention logits can be computed in low precision without degrading numerical stability — the kernels simply do not exploit it.
- **Mixed-precision FlashAttention**: key–query products and their exponentials accumulate in 8-bit, then sensitive sub-blocks are adaptively identified and **recomputed in 16-bit**.
- Genuinely a **hardware–algorithm co-design**: the paper specifies the dedicated accelerator that can execute the pipeline efficiently, rather than only simulating an algorithm on a GPU.
- The empirical claim is the useful one: rerouting a **selective minority** of sub-blocks to high precision suffices to fully recover baseline model performance (simulated on Qwen3 and Gemma 3).

---

### 27. Scaling Laws for Looped Mixture of Experts

- **arXiv:** [2609.40316](https://arxiv.org/abs/2609.40316) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`, `cs.CL`
- **Authors:** Yanbei Chen; Anirudh Goyal; Raghuraman Krishnamoorthi
- **Institution / company:** Meta AI
- **Affiliation evidence:** verified from author block
- **Author comment:** 19 pages

**Abstract.** Looped transformers and Mixture-of-Experts (MoE) offer complementary routes to efficient scaling: recurrence increases computational depth at fixed parameters, while MoE sparsity expands total capacity at fixed active compute. Yet existing scaling laws model recurrence or sparsity in isolation. In this work, we introduce Loop Scaling Laws, the first scaling law to jointly model recurrence and sparsity alongside model size and data. At its core is a bounded, sparsity-conditional recurrence mapping that characterizes the effective-parameter gain from looping and how sparsity raises this gain. The laws predict the held-out loss of looped models more accurately than prior alternatives, and recover the standard dense and MoE scaling laws as special cases. Beyond prediction, the fitted laws provide a principled foundation for designing looped MoE models under compute and memory constraints. Downstream evaluations further demonstrate the complementary benefits of the two axes: sparsity delivers ~3x active-parameter efficiency, recurrence yields ~2x total-parameter efficiency on reasoning, and joint scaling further advances the performance frontier. As a practical extension, we show these gains hold at trillion-token scale: at matched training compute, a looped MoE with law-derived recurrence matches a ~2x larger non-looped MoE on the reasoning benchmarks, while enabling test-time scaling through recurrence.

**Key innovations.**

- Points out that looped transformers and MoE are **complementary** axes — recurrence buys depth at fixed parameters, sparsity buys capacity at fixed active compute — yet every existing scaling law models them **in isolation**.
- **Loop Scaling Laws** is the first to model recurrence *and* sparsity jointly with size and data, built on a **bounded, sparsity-conditional recurrence mapping** describing the effective-parameter gain from looping and how sparsity raises that gain.
- Sanity property that raises confidence: it **recovers the standard dense and MoE scaling laws as special cases**.
- The two axes are quantified separately and they are not redundant: sparsity gives **~3× active-parameter efficiency**, recurrence **~2× total-parameter efficiency on reasoning**, and joint scaling advances the frontier further.
- Validated at real scale: at trillion-token scale and matched training compute, a looped MoE with law-derived recurrence **matches a ~2× larger non-looped MoE** on reasoning benchmarks while enabling test-time scaling through recurrence.

---

### 28. Denoising Surface: Modeling and Predicting Inference Cost for Diffusion LLM Serving

- **arXiv:** [2610.00499](https://arxiv.org/abs/2610.00499) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`
- **Authors:** Haoyu Zheng; Fangcheng Fu; Binhang Yuan; Yongqiang Zhang; Liang Deng; Hao Wang; Yuanyuan Zhu; Xiao Yan; Jiawei Jiang
- **Institution / company:** Wuhan University; Central China Normal University; Shanghai Jiao Tong University; The Hong Kong University of Science and Technology; Damen Database Co., Ltd.
- **Affiliation evidence:** verified from author block

**Abstract.** As diffusion large language models (dLLMs) become more capable, they are moving from research settings to real-world serving, where request management (such as scheduling and resource allocation) relies on accurate estimation of per-request inference cost. However, common cost proxies fall short for dLLMs: output length ignores that one forward pass can unmask multiple tokens, and denoising-step count ignores the heterogeneous per-step costs. We observe that the block-autoregressive generation mechanism induces a two-dimensional execution structure over output blocks and within-block denoising steps, whereas these proxies collapse it into a scalar, discarding information essential for characterizing the cost. Motivated by this insight, we propose the Denoising Workload Surface (DWS), which preserves this two-dimensional block-step structure as a probability surface to weight the heterogeneous per-step costs. We then design a coarse-to-fine training scheme that enables a lightweight prompt-only predictor to accurately predict the complex DWS. This predictor runs efficiently even on a single CPU core, avoiding GPU contention with the serving model. Since DWS decouples request-dependent execution behavior from deployment-specific cost factors, the predictor transfers across hardware configurations without retraining. In real-world serving experiments, DWS reduces cost-prediction error by up to 2.50x over scalar-based predictors, while the DWS-guided shortest-job-first scheduler reduces end-to-end latency by up to 1.92x for online chatbots.

**Key innovations.**

- Explains why standard cost proxies break for diffusion LLMs: **output length** ignores that one forward pass can unmask multiple tokens, and **denoising-step count** ignores heterogeneous per-step costs — both collapse a 2-D structure into a scalar.
- **DWS** (Denoising Workload Surface) preserves the two-dimensional block × denoising-step structure as a **probability surface** that weights heterogeneous per-step costs.
- Deployment-motivated engineering: a lightweight **prompt-only** predictor runs on a **single CPU core**, explicitly avoiding GPU contention with the serving model.
- The decoupling has a payoff beyond prediction: because DWS separates request-dependent execution behavior from deployment-specific cost factors, the predictor **transfers across hardware without retraining**.
- Measured in real serving: cost-prediction error down **2.50×** vs. scalar proxies, and a DWS-guided shortest-job-first scheduler cuts end-to-end latency **1.92×** for online chatbots.

---

## Multimodal Reasoning, Generative Architectures & VLM Evaluation (7)

### 29. MMVistaReason: Toward Open-Data and Post-Training Recipes for Multimodal Reasoning

- **arXiv:** [2610.01352](https://arxiv.org/abs/2610.01352) · submitted 2026-10-01 · primary category `cs.CV` · all categories: `cs.CV`
- **Authors:** Juekai Lin; Honglin Lin; Yuqian Yuan; Xiaolong Wu; Jie Cao; Liang Liang; Yunqi Cao; Yun Zhu; Wenqiao Zhang; Lijun Wu
- **Institution / company:** ⚠️ **not stated.** The HTML author block renders four bare `Affiliation:` labels with empty institution text; the only contact rendered is `wulijun@pjlab.org.cn`. **Not inferred from the email domain.**
- **Affiliation evidence:** verified that affiliation labels exist but carry no institution text

**Abstract.** Open multimodal reasoning models have benefited from large-scale reasoning supervision, yet reliable post-training remains challenging due to uneven data quality, inefficient supervision construction, imbalanced difficulty, and cross-domain interference. We introduce MMVistaReason (MVR), an open-data post-training recipe with three components: (1) broader capability coverage across complementary Analytical and Real-World reasoning groups, emphasizing structured reasoning versus visual perception and spatial grounding; (2) efficient SFT and RL data construction, standardizing heterogeneous open data through staged cleaning and annotation, combining difficulty-aware cascaded teacher distillation with answer-likelihood-based trajectory selection to construct MVR-SFT-528K, and applying scale-specific frontier filtering for MVR-RL-63K; (3) specialize-then-integrate training, which trains complementary RL experts and consolidates their capabilities through multi-teacher on-policy distillation (MOPD). Our analyses reveal a capacity-dependent interaction between supervision difficulty, trajectory quality, and model capacity: smaller students benefit more from selected supervision, while larger students are robust to trajectory variation and mixed-domain interference. Mixed-domain RL introduces benchmark-level negative transfer, whereas MOPD provides consistent capability integration, with the preferred KL direction varying across model scales. Across 15 multimodal benchmarks, MVR-4B achieves an average score of 72.8, outperforming Qwen3.5-9B (Instruct) and MMFineReason-8B while using about 70% fewer samples than MMFineReason. Scaling to 9B improves the average to 74.4, surpassing Qwen3.5-35B-A3B (Instruct).

**Key innovations.**

- Attacks four named causes of unreliable multimodal post-training at once: uneven data quality, inefficient supervision construction, imbalanced difficulty, and **cross-domain interference**.
- Three-part recipe: complementary **Analytical vs. Real-World** reasoning coverage (structured reasoning over visual perception and spatial grounding); efficient data construction via **difficulty-aware cascaded teacher distillation + answer-likelihood-based trajectory selection** (MVR-SFT-528K) and **scale-specific frontier filtering** (MVR-RL-63K); and **specialize-then-integrate** training where complementary RL experts are consolidated by **multi-teacher on-policy distillation (MOPD)**.
- The analysis is the real contribution: a **capacity-dependent interaction** between supervision difficulty, trajectory quality and model capacity — smaller students benefit more from selected supervision, larger students are robust to trajectory variation and mixed-domain interference.
- Negative result with a mechanism: **mixed-domain RL introduces benchmark-level negative transfer**, while MOPD integrates consistently — and the *preferred KL direction varies across model scales*.
- Efficiency claim: MVR-4B averages **72.8** across 15 benchmarks, beating Qwen3.5-9B-Instruct and MMFineReason-8B with **~70% fewer samples**; at 9B it reaches **74.4**, surpassing Qwen3.5-35B-A3B-Instruct.

---

### 30. Reinforcing Multimodal Reasoning via Token-Level Perception-Grounded Advantage Estimation

- **arXiv:** [2609.39168](https://arxiv.org/abs/2609.39168) · submitted 2026-09-30 · primary category `cs.AI` · all categories: `cs.AI`
- **Authors:** Zhihan Zhang; Lizi Liao
- **Institution / company:** Singapore Management University, Singapore
- **Affiliation evidence:** verified from author block
- **Author comment:** **Accepted by ACM MM 2026**

**Abstract.** Reinforcement Learning with Verifiable Rewards (RLVR) has improved the reasoning capabilities of Multimodal Large Language Models (MLLMs), yet existing frameworks rely on coarse, sequence-level reward signals that lack the fine-grained supervision over the visually-grounded steps within a multimodal reasoning chain. We investigate this gap through the lens of two token-level metrics: visual dependency (i.e. how much a token's prediction relies on the input image features) and predictive entropy. Our empirical analysis reveals two key findings: (1) correct reasoning chains exhibit a markedly sharper entropy reduction as visual grounding intensifies, compared to incorrect ones; (2) pivotal tokens, those whose misprediction triggers reasoning collapse, are statistical outliers in the joint distribution of visual dependency and predictive entropy derived from correct chains. Motivated by these findings, we propose token-level perception-grounded advantage estimation (TPAE), which estimates token-level advantages by measuring each token's statistical consistency with the vision-entropy patterns of correct rollouts. TPAE leverages this granular score to modulate the sequence-level advantage, producing a fine-grained supervision signal that can be integrated into various RLVR frameworks. Extensive experiments on seven benchmarks show that TPAE consistently outperforms leading strong baselines, yielding more stable and efficient optimization for multimodal reasoning.

**Key innovations.**

- Builds two token-level metrics from first principles — **visual dependency** (how much a token's prediction relies on image features) and **predictive entropy** — and uses them to diagnose where multimodal RLVR is blind: sequence-level rewards give no supervision over visually-grounded steps.
- Two empirical findings that motivate the method: correct chains show a **markedly sharper entropy reduction as visual grounding intensifies**, and **pivotal tokens** (whose misprediction collapses reasoning) are **statistical outliers** in the joint visual-dependency × entropy distribution of correct chains.
- **TPAE** scores each token by consistency with the vision–entropy pattern of correct rollouts and uses that to *modulate* the sequence-level advantage — so it is a plug-in for many RLVR frameworks rather than a new RL algorithm.
- Consistent gains over strong baselines on seven benchmarks with more stable and efficient optimization; ACM MM 2026.

---

### 31. Rethinking Multi-Image Re-Representation in Multi-Image Understanding

- **arXiv:** [2609.39363](https://arxiv.org/abs/2609.39363) · submitted 2026-09-30 · primary category `cs.CV` · all categories: `cs.CV`, `cs.AI`
- **Authors:** Gengyuan Zhang; Xiao Han; Xinyu Xie; Tong Liu; Volker Tresp
- **Institution / company:** LMU Munich; MCML
- **Affiliation evidence:** verified from author block
- **Author comment:** 27 pages, 7 figures, 9 tables

**Abstract.** Multi-image understanding requires MLLMs not only to recognise the content of individual images, but also to organise visual evidence distributed across them. We study this problem through multi-image re-representation, viewing prompted Chain-of-Thought reasoning and agentic visual tool use as different ways of re-organising visual evidence during reasoning. We introduce Mosaic, a general-purpose multi-image visual harness that enables an MLLM to actively construct visual intermediates with ten composable image operations. We compare five re-representation settings on existing multi-image benchmarks and on MosaicBench, a new grounding-focused benchmark for fine-grained multi-image understanding. Our experiments show that the relative benefits of textual and visual re-representation are strongly task-dependent. Visual re-representation is particularly effective for tasks requiring precise visual evidence, including hypothesis testing, precision comparison, and orientation-sensitive reasoning, while tasks dominated by higher-level semantic content show smaller or less consistent gains. Building on this finding, we train MosaicAgent-8B to use Mosaic with reinforcement learning using only accuracy and format rewards. Without demonstration trajectories or rewards for specific tool-use, the agent learns to compose visual operations over multiple steps and exhibits diverse problem-solving patterns unpromptedly. Code and data will be released at https://github.com/gengyuanmax/Mosaic.

**Key innovations.**

- Reframes multi-image understanding as **multi-image re-representation**: prompted CoT and agentic visual tool use are two ways of reorganizing visual evidence during reasoning, not two unrelated capabilities.
- **Mosaic** is a general-purpose multi-image visual harness with **ten composable image operations**, letting an MLLM actively construct visual intermediates instead of only reading pixels.
- Ships **MosaicBench**, a new grounding-focused benchmark for fine-grained multi-image understanding, alongside a comparison of five re-representation settings.
- The empirical claim is task-dependence, not "tools win": visual re-representation pays off on tasks needing **precise visual evidence** — hypothesis testing, precision comparison, orientation-sensitive reasoning — while higher-level semantic tasks show smaller or inconsistent gains.
- **MosaicAgent-8B** learns multi-step operation composition with RL on **accuracy and format rewards only** — no demonstration trajectories and no tool-specific rewards — and still shows diverse problem-solving patterns unprompted.

---

### 32. VisionQ: VLM-as-a-Judge Taxonomy, Dataset and Benchmark for Qualitative Analysis in Computer Vision

- **arXiv:** [2610.00666](https://arxiv.org/abs/2610.00666) · submitted 2026-09-30 · primary category `cs.CV` · all categories: `cs.CV`, `cs.AI`
- **Authors:** Vu Dinh Xuan; Duc-Hai Nguyen; Minh-Dung Dao; Vu Quynh Giao; Quang Hong Nguyen; Binh-Son Hua; Barry O'Sullivan; David Murphy; Hoang D. Nguyen
- **Institution / company:** University of Information Technology, VNU-HCM (Vietnam); University College Cork (Ireland); Hanoi University of Science and Technology (Vietnam); Trinity College Dublin (Ireland)
- **Affiliation evidence:** verified from author block
- **Author comment:** 29 pages, 18 figures, 6 tables

**Abstract.** Qualitative comparison figures are central evidence in computer vision papers, and vision-language models (VLMs) are increasingly used to judge them. Yet existing benchmarks score only scalar quality or overall preference, so a judge can be rewarded for picking the preferred image for the wrong visual reason. We introduce VisionQ, the first benchmark built from peer-reviewed CV comparison figures that grounds every judgment in a named visual criterion: each question states the criterion, and a judge is credited only when it selects the output the authors identify as best on that criterion. We call this task criterion-conditioned visual discrimination. VisionQ comprises (1) a corpus of 1,409 CVPR and ICCV papers with 1,800+ validated comparison figures and 3,911 hand-annotated data points linking method crops to author-stated visual claims; (2) a six-axis, 51-leaf taxonomy of the visual criteria behind qualitative judgment; (3) a criterion-conditioned evaluation protocol that hides method names, captions, and paper identity and reports accuracy per criterion; and (4) VisionQ-Judge, a DPO-tuned Gemma-4-E4B judge trained on symmetric evidence pairs, which reduces last-option predictions by 7.0pp and improves accuracy by 2.5pp on a held-out test set. Evaluating 20 open- and closed-source VLM judges, we find that the strongest reach only 63.1% accuracy (chance 32.2%) and that reliability varies sharply across criteria.

**Key innovations.**

- Identifies the reward-hacking surface in VLM-as-judge for CV: existing benchmarks score scalar quality or overall preference, so **a judge is rewarded for picking the preferred image for the wrong visual reason**.
- **VisionQ** grounds every judgment in a **named visual criterion**, crediting a judge only when it picks what the *authors* identify as best on that criterion — the task is *criterion-conditioned visual discrimination*.
- Substantial annotation effort: **1,409 CVPR/ICCV papers, 1,800+ validated comparison figures, 3,911 hand-annotated data points**, plus a **six-axis, 51-leaf taxonomy** of visual criteria.
- Protocol detail that matters: the evaluation **hides method names, captions and paper identity**, and reports accuracy *per criterion*.
- Ships a fix as well as a benchmark — **VisionQ-Judge**, a DPO-tuned Gemma-4-E4B trained on symmetric evidence pairs, cuts last-option predictions by **7.0 pp** and gains **2.5 pp** accuracy.
- The headline finding: across **20 open and closed VLM judges the strongest reaches only 63.1%** (chance 32.2%), and **reliability varies sharply across criteria** — so a single aggregate judge score hides the failure.

---

### 33. Do MLLM Judges Judge the Edit? Auditing Bias in Image Editing Evaluation with Verified Quality Preservation

- **arXiv:** [2610.01670](https://arxiv.org/abs/2610.01670) · submitted 2026-10-01 · primary category `cs.CV` · all categories: `cs.CV`, `cs.LG`
- **Authors:** Yuan Huang; Zirui Song; Xiuying Chen
- **Institution / company:** Northeastern University; Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)
- **Affiliation evidence:** verified from author block (first and third authors are visiting students at MBZUAI)
- **Author comment:** 30 pages, 9 figures

**Abstract.** Multimodal large language models (MLLMs) are increasingly used as automated judges for instruction-based image editing and as reward signals for model training. However, systematically auditing whether these judges are influenced by cues irrelevant to editing quality is challenging because visual interventions may themselves alter the quality being evaluated. A judgment shift can therefore be attributed to bias only when the intervention is verified to preserve the underlying editing quality. To address this challenge, we introduce EditJudgeBias, a counterfactual benchmark with verified quality preservation, comprising 1,196 real editing samples and 13 cues injected across four evaluation sites. We verify quality preservation for the requested edit using calibrated multimodal validators, controls, and human inspection. We then audit five MLLM judges along three complementary dimensions: invariance to quality-preserving cues, agreement with human judgments, and stability of pairwise preferences. Importantly, observed shifts are evaluated against each judge's own zero-dose and re-query noise floors rather than against zero. Experiments show that quality-preserving cues move every judge beyond its own noise. Fabricated majority opinions increase ratings, irrelevant visual elements cause larger shifts than whole-image manipulations, and swapping candidate order reverses up to 60.9% of pairwise decisions. Edit-region cues also tend to reduce human agreement.

**Key innovations.**

- Solves the methodological trap that makes image-editing judge auditing invalid: **a visual intervention may itself change the quality being judged**, so a judgment shift is only evidence of bias if the intervention is *verified* to preserve editing quality.
- **EditJudgeBias**: 1,196 real editing samples, **13 cues across four evaluation sites**, with quality preservation verified by calibrated multimodal validators, controls **and human inspection**.
- The measurement choice is the best part: shifts are judged against **each judge's own zero-dose and re-query noise floor**, not against zero — so "bias" means *beyond that judge's own noise*.
- Results are uncomfortable for the field: **quality-preserving cues move every judge beyond its own noise**; fabricated majority opinions increase ratings; **irrelevant visual elements shift judgments more than whole-image manipulations**; and **swapping candidate order reverses up to 60.9% of pairwise decisions**.
- Three measures (invariance, human agreement, preference stability) characterize judges *differently*, which the authors use to argue robustness **cannot be captured by a single metric** — and note edit-region cues also reduce *human* agreement.

---

### 34. 4MT-VLM: How Coarse Is a VLM's Cognitive Map?

- **arXiv:** [2609.39238](https://arxiv.org/abs/2609.39238) · submitted 2026-09-30 · primary category `cs.CL` · all categories: `cs.CL`
- **Authors:** Markus Frey
- **Institution / company:** Lamarr Institute for Machine Learning and Artificial Intelligence; Fraunhofer IAIS, University of Bonn
- **Affiliation evidence:** verified from author block

**Abstract.** An agent that moves must recognise a place from a viewpoint it has never seen. We introduce 4MT-VLM, a dataset of procedurally generated landscapes, each rendered across five stimulus modes that remove appearance cues while holding layout fixed: shape and colour, shape only, colour only, bare terrain peaks with no objects, and a valley viewpoint that puts the peaks on the horizon. The last condition is commonly used in clinics to probe hippocampal function in human patients. We test this benchmark across sixteen different open and closed-source models and report 4AFC performance, a measure which is also used to grade human participants. We observe that models identify a place from the studied viewpoint but lose it once the camera moves, dropping below the 25% chance level at 135° where a human observer scores 85%. Frontier models (Gemini 3.8 Flash, GPT-5.6) answer only 39% and 31% of rotated trials correctly, recovering to 85% and 55% only when distractors are moved more than 30 meters apart. Our benchmark demonstrates that while current VLMs possess rudimentary cognitive maps, their spatial resolution remains fundamentally too coarse to maintain a stable, 3D understanding of the world once the viewpoint changes.

**Key innovations.**

- Borrows a **clinical instrument**: the final stimulus mode — a valley viewpoint placing terrain peaks on the horizon — is the condition used in clinics to probe hippocampal function, and 4AFC is the same measure used to grade humans. So the models are being scored on a task with a human reference.
- Clean stimulus design: procedurally generated landscapes rendered across **five modes that remove appearance cues while holding layout fixed** (shape+colour, shape only, colour only, bare terrain peaks, valley viewpoint) — appearance is varied out, layout is controlled.
- The result is a **rotational cliff**: models recognize a place from the studied viewpoint but fall apart once the camera moves, dropping **below the 25% chance level at 135°** where a human observer scores **85%**.
- Quantified for frontier models: Gemini 3.8 Flash answers **39%** and GPT-5.6 **31%** of rotated trials correctly, recovering to 85% and 55% only when distractors are moved **more than 30 meters apart** — i.e. performance is rescued by making the task easier, not by better mapping.
- Conclusion is carefully bounded: VLMs have **rudimentary** cognitive maps, but spatial resolution is *fundamentally* too coarse to maintain a stable 3D understanding across viewpoint change. Tested across **16 open and closed models**.

---

### 35. DrivingBench: Can Vision-Language Models Drive a Toyota Corolla?

- **arXiv:** [2609.38948](https://arxiv.org/abs/2609.38948) · submitted 2026-09-30 · primary category `cs.RO` · all categories: `cs.RO`, `cs.AI`
- **Authors:** Aditya Ramabadran; Simon Mahns; Tobias Gessler
- **Institution / company:** ⚠️ **not stated.** The HTML author block renders numeric superscripts with no institution text; the abstract states the authors are at the same institution but does not name it. **Not inferred.**
- **Affiliation evidence:** abs page authors only — numeric superscript markers carry no institution text
- **Author comment:** the car keeps moving while the model thinks

**Abstract.** Frontier models excel at many digital benchmarks, yet their ability to drive a real car, an everyday human skill, remains largely untested. We present DrivingBench, to our knowledge the first benchmark where general-purpose vision-language models must drive a real car. Through three tools, the models see camera frames from a Toyota Corolla and directly command its steering and velocity around a parking lot cone course at low speeds. The car may continue moving while the model thinks and new commands replace the currently running one, so inference latency is part of the task, testing the models' abilities to observe, act, monitor, recover, and complete a long-horizon objective under such constraints. We benchmark GPT-6 Astra, Claude Fable 5.1, GPT-5.6 Sol, and Grok 4.6 in vendor-native harnesses (Codex, Claude Code, Cursor) with up to three attempts each in one conversation; Astra is the only model to finish the course, on its second attempt, with no other attempt passing 50% of the course. Two of the four models improved materially across attempts with retained context. We also detail the design principles behind our action interface, and show how the tool output format and the framing of the task combined to determine whether models would drive at all or refuse. We release our harness, prompts, course map, and traces with video and telemetry for reproducibility.

**Key innovations.**

- Closes a specific gap: frontier models ace digital benchmarks, but **driving a real car** — an everyday human skill — was untested. First benchmark where general-purpose VLMs must actually drive a real car (Toyota Corolla) via three tools commanding steering and velocity.
- The interface makes **inference latency part of the task**: the car keeps moving while the model thinks, and new commands *replace* the currently running one. That tests observe/act/monitor/recover/complete under real latency, not just accuracy.
- Results are stark and worth the read: of GPT-6 Astra, Claude Fable 5.1, GPT-5.6 Sol and Grok 4.6 in vendor-native harnesses (Codex, Claude Code, Cursor), **Astra alone finished, on attempt two, and no other attempt passed 50% of the course.** Two of four improved materially across attempts with retained context.
- The most transferable finding is about **failure of willingness, not capability**: the tool output format and the task framing together determined **whether models would drive at all or simply refuse** — a benchmark-design result about how VLM evaluations can accidentally measure refusal.
- Releases harness, prompts, course map, and traces with **video and telemetry**.

---

## Robotics & Embodied AI (5)

### 36. UniWAM: Unified World-Action Model

- **arXiv:** [2610.02054](https://arxiv.org/abs/2610.02054) · submitted 2026-10-01 · primary category `cs.RO` · all categories: `cs.RO`
- **Authors:** Jiayi Chen; Wenxuan Song; Jingbo Wang; Shuai Zhou; Xicheng Gong; Zehua Fan; Ziyang Zhou; Junwu E; Haodong Yan; Fuhao Li; Qize Yu; Xu Huang; Pengwei Wang; Wen Chen; Shunbo Zhou; Haoang Li (listed as "UniWAM Team")
- **Institution / company:** ⚠️ **not stated.** The HTML author block carries the collective name "UniWAM Team" with no institution text. **Not inferred.**
- **Affiliation evidence:** authors listed under a team name only

**Abstract.** Vision-language-action models benefit from the understanding and reasoning capabilities of pretrained vision-language models, but action-only supervision provides limited grounding in world dynamics. Conversely, world-action models inherit spatiotemporal priors from video generation models, yet remain limited in semantic understanding and reasoning under distribution shifts. We introduce UniWAM, a unified architecture that integrates a physical reasoner, a world generator, and an action predictor to jointly learn semantic understanding of the physical world, visual generation, and action prediction. To ensure the quality of the training data, we developed a rigorous data cleaning and annotation pipeline for both human egocentric data and robot data. To adapt the vision-language component to embodied tasks while preserving its inherited language capabilities, we represent low-level actions in natural language and introduce a pre-training recipe that assigns complementary supervision from visual question answering (VQA) data, human egocentric data, and robot demonstrations to the appropriate model components. During post-training, future visual noise augmentation reduces reliance on precise future predictions, while history-conditioned flow matching uses encoded action history to initialize action generation. Together, these designs significantly reduce denoising steps while maintaining performance. UniWAM achieves state-of-the-art (SOTA) performance across multiple evaluations, including in-distribution performance, robustness, generalization, instruction following, and long-horizon task execution. Furthermore, we uncover a log-linear scaling law of unified human-robot co-training, demonstrating the effectiveness of large-scale pre-training on a mixture of human and robot data.

**Key innovations.**

- States the trade-off precisely before solving it: **VLA models** get understanding and reasoning but lack grounding in world dynamics (action-only supervision); **world-action models** get spatiotemporal priors from video generation but lack semantic understanding and reasoning under distribution shift.
- **UniWAM** integrates three named components — a **physical reasoner**, a **world generator**, and an **action predictor** — trained jointly on semantic understanding, visual generation and action prediction.
- Two under-appreciated engineering decisions: low-level actions are represented **in natural language** so the VLM component adapts to embodied tasks without losing inherited language capability; and the pre-training recipe **assigns complementary supervision** (VQA data, human egocentric data, robot demonstrations) to the *appropriate* components rather than pooling it.
- Concrete efficiency gain from the training choices: **future visual noise augmentation** reduces reliance on precise future predictions and **history-conditioned flow matching** initializes action generation from encoded history, together **significantly reducing denoising steps while maintaining performance**.
- Reports a **log-linear scaling law for unified human–robot co-training**, plus SOTA across in-distribution performance, robustness, generalization, instruction following and long-horizon execution.

---

### 37. TOAST: Stochastic Robot Action Tokenization for Autoregressive Vision-Language-Action Models

- **arXiv:** [2610.00899](https://arxiv.org/abs/2610.00899) · submitted 2026-10-01 · primary category `cs.RO` · all categories: `cs.RO`, `cs.AI`, `cs.LG`
- **Authors:** Keisuke Shirai; Tomohiro Motoda; Hanbit Oh; Ryoichi Nakajo; Roman Mykhailyshyn; Ryo Hanai; Shotaro Miwa; Yukiyasu Domae
- **Institution / company:** AIST (National Institute of Advanced Industrial Science and Technology, Japan)
- **Affiliation evidence:** verified from author block

**Abstract.** Autoregressive Vision-Language-Action models often represent continuous robot actions as discrete token sequences, enabling action prediction with standard next-token objectives. FAST has substantially improved this representation by compactly encoding action containing diverse temporal frequencies into relatively few tokens. However, while such compression reduces the number of action tokens required for autoregressive prediction, it does not necessarily improve the efficiency of policy learning from limited demonstrations. In particular, FAST typically assigns a single deterministic tokenization to each quantized action sequence, although multiple token sequences can represent and decode to the same robot motion. We investigate whether exploiting this representational redundancy can improve policy learning. In this paper, we propose TOkenization of Action sequences with STochastic sampling (TOAST), a stochastic action tokenization method that samples alternative tokenizations of the same quantized action sequence during policy training. This diversifies the discrete supervision while preserving the underlying robot action and requires no additional demonstrations. Experiments on LIBERO show that TOAST consistently improves over its deterministic counterpart, with the improvement increasing as training data decreases, achieving a 6.8 point gain in success rate when only 1/16 of training data is available. Across four real-robot manipulation tasks, TOAST further improves mean success rate by 15.8 points over the deterministic counterpart.

**Key innovations.**

- Separates two things FAST conflates: compressing actions into fewer tokens improves *prediction efficiency* but **does not necessarily improve policy learning from limited demonstrations**.
- Spots unused representational redundancy: FAST assigns a **single deterministic tokenization** to each quantized action sequence, yet **multiple token sequences decode to the same robot motion**.
- **TOAST** samples alternative tokenizations of the *same* quantized action during training — diversifying discrete supervision while preserving the underlying action, and requiring **no additional demonstrations**.
- The data-efficiency scaling is the striking result: gains *grow* as data shrinks, reaching **+6.8 points** success on LIBERO with only **1/16** of the training data; **+15.8 points** mean success across four real-robot manipulation tasks.

---

### 38. Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models

- **arXiv:** [2609.39820](https://arxiv.org/abs/2609.39820) · submitted 2026-09-30 · primary category `cs.RO` · all categories: `cs.RO`, `cs.AI`
- **Authors:** Mingyue Cui; Zheyuan Liu; Yihan Zhu; Zheyuan Zhang; Meng Jiang
- **Institution / company:** University of Notre Dame
- **Affiliation evidence:** verified from author block (first two authors marked equal contribution)
- **Author comment:** Runtime-feedback-driven self-evolution for safer VLA policies

**Abstract.** Vision-language-action (VLA) models generalize broadly across robotic manipulation tasks, but complex environments require balancing task success with unintended contact. Runtime shields can correct individual actions, but they leave the underlying policy unchanged, so repeated disagreements may create a persistent policy-shield mismatch that blocks task progress. To address this challenge, we introduce FailBank, a four-stage self-evolving framework that converts runtime feedback into persistent policy improvement. During collection, a fixed CBF-based safety module serves as an observe-only teacher, producing counterfactual corrections while the policy remains in control. Outcome-aware admission then converts useful proposals into corrective targets and retains successful uncorrected actions as quiet anchors for guarded LoRA updates. We evaluate FailBank on the VLA-Arena benchmark across two difficulty levels and two VLA backbones. Compared with the base policies, FailBank improves the joint success-cost operating point. Across the two backbones, FailBank improves task success rate by 8.5 and 6.9 percentage points, while reducing policy-induced cumulative cost by 35.6% and 23.8%, respectively. Compared with runtime shielding, FailBank raises task success rate by 25.4 and 9.5 percentage points, while maintaining comparable policy-induced cumulative cost.

**Key innovations.**

- Identifies why runtime safety shields plateau: they correct individual actions but **leave the underlying policy unchanged**, so repeated disagreements accumulate a **persistent policy–shield mismatch** that blocks progress.
- **FailBank** converts runtime feedback into *persistent* policy improvement via four stages, with two mechanisms worth naming: a fixed **CBF-based safety module acts as an observe-only teacher**, producing counterfactual corrections while the policy stays in control; and **outcome-aware admission** keeps successful *uncorrected* actions as "quiet anchors" for guarded LoRA updates — so the safety teacher never fully takes over.
- Evaluated on the **joint success–cost operating point**, not success alone: against base policies, task success +8.5 and +6.9 pp while policy-induced cumulative cost drops **35.6%** and **23.8%**.
- The comparison that matters is against the obvious alternative: versus runtime shielding, FailBank raises task success by **25.4 and 9.5 pp** at comparable cost — i.e. learning the correction beats repeatedly applying it.
- Two difficulty levels × two VLA backbones on VLA-Arena.

---

### 39. When Reasoning Helps Action: Monitoring and Steering Chain-of-Thought in Vision-Language-Action Policies

- **arXiv:** [2610.00601](https://arxiv.org/abs/2610.00601) · submitted 2026-09-30 · primary category `cs.RO` · all categories: `cs.RO`, `cs.AI`
- **Authors:** Sathwik Karnik; Joseph JR. Lee; Aryaman Gupta; Somil Bansal
- **Institution / company:** Safe and Intelligent Autonomy Lab, Stanford University
- **Affiliation evidence:** verified from author block

**Abstract.** Reasoning-enabled VLA policies expose chain-of-thought (CoT) traces that appear to explain and guide their actions, creating a potential interface for runtime safety through reasoning monitoring and correction. In this work, we define and operationalize two evaluation axes for assessing when this interface can improve embodied behavior: correctability, which measures whether unreliable reasoning can be detected and improved during generation, and actionability, which measures whether reasoning corrections produce behaviorally meaningful changes in the intended direction. To enable correctability, we introduce Token-level Reward for Utility-Steered Chain-of-Thought (TRUST), an offline-trained value model that predicts eventual reasoning correctness from partial prefixes and uses these estimates to monitor and selectively steer reasoning generation in frozen VLA policies. On the Alpamayo 1.5 driving VLA, TRUST monitors correctness with 88.9% accuracy and improves reasoning correctness from 75.9% to 90.0%. On a baseline-defined challenging subset in AlpaSim, TRUST reduces collision rate by 30.4% and maximum trajectory error by 11.5% relative to the unsteered policy, outperforming a compute-matched Best-of-4 baseline. On the DeepThinkVLA manipulation VLA, TRUST improves the correctness of grasp-state claims from 69.3% to 90.2% and action-choice claims from 68.8% to 85.9%, yet closed-loop task performance on LIBERO-Plus remains largely unchanged. Empirical analysis reveals intent-consistent behavioral effects in Alpamayo 1.5 but limited effects in DeepThinkVLA, helping interpret these different task-level outcomes.

**Key innovations.**

- The conceptual contribution is the **two-axis evaluation framework**: **correctability** (can unreliable reasoning be detected and improved during generation?) and **actionability** (do reasoning corrections produce behaviorally meaningful change in the intended direction?). Most CoT-safety work measures only the first.
- **TRUST** is an offline-trained value model predicting eventual reasoning correctness from *partial prefixes*, used to monitor and selectively steer reasoning in **frozen** VLA policies — no policy retraining.
- Strong on driving: monitors correctness at **88.9%** accuracy and lifts reasoning correctness **75.9% → 90.0%** on Alpamayo 1.5; on AlpaSim it cuts collision rate **30.4%** and max trajectory error **11.5%**, beating a **compute-matched Best-of-4**.
- The negative half of the result is the valuable half: on DeepThinkVLA manipulation, claim correctness improves substantially (grasp-state **69.3% → 90.2%**, action-choice **68.8% → 85.9%**) yet **closed-loop task performance on LIBERO-Plus remains largely unchanged**.
- Conclusion stated plainly: **gains in reasoning correctness do not automatically imply gains in embodied performance** — which is why both axes must be measured when CoT is proposed as a runtime safety interface.

---

### 40. Scale and Selection: What Makes Automatic Harness Evolution Work for Visual-Interface Robot Agents

- **arXiv:** [2609.39304](https://arxiv.org/abs/2609.39304) · submitted 2026-09-30 · primary category `cs.RO` · all categories: `cs.RO`, `cs.AI`
- **Authors:** Zhijie Wei; Ferris Tan; Jinghui Wang
- **Institution / company:** Novaxbot
- **Affiliation evidence:** verified from author block
- **Author comment:** 12 pages, 4 figures

**Abstract.** When an off-the-shelf coding agent is used directly as a robot policy, observing a browser-based 3D interface through screenshots and acting by posing a virtual target gripper through a few tools, the agent's harness, its prompts, tools, and control rules, largely determines success, and until now it has been written by hand. We show that this harness can be improved automatically by another coding agent, the optimizer agent, and report two findings about what makes it work. First, the number of rollouts the optimizer agent sees per round governs whether the evolved harness is trustworthy, generalizes, and improves steadily. A single rollout is a noisy binary outcome, so with few rollouts per round a revision can be promoted on luck; enlarging the batch raises the signal-to-noise ratio of every promotion decision. Holding rounds fixed and growing the training set from 5 to 100 rollouts, held-out success rises from 47% to 67%, while small training sets overfit, reaching 70% on training tasks but only 54% held-out. Second, the optimizer agent must not be given free rein. With every revision it proposes accepted unconditionally, performance drifts downward within ten rounds as ill-judged edits accumulate; adding the most basic safeguard, Champion-Challenger selection that promotes a revision only if it strictly beats the incumbent on the same fixed evaluation set, turns the same loop into one that raises held-out success from 51% to 67% over 30 rounds. Automatic harness evolution for visual-interface robot agents is thus feasible, but its gains hinge on the rollout scale behind each decision and on how the optimizer agent's revisions are selected.

**Key innovations.**

- Sets up the harness question in a deliberately narrow, honest setting: an off-the-shelf coding agent as robot policy, watching a **browser-based 3D interface** through screenshots and posing a virtual target gripper through a few tools — so prompts, tools and control rules, not perception, largely determine success.
- Then shows the hand-written harness **can be evolved automatically by another coding agent**, and extracts two findings that generalize well past robotics.
- Finding 1 — **scale**: with rounds fixed, growing the optimizer's evidence from 5 to 100 rollouts lifts held-out success **47% → 67%**, because one rollout is a noisy binary outcome and small batches promote revisions **on luck**. Small training sets visibly overfit: 70% on training tasks, only 54% held-out.
- Finding 2 — **selection**: accepting every proposed revision makes performance **drift downward within ten rounds** as ill-judged edits accumulate; adding the most basic safeguard, **Champion–Challenger** promotion on a fixed evaluation set, turns the same loop into one that raises held-out success **51% → 67% over 30 rounds**.
- Small industrial-lab paper (Novaxbot) whose negative results are the point: automatic harness evolution is feasible, but gains hinge on rollout scale per decision and on how revisions are selected.

---

## Recommendation, Ads, Retrieval & Sequential Modeling (7)

> **Coverage note.** This is the thinnest section and it is thin for a structural reason, not a selection error: across the 1,061 unclaimed candidates in the window, there is **no CTR-prediction paper, no advertising/bidding paper, and no large-scale user-behavior sequential-modeling paper**. See §9 Vacancies.

### 41. Evaluating Biomedical Reranking for LLM-Based Question Answering over Longitudinal Clinical Notes

- **arXiv:** [2610.01324](https://arxiv.org/abs/2610.01324) · submitted 2026-10-01 · primary category `cs.CL` · all categories: `cs.CL`, `cs.ET`
- **Authors:** Maryam Shahbaz Ali; Laura B. Strachan; Caitlin Sherman; Mark Kovler; Eleanor Mackey; Syed Muhammad Anwar
- **Institution / company:** ⚠️ **not stated.** arXiv serves **no HTML rendition** for this submission (`HTML is not available for the source`), so no author block could be read. The abs page lists authors only. **Not inferred.**
- **Affiliation evidence:** abs page authors only — no HTML author block available

**Abstract.** Patient-specific clinical question answering requires locating the right evidence within long, heterogeneous longitudinal clinical records in which relevant facts may be scattered across encounters, repeated in copied-forward notes, or expressed using different clinical terminology. We evaluated whether biomedical reranking can improve evidence selection and downstream answer quality in a locally deployed retrieval-augmented generation pipeline for longitudinal clinical notes. The pipeline combines PubMedBERT dense retrieval, BM25 lexical retrieval, weighted reciprocal-rank fusion, and MedCPT cross-encoder reranking. Across 1,000 open- and closed-ended question-answer pairs from a cohort of 200 bariatric surgery patients, reranking increased exact source-chunk retrieval within the top 10 items, Hit@10 from 46.6% to 60.6% and mean reciprocal rank from 0.2371 to 0.3252. With Qwen3-8B generation, local judge-assessed answer correctness increased from 44.8% to 48.6%. These results show that biomedical reranking can improve the placement of relevant clinical evidence within a limited context window, although gains in retrieval do not translate proportionally into gains in answer correctness.

**Key innovations.**

- Value here is a **fully specified hybrid retrieval stack** rather than a new retriever: PubMedBERT dense retrieval + BM25 lexical retrieval + weighted reciprocal-rank fusion + MedCPT cross-encoder reranking, inside a **locally deployed** RAG pipeline.
- Reranking is the only component varied across conditions, which makes the retrieval→answer delta legible rather than confounded.
- Retrieval moves substantially: **Hit@10 46.6% → 60.6%** and **MRR 0.2371 → 0.3252**.
- The most valuable result is the **disconnect**: with Qwen3-8B generation and a local judge, answer correctness rose only **44.8% → 48.6%**. Retrieval gains do **not** translate proportionally into answer gains — a caution for anyone building retrieval-heavy pipelines.
- Scale is modest and stated plainly (1,000 open- and closed-ended QA pairs, 200 bariatric-surgery patients), which bounds how far these numbers generalize.

---

### 42. Not All Is Lost: Repairing Lossy User Preference States of Personalization Encoders

- **arXiv:** [2610.01270](https://arxiv.org/abs/2610.01270) · submitted 2026-10-01 · primary category `cs.LG` · all categories: `cs.LG`, `cs.IR`
- **Authors:** Parthiv Chatterjee; Dhiraj Golhar; Ummesalma Diwan; Sourish Dasgupta; Manjunath Joshi; Tanmoy Chakraborty
- **Institution / company:** ⚠️ **not stated.** The HTML author block carries no affiliation markup for any author, and no institution string appears in the rendered text. **Not inferred.**
- **Affiliation evidence:** abs page authors only — no affiliation markup of any kind in the author block
- **Author comment:** **Accepted to NeurIPS 2026.** Author-prepared archival version with expanded discussion and interpretation. 59 pages, including references and appendices

**Abstract.** Personalization encoders compress evolving interaction histories into preference states used to rank items or condition text generation. A task head operating only on this state can miss useful evidence that remains in the frozen encoder's cached representations for individual timesteps. We study this recoverability gap and propose REPAIR, which compares cached representations with the current preference state in a compact learned coordinate space. It resolves corrective evidence over extended history, recent interactions, and localized bursts. It then selects which patterns at which timesteps contribute and adds their aggregate correction to the state before the task head. Encoder-host repair reuses representations from the existing forward computation without re-encoding the history. Across MovieLens, PENS, MIND, and Amazon Reviews 2023, training only REPAIR improves MRR and nDCG@10 for all twelve representative recommendation hosts while both encoder and task head remain frozen. Head-only finetuning of the same hosts yields smaller gains. For example, Mamba4Rec on MovieLens gains 3.96 MRR points, compared with 0.19 from head-only finetuning. Rank and temporal diagnostics support a compact, host-dependent corrective structure. In personalized generation, IMPerSumm improves the two reported weighted PerSEval variants, which assess responsiveness to user preference, by up to 25.23%. These results support post-compression state correction and distinguish the availability of preference evidence from its downstream use.

**Key innovations.**

- Frames a **recoverability gap** in personalization encoders: they compress an evolving interaction history into a preference state, so evidence that remains useful in the frozen encoder's *per-timestep cached representations* becomes unreachable to any task head that sees only the state.
- **REPAIR** compares cached representations against the current preference state in a **compact learned coordinate space**, resolves corrective evidence across three horizons (extended history, recent interactions, localized bursts), selects which patterns at which timesteps contribute, and adds the aggregate correction to the state before the task head.
- The engineering constraint is what makes it deployable: **encoder-host repair reuses representations from the existing forward computation**, so history is never re-encoded.
- Strong claim, since **both encoder and task head stay frozen** and only REPAIR is trained: MRR and nDCG@10 improve for **all twelve** representative recommendation hosts across MovieLens, PENS, MIND and Amazon Reviews 2023. The head-only finetuning control is decisive — Mamba4Rec on MovieLens gains **3.96 MRR points** from REPAIR vs **0.19** from head-only finetuning, a ~20× gap.
- Rank and temporal diagnostics support a **compact, host-dependent** corrective structure; in personalized generation IMPerSumm improves weighted PerSEval variants by up to **25.23%**.
- Conceptual payoff: it separates the **availability** of preference evidence from its **downstream use** — a distinction that applies well beyond recommendation.

---

### 43. RPTune: Learned Context Curation for LLM Catalog Search

- **arXiv:** [2610.00964](https://arxiv.org/abs/2610.00964) · submitted 2026-10-01 · primary category `cs.IR` · all categories: `cs.IR`, `cs.CL`, `cs.LG`
- **Authors:** Chuxuan Hu; Hejie Cui; Norman Huang; Shubham Kumar Bharti; Wang-Chiew Tan; Sercan Ö. Arık
- **Institution / company:** Google; University of Illinois Urbana-Champaign (last author)
- **Affiliation evidence:** verified from author block
- **Author comment:** 23 pages, 9 figures, 4 tables

**Abstract.** For small merchant businesses (SMBs) whose catalogs fit within a long-context LLM, full-catalog prompting offers a compelling alternative to multi-stage retrieval designed primarily for large marketplaces with millions of items. However, fitting the catalog into the context window does not ensure that the model can use it effectively, since LLMs do not exploit long contexts uniformly. We therefore study in-context catalog search through two complementary questions: (1) how to curate and present catalogs to the LLM, and (2) how to adapt the LLM for product selection on curated contexts. We propose RPTune, an end-to-end framework that couples learned catalog curation with LLM post-training using automatically generated, catalog-grounded supervision. An encoder-reorganizer curator orders and prunes products guided by downstream LLM feedback, while the resulting curated catalogs in turn improve the effectiveness of LLM post-training with a context-relative reward. Evaluated on 7 real merchants spanning distinct retail verticals, using 100 complex conversational queries per merchant, RPTune consistently improves search accuracy across both proprietary and open-weight LLMs, with context curation yielding gains of up to 31.4 percentage points and post-training adding a further 10.3 points on average.

**Key innovations.**

- Identifies the deployment regime the multi-stage retrieval stack was **not** built for: SMB catalogs that **fit inside a long-context LLM**, making full-catalog prompting viable — and then names the real obstacle: fitting the catalog in the window does not mean the model can *use* it, because LLMs do not exploit long contexts uniformly.
- Frames the problem as two coupled questions — how to curate/present the catalog, and how to adapt the LLM for selection on curated contexts — and solves them as a **loop**: an **encoder-reorganizer** curator orders and prunes products guided by downstream LLM feedback, and the improved curated catalogs in turn make LLM post-training more effective via a **context-relative reward**.
- Supervision is **automatically generated and catalog-grounded**, so no human labeling of product selections is needed.
- Evaluation is on real merchants, not synthetic catalogs: **7 real SMBs across distinct retail verticals, 100 complex conversational queries each**, across both proprietary and open-weight LLMs.
- Gains decompose cleanly: **context curation up to +31.4 pp**, post-training a further **+10.3 pp on average**.

---

### 44. Targeted Retrieval, Compact Representations: How CoT Reasoning Improves Long-Context Counting

- **arXiv:** [2609.38958](https://arxiv.org/abs/2609.38958) · submitted 2026-09-30 · primary category `cs.AI` · all categories: `cs.AI`, `cs.CL`, `cs.LG`, `stat.AP`
- **Authors:** Liang Twist Shan; Tianyu Hu; Hao Yan; Yiqiao Zhong
- **Institution / company:** Department of Statistics, University of Wisconsin-Madison; Department of Computer Sciences, University of Wisconsin-Madison
- **Affiliation evidence:** verified from author block — Statistics and Computer Sciences listed as separate affiliations
- **Author comment:** 73 pages, including references and appendices

**Abstract.** Large language models (LLMs) have been rapidly improving in long-context tasks, powered by Chain-of-Thought (CoT) reasoning. However, the internal mechanisms underlying this improvement remain unclear. We investigate these mechanisms through a needle-in-a-haystack (NIAH) counting task, where an LLM is asked to count the number of records dispersed in a long text. Across twelve model comparison groups, Thinking (or reasoning) improves counting accuracy over Non-thinking, with pronounced gains at larger counts. This motivates our mechanistic analysis, which identifies two contrasting mechanisms: (i) broad retrieval, where Non-thinking models broadly attend to multiple needles; (ii) targeted retrieval, where Thinking models use enumeration in CoT traces to successively retrieve needles. Targeted retrieval concentrates attention on individual needles and is accompanied by more compact internal representations. Moreover, causal intervention analysis suggests that Thinking models use the CoT trace to maintain and update an internal counter as needles are successively retrieved, even without explicit numbering. In small controlled experiments, both retrieval mechanisms and counter states emerge under standard autoregressive training. Together, our results connect long-context retrieval with representation geometry of counting, supporting a state-tracking account of CoT reasoning.

**Key innovations.**

- Uses a **needle-in-a-haystack counting** task as a controlled microscope for long-context reasoning, then asks *why* thinking models are better at it.
- Names two contrasting retrieval mechanisms: **broad retrieval**, where Non-thinking models attend widely across many needles, and **targeted retrieval**, where Thinking models enumerate in the CoT trace and fetch needles successively.
- Targeted retrieval carries a **geometric** signature: attention concentrates on individual needles and internal representations become **more compact**.
- Causal intervention analysis suggests Thinking models maintain and update an **internal counter** across successive retrievals, with no explicit numbering required.
- Controls for the obvious objection: in small controlled experiments **both retrieval mechanisms and counter states emerge under standard autoregressive training** — so the contribution is about how these processes surface, not about training creating something new.
- Framing contribution: links long-context retrieval to the **representation geometry of counting**, supporting a state-tracking account of CoT reasoning.

---

### 45. TRACE: Trajectory Selection for Parallel Scaling of Search Agents

- **arXiv:** [2609.39912](https://arxiv.org/abs/2609.39912) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`
- **Authors:** Qisheng Zhou; Zhen Xiong; Qiaoyu Tan
- **Institution / company:** New York University Shanghai
- **Affiliation evidence:** verified from author block
- **Author comment:** 19 pages, 2 figures

**Abstract.** Parallel search may generate a correct answer that final-answer voting fails to select. We formulate this consolidation stage as trajectory selection and introduce TRACE (Trajectory Ranking with Aggregated Cross-Rollout Evidence), a lightweight learned selector that ranks completed trajectories using the search evidence behind their answers. TRACE preserves individual query and evidence occurrences, connects rollouts through shared content or document identity, and propagates information across these relations. Each candidate answer then reads the updated states of its own trajectory, preserving retrieval provenance while incorporating evidence from related rollouts. Trained with answer-level supervision over frozen text embeddings, TRACE returns an existing answer without additional search or autoregressive aggregation. One selector per search setting transfers across rollout policies and agent backbones without agent-specific fine-tuning, improving over voting across six WebQA policies and six long-horizon dataset-backbone combinations at K=16. On Qwen2.5-14B Base/SFT WebQA pools, TRACE achieves 45.2/49.2% EM, compared with 43.9/48.0% for the strongest Qwen3-32B generative aggregators. On long-horizon FRAMES, GAIA, and BrowseComp, it reaches 78.6% average accuracy, exceeding majority voting by 3.1 percentage points. On Base WebQA pools, TRACE with only 8 rollouts comes within 0.4 points of majority voting over 64. TRACE also achieves at least 10x higher processing throughput than SolAgg, SummAgg, and AggAgent across all seven WebQA benchmarks.

**Key innovations.**

- Reframes a failure that is usually reported as a retrieval problem: parallel search can **generate a correct answer that final-answer voting then fails to select**. The authors call the consolidation stage what it is — **trajectory selection**.
- **TRACE** ranks completed trajectories using *the search evidence behind their answers*: it preserves individual query and evidence occurrences, links rollouts through shared content or document identity, propagates across those relations, and lets each candidate answer read the updated state of its own trajectory — preserving retrieval provenance while borrowing evidence from related rollouts.
- The efficiency argument is structural: trained with answer-level supervision over **frozen text embeddings**, TRACE returns an already-existing answer, so it needs **no additional search and no autoregressive aggregation**.
- Generality is demonstrated, not asserted: **one selector per search setting** transfers across rollout policies and agent backbones without agent-specific fine-tuning.
- Strong numbers: beats voting across six WebQA policies and six long-horizon dataset–backbone combinations at K=16; a **14B selector (45.2/49.2% EM) beats the strongest Qwen3-32B generative aggregators (43.9/48.0%)**; 78.6% average on FRAMES/GAIA/BrowseComp (+3.1 pp over majority voting); **8 rollouts come within 0.4 points of majority voting over 64**; and **≥10×** the throughput of SolAgg, SummAgg and AggAgent on all seven WebQA benchmarks.

---

### 46. JoinGR: Learning to Traverse Join Graphs for Table Retrieval

- **arXiv:** [2610.01064](https://arxiv.org/abs/2610.01064) · submitted 2026-10-01 · primary category `cs.CL` · all categories: `cs.CL`, `cs.AI`, `cs.DB`, `cs.IR`
- **Authors:** Sandipan De; Abhijit Chakraborty; Sambaran Bandyopadhyay; Vivek Gupta
- **Institution / company:** Arizona State University; Adobe Research India
- **Affiliation evidence:** verified from author block

**Abstract.** Retrieving the right tables is a prerequisite for Text-to-SQL over realistic databases. Dense table retrievers rank schema elements independently, but this ignores a key source of evidence: some required tables are not mentioned in the question and become identifiable only through their join relationships to already relevant tables. We introduce JoinGR, a join-aware table retrieval method that treats the database join graph as the retrieval space. Columns are represented as graph nodes, while intra-table and foreign-key relationships are represented as typed edges. Given a question, JoinGR selects semantically similar anchor tables, traverses join edges with a query-conditioned scorer, and aggregates the resulting edge deposits into table scores. The scorer is a lightweight MLP on top of frozen query, node, and edge embeddings, trained with a pairwise margin loss over gold tables. On BIRD and Spider datasets, JoinGR is competitive with the strongest retrieval baselines. On BEAVER, a challenging enterprise benchmark with multi-hop table requirements, JoinGR substantially improves recall over dense retrieval and re-ranking baselines. Cross-domain experiments show that the learned scorer transfers across benchmarks, indicating that the method captures reusable join-graph traversal behavior.

**Key innovations.**

- Names the specific evidence dense retrievers throw away: **some required tables are never mentioned in the question** and become identifiable only through their **join relationships** to already-relevant tables.
- **JoinGR** makes the **database join graph the retrieval space** — columns are nodes, intra-table and foreign-key relations are *typed* edges — then selects semantically similar anchor tables, traverses join edges with a query-conditioned scorer, and aggregates edge deposits into table scores.
- Deliberately lightweight: the scorer is an **MLP on frozen query, node and edge embeddings**, trained with a pairwise margin loss over gold tables. No end-to-end retriever training.
- The enterprise benchmark **BEAVER** (multi-hop table requirements) is where the method earns its keep — substantial recall gains over both dense retrieval and re-ranking baselines — while on BIRD and Spider it is merely competitive with the strongest baselines.
- **Cross-domain transfer of the learned scorer** across benchmarks is the evidence that it captures reusable join-graph traversal behavior rather than benchmark-specific structure.

---

### 47. Algorithmic Recourse Under Competition

- **arXiv:** [2609.39877](https://arxiv.org/abs/2609.39877) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`
- **Authors:** Shahin Jabbari
- **Institution / company:** Drexel University
- **Affiliation evidence:** verified from author block (stated in the author footnote)

**Abstract.** Algorithmic recourse provides individuals who have received undesirable outcomes from machine learning models with suggestions for minimum-cost improvements to achieve the desired outcome. A central assumption when computing recourse is that the decision rule remains fixed throughout the recourse implementation phase. We challenge this assumption in settings where individuals compete for limited resources. In such settings, widespread recourse implementation can change the acceptance threshold even when the scoring model that is used to evaluate individuals remains the same. This change in acceptance threshold can, in turn, invalidate the original recourse recommendations (i.e., following the recourse may not lead to the desired outcome). To address this problem, we introduce a framework called recourse under competition that jointly optimizes for recommendation recipients and the recommended score target they need to satisfy to balance the recourse cost and post-shift validity among initially rejected individuals. We develop an algorithm based on the Implicit Function Theorem and empirically analyze its performance. Experiments on synthetic and real datasets show that personalized score targets can achieve higher validity, albeit at a higher cost. In contrast, common score targets generally offer favorable cost-validity trade-offs for lower to medium validity values.

**Key innovations.**

- Attacks a load-bearing but rarely stated assumption of algorithmic recourse: that **the decision rule stays fixed** while recourse is implemented.
- The mechanism is a genuine systems effect, not a modeling trick: when individuals **compete for limited resources**, widespread recourse implementation can move the **acceptance threshold** *even though the scoring model is unchanged* — which invalidates the original recommendations, i.e. **following the recourse may not produce the desired outcome**.
- The fix reframes the target: **recourse under competition** jointly optimizes over recipients *and* the score target each must hit, trading recourse cost against **post-shift validity**.
- Algorithm derived via the **Implicit Function Theorem**, with empirical analysis on synthetic and real data.
- The cost–validity frontier is reported honestly rather than optimized away: **personalized score targets achieve higher validity at higher cost**, while **common targets give better cost-validity trade-offs at lower-to-medium validity** — a Pareto statement, not a win.
- Read-across to ranking systems: any deployment where a fixed scoring model fronts a *capacity-constrained* threshold has the same latent instability.

---

## RL Theory, Games & Multi-Agent Economics (3)

> **Coverage note.** This section is small because the window's game/RL-environment supply is genuinely near-empty — see §9 Vacancies.

### 48. Spatial Strategies, Not Actions: Vector-Quantized Geodesics as Tools for LLM-Driven Agents

- **arXiv:** [2610.00613](https://arxiv.org/abs/2610.00613) · submitted 2026-09-30 · primary category `cs.AI` · all categories: `cs.AI`, `cs.RO`, `eess.SY`
- **Authors:** Gabriel Turinici
- **Institution / company:** CEREMADE CNRS, Université Paris Dauphine – PSL, Paris
- **Affiliation evidence:** verified from author block

**Abstract.** Large language model (LLM) based agents are often criticized for lacking spatial understanding and mainly exploiting statistical text patterns. We investigate their spatial comprehension through an architecture combining geometrical tools with a LLM serving as a high-level orchestrator in grid-world environments. The agent first collects geodesic trajectories, which are then vector-quantized to extract a representative subset. Offline, the LLM associates a natural language description of the underlying behavioral patterns to each selected trajectory, making it a tool. Online, the LLM chooses the appropriate tool conditioned on the current state and goal. Low-level control is handled by primitive actions that execute the trajectory associated with the tool. From an agentic AI perspective, this approach separates learning into two levels: tool discovery is handled through unsupervised quantization of trajectories, while reasoning and decision-making are handled by the LLM. We test the approach in a partially observable dynamic 2D grid environment with an open vision-language model (Qwen3.6-35B-A3B). Pairing the geometry-derived tool library with an agent-centered zoom tool and a collision detection tool lets a fast, non-reasoning configuration match the goal-reaching rate of a much more costly chain-of-thought version, while cutting the cost of a decision from minutes to seconds.

**Key innovations.**

- Takes the standard criticism of LLM agents — no spatial understanding, just statistical text patterns — as an engineering premise rather than a verdict, and answers it by **moving spatial competence out of the LLM entirely**.
- The architecture: collect **geodesic trajectories**, **vector-quantize** them to a representative subset, have the LLM *offline* attach a natural-language description of the behavioral pattern to each selected trajectory (making it a *tool*), and *online* have the LLM pick a tool given current state and goal. Low-level control stays with primitive actions executing the trajectory.
- The conceptual contribution is the **two-level separation of learning**: tool discovery is unsupervised quantization of trajectories; reasoning and decision-making is the LLM's job. The LLM never learns control.
- The result is a cost inversion: in a partially observable dynamic 2D grid world with Qwen3.6-35B-A3B, adding an agent-centered zoom tool and a collision-detection tool to the geometry-derived library lets a **fast non-reasoning configuration match the goal-reaching rate of a much costlier chain-of-thought version**, cutting per-decision cost **from minutes to seconds**.

---

### 49. Beyond Supra-Competitive Outcomes: Collusive Behaviour in Deep Reinforcement Learning for Optimal Execution Games

- **arXiv:** [2610.00619](https://arxiv.org/abs/2610.00619) · submitted 2026-09-30 · primary category `q-fin.TR` · all categories: `q-fin.TR`, `cs.AI`
- **Authors:** Christos Spyridon Koulouris; Carlo Campajola
- **Institution / company:** ⚠️ **not stated.** The HTML author block renders three bare `Affiliation:` labels with empty institution text. **Not inferred from author names.**
- **Affiliation evidence:** affiliation labels present but empty

**Abstract.** In this paper, we extend earlier findings of supra-competitive outcomes in optimal-execution games by identifying a learned punitive mechanism that deters deviations and provides behavioural evidence of collusion. We investigate this mechanism in a two-player, finite-horizon Almgren-Chriss liquidation game. Independent proximal policy optimisation agents with access to within-episode price and action histories achieve costs below the Nash benchmark. We identify a profitable deviation by training against the mean learned liquidation schedule, then impose its first trade on one of the original agents. The opponent responds by accelerating liquidation. This response more than offsets the deviator's gain in every run and both player roles, while leaving the punisher's average payoff materially unchanged relative to not punishing under the same deviation. The punisher imposes greater losses on the deviator while preserving its own average payoff, despite the availability of more profitable, less punitive liquidation plans. Matching deviations and subsequent additional selling rise and later decline during training, while final policies retain an effective punitive response. We formalise two checks: whether punishment outweighs the gain from deviating, and whether the change in trading behaviour is large enough to account for the loss imposed. Both checks hold for the tested deviation. Together, these findings provide behavioural and economic evidence supporting a collusive interpretation of the learned supra-competitive outcomes.

**Key innovations.**

- Extends prior observations of **supra-competitive** outcomes in optimal-execution markets by identifying a *mechanism*: independent PPO agents with within-episode price and action histories beat the **Nash benchmark** on cost in a two-player finite-horizon Almgren–Chriss liquidation game.
- The evidence is behavioral rather than statistical, and it is well designed: train an agent against the **mean learned schedule** to surface a profitable deviation, **impose that deviation's first trade** on one original agent, and watch the response — the opponent **accelerates liquidation**.
- The finding that makes it more than "agents collude": the punitive response **more than offsets the deviator's gain in every run and both player roles**, while leaving the **punisher's own average payoff materially unchanged** — and this happens *despite more profitable, less punitive plans being available*. That asymmetry (costly to the victim, free to the punisher) is the signature of collusion rather than of optimization error.
- Training-dynamics detail: matching deviations and subsequent extra selling **rise then decline** during training, while final policies **retain** an effective punitive response — so the behavior is learned, then consolidated.
- Formalizes two falsifiable checks — punishment outweighs the gain from deviating, and the behavioral change is large enough to account for the loss imposed — and **both hold**, which is the right standard for a claim this economically loaded.

---

### 50. Free Everywhere, Exact on Trees: PPO's Dropped Correction Buys Sample Efficiency Under Aggressive Reuse

- **arXiv:** [2609.39634](https://arxiv.org/abs/2609.39634) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`
- **Authors:** Nima H. Siboni
- **Institution / company:** Juna.ai (Berlin, Germany)
- **Affiliation evidence:** verified from author block (street address given)
- **Author comment:** explicitly disclaims the easy version of its own claim

**Abstract.** Common policy improvement methods, including TRPO, PPO, and GRPO, estimate policy improvement under the behavioral policy's state-visitation distribution rather than the improved policy's own. The substitution makes the objective estimable from the behavioral policy's rollouts but adds a bias growing with policy divergence, hence the trust region or clip, and hence no reuse of a batch far off-policy. We show that under history-injective dynamics, where each state is reached by exactly one history, the dropped state-visitation ratio equals the product of per-step policy ratios along the sampled prefix, on every trajectory and not only in expectation. The ratio is therefore restored exactly, from log-probabilities PPO already computes. Autoregressive generation and canonical-order constructive optimization are both history-injective. Autoregressive generation and canonical-order constructive optimization are both history-injective. On hard credit-assignment scheduling tasks, a short corrected warmup with aggressive early sample reuse learns faster than PPO and than the same reuse uncorrected; the marginal gain grows with task difficulty (+0.02 to +0.09 learning-curve AUC), while the early win over PPO tracks the prefix bias that reuse incurs. A correction held throughout, or applied where clipping already contains the reuse bias, is null to harmful.

**Key innovations.**

- Diagnoses the standard approximation precisely: TRPO/PPO/GRPO estimate improvement under the **behavioral** state-visitation distribution, which buys estimability but adds bias growing with policy divergence — hence the trust region, hence **no reuse of a batch far off-policy**.
- The theoretical contribution is a clean identification: under **history-injective dynamics** (each state reached by exactly one history), the dropped state-visitation ratio **equals** the product of per-step policy ratios along the sampled prefix — *on every trajectory, not only in expectation* — so it can be restored **exactly from log-probabilities PPO already computes**.
- Scope is stated honestly: autoregressive generation and canonical-order constructive optimization are both history-injective; general RL is not, so this is a *conditional* correction.
- Empirical claim is deliberately narrow: on hard credit-assignment scheduling tasks, a **short corrected warmup with aggressive early sample reuse** beats both PPO and uncorrected reuse, with the marginal gain growing with task difficulty (**+0.02 to +0.09 learning-curve AUC**), and the early win tracks the prefix bias reuse incurs.
- **Self-limiting by design, and this is the paper's best feature:** a correction held throughout, or applied where clipping already contains the reuse bias, is **null to harmful**. The title says it — *free everywhere, exact on trees*.

---

## Interpretability, Safety, Agents' Security & Measurement (9)

### 51. Making LLMs Say What They Think: Measuring and Improving CoT-Interpretability Alignment

- **arXiv:** [2609.38972](https://arxiv.org/abs/2609.38972) · submitted 2026-09-30 · primary category `cs.CL` · all categories: `cs.CL`, `cs.AI`
- **Authors:** Yihuai Hong; Shauli Ravfogel; Chen Zhao; Eunsol Choi
- **Institution / company:** New York University; NYU Shanghai
- **Affiliation evidence:** verified from author block
- **Author comment:** 28 pages, 9 figures, 10 tables

**Abstract.** Chain-of-thought (CoT) traces often serve as a proxy for how Large Language Models (LLMs) arrive at their answers. However, growing evidence shows that models' CoT often fails to reflect their internal computations and can be changed without affecting their final answers. In this work, we measure and improve the alignment between the reasoning described in an LLM's CoT and what it computes internally. We propose CoT-Interpretability Alignment (CIA), a metric that measures the agreement between a model's CoT traces and its internal reasoning strategies as detected by interpretability tools. We evaluate CIA on three tasks (two-hop question answering, hint intervention, and integer multiplication) across three LLMs, finding that LLMs exhibit limited alignment across all tasks (44.8-75.9%). We then experiment with improving CIA via post-training, setting both the task accuracy and parametric faithfulness signals as a reward. Experiments show that we can substantially improve CoT parametric faithfulness while maintaining or improving the task accuracy. We provide rich analysis, such as their generalization patterns.

**Key innovations.**

- Defines **CoT-Interpretability Alignment (CIA)**: agreement between what the CoT *says* and the internal reasoning strategies that interpretability tools actually detect. This makes "faithful CoT" a measurable quantity rather than an assertion.
- The baseline measurement is the finding: across two-hop QA, hint intervention and integer multiplication on three LLMs, alignment is only **44.8–75.9%** — so CoT is an unreliable window into computation even on trivial tasks.
- Crucially, the fix does **not** trade accuracy for faithfulness: the post-training reward sets **both task accuracy and parametric faithfulness** as signals, and CoT parametric faithfulness improves substantially while task accuracy is **maintained or improved**.
- Doubles as an auditing framework, which matters given the 2026-10-02 result (`2610.02015`) that RLVR permits unbounded CoT language drift while constraining drift necessarily constrains expected reward — CoT monitorability is a moving target by construction, so tooling that measures interpretability-alignment has to be re-validated rather than assumed.

---

### 52. RAIM: Robust Aggregation of Inexpensive Models for Hallucination Detection

- **arXiv:** [2609.39229](https://arxiv.org/abs/2609.39229) · submitted 2026-09-30 · primary category `cs.CL` · all categories: `cs.CL`, `cs.AI`, `cs.LG`
- **Authors:** Elia Onofri; Roberto Di Pietro
- **Institution / company:** Computer, Electrical and Mathematical Sciences and Engineering (CEMSE) Division, King Abdullah University of Science and Technology (KAUST), Thuwal 23955, Saudi Arabia
- **Affiliation evidence:** read from the paper's own institutional address block in the HTML front matter — the author block itself carries **no** affiliation markup, so the corresponding-author email domain was deliberately **not** used as evidence
- **Author comment:** 49 pages, 23 tables, 10 figures. Code and data released as two GitHub repositories (`raim-analysis`, `raim-verdicts`)

**Abstract.** Automatic evaluation of faithfulness increasingly relies on a large language model acting as a judge, yet the most reliable judges are proprietary frontier models, costly and ill-suited to high-throughput monitoring. We investigate whether a panel of cheap open-weight judges (4--9B) can be aggregated to stand in for a frontier one, what the substitution sacrifices, and when it is worth making. We propose RAIM, an aggregation scheme robust to the members' correlated errors, coupling a cross-fitted stacked logistic regression with an admissibility test that, read from the members' own outputs, identifies when aggregating them improves on their best member and stays within reach of the frontier judge. We instantiate RAIM with ten judges from disjoint families across eight faithfulness benchmarks. Against Claude Sonnet, the panel retains a median 93% of its Cohen's $κ$ and gives up only 2.9 points of balanced accuracy on average; read as paired differences, it clearly improves on one benchmark and clearly worsens on three (only two by a non-negligible margin), leaving four unresolved. At a sixty-fourth of the frontier's inference price, the operative expense is a one-time in-domain calibration on 50--100 labelled records. The panel is also competitive with purpose-trained detectors on their home benchmarks (within 1.3 accuracy points of GPT-4o and 1.9 of the LLM-AggreFact leader), and beats the strongest one we reran by 6 points on our grounded sets. Whether aggregation pays depends on the members themselves: where several capable members err on different items, the panel improves on its best judge and approaches the frontier; where one dominates, the stacker recovers the leader, and only there does the frontier remain materially ahead. Both conditions are read off the calibration set at no further cost, so a cheap panel can stand in for a frontier one wherever this audit admits it.

**Key innovations.**

- Asks the operational question directly: can a panel of **cheap open-weight judges (4–9B)** stand in for a proprietary frontier judge, what does the substitution cost, and when is it worth making?
- **RAIM** couples a **cross-fitted stacked logistic regression**, which handles the members' correlated errors, with an **admissibility test** read from the members' own outputs that flags when aggregating actually improves on the best single member.
- Headline result: against Claude Sonnet the panel retains a **median 93% of Cohen's κ** and gives up only **2.9 points** of balanced accuracy on average, at **one-sixty-fourth** of the frontier judge's inference price.
- The calibration is cheap and auditable: one-time in-domain calibration on **50–100 labelled records**, and *both* operating conditions — several capable members erring on different items, versus one member dominating — are read off that same set at no further cost.
- Competitive beyond mere substitution: within **1.3 accuracy points of GPT-4o** and **1.9 of the LLM-AggreFact leader** on their home benchmarks, and **6 points** above the strongest detector the authors reran on their grounded sets.
- Honest failure accounting, read as paired differences: clearly improves on one benchmark, clearly worsens on three (only two by a non-negligible margin), leaving four unresolved.

---

### 53. A Safe Prototype Is Not a Safety Direction: Reference Dependence and Prompt Confounds in Response-Safety Embeddings

- **arXiv:** [2610.01801](https://arxiv.org/abs/2610.01801) · submitted 2026-10-01 · primary category `cs.LG` · all categories: `cs.LG`, `cs.CL`, `cs.CR`
- **Authors:** Sahil Kadadekar
- **Institution / company:** New York University
- **Affiliation evidence:** verified from author block
- **Author comment:** **Accepted at the NeurIPS 2026 Workshop on Foundations of Language Model Security (FLMSec).** 15 pages, 3 figures, 11 tables. Code, results, and a verifier are in the ancillary files

**Abstract.** Can response safety be scored by cosine similarity to the mean embedding of known-safe responses? A recent sleeper-agent detector proposes exactly this score, yet the raw positive-centroid rule is not identified: positive observations locate the safe class relative to an encoder origin, but do not determine which direction separates safe from unsafe responses. We audit the rule on two prompt-controlled, human-labeled corpora and one auxiliary jury-labeled source control, using four frozen encoders and prompt-grouped splits. On the human-labeled corpora the safe prototype reaches ROC-AUC 0.457-0.545, with two cells significantly below chance and one above, while an explicit safe-minus-unsafe reference reaches 0.588-0.738 on the same embeddings; on the jury control the prototype is inverted (0.358-0.405) and the reference reaches 0.754-0.793. At validation-calibrated 5% false-safe thresholds, the reference accepts more safe responses on PKU-SafeRLHF (0.153-0.263 versus 0.039-0.061 across encoders) and Aegis (0.189-0.291 versus 0.004-0.045), but not reliably on BeaverTails. A fully unlabeled held-out reference recovers part to most of the referenced ranking, much less when only 5% of the pool is unsafe, whereas 80-634 labeled unsafe responses recover most of it. Prompt-only ablations show that prompt-label composition can inflate uncontrolled evaluations. A bounded result about a raw positive centroid, not all one-class methods or safety-specialized guards. A class mean is a location, not necessarily a safety direction; a declared reference with enough unsafe mass identifies orientation.

**Key innovations.**

- The statistical argument is the paper: the raw positive-centroid rule used by a recent **sleeper-agent detector** is **not identified**. Positive observations locate the safe class relative to an *encoder origin*, but that says nothing about **which direction separates safe from unsafe**.
- Audited properly — two prompt-controlled human-labeled corpora, one jury-labeled source control, **four frozen encoders, prompt-grouped splits** — the prototype scores ROC-AUC **0.457–0.545**, with **two cells significantly below chance** and one above, i.e. it can be *anti-correlated with safety*. On the jury control it is **inverted (0.358–0.405)**.
- The constructive fix is one line: an explicit **safe-minus-unsafe** reference reaches **0.588–0.738** on the same embeddings and **0.754–0.793** on the jury control.
- Operational stakes at a validation-calibrated 5% false-safe threshold: the reference accepts more safe responses on PKU-SafeRLHF (**0.153–0.263 vs 0.039–0.061**) and Aegis (**0.189–0.291 vs 0.004–0.045**), but *not* reliably on BeaverTails — so the fix is not uniform, and the paper says so.
- Cost of getting a reference is quantified: an unlabeled held-out reference recovers part-to-most of the ranking — **much less when only 5% of the pool is unsafe** — whereas **80–634 labeled unsafe responses recover most of it**. Prompt-only ablations further show prompt-label composition can inflate uncontrolled evaluations.
- Correctly bounded: this is a result about a **raw positive centroid**, not all one-class methods or safety-specialized guards. The closing line is the transferable one — *a class mean is a location, not necessarily a safety direction*.

---

### 54. Faithful Dual-constrained Erasure for Robust LLM Safety Alignment

- **arXiv:** [2609.39279](https://arxiv.org/abs/2609.39279) · submitted 2026-09-30 · primary category `cs.CR` · all categories: `cs.CR`, `cs.AI`
- **Authors:** Jiaqing Li; Shide Zhou; Zhibo Zhang; Yuxi Li; Tianlong Yu; Kailong Wang
- **Institution / company:** Huazhong University of Science and Technology; Hubei University
- **Affiliation evidence:** verified from author block — LaTeXML split "Huazhong University of" and "Science and Technology" into two consecutive affiliation spans; merged here

**Abstract.** Machine unlearning has emerged as a crucial mechanism for removing hazardous knowledge and enforcing safety alignment in Large Language Models (LLMs). However, recent studies reveal a persistent security risk: unlearned models remain highly vulnerable to retraining attacks, where suppressed malicious behaviors rapidly resurface after benign fine-tuning. In this work, we investigate the optimization dynamics of unlearning and identify that this vulnerability stems from shallow alignment. Rather than effectively erasing target knowledge, models often exploit a shortcut by activating previously dormant parameters to act as spurious suppressors, forming a fragile inhibitory shell over intact malicious representations. To address this issue and enforce authentic memory deletion, we propose FDCU, a novel dual-constrained subspace projection framework. FDCU restricts parameter updates through a highly scalable, element-wise dual-masking rule: it preserves general knowledge manifolds via Fisher Information and strictly prohibits the abnormal activation of spurious suppressors via the Principle of Minimal Functional Intervention (PMFI). By reliably blocking the model's ability to superficially hide knowledge, FDCU promotes the authentic dismantling of target representations. Extensive experiments across specific knowledge erasure and safe output control tasks demonstrate that FDCU achieves state-of-the-art robustness against retraining attacks while maintaining near-lossless general utility, ensuring durable safety for LLMs.

**Key innovations.**

- Names the security hole precisely: **unlearned models remain highly vulnerable to retraining attacks**, with suppressed malicious behavior resurfacing rapidly after benign fine-tuning.
- The diagnosis is mechanistic rather than empirical: the vulnerability stems from **shallow alignment**. Models activate previously dormant parameters to act as **spurious suppressors**, building a **fragile inhibitory shell over intact malicious representations**.
- **FDCU** (Faithful Dual-constrained Unlearning) enforces two constraints at once — preserving general knowledge manifolds via **Fisher Information**, and strictly prohibiting abnormal suppressor activation via the **Principle of Minimal Functional Intervention (PMFI)** — through a scalable element-wise dual-masking rule.
- The stated objective is **authentic dismantling**, not suppression: reliably blocking the shortcut is what forces the target representations to actually come apart instead of being hidden.
- Results are framed as robustness rather than raw utility — state-of-the-art resistance to retraining attacks at **near-lossless general utility**.

---

### 55. Cheap to Draw, Expensive to Trust: Certifying Test-Time Scaling Curves

- **arXiv:** [2609.40190](https://arxiv.org/abs/2609.40190) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`, `cs.CL`, `math.ST`, `stat.ML`
- **Authors:** Sohail (Neel) Sarkar; Shakuntala Baichoo
- **Institution / company:** PMCC AI Lab, Peter Munk Cardiac Centre, University Health Network (Toronto, Ontario, Canada)
- **Affiliation evidence:** verified from author block
- **Author comment:** 32 pages, 10 figures, 5 tables

**Abstract.** Sampling several answers and keeping the one a verifier scores highest is one of the simplest ways to buy accuracy at test time. Its effect is reported as a scaling curve: accuracy against the number k of sampled answers. The curve is cheap to draw and expensive to trust. A budget read off it is chosen after looking at every point, so only a band that covers all budgets at once protects the choice, and on a 100-question benchmark a fixed exact-binomial design needs 192,000 generated answers to certify 64 budgets to within ±1/32 at 95%. Most of that cost pays for the wrong uncertainty. A benchmark is a fixed list of questions; at budget 64, about three quarters of the variance of a selected answer's correctness lies between questions, and an audit that revisits every question need not pay for it. We derive the minimax cost of certifying the whole curve, up to logarithmic factors. It has three parts: calibrating the tail of the score distribution, telling the questions apart, and within-question noise summed along the curve. At a single benchmark the last part sharpens to the variance of one answer's influence under the best allocation of answers to questions, which every valid audit pays and an audit that learns the allocation attains, up to a logarithm, as the precision grows. A paired audit built on an exponential inequality for two independent draws at the same question needs no pilot. On 185 held-out score pools it uses 0.74 times the answers of the cheapest competing certified audit at 64 budgets and 0.53 times at 1,024, and on a newly generated MMLU-Pro study it certified the curve with 79,133 answers, within 0.6% of what a cost law fitted beforehand predicted from the study's within-question variance. The same paths certify pass@k and majority voting, and the bands extend to populations of questions and to answers that depend on earlier ones.

**Key innovations.**

- Correct premise for the whole field: a test-time scaling curve is **cheap to draw and expensive to trust**, because a budget read off it is chosen *after seeing every point* — so only a band covering all budgets simultaneously protects the decision.
- The price tag that motivates everything: on a 100-question benchmark, a fixed exact-binomial design needs **192,000 generated answers** to certify 64 budgets to within ±1/32 at 95%.
- The key diagnosis is *which* uncertainty matters: a benchmark is a fixed list of questions, so at budget 64 about **three quarters of the variance lies between questions** — and an audit that revisits every question is **paying for the wrong uncertainty**.
- Derives the **minimax cost of certifying the whole curve** (up to logarithmic factors), decomposing it into three parts: calibrating the tail of the score distribution, telling the questions apart, and within-question noise summed along the curve. At a single benchmark the last term sharpens to the variance of one answer's influence under the best allocation of answers to questions — which every valid audit pays and a learning allocation attains up to a log factor.
- Method is pilot-free: a **paired audit** built on an exponential inequality for two independent draws at the same question needs no pilot phase.
- Verified empirically: on **185 held-out score pools** it uses **0.74×** the answers of the cheapest competing certified audit at 64 budgets and **0.53×** at 1,024; on a fresh MMLU-Pro study it certified the curve with **79,133 answers, within 0.6%** of what a cost law fitted beforehand predicted. Same paths certify pass@k and majority voting, and bands extend to question populations and to answers dependent on earlier ones.

---

### 56. How Much Is an AI Token Worth? Scaling Laws for Wild AI-Generated Web Text

- **arXiv:** [2609.40295](https://arxiv.org/abs/2609.40295) · submitted 2026-09-30 · primary category `cs.CL` · all categories: `cs.CL`, `cs.LG`
- **Authors:** Jenna Russell; Ben Glickenhaus; Katherine Thai; John Wieting; Mohit Iyyer; Max Spero; Bradley Emi
- **Institution / company:** University of Maryland; Pangram Labs
- **Affiliation evidence:** verified from author block (first author marked equal contribution)

**Abstract.** Web text makes up the majority of pretraining data and is increasingly AI-generated. After applying FineWeb quality filtering, we find that 27.5% of tokens from June 2026 web data are labeled as AI-generated by Pangram, rising to 31.1% by August. Unlike synthetic data or model-collapse setups, this wild AI text comes from many models, is written for human readers, and arrives unlabeled in pretraining corpora. How does AI text in the wild affect language model pretraining? To answer this question, we pretrain 800 language models, varying the ratio of added AI tokens to human tokens, and fit scaling laws to held-out losses on both human and AI-generated text. For data-starved models, adding AI tokens to pretraining data initially lowers loss on human text, but the benefit saturates as more are added and quickly reverses into harm. For models trained on high budgets of human text, AI tokens raise loss almost immediately, while the same number of fresh human tokens keeps lowering it. Scaling laws such as Hoffman et al. (2022) fail to predict this behavior. We propose a new scaling law with separate benefit and harm terms that allows the value of an AI token to change sign while also reducing to Chinchilla in the absence of AI text. When fit on smaller models, our scaling law predicts the effect of AI text on held-out human-text loss for models up to 3.6x larger with 41% lower error than the best existing law over all AI ratios. We recommend filtering AI text when the target is human text, repeating human text before expanding the training dataset with AI-generated web text, and reporting validation loss on human and AI text separately — AI text remains valuable when the target is AI text. We release WildAI, an 83B-token corpus with AI, topic, and format labels, all 800 models and code.

**Key innovations.**

- Establishes the measurement first, after FineWeb quality filtering: **27.5% of tokens in June 2026 web data are labeled AI-generated, rising to 31.1% by August**. This is *wild* AI text — many models, written for human readers, arriving unlabeled — not synthetic data or a model-collapse setup.
- Empirical scale is unusual: **800 pretrained language models** varying the AI-to-human token ratio, with scaling laws fit to held-out loss on **both** human and AI text.
- The finding is a **sign change in token value**. For data-starved models, adding AI tokens initially lowers human-text loss, but the benefit **saturates and then reverses into harm**. For models already trained on high budgets of human text, AI tokens **raise loss almost immediately**, while the same number of fresh human tokens keeps lowering it.
- **Hoffman et al. (2022) fails to predict this**, and the proposed replacement has the right algebraic structure: separate **benefit and harm** terms, allowing an AI token's value to change sign, while **reducing to Chinchilla** when no AI text is present.
- Predictive validation: fit on smaller models, the new law predicts AI-text effects on held-out human-text loss for models up to **3.6× larger with 41% lower error** than the best existing law, across all AI ratios.
- Actionable recommendations, including the conditional one people will skip: filter AI text when the target is human text, **repeat human text before expanding with AI web text**, and report validation loss on human and AI text **separately** — because **AI text remains valuable when the target is AI text**.
- Releases **WildAI**, an 83B-token labeled corpus, plus all 800 models and code.

---

### 57. How Much Can Language Models Gain from Test-Time Computation?

- **arXiv:** [2610.01110](https://arxiv.org/abs/2610.01110) · submitted 2026-10-01 · primary category `cs.LG` · all categories: `cs.LG`
- **Authors:** Bangji Yang; Jingyuan Li; Jiajun Fan; Yi Evie Zhang; Ruihan Guo; Hongba Ma; Neil He; Chumeng Liang; Qinglong Zheng; Zhanghan Ni; Ge Liu
- **Institution / company:** ⚠️ **not stated.** The HTML author block renders three bare `Affiliation:` labels with empty institution text; the only contact rendered is `geliu@illinois.edu`. **Not inferred from the email domain.**
- **Affiliation evidence:** affiliation labels present but empty

**Abstract.** How much can test-time computation improve a language model, and at what cost? Test-time scaling is widely proposed as a substitute for larger models, but existing comparisons mostly evaluate one domain at a time and rarely charge selection to the budget. We introduce Self-POT, a benchmark and evaluation framework that measures the test-time potential of a model across competition mathematics, competitive programming, and agentic workflows. Self-POT separates candidate coverage from final accuracy on static tasks, tracks correctness transitions under revision, and measures protocol completion alongside task success in agentic environments. Under a unified budget rule, it compares Direct inference with parallel sampling and self-revision under fixed multiples of the Direct budget, and charges every model call, including selection and critique, in dollars. This design supports two kinds of comparison: the gain a model obtains from additional inference, and a lower-cost model with additional inference against a stronger model. Across five low-cost reasoning models on 350 sealed tasks, with Claude Opus 5.5 Direct as the reference, the returns depend on the domain, the selection rule, and failure handling. When we replay the retained programming candidate pools, public-example selection raises correct submissions from 376 to 453 of 500 scheduled cells while saving 12-49% of logical API cost across models, and simply retaining an available candidate when judging fails recovers 61 submissions at unchanged cost. On identical mathematics pools, judging with fallback yields 186 correct submissions versus 182 for voting, while voting saves 12-21% of logical API cost. These controlled replays show how selection and failure handling change the gains realized from the same generated candidates, and they quantify the marginal value of a model judge.

**Key innovations.**

- Targets a specific accounting failure in the test-time-scaling literature: comparisons "mostly evaluate one domain at a time and **rarely charge selection to the budget**". **Self-POT** charges *every* model call — **including selection and critique** — in dollars, under a unified budget rule across competition mathematics, competitive programming and agentic workflows.
- The framework separates quantities normally conflated: **candidate coverage vs. final accuracy** on static tasks, **correctness transitions under revision**, and in agentic environments **protocol completion alongside task success**.
- The design supports the comparison people actually care about — a cheaper model with more inference versus a stronger model — with five low-cost reasoning models on **350 sealed tasks** against Claude Opus 5.5 Direct as reference.
- The controlled-replay design is the methodological strength: rather than comparing systems, it **replays the same retained candidate pools** and varies only the selection rule and failure handling — so differences are attributable.
- Numbers that make the point: on programming pools, public-example selection raises correct submissions **376 → 453 of 500 scheduled cells** while **saving 12–49% of logical API cost**, and simply **retaining an available candidate when judging fails recovers 61 submissions at unchanged cost**. On identical math pools, judging-with-fallback yields **186 vs. 182** correct submissions for voting, while voting saves **12–21%**.
- Conclusion is appropriately deflationary about a hot topic: returns **depend on the domain, the selection rule, and failure handling**, and the paper quantifies the **marginal value of a model judge** rather than assuming it.

---

### 58. Chaining Skills to Hijack LLM Agents

- **arXiv:** [2610.01564](https://arxiv.org/abs/2610.01564) · submitted 2026-10-01 · primary category `cs.CR` · all categories: `cs.CR`, `cs.AI`
- **Authors:** Tian Dong; Zixuan Ma; Haodong Zhao; Huaien Zhang; Shaofeng Li; Hao Chen
- **Institution / company:** The University of Hong Kong; Shandong University; Shanghai Jiao Tong University; Southeast University
- **Affiliation evidence:** verified from author block (first and sixth authors marked equal contribution)

**Abstract.** LLM agents use skills to improve performance on specialized tasks. To complete a user request, an agent may invoke several skills in sequence, allowing information produced under one skill to guide the next. Because skills may come from open-source repositories, this handoff can also carry attacker-controlled claims into later decisions. In this paper, we introduce APEX, which constructs and refines adversarial skill chains tailored to a user task and an attacker-selected action. The key insight is that an agent-written record of genuine task progress can carry a false claim of user approval across skills: an upstream skill induces the agent to create the record, and a downstream skill uses it to direct the attacker-selected action. Across four targeted-action families and six models on SkillsBench, the chains induce the selected action in 512 of 690 attempts (74.2%). On GPT-5.4, the full chain succeeds in 84.3% of attempts, compared with 17.4% when the workflow is merged into one skill. We further evaluate a prompting defense that asks the agent to check skill-produced files against the original request. On GPT-5.4, it lowers targeted-action success from 84.3% to 59.1%, while the verifier test-pass rate across 72 benign native-skill tasks falls from 86.7% to 56.3%.

**Key innovations.**

- Identifies a genuinely new attack surface created by the **skill** pattern: because skills come from open-source repositories and run **in sequence**, information produced under one skill can carry attacker-controlled claims into later decisions. The trust boundary is *between skills*, not just at the model.
- The mechanism is subtle and well-chosen: an **agent-written record of genuine task progress** can carry a **false claim of user approval** across skills — an upstream skill induces the agent to write the record, a downstream skill reads it as authorization. Nothing is forged; the agent is misled by its own honest artifact.
- **APEX** constructs and refines adversarial skill chains tailored to both a user task and an attacker-selected action; across four targeted-action families and six models on SkillsBench the chains induce the selected action in **512 of 690 attempts (74.2%)**.
- Quantifies the compositional factor: on GPT-5.4 the full chain succeeds **84.3%** of attempts versus **17.4%** when the workflow is merged into a single skill — i.e. the multi-skill handoff, not the malicious content, is what carries the attack.
- The defense section is the most useful part for practitioners, because it prices the tradeoff: prompting the agent to check skill-produced files against the original request lowers targeted-action success **84.3% → 59.1%**, but drops verifier test-pass rate on 72 benign native-skill tasks from **86.7% → 56.3%**. Security here is not free, and the numbers say by how much.

---

### 59. When Reasoning Goes Astray: Attention Dynamics of Uncontrolled Reasoning

- **arXiv:** [2609.38817](https://arxiv.org/abs/2609.38817) · submitted 2026-09-30 · primary category `cs.AI` · all categories: `cs.AI`, `cs.CL`
- **Authors:** Yuanhe Zhang; Ziwei Wang; Jie Ren; Haoran Gao; Zhenhong Zhou; Fanyu Meng; Cong Wu; Li Sun; Sen Su
- **Institution / company:** Beijing University of Posts and Telecommunications; Wuhan University; JIUTIAN Research; Nanyang Technological University; Chongqing University of Posts and Telecommunications
- **Affiliation evidence:** verified from author block

**Abstract.** Large reasoning models (LRMs) improve performance on complex tasks through extended reasoning, yet the same process can degenerate into redundant verification and persistent generation loops. Such uncontrolled reasoning increases inference cost and creates risks of resource exhaustion and service degradation. However, existing mitigations largely truncate long outputs or react to surface repetition, and thus fail to distinguish normal thinking from uncontrolled reasoning or explain how benign reasoning degenerates into harmful behavior. In this paper, we operationalize LRM generation as four states and further introduce Reasoning-state Analysis via Dynamic Attention Responses (RADAR), which identifies the current reasoning state in real time and characterizes how effective reflection can develop into uncontrolled generation. Guided by RADAR's analysis, we further realign abnormal attention distributions toward patterns observed in normal requests and examine how this correction affects excessive reflection and persistent looping. Temporal analyses show that uncontrolled reasoning is characterized by attention distributions that deviate from normal generation, with abnormal trends becoming detectable **before repetition begins**. Correcting these deviations through Attention Realignment consistently reduces looping while largely preserving benign performance.

**Key innovations.**

- Critiques current mitigations on a correctness ground, not just an effectiveness one: truncating long outputs or reacting to surface repetition **cannot distinguish normal thinking from uncontrolled reasoning**, and cannot explain how benign reasoning degenerates.
- **RADAR** operationalizes LRM generation as **four states** and identifies the current reasoning state **in real time** from dynamic attention responses — so the unit of detection is the reasoning *state*, not the repetition *surface*.
- The timing claim is what makes it operationally useful: abnormal attention-distribution trends become **detectable before repetition begins**, giving a window to intervene rather than a post-hoc symptom to clean up.
- The intervention follows from the diagnosis: **Attention Realignment** pulls abnormal attention distributions back toward patterns observed in normal requests, which **consistently reduces looping while largely preserving benign performance** — i.e. it does not blunt reasoning to stop degeneration.
- Read against §1 and §3, this closes a loop. §1 (`2609.39118`) shows on-policy self-distillation's teacher signal is shaped by **reasoning-mode alignment and the complete teacher prefix**, so it is unstable exactly when reasoning mode drifts; §3 (`2609.39687`) shows a *diverse pool* of perturbed teachers repairs much of that instability; and this entry supplies the mechanism that would break it — detection of the reasoning state in real time from attention dynamics. The monitoring problem is therefore real, mechanistic, and upstream of both post-training methods. (The complementary paper that *proves* RLVR permits unbounded CoT language drift was already covered on 2026-10-02 as `2610.02015`.)

---

## Vacancies, Negative Windows & Coverage Accounting (recorded, not padded)

These are deliberate records of what is **absent**, kept so a later reader can tell a thin section from an unsearched one.

1. **There is no new arXiv submission block.** 2026-10-04 is a Sunday. `cs.LG` queries with `submittedDate` ending 2026-10-02 / 10-03 / 10-04 all return the identical `totalResults=1602`, and the newest indexed submission date remains **2026-10-01**. This report therefore re-sweeps the same 09-30 → 10-01 block the 2026-10-03 sibling covered, but across **14 categories instead of 6**, which is how it still found 1,030 unclaimed candidates. **No 10-02/10-03/10-04 papers exist to report.**

2. **Advertising, bidding and CTR prediction: zero papers.** Across 1,030 unclaimed candidates there is no CTR-prediction paper, no auction/bidding paper, and no ad-ranking paper. The nearest neighbors left after deduplication are (a) biomedical **reranking** for retrieval-grounded QA (`2610.01324`, §41) and (b) personalization *encoder* repair (`2610.01270`, §42) — both retrieval/ranking problems, neither a CTR task. The genuinely closest paper in this block, Meta's fleet-scale recommendation *training-infrastructure* study (`2610.02057`), had already been written up on 2026-10-02 and was removed here under the dedup rule. **This is the third consecutive arxiv-daily window in which advertising/CTR is an explicit vacancy**, consistent with the 10-03 sibling's recorded finding. Any CTR claim made from this window would be inference, not reporting.

3. **Games and RL environments: near-empty.** The `games` regex bucket over the unclaimed pool returns 30 hits, of which nearly all are *game-theoretic* or *market* papers (stochastic games, congestion pricing, Stackelberg alignment, quant trading) rather than game-playing or RL-environment work. The 2026-10-03 `game-rl-daily.md` sibling already recorded a single genuine unclaimed game paper in this same block, so the supply in the `2610.0xxxx` range is genuinely thin rather than mis-mined here. §7 contains three entries; one of them (Turinici, `2610.00613`) is a grid-world agent paper that only partly qualifies.

4. **Sequential modeling: one paper, and it is a compression paper.** The only entry that matches "sequential" in the modeling sense is `2610.00717` (Structured Tucker compression of LLM attentions, §25) — *sequential* in the compression-procedure sense, not the user-behavior sense. `2609.38805` (§9) evaluates on ALFWorld and Sokoban but is an RL-diversity paper. Genuine sequential user-behavior modeling is **absent from this window**.

5. **Search reliability note.** All arXiv access this run went through `https://export.arxiv.org/api/query` with `-L`. Plain `http://` returns **HTTP 301** with a zero-byte body — a silent-failure trap for any script that does not follow redirects and does not check the status code. A prior sibling run recorded **HTTP 429 `Rate exceeded`** for this account tier, so requests here were paced at ~4 s with ≤6-way concurrency; no 429 was hit.

6. **Thirteen of the 59 affiliation records could not be resolved and were left unresolved.** Grouped by cause: **bare `Affiliation:` labels with the institution text dropped** — `2610.01161` (§11, nine labels), `2610.01352` (§29, four), `2610.01110` (§57, three), `2610.00619` (§49, three), `2609.39740` (§16, two); **no affiliation markup at all** — `2609.39578` (§18), `2610.01270` (§42); **numeric superscripts with no institution text** — `2609.38948` (§35); **a collective team name only** — `2610.02054` (§36, "UniWAM Team"); **no author block in the HTML at all** — `2610.00949` (§13, where PDF text extraction also surfaced no institution string); **no arXiv HTML rendition** — `2610.00872` (§14), `2609.39687` (§3), `2610.01324` (§41). Several of these expose suggestive author email domains — `alibaba-inc.com`, `pjlab.org.cn`, `illinois.edu`, `umontreal.ca` — and **none were used**. The single instructive near-miss is `2609.39229` (§52, RAIM): its author block carries no affiliation markup and the corresponding author's address is `elia.onofri@kaust.edu.sa`, so the domain *alone* would have been an inference — but the paper prints a full **CEMSE Division, King Abdullah University of Science and Technology** address in its front matter, which is the authors stating it outright, so the entry is filled and labelled accordingly. Per-paper `Affiliation evidence` lines record which of these sources was used.

7. **Dedup baselines must be rebuilt from the tree, not carried forward between runs.** The first-pass claimed-ID list for this report was stale and under-counted by 69 IDs, which let 8 already-published papers into the draft. The failure mode is quiet: a stale baseline produces papers that *look* novel, and nothing downstream fails. The check that catches it is cheap and should be mandatory on every daily run — enumerate `wiki/` for every `\d{4}\.\d{4,5}` token, exclude the file being written, and assert the intersection with the new set is empty before declaring a section final.

8. **Pre-registration and self-limiting results are rare but present, and worth seeking out.** Three papers here volunteer evidence against their own strongest reading: `2609.39634` (§50) states its correction is "null to harmful" when held throughout or applied where clipping already contains the bias; `2610.00694` (§24) runs **two pre-registered tests** to mark the limits of its own law; `2609.40190` (§55) validates its cost model against a prediction fitted *before* the study (within 0.6%). These are the entries most worth trusting on the specific numbers.

---

## Cross-Cutting Observations

**1. Post-training is fragmenting into credit-assignment micro-methods, and four of today's papers attack the same GRPO weakness from different directions.** `2610.00838` (SHARPO) reweights the GRPO advantage per *segment* using teacher–student log-prob gaps; `2610.00388` (T2SPO) derives step credit from a TabPFN regressor over past successful trajectories; `2610.01161` (FAULT) converts self-diagnoses into step credit anchored by terminal outcomes; `2609.39402` (PEPO) replaces globally-computed token entropy with a local, provably confound-invariant *proximal* entropy. All four keep GRPO and change only how credit is distributed inside the group. That is a meaningful signal about where the field's effort is going — and a caution that these gains may not compose.

**2. The strongest theme is that measurement artifacts are now the primary finding, not methods.** `2609.38847` shows rubric criteria *compensating for each other* under a weighted sum so a policy scores higher and answers worse; `2609.39229` shows a cheap 4–9B judge panel retaining a median 93% of a frontier judge's Cohen's κ while being unable to say *when* it is safe to substitute — an audit problem, not just an accuracy problem; `2610.01670` shows candidate-order swaps reversing **60.9%** of MLLM pairwise decisions against each judge's own noise floor; `2609.40190` shows test-time scaling curves chosen after seeing every point; `2610.01801` shows a published sleeper-agent detector scoring *below chance* because a class mean is a location, not a direction. Four separate papers needed **noise floors, pre-registration, or a between-versus-within variance decomposition** to reach defensible conclusions.

**3. Two papers prove that a desirable property is unobtainable for free — and say so.** `2609.39118` shows on-policy self-distillation helps **only in narrow compatibility regimes**, degenerating otherwise into ineffective length growth, stable degradation, or outright collapse — so "privileged supervision improves reasoning" does not survive its own diagnostics. `2610.00661` proves the practical corollary for GRPO on diffusion LMs: MSE's reconstruction-loss *scale* varies across quantization stages, converting into uneven gradients and uneven optimization strength, so RMSE variants effectively act as implicit gradient normalization. Both replace "here is a better method" with "here is the shape of the constraint."

**4. Serving work is converging on measured, deployed numbers rather than kernel microbenchmarks.** `2609.40316` validates looped-MoE scaling at **trillion-token scale**; `2610.01439` (DRelay) reports speedups under **SGLang serving**; `2610.00499` measures in **real-world serving** with a CPU-only predictor to avoid GPU contention; `2610.01265` (RapidMoE) is **EuroSys 2027**; `2610.01324` reports its retrieval gains end-to-end inside a locally deployed RAG pipeline rather than on an offline index. Kernel-only claims are increasingly expected to come with a serving number attached.

**5. Agent *oversight* is being treated as a measurable capability, distinct from task performance.** `2609.39578` (Box²-Bench) measures whether a model can *override* unreliable guidance, training on bad workflows and evaluating on good ones; `2610.00601` separates **correctability** from **actionability** in CoT-steered VLA policies and finds reasoning correctness improving while closed-loop task performance does not; `2610.01787` shows which *components* of experience belong in weights versus context, predicting a held-out backbone's answer in 24 of 24 cells; `2609.39740` trains a model to choose among THINK / RECALL / EXIT. All four treat "how well does the agent use what it is given" as its own axis.

**6. Deliberate under-claiming is a marker of quality in this batch.** `2609.39634` states its own correction is null-to-harmful outside a narrow regime; `2610.01801` bounds itself to "a raw positive centroid, not all one-class methods"; `2610.00601` reports a large reasoning gain alongside flat task performance; `2610.01270` reports that head-only finetuning also helps, just 20× less; `2610.00949` states its method costs target-task performance. Contrast `2609.38847`, where the authors ran the control that could have exonerated their criticism and reported that the criteria were innocent.

**7. For CTR/advertising readers specifically: nothing here is usable as evidence.** The two closest papers (§41 biomedical reranking, §42 REPAIR) are respectively a cross-encoder reranking study in clinical QA and a personalization-encoder post-compression repair. `2610.00964` (§43) is the only paper touching product selection, and it is *in-context catalog search over long-context LLMs for small merchants*, which is a different problem from CTR prediction on impression logs. The three digests most likely to contain actual CTR work are `wiki/synthesis/ctr-scaling-landscape.md` and the ads/recsys sections of the 2026-09-* daily files.
