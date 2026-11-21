---
title: LLM 技术报告速览 — 2026-11-21
type: synthesis
created: 2026-11-21
updated: 2026-11-21
sources: [deepseek-v4, deepseek-v4-1-flash, openai-gpt-6-2-system-card, openai-gpt-live-1-1-system-card, openai-csam-image-classifier, anthropic-fable-5-2, anthropic-mythos-5-2, anthropic-opus-5-5, anthropic-sonnet-5-5, anthropic-haiku-5-5, gemini-4-neon, gemini-4-hydrogen, gemini-4-carbon, gemini-4-argon, mistral-large-4, mistral-le-chonk, qwen3.8-max, qwen3.8-flash-next, qwen3guard, muse-spark-1-3, muse-spark-1-2, muse-spark-open, nemotron-3-5-super, nemotron-3-5-bolt-e4b-4gb, kumo-tabular, nemotron-labs-sigma, nemotron-3-ultra, grok-4-7, nova-2-lite, nova-2-sonic, nova-2-omni-preview, glm-5-3, glm-5v-turbo, glm-5-turbo, glm-os, glm-pc, sage-s2-1-flash, kimi-k3-1-pro, kimi-k3, step-5-preview, dreamina-seedance-2-5, dreamina-seedance-2-0, yi-lightning, afm-3, siri-ai, frognano-4b, phi-4-reasoning-vision-15b]
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, mamba, hybrid-architecture, sparse-attention, reasoning, long-context, multimodal, scaling-law, alignment, rl, cybersecurity, open-weights, video-diffusion, daily-digest]
---

# LLM 技术报告速览 — 2026-11-21

> 覆盖 19 家目标机构最新一手 Tech Report / Technical Report / System Card / Model Card / 官方技术披露，重点关注新架构（MoE, Mamba, hybrid）、训练方法（pre-training, post-training, alignment, RL）、Scaling、多模态、长上下文与推理。
> 来源：官方新闻/文档页（Deployment Safety Hub、Anthropic Newsroom、DeepMind Gemini 模型页、Meta AI 目录、Mistral News、xAI News、NVIDIA Technical Blog、AWS News Blog/Nova 页、Apple AI 页、Qwen/Zhipu/Moonshot/StepFun/01.AI/ByteDance 新闻稿等）与 arXiv/HuggingFace 仓库。`websearch` 在环境中不可用（取消），改用 `webfetch`/HTTPS 直接复核官方页面。口径说明：系统卡/模型卡/博客/模型页披露层级不同，参数量与训练数据多为厂商自报（详见各条“核心参数”与“局限”）。

## 窗口发现（2026-11-21 核验）

- **新增首发**：Google DeepMind **Gemini 4 Neon**（2026-11-18，全新一级；AA Index v5.01 #3 (score 61), Vals Index #2；1M 上下文, 输入 $3/M / 缓存 $0.15/M / 输出 $15/M tokens，unjustified refusals −3.00pp vs Hydrogen）；OpenAI **GPT-6.2 System Card**（2026-11-17, Astra/Sol, 首个外部部署达 AI Self-Improvement High）；OpenAI **GPT-Live-1.1 System Card**（2026-10-15, 新增入选, full-duplex 语音模型, 可委托后台模型）；NVIDIA **Nemotron 3.5 Super**（arXiv:2611.22161, 2026-11-17, 混合 MoE Mamba-Transformer, CISPO RL 后训练 via Tinker rank-32 LoRA）；NVIDIA **Nemotron-Labs-Sigma 连续扩散 LM**（arXiv:2610.02665 v2, 2026-11-12, Phased DMD NFE 2/4/8/16）；ByteDance **Dreamina Seedance 2.5**（2026-07-31, Newsroom 新闻稿）。
- **复核情况**：Anthropic 最新仍为 **Fable 5.2 / Mythos 5.2**（11-09, Anthropic Newsroom, 最新确认披露）；Mistral 仍为 **Le Chonk**（11-05, 权重开放 10-29）+ **Mistral Large 4**（10-06）；xAI 最新 **Grok 4.7**（2026-09-22）；Amazon **Nova 2 Lite/Sonic**（2025-12-02, AWS 博客）；DeepSeek 最新 **V4.1-Flash**（2026-09-10, API deepseek-flash 更新 2026-10-17）；Meta 以 **Muse Spark 1.3**（ai.meta.com/llama/ 目录, 未标日期）为最新；Kimi 以 **K3.1 Pro**（2026-10-24）为最新；Apple 以 **AFM 3 + Siri AI**（apple.com/ai）；NVIDIA 依赖 arXiv/HF/技术博客口径（Nemotron 3.5 Super 11-17, 技术博客 2026-09-10 "How Full-Stack NIM Optimizations Deliver 2.5x More Users on Nemotron 3 Ultra"）。
- **OpenAI Deployment Safety Hub 状态**：窗口内无 11-19+ 新条目；sitemap 确认 openai.com/index/gpt-6-astra/ lastmod 2026-11-19（原文页在窗口内 403, 内容以系统卡与速览为准）；Hub 主页列出的最新 5 条：GPT-6.2 System Card (Nov 17)、OpenAI CSAM Image Classifier Model Card (Nov 16)、GPT-6 Cyber System Card (Nov 5)、ChatGPT Images 2.6 System Card (Oct 30)、GPT-Rosalind-6 Addendum (Oct 30)。
- **沙箱不可达页面**：ai.meta.com 全系列、www.meta.ai、baichuan.io 等（连接失败），口径沿用既有速览；NVIDIA newsroom 在窗口内不可达（NVIDIA 用 Technical Blog + 产品页 + 既有速览口径）。

