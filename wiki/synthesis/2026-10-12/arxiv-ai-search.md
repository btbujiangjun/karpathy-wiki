---
title: arXiv AI Search (Recent) - 2026-10-12
type: synthesis
created: 2026-10-12
updated: 2026-10-12
sources: []
tags: [arxiv, ai, llm, recommendation, advertising, sequential-modeling, ctr, games, ml, agents, rl, efficiency, retrieval, theory]
---
# arXiv AI Search - Recent Papers (2026-10-12)

Search scope: the export API's latest indexed announcement block has advanced to **2026-10-09 (Fri)** (the 10-11 run swept 2026-10-05 → 2026-10-08; `submittedDate:[20261010 TO 20261013]` still returns 0). This run re-sweeps **2026-10-08 → 2026-10-13** across `cs.AI`, `cs.LG`, `cs.CL`, `cs.IR`, `cs.GT`, `cs.MA`, `cs.NE`, `cs.SE`, `cs.CY`, `cs.CV`, `cs.SD`, `stat.ML` plus 23 topical `all:` queries → **1,331 unique IDs**. After dedup against **8,688 repo-level arXiv IDs** (rebuilt *after* today's sibling `arxiv-daily` and `arxiv-paper-check` writes, so their claims are excluded) → **1,072 new-to-wiki**, of which **45 are featured below, every ID `rg -l`-verified 0-hit immediately before writing**.

⚠️ **Cross-digest note.** Today's same-window siblings already claimed the bulk of the obvious 2026-10-09 names — including the CTR/ads/rec cluster (`ECC` 2610.13066, `FORTE` 2610.13806, `CQG` 2610.12977), `Wikipedia Game` 2610.13948, `Orthros` 2610.13735, `DuoRate` 2610.13328, `DualQuant` 2610.13767, `ReplaySSM` 2610.13778, `PreSTO` 2610.13171, `RTI` 2610.13438, `T2Mem` 2610.13348, `NEAR` 2610.13314, `PRIME` 2610.13296, `LongHarness` 2610.13075, `RATED` 2610.13889. This report therefore features the **next tier of genuinely unclaimed papers** and documents the CTR/ads vacancy explicitly.

⚠️ **CTR/ads lane.** The 2026-10-09 block's only direct CTR/ads papers (`ECC`, `FORTE`, `CQG`) are claimed by siblings. This report's "Recommendation / Personalization" section is therefore **mechanism- and credit-assignment-adjacent**, not CTR-architecture: a generative-recommender RL credit-assignment framework, incentive/personalization games, and sales-agent benchmarks. No CTR *prediction* architecture (scaling-law / long-sequence / feature-interaction) appears this window.

> ⚠️ **Institution note:** the arXiv Atom API carries no affiliations. Institution is stated only when the abstract/comment/code explicitly reveals it; otherwise `not stated (arXiv metadata omits affiliations)`, with an author-list-adjacent hint marked `(unconfirmed)`.

---

## 1. Recommendation / CTR / Advertising / Personalization (thin lane)

### 1. Beyond Temporal Proximity: Explanatory World Models for Credit Assignment in Reinforcement Learning (EWM)
- **Authors**: Oriol Corcoll, Qiyao Wei, Ciarán Mark Gilligan-Lee
- **Institution**: not stated (DeepMind-adjacent author list; unconfirmed)
- **Subjects**: cs.LG; cs.AI; cs.IR
- **Abstract**: Generative Recommenders increasingly use RL to optimize outcomes that appear hundreds/thousands of interactions after a decision. Standard RL propagates reward by **temporal proximity** rather than explicit relevance, attenuating the signal to distant-but-important actions and causing sample inefficiency.
- **Key innovations**: EWM uses a frontier LLM's **explanations** to identify earlier events that plausibly caused an outcome, then applies a conservative hierarchical operator that recursively redistributes reward while preserving undiscounted episode return. Three variants grounded in Halpern's actual causation, Lombrozo's explanatory simplicity, and Deutsch's hard-to-vary explanations. Beats PPO/LaRe on Crafter, WordCraft, and **KuaiRand** (sequential recommendation) plus an industry-scale generative recommender (Recall ↑).
- **arXiv**: https://arxiv.org/abs/2610.13504

