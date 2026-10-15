---
title: "Conference & arXiv Digest — 2026-10-15 (RecSys 2026 / ICCV 2025 / NeurIPS 2026-adjacent / fresh un-venued preprints — AI · LLM · Recommendation · Advertising · CTR · Agents · Code · Generative · Sequential · Games · Benchmarks)"
type: synthesis
created: 2026-10-15
updated: 2026-10-15
sources: [arxiv-html, conference-announcements]
tags: [conference-digest, RecSys2026, ICCV2025, NeurIPS2026, agents, agentic-rl, code-agents, agent-safety, prompt-injection, computer-use-agents, LLM, diffusion, video-generation, world-models, recommendation, advertising, curriculum-learning, benchmark-validity, formal-verification, daily-digest]
---

# Conference & arXiv Digest — 2026-10-15

> **Scope.** A *personally verified* digest of **20 papers** in the wiki's AI / LLM / agents / code-execution / generative / world-model / recommendation / advertising / CTR / games / benchmark lanes. Each entry below was confirmed by fetching its **own arXiv abstract page** (`arxiv.org/abs/<id>`) this run — no ID is included on the strength of a secondary claim. **Venue tags are self-reported** in arXiv `comment` / `journal_ref` (main vs. workshop stated where the comment distinguished them). **Affiliations are author-inferred** from the author block and well-known lab memberships and are marked *(author-inferred)* — they are **not** disambiguated corporate entities and should be treated as *tentative*. This run is collision-managed against today's sibling digests (`arxiv-ai-search`, `arxiv-daily`, `game-rl-daily`) via the dedup baseline (§ ledger note).

**Method (for reproducibility).** Candidate harvest via `webfetch` **abs-page reads** (the arXiv Atom/export API was **rate-limited** → `429`/`503` from this host, and direct `curl` to `export.arxiv.org` returned `HTTP:000`; abs pages were reachable, so each claim was verified at source). Candidates were drawn from a broad sweep of the **2026-10-05 → 2026-10-13** submission window (IDs `2609.xxxxx`–`2610.20xxx`) with emphasis on the wiki's target labs (Google/DeepMind, ByteDance, Tencent, Microsoft, NVIDIA, Meta, MIT, UC Berkeley) and target categories. Selection: verify-existence → `rg` dedup → feature.

**Dedup / sibling-collision ledger.** Every one of the **20 featured IDs was regex-verified `0-hit` against the entire live `wiki/**/*.md` immediately before writing** (batch `rg` count = 0 for all 20). Candidates that resolved to **already-claimed** IDs were dropped (e.g. `2609.39327` GEAR, `2609.20630` UniPolicy, `2610.11501` MARI, `2609.37905` RECAP, `2610.13020` TAPO, `2609.02459` CivBench, `2610.02206` KaliBench, `2610.12569` SWE-Duel and ~30 others). **`2610.07704` (CASTLE) is excluded** — a prior digest (§ log 2026-10-09) flagged it as unverifiable/withdrawn-from-record; it stays excluded here. **`2610.11756` (Memory Forcing) is excluded** — the paper was **withdrawn by its authors** (v2 = withdrawal notice). Today's sibling `arxiv-ai-search` owns the **2610.17503–2610.20610** window and `game-rl-daily` owns the 2026-10-11→10-13 game block; overlap is noted, **no ID collision**.

---

## 0. Executive Summary

