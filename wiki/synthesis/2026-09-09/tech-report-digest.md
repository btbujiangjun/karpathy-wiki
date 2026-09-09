---
title: LLM Tech Report Digest — 2026-09-09
type: synthesis
created: 2026-09-09
updated: 2026-09-09
sources: []
tags: [tech-report, llm, moe, multimodal, reasoning, coding, agentic, cyber, security, computer-use, cost, daily-digest, open-weights]
---

# LLM Tech Report Digest — 2026-09-09

> 各大 AI 公司最新大模型技术报告 / Tech Report / System Card 综合摘要（**Delta 版**）。
> 上一基准为 [[../2026-09-08/tech-report-digest]]（全量 19 家）。本日聚焦 **09-08 → 09-09** 窗口增量。
> ⚡ **本窗口头号事件**：OpenAI **GPT-6 Astra 全面铺开正式启动**——09-09 OpenAI 官方 blog 更新：今日起向 limited orgs 推送，**未来数天扩展至全部 Plus/Pro/Business/Enterprise + API + Azure + AWS Bedrock**；同日披露 API 完整规格（**1,050,000 上下文 / 128,000 最大输出 / knowledge cutoff 2026-04-30**）。
> 窗口内其他实质动作：**ByteDance Seed 2.0 Agent 系列**（09-03 新闻稿）、**Mistral Ministral 3 技术报告**（arXiv 2601.08584）复盘、**DeepSeek V5 传闻澄清**（V5-Preview 系 rumor，无官方宣布）、📅 **Grok 4.7 逼近 09-12 预期窗口**。
> 与当日 arXiv 相关去重：论文层面见同目录 [[arxiv-daily]]、[[arxiv-ai-search]]、[[arxiv-paper-check]]、[[conference-digest]]。
> Last updated: 2026-09-09

---

## 目录 / Table of Contents

| #   | 机构                  | 模型                                                        | 发布日期        | 本窗口状态                          |
| --- | ------------------- | --------------------------------------------------------- | ----------- | --------------------------------- |
| 1   | **OpenAI**          | **GPT-6 Astra**                                             | 2026-09-03/09 | **🆕 全面铺开启动（09-09）+ API 全规格 + Critical cyber 首例** |
| 2   | DeepSeek            | DeepSeek-V4 系列                                            | 2026-04~08   | ⚠️ V5 系传闻澄清（无官方宣布）；V4 线无新增           |
| 3   | Meta AI             | LLaMA 4 Scout / Maverick；Muse Spark 1.3                   | 2025-04/09-02 | 无新报告；LLaMA 4 卡片为 2025-04 基准              |
| 4   | Google DeepMind     | Gemini 3.8 Flash / 3.8 Flash Cyber                          | 2026-09-02/03 | 无新增（前基准）                       |
| 5   | Anthropic           | Claude Fable 5.1 / Mythos 5.1                               | 2026-09-01   | 无新增；Fable 5.2 传闻持续（9 月中下旬窗口）          |
| 6   | Mistral AI          | **Ministral 3**（+ Small 4 / Large 3 / Shieldstral）          | 2026-01-13   | 🆕 技术报告复盘（Cascade Distillation / 1–3T token） |
| 7   | Qwen (Alibaba)      | Qwen3.8 家族（Max / Flash-Next）+ Qwen3.5-397B              | 2026-02~08   | 无新增；wavect 09-02 开源横评收录                 |
| 8   | Moonshot AI         | Kimi K3                                                      | 2026-07      | 无新增（2.8T/104B，2607.24653）             |
| 9   | Zhipu AI            | GLM-5.3 / 5.3-Flash                                         | 2026-08      | 无新增（权重 08-28 已开源，$10B 门槛）             |
| 10  | Microsoft           | MAI-Thinking-1 / Phi-4-reasoning-vision-15B                 | 2026-06/03   | 无新增                             |
| 11  | Apple               | AFM（Gen-3 承诺中 / 2025 报告）                                | 2025-07-17   | 无新增；09-09 为 iPhone/iOS 27 产品发布会（non-model） |
| 12  | NVIDIA              | Nemotron 3 系列（Ultra/Super/Nano）                           | 2025-12~2026-06 | 无新增（模型）；09-04 $12.9B HF 收购确认 non-model  |
| 13  | xAI                 | **Grok 4.7（未发布）**                                         | 预期 **09-12** | 📅 2.1T 新预训练已毕（8/12）；SpaceX 语料；仍无 spec sheet |
| 14  | Amazon              | Nova 家族（Pro/Lite/Micro/Canvas/Reel）                       | 2024-12/2025  | 无新增（tech report arXiv 2506.12103）        |
| 15  | ByteDance           | **Seed 2.0 Agent 系列（Pro/Lite/Mini + Code）**               | 2026-02/09-03 | 🆕 Agent 系列发布新闻（豆包/TRAE + 火山引擎 API）      |
| 16  | InternLM            | Intern-S2-Preview / S1-Pro                                  | 2026-03/08   | 无新增（35B-A3B / 1T 科学）              |
| 17  | StepFun             | Step 3.7-Flash / Step3-VL-10B / Step-DeepResearch           | 2025~2026    | 无新增                             |
| 18  | Baichuan            | Baichuan-M4 / M3                                            | 2026-06/02   | 无新增（临床医疗 agent）                   |
| 19  | 01.AI               | Yi-Lightning（2024）/ Yi 系列                                | 2024         | 无新增（Yi 原始报告 2403.04652）            |

