---
title: "Conference Digest 2026-08-13：KDD 2026 落幕颁奖全景（XGBoost Test-of-Time / EARTH Honourable Mention / Wei Wang Innovation Award / Jeff Dean 等 keynote）+ KDD 2026 论文挖掘（Alibaba CVR 多归因 / 流式 Listwise CTR / Tencent 确定性广告分配）+ 大厂 arXiv 精选（Simulator Collapse / Mechanist / 临床 RAG）"
type: synthesis
created: 2026-08-13
updated: 2026-08-13
sources: []
tags: [conference-digest, kdd-2026, recsys-2026, icml-2026, arxiv, multi-agent-rl, interpretability, clinical-ai, ctr, cvr, advertising, recommendation]
---

# Conference Digest — 2026-08-13

本期为 **KDD 2026（Jeju, 8/9–13）闭幕/收尾版**：报告**颁奖全景**——**Test of Time = XGBoost**（Tianqi Chen & Carlos Guestrin）、**Best Research Paper Honourable Mention = EARTH**（HKBU Jianliang Xu 团队，top-3/2,000+）、**SIGKDD Innovation Award = Wei Wang**（UCLA，⚠️修正早期 digest 的 Haixun Wang 口径），主 Best Paper / Best Student Paper 至本期仍未官方确认（caveat 标注）；补 **Jeff Dean / Jingren Zhou / Regina Barzilay 三位 keynote** 全景；按 **Paper Digest 500 条 KDD 2026 库**挖掘 **3 篇工业论文**（Alibaba **MAC/MoAE** CVR 多归因 benchmark + Mixture-of-Asymmetric-Experts、**DLL** 流式兼容 Listwise CTR、Tencent **确定性分配匿名联合广告**）；并新增 **3 篇 arXiv 大厂/重点实验室论文**（Stanford/DeepMind **Simulator Collapse** 多智能体模拟器坍缩、NUS/ZJU **Mechanist** 机制发现 agent、**VITA** 语料特异临床 RAG 对比前沿 LLM）。当日 arXiv 流由同日 [arxiv-daily](./arxiv-daily.md)（37 篇）与 [arxiv-paper-check](./arxiv-paper-check.md)（17 篇）覆盖，本期三篇独立去重收录。**KDD 开幕前全景见 [08-08 digest](../2026-08-08/conference-digest.md)**，逐会进度导航见 §0。

---

## 0. 顶会获奖/动态全景快速导航（已覆盖 → 详情入口）

