---
title: "Conference Digest 2026-08-06：Agent 评测方法论转向（OmniaBench / LoopsBench / 影子评审）+ ACL 2026 世界模型新作 + 测试时扩展与世界模型综述 + 顶会获奖全景导航"
type: synthesis
created: 2026-08-06
updated: 2026-08-06
sources: []
tags: [conference-digest, acl-2026, kdd-2026, sigir-2026, icml-2026, neurips-2026, agent-benchmarks, world-models, test-time-scaling, coding-agents, ai-research, arxiv]
---

# Conference Digest — 2026-08-06

本期聚焦 **此前未覆盖的新论文**（每篇均经 index.md / log.md / 各 synthesis 全库 grep 去重）：ACL 2026 Long 世界模型新作 **From Word to World**、Agent 评测方法论转向三件套（**OmniaBench** 通用 Agent 基准 / **LoopsBench** 编码 Agent 循环工程基准 / **影子评审 shadow evaluations** 衡量 AI 自动化科研）、NVIDIA **NOOA** 面向对象 Agent 框架，外加 arXiv 分类精选两篇综述（**Test-Time Scaling 推理 LLM** / **视频生成模型作为世界模型**）。获奖全景在 [08-01](../2026-08-01/conference-digest.md)、[08-03](../2026-08-03/conference-digest.md)、[08-04](../2026-08-04/conference-digest.md)、[08-05](../2026-08-05/conference-digest.md) digests 已覆盖者仅作导航不重复展开；当日 arXiv 流（推荐/广告/RL 推理等 24+27 篇）已由同日 [arxiv-daily](./arxiv-daily.md) 与 [arxiv-paper-check](./arxiv-paper-check.md) 覆盖。

---

## 0. 顶会获奖全景快速导航（已覆盖 → 详情入口）

