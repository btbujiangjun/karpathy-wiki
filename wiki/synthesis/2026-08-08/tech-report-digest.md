---
title: "大模型技术报告摘要（2025-2026）| LLM Tech Report Digest (2025-2026)"
type: synthesis
created: 2026-08-08
updated: 2026-08-08
sources: [tech-report-digest-2026-08-07.md]
tags: [tech-report, system-card, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, bytedance, zhipu, kimi, internlm, baichuan, stepfun, minimax]
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告 / System Card 汇总。
> 更新日期：2026-08-08（每日更新；今日重点：**Grok 4.6 观察日（昨日 08-07）已过，仍待官方确认**——第三方聚合站 kie.ai 称 08-07 已上线，但 xAI 官方模型目录 / API release notes 截至今日仍仅列 grok-4.5，且 Musk 在 08-04 SpaceX 财报电话会上又称"下周"（≈08-10~14），发布时间表与第三方上线说法相互矛盾，**无官方 model card / 定价 / 基准**；**Qwen3.8-Max 开源权重窗口今日（08-08）正式开启**——08-03 承诺"下周"（08-08~08-14），截至今日仍缺具体日期 + license + model card，评论界对比 Kimi K3 按期放权持续质疑；OpenAI **GPT-5.7 泄漏复核**（8 月发布、新 pretraining foundation ~10T tokens、GPT-6 推迟 9 月，仍无官方确认）；Apple **AFM 3 技术报告仍待发布**（"later this summer" 未兑现），本次核实五模型家族细节——IFP 1–4B 激活、Cloud Pro 跑在 Google Cloud NVIDIA GPU、与 Google 合作（TPU 训练）；Anthropic **Claude Opus 5 System Card**（07-24 已收录）+ Sonnet 5 System Card 更新至 07-10；**GLM-5.5 传闻**（JPMorgan 8 月）、**Kimi K4 Blackwell 训练传闻**；Microsoft **Phi-5 仍无官方技术报告**；StepFun / InternLM / Yi / Baichuan 等均无 8 月新报告）

---

## 1. DeepSeek（深度求索）

### 1.1 DeepSeek-V4-Flash-0731（08-04 已确认，保留）

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

### 1.2 DeepSeek-V4 基础条目（保留）

- **DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence**（2026-04-24 预览 / 04-26 技术报告）：MoE + CSA；V4-Pro（1.6T 总参 / 49B 激活），V4-Flash（284B / 13B）；32T+ tokens；1M ctx；MIT 开源；V4-Pro-Max SWE-bench Verified 80.6%（开源最高）。arXiv:2606.19348。

> 今日核实：无 8 月新报告；V4-Pro 官方在开发中，未定日期。

---

## 2. OpenAI

### 2.1 GPT-5.6 系列降价（07-30 已收录，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 价格调整公告 |
| **英文标题** | Advancing the price-performance frontier with GPT-5.6 |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（Sol 旗舰 / Terra 中档 / Luna 最快最省） |
| **发布日期** | 2026-07-30 |
| **核心创新** | 效率收益让渡给客户：Luna 降价 80%（$0.20 in / $1.20 out 每 M tokens，低于 Gemini 3.5 Flash-Lite 的 $2.80 与 Gemini 3.6 Flash 的 $9），Terra 降价 20%（$2 / $12），Sol 价格不变并新增 premium Fast mode；定价向 DeepSeek/Xiaomi/MiniMax 低价层竞争 |
| **论文** | https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/ |

> 定位解读（VentureBeat）：Luna 从 $7 降至 $1.40 综合价，直接进入低成本推理层，是 OpenAI 对"成本敏感客户 + 中国初创低价竞争"的应对。

### 2.2 GPT-5.6 System Card（已收录，保留）

- **GPT-5.6 System Card**（2026-07-09）：Preparedness 框架下三模型均 Bio/Chem High + Cyber High；Sol bio/chem 评分 4（最高）。https://deploymentsafety.openai.com/gpt-5-6

