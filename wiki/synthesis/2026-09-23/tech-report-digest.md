---
title: "LLM Tech Report Digest — 2026-09-23"
type: synthesis
created: 2026-09-23
updated: 2026-09-23
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, reasoning, long-context, multimodal, hybrid-architecture, agentic, safety, daily-digest]
---

# LLM Tech Report Digest — 2026-09-23

> 全球主要 AI 公司大模型技术报告速览（截至 2026-09-23）
> 覆盖版：自 2026-09-22 增量版后的全公司覆盖（★ = 09-23 新增确认；⭐ = 官源补 pin/确认）
> 本日主线：**官卡静默于 09-22 被打破——Anthropic Claude Opus 5.5 System Card 与 OpenAI GPT-6 Sol / Luna 在约 90 分钟内先后落地，叠加 xAI Grok 4.7 官方 Model Card（09-21）补 pin，三家 frontier"卡面"同日归位；Qwen3.8-Next 架构技术报告（arXiv:2608.30320）给出 Flash-Next 完整设计**。三条纪律重申：Fable 5.2 rumor 不采信、Grok 4.7 参数量（2.1T）创始人口述 low confidence、DeepSeek 763B/552B 计量口径差异 tentative。

---

## 自 2026-09-22 digest 的 Delta（★ = 09-23 新增确认；⭐ = 官源补 pin）

- **Anthropic Claude Opus 5.5 System Card**（2026-09-22）★——首个 Claude 5.5 家族模型，Opus 5 升级；多数评测匹配/超过 Fable 5.1 与 Mythos 5.1；成本低于 Opus 5 约 40%。终结 09-17 后官卡静默（Anthropic 侧）。
- **OpenAI GPT-6 Sol & GPT-6 Luna**（2026-09-22，Astra 后 19 天、Claude Opus 5.5 后约 90 分钟）★——API + ChatGPT Work + Codex 上线；无独立 system card，09-22 于 GPT-6 Astra System Card 追加 Appendix（同日 HealthBench 数值修正）。
- **xAI Grok 4.7 官方 Model Card**（2026-09-21，media.x.ai PDF）⭐ 补 pin——09-22 digest 仅录发布页；本版补入卡面：500K ctx、四档 reasoning effort、EEBench xhigh 66.0%（卡）vs 64.0%（发布页）⚠️ 数值不一致、CVE-Bench Reward 36.6% （低于 4.6 的 39.8%）、FAIF 双用途生物低于阈值。
- **Qwen3.8-Next 架构技术报告**（arXiv:2608.30320，08-31 投稿）★——Qwen3.8-Flash-Next 完整设计：125B/6B active + 51B n-gram、GDN + 全局 attention 逐层混合、CPT 阶段 QSA、Gated Residual、Muon；8/14 基准领先 397B-A17B 前代。
- **无新增 frontier 报告（上版基础上维持）**：Google（3.8 Flash 09-02 / 3.8 Audio 09-15）、Meta（Muse Spark 1.3 09-02）、DeepSeek（V4.1-Flash arXiv 2609.19969）、NVIDIA（Nemotron 3.5 Lightning + Nemotron 3 Super nightly signal）、Mistral（Ministral 3 = arXiv 2601.08584，1 月报告非新）、Moonshot（K3；K4 单一信源 rumor 维持）。
- ⚠️ **CONTRADICTION（维持）**：kie.ai 声称 Fable 5.2 已于 09-10 发布 vs 官方 system-cards 页最新仍 5.1——维持不采信（09-18 已录）。

---

## 1. Anthropic — Claude Opus 5.5 System Card（★）

- **中文标题**: Claude Opus 5.5 系统卡
- **英文标题**: Claude Opus 5.5 System Card
- **发布机构**: Anthropic
- **模型名称**: Claude Opus 5.5（首个 Claude 5.5 家族模型）
- **发布日期**: 2026-09-22（系统卡 PDF 上线）
- **核心参数**: 参数量未公开；多模态；成本低于 Opus 5 约 40%（低于最大 reasoning effort 即可兑现大部分增益）
- **主要创新点**:
  - Opus 5 升级，多数评测 **匹配或超过 Fable 5.1 与 Mythos 5.1**——5.1 双子发布后 5.5 家族首落，官方以 "best cost-performance up to 40% reduction vs Opus 5" 口径并用
  - 能力增益集中在 **agentic coding / visual reasoning / computer use / long-horizon 专业知识工作**
  - SOTA 项：**Terminal-Bench 4.0、CursorBench、GDPval-AA、AA-Briefcase**
  - **三高风险双用途域护栏**（生物 / 网络 / 前沿 AI 开发）前置披露
- **链接**: [Claude Opus 5.5 System Card PDF](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)
- **口径注**: 系统卡级（Preparedness-style），区别于 Grok 的 model card 级；参数量仍未官方化。与 Fable 5.1 & Mythos 5.1（09-01）并列为 Anthropic 现行前沿卡。

