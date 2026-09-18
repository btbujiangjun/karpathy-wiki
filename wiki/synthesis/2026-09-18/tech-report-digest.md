---
title: "LLM Tech Report Digest — 2026-09-18"
type: synthesis
created: 2026-09-18
updated: 2026-09-18
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, reasoning, long-context, multimodal, hybrid-architecture, agentic, enterprise, data-retention, safety, daily-digest]
---

# LLM Tech Report Digest — 2026-09-18

> 全球主要 AI 公司大模型技术报告速览（截至 2026-09-18）
> 本篇聚焦自 2026-09-17 摘要后的新增项（★ = 新收录；⭐ = catch-up/官源补 pin）
> 本日主线：**xAI Grok 4.7 终于进入实际 rollout（09-17 Google Cloud quota 先行信号 + 有限用户开始收到更新）——上一个 digest 的"再度顺延"口径被实时推翻；Google 侧 Gemini 3.8 Flash 首个独立评测（AA Intelligence Index ≈59）齐平/略超 GPT-Astra（58），且 09-15 新增 Gemini 3.8 Live / Live Extended Thinking 双实时语音档（AA S2S ≈82.6，$3.50/hr 定价）**。同时今日出现**口径纪律重要样本**：kie.ai 宣称 Claude Fable 5.2 已于 09-10"发布"，与 anthropic.com/system-cards 页面（最新仍 Fable 5.1 / Mythos 5.1）直接矛盾——按 rumor 纪律不采信；DeepSeek 侧 The Register 给出 **V4.1-Flash 763B 总参数（含巨量 N-gram 参数池）** 与官方 552B 口径的分叉，需要显式标记为计量口径差异（tentative）。交叉趋势：**N-gram 混合参数池成为新一代"账面参数膨胀但激活稀疏"的共识手法**（DeepSeek V4.1-Flash / Qwen3.8-Flash-Next 51B / GLM-5.3 相关结构），详见文末交叉主题。

---

## 1. xAI — Grok 4.7 开闸：从"再顺延"到"开始 rollout"（★ 本日头条，状态修正）

- **状态更新（09-17 晚，ET）**：Grok 4.7 出现在 **Google Cloud quota 页面**（koltregaskes 信号，通常预示 12 小时内公开）→ 随后 **mark_k / testingcatalog 等实测用户报告"已经在向有限用户 rollout"**（HuggingNews 聚合 4 条 X 信号）；**Musk 同步定调：*"should be roughly on par with Opus 5.0, not 5.1. Better in some ways, worse in others"***
- **对 09-17 digest 的修正**：09-17 摘要称"第 5 次错失窗口、推迟至下周或更晚"——**该结论于同日美东晚间即被推翻**；最新口径 = **有限 rollout 已开始，公开 GA / 基准未发布**。
- **余下路线图（09-15 DigitalToday 复核，与 09-15 digest 已录一致，补细节）**:
  - **Grok 4.8**：**2.5T 参数**，xAI **新 C++ 软件栈**训练，**本周（发稿时）收尾进入 RL**；Musk："noticeable improvement" over 4.7（内部对比 2.5T > 2.1T 增量明显、JAX 中途修正了若干错误）
  - **Grok 4.9**："probably Astra / Fable class"（对标 GPT-6 Astra 与 Claude Fable 线）
  - **Grok 5**：**3T 参数**，改进训练软件 + 精炼数据，Musk 称"most excited about"
- **规模（⭐ 复用）**：4.7 约 **2.1T**（vs 4.6 约 1.5T，+40%），无官方 spec —— 仍是创始人口述，low confidence
- **链接**: HuggingNews 09-17 聚合（@koltregaskes / @mark_k / @testingcatalog / @brianroemmele）；DigitalToday 09-15（Musk 引语 + 路线图）；cross-ref [[tech-report-digest 2026-09-17|09-17 digest §2]]（上一日"顺延"口径）
- ⚠️ **CONTRADICTION**: 09-17 digest（"推迟至下周或更晚"）vs 09-17 实际（quota+limited rollout 已启动）——本 digest 采信后者，但**全体 rollout 与 benchmark card 仍未发布**。

## 2. Google — Gemini 3.8 Flash 首个独立评测 + 3.8 Live 双实时档（★ 新增量 + ⭐ 补 pin）

