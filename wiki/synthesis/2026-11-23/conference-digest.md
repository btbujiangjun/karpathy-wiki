---
title: "Conference Digest 2026-11-23 — Top ML/AI Conferences (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) + General AI/ML"
type: synthesis
created: 2026-11-23
updated: 2026-11-23
sources: ["2611.00420", "2611.00281", "2610.34418", "2609.07194", "2608.11260", "2611.02253", "2609.05818", "2610.17844", "2611.13641", "2611.00616", "2611.23678", "2610.41368", "2608.20614", "2611.22506", "2610.39946", "2610.36419", "2611.18930", "2607.10787", "2607.03213", "2512.02593", "2605.27374", "2610.33078", "2608.20389", "2605.10530", "2603.25498", "2603.24973", "2603.01104", "2512.16925", "2510.25220", "2611.13972", "2510.13359", "2510.06657", "2611.25659", "2611.24283", "2611.26060", "2611.26807", "2611.26624", "2611.06254", "2611.23613", "2611.22016", "2611.10843", "2611.23803", "2611.23388", "2611.27074", "2611.27173", "2611.27186", "2611.23045", "2611.27155", "2611.27206", "2611.08321", "2611.23621", "2611.22410", "2611.21176"]
tags: [conference-digest, ICML2026, AAAI2026, NeurIPS2025, ICLR2026, KDD2026, CVPR2026, ACL2026, EMNLP2025, SIGIR2026, WWW2026, CIKM2025, RecSys2025, recommendation, advertising, CTR, LLM, agents, generative-models, sequential-modeling, games, code-execution, benchmarks, daily-digest]
---

# Conference Digest — 2026-11-23

> Digest of newly accepted/published papers from top ML/AI conferences (ICML 2026, AAAI 2026, NeurIPS 2025, ICLR 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025) plus general AI/LLM/recommendation/ad/CTR/games/code-execution/agent/generative/sequential/benchmark papers from arXiv. Data sourced from arXiv (abstracts, PDF first pages for affiliations); numbers are author-reported, not independently verified.

---

### ICML 2026: Circuit Oracle: Automating Attribution Graph Analysis via Natural-Language Queries (电路或头：通过自然语言查询自动化归因图分析)