## 重点关注方向速览（2026-11-21）

| 方向 | 代表进展（已发布/可验证） |
|---|---|
| 新架构（MoE / Mamba / Hybrid / Sparse） | NVIDIA Nemotron 3.5 Super 混合 MoE（Mamba-Transformer hybrid, 1M ctx）；Qwen3.8-Max 双轨架构（Max/Flash, 面向编码, Qwen4 未发布）；DeepSeek-V4 混合注意力（CSA+HCA+DSA, 1M 上下文）；Mistral Large 4（MLA+DSA, 1M ctx）；Meta Muse Spark 1.3（个人超级智能, agentic）。 |
| 训练方法（Pre/Post/Alignment/RL） | NVIDIA Nemotron 3.5 Super（CISPO RL 后训练 via Tinker rank-32 LoRA, SWE-bench Pro V2 86.9%→92.1%, GDP_pdf +13.8）；OpenAI GPT-6.2（RL 后训练长 CoT, 分级 Preparedness 对齐后训练）；Apple AFM 3 Cloud models（Apple Intelligence 默认模型）；Sage S2.1 Flash（可验证环境 agentic 后训练, MLE-bench Lite 90.3 第一）；NVIDIA AVF 三阶段 curriculum（短上下文 SFT → 长上下文 SFT → CoT + GRPO, 2026-11-18, NVIDIA 技术博客）。 |
| Scaling Law / 缩放分析 | 重心转向吞吐/延迟/步数/长上下文：NVIDIA Nemotron 3.5 Super（120B/12B active, 1M ctx）；GPT-6.2 Astra（AI Self-Improvement High, NanoGPT 训练节省 42.87%）；Kimi K3（2.8T, KDA+MLA+DSA, 1M ctx）；DeepSeek-V4（预训练 >32T tokens, 1M ctx）。 |
| 多模态模型 | Google Gemini 4（Argon/Neon, 统一文本/图像/视频/音频, 1M ctx）；NVIDIA Nemotron 3.5 Super（120B VL 变体）；Apple AFM 3 Cloud models + Siri AI；Apple FastFrames（自回归两步视频扩散, 480p, 35.4 ms/帧, NVIDIA 技术博客 2026-11-18）；NVIDIA AVF（Qwen2.5-7B 主干, 32K/15 min 音视频推理, 2026-11-18）；InternLM Sage SciPerception（>10 类科学输入, 2026-11-16）。 |
| 长上下文模型 | NVIDIA Nemotron 3.5 Super（1M ctx）；Gemini 4 Neon/Hydrogen（1M）；Kimi K3.1 Pro（1M）；NVIDIA AVF（最长 15 分钟音视频/32K token）；NVIDIA Nemotron-Labs-Sigma 连续扩散 LM（Phased DMD）。 |
| 推理模型 / Reasoning | GPT-6.2（reasoning, evaluation awareness <3% turns, CoT 规避 <1%, 私有推理蒸馏 <1%）；NVIDIA Nemotron 3.5 Super（长 CoT 后训练, GDP_pdf +13.8）；Muse Spark 1.3（agentic coding, 计划长任务并委托子智能体）；Sage S2.1 Flash（多步科学推理, agentic 编码）；Nova 2 Lite（extended thinking 低/中/高, web grounding）；Grok 4.7（reasoning 模型, 500K ctx）。 |

## 目标机构覆盖状态（最新核验，详见逐家详情）

