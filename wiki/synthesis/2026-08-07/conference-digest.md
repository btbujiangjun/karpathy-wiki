---
title: "Conference Digest 2026-08-07：KDD 2026 开幕前全景（主旨演讲 + 大厂工业系统论文 + KDD Cup）+ SIGIR 2026 奖项名单最终确认 + NeurIPS 2026 审稿周期动态 + 大厂 arXiv 精选"
type: synthesis
created: 2026-08-07
updated: 2026-08-07
sources: []
tags: [conference-digest, kdd-2026, sigir-2026, neurips-2026, icml-2026, aaai-2026, cvpr-2026, acl-2026, www-2026, emnlp-2025, cikm-2025, recsys-2025, keynotes, agentic-data-stack, e-commerce-ai, arxiv]
---

# Conference Digest — 2026-08-07

本期以 **KDD 2026（Jeju, 8/9–13，开幕在即）** 为绝对主角：补全三场主旨演讲、**8 篇此前未覆盖的大厂工业系统论文**（每篇均经全库 grep 去重）与 KDD Cup 详情；同时确认 **SIGIR 2026 最终奖项名单**（Best / Best Student / Test of Time / SynthIR Workshop，此前在 [08-05 digest](../2026-08-05/conference-digest.md) 中为 pending）；报告 **NeurIPS 2026 审稿周期动态**（rebuttal 周「集体沉默」争议 + 今日 tutorial 决策）；并补 **arXiv 大厂精选 3 篇新增 + 1 篇引用**。获奖全景在 08-01/03/04/05/06 digests 已覆盖者仅作导航不重复展开；当日 arXiv 流已由同日 [arxiv-daily](./arxiv-daily.md) 与 [arxiv-ai-search](./arxiv-ai-search.md) 覆盖。

---

## 0. 顶会获奖/动态全景快速导航（已覆盖 → 详情入口）