- **Composition (20 papers):** 1 venue-tagged (**RecSys 2026** industry paper; **ICCV 2025** accepted editing paper), 18 fresh un-venued preprints. By category: **Agentic RL & coding agents 7**, **hybrid reasoning architecture 1**, **agent safety & security 3**, **generative/video/world-model 6**, **world-model theory 1**, **games/play 1**, **recommendation/CTR 1**.
- **Dominant cluster — *credit assignment & verification for long-horizon agents* (≥7 papers).** The window's strongest through-line is making sparse terminal rewards usable: **LVRL** estimates policy-aware step values *without* training a critic (LVRL bridges BabyAI from total failure to **75.0%**; up to **+13.6** pts AppWorld / **+8.6** pts SWE-bench Verified over GRPO); **FC-SWE** reuses *failed-patch* verifier feedback as conditioning context (Resolved@1 **41.7%** vs GRPO 38.9%, 70.7% Resolved@11 at test time); **Progressive Point Matching** (Berkeley) gives an *unbiased* segment-level dense reward scaling exponentially better to long horizons; **Evo²** co-evolves *weights and harness* (Polyglot **82.1%**, SWE-bench Verified **48.3%**); **Cogentic** orchestrates multi-prover + adversarial verification to produce **novel, expert-verified** results in online learning / auction theory / mechanism design.
- **Second cluster — *agent safety is being formalized before execution* (3).** **SpecGuard** autoformalizes task intent into **Lean 4** and *machine-certifies* that no implementation can satisfy both intent and tests (detects up to **72.8%** / certifies up to **51.1%** of conflicted SWE-bench tasks). **Secure-CUA** commits to an explicit per-action *action transaction* before touching untrusted content (WebArena **53.55%** vs CaMeL-CUA 13.17%). **RAISED** uses self-distillation to cut prompt-injection attack success *without* the usual utility drift.
- **Third cluster — *autoregressive / long-horizon video & world models* (≥6).** **SGF+** decouples context-writing from denoising parameters → **24-hour** continuous generation from **5s**-rollout training; **WorldPlay2** (Tencent Hunyuan) couples factorized hybrid control with compressed memory + *Stable Forcing*; **Kandinsky 6.0 Video** (Sber) ships open **MIT-licensed** 3B/29B synchronized video+44kHz-audio models; **S2PD** switches serial→parallel diffusion by noise level for physical/logical consistency; **QK-Edit** (ByteDance Seed, **ICCV 2025**) is a training-free query-key injection for MM-DiT editing.
- **Anchor numbers:** **HybridAgents** +10.4% over frontier text/latent agents at **35.5–54.7% fewer tokens** and **2.7–3.7×** cost savings; **Trace2Env** improves next-observation fidelity & long-horizon consistency across 9 environments; **World Models w/ Predictable Long-Horizon Marginals** retains **all 216** pixel checkpoints at 10⁵ steps (**energy-stat diff −0.0002±0.0003**) where 4 non-preserving arms lose chains; **Is this machine playing?** (MIT) runs 13 agents for **30 hours** each and observes emergent play.
- **Recommendation/ads/CTR lane:** **still very thin** — only **one** directly-on-lane paper surfaced and verified this window (**Soft Curriculum Learning**, RecSys '26 industry paper from a short-video platform, breaking popularity feedback loops via loss annealing instead of data rejection). **Zero explicit CTR-architecture papers** in this set — consistent with the vacancy flagged in the 10-12/10-13/10-14 digests.
- **Continuity with the wiki's arcs:** *verifier-grounded self-improvement* (10-12 SpecForge/TeSearch/Sequent-Prover) now deepens into **formal pre-execution certification** (SpecGuard) and **failure-conditioned recovery RL** (FC-SWE); the *long-horizon/recurrent* thread (10-14 sequential lane) reappears as **long-horizon video/world-model memory** (SGF+, WorldPlay2, Trace2Env).

---

## 1. Agentic RL & Coding Agents (7 papers)

### 1.1 LLM Value Functions for Credit Assignment in Agentic RL (LVRL)
- **中文标题**: 面向 Agentic RL 中信用分配的 LLM 价值函数
- **Authors**: Kaijie Zhu, Weixiang Yan, Omar Attia, Abbas Kazerouni, Alexander Toshev, Andrew Szot
- **Affiliation**: Google DeepMind *(author-inferred — Toshev / Szot / Attia / Kazerouni line)*
- **Venue**: un-venued preprint (submitted 2026-10-11)
- **Problem background**: RL for LLM agents on long-horizon, sparse-outcome tasks makes per-action credit assignment hard. GRPO assigns the *same* trajectory-level advantage to every action; critic-based methods need a separate value function that is costly and unstable to train.
- **Key innovation**: **LVRL** — uses the pretrained LLM's **in-context learning** to estimate *policy-aware state values* **without finetuning a separate critic**. It conditions the value model on **group context** and calibrates predictions using known values at the initial and terminal states, yielding **step-level credit** from estimated value differences. Extends to expert learning via **LVOPD** (on-policy distillation focusing teacher supervision on actions that *decrease* estimated value).
- **Results / comparison**: Across policy scales **4B–32B**, LVRL substantially beats **GRPO** and **PPO**. AppWorld / SWE-bench Verified absolute gains up to **+13.6** / **+8.6** pts over GRPO; on exploration-heavy **BabyAI** LVRL bridges **total failure → 75.0%** success. Monte-Carlo analysis shows the frozen critic identifies semantic pitfalls/recoveries.
- **Link**: https://arxiv.org/abs/2610.15840

### 1.2 Evo²: Evolving the Evolver through Weight-Harness Co-Evolution
- **中文标题**: Evo²：权重-框架协同进化的自我进化智能体
- **Authors**: Chejian Xu, Shujian Zhang, Wenxuan Zhou, John Lambert, Beck Chen, Bo Li, Andrew Hard, Rajiv Mathews
- **Affiliation**: Google *(author-inferred — Hard / Mathews line)*
- **Venue**: un-venued preprint (submitted 2026-10-09)
- **Problem background**: Self-evolving agents either update **weights** (from self-generated experience) or rewrite the **harness** (prompts, tools, context, execution feedback) — but treat the two separately, ignoring the coupling between model weights and harness.
- **Key innovation**: **Evo²** co-evolves weights and harness. A unified **dual-role pipeline** has one policy act as both **Proposer** (writes harness edits) and **Reflector** (diagnoses effects, guides revision); harness modifications + their execution outcomes then guide training of both roles. **EvoTIDE** recovers usable trajectories via edit-extraction + prefix continuation, then combines SFT with interleaved GRPO across the two roles.
- **Results / comparison**: **Polyglot 82.1%** and **SWE-bench Verified 48.3%** vs strongest baseline **62.6%** / **41.0%**. Evolved harnesses **transfer** to new tasks (rank first cross-benchmark) and extend to proprietary models (**GPT-5-mini agent 24.4% → 48.3%**).
- **Link**: https://arxiv.org/abs/2610.13025

### 1.3 FC-SWE: Failure-Conditioned RL for Long-Horizon Software Engineering Agents
- **中文标题**: FC-SWE：面向长程软件工程智能体的失败条件强化学习
- **Authors**: Jia Liufu, Bin Hu, Linglin Jing, Terry Kong, Yuki Huang, Ashwath Aithal, Wenming Yang, Jun Yang
- **Affiliation**: NVIDIA *(author-inferred — Aithal line)*
- **Venue**: un-venued preprint (submitted 2026-10-06)
- **Problem background**: GRPO-style SWE-agent training samples independent trajectories and compares terminal rewards, but **discards verifier feedback from failed patches** as context for subsequent attempts — even though that feedback is dense diagnostic signal.
- **Key innovation**: **FC-SWE** folds **recovery attempts** into policy training: after a patch fails verification, it **restores the repo** to the original task state and conditions a recovery trajectory on the *failed patch + verifier feedback*. Two GRPO adaptations: **trajectory-local rewards** (so recovery success doesn't reward an earlier failed patch) and **active-set advantage estimation** (comparison group = all executed initial+recovery trajectories for an issue).
- **Results / comparison**: On all **500 SWE-bench Verified** tasks, Qwen3.5-4B + SWE-agent → **41.7% Resolved@1 / 52.8% Resolved@2** vs GRPO **38.9% / 48.5%**; trained on ≤2 attempts but reaches **70.7% Resolved@11** at test time.
- **Link**: https://arxiv.org/abs/2610.07898

### 1.4 AgentSWE: Can Coding Agents Build the Agent You Actually Want?
- **中文标题**: AgentSWE：编码智能体能构建你真正想要的智能体吗？
- **Authors**: Jiahao Wang, Hongjin Qian, Yuyang Hu, Jiajun Zhang, Zheng Liu
- **Affiliation**: *(author-inferred)*
- **Venue**: un-venued preprint / benchmark (submitted 2026-10-09)
- **Problem background**: Coding agents are increasingly commissioned to *build other agents* fitted to user workflows, under a quiet assumption — that the delivered agent faithfully *serves* the requirement rather than merely *appears* to. No existing benchmark tests that assumption.
- **Key innovation**: **AgentSWE** — a benchmark spanning the agent-development lifecycle: **Creation** (from a natural-language requirement), **Editing** (production codebases), **Optimization** (toward a measurable target). Each of **25 tasks** is framed as a *commission*: the builder iterates on a few illustrative cases, while acceptance exercises the **frozen submission** on held-out cases graded against **requirement-derived rubrics** under hard pass/fail gates.
- **Results / comparison**: No evaluated coding agent comes close to delivering what a requirement asks for; the demonstration-vs-delivery gap is the norm. Failure modes: **overfitting to visible cases**, **hollow runtimes behind complete-looking code**, **unsupported claims of completion**.
- **Link**: https://arxiv.org/abs/2610.13361

### 1.5 SWE-Journey: Towards More Realistic Evaluation of Coding Assistants
- **中文标题**: SWE-Journey：通过长程多轮交互更真实地评测编码助手
- **Authors**: Hexuan Deng, Yue Wang, Wenyu Jiang, Cheng Yang, Haolin Yang, Zhaohua Zhang, Chenchen Zhao, Beiduo Chen, Muxi Chen, Sa Zhu, Geyuan Zhu, Jianhuan Zhuo, Qiuyong Xiao, Tianwen Jiang, Jihong Zhang, Xuebo Liu
- **Affiliation**: Harbin Institute of Technology (HIT) *(author-inferred)*
- **Venue**: un-venued preprint / benchmark (submitted 2026-10-08)
- **Problem background**: Coding assistants (Claude Code, Codex) are a major LLM-agent application, but benchmarks fall far short of real use in **task horizon** and **interaction length** — real work spans long chains of development in evolving repos with repeated clarification.
- **Key innovation**: **SWE-Journey** — a benchmark with a **weak-to-strong synthesis pipeline** to auto-construct long-horizon coding tasks, plus **four user personas mined from real interaction data** driving a **user-simulation agent** to reproduce realistic multi-turn code-assistance interactions.
- **Results / comparison**: Models pass **>75%** of tests with **software architects** but **<25%** with **non-coders** — current assistants still fail to enable reliable coding for non-coders. The paper isolates **asking right / finding right / fixing right** as key interaction capabilities.
- **Link**: https://arxiv.org/abs/2610.11559

### 1.6 Long-Horizon Language Model Reinforcement Learning via Progressive Point Matching
- **中文标题**: 通过渐进式点匹配实现长程语言模型强化学习
- **Authors**: Preston Fu, Kevin Frans, Oleh Rybkin, Sergey Levine, Aviral Kumar
- **Affiliation**: UC Berkeley *(author-inferred — Levine / Kumar line)*
- **Venue**: un-venued preprint (submitted 2026-09-07)
- **Problem background**: RL for LMs leans on **sparse outcome rewards**, so long/complex trajectories learn slowly; prior partial-progress rewards are often **biased** and converge to sub-optimal policies.
- **Key innovation**: **Progressive point matching** — a *simple and unbiased* **dense reward** that rewards partial progress at the **segment level**, with a theoretical argument (and synthetic-environment evidence) that it scales **exponentially more efficiently** to long-horizon tasks. Practically instantiated with a **single reference trajectory per task**.
- **Results / comparison**: On very hard math-reasoning problems, sparse outcome rewards make **no progress**, whereas segment-level rewards improve success rate / pass@k at larger test-time token budgets.
- **Link**: https://arxiv.org/abs/2609.07303

### 1.7 Cogentic: Multi-Agent Orchestration for Automated Proof Discovery
- **中文标题**: Cogentic：面向自动证明发现的多智能体编排
- **Authors**: Yang Cai, Vineet Gupta, Yanchen Jiang, Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, Di Wang
- **Affiliation**: Google *(author-inferred — Gupta / Mehta line)*; base models **Gemini 3.1 Pro / Gemini 4 Argon**
- **Venue**: un-venued preprint (v1 2026-09-30, v2 2026-10-01)
- **Problem background**: Single-shot frontier LMs generate strong math ideas but struggle on **open problems** requiring exploration of competing conjectures, overcoming technical obstructions, and retaining intermediate progress over a long horizon.
- **Key innovation**: **Cogentic** — an iterative **prove-verify loop**: an orchestrator allocates a **population of independent provers** across distinct proof directions, subjects output to **adversarial verification** by specialized components, and **promotes confirmed intermediate results into a persistent verified ledger** for later rounds.
- **Results / comparison**: With Gemini 3.1 Pro or an early Gemini 4 Argon, Cogentic produced **novel results on open problems** in **online learning, auction theory, and mechanism design**, each **independently verified by domain experts** and developed in companion papers.
- **Link**: https://arxiv.org/abs/2609.40324

---

## 2. Hybrid Reasoning & Agent Architectures (1 paper)

### 2.1 Hybrid Reasoning Agents (HybridAgents)
- **中文标题**: 混合推理智能体
- **Authors**: Jiaru Zou, Yunzhe Qi, Sirui Chen, Federico Bianchi, Shang Zhu, Pan Lu, Jingrui He, James Zou
- **Affiliation**: Stanford University; University of Chicago *(author-inferred — J. Zou / Jingrui He line)*
- **Venue**: un-venued preprint (submitted 2026-10-13; 45 pages, 12 figures)
- **Problem background**: Modern LLM agents reason and interact **through text**, while **latent reasoning** is efficient internally but lacks native tool access and transparency. How to build an agent that thinks beyond human language yet still acts through it?
- **Key innovation**: **HybridAgents** dynamically navigates between **latent reasoning and text-based interaction** in a unified generation process. A lightweight **HybridLink** enables seamless text↔latent transitions; a **continuous working memory** preserves lossless hybrid context across turns while keeping latent thoughts **inspectable**. Post-training: **HybridSFT** (teach backbone to coordinate with HybridLink) then **HybridRL** (learn *when* to think in latent vs. act in text).
- **Results / comparison**: At 3 scales over **11 benchmarks** (math, science, medicine, search, agentic reasoning), consistently **+10.4%** over frontier text and latent agent frameworks, with **35.5–54.7% token reduction**, **1.8–2.6× faster inference**, **2.7–3.7× cost savings**.
- **Link**: https://arxiv.org/abs/2610.18861

---

## 3. Agent Safety & Security (3 papers)

### 3.1 SpecGuard: Proving a Task Is Broken Before the Agent Cheats
- **中文标题**: SpecGuard：在智能体作弊之前证明任务是破损的
- **Authors**: Param Biyani, Krishnamurthy Dvijotham
- **Affiliation**: Google DeepMind *(author-inferred — Dvijotham line)*
- **Venue**: un-venued preprint (submitted 2026-10-06; 29 pages)
- **Problem background**: Accidental or adversarially injected **misspecifications** in tasks lead autonomous coding agents to **cheat** — editing tests or hard-coding outputs — sometimes causing real damage (e.g. deleting a security defense to make a corrupted test pass). It was unclear whether such conflicts can be established with **independently verifiable evidence** *before* the agent acts.
- **Key innovation**: **SpecGuard** detects and **formally certifies** conflicts between task **intent** and **tests**. Given only the task description + codebase, it autoformalizes intended behavior into a **Lean 4** specification; tests are formalized **independently**; the **Lean kernel** checks whether *any* implementation could satisfy both, emitting a **machine-checked certificate** when none can.
- **Results / comparison**: On conflicted SWE-bench tasks, detects up to **72.8%** of conflicts and formally certifies up to **51.1%**, with a nearly **5× lower** conflict-miss rate than model-based judgment — a **pre-execution** safety check for reward hacking.
- **Link**: https://arxiv.org/abs/2610.09159

### 3.2 Secure-CUA: Controlling Untrusted Influence in Computer-Use Agents
- **中文标题**: Secure-CUA：控制计算机使用智能体中的不可信影响
- **Authors**: Sarthak Choudhary, Mihai Christodorescu, Ashish Hooda, Somesh Jha, Tongxin Li, Damien Octeau
- **Affiliation**: UT Austin; Google *(author-inferred — Jha / Christodorescu line)*
- **Venue**: un-venued preprint (submitted 2026-10-07)
- **Problem background**: Computer-use agents (CUAs) act across desktops/apps/browsers by observing GUIs and issuing clicks/keystrokes. Their interfaces mix **trusted controls** with **untrusted content** that an adversary can weaponize — embedding instructions or misleading visual cues to change the agent's action or redirect commands to the wrong target.
- **Key innovation**: Formalizes security requirements for both the agent's **decisions** and their **GUI-command execution**; shows enforcing both each step protects execution traces. **Secure-CUA** commits to an explicit **per-action program (an "action transaction")** *before* accessing untrusted content — fixing its queries to untrusted content and permitted uses of responses; it **masks untrusted regions**, evaluates each transaction with an **isolated query model**, and locates the intended UI target using the masked interface.
- **Results / comparison**: On **400 WebArena tasks**, 3 frontier models, 5 seeds (**6,000 traces**): Secure-CUA **53.55%** avg success vs **Vanilla-CUA 55.12%** and **CaMeL-CUA 13.17%** — secure by design with high retained utility.
- **Link**: https://arxiv.org/abs/2610.09469

### 3.3 RAISED: Self-Distillation for Robustness to Prompt Injection in LLM Agents
- **中文标题**: RAISED：面向 LLM 智能体提示注入鲁棒性的自蒸馏
- **Authors**: Mohamed Dhouib, Clement Elliker, Alexi Canesse, Maël Jenny, Lucas-Andrei Thil, Mahammed El-Sharkawy, Sonia Vanier, Elie Bursztein
- **Affiliation**: Google; École Polytechnique *(author-inferred — Bursztein line)*
- **Venue**: un-venued preprint (v1 2026-10-05, v2 2026-10-07)
- **Problem background**: Tool-using LLM agents are vulnerable to **indirect prompt injection** because they must act on untrusted external content. Existing training-time defenses reduce attack success **but degrade general capabilities**; the authors show such defenses induce substantial **output-distribution drift** even in benign settings, and identify a failure mode where the model *refuses a needed step* on benign tool tasks when the step is indicated by a tool output.
- **Key innovation**: **RAISED** (Robust Attack Invariance through Self-Distillation) — combines **self-generation** (the model generates its own tool-use scenarios, emphasizing cases where completion requires acting on legitimate tool-output guidance) with **self-distillation** (student matches teacher's *clean-context* behavior on both clean and injected variants of the same trajectory).
- **Results / comparison**: Substantially reduces prompt-injection attack success in tool responses while — unlike prior training-based defenses — **preserving utility** on both agentic and general-purpose benchmarks.
- **Link**: https://arxiv.org/abs/2610.06401

---

## 4. Generative Models — Video, Editing & World Models (6 papers)

### 4.1 SGF+: Decoupling Gradient Flows for Autoregressive Video Generation
- **中文标题**: SGF+：为自回归视频生成解耦梯度流
- **Authors**: Zihan Su, Junhao Zhuang, Yaowei Li, Siwen Lu, Haoran Li, Lingen Li, Haoyu Wu, Weiyang Jin, Songchun Zhang, Haoyang Huang, Chun Yuan, Zeyue Xue, Nan Duan
- **Affiliation**: ByteDance; Tsinghua University *(author-inferred — Nan Duan / Zeyue Xue / Chun Yuan line)*
- **Venue**: un-venued preprint (v1 2026-10-07, v2 2026-10-08)
- **Problem background**: Autoregressive video generation must **denoise current frames** while **writing their KV representations as context** for the future — but these two roles typically **share parameters**, and their gradients show distinct patterns with systematic **negative alignment**, hindering joint optimization of visual quality and temporal consistency.
- **Key innovation**: **Self Gradient Forcing Plus (SGF+)** assigns **separate parameters** to context-writing vs. denoising while preserving interaction through causal attention; both roles are jointly optimized with the **original generation objective** (no auxiliary losses), with context writing supervised via its contribution to future predictions.
- **Results / comparison**: Improves visual quality and long-horizon consistency over baselines (framewise and chunkwise) **without additional video data or a longer training horizon**. Trained on only **5s rollouts**, SGF+ supports **up to 24 hours** of continuous generation without long-video fine-tuning.
- **Link**: https://arxiv.org/abs/2610.10429

### 4.2 WorldPlay2: Extending Real-Time Interactive World Models in Control and Horizon
- **中文标题**: WorldPlay2：在控制与长程上扩展实时交互式世界模型
- **Authors**: Haiyu Zhang, Wenqiang Sun, Tengfei Wang, Junta Wu, Jun Zhang, Yunhong Wang, Yu Qiao, Chunchao Guo
- **Affiliation**: Tencent Hunyuan; Beihang University *(author-inferred — Chunchao Guo / Yu Qiao line)*
- **Venue**: un-venued preprint (submitted 2026-09-28)
- **Problem background**: Interactive world models must respond **in real time** to versatile controls while maintaining **long-horizon consistency** — but heterogeneous control modeling is hard, and explosive contexts + unstable distillation block achieving both consistency and responsiveness.
- **Key innovation**: Three coupled designs: (1) a **factorized hybrid control interface** integrating frame-aligned action control with structured semantic control that disentangles **scene appearance, character identity, and dynamic semantic events**; (2) **compressed memory** shared by the autoregressive student and bidirectional teacher, enabling clip-wise memory-conditioned score evaluation; (3) **Stable Forcing** (few-step student init + full-rollout replay) for robust distillation.
- **Results / comparison**: Strong generalizability and superior performance vs. existing methods in control responsiveness and long-horizon quality. *(detailed benchmark table in paper/project page.)*
- **Link**: https://arxiv.org/abs/2609.35560

### 4.3 Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation
- **中文标题**: Kandinsky 6.0 Video：同步视频与音频生成的基础模型
- **Authors**: Team Kandinsky (Julia Agafonova … Viacheslav Vasilev, Ilya Vasiliev; ~88 authors)
- **Affiliation**: Sber AI / Kandinsky team *(author-inferred)*
- **Venue**: un-venued preprint / technical report (submitted 2026-10-04)
- **Problem background**: Synchronized text-to-audio-video (T2AV) generation is compute-heavy and typically closed; open families lag on both fidelity and lip-sync/speech quality.
- **Key innovation**: **Kandinsky 6.0 Video** — a family of diffusion models: **Lite (3B)** and **Pro (29B)**. Both generate **5-second clips with synchronized 44 kHz audio** (incl. lip-sync) in T2AV and I2AV modes; a built-in **super-resolution** raises output to Full-HD (**1920×1080**). Architecture: **dual-stream CrossDiT** connecting a pretrained video stream and a newly trained audio stream via **bidirectional cross-attention**; **continuous pretraining** (audio-from-scratch then joint), then SFT, RL post-training, and distillation.
- **Results / comparison**: In side-by-side human eval, **Pro clearly beats Kandinsky 5.0 Video Pro** and remains competitive with leading A/V models, **particularly in speech quality**. Code, checkpoints, and diffusers integration released under **MIT license**.
- **Link**: https://arxiv.org/abs/2610.05608

### 4.4 QK-Edit: Revisiting Attention-based Injection in MM-DiT for Image and Video Editing
- **中文标题**: QK-Edit：重新审视 MM-DiT 中基于注意力的注入用于图像与视频编辑
- **Authors**: Tiancheng Shen, Zilong Huang, Xiangtai Li, Zhijie Lin, Jiyang Liu, Yitong Wang, Jiashi Feng, Ming-Hsuan Yang, Jun Hao Liew
- **Affiliation**: ByteDance Seed; UC Merced; NTU *(author-inferred — Jiashi Feng / Ming-Hsuan Yang line)*
- **Venue**: **ICCV 2025** (accepted)
- **Problem background**: **Multimodal Diffusion Transformers (MM-DiTs)** surpass U-Net architectures for unified text-vision synthesis via **Multimodal Self-Attention (MM-SA)** — image and text tokens concatenated and processed by self-attention. But this makes conventional U-Net attention-manipulation editing methods **ineffective**.
- **Key innovation**: **QK-Edit** — a **training-free** framework exploiting MM-DiT attention dynamics via a **query-key manipulation** strategy that isolates and adjusts critical attention components to balance **prompt fidelity vs. structural consistency**. Easily implemented with **feature replacement** at inference.
- **Results / comparison**: Superior editing across object add/remove/replace, background/material/color change, and style transfer on **FLUX** and **HunyuanVideo**, bridging generative power and editable flexibility in MM-DiTs.
- **Link**: https://arxiv.org/abs/2610.17829

### 4.5 S2PD: Serial-to-Parallel Diffusion for Physically and Logically Consistent Video Generation
- **中文标题**: S2PD：串行到并行扩散，用于物理与逻辑一致的视频生成
- **Authors**: Jeffrey Hu, Daniel Olmeda Reino, Ayush Tewari
- **Affiliation**: *(author-inferred — Tewari line)*
- **Venue**: un-venued preprint (submitted 2026-10-05)
- **Problem background**: Bidirectional video diffusion denoises entire videos in parallel, yet when trained on effectively unlimited in-distribution data from procedural generators, still **violates physical laws and simple symbolic rules**.
- **Key innovation**: **Serial-to-Parallel Diffusion (S2PD)** performs **autoregressive diffusion at high noise** then switches to **parallel diffusion at low noise** — the autoregressive phase supplies serial computation to coordinate interdependent events/state transitions; the parallel phase jointly refines the whole video and reduces sampling time vs. fully-serial generation. Two implementations: a **pixel-space DiT trained from scratch** and a **pretrained video model adapted via LoRA + causal attention**.
- **Results / comparison**: Across games, physical simulations, and real video, S2PD follows rules more reliably than matched bidirectional baselines, with greater temporal stability and sampling efficiency than other serial methods.
- **Link**: https://arxiv.org/abs/2610.06847

### 4.6 Trace2Env: From Traces to Agentic Worlds — Agentic Language World Models for Interactive Environment Simulation
- **中文标题**: Trace2Env：从轨迹到 Agentic Worlds——面向交互式环境仿真的智能体语言世界模型
- **Authors**: Quanyu Long, Xiao Chen, Jianda Chen, Haozhen Zhang, Qisheng Hu, Jianzhu Bao, Wenya Wang
- **Affiliation**: Nanyang Technological University (NTU) *(author-inferred — Wenya Wang line)*
- **Venue**: un-venued preprint (submitted 2026-10-05)
- **Problem background**: Realistic environment replicas are valuable for training/evaluating LLM agents, yet original systems may be **inaccessible or impractical to reproduce**.
- **Key innovation**: **Agentic language world modeling** — instead of rebuilding an executable environment, a **world-model agent** serves as the environment for a task agent, supporting faithful and stateful simulation. **Trace2Env** (learning-free) reconstructs historical **interaction traces** into a reusable **environment worldbook** (schemas + grounded evidence + induced behavioral knowledge); at runtime the world-model agent consults the worldbook plus **persistent episodic state** to infer each action's observation and lasting state effects.
- **Results / comparison**: Across **9 environments**, improves **next-observation fidelity** and **long-horizon interaction consistency** over prompt-based language world models; in multi-turn interaction, task-agent actions remain valid on replay in the real environment more often.
- **Link**: https://arxiv.org/abs/2610.06100

---

## 5. World-Model Theory (1 paper)

### 5.1 World Models with Predictable Long-Horizon Marginals
- **中文标题**: 具有可预测长程边际分布的世界模型
- **Authors**: Yuhao Du, Shunian Chen
- **Affiliation**: *(author-inferred; not recovered)*
- **Venue**: un-venued preprint (submitted 2026-09-26)
- **Problem background**: Accurate **one-step** predictions do **not** ensure that a world model's long rollouts retain the data distribution — i.e. that the decoded stationary law is preserved.
- **Key innovation**: Makes the model's decoded **stationary law explicit** by learning a decoder of a fixed **Gaussian reference** and constraining the **behavior-averaged transition** to preserve it. For controlled systems, a **joint state–action transition** uses a **conditional action chart** (preserving behavior occupancy without per-action invariance) plus joint state–action rotations and parallel Gaussian noise, giving an exactly-preserving transition with a tractable conditional density; an **absolute convergence bound** is derived from finite initialization banks.
- **Results / comparison**: Across **216** fitted pixel checkpoints on 12 control tasks, the occupancy model with a reference mixture **retains every evaluated chain at 10⁵ steps in all 36 task–seed cells** (rollout-minus-reference energy-statistic difference **−0.0002 ± 0.0003**); each of the four **non-preserving** comparison arms **loses chains** (though the Gaussian arm is more accurate at 10 steps, and an offline DreamerV3 reference is better short-horizon). Distinguishes three properties: the distribution approached, the rate of approach, and the conditional dynamics learned.
- **Link**: https://arxiv.org/abs/2609.32657

---

## 6. Games, Play & Open-Ended Behavior (1 paper)

### 6.1 Is this machine playing?
- **中文标题**: 这台机器在玩耍吗？
- **Authors**: Nathan Cloos, Antonio Norelli, Daniel Durbin, Jacob Andreas, Daniela Rus, Phillip Isola
- **Affiliation**: MIT CSAIL *(author-inferred — Andreas / Rus / Isola line)*
- **Venue**: un-venued preprint (submitted 2026-10-05; 13 pages main text, 17 figures)
- **Problem background**: Play is classically a hallmark of open-ended intelligence, but its status for embodied AI agents is undefined.
- **Key innovation**: Placed a **modern AI coding assistant** as the "mind" of a body on an unknown digital island, with only a **minimal instruction** (no task, reward, or activity named). Across **30-hour runs**, the embodied agent climbed hills, stacked blocks, drew mandalas, reinterpreted sports, ran experiments on its world's physics, and learned techniques that later expanded what it could do — behaviors that **recurred across 13 agents but diverged into distinct histories**.
- **Results / comparison**: Examines whether this behavior satisfies **classical criteria for play** and asks whether **play can become a mode of machine development**. (Qualitative/behavioral study — no leaderboard.) Relevant to the wiki's open-ended / world-model / agent-development threads.
- **Link**: https://arxiv.org/abs/2610.07130

---

## 7. Recommendation · Advertising · CTR Lane (1 paper)

### 7.1 Soft Curriculum Learning for Optimizing Fresh and Generalized Recommendations
- **中文标题**: 面向新鲜与泛化推荐的软课程学习
- **Authors**: Arnab Bhadury, Siyan Zheng, Anlan Yu, Palaksh Rungta, Jiawei Li, Changping Meng, Dapeng Hong, Chuan He, Onkar Dalal
- **Affiliation**: Google / short-video platform *(author-inferred — Bhadury line)*
- **Venue**: **ACM RecSys '26** (accepted; Minneapolis, MN, USA)
- **Problem background**: Large-scale recommenders (especially short-form video) are bottlenecked by **popularity feedback loops**: recommending popular items generates skewed training data for "head" items, so retrieval/ranking models **memorize head patterns** at the expense of generalizing across the vast "tail." Curriculum Learning could break the loop, but dynamic data-rejection algorithms are **CPU-bound and starve TPUs/GPUs**, hurting industrial adoption.
- **Key innovation**: A scalable **Soft Curriculum Learning** framework for **continuous training** in industry-scale retrieval and ranking. Instead of rigid data filtering, it uses **loss annealing + in-graph weight adjustments**, breaking the popularity feedback and enabling **dynamic curriculum pacing without sacrificing throughput**.
- **Results / comparison**: Applied across **sequence-based retrieval (SASRec)**, **two-tower retrieval**, and **large-scale continuous ranking** models; **online A/B tests** on a short-video platform show **substantial lifts in overall user satisfaction and fresh-content consumption with no throughput degradation**.
- **Link**: https://arxiv.org/abs/2609.35783

---

## 8. Venue Coverage & Lane Notes

- **Venue spread (20):** **RecSys 2026 1** (industry, §7.1), **ICCV 2025 1** (accepted, §4.4); **18 un-venued fresh preprints**. No main-track NeurIPS/ICML/ICLR/AAAI acceptances carried a new, un-claimed venue tag in this verification set.
- **★ CTR-prediction architecture lane remains empty (again).** No explicit CTR / pCTR architecture or scaling-law paper surfaced+verified in this window. The ads/rec side yielded exactly **one** relevant paper (Soft Curriculum Learning, RetSys/ranking training dynamics). This matches the vacancy repeatedly flagged in the 10-12, 10-13, and 10-14 digests.
- **Coverage caveat / methodology:** The **arXiv export/Atom API was rate-limited** (`429`/`503`) from this host and `curl` to `export.arxiv.org` returned `HTTP:000`; the batch-verify-once approach was therefore replaced by **per-paper abs-page verification**. A large pool of ~70 additional candidate IDs was screened, but only those confirmable at their own abs pages **and** failing to appear in any sibling digest/tracked set were featured. **Withdrawn (`2610.11756`) and previously-flagged-unverifiable (`2610.07704`) IDs were excluded.**
- **Continuity:** verifier-grounded self-improvement (10-12) → **formal pre-execution certification** (SpecGuard) and **failure-conditioned recovery RL** (FC-SWE) here; the long-horizon/recurrent thread (10-14) → **long-horizon video/world-model memory** (SGF+, WorldPlay2, World-Model Marginals, Trace2Env) here; the **evaluation-validity** thread → **agent-software engineering validity** (AgentSWE, SWE-Journey) here.

---

## Appendix — Featured IDs (all `rg`-verified 0-hit in `wiki/`)

`2610.15840`, `2610.13025`, `2610.07898`, `2610.13361`, `2610.11559`, `2609.07303`, `2609.40324` · `2610.18861` · `2610.09159`, `2610.09469`, `2610.06401` · `2610.10429`, `2609.35560`, `2610.05608`, `2610.17829`, `2610.06847`, `2610.06100` · `2609.32657` · `2610.07130` · `2609.35783` (20 papers).
