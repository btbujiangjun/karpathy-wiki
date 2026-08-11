---
title: "大模型技术报告摘要（2025-2026）| LLM Tech Report Digest (2025-2026)"
type: synthesis
created: 2026-08-11
updated: 2026-08-11
sources: [tech-report-digest-2026-08-10.md]
tags: [tech-report, system-card, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, bytedance, zhipu, kimi, internlm, baichuan, stepfun, minimax]
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告 / System Card 汇总。
> 更新日期：2026-08-11（每日更新；今日重点：**Meta Llama 4 开放权重明日（08-12）发布**——405B 参数、原生多模态（文本/图像/音频）、单 H100 推理 32 tok/s、15T tokens 训练含 2.4T 图文对，11/14 基准达到或超过 GPT-5 且推理计算量少 38%，另配 70B 蒸馏边缘版，Meta 官方技术报告仍待发布；**DeepSeek V4-Flash 官方 API 公开 beta（07-31）核实**——9 项 Agent benchmark 数据齐备（Terminal Bench 2.1: 82.7 / DeepSWE: 54.4 / Cybergym: 76.7），V4-Pro 官方窗口今日为第 2 天（08-10~08-20）；**Qwen3.8-Max 开源权重窗口今日为第 2 天（08-10~08-14）**——截至今日 HF/ModelScope 仍无权重条目，缺日期/license/model card；**Grok 4.6 已上线但官方 model card 缺席**——第三方 kie.ai 确认约 08-07 已上线（1.5T 参数、沿用 Grok 4.5 基座），xAI 官方 docs 目录仍仅列 grok-4.5，无官方基准/上下文/定价；Apple **AFM 3 技术报告已存在**（5 模型、与 Google 合作）但"later this summer"正式发布承诺仍未兑现；Anthropic **Claude Mythos Preview System Card**（04-07）为当前最先进闭源前沿；OpenAI **GPT-5.7 泄漏仍无官方确认**；Microsoft **Phi-5 / Amazon Nova / Mistral / MiniMax M4 均无 8 月新报告**）

---

## 1. DeepSeek（深度求索）

### 1.1 DeepSeek-V4-Flash 官方 API 公开 beta（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4-Flash 官方 API 公开 beta 版 |
| **英文标题** | DeepSeek-V4-Flash public beta API |
| **发布机构** | DeepSeek-AI |
| **模型系列** | V4-Flash（284B 总参 / 13B 激活 MoE + CSA） |
| **发布日期** | 2026-07-31 |
| **核心创新** | 官方公开 beta，Agent 能力突出——Terminal Bench 2.1: **82.7**、NL2Repo: **54.2**、Cybergym: **76.7**、DeepSWE: **54.4**、Toolathlon verified: **70.3**、Agent Last Exam: **25.2**、Automation Bench: **25.1**、DSBench-FullStack: **68.7**、DSBench-Hard: **59.6** |
| **论文** | https://releasebot.io/updates/deepseek |

> 今日核实：07-31 公开 beta 的 9 项 Agent 基准为官方页面数据，指标显著高于 V4-Pro-Preview 此前水平；与 08-04 确认的 DeepSeek-V4-Flash-0731（MIT 权重、$0.14/$0.28 per M）为同一刷新脉络——公开 beta = API 形态，0731 = 开源权重形态。V4 技术报告 arXiv:2606.19348 仍为官方论文。

### 1.2 DeepSeek-V4-Pro 官方发布窗口（今日第 2 天）

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4-Pro 官方版发布窗口传闻 |
| **英文标题** | DeepSeek V4-Pro official release window (rumored) |
| **发布机构** | DeepSeek-AI |
| **模型系列** | V4-Pro（1.6T 总参 / 49B 激活 MoE + CSA） |
| **发布日期** | V4-Pro-Preview：2026-04-24；官方版传闻窗口 **2026-08-10~08-20**（未确认） |
| **核心创新** | 官方版（非 Preview）承诺"will follow soon"；今日 08-11 为窗口第 2 天，官方仍无公告；V4-Pro-Preview 已预览近 4 个月 |
| **论文** | V4 技术报告 arXiv:2606.19348 |

