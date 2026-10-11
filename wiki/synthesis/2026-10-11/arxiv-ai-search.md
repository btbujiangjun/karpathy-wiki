---
title: arXiv AI Search (Recent) - 2026-10-11
type: synthesis
created: 2026-10-11
updated: 2026-10-11
sources: []
tags: [arxiv, ai, llm, recommendation, advertising, sequential-modeling, ctr, games, ml]
---
# arXiv AI Search - Recent Papers (2026-10-11)

Search scope: the export API's latest indexed announcement block is still **2026-10-08 (Thu)** — `submittedDate:[20261009 TO 20261012]` returns 0, so this run sweeps **2026-10-05 → 2026-10-08** across `cs.AI`, `cs.LG`, `cs.CL`, `cs.IR`, `cs.GT`, `cs.MA` plus 30 topical `all:` queries. **1,330 unique papers** harvested; **983 are new to the wiki** (grep-verified against 8,531 repo-wide arXiv IDs, after excluding the 49 papers today's `arxiv-daily` digest features). All papers below are **new to the wiki** and **not claimed by the same-day digest**.

> ⚠️ Metadata note: the arXiv Atom API does not expose author affiliations. **Institution/company** is stated only where the abstract, comments, or code link name one; otherwise `not stated (arXiv metadata omits affiliations)`, with a `-adjacent author list; unconfirmed` hint where the author list strongly suggests a lab without stating it.

> ℹ️ Lane note: as in the sibling digests, the **CTR / ad-serving / recommender** lanes are effectively empty in this block — no direct CTR, advertising, or ad-auction paper surfaced in `abs:`-field sweeps. The closest material is assortment curation theory (§1), ranking/retrieval (§4), and credit-risk cold-start ranking (§5).

## Core AI / LLM / Agents

### 1. Universal Textual Teaching for LLMs (UTT)
- **Authors**: Zhanyi Lu, Huan Wang
- **Institution**: not stated (arXiv metadata omits affiliations); webpage: alexlu99.github.io/UTT
- **Subjects**: cs.AI
- **Abstract**: Knowledge distillation usually requires training Student parameters, binding distilled knowledge to one architecture/checkpoint and blocking API-only or costly models. UTT instead distills observed Teacher–Student knowledge gaps into a **textual, interpretable, reusable artifact (Primer)** — no parameter updates.
- **Key innovations**: A multi-role loop (Student attempts → Prompter turns feedback into teaching instructions → Teacher demonstrates → Synthesizer consolidates validated lessons) iteratively refines the Primer. Raises Student accuracy 9.4%→48.6% on KernelBench and fast-1 9%→35%, math reasoning 27.6%→51.7% on Omni-MATH-2, beating prompt engineering and parameter-based KD; a Primer for one pair generalizes to unseen Students.
- **arXiv**: https://arxiv.org/abs/2610.12114

### 2. Plan-and-Patch: Diffusion Language Models for Agentic Planning
- **Authors**: Syamantak Kumar, Jiang Guo, Hassan Hamad, Hideo Kobayashi, Yi Xiang, Yezhou Yang, Yanjun Qi, Daniele Bonadiman, Jiarong Jiang
- **Institution**: not stated (industry+academic author list; unconfirmed)
- **Subjects**: cs.AI; cs.CL; cs.LG
- **Abstract**: Assumptions made during planning get invalidated by the environment, so agents must not only generate plans but **repair** them. Regenerating the whole plan risks unnecessary changes; repair should regenerate only the affected region conditioned on the preserved prefix/suffix.
- **Key innovations**: Plan-and-Patch: a diffusion LM (dLLM) generates structured program-like plans through parallel unmasking and repairs selected regions in-place. On Natural Plan (no task training) diffusion repair success (53.7%) is ~2× autoregressive (27.0%); after agentic-task training it matches AR generation success while cutting plan-generation latency 39–46%.
- **arXiv**: https://arxiv.org/abs/2610.10786

### 3. EvoAlloc: A Self-Evolving Resource Allocation Agent for Efficient Program Evolution
- **Authors**: Yanning Dai, Yuhui Wang, Nanbo Li, Wenyi Wang, Jürgen Schmidhuber
- **Institution**: not stated (Schmidhuber-adjacent author list — likely KAUST/IDSA; unconfirmed)
- **Subjects**: cs.AI
- **Abstract**: LLM-based program evolution uses expensive evaluation feedback to guide search, but existing methods keep fixed allocation strategies, wasting compute on low-value candidates while overlooking promising ones.
- **Key innovations**: EvoAlloc learns to revise its resource-allocation strategy from search experience, plus **counterfactual exploration** (occasionally evaluating candidates denied resources to enrich experience). Cuts full evaluations 59–82% and LLM tokens 61–89% to reach baseline-level performance; +8.7–12.0% final performance under matched evaluation budget.
- **arXiv**: https://arxiv.org/abs/2610.12086

### 4. DuplexAgent-RSI: Recursive Harness Improvement for Full-Duplex Voice Agent Collaboration
- **Authors**: Yingda Shen, Yuxiang Wang, Kunyu Feng, Qinke Ni, Jiaqi Li, Minghao Hsu, Junan Zhang, Dekun Chen, Yutong Bian, Zhizheng Wu
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI; cs.SD
- **Abstract**: Voice agents are converging on full-duplex live interaction with asynchronous delegation of reasoning/tool work, but the coordinating harness uses coupled heuristics that are hard to improve from evidence.
- **Key innovations**: DuplexAgent expresses the harness as six editable modules; Duplex-Harness-RSI closes a loop that auto-generates timed test conversations, produces failure traces diagnosing which modules to repair, and uses the same reasoning/agent delegation pool to propose module edits. Beats the initial harness and repeated editing without diagnosis/repair archive; strong spoken-knowledge and executable-tool scores.
- **arXiv**: https://arxiv.org/abs/2610.11299

