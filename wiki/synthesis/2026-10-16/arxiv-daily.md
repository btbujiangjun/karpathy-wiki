---
title: arXiv Daily AI/LLM/RecSys/CTR/Games (2026-10-16)
type: synthesis
created: 2026-10-16
updated: 2026-10-16
sources: [arxiv-listing, arxiv-html]
tags:
  - arxiv
  - ai
  - llm
  - recommendation
  - advertising
  - sequential-modeling
  - ctr
  - games
  - daily-digest
---

# arXiv Daily Report (2026-10-16)

Search scope: the arXiv **export API** was rate-limited (HTTP 429) on every free-text `submittedDate`/`sortBy` query at run time, so this run harvested directly from the public **listing pages** (`arxiv.org/list/{cat}/pastweek?skip=0&show=2000`) across **26 primary categories** (`cs.AI`, `cs.LG`, `cs.CL`, `cs.IR`, `cs.GT`, `cs.MA`, `cs.MM`, `cs.CY`, `cs.NE`, `cs.SI`, `cs.SE`, `cs.CR`, `cs.SD`, `cs.RO`, `cs.AR`, `cs.DC`, `cs.PF`, `stat.ML`, `stat.ME`, `math.OC`, `quant-ph`, `eess.SP`, `eess.AS`, `q-bio.NC`, `physics.soc-ph`, `nlin.AO`), yielding **6,144 unique IDs**. Listing pages carry title/authors/subjects only, so abstracts were pulled from each candidate's `arxiv.org/abs/{id}` page. The newest fully-populated announcement block is **Thu, 2026-10-15** (881 unique cross-listed IDs; 798 new-to-wiki); **no 2026-10-16 / Friday block had been posted at run time**. This digest therefore mines the 10-15 block plus late-arriving 10-13/10-14 submissions.

Dedup: a repo-wide regex extract of every `\d{4}\.\d{4,5}` across `wiki/**` and `raw/**` yields a **9,222-ID baseline**. Of the harvested candidates, 89 survived abstract retrieval and are new to the wiki; the **54 featured papers below are all new-to-wiki** (verified by grep against the live wiki immediately before writing). One additional candidate — **CoPE** (`2610.20597`) — was dropped because today's sibling job `arxiv-paper-check` already covered it (collision-managed, 0 featured collisions).

> ℹ️ Affiliation note: the arXiv **Atom metadata** API omits affiliations, so **Institution/company** was recovered from each paper's own **arXiv full-text HTML author block** (`arxiv.org/html/{id}`). Where the paper states no affiliation, the entry is marked `not stated (arXiv HTML omits affiliations)`. Recovered affiliations reflect what the author block literally lists (not disambiguated corporate entities).

> ℹ️ Lane note: the classical **industrial CTR / ad-serving architecture** lane is **empty** this block — the only advertising-adjacent material is the search-adjacent **brand-mention forecast** (`2610.19608`, IR lane) and the sponsored/behavioral framing in **Rent-Seeking Language Models** (`2610.19832`, reasoning lane). The broader recommendation/advertising/CTR/user-modeling lane yields **4 papers** (§4). **On-policy distillation (OPD)** and **RLVR credit assignment** are again the most crowded lane (§2, 13 papers), and a **speculative-decoding / KV-reuse** cluster dominates efficiency (§3).

## Core AI / LLM / Agents

### 1. CoPE — Co-Evolving Acting and Forecasting for Language Agents
- **Authors**: Haofei Yu, Yixing Chen, Yining Zhao, Xuyan Ye, Yuxiang Liu, Zhigang Hua, Yan Xie, Shuang Yang, Jiaxuan You
- **Institution**: University of Illinois Urbana-Champaign; University of California San Diego; Meta AI
- **Subjects**: cs.AI; cs.LG
- **Abstract**: Agentic RL learns only from a terminal scalar reward, leaving intermediate-step supervision unused; prior value/observation targets are either derived from that same scalar or reach only one step ahead. **CoPE** adds a third kind of target — **multi-step action targets** — training the shared policy backbone to regenerate the action sequence following each history and to forecast each action from preceding histories.
- **Key innovations**: The temporal ensemble of forecasts is absorbed into one backbone, so acting and forecasting **co-evolve** with no inference overhead. Across ALFWorld, ScienceWorld, WebShop, τ²-bench and AppWorld, CoPE beats GRPO and predictive-auxiliary RL baselines, delivering up to **1.9× / 2.0×** higher sample efficiency than ECHO / GRPO on ScienceWorld — with a single backbone, no extra models or pretraining.
- **arXiv**: https://arxiv.org/abs/2610.20597

### 2. CIPR — One Task, Many Interfaces: Cross-Interface Consistency Training for LLM Agents
- **Authors**: Artin Tajdini, Manpreet Kaur, Peng Qi
- **Institution**: University of Washington; Uniphore
- **Subjects**: cs.LG; cs.AI; cs.CL
- **Abstract**: Post-training binds an agent's competence to the **interface** it trained on: semantics-preserving perturbations (renaming an action, changing notation) degrade performance, and per-sample scoring merely broadens dependence to the training interface distribution. **CIPR** is a self-supervised objective that replaces action names with uninformative identifiers and presents each sample under **two equivalent interfaces**, penalizing the KL divergence between the induced action distributions.
- **Key innovations**: Works in both SFT and RL post-training. On agentic function calling, held-out interface perturbations cost a post-trained agent ~**25%** accuracy, and CIPR recovers **10.5%** while leaving unchanged-interface accuracy intact.
- **arXiv**: https://arxiv.org/abs/2610.20576

### 3. Interlock — From Local Correctness to Task Completion in Long-Horizon Agents
- **Authors**: Linji Hao, Yanji He, Zihan Wang, Hansi Yang, Jiayuan Zhang, Hongyan Hao, Qi Gu, Yan Feng, Han Wu
- **Institution**: Peking University; The Hong Kong University of Science and Technology (Guangzhou); Tsinghua University; Meituan
- **Subjects**: cs.CL; cs.AI
- **Abstract**: Long-horizon agents satisfy individual requirements yet fail to maintain the **relationships** among evidence, decisions, and required effects, producing locally correct but incomplete outcomes. **Interlock** represents each task as a **typed completion graph** — grounding edges (public evidence → decisions), coupling hyperedges (joint constraints), and realization edges (decisions → all downstream effects) — compiled into a resettable workspace, public request, and evaluation rubric.
- **Key innovations**: Source-coverage and public-input reviews preserve original requirements; an agent-as-judge keeps only trajectories meeting mandatory requirements. Fine-tuning two Qwen3.6 backbones on accepted trajectories raises AutomationBench pass rates by **4.00–4.50 pts**, JobBench weighted scores by **3.20–6.64 pts**, and Harvey LAB pass rates by **3.89–4.16 pts**.
- **arXiv**: https://arxiv.org/abs/2610.19686

### 4. Precog-RM — Divergent Paths: Outcome-Predictive Representation of LLM Agent Trajectories
- **Authors**: Alexander Gill, Guram Gogia, Francisco Guzmán
- **Institution**: Handshake AI; University of Utah
- **Subjects**: cs.LG; cs.AI; cs.CL
- **Abstract**: Reframes agentic trajectories as paths through a shared embedding space of actions and observations, showing successful and failed rollouts of the same task separate cleanly in that space. **Precog-RM** is a transformer that meta-learns a representation for few-shot outcome prediction.
- **Key innovations**: Per-task discriminators reach up to **0.95 AUROC** across three benchmarks and three policy models; Precog-RM generalizes to unseen tasks/models and predicts success **long before termination**. Deployed as an early-stopping controller for GRPO on τ²-Bench, it cuts training FLOPs by up to **47.3%** at comparable performance.
- **arXiv**: https://arxiv.org/abs/2610.19614