### 2.1 Gemini 3.8 Flash：AA Intelligence Index ≈59（★ 第三方独立评测，首次）
- **09-17/18 Artificial Analysis 收录**：3.8 Flash（09-02 发布的模型卡片见 09-14 digest §1.2）取得 **AA Intelligence Index ≈59**，与 GPT-Astra（58）基本持平/略高（**第三/四款 Flash 在 4 个月内**，为 AA 判定"近 30 天最大发布"之一）
- 已录规格不复述（1M ctx / 65K out / thinking LOW-MED-HIGH / HLE-Verified 54.9 / TB2.1 90.8 / SWE-Bench Pro 61.6 / **$0.75–$3.75 per M** / 引价至 2026 年底）
- **社区反向信号（low confidence，single-source）**：discuss.ai.google.dev 09-14 出现"Gemini 3.8 regression"主题帖（部分用户报推理回归），**无官方回复、样本与口径未知**，仅作 watch

### 2.2 Gemini 3.8 Live / 3.8 Live Extended Thinking（★ 新收录，09-15 发布）
- **定位**：speech-to-speech 实时语音档（承接 09-16 已录的 GPT-Live-1 Astra 参照物）
- **规格（AA 实测口径）**：**AA S2S（speech-to-speech）质量 ≈82.6**；Live-ET 为 think-then-speak 的深度思考变体
- **定价**：**$3.50/hr（获 region-pricing 支持，AA 收录）**——直接对赌 GPT-Live-1 Astra（S2S ≈81.5，$5.83/hr）
- **意义**：实时语音 = 9 月双线竞争（对话智能 + 单位成本）的新战场；Google 用 Flash 定价水位（历史最低 frontier 级别）压缩语音时薪

## 3. Anthropic — Fable 5.2"已发布"与官方页矛盾（⚠️ CONTRADICTION，不断言）+ 蒸馏威胁报告（★ 新）

- **kie.ai 声称**：Claude **Fable 5.2**"launched September 10, 2026"，并给出规格链（延续 5.2 命名）——但 **anthropic.com/system-cards 页面仍以 Fable 5.1 / Mythos 5.1（2026-09-01 发布）为最新**，无 5.2 卡
  - ⚠️ **CONTRADICTION**：kie.ai（"09-10 已发布"）vs 官方 system-cards 页（最新仍 Fable 5.1）。**按 09-15/09-17 已确立纪律，marketplace/第三方页面的未来卡信息一律不采信为事实**；Manifold 10-01 前发布概率此前约 13%（09-15 已录）。Fable 5.2 维持 **rumor/unconfirmed**
  - 参照：Fable 5.1 定价 $10/$50 per M，Terminal-Bench-Science 52.6（09-15 已录）
- **Anthropic 威胁情报报告（2026）**：点名 **DeepSeek 等 7 家中国实验室对 Claude 运行蒸馏（distillation）campaign**——7 月 14 天窗口内约 **1210 万次 exchange**；此为"蒸馏战"的首个明确量化指控。⚠️ 属单方指控，DeepSeek 否认面未见；作行业安全叙事 recorded，不作事实定论
- 数据留存争议维持 09-16 口径（企业侧限制 + EFS 分阶段 watch），无新

## 4. DeepSeek — V4.1-Flash 参数口径：763B（含 N-gram 池）vs 552B 官方（★/⭐ 补 pin + 计量口径清理）

- **The Register（09-17）**：报告 **V4.1-Flash"总参数 763B"**，并强调其为 **"迄今最大之一 N-gram 参数池"**（45T 预训练 tokens 复述）——与官方/09-14 摘要的 **552B MoE（8B active in / 16B out，CED 40 层）** 直接分叉
- **计量口径解读（tentative）**：552B = 核心 MoE 权重；**763B ≈ 核心 552B + 大规模 N-gram/混合参数表征（类似 Qwen3.8-Flash-Next 的 51B N-gram embeddings、以及 Nemotron 线 hybrid 结构）**，即"账面参数 vs 激活参数"记账差异——**账单价与 benchmark 均不因记账口径改变**，但生态对标（4.7 2.1T / K3 2.8T / Muse 1.05M ctx 等）需统一口径
- **已录不复述**：890 bytes/token FP4 KV、持久 KV 1/8、CSA2/SPARQL 等见 09-14/09-17 digest；V4-Pro→V4.1-Flash 路由 09-14 生效
- **链接**: The Register（2026-09）；cross-ref [[tech-report-digest 2026-09-14|09-14 digest §1.1]]

