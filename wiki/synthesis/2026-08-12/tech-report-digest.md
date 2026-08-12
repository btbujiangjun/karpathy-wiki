---
title: "大模型技术报告摘要（2025-2026）| LLM Tech Report Digest (2025-2026)"
type: synthesis
created: 2026-08-12
updated: 2026-08-12
sources: [tech-report-digest-2026-08-11.md]
tags: [tech-report, system-card, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, bytedance, zhipu, kimi, internlm, baichuan, stepfun, minimax]
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告 / System Card 汇总。
> 更新日期：2026-08-12（每日更新；今日重点：**Meta "Llama 4 405B 开放权重 08-12" 验收失败——当日无发布，实际发生的是 08-10 开放权重战略转向：开源 30B Muse Glimmer（Apache 2.0、128K ctx、本地运行、由 Muse Spark 蒸馏）+ 承诺数周内开源 Muse Spark 1.2 权重，Zuckerberg 6000 字文章《The Future Is for Everyone》；llama.com 目录仍仅 Llama 4 Scout/Maverick**；**Qwen3.8-Max 权重验收日（08-12）截至撰写时仍未兑现**——ModelScope 页面指向今日，但 HF Qwen org 实时检查无 Qwen3.8-Max/27B 权重条目，license 未发布；**OpenAI 下一个大模型官方定名 Astra（08-01 官方博客）**——解决 10 道数学/理论计算机难题，"next major model"，GPT-5.7 传闻搁置；**NVIDIA Nemotron 3.5 Lightning（08-11）**——30B-A3B 开放 MoE，面向 always-on agents；**MiniMax M2.7 自我进化（08-08 新闻）**——MLE Bench Lite 66.6% 得牌率；**DeepSeek 涨价公告（08-06）**——V4-Pro GA 仍未发布，窗口第 3 天；**字节跳动 >5T/10T 参数新模型训练传闻（08-06/07）**——张一鸣公开反蒸馏、强调自有差异化；**Baichuan-M2（08-11）开源医疗增强模型**；**Anthropic Fable 5.1 事实核查（08-03）确认无官方公告**；**Google DeepMind 08-05 领导层改组**；智谱口径转向 **GLM-5.3**（GLM-5.5 传闻未确认））

---

## 1. DeepSeek（深度求索）

### 1.1 DeepSeek API 整体涨价公告（今日新增核实，08-06）

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek API 定价大幅上调公告 |
| **英文标题** | DeepSeek API price increase announcement |
| **发布机构** | DeepSeek-AI |
| **发布日期** | 2026-08-06 |
| **核心创新** | 官方公告"计划近期整体上调 API 定价、涨幅较大"；当前峰谷计费（工作日 9:00–12:00、14:00–18:00 高峰 = 平时 2 倍）；平时价：V4-Flash 输入（缓存未命中）1 元/百万 token、输出 2 元；V4-Pro 输入 3 元、输出 6 元 |
| **论文** | https://api-docs.deepseek.com/quick_start/pricing |

> 业内解读：涨价通常伴随正式版上线（计算资源承接信号）；配合官方 API 文档仍写"V4-Pro 正式版将尽快发布"，市场预期 GA 临近。口径待官方正式通知。

### 1.2 DeepSeek-V4-Flash 官方 API 公开 beta（继承 08-11，保留）

| 项目 | 内容 |
|------|------|
| **模型系列** | V4-Flash（284B 总参 / 13B 激活 MoE + CSA） |
| **发布日期** | 2026-07-31 |
| **核心创新** | Agent 能力突出——Terminal Bench 2.1: **82.7**、NL2Repo: **54.2**、Cybergym: **76.7**、DeepSWE: **54.4**、Toolathlon verified: **70.3**、Agent Last Exam: **25.2**、Automation Bench: **25.1**、DSBench-FullStack: **68.7**、DSBench-Hard: **59.6** |
| **论文** | https://releasebot.io/updates/deepseek |

### 1.3 DeepSeek-V4-Pro 官方版发布窗口（今日第 3 天，仍未发布）

| 项目 | 内容 |
|------|------|
| **模型系列** | V4-Pro（1.6T 总参 / 49B 激活 MoE + CSA） |
| **发布日期** | V4-Pro-Preview：2026-04-24；官方版传闻窗口 **2026-08-10~08-20**（未确认） |
| **核心创新** | 今日 08-12 为窗口第 3 天，官方仍无 GA 公告；08-06 涨价公告 + API 文档 "V4-Pro 正式版将尽快发布" 为最近官方表态；Preview 已预览近 4 个月 |
| **论文** | V4 技术报告 arXiv:2606.19348 |