### 5. Incremental Open-Ended Deep Research with Structured Harness
- **Authors**: Meilin Chen, Hongyuan Bao
- **Institution**: not stated (arXiv metadata omits affiliations); project: ioedr-project.github.io
- **Subjects**: cs.CL
- **Abstract**: Open-Ended Deep Research (OEDR) regenerates reports from scratch, which is inefficient when reports must be continuously maintained as new information arrives.
- **Key innovations**: Incremental-OEDR treats a report as an evolving research state, with a **Structured Harness** (outlines/sections/evidence, structured retrieval + persistent evidence pool + structured generation) for selective updating. Temporal eval across ten years (Single-Step / Long-Chain tasks): up to +0.51 ROUGE-L F1 and +0.63 outline EM F1 over re-generation, 33% lower tokens, 61% fewer search calls.
- **arXiv**: https://arxiv.org/abs/2610.11566

### 6. LiveMACE: Process-Aware Evaluation of LLM Agent Capabilities in Evolving Markets
- **Authors**: Jun Zhao, Leiming Fu, Yanbo Wen, Yiding Wang, Xuantong Liu, Yang Shu, Yuyang Lu, Xuanran Xing, Jingqi Tong, Hao Xu, Qi Zhang, Xuanjing Huang
- **Institution**: not stated (Fudan-adjacent author list; unconfirmed)
- **Subjects**: cs.AI; cs.CL
- **Abstract**: Evaluating agents by outcomes alone obscures the capabilities that produce them, especially in evolving environments where outcomes reflect agent×environment interaction.
- **Key innovations**: LiveMACEBench uses live financial markets as a naturally evolving testbed: five frontier LLMs run 30 days with matched Tool Use / Persistent Memory / Rule Following / Multi-Agent Collaboration configs, evaluated by realized outcomes **and** trace-derived mechanism diagnostics. Finds a pronounced outcome–capability gap: access, effective use, and downstream performance are not interchangeable measures of capability.
- **arXiv**: https://arxiv.org/abs/2610.09872

### 7. From Pareto to Preference: Personalized Test-Time Scaling via Amortized Agentic Policy Discovery
- **Authors**: Xinglin Wang, Zishen Liu, Tong Zheng, Shaoxiong Feng, Peiwen Yuan, Yiwei Li, Jiayi Shi, Yueqi Zhang, Chuyi Tan, Ji Zhang, Boyuan Pan, Kan Li
- **Institution**: not stated (industry+academic author list; unconfirmed)
- **Subjects**: cs.CL; cs.AI
- **Abstract**: Test-time scaling (TTS) is usually optimized along one resource axis at a time, but user requirements are multidimensional (accuracy, latency, cost jointly) and different profiles favor different controllers.
- **Key innovations**: Formulates Personalized TTS as discovering controllers maximizing joint requirement satisfaction; PersonTTS amortizes repeated discovery via **requirement-matched controller initialization** and source-distilled procedural guidance. On AIME/HMMT, beats strong TTS baselines in joint-satisfaction on unseen user profiles; experience reuse cuts discovery-agent time/cost substantially.
- **arXiv**: https://arxiv.org/abs/2610.09684

### 8. Curating Always-Loaded Context for LLM Agents: A Capacitated Assortment Model with Censored Feedback
- **Authors**: Zexuan Liu, Yuning Yang, Tiancheng Zhao
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.AI; cs.LG; math.OC
- **Abstract**: Agents load a fixed context file (e.g. `AGENTS.md`) every session; every token is re-charged and large files degrade compliance, yet curators mostly append. Context curation is a **capacitated assortment problem** with finite attention capacity and per-session setup cost.
- **Key innovations**: Proves an upper bound on optimal file size regardless of candidate count, and that appending every positive-value instruction is arbitrarily worse than selecting an optimal subset. With **censored feedback** (harm from absent instructions only observed when it occurs), characterizes how much evidence to collect before adding an instruction and bounds regret under limited human review; confirms irrelevant rules lower LM compliance empirically. (Assortment/constrained-optimization theory directly transferable to recommender/serving curation.)
- **arXiv**: https://arxiv.org/abs/2610.11007

### 9. Prior or Feedback? What an LLM Uses When Adapting Neural Operators
- **Authors**: Julian Chan, Javier Mora Jimenez
- **Institution**: not stated; venue: NeurIPS 2026 Workshop on AI for Science: Verification in the Age of AI Scientists
- **Subjects**: cs.AI; cs.LG; physics.comp-ph
- **Abstract**: Do LLM scientific agents rely only on initial context, or adapt to experimental feedback? Studied in neural-operator adaptation where an LLM picks fine-tuning configs under a limited trial budget.
- **Key innovations**: LLM beats random search and Bayesian optimisation on held-out test nRMSE in nearly every matched comparison across PDE families. Controlled interventions separate the sources: the first configuration already ranks near the top of the random pool (useful prior), base learning rate shifts with PDE description, and reassigning validation scores changes the next proposal in every tested case (genuine feedback sensitivity).
- **arXiv**: https://arxiv.org/abs/2610.12325

