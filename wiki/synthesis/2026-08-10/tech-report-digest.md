---
title: "大模型技术报告摘要（2025-2026）| LLM Tech Report Digest (2025-2026)"
type: synthesis
created: 2026-08-10
updated: 2026-08-10
sources: [tech-report-digest-2026-08-08.md]
tags: [tech-report, system-card, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, bytedance, zhipu, kimi, internlm, baichuan, stepfun, minimax]
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告 / System Card 汇总。
> 更新日期：2026-08-10（每日更新；今日重点：**Meta 确认 Llama 4 开放权重定档 08-12（2 日后）**——Bloomberg 07-27 报道 + X/@pmarca 佐证，405B 参数、多模态（文本/图像/音频）、单 H100 推理 32 tok/s，Meta 官方尚未发布独立技术报告；**DeepSeek V4-Pro 官方发布窗口传闻开启（今日 08-10 为窗口第一天）**——中文科技媒体称官方版可能 08-10~08-20 发布，V4-Pro-Preview 自 04-24 起预览已近 4 个月；**Qwen3.8-Max 开源权重窗口进入本周（08-10~08-14）**——byteiota 08-10 确认权重本周放行，2.4T 参数、基于 Qwen 3.5 架构、首个开源权重的 Max 级模型，截至今日 HF/ModelScope 仍无条目；**Grok 4.6 窗口外溢至本周（08-10~08-14）**——Musk 08-04 财报电话会"next week"承诺本周到期，仍无官方 model card / 定价 / 基准；Apple **AFM 3 技术报告仍待发布**（"later this summer" 承诺持续未兑现）；OpenAI **GPT-5.7 泄漏仍无官方确认**；Anthropic **Fable 5.1 泄漏**（07-27：8 月发布、抢在 GPT-6 前，未确认）；Microsoft **Phi-5 仍无官方技术报告**；MiniMax M4 仍为 H2 2026 承诺；InternLM/Yi/Baichuan/StepFun 均无 8 月新报告）

---

## 1. DeepSeek（深度求索）

### 1.1 DeepSeek-V4-Pro 官方发布窗口（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4-Pro 官方版发布窗口传闻 |
| **英文标题** | DeepSeek V4-Pro official release window (rumored) |
| **发布机构** | DeepSeek-AI |
| **模型系列** | V4-Pro（1.6T 总参 / 49B 激活 MoE + CSA） |
| **发布日期** | V4-Pro-Preview：2026-04-24；官方版传闻窗口 **2026-08-10~08-20**（未确认） |
| **核心创新** | 官方版（非 Preview）此前承诺"will follow soon"；中文科技媒体 08-06 起报道官方版可能本周至下周发布；V4-Pro-Preview 已预览近 4 个月（04-24 起），为目前最久的 Preview 状态 |
| **论文** | V4 技术报告 arXiv:2606.19348 |

> 今日核实：**今日 08-10 为传闻窗口（08-10~08-20）第一天**——官方尚无公告；若兑现，将与 Llama 4 开放权重（08-12）撞期。此为多源（中文科技媒体）报道，非官方确认，不升级为正式发布条目。

### 1.2 DeepSeek-V4-Flash-0731（08-04 已确认，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4-Flash-0731 刷新版 |
| **英文标题** | DeepSeek-V4-Flash-0731 |
| **发布机构** | DeepSeek-AI |
| **模型系列** | V4-Flash（284B 总参 / 13B 激活 MoE） |
| **发布日期** | 2026-07-31 |
| **架构** | 与 4 月 V4-Flash 同架构（CSA Compressed Sparse Attention），重新后训练（re-post-trained） |
| **核心创新** | 官方构建版，在 DeepSeek 全部 9 项 agent benchmark 上超越 V4-Pro-Preview；MIT 权重开源（HF）；API $0.14 in / $0.28 out 每 M tokens，98% cache-hit 折扣 |
| **论文** | https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731 |

---

## 2. OpenAI

### 2.1 GPT-5.6 部署更新（08-06，今日新增核实）

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

> ⚠️ 传闻更新（今日复核）：WinCentral 2026-07-30 报道 **GPT-5.7**（8 月发布，新的 pretraining foundation，约 10T tokens 规模训练，更强推理与 agent 能力），GPT-6 或推迟至 9 月；The Information 报道 OpenAI 内部代号 **Astra** 新模型家族。截至 08-10 仍为记者爆料，未获官方确认，不写入正式条目。