> 今日核实：窗口（08-10~08-20）第 3 天仍无官方公告；"涨价先行、GA 随后"为中文科技媒体主流预期，未确认，不升级为正式发布条目。

---

## 2. OpenAI

### 2.1 Astra 官方定名（今日新增核实，08-01 官方博客）

| 项目 | 内容 |
|------|------|
| **中文标题** | OpenAI 下一个大模型定名 Astra |
| **英文标题** | OpenAI's next major model: Astra |
| **发布机构** | OpenAI |
| **模型系列** | Astra（"next major model"，新家族，为 long-running workloads 设计） |
| **发布日期** | 定名公告 2026-08-01（官方博客） |
| **核心创新** | 内部版本已解决 **10 道数学/理论计算机难题**（非软 sofic、Connes rigidity 反例、高维 sphere packing 界、Erdős 问题等）；The Information 确认为新模型家族、面向长时间运行任务设计；**GPT-5.7 传闻被搁置** |
| **论文** | OpenAI 官方博客（08-01 定名公告） |

> 今日核实：Astra = 官方命名（08-01 博客），非仅代号；是否以"GPT-6"命名官方未确认；OpenAI 当前最新正式发布仍为 GPT-5.6（System Card 07-09）。

### 2.2 GPT-5.6 部署更新（继承 08-11，保留）

- **GPT-5.6 Sol/Luna 部署**（08-06）：Sol 成 Plus/Pro 默认、Luna 覆盖 Free/Go、新增 Think 按钮显式控制推理预算；07-30 已降价（Luna -80%、Terra -20%）。https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/

> 今日核实：无 8 月新技术报告；GPT-5.6 System Card（07-09）仍为最新。

---

## 3. Meta

### 3.1 Llama 4 开放权重 08-12 验收失败（今日最大纠偏）

> ⚠️ **验收结论（08-12）：昨日（08-11）报告的 "Meta Llama 4 405B 开放权重今日 08-12 发布" 未兑现**——截至撰写时无 405B 开放权重、无 Meta 官方技术报告。实际重大事件为 **08-10 开放权重战略转向**：

| 项目 | 内容 |
|------|------|
| **中文标题** | Meta 开放权重战略转向：Muse Glimmer 开源 + Muse Spark 1.2 权重承诺 |
| **英文标题** | Meta open-weight shift: Muse Glimmer open-source + Muse Spark 1.2 weights promised |
| **发布机构** | Meta AI |
| **发布日期** | 2026-08-10 |
| **核心创新** | **开源 30B Muse Glimmer**（Apache 2.0、128K ctx、本地运行、由 Muse Spark 蒸馏）；**承诺数周内开源 Muse Spark 1.2 权重**（Muse Spark 4 月首发为闭源）；Zuckerberg 6000 字文章《The Future Is for Everyone》（Ars Technica 08-10） |
| **论文** | Ars Technica 2026-08-10；llama.com 目录仍为 Llama 4 Scout/Maverick（2025-04 时代，17B 激活、10M ctx、MoE + early-fusion 多模态） |

> 昨日 08-11 页的 405B/15T tokens/11-14 基准超 GPT-5 等细节源自 Bloomberg/NeuralStack 预告口径，**以今日实际发生为准，不保留为正式发布条目**。405B 与 Behemoth "近 2T" 的早期口径矛盾随本次未发布而不再适用。

### 3.2 Muse 系列（继承 08-11，保留 + 更新）

- **Muse Spark Safety & Preparedness Report**（2026-07 PDF）：arXiv:2606.12429。
- **Muse Code**（2026-08-05）：AI 编程智能体，$0.20/百万输出 token 低价策略。
- **Muse Spark 1.2**（2026-08-05）：Terminal-Bench 82.9%；**权重承诺数周内开源（08-10 战略转向）**。

---

## 4. Google DeepMind

### 4.1 领导层改组（今日新增核实，08-05）

| 项目 | 内容 |
|------|------|
| **中文标题** | Google DeepMind 领导层改组 |
| **英文标题** | Google DeepMind leadership reshuffle |
| **发布机构** | Google DeepMind |
| **发布日期** | 2026-08-05（Reuters） |
| **核心创新** | **Hassabis 转任主席**（兼 Alphabet 首席科学家）；**Kavukcuoglu 升 SVP**（接任实质 CEO 职责）；**Jeff Dean 离职另有任用**（此前 08-06 已报道其创办 Discovery Loop） |
| **论文** | Reuters 2026-08-05 |