> ⚠️ 传闻更新（今日复核）：WinCentral 2026-07-30 报道 **GPT-5.7**（8 月发布，新的 pretraining foundation，约 10T tokens 规模训练，更强推理与 agent 能力），GPT-6 或推迟至 9 月；另据 The Information 报道 OpenAI 内部代号 **Astra** 的新模型家族（面向长期运行任务，已解决 10 道长期未解数学题），命名可能在 GPT-5.7 / GPT-6 之间未定。截至 08-08 仍为记者爆料，未获官方确认，不写入正式条目。

---

## 3. Meta

### 3.1 Muse Spark Safety & Preparedness Report（已收录，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | Muse Spark 安全与准备度报告 |
| **英文标题** | Muse Spark Safety & Preparedness Report |
| **发布机构** | Meta Superintelligence Labs（Meta AI） |
| **模型系列** | Muse Spark（Meta AI 底层模型） |
| **发布日期** | 2026-07（报告 PDF；Spark 1.1 2026-07-09 开放） |
| **核心创新** | 依据 Meta **Advanced AI Scaling Framework** 评估：Chem/Bio 风险 mitigation 前达 "high risk"（与 Anthropic/OpenAI 口径一致），已实施多层缓解；拒绝率 SOTA；但同行对比中 **cyber-misuse compliance 最低**；作为 Meta AI 的底层模型（underlying model）发布 |
| **论文** | arXiv:2606.12429；https://ai.meta.com/static-resource/muse-spark-safety-and-preparedness-report/ |

> 今日核实：搜索未发现 8 月新报告；无 Llama 5 新消息；Muse 系列为当前主线。

---

## 4. Google DeepMind

### 4.1 Gemini Robotics ER 2 / On-Device 2 Model Card（07-30 已收录，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini Robotics 2：全身智能（模型卡×3） |
| **英文标题** | Gemini Robotics 2 brings whole body intelligence to robots |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini Robotics 2（VLA，控制全身人形/双臂）/ ER 2（Embodied Reasoning VLM，基于 Gemini 3.5 Flash）/ On-Device 2（本地部署 VLA，基于 Gemma） |
| **发布日期** | 2026-07-30 |
| **核心创新** | Robotics 2 首个整体身体控制（feet to fingertips）+ 高级灵巧操作；ER 2 支持多机器人协作、连续视频自我监控任务进度、原生工具调用（Google Search）；On-Device 2 数小时数据适配全新机器人形态；ER 2 已在 Google AI Studio 与 Gemini Enterprise Agent Platform 提供 |
| **论文** | ER 2 Model Card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/ ；On-Device 2 Model Card: https://deepmind.google/models/model-cards/gemini-robotics-on-device-2/ |

### 4.2 Gemini 3.6 Flash Model Card（已收录，保留）

- **Gemini 3.6 Flash**（2026-07-21）：原生多模态推理；workhorse / 广泛部署；知识截止 2026-03。https://deepmind.google/models/model-cards/gemini-3-6-flash/
- **Gemini 3.5 Flash-Lite**（2026-07-21）：低成本层，现综合价格 $2.80/M（已被 OpenAI Luna 新价 $1.40/M 超越）。

> 今日核实：官方最新模型卡仍为 Gemini 3.6 Flash / 3.5 Flash-Lite（07-21）；Gemini 3.5 Flash Model Card（05-19）为更早条目；Gemini 4 预训练已启动（Gemini family update 2026-07）；Gemini 3.5 Pro 仍延迟未发布；8 月无新卡。

---

## 5. Anthropic

### 5.1 Claude Opus 5 System Card（08-04 已收录，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 5 系统卡 |
| **英文标题** | Claude Opus 5 System Card |
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 5（Opus 4.8 升级） |
| **发布日期** | System Card PDF: 2026-07-24 |
| **核心创新** | agentic coding、computer use、long-horizon knowledge work、math/science reasoning；effort dial 可调（$5/$25 每 M in/out）；SWE-bench Verified 96.0、SWE-bench Pro 79.2、Frontier-Bench v0.1 43.3（xhigh 下 44.4%）、ARC-AGI-3 30.2 |
| **论文** | PDF: https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude%20Opus%205%20System%20Card.pdf |

