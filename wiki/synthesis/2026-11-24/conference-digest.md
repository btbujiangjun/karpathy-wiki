---
title: arXiv 会议论文摘要 2026-11-24
type: synthesis
created: 2026-11-24
updated: 2026-11-24
sources: [2611.27253, 2611.26900, 2611.23704, 2611.15538, 2611.05979, 2610.39162, 2611.10906, 2611.10228, 2611.02253, 2611.27050, 2611.20608, 2611.13641, 2611.25404, 2611.23678, 2611.14493, 2611.23887, 2611.22506, 2611.20625, 2611.18930, 2610.17767, 2609.32684, 2610.33749, 2609.26347, 2609.07965, 2611.14236, 2610.37231, 2610.33078, 2610.36010, 2610.15427, 2608.15400, 2601.11954, 2603.21024, 2512.09260, 2611.13972, 2511.14865, 2510.22865, 2611.28671, 2611.28669, 2611.28650, 2611.28611, 2611.28604, 2611.28418, 2611.28447, 2611.28194, 2611.28572, 2611.28502, 2611.28501, 2611.28368, 2611.28202, 2611.27741, 2611.28613, 2611.28584, 2611.26875, 2611.28642, 2611.28483, 2611.28654, 2611.28628, 2611.28623, 2611.28603, 2611.28579, 2611.28488, 2611.28522, 2611.28499]
tags: [arxiv, conference, icml-2026, aaai-2026, neurips-2025, iclr-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025, llm, recommendation, advertising, ctr, games, code-execution, agents, generative, sequential, benchmarks]
---

# arXiv 会议论文摘要 (Conference Digest) — 2026-11-24

> **数据来源:** 本报告通过 arXiv API (`https://export.arxiv.org/api/query`) 检索,检索日期为 2026-11-24。
>
> - **会议论文:** 取对应会议名出现在论文 `comments` 或 `journal_ref` 中的论文,每会议按提交日期倒序取前 3 篇。
> - **主题论文:** 从 `cs.LG / cs.AI / cs.CL / cs.CV / cs.IR / cs.MA / cs.GT / cs.SE / cs.MM` 类别的最新论文中按关键词筛选,每主题按提交日期倒序取前 3 篇。
> - **单位说明:** arXiv API 与 abs 页面元数据未包含作者单位,本报告中所有单位均标注为"未公开";如需确认可查看论文原文摘要页或 PDF。
> - 每个条目包含: 标题(中英文)、作者、单位、会议/类别、arXiv 链接、摘要、核心创新、与先前方法对比、实验结果。
> - 共 36 篇会议论文 + 28 篇主题论文 = 64 篇。

---

## 第一部分: 会议论文 (Conference Papers)

### 1. ICML 2026

#### 2611.27253 — Proactive Defense Benchmark against Deepfake Generation（深度伪造生成主动防御基准）

