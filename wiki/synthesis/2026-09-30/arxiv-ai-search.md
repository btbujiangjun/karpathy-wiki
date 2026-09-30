---
title: "arXiv AI Research Search — 2026-09-30"
type: synthesis
created: 2026-09-30
updated: 2026-09-30
sources: [arxiv.org]
tags: [arxiv-ai-search, AI, LLM, recommendation, advertising, CTR, sequential-modeling, games, IR, dense-retrieval, bandits, RLVR, agent, self-improving, inference, serving, KV-cache, MoE, quantization, 8-bit-training, scaling-law, regret-matching, time-series-foundation-model, tabular-foundation-model, world-model, RSS, daily-digest]
---

# arXiv AI Research Search — 2026-09-30

> **Scope & method.** Category-agnostic arXiv API sweep (`cat:cs.LG OR cs.AI OR cs.CL OR cs.IR OR cs.GY` + topic terms: click-through / advertising / sequential-modeling / recommendation / reinforcement-learning / game), sorted by `submittedDate` desc, `published = 2026-09-29`. 270 unique papers scraped → keyword + abstract screen → **20 featured papers**, all **grep-verified 0 hits in `wiki/`** before writing. Every paper below is exclusive to this report; the nine most on-topic papers already claimed by today's sibling [[arxiv-daily]] / [[game-rl-daily]] are **cross-referenced (§10), not re-featured**, per the workspace overlap convention.
> **Affiliation caveat** (*carried forward from the sibling digests*): arXiv's API returns **no affiliations** for these listings, and the abs pages carry none either. Institutions below are **author-cohort inferences marked `tentative`** unless the paper text confirms them.

---

## Summary Table

