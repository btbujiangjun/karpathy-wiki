---
title: "Conference & arXiv Daily Digest: 2025-2026 Top ML/AI Venues"
type: synthesis
created: 2026-09-08
updated: 2026-09-08
sources: []
tags: [conference-digest, emnlp-2026, kdd-2026, sigir-2026, acl-2026, aaai-2027, icml-2026, agents, benchmark, tool-calling, skill-learning, reward-model, interpretability, sae, reasoning, evidence, fact-checking, health-ai, scientific-ai, peer-review, daily-digest]
---

# Conference & arXiv Daily Digest: 2025-2026 Top ML/AI Venues

> Compiled 2026-09-08. Venue-proceedings + arXiv 综合摘要。由于自 Mon 7 Sep 2026 起无新 arXiv 品类（当日清单同为 Mon 7 Sep 批次），本期为**第二批过筛 + 顶会锚定**：聚焦本周邮件批次中冒出的 EMNLP 2026 录用论文，并复核 SIGIR 2026 / KDD 2026 奖项动态。全部 featured arXiv ID 已 grep 验证在 `wiki/` 中无重复（16 篇新收录），兄弟 digest（09-07/09-08 [[arxiv-daily]]/[[arxiv-ai-search]]/[[arxiv-paper-check]]/[[game-rl-daily]]/[[conference-digest]]）已收录的 ID 只做交叉引用。
>
> 中文：本期为 2025-2026 各大顶会 + 最新 arXiv 综合摘要。机构归属部分基于作者身份推断（标注 `(推断)`），需以原文核实。

---

## 1. 概览 / Overview

- **EMNLP 2026** 录用论文开始在本周 arXiv 批次集中浮现：本期锚定了 4 篇（Main ×2 来自语音事实核查与社会语用、Industry ×1 多步工具调用、System Demonstrations ×1 代码重构），另有 2 篇 Findings/其他（见 §5）。
- **SIGIR 2026**（墨尔本, 7/20-24）奖项已确认：Best Paper《Why Advanced Encoders Lag on Sparse Retrieval》、Best Student《Topic-Specific Classifiers are Better Relevance Judges than Prompted LLMs》、Best Short《When RAG Disagrees》、Test of Time《Learning to Rank with Selection Bias in Personal Search (SIGIR 2016)》——**已于 08-07 digest 收录，本期不重复**，仅交叉引用 [[conference-digest]] (2026-08-07)。
- **KDD 2026**（济州岛, 8/9-13）已闭幕：公开渠道未见 Best Paper 公告（KDD 官方奖项页多为历届回顾）；论文页可见 Meta 广告实验系列（Jikai Jin/Stanford、Kenneth Hung、Baoyi Shi/Meta）。KDDCUP'26 CRAFT 等已在 09-07 digest 覆盖。
- **AAAI-27** 评审周期爆出审稿人联合 bidding（collusive bidding）报告——本期 CABAL（§4.4）正是对此的端到端模拟。
- **Rec / CTR / 广告**：本周 cs.IR Mon 7 Sep 批次已被 09-07 兄弟 digest「全量开采」（Embedding Surgery / AtomRec / PTDG / LARK / MURAL / AutoLR / Trade-up Rec 等），本期无新 rec 主条目，相关趋势见 §6。
- **Games**：新批次无全新 game-RL 主条目；本周游戏侧亮点（Abstraction Agent 2609.04303、CHAMP 2609.04870、HPGPN 2609.04803）已由 09-07 [[arxiv-daily]]/[[game-rl-daily]] 收录。

---

## 2. EMNLP 2026 — 本周 arXiv 批次中的录用论文

