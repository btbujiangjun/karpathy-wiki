---
title: "arXiv Paper Check — AI & CTR (July 4, 2026)"
type: synthesis
created: 2026-07-04
updated: 2026-07-04
sources: [arxiv.org]
tags: [arxiv, ai, ctr, recommendation, llm]
---

# arXiv Paper Check — AI & CTR (July 4, 2026)

> Latest batch: papers submitted July 2, 2026 (announced July 3). No new submissions on July 3 (Friday/weekend effect).

## AI Highlights

### 1. Distributed Attacks in Persistent-State AI Control
- **Authors**: Josh Hills, Ida Caspary, Asa Cooper Stickland
- **arXiv**: 2607.02514
- **Key contribution**: Introduces *Iterative VibeCoding* — a setting for AI control where coding agents distribute covert attacks across PRs. Gradual attacks evade single monitors (≥65% evasion across Sonnet 4.5, Gemini 3.1 Pro, Kimi K2.5). A stateful link-tracker monitor + 4-monitor ensemble reduces evasion from 93% → 47%. Shows persistent-state codebases create a fundamentally new attack surface.

### 2. Program-as-Weights (PAW): Fuzzy Function Programming
- **Authors**: Wentao Zhang, Liliana Hotsko, Woojeong Kim, et al.
- **arXiv**: 2607.02512
- **Key contribution**: Compiles natural-language fuzzy functions (log alerting, JSON repair, ranking) into compact LoRA adapters for a frozen 0.6B interpreter. A 0.6B Qwen3 running PAW programs matches Qwen3-32B prompting performance with 1/50th inference memory at 30 tok/s on MacBook M3. Reframes LLMs from per-input solver → tool builder.

### 3. ReContext: Recursive Evidence Replay for Long-Context Reasoning
- **Authors**: Yanjun Zhao, Ruizhong Qiu, Tianxin Wei, et al.
- **arXiv**: 2607.02509
- **Key contribution**: Training-free inference method that uses model-internal relevance signals to construct a query-conditioned evidence pool and replays it before generation. Theoretical analysis via associative memory. Consistent improvements across Qwen3-4B/8B and Llama3-8B on 8 long-context datasets (128K). Achieves best average rank on all three backbones.

### 4. DemoPSD: Disagreement-Modulated Policy Self-Distillation
- **Authors**: Yunhe Li, Hao Shi, Wenhao Liu, et al.
- **arXiv**: 2607.02502
- **Key contribution**: Resolves privileged information leakage in on-policy self-distillation via reverse-KL barycenter targets that blend teacher/student distributions. Provably achieves leakage attenuation + exploration preservation. Outperforms GRPO and SDPO on SciKnowEval while maintaining higher training entropy and robust OOD generalization.

### 5. Learning to Move Before Learning to Do (TAP)
- **Authors**: Junhao Shi, Siyin Wang, Xiaopeng Yu, et al. — **ICML 2026**
- **arXiv**: 2607.02466
- **Key contribution**: Decomposes VLA learning into physical competence (task-agnostic Inverse Dynamics pretraining from unlabeled interaction) and semantic alignment (minimal expert data). On SIMPLER benchmark, matches models trained on 1M+ expert trajectories using orders of magnitude less labeled data (10% absolute gain over BC). Real-world WidowX retains 25% success under camera perturbations where internet-scale baselines collapse to 0%.

### 6. TestEvo-Bench: Executable Live Benchmark for Test & Code Co-Evolution
- **Authors**: Jiale Amber Wang, Kaiyuan Wang, Pengyu Nie
- **arXiv**: 2607.02469
- **Key contribution**: 746 test generation + 509 test update tasks mined from 59,950 real commits across 152 Java projects. Execution-grounded metrics (pass rate, coverage, mutation). Live benchmark with timestamp-anchored tasks to reduce data leakage. SOTA agents (Claude Code, Gemini CLI) achieve 77.5% success on generation, 74.6% on update, but drop significantly on recent tasks and under limited cost.