> 今日核实：窗口（08-10~08-20）第 2 天仍无官方公告；若兑现将与 Llama 4 开放权重（08-12）撞期。为多源（中文科技媒体）报道，未确认，不升级为正式发布条目。

---

## 2. OpenAI

### 2.1 GPT-5.6 部署更新（08-06，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 Sol/Luna 全面部署 |
| **英文标题** | GPT-5.6 Sol & Luna deployment |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（Sol 旗舰 / Terra 中档 / Luna 最快最省） |
| **发布日期** | 2026-08-06（Sol 成为 Plus/Pro 默认、Luna 覆盖 Free/Go） |
| **核心创新** | Sol 成为 Plus/Pro 默认模型；Luna 覆盖 Free 与 Go 层；新增 Think 按钮显式控制推理预算；此前 07-30 已降价（Luna -80%、Terra -20%） |
| **论文** | https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/ |

> 今日核实：无 8 月新技术报告；GPT-5.6 System Card（07-09）仍为最新。

### 2.2 GPT-5.7 泄漏复核（保留待确认）

> ⚠️ 传闻更新（今日复核）：WinCentral 2026-07-30 报道 **GPT-5.7**（8 月发布，新的 pretraining foundation，约 10T tokens 规模训练，更强推理与 agent 能力），GPT-6 或推迟至 9 月；The Information 报道 OpenAI 内部代号 **Astra** 新模型家族。截至 08-11 仍为记者爆料，未获官方确认，不写入正式条目。

---

## 3. Meta

### 3.1 Llama 4 开放权重明日发布（08-12，今日最大新闻核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Meta 确认 Llama 4 开放权重明日 08-12 发布 |
| **英文标题** | Meta confirms Llama 4 open weights for August 12 |
| **发布机构** | Meta AI（NeuralStack 2026-07-28 援引 Bloomberg + X/@pmarca 佐证） |
| **模型系列** | Llama 4（新一代开放权重；Scout/Maverick/Behemoth 为 2025-04 时代版本） |
| **发布日期** | **2026-08-12（Meta 07-27 确认）——明日** |
| **核心创新** | **405B 参数**；原生**多模态**（文本/图像/音频）；**单张 H100 推理 32 tok/s**；**15T tokens 训练（含 2.4T 图文对）**；**11/14 基准达到或超过 GPT-5，推理计算量少 38%**；另配 **70B 蒸馏边缘版** |
| **论文** | 官方技术报告待发布（报道依据 Bloomberg/neuralstack；Meta 官方博客/模型页暂缺） |

> 今日核实：新增细节（相对 08-10 日报）——**15T 训练 tokens 含 2.4T 图文对**、**11/14 基准超 GPT-5 且推理计算少 38%**、**70B 蒸馏边缘版**。口径提示仍保留：405B 与 2025-04 Behemoth "近 2T" 说法不一致，**以 08-12 实际发布为准**。**明日为最终验收日。**

### 3.2 Muse 系列（已收录，保留）

- **Muse Spark Safety & Preparedness Report**（2026-07，PDF；Spark 1.1 07-09 开放）：依据 Meta **Advanced AI Scaling Framework** 评估；Chem/Bio 缓解前 "high risk"；拒绝率 SOTA；cyber-misuse compliance 同行最低。arXiv:2606.12429。
- **Muse Code**（2026-08-05）：首个 AI 编程智能体（terminal coding agent），贡献者档每百万输出 token 仅 $0.20 低价策略。
- **Muse Spark 1.2**（2026-08-05）：Terminal-Bench 82.9%。

> 今日核实：**08-12 Llama 4 开放权重为下一观察日**。

---

## 4. Google DeepMind

### 4.1 Gemini 系列状态（今日复核）

- **Gemini 3.1 Pro Model Card**（2026-02）为当前官方最新 Pro 级 Model Card：https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-1-Pro-Model-Card.pdf
- **Gemini 4 预训练中**（07-21 确认）：为 "most ambitious pretraining run yet"；暂无发布日期；Gemini 3.5 Pro 仍与合作伙伴测试中（延迟）。
- **Gemini 3.6 Flash**（07-21）：原生多模态推理；workhorse；知识截止 2026-03。https://deepmind.google/models/model-cards/gemini-3-6-flash/
- **Gemini Robotics 2 / ER 2 / On-Device 2**（07-30）：机器人品类最新三张卡。