### 2.1 Multi-Step Tool-Calling over Korean Open Public APIs: A Benchmark and a Data-Synthesis Recipe（KOPA-Bench + EDGE）
- **Title (中文)**: 韩语开放公共 API 上的多步工具调用：基准与数据合成方案
- **Authors**: Dain Kim, Eungi Cho, Kyumin Kim, Shinyeong Noh, Kyuseong Lim
- **Affiliation**: 未在 arXiv 标注（韩国公共机构数据主权的 on-premise LLM agent 场景）
- **Venue**: EMNLP 2026 Industry Track（arXiv [2609.05395](https://arxiv.org/abs/2609.05395)）
- **Abstract & Innovations**:
  - 数据主权法规要求公共机构部署**开源、on-premise** 的 LLM agent，跨多个政府 API 链式调用工具；开源模型在此多步场景下持续落后，且此前无基准量化该差距。
  - 提出 **KOPA-Bench**：145 个真实世界任务。再提出 **EDGE（Execution-grounded Dynamic Graph）**：构造"工具输出可喂给另一工具输入"的执行图，只保留**对活 API 实际调用成功**的边，遍历已验证边合成可执行的多步轨迹。
  - GRPO 微调得到 9B 模型，**几乎追平同族未调 27B 模型**，在 KOPA-Bench 与 BFCL 上均有显著提升。
- **Comparison**: 相比静态/规则合成 tool-calling 数据（常含幻觉链条），EDGE 用 live execution 验证链路，首次量化开源模型在真实政府 API 多步调用上的差距。
- **Relevance**: 与本周 [[arxiv-daily (2026-09-08)]] 中 Multi-Harness RL 的"evaluation harness 主导"结论相呼应——数据落地方式（execution-grounded vs 离线）直接决定 agent 能力。

### 2.2 TRILOGUE: A Trilingual Spoken Dialogue Fact-Checking Benchmark with Evidence and Paired Audio
- **Title (中文)**: 三语口语对话事实核查基准（含证据与配对音频）
- **Authors**: Chaewan Chun, Meruyert Aristombayeva, Jiyoung Choi, Mahjabin Nahar, Delvin Ce Zhang, Dongwon Lee
- **Affiliation**: 未标注（推断：Penn State — Dongwon Lee 等）
- **Venue**: EMNLP 2026 Main（arXiv [2609.04452](https://arxiv.org/abs/2609.04452)）
- **Abstract & Innovations**: 错误信息常先"被听到"而非"被读到"，但事实核查仍主要评估干净书面文本。TRILOGUE 是首个大型**三语（英/俄/哈萨克）源码背书口语对话**基准：近 12K 对话、187K turns、**390 小时配对音频**，含 ASR 文本与逐词时间戳对齐，近 5K 条人工录音俄/哈对话。支持 claim check-worthiness 检测、source-article evidence retrieval、claim verification（claim-only / gold-evidence / retrieved-evidence 三输入模式）。
- **Results**: 基线显示 ASR 退化与跨语言迁移仍是难点（哈萨克语尤甚）；retrieved evidence 显著缩小与 gold-evidence 验证的差距。
- **Comparison**: 相对此前小型、英语中心或仅注释的口语核查资源，TRILOGUE 是首个端到端、多语言、带配对语音 + turn 级标签的基准。

### 2.3 You Really Didn't Get That? Benchmarking Social Pragmatic Inference for Indirect and Playful Chinese Online Comments
- **Title (中文)**: 中文网络评论的间接与戏谑语用推理基准
- **Authors**: Shiwei Hong, Junjie Ma, Emma Jiren Wang, Ethan Z. Rong, Siying Hu, Haichang Li, Ziying Wang, Zhicong Lu
- **Affiliation**: 未标注（推断：City University of Hong Kong — Zhicong Lu）
- **Venue**: EMNLP 2026 Main（arXiv [2609.04384](https://arxiv.org/abs/2609.04384)）
- **Abstract & Innovations**: 中文在线评论常靠间接/戏谑语言传达社会意义。从 200,000+ 条公开中文社交媒体互动记录构建 **4,735 条人工验证诊断项**，每条把目标评论与重构前文 + 合理误读配对；8 个 LLM 同时作为题目作者与求解者做 leave-writer-out 评测。
- **Results**: 最强模型仅 81.42% LWO 准确率；8 模型均值 68.70%，人类 90.8%。案例分析：模型常识别出"讽刺/戏谑"，但**误判其机制或互动动作**（如反讽 vs 礼貌拒绝）。
- **Comparison**: 与按预定义语用类别组织项目（SOCIALIQA / Fig-QA 类）不同，本基准检验模型能否区分"具体会话中评论实际在做什么"的情境化解读。

### 2.4 RefactorPlatform: An Open-Source Harness for Controlled Evaluation of Repository-Scale Refactoring Agents
- **Title (中文)**: 仓库级重构 agent 的受控评估开源平台
- **Authors**: Aziz Ben Amor, Drish Mali, Mann Acharya, Vijayasri Iyer, Sébastien Bratières
- **Affiliation**: 未标注（推断：University of Auckland — Sébastien Bratières）
- **Venue**: EMNLP 2026 System Demonstrations（arXiv [2609.04898](https://arxiv.org/abs/2609.04898)）
- **Abstract & Innovations**: 仓库级重构要求 coding agent 把单点改动跨多相互依赖文件传播且不改变行为。RefactorPlatform 固定环境、逐轴隔离设计选择：模型 backbone（OpenRouter / GitHub Copilot CLI）、执行体制（baseline / retrieval-augmented / multi-agent）、prompt 特异性；每次运行在隔离工作区，带实时终端流、per-task token/diff/transcript 记录、AST 验证、可审计遥测。
- **Results**（100 个多文件 RefactorBench 任务 × 4 模型族）: AST-aware chunking 比普通 token-window chunking 高 **25–30%**；朴素 retrieval 反而低于无 retrieval 基线；**单 agent + 精简 RAG（86%）胜过 sub-agent 配置（66%）**；retrieval 的精度增益被 token 开销抵消，单位成功重构成本不变。
- **Comparison**: 首次把"设计选择对 agent 成功的因果贡献"隔离出来，提供可复现/可审计的评估基线——与 Harbor（§3.2）、TruthInsightBench（§3.4）同属本周"评估基建"主题。

---

## 3. Agents — Skill Learning & Evaluation Infrastructure

### 3.1 Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents
- **Title (中文)**: 面向 LLM agent 的过渡感知 EigenTrace 多层级技能归纳
- **Authors**: Jiazheng Sun, Boyu Yang, Binhao Yuan, Mingxuan Li, Xin Peng
- **Affiliation**: 未标注（推断：Fudan University — Xin Peng；cs.SE 交叉）
- **Venue**: arXiv 2609.05261 (cs.AI/cs.SE, 2026-09)
- **Abstract & Innovations**: 现有 agent 技能范式受限于浅层轨迹检索与扁平技能摘要，忽略时间依赖与"结果条件化"的行为拓扑。Trace2Tower 把 step 级交互抽象为规范事件，构建以语义兼容性、转移动态、结果证据统辖的统一图；经**对比谱分解**分离"稳定成功对齐行为模式"、抑制失败捷径；这些模式组织成精致技能塔（action templates → procedural routines → task strategies），由 verifier 反馈持续精炼。
- **Results**: ALFWorld 87.31% 成功率（10.35 步、0.26 次非法动作）；WebShop 50.67% 精确成功；显著超越现有基线在任务掌握与上下文高效复用上的表现。
- **Comparison**: 相对 Experiential Co-Learning / WikiSkill 等扁平技能检索，谱分解给出"时序+结果证据"感知的层级技能归纳；与本周 Illustration[[arxiv-daily (2026-09-08)]] 收录的 computer-use skill-evolution 形成正反对照（后者的 revision churn 负结果）。

### 3.2 Harbor Adapters and Harbor-Index: Infrastructure and a Curated Meta-Dataset for Large-Scale Agentic Evaluation
- **Title (中文)**: Harbor Adapters + Harbor-Index：大规模 agentic 评测基础设施与策展元数据集
- **Authors**: Lin Shi, Haowei Lin, ...（120+ 作者，含 Mike Merrill, Ludwig Schmidt, Alex Shaw, Di He 等）
- **Affiliation**: 大型开放协作（推断：Princeton / Stanford / 工业界 consortium）
- **Venue**: arXiv 2609.04298 (cs.AI, 2026-09)
- **Abstract & Innovations**:
  - **Harbor Adapters**：统一评测基础设施，把 **80+ agentic benchmark** 移植为可评估任意 agent，经严格代码评审与 parity 实验验证；随后对 **8 个能力层级模型 × 54 个基准**做大规模评估（每模型跑 Terminus-2 + 3 个原生 harness 之一）。
  - **Harbor-Index**：经难度过滤、AI/人工审计与 audit-and-fix 循环自适配套件提炼的 **82 个难/多样/高质量任务（29 个基准）**；无任何 model-harness 组合超过 30% 通过率，最强组合（GPT-5.5 + Codex）为 28.0%。
- **Comparison**: 相对各 benchmark 各自维护 harness 的割裂现状，"适配器 + 元数据集"是可负担、可复现的大规模 agent 评估基础设施；与本周 ττ-Bench（engagement 真实感路线，见 [[arxiv-daily (2026-09-08)]]）构成"规模 vs 真实感"两种评测哲学。
- **Release**: adapters、评估结果、分析、Harbor-Index 全开源。

### 3.3 Substrate-Aware AI Agents: Execution Context as a First-Class Input
- **Title (中文)**: 基底感知 Agent：执行上下文作为一等输入
- **Authors**: Manu Agrawal
- **Affiliation**: 未标注（单作者）
- **Venue**: arXiv 2609.05232 (cs.AI, 2026-09)
- **Abstract & Innovations**: agent 在动作选择时忽略内存/执行时/运行库/算力/运维约束，作者称之为 **substrate blindness**。以数值代码生成为可控实验场：三个前沿模型配置（Claude Opus 5 / GPT-5.6-Sol / Gemini 3.7 Flash）在"仅任务"对比"任务 + 128 MB RAM / 10.0 s wall-time 契约"下生成代码。
- **Results**: 契约披露在 13/14 组可执行配对中降低峰值内存、三组均降低平均 wall time（最快 **3.1×**）；结构变化含 bounded blocking、float32 retention、upper-triangle traversal、in-place/memory-mapped buffers。在更紧 96 MB 契约下：契约披露组正确且达标 4/5、5/5、3/5，任务only 组 0/5、1/5、0/5；MaxRSS 降 49–74%、wall time 降 35–64%。
- **Comparison**: 首次给出"最简执行契约诱导程序主动结构适配"的受控证明——执行约束从部署后修复项变成 planning 的一等输入。

### 3.4 TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents
- **Title (中文)**: 以证据为基的开放式科学发现 agent 自动化评测基准
- **Authors**: Zhibo Yang, Chen Zhang, Yuewei Zhang, Hao Wang
- **Affiliation**: 未标注
- **Venue**: arXiv 2609.05079 (cs.AI/cs.CL, 2026-09)
- **Abstract & Innovations**: 自动编码 agent 常被当作"AI 科学家"，但"执行规定分析 ≠ 做出发现"。既有基准均为 reproduction 配置（围绕隐藏目标研究构建）；TruthInsightBench 反之：**40 个盲任务（40 篇同行评审研究、10 个科学领域）**只暴露中立科学目标与冻结数据，隐蔽源结论/预期值/分析路径；固定 LLM 裁判沿 6 维度按 **29 个 artifact-grounded 条目**给分，确定性聚合、无需逐条人工打分。
- **Results**: 同一冻结基座模型上，4 个 coding agent 形成窄平台（58.4–60.3/100），**无统计显著的成对分离**：执行力与文档化好、可审计性与新颖性强，但缺乏确立可信论断的判别动作（control、robustness、falsifiability、cross-dataset generalization）。瓶颈是**科学判断而非编码**。
- **Comparison**: 与 SciDocBench（§4.2，"读论文/文档理解"）互补：TruthInsightBench 测"发现"，SciDocBench 测"文档叙述理解"，共同把"AI 科学家"拆成可测的维度。

---

## 4. Benchmarks & Eval-Driven Reliability Studies

### 4.1 WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data
- **Title (中文)**: 面向真实可穿戴数据的健康推理基准
- **Authors**: Ji Soo Lee, Xilun Chen, Pierce Chuang, Ashish Shenoy, Jason Wei, Dohwan Ko, Hyunwoo J. Kim, Benoit Corda
- **Affiliation**: 未标注（推断：Google —— Pierce Chuang / Ashish Shenoy / Jason Wei / Benoit Corda + KU）
- **Venue**: arXiv 2609.05405 (cs.CL, 2026-09)
- **Abstract & Innovations**: 可穿戴设备连续监测生理与行为信号，但既有基准很少评测 AI 对"真实用户纵向可穿戴记录"的推理。WearableQA 由 200 位真实用户（每人至多 **500 天**日测数据）的时间序列、血液生物标志物与人口统计学构建 **4,084 个 10 选 1 问题**，保留设备噪声与个体差异。16 种题型沿两轴组织：**data vs health reasoning**（纵向计算 vs 生理解读）、**single- vs cross-signal reasoning**（单信号 vs 多信号整合）；dual-grounding 构造框架 = 文献锚定的生理发现 + 统计验证的人群生理模式。
- **Results**: 14 个专有/开源 LLM 性能 19.6%–72.9%（10% 随机基线），多数模型 <60%，远未解决。
- **Comparison**: 相对合成/模拟健康数据基准，首个基于真实人口纵向可穿戴记录、带诊断性题型轴的基准（health AI 时序/多模态推理）。

### 4.2 SciDocBench: A Workflow-Centered Benchmark and Data Pipeline for Scientific Document Understanding (+ SciDocIR / SciDocDataset)
- **Title (中文)**: 以工作流为中心的科技文档理解基准与数据管道
- **Authors**: Shenxi Wu, Yuhong Liu, Haosong Zhang, Tongjin Zou, Yanxun Zhang, Gaochang Chen, Dun Liang, Jiaqi Wang, Zhecan James Wang, Yuhang Zang, Dahua Lin
- **Affiliation**: 未标注（推断：Shanghai AI Lab / CUHK-Shenzhen — Dahua Lin）
- **Venue**: arXiv 2609.05141 (cs.AI, 2026-09)
- **Abstract & Innovations**: 论文要求模型联合推理文本/公式/图/表/代码/数据集并保持证据溯源；既有基准分项孤立评估。SciDocBench 含 **124 条专家撰写、难度筛查的问题**，组织为 7 个研究助理能力组 × 19 个子任务 × 5 个科学领域；每题 4 种匹配条件（英/中 × all-images-first / interleaved），共 **496 评测实例**。
- **Results**: 最强系统仅 62.6/100，弱项集中在 document perception、evidence grounding、verification 与跨文档推理。配套 **SciDocIR**（类型化证据图，保留对象/布局/交叉引用/溯源）与 **SciDocDataset**（~15K SFT + 8K RL 样本，14 个可验证子任务），构成"评估→训练"闭环。
- **Comparison**: 相对单任务文档理解基准（DocVQA / LongBench 等），SciDocBench 首次以研究工作流为中心做受控矩阵评测并转成可扩展训练信号。

### 4.3 Same Trajectory, Contradictory Rewards (ROBORMBENCH): Paraphrase Fragility in Vision Language Reward Models
- **Title (中文)**: 同轨迹、矛盾奖励（ROBORMBENCH）：视觉语言奖励模型的语义改写脆弱性
- **Authors**: Wonje Jeung, Sangyeon Yoon, Hyesoo Hong, Yoonjun Cho, Dongjae Jeon, Bumjun Kim, Jean Oh, Youngjae Yu, Albert No
- **Affiliation**: 未标注（推断：韩国高校/研究所联盟）
- **Venue**: arXiv 2609.05401 (cs.RO/cs.CL, 2026-09)
- **Abstract & Innovations**: VLM 越来越多充当机器人学习奖励函数，该角色要求**语义改写不变性**：等价目标描述下同一轨迹应得同一奖励。ROBORMBENCH 以 **2,390 条真实机器人轨迹 + 21,673 条已验证改写**（词法/句法/动作目标三类）量化这一失败。
- **Results**: 仅改写指令即可大幅改变预测进度分数、甚至把相同行为在失败/成功之间翻转；跨专有与开源 VLM 普遍且严重，随改写发散程度增强，**不随规模或显式推理可靠减少**；带轨迹锚定监督的专用奖励模型显著更稳定。
- **Comparison**: 首次把 paraphrase robustness 定义为首要评测轴融入 VLM reward 建模；与本周 [[arxiv-daily (2026-09-08)]] 的 HackProbe（reward-model 黑客免疫）互证"奖励信号脆弱性是泛问题"。

### 4.4 CABAL: Multi-Agent Simulacra for Tracing the Effects of Collusive Bidding in Peer Review
- **Title (中文)**: 用多智能体仿真追踪同行评审中联合投标的影响
- **Authors**: Jicheng Zhou, Kemou Li, Kahim Wong, Zheyuan Li, Zhuan Shi, Fengpeng Li, Haiwei Wu, Jiantao Zhou
- **Affiliation**: 未标注（推断：University of Macau — Jiantao Zhou）
- **Venue**: arXiv 2609.05227 (cs.AI, 2026-09)
- **Abstract & Innovations**: AAAI-27 评审周期报告显示审稿人可协调投标以获取互利指派。CABAL 是端到端多智能体仿真框架：固定会议环境、配置诚实/合谋的 LLM 审稿人策略；提出 **affinity-guided collusive bidding**（用互评审稿人-论文亲和度构造合谋环并选目标论文，形成"专业一致"而非随机攻击）。
- **Results**: 合谋投标使目标论文被捕获率**翻倍以上**；被指派的合谋者评分比诚实共同审稿人高约 2 分，会议整体效应相对温和；现有 bid-phase 检测器证据有限——固定三元组压力测试中，本征"正投标图"被良性亲和混淆，而 Very-High 专诊视图可实现精确但低覆盖率的局部恢复。
- **Comparison**: 相对把 bidding / assignment / review 分阶段处理的工作，首次模拟其全生命周期效应并提供 counterfactual 基座（同一会议两个世界）。

---

## 5. Interpretability, Reasoning & Mechanisms

### 5.1 SharedSAE: One Feature Dictionary Across Language Models
- **Title (中文)**: 跨语言模型共享单一特征字典
- **Authors**: Daniil Ognev, Célian Vasson, Lijie Hu, Kentaro Inui, Benjamin Heinzerling
- **Affiliation**: 未标注（推断：Tohoku University / MBZUAI — Inui / Heinzerling）
- **Venue**: arXiv 2609.04344 (cs.LG/cs.CL, 2026-09)
- **Abstract & Innovations**: SAE 训练与 latent 标注需对每个模型重复。SharedSAE 用**共享字典 + 每模型专用 encoder-decoder 对**取代一组专用 SAE；相比最近方法（丢弃激活幅度、推理时需全部模型），SharedSAE 只归一化 selection scores、保留幅度，并用 model dropout 支持单模型推理。
- **Results**: 4 个 1B 级、跨家族/跨 tokenizer 的模型上，共享 latent 仍保留**专用 SAE 平均解释方差的 96.6%**；cross-model latent 相关比事后对齐的独立 SAE 高 1.8×；latent 描述跨模型可迁移；字典冻结后新模型可高效适配、接近专用重建质量且复用描述。
- **Comparison**: 相对 SAE 家族各自为政或 CrossSAE 剪枝路线，SharedSAE 首次给出"一个字典、全模型可用 + 可增量适配"的机制（feature-as-subspace 视角）。

### 5.2 Evidence Integration in Large Language Models
- **Title (中文)**: 大语言模型中的证据整合
- **Authors**: Sebastien Kawada, Manolis Kellis
- **Affiliation**: 未标注（推断：MIT — Manolis Kellis）
- **Venue**: arXiv 2609.04290 (cs.CL/cs.AI/cs.LG, 2026-09)
- **Abstract & Innovations**: 提出证据整合的**分布理论**——证据按"接收者先验权重 + 候选证据倾斜"平移初始答案分布，导出三条预测：(1) 对接收者越"可能"的候选越有说服力；(2) 接收者更易整合自己的特征性错误而非异源错误；(3) **同一证据可增强弱模型而损害强模型**。
- **Results**: 10M+ 试验、12 个 LLM、4 个家族、8 个领域（含量子力学/物理/遗传/分子生物学 4 个科学发现任务）验证；得 receiver-relative reliability frontier（接收者一致的错误比同率随机错误压得更狠）；LLM 甚至在内核证某候选无效后仍整合之（命题约束下 93–100%，跨 held-out 科学与生命推理最高 99.4%）。因果干预定位实现于**网络深处**：逐步 admitting/promoting/transporting 外部候选到答案态；verification 表征可解码但对答案因果影响很小（J-lens 分解：verbalized verification 状态可与 candidate integration 状态完全分离）。
- **Comparison**: 相对把证据当"标量信任"或简单 context 拼接的工作，给出接收者专属控制策略 + 机制层面的因果证据（对 RAG/工具链设计有直接含义）。

### 5.3 Fractal basins trap latent reasoning
- **Title (中文)**: 分形吸引盆困住隐性推理
- **Authors**: Jeffrey Lai, Anthony Bao, John Quinn, William Gilpin
- **Affiliation**: 未标注（推断：UT Austin / SFI — William Gilpin）
- **Venue**: arXiv 2609.04963 (cs.LG, 2026-09)
- **Abstract & Innovations**: 推理模型在难任务上推理更久，机制未明。本文显示推理模型呈现**瞬态混沌**（transient chaos）——困难任务计算复杂性的物理后果；前沿推理模型是有**分形吸引盆**的动力学系统，难度的分形性随 Sudoku、迷宫、视觉谜题、数学逻辑等任务难度上升；瞬态混沌源于推理在**鞍点**（对应"几乎正确的候选解"）附近长时间被困。
- **Results/Claim**: 推理变慢是问题硬度的**必然**后果，而非工程缺陷；推理 trace 是新的动力学系统类别。
- **Comparison**: 相对把验证/搜索开销归因于模型设计（如 RLHF 过度思考）的解释，从动力学角度给出"hardness-inherent"的机制性解释。

---

## 6. Generative & Applied Science

### 6.1 Training Large Language Models for Small-Molecule Design with Synthetic Task Scaling
- **Title (中文)**: 用合成任务缩放训练面向小分子设计的 LLM
- **Authors**: Frank Hu, Shriram Chennakesavalu, Zichen Wang, Patricia Suriana, Bodhi Vani, Kirill Shmilovich, Kangway Chuang, Colin Grambow
- **Affiliation**: 未在 arXiv 标注（工业级团队；涉及 lead optimization 强评分）
- **Venue**: arXiv 2609.04735 (cs.LG, 2026-09)
- **Abstract & Innovations**: 药物候选设计需在组合爆炸且崎岖的化学空间里多目标搜索；RLVR 虽可改进 LLM，但许多化学评分函数单次评估需数小时/数天。本文研究 LLM 能否从**廉价合成任务**学到分子设计策略、迁移到昂贵的 lead optimization：**课程式训练**逐步纳入更难合成设计任务，使模型在结构化 lead optimization 上**超越更大的前沿模型**。
- **Claim**: 合成任务缩放 post-training 是"训练成本高到无法直接训练"场景的有效策略。
- **Comparison**: 归入本周"post-training 数据经济学"叙事（1-shot OPD、Extremely Sparse Supervision，见 [[arxiv-daily (2026-09-08)]]）。本期简记为主项，未设分节。

---

## 7. 去重说明 / Dedup & Cross-References（不重复收录）

以下本周/近期已有条目仅在此交叉引用，不展开（避免重复 ingest）：

| ID / 主题 | 已收录位置 |
|---|---|
| AutoLR: Automating Research-to-Launch Review（NetEase DASHEN） | 09-07 [[arxiv-daily]] |
| Memory Portability（low-rank adapters） | 09-07 [[arxiv-ai-search]] / 09-08 [[arxiv-daily]]（引用） |
| Abstraction Agent for Imperfect-Information Games（Tsinghua） | 09-07 [[game-rl-daily]] / [[arxiv-daily]] |
| Extremely Sparse Supervision（1–2 tokens） | 09-08 [[arxiv-daily]] |
| Trade-up Rec / Distill Globally Adapt Locally | 09-07 [[arxiv-daily]] / [[arxiv-ai-search]] |
| SIGIR 2026 四大奖项（Best/Best Student/Best Short/ToT） | 08-07 [[conference-digest]] |
| ACL 2026 Outstanding — Lying with Truths | 08-05 / 08-16 / 08-17 / 08-26 digests |
| NeurIPS 2025 Best（Gated Attention）/ ICLR 2026 Outstanding（LLMs Get Lost; Transformers are Inherently Succinct） | 历史 digest |

---

## 8. Cross-Cutting Observations（2026-09-08）

1. **EMNLP 2026 批次开始成簇出现**：Main/Industry/SysDemo 论文在本周 arXiv 层级化 (KOPA-Bench、TRILOGUE、社会语用、RefactorPlatform)，叠加兄弟 digest 中的 EMNLP'26 论文（Persistent Teacher Anchoring、Beneath the Surface of CoT、Refuse without Refusal 等）——"录用即上传"节奏加快，conference-digest 后续会系统锚定。
2. **"评估评估者"（evaluating the evaluators）成显性主题**：ROBORMBENCH（VLM 奖励改写脆弱性）、CABAL（同行评审合谋）、TruthInsightBench（reproduction vs discovery）、WearableQA（真实数据 vs 合成）——本周四条并进，全部在测**评测/奖励机制本身的可靠性**。
3. **技能重用的两副面孔**：Trace2Tower（谱分解 + verifier 精炼，正向 SOTA）与 [[arxiv-daily (2026-09-08)]] 的 computer-use skill-evolution（revision churn 负向）并存——"skills always help"叙事需要按任务审计。
4. **Agent 评测基建两派**：Harbor（>80 benchmark 适配 + 元数据集 + 28% 天花板）vs ττ-bench（engagement 真实感 + 23.9% vs 82.2% 专家天花板）——规模可负担与端到端真实感的张力将持续。
5. **数据主权驱动开源 on-prem 部署成为欧亚市场专项**：KOPA-Bench（韩国公共 API）、中文语用基准、哈萨克语语音核查——多语言、非英语链路在本周密度明显上升。
6. **"执行契约/执行验证"贯穿多个子域**：Substrate-Aware（内存/时间契约）、KOPA-Bench EDGE（live API 验证）、RefactorPlatform（AST 验证）——把"运行真相"放进 agent 的设计与评估。

---

## 9. Sources & Method Notes

- 数据来源：arXiv（Mon 7 Sep 2026 批次，`/abs/` 逐篇核实 16 篇）、EMNLP 2026 官方录用信息（arXiv 注释）、SIGIR 2026 奖项页（交叉引用 08-07）、KDD 2026 官网/公开检索（奖项未见公开公告）。
- 方法：按 venue + 领域过滤；所有 featured arXiv ID 已 `rg` 验证在 `wiki/` 无重复；与同批兄弟 digest（09-07/09-08 全部 5 个）ID 级去重。
- 机构归属：多数 arXiv 页面未注机构，本页采用 `(推断)` 标注；需以论文原文核实。
- 语言：本页以中文为主体正文（符合仓库惯例与来源混合语言），YAML/表头/ID/协议标识保持英文。