- **作者:** Joonhyuk Baek; Wonjune Seo; Jae-yun Kim; Saerom Park; Hoki Kim（单位：未公开）
- **会议:** ICML 2026 · [arXiv 2611.27253](https://arxiv.org/abs/2611.27253) · [PDF](https://arxiv.org/pdf/2611.27253) · 提交日期 2026-11-20

**摘要:** 尽管主动防御对抗深度伪造的出现普及了,但缺乏统一的评估协议阻碍了公平比较并掩盖了关键漏洞。本文首次提出第一个全面的基准,系统评估扰动、鲁棒性与可迁移性(像素、感知、身份三类指标);分析发现保真度与身份指标捕捉了相互正交的表现轴(各自单独使用时常导致解释冲突),并识别出一个基本权衡:峰值白盒性能可能意味着过拟合;为此引入校准评估以修正生成器引起的身份偏差,为开发真正可泛化的防御提供严格的标准。

**核心创新:** 首个统一的深度伪造主动防御基准; 覆盖像素/感知/身份三类指标,暴露扰动与鲁棒性的盲点。

**先前方法对比:** 摘要未详细对比先前方法,强调本基准是首个、旨在统一评估。

**实验结果:** 摘要未给出具体数字(见论文实验设置与校准策略)。

#### 2611.26900 — Modeling Attributional Style at Scale: A Dataset and Analysis for Psychological Attribution Assessment and Reframing（规模化建模归因风格:心理学归因评估与重构的数据集与分析）

- **作者:** Qiang Zhou; Hanzhen Zhu; Pan Wang; Rui Tu; Huaizhi Qu; Zhuoran Wang; Xin Hu; Lei Li; Tianlong Chen; Jingtong Hu（单位：未公开）
- **会议:** ICML 2026 · [arXiv 2611.26900](https://arxiv.org/abs/2611.26900) · [PDF](https://arxiv.org/pdf/2611.26900) · 提交日期 2026-11-19

**摘要:** 按照重构的学习无助性理论,反复接触不可控的负面事件可能导致抑郁的归因性格式,增加抑郁的易感性。计算研究受限于缺少大规模数据集与鲁棒协议。本文引入 ASTD(Attributional Style Transfer Dataset)和评估指标,首个大规模可评估模型、评估并重构归因解释的基准;采用 Prevent-Filter-Validate 流水线(LLM 生成 + 专家校验)构建,含 42,000 条真实事件与 7 种归因风格;通过流监督分类器与零/少样本 LLM 实现可扩展评估;提出自动评估指标量化心理学有效性,用 DPO 微调 LLM 实现归因重构。

**核心创新:** 首个归因风格大规模建模基准 (ASTD,42,000 条事件,7 种风格); 可量化心理学有效性的自动评估指标; DPO 微调策略; 对心理健康干预提供新范式。

**先前方法对比:** 摘要强调缺乏规模化数据集与鲁棒评估协议。

**实验结果:** 摘要称重构质量有显著提升(substantial gains),具体数字未给出。

#### 2611.23704 — Localizing Text Anonymization for Trustworthy AI: Extending RAT-Bench to Malaysian Microdata and PII（面向可信 AI 的文本匿名化定位:将 RAT-Bench 扩展到马来西亚微数据和个人信息）（AI4GOOD Workshop @ ICML 2026）

- **作者:** David Hong Liang Chew; Zexi Yao; Nataša Krčo; Matthieu Meeus; Waqas Khalid Obeidy; Yves-Alexandre de Montjoye（单位：未公开）
- **会议:** ICML 2026 (AI4GOOD Workshop) · [arXiv 2611.23704](https://arxiv.org/abs/2611.23704) · [PDF](https://arxiv.org/pdf/2611.23704) · 提交日期 2026-11-18

**摘要:** 随着基础模型广泛应用于公共服务与职场生产力,敏感的市民/员工/行政文本可能进入 LLM 工作流;研究是否文本匿名化器能泛化到新环境。在马来西亚本地微数据、马来西亚 PII 格式与以马来西亚英语/Bahasa Malaysia 撰写的文化对话中拓展 RAT-Bench。以 NER 和 LLM 匿名化器 + LLM 攻击者测量再识别风险与文本效用:双 LLM 匿名化器在马来英语和巴哈马英语上再识别风险降至 23–29%,BLEU 0.77–0.94。

**核心创新:** 跨文化语言评估马来西亚微数据的匿名化能力; 暴露现有工具的盲点。

**先前方法对比:** 非 LLM 工具存在两种失败模式(保留实用性但再识别风险高;或严重过度匿名化降低实用性)。

**实验结果:** 马来英语与巴哈马英语中 LLM 匿名化器再识别风险 23–29%,文本效用 (BLEU) 0.77–0.94。

### 2. AAAI 2026

#### 2611.15538 — Faithful in Steps: Improving Generalization and Citation in RAG via Query Decomposition（查询分解提升可归因 RAG 的泛化与引用）

- **作者:** Yue Liu; Zhongying Ru; Shimin Di; Jipeng Zhang; Ruiyuan Zhang; Xiaofang Zhou（单位：未公开）
- **会议:** AAAI 2026 · [arXiv 2611.15538](https://arxiv.org/abs/2611.15538) · [PDF](https://arxiv.org/pdf/2611.15538) · 提交日期 2026-11-11

**摘要:** 可归因 RAGQ 生成引用以增强答案的可验证性,但在多跳推理与多模态理解中存在过度引用、实体识别失败与泛化问题。提出 QDRAG 框架,将问题分解为原子子问题以识别隐性实体,并用重排序剪枝消除过度引用;提供零样本方法 QD-C 与 QD-R 作为引导任务;实验在 4 个多模态 QA 基准上验证,显著超越所有基线(包括 Gemini-Pro)。

**核心创新:** 查询分解框架 (QDRAG); 原子子问题识别隐性实体; 重排序去除冗余引用; 在多模态 QA 上超越 Gemini-Pro。

**先前方法对比:** 已存在可归因 RAGQ 在多跳/多模态上退化,而本文提出的 QDRAG 通过分解+重排序改善。

**实验结果:** 与基线在多模态 QA 基准上超越 Gemini-Pro。

#### 2611.05979 — Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation（从人类数据学习以对象为中心的运动先验用于灵巧机械手操作）

- **作者:** Zhengdong Hong; Guofeng Zhang（单位：未公开）
- **会议:** AAAI 2026 (Oral) · [arXiv 2611.05979](https://arxiv.org/abs/2611.05979) · [PDF](https://arxiv.org/pdf/2611.05979) · 提交日期 2026-11-04

**摘要:** 操纵多样物体由高维动力学驱动,利用人类-物体交互 (HOI) 数据集学习手-物未来状态预测作为通用奖励项;实验在仿真与真实世界中优于 SOTA 并具备跨形态兼容性。

**核心创新:** 从 HOI 数据集学习手-物先验; 预测未来手-物状态作为 RL 的通用奖励。

**先前方法对比:** 仅模仿人类示例,本方法学习整体状态预测。

**实验结果:** 仿真与真实任务中成功率与泛化性均优于既有 SOTA。

#### 2610.39162 — A Novel Approach to Evaluating Evaluation Metrics for Multi-Output Structured Prediction（多输出结构化预测评估指标评估的新方法）

- **作者:** Akshay Vyas; Angelo Pimienta; Nicholas Ruozzi（单位：未公开）
- **会议:** AAAI 2026 · [arXiv 2610.39162](https://arxiv.org/abs/2610.39162) · [PDF](https://arxiv.org/pdf/2610.39162) · 提交日期 2026-10-29

**摘要:** 多输出结构化预测中只有唯一真实标签,而多个同样有效的输出,可靠评估具有挑战性;提出"近似任务特定不变量"作为诊断工具,并通过增强损失激励输出满足这些不变性。实验显示该框架能揭示标准分布式指标的盲点。

**核心创新:** 近似任务特定不变量与增强损失评估框架; 暴露分布式指标的失效模式。

**先前方法对比:** 传统指标对同等有效输出不敏感。

**实验结果:** 增强损失显著提升分布式指标(摘要未给具体数字)。

### 3. NeurIPS 2025

#### 2611.10906 — SCorPion: A Strategic, Controllable and Personified Conversational Companion（SCorPion:具有策略、可控性与人格化的会话陪伴模型）

- **作者:** Luo Ji; Xiyuan Chen; Dan Wang; Qingqing Gu; Teng Chen; Feixiang Guo; Yetao Wu; Jinxian Qu; Yue Zhao; Kun Fan; Ningyuan Xi; Hange Zhou; Zhonglin Jiang; Yong Chen; Hongyan Li（单位：未公开）
- **会议:** NeurIPS 2025 PersonaLLM Workshop · [arXiv 2611.10906](https://arxiv.org/abs/2611.10906) · [PDF](https://arxiv.org/pdf/2611.10906) · 提交日期 2026-11-07

**摘要:** 基于提示词的语言模型在开放域对话中存在问题;从多样语料提取"聊天策略"并以人类原则驱动的样式引导模型;SCorPion 通过 GraphRAG 提取并全局摘要知识图谱、社区摘要策略并按查询定制最优策略,具备策略思考、人格化与可控性。

**核心创新:** GraphRAG 驱动的社区策略提取; 显式人设/风格控制; 策略性思考的陪伴模型。

**先前方法对比:** 基于提示词的方法依赖单一样式,SCorPion 用策略库替代。

**实验结果:** 摘要未给出具体数字。

#### 2611.10228 — FAIR Universe Weak Lensing ML Uncertainty Challenge: Dataset and Cosmological Inference Competition（FAIR Universe 弱引力透镜 ML 不确定性挑战:数据集与宇宙学推理竞赛）

- **作者:** Biwei Dai; Po-Wen Chang; Erwan Allys; Wahid Bhimji; Boris Bolliet; Thomas Borrett; Paolo Calafiura; Ragansu Chakkappai; Yuan-Tang Chou; Noé Dia; Sascha Diefenbacher; Ibrahim Elsharkawy; Steven Farrell; Sacha Guerrini; Isabelle Guyon; Chris Harris; Shih-Chieh Hsu; Wassim Kablan; François Lanusse; Celia Lecat; Julia Linhart; Yuezhou Ma; Benjamin Nachman; Shubhojit Naskar; Andy Nilipour; Laurence Perreault-Levasseur; Sébastien Pierre; Benjamin Remy; David Rousseau; Uroš Seljak; Haonan Shangguan; Sammy Nasser Sharief; Yuanxu Sun; Andreas Tersenov; Ihsan Ullah; Huikun Weng; Licong Xu; Justine Zeghal; Yulei Zhang; Hang Zhou（单位：未公开）
- **会议:** NeurIPS 2025 FAIR Universe Weak Lensing ML Challenge (Phase 1) · [arXiv 2611.10228](https://arxiv.org/abs/2611.10228) · [PDF](https://arxiv.org/pdf/2611.10228) · 提交日期 2026-11-06

**摘要:** 弱引力透镜是强大的宇宙学探针,机器学习可超越传统统计方法提取宇宙学信息,但缺乏标准化基准。本论文作为 NeurIPS 2025 competition,提出对应的数据集与评估研究;数据含多种系统偏差,提供受控测试床。总结优胜方法:条件最优传输数据增强、AI 智能体驱动的参数推理、Ensemble 学习、Vision Transformer 架构、物理信息特征整合。

**核心创新:** 全球弱引力透镜 ML 不确定性挑战/基准资源; 优胜方法:条件最优传输数据增强 + AI 智能体驱动参数推理。

**先前方法对比:** 摘要指出进展受缺乏标准化基准限制(含系统偏差与模拟器瑕疵)。

**实验结果:** 总结基准与优胜方法(详见 Zenodo 数据集链接)。

#### 2611.02253 — Calibration-Constrained Diagnostics for Evaluating LLM Self-Evaluation（校准受约束的诊断:评估 LLM 自评）

- **作者:** Jae Oh Woo; Mengdie Flora Wang; Rahul Ghosh; Baishali Chaudhury; Mun Young Kim（单位：未公开）
- **会议:** NeurIPS 2025 LAW Workshop（扩展版） · [arXiv 2611.02253](https://arxiv.org/abs/2611.02253) · [PDF](https://arxiv.org/pdf/2611.02253) · 提交日期 2026-11-01

**摘要:** 引入可复用的评估工件,用于诊断 LLM 自报置信度是否可支持"置信度阈值或不确定"决策;提供黑盒协议、提示词、裁判标签、模型输出、再现脚本与校准受约束的诊断指标;在 13 个模型与 4 个基准中发现自评置信度在聚合上可能导致部署误导(某强模型聚合校准好但分类级受约束失败)。

**核心创新:** 分类级 PVC/C-PVC 诊断与 VUS 聚合; 基于正余方的体积、正余方限制与 fat-shattering 形式化; 指出需要校准受约束的类别级诊断。

**先前方法对比:** 聚合校准指标 (ECE/Brier) 不捕捉正余方情形下的失败。

**实验结果:** 覆盖 13 个模型,结构化的诊断排名与替代的分类化/裁判标签扰动测试。

### 4. ICLR 2026

#### 2611.27050 — Towards Text-Mask Consistency in Medical Image Segmentation（面向文本掩码一致性的医学图像分割）

- **作者:** Jie Gui; Hang Tu; Wen Sha; Xiuquan Du（单位：未公开）
- **会议:** ICLR 2026 (Poster) · [arXiv 2611.27050](https://arxiv.org/abs/2611.27050) · [PDF](https://arxiv.org/pdf/2611.27050) · 提交日期 2026-11-20

**摘要:** VLM 在医学图像分割中常产生与文本冲突的掩码;源于模板化临床语言导致硬对比学习中大量假负样本,以及缺乏语言主导的空间感知注意力;提出 C2Seg 两阶段方法,包含 Cluster-aware Contrastive Learning 与 Bidirectional Complementary Attention Module、KAN-based Attention Gating。实验在 4 个公开医学成像数据集上提升分割精度。

**核心创新:** C2Seg 双阶段; 软标签的对比学习; 双向互补注意力 + KAN 门控。

**先前方法对比:** 纯视觉模型依赖文本; 引入文本掩码一致性。

**实验结果:** 在四个公开医学成像数据集上提升分割精度(摘要无具体数字)。

#### 2611.20608 — Same Papers, Different Verdicts: Tracing Version Drift in LLM Peer Review（同样的论文,不同裁决:追踪 LLM 同行评审中的版本漂移）

- **作者:** Jizhou Guo（单位：未公开）
- **会议:** ICLR 2026 · [arXiv 2611.20608](https://arxiv.org/abs/2611.20608) · [PDF](https://arxiv.org/pdf/2611.20608) · 提交日期 2026-11-16

**摘要:** 对 OpenAI、Google、Anthropic 等 20 个前沿模型在 ICLR 2027 投稿期间的审稿行为进行审计(前后版本比较):Claude Opus 与 Gemini 之间不接受(accept)比例在 183 个随机投稿上下降了 52 点与 53 点;提示词禁止模型模仿时差 79 点;论文增加 30% 的投稿被拒绝的概率也会下降。实验数据以 ICLR 2027 决定后验证(2026-12-16)。

**核心创新:** 前后版本审稿一致性的百分比变化实验; 揭示 LLM 评审得分随模型版本漂移。

**先前方法对比:** 已有针对退休策略的模型评估,本文关注评审行为的漂移。

**实验结果:** 含 183 次随机投稿的成对比较,Opus/Gemini 差距 52/53 点,禁止提示词差距 79 点。

#### 2611.13641 — MOAI: Module-Optimizing Architecture for non-interactive secure transformer Inference（MOAI:基于非交互式安全 Transformer 推理的模块优化架构）

- **作者:** Linru Zhang; Xiangning Wang; Jun Jie Sim; Zhicong Huang; Jiahao Zhong; Huaxiong Wang; Pu Duan; Kwok-Yan Lam（单位：未公开）
- **会议:** ICLR 2026 · [arXiv 2611.13641](https://arxiv.org/abs/2611.13641) · [PDF](https://arxiv.org/pdf/2611.13641) · 提交日期 2026-11-10

**摘要:** 云服务提供商的 LLM 推理存在隐私问题,同态加密 (HE) 可实现加密输入的安全推理但计算开销大;MOAI 基于列打包与对角打包策略设计高效框架,通过层内格式转换的消除、无旋转的 Softmax/LayerNorm 算法等减少 HE 旋转。实验结果:相比现有改进工作,层矩阵乘法旋转少 ≥1.7×;推理评估时间减少 52.8%(比 THOR,CCS 25 相关的现有方法),在 LLaMA-3-8B 上的平摊时间为单张输入 2.36 分钟。

**核心创新:** 无旋转 HE 注意力架构; 列打包消除矩阵乘法旋转; 交错批处理降低旋转。

**先前方法对比:** 与 THOR 与 Powerformer (Park et al., ACL 25) 对比,时间降低 52.8%/55.7%。

**实验结果:** BERT-base 推理时间减少 52.8%,POWERFORMER 上 55.7%。

### 5. KDD 2026

#### 2611.25404 — Toward a Science of AI Agent Societies（走向 AI 智能体社会的科学）

- **作者:** Geon Lee; Fanchen Bu; Soo Yong Lee; Sunwoo Kim; Kijung Shin（单位：未公开）
- **会议:** KDD 2026 Blue Sky Ideas Track · [arXiv 2611.25404](https://arxiv.org/abs/2611.25404) · [PDF](https://arxiv.org/pdf/2611.25404) · 提交日期 2026-11-19

**摘要:** 提出 AI Agent Societies 的四核心属性(个体化目标、规则与治理、自主性、规模与复杂性)及四类研究方向(经济行为、冲突下的行为、不安全/不道德行为、系统级行为)。

**核心创新:** AI Agent Societies 的规范性框架与研究方向枚举。

**先前方法对比:** 回顾了现有多智能体系统,指出仅覆盖部分属性。

**实验结果:** 理论分析,无实验数据。

#### 2611.23678 — Evaluating Governed LLM-Driven ML Experimentation: Lifecycle, Provenance, and Failure Metrics（评估治理的 LLM 驱动 ML 实验:生命周期、溯源与失败指标）

- **作者:** Dowling Wong（单位：未公开）
- **会议:** KDD 2026 (ETAAI Workshop,非归档) · [arXiv 2611.23678](https://arxiv.org/abs/2611.23678) · [PDF](https://arxiv.org/pdf/2611.23678) · 提交日期 2026-11-18

**摘要:** 提出治理 harness: Control Plane 拥有试验生命周期,检查编辑范围并决定保留或丢弃,写入 append-only ledger;治理指标(invalid-action rate, repeated-bad rate, provenance completeness)。在 6 个 ML 任务上验证(含 1445 次试验);暴露无记忆 arm 全部 120 次试验失败、benchmark 适配器提案用尽与重置失败。

**核心创新:** 实验过程评估的治理范式; 1,445 次试验的可复现溯源指标。

**先前方法对比:** 传统做法只看任务分数; 对照实验:只记录成功试验的 arms 在 43/50 个试验中失去记录。

**实验结果:** 1,445 次试验,暴露任务分数掩盖的失败。

#### 2611.14493 — Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents（企业分析智能体评估框架的比较研究:稳定性、检测与发现）

- **作者:** Howard Zhang; Chuck Arvin; Logan Brown; Mihir Bhatia; Neelu Choudhary; Lily Miao（单位：未公开）
- **会议:** KDD 2026 · [arXiv 2611.14493](https://arxiv.org/abs/2611.14493) · [PDF](https://arxiv.org/pdf/2611.14493) · 提交日期 2026-11-10

**摘要:** 评估 LLM 分析智能体在复杂多工具工作流中的可靠性;比较三种评估框架(trace-based LLM judging, text-only LLM judging + red-teaming, deterministic heuristics)。结果: (1) 可用信息决定评估质量; (2) 功能与安全评估互补; (3) LLM-based 评估发现需要人工审查的微妙错误。推荐双框架策略。

**核心创新:** 三阶段比较研究(稳定性 / 检测 / 发现)。

**先前方法对比:** 对比了三种评估范式,含稳定性 (97%),F1=0.90,5× 更多假警报等数据。

**实验结果:** Phase 1 97% 稳定性阈值; Phase 2 已知风险 F1=0.90; Phase 3 发现 24 个新型失败。

### 6. CVPR 2026

#### 2611.23887 — Can AI Understand Indonesian Children's Book Illustrations? Compliance, Safety, and the Cultural Alignment Gap（AI 能理解印尼儿童绘本插图吗?合规性、安全性与文化对齐差距）

- **作者:** Rian Adam Rajagede; Rochana Prih Hastuti; Fitri Hasanah Amhar（单位：未公开）
- **会议:** CVPR 2026 (CV4CHL Workshop,非贡献赛道) · [arXiv 2611.23887](https://arxiv.org/abs/2611.23887) · [PDF](https://arxiv.org/pdf/2611.23887) · 提交日期 2026-11-18

**摘要:** 研究 VLM 在印尼 Book Leveling Guideline 下能否可靠识别并应用视觉标准(合规性、安全性、文化对齐),用于插图生成/评估;VLM 在合规与安全方面可靠,文化对齐存在盲点,AI 生成插图在结构/安全性上通过但在文化细节上失败。

**核心创新:** 用印尼政府改编的 Book Leveling Guideline 评测 VLM 的合规/安全/文化对齐能力。

**先前方法对比:** 比较真实绘本页与人类基线。

**实验结果:** 结论以合规性/安全性可靠为主(具体数字见论文),文化对齐存在系统性缺失。

#### 2611.22506 — EfficientVPR: Toward Efficient Visual Place Recognition via Scene-Aware Prompt Tuning and Adaptive Feature Enhancement（EfficientVPR:基于场景感知 Prompt Tuning 与自适应特征增强的高效视觉位置识别）

- **作者:** Wenjing Tang; Chuanguang Yang; Zhulin An; Libo Huang; Yongjun Xu（单位：未公开）
- **会议:** CVPR 2026 · [arXiv 2611.22506](https://arxiv.org/abs/2611.22506) · [PDF](https://arxiv.org/pdf/2611.22506) · 提交日期 2026-11-17

**摘要:** 提出 EfficientVPR:轻量单阶段 VPR 框架,通过场景感知视觉提示调优 + 实例依赖的关键局部特征增强模块解决极端环境变化与效率问题;在 Pitts250k, MSLS, Eynsham, AmsterTime 与 SVOX 等基准上,对 DINOv2-small 模型达到 SOTA,R@1 在 2.5% 以内优于 DINOv2-large 两阶段方法,同时 73× speedup、60% 更低维度特征。

**核心创新:** 场景感知视觉 Prompt Tuning; 自适应关键局部特征增强。

**先前方法对比:** 替代双阶段重排序方法,获 73× speedup 与 60% 更低维度。

**实验结果:** 73× speedup,60% lower-dimensional features(摘要数字)。

#### 2611.20625 — ASCG: Adaptive Spatial Classifier Guidance for Surgical Concept Suppression in Diffusion Models（ASCG:用于手术概念抑制的自适应空间分类器引导）

- **作者:** Younghwan Kil; Joonhyeong Park; Giung Nam; Juho Lee（单位：未公开）
- **会议:** CVPR 2026 (SAFE Workshop) · [arXiv 2611.20625](https://arxiv.org/abs/2611.20625) · [PDF](https://arxiv.org/pdf/2611.20625) · 提交日期 2026-11-16

**摘要:** 文本生成图像扩散模型有害内容风险高,现有安全机制基于全局干预;提出 Adaptive Spatial Classifier Guidance (ASCG),用概率监测 + Grad-CAM 局部抑制进行按需激活,平衡安全与语义保真。

**核心创新:** 监测进入抑制的需求; Grad-CAM 局部化抑制。

**先前方法对比:** NudeNet 不捕捉语义完整性,本文用 VLM 评估框架提升安全与保真度。

**实验结果:** 结论以安全与保真度平衡为主(摘要未给具体数字)。

### 7. ACL 2026

#### 2611.18930 — Between Rigor and Reality: How AI Safety Benchmark Developers Understand Benchmark Use and Maintenance（在严谨与现实之间:AI 安全基准开发者如何理解基准的使用与维护）

- **作者:** Megan Li; Ningjing Tang; Christopher Stewart; Hoda Heidari; Hong Shen（单位：未公开）
- **会议:** ACL 2026 (Eval Eval Workshop) · [arXiv 2611.18930](https://arxiv.org/abs/2611.18930) · [PDF](https://arxiv.org/pdf/2611.18930) · 提交日期 2026-11-13

**摘要:** 基于五场访谈(学术界与工业界),发现 AI safety benchmark 开发者的感知与实际适用性存在脱节;指出(1) inter-rater reliability 难度与(2) 外部有效性缺乏明确处理路径。

**核心创新:** 基于访谈的定性研究; 揭示 benchmark 的使用与维护限制。

**先前方法对比:** 摘要中讨论相关工作为硬件度量标准的评估。

**实验结果:** 定性结论(无具体数字)。

#### 2610.17767 — Efficiently Learning To Reason or Not to Reason: Root-token Policy Optimization for Adaptive Thinking（高效学习"是否推理":基于 Root-token 策略优化的自适应思考）

- **作者:** Taehyeon Kim; Hyunsoo Lee; Youngsoo Jang; Moontae Lee（单位：未公开）
- **会议:** ACL 2026 (Oral) · [arXiv 2610.17767](https://arxiv.org/abs/2610.17767) · [PDF](https://arxiv.org/pdf/2610.17767) · 提交日期 2026-10-13

**摘要:** 大型推理模型 (LRM) 性能强但存在过度思考问题;提出 RPO (Root-token Policy Optimization):通过训练根 token(如是否加 <think>)让 LRM 自行决定何时推理,训练成本仅为先前自适应推理方法的 ~2%。在多个模型家族与规模上验证难度感知的自适应思考。

**核心创新:** 通过 Root-token 决策是否推理,大幅降低训练开销。

**先前方法对比:** 传统工具的模型分离; 本文开源 LRMs 自身的自适应机制。

**实验结果:** 摘要说训练成本是先前自适应方法的 ~2%。

#### 2609.32684 — Focusing Condition: Inference-Time Self-Contrastive Steering Elicits Better Conditional Text Embeddings in LLMs（Focusing Condition:推理时自对比引导激发更好的 LLM 条件文本嵌入）

- **作者:** Zifeng Cheng; Lingyun Qian; Zhiwei Jiang; Cong Wang; Yafeng Yin; Fei Shen; Ao Zhou; Qing Gu（单位：未公开）
- **会议:** ACL 2026 (Oral) · [arXiv 2609.32684](https://arxiv.org/abs/2609.32684) · [PDF](https://arxiv.org/pdf/2609.32684) · 提交日期 2026-09-26

**摘要:** 用无需训练/微调的方法提取条件文本嵌入;现有方法依赖提示词,但产生的嵌入与一般文本嵌入纠缠;提出推理时、可插拔的 Self-Contrastive Steering (SCS):构造无条件嵌入并通过干预自注意力模块实现条件文本嵌入的聚焦;实验在聚类、Semantic Textual Similarity 与三元组对齐数据集上提升多种 LLM 的性能。

**核心创新:** 通过掩码 + 位置编码干预自注意力,构造无条件嵌入与完成条件嵌入。

**先前方法对比:** 传统 Prompt-based 方法存在纠缠问题。

**实验结果:** 在聚类/STS/triplet 数据集上显著提升(摘要无具体数字)。

### 8. EMNLP 2025

#### 2610.33749 — Refined Assessment for Translation Evaluation: Rethinking Machine Translation Evaluation in the Era of Human-Level Systems（人机同构系统时代:再审视机器翻译评估）

- **作者:** Dmitry Popov; Vladislav Negodin; Ekaterina Enikeeva; Iana Matrosova; Nikolay Karpachev; Max Ryabinin（单位：未公开）
- **会议:** Findings of EMNLP 2025 · [arXiv 2610.33749](https://arxiv.org/abs/2610.33749) · [PDF](https://arxiv.org/pdf/2610.33749) · 提交日期 2026-10-24

**摘要:** 传统 MQM 与 ESA 的局限:专家一致性、粒度粗糙、语义/流利度权衡、时间限制;本文引入专家标注的 English-Russian WMT24 数据集与 RATE 协议;发现 SOTA MT 系统在准确性上领先人类但在流利度上落后(结论中称 STOA 系统可能在准确性上超越人类翻译)。

**核心创新:** RATE 协议(自定义错误分类、更细粒度的严重度、准确性/流利度多维评分)。

**先前方法对比:** 指出 MQM/ESA 的短板,强调高质量专家标注的重要性。

**实验结果:** 发现 SOTA 系统准确性 > 人类,流利度落后(具体数字见论文)。

#### 2609.26347 — TransBERT: A Framework for Synthetic Translation in Domain-Specific Language Modeling（用合成翻译预训练: TransBERT 框架）

- **作者:** Julien Knafou; Luc Mottin; Anaïs Mottaz; Alexandre Flament; Patrick Ruch（单位：未公开）
- **会议:** Findings of EMNLP 2025 · [arXiv 2609.26347](https://arxiv.org/abs/2609.26347) · [PDF](https://arxiv.org/pdf/2609.26347) · 提交日期 2026-09-22

**摘要:** 专领域(生物科学,法语)高资源翻译方向的需求通过仅用合成翻译预训练解决;发布 TransCorpus 工具包,TransCorpus-bio-fr 语料库(36.4GB)与 TransBERT-bio-fr。

**核心创新:** TransCorpus 数据合成翻译工具; 合成数据实现高资源方向的下游性能。

**先前方法对比:** 传统依赖现有翻译资源。

**实验结果:** 发布 36.4GB 合成资源与模型。

#### 2609.07965 — Rethinking Sign Language Translation: The Impact of Signer Dependence on Model Evaluation（重新审视手语翻译:手语人依赖对模型评估的影响）

- **作者:** Keren Artiaga; Sabyasachi Kamila; Bannon Afli; Conor Lynch; Mohammed Hasanuzzaman（单位：未公开）
- **会议:** Findings of EMNLP 2025 · [arXiv 2609.07965](https://arxiv.org/abs/2609.07965) · [PDF](https://arxiv.org/pdf/2609.07965) · 提交日期 2026-09-07

**摘要:** 手语翻译存在大量手语依赖评估;做 signer-fold 交叉验证;在 PHOENIX14T 上 GFSLT-VLP 的 BLEU-4 从 21.44 降至 3.59(ROUGE-L 42.49→11.89),GASLT/SignCL 类似;指出 CSL-Daily 多个目标句可由多个手语者完成,造成训练/测试数据泄露;建议 signer-independent 评估与显式的手语人无关分割。

**核心创新:** 评估结论:既有评估大幅高估 SLT 能力,建议 signer-independent 协议。

**先前方法对比:** 先前的 signer-dependent 评估; 建议改为 signer-independent。

**实验结果:** 在 PHOENIX14T 上 BLEU-4 21.44→3.59 等(摘要具体数字)。

### 9. SIGIR 2026

#### 2611.14236 — StaRSE: Compact Russian Sentence Embeddings with a Sign-Coded Static Encoder（StaRSE:用符号编码的静态编码器获得紧凑的俄语句子嵌入）

- **作者:** Boris Malashenko; Ivan Jarsky; Egor Soldatov; Vladislav Luzhnov; Sviatoslav Stumpf; Vladislav Shmatkov; Viacheslav Shalamov; Andrey Stankevich; Valeria Efimova（单位：未公开）
- **会议:** ReNeuIR @ SIGIR 2026 · [arXiv 2611.14236](https://arxiv.org/abs/2611.14236) · [PDF](https://arxiv.org/pdf/2611.14236) · 提交日期 2026-11-10

**摘要:** 提出 StaRSE:紧凑的俄语静态句子编码器,用 token 符号位+绝对值表示 + mean pooling;初始化于 ruBERT-base;在 RuMTEB 上任务均值 51.16,比最强的静态基线高 7.98;模型 11.3 MiB,平均 CPU 延迟 0.08 ms/句子(比 Contextual 的 55.7 MiB/1.43 ms 更快)。

**核心创新:** 符号编码的静态编码器; RuMTEB 51.16 + 7.98; 11.3 MiB 与 0.08 ms 延迟。

**先前方法对比:** 对比了 Contextual 编码器,本文静态编码更快、更小且略高一级。

**实验结果:** RuMTEB 任务均值 51.16,模型体积 11.3 MiB,CPU 延迟 0.08 ms。

#### 2610.37231 — TaskBridge: Technical Report for SIGIR 2026 eCommerce Challenge（TaskBridge: SIGIR 2026 电商挑战技术报告）

- **作者:** Zhiheng Fu; Yupeng Hu; Zixu Li; Zhiwei Chen; Qinlei Huang; Shaokun Wang; Han Liu; Fan Liu; Weili Guan; Liqiang Nie（单位：未公开）
- **会议:** eCommerce Challenge @ SIGIR 2026 (首名) · [arXiv 2610.37231](https://arxiv.org/abs/2610.37231) · [PDF](https://arxiv.org/pdf/2610.37231) · 提交日期 2026-10-27

**摘要:** 挑战:将任务意图查询重写为产品检索相关的表达,随后用 BM25 检索;设计 TaskBridge 系统,含 Catalog Semantic Anchoring、Unified Five-Candidate Rewriting 与 Protocol-Aware Selection。实验在首个获胜的标准化解决方案上,多条查询在交互设置中提供额外增益。

**核心创新:** 目录锚定的句子重写,选择形成互补的 5 条查询; 可在 Automatic/Interactive 两种协议下使用。

**先前方法对比:** 挑战前的优势在多查询提供额外增益(摘要总结)。

**实验结果:** 首个获胜。

#### 2610.33078 — Evaluating Visual Language Models on Visual Grounding for Visually Impaired People（评估视觉语言模型在视障人群视觉定位上的表现）

- **作者:** Fairooz Azim; Lydia Achour; Claudia Borg; Lina Rojas-Barahona（单位：未公开）
- **会议:** EvalMG26 @ SIGIR 2026 · [arXiv 2610.33078](https://arxiv.org/abs/2610.33078) · [PDF](https://arxiv.org/pdf/2610.33078) · 提交日期 2026-10-21

**摘要:** 用 VizWiz-VQA-Grounding 评估开源 VLMs 的视觉定位;提出 VG-SHAP 将 explainability 框架用于黑盒评估;结论:VLMs 在视觉定位上存在显著差距(虽推理正确,但未能将其定位到正确区域)。

**核心创新:** 扩展 explainability 框架到黑盒 VLM 的定位评估。

**先前方法对比:** 很多开源 VLM 存在定位不可靠的盲点。

**实验结果:** 结论:正确率高但定位差(摘要未给具体数字)。

### 10. WWW 2026

#### 2610.36010 — CIVER: Causal Intervention Verification for Reliable Code Review（CIVER:基于因果干预的可靠代码审查验证）

- **作者:** Xinyuan Song; Hasibul Haque; Jay Somasundaram; Ryan Turner; Bowen Zhu; Liang Zhao（单位：未公开）
- **会议:** WWW 2026 · [arXiv 2610.36010](https://arxiv.org/abs/2610.36010) · [PDF](https://arxiv.org/pdf/2610.36010) · 提交日期 2026-10-26

**摘要:** 代码审查中存在大量虚假正误;提出 CIVER,通过可能干预生成修复方向,区分真正缺陷与虚报,并通过关节优化识别核心缺陷;实验在 SWE-Review-Bench 上正确识别 77% 真正缺陷,且下游修复任务成功率提升。

**核心创新:** 基于因果干预的代码审查可靠性框架; 在 SWE-Review-Bench 上 77% 缺陷识别率。

**先前方法对比:** 传统审查依赖模型感知; CIVER 通过"稳定在无关变化下"的可靠性。

**实验结果:** 正确识别 77% 的真实缺陷(摘要数字)。

#### 2610.15427 — Riemannian Graph Tokenizer for Structural Knowledge Transfer（黎曼图 Tokenizer:用于结构化知识迁移）

- **作者:** Qimin Zhou; Haibo Liu; Yujie Wang; Li Sun; Chuan Shi（单位：未公开）
- **会议:** WWW 2026 · [arXiv 2610.15427](https://arxiv.org/abs/2610.15427) · [PDF](https://arxiv.org/pdf/2610.15427) · 提交日期 2026-10-11

**摘要:** 提出 RGT(Riemannian Graph Tokenizer):用黎曼几何桥接结构化知识与离散表示,支持跨域结构化知识迁移;包含几何词汇定义(树/环/序列)、黎曼量化与几何对齐解码器;实验在多个图域上显著提升知识迁移可达性。

**核心创新:** 黎曼离散化与几何对齐解码器; 结构化知识迁移。

**先前方法对比:** 传统 tokenizer 针对结构不变性; RGT 通过黎曼几何建立统一的切空间。

**实验结果:** 实验结论以可达性提升为主(摘要有实验描述)。

#### 2608.15400 — Implementation of a Metacognition Framework for Self-Awareness and Self-Regulation in Ensembles of LLMs（LLM 集合的自我感知与自我调节元认知框架实现）

- **作者:** Charles Courchaine; Ricky J. Sethi; Hefei Qiu（单位：未公开）
- **会议:** WWW Companion 2026 (WWW Companion '26) · [arXiv 2608.15400](https://arxiv.org/abs/2608.15400) · [PDF](https://arxiv.org/pdf/2608.15400) · 提交日期 2026-08-15

**摘要:** 首次实现 LLM 集合的元认知框架:MSV(Metacognitive State Vector)包含 5 个维度(情绪反应、正确性评估、经验匹配、冲突信息、问题重要性),用于自我感知与自动 System 1/System 2 切换;提供 PoC 演示(现实法、雷达图)。

**核心创新:** MSV 自我感知与自动切换系统 1/System 2 的双模式架构。

**先前方法对比:** 初步实现(PoC); 展示可构建元认知框架。

**实验结果:** 展示通过不同查询类型触发不同处理模式。

### 11. CIKM 2025

#### 2601.11954 — Data-centric Prompt Tuning for Dynamic Graphs（基于数据中心的动态图 Prompt Tuning）

- **作者:** Yufei Peng; Cheng Yang; Zhengjie Fan; Chuan Shi（单位：未公开）
- **会议:** CIKM 2025 · [arXiv 2601.11954](https://arxiv.org/abs/2601.11954) · [PDF](https://arxiv.org/pdf/2601.11954) · 提交日期 2026-01-17

**摘要:** 提出 DDGPrompt:定义统一的节点表达特征矩阵 + 3 个 prompt 矩阵(时间偏差、边权重、特征掩码),通过输入数据层面的调优实现跨模型/任务的自适应;在 4 个动态图数据集的 few-shot 场景下显著优于传统方法与 prompting 方法(摘要未给数字)。

**核心创新:** 数据中心的输入层面提示调优; 统一节点表达特征矩阵 + 3 类 prompt。

**先前方法对比:** 现有方法强耦合模型架构/预训练任务,本文在数据层面解耦。

**实验结果:** 在 few-shot/冷启动条件下优势显著(摘要无数字)。

#### 2603.21024 — Query, Decompose, Compress: Structured Query Expansion for Efficient Multi-Hop Retrieval（查询分解压缩:多跳检索高效结构化查询扩展）

- **作者:** JungMin Yun; YoungBin Kim（单位：未公开）
- **会议:** CIKM 2025 · [arXiv 2603.21024](https://arxiv.org/abs/2603.21024) · [PDF](https://arxiv.org/pdf/2603.21024) · 提交日期 2026-01-14

**摘要:** 提出 DeCoR (Decompose and Compress for Retrieval):查询分解为显式推理步骤 + 文档压缩提取支持性证据;小模型超大模型基线,在多跳检索中获效率与效果优势(摘要未给数字)。

**核心创新:** 结构化信息细化框架; 用小 LLM 更高效替代大模型。

**先前方法对比:** 强调小模型在复杂检索中可优于大模型基线。

**实验结果:** 发现小模型通过结构化利用推理与总结能力效率更高。

#### 2512.09260 — From Forecast to Action: Uncertainty-Aware UAV Deployment for Ocean Drifter Recovery（从预测到动作:用于海洋浮标恢复的不确定性感知无人机部署）

- **作者:** Jingeun Kim; Yong-Hyuk Kim; Yourim Yoon（单位：未公开）
- **会议:** CIKM 2025 STIntelligence Workshop · [arXiv 2512.09260](https://arxiv.org/abs/2512.09260) · [PDF](https://arxiv.org/pdf/2512.09260) · 提交日期 2025-12-10

**摘要:** 提出海洋搜索的预测-执行框架:LLM 预测浮标轨迹,高斯粒子采样建模空间不确定性;动态适应检测半径并用元启发式优化部署;在韩国沿海实际数据上比随机搜索基线显著更好。

**核心创新:** 浮标轨迹预测与 UAV 部署的端到端整合,恢复机制。

**先前方法对比:** 传统部署方法静态。

**实验结果:** 韩国沿海真实数据实验(摘要无具体数字)。

### 12. RecSys 2025

#### 2611.13972 — Data Quality Challenges in Multimodal Tourism Recommender Systems（多模态旅游推荐的数据质量挑战）

- **作者:** Zehui Wang; Wolfram Höpken; Dietmar Jannach（单位：未公开）
- **会议:** DaQuaMRec Workshop @ RecSys 2025 · [arXiv 2611.13972](https://arxiv.org/abs/2611.13972) · [PDF](https://arxiv.org/pdf/2611.13972) · 提交日期 2026-11-10

**摘要:** 推荐系统越来越多使用多模态数据;但 YELP/Instagram 等数据的质量未充分关注;基于旅游推荐,研究 Yelp 与 Instagram 数据中的假评论、LLM 幻觉内容、模态矛盾与人口统计偏差,并提出未来方向。

**核心创新:** 发现多模态数据质量挑战并提出对策方向。

**先前方法对比:** 重点是定性研究与未来方向。

**实验结果:** 研究类,无实验数据。

#### 2511.14865 — FinTRec: Transformer Based Unified Contextual Ads Targeting and Personalization for Financial Applications（FinTRec:金融应用中基于 Transformer 的统一上下文广告定向与个性化）

- **作者:** Dwipam Katariya; Snehita Varma; Akshat Shreemali; Benjamin Wu; Kalanand Mishra; Pranab Mohanty（单位：未公开）
- **会议:** CARS @ RecSys 2025 · [arXiv 2511.14865](https://arxiv.org/abs/2511.14865) · [PDF](https://arxiv.org/pdf/2511.14865) · 提交日期 2025-11-18

**摘要:** 金融服务领域的递归推荐用 Transformer 因动态与跨产品情形;提出统一框架 FinTRec;实验在历史模拟中优于树模型基准,在实时 A/B 测试相关性中也持续更好(摘要提到 consistently outperforms production-grade tree-based baseline)。

**核心创新:** 统一序列推荐模型,解决产品共享信号与业务目标平衡; 从树模型向 Transformer 转型。

**先前方法对比:** 树模型长期领先(解释性与监管对齐),本文展示 Transformer 在模拟与 A/B 测试中的胜出。

**实验结果:** 历史模拟 + live A/B test correlations(摘要描述持续优于基线)。

#### 2510.22865 — Civic Ground Truth in News Recommenders: A Method for Public Value Scoring（新闻推荐中的公民事实真值:公共价值评分方法）

- **作者:** James Meese; Kyle Herbertson（单位：未公开）
- **会议:** NORMalize 2025 @ RecSys 2025 · [arXiv 2510.22865](https://arxiv.org/abs/2510.22865) · [PDF](https://arxiv.org/pdf/2510.22865) · 提交日期 2025-10-26

**摘要:** 新闻推荐系统研究如何嵌入编辑目标与公共价值;提出通过国家代表性受众评估生成价值标签的方法(公民事实真值)。

**核心创新:** 结构化的公共价值标注方法,面向公民新闻推荐。

**先前方法对比:** 回顾现有方法,关注自上而下的限制。

**实验结果:** 方法类,无实验数据。

---

## 第二部分: 研究主题论文 (Topic Papers)

### 1. LLM / 大语言模型与 AI

#### 2611.28671 — The Evaluation Substrate Matters: Benchmarking Multi-Agent Serving Substrates（子系统很重要:多智能体服务子系统的评估）

- **作者:** Haoyuan Zheng; Dongting Li; Hancheng Ye; Qinsi Wang; Mingyuan Ma; Yuncheng Yao; Yifei Wang; Baijun Zhou; Zishan Shao; Tingjun Chen; Hai Helen Li; Danyang Zhuo; Yiran Chen（单位：未公开）
- **会议:** 未说明(代码/数据集页) · [arXiv 2611.28671](https://arxiv.org/abs/2611.28671) · [PDF](https://arxiv.org/pdf/2611.28671) · 提交日期 2026-11-21

**摘要:** 工作流的速度在不同服务子系统下不稳定;MASSys 基准跨子系统与负载模式评估工作流,记录质量/交付/延迟/成本/资源压力/失败;动机实验显示 Star 在 KV-cache 压力下从第 1 降到第 4,Chain 上升。

**核心创新:** 跨 serving substrate 基准 MASSys; 动机诊断。

**实验结果:** Star 从第 1→第 4(KV-cache 压力下),Chain 第 4→第 1; 长尾/超时在负载增加时出现。

#### 2611.28669 — Physical regime changes expose formula misuse in large language models（物理机制变化揭示 LLM 公式误用）

- **作者:** Maohao Ran; Yanting Zhang; Chendong Ma; Jun Song（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28669](https://arxiv.org/abs/2611.28669) · [PDF](https://arxiv.org/pdf/2611.28669) · 提交日期 2026-11-21

**摘要:** LLMs 用于地球/环境科学计算存在物理机制相关的失效;前沿 LLMs 在 72 种机制中频繁误用公式(准确率降低 13–57%);后训练可改善(Qwen3.5-9B 匹配 DeepSeek V4 Flash 284B),SFT(少量 worked example)+RL 比单项提升 61 个百分点,从老师(含正确公式)+蒸馏从 0% 到 71%。

**核心创新:** 物理机制相关的 LLM 公式误用率统计; 后训练策略改善机制感知。

**实验结果:** 准确率降低 13–57%,RL 达匹配(Qwen3.5-9B 匹配 DeepSeek V4 Flash 284B),SFT+RL 提升 61 个百分点。

#### 2611.28650 — Unlearning Model Identity: Ablating LoRA Weights from Question-Based Identity Tuning（从基于问题的身份调优中去除 LoRA 解体权重）

- **作者:** Ming Cheung（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28650](https://arxiv.org/abs/2611.28650) · [PDF](https://arxiv.org/pdf/2611.28650) · 提交日期 2026-11-21

**摘要:** 模型继承教师模型嵌入的自身身份属性;本方法定位 LoRA 中的身份参数表示并激活去除,保持通用能力;实验显示去除率在 Qwen3.5-2B 完全移除,在 Gemma4-E2B 为 10%,通用任务性能不变。

**核心创新:** 身份特征定位与 LoRA 权重解体; 去除后保持通用能力。

**实验结果:** Qwen3.5-2B 100% 去除,Gemma4-E2B 10%,通用能力不变(摘要数字)。

### 2. 推荐系统 (Recommendation)

#### 2611.28611 — Action-Conditioned Transition Irreversibility for Out-of-Distribution Detection in Reinforcement Learning（基于动作条件的转移不可逆性用于 RL 的 OOD 检测）

- **作者:** Emil Mittag; Richard Dazeley; Peter Vamplew（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28611](https://arxiv.org/abs/2611.28611) · [PDF](https://arxiv.org/pdf/2611.28611) · 提交日期 2026-11-21

**摘要:** 探测 OOD 应该分析动作条件轨迹而非独立样本;提出 ACTI 计算前向/后向转移似然并比较;六个环境×十五个检测器实验;ACTI 取得较好 macro AUROC 并比 PEDM 快约两个数量级。

**核心创新:** 动作条件 + 分步校准的 OOD 检测器; 建议 ACTI-Forward。

**实验结果:** AUROC 领先; 速度快约两个数量级; AUPRC 数据组上 ACTI-Forward 更好(摘要具体数字较少)。

#### 2611.28604 — MADRec: Reliable Multi-Agent Reasoning with Evidence-Grounded Debate for Recommendation（MADRec:证据基于辩论的可靠多智能体推荐）

- **作者:** Zunlong Liu; Weijie Feng; Jingzhi Li; Lei Zhu; Zhiyong Cheng; Meng Wang（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28604](https://arxiv.org/abs/2611.28604) · [PDF](https://arxiv.org/pdf/2611.28604) · 提交日期 2026-11-21

**摘要:** LLM 将推荐从匹配向推理和可解释决策演进;提出 MADRec 三模块:Interaction Agent & Semantic Agent 辩论;EG-RAR 证据检索增强;JRC 校准排序;三个真实数据集实验优于基线。

**核心创新:** 证据基于辩论框架; 多智能体推荐的可靠性评估。

**实验结果:** 在三个真实数据集上 consistently outperforms competitive baselines(摘要描述)。

#### 2611.28418 — WingBench: Benchmarking How AI Agents Search for Better Designs（WingBench:测评 AI 智能体如何搜索更好的设计）

- **作者:** Yiming Yang; David Xia; Jisen Li; Yuqing Jian; Yunjia Yang; Koray Aydin; Zhaoran Wang（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28418](https://arxiv.org/abs/2611.28418) · [PDF](https://arxiv.org/pdf/2611.28418) · 提交日期 2026-11-20

**摘要:** 设计搜索使用廉价预测选择候选,但测试失败,尤其是优化偏好的异常设计;提出 WingBench 多保真基准,优化者与 AI 智能体设计护翼;数据/代码/提示词发布。

**核心创新:** 多保真优化中测试失败的困难; 6,629 次 CFD 记录。

**实验结果:** 分数取决于方法,差异数据; 优化器在反馈下改善,差异进化在保真度较低。

### 3. 广告 (Advertising)

#### 2611.28447 — Reimbursement as a Revenue Instrument in Costly Clock Auctions（在昂贵的钟形拍卖中,参与者成本节省的需求纳(即价格倡导)之地域性影响与可预测性规律与搏弈策略最优选择的变化）

- **作者:** Miriam Nelson; Jack Stanick; Edwin Lock; Francisco Marmolejo-Cossío（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28447](https://arxiv.org/abs/2611.28447) · [PDF](https://arxiv.org/pdf/2611.28447) · 提交日期 2026-11-21

**摘要:** 钟形拍卖中参与者可能在继续购买时产生成本;提出卖家通过允许参与者反映成本的拍卖来增加净收入;用线性规划找最䁙的支付策略;两标例子等。

**核心创新:** 成本补偿策略时机的线性规划分析; 双标对比。

**实验结果:** 关于补偿策略的条件分析(见摘要理论)。

#### 2611.28194 — HEP-Ex-Bench: Evaluating Agentic Performance in High Energy Physics Experiment Data Analyses with Sealed Worlds（用密封世界评估高能物理实验数据分析中智能体的表现）

- **作者:** Andrzej Novák; Yiyang Zhao; Dolores Garcia; Eric A. Moreno; Jeffrey Krupa; Víctor Bresó-Pla; Samuel Bright-Thonney; Lukas Heinrich; Michael Kagan; Philip Harris（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28194](https://arxiv.org/abs/2611.28194) · [PDF](https://arxiv.org/pdf/2611.28194) · 提交日期 2026-11-20

**摘要:** 基于密封世界的智能体分析基准,代理在公开数据上开发分析,在程序生成的私密数据集上评估,注入信号并变化模拟设置;结果:Gemini 4 Argon 60% 数据(4 个任务),GPT 6 Astra 38%,Claude Opus 5.5 31%。

**核心创新:** "Sealed Worlds"评估方法; 智能体表现排名(摘要给出得分)。

**实验结果:** Gemini 4 Argon 60%,GPT 6 Astra 38%,Claude Opus 5.5 31%(摘要数字)。

### 4. CTR (点击率预估)

#### 2611.28572 — Complex band-limited maximum likelihood: estimating the wave behind detected quanta（检测到的粒子背后的波的复带限极大似然估计）

- **作者:** Rahul Agarwal; Ankit Agarwal（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28572](https://arxiv.org/abs/2611.28572) · [PDF](https://arxiv.org/pdf/2611.28572) · 提交日期 2026-11-21

**摘要:** 物理中的量子带限 ML(complex BLML);估计模板构造;阵列到轴映射;实验在留出粒子上与 kernel estimators 等比较;在数据集、透镜问题上复现(特定波特征)。

**核心创新:** 物理前景的局限性方法(摘要含体现)。

**实验结果:** 发现留出粒子上 BLML 更好(摘要有结果描述)。

#### 2611.28502 — Shoonya: Zero-Socket In-Process Small Language Models for Graph Databases with Schema-Epoch KV Caching, Live Catalog Logit Masking, and Verifier-Advantage Distillation（Shoonya:面向图数据库的零 socket 内进程小语言模型）

- **作者:** Madhulatha Mandarapu; Sandeep Kunkunuru（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28502](https://arxiv.org/abs/2611.28502) · [PDF](https://arxiv.org/pdf/2611.28502) · 提交日期 2026-11-21

**摘要:** 面向图数据库的小语言模型(16.8M–1.07B),零 dependency;使用基于代码式'对用户问题确认模型身份'的 LoRA 去除。摘要数据:schema-epoch KV caching, live catalog logit masking 等。

**核心创新:** 三种技术的代码模式。

**实验结果:** 实现覆盖率 100%,错误率 0.0%(摘要数字)。

#### 2611.28501 — An equivariant classical density functional for ionic fluids at complex interfaces（具有同构性的经典阻密度函数在复杂界面的离子流体中的应用）

- **作者:** Bingqing Cheng（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28501](https://arxiv.org/abs/2611.28501) · [PDF](https://arxiv.org/pdf/2611.28501) · 提交日期 2026-11-21

**摘要:** 在复杂界面周围的离子流体中预测离子排列与长程电场;结果在分子动力学中复现(摘要描述,非具体数字)。

**核心创新:** 重构框架:分子动力学结果在代码(BEMFormer)下改进。

**实验结果:** 结论偏向性,稀疏矩阵加速(摘要未给具体数字)。

### 5. 游戏 (Games)

#### 2611.28368 — Schedule, Rank, Profile: Continuous Evaluation of LLM Agents in Games（LLM 智能体在游戏中的连续评估:调度、排名与画像）

- **作者:** Martyna Plomecka; Yao Yan; DJ Sterling; Jon Lipovetz; John Schultz; Michael Aaron; Chiamaka Chukwuka; Will Cukierski; Christopher D'Mello; Bovard Doerschuk-Tiberi; Robert Fraser; Ian Gemp; Yuting Han; Addison Howard; Oran Kelly; Siqi Liu; Jeff Moser; Meghan O'Connell; Jun Peng; Laurel Prince; Meg Risdal; Jonathan Ward; Domino Weir; Marc Lanctot（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28368](https://arxiv.org/abs/2611.28368) · [PDF](https://arxiv.org/pdf/2611.28368) · 提交日期 2026-11-20

**摘要:** 现有的一次性游戏基准会过时;提出自适应调度+ ULB 排名模型+ 游戏画像框架;调度节省 61.7% episodes,其中团队游戏被记录四次;基于类的帕累托前沿(模型性能 vs 推理成本)。

**核心创新:** 自适应调度 (scheduler saves 61.7% episodes),Unified Leaderboard, 游戏画像。

**实验结果:** 调度节省 61.7% episodes;其他 8 games 61.9%。

#### 2611.28202 — AutoPILOT: A Visual Agent Harness for Real-Time Gameplay（AutoPILOT:面向实时游戏的视觉智能体结构）

- **作者:** Mark Zhao; Pengcheng Wang; Rui Yang; Jiarui Yao; Xirui Jiang; Yuxi Chen; Bingxuan Li; Hanyang Chen; Ke Yang; Manling Li; Tong Zhang; Huan Zhang（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28202](https://arxiv.org/abs/2611.28202) · [PDF](https://arxiv.org/pdf/2611.28202) · 提交日期 2026-11-20

**摘要:** 改变第三方调用频率(模型不等于游戏速度);AutoPILOT 每次模型调用允许原语动作/宏/闭环控制器;AFK-Bench 浏览器游戏基准;GPT-6.1 Sol: 68.6% real-time vs 38.3%,GameWorld 80.0% vs 42.9%,达到同样的最终成功率只用 1/5 API 成本。

**核心创新:** 模型输出转为动作的时间远边(第三方调用频率); AFK-Bench 120 游戏。

**实验结果:** 68.6% vs 38.3%,80.0% vs 42.9%,1/5 成本达同样最终成功率(摘要数字)。

#### 2611.27741 — Can Vision-Language Models Synthesize Executable Game-Playing Programs?（AI 是否能合成可执行的游戏玩法程序?）

- **作者:** Yao Tong; Jiaxin Qi; Dingyu Zhang; Jianqiang Huang（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.27741](https://arxiv.org/abs/2611.27741) · [PDF](https://arxiv.org/pdf/2611.27741) · 提交日期 2026-11-20

**摘要:** VLM 无法提供适应性,四阶段(Explore、Perception、API Construction、Strategy Composition)解耦合成;实验在 16 games/4 genres 发现 VLM 在程序合成上存在差距。

**核心创新:** 用于 VLM 游戏玩法的脚本程序基准; 四阶段可靠控制器合成流水线。

**实验结果:** 暴露强 VLM 在程序合成上的短板(摘要描述)。

### 6. 代码执行预测 (Code Execution)

#### 2611.28613 — Internalized Experience: How Training Data Shapes Memory Formation in LLMs（如何训练数据塑造 LLM 中的记忆形成）

- **作者:** Xianxuan Long; Xinnan Dai; Kai Guo; Jiliang Tang（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28613](https://arxiv.org/abs/2611.28613) · [PDF](https://arxiv.org/pdf/2611.28613) · 提交日期 2026-11-21

**摘要:** FSMem 框架:训练数据如何影响 parametric memory 中可复用规则的学习;探索不同训练深度与数据组织的影响;累积语料优于长轨迹。

**核心创新:** FSMem (Finite-State Machine Memory) 与训练数据塑造记忆的学习模式。

**实验结果:** 各训练条件下,用大规模长轨迹数据改善规则学习(摘要总结)。

#### 2611.28584 — Right Verdict, Right Reason? An Execution-Grounded Study of Whether LLM Vulnerability Detectors Understand Vulnerabilities（LLM 漏洞检测器推理正确性(执行落地)研究）

- **作者:** Leizhen Zhang; Sheng Chen（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28584](https://arxiv.org/abs/2611.28584) · [PDF](https://arxiv.org/pdf/2611.28584) · 提交日期 2026-11-21

**摘要:** 用 515 个 BigVul/PrimeVul 函数(含 PoC)执行落地:检查 LLM 编织出 bug 的行号并测试删除证据后的 verdict;4 findings(商业模型定位强于 keyword rule,删除证据后新漏洞优势下降等);发布 framework 与 post-cutoff 漏洞基准。

**核心创新:** 执行基准的 5 层增值梯; 商业模型的反常下降发现。

**实验结果:** 515 函数,发现前/漏洞分类等具体数字(摘要仅结构描述)。

#### 2611.26875 — How Long Will My Language Model Run? A Benchmark for Pre-Execution Runtime Prediction（LLM 会运行多久?预执行运行时间预测基准）

- **作者:** Ashish Molakalapalli; Kangda Wei; Haonan Duan; Alex Carter; Ruihong Huang（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.26875](https://arxiv.org/abs/2611.26875) · [PDF](https://arxiv.org/pdf/2611.26875) · 提交日期 2026-11-19

**摘要:** PreRun 基准:801 training + 1,884 inference records;OpenAI/Claude 等模型与回归;Claude 的零样本 MAE 是 RF 的 4.5 倍;5 个标注 example 显著降错。

**核心创新:** 面向预执行运行时的 benchmark。

**实验结果:** PreRun: 801/1,884 记录,3 个模型对比。

### 7. 智能体系统 (Agents)

#### 2611.28671 — The Evaluation Substrate Matters: Benchmarking Multi-Agent Serving Substrates（子系统很重要:多智能体服务子系统的评估）

- **作者:** Haoyuan Zheng; Dongting Li; Hancheng Ye; Qinsi Wang; Mingyuan Ma; Yuncheng Yao; Yifei Wang; Baijun Zhou; Zishan Shao; Tingjun Chen; Hai Helen Li; Danyang Zhuo; Yiran Chen（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28671](https://arxiv.org/abs/2611.28671) · [PDF](https://arxiv.org/pdf/2611.28671) · 提交日期 2026-11-21

> 本条目与 LLM 类别中同篇论文重复(MASSys 同时被两个关键词命中),因此在本节仅保留一份概要。见上文"1. LLM"。

#### 2611.28642 — Aegis: A Conversational Prototype for Lung Cancer Risk Information and Follow-up（Aegis:肺癌风险信息对话原型）

- **作者:** Bowen Han; Chengwei Cao; Runxin Zhang; Yuyang Jiang（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28642](https://arxiv.org/abs/2611.28642) · [PDF](https://arxiv.org/pdf/2611.28642) · 提交日期 2026-11-21

**摘要:** 浏览器原型结合会话问卷、规则风险分类、可下载报告、RAG 健康信息与医生沟通;多智能体设计分离信息收集、验证、评估与报告。

**核心创新:** 结构化规则报告 + Firebase 链接; 可验证范围 45 条功能测试。

**实验结果:** 定性原型演示,无临床定量数据(摘要明确说明)。

#### 2611.28483 — Don't Train It, Write It: An AI Agent Writes New Capabilities into Language Model Weights（AI 智能体直接写入能力权重,无需训练）

- **作者:** Santiago Rivadeneira Quintero（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28483](https://arxiv.org/abs/2611.28483) · [PDF](https://arxiv.org/pdf/2611.28483) · 提交日期 2026-11-21

**摘要:** AI 智能体在预训练模型中添加门控注意力头与 MLP neurons(无需反向传播、无需 fit weights),预算 50 个模型 passes,无需验证/测试;实验:Qwen2.5-1.5B BBH 19.95→41.05,Gemma-3-1B 10.25→32.86;next-token 分布在 1,023,000 WikiText tokens 上 KL=0;同布局 LEADERBOARD 其他测试结果不变。

**核心创新:** 开放环的权重写入; 四种组合 BBH 分数提升; KL 守恒结果。

**实验结果:** Qwen2.5-1.5B:19.95→41.05,Gemma-3-1B:10.25→32.86,循环上限等(摘要数字)。

### 8. 生成模型 (Generative Models)

#### 2611.28654 — Stein Guidance without Gradients: Discretization Uniform Diffusion Inference Time Scaling beyond Particle SMC（Stein 引导的无梯度方法: 离散化 + 统一扩散推理时间缩放）

- **作者:** Youheng Zhu; Chenyang Wang; Minshuo Chen; Yiping Lu（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28654](https://arxiv.org/abs/2611.28654) · [PDF](https://arxiv.org/pdf/2611.28654) · 提交日期 2026-11-21

**摘要:** 奖励引导扩散的训练样本;提出 Stein Guidance 结合 derivative-free + Metropolis-Hastings 纠正,2 个 query/step;证明 superpolynomial decay 的有限网格 TV 误差。

**核心创新:** 值加权选择的推理时 Stein 引导; MH 纠正。

**实验结果:** 理论证明,无具体实验数字(摘要)。

#### 2611.28628 — Nearly Minimax-Optimal Sample Complexity of Natural Policy Gradient with a Matching Information-Theoretic Lower Bound（自然策略梯度的近极值可实现采样复杂度+信息论下界）

- **作者:** Asha Barua; Sajad Khodadadian（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28628](https://arxiv.org/abs/2611.28628) · [PDF](https://arxiv.org/pdf/2611.28628) · 提交日期 2026-11-21

**摘要:** 研究 NPG 的采样复杂度:获得多种批大小/步长策略的 O(SAH^4/ε²) 上界,并与 Ω(SAH^4/ε²) 下界匹配;已知 kernel 时 exact NPG 下界 Ω(H²/ε)。

**核心创新:** NPG 直接策略空间优化可达信息论极限。

**实验结果:** 采样复杂度 O(SAH^4/ε²)(摘要公式)。

#### 2611.28623 — Neural Schrödinger Bridge via Yasue Action with Applications to Generative Modeling（用 Yasue 动作构建神经薛定谔桥的生成建模应用）

- **作者:** Yan-Han Chen; Abhishek Halder; Hailiang Liu（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28623](https://arxiv.org/abs/2611.28623) · [PDF](https://arxiv.org/pdf/2611.28623) · 提交日期 2026-11-21

**摘要:** 提出神经薛定谔桥的新 solver,使用 Yasue 动作的 saddle point 形式,学习 ODE 速度而非 SDE 漂移;实验验证在低/高维、真实与合成数据。

**核心创新:** 通过Yasue action 实现桥的学习。

**实验结果:** 定性/定量分数提升(摘要无具体数字)。

### 9. 序列建模 (Sequential Modeling)

#### 2611.28603 — Bridging Teacher-Student Capability Gaps with Recurrent Computation（用递归计算弥合教师-学生能力差距）

- **作者:** Zeyi Huang; Jiuxiang Gu; Eli Shechtman; Yong Jae Lee; Zongze Wu（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28603](https://arxiv.org/abs/2611.28603) · [PDF](https://arxiv.org/pdf/2611.28603) · 提交日期 2026-11-21

**摘要:** 模型蒸馏中教师缩放时学生性能出现饱和/负反转;假设是学生容量不足;提出 loop/recurrent computation 修改计算图增强有效容量;在事后微调( mathematical post-training)中缩放优于 looped/vanilla。

**核心创新:** 使用递归计算提升学生容量; 教师-学生能力差异更小。

**实验结果:** 理论+实验安排(摘要含实验结论描述)。

#### 2611.28579 — Tight Mistake-Abstention Tradeoffs for Sequential Prediction under Adversarial Injections（对抗注入下序列预测的严格拒绝-错误权衡）

- **作者:** Moïse Blanchard; Ezra Edelman; Surbhi Goel; Shyam Narayanan; Jialin Yu（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28579](https://arxiv.org/abs/2611.28579) · [PDF](https://arxiv.org/pdf/2611.28579) · 提交日期 2026-11-21

**摘要:** 研究对抗注入下序列预测的拒绝-错误权衡(有限 VC dimension, oblivious adversary);提出 weighted shattering potential 与成对变体,闭合 Gap:已知可达 O(d log T),未知可达紧界;扩展到信息削弱。

**核心创新:** weighted shattering potential 与闭合的权衡界; 实验上 O(√(dT)) 均衡率。

**实验结果:** 理论分析(公式与界),无实验数据。

#### 2611.28488 — AMP-OD: Active Model Probing for Unsupervised Outlier Model Selection--Extended Version（AMP-OD:无监督异常值模型选择的主动模型探测（扩展版））

- **作者:** Hong-Phuc Phan; Tuan-Anh Vu; Tung Kieu; Son Ha Xuan; Sean Bin Yang; Bin Yang; Christian S. Jensen（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28488](https://arxiv.org/abs/2611.28488) · [PDF](https://arxiv.org/pdf/2611.28488) · 提交日期 2026-11-21

**摘要:** 自适应探测框架,利用小规模探针的得分设计证据进行 final selection;引入 LOO-FPP 将探针得分转换为 detector-family evidence;通过历史可靠性做 warm-start prior 等;实验表明探针提供有用证据。

**核心创新:** 基于探针的无监督模型选择, LOO-FPP。

**实验结果:** 摘要描述实验结论(无具体数字)。

### 10. 基准测试 (Benchmarks)

#### 2611.28671 — The Evaluation Substrate Matters: Benchmarking Multi-Agent Serving Substrates（子系统很重要:多智能体服务子系统的评估）

> 与 LLM 主题重复,见上文概要。

#### 2611.28522 — DisSparse: Pipelined Top-$p$ Sparse Attention for Long-Context LLM Serving（DisSparse:用于长上下文 LLM 服务的管道式 Top-$p$ 稀疏注意力）

- **作者:** Nurlan Nazaraliyev; Elaheh Sadredini; Nael Abu-Ghazaleh（单位：未公开）
- **会议:** NeurIPS 2026 · [arXiv 2611.28522](https://arxiv.org/abs/2611.28522) · [PDF](https://arxiv.org/pdf/2611.28522) · 提交日期 2026-11-21

**摘要:** 长上下文推理受 KV cache 主导的内存瓶颈;提出 DisSparse,集成 top-$p$ 稀疏注意力到 vLLM;两级管道隐藏选择延迟,通过直方图 kernel 优化选择;实验:1.17x–1.80x 加速。

**核心创新:** DisSparse 在 vLLM 内集成 top-$p$; 两级管道与直方图 kernel。

**实验结果:** 1.17x–1.80x 加速(摘要数字),8x 更大 batch size。

#### 2611.28499 — Accelerating wave-scattering simulations with learned search directions（用学习搜索方向加速波散射模拟）

- **作者:** Haoran Sun; Tao Shan; Hongyu Zhou; Rui Guo; Shenheng Xu; Fan Yang; Maokun Li（单位：未公开）
- **会议:** 未说明 · [arXiv 2611.28499](https://arxiv.org/abs/2611.28499) · [PDF](https://arxiv.org/pdf/2611.28499) · 提交日期 2026-11-21

**摘要:** BEMFormer:对一个积分方程学习生成搜索方向(提供几何相关方向),兼容粗网格修正;推广到新几何/网格/激励;在双喇叭上达到毫米形式雷达截面,1.04M unknowns 上每个系统求解快 30× 对比预处理 Krylov。

**核心创新:** 学习搜索方向替代从零构建。

**实验结果:** 毫米形式雷达截面约 1 dB(摘要数字),快 30×。