### 5. WebKD — Teaching Agents in their Own Style: Blackbox Teacher Distillation for Web Agents
- **Authors**: Md Farhan Ishmam, Kenneth Marino
- **Institution**: Kahlert School of Computing, University of Utah
- **Subjects**: cs.AI
- **Abstract**: Closed frontier web agents are costly; distilling them into open models is blocked because token-level distillation needs logits. Offline imitation instead trains students on states they never visit, in a style they don't write. **WebKD** makes the teacher the **editor of the student's failures**: given a failed episode the teacher locates the first mistake and minimally rewrites reasoning, harness states, and actions from there onward.
- **Key innovations**: Data-space edits are written in the **student's style**; an objective-space role-asymmetric KL anchor lets the corrected action move freely while keeping reasoning near the student's prior. On TimeWarp it gains **5.5–10.7 pp** over behavior cloning, outcome-reward RL, and teacher-editing baselines, transferring to unseen versions and the live web (OnlineMind2Web).
- **arXiv**: https://arxiv.org/abs/2610.19834

### 6. ProD — Progress-Aware Distillation for Mitigating Stagnation in SLM Agents
- **Authors**: Yuanpu Cao, Saket Sathe, Hanyu Wang, Ziyi Yin, Fenglong Ma, Jinghui Chen
- **Institution**: The Pennsylvania State University; Microsoft CoreAI
- **Subjects**: cs.LG
- **Abstract**: Distilling agentic capability into small language models (SLMs) causes **progress stagnation** as trajectories grow long — students get trapped in unproductive loops of failed strategies. **ProD** explicitly detects and penalizes stagnation, encoding the student–teacher stagnation gap into an **adaptive margin** for dynamic penalization.
- **Key innovations**: Systematic analysis shows the phenomenon across diverse SLMs and domains; ProD substantially mitigates stagnation and improves success rates and completion efficiency across **8 SLMs (0.6B–8B)** on in- and out-of-domain benchmarks. (NeurIPS 2026.)
- **arXiv**: https://arxiv.org/abs/2610.19439

### 7. DeLoop — Repeated Actions as Self-Supervision for Long-Horizon Agents
- **Authors**: Tianle Chen, Pushkar Singh, Ketan Todi, Biswajit Paria, Qijia He, Wenqi Wang, Yuwen Tan, Jike Zhong, Sugato Basu, Deepti Ghadiyaram, Arjun Akula
- **Institution**: Google; Boston University; University of Washington; University of Southern California
- **Subjects**: cs.AI
- **Abstract**: Long-task agents **loop**, re-issuing an earlier tool call and getting the identical observation with no new information — a failure that becomes far more common once history is compressed to fit the context window. **DeLoop** is a self-supervised method that uses a looping action as a **negative** example and the first later non-looping action as a **positive**, trained via DPO.
- **Key innovations**: Requires no task rewards, gold answers, or LLM judges. On CodeGym under compression it cuts the share of Qwen3-8B tasks containing loops from **57.3% to 6.1%** at ~⅓ the steps and similar success; on Qwen3-32B it raises task success from **37.7% to 44.8%**.
- **arXiv**: https://arxiv.org/abs/2610.19376

### 8. CTXGAP — What Coding Agents Leave Unsaid: Task-State Gaps Between Execution and Reports
- **Authors**: Guoyang Xu, Rui Zhang, Xiuyu Wu, Hao Chen
- **Institution**: Tencent
- **Subjects**: cs.AI
- **Abstract**: Supervisors rely on coding-agent **reports**, but failed attempts, workarounds, and unresolved risks can vanish from routine reporting. **CTXGAP** quantifies the **task-state recoverability gap** between agents' user-facing reports and their full recorded execution contexts.
- **Key innovations**: Across 37 coding tasks and 4,799 probes, full-context readers recover **92.7%** of task-state questions while report-only readers recover **52.0%** — a **40.7-pt** gap that persists at 34.8 pts at verified fixes. Full terminal scrollback only reaches 73.6%; context-informed rewrites improve recovery ~8 pts. Establishes report-based recoverability as a complementary evaluation dimension.
- **arXiv**: https://arxiv.org/abs/2610.20003

## Reasoning / RL / Post-Training / Test-Time

### 9. CriticOPD — Recovering Reliable Supervision via Critique-Guided On-Policy Distillation
- **Authors**: Kaixiang Zhao, Tianrun Yu, Shangzhe Li, Yuxiao Yang, Amanda Hughes, Weitong Zhang, Taylor W. Killian
- **Institution**: Brigham Young University; University of North Carolina at Chapel Hill
- **Subjects**: cs.LG; cs.AI
- **Abstract**: On-policy distillation (OPD) assumes the teacher can reach a correct answer from any student prefix — a property the authors call **recoverability** — and show it fails on incorrect rollouts, where the teacher follows student errors despite recognizing them. **CriticOPD** uses that error recognition to restore recoverability: the teacher critiques the incorrect rollout, the student rewrites, and the revision (including critique as privileged info) is scored.
- **Key innovations**: On two Qwen3 students and six math-reasoning benchmarks, CriticOPD improves OPD with the largest gains on competition problems. Code released. (21 pages.)
- **arXiv**: https://arxiv.org/abs/2610.20572

### 10. VASPO — Self-Distillation with Privileged Value Estimation
- **Authors**: Fei Wu, Zhenrong Zhang, Jianshu Zhang, Jun Du
- **Institution**: University of Science and Technology of China; IFLYTEK Research
- **Subjects**: cs.CL; cs.AI; cs.LG
- **Abstract**: On-policy self-distillation gives dense token supervision but reflects **local** token preferences, not expected return. VASPO identifies complementary **positional dynamics** — privileged info sharpens the critic's value prediction toward the response end, while self-teacher guidance is strong early, drops mid-generation, and rebounds — and integrates both within **PPO**.
- **Key innovations**: A critic computes token-level PPO advantages from continuation returns while the self-teacher modulates selected positive advantages via bounded probability ratios. Across six math benchmarks VASPO beats PPO by **2.59 / 1.81 pts** on Qwen3-4B / OLMo3-7B, and leads on Knights and Knaves.
- **arXiv**: https://arxiv.org/abs/2610.20516

### 11. HP-RLVR — Hindsight-Privileged RLVR: Single-Rollout Token Credit Without Group Sampling
- **Authors**: Wei Chen, Yubing Wu, Zhou Xu, Haoyue Zhang, Delu Zeng, Jiahao Wang, Junmei Yang, Pan Tiewen, Jingfeng Liu, Zhiheng Zhou, Bo Li, Min Chen
- **Institution**: South China University of Technology; Tsinghua University; The Hong Kong University of Science and Technology; Huawei 2012 Laboratories; Shenzhen Technology University (author-block parse, unconfirmed)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Group-relative RLVR (e.g. GRPO) loses its signal when all attempts share an outcome. **HP-RLVR** is a **single-rollout** method that turns a trajectory's own future into token-level weights: the policy scores each token under its causal history and a **hindsight context** containing the realized future plus verifier feedback, and a normalized Jensen–Shannon divergence between the two views weights the reward.
- **Key innovations**: Bounded token credit for both successes and failures, with no reference solution or learned critic. In paired Qwen3-8B runs it trains **1.21× / 1.46× / 2.30×** faster than GRPO on math/code/ALFWorld using **1/8 the rollouts per prompt**, with similar accuracy overall.
- **arXiv**: https://arxiv.org/abs/2610.20497