## Reasoning / RL / Post-Training / Test-Time Compute

### 10. All Verdicts are Not Equal: Rethinking LLM Judge Reliability
- **Authors**: Vineet Kumar, Darshita Rathore, Anindya Moitra
- **Institution**: not stated; venue: AACL-IJCNLP 2026 (Main)
- **Subjects**: cs.CL; cs.AI
- **Abstract**: LLM-as-a-Judge is treated as deterministic ground truth, but its systemic reliability is poorly understood. Stress-test of six frontier models across 4 benchmarks, 5 prompt formats, 2 presentation orders, 3 temperatures, 10 reps.
- **Key innovations**: Introduces the **trustworthy verdict rate (Ṟ)**, the joint probability that an evaluation is reproducible, order-invariant, and accurate; derives an accuracy upper bound imposed by position bias; shows reliability is item-specific, not model-level. Verdicts change at temperature 0; position swaps flip most verdicts on hard tasks; holistic rubric scoring beats any single-format prompting fix.
- **arXiv**: https://arxiv.org/abs/2610.12083

### 11. The Long Road to the Same Answer: Cognitive Bias Under Escalating Reasoning Budgets in LLMs
- **Authors**: Obada Kraishan
- **Institution**: not stated; venue: IEEE CogMI 2026
- **Subjects**: cs.CL
- **Abstract**: If longer thinking works like dual-process deliberation, it should weaken classic decision biases. A dose-response study over 30 vignettes (6 biases), 4 model families with matched reasoning/non-reasoning siblings, thinking ceilings 0→8192 tokens, 12,350 API calls.
- **Key innovations**: Reasoning models are **not** less biased than siblings; bias magnitude does not reliably fall with realized deliberation (no significantly negative slope). Anchoring is the only bias in the human direction (d=1.89); four of five others lean opposite in all seven models. A one-line anchor-restatement instruction beats any amount of added thinking (p=.057). Argues against test-time reasoning as a rationality guarantee.
- **arXiv**: https://arxiv.org/abs/2610.10049

### 12. Collaborative Reasoning Distillation via Cross-Feedback and Coherent Curation (CRD)
- **Authors**: Taehoon Kim, Seunggeun Cho, Dongsu Han
- **Institution**: not stated (KAIST-adjacent author list; unconfirmed); venue: NeurIPS 2026
- **Subjects**: cs.LG; cs.AI; cs.CL
- **Abstract**: Distilling reasoning to small models is hard when outcome-based rewards cannot separate sound reasoning from lucky guesses.
- **Key innovations**: CRD: (1) interactive cross-feedback where teachers critique each other's reasoning, (2) step-wise quality assessment independent of final answers, (3) coherence-aware step stitching. Trained with Reasoning Quality Optimization (RQO) under budget constraints, CRD-4B hits 97.3% MATH-500 / 70.3% AIME'25 using only 50K examples (up to 12× smaller datasets).
- **arXiv**: https://arxiv.org/abs/2610.09587

### 13. The Dichotomy Between Pattern Recognition and Step-by-Step Reasoning
- **Authors**: Amrut Nadgir, Pratik Chaudhari, Vijay Balasubramanian
- **Institution**: not stated (UPenn/NEC-adjacent author list; unconfirmed)
- **Subjects**: cs.LG; cond-mat.dis-nn
- **Abstract**: Argues pattern recognition and step-by-step reasoning are two ends of a spectrum determined by how much preceding context the next token depends on.
- **Key innovations**: Framing reasoning traces as paths on a **De Bruijn graph** (nodes=c-length contexts, edges=next-token transitions). Proves edges are vanishingly small vs. trace count, so learning to reason step-by-step is sample-efficient (power law in edge count). Frequent states (small c) → higher accuracy but more test-time fragility; Qwen3-14B/32B retain >75% accuracy on GSM8K/MATH-500/GPQA when attention is restricted to a window <15% of the trace.
- **arXiv**: https://arxiv.org/abs/2610.09186

### 14. Quantifying the Stability of Multi-Step Reasoning via Error Amplification
- **Authors**: Dongyue Li, Ziniu Zhang, Minxuan Duan, Hongyang R. Zhang
- **Institution**: not stated (college-adjacent author list — UBC/UIUC hint; unconfirmed); venue: NeurIPS 2026
- **Subjects**: cs.LG; cs.AI; stat.ML
- **Abstract**: Errors from intermediate steps accumulate in autoregressive reasoning. What determines the stability of multi-step reasoning?
- **Key innovations**: Inference error bound governed by the product of spectral norms of input-space Jacobians across steps (an **error amplification factor** that can be exponential in steps). Theoretically shows transformers trained on linear/quadratic tasks converge to low-stability solutions (near-zero error over arbitrarily long chains); derives chain-of-thought length compression and quantization-aware regularization from the analysis (+3.5% avg / +8.2% on longer inputs; stability measure down 3–8×).
- **arXiv**: https://arxiv.org/abs/2610.06404

### 15. LoGRA: Scaling LLM Reinforcement Learning with Low-Rank Gradient Sketches
- **Authors**: Shaokun Zhang, Yifan Zhang, Jian Hu, Yueying Li, Hao Zhang, Binfeng Xu, Jan Kautz, Yi Dong
- **Institution**: not stated (NVIDIA/UIUC-adjacent author list; unconfirmed); code in the Molt library
- **Subjects**: cs.CL
- **Abstract**: RL post-training's memory demands are a barrier to broader adoption, especially for larger models.
- **Key innovations**: LoGRA keeps useful learning signal in **low-rank gradient sketches** supporting both model updates and policy sync, plus **predicted-KL step control** to prevent overly large updates. Cuts average training memory up to 45.7% without performance loss; enables stable RL of a 27B model for 1,100+ steps on a single 8-GPU node where dense Adam OOMs.
- **arXiv**: https://arxiv.org/abs/2610.06647