> 与 08-06 investment-daily 口径一致（Hassabis 卸任 CEO → 转任董事长兼 Alphabet 首席科学家；Jeff Dean 创办 Discovery Loop；Koray 接任）。

### 4.2 Gemini 系列状态（继承 08-11，保留）

- **Gemini 3.1 Pro Model Card**（2026-02）为当前官方最新 Pro 级 Model Card。
- **Gemini 4 预训练中**（07-21）："most ambitious pretraining run yet"；Gemini 3.5 Pro 仍延迟；业内预期 Gemini 4 于 11-12 月（今日新增核实口径：Pichai 称"最雄心勃勃预训练"）。
- **Gemini 3.6 Flash**（07-21）：原生多模态推理。
- **Gemini Robotics 2 / ER 2 / On-Device 2**（07-30）。

> 今日核实：8 月无新模型卡（releasebot 08-08 仅 Classroom 集成类更新）。

---

## 5. Anthropic

### 5.1 Fable 5.1 事实核查（今日新增核实，08-03）

> ✅ 核查结论：**Fable 5.1 无任何官方公告**（AIToolsReview 08-03 事实核查）——仅两条 X 泄漏（Pankaj Kumar 07-26 + Lumina）；$10/$50 定价为传闻（与 Fable/Mythos 5 相同档位）；**Opus 5 已部分超越原 Fable 5**。继续不写入正式条目。

### 5.2 Claude Mythos Preview System Card（继承 08-11，保留）

| 项目 | 内容 |
|------|------|
| **发布日期** | System Card PDF: 2026-04-07 |
| **核心创新** | 当前最先进闭源前沿；首个按 RSP v3 发布决策审查的系统卡 |
| **论文** | PDF: https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf |

### 5.3 Claude Opus 5 System Card（继承 08-11，保留）

- **Opus 5 System Card**（07-24）：SWE-bench Verified 96.0、SWE-bench Pro 79.2、Frontier-Bench v0.1 43.3、ARC-AGI-3 30.2；effort dial $5/$25 每 M in/out。

---

## 6. Mistral

### 6.1 状态（继承 08-11，保留 + 更新）

- **Mistral 3 系列**为当前自有模型（最新 Mistral Large 3：2025-12，675B）；重心转向"模型经纪人"（model broker）定位。
- **今日新增核实**（08-02 新闻）：将推出 **Code / Apps sections**（Vibe / Le Chat）；**夏季将发布新的"大而稀疏"MoE 开放权重模型**——未发布，观察项。

> 今日核实：无 8 月新技术报告。

---

## 7. Qwen（通义千问）

### 7.1 Qwen3.8-Max 开源权重验收日（今日 08-12，截至撰写时未兑现）

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.8-Max 开源权重（验收日 08-12） |
| **英文标题** | Qwen3.8-Max open weights (acceptance day Aug 12) |
| **发布机构** | Alibaba Qwen |
| **模型系列** | Qwen3.8-Max（2.4T 总参 Sparse MoE / 95B 激活 / 1M ctx / 原生视觉多模态）；Qwen3.8-27B（同日，27B dense） |
| **发布日期** | API GA：2026-08-03；**权重：ModelScope 发布页指向 2026-08-12（今日）** |
| **核心创新** | 首个开源权重的 Max 级模型；**$2 in / $6 out 每 M tokens** |
| **论文** | https://qwen.ai/blog?id=qwen3.8 |

> **今日实时检查（HF Qwen org，2026-08-12）：仍无 Qwen3.8-Max / Qwen3.8-27B 权重条目**（最新模型为 Qwen3-ASR，约 07-22）。license 未发布——byteiota（08-07）提示草案 license 曾含 US/EU/UK/Korea 地域限制争议。对照 Moonshot Kimi K3 按期放权（07-27 兑现），"承诺→兑现"信用质疑延续。

### 7.2 其他 Qwen 条目（继承 08-11，保留）

- **Qwen3.8-27B**（08-03，同日发布，权重同验收日）。
- **Qwen3.7-Flash**（07-25）；**Qwen-Audio-3.0-ASR-Flash**（07-30）；**Qwen-UI-Agent TR**（07，arXiv:2607.28227）。

---

## 8. Microsoft（Phi）

### 8.1 Phi-5 状态（继承 08-11，保留）