## 2. OpenAI — GPT-6 Sol & Luna（★）

- **中文标题**: GPT-6 Sol 与 GPT-6 Luna（家族第三/四档，无独立系统卡）
- **英文标题**: Announcing GPT-6 Sol and GPT-6 Luna
- **发布机构**: OpenAI
- **模型名称**: GPT-6 Sol / GPT-6 Luna
- **发布日期**: 2026-09-22（18:16 UTC 社区公告；GPT-6 Astra 09-03 之后 19 天）
- **核心参数**:
  - **Sol**: $2 / $10 per M（input/output）、**1.05M ctx**、knowledge cutoff **2026-04-20**
  - **Luna**: $0.10 / $0.50 per M、cutoff **2026-05-18**
  - 参数量未公开；GPT-6 家族 = Astra（$10/$50）/ Sol（$2/$10）/ Luna（$0.10/$0.50）——**无 Terra 档**
- **主要创新点**:
  - **AA Intelligence Index**: GPT-6 Sol **48**（vs GPT-5.6 Sol 47）、GPT-6 Luna 37（与 GPT-5.6 Luna 37 持平）；**Coding Agent Index Sol 57 vs 55**
  - factuality 误差约减半；**deception coding 1.3% / 2.8%（Sol）vs GPT-5.6 Sol 10.4% / 9.5%**
  - **无独立 system card**——09-22 在 [GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra/sec:appendix-210198) 追加 Sol/Luna Appendix；同日 HealthBench 数值修正（misconfiguration 更正）
  - 可用性：API + ChatGPT Work + Codex；Free/Go 用户桌面应用可用 Luna（tiered 体验）；GPT-5.6 系列促销 $4/$20