## 5. Microsoft / 6. Meta / 7. NVIDIA / 8. Apple（参照 — 无新增）

- **Microsoft**：Phi-5 仍无官方报告；MAI 线（MAI-Thinking-1 2026-06-02）无 09 月新卡
- **Meta**：Muse Glimmer（08-10）/ Muse Spark 1.3（09-02，1.05M ctx）已收录；**AA 近期指数收录 Muse Spark 1.3 ≈60（第三方补 pin，标记"量级一致"）**；LLaMA 线退役维持
- **NVIDIA**：Nemotron 3 家族（Nano 30B-A3B 2025-12 / Super 120B-A12B 2026-04 / Ultra 550B-A55B 2026-06；hybrid Mamba-Transformer MoE、NVFP4）——技术报告线已录，**无 09 月新卡**；Nemotron-SEA-LION-v4.8 已于 09-17 sibling 收录，不重复
- **Apple**：AFM 3 年度技术报告继续爽约（"later this summer" 已过期）；iPhone 18 系列 09-18 开售为产品侧，非报告事件

## 9. 其他目标机构（参照 — 无新增，逐条复核）

- **Qwen**：Qwen3.8-Flash-Next（08-26，125B-A6B + **51B N-gram 嵌入、off-accelerator 系统 RAM**，Qwen4 架构预览）已于 09-12/09-05 收录；Qwen3.8-Max-0902 已录；无新
- **Moonshot Kimi**：K3（2.8T-A104B，07-16）与 K2.7 Code（06-16）均已录；无新
- **MiniMax**：M3（428B-A23B）已录；无新
- **智谱 GLM**：GLM-5.3（08-14，CyberGym 84.5 / 1M ctx / 权重 ~08-28 开源）与 GLM-5.3-Flash（国产芯片全流程）已在 09-14/09-12 digest；无新（N-gram/稀疏注意力细节并入交叉主题）
- **ByteDance**：Seed 2.0 / Doubao 1.6（02-14）最新；无新
- **Mistral**：Mistral Medium 3.5（04-28/05-22，128B dense，Modified MIT）已录；无新
- **StepFun**：Step 3.7 Flash（05-29）已录；无新
- **01.AI**：最新仍 Yi-Lightning（2024-10-16），confirmed zero 动态（延续 09-17 复核）
- **Baichuan / InternLM / Tencent Hy4**：Baichuan-M4、Intern-S2-397B（09-13 Apache-2.0）、Hy4 已录；无新
- **Amazon (Nova 2)**：技术报告/模型卡已于 09-14 digest 收录（Lite/Pro/Omni、1M ctx）；本轮补 ⭐ 官网技术报告 URL（cdn.amazon.science PDF，2025-12-02 发布家族），无新增规格

---

## 本日头条与动态（相对 2026-09-17 摘要的 Delta）

### 1. 官方侧静默窗口被"半官方信号"打破：Grok 4.7 从 rumor 走向 rollout
- 09-17 的确认待办变为实际事件：**Google Cloud quota 页 = xAI 系平台发布先行信号**（此前 4.6 也在 Bedrock/配额页先见于 08-19），预示 12h 内公开；本次以-limited tester rollout 形式开始
- **发布纪律提示**：OpenAI（09-16 Astra）、xAI（09-17 Grok 4.7）都出现"平台配额/产品页先行、benchmark card 滞后"的发布节奏——**quota 信号 vs 官方卡之间的时间窗正成为新的确认判据**

### 2. Gemini 3.8"价值前沿"双述职：Flash 档与 Live 档同日补位
- Flash 档用 **$0.75/$3.75** 拉平 frontier 性价比；Live 档用 **$3.50/hr S2S ≈82.6** 对标 GPT-Live-1（$5.83/hr）——Google 在**单位 token / 单位语音时薪**两条成本曲线上同时压价

### 3. N-gram 混合参数池：账面参数膨胀的新记账语言正在形成
- DeepSeek V4.1-Flash（763B 含巨量 N-gram 池）、Qwen3.8-Flash-Next（51B N-gram 嵌入）、GLM-5.3（稀疏注意力 + 相关结构）**三家在同周以不同方式报告"参数 = 激活 + 检索式 N-gram 混合"**——⚠️ 跨厂参数对比若不含 N-gram 池会系统性低估中系 flash 档、高估稠密旗舰；推荐对照时统一采用"激活参数 + KV/账单价"口径（大纲与 09-16 Karpathy 系摘要建议一致）