### 5.2 Claude Sonnet 5 / Fable 5（保留）

- **Claude Sonnet 5**（2026-06-30）：1M ctx / 128K 输出；MASK 诚实性说谎率 3.1%（对比集最低）。
- **Claude Fable 5 & Mythos 5**（2026-06-09）：Fable 5 为闭源能力前沿（SWE-bench 95.5%）。

> 今日核实：无 8 月新报告；最新官方 System Card 为 Claude Opus 5（07-24）；Sonnet 5 System Card 在 Anthropic 文档站已更新至 2026-07-10 版本。

---

## 6. Mistral

### 6.1 Shieldstral（08-05 已收录；保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | Shieldstral：多模态安全分类器 |
| **英文标题** | Shieldstral |
| **发布机构** | Mistral AI |
| **模型系列** | Shieldstral（3B 开源） |
| **发布日期** | 2026-08-04（公告）/ 技术报告 arXiv 2026-07-28 |
| **架构** | 3B 多模态安全分类模型 |
| **核心创新** | policy-adaptive QA（自适应政策评估）；Apache-2.0 开源；支持 12 种语言；单张 16GB GPU 可跑；性能匹配体量 7× 于它的模型；Mistral 加入 **Open Secure AI Alliance**（与 NVIDIA） |
| **论文** | arXiv（Shieldstral，2026-07-28） |

### 6.2 其他 Mistral 条目（保留）

- **Mistral Medium 3**（2026-08-02）：128K，coding/reasoning 中档；la Plateforme + Azure Foundry（`mistral-medium-2505`）。
- **Leanstral 1.5**（2026-07-02）：119B 总 / 6B 激活稀疏 MoE，Apache-2.0；miniF2F 100%。
- **Robostral Navigate**（2026-07-08）：具身导航模型。

> 今日核实：无 8 月新报告。

---

## 7. Qwen（通义千问）

### 7.1 Qwen3.8-Max（08-04 已收录；今日开源窗口正式开启）

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.8-Max |
| **英文标题** | Qwen3.8-Max |
| **发布机构** | Alibaba Qwen |
| **模型系列** | Qwen3.8（Max 旗舰） |
| **发布日期** | 2026-08-03（博客 qwen.ai/blog?id=qwen3.8 ；阿里云官方博客 "Qwen3.8-Max: A New Bar for Coding and Cowork"） |
| **架构** | 2.4T 总参 / 95B 激活 Sparse MoE + hybrid attention |
| **上下文长度** | 1M |
| **核心创新** | 原生视觉多模态基础模型（native vision）；Text Arena #5、Vision Arena #2；**定价 $2 in / $6 out / $0.25 cached per 1M tokens**；权重"下周"开源（与 Qwen3.8-27B 同行开源）；Alibaba Cloud Model Studio + QwenWork（职场 AI agent 平台，公测）；激活参数数与 license 尚未披露；发布当日阿里港股 +7% |
| **论文** | https://qwen.ai/blog?id=qwen3.8 ；https://www.alibabacloud.com/press-room/alibaba-unveils-qwen3-8-max |

> 今日状态（开源窗口正式开启）：08-03 承诺"下周"开源 → 按约定 **08-08 即窗口第一天**，截止 08-08~08-14 窗口内截至搜索时仍未放权——HF/ModelScope 无新权重条目，缺具体日期 + license + model card。对照 Moonshot Kimi K3 的明确权重日期（07-27 已兑现），Qwen 缺最后三项细节受评论界持续质疑。**08-08~08-14 为权重观察窗口（今日起）**。

### 7.2 其他 Qwen 条目（保留）

- **Qwen3.7-Flash**（2026-07-25）：Flash 系列原生视觉语言升级。
- **Qwen-Audio-3.0-ASR-Flash**（2026-07-30）：30 语言 + 中文七大方言 ASR 家族。
- **Qwen-UI-Agent Technical Report**（2026-07）：GUI 代理技术报告。arXiv:2607.28227。

---

## 8. Microsoft（Phi）