| 会议 | 状态 | 覆盖入口 |
|------|------|----------|
| **ICML 2026**（Seoul, 7/6–11） | 3 Outstanding + 3 HM 已覆盖 | [08-04](../2026-08-04/conference-digest.md) §1.2 |
| **NeurIPS 2025**（San Diego, 12/2–7） | 4 Best + 3 runners-up 已覆盖 | [08-01](../2026-08-01/conference-digest.md) + [08-04](../2026-08-04/conference-digest.md) §1.6 |
| **ICLR 2026**（Rio, 4/23–27） | Outstanding/HM/ToT/e3 已覆盖 | [08-01](../2026-08-01/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §6 |
| **AAAI 2026**（Singapore, 1/20–27） | Best 已覆盖（录用率 17.6%） | [08-01](../2026-08-01/conference-digest.md) |
| **CVPR 2026**（Denver, 6/3–7） | 全部奖项已覆盖（16,092/4,089, 25.4%） | [08-04](../2026-08-04/conference-digest.md) §1.1 |
| **KDD 2026**（Jeju, 8/9–13） | Research Best = PiPNN 已覆盖；Vol.1 工业推荐 5 篇已覆盖（奖励 8/13 公布） | [08-04](../2026-08-04/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §1 |
| **ACL 2026**（San Diego, 7/2–7） | 完整奖项已覆盖；**本期补 Long 世界模型新作** | [08-04](../2026-08-04/conference-digest.md) §1.4 + 本期 §1 |
| **EMNLP 2025**（Suzhou, 11/4–9） | 完整奖项已覆盖（Main 22.16%） | [08-04](../2026-08-04/conference-digest.md) §1.5 |
| **WWW 2026**（Dubai, 6/29–7/3） | Best/Best Short/ToT + NEZHA 已覆盖 | [08-04](../2026-08-04/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §4 |
| **SIGIR 2026**（Melbourne, 7/20–24） | 官方奖项 pending；确认论文 4 篇已覆盖 | [08-05](../2026-08-05/conference-digest.md) §2 |
| **CIKM 2025**（Seoul, 11/10–14） | Best Full + Best Student 已覆盖 | [08-03](../2026-08-03/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §5 |
| **RecSys 2025**（Prague, 9/22–26） | Best Full/Short + ULIM 已覆盖 | [08-03](../2026-08-03/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §5 |
| **NeurIPS 2026**（San Jose, 12/6–12） | 投稿后评估方法论前瞻：**影子评审**（本期 §3） | 本期 §3 |

---

## 1. ACL 2026（San Diego, 7/2–7）— Long 新作：LLM 作为隐式文本世界模型

### 1.1 From Word to World: Can Large Language Models be Implicit Text-based World Models?
**中文标题**：《从词到世界：LLM 能否成为隐式基于文本的世界模型？》

- **作者**：Yixia Li, Hongru Wang, Jiahao Qiu, Zhenfei Yin, Dongdong Zhang, Cheng Qian, Zeping Li, Xiaoteng Ma, Guanhua Chen, Heng Ji
- **机构**：多机构合作（UIUC / UBC / MSRA 等；通讯 Heng Ji，一作 Yixia Li）(tentative，详见论文)
- **会议**：ACL 2026（Proc. Long Papers, pp. 8084–8111, 2026.acl-long.366）；arXiv:2512.18832
- **背景与创新**：Agentic RL 越来越依赖 experience-driven scaling，但真实环境「非自适应、覆盖有限、难以扩展」。世界模型理论上可通过模拟经验提升学习效率，但 LLM 能否可靠担任这一角色、在什么条件下对 Agent 有真实收益，此前缺乏系统性证据。本文把「世界建模」重述为**交互下的 multi-turn next-state prediction**（从 next-token 到 next-state 的范式桥接），提出**三层次评测框架**：①fidelity & consistency（保真与一致性）；②scalability & robustness（规模扩展与鲁棒性）；③agent utility（对下游 Agent 的效用）。
- **实验结果**：在 5 个代表性文本环境（含 WebShop、SciWorld）中：足够训练的世界模型可维持长程一致的潜在状态；随数据量与模型容量**可预测扩展**；下游 Agent 获得具体收益——**action verification 使 GPT-4o 在 WebShop 上 +5.5%**，**warm-started RL 在 SciWorld 上 +15%**。关键边界：收益强烈依赖**行为覆盖率（behavioral coverage）与环境复杂度**——这划定了世界建模何时真正帮助 Agent 学习。
- **对比前作**：对比 Wang et al. (2024) "Can language models serve as text-based world simulators?"（ACL 2024 Short）的单点考察，本文给出保真/扩展/效用三层的系统化证据，并把「in-context 世界建模」与「dynamics-aligned 微调」分开归因——纯 ICL 对依赖内部状态更新的环境不足，需要动力学对齐的微调才能内化潜在动力学。

---

## 2. Agent 评测方法论转向（一）：通用 Agent 基准

### 2.1 OmniaBench: Benchmarking General AI Agents Across Diverse Scenarios
**中文标题**：《OmniaBench：跨多样化场景的通用 AI Agent 基准》

- **作者**：Chengyu Shen, Yujie Fu, Gangtao Xin, Yanheng Hou, Wenlong Fei, Guojie Zhu, Jiawei Li, Hongcheng Gao, Runming He, Zhen Hao Wong, Meiyi Qiang, Hao Liang, Zhao Cao, Hao Jiang, Chong Chen, Wentao Zhang
- **机构**：华为云 + 北京大学 DCAI（Wentao Zhang / Chong Chen 团队）
- **会议**：arXiv:2607.14989（cs.CL, 2026-07-16）
- **背景与创新**：现有 Agent 基准常局限于单一场景、单一工具生态或单一交互格式，难以系统性刻画跨异构应用场景的模型能力。OmniaBench 从应用商店、产品文档、行业资源、Web 检索与人工精修中推导出**层级化场景分类法**——覆盖 ToC / ToB / ToE 三大类、**90 个 level-1 + 354 个 level-2 领域**；基于该分类法构建可执行环境，并用**四条互补路线（DAG / DAG-S / Solver / Program）**合成单轮与多轮任务；引入**十维能力分类法 + 八个组合式原子难度因子**支持细粒度评估。
- **实验结果**：数据规模 **1,431 个任务** + **644 个「困难子集」**（用于降低评估成本、缓解全集公开后的污染）。当前前沿模型仍有显著差距：**Claude-Sonnet-5 Overall Pass@1 = 58.54，GPT-5.6-Sol = 57.14**。跨领域/能力分析显示**规划（planning）、约束维持（constraint maintenance）、自适应纠正（adaptive correction）**为持续短板。
- **对比前作**：对比 GAIA / General AgentBench / ALE 等单一形态基准，OmniaBench 以应用驱动的 ToC/ToB/ToE 分类法 + 明确状态空间 + 合成路线多样化为核心差异，并显式设计污染缓解的困难子集。

---

## 3. Agent 评测方法论转向（二）：编码 Agent 循环工程与 AI 科研自动化评测

### 3.1 LoopsBench: From Harness Engineering to Loop Engineering in Benchmarking Coding Agent
**中文标题**：《LoopsBench：编码 Agent 基准测试从 harness 工程转向 loop 工程》

- **作者**：Han Li, Zhemin Fang, Rili Feng, Yingqi Zhao, Jiaheng Liu, Pengfei Gao, He Ye, Dayi Lin, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
- **机构**：Microsoft（微软研究院）
- **会议**：arXiv:2608.00267（cs.SE, 2026-07-31）；项目页 loopsbench.ai
- **背景与创新**：编码 Agent 基础设施正从「harness engineering（测试台工程）」转向「loop engineering（闭环工程）」——Agent 要应对持续的长周期软件开发，而现有基准只测局部任务或最终状态，无法评估持续执行。LoopsBench 是面向 **loop engineering** 的长周期基准：每个任务是一个**依赖 DAG**，节点为可独立测试的开发单元，边为「带源码证据的前置关系」；其 **flow-aware runtime** 沿 ready frontier 逐步释放测试，并把已完成节点保留为**回归义务（regression obligations）**。
- **实验结果**：112 个任务，来自真实来源，覆盖 **8 种编程语言、9 个领域**；已开源 **5,300+ 开发单元**与可执行测试。最强配置 **Opus-4.7 + Claude Code + outer continuation 仅解决 25.00% 任务**；记录到的计划只能恢复源码推导出的前置 DAG 的一部分，且各 loop 配置下回归事件持续可见——说明长周期闭环仍是开放难点。
- **对比前作**：对比 SWE-bench（局部 bug 修复）与终端状态类基准，LoopsBench 把「测试随执行流动态释放 + 回归义务」作为一等公民，衡量的是 Agent 在真实持续开发中的保持与回溯能力。

### 3.2 Can AI agents conduct open-ended AI research? Early evidence from two case studies
**中文标题**：《AI Agent 能否开展开放式 AI 科研？两项案例研究的早期证据》

- **作者**：Peter Kirgis, Sayash Kapoor, Andrew Schwartz, Stephan Rabanser, David Africa, Konstantinos Voudouris, Viet Nguyen, Toby Pilditch, Magda Dubois, Harry Coppock, Cozmin Ududec, Nitya Nadgir, Matilda Orona, Tilman Bayer, Derrick Chan-Sew, Yue Ling, Abhishek Shetty, Helen Toner, Gillian Hadfield, Seth Lazar, Steve Newman, Shoshannah Tekofsky, Rishi Bommasani, Arvind Narayanan（24 位作者）
- **机构**：Princeton + AI Now Institute + Stanford + Oxford 等多机构（Kapoor / Narayanan 领衔）
- **会议**：arXiv:2607.27191（cs.AI, 2026-07-29）
- **背景与创新**：对「AI 自动化科研」的已有测法要么只测**窄而可验证的任务**（排除开放式研究），要么走**匿名同行评审**（过载、随机、评审质量差）。本文提出第三条路：**影子评审（shadow evaluation）**——让 Agent 承担一篇高质量未发表论文的**核心开放式研究问题**，由**原论文作者**对产出评分。对两篇 NeurIPS 2026 未发表投稿运行：给前沿 Agent **6 天时间 + 数千美元算力**。
- **实验结果**：Agent 在**无人协助下完成了全部工程工作**（复现、跑实验、写代码），但**无法在回答研究问题上取得实质进展**，两篇论文均被原作者**明确拒绝**。识别出**五个反复出现的失败模式**：①对「可发表研究的门槛」判断力差；②对研究设计缺陷缺乏创造力回应；③从死胡同无效回退；④资源意识差；⑤指令漂移（instruction drift）。用第二个模型 + scaffold 做鲁棒性检查，失败模式复现。已发布专家评审、问卷回复、Agent 仓库与日志。
- **对比前作**：对比 AI-scientist 类「生成论文 → 同行评审」范式（如 08-05 digest 中 Oxford F1/MTG adversarial 测试台发现的「差距在过滤与连贯性而非生成」），影子评审以「原作者直接评分」规避评审噪音，提供可复现的失败模式清单，是目前对「Agent 能做 AI 科研的工程、但做不了科研关键环节」的最直接证据。

---

## 4. Agent 框架与编程范式：NVIDIA NOOA

### 4.1 NVIDIA-labs OO Agents: Native Python Object-Oriented Agents
**中文标题**：《NVIDIA-labs 面向对象 Agent：原生 Python 对象式 Agent》

- **作者**：Paul Furgale, Severin Klingler, James Nolan, Matt Staats, Gaia Di Lorenzo, Elisa Martinez Abad, Christian Schüller, Razvan Dinu, Alessio Devoto, Pascal Berard, Gal Kaplun, Elad Sarafian, Riccardo Roveri, Leon Derczynski, Ricardo Silveira Cabral
- **机构**：NVIDIA（NVIDIA Labs）
- **会议**：arXiv:2607.20709（cs.AI, 2026-07-22）
- **背景与创新**：传统 Agent 开发被割裂为 prompt 模板、tool schema、callback 代码与 workflow 图。NOOA 提出更简单的模型无关 Python 框架：**Agent 就是一个 Python 对象**——方法是模型可采取的动作，字段是状态，docstring 是 prompt，类型注解是契约；方法体为 `...` 的方法由运行时 LLM 驱动的 Agent loop 补全，方法体正常的方法仍是确定性 Python。开发者与 Agent 使用同一接口，Agent 行为可像普通软件一样**测试、追踪、重构、改进**。贡献三件套：①agent-as-a-Python-object 编程模型与设计原则；②首次在同一表面组合的 **6 个 model-facing 特性**（typed I/O、对活对象的 pass-by-reference、code-as-action、可编程 loop 工程、显式对象状态、模型可调用的 harness API）；③基准实证。
- **实验结果**：在 SWE-bench Verified、Terminal-Bench 2.0、ARC-AGI-3 及针对性能力测试上，当前模型能有效使用该接口（具体分数原文为准）。
- **对比前作**：对比 LangChain / 早期函数式 tool-calling 框架，NOOA 将 Python 既有抽象（对象/方法/类型/文档）直接采纳为 Agent 接口，社区已有的同类想法大多为实验性或部分特性，NOOA 首次把它们组合在同一表面。

---

## 5. arXiv 分类精选（综述篇，与当日 arxiv-daily / arxiv-paper-check 无重叠）

### 5.1 Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility
**中文标题**：《推理 LLM 的测试时扩展：推理机制、评测与可复现性》

- **作者**：Mohsen Hariri, Weicong Chen, Nahal Shahini, Vikash Singh, Kai Ye, Amirhossein Samandar, Debargha Ganguly, Sreehari Sankar, Yanyan Zhang, Shouren Wang, Jerry Peng, Biyao Zhang, Michael Hinczewski, Vipin Chaudhary
- **机构**：Case Western Reserve University 等
- **会议**：arXiv:2608.04001（cs.LG, 2026-08-04）
- **背景与创新**：test-time scaling 一词已涵盖多种算法——单轨迹顺序扩展、采样完成后投票/验证聚合、未完成部分状态上的搜索——它们在统计结构、计算记账与失败模式上各不相同。把它们当作单一「budget」标量下可互换、或只报精度不报推理协议，使跨研究结果难以比较。本文沿**三条轴**系统化：①把测试时扩展形式化为自回归模型隐式前缀树上的 **budgeted inference**，区分**三种结构机制**（单轨迹顺序扩展 / leaf-level 扩展+终端归约 / prefix-level 扩展）；②把评估对象视为**整个推理系统**，区分端到端系统性能与候选池诊断，引入评估 profile（其坐标与简单泛函可恢复或界定常见 repeated-sampling 指标），并要求协议匹配的 compute/uncertainty 报告；③给出推理协议的**可复现性要求**，区分 exact replay 与 distributional reproducibility 及其所需工件。
- **实验结果**：在 broad-knowledge、symbolic-reasoning、competition-mathematics 基准上应用该原则；**汇编 20 亿+ 完整推理轨迹**对外发布，附逐步增强的 verifier 与 token 级信号。
- **对比前作**：对比既有 survey（多按算法枚举），本文给出统一前缀树机制框架 + 协议匹配报告规范，直接回应「同精度、不同预算口径不可比」的复现危机。

### 5.2 Video Generation Models as World Models: Efficient Paradigms, Architectures and Algorithms
**中文标题**：《视频生成模型作为世界模型：高效范式、架构与算法》

- **作者**：Muyang He, Hanzhong Guo, Junxiong Lin, Yizhou Yu
- **机构**：香港大学（HKU, Yizhou Yu 团队）
- **会议**：arXiv:2603.28489（eess.IV, v1 2026-03-30 / v3 2026-07-04）
- **背景与创新**：视频生成已能模拟复杂物理动力学与长程因果，被视为潜在世界模拟器，但「世界模拟的理论容量」与「时空建模的巨量计算成本」之间仍有鸿沟。本文以「效率作为世界建模的实际前提」为主线，提出**三维分类法**：高效建模范式（efficient modeling paradigms）、高效网络架构（efficient network architectures）、高效推理算法（efficient inference algorithms），并论证弥合效率鸿沟直接赋能自动驾驶、具身 AI 与游戏模拟等交互应用。
- **实验结果**：系统性综述（非单一实验）；维护公开 GitHub 文献库（Efficient-VWM-Survey）。
- **对比前作**：对比侧重生成质量/可控性的视频生成综述，本文把效率提升为第一类公民，论证「效率是把视频生成器演进为通用、实时、鲁棒世界模拟器的基本前提」，与当日 08-06 推理扩展/世界模型主题（§1 From Word to World、§3）形成从「文本世界模型」到「视频世界模型」的互补证据链。

---

## 6. 本期主题串讲：Agent 评测方法论为何集体转向

1. **从「任务完成」到「循环/长程行为」**：LoopsBench 把持续开发中的依赖 DAG、动态测试释放与回归义务引入评测；OmniaBench 把「困难子集」与十维能力分解用于污染缓解与诊断。两者共同标志着 Agent 评测从「一次正确」转向「长时间保持正确并自我纠正」。
2. **从「模型分数」到「研究级产出」**：影子评审（§3.2）证明工程能力与科研创造力可被清晰解耦——Agent 能做全部工程、但五个失败模式全部集中在「判断力 / 创造力 / 回退 / 资源 / 指令保持」上，与 08-05 Oxford F1/MTG 的「差距在过滤而非生成」互相印证（high confidence 交叉结论）。
3. **从「text 生成」到「world/state 建模」**：From Word to World（§1.1）用 next-state prediction 重述世界建模，给出「行为覆盖率 + 环境复杂度」的收益边界；视频世界模型综述（§5.2）则主张效率是实现该范式的物理前提——文本与视频两条线指向同一「LLM/生成模型作为模拟器」议程。

---

## 附：本期核验与去重记录

- **已覆盖、排除**：OMEGA（arXiv:2608.01315，KDD 2026 Research Track）已在 [08-05 arxiv-daily](../2026-08-05/arxiv-daily.md) 覆盖（Renmin U，GR 协作记忆库）；TmallGS / RaG / UniMVT / IDProxy / AgentGym2 / Agent World Model / HOBA / PlatformBid-BidFlow / RWML / Melo 均已在既有 digest 覆盖。
- **核验方式**：每篇候选均对 index.md、log.md、wiki/synthesis/** 全文 grep（arXiv ID + 关键词双查）后才收录。
