---
title: "arXiv AI Research Scan — August 2, 2026"
type: synthesis
created: 2026-08-02
updated: 2026-08-02
tags: [arxiv, survey, llm, agents, recommendation, ctr, sequential-modeling, memory, games, game-theory, retrieval]
---

# arXiv AI Research Scan — August 2, 2026

Curated papers submitted Jul 29–30, 2026 (the Fri Jul 31 arXiv batch) across LLMs/agents, recommendation/retrieval/advertising, sequential modeling/memory, and games/strategic reasoning. Complements the [Jul 30 scan](../2026-07-30/arxiv-ai-search.md), the [Aug 1 scan](../2026-08-01/arxiv-ai-search.md), and the [Aug 1 paper check](../2026-08-01/arxiv-paper-check.md) — **no overlap** with papers covered there.

---

## Large Language Models, Agents & AI4AI

### 1. Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering
- **Authors**: Junlin Yang, Che Jiang, Yu Fu, Tianwei Luo, Can Ren, Weizhi Wang, Kaikai Zhao, Hongyi Liu, Yuxin Zuo, Yuru Wang, Yuchen Fan, Kai Tian, Zhenzhao Yuan, Xiaojian Lin, Li Sheng, Rushi Qiang, Guoli Jia, Xingtai Lv, Ermo Hua, Dianqiao Lei, Youbang Sun, Ning Ding, Bowen Zhou, Kaiyan Zhang
- **Institution**: Tsinghua University / Zhipu AI (tentative, based on author affiliations)
- **Abstract**: Recursive self-improvement (RSI) requires AI that improves the process of building AI (AI4AI); machine learning engineering (MLE) is a concrete executable testbed. Introduces OpenMLE, an open full-stack system (OpenMLE-Gym verifiable task envs, OpenMLE-RL operator learning, OpenMLE-Evo long-horizon search) on which Frontis-MA1 (35B) is post-trained as a meta-evolution agent around four atomic program-evolution operators (Draft, Improve, Debug, Crossover), coupling learning and evolution in a single loop.
- **Key Innovations**: On MLE-Bench Lite (12h/task, one RTX 4090, 12 GB VRAM) improves Medal Average 39.39%→60.61% over base, reaching 71.21% with OpenMLE-Evo-Max — exceeding GPT-5.5 + Codex and approaching GPT-5.6 Sol and 2.8T Kimi K3; transfers to held-out NatureBench Lite; releases weights + full OpenMLE stack.
- **Link**: https://arxiv.org/abs/2607.28568

### 2. One Human, $N$ Agents: Audit-Budget Allocation for LLM Agent Fleets under Miscalibrated, Correlated Confidence
- **Authors**: Cesare Zavattari, Alessandro Tommasi, Giuseppe Prencipe
- **Institution**: N/A
- **Abstract**: A single human must audit $N$ LLM agents under budget $B \ll N$ audits/round, guided by self-reported confidence that may be adversarially miscalibrated with correlated errors. Models this as budgeted noisy inspection over a two-level Gaussian copula and locates the miscalibration threshold $\delta^*$ past which confidence-ranked auditing is worse than random.
- **Key Innovations**: Two prior expectations reverse: $\delta^*$ rises as budget shrinks, and cross-family correlation is not low — shared difficulty dominates lineage. Five open-weight LLMs show near-constant (operationally useless) confidence at/beyond the flip; a proprietary model is informative and lands below it. Gives a quantitative criterion for "vacuous" oversight.
- **Link**: https://arxiv.org/abs/2607.28317

### 3. RepBench: Compiling Benchmarks into Capability Representations for Large Language Models
- **Authors**: Yanshi Li, Xueru Bai, Shuman Liu, Long Zhang
- **Institution**: N/A
- **Abstract**: Representation engineering reads/steers capability directions in LLMs, but methods are usually evaluated on paper-specific synthetic data. RepBench is a benchmark-grounded data layer for capability-aligned representation probing: crawls 13,427 benchmark papers into a taxonomy of 182 capability clusters in 13 families; harvests 353 public datasets into 46,149 audited probe texts covering 94 capabilities (each backed by ≥2 independent benchmarks).
- **Key Innovations**: Multi-benchmark design reduces single-source dependence; cross-benchmark transfer eval across 12 models × 4 readouts shows difference-in-means wins model-level on 10 models while logistic regression wins the most capability-model cells — readout/aggregation are meaningful evaluation dimensions. Releases reusable closed-loop workflow.
- **Link**: https://arxiv.org/abs/2607.28008