> 截至 08-12 **仍无 Phi-5 官方技术报告**；MSR 最新技术报告仍为 Phi-4-reasoning-vision-15B（2026-03）。16B/MMLU 86.7% 报道仍为 single-source（GogoAI），未确认。

---

## 9. Apple

### 9.1 AFM 3（继承 08-11，保留）

| 项目 | 内容 |
|------|------|
| **模型系列** | AFM 3 Core（3B 端侧 dense）/ Core Advanced（20B 端侧稀疏，IFP 激活 1–4B）/ AFM 3 Cloud（PCC）/ ADM 3 Cloud（图像）/ AFM 3 Cloud Pro（PCC on Google Cloud NVIDIA GPU） |
| **发布日期** | 技术报告 2026-06-08（WWDC26）；正式发布承诺 "later this summer" 仍未兑现 |
| **核心创新** | IFP（Instruction-Following Pruning）端侧稀疏路由；与 Google/NVIDIA 合作；Cloud Pro 可在 Google Cloud NVIDIA GPU 运行 |
| **论文** | https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models |

> 今日核实：08-12 仍在"summer"窗口内，正式发布承诺尚未兑现；Siri AI 已进入 iOS 27 消费者测试版。

---

## 10. NVIDIA

### 10.1 Nemotron 3.5 Lightning（今日新增核实，08-11）

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron 3.5 Lightning |
| **英文标题** | Nemotron 3.5 Lightning |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3.5 Lightning（**30B-A3B** 开放 MoE） |
| **发布日期** | 2026-08-11 |
| **核心创新** | 面向 **always-on agents** 设计；开放权重 MoE；延续 Nemotron 3 家族 1M ctx + 开放权重 + 技术报告卖点 |
| **论文** | https://developer.nvidia.com/topics/ai/nemotron |

### 10.2 Nemotron 3 家族（继承 08-11，保留）

- **Ultra**（06-09）：550B/55B hybrid Mamba-Attention MoE + LatentMoE + MTP + NVFP4；1M ctx。
- **Super**（04-03）：120B/12B；25T tokens。
- **Nano**（08-04）：30B-A3B；吞吐最高 3.3×。

> 今日核实：官方 Nemotron 3 家族总报告仍待发布；Lightning（08-11）为家族最新成员。

---

## 11. xAI

### 11.1 Grok 4.6（继承 08-11，状态不变：已上线但官方 model card 缺席）

| 项目 | 内容 |
|------|------|
| **模型系列** | Grok 4.6（**1.5T 参数**、基于 Grok 4.5 V9 基座） |
| **发布日期** | 约 **2026-08-07 上线**（第三方 kie.ai）；Musk 08-04 财报电话会口径 |
| **核心创新** | 大幅升级 SFT + RL 后训练；**仍无官方 model card / 基准 / 上下文 / 定价** |
| **论文** | https://x.ai/news/grok-4-5（官方最新博文仍为 4.5） |

> 今日核实：截至 08-12，**xAI 官方 docs.x.ai 目录仍仅列 grok-4.5**（$2/$6、500K ctx、知识截止 2026-02-01），API release notes 无 4.6 条目——"上线 vs 官方目录"矛盾持续。Grok 4.7（2.1T）计划 3-4 周后、Grok 5 年内。

---

## 12. Amazon

### 12.1 Nova 家族（继承 08-11，保留）

- **Nova 2 Sonic 2.1**（05-21~05-28 部署）：自回归 transformer 架构（无视觉编码器）。
- **Nova 原版技术报告**（2024）仍为唯一正式技术报告。
- **战略收缩**（07-28）：Nova Premier/Omni/Reel/Canvas 弃用；FMR 由 Pieter Abbeel 领导；新旗舰目标 re:Invent 2026 秋。

> 今日核实：无 8 月新报告；re:Invent 2026（11-30~12-04，Las Vegas，早鸟注册 08-25 截止）为下一观察点。

---

## 13. ByteDance（字节跳动）

### 13.1 >5T/10T 参数新模型训练传闻（今日新增核实，08-06/07）

| 项目 | 内容 |
|------|------|
| **中文标题** | 字节跳动超大规模模型训练传闻 |
| **英文标题** | ByteDance >5T/10T parameter model training (rumored) |
| **发布机构** | 字节跳动 Seed（传闻；晚点 LatePost 08-06 + 金融时报 08-07） |
| **模型系列** | 新模型（参数超 5T~10T，为国内已知最大规模） |
| **发布日期** | 预训练早期阶段（预计 3-6 个月预训练），未发布 |
| **核心创新** | 由 Seed Foundation 负责人**项亮**主导、预训练数据负责人**沈科**合作；张一鸣 Seed 全员会表态：**反对蒸馏**（"复制 Claude 已有能力，最多逼近难超越"）、编程是当前关键但非唯一热点、接受短期落后、追求智能上限；梁汝波承认豆包 AI Coding 不突出 |
| **论文** | 晚点 LatePost（08-06）；金融时报（08-07） |