| 会议 | 状态 | 覆盖入口 |
|------|------|----------|
| **KDD 2026**（Jeju, 8/9–13） | **已落幕：ToT = XGBoost、HM = EARTH、Innovation = Wei Wang、三位 keynote 确认；主 Best/Student 未确认** | 本期 §1 + [08-08](../2026-08-08/conference-digest.md) §1 + [08-07](../2026-08-07/conference-digest.md) §1 + [08-05](../2026-08-05/conference-digest.md) §1 + [08-04](../2026-08-04/conference-digest.md) |
| **RecSys 2026**（Minneapolis, 9/28–10/2） | 议程前瞻已覆盖（PC=Minmin Chen 等, GC=Konstan/Karypis/Adomavicius） | [08-08 digest](../2026-08-08/conference-digest.md) §3.1 + 本期 §3.1 |
| **ICML 2026**（Seoul, 7/6–11） | 3 Outstanding + 3 HM 已覆盖；A3C ToT 报告 | [08-04](../2026-08-04/conference-digest.md) §1.2 + 本期 §3.2 |
| **NeurIPS 2026** | 三城官宣（Sydney + Atlanta + Paris, 12/6–13）；通知 9/24 | [08-08](../2026-08-08/conference-digest.md) §2 |
| **NeurIPS 2025**（San Diego, 12/2–7） | 4 Best + 3 runners-up 已覆盖 | [08-01](../2026-08-01/conference-digest.md) + [08-04](../2026-08-04/conference-digest.md) §1.6 |
| **ICLR 2026**（Rio, 4/23–27） | Outstanding/HM/ToT/e3 已覆盖 | [08-01](../2026-08-01/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §6 |
| **AAAI 2026**（Singapore, 1/20–27） | Best 已覆盖（录用率 17.6%） | [08-01](../2026-08-01/conference-digest.md) |
| **CVPR 2026**（Denver, 6/3–7） | 全部奖项已覆盖（25.4%） | [08-04](../2026-08-04/conference-digest.md) §1.1 |
| **ACL 2026**（San Diego, 7/2–7） | 完整奖项 + Long 世界模型新作已覆盖 | [08-04](../2026-08-04/conference-digest.md) §1.4 + [08-06](../2026-08-06/conference-digest.md) §1 |
| **EMNLP 2025/2026** | EMNLP 2025 奖项 + EMNLP 2026 accepted 名单上线已覆盖 | [08-04](../2026-08-04/conference-digest.md) §1.5 + [08-08](../2026-08-08/conference-digest.md) §3.3 |
| **WWW 2026**（Dubai, 6/29–7/3） | Best/Best Short/ToT + NEZHA 已覆盖 | [08-04](../2026-08-04/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §4 |
| **SIGIR 2026**（Melbourne, 7/20–24） | 奖项名单最终确认已覆盖 | [08-05](../2026-08-05/conference-digest.md) §2 + [08-07](../2026-08-07/conference-digest.md) §2 |
| **CIKM 2025/2026** | CIKM 2025 奖项 + CIKM 2026 录用论文流（HCGRec 等）已覆盖 | [08-03](../2026-08-03/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §5 + [08-13 arxiv-daily](./arxiv-daily.md) |
| **RecSys 2025**（Prague, 9/22–26） | Best Full/Short + ULIM 已覆盖 | [08-03](../2026-08-03/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §5 |

---

## 1. KDD 2026（Jeju, 8/9–13）— 落幕颁奖全景

> 主会 8/11–13，8/13 闭幕。本期以**闭幕/收尾版**口径汇总全部已确认奖项、keynote 与论文挖掘。⚠️ **主 Best Research Paper 与 Best Student Paper 获奖者名单至本期仍未获官方确认**（kdd.org 奖项页反爬、新闻稿截断），下文仅列已核实项；EARTH 按 HKBU 官方口径记为「top three awards」之一（HM）。

### 1.1 奖项全景（已确认）

- **Test of Time Award：*XGBoost: A Scalable Tree Boosting System***（Tianqi Chen & Carlos Guestrin, **KDD '16**, DOI [10.1145/2939672.2939785](https://dl.acm.org/doi/10.1145/2939672.2939785)）。
  - **数据**：42,397 引用、300,534 下载（ACM DL 口径）。XGBoost 在可扩展性/分布式系统工程上的贡献使其成为表格数据机器学习十年来的事实标准，是 KDD 时间检验奖中最「工业影响力溢出学术界」的例子之一。
  - **意义**：与本期 §1.2 MAC/MoAE、§1.3 DLL 等工业 CTR/CVR 论文形成一条暗线——**树模型时代的标准工具，正被深度模型 + 归因/流式范式迭代**，但 XGBoost 依然活跃在广告/风控生产栈的 baseline 层。
- **Best Research Paper Honourable Mention：*EARTH: Accelerating Spatiotemporal Network K-function-based Analytics***（Jianliang Xu 领衔, HKBU；通讯作者为博士生 **Yun Peng** + 合作者）。
  - **数据**：空间时间网络 K-function 分析（用于空间相关/聚类检测）相比 SOTA **快 26×–19.04×**；官方口径为「**top three awards among 2,000+ submissions**」（来源：HKBU 2026-08-11 新闻）。
  - **意义**：延续 KDD 2026 的**「空间/时序基础设施算法提速」**叙事（与已覆盖的 MSR Battery-Sim-Agent 等构成「加速科学/工程分析」簇），也是香港高校在 KDD 的又一高排位成绩。
- **SIGKDD Innovation Award 2026：Wei Wang**（UCLA 计算机系教授兼系主任）。
  - ⚠️ **口径修正**：早前 digest/检索片段曾将获奖者记为 Haixun Wang，**以 UCLA CS 官方公告为准，为 Wei Wang**（来源：cs.ucla.edu 2026-08-11 公告）。Wei Wang 以数据挖掘/生物信息学/Large-Scale Computing 交叉研究著称，兼具 KDD 2026 SIGKDD General Chair 身份。
- **主 Best Research Paper / Best Student Paper**：**未确认**（kdd.org 奖项页被反爬截断）。后续 digest 在官网可访问后补录。

### 1.2 Keynote 全景（已确认三人）

- **Jeff Dean**（周二 8/11）：*"Important Trends in AI: How Did We Get Here, What Can We Do Now, and What Will Be Important In the Future?"* — 以 Gemini / TPU / 大规模训练经验谈 AI 现状与未来。这是 Jeff Dean 自 8/5 离开 Alphabet 另立 **Discovery Loop**（[08-08 digest §4.6](../2026-08-08/conference-digest.md)）后的公开演讲之一，仍以「大模型 + 系统」技术史视角而非组织视角展开。
- **Jingren Zhou（周靖人, Alibaba CTO）** — 阿里云/通义千问技术路线与「AI 基础设施 + 应用」双轮叙事的官方口径。
- **Regina Barzilay（MIT）** — 延续 [08-07 digest §1.1](../2026-08-07/conference-digest.md) 记录的「高预测精度不足以保证支撑临床决策」警示主题，与本期 §2.3 临床 RAG、[08-08 digest](../2026-08-08/conference-digest.md) §4.1 ResidencyRL 的「医学 AI 可行动增益」主线互证。

### 1.3 KDD Cups 收尾导航（此前已覆盖，仅导航）

- **Tencent UNI-REC Challenge**、**HKUST Data Agents Challenge** 等 KDD Cup 赛况与题目已在 [08-07 digest §1](../2026-08-07/conference-digest.md) 记录；本期不重复。

---

## 2. KDD 2026 论文挖掘（Paper Digest 500 条 KDD 2026 库，DOI 核验）

> 来源：paperdigest.org KDD 2026 论文集抽取（500 条目），DOI 前缀 10.1145/3770855.* / 3770854.*。以下 3 篇经 grep 去重确认无既有 wiki 覆盖（注：**FAT-CTR 已在 [wiki/papers/ctr/fat-ctr-scaling.md](../../papers/ctr/fat-ctr-scaling.md) 覆盖**，此处不重复；其余候选 HCGRec/PRISM/GALLM 等归 [arxiv-daily](./arxiv-daily.md) 的 CIKM 2026 簇）。

### 2.1 Alibaba: MAC — 多归因机制下的 CVR 预测 benchmark + MoAE 架构
**中文标题**：《MAC：多归因机制标签下的 CVR 预测基准与 Mixture-of-Asymmetric-Experts》

- **作者**：Jinqi Wu, Zhangming Chan, Xiang-Rong Sheng, Han Zhu, Jian Xu, Bo Zheng 等 12 人（Alibaba 广告/搜索工程集群 + 学界）
- **出处**：KDD 2026, DOI [10.1145/3770855.3817488](https://doi.org/10.1145/3770855.3817488)
- **创新点**：首次系统化建模**多重归因机制（multiple attribution mechanisms）**下的 CVR 标签生成——同一转化行为可归因到多个前置触点/场景，标签语义高度歧义。给出两条架构原则：①**充分学习 multi-attribution 知识**（不只拟合单一标签）；②**以主任务为中心利用该知识**。据此提出 **Mixture of Asymmetric Experts（MoAE）**，把归因知识学习与主任务（CVR）利用解耦为不对称专家。
- **意义**：CVR 从「点估计」走向「归因歧义显式建模」——与本期 §2.3 Tencent 广告「确定性分配」论文、以及已覆盖的 CTR scaling law 主线（FAT-CTR）共同构成 KDD 2026 工业数据标签层的「**标签质量/归因正确性**」主题。

### 2.2 DLL: Decoupled Listwise Learning — 流式兼容的 Listwise CTR
**中文标题**：《打破 Listwise-Shuffle 困境：面向工业 CTR 的流式兼容 Listwise 框架》

- **作者**：Junlin He, Rui Tang, Liyin Hong（电商/广告推荐集群）
- **出处**：KDD 2026, DOI [10.1145/3770855.3818327](https://doi.org/10.1145/3770855.3818327)
- **创新点**：Listwise 训练需要在 session 级重构样本，但工业流式（streaming）训练要求样本独立可批。本文提出 **Decoupled Listwise Learning（DLL）**：**无需 session batching** 即可重建 session 级监督信号，打破「listwise 需要 shuffle/session 批」与「流式训练不能批 session」的两难。
- **意义**：与 [08-06/08-07 digest](../2026-08-06/conference-digest.md) 覆盖的生成式重排（DEGR、Gryphon-v2）并置可见——**训练时监督结构（listwise/session）正在成为 CTR 工程第二战场**，DLL 是「流式约束下做 listwise」的工业解法。

### 2.3 Tencent: Deterministic-Allocation & Anonymous Joint Advertising
**中文标题**：《电商平台的确定性分配与匿名联合广告》

- **作者**：Zhen Zhang, Qianlong Xie, Qi Qi, Xingxing Wang 等 8 人（Tencent 广告集群）
- **出处**：KDD 2026, DOI [10.1145/3770855.3818370](https://doi.org/10.1145/3770855.3818370)
- **创新点**：证明在所有在线广告场景中，**以往的非确定性（non-deterministic）分配方法都会导致可行解不存在**，即在「取整解（rounded solution）与最优解之间」存在系统性 gap。据此提出**确定性分配（deterministic allocation）** + **匿名联合广告（anonymous joint advertising）**：在保护用户/广告主匿名性的前提下做确定性预算分配。
- **意义**：广告预算分配从「随机化/概率取整」转向「确定性可证明可行」，直接把 gap 问题理论化；与 §2.1 的归因标签歧义、以及 [08-08 digest](../2026-08-08/conference-digest.md) 的「广告经济学」主线（CMI/Geo 等）互证：**KDD 2026 工业广告在「标签、分配、归因」三个数据/决策层做严谨化**。

---

## 3. 2027 议程收尾导航

### 3.1 RecSys 2026（Minneapolis, 9/28–10/2）

- 已覆盖（[08-08 digest §3.1](../2026-08-08/conference-digest.md)）：PC Chairs = **Minmin Chen**（Google DeepMind）、**Bart Goethals**（FLAIR）、**Martijn Willemsen**（Eindhoven）；General Chairs = **Joseph Konstan**（UMN）、**George Karypis**、**Gediminas Adomavicius**。Main Sessions 9/29–10/1。
- 补充线索：同日 [arxiv-paper-check](./arxiv-paper-check.md) 收录 **IToM**（RecSys '26, inverse theory-of-mind 推荐）与 **RecSys Factory**（RecSys '26, 决策点自治平台）——RecSys 2026 学术流已在 arXiv 提前露出，后续 digest 可在 9/28 前持续聚合。

### 3.2 ICML 2026（Seoul, 7/6–11）— 已覆盖，仅导航

- 3 Outstanding + 3 Honourable Mention 已在 [08-04 digest §1.2](../2026-08-04/conference-digest.md) 覆盖；A3C Test-of-Time 报告为已发表论文集引用，不展开。

---

## 4. arXiv 大厂/重点实验室精选（2608.12xxx 收盘批次，全库 grep 去重）

> 收录原则：3 篇新收录论文**全部经 arXiv ID + 标题 grep 核验 0 命中**后才收录；不覆盖同日 [arxiv-daily](./arxiv-daily.md) 的 37 篇与 [arxiv-paper-check](./arxiv-paper-check.md) 的 17 篇。

### 4.1 Stanford/Berkeley/MIT: Simulator Collapse — 多智能体 RL 的「一个冻结模拟器不够」
**中文标题**：《一个冻结的模拟器不够：多智能体 RL 中的模拟器坍缩》

- **作者**：Simon Yu, Nicholas Tomlin, Marwa Abdulhai, Ximing Lu, Sergey Levine, Christopher D. Manning, Weiyan Shi 等 10 人（Stanford + UC Berkeley + MIT + 上海交大）
- **会议**：arXiv:2608.12253（cs.LG/cs.MA, 2026-08-13 批次）
- **背景与创新**：人机交互多智能体 RL 通常用**单个 LLM 模拟用户行为**。本文证明这种单模拟器范式**系统性泛化失败**，并溯源到 **simulator collapse（模拟器坍缩）**：因为模拟器 LLM 本身 mode-collapsed，policy 在训练中过拟合到「利用模拟器主导模式」的窄策略，迁移到未见模拟器与真实用户时表现差。作者将坍缩**形式化**（理论证明），并提出两条互补解：①推理期 **Verbalized Sampling**——从「口头化（verbalized）响应分布」采样以拓宽模拟器行为、缓解 mode collapse；②训练期 **Co-Training**——对**一群可训练模拟器**联合优化 policy，防止过拟合单一模式。
- **意义**：这是「**RL 数据生成层的坍缩诊断**」主题在人机交互/多智能体域的翻版——与 [arxiv-daily](./arxiv-daily.md) 的 OPD 诊断-约束簇（GCPO/PAIR/REOPD）共享同一方法论立场：**训练分布中的单模态偏差必须被显式诊断与校正**；也直接回击 [08-08 digest](../2026-08-08/conference-digest.md) §4.1 ResidencyRL「用模拟器做职业训练」的隐含假设（模拟器本身须可保真）。作者阵容罕见地横跨 Manning（NLP）+ Levine（RL）两系。

### 4.2 NUS/ZJU/Amazon: Mechanist — 把 AI 当作科学仪器做机制发现
**中文标题**：《Mechanist：把 AI 作为科学仪器，自主发现智能的机制》

- **作者**：Mengru Wang, Junfeng Fang, Shuofei Qiao, Linyi Yang, Ningyu Zhang, Tat Seng Chua, Huajun Chen, Julian McAuley 等 25 人（NUS + ZJU + UC San Diego）
- **会议**：arXiv:2608.12036（cs.AI/cs.LG, 2026-08-13 批次）
- **背景与创新**：模型能力增长远快于人类对其机制的理解，而**机制探索仍高度手工**。Mechanist 是一个 **agentic 系统**，把 AI 当作「科学仪器」自主发现机制：①构建 **约 13,000 篇**可解释性聚焦的知识图谱；②整合**覆盖 26 个领域、4,300 万篇**论文的多学科数据库；③精选 **32 种**机制分析/因果干预/验证基础方法库。相比 Claude Code 与既有 AI-scientist 系统，Mechanist 生成**更有价值的机制假设**且实验执行更可靠。
- **三个里程碑发现**：①实验室安全风险——**不安全特质可经由看似安全的数据在模态间迁移**（counterintuitive）；②**信念机制理论**——模型如何表征世界知识、形成信念、推断他人信念、并在预训练中涌现；③把机制洞见转化为**实际干预**——提升跨场景模型表现，并**引导科学基础模型生成带指定性质的 DNA 序列**。
- **意义**：与当日 [arxiv-daily](./arxiv-daily.md) 的机制可解释工作（Orientation-not-magnitude 任务向量因果等）构成「**机制研究从描述走向自主发现**」的收敛信号；「43M 论文库 + 13K 可解释图」的科研基建维度呼应 KDD 2026 的 AI-for-Science 主题与 [08-08 digest](../2026-08-08/conference-digest.md) 的 WeatherNext 叙事。

### 4.3 VITA: 语料特异临床 RAG 在新一线模型上的 HealthBench 表现
**中文标题**：《语料特异的临床 RAG 系统在 HealthBench 上匹配或超越更新的前沿 LLM》

- **作者**：Praveen Reddy, Charuta Mandke, Suvrankar Datta, Shitij Arora, Vishal Singh 等 7 人（临床/医学信息团队）
- **会议**：arXiv:2608.12138（cs.CL/cs.IR, 2026-08-13 批次）
- **背景与创新**：通用 LLM 被报道在医学基准上「追平/超过专用临床 AI」，但这类对比基于**窄系统集合 + 高收入国家开发的基准**。本文评估 **VITA**——为**印度等中低收入（LMIC）环境**打造的语料特异 RAG：从**疾病特异指南、印度抗菌素耐药（AMR）数据、国家处方集约束、资源受限护理方案**的精选语料检索。架构与语料为专有，但**基准、医生撰写的评分 rubric、完整响应与打分输出全部公开**可独立复现。
- **关键结果**：在 HealthBench 4,023 道英文题（基准的 80.5%），GPT-4.1 裁判评分下，VITA **匹配或超越更新的 frontier LLM**——支撑「**专用 RAG + 本地语料在卫生系统现实约束下可与通用大模型竞争**」。
- **⚠️ 去重说明**：**HealthBench benchmark 本身**此前已在 [08-13 tech-report-digest（2026-06-13）](../2026-06-13/tech-report-digest.md) 覆盖（index/log 命中）；**本篇 VITA 论文（arXiv ID 2608.12138）为全新收录**（0 命中），与既往 VitaBench（agent 工具评测）无关。
- **意义**：与 Regina Barzilay keynote（§1.2）、ResidencyRL（[08-08 digest](../2026-08-08/conference-digest.md) §4.1）构成「医学 AI」三角：**模拟训练 / 语言模型能力 / 本地语料落地**，且本文主动开源评测材料，是「可独立复现的临床 RAG 对比」的样板（呼应 [08-08 digest](../2026-08-08/conference-digest.md) §4.5 的「可行动增益」标准）。

---

## 5. 本期主题串讲

1. **KDD 2026 颁奖「树模型回望 × 提速基础设施 × 华人学者」**：XGBoost ToT 是树模型时代工业影响力的封存证词；EARTH HM（26×–19× 加速）把奖项给了「空间网络 K-function 分析」这一基础算法；Innovation Award 归 Wei Wang（UCLA）。三者组合的信号：**KDD 价值观仍高度尊重「可部署的系统贡献 + 可验证的基础设施」**。
2. **广告/推荐工业论文进入「标签—分配—训练结构」严谨化**：MAC/MoAE（归因歧义显式建模）、Tencent 确定性分配（非确定性→可行解不存在性的理论证明）、DLL（流式下重建 session 监督）——KDD 2026 工业簇不再只报「+X% 指标」，而是在**数据/标签/决策三层的正确性**上做文章。
3. **模拟器可信度成为 RL 主课题**：Simulator Collapse 与 [arxiv-daily](./arxiv-daily.md) 的 OPD 诊断簇（GCPO/PAIR/REOPD）形成呼应——**「训练分布里的单模态偏差必须被显式诊断」从 LLM RL 泛化到人机交互多智能体**；对「模拟器在环 RL」（ResidencyRL 等）构成方法论前提性批判。
4. **机制可解释从「描述」走向「自主发现 + 可干预」**：Mechanist 的「13K 知识图谱 + 43M 论文库 + 32 方法库」把可解释性变成可运行的 agent 科研流水线，且产出可直接干预 DNA 生成的落地结果——与 [arxiv-daily](./arxiv-daily.md) 的机制工作（任务向量因果、unlearning 定位）同频。

---

## 附：本期核验与去重记录

- **已覆盖、排除**：HealthBench benchmark 本体（[2026-06-13 tech-report-digest](../2026-06-13/tech-report-digest.md)，index/log 命中）、FAT-CTR（[wiki/papers/ctr/fat-ctr-scaling.md](../../papers/ctr/fat-ctr-scaling.md)）、KDD 开幕前数据口径与 KDD Cup（[08-08 digest](../2026-08-08/conference-digest.md)）、主会论文与 AI-for-Science 等（[08-07 digest](../2026-08-07/conference-digest.md)）、同日 37+17 篇 arXiv（[arxiv-daily](./arxiv-daily.md) + [arxiv-paper-check](./arxiv-paper-check.md)）、Jeff Dean 组织变更（[08-08 digest §4.6](../2026-08-08/conference-digest.md)）。
- **核验方式**：3 篇新收录 arXiv（2608.12253 / 2608.12036 / 2608.12138）全部经 arXiv ID + 标题对 index.md、log.md、wiki/synthesis/** 全文 grep（0 命中）后收录；KDD 奖项以 kdd.org / ACM DL / HKBU / UCLA 官方公告为准；Innovation Award 口径修正为 Wei Wang（以 UCLA CS 公告为准）；主 Best Paper / Best Student Paper 未确认（kdd.org 奖项页反爬），标注待后续核验；Paper Digest 三篇以 DOI 对应官方录用为准。