- **arXiv**: [2611.00420](https://arxiv.org/abs/2611.00420) · **Venue**: ICML 2026 · **Published**: 2026-10-30
- **Title (English)**: Circuit Oracle: Automating Attribution Graph Analysis via Natural-Language Queries
- **Title (Chinese)**: 电路或头：通过自然语言查询自动化归因图分析
- **Authors**: Shariar Kabir, Hong Kiat Tan, Swastik Agrawal, Sai V R Chereddy, Sriram Balasubramanian
- **Affiliation**: 1Independent Researcher; 2University of California, Los Angeles, CA, USA; 3The University of Maryland, College Park, MD, USA

**Problem background**: 归因图作为机制可解释性工具，用 Transcoder 把 LM 计算分解为稀疏可解释特征并建立因果边，但把图转成安全相关的洞察仍需数小时人工。

**Methodology & innovations**:
开箱即用的 LLM + 多智能体技能包：直接读归因图、自动生成裁剪子图与特征解释； 三类安全相关代理任务：虚假特征检测（78.2% ± 2.4 准确率，超单层特征排序基线 72.5%、SAE 65.0%）、密秘获取（训练得出的自解释模型仍优于激活 Oracle）、拒绝绕过（50 次提示中单次干预略低于差分均值基线，最优 5 次尝试后反而略高）。

**Comparison with prior methods**: 相比既有方法：用 LLM 读归因图的办法避免了原始深度的人工分析，Circuit Oracle 改进了单层特征排序基线在虚假特征检测上 78.2% 的准确率，且在 5 次采样稳定、跨模型稳定。

**Experimental results**: 虚假特征检测 78.2% ± 2.4 准确率（Transcoder 72.5%、SAE 65.0%）；密秘获取展示 Activation Oracle 仍最强；拒绝绕过在 best-of-5 下略优。

**Abstract**: Attribution graphs, an emerging tool in mechanistic interpretability, use transcoders to decompose language model computations into sparse interpretable features connected by causal edges. However, turning a graph into a safety-relevant insight requires hours of manual analysis by experts. We introduce Circuit Oracle, an off-the-shelf LLM equipped with a multi-agent harness and task-specific authored skills, which answers natural-language questions about a target model by reading the attribution graph through tool calls. We evaluate it on three safety-relevant proxy tasks: detecting spurious features in probe circuits, eliciting hidden knowledge from taboo-finetuned models, and suppression jailbreaking via feature-level interventions. Beyond task scores, the oracle produces pruned subgraphs and context-specific feature explanations that we assess qualitatively. Results are mixed. On spurious-feature detection, Circuit Oracle reaches 78.2 ± 2.4% accuracy, outperforming single-layer feature-ranking baselines. On secret elicitation, trained self-explainers like Activation Oracles remain the stronger baseline. On refusal suppression over 50 prompts, its single committed intervention is slightly below a diff-in-means baseline, and only exceeds it when allowed the best of five attempts. Results are stable across five runs and across model choices for the agents. We also release the pruned subgraphs and context-specific feature readings that revise existing global labels, and invite future work to develop evaluations that can measure their usefulness directly.


### ICML 2026: DELBERT-2: Pretrained Fingerprint Language Models for DEL Protein Binder Prediction (DELBERT-2：面向 DEL 蛋白结合预测的指纹语言模型预训练)

- **arXiv**: [2611.00281](https://arxiv.org/abs/2611.00281) · **Venue**: ICML 2026 · **Published**: 2026-10-30
- **Title (English)**: DELBERT-2: Pretrained Fingerprint Language Models for DEL Protein Binder Prediction
- **Title (Chinese)**: DELBERT-2：面向 DEL 蛋白结合预测的指纹语言模型预训练
- **Authors**: Bing Hu, Sun Sun, Shaik Salman Basha, Anita Layton, Helen Chen
- **Affiliation**: 1Computer Science, University of Waterloo, Canada 2National; University of Waterloo, Canada 4School of Public Health, Uni-

**Problem background**: 药物结合筛选的早期阶段需要高置信度的结合亲和，稀疏的分子指纹是关键输入，但将其建模要么依赖特征工程，要么由通用 LLM/MolFormer 等模型处理。

**Methodology & innovations**:
以指纹为中心的自监督预训练（掩码语言建模 + ModernBERT），用统一 token 序列替代固定分子表征； 三种OOD 协议：化学复合物块、跨药物库、构建块组合；

**Comparison with prior methods**: 对比 LightGBM 集成基线与从零训练的 Transformer，DELBERT-2 在近乎最大 OOD 歧义中 PR-AUC、NDCG@1000 更优。

**Experimental results**: top-100 富集因子 13.28 ± 3.72 vs 无预训练 12.36 ± 3.75（p=0.040），较随机扩大 13 倍、提升 7.4%；拆掉 MLM 预训练即差。

**Abstract**: We present DELBERT-2, a pretrained fingerprint language model that converts sparse molecular fingerprints into unified token sequences using a ModernBERT encoder trained with masked language modelling on 2.5M molecules from the AIRCHECK DEL corpus. We evaluate across six targets (WDR91, WDR12, SETDB1, PLCZ1, LRRK2, DCAF7) under three out-of-distribution (OOD) protocols: hierarchical cluster splits probe chemical novelty, library splits test cross-library transfer, and building-block splits assess compositional generalization. DELBERT-2 consistently improves PR-AUC and NDCG@1000 relative to LightGBM ensemble baselines and transformers trained from scratch, with the largest gains in stringent OOD regimes. DELBERT-2 achieves 13.28+/-3.72 enrichment factor at top-100 vs. 12.36+/-3.75 for no-pretraining (p=0.040), representing 7.4% improvement and 13x enrichment over random selection. These results demonstrate that fingerprint-centric self-supervised learning effectively improves hit prioritization under distribution shift, enabling practical DEL virtual screening. Code is available at \hyperlink{ this https URL {DELBERT-2.


### ICML 2026: MulFCoder: Framework-conditioned Multi-agent for MLLM-based Multi-framework Front-end Code Generation (MulFCoder：框架条件多智能体框架（UI 截图→多框架前端代码生成）)

- **arXiv**: [2610.34418](https://arxiv.org/abs/2610.34418) · **Venue**: ICML 2026 · **Published**: 2026-10-25
- **Title (English)**: MulFCoder: Framework-conditioned Multi-agent for MLLM-based Multi-framework Front-end Code Generation
- **Title (Chinese)**: MulFCoder：框架条件多智能体框架（UI 截图→多框架前端代码生成）
- **Authors**: Jie Wu, Haoran Ma, Shisong Tang, Yulin Xu, Xiaoyu Kang, Jiechao Gao
- **Affiliation**: University of China 2Harvard University 3Tsinghua university; 4University of Southern California 5Chinese Academy of Sci-; ences 6Stanford University. Correspondence to: Jiechao Gao; <jiechao@stanford.edu>.

**Problem background**: MLLM 把 UI 截图翻译成 HTML/CSS 成功率尚可，但 React/Vue/Angular 三框架下表现差距大且错误模式框架特异性强，提示词微调效果较差。

**Methodology & innovations**:
把框架约束显式编码为可分析的"可决策规则空间"，针对 React/Vue/Angular 三者生成 4 智能体分工 + 契约反馈闭环，减少框架间互相泄漏和无界重试

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Generating runnable front-end code from UI screenshots is a long-standing goal in automated software engineering. Existing MLLM-based methods predominantly focused on HTML/CSS, leaving multi-framework generation for React/Vue/Angular underexplored. Naively modifying prompts leads to substantial performance gaps across multi-framework and highly framework-specific error modes. To address this, we propose MulFCoder, a framework-conditioned multi-agent method that explicitly encodes framework constraints to bring multi-framework differences into a decidable rule space. MulFCoder orchestrates four agents: Grounder constructs an ElementTable, ContentTable, and macro-layout regions from detected UI elements; Planner builds a DOM-like hierarchical layout tree, produces a task schedule, and derives a framework-specific file Contract; Writer generates structured file writes or patches within a restricted edit window; Judger enforces lightweight, framework-conditioned constraints to accept or reject updates and trigger bounded repairs, preventing drift and deadlocks without expensive builds. Experiments demonstrate that MulFCoder substantially improves compilation success rate and reduces framework-specific errors, with particularly pronounced gains on Angular.


### AAAI 2026: EmoMed: An Emotionally-Aware Agent for Multimodal Medical Support with Real-Time Information Retrieval (EmoMed：情感感知多模态医疗咨询智能体)

- **arXiv**: [2609.07194](https://arxiv.org/abs/2609.07194) · **Venue**: AAAI 2026 · **Published**: 2026-09-07
- **Title (English)**: EmoMed: An Emotionally-Aware Agent for Multimodal Medical Support with Real-Time Information Retrieval
- **Title (Chinese)**: EmoMed：情感感知多模态医疗咨询智能体
- **Authors**: Ivan Nasonov, Nikita Glazkov, Ivan Makovetskiy, Mikhail Mozikov, Daniil Sukhorukov, Andrey Savchenko, Ilya Makarov
- **Affiliation**: 1 ISP RAS Research Center for Trusted Artificial Intelligence, 109004 Moscow,; 3 National University of Science and Technology (NUST) MISIS, 119049 Moscow,; 4 SB AI Lab, 117997 Moscow, Russia; 5 Research Center of the Artificial Intelligence Institute, Innopolis University, 420500

**Problem background**: 医疗对话的情绪适应性回应直接影响用户信任与治疗效果，但既有医疗 AI 缺乏情绪感知与临床事实核验的联动。

**Methodology & innovations**:
情感自适应回应校准：LLM-as-judge 评估、MedQA 风格准确率、BERTScore、安全/有用性评分； 多模态情绪输入（文本 + 医学图像）+ 持续更新的知识库（云端 + API 同步）。

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: We present EmoMed - a multimodal medical consultation agent that adapts its responses based on users' emotional states while maintaining clinical accuracy. The system processes text and medical images, detects affect indicators (anxiety, confusion, urgency) from user input, and adjusts response tone, structure, and detail level accordingly. To ensure factual reliability, the agent grounds clinical information through a dual retrieval mechanism: web-based fact-checking and an API-connected, continuously updated medical knowledge base. We evaluate our approach across seven state-of-the-art language models (GPT-4/5, Qwen3, Llama 4, Gemini 2.5, Grok4, Claude3) using comprehensive metrics including LLM-as-judge assessments, MedQA style accuracy tests, BERT Score, safety/helpfulness ratings, and multimodal medical benchmarks. The results demonstrate that emotionally adaptive responses consistently outperform neutral baseline across evaluation dimensions, without compromising clinical accuracy. A controlled user study validated these findings, with participants reporting improved perceived empathy and communication clarity, while maintaining trust in factual accuracy. Source code: this https URL


### AAAI 2026: Glance, Scrutinize, and Think: Advancing Video Anomaly Detection from Training-Free to Agentic Reasoning (Glance、Scrutinize、Think：从无训练到智能推理的异常视频检测)

- **arXiv**: [2608.11260](https://arxiv.org/abs/2608.11260) · **Venue**: AAAI 2026 · **Published**: 2026-08-07
- **Title (English)**: Glance, Scrutinize, and Think: Advancing Video Anomaly Detection from Training-Free to Agentic Reasoning
- **Title (Chinese)**: Glance、Scrutinize、Think：从无训练到智能推理的异常视频检测
- **Authors**: Shibo Gao, Peipei Yang, Xu-Yao Zhang, Linlin Huang
- **Affiliation**: 1School of Electronic and Information Engineering, Beijing; Jiaotong University, Beijing 100044, China.; 2Institute of Automation, Chinese Academy of Sciences, Beijing; 3State Key Laboratory of Multimodal Artificial Intelligence; Systems, Institute of Automation, Chinese Academy of Sciences,

**Problem background**: 传统无训练 VAD 缺乏时间定位；LLM 形式论定位了但不接地。VAD 需要 "何时+何种" 的全局-局部推理。

**Methodology & innovations**:
静态+动态文本引导，先平衡全局假设与局部检查； 以模型审查视频帧、复核异常点、迭代校正，减少离线模型的泛化弱点。

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Video Anomaly Detection (VAD) aims to identify anomalous events and localize their temporal intervals. Existing approaches exhibit a "when-what" dissociation: traditional DNN-based methods localize when anomalies occur but lack semantic understanding, whereas LLM-based methods explain what happens but neglect precise temporal grounding. We attribute this to the absence of a unified reasoning paradigm. Inspired by how humans inspect surveillance videos - glancing globally to form temporal hypotheses, scrutinizing suspicious segments, and thinking iteratively to correct errors - we study this global-to-local paradigm from two perspectives. We first propose Glance then Scrutinize (GtS), a training-free framework using static and dynamic textual guidance for coarse-to-fine anomaly grounding and understanding, balancing accuracy and speed. To break the ceiling imposed by frozen external modules, we further propose a tool-augmented agentic VAD method, where a multimodal large language model learns to invoke a video cropping tool, inspect densely resampled frames, and self-correct mislocalized hypotheses, via cold-start supervised fine-tuning followed by reinforcement learning with a joint answer-grounding reward. For training and evaluation, we extend our prior VAGU benchmark into VAGU-T (Video Anomaly Grounding, Understanding, and Thinking), comprising 7,567 real-world videos over 21 anomaly categories with human-validated grounding, explanations, QA pairs, and chain-of-thought tool-calling traces. We further introduce JeAUG, a metric jointly evaluating semantic interpretability and temporal precision. Experiments show that GtS substantially surpasses training-free baselines, while the agentic model delivers both higher accuracy and faster inference.


### NeurIPS 2025: Calibration-Constrained Diagnostics for Evaluating LLM Self-Evaluation (用于评估 LLM 自我评估的校准约束诊断)

- **arXiv**: [2611.02253](https://arxiv.org/abs/2611.02253) · **Venue**: NeurIPS 2025 · **Published**: 2026-11-01
- **Title (English)**: Calibration-Constrained Diagnostics for Evaluating LLM Self-Evaluation
- **Title (Chinese)**: 用于评估 LLM 自我评估的校准约束诊断
- **Authors**: Jae Oh Woo, Mengdie Flora Wang, Rahul Ghosh, Baishali Chaudhury, Mun Young Kim
- **Affiliation**: AWS Generative AI Innovation Center; {jaeohwoo, florawan, rahulgh, baishch, munkim}@amazon.com

**Problem background**: LLM 自我报告的置信度常用于做或推迟决策，但聚合校准指标可能掩盖分类级不一致；评估缺乏工程化。

**Methodology & innovations**:
聚合与约束分离：同一模型在聚合校准指标下可看似最强，但在类别级约束下失效（类别级校准更受高置信选择边界约束）。

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: We introduce a reusable evaluation artifact for diagnosing whether LLM self-reported confidence can support confidence-gated act-or-defer decisions. The artifact is designed for evaluation rather than safety certification: it provides a black-box protocol, prompts, judge-reference labels, model outputs, reproduction scripts, and calibration-constrained diagnostic metrics for auditing LLM self-evaluation across math, factual, and commonsense reasoning tasks. Our central finding is that aggregate uncertainty summaries can produce deployment-misleading rankings: a model that appears strongest under standard aggregate calibration metrics can fail under category-level calibration constraints, while a model with worse aggregate calibration can exhibit stronger calibration-constrained behavior in the positive-margin region where high self-selection accuracy and tight calibration coexist. To expose this failure mode, we define PVC and C-PVC as category-level diagnostics over an accuracy-by-calibration surface: PVC counts categories whose self-evaluation accuracy exceeds a threshold, while C-PVC additionally requires category-level calibration error below a tolerance. We aggregate these diagnostics using Volume Under Surface (VUS) and a positive-margin restriction; they are VC/fat-shattering motivated but are empirical evaluation proxies, not literal VC-dimension estimates. Across 13 models and four benchmarks, the artifact shows weak confidence-correctness separation, stable diagnostic rankings under alternative categorizations and judge-label perturbations, and persistent positive-margin failures not captured by ECE or Brier score. Confidence-gated self-evaluation therefore requires calibration-constrained, category-level diagnostics, and we provide a reusable artifact for applying them under black-box access.


### NeurIPS 2025: Agentic BAIM-LLM Evaluation (ABLE): Benchmarking LLM Use of Protein Design Tools (Agentic BAIM-LLM 评估（ABLE）：用 LLM 使用蛋白设计工具的基准)

- **arXiv**: [2609.05818](https://arxiv.org/abs/2609.05818) · **Venue**: NeurIPS 2025 · **Published**: 2026-09-05
- **Title (English)**: Agentic BAIM-LLM Evaluation (ABLE): Benchmarking LLM Use of Protein Design Tools
- **Title (Chinese)**: Agentic BAIM-LLM 评估（ABLE）：用 LLM 使用蛋白设计工具的基准
- **Authors**: Bryce Cai, Geetha Jeyapragasan, Samira Nedungadi, Jake Yukich, Seth Donoughe
- **Affiliation**: *Equal contribution 1SecureBio, Cambridge, MA, USA. Corre-

**Problem background**: 前沿 LLM 越来越多地调用生物 AI 模型（BAIM）完成蛋白设计，但缺乏对智能体在复杂生物工作流中可靠性的系统评估。

**Methodology & innovations**:
覆盖工具选择、工具使用与规划策略，包含多轮、多步骤双层任务与结构检索的专家基准对比

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: We introduce ABLE, a benchmark for evaluating LLM agents' ability to use biological AI models (BAIMs), such as ProteinMPNN and AlphaFold3, in dual-use protein design workflows. ABLE assesses agent performance through a set of tasks spanning structure retrieval, sequence generation, and design validation. We evaluate 15 frontier models and find that seven refuse all tasks, while the remaining models exhibit substantial performance differences. Claude Sonnet 4 and Gemini 3 Pro achieve the highest scores across information retrieval, tool selection, and tool use. We further compare model performance on a subset of tasks against an expert human baseline. Our results suggest that current LLMs can substantially lower barriers to protein design, but remain inconsistent in planning, strategy generation, and integrating biological knowledge with tool use.


### NeurIPS 2025: What Makes a Good Visual Representation for Spatial Understanding in MLLMs? (MLLM 空间理解：通过外部视觉/几何/生成模型间的表示迁移)

- **arXiv**: [2610.17844](https://arxiv.org/abs/2610.17844) · **Venue**: NeurIPS 2025 · **Published**: 2026-10-13
- **Title (English)**: What Makes a Good Visual Representation for Spatial Understanding in MLLMs?
- **Title (Chinese)**: MLLM 空间理解：通过外部视觉/几何/生成模型间的表示迁移
- **Authors**: Xiaohu Huang, Yumin Guo, Kai Han
- **Affiliation**: Not listed on arXiv page

**Problem background**: MLLM 只用 2D 图像预训练，缺乏 3D 结构，空间理解是推进物理世界推理的关键；已有工作证明迁移结构有助，但"把什么东西迁移"较"怎么迁移"只看性质差异。

**Methodology & innovations**:
把结构引入形状与点云完全空缺；时空一致性（形状坍塌情况与机制）随对象数量平方增长。

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Spatial understanding is a necessary step in moving multimodal large language models (MLLMs) toward reasoning about the 3D physical world. Their visual pretraining data, however, is almost entirely 2D, so the visual tokens processed by MLLMs often lack inherent 3D structural information. A growing number of methods inject such structure by transferring representations from external vision or geometry models, and collectively establish that such transfer helps. Behind these methods lies a largely underexplored question: what makes a visual representation good for spatial understanding? To answer it, we first separate what is transferred from how it is transferred, and then trace the resulting differences back to properties of the representations themselves. What we transfer comes from 3D geometry models, self-supervised image and video models, vision-language models, and generative models, in the form of latent features or explicit depth and point maps. We transfer it either by distillation, using it as a supervision target, or by fusion, feeding it as an additional input. We find that a representation's 3D structure correlates strongly with how much it helps, measured by cross-view consistency for latent features and by depth and reconstruction accuracy for explicit geometry. We further show that the form of a representation dictates the mechanism it needs. Latent features gain as much from fusion as from distillation; explicit geometry gains little from fusion, and most of its distillation gain depends on a geometry decoding head. Guided by these findings, we distill both latent features and explicit geometry into a single MLLM. Taking only RGB video as input, it consistently improves over its base model on both static 3D and dynamic 4D spatial reasoning benchmarks.


### ICLR 2026: MOAI: Module-Optimizing Architecture for non-interactive secure transformer Inference (MOAI：非交互式安全 Transformer 推理的模块化架构)

- **arXiv**: [2611.13641](https://arxiv.org/abs/2611.13641) · **Venue**: ICLR 2026 · **Published**: 2026-11-10
- **Title (English)**: MOAI: Module-Optimizing Architecture for non-interactive secure transformer Inference
- **Title (Chinese)**: MOAI：非交互式安全 Transformer 推理的模块化架构
- **Authors**: Linru Zhang, Xiangning Wang, Jun Jie Sim, Zhicong Huang, Jiahao Zhong, Huaxiong Wang, Pu Duan, Kwok-Yan Lam
- **Affiliation**: 1Nanyang Technological University,2Ant International, 3Ant Group

**Problem background**: HE 对 LLM 推理耗时且不可交互；作者用 SM2 的多层结构论证需要改进 HE 推理引擎。

**Methodology & innovations**:
层级数组化编码器，转换成更紧凑架构（全局特征解耦），并以 2/3 倍数的惩罚收益指数稀疏化；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Privacy concerns have been raised in Large Language Models (LLM) inference when models are deployed in Cloud Service Providers (CSP). Homomorphic encryption (HE) offers a promising solution by enabling secure inference directly over encrypted inputs. However, the high computational overhead of HE remains a major bottleneck. To address this challenge, we propose MOAI, an efficient HE-based, non-interactive framework for secure transformer inference. MOAI gains significant efficiency improvement from: (1) a novel evaluation flow that combines column and diagonal packing with consistent strategies across all layers, eliminating expensive format conversions. (2) rotation-free algorithms for Softmax and LayerNorm that significantly reduce the number of costly HE rotations, removing 2,448 HE rotations in BERT-base inference. (3) Column packing removes rotations in plaintext-ciphertext matrix multiplications and interleaved batching further reduces the rotations in ciphertext-ciphertext matrix multiplications. MOAI uses at least 1.7x fewer HE rotations compared to the state-of-the-art works across all matrix multiplications of BERT-base. As a result, we achieve a 52.8 \% reduction in evaluation time compared to the state-of-the-art HE-based non-interactive secure transformer inference, THOR (Moon et al., CCS 25). We then apply MOAI on the Powerformer's framework and achieve a 55.7 \% reduction in evaluation time compared to Powerformer (Park et al., ACL 25), which approximates Softmax and LayerNorm with simpler functions in transformer and proposes HE-based non-interactive transformer inference. We report an amortized time of 2.36 minutes per input on a single GPU environment. We show the extendibility by applying MOAI in LLaMA-3-8B. Our implementation is publicly available as open source.


### ICLR 2026: Enhancing Language Model Reasoning with Structured Multi-Level Modeling (用结构化多层推理增强语言模型推理)

- **arXiv**: [2611.00616](https://arxiv.org/abs/2611.00616) · **Venue**: ICLR 2026 · **Published**: 2026-10-31
- **Title (English)**: Enhancing Language Model Reasoning with Structured Multi-Level Modeling
- **Title (Chinese)**: 用结构化多层推理增强语言模型推理
- **Authors**: Siheng Xiong, Ali Payani, Faramarz Fekri
- **Affiliation**: 1Georgia Institute of Technology 2Cisco Research; 1Code and data are available athttps://github.com/xiongsiheng/MLR.; OpenAI’s o1 series (OpenAI, 2024) introduce inference-time scaling by allocating more computation

**Problem background**: 推理时扩展（如 CoT）受限于单策略 RL 的长期规划；在小模型上常见规划漂移。

**Methodology & innovations**:
把规划与执行分层建模，以 LoRA 轻量化层级策略；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Inference-time scaling enhances a model's reasoning by extending its chain-of-thought (CoT). However, existing approaches typically rely on a single policy trained with outcome-reward reinforcement learning (RL), which often suffers from long-horizon plan failures where the implicit plan drifts from valid strategies, especially for small LMs with limited capacity. To address this, we propose Multi-Level Reasoning (MLR), which reformulates long-CoT generation as a two-level stochastic process. A high-level planner generates structured step descriptors specifying both the reasoning mode and the semantic subgoal. The low-level executor then produces detailed reasoning conditioned on these descriptors, forming an alternating plan--execute loop. To maintain scalability, we adopt a minimal design where the base model serves as the low-level policy and a lightweight LoRA module implements the high-level policy. For training, we observe that outcome-reward RL provides sparse and delayed feedback for long trajectories (e.g., several thousand tokens), hindering credit assignment. We therefore introduce iterative Step-DPO, a process-level preference optimization scheme that leverages Twisted Sequential Monte Carlo (TSMC) to provide scalable stepwise supervision. This yields more effective training, improved stability, and higher accuracy. Extensive experiments on challenging math, science, and logical reasoning benchmarks show that, under the same reduced data budget (10% SFT and 5% preference relative to the DeepSeek-R1 distillation setup), MLR outperforms both SFT-based distillation and strong RL/preference-optimization baselines across multiple base models and tasks. Moreover, MLR exhibits slower performance degradation on long-horizon reasoning, demonstrating stronger robustness under extended CoT generation.


### KDD 2026: Evaluating Governed LLM-Driven ML Experimentation: Lifecycle, Provenance, and Failure Metrics (评估 LLM 驱动的 ML 实验治理：生命周期、溯源与失败指标)

- **arXiv**: [2611.23678](https://arxiv.org/abs/2611.23678) · **Venue**: KDD 2026 · **Published**: 2026-11-18
- **Title (English)**: Evaluating Governed LLM-Driven ML Experimentation: Lifecycle, Provenance, and Failure Metrics
- **Title (Chinese)**: 评估 LLM 驱动的 ML 实验治理：生命周期、溯源与失败指标
- **Authors**: Dowling Wong
- **Affiliation**: Karlsruhe Institute of Technology

**Problem background**: 自主 Agent 跑实验常按准确率排名，但无法判断改动轨迹（可逆性、溯源、失败处理）；监管需求上升。

**Methodology & innovations**:
治理化执行框架 + 对比不治理对照；以 1,445 个 trials（含语言模型训练任务）验证。

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Autonomous agents that run ML experiments are usually judged by the best score they reach. That score says nothing about how it was reached: whether the agent stayed within the files it was allowed to edit, whether failed trials were kept or silently dropped, and whether each keep or discard decision can be traced to its evidence. We propose evaluating such systems on their experimental process as well as their outcome, and we build a governed harness that makes this possible. A control plane, not the LLM that proposes changes, owns each trial's lifecycle, checks its edit scope, decides keep or discard, and appends one record per trial to an append-only ledger. Governance metrics such as the invalid-action rate, the repeated-bad rate and provenance completeness are computed from that ledger. Across six ML tasks, from synthetic logistic regression to language-model training, and 1,445 trials, the same contract applied unchanged. The ledger exposed failures that a task score hides: a no-memory arm in which all 120 trials failed, a benchmark adapter whose bounded proposals ran out, and a reset failure that reproducibility hashes revealed, after which the affected campaigns were rerun. In a matched counterfactual, a loop that logs only successful trials left no record of 43 of 50 trials, while the governed ledger recorded all 50. Memory ablations show that memory's effect on repeated bad proposals depends on the task. We release the ledgers of all 1,445 trials, so that every number reported for them can be recomputed.


### KDD 2026: RECITE: Revising Eligibility Criteria Incorporating Textual Evidence (RECITE：结合文本证据的资格标准修订)

- **arXiv**: [2610.41368](https://arxiv.org/abs/2610.41368) · **Venue**: KDD 2026 · **Published**: 2026-10-30
- **Title (English)**: RECITE: Revising Eligibility Criteria Incorporating Textual Evidence
- **Title (Chinese)**: RECITE：结合文本证据的资格标准修订
- **Authors**: Russell Ro, Reza Abbasi-Asl
- **Affiliation**: 1University of California, San Francisco 2University of California, Berkeley

**Problem background**: 临床试验资格标准常过于严格，致招募失败；现有方法难以接地文档证据与试验设计。

**Methodology & innovations**:
LLM-as-judge 评估 + 合成生成与医学专家的对齐校验（quad. weighted Cohen's κ）。

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Overly restrictive eligibility criteria contribute to widespread enrollment failure in clinical trials, yet published recommendations for how specific criteria should be broadened remain disconnected from trial design at scale. We introduce RECITE (Revising Eligibility Criteria Incorporating Textual Evidence), a framework for automated discovery, extraction, and implementation of evidence-based eligibility criteria revisions. RECITE uses protocol amendment documents from this http URL to construct a dataset of 11,913 curated instances across 5,735 trials, each pairing original criteria with documentary evidence and target revisions. We benchmark fifteen LLM configurations under truncated-to-context-window and retrieval-augmented generation conditions, on a 3,116-instance sample under an LLM-as-judge protocol validated against ten domain experts (judge vs. human quadratic-weighted Cohen's \kappa_{qw = 0.694 ± 0.096). The best open-weight model, Gemma 2 9B, achieves \kappa_{qw-aligned ordinal score 3.0 ± 0.9 on a 0--4 scale (normalized 0.742) and the best closed-weight model, GPT-4o, reaches 3.0 ± 0.8 (normalized 0.745). Using an agentic literature discovery system, we then identified 44 paper--trial matches across five publications providing trial-design and EC-modification evidence. Our findings suggest that existing clinical knowledge can be operationalized into actionable trial design recommendations.


### KDD 2026: Evaluating Skills, Not Just Agents: Agentic Continuous Evaluation of Skills (ACES：基于轨迹等级的 Agent Skill 评估)

- **arXiv**: [2608.20614](https://arxiv.org/abs/2608.20614) · **Venue**: KDD 2026 · **Published**: 2026-08-20
- **Title (English)**: Evaluating Skills, Not Just Agents: Agentic Continuous Evaluation of Skills
- **Title (Chinese)**: ACES：基于轨迹等级的 Agent Skill 评估
- **Authors**: Christopher Kevin, Narendran Raghavan, Jean-Francois Puget, Roshni Malani, Meghana Puvvadi, Moshe Abramovitch, Mohit Gupta, Rama Akkiraju, Subodh Prabhu, Yogesh Dangi, Wei Luo, Seong Hee Lee
- **Affiliation**: NVIDIA; christopherk@nvidia.com; baseline, skill, bundle, team-skill, and plugin targets.; tion of the methodology is available in NVIDIA SkillEvaluator.

**Problem background**: Enterprise Agent 已搬入生产，Skill/Tool/Workflow 需要能力包评审，但现有方法只查结构/风格/安全。

**Methodology & innovations**:
Skill 价值指标 = 启用 Skill 的两个 Agent 之间的成功率差；广泛任务 87.5% / 执行任务 89.9%；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Enterprise agent programs are moving from prototypes into production, where reusable skills, tools, and workflow packages must be reviewed with evidence rather than prose. Current gates often scan these artifacts for structure, style, and security, but they do not answer the deployment question: does the capability package help a live agent complete enterprise tasks under the same model, sandbox, and grading policy? We present ACES (Agentic Continuous Evaluation of Skills), a repository-native framework for evaluating skills and product capability packages as executable agent artifacts. ACES runs paired live trials with and without a target skill, normalizes trajectories into the Agent Trajectory Interchange Format (ATIF), grades six default runtime metrics, and reports Skill Lift: the target skill's added value for a fixed task, harness, workspace, and scorer. The same protocol supports product-owned task suites that compare baseline, skill, bundle, team-skill, and plugin targets. On 145 real skills from internal enterprise repositories and public catalogs, scan-only gates surface useful authoring issues but measure complementary facets (structural versus LLM-judge Spearman \rho = 0.14). Across 947 scored paired cases from 58 of 64 production skills and four primary harnesses, mean composite Skill Lift is 0.2134 (95\% paired-case CI [0.1967, 0.2301]); mean outcome-only lift, the average of accuracy and goal accuracy, is 0.1799. Composite lift is positive in 72.8\% of paired cases. The largest process-metric gains appear in skill execution, behavior check, and skill efficiency---signals about discovery, routing, workflow following, and tool use that document scans cannot observe. An open-source implementation of the methodology is available in NVIDIA SkillEvaluator.


### CVPR 2026: EfficientVPR: Toward Efficient Visual Place Recognition via Scene-Aware Prompt Tuning and Adaptive Feature Enhancement (EfficientVPR：基于场景感知提示调优的高效视觉位置识别)

- **arXiv**: [2611.22506](https://arxiv.org/abs/2611.22506) · **Venue**: CVPR 2026 · **Published**: 2026-11-17
- **Title (English)**: EfficientVPR: Toward Efficient Visual Place Recognition via Scene-Aware Prompt Tuning and Adaptive Feature Enhancement
- **Title (Chinese)**: EfficientVPR：基于场景感知提示调优的高效视觉位置识别
- **Authors**: Wenjing Tang, Chuanguang Yang, Zhulin An, Libo Huang, Yongjun Xu
- **Affiliation**: 1State Key Laboratory of AI Safety, Institute of Computing Technology, Chinese Academy of Sciences; 2University of Chinese Academy of Sciences, Beijing, China

**Problem background**: VPR 需处理极端环境变化与可部署精度，模型放大或重排序计算开销大。

**Methodology & innovations**:
场景感知视觉提示调优：自适应调整预训练特征，更少参数，动态接受样本级特征；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Visual place recognition (VPR) faces critical challenges in handling extreme environmental variations while meeting the computational constraints of practical applications. Current methods predominantly address these challenges by either scaling up model capacity or employing computationally intensive reranking stages, creating a significant efficiency bottleneck. To overcome this limitation, we propose EfficientVPR, a lightweight one-stage framework that achieves speed-accuracy trade-offs through two key innovations: i) a scene-aware visual prompt tuning method which adapts pretrained features with less parameters while dynamically adjusting to sample-specific characteristics, and ii) an instance-dependent key local feature enhancement module that further reinforces discriminative regions. Comprehensive evaluations on Pitts250k, MSLS, Eynsham, AmsterTime and SVOX demonstrate that our method establishes a new SOTA for DINOv2-small models by outperforming all same-scale competitors, and delivers a 73× speedup with 60\% lower-dimensional features while maintaining competitive (within 2.5% average R@1 gap) against the SOTA DINOv2-large-based two-stage method. Our code will be available at this https URL .


### CVPR 2026: ElasticFormer: Detecting Objects in HRW Shots via Elastic Computing Vision Transformer (ElasticFormer：HRW 远景目标检测的稀疏视觉 Transformer)

- **arXiv**: [2610.39946](https://arxiv.org/abs/2610.39946) · **Venue**: CVPR 2026 · **Published**: 2026-10-29
- **Title (English)**: ElasticFormer: Detecting Objects in HRW Shots via Elastic Computing Vision Transformer
- **Title (Chinese)**: ElasticFormer：HRW 远景目标检测的稀疏视觉 Transformer
- **Authors**: Wenxi Li, Jingchen Huang, Chenyang Lyu, Moran Liu, Haozhe Lin, Guiguang Ding, Yuchen Guo
- **Affiliation**: §Beijing National Research Center for Information Science and Technology,; Tsinghua University, Beijing, China; ¶Department of Automation, Tsinghua University, Beijing, China; ‡KLATASDS-MOE, School of Statistics, East China Normal University, Shanghai, China; ⋆School of Software, Tsinghua University, Beijing, China

**Problem background**: HRW 图像极其稀疏且分辨率高，检测器若贴近视觉分辨率却受背景淹没，Sparse 编码器固定稀疏度不适应多样目标数。

**Methodology & innovations**:
全局与前景动态切换；对前景高比例窗建设性权重；仅 +3.9 mAP 增益，计算效率与 MSL 系列相当；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Recent advances in gigapixel-level imaging have brought High-Resolution Wide shots to the forefront of research. However, these images present significant challenges: extreme sparsity of foreground, gigapixel-level resolutions and diverse target counts. This makes traditional close-up detectors inaccurate and slow as they are overwhelmed by the background. Although previous research has explored sparse backbones, their fixed sparsity patterns lack the adaptability required to handle diverse target numbers. To address this, we introduce ElasticFormer, a sparse backbone that dynamically allocates computational resources based on foreground proportion. After scoring windows based on variance, proposed ElasticSelector module will predict the foreground proportion for top-k selection. The mechanism guides the model to select target-containing windows, scaling resources in areas where objects are clustered. We introduce a novel loss function combined with the 3-phase training strategy for ElasticSelector, allowing it to function properly when bounding box annotations are missing. A WSOD study is carried on PASCAL VOC 2007 to evaluate its extensibility. Further, ElasticNet is created to verify its backbone-agnostic nature. In experiments on the PANDA gigapixel benchmark, ElasticFormer reduces backbone FLOPs by 80% while achieving a significant improvement in AP50 when compared to fixed-ratio sparse methods.


### CVPR 2026: SpeeDiff: Scalable Pixel-Anchored End-to-End Latent Diffusion Model (SpeeDiff：可扩展端到端潜在扩散模型（从零联训 VAE + DiT）)

- **arXiv**: [2610.36419](https://arxiv.org/abs/2610.36419) · **Venue**: CVPR 2026 · **Published**: 2026-10-26
- **Title (English)**: SpeeDiff: Scalable Pixel-Anchored End-to-End Latent Diffusion Model
- **Title (Chinese)**: SpeeDiff：可扩展端到端潜在扩散模型（从零联训 VAE + DiT）
- **Authors**: Bingliang Zhang, Wenda Chu, Yizhuo Li, Linjie Yang, Yisong Yue, Katherine L. Bouman, Yang Song, Qiushan Guo
- **Affiliation**: 1ByteDance Seed 2California Institute of Technology 3Meta

**Problem background**: 联训 VAE 传统上比较弱（收敛慢、扭曲），且无法接地 DiT 的早期选定表示。

**Methodology & innovations**:
端到端联训（VAE+DiT），36% 生成质量提升并收敛速度加快；TPR 抑制潜在空间崩溃，语义一致性 mAP 提升 6.8%。

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: We present Scalable Pixel-anchored End-to-end Diffusion (SpeeDiff), a latent diffusion method that jointly trains the VAE and the diffusion model from scratch. In principle, joint training allows the diffusion loss gradient to directly guide the VAE encoder, encouraging the formation of a generation-friendly latent space and potentially yielding faster convergence than the conventional two-stage approach with a pretrained frozen VAE. However, a naive end-to-end implementation severely degrades performance, as unrestricted backpropagation of the diffusion loss leads to latent space collapse. Our main technical contribution is a simple yet effective Tweedie Pixel Reconstruction (TPR) loss, which provides additional pixel-level feedback by decoding a predicted clean latent from an intermediate noisy state using Tweedie's formula, thereby alleviating collapse. Furthermore, our method enables jointly scaling a fully transformer-based architecture and enhances representation alignment within the end-to-end framework. Our SpeeDiff-XL model achieves over 140x and 61x faster training compared to Vanilla SiT and REPA, respectively, while attaining an FID of 1.50 without guidance on ImageNet 256x256 generation. With a more efficient 32x compressed VAE, our model further reaches an FID of 1.53 without guidance on ImageNet 512x512 generation.


### ACL 2026: Between Rigor and Reality: How AI Safety Benchmark Developers Understand Benchmark Use and Maintenance (Rigor and Reality: AI Safety Benchmarks Developers Understand — Safety (Benchmarks Developer Understanding: 2nd Edition))

- **arXiv**: [2611.18930](https://arxiv.org/abs/2611.18930) · **Venue**: ACL 2026 · **Published**: 2026-11-13
- **Title (English)**: Between Rigor and Reality: How AI Safety Benchmark Developers Understand Benchmark Use and Maintenance
- **Title (Chinese)**: Rigor and Reality: AI Safety Benchmarks Developers Understand — Safety (Benchmarks Developer Understanding: 2nd Edition)
- **Authors**: Megan Li, Ningjing Tang, Christopher Stewart, Hoda Heidari, Hong Shen
- **Affiliation**: Carnegie Mellon University‡; Correspondence:meganli@andrew.cmu.edu, ningjint@andrew.cmu.edu, cstewar3@andrew.cmu.edu

**Problem background**: 安全基准在安全评估中经常失效，五节实访学科与工业界安全基准开发者，揭示感知其功能与实际用途的脱节，互利研究与数据集的转变，基准应整合而非只是统计。

**Methodology & innovations**:
表达基准应整合在实际部署中，不仅发布；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Safety benchmarks are cited as the primary tool to understand the risks posed by generative AI (GenAI) systems, yet growing evidence suggests they often fail to meet the needs of real-world safety evaluation. We present findings from five interviews with AI safety benchmark developers in academia and industry. We find a disconnect between perceptions of the intended usefulness of safety benchmarks and their practical usefulness in safety evaluations of deployed systems. Our participants offered perspectives on two challenges contributing to this disconnect: (1) the difficulty of achieving inter-rater reliability on safety constructs, and (2) a lack of clarity regarding how to address persistent threats to external validity. Based on our analysis, we argue that safety benchmarks must not only be grounded in deployment contexts, but actively integrated with them. To facilitate this, we outline pathways for more transparent communication between academic and industry AI safety stakeholders.


### ACL 2026: Detecting AI-Generated Video: A Vision-Language Dual-View Survey (检测 AI 生成视频：Vision-Language 双视图调研)

- **arXiv**: [2607.10787](https://arxiv.org/abs/2607.10787) · **Venue**: ACL 2026 · **Published**: 2026-07-12
- **Title (English)**: Detecting AI-Generated Video: A Vision-Language Dual-View Survey
- **Title (Chinese)**: 检测 AI 生成视频：Vision-Language 双视图调研
- **Authors**: Dylan Xinming Hou, Juntian Zhang, Xu Gu, Yichen Wu, Nils Lukas, Gus Xia, Xiuying Chen, Yuhan Liu
- **Affiliation**: 1MBZUAI, 2Gaoling School of Artificial Intelligence, Renmin University of China,; 3Harvard University; {zhangjuntian, guxu}@ruc.edu.cn, yiwu6@mgh.harvard.edu

**Problem background**: AI 生成视频真实度提升，以长度为策略向高维度转变。

**Methodology & innovations**:
四层双视图分类：内在信号、时空一致性、跨模态推理、语言引导；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: The evolving realism of AI-generated Videos (AIGC-V) is rapidly rendering traditional artifact-centric detection insufficient, necessitating a paradigm shift from low-level inspection to high-level semantic verification. This paper presents a comprehensive survey of AIGC-V detection, reframing the task as Factual Fidelity Verification, which asks whether the events, entities, and physical processes depicted in a video are consistent with real-world facts. To systematize this rapidly evolving field, we propose a Vision-Language Dual-View taxonomy that organizes existing methods into a hierarchical, four-layer landscape, spanning intrinsic cue analysis, spatiotemporal consistency modeling, cross-modal consistency reasoning, and language-guided world-level reasoning. This dual-view framing highlights a fundamental transition from artifact matching in traditional deepfake detection to evidence-based semantic verification enabled by vision-language models and agentic reasoning pipelines. Based on a systematic review of 221 works, we synthesize AIGC-V generation paradigms, survey the landscape of detection methods, and review evaluation metrics and benchmarks in line with proposed views. Finally, we discuss current challenges and identify promising directions toward robust, explainable, and trustworthy detection.


### ACL 2026: OpenGlass: A Sensing-Computing Split Architecture for Local MLLM-Driven Real-Time Visual Assistance (OpenGlass：面向非视障可视化助手的本地化多模态架构)

- **arXiv**: [2607.03213](https://arxiv.org/abs/2607.03213) · **Venue**: ACL 2026 · **Published**: 2026-07-03
- **Title (English)**: OpenGlass: A Sensing-Computing Split Architecture for Local MLLM-Driven Real-Time Visual Assistance
- **Title (Chinese)**: OpenGlass：面向非视障可视化助手的本地化多模态架构
- **Authors**: Mengzhang Li, Yuan Yao
- **Affiliation**: 1Shanghai Qizhi Institute, 2College of AI, Tsinghua University; ini (Team et al., 2023), and Qwen (Bai et al., 2023),

**Problem background**: 云 MLLM 强但上传隐私、9 秒时延；眼镜仅能感知但本地计算受限。

**Methodology & innovations**:
本地工作流：ESP32 WiFi 感知 + 附近消费设备本地推理与语音，所有关键交互数据与推理均留在用户设备；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: We present OpenGlass, an open-source, privacy-oriented, local-first system for low-latency multimodal visual assistance, with a primary focus on blind and low-vision users. Cloud MLLM assistants offer strong visual understanding, but often require uploading first-person visual data and can suffer multi-second network delays; wearable glasses are ideal for sensing, but cannot host large models under tight compute and power budgets. OpenGlass addresses this gap with a sensing-computing split: an ESP32-based glasses-side unit captures visual context, while a nearby consumer-grade device performs local MLLM inference and local speech output, reducing cloud reliance and keeping raw egocentric visual data on user-controlled devices by default. We evaluate response quality, query-ready-to-audio latency, safety-aware abstention, and auditable logs. Under real ESP32 Wi-Fi capture, OpenGlass reaches 993 ms median user-to-audio latency with resized payloads and 1625 ms with raw 1280 x 720 payloads; 97.5% and 93.3% of trials fall below 2 s, respectively. OpenGlass is a user-initiated visual-assistance reference platform for obstacle/hazard awareness, sign/object queries, and image-quality self-checking, rather than a certified navigation aid. We release source code, hardware instructions, prompts, evaluation data, and logs.


### EMNLP 2025: Spoken Conversational Agents with Large Language Models (基于大语言模型的语音会话智能体)

- **arXiv**: [2512.02593](https://arxiv.org/abs/2512.02593) · **Venue**: EMNLP 2025 · **Published**: 2025-12-02
- **Title (English)**: Spoken Conversational Agents with Large Language Models
- **Title (Chinese)**: 基于大语言模型的语音会话智能体
- **Authors**: Chao-Han Huck Yang, Andreas Stolcke, Larry Heck
- **Affiliation**: NVIDIA Research1 Uniphore2 Georgia Institute of Technology2; hucky@nvidia.com andreas.stolcke@uniphore.com larryheck@gatech.edu

**Problem background**: 口语自然语言处理是级联 ASR/NLU 到 E2E、检索式的未来；改编既有语音 LLM 很难泛化。

**Methodology & innovations**:
统一报告：两条架构路径的全面调研、成本权衡与训练规模建议。

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Spoken conversational agents are converging toward voice-native LLMs. This tutorial distills the path from cascaded ASR/NLU to end-to-end, retrieval-and vision-grounded systems. We frame adaptation of text LLMs to audio, cross-modal alignment, and joint speech-text training; review datasets, metrics, and robustness across accents and compare design choices (cascaded vs. E2E, post-ASR correction, streaming). We link industrial assistants to current open-domain and task-oriented agents, highlight reproducible baselines, and outline open problems in privacy, safety, and evaluation. Attendees leave with practical recipes and a clear systems-level roadmap.


### EMNLP 2025: ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment (ICG：基于 MLLM 提示的封面图生成与个性化偏好对齐)

- **arXiv**: [2605.27374](https://arxiv.org/abs/2605.27374) · **Venue**: EMNLP 2025 · **Published**: 2026-04-08
- **Title (English)**: ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment
- **Title (Chinese)**: ICG：基于 MLLM 提示的封面图生成与个性化偏好对齐
- **Authors**: Zhipeng Bian, Jieming Zhu, Qijiong Liu, Wang Lin, Guohao Cai, Zhaocheng Du, Jiacheng Sun, Zhou Zhao, Zhenhua Dong
- **Affiliation**: 1Huazhong University of Science and Technology 2Huawei Noah’s Ark Lab; 3Hong Kong Polytechnic University 4Zhejiang University; reference images via meta tokens, refines them

**Problem background**: 封面图在用户参与中的功能巨大；错过生成式人工内容检测器，但个性化生成不稳定。

**Methodology & innovations**:
MLLM 语义特征提取：meta token 驱动；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Recent advances in multimodal large language models (MLLMs) and diffusion models (DMs) have opened new possibilities for AI-generated content. Yet, personalized cover image generation remains underexplored, despite its critical role in boosting user engagement on digital platforms. We propose ICG, a novel framework that integrates MLLM-based prompting with personalized preference alignment to generate high-quality, contextually relevant covers. ICG extracts semantic features from item titles and reference images via meta tokens, refines them with user embeddings, and injects the resulting personalized context into the diffusion model. To address the lack of labeled supervision, we adopt a multi-reward learning strategy that combines public aesthetic and relevance rewards with a personalized preference model trained from user behavior. Unlike prior pipelines relying on handcrafted prompts and disjointed modules, ICG employs an adapter to bridge MLLMs and diffusion models for end-to-end training. Experiments demonstrate that ICG significantly improves image quality, semantic fidelity, and personalization, leading to stronger user appeal and offline recommendation accuracy in downstream tasks. As a plug-and-play adapter bridging MLLMs and diffusion models, ICG is compatible with common checkpoints and requires no ground-truth labels during optimization.


### SIGIR 2026: Evaluating Visual Language Models on Visual Grounding for Visually Impaired People (评估视觉语言模型在视觉基础上的感知能力（VizWiz）)

- **arXiv**: [2610.33078](https://arxiv.org/abs/2610.33078) · **Venue**: SIGIR 2026 · **Published**: 2026-10-21
- **Title (English)**: Evaluating Visual Language Models on Visual Grounding for Visually Impaired People
- **Title (Chinese)**: 评估视觉语言模型在视觉基础上的感知能力（VizWiz）
- **Authors**: Fairooz Azim, Lydia Achour, Claudia Borg, Lina Rojas-Barahona
- **Affiliation**: University of Malta, Msida, Malta; University of Malta

**Problem background**: VLM 通用能力强，但视觉基础（VG）是盲人视觉问答（VQA）的关键能力，需真实设施与公平性验证。

**Methodology & innovations**:
样本内一致性指标：解释能力（一致性掩码提示的超类别和隐形接口）；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Visual grounding (VG) in visual question answering (VQA) is a fundamental capability of Vision-Language Models (VLMs), enabling the detection of the most relevant region in an image to answer the question. This reflects the model's capability of multimodal comprehension, which is crucial when interacting with visually impaired people (VIP). Indeed, visual grounding, when applied to assistive scenarios, is not merely a technical feature, but rather a trust and safety requirement. In this work, we study visual grounding in VLMs for visually impaired people. To this end, we assess open-source VLMs on visual grounding using the VizWiz-VQA-Grounding dataset and challenge, which contains real-life images taken by VIP. We propose VG-SHAP, which extends an existing explainability framework to provide visual grounding explanations, allowing the evaluation of black-box VLMs. Our results on the VizWiz-VQA-Grounding challenge show that despite generating correct answers, VLMs struggle to ground in the proper region in the image. However, these results are constrained by the quality of the segmentation model of our explainability framework and further research is necessary.


### SIGIR 2026: Representation Affects Retrieval: A Case Study of Skill Discovery and Routing in a Multimodal Agent Harness (认识转矩身份：Multimodal Agent Harness 中的 Skill 发现与路由)

- **arXiv**: [2608.20389](https://arxiv.org/abs/2608.20389) · **Venue**: SIGIR 2026 · **Published**: 2026-06-30
- **Title (English)**: Representation Affects Retrieval: A Case Study of Skill Discovery and Routing in a Multimodal Agent Harness
- **Title (Chinese)**: 认识转矩身份：Multimodal Agent Harness 中的 Skill 发现与路由
- **Authors**: Kevin Dela Rosa
- **Affiliation**: Not listed on arXiv page

**Problem background**: Agent Harness 中 skill 库增长，对 LLM Planner 的表示方式决定哪些 Skill 能被选择；小 N 方法需推翻现有产品化意见。

**Methodology & innovations**:
策略 = 特定 Workflow 的检索结果；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: A production agent harness must discover and rank, from a growing library of skills, the one most appropriate for a user's task. At small scale this selection happens in context: the LLM planner chooses among skill representations exposed in its system prompt, without an explicit embedding-based retrieval step. We treat this in-context selection as the small-N counterpart to embedding-based skill retrieval at scale, and present a case study of how Tinycloud, a production multimodal video agent harness, represents its skills for the planner. The harness ships skills under two recurring representations: tool-skills that wrap a single external API or system tool and serve as primitive vocabulary, and workflow-skills that orchestrate tool-skill calls plus a template render to produce one named deliverable. The harness exposes them via two surfaces in the system prompt: an inlined-body surface (full instructions, scripts, templates) for autoloaded skills, and a one-line listing for on-demand skills. A six-task selection ablation across three exposure regimes (all-on, default, all-off) shows that full autoload selects the gold skill on every task; all-off slows execution and produces hard discovery failures; and the production default misroutes one task because its lexical signal collides with an autoloaded tool-skill that pulls planner attention away from a listed workflow-skill. The headline finding is that in-prompt exposure of skills is not monotonically helpful: partial exposure can create lexical competition that suppresses correct selection. We connect this small-N observation to recent retrieval-based skill-routing work at large scale, and frame this contribution as a case study rather than a benchmark.


### SIGIR 2026: Personalized Deep Research: A User-Centric Framework, Dataset, and Hybrid Evaluation for Knowledge Discovery (个性化深度研究：用户中心框架、数据集与混合评估)

- **arXiv**: [2605.10530](https://arxiv.org/abs/2605.10530) · **Venue**: SIGIR 2026 · **Published**: 2026-05-11
- **Title (English)**: Personalized Deep Research: A User-Centric Framework, Dataset, and Hybrid Evaluation for Knowledge Discovery
- **Title (Chinese)**: 个性化深度研究：用户中心框架、数据集与混合评估
- **Authors**: Xiaopeng Li, Wenlin Zhang, Yingyi Zhang, Pengyue Jia, Yejing Wang, Yichao Wang, Yong Liu, Huifeng Guo, Xiangyu Zhao
- **Affiliation**: City University of Hong Kong; Hong Kong, China; Singapore, Singapore

**Problem background**: Deep Research 缺乏个性化检索，通用策略使冗余/密集报告，影响用户目标。

**Methodology & innovations**:
把用户目标融入检索与推理闭环；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Deep Research agents driven by LLMs have automated the scholarly discovery pipeline, from planning and query formulation to iterative web exploration. Yet they remain constrained by a static, ``one-size-fits-all'' retrieval paradigm. Current systems fail to adaptively adjust the depth and breadth of exploration based on the user's existing expertise or latent interests, frequently resulting in reports that are either redundant for experts or overly dense for novices. To address this, we introduce Personalized Deep Research (PDR), a framework that integrates dynamic user context into the core retrieval-reasoning loop. Rather than treating personalization as a post-hoc formatting step, PDR unifies user profile modeling with iterative query development, dual-stage (private/public) retrieval, and context-aware synthesis. This allows the system to autonomously align research sub-goals with user intent and optimize the stopping criteria for evidence collection. To facilitate benchmarking, we release the PDR Dataset, covering four realistic user tasks, and propose a hybrid evaluation framework combining lexical metrics with LLM-based judgments to assess factual accuracy and personalization alignment. Experimental results against commercial baselines demonstrate that PDR significantly improves retrieval utility and report relevance, effectively bridging the gap between generic information retrieval and personalized knowledge acquisition. The resource is available to the public at this https URL .


### WWW 2026: EcoThink: A Green Adaptive Inference Framework for Sustainable and Accessible Agents (EcoThink：可持续与公平的 LLM 自适应推理)

- **arXiv**: [2603.25498](https://arxiv.org/abs/2603.25498) · **Venue**: WWW 2026 · **Published**: 2026-03-26
- **Title (English)**: EcoThink: A Green Adaptive Inference Framework for Sustainable and Accessible Agents
- **Title (Chinese)**: EcoThink：可持续与公平的 LLM 自适应推理
- **Authors**: Linxiao Li, Zhixiang Lu
- **Affiliation**: The University of Sydney; University of Liverpool

**Problem background**: 全球数十亿查询/日导致 LLM 过度思考（CoT），能耗高且不可及；负责任的改进是要平衡效率与质量。

**Methodology & innovations**:
双层设计：轻量迁移知识 + 分辨验证，服务通过上下文配置自适应深度/广度；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: As the Web transitions from static retrieval to generative interaction, the escalating environmental footprint of Large Language Models (LLMs) presents a critical sustainability challenge. Current paradigms indiscriminately apply computation-intensive strategies like Chain-of-Thought (CoT) to billions of daily queries, causing LLM overthinking, a redundancy that amplifies carbon emissions and operational barriers. This inefficiency directly undermines UN Sustainable Development Goals 13 (Climate Action) and 10 (Reduced Inequalities) by hindering equitable AI access in resource-constrained regions. To address this, we introduce EcoThink, an energy-aware adaptive inference framework designed to reconcile high-performance AI intelligence with environmental responsibility. EcoThink employs a lightweight, distillation-based router to dynamically assess query complexity, skipping unnecessary reasoning for factoid retrieval while reserving deep computation for complex logic. Extensive evaluations across 9 diverse benchmarks demonstrate that EcoThink reduces inference energy by 40.4% on average (up to 81.9% for web knowledge retrieval) without statistically significant performance loss. By mitigating algorithmic waste, EcoThink offers a scalable path toward a sustainable, inclusive, and energy-efficient generative AI Agent.


### WWW 2026: Belief-Driven Multi-Agent Collaboration via Approximate Perfect Bayesian Equilibrium for Social Simulation (通过近似完美贝叶斯纳什均衡的信仰驱动多智能体协作用于社会模拟)

- **arXiv**: [2603.24973](https://arxiv.org/abs/2603.24973) · **Venue**: WWW 2026 · **Published**: 2026-03-26
- **Title (English)**: Belief-Driven Multi-Agent Collaboration via Approximate Perfect Bayesian Equilibrium for Social Simulation
- **Title (Chinese)**: 通过近似完美贝叶斯纳什均衡的信仰驱动多智能体协作用于社会模拟
- **Authors**: Weiwei Fang, Lin Li, Kaize Shi, Yu Yang, Jianwei Zhang
- **Affiliation**: Wuhan University of Technology; University of Southern Queensland; The Education University of Hong; Hong Kong, China; Iwate University

**Problem background**: 社会模拟缺乏人类行为的对应物；单纯统计无法解释信任、凝聚力与个体机制；PBE 引入非模型与结构不确定性。

**Methodology & innovations**:
信任设计：简单诚实过家宽；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: High-fidelity social simulation is pivotal for addressing complex Web societal challenges, yet it demands agents capable of authentically replicating the dynamic spectrum of human interaction. Current LLM-based multi-agent frameworks, however, predominantly adhere to static interaction topologies, failing to capture the fluid oscillation between cooperative knowledge synthesis and competitive critical reasoning seen in real-world scenarios. This rigidity often leads to unrealistic ``groupthink'' or unproductive deadlocks, undermining the credibility of simulations for decision support. To bridge this gap, we propose \textit{BEACOF, a \textit{belief-driven adaptive collaboration framework inspired by Perfect Bayesian Equilibrium (PBE). By modeling social interaction as a dynamic game of incomplete information, BEACOF rigorously addresses the circular dependency between collaboration type selection and capability estimation. Agents iteratively refine probabilistic beliefs about peer capabilities and autonomously modulate their collaboration strategy, thereby ensuring sequentially rational decisions under uncertainty. Validated across adversarial (judicial), open-ended (social) and mixed (medical) scenarios, BEACOF prevents coordination failures and fosters robust convergence toward high-quality solutions, demonstrating superior potential for reliable social simulation. Source codes and datasets are publicly released at: this https URL .


### WWW 2026: Egocentric Co-Pilot: Web-Native Smart-Glasses Agents for Assistive Egocentric AI (Egocentric Co-Pilot：智能眼镜在支持任务中的无框架对象、意图与情绪感知)

- **arXiv**: [2603.01104](https://arxiv.org/abs/2603.01104) · **Venue**: WWW 2026 · **Published**: 2026-03-01
- **Title (English)**: Egocentric Co-Pilot: Web-Native Smart-Glasses Agents for Assistive Egocentric AI
- **Title (Chinese)**: Egocentric Co-Pilot：智能眼镜在支持任务中的无框架对象、意图与情绪感知
- **Authors**: Sicheng Yang, Yukai Huang, Weitong Cai, Shitong Sun, Fengyi Fang, You He, Yiqiao Xie, Jiankang Deng, Hang Zhang, Jifei Song, Zhensong Zhang
- **Affiliation**: Shenzhen International Graduate School; Tsinghua University; yangsc25@mails.tsinghua.edu.cn; Independent Researcher; Queen Mary University of London; fangfy22@tsinghua.org.cn

**Problem background**: 智能眼镜与眼球助手在面向无障碍者的助手上有差距，本地模型难以直接把领域特定感知编码进通用模型。

**Methodology & innovations**:
以视频为中心的 X把训练流程与最优实验带报告规模到 12T / OpenHands WebJREAM（1.3B → LLM）；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: What if accessing the web did not require a screen, a stable desk, or even free hands? For people navigating crowded cities, living with low vision, or experiencing cognitive overload, smart glasses coupled with AI agents could turn the web into an always-on assistive layer over daily life. We present Egocentric Co-Pilot, a web-native neuro-symbolic framework that runs on smart glasses and uses a Large Language Model (LLM) to orchestrate a toolbox of perception, reasoning, and web tools. An egocentric reasoning core combines Temporal Chain-of-Thought with Hierarchical Context Compression to support long-horizon question answering and decision support over continuous first-person video, far beyond a single model's context window. Additionally, a lightweight multimodal intent layer maps noisy speech and gaze into structured commands. We further implement and evaluate a cloud-native WebRTC pipeline integrating streaming speech, video, and control messages into a unified channel for smart glasses and browsers. In parallel, we deploy an on-premise WebSocket baseline, exposing concrete trade-offs between local inference and cloud offloading in terms of latency, mobility, and resource use. Experiments on Egolife and HD-EPIC demonstrate competitive or state-of-the-art egocentric QA performance, and a human-in-the-loop study on smart glasses shows higher task completion and user satisfaction than leading commercial baselines. Taken together, these results indicate that web-connected egocentric co-pilots can be a practical path toward more accessible, context-aware assistance in everyday life. By grounding operation in web-native communication primitives and modular, auditable tool use, Egocentric Co-Pilot offers a concrete blueprint for assistive, always-on web agents that support education, accessibility, and social inclusion for people who may benefit most from contextual, egocentric AI.


### CIKM 2025: V-Agent: An Interactive Video Search System Using Vision-Language Models (V-Agent：一款交互式视频检索系统使用 Vision-Language 模型)

- **arXiv**: [2512.16925](https://arxiv.org/abs/2512.16925) · **Venue**: CIKM 2025 · **Published**: 2025-11-04
- **Title (English)**: V-Agent: An Interactive Video Search System Using Vision-Language Models
- **Title (Chinese)**: V-Agent：一款交互式视频检索系统使用 Vision-Language 模型
- **Authors**: SunYoung Park, Jong-Hyeon Lee, Youngjune Kim, Daegyu Sung, Younghyun Yu, Young-rok Cha, Jeongho Ju
- **Affiliation**: Korea Advanced Institute

**Problem background**: 视频搜索的门槛（关键帧 + 关键词）低，文本查询和 VLM 检索的结合有显著改善。

**Methodology & innovations**:
实时语义搜索（动态查询分解）、展示用户浏览行为、预测下一个相关子查询。

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: We introduce V-Agent, a novel multi-agent platform designed for advanced video search and interactive user-system conversations. By fine-tuning a vision-language model (VLM) with a small video preference dataset and enhancing it with a retrieval vector from an image-text retrieval model, we overcome the limitations of traditional text-based retrieval systems in multimodal scenarios. The VLM-based retrieval model independently embeds video frames and audio transcriptions from an automatic speech recognition (ASR) module into a shared multimodal representation space, enabling V-Agent to interpret both visual and spoken content for context-aware video search. This system consists of three agents-a routing agent, a search agent, and a chat agent-that work collaboratively to address user intents by refining search outputs and communicating with users. The search agent utilizes the VLM-based retrieval model together with an additional re-ranking module to further enhance video retrieval quality. Our proposed framework demonstrates state-of-the-art zero-shot performance on the MultiVENT 2.0 benchmark, highlighting its potential for both academic research and real-world applications. The retrieval model and demo videos are available at this https URL .


### CIKM 2025: GReF: A Unified Generative Framework for Efficient Reranking via Ordered Multi-token Prediction (GReF：基于 Lambda Weighting 的连续 N-token 预测的生成式重排)

- **arXiv**: [2510.25220](https://arxiv.org/abs/2510.25220) · **Venue**: CIKM 2025 · **Published**: 2025-10-29
- **Title (English)**: GReF: A Unified Generative Framework for Efficient Reranking via Ordered Multi-token Prediction
- **Title (Chinese)**: GReF：基于 Lambda Weighting 的连续 N-token 预测的生成式重排
- **Authors**: Zhijie Lin, Zhuofeng Li, Chenglei Dai, Wentian Bao, Shuai Lin, Enyun Yu, Haoxiang Zhang, Liang Zhao
- **Affiliation**: Kuaishou Technology; linzhijie@kuaishou.com; Shanghai University; Shanghai, China; daichenglei@kuaishou.com

**Problem background**: 基于点的重排受限于 NDCG 在度量无相关的困难案例；生成式重排与多样性、零缺失物品等问题。

**Methodology & innovations**:
把 NDCG 优化纳入 Lambda 权重，使 Listw 优化转换为对点排序的列表分数梯度损失；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: In a multi-stage recommendation system, reranking plays a crucial role in modeling intra-list correlations among items. A key challenge lies in exploring optimal sequences within the combinatorial space of permutations. Recent research follows a two-stage (generator-evaluator) paradigm, where a generator produces multiple feasible sequences, and an evaluator selects the best one. In practice, the generator is typically implemented as an autoregressive model. However, these two-stage methods face two main challenges. First, the separation of the generator and evaluator hinders end-to-end training. Second, autoregressive generators suffer from inference efficiency. In this work, we propose a Unified Generative Efficient Reranking Framework (GReF) to address the two primary challenges. Specifically, we introduce Gen-Reranker, an autoregressive generator featuring a bidirectional encoder and a dynamic autoregressive decoder to generate causal reranking sequences. Subsequently, we pre-train Gen-Reranker on the item exposure order for high-quality parameter initialization. To eliminate the need for the evaluator while integrating sequence-level evaluation during training for end-to-end optimization, we propose post-training the model through Rerank-DPO. Moreover, for efficient autoregressive inference, we introduce ordered multi-token prediction (OMTP), which trains Gen-Reranker to simultaneously generate multiple future items while preserving their order, ensuring practical deployment in real-time recommender systems. Extensive offline experiments demonstrate that GReF outperforms state-of-the-art reranking methods while achieving latency that is nearly comparable to non-autoregressive models. Additionally, GReF has also been deployed in a real-world video app Kuaishou with over 300 million daily active users, significantly improving online recommendation quality.


### RecSys 2025: Data Quality Challenges in Multimodal Tourism Recommender Systems (多模态旅游推荐中的数据质量挑战)

- **arXiv**: [2611.13972](https://arxiv.org/abs/2611.13972) · **Venue**: RecSys 2025 · **Published**: 2026-11-10
- **Title (English)**: Data Quality Challenges in Multimodal Tourism Recommender Systems
- **Title (Chinese)**: 多模态旅游推荐中的数据质量挑战
- **Authors**: Zehui Wang, Wolfram Höpken, Dietmar Jannach
- **Affiliation**: 1University of Applied Sciences Ravensburg-Weingarten, Doggenriedstrasse, Weingarten, Weingarten, 88250, Germany; 2University of Klagenfurt, Universitätsstraße 65–67, Klagenfurt am Wörthersee, 9020, Austria; structured and controlled LLM-based content generation to reduce hallucinations, and user group differentiation; 2, 3]. Recently, researchers have increasingly explored the use of diverse information types to improve

**Problem background**: 多模态旅游推荐（图像+文本+元数据）在旅游系统的部署中，经常面临推荐质量问题，而这些问题源于数据预处理而非模型本身。

**Methodology & innovations**:
把数据质量（视觉-现实描述偏差）与模型推荐结合；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Modern recommender systems increasingly consider diverse data modalities to enhance model performance. However, the quality of the underlying multimodal data (e.g. data from social media platforms) has received limited attention so far. Focusing on tourism recommendation, we examine real-world challenges encountered when using datasets from Yelp and Instagram. Issues include noise from fake reviews, hallucinated content from LLMs, modality contradictions, and demographic bias. We outline future directions such as quality-aware fusion, structured and controlled LLM-based content generation to reduce hallucinations, and user group differentiation to improve the robustness and reliability of multimodal recommendation systems.


### RecSys 2025: Improving Visual Recommendation on E-commerce Platforms Using Vision-Language Models (用视觉语言模型提升 E 商务平台上的视觉推荐)

- **arXiv**: [2510.13359](https://arxiv.org/abs/2510.13359) · **Venue**: RecSys 2025 · **Published**: 2025-10-15
- **Title (English)**: Improving Visual Recommendation on E-commerce Platforms Using Vision-Language Models
- **Title (Chinese)**: 用视觉语言模型提升 E 商务平台上的视觉推荐
- **Authors**: Yuki Yada, Sho Akiyama, Ryo Watanabe, Yuta Ueno, Yusuke Shido, Andre Rusli
- **Affiliation**: have become essential. Platforms such as Pinterest [15], Amazon

**Problem background**: 电商平台以视觉为首的特征，但通用模型难以访问用户交互；需要在电商视觉中应用域特定视觉嵌入。

**Methodology & innovations**:


**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: On large-scale e-commerce platforms with tens of millions of active monthly users, recommending visually similar products is essential for enabling users to efficiently discover items that align with their preferences. This study presents the application of a vision-language model (VLM) -- which has demonstrated strong performance in image recognition and image-text retrieval tasks -- to product recommendations on Mercari, a major consumer-to-consumer marketplace used by more than 20 million monthly users in Japan. Specifically, we fine-tuned SigLIP, a VLM employing a sigmoid-based contrastive loss, using one million product image-title pairs from Mercari collected over a three-month period, and developed an image encoder for generating item embeddings used in the recommendation system. Our evaluation comprised an offline analysis of historical interaction logs and an online A/B test in a production environment. In offline analysis, the model achieved a 9.1% improvement in nDCG@5 compared with the baseline. In the online A/B test, the click-through rate improved by 50% whereas the conversion rate improved by 14% compared with the existing model. These results demonstrate the effectiveness of VLM-based encoders for e-commerce product recommendations and provide practical insights into the development of visual similarity-based recommendation systems.


### RecSys 2025: LLM-Powered Nuanced Video Attribute Annotation for Enhanced Recommendations (用 LLM 驱动精细的视频属性标注以增强推荐)

- **arXiv**: [2510.06657](https://arxiv.org/abs/2510.06657) · **Venue**: RecSys 2025 · **Published**: 2025-10-08
- **Title (English)**: LLM-Powered Nuanced Video Attribute Annotation for Enhanced Recommendations
- **Title (Chinese)**: 用 LLM 驱动精细的视频属性标注以增强推荐
- **Authors**: Boyuan Long, Yueqi Wang, Hiloni Mehta, Mick Zomnir, Omkar Pathak, Changping Meng, Ruolin Jia, Yajun Peng, Dapeng Hong, Xia Wu, Mingyan Gao, Onkar Dalal, Ningren Han
- **Affiliation**: Google; yueqiw@google.com; hiloni@google.com; mzomnir@google.com; omkarpathak@google.com; changping@google.com

**Problem background**: 细粒度视频属性对 Google 的视频推荐至关重要，但手工标注代价高，模型能力不足。

**Methodology & innovations**:
层级时长/占有性：通过 LLM 知识蒸馏注入强可解释性与时长占有性特征；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: This paper presents a case study on deploying Large Language Models (LLMs) as an advanced "annotation" mechanism to achieve nuanced content understanding (e.g., discerning content "vibe") at scale within a large-scale industrial short-form video recommendation system. Traditional machine learning classifiers for content understanding face protracted development cycles and a lack of deep, nuanced comprehension. The "LLM-as-annotators" approach addresses these by significantly shortening development times and enabling the annotation of subtle attributes. This work details an end-to-end workflow encompassing: (1) iterative definition and robust evaluation of target attributes, refined by offline metrics and online A/B testing; (2) scalable offline bulk annotation of video corpora using LLMs with multimodal features, optimized inference, and knowledge distillation for broad application; and (3) integration of these rich annotations into the online recommendation serving system, for example, through personalized restrict retrieval. Experimental results demonstrate the efficacy of this approach, with LLMs outperforming human raters in offline annotation quality for nuanced attributes and yielding significant improvements of user participation and satisfied consumption in online A/B tests. The study provides insights into designing and scaling production-level LLM pipelines for rich content evaluation, highlighting the adaptability and benefits of LLM-generated nuanced understanding for enhancing content discovery, user satisfaction, and the overall effectiveness of modern recommendation systems.


### Advertising / CTR: DNA: Unlocking Depth Scaling in CTR Models (DNA：通过动态 Attention 突破 CTR 模型深度缩放的瓶颈)

- **arXiv**: [2611.25659](https://arxiv.org/abs/2611.25659) · **Venue**: Advertising / CTR · **Published**: 
- **Title (English)**: DNA: Unlocking Depth Scaling in CTR Models
- **Title (Chinese)**: DNA：通过动态 Attention 突破 CTR 模型深度缩放的瓶颈
- **Authors**: Caiyuan Li, Wenjie Wu, Yuheng Huang, Xiao Zhou, Silu Zhou, Ke Chen, Zinan Zhao, Xinrui Zeng, Hanmo Xu, Chaoqun Song, Hua Zong, Zongyuan Wu, Hongbin Zhou, Huimin Yi, Zhixuan Zhang, Dan Ou, Haihong Tang
- **Affiliation**: Alibaba Group; licaiyuan.lcy@alibaba-inc.com; wuwenjie.wwj@alibaba-inc.com; hexing.hyh@alibaba-inc.com; silu.zsl@alibaba-inc.com; ck325090@alibaba-inc.com

**Problem background**: 深度是 CTR 模型的主要瓶颈；深度大于 28 层时性能几乎不再提升；需要密钥侧的解决方案。

**Methodology & innovations**:
DNA（Dual-stream Nexus Attention）：32 位浮点模型 12.7% AUC 增益（Chi2 p<0.001），使用稀疏稀疏窗口选择性重用，相比全注意力层堆叠 22% FLOPs；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Long user behavior sequences are among the strongest signals for click-through rate (CTR) prediction. Cross-attention makes these sequences practical for industrial ranking by keeping compute linear in sequence length. Yet the gains from stacking cross-attention layers taper off: on Taobao search, growing a cross-attention stack from 16 to 28 layers adds only 0.02 percentage points (pt) of AUC. We argue that the key-value side is the bottleneck. Each layer projects the same behavior sequence into keys and values, so adding depth gives the model more reads of a fixed sequence. We propose DNA (Dual-stream Nexus Attention), which lets the sequence itself evolve with depth. At each layer, the request representation (the search query, user features and scene) first reads the sequence. Each behavior token then attends to the updated request representation and uses what it reads to update itself, so the next layer reads a sequence shaped by the current request. The update runs once per request, all candidates share the resulting sequence, and both the reads and the update keep linear complexity in sequence length. At comparable forward FLOPs, DNA improves AUC over cross-attention stacks by 0.08 to 0.26 pt and keeps improving in the depth range where those stacks level off. DNA-4 is deployed in Taobao search. In an online A/B test against the production model, it improves CTR by 0.8% and GMV by 0.5%.


### Advertising / CTR: X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction (X-split Argus：可复用历史令牌用于高效 CTR 预测)

- **arXiv**: [2611.24283](https://arxiv.org/abs/2611.24283) · **Venue**: Advertising / CTR · **Published**: 
- **Title (English)**: X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction
- **Title (Chinese)**: X-split Argus：可复用历史令牌用于高效 CTR 预测
- **Authors**: Alexander Ploshkin, Nikita Stepanov, Alexey Pismenny, Viacheslav Ovchinnikov, Nikolay Savushkin
- **Affiliation**: Not listed on arXiv page

**Problem background**: 用户行为序列可达数千，CTR 预测需在线请求限速的限制内处理提取。

**Methodology & innovations**:
离线抽象 + 在线 ranker；跨候选复用缓存令牌；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Accurate click-through rate (CTR) prediction depends on user representations that capture both persistent preferences and recent intent, yet processing extensive behavioral histories for every ranking request is costly under production compute and latency constraints. We present X-split ARGUS, a framework for ad ranking whose history compressor and online ranker are trained end to end. The compressor encodes past interactions into a compact set of tokens that are computed offline and reused across candidates, while the online ranker scores ads through cross-attention to these tokens and representations of recent events. Training combines an autoregressive loss for click feedback with distillation of candidate-specific click logits from a larger teacher that scores each candidate using the uncompressed history. The number of compressed history tokens and the length of recent history can be adjusted to fit serving compute and latency budgets. Offline evaluation shows a 0.81% relative reduction in normalized entropy (NE) compared with the production baseline. Deployment in a large-scale real-time bidding system increases online inference cost by 15% relative to the production baseline. An online A/B test against this baseline yields relative gains of 4.65% in a business metric reflecting the monetary value of conversions generated for advertisers and 2.96% in clicks.


### Advertising / CTR: Iterative Scarcity-Guided Exploration: Bootstrapping Generative Auto-bidding from Narrow Support (迭代稀缺性引导探索：从窄支撑自举生成式自动竞价)

- **arXiv**: [2611.26060](https://arxiv.org/abs/2611.26060) · **Venue**: Advertising / CTR · **Published**: 
- **Title (English)**: Iterative Scarcity-Guided Exploration: Bootstrapping Generative Auto-bidding from Narrow Support
- **Title (Chinese)**: 迭代稀缺性引导探索：从窄支撑自举生成式自动竞价
- **Authors**: Qingmao Yao, Guangzheng Hu, Yusen Huo, Zhilin Zhang, Chuan Yu, Jian Xu, Xu Chu, Bo Zheng, Xiaotie Deng
- **Affiliation**: 1Center on Frontiers of Computing Studies, School of Computer Science, Peking University; 2Alimama Tech, Taobao & Tmall Group of Alibaba; 3Department of Computer Science, City University of Hong Kong; 4Independent Researcher; bozheng@alibaba-inc.com,{chu_xu,xiaotie}@pku.edu.cn

**Problem background**: 自动竞价中 AIGB 依赖历史数据，窄支撑在冷启动时声称退化问题；Auction 信号/噪声尺度导致期望收益退化；SNR 内化方法失败。

**Methodology & innovations**:
基于 SNR 的连续阻尼坐标下降 + 迭代重构，稀疏度与两级参考池自适应；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Auto-bidding is a core algorithmic component in online advertising auctions. In practical cold-start settings, iterative training is commonly used to compensate for low-quality, narrowly supported historical data. Unfortunately, in iterative training, representative diffusion-based AI-Generated Bidding (AIGB) methods fail to sustain extrapolation beyond the narrow data support and stagnate at a suboptimal level. In this paper, we theoretically attribute this stagnation to Signal-to-Noise Ratio (SNR) collapse: the weak radial return signal is overwhelmed by a curvature-induced penalty. To break this stagnation, we propose \textbf{Iterative Scarcity-Guided Exploration (ISGE), which introduces a guidance handoff: as the return signal collapses, scarcity subsequently takes over as an exploratory signal to elevate the SNR above a critical threshold. Specifically, ISGE iteratively alternates between a \emph{Judger that assigns scarcity scores to trajectories and an \emph{Explorer that performs guided generation of high-scarcity and high-return trajectories, thereby bootstrapping from the narrow support with such self-generated trajectories. Extensive experiments on the industrial AuctionNet benchmark demonstrate that ISGE, starting from cold-start datasets, effectively surpasses the performance of the Full-Dataset baseline within three iterations. Code is available at this https URL


### Games: NitroGen: Observations on the Action Dynamics, Visual Instruction Following, and Spatial Exploration (NitroGen：Hollow Knight 中游戏控制的观察报告)

- **arXiv**: [2611.26807](https://arxiv.org/abs/2611.26807) · **Venue**: Games · **Published**: 
- **Title (English)**: NitroGen: Observations on the Action Dynamics, Visual Instruction Following, and Spatial Exploration
- **Title (Chinese)**: NitroGen：Hollow Knight 中游戏控制的观察报告
- **Authors**: Shengyuan Lin, Zhiling Li, Haoyu Nie, Ozan K. Tonguz
- **Affiliation**: Shengyuan Linshengyu3@andrew.cmu.edu; Carnegie Mellon University; Zhiling Li zhilingl@andrew.cmu.edu; Haoyu Nie hnie@andrew.cmu.edu; Ozan K. T onguztonguz@andrew.cmu.edu

**Problem background**: 在游戏中 AI 我们检查行动适应性、视觉指令跟随与空间探索。

**Methodology & innovations**:
拒绝行动匹配的高准确率 —— 这是一个超越共性的危险信号；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: NitroGen is an open vision-action foundation model for game control. It is trained by behavior cloning on online gameplay videos. In this paper, we study the frozen controller in Hollow Knight and Trackmania as examples along three dimensions: action adaptation, visual instruction following, and spatial exploration. Our results indicate that NitroGen can adapt its actions to local context, but it lacks the planning, recovery, and exploration needed for longer-horizon game control.


### Games: PlayCraft: Designing Engaging Games from Agent Play Experience (PlayCraft：基于智能体对弈体验设计引人注目的游戏)

- **arXiv**: [2611.26624](https://arxiv.org/abs/2611.26624) · **Venue**: Games · **Published**: 
- **Title (English)**: PlayCraft: Designing Engaging Games from Agent Play Experience
- **Title (Chinese)**: PlayCraft：基于智能体对弈体验设计引人注目的游戏
- **Authors**: Weihao Cheng
- **Affiliation**: Recent agents based on foundation models, such as GPT-6 Astra (OpenAI, 2026b), can play 2D and

**Problem background**: 设计门槛高；智能体游玩并生成路径；需要对游戏持续的改进。

**Methodology & innovations**:
将循环向前调优：对局中的代理观察 + 超越，调整全局对象收益；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Recent AI agents can generate playable games, but these games are not necessarily engaging. Mastery is a key source of engagement, yet designing for it requires extensive human play and tuning. We propose PlayCraft, an automated framework that uses a vision-based agent to play games and draws on its detailed play experience to revise them for mastery. Starting from an initial game, PlayCraft alternates between playing and crafting. In the playing stage, a player agent watches the game screen, uses the controls, and pursues the game objective over repeated episodes while retaining memory. After each episode, it reports its progress, outcomes, decisions, and reflections. In the crafting stage, a crafter agent uses these reports to revise the game. It estimates player abilities, predicts performance at different proficiency levels, and compares those predictions with a target learning progression. It diagnoses the game and addresses the gaps by giving players meaningful opportunities to improve through better decisions and execution. We evaluate games in fresh runs with player agents across three intelligence settings, measuring learning gain and learning slope. Compared with the initial games, PlayCraft yields larger learning gains and steeper learning slopes in most games. It also outperforms the baselines on the macro-average of each metric at every intelligence setting.


### Agent Systems: HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents (HarnessFlow：基于 MCTS 导向的 LLM Agent 技能优化)

- **arXiv**: [2611.06254](https://arxiv.org/abs/2611.06254) · **Venue**: Agent Systems · **Published**: 2026-11-04
- **Title (English)**: HarnessFlow: MCTS-Guided Harness Optimization for LLM Agents
- **Title (Chinese)**: HarnessFlow：基于 MCTS 导向的 LLM Agent 技能优化
- **Authors**: Zhi Hong, Qianlong Wang, Hongchen Wei, Aidan Wu, Daohong Ying, Mingze Kong, Bei Liu, Chong Luo
- **Affiliation**: 1South China University of Technology 2Fudan University; 3Wuhan University 4Cornell University 5University of California, San Diego; 6The Chinese University of Hong Kong, Shenzhen 7Microsoft Research Asia; and Meta-Harness by10.89and3.95percentage points, respectively, while incur-

**Problem background**: Agent 的模型和任务相同，只有组件不同，手工设计的 harness 最优利率不一致。

**Methodology & innovations**:
共享骨干的增长骨架；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: The performance of large language model (LLM) agents depends on both the underlying model and the harness that governs interaction with tools and the environment. Yet harness design remains largely manual, and automating it requires navigating an open-ended search space through costly end-to-end evaluations. We introduce HarnessFlow, a framework for optimizing complete executable harnesses under a limited candidate-evaluation budget, with the model and task environment held fixed. HarnessFlow organizes candidates and their evaluation histories in a refinement tree, using a Monte Carlo Tree Search (MCTS)-based policy to balance exploitation and exploration. A coding agent refines selected harnesses using archived code, execution feedback, and a library of reusable harness mechanisms. With 15 refinement attempts per benchmark, HarnessFlow achieves the highest mean test scores among the compared methods on six benchmarks spanning agentic tasks, coding, and web interaction. The optimized harnesses achieve an average score of 69.48%, outperforming the initial harnesses and Meta-Harness by 10.89 and 3.95 percentage points, respectively, while incurring lower average per-task execution costs than hand-engineered baselines. These results suggest that structured harness search offers a promising route toward automating the design of capable and efficient LLM agents.


### Agent Systems: MANGO Arena: Same Seeds, Different Chains Evaluating LLM Agents in a Disrupted Supply Chain (MANGO Arena：同种种子不同链条在供应链被扰动环境中评估 LLM Agent)

- **arXiv**: [2611.23613](https://arxiv.org/abs/2611.23613) · **Venue**: Agent Systems · **Published**: 2026-11-17
- **Title (English)**: MANGO Arena: Same Seeds, Different Chains Evaluating LLM Agents in a Disrupted Supply Chain
- **Title (Chinese)**: MANGO Arena：同种种子不同链条在供应链被扰动环境中评估 LLM Agent
- **Authors**: Sara Amar
- **Affiliation**: Department of Engineering, Bowling Green State University; company in a serial supply chain adapted from MANGO, a classroom factory-management game.; classroom factory-management game, into an environment in which each company is an LLM; Figure 1:The MANGO Arena supply chain. Each company is played by its own agent.

**Problem background**: 基于种子/交叉组合的工厂游戏，用策略测试 Agent 是否违规规则；关注石料、价格输错、生产容量等，真实环境（石料、现金、容量），双规则交互。

**Methodology & innovations**:
三种测量：bullwhip 效应（经济结果）、在压力下的规则遵守度、须请求路径；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: We introduce MANGO Arena, an open-source testbed in which four LLM agents each run one company in a serial supply chain adapted from MANGO, a classroom factory-management game. The environment enforces hard rules (a truck limit, a no-credit cash constraint and production capacity), logs every blocked attempt to break them, and gives agents a public message board on which side payments are explicitly forbidden. This lets one environment measure three things at once: an economic outcome (the bullwhip effect), rule adherence under pressure, and proposals to collude. In a pilot with three small reasoning models, two scripted reference policies, two conditions (with and without a supplier fire) and three demand seeds, all LLM agents amplified demand variability as it moved upstream, by 7 to 25 times at the Retailer and 13 to 179 times at the Supplier, often more than a textbook order-up-to policy. They did so largely by ordering in batches (zero orders in up to 60% of decisions). Real rule violations were rare (at most 7 of 288 decisions per model) and no agent proposed a money side deal. The pilot's main lesson concerns evaluation method. API failures (rate limits and runaway hidden reasoning) entered the metrics silently as "no order" decisions. And when we reran games with the same seeds and no failed calls, upstream bullwhip changed by up to 17 times between runs. With three seeds, conclusions about how a disruption affects a given model did not survive a rerun. We report these failures in full and propose reporting practices for multi-agent evaluations of this kind. Code, prompts and every logged decision are public.


### Agent Systems: An Explainable Agentic AI Framework for Distribution System Load Restoration (可解释 Agent 框架：分布系统负荷恢复)

- **arXiv**: [2611.22016](https://arxiv.org/abs/2611.22016) · **Venue**: Agent Systems · **Published**: 2026-11-17
- **Title (English)**: An Explainable Agentic AI Framework for Distribution System Load Restoration
- **Title (Chinese)**: 可解释 Agent 框架：分布系统负荷恢复
- **Authors**: S. M. Monzurul Hoque Chowdhury, Qinghua Li
- **Affiliation**: ment of Electrical Engineering and Computer Science, University of Arkansas,

**Problem background**: 配电系统负荷恢复，增加了惩罚权重，可解释性支持。

**Methodology & innovations**:
多智能体架构：多智能体+LLM，多级 LLM Agent 用于规划、仲裁与决策；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Distribution system load restoration is a sequential decision-making problem in which restoration actions must maximize served load, prioritize critical loads, and preserve power-flow feasibility. This paper proposes an explainable agentic artificial intelligence (AI) framework for distribution system load restoration. The proposed framework uses multiple large language model (LLM) agents for planner guidance, strategic plan generation, decision arbitration, memory-based feedback, and explanation generation. Unlike unconstrained LLM-based control, the proposed method restricts agent decisions to feasible restoration actions and evaluates all candidate plans using deterministic AC power-flow feasibility checks. The framework is evaluated on IEEE 33-bus and 69-bus distribution feeders, as well as a larger IEEE 118-bus test case, and compared against reinforcement learning and planning baselines. The results show that the proposed agentic framework achieves better restoration performance while producing structured explanations for operator-facing decision support. A direct comparison with a Single-LLM-Agent baseline further shows that the proposed multi-agent decomposition improves weighted restored load and critical-load recovery compared with a monolithic LLM decision structure.


### Agent Systems: Agents of Chaos: A Systematization of Knowledge (SoK) on Malicious Attacks on Agentic AI Systems (Agentic AI 的混乱：在 Agentic 系统上恶意攻击的系统梳理知识 (SoK))

- **arXiv**: [2611.10843](https://arxiv.org/abs/2611.10843) · **Venue**: Agent Systems · **Published**: 2026-11-07
- **Title (English)**: Agents of Chaos: A Systematization of Knowledge (SoK) on Malicious Attacks on Agentic AI Systems
- **Title (Chinese)**: Agentic AI 的混乱：在 Agentic 系统上恶意攻击的系统梳理知识 (SoK)
- **Authors**: Thanh M. Truong-Le, Amber Bennoui, Hoang-Ly Nguyen, Gia-Thang Ho, Thai-Minh Truong, Duc-Ly Vu
- **Affiliation**: ∗University of Information Technology, Vietnam; †Jiffy Labs, USA; ‡Eastern International University, Vietnam; §Ho Chi Minh City University of Technology (HCMUT), Vietnam National University, Vietnam

**Problem background**: Agentic 技能可以静默注入思考或访问权限，渗透不确定性和状态通道。

**Methodology & innovations**:
针对不可观察性的多层级策略蒸馏，动态行为探测（渗透），用控制论重写；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Agentic AI systems extend large language models with tools, memory, retrieval, browser or computer-use interfaces, code execution, external services, and multi-agent coordination. Although these capabilities enable agents to act beyond text generation and perform tasks, they also create attack paths through which adversaries can exploit untrusted content, deceptive metadata, poisoned state, compromised skills, mutable dependencies, or malicious code. Such attacks can manipulate planning and tool use, corrupt memory, abuse code-execution environments, and trigger harmful downstream effects. In this paper, we present a systematic review of malicious attacks targeting agentic AI systems. We screened 186 candidate sources and retained 98. Following independent coding and resolver adjudication, we identified 284 atomic attacks, 452 atomic safeguards, and 660 explicit attack--safeguard relationships. We organize attacks into eight causal-mechanism classes while retaining insertion points, activation conditions, abused capabilities, objectives, impacts, persistence, and evidence as orthogonal dimensions. Our analysis shows that tool, MCP, and action-layer attacks account for the largest share of atomic attacks, while the prompt-injection and action-hijacking class has the broadest paper coverage. We identify distinct class-specific activation patterns and separation between insertion and later activation. Safeguard coverage remains uneven: only 278 of 660 relationships are directly assessed, and strong coverage is uncommon. These findings support lifecycle-aware threat modeling, agent evaluation, tool governance, and defense-in-depth security for agentic AI systems.


### Agent Systems: CoT-WAM: Collaborative Training of Vision-Language Models and World-Action Models via Plan Latents (CoT-WAM：协同训练 Vision-Language Model 与 World-Action Model)

- **arXiv**: [2611.23803](https://arxiv.org/abs/2611.23803) · **Venue**: Agent Systems · **Published**: 2026-11-18
- **Title (English)**: CoT-WAM: Collaborative Training of Vision-Language Models and World-Action Models via Plan Latents
- **Title (Chinese)**: CoT-WAM：协同训练 Vision-Language Model 与 World-Action Model
- **Authors**: Jinhao Zhang, Yushen Zuo, Ke Rui, Weitao Zhou, Haibao Yu, Honglong Tian, Xiaoheng Ma, Jie Mei, Jiawei Wang, Minglei Li
- **Affiliation**: 1Harbin Institute of Technology, Shenzhen 2Simple AI; 3Tsinghua University 4Tuojing Intelligence 5The University of Hong Kong; 6The Hong Kong University of Science and Technology

**Problem background**: 需要语义和物理预测的室内操作；现有 WAM 缺乏语义基础。

**Methodology & innovations**:
提出模型：三个部件：语义工程仪器（状态分词与 MCMC 推理）、语言嵌入式事件模式与自我协调的对象属性；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: General robot manipulation requires both semantic competence and physical foresight. World action models (WAMs) acquire an understanding of and predictive capability over the physical world by jointly modeling visual foresight and action distributions. However, existing WAMs still lack semantic competence: they have limited ability to perform open-world scene understanding, semantic reasoning, and long-horizon planning. Although vision-language models (VLMs) provide these capabilities, effectively integrating their semantic priors into WAM prediction and control remains challenging. To address this challenge, we propose CoT-WAM, a jointly trained WAM-VLM framework. CoT-WAM uses a learnable embedding to exchange information between the VLM and the WAM, which is supervised by textual and goal-image signals during training to encode rich intent information. A tailored two-stage training strategy enables joint optimization and more effective collaboration between the VLM and WAM. We evaluate CoT-WAM on six benchmarks covering control performance, zero-shot generalization, and long-horizon planning. CoT-WAM achieves SOTA performance on LIBERO, CALVIN, and RoboCasa-Kitchen, and demonstrates stronger zero-shot generalization on LIBERO-Plus and LIBERO-Pro without fine-tuning. On RoboCasa365, it further improves long-horizon planning over baselines with and without external planners. Real-world experiments further demonstrate the effectiveness of our method in practical deployments. Code is available at: this https URL


### Agent Systems: QDA: Closed-Loop LLM Quantization Design with Agents (QDA：带 Agent 的闭环 LLM 量化设计)

- **arXiv**: [2611.23388](https://arxiv.org/abs/2611.23388) · **Venue**: Agent Systems · **Published**: 2026-11-17
- **Title (English)**: QDA: Closed-Loop LLM Quantization Design with Agents
- **Title (Chinese)**: QDA：带 Agent 的闭环 LLM 量化设计
- **Authors**: Xingyang Li, Tianlang Zhao, Song Han, Ligeng Zhu
- **Affiliation**: MIT NVIDIA

**Problem background**: Post-training quantization 受模型/精度差异影响；评估一个量化模型需数十个 GPU 时。

**Methodology & innovations**:
QDA 本身调用 LLM agent 量化 recipe；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Post-training quantization is the standard way to serve large language models at low cost. However, the best quantization recipe differs across models and precisions. As a result, experts must redesign it for every new model, which is time-consuming and often sub-optimal. Fortunately, an LLM agent can take over this design by refining the recipe over rounds of building and evaluating candidates, so that more rounds lead to better recipes. However, evaluating one quantized reasoning model takes tens of GPU-hours, and combining methods from different codebases means porting each to the new architecture by hand. We present QDA, a system in which an agent designs the recipe for each model and precision. To make evaluation fast, QDA scores each candidate in minutes by its output KL divergence from the original model on reasoning traces that the agent never sees, and checks promising ones with long generations to catch failures such as repetition loops. To make building fast, QDA provides a library of public PTQ methods that are compatible with one another and with new model architectures. Across four reasoning models, QDA improves accuracy over the strongest public recipe by 0.9, 1.4 and 2.2 percentage points on average at W4A16, W4A8 and W3A16, using 64 GPU-hours per search. On the 320B-parameter MoE model GLM-5.3-Flash at NVFP4 W4A4, it recovers 98.3% of the FP8 model's accuracy, against 96.9% for the best vendor checkpoint. Every QDA checkpoint also runs on existing serving kernels with no inference overhead. We will release the library, the evaluator and the harness.


### Sequential Modeling: Hindsight Forcing: Learning Better History from the Future in Autoregressive Video Diffusion (Hindsight Forcing：从未来修正历史的自回归视频扩散学习)

- **arXiv**: [2611.27074](https://arxiv.org/abs/2611.27074) · **Venue**: Sequential Modeling · **Published**: 
- **Title (English)**: Hindsight Forcing: Learning Better History from the Future in Autoregressive Video Diffusion
- **Title (Chinese)**: Hindsight Forcing：从未来修正历史的自回归视频扩散学习
- **Authors**: Haonan An, Yihang Tao, Yu Guo, Renlong Chen, Jiasheng Zhang, Yuguang Fang
- **Affiliation**: 1City University of Hong Kong, Hong Kong 2Philo AI, Singapore; 19]. To mitigate this mismatch, recent self-rollout methods,

**Problem background**: Few-step 流式扩散需生成历史，回顾传播收敛问题；解决退热更新已被探索。

**Methodology & innovations**:
知识输出：在推断期间增强性能向后校准，改善视觉稳定性与一致性；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Few-step autoregressive video diffusion enables real-time streaming generation, with each generated chunk serving as historical context for subsequent generation. To avoid the memory explosion of backpropagation through time, previous self-rollout methods typically truncate cross-chunk gradients or detach historical latents. As a result, earlier denoising computations receive no downstream feedback through the generated history on how to synthesize frames that facilitate subsequent generation, leading to visual drift and structural collapse as rollouts extend. To address this limitation, we propose Hindsight Forcing, which allows historical chunks to learn directly from future outcomes by decoupling forward generation from backward credit assignment via a latent straight-through bridge. In the forward pass, each chunk completes a full multi-step rollout to update the KV cache. In the backward pass, the bridge routes gradients from future losses back to a single selected denoising step per historical chunk, training both the context writer and historical denoiser on shared parameters without retaining the full trajectory graph. Remarkably, Hindsight Forcing requires no additional model parameters, architecture modifications, or separate trajectory replay. Extensive experiments on VBench demonstrate that Hindsight Forcing outperforms existing baselines in overall visual quality and dynamic motion, while ablation studies validate the benefit of supervising historical denoising. Code is available at this https URL .


### Sequential Modeling: PACE-WM: Parallel World Modeling with Action History for Visual Planning (PACE-WM：基于动作历史的并行世界建模)

- **arXiv**: [2611.27173](https://arxiv.org/abs/2611.27173) · **Venue**: Sequential Modeling · **Published**: 
- **Title (English)**: PACE-WM: Parallel World Modeling with Action History for Visual Planning
- **Title (Chinese)**: PACE-WM：基于动作历史的并行世界建模
- **Authors**: Haishan Liu, Shijie Lian, Bin Yu, Yao Zhang, Changti Wu, Fanping Liu, Jianzheng Liu, Lei Xie, Cong Huang, Kai Chen
- **Affiliation**: 1Nanjing University 2Zhongguancun Academy 3Huazhong University of Science and Technology; 4Harbin Institute of Technology 5Wuhan University 6East China Normal University; 7Zhongguancun Institute of Artificial Intelligence 8DeepCybo

**Problem background**: 世界模型只基于最后的观察没有考虑动作历史；相似观察隐藏不同状态。

**Methodology & innovations**:
用动作历史嵌入（递归记忆 + 因果 Transformer）为未来预测提供上下文；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: JEPA-style world models support visual planning by predicting future representations conditioned on future actions. However, similar observations can conceal different motion states, making temporal context essential for interpreting future action effects. We propose PACE-WM, a parallel world model that uses executed-action history to contextualize future prediction and planning. Specifically, PACE-WM maintains a recurrent memory of executed actions and uses this memory to condition a causal Transformer. PACE-WM predicts multiple future representations in parallel without recursive predicted-state feedback within each prediction window. We further introduce Reference-Anchored Minimum Progress (RAMP) for action selection during planning. RAMP scores candidate actions by their predicted goal improvement along direct and split paths relative to a shared reference. Across four visual planning tasks, PACE-WM with RAMP achieves an average success rate of 98\% and plans approximately 7-9× faster than autoregressive LeWM under matched CEM settings. We also construct four controlled benchmarks to evaluate PACE-WM's capabilities in motion disambiguation, goal-relative motion, and goal adaptation. Project page is available at this https URL .


### Benchmarks: What Does Matching a Human Intervention Effect Establish? Benchmark Checks for LLM Simulations (什么是匹配人类干预效果——LLM 模拟的基准检查)

- **arXiv**: [2611.27186](https://arxiv.org/abs/2611.27186) · **Venue**: Benchmarks · **Published**: 
- **Title (English)**: What Does Matching a Human Intervention Effect Establish? Benchmark Checks for LLM Simulations
- **Title (Chinese)**: 什么是匹配人类干预效果——LLM 模拟的基准检查
- **Authors**: Tengfei Shao, Asma Rezaei, Ali Reza Kamali
- **Affiliation**: ¹ Global Education Center, Waseda University, Tokyo, Japan; ² Faculty of Business and Law, School of Management, Anglia Ruskin University,; Cambridge CB1 1PT, United Kingdom; ³ Cambridge Silicon Age Centre for Innovation, Barnwell Business Park, Cambridge; Corresponding author: Tengfei Shao, Global Education Center, Waseda University, 1-

**Problem background**: LLM 模拟的验证依赖于与人类效果的等效性；聚合校准指标可能掩盖分类级差异。

**Methodology & innovations**:
Exploratory reanalysis: 72% of GPT-4's ±0.20 SD passes were zero-reference passes; GPT-4 passed 16 contrasts the zero reference failed (1.58 expected without response).

**Comparison with prior methods**: See abstract: reusable evaluation artifact for LLM self-evaluation diagnostics — black-box protocol, prompts, judge-reference labels, reproduction scripts, calibration-constrained diagnostic metrics.

**Experimental results**: 

**Abstract**: LLM simulations are validated by equivalence with human effects, yet a zero reference passes whenever the human 90 percent interval lies inside the margin, as the human benchmark shows before simulation. When the zero reference fails, planned precision gives independent simulations the margin up to which passing is a 5 percent test of response. In an exploratory 70-experiment reanalysis, 72 percent of GPT-4's ±0.20 SD passes were zero-reference passes; GPT-4 passed 16 contrasts the zero reference failed (1.58 expected without response). In a preregistered audit, Claude Sonnet 5.5 passed three intention targets, all zero-reference passes, and the registered belief-gradient control; norm beliefs changed 0.065 SD against humans' 0.351 (zero-reference check added after unblinding; norm beliefs emphasized after inspection). Registered tests detected no overestimation; average-effect intervals excluded overestimation above 0.08 SD. A group audit's precision floor is 1.33 facts against a 2.9-fact effect. Report the zero-reference threshold beside every equivalence decision.


### Benchmarks: ForecastGym: A Live, Controlled, and Replayable Benchmark for Forecasting Agents (ForecastGym：可控的、可复现的 LLM Agent 预测达人类级基准)

- **arXiv**: [2611.23045](https://arxiv.org/abs/2611.23045) · **Venue**: Benchmarks · **Published**: 2026-11-17
- **Title (English)**: ForecastGym: A Live, Controlled, and Replayable Benchmark for Forecasting Agents
- **Title (Chinese)**: ForecastGym：可控的、可复现的 LLM Agent 预测达人类级基准
- **Authors**: Yicheng Tao, Yuante Li, Zipei Fan
- **Affiliation**: yichengtao@cmu.edu; Carnegie Mellon University; yuantel@cs.cmu.edu; Jilin University

**Problem background**: 预测对 Web 搜索上任务需要动态分辨性决策，分布向阶梯收敛发展。

**Methodology & innovations**:
Live 工具分折：可调整的新闻时间范围（PublishDate_time_to 扩大 1.6×），例如现在只同之前 +2.6 倍差异；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Agents built on large language models (LLMs) increasingly forecast real-world events by searching the Web and reasoning over what they find. How well such an agent forecasts depends on both the retrieved evidence and the model, making control over that evidence essential for evaluation. Live evaluations can mix retrieval with reasoning when each system searches on its own, while retrospective search can leak later information through date filters or today's ranking of historical pages. Comparing models, search sources, and memory strategies requires both fixed evidence and a record of how it evolved before resolution. We introduce ForecastGym, which records what four commercial web search APIs return for open prediction-market questions every two days and replays this frozen evidence offline once outcomes are known, comparing models, memory, and captured search sources under a fixed evidence-acquisition policy. Its first release covers 150 questions, 614 evidence states, one per question and collection time, and 131k search results. Rerunning the same queries after settlement returns results that all but state the outcome for up to 92% of the questions, despite the tested date filters. On the frozen evidence, all tested LLMs trail the market in forecasting accuracy. Our diagnostic analysis suggests that missed public information contributes more to the gap in high-gap states than misreading does. Switching the search API changes a model's Brier score by up to 0.043, more than the spread across models, while persistent notes score similarly to rereading all evidence at half the input tokens. The evidence a forecaster sees can matter as much as the model that reads it.


### Benchmarks: The Vulnerability Window: Decision Instability in Quantized Reward Models (脆弱窗口：量化奖励模型决策不稳定性)

- **arXiv**: [2611.27155](https://arxiv.org/abs/2611.27155) · **Venue**: Benchmarks · **Published**: 
- **Title (English)**: The Vulnerability Window: Decision Instability in Quantized Reward Models
- **Title (Chinese)**: 脆弱窗口：量化奖励模型决策不稳定性
- **Authors**: Omkar Shewale, Deepak Kumar, Divakar Kumar Yadav
- **Affiliation**: Illinois Institute of Technology; University of Wisconsin–Milwaukee

**Problem background**: 奖励模型和 LLM 评判经常被量化，常性核查较为公平；决策不稳定性更关键。

**Methodology & innovations**:
4 位量化导致 reward 模型的成对决策在 1.1-12.3% 的情况反转，聚合准确率变化 ≤0.03 分（p=1.00，因为修复的错误与引入的错误相互抵消）。

**Comparison with prior methods**: 反转集中在全精度 margin 与量化噪声 σ 同阶的情况（高斯近似 Φ 分布）。

**Experimental results**: 

**Abstract**: Reward models and LLM judges are routinely quantized to 4 bits so that scoring many candidates stays affordable, and the usual check is that benchmark accuracy barely moves. That check is close to blind. Across eight reward models from two families (0.6B-8B), three generative judges and four 4-bit quantizers, quantization rewrites 1.1-12.3% of pairwise preference decisions on RewardBench while aggregate accuracy moves by as little as 0.03 points (p = 1.00), because the errors it fixes and introduces cancel. Flips concentrate where the full-precision margin is small relative to the quantization noise scale sigma: a Gaussian approximation Phi(-|m|/sigma) describes the aggregate rate, over-predicting it in all 30 scalar settings and failing for generative judges, and occupancy of the resulting vulnerability window falls from 25% to 7% with model size, which is what makes small judges fragile. The churn stays within noise under benign best-of-16 and becomes clear under adversarial pressure for some quantizers (146:54 harmful:helpful flips on one family, reversing sign on another). Downstream it changes what ships: across six (model, quantizer) pairs from two families, 14.6-65.7% of problems get a different best-of-64 selection while only 2.6-9.6% get a different final answer, with selections changing 5-8x more often than answers in every pair, and the pair the benchmark calls identical (0.03 points, p = 1.00) still changes 34.5% of them. Benchmark churn ranks that downstream change (rho = 0.89); benchmark accuracy does not order it reliably. Held-out audits then locate the useful diagnostic in the margin rather than the Gaussian: every margin-based predictor orders flips identically (AUC 0.927), and on the level a directly measured churn rate wins in-distribution. As a routing signal it is matched by plain top-k. The contribution is the characterization, not the model.


### Generative Models: LingSante-Pulse: Unified Physiological Pretraining through Random-Feature Prediction and Cross-Modal Alignment (LingSante-Pulse：通过随机特征预测与跨模态对齐的统一生理预训练)

- **arXiv**: [2611.27206](https://arxiv.org/abs/2611.27206) · **Venue**: Generative Models · **Published**: 
- **Title (English)**: LingSante-Pulse: Unified Physiological Pretraining through Random-Feature Prediction and Cross-Modal Alignment
- **Title (Chinese)**: LingSante-Pulse：通过随机特征预测与跨模态对齐的统一生理预训练
- **Authors**: Linxiao Yang, Wenwei Wang, Tian Zhou, Bingqing Peng, Zihao Zhang, Zuyi Zhu, Jinjie Gu, Liang Sun
- **Affiliation**: Not listed on arXiv page

**Problem background**: 临床监控与穿戴设备产生的信号组合和跨模态关系，难以联合利用；单传感器场景受限。

**Methodology & innovations**:
支持多信号 + 单传感器；一个统一的轻量模型；高效参数训练（占比 5.4%）；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Clinical monitoring and wearable devices capture complementary physiological signals, but their partially overlapping modality coverage makes within-signal information and cross-modal relationships difficult to exploit jointly. We introduce LingSante-Pulse, a unified, general-purpose and flexible physiological representation framework that learns from these heterogeneous recordings. A shared, signal-conditioned encoder processes each physical channel independently and supports different numbers and combinations of signals for multimodal assessment and single-sensor inference. Pairwise cross-modal alignment, structured random-feature prediction (RFP) and masked waveform reconstruction jointly learn physiological relationships and preserve informative within-signal structure. Across 38 general physiological task configurations spanning PPG, ECG, EEG and EMG, the frozen encoder achieves the best dataset-balanced mean rank in each domain. In sleep assessment, multimodal staging on the HMC dataset and EEG-only staging on the Sleep-EDF dataset reach Macro-F1 scores of 0.7784 and 0.7941, respectively, while single-lead ECG apnea screening achieves an AUROC of 0.9183. Controlled experiments show that function prediction and waveform reconstruction provide complementary supervision for retaining temporal and rhythmic information. Representations learned under continually refreshed random supervision generalize to unseen teacher realizations, and correct auxiliary modality correspondence improves respiration-only representations. These results demonstrate that a single encoder can learn reusable physiological features across signal types, prediction targets and sensor configurations from partially overlapping recordings.


### Generative UI: ControlAnything: Generative UI and On-Demand Device Integration for Mixed-Reality Hand Interaction by a Coding Agent (ControlAnything：通用混合现实控件的生成式 UI)

- **arXiv**: [2611.08321](https://arxiv.org/abs/2611.08321) · **Venue**: Generative UI · **Published**: 2026-11-05
- **Title (English)**: ControlAnything: Generative UI and On-Demand Device Integration for Mixed-Reality Hand Interaction by a Coding Agent
- **Title (Chinese)**: ControlAnything：通用混合现实控件的生成式 UI
- **Authors**: Bektur Ryskeldiev
- **Affiliation**: this integration to the moment of use and assigns it to a coding agent. On a Meta Quest 3, the; built on Meta’s Muse Spark model then writes a connector program on the wearer’s laptop, tests it; Code and video:https://github.com/Apolotary/controlanything(MIT license).; on Meta’s Muse Spark model, writes aconnector, a small Node program that declares named actions such as cutoff

**Problem background**: 数百亿节点的 LLM 结合第三方 LLM Agent（Meta Muse Spark）等形式输出；生成 MCP server 转换器、Web 语音界面等；

**Methodology & innovations**:
代码规模增长，延迟降至 25.2s（Meta Quest 3 实测）；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Connecting hand input in mixed reality (MR) to a nearby physical device typically requires an integration written in advance for that device, its transport and the mapping. ControlAnything defers this integration to the moment of use and assigns it to a coding agent. On a Meta Quest 3, the wearer selects an object outlined by SAM 3.1 and states what their hands should control. An agent built on Meta's Muse Spark model then writes a connector program on the wearer's laptop, tests it against the live device through hand-written MIDI, Bluetooth and key-press transports, and returns augmented-reality (AR) controls, a per-frame hand program, or both. These outputs are a form of generative UI, interfaces created by an AI model; here, the agent also generates and tests the code that binds the interface to a physical device. In a single-session technical evaluation with the author as the only wearer, nine of ten requests addressing five targets reached a ready state, and the wearer stopped one. The median time to ready was 32.5 s (range 24.9-57.8 s, excluding speech transcription); sequential model calls accounted for a median of 89.9% of this time, and 91.7% of input tokens came from the prompt cache. The system's evidence of success extends to transport acknowledgements but not to physical effects. These findings point to connector reuse and the observation of effects through the headset's own sensors as next steps for on-demand device integration in MR. A user study with first-time wearers is planned.


### Benchmarks: Agent Verifiers in Counterfactual Analysis: A Pilot Study Benchmarking Agentic Heterogeneous Treatment Effects ()

- **arXiv**: [2611.23621](https://arxiv.org/abs/2611.23621) · **Venue**: Benchmarks · **Published**: 2026-11-17
- **Title (English)**: Agent Verifiers in Counterfactual Analysis: A Pilot Study Benchmarking Agentic Heterogeneous Treatment Effects
- **Title (Chinese)**: 
- **Authors**: Satiyabooshan Murugaboopathy, Entejar Alam, Adel Daoud, Connor T. Jerzak
- **Affiliation**: 1Institute for Analytical Sociology, Linköping University, Linköping, Sweden; 2AI and Global Development Lab 3Uppsala University, Uppsala, Sweden; 4NLP@DSAI, Chalmers University of Technology, Gothenburg, Sweden; 5Department of Government, The University of Texas at Austin, Austin, TX, USA; 6Department of Statistics and Data Sciences, The University of Texas at Austin, Austin, TX, USA

**Problem background**: 

**Methodology & innovations**:


**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Agents can expand the covariate space of randomized experiments by retrieving fast-moving local context missed by slow-changing survey baseline covariates, helping characterize who benefits most from an intervention. Verifying such covariates is difficult: individual treatment effects are unobserved, retrieval leakage can pull post-treatment information into nominally pretreatment summaries, and encoder leakage can inject post-treatment pretraining knowledge into representations even after temporal filtering of inputs. Guided by a two-channel information bound separating summary provenance from encoder weights, we propose a three-layer benchmark protocol: (i) retrieval admissibility via pre-treatment date filtering; (ii) heterogeneity validation scored rank-weighted average treatment effects (RATEs); and (iii) encoder admissibility checked with chronologically vintaged encoders, future-fact probes, and weight perturbations. Across 11 datasets anchored by Uganda's Youth Opportunities Program, we compare session-isolated retrieval (sandboxed, bounded-budget agent runs per study) against a persistent workspace teammate (xAI's GrokBot) that builds one date-verified corpus per study while blinded to outcomes. The workspace teammate yields higher mean RATE ratios in 6/11 datasets for text alone and 7 for combined features, though paired tests show neither workflow universally dominates. Even on fixed retrieved text, encoder choice significantly shifts heterogeneity signal. Chronologically vintaged probes show no clear evidence of weight leakage, but single-record adapter perturbation analyses show that memorized future facts, once present, persist until injected noise degrades model output. Temporal filtering of retrieval is necessary but insufficient: verifying agent-generated covariates requires jointly examining source provenance, out-of-sample treatment-effect signal, and encoder weights.


### Recommendation Systems: More Than a Score: Reinforcement Learning with Verbalized Feedback for Generative Recommendation (More Than a Score: 带 Verbalized Feedback 的生成式推荐强化学习)

- **arXiv**: [2611.22410](https://arxiv.org/abs/2611.22410) · **Venue**: Recommendation Systems · **Published**: 2026-11-17
- **Title (English)**: More Than a Score: Reinforcement Learning with Verbalized Feedback for Generative Recommendation
- **Title (Chinese)**: More Than a Score: 带 Verbalized Feedback 的生成式推荐强化学习
- **Authors**: Zipeng Chen, Xinyu Lin, Yuliang Sun, Sheng Zhang, Zeyu Wang, Xiaowen Shi, Junwei Pan, Chengguo Yin
- **Affiliation**: 1Tencent Inc., China 2National University of Singapore, Singapore 3The Chinese University of Hong Kong, Hong Kong, China; 1beckzpchen@tencent.com, dragon_201203@yeah.net, peterzywang@tencent.com,; princewen2019@outlook.com, jonaspan@tencent.com, turingyin@tencent.com; group and are jointly optimized with group relative policy optimization. The user simulator is only required during training and; is removed at inference time. Experiments on three Amazon review datasets with two generative recommendation backbones

**Problem background**: 生成式推荐用 LLM 直接生成推荐，缺乏可解释约束。

**Methodology & innovations**:
VerRec：问句+动作条件 token 嵌入，高效引导生成式推荐；

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Large language models (LLMs) are increasingly used for generative recommendation, where recommended items are generated directly from users' interaction histories. To further improve recommendation quality, reinforcement learning (RL) has been applied to align these models with recommendation objectives. However, existing RL methods rely on scalar rewards to implicitly guide exploration. These rewards do not specify which aspects of a candidate conflict with the user's preferences or how the next candidate should differ. To address this gap, we propose VerRec, a verbalized feedback-guided RL framework for generative recommendation. Specifically, a user simulator generates personalized verbalized feedback based on the user's historical preferences and the candidate item profile. The policy uses this feedback to produce refined recommendations. Original and refined candidates form an expanded group and are jointly optimized with group relative policy optimization. The user simulator is only required during training and is removed at inference time. Experiments on three Amazon review datasets with two generative recommendation backbones demonstrate that VerRec improves recommendation accuracy and ranking quality. Further analyses show that verbalized guidance encourages exploration of more diverse candidates and helps the policy discover more rewarding recommendations during training.


### Code Execution Prediction: Scientific Coding with Large Language Models: Evidence from Finite Element Analysis (用大语言模型撰写科学代码：FEM 分析指标与差距)

- **arXiv**: [2611.21176](https://arxiv.org/abs/2611.21176) · **Venue**: Code Execution Prediction · **Published**: 2026-11-16
- **Title (English)**: Scientific Coding with Large Language Models: Evidence from Finite Element Analysis
- **Title (Chinese)**: 用大语言模型撰写科学代码：FEM 分析指标与差距
- **Authors**: Erfan Hamdi, Joel Shor, Emma Lejeune
- **Affiliation**: Department of Mechanical Engineering; Boston University; AI Bio Design, Allen Institute & Move37 Labs; Division of Systems Engineering

**Problem background**: LLM 自动化科学编程；数值正确性差；资料库庞大。

**Methodology & innovations**:
最佳模型单次实现率 87.1%；前两名实现者达到 49.9% 结合成功率；前两名测试者分别 82.6%；Claude Opus 5 with SimpleAgent 在 Pass@3 达到 96.5%，Pass^3 最高为 78.8%（任何模型-harness 组合 Pass^3 上界）。

**Comparison with prior methods**: Comparison with prior methods: see the paper — the abstract documents how this work relates to prior approaches.

**Experimental results**: Experimental results are author-reported in the abstract; not independently verified.

**Abstract**: Large language models (LLMs) offer a potential route to automating scientific programming, but their usefulness depends on consistently producing numerically correct code. We extend FEM-Bench to 17 finite element tasks involving nonlinear and history-dependent mechanics and structural dynamics, and evaluate 15 models on implementation and test generation without execution feedback. The best model succeeds in 87.1% of single-pass implementation trials, but rankings differ between tracks. The leading implementer achieves 49.9% joint test success, while the leading tester reaches 82.6%. For six models, we compare single-pass generation with two agentic harnesses that allow code execution and revision. Agentic execution solves some tasks that never succeeded in single-pass trials and improves consistency on others, but gains vary across models and harnesses, and regressions also occur. Claude Opus 5 with SimpleAgent reaches 96.5% Pass@3, the probability of at least one success in three attempts, but 77.1% Pass^3, the probability that all three succeed. No model-harness combination exceeds 78.8% Pass^3. To understand why agents submit incorrect code after passing their own checks, we analyze 249 failed agentic trajectories and identify six categories of self-verification failure. The most common are inadequate test coverage (73.1%) and reliance on generic consistency checks (70.3%), and in 28.5% of cases the tests share an error with the implementation. Motivated by these findings, an exploratory configuration with separate coder and tester agents achieves the highest observed scores, with 97.6% Pass@3 and 88.8% Pass^3. These results identify consistency across attempts and independent verification as the main obstacles to trusting LLM-generated scientific code.