### 4. When Specifications Conflict: A Symmetry-Based Framework for Measuring LLM Preferences
- **Authors**: Tairan Wang, Liang Zhou, Zikang Zhan, Pingchuan Yan
- **Institution**: N/A
- **Abstract**: LLMs increasingly must integrate inconsistent/conflicting sources, but there is no controllable, attributable method for analyzing how they resolve conflicts between competing specifications. Proposes a controlled experimental framework with explicitly conflicting specifications and a symmetry-based design that reduces confounds.
- **Key Innovations**: On a math benchmark with 550 conflict instances across 11 function families, finds a consistent preference ordering Formal ≈ Naturalized Formal > Pure Natural Language > Input–Output Examples; extends to Boolean algebra, code generation, and clinical domains.
- **Link**: https://arxiv.org/abs/2607.28384

### 5. MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck
- **Authors**: Dongyi Liu, Haixing He, Xiaobao Wu, Jia Li
- **Institution**: HKUST (tentative)
- **Abstract**: Memory-augmented agents are vulnerable to memory injection attacks — poisoned retrieved memory diverts behavior from user intent. Existing defenses are costly or suffer information redundancy in multi-turn contexts. MIND (Memory Intent-Aware Neural Denoising) uses an intent-aware Information Bottleneck to extract compact intent–behavior representations, filtering task-irrelevant/repetitive info while preserving cross-turn attack signals; a lightweight detector flags malicious memories.
- **Key Innovations**: On ReAct-StrategyQA reduces mean ASR-r and ASR-a by 55.4%/55.3% while matching undefended agent accuracy and latency; avoids repeated LLM auditing overhead.
- **Link**: https://arxiv.org/abs/2607.28103

### 6. FinanceHarness: Autonomous Financial Deep Research Framework
- **Authors**: Yijia Xiao, Rujun Han, Yanfei Chen, Zifeng Wang, Ke Jiang, Zhongying CuiZhu, Vishy Tirumalashetty, Wei Wang, Burak Gokturk, Tomas Pfister, Chen-Yu Lee
- **Institution**: Google (Cloud AI / Research)
- **Abstract**: Financial deep research demands specialized knowledge for historical patterns and forecasts, unlike general-purpose reports. FinanceHarness is a layered harness (environment/data construction, agent execution loop, reward modeling) plus FinanceGym, a point-in-time benchmark of thesis-driven questions with rubrics combining pre- and post-cutoff criteria that prevent future-information leakage.
- **Key Innovations**: Expert validation yields 82% pass rate while leading LLMs/agents score below 40% (headroom); same open-weight backbone improves rubric score 25.3%→32.4%. Open-sourced.
- **Link**: https://arxiv.org/abs/2607.27853

### 7. AutoSupervision: Closing the Feedback Loop in Scientific Workflows with Grounded Revision Verification
- **Authors**: Haobo Li, Eunseo Jung, Wenxiao Zhao, Feng Liu, Jiong Wang, Kaiyi Xu, Zijie Guo, Zixin Chen, Ben Fei, Fenghua Ling, Lei Bai
- **Institution**: Shanghai AI Laboratory (tentative)
- **Abstract**: Evaluates whether manuscript revisions genuinely address reviewer concerns through grounded evidence, using transparent peer-review records (comments → responses → revised manuscripts) as natural supervision. Models must characterize concerns, judge resolution, and identify supporting evidence.
- **Key Innovations**: 56,000 Nature Communications articles + review records. LLMs do well characterizing concerns (GPT-5.5: 0.754) but evidence-based verification is the bottleneck (best model only 0.501).
- **Link**: https://arxiv.org/abs/2607.27845

