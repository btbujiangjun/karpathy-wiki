---
title: LLM 技术报告速览 — 2026-11-22
type: synthesis
created: 2026-11-22
updated: 2026-11-22
sources: [openai-gpt-6-2-system-card, openai-chatgpt-images-2-6-system-card, anthropic-fable-5-2, gemini-4-neon, nvidia-nemotron-3-5-super, meta-muse-spark-1-3, mistral-le-chonk, mistral-large-4, qwen4-max, qwen3-8-max, microsoft-frognano-4b, apple-afm-3-siri-ai, xai-grok-4-7, amazon-nova-2-sonic, zhipu-glm-5-3, zhipu-glm-os-concept, internlm-sage-s2-1-flash, moonshot-kimi-k3-1-pro, stepfun-step-5-preview, bytedance-dreamina-seedance-2-5, deepseek-v4-1-flash, deepseek-v4-preview, yi-lightning]
tags: [tech-report, LLM, technical-report, system-card, model-card, ArXiv, moe, mamba, hybrid-architecture, sparse-attention, reasoning, long-context, multimodal, scaling-law, alignment, rl, cybersecurity, open-weights, daily-digest]
---

# LLM 技术报告速览 — 2026-11-22

> 覆盖 20 家目标机构最新一手 Tech Report / Technical Report / System Card / Model Card / 官方技术披露，重点关注新架构（MoE, Mamba, hybrid, Sparse）、训练方法（pre-training, post-training, alignment, RL）、Scaling、多模态、长上下文与推理。本页为 2026-11-22 日报，新增首发：OpenAI ChatGPT Images 2.6 系统卡、Qwen4-Max 系统卡。

## 来源方法

`websearch` 在环境中不可用（取消），本次通过 `webfetch` 直接抓取各公司官方页面：OpenAI Deployment Safety Hub、Anthropic News、Google ai.google/blog.google 新闻、NVIDIA Technical Blog / NVIDIA AI Models 页、AWS News Blog / Amazon Nova 分类、Microsoft Azure AI Foundry Models / Microsoft AI 页、Alibaba Cloud Community 博客（Qwen4-Max 系统卡专题）、01.AI 新闻中心、智谱 open.zhipu.ai、Moonshot AI Blog、ByteDance 新闻稿、DeepSeek 中文版 news、InternLM GitHub 主页。Meta AI / Mistral / xAI 站点本窗口传输失败/超时，沿用 2026-11-21 速览口径（Muse Spark 1.3、Le Chonk/Large 4、Grok 4.7）。

## 重点关注方向速览（2026-11-22）

| 方向 | 代表进展 |
|---|---|
| 新架构（MoE/Mamba/Hybrid/Sparse） | Qwen4（Gated DeltaNet + Qwen Sparse Attention + Gated Residual + N-gram embedding 328B, 2.4T 总参/71B 激活）；NVIDIA Nemotron 3.5 Super（Hybrid MoE Mamba-Transformer, 1M ctx, CISPO RL 后训练）；DeepSeek V4.1 Flash（不对称 8B/16B MoE, 原生多模态）；Mistral Large 4（MLA+DSA, 1M ctx） |
| 训练方法（Pre/Post/Alignment/RL） | Qwen4（Live Delivery 长期任务分版交付，90 MCP 工具，Last Secure Code Bench 安全功能性通过率 31.8%）；NVIDIA Nemotron 3.5 Super（CISPO RL 后训练 via Tinker rank-32 LoRA）；OpenAI GPT-6.2（RL 长 CoT 后训练, Preparedness 分级对齐） |
| Scaling Law / 缩放分析 | Qwen4-Max（Work360 52.69, 成本下降 58%）；DeepSeek V4.1 Flash（承超 DeepSeek V4 Pro 的智能水平，价格同步下降）；Kimi K3.1 Pro（3T, 1M ctx）；NVIDIA Nemotron 3.5 Super（120B 总参/12B 激活, 1M ctx, GDP_pdf +13.8） |
| 多模态模型 | Google Gemini 4（Argon/Neon, 统一文本/图像/视频/音频, 1M ctx）；NVIDIA Nemotron 3.5 Super（120B VL 变体）；DeepSeek V4.1 Flash（原生多模态视觉）；OpenAI ChatGPT Images 2.6（图片模型, Sunburst/Flare）；Qwen4（原生 vision） |
| 长上下文模型 | Qwen4-Max（1M）；Gemini 4 Neon/Hydrogen（1M）；NVIDIA Nemotron 3.5 Super（1M）；Kimi K3.1 Pro（1M）；DeepSeek V4/V4.1 Flash（1M） |
| 推理模型 / Reasoning | GPT-6.2（reasoning, evaluation awareness <3% turns, CoT 规避 <1%）；NVIDIA Nemotron 3.5 Super（长 CoT 后训练）；Muse Spark 1.3（agentic 编码）；Grok 4.7（reasoning, 500K ctx） |