### 8.1 Phi-4-reasoning-vision-15B Technical Report（已收录，保留）

- **Phi-4-reasoning-vision-15B**（2026-03，MSR-TR-2026-10）：数据质量为最大性能杠杆；高分辨率动态分辨率视觉编码器；单一模型双模式（推理/非推理 mode token）。https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/

> ⚠️ 传闻更新（今日核实）：**Phi-5** 截至 08-08 仍无官方技术报告——唯一新增为 Inference Index 目录条目（2026-01-08，128K ctx，小模型 champion）；此前的 16B / MMLU 86.7% 报道为 single-source（GogoAI），官方 MSR 页面仍以 Phi-4-reasoning-vision-15B 为最新技术报告，**未确认，不写入正式条目**。

---

## 9. Apple

### 9.1 AFM 3（已收录；今日新增核实五模型家族细节）

| 项目 | 内容 |
|------|------|
| **中文标题** | 第三代 Apple Foundation Models（AFM 3） |
| **英文标题** | Introducing the Third Generation of Apple's Foundation Models |
| **发布机构** | Apple（与 Google 合作定制，训练于 Google Cloud TPU） |
| **模型系列** | AFM 3 Core（3B 端侧 dense）/ Core Advanced（20B 端侧稀疏，IFP 激活 1–4B）/ AFM 3 Cloud（PCC）/ ADM 3 Cloud（图像生成/编辑）/ AFM 3 Cloud Pro（PCC on Google Cloud NVIDIA GPU，agentic tool use + 复杂推理） |
| **发布日期** | 2026-06-08（WWDC26） |
| **核心创新** | IFP（Instruction-Following Pruning）把全模型放 flash、按 prompt 一次路由加载 1–4B 专家权重 + always-active shared experts；AFM 3 Cloud Pro 首次把 PCC 扩展到 Google Cloud NVIDIA GPU（NVIDIA Confidential Computing + Intel TDX + Google Titan，密钥仍归 Apple）；Siri 表达语音 MOS 4.15 / 会话文本 4.24 |
| **论文** | https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models |

> 今日核实：TechCrunch 2026-08-03（"Apple finally fixed Siri"）——**Siri AI 已进入 iOS 27 消费者测试版**（beta，2026-07 起）；Apple Foundation Models 训练借助 **Google Gemini/TPU 合作**（与 AFM 3 发布的"与 Google 合作定制"一致）；**AFM 3 正式技术报告仍待发布**——Apple 承诺 "later this summer"（约同 2025 年 7 月技术报告节奏），截至 08-08 尚未兑现，为"承诺未兑现"观察项。

---

## 10. NVIDIA

### 10.1 Nemotron 3 Super Technical Report（08-05 已收录，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | NVIDIA Nemotron 3 Super 技术报告 |
| **英文标题** | NVIDIA Nemotron 3 Super Technical Report |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 家族（Nano 30B-A3B · **Super 120B/12B** · Ultra 550B/55B） |
| **发布日期** | 技术报告 PDF（2026-04-03） |
| **架构** | MoE + **混合 Mamba-Attention**（Hybrid Mamba-Attention MoE）；**LatentMoE**（latent 维度路由）+ MTP（Multi-Token Prediction）投机解码层 |
| **训练数据** | 25T tokens；**NVFP4 量化感知预训练**（自始即低精度） |
| **上下文长度** | 1M |
| **核心创新** | 吞吐最高达 GPT-OSS-120B 的 **2.2×**、Qwen3.5-122B 的 **7.5×**；首次将 LatentMoE + NVFP4 预训练用于 120B 级模型；权重开源 |
| **论文** | PDF: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf |

### 10.2 Nemotron 3 Ultra Technical Report（08-02/03 已收录；保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | NVIDIA Nemotron 3 Ultra 技术报告 |
| **英文标题** | NVIDIA Nemotron 3 Ultra Technical Report |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 Ultra（550B 总参 / 55B 激活） |
| **发布日期** | 技术报告 PDF（2026-06-09） |
| **架构** | MoE **混合 Mamba-Attention**（Mamba-2 + Attention）+ **LatentMoE** + MTP 投机解码层 |
| **训练数据** | 20T tokens；**NVFP4 量化感知预训练** |
| **上下文长度** | 1M |
| **核心创新** | 多环境 RLVR（MOPD）；推理预算控制（reasoning budget）；~6× 更高推理吞吐；权重开源 |
| **论文** | PDF: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf |

