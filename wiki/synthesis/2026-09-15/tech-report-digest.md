---
title: "LLM Tech Report Digest — 2026-09-15"
type: synthesis
created: 2026-09-15
updated: 2026-09-15
sources: []
tags: [tech-report, LLM, technical-report, system-card, arXiv, model-card, moe, reasoning, long-context, multimodal, hybrid-architecture, agentic, open-source, kv-cache, daily-digest]
---

# LLM Tech Report Digest — 2026-09-15

> 全球主要 AI 公司大模型技术报告速览（截至 2026-09-15）
> 本篇聚焦自 2026-09-14 摘要后的新增项（★ = 新收录；⭐ = catch-up）
> 本日主线：**xAI 首次公开 Grok 4.7→5 代际路线图（4.7 ≈ Opus 5.0；4.8 = 2.5T C++ 栈；4.9 ≈ Astra/Fable class；Grok 5 "maybe better than anything"）** + **上海 AI Lab 释放非 Preview 版 Intern-S2-397B 开放权重（Apache-2.0）** + 全行业系统卡静默窗口（OpenAI / Anthropic / Google / Meta / Apple 均无新卡）

---

## 1. xAI — SpaceXAI / Grok（★ 本日头条）

### 1.1 Grok 4.7 → 5 路线图公开 + 4.7 继续跳票（★ 更新）
- **动态（2026-09-14，Musk X 连发）**:
  - **Grok 4.7 自我定位**：*"should be roughly on par with Opus 5.0, not 5.1. Better in some ways, worse in others. We need to fix multimodal performance."* —— 首次官方口径下调：从 09-02 的"surpass all current models"降为"对标 Claude Opus 5.0（非 5.1）"，并承认多模态弱项（⚠️ 与其 09-02 声称的"全面超越"矛盾）
  - **Grok 4.8**：*2.5T 参数、基于全新 C++ 软件栈训练，预计本周完成训练并进入 RL*（首次披露 4.8 > 4.7）
  - **AGI 问答**：被问 4.8 离 AGI 多近 → *"That will be Grok 5"*
  - **4.9 / 5 定位**：4.9 *"probably Astra/Fable class"*；Grok 5 *"maybe better than anything. We shall see."*（= 对标 OpenAI GPT-6 Astra 与 Anthropic Fable 5 class 成为 xAI 迭代锚点）
  - **跳票归因（沿用 09-13 Data Studios 分析）**：RL 阶段 *"penalized response length too heavily"* → 模型 *"gives up on hard tasks (that it can do!) too early"*，自我校验未达要求 → 仍需 *"a few more days to cook"*
- **发布状态**：截至 **2026-09-15 仍未发布**；docs.x.ai 公开档位最高仍为 **grok-4.6**；无 4.7 模型卡/系统卡
- **参数（founder-reported，未验证）**：~2.1T（较 Grok 4.6 的 1.5T +40%），首训完成、补充 SpaceX 工程语料训练中；更慢但 token 效率更高（Musk 口径）
- **错失窗口计数（第 4 次）**：07-25 "~4 周"（≈08-22）→ 08-12 "3–4 周"（≈09-02~09-09）→ 09-02 "10 天"（≈09-12）→ 09-12 起 "few more days"（当下）
- **生态动作（本周，非模型卡）**:
  - **Grok 进入 Microsoft 365 Copilot**（2026-09-12；Word/Excel/PPT，Microsoft Frontier Program 有限预览）——与 GitHub Copilot 的 Grok 4.6（08-19）、Copilot Studio 的 Grok 4.1 Fast 并行为"三套 Copilot、三个 Grok 模型"的多模战略
  - **Grok Bot for Enterprise**（09-03）上线
  - **Grok × Cursor 订阅合并**（09-14，产品负责人 Maxime Prades 宣布：数周内统一 Grok+Cursor 订阅体系）
