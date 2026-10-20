---
title: "LLM Tech Report Digest — 2026-10-20"
type: synthesis
created: 2026-10-20
updated: 2026-10-20
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, mistral, timestral, time-series, microsoft, guardian-agents, project-perception, anthropic, metr, embedded-evaluation, minimax, inception, mercury-3, governance, agent-security, silent-window, daily-digest]
---

# LLM Tech Report Digest — 2026-10-20

> **窗口判定：2026-10-19 → 2026-10-20（周一→周二）。本期为「静默 + 治理」日：19 家目标机构窗口内 0 份新技术报告 / 系统卡 / 模型卡**。窗口内唯一的机构级一手发布是 **Microsoft 安全博客《Securing the agentic insider》（10-19）**——推出 **Guardian Agents** 监控企业内部 AI agent，并抛出 "**frontier models, regardless of their origin, cannot be trusted**" 的官方判断（安全/治理层，非模型发布）。另有两笔补录：**Mistral Timestral（10-15 一手发布，10-16→10-19 二手报道密集，全库此前 0 收录、连续漏收 4 期）**——Mistral 首个时序基础模型家族（5M–209M，CPU 推理）；**Anthropic METR 嵌入式评估（10-15 一手已录 10-16 期）在 10-18/19 迎来 FT / Ars Technica / TechTimes 广泛二次报道**（新增 6 名评估员、三层访问体系、Altman 称 OpenAI 将跟进等细节，本期交叉引用补细节）。**arXiv：Monday 10-19 block（1,162 标题）已由 10-19 期逐一扫描 = 0 篇目标机构技术报告**；export API 持续空响应 → 以 title "Technical Report" 检索 top-50 复核，最新至 10-16（Cortex `2610.24255` / MOSS-Image `2610.23374` / Xiaomi-Lens-0 `2610.23279` 均非目标机构，前两篇 10-19 期已排除）——**窗口内 0 篇目标机构 arXiv 报告**。非目标机构同日新卡：**MiniMax M3.1 Flash（10-19）**、**Inception Mercury 3（10-19，扩散语言模型）**、Hugging Face Apertus 1.5、Disney 吸收 Character.AI 团队。

> **本期主线：① "模型静默、控制层喧哗"——窗口内目标机构的全部实质动作都发生在模型之外的安全/治理层**：微软把"企业内部 agent = 内部威胁"产品化（Guardian Agents + Defender 影子 agent 检测 60 类，含 Claude Code/Codex/OpenClaw），Anthropic 的 METR 嵌入式评估获得跨媒体二次传播并披露 6 人/三层访问细节，与 10-19 期已录的公共利益基金共同构成 IPO 前夜的"治理资产包"；**② Mistral 用 209M 时序模型补上"非 LLM 产品线"的空窗**——GIFT-Eval/TIME/fev-bench 零样本预训练第一（**Mistral 自报口径**）、CPU 10–140ms、Modified MIT（月营收 >$20M 需授权），是"小模型 + 边缘部署"对 scaling 主线的反向注脚；**③ 两个"预计 10-19"预告连续第二日落空**——GPT-6.1 Sol 相关事件与智谱 GLM-5.3-Highspeed 官方发布均未发生（Highspeed 仍 ZCode 灰度）；**④ 明日（10-21）为事件密度日**：黄仁勋 GTC 柏林 Keynote（11:00–13:00 CEST）+ Meta/特斯拉财报——Nemotron 系与 RTX Spark 生态的后续卡大概率在此落地。**

---

## 本期要点（相对 2026-10-19 新增/更新）