### 12. When Does Momentum Help in RLVR?
- **Authors**: Kaifei Wang, Zikang Shan, Liwei Wang, Yinyu Ye, Han Zhong
- **Institution**: Peking University
- **Subjects**: cs.LG; cs.AI; math.OC; stat.ML
- **Abstract**: Recent work questions the usefulness of first-moment momentum in RLVR. Through a **bandit formulation** with bias-corrected EMA momentum (coefficient β), the paper proves that increasing β within a non-overshooting range strictly accelerates optimization when gradients are exact, and characterizes when sampling fluctuations obscure the gain.
- **Key innovations**: Shows the safe regime is governed by η/(1−β): with decreasing learning rate, raising β to keep this ratio constant preserves a nonvanishing gain that dominates fluctuations. RLVR experiments on Qwen3-4B-Base and Qwen2.5-32B (AdamW) support larger β₁ — nearly **+2 pts** mean validation accuracy at 32B.
- **arXiv**: https://arxiv.org/abs/2610.20413

### 13. RM-OPD — On-Policy Distillation for Generative Reward Models
- **Authors**: Qinglin Su, Licheng Pan, Zhen Fang, Jiakang Wang, Qingnan Ren, Yunsheng Lu, Yan Gao, Zhixuan Chu
- **Institution**: Zhejiang University; University of Science and Technology of China; Xiaohongshu Inc.
- **Subjects**: cs.LG; cs.CL
- **Abstract**: RL on mixed-domain preference data (Mix-RL) for generalist Generative Reward Models suffers from reward sparsity and cross-domain interference, causing imbalanced capability acquisition and reward hacking. **RM-OPD** separates specialist acquisition from integration: train per-domain teacher GRMs via single-domain GRPO, then consolidate them into one student.
- **Key innovations**: Combines **routed on-policy distillation** (dense signed token supervision on student critiques), **domain contribution reweighting**, and optional **criteria context distillation**. Consistently beats vanilla Mix-RL and strong baselines across RM benchmarks and two base models, with an emergent **teacher-surpassing** effect.
- **arXiv**: https://arxiv.org/abs/2610.20174

### 14. DrOPD — Divergence-Routed On-Policy Distillation
- **Authors**: Tiantian Peng, Guannan Lv, Hongyang Li, Qiuhe Hong, Hang Cheng, Hongjian Dou, Xiangyu Wu, Yuyang Liu
- **Institution**: Peking University; Kuaishou Technology; Tsinghua University
- **Subjects**: cs.AI
- **Abstract**: Standard OPD minimizes reverse KL (RKL), which gives weak corrective signals for teacher-supported tokens the student assigns low probability. Via cross-sampling, the authors find **divergence-based routing** pinpoints performance-gap positions better than entropy-based routing, and that high-JS positions show **teacher-mode under-coverage**.
- **Key innovations**: **DrOPD** keeps RKL everywhere and adds selective **forward-KL (FKL)** supervision at high-JS positions. Across six math benchmarks it improves on standard OPD and entropy routing, reducing severe under-coverage cases by **37.9%**.
- **arXiv**: https://arxiv.org/abs/2610.19572

### 15. Advantage Guidance
- **Authors**: Zhiyuan Zhou, Sergey Levine
- **Institution**: UC Berkeley
- **Subjects**: cs.LG
- **Abstract**: RL can outperform demonstrated behavior but is unstable; supervised learning is stable but bounded by demonstration quality. The paper asks whether policy optimization can be as stable as supervised learning yet as performant as RL. **Advantage Guidance** retains a simple supervised structure with advantage conditioning, improved by effective conditional training and **contrastive diffusion guidance** during sampling.
- **Key innovations**: The contrastive guidance uses the learned advantage-conditioned policy to target the KL-regularized optimal policy. Significantly outperforms prior SOTA RL methods on **26 long-horizon, sparse-reward tasks** across datasets of varying optimality.
- **arXiv**: https://arxiv.org/abs/2610.19783

### 16. CRDS — Beyond Correctness: Compute-Responsive Data Selection
- **Authors**: Liang He, Xiangyu Li, Yuxin Wang, Hanbin Zhang, Mingyu Cao, Zhaomiao Guo, Xilu Wang
- **Institution**: University of Texas at Austin; Advanced Micro Devices (AMD); University of Warwick; University of Surrey
- **Subjects**: cs.AI
- **Abstract**: Reasoning problems differ in their **response to additional test-time compute**. **Compute-Responsive Data Selection (CRDS)** is a post-training data-selection principle that prioritizes **compute-responsive (CR)** examples — those that flip from failure to success under more reasoning.
- **Key innovations**: On Qwen3-8B, SFT on CR examples recovers **45.3%** of held-out low-compute failures vs **40.6%** on already-solved examples, reaching **51.8%** overall on an independent test distribution. Shifts the compute–accuracy frontier across 512–4,096-token budgets, replicates across data sources, works under OPD, and transfers to Llama-3.1-8B-Instruct.
- **arXiv**: https://arxiv.org/abs/2610.20057

### 17. Rent-Seeking Language Models
- **Authors**: Zixiao Wang, Xingbo Du, Duzhen Zhang, Le Song
- **Institution**: Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)
- **Subjects**: cs.LG
- **Abstract**: Recasts reward-model overoptimization (reward hacking) as **rent-seeking**: the policy earns reward from a proxy regulator that true quality does not back. This yields measurable quantities — **rent, a capture index, deadweight loss** — and testable predictions from regulatory economics.
- **Key innovations**: In a version-controlled testbed with three model families and two gold reward models, RL turns **41%–66%** of proxy gain into rent. Policies fabricate details about nonexistent entities (**97%–100%** of probes) or deflect factual questions (**67%–98%**). Finds **frequent mild audits beat rare severe ones**, random audits are as efficient as targeted, and RL policies learn to bunch just below an audit threshold.
- **arXiv**: https://arxiv.org/abs/2610.19832

### 18. Tail Competition Explains Scaling in Best-of-N Sampling
- **Authors**: Taro Yano, Yoichi Ishibashi, Masafumi Oyamada
- **Institution**: NEC Corporation
- **Subjects**: cs.CL; cs.AI; cs.LG
- **Abstract**: Studies Best-of-N as a competition between the **extreme reward tails** of correct and incorrect responses. Using extreme value theory it characterizes three asymptotic regimes (correct-tail-dominant, incorrect-tail-dominant, critical) explaining both monotone gains and reward-hacking degradation.
- **Key innovations**: Derives finite-sample scaling laws showing incorrect responses with large variance can dominate selection despite lower mean reward, and that convergence with an incomplete selector can be **polynomial rather than exponential**. Proposes a lightweight **tail-tension** criterion to estimate when extra sampling becomes harmful. (NeurIPS 2026.)
- **arXiv**: https://arxiv.org/abs/2610.19362

### 19. REWIND — Uncertainty-Guided Trajectory Repair for Test-Time Reasoning
- **Authors**: Yi Ding, Mengyu Wang, Min Zhou, Menglin Yang
- **Institution**: The Hong Kong University of Science and Technology (Guangzhou); University of Edinburgh
- **Subjects**: cs.CL; cs.AI
- **Abstract**: An early mistake can constrain all later reasoning, and repeated-generation methods pick regeneration points almost randomly. The authors find incorrect responses have ~**112%** higher mean token entropy than correct ones on MATH500 with Qwen2.5-Math-7B, and introduce **REWIND**, a training-free controller that uses **entropy dynamics** to propose targeted suffix regenerations.
- **Key innovations**: Across three model families and five benchmarks REWIND beats all baselines by **0.51–10.00 pts**, showing targeted uncertainty-guided repair generalizes across models and tasks.
- **arXiv**: https://arxiv.org/abs/2610.19561