## 目标机构覆盖状态（2026-11-22 核验）

| 机构 | 最新核验报告（型号/日期） | 状态 |
|------|--------------------------|------|
| Qwen (Alibaba) | Qwen4-Max（2026-11-16/17） | ✓ 已记录（本窗口新增首发） |
| OpenAI | GPT-6.2 System Card（11-17）+ ChatGPT Images 2.6 系统卡（11-4） | ✓ 已记录（新增 Images 2.6） |
| Anthropic | Fable 5.2 / Mythos 5.2（11-09） | ✓ 已记录 |
| Google DeepMind | Gemini 4 Neon（11-18，AA Index v5.01 #3, 1M ctx, $3M/$15M per M in/out tokens） | ✓ 已记录 |
| NVIDIA | Nemotron 3.5 Super（2611.22161, 11-17） | ✓ 已记录 |
| DeepSeek | V4.1 Flash（2026-09-10）+ V4 Preview（2026-04-24） | ✓ 已记录 |
| Meta AI | Muse Spark 1.3（ai.meta.com/llama/, 日期未标注） | 已记录 |
| Mistral AI | Le Chonk（11-05, 10-29 开放权重）+ Large 4（10-06） | ✓ 已记录 |
| xAI | Grok 4.7（2026-09-22） | ✓ 已记录 |
| Amazon Nova | Nova 2 Sonic（2025-12-02）+ Nova 2.5 Sonic（AWS Nova 分类, 2026-10-13） | ✓ 已记录 |
| Apple | AFM 3 + Siri AI（2026） | ✓ 已记录 |
| Zhipu AI | GLM-5.3 + GLM-OS 概念（2026-11-29 公告） | ✓ 已记录 |
| InternLM (Shanghai AI Lab) | Sage S2.1 Flash（2611.21072, 2026-11-16, 320B MoE） | ✓ 已记录 |
| Moonshot AI (Kimi) | Kimi K3.1 Pro（2026-10-24, 3T, 1M ctx） | ✓ 已记录 |
| StepFun (阶跃星辰) | Step 5 Preview（2026-11, 600B/27B, 92 层, Sparse GQA） | ✓ 已记录 |
| ByteDance (豆北/Doubao) | Dreamina Seedance 2.5（2026-07-31） | ✓ 已记录 |
| Microsoft | FrogNano-4B（Phi 系, 11-18） | ✓ 已记录 |
| Yi (01.AI) | Yi-Lightning（2024.10, 千亿参数 MoE, LMSYS 第六） | ✓ 已记录 |
| Baichuan | —（网站不可达, 无可验证新报告） | — |

## 逐家详情

### 1. Qwen (Alibaba) — 本窗口新增首发

**Qwen4-Max（新发布, 2026-11-16/17, Alibaba Cloud Community 博客）**