---

## 3. Meta

### 3.1 Llama 4 开放权重定档 08-12（今日最大新闻，新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Meta 确认 Llama 4 开放权重 08-12 发布 |
| **英文标题** | Meta confirms Llama 4 open weights for August 12 |
| **发布机构** | Meta AI（NeuralStack 2026-07-28 援引 Bloomberg + X/@pmarca 佐证） |
| **模型系列** | Llama 4（Scout / Maverick / Behemoth 为 2025-04 时代版本；此为新一代开放权重） |
| **发布日期** | **2026-08-12（Meta 07-27 确认）** |
| **核心创新** | **405B 参数**；原生**多模态**（文本/图像/音频）；**单张 H100 推理 32 tok/s**；Meta 官方称 08-12 为发布日期目标（Meta 07-27 确认，原传 07-31 因故延期） |
| **论文** | 官方技术报告待发布（报道依据 Bloomberg；Meta 官方博客/模型页暂缺） |

> ⚠️ 口径提示：07-27 确认的 405B 与早期 Llama 4 Behemoth "近 2T" 说法不一致——NeuralStack 报道明确写 405B，而 2025-04 Llama 4 家族（Scout 109B / Maverick 400B / Behemoth ~2T 训练中）中 Maverick 即为 400B 档。405B 可能是新发布档位或媒体误差，**以 08-12 实际发布为准**。多模态（文本+图像+音频）与单 H100 32 tok/s 为报道要点。

### 3.2 Muse 系列（已收录，保留）

- **Muse Spark Safety & Preparedness Report**（2026-07，PDF；Spark 1.1 07-09 开放）：依据 Meta **Advanced AI Scaling Framework** 评估；Chem/Bio 缓解前 "high risk"；拒绝率 SOTA；cyber-misuse compliance 同行最低。arXiv:2606.12429。
- **Muse Code**（2026-08-05）：首个 AI 编程智能体（terminal coding agent），贡献者档每百万输出 token 仅 $0.20 低价策略（投资日报 08-06 已收录）。
- **Muse Spark 1.2**（2026-08-05）：Terminal-Bench 82.9%。

> 今日核实：Meta 无 08-10 当日新报告；**Llama 4 开放权重 08-12 为下一观察日**。

---

## 4. Google DeepMind

### 4.1 Gemini 4 预训练确认（07-21，保留）

- **Gemini 4 预训练中**（Gemini family update 2026-07-21 + Pichai Q2 财报电话会 07-22 首次官方确认）：为"most ambitious pretraining run yet"；**暂无发布日期**。Gemini 3.5 Pro 仍与合作伙伴测试中（延迟）。
- **Gemini 3.6 Flash**（07-21）：原生多模态推理；workhorse；知识截止 2026-03。https://deepmind.google/models/model-cards/gemini-3-6-flash/
- **Gemini 3.5 Flash-Lite**（07-21）：低成本层，现综合价 $2.80/M（已被 OpenAI Luna $1.40/M 超越）。

> 今日核实：官方最新模型卡仍为 Gemini 3.6 Flash / 3.5 Flash-Lite（07-21）；Gemini Robotics 2 / ER 2 / On-Device 2 三张模型卡（07-30）为机器人品类最新；8 月无新卡。Gemini 3.6 Flash 为近月"near-monthly"节奏延续。

---

## 5. Anthropic

### 5.1 Claude Opus 5 System Card（已收录，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 5 系统卡 |
| **英文标题** | Claude Opus 5 System Card |
| **发布机构** | Anthropic |
| **发布日期** | System Card PDF: 2026-07-24 |
| **核心创新** | agentic coding、computer use、long-horizon knowledge work；effort dial（$5/$25 每 M in/out）；SWE-bench Verified 96.0、SWE-bench Pro 79.2、Frontier-Bench v0.1 43.3、ARC-AGI-3 30.2 |
| **论文** | PDF: https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude%20Opus%205%20System%20Card.pdf |

### 5.2 Fable 5.1 泄漏（07-27，新增核实，未确认）