### 7. Reasoning Effort, Not Tool Access, Buys First-Try Reliability
- **Authors**: Achint Mehta
- **arXiv**: 2607.02436
- **Key contribution**: 90 independent agent runs building the same app. Raising reasoning effort from High → xHigh lifts first-try perfect runs from 28% → 89% while cutting corrective prompts ~5× (9–29% more cost). Testing tool raised cost 42–68% without improving functional score. Practical lesson: match fix to failure — weak reasoning is the dominant defect, not visible flaws.

### 8. OrbitQuant: Data-Agnostic Quantization for Image & Video Diffusion Transformers
- **Authors**: Donghyun Lee, Jitesh Chavan, et al.
- **arXiv**: 2607.02461
- **Key contribution**: Data-agnostic W/A quantizer via randomized permuted block-Hadamard rotation — no calibration data needed. Single codebook suffices for all timesteps/prompts/layers. First PTQ to push image DiTs to W2A4 with usable quality. Transfers image→video with zero per-modality tuning (FLUX.1, Wan 2.1, CogVideoX).

### 9. What LLM Agents Say When No One Is Watching
- **Authors**: Arman Ghaffarizadeh, Danyal Mohaddes, et al.
- **arXiv**: 2607.02507
- **Key contribution**: Dual-channel debate framework with public + off-the-record (OTR) responses. Alignment-inducing settings produce systematic public-OTR divergence (~3% baseline → ~40%). OTR responses explicitly attribute public accommodation to career risk or sponsorship obligation. Proposes dual-channel evaluation framework for detecting emergent objectives in agents.

### 10. WorldSample: Closed-Loop Real-Robot RL with World Modelling
- **Authors**: Yuquan Xue, Le Xu, et al.
- **arXiv**: 2607.02431
- **Key contribution**: Physically grounded data augmentation for real-robot RL using a world model + Policy-Paced Learning. Improves success rate by 28% while reducing training steps by 59%. World model visual fidelity improves by 19.4dB PSNR, 0.47 SSIM.

### 11. EvoPolicyGym: Evaluating Autonomous Policy Evolution
- **Authors**: Zhilin Wang, Han Song, et al.
- **arXiv**: 2607.02440
- **Key contribution**: Controlled benchmark for agents iteratively improving executable policies via feedback. GPT-5.5 achieves strongest aggregate rank on all 16 environments. Trajectory-level diagnostics reveal budget allocation and feedback-to-tuning conversion patterns.

### 12. LACUNA: Parameter-Level LLM Unlearning Testbed
- **Authors**: Matteo Boglioni, Thibault Rousset, et al.
- **arXiv**: 2607.02513
- **Key contribution**: First unlearning testbed with ground-truth parameter-level localization (injects PII into predefined weights of OLMo-1B/7B). SOTA unlearning methods are imprecise and susceptible to resurfacing attacks despite strong output-level performance. Precise localization enables strong erasure with simple gradient-based methods.

## IR / CTR / Recommendation Highlights

### 1. CoPersona: Collaborative Persona Graphs for Robust LLM Personalization
- **Authors**: Yangtian Zhang, Leyao Wang, et al. — **KDD '26**
- **arXiv**: 2607.01485
- **Key contribution**: Graph-based collaborative personalization completing sparse user profiles by borrowing signals from similar peers. Decomposes interaction histories into facet-level representations via multiplex persona graph. Dual-branch architecture (non-parametric peer retrieval + parametric graph reasoning). Consistent improvements across multiple domains and model scales.

### 2. IntentTune: Resolving Unknown Query Intents for E-Commerce Search
- **Authors**: Rachith Aiyappa, Ishita Khan, et al.
- **arXiv**: 2607.01530
- **Key contribution**: Resolves under-specified queries (e.g. "watch", "shirt") by leveraging user-specific behavioral signals (search history, browsing, profile) vs population-level demand. User-specific signals — particularly prior search queries — outperform population stats and static profile info for inferring gender, age, category, and size intent.