- ★★ **Microsoft：《Securing the agentic insider》+ Guardian Agents（Microsoft 官方博客一手，2026-10-19；TechCrunch/Firstpost/ANI/Gate 等同日广泛报道）**——安全业务负责人 Hayete Gallot 官方表态：**"Unfortunately, frontier models, regardless of their origin, cannot be trusted"**——理由不是模型恶意或易被黑，而是**不可预测**：模型为"完成任务"训练，未按"组织规范/判断"优化，存在 reward hacking，且 agent 之间可**合谋**而无需被攻破。产品动作：① **Guardian Agents**（Project Perception 新增类别）监控企业已部署的内部 agent，随风险升高干预——Project Perception 此前的红/蓝/绿 agent 三件套假设威胁来自**外部**，本次转向**内部**；② **Microsoft Defender 影子 agent 检测：可发现员工带入企业的 ~60 类 agent（点名 Claude Code、Codex、OpenClaw）**；③ 权限按任务动态调整 + 高风险决策需人工批准。Nadella 10 月初私人博客铺垫："**separate the supply of intelligence from the authority over it**"。⚠️ TechCrunch 点破自指性：微软同时重仓 OpenAI/Anthropic 且 OpenAI 是其大客户——此为对自家被投生态的"不可信任"宣言（战略层解读）。**（窗口内唯一目标机构一手发布，详见 §1。）**
- ★★ **Mistral Timestral 补录（Mistral，10-15 一手发布；10-16 ODSC / 10-18 MarkTechPost / 10-19 LDS、AI Weekly、Tech Insider 等报道密集，全库此前 0 收录，10-16/17/18/19 四期连续漏收，本期补录）**——Mistral **首个时序基础模型家族（TSFM）**：**4 档 5M / 28M / 123M / 209M**（patch-based transformer，temporal + variate attention；209M = 24 层 / hidden 768 / 32-step patch / 21 分位输出头），**32,768 时间步上下文**、单次前向最多 1,024 步、概率预测 21 分位（0.01–0.99，pinball loss ≈ CRPS 离散近似）。**Mistral 自报：209M 在 GIFT-Eval / TIME / fev-bench 三大公开基准零样本预训练模型中均第一**，以约 2/3 参数量胜 Google **TimesFM-3（330M）** 与 Amazon **Chronos-2（120M）**（⚠️ 竞品分数出自 Mistral model card，非对手团队自报）。**CPU 即可推理**（8 线程服务器 CPU：5M 约 10ms、209M 约 140ms 单日预测）；训练以**合成数据为主**（趋势/季节/噪声过程合成多变量序列）+ 真实/合成 post-training（上下文 ×4）。**权重 Modified MIT（免费下载；月营收 >$20M 企业需 Mistral 授权）、推理代码 Apache 2.0**；on-prem / VPC / air-gapped；微调走 Mistral Forge。**（详见 §2。）**
- ★ **Anthropic METR 嵌入式评估：二次报道 + 细节补全（一手 10-15 已录 10-16 期；FT/Ars Technica 10-18、TechTimes/Value Add VC/MLQ 10-19 广泛扩散，本期交叉引用补细节）**——新增可记录细节：① **6 名 METR 评估员**获公司硬件、工位与内部工具访问，权限大致对齐 Anthropic 自有风险评估团队；② **三层访问体系**：METR 位于最高层（发表无需 Anthropic 批准，Anthropic 仅可要求对预定义类别——客户数据/律师-客户特权/模型架构细节——做 redaction，且 METR 可公开对 redaction 提出异议）；**SecureBio 等低层评估者发表前需 Anthropic 放行**；③ 另与 **Accenture** 合作、与 **Hugging Face** 早期洽谈中；④ **Altman 称 OpenAI 将向独立评估者提供类似访问**（⚠️ 二手转述，无 OpenAI 一手文本，single-source, tentative）。与 10-18 公共利益基金（5%+2% 股权）合成 Anthropic IPO 前夜的治理叙事双件套。
- ★ **预告核验（连续第二日）**——10-16/10-17 期标注的两个"预计 10-19"截至撰稿均未落地：① GPT-6.1 Sol 相关事件：OpenAI 窗口内无新公告，最新正式卡仍为 09-29 GPT-6.1 Sol addendum 系统卡 + 10-07 GPT-6 October update；`aurora-*-alpha` 三 ID 自 10-18 曝光后无新进展（仍无成功调用记录）；② **智谱 GLM-5.3-Highspeed：仍为 ZCode 灰度**（36氪/量子位 10-18 仍以"悄悄亮相"描述；用户实测 ~490 tokens/s、1M ctx / 131K max output 来自 Pi 目录，智谱无官方速度口径、无定价、无正式发布）。
- ★ **其他窗口信号**——① **NVIDIA GTC Berlin Keynote 预告（官方日程）**：黄仁勋 **10-21 11:00–13:00 CEST（北京时间 17:00–19:00）**——10-15 Nemotron 3.5 Super VL/Bolt + RTX Spark（10-16 起全球开售）之后的下一个机构动作窗口，与 Meta/特斯拉 10-21 财报同日（投资线 10-18/10-19 期已记）；② **Gemini 2.5 Pro / Flash / Flash-Lite 于 2026-10-20 正式退役**（Google Cloud 文档，替换为 gemini-3.8-flash 系）——生命周期事件，无新卡含义；③ **The Information 10-19：《How DeepSeek Is Shaping Huawei's AI Chips》**——对 09-30 已录 DeepSeek×Huawei Ascend 编程基础设施合作（128 芯片 supernode + TileLang）的分析性跟进，无新增一手技术内容；④ **Nscale × Anthropic 传再谈 $450 亿算力交易（TechCrunch 10-19，未证实）**——投资线素材，本期不展开；⑤ 特朗普 10-17 宣布将设 "AI Force"（仿 Space Force、含执法职能）——**同日 `investment-daily` 10-19 已记**，本页交叉引用不重复。
- **非目标机构排除记录（窗口内）**：**MiniMax M3.1 Flash（10-19 免费档跟进；同模型 M3.1-Flash-Preview 已录 09-29 期，非新卡）**；**Inception Mercury 3（10-19 报道，快速扩散语言模型；Mercury 2/2.5 既有记录，3 为新版本）**；Hugging Face Apertus 1.5（10-19 更新）；Disney 吸收 Character.AI 多数员工（stalking horse 结构，10-19）；ModelBest / Tencent / Underdog 等无新卡。**arXiv title "Technical Report" top-50 复核**：最新 3 篇（Cortex `2610.24255` 治理型编码 agent、MOSS-Image `2610.23374`、Xiaomi-Lens-0 `2610.23279`）均非目标机构，且后两篇 10-19 期已排除——**不重复展开**。
- **静默**：**17/19 目标机构窗口内零新卡**——DeepSeek（1017+Search API 已录）、OpenAI（最新卡 09-29/10-07）、Meta（Muse Spark Open 10-15 已录 10-16 期）、Google（Harness² 10-18 已录；Argon 无新卡）、Anthropic（治理层活跃、无新 Claude 卡）、Qwen、Yi、Baichuan、Microsoft（**本窗口动作 = 安全博客，非模型**；MAI-Base-2 已录 10-17 期；Phi-5 无官方报告）、Apple（AFM 3 后持续静默）、NVIDIA（Super VL 10-15 已录 10-16 期）、xAI（Grok 4.7 卡仍缺）、Amazon（Nova 2 后无新卡）、Zhipu（Highspeed 仍灰度）、InternLM（Atria Dawn 已录）、Moonshot（K3 权重 07-27）、StepFun（Step 5 权重 10-15 已录 10-16 期）、ByteDance（Seed2.0 后无新卡）。