> ⚠️ 传闻（未确认）：X/@rowancheung 报道 **Fable 5.1**（Claude Fable 5 的升级）预计 8 月发布、抢在 GPT-6 之前。Claude Fable 5（06-09）为闭源能力前沿（SWE-bench 95.5%）。截至 08-10 无官方确认；Anthropic 最新官方 System Card 仍为 Opus 5（07-24），Sonnet 5 System Card 文档站更新至 07-10 版本。

---

## 6. Mistral

### 6.1 开发者能力新增（07-28/08-06，今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral 开发者平台新增模型能力 |
| **英文标题** | Mistral: Nova 2 compute / Gemini vision / Claude codebase for developers |
| **发布机构** | Mistral AI |
| **发布日期** | 2026-07-28~08（陆续） |
| **核心创新** | 为开发者提供 **Nova 2 计算 / Latent reasoning**、**Gemini 2.5 / 2.5 Pro 的图像理解**、**Claude Sonnet 4.5 代码库**能力；并推出带日志（logging）与影子提示（shadow prompt）版本的合规选项——聚合多家第三方模型能力形成开发平台 |
| **论文** | https://mistral.ai/news/ |

### 6.2 其他 Mistral 条目（保留）

- **Shieldstral**（08-04 公告 / 07-28 arXiv）：3B 多模态安全分类器；policy-adaptive QA；Apache-2.0；12 种语言；单张 16GB GPU；匹配 7× 体积模型；加入 Open Secure AI Alliance。
- **Mistral Medium 3**（08-02）：128K；la Plateforme + Azure Foundry。
- **Leanstral 1.5**（07-02）：119B 总 / 6B 激活稀疏 MoE；Apache-2.0；miniF2F 100%。
- **Robostral Navigate**（07-08）：具身导航模型。

> 今日核实：无 8 月新技术报告；最新自有模型仍为 Mistral Medium 3.5（04-29，AI Release Tracker）。Mistral 重心转向聚合层（第三方模型代理能力）。

---

## 7. Qwen（通义千问）

### 7.1 Qwen3.8-Max 开源权重窗口进入本周（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.8-Max 开源权重（本周窗口） |
| **英文标题** | Qwen3.8-Max open weights (this week) |
| **发布机构** | Alibaba Qwen |
| **模型系列** | Qwen3.8（Max 旗舰） |
| **发布日期** | 2026-08-03（官方发布页）；**开源权重窗口：本周 2026-08-10~08-14** |
| **架构** | 2.4T 总参 Sparse MoE + hybrid attention（基于 Qwen 3.5 架构，byteiota） |
| **核心创新** | 首个开源权重的 Max 级模型（weight-open Max-level）；原生视觉多模态；Text Arena #5 / Vision Arena #2；$2 in / $6 out / $0.25 cached per 1M tokens；08-02 X/@SirSafeAI "harden" + 暗示下周发布 → 本周窗口兑现中 |
| **论文** | https://qwen.ai/blog?id=qwen3.8 |

> 今日状态（权重窗口进入本周）：byteiota 08-10 明确称权重窗口为 8 月 10 日那周；08-02 X/@SirSafeAI 暗示"下周"发布。**截至今日搜索 HF/ModelScope 仍无新权重条目**，仍缺具体日期 + license + model card——对照 Moonshot Kimi K3 按期放权（07-27），评论界持续质疑。**08-10~08-14 为最终权重观察窗口**。

### 7.2 其他 Qwen 条目（保留）

- **Qwen3.7-Flash**（07-25）：Flash 系列原生视觉语言升级。
- **Qwen-Audio-3.0-ASR-Flash**（07-30）：30 语言 + 中文七大方言 ASR 家族。
- **Qwen-UI-Agent Technical Report**（07，arXiv:2607.28227）：GUI 代理技术报告。

---

## 8. Microsoft（Phi）

### 8.1 Phi-5 状态（今日复核，保留）

- **Phi-4-reasoning-vision-15B Technical Report**（2026-03，MSR-TR-2026-10）：数据质量为最大性能杠杆；动态分辨率视觉编码器；单一模型双模式（推理/非推理 mode token）。