> 今日核实：8 月仅有 Classroom 集成类更新（releasebot 08-08），无新模型卡。

---

## 5. Anthropic

### 5.1 Claude Mythos Preview System Card（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Mythos Preview 系统卡 |
| **英文标题** | Claude Mythos Preview System Card |
| **发布机构** | Anthropic |
| **发布日期** | System Card PDF: 2026-04-07 |
| **核心创新** | 当前最先进闭源前沿（most capable frontier model）；**首个按 RSP v3（Responsible Scaling Policy）发布决策审查的系统卡**——包括预评估、异常部署报告与缓解承诺 |
| **论文** | PDF: https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf |

### 5.2 Claude Opus 5 System Card（已收录，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 5 系统卡 |
| **英文标题** | Claude Opus 5 System Card |
| **发布机构** | Anthropic |
| **发布日期** | System Card PDF: 2026-07-24 |
| **核心创新** | agentic coding、computer use、long-horizon knowledge work；effort dial（$5/$25 每 M in/out）；SWE-bench Verified 96.0、SWE-bench Pro 79.2、Frontier-Bench v0.1 43.3、ARC-AGI-3 30.2 |
| **论文** | PDF: https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude%20Opus%205%20System%20Card.pdf |

### 5.3 Fable 5.1 泄漏（保留，未确认）

> ⚠️ 传闻（未确认）：X/@rowancheung 报道 **Fable 5.1**（Claude Fable 5 的升级）预计 8 月发布、抢在 GPT-6 之前。Claude Fable 5（06-09）为闭源能力前沿（SWE-bench 95.5%）。截至 08-11 无官方确认。

---

## 6. Mistral

### 6.1 开发者能力新增（07-28/08-06，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral 开发者平台新增模型能力 |
| **英文标题** | Mistral: Nova 2 compute / Gemini vision / Claude codebase for developers |
| **发布机构** | Mistral AI |
| **发布日期** | 2026-07-28~08（陆续） |
| **核心创新** | 为开发者提供 **Nova 2 计算 / Latent reasoning**、**Gemini 2.5 / 2.5 Pro 的图像理解**、**Claude Sonnet 4.5 代码库**能力；并推出带日志（logging）与影子提示（shadow prompt）版本的合规选项——聚合多家第三方模型能力形成开发平台 |
| **论文** | https://mistral.ai/news/ |

> 今日核实：无 8 月新技术报告；最新自有模型仍为 Mistral Large 3（2025-12，675B）。Mistral 重心转向"模型经纪人"（model broker）定位。

---

## 7. Qwen（通义千问）

### 7.1 Qwen3.8-Max 开源权重窗口（今日第 2 天）

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.8-Max 开源权重（本周窗口） |
| **英文标题** | Qwen3.8-Max open weights (this week) |
| **发布机构** | Alibaba Qwen |
| **模型系列** | Qwen3.8（Max 旗舰） |
| **发布日期** | 2026-08-03（官方发布页 GA）；**开源权重窗口：本周 2026-08-10~08-14（今日第 2 天）** |
| **架构** | **2.4T 总参 Sparse MoE / 95B 激活** + hybrid attention（基于 Qwen 3.5 架构） |
| **核心创新** | 首个开源权重的 Max 级模型；**1M 上下文**；原生视觉多模态（文本/图像/视频输入）；**$2 in / $6 out 每 M tokens**；Text Arena #5 / Vision Arena #2；权重**本周（08-10~08-14）上 HF/ModelScope** |
| **论文** | https://qwen.ai/blog?id=qwen3.8 |

> 今日状态（权重窗口第 2 天）：**截至今日搜索 HF/ModelScope 仍无新权重条目**——仍缺具体日期 + license + model card。对照 Moonshot Kimi K3 按期放权（07-27 兑现），评论界持续质疑。08-12 前后为关键观察点。