### 8. DataClawEval: A Benchmark for Data Engineering Agents in Real Industrial Harness
- **Authors**: Debin Meng, Jiaming Yang, Zefang Zong, Tengyue Xu, Haining Xie, Yang Li, Peng Chen
- **Institution**: N/A
- **Abstract**: First comprehensive benchmark for end-to-end data-engineering agents. Built on production-grade enterprise code: 100 rigorous tasks across PySpark, MySQL, HiveSQL, PrestoSQL/Trino, FlinkSQL, graded by deterministic rule-based scripts in isolated sandboxes (no LLM-as-a-judge).
- **Key Innovations**: 16 frontier agents evaluated: strongest attains only 74.9 overall; no single model dominates — each excels on a different engine, revealing strict domain specialization. Autonomous data engineering remains unsolved. Releases dataset + containerized envs + scripts.
- **Link**: https://arxiv.org/abs/2607.28033

### 9. Fidelity Is Not Safety: Gently-Compressed LLMs Pass Every Data-Free Quality Guard Yet Invent Procedure Steps in Agentic Execution
- **Authors**: I. Kennedy, T. Kennedy
- **Institution**: N/A
- **Abstract**: Standard data-cheap guards (perplexity within a factor, MMLU in CI, data-free output-fidelity probes) have a blind spot. Across three model families, gently-compressed models clear every guard yet invent procedure steps never in the instructions when running a standard operating procedure (SOP) as an agent.
- **Key Innovations**: Operator-specificity — coherent low-rank (SVD) truncation induces it, magnitude pruning matched to same perplexity does not; governing axis is coherence of compression error × its rate. Gives a data-free two-axis screen (coherent-fraction, error-rate) that flags failing builds across architectures.
- **Link**: https://arxiv.org/abs/2607.28196

### 10. Why Are GUI Agents Correct but Late? Decode on the Decision-Time Critical Path, Tested with Pre-Compiled Policy Trees
- **Authors**: Zihan Dong, Rui Qian, Qishi Zhan, Dongshen Peng, Kaixin Li, Yu Li
- **Institution**: N/A
- **Abstract**: Computer-use agents fail on transient GUI events because they produce the correct action only after the window closed — caused by expensive autoregressive decoding on the decision-time critical path. Adaptive Anticipatory Policy Trees (AAPT) eliminate the delay without modifying the model: during idle periods the frozen model builds a bounded conditional policy tree with observable guards and branch deadlines; a lightweight observer matches change-gated frames and executes immediately.
- **Key Innovations**: Paired trials: success 0.50→0.79 in a contested decision window (p=1.8×10⁻³) with no incorrect actions; open-loop/predict-and-replan baselines get zero success. Pre-registered oracle probe rejects the initial hypothesis, pointing to branch routing as the causal bottleneck; reproduces on an independent model over 126 paired trials.
- **Link**: https://arxiv.org/abs/2607.28399

---

## Recommendation, Retrieval & Advertising

### 11. OneShot: Index-in-Ranking with Neural Scoring for Large-Scale Retrieval
- **Authors**: Ziwei Li, Shuyao Li, Xufeng Cai, Xue Zou, Yiming Ma, Huiting Lu, Wujie Yan, Zhichen Zhao, Yang Lu, Zhe Wang, Rui Luo, Zhengyu Su, Dan Zhang, Ji Liu
- **Institution**: Meta (Instagram)
- **Abstract**: In recommendation, retrieval (billions→thousands of candidates) traditionally optimizes ranking accuracy and indexing efficiency separately, which are structurally misaligned. OneShot is an end-to-end, in-model index learning framework that natively aligns index learning with ranking objectives, and scales interaction modeling with neural scoring beyond the dot-product bottleneck.
- **Key Innovations**: Fully deployed in Instagram short-video recommendation with wins in daily sessions, engagement, and time-spent; +20% recall at operational ranking volume and 10× efficiency at equivalent recall.
- **Link**: https://arxiv.org/abs/2607.27475

### 12. Reproducibility in Recommender Systems: A Survey
- **Authors**: Alan Said, Alejandro Bellogin
- **Institution**: University of Gothenburg / Universidad Autónoma de Madrid
- **Abstract**: Structured analysis of the ACM RecSys Reproducibility Track 2020–2025 (51 papers), classifying contribution types and analyzing patterns in datasets, algorithms, frameworks, and evaluation practices. Accepted at ACM TORS.
- **Key Innovations**: Track expanded from reproduction/replication to benchmarking, resources, methodology; reproducibility work improved transparency but had limited impact on methodological diversity — a gap between the conceptual definition and its implementation.
- **Link**: https://arxiv.org/abs/2607.26074

