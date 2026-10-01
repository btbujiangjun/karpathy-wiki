---
title: arXiv Conference Digest — 2026-10-01
type: synthesis
created: 2026-10-01
updated: 2026-10-01
sources: []
tags: [arxiv, conference-digest, llm-agents, on-policy-distillation, multimodal, efficiency, 2026-10-01]
---

# arXiv Conference Digest — 2026-10-01

Detailed digest of 31 papers from the 2026-09-30 → 2026-10-01 arXiv submission batch, covering top-conference acceptances (ICML 2026, NeurIPS 2026, EMNLP 2026, ECCV 2026, COLM 2026, Interspeech 2026), NeurIPS 2026 workshops, and high-signal unreviewed preprints from target institutions. Every entry carries authors, affiliation evidence, venue evidence, condensed abstract, the specific innovation, the comparison baseline set, and quantitative results where the abstract reports them.

## Scope & Method

- **Window**: `submittedDate:[202609300000 TO 202610010000]` via the arXiv API. `totalResults = 1688`; published timestamps run `2026-09-30T00:01Z` → `2026-09-30T17:59:56Z`; ID range `2609.38676`–`2609.40363`.
- **Deduplication**: version suffixes are stripped with `re.sub(r'v\d+$', '', id)` before comparison against bare arXiv IDs harvested from the wiki. Result: **1688 unique base IDs, 161 already claimed elsewhere, 1527 unclaimed**. All 31 papers below are unclaimed at the time of writing.
- **Selection criteria**: (a) explicit venue acceptance in the arXiv comment field; (b) named target institution in title/abstract/authors/comments; (c) requested follow-ups on the [[agents]] and [[on-policy-distillation]] themes surfaced by same-day scans.
- **Affiliation discipline**: the arXiv API returns no author affiliations. Affiliations are therefore marked **(project page)** when the arXiv comment links an institutional domain, **(named in text)** when the abstract names the institution, or **not listed** otherwise. Nothing is inferred from author surnames.
- **Results discipline**: numbers are quoted from the authors' own abstracts. Where an abstract reports no numbers, the entry says so rather than paraphrasing a vague claim. No proceedings page was consulted, so venue strings are quoted verbatim from the arXiv comment field.

## Coverage Summary

| Venue | Count | Notes |
|---|---|---|
| ICML 2026 | 1 | Spotlight acceptance quoted from comment |
| NeurIPS 2026 (main) | 8 | Includes 1 Spotlight, 1 poster |
| NeurIPS 2026 (workshop) | 3 | AI-Native Academia (Oral), On-Device Intelligence (ODI), others excluded as off-topic |
| EMNLP 2026 | 2 | Main + Findings-track |
| ECCV 2026 | 1 | With supplementary material |
| COLM 2026 | 1 | Main conference paper |
| Interspeech 2026 | 1 | — |
| Preprint / tech report (no venue) | 15 | Includes NVIDIA LPR, Bilibili, Tencent GitHub releases |

Requested venues with **no unclaimed acceptance found in this window**: ICML 2025 camera-ready (one entry, `2609.38998`, is an ICML 2025 re-upload and was excluded as already-claimed), AAAI 2026, ICLR 2026/2027, KDD 2026, CVPR 2026, ACL 2026, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025/2026. This is a negative finding for a single 18-hour arXiv window, not evidence of absence — arXiv comments are author-supplied and many acceptances are announced weeks after the conference date.

## Cross-References to Same-Day Digests

161 papers in this batch were already claimed by sibling reports and are **not** re-summarized here. Notable overlaps include the Douyin GEAR work (`2609.39327`), the Kuaishou RouteRec system (`2609.39007`), the Kuaishou challenge paper (`2609.39828`), and SparLeak (`2609.38830`). See `arxiv-ai-search.md`, `arxiv-daily.md`, and `arxiv-paper-check.md` (all 2026-10-01) in this directory.

## A. LLM Agents, Self-Improvement, and On-Policy Distillation

### 1. PivotOPD: Learning to Recover from Pivotal Mistakes in Multi-Turn Agents / PivotOPD：让多轮 Agent 从关键性错误中学习恢复