> ⚠️ 传闻（未发布，不入正式发布条目）：规模数字两版本——晚点"超 5 万亿" vs FT"10 万亿（或超 Anthropic Mythos 5 约 8T 参数）"。为观察项。

### 13.2 Seed2.1（继承 08-11，保留）

- **Seed2.1 Pro + Turbo**：Agent/代码工程（agentic + coding E2E）；视频理解多评测 SOTA（含小时级长视频）；官方 Model Card PDF 随发布（seed.bytedance.com/zh/seed2_1）。

---

## 14. Zhipu（智谱）

### 14.1 GLM-5 技术报告（继承 08-11，保留）

- **GLM-5 TR**（02-22）：~745B/44B；DSA 稀疏注意力 + 异步 RL + 异步 Agent RL；完全适配华为等国产芯片。

### 14.2 GLM-5.3 口径（今日新增核实，08-12）

> **口径更新**：新浪财经（07-20）与 JPMorgan（8 月预测）口径更偏向新旗舰为 **GLM-5.3**（>1T 参数），而非此前传闻的 GLM-5.5（早期传闻，未确认）；唐杰此前回应"史诗级 plus"。**均未发布/未确认**，不入正式条目。GLM-5.2（06-13，MIT 权重，1M ctx）仍为当前确认旗舰。

---

## 15. Moonshot（月之暗面）

### 15.1 Kimi K3 / K4（继承 08-11，保留）

- **Kimi K3**（API 07-16；全量权重 + 47 页技术报告 07-27）：2.8T/104B 激活；93 层（69 KDA + 24 Gated MLA）；896 experts；AttnRes；MoonViT-V2；MXFP4/8；1M ctx；首个开源 3T 级模型；WebDev Arena #1。
- **MoonEP / FlashKDA**（07-29）：全链路开源配套。
- **Kimi K4 训练中**（The Information 07-28/29）：寻求更多 NVIDIA Blackwell 芯片，未发布。

> 今日核实：K3 技术报告（07-27）仍为最新，权重按期兑现。

---

## 16. InternLM（上海 AI 实验室）

### 16.1 Intern-S2-Preview（继承 08-11，保留）

- **Intern-S2-Preview**（35B 07-17 / 397B 07-18）：科学多模态基础模型；task scaling；397B MoE ~120B 激活；Apache-2.0；BF16 + FP8。WAIC 2026（07-01）发布"书生·端砚"科学发现平台 + Intern-S2-Preview-397B 以 397B 追平此前万亿模型。

> 今日核实：无 8 月新报告；InternLM4 官方状态不明（04-13 传闻，未确认）。

---

## 17. Baichuan（百川智能）

### 17.1 Baichuan-M2（今日新增核实，08-11）

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan-M2 开源医疗增强大模型 |
| **英文标题** | Baichuan-M2 open-source medical model |
| **发布机构** | 百川智能 |
| **模型系列** | Baichuan-M2（**32B**） |
| **发布日期** | 2026-08-11（36氪 newsflash） |
| **核心创新** | **开源医疗增强**；HealthBench **60.1**——以 32B 尺寸超过 OpenAI 最新开源模型 **gpt-oss-120B**；延续医疗垂直战略（M4 06-22 曾以 HealthBench 68.6 世界第一） |
| **论文** | 36氪 2026-08-11 |

### 17.2 Baichuan-M4 / M3（继承 08-11，保留）

- **Baichuan-M4**（05-26/06-22）：临床级医疗 Agent；HealthBench 68.6 世界第一；hallucination 3.3%。arXiv:2606.08982。
- **Baichuan-M3**（2026-01）：235B；HealthBench 65.1。

> 今日核实：战略全面转向医疗垂直领域；M2 为开源线最新。

---

## 18. StepFun（阶跃星辰）

### 18.1 Step-3 系列（继承 08-11，保留）

- **Step-3**（07-31）：198B 稀疏 MoE、256K ctx、GGUF 开源。
- **Step-3-0304**：70B 稀疏 MoE、256K ctx。
- **Step 3.5 Flash / 3.7 Flash**（05-29）仍为家族。

