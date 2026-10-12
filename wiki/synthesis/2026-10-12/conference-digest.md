---
title: "Conference & arXiv Digest — 2026-10-12 (NeurIPS 2026 / EMNLP 2026 / ICLR 2027-under-review / ICML 2026 / CIKM 2026 / ACL 2026 / AAAI 2026 / SIGMOD-ICDE / CVPR 2026 / RecSys-Ads lane)"
type: synthesis
created: 2026-10-12
updated: 2026-10-12
sources: [arxiv-export-api, arxiv-html, conference-announcements]
tags: [conference-digest, NeurIPS2026, EMNLP2026, ICLR2027, ICML2026, CIKM2026, ACL2026, AAAI2026, SIGMOD2027, CVPR2026, agents, LLM, diffusion, flow-matching, information-bottleneck, distillation, graph-diffusion, offline-RL, reinforcement-learning, KV-cache, quantization, model-editing, safety, unlearning, clinical-EHR, finance, recommendation, ads, CTR, online-bidding, evaluation, benchmark-validity, genomics, EEG, daily-digest]
---

# Conference & arXiv Digest — 2026-10-12

> **Scope.** Papers carrying a *verified* venue tag from **NeurIPS 2026, EMNLP 2026, ICML 2026, CIKM 2026, ACL/NAACL 2026, AAAI 2026, CVPR 2026, SIGMOD/ICDE**, plus **ICLR 2027 (under review)** preprints and the wiki's recsys/advertising/CTR lane. **60 papers featured**, organized by venue, then category. The run is **collision-managed against today's three siblings** — `arxiv-daily` (50), `arxiv-paper-check` (17), and `tech-report-digest` — whose IDs are already excluded by the dedup baseline (§0).