> ⚠️ 传闻更新（今日核实）：**Phi-5** 截至 08-10 仍无官方技术报告——唯一新增为 Inference Index 目录条目（2026-01-08，128K ctx）；此前的 16B / MMLU 86.7% 报道为 single-source（GogoAI），官方 MSR 页面仍以 Phi-4-reasoning-vision-15B 为最新技术报告，**未确认，不写入正式条目**。

---

## 9. Apple

### 9.1 AFM 3（已收录；技术报告持续未发布）

| 项目 | 内容 |
|------|------|
| **中文标题** | 第三代 Apple Foundation Models（AFM 3） |
| **英文标题** | Introducing the Third Generation of Apple's Foundation Models |
| **发布机构** | Apple（与 Google 合作定制，训练于 Google Cloud TPU） |
| **模型系列** | AFM 3 Core（3B 端侧 dense）/ Core Advanced（20B 端侧稀疏，IFP 激活 1–4B）/ AFM 3 Cloud（PCC）/ ADM 3 Cloud（图像生成）/ AFM 3 Cloud Pro（PCC on Google Cloud NVIDIA GPU） |
| **发布日期** | 2026-06-08（WWDC26） |
| **核心创新** | IFP（Instruction-Following Pruning）：全模型放 flash、按 prompt 一次路由加载 1–4B 专家权重 + always-active shared experts；AFM 3 Cloud Pro 首次把 PCC 扩展到 Google Cloud NVIDIA GPU |
| **论文** | https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models |

> 今日核实：**AFM 3 正式技术报告仍待发布**——承诺 "later this summer" 已过（08-10 仍在"summer"内，2025 年 AFM 2 技术报告为 7 月发布），仍为"承诺未兑现"观察项；Siri AI 已进入 iOS 27 消费者测试版（2026-07 起，TechCrunch 08-03 "Apple finally fixed Siri"）。

---

## 10. NVIDIA

### 10.1 Nemotron 3 家族（已收录，保留；官方报告仍待发布）

- **Nemotron 3 Ultra**（技术报告 PDF 06-09）：550B 总参 / 55B 激活 MoE **混合 Mamba-Attention**（Mamba-2 + Attention）+ **LatentMoE** + MTP；20T tokens；NVFP4 量化感知预训练；多环境 RLVR（MOPD）；1M ctx；~6× 推理吞吐；开源。
- **Nemotron 3 Super**（技术报告 PDF 04-03）：120B/12B；25T tokens；吞吐最高 2.2× GPT-OSS-120B / 7.5× Qwen3.5-122B；1M ctx；开源。
- **Nemotron 3 Nano**（08-04）：30B-A3B；吞吐最高 3.3×。

> 今日核实：Nemotron 3 三档技术报告全部收录；**官方 Nemotron 3 家族正式发布报告仍待发布**（NVIDIA 尚未发布单一家族总报告）；无 8 月新报告。

---

## 11. xAI

### 11.1 Grok 4.6（今日核实：窗口外溢至本周 08-10~08-14）

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.5（SpaceXAI 旗舰） |
| **英文标题** | Introducing Grok 4.5 |
| **发布机构** | xAI（SpaceX 收购后改称 SpaceXAI） |
| **发布日期** | 2026-07-08（发布）/ 07-16（官方博文）/ Model Card 07-14 |
| **核心创新** | 与 Cursor 联合训练；DeepSWE 1.0 62.0%、SWE-bench Pro 64.7%、CursorBench v3.2 91.3% |
| **论文** | https://x.ai/news/grok-4-5 |

> ⚠️ **Grok 4.6 今日（08-10）复核**：Musk 07-28 确认 4.6 为 1.5T 参数 V9 基座（与 4.5 相同）、重点在大幅升级的 SFT + RL 后训练；**08-04 SpaceX 财报电话会承诺"下周"→ 今日 08-10 为窗口第一天（08-10~08-14）**。xAI 官方 docs.x.ai 模型目录截至今日仍仅列 grok-4.5，API release notes 无 4.6 条目；第三方 kie.ai 称 08-07 已上线与官方目录矛盾。**无官方 model card / 定价 / 基准**。观察日再度后移：07-27 "around August 7" → 08-04 "next week"。一旦官方文档更新再升级为正式条目。**Grok 4.7**（2.1T）随后数周。

---

## 12. Amazon