> Nemotron 3 三档（Nano 08-04 / Super 08-05 / Ultra 08-02-03）技术报告现已全部收录，构成完整家族：混合 Mamba-Attention + LatentMoE + NVFP4 预训练 + 1M ctx + 开源。今日复核：无 8 月新报告。

---

## 11. xAI

### 11.1 Grok 4.5（已收录；今日核实 4.6 观察日已过）

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.5（SpaceXAI 旗舰） |
| **英文标题** | Introducing Grok 4.5 |
| **发布机构** | xAI（SpaceX 收购后改称 SpaceXAI；2026-06 收购 Cursor） |
| **发布日期** | 2026-07-08（发布）/ 07-16（官方博文）/ Model Card 07-14 |
| **上下文长度** | 500K；$2/$6 每 M tokens |
| **核心创新** | 与 Cursor 联合训练；DeepSWE 1.0 62.0%、SWE-bench Pro 64.7%、CursorBench v3.2 91.3%；Model Card 覆盖 cyber/bio/jailbreak/CBRN/mental-health 等安全面 |
| **论文** | https://x.ai/news/grok-4-5 ；Model Card PDF: https://media.x.ai/v1/website/card-7f81d41b.pdf |

> ⚠️ **Grok 4.6 观察日（08-07）已过，仍待官方确认**：Musk（2026-07-28）确认 **Grok 4.6** 为 1.5T 参数 V9 基座（与 4.5 相同）、重点在**大幅升级的 SFT + RL 后训练**而非新架构；性能目标直指 Kimi K3 与 Claude Opus 4.8；保持 4.5 的吞吐与 token 效率（~80 tps）。**Grok 4.7**（2.1T）随后数周发布。今日（08-08）状态核实：
> - 第三方基准聚合站 kie.ai 的 Grok 4.6 页面仍称 **2026-08-07 已上线**（xAI API / Grok app / grok.com / SuperGrok / X Premium+ / 第三方渠道）；
> - 但 **xAI 官方 docs.x.ai 模型目录截至今日仍仅列 grok-4.5**（$2/$6，500K ctx，知识截止 2026-02-01），API release notes 无 grok-4.6 条目；
> - 时间表矛盾：Musk 07-27 称"around August 7"、07-28 称 1.5T/2.1T，但 **08-04 SpaceX 财报电话会称"next week"（≈08-10~14）**——发布时间表实际后移；
> - **无官方 model card、定价、上下文、基准**；Arena 独立得分预期在正式上线后一周。
> → 结论：**观察日已过但官方仍未确认**，所有性能数字均为第三方传闻；一旦官方文档更新再升级为正式条目。

---

## 12. Amazon

### 12.1 Nova 系列收缩 + Frontier Model Research（07-28 已收录，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon 调整 AI 战略：Nova 收缩，Frontier Model Research (FMR) 成立 |
| **英文标题** | Amazon overhauls AI strategy; Pieter Abbeel leads new FMR |
| **发布机构** | Amazon（报道：Business Insider 2026-07-28） |
| **核心创新** | 逐步弃用 **Nova Premier / Omni / Reel / Canvas**（Nova Premier 9 月 EOL；Nova 2 Lite / Sonic 保留）；AGI Lab 解散；新前沿项目 **Frontier Model Research (FMR)** 由 **Pieter Abbeel（Covariant）** 领导；新旗舰目标 re:Invent 2026 秋发布 |
| **论文** | https://www.businessinsider.com/amazon-nova-premier-omni-reel-canvas-fmr-2026-7 |

> ⚠️ 与 08-03/08-04 收录的 **Amazon Nova 2 技术报告**（2025-12-02）形成对比：Nova 2 架构本身仍有效，但产品线组合正被重新洗牌（多模态生成模型 Omni/Reel/Canvas 被砍，保留 2.0 Lite/Sonic 推理与语音）。此为战略收缩而非架构否定。

