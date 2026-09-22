---
title: "LLM Tech Report Digest — 2026-09-22"
type: synthesis
created: 2026-09-22
updated: 2026-09-22
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, reasoning, long-context, multimodal, hybrid-architecture, agentic, enterprise, safety, daily-digest]
---

# LLM Tech Report Digest — 2026-09-22

> 全球主要 AI 公司大模型技术报告速览（截至 2026-09-22）
> 增量版：聚焦自 2026-09-20 增量版后的新增/确认项（★ = 新收录；⭐ = 官源补 pin/确认）
> 本日主线：**xAI Grok 4.7 官方发布页于 09-21 正式上线（x.ai/news/grok-4-7）——终结 09-17 起的 "limited rollout 无卡/无定价/无基准" 状态，官方定价 $2/$6 per M + 首套官方基准/安全数据落地**；stepfun 发布 Step 5 Preview（600B-A27B 稀疏 MoE，全球开源模型前三）；Qwen3.8-Omni-Flash（09-18 原生全模态）补收录。OpenAI / Anthropic / Google / Meta 官方 frontier 系统卡仍静默（无新卡），下一官方节点 = **09-29 OpenAI DevDay**。三条纪律保留：Fable 5.2 rumor 不采信、Grok 4.7 参数量（2.1T）创始人口述 low confidence、DeepSeek 763B/552B 计量口径差异 tentative。

---

## 自 2026-09-20 digest 的 Delta（★ = 09-22 新增确认/收录）

- **xAI Grok 4.7 官方发布**（x.ai/news/grok-4-7，09-21）——官方定价 + 七档官方基准 + 安全数据首次落地，直接推翻 09-20 digest "limited rollout 无卡/无定价/无基准" 口径；参数量仍未官方化（2.1T 维持创始人口述 low confidence），无正式 system card。
- **StepFun Step 5 Preview**（09-18 发布/09-20 媒体广泛报道）——旗舰推理/Agentic 稀疏 MoE，Keygate 与 AA 双口径进入全球开源前二/前三，API 全量开放、权重 10-15 开源。
- **Qwen3.8-Omni-Flash**（09-18）——原生全模态（text/audio/image/video），1M ctx，补录技术报告 digest（此前仅投资侧收录）。
- **NVIDIA Nemotron 3 Super 120B-A12B nightly 训练 recipe + 权重胶囊**（docs.nvidia.com/nemotron/nightly，09-21 观察）——signal-layer/tentative，尚未正式发布卡。
- **Anthropic Opus 5.2 灰度测试信号**（aibase 09-16，仅 Claude Code 环境）——signal-layer low confidence，维持不升级确认。
- **无新 frontier 系统卡**：Anthropic（Fable 5.1 & Mythos 5.1 09-01）、OpenAI（GPT-6 Astra 09-03 / GPT-5.6 07-09）、Google（3.8 Flash 09-02）、Meta（Muse Spark 1.3 09-02）全部维持。
- ⚠️ **CONTRADICTION（维持）**：kie.ai 声称 Fable 5.2 已于 09-10 发布 vs 官方 system-cards 页最新仍 5.1——维持不采信（09-18 已录）。

---

## 1. xAI — Grok 4.7 官方发布（★ 官方发布页，终结 limited rollout 状态）

