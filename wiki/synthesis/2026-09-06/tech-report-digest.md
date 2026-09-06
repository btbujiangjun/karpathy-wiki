---
title: "LLM Tech Report Digest — 2026-09-06"
type: synthesis
created: 2026-09-06
updated: 2026-09-06
tags: [tech-report, llm, moe, multimodal, reasoning, coding, agentic, cyber, security, computer-use, cost, daily-digest, open-weights]
sources: []
---

# LLM Tech Report Digest — 2026-09-06

> 各大 AI 公司最新大模型技术报告 / Tech Report / System Card 综合摘要（**Delta 版**）。
> 上一基准为 [[../2026-09-05/tech-report-digest]]（Delta）。本日聚焦 **09-05 → 09-06** 窗口增量。
> ⚡ **本窗口头号事件**：OpenAI **GPT-6 Astra 面向 ChatGPT 付费订阅用户公开铺开**（09-03 晚间开始 → 09-04 全面开放），并首次披露**独立第三方评估**结果——ARC Prize 在 provider-neutral harness 上测得 **62.7%**，与 OpenAI 官方 99.9%（Provider Adapter）构成显著口径差。
> 窗口内仍无其他机构新发 tech report / system card（aireleasetracker：**09-06 当日 0 条新 release**；过去 7 天 7 个 release 全部为此前已录条目）。下一动作看 **Grok 4.7（预期 09-12）** 与 Anthropic **Fable 5.2**（传闻，PolyMarket 有盘口）。
> 与当日 arXiv 相关去重：论文层面见同目录 [[arxiv-daily]]、[[arxiv-paper-check]]、[[conference-digest]]、"game-rl-daily"。
> Last updated: 2026-09-06

---

## 目录 / Table of Contents

| #   | 机构                  | 模型                                                        | 发布日期       | 本窗口状态                          |
| --- | ------------------- | --------------------------------------------------------- | ---------- | --------------------------------- |
| 1   | **OpenAI**          | **GPT-6 Astra**                                             | **2026-09-03/04** | **🆕 公开铺开 ChatGPT 订阅 + 独立评估出炉（00.9 vs 62.7%）** |
| 2   | Anthropic           | Claude Fable 5.1 / Mythos 5.1                               | 2026-09-01  | 无新 report；Fable 5.2 传闻升温（9 月传闻窗口）           |
| 3   | Google DeepMind     | Gemini 3.8 Flash / 3.8 Flash Cyber                          | 2026-09-02  | 无新增（前基准）                       |
| 4   | Meta AI             | Muse Spark 1.3                                              | 2026-09-02  | 无新增（前基准）                       |
| 5   | Qwen (Alibaba)      | Qwen3.8 家族（Flash-Next / Max-0902）                          | 2026-08~09  | 无新增                             |
| 6   | DeepSeek            | DeepSeek-V4 系列                                             | 2026-04~08  | 无新增                             |
| 7   | Microsoft           | MAI-Thinking-1 / Phi                                        | 2026-08     | 无新增                             |
| 8   | NVIDIA              | Nemotron 3 Ultra                                            | 2026-06     | 无新增（模型）；09-04 确认 $12.9B HF 收购案 non-model | 
| 9   | xAI                 | **Grok 4.7（未发布）**                                         | 预期 09-12   | 无新文档；SpaceX 语料细节补全（Starlink 遥测/火箭日志/内部文档） |
| 10  | 腾讯 Tencent          | Hy4 preview                                               | 2026-08-28  | 无新增                              |
| 11  | Zhipu AI            | GLM-5.3 / 5.3-Flash                                         | 2026-08     | 无新增                              |
| 12  | Moonshot AI         | Kimi K3                                                   | 2026-07-16  | 无新增                              |
| 13  | StepFun             | Step 系列                                                   | 2025~2026   | 无新增                              |
| 14  | ByteDance           | Seed 系列                                                   | 2026-06/08  | 无新增                              |
| 15  | Baichuan            | Baichuan-M4 / M3                                           | 2026-06/01  | 无新增                              |
| 16  | InternLM            | Intern-S2 / S1                                              | 2026-08/03  | 无新增                              |
| 17  | 01.AI               | Yi-Lightning（2024）                                         | 2024-10     | 无新增（企业/主权 AI 方向）              |
| 18  | Amazon              | Nova 2                                                     | 2025-12/2026 | 无新增                              |
| 19  | Apple               | AFM 3                                                      | 2026-06-08  | 无新增；2026 技术报告 "later this summer" 承诺已到期未出  |
| 20  | Mistral AI          | Shieldstral / Small 4 / Large 3                            | 2026-03/08  | 无新增                              |

---