### 12.2 Amazon Nova 2（已收录，保留）

- **Amazon Nova 2: Multimodal Reasoning and Generation Models**（2025-12-02）：Hybrid Reasoning（low/medium/high effort）；1M ctx；Lite τ²-bench 76.0、Pro 92.7。PDF: https://cdn.amazon.science/c5/3d/84514a224666b5be6de4b43ef4aa/nova-2-0-technical-report2.pdf

---

## 13. ByteDance（字节跳动）

### 13.1 Seed2.0 系列（已收录，保留）

- **Seed2.0 Pro / Lite / Mini**：agent 模型系列；**Lite 于 2026-04 底升级为字节首个 omni-modal 理解模型**（视频/图像/音频/文本四模态统一理解）；**BabyVision** 评测 SOTA（多模态）。
- **Seed2.1**（2026-06-23）：agent + coding E2E；Pro 在 dev crowdsource coding 上以 59.1% 击败 Claude Opus 4.6。https://research.doubao.com/zh/blog/seed2-1-officially-released-advancing-ai-productivity
- **Seedance 2.5**（2026-07-31）：单次 30 秒视频 + 多轮延长；统一多模态音视频联合生成。
- **Seedream 5.0 Pro** / **Seed Audio 1.0** / **Seed3D 2.0**。

> 今日核实：无 8 月新报告；Seed2.1（06-23）为最新技术报告。

---

## 14. Zhipu（智谱）

### 14.1 GLM-5.2（已收录；GLM-5.5 传闻仍待确认）

- **GLM-5.2**（2026-06-13）：MIT 开放权重；1M ctx；稀疏注意力 + IndexShare；无原生视觉。https://zhipu-ai.cn/glm-5.2
- **GLM-5**（2026-02）：~745B 总 / 44B 激活。

> ⚠️ **GLM-5.5** 截至 08-08 仍未发布：JPMorgan 研报（Reuters/CGTN 转载）称可能 2026-08 发布，1T+ 参数（基于 GLM-5.2 744B 升级）、1M ctx。单源传闻，不写入正式条目；GLM-5.2 仍为当前确认旗舰。

---

## 15. Moonshot（月之暗面）

### 15.1 Kimi K3（已收录，保留）

- **Kimi K3**（API 2026-07-16；全量权重 + 47 页技术报告 2026-07-27）：2.8T 总参 / 104B 激活；93 层 = 69 KDA + 24 Gated MLA；896 experts（16 selected + 2 shared）；AttnRes；MoonViT-V2；MXFP4/8 量化感知训练；1M ctx；首个开源 3T 级模型；~2.5× scaling efficiency vs K2；WebDev Arena #1；Kimi K3 License。https://kimi.ai/k3-technical-report
- **MoonEP** / **FlashKDA**（2026-07-29）：K3 全链路开源配套。

> 今日复核：**Kimi K4** 仍为训练阶段传闻（AI Weekly 07-28：Moonshot 寻求更多 NVIDIA Blackwell 芯片）——未发布，不入正式条目。K3 技术报告（07-27）仍为最新；K3 权重已按承诺日期发布（对照 Qwen3.8-Max 的"下周"）。

---

## 16. InternLM（上海 AI 实验室）

### 16.1 Intern-S2-Preview 系列（08-05 已确认，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | Intern-S2-Preview（35B）/ Intern-S2-Preview-397B：科学多模态基础模型 |
| **英文标题** | Intern-S2-Preview / Intern-S2-Preview-397B |
| **发布机构** | Shanghai AI Laboratory（InternLM） |
| **模型系列** | Intern-S1 → Intern-S1-Pro → **Intern-S2-Preview** |
| **发布日期** | 35B: 2026-07-17（HF）；397B: 2026-07-18（The Neural Feed 报道，GitHub README 同期） |
| **架构** | 35B（从 Qwen3.5 续训，dense）；397B（MoE，~120B 激活/约 30%） |
| **核心创新** | 引入 **task scaling**：提升科学任务难度/多样性/覆盖度而非仅扩参数；35B 版在多个核心专业科学任务上媲美万亿级 Intern-S1-Pro；397B 版沿三个维度扩展（预训练、RL task coverage、interactive agent environments）；均 Apache-2.0，BF16 + FP8 双格式，HF + ModelScope |
| **论文** | 35B: https://huggingface.co/internlm/Intern-S2-Preview ；397B: https://huggingface.co/internlm/Intern-S2-Preview-397B ；S1 arXiv:2508.15763、S1-Pro arXiv:2603.25040 |