### 12.1 Nova 2 Sonic 2.1 架构细节（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 2 Sonic 2.1：自回归架构确认 |
| **英文标题** | Amazon Nova 2 Sonic 2.1 autoregressive architecture |
| **发布机构** | Amazon（release-notes 官方文档） |
| **模型系列** | Nova 2（Sonic / Lite / Pro；Sonic 为语音） |
| **发布日期** | Sonic 2.1 部署始于 2026-05-21、完成于 05-28；Sonic 在美东/美西/东京/斯德哥尔摩 GA |
| **核心创新** | **Sonic 2.1 为自回归 transformer 架构（无视觉编码器）**——多模态能力通过直接 token 化输入而非独立视觉编码器实现；与 Nova 2 技术报告（2025-12-02，Hybrid Reasoning + 1M ctx）口径一致 |
| **论文** | https://docs.aws.amazon.com/nova/ （release notes） |

### 12.2 Nova 战略收缩 + FMR（07-28 已收录，保留）

- 逐步弃用 Nova Premier / Omni / Reel / Canvas（Premier 9 月 EOL）；AGI Lab 解散；**Frontier Model Research (FMR)** 由 **Pieter Abbeel（Covariant）** 领导；新旗舰目标 re:Invent 2026 秋。

---

## 13. ByteDance（字节跳动）

### 13.1 Seed2.0 系列（已收录，保留）

- **Seed2.1**（2026-06-23）：agent + coding E2E；Pro 在 dev crowdsource coding 上以 59.1% 击败 Claude Opus 4.6。https://research.doubao.com/zh/blog/seed2-1-officially-released-advancing-ai-productivity
- **Seed2.0 Pro / Lite / Mini**：agent 模型系列；Lite 为字节首个 omni-modal 理解模型。
- **Seedance 2.5**（2026-07-31）：单次 30 秒视频 + 多轮延长。

> 今日核实：无 8 月新报告；Seed2.1（06-23）为最新技术报告。

---

## 14. Zhipu（智谱）

### 14.1 GLM-5.2 / GLM-5.5 传闻（今日复核，保留）

- **GLM-5.2**（2026-06-13）：MIT 开放权重；1M ctx；稀疏注意力 + IndexShare；无原生视觉。https://zhipu-ai.cn/glm-5.2
- **GLM-5**（2026-02）：~745B 总 / 44B 激活。

> ⚠️ **GLM-5.5** 截至 08-10 仍未发布：JPMorgan 研报称可能 2026-08 发布，1T+ 参数、1M ctx。单源传闻，不写入正式条目；GLM-5.2 仍为当前确认旗舰。

---

## 15. Moonshot（月之暗面）

### 15.1 Kimi K3（已收录，保留）

- **Kimi K3**（API 2026-07-16；全量权重 + 47 页技术报告 2026-07-27）：2.8T 总参 / 104B 激活；93 层 = 69 KDA + 24 Gated MLA；896 experts；AttnRes；MoonViT-V2；MXFP4/8 量化感知训练；1M ctx；首个开源 3T 级模型；~2.5× scaling efficiency vs K2；WebDev Arena #1。https://kimi.ai/k3-technical-report
- **MoonEP / FlashKDA**（07-29）：K3 全链路开源配套。

> 今日复核：**Kimi K4** 仍为训练阶段传闻（AI Weekly 07-28：寻求更多 NVIDIA Blackwell 芯片）——未发布，不入正式条目。K3 技术报告（07-27）仍为最新，权重已按期兑现（对照 Qwen3.8-Max）。

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

### 18.1 Step-3 系列（今日新增核实）

| 项目 | 内容 |
|------|------|
| **中文标题** | Step-3 / Step-3-0304 |
| **英文标题** | Step-3 / Step-3-0304 |
| **发布机构** | StepFun（阶跃星辰） |
| **模型系列** | Step 3 |
| **发布日期** | Step-3: 2026-07-31；Step-3-0304: 更早（0312 版号） |
| **架构** | Step-3: **198B 稀疏 MoE**、256K ctx、**GGUF 格式开源**；Step-3-0304: **70B 稀疏 MoE**、256K ctx、Open Source |
| **核心创新** | Step-3 为当前官网旗舰（与 Step 3.7 Flash 并列）；GGUF 开源降低部署门槛 |
| **论文** | https://github.com/stepfun-ai/Step3 |

