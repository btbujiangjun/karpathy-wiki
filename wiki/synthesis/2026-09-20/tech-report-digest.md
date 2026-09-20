---
title: "LLM Tech Report Digest — 2026-09-20"
type: synthesis
created: 2026-09-20
updated: 2026-09-20
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, reasoning, long-context, multimodal, hybrid-architecture, agentic, enterprise, data-retention, safety, daily-digest]
---

# LLM Tech Report Digest — 2026-09-20

> 全球主要 AI 公司大模型技术报告速览（截至 2026-09-20）
> 增量版：聚焦自 2026-09-19 全量版（09-11 格式逐家盘点）后的新增/确认项（★ = 新收录；⭐ = 官源补 pin/确认）
> 本日主线：**官方 frontier 系统卡静默进入第 5 天（09-17 后 19 家目标机构无任何新卡）——信号层/事件层有确认级进展：① OpenAI 官方定档 DevDay 2026 = 09-29（周二）旧金山，成为下一官方发布节点；② Google 的 Gemini 3.8 Audio 正式模型卡上线（09-15，3.8 Live / Live-ET 统一档位，证实 09-18 摘要的 AA S2S ≈82.6 并官方化定价/安全结论）；③ 阿里 Qwen-Audio-3.0-ASR 技术报告上线 arXiv（2609.07549）；④ Apple 新一代 Apple Intelligence 09-15 正式全系上线（AFM 3 Core Advanced 端侧）**。Grok 4.7 仍停留在 limited rollout（无卡/无定价/无基准）；Moonshot Kimi K4 维持单一信源 rumor。三条纪律保留：Fable 5.2 rumor 不采信、Grok 4.7 规格创始人口述 low confidence、DeepSeek 763B/552B 计量口径差异 tentative。

---

## 自 2026-09-19 digest 的 Delta（★ = 09-20 新增确认）

- **OpenAI DevDay 2026 官宣（09-29 周二，旧金山 Fort Mason）**——官方事件页 + devday.openai.com 同步上线，keynote 免费 livestream、Sam Altman 出席；业界普遍视为 Astra 之后的下一个发布节点。
- **Gemini 3.8 Audio 官方模型卡**（deepmind.google/models/model-cards/gemini-3-8-audio/，09-15 发布）——3.8 Live / Live-ET 视为同一档位，规格、定价、安全评估正式化（09-18 digest 仅 blog + AA 第三方数据，本轮官源确认）。
- **Qwen-Audio-3.0-ASR 技术报告**（arXiv:2609.07549，09-07 投稿，v2 09-09）——MoE LLM 主干 ASR 基座，一线中系语音侧技术报告。
- **Apple 新一代 Apple Intelligence 09-15 上线**（iOS 27 / iPadOS 27 / macOS 26 等）——产品/OS 级事件，AFM 3 Core Advanced 承担端侧；AFM 3 技术报告仍爽约。
- **无新 frontier 系统卡**：Anthropic（Fable 5.1 & Mythos 5.1 09-01）、OpenAI（GPT-6 Astra 09-03 / GPT-5.6 07-09）、Google（3.8 Flash 09-02）、Meta（Muse Spark 1.3 09-02）、xAI（Grok 4.7）全部维持。
- **Grok 4.7**：limited rollout 持续（09-17 起），GA/定价/benchmark card 均无新增。
- ⚠️ **CONTRADICTION（维持）**：kie.ai 声称 Fable 5.2 已于 09-10 发布 vs 官方 system-cards 页最新仍 5.1——维持不采信（09-18 已录并论证，本轮仅复核无变化）。

---

## 1. Google — Gemini 3.8 Audio 官方模型卡（⭐ 官源补 pin，09-18 第三方数据的官方背书）

