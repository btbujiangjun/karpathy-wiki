---
title: "Conference & arXiv Digest — 2026-10-11 (NeurIPS 2026 / EMNLP 2026 / ICML 2026 / ICLR 2026 / ICLR 2027-under-review / CIKM 2026 / AAAI 2026 / RecSys-Ads lane)"
type: synthesis
created: 2026-10-11
updated: 2026-10-11
sources: [arxiv-export-api, arxiv-html, conference-announcements]
tags: [conference-digest, NeurIPS2026, EMNLP2026, ICML2026, ICLR2026, CIKM2026, AAAI2026, agents, LLM, code-execution-prediction, looped-llm, world-models, memory, evaluation, calibration, safety, adversarial, recommendation, advertising, CTR, ranking-bandits, diffusion, offline-RL, continual-learning, KV-cache, daily-digest]
---

# Conference & arXiv Digest — 2026-10-11

> **Scope.** Papers carrying a *verified* venue tag from **NeurIPS 2026, EMNLP 2026, ICML 2026, ICLR 2026, CIKM 2026, AAAI 2026**, plus **ICLR 2027 (under review)** preprints and the wiki's recsys/advertising/CTR lane. **45 papers featured**, organized by venue, then category. This run was **collision-managed against today's two siblings** — `arxiv-ai-search` (44) and `arxiv-daily` (49) — that both landed *before* this run's dedup baseline was built, so the baseline already excludes them (§0).

**Method (for reproducibility).** Harvest via the **arXiv export API** (`export.arxiv.org/api/query`, Atom XML): **43 serialized queries** — 17 venue `co:`/`comment:` sweeps (pull the newest ~100 matching each tag, so 2026 acceptances surface regardless of submission date), 8 category sweeps bounded to `submittedDate:[20261001 … 20261009]`, and 18 topical `all:` queries (recommendation, click-through rate, advertising, auction, CTR prediction, ranking, retrieval, agent, world model, game playing, reasoning, reinforcement learning, diffusion model, sequential recommendation, code execution, benchmark, generative recommendation, large language model) — spaced ≥2.2 s. **3,370 unique records → 1,281 unclaimed + comment-venue-flagged → 240 published ≥ 2026-09-25 with an explicit venue tag → 62 shortlisted → 45 featured.** Venue tags were read from each entry's arXiv `comment` / `journal_ref` fields and are self-reported (main vs workshop vs oral stated where the comment distinguished them). **Affiliations were read only from the paper's own arXiv HTML author block**; unresolved items are marked *(affiliation not recovered)* rather than guessed. The API's fresh-announcement window is **frozen at 2026-10-08** (`submittedDate:[20261009 TO 20261012]` returns 0; latest indexed block is 2026-10-08) — same frozen window as both siblings.