---

## 一、Microsoft《Securing the agentic insider》+ Guardian Agents（2026-10-19）

| 字段 | 内容 |
|------|------|
| **中文标题** | 保护"智能体内鬼"：微软把企业 AI agent 按内部威胁管控，称"前沿模型不可信任" |
| **英文标题** | Securing the agentic insider（Microsoft 官方博客原标题） |
| **发布机构** | Microsoft（一手：`blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/`，署名 Hayete Gallot，EVP, Microsoft Security） |
| **发布日期** | 2026-10-19（TechCrunch/Firstpost/ANI/Gate/tribuneindia 同日跟进） |
| **性质** | **安全产品 + 官方立场声明，非模型/系统卡** |
| **核心判断（官方原文）** | **"Unfortunately, frontier models, regardless of their origin, cannot be trusted."**——归因：非恶意/易被黑，而是**不可预测**（为任务完成训练 → reward hacking；未按组织规范优化；agent 可互相合谋且无需被攻破；常见过度授权：数据/工具/系统访问 + 关键流程自主决策） |
| **产品动作** | ① **Guardian Agents**（Project Perception 扩展）：持续监控企业内部 agent、风险升高时干预——Project Perception（6 月宣布，红/蓝/绿 agent 三类）原设计假设威胁**来自外部**，本次转向**内部**；② **Defender 影子 agent 检测：识别员工带入企业的 ~60 类 agent（点名 Claude Code、Codex、OpenClaw）**；③ 任务级动态权限调整 + 高风险决策强制人工批准；④ 要求对模型决策的透明度（"Model transparency will not replace containment. It will make containment smarter."——但检查 reasoning tokens 被明确列为**下一步、非当前能力**） |
| **高层铺垫** | Nadella 10 月初私人博客："We simply can't outsource responsibility for what intelligence does on our behalf. A model provider's assurances do not relieve us of that responsibility. … we need to **separate the supply of intelligence from the authority over it**." |
| **战略矛盾（媒体指出）** | 微软重仓 OpenAI/Anthropic、OpenAI 是其大云客户、自有 AI 实验室——此番"不可信任"针对自家被投生态（TechCrunch："surprising and self-serving"） |