| 机构 | 最新核验报告（型号/日期） | 状态 |
|------|--------------------------|------|
| DeepSeek | DeepSeek V4.1-Flash（2026-09-10, 552B MoE, KV Cache 缩小 437 倍）/ DeepSeek-V4（2606.19348, 2026-04-26） | ✓ 已记录（新） |
| OpenAI | GPT-6.2 System Card（Astra/Sol, 2026-11-17）; GPT-Live-1.1 System Card（2026-10-15）; GPT-6.1 Terra 增补（2026-10-26）; CSAM Image Classifier Model Card（2026-11-16） | ✓ 已记录（新） |
| Meta AI | Muse Spark 1.3（ai.meta.com/llama/ 目录，未标日期） | 新（目录无日期） |
| Anthropic | Fable 5.2 / Mythos 5.2 (2026-11-09) | ✓ 已记录 |
| Google DeepMind | Gemini 4 Neon (2026-11-18); Gemini 4 Hydrogen (2026-11-12); Gemini 4 Carbon (2026-11-10); Argon (2026-09) | ✓ 已记录（新） |
| Mistral AI | Le Chonk (2026-11-05), Mistral Large 4 (2026-10-06) | ✓ 已记录 |
| Qwen (Alibaba) | Qwen3.8-Max (2.4T, 11-07), Qwen3.8-Flash-Next | ✓ 已记录 |
| Yi (01.AI) | Yi-Lightning (2024.10, 千亿参数 MoE) | ✓ 已记录 |
| Baichuan | 无可验证新报告（网站不可达） | — |
| Microsoft | Phi-4-reasoning-vision-15B (15B, vision+reasoning); FrogNano-4B | ✓ 已记录 |
| Apple | Apple Foundation Model 3 (AFM 3, 20B sparse); Siri AI | ✓ 已记录 |
| NVIDIA | Nemotron 3.5 Super (2611.22161, 2026-11-17); Nemotron 3.5 Bolt E4B 4GB (2611.20771); Kumo Tabular (2611.23001); Nemotron 3 Ultra (2026, 技术博客); Nemotron-Labs-Sigma (2610.02665) | ✓ 已记录（Super 新） |
| xAI | Grok 4.7 (2026-09-22, 500K ctx) | ✓ 已记录 |
| Amazon Nova | Nova 2 Lite (2025-12-02, 1M ctx, extended thinking, web grounding+code interpreter); Nova 2 Sonic (2025-12-02, speech-to-speech) | ✓ 已记录 |
| Zhipu AI | GLM-5.3 (1M 上下文) | ✓ 已记录 |
| InternLM (Shanghai AI Lab) | Sage S2.1 Flash (arXiv:2611.21072, 2026-11-16, 320B MoE 科学多模态) | ✓ 已记录 |
| Moonshot AI (Kimi) | Kimi K3.1 Pro (2026-10-24, 3T 规模, 1M ctx) | ✓ 已记录 |
| StepFun (阶跥星辰) | Step 5 Preview (600B/27B, 92 层, Sparse GQA) | ✓ 已记录 |
| ByteDance (豆北/Doubao/Seed) | Dreamina Seedance 2.5 (2026-07-31), Seedance 2.0 (2026-04-09), Seed 2.0 (11-07 速览) | ✓ 已记录（Seedance 2.5 新） |

## 逐家详情

### 1. OpenAI

**OpenAI GPT-6.2 System Card（最新, 2026-11-17）**