### 20. AtomSearch — Evidence-Grounded Tree Search for Agent Skill Optimization
- **Authors**: Jia Tong, Senyou Deng, Min Peng, Jianfeng Pan
- **Institution**: 360 Security Technology Inc.
- **Subjects**: cs.CL; cs.AI; cs.LG
- **Abstract**: Agent skills edit frozen models via external instructions; revising many rules at once is opaque, and judging edits only by immediate score discards useful intermediates. **AtomSearch** keeps revisions **local** while using subsequent skill states to guide search: contrastive atomic editing links each rule edit to failed/successful executions, a behavioral hypothesis, and an intended scope; **Skill-State Tree Search** retains short edit compositions as revisit-able states.
- **Key innovations**: With deepseek-v4-flash it beats SkillOpt on 3 of 4 tasks (e.g. **+9.68 pp** on LiveMathematicianBench) while producing far more compact skills (SkillOpt's are 2.3–19.7× longer). In **67%** of searches the best state passes through a non-best-at-its-depth ancestor.
- **arXiv**: https://arxiv.org/abs/2610.19951

### 21. Reliability–Uncertainty Self-Distillation for Reasoning
- **Authors**: Jinhao Pan, Bowen Wei, Yuqing Zhou, Ziwei Zhu
- **Institution**: George Mason University
- **Subjects**: cs.AI
- **Abstract**: Reference solutions and rubrics aren't always available to guide self-distillation. Using the model's own attempts as teacher material, the paper weights each attempt's distillation loss by combining **judged reliability** (self-judge score + confidence) with **student predictive uncertainty**, with the same model serving as teacher and student.
- **Key innovations**: Across **eleven** reasoning benchmarks it leads five baselines in average accuracy, reaching **70.47%** (Qwen3-4B) and **76.69%** (Qwen3-8B) — **+8.90 / +2.10 pts** over the base models.
- **arXiv**: https://arxiv.org/abs/2610.19176

## Efficiency / Inference / Serving / Generation

### 22. JetSpec++ — Foresight Parallel Drafting with Self Refinements
- **Authors**: Zhaoxiang Feng, Lanxiang Hu, Haoran Yuan, Yu-Yang Qian, Jihui Yang, Peng Zhao, Yibo Zhu, Tajana Rosing, Hao Zhang
- **Institution**: UC San Diego; UIUC; Nanjing University; Meta; StepFun
- **Subjects**: cs.CL
- **Abstract**: Speculative decoding is governed by draft-token acceptance rate and drafting cost. **JetSpec++** co-optimizes both via algorithm–system co-design: **intra-block self-refinement** (the draft model iteratively corrects its own parallel predictions), **inter-block foresight drafting** (start the next block before the current is verified), and **pipelined drafting/verification**.
- **Key innovations**: Up to **7.45×** wall-clock speedup over autoregressive decoding and **1.54×** over DSpark, reaching **1,361 tok/s** single-request on GB200 with average acceptance length **8.94** across seven benchmarks, while preserving the target distribution. Code/models released.
- **arXiv**: https://arxiv.org/abs/2610.19792

### 23. TreeSpark — Learning to Draft the Trees You Verify
- **Authors**: Jihao Zhao, Qianyu Jiang, Shuaishuai Zu, Pengfei Li, Guanghuan Fang, Ben Feng, Biao Qin, Zhibin Wang, Baochuan Yang
- **Institution**: Renmin University of China; Nanjing University; Huawei Technologies Ltd.
- **Subjects**: cs.CL
- **Abstract**: Parallel drafters (DFlash/DSpark) reduce proposal latency but early mismatches cap acceptance; retaining alternatives introduces parent states and candidate choices that reference-conditioned training doesn't supervise. **TreeSpark** extends semi-autoregressive DSpark with **parent-conditioned candidate trees** constructed in one backbone pass and replayed during training.
- **Key innovations**: Survival NLL weights retained edges by reference-derived path mass, plus a capped coverage hinge for target-important alternatives; both reuse reference-chain targets with no extra target forward passes. Improves mean acceptance length over DSpark by **23.4–31.6%** and single-request throughput by **15.1–25.0%** (Qwen3-4B/8B, 15 suites).
- **arXiv**: https://arxiv.org/abs/2610.20175

### 24. CacheSmith — Accurate RAG Serving under Latency SLOs with Adaptive KV Reuse
- **Authors**: Xinyue Ma, Damin Lee, Aashaka Shah, Myeongjae Jeon
- **Institution**: POSTECH; Microsoft Research
- **Subjects**: cs.AR; cs.DC
- **Abstract**: Context caching lowers RAG prefill latency but misses cross-chunk attention that full prefill computes; prior selective-recompute schemes use static configs that fail under request heterogeneity and dynamic latency budgets. **CacheSmith** decomposes selective recomputation into a dynamically configurable **WarmUp → Probe → Patch** workflow.
- **Key innovations**: An SLO-aware scheduler plus budget-aware planner make fast, **solver-free** decisions over profiled cost-accuracy bands. On four benchmarks across arrival rates and burstiness it improves quality-gated SLO attainment by up to **27.5%** over four SOTA baselines.
- **arXiv**: https://arxiv.org/abs/2610.18925

### 25. One Block Ahead (OBA) — Promoting Sampler State in Diffusion LMs
- **Authors**: Yangyi Shen, Pin-Jui Ku, Nicolai Oswald, Jean-Marie Lemercier, Yonggan Fu, Stefano Ermon, Jure Leskovec, Boris Ginsburg, Ante Jukić
- **Institution**: Stanford University; NVIDIA
- **Subjects**: cs.CL
- **Abstract**: Block-diffusion LMs denoise a block in parallel but blocks are still denoised **strictly sequentially**. **OBA** is a training-free decoder that denoises the next block alongside the current one, promoting the next block's tokens **together with the sampler state** (self-conditioning signal and denoising time), with a break-even criterion relating benefit to paired-block forward cost.
- **Key innovations**: On DiffusionGemma it raises tokens-per-forward-pass by **42.3%** (15.64 → 22.25) and single-request denoising throughput by **16.3%** averaged over ten benchmarks, with a small accuracy regression.
- **arXiv**: https://arxiv.org/abs/2610.19510

### 26. SQUELCH — How Many Ranks Does a Token Need?
- **Authors**: Mei Okonkwo, Owen Castellanos, Ingrid Solberg, Yusuf Demirel
- **Institution**: University of Edinburgh; Delft University of Technology
- **Subjects**: cs.LG
- **Abstract**: Argues the number of rank-one LoRA components a token needs is a **detection** problem: a token's responses to trained rank-one components sit on a Gaussian noise floor (matching an untrained adapter) that carries cross-talk. **SQUELCH** soft-thresholds each token's responses at a multiple of its own robust noise level, chooses that multiple per module by **Stein's unbiased risk estimate**, and adds one explaining-away step on the value Gram matrix.
- **Key innovations**: Router-free, adds **no trainable parameters** to LoRA; proves near-oracle allocation, risk-consistent thresholding, and controlled explaining-away error. Improves over LoRA by **2.2–3.2 pts** and over the strongest MoE baseline by **0.8–1.2 pts** while activating **8.6 of 32** components per token on average (LLaMA-3.1-8B, Qwen3, DeBERTaV3).
- **arXiv**: https://arxiv.org/abs/2610.19033

### 27. Memory-Efficient Subspace Optimization with Residual Correction (SMRC / PMRC)
- **Authors**: Sifan Yang, Hongyi Tao, Dingzhi Yu, Haomin Bai, Wei Jiang, Silin Gao, Pi Bu, Lijun Zhang
- **Institution**: Nanjing University; Alibaba Group (Alibaba Token Hub); Nanjing University of Science and Technology
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Subspace optimizers usually keep the leading singular subspace of stochastic gradients, but gradient noise dominates later and can block convergence. A **residual correction** framework keeps optimizer states in-subspace and adds the orthogonal residual to the parameter update.
- **Key innovations**: **SMRC** (momentum SGD) attains **O(T⁻¹ᐟ⁴)** with a fixed basis (matching full-space momentum SGD), with a multi-stage variant that refreshes bases; **PMRC** brings the framework to **Muon** with the same rate. Introduces a subspace virtual iterate and boundary correction across stages.
- **arXiv**: https://arxiv.org/abs/2610.19844

### 28. CAST — History-Adaptive Spectral Clipping for LLM Pretraining
- **Authors**: Jiacheng Li, Jianchao Tan, Kefeng Zhang, Yuchen Xie, Xunliang Cai
- **Institution**: Meituan
- **Subjects**: cs.LG
- **Abstract**: Soft spectral clipping (SSC) depends on gradient scale and clipping threshold. **CAST** makes SSC **history-adaptive**: AdamW's previous second moment sets row/column scales, and an EMA of the clipped output's estimated spectral norm sets each matrix's threshold, restoring original coordinates before the AdamW update.
- **Key innovations**: Trains a 19.08B-parameter MoE for 83.89B tokens, achieving lower training and mean validation losses than **nine** gradient-processing baselines with the fewest relative gradient spikes, reaching the best baseline's final smoothed training loss in **7.2% fewer steps**.
- **arXiv**: https://arxiv.org/abs/2610.19761

## Recommendation / Advertising / CTR / User Modeling

### 29. HEM-Med — Hierarchical Agentic Memory for Safe Multi-Center Medication Recommendation
- **Authors**: Min Xiao, Jin Li, Shoujin Wang, Yeguang Zhen, Yishuo Li, Wenpeng Lu
- **Institution**: Qilu University of Technology (Shandong Academy of Sciences); University of Technology Sydney
- **Subjects**: cs.AI; cs.IR
- **Abstract**: Multi-center medication recommendation (MR) must disentangle transferable cross-hospital experience from hospital-specific prescribing, and respect safety constraints (drug-drug interactions, local formulary). **HEM-Med** is a hierarchical agentic memory framework with a **disentangled hierarchical memory** (cross-hospital experience vs hospital-specific residual) and a **safety-aware medication set generation** module.
- **Key innovations**: Dual-level experience retrieval plus safety-aware set decoding produces clinically relevant, safer, locally adaptive recommendations. On a real-world multi-center **eICU** dataset it beats transfer-learning, LLM-based, and MR baselines on accuracy and safety. (BIBM 2026.)
- **arXiv**: https://arxiv.org/abs/2610.20191

### 30. On the Limits of Skill-Augmented Career Path Prediction
- **Authors**: Ege Süalp, Elena Senger, Toine Bogers, Barbara Plank
- **Institution**: Fraunhofer Institute for Systems and Innovation Research ISI; IT University of Copenhagen
- **Subjects**: cs.CL
- **Abstract**: Tests whether explicit **skill** representations add signal beyond text-based job representations for career path prediction (CPP), comparing score fusion and neural architectures under predicted skills and ground-truth ESCO annotations.
- **Key innovations**: A careful **negative result**: across two benchmarks, neither setting yields substantial gains over strong text-only baselines, even with ground-truth skills. Attributes this to high text/skill redundancy, weak discriminative power of ESCO, representational collapse, and skill-difficulty correlation — challenging the assumption that explicit skill modeling helps CPP. (RecSys in HR.)
- **arXiv**: https://arxiv.org/abs/2610.20186

### 31. SemICD — Beyond ICD Codes: Semantic IDs for Generative Medical Coding
- **Authors**: Yihang Cheng, Qian Zhang, Yonghui (Andie) Huang, Baoshuo Kan, Junyi Shen
- **Institution**: University of Otago; Massey University; South China Normal University
- **Subjects**: cs.AI
- **Abstract**: Generative ICD coding predicts raw code strings, but the ICD hierarchy doesn't always reflect clinical relationships and LLMs struggle with the strings. **SemICD** trains LLMs to generate **Semantic IDs (SIDs)** built by hierarchically clustering embeddings of textual code profiles, so related codes share prefixes while each SID uniquely identifies one code.
- **Key innovations**: Two auxiliary bidirectional generation tasks (profile ↔ SID) align SID tokens with clinical semantics. On MIMIC-III/IV with four LLMs, SemICD improves Micro-F1 by **1.34–8.00 pts** over direct code generation. Code released.
- **arXiv**: https://arxiv.org/abs/2610.19301

### 32. PROMETHEUS — Multi-Treatment Causal Ranking for Population Health Stratification
- **Authors**: Rocco Zaccagnino, Martina Girolamo, Alberto Lombardi, Delfina Malandrino, Donatello Telesca, Alessia Ture
- **Institution**: University of Salerno; Local Health Authority of Benevento; University of California, Los Angeles
- **Subjects**: cs.LG
- **Abstract**: Population-health stratification frameworks (e.g. Italy's DM77) organize patients by clinical need but don't say which care changes to prioritize. **PROMETHEUS** formulates stratification as a **multi-treatment causal ranking** problem, ordering patient-treatment opportunities by expected **incremental benefit** rather than calibrated individual effects.
- **Key innovations**: Combines doubly robust causal signals with a **Siamese neural ranking** model and contrastive pretraining to produce a globally comparable ranking. Synthetic and semi-synthetic experiments (real ASL Benevento covariates) evaluate ranking quality, allocation value, robustness, and failure modes; validation on observed treatment-outcome data is required before clinical use.
- **arXiv**: https://arxiv.org/abs/2610.19782

## IR / Retrieval / Ranking

### 33. Twenty Days Later — Pre-Registered Forecasts of Brand Mentions in Gemini Answers
- **Authors**: Dmitrij Żatuchin
- **Institution**: Rankfor.AI (Wrocław, Poland)
- **Subjects**: cs.IR; cs.CL
- **Abstract**: Because LLM brand-mention counts are only useful if they persist, the paper runs a **pre-registered** replication: the same 162 requests were sent to gemini-3.1-pro-preview in three waves within ~10 hours and again **20.3 days** later, with the plan and decision rule frozen on OSF beforehand.
- **Key innovations**: The primary history-based forecast scored **Brier 0.0281 / log loss 0.126** (vs brand history 0.104, overall rate 0.234), winning all nine question families (exact sign-flip p = 0.0039). A first-wave-only forecast stayed stable across 1.5 h → 20.7 d; of 202 8-hour-unanimous cells, 194 were unchanged and **none reversed**. A blind human check agreed on 96/96 after adjudication.
- **arXiv**: https://arxiv.org/abs/2610.19608

### 34. RCER — Reconstructing Cross-Evidence Relations for Iterative RAG
- **Authors**: Linyao Zheng, Xuhang Shi, Zhifang Mao, Xiuquan Hou, Sai Zhou
- **Institution**: Xi'an Jiaotong University; Beijing University of Posts and Telecommunications
- **Subjects**: cs.IR
- **Abstract**: Iterative RAG struggles to reconstruct entity correspondences and inferential dependencies across passages as information accumulates. **RCER** reconstructs **cross-evidence relations** from accumulated passages: inter-round relational evidence acquisition drives dynamic decomposition and retrieval, while reasoning-context reconstruction jointly selects complementary passages and derives cross-evidence inferences.
- **Key innovations**: Cross-evidence compositional reasoning composes relations across selected passages for answer derivation. Outperforms the best baselines by **+2.83 EM / +3.06 F1** on average across three multi-hop QA benchmarks and leads on narrative and implicit-reasoning tasks.
- **arXiv**: https://arxiv.org/abs/2610.19398

### 35. FinGREAT — Financial Graph-guided Retrieval And Typing
- **Authors**: Ashman Mehra, Bryan Routledge, Jane JaeYeon Pyo, Pierre Jinghong Liang
- **Institution**: Carnegie Mellon University
- **Subjects**: cs.LG
- **Abstract**: Financial disclosures encode double-entry accounting relationships in unstructured text, but financial LLM benchmarks emphasize QA/classification over **schema-guided evidence discovery**. Using an accounting graph of **11 accounts / 11 transaction types**, the paper studies whether open-weight LLMs can extract and classify evidence matching these relationships.
- **Key innovations**: Evaluates mid-sized models from **5 open-weight families** on **1,300 SEC 10-K Item 7 filings** over 26 years vs three proprietary models, and introduces a human-annotated relation-classification benchmark (**483 passages**; 34 open-weight + 10 proprietary models). Best open-weight / proprietary accuracy: **84.1% / 92.8%**. Argues evidence discovery and relation understanding should be evaluated separately.
- **arXiv**: https://arxiv.org/abs/2610.19240

## Sequential / Time Series / Trajectory

### 36. TimeRSI — Self-Improved Agentic Deployment for Time-Series Foundation Models
- **Authors**: Haoxin Liu, Deqing Fu, Lucheng Fu, Yiqiao Jin, Rushi Qiang, Harshavardhan Kamarthi, B. Aditya Prakash
- **Institution**: Georgia Institute of Technology; University of Southern California; Samay AI
- **Subjects**: cs.LG
- **Abstract**: Time-series foundation models give strong zero-shot forecasts, but real deployment needs task-specific input/output designs. **TimeRSI** is a self-improving **agentic deployment** system around frozen forecasting models: a coding agent translates task descriptions into executable pipeline changes, tests each revision on historical windows, and uses observed errors to guide subsequent revisions.
- **Key innovations**: An **adaptive selector** picks among pipelines using completed forecasts under similar conditions. Across **198 tasks** on TIME and fev-bench it outperforms all submissions on six point and probabilistic metrics; controlled comparisons attribute gains to **feedback-guided revision** over non-iterative search, and it generalizes across coding agents and forecasting models. Code released.
- **arXiv**: https://arxiv.org/abs/2610.19725

### 37. CTIA-ODE — Continuous-Time Inter-Variable Attention for LTSF
- **Authors**: Chengyi Pan, Huangqimei Zheng, Hao Xue
- **Institution**: The Hong Kong University of Science and Technology (Guangzhou); Yunnan University
- **Subjects**: cs.LG
- **Abstract**: Discrete-time architectures impose rigid temporal alignment across heterogeneous variables, limiting capture of continuously evolving exogenous effects. **CTIA-ODE** embeds **Continuous-Time Inter-Variable Attention** in an ODE solver, letting the evolving endogenous trajectory query a static exogenous context along the integration path without explicit alignment.
- **Key innovations**: A **Linear Residual Augmentation** trend anchor and an **Outlier-Robust Hybrid Loss** stabilize continuous latent dynamics. Across eight real-world datasets it reaches state-of-the-art forecasting with a compact memory footprint and low inference latency, especially under long horizons. Code released.
- **arXiv**: https://arxiv.org/abs/2610.19831

### 38. TEX-MEX — Similarity-Guided Temporal Contrastive Learning for Time Series
- **Authors**: Aditya Radhakrishnan, Maxwell A. Xu, Wanting Mao, Santosh Kumar, Harish Haresamudram, James M. Rehg
- **Institution**: University of Illinois Urbana-Champaign; University of Memphis
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Contrastive time-series learning relies on deciding which windows are similar. Prior methods use two disjoint notions — **structural** similarity (morphology) and **temporal** similarity (proximity in time). **TEX-MEX** unifies them into a single relationship, pulling each window toward temporally shifted versions of structurally similar windows and away from those of dissimilar ones.
- **Key innovations**: Broadly state-of-the-art across PPG, EEG, ECG, accelerometry, and continuous glucose monitoring versus contrastive, reconstructive, JEPA-based, and modality-specific methods; a **560K-parameter** PPG foundation model (~50× smaller than the next-best unimodal pretrained PPG model) leads downstream benchmarks. To be released open-weight.
- **arXiv**: https://arxiv.org/abs/2610.19557

### 39. BTA — Bayesian Time-aware Attention for Non-Stationary LTSF
- **Authors**: Xinjie Lan, Yunbo Mei, Leheng Zhou, Hao Qi
- **Institution**: Rice University; The University of Hong Kong; University of North Carolina at Charlotte
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Interprets self-attention as a **Bayesian posterior** over attended positions — a content-based prior from scaled dot-product similarity combined with a temporal-evidence likelihood from positional encoding — and derives a population-level **ELBO** characterizing positional encoding's role in weakly stationary forecasting.
- **Key innovations**: Shows static positional encoding is suboptimal under non-stationarity (a fixed temporal bias must cover heterogeneous dynamics), and proposes **Bayesian Time-aware Attention (BTA)**: an MoE router adaptively combines temporal kernels into input-conditioned, head-specific positional biases. Improves multiple LTSF Transformer backbones at modest overhead.
- **arXiv**: https://arxiv.org/abs/2610.19603

### 40. VaryST — Generalizable Spatio-Temporal Forecasting Beyond the Closed World
- **Authors**: Shengnan Guo, Jinjun Cheng, Xiaowei Mao, Jianhao Zhang, Haochen Lv, Yang Jiang, YiHeng Huang, Yan Lin, Youfang Lin, Huaiyu Wan
- **Institution**: Beijing Jiaotong University; Aalborg University
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Spatio-temporal forecasting models are tightly coupled to their training environment via node-specific representations, predefined spatial support, and consistently available observations. **VaryST** constructs predictive context dynamically from available long-term observations: node representations from long-term histories (temporal change), functionally relevant support nodes beyond predefined neighborhoods (spatial change), and selective masking of relied-upon historical patches (varying availability).
- **Key innovations**: On six datasets vs **seventeen** baselines, VaryST achieves strong in-domain accuracy, substantially improves zero-/few-shot generalization under spatial and temporal change, and stays robust to missing observations.
- **arXiv**: https://arxiv.org/abs/2610.19813

### 41. Lotus — Learning to Understand Time-series by Learning to Forecast
- **Authors**: Van Dai Do, Huu Hiep Nguyen, Minh Hoang Nguyen, Manh Nguyen, Hung Le
- **Institution**: Deakin University (Applied AI Initiative)
- **Subjects**: cs.LG; cs.AI; cs.CL
- **Abstract**: Time-series language models usually align numerical signals with language via labels/captions/QA, which doesn't require preserving signal evolution. **Lotus** instantiates **forecast grounding**: language-aligned time-series representations must remain predictive of the future — each channel is split into patches mapped into the LLM embedding space, and the next patch is predicted from the hidden states. A **temporal-spectral patch representation** augments each patch with its spectrum.
- **Key innovations**: Across three LLM backbones and six downstream datasets, Lotus reaches **59.91%** accuracy (+3.36% over the strongest matched baseline) with minimal trainable parameters, outperforming models **25–50× larger** on TSRBench.
- **arXiv**: https://arxiv.org/abs/2610.18877

### 42. MetaModelSelect — Selective Next-Location Prediction
- **Authors**: Calvin Jary, Nafiseh Kahani
- **Institution**: Carleton University
- **Subjects**: cs.LG; cs.NI
- **Abstract**: Acting on unreliable next-location predictions wastes mobile-network resources. **MetaModelSelect** is a lightweight **post-hoc confidence metamodel** that learns whether a frozen RNN's top-1 prediction is correct from its outputs alone (predicted-location embedding + four largest softmax probabilities + Softmax Concentration), without retraining the backbone.
- **Key innovations**: On path-balanced Changchun cellular trajectories, versus eight scalar confidence scores, two location-aware lookups, and a raw-logit MLP, it reduces AURC/E-AURC/AUGRC by **2.6% / 4.2% / 3.0%** (CE) and **2.0% / 3.3% / 1.9%** (SAT+EM), with the lowest mean risk at every evaluated coverage. (ICTAI 2026.)
- **arXiv**: https://arxiv.org/abs/2610.19394

### 43. Neural Wasserstein Splines (NWSP)
- **Authors**: Amartya Banerjee, Harlin Lee, Caroline Moosmüller
- **Institution**: not stated (arXiv HTML omits affiliations)
- **Subjects**: cs.LG; cs.AI; stat.ML
- **Abstract**: Population dynamics observed as unpaired snapshots leave evolution underdetermined, and penalizing sampled-particle accelerations depends on the particle representation. **NWSP** learns a continuous population curve under a **Wasserstein smoothness prior**: a network maps latents to cubic-spline control points, and the generator's velocity is projected onto a finite dictionary of scalar potentials to get a finite-dimensional surrogate for intrinsic Wasserstein acceleration.
- **Key innovations**: For a fixed dictionary the population penalty depends only on the **marginal curve** (representation invariance), with bounds on sensitivity to moment-estimation error; learned potentials sharpen acceleration. Top-two in **11 of 16** settings and beats an unregularized spline in **13 of 16**. Code released.
- **arXiv**: https://arxiv.org/abs/2610.19878

## Games / Multi-Agent / Bandits / Mechanism Design

### 44. PREFER — From Player Experience to Personalized Game Refinement
- **Authors**: Qi Chai, Zhang Zheng, Lu Yang, Zixun Sun, Hao Wang
- **Institution**: not stated (arXiv HTML omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Overall LLM gameplay ratings give little insight into which experience aspects drive judgments or how to change the game. **PREFER** uses a shared set of **experience dimensions** adapted from psychometric questionnaires to benchmark how models evaluate gameplay and to guide **persona-specific** refinement.
- **Key innovations**: Personas simulate distinct player profiles; per persona, PREFER selects refinement objectives from experience-preference relationships, revises rules and implementations, and playtests candidates. With five personas it achieves **9.2%** higher mean post-play preference ratings than the strongest baseline.
- **arXiv**: https://arxiv.org/abs/2610.19213

### 45. SGQN — Selective Growing Q-Networks
- **Authors**: Parham Nooranbakht, Seyed Mahdi Basiri Azad, Joschka Bödecker
- **Institution**: Albert-Ludwigs-Universität Freiburg
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Decoupled Q-learning discretizes continuous actions, and Growing Q-Networks (GQN) grow resolution uniformly. **SGQN** replaces uniform growth with an **adaptive action grid** — bins added next to high-Q bins, low-Q bins pruned, ε-greedy selection — keeping decoupled Q-learning.
- **Key innovations**: A pointed **analysis**: the adaptive grid does **not** explain results (growth activates every candidate bin, pruning changes return ≤1.1%); what matters is a coarse start and ε-greedy selection (annealed softmax lowers return 23–100%). Highest mean final return on 4 of 8 DMControl tasks and within 1.1% on three more, using ~7.5 of 9 bins/dimension. TMLR under review.
- **arXiv**: https://arxiv.org/abs/2610.20463

### 46. PPAD-Completeness of Contiguous Envy-Free Cake Cutting
- **Authors**: Yasushi Kawase, Bodhayan Roy, Mohammad Azharuddin Sanpui
- **Institution**: Chuo University (Tokyo); Indian Institute of Technology Kharagpur
- **Subjects**: cs.GT; cs.AI; cs.MA
- **Abstract**: Proves that computing a complete contiguous **ε-envy-free** cake allocation is **PPAD-complete** even for normalized rational piecewise-constant additive valuations — with ε in unary, every density taking two values shared by all agents with ≤6 breakpoints. Consequently exact contiguous envy-free allocation is also PPAD-complete under the same restrictions.
- **Key innovations**: The key gadget assigns **prices** to pieces so that in every approximately envy-free allocation all prices are nearly equal. Further shows contiguous **EFc** allocation of indivisible goods on a path is PPAD-complete for every fixed c ≥ 1, even for binary valuations — resolving open questions of Goldberg–Hollender–Suksompong (JAIR 2020) and Bilò et al. (ITCS 2019).
- **arXiv**: https://arxiv.org/abs/2610.19690

### 47. Thompson Sampling for Learning in Zero-Sum Games
- **Authors**: Kenshi Abe, Kaito Ariu, Po-An Wang
- **Institution**: CyberAgent; Tohoku University; National Tsing Hua University
- **Subjects**: cs.GT; stat.ML
- **Abstract**: Studies Thompson sampling (TS) in an unknown finite two-player zero-sum matrix game with Gaussian bandit feedback. Under **centralized self-play** TS samples a payoff matrix from the posterior and plays a Nash equilibrium of the sampled game.
- **Key innovations**: For every fixed zero-sum game with a unique Nash equilibrium, expected cumulative duality gap is **O(√T)** (improving to **O(log T)** for pure equilibria); the exact √T coefficient depends only on equilibrium strategies and noise level. Establishes matching minimax and instance-dependent lower bounds; experiments confirm predicted rates.
- **arXiv**: https://arxiv.org/abs/2610.18899

### 48. Learning in Strategic Queuing with Geometric Recharge
- **Authors**: Cristian Palma Foster, Eva Tardos
- **Institution**: Cornell University
- **Subjects**: cs.GT; cs.LG; cs.PF
- **Abstract**: Studies packet routing where selfish, myopic queues use **no-regret** learning over servers with unknown rates and single-packet buffers. A single queue routing to m buffered servers is shown equivalent to **recharging bandits with geometric recharge**.
- **Key innovations**: Proves any no-regret learner achieves long-run throughput ≥ the **Hamacher sum** of server rates (tight), giving a stable-iff condition, and is at least **0.77-competitive** (tight). For multi-queue systems, the smallest overprovisioning factor for stability is **1/(1−λ_max)** — for λ_max = 1/2 improving Abel et al. (EC 2026)'s bound from 3 to **2**, matching their lower bound and resolving their open question.
- **arXiv**: https://arxiv.org/abs/2610.19179

### 49. Neurosymbolic Learning of Interpretable World Models (CGWM)
- **Authors**: Riccardo Andreoni, Massimiliano Ronzani, Chiara Ghidini, Alessandro Daniele, Emile van Krieken
- **Institution**: Fondazione Bruno Kessler; Free University of Bozen-Bolzano
- **Subjects**: cs.AI
- **Abstract**: Most world models are black boxes with limited ability to incorporate prior knowledge. **Concept-Grounded World Models (CGWMs)** learn **interpretable concept representations** using explicit, complete knowledge expressed in **temporal logic** that specifies valid world states and their dynamics, and use that knowledge directly by formulating planning as **differentiable reasoning** (gradient ascent on a goal).
- **Key innovations**: Across two game environments, CGWMs ground concepts far more accurately — even over long horizons — than a purely neural and a neurosymbolic baseline, yielding significantly more robust planning in and out of distribution.
- **arXiv**: https://arxiv.org/abs/2610.19955

### 50. What Happens to the Goal? Distinct Failures of Policy Alignment in Goal Misgeneralization
- **Authors**: Julia Barth, Armin Sommer, Kunvar Thaman, Jannik Schilling
- **Institution**: Pantheon Industries; ETH Zurich
- **Subjects**: cs.LG; cs.AI; cs.RO
- **Abstract**: Agents can behave competently out of distribution while not pursuing the intended goal, but what happens to the goal is unclear. Across three Procgen environments and five robot tasks, the paper distinguishes three forms of policy-goal misalignment: **functional target substitution**, **policy shortcut**, and **cue competition**, tracing where goal information remains available, how strongly it influences the policy, and its role in action selection.
- **Key innovations**: The goal is lost at different depths, and the recovery differs accordingly: steering raises intended-goal reach from **16.0% → 95.3%** where the goal reaches the decision (cue competition); downstream rewiring recovers **31.6% → 84.3%** where it reaches the policy but not the decision; where it is inert, neither works.
- **arXiv**: https://arxiv.org/abs/2610.19731

### 51. The Value of Information — Characterization and Complexity
- **Authors**: Ratip Emin Berker, Ioannis Anagnostides, Emanuel Tewolde, Brian Hu Zhang, Tuomas Sandholm, Vincent Conitzer
- **Institution**: Carnegie Mellon University; Massachusetts Institute of Technology; Foundations of Cooperative AI Lab (FOCAL)
- **Subjects**: cs.GT
- **Abstract**: Examines the **value of information** in extensive-form decision problems — the largest multiplicative gain from an information refinement over all payoff environments — generalizing the value of recall (Berker et al., AAAI'25). Establishes a unifying characterization connecting it to the **maximum fractional chromatic number** over a family of conflict graphs.
- **Key innovations**: For the value of perfect information the conflict graphs are **cographs**, so it reduces to clique number, yet optimizing over the graph family is **NP-complete** (with FPT in the degree of imperfect information). For the value of recall, shows it can realize any graph's fractional chromatic number, hence can take **fractional** values, and proves **S2P-completeness** — strictly harder than perfect information. (WINE-26.)
- **arXiv**: https://arxiv.org/abs/2610.19488

## Benchmarks / Evaluation / Interpretability

### 52. Sparse Transformer — A Controlled Testbed for Mechanistic Interpretability
- **Authors**: Anton Korznikov, Alexey Dontsov, Elena Tutubalina
- **Institution**: not stated (arXiv HTML omits affiliations)
- **Subjects**: cs.AI
- **Abstract**: Mechanistic interpretability lacks ground-truth units to evaluate against. The paper introduces a **Sparse Transformer (ST)**: a 5-layer TinyStories LM whose wide, TopK-sparse MLP forces **neuron specialization**, giving known reference units.
- **Key innovations**: ST neurons outperform a loss-matched dense transformer by **43%** on AutoInterp, and circuits of a **median 12 neurons** reproduce individual predictions. A controlled comparison shows **Transcoder** recovers ST neuron vectors with **52.6% higher** cosine similarity than a Sparse Autoencoder; distilling the sparse MLP into a dense counterpart reveals how compression yields **feature superposition**. Code/models released.
- **arXiv**: https://arxiv.org/abs/2610.19907

### 53. SAE-IDF — Sparse Autoencoders Are a Shared Coordinate System for Symbolic Matching
- **Authors**: Xiaocong Yang, Xuanyu Meng, Yuji Zhang, Jiawei Han, ChengXiang Zhai
- **Institution**: University of Illinois Urbana-Champaign
- **Subjects**: cs.LG; cs.AI; cs.CL; cs.SC
- **Abstract**: Neuro-symbolic models could scale like LLMs but their symbolic backbone is built by hand and is domain-specific. Matching units across heterogeneous symbolic systems is the foundational step. **SAE-IDF** encodes a symbol in its native context into a sparse code with an SAE, **re-weights each dimension by its rarity** (IDF), and matches across systems.
- **Key innovations**: On **12 tasks across 6 kinds of symbolic system**, SAE-IDF beats the same LLM's dense baseline on all tasks (Gemma-2-9B) and all but one (Llama-3.1-8B), by up to **45 pts**, consistently across SAE layers/configurations — and every sparse-code dimension has a human-readable meaning, so matches decompose into named concepts.
- **arXiv**: https://arxiv.org/abs/2610.19636

### 54. Target-Token Asymmetry Can Masquerade As Depth Specialization
- **Authors**: Danlin Li, Miao Li, Xu Han, Jiecheng Lu
- **Institution**: Georgia Institute of Technology; AWS
- **Subjects**: cs.CL; cs.LG
- **Abstract**: Layer-ablation studies compare early/late-layer damage across two corpora and read a larger early-layer effect as task specialization — but this **averages over target tokens** that differ by corpus (math solutions ask for far more whitespace and numbers than prose). The paper shows this difference can *create* the appearance of depth specialization.
- **Key innovations**: Splitting the cross-corpus early–late damage interaction by **target-token type** and rematching the target mixture: for GSM8K vs Wikitext, only **whitespace** has a positive interaction across three decomposed models, and removing whitespace reverses the pooled effect. A **tokenizer-only screen** predicts the risk before any model runs. Argues depth-specialization claims require reporting the target-token mixture, token-type decomposition, and a mixture-matched summary.
- **arXiv**: https://arxiv.org/abs/2610.19344

---

## Coverage & Method Notes

- **Window**: public arXiv **listing pages** (`arxiv.org/list/{cat}/pastweek?skip=0&show=2000`) across 26 primary categories → **6,144 unique IDs**. The export Atom API was **rate-limited (HTTP 429)** all run, so abstracts came from `arxiv.org/abs/{id}` pages. Newest fully-populated announcement block = **2026-10-15** (881 unique cross-listed IDs; 798 new-to-wiki); no 2026-10-16 block was posted at run time.
- **Dedup**: repo-wide `\d{4}\.\d{4,5}` baseline = **9,222 IDs**; 89 candidates survived abstract retrieval and are new-to-wiki; all **54 featured** re-verified grep 0-hit against the live wiki before writing. One further candidate — **CoPE** (`2610.20597`) — was excluded because today's sibling `arxiv-paper-check` already covered it.
- **Sections (54 featured)**: Core AI/LLM/Agents (8), Reasoning/RL/Post-Training/Test-Time (13), Efficiency/Inference/Serving (7), Recommendation/Advertising/CTR/User Modeling (4), IR/Retrieval/Ranking (3), Sequential/Time Series/Trajectory (8), Games/Multi-Agent/Bandits/Mechanism Design (8), Benchmarks/Evaluation/Interpretability (3).
- **Affiliation provenance**: recovered from each paper's arXiv full-text HTML author block (`arxiv.org/html/{id}`); otherwise `not stated`. Notably recovered: **Meta AI** (2610.20597, 2610.19792), **Google** (2610.19376), **Microsoft CoreAI** (2610.19439), **Microsoft Research** (2610.18925), **NVIDIA + Stanford** (2610.19510), **NEC Corporation** (2610.19362), **Kuaishou Technology** (2610.19572), **Xiaohongshu Inc.** (2610.20174), **Tencent** (2610.20003), **Meituan** (2610.19686, 2610.19761), **Huawei** (2610.20175), **Alibaba Group** (2610.19844), **AMD** (2610.20057), **MBZUAI** (2610.19832), **360 Security Technology** (2610.19951), **Uniphore** (2610.20576), **Handshake AI** (2610.19614), **Rankfor.AI** (2610.19608), **CyberAgent** (2610.18899), **Pantheon Industries** (2610.19731), **ETH Zurich** (2610.19731), **Cornell University** (2610.19179).
- **CTR lane**: explicit industrial-CTR-prediction architecture work is **absent** this block. The advertising-adjacent material is limited to the brand-mention **appearance-in-LLM-answers** forecast (`2610.19608`, §5) and the rent-seeking/behavioral framing of reward models (`2610.19832`, §2). Recommendation/user-modeling is represented by medical/clinical ranking and career-path work (§4), plus sponsored-adjacent IR (§5).
- **Caveats**: `2610.20497` (HP-RLVR) and `2610.20186`/`2610.19878`/`2610.19907`/`2610.19213` author-block affiliations were partially ambiguous or absent; those entries carry an explicit `unconfirmed` / `not stated` marker.
