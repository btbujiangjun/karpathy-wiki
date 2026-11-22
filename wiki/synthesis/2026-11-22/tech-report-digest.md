---
title: LLM 技术报告速览 — 2026-11-22
type: synthesis
created: 2026-11-22
updated: 2026-11-22
sources: [openai-gpt-6-2-system-card, openai-chatgpt-images-2-6-system-card, anthropic-fable-5-2, gemini-4-neon, nvidia-nemotron-3-5-super, meta-muse-spark-1-3, mistral-le-chonk, mistral-large-4, qwen4-max, qwen3-8-max, microsoft-frognano-4b, apple-afm-3-siri-ai, xai-grok-4-7, amazon-nova-2-sonic, zhipu-glm-5-3, zhipu-glm-os-concept, internlm-sage-s2-1-flash, moonshot-kimi-k3-1-pro, stepfun-step-5-preview, bytedance-dreamina-seedance-2-5, deepseek-v4-1-flash, deepseek-v4-preview, yi-lightning]
tags: [tech-report, LLM, technical-report, system-card, model-card, ArXiv, moe, mamba, hybrid-architecture, sparse-attention, reasoning, long-context, multimodal, scaling-law, alignment, rl, cybersecurity, open-weights, daily-digest]
---

# LLM 技术报告速览 — 2026-11-22

> 覆盖 20 家目标机构最新一手 Tech Report / Technical Report / System Card / Model Card / 官方技术披露，重点关注新架构（MoE, Mamba, hybrid, Sparse）、训练方法（pre-training, post-training, alignment, RL）、Scaling、多模态、长上下文与推理。本页为 2026-11-22 日报，含本窗口新增首发（OpenAI Images 2.6 系统卡、Qwen4-Max 系统卡）；参数量/训练数据为各厂商自报（如无公开则标注“未公开”）。

## 来源方法

`websearch` 在环境中不可用（取消），本次通过 `webfetch` 直接抓取各公司官方页面：OpenAI Deployment Safety Hub、Anthropic News、Google ai.google/blog.google 新闻、NVIDIA Technical Blog、NVIDIA AI Models 页、AWS News Blog / Amazon Nova 分类、Microsoft Azure Blog / Azure AI Foundry Models、Azure AI Foundry Models、Microsoft AI（中文版）、Alibaba Cloud Community 博客（Qwen4-Max 系统卡专题）、01.AI 新闻中心、智谱 open.zhipu.ai、Moonshot AI Blog、NVIDIA Nemotron 模型页、NVIDIA Models 页、ByteDance 新闻稿、DeepSeek 中文版 news、InternLM GitHub 主页。未获取到有效来源的机构（Meta AI、Mistral、xAI 站点传输失败/超时）沿用 2026-11-21 速览口径（Muse Spark 1.3、Le Chonk/Large 4、Grok 4.7）。

## 重点关注方向速览（2026-11-22）

| 方向 | 代表进展 |
|---|---|
| 新架构（MoE/Mamba/Hybrid/Sparse） | Qwen4（Gated DeltaNet + Qwen Sparse Attention + Gated Residual + N-gram embedding 328B，2.4T 总参、激活 71B）；NVIDIA Nemotron 3.5 Super（Hybrid Mamba-Transformer, 1M ctx, CISPO RL 后训练）；DeepSeek V4.1 Flash（不对称 8B/16B MoE, 原生多模态）；Mistral Large 4（MLA+DSA, 1M ctx）；DeepSeek V4（DSA 混合注意力，1M 上下文） |
| 训练方法（Pre/Post/Alignment/RL） | Qwen4（Live Delivery 长期任务分版交付，90 MCP 工具，Last Secure Code Bench 31.8% 安全功能性双重通过）；NVIDIA Nemotron 3.5 Super（CISPO RL 后训练 via Tinker rank-32 LoRA）；OpenAI GPT-6.2（RL 长 CoT 后训练, Preparedness 分级对齐） |
| Scaling Law / 缩放分析 | Qwen4-Max（Work360 52.69，成本下降 58%）；DeepSeek V4.1 Flash（承超 DeepSeek V4 Pro 的智能水平，价格同步下降）；Kimi K3.1 Pro（3T, 1M ctx）；NVIDIA Nemotron 3.5 Super（120B 总参/12B 激活, 1M ctx, GDP_pdf +13.8） |
| 多模态模型 | Google Gemini 4（Argon/Neon, 统一文本/图像/视频/音频, 1M ctx）；NVIDIA Nemotron 3.5 Super（120B VL 变体）；DeepSeek V4.1 Flash（原生多模态视觉）；OpenAI ChatGPT Images 2.6（图片模型，Sunburst/Flare）；Qwen4（原生 vision） |
| 长上下文模型 | Qwen4-Max（1M）；Gemini 4 Neon/Hydrogen（1M）；NVIDIA Nemotron 3.5 Super（1M）；Kimi K3.1 Pro（1M）；DeepSeek V4/V4.1 Flash（1M） |
| 推理模型 / Reasoning | GPT-6.2（reasoning, evaluation awareness <3% turns, CoT 规避 <1%）；NVIDIA Nemotron 3.5 Super（长 CoT 后训练）；Muse Spark 1.3（agentic 编码）；Grok 4.7（reasoning, 500K ctx） |

## 目标机构覆盖状态（2026-11-22 核验）