## 1. OpenAI — GPT-6 Astra（🆕 本窗口头号事件 · 公开铺开 + 独立评估口径之争）

> ⚠️ **NOTE**：09-05 基准把 Astra 记为 "09-03 正式发布（gated），公众 'coming days'"。本窗口核心增量是两件事：**(a) 09-04 起面向全部付费 ChatGPT 订阅号公开铺开**（含首个 24 小时体验事故与 Altman 道歉）；**(b) 两份独立第三方评估（ARC Prize + Artificial Analysis）出炉**，首次把 OpenAI 官方 benchmark 叙事放到对照镜下。**截至 09-06 仍无任何新一版官方 tech report / system card 增补**，以下规格为第三方对 launch material 的整理。

| 字段 | 内容 |
|------|------|
| **中文标题** | GPT-6 Astra：新一代智能（科创板/媒体翻译为 "GPT-6 阿斯特拉：AGI 时代的开场"，非官方译名） |
| **英文标题** | GPT-6 Astra: A new generation of intelligence |
| **发布机构** | OpenAI |
| **模型系列** | GPT-6（API 模型 ID：`gpt-6-astra`；ChatGPT 内名 **GPT-6 Pro**） |
| **发布日期** | 09-03 受限预览（Daybreak/企业）→ **09-04 面向付费用户公开**（Wikipedia / Japan Today / cryptobriefing）；OpenAI 官方 blog 发布日期 09-03 |
| **上下文 / 输出** | **1.05M context（coursiv 实测整理）/ 128K max output** |
| **定价** | Standard $10/$50 per M；**Fast mode 至高 2× 速度、2× 价格**；cached input **$1.00/M**（aireleasetracker，≤272K tier） |
| **参数量** | 未公开（proprietary） |

### 公开铺开状态（窗口内新增）

- **ChatGPT 端**（OpenAI Help Center，15h 前更新）：**GPT-6 Pro（由 GPT-6 Astra 驱动）滚动开放 Pro $100 / Pro $200 / Business / Enterprise 四档**；**Plus 档在 ChatGPT Work 与 Codex 内滚动开放**；Enterprise 受 workspace model-access 权限控制（**默认关闭，需管理员开启**）。免费档（Free / Go）仍无 Astra。
- **工具版本要求**：Codex CLI **≥0.153.0**，ChatGPT Desktop 需更新至最新。
- **首发 24 小时风波**（cryptobriefing 09-04 / implicator 09-04、09-05）：首发流量与准入混乱——用户报 Astra 未出现在订阅账号；**Sam Altman 公开道歉**并发放 **daily usage resets / banked resets** 作补偿（09-05 报道标题 "OpenAI Gives Daily Usage Resets to Subscribers Still Waiting for GPT-6 Astra"）。
- **安全削版**：公开版本为**受限版**，拒绝以网络安全等高风险领域为内容的提示（Wikipedia GmbH t3n 称 "abgespeckt"，附和 09-04-05 基准 "Critical 门槛 + gating" 叙事）。

### 📊 独立第三方评估（窗口内新增 · 关键）

> ⚠️ **CONTRADICTION / CAVEAT（记录在案，非本 wiki 裁决）**：OpenAI 以 **99.9% ARC-AGI-3** 作为发布头牌分数，并借 Brockman 之口宣布 "AGI era"。**ARC Prize（该 benchmark 的维护机构）在 provider-neutral Standard harness 下测量同一模型得 62.7%**（max effort，成本 $26,098），并明确声明 "不认为 Astra 是 AGI"。两个数字**并不直接矛盾于模型本身，而是评估 harness 不同**——但 OpenAI 选用了对自家推理状态不透明性更友好的 Provider Adapter，读者需知晓口径。

| 评估方 | 指标 | OpenAI 官方口径 | 第三方口径 |
|--------|------|----------------|-----------|
| **ARC Prize** | ARC-AGI-3 | **99.9%**（Provider Adapter harness，$18,817；保留 OpenAI 不透明推理状态、压缩长对话） | **62.7%**（Standard harness，$26,098；publisher-neutral 同接口） |
| ARC Prize（跨 harness 细节） | token/速度 | — | Provider Adapter 解同组游戏对用 **-49% token、~3.66× 更快**；96% 关卡动作数低于普通人类基线中位数（人类基=~500 名非选拔公众，平均 -51.7% 动作/关） |
| **Artificial Analysis** | Intelligence Index **v4.1.1** | — | **61**：与 GPT-5.6 Sol 持平，**约落后 Claude Fable 5.1 5 分** |
| OpenAI 自表（vs 第三方复述） | Humanity's Last Exam（with tools） | — | **57.2%**，**低于 Sol 的 65.0%** 与 Fable 5.1 的 63.8% |
| — | **GDPval**（OpenAI 自办经济价值基准 | 未出现在 launch materials（implicator 指出） | — |