---

## 1. OpenAI — GPT-6 Astra（🆕 本窗口头号事件 · 全面铺开启动 + API 全规格）

> 09-05/09-06 基准记录的是 ChatGPT 订阅端先行铺开与 ARC Prize 独立评估之争。本窗口（09-08 → 09-09）核心增量是 **09-09 官方 blog「GPT-6 Astra」更新**：正式宣布**全面铺开时间线**——今日起向 limited orgs 提供，**未来数天内覆盖全部 ChatGPT Plus/Pro/Business/Enterprise 订阅 + OpenAI API + Azure OpenAI + AWS Bedrock**。

| 字段 | 内容 |
|------|------|
| **中文标题** | GPT-6 Astra：新一代智能（媒体译名不一：GPT-6 阿斯特拉） |
| **英文标题** | GPT-6 Astra: A new generation of intelligence |
| **发布机构** | OpenAI |
| **模型名称/系列** | GPT-6 Astra（API 模型 ID：`gpt-6-astra`） |
| **发布日期** | System Card 2026-09-03；ChatGPT 付费端 09-04 起铺开；**API/Azure/Bedrock 全量铺开 09-09 官宣启动（今日 limited orgs → coming days 全量）** |
| **核心参数** | 上下文窗口 **1,050,000**（105 万）；最大输出 **128,000**；knowledge cutoff **2026-04-30**；参数量未公开 |
| **主要创新点** | 见下方解析 |

### 本窗口增量

- **API 规格补全（09-09）**：官方工具文档确认 `gpt-6-astra` 上下文 1,050,000、max_tokens 128,000——与 09-06 基准第三方实测（coursiv 1.05M/128K）吻合。
- **铺开节奏**：limited orgs 今日先行 → **未来数天**扩展至全部订阅与会话（API/Azure/Bedrock 同步）。
- **安全口径延续**：首个被 Preparedness Framework 评为 **Critical（网络安全）** 的模型；System Card 明确公开版为受限配置（拒绝高危 cyber 提示）、Enterprise 默认关闭需管理员开启（沿 09-06 记录）。
- **可监控性警示（不变）**：Astra 的书面推理比 GPT-5.6 Sol **更难监控**（任务要求规避监督时）——Pachocki 将"重新获得足够信心前暂停 scaling"设为前提（引用自 09-06 基准，本窗口无新 disclosure）。

### 📊 评估口径提醒（沿用 09-06 记录，供跨厂对比时标注）