- 中文标题：GPT-6.2 系统卡（GPT-6.2 Astra 与 GPT-6.2 Sol）
- 英文标题：GPT-6.2 System Card (GPT-6.2 Astra and GPT-6.2 Sol)
- 发布机构：OpenAI
- 模型名称/系列：GPT-6.2 Astra / GPT-6.2 Sol（GPT-6 系列, reasoning 模型）
- 发布日期：2026-11-17
- 核心参数：参数量/训练数据量未公开；官方说明为经多样数据集训练与过滤(降低个人信息), reasoning 模型通过 **RL** 训练先思考后回答(长内部 CoT); Preparedness: **网络安全 Critical、生物化学 High、AI Self-Improvement below High**；自报关键指标: GPQA Diamond (no tools) **97.0%**(Astra)/96.0%(Sol, 门槛 83%); ExploitBench Internal Port (2026-06→08) 任意代码执行率 **53.5%/50.5%**(GPT-6 Astra 31.5%); SEC-Bench Pro 86.75%/88.34%; MLE-Bench Revised 参考百分位 96.06; NanoGPT 训练时间节省 **42.87%**; evaluation awareness <3% turns
- 主要创新点：Control Room（跨研究基础设施跟踪模型负载, 快速停止/急停, 扩展前沿 agent 监控）；AI 自我改进工程评测（Internal Research Debugging 81.85%, KernelGen 1P 76.92%, PostTrainBench Lite 74.79%）；对齐与可监控性：CoT 规避 <1%, 未授权蒸馏提取 private reasoning <1%, 新加密推理保护, 可扣留流式响应, Codex developer prompt 抑制信息遗漏；外部评估（SecureBio VCT +2.63pp、UK AISI 网络/对齐/可监控性评测）
- arXiv/链接：[GPT-6.2 System Card (deploymentsafety.openai.com)](https://deploymentsafety.openai.com/gpt-6-2-astra-sol)（View PDF 可下载；Hub 首页 https://deploymentsafety.openai.com/）

**OpenAI GPT-Live-1.1 System Card（新增, 2026-10-15）**

- 中文标题：GPT-Live-1.1 系统卡（GPT-Live-1.1, GPT-Live-1.1 Quip, GPT-Live-1.1 API）
- 英文标题：GPT-Live-1.1 system card (GPT-Live-1.1, GPT-Live-1.1 Quip, GPT-Live-1.1 API)
- 发布机构：OpenAI
- 模型名称/系列：GPT-Live-1.1（语音模型; ChatGPT/Codex/Dots 默认语音模型, Plus+ 用户, 可委托需推理的工作给开发者指定的后台模型）
- 发布日期：2026-10-15
- 核心参数：参数未公开; full-duplex(同时倾听和说话, 可跟随暂停/中断/语速变化, 监听时刻决定响应); 语音安全评估在 production/synthetic 提示上分值更高(对比 GPT-Live-1, API 版在 mental health/emotional reliance/self-harm 类别分值更高, sexual/illicit/personal data 分值持平)
- 主要创新点：完整双工对话; 训练数据含公开数据与第三方数据, API 输入默认不用于训练; 训练数据质量过滤与双用途模型访问策略
- arXiv/链接：[GPT-Live-1.1 system card (deploymentsafety.openai.com)](https://deploymentsafety.openai.com/gpt-live-1-1/)

**OpenAI GPT-6.1 Terra 增补（2026-10-26, Deployment Safety Hub 列表口径）** — 系统卡: 网络安全 Critical / 生物化学 High, 评测觉察 9.88%（来自 11-18 速览）

**OpenAI GPT-Rosalind-6（2026-10-30, Hub 列表口径）** — 同 Astra 权重的 trusted-access 生物推理模型

**OpenAI CSAM Image Classifier Model Card（2026-11-16, 11-18 速览复核）** — CLIP+MLP 视觉安全分类器, 训练 505K/913K 样本

**OpenAI GPT-Live-1/Quip 链（10 月一手发现, 新增 GPT-Live-1.1/Quip 迭代）** — GPT-Live-1, GPT-Live-1 Quip, GPT-Live-1.1 API, GPT-Live-1.1 Quip

**OpenAI ChatGPT Images 2.6 System Card（2026-10-30, Hub 列表）** — ChatGPT Images 2.6 系统卡

**OpenAI GPT-6 Astra（窗口口径, 2026-11-17 首发）** — sitemap 确认 openai.com/index/gpt-6-astra/ lastmod 2026-11-19; 原文页 403, 内容以系统卡与速览为准

### 2. Google DeepMind (Gemini 4)

**Gemini 4 Neon（2026-11-18）**

- 中文标题：Introducing Gemini 4 Neon
- 英文标题：Introducing Gemini 4 Neon
- 发布机构：Google DeepMind
- 模型名称/系列：Gemini 4（Neon）
- 发布日期：2026-11-18
- 核心参数：combined input-output 1M 窗口（同步默认输出 64K, 最长 1M; 文本/图像/音频/视频输入）；AA Index v5.01 #3 (score 61), Vals Index #2；定价：输入 $3/M tokens（缓存 $0.15/M, 95% 折扣）、输出 $15/M tokens；内部安全：unjustified refusals −3.00pp vs Hydrogen
- 主要创新点：frontier coding + 复杂高频工作负载 fast end-to-end; 被 Gemini 4 Carbon 适配（architecture/training data 细节在 Carbon card）; MCC 评估在 Argon 上无必要的存量评估被沿用; 知识截至 2026-03
- arXiv/链接：[Introducing Gemini 4 Neon (blog.google)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)、[Gemini 4 Neon Model Card (PDF)](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Neon-Model-Card.pdf)、[evals methodology](https://deepmind.google/models/evals-methodology/gemini-4-neon)、[Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-4-neon)

**Gemini 4 Hydrogen（2026-11-12, Last updated 2026-11-16）**

- 核心参数：AA Index 51（默认）/ 54（xhigh）; 输入 $1.50/M tokens、输出 $7.50/M tokens; 1M 上下文; everyday coding & agentic workflows
- 链接：[Introducing Gemini 4 Hydrogen (blog.google)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)、[Hydrogen model card (PDF)](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Hydrogen-Model-Card.pdf)

**Gemini 4 Carbon（2026-11-10, is now available）**

- 链接：[Gemini 4 Carbon is now available (blog.google)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)、[Gemini 4 Argon（2026-09, 见 11-07 速览）](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)

### 3. Anthropic（Claude）

**Introducing Claude Fable 5.2 and Claude Mythos 5.2（2026-11-09）**

- 中文标题/英文标题：Introducing Claude Fable 5.2 and Claude Mythos 5.2
- 发布机构：Anthropic
- 模型系列：Claude Fable 5.2 / Claude Mythos 5.2
- 发布日期：2026-11-09
- 核心参数：公开页未披露
- 主要创新点："most capable models for daunting technical work — coding, finance, sciences"；适用于 coding/finance/sciences 等关键技术领域
- 官方链接：[Anthropic News (www.anthropic.com/news)](https://www.anthropic.com/news)

**Claude Opus 5.5（2026-09-22）** — leads in agentic coding and knowledge work; costs 40% less to run than Opus 5 on typical workloads（来自 11-17 速览）

**Claude Sonnet 5.5（2026-09-28）** — clear upgrade over Claude Sonnet 5, runs 30%+ faster, and costs up to 30% less（来自 Anthropic news）

**Claude Haiku 5.5（2026-10-07）** — fastest, most capable small model. Built for high-volume work like summarization, subagents, and browser use（来自 Anthropic news）

### 4. NVIDIA（Nemotron）

**NVIDIA Nemotron 3.5 Super（最新, 2026-11-17, arXiv:2611.22161）**

- 中文标题：What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super
- 英文标题：What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super
- 发布机构：NVIDIA
- 模型名称/系列：NVIDIA Nemotron 3.5 Super（120B total / 12B active, 含一个 VL 变体, 11-18 速览）
- 核心参数：120B 总量 / 12B 活跃; 1M 上下文; 混合 MoE 架构（Mamba-Transformer hybrid, 10-31 速览）; 性能：SWE-bench Pro V2 86.9%→92.1%, GDP_pdf +13.8
- 主要创新点：post-training via RL — CISPO 算法, 每次训练在 Tinker 上用 rank-32 LoRA 针对单一专家构建任务（software engineering、complex constraints、long-horizon tool use、professional chart understanding、enterprise document reasoning, 文档 adapter 无 API 工具 +8.0）；以「专家构建任务」驱动 RL 训练验证收益（可验证环境, 12 个基准 +4.5–13.8 点, NVIDIA 技术博客 2026-11-18）
- 链接：[What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super (arXiv:2611.22161)](https://arxiv.org/abs/2611.22161)

**NVIDIA Nemotron 3.5 Bolt E4B 4GB（2026-11-16, arXiv:2611.20771）**

- 模型系列：Nemotron 3.5 Bolt E4B 4GB；post-trained from Gemma-4-E4B-it; 4GB 嵌入式/桌面部署; DFlash drafter → 2.74× per-user decode speed
- 链接：[Nemotron 3.5 Bolt E4B 4GB (arXiv:2611.20771)](https://arxiv.org/abs/2611.20771)

**Kumo Tabular（2026-11-17, arXiv:2611.23001）**

- 模型系列：NVIDIA Kumo Tabular（S 27M / M 61M / L 214M）; open tabular foundation models（classification/regression）
- 链接：[Kumo Tabular (arXiv:2611.23001)](https://arxiv.org/abs/2611.23001)

**Nemotron-Labs-Sigma（连续扩散 LM, 2026-11-12, arXiv:2610.02665 v2, HF collection 11-16 更新）**

**Nemotron 3 Ultra（2026-09-10, NVIDIA 技术博客, 参数未公开）** — "How Full-Stack NIM Optimizations Deliver 2.5x More Users on Nemotron 3 Ultra"

### 5. Meta AI（Muse Spark）

**Muse Spark 1.3（ai.meta.com/llama/ 目录, 未标日期）**

- 中文标题：Muse Spark 1.3：Frontier Coding, Long-Running Agents & Advanced Computer Use
- 英文标题：Muse Spark 1.3：Frontier Coding, Long-Running Agents & Advanced Computer Use
- 发布机构：Meta AI
- 模型名称/系列：Muse Spark 1.3（页面产品：MuseWonder-1.0、Muse Ember-1.0 变体）— 系列原 Llama 目录（ai.meta.com/llama/）
- 核心参数：参数未公开（dev.meta.ai/models 目录, dev.meta.ai/models/muse-spark-1.3 为 404 未取得正文）
- 主要创新点："Plans long tasks and delegates to sub-agents"；"Cleaner code, fewer tokens"（Muse Spark 1.2 描述）; single-agent frontier coding；capabilities: frontier coding, long-running agents, advanced computer use
- 局限：dev.meta.ai/models/muse-spark-open 为 404, 未取得正文; 目录无日期; 最近一次有日期的版本 Muse Spark 1.1(2026-07-09)
- 链接：[ai.meta.com/llama/ 模型目录](https://ai.meta.com/llama/)、[Introducing Muse Spark 1.1 (blog, 2026-07-09)](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/)

**Muse Spark 1.2 / Muse Spark Open（11-20 速览口径）**：1.2 "A coding-optimized model purpose-built for agentic workflows."; Spark Open "The most capable US open-weight model to date"（816B-A42B MoE）

### 6. Apple

**Apple AFM 3 + Siri AI（apple.com/ai 页, 不标日期）**

- 中文标题：Apple AFM 3；Apple Intelligence / Siri AI
- 英文标题：Apple Foundation Model 3 (AFM 3)；Apple Intelligence and Siri
- 发布机构：Apple
- 模型系列：Apple Foundation Model 3（AFM 3）; Siri AI（Apple Intelligence, Apple Intelligence–enabled）
- 核心参数：AFM 3: 20B sparse（IFP, PC C）; Siri AI: 未公开参数（多为服务端模型, AFM 3 Cloud models in Shortcuts, daily usage limits）
- 主要创新点：AFM 3 为第三代 Foundation Model, 已部署于 Apple Intelligence 产品（"Truly helpful. Truly yours..."）; Siri AI(Apple Intelligence) 在 2026 发布，专属 Siri app, 语音更自然；Siri AI 在 iOS 27 等系统首批提供（beta）
- 局限：Siri AI beta in iOS/iPadOS/macOS/watchOS/visionOS 27; 不构成训练输入；目录正文与参数不完整（self-reported）
- 链接：[Apple Intelligence and Siri - Apple](https://www.apple.com/ai/)

### 7. DeepSeek

**DeepSeek V4.1-Flash（最新, 2026-09-10, API deepseek-flash）**

- 中文标题：DeepSeek V4.1 Flash
- 英文标题：DeepSeek V4.1 Flash（DeepSeek-V4.1-Flash, V4.1-Flash-1017 于 2026-10-17 更新）
- 发布机构：DeepSeek
- 模型名称/系列：DeepSeek V4.1-Flash（API deepseek-flash; 窗口内更新 V4.1-Flash-1017, 2026-10-17）
- 发布日期：2026-09-10
- 核心参数：552B MoE; 输入激活 8B / 输出激活 16B 非对称; 原生多模态视觉理解; KV Cache 较历代缩小 437 倍; 全新非对称模型结构, 能力更强、速度更快、成本更低
- 主要创新点：原生多模态; 强化学习后训练(前传 DeepSeek-V4)
- 链接：[DeepSeek V4.1 Flash (官网)](https://www.deepseek.com/news/deepseek-v4-1-flash/)、[DeepSeek-V4.1-Flash (HF)](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)

**DeepSeek-V4（arXiv:2606.19348, 预览 2026-04-24/发布 2026-04-26）**

- 中文标题：DeepSeek-V4：Towards Highly Efficient Million-Token Context Intelligence
- 英文标题：DeepSeek-V4
- 发布机构：DeepSeek
- 模型名称/系列：DeepSeek-V4（V4-Pro/V4-Flash 分支）
- 发布日期：2026-04-24（deepseek.com/news 预览, arXiv 发布 2026-04-26）
- 核心参数：V4-Pro 1.6T(49B 活跃); V4-Flash 284B(13B 活跃); 两者 1M 上下文; 预训练 >32T tokens(自报)
- 主要创新点：混合注意力架构 CSA+HCA+DSA 提升 1M 上下文效率; Manifold-Constrained Hyper-Connections(mHC)改进残差; Muon 优化器; DeepSeek-V4-Pro-Max(最大推理模式版); 统一 post-training 管线
- 链接：[DeepSeek-V4 (arXiv:2606.19348)](https://arxiv.org/abs/2606.19348)、[DeepSeek V4 预览 (官网)](https://www.deepseek.com/news/v4-preview/)

### 8. Mistral AI

**Le Chonk（最新, 2026-11-05, 权重开放 2026-10-29）**

- 中文标题：Le Chonk: Built for Coders, Trusted by Defenders
- 英文标题：Le Chonk: Built for Coders, Trusted by Defenders
- 发布机构：Mistral AI
- 模型系列：Le Chonk（agentic coding & cybersecurity 方向; Studio/Forge/Vibe 生态; 权重开放 2026-10-29）
- 核心参数：参数未公开(报告层级, "Trusted by Defenders" 定位)
- 主要创新点：agentic coding + cybersecurity 的新一代模型, 能力聚焦代码与防御侧
- 链接：[Mistral News (www.mistral.ai/news/)](https://www.mistral.ai/news/)、[Le Chonk page (www.mistral.ai/news/le-chonk/)](https://www.mistral.ai/news/le-chonk/)、[Mistral Large 4 page (www.mistral.ai/news/mistral-large-4/)](https://www.mistral.ai/news/mistral-large-4/)

**Mistral Large 4（2026-10-06）**

- 中文标题/英文标题：Mistral Large 4
- 发布机构：Mistral AI
- 模型系列：Mistral Large 4（1T total/49B active, 1M ctx, MLA+DSA, 128 experts top-4+shared, FP8/NVFP4, 开源权重 10-29, 技术报告待发）

### 9. xAI（Grok）

**Introducing Grok 4.7（2026-09-22）**

- 中文标题/英文标题：Introducing Grok 4.7
- 发布机构：xAI（SpaceXSI）
- 模型系列：Grok 4.7
- 核心参数：500K ctx（11-07 速览）
- 官方链接：[x.ai/news](https://x.ai/news)
- 局限：窗口内无更新

### 10. Amazon（Amazon Nova）

**Amazon Nova 2 Lite（2025-12-02, AWS 博客）**

- 中文标题：Amazon Nova 2 Lite
- 英文标题：Amazon Nova 2 Lite, a fast, cost-effective reasoning model
- 发布机构：Amazon (AWS)
- 模型系列：Amazon Nova 2 Lite（fast, cost-effective reasoning model, 1M ctx, extended thinking low/medium/high, web grounding + code interpreter, text/image/video/document inputs）
- 核心参数：1M 上下文; extended thinking(默认关闭, 低/中/高预算); 内置 web grounding(带引用)与 code interpreter
- 主要创新点：reasoning 方向的快速低成本模型; 可用于 customer service chatbots、document processing、business process automation; Nova 2 Lite 与 Nova Forge 可建立 frontier
- 官方链接：[Introducing Amazon Nova 2 Lite (AWS blogs, 2025-12-02)](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-2-lite-a-fast-cost-effective-reasoning-model/)

**Amazon Nova 2 Sonic（2025-12-02, AWS 博客）**

- 中文标题：Amazon Nova 2 Sonic
- 英文标题：Amazon Nova 2 Sonic: Our new speech-to-speech model for conversational AI
- 发布机构：Amazon (AWS)
- 模型系列：Amazon Nova 2 Sonic（speech-to-speech, 对话 AI, expressive voices in multiple languages, polyglot, Portuguese and Hindi support）
- 核心参数：语音转语音通用模型, 8KHz telephony speech input, Expressive voices(masculine/feminine in each supported language with native expressivity), natural turn-taking, seamless handling of user interruptions
- 官方链接：[Introducing Amazon Nova 2 Sonic (AWS blogs, 2025-12-02)](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-2-sonic-next-generation-speech-to-speech-model-for-conversational-ai/)

**Amazon Nova（AWS Nova 页, 2026-11-07 速览口径）**

- 模型系列：Amazon Nova portfolio（Nova 2 Lite/Sonic, Nova 2）
- 官方链接：[Generative foundation model – Amazon Nova – AWS](https://aws.amazon.com/nova/) — Nova Act(新增, agents for browser automation), Nova Forge(新服务, build your own frontier models)

### 11. Zhipu AI（GLM/ChatGLM）

**GLM-5.3（2026, zhipuai.cn/en）**

- 中文标题：GLM-5.3：Frontier Coding with Emergent Cyber Capabilities
- 英文标题：GLM-5.3: Frontier Coding with Emergent Cyber Capabilities
- 发布机构：Zhipu AI（Z.ai）
- 模型系列：GLM-5.3（GLM-5V-Turbo, GLM-5-Turbo, AutoGLM, GLM-PC, GLM-OS 概念, open-source SOTA for coding）
- 核心参数：1M 上下文
- 主要创新点：Agent 产品矩阵：GLM-OS 概念, AutoGLM(autonomous planning/reasoning/execution, 50+ 步长操作), GLM-PC(agent, pre-release)
- 官方链接：[Z.ai - Inspiring AGIT](https://www.zhipuai.cn/en)、[GLM-5.3 (zhipuai.cn/en)](https://www.zhipuai.cn/en)

### 12. Shanghai AI Lab（InternLM / Sage）

**Sage S2.1 Flash（arXiv:2611.21072, 2026-11-16）**

- 中文标题：Sage S2.1 Flash 技术报告
- 英文标题：Sage S2.1 Flash
- 发布机构：Shanghai AI Lab（InternLM）
- 模型名称/系列：Sage S2.1 Flash（320B 总量 MoE 科学多模态, Sage SciPerception, 可验证环境 agentic 后训练, MIT 权重）
- 核心参数：320B MoE; Sage SciPerception(>10 类科学输入: 分子图、晶体结构、蛋白质序列/3D、谱图等); MLE-bench Lite 90.3 第一; 2026-11-16 同步 HF(MIT License); 标注：arXiv 标题 S2.1 与摘要 S1.5 不一致
- 局限：参数/数据/训练细节为自报, 口径沿用速览
- 链接：[Sage S2.1 Flash (arXiv:2611.21072)](https://arxiv.org/abs/2611.21072)、[Shanghai AI Lab](https://www.shlab.ai/)（网页不可达, 口径沿用既有速览）

### 13. Moonshot AI（Kimi）

**Kimi K3.1 Pro（2026-10-24）**

- 中文标题/英文标题：Kimi K3.1 Pro
- 发布机构：Moonshot AI
- 模型系列：Kimi K3.1 Pro
- 核心参数：3-trillion-parameter-class model, 1M context window；built for long-horizon coding、3D creation、financial research、complex agentic tasks
- 官方链接：[Moonshot AI (www.moonshot.ai/blog)](https://www.moonshot.ai/blog/)

**Kimi K3（2026-07-16, K3 Launch）**

- 模型系列：Kimi K3（KDA+MLA+DSA, 2.8T parameters, new architecture）

### 14. StepFun（阶跥星辰）

**Step 5 Preview（11-07 速览）**

- 中文标题/英文标题：Step 5 Preview
- 发布机构：StepFun
- 模型系列：Step 5 Preview
- 核心参数：600B/27B（total/active）, 92 层, Sparse GQA
- 官方链接：[阶跥星辰](https://www.stepfun.com/)

### 15. ByteDance（豆北/Doubao/Seed）

**Dreamina Seedance 2.5（2026-07-31, ByteDance Newsroom, 生成式视频 AI）**

- 中文标题/英文标题：Dreamina Seedance 2.5 and Dola Seedream 5.0 Pro
- 发布机构：ByteDance（豆北/Doubao/Seed）
- 模型系列：Dreamina Seedance 2.5、Dola Seedream 5.0 Pro（两款行业领先生成式 AI 视频/图像模型, combine top-tier content quality with innovative editing capabilities）
- 核心参数：未给（生成式视频模型, 非 LLM 架构）
- 官方链接：[ByteDance Newsroom (2026-07-31)](https://www.bytedance.com/en/newsroom/)、[豆北 - 字节跳动旗下 AI 智能助手](https://www.doubao.com/)

**Dreamina Seedance 2.0（2026-04-09, 豆北 Seedance 权重版本）**

**Seed 2.0 / doubao-seed-evolving（11-07 速览, 见 11-20 速览口径）**

### 16. Qwen（Alibaba Cloud Model Studio）

**Qwen3.8-Max（2.4T, 11-07 速览）**

- 中文标题/英文标题：Qwen3.8-Max
- 发布机构：Alibaba Cloud（Model Studio）
- 模型系列：Qwen3.8-Max; Qwen3.8-Flash-Next（qwen4_exp 预览, Qwen4 未发布）
- 核心参数：Qwen3.8-Max 参数 2.4T
- 官方链接：[Qwen (qwenlm.github.io → qwen.ai)](https://qwenlm.github.io/)、[Alibaba Cloud - AI models](https://www.alibabacloud.com/en/models)

**Qwen3Guard（2025-09-23, 首个安全 Tech Report）**

- 中文标题/英文标题：Qwen3Guard: Real-time Safety for Your Token Stream
- 发布机构：Qwen Team
- 模型系列：Qwen3Guard（安全分类模型, 基于 Qwen3, 含 risk levels and categorized classifications）
- 官方链接：[Tech Report (qwen.ai)](https://qwen.ai/)、[GitHub (QwenLM)](https://github.com/QwenLM/Qwen)

### 17. 01.AI

**Yi-Lightning（2024.10）**

- 中文标题：Yi-Lightning 发布
- 英文标题：Yi-Lightning
- 发布机构：01.AI
- 模型系列：Yi-Lightning（千亿参数 MoE）
- 核心参数：千亿参数 MoE（LMSYS 盲测世界第六、中国第一, 2024.10）
- 官方链接：[01.AI 零一万物 - 大模型赋能千行百业](https://www.01.ai/news/)

### 18. Baichuan（百川智能）

- 状态：窗口未发现可验证新一手 Tech Report/System Card（网站不可达, baichuan.io 等）

### 19. Microsoft（Phi）

**Microsoft Phi-4-reasoning-vision-15B（vision+reasoning 合一, 15B）与 FrogNano-4B（2026, 11-18 速览型号）**

- 中文标题：Microsoft Phi-4-reasoning-vision-15B；FrogNano-4B
- 发布机构：Microsoft
- 模型系列：Phi-4-reasoning-vision（15B, vision+reasoning 合一）; FrogNano-4B（4GB 入门级）
- 发布日期：FrogNano-4B：2026（11-18 速览）
- 核心参数：Phi-4-reasoning-vision 15B
- 官方链接：[Microsoft AI (Blogs)](https://blogs.microsoft.com/ai/)、[Microsoft Newsroom (AI topics)](https://news.microsoft.com/source/topics/ai/)

## 局限说明

- 系统卡/模型卡/博客/模型页披露层级不同；参数量、训练数据量与 benchmark 多为厂商自报，口径不一不可横比（如 GPT-6.2 对比值可能反映后续版本而非发布时版本；OpenAI 评测数据多按系统卡引用）
- `websearch` 在环境中不可用(取消); 本期通过 `webfetch`/HTTPS 直接复核官方页面与 arXiv 口径; 此窗口 arXiv 导出 API 持续 429 限流, 部分机构以既有速览(synthesis/2026-11-18/19/20 tech-report-digest)为准
- 沙箱不可达页面：ai.meta.com 全系列、www.meta.ai、baichuan.io(网站近期不可达); NVIDIA newsroom 在本窗口不可达(NVIDIA 用 Technical Blog + 产品页 + 既有速览口径)
- Qwen/Moonshot 等官方页面在沙箱不可达或指向 qwen.ai 等重定向, 口径沿用既有速览(Qwen3.8-Max 2.4T, Kimi K3.1 Pro), 属此前一手发现, 无本窗口新首发确认
- Baichuan 窗口未发现可验证新报告