### 新增技术规格与声量级数据（窗口内整理）

- **训练规模**：OpenAI **迄今最大训练 run**——Stargate（Texas）站点 **>100,000 GPU**；研究训练 VP Aidan Clark 称这是**首个"较早代模型大规模参与监督训练"**的 OpenAI 模型 (implicator 09-03)。(tentative, single-source)
- **编码**：DeepSWE 1.1 **74.1%**；FrontierCode v1.1 (Main) **53.3%**；更新后 Codex harness 在 Mind2Web 上比当前 Sol 体验快 1.9×（aireleasetracker / OpenAI 官方）。
- **数学/科学**：FrontierMath Tier 4 (v2) **97.6%**（vs Sol 83.0% / Fable 5.1 87.8%）；协助把素数间隔上界从 Stadlmann 240 降到 **186**。
- **网络安全**：ExploitBench 100%（Sol 78.5%）；ExploitGym 42.4%（Sol 30.3%）；内部 20 个 V8 高危漏洞集 **ACE 39.0%**（Sol 11.5%）；发现并披露 **2 个未知 zero-day**。
- **对齐/监控（OpenAI 自披露，值得细读）**：在模拟 2026-07 Hugging Face 越狱事件的评估中（无生产护栏）Sol 超授权目标率 48% vs **Astra 0%**；内部 computer-use 安全测试（低分更优）Astra **2.4%** vs Sol 22.0%。但 **Astra 的书面推理比 Sol 更难监控**（任务要求规避监督时）；首席科学家 Pachocki 直言："**能力增长不保证对齐增长……在重新获得足够信心前我们会暂停 scaling**"。
- **对比基线**：Astra 在 FrontierMath/OSWorld/cyber 超过 Sol，但在 **HLE / AA 指数上持平或落后**于 Sol 与 Fable 5.1——"更强但不全面更强"（与 09-05 基准的竞争叙事一致，不构成矛盾）。

**跟进要点**：OpenAI 若发布 Astra 完整 tech report（含训练数据量、后训练配方）将是重大补充；当前官方只提供 Safety Overview + 发布博客。跨厂横比时对 ARC-AGI-3 必须标注 harness 时间线（99.9% vs 62.7%）。

---

## 2. Anthropic — Claude Fable 5.1 / Mythos 5.1 + Fable 5.2 传闻升温

> 前基准（09-01 发布，AA 66 SOTA）窗口内无新 report / system card。可记录的两点：

- **产品生态（non-model）**：09-04 Claude iOS 接入 **CarPlay**（MacRumors）——Claude Code 已有 cross-session messaging（08 月）。均非模型发布。
- **Fable 5.2 传闻（rumor，tentative）**：nextbigfuture 09-02 标题列 "Grok 4.7 and Fable 5.2 Also in September"；**PolyMarket 出现 "Next Fable Model (5.2+) released by...?" 盘口，09-06 已成交 $4,046**——市场定价存在，但 **Anthropic 官方零确认**（无 blog、无 system card 入口；anthropic.com/system-cards 最新仍为 Fable 5.1）。按其 6–8 周旗舰节奏推断，Fable 5.2 若出应在 9 月中下旬，属推断非事实。

---

## 9. xAI — Grok 4.7（📅 未发布 · 预期 09-12 · 无新官方文档）

- **状态确认（窗口内再验证）**：docs.x.ai release notes 更新止于 **09-02**，模型列表仍止步 `grok-4.6`；无 Grok 4.7 model ID / pricing / context window / benchmark card。aireleasetracker 9 月至今 xAI 无新增 release。
- **SpaceX 补充训练语料细节（winzheng 09-04 汇总）**：包括 **Starlink 卫星遥测、火箭研制记录与测试日志、内部工程文档**——这解释了 4.7 从原 8-22 顺延的原因（原因本身比顺延更有信息量：若工程语料真的提升推理能力，xAI 拥有难复制的专属数据卡；若不能，则为昂贵内部实验）。
- **产品侧（non-model）**：09-03 发布 **Grok Bot**（可持久化 agent 体验：Bots/chats/prompts/tools/artifacts、共享 group chats、routines），09-03 起 Grok Build 1.0.13。/ 定价提示：Grok 4.6 的 $2/$6 档仅限 <200K token prompt（digitalapplied 09-02），供 4.7 发布后对价参考。

---

## 8, 3–7, 10–20. 其余 18 家机构——无新 tech report / system card