**Dedup.** Baseline regex-extract of every arXiv ID across `wiki/**/*.md` at run start (built *after* today's siblings committed) → **8,567 claimed IDs**. All **45 selections re-verified `rg -l` 0-hit against the whole live wiki immediately before writing**; **0 collisions**. No acronym/name-collision defects found during the ID-level sweep.

---

## 0. Executive Summary

- **Venue spread (45 papers):** NeurIPS 2026 **14** (11 main + 2 Datasets & Benchmarks/evals track + 1 workshop), EMNLP 2026 **12** (3 main oral), ICML 2026 **4** (1 mechanistic-interpretability workshop), **ICLR 2026** 1, **CIKM 2026** 2, **AAAI 2026** 1, **ICLR 2027 (under review)** 7 — plus **4** un-venued RecSys/Ads/CTR-lane papers. Empty this window: **ACL 2026, EMNLP 2025, NeurIPS 2025, KDD 2026, SIGIR 2026, WWW 2026, RecSys 2025, CVPR 2026** (§9).
- **Industry density (10 of 45 have a company author/affiliation):** **AWS 2** (On the Clock co-affiliation; Teaching-Agents-to-Code Stanford+AWS), **Qualcomm AI Research 1**, **BMW AG 1** (CRISP), **Shell 1** (CANDO/ALPS-Bench), **Shopify 1** (TreeWalker), **Tencent 1** (SlimKV), **Meta Reality Labs 1** (Mixture of Layers), **Google 1** (CroissantMiner), **Microsoft Research Asia 1** (SafeBridge), **Datumo Inc. 1** (guard-model calibration). The CTR/ads/recsys lane is again thin — the most industrial-adjacent material lives in the §8 lane (ranking bandits, ad-lift 𝒶/𝒷 testing, ad-platform mechanism design).
- **The strongest cluster is *looped / recurrent language models* — 2 same-group papers** (ShanghaiTech + MSR Asia): **LoopOPD** makes the LoopLM's own frozen terminal loop a dynamically-refreshed compute-privileged teacher (recurrent self-improvement), and **SafeBridge** shows **jailbreak success grows at deeper recurrent depths** — SFT and preference alignment do *not* close the depth gaps, motivating depth-specific safety alignment. The pair reads as the answer to the wiki's looped-LM arc (§7.5/§7.6): *capability and safety both scale with loop depth, and both need dedicated post-training*.
- **A second dense cluster: on-policy distillation under a supervision budget** — **SR-OPD** uses a student's own successful rollout as the reference to pick failed rollouts for teacher tokens (**3.46–5.02%** of Vanilla OPD teacher cost, 6 maths benchmarks), **Pivot-SD** supervises only information-gain-maximizing "pivot" commitments in masked-diffusion LMs (LLaDA-8B-Instruct beats full-sequence SFT and budget-matched diffusion RL), and **OSPD** applies the same teacher/student-asymmetric-information trick to persona-consistent dialogue. The theme: *teacher signal is scarce — allocate it by what the student's own success/failure predicts, not uniformly*.
- **Numbers that anchor the window:** Teaching Agents to Code Reliably (Stanford+AWS) lifts SWE-bench Verified **pass@1 31.9→43.0%, pass@8→60.7%**, and cuts agent-steps to **48.1%** of an 8-sample baseline by scoring each patch against its reverted tree (**52.8%** resolve, verifier precision 26.8→41.7%, holds at 7B/14B/30B); **CRISP** cuts flying-pixel error (FSVD/FPVD) **50.5% avg** and FRID **71%** on the LiDAR-native LiDM backbone with a zero-shot decoder swap; **EDISCO** beats learned SOTA TSP/CVRP solvers on **33–50% of the training data**; **SlimKV** retains **>96%** of uncompressed score at 4×/8× KV compression with **3.38×** end-to-end decode speedup at 128K; **DP-ES** gets **88.1% GSM8K under ε≤1.0** (+38.6 pp over DP-OPT, ~9× lower std); **TreeWalker** (Shopify) is **2.5–3.2×** faster at the reference config and **6.8–7.8×** at G=128 grouped inference.
- **Calibration is the surprise cross-cutting theme** (4 papers): *Panel-relative posterior* LLM judging (BayesJudge), **guard models get order-of-magnitude worse calibration under adversarial attack while the base LM still hedges** (Datumo), the judge-proxy literature conflates close-gap-pair inconsistency with incompetence (Pair-Difficulty — recorded, §9), and CoT detectors' instability is **80% sampling stochasticity, not distribution shift** (SIFT — see §9).

---

## 1. NeurIPS 2026 — Main Track (11 papers)

### 1.1 Differentiable Systematic Resampling for Variational Sequential Monte Carlo
- **中文标题**: 面向变分序贯蒙特卡洛的可微系统性重采样（DSR）
- **Authors**: Fredrik Cumlin, Saikat Chatterjee
- **Affiliation**: KTH Royal Institute of Technology
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: Particle filters' resampling step is discrete → no gradient flow for variational SMC; existing differentiable resampling (optimal-transport-based) needs iterative solvers.
- **Key innovation**: **DSR** — a temperature-controlled relaxation of *systematic resampling* that keeps its CDF-ordered, banded structure; converges to exact systematic resampling as temperature→0 with a **proved pointwise exponential convergence rate** for the induced bias. Low computational overhead, no iterative solvers.
- **Results / comparison**: Brighter gradient geometry than OT-based resampling at substantially lower overhead; comparable/superior filtering and dynamics learning on stochastic dynamical systems + real-world handwriting data.
- **Link**: https://arxiv.org/abs/2610.12094

### 1.2 CRISP: Fixing Flying Pixels in Latent LiDAR Generation via Diffusion Decoding
- **中文标题**: CRISP：用扩散解码修复潜空间 LiDAR 生成中的"飞散像素"
- **Authors**: Andrea Ceron, Michael Schmidt, Alvaro Marcos-Ramiro, Sebastian Schmidt, Benjamin Busam
- **Affiliation**: TU München; **BMW AG**
- **Venue**: **NeurIPS 2026** (poster)
- **Problem background**: Latent LiDAR pipelines blur sharp radial depth discontinuities through convolutional VAEs → edge depths back-project to "flying pixels" floating between surfaces; identified as a *directly correctable decoder bottleneck*.
- **Key innovation**: **CRISP** — pixel-space diffusion decoder with a backbone-agnostic latent adapter, DiT denoiser, support-mask predictor; swaps only the decoder while encoder + latent generator stay frozen (works with video-VAE and LiDAR-native decoders).
- **Results / comparison**: Replacing just the decoder reduces **FSVD/FPVD by 50.5% avg** across frozen backbones (KITTI-360, SemanticKITTI, nuScenes); 71%/74% on generic video VAEs; **FRID −71%** on the LiDAR-native LiDM backbone with largest gains at depth discontinuities; zero-shot swap into a pretrained LiDM world model improves **FSVD 15.5%**, narrowing sim-to-real gap.
- **Link**: https://arxiv.org/abs/2610.11376

### 1.3 Diffusion Meta-Prompting and Steering for Generalizable Foundation Model Adaptation
- **中文标题**: 面向泛化基础模型适配的扩散元提示与引导（DMP）
- **Authors**: Deepak Sridhar, Yi Li, Kartikeya Bhardwaj, Shuangjun Liu, Taotao Jing, Yuan Li, Shuai Zhang, Jiancheng Lyu, Dashan Gao, Nuno Vasconcelos
- **Affiliation**: UC San Diego; **Qualcomm AI Research**
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: Learned prompts are task-specific and fail to generalize to new classes/domains/compositions; retrieval incurs storage + inference cost.
- **Key innovation**: **DMP** — a diffusion model over the *distribution of learned prompts*; trained/sampled **without the original task examples or task losses**, conditioned on natural-language task descriptions; test-time steering anchors sampling at the best training-selected prompt. Includes a theory bound on expected task loss of sampled prompts.
- **Results / comparison**: Storage/inference cost **−90%+ vs prompt retrieval**; composite classification up to **+2.0% avg (max +8.5% on Eurosat×Flowers)** over prior meta-learners across 55 dataset pairs; +2–9% hierarchical classification; improves classification, retrieval, text-to-image with concept composition + negative prompting without extra training.
- **Link**: https://arxiv.org/abs/2610.11067

### 1.4 BayesJudge: Uncertainty-Aware Bayesian Meta-Evaluation of Human and LLM Judgments
- **中文标题**: BayesJudge：人类与 LLM 判断的不确定性感知贝叶斯元评测
- **Authors**: Jiahao Zhang, Pengbin Feng, Chunlei Meng, Hang He, Tianyong Hao
- **Affiliation**: South China Normal University; University of Southern California; Fudan University; East China Normal University
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: Pairwise LLM evaluation produces *conflicting* verdicts (ambiguous items, underspecified rubrics, unstable raters, order-swap flip-flops) but pipelines collapse them into clean labels.
- **Key innovation**: **BayesJudge** — an online Bayesian meta-evaluation layer over conflicting human–LLM judge streams: panel-relative posterior over verdicts with explicit tie/ambiguity state, per-rater confusion matrices, and LLM presentation-order bias — via Rao-Blackwellized assumed-density SMC. Uses tie-open labels + paired order-swapped calls to separate quality from position bias.
- **Results / comparison**: Recovers prespecified evaluator parameters in controlled experiments; on SummEval detects systematic presentation-order effects in LLM judges and infers distinct expert vs crowdworker signatures *without rater metadata*; posterior uncertainty correlates with human disagreement.
- **Link**: https://arxiv.org/abs/2610.11116

### 1.5 Mixture of Layers: Dynamic Layer Routing for Visual Reasoning
- **中文标题**: 层混合（MoL）：面向视觉推理的动态层路由
- **Authors**: Jeonghwan Kim, Sofia Stoica, Jiwan Chung, Ansel Blume, Hyeonjeong Ha, Zhenhailong Wang, Xin Luna Dong, Heng Ji
- **Affiliation**: UIUC; Yonsei University; **Meta Reality Labs**
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: MLLMs use only final/penultimate vision-encoder representations or fixed aggregations → query-agnostic visual abstraction, missing fine-grained cues (small objects, text, spatial details).
- **Key innovation**: **MoL** — instruction-conditioned *layer routing at the visual-patch level*: predicts routing probabilities over vision-encoder layers, top-k sparse aggregation over selected hidden states (image-level, patch-level, or hybrid). No multi-resolution inputs, no extra encoders, no added patch tokens.
- **Results / comparison**: On 7 fine-grained visual reasoning tasks — **+18.9% on V\*, +4.5% HRBench4K, +16.3% CharXiv** vs baseline MLLMs; includes a receptive-field/sampling analysis explaining *why* conditional representations help.
- **Link**: https://arxiv.org/abs/2610.09440

### 1.6 LASER: Latent Space Adjoint Matching for Support-Constrained Entropy-Regularized Offline RL
- **中文标题**: LASER：支撑受限、熵正则化离线强化学习的潜空间伴随匹配
- **Authors**: Songyuan Zhang, Oswin So, Eric Yang Yu, Matthew Cleaveland, Peter Crowley-Dolen, Chuchu Fan
- **Affiliation**: MIT; MIT Lincoln Laboratory
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: Latent-space offline RL (flow-matching behavior clone + constrained latent policy) collapses into brittle modes or exploits sharp critic artifacts.
- **Key innovation**: **LASER** — shows entropy regularization is *essential* in latent-space RL; achieves entropy-regularized latent-space RL with expressive flow policies via **latent-space adjoint matching** that avoids backpropagation-through-time.
- **Results / comparison**: SOTA on **40 OGBench tasks** across dataset qualities with **fixed per-method hyperparameters** — outperforms baselines even when those are task/dataset-tuned, demonstrating robustness.
- **Link**: https://arxiv.org/abs/2610.08989

### 1.7 Decision-Focused Learning in MDPs: An Occupancy Measure Approach
- **中文标题**: 马尔可夫决策过程中的决策聚焦学习：占据测度方法
- **Authors**: Zihao Zhao, Ashwath K. Karunakaram, Ali Eshragh, Yuexing Li, Kai Wang
- **Affiliation**: Johns Hopkins Carey Business School; ICSI Berkeley
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: Decision-focused learning through MDP Bellman-KKT differentiates a linear system over *all* state-action pairs — not scalable, discontinuous gradients when active constraints change.
- **Key innovation**: Reformulates the MDP as an **occupancy-measure LP** induced by predicted dynamics, closed-form gradient from active constraints via pivoting; smooths jumps with augmented-Lagrangian surrogate + random row sketching, and scales to large/continuous state spaces with a learnable soft state-aggregation layer.
- **Results / comparison**: Lower regret than KKT-based DFL and two-stage baselines across tasks at significantly lower compute.
- **Link**: https://arxiv.org/abs/2610.08384

### 1.8 Best-of-N Guidance for Test-time Diffusion Alignment
- **中文标题**: 面向测试时扩散对齐的 Best-of-N 引导（BoNG）
- **Authors**: Richard Lee Kim, Yeongmin Kim, Gyuwon Sim, Taekyu Kim, Minsang Park, Il-chul Moon
- **Affiliation**: KAIST; summary.ai
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: Best-of-N sampling uses reward only at final selection, not along the trajectory → doesn't raise *average* alignment, single-output only.
- **Key innovation**: **BoNG** embeds BoN into the reverse process — online BoN over denoising particles, with asymmetric guidance *among* particles steering the population toward higher-reward regions during generation.
- **Results / comparison**: BoNG ranks best in **29/36 comparisons (80.56%)** vs SMC and Vanilla BoN; multi-output support with **1.3× ImageReward** and **1.6× speedup** vs the latest sample-based guidance.
- **Link**: https://arxiv.org/abs/2610.05108

### 1.9 EDISCO: Equivariant Discrete Diffusion for Euclidean Combinatorial Optimization
- **中文标题**: EDISCO：面向欧氏组合优化的等变离散扩散
- **Authors**: Ruogu Chen, Jie Han
- **Affiliation**: University of Alberta
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: Euclidean CO problems (TSP/CVRP) are symmetric under E(2); prior learning methods only *approximate* equivariance via augmentation/regularization.
- **Key innovation**: First discrete diffusion model with **exact E(2)-invariant generative distributions over node-index solutions** — an E(2)-equivariant edge-score network + categorical CTMC over discrete edge variables, exact posterior sampling for efficient multi-step inference.
- **Results / comparison**: Beats prior learned SOTA on synthetic **TSP 100–10,000 nodes** and **CVRP 50–2,000 customers** using **only 33–50% of the training instances**; strong under spatial-distribution and constraint-tightness shift.
- **Link**: https://arxiv.org/abs/2610.04953

### 1.10 TreeWalker: Partial Evaluation for Grouped Tree-Ensemble Inference
- **中文标题**: TreeWalker：分组树集成推理的偏求值
- **Authors**: Durmus Karatay, Richard Newman
- **Affiliation**: **Shopify**
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: Many workloads score row groups that share features (survival models per patient-step, **CTR models per search-session item**, scenario analysis); standard inference repeats shared work G times.
- **Key innovation**: **TreeWalker** applies partial evaluation to grouped inference — walks each tree once per group, partitions a row bitmask at varying splits, skips empty subtrees; reads standard LightGBM/XGBoost models, training unchanged. Proved per-row work → $(d_v+1)/(d+1)$ fraction of a row-independent walk as G→∞.
- **Results / comparison**: On Intel **2.5–3.2×** faster at the reference config and **6.8–7.8×** at G=128 on survival datasets; faster in all 16 scenario-analysis configs (both Intel/Arm); f32 numerics closer to a Kahan-compensated reference than native f32 on 99.98% of rows.
- **Link**: https://arxiv.org/abs/2610.03939

### 1.11 CANDO: Cooperative Agentic Network for Layout Design Optimization
- **中文标题**: CANDO：面向布局设计优化的协作式 Agent 网络（含 ALPS-Bench）
- **Authors**: Athanasios Masouris, Zheng Jing, Benjamin Sam Chandler, Hadi Jamali-Rad
- **Affiliation**: **Shell** Information Technology International; Shell China; TU Delft
- **Venue**: **NeurIPS 2026** (main)
- **Problem background**: Real-world facility layout needs irregular boundaries, orientations, access-awareness, motion-planning feasibility — existing generative benchmarks reward conformity (FID/IoU) on rectangular domains, discounting design innovation.
- **Key innovation**: **ALPS-Bench** (1,000 professionally annotated facility layouts, instance-specific scoring from a structured design manual) + **CANDO**, a training-free multi-agent framework with a verification-grounded refinement loop concentrating reasoning on strategic spatial decisions.
- **Results / comparison**: CANDO surpasses state-of-the-art trained and LLM baselines on **PubLayNet, RICO, PKU-PosterLayout** — cooperative agentic design becomes a broadly effective recipe for constraint-aware layout synthesis.
- **Link**: https://arxiv.org/abs/2610.10044

---

## 2. NeurIPS 2026 — Workshops & Datasets/Benchmarks Tracks (3 papers)

### 2.1 PatchBench: Measuring Collateral Damage in Activation Patching
- **中文标题**: PatchBench：衡量激活补丁的附带损伤
- **Authors**: Alexi Canesse, Mathis Le Bail, Maël Jenny, Clément Elliker, Mahammed El Sharkawy, Sonia Vanier
- **Affiliation**: LIX, École Polytechnique (IP Paris, CNRS); AMIAD (Agence Ministérielle pour l'IA de Défense)
- **Venue**: **NeurIPS 2026** (Datasets & Benchmarks Track)
- **Problem background**: A jailbreak "repair" can pass a benchmark yet over-refuse benign prompts sharing the harmful prompt's wording/structure — aggregate metrics can't separate selective repairs from broad suppression.
- **Key innovation**: **PatchBench** — 15,314 curated English prompts from 27,870 (37 public datasets), 400 high-confidence empirically observed jailbreak failures across 8 instruction-tuned models; **PatchBench-Local** protocol generates 3 families of local neighbours (harmful variants / matched-structure benign / reused-key-term benign) to test behavioural precision.
- **Results / comparison**: Global capability (MMLU) can stay flat while local benign regressions are severe — confirms aggregate metrics miss collateral damage in 4 steering methods.
- **Link**: https://arxiv.org/abs/2610.10276

### 2.2 CroissantMiner: Automated Extraction and Validation of Croissant Metadata for ML Datasets
- **中文标题**: CroissantMiner：ML 数据集 Croissant 元数据的自动化提取与校验
- **Authors**: Berke Arda, Ahmetcan Yavuz, Paul Gerry, Sebastian Lobentanzer, Nobin Sarwar, Joan Giner-Miguelez, Kongtao Chen, Luyao Zhang, Mrinmaya Sachan, Mubashara Akhtar
- **Affiliation**: ETH Zurich; CSAIL MIT; Helmholtz Zentrum München; UMBC; Barcelona Supercomputing Center; **Google**; Duke Kunshan University
- **Venue**: **NeurIPS 2026** (Datasets & Benchmarks Track / Evaluations)
- **Problem background**: Croissant dataset metadata is manual and labor-intensive.
- **Key innovation**: First end-to-end benchmark for schema-aligned metadata extraction — 602 papers (102 human-gold + 500 LLM-silver), full Croissant schema incl. Responsible-AI fields; two-tier evaluation (rule-based + human-audited LLM judge).
- **Results / comparison**: **Single-pass extraction beats all four agentic architectures** across backbones; largest gap on long-form RAI fields that require synthesis across the paper — current systems not yet reliable there.
- **Link**: https://arxiv.org/abs/2610.07132

### 2.3 On the Clock: Towards Punctual and Productive Time-Budgeted AI Agents
- **中文标题**: On the Clock：面向守时且高效的限时 AI Agents
- **Authors**: Aaron Wang, Neelabh Madan, Vlad Sobal, Matthew Trager, Michael Kleinman, Elman Mansimov, Wei Xia, Stefano Soatto
- **Affiliation**: University of Illinois at Chicago; New York University; **AWS**
- **Venue**: **NeurIPS 2026 Workshop on Resource-Aware Agentic AI**
- **Problem background**: Small agents mostly ignore wall-clock budgets stated in the prompt — no timing feedback, can't anticipate action durations, no time→strategy mapping.
- **Key innovation**: Two complementary intervention classes: harness-based timing feedback + deadline enforcement, and **RL with budget-aware rewards** (GRPO); evaluated on MLE-Bench Lite (Qwen3.6-27B) and Zork I (Qwen3-4B).
- **Results / comparison**: Harness timing info gives near-perfect budget adherence without measurable performance loss; RL hits near-perfect adherence on Zork I and generalizes to held-out budgets — but RL agents fill extra time with *repeated actions* and multi-budget GRPO collapses toward the shortest-budget policy. **Adherence ≠ productive use of time** remains open.
- **Link**: https://arxiv.org/abs/2610.10833

---

## 3. EMNLP 2026 (12 papers)

### 3.1 Is Memorization Context-Sensitive? Prefix-Based Extraction Beyond Isolated Prefixes
- **中文标题**: 记忆是否具有上下文敏感性？超越孤立前缀的前缀式提取
- **Authors**: Ali Satvaty, Narjes Sharafi, Jirui Qi, Suzan Verberne, Fatih Turkmen
- **Affiliation**: *(affiliation not recovered)*
- **Venue**: **EMNLP 2026** (main)
- **Problem background**: Prefix-based memorization extraction is usually tested in isolation, but deployment prefixes come with instructions / RAG context.
- **Key innovation**: Paired item-level suffix-extraction measurement — same prefix-suffix scored under empty vs retrieved contexts of varying relevance, across 3 open-weight instruction-tuned models.
- **Results / comparison**: Context doesn't erase memorization: extractable memory = a **context-robust core + context-sensitive boundary**; robustly extractable samples persist as prefix length grows, and context *enables new* extractions. Qualifies the "RAG reduces memorization" view.
- **Link**: https://arxiv.org/abs/2610.12085

### 3.2 From Prompts to Trees: Effective LLM-Guided Tree Generation for Few-Shot Tabular Classification
- **中文标题**: 从提示到树：面向少样本表格分类的高效 LLM 引导式树生成
- **Authors**: Yue Qiu, Zekang Du, Yiqun Diao, Bingsheng He, Qinbin Li
- **Affiliation**: National University of Singapore; Huazhong University of Science and Technology
- **Venue**: **EMNLP 2026** (main, **oral**)
- **Problem background**: LLMs on tabular data are costly and opaque; decision trees are fast/transparent but weak in low-data regimes.
- **Key innovation**: Three-stage distillation — prompt the LLM to generate rules, organize the rules into a tree (instead of unstable full-tree generation); interpretable few-shot classifier.
- **Results / comparison**: **Superior accuracy and interpretability with significantly lower prompting overhead** than existing baselines across real-world tabular datasets.
- **Link**: https://arxiv.org/abs/2610.10227

### 3.3 Goldsmith: Gold-Loss-Guided Definition Optimization with an Agentic Annotation Harness
- **中文标题**: Goldsmith：以金标损失引导的标注定义优化（基于 Agent 化标注框架）
- **Authors**: Yihan Li, Hanyi Zhang, Xiaoxi Jiang, Man Guo
- **Affiliation**: Sun Yat-sen University
- **Venue**: **EMNLP 2026** (main)
- **Problem background**: Annotation projects often start before stable guidelines or labels exist; definitions are hard to iterate when no model can be trained.
- **Key innovation**: Treats the annotation definition as a *trainable textual object* — candidate definitions scored on a small gold set by an executable structured loss; an LLM editor converts the highest-loss failures into "textual-gradient" revisions accepted only when measured loss decreases.
- **Results / comparison**: Beats direct rewriting, **OPRO, APE, PromptBreeder** under matched protocols; improves downstream annotation across typed-span, pair-relation, and event-argument tasks via retrieval + score-based routing + human review.
- **Link**: https://arxiv.org/abs/2610.09489

### 3.4 CoDe-LoRA: Mitigating the Orthogonality Dilemma in Continual Learning of LLMs
- **中文标题**: CoDe-LoRA：缓解 LLM 持续学习中的"正交性困境"
- **Authors**: Maoqi Liu, Quan Fang, Yufei He
- **Affiliation**: Beijing University of Posts and Telecommunications; National University of Singapore
- **Venue**: **EMNLP 2026** (main)
- **Problem background**: Replay-free orthogonal-projection LoRA (O-LoRA) isolates task parameters but blocks transfer/accumulation of shared representations across related tasks — the "orthogonality dilemma".
- **Key innovation**: **CoDe-LoRA** decouples learning into Consolidating Universal Knowledge + Decoupling Task-Specific Knowledge via an adaptive null-space projection and semantic routing.
- **Results / comparison**: Best average accuracy across **4 backbones × 3 continual-learning benchmarks**; code released.
- **Link**: https://arxiv.org/abs/2610.08312

### 3.5 MoF: Preference-Aware Mixture Modeling for Black-Box LLM Personalization
- **中文标题**: MoF：面向黑盒 LLM 个性化的偏好感知混合建模
- **Authors**: Hun Park
- **Affiliation**: Korea University
- **Venue**: **EMNLP 2026** (main)
- **Problem background**: Black-box personalization via per-user scoring heads grows parameters linearly with users and fails on unseen users.
- **Key innovation**: **Mixture-of-Facets (MoF)** models preferences as compositions of *shared latent preference facets*; history-conditioned routing over shared facet heads gives personalization for unseen users with **zero extra parameter updates**.
- **Results / comparison**: Stronger personalization than prior approaches with more scalable, parameter-efficient design; strong generalization to unseen users.
- **Link**: https://arxiv.org/abs/2610.08330

### 3.6 ThinkFuse: Trajectory-Aware Test-Time Fusion for Small Reasoning Models
- **中文标题**: ThinkFuse：面向小推理模型的轨迹感知测试时融合
- **Authors**: Myunghoon Kang, Jungseob Lee, Jaehyung Seo, Heuiseok Lim
- **Affiliation**: Korea University; Konkuk University; Human-inspired AI Research
- **Venue**: **EMNLP 2026** (Findings)
- **Problem background**: Small reasoning models can't recover once reasoning enters a wrong path; local-fusion triggers get misled by transient uncertainty fluctuations.
- **Key innovation**: **ThinkFuse** — training-free, trajectory-aware: compares *segment-level uncertainty shifts* with *trajectory-level trends* to detect unstable points, fuses auxiliary reasoning paths selectively.
- **Results / comparison**: Outperforms baselines on math + knowledge-intensive reasoning across model-family combinations; **fewer fusion triggers and fewer generated tokens** — efficiency of selective triggering.
- **Link**: https://arxiv.org/abs/2610.07803

### 3.7 Understanding and Enhancing Backdoor Persistency in LLM Agent Post-Training
- **中文标题**: 理解并增强 LLM Agent 后训练中的后门持久性
- **Authors**: Qiusi Zhan, Nian Lyu, Stephanie Ding, Arnav Mehta, Chris Canal, Connor Tabarrok, Xander Davies, Daniel Kang
- **Affiliation**: UIUC; MATS Research; Measuring AI Progress; EquiStamp; University of Oxford (OATML)
- **Venue**: **EMNLP 2026** (Findings)
- **Problem background**: Supply-chain threat — a backdoored third-party model survives the developer's benign SFT then task-level RL (software-engineering agents).
- **Key innovation**: Factor analysis (initial backdoor strength + gradient compatibility with benign training) + **PersistBD**, which refines an already-backdoored model to improve persistence through benign post-training.
- **Results / comparison**: On Qwen2.5-Coder-7B, PersistBD raises attack success **20→74% after SFT and 20→76% after SFT+RL** with comparable benign-task performance → backdoors stay active through benign post-training.
- **Link**: https://arxiv.org/abs/2610.07510

### 3.8 DP-ES: Differentially Private Evolution Strategies for Prompt Optimization
- **中文标题**: DP-ES：用于提示优化的差分隐私进化策略
- **Authors**: Ziniu Liu, Aiping Li, Yue Han, Han Yu, Junjian Zhang, Dong Zhu, Changjian Li, Shiqiang Zhang
- **Affiliation**: National University of Defense Technology; CRRC Zhuzhou Institute; China Academy of Railway Sciences
- **Venue**: **EMNLP 2026** (main)
- **Problem background**: Token-level DP prompt optimization (DP-OPT) is unstable under tight privacy budgets (GSM8K 49.5±28.5% across 30 runs).
- **Key innovation**: **DP-ES** — maintains a *population* of full prompts, mutations via LLM calls that never touch the private dataset, privacy spent only on sampled-Gaussian evaluation; deterministic/Gumbel-smoothed selection as post-processing. Formal guarantee **ε≤1.0, δ=10⁻⁵**.
- **Results / comparison**: **88.1% GSM8K (+38.6 pp over DP-OPT, ~9× lower std)**, 99.7% MedQA, 73.5% BANKING77, 86.8% Alpaca; **2.5× faster wall-clock, 3.3× fewer private-data call groups**.
- **Link**: https://arxiv.org/abs/2610.06236

### 3.9 Pivot-SD: Efficient Self-Distillation for Masked Diffusion Language Models
- **中文标题**: Pivot-SD：掩码扩散语言模型的高效自蒸馏
- **Authors**: Seo Hyun Kim, Sunwoo Hong, Younwoo Choi, Chen-Hao Chao, Se-Young Yun, Rahul G. Krishnan
- **Affiliation**: KAIST AI; University of Toronto & Vector Institute
- **Venue**: **EMNLP 2026** (main, **oral**)
- **Problem background**: Masked diffusion LMs (dLMs) give a parallel alternative to AR models but have a distinct credit-assignment problem: a *few commitments* during denoising shape most of the response — yet post-training trains all tokens or whole-step rewards.
- **Key innovation**: **Pivot-SD** — offline self-distillation supervising only high-impact "pivot" commitments, selected by an information-gain metric (uncertainty reduction over remaining masked positions); successful pivots get cross-entropy, failed pivots targeted unlikelihood.
- **Results / comparison**: With only **200 questions × 4 rollouts**, improves LLaDA-8B-Instruct over full-sequence SFT *and* budget-matched diffusion RL baselines on math + code.
- **Link**: https://arxiv.org/abs/2610.03665

### 3.10 SlimKV: Joint Token-Feature KV Cache Compression with Reconstruction-Free Beacon Attention
- **中文标题**: SlimKV：基于免重建 Beacon Attention 的 token-特征联合 KV 缓存压缩
- **Authors**: Zihan Teng, Jiayu Zhao, Wentao Ren, Minhao Fan, Tianrui Ma, Song Chen, Weichen Liu
- **Affiliation**: USTC; Nanyang Technological University; **Tencent**
- **Venue**: **EMNLP 2026** (main, **oral**)
- **Problem background**: Long-context serving is KV-bound; token-wise compression risks information loss, feature-wise compression needs full-dim reconstruction for positional embedding (limits decode speedup).
- **Key innovation**: Question-agnostic **joint token-feature compression** into "beacon" memory states (low-rank-aware training, layer-adaptive rank allocation) exploiting a positional asymmetry: removing key-side RoPE damages beacon tokens much less than raw tokens → K-RoPE-free beacon projections enable **latent-space attention without reconstruction**.
- **Results / comparison**: On LongBench beats baselines at 16×/32× and still leads at 4×/8× (**>96% of uncompressed score**); up to **7.34× attention and 3.38× end-to-end decode speedup** at 128K; NiH robust across positions.
- **Link**: https://arxiv.org/abs/2610.02953

### 3.11 Guard Models Are Overconfident Where Base Models Are Uncertain
- **中文标题**: 基础模型不确定之处，守卫模型却过度自信
- **Authors**: Jonghyun Hong, MinJae Jung, Minwoo Kim
- **Affiliation**: **Datumo Inc.**
- **Venue**: **EMNLP 2026** (Findings)
- **Problem background**: Guard/classifier safety models' confidence drives moderation; adversarial attacks can turn false negatives into high-confidence errors — but are guard models calibrated under attack?
- **Key innovation**: Evaluates 5 guard models for prompt classification; layer-wise analysis localizes guard–base divergence to later layers (sharper safe/unsafe separation, lower-rank reps near the clean-safe region).
- **Results / comparison**: Though nearly calibrated on clean inputs, adversarial attacks degrade calibration **by an order of magnitude** while the base LM still expresses uncertainty on the same inputs — a guard-confidence ≠ base-uncertainty mismatch.
- **Link**: https://arxiv.org/abs/2609.36477

### 3.12 OSPD: On-Policy Self-Distillation for Persona-Consistent Dialogue
- **中文标题**: OSPD：面向人设一致对话的在策略自蒸馏
- **Authors**: Rui Xu, Yikai Zhang, Aili Chen, Zicheng Zhao, Xu Yinghui, Libo Wu
- **Affiliation**: Fudan University; Shanghai Innovation Institute
- **Venue**: **EMNLP 2026** (main)
- **Problem background**: Persona-consistent role-play: off-policy distillation mismatches compound across turns; RL faces subjective reward ambiguity.
- **Key innovation**: **OSPD** — same model as teacher and student under asymmetric information (teacher: full profile; student: brief summary), student rolls out its own policy; **role-aware divergence switching** matches the bimodal structure of teacher confidence (peaked at character-critical tokens), plus a progressive trait-masking curriculum.
- **Results / comparison**: Substantially improves persona consistency over SFT and multi-turn RL baselines on CharacterBench, CharacterEval, SocialBench — no external teacher or reward model.
- **Link**: https://arxiv.org/abs/2609.34418

---

## 4. ICML 2026 (4 papers, incl. 1 workshop)

### 4.1 ZeroDiff: Zero-Shot Time Series Reconstruction via Informed-Prior Diffusion
- **中文标题**: ZeroDiff：基于信息先验扩散的零样本时间序列重建
- **Authors**: Yingda Fan, Dan Lu, Xiaowei Jia
- **Affiliation**: University of Pittsburgh; Oak Ridge National Laboratory
- **Venue**: **ICML 2026** (main)
- **Problem background**: Zero-shot time series reconstruction — infer targets at locations where measurements never existed from exogenous inputs; naive direct mapping produces over-smooth outputs that underestimate extremes.
- **Key innovation**: **ZeroDiff** builds an informed prior from exogenous variables alone, then learns to calibrate reconstruction errors through diffusion (train on observed locations, generalize to unobserved).
- **Results / comparison**: Significant improvements over existing approaches across diverse real-world datasets.
- **Link**: https://arxiv.org/abs/2609.37078

### 4.2 ConEx: Human-Interpretable Saliency Maps via Concept-Aware Attribution
- **中文标题**: ConEx：基于概念感知归因的可解释显著性图
- **Authors**: Yehonatan Elisha, Oren Barkan, Ziv Weiss Haddad, Noam Koenigstein
- **Affiliation**: Tel Aviv University; The Open University
- **Venue**: **ICML 2026** (main)
- **Problem background**: Pixel-level saliency can't link low-level cues to semantic concepts; learned concepts often carry segmentation-mask noise.
- **Key innovation**: **ConEx** — automatic class-specific concept discovery via concept activation vectors with an architecture-specific masking mechanism (concept purity), concept-aware saliency maps, plus **VCM/CCM** metrics for concept alignment.
- **Results / comparison**: SOTA on faithfulness, segmentation, and concept-quality benchmarks across diverse settings.
- **Link**: https://arxiv.org/abs/2610.04605

### 4.3 Ariadne's Thread of LipSync: Unraveling Forgeries via Inconsistency between Lip Motions and Head Poses
- **中文标题**: LipSync 的阿里阿德涅之线：通过唇动与头部姿态不一致识别伪造视频（LipDA）
- **Authors**: Tianyi She, Jiawei Liu, Weifeng Liu, Hanqing Zhao, Weiming Zhang, Kejiang Chen
- **Affiliation**: USTC; Shanghai Jiao Tong University; Peking University; Nanyang Technological University
- **Venue**: **ICML 2026** (main)
- **Problem background**: Modern LipSync generators both sync well *and* remove visual artifacts — defences that rely on artifacts fail; ignores the biological coupling of lip movement and head pose.
- **Key innovation**: **LipDA** — joint LipSync detection + model attribution via head-lip inconsistency; attribution fingerprints per-model temporal/AV-sync dynamics; new large-scale multi-generator **LipSync-A** dataset.
- **Results / comparison**: **>97% AUC detection, 97.5% attribution accuracy**, significantly outperforming existing methods.
- **Link**: https://arxiv.org/abs/2610.08417

### 4.4 FLIP: Final Layer Inference-Time Probing for Vision-Language Models
- **中文标题**: FLIP：视觉-语言模型的末层推理时探针
- **Authors**: Drandreb Earl O. Juanico, Rowel O. Atienza
- **Affiliation**: *(affiliation not recovered)*
- **Venue**: **ICML 2026 Workshop on Mechanistic Interpretability**
- **Problem background**: Behavioral change under internal intervention is mechanistically ambiguous (better visual evidence vs generic instability vs degradation).
- **Key innovation**: **FLIP** — elementwise floor the final normalized hidden state before logit computation (params/prompts/decoding untouched); a four-criterion probe-and-sweep protocol (regime structure, grounding-proxy alignment, feature-coherence dependence, negative control) disciplines the interpretation.
- **Results / comparison**: Final-site flooring satisfies the full protocol and reproduces across operators/VLMs; raw decoder-layer interventions and singleton-pair controls fail — FLIP is a validation step, not a steering method.
- **Link**: https://arxiv.org/abs/2609.30993

---

## 5. ICLR 2026 (1 paper)

### 5.1 PointLearner: Point-Focused Attention Meets Context-Scan State Space — Robust Biological Visual Perception for Point Cloud Representation
- **中文标题**: 焦点注意遇见上下文扫描状态空间：强鲁棒的仿生视觉点云表示（PointLearner）
- **Authors**: Kanglin Qu, Pan Gao, Qun Dai, Yuanhao Sun
- **Affiliation**: Nanjing University of Aeronautics and Astronautics
- **Venue**: **ICLR 2026** (accepted; comment: "Accepted by ICLR'26")
- **Problem background**: Point-cloud learning needs simultaneous local structure + global context; prior methods trade one for the other.
- **Key innovation**: Biomimetic foveation processing — **point-focused attention** (competitive normalized attention between local neighbours and inducing-point-downsampled features) + **context-scan state space** (saccade-like scan path guided by a Hilbert curve over bidirectional S6).
- **Results / comparison**: Remarkable robustness and SOTA across multiple point-cloud tasks — a focus-then-context design aligned with biological vision.
- **Link**: https://arxiv.org/abs/2610.11342

---

## 6. CIKM 2026 (2 papers)

### 6.1 Ontology Concept Overlap as a Training Signal: Knowledge-Grounded RL for Clinical Question Answering
- **中文标题**: 以本体概念重叠作为训练信号：面向临床问答的知识锚定强化学习
- **Authors**: Aditya Tanna, Abhishek Jindal
- **Affiliation**: *(affiliation not recovered)*
- **Venue**: **CIKM 2026** (main)
- **Problem background**: Clinical QA fits neither RLHF/DPO (human preference) nor RLVR (binary verifier) — near-correct answers differ by one substituted entity, no executable check of clinical correctness.
- **Key innovation**: Soft verifier from UMLS Concept-Identifier overlap (scispaCy set-level F1, computed with no model in the loop) inside **GRPO**, fused with an entropy-normalised LLM judge (safety/evidence axes) + small consistency penalty.
- **Results / comparison**: Over SFT on Phi-3-mini 3.8B: **+2.9% EM (+39% Token-F1)** on MedQA; Llama-3.2-3B: **+14% EM (+35% Token-F1)**; transfers to PubMedQA; ablation attributes 3 EM pts to the ontology term; 3 negative results (DPO w/ random negatives ≤ SFT, PPO w/ sparse neural reward diverges, GRPO-KL collapses at 7B).
- **Link**: https://arxiv.org/abs/2610.06360

### 6.2 Mitigating Convergence Collapse in Fixed-Target Anomaly Detectors via Kernel-Anchored Locality Regularization
- **中文标题**: 通过核锚定局部性正则化缓解固定目标异常检测器的收敛坍缩
- **Authors**: José Lucas De Melo Costa, Fabrice Popineau, Arpad Rimmel, Bich-Liên Doan
- **Affiliation**: *(affiliation not recovered)*
- **Venue**: **CIKM 2026** (main, **oral**)
- **Problem background**: Fixed-target neural anomaly detectors (contraction matching, one-step rectified flow, reconstruction AEs) suffer *convergence collapse*: at convergence the map tracks the target even off-distribution, so residuals vanish on anomalies too.
- **Key innovation**: Formalizes the structural diagnosis — fixed-target detectors need a *locality constraint*; the kernel-regression analog is a finite-bandwidth **Nadaraya-Watson smoother ("Kernel Contraction Matching", KCM**, closed-form, training-free) and the fix is **Kernel-Anchored Regularizer (KAR)**, penalizing deviation from a kernel-weighted average of training targets.
- **Results / comparison**: KCM matches established neural baselines on ADBench while CPU-cheap; KAR mitigates collapse and improves AUROC under prolonged training across collapse-prone ADBench datasets and three backbones.
- **Link**: https://arxiv.org/abs/2610.02345

---

## 7. AAAI 2026 (1 paper)

### 7.1 Learning the Latent Structure: A Feature-Centric Approach to Graph Data Augmentation
- **中文标题**: 学习潜在结构：以特征为中心的图数据增强方法（SelfAug）
- **Authors**: Yu Song, Zhigang Hua, Yan Xie, Bingheng Li, Jingzhe Liu, Bo Long, Jiliang Tang, Hui Liu
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **AAAI 2026** (main)
- **Problem background**: Real-world graphs are incomplete; existing Graph Data Augmentation is label-dependent, expensive, transductive.
- **Key innovation**: **SelfAug** — feature-centric augmentation operating in embedding space: a self-supervised inverse-masking process captures latent ties between observed and complete graphs; message regularizer + bootstrap for noisy/sparse supervision.
- **Results / comparison**: Consistently beats SOTA in accuracy and efficiency across 10 graph datasets in inductive and cold-start settings — scalable, generalizable graph learning.
- **Link**: https://arxiv.org/abs/2610.02517

---

## 8. ICLR 2027 — Under Review (7 papers)

### 8.1 Teaching Agents to Code Reliably
- **中文标题**: 教 Agent 可靠地编写代码
- **Authors**: Muhammad Ahmed Mohsin, Myeongsoo Kim, Kangrui Ruan, Shweta Garg, Varun Kumar, Murali Krishna Ramanathan
- **Affiliation**: Stanford University; **AWS AI Labs**
- **Venue**: **ICLR 2027** (submission)
- **Problem background**: Extra inference-time compute pays only when it yields a useful repair + reliable evidence; three *teachable* behaviors govern — location diversity, edit diversity, verifier quality.
- **Key innovation**: Directing search by execution feedback + **scoring each patch against its own reverted tree** (verification misleads when the agent writes its own tests); then moves the behaviors into the policy via weighted SFT + an RL objective that trains the verifier against gold-labeled repairs/incorrect variants.
- **Results / comparison**: **52.8% SWE-bench Verified using 48.1% of the agent-steps** of an 8-sample baseline; pass@1 **31.9→35.2 (SFT)→43.0% (RL)**, pass@8 **46.7→51.1→60.7%**; verifier precision 26.8→41.7% with false acceptance more than halved; gains hold at 7B/14B/30B and on 2/3 OOD suites.
- **Link**: https://arxiv.org/abs/2610.03984

### 8.2 COUNTERMEM: World-Model Verified Counter-Factual Memory for Language Agents
- **中文标题**: COUNTERMEM：语言 Agent 的世界模型校验反事实记忆
- **Authors**: Hongji Pu, Ruixiang Tang, Yongfeng Zhang
- **Affiliation**: *(affiliation not recovered)*
- **Venue**: **ICLR 2027**
- **Problem background**: Agent memory is built from factual interaction only — never asks "what if a different action had been taken".
- **Key innovation**: **COUNTERMEM** — RL framework for verified counterfactual memory: after a failed action, evaluates local alternatives via executable world models (tests, proof checkers, solvers); stores *original vs corrected action + checked outcomes + reuse conditions*; a learned memory-use policy decides retrieve vs skip while the base LLM stays frozen.
- **Results / comparison**: With gpt-oss-120b, beats **ReAct and Reflexion on all 12 benchmarks across 6 domains (+12.6 pp avg)**; task-run tokens **−7.7–42.0%**; removing verification or persistence weakens gains.
- **Link**: https://arxiv.org/abs/2609.31874

### 8.3 State Trace Rationale As Auxiliary Task in Reinforcement Learning
- **中文标题**: 状态轨迹文本描述作为强化学习的辅助任务（STRAT）
- **Authors**: Muhammad U. Nasir, Alex Vogt, Steven D. James, Julian Togelius
- **Affiliation**: University of the Witwatersrand; New York University
- **Venue**: **ICLR 2027** (submission)
- **Problem background**: RL agents lack readable, compressible internal state; sparse rewards stall learning.
- **Key innovation**: **STRAT** — auxiliary head predicts a short textual trace of the agent's own state (landmark/route/survey knowledge: position, inventory, goals, progress), generated online by environment rules with no human labelling.
- **Results / comparison**: Across 60 sparse-reward XLand-MiniGrid tasks, STRAT solves environments where standard RL fails outright, compacts state representations, prevents rank collapse — and yields a free readable account of agent beliefs per step.
- **Link**: https://arxiv.org/abs/2609.36867

### 8.4 Spend Teacher Tokens Where They Matter: Success-Referenced On-Policy Distillation
- **中文标题**: 把教师 token 花在刀刃上：成功参照的在策略蒸馏（SR-OPD）
- **Authors**: Xiang Chen, Futao Su, Kong Wang, Jiayi Chen, TanLin Li
- **Affiliation**: Tongji University; Shanghai Jiao Tong University; Hunan University
- **Venue**: **ICLR 2027** (submission)
- **Problem background**: On-policy distillation supervises every student rollout with dense teacher tokens — expensive.
- **Key innovation**: **SR-OPD** — focuses teacher supervision on prompts where the student produced *both* successful and failed rollouts, prioritizing failed rollouts whose hidden-state trajectories diverge from the successful reference (cost-aware).
- **Results / comparison**: **3.46–5.02% of Vanilla OPD teacher-input tokens** (one-pass) with comparable reasoning accuracy across 3 teacher-student pairs × 6 math benchmarks; controlled 5%-budget experiments validate both design choices.
- **Link**: https://arxiv.org/abs/2610.02678

### 8.5 Recurrent Self-Improvement: Dynamic Cross-Loop On-Policy Distillation for Looped Language Models
- **中文标题**: 循环自改进：循环语言模型的动态跨循环在策略蒸馏（LoopOPD / D-LoopOPD）
- **Authors**: Yi Wang, Rui Qian, Yu Li, Haoyang Yao, Wenjie Wang
- **Affiliation**: ShanghaiTech University; Fudan University; Southeast University; Peking University
- **Venue**: **ICLR 2027** (submission)
- **Problem background**: LoopLMs reuse shared parameters across recurrent steps (parameter-efficient reasoning scaling) but post-training them is hard — rewards are sparse across loops, external teachers create context mismatch.
- **Key innovation**: **LoopOPD** uses the LoopLM's own *frozen terminal loop* as a compute-privileged teacher for an intermediate-loop student on student rollouts (no external teacher); **D-LoopOPD** continually refreshes the terminal teacher as parameters update → recurrent self-improvement. Includes propagation analysis + sufficient conditions for simultaneous local improvement at both loop depths.
- **Results / comparison**: Improves mathematical reasoning on Ouro-Thinking models; further gains from dynamic teacher refresh; transfer to general reasoning + code benchmarks despite math-only training.
- **Link**: https://arxiv.org/abs/2610.10623

### 8.6 Safe at One Loop, Risky at Another: Aligning Safety Across Recurrent Depths in Looped Language Models
- **中文标题**: 某一循环安全、另一循环危险：循环语言模型跨循环深度对齐安全性（SafeBridge）
- **Authors**: Yi Wang, Xiuyuan Qi, Dongqi Han, Dongsheng Li, Wenjie Wang
- **Affiliation**: ShanghaiTech University; **Microsoft Research Asia**
- **Venue**: **ICLR 2027** (submission)
- **Problem background**: A LoopLM exposes a broader output space *across recurrent depths*, each readable independently — is safety preserved throughout?
- **Key innovation**: Systematic jailbreak evaluation targeting different loop depths reveals attack success **increases at deeper depths**, same query behaves differently across depths, and attacks transfer between depths — and SFT/preference alignment do *not* close the gaps. **SafeBridge**: depth-specific control of shared recurrent layers + selective state bridging + joint safety supervision across depths.
- **Results / comparison**: Substantially reduces attack success for both matched-depth and cross-depth attacks across scales/attack methods/safety benchmarks, while improving general utility and keeping over-refusal comparable.
- **Link**: https://arxiv.org/abs/2610.10625

### 8.7 CEO Arena: Evaluating Long-Horizon Multi-Agent Decision-Making in Competitive Markets
- **中文标题**: CEO Arena：竞争市场中长周期多智能体决策评测
- **Authors**: An Yan, Yu Huo, Zhiwei Shang, Yiran Peng, Chenglin Wu
- **Affiliation**: *(affiliation not recovered)*
- **Venue**: **ICLR 2027** (submission)
- **Problem background**: Long-horizon agent competition under uncertainty needs matched-replacement evaluation to separate agent quality from market effects.
- **Key innovation**: **CEO Arena** — 8 companies × 500 simulated days, sequential pricing/procurement/marketing/R&D/service decisions under private information, noisy signals, delayed feedback; each CEO agent compared to a reference policy in the same company under the same economic seed.
- **Results / comparison**: 8 LLM CEOs in 27 main + 26 robustness runs — most have **negative mean returns, private gains can accompany market losses**; demand capture and rivals' pricing/spending responses emerge as candidate mechanisms.
- **Link**: https://arxiv.org/abs/2609.34821

---

## 9. RecSys / Ads / CTR / Personalization Lane (4 papers)

> ⚠️ **Lane disclosure (as in both today's siblings):** the fresh announcement window (2026-10-01 → 2026-10-08) again contains **essentially no direct CTR-prediction or ad-serving papers** — `abs`-level sweeps for "click-through rate", "CTR prediction", "advertising", "ad auction", "sponsored search", "sequential recommendation", "generative recommendation" surface adjacent material (ranking, memory, mechanism design) but no new architecture entrants for [[ctr-scaling-landscape]]. The 4 papers below are the closest material; three carry **no venue tag** (preprints).

### 9.1 Ranking Bandits for Carousel Interfaces with Observable Browsing Depth
- **中文标题**: 可观测浏览深度的轮播界面排名 Bandit
- **Authors**: Takuma Yasuda, Atsuyoshi Nakamura
- **Affiliation**: Hokkaido University
- **Venue**: (no venue tag — recent arXiv preprint)
- **Problem background**: Carousel interfaces reveal how far a user browsed — a signal that distinguishes *displayed-but-unclicked* from *never-displayed*, which standard cascade/position-based ranking bandits treat as latent.
- **Key innovation**: Ranking-bandit formulation with observable max browsing depth + click feedback up to that depth; **UCB, Thompson Sampling, DMED** variants updating statistics only from observed exposures; instance-dependent logarithmic UCB bound + asymptotic-optimal DMED bound (coincides with lower bound as α↓0).
- **Results / comparison**: In synthetic shallow/deep environments and RecGaze-parameterized experiments, **OD-TS matches PBM-TS's final mean regret** while UCB/DMED variants beat PBM-UCB — directly actionable for carousel product surfaces (recommendation adjacency).
- **Link**: https://arxiv.org/abs/2610.05220

### 9.2 Pseudo-Incrementality Testing: Measuring Advertising Lift from Naturally Occurring Interventions
- **中文标题**: 伪增量测试：从自然发生的干预中度量广告增量
- **Authors**: Georgios Filippou, Boi Mai Quach, Ashish Kumar Jha
- **Affiliation**: *(affiliation not recovered)*
- **Venue**: (no venue tag — recent arXiv preprint)
- **Problem background**: Randomized geo experiments are unavailable to many advertisers; they still generate abrupt budget-cut / launch / pause events.
- **Key innovation**: Two-stage quasi-experiment — **Bayesian run-length inference** discovers/dates interventions on marketing-activity series, then variance-constrained **structural time-series counterfactual** with simulation-based inference, 5 qualification conditions, closed-form power bound.
- **Results / comparison**: On Meta's two GeoLift experimental benchmarks: intervention day found **exactly**; lift recovered within **6.2%** on the removal experiment (ROI 1.50 vs 1.60); only method of six estimators that needs **no geographic panel** and yields correct + narrow intervals on both experiments.
- **Link**: https://arxiv.org/abs/2609.18257

### 9.3 Mechanism Design for Ad-Supported Platforms
- **中文标题**: 广告支撑平台的机制设计
- **Authors**: Shota Ichihashi, Doh-Shin Jeon, Byung-Cheol Kim
- **Affiliation**: *(affiliation not recovered)*
- **Venue**: (no venue tag — economics preprint, 96 pp incl. appendix; JEL D42/D82/L15/O31)
- **Problem background**: Platforms selling content access + advertising face an intrinsic trade-off: ads generate revenue but impose nuisance that alters information rents.
- **Key innovation**: Monopoly screening across heterogeneous content/ads/consumers — optimal mechanism balances ad revenue vs rent extraction; expanding access raises ad revenue but *reduces* sales revenue by raising information rents.
- **Results / comparison**: Novel distortions in content access and ad exposure; **rationalizes observed contracts across ad-supported platforms and explains why greater ad profitability can weaken content-quality incentives** — a structural model directly relevant to the ad-platform economics arc.
- **Link**: https://arxiv.org/abs/2609.12870

### 9.4 CUE-Mem: Benchmarking Long-Term User Memory via Implicit Cues in Multimodal Conversations
- **中文标题**: CUE-Mem：通过多模态对话中的隐式线索评测长期用户记忆
- **Authors**: Yulin Hu, Yanyan Zhao, Zimo Long, Xing Fu, Mengtong Ji, Weixiang Zhao, Yutai Hou, Qianchao Wang, Dandan Tu
- **Affiliation**: *(affiliation not recovered)*
- **Venue**: submitted to **AAAI 2027** (recent preprint)
- **Problem background**: User memories are often *implied* (recurring background objects, ambient audio) but benchmarks are text-only or explicit-evidence.
- **Key innovation**: **CUE-Mem** — text-image-audio benchmark, 2,674 questions across explicit/implicit settings, 4 tasks (Entity Recall, Long Pattern, Personalized Recommendation, Answer Refusal).
- **Results / comparison**: Textualized memory systems sit **far below oracle evidence (implicit lane)** — the bottleneck is preserving/retrieving subtle cues, not answerability; richer captions recover some evidence but inflate token cost; native multimodal access helps only with strong backbones, and multimodal indexing adds retrieval noise.
- **Link**: https://arxiv.org/abs/2609.32574

---

## 10. Empty Lanes & Collision Notes

- **Empty this window:** ACL 2026, EMNLP 2025, NeurIPS 2025, KDD 2026, SIGIR 2026, WWW 2026, RecSys 2025, CVPR 2026 produced **no new venue-tagged entries** in the frozen 2026-10-01→2026-10-08 block (their recent proceedings were covered in the 2026-09/07 digests). The conventional "CTR-prediction architecture" lane again has no entrant — see §9 note.
- **Clusters consciously *not* featured** (available for later ingestion if desired): the formalization/spec-gen papers (**2610.10604** SpecGen eval; **2610.12030** NL→FOL autoformalization survey), the judge-proxy re-analysis **2609.37577** Pair-Difficulty, the CoT-distribution-shift audit **2610.04594** SIFT (its main finding — 80% of detector instability is sampling stochasticity — is referenced in §0), the code-environment reproducibility study **2610.00425** REXRepro, the security/prompt-harness **2609.35873**, and the story-video agent **2609.33627** StoryEngine.
- **Collision bookkeeping:** dedup baseline **8,567 claimed arXiv IDs** (built *after* today's `arxiv-ai-search` 44 and `arxiv-daily` 49 committed); all **45 IDs `rg -l` 0-hit** immediately before write; 0 sibling overlaps by construction. Acronym collisions: none found.
- **Same-window siblings for cross-reading:** [[arxiv-ai-search]] (44 papers, `2610.12114` UTT textual-KD → `2610.12325` LLM neural-operator), [[arxiv-daily]] (49 papers, `2610.11253` LLM-IDEA → `2610.05817` Nash-decodable LLM).

---

## 11. Follow-ups

1. **Looped-LM post-training (LoopOPD + SafeBridge) is the new frontier**: capability and safety are both *depth-indexed*. Before the next digest, consider a synthesis page [[looped-llm-posttraining]] tying together recurring-depth capability scaling (§8.5), depth-graded safety (§8.6), and this wiki's earlier HLA/SanSi/Recurrent-Looped-Transformer findings (arxiv-paper-check 2026-10-07).
2. **Calibration trio worth a comparison page**: BayesJudge (panel-relative posterior judging, NeurIPS 2026), Datumo guard-model overconfidence (EMNLP 2026 Findings), and SIFT's "detector instability is variance, not shift" claim — a [[calibration-of-evaluators]] page could consolidate the "who audits the auditor" arc.
3. **Distillation-under-budget is now 4-strong this calendar run** (SR-OPD, Pivot-SD, OSPD, LoopOPD) — candidate for a synthesis page on teacher-signal allocation.
4. **Recsys/ads lane continuity**: the ranking-bandit carousel paper (§9.1) and pseudo-incrementality 𝒶/𝒷 (β) lift method (§9.2) are both deploy-ready; flag for the next industry heavy digest where CTR-architecture entrants remain scarce.