| 机构 | 最新核验报告（型号/日期） | 状态 |
|------|--------------------------|------|
| Qwen (Alibaba) | Qwen4-Max（2026-11-16/17）；Qwen3.8-Max（2026-11-07） | ✓ 已记录（新增首发 Qwen4-Max） |
| OpenAI | GPT-6.2 System Card（11-17）；ChatGPT Images 2.6 系统卡（11-4） | ✓ 已记录（新增 Images 2.6） |
| Anthropic | Fable 5.2 / Mythos 5.2（11-09） | ✓ 已记录（窗口内未发现新） |
| Google DeepMind | Gemini 4 Neon（11-18, AA Index v5.01 #3, 1M ctx, $3M/$15M per M in/out tokens） | ✓ 已记录（窗口内未发现新） |
| NVIDIA | Nemotron 3.5 Super（2611.22161, 2026-11-17, Hybrid MoE Mamba-Transformer, CISPO RL 后训练 via Tinker rank-32 LoRA） | ✓ 已记录 |
| DeepSeek | V4.1 Flash（2026-09-10, 552B MoE）；V4 Preview（2026-04-24, arXiv:2606.19348） | ✓ 已记录（窗口内未发现新） |
| Meta AI | Muse Spark 1.3（ai.meta.com/llama/ 目录, 日期未标注） | 已记录 |
| Mistral AI | Le Chonk（2026-11-05, 10-29 开放权重）；Mistral Large 4（2026-10-06, 1T/49B, MLA+DSA） | ✓ 已记录 |
| xAI | Grok 4.7（2026-09-22, 500K ctx） | ✓ 已记录 |
| Amazon Nova | Nova 2 Sonic（2025-12-02, 1M ctx, extended thinking 低/中/高, web grounding+code interpreter）；Nova 2.5 Sonic（AWS Nova 分类, 2026-10-13 Weekly Roundup 引用） | ✓ 已记录 |
| Apple | Apple Foundation Model 3 (AFM 3, 20B sparse)；Siri AI（2026） | ✓ 已记录 |
| Zhipu AI | GLM-5.3（zhipuai.cn, 1M 上下文）；GLM-OS 概念（智谱公告, 页面标注 2026-11-29） | ✓ 已记录（GLM-OS 为概念/公告） |
| InternLM (Shanghai AI Lab) | Sage S2.1 Flash（arXiv:2611.21072, 2026-11-16, 320B MoE 科学多模态, MLE-bench Lite 90.3 第一） | ✓ 已记录 |
| Moonshot AI (Kimi) | Kimi K3.1 Pro（2026-10-24, 3T 规模, 1M ctx）；Kimi K3（2026-07-16, 2.8T, KDA+MLA+DSA） | ✓ 已记录 |
| StepFun | Step 5 Preview（2026-11, 600B/27B, 92 层, Sparse GQA） | ✓ 已记录 |
| ByteDance (豆北/Seed) | Dreamina Seedance 2.5（2026-07-31, Newsroom 新闻稿） | ✓ 已记录（以既有口径） |
| Microsoft | FrogNano-4B（Phi 系, 11-18）；Phi-4-reasoning-vision-15B（15B, vision+reasoning, 11-18） | ✓ 已记录 |
| Yi (01.AI) | Yi-Lightning（2024-10, 千亿参数 MoE, LMSYS 第六, 中国第一） | ✓ 已记录 |
| Baichuan | —（网站不可达, 未发现新报告） | — |

## 逐家详情

### 1. Qwen (Alibaba) — 新增首发

**Qwen4-Max（新发布, 2026-11-16/17）**

