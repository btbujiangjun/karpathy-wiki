---
title: arXiv 会议论文摘要 2026-11-25
type: synthesis
created: 2026-11-25
updated: 2026-11-25
sources: [2611.30168, 2610.33456, 2610.29925, 2611.31848, 2511.15241, 2511.08181, 2601.11528, 2611.29753, 2610.38587, 2608.23271, 2611.30233, 2611.01870, 2610.32189, 2610.35635, 2509.12382, 2509.05564, 2609.06604, 2604.27852, 2611.31813, 2611.31804, 2611.31063, 2611.31554, 2611.31689, 2611.31656, 2611.31873, 2611.31868, 2611.31851, 2611.31685, 2611.31618]
tags: [arxiv, conference, icml-2026, aaai-2026, neurips-2025, iclr-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025, llm, recommendation, advertising, ctr, games, code-execution, agents, generative, sequential, benchmarks]
---

# arXiv 会议论文摘要 (Conference Digest) — 2026-11-25

> **数据来源:** 本报告通过 arXiv Export API (`https://export.arxiv.org/api/query`, `sortBy=submittedDate`) 于 2026-11-25T02:30Z 检索。会议论文以 `comments`/`journal_ref` 含会议名为据（如 ICML 2026、AAAI 2026 等）；每会议取最新提交的论文。
>
> - **筛选:** 已去重，仅保留 wiki 既有 arXiv ID 之外的新增论文（共 29 篇：18 篇会议论文 + 11 篇研究主题论文）。
> - **每个条目包含:** 标题（中英文）、作者与单位、会议、问题背景、方法论、核心创新、先前方法对比、实验结果、arXiv 链接（指标/结果按论文自报）。
> - arXiv API 与 abs 页面元数据未包含作者单位，局部条目标注为“未公开”。

---

## 第一部分: 会议论文 (Conference Papers)

### 1. ICML 2026

#### 2611.30168 — FiRE: Fine-grained Ranking Evaluation for Machine Translation（深度精细排序评估：机器翻译评估）