- **中文标题**: Gemini 3.8 Audio（Live / Live Extended Thinking）模型卡
- **英文标题**: Gemini 3.8 Audio (Live, Live Extended Thinking) — Model Card
- **发布机构**: Google DeepMind
- **模型名称**: Gemini 3.8 Live（低延迟默认档）/ Gemini 3.8 Live Extended Thinking（深度思考档）
- **发布日期**: 2026-09-15（模型卡 + API + AI Studio 同日；rollout 中）
- **核心参数**（卡内正式化，印证 09-18 AA 口径）:
  - AA Speech-to-Speech Quality Index：**3.8 Live-ET = 82.6（#1）** / 3.8 Live = 76.0；time-to-first-audio 1.35s / 1.18s
  - 基于 Gemini 3 Pro；原生 audio-to-audio + 输入 text/images/audio/video，输出 text+audio；输入 128K / 输出 64K（API 口径 131,072 / 65,536 tokens）；knowledge cutoff 2025-01
  - 97 语言自动切换（Live API 文档仍标 70——口径 lag 已 flag）；SynthID 音频水印
- **定价**（dev blog + API pricing 官方）：audio input **$0.005/min** / audio output **$0.018/min**；text 输入 $0.75/M、输出 $4.50/M（含 thinking）；image/video 输入 $1.00/M 或 $0.002/min——与 09-18 已录 AA 换算 **$3.50/hr** 同为账单价口径（换算方式不同，并存标注 tentative）
- **主要创新点**:
  - **背景工具执行（background tool calls / asynchronous function calling）**——边说边做事，替代 cascaded 架构
  - Live-ET 的 think-then-speak 并行 reasoning（"let me check that..." 实时进度叙述）
  - 与 GPT-Live-1 Astra（09-16 已录）正面对标，价格约 40% 低