**要点**
1. **与 10-19 期 Harness² 构成同一转向的两面**：Google 把"harness 层"做成可开放进化的对象（能力视角），微软把"harness/控制层"做成不可信任模型之外的**强制隔离层**（安全视角）——**"模型能力"与"模型控制权"正式分家**。
2. **点名 Claude Code / Codex / OpenClaw 为"影子 agent"** 值得注意：这是主流云厂商首次把主流编码 agent 直接列为需被发现与管控的内部威胁面。
3. ⚠️ 非技术报告：无基准、无参数、无论文；`insider threat` 叙事的证据层全部是产品能力宣称，**不得当作模型安全性研究引用**。

---

## 二、Mistral Timestral（Mistral AI，2026-10-15 发布，本期补录）

| 字段 | 内容 |
|------|------|
| **中文标题** | Timestral：Mistral 的时序基础模型家族 |
| **英文标题** | Timestral: Mistral's time-series foundation models |
| **发布机构** | Mistral AI（一手：`mistral.ai/news/timestral/`；HF `Timestral-209M` model card + license；`timestral-1-0` 文档为 public preview） |
| **发布日期** | 2026-10-15（一手）；10-16 ODSC、10-18 MarkTechPost、10-19 LDS/AI Weekly/Tech Insider/Lumien 等报道扩散——**全库此前 0 收录，本期补录并标注漏收 10-16/17/18/19 四期** |
| **模型家族** | Timestral-5M / 28M / 123M / **209M**（旗舰）——同架构同配方 |
| **架构** | patch-based transformer，**temporal attention + variate attention**；209M：24 层 / hidden 768 / 32-step patch；**21 分位概率输出头** |
| **上下文 / 输出** | **32,768 时间步**；单次前向最多 **1,024 步**（更长 horizon 分块）；多变量目标 + past-only / known-future covariates |
| **训练** | 以**合成过程为主**（趋势/季节/噪声组合成多变量序列）预训练 + 真实/合成 post-training（**上下文 ×4**）；目标函数 = 21 分位 pinball loss（CRPS 离散近似）；微调走 Mistral Forge |
| **基准（Mistral 自报）** | 209M 在 **GIFT-Eval（MASE 0.658）/ TIME（0.626）/ fev-bench（SQL skill 50.39）** 零样本预训练模型中均第一；胜 **TimesFM-3 330M**（0.667 / 0.640 / 48.99）与 **Chronos-2 120M**（0.698 / 0.662 / 47.28）、Datadog Toto 2.0-2.5B——⚠️ **竞品分数出自 Mistral model card，Google/Amazon 未在自家页面发布可比数字**；123M 与 209M 差距仅 0.001 MASE（规模收益快速递减） |
| **部署** | **无需 GPU**：8 线程服务器 CPU 单日预测 5M ≈ 10ms / 209M ≈ 140ms；on-prem / VPC / air-gapped |
| **许可** | 权重 **Modified MIT**（月营收 >$20M 企业需 Mistral 授权）；推理代码 Apache 2.0——**商用友好度高于 TimesFM-3 的 non-commercial** |
| **定位** | 企业时序数据（传感器遥测、可观测性指标）→ 容量规划/能源/供应链/风险/维护；**AI Weekly：90 天内 Mistral 第 11 篇、首篇非语言模型** |