- 中文标题：Alibaba Unveils Qwen4-Max：New AI Teammate for Work, Creativity, and Discovery（首发）/ Alibaba Cloud Brings Qwen4-Max to the Enterprise：An AI Colleague That Plans, Builds and Delivers Finished Work（企业版, 2026-11-17）
- 英文标题：Alibaba Unveils Qwen4-Max：New AI Teammate for Work, Creativity, and Discovery / Alibaba Cloud Brings Qwen4-Max to the Enterprise
- 发布机构：Alibaba（Alibaba Cloud Community 博客）
- 模型名称/系列：Qwen4-Max（Qwen4 系列旗舰）；Qwen4-Max for Enterprise（企业版）
- 发布日期：2026-11-16（首发, Alibaba Cloud Community）；2026-11-17（企业版, San Francisco）
- 核心参数：总参数 2.4T，激活 71B/token；原生 vision；上下文 1M token；架构为 MoE（2.4T 总参/71B 激活）+ Gated DeltaNet + Qwen Sparse Attention + Gated Residual，附 N-gram embedding 参数 328B（enterprise 口径）
- 主要创新点：Qwen4 架构升级（Gated DeltaNet + Qwen Sparse Attention + Gated Residual + N-gram embedding 328B）；**Live Delivery**（长任务分版交付, 先给可用初稿再持续迭代）；安全（Last Secure Code Bench 安全功能性通过率 31.8% vs Qwen3.8-Max 22.0%；代码安全检查加入训练；网络安全：防御类数据保留、攻击类数据剔除）；基准：Work360 52.69（Qwen3.8-Max 47.74），Xhigh/High 推理下 token 耗尽 24%/35%，长任务平均成本 58% 降低；支持 90 个 MCP 工具（首发页面列出的接符为 8 款）；Qwen4-Max 在 Code Arena 排名第 6 名，Agents' Last Exam、Vals Index、JobBench、Chartography 等专项基准强势
- arXiv/链接：[Alibaba Unveils Qwen4-Max (Alibaba Cloud Community)](https://www.alibabacloud.com/blog/alibaba-unveils-qwen4-max-new-ai-teammate-for-work-creativity-and-discovery_603783)、[Qwen4-Max for Enterprise (Alibaba Cloud Community)](https://www.alibabacloud.com/blog/alibaba-cloud-brings-qwen4-max-to-the-enterprise-an-ai-colleague-that-plans-builds-and-delivers-finished-work_603786)

**Qwen3.8-Max（最新已记录, 2026-11-07, 双轨架构, Max/Flash 双轨, 面向编码, Qwen4 未发布）**

### 2. OpenAI

**GPT-6.2 System Card（最新, 2026-11-17）**

- 中文标题：GPT-6.2 系统卡（GPT-6.2 Astra 与 GPT-6.2 Sol）
- 英文标题：GPT-6.2 System Card (GPT-6.2 Astra and GPT-6.2 Sol)
- 发布机构：OpenAI（Deployment Safety Hub）
- 模型名称/系列：GPT-6.2 Astra / GPT-6.2 Sol（GPT-6 系列, reasoning 模型）
- 发布日期：2026-11-17
- 核心参数：参数量/训练数据量未公开；reasoning 通过 **RL** 训练先思考后回答（长内部 CoT）；Preparedness: 网络安全 **Critical**、生物化学 **High**、AI Self-Improvement below High
- 主要创新点：Control Room（跨研究基础设施跟踪模型负载, 快速停止/急停, 扩展前沿 agent 监控）；AI 自我改进工程评测（Internal Research Debugging 81.85%, KernelGen 1P 76.92%, PostTrainBench Lite 74.79%）；可监控性（CoT 规避 <1%, 未授权蒸馏提取 private reasoning <1%, 新加密推理保护, 可扣留流式响应, Codex developer prompt 抑制信息遗漏）；自报指标：GPQA Diamond 97.0%(Astra)/96.0%(Sol), NanoGPT 训练时间节省 42.87%
- arXiv/链接：[GPT-6.2 System Card (deploymentsafety.openai.com)](https://deploymentsafety.openai.com/gpt-6-2-astra-sol)

**ChatGPT Images 2.6 System Card（新增首发, 2026-11-04, 图片模型, 非 LLM）**

- 中文标题：ChatGPT Images 2.6 系统卡（GPT-Image-2.6 Sunburst / Flare）
- 英文标题：ChatGPT Images 2.6 System Card (GPT-Image-2.6 Sunburst and Flare)
- 发布机构：OpenAI
- 模型名称/系列：GPT-Image-2.6 Sunburst / GPT-Image-2.6 Flare（图片生成模型）
- 发布日期：2026-11-04
- 核心参数：参数量未公开；自报安全评测（Sunburst: 安全生成 75.50%、未阻止 22.78%，vs GPT-Image-2.5 Sunburst 基线 76.15%/21.94%；Flare: 安全生成 75.04%、未阻止 2.14%，vs Flare 基线 78.36%/1.49%，均有统计显著差异；安全评估涵盖 sexual/hate/violence/extremism/self-harm/political 等类别）
- 主要创新点：新增 GIF 生成、照片标记（markup）、SVG 输出；Flare 可配置推理强度（生成与编辑速度）；合规改进：进一步强化扩充在线监控；CSAM 自动分类等
- arXiv/链接：[ChatGPT Images 2.6 System Card (deploymentsafety.openai.com)](https://deploymentsafety.openai.com/chatgpt-images-2-6)（PDF: /chatgpt-images-2-6/chatgpt-images-2-6.pdf）

### 3. Anthropic

**Fable 5.2 / Mythos 5.2（最新, 2026-11-09, Anthropic News）**

- 中文标题：Claude Fable 5.2 与 Claude Mythos 5.2 系统卡（Anthropic News, 2026-11-09）
- 英文标题：Introducing Claude Fable 5.2 and Claude Mythos 5.2 (Anthropic News)
- 发布机构：Anthropic
- 模型名称/系列：Claude Fable 5.2 / Claude Mythos 5.2（Fable/Mythos 系列）
- 发布日期：2026-11-09
- 核心参数：参数量/训练数据未公开；最近窗口内已核验无新模型（News 顶部最新为 IPO Close 11-20, IPO 定价 11-18, roadshow 11-10）
- 主要创新点：coding/finance/sciences 同级新高（既有速览）：训练数据含公开+第三方数据+自报数据；需在代码任务、文档生成等场景自主工作；内容安全改进的工作成果；链接：[Anthropic News — Introducing Claude Fable and Mythos 5.2](https://www.anthropic.com/news/claude-fable-and-mythos-5-2)

### 4. Google DeepMind

**Gemini 4 Neon（最新, 2026-11-18, DeepMind Gemini 模型页, AA Index v5.01 #3）**

- 中文标题：Google DeepMind Gemini 4 Neon 系统卡（发布 2026-11-18, AA Index v5.01 #3）
- 英文标题：Introducing Gemini 4 Neon（Google DeepMind）
- 发布机构：Google DeepMind
- 模型名称/系列：Gemini 4 Neon（Gemini 4 系列旗舰）
- 发布日期：2026-11-18
- 核心参数：上下文 1M token；定价 $3M/$15M per M in/out tokens（输入 $3/M, 缓存 $0.15/M, 输出 $15/M）；统一文本/图像/视频/音频；Vals Index #2
- 主要创新点：全新一级, AA Index v5.01 #3 (score 61), Vals Index #2, 一级学技术重心；内部安全：unjustified refusals −3.00pp vs Hydrogen
- arXiv/链接：[Introducing Gemini 4 Neon (blog.google)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)、[ai.google news](https://ai.google/news/introducing-gemini-4-neon/)

### 5. NVIDIA

**NVIDIA Nemotron 3.5 Super（最新, arXiv:2611.22161, 2026-11-17, NVIDIA Technical Blog）**

- 中文标题：NVIDIA Nemotron 3.5 Super 技术报告（arXiv:2611.22161, 2026-11-17, NVIDIA Technical Blog）
- 英文标题：NVIDIA Nemotron 3.5 Super（technical report, arXiv:2611.22161）
- 发布机构：NVIDIA
- 模型名称/系列：Nemotron 3.5 Super（Nemotron 系列, Super/Bolt/Nano/Ultra/Labs-Sigma, Llama Nemotron Super v1.5）
- 发布日期：2026-11-17
- 核心参数：总参数 120B，激活 12B（MoE 混合 Mamba-Transformer, 1M ctx）；GDP_pdf +13.8；120B/12B 激活
- 主要创新点：Hybrid MoE Mamba-Transformer 架构；**CISPO RL 后训练 via Tinker rank-32 LoRA**；SWE-bench Pro V2 86.9%→92.1%；NVIDIA Nemotron-Labs-Sigma 连续扩散 LM（arXiv:2610.02665, Phased DMD NFE 2/4/8/16）
- arXiv/链接：[arXiv:2611.22161 (Google Search, 之前由引擎托管)](https://arxiv.org/abs/2611.22161)、[NVIDIA AI Models 页 — NVIDIA Nemotron Super v1.5](https://developer.nvidia.com/ai-models/nemotron)

### 6. DeepSeek

**DeepSeek-V4.1 Flash（最新, 2026-09-10, 深度思考智能搜索 + API 更新 V4.1-Flash-1017）**

- 中文标题：DeepSeek V4.1 Flash（更强、更快、更普惠，API 更新 V4.1-Flash-1017, DeepSeek 中文版 news）
- 英文标题：DeepSeek V4.1 Flash（Stronger, Faster, Cheaper）
- 发布机构：DeepSeek
- 模型名称/系列：DeepSeek V4.1 Flash（V4.1 系列; V4-Pro/V4-Flash 同系列, deepseek-v4-pro/deepseek-v4-flash 路由, V4-Pro 紧随）
- 发布日期：2026-09-10
- 核心参数：总参数 552B, 激活 8B 输入/16B 输出（Causal-Encoder-Decoder 不对称, 等负未知）；原生多模态（视觉理解）；KV Cache 缩小 437 倍（SSD 需求较 HBM 输出降为 1/8）
- 主要创新点：新的不对称 MoE 结构（激活 ≤16B, 比已知同尺寸模型显著降低成本）；新预训练 + 强化学习后训练；Agentic Benchmark 超越 DeepSeek V4 Pro 及主流旗舰；原生多模态；技术报告 PDF 公开
- arXiv/链接：[DeepSeek V4.1 Flash tech report (huggingface.co/deepseek-ai)](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf)、[DeepSeek 中文版 news — V4.1 Flash](https://www.deepseek.com/news/deepseek-v4-1-flash/)

**DeepSeek-V4 Preview（最新, 2026-04-24, arXiv:2606.19348, DeepSeek 中文版 news）**

- 中文标题：DeepSeek-V4 预览版：迈入百万上下文普惠时代
- 英文标题：DeepSeek-V4 Preview: Entering the Era of Affordable 1M Context
- 发布机构：DeepSeek
- 模型名称/系列：DeepSeek-V4（Pro 1.6T/49B Flash 284B/13B 规格, 1M 上下文, CSA+HCA+DSA）
- 发布日期：2026-04-24
- 核心参数：上下文 1M（1,048,576 token, DeepSeek API）；混合注意力（DSA, CSA+HCA, 更高效的分词缓存效率）；1M 上下文统一服务首发
- 主要创新点：新架构（DSA 混合注意力, 全局长上下文能力, 降低计算和显存需求）；Agent 能力显著提高（Agentic Coding 达开源最佳）；世界知识领先（仅稍逊 Gemini-Pro-3.1）；世界顶级推理（数学/STEM/竞赛型代码）
- arXiv/链接：[arXiv:2606.19348 (arxiv.org/abs/2606.19348)](https://arxiv.org/abs/2606.19348)、[DeepSeek 中文版 news — V4 Preview](https://www.deepseek.com/news/v4-preview/)

### 7. Meta AI

**Muse Spark 1.3（最新, ai.meta.com/llama/ 目录, 日期未标注）**

- 中文标题：Meta Muse Spark 1.3（ai.meta.com/llama/ 目录, 日期未标注）
- 英文标题：Muse Spark 1.3（ai.meta.com/llama/）
- 发布机构：Meta AI
- 模型名称/系列：Muse Spark 1.3（个人超级智能, agentic 编码）
- 发布日期：日期未标注（窗口内 ai.meta.com/llama/ 页面超时, 沿用 2026-11-21 口径）
- 核心参数：参数量未公开；最近核验（2026-11-21 速览）记录为 2026-11, 双轨产品 Muse Spark 1.3（视频/文档/幻灯片/音频等，FastFrames, Deep Thinking 3.8/3.3, 安全用途等）
- 主要创新点：Muse Spark（个人超级智能, agentic 编码, 适配 Claude Code/OpenClaw/OpenCode 等 Agent；长达数分钟, 立即启动, 立即检查进度, 立即停止/重跑/编辑）；Muse Spark MCP（工具）；Muse Spark（音频）；Muse Spark（视频/文档/幻灯片/音频, 于晚上/上海时间 1:40 以后发布）
- arXiv/链接：[Meta AI — Muse Spark (ai.meta.com/llama/)](https://ai.meta.com/llama/)

### 8. Mistral AI

**Le Chonk（最新, 2026-11-05, 10-29 开放权重, Mistral News）**

- 中文标题：Mistral Le Chonk（Mistral News, 2026-11-05, 10-29 开放权重）
- 英文标题：Le Chonk（Mistral News）
- 发布机构：Mistral AI
- 模型名称/系列：Le Chonk（Mistral 系列最新, 自毁 10-29 开放权重）
- 发布日期：2026-11-05（自毁 10-29 开放权重）
- 核心参数：激活参数（双轨架构, 见 Mistral Large 4/Le Chonk 系列）；最新核验为：Le Chonk 最新, Large 4 最新 (2026-10-06, 1T/49B, MLA+DSA, 1M ctx)
- 主要创新点：Le Chonk 与旗舰多模态的最新权衡, 推理模型转变, 效率为王；窗口内 Mistral 站点未新增, 沿用 2026-11-21 口径
- arXiv/链接：[Mistral News — Le Chonk](https://www.mistral.ai/news/)

**Mistral Large 4（最新, 2026-10-06, 1T/49B, MLA+DSA）**

### 9. xAI

**Grok 4.7（最新, 2026-09-22, xAI News, 500K ctx）**

- 中文标题：Grok 4.7（xAI News, 2026-09-22）
- 英文标题：Grok 4.7（xAI）
- 发布机构：xAI
- 模型名称/系列：Grok 4.7（Grok 系列最新）
- 发布日期：2026-09-22
- 核心参数：500K 上下文；reasoning 模型；最新核验（2026-11-21 速览）
- 主要创新点：reasoning 模型；速度/计算相关优化；最新 xAI 站点本窗口传输失败, 沿用既有口径
- arXiv/链接：[xAI News — Grok 4.7](https://x.ai/news/)

### 10. Amazon Nova

**Amazon Nova 2 Sonic（最新报告, 2025-12-02, AWS 技术博客, Speech-to-Speech）**

- 中文标题：Amazon Nova 2 Sonic（AWS 技术博客, 2025-12-02）
- 英文标题：Introducing Amazon Nova 2 Sonic: Our New Speech-to-Speech Model for Conversational AI
- 发布机构：Amazon Web Services (AWS), Amazon Nova
- 模型名称/系列：Amazon Nova 2 Sonic（Nova 2 系列, Speech-to-Speech 模型）
- 发布日期：2025-12-02
- 核心参数：2025-12-02 技术博客口径: 1M ctx, extended thinking 低/中/高；经 Nova 分类周报（2026-10-13）确认更新为 Nova 2.5 Sonic（2026-10）
- 主要创新点：语音到语音对话 AI, 多语言, 动态语速控制, 跨模态输入, 更好的遥控分析（Nova 2 Lite/Sonic 既有口径, 2025-12-02, 1M ctx）
- arXiv/链接：[Introducing Amazon Nova 2 Sonic (aws.amazon.com/blogs/aws)](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-2-sonic-next-generation-speech-to-speech-model-for-conversational-ai/)、[AWS News Blog — Nova 2 Sonic](https://aws.amazon.com/blogs/aws/)（Amazon Nova 分类: https://aws.amazon.com/blogs/aws/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/amazon-nova/）

### 11. Apple

**Apple Foundation Model 3 (AFM 3) + Siri AI（最新, apple.com/ai, 2026）**

- 中文标题：Apple Foundation Model 3 (AFM 3, 20B sparse) 与 Siri AI（apple.com/ai, 2026）
- 英文标题：Apple Foundation Model 3 (AFM 3) + Siri AI (apple.com/ai)
- 发布机构：Apple
- 模型名称/系列：Apple Foundation Model 3 (AFM 3, 20B sparse)；Siri AI（Apple Intelligence）
- 发布日期：2026（AFM 3, 2.x–2.4 发布系, FrogNano-4B 等; 2026-11-21 速览记录）
- 核心参数：AFM 3 Cloud 模型（AFM 3 为 3B/3.5B 大模型, 服务器规模模型，AFM 3-4B FrogNano 总参）；Apple Intelligence/Siri AI 是 Apple Silicon 上的设备端模型, 推理模型快于 Apple Intelligence; Apple silicon 上的高能效 AI 加速
- 主要创新点：设备端 AI 模型（Apple Silicon 真智能端, 解笺与分析口径）；Siri AI（真聊天, 资源与用户数据已通过 20B sparse AFM 3 等端侧模型, 定制化AFM 3.5B 与 AFM 3 系列优化, 推理性能提升至超过 90% 以上, 推理速度 2x）；AFM 3 Cloud 模型(A28 技术, 日前拓展)
- arXiv/链接：[Apple AI — Siri AI 与 Apple Intelligence](https://www.apple.com/ai/)（文档: Apple Intelligence 技术与工作原理, 2026, Apple 文档门户, Apple Intelligence/其他模型文档路径）

### 12. Zhipu AI

**GLM-5.3（最新, zhipuai.cn, 2026, Frontier Coding）**

- 中文标题：GLM-5.3（智谱 open.zhipu.ai, Frontier Coding with Emergent Cyber Capabilities, 1M 上下文）
- 英文标题：GLM-5.3（zhipuai.cn, Frontier Coding with Emergent Cyber Capabilities）
- 发布机构：Z.AI / 智谱 AI（open.zhipu.ai）
- 模型名称/系列：GLM-5.3（GLM 系列旗舰）；GLM-5V-Turbo；GLM-5-Turbo；AutoGLM；ZCode；GLM-OS（概念）
- 发布日期：2026（GLM-5.3 为最新模型）
- 核心参数：最新核验（2026-11-21 速览）记录为 1M 上下文；窗口内未发现 GLM-5.3 明确激活参数；GLM-OS 概念公告标注 2026-11-29
- 主要创新点：Coding benchmark 全新高；CLaw（最后一个, Claw.）优化；ZCode（Multi-Agent 开发平台, 由 GLM-5.3 优化）；AutoGLM（自主规划、推理与执行）；GLM-OS 概念（智谱 2026-11-29 公告）；GLM-PC（基座 CogAgent-9B 开源, GLM-4V-9B 训练, 链接定格, 优化定制为 Multi-Agent 团队）；CogAgent-9B（GLM-4V-9B 训练基座, GLM-PC 基座开源, 效率达到 GLM-5.3 同级别的 70% 以下）；GLM-PC (Computer Use Bench, ZCode, 工具调用, CLI, Deep(Art)Agent)
- arXiv/链接：[Z.ai / 智谱 — GLM-5.3 (open.zhipu.ai)](https://open.zhipu.ai/)、[zhipuai.cn — GLM-OS 概念公告](https://www.zhipuai.cn/)

### 13. InternLM (Shanghai AI Lab)

**Sage S2.1 Flash（最新, arXiv:2611.21072, 2026-11-16, InternLM GitHub, MIT 权重）**

- 中文标题：InternLM Sage S2.1 Flash 技术报告（arXiv:2611.21072, 2026-11-16, MIT 开放权重, 上海人工智能实验室）
- 英文标题：Sage S2.1 Flash: AI for Scientific Research（arXiv:2611.21072, InternLM）
- 发布机构：InternLM (Shanghai AI Laboratory)
- 模型名称/系列：Sage S2.1 Flash（Sage 科学多模态系列, InternLM3/3.5）
- 发布日期：2026-11-16
- 核心参数：总参数 320B，激活 32B（MoE）；科学多模态, 多步定向多模态参数路由；第一名 MLE-bench Lite 90.3；与 S1.5 标题/摘要型号不一致
- 主要创新点：科学多模态模型（InternLM3.5, 320B MoE 科学多模态, 深度思考模式, OpenAI 兼容命令行）；可验证环境 agentic 后训练, MLE-bench Lite 90.3 第一
- arXiv/链接：[Sage S2.1 Flash (arxiv.org/abs/2611.21072)](https://arxiv.org/abs/2611.21072)、[InternLM GitHub (github.com/InternLM/InternLM)](https://github.com/InternLM/InternLM)、[HF: InternLM/Sage_S2.1_Flash](https://huggingface.co/internlm)

### 14. Moonshot AI (Kimi)

**Kimi K3.1 Pro（最新, moonshot.ai/blog, 2026-10-24, Kimi Blog）**

- 中文标题：Kimi K3.1 Pro（moonshot.ai/blog, 2026-10-24, KDA+MLA+DSA, 1M ctx, 3T 规模）
- 英文标题：Kimi K3.1 Pro（moonshot.ai/blog, 2026-10-24）
- 发布机构：Moonshot AI
- 模型名称/系列：Kimi K3.1 Pro（Kimi K3 系列, KDA+MLA+DSA, 推理模型）
- 发布日期：2026-10-24
- 核心参数：3T 规模参数, 1M 上下文（1,048,576, 0.2M tokens/turn 策略下的 128K, 详见速览）；KDA+MLA+DSA
- 主要创新点：前沿智能, 一级异质混合架构, 1M 上下文；链接: [Kimi K3.1 Pro (moonshot.ai/blog)](https://www.moonshot.ai/blog/kimi-k3-1-pro)、[PerceptionBench (2026-07-16, 检测结果更新)](https://www.kimi.ai/blog/perceptionbench)

### 15. StepFun (阶跃星辰)

**Step 5 Preview（最新, 2026-11, StepFun 官网, 92 层, Sparse GQA）**

- 中文标题：Step 5 Preview（StepFun 官网, 2026-11, 92 层, Sparse GQA）
- 英文标题：Step 5 Preview（StepFun）
- 发布机构：StepFun（阶跃星辰）
- 模型名称/系列：Step 5 Preview（StepFun 系列最新, 开源, 首款 MOE 架构预览）
- 发布日期：2026-11（既有口径: 2026-11-18, 11-19 速览核验: 600B/27B, 92 层, Sparse GQA）
- 核心参数：600B 总参, 27B 激活（MoE）；92 层, Sparse GQA（阶跃星辰, 全新 MOE 架构预览）
- 主要创新点：下一代 MOE 架构（阶跃星辰架构, 92 层, Sparse GQA）；3.5B/7.5B 地方 AI 模型, 27B 旗舰预览；S3 Step Models（GLM-4.5-Distill）
- arXiv/链接：[StepFun 官网 (Step 5 Preview)](https://www.stepfun.com/)

### 16. ByteDance (豆北/Doubao/Seed)

**Dreamina Seedance 2.5（最新, 2026-07-31, ByteDance Newsroom）**

- 中文标题：ByteDance Dreamina Seedance 2.5（Newsroom, 2026-07-31, 豆北/Doubao 系列）
- 英文标题：ByteDance Dreamina Seedance 2.5（Newsroom）
- 发布机构：ByteDance（豆北/Doubao 系列）
- 模型名称/系列：Dreamina Seedance 2.5（2026-07-31, Seedance 2.5 系列, 人像转动化）
- 发布日期：2026-07-31
- 核心参数：既有口径：2 分钟生成，Seedance 2.0-Fast（0.8s/frame）
- 主要创新点：两步视频扩散；Fast 8.5s/frame, Pro 35.4ms, HD 2.6s/frame（Fast Models, HD Models）；NVIDIA CUDA Kernels；Seed Models, Doubao 9S, video clip（4s,480p）, Doubao 10S (3s,720p）
- arXiv/链接：[ByteDance Newsroom (bytedance.com/en/newsroom/)](https://www.bytedance.com/en/newsroom/)

### 17. Microsoft (Phi)

**FrogNano-4B（最新, Microsoft Tech Community / Azure AI Foundry, 2026-11）**

- 中文标题：FrogNano-4B（Microsoft Phi 系列变体, 2026-11, Microsoft Tech Community 记录）
- 英文标题：FrogNano-4B（Phi 4B 小型模型变体）
- 发布机构：Microsoft（Phi 系列, Azure AI Foundry, Microsoft Tech Community, 2026-11-18 速览记录）
- 模型名称/系列：FrogNano-4B（Microsoft Phi 系列, Mini Models, 3B/3.5B/4B）
- 发布日期：2026-11-18（窗口内 Microsoft Tech Community 搜索已确认, 上期速览记录, 2026-11-18; Azure AI Foundry Models 页称 Phi 在 Foundry Models 有 60M+ downloads, Microsoft AI 页 Microsoft Ignite 2026 (2026-11-17-20) 发布行业创新）
- 核心参数：4B 参数（Phi 4B 小型模型, 无详细公开, FrogNano 4B 为 Mini 模型变体, 符合 phi 扩展化）
- 主要创新点：Phi 系列大模型架构设计（Phi-4 发布系, FrogNano 是 Microsoft 首款可下载的 Frog 系列密集家族模型, 推理强度 60-100%, TensorRT-LLM 优化, 推理加速，体系: Microsoft AI (Phi 面向个人使用).Prompt-PIT "读写节日" Phase Models
- arXiv/链接：[Azure AI Foundry Models — Microsoft Foundry Models (azure.microsoft.com/en-us/products/ai-foundry/models/)](https://azure.microsoft.com/en-us/products/ai-foundry/models/)、[Microsoft Tech Community (techcommunity.microsoft.com) — 2026-11-18 相关记录]

### 18. Apple (另含 AFM 3 Cloud 模型, Apple 目录)

**Apple Foundation Model 3 (AFM 3, 20B sparse) + Siri AI（最新, apple.com/ai, 2026）**

### 19. Apple — Apple Foundation Model 3 (AFM 3, 20B sparse)（细节: Apple AI 页, 2026）

**Apple Foundation Model 3（AFM 3, 20B sparse, Apple AI 页, 2026）**

### 20. Apple — Siri AI（apple.com/ai, 2026）

## 局限说明

系统卡/模型卡/官方文档披露层级不一，参数量与训练数据量多为厂商自报（不可横比, 详见各条“核心参数”）；Baichuan 网站暂不可访问, 未发现新报告；Meta AI/Mistral/xAI 站点本窗口传输失败/超时, 沿用 2026-11-21 速览口径；不构成投资建议。

---

跟进 `wiki/index.md` 与 `wiki/log.md` 更新后，执行 git 提交并推送。

先更新 index.md — 在 Synthesis 表顶部插入新条目（第一行 `| [conference-digest](synthesis/2026-11-21/conference-digest.md) | Conference Digest...` 是 Synthesis 表第一行, 在它前面插入 tech-report-digest 2026-11-22 行）。

再更新 log.md — 在日志顶部插入新条目。

然后 git add/commit/push。

等等 — 我需要写下完整的tech-report-digest页面。上面我给出了一部分草稿，但不够完整。让我整理一下整个页面结构再写。

页面结构（中文）：

frontmatter
# 标题
> 摘要块

## 来源方法 — 简述

## 重点关注方向速览 — 表格（新）

## 目标机构覆盖状态 — 表（全，按覆盖状态）

## 逐家详情 — 各公司条目（包含所有必需字段）

## 局限说明

注意：用户要求“报告保存到 wiki/synthesis/{{YYYY-MM-DD}}/tech-report-digest.md”，即 2026-11-22。

现在让我写完整页面。由于上面的草稿还不完整，我来整理最终内容。

每个报告包含：中文标题、英文标题、发布机构、模型名称/系列、发布日期、核心参数（参数量、训练数据量、上下文长度等）、主要创新点、arXiv/链接。

按日期排序，从最新的开始。

现在组织最终内容。我会用中文写详细的逐家详情，包含用户要求的所有字段。

需要注意的是：
- OpenAI Images 2.6 是"图片模型"，用户问的是"大模型技术报告"，但系统卡属于tech report类型，我应该包含它，但标注清楚是图片模型。
- Anthropic Fable 5.2/Mythos 5.2 — 按之前的记录, 11-9 发布
- Google Gemini 4 Neon — 11-18, AA Index v5.01 #3
- NVIDIA Nemotron 3.5 Super — 2611.22161, 2026-11-17
- Qwen4-Max — 2026-11-16/17 （新增首发）
- 等等

另外 Baichuan 在2026-11-21页面里说"Baichuan | 无可验证新报告（网站不可达）"。今天再次检查网站时传输失败，我把它注明为暂时不可访问。

Mistral Le Chonk — 11-5，权重开放 10-29。Mistral Large 4 — 2026-10-06。

xAI Grok 4.7 — 2026-09-22。

Amazon Nova 2 Sonic — 2025-12-02；Nova 2.5 Sonic — 2026-10-13（per AWS Nova category）。

Apple AFM 3 + Siri AI — 2026（Apple AI page, iPhone 18 Pro 等新设备）。

Zhipu GLM-5.3 + GLM-OS 概念 — GLM-5.3 已记录，GLM-OS 是 2026-11-29 公告（页面标注）。

InternLM Sage S2.1 Flash — arXiv:2611.21072, 2026-11-16, 320B MoE 科学多模态。

Moonshot Kimi K3.1 Pro — 2026-10-24, 3T 规模。

StepFun Step 5 Preview — 2026-11, 600B/27B, 92层。

ByteDance Dreamina Seedance 2.5 — 2026-07-31。

DeepSeek V4.1 Flash — 2026-09-10, 552B MoE, 激活 8B/16B; DeepSeek-V4 Preview — 2026-04-24, arXiv:2606.19348。

Microsoft FrogNano-4B — 2026-11-18（Tech Community 搜索结果）。

Meta Muse Spark 1.3 — 最新核验 2026-11-21（ai.meta.com/llama/ 目录，无日期）。

Yi-Lightning — 2024-10（无新）。

OK，我现在来写完整页面。我需要保持全面但简练。

关于页面内容的决定：
- 摘要块
- 来源方法简述
- 重点关注方向速览表
- 目标机构覆盖状态表
- 逐家详情（按机构，每个报告含所有字段）
- 局限说明

让我开始写最终页面内容。

关于“核心参数（参数量、训练数据量、上下文长度等）”——我需要尽可能填上每家的这些字段，不可知的写“未公开”。

训练数据量：
- Qwen4-Max: 未公开（提到 Live Delivery 等）
- OpenAI GPT-6.2: 未公开
- Google Gemini 4 Neon: 未公开（统一文本/图像/视频/音频，1M 上下文）
- NVIDIA Nemotron 3.5 Super: 未公开（Hybrid MoE, 1M ctx, CISPO RL, GDP_pdf +13.8）
- DeepSeek V4.1 Flash: 552B, 激活 8B/16B, 原生多模态
- DeepSeek V4 Preview: Pro/Flash 版本, CSA+HCA+DSA, 1M ctx
- OpenAI Images 2.6: 图片模型, Sunburst/Flare, 安全评测数据

训练数据量大多是未公开的，我会说明未公开。

关于主要创新点——参考之前页面的风格。

链接——给出每家的关键 URL。

好，让我写。我要用中文，按要求的格式。

我会写两段逐家详情：第一组（有新首发或关键数据），然后其他机构按从新到旧排序。

实际上，日报风格的逐家详情可以按机构（Alphabetical or by recency）。我按汇总表的顺序：Qwen (Alibaba)、OpenAI、Anthropic、Google、NVIDIA、DeepSeek、Meta、Mistral、xAI、Amazon、Apple、Zhipu、InternLM、Moonshot、StepFun、ByteDance、Microsoft、Yi、Baichuan（跳过或注明暂无）。

Baichuan 我注明暂无可验证新报告，网站不可达。

OK写完整页面。由于很长，我直接用 write 工具写文件。

关于 frontmatter tags 我用之前 style（tech-report, LLM, technical-report, system-card, model-card, ArXiv, moe, reasoning, long-context, multimodal, hybrid-architecture, scaling-law, alignment, rl, cybersecurity, open-weights, daily-digest）。

我会写页面内容，然后调整 index.md 和 log.md，然后 commit/push。

注意：page 里“窗口内 Anthropic Fable 5.2/Mythos 5.2(11-09)” — 来自之前digest。

现在开始写最终页面。我不会把所有细节塞进一行，保持结构化。

另外注意 — 用户的提问：“搜索各大 AI 公司最新发布的大模型技术报告”，报告要包含：中文标题 + 英文标题、发布机构、模型名称/系列、发布日期、核心参数、主要创新点、arXiv/论文链接。

好。写页面。

之前写的草稿比较乱，让我重新组织最终版本。现在来写。

对于每家公司的条目，保持如下格式：

### N. 机构（中文名）

**报告中文标题（最新, 日期）**

- 中文标题：...
- 英文标题：...
- 发布机构：...
- 模型名称/系列：...
- 发布日期：...
- 核心参数：...
- 主要创新点：...
- arXiv/链接：[text](url)

好，开始写最终页面。