### 13. TCA-SIR: Learning Target-Conditioned Abstractions for Scientific Inspiration Retrieval
- **Authors**: Yuto Suzuki, Farnoush Banaei-Kashani
- **Institution**: University of Colorado Denver
- **Abstract**: Reformulates Scientific Inspiration Retrieval (SIR) as target-conditioned abstraction (TCA): the retrieval object is a transferable abstract principle extracted from a candidate specifically for the target problem, rather than topical similarity. This matters for "remote inspirations" whose value lies in reusable problem-solving principles.
- **Key Innovations**: Learns to generate target-conditioned abstractions and predicts transferability from their representations; on ResearchBench improves HitRate@top4% over MOOSE-Chem by >10 pp, with more interpretable rationales.
- **Link**: https://arxiv.org/abs/2607.28498

### 14. VIG-RL: Learning to Search and Insert for Verified Image Grounding
- **Authors**: Qinhan Yu, Jun Guang, Chong Chen, Wentao Zhang
- **Institution**: Peking University (tentative)
- **Abstract**: Verified Image Grounding (VIG) — precisely integrating retrieved authentic visual evidence into interleaved text-image responses — is currently done by decoupled static pipelines that can't reason about when external knowledge is needed or where to insert images. VIG-RL formulates search-selection-insertion as an active decision-making process in a ReAct-style loop, optimized via RL with a composite reward for step-wise tool execution and final multimodal alignment.
- **Key Innovations**: First agentic/RL formulation of image grounding for RAG; establishes SOTA over static baselines.
- **Link**: https://arxiv.org/abs/2607.28055

### 15. GLM-RAG: Graph Language Models for Graph-Based Retrieval-Augmented Generation
- **Authors**: Maya Arseven, Anette Frank, Beni Egressy, Johann Higl, Moritz Plenz
- **Institution**: Heidelberg University et al.
- **Abstract**: Compares GLM-based, GNN-based, and vector-search retrievers for RAG over knowledge graphs in single- and multi-hop settings, with focus on transferability to unseen domains.
- **Key Innovations**: Fine-tuned GLM retrievers generalize better out-of-domain, achieving SOTA on two multi-hop benchmarks and staying comparable in-domain; GNN retrievers achieve higher graph coverage with efficient training; vector search excels at single-hop.
- **Link**: https://arxiv.org/abs/2607.28397

---

## Sequential Modeling, Memory & Retrieval

### 16. ConMem: Contribution-Aware Memory for Long-Horizon Manufacturing Inspection Logs
- **Authors**: Bingchen Liu, Yuanyuan Fang, Lei Liu, Guangyuan Dong, Xing Fu, Yuanyuan Gao, Shuyue Wei, Xin Li, Xiangtian Meng
- **Institution**: N/A (industrial steel inspection)
- **Abstract**: Long-horizon steel-equipment inspection must reason over heterogeneous logs across repeated cycles; naive RAG treats history as static corpus without estimating diagnostic value, failing to report early risk. ConMem segments logs into functional evidence units, estimates each unit's contribution to downstream diagnosis via Shapley-style estimation, and retains high-value evidence under a memory budget.
- **Key Innovations**: 76.0% QA accuracy exceeding the strongest directly comparable baseline; −88.2% input tokens and −86.6% response time vs naive 8K-context LLM; retains weak early seal-wear signal across three inspection cycles in deployment.
- **Link**: https://arxiv.org/abs/2607.28126

### 17. RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon Multimodal Reasoning
- **Authors**: Jingxiang Fan, Junbao Zhuo, Bochao Zou
- **Institution**: N/A
- **Abstract**: Multimodal long-term memory agents emphasize what to store, not how to retrieve. RRM augments an entity-centric multimodal memory graph with reflective experience memory that distills transferable procedural retrieval knowledge from historical task trajectories; retrieved experiences become query-level guidance while answer generation is conditioned only on newly retrieved factual evidence.
- **Key Innovations**: Lifecycle management (usage frequency, reuse feedback, temporal decay) cuts redundancy; SOTA on M3-Bench-Robot, M3-Bench-Web, and Video-MME-Long.
- **Link**: https://arxiv.org/abs/2607.28156

