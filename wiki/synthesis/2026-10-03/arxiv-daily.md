---
title: arXiv Daily 2026-10-03 — AI / LLM / Recommendation / Ads / Sequential / CTR / Games
type: synthesis
created: 2026-10-03
updated: 2026-10-03
sources: [arxiv-api]  
tags: [arxiv, arxiv-daily, llm, post-training, agents, inference, recsys, ctr, advertising, sequential-modeling, rl, games, multimodal, evaluation]
---

# arXiv Daily — AI / LLM / Recommendation / Ads / Sequential Modeling / CTR / Games (2026-10-03)

**Window.** arXiv submissions dated **2026-09-18 → 2026-10-01**, dominated by the 2610.01xxx–2610.02xxx block (submitted 2026-10-01). 2026-10-03 is a Saturday and the API's newest indexed submission date is 2026-10-01, so this window is the latest batch arXiv is serving; there is no 10-02/10-03 submission block yet.

**Contents.** 47 papers in 8 sections. Every entry carries title, authors, institution, abstract, key innovations and an arXiv link, as requested.

**Dedup.** All entries were checked against every arXiv ID already mentioned anywhere under `wiki/` before selection (6,285 unique IDs claimed at run time; the pool contributed 1,886 candidate records of which 1,444 were unclaimed). No paper below had been written up previously.

---

## LLM Post-Training, Preference Optimization & Alignment Theory (7)

### 1. Sharpening Tax in Post-Training