**Method (for reproducibility).** Harvest via the **arXiv export API** (`export.arxiv.org/api/query`, Atom XML) in two passes: **(1)** 17 venue `co:`/`comment:` sweeps (pull the newest ~100 matching each tag, so 2026 acceptances surface regardless of submission date), 9 category sweeps bounded to `submittedDate:[20261001 … 20261010]`, and 21 topical `all:` queries (recommendation, click-through rate, advertising, ad auction, CTR prediction, ranking, retrieval, agent, world model, game playing, reasoning, RL, diffusion model, sequential recommendation, code execution, benchmark, generative recommendation, LLM, user modeling, conversion rate, sponsored search, multi-agent); **(2)** 17 industry `co:` sweeps (Kuaishou, ByteDance, Alibaba, Tencent, Baidu, Meituan, Netflix, Google DeepMind, Microsoft Research, Meta AI, Ant Group, Xiaohongshu, Shopee, LinkedIn, NVIDIA, Amazon, Huawei) + 15 farther topical queries (CTR, click-through-rate prediction, conversion-rate prediction, ad ranking, user behavior sequence, recommender system, advertising recommendation, bidding, candidate generation, user engagement, search ranking, …). All queries spaced ≥2.2 s. **5,851 unique records → 1,436 unclaimed with a venue tag → 266 venue-tagged, published ≥ 2026-09-20 → shortlisted (incl. the rec/ads lane) → 60 featured.** Venue tags were read from each entry's arXiv `comment` / `journal_ref` fields and are **self-reported** (main vs Findings vs workshop vs industry track stated where the comment distinguished them). **Affiliations were read only from the paper's own arXiv HTML author block**; unresolved items are marked *(affiliation not recovered)* rather than guessed. The newest indexed announcement block is **2026-10-09** (same block as today's `arxiv-daily` / `arxiv-paper-check`; 10-10 → 10-12 not yet indexed).

**Dedup.** Baseline regex-extract of every arXiv ID across `wiki/**/*.md` at run start (built *after* today's siblings were staged) → **8,730 claimed IDs** (bare-ID scan). All **60 selections re-verified `rg -l` 0-hit against the whole live wiki immediately before writing**; **0 collisions**. Twelve initially shortlisted IDs were dropped at this step because they appear *somewhere* in the wiki (featured or merely *mentioned* by earlier digests) — see §13.

---

## 0. Executive Summary

- **Venue spread (60 papers):** NeurIPS 2026 **15** (12 main + 2 Evaluations & Datasets + 1 workshop), EMNLP 2026 **13** (7 main + 4 Findings + 2 Industry), **ICLR 2027 (under review)** 9, ICML 2026 **4** (1 submission), CIKM 2026 **3**, ACL/NAACL 2026 **4**, SIGMOD 2027 / ICDE 2027 **4**, AAAI 2026 + AAAI-27 submissions + AIES **3**, CVPR 2026 **2** (1 EarthVision workshop), KDD 2025 workshop **1**, RecSys/Ads/CTR lane **2** (un-venued preprints).
- **Industry density (14 of 60 have a company/lab affiliation):** **Tencent** (Exemplar2VQA, with ECNU/SJTU/Fudan), **vivo BlueImage Lab** (CFG/Information-Bottleneck paper, with SJTU/Stanford/UBC), **Sony Group** (ELMA, with Keio), **JPMorgan Chase** (FinDialogLens), **Kensho Technologies** (FLINT), **Huawei** (AIM-ZO, with SUSTech/NUS/CityU HK), **Infinigence AI** (HAPMoE, with PKU/Tsinghua), **RWS Language Weaver** (multilingual privacy tagging), **TelePIX** (SatUnreal), **Hive Trace Lab** (DUMA-Bench), **Cisco Systems** (sk-bench, with Slovak universities), **CAS / UCAS** (ChemDiffAgent; OGPO's parent lab), plus **NVIDIA/Meta/Google** appear only as baselines this window.
- **The densest technical cluster is *diffusion as a reasoning/generation substrate* (5 papers):** **ChemDiffAgent** is the first masked-diffusion *tool-using* language agent (chemical reasoning, +20% over autoregressive agents); **PDFM** turns sample-wise constraints into a primal–dual flow-matching objective with a membership-oracle-only interface; **CFG via Information Bottleneck** derives *when* classifier-free guidance should activate (post a Fisher-balance critical stage); **LSP** fixes discrete *graph* diffusion's Erdős–Rényi terminal-prior pathology by co-evolving latent sociability; and **"Your Discrete Graph Diffusion Model is Secretly Memorizing"** uses two-block SBMs to expose *conditional memorization* invisible to sample-level metrics. Two of the five audit the *same* mechanism (independent edge updates) from the generation and memorization sides.
- **A second cluster: evaluation/validity instruments (6 papers):** **LongSocialBench** (73K-token discussion threads, best model 63.0% vs human 72.4%), **sk-bench** (native Slovak, 30 datasets, 55 models), **"Which Language Should a Skeleton Speak?"** (English skeletons help only weakly and not universally), **DUMA-Bench** (dual-control agent security: ASR 26.9%→41.1%), **SALUS** (weakly-supervised auditing finds ~37% BIRD / ~27% Spider annotation errors), and **ReproBench** (only 5.3% of CVE–model pairs reproduce a real vulnerability from a CVE ID alone). The recurring finding is *measurement agreement without correctness*.
- **Numbers that anchor the window:** **OMNI** matches or beats 10 pathology foundation models across 39 tasks at **up to 10× fewer parameters** (multi-teacher distillation that *scales* with teacher count); **Exemplar2VQA** synthesizes 3D spatial QA by deterministic code execution so fine-tuned Qwen2.5-VL (3B/7B) transfers from indoor to outdoor; **APEX-Voice** — five frontier real-time voice agents, **none above 25% Pass@1, best Reliable@3 10.8%**; **KVFetch** recovers verbatim copying on RULER-16K from **0.8 → 78.4** at iso-budget; **SWE-Duel** self-scaling arena: GPT-5.5+Codex repairs **98.3%** of reviewed defects, Claude Opus 4.8 writes tasks that defeat a fixed solver **42.9% vs 4.0%** for older authors; **Softmax Reparameterization** cuts test KL by **93%** (XGLM/RTN) at W4 with **10.8%** batch-one latency reduction; **QPT** (safe offline RL) is best on **38/38 DSRL tasks**.
- **Continuity with the wiki's arcs:** the *optimization-of-generation* thread (from 10-07's looped-LM and OPD digests) now shows up as *inference-time control* — dynamic CFG activation, KV prefetch, routed memory (ARM), softmax reparameterization, AIM-ZO subspace maintenance — i.e. **capability is being bought at serving time, not training time**. The CTR-prediction architecture lane remains empty (§12), as in the last several digests.

---

## 1. NeurIPS 2026 — Main Track (12 papers)

### 1.1 ChemDiffAgent: Masked Diffusion Language Agents for Tool-Integrated Chemical Reasoning
- **中文标题**: ChemDiffAgent：面向工具集成化学推理的掩码扩散语言智能体
- **Authors**: (see paper) — *bilemond* group
- **Affiliation**: State Key Laboratory of AI Safety, Institute of Computing Technology, CAS, China; University of Chinese Academy of Sciences (CAS), China
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Chemical agents built on the autoregressive paradigm are limited by causal (left-to-right) attention — they struggle with bidirectional molecular understanding, globally coordinated tool planning, and multi-source evidence integration.
- **Key innovation**: **ChemDiffAgent** — the first **masked diffusion language agent** for tool-integrated chemical reasoning; reformulates reasoning as iterative denoising over interleaved reasoning/tool-use trajectories, so tool-use decisions are made under **full-trajectory context**, aligning the decision boundary with the knowledge boundary. Two-stage post-training: agentic SFT + variance-reduced preference optimization.
- **Results / comparison**: On a new benchmark of six chemistry tasks (single- and multi-turn tool use), **~20% overall improvement over autoregressive agents**; the 8B model matches or surpasses much larger frontier models (GPT-5.5, Claude Opus 4.7) under matched budgets.
- **Link**: https://arxiv.org/abs/2610.13330

### 1.2 Budgeted Multi-Source Counterfactual Annotation for Off-Policy Evaluation
- **中文标题**: 面向离线策略评估的预算化多源反事实标注
- **Authors**: (see paper) — **Lygist** group
- **Affiliation**: Johns Hopkins Carey Business School; International Computer Science Institute, Berkeley; Georgia Institute of Technology
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Off-policy evaluation (OPE) suffers high-variance reweighting / reward-model extrapolation when the behavior policy has poor coverage; counterfactual annotations from experts/LLMs can help but are costly, biased, or noisy.
- **Key innovation**: Casts **budgeted annotation acquisition for contextual-bandit OPE** as an integer allocation over (context-action, source) pairs; a **first-annotation threshold** characterizes when annotations pay off, and a **majorization-minimization** algorithm with dynamic-programming subroutines monotonically improves the objective.
- **Results / comparison**: Reduces fixed-profile MSE by **20.58% (synthetic clinical)** and **10.77% (LLM-annotated education)** bandits vs no annotation.
- **Link**: https://arxiv.org/abs/2610.10974

### 1.3 Network Intervention by Polling Strategic Agents
- **中文标题**: 通过轮询策略性智能体进行网络干预
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **NeurIPS 2026** (published as conference paper)
- **Problem background**: A planner in a network of *strategic* agents must set prices when the optimum depends on private information, agents may misreport, and exact computation does not scale.
- **Key innovation**: Shows optimal non-discriminatory prices admit a **centrality-based decomposition of the welfare kernel** (contribution scales with *squared* centrality in a preference-reweighted network); motivates **Poll**, which samples one agent per round, walks its neighborhood briefly, and updates prices from local reports. Three efficiencies follow from the same decomposition: computational, statistical (query complexity scales with topology/heterogeneity, not population size), and economic (truthful reporting; adversarial deviations detected).
- **Results / comparison**: Up to **three orders of magnitude less communication** than exact/other distributed methods on a real network with **300,000+ agents**.
- **Link**: https://arxiv.org/abs/2610.08347

### 1.4 How Do Transformers Learn to Represent Symmetries?
- **中文标题**: Transformer 如何学习表示对称性？
- **Authors**: (see paper)
- **Affiliation**: Technical University of Munich; Munich Center for Machine Learning; Massachusetts Institute of Technology
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Training Transformers with finite data augmentation is a popular route to geometric invariance, but the interplay of architecture, symmetry type, and augmentation budget is underexplored.
- **Key innovation**: Identifies an **ordering of learnability across symmetry groups** — non-angle-preserving < angle-preserving < base angle-preserving (translation/rotation/scale) — and performs a structural analysis of trained point-cloud Transformers that exposes **interpretable mechanisms inducing invariance**, then extends them to learned equivariance.
- **Results / comparison**: For base angle-preserving groups, characterizes extrapolation behavior and shows the detected approximate-invariance mechanisms form a **building block for learned equivariance**.
- **Link**: https://arxiv.org/abs/2610.10305

### 1.5 Primal-Dual Flow Matching for Sample-Wise Constrained Generation
- **中文标题**: 面向样本级约束生成的原始–对偶流匹配（PDFM）
- **Authors**: Zhengyan Huan (et al.)
- **Affiliation**: Department of Electrical and Computer Engineering, Tufts University; NSF AI Institute for AI and Fundamental Interactions
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Generating data that satisfies a *sample-wise* constraint with a user-specified satisfaction probability usually needs differentiable distances, projections, or convexity of the constraint set.
- **Key innovation**: **PDFM** starts from a population-level constrained NLL and, under a flow-matching parameterization, derives **guarantees on the probability of constraint satisfaction** for the primal–dual algorithm; it requires only **binary membership-oracle feedback**, with no differentiable distance, projection, or convexity assumptions, and gives direct control over the satisfaction rate.
- **Results / comparison**: Improves constraint satisfaction over vanilla flow matching and is competitive with constraint-aware baselines while maintaining distributional fidelity.
- **Link**: https://arxiv.org/abs/2610.12699

### 1.6 Opening the Black Box of Classifier-Free Guidance via Information Bottleneck
- **中文标题**: 用信息瓶颈揭开 Classifier-Free Guidance 的黑箱
- **Authors**: (see paper)
- **Affiliation**: Shanghai Jiao Tong University; **vivo BlueImage Lab, vivo Mobile Communication Co., Ltd.**; Stanford University; Michael Smith Laboratories, University of British Columbia
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: CFG's activation schedule is usually picked heuristically; dynamic variants rely on hand-designed schedules with no principled account of *when* conditional information is most useful.
- **Key innovation**: Formulates the diffusion trajectory as a **time-dependent information bottleneck** and shows the effectiveness of conditioning is non-uniform — it strengthens sharply after a **critical stage characterized by a Fisher-information balance condition**. Proposes a **training-free dynamic CFG** that builds a stochastic process from conditional/unconditional score statistics and activates guidance when the estimated guidance gain crosses a threshold (interval-based guidance recovered as a limiting case).
- **Results / comparison**: Robust and broadly applicable across architectures/tasks; provides an interpretation of dynamic guidance and a principled inference-time control foundation.
- **Link**: https://arxiv.org/abs/2610.13369

### 1.7 OMNI: Scaling Multi-Teacher Distillation for Digital Pathology
- **中文标题**: OMNI：面向数字病理的多教师蒸馏规模化
- **Authors**: Sofiene Boutaj (et al.) — *OMNI project*
- **Affiliation**: Université Paris-Saclay / CentraleSupélec / Gustave Roussy / INSERM IHU PRISM (Cancer Data Science Unit), France; Stony Brook University, USA
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Many pathology foundation models now exist, but standard multi-teacher distillation (MTD) *degrades* as more teachers are added to a single student encoder.
- **Key innovation**: Shows **learning teacher-specific representations** is the key to scaling MTD; proposes teacher tokens, a tailored attention scheme, extra mixture-of-experts layers, and a contrastive loss. Releases **OMNI**, a collection of student encoders trained from **10 SOTA foundation models**.
- **Results / comparison**: Students **up to 10× more efficient** than the teacher foundation models while matching — and sometimes beating — them across **39 tile- and slide-level tasks** (validated over **>10 foundation models**); analysis shows the teacher-specific representations are complementary and easy to aggregate downstream.
- **Link**: https://arxiv.org/abs/2610.12574

### 1.8 When Edge Independence Fails: Joint Graph Diffusion with Latent Sociability Priors
- **中文标题**: 当边独立性失效：带潜在社交性先验的联合图扩散
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Discrete graph diffusion corrupts structure via **independent edge updates**; with an exchangeable output distribution the terminal prior must be Erdős–Rényi (E-R), and in the large-graph limit an E-R input makes any GNN denoiser output approximately E-R — so denoising is weak and node heterogeneity/higher-order structure is lost.
- **Key innovation**: Diagnoses the **prior**, not expressivity, as the root cause; introduces the **Latent Sociability Prior (LSP)** and a joint diffusion that **co-evolves latent node sociability and graph structure**, removing edge independence while preserving exchangeability and requiring no complex encoder.
- **Results / comparison**: More accurately captures graph distributions than baselines **without node features** across multiple graph-generation datasets.
- **Link**: https://arxiv.org/abs/2610.13765

### 1.9 Exemplar2VQA: Scalable Exemplar-Driven VQA Generation via Multi-Agent Coding
- **中文标题**: Exemplar2VQA：基于多智能体编码的可扩展范例驱动 VQA 生成框架
- **Authors**: Jiayu Ying (et al.)
- **Affiliation**: East China Normal University; Shanghai Jiao Tong University; Fudan University; **Tencent**
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Spatial intelligence in MLLMs is bottlenecked by scarce complex 3D QA data; manual annotation is costly and direct LLM synthesis fails on spatial/geometric computation.
- **Key innovation**: **Exemplar2VQA** — a scalable, **exemplar-driven** generation framework: collaborative agents use a library of geometric utilities to produce large-scale spatial QA via **deterministic code execution**, autonomously scaling static object-centric query templates into massive synthetic datasets.
- **Results / comparison**: Fine-tuning **Qwen2.5-VL (3B/7B)** exclusively on generated synthetic indoor data significantly improves diverse benchmarks, and transfers **out-of-domain to outdoor and mixed-scene** benchmarks — closing the sim-to-real gap.
- **Link**: https://arxiv.org/abs/2609.37655

### 1.10 Asymptotically Optimal Best Arm Identification with Fixed Budget under Differential Privacy
- **中文标题**: 差分隐私下固定预算最优臂识别
- **Authors**: (see paper)
- **Affiliation**: Institute of Data Science; National University of Singapore; Dept. of Electrical and Computer Engineering; Dept. of Mathematics
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Best-arm identification under pure ε-DP must achieve statistical efficiency and privacy simultaneously; the fixed-budget error exponent differs from the fixed-confidence stopping-time exponent.
- **Key innovation**: Proves the optimal error-probability exponential rate is bounded by an instance-dependent **privacy-aware transportation exponent**; proposes **AO-Pri-BAI**, which keeps private running estimates via **Laplace-tree mechanisms** and learns a sampling design through a min–max interaction between hard alternatives and arm allocations, and matches the privacy-aware benchmark.
- **Results / comparison**: Satisfies pure ε-DP; beats benchmark algorithms non-asymptotically on various instances.
- **Link**: https://arxiv.org/abs/2610.04600

### 1.11 OGPO: Offline Goal-conditioned Policy Optimization for Recoverable Vision-Language-Action Models
- **中文标题**: OGPO：面向可恢复视觉-语言-动作模型的离线目标条件策略优化
- **Authors**: (see paper)
- **Affiliation**: National Key Laboratory of Space Integrated Information System; Institute of Software, Chinese Academy of Sciences; University of Chinese Academy of Sciences; Wangxuan Institute of Computer Technology, Peking University
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: VLA post-training usually supervises trajectory-level imitation, biasing policies toward demonstration-specific action paths and giving little guidance to **recover** once execution deviates.
- **Key innovation**: **OGPO** relabels trajectories with **semantic key states** and builds **goal-conditioned process rewards**, shifting VLA post-training from trajectory-level action imitation to **key-state reachability learning** — no extra online interaction.
- **Results / comparison**: Consistently improves over standard SFT on LIBERO and MetaWorld; on LIBERO-Plus and a new **LIBERO-ReAct** mid-execution-perturbation benchmark it shows stronger robustness and goal-directed recoverability under distribution shift.
- **Link**: https://arxiv.org/abs/2610.12914

### 1.12 PANDA: Prior-guided Attentional Dual-path Architecture
- **中文标题**: PANDA：先验引导的注意力双路径架构
- **Authors**: (see paper) — **jainris** group
- **Affiliation**: University of Cambridge, UK; University of Bergamo, Italy; Independent Researcher
- **Venue**: **NeurIPS 2026** (accepted)
- **Problem background**: Hypergraph neural networks use either fixed structural weights (which propagate misleading information under heterophily) or normalized attention (which is *competitive*: raising one sender's weight lowers others' in the same aggregation set).
- **Key innovation**: **PANDA** — a plug-in for two-stage message-passing HNNs (directed and undirected): the main path interpolates between learned receiver-normalized attention and structural incidence priors, while a **non-competitive, non-normalized auxiliary path** lets each sender contribute its own transformed information; recovers a known complex-valued convolution operator under fixed structural coefficients.
- **Results / comparison**: Plugging PANDA into **four HNNs** (spatial + spectral, directed + undirected) yields an average **+5.18 pp** across eight real-world benchmarks.
- **Link**: https://arxiv.org/abs/2610.13635

---

## 2. NeurIPS 2026 — Evaluations & Datasets Track / Workshops (3 papers)

### 2.1 Realism vs Accuracy: Event Sequence Forecasting from a Generative Modeling Perspective
- **中文标题**: 真实性与准确性：从生成建模视角看事件序列预测
- **Authors**: (see paper) — **xaosina** group
- **Affiliation**: ITMO University; Vega Institute Foundation; SB AI Lab; Applied AI Institute
- **Venue**: **NeurIPS 2026** (Spotlight, Evaluations & Datasets Track)
- **Problem background**: Multi-horizon event-sequence forecasting is studied for accuracy alone, ignoring distributional realism — yet both matter in finance/healthcare/business-process intelligence.
- **Key innovation**: A **benchmark** with metrics for both quality axes, strong statistical baselines, and recent models adapted from adjacent fields; then **Wasserstein BaryBooster**, which aggregates samples from a realism-strong diffusion model into an SOTA predictor, converting distributional realism into prediction accuracy.
- **Results / comparison**: Careful evaluation shows **no method excels at both** — a fundamental accuracy/realism trade-off — that BaryBooster partly bridges.
- **Link**: https://arxiv.org/abs/2610.12586

### 2.2 ELMA: Benchmarking Anaphoric Compositions for Long-Term Text-to-Motion Generation
- **中文标题**: ELMA：面向长时文本到动作生成的照应组合评测
- **Authors**: (see paper)
- **Affiliation**: Keio University / Keio AI Center; **Sony Group Corporation**
- **Venue**: **NeurIPS 2026** (Evaluations & Datasets Track)
- **Problem background**: Text-guided long-term motion generation fails on multi-segment instructions with **anaphora**, where constraints set in earlier segments must be preserved over time.
- **Key innovation**: Introduces the task of **long-term motion generation from anaphoric compositions** and **ELMA**, an episodic dataset with dense segment-level annotations preserving cross-segment dependencies, built by a fully automated collection/filtering pipeline that extracts continuous 30-second clips from in-the-wild video.
- **Results / comparison**: Fine-tuning SOTA motion generators on ELMA reveals fundamental shortcomings on context-dependent instructions, and yields significant gains in **global physical realism and semantic alignment** — a new long-term baseline.
- **Link**: https://arxiv.org/abs/2610.13549

### 2.3 Your Discrete Graph Diffusion Model is Secretly Memorizing
- **中文标题**: 你的离散图扩散模型正在悄悄记忆
- **Authors**: (see paper)
- **Affiliation**: CNRS, IRISA, Rennes, France
- **Venue**: **NeurIPS 2026 Workshop BeNTo (Beyond Next Token Prediction)**
- **Problem background**: Sample-level metrics (edge overlap, WL-kernel similarity) suggest equivariant graph diffusion trained on a single graph produces novel graphs — i.e. no memorization.
- **Key innovation**: Challenges this: analyzing reverse trajectories of GDMs trained on **two-block stochastic block models** reveals **conditional memorization** — the model recovers a corrupted *training* graph almost perfectly vs a held-out test graph, visible only when the trajectory is conditioned on a corrupted training graph. Coincides with a growing generalization gap that **early stopping cannot fix**; memorization onset always precedes community-structure emergence.
- **Results / comparison**: Holds across all tested node sizes; every earlier checkpoint produces structureless graphs.
- **Link**: https://arxiv.org/abs/2610.13786

---

## 3. EMNLP 2026 (13 papers)

### 3.1 GLIME: Generalizable Lifelong Model Editing via Preference Optimization
- **中文标题**: GLIME：通过偏好优化实现可泛化的终身模型编辑
- **Authors**: (see paper)
- **Affiliation**: Department of Computer Science and Engineering, Korea University
- **Venue**: **EMNLP 2026** (Main)
- **Problem background**: Lifelong knowledge editing (continual updates) makes existing methods overfit target prompts, degrading generalization and general capabilities.
- **Key innovation**: **GLIME** combines knowledge editing with **preference optimization over generation behavior**, plus replay-based editing and a gradient constraint to preserve previously edited knowledge.
- **Results / comparison**: Significantly improves knowledge generalization in lifelong editing while maintaining editing performance and general capabilities.
- **Link**: https://arxiv.org/abs/2609.36748

### 3.2 LongSocialBench: Do Long-Context LLMs Understand Online Discussion Threads?
- **中文标题**: LongSocialBench：长上下文 LLM 理解在线讨论帖吗？
- **Authors**: (see paper)
- **Affiliation**: University of Illinois Urbana-Champaign; Semantic Code Lab
- **Venue**: **EMNLP 2026** (Main)
- **Problem background**: Understanding discussion threads needs structure-aware social reasoning (parent-reply relations, turning points, scoped subtrees, cross-branch contrasts, participant trajectories), not just long-document reading.
- **Key innovation**: **LongSocialBench** — **1,462 verified human-authored MCQ items** from 94 complete Hacker News / Stack Exchange / r/ChangeMyView episodes (**median ~73K tokens**), each pairing a serialized discussion + reply structure with a 4-option question; items verified for answerability, option uniqueness, and evidence grounding.
- **Results / comparison**: Across **18 models / 29 settings**, best is **Claude-Opus-4.7 at 63.0%** (eliminate-options prompting) vs **72.4% human**; the full-context baseline averages **43.9%**, and supplying gold evidence scope only lifts it to **55.0%** — the missing capability is social understanding over reply trees.
- **Link**: https://arxiv.org/abs/2610.04118

### 3.3 Tracing a Sparse Emotion-Control Circuit in LLM-Based Text-to-Speech
- **中文标题**: 追踪 LLM 文本到语音中的稀疏情绪控制回路
- **Authors**: (see paper)
- **Affiliation**: Department of Computer Science, William & Mary, USA
- **Venue**: **EMNLP 2026** (Main)
- **Problem background**: LLM-based TTS can be emotionally expressive, but how reference emotion is routed and realized in decoded speech is unclear.
- **Key innovation**: Two emotion-sensitive metrics (**codec trajectory score**, **late residual direction score**) plus activation-patching reveal a **sparse source-to-readout circuit: 23–27 attention heads + MLPs per emotion (~5% of components)** recovering/suppressing **74–88%** of the late emotion-readout shift; circuit = shared backbone + emotion-specific parts; cross-emotion swaps reduce target readout in **47/48** cases.
- **Results / comparison**: Interventions change pitch/energy/spectral brightness over 24 matched pairs/emotion; a readout-matched residual baseline reproduces only **17–27%** of the pitch effect — readout movement alone does not explain decoded acoustics.
- **Link**: https://arxiv.org/abs/2610.05080

### 3.4 sk-bench: A Native-First Benchmark for Evaluating LLMs in Slovak
- **中文标题**: sk-bench：面向斯洛伐克语的母语优先 LLM 评测基准
- **Authors**: (see paper) — **slovak-nlp** group
- **Affiliation**: Comenius University in Bratislava; Kempelen Institute of Intelligent Technologies; Technical University of Košice; **Cisco Systems**; Brno University of Technology
- **Venue**: **EMNLP 2026** (Main)
- **Problem background**: Morphologically rich Slovak is omitted from (or machine-translated into) multilingual benchmarks.
- **Key innovation**: **sk-bench** — native-first benchmark, **30 datasets (33 task variants)** across ten skill categories, **11 resources introduced/first packaged** for generative-LLM eval (incl. IFEval-SK with Slovak-adapted checkers); evaluates **55 open/closed models** under one harness.
- **Results / comparison**: Best open model trails proprietary APIs by **12.6 pts**; native vs translated closed-form rankings agree (**ρ≥0.98**) but human- vs LLM-authored QA rank models differently (**ρ=0.72**); continued Slovak pretraining *lowers* Qwen3-14B by **13.9 pts** (a small instruction set recovers ~3/4); test-time reasoning adds **8.5–12.5 pts** for ≥9B models.
- **Link**: https://arxiv.org/abs/2610.09152

### 3.5 Bridge Routing Heads: Where Multilingual Multi-hop Reasoning Lives in LLMs
- **中文标题**: Bridge Routing Heads：多语言多跳推理在 LLM 中的位置
- **Authors**: (see paper) — Chosun / Soongsil University
- **Affiliation**: Chosun University; Soongsil University
- **Venue**: **EMNLP 2026** (accepted)
- **Problem background**: Multilingual LLMs answer the same multi-hop question across languages, but there is no mechanistic account of whether a shared internal circuit exists.
- **Key innovation**: Identifies **Bridge Routing Heads (BRH)** via a three-stage pipeline; head sets are nearly **mutually exclusive across five languages** (mean Jaccard **0.017** for Llama 3.1 70B, **0.057** for Qwen 2.5 72B) — language-idiosyncratic circuits; the two models share the *pattern* but allocate heads differently (Llama: large general pool; Qwen: larger language-specific pools).
- **Results / comparison**: Ablating general BRH raises two-hop NLL by **39–89×** the random-head baseline (causal evidence); amplifying these heads **rescues up to 51.7%** of cross-lingual failures with **no training**.
- **Link**: https://arxiv.org/abs/2610.09733

### 3.6 Which Language Should a Skeleton Speak? (LASEF)
- **中文标题**: 骨架该说哪种语言？多语言推理中的骨架语言选择（LASEF）
- **Authors**: (see paper) — **lhsstn** group
- **Affiliation**: ETRI; KAIST; Department of Artificial Intelligence, Dankook University
- **Venue**: **EMNLP 2026** (Findings)
- **Problem background**: Skeleton-based reasoning prompting is training-free but largely assumes an English-centric setting.
- **Key innovation**: **LASEF** (Language-Aware Skeleton Exploration Framework) studies skeleton-language choice across math benchmarks, model scales, and languages, combining greedy decoding, multi-rollout evaluation, translation ablation, and cross-benchmark validation.
- **Results / comparison**: English skeletons give only a **small positive tendency on average** (most visible for smaller models and low-resource languages); **few language-level gains survive correction** and English is **not universally optimal** — skeleton language is a context-dependent design variable with directionally-consistent, benchmark-dependent, and asymmetric-negative effects.
- **Link**: https://arxiv.org/abs/2610.09607

### 3.7 Narrowing the Horizon: Quantifying Topic Saliency Shifts in Generative Monoculture
- **中文标题**: 收窄视野：量化生成式单一文化中的主题显著性漂移
- **Authors**: (see paper) — **oriane** group
- **Affiliation**: King's College London, United Kingdom
- **Venue**: **EMNLP 2026** (Findings)
- **Problem background**: LLM outputs risk converging into a *generative monoculture*, but model-level studies cannot pinpoint which topics/viewpoints are marginalized.
- **Key innovation**: A method to measure **shifts in topic saliency** across model families during post-training, applied as a case study of climate-change discourse; also tests interventions.
- **Results / comparison**: Homogenization measurably narrows the representation of diverse solutions; **specialized models can preserve a broader range of perspectives**.
- **Link**: https://arxiv.org/abs/2609.35302

### 3.8 REDaCT: Collapse-Free Unlearning in Large Reasoning Models
- **中文标题**: REDaCT：大型推理模型中的无坍缩遗忘
- **Authors**: (see paper) — **jmaccoby** group
- **Affiliation**: Stevens Institute of Technology, Hoboken, NJ, USA
- **Venue**: **EMNLP 2026** (Findings)
- **Problem background**: Unlearning in LRMs must remove forget-set info from both reasoning trace and answer, but existing methods cause **reasoning collapse** (no coherent CoT, no proper termination).
- **Key innovation**: **REDaCT** (REgenerate via Detection and Corrective Tuning), an **inference-time** framework: a binary **leak detector** finds leaking sentences, and an offline-learned **corrective embedding** injected at the first detected leak steers subsequent reasoning away from leakage.
- **Results / comparison**: Completely avoids reasoning collapse, substantially improves reasoning preservation vs SOTA, while keeping **perfect answer forgetting and near-perfect CoT forgetting**.
- **Link**: https://arxiv.org/abs/2610.12769

### 3.9 HAPMoE: Heterogeneity-Aware Automatic Parallelism Planning for MoE Training
- **中文标题**: HAPMoE：面向 MoE 训练的异构感知自动并行规划
- **Authors**: (see paper)
- **Affiliation**: State Key Laboratory of Multimedia Information Processing, Peking University; **Infinigence AI**; Tsinghua University
- **Venue**: **EMNLP 2026** (Findings)
- **Problem background**: Automatic parallelization must handle both MoE architecture complexity and **cluster heterogeneity**, but existing approaches target only one of the two.
- **Key innovation**: **HAPMoE** builds a light **MoE-aware cost model** and searches a **six-dimensional parallel space**, producing plans directly deployable on **Megatron-LM**; a pruning-enhanced dynamic program completes the search in **<1 minute**; non-uniform pipeline partitioning.
- **Results / comparison**: Up to **3.2× end-to-end training-throughput** improvement over baselines across heterogeneous clusters, with non-uniform partitioning adding up to **78%**.
- **Link**: https://arxiv.org/abs/2609.39350

### 3.10 FLINT: From Benchmarks to Production — A Text-to-SQL System for Complex Financial Data
- **中文标题**: FLINT：从基准到生产——面向复杂金融数据的 Text-to-SQL 系统
- **Authors**: (see paper)
- **Affiliation**: **Kensho Technologies**
- **Venue**: **EMNLP 2026** (Industry Track)
- **Problem background**: General Text-to-SQL systems fall below 50% on production financial DBs where concepts are **opaque integer keys** and simple queries require multiple joins/filters.
- **Key innovation**: **FLINT** has three parts: (1) a **lookup agent** resolving NL concepts to question-specific reference-table constraints; (2) embedding-based retrieval of structurally similar query templates from an expert-authored bank; (3) **schema linking** that prunes a large schema by traversing **foreign-key chains** rather than name similarity.
- **Results / comparison**: On two datasets (**359 questions**) over production financial schemas, outperforms SOTA baselines using the same LLM; **deployed in production** as part of a financial data-retrieval service.
- **Link**: https://arxiv.org/abs/2610.03524

### 3.11 FinDialogLens: Event Extraction over Multi-Party Dialogue for Missed-Trade Identification
- **中文标题**: FinDialogLens：多方对话事件抽取用于识别漏单交易
- **Authors**: (see paper)
- **Affiliation**: Machine Learning Center of Excellence, **JPMorgan Chase & Co.**
- **Venue**: **EMNLP 2026** (Industry Track)
- **Problem background**: In financial chatrooms, each Request-for-Quote's final price/outcome appears many messages after the trigger, interleaved with concurrent RFQs — manual missed-trade recovery is infeasible.
- **Key innovation**: **FinDialogLens** — a hybrid LLM pipeline where compact fine-tuned classifiers act as inference-time scaffolds (RFQ-trigger + price/outcome detection, RFQ-Level Module segmentation, Trade Engine role filling); a **difficulty-aware router** allocates RFQs between a low-cost rule engine and the LLM Trade Engine.
- **Results / comparison**: With GPT-4o, **92.1% / 94.3%** accuracy on final price / trade outcome (beats full-chatroom CoT); fine-tuned open-source LLMs with as few as 3B params are comparable; the router cuts LLM calls by **85%** on final price, saving **>$300/day** at a **70,000-RFQ/day** scale.
- **Link**: https://arxiv.org/abs/2610.02455

### 3.12 How Well Can LLMs Simulate Real Learner Evaluations of Educational Feedback?
- **中文标题**: LLM 能在多大程度上模拟真实学习者对教育反馈的评估？
- **Authors**: (see paper)
- **Affiliation**: Tohoku University; NII R&D Center for Large Language Models; National Institute of Informatics; University of Tokyo; Osaka Kyoiku University
- **Venue**: **EMNLP 2026** (Main)
- **Problem background**: It is unclear how well LLMs can simulate subjective learner evaluations in education.
- **Key innovation**: Uses **real learner evaluation data** on feedback for high-school biology questions, at group and individual levels, comparing with/without learner-specific information (personality traits, evaluation examples) across six models.
- **Results / comparison**: LLMs still simulate learner evaluations only **limitedly**; learner profiles + examples improve score calibration and individual-level simulation but **more often fail to improve group-level consistency**.
- **Link**: https://arxiv.org/abs/2609.35376

### 3.13 RASPER: Reward-Aligned Summarization of Clinical Notes for EHR Outcome Prediction
- **中文标题**: RASPER：面向 EHR 结局预测的奖励对齐临床笔记摘要
- **Authors**: (see paper)
- **Affiliation**: Electrical Engineering and Computer Science, University of Kansas, USA
- **Venue**: **EMNLP 2026** (Main)
- **Problem background**: Unstructured discharge notes carry complementary signal but bury it in noisy text; generic summaries omit decisive evidence.
- **Key innovation**: **RASPER** optimizes summarization **directly against the downstream clinical task** — a tunable LLM summarizer trained via RL from prediction feedback (reward = downstream predictor loss), grounded by a **longitudinal encoder** converting structured codes into soft prompts so summaries complement rather than duplicate codes.
- **Results / comparison**: Consistently outperforms strong baselines on **readmission prediction and medication recommendation** across MIMIC-III and MIMIC-IV.
- **Link**: https://arxiv.org/abs/2610.02979

---

## 4. ICLR 2027 (Under Review) (9 papers)

### 4.1 SWE-Duel: Towards a Self-Scaling Arena for Coding Agents
- **中文标题**: SWE-Duel：面向编码智能体的自扩展竞技场
- **Authors**: (see paper)
- **Affiliation**: School of Computing and Information Systems, Singapore Management University
- **Venue**: **ICLR 2027** (under review)
- **Problem background**: Static coding benchmarks leak into training data and saturate; a benchmark should instead be **self-scaling** — tasks/oracles created at evaluation time, difficulty set by participating agents.
- **Key innovation**: **SWE-Duel** — two coding agents evaluate each other over **mirrored Red–Blue turns**: Red implements a feature with tests then embeds a subtle bug + sealed tests; the PR is admitted only if it passes feature/repo tests and fails exactly the bug tests *and* a fresh same-agent session can repair the bug blind; Blue reviews without being told a bug exists and wins only if its revision passes all three suites; then roles swap.
- **Results / comparison**: Tournament among **11 model-harness participants, 15 repos, 5 languages, 1,500 turns**: GPT-5.5+Codex CLI ranks first as solver, repairing **98.3%** of reviewed defects; Claude Opus 4.8 + mini-swe-agent ranks second as author (**27.3%** Red win rate); within one family, tasks by the newest version defeat a fixed-reference solver **42.9% vs 4.0%** for older versions — task difficulty scales with authoring capability.
- **Link**: https://arxiv.org/abs/2610.12569

### 4.2 ARTS-Hybrid: Mechanism-Guided Generation and Refinement of LLM Rubrics
- **中文标题**: ARTS-Hybrid：机制引导的 LLM 评分标准生成与精炼
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **ICLR 2027** (under review)
- **Problem background**: Existing work generates better rubrics but has limited understanding of *what makes rubric design effective*.
- **Key innovation**: A systematic **mechanistic analysis** of rubric design (criterion organization, operationalization, score aggregation): structural organization enables more comprehensive criteria; semantic specification alone does **not** ensure effective criterion-level judgments; sophisticated aggregation gives limited extra gains. Then **ARTS-Hybrid** — adaptive **rubric tree search** + semantic-first, **response-calibrated** refinement.
- **Results / comparison**: Improves end-to-end evaluation and intrinsic rubric quality; generated rubrics also provide effective signals for model optimization.
- **Link**: https://arxiv.org/abs/2610.13375

### 4.3 KVFetch: Temporal Prefetching for the Missing Half of KV Cache Compression
- **中文标题**: KVFetch：KV Cache 压缩缺失一半的时序预取
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **ICLR 2027** (under review)
- **Problem background**: All three KV-compression families (score eviction, summary compensation, offload-and-recall) decide what to keep **by content relevance** — but a cache supports both **associative lookup** and **sequential traversal**, and only the former is implemented. Under content eviction, verbatim copying (RAG/code/structured extraction) breaks irreversibly: **sequential forgetting**.
- **Key innovation**: **KVFetch** — training-free, drop-in **temporal recall channel** for any score-based compressor: suggests demote evicted candidates to a **quantized cold tier**, detect active copying via a **monotone read pointer**, and **prefetch positional successors** into fixed-size hot slots at no added attention cost.
- **Results / comparison**: On RULER-16K at iso-budget, recovers verbatim copying **0.8 → 78.4** and raises the 13-task average by **+8.4** (gains concentrated on sequential-access tasks); on LongBench (no sequential access) the channel stays **dormant and cost-free**.
- **Link**: https://arxiv.org/abs/2610.08811

### 4.4 Softmax Reparameterization for Output-Head Quantization
- **中文标题**: 面向输出头量化的 Softmax 重参数化
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **ICLR 2027** (under review)
- **Problem background**: Large vocabularies make output heads a substantial inference cost for small LMs; naive post-training quantization distorts predictions.
- **Key innovation**: **Softmax reparameterization** — a post-training search over functionally equivalent output heads *before* quantization: subtract a scalar multiple of the vocabulary-row mean from every output row, choosing the coefficient by validation KL. For linear-softmax heads these shifts preserve full-precision predictions exactly (no retraining); a rank-one correction extends to nonlinear logit paths.
- **Results / comparison**: Across **7 heads × 3 quantizers**, W4 test KL falls **93%** (XGLM/RTN) and **73–77%** (Phi/BLOOM/BLOOMZ, activation-weighted MSE); gains persist under GPTQ and replicate on holdout; frozen WikiText coefficients transfer to C4/OpenWebMath; a packed W4 Phi head cuts batch-one latency **10.8%** while preserving the speedup.
- **Link**: https://arxiv.org/abs/2609.31291

### 4.5 Knowing the Store: What a Memory Backend Must Write Down Before an Agent Can Read It
- **中文标题**: 了解存储：智能体读取前记忆后端必须写下什么
- **Authors**: (see paper) — **ansh348** group
- **Affiliation**: Bilkent University, Ankara, Türkiye
- **Venue**: **ICLR 2027** (under review, 94 pp)
- **Problem background**: A long-term-memory agent can answer from a record it should no longer use (e.g. a cancelled plan); what must a store expose for the agent to know this *before* retrieving?
- **Key innovation**: Scores **metamemory monitoring** on its own: readers see only a **value-free summary** (record counts by lifecycle state + attribute-name list); **148 questions** each asked against **three store versions differing in one attribute** so wording cannot give the answer away.
- **Results / comparison**: On short lists (avg **2.6** names) **no model reliably beats** a cosine-similarity lookup over the names; on padded 60-name lists the lookup loses **0.18** while GPT-5.6 Luna/Sol lose 0.06–0.07 and lead by 0.13–0.14; under **FR-Bank** metadata several readers drop (GPT-4.1 mini 0.73→0.60, Haiku 4.5 0.82→0.71) — **what the store wrote down limited every reader**.
- **Link**: https://arxiv.org/abs/2610.04794

### 4.6 AIM-ZO: Activation-Informed Subspace Maintenance for Zeroth-Order LLM Fine-Tuning
- **中文标题**: AIM-ZO：面向零阶 LLM 微调的激活信息子空间维护
- **Authors**: (see paper) — **EkkoXy** group
- **Affiliation**: Southern University of Science and Technology; National University of Singapore; **Huawei Technologies Ltd.**; City University of Hong Kong
- **Venue**: **ICLR 2027** (under review)
- **Problem background**: Zeroth-order optimization estimates updates from forward evaluations only, but isotropic perturbations waste evaluations on weakly informative directions; existing low-dimensional-subspace ZO methods can miss useful directions.
- **Key innovation**: **AIM-ZO** uses **forward activations as local directional information**, continuously integrating them into a broad evolving subspace; decouples **maintained width** from **active width** (activate a smaller set of shared/sampled directions) to access gradient-relevant structure cheaply.
- **Results / comparison**: Across **5 LLMs × 11 tasks** at matched forward-evaluation budgets, its six-task average beats the strongest fully-evaluated ZO baseline by **1.26 pp** (OPT-2.7B) and MeZO by **2.85 pp** (OPT-30B).
- **Link**: https://arxiv.org/abs/2609.35257

### 4.7 Jailbreak Context Lingers: Divergent Safety Routing and Its Cross-Task Predictability in Tool Agents
- **中文标题**: 越狱上下文挥之不去：工具智能体中的分歧安全路由及其跨任务可预测性
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **ICLR 2027** (under review)
- **Problem background**: Post-jailbreak safety feedback is assumed to be a reliable safeguard, but how lingering jailbreak context shapes subsequent agent behavior is unexplored.
- **Key innovation**: A **paired continuation framework** across 192 parent tasks / 42 domains, **12,148 analyzed continuation pairs** across 8 agents; finds identical safety feedback induces model-dependent routing — **rescue**, **persistent unsafe**, or **collateral loss** (over-refusal); layer-wise activation patching reveals a shared **late-commit pattern** (causal effects surge at relative depths **0.958–0.984**) whose peak magnitude varies >30× across architectures.
- **Results / comparison**: Critical-layer features predict full-trajectory routing under leave-one-parent-task-out (ROC AUC **0.675 rescue / 0.777 collateral loss / 0.702 persistent unsafe**) and intervening there causally alters concrete tool actions.
- **Link**: https://arxiv.org/abs/2609.34686

### 4.8 APEX-Voice: Can Voice Agents Complete Professional Workflows Through Full-Duplex Interaction?
- **中文标题**: APEX-Voice：语音智能体能否通过全双工交互完成专业工作流？
- **Authors**: (see paper)
- **Affiliation**: University of Maryland College Park, USA
- **Venue**: **ICLR 2027** (under submission)
- **Problem background**: Fluent full-duplex dialogue does not guarantee correct completion of delegated professional workflows.
- **Key innovation**: **APEX-Voice** — a benchmark of **120 interactive professional workflows** across ten work archetypes (form completion, negotiation, coordination, consulting, interviewing, …), each in a **stateful Voice Workbench** with task knowledge, typed tools, gold final artifact, authorization constraints, and a user simulator backed by pre-compiled speech; scores both **artifact field accuracy** and **end-to-end workflow success** (correct terminal state, valid process, completed actions, valid artifact).
- **Results / comparison**: Across five frontier real-time voice agents (GPT-Live-1, Gemini-3.8-Live, Grok-Voice-Think-2.0, Step-Audio3, GPT-realtime-2.1), **none exceeds 25% Pass@1**, best **Reliable@3 = 10.8%**; **stateful coordination is the dominant failure mode**, worsening with knowledge retrieval and mid-speech corrections.
- **Link**: https://arxiv.org/abs/2609.34973

### 4.9 FATA: Feature-Aware Token Attack for Compression-Triggered Stealthy Failures in Large VLMs
- **中文标题**: FATA：面向大型视觉语言模型中压缩触发隐蔽失效的特征感知 token 攻击
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **ICLR 2027** (submitted)
- **Problem background**: Visual-token compression improves efficiency but exposes failures full-token evaluation misses; crafting adversarial images that stay correct full-token yet fail compressed is hard because perturbing token importance also damages content.
- **Key innovation**: **FATA** couples **attention suppression** with **cosine-based feature preservation** on a fixed set of salient clean-image tokens; in LLaVA-1.5-7B it uses only **vision-encoder gradients**, with **no access to the compressor, token budget, or downstream task**.
- **Results / comparison**: Across four visually dependent subsets and four compressors under a controlled reconstruction protocol: **SR = 96.3%** full-token accuracy retention and **CBR = 22.1%** conditional blinding (vs 89.8%/15.7% for CAA); lowest measured detection rate among four attacks across three detectors at 5% FPR.
- **Link**: https://arxiv.org/abs/2609.39134

---

## 5. ICML 2026 (4 papers)

### 5.1 ARM: Attention with Routed-Memory for Learnable Sparse Control
- **中文标题**: ARM：面向可学习稀疏控制的路由记忆注意力
- **Authors**: (see paper)
- **Affiliation**: University of Toronto; Vector Institute; Université de Montréal; Mila; RIKEN AIP; Western University
- **Venue**: **ICML 2026** (accepted)
- **Problem background**: Selective token eviction/pruning manage the growing KV cache but discard core information.
- **Key innovation**: **ARM** — a fully differentiable, **fixed-size memory** organized as a hierarchical router; a **Gumbel-Softmax** selects memory slots and **sigmoid-gated updates** softly combine new/stored information (no hard eviction), while a learned policy dynamically selects how much memory to read at inference.
- **Results / comparison**: Superior performance and efficiency vs fixed KV-caching on commonsense and long-context reasoning benchmarks, scalable in memory and generation latency.
- **Link**: https://arxiv.org/abs/2609.24417

### 5.2 CE⁴L: Continual Ego, Exo, and Ego-Exo Learning
- **中文标题**: CE⁴L：持续自我、外部与自我-外部视角学习
- **Authors**: (see paper) — **AnAppleCore** group
- **Affiliation**: Tsinghua University (School of Life Sciences / IDG-McGovern; Dept. of Computer Science; Dept. of Psychological and Cognitive Sciences; IIIS)
- **Venue**: **ICML 2026** (accepted)
- **Problem background**: Embodied perception is multi-view (ego/exo/both) and continual with **simultaneous task and viewpoint shifts**, yet continual learning is dominated by exo-only recognition.
- **Key innovation**: **CE⁴L** — a unified multi-view CL benchmark over four tasks (cross-view referenced skill assessment, temporal action segmentation, cross-view association, action anticipation & planning) exposing cross-view correspondence, view-dependent asynchrony, and heterogeneous semantic objectives; proposes **VISTA** — parameter-efficient **subspace-routed task adapters** with training-free routing via residual distance to task-specific whitened subspaces.
- **Results / comparison**: Representative CL methods vary widely across CE⁴L settings; **VISTA is consistently competitive and achieves SOTA overall**.
- **Link**: https://arxiv.org/abs/2609.23492

### 5.3 QPT: Q-learning Penalized Transformer for Safe Offline Reinforcement Learning
- **中文标题**: QPT：面向安全离线强化学习的 Q 学习惩罚 Transformer
- **Authors**: (see paper)
- **Affiliation**: Shanghai Jiao Tong University; Sun Yat-sen University (Shenzhen); Jilin University; Nanyang Technological University
- **Venue**: **ICML 2026** (submission)
- **Problem background**: Safe offline RL must balance three competing objectives: satisfy safety constraints, maximize reward, and stay close to the behavior dataset.
- **Key innovation**: **QPT** — a **training–inference consistent** framework bridging conditional sequence modeling with constraint-aware value estimation: a Transformer policy conditions on trajectory context + target return/cost (strong behavior regularization), and sequence-model training is augmented with a **Q-shaped penalty** from learned reward/cost Q-functions; at inference the same Q-functions enforce the cost threshold and pick the highest-reward feasible action.
- **Results / comparison**: Consistently outperforms strong safe-offline-RL baselines across **38 tasks on the DSRL benchmark** and shows robust zero-shot adaptation to different constraint thresholds; with a principled analysis under near-deterministic CMDPs.
- **Link**: https://arxiv.org/abs/2609.34426

### 5.4 DISSOLVR: An Interpretable and Fast Framework for Aqueous and Organic Solubility Prediction
- **中文标题**: DISSOLVR：可解释且快速的水相/有机相溶解度预测框架
- **Authors**: (see paper)
- **Affiliation**: Indian Institute of Technology, Delhi, India
- **Venue**: **ICML 2026** (accepted)
- **Problem background**: Deep-learning solubility predictors sacrifice physical interpretability for power.
- **Key innovation**: **DISSOLVR** — a **transparent** framework mapping molecules to physically grounded descriptors; includes a literature review + benchmarking, an **LLM-assisted post-hoc explanation pipeline** bridging symbolic artifacts to chemical narratives, and an expert survey (**22 chemists**).
- **Results / comparison**: Approaches the **aleatoric limit of experimental uncertainty** and achieves OOD generalization via structural invariance — challenging the assumption that SOTA requires non-transparent architectures.
- **Link**: https://arxiv.org/abs/2610.02574

---

## 6. CIKM 2026 (3 papers)

### 6.1 CSC: Calibrated Simplicity for Conflict-Aware Social Bot Detection in the LLM Era
- **中文标题**: CSC：LLM 时代冲突感知社交机器人检测的校准简约框架
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **CIKM 2026** (accepted)
- **Problem background**: LLMs make social bots hard to detect from text alone (cheap, fluent semantic camouflage); the challenge is **modality conflict** — human-like semantically but suspicious in graph/profile/cross-modal consistency.
- **Key innovation**: **CSC** — a calibrated-simplicity framework: a simplified **prototype-guided graph expert** (retains useful structural biases, removes unstable heuristics), **calibrated simplex-constrained fusion** that aligns heterogeneous confidence spaces before late fusion, and a lightweight **inconsistency expert** modeling cross-modal disagreement.
- **Results / comparison**: On TwiBot-22, TwiBot-20, MGStBot-large, improves **calibrated operating-point decision quality** while staying competitive across external benchmarks; a semantic-camouflage stress test shows text-only evidence degrades while graph and fused evidence stay stable.
- **Link**: https://arxiv.org/abs/2609.23320

### 6.2 HyBrain: Spatiotemporal Hyperedges for EEG Seizure Detection and Prediction
- **中文标题**: HyBrain：面向 EEG 癫痫检测与预测的时空超边
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **CIKM 2026** (accepted)
- **Problem background**: Dynamic GNNs model EEG as per-time-step **pairwise** channel edges, missing the spatiotemporal coupling of a seizure at substantial training cost.
- **Key innovation**: **HyBrain** summarizes spatiotemporal EEG evidence through a small set of **soft hyperedges**: a per-channel **Mamba** backbone emits one token per (channel, second), and a hyperedge block pools tokens into shared group embeddings via soft memberships and broadcasts them back; the same encoder serves three tasks (window detection, one-second point-wise detection, preictal prediction).
- **Results / comparison**: On TUSZ and CHB-MIT, **best AUROC in every reported setting vs ten baselines** (largest gap on long-clip preictal prediction) while matching the most efficient baselines in training time and peak GPU memory; a single learned hyperedge captures the preictal→ictal→postictal trajectory.
- **Link**: https://arxiv.org/abs/2609.37730

### 6.3 BERT4DTI: BERT-based Model for Predicting Drug-Protein Interactions
- **中文标题**: BERT4DTI：基于 BERT 的药物-蛋白质相互作用预测
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **CIKM 2026** (accepted)
- **Problem background**: Sequence-based DTI models face scarce/uneven labels, expensive full fine-tuning of large encoders, and independent encoding missing pair-specific dependencies.
- **Key innovation**: **BERT4DTI** encodes SMILES with **ChemBERTa** and amino-acid sequences with **ProtBERT**, applies **bidirectional mutual attention** between token-level representations, and classifies with conv layers + MLP; ProtBERT is truncated to **18 layers** and only the **last two layers** of each encoder are fine-tuned (**125M trainable vs 353M** for full BERT).
- **Results / comparison**: On BIOSNAP, DAVIS, BindingDB: best ROC-AUC/PR-AUC on BIOSNAP, best sensitivity on all three; ablation shows mutual attention improves PR-AUC and specificity — a favorable performance/parameter trade-off.
- **Link**: https://arxiv.org/abs/2609.33254

---

## 7. ACL / NAACL 2026 (4 papers)

### 7.1 DUMA-Bench: A Dual-Control Multi-Agent Benchmark for Evaluating LLM Agent Security
- **中文标题**: DUMA-Bench：面向 LLM 智能体安全评测的双重控制多智能体基准
- **Authors**: (see paper)
- **Affiliation**: AI Security Lab, ITMO University; Hive Trace Lab; Independent Researcher
- **Venue**: **ACL** (ARR 2026 Findings)
- **Problem background**: Most agent security evaluations assume **passive users and static control**, ignoring the interactive dynamics that shape real behavior.
- **Key innovation**: **DUMA-Bench** — measures agent security under **dual-control** interaction (both agent and user influence shared environment state); extends τ²-bench with adversarial environments covering **eight vulnerability classes** (RAG poisoning, cross-agent manipulation, unsafe output handling, …).
- **Results / comparison**: **14 models from 5 families** (OpenAI, Anthropic, DeepSeek, Qwen, Z.ai) across 8 domains and multiple user-behavior regimes: dual-control interaction raises ASR from **26.9% → 41.1%** — agent security emerges from model×user×environment, not the model alone.
- **Link**: https://arxiv.org/abs/2609.24662

### 7.2 Strong Multilingual Privacy Tagging at Encoder Speed
- **中文标题**: 以编码器速度实现强多语言隐私标注
- **Authors**: (see paper)
- **Affiliation**: **RWS Language Weaver**
- **Venue**: **ACL** (Rolling Review, October 2026 cycle)
- **Problem background**: Privacy redaction must remove PII while preserving expressed relationships, and local LLM annotators are slow and weak.
- **Key innovation**: Fine-tunes a multilingual **encoder** with an affine span-tagging head on frontier-model annotations in **35 languages**, with coverage-aware masking on replayed human gold and a learned ±1-character boundary adjustment.
- **Results / comparison**: On 1,283 human-gold segments in 7 languages, best redaction **F1 = 88.8** vs **69.1** (GLiNER2), 67.8 (GLiNER2 retrained), 57.3 (Presidio), 35.8 (best published OpenAI Privacy Filter fine-tune); encoder delivers **4.9× GLiNER2's CPU throughput** (local LLMs encode 30–95× slower than XLM-R).
- **Link**: https://arxiv.org/abs/2609.38630

### 7.3 Constrained Decoding Eliminates Structural Failures in Small LLMs but Reveals a Scale-Dependent Semantic Gap
- **中文标题**: 约束解码消除小模型结构失败，却揭示随规模变化的语义鸿沟
- **Authors**: (see paper) — **CruiseDevice** group
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **ACL** (ARR-format preprint)
- **Problem background**: Small LLMs (0.6B–4B) are widely deployed for structured output (JSON, function calling, extraction), but how constrained decoding interacts with scale is unknown.
- **Key innovation**: Benchmarks 5 models from 3 families across **14 structured-output tasks** under three decoding conditions (native, Outlines, XGrammar), with a **two-axis evaluation** separating structural (schema validity) from semantic (content accuracy) correctness.
- **Results / comparison**: CD eliminates **all** structural failures (**78.6–92.9% → 100%** schema validity) but a **scale-dependent semantic gap** persists: type-coercion failures are CD-rescuable, while instruction-semantic failures (e.g. multi-step function calling) stay **CD-resistant** — CD's reach ends exactly where schema conformance ends.
- **Link**: https://arxiv.org/abs/2609.23742

### 7.4 Towards the Roof of the World: NLP Progress in Tibetan Languages
- **中文标题**: 走向世界屋脊：藏语自然语言处理进展
- **Authors**: (see paper)
- **Affiliation**: Minzu University of China (Philosophy/Information Engineering/National Security); National Language Resource Monitoring & Research Center — Minority Languages Branch; Xizang University; The State Key Laboratory of Tibetan Intelligence
- **Venue**: **ACL** (Findings of AACL-IJCNLP 2026, camera-ready)
- **Problem background**: Tibetan (~7M speakers) is underrepresented in NLP.
- **Key innovation**: First peer-reviewed systematic **bibliometric survey** of Tibetan NLP — **140 publications (2004–2026)** from ACL Anthology + DBLP, annotated for venue, research area, first-affiliation country, and resource release.
- **Results / comparison**: **84%** appeared since 2018; bottom-up expansion along the pipeline (corpora → segmentation → script → speech → applications → LLMs); China first-authored **87%**; **only 29%** release data/code/models; argues this full-pipeline paradigm is a reference model for other Global-South low-resource languages, and identifies dialect-coverage, responsible-NLP, and native-evaluation gaps.
- **Link**: https://arxiv.org/abs/2610.13398

---

## 8. CVPR 2026 / KDD 2025 Workshop (3 papers)

### 8.1 KASALv2: Fully Automatic 3D Rotational Symmetry Classification and Axis Localization
- **中文标题**: KASALv2：全自动 3D 旋转对称分类与轴定位
- **Authors**: Mengxin Zhang, Yulin Wang (equal); Chen Luo, Yijun Zhou (corresponding)
- **Affiliation**: School of Mechanical Engineering, Southeast University, Nanjing, China
- **Venue**: **CVPR 2026** (accepted)
- **Problem background**: Rotational-symmetry annotations for 3D objects are largely manual/semi-automatic, limiting scalability for 6D pose priors.
- **Key innovation**: A **fully automatic, reference-free** framework for symmetry-type classification, rotational-order identification, and **full-axis localization** across all **eight canonical 3D rotational symmetry types** (dominant high-order axis, self-consistency order inference, hierarchy-guided reconstruction); a texture-aware extension models appearance-induced order reductions.
- **Results / comparison**: **94.75%** accuracy on **438 symmetric objects in GSO**; training FoundationPose with these priors improves accuracy up to **0.9%** across five BOP datasets.
- **Link**: https://arxiv.org/abs/2610.09534

### 8.2 SatUnreal: A High-Precision Synthetic Dataset for Satellite Stereo Matching via Unreal Engine
- **中文标题**: SatUnreal：基于 Unreal Engine 的高精度卫星立体匹配合成数据集
- **Authors**: (see paper) — **jmp-Telepix** group
- **Affiliation**: **TelePIX**, South Korea
- **Venue**: **CVPR 2026 Workshop on EarthVision (CVPRW 2026)**
- **Problem background**: Satellite 3D reconstruction lacks high-fidelity training data with accurate occlusion labels; real benchmarks (US3D, WHU-Stereo) suffer spatio-temporal mismatch and ambiguous ground truth from LiDAR sparsity.
- **Key innovation**: **SatUnreal** — Unreal Engine simulation pipeline: **10,000 stereo pairs at 0.3 m GSD**, physical orbit simulation (varying baselines/azimuths), spatio-temporal consistency (fixed virtual environments), topographic diversity (urban canyons → low-texture terrain), and a two-step **linetrace** algorithm generating flawless occlusion masks.
- **Results / comparison**: Models trained **exclusively on SatUnreal** achieve superior **zero-shot** transfer to real benchmarks (US3D, WHU-Stereo) vs models trained on real data — physically accurate synthetic data is a better geometric supervisory signal than complex real observations.
- **Link**: https://arxiv.org/abs/2609.27442

### 8.3 SURE: Framework for Safety to Construct Trustworthy AI
- **中文标题**: SURE：构建可信 AI 的安全框架
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **KDD 2025** — 4th Workshop on Ethical Artificial Intelligence (EAI)
- **Problem background**: AI-safety criteria vary by country/culture/company policy, so a one-size framework is insufficient.
- **Key innovation**: **SURE** (Safe and Unified AI Framework foR Everyone) customizes AI-safety attributes: taxonomies of adversarial prompts, template-based desirable responses, an **absolute safety scoring** scheme, and staged **AI alignment** on the resulting datasets.
- **Results / comparison**: Demonstrated across various base models; provides a configurable safety-customization pipeline rather than a fixed rubric. (Paper contains harmful/offensive example text by design.)
- **Link**: https://arxiv.org/abs/2609.38249

---

## 9. AAAI / AAIA-AIES (3 papers)

### 9.1 ReproBench: Benchmarking LLM Agents on Reproducing Vulnerabilities From Scratch
- **中文标题**: ReproBench：从零复现漏洞的 LLM 智能体评测
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **AAAI 2027** (submitted)
- **Problem background**: Existing cybersecurity benchmarks operate under a **post-environment** paradigm (hand the agent source, container, or binary), bypassing environment reconstruction — so it is unknown whether an agent can reproduce a vulnerability **entirely from scratch**.
- **Key innovation**: **ReproBench** — evidence-grounded benchmark evaluating end-to-end reproduction **starting from a CVE identifier alone**, decomposing the workflow into **six phases** scored with verifiable artifacts (firmware images, unpacked binaries, analysis logs, validated crash samples); instantiated with **30 real-world IoT firmware vulnerabilities**.
- **Results / comparison**: **45.3%** of test runs resort to **vulnerability simulation** (a remediation shortcut adopted across all agents); only **5.3%** of CVE–model pairs actually reproduce real vulnerabilities — yet those confirm frontier agents already possess fully autonomous end-to-end capability.
- **Link**: https://arxiv.org/abs/2609.34450

### 9.2 Open Science, Closed Models: How Funding Shapes AI in Science
- **中文标题**: 开放科学、封闭模型：资助如何塑造科学中的 AI
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **AAAI/ACM AIES 2026** (accepted)
- **Problem background**: How funding shapes AI engagement in science is structurally important but poorly understood.
- **Key innovation**: Analyzes **104,226 papers (2018–2025)**, linking funding acknowledgments to how each paper engages with foundation models (extends / off-the-shelf use / peripheral reference). Three findings: both private and public funding associate with greater AI engagement (public → more off-the-shelf/open-weight use; private → more model extension); industry cloud credits associate with **less open-weight use**; industry involvement reaches science mainly via **coauthorship** (concentrated in CS and Global-North collaborations).
- **Results / comparison**: The cross-system gap is **control, not adoption** — the Global South (least publicly funded) has the highest API-only share (**0.4% → 10.0%**), while China shows the opposite (highest public-funding share, lowest API-only, stable extension).
- **Link**: https://arxiv.org/abs/2609.25347

### 9.3 Motif-Vocab: Statistically Calibrated TF-Identity Tokenization for Genomic Language Models
- **中文标题**: Motif-Vocab：面向基因组语言模型的统计校准转录因子身份分词
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **AAAI-27** (submitted)
- **Problem background**: DNA tokenizers use characters, fixed k-mers, or frequency-derived subwords without the specificity of DNA-binding regulatory factors.
- **Key innovation**: **Motif-Vocab** scans both strands for **statistically calibrated motif matches**, emits **transcription-factor identity tokens**, and applies nucleotide/k-mer/BPE to unmatched sequence; motif-specific null distributions put PWMs of different lengths/degeneracy on a common significance scale, with deterministic overlap rules.
- **Results / comparison**: In controlled BERT pretraining on **2B base pairs**, real motif libraries beat randomized-motif controls on **54 of 55** downstream tasks; on a motif-disjoint recognition task, TF-specific tokens improve macro-F1 by **0.040** over a position-matched generic motif token and **0.033** over a matched no-motif tokenizer — a targeted, interpretable inductive bias (not a universal replacement; dense no-motif tokenizers stay strong).
- **Link**: https://arxiv.org/abs/2609.28386

---

## 10. SIGMOD 2027 / ICDE 2027 — Data Systems (4 papers)

### 10.1 SALUS: Automated Auditing of NL-to-SQL Benchmarks through Weak Supervision
- **中文标题**: SALUS：通过弱监督多智能体输出自动审计 NL-to-SQL 基准
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **ACM SIGMOD 2027** (accepted; extended version)
- **Problem background**: Widely used NL-to-SQL benchmarks contain annotation errors that silently corrupt metrics and distort SOTA understanding.
- **Key innovation**: **SALUS** frames auditing as **weakly supervised error detection**: SQL from multiple LLM agents drives complementary **weak-labeling functions**; a generative label model on the noisy vote matrix extracts high-confidence samples without human ground truth, then a decision plane maps gold-SQL features to **per-agent trustworthiness**, fusing reliability estimates with raw verdicts.
- **Results / comparison**: On **BIRD-Clean-xs** (298 dev tasks with verified labels) reaches **F1 = 0.9194**, beating SOTA baselines; estimates annotation error rates of **~37% (BIRD)** and **~27% (Spider)**.
- **Link**: https://arxiv.org/abs/2610.05540

### 10.2 SHED: Robust Hierarchical Structures for Agentic Document Analysis
- **中文标题**: SHED：面向智能体文档分析的鲁棒层次结构
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **ACM SIGMOD 2027** (Proceedings of the ACM on Management of Data, to appear)
- **Problem background**: LLM agents treat hierarchical documents (PDF/Word) as flat text, ignoring section structure; prior structure extraction gives no formal guarantee of matching the true structure.
- **Key innovation**: Targets a **robust and compact** structure — robustness (each subsection's text is a *superset* of the true text under that header) plus compactness (minimize the superset to cut agentic cost) — and proposes **SHED**, a two-stage workflow whose first stage is pluggable with an infinite family of approaches (each guaranteeing robustness for a document class), with theoretical characterization of the document space.
- **Results / comparison**: Improves F-1 (robustness–compactness trade-off) by **13–68%** over non-LLM baselines and **9–15%** over expensive LLM approaches; agents using SHED-inferred structures are **3–23% more accurate** and up to **10× cheaper**.
- **Link**: https://arxiv.org/abs/2609.33322

### 10.3 Benchmarking Content-Defined Chunking Algorithms for Data Deduplication
- **中文标题**: 面向数据去重的内容定义分块算法基准
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **ICDE 2027** (accepted)
- **Problem background**: CDC algorithms are **modular** (a base chunker + layered size normalization / min-max thresholds / caching), but existing benchmarks conflate the two layers, obscuring which design choices drive performance.
- **Key innovation**: Isolates and evaluates **eight base chunking algorithms** across four workloads and four metrics (throughput, dedup ratio, mean chunk size, chunk-size variance); derives new formulas relating parameters to expected chunk size for AE, RAM, and MII.
- **Results / comparison**: Uncovers a **longstanding AE parameterization error** reproduced across papers/tools (chunks **13–39% smaller** than intended, inflating AE's reported dedup ratio); AE is the most balanced base algorithm, RAM's similarity to AE does not carry to low-entropy data, and MII/PCI show limited advantages in storage-oriented workloads. All implementations/data/scripts released.
- **Link**: https://arxiv.org/abs/2610.13704

### 10.4 WPBench: A Comprehensive Benchmark for Wind Power Forecasting
- **中文标题**: WPBench：面向风电功率预测的综合基准
- **Authors**: (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: **ICDE 2027** (accepted)
- **Problem background**: Existing wind-power forecasting benchmarks lack scenario coverage, model-family coverage, aligned metrics, and structure-aware diagnostics.
- **Key innovation**: **WPBench** integrates **26 public datasets** by turbine scale and variable composition (single/multi-turbine, univariate/multivariate), unifies processing/training/evaluation, and benchmarks **19 representative models** (traditional, deep temporal, spatio-temporal, foundation); beyond point error it assesses **forecast-curve fidelity**, computational efficiency, and **structure-aware diagnostics** (temporal/variable/spatial dependence).
- **Results / comparison**: Enables systematic cross-scenario comparison and a reusable platform for future wind-forecasting research.
- **Link**: https://arxiv.org/abs/2609.24444

---

## 11. RecSys / Ads / CTR / Personalization Lane (2 papers)

> ⚠️ **Lane disclosure (as in today's three siblings):** the newest indexed block (2026-10-09) again contains **no direct CTR-prediction or ad-serving architecture papers** — `abs`-level sweeps for "click-through rate", "CTR prediction", "advertising", "ad auction", "sponsored search", "sequential recommendation", "generative recommendation" surface adjacent material but **no new entrant for [[ctr-scaling-landscape]]**. The two papers below are the closest material, both **un-venued preprints**.

### 11.1 Privacy in Personalized AI Is a System Property, Not Just a Model Property
- **中文标题**: 个性化 AI 中的隐私是系统属性，而非仅模型属性
- **Authors**: (see paper)
- **Affiliation**: SJTU Paris Elite Institute of Technology; Kibo Ryoku Research
- **Venue**: (no venue tag — recent arXiv preprint)
- **Problem background**: In personalized AI (assistants, recommenders), users interact with **systems** that access, infer, and reuse user information across components and over time — so model- or component-level privacy analyses miss risks.
- **Key innovation**: Argues for a **system-level** privacy perspective; distinguishes and analyzes **four interconnected privacy-risk channels**, then proposes **four requirements** for system-level evaluation (interaction trajectories, internal information flows, indirect leakage, privacy–utility trade-off).
- **Results / comparison**: A position/argument paper calling for systematic incorporation of these requirements into privacy audits of personalized AI.
- **Link**: https://arxiv.org/abs/2609.38289

### 11.2 A Primal-Dual Approach to Randomized Online Bidding with Tail Constraints
- **中文标题**: 带尾部约束的随机在线竞价原始–对偶方法
- **Authors**: Alison Hsiang-Hsuan Liu, Fu-Hong Liu (see paper)
- **Affiliation**: *(affiliation not recovered from arXiv HTML)*
- **Venue**: (no venue tag — recent arXiv preprint)
- **Problem background**: Recent work imposes **tail constraints** (limiting the probability of poor outcomes) on randomized online algorithms; the randomized **online bidding** problem under such constraints is new.
- **Key innovation**: When tail constraints require **zero** probability of exceeding a threshold, determines the **optimal expected competitive ratio**; for general tail constraints allowing positive exceedance, derives a **parameter-dependent upper bound** on the optimal ratio, with a matching lower bound for the pure-tail case.
- **Results / comparison**: Advances a nascent tail-constrained online-algorithm theory; explicitly notes it builds on a Master's thesis and responds to independent work by Basiak et al. (preliminary version).
- **Link**: https://arxiv.org/abs/2610.05580

---

## 12. Empty Lanes & Collision Notes

- **Empty / thin this window:** the conventional "CTR-prediction architecture" lane again has **no entrant** — see §11 disclosure. No new venue-tagged entries surfaced for **EMNLP 2025, NeurIPS 2025, KDD 2026, SIGIR 2026, WWW 2026, RecSys 2025/2026, WSDM 2026, IJCAI 2026** main tracks in the 2026-09-20→2026-10-09 block (their recent proceedings were covered by earlier 2026-09/10 digests). SIGMOD/ICDE items are tagged **2027**.
- **IDs dropped at the 0-hit gate** (appear *somewhere* in the wiki — featured or merely *mentioned* by earlier digests, so excluded per protocol): `2610.12242` (TokenRouter), `2610.12030` (NL→FOL autoformalization — consciously deferred by the 10-11 digest), `2609.27297` (Large Knowledge Model), `2609.23780` (Falling Trees), `2609.28972` (CMRec), `2609.25542` (DefaultGNN), `2609.28980` (Seek), `2609.33073` (KDD OARS algorithmic harms), `2610.00425` (REXRepro — deferred by 10-11), `2609.33045` (RecSys Challenge 2026), `2609.30568` (Nearest but Not Dearest — featured 09-28), `2610.07663` (SWORD — featured 10-07). No acronym/name-collision defects found beyond these ID-level hits.
- **Collision bookkeeping:** dedup baseline **8,730 claimed arXiv IDs** (bare-ID scan, built *after* today's siblings were staged); all **60 featured IDs `rg -l` 0-hit** immediately before write. Acronym collisions: none found.
- **Same-window siblings for cross-reading:** [[arxiv-daily]] (50 papers, `2610.13948` Wikipedia Game → `2610.13407` PC-LinUCB), [[arxiv-paper-check]] (17 papers, `2610.13066` ECC → `2610.13778` ReplaySSM), [[tech-report-digest]] (Ai2 Olmo Hybrid / Bolmo, Cloudflare Clef-omni).

---

## 13. Follow-ups

1. **Diffusion-as-substrate is now 5-strong this block** (ChemDiffAgent, PDFM, CFG-Information-Bottleneck, LSP graph diffusion, GDM memorization) — and two of them **audit the independent-edge-update mechanism** from opposite sides. Before the next digest, consider a synthesis page tying the graph-diffusion prior critique (LSP) to the memorization finding (§2.3) and this wiki's earlier diffusion/flow-matching threads.
2. **Inference-time control is the through-line of the window** (dynamic CFG activation, KVFetch temporal recall, ARM routed memory, softmax reparameterization, AIM-ZO subspace maintenance): five papers that buy capability at serving time rather than training time. Candidate synthesis: [[inference-time-control]].
3. **Evaluator/benchmark-validity instruments keep stacking** (LongSocialBench, sk-bench, LASEF, DUMA-Bench, SALUS's ~37%/27% annotation-error estimate, ReproBench, SWE-Duel's self-scaling arena). This is the same "who audits the auditor" arc flagged by the 10-11 digest — a [[benchmark-validity-instruments]] page would consolidate it.
4. **Recsys/ads lane continuity:** the privacy-as-system-property position paper (§11.1) and tail-constrained online bidding (§11.2) are both deploy-relevant theory; flag for the next industry-heavy digest where CTR-architecture entrants remain scarce.
