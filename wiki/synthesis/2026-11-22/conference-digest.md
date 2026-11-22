---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-22 Daily Edition"
type: synthesis
created: 2026-11-22
updated: 2026-11-22
sources:
  - 2611.00616
  - 2611.00281
  - 2611.00420
  - 2512.16895
  - 2512.11193
  - 2512.10892
  - 2512.10292
  - 2512.09367
  - 2512.00709
  - 2512.00881
  - 2512.01020
  - 2512.01089
  - 2512.00918
  - 2512.04111
  - 2512.00919
  - 2512.00679
  - 2512.00947
  - 2512.00930
  - 2512.00524
  - 2512.00311
  - 2512.00272
  - 2512.00349
  - 2512.00352
  - 2512.01351
  - 2512.08702
  - 2512.06883
  - 2610.03727
  - 2512.09218
  - 2512.00656
  - 2512.07846
  - 2611.03113
  - 2512.07650
  - 2611.23949
  - 2611.00554
  - 2611.00871
  - 2611.01320
  - 2611.00286
  - 2512.13576
  - 2512.12582
  - 2610.00715
  - 2512.17238
  - 2512.16570
  - 2512.16514
  - 2611.00586
  - 2611.00319
  - 2611.00077
  - 2611.00300
  - 2611.00442
  - 2610.16158
  - 2611.00050
  - 2610.00511
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, ICLR2026, KDD2026, CVPR2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, advertising, CTR, LLM, agents, generative-models, sequential-modeling, games, code-execution, benchmarks, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-11-22 Daily Edition
# 会议论文日报：2025-2026 顶级 ML/AI 会议（2026-11-22 每日版）

> Venues covered: **ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025** — plus general recent papers in AI, LLMs, recommendation systems, advertising/CTR, games, code execution prediction, agent systems, generative models, sequential modeling, and benchmarks. New to this wiki: **26 venue papers + 25 topic papers** (deduped against all existing wiki pages; 27 papers matched topics but 2611.26011 and 2611.13940 are excluded from Advertising/CTR as not ads-related). Additionally, 36 new papers tagged "NeurIPS 2026" exist in the window (IDs 2610.00025–2611.06522, e.g. 2611.00554, 2611.00871, 2611.01320, 2611.00554); venue strings appearing only in abstracts as related work are excluded per digest convention.

## Method, data window & limitations (方法、数据窗口与限制)

- **Query date:** 2026-11-22. **arXiv access:** arXiv.org month browse pages (`https://arxiv.org/list/{subject}/{month}`; subjects cs.AI, cs.LG, cs.CL, cs.CV, cs.IR, cs.DS, cs.NE, cs.GT, cs.SE, stat.ML; months 2026-11, 2026-10, 2025-12) + per-paper abstract pages (`https://arxiv.org/abs/{id}`); venue match = venue+year regex on arXiv Comments field.
- **Selection:** venue papers = new to the wiki, sorted by arXiv submission date (newest first): ICML 2026 ×6, AAAI 2026 ×5, NeurIPS 2025 ×6, ICLR 2026 ×3, KDD 2026 ×2, ACL 2026 ×3, SIGIR 2026 ×1; topic papers sorted by submission date, top per category (LLMs ×5, Recommendation Systems ×4, Games ×4, Agents ×5, Benchmarks ×3, Generative Models ×2, Sequential Modeling ×2).
- **Affiliations:** recovered from arXiv PDF page-1 author/affiliation blocks (pypdf); generic lines truncated from PDF extraction; some papers have no affiliation block on PDF page 1.
- **Evidence:** all metrics/results/claims are **author-reported**; abstracts from arXiv abs pages; Chinese titles are translation aids; technical terms stay in English.

---

## 1. Venue digest — new venue-tagged papers (会议论文日报 — 新增 venue 标签论文)

### ICML 2026

#### 2611.00281 — DELBERT-2: Pretrained Fingerprint Language Models for DEL Protein Binder Prediction (DELBERT-2：用于 DEL 蛋白结合物预测的预训练指纹语言模型)

- **Authors / 作者:** Bing Hu, Sun Sun, Shaik Salman Basha, Anita Layton, Helen Chen
- **Affiliation / 机构:** Computer Science, University of Waterloo, Canada; 2National (U); 4School of Public Health, U (PDF page-1)
- **Venue / 会议:** ICML 2026 (comments: "14 pages, 6 figures, 2026 Workshop on Generative and Agentic AI for Biology (ICML 2026)")
- **Problem / 问题:** DEL virtual screening must prioritize candidate binders among millions of small molecules; standard transformers trained from scratch and LightGBM ensembles underperform on OOD protocols (hierarchical cluster splits, library splits, building-block splits).
- **Methodology / 方法:** DELBERT-2 — pretrained fingerprint LM: ModernBERT encoder trained with masked language modelling on 2.5M molecules (AIRCHECK DEL corpus) that converts sparse molecular fingerprints into unified token sequences; evaluated across six DEL targets (WDR91, WDR12, SETDB1, PLCZ1, LRRK2, DCAF7) under three OOD protocols.
- **Key innovations / 关键创新:**
  - Fingerprint-centric self-supervised learning pipeline (MLM on fingerprints → unified token sequences) improves PR-AUC and NDCG@1000 relative to LightGBM ensembles and from-scratch transformers.
  - Largest gains in stringent OOD regimes; generalises to held-out library-split and building-block-split protocols.