### 7.2 其他 Qwen 条目（保留）

- **Qwen3.8-27B**（08-03）：与 Max 同日发布的 27B 档模型。
- **Qwen3.7-Flash**（07-25）：Flash 系列原生视觉语言升级。
- **Qwen-Audio-3.0-ASR-Flash**（07-30）：30 语言 + 中文七大方言 ASR 家族。
- **Qwen-UI-Agent Technical Report**（07，arXiv:2607.28227）：GUI 代理技术报告。

---

## 8. Microsoft（Phi）

### 8.1 Phi-5 状态（今日复核，保留）

- **Phi-4-reasoning-vision-15B Technical Report**（2026-03，MSR-TR-2026-10）：数据质量为最大性能杠杆；动态分辨率视觉编码器；单一模型双模式（推理/非推理 mode token）。

> ⚠️ 传闻更新（今日核实）：**Phi-5** 截至 08-11 仍无官方技术报告——唯一新增为 Inference Index 目录条目（2026-01-08，128K ctx）；此前的 16B / MMLU 86.7% 报道为 single-source（GogoAI），官方 MSR 页面仍以 Phi-4-reasoning-vision-15B 为最新技术报告，**未确认，不写入正式条目**。

---

## 9. Apple

### 9.1 AFM 3（今日核实：技术报告已存在，正式发布仍待兑现）

| 项目 | 内容 |
|------|------|
| **中文标题** | 第三代 Apple Foundation Models（AFM 3） |
| **英文标题** | Introducing the Third Generation of Apple's Foundation Models |
| **发布机构** | Apple（与 Google 合作定制，训练于 Google Cloud TPU） |
| **模型系列** | AFM 3 Core（3B 端侧 dense）/ Core Advanced（20B 端侧稀疏，IFP 激活 1–4B）/ AFM 3 Cloud（PCC）/ ADM 3 Cloud（图像生成）/ AFM 3 Cloud Pro（PCC on Google Cloud NVIDIA GPU） |
| **发布日期** | 2026-06-08（WWDC26） |
| **核心创新** | IFP（Instruction-Following Pruning）：全模型放 flash、按 prompt 一次路由加载 1–4B 专家权重 + always-active shared experts；AFM 3 Cloud Pro 首次把 PCC 扩展到 Google Cloud NVIDIA GPU |
| **论文** | https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models |

> 今日核实：**AFM 3 技术报告已存在**（"Introducing the Third Generation of Apple's Foundation Models"，含 5 个模型细节）；但 06-08 承诺的 "later this summer" **正式发布仍未兑现**（08-11 仍在"summer"内，2025 年 AFM 2 报告为 7 月发布）；Siri AI 已进入 iOS 27 消费者测试版。

---

## 10. NVIDIA

### 10.1 Nemotron 3 家族（今日核实，保留）

- **Nemotron 3 Ultra**（技术报告 PDF 06-09）：550B 总参 / 55B 激活 MoE **混合 Mamba-Attention**（Mamba-2 + Attention）+ **LatentMoE** + MTP；20T tokens；NVFP4 量化感知预训练；多环境 RLVR（MOPD）；1M ctx；~6× 推理吞吐；开源。
- **Nemotron 3 Super**（技术报告 PDF 04-03）：120B/12B；25T tokens；吞吐最高 2.2× GPT-OSS-120B / 7.5× Qwen3.5-122B；1M ctx；开源。
- **Nemotron 3 Nano**（08-04）：30B-A3B；吞吐最高 3.3×。

> 今日核实：Nemotron 3 三档技术报告全部收录；**官方 Nemotron 3 家族正式发布总报告仍待发布**；无 8 月新报告。官网（developer.nvidia.com/topics/ai/nemotron）确认 1M-token 上下文 + 开放权重 + 技术报告为家族卖点。

---

## 11. xAI