- **链接**: [OpenAI Community 公告](https://community.openai.com/t/announcing-gpt-6-sol-and-gpt-6-luna-in-the-api-codex-and-chatgpt/1399925)；[GPT-6 Astra System Card（09-22 附录）](https://deploymentsafety.openai.com/gpt-6-astra/)
- **口径注**: 与 Claude Opus 5.5 同日（Grok 4.7 卡后 24h 内），frontier 定价档位下探（Sol=$2/$10 对齐 Grok 4.7、Luna 为 $0.10/$0.50 入门档）——三厂价格-能力赛道完整成形。

## 3. xAI — Grok 4.7 官方 Model Card（⭐ 补 pin，自 09-21）

- **中文标题**: Grok 4.7 官方模型卡
- **英文标题**: Model Card: Grok 4.7
- **发布机构**: SpaceXAI（XAI LLC 的 DBA）
- **模型名称**: Grok 4.7
- **发布日期**: 2026-09-21（模型卡 PDF）；limited rollout 09-17 起；官方发布页同日
- **核心参数**: **500K ctx**；text+image in / text out；**四档 reasoning efforts（low / medium / high / xhigh）**；pretrain cutoff **2026-06**、supplemental 训练至 **2026-08**（含匿名 Cursor workflow 数据）；参数量未披露（2.1T 维持创始人口述 **low confidence**）
- **定价**（与 4.6 同档）：input **$2/M**、output **$6/M**；cached **$0.50/M**；>200K ctx **$4/$12**；**fast 变体 2× 速度 2× 价**（仅 Cursor / Grok Build）
- **卡面基准**（xhigh=最高 effort）:
  - CursorBench 4.0 **46.3** / DeepSWE v1.1 **71.0**（high）/ Terminal-Bench 4.0 **38.0** / FrontierSWE V2 **29.0** mean@5 / EEBench **66.0**（xhigh）
  - ⚠️ **EEBench 数值不一致**：模型卡 66.0 vs 09-21 官方发布页 64.0——卡/页账目差异，tentative
  - LatchBio Capabilities **44.5**；LatchBio BioSecBench refusal **62.4**；CyberGym **80.3**（high）；**CVE-Bench Reward 36.6（低于 Grok 4.6 的 39.8）**
- **安全面**（卡级）: FAIF 双用途生物 **低于阈值**；MASK-Rectified Dishonesty **0.00%**、Sycophancy **0.03%**、self-harm compliance **1.05%**；HackerBench harmful compliance high **3.31%** / xhigh **4.02%**
- **链接**: [Grok 4.7 Model Card PDF](https://media.x.ai/v1/website/4p7card-5eccc980.pdf)；[x.ai/news/grok-4-7](https://x.ai/news/grok-4-7)
- **口径注**: 卡面级（model card），非 Preparedness-style system card；参数量依然未官方化。安全底层较 blog 级发布页完整（FAIF/MASK/sycophancy/self-harm 全套），但 CVE-Bench 反超 4.6 未成。

## 4. Qwen — Qwen3.8-Next 架构技术报告（★）

- **中文标题**: Qwen3.8-Next：原生序列架构的类型化混合（架构技术报告）
- **英文标题**: Qwen3.8-Next Architecture Technical Report
- **发布机构**: Alibaba / Qwen Team
- **模型名称**: Qwen3.8-Flash-Next（序号模型线：Qwen3.8-Next 架构族）
- **发布日期**: arXiv 投稿 2026-08-31（**arXiv:2608.30320**）
- **核心参数**: **125B 总参 / 6B active** + **51B n-gram 嵌入表**（off-accelerator 系统 RAM）；layer-wise hybrid——**Gated DeltaNet (GDN)** + 每 4 层 1 个全局 attention 层；CPT 阶段换 **Qwen Sparse Attention (QSA)**；**Gated Residual (GR) 四分支残差流**；**Muon** 优化器
- **主要创新点**:
  - 14 项预训练基准中 **8 项领先 397B-A17B 前代**、其余差距 ≤2.6 分——仅用 **1/3 activated params、1/3 tokens、~1/9 FLOPs**
  - "类型化混合"（typed mixing）方法论：注意力/线性 recurrence/稀疏 attention 按需求分层装配
  - N-gram 非激活参数池 + off-accelerator 记账延续中系稀疏记账手法（09-19 已录 Flash-Next 线）
- **链接**: [arXiv:2608.30320](https://arxiv.org/abs/2608.30320)
- **定位注**: 09-23 兄弟页 `arxiv-daily` 收录的 **Qwen3.8-Omni**（2609.25611，原生 omni-modal agentic、1M ctx）声明"inherits Qwen3.8-Next's sparse MoE"——本报告为其架构底座出口。

## 5. 其他目标机构（逐家复核 — 无新增，参照 09-22/09-19 记录）

| 机构 | 最新有效报告 | 日期 | 状态 |
|------|-------------|------|------|
| Google | Gemini 3.8 Flash Model Card（AA ≈59、$0.75–3.75/M）；3.8 Live / Live-ET（09-15，S2S ≈82.6）；3.8 Audio 卡 | 09-02 / 09-15 | 维持 |
| Meta | Muse Spark 1.3（1.05M ctx，AA ≈60）；Muse Glimmer（08-10） | 09-02 | 维持 |
| DeepSeek | V4.1-Flash TR（arXiv:2609.19969，552B MoE / CSA2+FP4 / SWA Bounded Replay）；763B 口径差异 tentative | 09-17 | 维持 |
| Microsoft | MAI-Thinking-1 白皮书（1T/35B，no-distillation）；MAI-Code-1.1-Flash（138B/256K） | 06-02 / 08 | 维持 |
| NVIDIA | Nemotron 3 Family TR（2512.20856）+ 3.5 Lightning（30B-A3B，09-16 SageMaker 支持）；Nemotron 3 Super 120B-A12B nightly signal | 2025-12 起 | 维持 |
| Apple | AFM 3（Core 3B / Core Advanced 20B sparse 1–4B active）；2026 年度技术报告仍缺席 | 06-08 | 维持 |
| Moonshot | Kimi K3（2.8T-A104B，arXiv:2607.24653）；**K4 = The Information 单一信源 rumor**（Blackwell GPU 网罗传闻，无官方确认） | 07-16 | 维持 |
| Mistral | Ministral 3（arXiv:2601.08584；3B/8B/14B dense、Cascade Distillation）；非 9 月新报告 | 2026-01 | 维持 |
| Amazon | Nova 2（Lite/Pro/Omni/Sonic，≤1M ctx） | 2025-12-02 | 维持 |
| 智谱 GLM | GLM-5.3（CyberGym 84.5 / NIST CAISI 开源最强）+ GLM-5（2602.15763v2）；GLM-5.3-FlashX | 08-14 | 维持 |
| StepFun | **Step 5 Preview**（600B-A27B、1M ctx、权重 10-15 开源） | 09-18/20 | 维持 |
| ByteDance | Seed2.0 Model Card（Pro/Lite/Mini） | 02-14 | 维持 |
| InternLM | Intern-S2-397B（Apache-2.0，09-13）；Intern-S2-Preview（2608.13505） | 09-13 | 维持 |
| Baichuan | Baichuan-M4（arXiv:2606.08982，医疗 Agent，SPAR++） | 06 | 维持 |
| 01.AI | Yi-Lightning（2024-10-16）零动态（四次复核一致） | — | 维持 |
| MiniMax | M3（428B-A23B）+ H3 预热 | 06-16 | 维持 |

---

## 本日头条与动态（相对 2026-09-22 增量版）

### 1. 官卡静默终结：Opus 5.5 → Sol/Luna → Grok 4.7 卡 24 小时窗口
- 09-17 起的官方 frontier 系统卡静默在 09-22 被 Anthropic + OpenAI 接力打破；xAI 官方 model card（09-21）补 pin 后，"无新卡"叙述正式失效——**下一静默观察窗口重置**。事件节点维持：**09-29 DevDay**、10-14 GPT-5.5 系列退役、10-15 Step 5 权重开源。

### 2. 三档价格-能力赛道完整成形（2026 秋季定价表）
- 旗舰线：Fable 5.1 / GPT-6 Astra / Opus 5.5（$10/$50 档）；中档：Grok 4.7 = Sol = $2/$10；入门：Luna $0.10/$0.50——与中系开源线（DeepSeek V4.1-Flash / Step 5 / GLM-5.3）构成"价格×能力"双轴竞争。**Luna 的 $0.10 input 为 frontier 家族最低档**。

### 3. EEBench 卡/页不一致 + CVE-Bench 倒退 → 官卡临界解读
- Grok 4.7 模型卡 EEBench 66.0 vs 发布页 64.0（tentative）；CVE-Bench Reward 36.6 低于 4.6 的 39.8——**xAI 系统安全面"有升有降"，不宜以单一指标论卡**；参数量持续缺位（2.1T low confidence）。

### 4. 今日 Delta 汇总（★ 新增 4 项 + ⭐ 补 pin 1 项）
| 公司/机构 | 新增项 | 日期 | 类型 |
|-----------|--------|------|------|
| Anthropic | **Claude Opus 5.5 System Card**（首个 5.5 家族；SOTA Terminal-Bench 4.0/CursorBench/GDPval-AA；成本 -40%）★ | 2026-09-22 | 官方系统卡 |
| OpenAI | **GPT-6 Sol & Luna**（$2/$10 与 $0.10/$0.50；Astra 卡 09-22 附录）★ | 2026-09-22 | 官方模型 |
| xAI | **Grok 4.7 官方 Model Card**（500K ctx、四档 effort、EEBench 66.0 vs 页 64.0）⭐ | 2026-09-21 | 官方卡补 pin |
| Qwen | **Qwen3.8-Next Architecture TR**（arXiv:2608.30320；125B-A6B + 51B N-gram）★ | 2026-08-31 | arXiv 技术报告 |

---

## 交叉主题分析

### 1. "卡面三极"再分层：system card / model card / 无卡
- 09-22 后三厂口径分层清晰：Anthropic = Preparedness-style **system card**（安全前置 + 成本-性能）；xAI = **model card**（参数缺位但安全面完整，EEBench 卡/页不符待复核）；OpenAI = **无独立卡**，以 Astra 卡附录补齐（HealthBench 数值同页修正）。**frontier 状态追踪以"cell：卡级 + 账目 + 参数量披露度"三列为准**。

### 2. 中系稀疏记账与"原生架构混合"叙事汇流
- Qwen3.8-Next（GDN+attention+QSA typed mixing）、DeepSeek V4.1-Flash（CED/CSA2）、Kimi K3（KDA+Stable LatentMoE）、Nemotron（SSM+attention）——**"typed mixing / 分层混合"成为 2026 秋季架构共同语言**；Flash-Next 以 ~1/9 FLOPs 追平前代旗舰是"账面稀疏 + 激活高效"最清晰的单点证据。

### 3. 纪律重申（无变化）
- Fable 5.2（kie.ai 09-10 claim）不采信；Grok 4.7 参数量（2.1T）创始人口述 low confidence；DeepSeek 763B vs 552B 计量口径差异 tentative；Kimi K4 单一信源 rumor；Opus 5.2 灰度 signal-layer 不入 claim 页——全部维持。

---

*Generated 2026-09-23. Sources: Web 检索（Claude Opus 5.5 System Card PDF 2026-09-22、OpenAI Community GPT-6 Sol/Luna 公告 2026-09-22、deploymentsafety.openai.com GPT-6 Astra System Card 附录 09-22、media.x.ai Grok 4.7 Model Card PDF 09-21、x.ai/news/grok-4-7、arXiv:2608.30320 Qwen3.8-Next、anthropic.com/system-cards 复核、openai.com/index/gpt-6-astra/；其余公司状态沿用 09-22/09-19 digest 复核基线：deepseek.com 2609.19969、research.meta.ai Muse Spark、blog.google 3.8 Flash、aws nemotron SageMaker、aitoolsreview kimi-k4 rumor、devday 09-29）。Cross-referenced with wiki/synthesis/2026-09-22/tech-report-digest.md（增量基线）、wiki/synthesis/2026-09-19/tech-report-digest.md（全量基线）、wiki/synthesis/2026-09-23/arxiv-daily.md（Qwen3.8-Omni 2609.25611 架构互证）、wiki/synthesis/2026-09-23/arxiv-ai-search.md、wiki/synthesis/2026-09-23/arxiv-paper-check.md。*