> 今日核实：无 8 月新报告；Step 4 训练（2026-02 宣布启动）为下一观察点。

---

## 19. Yi / 01.AI

### 19.1 Yi 系列（继承 08-11，保留）

- **Yi-34B / Yi-6B**（2023-11）；**Yi-Lightning**（2024-10-16，Chatbot Arena #6，arXiv:2412.01253）；**Yi-Coder**（2024-09）。

> 今日核实：2026 无新旗舰或新技术报告；开源节奏自 2024 年后放缓。

---

## 20. MiniMax

### 20.1 M2.7 自我进化（今日新增核实，08-08 官方新闻）

| 项目 | 内容 |
|------|------|
| **中文标题** | MiniMax M2.7——开启模型的自我进化 |
| **英文标题** | MiniMax M2.7 self-evolution |
| **发布机构** | MiniMax |
| **模型系列** | M2.7 |
| **发布日期** | 模型发布 2026-03-18；全量上线新闻 2026-08-08 |
| **核心创新** | "第一代自我进化"模型——深度参与迭代自身模型的 RL harness（Agent Harness 自建）；**MLE Bench Lite 22 任务 66.6% 得牌率**（9 gold/5 silver/1 bronze 最佳 run），仅次于 Opus 4.6（75.7%）/ GPT-5.4（71.2%），与 Gemini 3.1（66.6%）持平；已在 MiniMax Agent / 开放平台全量上线 |
| **论文** | MiniMax 官方新闻（08-08） |

### 20.2 M3 / H3（继承 08-11，保留）

- **M3**（2026-06-01）：428B；1M ctx；开源；现役 SOTA；**M4 仍为 H2 2026 承诺**。
- **MiniMax H3**（API 07-31；权重 08-02/03）：33B dense 单流 Omni Transformer；全模态生成。

> 今日核实：M2.7 为开源/全量上线方向最新动态；M4（H2 2026）无新进展。

---

## 交叉观察

- **08-12 双验收日：两"承诺制发布"均未兑现（截至撰写时）**——①**Meta Llama 4 405B 开放权重未发布**，实际为 08-10 战略转向（Muse Glimmer 30B 开源 + Muse Spark 1.2 权重承诺）；②**Qwen3.8-Max / 27B 权重未上架**（ModelScope 页面指向今日，HF 实时检查无条目、无 license）。对照 Kimi K3（07-27 按期放权）与 Nemotron 家族（报告齐备），"承诺→兑现"信用分化加剧。
- **同日并存的新发布/新动态**：NVIDIA Nemotron 3.5 Lightning（08-11）、MiniMax M2.7 自我进化全量上线（08-08 新闻）、Baichuan-M2 开源医疗模型（08-11）、DeepSeek API 涨价（08-06）、OpenAI Astra 定名（08-01）、Google DeepMind 领导层改组（08-05）。
- **闭源前沿"文档差距"持续扩大**：Grok 4.6（上线 5 天无 model card）、DeepSeek V4-Pro（官方窗口第 3 天仍无 GA）、Apple AFM 3（承诺未兑现）——与开源阵营（Muse Glimmer Apache 2.0、Nemotron 3.5 Lightning、Baichuan-M2 32B、Kimi K3 47 页报告）形成对照。
- **Agent 能力仍是官方评测主战场**：MiniMax M2.7 MLE Bench Lite 66.6%（自我进化 RL harness）、DeepSeek V4-Flash 9 项 Agent 基准、Muse Spark 1.2（Terminal-Bench 82.9）——自我进化/自训练 harness 成为新叙事（MiniMax M2.7、字节反蒸馏表态、Muse 蒸馏路径并存）。
- **"规模军备竞赛"叙事升级**：字节 >5T~10T 参数新模型（传闻）+ Grok 4.7（2.1T）+ Kimi K4（Blackwell 训练）+ 智谱 GLM-5.3（>1T）+ MiniMax M4——中国阵营继 2.4T（Qwen）/2.8T（K3）后继续上探。
- **传闻需谨慎（未确认不入正式条目）**：GPT-5.7（被 Astra 搁置）、Fable 5.1（08-03 核查无官方公告）、GLM-5.3/5.5（>1T，未发布）、Phi-5（single-source）、Grok 4.6 model card / 4.7、DeepSeek V4-Pro 官方窗口、Kimi K4、字节 >5T/10T 新模型、InternLM4、MiniMax M4（H2 2026）、Mistral 夏季"大而稀疏"开放权重。