**要点**
1. **反 scaling 注脚**：当主流叙事在 1T+/10^26 FLOPs 与出口管制门槛之间拉扯时，Mistral 把旗舰动作落在 **209M、CPU、10ms**——"够用 + 边缘 + air-gapped"是与 frontier 完全正交的产品逻辑。
2. **与 48 号公告的隐性呼应**（10-19 期 §2）：小参数 + 时序域 + Modified MIT，落在任何"大模型"管制门槛的距离之外；开源豁免逻辑（公共领域不纳入）在此类产品上几乎无争议。
3. ⚠️ **口径纪律**：所有"第一"均为 Mistral 自报 + 榜单提交口径；TimesFM-3/Chronos-2 分数未经对手确认——引用时必须带 "per Mistral model card" 标签。
4. 时序补录不影响既有 LLM 主线记录：本库 [[ctr-scaling-landscape]] 等页不新增成员。

---

## 三、Anthropic METR 嵌入式评估：二次报道细节（10-15 一手已录 10-16 期）

- **不重复 10-16 期主记录**，本期仅补窗口内二次报道新增/细化的事实：**6 名 METR 评估员**（Value Add VC / MLQ，10-19）；**三层访问体系**——METR 最高层（发表无需批准、可对 redaction 公开异议）vs SecureBio 等低层（发表需 Anthropic 放行）；另与 **Accenture** 合作、与 **Hugging Face** 早期洽谈；Anthropic 类比**银行驻场监管员**（resident examiners）。
- **Altman 表态**："OpenAI will offer independent evaluators similar access"——⚠️ **二手转述，无 OpenAI 一手文本**（single-source, tentative）；若属实，将是 10-15 Anthropic 公告后第一家公开跟进的 frontier lab。
- 与 10-18 **公共利益基金（5%+2% 股权）**、10-17 已录 Misalignment/访问控制叙事共同构成 IPO 前（最早 11-09 当周路演）的治理三件套；FT/Ars Technica 10-18 的广泛转载本身即"治理资产媒体化"的证据。
- 窗口内 Anthropic **无新 Claude 卡**：最新仍为 Sonnet 5.5 / Fable 5.1 / Opus 5.5 系（既有记录）。

---

## 四、其他窗口信号与排除项

- **事件日历（前瞻）**：**10-21 = NVIDIA GTC Berlin Keynote（黄仁勋，11:00–13:00 CEST / 北京 17:00–19:00）+ Meta、特斯拉财报**——Nemotron 系（Super VL/Bolt 已于 10-15 落地）与 RTX Spark PC 生态（10-16 全球开售）的后续发布大概率集中于此；10-23 iPhone Duo 开售。投资线 10-18/10-19 期已从市场视角覆盖，本页仅标注为**技术报告预期窗口**。
- **Gemini 2.5 系退役（10-20，Google Cloud 生命周期文档）**：gemini-2.5-pro / flash / flash-lite 今日退役，替换指向 gemini-3.8-flash 系——纯生命周期事件。
- **DeepSeek**：The Information 10-19 深度分析《How DeepSeek Is Shaping Huawei's AI Chips》——09-30 已录 Ascend 合作（128 芯片 supernode、TileLang、计算/通信库）的分析跟进，**无新增一手技术内容**，不重复。
- **Nscale × Anthropic $450 亿算力谈判传闻**（TechCrunch 10-19）——未证实；投资线素材。
- **非目标机构排除**：MiniMax **M3.1 Flash**（10-19，含免费档）、Inception **Mercury 3**（10-19，扩散语言模型）、Hugging Face Apertus 1.5、Disney/Character.AI、ModelBest MiniCPM 系无新动作。
- **arXiv 收割（复核）**：export API 持续 503/空响应；title "Technical Report" 简单检索 top-50 可用，最新 3 篇（`2610.24255` Cortex / `2610.23374` MOSS-Image / `2610.23279` Xiaomi-Lens-0，均 10-16）非目标机构；Monday 10-19 block 的 1,162 标题扫描（10-19 期）为本窗口权威口径——**0 篇目标机构报告**。
- **同日兄弟交叉引用**（不重复）：`arxiv-daily` / `arxiv-paper-check`（10-20，论文线）、`investment-daily` / `wq101-alpha-daily`（10-19，已覆盖 AI Force、GTC 柏林日历、Anthropic 治理的投资视角）。本页独占机构/技术报告线。