- **安全**：卡内披露 3.8 Live/ET 相对 3.7 Flash **无 meaningful 新能力/材料级性能提升**，依据 3.7 Flash 的 Frontier Safety Framework（2026-04 版）评估，判定**不达任何 T/CCL**
- **链接**: [Gemini 3.8 Audio 模型卡](https://deepmind.google/models/model-cards/gemini-3-8-audio/)；[发布博客 09-15](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)；[AI Studio 模型文档](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live)
- 3.8 Flash（09-02，AA ≈59，$0.75–3.75/M）同日复核无变化

## 2. Qwen — Qwen-Audio-3.0-ASR 技术报告（★ 新收录）

- **中文标题**: Qwen-Audio-3.0-ASR 技术报告
- **英文标题**: Qwen-Audio-3.0-ASR Technical Report
- **发布机构**: Alibaba / Qwen Team
- **模型名称**: Qwen-Audio-3.0-ASR（语音识别基座，非通用对话旗舰）
- **发布日期**: arXiv:2609.07549（2026-09-07 投稿，v2 09-09）
- **核心参数**: 以 MoE LLM 为主干的 ASR 模型；大规模（tens of millions of hours）语音语料训练
- **主要创新点**:
  - **LLM-based ASR 基座**（MoE 架构主干，非独立 E2E 识别模型）——同代 Qwen3.8 系生态的语音入口
  - **30 languages + 16 Chinese dialects** 覆盖
- **定位注**：语音侧技术报告，与 Qwen3.8-Max（2026-08）/ Flash-Next（08-26，51B N-gram）并列；中系 LLM-based ASR 基座竞争（vs GLM 语音线、Baichuan 语音侧）watch
- **链接**: [arXiv:2609.07549](https://arxiv.org/abs/2609.07549)

## 3. OpenAI — DevDay 2026 定档（★ 官方事件，下个确认节点）

- **DevDay 2026**：**2026-09-29（周二）旧金山 Fort Mason**；开场 keynote 免费 livestream；Sam Altman 出席；DevDay Exchanges 全球化扩展；现场票 $650
- **节点串联**：09-03 Astra 系统卡 →（灰度铺开 09 月全月）→ **09-29 DevDay**——业界预期 GPT-6 Sol / 平台与开发者工具更新；GPT-6 Sol 传闻（09-16 CometAPI）维持 rumor 级，不入 claim 页
- **最新卡维持**：GPT-6 Astra（09-03，首个 Preparedness Critical 网络安全级；AEL 59.3%；1.05M ctx / 128K out；$10/$50 per M）；GPT-5.6（07-09，Sol/Terra/Luna）
- **链接**: [openai.com/index/devday-2026](https://openai.com/index/devday-2026/)；[devday.openai.com](https://devday.openai.com/)

## 4. Apple — 新一代 Apple Intelligence 上线（★ 产品/OS 事件）+ AFM 3 参照

- **09-15 起**：新一代 Apple Intelligence 正式可用（iOS 27 / iPadOS 27 / macOS 26 等系统更新）；端侧 AFM 3 Core Advanced 承载系统级 AI 能力
- AFM 3 技术报告（2026 年度版）继续爽约（"later this summer" 已过期）；以官网研究笔记为准：AFM 3 Core 3B dense / Core Advanced 20B sparse（激活 1–4B 按需）、原生多模态、与 Google 联合
- **链接**: [Apple Newsroom](https://www.apple.com/ie/newsroom/2026/09/next-generation-of-apple-intelligence-available-today/)

## 5. 其他目标机构（参照 — 无新增，逐条复核）

- **Anthropic**：最新仍 Fable 5.1 & Mythos 5.1（09-01）；Fable 5.2 传闻维持不采信；07 月威胁情报蒸馏指控（点 7 家实验室、7 月 14 天约 1210 万 exchange）维持单方指控记录
- **DeepSeek**：最新仍 V4.1-Flash 技术报告 arXiv:2609.19969（09-17 投稿，552B MoE CED / 8B-16B active / 1M ctx / CSA2+FP4 → 890 B/token / SWA Bounded Replay ≈1/8 SSD）；763B vs 552B 计量口径差异维持 tentative
- **Meta**：Muse Spark 1.3（09-02，1.05M ctx，AA ≈60）最新；LLaMA 线退役维持；无新
- **xAI**：Grok 4.7 limited rollout 持续（无卡/定价/基准；2.1T 创始人口述 low confidence）；路线图 4.8（2.5T、C++ 栈、本周收尾入 RL）/ 4.9（Astra-Fable class）/ 5（3T）维持
- **Microsoft**：MAI-Thinking-1（06-02 白皮书，1T/35B，no-distillation）最新；Phi-5 仍无官方报告
- **NVIDIA**：Nemotron 3 Family + 3.5 Lightning（30B-A3B，Mamba-2+MoE+Attention，1M ctx，NVFP4）——无 09 月新卡
- **Moonshot Kimi**：K3（2.8T-A104B，07-16，KDA + AttnRes + Stable LatentMoE）最新；**K4 传闻（The Information 07-29 单一信源芯片采购）维持 rumor——无任何官方规格/日期；K3.1/K3.5 亦无官方**
- **Mistral**：无新 frontier 技术报告；仅档位页更新（docs/models）：Mistral Medium 3.5（v26.04）/ Small 4 / OCR 4.1 / Leanstral 1.5——档位维护，非报告事件
- **智谱 GLM**：GLM-5.3（08-14，CyberGym 84.5）+ GLM-5.3-Flash（国产芯片）+ GLM-5（2602.15763v2）；无新
- **ByteDance / StepFun / Baichuan / InternLM / 01.AI / MiniMax / Amazon**：Seed2.0 卡、Step-3.7-Flash（198B/~11B active）、Baichuan-M4（SPAR++，幻觉 3.3%）、Intern-S2-Preview/S2-397B、01.AI 维持 Yi-Lightning（2024-10-16）零动态（四次复核一致）、MiniMax M3、Nova 2——全部维持，无新

---

## 本日头条与动态（相对 2026-09-19 全量版的 Delta）

### 1. 官方卡静默第 5 天 → 下一个确认节点 = 09-29 OpenAI DevDay
- 09-17（DeepSeek arXiv + Grok 4.7 quota 先行）之后无任何新 frontier 系统卡；Anthropic/OpenAI/Google/Meta/xAI 官方页全部维持。**DevDay 09-29 成为本周唯一的官方时间锚**（OpenAI"ship week"传闻同指该窗口，rumor 级）。

### 2. Gemini 3.8 Audio：从"博客 + AA 第三方数字"到"官方卡正式化"
- 09-15 发布 4 天后官方模型卡落地，AA 的 S2S 82.6（Live-ET #1）获官卡背书；定价明确到 per-min 口径；**安全结论（无 T/CCL）首次官方化**——实时语音线的 frontier 安全评估正式进入"卡面"。

### 3. 事件层面：Apple 产品落地 vs Qwen 语音基座论文化
- Apple 09-15 全系上线（AFM Core Advanced 端侧）= OS 级产品事件；Qwen-Audio-3.0-ASR = 中系 LLM-based ASR 基座的论文级信号。**共同点：旗舰卡之外，周边模态（语音/端侧）报告正成为 9 月下旬的主要信号源。**

### 4. 今日 Delta 汇总（★ 新增 3 项 + ⭐ 官源确认 1 项）
| 公司/机构 | 新增项 | 日期 | 类型 |
|-----------|--------|------|------|
| OpenAI | DevDay 2026 官宣 = 09-29 旧金山（下个官方发布节点）★ | 2026-09 | 官方事件 |
| Google | Gemini 3.8 Audio 官方模型卡（3.8 Live/Live-ET 规格 + 定价 + 安全官方化）⭐ | 2026-09-15 | 官源补 pin |
| Qwen | Qwen-Audio-3.0-ASR 技术报告 arXiv:2609.07549（MoE LLM ASR，30 语言 + 16 中方言）★ | 2026-09-07/09 | 官方 TR |
| Apple | 新一代 Apple Intelligence 09-15 全系上线（AFM 3 Core Advanced 端侧）★ | 2026-09-15 | 产品/OS 事件 |

---

## 交叉主题分析

### 1. "官卡静默"下，事件日历比新卡更可依赖
- 后续密集节点：09-29 OpenAI DevDay + RecSys 2026（09-29~10-01）、~09-24 NeurIPS 2026 通知、09-30 MU 财报（投资侧）——**本周确认级信息源 = DevDay keynotes 与各厂卡页变更**，arbitrary 传闻一律划入 rumor。

### 2. 语音大战从"博客战"进入"卡面战"
- Gemini 3.8 Audio 官卡（AA S2S 82.6、$0.005/$0.018 per-min）vs GPT-Live-1 Astra（$5.83/hr）；中系以 Qwen-Audio-3.0-ASR / GLM 语音线构成 LLM-based ASR 第三极——**原生 audio-to-audio 成为 9 月最活跃的"新卡面"战场**。

### 3. 纪律重申（无变化）
- Fable 5.2（kie.ai，与官方页矛盾）不采信；Grok 4.7 规格（2.1T/2.5T/3T）创始人口述 low confidence；DeepSeek 763B/552B 计量差异 tentative；Kimi K4 单一信源 rumor；Gemini 3.8 Audio $3.50/hr（AA 换算）vs per-min 官方定价 = 账单价口径并存——全部维持，不入 claim 页。

---

*Generated 2026-09-20. Sources: Web 检索（openai.com/index/devday-2026、devday.openai.com、deepmind.google 模型卡 gemini-3-8-audio、blog.google 3.8 Live 发布、ai.google.dev 3.8 Live 模型文档、arXiv:2609.07549 Qwen-Audio-3.0-ASR、apple.com newsroom next-gen Apple Intelligence、anthropic.com/system-cards 复核、docs.mistral.ai models 档位页、Moonshot K4 rumor 复核）。Cross-referenced with wiki/synthesis/2026-09-19/tech-report-digest.md（全量基线）、2026-09-18/tech-report-digest.md（Grok 4.7 rollout、Gemini 3.8 Flash/Live 数据与美元口径、Fable 5.2 纪律、DeepSeek 763B 口径）。*