- **Experimental results / 实验结果：** DELBERT-2 achieves enrichment factor 13.28±3.72 at top-100 vs. 12.36±3.75 for no-pretraining (p=0.040), a 7.4% improvement and 13× over random selection; consistent improvements across hierarchical/library/building-block OOD protocols.
- **Comparison with prior methods / 对比：** LightGBM ensemble baselines; transformers trained from scratch (the paper's main baselines); same OOD protocols (cluster/library/building-block splits).
- **Abstract / 摘要:** We present DELBERT-2, a pretrained fingerprint language model that converts sparse molecular fingerprints into unified token sequences using a ModernBERT encoder trained with masked language modelling on 2.5M molecules from the AIRCHECK DEL corpus. We evaluate across six targets (WDR91, WDR12, SETDB1, PLCZ1, LRRK2, DCAF7) under three out-of-distribution (OOD) protocols: hierarchical cluster splits probe chemical novelty, library splits test cross-library transfer, and building-block splits assess compositional generalization. DELBERT-2 consistently improves PR-AUC and NDCG@1000 relative to LightGBM ensemble baselines and transformers trained from scratch, with the largest gains in stringent OOD regimes. DELBERT-2 achieves 13.28+/-3.72 enrichment factor at top-100 vs. 12.36+/-3.75 for no-pretraining (p=0.040), representing 7.4% improvement and 13x enrichment over random selection. These results demonstrate that fingerprint-centric self-supervised learning effectively improves hit prioritization under distribution shift, enabling practical DEL virtual screening. Code is available at DELBERT-2.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.00281) · [PDF](https://arxiv.org/pdf/2611.00281)

#### 2611.00420 — Circuit Oracle: Automating Attribution Graph Analysis via Natural-Language Queries (熔路预言机：通过自然语言查询自动分析归因图)

- **Authors / 作者:** Shariar Kabir, Hong Kiat Tan, Swastik Agrawal, Sai V R Chereddy, Sriram Balasubramanian
- **Affiliation / 机构:** Anthropic (PDF page-1)
- **Venue / 会议:** ICML 2026 (extended version of workshop paper at the Mechanistic Interpretability and Compositional Learning workshops at ICML 2026)
- **Problem / 问题:** Turning an attribution graph into a safety-relevant insight requires hours of manual analysis by experts — there is no tool that queries graphs in natural language.
- **Methodology / 方法:** Circuit Oracle — an off-the-shelf LLM equipped with a multi-agent harness and task-specific authored skills, which answers natural-language questions about a target model by reading the attribution graph through tool calls; also produces pruned subgraphs and context-specific feature explanations.
- **Key innovations / 关键创新:**
  - End-to-end natural-language interface to attribution graphs (3 safety-relevant proxy tasks).
  - Mixed qualitative/quantitative results: stable across 5 runs and across model choices of the agents.
- **Experimental results / 实验结果：** Spurious-feature detection: Circuit Oracle reaches 78.2 ± 2.4% accuracy, outperforming single-layer feature-ranking baselines; refusal suppression over 50 prompts: single committed intervention slightly below a diff-in-means baseline, only exceeded by best-of-five attempts.
- **Comparison with prior methods / 对比：** Single-layer feature-ranking baselines; Activation Oracles (trained self-explainers are stronger at secret elicitation); diff-in-means baselines.
- **Abstract / 摘要:** Attribution graphs, an emerging tool in mechanistic interpretability, use transcoders to decompose language model computations into sparse interpretable features connected by causal edges. However, turning a graph into a safety-relevant insight requires hours of manual analysis by experts. We introduce Circuit Oracle, an off-the-shelf LLM equipped with a multi-agent harness and task-specific authored skills, which answers natural-language questions about a target model by reading the attribution graph through tool calls. We evaluate it on three safety-relevant proxy tasks: detecting spurious features in probe circuits, eliciting hidden knowledge from taboo-finetuned models, and suppression jailbreaking via feature-level interventions. Beyond task scores, the oracle produces pruned subgraphs and context-specific feature explanations that we assess qualitatively. Results are mixed. On spurious-feature detection, Circuit Oracle reaches 78.2 ± 2.4% accuracy, outperforming single-layer feature-ranking baselines. On secret elicitation, trained self-explainers like Activation Oracles remain the stronger baseline. On refusal suppression over 50 prompts, its single committed intervention is slightly below a diff-in-means baseline, and only exceeds it when allowed the best of five attempts. Results are stable across five runs and across model choices for the agents. We also release the pruned subgraphs and context-specific feature readings that revise existing global labels, and invite future work to develop evaluations that can measure their usefulness directly.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.00420) · [PDF](https://arxiv.org/pdf/2611.00420)

#### 2512.04111 — CentaurEval: Benchmarking Human-in-the-Loop Value in Agentic Coding (CentaurEval：评估智能体编程中的人在回路价值)

- **Authors / 作者:** Hanjun Luo, Chiming Ni, Jiaheng Wen, Zhimu Huang, Yiran Wang, Bingduo Liao, Sylvia Chung, Yingbin Jin, Xinfeng Li, Wenyuan Xu, XiaoFeng Wang, Hanan Salam
- **Affiliation / 机构:** Equal contribution 1: New York University Abu Dhabi, University of Illinois Urbana-Champaign (3), Harvard University, UET (PDF page-1)
- **Venue / 会议:** ICML 2026 (comments: "Accepted by ICML 2026")
- **Problem / 问题:** Existing coding evaluation systems — traditional tests for humans and benchmarks for LLMs — fail to capture the shift toward human-AI collaboration, excluding "Collaboration-Necessary" problems that require both human reasoning and AI efficiency.
- **Methodology / 方法:** CentaurEval — a unified, ecologically valid benchmark; "Collaboration-Necessary" problem templates are intractable for standalone LLMs or humans but solvable through effective collaboration; dynamically instantiates tasks from 45 templates with a standardized IDE for humans and a reproducible 450-task toolkit for LLMs; benchmarked 45 participants against 5 LLMs under 4 levels of human intervention.
- **Key innovations / 关键创新:** Separates human value from standalone LLM/human baselines (0.67% / 18.89%); shows human-AI collaboration yields 31.11% — an emerging co-reasoning partnership.
- **Experimental results / 实验结果：** LLM-only pass rate 0.67%; human-only 18.89%; human-AI collaboration 31.11%; analysis shows strategic breakthroughs can originate from either humans or AI.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.04111) · [PDF](https://arxiv.org/pdf/2512.04111)

#### 2512.00918 — Sparse Neuron Ablation Triggers Catastrophic Collapse of the Language Core in Large Vision-Language Models (大型视觉语言模型中稀疏神经元消融引发语言核心的灾难性崩溃)

- **Authors / 作者:** Cen Lu, Yung-Chen Tang, Andrea Cavallaro
- **Affiliation / 机构:** Idiap Research Institute, Martigny, Switzerland (PDF page-1)
- **Venue / 会议:** ICML 2026 (comments: "Accepted to ICML 2026 Mechanistic Interpretability Workshop")
- **Problem / 问题:** Structures sustaining LVLMs remain poorly understood from a mechanistic interpretability standpoint.
- **Methodology / 方法:** CAN (Consistently Activated Neurons) — progressive neuron ablation method identifying critical neurons; investigated in representative 7B LVLMs (LLaVA-1.5-7b-hf, InstructBLIP-vicuna-7b).
- **Key innovations / 关键创新:** Catastrophic collapse triggered by ablating as few as four neurons in LLaVA-1.5-7b-hf (and a few thousand in InstructBLIP-vicuna-7b); critical neurons are localized in the language model's down-projection layer, not the vision components; consistent two-stage collapse pattern (initial expressive degradation then sudden complete collapse).
- **Experimental results / 实验结果：** LVLMs depend on a sparse subset of neurons concentrated in the language backbone — mechanism of vulnerability and where LVLMs are most vulnerable.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.00918) · [PDF](https://arxiv.org/pdf/2512.00918)

#### 2512.04111 — CentaurEval (see above; ICML 2026) — (placed in ICML 2026)

*(CentaurEval is listed under ICML 2026 above.)*

#### 2512.00919 — Outcome-Aware Spectral Feature Learning for Instrumental Variable Regression (面向工具变量回归的结果感知谱特征学习)

- **Authors / 作者:** Dimitri Meunier, Jakub Wornbard, Vladimir R. Kostic, Antoine Moulin, Alek Fröhlich, Karim Lounici, Massimiliano Pontil, Arthur Gretton
- **Affiliation / 机构:** University College London; CSML (Istituto Italiano di Technology); Faculty of Science, University of Novi Sad; Universitat Pompeu Fabra; DIBRIS, University of Genoa; CMAP-Ecole Polytechnique (PDF page-1)
- **Venue / 会议:** ICML 2026 (comments: "ICML 2026")
- **Problem / 问题:** Established spectral-feature approaches for IV regression are agnostic to the outcome; they fail when the true causal function is poorly represented by dominant singular functions.
- **Methodology / 方法:** Augmented Spectral Feature Learning — learns features by minimizing a novel contrastive loss derived from an augmented operator that incorporates outcome information.
- **Key innovations / 关键创新:** Task-specific feature learning remains effective under spectral misalignment; theoretical analysis + validation on challenging benchmarks.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.00919) · [PDF](https://arxiv.org/pdf/2512.00919)

#### 2512.00349 — Debate with Images: Detecting Deceptive Behaviors in Multimodal Large Language Models (以图像辩论：检测多模态大语言模型中的欺骗行为)

- **Authors / 作者:** Sitong Fang, Shiyi Hou, Kaile Wang, Boyuan Chen, Donghai Hong, Jiayi Zhou, Josef Dai, Yaodong Yang, Jiaming Ji
- **Affiliation / 机构:** OpenAI; Anthropic (PDF page-1)
- **Venue / 会议:** ICML 2026 (comments: "camera ready version for ICML 2026")
- **Problem / 问题:** Deceptive behaviors spread from text to multimodal settings, but there are no tools to monitor covert multimodal deception (monitoring is largely ineffective due to visual-semantic ambiguity).
- **Methodology / 方法:** MM-DeceptionBench — the first benchmark explicitly designed to evaluate multimodal deception (6 categories; stealth, compounded by visual-semantic ambiguity). Debate-with-images multi-agent debate monitor framework: compelling models to ground claims in visual evidence.
- **Key innovations / 关键创新:** Debate with images substantially improves detectability of deceptive strategies across all tested models; boosts agreement with human judgements consistently.
- **Experimental results / 实验结果：** MM-DeceptionBench — first benchmark for multimodal deception, covering 6 deception categories in VLMs.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.00349) · [PDF](https://arxiv.org/pdf/2512.00349)

### AAAI 2026

#### 2512.16895 — On the Edge of Core (Non-)Emptiness: An Automated Reasoning Approach to Approval-Based Multi-Winner Voting (核心(非)空边缘：基于批准投票的多赢者投票的自动推理方法)

- **Authors / 作者:** Ratip Emin Berker, Emanuel Tewolde, Vincent Conitzer, Mingyu Guo, Marijn Heule, Lirong Xia
- **Affiliation / 机构:** Carnegie Mellon University; Foundations of Cooperative AI Lab FOCAL; University of Oxford (PDF page-1)
- **Venue / 会议:** AAAI 2026 (comments: "main body to be published in Proceedings of the Fortieth AAAI Conference on Artificial Intelligence (AAAI-26), Singapore, 2026")
- **Problem / 问题:** Whether a core-stable committee always exists in approval-based multi-winner voting remains a major open problem in computational social choice.
- **Methodology / 方法:** MILP-based approach for deciding whether/when core-stable committees are guaranteed to exist; duality-based reformulation of the core stability problem; reveals previously unknown relationships (e.g., priceability).
- **Key innovations / 关键创新:** Theoretical gains independent of the number of voters (proofs); computational speedups vs SAT-based approaches.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.16895) · [PDF](https://arxiv.org/pdf/2512.16895)

#### 2512.10892 — Designing Truthful Mechanisms for Asymptotic Fair Division (为渐近公平分配设计真实机制)

- **Authors / 作者:** Jugal Garg, Vishnu V. Narayan, Yuang Eric Shen
- **Affiliation / 机构:** University of Illinois Urbana-Champaign (PDF page-1)
- **Venue / 会议:** AAAI 2026 (comments: "To appear at AAAI 2026")
- **Problem / 问题:** Asymptotic fair division: showing envy-free allocations exist with high probability when item values are i.i.d. across agents (m = Ω(n log n / log log n)); prior mechanisms are non-strategyproof.
- **Methodology / 方法:** New randomized mechanism, truthful in expectation, efficiently implementable in poly time, outputs envy-free allocations with high probability (answers open question posed by Manurangsi & Suksompong 2017). Extensions: weighted fair division, multiple agent/good types.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.10892) · [PDF](https://arxiv.org/pdf/2512.10892)

#### 2512.00709 — When Human Preferences Flip: An Instance-Dependent Robust Loss for RLHF (当人类偏好翻转：面向 RLHF 的实例相关鲁棒损失)

- **Authors / 作者:** Yifan Xu, Xichen Ye, Yifan Chen, Qiaosheng Zhang
- **Affiliation / 机构:** Hong Kong Baptist University; Fudan University; Shanghai Artificial Intelligence Laboratory (PDF page-1)
- **Venue / 会议:** AAAI 2026 (comments: "Accepted by AAAI-26-AIA")
- **Problem / 问题:** Preference flipping (annotator flips preferences) corrupts RLHF data; robustness to flipped pairs needed.
- **Methodology / 方法:** FA-DPO (Flipping-Aware Direct Preference Optimization); instance-dependent flipping probability on the Bradley-Terry model; iterative optimization algorithm compatible with RLHF/DPO.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.00709) · [PDF](https://arxiv.org/pdf/2512.00709)

#### 2512.00881 — Hybrid-DMKG: A Hybrid Reasoning Framework over Dynamic Multimodal Knowledge Graphs for Multimodal Multihop QA with Knowledge Editing (Hybrid-DMKG：面向多模态多跳问答与知识编辑的动态多模态知识图谱混合推理框架)

- **Authors / 作者:** Li Yuan, Qingfei Huang, Bingshan Zhu, Yi Cai, Qingbao Huang, Changmeng Zheng, Zikun Deng, Tao Wang
- **Affiliation / 机构:** Key Laboratory of Big Data and Intelligent Reasoning, etc. (PDF page-1)
- **Venue / 会议:** AAAI 2026 (comments: "Accepted by AAAI 2026")
- **Problem / 问题:** Multimodal knowledge editing benchmarks assess final answer correctness but neglect reasoning quality and robustness to visually rephrased inputs (existing MKE methods struggle after updates).
- **Methodology / 方法:** Hybrid-DMKG — dynamic multimodal knowledge graph (DMKG); decomposes multihop questions into sequential sub-questions; multimodal retrieval model locates updated facts; hybrid reasoning module (relation linking + RAG reasoning); decision module aggregates evidence.
- **Key innovations / 关键创新:** MMQAKE benchmark (first for multimodal MKE); hybrid reasoning over DMKG; significantly outperforms existing MKE approaches.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.00881) · [PDF](https://arxiv.org/pdf/2512.00881)

#### 2512.00524 — Hyperbolic Continuous Structural Entropy for Hierarchical Clustering (基于双曲空间连续结构熵的层次聚类)

- **Authors / 作者:** Guangjie Zeng, Hao Peng, Angsheng Li, Li Sun, Chunyang Liu, Shengze Li, Yicheng Pan, Philip S. Yu
- **Affiliation / 机构:** School of Computer Science and Engineering, Beihang University, China; Department of Computer Science, University of Illinois Chicago, USA (PDF page-1)
- **Venue / 会议:** AAAI 2026 (comments: "14 pages, accepted by AAAI 2026")
- **Problem / 问题:** Existing hierarchical clustering methods either specify dendrograms without a global objective or neglect graph structure.
- **Methodology / 方法:** HypCSE — maps data points to hyperbolic space; minimizes relaxed continuous structural entropy (CSE) on structure-enhanced graphs; GNN encodes vertices; GSL updates graph structure during training.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.00524) · [PDF](https://arxiv.org/pdf/2512.00524)

### NeurIPS 2025

#### 2512.11193 — Learning-Augmented Facility Location Mechanisms for Envy Ratio (面向嫉妒率的学习增强设施选址机制)

- **Authors / 作者:** Haris Aziz, Yuhang Guo, Alexander Lam, Houyu Zhou
- **Affiliation / 机构:** (none on PDF page-1)
- **Venue / 会议:** NeurIPS 2025 (comments: "Accepted in NeurIPS 2025")
- **Problem / 问题:** Learning-augmented facility location on a line for the envy ratio objective (max utility ratio between any two agents).
- **Methodology / 方法:** α-Bounding Interval Mechanism (α-BIM) — predictions of the optimal solution; α-consistency + (α−1)-robustness, optimality proven; also a randomized no-predictions mechanism improving the best-known ratio from 2 to ≈1.8944 (resolving open questions); Bias-Aware Mechanism (BAM).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.11193) · [PDF](https://arxiv.org/pdf/2512.11193)

#### 2512.10292 — Certifying Concavity and Monotonicity in Games via Sum-of-Squares Hierarchies (通过平方和层级认证博弈的凹性与单调性)

- **Authors / 作者:** Vincent Leon, Iosif Sakos, Ryann Sim, Antonios Varvitsiotis
- **Affiliation / 机构:** UIUC, USA; Singapore University of Technology and Design, Singapore (PDF page-1)
- **Venue / 会议:** NeurIPS 2025 (comments: "NeurIPS 2025")
- **Problem / 问题:** Certifying concavity/monotonicity of multiplayer games is NP-hard (already for extensive-form games).
- **Methodology / 方法:** Two hierarchies of sum-of-squares programs solvable in polynomial time that certify concavity/monotonicity of a given game; SOS-concave/monotone games — the closest such game in poly time; applies to canonical examples of imperfect recall extensive-form games.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.10292) · [PDF](https://arxiv.org/pdf/2512.10292)

#### 2512.09367 — Procurement Auctions with Predictions: Improved Frugality for Facility Location (带预测的采购竞价：设施选址的改进节约机制)

- **Authors / 作者:** Eric Balkanski, Nicholas DeFilippis, Vasilis Gkatzelis, Xizhi Tan
- **Affiliation / 机构:** Columbia University; New York University; Drexel University (PDF page-1)
- **Venue / 会议:** NeurIPS 2025 (comments: "In proceeding at NeurIPS 2025")
- **Problem / 问题:** Designing truthful procurement auctions for strategic uncapacitated facility location — minimizing payment cost + connection cost (frugality ratio); private owner costs, payoffs, VCG ratio = 3 baseline.
- **Methodology / 方法:** Learning-augmented auctions with predictions of owners' private costs; family achieving reduced frugality when predictions are accurate and robust when they are not; error-tolerant auctions with improved frugality even for approximately accurate predictions.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.09367) · [PDF](https://arxiv.org/pdf/2512.09367)

#### 2512.00947 — Table as a Modality for Large Language Models (将表格作为大语言模型的一种模态)

- **Authors / 作者:** Liyao Li, Chao Ye, Wentao Ye, Yifei Sun, Zhe Jiang, Haobo Wang, Jiaming Tian, Yiming Zhang, Ningtao Wang, Xing Fu, Gang Chen, Junbo Zhao
- **Affiliation / 机构:** OpenAI; Meta AI (PDF page-1)
- **Venue / 会议:** NeurIPS 2025 (comments: "Accepted to NeurIPS 2025")
- **Problem / 问题:** Community efforts to generalise LLMs to tabular data largely rely on serialising tables, losing structural information.
- **Methodology / 方法:** TAMO — treats tables as an independent modality integrated with text tokens: hypergraph NN global table encoder + mainstream LLM; multimodal framework.
- **Experimental results / 实验结果：** Average relative gain of 42.65% on benchmarking datasets (HiTab, WikiTQ, WikiSQL, FeTaQA).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.00947) · [PDF](https://arxiv.org/pdf/2512.00947)

#### 2512.00930 — Thompson Sampling for Multi-Objective Linear Contextual Bandit (多目标线性语境老虎机的汤普森采样)

- **Authors / 作者:** Somangchan Park, Heesang Ann, Min-hwan Oh
- **Affiliation / 机构:** Seoul National University (PDF page-1)
- **Venue / 会议:** NeurIPS 2025 (comments: "NeurIPS 2025")
- **Problem / 问题:** Multi-objective linear contextual bandit — optimizing multiple conflicting objectives simultaneously.
- **Methodology / 方法:** MOL-TS — first Thompson Sampling algorithm with Pareto regret guarantees (samples parameters across objectives; effective Pareto front accounting for repeated selections).
- **Experimental results / 实验结果：** Worst-case Pareto regret bound Õ(d^{3/2}√T); improved regret minimisation and strong multi-objective performance in experiments.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.00930) · [PDF](https://arxiv.org/pdf/2512.00930)

#### 2512.00352 — Sample-Efficient Tabular Self-Play for Offline Robust Reinforcement Learning (离线鲁棒强化学习的样本高效表格式自我对弈)

- **Authors / 作者:** Na Li, Zewu Zheng, Wei Ni, Hangguan Shan, Wenjie Zhang, Xinyu Li
- **Affiliation / 机构:** Zhejiang University; The Chinese University of Hong Kong; Edith Cowan University (PDF page-1)
- **Venue / 会议:** NeurIPS 2025 (comments: "NeurIPS 2025")
- **Problem / 问题:** Robust two-player zero-sum Markov games (TZMGs) in offline settings, tabular robust TZMGs (RTZMGs).
- **Methodology / 方法:** RTZ-VI-LCB — optimistic robust value iteration with Bernstein-style penalty for robust value estimation under distribution shifts.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.00352) · [PDF](https://arxiv.org/pdf/2512.00352)

### ICLR 2026

#### 2611.00616 — Enhancing Language Model Reasoning with Structured Multi-Level Modeling (增强语言模型推理的结构化多层建模)

- **Authors / 作者:** Siheng Xiong, Ali Payani, Faramarz Fekri
- **Affiliation / 机构:** Georgia Institute of Technology; Cisco Research (PDF page-1)
- **Venue / 会议:** ICLR 2026 (comments: "ICLR 2026")
- **Problem / 问题:** Inference-time scaling via CoT often suffers from long-horizon plan failures where the implicit plan drifts from valid strategies (esp. for small LMs).
- **Methodology / 方法:** Multi-Level Reasoning (MLR) — reformulates long-CoT generation as a two-level stochastic process (high-level planner generates structured step descriptors; low-level executor produces detailed reasoning conditioned on them, alternating plan–execute); minimal LoRA-based high-level policy over a base model; outcome-reward RL gives sparse delayed feedback — introduces iterative Step-DPO (process-level preference optimisation via Twisted Sequential Monte Carlo for scalable stepwise supervision).
- **Key innovations / 关键创新:** Structured step descriptors; weaker data budget (10% SFT / 5% preference vs DeepSeek-R1 distillation); slower degradation on long-horizon reasoning.
- **Experimental results / 实验结果：** On challenging math/science/logical benchmarks, MLR outperforms SFT-based distillation and strong RL/preference-optimisation baselines across multiple base models and tasks (no specific numbers in abstract).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.00616) · [PDF](https://arxiv.org/pdf/2611.00616)

#### 2512.00272 — WARP: Weight Teleportation for Attack-Resilient Unlearning Protocols (WARP：面向抗攻击的模型遗忘协议的权重传送)

- **Authors / 作者:** Mohammad M Mahmood, Xavier Cadet, Peter Chin, Hamed Haddadi
- **Affiliation / 机构:** (none on PDF page-1)
- **Venue / 会议:** ICLR 2026 (comments: "This work has been accepted for publication at the International Conference on Learning Representations (ICLR) 2026 (to appear)")
- **Problem / 问题:** Approximate machine unlearning leaks via differences between pre/post-unlearning models (membership inference, data reconstruction).
- **Methodology / 方法:** WARP — plug-and-play "teleportation" defence leveraging neural network symmetries; reparameterisation reduces forget-set gradient energy and increases parameter dispersion while preserving predictions.
- **Experimental results / 实验结果：** Across six unlearning algorithms, adversarial advantage (AUC) reduced by up to 64% (black-box) / 92% (white-box), accuracy on retained data maintained.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.00272) · [PDF](https://arxiv.org/pdf/2512.00272)

#### 2512.01351 — Benchmarking Overton Pluralism in LLMs (评测大语言模型的 Overton 多元主义)

- **Authors / 作者:** Elinor Poole-Dayan, Jiayi Wu, Taylor Sorensen, Jiaxin Pei, Michiel A. Bakker
- **Affiliation / 机构:** MIT; Stanford University (PDF page-1)
- **Venue / 会议:** ICLR 2026 (comments: "Paper accepted to ICLR 2026")
- **Problem / 问题:** Community efforts to generalise LLMs to tabular data largely rely on serialising tables, losing structural information.
- **Methodology / 方法:** TAMO — treats tables as an independent modality integrated with text tokens: hypergraph NN global table encoder + mainstream LLM; multimodal framework.
- **Experimental results / 实验结果：** Average relative gain of 42.65% on benchmarking datasets (HiTab, WikiTQ, WikiSQL, FeTaQA).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.01351) · [PDF](https://arxiv.org/pdf/2512.01351)

### KDD 2026

#### 2512.00679 — ProEx: A Unified Framework Leveraging Large Language Model with Profile Extrapolation for Recommendation (ProEx：利用大语言模型与用户画像外推的推荐统一框架)

- **Authors / 作者:** Yi Zhang, Yiwen Zhang, Yu Wang, Tong Chen, Hongzhi Yin
- **Affiliation / 机构:** Anhui University; The University of Queensland (PDF page-1)
- **Venue / 会议:** KDD 2026 (comments: "Accepted by KDD 2026 (First Cycle)")
- **Problem / 问题:** Generating a unique user/item profile from historical interactions and mapping it into semantic space is limited by single-instance profiles; LLM instability can bias profiles and hurt recommendation performance.
- **Methodology / 方法:** ProEx — multi-faceted profile extrapolation: chain-of-thought constructs multiple distinct profiles per user/item; profiles mapped into semantic vectors ("environments"); differences across environments minimised to reveal inherent invariance of user preferences.
- **Key innovations / 关键创新:** Applied to 3 discriminative + 3 generative recommendation methods; experiments on 3 datasets show significant enhancements of the base models.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.00679) · [PDF](https://arxiv.org/pdf/2512.00679)

#### 2512.08702 — VI-MMRec: Similarity-Aware Training Cost-free Virtual User-Item Interactions for Multimodal Recommendation (VI-MMRec：基于相似度感知、零训练成本的多模态推荐虚拟用户-物品交互)

- **Authors / 作者:** Jinfeng Xu, Zheyu Chen, Shuo Yang, Jinze Li, Zitong Wan, Hewei Wang, Weijie Liu, Yijie Li, Edith C. H. Ngai
- **Affiliation / 机构:** The University of Hong Kong; Beijing Institute of Technology; University College Dublin (PDF page-1)
- **Venue / 会议:** KDD 2026 (comments: "Accepted by KDD 2026")
- **Problem / 问题:** Existing multimodal recommendation models suffer from data sparsity: unobserved items are treated as negatives arbitrarily; no training-cost-free augmentation of sparse user-item interactions.
- **Methodology / 方法:** VI-MMRec — model-agnostic, plug-and-play framework; constructs similarity-aware virtual user-item interactions from modality-specific feature similarities (Overlay aggregates modality-specific similarities; Synergistic fuses cross-modal similarities); statistically informed weight allocation adapts to dataset-specific modality relevance; no training overhead.
- **Experimental results / 实验结果：** Experiments on 6 real-world datasets × 7 SOTA multimodal recommendation models validate VI-MMRec.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.08702) · [PDF](https://arxiv.org/pdf/2512.08702)

### ACL 2026

#### 2512.01020 — Evaluating Legal Reasoning Traces with Legal Issue Tree Rubrics (基于法律问题树评分标准评估法律推理轨迹)

- **Authors / 作者:** Jinu Lee, Kyoung-Woon On, Simeng Han, Arman Cohan, Julia Hockenmaier
- **Affiliation / 机构:** University of Illinois Urbana-Champaign 2LBOX (PDF page-1)
- **Venue / 会议:** ACL 2026 (comments: "ACL 2026 Main Conference")
- **Problem / 问题:** Quality of LLM-generated reasoning traces in expert domains is hard to evaluate due to inherent complexity; current rubrics mostly check final answer correctness.
- **Methodology / 方法:** LEGIT (LEGal Issue Trees) — 24K-instance expert-level legal dataset with rubrics converting court judgments into hierarchical trees of opposing parties' arguments + court conclusions (issue coverage and correctness rubrics); human-verified; RAG + RL with rubrics tested.
- **Key innovations / 关键创新:** Shows RAG improves overall reasoning capability while RL improves correctness (reduced coverage).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.01020) · [PDF](https://arxiv.org/pdf/2512.01020)

#### 2512.01089 — CodeDistiller: Automatically Generating Code Libraries for Scientific Coding Agents (CodeDistiller：为科学编程智能体自动生成代码库)

- **Authors / 作者:** Peter Jansen, Samiah Hassan, Pragnya Narasimha
- **Affiliation / 机构:** Allen Institute for Artificial Intelligence; University of Arizona (PDF page-1)
- **Venue / 会议:** ACL 2026 (comments: "Accepted to ACL 2026 (Demo Track)")
- **Problem / 问题:** Automated Scientific Discovery (ASD) agents are limited by the code they can reliably generate from parametric knowledge alone.
- **Methodology / 方法:** CodeDistiller — distills large collections of scientific GitHub repositories into vetted libraries of working domain-specific code examples; combination of automatic + domain-expert evaluation on 250 materials-science repositories; ASD agent + CodeDistiller-generated library produces more accurate, complete, scientifically sound experiments than general examples; LLM-as-a-judge vs expert ratings in A/B testing.
- **Experimental results / 实验结果：** Best model produces functional examples for 74% of repositories; modified-nanoGPT-style experiments improved.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.01089) · [PDF](https://arxiv.org/pdf/2512.01089)

#### 2512.00311 — Tracing Mathematical Proficiency Through Problem-Solving Processes (通过解题过程追踪数学熟练度)

- **Authors / 作者:** Jungyang Park, Suho Kang, Jaewoo Park, Jaehong Kim, Jaewoo Shin, Seonjoon Park, Youngjae Yu
- **Affiliation / 机构:** Yonsei University 2Mathpresso 3Seoul National University (PDF page-1)
- **Venue / 会议:** ACL 2026 (comments: "Accepted to ACL 2026 Findings")
- **Problem / 问题:** Knowledge Tracing (KT) methods rely solely on response correctness; they neglect rich information in students' problem-solving processes (traditional KT methods lack explainability).
- **Methodology / 方法:** KT-PSP (Knowledge Tracing via Problem-Solving Process) — incorporates students' solution processes (multidimensional aspects of proficiency); KT-PSP-25 dataset (newly designed for KT-PSP); StatusKT — teacher-student-teacher three-stage LLM pipeline extracting mathematical proficiency (MP) as intermediate representation.
- **Experimental results / 实验结果：** StatusKT improves prediction performance on KT-PSP-25 vs existing KT methods; provides interpretable explanations of predictions.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.00311) · [PDF](https://arxiv.org/pdf/2512.00311)

### SIGIR 2026

#### 2512.06883 — Structural and Disentangled Adaptation of Large Vision Language Models for Multimodal Recommendation (面向多模态推荐的大视觉语言模型结构与解耦适配)

- **Authors / 作者:** Zhongtao Rao, Peilin Zhou, Dading Chong, Zhiwei Chen, Shoujin Wang, Nan Tang
- **Affiliation / 机构:** The Hong Kong University of Science and Technology (Guangzhou) (PDF page-1)
- **Venue / 会议:** SIGIR 2026 (comments: "Accepted to SIGIR '26")
- **Problem / 问题:** Applying LVLMs to recommendation is challenged by (i) representation misalignment (domain gaps between item data and pre-training → unaligned embedding spaces) and (ii) gradient conflicts during fine-tuning (shared adapters, lack of discriminative power).
- **Methodology / 方法:** SDA (Structural and Disentangled Adaptation) — integrates Cross-Modal Structural Alignment (CMSA, soft teacher from intra-modal structures) and Modality-Disentangled Adaptation (MoDA, gated low-rank expert paths mitigate gradient conflicts and disentangle gradient flows).
- **Experimental results / 实验结果：** On 3 public Amazon datasets: +6.15% Hit@10, +8.64% NDCG@10 vs existing multimodal/sequential recommenders; up to +12.83% and +18.70% on long-tail items with minimal inference overhead; code/results at url.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.06883) · [PDF](https://arxiv.org/pdf/2512.06883)

### CVPR 2026
> No new CVPR 2026 venue-tagged papers (coverage through the 2026-11-21 digest: 2611.23887, 2611.22506, 2611.20625, 2611.09191, 2611.03438).

### EMNLP 2025
> No new EMNLP 2025 venue-tagged papers (coverage through the 2026-11-21 digest). EMNLP-2026-tagged papers in the window appear under the LLMs/topic sections (e.g., 2611.00442).

### WWW 2026
> No new WWW 2026 venue-tagged papers (coverage through the 2026-11-21 digest).

### CIKM 2025
> No new CIKM 2025 venue-tagged papers (coverage through the 2026-11-21 digest).

### RecSys 2025
> No new RecSys 2025 venue-tagged papers (coverage through the 2026-11-21 digest).

---

## 2. Topic digest — general AI/ML recent papers (主题日报 — 近期 AI/ML 论文)

### LLMs

#### 2611.23949 — Incremental Speciation in Evolutionary Red Teaming of Large Language Models (大语言模型进化红队测试中的增量群系分化)

- **Affiliation / 机构:** Rochester Institute of Technology, Rochester NY 14623
- **Venue / 会议:** LLM topic (no venue tag)
- **Problem / 问题:** Speciation structures (species-aware parent selection via representation-based compatibility) depend on the assignment operator turning pairwise relations into species; design space under-explored for text-based individuals.
- **Methodology / 方法:** Comparing embedding dissimilarity (MiniLM d_E) vs DeBERTa-v3-small NLI non-entailment (d¬E); two speciation structures (representative-based, density-based); offline calibration on 3,139-prompt archive; online validation under matched evaluation budget.
- **Experimental results / 实验结果：** Representation-dependent connectivity predicts population structure more consistently than endpoint fitness; species count alone does not establish quality-diversity; MiniLM incremental DBSCAN maintains mature niches; NLI reaches the same highest observed median fitness while concentrating high-fitness prompts in few seed topics; bootstrap intervals include zero (no reliable advantage detected).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.23949) · [PDF](https://arxiv.org/pdf/2611.23949)

#### 2611.00554 — From Weeks to Hours: Fast and Principled SFT Data Generation for Reasoning LLMs (从周到小时：快速且原则化的推理 LLM 监督微调数据生成)

- **Affiliation / 机构:** University of California, Los Angeles Optum AI
- **Venue / 会议:** NeurIPS 2026 (comments); LLM topic
- **Problem / 问题:** SFT data curation relies on costly generate-then-filter pipelines taking weeks; hard to scale.
- **Methodology / 方法:** SFTProbe — LoRA-based adaptation evaluating loss on 5% of each reasoning trace; geometric view: pretrained LLMs lie in a low-rank anisotropic loss basin; probing via low-rank perturbations; clustering loss signatures captures diversity; loss at curvature inflection points proxies difficulty; simple teacher-selection criterion.
- **Experimental results / 实验结果：** Reduces data curation from weeks to hours while maintaining/improving performance; on mathematical reasoning, 5k generated examples match the 89k-example filtered OpenThoughts-Math, and 7.5k beats it by 2.5% accuracy; trains a model outperforming an IPhO 2025 silver-medal-winning model.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.00554) · [PDF](https://arxiv.org/pdf/2611.00554)

#### 2611.00871 — ShiftRAG: Bypassing the Textual Bottleneck via Decoupled Learning and Continuous Soft Tokens (ShiftRAG：通过解耦学习与连续软令牌绕过文本瓶颈)

- **Affiliation / 机构:** Department of AI, Hanyang University; Department of Data Science, Hanyang University
- **Venue / 会议:** NeurIPS 2026 (comments); LLM topic
- **Problem / 问题:** Unifying retrieval and generation in a single LLM induces severe objective conflict, degrading performance on both tasks.
- **Methodology / 方法:** ShiftRAG — decoupled RAG: single LLM backbone; discriminative retrieval learning isolated from autoregressive generation; bridges the two modes by projecting retrieval alignments into continuous soft tokens (high-bandwidth interface); soft orthogonality objective mitigates rank collapse; layer-wise relevance dynamics preserve latent space.
- **Experimental results / 实验结果：** Significantly improves retrieval and QA over SOTA baselines; preserves foundational backbone capabilities with favorable efficiency-performance trade-off.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.00871) · [PDF](https://arxiv.org/pdf/2611.00871)

#### 2611.01320 — Step-dLLM: Adaptive Step-aware Sparse Attention for Efficient Diffusion LLM Inference (Step-dLLM：面向高效扩散 LLM 推理的自适应分步感知稀疏注意力)

- **Affiliation / 机构:** University of Washington; University of Waterloo; Northwestern University; Cornell University; Meta AI
- **Venue / 会议:** NeurIPS 2026 (comments); LLM topic
- **Problem / 问题:** dLLMs recompute the full attention map at every step (quadratic per-step cost); existing sparse attention methods allocate the sparsity budget uniformly across heads and construct the mask after a full-attention warm-up.
- **Methodology / 方法:** Step-dLLM — periodically refreshes a block-sparse mask at anchor steps along the denoising trajectory and reuses it within each locally consistent interval (attention patterns shift abruptly); head-adaptive global budget compresses heads with concentrated attention more aggressively; fused IO-aware Triton kernel.
- **Experimental results / 实验结果：** Applies to LLaDA-1.5 and Dream-7B-Instruct without retraining; 2.78× end-to-end speedup over dense FlashAttention on LLaDA-1.5 at 8K context with 256 denoising steps and 90% sparsity; improves accuracy-latency trade-off vs prior sparse-attention methods.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.01320) · [PDF](https://arxiv.org/pdf/2611.01320)

#### 2611.00286 — Quantization of Large Models with Weight Outliers and Sparsity (大模型量化：权重异常值与稀疏性)

- **Affiliation / 机构:** Department of ECE, University of Minnesota, Minneapolis, MN 55455
- **Venue / 会议:** NeurIPS 2026 workshop; LLM topic
- **Problem / 问题:** PTQ on LMs suffers from quantization error from weight outliers.
- **Methodology / 方法:** Decomposes weights into quantized + low-rank + sparse (outlier rows); simulated annealing search to avoid poor local minima.
- **Experimental results / 实验结果：** Outperforms direct quantization markedly; minimal memory overhead; evaluated on Llama 3.2 1B/3B, Llama 3.1 8B, Qwen2.5 7B on generation benchmarks with 4-bit NF4/FP4.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.00286) · [PDF](https://arxiv.org/pdf/2611.00286)

### Recommendation Systems

#### 2512.00656 — Sycophancy Claims about Language Models: The Missing Human-in-the-Loop (关于语言模型的好好先生倾向：缺失的人机回路)

- **Affiliation / 机构:** Weizenbaum Institute; Technical University Berlin; Munich Center for Machine Learning & Technical University Munich
- **Venue / 会议:** NeurIPS 2025 workshop (LLM Evaluation) & ICLR 2025 workshop (Bi-Directional Human-AI Alignment); Recommendation topic
- **Problem / 问题:** Sycophantic response patterns claimed increasing in literature but hard to measure; sycophancy is inherently human-centric but human perception unmeasured.
- **Methodology / 方法:** Review of methodological challenges; identifies five core operationalisations; actionable recommendations.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.00656) · [PDF](https://arxiv.org/pdf/2512.00656)

#### 2512.07846 — MixLM: High-Throughput and Effective LLM Ranking via Text-Embedding Mix-Interaction (MixLM：通过文本-嵌入混合交互实现高吞吐高效的 LLM 排序)

- **Affiliation / 机构:** (none on PDF page-1)
- **Venue / 会议:** Recommendation topic (LinkedIn deployment)
- **Problem / 问题:** LLM rerankers create long context prefill-heavy workloads; industry needs high-throughput LLM search ranking.
- **Methodology / 方法:** MixLM — mixture of text and embedding tokens; encodes catalog items into few embedding tokens (nearline cache); uses encoded descriptions online; shared insights from LinkedIn deployment (training pipelines, serving optimizations).
- **Experimental results / 实验结果：** 10.0× throughput vs strong baselines (75.9× vs full-text LLM rerankers) at same latency; +0.47% DAU increase in A/B tests.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.07846) · [PDF](https://arxiv.org/pdf/2512.07846)

#### 2611.03113 — Preprocessing Choices in Fine-Tuning Data Matter: Utility and Demographic Sensitivity in LLM-Based Recommendation (微调数据的预处理选择很重要：基于 LLM 的推荐中的效用与人口统计敏感性)

- **Affiliation / 机构:** Istanbul Technical University
- **Venue / 会议:** EARL at CIKM 2026 ( workshop); Recommendation topic
- **Problem / 问题:** Preprocessing choices (item-title representation, demographic balancing, auxiliary knowledge) affect recommendation utility and fairness-related behavior, but are rarely evaluated jointly.
- **Methodology / 方法:** Controlled LLM-based recommendation pipeline; controlled preprocessing study on MovieLens-1M (catalog-constrained decoding, prompt augmentation, three preprocessing choices).
- **Experimental results / 实验结果：** Original titles improve HR@10 from 10.67% to 12.47% and Coverage@10 from 41.36% to 47.88%; age balancing reduces group-level utility gaps; gender balancing reduces utility without improving gender indicators.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.03113) · [PDF](https://arxiv.org/pdf/2611.03113)

#### 2512.07650 — Exploring Test-time Scaling via Prediction Merging on Large-Scale Recommendation (探索大规模推荐中基于预测合并的测试时缩放)

- **Affiliation / 机构:** MBZUAI; McGill University; MILA — Quebec AI Institute; Shenzhen Technology University
- **Venue / 会议:** Recommendation topic
- **Problem / 问题:** Test-time scaling in DLRS is underexplored — how to efficiently generate diverse meaningful outputs per instance under inference budgets.
- **Methodology / 方法:** Two approaches: heterogeneity of model architectures; randomness of model initialisation under homogeneous architectures; evaluated across 8 classic/SOTA models on 3 benchmarks.
- **Experimental results / 实验结果：** Test-time scaling outperforms parameter scaling under the same inference budget; seamless acceleration with parallel servers; no user-side inference-time changes.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.07650) · [PDF](https://arxiv.org/pdf/2512.07650)

### Advertising / CTR
> Note: 2 papers matched loose topic patterns (2611.26011, 2611.13940) but are not advertising/CTR: 2611.26011 is a cryptography paper on Evolving Partial Spreads for Bent Functions; 2611.13940 is an optimization paper on Tailoring Optimization Approaches with Domain Knowledge in Industry Process for Meta-heuristic Development.

### Games

#### 2610.00715 — Robust Nash Alignment under Preference Uncertainty (偏好不确定性下的鲁棒纳什对齐)

- **Affiliation / 机构:** University of Central Florida; University of Colorado Boulder
- **Venue / 会议:** 2026 40th NeurIPS (Advances in Neural Information Processing Systems); Games topic
- **Problem / 问题:** Preference-based alignment methods are brittle when pairwise preferences are noisy, heterogeneous, or shift after deployment (single preference model assumed).
- **Methodology / 方法:** Robust Nash Alignment — four-player primal-dual proxy game (major learner + follower + adversarial preference kernel + dual variable); single-loop optimistic mirror descent-ascent algorithm; ambiguity set around nominal preference captures uncertainty.
- **Experimental results / 实验结果：** O(1/√T) convergence of duality gap; near-optimal robust policy; improved robustness to preference perturbations on tabular games and LLM alignment with uncertain preferences.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2610.00715) · [PDF](https://arxiv.org/pdf/2610.00715)

#### 2512.12582 — Generative AI as Digital Representatives in Collective Decision-Making: A Game-Theoretical Approach (生成式 AI 作为集体决策中的数字代表：博弈论视角)

- **Affiliation / 机构:** Google
- **Venue / 会议:** ECAI 2025; Games topic
- **Problem / 问题:** Digital representatives (GenAI deciding on behalf of team members) face preference-representation fidelity challenges (complete information access impractical).
- **Methodology / 方法:** Game-theoretic framework modeling strategic information revelation to GenAI; characterises members' equilibrium behaviour under interdependent strategies; quantifies imperfect preference-learning outcomes.
- **Experimental results / 实验结果：** Members paradoxically achieve decisions more aligned with their preferences when using digital representatives when manual participation costs are high or GenAI is advanced.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.12582) · [PDF](https://arxiv.org/pdf/2512.12582)

#### 2512.17238 — Fairly Dividing Non-identical Random Items: Just Sample or Match (公平分配非同构随机物品：只采样还是匹配)

- **Affiliation / 机构:** National University of Singapore; Indian Institute of Technology, Bombay
- **Venue / 会议:** Games topic
- **Problem / 问题:** Existence of envy-free + efficient allocations for non-identical items (non-identical distributions U_j); need for fast computation.
- **Methodology / 方法:** Shows envy-free and max social-welfare efficient allocations exist with high probability asymptotically; when m = O(n log n), sampling O(log m) or O((log m)^2) utilities per item suffices to compute allocations in Õ(m) time.
- **Experimental results / 实验结果：** Simulations show small multiplicative losses even for small instances, converging to fully optimal guarantees quickly.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.17238) · [PDF](https://arxiv.org/pdf/2512.17238)

#### 2512.16570 — Online Resource Allocation via Static Bundle Pricing (基于静态捆绑定价的在线资源分配)

- **Affiliation / 机构:** National Technical University of Athens, Greece
- **Venue / 会议:** Games topic
- **Problem / 问题:** Online resource allocation with sequential buyer arrivals (values from known distributions, strong complementarities); static/anonymous bundle pricing analysis for complementarity environments.
- **Methodology / 方法:** Unified bundle-pricing framework for three well-studied domains (single-minded combinatorial auctions, network routing); exponential improvement with item multiplicity.
- **Experimental results / 实验结果：** O(d^{1/B})-competitive for d-single-minded with min multiplicity B; O(m^{1/(B+1)}) for general single-minded and network routing; information-theoretic lower bounds derived.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.16570) · [PDF](https://arxiv.org/pdf/2512.16570)

#### 2512.16514 — Blockchain Monetary Policy, Strategic Participation, and the Dynamics of Decentralization (区块链货币政策、战略参与与去中心化动态)

- **Affiliation / 机构:** University of Salerno
- **Venue / 会议:** Games topic
- **Problem / 问题:** Blockchain systems navigate a tradeoff between rewarding capable participants and preserving sufficient stake decentralisation (winner selection under capability types + evolving stakes).
- **Methodology / 方法:** Algorithmic reward policies in dynamic blockchain environments with publicly known capability types and evolving token stakes; analysis of stage equilibria under myopic behaviour in a repeated participation game.
- **Experimental results / 实验结果：** Performance-first designs can drive the system to minimum decentralisation under myopic play; three design benchmarks identified (top-k types, lookahead simulation, broad-sharing) that mitigate failures with tradeoffs in participation, robustness, and performance.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.16514) · [PDF](https://arxiv.org/pdf/2512.16514)

### Code Execution Prediction
> No new papers (coverage through earlier digests; e.g., MaskPE — UMass Amherst, 2026-11-21 digest — reported earlier).

### Agents & Agent Systems

#### 2611.00300 — Cross-Lingual Persona Effects in LLM Negotiation (LLM 谈判中的跨语言角色效应)

- **Affiliation / 机构:** Georgia Institute of Technology
- **Venue / 会议:** SocialAgent Workshop at NeurIPS 2026; Agents topic
- **Problem / 问题:** Cross-lingual social-policy fidelity — whether prompt-defined social policies produce the same behavioural effect in every language (negotiation persona + urgency + language effects on agreement rates).
- **Methodology / 方法:** Identical buyer/seller Gemini 3.6 Flash instances negotiating 12 Joey Crabshift Bargain scenarios in English and Korean (2×2×3 design, 432 negotiations).
- **Experimental results / 实验结果：** Korean negotiations: 77.3% vs 52.5% English agreement (Holm-adjusted p = .0039) for neutral/headstrong buyers; Korean was lower on opening offers but larger seller concessions and smaller final gap; repeat with Qwen3.7 Flash supports directional agreement (+13.9 points for Korean).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.00300) · [PDF](https://arxiv.org/pdf/2611.00300)

#### 2611.00442 — Fidelity Collapses with Table Size, Not Turn Count: Delivery Architecture in a Deployed Tool-Using Agent (保真度随表大小而非轮数崩溃：部署的工具使用智能体的投递架构)

- **Affiliation / 机构:** OpenAI; Anthropic; Google
- **Venue / 会议:** REALM at EMNLP 2026 (non-archival); Agents topic
- **Problem / 问题:** Multi-turn agents delivering tool records into context suffer from data corruption across turns (unobserved data the tool computed correctly).
- **Methodology / 方法:** Two-architecture evaluation over identical frozen payloads (SYNTHESIS vs BYPASS) in a production award-travel agent: BYPASS keeps records in session state and uses a deterministic filter via a typed side channel; SYNTHESIS re-emits records each turn.
- **Experimental results / 实验结果：** BYPASS 92.3% of turns fully correct vs SYNTHESIS 45.7% (+46.6pp gap); SYNTHESIS collapses from near-perfect at ≤10 rows to ≤8% beyond ~74 rows; beyond 100 rows, each correct SYNTHESIS answer costs ~200× BYPASS's flat cost.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.00442) · [PDF](https://arxiv.org/pdf/2611.00442)

#### 2610.16158 — CIPHEUR: LLM-Guided Structural Search Control for Conflict-Graph Optimization (CIPHEUR：面向冲突图优化的 LLM 引导结构搜索控制)

- **Affiliation / 机构:** National University of Defense; Dalian Maritime University; Jiangsu University of Technology
- **Venue / 会议:** Agents topic
- **Problem / 问题:** Conflict-graph search stagnates when interventions fail to address conflicts blocking progress; disruptive interventions may require further search before value emerges.
- **Methodology / 方法:** CIPHEUR — LLM-guided Structured Intervention Units (SIUs); shared control interface; offline synthesis of executable policies + online contextual decisions.
- **Experimental results / 实验结果：** Across 8 satellite-ground scheduling conflict views × 5 runs: CIPHEUR-online achieves the highest mean objective; mean scheduled contact duration +14.84% over GWMIN; exceeds strongest external per-view mean in 7/8 views.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2610.16158) · [PDF](https://arxiv.org/pdf/2610.16158)

#### 2611.00050 — ReactionBench: A Human-Anchored Benchmark for Modeling Reactions to Video (ReactionBench：建模视频反应的人类锚定基准)

- **Affiliation / 机构:** UIUC; Massachusetts; Independent Researcher; NUS
- **Venue / 会议:** IAEval at NeurIPS 2026; Agents topic
- **Problem / 问题:** Reaction-specific video understanding is underexplored: relating viewer reactions to stimulus context.
- **Methodology / 方法:** ReactionBench — human-anchored benchmark built from 31,834 synchronized stimulus-reaction clips (433 hours, 8 domains); evaluates intensity ranking, stimulus-reaction matching, and reaction explanation (447 blind-written human references).
- **Experimental results / 实验结果：** Best model 50.9% on four-way stimulus-reaction matching; GPT-5 shows no detectable loss under reaction substitution.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.00050) · [PDF](https://arxiv.org/pdf/2611.00050)

#### 2610.00511 — Before Agents Decide: Epistemic Action in LLM-Based Systems (智能体决策之前：基于 LLM 系统中的认知行动)

- **Affiliation / 机构:** Fox School of Business, Temple University; Robert H. Smith School of Business, University of Maryland
- **Venue / 会议:** FAST at NeurIPS 2026; Agents topic
- **Problem / 问题:** LLM-based agents search and explore, but agent design gives less attention to the question of whether evidence is ready for the decision before deciding.
- **Methodology / 方法:** Three epistemic action modes: acquiring missing evidence, transforming available evidence, probing a system to create a revealing response; "epistemic scaffolding" interfaces/tools/environments make these actions auditable.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2610.00511) · [PDF](https://arxiv.org/pdf/2610.00511)

### Generative Models

#### 2512.13576 — Reproducing and Dissecting Denoising Language Models for Speech Recognition (复现与解构面向语音识别的去噪语言模型)

- **Affiliation / 机构:** (none on PDF page-1)
- **Venue / 会议:** Generative topic (DLMs for ASR)
- **Problem / 问题:** DLM complexity hindered wider investigation; first independent large-scale empirical study of DLMs.
- **Methodology / 方法:** First independent, large-scale empirical study of DLMs: builds and releases a complete reproducible pipeline; evaluates dozens of configurations across data augmentation (SpecAugment, dropout, mixup), text-to-speech systems, decoding strategies; DLM-sum decoding from multiple ASR hypotheses (outperforms DSR decoding).
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.13576) · [PDF](https://arxiv.org/pdf/2512.13576)

#### 2512.12582 — Generative AI as Digital Representatives in Collective Decision-Making: A Game-Theoretical Approach (see Games section above — reported under Games)

*(Also tagged Generative; see Games.)*

### Sequential Modeling

#### 2610.03727 — On the Tightness and Computational Tractability of Higher-Dimensional Confidence Sequences (高维信念序列的紧致性与计算可处理性)

- **Affiliation / 机构:** Eindhoven University of Technology; University of Amsterdam
- **Venue / 会议:** NeurIPS 2026 (Spotlight); Sequential topic
- **Problem / 问题:** Multivariate confidence sequences for bounded vector means are either tight but computationally intractable, or fast to compute but conservative — limits multi-metric A/B testing and model comparison.
- **Methodology / 方法:** Studies three lifts of 1-D betting-based CSs: weighted Bonferroni region, max-wealth form, portfolio region; proposes tractable outer approximations (bounding box, ℓp-ellipsoid, intersection) preserving statistical validity; proves set relations and empirically evaluates approximation tightness, competitive performance vs existing tractable CSs, and multi-metric use cases.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2610.03727) · [PDF](https://arxiv.org/pdf/2610.03727)

#### 2512.09218 — Dynamic Graph Coloring: Sequential, Parallel, and Distributed (动态图着色：顺序、并行与分布式)

- **Affiliation / 机构:** (none on PDF page-1)
- **Venue / 会议:** SODA 2027; Sequential topic
- **Problem / 问题:** Maintaining a (Δ+1)-coloring as the graph undergoes edge insertions/deletions — needs an ideal parallelization and distributed protocol.
- **Methodology / 方法:** Randomized dynamic graph coloring — sequential O(1) expected time per update (matches/strengthens Henzinger–Peng, Bhattacharya 2022); parallel: O(1) work per update in batch with poly(log n) depth; distributed with O(1) expected message complexity.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2512.09218) · [PDF](https://arxiv.org/pdf/2512.09218)

### Benchmarks

#### 2611.00586 — Dataset Mismatch Matters in Group Relative Policy Optimization for Reinforcement Learning from Verifiable Rewards (数据集不匹配对面向可验证奖励的强化学习中组相对策略优化的影响)

- **Affiliation / 机构:** OpenAI
- **Venue / 会议:** NeurIPS 2026 (comments); Benchmarks topic
- **Problem / 问题:** Source training data is rarely identically distributed to target test data; when mismatch exists, sharing target prompts is unacceptable, so target-side feedback is limited to small held-out aggregated statistics.
- **Methodology / 方法:** L2RR (learning-to-reweight rollout) — learns a discrete sampling distribution over source prompts by optimising a bi-level objective (max accuracy on held-out target dataset while penalising low-incremental-learning rollouts).
- **Experimental results / 实验结果：** 6 math benchmarks × 3 model scales: L2RR improves target-domain performance and increases rollout efficiency.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.00586) · [PDF](https://arxiv.org/pdf/2611.00586)

#### 2611.00319 — GAVAGAI: Referential Alignment for Infant-Scale Vision-Language Models via Balanced Optimal Transport (GAVAGAI：基于平衡最优传输的婴儿规模视觉-语言模型的指称对齐)

- **Affiliation / 机构:** Jadavpur University
- **Venue / 会议:** BabyVLM Workshop at NeurIPS 2026; Benchmarks topic
- **Problem / 问题:** VLMs bind words to referents far less reliably than infants; the next-token captioning objective has no variable for "this word refers to that region" so training applies no pressure to ground words.
- **Methodology / 方法:** Entropic optimal transport with a NOTHING column (words not naming visible things) + capacity constraint (mutual exclusivity); Sinkhorn ≈ 8 iterations; on SAYCam infant video: word-to-picture accuracy 32.4%→48.7%, localization IoU 0.18→0.38.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.00319) · [PDF](https://arxiv.org/pdf/2611.00319)

#### 2611.00077 — AegisBench: Auditing Aerial Search-and-Rescue Person Detection Under the Conditions It Is Deployed In (AegisBench：审计面向实际部署条件的无人机搜救人体检测)

- **Affiliation / 机构:** (none on PDF page-1)
- **Venue / 会议:** AI4GOOD workshop at NeurIPS 2026; Benchmarks topic
- **Problem / 问题:** Detector datasets are collected in calm, clear daylight, while missions deploy in floods, wildfires, storms, at night — the deployment gap is unmeasured.
- **Methodology / 方法:** AegisBench — 9 physically-motivated corruptions (4 disaster families × 3 severities) applied to HERIDAL + SARD; 3 architecture detectors (Faster R-CNN, YOLOv11, RT-DETR) scored across 168 conditions by one evaluator.
- **Experimental results / 实验结果：** Low light (4.5-stop exposure loss) drives recall to exactly zero for all detectors on both datasets (mirrored on 300 real night drone images, 2/759 people found); fine-tuning on milder low-light recovers 0.06–0.19 recall at held-out severity.
- **Links / 链接:** [arXiv](https://arxiv.org/abs/2611.00077) · [PDF](https://arxiv.org/pdf/2611.00077)

---

*Notes: venue papers are new to the wiki (deduped against all existing wiki pages); topic papers are sorted by arXiv submission date; all metrics/results/claims are author-reported; Chinese titles are translation aids; technical terms stay in English.*