> 今日复核：无 8 月新报告；S1-Pro 为 1T 级科学多模态（arXiv:2603.25040，group routing + 6T tokens 科学数据续训，AIME-2025 93.1 / MMLU-Pro 86.6），S2-Preview 为当前最新发布。

---

## 17. Baichuan（百川智能）

### 17.1 Baichuan-M4（已收录，保留）

- **Baichuan-M4**（2026-05-26 发布 / 06-22 与清华正式发布）：临床级医疗 Agent 系统；**HealthBench 68.6 世界第一**（超 GPT-5.5 10+ 分）；hallucination 3.3%；事实性感知 RL；1000+ 原子化临床路径；AI 家庭医生"百小医"。arXiv:2606.08982。
- **Baichuan-M3**（2026-01）：235B；HealthBench 65.1；hallucination 3.5%。arXiv:2602.06570。

> 今日核实：无 2026 年 8 月新报告；公司战略全面转向医疗垂直领域。

---

## 18. StepFun（阶跃星辰）

### 18.1 Step 3.7 / 3.5 Flash（已收录；今日核实无 8 月新报告）

- **Step 3.7 Flash**（当前旗舰，官网现列；2026-05-29 发布）：198B 总 / 11B 激活稀疏 MoE；原生多模态；256K ctx；low/medium/high 三级 reasoning level。
- **Step 3.5 Flash**（2026-02 开源）：196B 总 / 11B 激活；MTP-3；SWA + Full Attention 混合；256K。
- **Step 4**：训练已于 2026-02 宣布启动。
- **Step3-Sys Technical Report**：https://github.com/stepfun-ai/Step3

> 今日核实：官网/平台最新仍为 Step 3.7 Flash（05-29），无 8 月新报告；Step-DeepResearch（12/25 技术报告）仍为 agent 侧最新。

---

## 19. Yi / 01.AI

### 19.1 Yi-Lightning（已收录，保留）

- **Yi-Lightning**（2024-10-16）：01.AI 旗舰 MoE，Chatbot Arena #6；$0.14/M tokens；arXiv:2412.01253。

> 今日核实：2026 无新旗舰或新技术报告，repo 冻结于 Yi-1.5 / Yi-9B-200K。

---

## 20. MiniMax

### 20.1 MiniMax H3 开源（08-02/03 已收录，保留）

| 项目 | 内容 |
|------|------|
| **中文标题** | MiniMax H3：全模态生成模型（开源权重） |
| **英文标题** | MiniMax H3 Is Now Open Source |
| **发布机构** | MiniMax |
| **模型系列** | H3（H 系列 omni-modal） |
| **发布日期** | API 2026-07-31；**开源权重 2026-08-02/03** |
| **架构** | 33B 总参 **dense** 单流 Omni Transformer（H3-Omni-Transformer），其中约 13B 位于 AdaLN 相关分支（可预计算缓存，推理部署时无需加载）；Qwen3-VL-32B 文本编码器；Visual VAE + 独立 Audio VAE |
| **核心创新** | 文本/图像/视频/音频统一全模态生成（omni-modal generation）；原生 dual-channel audio-visual 输出；最高 15s 2K 视频；发布 2 个任务专用 checkpoint（FL2VA / Ref2VA，CFG-distilled）；SGLang / vLLM / diffusers 支持；**MiniMax H3 Community License**（可用区域：EU / UK / South Korea / US，其他地区"not yet, not not ever"可申请） |
| **论文** | https://huggingface.co/MiniMaxAI/MiniMax-H3 ；https://www.minimax.io/news/minimax-h3-open-source |