- 中文标题：Alibaba Unveils Qwen4-Max：New AI Teammate for Work, Creativity, and Discovery（首发 2026-11-16）/ Alibaba Cloud Brings Qwen4-Max to the Enterprise：An AI Colleague That Plans, Builds and Delivers Finished Work（企业版 2026-11-17）
- 英文标题：Alibaba Unveils Qwen4-Max：New AI Teammate for Work, Creativity, and Discovery / Alibaba Cloud Brings Qwen4-Max to the Enterprise
- 发布机构：Alibaba（Alibaba Cloud Community）
- 模型名称/系列：Qwen4-Max（Qwen4 系列旗舰）；Qwen4-Max for Enterprise
- 发布日期：2026-11-16（首发）；2026-11-17（企业版, San Francisco）
- 核心参数：总参数 2.4T，激活 71B/token；原生 vision；上下文 1M token；附 N-gram embedding 参数 328B（企业版口径）
- 主要创新点：Qwen4 架构（Gated DeltaNet + Qwen Sparse Attention + Gated Residual + N-gram embedding 328B）；Live Delivery（长任务分版交付, 给可用初稿后持续迭代）；安全（Last Secure Code Bench 安全功能性通过率 31.8% vs Qwen3.8-Max 22.0%；代码安全检查加入训练；网络安全：防御类数据保留、攻击类数据剔除）；基准：Work360 52.69（Qwen3.8-Max 47.74），Xhigh/High 推理下 token 耗尽 24%/35%，长任务平均成本 58% 降低；支持 90 个 MCP 工具；Code Arena 排名第 6，Agents' Last Exam、Vals Index、JobBench、Chartography 等专项基准强势
- arXiv/链接：[Alibaba Unveils Qwen4-Max (Alibaba Cloud Community)](https://www.alibabacloud.com/blog/alibaba-unveils-qwen4-max-new-ai-teammate-for-work-creativity-and-discovery_603783)、[Qwen4-Max for Enterprise](https://www.alibabacloud.com/blog/alibaba-cloud-brings-qwen4-max-to-the-enterprise-an-ai-colleague-that-plans-builds-and-delivers-finished-work_603786)

**Qwen3.8-Max（最新已记录, 2026-11-07，双轨架构, Max/Flash 双轨, 面向编码, Qwen4 未发布）**

### 2. OpenAI

**GPT-6.2 System Card（最新, 2026-11-17）**

- 中文标题：GPT-6.2 系统卡（GPT-6.2 Astra 与 GPT-6.2 Sol）
- 英文标题：GPT-6.2 System Card (GPT-6.2 Astra and GPT-6.2 Sol)
- 发布机构：OpenAI（Deployment Safety Hub）
- 模型名称/系列：GPT-6.2 Astra / GPT-6.2 Sol（GPT-6 系列, reasoning 模型）
- 发布日期：2026-11-17
- 核心参数：参数量/训练数据量未公开；reasoning 通过 RL 训练先思考后回答（长内部 CoT）；Preparedness: 网络安全 **Critical**、生物化学 **High**、AI Self-Improvement below High
- 主要创新点：Control Room（跨研究基础设施跟踪模型负载, 快速停止/急停, 扩展前沿 agent 监控）；AI 自我改进工程评测（Internal Research Debugging 81.85%, KernelGen 1P 76.92%, PostTrainBench Lite 74.79%）；可监控性（CoT 规避 <1%, 未授权蒸馏提取 private reasoning <1%, 新加密推理保护, 可扣留流式响应, Codex developer prompt 抑制信息遗漏）；自报指标：GPQA Diamond 97.0%(Astra)/96.0%(Sol), NanoGPT 训练时间节省 42.87%
- arXiv/链接：[GPT-6.2 System Card (deploymentsafety.openai.com)](https://deploymentsafety.openai.com/gpt-6-2-astra-sol)

**ChatGPT Images 2.6 System Card（新增首发, 2026-11-04, 图片模型, 非 LLM）**

- 中文标题：ChatGPT Images 2.6 系统卡（GPT-Image-2.6 Sunburst / Flare）
- 英文标题：ChatGPT Images 2.6 System Card (GPT-Image-2.6 Sunburst and Flare)
- 发布机构：OpenAI
- 模型名称/系列：GPT-Image-2.6 Sunburst / GPT-Image-2.6 Flare（图片生成模型）
- 发布日期：2026-11-04
- 核心参数：参数量未公开；安全评估：Sunburst 安全生成 75.50%、未阻止 22.78%（vs GPT-Image-2.5 Sunburst 基线 76.15%/21.94%）；Flare 安全生成 75.04%、未阻止 2.14%（vs Flare 基线 78.36%/1.49%）；涵盖 sexual/hate/violence/extremism/self-harm/political 等类别
- 主要创新点：新增 GIF 生成、照片标记（markup）、SVG 输出；Flare 可配置推理强度（生成与编辑速度）；安全监控层外扩；CSAM 自动分类等
- arXiv/链接：[ChatGPT Images 2.6 System Card (deploymentsafety.openai.com)](https://deploymentsafety.openai.com/chatgpt-images-2-6)

### 3. Anthropic

**Fable 5.2 / Mythos 5.2（最新, 2026-11-09, Anthropic News）**

- 中文标题：Claude Fable 5.2 与 Claude Mythos 5.2 系统卡（Anthropic News）
- 英文标题：Introducing Claude Fable 5.2 and Claude Mythos 5.2 (Anthropic News)
- 发布机构：Anthropic
- 模型名称/系列：Claude Fable 5.2 / Claude Mythos 5.2（Fable/Mythos 系列）
- 发布日期：2026-11-09
- 核心参数：参数量/训练数据量未公开；窗口内未发现新模型（News 顶部最新为 IPO Close 11-20, IPO 定价 11-18, roadshow 11-10）
- 主要创新点：既有口径：训练数据含公开+第三方数据+自报数据；在代码/金融/科学等领域同级新高；需在代码任务、文档生成等场景自主工作；链接：[Anthropic News — Introducing Claude Fable and Mythos 5.2](https://www.anthropic.com/news/claude-fable-and-mythos-5-2)

### 4. Google DeepMind

**Gemini 4 Neon（最新, 2026-11-18, Google ai.google / DeepMind Gemini 模型页, AA Index v5.01 #3）**

- 中文标题：Google DeepMind Gemini 4 Neon 系统卡（发布 2026-11-18）
- 英文标题：Introducing Gemini 4 Neon（Google DeepMind）
- 发布机构：Google DeepMind
- 模型名称/系列：Gemini 4 Neon（Gemini 4 系列旗舰）
- 发布日期：2026-11-18
- 核心参数：上下文 1M token；定价 $3M/$15M per M in/out tokens（输入 $3/M, 缓存 $0.15/M, 输出 $15/M）；统一文本/图像/视频/音频；Vals Index #2
- 主要创新点：全新一级, AA Index v5.01 #3 (score 61); 内部安全：unjustified refusals −3.00pp vs Hydrogen
- arXiv/链接：[Introducing Gemini 4 Neon (blog.google)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)、[ai.google — Gemini 4 Neon 新闻](https://ai.google/news/introducing-gemini-4-neon/)

### 5. NVIDIA

**NVIDIA Nemotron 3.5 Super（最新, arXiv:2611.22161, 2026-11-17, NVIDIA Technical Blog / NVIDIA AI Models 页）**

- 中文标题：NVIDIA Nemotron 3.5 Super 技术报告（arXiv:2611.22161, 2026-11-17）
- 英文标题：NVIDIA Nemotron 3.5 Super（technical report, arXiv:2611.22161）
- 发布机构：NVIDIA
- 模型名称/系列：Nemotron 3.5 Super（Nemotron 系列, Super/Bolt/Nano/Ultra/Labs-Sigma）
- 发布日期：2026-11-17
- 核心参数：总参数 120B, 激活 12B（Hybrid MoE Mamba-Transformer, 1M ctx）；GDP_pdf +13.8
- 主要创新点：Hybrid MoE Mamba-Transformer 架构；**CISPO RL 后训练 via Tinker rank-32 LoRA**；SWE-bench Pro V2 86.9%→92.1%；另有 Nemotron-Labs-Sigma 连续扩散 LM（arXiv:2610.02665, Phased DMD NFE 2/4/8/16）
- arXiv/链接：[arXiv:2611.22161](https://arxiv.org/abs/2611.22161)、[NVIDIA AI Models — NVIDIA Nemotron Super v1.5](https://developer.nvidia.com/ai-models/nemotron)

### 6. DeepSeek

**DeepSeek-V4.1 Flash（最新, 2026-09-10, 深度思考智能搜索 + API 更新 V4.1-Flash-1017）**

- 中文标题：DeepSeek V4.1 Flash（更强、更快、更普惠, API 更新 V4.1-Flash-1017, DeepSeek 中文版 news）
- 英文标题：DeepSeek V4.1 Flash（Stronger, Faster, Cheaper）
- 发布机构：DeepSeek
- 模型名称/系列：DeepSeek V4.1 Flash（V4-Pro/V4-Flash, deepseek-v4-pro/deepseek-v4-flash 路由, V4-Pro 计划在 V4.1 Flash 上线后随时上线）
- 发布日期：2026-09-10
- 核心参数：总参数 552B, 激活 8B/16B（Causal-Encoder-Decoder 不对称, 输入/输出非对称, 已公开说明）；原生多模态（视觉理解）；KV Cache 缩小 437 倍（相对代价：HBM 需求下降到 1/4, SSD 需求下降到 1/8）
- 主要创新点：新的不对称 MoE 结构（激活 ≤16B, 与已知同尺寸模型相比显著降低成本, 更低成本、更快速度完成任务）；新预训练 + 强化学习后训练, Agentic Benchmark 超越 DeepSeek V4 Pro 及主流旗舰；技术报告 PDF 公开
- arXiv/链接：[DeepSeek V4.1 Flash tech report (huggingface.co/deepseek-ai)](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf)、[DeepSeek 中文版 news — V4.1 Flash](https://www.deepseek.com/news/deepseek-v4-1-flash/)

**DeepSeek-V4 Preview（最新, 2026-04-24, arXiv:2606.19348, DeepSeek 中文版 news）**

- 中文标题：DeepSeek-V4 预览版：迈入百万上下文普惠时代
- 英文标题：DeepSeek-V4 Preview（arXiv:2606.19348）
- 发布机构：DeepSeek
- 模型名称/系列：DeepSeek-V4（Pro 1.6T/49B Flash 284B/13B 规格, 1M 上下文, CSA+HCA+DSA）
- 发布日期：2026-04-24
- 核心参数：上下文 1M（1,048,576, DeepSeek API）；混合注意力（DSA, CSA+HCA）；Agentic Coding 达开源最佳；世界知识略逊 Gemini-Pro-3.1；数学/STEM/竞赛型代码世界顶级
- 主要创新点：新架构（DSA 混合注意力, 全局长上下文能力, 降低计算与显存需求, 全部官方服务统一支持 1M 上下文）
- arXiv/链接：[arXiv:2606.19348 (arxiv.org/abs/2606.19348)](https://arxiv.org/abs/2606.19348)、[DeepSeek 中文版 news — V4 Preview](https://www.deepseek.com/news/v4-preview/)

### 7. Meta AI (LLaMA)

**Muse Spark 1.3（最新, ai.meta.com/llama/, 日期未标注）**

- 中文标题：Meta Muse Spark 1.3（ai.meta.com/llama/ 目录, 日期未标注）
- 英文标题：Muse Spark 1.3（ai.meta.com/llama/）
- 发布机构：Meta AI
- 模型名称/系列：Muse Spark 1.3（个人超级智能, agentic 编码）
- 发布日期：日期未标注（窗口内 ai.meta.com/llama/ 页面传输失败, 沿用 2026-11-21 速览口径）
- 核心参数：参数量未公开；最新核验为：双轨产品 Muse Spark 1.3（视频/文档/幻灯片/音频等, FastFrames, 思考范围 0–90%, 计划并执行长任务）
- 主要创新点：agentic 编码；适配 Claude Code/OpenClaw/OpenCode 等 Agent 产品；长达数分钟, 立即启动, 立即检查进度, 立即停止/重跑/编辑；链接：[Meta AI — Muse Spark (ai.meta.com/llama/)](https://ai.meta.com/llama/)

### 8. Mistral AI

**Le Chonk（最新, 2026-11-05, 10-29 开放权重, Mistral News）**

- 中文标题：Mistral Le Chonk（Mistral News, 2026-11-05, 10-29 开放权重）
- 英文标题：Le Chonk（Mistral News）
- 发布机构：Mistral AI
- 模型名称/系列：Le Chonk（Mistral 系列最新）
- 发布日期：2026-11-05（自毁 10-29 开放权重）
- 核心参数：额外核验: Large 4 最新 (2026-10-06, 1T/49B, MLA+DSA, 1M ctx)
- 主要创新点：Le Chonk 是 Mistral 近期的旗舰, 窗口内站点未新增; 沿用 2026-11-21 速览口径
- arXiv/链接：[Mistral News — Le Chonk](https://www.mistral.ai/news/)

**Mistral Large 4（最新, 2026-10-06, 1T/49B, MLA+DSA, 1M ctx）**

- 中文标题：Mistral Large 4（2026-10-06, 1T/49B）
- 英文标题：Mistral Large 4（Mistral AI, 2026-10-06）
- 发布机构：Mistral AI
- 模型名称/系列：Mistral Large 4
- 发布日期：2026-10-06
- 核心参数：参数量 1T/49B（双轨架构）；MLA+DSA, 1M 上下文
- 主要创新点：长上下文架构（MLA+DSA）；大模型全球领先
- arXiv/链接：[Mistral AI — Le Chonk (Mistral News)](https://www.mistral.ai/news/)

### 9. xAI

**Grok 4.7（最新, 2026-09-22, xAI News, 500K ctx）**

- 中文标题：Grok 4.7（xAI News, 2026-09-22）
- 英文标题：Grok 4.7（xAI）
- 发布机构：xAI
- 模型名称/系列：Grok 4.7（Grok 系列最新）
- 发布日期：2026-09-22
- 核心参数：500K 上下文；reasoning 模型
- 主要创新点：reasoning 模型; 最新 xAI 站点本窗口传输失败, 沿用既有口径
- arXiv/链接：[xAI News — Grok 4.7](https://x.ai/news/)

### 10. Amazon Nova

**Amazon Nova 2 Sonic（最新报告, 2025-12-02, AWS 技术博客, Speech-to-Speech）**

- 中文标题：Amazon Nova 2 Sonic（AWS 技术博客, 2025-12-02）
- 英文标题：Introducing Amazon Nova 2 Sonic: Our New Speech-to-Speech Model for Conversational AI
- 发布机构：Amazon Web Services (AWS), Amazon Nova
- 模型名称/系列：Amazon Nova 2 Sonic（Nova 2 系列, Speech-to-Speech 模型）
- 发布日期：2025-12-02
- 核心参数：2025-12-02 技术博客口径: 1M ctx, extended thinking 低/中/高, web grounding + code interpreter；经 AWS Nova 分类周报（2026-10-13）确认更新为 Nova 2.5 Sonic（2026-10）
- 主要创新点：语音到语音对话 AI, 多语言, 动态语速控制, 跨模态输入, 更好的遥控分析
- arXiv/链接：[Introducing Amazon Nova 2 Sonic (aws.amazon.com/blogs/aws)](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-2-sonic-next-generation-speech-to-speech-model-for-conversational-ai/)、[AWS News Blog — Amazon Nova 分类](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-nova/)

### 11. Apple

**Apple Foundation Model 3 (AFM 3) + Siri AI（最新, apple.com/ai, 2026）**

- 中文标题：Apple Foundation Model 3 (AFM 3, 20B sparse) 与 Siri AI（apple.com/ai, 2026）
- 英文标题：Apple Foundation Model 3 (AFM 3) + Siri AI (apple.com/ai)
- 发布机构：Apple
- 模型名称/系列：Apple Foundation Model 3 (AFM 3, 20B sparse)；Siri AI（Apple Intelligence）
- 发布日期：2026（AFM 3 发布系, FrogNano-4B 等）
- 核心参数：AFM 3 Cloud 模型（AFM 3 是 3B/3.5B 小模型, 结合 FrogNano-4B 等 Mini 模型）；Siri AI 是 Apple Silicon 设备端推理模型
- 主要创新点：Apple Silicon 设备端 AI 模型（AFM 3 发布系）；Siri AI（Apple Intelligence, 新高性能设备端模型，推理速度提升至超过 90% 以上, 推理速度 2x, 资源与用户数据已通过 20B sparse AFM 3 等端侧模型）
- arXiv/链接：[Apple AI — Siri AI 与 Apple Intelligence](https://www.apple.com/ai/)

### 12. Zhipu AI

**GLM-5.3（最新, zhipuai.cn, 2026, Frontier Coding）**

- 中文标题：GLM-5.3（智谱 open.zhipu.ai, Frontier Coding with Emergent Cyber Capabilities, 1M 上下文）
- 英文标题：GLM-5.3（zhipuai.cn, Frontier Coding with Emergent Cyber Capabilities）
- 发布机构：Z.AI / 智谱 AI（open.zhipu.ai）
- 模型名称/系列：GLM-5.3（GLM 系列旗舰）；GLM-5V-Turbo；GLM-5-Turbo；AutoGLM；ZCode
- 发布日期：2026（GLM-5.3 为最新模型）
- 核心参数：最新核验（2026-11-21 速览）记录为 1M 上下文；窗口内未发现 GLM-5.3 明确激活参数；GLM-OS 概念公告标注 2026-11-29
- 主要创新点：Coding benchmark 全新高；GLM-OS 概念（智谱 2026-11-29 公告）
- arXiv/链接：[Z.ai / 智谱 — GLM-5.3 (open.zhipu.ai)](https://open.zhipu.ai/)、[zhipuai.cn — GLM-OS 概念公告](https://www.zhipuai.cn/)

### 13. InternLM (Shanghai AI Lab)

**Sage S2.1 Flash（最新, arXiv:2611.21072, 2026-11-16, InternLM GitHub, MIT 权重）**

- 中文标题：InternLM Sage S2.1 Flash 技术报告（arXiv:2611.21072, 2026-11-16, MIT 开放权重, 上海人工智能实验室）
- 英文标题：Sage S2.1 Flash: AI for Scientific Research（arXiv:2611.21072, InternLM）
- 发布机构：InternLM (Shanghai AI Laboratory)
- 模型名称/系列：Sage S2.1 Flash（Sage 科学多模态系列）
- 发布日期：2026-11-16
- 核心参数：总参数 320B, 激活 32B（MoE）；科学多模态, 多步定向多模态参数路由；MLE-bench Lite 90.3 第一
- 主要创新点：科学多模态模型（InternLM3.5, 320B MoE 科学多模态, 深度思考模式）；可验证环境 agentic 后训练, MLE-bench Lite 90.3 第一
- arXiv/链接：[Sage S2.1 Flash (arxiv.org/abs/2611.21072)](https://arxiv.org/abs/2611.21072)、[InternLM GitHub (github.com/InternLM/InternLM)](https://github.com/InternLM/InternLM)

### 14. Moonshot AI (Kimi)

**Kimi K3.1 Pro（最新, moonshot.ai/blog, 2026-10-24, Kimi Blog）**

- 中文标题：Kimi K3.1 Pro（moonshot.ai/blog, 2026-10-24, KDA+MLA+DSA, 1M ctx, 3T 规模）
- 英文标题：Kimi K3.1 Pro（moonshot.ai/blog, 2026-10-24）
- 发布机构：Moonshot AI
- 模型名称/系列：Kimi K3.1 Pro（Kimi K3 系列, KDA+MLA+DSA, 推理模型）
- 发布日期：2026-10-24
- 核心参数：3T 规模参数, 1M 上下文
- 主要创新点：前沿智能, 一级异质混合架构, 1M 上下文
- 链接: [Kimi K3.1 Pro (moonshot.ai/blog)](https://www.moonshot.ai/blog/kimi-k3-1-pro)

### 15. StepFun (阶跃星辰)

**Step 5 Preview（最新, 2026-11, StepFun 官网, 92 层, Sparse GQA）**

- 中文标题：Step 5 Preview（StepFun 官网, 2026-11, 92 层, Sparse GQA）
- 英文标题：Step 5 Preview（StepFun）
- 发布机构：StepFun（阶跃星辰）
- 模型名称/系列：Step 5 Preview（StepFun 系列最新, 首款 MOE 架构预览）
- 发布日期：2026-11（既有口径: 2026-11-18, 11-19 速览核验: 600B/27B, 92 层, Sparse GQA）
- 核心参数：600B 总参, 27B 激活（MoE）；92 层, Sparse GQA
- 主要创新点：下一代 MOE 架构（全新 MOE 架构预览）
- arXiv/链接：[StepFun 官网 (Step 5 Preview)](https://www.stepfun.com/)

### 16. ByteDance (豆北/Doubao/Seed)

**Dreamina Seedance 2.5（最新, 2026-07-31, ByteDance Newsroom）**

- 中文标题：ByteDance Dreamina Seedance 2.5（Newsroom, 2026-07-31, 豆北/Doubao 系列）
- 英文标题：ByteDance Dreamina Seedance 2.5（Newsroom）
- 发布机构：ByteDance（豆北/Doubao 系列）
- 模型名称/系列：Dreamina Seedance 2.5（2026-07-31, Seedance 2.5 系列, 人像转动化）
- 发布日期：2026-07-31
- 核心参数：既有口径：2 分钟生成，Seedance 2.0-Fast（0.8s/frame）
- 主要创新点：两步视频扩散；Fast 8.5s/frame, Pro 35.4ms, HD 2.6s/frame
- arXiv/链接：[ByteDance Newsroom (bytedance.com/en/newsroom/)](https://www.bytedance.com/en/newsroom/)

### 17. Microsoft (Phi)

**FrogNano-4B（最新, Microsoft Tech Community / Azure AI Foundry, 2026-11）**

- 中文标题：FrogNano-4B（Microsoft Phi 系列变体, 2026-11, Microsoft Tech Community 记录）
- 英文标题：FrogNano-4B（Phi 4B 小型模型变体）
- 发布机构：Microsoft（Phi 系列, Azure AI Foundry, Microsoft Tech Community）
- 模型名称/系列：FrogNano-4B（Microsoft Phi 系列, Mini Models, 3B/3.5B/4B）
- 发布日期：2026-11-18（窗口内 Microsoft Tech Community 搜索已确认, 上期速览记录）
- 核心参数：4B 参数（Phi 4B 小型模型, 无详细公开, FrogNano 4B 为 Mini 模型变体）
- 主要创新点：Phi 系列大模型架构设计；Foundry Models 页称 Microsoft Phi 在 Foundry Models 有 60M+ downloads（2026-11-22）
- arXiv/链接：[Azure AI Foundry Models — Microsoft Foundry Models (azure.microsoft.com/en-us/products/ai-foundry/models/)](https://azure.microsoft.com/en-us/products/ai-foundry/models/)、[Microsoft Tech Community (techcommunity.microsoft.com) — 2026-11-18 相关记录]

**Phi-4-reasoning-vision-15B（最新, 2026-11-18, 双轨, vision+reasoning, 既有口径, 11-21 速览）**

### 18. Yi (01.AI)

**Yi-Lightning（2024.10, 千亿参数 MoE, 无新报告）**

- 中文标题：Yi-Lightning（01.AI, 2024-10, 千亿参数 MoE）
- 英文标题：Yi-Lightning（01.AI）
- 发布机构：01.AI
- 模型名称/系列：Yi-Lightning（LMSYS 第六, 中国第一）
- 发布日期：2024-10（窗口内未发现新报告）
- 核心参数：千亿参数 MoE（双轨架构, 既有口径, LMSYS 第六）
- 主要创新点：暂无（窗口内未发现新报告, 01.AI 新闻中心/网页均未核验到新 LLM 报告）
- arXiv/链接：[Yi-Lightning (01.ai newsroom.html)](https://www.01.ai/newsroom.html)、[Yi 官网 (01.ai)](https://www.01.ai/)

### 19. Baichuan

**无可验证新报告（网站不可达, 2026-11-22）**

- 中文标题：（暂无可验证新报告，网站不可达）
- 英文标题：（N/A）
- 发布机构：（N/A）
- 模型名称/系列：（N/A，暂无可验证新报告）
- 发布日期：（N/A，窗口内网站不可达）
- 核心参数：（N/A）
- 主要创新点：（N/A，窗口内网站不可达, 无可验证新报告）
- arXiv/链接：（N/A）

## 局限说明

系统卡/模型卡/官方文档披露层级不一，参数量与训练数据量多为厂商自报（不可横比，详见各条“核心参数”）；Baichuan 网站暂不可访问，无可验证新报告；Meta AI/Mistral/xAI 站点本窗口传输失败/超时，沿用 2026-11-21 速览口径；不构成投资建议。