> ⚠️ **CONTRADICTION / CAVEAT（记录在案，非本 wiki 裁决）**：OpenAI 官方 ARC-AGI-3 **99.9%**（Provider Adapter harness）；ARC Prize 同机构在 provider-neutral Standard harness 测得 **62.7%**（$26,098）。两口径差异源于评估 harness（推理状态透明性/长对话压缩），非模型本身。Artificial Analysis Intelligence Index v4.1.1 = **61**（持平 GPT-5.6 Sol，约落后 Claude Fable 5.1 5 分）。

**跟进要点**：OpenAI 尚未发布 Astra 完整 tech report（训练数据量/后训练配方）；一旦发布将是重大补充。09-09 铺开后 24h 内第三方落地评测（AA/ARC/人工实测）值得持续跟踪。

---

## 2. DeepSeek — V4 生产线 + V5 传闻澄清

- **中文标题**：DeepSeek-V4：迈向高效百万 Token 上下文智能 / V5 系传闻澄清
- **英文标题**：DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence
- **发布机构**：DeepSeek AI
- **模型名称/系列**：生产级 = **V4-Flash-0731 / V4-Pro-0813 / V4-Flash-Vision-Exp**（08-31 开源 MIT）；V5-Preview **为传闻**
- **发布日期**：V4 报告 2026-04-26（arXiv 2606.19348）；V4-Flash-Vision-Exp 08-30 发布
- **核心参数**（V4 线，不变）：V4-Pro 1.6T/49B active；V4-Flash 284B/13B active；1M 上下文；33T/32T tokens；CSA + HCA 混合注意力、mHC、Muon、FP4 routed experts
- **主要创新点**（不变）：1M 上下文仅需 V3.2 的 27% FLOPs / 10% KV cache；V4-Pro-Max 推理模式定义开源推理 SOTA
- **本窗口增量**：⚠️ **V5-Preview 澄清**——截至 09-09 **无任何官方宣布**（无 model card / 权重 / API 入口），第三方面向文章（orcarouter.ai 等）将其标为 rumor/预期项，**不应计入已发布模型**。若 V5 真线存在，参考 Grok 4.7（09-12）与 Fable 5.2（9 月中下旬）为 9 月传闻窗口的一部分。
- **链接**：[arXiv:2606.19348](https://arxiv.org/abs/2606.19348) | [HF](https://huggingface.co/collections/deepseek-ai/deepseek-v4) | V5 rumor 注记：[orcarouter V5 leak 分析](https://www.orcarouter.ai/blog/deepseek-v5-preview-leak)

---

## 3. Meta AI — LLaMA 4（无新报告，基线不变）

- **中文标题**：LLaMA 4：原生多模态 AI（架构基线）
- **英文标题**：LLaMA 4: Multimodal Intelligence
- **发布机构**：Meta AI
- **模型名称/系列**：LLaMA 4 Scout（109B total / 17B active / 16 experts）；Maverick（400B / 17B / 128 experts）；Behemoth（~2T / 288B active，教师模型·仍在训练）
- **发布日期**：2025-04-05（model card）；Muse Spark 1.3 09-02（前基准，产品级）
- **核心参数**：Scout **10M 上下文**（iRoPE，交错 attention 无位置编码），~40T tokens；Maverick 1M 上下文，~22T tokens；原生多模态，early fusion
- **主要创新点**（不变）：首个开源原生多模态 MoE；Behemoth → Maverick 联合蒸馏（novel distillation loss）
- **本窗口增量**：无新 tech report / system card。LLaMA 4 "mid-cycle checkpoint"（07 月）与 Muse 线（Spark 1.3 / Glimmer 30B）维持前基准。
- **链接**：[Model Card](https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md) | [Meta AI Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)

---

## 4. Google DeepMind — Gemini 3.8 Flash（无新报告，前基准）

- **中文标题**：Gemini 3.8 Flash 模型卡 / Gemini 3.1 Pro 模型卡
- **英文标题**：Gemini 3.8 Flash Model Card / Gemini 3.1 Pro Model Card
- **发布机构**：Google DeepMind
- **模型名称/系列**：Gemini 3.8 Flash / 3.8 Flash Cyber；3.1 Pro；Omni Flash
- **发布日期**：3.8 Flash model card **2026-09-02/03**；3.1 Pro 2026-02
- **核心参数**：Sparse MoE Transformer；原生多模态；1M+ 上下文；3.8 Flash 与 3.7 同价 $0.75/$3.75；所有模型低于 Critical Capability Levels（CCL）
- **主要创新点**（不变）：基于 3.7 持续训练（"works harder"，烧更多 thinking tokens）；**软件工程 + agentic knowledge workflows** 提升；customizable effort levels；3.8 Flash Cyber 仅经 **Fairwind Program** 对受信防御者放行（CWE-Bench 47.2% pass@1）
- **本窗口增量**：无。模型卡 09-02/03 已在前基准记录。
- **链接**：[Model Card](https://deepmind.google/models/model-cards/gemini-3-8-flash/) | [3.1 Pro](https://deepmind.google/models/model-cards/gemini-3-1-pro/)

---

## 5. Anthropic — Claude Fable 5.1 / Mythos 5.1（无新报告，前基准）

- **中文标题**：Claude Fable 5.1 & Mythos 5.1 系统卡
- **英文标题**：Claude Fable 5.1 & Claude Mythos 5.1 System Card
- **发布机构**：Anthropic
- **模型名称/系列**：Claude Fable 5.1（通用 + 安全分类器）/ Claude Mythos 5.1（高权限，受信伙伴）；另有 Opus 5（07-24）
- **发布日期**：**2026-09-01**（System Card；AA 指数 66 = SOTA）
- **核心参数**：同一底层权重、两种安全配置；1M 上下文 / 128K 输出 / cutoff 2026-06；Fable 阻断生物/网络高敏双用途，Mythos 经 **Life Sciences / Cyber Verification Program** 受信访问
- **主要创新点**（不变）：always-on adaptive thinking + Effort 五档；ProofBench v1.1 100%、SWE-bench Verified 95.0%、Coding/knowledge work/novel math-science reasoning 领先；Cache Read -75%（$0.25/M）；reward hacking 自曝（>10% 训练环境）→ 150 工程师转安全
- **本窗口增量**：无新 card。**Fable 5.2 传闻持续**（PolyMarket 有盘口，官方零确认，按 6–8 周旗舰节奏推断 9 月中下旬——推断非事实）。
- **链接**：[System Card PDF](https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205.1%20&%20Claude%20Mythos%205.1%20System%20Card.pdf) | [System Cards Hub](https://www.anthropic.com/system-cards)

---

## 6. Mistral AI — Ministral 3（🆕 技术报告复盘）

- **中文标题**：Ministral 3：3B/8B/14B 系列的级联蒸馏训练
- **英文标题**：Ministral 3: Technical Report（arXiv 2601.08584）
- **发布机构**：Mistral AI
- **模型名称/系列**：Ministral 3（三个尺寸 3B/8B/14B × 三种变体 base/instruct/reasoning = 9 个模型）
- **发布日期**：2026-01-13（tech report 日期；本窗口复盘录入）
- **核心参数**：
  - **Dense 架构**（非 MoE）：3B / 8B / 14B，各配 base / instruct / reasoning 变体
  - **训练 token 仅 1–3T**（对比：Qwen3 36T、Llama 3 15T——**数据效率是卖点**）
  - 上下文 ≤**256K**（reasoning 变体 128K）
  - 支持图像理解；Apache 2.0 开放权重
- **主要创新点**：
  - **Cascade Distillation（级联蒸馏）**：迭代剪枝（pruning）+ 从大到小的持续蒸馏，教师为 **Mistral Small 3.1（24B 父模型）**
  - 以 1/12 ~ 1/36 的训练数据量对齐更大开源模型，验证"剪辑再蒸馏"训练路线
  - 9 款变体矩阵覆盖性价比推理/通用/多模态三档场景
- **本窗口增量**：技术报告（01-13）为非窗口期事件，此前 09-08 摘要已列入；本窗口复核其关键点——**Cascade Distillation + 1–3T token 是区别于 Qwen3/Llama3 大规模预训练的风格化证据**，值得与 [[intern-lm3]] 式"思维密度"叙事对照。
- **链接**：[arXiv:2601.08584](https://arxiv.org/pdf/2601.08584) | [Mistral Docs](https://docs.mistral.ai/models/minstral-3) | 系列基线：Mistral Large 3（675B-A41B Mamba-MoE，arXiv 2506.10910 Magistral）

---

## 7. Qwen（阿里巴巴）— Qwen3.8 家族（无新报告）

- **中文标题**：Qwen3.8 家族基线 / Qwen3.5 技术报告
- **英文标题**：Qwen3.5 Technical Report / Qwen3.8 family
- **发布机构**：Qwen Team（Alibaba Cloud，通义千问）
- **模型名称/系列**：Qwen3.8-Max 2.4T-A95B（08-03）；Qwen3.8-Flash-Next（08-26，Qwen4 架构 preview，125B/~6B active + 51B 系统 RAM 组件）；Qwen3.5-397B-A17B（DeltaNet 混合线性注意力）；qwen-long **10M ctx**
- **发布日期**：2026-02~08（持续）
- **核心参数**：Sparse MoE + hybrid attention（Gated DeltaNet）；262K→1M 上下文扩展；Apache 2.0（Qwen3.5）/ 今夏 4 版 4 license 无 Apache
- **主要创新点**（不变）：Thinking mode 动态分配；Flash-Next 异构内存（GPU + 系统 RAM）轨道
- **本窗口增量**：无新报告。09-02 wavect.io 开源模型横评（Qwen vs Kimi vs GLM）可作为市场叙事参考——Kimi K2 主打 agentic coding specialist、Qwen3.8-Max 综合、GLM-5.3 权重开源。
- **链接**：[Wavect 横评 09-02](https://wavect.io/blog/open-weight-llm-comparison-2026/) | [Qwen Blog](https://qwen.ai/blog) | [Qwen3 arXiv:2505.09388](https://arxiv.org/abs/2505.09388)

---

## 8. Moonshot AI — Kimi K3 / 9. Zhipu AI — GLM-5.3（无新报告，基线不变）

**Moonshot AI（月之暗面）— Kimi K3**
- **中文标题**：Kimi K3：开源前沿智能
- **英文标题**：Kimi K3: Open Frontier Intelligence
- **发布机构**：Moonshot AI
- **模型名称/系列**：Kimi K3（Kimi-K3 Dev 开发版）
- **发布日期**：2026-07-27（arXiv 2607.24653）
- **核心参数**：2.8T total / 104B active；896 routed experts（top-16）+ 2 shared；93 层（69 KDA + 24 Gated MLA + 1 dense）；MoonViT-V2 401M 视觉编码；1,048,576（1M）上下文；MXFP4/MXFP8 量化
- **主要创新点**（不变）：世界首个开源 3T 级模型；**KDA（Kimi Delta Attention）** 固定态 recurrent state 替代 growing KV cache；**Stable LatentMoE**（Quantile Balancing）；约 2.5× K2 缩放效率；BrowseComp 91.2%
- **链接**：[arXiv:2607.24653](https://arxiv.org/abs/2607.24653) | [HF](https://huggingface.co/moonshotai/Kimi-K3)

**Zhipu AI（智谱）— GLM-5.3**
- **中文标题**：GLM-5：从 Vibe Coding 到 Agentic Engineering（+ 5.3 权重开源）
- **英文标题**：GLM-5: from Vibe Coding to Agentic Engineering
- **发布机构**：智谱 AI & 清华大学
- **模型名称/系列**：GLM-5（744B-A40B，arXiv 2602.15763）；**GLM-5.3 权重 08-28 开源**（FP8+BF16，License 营收阈值 **$10B USD**）；GLM-5.3-Flash = Ox Alpha（320B-A18B，MIT，1M ctx，10 万国产芯片）
- **发布日期**：主报告 2026-02-17；5.3 权重 2026-08-28
- **核心参数**：744B/40B active MoE + **DSA 动态稀疏注意力**（KV cache -75% / 推理 +3×）；28.5T tokens；SWE-bench Verified 77.8%（开源 SOTA）
- **本窗口增量**：无新报告；08-28 权重开源在前基准已化解（[[../2026-09-01/tech-report-digest]]）。
- **链接**：[arXiv:2602.15763](https://arxiv.org/abs/2602.15763) | [GitHub](https://github.com/zai-org/GLM-5)

---

## 10. Microsoft — MAI-Thinking-1 / 11. Apple — AFM（无新报告，基线不变）

**Microsoft**
- **中文标题**：MAI-Thinking-1 技术报告 / Phi-4-reasoning-vision-15B
- **英文标题**：MAI-Thinking-1 Technical Report / Phi-4-reasoning-vision-15B Technical Report
- **发布机构**：Microsoft Research / MAI
- **模型名称/系列**：MAI-Thinking-1（首个从零训练的 reasoning 模型，零第三方蒸馏）；Phi-4-reasoning-vision-15B（仅 200B multimodal tokens）
- **发布日期**：2026-06-06（MAI 报告）；2026-03（Phi-vision，arXiv 2603.03975）
- **本窗口增量**：无。Phi-5 仍无官方 tech report。

**Apple（09-09 产品发布会 = non-model）**
- **中文标题**：Apple Intelligence 基础语言模型技术报告 2025
- **英文标题**：Apple Intelligence Foundation Language Models Tech Report 2025
- **发布机构**：Apple
- **模型名称/系列**：On-Device（~3B）+ Server（**PT-MoE**，Private Cloud Compute）；第三代 AFM（Gen-3，5 模型家族，与 Google TPU 合作）**tech report 承诺 "later this summer" 已逾期**
- **发布日期**：2025-07-17（arXiv 2507.13575）；AFM Gen-3 2026-06-08 宣布、报告违约金仍 pending
- **本窗口增量**：**09-09 = Apple 年度秋季发布会（iPhone 18 / iOS 27 / Siri AI 正式路径）**——产品侧事件，非模型 tech report；AFM 2026 技术报告继续标注为"承诺中"。

---

## 12. NVIDIA — Nemotron 3 系列（无新报告；non-model 事件先行）

- **中文标题**：Nemotron 3 Ultra：高效 MoE 混合 Mamba-Transformer 推理模型
- **英文标题**：Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning
- **发布机构**：NVIDIA
- **模型名称/系列**：Nemotron 3 Ultra（550B-A55B）/ Super（120B-A12B）/ Nano（30B-A3B）
- **发布日期**：2026-06-09（Ultra 报告）；2025-12（Nano）
- **核心参数**（不变）：Hybrid Mamba-Attention MoE + LatentMoE + MTP + MOPD + NVFP4；20T tokens；1M 上下文；推理吞吐比 GLM-5.1 高 5.9×
- **本窗口增量**：模型侧无新增；**09-04 确认 $12.9B 收购 Hugging Face**（non-model，H100/H200 非必需）+ RTX Spark N1X 定档 10 月（前基准已录）。Nemotron 3 系白皮书停在 2025-12（arXiv 2512.20856）。

---

## 13. xAI — Grok 4.7（📅 未发布 · 预期 09-12 · 无官方文档）

- **中文标题**：Grok 4.7：2.1T 新预训练 + SpaceX 工程语料（未发布）
- **英文标题**：Grok 4.7 (unreleased, expected 2026-09-12)
- **发布机构**：xAI
- **模型名称/系列**：Grok 4.7（接续 Grok 4.6 / 4.5 / 4.20 线）
- **发布日期**：Musk 09-02 "10 天"倒计时 → **预期 09-12**（无官方 spec sheet / model ID / pricing / context / benchmark card）
- **核心参数**：**~2.1T 参数**（vs Grok 4.6 的 1.5T，**+40%**）；预训练 08-12 已完成；**补充训练语料 = SpaceX 工程数据**（火箭研制日志/测试记录、**Starlink 卫星遥测**、内部工程文档）
- **主要创新点**（founder claim，tentative）：Musk 称其为"最 architecturally novel 的前沿发布"（2026 年）且 token 效率更好；SpaceX 语料若提升推理能力 = xAI 难复制的专属数据卡；若不能 = 昂贵内部实验（见 09-06 基准理性分析）
- **本窗口增量**：倒计时 3 天（09-09 → 09-12）；仍无 docs.x.ai release note / 模型 ID。**09-12 是本季下一个确定发布窗口**。
- **链接**：[bighatgroup 09-06 周报](https://www.bighatgroup.com/blog/xai-weekly-2026-09-06/)（二手综合，官方零确认）

---

## 14. Amazon — Nova 家族（无新报告，基线不变）

- **中文标题**：Amazon Nova 基础模型技术报告
- **英文标题**：Amazon Nova Foundation Models Technical Report
- **发布机构**：Amazon（AWS）
- **模型名称/系列**：Nova Pro（多模态 frontier）/ Lite（低成本多模态）/ Micro（纯文本轻量）/ Canvas（文生图）/ Reel（文生视频）；Nova 2.x 线（前基准）
- **发布日期**：2024-12-03（报告）；Premier addendum 2025-04-30；arXiv 2506.12103
- **核心参数**：统一多模态理解+生成；企业安全与成本分层；Nova 2 线多重模态动态推理（1M ctx 等，见 08-29/08-31 基准）
- **本窗口增量**：无新报告。Nova 2 系列的 FMSF（arXiv 2601.19134）等在 08 月基准已录。

---

## 15. ByteDance Seed — Seed 2.0 Agent 系列（🆕 本窗口新增）

- **中文标题**：Seed 2.0 Agent 系列发布（三个 Agent 模型 + Code 模型）
- **英文标题**：Seed 2.0 Agent Series Launch
- **发布机构**：ByteDance Seed（火山引擎 / 豆包）
- **模型名称/系列**：**Seed 2.0 Agent 系列 = Agent 2.0 Pro / Agent 2.0 Lite / Agent 2.0 Mini + Seed 2.0 Code**；先行款 Seed2.1（2026-06-23）
- **发布日期**：09-03 新闻稿发布系列（2026-09-03）；Seed2.0 家族 2026-02-14
- **核心参数**：三档 Agent 模型（Pro/Lite/Mini）按场景分级；Code 模型聚焦编码/工具链；已部署 **豆包 App / TRAE**（Pro 与 Code）；**全系 API 通过火山引擎**开放
- **主要创新点**：
  - Seed 2.0 主打 **agentic coding / long-horizon agent 任务**（评估系统基于真实用户需求构造）
  - 生态配套：Seedance 2.0 视频生成（arXiv 2604.14148）、Seedream 图像、SeedRealtime（08-05 全双工音视频）
  - 火山引擎为唯一对外 API 通道，与 DeepSeek/GLM 开放权重路线不同（**闭源 + MaaS 分发**）
- **本窗口增量**：Agent 系列产品化发布（09-03），此前 Seed 2.0 报告（arXiv 2607.00248）/ Seed2.1（06-23）已在 08 月基准。
- **链接**：[Seed Blog: Seed2.1](https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity) | [Seed2.0 Card arXiv:2607.00248](https://arxiv.org/abs/2607.00248)

---

## 16–19. InternLM / StepFun / Baichuan / 01.AI（无新报告，基线不变）

- **InternLM（上海 AI 实验室）**：Intern-S2-Preview **35B-A3B**（科学多模态，逼近 1T S1-Pro）；S1-Pro 1T 科学（arXiv 2603.25040，AIME-2025 93.1 / SmolInstruct 74.8）；S2-Mobius（arXiv 2608.14290，知识-推理解耦 ~4× 加速）。——08 月基准已录。
- **StepFun（阶跃星辰）**：Step 3.7-Flash（05-发布产品线）/ Step3-VL-10B（PaCoRe 并行视觉推理，MMMU 80.11% / AIME2025 94.43%，arXiv 2601.09668）/ Step-DeepResearch（32B 单次 <0.5 RMB，ResearchRubrics 61.42）。——前基准已录。
- **Baichuan（百川智能）**：M4 临床级医疗 Agent（Baichuan-Harness、SPAR++、幻觉率 3.3%，arXiv 2606.08982）；M3-235B（HealthBench-Hard 44.4%，arXiv 2602.06570）。
- **01.AI（Yi）**：Yi: Open Foundation Models（arXiv 2403.04652，6B/34B，3.1T tokens，200K ctx）；Yi-Lightning（arXiv 2412.01253）。2026 无新旗舰，转向企业/主权 AI。

---

## 其余增量 & 时间表（09-09 → 09-20）

| 日期 | 事项 |
|------|------|
| **09-09** | **OpenAI GPT-6 Astra 全面铺开启动**（limited orgs → coming days 全量 + API/Azure/Bedrock） |
| 09-09 | Apple 秋季发布会（iPhone 18 / iOS 27 / Siri AI 路径，non-model） |
| **09-12（预期）** | **xAI Grok 4.7**（2.1T 新预训练 + SpaceX 数据；倒计时 3 天） |
| 09-14 | Claude Code weekly-limit 调整落地 |
| 9 月中下旬（传闻） | Anthropic **Fable 5.2**（PolyMarket 盘口，官方零确认） |
| 10 月 | NVIDIA RTX Spark N1X 发布 |
| 09 月内 | Anthropic **Enterprise Frontier Safeguards（EFS）** 上线 |
| 12-31 | Google Gemini 3.8 Flash 引入价到期 |

---

## 本窗口趋势观察

1. **"限游客 → 全量"成为 frontier 发布标配第二幕**：GPT-6 Astra 历经 09-03 gated 预览 → 09-04 ChatGPT 订阅 → 09-09 API/Azure/Bedrock 全量三阶段铺开；发布即受限（cyber 削版 + Enterprise 默认关闭）——能力管线与范围控制解耦的部署范式进一步固化。
2. **9 月发布传闻窗口集中**：Grok 4.7（09-12，有具体时间线但零官方文档）→ Fable 5.2（9 月中下旬，零确认）→ DeepSeek V5（纯 rumor）——**三类传闻置信度分层**（日期已定 / 市场定价 / 完全无源）值得在后续 digest 中持续校验，避免把 rumor 计入已发布模型。
3. **数据效率叙事强化**：Mistral Ministral 3 以 1–3T token 训练对齐更大模型（Cascade Distillation），呼应 InternLM"思维密度/IQPT"路线——vs 大规模预训练（Qwen3 36T/Llama3 15T）的路线分化更加清晰。
4. **中国厂商分发分化**：ByteDance Seed 走**闭源 MaaS**（豆包/TRAE + 火山引擎），DeepSeek/Qwen 走**开放权重**，GLM 走**门槛开源**（$10B）——三种商业化策略并行。
5. **Apple 09-09 发布会是产品侧而非模型侧**：AFM 2026 tech report 继续逾期，"later this summer" 承诺已实质落空两季。

---

## 信源注记

本窗口断言基于：OpenAI 官方 blog/API docs（gpt-6-astra，09-09 更新）、deploymentsafety.openai.com/gpt-6-astra（System Card 09-03）、ByteDance Seed Blog（Seed2.1/Seed 2.0）、arXiv 2601.08584（Ministral 3）、arXiv 2606.19348（DeepSeek-V4）、deepmind.google model cards（Gemini 3.8 Flash）、anthropic.com（Fable/Mythos 5.1 System Card）、meta-llama llama4 MODEL_CARD、amazon.science Nova report、orcarouter.ai（DeepSeek V5 rumor）、bighatgroup.com（Grok 4.7 周报）、wavect.io（开源横评 09-02）。其余机构规格沿 09-08/09-07 基准，未重复检索。

> 本报告由 opencode 自动搜索编译，数据截至 2026-09-09。部分信息来自公开技术报告、模型卡、官方 blog 与第三方聚合，具体细节请参阅原始链接。传闻类条目已显式标注置信度。