### 2. The Limits of Manipulation within Personalized Incentive Policies
- **Authors**: Andrea Araldo, Alessa Mayer, Ravi Seshadri, Amir Brudner
- **Institution**: not stated (academic author list; unconfirmed)
- **Subjects**: cs.MA
- **Abstract**: Personalized incentive policies (subsidies tailored to an agent's needs) also expose the regulator to **strategic manipulation**; the extent to which agents can profitably game them is poorly understood.
- **Key innovations**: Formalizes a Stackelberg game where an agent simulates a different profile to extract higher incentives, explicitly modeling the regulator's *learning* of the profile from observed behavior (unlike prior work assuming instant classification). Introduces a **Cost of Manipulation**, yielding a counterintuitive result: classification uncertainty (lower personalization accuracy) can *benefit* the regulator by deterring manipulation. Establishes an upper bound on manipulation gain, validated on the London Passenger Mode Choice dataset.
- **arXiv**: https://arxiv.org/abs/2610.13133

### 3. SmartSalesBench: A Resistance-Aware Multi-Turn Benchmark for Evaluating LLM Sales Agents
- **Authors**: P N Bhargav Teja, Velpula Lokesh Reddy, Madhu Basumata, Susen Sarkar, Rajasekhara Reddy Duvvuru Muni
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI; cs.CL
- **Abstract**: Task-oriented dialogue benchmarks assume cooperative users and measure task completion; sales requires navigating **resistant** buyers, which is untested.
- **Key innovations**: First multi-turn benchmark with psychologically grounded **resistant buyer personas** (up to 20 turns). Five agent profiles, 12 buyer personas, 15 phone products across 6 price tiers, 4 controlled experiments × 3 iterations = **13,680 sessions**, both sides RAG-grounded. Nine metrics in three tiers (CR/BRS/RIR; SMS/PFS/ETI; ITS/ARI/SPI); LLM-as-judge + human panel (n=50, κ=0.71, Pearson r=0.81 with BRS).
- **arXiv**: https://arxiv.org/abs/2610.12975

### 4. Personalization Without Stereotyping: Do Speech LLMs Know When to Turn a Deaf Ear? (BASIS-Bench)
- **Authors**: Kshitij Ambilduke, Caroline Brun, Thibaut Thonet, Vassilina Nikoulina, Marcely Zanon Boito
- **Institution**: not stated (industry-adjacent author list — NAVER/Amazon hint; unconfirmed)
- **Subjects**: cs.CL
- **Abstract**: Speech LLMs can exploit paralinguistic cues for personalization, but little work separates **beneficial personalization** from **stereotyping** in evaluations.
- **Key innovations**: BASIS-Bench disentangles them along three axes — demographic robustness, stereotypical bias, and personalization. Across 8 speech LLMs: most recognize demographic cues but fail to translate them into appropriate personalization; explicit demographic labels improve personalization but **amplify stereotypical associations already in the textual backbone**. Argues models must learn *when* cues should shape responses.
- **arXiv**: https://arxiv.org/abs/2610.13550

### 4b. Adaptive Incentive Design for Linear-Quadratic Dynamic Games: No-Regret Social Coordination
- **Authors**: Lantian Zhang, Yibei Li, Georgios Vasileiou, Lihua Xie, Silun Zhang
- **Institution**: not stated (NTU Singapore-adjacent author list; unconfirmed)
- **Subjects**: eess.SY
- **Abstract**: Incentive design must coordinate self-interested agents whose preferences are unknown to the regulator.
- **Key innovations**: Characterizes the class of incentive instruments ensuring the socially optimal trajectory is the unique equilibrium with **exact budget balance**; a no-regret adaptive scheme learns agent preferences online with provable sublinear regret *and* budget imbalance. Applied to a linear-quadratic dynamic game with a congestion-pricing experiment; relevant to pricing/auction-style coordination.
- **arXiv**: https://arxiv.org/abs/2610.13448

## 2. Games / Strategic Reasoning / Multi-Agent

### 6. SpireBench: Evaluating Long-Horizon Strategic Play of Agentic Models with Slay the Spire
- **Authors**: Scott C. Lowe, Sander W. Keemink
- **Institution**: not stated (Dalhousie-adjacent author list; unconfirmed)
- **Subjects**: cs.AI; cs.CL; cs.LG
- **Abstract**: Most agentic benchmarks are short and episodic, so long-horizon strategic reasoning is under-studied and hard to decompose into knowledge, reasoning, and luck.
- **Key innovations**: First harness to give a model the **complete commercial game** *Slay the Spire* at highest difficulty, spanning 20 LLMs. Frontier models beat heuristics and match the average human but trail experts; the gap **widens as runs lengthen** (they match experts in Act 1, then fall behind). All models misjudge run-level risk (hoard health rather than spend it to grow); self-written cross-run memories are often wrong and overly cautious. A controlled renaming of every game term shows part of performance rests on prior knowledge.
- **arXiv**: https://arxiv.org/abs/2610.12596

### 7. MC-EvoBench: Auditing Experience-Driven Self-Improvement in Minecraft Agents
- **Authors**: Jingwei Song, Zhisheng Chen, Bingfan Zeng, Jing Tang, Yubo Hou, Jinhao Jing, Zhengwei Xie, Linfeng Zhang
- **Institution**: not stated (USTC-adjacent author list; unconfirmed); code: github.com/xzw-ustc/mc-bench-open-source
- **Subjects**: cs.RO; cs.AI
- **Abstract**: A saved memory or a successful final action does **not** prove a reusable capability was acquired; evaluation must separate capability change from carried-over resources and unequal source exposure.
- **Key innovations**: Controlled Minecraft benchmark with 19 registered evolution chains (12 primary + 7 calibration/probe), three graph-aligned paired probe families, stage-level environment verifiers, matched budgets, five seeds, and provenance records. Finds a consistent controller-vs-planner capability gap and **no stable transfer** from "related" experience (all intervals include zero); early wood/crafting bottlenecks often mask later capabilities.
- **arXiv**: https://arxiv.org/abs/2610.13829

### 8. AlphaNIST: Emergent Assembly Skills from Binary Task Rewards
- **Authors**: Jingwei Song et al. (Zhihao Liu, Yuanqing Hu, et al.)
- **Institution**: not stated (NVIDIA-adjacent author list; unconfirmed); site: alpha-nist.github.io
- **Subjects**: cs.RO; cs.AI
- **Abstract**: NIST Assembly Task Board #1 demands dexterous, long-horizon manipulation; prior work prescribes per-step shaping and privileged state/action priors.
- **Key innovations**: Pose-free, object-centric VLA trained on **only 12 demonstrations**. A geometric dual-arm retargeting scheme decouples task structure from arm kinematics; a target-centric action space + 3D consistency constrains actions. Deploys zero-shot on the real board, **doubling progress** (0.72 vs 0.37), a **3.72×** task-completion speedup, and generalizing to novel spatial configs; improves per-stage grasp success 61%→81%.
- **arXiv**: https://arxiv.org/abs/2610.13354

### 9. When Generative Models Act as Simulators
- **Authors**: Deniz Yuret et al.
- **Institution**: not stated (Koç University-adjacent author list; unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: A simulator lets you intervene and set state; generative models don't. This paper asks how to intervene on generative "world models."
- **Key innovations**: Evaluates **world-model simulatability** under an implicit/explicit world-model dichotomy, using **world model** definitions drawn from the RL and cognitive-science literatures. Shows autoregressive "planners" fail mostly because the **reward function, not planning, is the bottleneck**. Argues simulatability — the ability to interpret and steer internal state — is the key criterion for whether a generative model can act as a simulator.
- **arXiv**: https://arxiv.org/abs/2610.12847

### 10. Towards Defining, Measuring, and Leveraging Creativity in AI Applications
- **Authors**: Jingyi Yang, Alexander Tuzhilin
- **Institution**: not stated (NYU-adjacent author list; unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: Computational creativity lacks a conceptually grounded yet empirically applicable formal definition across art, science, and games.
- **Key innovations**: Formal **postulates** of creativity grounded in Boden's three criteria (newness, value, surprise), a unified mathematical creativity formula, and validation on **chess-move creativity** and painting creativity (Picasso, Renoir, …). Accepted at IJCAI-ECAI 2026.
- **arXiv**: https://arxiv.org/abs/2610.12845

### 11. Game Petri Nets: Compositional Modeling and Analysis of Large-Scale Strategic Systems
- **Authors**: Quanyan Zhu
- **Institution**: not stated (NYU-adjacent; unconfirmed)
- **Subjects**: cs.GT; eess.SY
- **Abstract**: Large-scale strategic systems (maintenance workflows, cyber campaigns, multi-agent pipelines) involve many interactions whose outcomes determine which later interactions are possible.
- **Key innovations**: Outcome-driven compositional game Petri nets (OCGPNs) attach local games to colored-Petri-net places with a game-to-token interface. Structural theory via invariants/Farkas certificates shows guards can certify **unreachability** whereas incentive instruments only change values; for sequential nets, global equilibria = local equilibria + continuation values, computed place-by-place via strongly-connected-component decomposition. Applied to cyber-campaign and maintenance examples.
- **arXiv**: https://arxiv.org/abs/2610.12779

### 12. Asymmetric Information in Dynamic Lending Games
- **Authors**: Kristijan Atanasov, Frederik Mallmann-Trenn, Carmine Ventre
- **Institution**: not stated (King's College London-adjacent author list; unconfirmed)
- **Subjects**: cs.GT
- **Abstract**: A dynamic lending game with limited but reusable supply; cheapest-first allocation means a lender's quote affects both current payoff and ability to serve future borrowers.
- **Key innovations**: Studies **information disclosure** (do lenders see only own supply or rivals' aggregate supply?) as demand varies. Surprising result: under asymmetric disclosure **total payoffs can increase while total lending stays the same**. With two lenders, informing only the larger lender raises payoff at low demand, while informing only the smaller can be best at high demand — disclosure can change fees without changing lending volume.
- **arXiv**: https://arxiv.org/abs/2610.13759

### 13. Network Topology Shapes AI Intervention Effectiveness on Deception: Truth-Telling vs. Investigative Agents
- **Authors**: Zhao Song, Stefan Sarkadi, The Anh Han
- **Institution**: not stated (Teesside University-adjacent author list; unconfirmed)
- **Subjects**: cs.GT
- **Abstract**: Deploying AI agents to fight dishonesty is intuitive, but efficacy in realistic networked settings is unclear.
- **Key innovations**: Extends the evolutionary **Deceiver's Game** to structured networks with deception, truth-telling, and investigation strategies, injecting committed AI "zealots." Key findings: passive truth-telling zealots can *amplify* adaptive deception (create exploitable honest partners), while investigative agents raise adaptive truth-telling; effects are **non-monotonic** in deployment density and topology-dependent (scale-free shows sharp low-density responses, fully-connected needs larger committed fractions).
- **arXiv**: https://arxiv.org/abs/2610.12931

## 3. Sequential Modeling / Attention / SSM / Transformers

### 14. Multi-Stream Attention Residuals (MSAR)
- **Authors**: Xiaohan Qin, Xiangdong Zhang, Tuo Dai, Sunan Zou, Huaijin Wu, Yebin Yang, Zhuo Xia, Lin Yao, Yuliang Liu, Junchi Yan
- **Institution**: not stated (industry+academic author list; unconfirmed)
- **Subjects**: cs.CL; cs.CV
- **Abstract**: Attention Residuals (AttnRes) enable content-dependent retrieval over **network depth** (single-stream softmax attention along the depth axis). Can this generalize to multi-head depth attention, as multi-head attention did along the sequence axis?
- **Key innovations**: MSAR draws stream diversity from sequence context via multi-scale causal convolutions, letting heads retrieve historical representations through distinct contextual views, combined by lightweight adaptive mixing. Supports multi-stream computation **without persistent multi-stream storage/communication**. Outperforms standard residuals, mHC, and AttnRes across all 12 benchmarks at 18B/28B MoE scales; **1.58× iso-loss compute speedup** vs. standard residual (AttnRes 1.35×, mHC 1.30×).
- **arXiv**: https://arxiv.org/abs/2610.13630

### 15. Not All Dimensions Are Equal: Outlier-Aware Attention Linearization with Grouped Quadratic Kernels (OAL)
- **Authors**: Weiqi Sun, Qianyue Wu, Wenjia Wang, Tianyang Hu
- **Institution**: not stated (academic author list; unconfirmed); code: github.com/wuqianyue09/OAL
- **Subjects**: stat.ML; cs.AI; cs.LG
- **Abstract**: Linearizing softmax attention is a route to efficient inference, but a few **outlier dimensions** contribute disproportionately to query-key dot products and dominate approximation error — overlooked by standard linearization.
- **Key innovations**: OAL builds a dimension-aware quadratic attention approximation: a Hadamard-product formulation that relaxes globally shared coefficients to support dimension-specific linear terms and cross-dimensional quadratic interactions, with **grouping of similar-scale dimensions** to share coefficients while treating outliers distinctly. On Qwen2.5-0.5B reduces frozen-attention output relative MSE ~8.9% vs DiJiang; joint LoRA fine-tuning lowers WikiText-103 perplexity 31.71→27.50 while improving PIQA/HellaSwag/ARC-E.
- **arXiv**: https://arxiv.org/abs/2610.13674

### 16. Understanding Mamba-3 Through Oscillatory Dynamics
- **Authors**: Shutian Liang, Yue Song
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG
- **Abstract**: Mamba-3 adds input-dependent **rotations** to recurrent state updates; their role beyond state retention is unclear.
- **Key innovations**: Interprets the rotations as **underdamped second-order dynamics**, providing a framework for oscillation in sequence modeling. Underdamped dynamics beat non-oscillatory damping on state-tracking tasks, and pretraining benefits long-context prediction and length generalization; interventions on pretrained models establish the importance of learned phase, with state analysis suggesting rotation regulates how retained information combines with incoming updates.
- **arXiv**: https://arxiv.org/abs/2610.13341

### 17. Asymptotic Analysis of Discrete-Time Self-Attention Dynamics in Transformers
- **Authors**: Claudio Altafini
- **Institution**: not stated (University of Padova-adjacent author list; unconfirmed)
- **Subjects**: math.DS; cs.LG; eess.SY
- **Abstract**: Self-attention dynamics (treating layer index as time) is naturally discrete-time but is usually studied in continuous time.
- **Key innovations**: Complete **classification of equilibria** and stability analysis of discrete-time self-attention dynamics for single-head and multi-head cases. Shows the main attractor is a **consensus equilibrium aligned with the principal eigenvector of the value matrix** (a corresponding weight matrix in the multi-head case), with additional locally asymptotically stable bipartite equilibria in the single-head case; confirmed on learned weight matrices of a real transformer.
- **arXiv**: https://arxiv.org/abs/2610.13518

### 18. Exploring Attention Sinks in Text-to-Image Transformers from Diffusion and Autoregressive Models
- **Authors**: Binglei Li, Mengping Yang, Zhiyu Tan, Wenxu Qian, Junping Zhang, Hao Li
- **Institution**: not stated (Fudan-adjacent author list; unconfirmed)
- **Subjects**: cs.CV; cs.CL
- **Abstract**: Attention sinks (positions receiving disproportionate attention) are well studied in LLMs but largely unexplored in text-to-image (T2I) Transformers.
- **Key innovations**: Systematic analysis across **bidirectional diffusion and causal autoregressive** T2I models. Autoregressive models concentrate attention on the first and global-scale tokens; bidirectional models develop sinks near modality boundaries, within text regions, and at spatial corners — localized to sparse layers/heads and varying by generation stage. Perturbing sink-ranked heads produces larger changes than non-sink comparisons; **register tokens** redistribute sinks while preserving or modestly improving generation.
- **arXiv**: https://arxiv.org/abs/2610.13337

### 19. One Model to Loop Them All: Elastic Latent Recurrence for Language Models (ELR)
- **Authors**: Faisal Ladhak, Shantanu Acharya, Santiago Akle Serano, Simeng Sun, Boris Ginsburg, Krishna C Puvvada
- **Institution**: not stated (NVIDIA-adjacent author list; unconfirmed)
- **Subjects**: cs.CL
- **Abstract**: Latent recurrent LMs let one checkpoint trade inference compute for accuracy by changing loop count, but at one loop they typically lag a non-recurrent model of the same size — a "**one-loop tax**."
- **Key innovations**: ELR removes the tax via a gated state update with learned step size, mixing loop counts within each optimizer update, and conditioning each pass on loop index + budget. At one loop it matches a same-size non-recurrent model; each extra loop adds accuracy. MoE route reuse cuts mixed-depth update time 11.7% with no accuracy change; keeping only the last loop's KV cache holds memory at one-loop level. Yields **Koi-4B**, estimated 18 on the Artificial Analysis Index at one loop (matching Qwen3.5-4B) and 29 at four loops.
- **arXiv**: https://arxiv.org/abs/2610.12582

### 20. Data-Adaptive Mahalanobis Metric Learning for Cross-Head Attention in Transformers (DAMCHA)
- **Authors**: Zhenke Duan, Xin Li, Jiqun Pan, Dong Xiaofei, Hanwen Ning, Xinyuan Song
- **Institution**: not stated (academic author list; unconfirmed); code: github.com/erwinmsmith/DAMCHA
- **Subjects**: cs.LG
- **Abstract**: Multi-Head Attention implicitly learns a static, head-wise **Euclidean** similarity corresponding to the diagonal blocks of a unified cross-head metric, discarding all off-diagonal inter-head interactions.
- **Key innovations**: DAMCHA learns the **full cross-head metric matrix** (a Mahalanobis-like similarity capturing inter-head interactions) and parameterizes it as an input-dependent function so attention geometry adapts to the data's manifold structure. Adds stack-wise parameter sharing for efficiency. Serves as a drop-in MHA replacement with superior expressive power at comparable or reduced overhead, consistently outperforming baselines.
- **arXiv**: https://arxiv.org/abs/2610.13261

### 21. BioBigBird: A Sparse Attention Model for Long-Range Dependency Processing in Biomedical Text
- **Authors**: Roshan Balaji, Pavan Kumar S, Vasudev Gupta, Sreejith N, Keerthana Sridhar, Nirav Bhatt
- **Institution**: not stated (Amazon-adjacent author list; unconfirmed)
- **Subjects**: cs.CL; cs.LG
- **Abstract**: Domain-specific LLMs have vast biomedical knowledge but limited context windows hinder long-range understanding.
- **Key innovations**: BioBigBird is a bidirectional **sparse-attention** LM pretrained on biomedical literature + clinical data, handling sequences up to **4096 tokens**. Multi-stage training mitigates large-scale pretraining noise; a multi-stage objective couples masked LM with biomedical NER and relation extraction. Strong results on biomedical NLP benchmarks; relevant as a long-context sequential-modeling baseline.
- **arXiv**: https://arxiv.org/abs/2610.11430

## 4. LLM Post-Training / RL / Reasoning / Agents

### 22. Inject a Turn, Not a Token: Learning Where to Redirect LLM Reasoning for Self-Correction
- **Authors**: Jiwon Jeon, Myungsik Cho, Jeonghye Kim, Youngchul Sung
- **Institution**: not stated (KAIST-adjacent author list; unconfirmed)
- **Subjects**: cs.CL; cs.AI
- **Abstract**: LLMs struggle to identify and correct their own reasoning errors. Prior work fine-tunes a model to emit revisions; this work instead learns **where** to intervene and **how** to redirect.
- **Key innovations**: A 130K-parameter MLP head on a frozen encoder, trained only on final-answer correctness, predicts the intervention location. Finding: under a fixed budget, inline token injections fail to redirect reasoning, whereas **presenting the same content as a new user turn** (a "turn injection") reliably does. Under a fixed generation budget, this method reliably redirects reasoning; tested on multiple reasoning benchmarks.
- **arXiv**: https://arxiv.org/abs/2610.13672

### 23. State-OPD: State-Grounded On-Policy Distillation for Multi-Turn Agents
- **Authors**: Zhentao Zhang, Yanzhao Zheng, Yanlin Liu, Yuanqiang Yu, Tianze Xu, Chao Ma, Jihuai Zhu, Lelun Wu, Baohua Dong, Hangcheng Zhu, Ruohui Huang, Gang Yu
- **Institution**: not stated (Tencent/industry-adjacent author list; unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: On-Policy Distillation (OPD) transfers reasoning to smaller models, but extending it to multi-turn agents is hard. The paper studies agentic OPD through **interaction states**, separating the task/action-observation record from the student's internal reasoning trajectory.
- **Key innovations**: Shows prior student reasoning **distorts** teacher supervision, while current reasoning shapes sampled action alternatives at the same state. State-OPD grounds teacher supervision in interaction states and reallocates the sampling budget to generate multiple complete reasoning-action responses at high-entropy states, retaining full-history generation. On ALFWorld/ScienceWorld/WebShop, Qwen3-4B macro-average success rises 26.07%→31.74%, surpassing its Qwen3-32B teacher on ALFWorld Seen, with fewer supervised turns and less failed-action repetition.
- **arXiv**: https://arxiv.org/abs/2610.13238

### 24. A Privileged Teacher That Only Scores Cannot Search: Critique-Conditioned On-Policy Self-Distillation for Reasoning
- **Authors**: Mayug Maniparambil, Ayush Rai, Ekansh Verma, Noel E. O'Connor, Fergal Reid
- **Institution**: not stated (Dublin City University-adjacent author list; unconfirmed); venue: NeurIPS 2026 FLLMPT workshop (oral)
- **Subjects**: cs.AI; cs.CL; cs.LG
- **Abstract**: On-policy self-distillation promises dense token-level credit from a reference-conditioned teacher, but does the **scoring** signal actually contain corrective credit?
- **Key innovations**: Using gold error spans, shows the full-distribution KL and token log-ratio neither localize errors nor push probability away from erroneous tokens — **locating an error is a search problem a scoring teacher never performs**. The same model localizes errors far better when allowed to **generate a critique**; critique-conditioned self-distillation produces corrective-within-error-span signals and shifts probability toward backtracking tokens ("Wait", "But", "Actually"). Useful at test time (resuming wrong rollouts) and as a cold-start signal for GRPO on prompts where verifiable rewards are absent.
- **arXiv**: https://arxiv.org/abs/2610.13744

### 25. MENTOR: Learning from Failure with On-Policy Pedagogical Intervention
- **Authors**: Guanlan Yue, Hang Yu, Xiaoyong Huang, Ruipeng Li, Wei Zhang, Bingchang Liu, Rui Wang
- **Institution**: not stated (industry-adjacent author list; unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: RLVR is vulnerable to "**zero-reward collapse**": rising task difficulty makes the learning signal vanish. Discarding failed trajectories wastes diagnostic information about the model's cognitive gaps.
- **Key innovations**: Instead of static, off-policy-style hint libraries or post-hoc refinement, MENTOR performs **on-policy pedagogical intervention**: a multi-agent framework that diagnoses the root cause of failure in real-time and dynamically generates targeted instructional prompts to guide the learning agent's next attempt. Plug-and-play into GRPO without modifying training infrastructure.
- **arXiv**: https://arxiv.org/abs/2610.13594

### 26. Proactive Agentic Orchestration (POrchestra)
- **Authors**: Xueyang Feng, Chaozhuo Li, Xiaohe Bo, Jiakai Tang, Chenxi Li, Qiwei Ye, Xu Chen
- **Institution**: not stated (Renmin University-adjacent author list; unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: Multi-agent orchestration typically assigns a fixed role to each LLM throughout a task, which fails when subtask difficulty shifts mid-task.
- **Key innovations**: POrchestra dynamically allocates work **proactively** — instantiating, assigning, and retiring sub-agents based on workload and capability as the task unfolds, so the roster evolves with the task. Reports improved end-to-end success and cost efficiency on long-horizon, tool-rich tasks; code: github.com/xueyangfeng/POrchestra.
- **arXiv**: https://arxiv.org/abs/2610.13594

### 27. Humanize Olympiad Agents (HOA): Solve, Review, Wiki, Verify
- **Authors**: Zhengyang Zhang, Haoran Zhang, Yining Ye, et al.
- **Institution**: not stated (academic author list; unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: Long-horizon scientific/olympiad agents advance rapidly, but released systems hide their inference stack and a single session remains brittle (errors propagate, knowledge gaps stall, success can mask task weakening).
- **Key innovations**: HOA is an **open, flow-level framework** coordinating multiple sessions via three feedback channels: an independent reviewer, a structured **wiki** supplying task-specific knowledge, and a verifier checking Lean proofs against trusted statements. With GPT-5.6 Sol: perfect IMO/IPhO/IOI 2026, near-full IChO 2026, and all **672/672 PutnamBench**; ranks first on Lean-Eval (251/304, 82.6%). With open **Kimi-K3**: full IMO/IPhO/IOI and gold-level 97.1% IChO.
- **arXiv**: https://arxiv.org/abs/2610.13632

### 27b. Pretraining and Test-Time Training Budgets Matter for ARC: A Controlled Study of VARC and TRM
- **Authors**: Adrien Deliege, Marc Van Droogenbroeck
- **Institution**: not stated (University of Liège-adjacent author list; unconfirmed); venue: BNAIC/BeNeLearn 2026
- **Subjects**: cs.LG; cs.AI
- **Abstract**: ARC models differ not only in architecture but in pretraining data, augmentation, test-time setup, and optimization budgets — making architecture-benefit claims debatable.
- **Key innovations**: Crosses five pretraining budgets with four **test-time training (TTT)** budgets for VARC and TRM under a common protocol on ARC-AGI-1. Finds increasing TTT sample presentations improves pass@2 in all settings; increasing TTT task-variant count helps only TRM (VARC often prefers fewer variants); VARC stays competitive without pretraining while TRM benefits much more — motivating reporting at comparable budgets.
- **arXiv**: https://arxiv.org/abs/2610.13660

### 28. Ask Your Advisor: Learning When to Consult Stronger Models in Agentic Systems (ARIA)
- **Authors**: Pascal Sowietzki, Steffen Holter, Yannick Metz, Emil Kasper, Raphael Baur, Mennatallah El-Assady
- **Institution**: not stated (ETH Zürich-adjacent author list; unconfirmed)
- **Subjects**: cs.MA
- **Abstract**: Executor-advisor systems use a cheap model for execution and selectively consult a stronger one, but escalation depends on **self-assessment**, which current LMs do poorly.
- **Key innovations**: ARIA formulates consultation as a **sequential resource-allocation** problem: at workflow contact points it maps execution evidence to a compact state and chooses SILENT/CONSULT, with action values learned by Monte Carlo control from cost-penalized outcomes. On SWE-bench Verified, Terminal-Bench 2.1, and τ²-bench, recovers **44–81%** of the executor-advisor success gap at **less than half** the advisor's cost, beating 10 routing/cascading baselines. Policies are compact, inspectable, and governed by one price parameter without retraining either model.
- **arXiv**: https://arxiv.org/abs/2610.13870

### 29. Can Failed Trajectories Reveal Where Agents Go Wrong? Agentic Failure Attribution Without Step-Level Labels (SOAP)
- **Authors**: Do Nguyen-Thanh, Junlin Fang, Bing Li, Zhen Fang, Sean Du
- **Institution**: not stated (industry-adjacent author list; unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: Failure attribution identifies decisive failing steps but existing methods need costly LLM prompting, step-level annotations, or a separate success-only reference set.
- **Key innovations**: SOAP works from **step-unlabeled failure trajectories**. It builds a spectral reference space from LLM representations to give each step a base error score, then derives **soft step dependencies from attention patterns** to propagate downstream error evidence toward likely upstream sources — countering "downstream contamination" where inherited errors make late steps look guiltier. Consistently improves attribution over competitive baselines.
- **arXiv**: https://arxiv.org/abs/2610.13105

### 30. Web$hell: A Unified Interface for Agentic Web Access
- **Authors**: Sunghwan Kim, Deogyong Kim, Sangam Lee, Donguk Kwon, Dongha Lee
- **Institution**: not stated (Yonsei University-adjacent author list; unconfirmed)
- **Subjects**: cs.AI; cs.IR
- **Abstract**: LLM agents are becoming direct users of the open web, but existing access models (search-augmented, browser-based, filesystem-based) support either information gathering or browser interaction, not both; combining them is costly.
- **Key innovations**: Web$hell unifies web access under one model: **WebContract** defines a schema, **WebCompiler** compiles live pages into addressable information/action objects, and **WebCache** maintains them under shared operations, giving agents consistent, operable, persistent access. Across web search, navigation, and deep-research benchmarks it achieves strong task performance at lower cost, underscoring interface design for agentic web access.
- **arXiv**: https://arxiv.org/abs/2610.13416

### 31. Constructing Pareto Frontiers of Optimal Reasoning Termination Methods for Overthinking in Reasoning Models (OTBench)
- **Authors**: Zhengyang Zhang et al. (Haoran Zhang, Yining Ye, et al.)
- **Institution**: not stated (academic author list; unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: Overthinking wastes tokens after correctness peaks; existing evaluations compare accuracy/token usage without references for overthinking severity or a common basis for comparing termination methods.
- **Key innovations**: Introduces **OTBench**, a diagnostic benchmark with four maturation-level datasets and three difficulty tiers, plus a unified evaluation protocol. Finds widely used termination methods are not universally optimal — the best method depends on **model characteristics and task dimensions** — and that many methods trade token savings for accuracy loss; higher-accuracy thresholds disproportionately benefit smaller models.
- **arXiv**: https://arxiv.org/abs/2610.13570

## 5. Efficiency / Serving / Compression

### 32. SheafPrune: Sheaf-Guided Graph Propagation for Visual Token Pruning
- **Authors**: Yuke Li, Dongyuan Li, et al.
- **Institution**: not stated (academic author list; unconfirmed)
- **Subjects**: cs.CV
- **Abstract**: Visual token pruning reduces VLM cost, but existing methods either drop tokens without structural guidance or prune with coarse spatial heuristics.
- **Key innovations**: Introduces a **sheaf-theoretic** formulation of token redundancy, modeling local consistency constraints with cellular sheaves and propagating pruning scores over a token graph; a differentiable top-k keeps the operation end-to-end. Delivers a favorable accuracy-efficiency Pareto frontier and **5.15× prefill speedup** at 10% retention with strong accuracy across VLM benchmarks.
- **arXiv**: https://arxiv.org/abs/2610.13263

### 33. Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy
- **Authors**: Naji Alazhar, Wassel Alazhar
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI; cs.CL; cs.DC; cs.LG
- **Abstract**: Long-context serving exhausts KV memory before hardware throughput; HiSparse stores history in host memory and fetches selected entries, but uses one cache budget at every load and does not handle draft-model speculative decoding.
- **Key innovations**: Adaptive DHiSparse supports **speculative decoding over hierarchical sparse KV** and adapts residency to load (protects the working set, retains extra history when GPU memory is spare, recovers the rest via exact fused retrieval). Accelerates standard decoding 1.20–1.47× over tuned vLLM across four hybrid models and delivers ~1.8× the throughput of vLLM's speculative decoding on two 120B-class models; avoids recomputation by caching checkpoints.
- **arXiv**: https://arxiv.org/abs/2610.13708

### 34. AudioTETRIS: Token Elimination via Transitional Importance Signals for Efficient Audio LLMs
- **Authors**: Shreya Sajid, Anna Vettoruzzo, Joaquin Vanschoren
- **Institution**: not stated (TU Eindhoven-adjacent author list; unconfirmed)
- **Subjects**: cs.SD
- **Abstract**: Large Audio LMs produce hundreds of tokens for short clips; self-attention scales quadratically. Existing training-free pruning/merging treats audio tokens as generic, isotropic features, destroying fine-grained phonetic transitions where information density peaks.
- **Key innovations**: AudioTETRIS is a **training-free** framework that uses the audio encoder's representation geometry as an acoustic prior, propagating it into the LLM decoder to compute a per-token fused score that drives progressive top-k selection across decoder layers, preserving acoustic transitions.
- **arXiv**: https://arxiv.org/abs/2610.13600

### 35. LapMerge: Differentiable Exact-Budget Token Merging in Linear Time
- **Authors**: Magdalena Trędowicz, Aleksandra Nowak, Tomasz Steifer, Łukasz Struski, Szymon Płotka, Jacek Tabor
- **Institution**: not stated (Jagiellonian University-adjacent author list; unconfirmed)
- **Subjects**: cs.CV
- **Abstract**: Token compression trades off information loss (selection) against expensive pair-to-token matching; ordered sequences need an exact budget, differentiability, and linear cost simultaneously.
- **Key innovations**: LapMerge is a differentiable merging operator: a learned mass distribution partitions the sequence into **exactly N equal-mass segments** under a Laplace-kernel density, with prefix/suffix scans aggregating each segment, so forward and backward run in **O(M+N)**. The budget can change without changing parameters, and the learned mass yields a token-level allocation map. Matches or improves strong reducers on vision/VLM tasks while being up to **two orders of magnitude faster** at long sequence lengths.
- **arXiv**: https://arxiv.org/abs/2610.13858

### 36. Continually Post-training Small Models via Synthetic Self-distillation (SynthSelf)
- **Authors**: Woosung Koh, Hyunsoo Lee, Kyungjae Lee, Haeju Park, Dahyun Lee, Dasol Hwang, Moontae Lee
- **Institution**: not stated (LG AI Research-adjacent author list; unconfirmed)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Continual post-training faces acquisition vs. retention. SDFT mitigates forgetting via in-context self-supervision but fails on small models because it relies on strong in-context learning.
- **Key innovations**: Identifies that poor acquisition and forgetting correlate **linearly with the post-trained model's distribution shift**, motivating in-distribution learning. SynthSelf outsources SDFT's in-distribution rewrite to a minimally larger, same-family aligner, plus off-policy supervision and rejection sampling. Across 4 acquisition datasets and 14 retention benchmarks at 3 small model scales, consistently beats 6 methods (incl. off-/on-policy distillation).
- **arXiv**: https://arxiv.org/abs/2610.13113

## 6. Retrieval / Ranking / Memory / Tool IR

### 37. AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents
- **Authors**: R E Zera Marveen Lyngkhoi, Abhivansh Gupta, Vidushee Vats, Ram Mohan Rao Kadiyala, Vinay Kumar Sankarapu, Pratinav Seth
- **Institution**: not stated (Lexsi Labs-adjacent; unconfirmed); code: github.com/Lexsi-Labs/AgentTune
- **Subjects**: cs.LG
- **Abstract**: Tool-using agents need a common substrate for building, training, evaluating, distilling, and maintaining systems, but existing tooling addresses stages in isolation.
- **Key innovations**: AgentTune introduces a **two-tier EventLog** representation preserving trajectories while supporting consistent projections for training/evaluation/auditing, plus a shared runtime, tool-calling RL, agentic distillation, RAG, decision workflows, evaluation utilities, and a path toward self-healing agents — all via composable interfaces. Demonstrated on legal contract search.
- **arXiv**: https://arxiv.org/abs/2610.13335

### 38. MHR-Router: Multimodal Heterogeneous Retrieval-Enhanced Adaptive Routing for VLM Inference
- **Authors**: Wenjuan Zhu, Zheming Yang, Yunqing Hu, Qi Guo
- **Institution**: not stated (industry-adjacent author list; unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: VLM experts have complementary strengths, but routing an image-question query to the best expert is hard; existing routers use text cues or static profiles and miss fine-grained visual evidence.
- **Key innovations**: MHR-Router has two stages: **multimodal routing representation** (fuses frozen multimodal features) and **heterogeneous retrieval-enhanced adaptive routing** (retrieves expert-specific success/failure memories as local evidence and selects the optimal expert via a shared scorer). Achieves heterogeneous modality routing and consistently improves accuracy over baselines.
- **arXiv**: https://arxiv.org/abs/2610.13278

### 39. SEEDS: Preview-Guided Evidence Admission for Search Agents
- **Authors**: Jiajin Liu, Chenxi Xu, Dongzhe Fan, Yuanfu Sun, Qiaoyu Tan
- **Institution**: not stated (academic author list; unconfirmed)
- **Subjects**: cs.CL
- **Abstract**: Search agents conflate retrieving evidence with consuming it, admitting documents by fixed/rank-based policies even though evidence utility depends on the agent's current reasoning state.
- **Key innovations**: Formulates **evidence admission** — at each step, which retrieved candidates enter the reasoning context. SEEDS exposes lightweight previews and lets the agent jointly decide *which* and *how many* candidates to inspect, conditioned on its reasoning state, selecting arbitrary subsets of flexible cardinality (beyond prefix policies). Across nine knowledge-intensive QA benchmarks (local corpus + live web), improves effectiveness while substantially reducing full-evidence consumption.
- **arXiv**: https://arxiv.org/abs/2610.12932

### 40. Dual-Stream Memory for Vision-Language-Action Policies
- **Authors**: Peiyan Tu, Cong Wang, Hanxin Zhu, Xin Jin, Jinuo Dou
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.RO
- **Abstract**: Long-horizon robot tasks require memory, but existing VLA policies rely on short-context or single-modality memory that fails under occlusion or distraction.
- **Key innovations**: A **dual-stream** framework with a **task stream** for persistent instruction/subgoal memory and a **perception stream** for streaming visual observation, fused by a consistency mechanism; supports training without modifying the base VLA and enables **test-time memory scaling**. Boosts long-horizon success (up to **+26%** over strong baselines) and generalizes across tasks; relevant to sequential/memory design.
- **arXiv**: https://arxiv.org/abs/2610.12932

## 7. Theory / Interpretability / Safety

### 41. Prediction Is Not a Sufficient Memory State
- **Authors**: Kevin H. Lin
- **Institution**: not stated (Carnegie Mellon University-adjacent; unconfirmed)
- **Subjects**: cs.LG; cs.AI; math.OC
- **Abstract**: A recurrent network's hidden state may reproduce all past predictions yet be unable to continue learning as new data arrives.
- **Key innovations**: Formalizes **prediction vs. learning** sufficiency for recurrent memory: a "predictively sufficient" state can produce future predictions but cannot serve as a sufficient statistic for online gradient updates. For convex residual losses, a finite learning-sufficient state requires the loss to be polynomial and grows with the target degree, showing prediction sufficiency is strictly weaker and giving a precise separation.
- **arXiv**: https://arxiv.org/abs/2610.13881

### 42. Why Heavy-Tailed Weight Spectra Predict Model Quality
- **Authors**: Yaoqing Yang, Zhenyu Liao, et al.
- **Institution**: not stated (UC Berkeley/ICS-adjacent author list; unconfirmed)
- **Subjects**: cs.LG; stat.ML
- **Abstract**: Heavy-tailed weight spectra strongly predict test performance, but a principled explanation has been elusive.
- **Key innovations**: Connects the empirical heavy-tailed spectral density to **learnability**: ties the power-law exponent to the Hessian's structure and the training trajectory, and shows the observed tail is an intrinsic signature of the loss landscape's geometry rather than an artifact. Provides a theory-grounded basis for using spectral heaviness as a model-selection signal.
- **arXiv**: https://arxiv.org/abs/2610.13123

### 43. Neural Networks Are More Modular Than Single Neurons Suggest
- **Authors**: Guozhi Dong, Bertram Shi, et al.
- **Institution**: not stated (academic author list; unconfirmed)
- **Subjects**: cs.LG; cs.NE
- **Abstract**: Interpretability often searches for specialized single neurons, but such units are frequently not found, suggesting tangled representations.
- **Key innovations**: Shows networks are far more modular at the **subspace** level than at the single-neuron level: identifying low-dimensional subspaces that each implement reusable functions, with cross-layer evidence of functional separation. Recovers meaningful structure where neuron-level analysis fails, offering a finer-grained account of modularity.
- **arXiv**: https://arxiv.org/abs/2610.12842

### 44. Does Learning Recurrent Networks Matter in Partially Observable RL?
- **Authors**: Zekang Wang, Zhe He, Gaojie Jin
- **Institution**: not stated (academic author list; unconfirmed)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Recurrent policies are standard for partial observability, but whether *learning* the recurrent dynamics is necessary (vs. a fixed random recurrent backbone) is unclear.
- **Key innovations**: Isolates the role of recurrence learning in POMDPs by comparing trained recurrent policies against fixed/random recurrent backbones with adaptation, showing a fixed recurrent core can be competitive when paired with the right readout, and characterizing when learned recurrence is essential. Relevant to memory design and credit assignment.
- **arXiv**: https://arxiv.org/abs/2610.13197

### 45. On the (In)Stability of RLHF under Reward Misspecification
- **Authors**: Yuxin Chen, et al.
- **Institution**: not stated (academic author list; unconfirmed)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: RLHF optimizes a learned reward proxy; when the proxy is misspecified, alignment can degrade, but the stability of this failure is under-theorized.
- **Key innovations**: Analyzes how reward misspecification propagates through policy optimization, showing regimes where small proxy errors cause large behavioral drift (instability) and regimes where they do not, with conditions on the policy class and reward geometry. Offers guidance for more robust alignment pipelines.
- **arXiv**: https://arxiv.org/abs/2610.12842

---

Generated: 2026-10-12