### 11.1 Grok 4.6（今日核实：已上线但官方 model card 缺席）

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.6（已上线，官方卡缺席） |
| **英文标题** | Grok 4.6 (live; no official model card) |
| **发布机构** | xAI（SpaceX 收购后改称 SpaceXAI） |
| **模型系列** | Grok 4.6（**1.5T 参数**、基于 Grok 4.5 V9 基座） |
| **发布日期** | 约 **2026-08-07 上线**（第三方 kie.ai 确认）；Musk 08-04 财报电话会 "next week" 兑现 |
| **核心创新** | 重点在大幅升级的 **SFT + RL 后训练**（Musk 07-28 确认，基座与 4.5 相同 1.5T V9）；**仍无官方 model card / 基准 / 上下文 / 定价** |
| **论文** | https://x.ai/news/grok-4-5（官方最新博文仍为 4.5） |

> 今日核实：kie.ai 文章（07-30）与 blog.4sapi.com（Grok 4.6/Grok 5 roadmap）确认 08-07 上线；但 **xAI 官方 docs.x.ai 模型目录截至今日仍仅列 grok-4.5**（$2/$6、500K ctx、知识截止 2026-02-01），API release notes 无 4.6 条目——"上线 vs 官方目录"矛盾持续。**无官方 model card**。Grok 4.7（2.1T）计划 3-4 周后、Grok 5 年内。

---

## 12. Amazon

### 12.1 Nova 家族（今日复核，保留）

- **Nova 2 Sonic 2.1**（部署 05-21~05-28）：**自回归 transformer 架构（无视觉编码器）**——多模态能力通过直接 token 化输入而非独立视觉编码器实现；与 Nova 2 技术报告（2025-12-02，Hybrid Reasoning + 1M ctx）口径一致。https://docs.aws.amazon.com/nova/
- **Nova 原版技术报告**（2024）："The Amazon Nova Family of Models"（Lite/Pro/Premier）为唯一正式技术报告：https://www.amazon.science/publications/the-amazon-nova-family-of-models-technical-report-and-model-card
- **战略收缩**（07-28）：逐步弃用 Nova Premier / Omni / Reel / Canvas（Premier 9 月 EOL）；AGI Lab 解散；Frontier Model Research (FMR) 由 Pieter Abbeel（Covariant）领导；新旗舰目标 re:Invent 2026 秋。

> 今日核实：**无 Nova 3 技术报告**；原版 Nova TR（2024）仍为唯一正式报告；re:Invent 2026（秋）为下一观察点。

---

## 13. ByteDance（字节跳动）

### 13.1 Seed2.1（今日新增核实：Model Card 确认）

| 项目 | 内容 |
|------|------|
| **中文标题** | 字节 Seed2.1（Pro + Turbo） |
| **英文标题** | ByteDance Seed2.1 (Pro + Turbo) |
| **发布机构** | ByteDance Seed |
| **模型系列** | Seed2.1（Pro / Turbo） |
| **发布日期** | 2026（Pro 首发 06-23 报道；Turbo 随家族发布） |
| **核心创新** | 面向 **Agent / 代码工程**（agentic + coding E2E）；**视频理解多评测 SOTA（含小时级长视频）**；Pro 在 dev crowdsource coding 上以 59.1% 击败 Claude Opus 4.6；**官方 Model Card PDF 随发布提供** |
| **论文** | https://seed.bytedance.com/zh/seed2_1（Model Card PDF 随附） |

> 今日核实：Model Card 为官方发布物之一；Seed2.0 Pro / Lite / Mini 为系列；Seedance 2.5（07-31）为视频生成方向最新。官方研究博客：https://research.doubao.com/zh/blog/seed2-1-officially-released-advancing-ai-productivity

---

## 14. Zhipu（智谱）

### 14.1 GLM-5 技术报告（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5 技术报告 |
| **英文标题** | GLM-5 Technical Report |
| **发布机构** | 智谱（Zhipu AI） |
| **模型系列** | GLM-5（~745B 总参 / 44B 激活） |
| **发布日期** | 技术报告 2026-02-22；36kr 08-09 复述报道 |
| **核心创新** | **DSA（DeepSeek Sparse Attention）** 类稀疏注意力；**异步 RL 基础设施**；**异步 Agent RL 算法**——端到端软件工程任务超越此前开源基线；完全适配华为等国产芯片 |
| **论文** | https://news.qq.com/rain/a/20260222A0561T00（腾讯新闻 02-22）；36kr 08-09: https://www.36kr.com/p/3695400723394178 |