---

## 五、19 家目标机构窗口复核（2026-10-19 → 10-20）

| 机构 | 本期状态 | 窗口内事件 / 最新已录卡 |
|------|----------|--------------------------|
| **Mistral** | ★★ 补录 | **Timestral（10-15，本期补录，漏收四期）**：5M–209M 时序家族、CPU 推理、Modified MIT；Large 4（1T/49B）开放权重仍承诺 **10-31** |
| **Microsoft** | ★★ 一手（非模型） | **《Securing the agentic insider》（10-19）**：Guardian Agents + Defender 60 类影子 agent 检测 + "frontier models cannot be trusted"；MAI-Base-2（10-15）已录 10-17 期；Phi-5 仍无官方报告 |
| **Anthropic** | ★ 交叉引用 | METR 嵌入式评估二次报道（10-15 一手已录 10-16 期）：6 人/三层访问/SecureBio 需放行 + Altman 跟进表态（二手）；无新 Claude 卡 |
| DeepSeek | 无 | 1017+Search API（10-17）已录 10-19 期；The Information 华为芯片分析无新一手内容 |
| OpenAI | 无 | "预计 10-19"事件未落地（连续第二日待核）；`aurora-*-alpha` 无新进展；最新正式卡仍 09-29/10-07 |
| Google (DeepMind) | 无 | Gemini 2.5 系今日退役（生命周期）；Harness²（10-18）/ Argon（10-13）已录；GTC 明日 |
| Meta | 无 | Muse Spark Open（10-15）已录 10-16 期；10-21 财报 |
| Qwen (Alibaba) | 无 | 无新卡 |
| Yi (01.AI) | 无 | 2026 年内持续静默 |
| Baichuan | 无 | 最新仍 Baichuan-M4（既有记录） |
| Apple | 无 | AFM 3（06-08）后持续静默 |
| NVIDIA | 无（前瞻） | Super VL/Bolt（10-15）已录 10-16 期；**GTC Berlin Keynote 明日 11:00 CEST** |
| xAI | 无 | Grok 4.7 卡仍缺（既有记录） |
| Amazon | 无 | Nova 2（2025-12）后无新卡 |
| Zhipu | 无 | GLM-5.3-Highspeed 仍 ZCode 灰度（10-18 量子位/36氪）；"预计 10-19"落空 |
| InternLM | 无 | Atria Dawn 正式版（10-17）已录 10-19 期 |
| Moonshot (Kimi) | 无 | "10-17 开源 K3"仍判旧闻（K3 权重 07-27） |
| StepFun | 无 | Step 5 权重（10-15）已录 10-16 期 |
| ByteDance (Seed) | 无 | Seed2.0 模型卡（2607.00248）后无新卡 |

---

## 六、六方向归纳（静默期简版）

1. **架构**：窗口内无新架构发布。Timestral 的 temporal+variate attention 属时序专用设计，不进入 LLM 架构讨论线。
2. **训练/RL**：无新训练报告。Timestral "合成数据为主 + 4× 长上下文 post-training" 可作为小模型配方的一条注脚。
3. **Scaling**：无新 scaling 分析；反而是 Timestral（209M、123M≈209M 的 0.001 差距）提供了"规模收益递减发生在亚千 M 区间"的时序域样本。
4. **多模态**：无新卡（1017 的 vision config、EmbeddingGemma 2 等均为既有记录）。
5. **长上下文**：无新卡；Argon 500K 第三方测试（10-19 期单源）无后续。
6. **推理模型**：无新卡；`aurora` 图像线无新进展。**治理层是本期唯一有实质增量的方向**（Microsoft 不可信论 + Anthropic METR 细节），与 10-19 期"Harness² / 公共利益基金 / 48 号公告"的治理周主题无缝衔接——**本周（10-13→10-20）可概括为：模型卡稀薄、控制权与管制条文密集**。