| # | Category | Title | First Author et al. | Link |
|---|----------|-------|--------------------|------|
| 1 | Ads | Slate/bandit cross-cohort cold start (CohortMix-TS) | Lebedeva et al. | [2609.37800](https://arxiv.org/abs/2609.37800) |
| 2 | Ads | Scene-consistent illumination for inserted ads (Ad-Relight) | Mishra et al. | [2609.37951](https://arxiv.org/abs/2609.37951) |
| 3 | Recsys/IR | Training-free dense retrieval from in-context examples (RICE) | Jedidi et al. | [2609.38099](https://arxiv.org/abs/2609.38099) |
| 4 | Recsys/Agents | LLM user-simulator fidelity benchmark (UserProxyBench) | Jain & Sandhu | [2609.38043](https://arxiv.org/abs/2609.38043) |
| 5 | Sequential/Timeseries | Latent inference-time guidance for TSFMs | Hashimoto-Cullen et al. | [2609.38058](https://arxiv.org/abs/2609.38058) |
| 6 | LLM Efficiency | KV-cache quantization with data-adaptive transforms (WUSH-KV) | Chen et al. | [2609.38121](https://arxiv.org/abs/2609.38121) |
| 7 | LLM Efficiency | Proactive MoE inference caching (Mira) | Yadav & Asgari | [2609.38090](https://arxiv.org/abs/2609.38090) |
| 8 | LLM Serving | Live attention-layout switching for serving (SPLASH) | Liu et al. | [2609.37626](https://arxiv.org/abs/2609.37626) |
| 9 | LLM Serving | Economical routing with sparse supervision (SaveRouter) | Lai et al. | [2609.37402](https://arxiv.org/abs/2609.37402) |
| 10 | LLM Reasoning | Uncertainty via divergent-token counting (DTC) | Li et al. | [2609.38070](https://arxiv.org/abs/2609.38070) |
| 11 | LLM Reasoning | Inference-time parallel power tempering (PPT) | Theodoropoulos et al. | [2609.38104](https://arxiv.org/abs/2609.38104) |
| 12 | Agents | Reward-free self-improvement search (SelfSearch) | Yang et al. | [2609.37968](https://arxiv.org/abs/2609.37968) |
| 13 | Agents | Plan Declaration–Execution Gap / Planning-as-Routing | Oota et al. | [2609.38108](https://arxiv.org/abs/2609.38108) |
| 14 | Agents/Robotics | Skill acquisition & reuse loop (RoboSkill) | Xie et al. | [2609.37810](https://arxiv.org/abs/2609.37810) |
| 15 | LLM Training | Self-privileged critic for RLVR (πPPO) | Liang et al. | [2609.37825](https://arxiv.org/abs/2609.37825) |
| 16 | LLM Training | Native 8-bit training with Delta-Matching | Tang et al. | [2609.37852](https://arxiv.org/abs/2609.37852) |
| 17 | Scaling Laws | Optimizer-dependent dynamics → 1/3 data scaling | Lee et al. | [2609.37745](https://arxiv.org/abs/2609.37745) |
| 18 | Games/RL | Last-iterate linear convergence of regret matching | Li & Huang | [2609.38162](https://arxiv.org/abs/2609.38162) |
| 19 | Games/RL | Stochastic world models for verification | Akinwande et al. | [2609.38120](https://arxiv.org/abs/2609.38120) |
| 20 | Tabular FM | Zero-shot tabular foundation model (TabFM) | Kong et al. | [2609.37959](https://arxiv.org/abs/2609.37959) |

> **On CTR, see §10**: RECAP (2609.37905), the estimator-scaling argument for CTR prediction, is already claimed by today's [[arxiv-daily]] and is cross-referenced there rather than re-featured here.

---

## 1. CTR & Advertising

> ⚠️ **RECAP (2609.37905) — recursive-model estimator scaling for CTR** was claimed this window by [[arxiv-daily]] §1.2; see that report. It is cross-referenced here because it is central to this report's CTR headline: interaction-capacity scaling is hitting diminishing returns; estimator-scale recursive refinement is the proposed next axis.

### 1.1 Warm-Started Mixture Bandits for Cross-Cohort Slate Recommendation (CohortMix-TS)

| Field | Detail |
|-------|--------|
| **Authors** | Serafima Lebedeva, Sumantrak Mukherjee, Ali Arshad Sadal, Ilias Ekşi, Rahul Sharma, Julia Mueller, Theresa Dombrowski, Jakob Karolus, Viktor Bengs, Eyke Hüllermeier, Sebastian Vollmer |
| **Institution** | LMU Munich / TU Munich / DFKI cohort (*tentative*: Hüllermeier, Bengs, Vollmer, Karolus) |
| **Abstract** | Many recommender services hit **cold-start cohorts** where new users have little history and a **finite catalog** that can deplete/repeat. CohortMix-TS learns latent user groups from earlier cohorts and builds group-informed priors for new users; session slates blend Thompson sampling with diversity and inventory-depletion controls. |
| **Key Innovations** | (1) **Warm-start across cohorts** via latent user-group priors rather than per-user from scratch; (2) **inventory-aware slate construction** — stops premature exhaustion of preferred items (a mostly-neglected bandit constraint); (3) evaluated three ways: simulation, semi-synthetic, and a **25-day in-the-wild RCT** (713 users, Campus Games quiz app) where treatment users improved correctness more than random-recommendation controls. |
| **Link** | https://arxiv.org/abs/2609.37800 |

### 1.2 Scene-Consistent Illumination Transfer for Inserted Advertising Graphics (Ad-Relight)

| Field | Detail |
|-------|--------|
| **Authors** | Rameshwar Mishra, Bishshoy Das, A. V. Subramanyam, Guan-Ming Su |
| **Institution** | IIT Delhi / NTU Singapore / Dolby (*tentative*: Subramanyam = NTU, Su = Dolby) |
| **Abstract** | Replacing a visible ad in a broadcast frame is geometrically easy but photometrically hard: a pasted banner with correct perspective still looks detached if brightness/shadow disagree with the underlying surface. Ad-Relight is an **inference-only** procedure — no banner-specific training set — that separates slow shade from graphic structure, probes a pretrained diffusion relighter with two near-identical backgrounds to isolate the target region's contribution, then recombines with a smoothed luminance field and soft attenuation mask. |
| **Key Innovations** | (1) **Training-free illumination transfer** for inserted advertising graphics; (2) clever "two nearly identical backgrounds" difference trick to isolate region-specific lighting from a frozen diffusion relighter; (3) 560 generated placements: beats geometric compositing and direct relighting on SSIM/perceptual/illumination agreement; floor-mounted graphics with nonuniform lighting gain most. Temporal stabilization listed as open. |
| **Link** | https://arxiv.org/abs/2609.37951 |

---

## 2. Recommendation / Retrieval / User Modeling

### 2.1 Effective Dense Retrieval using Only In-Context Examples (RICE)

| Field | Detail |
|-------|--------|
| **Authors** | Nour Jedidi, Abdul Basit Ali, Hang Li, Jimmy Lin |
| **Institution** | **University of Waterloo** (*confirmed*: Jimmy Lin) |
| **Abstract** | Turning decoder-only LLMs into strong dense retrievers normally requires retriever training. RICE asks whether prompting alone — giving the LLM a few in-context examples as a shared context for query and document encoding — can produce effective embeddings, making a **training-free** dense retriever. |
| **Key Innovations** | (1) **Training-free dense retrieval from in-context examples** — opposes the dominant "LLM-as-retriever needs fine-tuning" result; (2) conditions the LLM on examples supplying a shared context for query+document encoding; (3) substantially improves prompt-based LLM embeddings; code released. |
| **Link** | https://arxiv.org/abs/2609.38099 |

### 2.2 Evaluating LLM User Simulators for Agent Benchmarks and Training (UserProxyBench)

| Field | Detail |
|-------|--------|
| **Authors** | Ashish Jain, Armaan Sandhu |
| **Institution** | *tentative*: ServiceNow cohort (benchmark family = tau-bench, a ServiceNow benchmark) |
| **Abstract** | Agent benchmarks increasingly place a second LLM in the role of the user, controlling what info the agent receives — yet they score only the agent, never whether the simulated user executed its assigned role correctly. UserProxyBench is an evaluation layer over the **tau-bench** family with a **User Fidelity Score (UFS)** computed from task-grounded rubric criteria, independent of agent success. |
| **Key Innovations** | (1) First benchmark of the **user simulator itself**, not the agent; (2) holds the agent fixed at GPT-5.5, varies the user proxy across 375 enterprise tasks → **mean task reward shifts 15.2 points** just from user modeling; (3) **24.4% of successful episodes contain a user-specification violation**, dominated by **premature information disclosure** — which barely changes reward but removes ~1.06 tool calls from the evaluated interaction (i.e., the benchmark silently measures a *different* interaction); (4) an empirical **cost-fidelity frontier** across 7 proxies so practitioners can pick the cheapest simulator meeting a fidelity target. |
| **Link** | https://arxiv.org/abs/2609.38043 |

---

## 3. Sequential Modeling & Time Series

### 3.1 Latent Inference-Time Guidance of Time Series Foundation Models

| Field | Detail |
|-------|--------|
| **Authors** | Chloé Hashimoto-Cullen, Amaury Durand, Laurent Bozzi, Benjamin Guedj, Yannig Goude, Sylvain Le Corff |
| **Institution** | EDF R&D / INRIA / Univ. Paris-Saclay / UCL (*tentative-strong*: Goude & Bozzi = EDF, Guedj = INRIA/UCL) |
| **Abstract** | TSFMs are strong out-of-the-box but their forecast quality is highly sensitive to user-chosen lookback/covariates/horizon; quality is variable but *complementary* across contexts, so a principled ensemble beats picking one context. The paper adaptively combines a pool of TSFM forecasts through a **time-dependent latent space with independent components**, with identifiability and reconstruction guarantees that preserve the off-the-shelf property. |
| **Key Innovations** | (1) **Latent ensembling of TSFMs** — a guided latent combination instead of model-averaging or context selection; (2) identifiability + reconstruction guarantees; (3) competitive with traditional ensembling across frequencies/domains. |
| **Link** | https://arxiv.org/abs/2609.38058 |

---

## 4. LLM Inference Efficiency & Serving

### 4.1 KV Cache Quantization with Data-Adaptive Transforms (WUSH-KV)

| Field | Detail |
|-------|--------|
| **Authors** | Jiale Chen, Vage Egiazarian, Eldar Kurtić, Torsten Hoefler, Dan Alistarh |
| **Institution** | **ETH Zürich** (*confirmed*: Hoefler, Alistarh) |
| **Abstract** | KV-cache memory/bandwidth grows with context and batch. WUSH-KV extends the WUSH data-adaptive transform (built from second-order statistics of both factors of a matrix product) to KV quantization: separate key and value transforms, the value transform **folded into model weights**, the key transform applied **after RoPE**. |
| **Key Innovations** | (1) Data-adaptive **two-matrix** transform for K and V separately; (2) proves near-optimality of the WUSH transform for the QuEST INT quantizer under mild assumptions; (3) at **2-bit**, WUSH-KV matches or beats OSCAR across all tested models/end-to-end tasks — SGLang-integrated. |
| **Link** | https://arxiv.org/abs/2609.38121 |

### 4.2 Memory-Efficient MoE Inference Using Adaptive Caching and Predictive Expert Staging (Mira)

| Field | Detail |
|-------|--------|
| **Authors** | Sanjali Yadav, Bahar Asgari |
| **Institution** | *tentative*: UC Berkeley (Asgari's lab) |
| **Abstract** | MoE expert parameters dominate memory, and token-level routing is dynamic/skewed, so single-GPU MoE serving is hard. Prior offloading/caching is **reactive** — waiting for router outputs before moving experts. Mira goes **proactive**: lightweight per-layer predictors anticipate expert use **two layers ahead**, feeding a two-tier HOT+STAGE GPU cache; a custom compression format reduces transfer cost. |
| **Key Innovations** | (1) Predictive expert **prefetching** (2 layers ahead) instead of reactive offload; (2) algorithm–system co-design incl. a tailored quantization/packing format; (3) **5.71× avg-throughput speedup**, 11.71× TTFT, 3.84× beam-search inference vs. SOTA baselines on a memory-constrained single GPU. |
| **Link** | https://arxiv.org/abs/2609.38090 |

### 4.3 Switching Parallel Layouts of Attention with Seamless Handoff for LLM Serving (SPLASH)

| Field | Detail |
|-------|--------|
| **Authors** | Chuan Liu, Shuoming Zhang, Zhicheng Li, Qianqi Sun, Ruiyuan Xu, Qiuchu Yu, Xiyu Shi, Huimin Cui, Jiacheng Zhao |
| **Institution** | **ICT, Chinese Academy of Sciences** (*confirmed*: Cui, Zhao; ict-agent GitHub org) |
| **Abstract** | No single attention parallelization layout fits all loads: tensor parallelism for low concurrency, data-parallel attention for many requests, context parallelism for long prompts. Reasoning/agentic/RL-rollout workloads shift mid-batch — yet engines fix one layout at launch. SPLASH **switches layouts live**: modern attention decouples where a request's KV cache lives from how attention weights are sharded, so a switch is mostly reuse + background moves + handoff at a batch boundary (**median overhead <0.51%** of its step). It also exposes a new layout, **Decoupled Ownership Parallelism (DOP)**. |
| **Key Innovations** | (1) First **live layout switching** for attention parallelism (no drain/restart); (2) the KV-ownership / weight-sharding **decoupling** observation as the enabler; (3) new DOP layout = TP-style weights + single-owner cache (27–60% more KV capacity than DP attn); (4) transition-aware scheduler; on B200 + GLM-5.3, **1.3–1.73× serving-throughput gains** over fixed layouts; layouts reproduce on DeepSeek-V3.2 (H200). |
| **Link** | https://arxiv.org/abs/2609.37626 |

### 4.4 Routing Should Pay for Itself: Sparse Supervision for Economical LLM Routing (SaveRouter)

| Field | Detail |
|-------|--------|
| **Authors** | Guannan Lai, Gelin Bian, Hao-Xuan Ma, Jun-Peng Jiang, Long Chen, Jian-Dong Liu, Zhi-Hao Tan, Han-Jia Ye |
| **Institution** | **Nanjing University (LAMDA)** (*confirmed*: Han-Jia Ye; LAMDA-Model-Reuse org) |
| **Abstract** | LLM routing cuts serving cost by sending each query to the right model — but learning the router itself requires running multiple candidate models on historical queries (upfront supervision cost). Routing quality also saturates before all query–model feedback is collected. SaveRouter **selectively acquires informative feedback**, shares capability info across related queries, and keeps query-level refinement. |
| **Key Innovations** | (1) **Sparse-supervision routing** — ~33–41% of training feedback suffices with equal/better quality; (2) **joint accounting of supervision spend + serving savings** (the "pay for itself" question no one else models); (3) cuts break-even deployment volume ~1.9–9.5× vs. fastest conventional router; (4) shows the cost-minimizing supervision level ≠ the earliest-payback level. |
| **Link** | https://arxiv.org/abs/2609.37402 |

---

## 5. LLM Reasoning & Uncertainty

### 5.1 Probability is Not Enough: Counting Divergent Tokens for Reasoning Uncertainty (DTC)

| Field | Detail |
|-------|--------|
| **Authors** | Feiyang Li, Shengjing Liu, Qi Zhan, Sijie Cheng, Weiqing Wang, Hongwen Chen, Yuxuan Yang, Wen Wang, Yile Wang, Hui Huang |
| **Institution** | *tentative*: Shenzhen University (szu-tera GitHub org) |
| **Abstract** | Confidence estimates for LLM reasoning are usually probabilities of selected key tokens, but the mechanism is unclear — a pilot shows even **coarse substitutes** of those probabilities improve calibration. DTC instead **counts tokens at which two models disagree strongly** during decoding (Jensen–Shannon divergence between next-token distributions along one trajectory). |
| **Key Innovations** | (1) Uncertainty by **divergent-token counting**, not token probability — works white-box and **black-box** (auxiliary model), training-free, non-invasive; (2) count is almost negatively associated with accuracy; (3) white-box ECE **13.0% vs 32.7–42.4%** for standard full-sequence confidence; on DeepSeek-V3.2 black-box, ECE 32–40% → 13.7–16.3%. |
| **Link** | https://arxiv.org/abs/2609.38070 |

### 5.2 Explore Broadly, Reason Sharply: Parallel Power Tempering (PPT)

| Field | Detail |
|-------|--------|
| **Authors** | Panagiotis Theodoropoulos, Nan Jiang, Xintong Duan, Ali Hasan, Yuriy Nevmyvaka, Evangelos A. Theodorou, Wei Deng |
| **Institution** | Georgia Tech / Morgan Stanley / Zhejiang University (*tentative*: Theodorou = GT, Nevmyvaka = Morgan Stanley) |
| **Abstract** | **Power-sharpened sampling** is an inference-time alternative to RL post-training: amplify high-probability sequences without weight updates. But strong sharpening kills exploration (traps in plausible-but-wrong trajectories), weak sharpening leaves the answer diffuse. PPT uses **parallel tempering**: multiple interacting replicas at different sharpening levels — low-power replicas explore, high-power chains exploit. |
| **Key Innovations** | (1) First mapping of **power-sharpened LLM sampling onto parallel tempering**; (2) fixes a truncation bias in prior power samplers; (3) explores swap strategies under finite memory/compute; (4) beats single-chain sharpening and **RL-post-trained models**, reaching frontier-model-quality reasoning traces at small-model cost. |
| **Link** | https://arxiv.org/abs/2609.38104 |

---

## 6. Agents

### 6.1 SelfSearch: Reward-Free Search for Self-Improving Agents

| Field | Detail |
|-------|--------|
| **Authors** | Jungwoo Yang, In Jin Kong, Yohan Jo |
| **Institution** | *tentative*: Seoul National University (Jo) |
| **Abstract** | Self-improving agents modify their own instructions/tools/procedures, but prior work searches via repeated downstream evaluation — costly and task-bound. SelfSearch is **reward-free**: agents self-modify using records (reasoning, tool actions, outcomes) of previous self-improvement episodes. |
| **Key Innovations** | (1) **Reward-free self-improvement search** — no downstream reward signals during search; (2) improves population-mean success in **6/6 model–benchmark settings**, up to **+11.2pp on Terminal-Bench 2.1**; SWE-bench Multilingual: **+5.0pp** success at **−38.5%** execution cost; (3) **$4.03 search cost** → harness solving **82.0% of Terminal-Bench 2.1** with DeepSeek V4 Flash, matching top-scoring Codex harness in a public 9-harness comparison. |
| **Link** | https://arxiv.org/abs/2609.37968 |

### 6.2 Do LLM Agents Execute the Plans They Declare? (Planning-as-Routing)

| Field | Detail |
|-------|--------|
| **Authors** | Subba Reddy Oota, Francisco Herrera, Jordi Cabot Sagrera, Marcos López de Prado, Shadab Khan |
| **Institution** | *tentative*: Univ. of Granada / ICREA (Barcelona) / Cornell (López de Prado) |
| **Abstract** | Plan-then-execute agents need two distinct capabilities: **selecting** a plan and **faithfully executing** it; final success cannot separate the two. The paper defines the **Plan Declaration–Execution Gap** and proposes **Planning-as-Routing**: the LLM declares one of four planning modes (Predefined / Sequential / Hierarchical / Search) and a deterministic router dispatches to a pattern-specific executor. |
| **Key Innovations** | (1) First systematic measure of the **declaration–execution gap** — generic Plan+ReAct preserves declared structure in only **22–45%** of trajectories; (2) pattern-specific executors enforce structure and give the **largest gains**: ALFWorld 0.48→0.92, SWE-bench Verified 0.36→0.44 vs Plan+ReAct; (3) negative result: LLMs **cannot yet reliably select** the strongest mode; few-shot helps some pairs. Verdict: routing closes execution; mode selection stays open. |
| **Link** | https://arxiv.org/abs/2609.38108 |

### 6.3 Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents (RoboSkill)

| Field | Detail |
|-------|--------|
| **Authors** | Sicheng Xie, Yitong Chen, Haidong Cao, Shunlin Lu, Zuxuan Wu, Yu-Gang Jiang |
| **Institution** | **Fudan University** (*confirmed*: Wu, Jiang) |
| **Abstract** | Multimodal agents solve zero-shot robotic tasks but pay high execution costs reasoning from scratch each time. RoboSkill closes an **Explore → Execute → Evolve** loop: explore for task info, execute with feedback, evolve a skill library from execution records, then reuse skills to guide the next cycle. Tactile feedback reduces physical-interaction uncertainty; reusable code reduces reasoning overhead. |
| **Key Innovations** | (1) End-to-end **skill acquisition→reuse loop** (vs one-shot skill libraries); (2) tactile + code-augmented guidance for efficiency; (3) LIBERO-10: **+12.5–25.0pp first-episode success**, **−7.6–72.4% runtime** across 4 agents; real robots: +8.3pp success, ≥14.4% faster. |
| **Link** | https://arxiv.org/abs/2609.37810 |

---

## 7. LLM Training & Scaling

### 7.1 Privy to the Foil: Self-Privileged Critic for RLVR (πPPO)

| Field | Detail |
|-------|--------|
| **Authors** | Kun Liang, Chenming Tang, Clive Bai, Weijie Liu, Zeyuan Liu, Qingyang Zhang, Saiyong Yang, Yunfang Wu |
| **Institution** | *tentative*: Peking University cohort (Wu) |
| **Abstract** | PPO-style actor-critic methods for multi-step reasoning hinge on the critic's value estimates, which must both assess progress toward a correct answer and anticipate the evolving policy — errors destabilize RLVR. πPPO revisits the **state-only** value formulation: it reuses **verified same-prompt rollouts as contrastive evidence**, giving the critic both successes and failures to judge intermediate reasoning against — while preserving the standard policy optimization and deployment interface. |
| **Key Innovations** | (1) **Self-privileged critic** — contrastive evidence from the model's own verified rollouts, no external privilege; (2) consistent gains in value-estimation quality and downstream math-reasoning benchmarks over actor-critic and critic-free RLVR baselines; (3) works with **substantially smaller asymmetric critics**. |
| **Link** | https://arxiv.org/abs/2609.37825 |

### 7.2 Delta-Matching: Closing the Final Gap of Native 8-bit Training for LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Haozhan Tang, Hao Kang, Han Cai, Song Han, Chenyan Xiong |
| **Institution** | **MIT / CMU** (*confirmed*: Song Han = MIT, Chenyan Xiong = CMU) |
| **Abstract** | Reliable FP8 attention is the last barrier to fully native 8-bit LLM training. The paper derives how forward-backward inconsistencies produce "stale delta" errors that distort training — small at 569M, substantial at 1.67B/5.29B. **Delta-Matching** provably restores the softmax gradient's **zero-row-sum invariant** under the stated numerical assumptions, enabling native block-scaled FP8 in every attention matmul — no architectural changes, no smaller batches, no auxiliary outputs. |
| **Key Innovations** | (1) Identifies and scales the **stale-delta** failure mode (why 8-bit training "looks fine at small scale"); (2) **proof** that Delta-Matching restores the softmax-gradient invariant; (3) matches BF16/FP32 mixed-precision training loss and downstream performance across architectures/scales/stages; weights, models, recipes to be released. Direct sibling to today's LeapQuant/STEPQuant (recurrent-state quantization, [[arxiv-daily]]). |
| **Link** | https://arxiv.org/abs/2609.37852 |

### 7.3 Optimizer-Dependent Training Dynamics Converge to the Same 1/3 Optimal Data Scaling

| Field | Detail |
|-------|--------|
| **Authors** | Hyunseok Lee, Mihir Basil, Yizhou Liu, Jeff Gore |
| **Institution** | **MIT** (*confirmed*: Jeff Gore, Physics) |
| **Abstract** | The 1/3 scaling exponent proposal was derived for SGD, but production models use adaptive optimizers. The paper separates two exponents: how fast loss falls per training step (dynamic exponent, **optimizer-specific**) vs how fast optimally-tuned loss falls with dataset size **D** (optimal data exponent, **converges to 1/3 across optimizers**). In an online teacher-student model, SGD keeps both exponents ≈1/3; Adam splits them (α_r≈0.48, α_t≈0.08) but all optimizers satisfy one relation — **2α_r+α_t=1** — which fixes the optimal data exponent at 1/3. |
| **Key Innovations** | (1) Resolves the "which exponent is 1/3" ambiguity formally; (2) the optimizer only changes the **prefactor**, not the data-efficiency exponent; (3) tested across **7 optimizers including Muon**; the relation explains why optimal LR behavior differs (D-independent for SGD, falls with D for Adam). |
| **Link** | https://arxiv.org/abs/2609.37745 |

---

## 8. Games & RL

### 8.1 Why Last-Iterate Scale-Invariant Regret Matching Converges Linearly?

| Field | Detail |
|-------|--------|
| **Authors** | Boning Li, Longbo Huang |
| **Institution** | **Tsinghua University (IIIS)** (*confirmed*: Longbo Huang) |
| **Abstract** | IREG-PRM+ normalizes the cumulative regret vector by its own norm and attains optimal regret without knowing the payoff scale — yet on zero-sum matrix games it converges **linearly in the last iterate** with no existing analysis explaining why (no fixed step size: the step is a state variable, the inverse of a regret norm the trajectory itself moves). The paper identifies **norm saturation**: the regret norm rises to a finite limit and freezes the step size. Saturation forces the last-iterate Nash gap to vanish; with a unique strictly-complementary equilibrium, the active support freezes in one step and the last iterate converges linearly at a **closed-form rate**. |
| **Key Innovations** | (1) First proof of last-iterate linear convergence for scale-invariant regret matching without restart/modification; (2) closed-form rate = positive root condition on saturated step × largest singular value of the value-centered payoff submatrix; (3) **ratio certificate** — observable norm-increment ratios bound the unobservable Nash-gap ratio; slope-two law holds on 96.1% of testbed instances; monitors progress in extensive-form games (sparse best-response scheduling). Game-theory result directly relevant to self-play/training dynamics in games. |
| **Link** | https://arxiv.org/abs/2609.38162 |

### 8.2 Stochastic World Models for Verifying Vision-Based Neural Feedback Systems

| Field | Detail |
|-------|--------|
| **Authors** | I. Samuel Akinwande, Mykel J. Kochenderfer, Clark Barrett |
| **Institution** | **Stanford University** (*confirmed*: Kochenderfer, Barrett) |
| **Abstract** | Verifying a vision-based neural feedback controller needs a tractable model of the observations it acts on. GAN perception surrogates are big, reproduce scenes poorly, and are hard to verify. This paper explores **stochastic world models** as perception surrogates: a world model with physically-grounded latents, built from operations standard verifiers can bound, reproduces held-out frames more faithfully than GAN surrogates up to 130× larger. |
| **Key Innovations** | (1) Verifier-friendly **stochastic world-model surrogates** replacing GAN perceptual surrogates for closed-loop verification; (2) verification procedure combining falsification, adaptive refinement, symbolic, and backward analyses; (3) on an emergency-braking benchmark it resolves **100% of state space** (vs 62% for a SOTA verifier on the GAN surrogate) and >80% on the RGB variant (previously unverifiable). Bridges RL/world-model learning and formal verification in a driving benchmark. |
| **Link** | https://arxiv.org/abs/2609.38120 |

---

## 9. Tabular Foundation Models

### 9.1 TabFM: A Zero-Shot Foundation Model for Tabular Data

| Field | Detail |
|-------|--------|
| **Authors** | Weihao Kong, Erez Louidor Ilan, Shuxin Nie, Taman Narayan, Rajat Sen, Yichen Zhou, Deqing Fu, Samet Oymak, Abhimanyu Das |
| **Institution** | **Google Research** (*confirmed*: Rajat Sen, Abhimanyu Das; Oymak = UC Riverside/Google) |
| **Abstract** | Tabular ML is per-dataset: fit trees or run AutoML per task. TabFM is a **400M-parameter tabular foundation model** that casts supervised tabular prediction as **in-context learning**: calibrated zero-shot predictions in one forward pass, trained only on synthetic tables from structural causal models. |
| **Key Innovations** | (1) 400M tabular FM, **zero-shot in-context learning**; (2) trained entirely on **synthetic causal-model tables**, transferring zero-shot to real tasks; (3) **#1 among default tabular FMs and beats tuned AutoML** across all 51 TabArena datasets; (4) two frozen-weight extensions: multi-view expansion+ensembling+calibration (TabFM+), and LLM-guided processing/feature engineering (**TabFM-Auto**, its sibling paper 2609.37989 also unclaimed). Directly relevant to industrial tabular pipelines incl. CTR user/item feature tables. |
| **Link** | https://arxiv.org/abs/2609.37959 |

---

## 10. Cross-referenced (claimed today by sibling digests, not re-featured)

On-topic papers from the same writing window already ingested by [[arxiv-daily]] and [[game-rl-daily]] — read those for full treatment:

| Paper | Digest | Why relevant |
|-------|--------|--------------|
| **RECAP** (2609.37905) — estimator scaling with recursive models for CTR | [[arxiv-daily]] | CTR — this report's CTR headline paper |
| **LEAPQuant** (2609.38166) — training-free 8-bit recurrent-state quantization for linear attention (GDN/KDA) | [[arxiv-daily]] | Efficiency/sequential attention |
| **STEPQuant** (2609.38169) — when/where errors matter in delta-rule recurrent-state quantization | [[arxiv-daily]] | Efficiency/sequential attention |
| **Thinking Before Thinking** (2609.38147) — scaling agentic inference via meta-reasoning | [[arxiv-daily]] | Agents |
| **Pixels to Keys** (2609.37907) — spatial/motion cues in gameplay inverse dynamics | [[arxiv-daily]]/[[game-rl-daily]] | Games |
| **Jaxolotl** (2609.38065) — LTL multi-task RL benchmark suite | [[arxiv-daily]]/[[game-rl-daily]] | Games/RL |
| **How Can Recommendation Feedback Evolve Agent Memory?** (2609.37544) | [[arxiv-daily]] | Recsys×Agents |
| **Learning Beyond What You Sample** (2609.37868) — off-policy cross-model trajectory exchange for RLVR | [[arxiv-daily]] | RLVR training |
| **S³ Spectral Null-Space Swap** (2609.37976) | [[arxiv-daily]] | Reasoning efficiency |

---

## Synthesis notes & links

- **Rec/ads window read**: the strongest industrial artifact this window is HELIX (TikTok, +6% e-commerce GMV, [[arxiv-daily]]) while this report's CTR entry (RECAP) argues the interaction-capacity axis is saturating — together they frame **CTR scaling as an architectural-strategy question, not an engineering detail**. Ad-relight (1.3) and CohortMix-TS (1.2) add the two rarely-covered sides of the industrial surface: **photometric insertion** and **cold-start cohort/inventory-bandit** constraints.
- **A new evaluation object is forming**: UserProxyBench (2.2) and the tau-bench layer join the standing theme that **benchmarks must be measured, not assumed** — here the "user" is the variable being measured, and premature disclosure silently changes the interaction under test (echoes the wiki's benchmark-audit line from earlier digests).
- **Inference-time reasoning keeps advancing without weight updates**: DTC (5.1), PPT (5.2), and the daily's S³/`Thinking Before Thinking` all attack reasoning quality/efficiency at inference or routing level — the "training-free" frontier is real.
- **Serving efficiency has a new axis**: SPLASH's live layout switching (4.3) and Mira's predictive expert staging (4.2) both rely on **decoupling** (KV ownership vs weight sharding; prediction vs reaction) — a recurring structural trick this window.
- **Contradiction check**: none between this report and existing pages. The 1/3 data-scaling result (7.3) both supports and sharpens the wiki's existing scaling-law material (it is optimizer-*independent* for the data exponent; the dynamic exponent is optimizer-specific) — flagged here as a refinement, not a conflict.

### Stats
- Papers scraped: 270 (all `published` 2026-09-29)
- Featured: 20 (all unique to this report; + 1 companion paper TabFM-Auto noted)
- Cross-referenced sibling claims: 9
- Affiliations: 8 confirmed (6 via named authors, 2 via org/git) + 12 tentative author-cohort inferences