### 18. Gradient-free Task-Conditioned Retrieval for On-Device In-Context Learning (CoRA)
- **Authors**: Xinyu Luo, Hui Liu, Yihua Shao, Junyi Yang, Arindam Basu, Haoliang Li
- **Institution**: City University of Hong Kong (tentative)
- **Abstract**: On-device ICL needs pre-inference demonstration retrieval exploiting task-specific information under limited compute/memory/data budgets. Conditional Retrieval Alignment (CoRA) converts a frozen encoder into a task-conditioned retriever: selects complementary encoder layers, builds an output-derived conditioning space via closed-form ridge regression, and a rank-constrained basis (proven optimal low-rank compression of the output-conditioned fitted representation) with an exact two-pass streaming construction.
- **Key Innovations**: Gradient-free, no retriever fine-tuning/backprop/target-model calls; validated on 10 text + 4 multimodal benchmarks (Llama-3.2-1B, MobileLLM-Pro, OpenFlamingo-3B, Qwen3.5-2B) with end-to-end Raspberry Pi 5 deployment.
- **Link**: https://arxiv.org/abs/2607.27766

### 19. CACHE-UK: A Stability-Aware Memory Editor for Sequentially Updated Quantized LLMs in Finance
- **Authors**: Anubhav Lakra, Yue Feng
- **Institution**: University of Birmingham (tentative)
- **Abstract**: 4-bit quantization limits sequential memory editing in dynamic financial deployments (the "quantization stability crisis"). CACHE-UK (Contextual Adaptive Continual Hybrid Editor for UK Finance) combines a rank-1 LoRA perturbation confined to the low-rank adapter subspace, a financial domain prioritization module, and a closed-loop Stability Controller tracking "degradation debt".
- **Key Innovations**: On 4-bit OpenLLaMA-3B + 88,021 UK financial docs: −11–17% knowledge degradation vs adapted baselines under identical 4-bit constraints; best test (generalization) success 28% (+6 pp), though absolute rates remain low.
- **Link**: https://arxiv.org/abs/2607.28292

### 20. Stage-Replay Divergence Follows the KV Cache: Fixed-Prefix Precision Controls and Bidirectional Cache Transplantation
- **Authors**: Alexander Boesgaard Lorup
- **Institution**: N/A
- **Abstract**: Audits stage-replay diagnostics that treat fresh-prefill continuation as continuation from the original decoder state, at a whole reasoning-stage boundary in a Qwen2.5-derived system. Matched 200-item experiment compares retained live cache vs one-shot prefill of identical tokens; BF16 replicas remain exact yet constructions differ on 166 suffixes.
- **Key Innovations**: Fixed-prefix 2×2 shows BF16 disagreements recur while FP32 gives no decoded disagreement (95% Wilson upper bound 1.88%); bidirectional transplantation of all 48 K/V layers makes divergent continuations follow their cache donor (24/24 primary, 43/43 outcome-blind replication) — boundary K/V cache is a causally sufficient carrier of divergence, with precision moderating its expression.
- **Link**: https://arxiv.org/abs/2607.28495

---

## Games & Strategic Reasoning

### 21. Correlated Chance Sampling for Monte Carlo Counterfactual Regret Minimization (CCS-MCCFR)
- **Authors**: Boning Li, Yu Chen, Longbo Huang
- **Institution**: Tsinghua University
- **Abstract**: MCCFR repeatedly samples chance outcomes while strategy evolves, drawing them independently each visit. CCS-MCCFR is a drop-in replacement assigning each chance node a persistent randomized Weyl stream mapped through the node's distribution, giving the first $N$ draws deterministic local frequency error $O(\log(N+1)/N)$ vs i.i.d. $O(N^{-1/2})$.
- **Key Innovations**: Unbiasedness along fixed strategy trajectories; per-traversal reset retains the standard $O(1/\sqrt{T})$ External Sampling guarantee. Reduces final exploitability 19.05–34.01% across Kuhn and four Leduc poker configs, 4.27% on Goofspiel-4; one-line change, no new hyperparameters, no time overhead.
- **Link**: https://arxiv.org/abs/2607.27035

