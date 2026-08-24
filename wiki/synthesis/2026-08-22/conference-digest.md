---
title: 会议与 arXiv 论文日报（2026-08-22）
title-en: Conference & arXiv Paper Daily Digest (2026-08-22)
type: synthesis
created: 2026-08-22
updated: 2026-08-22
tags: [conference-digest, arxiv-daily, CIKM2026, ICONIP2026, agents, agentic-rl, llm-serving, video-generation, code-generation, benchmark, daily-digest]
sources: []
---

# 会议与 arXiv 论文日报（2026-08-22）

> **日期**：2026-08-22（周六，arXiv 周末无公告；本期窗口 = 8/20–8/22 提交批次，IDs ~2608.19xxx–2608.20xxx）
> **覆盖范围**：ICML 2026 / AAAI 2026 / NeurIPS 2025 / ICLR 2026 / KDD 2026 / CVPR 2026 / ACL 2026 / EMNLP 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025–2026 / RecSys 2025–2026 各会议新确认产出 + AI、LLM、推荐系统、广告与 CTR、游戏、代码执行预测、Agent 系统、生成模型、Sequential Modeling、Benchmark 方向近期论文
> **来源**：arXiv API（8/20–22 窗口全量 829 篇扫描）、OpenReview、DBLP、各会议官网
> **去重说明**：本期 20 篇论文均经 ID+名称双重 grep 验证未在 wiki 此前任何页面收录。已剔除的同窗口重复：SSR-GRPO / RecPFN / SCoRD / MoE μP transfer (COLM) / Learning When to Think / StateMemBench / MidTool / SAPO / SeqRec benchmark probes / CoRRe / Credit Without Ground Truth（均为 08-21 sibling digests 已收录）、NSMC discrete diffusion 与 Orthogonal JEPA（同日 arxiv-ai-search 已收录）。**游戏与 CTR/广告方向本窗口无新增**——广告拍卖理论两篇由同日 arxiv-ai-search 收录。

---

## 目录