- **arXiv:** [2610.01509](https://arxiv.org/abs/2610.01509) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`, `cs.LG`
- **Authors:** Changdae Oh; Qi Zeng; Qi Qi; Andrey Zhmoginov; Deren Lei; Yun He; Hoang Phan; Hangoo Kang; Azalia Mirhoseini; Sharon Li
- **Institution / company:** Meta Superintelligence Labs; University of Wisconsin–Madison; NYU; Stanford University
- **Affiliation evidence:** verified from author block (`ltx_contact ltx_role_affiliation`)

**Abstract.** An emerging hypothesis about reinforcement learning (RL) post-training of large language models (LLMs) is that it merely sharpens existing behaviors of a base model, improving single-shot accuracy at the cost of solution coverage. Although this trade-off has been observed in math and coding tasks, it need not extend to agentic tasks, where multi-turn tool use and interaction may require capabilities newly acquired during post-training. Our surprising finding is that pre-trained LLMs, equipped with a light inference harness, can serve as capable agents. Despite far lower accuracy (pass@1), they often surpass their post-trained counterparts in solution coverage (pass@K) given a sufficient test-time budget. We further analyze the underlying mechanism and show that post-training pushes tasks toward two extremes, always solved or never solved, and thereby improves sampling efficiency and consistency at the cost of solution coverage. To measure this cost, we propose Sharpening Tax, a diagnostic metric that quantifies the loss in test-time scalability after post-training. Across 14 base/post-trained model pairs from four families and three agentic benchmarks (42 cases in total), the tax is prevalent in most settings, can be estimated from a few rollouts, and correlates well with other metrics. Finally, we present posterior-tempered group sampling (PTGS), a simple plug-and-play Bayesian sampler that adapts the sampling temperature per prompt to its estimated difficulty. Applied during RL training in two agentic environments, PTGS pays a smaller tax than the fixed-temperature baseline, solving more tasks under repeated sampling while also improving single-shot accuracy.

**Key innovations.**

- Reframes RL post-training as a question about **coverage**, not accuracy: base LLMs given a light inference harness beat their post-trained counterparts on pass@K despite far lower pass@1.
- Mechanism claim: post-training pushes tasks toward two extremes — always solved or never solved — buying sampling efficiency and consistency at the cost of solution coverage.
- Introduces **Sharpening Tax**, a diagnostic for lost test-time scalability that can be estimated from a few rollouts; measured over 14 base/post-trained pairs from four families across three agentic benchmarks (42 cases).
- **PTGS** (posterior-tempered group sampling) sets temperature per prompt from estimated difficulty; it pays a smaller tax than fixed temperature in two agentic environments while also improving single-shot accuracy.

---

### 2. GAW-PO: Preference Optimization with Gradient-Aligned Token Weights

- **arXiv:** [2610.01511](https://arxiv.org/abs/2610.01511) · submitted 2026-10-01 · primary category `cs.CL` · all categories: `cs.CL`
- **Authors:** Andreea Dutulescu; Stefan Ruseti; Mihai Masala; Traian Rebedea; Mihai Dascalu
- **Institution / company:** National University of Science and Technology POLITEHNICA Bucharest; NVIDIA
- **Affiliation evidence:** verified from author block

**Abstract.** Most preference optimization methods, such as Direct Preference Optimization (DPO), apply preference supervision at the response level, although autoregressive language models are optimized token by token. As a result, all tokens in a rejected response contribute to the negative training signal, including tokens that may encode behavior that is useful for the preferred response. We introduce GAW-PO, a gradient-aligned token reweighting method for DPO that estimates, for each rejected token, whether penalizing it would interfere with the preferred update directions. Tokens whose gradients are strongly aligned with the preferred behavior receive a weaker negative contribution, while conflicting tokens retain a stronger penalty. Our method achieves the highest average performance among the evaluated preference-optimization methods, improving by 0.97 points over standard DPO and 0.65 points over the strongest competing baseline across 11 benchmarks spanning mathematics, reasoning, coding, and question answering. We further show that gradient-aligned weighting is substantially more robust to aggressive preference optimization: as the DPO regularization parameter $β$ decreases, standard DPO degrades sharply, whereas GAW-PO continues to improve. These results suggest that accounting for the interaction between rejected-token updates and preferred behavior provides an effective form of token-level credit assignment for preference optimization.

**Key innovations.**

- Names a concrete defect of DPO: response-level supervision drives *every* token of a rejected sample down, including tokens whose updates would interfere with the preferred behavior.
- Gradient-aligned token reweighting estimates, per rejected token, whether penalizing it would conflict with the preferred update direction; aligned tokens receive a weaker negative contribution, conflicting tokens keep a strong penalty.
- +0.97 over standard DPO and +0.65 over the strongest competing baseline, averaged over 11 benchmarks spanning math, reasoning, coding and QA.
- Robustness result matters as much as the average: as DPO's β falls (aggressive optimization) standard DPO degrades sharply while GAW-PO keeps improving.

---

### 3. The Weakest Link: Distilling LLM Reasoning with Worst-Case Constrained Reinforcement Learning

- **arXiv:** [2610.00332](https://arxiv.org/abs/2610.00332) · submitted 2026-09-29 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`
- **Authors:** Matthieu Zimmer; Xiaotong Ji; Tu Nguyen; Haitham Bou-Ammar
- **Institution / company:** Huawei Noah's Ark Lab; Huawei Heisenberg Research Center; UCL Centre for AI
- **Affiliation evidence:** verified from author block

**Abstract.** Distilling the reasoning capabilities of large language models (LLMs) into smaller students is a central challenge for efficient deployment. Current approaches face a fundamental tension: optimizing purely for verifiable task rewards (e.g., via GRPO) leads to reward hacking, where students arrive at correct final answers through flawed intermediate logic, while regularizing with soft divergence penalties against a teacher (e.g., KL-based distillation) dilutes task performance and, critically, allows the student to compensate for severe logical violations at one step with high teacher agreement at others. We argue that this averaging is fundamentally misaligned with the nature of reasoning: a chain-of-thought is only as valid as its weakest link. Motivated by this observation, we formulate reasoning distillation as a constrained reinforcement learning problem in which the task reward is maximized subject to a worst-case constraint on the teacher log-likelihood along every prefix of the trajectory. To avoid the prohibitive cost of dual Lagrangian solvers and the test-time teacher dependence of state-augmented methods such as Saute, we derive an unaugmented constrained MDP whose reward transformation preserves the hard-constraint semantics, admits a low-variance policy gradient decomposition into single-step and long-term terms, and provably satisfies the worst-case constraint almost surely in the penalty limit. Through extensive experiments on mathematical reasoning and code generation tasks, we demonstrate that our method significantly expands the accuracy-fidelity Pareto front. By matching the high Final Answer Correctness of pure RL and drastically reducing teacher constraint violations, we ultimately achieve the highest rigorous Reasoning Success Rate across all evaluated settings.

**Key innovations.**

- Argues KL-to-teacher distillation is structurally misaligned with reasoning: per-step teacher agreement *averages*, so a student can buy high agreement at other steps to cover one severe logical violation.
- Formalizes reasoning distillation as constrained RL — maximize task reward subject to a **worst-case** bound on teacher log-likelihood along *every prefix* of the trajectory, on the premise that a chain-of-thought is only as valid as its weakest link.
- Derives an unaugmented constrained MDP that avoids both the dual-Lagrangian solver cost and the test-time teacher dependence of Saute-style state augmentation, admits a low-variance gradient split into single-step and long-term terms, and satisfies the worst-case constraint almost surely in the penalty limit.
- Reports an accuracy–fidelity Pareto front rather than a single score, explicitly penalizing right-answer-wrong-logic; reaches the highest rigorous Reasoning Success Rate across all evaluated settings.

---

### 4. Function-Structured Reinforcement Learning with Executable Verifiers for Mathematical Reasoning

- **arXiv:** [2610.01729](https://arxiv.org/abs/2610.01729) · submitted 2026-10-01 · primary category `cs.LG` · all categories: `cs.LG`
- **Authors:** Zihan Liu; Xurong Xie
- **Institution / company:** _(not stated — author block contains no affiliation)_
- **Affiliation evidence:** author block renders only a corresponding-author note; OpenAlex has no record. Not inferred.
- **Author comment:** 5 pages, 2 figures, 2 tables

**Abstract.** Algorithmic mathematical reasoning requires reliable decomposition, computation, and aggregation. Final-answer rewards provide limited guidance on intermediate errors, while successful execution does not guarantee mathematical correctness. This work proposes Function-Structured Graph Reinforcement Learning (FSG-RL), connecting subproblem graphs and Python implementations with multi-verifier feedback. The policy first learns to generate code from function graphs through supervised fine-tuning (SFT). Group Relative Policy Optimization (GRPO) then optimizes the policy using answer-gated rewards and span-level credit assignment. The framework also supports teacher supervision and structured memory. A benchmark curated from Grade School Math 8K (GSM8K), MathQA, MATH, and Omni-MATH pairs public function graphs with private verification specifications. Under a unified evaluation protocol, GRPO improves final-answer accuracy from 43.25% to 67.50% and full solution success from 32.25% to 52.25% over SFT. Continued reinforcement learning (RL) with teacher supervision yields additional gains. The gains extend beyond producing correctly formatted code, supporting verifier-guided reinforcement learning for mathematical reasoning. Code is available at https://github.com/ZihanLiummyycc/FSG-RL.

**Key innovations.**

- Makes the decomposition itself the learning target: subproblem **function graphs** connected to Python implementations, so intermediate errors become checkable instead of only the final answer.
- Multi-verifier feedback with answer-gated rewards and **span-level credit assignment** on top of GRPO; SFT first teaches code generation from function graphs.
- GRPO over SFT lifts final-answer accuracy 43.25% → 67.50% and full-solution success 32.25% → 52.25%; continued RL with teacher supervision adds further gains.
- Ships a benchmark built from GSM8K, MathQA, MATH and Omni-MATH that pairs **public** function graphs with **private** verification specifications — separating 'can plan the decomposition' from 'can pass a hidden checker'.

---

### 5. Cross-Benchmark Transfer from RL on Agentic Coding Tasks

- **arXiv:** [2610.00890](https://arxiv.org/abs/2610.00890) · submitted 2026-10-01 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`, `cs.SE`
- **Authors:** Sushant Mehta; Logan Ritchie; Edwin Chen
- **Institution / company:** Surge AI
- **Affiliation evidence:** verified from author block
- **Author comment:** 15 pages, 2 figures, 4 tables

**Abstract.** Coding agents often fail in the last mile: they build most of a feature but drop a requirement, test only the cases their implementation already handles, break behavior that was supposed to stay intact, or validate against an unchecked assumption. We ask whether reinforcement learning (RL) on expert-built agentic coding tasks closes this gap, and whether what the agent learns transfers beyond the training distribution. We post-train Kimi K2.7 Code, a 1T-parameter (32B active) open-weight mixture-of-experts model, with RL alone on 1,700 tasks: 1,000 repository tasks graded by hidden fail-to-pass tests and by pass-to-pass tests of existing behavior, and 700 terminal tasks graded by expert-written hidden verifiers. The reward is the fraction of target checks passed and drops to zero if any pass-to-pass test fails. One epoch of GSPO on a rank-32 LoRA adapter improves pass@1 on each of the six external benchmarks we evaluated, across three agent harnesses: SWE-Bench Pro (60.1 to 64.8), DeepSWE (31.0 to 43.4), Terminal-Bench 2.1 (67.4 to 82.0), Terminal-Bench 3 (1.4 to 12.1), Terminal-Bench 4 (0.0 to 7.6), and SWE-Marathon (5.0 to 25.0). Pooled over the five independent task sets (Terminal-Bench 4 revises Terminal-Bench 3), the improvement is significant (p < 0.001), and it remains significant on the three sets released after the training data was collected (p = 0.004); the model also improves under both harnesses never used in training. Median trajectories on DeepSWE and Terminal-Bench 3 are 24-35% shorter in agent steps. The base model's failed DeepSWE runs are mostly near-misses, and on the tasks the trained model newly solves, paired trajectories show it avoiding each of the four failure modes above.

**Key innovations.**

- Post-trains a 1T-parameter / 32B-active open-weight MoE (Kimi K2.7 Code) with **RL only** — no SFT distillation — on 1,700 expert-built agentic coding tasks (1,000 repo tasks graded by hidden fail-to-pass *and* pass-to-pass tests, 700 terminal tasks graded by expert-written hidden verifiers).
- Regression-protection is built into the reward: fraction of target checks passed, forced to zero if any pass-to-pass test fails.
- One epoch of GSPO on a rank-32 LoRA adapter improves pass@1 on **all six** external benchmarks across three harnesses — SWE-Bench Pro 60.1→64.8, DeepSWE 31.0→43.4, Terminal-Bench 2.1 67.4→82.0, TB 3 1.4→12.1, TB 4 0.0→7.6, SWE-Marathon 5.0→25.0.
- Transfer is stress-tested rather than asserted: gains stay significant on the three task sets released *after* training data collection (p = 0.004) and under harnesses never used in training; median trajectories shorten 24–35% and paired analysis attributes gains to removing four named last-mile failure modes, not to taking more steps.

---

### 6. Where the Model Changes Its Mind: Hindsight-Divergence Localization for Efficient Reinforcement Learning with Verifiable Rewards

- **arXiv:** [2609.36864](https://arxiv.org/abs/2609.36864) · submitted 2026-09-29 · primary category `cs.LG` · all categories: `cs.LG`
- **Authors:** Fanchao Chen; Hengyu Fu; Shivaram Venkataraman; Jiantao Jiao
- **Institution / company:** University of Wisconsin–Madison; University of California, Berkeley; ETH Zurich; NVIDIA
- **Affiliation evidence:** verified from author block

**Abstract.** Group-relative methods for reinforcement learning with verifiable rewards (RLVR) learn from differences in rollout outcomes. Independently sampling complete trajectories is costly and does not explicitly explore the decision space at critical positions. Feedback on a completed trajectory can reveal which earlier choices the policy reconsiders, suggesting where to sample alternative continuations. We introduce Hindsight-Divergence Localization (HDL), which uses hindsight-induced changes in token log-likelihoods to select branch points. HDL generates a small number of complete root trajectories and fills each training group with continuations from the selected positions under the original task context. Each continuation reuses its root prefix and contributes policy updates only through its newly generated suffix, reducing generation cost while focusing additional exploration and learning on decisions after branching. Experiments with three models across math, code, and agent tasks show gains in both rollout efficiency and task performance. Compared with GRPO at matched group sizes and training steps, HDL yields up to a 2.5$\times$ reduction in generated tokens and a 1.8$\times$ speedup in rollout wall-clock time. Despite this reduced generation budget, HDL improves performance across all three domains, with gains of up to 12.5 points on agent tasks.

**Key innovations.**

- Uses *hindsight* as the search signal: the change in token log-likelihoods after a completed trajectory reveals which earlier decisions the policy reconsiders, indicating where to branch.
- Each continuation reuses its root prefix and contributes policy updates only through its newly generated suffix, so generation cost falls while extra exploration concentrates on post-branch decisions.
- Against GRPO at matched group size and step count: up to **2.5× fewer generated tokens** and **1.8× rollout wall-clock speedup**.
- Efficiency is not bought with quality — improvements across math, code and agent tasks, with up to +12.5 points on agent tasks.

---

### 7. The Asymptotics of Language Model Alignment with Memory

- **arXiv:** [2610.01828](https://arxiv.org/abs/2610.01828) · submitted 2026-10-01 · primary category `cs.CL` · all categories: `cs.CL`, `cs.IT`
- **Authors:** Haricharan Balasundaram; V. Arvind Rameshwar
- **Institution / company:** Georgia Institute of Technology (School of ECE); IIT Madras (Department of EE)
- **Affiliation evidence:** verified from author block

**Abstract.** Language model (LM) alignment broadly aims to perturb a given LM $Q$ into an aligned LM $q$ such that i) the outputs produced by $q$ and $Q$ are 'close' in probability, ii) $q$ has a higher expected reward than $Q$. Two common techniques for LM alignment are: KL-constrained RL, which requires knowledge of the LM distribution and is computationally expensive, and the best-of-$n$ algorithm, which requires only sampling from the LM. The work of Yang et al. established asymptotic closeness between the distributions produced by the two alignment methods for an $m$--length i.i.d. token sequence output by the LM, in the limit as $m$ increases to infinity. However, the i.i.d. assumption is not representative of practical LMs, whose output sequences often have memory. In this paper, we extend the asymptotic closeness result to the case when the $m$--length token sequence outputted by the LM is Markovian. Further, for finite-length output sequences -- particularly, when $m=1$ -- we provide a complete characterization of LM distributions and reward functions for which the KL-divergence between the distributions produced by the two alignment methods is zero -- a question first posed in Yang et al.

**Key innovations.**

- Identifies the load-bearing weakness of the existing result that KL-constrained RL and best-of-n produce asymptotically close distributions: that result assumes **i.i.d.** tokens, while real LM outputs are Markovian.
- Extends asymptotic closeness to Markovian length-m outputs.
- For finite lengths — particularly m = 1 — gives a complete characterization of the (LM distribution, reward function) pairs for which the two alignment methods coincide with *exactly zero* KL divergence, answering a question left open by Yang et al.

---

## Agents, Harnesses & Multi-Agent Systems (9)

### 8. Mid-Harness: Scaling Actions Between Model and Harness for Terminal Agents

- **arXiv:** [2609.39982](https://arxiv.org/abs/2609.39982) · submitted 2026-09-30 · primary category `cs.CL` · all categories: `cs.CL`, `cs.AI`, `cs.MA`
- **Authors:** Minki Kang; Ryo Hachiuma; Shaokun Zhang; Subhashree Radhakrishnan; Yonggan Fu; Jindong Jiang; Mingjie Liu; Ehsan Hosseini-Asl; Yi Dong; Yu-Chiang Frank Wang; Byung-Kwan Lee
- **Institution / company:** _(not stated — author block carries numeric affiliation superscripts 1,2 but no institution text is rendered)_
- **Affiliation evidence:** LaTeXML dropped the institution list; OpenAlex has no institutions. **Not inferred from author names.**
- **Author comment:** Project page: https://byungkwanlee.github.io/MidHarness-page/

**Abstract.** Terminal agents act through stochastic model generations, yet the ability to generate a useful action does not ensure its reliable execution. A poor command (e.g., wrong package install) can change the environment in ways that hinder subsequent progress, even when the model could generate a better alternative. We investigate whether allocating test-time compute at the model-harness boundary can improve action reliability and trajectory success, and what makes this allocation effective. To study these questions, we introduce Mid-Harness, which samples and verifies candidate actions before forwarding one for execution, while keeping the generator and harness unchanged. With a TMAX-9B generator, more action sampling yields little benefit under weak verification, whereas a capable verifier can exploit useful alternatives from the same generator. On TerminalBench-Lite, a GPT-5.6 Sol verifier raises Pass@1 from 50.00% for the base agent to 68.03% with 8 sampled actions. When the same TMAX-9B model serves as the verifier, pairwise verification performs best among the evaluated verification mechanisms. Distilling responses from the stronger verifier into TMAX-9B further improves Pass@1, while leaving the action generator unchanged. With TMAX-9B on TerminalBench-Lite, combining action and trajectory scaling reaches higher success at lower estimated token cost than generating more trajectories alone. Mid-Harness also improves performance across additional models, benchmarks, and harnesses. These findings identify action scaling as a promising target for test-time compute scaling in terminal agents.

**Key innovations.**

- Isolates a failure mode that pass@1 metrics hide: an agent can *generate* a good action and still execute a bad one, because a wrong command (e.g. a bad package install) mutates the environment in ways that block later progress.
- Allocates test-time compute at the model–harness boundary — sample candidate actions and verify before forwarding one for execution — while leaving the generator and the harness unchanged, so it drops into existing pipelines.
- Verifier quality is the binding constraint: with weak verification, more action sampling buys little; a GPT-5.6 Sol verifier raises TerminalBench-Lite Pass@1 from 50.00% to **68.03%** with 8 sampled actions. When the small TMAX-9B model verifies itself, pairwise comparison is the best of the tested mechanisms.
- Distilling the strong verifier's responses into TMAX-9B improves Pass@1 **without changing the action generator**, and action scaling reaches higher success at lower estimated token cost than generating more trajectories.

---

### 9. Mem++: Non-Destructive Memory for Long-Term Organizational LLM Agents

- **arXiv:** [2610.02002](https://arxiv.org/abs/2610.02002) · submitted 2026-10-01 · primary category `cs.CL` · all categories: `cs.CL`, `cs.AI`
- **Authors:** Ahmad Yehia; Aly O. Abdelkareem; Islam Ahmed; Hesham Omran; Khaled Alashmouny; Christian Claudel; Abduallah Mohamed
- **Institution / company:** The University of Texas at Austin; AIDAChip Inc.
- **Affiliation evidence:** verified from author block
- **Author comment:** 15 pages, 4 figures

**Abstract.** Large Language Model (LLM) agents now take part in organizational work, where many authors record decisions across documents over months. Because a revised decision arrives as a new document rather than an edit, answering a question requires knowing which version held at a given time. However, most memory systems compress the record at write time. By distilling each document into facts, notes or graph edges, these methods fix what can be answered before any question is asked. To address this, we propose Mem++, a non-destructive memory framework shifting from write-time distillation to read-time selection. Mem++ stores every document whole with its date and author, and it calls no generative model at write time. At read time, it retrieves only documents dated up to the time a question asks about and fuses lexical and semantic rankings. Unlike systems that overwrite older versions, Mem++ keeps them and leaves the choice to the answering model. Evaluations on the organizational benchmark OrgMemBench demonstrate that Mem++ surpasses the strongest memory system baseline by 8.0 to 13.1 points across two answering models. With gpt-4.1-mini, it also achieves the best overall score, 2.6 points above RAG. In addition, Mem++ achieves the best average LLM-judge score on LoCoMo and ranks second on LongMemEval-S, behind only its entity-graph variant. Code for benchmark evaluation is available at https://github.com/AIDAChip-Inc/mem-plus-plus.

**Key innovations.**

- Targets a structural flaw in write-time memory distillation: distilling each document into facts, notes or graph edges fixes what can be answered *before any question is asked*.
- Frames the versioning problem precisely — a revised decision arrives as a new document rather than an edit, so answering a question requires knowing which version held at a given time.
- Non-destructive design: store every document whole with its date and author, call **no generative model at write time**, and shift the work to read-time selection that retrieves only documents dated up to the queried time and fuses lexical with semantic rankings.
- +8.0 to +13.1 points over the strongest memory-system baseline on OrgMemBench across two answering models; with gpt-4.1-mini it also takes the best overall score, 2.6 above plain RAG.

---

### 10. Mingbird: A Local-First Agent Harness Enabling Small Open Models to Complete Real Tasks

- **arXiv:** [2610.02001](https://arxiv.org/abs/2610.02001) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`, `cs.CL`
- **Authors:** Hao Wang; Ting Huang
- **Institution / company:** University of Science and Technology Beijing; Honor Device Co., Ltd.
- **Affiliation evidence:** verified from author block
- **Author comment:** 44 pages, 9 figures. Code, benchmark protocol, scoring code, and all 288 per-cell results: https://github.com/Mingbird/Mingbird-agent

**Abstract.** Small open-weight models (2-9B) run on ordinary laptops, but under cloud-scale agent harnesses they rarely complete real tasks: tool prefill overflows the context, self-correction diverges, tool demonstrations loop, and tasks are silently abandoned. We present evidence, from a controlled single-machine comparison and one third-party benchmark, that a substantial share of these failures is attributable to the harness rather than the model. We introduce Mingbird, a local-first agent harness for Windows and Ollama whose ten mechanisms compensate point-by-point for small-model failure forms, three of them representative: a byte-level net-zero prefill budget, a finish gate that re-reads the task before accepting completion, and signature-level loop detection. On LRAB, a controlled comparison holding machine, models, budgets, and scoring fixed (4 harnesses $\times$ 4 open models (2B-35B) $\times$ 18 real tasks, deterministic artifact scoring), Mingbird reaches 0.886 overall against 0.631 (goose), 0.479 (opencode), and 0.405 (agent-mini), with all 288 cells published; on $τ^2$-bench (278 tasks, three arms, one protocol) it totals 0.856 against 0.791 and 0.737; and a frontier-model probe on the same 18 tasks spans 0.997 to 0.478 across harnesses, with well-formed scaffolds staying within 0.072 of each other. A leave-one-mechanism-out ablation is reported as directional only: same-night replications of the same arm move its mean by up to 0.069, the size of every nominal single-trial delta, and the one batch-matched comparison (full mechanism stack versus text re-read alone) gives the executable completion guards a paired +0.10 across three replications. The evidence carries stated limits: a self-built benchmark, a single machine, and single-trial scoring.

**Key innovations.**

- Reframes small-model agent failure as substantially a **harness** problem, naming four concrete forms: tool prefill overflowing context, diverging self-correction, looping tool demonstrations, and silently abandoned tasks.
- Ten compensating mechanisms, three representative: a byte-level net-zero prefill budget, a finish gate that re-reads the task before accepting completion, and signature-level loop detection.
- Controlled protocol rather than anecdote — 4 harnesses × 4 open models (2B–35B) × 18 real tasks with deterministic artifact scoring, all 288 cells published: 0.886 vs goose 0.631, opencode 0.479, agent-mini 0.405; on τ²-bench (278 tasks) 0.856 vs 0.791 and 0.737.
- **Unusually disciplined negative reporting**: the leave-one-mechanism-out ablation is declared *directional only*, because same-night replications move an arm's mean by up to 0.069 — the size of every nominal single-trial delta — and the one batch-matched comparison gives the completion guards a paired +0.10. The frontier-model probe shows well-formed scaffolds landing within 0.072 of each other, i.e. most of the measured spread is harness choice, not model capability.

---

### 11. Beyond Memory: Harnessing Long-Horizon Agents with Explicit Belief States

- **arXiv:** [2610.01415](https://arxiv.org/abs/2610.01415) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`
- **Authors:** Yu Luo; Jiamin Jiang; Yimin Zuo; Xidao Wen; Rongchen Gao; Yongqian Sun; Shenglin Zhang; Guiyang Liu; Cheng Zhang; Fang Situ; Qi Zhou; Dan Pei
- **Institution / company:** Nankai University; Alibaba Group; Tsinghua University
- **Affiliation evidence:** verified from author block

**Abstract.** Large language model (LLM) agents can now undertake increasingly complex tasks, but the way they organize interaction history into memory does not ensure a coherent understanding of the current world. We introduce PoS, an inference-time framework that constructs and continually maintains explicit belief states as the agent's decision context. Each belief combines an estimate of the current world state with unresolved task requirements, making explicit what the agent still needs to learn and accomplish. To keep this belief reliable and actionable, PoS validates its consistency and monitors task progress to detect Belief Trapping, where the agent continues to act without making meaningful progress toward the goal. Recovery is then tailored to both the trapping pattern and the type of unresolved task requirement. Experiments on four benchmarks spanning execution and diagnosis show that PoS achieves the highest overall performance on every benchmark with all three LLM backbones. Ablations demonstrate the importance of consistency validation and recovery, while context-scaling experiments show resilience to context growth. Together, these results support belief construction and continual maintenance as a foundation for long-horizon context management beyond history retention and compression.

**Key innovations.**

- Argues that organizing interaction history into memory does not produce a coherent model of the current world — retention and compression are not understanding.
- **PoS** maintains explicit belief states as the decision context, each combining an estimate of world state with *unresolved task requirements*, so 'what I still need to learn' becomes first-class.
- Adds consistency validation and progress monitoring to detect **Belief Trapping** (the agent keeps acting without meaningful progress); recovery is tailored to both the trapping pattern and the type of unresolved requirement.
- Best overall performance on all four benchmarks with all three backbones; ablations isolate consistency validation and recovery, and context-scaling experiments show resilience as context grows.

---

### 12. Beyond Final Accuracy: Auditing Communication in LLM Multi-Agent Systems

- **arXiv:** [2610.01042](https://arxiv.org/abs/2610.01042) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`, `cs.CL`
- **Authors:** Shixuan Li; Wei Yang; Peiyu Zhang; Anzhe Cheng; Heng Ping; Paul Bogdan
- **Institution / company:** University of Southern California (Department of Computer Science); plus one affiliation rendered as '… Department of Electrical and Computer Engineering' with **no institution named** — the source's LaTeX template is malformed
- **Affiliation evidence:** verified from author block; the second affiliation string names a department but no university, so it is left unassigned rather than guessed

**Abstract.** Multi-agent communication aims to help agents benefit from one another's information. Yet improvements in system performance leave a fundamental ambiguity: do they reflect effective communication, a favorable agent architecture, or simply additional reasoning? Because communication methods are commonly evaluated within the systems they were designed for, these factors are difficult to disentangle. Final accuracy further merges corrected errors and corrupted answers into a single outcome, obscuring how communication changes decisions. We introduce Independent--Communicate--Revise (ICR), a controlled framework that evaluates communication as answer revision following independent reasoning. ICR fixes initial reasoning trajectories, measures correction and preservation conditional on both agents' initial correctness, and uses a no-message revision control to quantify gains beyond additional reasoning. Across four reasoning benchmarks, our audit of textual and latent communication reveals that similar aggregate accuracy can conceal substantially different revision behaviors. Compared with transmitting answers alone, full reasoning increases correction while reducing preservation on all four benchmarks, so richer messages amplify beneficial and harmful influence alike. Receiver-policy comparisons on MedQA and GPQA-D further show that a structured verification policy shifts every channel toward greater preservation and lower correction, while its effect on selectivity varies across channels and tasks. These findings challenge treating communication quality as an intrinsic property of a channel. ICR therefore recenters evaluation on selective revision, providing a unified framework for examining how message content and receiver policies jointly produce benefits and harms.

**Key innovations.**

- Names the confound in multi-agent communication evaluation: gains can reflect effective messaging, a favorable architecture, or simply additional reasoning — and the standard practice of evaluating a communication method inside the system it was designed for makes these inseparable.
- **ICR** (Independent–Communicate–Revise) fixes the initial reasoning trajectories, measures correction and preservation *conditional on both agents' initial correctness*, and adds a no-message revision control to quantify gains beyond extra inference.
- Finding that inverts the usual assumption: transmitting full reasoning rather than answers **increases correction and decreases preservation on all four benchmarks** — richer messages amplify beneficial and harmful influence alike.
- A structured verification policy shifts every channel toward greater preservation and lower correction, while its effect on selectivity varies across channels and tasks — so communication quality is not an intrinsic property of a channel.

---

### 13. Safety of Latent Communication in Multi-Agent Systems

- **arXiv:** [2609.39788](https://arxiv.org/abs/2609.39788) · submitted 2026-09-30 · primary category `cs.AI` · all categories: `cs.AI`, `cs.LG`, `cs.MA`
- **Authors:** Muhammad Huzaifa; Sina Mavali; Thorsten Eisenhofer
- **Institution / company:** CISPA Helmholtz Center for Information Security, Saarbrücken, Germany
- **Affiliation evidence:** verified from author block

**Abstract.** Latent communication enables multi-agent systems to exchange information directly in internal representation space, reducing the token, computation, and latency overhead of text-based communication. To this end, lightweight trainable links are introduced to map the sender's representations into the receiver's input space. In this work, we show that even benign link training can increase harmful compliance relative to text-based communication while the underlying safety-aligned agents remain unchanged. An attacker can amplify this effect by optimizing the links on harmful query--response pairs or poisoning otherwise benign training data. We further develop a reinforcement-learning attack that rewards harmful compliance alongside benign task performance without requiring harmful target responses. Across three communication topologies and four safety benchmarks, this attack raises the mean harmful-compliance score from 27.9 with benignly trained links to 76.9. Compared with direct supervised optimization, it also achieves higher average accuracy on two benign utility benchmarks. Adapting the rewards toward safer behavior also enables repair of compromised links, substantially reducing harmful compliance across all evaluated attacks without updating the agents. Overall, our results show that safety alignment requires considering the multi-agent system as a whole. Code: https://github.com/Muhammad-Huzaifaa/latent-safety

**Key innovations.**

- Core result: benignly training latent-communication links **alone** raises harmful compliance relative to text communication, while the underlying safety-aligned agents are completely unchanged — safety alignment is not compositional over the link.
- An attacker amplifies this either by optimizing the links directly on harmful query–response pairs or by poisoning otherwise benign training data.
- Builds an RL attack that rewards harmful compliance *without* requiring harmful target responses, which is both stronger and harder to detect; mean harmful-compliance score rises 27.9 → **76.9** across three topologies and four safety benchmarks, and it also beats direct supervised optimization on benign utility.
- Repair is possible by adapting the attack reward toward safety — compromised links are substantially fixed across all evaluated attacks without updating the agents.

---

### 14. Beyond Leaderboards: Tokenomics of Agentic Small Language Model Ensembles

- **arXiv:** [2610.00954](https://arxiv.org/abs/2610.00954) · submitted 2026-10-01 · primary category `cs.CL` · all categories: `cs.CL`
- **Authors:** Alexei N. Skurikhin; Emily M. Taylor; Nathan A. DeBardeleben
- **Institution / company:** Los Alamos National Laboratory
- **Affiliation evidence:** verified from author block
- **Author comment:** 8 pages, 9 figures, Presented at ACM CAIS 2026 Workshop RLEval: Methods and Reinforcement Learning Environments for Evaluating AI Agents. Resubmission of permitted appeal, Ticket #MOD-104177

**Abstract.** As large language models (LLMs) move from standalone assistants into agentic workflows, evaluation must extend beyond scalar leaderboard accuracy to account for operational reliability, cost, latency, and token efficiency. We use an agentic ensemble of small language models (SLMs) with an SLM-judge-mediated feedback loop as a case study for such beyond-leaderboard evaluation. On the 541-prompt IFEval benchmark, the best ensemble achieves 97.34% strict prompt accuracy, exceeding the strongest standalone LLM baseline, gpt-5.4, by 5.81 percentage points while operating in a lower-cost regime. We then analyze the tokenomics and operational behavior behind this gain, including cost per sample, token composition, useful-output goodput, feedback-loop recovery, latency decomposition, and performance across instruction categories and constraint counts. Our results show that agentic SLM ensembles can trade additional test-time tokens and orchestration overhead for improved instruction-following fidelity, motivating multi-dimensional evaluation protocols for future agentic AI systems.

**Key innovations.**

- Argues leaderboard accuracy is the wrong axis for agentic systems and proposes cost, latency, token efficiency and operational reliability as first-class evaluation dimensions.
- An agentic ensemble of small language models with an SLM-judge-mediated feedback loop reaches **97.34%** strict prompt accuracy on the 541-prompt IFEval benchmark — +5.81 points over the strongest standalone baseline (gpt-5.4) — while operating in a lower-cost regime.
- Then dissects the gain rather than asserting it: cost per sample, token composition, useful-output goodput, feedback-loop recovery, latency decomposition, and performance across instruction categories and constraint counts.
- States the trade honestly: agentic SLM ensembles convert extra test-time tokens and orchestration overhead into instruction-following fidelity.

---

### 15. VeriHarness: Scaling Agentic Verification for Long-Horizon Tasks

- **arXiv:** [2610.00972](https://arxiv.org/abs/2610.00972) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`, `cs.MA`
- **Authors:** Caiqi Zhang; Rujun Han; Zifeng Wang; Zoey CuiZhu; Nigel Collier; Tomas Pfister; Chen-Yu Lee
- **Institution / company:** Google Cloud AI Research; University of Cambridge
- **Affiliation evidence:** verified from author block

**Abstract.** As LLM agents undertake increasingly complex, long-horizon tasks, verifying their outputs becomes increasingly challenging. We study how verification capability can be strengthened with a fixed base model, without access to reference answers or grading rubrics at test time. Repeated sampling yields multiple rollouts that can contain complementary correct claims, but we need a reliable verification mechanism to determine which claims to trust. We first find that disagreement often exposes correct alternatives, while consensus can conceal errors. These observations motivate VeriHarness, which turns the underlying LLM a generator uses into an agentic verifier by giving it a workspace, evidence tools, and reusable verification skills. A disagreement resolver checks competing claims against environmental evidence, while a consensus challenger tests shared claims and searches for omitted requirements. Their findings guide the selection and revision of the final artifact. Across five long-horizon workspace benchmarks and two frontier models, VeriHarness achieves the highest selection scores among the evaluated baselines. Evidence-backed revision further improves average performance, bringing gains over a single rollout to 6.2 points with Gemini 3.5 Flash and 6.4 points with Claude Opus 4.8. We further show that verification skills can self-improve from failure feedback, demonstrating VeriHarness as a novel and critical approach for scaling long-horizon agentic verification. We release the full pool of approximately 26,000 rollouts across all five benchmarks and both models, produced at a cost of over $100,000, to support future research on agentic verification.

**Key innovations.**

- Sharp empirical premise with an edge: **disagreement often exposes correct alternatives, while consensus conceals errors** — which makes majority voting the wrong primitive for verification.
- Turns the generator itself into an agentic verifier using a workspace, evidence tools and reusable verification skills; a disagreement resolver checks competing claims against environmental evidence, and a consensus challenger tests shared claims while hunting for omitted requirements.
- Evidence-backed revision adds +6.2 points with Gemini 3.5 Flash and +6.4 with Claude Opus 4.8 over a single rollout, best selection scores among evaluated baselines across five long-horizon workspace benchmarks and two frontier models.
- Verification skills self-improve from failure feedback, and the full pool of ~26,000 rollouts across all five benchmarks and both models is released at a stated cost of over $100,000.

---

### 16. Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens

- **arXiv:** [2610.01939](https://arxiv.org/abs/2610.01939) · submitted 2026-10-01 · primary category `cs.CV` · all categories: `cs.CV`
- **Authors:** Ruiyang Si; Jianxin Bi; Shunyu Yang; Rui Ni; Wenbo Huang; Qiang Wang; Shulong Jiang; Duomin Wang; Xiuyu Li; Haiwen Feng; Zhen Dong; Daquan Zhou
- **Institution / company:** Peking University; National University of Singapore; NVIDIA; Impossible Research
- **Affiliation evidence:** verified from the paper's numbered front-matter institution list

**Abstract.** Vision language model (VLM) agents can control robots through visual feedback and action primitives, but repeated model invocations and redundant observations incur substantial token overhead. We introduce PyRUA-Lean, an interactive code-execution framework that couples feedback-driven primitive composition with selective observation: the agent composes classical robot primitives and learned vision-language-action (VLA) policies into Python cells that perform conditional checks and local retries, returning only explicitly requested images and state feedback for replanning. Across 700 simulated task instances from LIBERO-PRO, RoboTwin 2.0, and RoboCasa365, we compare PyRUA-Lean with a tool-calling baseline using the same GPT-6 Astra planner and underlying robot primitives. Under equal LLM-call budgets, PyRUA-Lean increases overall success from 63.1% to 71.7%. On instances solved by both agents, it uses 49% fewer LLM calls and 65% fewer input tokens.

**Key innovations.**

- Identifies where VLM robot-agent token overhead actually comes from: repeated model invocations and redundant observations, not the actions themselves.
- **PyRUA-Lean** couples feedback-driven primitive composition with selective observation — classical robot primitives *and* learned VLA policies are composed into Python cells that run conditional checks and local retries, returning only explicitly requested images and state feedback for replanning.
- At **equal LLM-call budget** across 700 simulated instances from LIBERO-PRO, RoboTwin 2.0 and RoboCasa365, overall success rises 63.1% → 71.7% against a tool-calling baseline using the same GPT-6 Astra planner and the same underlying primitives.
- On instances both agents solve, it uses 49% fewer LLM calls and 65% fewer input tokens.

---

## Inference, Architecture & Serving Systems (9)

### 17. AgSpec: Pushing the Limits of Retrieval-Based Speculative Decoding in Coding Agent Pipelines

- **arXiv:** [2610.01108](https://arxiv.org/abs/2610.01108) · submitted 2026-10-01 · primary category `cs.CL` · all categories: `cs.CL`
- **Authors:** Sumin Lee; Sukmin Cho; Suengjae Lim; Youngjin Kwon
- **Institution / company:** KAIST (School of Computing)
- **Affiliation evidence:** verified from author block

**Abstract.** Retrieval-based speculative decoding (SD) drafts tokens by copying continuations from existing text, which suits coding agents that repeatedly reproduce code, logs, and earlier attempts. Yet existing methods fall short in agent pipelines: much of the reusable text is missing from their corpora or stored in a form that differs from what the agent emits, and their draft lengths ignore that accept length varies across agents and drifts over turns. We present AgSpec, a framework that supplies the corpus and draft-length policies that existing retrieval engines lack in coding-agent pipelines. AgSpec retrieves from session, workspace, and global corpora, retaining the ongoing session trajectory and indexing opened files in the agent's emission format. It bounds each agent's draft length with an offline-profiled cap and adapts the length online from verification feedback. On two repository-level multi-agent coding benchmarks, AgSpec outperforms five retrieval-based drafters and EAGLE-3 in most evaluated settings, raising generation throughput over autoregressive decoding up to 4.37$\times$ at batch size 1 and 4.76$\times$ at batch size 16. AgSpec also remains effective on benchmarks without a repository or a multi-agent pipeline, showing that its gains generalize to coding agents broadly.

**Key innovations.**

- Argues retrieval-based speculative decoding is a natural fit for coding agents — code, logs and earlier attempts get reproduced — then identifies why existing engines fail there: reusable text is missing from the corpus, or stored in a form that differs from what the agent actually emits.
- Supplies the two policies existing retrieval engines lack: corpus *format* (session / workspace / global tiers, retaining the live session trajectory and indexing opened files in the agent's emission format) and draft *length* (an offline-profiled per-agent cap, adapted online from verification feedback).
- Throughput over autoregressive decoding up to **4.37×** at batch size 1 and **4.76×** at batch size 16; beats five retrieval-based drafters and EAGLE-3 in most evaluated settings on two repository-level multi-agent coding benchmarks.
- Gains persist on benchmarks with no repository and no multi-agent pipeline, so the mechanism is not an artifact of the setting it was designed for.

---

### 18. CommunityKV: Efficient Long-Context Decoding via Graph Partitioning

- **arXiv:** [2610.00418](https://arxiv.org/abs/2610.00418) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`
- **Authors:** Joe McKenna; Anastasios Alexandridis; Nathan Susanj; Jing Liu
- **Institution / company:** Amazon AGI
- **Affiliation evidence:** verified from author block

**Abstract.** Scaling Transformers to long contexts is constrained by the quadratic cost of self-attention and the linear growth of key-value cache memory transfer. Sparse attention mitigates this by retrieving only relevant tokens, but current approaches either require large-scale training or, within the training-free regime, rely on semantically coarse heuristics or expensive clustering that is difficult to update efficiently during decoding. We introduce CommunityKV, a framework that formulates sparse attention as a community detection problem. CommunityKV constructs a token graph from the $QK^T$ scores already computed during standard prefill, and partitions the graph into communities to enable retrieval of semantically coherent token groups. A local update rule assigns newly generated tokens to communities in constant time, enabling sparse retrieval throughout streaming decoding without global re-partitioning. We evaluate CommunityKV on Qwen3 and Llama-3.1 models across three long-context benchmarks. With one graph per query head, CommunityKV delivers up to $1.25\times$ the end-to-end generation throughput of dense attention, while query-group graph aggregation yields up to $1.71\times$ with comparable accuracy.

**Key innovations.**

- Reframes training-free sparse attention as **community detection**: build the token graph from the QK^T scores already computed during ordinary prefill, then partition it so retrieval returns semantically coherent token groups.
- Avoids the two usual costs — no large-scale training, and no expensive clustering that is hard to update mid-decoding — via a local update rule that assigns each newly generated token to a community in **constant time**, so sparse retrieval runs throughout streaming decoding without global re-partitioning.
- Up to **1.25×** end-to-end generation throughput vs. dense attention with one graph per query head, and up to **1.71×** with query-group graph aggregation at comparable accuracy.
- Measured on Qwen3 and Llama-3.1 across three long-context benchmarks.

---

### 19. AVSG: Accelerated Vectorized Sparse Gather for Efficient KV Cache Offload in Sparse-Attention LLM Serving

- **arXiv:** [2609.37538](https://arxiv.org/abs/2609.37538) · submitted 2026-09-29 · primary category `eess.SP` · all categories: `eess.SP`
- **Authors:** Wenwei Kuang; Xiangyu Wang; Chong Wu; Jun Wang; Weijie Zhang; Brian K Chen; Longwen Lan; Ken Zhang
- **Institution / company:** Theory Lab, 2012 Labs, Huawei Technologies Co., Ltd
- **Affiliation evidence:** verified from author block
- **Author comment:** 20 pages, 7 figures

**Abstract.** Dynamic sparse attention reduces long-context attention computation by selecting only a subset of tokens, but still requires access to the full KV cache, leaving serving memory-bound. Offloading the KV cache to host memory reduces device memory pressure but places H2D transfers on the decoding critical path. In DSA, substantial overlap in selected KV entries across decoding steps creates an opportunity for device-resident reuse. Exploiting this reuse efficiently, however, presents three critical challenges: costly matching of selected tokens against entries retained in the HBM buffer, uneven distribution of the remaining H2D transfers across accelerator cores, and retaining frequently accessed KV entries within limited HBM capacity. We present AVSG, an operator that addresses these challenges for DSA while preserving its exact token selections. AVSG uses vectorized hash matching to identify reusable HBM-buffer slots and reserve slots for entries requiring transfer, then evenly partitions these H2D transfers across accelerator cores. Lifetime-based buffer management retains frequently accessed KV entries in the device buffer across decoding steps, and shared slot reservations extend reuse across tokens within a multi-token prediction iteration. On a single NPU, vectorized hash matching is 2.80x faster than scalar dual-pointer matching, miss-only transfer raises effective H2D bandwidth by up to 34.44x over request-level assignment, and an 8K-entry buffer reaches a 94.83% hit rate on real requests. These gains translate into end-to-end improvement: on a serving stack processing a real-world production dataset, AVSG reduces time per output token by 39% and increases output throughput by 1.27x relative to the same KV offload layout without HBM-buffer reuse, demonstrating the benefit of efficient matching, balanced transfer, and effective HBM residency in production-scale serving.

**Key innovations.**

- Finds the bottleneck that dynamic sparse attention does *not* remove: token selection shrinks attention compute but serving stays memory-bound because the full KV cache must still be reachable, and host offload puts H2D transfers on the decode critical path.
- Exploits the fact that DSA selects substantially overlapping KV entries across decoding steps: vectorized hash matching to identify reusable HBM-buffer slots and reserve slots for entries needing transfer, even partitioning of the residual H2D transfers across accelerator cores, lifetime-based retention of hot entries, and shared slot reservations across a multi-token-prediction iteration — all **while preserving exact token selections**.
- Microbenchmarks: hash matching 2.80× faster than scalar dual-pointer matching; miss-only transfer raises effective H2D bandwidth by up to 34.44×; an 8K-entry buffer reaches a 94.83% hit rate on real requests.
- End-to-end on a serving stack with a real production dataset: **−39% time per output token and 1.27× output throughput** versus the same KV-offload layout without HBM reuse.

---

### 20. Triadic Linear Attention: Three-Dimensional Recurrent States for Long-Context Sequence Modeling

- **arXiv:** [2609.36529](https://arxiv.org/abs/2609.36529) · submitted 2026-09-29 · primary category `cs.LG` · all categories: `cs.LG`, `cs.CL`
- **Authors:** Oliver Sieberling; Bharat Runwal; David Jin; Ryan Chin; Rameswar Panda; Yoon Kim
- **Institution / company:** Massachusetts Institute of Technology; MIT-IBM Computing Research Lab
- **Affiliation evidence:** verified from author block
- **Author comment:** Preprint

**Abstract.** Recurrent neural networks (RNNs) compress the historical context into a memory state of fixed size, thus allowing for constant-time inference. The memory state size is a crucial factor in their performance, as exemplified by the strong performance and resurgence of linear attention, which extends the vector-valued hidden states of ordinary RNNs to matrix-valued hidden states. Crucially, linear attention does so in a parameter-efficient way, in particular by using an outer product of the key and value vectors to write to the matrix-valued hidden state. We generalize this construction and propose triadic linear attention, which writes the triadic outer product of a key, a second key, and a value, into a third-order (i.e., 3D) tensor state, and reads from it by contracting both key axes with two queries. An $E$-dimensional second key thus yields an $E$-fold increase in state size while adding only two projections. Triadic linear attention is compatible with data-dependent forgetting, the delta rule, and chunkwise-parallel training. Applied to Gated DeltaNet and scalar-gated linear attention, triadic linear attention substantially improves long-context language modeling and recall, outperforming alternatives that enlarge the state.

**Key innovations.**

- Generalizes linear attention's key⊗value outer product to a **triadic** product — key, second key, value — written into a third-order (3D) tensor state and read by contracting both key axes with two queries.
- Cost claim: an E-dimensional second key yields an **E-fold increase in state size for only two extra projections**, because state capacity is raised by factorizing along a new axis rather than by widening existing ones.
- Stays compatible with data-dependent forgetting, the delta rule, and chunkwise-parallel training.
- Applied to Gated DeltaNet and scalar-gated linear attention, it substantially improves long-context language modeling and recall — and beats alternatives that simply enlarge the state.

---

### 21. Decoding Looped Transformers Better for (Almost) Free

- **arXiv:** [2610.02185](https://arxiv.org/abs/2610.02185) · submitted 2026-10-01 · primary category `cs.LG` · all categories: `cs.LG`
- **Authors:** Weihao Liu; Huangjie Zheng; Tianrong Chen; Rohit Dilip; Richard He Bai; Yizhu Jiao; Yuyang Wang; Ruixiang Zhang
- **Institution / company:** Apple
- **Affiliation evidence:** the author's LaTeX template dumps the affiliation into an `ltx_dates` div; read directly from the rendered front matter
- **Author comment:** 32 pages, 19 figures

**Abstract.** Looped Transformers achieve parameter efficiency by repeatedly executing a shared block across recurrent loops. Each loop yields an intermediate representation decodable for the same next token, yet standard decoding discards earlier states. Because earlier loops embody less computation, recurrence inherently supplies aligned weak-and-strong prediction pairs without auxiliary models or external training. We introduce LoopCD, a training-free contrastive decoding framework that guides token selection by contrasting the final prediction with an earlier recurrent pass, operating either in logit space with one extra output pass (LoopCD-Logits) or in hidden-state space with zero output overhead (LoopCD-Hidden). Across four looped Transformer families, LoopCD delivers substantial, consistent gains at full recurrent depth: LoopCD-Logits raises Ouro-2.6B-Thinking's AIME 2024 pass@1 from 61.88% to 73.33%, while LoopCD-Hidden lifts Huginn's HumanEval pass@1 from 22.56% to 31.71%. Crucially, these performance gains enable halving the number of recurrent loops while still matching or exceeding full-depth unguided baselines, reducing forward FLOPs by 22.5% to 48.2%. By transforming intermediate recurrent states into effective guidance signals, LoopCD achieves superior decoding quality while substantially reducing inference compute.

**Key innovations.**

- Points out that looped Transformers contain free supervision nobody was using: earlier recurrent passes are weaker predictors of the *same* next token, so recurrence inherently supplies aligned weak-and-strong pairs with no auxiliary model and no training.
- **LoopCD** is training-free contrastive decoding that guides token selection by contrasting the final prediction against an earlier pass — in logit space (one extra output pass) or in hidden-state space (zero output overhead).
- Ouro-2.6B-Thinking AIME 2024 pass@1 61.88% → 73.33%; Huginn HumanEval pass@1 22.56% → 31.71%, consistent across four looped Transformer families.
- The real payoff is compute, not accuracy: the gains allow **halving the number of recurrent loops** while still matching or exceeding full-depth unguided baselines, cutting forward FLOPs by 22.5–48.2%.

---

### 22. Learn the Directions, Normalize the Gains: Post-Training Normalization for LoRA

- **arXiv:** [2610.02067](https://arxiv.org/abs/2610.02067) · submitted 2026-10-01 · primary category `cs.LG` · all categories: `cs.LG`
- **Authors:** Zailong Tian; Yanzhe Chen; Zhuoheng Han; Houfeng Wang; Lizi Liao
- **Institution / company:** Singapore Management University; National University of Singapore; Peking University
- **Affiliation evidence:** verified from author block

**Abstract.** While Low-Rank Adaptation (LoRA) enables efficient task specialization, its learned updates can compromise capabilities beyond the target task. We identify \textbf{adaptation imbalance}: a few singular directions dominate the trained update, leaving its performance sensitive to how gains are allocated. We argue that \textbf{learning where to adapt does not ensure that adaptation gains are well balanced}. This motivates \textbf{LoRA-Norm}, a post-training normalization method that retains learned directions while rebalancing their gains. LoRA-Norm combines spectral rebalancing, a fixed nonlinear transformation of singular values, with nuclear-norm restoration, which preserves the original total spectral mass. It requires no calibration data or additional training and introduces no inference overhead. Across two backbones and three adaptation tasks, LoRA-Norm improves average specialization and capability retention, outperforming the evaluated post-hoc spectral pruning and gradient-guided editing configurations on both measures. Stronger functional equalization brings no consistent additional gains, revealing that balancing adapter gains and equalizing their responses are distinct objectives.

**Key innovations.**

- Names **adaptation imbalance**: a few singular directions dominate the trained LoRA update, leaving performance sensitive to how gain is allocated — so 'learning *where* to adapt' does not ensure adaptation gains are balanced.
- **LoRA-Norm** keeps the learned directions and rebalances their gains after training: spectral rebalancing (a fixed nonlinear transform of singular values) plus nuclear-norm restoration to preserve total spectral mass. No calibration data, no additional training, no inference overhead.
- Improves both specialization and capability retention over post-hoc spectral pruning and gradient-guided editing configurations, across two backbones and three adaptation tasks.
- Useful negative result: stronger *functional* equalization brings no consistent additional gain — balancing adapter gains and equalizing their responses are distinct objectives.

---

### 23. Reshaping Rollout Workloads for Asynchronous RL Post-Training on Heterogeneous Accelerators

- **arXiv:** [2609.36899](https://arxiv.org/abs/2609.36899) · submitted 2026-09-29 · primary category `cs.DC` · all categories: `cs.DC`
- **Authors:** Jiahui Li; Hao Nie; Yibo Zhu; Pengjin Xie; Yu Zhou; Xiaolong Zheng; Liang Liu; Huadong Ma
- **Institution / company:** Beijing University of Posts and Telecommunications; StepFun
- **Affiliation evidence:** verified from the paper's numbered front-matter institution list

**Abstract.** Reinforcement learning (RL) post-training increasingly relies on long-horizon, multi-turn rollouts. As post-training jobs outgrow a single cluster, rollout pools assembled across clusters introduce hardware heterogeneity. Rollout scheduling must serve two stakeholders: the hardware needs high aggregate decode throughput, while each trajectory needs to finish quickly. The tension arises from the memory-bandwidth-bound nature of autoregressive decoding. A large active batch amortizes weight reads for high throughput but leaves each trajectory a smaller bandwidth share and a longer completion time. The scheduling objective is therefore specialization, letting different workers serve different roles. Heterogeneous hardware further enables this specialization. High-bandwidth accelerators favor long-context work, while cost-efficient accelerators sustain large batches. Workload evolution makes this specialization difficult to sustain, and dynamic reassignment faces a circular dependency because a move's benefit depends on subsequent placement decisions. We present CadenceRL, which bypasses this dependency through structural workload reshaping rather than per-move benefit estimation. Pacing replaces long-context trajectories with shorter ones, providing a structurally positive transformation that sustains large active batches for high throughput. When accumulated staleness demands faster completion, concentration directs the residual long-context tail onto high-affinity workers. Late-bound KV preparation stages accumulated prefixes before a destination is selected. On heterogeneous rollout pools, CadenceRL improves decode throughput by up to 48% and reduces P95 trajectory latency by up to 64%. Adding high-bandwidth accelerators reduces tail latency, while adding cost-efficient accelerators increases throughput, without manual routing configuration.

**Key innovations.**

- Names the scheduling tension precisely: autoregressive decoding is bandwidth-bound, so a large active batch buys aggregate throughput by starving each trajectory of bandwidth — throughput and per-trajectory latency are in direct conflict.
- Heterogeneous hardware enables **specialization** (high-bandwidth parts take long-context work, cost-efficient parts sustain large batches), but workload evolution breaks it, and dynamic reassignment is circular because a move's value depends on subsequent placements.
- **CadenceRL** sidesteps the circular dependency through structural workload reshaping instead of per-move benefit estimation: *pacing* replaces long-context trajectories with shorter ones (a structurally positive transformation that sustains large active batches), *concentration* routes the residual long-context tail onto high-affinity workers, and late-bound KV preparation stages accumulated prefixes before a destination is chosen.
- Up to **+48% decode throughput** and **−64% P95 trajectory latency**; adding high-bandwidth accelerators cuts tail latency while adding cost-efficient accelerators raises throughput, with no manual routing configuration.

---

### 24. HHR: Hierarchical Hash Retrieval for Efficient LLM Generation

- **arXiv:** [2610.01230](https://arxiv.org/abs/2610.01230) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`
- **Authors:** Lianjun Liu; Tiantian Zheng; You Huang; Weiqi Yan; Mingte Qiu; Huazhong Liu; Xiaofeng Zhu; Yunshan Zhong
- **Institution / company:** Hainan University; Xiamen University; Zhejiang Normal University
- **Affiliation evidence:** verified from author block

**Abstract.** Efficient long-context inference is essential for large language models (LLMs), yet it poses a severe computational bottleneck. Hash-based retrieval offers an efficient alternative by encoding queries and keys into binary codes and using Hamming distance for key selection. However, this leads to a critical mismatch between Hamming distance and attention relevance. Query-Key logits depend jointly on directional similarity and feature magnitudes, whereas hash binarization discards magnitude information, causing both false-positive retrieval of low-logit keys and false-negative omission of high-logit keys. To address these failures, we propose Hierarchical Hash Retrieval (HHR), a coarse-to-fine framework that progressively improves retrieval accuracy through Geometry-Aware Key Routing (GKR) and Learned Hash Projection (LHP). GKR learns a head-wise orthogonal transformation to redistribute feature magnitudes and derive more discriminative page-level logit bounds, enabling effective pruning of low-logit keys while preserving important candidates. LHP then learns a head-wise projection space that aligns Hamming distance with the true Query-Key relevance ranking for fine-grained retrieval. By combining GKR and LHP, HHR suppresses false positives and recovers false negatives, substantially improving the fidelity of hash-based sparse attention. Extensive experiments across diverse LLMs and benchmarks demonstrate that HHR achieves superior performance over existing methods. For example, on LongBench, HHR improves the average score by 1.10 points and, at a context length of 128K, achieves up to a 3.30x decoding speedup and a 2.83x end-to-end speedup for Llama-3.1-8B-Instruct. The code is publicly available at https://github.com/lianjunl13-sudo/HHR.

**Key innovations.**

- Diagnoses the core defect of hash-based retrieval: Hamming distance discards magnitude, while QK logits depend jointly on directional similarity *and* feature magnitudes — producing both false-positive retrieval of low-logit keys and false-negative omission of high-logit keys.
- Two-stage coarse-to-fine fix. **Geometry-Aware Key Routing** learns a head-wise orthogonal transformation to redistribute magnitudes and derive discriminative page-level logit bounds, enabling safe pruning of low-logit keys. **Learned Hash Projection** then learns a head-wise projection space aligning Hamming distance with true QK relevance ranking for fine-grained retrieval.
- LongBench average +1.10 points; at 128K context, up to **3.30× decoding** and **2.83× end-to-end** speedup for Llama-3.1-8B-Instruct.
- Reported as improving fidelity of hash-based sparse attention rather than trading it away, across diverse LLMs and benchmarks; code released.

---

### 25. Universal Byte-Level Encoding: UTF-8/UTF-16 Routing to Reduce Cross-Script Token-Budget Disparities

- **arXiv:** [2610.01984](https://arxiv.org/abs/2610.01984) · submitted 2026-10-01 · primary category `cs.CL` · all categories: `cs.CL`, `cs.LG`
- **Authors:** Hyunsik Kim; Youngmoon Jung
- **Institution / company:** Samsung Research
- **Affiliation evidence:** verified from author block
- **Author comment:** Accepted to NeurIPS 2026

**Abstract.** Byte-level byte-pair encoding (BBPE) tokenizers are attractive for multilingual large language models (LLMs) because they cover all Unicode text. In UTF-8-based BBPE, however, many scripts start from a higher fallback cost than English: when no learned merges can be applied, a multibyte character requires multiple byte-derived symbols. We call this worst-case pre-merge cost the encoding floor. A higher floor can increase token counts and per-request cost and shrink usable context. Changing the text encoding can reduce this gap, but a single global encoding can make already-efficient English spans more expensive in mixed-script text. We propose Universal Byte-Level Encoding (UBE), a dual-alphabet tokenizer that keeps 1-2-byte UTF-8 characters on the UTF-8 path while routing 3-4-byte UTF-8 characters through UTF-16. This lowers the encoding floor for 3-byte Basic Multilingual Plane (BMP) characters in scripts with high token premiums (token counts relative to English) without raising it for already-efficient spans in mixed-script text. UBE changes only the byte representation presented to byte-pair encoding (BPE); the merge rule remains standard, and exact decoding is preserved. UBE also composes with alternative boundary policies and morphology-based representations. In a Unicode 17 audit, UBE exactly round-trips all Unicode scalar values and all inputs in the official normalization, grapheme-break, and emoji test suites. Across intrinsic evaluations, UBE lowers dispersion in English-normalized token-count ratios, reducing cross-lingual token-budget disparity. In multilingual language model (LM) experiments, UBE matches BBPE's LM quality. In the main multilingual settings, UBE reduces token counts most for high-premium scripts and slightly lowers English token counts, yielding more usable context under fixed token budgets and faster prompt processing in content-matched benchmarks.

**Key innovations.**

- Introduces the **encoding floor**: in UTF-8 byte-level BPE, scripts for which no learned merge applies start from a worst-case pre-merge cost of one symbol per byte, which inflates token counts and per-request cost and shrinks usable context.
- Shows the obvious fix has a countervailing cost — a single global encoding change makes already-efficient English spans *more* expensive in mixed-script text.
- **UBE** is a dual-alphabet tokenizer: 1–2-byte UTF-8 characters stay on the UTF-8 path while 3–4-byte characters route through UTF-16, lowering the floor for high-token-premium BMP scripts without raising it for efficient spans. Only the byte representation fed to BPE changes — merge rules stay standard and decoding stays exact.
- Unicode 17 audit: exact round-trip of all Unicode scalar values and all inputs in the official normalization, grapheme-break and emoji test suites; matches BBPE's LM quality while reducing cross-lingual token-budget dispersion. **Accepted to NeurIPS 2026.**

---

## Recommendation, Sequential Modeling, Advertising & CTR (7)

### 26. AgentWebRec: Compact Evidence Fusion over the Agent Web for Personalized Recommendation

- **arXiv:** [2610.01705](https://arxiv.org/abs/2610.01705) · submitted 2026-10-01 · primary category `cs.IR` · all categories: `cs.IR`
- **Authors:** Haoran Qiang; Guannan Liu; Liang Zhang; Junjie Wu
- **Institution / company:** MIIT Key Laboratory of Data and Decision Intelligence, Beihang University; The Hong Kong University of Science and Technology (Guangzhou)
- **Affiliation evidence:** verified from author block

**Abstract.** LLM-based personal agents are emerging as persistent carriers of user semantics and intermediaries between users and recommendation platforms, maintaining richer user knowledge locally. As agents interact with one another, the conventional \textit{User--Platform} relation evolves into a \textit{User--Agent Web--Platform} information pathway, enabling distributed user-side information to complement item-side information. This new pathway, however, defies conventional recommendation: evidence is scattered across mutually opaque agents and reachable only through bounded queries, only a small portion of it is relevant to the current recommendation decision, and the responses returned by different agents are semantically heterogeneous. We therefore recast recommendation over the agent web as a \emph{task-time evidence acquisition and fusion} problem under a finite evidence budget by deciding what to ask and what to keep, rather than learning from aggregated data. We propose AgentWebRec, a user-agent-oriented framework that progressively acquires and fuses distributed evidence for each user-item decision while keeping underlying agent memories local. It grounds each decision in platform-provided item semantics and task-relevant evidence from the target user agent's private memory, and conditionally queries neighboring user agents for complementary preference patterns when local evidence is insufficient. Experiments on four InstructRec datasets show that AgentWebRec consistently outperforms baseline recommenders, and ablations verify that the evidence layers contribute complementary gains.

**Key innovations.**

- Reframes the topology: persistent user-side LLM agents turn the User–Platform relation into a **User–Agent Web–Platform** pathway, so distributed user-side information can complement item-side information.
- Names three obstacles conventional recommendation cannot absorb: evidence is scattered across mutually opaque agents reachable only through bounded queries, only a small portion is relevant to the current decision, and responses from different agents are semantically heterogeneous.
- Recasts recommendation as **task-time evidence acquisition and fusion under a finite evidence budget** — deciding what to ask and what to keep rather than learning from aggregated data — while keeping the underlying agent memories local.
- Each decision is grounded in platform item semantics plus task-relevant evidence from the target user agent's private memory, conditionally querying neighbouring user agents only when local evidence is insufficient; consistent gains over baseline recommenders on four InstructRec datasets, with ablations showing the evidence layers contribute complementary gains.

---

### 27. VirusCascade: Hijacking Collaborative Reflection in LLM-Powered Recommender Agents

- **arXiv:** [2609.38270](https://arxiv.org/abs/2609.38270) · submitted 2026-09-29 · primary category `cs.CR` · all categories: `cs.CR`, `cs.LG`, `cs.MA`
- **Authors:** Yurong Hao; Wen Zhou; Guowei Guan; Tiantong Wu; Fuyao Zhang; Wei Yang Bryan Lim
- **Institution / company:** Nanyang Technological University (College of Computing and Data Science)
- **Affiliation evidence:** verified from author block
- **Author comment:** Accepted by NDSS 2027

**Abstract.** Advancing beyond traditional static scoring models, LLM-powered agentic recommender systems (LLM-ARS) instantiate users and items as autonomous agents, whose semantic states are dynamically refined through a recurrent process known as collaborative reflection. While this mechanism improves recommendation quality, it simultaneously introduces a systemic vulnerability: adversarial evidence injected into a single agent can be rationalised into a legitimate preference narrative, written back into memory, and propagated to other agents through interaction contexts. We term the local rationalisation process reflection laundering, and its system-wide escalation through collaborative reflection collaborative-reflection hijacking. Existing attacks on recommender systems, whether based on interaction-level data poisoning or text-level adversarial perturbations, assume static pipelines and thus cannot exploit this recurrent, multi-agent amplification pathway. To bridge this gap, we first conduct a controlled vulnerability analysis that establishes two exploitable properties underlying collaborative-reflection hijacking: reflective persistence and cross-agent propagation. Then building on these findings, we propose VirusCascade, the first black-box targeted promotion attack that jointly shapes semantic and structural attack surfaces: the former ensures the target item is naturally rationalised as satisfying broad user preferences, the latter positions it for system-wide propagation. Extensive experiments on four real-world datasets across diverse LLM-ARS architectures demonstrate that VirusCascade consistently achieves state-of-the-art targeted exposure under evaluated stealth constraints, reaching a mean E@20 of 0.384 and surpassing the strongest baseline by an absolute margin of +0.185.

**Key innovations.**

- Identifies an attack surface that does not exist for static scoring models: LLM-powered agentic recommenders (LLM-ARS) instantiate users and items as autonomous agents whose semantic states are refined recurrently through **collaborative reflection** — the very mechanism that improves quality also enables propagation.
- Names the two mechanisms: *reflection laundering* (adversarial evidence injected into one agent gets rationalized into a legitimate preference narrative and written back to memory) and *collaborative-reflection hijacking* (system-wide escalation through interaction contexts).
- Establishes two exploitable properties by controlled analysis — reflective persistence and cross-agent propagation — then builds **VirusCascade**, the first black-box targeted-promotion attack that jointly shapes the semantic surface (target naturally rationalized as broadly preferred) and the structural surface (positioned for system-wide propagation).
- Mean E@20 of 0.384, **+0.185 absolute** over the strongest baseline, across four real-world datasets and diverse LLM-ARS architectures under evaluated stealth constraints. **Accepted at NDSS 2027.**

---

### 28. FairDiff: Mitigating the Self-Reinforcing Matthew Effect in Diffusion Recommender Models

- **arXiv:** [2609.36671](https://arxiv.org/abs/2609.36671) · submitted 2026-09-29 · primary category `cs.AI` · all categories: `cs.AI`
- **Authors:** Song-Li Wu; Xianquan Wang; Zhaocheng Du; Weinan Gan; Jingyi Wang
- **Institution / company:** Tsinghua University; Huawei Noah's Ark Lab; University of Science and Technology of China
- **Affiliation evidence:** verified from the paper's numbered front-matter institution list

**Abstract.** While the "Matthew Effect" and filter bubbles are widely recognized outcome-level biases in recommender systems, we reveal that Diffusion Recommender Models (DRMs) uniquely compound this issue through their generative dynamics. Rather than merely inheriting data imbalances, DRMs trigger a self-reinforcing amplification of popularity bias. We identify that this phenomenon is driven by two compounding mechanisms. First, while optimization loss is universally dominated by high-frequency items across recommenders, DRMs suffer from a unique structural prior mismatch during generation. Because the forward terminal distribution of long-tailed data deviates significantly from the standard Gaussian prior, reverse sampling trajectories inherently collapse toward high-density popular items, fundamentally suppressing niche item generation. To dismantle this self-reinforcing loop, we propose FairDiff, a plug-and-play fairness-aware diffusion framework. To overcome the popularity-dominated loss, we introduce Popularity Condition Guidance (PCG). Rather than altering the training objective, PCG acts as an inference-time distributional reweighting mechanism, mathematically reshaping the score-based gradient field to penalize high-popularity regions and guide trajectories toward niche semantics. Furthermore, we design a Semantic Calibration (SC) Module to bridge the prior mismatch, aligning the forward and reverse distributions via one-step optimal transport. Comprehensive evaluations demonstrate that FairDiff achieves state-of-the-art performance while effectively mitigating the self-reinforcing Matthew Effect, highlighting its value as a general framework for DRMs.

**Key innovations.**

- Makes a mechanism claim rather than an inheritance claim: diffusion recommender models do not merely inherit popularity imbalance from data, they *self-reinforce* it through their generative dynamics.
- Two compounding causes. The optimization loss is universally dominated by high-frequency items across all recommenders; but DRMs additionally suffer a structural **prior mismatch** — the forward terminal distribution of long-tailed data deviates from the standard Gaussian prior, so reverse sampling trajectories inherently collapse toward high-density popular items and suppress niche generation.
- **Popularity Condition Guidance** acts purely at inference time (the training objective is untouched), reshaping the score-based gradient field to penalize high-popularity regions and steer trajectories toward niche semantics.
- A **Semantic Calibration** module closes the prior mismatch by aligning forward and reverse distributions through one-step optimal transport; plug-and-play, with state-of-the-art results claimed while mitigating the Matthew Effect.

---

### 29. Inherit4Rec: Parameter Inheritance for Efficient Scaling of Recommendation Models

- **arXiv:** [2609.23111](https://arxiv.org/abs/2609.23111) · submitted 2026-09-19 · primary category `cs.IR` · all categories: `cs.IR`
- **Authors:** Ruihao Zhang; Bo Chen; Xiao Wang; Jinlong Jiao; Tijian Hu; Qinglin Jia; Xiuqiang He; Xiangyu Zhao; Chaoyi Ma; Ruiming Tang; Wenwu Ou
- **Institution / company:** Kuaishou Technology; Shenzhen Technology University; City University of Hong Kong
- **Affiliation evidence:** verified from author block

**Abstract.** Scaling model capacity has emerged as an effective approach to overcoming performance bottlenecks in industrial recommender systems. However, repeatedly training larger dense models from scratch demands substantial data and time, while their growing computation conflicts with the strict serving budgets of industrial systems. Parameter inheritance provides a promising route for both dense model growth and sparse conversion, yet existing methods are primarily designed for static corpora and can suffer sharp performance drops under dynamically evolving recommendation data. To address these challenges, we propose Inherit4Rec, a parameter-inheritance framework that supports both Dense-to-Dense (D2D) growth and Dense-to-Sparse (D2S) conversion. Inherit4Rec-D2D combines hybrid growth with asymmetric training to preserve the forward function at expansion and maintain update continuity. Inherit4Rec-D2S constructs SMoE networks through co-activation-aware partitioning and a load-balancing loss, preserving dense-model capabilities while promoting balanced expert activation. Experiments on KuaiRand-1K and an industrial short-video recommendation dataset show that both transformations consistently outperform the evaluated inheritance baselines across all prediction objectives. These results demonstrate the effectiveness of Inherit4Rec for continual capacity expansion and computation-efficient sparse conversion in industrial recommender systems.

**Key innovations.**

- Frames the industrial constraint precisely: scaling recommender capacity means repeatedly training larger dense models from scratch, and their growing compute conflicts with strict industrial serving budgets — so growth must come by *inheriting* parameters, both for dense growth and for sparse conversion.
- Identifies the gap: existing inheritance methods are designed for static corpora and suffer sharp drops under dynamically evolving recommendation data.
- **D2D** combines hybrid growth with asymmetric training to preserve the forward function at expansion and maintain update continuity. **D2S** constructs SMoE networks via co-activation-aware partitioning plus a load-balancing loss, preserving dense-model capability while promoting balanced expert activation.
- Both transformations consistently beat the evaluated inheritance baselines across all prediction objectives on KuaiRand-1K and an industrial short-video dataset — a rare case of a capacity-scaling result reported on a named production dataset.

---

### 30. Nash Equilibria in Auctions with Pacing Strategies: Complexity and Inefficiency

- **arXiv:** [2609.34515](https://arxiv.org/abs/2609.34515) · submitted 2026-09-28 · primary category `cs.GT` · all categories: `cs.GT`, `cs.CC`
- **Authors:** Aris Filos-Ratsikas; Charalampos Kokkalis; Mohamad Latifian
- **Institution / company:** Imperial College London; University of Edinburgh
- **Affiliation evidence:** verified from author block
- **Author comment:** 29 pages, to appear in The 22nd Conference on Web and Internet Economics (WINE 2026)

**Abstract.** We introduce and study Auctions with Pacing Strategies (APS) games, a full-information model in which utility-maximizing bidders compete across many simultaneous first-price auctions, each choosing a single pacing multiplier that uniformly scales their values into bids. We settle three central questions. First, we show that there are instances that admit no approximate pure Nash equilibria. Then, we prove that the problem of deciding whether an APS game admits an (approximate) equilibrium is NP-complete in general, but can be solved in polynomial time if either the number of bidders or the number of items is fixed. Finally, when an equilibrium does exist, we characterize its inefficiency exactly, showing that both the Price of Anarchy and the Price of Stability equal $\frac{e}{e-1}$.

**Key innovations.**

- Formal model with direct ad-platform reading: full-information **Auctions with Pacing Strategies (APS)** — utility-maximizing bidders compete across many simultaneous first-price auctions, each choosing a single pacing multiplier that uniformly scales their values into bids, so pacing is the only strategic degree of freedom.
- Settles three questions. (1) Some instances admit **no approximate pure Nash equilibrium at all**. (2) Deciding whether an APS game admits an (approximate) equilibrium is NP-complete in general, but polynomial if either the number of bidders or the number of items is fixed.
- Exact inefficiency characterization when equilibria exist: **Price of Anarchy = Price of Stability = e/(e−1) ≈ 1.582**.
- Practical reading: budget-pacing constraints make equilibrium-based ad allocation structurally hard, and that is a mechanism-design cost rather than an implementation defect. **To appear at WINE 2026.**

---

### 31. FARE: Deep Reinforcement Learning For Fair Exposure Constrained Uncertainty Aware Financial Content Personalization

- **arXiv:** [2609.31890](https://arxiv.org/abs/2609.31890) · submitted 2026-09-25 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`, `cs.IR`
- **Authors:** Arundeep Chinta; Lucas Vinh Tran; Jay Katukuri
- **Institution / company:** JPMorganChase (Palo Alto, CA and London)
- **Affiliation evidence:** verified from author block
- **Author comment:** Extended version of a paper accepted to the Advances in Financial AI: Towards Agentic and Responsible Systems Workshop at ICLR 2026

**Abstract.** Content personalization systems in financial services must ensure fair exposure across diverse offerings-a requirement driven by contractual obligations and the need to prevent "rich-get-richer" dynamics where content with high click-through rate (CTR) dominates while other relevant products receive minimal visibility. Share of Voice (SOV) constraints, which guarantee each content category a target fraction of top-position exposure, address this by promoting product diversity and balanced user discovery. While re-ranking layers atop CTR models are common in practice, we propose two key novelties: (1) framing SOV-constrained ranking as a deep reinforcement learning problem analogous to constrained trade execution in algorithmic finance, and (2) explicitly incorporating CTR prediction uncertainty into the agent's state space and policy design-enabling larger ranking adjustments for high-uncertainty predictions where deviation from CTR-optimal ordering is less costly. We introduce FARE (Fair Ranking Executor), a modular uncertainty-aware execution layer that translates any black-box CTR model's predictions into SOV-fair rankings without retraining the underlying model. Our uncertainty-weighted proportional control policy (FARE-PC) and learned neural policies (FARE-ES, FARE-PPO) demonstrate that uncertainty-aware approaches can substantially reduce SOV deviation from fairness targets while minimizing engagement loss, with gradient-free evolution strategies outperforming policy gradient methods on synthetic data and the ordering reversing on KuaiRand-Pure.

**Key innovations.**

- Frames Share-of-Voice-constrained ranking as **constrained trade execution** — the finance analogy is the contribution, not just the algorithm: SOV guarantees each content category a target fraction of top-position exposure, directly countering the rich-get-richer dynamic where high-CTR content crowds out relevant products.
- Puts **CTR prediction uncertainty into the agent's state space and policy**, so ranking may deviate further from CTR-optimal order exactly where predictions are uncertain and deviating is cheaper.
- **FARE** is a modular, uncertainty-aware execution layer that converts *any* black-box CTR model's predictions into SOV-fair rankings with no retraining; ships an uncertainty-weighted proportional-control policy (FARE-PC) and learned neural policies (FARE-ES, FARE-PPO).
- Reduces SOV deviation substantially while minimizing engagement loss — and the method ranking **reverses** between synthetic data (evolution strategies beat policy gradient) and KuaiRand-Pure. Extended version of a Financial-AI-workshop paper.

---

### 32. Data Processing for Offline Evaluation in Recommender Systems: a Survey

- **arXiv:** [2609.31696](https://arxiv.org/abs/2609.31696) · submitted 2026-09-18 · primary category `cs.IR` · all categories: `cs.IR`, `cs.LG`
- **Authors:** Alberto Carlo Maria Mancino; Angela Di Fazio; Danilo Danese; Matteo Attimonelli; Daniele Malitesta; Antonio Ferrara; Claudio Pomo; Tommaso Di Noia
- **Institution / company:** Politecnico di Bari; LUISS Guido Carli University; University of Cambridge; Sapienza Università
- **Affiliation evidence:** verified from the paper's author-affiliation listing

**Abstract.** Offline evaluation is the dominant experimental paradigm in recommender systems research, enabling reproducible and cost-effective comparisons on historical interaction data. Yet, while considerable attention has been devoted to recommendation models and evaluation methodologies, the data processing decisions that precede model training have received less scrutiny. These decisions determine the information available to recommendation algorithms and can affect the comparability and reproducibility of experimental results. This survey provides a systematic, cross-domain characterisation of data processing practices for the offline evaluation of recommender systems. We examine the data-centric pipeline, from dataset selection and interaction representation to data preparation, multimodal feature extraction, and train-validation-test splitting. Our analysis spans recommendation paradigms, including collaborative, sequential, session-based, graph-based, knowledge-aware, context-aware, multimodal, federated, cross-domain, contrastive-learning, and LLM-based recommendation. Beyond reviewing existing practices, we introduce a unified framework and taxonomy for describing data transformations and feature-extraction strategies, distinguishing data preparation from the extraction of representations from multimodal side information. Our empirical analysis reveals a landscape dominated by a narrow set of dataset-level transformations, particularly support-driven filtering, while representation-dependent transformations remain less common. We further identify substantial heterogeneity in how auxiliary information is prepared and represented, as well as inconsistencies in the specification of data splitting protocols, where similar labels may conceal different experimental conditions.

**Key innovations.**

- Points at the least-examined step in the field: the data-processing decisions that precede training determine what information is available to the algorithm and whether results are comparable at all, yet attention goes to models and metrics instead.
- Systematic cross-domain characterization of the data-centric pipeline — dataset selection, interaction representation, data preparation, multimodal feature extraction, train/validation/test splitting — spanning collaborative, sequential, session-based, graph, knowledge-aware, context-aware, multimodal, federated, cross-domain, contrastive and LLM-based recommendation.
- Introduces a unified taxonomy that explicitly separates **data preparation** from **extraction of representations from multimodal side information** — two things the literature routinely conflates.
- Two empirical findings worth acting on: practice is dominated by a narrow set of dataset-level transforms (support-driven filtering) while representation-dependent transforms remain uncommon; and split protocols are specified so inconsistently that identical labels can conceal different experimental conditions — i.e. part of the field's irreproducibility is a data-processing artifact.

---

## Reinforcement Learning & World Models (6)

### 33. MA-JEPA: Joint-Embedding World Models for Multi-Agent Reinforcement Learning

- **arXiv:** [2609.33563](https://arxiv.org/abs/2609.33563) · submitted 2026-09-27 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`, `cs.MA`
- **Authors:** Brandon Gary Kaplowitz; Osaze James Obahor; Christian Schroeder de Witt
- **Institution / company:** University of Oxford (Department of Engineering Science)
- **Affiliation evidence:** verified from author block

**Abstract.** World models improve sample efficiency by training policies on imagined trajectories, but their usefulness depends on learning representations that capture the information needed for future control. We study whether self-supervised joint-embedding prediction (JEPA) can provide this learning signal for multi-agent reinforcement learning. We introduce MA-JEPA, a stochastic world model that replaces observation reconstruction with prediction of target representations, enabling model-based multi-agent reinforcement learning with centralized training and decentralized execution. A categorical latent state and a causal Transformer are trained with posterior and action-conditioned dynamics prediction objectives and are then used for actor-critic learning from latent imagination. A training-only joint predictor conditions on all agents' local states and actions to predict each agent's next local observation embedding. These predictions are passed through the same local posterior used during real interaction with a centralized critic that is used only for value learning, with execution remaining decentralized. Our experiments show that this architecture performs strongly on SMAC, matching or exceeding the strongest reported comparator mean win rate on four of eight evaluated maps.

**Key innovations.**

- Asks whether self-supervised joint-embedding prediction (JEPA) can supply the representation-learning signal that makes a world model useful for *multi-agent* RL — replacing observation reconstruction with prediction of target representations.
- Architecture: categorical latent state plus a causal Transformer trained with posterior and action-conditioned dynamics objectives, then used for actor-critic learning from latent imagination.
- CTDE is enforced structurally: a training-only joint predictor conditions on all agents' local states and actions to predict each agent's next local observation embedding, and those predictions pass through the *same* local posterior used during real interaction; the centralized critic is used only for value learning and execution stays decentralized.
- Matches or exceeds the strongest reported comparator mean win rate on four of eight evaluated SMAC maps.

---

### 34. JEPA-TTT: Persistent Test-Time Training of Latent World Models for Planning under Dynamics Shifts

- **arXiv:** [2610.00722](https://arxiv.org/abs/2610.00722) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`
- **Authors:** Zheyuan Zhang; Suyu Ye; Nakul Agarwal; Hossein Nourkhiz Mahjoub; Ehsan Moradi Pari; Daniel Khashabi; Tianmin Shu; Vaishnav Tadiparthi
- **Institution / company:** Honda Research Institute USA; Johns Hopkins University
- **Affiliation evidence:** verified from the paper's numbered front-matter institution list
- **Author comment:** Accepted to World Models in Physical AI Workshop @ NeurIPS 2026 | Project page: https://jepa-ttt.github.io/

**Abstract.** World models enable agents to plan by predicting future states of the environment, but their predictions can become unreliable when test-time dynamics differ from those seen during training. We present JEPA-TTT, which adapts the latent dynamics predictor of a pretrained action-conditioned Joint-Embedding Predictive Architecture world model throughout test time. Self-supervised updates accumulate across episodes, while the visual encoder and reward head remain fixed, preserving the pretrained representation and task objective. Planning requires neither a goal image nor online environment reward. JEPA-TTT uses dense replay, which forms prediction windows at every temporal offset, retains them in a growing buffer, and samples minibatches from that buffer for predictor updates. Across eight dynamics shifts in four continuous-control environments, JEPA-TTT improves planning on every shift. After 500 test-time episodes, it reduces autoregressive latent prediction error by 83% on average and improves planning performance by 153% over the frozen JEPA world model. These results show that persistent self-supervised test-time training can adapt a pretrained latent world model under changed dynamics.

**Key innovations.**

- Targets the deployment failure: world-model predictions become unreliable when test-time dynamics differ from training dynamics.
- **JEPA-TTT** adapts only the latent dynamics predictor of a pretrained action-conditioned JEPA world model, continually through test time; the visual encoder and reward head stay frozen, preserving both the pretrained representation and the task objective.
- Planning needs **neither a goal image nor online environment reward**; dense replay forms prediction windows at every temporal offset, retains them in a growing buffer and samples minibatches for predictor updates.
- Across eight dynamics shifts in four continuous-control environments it improves planning on *every* shift; after 500 test-time episodes, autoregressive latent prediction error falls **83%** on average and planning performance improves **153%** over the frozen model. **NeurIPS 2026 World Models in Physical AI Workshop.**

---

### 35. Semifactual Credit-Augmented Policy Optimization

- **arXiv:** [2609.40360](https://arxiv.org/abs/2609.40360) · submitted 2026-09-30 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`, `cs.CL`
- **Authors:** Junshu Pan; Zhizhang Fu; Shulin Huang; Yiran Ding; Zifan Cheng; Wenqi Shao; Qiaosheng Zhang; Yue Zhang
- **Institution / company:** Zhejiang University; Westlake University; Shanghai Innovation Institute; Shanghai AI Laboratory
- **Affiliation evidence:** verified from author block

**Abstract.** Reinforcement learning with verifiable rewards (RLVR) has improved the reasoning capabilities of large language models (LLMs), yet their predictions remain sensitive to task-irrelevant prompt features. We investigate this sensitivity through semifactual prompt interventions that preserve the underlying problem and its answer. Our analysis reveals substantial variation in token-level sensitivity and shows that suppressing high-drift token candidates during decoding improves reasoning accuracy without updating model weights. These findings highlight a limitation of Group Relative Policy Optimization (GRPO), which assigns the same outcome-derived advantage to every response token and may reinforce potential spurious dependence alongside useful reasoning. Motivated by this observation, we introduce Semifactual Credit-Augmented Policy Optimization (SCAPO), a causally inspired variant of GRPO that incorporates semifactual stability into token-level credit assignment. SCAPO measures token probability drift for fixed responses under semifactual interventions and uses normalized stability scores to reduce advantages for relatively unstable tokens during early training, while granting no additional credit for stability alone. On Qwen3-4B-Base and Qwen3-1.7B-Base, SCAPO improves AIME 2024-2026 accuracy over GRPO by 5.63 and 4.17 percentage points, respectively. At both model scales, SCAPO achieves the best results on most evaluated mathematics benchmarks and all evaluated out-of-distribution benchmarks among the compared methods. These results suggest that semifactual stability provides an effective training signal for improving reasoning and generalization through finer-grained credit assignment in RLVR. The code is available at https://github.com/DtYXs/SCAPO.

**Key innovations.**

- Diagnostic first: RLVR-trained models stay sensitive to task-irrelevant prompt features, exposed via **semifactual interventions** that preserve the underlying problem and its answer; suppressing high-drift token candidates *at decoding time* improves reasoning accuracy with **no weight updates**.
- That localizes a GRPO defect: one outcome-derived advantage applied to every response token can reinforce spurious dependence alongside useful reasoning.
- **SCAPO** adds semifactual stability to token-level credit assignment — measures token probability drift for fixed responses under semifactual interventions, uses normalized stability scores to reduce advantages for relatively unstable tokens early in training, and deliberately grants **no extra credit for stability alone**.
- AIME 2024–2026 over GRPO: **+5.63** points on Qwen3-4B-Base and **+4.17** on Qwen3-1.7B-Base; best results on most evaluated mathematics benchmarks and on *all* evaluated out-of-distribution benchmarks among the compared methods.

---

### 36. FERPO: Forward Entropy-Regularized Policy Optimization

- **arXiv:** [2610.02198](https://arxiv.org/abs/2610.02198) · submitted 2026-10-01 · primary category `cs.LG` · all categories: `cs.LG`, `cs.AI`, `cs.RO`, `stat.ML`
- **Authors:** Sebastian Sanokowski; Alireza Sarmadi; Majid Khadiv
- **Institution / company:** Technical University of Munich (MIRMI; ATARI Lab)
- **Affiliation evidence:** verified from author block
- **Author comment:** Code: https://github.com/Atarilab/FERPO

**Abstract.** Several state-of-the-art methods for online reinforcement learning in continuous control improve policies using action gradients of a learned critic. However, critics are typically trained to predict returns, and accurate value predictions do not necessarily yield accurate action derivatives, potentially leading to unreliable policy updates. We propose Forward Entropy-Regularized Policy Optimization (FERPO), an on-policy maximum entropy reinforcement learning algorithm that performs policy improvement using critic values without differentiating the critic with respect to actions. FERPO derives an optimal target action distribution from a policy-improvement objective regularized by entropy and Kullback-Leibler (KL) divergence. We then fit the actor to this target by minimizing a forward-KL objective, estimated using self-normalized importance sampling (SNIS) with actions drawn from the rollout policy. By limiting the target distribution's deviation from the rollout policy, the KL regularization helps keep these importance weights well behaved. In contrast to reverse-KL objectives, which can favor a subset of the target distribution's modes, the forward-KL objective encourages coverage of multiple high-value modes and thereby promotes exploration. Experiments and ablations on MuJoCo Playground and ManiSkill show competitive performance and sample-efficiency gains. Computational benchmarks also demonstrate faster actor updates than Relative Entropy Pathwise Policy Optimization (REPPO).

**Key innovations.**

- Objects to standard practice: critics are trained to predict *returns*, and accurate value prediction does not imply accurate action *derivatives* — so differentiating a learned critic with respect to actions can yield unreliable policy updates.
- **FERPO** performs policy improvement **without differentiating the critic with respect to actions**: it derives an optimal target action distribution from an entropy- and KL-regularized policy-improvement objective, then fits the actor to that target by minimizing a forward-KL objective estimated with self-normalized importance sampling over rollout-policy actions.
- Two consequences follow from the design: bounding the target's deviation from the rollout policy keeps importance weights well-behaved, and forward KL — unlike reverse KL — encourages coverage of multiple high-value modes rather than collapsing onto a subset of modes.
- Competitive performance and sample-efficiency gains on MuJoCo Playground and ManiSkill, with faster actor updates than REPPO.

---

### 37. Same Reward, Different Skills: When Multimodal RL Learns to Look

- **arXiv:** [2610.01908](https://arxiv.org/abs/2610.01908) · submitted 2026-10-01 · primary category `cs.LG` · all categories: `cs.LG`
- **Authors:** Haocun Ye; Xinlong Jiang; Qile Chen; Bingyu Wang; Teng Zhang; Shubai Chen; Tingyu Wu; Zhenkun Zheng; Yiqiang Chen
- **Institution / company:** University of the Chinese Academy of Sciences; Institute of Computing Technology, Chinese Academy of Sciences; Independent Researcher
- **Affiliation evidence:** verified from author block

**Abstract.** Reinforcement learning with verifiable rewards (RLVR) improves vision-language benchmark scores even without visual information during training. With images at test, blind-trained models recover roughly half of the real-image gain at 3B and nearly four fifths at 7B. Prolonged real-image training can erode grounding while benchmark gains persist. Both findings expose the same gap: an image in the prompt is not an image in the learning signal. Our design rule, visual resolvability, asks that visual evidence be necessary for a correct answer and that the task remain learnable. We test it on counterfactual coordinate scenes in which the question stays fixed and the target is never named, so a correct answer requires finding the target in the image. With standard GRPO and correctness-and-format rewards, a 7B model raises its accuracy at finding the target (discovery) from 0.425 to 0.875 on held-out scenes denser than any it trained on, and it improves on question types it never trained on. Two controls locate the source of the gain. Replacing test images with gray canvases drops discovery to zero; training on gray canvases instead, at matched step 30 and in each of four seeds, yields essentially none of the gain even when the model is then tested with real images. The learned skill carries over to grounding tasks built independently of the training corpus. A caption that answers the training question, added to the same images, reward and budget, cuts the gain by nearly two thirds. Changing what reward requires changes what RL learns.

**Key innovations.**

- Two findings that indict RLVR for multimodal models: benchmark gains occur **even without visual information during training** — blind-trained models recover roughly half the real-image gain at 3B and nearly four fifths at 7B — and prolonged real-image training erodes grounding while benchmark gains persist.
- Unifies both under one diagnosis: *an image in the prompt is not an image in the learning signal*.
- Design rule **visual resolvability**: visual evidence must be necessary for a correct answer, and the task must remain learnable. Tested on counterfactual coordinate scenes where the question is fixed and the target is never named, so a correct answer requires finding it in the image.
- A 7B model raises discovery accuracy 0.425 → 0.875 on held-out scenes denser than any it trained on, and transfers to independently built grounding tasks. Two controls pin the source: gray canvases at test drop discovery to zero; gray-canvas training yields essentially none of the gain across four seeds even when later tested with real images; and a caption that answers the training question cuts the gain by nearly two thirds.

---

### 38. Dependency-Aware Reward Shaping for Agentic Reinforcement Learning

- **arXiv:** [2610.01207](https://arxiv.org/abs/2610.01207) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`
- **Authors:** Ziyi Chen; Yan Zhang; Jianhui Wei; Daoan Zhang; Zuozhu Liu
- **Institution / company:** University of Illinois Urbana-Champaign; National University of Singapore; Zhejiang University; University of Rochester
- **Affiliation evidence:** verified from author block

**Abstract.** When training large language models with reinforcement learning, terminal rewards provide little guidance about which steps matter. Common methods for assigning step credit overlook that work built on uncorrected mistakes is wasted while independent work remains valid. With only a final success/failure reward, every step in a failed episode has zero total future reward, even when it made progress. We propose Dependency-Aware Reward Shaping (DARS), which represents task progress as predicates linked by prerequisite relations and assigns step-level credit over the dependency graph. An annotator marks which predicates each step verifies, invalidates, or repairs. Verified predicates are discounted according to graph distance from the nearest broken prerequisite, while independent predicates are unaffected. Repairs update these weights based on any errors that remain; invalidated predicates need re-verification to regain credit. A fixed potential converts these annotations into signed per-step rewards. A common reward and annotation interface allows DARS to integrate with a range of reasoning and agentic training methods, such as GiGPO and ARPO/AEPO, without changing their rollout strategies or optimizers. Across five task families and models from 1.5B to 8B, DARS improves success by up to 10 points over GiGPO trained with the same budget and harness (ALFWorld), raises the WebShop task score and Search-R1 QA accuracy, complements AEPO's entropy-based training on AIME24/25 with a Python interpreter, and exceeds OmniOPD in controlled tool-free reasoning comparisons at 1.7B and 4B. Ablations show that step-level credit, dependency attenuation, and graph topology each contribute. On ALFWorld, a distilled 8B annotator matches the API annotator, enabling DARS to run efficiently without a frontier judge. Code is available at https://github.com/JianhuiWei7/DARS.

**Key innovations.**

- Names the credit-assignment gap two ways: with only terminal reward every step in a failed episode has zero future reward even when it made progress; and existing step-credit schemes ignore that work built on an uncorrected mistake is wasted while independent work remains valid.
- **DARS** represents task progress as predicates linked by prerequisite relations; an annotator marks which predicates each step verifies, invalidates or repairs. Verified predicates are discounted by graph distance to the nearest broken prerequisite, independent predicates are unaffected, and invalidated predicates need re-verification to regain credit.
- A fixed potential converts annotations into signed per-step rewards behind a common reward/annotation interface, so it drops into GiGPO and ARPO/AEPO without changing their rollout strategies or optimizers.
- Up to **+10 points** success over budget- and harness-matched GiGPO on ALFWorld; raises WebShop score and Search-R1 QA accuracy, complements AEPO's entropy-based training on AIME24/25, and exceeds OmniOPD in controlled tool-free reasoning at 1.7B and 4B. A distilled 8B annotator matches the API annotator, removing the frontier-judge dependency.

---

## Games, World Models & Interactive Generation (3)

### 39. RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement

- **arXiv:** [2609.39045](https://arxiv.org/abs/2609.39045) · submitted 2026-09-30 · primary category `cs.CL` · all categories: `cs.CL`, `cs.GT`, `cs.LG`, `cs.MA`
- **Authors:** Wenyi Wu; Minghao Fu; Jieyu You; Kun Zhou; Siqi Liu; Aayush Salvi; Yiheng Lin; Ce Zhang; Xiaohan Lan; Jiahui Zhu; Yujie Zhong; Qi She; Biwei Huang
- **Institution / company:** UC San Diego; ByteDance Inc.; Carnegie Mellon University
- **Affiliation evidence:** verified from author block

**Abstract.** Recent advances in large language models have made automatic game generation increasingly feasible, yet reliably improving generated games beyond a playable version remains challenging. Naive iterative refinement can easily overfit a small set of test cases, producing fragile games with unresolved bugs, missing behaviors, and poor generalization to broader player interactions. We introduce RSIGame, an autonomous agentic game development framework with recursive self-improvement. RSIGame organizes development into complementary local and global loops. Concretely, a local explore-diagnose-improve loop broadly explores the executable game, diagnoses and prioritizes discovered issues, and performs evidence-grounded revision, where an evolving checklist continually accumulates new testing and improvement guidance. A global loop tracks overall quality, preserves the best checkpoint, and detects saturation or regression over long-horizon development. Beyond test-time improvement, RSIGame further internalizes successful development experience into the generator through training. Across 140 GameCraft-Bench tasks, two game engines, and five generators, RSIGame consistently improves game quality under matched development budgets. Notably, experience internalization enables Qwen3.8-27B to reach 61.38 on Godot and 58.53 on Phaser, exceeding GPT-5.5 one-shot scores while reducing Qwen's generation tokens by 11 times.

**Key innovations.**

- Targets the failure of naive iterative game refinement: it overfits a small set of test cases, producing fragile games with unresolved bugs and missing behaviours that do not generalize to broader player interaction.
- **RSIGame** separates complementary loops — a *local* explore-diagnose-improve loop that explores the executable game, prioritizes discovered issues and performs evidence-grounded revision against an evolving checklist, and a *global* loop that tracks overall quality, preserves the best checkpoint and detects saturation or regression over long-horizon development.
- Adds a step beyond test-time improvement: successful development experience is internalized into the generator through training.
- Across 140 GameCraft-Bench tasks, two game engines and five generators, consistent gains at matched development budgets; internalization lifts Qwen3.8-27B to 61.38 on Godot and 58.53 on Phaser — above GPT-5.5 one-shot scores — while cutting Qwen's generation tokens **11×**.

---

### 40. ROWBench: Do Video Models Render What the Program Specifies?

- **arXiv:** [2610.02205](https://arxiv.org/abs/2610.02205) · submitted 2026-10-01 · primary category `cs.CV` · all categories: `cs.CV`
- **Authors:** Zheng-Hui Huang; Guixu Lin; Yu-Ju Tsai; Jian-Kai Zhu; Fengbo Lan; Yu-Lun Liu; Yung-Yu Chuang; Kaipeng Zhang; Zhixiang Wang
- **Institution / company:** _(not stated — author block renders an empty affiliation marker)_
- **Affiliation evidence:** LaTeXML rendered only '[' in the affiliation slot; OpenAlex has no institutions. **Not inferred from author names.**

**Abstract.** Programmable world models separate executable dynamics from visual generation, offering a promising foundation for next-generation game engines. However, their visual adherence to explicit rules and interactions remains insufficiently evaluated. Existing benchmarks assess visual quality, controllability, and instruction or physical adherence, but rarely test fidelity to fine-grained, program-specified world events. We introduce PROWBench, comprising 170 programmatically constructed episodes and 600 proxy videos covering diverse scenes and interactions. PROWBench logs entity states and timestamped events, including those outside the camera's field of view, as replayable world records, from which it renders synchronized views and proxy representations. This enables generated videos to be checked against the observable consequences of program execution. An extensible framework constructs scenes, controls behaviors, and can render each camera view in different representations, such as coarse 3D, and bounding boxes. The benchmark covers first- and third-person perspectives, with synchronized multi-view observations available for a subset of episodes. Grounded in these records, PROWBench evaluates entity control, long-horizon memory, and, with two VLM-based metrics, Logic-Render Alignment and Interaction Success Rate, adherence to the prescribed timeline and the visual realization of timestamped engine-recorded events.

**Key innovations.**

- Argues that programmable world models — executable dynamics separated from visual generation, the promised basis for next-generation game engines — are not evaluated for fidelity to **fine-grained, program-specified world events**; existing benchmarks test visual quality, controllability, and instruction or physical adherence.
- Benchmark of 170 programmatically constructed episodes and 600 proxy videos, logging entity states and timestamped events *including those outside the camera's field of view* as replayable world records, from which synchronized views are rendered — so generated video can be checked against the observable consequences of program execution.
- Evaluation dimensions: entity control, long-horizon memory, and two VLM-based metrics — Logic-Render Alignment (adherence to the prescribed timeline) and Interaction Success Rate (visual realization of timestamped engine-recorded events).
- Extensible construction framework, first- and third-person coverage, synchronized multi-view observations on a subset. **Note: the title says ROWBench while the abstract names the benchmark PROWBench — an internal naming inconsistency in v1, worth watching for a v2 rename.**

---

### 41. Code Owns the Simulation, Jev Owns the Evaluation

- **arXiv:** [2610.01834](https://arxiv.org/abs/2610.01834) · submitted 2026-10-01 · primary category `cs.AI` · all categories: `cs.AI`, `cs.LG`
- **Authors:** Yaodong Yang; Hongyao Tang; Yi Ma; Xingyu Fan; Weixun Wang; Jinpeng Li; Tianpei Yang
- **Institution / company:** The Chinese University of Hong Kong; Tianjin University; Shanxi University; Independent Researcher; CAIR, Hong Kong Institute of Science & Innovation, Chinese Academy of Sciences; Nanjing University
- **Affiliation evidence:** verified from the paper's numbered front-matter institution list
- **Author comment:** 10 pages main text, 20 pages total with appendix; 6 figures, 7 tables. Preprint

**Abstract.** Judgment models such as \jev{} return, in a single call and without reasoning text, a probability for each described option. This makes them attractive as an agent's action-selection layer, but it is unclear which decisions they can be trusted with. We test \jev{} on reflection tests, one-shot matrix games, the text game ALFWorld and robot control, and find a sharp boundary. \jev{} succeeds when the right option can be judged from what the input describes, which we call \emph{evaluation}. Specifically, it solves 99\% of the counterintuitive Cognitive Reflection Test questions. However, it fails when the right option depends on \emph{simulation} (i.e., predicting something not in the input), such as the opponent's action or the subgoal that must come first. In games, \jev{} plays suboptimally as if its rational opponent acted at random, because the opponent's action is not given. In ALFWorld, \jev{} favors commands that mention an object or place named in the task description. For example, given the task ``put a clean knife in the drawer'', \jev{} carries an unwashed knife straight to the drawer instead of first washing it at the sink. Surprisingly, many of these failures are not due to a lack of knowledge. Asked separately what the opponent will do, \jev{} usually answers correctly, and it responds well given the opponent's action. It fails when one call must both perform the simulation and evaluate based on it. This suggests letting code make the prediction or simulation. When code supplies it, such as a lookahead in ALFWorld and physics simulation in robot control, \jev{} becomes an expert controller through its general evaluation ability.

**Key innovations.**

- Asks a sharp boundary question about judgment models used as an agent's action-selection layer: they return a per-option probability in one call with no reasoning text, so *which* decisions can they be trusted with?
- Finds a clean split. **Evaluation** works — the model solves 99% of counterintuitive Cognitive Reflection Test items. **Simulation** fails: whenever the right option depends on something not in the input (the opponent's next action, the subgoal that must come first), it breaks — in games it plays as if a rational opponent acted at random, and in ALFWorld it prefers commands naming objects in the task description (given 'put a clean knife in the drawer', it carries an unwashed knife straight to the drawer).
- The failure is not missing knowledge: asked separately what the opponent will do, the model usually answers correctly, and it responds well once the opponent's action is given. It fails when one call must both simulate and evaluate on the simulation.
- Design implication is explicit — *let code make the prediction or simulation* — which reframes tool use as a correctness requirement rather than a capability upgrade.

---

## Multimodal Reasoning & Scaling Laws (4)

### 42. Not All Error Yields to Scale: Where Scaling Stops in Vision-Language Inference

- **arXiv:** [2610.01640](https://arxiv.org/abs/2610.01640) · submitted 2026-10-01 · primary category `cs.CV` · all categories: `cs.CV`, `cs.AI`
- **Authors:** Xinye Zhao; Yunkai Dang; Yunchen Wu; Wenbin Li
- **Institution / company:** Nanjing University (School of Intelligence Science and Technology)
- **Affiliation evidence:** verified from author block

**Abstract.** Vision-language models (VLMs) face a fixed-budget trade-off between processing more visual information for fine-grained perception and using a larger language backbone for complex reasoning. Existing studies do not tell us which combination of backbone size and input resolution to deploy, especially in high-resolution deployments. To address this gap, we propose the Separable Law that describes how VLM performance changes with language backbone size and visual token count. We fit the law to measurements from 26 InternVL and QwenVL models, with language backbone sizes from 1B to 72B, on four high-resolution benchmarks with image sizes from 224 pixels to 8K. We find that the questions responding to scaling can be predicted from the skill they require, while a substantial fraction never responds at all. We also find that the two model families gain similarly from a larger backbone, while their gains from more visual tokens differ sharply. Combined with a cost law, the Separable Law gives a closed-form rule for allocating compute between backbone size and visual tokens. When deployment is limited to available configurations, the law identifies model and image sizes that perform close to the best feasible choice under the same budget. We hope our work offers a principled way to decide how much a model should be allowed to see at high resolution, given what it must reason about.

**Key innovations.**

- Asks the deployment question prior work dodges: under a fixed budget, should you buy a larger language backbone or more visual tokens? Existing studies do not say, especially for high-resolution deployment.
- Fits a **Separable Law** over measurements from 26 InternVL and QwenVL models, language backbones from 1B to 72B, four high-resolution benchmarks and image sizes from 224 px to 8K.
- Two findings with operational teeth: whether a question responds to scaling is predictable from the skill it requires, and **a substantial fraction never responds at all**; and the two model families gain similarly from a larger backbone while their gains from more visual tokens differ sharply.
- Combined with a cost law this yields a closed-form rule for allocating compute between backbone size and visual tokens, and — when only some configurations are available — identifies model and image sizes performing close to the best feasible choice under the same budget.

---

### 43. 4Director: Controlling Video World Models with Rigid 3D Geometry

- **arXiv:** [2610.02160](https://arxiv.org/abs/2610.02160) · submitted 2026-10-01 · primary category `cs.CV` · all categories: `cs.CV`
- **Authors:** Wei Cao; Hao Zhang; Vikram Voleti; Yuqun Wu; Mallikarjun B R; Shimon Vainer; Mark Boss; Yaoyao Liu
- **Institution / company:** Stability AI; University of Illinois Urbana-Champaign
- **Affiliation evidence:** verified from author block
- **Author comment:** 28 pages, 15 figures. Project page: https://stability-ai.github.io/4director/

**Abstract.** Precise control over camera and object motion is essential for professional video production. Existing methods control objects only coarsely, through image-plane cues that are ambiguous in depth and rotation or through 3D tracks and blobs that lack complete geometry and lose consistency across viewpoint changes. We introduce 4Director, a video world model conditioned on an explicit 4D scene representation: each object is reconstructed once from the input image as a canonical mesh and moved by one prescribed rigid transformation per frame. This representation provides an intuitive 3D control interface and prevents unobserved geometry from being regenerated independently in every frame. We render the controlled scene as a depth video and introduce a Motion Adapter that transforms this geometric scaffold into video while synthesizing view-consistent appearance, illumination, and non-rigid dynamics. For training, we construct RealCOD-Rigid, a new dataset of 20,774 clips annotated with rigid 3D scenes by our automatic pipeline. We further introduce Identity-Gated IoU (IG-IoU), which jointly evaluates adherence to prescribed object motion and preservation of object identity. Experiments demonstrate that 4Director consistently outperforms prior methods in visual quality and in camera and object control.

**Key innovations.**

- Argues existing video control fails in one of two ways: image-plane cues are ambiguous in depth and rotation, while 3D tracks and blobs lack complete geometry and lose consistency across viewpoint changes.
- Control representation: each object is reconstructed **once** as a canonical mesh and moved by one prescribed rigid transformation per frame, which gives an intuitive 3D interface and prevents unobserved geometry from being regenerated independently in every frame.
- The controlled scene is rendered as a depth video, and a **Motion Adapter** converts that geometric scaffold into video while synthesizing view-consistent appearance, illumination and non-rigid dynamics.
- Ships **RealCOD-Rigid** (20,774 clips annotated with rigid 3D scenes by an automatic pipeline) and **Identity-Gated IoU**, a metric that scores adherence to prescribed motion and preservation of object identity *jointly* — a metric choice that reflects the actual failure mode rather than motion error alone.

---

### 44. Waypoint-1.5: A Real-Time Video World Model for Consumer Hardware

- **arXiv:** [2609.37107](https://arxiv.org/abs/2609.37107) · submitted 2026-09-29 · primary category `cs.CV` · all categories: `cs.CV`, `cs.HC`
- **Authors:** Rajit Rajpal; Shahbuland Matiana; Liew Wei Pyn; Anmol Agarwal; Ryan Craig; Andrew Lapp; Mithun Hunsur; Sami BuGhanem; Scottie Fox; Aaron Sanders; Carson Poole; Irene Park; Dave Rossi; Spencer Frazier; Louis Castricato
- **Institution / company:** Overworld; Hugging Face
- **Affiliation evidence:** verified from author block

**Abstract.** We present Waypoint 1.5, a real-time diffusion world model for interactive video generation on consumer-grade hardware. Unlike general video diffusion models, interactive world models (iWMs) must respond to dense user controls under strict latency and throughput constraints. Waypoint 1.5 is pre-trained on 100,000 hours of diverse, control-aligned video game data across hundreds of games, and generates playable video conditioned on full keyboard and mouse input. The model includes two resolution variants that run across a wide spectrum of consumer hardware. To characterize this unique setting, we distinguish rendered FPS, latent FPS, and control rate. We describe the data pipeline, architecture, training methodology, and runtime system behind Waypoint 1.5. We evaluate interactivity through latency and throughput. Finally, we discuss the safety and ethics considerations unique to iWMs.

**Key innovations.**

- Argues interactive world models (iWMs) face a constraint general video diffusion does not: they must respond to **dense user controls** under strict latency and throughput limits.
- **Waypoint 1.5** is pre-trained on 100,000 hours of diverse, control-aligned video game data across hundreds of games and generates playable video conditioned on full keyboard-and-mouse input; two resolution variants span a wide range of consumer hardware.
- Measurement contribution: distinguishes **rendered FPS, latent FPS and control rate** — three quantities routinely conflated when 'real-time' is claimed for world models.
- Documents the data pipeline, architecture, training methodology and runtime system, evaluates interactivity through latency and throughput, and closes with the safety and ethics considerations specific to iWMs.

---

### 45. Video Generation Models: A Survey of Post-Training and Alignment

- **arXiv:** [2610.00812](https://arxiv.org/abs/2610.00812) · submitted 2026-09-30 · primary category `cs.CV` · all categories: `cs.CV`, `cs.AI`, `cs.LG`
- **Authors:** Chaoyu Li; Xiaoyi Gu; Yogesh Kulkarni; Eun Woo Im; Mohammadmahdi Honarmand; Zeyu Wang; Juntong Song; Fei Du; Xilin Jiang; Kexin Zheng; Tianzhi Li; Fei Tao; Pooyan Fazli
- **Institution / company:** Arizona State University; Twitch; Stanford University; eBay; NewsBreak; Microsoft; Columbia University; University of Southern California; Carnegie Mellon University
- **Affiliation evidence:** verified from the paper's numbered front-matter institution list
- **Author comment:** Published in Transactions on Machine Learning Research (TMLR), 2026. Project page: https://github.com/people-robots/Awesome-Video-Generation-Post-Training
- **Journal ref:** Transactions on Machine Learning Research, 2026-June, 2026. ISSN 2835-8856

**Abstract.** Video generation has rapidly progressed from short, low-quality clips to high-resolution, long-duration sequences with complex spatiotemporal dynamics. Despite strong generative priors learned through large-scale pretraining, pretrained video models often fail to reliably follow human intent, maintain temporal coherence, or satisfy physical and safety constraints. Compared with image and text generation, alignment in video generation presents unique challenges, including error accumulation over time, motion-appearance coupling, multi-objective trade-offs, and limited supervision for temporal properties. These challenges motivate systematic post-training strategies that adapt pretrained models without retraining them from scratch. In this survey, we present the first comprehensive review of post-training and alignment in video generation models. We frame post-training as a unifying framework and distinguish between implicit alignment and explicit alignment based on how alignment signals are enforced. From this perspective, we organize existing approaches into four broad categories: supervised fine-tuning methods, self-training and distillation methods, preference- and reward-based methods, and inference-time methods. This taxonomy provides a coherent view of how alignment signals shape model behavior across both training and deployment. Beyond methodological advances, we review commonly used datasets, benchmarks, and evaluation practices, and discuss open challenges such as scalable reward design, long-horizon temporal consistency, stability-expressiveness trade-offs, and safety-aware generation. This survey aims to provide a structured conceptual foundation and practical guidance for advancing controllable and reliable video generation models.

**Key innovations.**

- First comprehensive review of post-training and alignment for **video** generation, framing post-training as the unifying lens and splitting alignment into *implicit* vs *explicit* according to how the signal is enforced.
- Taxonomy of four families: supervised fine-tuning; self-training and distillation; preference- and reward-based methods; inference-time methods — organized so that alignment signals can be traced across training and deployment.
- Isolates what makes video alignment harder than image and text: error accumulation over time, motion–appearance coupling, multi-objective trade-offs, and limited supervision for temporal properties.
- Reviews datasets, benchmarks and evaluation practice, and names open problems — scalable reward design, long-horizon temporal consistency, stability–expressiveness trade-offs, safety-aware generation. **Published in TMLR, 2026.**

---

## Evaluation, Safety Measurement & Methodology (2)

### 46. False Floors: LLM Safety Routing Evaluations Break Under Distribution Shift

- **arXiv:** [2610.01535](https://arxiv.org/abs/2610.01535) · submitted 2026-10-01 · primary category `cs.CR` · all categories: `cs.CR`, `cs.AI`
- **Authors:** Amit Singh Bhatti; Vishal Vaddina
- **Institution / company:** Quantiphi Analytics
- **Affiliation evidence:** verified from author block

**Abstract.** Safety routers send each request to one of several models and are judged against the best single model. A major routing benchmark picks that comparator on the evaluation data. In the benchmark's own setting this is harmless, but under distribution shift it is not. On HELM Safety the selection cost is 0.003-0.030 of harm under random splits and 0.045-0.113 under held-out categories, comparable to the whole deficit attributed to routing, with its direction holding under either published judge alone. It rises seven- to ninefold on AgentDojo when suites are held out. Across seven safety corpora chosen by rules fixed in advance, three meet a registered interval test and four beat a later permutation null, and three of the four interval misses are corpora where some models have zero observed harm. Prior work proves the direction of this bias. We size it on harm and accuracy, show that it is larger under the held-out splits we measure, and bound it by optimism plus a shift-dependent regret. Scored honestly under shift, routing buys little on these benchmarks. In most pool cells the nested router serves the honest baseline's model, and on the nearly saturated AgentDojo corpus a perfect pre-dispatch router is worth at most two points of harm. We also find a model's expressed recognition of a late injection steerable. On held-out reruns an attacker who knows which model it faces lowers GPT-5.4's judged recognition by 19.6 points, confirmed by an independent label. In an offline counterfactual composition into a controller, the same attack raises or lowers estimated harm depending on the fallback model. Safety routing should be evaluated under shift, against a baseline chosen without the test labels, and recognition-based defences should be scored on harm against an attacker who chooses what the model sees.

**Key innovations.**

- Finds a benchmark-construction artifact in safety routing: the routing benchmark selects its best-single-model comparator **on the evaluation data**. Harmless in-distribution, misleading under shift.
- Sizes the resulting selection cost: 0.003–0.030 of harm under random splits, but 0.045–0.113 under held-out categories — comparable to the entire deficit attributed to routing — and it rises **seven- to ninefold** on AgentDojo when suites are held out.
- Registered analysis across seven safety corpora chosen by rules fixed in advance: three meet an interval test and four beat a later permutation null, and three of the four interval misses are corpora where some models show **zero observed harm** — a floor effect rather than a clean null, which is why the paper declines to read those as refutations.
- Conclusions with teeth: scored honestly under shift, routing buys little on these benchmarks, and a perfect pre-dispatch router on the nearly saturated AgentDojo corpus is worth at most two points of harm. Separately, an attacker who knows which model it faces lowers GPT-5.4's judged injection recognition by 19.6 points (confirmed by an independent label), so recognition-based defences must be scored against an adaptive attacker.

---

### 47. Keyword Harnesses Fail Open: A Cheap Diagnostic Ladder for Tool-Use Claims in Small Language Models

- **arXiv:** [2610.02142](https://arxiv.org/abs/2610.02142) · submitted 2026-10-01 · primary category `cs.CL` · all categories: `cs.CL`
- **Authors:** Juan S. Santillana
- **Institution / company:** Independent Researcher
- **Affiliation evidence:** verified from author block
- **Author comment:** 24 pages, 12 tables, preprint

**Abstract.** Keyword-matching benchmarks can credit small models for tool use they never perform. We document such a false positive in a matched-architecture pair of Spanish security language models and propose a ladder of strict, cheap diagnostics. A 661.6M parameter model (approx. 65% code/technical text; no dedicated SFT) and a 1,109M model (web-heavy multi-phase curriculum; 6B-token tool-SFT) share decoder, tokenizer, and special tokens, scoring almost identically on lenient tool-use metrics (B4: 0.660 vs. 0.650). Verbatim-reproduction checks on training examples separate them completely: the 600M emits valid tool calls with generalized arguments on 6/6 examples; the 1B does so on 0/6 across checkpoints. A first-token probe localizes the 1B's failure to a missing prior (prob. $10^{-4}$--$10^{-5}$ on <|tool_call|>), which was erased by its web-heavy training phase. A targeted SFT recipe (diverse corpus, 5x higher learning rate, 2,202 steps, ~3.3 GPU-hours) repairs the 1B using three orders of magnitude fewer tokens than the failed phase. On all 269 corpus rows, valid emission rises from 0.100 to 0.959 (600M: 0.926). On 238 unseen prompts, the repaired 1B passes 0.536 vs. the 600M's 0.428 ($p = 0.004$). Embedding-drift checks show the repair did not move the trigger token's tied embedding (97.7% of the bf16 table remains bit-identical), meaning changes live in the surrounding network. Both models over-trigger, rarely answering negative prompts without a call (0.09 for 600M, 0.17 for repaired 1B). Factorial analyses confirm all repair configurations install the format, though suppression benefits from a diverse corpus remain a hypothesis due to seed sensitivity. This cheap diagnostic ladder costs minutes of CPU time and should gate tool-use claims on small models.

**Key innovations.**

- Documents a false positive that keyword-matching tool-use benchmarks structurally cannot see: a matched-architecture pair (same decoder, tokenizer, special tokens; one 661.6M model with ~65% code/technical text and no dedicated SFT, one 1,109M model with a web-heavy multi-phase curriculum and 6B-token tool-SFT) scores almost identically on lenient metrics (B4 0.660 vs 0.650) while one of them emits **no** valid tool calls at all.
- Proposes a ladder of strict, cheap diagnostics, cheapest first. Verbatim-reproduction checks on training examples separate the models completely (600M: valid calls with generalized arguments on 6/6; 1B: 0/6 across checkpoints). A first-token probe localizes the failure to a missing prior on `<|tool_call|>` (probability 1e-4–1e-5) that the web-heavy training phase erased.
- Repair is cheap: targeted SFT (diverse corpus, 5× learning rate, 2,202 steps, ~3.3 GPU-hours) lifts valid emission from 0.100 to 0.959 on all 269 corpus rows using three orders of magnitude fewer tokens than the failed phase, and reaches 0.536 vs the 600M's 0.428 on 238 unseen prompts (p = 0.004). Embedding-drift checks show 97.7% of the bf16 table is bit-identical, so the repair lives in the surrounding network rather than in the trigger token's embedding.
- Reports its own negatives: both models over-trigger on negative prompts (0.09 and 0.17), and the suppression benefit of a diverse corpus remains a hypothesis due to seed sensitivity. Total diagnostic cost: minutes of CPU time — the paper's actual recommendation is that this ladder should gate tool-use claims on small models.

---


## Cross-cutting observations

These are the patterns that survive across sections. Each names the papers it rests on, so a future run can check whether it is still true.

**1. Post-training is being re-scored on coverage, not accuracy.** [[Sharpening Tax in Post-Training]] ([2610.01509](https://arxiv.org/abs/2610.01509)) shows base LLMs with a light harness beating post-trained models on pass@K while losing badly on pass@1. [[Cross-Benchmark Transfer from RL on Agentic Coding Tasks]] ([2610.00890](https://arxiv.org/abs/2610.00890)) reports median trajectories getting 24–35% *shorter*. [[Mid-Harness]] ([2609.39982](https://arxiv.org/abs/2609.39982)) and [[Hindsight-Divergence Localization]] ([2609.36864](https://arxiv.org/abs/2609.36864)) then buy coverage back cheaply — by branching and by verifying actions rather than by sampling more trajectories. Four independent groups, one reframing: test-time budget is now a first-class reported quantity, and pass@1 alone is treated as an incomplete metric.

**2. The harness is a research object, not plumbing.** Five papers locate the win strictly outside the weights: [[Mingbird]] ([2610.02001](https://arxiv.org/abs/2610.02001)) reports 0.886 vs 0.405 across four harnesses holding models and machine fixed; [[AgSpec]] ([2610.01108](https://arxiv.org/abs/2610.01108)) finds retrieval-based speculative decoding fails on *corpus format* and *draft-length policy*, not on the drafting idea; [[LoopCD]] ([2610.02185](https://arxiv.org/abs/2610.02185)) turns discarded intermediate recurrent states into a training-free contrastive signal; [[PyRUA-Lean]] ([2610.01939](https://arxiv.org/abs/2610.01939)) gets 65% fewer input tokens at equal call budget by returning only requested observations; [[Mem++]] ([2610.02002](https://arxiv.org/abs/2610.02002)) shows write-time memory distillation forecloses questions before they are asked. The honest boundary is Mingbird's own frontier probe — well-formed scaffolds land within 0.072 of each other, so the ceiling here is set by harness design, not by the base model.

**3. Token-level credit assignment is being attacked from four directions at once.** [[GAW-PO]] ([2610.01511](https://arxiv.org/abs/2610.01511)) reweights rejected tokens by gradient interference with the preferred update; [[SCAPO]] ([2609.40360](https://arxiv.org/abs/2609.40360)) reduces advantages for tokens whose probability drifts under semantics-preserving prompt interventions; [[DARS]] ([2610.01207](https://arxiv.org/abs/2610.01207)) represents progress as predicates on a prerequisite graph and discounts by distance to the nearest broken prerequisite; [[FSG-RL]] ([2610.01729](https://arxiv.org/abs/2610.01729)) assigns span-level credit against function graphs. All four argue the same thing: response-level or outcome-level advantage assignment is the binding constraint on RLVR.

**4. Measurement discipline is the differentiator in this window, and it cuts downward.** [[False Floors]] ([2610.01535](https://arxiv.org/abs/2610.01535)) shows safety routing's reported deficit is largely an artifact of choosing the comparator on the test set — and concludes routing is worth at most two points of harm on a saturated corpus. [[Keyword Harnesses Fail Open]] ([2610.02142](https://arxiv.org/abs/2610.02142)) shows two models scoring 0.660 vs 0.650 on a lenient tool-use metric where one of them emits **zero** valid tool calls. [[Mingbird]] ([2610.02001](https://arxiv.org/abs/2610.02001)) downgrades its own ablation to "directional only" because replication noise equals the effect size. [[VirusCascade]] ([2609.38270](https://arxiv.org/abs/2609.38270)) states its stealth constraints rather than claiming stealth. Four papers whose main contribution is removing value from a headline number is an unusual density for one window.

**5. Long-context work has shifted from compression to routing.** [[CommunityKV]] ([2610.00418](https://arxiv.org/abs/2610.00418)) casts sparse attention as community detection over the QK^T scores already computed in prefill; [[HHR]] ([2610.01230](https://arxiv.org/abs/2610.01230)) casts hash retrieval as a learned routing problem and diagnoses its own failure mode as magnitude-discarding binarization; [[AgSpec]] ([2610.01108](https://arxiv.org/abs/2610.01108)) routes drafting across session/workspace/global corpora; [[AVSG]] ([2609.37538](https://arxiv.org/abs/2609.37538)) routes KV entries across an HBM buffer by lifetime. In each case the contribution is an explicit *update rule* under streaming, not a one-shot clustering.

**6. Systems papers in this window report end-to-end numbers, not only microbenchmarks.** [[AVSG]]: −39% time per output token and 1.27× throughput on a real production dataset. [[CadenceRL]]: +48% decode throughput, −64% P95 trajectory latency. [[AgSpec]]: 4.37× at batch 1, 4.76× at batch 16. [[CommunityKV]]: 1.25×/1.71× end-to-end. [[HHR]]: 2.83× end-to-end at 128K. This is a genre change relative to cache papers of a year ago and it makes the numbers comparable across papers for the first time.

**7. Popularity bias now has a proposed generative mechanism.** [[FairDiff]] ([2609.36671](https://arxiv.org/abs/2609.36671)) does not claim diffusion recommenders inherit imbalance — it claims their reverse sampling trajectories collapse onto high-density items because the forward terminal distribution of long-tailed data deviates from the Gaussian prior. That is falsifiable in a way "DRMs are unfair" is not: the prediction is that the bias worsens with trajectory length and narrows when a one-step optimal-transport calibration is added.

**8. Agentic recommenders created an attack surface with no static analogue.** [[VirusCascade]] ([2609.38270](https://arxiv.org/abs/2609.38270)) shows the quality mechanism and the attack mechanism are the *same* mechanism — collaborative reflection rationalizes injected evidence into memory and then propagates it. A static scoring model has no recurrent write-back path, so there is no analogue to compare against, which also means there is no established defense to import.

**9. Verification is separating from generation.** [[VeriHarness]] ([2610.00972](https://arxiv.org/abs/2610.00972)) reports the sharpest version of the idea: disagreement exposes correct alternatives, consensus conceals errors — so majority voting is the wrong primitive. [[Mid-Harness]] ([2609.39982](https://arxiv.org/abs/2609.39982)) finds verifier quality, not action sampling, is the binding constraint, and distills a strong verifier into a small generator *without* touching that generator. [[Code Owns the Simulation]] ([2610.01834](https://arxiv.org/abs/2610.01834)) draws the boundary from the other side: a judgment model is reliable for evaluation and unreliable for simulation, so let code do the predicting.

**10. A recurring negative result about "grounding".** [[Same Reward, Different Skills]] ([2610.01908](https://arxiv.org/abs/2610.01908)) finds RLVR benchmark gains occur *without visual information during training*, with blind-trained 3B models recovering ~half the real-image gain and 7B models ~four fifths. Combined with [[False Floors]]' comparator artifact, the pattern is that headline gains in this window survive their own authors' scrutiny less often than in the previous window.

## Coverage, vacancies and things deliberately not included

**Advertising / CTR / auction is a genuine vacancy in this window.** Queries run: `cat:cs.IR`, `all:"CTR prediction"`, `all:"click-through rate"`, `all:"computational advertising"`, `all:"advertis*"`, `all:auction`, `all:bidding`, plus category windows for cs.IR over 2026-09-30 → 2026-10-04. Result: **two** papers touching ads in the whole 72-hour window — the auction-pacing theory paper ([2609.34515](https://arxiv.org/abs/2609.34515)) and, marginally, [[FARE]] ([2609.31890](https://arxiv.org/abs/2609.31890)), a JPMorganChase workshop paper from 09-25 on SOV-constrained ranking. **No CTR-prediction, auto-bidding, budget-allocation or real-time-bidding paper appeared.** This is recorded as a vacancy rather than filled with adjacent retrieval or generic re-ranking papers. The relevance-sorted fallback queries (which skew old) surfaced several unclaimed CTR/bidding papers from earlier in 2026 — 2606.21101, 2606.14192, 2606.09896, 2605.01756, 2604.12799, 2601.02754, 2601.07613, 2512.03354 — none re-checked or featured here, since all fall outside the window.

**Games.** No paper in the window reports a deployed player-facing game-RL policy or a live-service metric. The window's game content is: agentic *game development* ([[RSIGame]] [2609.39045](https://arxiv.org/abs/2609.39045)), benchmark infrastructure for programmable world models ([[ROWBench]] [2610.02205](https://arxiv.org/abs/2610.02205)), a judgment-model boundary study evaluated on matrix games and ALFWorld ([[Code Owns the Simulation]] [2610.01834](https://arxiv.org/abs/2610.01834)), and one real-time game-data world model ([[Waypoint-1.5]] [2609.37107](https://arxiv.org/abs/2609.37107)). A keyword sweep for game-RL in cs.GT/cs.LG/cs.AI over the window returned mostly game *theory* (matroid packing games, Nash complexity in congestion games, matrix-game regret) with no commercial-environment RL result. The strongest game-learning item found, [[Temporal-Difference Learning for Dragonchess]] ([2610.01845](https://arxiv.org/abs/2610.01845), Springer LNAI), is a small round-robin study (10,000 games after a PyGame→C++ rewrite) and is noted here rather than featured.

**Sequential modeling** appears only inside recommendation work — Inherit4Rec's SMoE conversion, AgentWebRec's evidence-acquisition ordering, FairDiff's trajectory dynamics — with no dedicated sequential-modeling architecture paper in the window.

**Deliberately excluded:** papers already written up anywhere in this wiki (442 of the 1,886 pooled records were already claimed and were dropped before selection); and adjacent-topic filler, specifically generic information-retrieval papers that keyword-matched "retrieval" but concern neither recommendation nor ads.

## Affiliation discipline

arXiv's API exposes no affiliation data, so every institution in this report comes from the **rendered LaTeX author block** of the paper itself (`arxiv.org/html/<id>v<n>`, `ltx_contact ltx_role_affiliation` spans), or from the paper's own numbered front-matter institution list where the template uses footnote markers. OpenAlex was probed for 8 papers as a cross-check and returned an institution list for exactly 1 (Inherit4Rec), where it agreed with the author block, so it is not usable as a primary source here.

- **43 of 47 entries:** institution fully verified from the paper's own front matter.
- **3 entries unresolved, marked explicitly and not guessed:** [2610.01729](https://arxiv.org/abs/2610.01729) (author block contains only a corresponding-author note), [2609.39982](https://arxiv.org/abs/2609.39982) (numeric affiliation superscripts 1,2 present, institution text dropped by LaTeXML), [2610.02205](https://arxiv.org/abs/2610.02205) (empty affiliation marker).
- **1 entry partially malformed:** [2610.01042](https://arxiv.org/abs/2610.01042) — the second affiliation string names a department ("Department of Electrical and Computer Engineering") with no institution, so only USC is recorded.
- **Nothing was inferred from author surnames.** This matters concretely for [2609.39982](https://arxiv.org/abs/2609.39982) (Mid-Harness), where several author names are widely associated with one industrial lab; the report records "not stated" instead.
- **One affiliation had to be read out of a broken template:** [2610.02185](https://arxiv.org/abs/2610.02185) dumps its institution into an `ltx_dates` div; the report says so.

## Method and known limits

**Discovery.** arXiv API (`export.arxiv.org/api/query`), 28 queries: 9 category feeds sorted by `submittedDate` (cs.AI, cs.LG, cs.CL, cs.IR, cs.MA, cs.GT, cs.CV, cs.RO, stat.ML) at 120–200 records each, and 19 targeted keyword queries (`CTR prediction`, `click-through rate`, `computational advertising`, `ad recommendation`, `sequential recommendation`, `session-based recommendation`, `recommender systems`, `collaborative filtering`, `speculative decoding`, `KV cache`, `inference efficiency`, `scaling law`, `compute-optimal`, `alignment`, `agentic`, `LLM agents`, `Atari`, `video games`, `benchmark contamination`, `pretraining data`). Pool after dedup: 1,886 records, 1,444 unclaimed.

**Rate limiting is a real constraint on this run and is disclosed.** The API returned HTTP 429 repeatedly for this account tier; pacing was raised to ~16 s between requests with escalating backoff, and two query groups (`cat:cs.MM` keyword variants, `cat:cs.CY`/`stat.ML` window variants) were abandoned mid-sequence. The consequence: **cs.MM (multimodal) and cs.CY coverage is thinner than intended**, and multimodal results here lean on cs.CV cross-listing rather than on a dedicated cs.MM sweep. Every query name and its outcome is recorded in the run log so a later run can close the gap deliberately.

**Selection was manual and topic-weighted**, not a top-N by any arXiv ranking. Papers were chosen for coverage of the requested areas and for having a concrete, checkable claim; a paper with a mechanism and a number beat a paper with a broad claim. This biases the report toward substantive papers and against high-volume low-signal ones — it is not a random sample of the window and should not be read as one.

**No result here was independently replicated, and none of the numbers were re-measured.** Every figure in the "Key innovations" lines is quoted from the paper's own abstract or author comment. Where an abstract's own framing looks like an overreach, the entry says so (see [[Same Reward, Different Skills]] on the blind-training result, [[False Floors]] on its floor-effect corpora). Four entries carry a peer-reviewed venue from the author comment: NeurIPS 2026 ([2610.01984](https://arxiv.org/abs/2610.01984)), TMLR 2026 ([2610.00812](https://arxiv.org/abs/2610.00812)), WINE 2026 ([2609.34515](https://arxiv.org/abs/2609.34515)), NDSS 2027 ([2609.38270](https://arxiv.org/abs/2609.38270)), plus one NeurIPS 2026 workshop ([2610.00722](https://arxiv.org/abs/2610.00722)).

**Related wiki pages:** [[affiliation-landscape]] (why affiliation verification is handled this way), [[ctr-scaling-landscape]] (the standing CTR thread this window did not advance), [[game-rl-daily]]-class digests under `wiki/synthesis/2026-09-30/` and `2026-10-01/` (the game-RL vacancy line), and [[2026-10-02/arxiv-daily]] (the immediately preceding window, deduped against).