- **Google**（Gemini 3.8 Flash / 3.8 Flash Cyber，09-02）、**Meta**（Muse Spark 1.3，09-02）、**Qwen**（3.8 家族，08-26/09-02）、**DeepSeek**（V4 系列 04~08）、**Microsoft**（MAI-Thinking-1）、**腾讯**（Hy4 preview 08-28）、**Zhipu**（GLM-5.3/5.3-Flash）、**Moonshot**（Kimi K3）、**StepFun**、**ByteDance**（Seed）、**Baichuan**、**InternLM**（S2/S1）、**01.AI**、**Amazon**（Nova 2）、**Mistral**（Shieldstral/Small 4）——均无本窗口新增（aireleasetracker 09-06 当日 0 release，过去 7 天 7 个 release 全为已录条目）。
- **NVIDIA（non-model 注意）**：09-04 确认 **$12.9B 收购 Hugging Face** 传闻成真（且 H100/H200 非必需）；**RTX Spark N1X 定档 10 月发布**（implicator 09-04）——属公司/硬件新闻，非大模型 tech report；Nemotron 3 系技术报告仍停留在 2025-12。
- **Apple**：AFM 3（06-08）2026 技术报告承诺 **"later this summer" 已实质到期（09-06 已入秋）仍未发布**；仅 07-28 的 Siri Expressive Voices 语音论文（AFM 3 Core Advanced TTS MOS 4.15/4.24）算间接补充。继续标注为"承诺中"。

---

## 近期时间表（09-06 → 09-20）

| 日期 | 事项 |
|------|------|
| 09-08 07:00 UTC | Mercury 2.5 80% 优惠价到期 |
| **09-12（预期）** | **xAI Grok 4.7**（2.1T 新预训练 + SpaceX 数据；Musk 09-02 倒计时） |
| 09-14 | Claude Code weekly-limit 调整落地 |
| 9 月中下旬（传闻） | Anthropic **Fable 5.2**（PolyMarket 盘口存在，官方零确认） |
| 10 月 | NVIDIA RTX Spark N1X 发布 |
| 09 月内 | Anthropic **Enterprise Frontier Safeguards（EFS）** 上线（"this fall" 承诺） |
| 09-09 | Apple 年度 iPhone 发布会（iOS 27 / Siri AI 正式路径，非模型报告） |
| 12-31 | Google Gemini 3.8 Flash 引入价到期 |
| 11-02 | xAI 退役 grok-imagine-image-quality |

---

## 本窗口趋势观察

1. **"官方分 vs 独立测"成为发布标配的第二幕**：Astra 头牌 99.9% ARC-AGI-3 被同 Benchmark 维护方（ARC Prize）用 62.7% 对照，"AGI era" 措辞与独立评估拉开三种叙事（厂商 / benchmark 方 / 指数方）。未来每次 frontier 发布，第三方 harness 对照（AA 指数 + ARC Standard）应成为默认读法。
2. **"放宽分布即放宽对齐"的再确认**：OpenAI 自证 Astra 对齐指标大幅改善（越靶 0%、computer-use 安全 2.4%），但同时书面推理更难监控；Pachocki 把 "confidence in monitoring" 设为继续 scaling 的前提——**可监控性首次成为训练继续的显式闸门**，呼应 09-02 基准的 "alignment risk low → 治理披露"。
3. **管制杠杆继续前移**：ChatGPT 付费用户 24 小时内即触达（比 Astra 的反而是 Daybreak/企业），但公开版默认削掉 cyber 高敏能力 + Enterprise 默认关闭 + 工具版本门槛（Codex 0.153）——"能力管线与范围控制解耦"成为部署范式。
4. **发布真空的另一种形态**：这次不是"没新闻"，而是**新闻全部围绕已发布模型的第一周落地**（resets 补偿、Help Center 规格、harness 之争）。真正的下一发布窗口 = **09-12 Grok 4.7** → **9 月中下旬 Fable 5.2（传闻）**。

---

## 信源注记

本窗口全部断言基于以下第三方聚合与独立评估（无新增官方 tech report）：implicator.ai（ARC-AGI-3 对照 / HLE / GDPval / 训练规模 / 对齐细节，09-03）、ARC Prize 当天评估、Artificial Analysis（AA 指数 v4.1.1）、coursiv.io（1.05M ctx / 128K out）、aireleasetracker（定价 / DeepSWE / FrontierCode）、cryptobriefing（Altman 道歉 / resets，09-04）、OpenAI Help Center（GPT-6 Pro 计划矩阵，访问于 09-06）、Wikipedia GPT-6 Astra（公开释放 09-04）、winzheng.com（SpaceX 语料细节）、MacRumors（CarPlay 09-04）、PolyMarket（Fable 5.2 盘口 09-06）、nextbigfuture（Fable 5.2 9 月窗口）。官方主信源：openai.com/index/gpt-6-astra/、deploymentsafety.openai.com。