- **链接**: [TeslaNorth (09-14)](https://teslanorth.com/2026/09/14/elon-grok-roadmap-through-grok-5/) / [MITrade (09-14)](https://www.mitrade.com/insights/news/live-news/article-3-2084364-20260914) / [The Standard/AFP (09-02)](https://www.thestandard.com.hk/innovation/article/341654/SpaceXAI-to-launch-Grok-47-model-in-10-days-to-outpace-rivals) / [OrcaRouter 4.7 时间线复盘 (09-12)](https://www.orcarouter.ai/blog/grok-4-7-release-date) / [kie.ai 4.7 汇总 (09-11)](https://kie.ai/blog/what-is-grok-4-7)
- ⚠️ **CONTRADICTION】：Musk 09-02 "Grok 4.7 will exceed all current models" vs 09-14 "roughly on par with Opus 5.0, not 5.1"——定位口径显著下调（第三次窗口错失后）**

---

## 2. InternLM / 上海 AI Lab — Intern-S2-397B（★ NEW）

### 2.1 Intern-S2-397B 正式版开放权重（★ 新收录）
- **中文标题**: Intern-S2-397B：面向科学智能与长程 Agent 的开放权重多模态旗舰
- **英文标题**: Intern-S2-397B: Open-Weight Scientific Multimodal Foundation Model for Long-Horizon Agents (Shanghai AI Laboratory InternLM)
- **发布机构**: 上海人工智能实验室（Shanghai AI Laboratory / InternLM 团队）
- **模型名称**: **Intern-S2-397B**（非 Preview；HF 仓库实测 ~404B，命名口径 397B/403B/404B 不一 —— 已 flag）
- **发布日期**: **2026-09-13**（HF `internlm/Intern-S2-397B`，Apache-2.0，发布当日即开放权重）
- **核心参数**: **403B total MoE（512 experts / 10 active，OrcaRouter 口径）**；上下文 **256K text / 64K multimodal**；输入 **text + image + time-series**（科学时序模态为 Intern-S2 线特色）；自托管或官方 Intern API，无公开每-token 价目
- **定位与创新（模型卡/第三方转述）**:
  - 科学专项 + 长程 agent：继 **Intern-S2-Preview-397B**（2026-07-16~18 发布、08-13 论文 arXiv:2608.13505，本 Wiki 已收录于 09-12 摘要）之后的非 Preview 正式版开放
  - 与同为 9 月开局的 **Qwen3.8-Max**（$2/$6 计量企业旗舰）构成**相反的经济赌注**：Apache-2.0 开放权重 + 零每-token 价格 vs 商用 custom license 按量计费
  - **尚无任何独立第三方评测**（vendor table only，tentative）
- **关键基准（InternLM 自测，未复现）**: MMLU Pro **89.77** / HMMT-2026 **93.56** / MMMU Pro **81.68** / SWE-bench-Pro **68.54** / **TerminalBench 2.1 64.04**（表格中最大短板）；对照列含 Qwen3.5-397B-A17B / DeepSeek V4 Pro / Kimi K2.7-Code / GLM-5.2 / GPT-5.5 / Gemini 3.1 Pro / Claude Opus 4.8
- **生态**: 与 **Intern-S2-Mobius（35B，知识-推理解耦，arXiv:2608.14290）**（09-14 摘要）拼成"科学智能旗舰 + 紧凑研究"两条线；工具链沿 XTuner / LMDeploy / Lagent
- **链接**: [HF internlm/Intern-S2-397B](https://huggingface.co/internlm/Intern-S2-397B) / [HF Intern-S2 合集](https://huggingface.co/collections/internlm/intern-s2) / [OrcaRouter 对比 Qwen3.8-Max (09-13)](https://www.orcarouter.ai/blog/intern-s2-397b-vs-qwen-3-8-max) / [Intern-S2-Preview 论文 arXiv:2608.13505](https://arxiv.org/pdf/2608.13505v1)
- ⚠️ 说明: Preview-397B 已收录于 09-12 摘要；本轮为**正式版（去 Preview）开放权重**新增；总参数媒体口径 397B/403B/404B 不一，未裁定

---

## 3. DeepSeek（参照 — 延续 09-14）

- **V4.1-Pro 仍待定**；`deepseek-v4-pro` 自 **2026-09-14 12:00（北京时间）** 起已按 09-14 摘要生效的临时路由至 **V4.1-Flash**（Flash 计价）持续中
- **定价战延续（OrcaRouter 09-14 复盘）**：V4 Pro 高峰 $1.32/$3.96、错峰 $0.66/$1.98 vs Qwen3.8-Max $2.00/$6.00 flat——输出价差可达 3–6×，Intelligence Index 40 vs 36（Qwen3.8-Max 领先 4 分）；"三分钱价差是否值得四点评分差距"的 +字 命题成为服务商叙事
- V4.1-Flash 技术报告（09-10）详见 09-14 摘要，本窗口无新增

## 4. OpenAI（参照 — 无新增系统卡）

- **GPT-6 Astra**：继续 GA 推进中（Microsoft Foundry 等企业侧）；无新 system card / tech report；9 月中旬窗口未流出新卡
- OpenAI DevDay **09-29** 为下一个预期节点（09-13 投资摘要已收录）

## 5. Anthropic — Claude（参照 — 无新增）

- **Claude Fable 5.2+ 仍未发布**（截至 09-15）：Anthropic 官方 system cards 页面最新仅止于 **Fable 5.1 / Mythos 5.1（2026-09）**；Manifold 市场（09-11 更新）对 Fable 5.2+ 的发布时间预期整体落在 **10 月中下旬之后**（10-01 前仅 ~13%）
- ⚠️ **kie.ai 声称 Fable 5.2 于 09-10 发布 = 第三方聚合站传闻，官方无任何卡/发布页佐证 → 维持 low confidence，本 Wiki 不采信**

## 6. Google DeepMind — Gemini（参照 — 无新增）

- Gemini 3.8 Flash + 3.8 Flash Cyber 双卡已收录于 09-14 摘要；Gemini 4（10 月发布传闻、3.5 Pro 搁置，low confidence）持续在研
- LM Market Cap 数据点：**Gemma 4 26B-A4B / 31B（free）** 列开源榜 Top4/5（已收录于 09-12 摘要，示例）

## 7. Meta / 8. Microsoft / 9. NVIDIA / 10. Apple（参照 — 无新增）

- **Meta**：Muse Glimmer / Muse Spark 1.3 已收录；无新卡
- **Microsoft**：Phi-5 pre-release；Grok 接入 Copilot 属产品动作（见 §1）；无新 Phi 技术报告
- **NVIDIA**：Nemotron 3.5 Lightning / Nemotron 3 Ultra 已收录；LM Market Cap 开源榜 **Nemotron 3 Nano Omni (free)** 出现但为旧账
- **Apple**：AFM 3 年度技术报告仍爽约（官方曾承诺 "later this summer"，现已 9 月中，第三季度未完）——**watch：WWDC26 The Batch 口径称"benchmark 结果年内发布"而非点名"技术报告"**

## 11. Alibaba — Qwen（参照 — 无新增）

- Qwen3.8-Max 权重已于 08-12 开源（custom license）、Qwen3.8-27B（08-14 Apache 2.0）均已在先前摘要收录；LM Market Cap 确认 Qwen3.8-Max ($2/$6, AA Index 40, GPQA 92.7) 与 Qwen3.8-27B（`qwen3.8-max` license）定价
- LMMarketCap 近期发布列（供索引）：Qwen3.8 Max (0902) / Qwen3.8 Flash (08-26) / Qwen3.8 27B (08-14) / Qwen3.7 Flash (07-27) —— 均已在历史摘要覆盖

## 12. Moonshot AI — Kimi / 13. MiniMax / 14. 智谱 GLM / 15. StepFun / 16. ByteDance / 17. Mistral / 18. 01.AI / 19. Baichuan（参照 — 无新增）

- **Kimi K3**（2.8T-A104B）已收录；LM Market Cap 开源榜 #2（$3/$15）
- **MiniMax M3**（428B-A23B, MSA sparse attention, 1M ctx）已收录（08-14 摘要）；LM Market Cap 开源榜 **#1**、Kilo 榜活跃 #2
- **智谱 GLM-5.3**（Terminal-Bench 3.0 28.3 开源第一）已收录（09-14 catch-up）；GLM-5.3 Flash 配件生态（Volcano/Coding Plan 权重配比）在第三方监控中活跃
- **StepFun**：Step-3.7-Flash（198B-A11B）已收录；LMMarketCap 开源榜 17 位；本周无新报告
- **ByteDance / Mistral / 01.AI / Baichuan**：无新 tech report / system card

## 20. 补充 — Tencent Hy4 Preview（已有 Wiki 收录，仅更新动向）

- Hy4 Preview（770B-A49B, 1M+ ctx, Apache 2.0, MTP）已收录于 09-01 摘要；编码/Token 计划生态中持续铺开（多平台 Coding Plan 配比）
- 今日不重复展开，仅提醒社区口碑来源（LMMarketCap/Kilo）已将 Tencent **hy3** 列为历史档位、**Hy4** 进入活跃监控

---

## 本日头条与动态（相对 2026-09-14 摘要的 Delta）

### 1. xAI 路线图首次公开化：Grok 4.7→5 阶梯（★ 本日主线）
| 代际 | 规模/栈 | 自我定位（Musk 09-14） | 状态 |
|------|---------|------------------------|------|
| Grok 4.7 | ~2.1T（founder 口径） | 大致对标 **Opus 5.0，非 5.1**；多模态待修 | 未发布（第 4 次错失窗口） |
| Grok 4.8 | 2.5T / 新 C++ 软件栈 | "noticeable improvement" | 本周完成训练进入 RL |
| Grok 4.9 | — | "probably **Astra/Fable class**" | 规划 |
| Grok 5 | — | "maybe better than anything" | 规划（Musk 答"离 AGI 最近的答案"） |

→ 关键信号：**xAI 首次把 OpenAI GPT-6 Astra 与 Anthropic Fable 5 写成自己的代际对标锚点**；4.7 的三连定位（顶配→大幅领先→对等 Opus 5.0）本身就是一张"压缩版发布叙事"时间表

### 2. 科学智能开放权重再添旗舰（★ NEW）
- **Intern-S2-397B**（09-13, Apache-2.0）：403B MoE / 512e-10a / 256K+64K / text+image+time-series；姊妹线 35B Mobius（09-14 已收录）+ Preview 397B（09-12 已收录）

### 3. 系统卡静默窗口
- 09-14 → 09-15 **无任何新的 frontier 系统卡 / 技术报告**（OpenAI / Anthropic / Google / Meta / Apple / Qwen / Kimi / GLM / MiniMax 等全部静默）
- 活跃侧均为**产品/生态动作**：Grok×Microsoft 365 Copilot、Grok×Cursor 订阅合并、Grok Bot Enterprise、Qwen-Image-3.0（08-03，历史摘要）

### 4. 今日新增/更新汇总（★ 新增共 2 项，均非"新发布当天"）
| 公司/机构 | 新增项 | 日期 | 类型 |
|-----------|--------|------|------|
| xAI | Grok 4.7→5 路线图 + 4.7 第 4 次跳票 ★ | 2026-09-14 | 官方（X）动态 |
| 上海 AI Lab | Intern-S2-397B 正式版开放权重 ★ | 2026-09-13 | 模型/开放权重 |

---

## 交叉主题分析

### 1. "发布即跳票"成为美系前沿的常态，9 月窗口由开源侧主导
- 美系四档全部挂在"即将发布"状态：**Grok 4.7**（第 4 个窗口）、**Claude Fable 5.2+**（Manifold 预期 10 月中下旬）、**DeepSeek V4.1-Pro**（待定）、**Gemini 4**（10 月传闻）——而 9 月已经落地的技术增量（DeepSeek-V4.1-Flash KV 压缩、GLM-5.3、Intern-S2 线、Qwen 3.8 全系）**全部来自开源/半开源阵营**
- 与 09-14 摘要判断一致：后训练数据工程与 KV 成本成为开源阵营的主战场，闭源侧进入"命名+营销先行、发布后置"节奏

### 2. xAI 定位变化：从"独角兽断言"到"可比较的阶梯"
- 09-02 "surpass all current models" → 09-14 "on par with Opus 5.0, not 5.1"——**把自我评价降级为可被第三方验证的相对定位**，同时用 4.8/4.9/5 的未来档位维持想象力
- RL 翻车细节（response-length 惩罚过重 → 提前放弃难题）与 09-13 Data Studios 归因、Kilo/OpenClaw 榜单上 Grok 长任务放弃现象互相印证 → **"响应长度惩罚 vs 难题坚持度"成为 2026Q3 RL 后训练水温和风向标**

### 3. 科学智能 = 中国开放权重的差异化赛道
- Intern-S2-397B（科学/时序/长程 agent）+ Mobius（知识-推理解耦）+ GLM-5.3（编程/网安）→ 中国开源阵营在**细分纵深**上与美系"通用前沿"错位竞争；Intern-S2 线保持"Apache-2.0 + 发布当日开放"策略，恰与 Qwen3.8-Max 的"GA 后一周开权重 + custom license"形成中国内部的两条开源路径

### 4. 服务商榜单成为模型"非官方财报"
- OrcaRouter / LMMarketCap / Artificial Analysis 的日更指数（Intelligence Index、$2/$6 价差 vs $0.66/$1.98 错峰、开源榜 #1 MiniMax M3 #2 Kimi K3）开始成为本 Wiki 在官方卡缺失时的交叉验证源（keep citing, mark口径）
- 提示：这些第三方口径之间存在系统性差异（如 Anthropic OSWorld 跨库不一致的历史问题——09-04 摘要已记录），引用时需标注来源

---

*Generated 2026-09-15. Source: Web search results (TeslaNorth, MITrade/Reuters, The Standard/AFP, OrcaRouter, kie.ai, HF model cards, aibase, eesel, KuCoin, x.ai docs, LMMarketCap, qwen.ai, Anthropic system-cards page, Manifold Markets). Cross-referenced with wiki/synthesis/2026-09-14/tech-report-digest.md.*