> 区域限定许可证为开源视频生成模型树立新范式——API 全球可用、权重按地区合规状态逐步放开（EU AI Act 已生效、美国涉生成式视频版权诉讼进行中）。

---

## 交叉观察

- **"承诺制发布"进入验收窗口**：①**Grok 4.6**——08-07 观察日已过，kie.ai 称已上线但 xAI 官方目录无记录，且 Musk 08-04 财报电话会把时间表后移至"下周"（08-10~14）→ 状态为"窗口外溢，官方未确认"；②**Qwen3.8-Max 开源**——08-08 起进入 08-03 承诺的"下周"权重窗口，仍缺日期/license/model card，对照 Kimi K3 按期放权持续被质疑。两个承诺均在今日进入验收期。
- **8 月上旬密集发布窗口延续**：Grok 4.6（窗口外溢）+ 传闻中 GPT-5.7（8 月）+ Qwen3.8-Max 开源——若兑现，将与 Nemotron 3 家族、Kimi K3 构成 8 月第二波"旗舰对决"。
- **Nemotron 3 家族技术报告齐备**：Nano/Super/Ultra 三档（30B/120B/550B，激活 3B/12B/55B）全部采用混合 Mamba-Attention + LatentMoE + NVFP4 预训练 + 1M ctx + 开源——NVIDIA 以完整技术栈对抗开源 2T 级阵营（K3/Qwen3.8-Max）。
- **定价战进入 2T+ 开源旗舰层**：OpenAI Luna 综合价 $1.40/M 下探至低成本层，直逼 DeepSeek V4-Flash（$0.14/$0.28）与 Xiaomi MiMo；Qwen3.8-Max API $2/$6 定价（激活参数未披露）——"质量-价格双曲线"成为发布标配。
- **Apple 技术报告"承诺未兑现"观察**：AFM 3（06-08 发布）承诺 "later this summer" 的技术报告至今未出（2025 年 AFM 2 技术报告 7 月发布）；Siri AI 已进 iOS 27 消费者 beta，但与公开报告的滞后形成对比——闭源巨头中 Apple 是唯一仍欠一份正式技术报告的。
- **Amazon 战略收缩 vs 前沿加码**：Nova 生成模型线（Omni/Reel/Canvas）被砍、AGI Lab 解散，Pieter Abbeel 领衔 FMR 冲刺 re:Invent 2026 旗舰——与 OpenAI/Meta/Anthropic 的"前端模型集中投入"同频。
- **机器人成为 System Card 新品类**：Gemini Robotics 2 / ER 2 / On-Device 2 三张模型卡 + Mistral Robostral，机器人基础模型安全评估（embodiment safety）开始规范化。
- **开放权重 = 新的竞争单位**：MiniMax H3（区域限 License）、Kimi K3（明确日期）、DeepSeek V4-Flash-0731（MIT）、Intern-S2 系列（Apache-2.0）、Nemotron 3（开源）——开源不再只是生态策略，而是前沿扩散的主通道；Qwen3.8-Max 的"下周"因缺 license/日期而受评论界质疑。
- **Agentic 基准仍是发布主战场**：GPT-5.6 降价服务于高吞吐多步工作流；Claude Opus 5 / Grok 4.5 / DeepSeek-V4-Flash 均以 agent/coding 为头条。
- **安全报告标配化继续，且开始互相参照**：Meta Muse Spark 的 Advanced AI Scaling Framework（Chem/Bio high risk 缓解前）与 Anthropic/OpenAI Preparedness 口径趋同；Mistral 加入 Open Secure AI Alliance——安全评估成为行业共同语言。
- **传闻需谨慎（未确认不入正式条目）**：GPT-5.7/Astra（The Information + WinCentral）、GLM-5.5（JPMorgan 8 月）、Phi-5（仅 Inference Index 目录条目）、Grok 4.6/4.7（Musk 口头时间表后移，kie.ai 称 08-07 上线但官方未确认）、Kimi K4（Blackwell 训练传闻）。