### 22. Learning to Persuade Privately Informed Receivers
- **Authors**: I. Arda Vurankaya, Ufuk Topcu
- **Institution**: UT Austin
- **Abstract**: Online Bayesian persuasion where a binary-action receiver also consults a fixed private signaling scheme the sender can neither observe nor control. Over $T$ rounds the sender commits to a signaling scheme and observes only the receiver's action.
- **Key Innovations**: Algorithm achieves regret $\widetilde{O}(T^{3/4})$ vs the sender who knows the private scheme, with polynomial dependence on state-space and signal-alphabet sizes; reduces learning the exponentially large belief-space partition to a one-dimensional change-point detection problem.
- **Link**: https://arxiv.org/abs/2607.28342

### 23. Learning Dynamics of Strategic Publishers in Generative AI Ecosystems
- **Authors**: Sagie Dekel, Omer Madmon, Moshe Tennenholtz, Oren Kurland
- **Institution**: Technion
- **Abstract**: GenAI search generates answers with citations, so content creators compete for attribution-based exposure rather than ranking position. Introduces a game-theoretic model of publishers competing for exposure, studying better-response learning dynamics and associating convergence to equilibrium with ecosystem stability via potential games.
- **Key Innovations**: Shows instability of mechanisms representing real-world modern systems and characterizes a stable mechanism; simulations reveal stable mechanisms do not necessarily maximize welfare — platform designers face a stability/welfare trade-off.
- **Link**: https://arxiv.org/abs/2607.25514

### 24. Collusion with Competitive Marginals: Price-Level Audits Are Blind by Construction
- **Authors**: Xin Xu, Chengrui Wu, Jiayu Lu, Kaizhen Tan, Siru Tao, Hanzhe Hong
- **Institution**: N/A
- **Abstract**: Empirical work on algorithmic collusion asks whether prices are supracompetitive. Shows a conspiracy can keep every agent's bid law exactly competitive while coupling only through the joint distribution of unexplained bid components — any test on a single agent's price history has power equal to its false-positive rate, for any coupling up to comonotonicity.
- **Key Innovations**: Mechanism appears in real LLM agents (residual correlation +0.053 within a model vs +0.0001 across models), falls monotonically with sampling temperature (p=0.002); on 24 days of Ethereum builder-auction data (77,684 bids/39 bidders), honest bidder pairs are so dependent that a 5% FPR screen sits above a floor of +0.50 to +0.81. Argues the regulatory target is counting operators, not detection.
- **Link**: https://arxiv.org/abs/2607.26385

---

## Key Themes

| Theme | Papers | Trend |
|-------|--------|-------|
| **AI4AI & recursive self-improvement** | Frontis-MA1 | Executable AI4AI stacks (verifiable envs + operator learning + long-horizon search) are becoming open, reproducible research infrastructure |
| **Oversight & audit of agent fleets** | One Human N Agents, MIND, AutoSupervision | Human audit budgets vs N agents; confidence calibration is the weak link; memory injection as first-class attack surface; evidence-grounded verification as bottleneck |
| **Evaluation of LLM capabilities** | RepBench, When Specifications Conflict, DataClawEval | Benchmark-grounded probing layers; controllable conflict-resolution measurement; domain-specialized (not omnipotent) agents |
| **Neural retrieval beyond dot-product** | OneShot, VIG-RL, GLM-RAG, TCA-SIR | Index-in-ranking joint learning; agentic/RL image grounding; graph-language-model retrievers that transfer out-of-domain; target-conditioned abstraction for scientific inspiration |
| **Memory as value-filtered state** | ConMem, RRM, CACHE-UK, Stage-Replay | Shapley-style contribution scoring of memory units; reflective (procedural) vs episodic memory; stability-aware editing under quantization; KV-cache precision as causal carrier of divergence |
| **Algorithmic collusion & GenAI search economics** | Collusion with Competitive Marginals, Learning Dynamics of Strategic Publishers | Standard price-level audits provably blind to a class of collusion; game-theoretic design needed for stable attribution-based ecosystems |

(End of file)