### 4. 今日新增/更新汇总（★ 新增 5 项 + 修正 1 项 + 补 pin 2 项）
| 公司/机构 | 新增项 | 日期 | 类型 |
|-----------|--------|------|------|
| xAI | Grok 4.7 开始有限 rollout（GC quota 先行）+ 修正 09-17"再顺延"口径；路线图 4.8/4.9/5 补细节 ★ | 2026-09-17 | 半官方/实测 |
| Google | Gemini 3.8 Flash AA Intelligence Index ≈59（首个独立评测）★ | 2026-09-17 | 第三方评测 |
| Google | Gemini 3.8 Live / Live-ET 发布（S2S ≈82.6，$3.50/hr）★ | 2026-09-15 | 官方发布 |
| Anthropic | Fable 5.2"已发布"claim 与官方卡页矛盾 ⚠️；威胁情报报告点名 DeepSeek 蒸馏 ★ | 09-10 / 2026 | unconfirmed/指控 |
| DeepSeek | V4.1-Flash 763B（含 N-gram 池）vs 552B 官方口径清理 ★/⭐ | 2026-09-17 | 报道分叉 |
| Meta | Muse Spark 1.3 第三方指数 ≈60 补 pin ⭐ | 2026-09 | 第三方评测 |
| Amazon | Nova 2 技术报告官网 URL 补 pin ⭐ | 2025-12 | 官源补 pin |

---

## 交叉主题分析

### 1. "发布 = 配额页 + 有限 rollout，卡在后发"成为 xAI 新节奏
- Grok 4.6（08-12，Bedrock/配额先见）→ 4.7（09-17）延续同一模式；**注意区分"rollout 已开始"vs"已发布（官方卡/API/定价）"**——目前 4.7 三样都缺。与 OpenAI Astra 的分阶段铺开（09-16 已录）对照，**"GA 义务"正在被"灰度发布"取代**，benchmark 对比要等官方卡

### 2. 独立评测成为"价值档"定价锚
- AA Intelligence Index 59（3.8 Flash）/ 60（Muse Spark 1.3）/ 61（Astra）构成可比较的第三方坐标——**注意指数含"成本-能力"混合成分**（AA 方法学），数值排序 ≠ 纯能力；跨模型基准对比请回到 HLE/TB2.1/SWE-Bench Pro 成分项

### 3. 蒸馏指控与"账面参数"叙事互相取暖
- Anthropic 指控 DeepSeek 7 月 1210 万 exchange 蒸馏的同时，DeepSeek/Qwen/GLM 共同把参数口径转向"激活稀疏 + 检索记忆大型化"——**若蒸馏论成立，则 N-gram 混合档案正是"在平替账单价下复制前沿能力"的工程化路线**（tentative，单方指控 + 口径推断）；维持 rumor/指控纪律，不入 claim 页

### 4. Rumor 边界纪律（延续 09-15/17）
- Fable 5.2"已发布"（kie.ai，与官方页矛盾）、Grok 4.7 2.1T/2.5T/3T 规格（创始人口述）、Muse 指数值（第三方近似）——**一律 low confidence 或 tentative，不得入 claim 页**；唯一可作 claim 候选：Gemini 3.8 Live 定价与 S2S 数值（有官方/AA 双侧）、V4.1-Flash 763B 口径分叉本身（有双源）

---

*Generated 2026-09-18. Source: Web search results (HuggingNews xAI 09-17 聚合、DigitalToday 09-15 Musk 引语、artificialanalysis.ai Gemini 3.8 Flash / Muse Spark 1.3 指数、Google Gemini 3.8 Live/Live-ET 发布、discuss.ai.google.dev 回归帖、kie.ai Fable 5.2 页、anthropic.com/system-cards、Anthropic threat intelligence report、The Register DeepSeek V4.1-Flash、siliconangle、cdn.amazon.science Nova 2 tech report PDF). Cross-referenced with wiki/synthesis/2026-09-17/tech-report-digest.md（Grok 4.7 顺延口径修正、默认静默窗口状态）、2026-09-16/tech-report-digest.md（Astra 铺开/GPT-Live-1 参照）、2026-09-15/tech-report-digest.md（Grok 4.7→5 路线图、Fable 5.2 rumor 纪律）、2026-09-14/tech-report-digest.md（Gemini 3.8 Flash 规格、DeepSeek V4.1-Flash 技术细节、Nova 2）。*