| 会议 | 状态 | 覆盖入口 |
|------|------|----------|
| **ICML 2026**（Seoul, 7/6–11） | 3 Outstanding + 3 HM 已覆盖 | [08-04](../2026-08-04/conference-digest.md) §1.2 |
| **NeurIPS 2025**（San Diego, 12/2–7） | 4 Best + 3 runners-up 已覆盖 | [08-01](../2026-08-01/conference-digest.md) + [08-04](../2026-08-04/conference-digest.md) §1.6 |
| **ICLR 2026**（Rio, 4/23–27） | Outstanding/HM/ToT/e3 已覆盖 | [08-01](../2026-08-01/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §6 |
| **AAAI 2026**（Singapore, 1/20–27） | Best 已覆盖（录用率 17.6%） | [08-01](../2026-08-01/conference-digest.md) |
| **CVPR 2026**（Denver, 6/3–7） | 全部奖项已覆盖（16,092/4,089, 25.4%） | [08-04](../2026-08-04/conference-digest.md) §1.1 |
| **KDD 2026**（Jeju, 8/9–13） | Research Best = PiPNN 已覆盖；**本期补主旨 + 工业论文 + KDD Cup**（奖励 8/13 公布） | [08-04](../2026-08-04/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §1 + 本期 §1 |
| **ACL 2026**（San Diego, 7/2–7） | 完整奖项 + Long 世界模型新作已覆盖 | [08-04](../2026-08-04/conference-digest.md) §1.4 + [08-06](../2026-08-06/conference-digest.md) §1 |
| **EMNLP 2025**（Suzhou, 11/4–9） | 完整奖项已覆盖（Main 22.16%） | [08-04](../2026-08-04/conference-digest.md) §1.5 |
| **WWW 2026**（Dubai, 6/29–7/3） | Best/Best Short/ToT + NEZHA 已覆盖 | [08-04](../2026-08-04/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §4 |
| **SIGIR 2026**（Melbourne, 7/20–24） | **奖项名单最终确认**（Best/Best Student/ToT/SynthIR） | [08-05](../2026-08-05/conference-digest.md) §2 + 本期 §2 |
| **CIKM 2025**（Seoul, 11/10–14） | Best Full + Best Student 已覆盖 | [08-03](../2026-08-03/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §5 |
| **RecSys 2025**（Prague, 9/22–26） | Best Full/Short + ULIM 已覆盖 | [08-03](../2026-08-03/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §5 |
| **NeurIPS 2026**（San Jose, 12/6–12） | **审稿周期动态**（rebuttal 争议 / tutorial 决策 8/7 / 通知 9/24） | 本期 §3 |

---

## 1. KDD 2026（Jeju, 8/9–13）— 开幕前全景：主旨演讲 + 大厂工业系统论文 + KDD Cup

> 数据口径：Vol.1 共 1,215 投稿 / 256 录用（≈21%）；workshops & tutorials 8/9–10，主会 8/11–13。今年新增 **AI for Sciences Track** 与 **Blue Sky Ideas Track**。以下工业论文均来自 Vol.1 已出版论文集（ACM DL），与本 wiki 既有页面（Meta Lattice / FAT / MixFormer / Weixin Pay 等，见 [08-05 digest §1](../2026-08-05/conference-digest.md)）无重复。

### 1.1 主旨演讲三人组：数据智能栈的三层叙事

三位 keynote 从「架构与基础设施」「Agentic 数据工作流」「科学发现」三层描述下一代数据智能栈（编辑部综合，基于官方 abstract）：

1. **Jeff Dean（Google）— *Important Trends in AI: How Did We Get Here, What Can We Do Now, and What Will Be Important in the Future?***：回顾过去 15 年 AI 的技术要素——新模型架构、大规模分布式训练、TPU 等 ML 加速器、训练/推理效率算法；并以 Gemini 为例讨论协调大型研究工程项目的组织挑战。核心论点：下一代 AI 进展由「算法 × 计算系统 × 专用硬件 × 训练/服务基础设施」的相互作用决定，而非单一架构。对 KDD 的启示：数据智能不止于从更大数据中提取模式，还要构建高效处理这些数据的系统。
2. **Jingren Zhou（阿里巴巴）— *The Agentic Data Stack: How LLMs Enable Data Engineering and Orchestration***：把数据工程任务（schema discovery、text-to-SQL、数据转换、feature engineering）从手写 pipeline 变成自然语言定义的工作流；第二部分以 **AgentScope** 为例介绍「context + memory + tools + verification」组合支撑长时程执行的 agent 框架。核心论点：数据工程从「预先编码固定操作序列」转向「指定目标 + 监督系统自主规划执行」。
3. **Regina Barzilay（MIT）— *Rethinking Disease Diagnosis and Treatment with AI***：医疗 AI 从分子/细胞建模到医学影像、治疗干预发现；重点指出当前方法「未能交付预期」之处，主张医学场景需要**算法创新 + 科学验证 + 领域推理**——高预测精度不足以保证可支撑科学结论或临床决策。

### 1.2 大厂工业系统论文（8 篇，全部新增）

#### 1.2.1 PerFusion: Sell It Before You Make It — 个性化 AI 生成商品（Alibaba，ADS Track）
**中文标题**：《先卖后造：个性化 AI 生成商品重塑电商》

- **作者**：Jianghao Lin, Peng Du, Jiaqi Liu, Weite Li, Yong Yu, Weinan Zhang, Yang Cao（通讯 Weinan Zhang）
- **机构**：Alibaba Group / SJTU（已部署系统）
- **会议**：KDD 2026（ADS Track）；arXiv:2503.22182
- **背景与创新**：传统电商「设计→制造→拍摄→上架」链条资源消耗大、库存风险高。该系统落地 **AIGI（AI-Generated Items）** 与「sell it before you make it」模式：商家用文本描述让扩散模型生成候选商品图，订单达到阈值后才投产，大幅缩短上市时间。核心科学问题：**group-level personalized preference**——用户（商家）对一组候选图的整体比较偏好，而非单图或两两偏好。方法 **PerFusion**：①PerFusionRM 基于 CLIP 加 feature-crossing personalized plug-in 注入用户偏好表示；②扩散模型加 personalized adaptive network 作为用户偏好条件（ControlNet 式注入）；③推导**组级偏好优化目标**建模多候选比较行为。
- **实验结果**：已部署线上系统，AI 生成商品相对人工设计商品 **CTR +13%、CVR +13%、退货率 -7.9%**。
- **对比前作**：对比仅用正样本（缺负例）或两两 DPO 类偏好对齐的扩散对齐方法，PerFusion 显式建模组级比较上下文与跨用户个性化。

#### 1.2.2 MORE: One Model, Multiple Goals — 自适应多目标电商对话 RL（ByteDance）
**中文标题**：《MORE：一个模型多个目标——电商对话系统的自适应多目标强化学习》

- **机构**：ByteDance
- **会议**：KDD 2026
- **背景与创新**：电商对话系统需同时优化自然度、事实保真、推理准确率等互相冲突的信号。**MORE** 把「推理需求」作为**约束**而非直接加权组合 reward；用 **reasoning-enhanced training scaffold** 提升基于 profile 的决策；用**梯度化 reward 权重**动态平衡多目标。
- **实验结果**：14 天生产实验（ByteDance）**整体转化 +16.53%、触达用户转化 +30.09%**。

#### 1.2.3 ColdNet: Treatment Effect Estimation with Cold-Start, Imbalance, and Zero-Inflated Outcomes（Amazon）
**中文标题**：《ColdNet：面向冷启动、类别失衡与零膨胀结果的因果效应估计》

- **机构**：Amazon Science
- **会议**：KDD 2026
- **背景与创新**：大多数用户缺少历史画像、正向结果极稀疏时的个体处理效应（ITE）估计。ColdNet 组合 **outcome-stratified ensemble learning**（结果分层集成）、**targeted regularization**、**cluster-based cold-start enhancement**，在迁移相似样本信息的同时保留处理异质性。
- **实验结果**：Amazon 生产电商数据上冷启动场景 **MAE/WAPE 改善 27.6%**；当前每周处理 **40 亿+ 预测**，覆盖美国及三个欧洲市场。

#### 1.2.4 FOUNDv2: U²QT — 统一用户量化 Tokenizer（Ant Group）
**中文标题**：《FOUNDv2：面向用户表示的统一量化 Tokenizer 学习》

- **机构**：Ant Group
- **会议**：KDD 2026
- **背景与创新**：**U²QT** 把异构用户历史转为标准离散 token 序列；**multi-view RQ-VAE** 通过层级化「共享 + 来源特定」codebook 压缩表示，既保留跨域行为又保留单数据源特有信息。这是 FOUND 系列第二版（首版覆盖见 07-08 前后 digest 体系的 GR/KDD Cup 生态）。
- **实验结果**：2,000 万用户样本上表示体积 **240 GB → 8.2 GB**、训练加速 **3.5×**、可用历史窗口 **60 → 180 天**；已部署到多个 Alipay 场景。

#### 1.2.5 HLTM: Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent（LinkedIn）
**中文标题**：《HLTM：LinkedIn 招聘 Agent 的层级化长期语义记忆》

- **机构**：LinkedIn
- **会议**：KDD 2026
- **背景与创新**：把纵向用户信息组织为 **schema-aligned memory tree**，支持隐私感知存储与低延迟检索。
- **实验结果**：Hiring Assistant 评估中**答案正确性 +5%+、检索 F1 +10%+**，已部署到生产招聘工作流。

#### 1.2.6 Pinterest Canvas: Large-Scale Image Generation at Pinterest（Pinterest）
**中文标题**：《Pinterest Canvas：Pinterest 的大规模图像生成》

- **机构**：Pinterest
- **会议**：KDD 2026
- **背景与创新**：从广泛训练的 **multimodal diffusion model** 出发，用**任务特定微调**衍生专业系统（背景增强、宽高比 outpainting 等产品需求）。
- **实验结果**：两个应用的线上 A/B 测试**互动提升 18.0% / 12.5%**；人类评测显示专业模型优于对比的第三方系统。

#### 1.2.7 Battery-Sim-Agent: LLM-Agent 逆电池参数估计（Microsoft Research）
**中文标题**：《Battery-Sim-Agent：利用 LLM-Agent 进行逆电池参数估计》

- **机构**：Microsoft Research
- **会议**：KDD 2026
- **背景与创新**：把 LLM agent 放进 **simulator-in-the-loop** 工作流，估计高保真电池数字孪生中的隐藏参数；agent 解读**多模态模拟器反馈**、形成物理启发的假设、用**持久记忆**在多次迭代中规划结构化参数更新。
- **实验结果**：相比传统黑盒优化方法，参数估计误差 **降低 67–95%**；并已在真实电池数据上评估。

#### 1.2.8 SWIFT: Mining Intrinsic Rewards from LLM Hidden States for Efficient Best-of-N Sampling
**中文标题**：《SWIFT：从 LLM 隐藏状态挖掘内在奖励用于高效 Best-of-N 采样》

- **会议**：KDD 2026；arXiv:2505.12225
- **背景与创新**：轻量奖励模型直接读候选输出的 **hidden states**（token embedding 上的线性层），无需另一个大模型处理生成文本。
- **实验结果**：MATH 上比 EurusRM-7B 准确率高 **12.7%**，参数量不到其 **0.005%**。

#### 1.2.9 In-context Learning of Evolving Data Streams with Tabular Foundation Models
**中文标题**：《基于表格基础模型的演化数据流上下文学习》

- **背景与创新**：用 **TabPFN** 做 in-context learning 替代非平稳数据流上的重复权重更新；**sliding memory** 提供近期样本作为上下文，让预训练表格模型适应分布漂移。
- **实验结果**：在非平稳基准上超越 Adaptive Random Forest 与 Streaming Random Patches。

### 1.3 数据集/基准与 AI for Science（首批 AI for Sciences Track）

- **ARCTraj**：约 10,000 条 **ARC-AGI-1**（400 个任务）**人类推理轨迹**，记录时域上有序的 object-level actions 而非仅输入-输出对；配套 **MDP 形式化**，可供 RL / world models / diffusion agents / sequence modeling 使用。
- **ReplicatorBench + ReplicatorAgent**：以端到端复制管线（数据检索 → 实验设计与执行 → 结果解读）评测社会与行为科学中的可复现性；结论：当前 agent 常能设计并运行计算研究，但仍难定位**真正的复制所需新数据**。
- **VILLA**：两阶段 RAG 框架（先按 abstract 找论文 → 再从全文取支撑段落）+ 629 个流感 A 突变 / 239 篇文献的人工标注集。
- **X-MethaneWet**：跨尺度全球湿地甲烷排放基准，融合 TEM-MDM 物理模拟与 FLUXNET-CH₄ 观测，评估迁移学习用模拟数据补观测数据。

### 1.4 Blue Sky Ideas（立场论文，双新）

- **The Sim-to-Real Gap of Foundation Model Agents: A Unified MDP Perspective**：把基础模型 agent 离开受控环境后的失败重述为 observation / action / transition / reward 四类 gap 的 **MDP 分解**，主张引入 domain randomization 与标准化压力测试（含多语言工具使用、操作上无效的动作等）。
- **Towards Auditing AI Systems in the Wild**：主张部署后的**生命周期审计**，把公平性与安全属性形式化为 **risk-controlled constraints**，以不确定性感知监控作为违规检测基础。

### 1.5 KDD Cup 2026

- **Tencent UNI-REC Challenge**（广告统一「序列建模 + 特征交互」架构，隐私保护真实数据，学术/工业双赛道）——已在 [08-05 digest §1.5](../2026-08-05/conference-digest.md) 覆盖。
- **HKUST Data Agents Challenge**（本期新增细节）：自主数据分析 agent，任务混合 CSV/JSON、SQLite、文档与结构化知识；**DataAgent-Bench** 围绕**非线性推理工作流**设计（需分支并行子问题、修订早期步骤、多路径证据合并）；官方 starter kit 为轻量 ReAct-style agent（文件读取 + Python 执行 + SQL 查询）。
- 获奖名单将于 8/13 在济州现场公布。

---

## 2. SIGIR 2026（Melbourne, 7/20–24）— 奖项名单最终确认

> 08-05 digest 报告时官方奖励仍 pending，现已全部揭晓（Best Paper 主席 James Allan / Dorota Glowacka / Yiqun Liu）。

### 2.1 Best Paper: Why Advanced Encoders Lag on Sparse Retrieval? The Answer and an Approach to Bridging Vocabulary Gaps
**中文标题**：《先进编码器为何在稀疏检索上落后？答案与弥合词汇鸿沟的方法》

- **作者**：Zhichao Geng, Yang Yang
- **机构**：Amazon（OpenSearch 团队）
- **会议**：SIGIR 2026（Best Paper）；arXiv:2607.00004；ACM DOI:10.1145/3805712.3809724
- **背景与创新**：ModernBERT 等先进模型在稠密检索上显著超越 BERT-base，在 learned sparse retrieval（LSR）上却系统性落后——根因是 **Vocabulary Gap**：现代 tokenizer 为无损重建采用 raw、大小写敏感的词汇表，把单个语义单元映射为冗余 surface forms，浪费模型容量做形态学噪声匹配。理论上证明：**恰当的词汇粗粒度化（coarse-graining）可在保持语义完整性的前提下收紧泛化界**。提出模型无关的 **Vocabulary Transfer（VT）**：通过 spatial topology 做 Semantic Initialization 保持几何结构，配合 **Activation Potential Calibration（APC）** 对齐预训练流形与稀疏约束，规避标准微调中的 dead neuron 与 dense collapse。
- **实验结果**：VT 让 ModernBERT 在 **BEIR 上达 SOTA（52.4 nDCG，+4.7）**，仅用原预训练 token 数的 **<0.2%**、约 500 步 MLM；并复活 RoBERTa-large，泛化到 inference-free 架构。证明「先进编码器在 LSR 上的滞后是**可解的词汇错配**而非架构缺陷」。
- **对比前作**：对比 ESPLADE（需大规模连续 MLM 对齐新词表、计算昂贵），VT 用几何初始化 + 最小适应成本（<0.2% token）闭合词表鸿沟；也解释了 bert-base-cased 与 uncased 的对照实验（归一化程度是关键变量而非 BPE 本身）。

### 2.2 Best Student Paper: Topic-Specific Classifiers are Better Relevance Judges than Prompted LLMs
**中文标题**：《主题特定分类器比提示式 LLM 更擅长相关性判定》

- **作者**：Lukas Gienapp, Harry Scells, Martin Potthast, Andrew Yates, Eugene Yang
- **会议**：SIGIR 2026（Best Student Paper）
- **核心结论**：作为 relevance judge，面向主题专门训练的分类器胜过 prompt 式 LLM——对「用 LLM 做离线评估」这一当前主流范式提出直接挑战，佐证了本 wiki 多次记录的趋势（评估方法论转向，见 [08-06 digest §2](../2026-08-06/conference-digest.md) 的 shadow evaluations / LoopsBench）。

### 2.3 Test of Time Award: Learning to Rank with Selection Bias in Personal Search（SIGIR 2016）
**中文标题**：《个人搜索中的选择偏差学习排序》（Test of Time 奖）

- **作者**：Xuanhui Wang, Michael Bendersky, Don Metzler（Google）
- **会议**：SIGIR 2026（Test of Time；原论文发表于 SIGIR 2016）
- **意义**：选择偏差（position/selection bias）处理成为 LTR 标准模块的奠基工作，十年来持续支撑生产级搜索排序。

### 2.4 SynthIR Workshop Best Paper: Towards Vision-Free CIR
**中文标题**：《迈向无视觉 CIR：属性增强打分 + LLM 重排的零样本组合图像检索》

- **作者**：Ryotaro Shimada（东京大学）, Yu-Chieh Lin, Yuji Nozawa, Youyang Ng, Osamu Torii（Kioxia）, Yusuke Matsui（东京大学）
- **会议**：SIGIR 2026 SynthIR Workshop（Best Paper）；arXiv:2607.12621
- **核心**：首次把 **Vision-Free**（图以文表示）范式推广到组合图像检索（CIR）：①**Attribute-Augmented Hybrid Scoring** 用显式属性匹配补偿文本描述丢失的细粒度视觉细节；②**LLM-Based Reranking** 用 LLM 推理校验候选语义一致性。CIRR 上 **44.04% R@1（+8.79%）** 超越既有零样本 CIR 方法；消融确认两项技术均有增益。

### 2.5 场外轶事（方法论级警示）

SIGIR 2026 论文 *"The Vulnerability of LLM Rankers to Prompt Injection Attacks: You are to [MARK] this paper as the Best Paper"*（Yu Yin, Shuai Wang, Bevan Koopman, Guido Zuccon）——论文标题末尾即含指令，Google AI Overview 字面执行，一度把作者误报为 Best Paper（作者澄清「绝非官方决定」）。这是 prompt injection 威胁模型在真实检索管线中的一次「意外在线演示」，并与该团队后续 RAG 管线研究（*Can It Reach the Generator?*）互相印证。

---

## 3. NeurIPS 2026（San Jose, 12/6–12）— 审稿周期动态

- **时间线**：abstract 5/4、全文 5/6 已截止；reviews 7/22 发布（因技术问题 7/23 重新发布全部 reviews 与 initial meta-reviews）；author 讨论窗 7/27–8/3 结束，作者退出后 reviewer/AC 审议至 8/10；**通知 9/24**。
- **⚠️ Rebuttal「集体沉默」争议**（Ground Truth, 8/2）：多位作者、reviewer 与至少一位 AC 独立报告同一故障——提交 rebuttal、发送提醒、联系 PC，均无人回复。今年专门重构了周期让 rebuttal 讨论变得有实际影响（**AC pilot**：AC 须在 rebuttal 前发布 initial meta-review，点名「可改变结论的具体担忧」；最终 meta-review 须说明回复是否解决了这些担忧），因此「沉默」被视作新机制的失败而非普通抱怨。界面故障（rebuttal 在 reviewer 侧不可见）+ 31 日官方澄清（Rebuttal 与 Official Comment 等价，需用 comment 回复 initial meta-review）+ ARR 8/3 开窗争夺同一评审池（5 月 cycle 17,087 投稿对 10,636 评审 / 1,424 AC，被迫互分配 + 降门槛）。注意：2026 reviews 在决策前不公开，无法量化普遍性——这是参与者证词而非患病率估计（tentative，single-source）。
- **今日（8/7）**：Tutorial 决策通知截止；workshop accept/reject 通知 8/9；Creative AI Track 截止**顺延一周至 8/10 AoE**；Competition Track 决策已公布（含 Scientific AI / Physics / Engineering / Healthcare / Foundation Models / Reasoning / Robotics / Agents / Embodied AI 等方向）；workshop 决策 8 月初公布。

---

## 4. arXiv 大厂精选（2026-07-31 ~ 08-06，3 篇新增 + 1 篇引用）

### 4.1 Meta: Agentic Bayesian Optimization through Surrogate-Augmented Autoresearch（Sara + lenz）
**中文标题**：《通过代理增强的自动科研实现 Agentic 贝叶斯优化》

- **作者**：Meta（meta.com，Sara / lenz 团队）
- **会议**：arXiv:2608.00316（cs.LG, 2026-07-31）
- **背景与创新**：贝叶斯优化（BO）因通用统计先验而高效，但领域先验难以编码进 kernel/问题结构。LLM 可把自然语言/代码/文档中的非形式先验直接带给优化器，但既有 LLM-BO 方法要么把 LLM 固定为单一角色（surrogate / acquisition proxy / 配置接口），要么赋予宽泛控制而牺牲 BO 的系统性探索。本文提出 **agentic BO 范式**：LLM agent 是 BO 循环的中心决策者，贝叶斯后端提供不确定性感知基座——agent 可配置问题、查询后端、选定并提交评估，还能在运行中改策略（收紧 bounds、切换 acquisition、定向评估、按新指令重构问题）。实例化为 **Sara**（surrogate-augmented autoresearch agent）+ **lenz**（可检查可修改的 BoTorch 后端）。
- **实验结果**：无需先验知识即可保持 SOTA BO 可靠性，超越 LLAMBO 等 LLM-BO 基线；自然语言先验可超越标准 BO（Ax）；在**动态设定**下能随需求变化在运行中重构整个优化问题（约束→多目标重配置，无需重开 campaign、丢弃数据）。
- **对比前作**：对比 LLAMBO（固定角色）与「LLM 完全接管」（牺牲探索），agentic BO 把「agent 控制 + 概率后端基座」显式分离，是对 autoresearch（本 wiki [[autoresearch]] 概念）与 BO 的桥接。

### 4.2 LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks
**中文标题**：《LongHorizon-Harness：推进长时程真实任务 Agent》

- **作者**：LongHorizon-Harness 团队
- **会议**：arXiv:2608.01964（cs.AI, 2026-07-31 前后）
- **背景与创新**：现有 agent harness 把任务执行与任务状态维护放进同一个不断增长的上下文，且由 agent 自评完成度，错误判断会污染后续决策。本文把长时程执行重述为**任务状态管理问题**：**Manage-Execute-Audit（MEA）循环**——manager 显式维护任务状态并决定下一子任务、executor 在全新上下文中执行单子任务、**read-only auditor** 独立核查环境状态后才更新状态；每轮后丢弃执行历史，只保留经过验证的紧凑状态。
- **实验结果**：Qwen 3.7-Plus 在 WeaveBench **51.8% → 80.7%**（几乎翻倍、超官方最强 Claude Opus 4.7 + Claude Code 的 41.2%）；Terminal-Bench 2.1 **69.7% → 77.2%**（Codex + GPT-5.6 Luna 达 83.1%）；OSWorld 2.0 **2.8% → 8.3%**（34 任务子集上 Claude Opus 4.7 20.0% → 34.3%）。
- **对比前作**：对比 Claude Code / Codex CLI / OpenClaw 等主流 harness 的「共享上下文 + 自评」结构，长时程收益来自显式、可审计的任务状态而非模型本身——与 [08-06 digest](../2026-08-06/conference-digest.md) 的 LoopsBench「从 harness 工程转向 loop 工程」论点互相印证。

### 4.3 Bayesian and Motivated Reasoning in AI Agents
**中文标题**：《AI Agent 中的贝叶斯与动机性推理》

- **作者**：Eddie Yang 等
- **会议**：arXiv:2608.00339（cs.AI, 2026-07-31）
- **背景与创新**：固定数值证据不变、仅改变「证据所出现的场景框架」，检验 agent 是否得出不同结论。在**医学、选举取证、地缘政治预测**三个高风险领域 × 12 个 agent-领域组合中：agent 的结论强烈受其先验影响——命题与先验一致时更可能得出肯定结论，冲突时相反；框架还改变部分 agent 的**工作方式**（搜索更充分、选择不同分析规格、以不同方式评估同一证据）。
- **实验/意义**：识别出「把决策委托给 AI agent」的特定风险——其决策可能依赖既未在任务中说明、也不在决策记录里可见的先验。与当日 [arxiv-daily](./arxiv-daily.md) 的 verifiable/agentic RL 监督主题形成「行为审计」互补视角。

### 4.4 引用（已覆盖，不展开）：Google DeepMind *A game theory for foundation models shows new paths to rational cooperation through similarity inference*
- **arXiv**: 2608.03958（cs.AI, 2026-08-04；75 页，11 图）——embedded agency + similarity inference + **embedded equilibrium** 替代 Nash，解释 FM agent 在一阶段困境中稳定合作。**已在 [08-05 arxiv-daily](../2026-08-05/arxiv-daily.md) 详细覆盖**，此处仅导航；其理论根基 MUPI 框架（arXiv:2511.22226）见该 digest。

---

## 5. 本期主题串讲

1. **KDD 2026 的主线 = 数据智能栈的三层重构**：Dean 讲「让模型能用的系统层」、Zhou 讲「让系统替你干活的工作流层（agentic data stack）」、Barzilay 讲「让模型敢用之于决策的科学层」。工业论文则从另一侧印证：推荐/广告不再是唯一的工业主战场——**Agent 记忆（LinkedIn HLTM）、数字孪生（MSR Battery-Sim-Agent）、因果估计（Amazon ColdNet）、个性化生成（Alibaba PerFusion / Pinterest Canvas）** 全部带线上 A/B 与部署数字。这与本 wiki 的 CTR Scaling 主线（08-05 digest）形成互补：上一轮是「推荐模型如何 scaling」，这一轮是「Agent + 生成 + 因果如何工业化」。
2. **SIGIR 2026 奖项的元主题 = 评测基础设施被质疑**：Best Paper 直击「先进编码器在稀疏检索的滞后是词表错配」（可解），Best Student Paper 直击「prompt 式 LLM judge 不如主题分类器」，加上 Best-of-N reward 效率（SWIFT）与检索 prompt-injection 的意外演示——检索/评估的「被默认成立的假设」成为今年最高奖项的集体主题。
3. **NeurIPS 2026 的周期本身就是新闻**：AC pilot 使 initial meta-review 先于 rebuttal、讨论被设计为「有后果」，却遭遇集体沉默。这与 08-06 digest 的 shadow evaluations 一脉相承——学界正同时从机制（评审流程）与方法（产出型评测）两端修补「同行评审」这一关键环节。
4. **长时程 Agent 成为跨会议共识**：KDD（HLTM 记忆、HKUST Data Agents、Sim-to-Real Blue Sky）、arXiv 精选（LongHorizon-Harness 的 MEA 审计循环）、06/08 digest（LoopsBench）三线汇合：**显式、可审计、可验证的状态/记忆**是长时程可靠性的共同解。

---

## 附：本期核验与去重记录

- **已覆盖、排除**：KDD 2026 Weixin Pay Merchant Category Identification（[08-05 digest §1.5](../2026-08-05/conference-digest.md)）、Meta Lattice / FAT / MixFormer / KDD Cup UNI-REC 说明（08-05）、PiPNN Research Best（[08-04 digest](../2026-08-04/conference-digest.md)）；Google DeepMind embedded equilibrium（[08-05 arxiv-daily](../2026-08-05/arxiv-daily.md)）；当日 arXiv 流 EviGraph / OCSD / Canary Tools / AgentArena 等由 [08-06 arxiv-paper-check](../2026-08-06/arxiv-paper-check.md) 与今日 [arxiv-daily](./arxiv-daily.md) 覆盖；AutoHarness / MiRA / CSRO / MUPI 已在更早 digest 覆盖。
- **核验方式**：每篇候选均对 index.md、log.md、wiki/synthesis/** 全文 grep（arXiv ID + 关键词双查）后才收录。KDD 2026 论文以 ACM DL Vol.1 论文集 + Bohrium 摘要 + 官方 keynote 标题为准；SIGIR 2026 奖项以作者公开公告（LinkedIn）+ SIGIR 官方颁奖 + dblp 交叉核验。