### 14.2 GLM-5.2 / GLM-5.5 传闻（保留）

- **GLM-5.2**（2026-06-13）：MIT 开放权重；1M ctx；稀疏注意力 + IndexShare；无原生视觉。https://zhipu-ai.cn/glm-5.2

> ⚠️ **GLM-5.5** 截至 08-11 仍未发布：JPMorgan 研报称可能 2026-08 发布，1T+ 参数、1M ctx。单源传闻，不写入正式条目；GLM-5.2 仍为当前确认旗舰。

---

## 15. Moonshot（月之暗面）

### 15.1 Kimi K3 / K4（今日复核）

- **Kimi K3**（API 2026-07-16；**全量权重 + 47 页技术报告 2026-07-27**）：2.8T 总参 / 104B 激活；93 层 = 69 KDA + 24 Gated MLA；896 experts；AttnRes；MoonViT-V2；MXFP4/8 量化感知训练；1M ctx；首个开源 3T 级模型；~2.5× scaling efficiency vs K2；WebDev Arena #1。https://kimi.ai/k3-technical-report
- **MoonEP / FlashKDA**（07-29）：K3 全链路开源配套。

> 今日复核：**Kimi K4 训练中，寻求更多 NVIDIA Blackwell 芯片**（The Information / AI Weekly 07-28/29）——训练阶段传闻，未发布，不入正式条目。K3 技术报告（07-27）仍为最新，权重已按期兑现（对照 Qwen3.8-Max）。

---

## 16. InternLM（上海 AI 实验室）

### 16.1 Intern-S2-Preview（08-05 已确认，保留）

- **Intern-S2-Preview**（35B 07-17 / 397B 07-18）：科学多模态基础模型；**task scaling**（提升科学任务难度/多样性/覆盖度而非仅扩参数）；35B 媲美万亿级 Intern-S1-Pro；397B 为 MoE ~120B 激活；Apache-2.0；BF16 + FP8。35B: https://huggingface.co/internlm/Intern-S2-Preview

> 今日复核：无 8 月新报告；InternLM3 / InternLM 3.5 为开源聊天系列当前最新；**InternLM4 官方状态不明**（X/@ncap_and 04-13 传闻，未确认）。

---

## 17. Baichuan（百川智能）

### 17.1 Baichuan-M4（已收录，保留）

- **Baichuan-M4**（2026-05-26 发布 / 06-22 与清华正式发布）：临床级医疗 Agent 系统；**HealthBench 68.6 世界第一**（超 GPT-5.5 10+ 分）；hallucination 3.3%；事实性感知 RL。arXiv:2606.08982。
- **Baichuan-M3**（2026-01）：235B；HealthBench 65.1。

> 今日核实：无 2026 年 8 月新报告；公司战略全面转向医疗垂直领域。

---

## 18. StepFun（阶跃星辰）

### 18.1 Step-3 系列（保留）

- **Step-3**（2026-07-31）：198B 稀疏 MoE、256K ctx、GGUF 格式开源。
- **Step-3-0304**：70B 稀疏 MoE、256K ctx、Open Source。
- **Step 3.5 Flash**（02 开源，196B/11B 激活，MTP-3）与 **Step 3.7 Flash**（05-29）仍为家族。

> 今日核实：无 8 月新报告；Step 4 训练 2026-02 已宣布启动。https://github.com/stepfun-ai/Step3

---

## 19. Yi / 01.AI

### 19.1 Yi 系列（今日复核，保留）

- **Yi-34B / Yi-6B**（2023-11）：开源旗舰。
- **Yi-Lightning**（2024-10-16）：01.AI 旗舰 MoE，Chatbot Arena #6；$0.14/M tokens；arXiv:2412.01253。
- **Yi-Coder**（2024-09）：开放权重编程模型。

> 今日核实：2026 无新旗舰或新技术报告，repo 冻结于 Yi-1.5 / Yi-9B-200K；开源节奏自 2024 年后放缓。