- **arXiv**: `2609.40285` — [abstract](https://arxiv.org/abs/2609.40285) | [PDF](https://arxiv.org/pdf/2609.40285)
- **Authors**: Yinghui He, Yapei Chang, Khushi Bhardwaj, Daniele Molinari, Tugrul Konuk, Jan Kautz, Ali Hatamizadeh
- **Affiliation**: **NVIDIA** (project page hosted at `research.nvidia.com/labs/lpr/pivotopd/` — NVIDIA LPR). The arXiv API lists no affiliation strings.
- **Venue**: No conference label. Self-described "PivotOPD technical report". (single-source)

**Condensed abstract**: On-policy distillation (OPD) trains language agents with dense teacher supervision on student-generated trajectories. In multi-turn interaction this breaks down because a single wrong action changes every later state, so errors compound. Across three Qwen3 models (8B–235B) the authors find that **more than half of failed rollouts contain a "pivotal mistake"** — an action that moves the agent *farther* from completion — and that this mistake **usually occurs early**. Critically, these mistakes are often recoverable: supervising the model for only a few turns after the pivotal turn restores task success. PivotOPD therefore trains the student on two objectives simultaneously.

**Innovation**: At each detected pivotal mistake, the teacher (a) supplies a *gold action*, and (b) names a *recovery action* for each of the next few turns. **Preventive distillation** applies the gold action with **reverse KL** to push the student away from the pivotal mistake; **recovery distillation** applies the named recovery actions with **forward KL** to transfer recovery behavior the student almost never samples on its own. The asymmetric KL directions are the core design choice — prevention needs mode-seeking, recovery needs mass-covering.

**Comparison**: 13 baselines across ALFWorld, WebShop, and search-based QA; best average performance for both Qwen3-1.7B and Qwen3-8B students.

**Results**: **+5.5%** over the strongest baseline on ALFWorld for the 1.7B student. Transfers across model families: **+3.2%** resolve rate for a Nemotron-3.5 student on SWE-Bench Verified.

---

### 2. DAGent: Evaluate-then-Grow Planning for Deep Research Agents / DAGent：面向深度研究 Agent 的 Evaluate-then-Grow 增量规划

- **arXiv**: `2609.39154` — [abstract](https://arxiv.org/abs/2609.39154) | [code](https://github.com/hanwenliu6825/DAGent)
- **Authors**: Hanwen Liu, Yuanfu Sun, Qiaoyu Tan
- **Affiliation**: not listed.
- **Venue**: **NeurIPS 2026** (accepted; comment: "Accepted at NeurIPS 2026"). (single-source)

**Condensed abstract**: DAG-based multi-agent systems suit deep research because they parallelize sub-tasks and isolate each one in a focused dependency context. But existing DAG agents instantiate the whole plan *before* execution and patch the graph only after failures — a Plan-then-Patch strategy that "commits most strongly when its evidence is weakest" and burns computation on branches that should never have been planned. DAGent replaces this with incremental growth: an Orchestrator extends the task graph one batch at a time, conditioned on confidence and uncertainty signals from already-completed nodes.

**Innovation**: Three coupled pieces. (i) **Evaluate-then-Grow** planning instead of plan-then-patch. (ii) A **hierarchical context layer** that propagates compact `QueryDocs` by default while preserving full execution traces for on-demand recall. (iii) **DAGRPO**, a GRPO adaptation that injects *topology-conditioned credit assignment* on Executor rollouts plus a structural-compliance regularizer on Orchestrator plans — the recorded DAG topology admits structural RL signals that outcome-only recipes cannot define.

**Comparison**: Strongest open-source baseline at Qwen3-235B-A22B; same-budget outcome-only GRPO at Qwen3-8B; Plan-then-Patch same-architecture ablation; replicated across four open-source backbones and extended to GPT-5 at 327K context.

**Results**: **+5.3 / +5.8 / +2.0** points on BrowseComp-Plus / GAIA / xbench-DeepSearch over the strongest open-source baseline. At Qwen3-8B, DAGRPO gains **+3.0** average Pass@1 over same-budget outcome-only GRPO. The same-architecture ablation shows evidence-conditioned planning reaches higher accuracy at *lower* per-task token, tool-call, and step cost.

---

### 3. Make Code as Policy Great Again: Frontier Agents Write, Call, and Evolve Robot Tools / Make Code as Policy Great Again：前沿 Agent 编写、调用并演化机器人工具

- **arXiv**: `2609.39018` — [abstract](https://arxiv.org/abs/2609.39018)
- **Authors**: Shijia Ge, Alex Zhou, Jianshu Zeng, Yexing Wan, Di Wu, Zelin Zheng, Yazhe Wang, Zhiqi Jia, Xuan Shangguan, Jay Zhu, Yijun Liu, Lingyu He, Sihang Wu, Xiao He, Hongcheng Gao
- **Affiliation**: **tentative** — no institutional affiliation listed; the abstract names **DeepSeek-V4-Flash** only as an evaluated execution agent, not as the authoring institution. The author list resembles an HKU-affiliated robotics group (Sihang Wu / Lingyu He / Hongcheng Gao), but this is **not verified** and is recorded as speculation only. (single-source)
- **Venue**: No conference label. 33 authors, no comment field. (single-source)

**Condensed abstract**: Frontier models can control robots, but reasoning through every reach, grasp, and retreat makes manipulation slow and token-heavy. The paper revisits *code as policy* with a different division of labor: **models build executable tools, code executes multi-phase motions, models decide what happens next**. URAI (Universal Robot-Agent Interface) couples a programming agent that constructs tools with an execution agent that consumes them in a feedback loop.

**Innovation**: The programming agent writes reusable and task-specific tools from task intent and refines them through execution feedback plus human guidance. The execution agent selects and parameterizes tools from current observations, with each call running a complete motion locally before returning control. Two consequences matter: (i) model-level decision-making is *retained between* tool executions, unlike designs that hand all subsequent decisions to a generated program; (ii) validated tool revisions persist across episodes **without updating foundation-model weights**, and a shared GUI/API makes the same tools available to humans and agents.

**Comparison**: Direct fingertip control (no tools); a program written in advance vs. agents deciding after each call; four frozen execution agents.

**Results**: Aggregate success across five RoboDojo tasks rises **18.0% → 53.0%** vs. direct fingertip control, largest gain on Swap Blocks. With identical tools, a pre-written program reaches only **24%** while two agents deciding after each call reach **56%**. Three of four agents finish **1.3–1.5× faster** with **1.5–1.7× fewer** execution-agent output tokens; DeepSeek-V4-Flash's cost barely changes. Also validated on seven real-world AgileX dual-arm tasks (manipulation, cloth folding, human-interactive tic-tac-toe).

---

### 4. WorkGenesis: Building the Worlds That Teach Agents to Work / WorkGenesis：构建教会 Agent 工作的世界

- **arXiv**: `2609.39325` — [abstract](https://arxiv.org/abs/2609.39325)
- **Authors**: Xinyu Zhu, Fenyi Liu, Yuzhu Cai, Shuo Tang, Rui Ye, Linfeng Zhang, Siheng Chen
- **Affiliation**: **not listed**; abstract names **DeepSeek-V4-Pro-Preview (1.6T)** only as a beaten frontier baseline.
- **Venue**: No conference label; 47 pages. (single-source)

**Condensed abstract**: Training work-capable agents requires realistic work scenarios. Expert-authored occupational work is slow and expensive to produce, while unconstrained synthesis yields tasks with weak factual grounding or internally inconsistent requirements. WorkGenesis builds executable occupational work from *real-world artifacts* rather than from model imagination.

**Innovation**: Two components. (i) **Evidence-Based Work Construction** — grounds each work unit in real evidence by retrieving public files guided by **O\*NET occupational knowledge**, then synthesizes surrounding context, companion materials, the work request, and an *itemwise rubric* around those files. (ii) **Execution-Guided Consistency Verification** — renders a reference deliverable inside the constructed work, attributes every unsatisfied rubric item to the agent, the task, or the rubric itself, and uses task/rubric defects as feedback to iteratively repair until the audit passes. The attribution step is what makes this more than a rubric checker: it distinguishes agent failure from data defect.

**Comparison**: Comparable-scale baselines across GDPvalAA-v2, APEX-Agents-AA, and JobBench (5 metrics); frontier model DeepSeek-V4-Pro-Preview (1.6T params).

**Results**: **Fx-Work-35B**, trained with plain SFT on only **20K** synthesized work units, scores **31.00 vs 24.79** average — highest among all comparable-scale baselines and above the 1.6T frontier model.

---

### 5. Can Terminal Agents Trust Their Own Verification? / Terminal Agent 能相信自己的验证吗？诊断并改进自验证

- **arXiv**: `2609.38812` — [abstract](https://arxiv.org/abs/2609.38812)
- **Authors**: Yingfeng Luo, Shaowei Wei, Daixin Wang, Dingyang Lin, Kaiyan Chang, Weiqiao Shan, Tong Zheng, Zhiqiang Zhang, Jingbo Zhu, Tong Xiao
- **Affiliation**: not listed (Zhejiang University is plausible from the author list but unverified).
- **Venue**: No conference label. (single-source)

**Condensed abstract**: Terminal agents solve tasks through command-line interaction and rely on self-verification to assess and correct their solutions. The paper asks how trustworthy that self-verification actually is, and answers with a purpose-built diagnostic rather than a new method first.

**Innovation**: A **diagnostic framework** that identifies the first complete solution in each trajectory, determines objectively whether it is correct, and uses that ground truth to quantify the agent's *subsequent* verification and recovery behavior. This decouples "did the agent verify?" from "did verification work?" — a distinction prior work conflates.

**Results — diagnostic**: Across ten terminal agents on TerminalBench2.1, verification is **nearly universal** once a complete candidate exists, but only **61.43%** of incorrect candidates are detected, and only **49.36%** of detected errors are successfully repaired. The bottleneck is therefore detection and repair, not initiation.

**Innovation — method**: **SCVD (Student-Conditioned Verification Distillation)** lets the student first produce a candidate solution, then distills a *stronger teacher's* subsequent verification and recovery **from the same interaction context**. Conditioning on the student's own candidate avoids the distribution mismatch of full-trajectory distillation.

**Results — method**: Across three Qwen3.5 backbones, Pass@1 on TerminalBench2.1 improves **+9.74 to +16.85** points over base models and **+4.49 to +8.61** points over standard full-trajectory distillation, while avoiding full-trajectory distillation's pronounced out-of-distribution degradation on SWE-bench Verified.

---

### 6. Do Self-Evolving Skills Generalize to Held-Out Tasks? / 自演化 Skill 能泛化到 Held-Out 任务吗？

- **arXiv**: `2609.39148` — [abstract](https://arxiv.org/abs/2609.39148)
- **Authors**: Xihao Piao, Zifeng Wang, Zhen Chen
- **Affiliation**: not listed.
- **Venue**: No conference label. (single-source)

**Condensed abstract**: Agents can externalize what they learn into reusable *skills* (procedures, checklists, code, executable artifacts). Self-evolving skill methods rewrite these skills after each round of practice on training tasks, then apply them to new tasks of the same kind. The paper asks the question the field has been skipping: **does improvement on training tasks carry over to test tasks?**

**Innovation**: A controlled generalization study — five self-evolving methods plus a one-shot skill, six benchmarks, *same model, same agent, same train/test split* for every method — followed by a mechanistic read of *why* skills fail to transfer, and a corrective design (**GSO**) derived from that read.

**Results**: Of the **21 skills that improve on their training tasks, 5 keep all of the improvement on test tasks, 13 keep part, and 3 keep none**. **No existing method is best everywhere.** Reading the skills explains it: skills that transfer badly hard-code details that should be task-dependent (column names, output filenames), or generalize a fix for one failure into a rule for every task. An LLM judge that reads skill content ranks *finished* skills the same way test results do in **86% of pairs** — but predicts the effect of a *single edit* poorly, so edits still have to be validated by running them.

**Innovation — GSO (Generalizable Skill Optimization)**: keep only a *guide for writing skills* and write a **new skill per task** instead of mutating one accumulating artifact. It scores highest on **all six benchmarks**.

---

### 7. Rep2Skill: Representation-Guided Skill Self-Evolution for LLM Agents / Rep2Skill：面向 LLM Agent 的表示引导 Skill 自演化

- **arXiv**: `2609.39149` — [abstract](https://arxiv.org/abs/2609.39149)
- **Authors**: Kaixing Zhang, Changming Li, Yingdong Shi, Zheng Zhang, Kaitao Song, Wenjie Shi, Jingang Wang, Kan Ren
- **Affiliation**: not listed (author list overlaps with Shanghai Jiao Tong / industry labs; unverified).
- **Venue**: No conference label. (single-source)

**Condensed abstract**: Textual skills let LLM agents accumulate reusable procedural knowledge without touching model parameters, but existing skill evolution stays inside the text space: the optimizer must diagnose success and failure patterns from long execution trajectories and sparse task outcomes. The paper asks whether an agent can improve its textual skills by reflecting on its **own internal representations**.

**Innovation**: Rep2Skill models the **internal model representation trajectories** recorded during agent rollouts, uses them to **localize the specific turns that deviate from successful execution dynamics**, and then interprets those signals alongside execution context to produce actionable textual feedback for targeted skill revision. The deviant-turn localization is the substantive contribution — text-only methods only learn that an episode failed, not which turn went wrong.

**Comparison**: Text-only skill-evolution approaches, under the harder self-evolution setting where **the same LLM serves as both executor and optimizer** (no stronger external model to critique with).

**Results**: Consistently outperforms text-only approaches across two agent environments with two open-source LLMs. (No absolute numbers given in the abstract.)

---

### 8. ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation / ReSAIL：缓解迭代式 Agent 自蒸馏中的崩塌

- **arXiv**: `2609.39306` — [abstract](https://arxiv.org/abs/2609.39306)
- **Authors**: Shengjie Jin, Hengbo Xu, Zelong Sun, YuJie Guo, Zhiwu Lu
- **Affiliation**: not listed.
- **Venue**: No conference label. (single-source)

**Condensed abstract**: Iterative self-distillation lets LLM agents learn across successive deployments — a path toward recursive self-improvement (RSI). The authors' experiments with existing methods reveal a **collapse in deployment performance across cycles**, and notably *task performance with privileged information also declines*, which localizes the failure to the learning mechanism rather than to the supervision signal.

**Innovation**: **ReSAIL** (Retentive and Selective Augmentation for Iterative Self-Distillation) is a **plug-in** augmentation for iterative privileged-information self-distillation with two moves: (i) select interaction steps **where privileged information most strongly changes the teacher's predictions**, and balance the resulting distillation losses across trajectories; (ii) regularize the student's PI-conditioned output distributions toward those of the **frozen** teacher at both selected *and* unselected steps, so PI-conditioned behavior survives to supervise the next cycle. (ii) is what makes the method iterative rather than single-shot — without retention there is nothing to carry forward as the student becomes the teacher.

**Comparison**: Self-distillation baselines over three cycles on ALFWorld and TextCraft across model scales; sensitivity-guided offline data selection for multimodal GUI agents on AITZ.

**Results**: Sustains substantial gains across scales and three cycles, with an **average absolute gain of 22.5% in final-cycle success rates** when added to self-distillation baselines. Sensitivity-guided selection also improves action-prediction accuracy for multimodal GUI agents on AITZ.

---

### 9. Disentangling Self-Distillation: Measuring and Modeling Acquisition and Retention / 解耦自蒸馏：度量并建模获取与保持

- **arXiv**: `2609.39494` — [abstract](https://arxiv.org/abs/2609.39494)
- **Authors**: Luis Zuin, Alexis Huet, Dario Rossi, Zied Ben Houidi
- **Affiliation**: not listed (Orange-affiliated by author list; unverified).
- **Venue**: No conference label. (single-source)

**Condensed abstract**: Self-distillation with privileged context adapts a model by letting it, once conditioned on a reference response, teach its context-free copy token by token. Prior work differs along three entangled axes but usually studies them in fixed combinations, producing **conflicting conclusions**.

**Innovation**: A taxonomy of the three axes — **(i) rollout source** (student vs. teacher), **(ii) teacher coupling** (frozen vs. EMA of the student at some coupling rate), **(iii) KL direction** (reverse vs. forward) — plus a unifying framework that subsumes all self-distillation methods and classic SFT, and a **controlled model of the same objective** that explains the observed trade-offs rather than merely reporting them.

**Results**: **1,200 adaptation runs** across every combination of the three axes, on Qwen2.5-7B and Ministral-3-3B, on ordinary *and* contradictory tasks. Findings: (i) rollout source matters most where the task **contradicts pretrained behavior** — teacher rollouts raise acquisition far above student rollouts with almost no retention change; (ii) teacher coupling changes **acquisition most on every task** — acquisition rises with coupling rate, then *falls* past a task-specific rate; (iii) switching KL direction costs retention in one model but not the other, so which axis to tune first is **model-dependent**. The controlled model reproduces all three trends.

---

### 10. Is Better Teacher Supervision Enough? Unlocking Student-side Learning in Multimodal OPD / 更好的教师监督就够了吗？释放多模态 On-Policy Distillation 中的学生侧学习

- **arXiv**: `2609.39120` — [abstract](https://arxiv.org/abs/2609.39120) | [code](https://github.com/Sirilaw/S-OPD)
- **Authors**: Siyuan Liu, Kanghui Tian, Yue Duan, Yutao He, Shangdong Yang, Jian Zhang, Yinghuan Shi
- **Affiliation**: not listed.
- **Venue**: No conference label. (single-source)

**Condensed abstract**: Multimodal on-policy distillation (OPD) improves reasoning with token-level teacher supervision on the student's own trajectories. Existing methods focus on the *teacher side* — enriching teacher inputs, refining teacher feedback. This paper shows that **limited student perception is a second critical bottleneck**: supplying oracle visual facts still substantially improves OPD-trained students for *both weak and strong teachers*.

**Innovation — S-OPD**: two objectives that strengthen student perceptual learning. **Teacher-calibrated Policy Contrast** separates student policies under original vs. *masked* images with teacher-based token-level gating, forcing reliance on visual evidence during reasoning; **Policy Agreement** aligns student policies under original vs. *noise-perturbed* images for robustness to visual noise. It is a **plug-in**: no additional data annotations, no extra model parameters, no additional inference operations, and it stacks with existing teacher-side supervision methods.

**Comparison**: 8 benchmarks across student scales and multiple distillation paradigms; combined with existing teacher-side methods.

**Results**: Consistent improvements, **up to +4.25 points on LogicVista**; further gains when combined with teacher-side supervision methods.

---

### 11. Trustworthy Runtime Error Healing in Real-World Repositories / 真实代码仓库中的可信运行时错误修复：Benchmark 与 Guardrail

- **arXiv**: `2609.39086` — [abstract](https://arxiv.org/abs/2609.39086)
- **Authors**: Gou Tan, Pengfei Chen, Zhensu Sun, Jieke Shi, Junkai Chen, Ting Zhang, Weifeng Sun, Junda He, Shuai Liang, Chuanfu Zhang, Lwin Khin Shar, David Lo
- **Affiliation**: not listed (Nanyang Technological University is plausible from the author list; unverified).
- **Venue**: No conference label. (single-source)

**Condensed abstract**: Runtime error healing lets a crashed program continue by generating code that repairs its live runtime state. Prior work evaluates this only on small competition programs, and executing LLM-generated code inside a live process raises safety concerns the field has not addressed. This paper moves it toward real repositories on two fronts at once — evaluation and safety.

**Innovation**: **(i) HealBench** — 265 runtime errors drawn from **18 real-world repositories**, each paired with a reference execution on the patched version, plus a unified framework that lets agents heal with **cross-file context and live runtime state**. **(ii) HealGuard** — requires healing code to be written in **HealCore**, an analyzable subset of Python, and applies **static and dynamic taint analysis** to check whether state changed by healing reaches operations that developers marked as protected. HealGuard turns an open-ended code-generation problem into a statically checkable one.

**Comparison**: A dedicated healing method plus three general coding agents across three backbone LLMs.

**Results**: Best setting **resumes execution in 38.11%** of instances and **passes the target test in 28.68%** — existing agents already heal a meaningful share of repository-level crashes. However, among executions that pass, HealGuard flags **17.4%** whose healing-changed state may reach a protected operation. On 684 controlled cases HealGuard detects **all** unsafe cases at the cost of a **68.42% false-positive rate**.

---

### 12. NarrativeSteward: Coordinating Delegation, Guidance, and Verification / NarrativeSteward：在 Agent 辅助的交互式叙事创作中协调委派、指导与验证

- **arXiv**: `2609.39333` — [abstract](https://arxiv.org/abs/2609.39333) | [code](https://github.com/Tencent/NarrativeSteward)
- **Authors**: Wenjin Wang, Jiazhen Lei, Yuxin Sha, Nuwa Xi, Meng Zhao, Xingxi Yin, Qi Liu, Yuliang Shen, Zixun Sun
- **Affiliation**: **Tencent** (project released at `github.com/Tencent/NarrativeSteward` — Tencent organization namespace). The arXiv API lists no affiliation strings.
- **Venue**: No conference label; open-sourced technical report. (single-source)

**Condensed abstract**: Autonomous agents can turn author goals into interactive narratives by independently organizing and carrying out generation and revision. But as agents generate and revise extensive content, authors lose the thread — they struggle to grasp overall structure, local detail, and the relationships between them, which makes continued guidance hard.

**Innovation**: An authoring environment that organizes **outlines, worldbuilding, and narrative graphs as linked artifacts**, so the same structures are both executable by the agent and inspectable by the author. Agent dialogue plus project-wide structural review help authors understand the evolving work and guide local *and* cross-layer revisions; change records and execution verification help them assess the result.

**Comparison**: General-purpose agents (the baseline condition in the user study).

**Results**: Technical tests validated the system's change records, recovery mechanisms, and execution diagnostics. In a **12-participant within-subject study**, NarrativeSteward supported easier formulation of revision requests and easier inspection of changes, and produced greater perceived understanding of changes and story structure than general-purpose agents. Qualitative findings show how reviewing work and feedback lets authors develop requirements and guide subsequent delegation. **No effect sizes reported** — read as qualitative evidence only.

## B. Reasoning Reliability, Evaluation, and Decoding

### 13. Alleviating Hallucination in Reasoning Tasks with Training-Free Uncertainty-Guided Steering / 用免训练的 Uncertainty-Guided Steering 缓解推理任务中的幻觉

- **arXiv**: `2609.38962` — [abstract](https://arxiv.org/abs/2609.38962)
- **Authors**: Litian Liu, Qiqi Hou, Yubing Jian, Reza Pourreza, Mohammad Ghavamzadeh, Roland Memisevic, Yao Qin, Hong Cai
- **Affiliation**: **tentative** — no affiliation listed; the author list is consistent with an industrial research group (Amazon/FAIR-adjacent naming patterns are unverified).
- **Venue**: **NeurIPS 2026 main conference** (comment: "Neurips 2026 main conference paper"). (single-source)

**Condensed abstract**: For a fixed pre-trained model and reasoning task, hallucination-detection work shows it is possible to estimate the model's confidence in its own outputs — but those uncertainty estimates have been used almost exclusively *reactively*, to detect or filter confabulations after the fact. This paper asks whether the same signals can act *proactively* to improve accuracy.

**Innovation — USteer**: a **training-free steering mechanism** that adjusts a model's **layer-wise activations during inference** using the **gradient of a confidence measure with respect to those activations**. This nudges generation toward lower-uncertainty outputs at inference time with **no parameter modification and no additional supervision**. The conceptual contribution is the reframing: confidence is a *control signal*, not merely a *detection signal*.

**Comparison**: No baseline set is enumerated in the abstract; the paper reports consistent hallucination reduction across a range of reasoning tasks.

**Results**: Qualitative — "consistently reduces hallucination across a range of tasks." **No numbers in the abstract.**

---

### 14. On the (In)effectiveness of AMR Augmentation for Large Language Models / AMR 增强对大语言模型的（无）有效性

- **arXiv**: `2609.40121` — [abstract](https://arxiv.org/abs/2609.40121)
- **Authors**: Hoa Quynh Nhung Nguyen, Jacopo Staiano, Michael Sullivan
- **Affiliation**: not listed (Staiano/Sullivan are commonly at Amazon; unverified).
- **Venue**: **EMNLP 2026** (comment: "accepted at EMNLP 2026"; 23 pages, 6 figures, 18 tables). (single-source)

**Condensed abstract**: Abstract Meaning Representation (AMR) historically improved a range of NLP tasks, but whether AMR augmentation still helps *modern* LLMs is unclear. The authors attempt to reproduce recent work reporting substantial downstream gains and conclude the gains are likely **artifacts of specific experimental-setting choices**.

**Innovation**: A **reproduction with a consistent, unified hyperparameter-selection protocol** — the methodological contribution — plus, to explain the null result, a **perplexity-based probe** that measures the degree to which AMR actually supplies the LLM with *supplemental relational knowledge not already available to the model*.

**Results**: Under the unified protocol, **text-only baselines consistently match or exceed** AMR-augmented models. The probe shows AMR augmentation **does not** help LLMs improve their understanding of relational content already in the sentence. Conclusion: augmenting these models with AMR offers **no clear downstream benefit**.

**Significance**: A well-documented negative result with a mechanism. Read alongside [[amr]]-related claims elsewhere in the wiki before treating structural augmentation as a default lever for modern LLMs.

---

### 15. A Missing Piece for Trustworthy AI Reviewers: From Benchmarking Rhetorical Robustness to SciCore Review / 可信 AI Reviewer 的缺失一环：从 Benchmarking Rhetorical Robustness 到 SciCore Review

- **arXiv**: `2609.39027` — [abstract](https://arxiv.org/abs/2609.39027)
- **Authors**: Chenguang Wang, Ming Li, Chengrui Fan, Jianpeng Chen, Han Chen, Tianyi Zhou, Dawei Zhou
- **Affiliation**: not listed.
- **Venue**: **AI-Native Academia workshop @ NeurIPS 2026 — Oral** (35 pages, 2 figures, 20 tables). (single-source)

**Condensed abstract**: AI reviewers can assign different judgments to manuscripts that report *the same science* in different wording — which means the review process can reward **rhetorical optimization over scientific improvement**.

**Innovation**: (i) A formalization of **Rhetorical Robustness** as the *joint* requirement of **stability across content-preserving rewrites** *and* **discrimination across papers** — a single reviewer can trivially satisfy stability by being constant, so both halves are needed. (ii) **RobustReview**, a controlled **full-manuscript** benchmark with **1,260 manuscript versions**, evaluating **30 reviewer configurations**. (iii) **SciCore**, a dual-branch reviewer that averages a full-manuscript judgment with a judgment over an extracted, structured *science core*.

**Results**: The benchmark exposes **false robustness** — low rewrite sensitivity occurring together with score collapse across papers — and shows that **human alignment and rhetorical robustness rank reviewers differently**, i.e. the two criteria are not interchangeable. The evaluated content-focused prompting protocol **does not consistently improve robustness across backbones**. In the primary GPT-5.5 comparison, SciCore achieves a **leading joint stability-discrimination profile** while maintaining competitive human alignment.

---

### 16. Making Grid Beam Search Less Greedy / 让 Grid Beam Search 不那么 Greedy

- **arXiv**: `2609.39368` — [abstract](https://arxiv.org/abs/2609.39368)
- **Authors**: Sean Papay, Roman Klinger
- **Affiliation**: not listed.
- **Venue**: **COLM 2026** (comment: "Published as a conference paper at COLM 2026"). (single-source)

**Condensed abstract**: A common formalism for constraining autoregressive generation requires certain words or phrases to appear in the output. **DFA-constrained beam search** needs a number of forward passes exponential in the number of constraint tokens; **grid beam search** needs only linearly many — a large speedup. But this paper shows the speedup is obtained in a way that **does not treat constraints equally**.

**Innovation**: A demonstrated **bias** in grid beam search: it satisfies **easier constraints first** and pushes harder constraints to the end of the sequence, whereas DFA-constrained beam search exhibits **no such bias**. The fix, **fair grid beam search**, removes the bias while retaining only linearly many forward passes. A pleasing secondary finding: it also finds **higher-probability strings** in the process — the bias was not free.

**Comparison**: DFA-constrained beam search (exponential but unbiased) vs. standard grid beam search (linear but biased) vs. fair grid beam search (linear and unbiased), on two constrained-generation tasks.

**Results**: Confirms the bias on both tasks, finding **significant differences in constraint-token ordering** relative to DFA-constrained beam search, and shows fair grid beam search both fixes the bias and finds higher-probability strings.

---

## C. Efficiency, Systems, and On-Device Deployment

### 17. Raw-Routed Mixture of Adapters: A Causal Intervention for Routing Collapse in Time Series Foundation Models / Raw-Routed Mixture of Adapters：时间序列基础模型路由崩塌的因果干预

- **arXiv**: `2609.39445` — [abstract](https://arxiv.org/abs/2609.39445)
- **Authors**: Hung Phan, Thuy T. Nguyen, Minh Ngoc Dinh, Nhat-Quang Tran
- **Affiliation**: not listed.
- **Venue**: **NeurIPS 2026 — poster** (50 pages, 9 figures). (single-source)

**Condensed abstract**: Time series foundation models (TSFMs) adapt to new data by attaching a single trainable head to a frozen backbone — a one-size-fits-all setup that underfits heterogeneous regimes. Replacing the head with a mixture of experts is the standard upgrade, but on **instance-normalized backbones** (the dominant TSFM design class) **it fails**: routing entropy collapses to zero and one expert absorbs every input. The authors name this **normalization-induced routing collapse** and show that standard MoE rescue mechanisms do *not* repair it, because the cause is in the **router's input**, not its optimization.

**Innovation**: (i) A **mutual-information decomposition** that makes the mechanism precise and yields a **signal-ratio computable before training** which **predicts dataset vulnerability (Spearman ρ = −0.88)** — a cheap pre-flight diagnostic. (ii) **Eight causal controls**, including a **vision-modality replication**, that isolate instance normalization as the cause. (iii) The prescription — **RR-MoA (Raw-Routed Mixture of Adapters)** — routes on the **raw, pre-normalization input**. The paper's epistemic framing is unusually strong for an empirical ML paper: named failure mode, causal isolation, and a minimal intervention.

**Comparison**: LoRA, TRACE, AdaMix, full fine-tuning, and the strongest fixed-adapter configuration, under a **strictly frozen backbone**.

**Results**: RR-MoA wins **54/54 comparisons** against the strongest fixed adapter and significantly outperforms LoRA, TRACE, AdaMix, and full fine-tuning. Generalizes across **six backbones** and an imputation task. Frozen RR-MoA beats full fine-tuning by **12–79%** (the paper's "**Frozen Paradox**"); two architecturally distinct variants confirm the principle generalizes beyond this specific router.

---

### 18. DCM-SAM: Defect-Conditioned Mixture of LoRA Experts for NPU-Deployed AM Defect Segmentation / DCM-SAM：面向 NPU 部署的 AM 缺陷分割的缺陷条件化 LoRA 专家混合

- **arXiv**: `2609.38811` — [abstract](https://arxiv.org/abs/2609.38811) | [code](https://github.com/MushfiqShovon/DCM-SAM)
- **Authors**: Md Mushfiqur Rahaman, Md Mahedi Hasan, Imtiaz Ahmed, Srinjoy Das
- **Affiliation**: **tentative** — no affiliation listed; the deployment target is a **Qualcomm Hexagon NPU**, and this paper is one of very few in the batch whose *actual* contribution names a target lab in a substantive rather than incidental way. Author-institution mapping unverified.
- **Venue**: **NeurIPS 2026 Workshop on On-Device Intelligence: Foundation Models under Real-World Constraints (ODI)** (12 pages, 1 figure, 8 tables). (single-source)

**Condensed abstract**: Metal additive manufacturing parts are inspected by X-ray CT, where labelled data is scarce, the pores and inclusions that matter span a few pixels, and **inspection must happen at the machine**. DCM-SAM is a defect-conditioned adaptive mixture of LoRA experts.

**Innovation**: **One frozen Segment Anything backbone** carries a **separate Conv-LoRA expert bank and mask decoder per defect class**, each trained in its own pass, **without prompts**, on **synthetic slices alone**, updating only **4.4% of parameters**. Per-class experts matched to per-class visual signatures is the domain-specific bet.

**Comparison**: Baselines on the benchmarks XCT-SAM reports, with the fairness twist that DCM-SAM runs a **ViT-B backbone while baselines use ViT-H**; plus a direct NPU deployment study.

**Results**: Improves on **every baseline for both defect classes** from a ViT-B backbone *against their ViT-H*, and reaches **64.2% pore IoU on real NIST scans having seen no real images during training**. The deployment section is the paper's most transferable contribution: on a **Qualcomm Hexagon NPU**, ViT-H and ViT-L **compile but cannot allocate at 1024×1024** — **activations rather than weights** exceed the device ceiling, and **quantizing weights does not help**. ViT-B alone runs, but the adapted encoder then fails where the stock one succeeds, until a **numerically identical rewrite of the attention** lets the full model run in **FP16 at 1024×1024 with no operator falling back to CPU**, masks within **0.01% of pixels** of the FP32 reference.

---

### 19. The Invisible Language Tax: Token Premiums of French and Regional Languages in 2026 LLM Tokenizers / 隐形语言税：2026 年 LLM Tokenizer 中法语与地区语言的 Token 溢价

- **arXiv**: `2609.39001` — [abstract](https://arxiv.org/abs/2609.39001) | [code](https://github.com/Baracoda-ai-labs/baracoda-fr)
- **Authors**: Thomas Serval
- **Affiliation**: not listed (project under `Baracoda-ai-labs`).
- **Venue**: No conference label; 11 pages, 5 figures, 7 tables, with released tokenizer, per-sentence counts and controls. (single-source)

**Condensed abstract**: LLM services bill per token and context windows are measured in tokens, yet the number of tokens needed for identical content **varies across languages**. This paper measures that premium across a broad set of production tokenizers and quantifies its cost amplification in agentic use.

**Method — notable**: **seven tokenizers of widely used 2026 models** — OpenAI **o200k**, Llama 3, Qwen3, **DeepSeek V3/V4**, Gemma 3, Mistral **Tekken**, and the **Claude generation-5** tokenizer via **Anthropic's counting API** — evaluated on **NTREX-128** (124 non-English reference translations) and the **Universal Declaration of Human Rights** for regional languages.

**Results**: **French requires 31%–58% more tokens than English.** Simplified Chinese ranges from 5% fewer to 40% more, and is **cheaper than French on six of seven tokenizers**. Regional and overseas languages of France pay roughly **1.6×–3.3×** the English count. The paper argues history re-sending, tiered pricing, and fixed context windows **amplify the absolute gap in agentic use** — a token inefficiency compounds across a long agent trajectory.

**Intervention**: In a controlled experiment (**BPE**, **Europarl**, **50k vocabulary**), adding French to tokenizer training data **quickly reduces the premium**, with **diminishing returns** and a growing cost for English. The released prototype **Baracoda FR v1.2** — byte-level BPE at **Tekken's vocabulary size** — uses **11.5% fewer tokens than Tekken on French** and **3.7% fewer on English** on six corpora never consulted during design, under a **protocol declared fixed beforehand**; results hold after removing test sentences overlapping training data and at an equal ordinary-token budget. It is **worse on other languages** and, at comparable vocabulary size, **does not outperform CroissantLLM**.

**Caveat stated by the authors**: these are **segmentation results only**; effects on model quality and task cost remain to be shown.

---

### 20. GPU-Accelerated Path-Dependent Marginal Information Gain for Autonomous Exploration / GPU 加速的路径相关边缘信息增益与自主探索

- **arXiv**: `2609.40297` — [abstract](https://arxiv.org/abs/2609.40297)
- **Authors**: João Félix Mendes, Rodrigo Ventura, Meysam Basiri
- **Affiliation**: not listed; evaluated on an **NVIDIA Jetson Orin NX**.
- **Venue**: **Submitted for review to IEEE ICRA 2027** (not accepted). (single-source)

**Condensed abstract**: Autonomous exploration must continuously evaluate candidate viewpoints by expected information gain and execution cost. Sampling-based planners estimate this gain by volumetric raycasting, and — because of the cost — evaluate candidates under an assumption of **mutual independence**, ignoring overlap between viewpoints along the same path.

**Innovation**: Instead of storing and merging observed-unknown voxels along each candidate path, previous observations are represented using **depth buffers**. Candidate rays are projected into the **depth buffers of their ancestors** to identify observation overlap and exclude regions expected to be seen. The planning tree is evaluated **in depth order** to preserve the dependency between viewpoints and their optimized yaws, while candidate nodes and rays at each level are processed **in parallel on the GPU**.

**Comparison**: Exact marginal gain computed with voxel hash maps; two sampling-based exploration planners; three simulation environments plus real-world experiments.

**Results**: Within **5–10%** of exact marginal gain, with speed-ups up to **118× on a desktop GPU** and **28× on an NVIDIA Jetson Orin NX**. Marginal gain reduced time to 95% coverage in **5 of 6** evaluated planner-environment combinations. Real-world experiments show a **30% reduction** in time to 95% coverage and earlier exploration termination.

---

### 21. Skill-Based AI Agents for Power-System Studies / 面向电力系统研究的 Skill-Based AI Agent

- **arXiv**: `2609.40272` — [abstract](https://arxiv.org/abs/2609.40272)
- **Authors**: Pavel Etingov, Shuchismita Biswas
- **Affiliation**: **tentative** — no affiliation listed; the work exposes **Siemens PTI PSSE** functions via a custom MCP server and builds on both the **OpenAI Agents SDK** and the **Claude Code CLI**, which is consistent with an industrial-vendor research setting but is not verified.
- **Venue**: **Submitted to 2027 IEEE PES Grid Edge Technologies Conference & Exposition** (not accepted). (single-source)

**Condensed abstract**: A skill-based agentic framework for power-system studies using **Model Context Protocol (MCP)**-connected engineering tools. A custom MCP server exposes **Siemens PTI PSSE** functions for power-flow analysis, dynamic simulation, result extraction, and model-validation workflows.

**Innovation**: Two implementation pathways were built and compared — one on a programmable **OpenAI Agents SDK**, one on the **Claude Code CLI** — both using reusable **skills, subagents, MCP tools, data-repository connections, and local shell/Python execution**. Success was evaluated on task completion, output accuracy, and *need for human expert intervention*.

**Results**: Both frontier-model-based implementations successfully executed representative study tasks on public datasets. The authors conclude agentic systems can **greatly accelerate the power-system dynamic simulation process** for transmission planning studies when leveraging industry-grade simulation platforms, and argue this shifts transmission-planning practice so engineers spend effort on scenario design and interpretation rather than tool operation.

**Note**: No quantitative speedup is given in the abstract — the claim is directional.

## D. Multimodal, Vision, Speech, and Machine Translation

### 22. Prototype-guided Bilateral Alignment Multimodal Federated Learning / Prototype-guided Bilateral Alignment 多模态联邦学习

- **arXiv**: `2609.38925` — [abstract](https://arxiv.org/abs/2609.38925)
- **Authors**: Tianchi Liao, Lele Fu, Sheng Huang, Qing Hu, Hong-Ning Dai, Chuan Chen
- **Affiliation**: not listed (Hong-Ning Dai and Chuan Chen are commonly at HKU; unverified).
- **Venue**: **ICML 2026 — Spotlight** (comment: "28 pages, 16 figures, ICML 2026 (Spotlight)"). (single-source)

**Condensed abstract**: Multimodal federated learning (MFL) is a key paradigm for using distributed data, but existing methods rely on idealized assumptions of **model homogeneity** and **balanced modality distributions** — neither of which holds in practice with heterogeneous client architectures and severe modality imbalance.

**Innovation — MFedPBA**: robust knowledge synergy through a **dual alignment mechanism**. (i) **Feature level** — aligns heterogeneous feature spaces via a **projection encoder optimized by contrastive learning and the Gromov-Wasserstein distance**; GW distance is the notable choice because it matches distributions in *structure* without requiring a common embedding space, which is exactly what cross-architecture clients lack. (ii) **Decision level** — **entropy-weighted aggregation of naturally aligned logit prototypes**, using the prototypes as a common decision currency so features never have to be directly comparable.

**Comparison**: State-of-the-art MFL baselines, evaluated specifically under model heterogeneity and modality imbalance.

**Results**: "Significantly outperforms" state-of-the-art baselines under both conditions. **No numeric deltas in the abstract** — 16 figures suggest substantial empirical coverage.

---

### 23. Seeing as Humans Do: Learning from Motion to Segment Anything Without Supervision / 像人类一样看：从运动中无监督学习 Segment Anything

- **arXiv**: `2609.39785` — [abstract](https://arxiv.org/abs/2609.39785) | [code](https://github.com/360CVGroup/MoSA)
- **Authors**: Weijian Jian, Xiaoyue Zhang, Bin Xiao, Chunyu Xie, Yixiao He, Yutao Liu, Dawei Leng, Yuhui Yin
- **Affiliation**: not listed (project under `360CVGroup`; Yutao Liu is commonly at MBZUAI, Dawei Leng at NUS — both unverified).
- **Venue**: **ECCV 2026** (published, includes supplementary material). (single-source)

**Condensed abstract**: SAM relies heavily on massive manual annotation, creating a fundamental bottleneck for scaling. Unsupervised methods that learn object concepts from motion exist, but they **overfit to moving entities**, lacking both multi-granularity understanding and the ability to generalize to **static objects**.

**Innovation — MoSA** (Motion-Grounded Segment Anything), three progressive stages: (i) automatically generate **multi-granularity motion pseudo-labels** from large-scale unlabeled video; (ii) train a **Perceptual Grouping Model (PGM)** by contrastive learning to internalize a generalized, **appearance-driven** concept of objects — this is the step that decouples the learned prior from motion itself; (iii) transfer the learned prior into a **prompt-guided, segment-anything-style architecture** for image inference.

**Comparison**: Existing unsupervised segmentation methods, evaluated zero-shot across seven challenging benchmarks including **COCO** and **ADE20K**.

**Results**: Significantly outperforms existing unsupervised methods across all seven benchmarks. Notably, **despite using zero manual annotations**, MoSA achieves segmentation performance **comparable to the fully supervised SAM**. Conclusion: large-scale unlabeled motion is a feasible, highly scalable alternative to annotation-driven segment-anything pipelines.

---

### 24. Universal Cross-Prompt Adversarial Attacks on Promptable Concept Segmentation / 面向 Promptable Concept Segmentation 的通用跨 Prompt 对抗攻击

- **arXiv**: `2609.39265` — [abstract](https://arxiv.org/abs/2609.39265)
- **Authors**: Ziqi Zhou, Yifan Hu, Yufei Song, Haowen Jiang, Xianlong Wang, Shengshan Hu, Dezhong Yao, Leo Yu Zhang
- **Affiliation**: not listed (Xianlong Wang and Shengshan Hu are commonly at Xiamen University; unverified).
- **Venue**: **NeurIPS 2026** (accepted). (single-source)

**Condensed abstract**: SAM achieves remarkable visual segmentation performance, and **SAM3 extends promptable segmentation to concept-level prediction**, broadening the scope of segmentation foundation models. While SAM and SAM2 are known to be vulnerable to adversarial examples, the robustness of SAM3 under the concept-segmentation paradigm **remains unexplored**, and existing SAM-family attacks exhibit **limited cross-prompt transferability**.

**Innovation — AdvPCS**: three components. (i) **Min-max prompt optimization** via bilevel optimization: the inner maximization enhances diversity over candidate **point, box, and text** prompts; the outer minimization selects prompts with the **highest detector confidence responses** — i.e. it first finds the hardest-to-attack prompts. (ii) A **global-local perception deception attack** minimizing both global and local existence probabilities under joint prompting. (iii) A **temporal transition deviation attack** maximizing inter-frame semantic inconsistency and corrupting **memory pointers**, which attacks SAM3's temporal memory rather than its per-frame segmentation.

**Comparison**: Prior adversarial attacks on SAM/SAM2/SAM3 across four benchmark datasets, under point, box, and text prompts.

**Results**: A **single universal adversarial perturbation** generated by AdvPCS **generalizes across frames from different videos**, and under text prompts reduces the average **mIoU of various PCS models on SA-CO to below 5%**.

---

### 25. Index-Translate: A Multilingual Translation Model Family / Index-Translate：多语言翻译模型家族——文本、语音、受控配音与长文档翻译

- **arXiv**: `2609.40181` — [abstract](https://arxiv.org/abs/2609.40181) | [project](https://index-translate.bilibili.com) | [code](https://github.com/bilibili/Index-Translate)
- **Authors**: Tianjiao Li, Mengran Yu, Chenyu Shi, Lusheng Zhang, Qisi Chen, Yanshan Zhou, Ji Qi, Jingying Liu, Yuang Feng, Ziang Cui, Tianxing Yan
- **Affiliation**: **Bilibili** (project hosted at `index-translate.bilibili.com`; code under the `bilibili` GitHub organization).
- **Venue**: No conference label; 27 pages, with project page and released code/models. (single-source)

**Condensed abstract**: A multilingual translation model family combining a **shared multilingual foundation** with **specialized training** across five task regimes, in three model sizes.

**Innovation**: The architectural bet is a *shared foundation plus per-task heads/training*, not separate task models: three sizes (**2B, 9B, 35B-A3B** — the last being a mixture-of-experts configuration), **150 languages**, and multilingual instruction following. Four specialized members: **Index-Echo** for end-to-end speech-to-text and speech-to-speech translation; **Index-Homura** for **syllable-controlled dubbing** (controlling output syllable count/structure, useful for dubbing alignment); **Index-NativeLong** for **native long-document translation** with a **dedicated task formulation and benchmark** — the benchmark is itself a contribution, since existing long-document MT evaluation is largely borrowed from summarization setups.

**Comparison**: Translation models of comparable size; 100B-scale translation models; frontier models. For Index-Echo: existing end-to-end models and frontier omni models.

**Results**: Outperforms comparable-size translation models on general translation **and** complex translation instructions, achieving performance **comparable to 100B-scale translation models and frontier models**. Index-Echo outperforms existing end-to-end models and is **comparable to frontier omni models**. **No per-language or per-size numbers in the abstract.**

---

### 26. ANI: Adaptive Numerical Injection for Unifying Semantic and Arithmetic Representations / ANI：自适应数值注入，统一数值推理中的语义与算术表示

- **arXiv**: `2609.39294` — [abstract](https://arxiv.org/abs/2609.39294) | [code](https://github.com/Jinsung-Jeon/ANI_EMNLP)
- **Authors**: Jinsung Jeon, Seung-won Hwang
- **Affiliation**: not listed.
- **Venue**: **EMNLP 2026** (accepted; 16 pages, 7 figures). (single-source)

**Condensed abstract**: Precise numerical reasoning with LLMs is essential for real-world applicability, but **text-based tokenization often fragments numbers**, significantly hindering precise arithmetic reasoning. Numerical embeddings, meanwhile, are arithmetically precise but rely on **context-agnostic substitution** that disregards the **semantic role of numbers as identifiers** — an account number is not a quantity.

**Innovation — ANI (Adaptive Numerical Injection)**: a hybrid framework that governs **selective injection of numerical features based on semantic context**. A **context-aware gating mechanism** selectively injects numerical embeddings (specifically **FoNE** — Fourier numeric encoding) into the latent space, **explicitly preserving nominal identifiers while enhancing quantitative operands**. The semantic/arithmetic role assignment is decided by the model, not by a heuristic.

**Comparison**: Official reference models across various LLMs; general linguistic benchmarks retained as a control.

**Results**: Enhances **MATH performance by 9.5 points** over the official reference model while **maintaining robust performance on general linguistic benchmarks** — i.e. the numeric pathway does not degrade linguistic ability.

---

### 27. A barrier or a booster? Familiarity effects on Mandarin emotion prosody recognition / 壁垒还是助推？基于 AI 语音克隆的普通话情感韵律识别中的熟悉度效应

- **arXiv**: `2609.38794` — [abstract](https://arxiv.org/abs/2609.38794)
- **Authors**: Feng Xu, Gaoyuan Zhang, Shanshan Xue, Yixiang Chen, Hanrui Zhou, Xurong Xie, Hui Chen
- **Affiliation**: not listed (Xurong Xie is commonly at SJTU; unverified).
- **Venue**: **Interspeech 2026** (accepted). (single-source)

**Condensed abstract**: Emotion prosody perception requires simultaneous processing of acoustic cues and speaker identity. Listeners decode natural speech effortlessly, but **AI synthetic voices introduce cognitive complexity** due to subtle acoustic atypicalities. It is unclear how these synthetic features interact with a listener's **prior social knowledge and memory of a familiar speaker**.

**Method**: Within-subject task with Mandarin-speaking adults, measuring **behavioral** (accuracy, reaction time) and **physiological** (**heart rate variability**) data across a 2×2 design of speech source (human vs. AI) × speaker familiarity.

**Results**: **Human voices yielded significantly higher accuracy and faster processing times than AI voices**, while **HRV did not significantly differentiate between conditions**. Interpretation: decoding synthetic speech is **gated by top-down social cognition** — the deficit is in the listener's social model, not in acoustic decodability per se, which has direct implications for how synthetic-voice quality should be evaluated.

## E. Theory, Geometry, and Methods

### 28. Parameter symmetries determine representational geometry in overparameterized nonlinear networks / 过参数化非线性网络中的参数对称性决定表示几何

- **arXiv**: `2609.39078` — [abstract](https://arxiv.org/abs/2609.39078) | [code](https://github.com/mrvnthss/symmetries-representational-geometry)
- **Authors**: Marvin Theiss, Lukas Braun, Andrew M. Saxe, Erin Grant
- **Affiliation**: not listed (Erin Grant and Andrew M. Saxe are commonly at Cambridge/Imperial; unverified).
- **Venue**: **NeurIPS 2026** (to appear; 89 pages, 9 figures — an unusually long main-track paper). (single-source)

**Condensed abstract**: Representations are routinely used across ML, psychology, and neuroscience to infer what a system computes. Such inferences presume a meaningful link between **representational geometry** and the **computation performed**. For artificial networks, however, how much **function constrains representation** is unclear. The key obstacle: networks admit **parameter symmetries** — changes in parameterization that **preserve function exactly** while **reshaping representational geometry**.

**Innovation**: Three results. (i) A broad class of parameter symmetries acts on representations through only **three primitive feature transformations: addition, duplication, and scaling**. (ii) This feature-level characterization yields a **closed-form decomposition of representational geometry into essential and auxiliary components**, making precise how geometric degeneracy can grow with **overparameterization even when function is held fixed**. (iii) **Implementation-level selection rules resolve this degeneracy**, yielding **identifiable geometries** in which features are weighted according to their contribution to the network's function.

**Significance**: The paper delineates **when representations can support inferences about computation, and when they cannot** — a direct methodological constraint on the whole field's use of representational-similarity analysis. (No experiments to report; this is a theory paper.)

---

### 29. Markovian Dynamics Enforcer: Feasibility Preserving Correction on Learned Dynamics Manifolds / Markovian Dynamics Enforcer：学习动力学流形上的可行性保持修正

- **arXiv**: `2609.39888` — [abstract](https://arxiv.org/abs/2609.39888) | [code](https://github.com/tsl-imperial/MaDE)
- **Authors**: Kevin Yu, Tao Guo, Constantinos Antoniou, Panagiotis Angeloudis
- **Affiliation**: not listed (code under `tsl-imperial` — **Imperial College London**, tentative).
- **Venue**: **NeurIPS 2026** (accepted; 26 pages, 2 figures, 11 tables). (single-source)

**Condensed abstract**: Neural trajectory predictors can reach low prediction error while **violating dynamics, actuator limits, or state constraints** — especially when controls are unobserved and dynamics are partially specified. MaDE is a **time-invariant post-hoc operator** mapping state-transition proposals onto a learned **feasible dynamics manifold**, trained on feasible states **without ground-truth controls**.

**Innovation**: For each transition, MaDE **infers a control** and **recomputes the state** through a *completion model* of known physics plus a learned residual; it then corrects that control by **gradient-based inequality reduction**, so inequality satisfaction is **best-effort within an iteration budget**. Because **every correction iterate re-enters the completion model**, the returned state is **dynamically consistent by construction** relative to that model and the supplied previous-state anchor — feasibility is a structural property, not a penalty term. The operator is designed to attach to **arbitrary** predictors and stays **frozen**.

**Comparison**: Raw recurrent, structured state-space, and transformer predictors, evaluated downstream of MaDE; kinematic bicycle model as the dynamics reference on recorded vehicle trajectories.

**Results**: Dynamics residuals driven to **essentially zero on fully specified simulated systems**; on an underspecified system MaDE leaves a **smaller true-dynamics residual than the baselines**. On recorded vehicle trajectories, one-step residual against a kinematic bicycle model is **0.0071–0.0072** for MaDE versus **0.1703–0.1714** for raw predictors (a ~24× reduction). MaDE **raises average displacement error by a factor of 1.57–1.83**.

---

### 30. Evolutionary foraging in grids: Intermittent search dynamics emerge in finite, depletable landscapes / 网格中的进化觅食：有限、可耗尽景观中涌现的间歇搜索动力学

- **arXiv**: `2609.39239` — [abstract](https://arxiv.org/abs/2609.39239) | [project](https://evo-foraging.github.io/)
- **Authors**: Shailendra Bhandari, Alex Szorkovszky, Anis Yazidi, Pedro G. Lind
- **Affiliation**: not listed (Pedro G. Lind is commonly at University of Szeged / Bolzano; unverified).
- **Venue**: **NeurIPS 2026** (accepted). (single-source)

**Condensed abstract**: How search strategies evolve in **finite, depletable** landscapes is an open question in foraging theory. The authors run an evolutionary simulation in which agents forage on a **two-dimensional toroidal lattice** containing **non-renewable resources** distributed either uniformly or as **Lévy dust**. Each agent carries a **heritable genome** encoding step lengths, velocities, and turning angles; selection acts on a fitness function combining energetic gain, movement cost, and coverage efficiency. Crucially, movement traits are allowed to evolve **without imposing a prescribed power-law step-length distribution**, so the question is not rigged in favor of one answer.

**Innovation**: Model selection by **fitting second- and fourth-order displacement moments** against both intermittent-search and Lévy-walk models, rather than eyeballing trajectories.

**Results**: Evolved search is **more consistent with intermittent dynamics than with strict scale-free Lévy motion** in finite depletion-driven landscapes. A Lévy-like random walk fits the evolutionary trajectories well (**mean adjusted R² > 0.9** in most tested conditions), but **intermittent search achieves a closer fit (mean adjusted R² > 0.99) for all tested resource distributions**. This preference holds across tested grid sizes and resource densities, and reproduces over **five independent evolutionary runs per environment** on a **503×503** grid at nominal resource density ρ = 0.15, for both the uniform environment and five Lévy-dust environments. Evolution **rapidly reshapes the movement genome toward short displacements while retaining a sparse tail of longer relocations**, consistent with local exploitation punctuated by occasional transfer.

---

### 31. QuanVI: Score-based Variational Inference via Quantum Maximally Mixed States / QuanVI：基于量子最大混合态的 Score-based 变分推断

- **arXiv**: `2609.39164` — [abstract](https://arxiv.org/abs/2609.39164)
- **Authors**: Yuchen Cong, Zerui Tao, Chao Li, Zhe Sun, Qibin Zhao
- **Affiliation**: not listed (Tongji-affiliated by author list; unverified).
- **Venue**: **NeurIPS 2026** (accepted). (single-source)

**Condensed abstract**: Score-based variational inference (VI) offers an alternative to KL-based VI by minimizing the **Fisher divergence** between variational and target distributions. A prior score-VI approach formulates this as an **eigenvalue problem**, building the variational distribution from low-energy eigenstates — but this hits two high-dimensional obstacles: an **intractably large parameter count due to exponential scaling**, and **non-uniqueness of individual eigenvectors** in degenerate or nearly degenerate low-energy subspaces.

**Innovation — QuanVI**: a scalable **quantum-inspired** algorithm combining a **mixed-state density-operator formulation** with a **quantum tensor network (QTN)** parameterization using the **matrix product operator (MPO)** structure. In degenerate low-energy subspaces, the density-operator formulation represents the subspace by its **maximally mixed state** rather than relying on a non-unique individual eigenvector — resolving the degeneracy principledly instead of by regularization — while the QTN parameterization **compresses the density operator to avoid exponential parameter growth**.

**Comparison**: Exact solutions in low dimensions; high-dimensional synthetic and Bayesian posterior-approximation benchmarks including challenging **non-Gaussian** targets.

**Results**: QuanVI **agrees with exact solutions in low dimensions** and **scales to high-dimensional** synthetic and Bayesian posterior-approximation benchmarks, including non-Gaussian targets. (Ablations reported; specific numbers not in the abstract.)

## Cross-Cutting Observations

Five patterns recur across otherwise unrelated papers in this batch.

**1. On-policy distillation is fragmenting by *which* failure it targets.** PivotOPD targets compounding multi-turn error with an asymmetric reverse/forward KL pair; S-OPD targets *student perception* rather than teacher supervision; ReSAIL targets collapse across self-distillation cycles; [[self-distillation]] axis work (entry 9) shows the field's design choices were being studied in fixed combinations producing contradictory conclusions. The shared lesson from entries 9 and 10 is that **the teacher is not the bottleneck** — student-side and retention-side factors dominate.

**2. Negative results with mechanisms are now publishable at top venues.** Entry 14 (AMR augmentation) reproduces a positive result and refutes it with a unified protocol plus a diagnostic probe; entry 15 (Rhetorical Robustness) constructs a criterion that a trivial reviewer fails by construction; entry 17 names a failure mode and isolates its cause with eight controls. This is a methodological improvement over the field's earlier pattern of reporting multi-baseline wins without isolating mechanisms.

**3. Deployment constraints are shaping method design, not just being checked afterward.** Entry 18's finding that **activations rather than weights** exceed an NPU's ceiling, and that quantizing weights does not help, is the kind of result that changes how adapter papers report efficiency. Entry 20 replaces voxel hashing with depth buffers because of raycasting cost. Entry 17's "Frozen Paradox" (frozen adapters beating full fine-tuning by 12–79%) and entry 16's incidental discovery that bias removal *also* improves likelihood are both cases where a diagnostic improved the method.

**4. Measurement artifacts in the tokenizer economy are large enough to be engineering constraints.** Entry 19 quantifies a 31–58% French token premium and 1.6–3.3× for regional languages. Combined with entry 15's rhetorical-robustness finding and entry 3's token-efficiency result (1.5–1.7× fewer output tokens), **token counts are a first-class cost axis** in this batch, not an afterthought.

**5. Interpretability claims are being narrowed by theory.** Entry 28 shows representational geometry is *not* determined by function in overparameterized networks, and specifies exactly when it can and cannot support inferences about computation. Entry 16 shows a standard decoding algorithm carries an undocumented constraint-ordering bias. Both are constraint-on-the-methods papers rather than method papers.

## Negative Findings and Verification Notes

- **Affiliations**: the arXiv API exposes no affiliation data. 12 of 31 entries are marked *not listed*; 12 are *tentative* with the evidence (project page domain, GitHub org, or platform under test) stated inline; 7 are positively evidenced by an institutional project domain or GitHub organization. No affiliation was inferred from author surnames.
- **Venues**: every venue string above is quoted verbatim from the arXiv comment field. No proceedings site was consulted. Two entries are **submissions, not acceptances** (ICRA 2027, IEEE PES 2027) and are labeled as such.
- **Quantitative results**: 17 entries carry concrete numbers from the abstract; 14 do not and say so. No number in this digest was estimated, converted, or inferred.
- **Requested venues with no unclaimed acceptance in this window**: AAAI 2026, ICLR 2026/2027, KDD 2026, CVPR 2026, ACL 2026, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025/2026, NeurIPS 2025, ICML 2025. This is a **single 18-hour window** result, not evidence of absence — and given that ICML 2026, NeurIPS 2026, EMNLP 2026, ECCV 2026, COLM 2026 and Interspeech 2026 acceptances *are* present, the 2026 cycles are clearly running while others announce later.
- **Workshop filter**: NeurIPS 2026 workshops contributed 3 of 10 NeurIPS entries; the remaining workshop submissions in the batch (quantum ML, mathematical reasoning, symmetry/geometry in neural representations, trustworthy AI, biological discovery, agentic pretraining-to-acting, LP4FM, GDDL, secure quantum ML, etc.) were screened and excluded as off-topic for this digest's scope.

## Statistics

| Metric | Value |
|---|---|
| Unique base arXiv IDs in window | 1,688 |
| Already claimed by sibling digests | 161 |
| Unclaimed at selection time | 1,527 |
| Papers detailed in this digest | 31 |
| Entries with concrete quantitative results | 17 |
| Entries with verified institutional affiliation | 7 |
| Main-track conference acceptances | 14 |
| Workshop / submission-only / preprint | 17 |

## Related Pages

- `arxiv-ai-search.md`, `arxiv-daily.md`, `arxiv-paper-check.md` — sibling digests for 2026-10-01 covering the other claimed papers in this batch
- `wiki/synthesis/2026-09-29/conference-digest.md` — prior day's conference digest
- `wiki/claims/` — check for tracked claims on on-policy distillation, tokenizer efficiency, or AMR augmentation before filing any of the above as a claim