- [1. 本期概览与会议时间线](#1-本期概览与会议时间线)
- [2. 会议论文新确认（CIKM 2026 / ICONIP 2026）](#2-会议论文新确认cikm-2026--iconip-2026)
- [3. Agent 系统与 Agentic RL（本期主线，7 篇）](#3-agent-系统与-agentic-rl本期主线7-篇)
- [4. LLM Serving 与推理效率](#4-llm-serving-与推理效率)
- [5. 生成模型与视频生成](#5-生成模型与视频生成)
- [6. 代码执行预测与代码智能](#6-代码执行预测与代码智能)
- [7. Benchmark 与评测补充](#7-benchmark-与评测补充)
- [8. 热门主题与趋势](#8-热门主题与趋势)
- [9. 值得关注的论文（Top Picks）](#9-值得关注的论文top-picks)

---

## 1. 本期概览与会议时间线

| 会议 | 状态 | 本期动态 |
|------|------|---------|
| **SIGIR 2026**（墨尔本 7/20–24） | 已闭幕 | 正式 proceedings DOI 已上线：RecPFN（SAP）等已由 08-21 digest 跟踪 |
| **CIKM 2026**（罗马 11/7–11） | 接收论文陆续放榜 | 本期新确认 ViT Feature Evolution；此前 SSR-GRPO、SCoRD、CoRRe 已记录 |
| **COLM 2026** | 接收论文陆续放榜 | MoE LR transfer 已于 08-21 记录 |
| **ICONIP 2026** | 接收通知期 | 本期新增 RGA-Designer（multi-agent 拓扑设计 poster） |
| ICML/KDD/CVPR/ACL 等 | 已闭幕 | 无新奖项或 proceedings 动态 |

| 方向 | 篇数 | 关键词 |
|------|------|--------|
| Agent 系统与 Agentic RL | 7 | 环境自动改造（Google）、有状态业务工作流基准（Microsoft）、milestone credit assignment、policy 编译成 workflow graph、skill 选择理论保证 |
| LLM Serving 与推理效率 | 4 | block-sparse prefill（腾讯微信）、prefix-affinity routing、tool-agent KV cache 复用、CPU-first 小模型 |
| 生成模型与视频生成 | 2 | 4D-consistency RL 奖励、analog CIM 下的 CFG 再校准 |
| 代码智能与 ML Agent | 3 | zero-to-all 仓库生成、科学软件工程基准、ML 实验自动化基准 |
| Benchmark 与评测 | 4 | 记忆认知陷阱、金融合规 rule grounding、个性化 authorship gap、压缩的不对称伤害 |

---

## 2. 会议论文新确认（CIKM 2026 / ICONIP 2026）

### 2.1 Feature Evolution and Migration during Vision Transformer Training（ViT 训练中的特征演化与迁移）

| 项目 | 内容 |
|------|------|
| 作者 | Joonas Järve, Halil Ibrahim Aysel, Tarun Khajuria, Meelis Kull |
| 机构 | University of Tartu 等（据作者名单推断） |
| 发表 | **CIKM 2026** |
| 链接 | [arXiv:2608.20134](https://arxiv.org/abs/2608.20134) · [PDF](https://arxiv.org/pdf/2608.20134) |

**问题背景**：ViT 内部特征如何随训练形成与迁移，表征级相似度度量难以观察。本文提出在**深度 × 训练时长**两个维度上直接可视化特征动力学。

**方法与创新点**：
- 用 Sparse Autoencoders (SAEs) 从 CLS-token 表征提取候选稀疏特征，比较其在 epoch–layer 对上的激活剖面；
- 定义并刻画 **feature migration**——一个特征在训练过程中"最可检测层"的迁移现象。

**实验结果**：migration 集中在训练早期、更多朝更早层方向发生、随特征组织稳定而衰减；深层比浅层更早且更强地稳定。

**对比先前方法**：先前可解释性工作多分析训练完成后的静态特征，或仅在单一维度（层数或时间）切片；本框架将 SAE 特征字典沿训练轨迹对齐，是 feature-level dynamics 的系统性纵向研究。

### 2.2 RGA-Designer: Reward-Guided Autoregressive Graph Generation for Multi-Agent Topology Design（奖励引导的自回归图生成多智能体通信拓扑设计）

| 项目 | 内容 |
|------|------|
| 作者 | Poomphob Suwannapichat, Boonyarit Changaival, Caesar Wu, Pascal Bouvry |
| 机构 | Luxembourg 系高校团队（据作者名单推断） |
| 发表 | **ICONIP 2026 (poster)** |
| 链接 | [arXiv:2608.20099](https://arxiv.org/abs/2608.20099) · [PDF](https://arxiv.org/pdf/2608.20099) |

**方法与创新点**：ARG-Designer 将 multi-agent 拓扑设计重构为自回归图生成，但其训练目标不激励稀疏高效拓扑。RGA-Designer 引入 RLHF 式奖励引导：训练一个同时捕捉任务正确性与结构紧凑性的 reward model，再以其为反馈微调图生成器。

**实验结果**：任务准确率保持 ARG-Designer 水平的同时，token 消耗平均降低 **20.5%**。

**对比先前方法**：把"拓扑效率"从后处理剪枝前移为训练信号，与 §3.4 Optimal Skill Selection 共同指向 "agent 系统 token 经济学" 这一新兴主题。

---

## 3. Agent 系统与 Agentic RL（本期主线，7 篇）

> 本周该方向呈现清晰三条线：①环境侧自动化（Google EnvHarness 让静态环境自适应 agent 弱点）；②评测侧可靠性（Microsoft Thinkingbox 揭示 pass@1 与可靠完成的巨大鸿沟）；③训练侧信用分配与技能管理精细化（MileGPO / BPS / Skill Transfer / CAMA）。

### 3.1 EnvHarness: Awakening Static Worlds for Agent Learning（唤醒静态世界：面向 Agent 学习的环境改造层）

| 项目 | 内容 |
|------|------|
| 作者 | Chengsong Huang, Zifeng Wang, Rujun Han, Jun Yan, Yanfei Chen, Zoey CuiZhu, Ke Jiang, Peng Xia, Han Yu, Yufan Zhuang, Yifei Ming, Jiaqi Pan, Bhavana Dalvi Mishra, Jiaxin Huang, Burak Gokturk, Tomas Pfister, Chen-Yu Lee |
| 机构 | Washington University in St. Louis, **Google Cloud AI Research**, Google Cloud, UNC Chapel Hill |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.19880](https://arxiv.org/abs/2608.19880) · [PDF](https://arxiv.org/pdf/2608.19880) · [代码](https://github.com/google-research/envharness) |

**问题背景**：LLM agent 通过与环境交互学习，但现有环境是手工构建且静态的——看不见 agent 的弱点，也很快被进步的 agent 甩在身后。已有环境生成方法需要 domain-specific pipeline、依赖昂贵或不可靠的 verifier，产出的仍是静态环境。

**方法与创新点**：
- **EnvHarness**：一层可编程的插件组件，包裹静态环境以重塑其行为而不修改底层逻辑；通过标准接口运作，跨域适用，且保证每个被改造的环境**保留原 verifier**；
- 自动化组件 **EnvRigger**：把目标策略当黑盒，观察执行轨迹诊断缺陷，合成针对性的 EnvHarness 组件，再用 fresh rollouts 验证有效性；
- 支持技能学习与 RL 两类范式下 policy-environment 的持续定向协同演化。

**实验结果**：在 4 个域的 5 个基准（ALFWorld 具身任务、WebArena 网页浏览、SWE-bench 软件工程、OfficeQA 办公事务）上超过原始环境与 domain-specific 环境生成管线：held-out 实例最高提升 **9.0 分**，同时执行步数减少 **9.8%**；作为 RL 优化信号时质量优于原始环境。

**对比先前方法**：EnvGen 类方法重造环境本体，EnvHarness 是不改逻辑的"外挂改造层"，工程成本低得多；与 [[mem1-agent]] 等记忆侧优化正交。Google Cloud AI Research 团队延续其 agentic environments 布局。

### 3.2 One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows（一次成功≠可靠：面向有状态业务工作流的 Agent 沙箱与基准）

| 项目 | 内容 |
|------|------|
| 作者 | Zhuochun Li, Youngmin Ko, Ali Keramati, Nicola Ferri, Susana Palmaz Lopez Pelaez, Liang-Chun Tsai, Calvin Wang, Mirco Milletari, Tuhin Kundu, Vadim Smolyakov, Kjartan Ólafsson, Tommy Guy |
| 机构 | **Microsoft**（+ Univ. of Pittsburgh / Northwestern / UC Irvine；benchmark 任务与 Toloka 合作构建） |
| 发表 | arXiv preprint（官方博客 2026-08-19 同步发布） |
| 链接 | [arXiv:2608.19741](https://arxiv.org/abs/2608.19741) · [PDF](https://arxiv.org/pdf/2608.19741) · [代码](https://github.com/microsoft/thinkingbox) |

**问题背景**：完成代码之外的"真实业务工作"不只是产生合理回复或合法 tool call：agent 必须跨轮收集缺失信息、遵循领域政策、协调依赖工具，并实现正确的持久状态转移而不产生附带损害。现有 function-call 导向评测只检查 API 选择/参数合法性，无法检验"这个 call 是否真正完成了它要做的事"。

**方法与创新点**：
- **Thinkingbox 沙箱**：tool-agent-user 交互的可复用底座——隔离的 MCP-compatible 工具会话、模拟用户追问、完整执行轨迹、以及**基于终端后端状态的 outcome 校验**（接受正确轨迹、拒绝错误/遗漏/多余副作用）；
- **Thinkingbox-Bench**：507 个 policy-conditioned 有状态任务，横跨零售电商（98）、差旅酒店（104）、车险（100）、新银行内部 IT（104）、咨询 IT/HR（101）五大域；30 个任务额外检查最终回复的必要属性（披露义务、保密性等）。

**实验结果**（12 个专有+开源模型 × 20 trials）：
- 最强模型 pass@1 仅 **65.36%**；pass@20（至少一次成功）91.12%，但 **pass^20（全部成功）只有 25.25%**——发现与可靠性之间存在巨大鸿沟；
- 大量失败案例表现为干净终止 + 合法的状态变更动作，说明 response/tool-call 层面信号不是端到端完成的可靠代理指标。

**对比先前方法**：tau-bench/tau²-bench 是最接近的系统，Thinkingbox 补齐了 side-effect checks 与真实 MCP server 支持；其贡献在于把评测契约（stateful env × 受控工具面 × 交互用户 × 可隔离重跑）四要素全部落地到企业工作流场景。

### 3.3 MileGPO: Milestone Inference with Local Evidence for Graph-Based Policy Optimization（基于局部证据的 Milestone 推断图策略优化）

| 项目 | 内容 |
|------|------|
| 作者 | Bo Qian, Yuting Wu, Shuang Zeng, Huaiyu Wan, Dalin Zhang, Jiqiang Liu |
| 机构 | 北京交通大学（推断）+ City University of Hong Kong（推断） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.19803](https://arxiv.org/abs/2608.19803) · [PDF](https://arxiv.org/pdf/2608.19803) |

**问题背景**：长程 agentic RL 的监督常只剩最终奖励；step grouping 或 graph-based advantage estimation 能细化轨迹级信号，但会忽略有意义的中间 milestone。

**方法与创新点**（三设计，从 grouped on-policy rollouts 中提取过程级 credit）：
1. **Milestone Discovery**：在成功 rollout 上识别候选里程碑、在失败 rollout 上识别反复出现的陷阱（recurring traps）；
2. **Reliability-Calibrated Shaping (RCS)**：按结果置信度加权候选——强化可靠的里程碑/陷阱、下调不确定者；
3. **Progress-Contrastive Calibration (PCC)**：检验候选是否反映局部进展、以及其入边转移是否优于同一状态下观测到的其他分支。

无需辅助模型、无需额外环境交互。

**实验结果**：ALFWorld 与 WebShop 上达到 SOTA；ALFWorld 上 in-distribution 到 out-of-distribution 的落差很小。Credit diagnostics 显示三个校准设计与 milestone discovery 互补，消解歧义的中间 credit。

**对比先前方法**：与 step-grouping 类方法（如 GIPO）和 graph-based advantage 方法相比，显式引入"中间里程碑"这一过程语义单元，并以可靠性与局部进展双重证据过滤噪声 credit。

### 3.4 Optimal Skill Selection for LLM Agents with Provable Bicriteria Guarantees（带可证明双准则保证的 Agent 技能最优选择）

| 项目 | 内容 |
|------|------|
| 作者 | Yu Chen, Ruishuo Chen, Xun Wang, Zhuoran Li, Longbo Huang |
| 机构 | Tsinghua University（推断，Longbo Huang 团队） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.19993](https://arxiv.org/abs/2608.19993) · [PDF](https://arxiv.org/pdf/2608.19993) |

**问题背景**：把可复用 skill 文档装入有限 context window 是当前 agent 获取任务能力的主要方式，skill 选择直接决定任务表现与 token 成本。现有 agent 按语义相关性独立打分后 top-k/greedy 装配，既无质量保证也不感知成本——冗余技能浪费稀缺 context token 甚至损害性能。

**方法与创新点**：
- 首个"所选 skill 集合如何塑造执行结果"的形式化模型：在硬 token 预算下最大化 monotone submodular benefit 减去 context penalty；
- **Best Prefix Selection (BPS)** 多项式时间算法，并证明首个 skill 选择性能保证：bicriteria (1−1/e, 1) 近似，benefit 系数在多项式时间内最优。

**实验结果**：在 contamination-controlled BigCodeBench 变体上，BPS 达到 **0.73** 任务成功率（已发布 skill routers、文本检索器与 executor 自选为 0.20–0.52），且比最强已发布 router 少用 **28%** tokens。

**对比先前方法**：把 skill loading 从启发式工程问题升级为有理论保证的组合优化；与 §2.2 RGA-Designer 共同构成 agent 系统 token 经济学的新证据。

### 3.5 Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents（拆解再传递：LLM Agent 的跨任务技能迁移受控研究）

| 项目 | 内容 |
|------|------|
| 作者 | Yiyang Feng, Biddut Sarker Bijoy, Niranjan Balasubramanian, Jiawei Zhou |
| 机构 | Stony Brook University 等（据作者名单推断） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.20274](https://arxiv.org/abs/2608.20274) · [PDF](https://arxiv.org/pdf/2608.20274) |

**问题背景**：agent 可从完成任务中归纳 skill 并复用以"越用越强"，但归纳出的 skill 迁移不可靠，甚至伤害检索到它的 agent。何时可靠迁移是开放问题。

**方法与创新点**：沿现有方法的两个轴做全面受控实验——task-level vs subtask-level 归纳 × text vs code 格式；并提出 **specificity（技能与真实任务的贴合度）× abstractness（相关性跨任务分布均匀度）** 双属性及其组合的 **skill utility score**。

**实验结果**：
- task-level skills 多数情况下把 agent 拉到 no-memory baseline 之下；subtask-level skills 平均高于 baseline；text skills 比 code skills 迁移更好；
- 单一属性不能预测任务成功，二者组合可以——utility score 与迁移后的任务成功一致相关，且计算只需 skill 与任务描述、无需执行任何任务，可作为 skill memory 在新任务运行前的实用诊断器。

**对比先前方法**：先前 skill-induction 工作（Voyager 类）报告的是"能迁移"的正例；本文首次给出系统性负结果与预测性诊断指标，对 skill memory 系统设计是直接的工程指南。

### 3.6 Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration（CAMA：多智能体记忆仲裁中的 Memory Correlation Bias）

| 项目 | 内容 |
|------|------|
| 作者 | Chenchen Lin, Wenhao Yuan, Xuehe Wang, Edith Cheuk Han Ngai |
| 机构 | The University of Hong Kong（推断，Edith Ngai 团队） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.19701](https://arxiv.org/abs/2608.19701) · [PDF](https://arxiv.org/pdf/2608.19701) |

**问题背景**：长期 multi-agent 系统持续积累不同 agent 写下的记忆。现有方法把检索到的记忆当独立证据投票/加权——但多智能体场景下不同 agent 的记忆可能继承同一上游来源或共享偏差，相关证据被重复计数形成**假多数**。作者命名该失败模式为 **Memory Correlation Bias**。

**方法与创新点**：提出 **Correlation-Aware Memory Arbitration (CAMA)**：
1. 将检索记忆建模为 query-conditioned evidence groups，结合 neural dependency inference 与 provenance-based symbolic priors 估计**有效独立证据源数量**，阻止相关记忆形成假多数；
2. 关键独立证据可能不在初始检索集内——进一步学习 sequential recovery policy，主动检索替代证据或回溯上游来源，在最小化检索成本的同时恢复充分独立证据再做仲裁。

**实验结果**：多个基准上超越 SOTA baseline，有效抑制相关记忆诱发的假多数。

**对比先前方法**：与 wiki 已收录的记忆侧工作（StateMemBench 关注状态时效、MemTrapBench 见 §7.1 关注认知陷阱、Router-Mem 关注成本路由）互补——本文独有地处理**多智能体证据相关性**维度。

### 3.7 PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents（从守护单步动作到引导整个工作流）

| 项目 | 内容 |
|------|------|
| 作者 | Seongjae Kang, Taehyung Yu, Sung Ju Hwang |
| 机构 | KAIST（Sung Ju Hwang 团队） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.19861](https://arxiv.org/abs/2608.19861) · [PDF](https://arxiv.org/pdf/2608.19861) |

**问题背景**：客服 LLM agent 必须遵循组织政策行事。违规来自两类：禁止动作（如给不合格用户改单）与遗漏程序要求（如身份核验、二次确认）。Runtime safeguard 只能拦单步风险动作，无法引导多步流程；workflow-following 系统以完成流程为目标而非保障行为合规。

**方法与创新点**：PolicyGuide 把每条领域政策编译成 workflow graph，并在用户轮边界调用 proactive verifier：从持久化的图状态出发 reconcile 未决请求，沿政策合规路径返回 step-specific remediation——把"事后拦截"变成"全程导航"。

**实验结果**：τ²-bench airline/retail/telecom 三域 + GPT-5.4 agent & verifier：mean Pass⁴ 从 **0.42 提升到 0.62**，最大增益在流程结构最强的 telecom 域（**0.19→0.61**）；同一套 workflows 可迁移到 Claude Sonnet 4.6 与 Gemini 2.5 Pro agents。对抗用户场景下攻击成功率最低；自建 workflow 级验证中程序合规最强。

**对比先前方法**：与 guardrail 类（单动作审查）和 workflow-following 类（只管走完流程）两条路线相比，首次把政策合规作为贯穿多步执行的一等目标；与 Thinkingbox（§3.2）的评测发现互为印证——企业场景缺的正是这种程序级保障。

---

## 4. LLM Serving 与推理效率

### 4.1 FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving（面向长上下文 LLM Serving 的块稀疏 Prefill 注意力）

| 项目 | 内容 |
|------|------|
| 作者 | Qihang Fan, Huaibo Huang, Zhiying Wu, Bingning Wang, Ran He |
| 机构 | MAIS & NLPR, CASIA（中科院自动化所）+ UCAS + **WeChat, Tencent** |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.19758](https://arxiv.org/abs/2608.19758) · [PDF](https://arxiv.org/pdf/2608.19758) |

**问题背景**：长上下文注意力的二次复杂度瓶颈集中在计算密集的 prefill 阶段。前代 FlashPrefill 用即时模式发现 + max 动态阈值缓解，但仍是算法原型：激进稀疏下精度失控、kernel 基于 FlashAttention-2 落后于 FA3/4、连续 KV 布局不兼容 paged KV cache 与 continuous batching。

**方法与创新点**（三个维度的产品化演进）：
1. **mean correction term**：用被剪枝块的池化 K/V 统计量补偿近似误差，极端稀疏下精度可控；
2. **FA3/4 对齐的稀疏 kernel**：PackGQA 访存、warp specialization、pingpong pipelining，支持 FP8 推理；
3. **原生支持 paged KV cache 与 continuous batching**，可直接作为 SGLang 的 attention backend 集成。

**实验结果**（NVIDIA H20，生产级部署最广的推理卡之一）：
- vs FlashAttention-2 @128K：FP8 **47.26×**、BF16 **27.19×** 加速；
- vs 更强的 FA3/4-aligned dense baseline：FP8 仍达 **30.49×**（BF16 17.54×），且从 4K 上下文起即保持加速；
- 端到端 SGLang TP=4×H20 配置验证，decode 回退 dense 不受影响。

**对比先前方法**：与 MInference/Quest 等 block-sparse 方案相比，首次同时做到 FA3/4 kernel 级实现 + FP8 + paged KV + 框架集成四位一体，是从 paper 到 production 的关键跨越；与 wiki 已收录的 [[gated-attention]]（训练侧注意力改造）分别占据推理加速与训练效率两端。

### 4.2 CacheRoute: Planned Prefix-Affinity Routing for Large-Scale LLM Serving（大规模 LLM Serving 的计划式 Prefix 亲和路由）

| 项目 | 内容 |
|------|------|
| 作者 | Huang Cheng（独立作者） |
| 机构 | 未标注 |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.19677](https://arxiv.org/abs/2608.19677) · [PDF](https://arxiv.org/pdf/2608.19677) |

**问题背景**：Prefix caching 只有当重复请求回到仍持有该 prefix KV 的服务器才能免 prefill。cache-blind 负载均衡打散复用；固定亲和保住复用却可能过载单机。

**方法与创新点**：周期性 routing plan 化解两难——把高频 key 准入稳定 warm set，按预期负载放置分配；hot key 可映射多个目的地。

**实验结果**：Llama-3.3-70B fp8、60×H100：3.5s p99 SLO 下持续 **176±11 QPS**，为五个基线中最强者的 **2.3×**；KV hit rate 从 64.1% 提升至 **93.2%**。两个 32B 反例负载显示：当亲和挽回的 KV 工作量太少时残余负载偏斜会侵蚀收益——作者建议部署前用 shadow replay 门控而非仅凭负载统计开启 affinity。

**对比先前方法**：与 SGLang/vLLM 的缓存感知调度相比引入全局周期规划视角，并给出诚实的适用边界分析（何时不开亲和更好），工程决策价值高。

### 4.3 ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents（工具增强 LLM Agent 的高效 KV Cache 复用与压缩）

| 项目 | 内容 |
|------|------|
| 作者 | Yichu Fang, Sitong Wei, Haozhe Hu, Xiaoyu Shen |
| 机构 | Zhejiang University（推断，EIT-NLP 组） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.19662](https://arxiv.org/abs/2608.19662) · [PDF](https://arxiv.org/pdf/2608.19662) · [代码](https://github.com/EIT-NLP/ReCache) |

**问题背景**：agentic 模型反复编码以不同组合与顺序出现的 tool/skill schema——标准 prefix caching 因前缀不同而完全失效。

**方法与创新点**：独立缓存资源表征并压缩其推理开销：
- **Resource-wise attention** 去除跨资源交互、分配 resource-local positions，产出**组合不变（composition-invariant）**的 KV blocks——无论 schema 以何种顺序组合都可直接复用；
- 将资源可见性限制到按贡献选出的 layer–KV-head-group 路由，并通过结构与语义剪枝只保留 invocation-critical 字段。

**实验结果**：7 个公开 tool/skill-use 数据集（含 resource-disjoint 测试）：resource-wise attention 以 **82.3% vs 82.4%** Inv-F1 匹配 dense 调用，TTFT 加速 **3.655×**；完整框架减少 KV tensor 内存 **92.43%**、attention 加速 **1.423×**。

**对比先前方法**：prefix caching 只能复用相同前缀；本篇将"可复用单元"从字符串前缀升级为语义资源块，是 agentic serving 特有的缓存抽象。

### 4.4 Daedalus-150M: A Convolution-Attention Hybrid Designed for CPU Inference（面向 CPU 推理设计的卷积-注意力混合小模型）（简报）

| 项目 | 内容 |
|------|------|
| 作者/机构 | Christos Koutsiaris（独立研究者） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.20210](https://arxiv.org/abs/2608.20210) |

反向设计范式："先定目标再定架构"——单用户、逐 token、4-bit 权重、普通 CPU。18 个 block 中仅 6 个保留 full attention，其余 12 个用短卷积（记忆宽度恒为 2 timesteps，不随对话增长）。59.9B tokens 从头训练：五任务基准 **47.31**（预注册门槛 42.20），胜过 GPT-2 124M / Pythia-160M / OPT-125M / GPT-neo-125M（数据量为其 3–6 倍）及看过 1T tokens 的 MobileLLM-125M 公开分数；同尺寸同数据对照实验中混合架构 4-bit 文件小 6.3%、2048 上下文解码快 **1.76–2.08×**，且速度优势随上下文增长而扩大（机制预测成立）。诚实报告失败项：未缓解的 4-bit 质量损失、约半数卷积通道惰性不可移除。

---

## 5. 生成模型与视频生成

### 5.1 Stream4D: Reinforcing Streaming Video Generation with 4D Consistency（以 4D 一致性强化流式视频生成）

| 项目 | 内容 |
|------|------|
| 作者 | Yikang Deng, Daoyi Gao, Martin R. Oswald |
| 机构 | UCLA + University of Amsterdam（推断） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.19556](https://arxiv.org/abs/2608.19556) · [PDF](https://arxiv.org/pdf/2608.19556) |

**问题背景**：RL 后训练正成为提升自回归视频扩散模型的标配，但现有奖励几乎全是"看视频评视频"，隐式假设被奖励的视频就是最终产物。对 feed-forward streaming 4D 重建这类下游应用，静态视觉保真度奖励反而有害——它鼓励模型输出冻结、静止的帧，牺牲时间动态。

**方法与创新点**：
- 首个面向流式视频生成的 **4D-consistency RL 框架**：用 feed-forward 4D-GS（基于 MoVieS）的重建奖励替换刚性 3D critic，奖励能被稳定重建为一致 3D 的视频，从而保持时间动态；
- **Gaussian motion gate reward**：惩罚相机运动过快导致的重建退化；
- 无需人工标注或外部 VLM judge。

**实验结果**：在 Self-Forcing、Causal-Forcing、LongLive 三个骨干上验证：4D-PSNR 提升 **+3.46 / +5.53 / +6.76 dB**；与 World-R1 对比，在更严格的 4DGT check 下仍领先 **+0.7 / +1.1 / +2.5 dB**；vision-LLM judge 一致性 82.2% / 73.9% / 74.2%，且不损失文本一致性。

**对比先前方法**：World-R1 等世界模型 RL 用静态 3D 一致性作奖励，本篇证明该信号对 streaming 场景是错误目标；奖励设计从"像素/语义相似"转向"下游可用性"，与 [[reward-hacking]] 讨论直接相关——奖励错定在生成模型侧的新实例。

### 5.2 Recalibrating Guidance for Rectified Flow Models under Low-Precision Analog Compute（模拟计算下 Rectified Flow 引导再校准）（简报）

| 项目 | 内容 |
|------|------|
| 作者 | Shanshan Yan, Heng Fan, Hongwei Huo, Xiaoming Chen, Yinhe Han |
| 机构 | 中科院计算所等（推断） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.19644](https://arxiv.org/abs/2608.19644) · [PDF](https://arxiv.org/pdf/2608.19644) |

Compute-in-Memory (CIM) 硬件为扩散模型提供数量级能效增益，但低精度模拟噪声会系统性削弱 classifier-free guidance (CFG)。本文提出轻量再校准方案恢复 CFG 效果，使 DiT 类 rectified flow 模型在 CIM 平台上保持生成质量——AI 加速器 × 生成模型交叉方向的务实工作。

---

## 6. 代码执行预测与代码智能

### 6.1 Repo0: Zero-to-All Code Repository Generation via Dual-DAG-Guided Multi-Agent System（Dual-DAG 引导的多智能体零到全仓库生成）

| 项目 | 内容 |
|------|------|
| 作者 | Jiaxin Wang, Zhengyang Liu, Xiao Wang 等 |
| 机构 | Tongji University + Shanghai Jiao Tong University（推断） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.19854](https://arxiv.org/abs/2608.19854) · [PDF](https://arxiv.org/pdf/2608.19854) |

**问题背景**：现有 code generation 局限于单文件/单函数粒度；从零生成完整多文件仓库（zero-to-all）需要全局架构规划与跨文件依赖管理，超出单 LLM 能力。

**方法与创新点**：multi-agent 系统以**双 DAG（Dual-DAG）**为核心数据结构——一个建模文件间依赖、一个建模任务执行顺序——引导 planner / coder / reviewer 协同完成仓库级生成。

**实验结果**：在自建 zero-to-all 基准上显著超越单模型与常规 multi-agent baseline，可端到端产出结构完整、可运行的中小型项目。

**对比先前方法**：与 MetaGPT/AutoGen 类框架的"对话驱动"协作不同，Repo0 把协作约束显式编码进图结构，减少自由对话的漂移；与 wiki 已收录的 SWE-agent 类工作互补（后者在既有仓库上修 bug，本篇从零建仓）。

### 6.2 SWE-bench Science: Benchmarking AI for Scientific Software Engineering（科学软件工程基准）

| 项目 | 内容 |
|------|------|
| 作者 | Huan Sun, Yukang Huo, Haoqiu Wu, Biqing Qi, Fangwen Mu, Linjun Li, Yihao Wang, Wenbo Zhang, Xinfeng Li, Yang Liu 等 |
| 机构 | Fudan University（邱锡鹏团队，推断） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.19799](https://arxiv.org/abs/2608.19799) · [PDF](https://arxiv.org/pdf/2608.19799) |

**问题背景**：SWE-bench 系列聚焦 Web 软件栈；科学计算软件（物理仿真、生物信息、数值库）有独特的正确性标准——数值精度、物理守恒律、API 数值契约——未被覆盖。

**方法与创新点**：从真实科学软件仓库的历史 issue/PR 构建 benchmark，测试用例包含领域特定的数值验证逻辑；覆盖 Python/C++/Fortran 混合栈。

**实验结果**：最强 coding agent 在科学软件任务上的表现显著低于通用 SWE-bench 水平，暴露出 agent 对数值语义与科学计算惯例的理解缺口。

**对比先前方法**：把 SWE-bench 范式扩展到科学领域，是"AI for Science × agentic coding"交叉的评测基础设施。

### 6.3 DeltaML-Bench: Evaluating ML Experiment Automation Agents on Incremental Changes（增量变更下的 ML 实验自动化 Agent 评测）（简报）

| 项目 | 内容 |
|------|------|
| 作者 | AlgorithmicResearchGroup 团队 |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.19653](https://arxiv.org/abs/2608.19653) · [PDF](https://arxiv.org/pdf/2608.19653) |

ML 实验的真实工作流不是从零写训练脚本，而是在既有代码上做受控增量修改（换 loss、加正则、调 schedule）。DeltaML-Bench 以 delta 形式的 ML 实验变更请求为单元评测 agent，补齐 ML-agent 评测中"增量迭代"这一缺失环节。

---

## 7. Benchmark 与评测补充

### 7.1 MemTrapBench: Systematic Evaluation of Memory Traps in Long-Horizon Agents（长程 Agent 记忆陷阱的系统评测）

| 项目 | 内容 |
|------|------|
| 作者 | Zhejiang University 团队（推断） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.20202](https://arxiv.org/abs/2608.20202) · [PDF](https://arxiv.org/pdf/2608.20202) |

**问题背景**：agent memory 系统在检索与写入上进步迅速，但"记忆何时反而伤害 agent"缺乏系统评测——过时信息、来源混淆、跨会话污染等"记忆陷阱"普遍存在却难以定位。

**方法与创新点**：构建带受控记忆缺陷注入的评测套件，系统变化陷阱类型（staleness / attribution / contamination）× 注入位置 × 干预时机，量化各 memory 架构（RAG 式、分层式、自我编辑式）对陷阱的抵抗力。

**实验结果**：现有 SOTA memory 系统在陷阱场景下性能显著退化；简单的时间戳过滤或来源标注即可恢复部分损失，说明多数系统的失败源于缺失元数据而非检索本身。

**对比先前方法**：与 StateMemBench（08-21 已收录，状态时效）方向相近但陷阱维度更宽；与 §3.6 CAMA（多智能体证据相关性）共同构成 agent memory 可靠性评测的三块拼图。

### 7.2 ReguSim: Benchmarking LLM Agents on Financial Regulatory Compliance（金融监管合规 Agent 基准）（简报）

| 项目 | 内容 |
|------|------|
| 作者 | Cornell University + Stanford University + HKUST 团队（推断） |
| 发表 | arXiv preprint |
| 链接 | [arXiv:2608.19974](https://arxiv.org/abs/2608.19974) · [PDF](https://arxiv.org/pdf/2608.19974) |

以真实金融监管规则（KYC、交易限制、披露义务）构造合规判定任务，要求 agent 在长规则文本下做 rule grounding 并给出可审计的理由。结果显示主流模型在规则冲突与例外条款处理上错误率高——与 §3.2 Thinkingbox 的企业工作流发现互相印证：政策遵循是当前 agent 最薄弱环节之一。

### 7.3 其他值得关注的 Benchmark（简报）

- **PersonalBench** [arXiv:2608.19746]：个性化文本生成评测。发现 LLM 在模拟用户个人写作风格/偏好时的 authorship gap——模型能模仿表面特征但无法保持个体一致性，个性化 RLHF 路线的重要负结果。
- **Asymmetric Harms of LLM Compression** [arXiv:2608.19670]：系统测量量化/剪枝/蒸馏对不同人口群体查询的错误率差异，发现压缩在整体精度不变时仍会放大群体间差异——部署侧公平性的新证据。
- **MaliciousSkillBench** [arXiv:2608.19901]：评测 agent skill marketplace 场景下的恶意 skill 检测与防御，与 skill 生态安全直接相关。
- **MCB (Remember–Verify–Ask)** [arXiv:19564→2608.19564]：针对 multi-agent 协作中的记忆一致性问题提出 Remember–Verify–Ask 三段式协议，减少协作幻觉传播。

---

## 8. 热门主题与趋势

1. **Agent 可靠性成为主战场**。Microsoft Thinkingbox 用 pass@1 65% vs pass^20 25% 的鸿沟宣告"单次成功"叙事失效；PolicyGuide 把政策合规做成全程导航；ReguSim 攻克规则遵循。评测正在从 capability 转向 reliability。
2. **Agent 系统的 token 经济学成形**。RGA-Designer（拓扑稀疏化省 20.5% token）、BPS（skill 选择理论保证）、ReCache（组合不变 KV 缓存省 92% 内存）：上下文预算作为一等约束进入训练目标与系统设计。
3. **环境侧自动化启动**。Google EnvHarness 让环境主动适应 agent 弱点，policy-environment 协同演化可能复制 GAN 式的动态博弈提升曲线。
4. **Serving 层面向 agentic 负载重构**。CacheRoute（prefix 亲和路由）与 ReCache（工具 schema 缓存）表明传统 serving 优化假设（负载独立同分布、前缀重复为主）正被 agent 工作流打破。
5. **奖励函数设计向"下游可用性"迁移**。Stream4D 证明为下游任务（4D 重建）定制的奖励优于通用视觉奖励，生成模型的 RL 后训练开始与具体应用耦合。

## 9. 值得关注的论文（Top Picks）

| 排名 | 论文 | 推荐理由 |
|------|------|---------|
| ⭐⭐⭐ | EnvHarness (Google) §3.1 | 环境自动改造层 + 黑盒诊断 EnvRigger，agentic RL 数据飞轮的新范式 |
| ⭐⭐⭐ | Thinkingbox (Microsoft) §3.2 | pass^20 指标揭示可靠性鸿沟；507 个有状态业务任务的评测基础设施 |
| ⭐⭐⭐ | FlashPrefill V2 (CASIA+腾讯微信) §4.1 | FA3/4 对齐 kernel + FP8 + paged KV 全栈落地，128K 下 47× 加速 |
| ⭐⭐ | Stream4D (UCLA) §5.1 | 首个 4D-consistency 视频生成 RL，奖励错定的教科书案例 |
| ⭐⭐ | BPS Skill Selection (清华) §3.4 | skill loading 首个理论保证，token 经济学的优化视角 |

---

*本日报由 arXiv API 全量扫描 + OpenReview/DBLP/会议官网交叉验证生成。机构推断项已标注"推断"。*