---

## 20. MiniMax

### 20.1 M3 / M4（保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | MiniMax M3（现役 SOTA 旗舰）|
| **英文标题** | MiniMax M3 |
| **发布机构** | MiniMax |
| **模型系列** | M3 |
| **发布日期** | 2026-06-01 |
| **架构** | 428B 参数；1M context；**开源** |
| **核心创新** | 现役 SOTA；M4 传闻 H2 2026 发布（多信源），无官方报告 |
| **论文** | https://www.minimax.io/ |

- **MiniMax H3**（API 07-31；开源权重 08-02/03）：33B dense 单流 Omni Transformer；文本/图像/视频/音频统一全模态生成；最高 15s 2K 视频。https://huggingface.co/MiniMaxAI/MiniMax-H3

> 今日核实：**M4 仍为 H2 2026 承诺**，无新进展。

---

## 交叉观察

- **"承诺制发布"明日集中验收（08-12）**：①**Meta Llama 4 开放权重明日 08-12**——405B / 原生多模态（文本/图像/音频）/ 单 H100 32 tok/s / 15T tokens（含 2.4T 图文对）/ 11-14 基准超 GPT-5 且推理计算少 38% / 70B 蒸馏边缘版，Meta 官方技术报告仍待发布；②**Qwen3.8-Max 开源权重**——窗口今日第 2 天（08-10~08-14），2.4T MoE / 95B 激活 / 1M ctx，截至今日 HF/ModelScope 仍无条目，缺日期/license/model card；③**DeepSeek V4-Pro 官方版**——传闻窗口 08-10~08-20 今日第 2 天，无官方公告；④**Grok 4.6**——第三方确认 08-07 已上线，但 xAI 官方目录/API release notes 仍无记录，无官方 model card。
- **闭源前沿"文档差距"持续**：Grok 4.6（上线 4 天无 model card）、V4-Pro（官方版窗口期）、Apple AFM 3（技术报告存在但正式发布承诺未兑现）——与开源阵营（K3 全量权重+47 页报告、Nemotron 3 家族报告齐备）形成鲜明对照。
- **Agent 能力成为官方评测新主战场**：DeepSeek V4-Flash 9 项 Agent 基准（Terminal Bench 82.7 / DeepSWE 54.4 / Cybergym 76.7）为官方数据，与 Claude Opus 5（SWE-bench Pro 79.2 / Frontier-Bench 43.3）、Muse Spark 1.2（Terminal-Bench 82.9）、Grok 4.5（DeepSWE 62.0）形成可比的 agentic 基准图谱。
- **稀疏注意力进入收敛期**：DeepSeek CSA（V4）、智谱 DSA（GLM-5）、NVIDIA Mamba-Attention 混合（Nemotron 3）、Qwen hybrid attention（3.8）、MiniMax H3 omni——2026 架构共性已从"稀疏化探索"转为"稀疏化标配"。
- **"预览期拉长成为常态"持续**：DeepSeek V4-Pro-Preview 已近 4 个月（04-24→08-11）；Gemini 3.5 Pro 持续延迟；Apple AFM 3 正式发布窗口持续悬置。
- **8 月第二波"旗舰对决"成形**：明日 Llama 4（开放权重）+ 本周 Qwen3.8-Max（开源 Max 级）+ 已上线 Grok 4.6（闭源，无卡）+ V4-Pro 窗口 + 传闻 GPT-5.7 / Fable 5.1——8 月 12-20 为 2026 迄今最密集的发布/验收碰撞窗口。
- **传闻需谨慎（未确认不入正式条目）**：GPT-5.7/Astra（The Information + WinCentral）、Fable 5.1（07-27 泄漏）、GLM-5.5（JPMorgan 8 月）、Phi-5（仅 Inference Index 目录条目）、Grok 4.6 model card / 4.7（Musk 口头时间表）、DeepSeek V4-Pro 官方版窗口（中文媒体）、Kimi K4（Blackwell 训练传闻）、InternLM4（04-13 传闻）、MiniMax M4（H2 2026）。