> 今日核实：无 8 月新报告；Step-3.5 Flash（02 开源，196B/11B 激活，MTP-3）与 Step 3.7 Flash（05-29）仍为家族；Step 4 训练 2026-02 已宣布启动。

---

## 19. Yi / 01.AI

### 19.1 Yi 系列（今日复核，保留）

- **Yi-34B / Yi-6B**（2023-11）：开源旗舰。
- **Yi-Lightning**（2024-10-16）：01.AI 旗舰 MoE，Chatbot Arena #6；$0.14/M tokens；arXiv:2412.01253。
- **Yi-Coder**（2024-09）：开放权重编程模型。

> 今日核实：2026 无新旗舰或新技术报告，repo 冻结于 Yi-1.5 / Yi-9B-200K；开源节奏自 2024 年后放缓。

---

## 20. MiniMax

### 20.1 M3 / M4（今日新增核实）

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

### 20.2 MiniMax H3 开源（08-02/03 已收录，保留）

- **MiniMax H3**（API 07-31；开源权重 08-02/03）：33B dense 单流 Omni Transformer；文本/图像/视频/音频统一全模态生成；最高 15s 2K 视频；MiniMax H3 Community License（EU/UK/SK/US）。https://huggingface.co/MiniMaxAI/MiniMax-H3

---

## 交叉观察

- **"承诺制发布"进入本周集中验收（08-10~08-14）**：①**Meta Llama 4 开放权重 08-12**——Meta 07-27 经 Bloomberg 确认，405B / 多模态 / 单 H100 32 tok/s，官方技术报告待发布；②**Qwen3.8-Max 开源权重**——byteiota 08-10 确认窗口为 8 月 10 日那周，首个开源 Max 级模型，仍缺日期/license/model card；③**Grok 4.6**——Musk 08-04 "next week" 承诺本周到期，官方目录仍无记录；④**DeepSeek V4-Pro 官方版**——传闻窗口 08-10~08-20 今日开启。四大发布本周密集撞期（08-12 Llama 4 + 可能的 Grok 4.6/V4-Pro）。
- **8 月第二波"旗舰对决"成形**：Nemotron 3 家族、Kimi K3 之后，本周 Llama 4（开放权重）+ Qwen3.8-Max（开源 Max 级）+ Grok 4.6（闭源）+ 传闻 GPT-5.7/V4-Pro 构成 8 月中旬发布潮。
- **"承诺→兑现"是 2026 竞争单位的核心**：Kimi K3（按期兑现）vs Qwen3.8-Max（缺最后三项细节）vs Grok 4.6（窗口三次后移）vs Llama 4（官方定档）——开源权重的"交付信用"成为评论界衡量标准。
- **预览期拉长成为常态**：DeepSeek V4-Pro-Preview 已近 4 个月（04-24→08-10），"Preview"不再是数周过渡而是事实发布形态；Gemini 3.5 Pro 亦持续延迟。
- **Mistral 转向聚合层**：提供 Nova 2 计算、Gemini 图像理解、Claude 代码库 + 日志/影子提示合规选项——"模型经纪人"（model broker）定位，自有前沿模型开发放缓。
- **Apple 技术报告"承诺未兑现"观察持续**：AFM 3（06-08）承诺 "later this summer" 技术报告至今未出；Siri AI 已进 iOS 27 消费者 beta，闭源巨头中 Apple 仍欠一份正式报告。
- **8 月上旬密集发布窗口延续**：Llama 4（08-12）+ Qwen3.8-Max 权重（本周）+ Grok 4.6（本周）+ 传闻 GPT-5.7 / V4-Pro / Fable 5.1 / GLM-5.5 / Kimi K4——8 月中旬是 2026 迄今最密集的发布/传闻碰撞窗口。
- **传闻需谨慎（未确认不入正式条目）**：GPT-5.7/Astra（The Information + WinCentral）、Fable 5.1（07-27 泄漏）、GLM-5.5（JPMorgan 8 月）、Phi-5（仅 Inference Index 目录条目）、Grok 4.6/4.7（Musk 口头时间表）、DeepSeek V4-Pro 官方版窗口（中文媒体）、Kimi K4（Blackwell 训练传闻）、InternLM4（04-13 传闻）、MiniMax M4（H2 2026）。