- **中文标题**: Grok 4.7 官方发布博客
- **英文标题**: Introducing Grok 4.7
- **发布机构**: SpaceXAI（xAI）
- **模型名称**: Grok 4.7（Grok Build / Grok API / Cursor / 模型路由与云平台）
- **发布日期**: 2026-09-21（官方发布页）；limited rollout 自 09-17
- **核心参数**: 使用相对 4.6 更大规模的新基座；更长 RL run、面向"多小时长程任务"的更硬任务混合；官方未披露参数量（2.1T 维持创始人口述 low confidence）
- **定价**（与 4.6 同档）：input **$2/M**、output **$6/M**；另有 2× 输出速度的 fast 变体（2× 价）——"Twice as fast, at half the price of comparable models"
- **官方基准**（Grok 4.7 vs 4.6 / GPT-5.6 Sol / Fable 5.1）:
  - CursorBench 4.0：46.3 / 40.4 / 41.7 / 51.8
  - DeepSWE v1.1：71.0*（high effort）/ 65.2 / 72.7 / 70.0
  - EEBench：64.0 / 53.0 / 39.4 / 56.4
  - AA Briefcase v1.1：1,657 / 1,546 / 1,487 / 1,678
  - Terminal-Bench 4.0：38.0 / 20.3 / 37.3 / 57.9
  - Harvey Legal Agent：19.6 / 15.8 / 2.5 / 6.7
  - HealthBench Pro：56.7 / 48.5 / 60.5 / 62.1
  - GDPval（Elo）：**Grok 4.7 (xhigh) 1735** > Fable 5.1 (max) 1695 > Grok 4.6 (high) 1605 > GPT-6 Astra (max) 1542
- **主要创新点**:
  - 更长 RL 训练 + 多小时长程任务加权，自校验（self-verification）与长上下文管理更强
  - 原生理解 **Grok Bot** harness（对话/通用知识工作）
  - **全新安全栈**：最高 refusal / jailbreak 抗性；LatchBio biosafety **62.4%**（登顶）；HackerBench v0.3 仅放行 **3.3%** risky dual-use prompts；向选定网络安全伙伴开放 red-team 邀请访问