### 16. Dynamic Minimax Regret Optimization for Robust LLM Post-Training (DUCB-OGD)
- **Authors**: Chengbo Zang, Haoyu Dong, Mehmet Kerem Turkcan, Gil Zussman, Zoran Kostic, Javad Ghaderi
- **Institution**: not stated (Columbia-adjacent author list; unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: Group-DRO post-training under mini-batch-only bandit feedback, where source losses evolve with training but history is never re-evaluated.
- **Key innovations**: Formulates a two-player sampler–optimizer process and proposes DUCB-OGD: a Discounted UCB sampler with EMA loss estimates and discounted effective sample sizes coupled to online gradient descent. Proves dynamic minimax regret Õ(K^¼ T^¾) — optimal up to log factors. Integrates into SFT, preference optimization, and RL pipelines, improving worst-group robustness at negligible overhead.
- **arXiv**: https://arxiv.org/abs/2610.06329

### 17. Transfer-Stratified On-Policy Distillation for RL-Improved Reasoning Teachers (TS-OPD)
- **Authors**: Xiaoyu Chen, Bo Shao, Tiangang Zhu, Bintao Wu, Linjun Shou, Fengge Wu, Feng Sun, Wenbiao Ding
- **Institution**: not stated (industry author list; unconfirmed)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: An RL-improved reasoning teacher should help a smaller on-policy student, but it is unclear which teacher improvements actually transfer. Central finding: transfer is **structured rather than scalar** — teacher strength alone doesn't make dense distillation competitive.
- **Key innovations**: TS-OPD screens problems by joint sampled success, routes acquisition problems to gated forward KL and consolidation problems to gated reverse KL, with an entropy brake. Strongest student objective in macro-avg correctness with a GRPO-improved teacher; gains come from routing/token gating, not skipping problems. Supports a transfer-aware view of OPD.
- **arXiv**: https://arxiv.org/abs/2610.05974

### 18. RELACE: Retrospective Likelihood-based Action Credit for Long-Horizon Language Agents
- **Authors**: Sayak Chakrabarti, Sathish Reddy Indurthi
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: For multi-turn agents, GRPO's trajectory-level supervision is coarse and noisy — terminal rewards don't locate errors.
- **Key innovations**: RELACE scores executed actions by teacher-forced likelihood under original vs. outcome-augmented contexts, deriving a trajectory-normalized retrospective factor that reweights discounted returns to build local state-conditioned advantages (no value/reward model, no extra rollouts). Qwen2.5-1.5B: 96.35% ALFWorld / 79.43% WebShop, +5.47/+5.60 pts over GiGPO.
- **arXiv**: https://arxiv.org/abs/2610.07349

### 19. Higher-Order Action Supervision Makes A Strong Policy Class
- **Authors**: Peng Cheng, Yunxian Hou, Zhi Zhou, Qian Zhang, Chang Huang, Xianyuan Zhan
- **Institution**: not stated (Tsinghua-adjacent author list; unconfirmed); venue: NeurIPS 2026
- **Subjects**: cs.RO; cs.AI
- **Abstract**: Imitation/reinforcement learning supervise only zeroth-order actions, ignoring action dynamics and temporal consistency — a key source of control instability in robotics/autonomous driving.
- **Key innovations**: A loss scheme with formal guarantees supervises zeroth- **and** first-order actions on any policy model (deterministic, stochastic, flow) with no structural changes. Plug-and-play module for offline RL frameworks; large gains on OGBench/D4RL including better OOD generalization in low-data regimes.
- **arXiv**: https://arxiv.org/abs/2610.11175

## Efficiency / Inference / Serving / Compression

### 20. DVD: Dynamic Vector Decoding for Efficient MLLM-based Perception
- **Authors**: Jinghua Hou, Zhe Liu, Hengshuang Zhao
- **Institution**: not stated (HKU-adjacent author list; unconfirmed)
- **Subjects**: cs.CV; cs.AI
- **Abstract**: MLLM perception uses text-based coordinates (token-heavy) or fixed-range quantization (range/precision limits, especially in unbounded 3D).
- **Key innovations**: DVD unifies 2D/3D perception into a dynamic vector decoding scheme: representations are transformed into 1D vector sequences mapped to compact discrete tokens, decoded by a lightweight de-tokenizer. On RefCOCO/SUN-RGBD/KITTI/Hypersim/nuScenes it achieves superior 2D/3D performance with significantly lower token overhead and latency.
- **arXiv**: https://arxiv.org/abs/2610.12266

### 21. Activation-Aware Weight Tensorization (AWT): A Calibration-Time Preconditioner for Tensor-Network LLM Compression
- **Authors**: Alessandro Beatini, Marco Maronese, Emanuele Rodolà
- **Institution**: not stated (Sapienza-adjacent author list; unconfirmed)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Post-training tensor-network compression minimizes weight-space Frobenius error instead of functional error under the layer's activation distribution.
- **Key innovations**: AWT is a training-free calibration wrapper that preconditions each weight with a diagonal activation-derived scale before an unchanged TT/TTN solver, deployed with input-side rescaling only. At 2–6× compression across Llama 3.1 8B / Ministral 8B / Qwen2.5 7B it closes 12–35% of the WikiText perplexity gap (single-operator), 27–60% (multi-operator); gains transfer to HellaSwag/ARC. Shows diagonal preconditioning is a robustness–modularity tradeoff, not an assumption.
- **arXiv**: https://arxiv.org/abs/2610.10085

### 22. AlignQuant: Tile-Aligned Mixed-Precision Quantization for Efficient LLM Generation
- **Authors**: Hanzhi Zhang, Qiao Zhang, Qinglei Cao, Heng Fan, Yan Huang, Kewei Sha, Yunhe Feng
- **Institution**: not stated (academic author list; unconfirmed); code: github.com/HanzhiZhang-Ulrica/AlignQuant
- **Subjects**: cs.LG; cs.AI; cs.CL
- **Abstract**: Fine-grained mixed-precision goals conflict with regular GPU storage/compute units — precision-boundary mismatch limits practical acceleration.
- **Key innovations**: Uses GPU-compatible 2D weight tiles as the common unit of precision allocation, storage, and execution, with phase-normalized prefill/decode joint calibration and phase-specialized kernels (lower-bit expansion to INT8). Up to 2.50× generation speedup over BF16 across 3–14B models on three GPUs, at up to 64K context, while preserving quality.
- **arXiv**: https://arxiv.org/abs/2610.07457

### 23. Align, Then Correct: Training-Free Two-Stage Low-Rank Compensation for Extremely Quantized LLMs
- **Authors**: Seobin Song, Geonho Lee, Janghwan Lee, Jungwook Choi
- **Institution**: not stated (Hanyang-adjacent author list; unconfirmed)
- **Subjects**: cs.LG; cs.CL
- **Abstract**: Low-rank quantization-error compensation recovers accuracy under aggressive weight quantization, but existing compensators calibrate symmetrically (yielding a high-rank target) and minimize only the second-order term while a first-order signal remains.
- **Key innovations**: Two-stage closed-form framework: Stage 1 aligns layer outputs under a **Fisher-weighted asymmetric objective** (concentrating rank on a compressible target), Stage 2 re-measures on the compensated model and applies a rank-constrained natural-gradient step; each adapter is one truncated SVD. At 2 bits under QuIP#: Qwen3-8B WikiText-2 12.43→10.26 perplexity; recovers 51–84% of the FP16 gap on C4 vs 31–63% for the strongest baseline.
- **arXiv**: https://arxiv.org/abs/2610.08164

### 24. OrBIT: Structure-Guided Embedding Compression
- **Authors**: Yunied Puig, Amit Kumar Jaiswal
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.LG
- **Abstract**: Embedding tables are among the largest components of modern LMs; most compression fixes a coding geometry (blocks, low-rank, codebooks) and optimizes within it.
- **Key innovations**: OrBIT learns reusable local geometry from **orbit dynamics** to constrain shared codewords, with the global reconstruction residual directing capacity allocation and overlapping charts letting local errors compensate. Achieves 37.9× compression on GPT-2 and >23× on 7B tables vs 16-bit, with competitive rate-distortion vs quantization and low-rank baselines.
- **arXiv**: https://arxiv.org/abs/2610.10385

### 25. How Much Audio Is Left In An Embedding? An Inversion Audit Of Audio Encoders
- **Authors**: Marios Glytsos, Brian McFee
- **Institution**: not stated (NYU-adjacent author list; unconfirmed)
- **Subjects**: cs.SD; cs.AI
- **Abstract**: Pretrained audio encoders are reused for unknown downstream tasks, so usefulness depends on which signal properties survive the pretext objective.
- **Key innovations**: Paired source reconstruction of 5s/44.1kHz stereo music from frozen representations (VGGish, ConvNeXt, CLAP, EnCodec) via a shared Stable Audio Open latent diffusion decoder, evaluated on Million Song Dataset. Clear reconstructability differences across objectives, with improvements when finer temporal/spectral structure is exposed; even task-oriented embeddings preserve measurable source specificity.
- **arXiv**: https://arxiv.org/abs/2610.12250

## Information Retrieval / Retrieval / Ranking

### 26. Towards Explaining Query Expansion Performance in Information Retrieval
- **Authors**: Sourav Saha, Aditya Dutta, Soumajit Pramanik, Mandar Mitra
- **Institution**: not stated (ISI Kolkata-adjacent author list; unconfirmed)
- **Subjects**: cs.IR; cs.CL
- **Abstract**: No single Query Expansion (QE) method beats others on all queries; why?
- **Key innovations**: Two lenses — the **Ideal Expanded Query (IEQ)** (hypothetical query maximizing BM25 effectiveness) and a **separability perspective** (Cohen's d between relevant/non-relevant score distributions). On TREC Robust + DL 2019–2022, expanded queries closer to IEQ achieve higher effectiveness, and separability is a complementary predictor of QE performance.
- **arXiv**: https://arxiv.org/abs/2610.09724

### 27. From Chunks to Functional Evidence: Function-Aware Retrieval for EDA Documentation QA
- **Authors**: Xiaotian Qiu, Kairui Liu, Shi Chenyi, Jinyuan Deng, Qi Sun, Cheng Zhuo
- **Institution**: not stated (Zhejiang University-adjacent author list; unconfirmed)
- **Subjects**: cs.IR; cs.AI
- **Abstract**: In EDA documentation, answers depend on information scattered across heterogeneous but tightly coupled artifacts — the bottleneck is how knowledge is organized for retrieval, not model reasoning.
- **Key innovations**: Redesigns the retrieval unit: typed artifacts are collected into **EDA functional units** (hyperedges over source chunks), an encoder aligns queries to units, and unit+chunk retrieval feeds a unified reranker. New EDADocEval-QA dataset: +37.1% ROUGE-L over Chunk RAG, +55.6% over the strongest graph baseline; +30.0% on ORD-MMBench.
- **arXiv**: https://arxiv.org/abs/2610.09361

### 28. DBRAG: Multi-Table Retrieval-Augmented Generation for Complex Database Queries
- **Authors**: Prince Larbi Ampofo, Ryoji Kubo, Djellel Difallah
- **Institution**: not stated (NYU Abu Dhabi-adjacent author list; unconfirmed)
- **Subjects**: cs.IR
- **Abstract**: Many table-reasoning methods assume a single table or given relevant tables; real queries span multiple relations in an entire database.
- **Key innovations**: DBRAG retrieves candidate tables via an offline index, enriches summaries with query-relevant rows, LLM-reranks, then a program-aided reasoner selects tables and executes over full contents with compact prompts. Improvements in table retrieval and multi-table QA on Spider, GeoQuery, ATIS.
- **arXiv**: https://arxiv.org/abs/2610.07622

### 29. Your Prompt Should Do More: Effects of Retrieval Instructions in Embedding Models
- **Authors**: Amanda Myntti, Jenna Kanerva, Veronika Laippala, Filip Ginter
- **Institution**: not stated (University of Turku-adjacent author list; unconfirmed)
- **Subjects**: cs.CL
- **Abstract**: Prompted embedding models often struggle to follow detailed retrieval instructions when tested reliably.
- **Key innovations**: Shows models fail even simple task instructions when query-side distractors are present; blames the training/eval setup, and shows fine-tuning with added query-side distractors gives substantial instruction-following gains with minimal impact on other tasks.
- **arXiv**: https://arxiv.org/abs/2610.10508

### 30. T-Search: An Open Agentic Retriever and Playground for Hard Multi-Step Search
- **Authors**: Olga Tsymboi, Ramil Latypov, Aleksandr Medvedev, Danil Taranets, Dmitrii Stoianov, Nikita Gulyakov, Gleb Alektorov, Anatolii Potapov
- **Institution**: not stated (Russian industry author list; unconfirmed)
- **Subjects**: cs.CL
- **Abstract**: Hard multi-step search requires an agentic retriever that returns ranked evidence with justifications, leaving answer generation to a swappable backend.
- **Key innovations**: T-Search (Qwen3.6-35B-A3B base) trained on adversarially filtered synthetic search tasks with round-sliced SFT + GSPO on recall. Recall@10 56.0 with one rollout (+14.4 over base), 61.3 with three fused rollouts across seven EN/RU benchmarks; releases model, harness, demo, and TRuST (first native-Russian hard-search benchmark).
- **arXiv**: https://arxiv.org/abs/2610.06782

## Sequential Modeling / Time Series

### 31. Multimedia Identity-Aware Prism Network (MIDAPN) for Media-Bridged Time Series Forecasting
- **Authors**: Jierui Lei, Wenjian Zhang, Qingyi Yang, Yuyang Hong, Fangzheng Chen, Zhengbo Zhang, Haina Tang, Shiming Xiang
- **Institution**: not stated (CAS-adjacent author list; unconfirmed); code: github.com/MIDAPN
- **Subjects**: cs.CV; cs.LG
- **Abstract**: Media-bridged time series forecasting now spans numeric multivariate signals and narrative multimodal flows, but models still use paradigm-specific modules, blocking a common backbone.
- **Key innovations**: MIDAPN — a joint forecasting backbone via media-general graph adaptation: a Multimedia Identity-Aware Graph (essence/behavior/latent commonality) plus Spectral Prism Convolution for hierarchical temporal analysis with adaptive scale search. Beats 16 SOTA TSF models across 13 multivariate + 12 multimodal datasets and 14 TSF foundation models/pretrained LMs in long-context comparisons. (Highly relevant to recommendation-time-series modeling.)
- **arXiv**: https://arxiv.org/abs/2610.11924

### 32. Deep Learning vs. Statistical Models for Multi-Horizon Price Forecasting of Second-Hand Electronics
- **Authors**: Mateusz Buczyński, Michał Woźniak, Konrad Kaczyński, Anna Wróblewska, Sebastian Kuk
- **Institution**: not stated (Warsaw University of Technology-adjacent author list; unconfirmed)
- **Subjects**: q-fin.CP; cs.LG
- **Abstract**: First multi-horizon benchmark for used-electronics resale pricing (subscription platforms where pricing errors = direct risk): 11 models, horizons 1–365 days, 100+ phone/laptop models from Polish marketplaces 2022–2025.
- **Key innovations**: N-BEATS achieves lowest MAPE beyond 30 days (8.51% at 365 days vs 14.94% best statistical baseline, −43%); a single 365-day-trained N-BEATS generalizes to all shorter horizons; short-horizon (1–7 days) naive remains competitive (~0.72% MAPE).
- **arXiv**: https://arxiv.org/abs/2610.10727

### 33. Low-Rank Tensor Structure of Precipitation and Application to Satellite-Reference Merging (TMerge)
- **Authors**: Ryan Solgi, Rohan Shankar, Hugo A. Loaiciga
- **Institution**: not stated (UCSB-adjacent author list; unconfirmed)
- **Subjects**: cs.LG; physics.ao-ph
- **Abstract**: Precipitation is intermittent and variable, but its spatiotemporal structure may admit a low-rank representation useful for correcting satellite estimates with sparse reference data.
- **Key innovations**: CP factorization over native space-time modes reconstructs better than factorizing daily fields or flattened matrices; TMerge merges satellite precipitation with reference data through shared low-rank factors. Correcting IMERG over CONUS 2019–2022: correlation 0.53→0.85, RMSE −48.2%, MAE −29.3%, consistently better than linear bias correction, quantile mapping, and neural nets.
- **arXiv**: https://arxiv.org/abs/2610.11000

## Games / Bandits / Mechanism Design / Multi-Agent

### 34. Beyond Reward Suppression: Near-Optimal Offline Attacks on Warm-Start Bandits with Bounded Rewards
- **Authors**: Qirun Zeng, Manhin Poon, Xiangxiang Dai, Qixin Zhang, Jinhang Zuo
- **Institution**: not stated (academic author list; unconfirmed)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Bandit attacks usually suppress non-target arms, but real manipulation (e.g. fake reviews) directly promotes the target. This gap is studied via bounded offline attacks on warm-start bandits — attacker injects valid action-reward pairs before deployment.
- **Key innovations**: Proves target promotion isn't a heuristic: near the lower reward boundary, any order-optimal-cost attack on UCB must spend a non-vanishing fraction of cost on the target arm. Designs the optimal-cost attack, characterizes the promotion/suppression split, and extends to Thompson Sampling, ε-greedy, and broader algorithm classes.
- **arXiv**: https://arxiv.org/abs/2610.10000

### 35. A General Ω̃(√(T γ_T)) Lower Bound for Kernel Bandits
- **Authors**: Chenkai Ma, Jonathan Scarlett
- **Institution**: not stated (NUS-adjacent author list; unconfirmed)
- **Subjects**: stat.ML; cs.IT; cs.LG
- **Abstract**: Kernel-bandit upper bounds scale as √(Tγ_T), but matching lower bounds existed only for specific kernels (SE, Matérn). Does near-optimality hold in general?
- **Key innovations**: Establishes a general Ω(√(Tγ_T/log T)) minimax regret lower bound for non-constant continuous kernels on compact domains, with the log factor provably unavoidable in general but removable under conditions. Implies exact Θ(√(Tγ_T)) scaling (within constants) for Matérn-ν (ν<2), γ-exponential (γ<2), and certain piecewise-polynomial kernels.
- **arXiv**: https://arxiv.org/abs/2610.11082

### 36. m-Set Adversarial Bandits with Winner Feedback
- **Authors**: Nicolò Cesa-Bianchi, Matteo Papini
- **Institution**: not stated (Università degli Studi di Milano-adjacent author list; unconfirmed)
- **Subjects**: cs.LG; stat.ML
- **Abstract**: Upper/lower bounds for m-set adversarial bandits across utilities (winner reward vs sum) and feedback models (winner index, winner reward, sums, combinations).
- **Key innovations**: Information-theoretic regret lower bounds showing subtle setting changes dramatically alter learning rates, with comparison against combinatorial and MNL bandits; synthetic experiments confirm the theory.
- **arXiv**: https://arxiv.org/abs/2610.10128

### 37. Computing Stable Matchings under Complementarities and Preference Misalignment (CDAR)
- **Authors**: Tatsuya Iwase, Baharak Rastegari, Sebastian Stein, Enrico H. Gerding
- **Institution**: not stated (University of Southampton-adjacent author list; unconfirmed)
- **Subjects**: cs.GT
- **Abstract**: Stable matching may not exist with complementary preferences; this paper gives conditions under which it does.
- **Key innovations**: Existence when each firm has an **anchor worker** in every feasible coalition plus **Transitive Alignment** (a global cross-coalition ranking consistent with worker preferences). CDAR (Combinatorial Deferred Acceptance with Reproposals) converges in finite time, outputs stable matchings (potential-function proof), and under strict preferences is Pareto optimal among stable matchings; applications to vehicle-route assignment and wage negotiation.
- **arXiv**: https://arxiv.org/abs/2610.06337

### 38. Self-Referenced Social Preferences: Cooperation without Observing Others' Rewards
- **Authors**: Mohamed Ayman Mohamed, Harshil Kotamreddy, Marcos Menon Jose
- **Institution**: not stated (academic author list; unconfirmed)
- **Subjects**: cs.AI; cs.MA
- **Abstract**: Social preferences promote MARL cooperation but usually require observing peers' reward signals, which real interactions don't expose.
- **Key innovations**: Each agent models its own reward, applies it to others' observed transitions, and feeds these self-referenced assessments into standard social preferences (reward modification or policy-update weighting). On Escape Room, Clean Up, Commons Harvest, agents cooperate without others' rewards even where independent learners fail, often with more equitable return splits; policy-update weighting stays robust under partial observability.
- **arXiv**: https://arxiv.org/abs/2610.07881

### 39. AGAR: A Reinforcement Learning Substrate for LLM Program Evolution
- **Authors**: Haoran Li, Zengle Ge, Xiaomin Yuan, Yui Lo, Haoxin Li, Songlin Zhou, Qianhui Liu, Jiahua Ying, Yuanhang Liu, Mingju Chen, Annan Li, Jianmin Wu, Dawei Yin, Dou Shen
- **Institution**: not stated (Baidu-adjacent author list; unconfirmed)
- **Subjects**: cs.AI; cs.MA
- **Abstract**: LLM program evolution is governed by five hand-set constants (parent selection, mutation hardness, diversity, memory, scalar fitness) — each has an RL estimator.
- **Key innovations**: Formalizes program evolution as an MDP whose action is the **modular prefix the model is conditioned on** rather than the emitted program, letting credit assignment/value/exploration/memory attach to distinct components with no gradient training of the backend. Improves on the stronger of two published baselines across most of 19 tasks (gains concentrated in competitive programming); also yields a checkable reading of prior systems as implicitly zero-discount.
- **arXiv**: https://arxiv.org/abs/2610.09215

### 40. ThunderSyncRL: Lossless Acceleration of Agentic Reinforcement Learning
- **Authors**: Seil Kang, Hangoo Kang, Tarun Suresh, Youngeun Kim, Shreyas Pimpalgaonkar, Seong Jae Hwang, Azalia Mirhoseini
- **Institution**: not stated (industry+academic author list; unconfirmed)
- **Subjects**: cs.LG; cs.AI
- **Abstract**: Synchronous agentic RL leaves learners idle until rollout/verification finishes; asynchronous training overlaps work but introduces policy staleness.
- **Key innovations**: ThunderSyncRL starts gradient computation as soon as required inputs are fixed **without staleness** — per-trajectory score gradients for GRPO, per-turn teacher-scored gradients for OPD while tools run. Proof of identical updates to batch-synchronous training; up to 1.9× faster to the same performance (SWE-bench Verified, Terminal Bench 4.0), and up to +2.47 pts over asynchronous training at fixed budget.
- **arXiv**: https://arxiv.org/abs/2610.05935

### 41. Continual Graph Multi-Agent Reinforcement Learning (CGMARL / FROG)
- **Authors**: Tommaso Marzi, Ahmed Hendawy, Jan Peters, Carlo D'Eramo, Andrea Cini, Cesare Alippi
- **Institution**: not stated (TU Darmstadt/USI/Politecnico di Milano-adjacent author list; unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: In Continual MARL, tasks differ in underlying structure (network topologies, formation configurations), which existing methods fail to exploit.
- **Key innovations**: Maps task sequences to attributed graphs (structure defines dynamics, rewards, and number of agents); introduces GRAFO benchmark and FROG, a **frozen graph encoder** preserving structural knowledge. Pairing FROG with existing continual-learning methods substantially improves CMARL scenarios.
- **arXiv**: https://arxiv.org/abs/2610.10302

## Personalization / RecSys-adjacent (thin lane)

### 42. Commercial Intent in Human-AI Conversations: A Corpus Audit and Architecture for Website Sales Agents
- **Authors**: Benjamin Tannenbaum
- **Institution**: not stated (arXiv metadata omits affiliations)
- **Subjects**: cs.IR
- **Abstract**: Conversational sales agents must separate product questions from purchase commitments, preserve explicit requirements, and ground the next action in current business information.
- **Key innovations**: Aggregate census of 725,219 conversation records (Aiso): 6.09% commercial / 0.33% transactional; commercial-label prevalence 4.87–6.35% across source batches. Proposes a reference architecture separating corpus inventory, commercial relevance, training eligibility, and business outcomes, with provenance-bearing conversation state and constrained next-action policy. Metadata audit + technical design, not a conversion-validity claim.
- **arXiv**: https://arxiv.org/abs/2610.06205

### 43. Personalize at Test Time: Learning User Preferences for Image Generation
- **Authors**: Jiamu Bai, Jiaming Hu, Yanhong Wu, Zellux Wang
- **Institution**: not stated (academic/industry author list; unconfirmed)
- **Subjects**: cs.CV; cs.AI
- **Abstract**: Aligning image generation with individual user preferences is bottlenecked by costly annotations or VLM extraction from interaction histories.
- **Key innovations**: An autoencoder compresses hundreds of visual attributes into 50 attribute-anchored dimensions; an evaluator scores images on them; each user is a linear combination estimated via Bradley-Terry likelihood on sparse pairwise feedback. Per-user adaptation reduces to a low-dimensional weight vector — ~77% held-out pairwise prediction accuracy, improved alignment, diffusion model stays frozen.
- **arXiv**: https://arxiv.org/abs/2610.09015

### 44. Ranking Prior Alignment for Credit Risk Modeling: When Do External Priors Matter?
- **Authors**: Qiye Lu, Jiang Ji, Liang Zhang
- **Institution**: not stated (industry author list; unconfirmed)
- **Subjects**: cs.LG
- **Abstract**: Cold-start credit scoring (scarce labels, immature features, minimal capacity) needs external regularization grounded in domain knowledge.
- **Key innovations**: Model-agnostic framework distilling external **ranking priors** (experts, teachers, or LLMs) into any scoring model via temperature-scaled KL, unifying MIL attention and XGBoost custom objective with a single L = L_task + γ(t)·KL loss. On an industrial 1.5M-merchant dataset: 7/7 positive cells (MIL, 3K bags), 9/9 (XGBoost); Amex cross-dataset 5/5 positive folds (ΔAUC +0.041); gains follow an **inverse-scaling pattern** (benefits grow as data/capacity/feature quality fall) — guidance for when to invest in prior annotation.
- **arXiv**: https://arxiv.org/abs/2610.11146

---

Generated: 2026-10-11