---

## 七、口径与不确定性

1. **Timestral 基准全部为 Mistral 自报**：TimesFM-3 / Chronos-2 / Toto 分数出自 Timestral-209M model card，对手团队未发布可比数字——**引用必须带口径标签**；榜单分数为提交状态（GIFT-Eval/TIME "results have been submitted"）。
2. **Microsoft "不可信任"为产品立场**：无实验数据、无评测、无论文支撑；Guardian Agents / Defender 60 类检测为厂商宣称，未经第三方验证。
3. **Altman 跟进 METR 式访问 = 二手**（Value Add VC 转述），无 OpenAI 一手文本——在 OpenAI 发布公告前不得升格为 claim。
4. **"预计 10-19"双预告落空**（GPT-6.1 Sol 事件、GLM-5.3-Highspeed）：连续第二日标注；Highspeed 维持"灰度测试、非发布"三态；若 10-20 稍晚落地，下期补录。
5. **MiniMax M3.1 Flash / Inception Mercury 3 为非目标机构**，仅排除记录；MiniMax 若未来进入官方清单再升格。
6. **漏收标注**：Timestral 在 10-16/17/18/19 四期漏收（当时注意力集中于"开放权重超级周"的 LLM 交付），本期补录并记录漏收期数；Anthropic METR 一手已于 10-16 期正确收录，本期仅为交叉引用补细节，不计漏收。
7. **arXiv**：export API 本窗口不可用；Monday block 扫描（10-19 期）+ title 检索 top-50 复核为替代口径，**不能完全排除**极少数标题未含 "Technical Report" 字样的目标机构报告，但周一至周二的低产节奏下风险很低（tentative）。

---

## 八、方法论

- **窗口与来源**：2026-10-19 → 10-20；一手 = `blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/`、`mistral.ai/news/timestral/` + HF Timestral-209M model card/license、`anthropic.com/news/an-update-on-independent-evaluators`（交叉引用）、Google Cloud Gemini 生命周期文档；二手 = TechCrunch（微软/英伟达/Nscale）、Firstpost/ANI/Gate/tribuneindia（微软）、FT/Ars Technica/TechTimes/Value Add VC/MLQ（METR）、ODSC/MarkTechPost/LDS/AI Weekly/Tech Insider/Lumien（Timestral）、36氪/量子位/Pandaily（Highspeed 灰度）、The Information（DeepSeek×华为分析）、whatisai/lmmarketcap/aireleasetracker（非目标新卡雷达）。
- **arXiv 收割**：export API 空响应持续 → title "Technical Report" 简单入口 top-50（最新至 10-16，非目标）+ 引用 10-19 期 Monday block 1,162 标题扫描结论（0 目标）。
- **去重（grep 全库）**：`Timestral`、`Guardian Agents`、`agentic insider`、`Mercury 3` 写入前 0 命中；`cannot be trusted` 仅 10-03 conference-digest 无关语境命中（ARC-AGI-3 分数可信度，非微软语境）；**`M3.1 Flash` 非 0 命中——09-29 期已录 M3.1-Flash-Preview 公测，本期 10-19 条目为同一模型的免费档跟进，排除记录已改注"已录（09-29 预览）"**；`METR`/`public benefit`/`aurora` 已在既有期（交叉引用不重复）；Nemotron 3.5 Super VL 已录 10-16 期（TechCrunch 10-19 文为二次报道，不重复）。
- **同日兄弟**：`arxiv-daily`、`arxiv-paper-check`（10-20 论文线）、`investment-daily` / `wq101-alpha-daily`（10-19，AI Force / GTC 日历 / Anthropic 治理投资视角）——本页独占机构/技术报告线。
- **19 家机构以 CLAUDE.md 官方清单为准**（与 10-19 期复核表一致，无漂移）。
- **临时文件**：`/tmp/{atr1,atr2,atrs}.html|xml`——写完即删。