- **作者:** Wenyang Gao [Zhejiang University; School of Engineering, Westlake University]; Yinghao Yang [School of Engineering, Westlake University]; Xi Jin [Zhejiang University]; Jing Li [Sichuan Lan-bridge Information Technology Co., Ltd]; Yue Zhang [School of Engineering, Westlake University]（单位标注为 arXiv 元数据可得）
- **会议:** ICML 2026 · [arXiv 2611.30168](https://arxiv.org/abs/2611.30168) · [PDF](https://arxiv.org/pdf/2611.30168) · 提交日期 2026-11-23

**问题背景:** 现有 MT 评估范式要么是粗粒度的整体排名（奖励一致的翻译质量），要么与人类偏好不对齐。对标注数据有限的参考无场景（reference-free）下的评估，获得既可解释又聚焦人类比较判断的方法仍是难点。

**方法论:** 提出 Fine-Grained Ranking Evaluation（FiRE）：利用已有大语言模型执行由准则驱动的成对比较，沿三个互补维度（faithfulness 信忠度、fluency 流畅度、consistency of style 风格一致性）替代单一整体判定。构造首个人类标注的、参考无场景的细粒度排序评估基准，用于 meta-evaluation；在此基准与既有 MQM 数据集上对比回归型与错误分析指标的对齐能力。

**核心创新:**
1. 细粒度、多维准则驱动的配对比较范式（信忠度/流畅度/风格一致性三维度）。
2. 首个参考无场景细粒度排序评估基准，用于 meta-evaluation（对比：此前均依赖整体排名或外部人类标注，参考无场景高粒度测评较少）。

**先前方法对比:** 对比回归型指标与错误分析指标，FiRE 在对齐人类比较判断上表现更好（摘要：demonstrably outperforms）。

**实验结果:** 摘要称 FiRE 在基准与既有 MQM 数据集上对齐度更高；代码在 https://github.com/wygao8/FiRE-MT。

---

### 2. AAAI 2026

#### 2610.33456 — FG-ConvNO: A Geometry-Aware Neural Operator for Propeller CFD Prediction（面向螺旋桨 CFD 预测的几何感知神经算子）

- **作者:** Yichen Di、Valentin Duruisseaux、Di Zhou、Xinyi Li、Daniel Leibovici、Jean Kossauti、Anima Anandkumar（单位未公开）
- **会议:** AAAI 2026 · [arXiv 2610.33456](https://arxiv.org/abs/2610.33456) · [PDF](https://arxiv.org/pdf/2610.33456) · 提交日期 2026-10-24

**问题背景:** 计算流体力学（CFD）高仿真代价高昂，传统代理模型（如 grid-based 卷积算子）在复杂几何（螺旋桨）、低数据场景下存在严重泛化缺口。

**方法论:** 提出 Factorized Geometry Convolutional Neural Operator（FG-ConvNO）：几何感知编码、插值解码与全局量监督；并结合 DISCO 块（discrete-continuous 卷积）使模型不依赖离散化。

**核心创新:** 几何感知与可转移的神经算子；DISCO 使模型具备 discretization-agnostic 能力；提供在程序生成螺旋桨 CFD 数据集上最准的表面压力与全局推力预测。

**先前方法对比:** 摘要称 FG-ConvNO 在程序生成螺旋桨数据集上表面压力与全局推力预测精度最高。

**实验结果:** 摘要称几何先验整合提升了复杂几何上的稳定性与低数据泛化能力。

#### 2610.29925 — Privacy in Context Is Being Overlooked in the Age of General-Purpose LLMs（通用大模型时代私密性在语境中被忽视的现象）

- **作者:** Prakhar Ganesh、Yash More、Marco Romanelli、Ferdinando Fioretto、Golnoosh Farnadi（单位未公开）
- **会议:** AAAI 2026 · [arXiv 2610.29925](https://arxiv.org/abs/2610.29925) · [PDF](https://arxiv.org/pdf/2610.29925) · 提交日期 2026-10-21

**问题背景:** 用户与通用系统交互时会跨许多语境，加剧了由此导致的隐私风险；现有提示隐私方向逐渐走向统一框架，可能造成误导。

**方法论:** 定性分析此类“统一框架”趋势的问题与需求，建议三条前进路径。

**核心创新:** 系统性地指出了统一提示隐私框架的更深张力；给出三条具体路径：应用特定部署、语境特定评估、隐私素养提升。

**实验结果:** 摘要级研究，无量化实验结果。

---

### 3. NeurIPS 2025

#### 2610.35635 — Offline Language-Based Support System for Tactical Decision-Making in Air Combat Operations（航空战斗指令行动的离线语言支持系统——MATE）

- **作者:** Joao P. A. Dantas（单位未公开）
- **会议:** NeurIPS 2025 · [arXiv 2610.35635](https://arxiv.org/abs/2610.35635) · [PDF](https://arxiv.org/pdf/2610.35635) · 提交日期 2026-10-26

**问题背景:** 飞行员需要快速、准确地检索战术规则，现有系统要么依赖人工索引，要么在线检索延迟高。

**方法论:** 提出 MATE（Mission Assistant for Training and Evaluation）系统，全部基于开源组件（文本预处理、embedding 生成、语义搜索、LLM 生成）完成，全离线部署。

**核心创新:** 完全离线的语义检索与战术决策支持流程；与人工索引系统相比，能以 RAG 方式回答 5 个战术问题。

**先前方法对比:** 相对人工检索提供自动化且低延迟的路径。

**实验结果:** 由 3 名巴西空军战斗机飞行员评分（1–5 分，Mistral NeMo 12B 得分最高），反应时评价为“完全满意”。

---

### 4. ICLR 2026

#### 2611.30233 — CLIP-FMoE: Scalable CLIP via Fused Mixture-of-Experts with Enforced Specialization（基于融合 MoE 的可扩展 CLIP：CLIP-FMoE）

- **作者:** Luong Tran、Lan-Cuong Nguyen、Huynh Dang Nguyen、Dat Nguyen Cong、Dung D. Le、Van Nguyen（单位未公开）
- **会议:** ICLR 2026 · [arXiv 2611.30233](https://arxiv.org/abs/2611.30233) · [PDF](https://arxiv.org/pdf/2611.30233) · 提交日期 2026-11-23

**问题背景:** 现有 MoE 适配 CLIP 模型存在训练开销大、零样本能力下降、上下文长度泛化弱等问题。

**方法论:** 提出 CLIP-FMoE，集成 MoE 于 CLIP 细调：Isolated Constrained Contrastive Learning 在簇划分的数据分区上训练专家；Fusion Gate 缓解灾难性遗忘。

**核心创新:** 专家专业化加速 + 防遗忘 Gate；在多个基准上提升下游任务性能，同时保持零样本能力。

**实验结果:** 摘要称：实验在多个基准/任务上进行，在长上下文下稳定。

#### 2611.01870 — Automated Stateful Specialization for Adaptive Agent Systems（自适应智能体系统的有状态专业化：ASpec）

- **作者:** Myan Vu、Harrish Ayyanar、Jiang Pang、Anwiketh Reddy、Mayank Goel（单位未公开）
- **会议:** ICLR 2026 · [arXiv 2611.01870](https://arxiv.org/abs/2611.01870) · [PDF](https://arxiv.org/pdf/2611.01870) · 提交日期 2026-11-01

**问题背景:** 现有自动化智能体设计框架二元：静态工作流（缺乏可适应性）或逐查询优化（阻碍技能的积累），无法让智能体在新任务中自主进化。

**方法论:** 提出 ASpec 框架：进化搜索自动发现专家架构原型，通过经验耕作培养专长；引入"retain-then-escalate"层级控制策略（先使用现有系统再适应结构）。

**核心创新:** 有状态专家团队（specialist teams of specialist agents）+ 进化自动化发现；在 GPQA 等专家级科学基准上取得显著提升。

**实验结果:** 摘要称：在专家级科学基准（GPQA）上取得了显著性能提升，同时在更广泛的领域任务上匹配 SOTA。

---

### 5. KDD 2026

#### 2610.32189 — EVOLVE: Uncertainty-Aware Multivariate Time Series Anomaly Prediction with Adaptive Prototype Memories（EVOLVE：带自适应原型记忆的多变量时序异常预测）

- **作者:** Jianxin Jin、Kai Zhao、Shiyan Hu、Yang Shu、Peng Chen、Meng Wang、Zhongwen Rao、Yijie Li、Jing Wang、Bin Yang、Chenjuan Guo（单位未公开）
- **会议:** KDD 2026 · [arXiv 2610.32189](https://arxiv.org/abs/2610.32189) · [PDF](https://arxiv.org/pdf/2610.32189) · 提交日期 2026-10-23

**问题背景:** 既有异常预测方法共享同一扰动轨迹（变量/语境无差异），且未对未确定性做建模；现实异常发展具有变量-语境相关性，未来轨迹可不唯一。

**方法论:** 提出 EVOLVE 框架：变量/语境条件化扰动 + 变异性感知未来推理（采样多潜变量历史状态，解码互补的平滑与偏离放大假设，以轨迹不一致度估计异常风险）；自适应异常原型记忆支持动态更新与检索。

**核心创新:** 变量/语境条件化扰动 + 不确定性估计；跨六个真实基准数据集显著优于既有基线。

**实验结果:** 摘要称：六个真实基准上一致优于 SOTA 异常预测基线。

---

### 6. CVPR 2026

#### 2611.29753 — DREAM: Dual-Memory Reasoning for Anticipatory 3D Perception in Autonomous Driving（DREAM：自动驾驶预感 3D 感知的双记忆推理）

- **作者:** Sriram Mandalika、Athira Nambiar（单位未公开）
- **会议:** CVPR 2026 · [arXiv 2611.29753](https://arxiv.org/abs/2611.29753) · [PDF](https://arxiv.org/pdf/2611.29753) · 提交日期 2026-11-22

**问题背景:** 现有 LiDAR 语义分割逐帧处理，丢弃历史上下文，限制了动态场景变化下的鲁棒性。

**方法论:** 提出 DREAM 框架：在线双记忆——潜在记忆（紧凑语义抽象）+ 错误记忆（高不确定性预测的表示），通过余弦相似度检索并轻量调制到特征中；冻结骨干，无重放。

**核心创新:** 持久语义记忆与错误感知记忆的组合；无积累的计算/内存上限；大型 LiDAR 基准上一致提升动态与小目标的性能。

**实验结果:** 摘要称多个大规模 LiDAR 基准上达到 SOTA。

#### 2610.38587 — RoSAMDepth: Robust Self-supervised Depth Estimation Leveraging Segment Anything Model（RoSAMDepth：利用 SAM 的鲁棒自监督深度估计）

- **作者:** Xuanang Gao、Zhiwei Ning、Gengming Zhang、Jiaxi Cao、Runze Yang、Zhonglong Zheng、Jie Yang、Rong Xiao、Wei Liu（单位未公开）
- **会议:** CVPR 2026 · [arXiv 2610.38587](https://arxiv.org/abs/2610.38587) · [PDF](https://arxiv.org/pdf/2610.38587) · 提交日期 2026-10-28

**问题背景:** 自监督深度估计在恶劣条件下深度不准，且单模态不考虑对象级信息（对象内深度变化）。

**方法论:** 提出 RoSAMDepth：引入 SAM（Segment Anything Model）对象级先验，分三个方面：分段引导的表示对比注入；自适应区域外点掩蔽 + 区域高斯似然损失（区域深度平滑）；对象级可靠性估计缓解噪声监督。

**核心创新:** 对象级先验三个方面；多数据集/恶劣天气下一致超越 SOTA。

**实验结果:** 摘要称：在多个数据集与天气条件下生成更锐利、更准确的深度（代码 https://github.com/xagao/RoSAMDepth）。

---

### 7. ACL 2026

#### 2611.31848 — Faithful Persona Steering under Incongruity via Dual-Stream Refinement（QuirkyMind：基于双流细化的信任主体一致性自适应发展）

- **作者:** Yu-An Chu、Jen-Ren Pong、Chia-Yao Yeh、Meng-Fen Chiang（单位未公开）
- **会议:** ACL 2026 · [arXiv 2611.31848](https://arxiv.org/abs/2611.31848) · [PDF](https://arxiv.org/pdf/2611.31848) · 提交日期 2026-11-24

**问题背景:** 标准 LLM 个性化将身份视为静态检索，忽略了人类人格中“稳定特征与非典型角色立场并存”的一致性；Prompt 在长序列中漂移、微调抹掉热点。

**方法论:** 提出 QuirkyMind：Traits Anchoring 构建双流潜态（语句级摘要用于语义稳定 + token 级序列用于生成控制）；In-Context Narrative Refinement 用 InfoNCE 锚定 + 交叉熵保证表示稳定与逐字一致；通过参数高效适配器将状态迁移到下游任务。

**核心创新:** 身份定义与表达分离；双流潜态 + 缓解漂移；在 Persona-Steered QA 与 Narrative Inference 上验证。

**实验结果:** 摘要称：缓解漂移、稳固个性知识且不抹除真实的“热点”。

---

### 8. EMNLP 2025

#### 2608.23271 — Expectations and Practices around AI Disclosure in CS Research（CS 研究中 AI 披露的期望与实践）

- **作者:** Arati Mohapatra、Danish Pruthi（单位未公开）
- **会议:** EMNLP 2025 · [arXiv 2608.23271](https://arxiv.org/abs/2608.23271) · [PDF](https://arxiv.org/pdf/2608.23271) · 提交日期 2026-08-24

**问题背景:** 各顶会 AI 披露政策千篇一律（低质量），实践中则出现“写作辅助被大量披露却被视为不必要”的错位。

**方法论:** ① 调研 109 位 CS 研究者，编码披露必要性；② 分析 13,867 条 EMNLP 2025 与 ICLR 2026 的披露声明；比对期望与实践。

**核心创新:** 提出任务分级与披露路线图（分类研究任务、新模板），提升政策与实践的一致性。

**实验结果:** 摘要称发现了期望与实践的大面积错位（写作辅助）。

---

### 9. SIGIR 2026

#### 2609.06604 — TaxoConf: Taxonomy-Guided Automatic Conference Program Organization（TaxoConf：基于主题分类的会议程序自动组织）

- **作者:** Daomin Ji、Zhifeng Bao、Junhao Gan（单位未公开）
- **会议:** SIGIR 2026 · [arXiv 2609.06604](https://arxiv.org/abs/2609.06604) · [PDF](https://arxiv.org/pdf/2609.06604) · 提交日期 2026-09-06

**问题背景:** 将接收论文组织成技术会话是劳动密集型且受硬约束限制；此前方法在主题连贯性与硬约束两端难以兼得。

**方法论:** 构建会议特定的全排序主题分类，对论文表示为最具体主题的边界；用特异性加权的最优传输距离 + 二元整数规划，在满足全部硬约束下最小化会话内距离。

**核心创新:** 约束感知的会话赋值；已实际部署于 SIGIR 2026（保留 91.8% 的 oral 评分，无硬约束违规，参与人员正面评价 4.26/5）。

**实验结果:** 基准四个 2025 会议上 session coherence 4.62/5，与人工会话 NMI 0.761，无约束违反。

---

### 10. WWW 2026

#### 2604.27852 — NeocorRAG: Less Irrelevant Information, More Explicit Evidence, and More Effective Recall via Evidence Chains（NeocorRAG：基于证据链的 RAG 检索质量优化）

- **作者:** Shiyao Peng、Qianhe Zheng、Zhuodi Hao、Zichen Tang、Rongjin Li、Qing Huang、Jiayu Huang、Jiacheng Liu、Yifan Zhu、Haihong E（单位未公开）
- **会议:** WWW 2026 · [arXiv 2604.27852](https://arxiv.org/abs/2604.27852) · [PDF](https://arxiv.org/pdf/2604.27852) · 提交日期 2026-04-30

**问题背景:** 检索质量与下游推理性能之间存在缺乏整体性优化的痛点（只优化 Recall 或只优化相关性，会造成另一处的权衡）。

**方法论:** 提出 Recall Conversion Rate（RCR）指标，量化检索对推理的贡献；提出 NeocorRAG 框架：（1）激活搜索生成细化候选空间；（2）受约束解码生成精确证据链；（3）证据链指导检索优化。

**核心创新:** 系统性检索质量优化标准 + 证据链驱动；在 HotpotQA、2WikiMultiHopQA、MuSiQue 与 NQ 上在 3B 与 70B 参数模型上均达 SOTA。

**实验结果:** 调研显示 Recall@5 提升时 RCR 呈近似线性衰减；最终 NeocorRAG 以 <20% token 预算达到 SOTA。

---

### 11. CIKM 2025

#### 2511.15241 — Selective Mixup for Debiasing Question Selection in Computerized Adaptive Testing（CAT 选题去偏：选择性 Mixup）

- **作者:** Mi Tian、Kun Zhang、Fei Liu、Jinglong Li、Yuxin Liao、Chenxi Bai、Zhengtao Tan、Le Wu、Richang Hong（单位未公开）
- **会议:** CIKM 2025 · [arXiv 2511.15241](https://arxiv.org/abs/2511.15241) · [PDF](https://arxiv.org/pdf/2511.15241) · 提交日期 2025-11-19

**问题背景:** CAT 的题目选择本身存在选择偏差（低估者给更简单题目），该偏差贯穿自适应过程被放大。

**方法论:** 提出两模块：Cross-Attribute Examinee Retrieval（检索可近于均衡的“参照考生”）+ Selective Mixup-based Regularization（在偏差考生与参照考生间做 label-consistency 的 Mixup，增强偏差冲突样本）。

**核心创新:** 双模块反偏；在两个基准、多种诊断模型上显著提升泛化与公平性。

**实验结果:** 摘要称性能大幅提升（具体数字未公布）。

#### 2511.08181 — MARC: Multimodal and Multi-Task Agentic Retrieval-Augmented Generation for Cold-Start Recommender System（MARC：冷启动推荐系统的多模态多任务智能体 RAG）

- **作者:** Seung Hwan Cho、Yujin Yang、Danik Baeck、Minjoo Kim、Young-Min Kim、Heejung Lee、Sangjin Park（单位未公开）
- **会议:** CIKM 2025 · [arXiv 2511.08181](https://arxiv.org/abs/2511.08181) · [PDF](https://arxiv.org/pdf/2511.08181) · 提交日期 2025-11-11

**问题背景:** 推荐系统冷启动场景下，现有方法多依赖模态信息或追加“Agent”概念，难以生成高质量、语境相关的商品推荐。

**方法论:** MARC 是一个多模态多任务餐厅（鸡尾酒）推荐系统：构建基于图数据库的应用场景，两个核心流程：任务识别路由 + 反思流程；构建 Kaggle 餐厅数据集。

**核心创新:** 图库+智能体 RAG 的冷启动框架；验证用 LLM-as-a-judge 与人工评估（图库路径优于简单向量库）。

**实验结果:** 摘要称通过 200 个人工构造问题的评估获得 200 个手工构造的问题。

#### 2601.11528 — Knowledge Graph Construction for Stock Markets with LLM-Based Explainable Reasoning（基于 LLM 可解释推理的股票市场知识图谱构建）

- **作者:** Cheonsol Lee、Youngsang Jeong、Jeongyeol Shin、Huiju Kim、Jidong Kim（单位未公开）
- **会议:** CIKM 2025 · [arXiv 2601.11528](https://arxiv.org/abs/2601.11528) · [PDF](https://arxiv.org/pdf/2601.11528) · 提交日期 2025-11-16

**问题背景:** 股市复杂且关系密集，传统研究偏好时间序列预测，缺乏关系建模与可解释的投资推理。

**方法论:** 构建针对性股市 KG schema（公司、板块、股指、财务指标、跨公司关系），与 LLM 结合做多跳推理与关系查询。

**核心创新:** 系统化股市 KG schema；基于 KG 的 LLM 可解释投资分析（在韩国上市公司上验证）。

**实验结果:** 摘要称在实际案例中验证该框架，展示了相比传统数据库查询更深的洞察。

---

### 12. RecSys 2025

#### 2509.12382 — LLM-as-a-Judge: Rapid Evaluation of Legal Document Recommendation for Retrieval-Augmented Generation（LLM-as-a-Judge：法律文档推荐 RAG 的快速评估）

- **作者:** Anu Pradhan、Alexandra Ortan、Apurv Verma、Madhavan Seshadri（单位未公开）
- **会议:** RecSys 2025 · [arXiv 2509.12382](https://arxiv.org/abs/2509.12382) · [PDF](https://arxiv.org/pdf/2509.12382) · 提交日期 2025-09-15

**问题背景:** RAG 系统评估在法律检索中最紧迫，传统指标难以捕获推荐质量的细微维度（摘要：标准指标缺失了 RAG 语境下推荐质量的细微维度）。

**方法论:** 将 LLM 作为自身的评判者；验证 LLM-vs-人工的一致性（Gwet's AC2、威尔科克松秩相关 + Benjamini-Hochberg），并进行统计严谨的系统对比。

**核心创新:** 两大可落地问题：应选择哪些一致性指标？如何严谨比较。结论：统计显著性强。

**实验结果:** 摘要称建立了可扩展、成本更低且精度更高的评估路径。

#### 2509.05564 — Knowledge-Augmented Relation Learning for Complementary Recommendation with Large Language Models（基于 LLM 的知识增强互补推荐关系学习：KARL）

- **作者:** Chihiro Yamasaki、Kai Sugahara、Kazushi Okamoto（单位未公开）
- **会议:** RecSys 2025 · [arXiv 2509.05564](https://arxiv.org/abs/2509.05564) · [PDF](https://arxiv.org/pdf/2509.05564) · 提交日期 2025-09-06

**问题背景:** 互补推荐的标签由“函数标签 FBL”（高质量、人工定义）与“行为标签（噪声大、容易生成）”之间存在巨大权衡。

**方法论:** KARL 框架：动态采样策略（基于最难样本）+ LLM 语义扩展（扩充 FBL 标注）；降低 FBL 构建成本。

**核心创新:** 知识增强 + 主动学习融合；在 OOD 设置下 KARL 提升达 37%。

**实验结果:** 摘要称 OOD 下准确度提升最高达 37%，ID 下提升 <0.5%（长期可能劣化）。

---

## 第二部分: 其他研究主题论文 (General Topic Papers)

### A. AI / LLMs

#### 2611.31813 — Agentic Discovery of Soundness Bugs in Safe Rust Bindings（LLM 智能体审计安全 Rust 绑定接口，发现超 60 个注入 UB 的缺陷）

- **作者:** Marius Momeu、Koushik Sen（单位未公开）
- **会议:** 相关单位：Crustify 方案基于安全/安全性工具；[arXiv 2611.31813](https://arxiv.org/abs/2611.31813) · [PDF](https://arxiv.org/pdf/2611.31813) · 提交日期 2026-11-24

**问题背景:** Rust 安全接口编码错误（“弱上界规则”）可使纯安全 Rust 程序产生 UB，但静态分析与 Fuzzer 固定模式、高开销，无法发现深层缺陷。

**方法论:** 将 LLM 智能体（Claude Opus 5.5 / DeepSeek V4.1 Flash）作为接口审计员；构建缺陷分类（UB、库不一致、不完整 contracts）；两次激进的试水（3 小时内完成，p50 成本不足 $50）。

**核心创新:** 智能体发现 UB 与不完整 contract 优于静态工具；Crustify 自动化 C-to-Rust 迁移流水线。

**实验结果:** 在 16 个常用 crate（OpenSSL、SQLite、libgit2、libcurl、V8 等）中发现 225 个 UB 漏洞、23 个行为不一致、36 个不完整 contracts；Maintainers 已修复其中 26/83。

#### 2611.31804 — Federated Policy Gradient for Dynamic Consensus: Gradient Dominance and Topological Bounds（联邦策略梯度动态共识）

- **作者:** Maryam Babazadeh（单位未公开）
- **来源:** [arXiv 2611.31804](https://arxiv.org/abs/2611.31804) · [PDF](https://arxiv.org/pdf/2611.31804) · 提交日期 2026-11-24

**问题背景:** 多智能体动态共识中，通信图谱驱动的异构性带来了任何控制之外的挑战。

**方法论:** 模态分解（Modal Decomposition）转化为模式基准；推导参数化的子最优上界；基于拉普拉斯谱的缺陷轨迹收敛条件（互补测试达到全局共识策略，目标在零阶探索 + 双分方程确定后渐近轨迹的可实现性）。

**核心创新:** 首个联邦策略梯度框架 + 谱边界分析（支持积极图谱、拓扑分布实现“梯度主导”约束）。

**实验结果:** 模拟研究表明，联邦方法相对模型基与数据驱动分离方法的性能一致性领先（摘要未给具体数字）。

### B. 推荐系统

#### 2611.31063 — From Local Errors to System Failures: Modeling and Benchmarking Error Propagation in Multi-Agent LLM Systems（REPA：多智能体系统错误传播模型与基准 ErrPropBench-10）

- **作者:** Wenlong Yu、Bingxu Lu、Qilong Wang、Qinghua Hu、Qianru Sun（单位未公开）
- **来源:** [arXiv 2611.31063](https://arxiv.org/abs/2611.31063) · [PDF](https://arxiv.org/pdf/2611.31063) · 提交日期 2026-11-23

**问题背景:** MAS（LLM 驱动）中本地错误可通过消息传播造成系统级失败；结果基评估掩盖了放大、衰减或修正的机制。

**方法论:** 提出 REPA（Response-Aware Error Propagation among Agents）：分离输入组装与智能体处理两个维度；理论分析联系本地模型误差与端点预测误差。

**核心创新:** REPA 在 6 个 MAS 工作流、3 个 Qwen 基础模型、10 种知识/推理场景上实现中级相关性（Spearman 0.84 vs 0.47）；报告 ERRPROP 基准与性能（摘要数字：平均 0.84 vs 0.47）。

**实验结果:** 摘要：REPA-guided RAG 让准确度提升 19 个百分点（+16% token），提供可解释的错误传播路径。

#### 2611.31656 — BRAG: Bayesian Retrieval Augmented Generation（BRAG：贝叶斯检索增强生成）

- **作者:** Javier Movellan、Manjot Bilkhu、Young-mok Jung、Sirajul Salekin、Henry Tran、Zhao Huang（单位未公开）
- **来源:** [arXiv 2611.31656](https://arxiv.org/abs/2611.31656) · [PDF](https://arxiv.org/pdf/2611.31656) · 提交日期 2026-11-23

**问题背景:** RAG 以语义相似性排序记忆块，但此类方法在检索价值漂移下缺乏框架。

**方法论:** BRAG 提出一种可更新的检索生成模型：每个块生成其可回答的查询（VMSF 模型），每个块可预设价格稳定；构建可实时更新的线程记忆；闭式滤波器在归约逻辑中处理检索与主题动态。

**核心创新:** 通过闭式滤波（仅每块两个标量 + 少量键）实现对各方法的判定，并把检索建模为经验控制问题。

**实验结果:** 两个长期记忆基准上 BRAG 在旧块问题上相当于既有方法，新块检出率上升 0.8–0.86；个人代理记忆 9 个月 20,640 条块上，Recall@5 提升 0.75→0.98，Recall@1 提升 0.44→0.97。

#### 2611.31851 — Modeling Event-Conditioned Emotional Expression Response with LLM Agents in a Synthetic Social Simulation（LLM 智能体在合成社会模拟中的情绪反应建模）

- **作者:** Rebecca Marigliano、Peter Carragher、Kathleen M. Carley（单位未公开）
- **来源:** [arXiv 2611.31851](https://arxiv.org/abs/2611.31851) · [PDF](https://arxiv.org/pdf/2611.31851) · 提交日期 2026-11-24

**问题背景:** 现有行为模型难以捕捉情绪对认知/集体行为的驱动作用，且缺乏可验证性。

**方法论:** 层级提示框架：LLM 智能体条件于人口统计、心理与语境，生成对真实世界事件的情绪反应，验证结果与斯坦福 Facebook URL Shares 数据集 + 年龄/人格基准一致。

**核心创新:** 验证了 LLM 智能体可模拟极性与一致性情绪模式；发现智能体表达缺乏“怒火”，与人类基线需进一步校准。

**实验结果:** 摘要称模拟结果显著重现分化与共识型情绪模式。

### C. 广告与 CTR

本窗口无 NEW 的广告/CTR 类论文（参考口径：2026-11-25 窗口内 arXiv 中 CTR 类相关笔记已在既有报告 `synthesis/2026-11-25/arxiv-daily.md` 等覆盖，如 DNA 2611.25659v1）。因此在本报告中 CTR/广告类条目取 0 篇。

### D. 代码执行预测

#### 2611.31554 — Agent Recovery Gone Wrong: Measuring Harm Beyond Duplicate Calls（代码执行失败后的恢复行为风险）

- **作者:** Artem Trofimov、Boris Novikov（单位未公开）
- **来源:** [arXiv 2611.31554](https://arxiv.org/abs/2611.31554) · [PDF](https://arxiv.org/pdf/2611.31554) · 提交日期 2026-11-23

**问题背景:** LLM 代码执行智能体在部分写入生效后失败时会改写并重试，此类“恢复”可能导致外部状态损坏，但无人统计其频率。

**方法论:** 以 AppWorld 智能体轨迹为基础：抽样 200 个智能体候选回话（145 个被数据库状态确认为部分执行），量化随后“有害恢复”的发生率。

**核心创新:** 定义并计算“有害恢复”率：30/143（加权估计 24.6%），并分析各类有害恢复（重复写入 2/3，删数据/错误写入 1/3）。

**实验结果:** 另分析了两种“操作身份”概念用于 idempotency contract（模型提供 vs 内容推导），推导时匹配为14–18/30。

### E. 智能体系统

#### 2611.31813（A 类已覆盖）、2611.31804（已覆盖）、2611.31063（已覆盖）、2611.31813 — 见第 A 部分。

#### 2611.31689 — GeoMVGen: Joint Appearance-Geometry Modeling for Multi-View Video Generation in Robotic Manipulation（GeoMVGen：精密机器人操作中的多视角外观-几何联合生成）

- **作者:** Qiaoqiao Jia、Guile Wu、Dongfeng Bai（单位未公开）
- **来源:** [arXiv 2611.31689](https://arxiv.org/abs/2611.31689) · [PDF](https://arxiv.org/pdf/2611.31689) · 提交日期 2026-11-23

**问题背景:** 机器人操作中，多视角的视觉外观与几何一致性难以建模，现有模型多为单模态。

**方法论:** 提出 GeoMVGen 框架：视频扩散 Transformer + 模态适配器（appearance/geometry 专用）+ 交叉模态残差；引入跨视角投影机制与几何导向损失（pointmap consistency + 几何基础模型对齐）。

**核心创新:** 模态特化 + 跨模态残差 + 几何跨视角对齐；在 4D 数据集（仿真与真实）上超越 SOTA 在质量/几何精度/跨视角一致性。

**实验结果:** 摘要称着在多个视觉质量与几何指标上击败了 SOTA 方法。

### F. 生成模型

#### 2611.31656 — BRAG（已于 B 提交）

### G. 游戏

#### 2611.31685 — A Constant-Factor Single-Sample Prophet Inequality for Subadditive Valuations（子可加估值的单样本先知不等式，常数因子）

- **作者:** Shuchi Chawla、Trung Dang（单位未公开）
- **来源:** [arXiv 2611.31685](https://arxiv.org/abs/2611.31685) · [PDF](https://arxiv.org/pdf/2611.31685) · 提交日期 2026-11-23

**问题背景:** 单样本先知不等式是研究信息价值与分配获利二元理论的基础。

**方法论:** 将任意 α 近似离线分配算法“简化”为在线算法：得到 α/120（先知）的全局获利；通过随机评分生成器与新型单候选分配构造控制内容竞争。

**核心创新:** 理论上首个子可加估值类单样本先知不等式（常数因子）+ 内容有界竞争结构。

#### 2611.31618 — Realization of expanding dynamics by a finite horizon parabolic law response（有限时视场残差实现扩张动力学）

- **作者:** Masood Shahbaz Shoukat、Luca Di Persio、Wensheng Jia（单位未公开）
- **来源:** [arXiv 2611.31618](https://arxiv.org/abs/2611.31618) · [PDF](https://arxiv.org/pdf/2611.31618) · 提交日期 2026-11-23

**问题背景:** 分位/收敛动力系统研究中，找到有限模式实现可确定规律。

**方法论:** 构造精确的有限模式相互作用，实现在平衡坐标上 ε 量级，并以 C^k 范数估计误差 ≤ Cε。

**核心创新:** 数学上验证了在扩张分支上产生紧积不变集与可寻找周期轨迹。

### H. 序列建模

#### 2611.11622 — GenISys: Integrated Ship Systems Design Using Subsystem-Conditional Tabular Diffusion（GenISys：基于子系统条件表格扩散模型的集成船舶系统设计）

- **作者:** Noah J. Bagazinski、Faez Ahmed（单位未公开）
- **来源:** [arXiv 2611.11622](https://arxiv.org/abs/2611.11622) · [PDF](https://arxiv.org/pdf/2611.11622) · 提交日期 2026-11-08

**问题背景:** 舰船设计需要协调耦合子系统以满足工程约束并在性能与成本上取得平衡；通用扩散模型难以区分各子系统的角色。

**方法论:** 提出“子系统条件化”表格扩散模型（GenISys）：一个生成模型构建集成设计，不同子系统由不同条件分支处理，生成过程考虑系统级耦合。

**核心创新:** 条件化扩散架构驱动多子系统协同设计。

**实验结果:** 摘要未给出具体数字。

### I. 基准测试

#### 2611.31873 — RepoEviAgent: Scalable Synthesis of Evidence-Grounded Repository-Level Question Answering Tasks（RepoEviAgent：证据驱动仓库级问答任务合成）

- **作者:** Aoqi Hu、Yueao Xing（单位未公开）
- **来源:** [arXiv 2611.31873](https://arxiv.org/abs/2611.31873) · [PDF](https://arxiv.org/pdf/2611.31873) · 提交日期 2026-11-24

**问题背景:** SWE 任务需要理解仓库结构/依赖/运行时行为，高质量训练与评估数据构造难。

**方法论:** RepoEviAgent：从 8,477 个仓库、约 2.48M PR 入口构建质量分级样本；沙盒化多智能体流水线做环境构建、执行验证、仓库探索与证据驱动问答合成。

**核心创新:** 构造 RepoEviQA（334 个任务 × 5 种编程语言），严格分级规则评估；在 5 个 frontier 模型上评估。

**实验结果:** 摭示不同任务类别/编程语言间性能差异（摘要称）。

#### 2611.31868 — CALVIN-MAX: When Does a Mid-Execution Change Hurt a Robot Policy?（CALVIN-MAX：中途改变对机器人策略的影响）

- **作者:** Sajjad Pakdamansavoji（单位未公开）
- **来源:** [arXiv 2611.31868](https://arxiv.org/abs/2611.31868) · [PDF](https://arxiv.org/pdf/2611.31868) · 提交日期 2026-11-24

**问题背景:** CALVIN 的 5 指令链受工程变化（对象/相机/机器人/指令），且此前结果难以分离世界变化、时机与后续影响。

**方法论:** 构造 7,828 个对照分组（同步三条轨迹：无变化/变化/变化到跟路中），10 个政策 × 1,526 条离组内假设检验。

**核心创新:** 用精定的提前判断来把“世界变化的损害”与“中途跟进的代价”区分开。

**实验结果:** 10 个政策在 8 种变化上后失败率 4.4–9.9 pp；一视同仁的假设成立，离此前还有 3/10 政策通过。

---

> **注:** 本报告按“会议论文”与“其他研究主题论文”两大部分组织；各会议条目包含中英文标题、作者与单位、会议链接、问题背景、方法论、核心创新、先前方法对比、实验结果与 arXiv 链接（指标/结果按论文自报）。