- **可用性**: Cursor、Grok Build（免费试用）、Grok API、第三方 coding harness、模型路由与云平台
- **链接**: [x.ai/news/grok-4-7](https://x.ai/news/grok-4-7)
- **口径注**: 官方发布页 ≠ 系统卡/模型卡——安全声明为 blog 级而非 Preparedness-style 卡面；参数量未官方化。

## 2. StepFun — Step 5 Preview（★ 新收录）

- **中文标题**: Step 5 Preview——旗舰推理/Agentic 稀疏 MoE 基座
- **英文标题**: Step 5 Preview（sparse MoE reasoning/agentic flagship）
- **发布机构**: 阶跃星辰（StepFun）
- **模型名称**: Step 5 Preview
- **发布日期**: 2026-09-18（发布）；09-20 媒体广泛报道（sohu 等）
- **核心参数**: **600B 总参 / 27B 激活**稀疏 MoE；**1M ctx**；原生文本+视觉（vision-language）；推理模型
- **主要创新点**:
  - Keygate "Comprehensive Intelligence" **43.6** / AA Intelligence Index **44**，全球开源模型前三
  - **单任务成本 ≈ 1/8 的 Claude Opus 5**（报告口径）
  - API 已全量开放；**权重 2026-10-15 开源**（官网公布）
- **链接**: [sohu 09-20 报道](https://www.sohu.com/a/step5-preview)（次级）；Keygate 模型页（09-18）
- **观察**: 与 DeepSeek V4.1-Flash、Qwen3.8-Max、GLM-5.3 并列中系 2026 秋季旗舰线；"600B/27B active + 1M ctx + 权重开源" 组合延续中系"账面稀疏高激活比 + 低价开放"路线。

## 3. Qwen — Qwen3.8-Omni-Flash（★ 补收录，09-18）

- **中文标题**: Qwen3.8-Omni-Flash——原生全模态模型
- **英文标题**: Qwen3.8-Omni-Flash（native omnimodal）
- **发布机构**: Alibaba / Qwen Team
- **模型名称**: Qwen3.8-Omni-Flash
- **发布日期**: 2026-09-18
- **核心参数**: 原生全模态（text / audio / image / video 统一输入）；**1M ctx**
- **主要创新点**: 单一模型覆盖全模态理解 + 生成，一键 API 全模态对话；此前已由 09-19 投资日报收录，本 digest 补录
- **定位注**: 与 Qwen3.8-Max-0902（09-02 快照，编码/长程自主开发能力升级）、Qwen-Audio-3.0-ASR（arXiv:2609.07549）构成 3.8 系生态

## 4. OpenAI — DevDay 2026 临门 + 灰度层信号（维持 + 补 pin）

- **DevDay 2026**：**2026-09-29（周二）旧金山 Fort Mason**，keynote 免费 livestream，Sam Altman 出席——下一官方节点进入 7 天倒计时（本 digest 里程碑）
- **GPT-6 Sol 灰度测试信号**（aibase 09-16，CometAPI 传闻线）——Arena/API 层出现 Sol 踪迹（OpenAI Community），维持 rumor 级，不入 claim 页
- **GPT-5.5 系列退役**：2026-10-14 起下线（GPT-5.5 / 5.5-mini / 5.5-nano），指向 DevDay 前后架构切换
- ⚠️ "28K tokens / 3 min" 类性能传闻低置信度，不收录
- **最新卡维持**：GPT-6 Astra（09-03，首个 Preparedness Critical 网络安全级；AEL 59.3%；1.05M ctx / 128K out；$10/$50 per M）；GPT-5.6（07-09，Sol/Terra/Luna）

## 5. Anthropic — Opus 5.2 灰度信号层观察（signal-layer，无新卡）

- **官方卡维持**：Fable 5.1 & Mythos 5.1（09-01）——system-cards 页无新
- **Opus 5.2 灰度测试**（aibase 09-16，low confidence）——仅出现在 **Claude Code 环境**，与正式发布分离；signal-layer 记录，不升级为确认事件
- **Fable 5.2 rumor 维持不采信**；企业侧 26% AI 研发使用 Claude（R&D 指标，非本 digest 核心）

## 6. Google — API 文档双新增（语音侧，非 frontier 卡）

- **Gemini 3.5 Live Translate**（API docs，preview）——语音到语音翻译，70+ 语言；延续 3.8 Audio/Live 语音线的工具侧补充（非模型卡）
- **Gemini 3.5 Transcribe**（API docs）——流式 ASR，utterance 语种检测（UAD）、说话人分离（diarization）、word-level timestamps
- **Gemini 3.8 Flash**（09-02 GA）维持；3.8 Flash Cyber（受限变体）维持；Lyria 3.5 音乐生成公开预览（09-03）维持
- **无新 frontier 模型卡**；3.8 Flash / 3.8 Flash Cyber / 3.8 Audio（09-15 卡）为当前全档位

## 7. Meta — Muse 语音/轻量补录两款（⭐ gap-fill，09-22 补 pin）

- **Muse Voice Transcribe**（09-02，⭐ 补录）——Superintelligence Labs 首个实时流式语音识别；自回归多模态；WER 3.1%；20+ 说话人 diarization；70+ 语言（25 认证）；定价 ~$0.18/hr
- **Muse Glimmer**（08-10，⭐ 补录）——**30B（配合 1.8B ViT-G）Apache 2.0 开源权重**；单消费级 GPU 本地运行（~4-bit <20GB）；文本+图像；100+ 语言；Muse Spark 蒸馏
- **Muse Spark 1.3**（09-02，1.05M ctx，AA ≈60）维持；无 Muse Spark 1.4

## 8. Microsoft — MAI-Code-1.1-Flash（★ 补收录）

- **中文标题**: MAI-Code-1.1-Flash 补充收录
- **发布机构**: Microsoft MAI
- **模型名称**: MAI-Code-1.1-Flash
- **发布日期**: 2026-08（补录）
- **核心参数**: **138B**、**256K ctx**、多模态；定价 $0.20 / $1.20 per M（代码档低价区）
- **维持项**: MAI-Thinking-1（1T/35B，06-02 白皮书，no-distillation 从零训练）为最新旗舰；Phi-5 仍无官方报告

## 9. NVIDIA — Nemotron 3 Super 120B-A12B nightly recipe（signal-layer/tentative）

- **观察**：docs.nvidia.com/nemotron/nightly 出现 **Nemotron 3 Super 120B-A12B** 训练 recipe + 权重胶囊（BF16 / FP8 / NVFP4 变体）
- **推断要点**: hybrid Mamba-Transformer MoE + LatentMoE + MTP（延续 Nemotron 3 家族线）；120B-A12B = 12B 激活档
- **口径**: nightly 文档 = signal-layer 先行，正式模型卡未发布，tentative；延续 Nemotron 3.5 Lightning（30B-A3B）与 Nemotron 3 Ultra 记录

## 10. 智谱 GLM — NIST CAISI 网络能力评估（⭐ 补 pin）+ FlashX

- **NIST CAISI 评估**（09-17）——**GLM-5.3 为网络能力最强的开源权重模型**；相对于美国 frontier 模型落后 ~4 个月（官方/评估层口径，非自评）
- **GLM-5.3-FlashX**（09-18）——200 tok/s，国产芯片 10 万张全流程（此前投资日报已录）
- **维持项**: GLM-5.3（08-14，CyberGym 84.5）+ GLM-5（2602.15763v2）；CyberGym 84.5 与 NIST CAISI 结论互证"开源最强 cyber"定位

## 11. 其他目标机构（参照 — 无新增，逐条复核）

- **DeepSeek**：最新仍 V4.1-Flash 技术报告 arXiv:2609.19969（09-17 投稿，552B MoE CED / 8B-16B active / CSA2+FP4 → 890 B/token / SWA Bounded Replay ≈1/8 SSD）；763B vs 552B 计量口径差异维持 tentative；无新
- **Apple**：无新技术报告；官网 ML 研究页 AFM 3（Core 3B dense / Core Advanced 20B sparse，IFP 剪枝 + flash 存储，1-4B 激活，与 Google 联合）09-18 仍为最新；2026 年度技术报告继续爽约
- **Moonshot Kimi**：K3（2.8T-A104B，07-16）最新；**K4 传闻维持 rumor**（无任何官方规格/日期）；K3.1/K3.5 无官方
- **Mistral**：无新 frontier 技术报告（档位维护沿 09-20 记录）
- **Amazon**：Nova 2 技术报告仍为 2025-12-02；无 2026 Nova 新卡
- **ByteDance**：Seed 2.0 卡维持；2026 命题（世界模型至 Genie 3 级、Seedance SOTA、coding）无新报告
- **MiniMax**：M3（06-16）+ H3 预热维持；无新
- **01.AI / Yi**：零动态（四次复核一致），最新仍 Yi-Lightning（2024-10-16）
- **Baichuan**：战略收缩至医疗 AI（Baichuan-M4）维持，无新 LLM 报告
- **InternLM / 上海 AI Lab**：无新技术报告；InternAgent 为 agent 框架（08-14 开源）非模型报告

---

## 本日头条与动态（相对 2026-09-20 增量版的 Delta）

### 1. Grok 4.7：从 "limited rollout 无卡无定价" 到 "官方发布页落档"
- 09-21 官方页给出首套**官方基准**与**官方定价**（$2/$6，fast 2× 价），并配 CursorBench 4.0 价格-性能前沿图——终结两周的"quota 先行、卡面滞后"状态。**但**：无参数量、无 system card，安全为 blog 级声明；GPT-5.6 Sol 在 CursorBench 4.0（41.7 vs 46.3）与 Terminal-Bench 4.0（37.3 vs 38.0）被 Grok 4.7 反超，而 Fable 5.1 仍在 CursorBench/Terminal-Bench 领跑——**档位于中端偏上，未称王**。

### 2. 开盘价 vs 旗舰价的三轨定价再次显形
- $2/$6（Grok 4.7）· $4/$20（GPT-5.6 Sol）· $10/$50（GPT-6 Astra / Fable 5.1 Max 参照）——OpenAI 三档与 xAI 同价加量构成"价格-性能赛道"，中系以 Step 5（600B-A27B，成本 1/8 Opus 5 宣称）与 V4.1-Flash 压价。**成本曲线双线竞争延续**。

### 3. 无新 frontier 卡静默第 7 天 → 事件日历收窄到 DevDay 09-29
- 09-17（DeepSeek arXiv + Grok 4.7 quota）之后仍无新卡；**09-29 DevDay + 10-14 GPT-5.5 系列退役 + 10-15 Step 5 权重开源**为近两周三个确定性时间锚。

### 4. 今日 Delta 汇总（★ 新增 4 项 + ⭐ 补 pin 2 项）
| 公司/机构 | 新增项 | 日期 | 类型 |
|-----------|--------|------|------|
| xAI | Grok 4.7 官方发布页（定价 $2/$6 + 七档官方基准 + HackerBench 3.3% 放行安全数据）★ | 2026-09-21 | 官方发布 |
| StepFun | Step 5 Preview（600B-A27B、1M ctx、AA/Keygate 双口径开源前三、权重 10-15 开源）★ | 2026-09-18/20 | 官方模型 |
| Qwen | Qwen3.8-Omni-Flash 原生全模态（1M ctx）★ 补收录 | 2026-09-18 | 官方模型 |
| Microsoft | MAI-Code-1.1-Flash（138B/256K，$0.20/$1.20）★ 补收录 | 2026-08 | 官方模型 |
| Meta | Muse Voice Transcribe（09-02）+ Muse Glimmer（08-10，30B Apache 2.0）⭐ 补 pin | 2026-08/09 | gap-fill |
| NVIDIA | Nemotron 3 Super 120B-A12B nightly recipe（signal-layer）◆ | 2026-09-21 | signal-layer |

---

## 交叉主题分析

### 1. "发布页 ≠ 系统卡"成为新常态
- Grok 4.7 官方发布页已给定价+基准+安全摘要，但无 Preparedness-style 卡面、无参数量。**track frontier 状态以"官方页 + 卡页 + docs"三源并存为准**；blog 级安全声明与卡级安全评估分层记录（延续 Gemini 3.8 Audio"卡面化"对照叙事）。

### 2. 中系旗舰线 2026 秋季落位完整
- DeepSeek V4.1-Flash（552B-A16B，arXiv）· Qwen3.8-Max/Omni-Flash · Step 5 Preview（600B-A27B）· GLM-5.3/FlashX——四家齐发，共同特征：**高稀疏激活比 + 长上下文（1M）+ 低价/开源**；Step 5 以 600B-A27B 与"1/8 Opus 5 成本"成中系单任务成本标杆。

### 3. 语音/端侧报告仍是 9 月下旬主要信号源
- Google Live Translate/Transcribe 工具侧、Meta Muse Voice Transcribe、Qwen-Omni-Flash——旗舰卡之外，语音与端侧（AFM 3 端侧参考）持续贡献确认级信号。**audio/open-weights 两战场围绕 09-29 DevDay 前竞跑**。

### 4. 纪律重申（无变化）
- Fable 5.2（kie.ai，与官方页矛盾）不采信；Grok 4.7 规格（2.1T/2.5T/3T）创始人口述 low confidence；DeepSeek 763B/552B 计量差异 tentative；Kimi K4 单一信源 rumor；Opus 5.2 灰度 = signal-layer 不入 claim 页——全部维持。

---

*Generated 2026-09-22. Sources: Web 检索（x.ai/news/grok-4-7 官方发布页、x.ai/news/grok-4-6 参照、anthropic.com/system-cards 复核、ai.google.dev Gemini 3.5 Live Translate/Transcribe API 文档复核、docs.nvidia.com/nemotron/nightly、aibase 09-16 Opus 5.2 / GPT-6 Sol 传闻、sohu Step 5 Preview 09-20、Keygate Step 5 Preview 模型页、Meta AI Muse Voice Transcribe 09-02、Muse Glimmer 08-10、deepseek.com 官方新闻复核、apple machinelearning.research 页复核、qwen 官方 09-18、MS MAI-Code-1.1-Flash、NIST CAISI GLM-5.3 09-17、03-02/03-03 recall 复核）。Cross-referenced with wiki/synthesis/2026-09-20/tech-report-digest.md（增量基线）、2026-09-19/tech-report-digest.md（全量基线）、2026-09-18/tech-report-digest.md（Grok 4.7 rollout、纪律）、09-19 investment-daily（Qwen3.8-Omni-Flash/GLM-5.3-FlashX 首次收录）。*