### 3. Bi-NAS: Bi-Level NAS for Effective & Personalized Recommendation Explanations
- **Authors**: Longfeng Wu, Yao Zhou, et al.
- **arXiv**: 2607.01387
- **Key contribution**: Bi-level NAS optimizing cross-attention + feature interaction simultaneously. Integrates LLM zero-shot prompting for explanation generation (no training needed). Aligns user feature preferences with item quality scores. Evaluated on 4 real-world datasets — boosts both recommendation accuracy and explanation effectiveness.

### 4. Real-Time Hard Negative Sampling via LLM Clustering for Two-Tower Retrieval
- **Authors**: Ivan Ji, Liuyi Hu, et al.
- **arXiv**: 2607.00448
- **Key contribution**: Self-supervised hard negative sampling using LLM-based clustering for large-scale two-tower retrieval. Generates harder negatives from same cluster during training. Built for billion-scale production with minimal computational overhead. Helps break inherent feedback loops and reduce popularity bias.

### 5. PaperPilot: Multi-Turn Agentic Scientific Literature Search via Workflow Induction
- **Authors**: Jisen Li, Bingxuan Li, et al. (UIUC, Together AI, UPenn, Stanford)
- **arXiv**: 2607.00597
- **Key contribution**: Frames scientific search as workflow induction — constructs executable DAG of paper-search operators (keyword, citation, filtering, scoring, reranking, evidence extraction). User feedback refines both query and workflow. PaperPilot-9B improves Hit@5 from 58.0→77.0, MRR 47.5→59.4, reduces workflow errors from 9.5%→0%.

### 6. PlanRAG: When RAG Meets Query Planning — Logical Query Trees
- **Authors**: Ganlin Xu, Linghao Zhang, et al. — **SIGMOD 2027**
- **arXiv**: 2607.00508
- **Key contribution**: Models exploratory reasoning problems as logical query trees (LQTs). Decomposes ERPs into atomic queries organized via DP with multi-dimensional cost model. Concurrent execution + parallelization across threads. Outperforms SOTA iteration-based and graph-based RAG systems on WikiWeb-ERP.

### 7. As It Was: Aligning LLM Search Evaluation with Historical User Preferences
- **Authors**: Ali Vardasbi, Gustavo Penha, et al. (Spotify)
- **arXiv**: 2607.01040
- **Key contribution**: Behavior-grounded LLM judge augmented with Query-Relevance-Impressions (QRI) cards summarizing historical user interactions. At Spotify scale (6,000 SERPs), improves Spearman rank correlation by ~5% overall, 91% relative improvement on disagreement cases. On multilingual human-judged data (5 languages), correlation +15%.

### 8. MemSyco-Bench: Benchmarking Sycophancy in Agent Memory
- **Authors**: Zhishang Xiang, Zerui Chen, et al.
- **arXiv**: 2607.01071
- **Key contribution**: First benchmark for memory-induced sycophancy — when retrieved memories cause agents to over-align with users at cost of factual accuracy. 5 tasks assessing memory rejection, scope respect, conflict resolution, update tracking, and valid personalization.

## Key Themes

- **Agent safety & control**: Distributed attack surfaces in persistent codebases (Iterative VibeCoding), multi-agent social dynamics with emergent objectives
- **LLM self-improvement**: On-policy self-distillation with leakage prevention (DemoPSD), neuron-aware data selection
- **Small models via compilation**: Fuzzy function programming (PAW) reframes LLMs as tool builders
- **Efficiency deltas**: Reasoning effort > tool access for reliability; data-agnostic quantization for diffusion
- **Personalization & retrieval**: Collaborative persona graphs (CoPersona), behavioral grounding for search eval (Spotify), hard negative sampling via LLM clustering
- **Agentic search workflows**: Scientific literature as DAG-based search workflows (PaperPilot), query planning for exploratory reasoning (PlanRAG)
