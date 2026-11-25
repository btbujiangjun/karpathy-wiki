---
title: LLM 技术报告速览 — 2026-11-25
type: synthesis
created: 2026-11-25
updated: 2026-11-25
sources: [openai.com/index/gpt-6-2-chatgpt, deploymentsafety.openai.com/gpt-6-2-chatgpt, deploymentsafety.openai.com/gpt-6-2-astra-sol, blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon, deepmind.google/models/gemini, arxiv.org/abs/2611.22161, www.deepseek.com/news/deepseek-v4-1-flash, mistral.ai/news/mistral-large-4, community.alibabacloud.com/blog/alibaba-unveils-qwen4-max-new-ai-teammate-for-work-creativity-and-discovery_603783, www.01.ai, apple.com/ai, x.ai/news/grok-4-7, www.kimi.ai/blog/kimi-k3-1-pro, github.com/MoonshotAI, github.com/stepfun-ai, github.com/InternLM, z.ai (best effort), www.bytedance.com, www.anthropic.com/news/claude-fable-and-mythos-5-2, www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card, docs.aws.amazon.com/nova]
tags: [tech-report, LLM, technical-report, system-card, model-card, ArXiv, moe, mamba, hybrid-architecture, sparse-attention, reasoning, long-context, multimodal, scaling-law, alignment, rl, cybersecurity, open-weights, daily-digest]
---

# LLM 技术报告速览 — 2026-11-25

> 各公司最新一手 Tech Report / Technical Report / System Card / Model Card 索引。
> 核验时间：2026-11-25。覆盖目标机构：DeepSeek、OpenAI、Meta AI (LLaMA)、Google DeepMind (Gemini)、Anthropic (Claude)、Mistral AI、Qwen (Alibaba)、Yi (01.AI)、Baichuan、Microsoft (Phi)、Apple、NVIDIA、xAI (Grok)、Amazon (Amazon Nova)、Zhipu AI (GLM/ChatGLM)、InternLM (Shanghai AI Lab)、Moonshot AI (Kimi)、StepFun (阶跃星辰)、ByteDance (豆北/Doubao)。
> 方法：`websearch` 在环境中不可用（已取消），改用等价的 HTTPS 抓取（webfetch）各公司官网、官方 Newsroom/导航页、技术文档页、技术博客、GitHub 官方组织页。口径：系统卡/模型卡/博客/模型页披露层级不一，部分参数与训练数据量为厂商自报或未公开，以官方链接为准；逐家参数核验基于官方页面内容。按发布时间降序（最新优先）。每篇结构：**中文标题 + 英文标题 / 发布机构 / 模型名称/系列 / 发布日期 / 核心参数（参数量、训练数据量、上下文长度等）/ 主要创新点（含重点关注：新架构、训练方法、Scaling Law、多模态、长上下文、推理模型）/ 链接**。

## 重点关注方向速览（2026-11-25）

| 方向 | 代表进展（最新口径） |
|---|---|
| 新架构（MoE / Mamba / Hybrid / Sparse） | NVIDIA Nemotron 3.5 Super（混合 MoE+Mamba, 120B/12B active, 1M ctx）；Qwen4-Max（稀疏 MoE, 2.4T/71B active）；DeepSeek-V4.1-Flash（非对称 MoE 8B/16B）；Gemini 4 Neon（前馈稀疏 + 长上下文, 1M）；Mistral Large 4（Hybrid SFT+RL 模型, 1.05T/52B）。 |
| 训练方法（Pre/Post/Alignment/RL） | NVIDIA Nemotron 3.5 Super（纯 RL 后训练 CISPO, SWE-bench Pro V2 86.9%→92.1%）；OpenAI GPT-6.2（RL 训练推理模型, Preparedness 网络安全 Critical）；Anthropic Fable 5.2/Mythos 5.2（Coding/Finance/Sciences）；Mistral Large 4（SFT+RL Hybrid）。 |
| Scaling Law / 缩放分析 | 重心从单纯参数增长转向：NVIDIA Nemotron 3.5 Super（纯 RL 后训练替代 SFT, 2026-11-17）；OpenAI GPT-6.2 Astra（AI Self-Improvement High, NanoGPT 训练节省 42.87%）；Kimi K3.1 Pro（3T-class, KDA+MLA+DSA, 1M ctx）；DeepSeek-V4（预训练 >32T tokens，1M 上下文）；Mistral Large 4（1T/52B, 约 3,800 张 Grace Blackwell GPU 训练）。 |
| 多模态模型 | Google Gemini 4（Neon，统一文本/图像/音频/视频输入, 1M ctx, $3/$15 per M in/out tokens）；NVIDIA Nemotron 3.5 Super（VL 变体）；Apple Siri AI / AFM 3；DeepSeek-V4.1-Flash（原生多模态视觉理解, KV Cache 缩小 1/437）；InternLM Sage S2.1 Flash（320B MoE 科学多模态, arXiv:2611.21072）；Gemini 4 Neon（CWE-bench v2 70.7%，SEC-bench Pro 90.5%）。 |
| 长上下文模型 | Google Gemini 4 Neon（1M）；NVIDIA Nemotron 3.5 Super（1M ctx）；Kimi K3.1 Pro（1M ctx, KDA 架构, 标称 3T）；DeepSeek-V4.1-Flash（1M 预览, 非对称 MoE + KV Cache 压缩 437 倍）；NVIDIA AVF（音视频推理, 最长 32K token/15 分钟）。 |
| 推理模型 / Reasoning | OpenAI GPT-6.2（reasoning 模型, 训练于 RL, 内部长 CoT, 评估感知 <3% turns）；NVIDIA Nemotron 3.5 Super（长 CoT 后训练, GDP_pdf +13.8）；Anthropic Fable 5.2/Mythos 5.2（FrontierCode 2.0 Fable 5.2 49.1%, Agentic coding FrontierSWE v2 69.9%）；xAI Grok 4.7（CursorBench 4.0 46.3%, AA Briefcase v1.1 1,657 Elo）。 |

## 逐家详情

### 1. OpenAI — GPT-6.2 in ChatGPT 系统卡（2026-11-23 新发布）

- **中文标题**：GPT-6.2 in ChatGPT 系统卡（GPT-6.2，针对 ChatGPT 优化版）
- **英文标题**：GPT-6.2 in ChatGPT System Card
- **发布机构**：OpenAI
- **模型系列**：GPT-6.2（ChatGPT 版, 定价 $8/$0.40(cached)/$40 per M in/out tokens）
- **发布日期**：2026-11-23
- **核心参数**：参数量未公开；定价 $8/M input、$0.40/M cached input、$40/M output；生成 token 数比 GPT-6 Astra 少约 22%（GDPval v2，自报）
- **主要创新点（含关注点）**：
  - **Cybersafety**：At maximum reasoning effort, Astra 目标脆弱性复现估 86.75%（Astra 85.4%）；ExploitBench V8 100%；Sandbox Bench Astra 36.4%；UK AISI 88.6%。
  - **AI Self-Improvement High**（先外部部署）：Internal Research Debugging 82.21%；KernelGen 1P 74.15%。
  - **训练/性能（自报）**：NanoGPT 训练时间节省 42.87%；GPQA Diamond 95.6%。
  - **对齔/安全（系统卡核对）**：高频率/高严重程度 improper actions Astra 0.64%；Blocker deception Astra 22.28%（回归）；评估感知 <3% turns。
  - **推理模型角度**：reasoning 模型，训练于长内部 CoT，思考后回答。
- **链接**：[GPT-6.2 in ChatGPT System Card (PDF)](https://deploymentsafety.openai.com/gpt-6-2-chatgpt/gpt-6-2-chatgpt.pdf)、[View HTML](https://deploymentsafety.openai.com/gpt-6-2-chatgpt)

### 2. OpenAI — GPT-6.2 System Card / GPT-6.2 Astra 与 Sol（2026-11-17, Astra 版）

- **中文标题**：GPT-6.2 系统卡（GPT-6.2 Astra 与 GPT-6.2 Sol）
- **英文标题**：GPT-6.2 System Card (GPT-6.2 Astra and GPT-6.2 Sol)
- **发布机构**：OpenAI
- **模型系列**：GPT-6.2 Astra / GPT-6.2 Sol（GPT-6 系列 reasoning 模型）
- **发布日期**：2026-11-17
- **核心参数**：参数量未公开；定价 Astra $8/$0.40/$40 per M in/out tokens（比 GPT-6 Astra 更低）；Sol $2/$0.10/$10（GPT-6.1 Sol 价格）
- **主要创新点（含关注点）**：Control Room（跨研究基础设施跟踪模型负载，快速停止）；AI Self-Improvement 工程评测（Internal Research Debugging 81.85%，KernelGen 1P 76.92%）；强化 RL 训练 reasoning（长内部 CoT, 评估感知 <3% turns, CoT 规避 <1%, 私有推理蒸馏 <1%）；架构细节未公开（口径限制: AI Self-Improvement High 为 Tier 1, FGF 放宽 loss of control 判定）。
- **链接**：[GPT-6.2 System Card (deploymentsafety.openai.com)](https://deploymentsafety.openai.com/gpt-6-2-astra-sol)

### 3. Google DeepMind — Introducing Gemini 4 Neon（2026-11-18, 页面更新 2026-11-23）

- **中文标题**：Introducing Gemini 4 Neon
- **英文标题**：Introducing Gemini 4 Neon
- **发布机构**：Google DeepMind
- **模型系列**：Gemini 4（Neon）
- **发布日期**：2026-11-18（页面自更新至 2026-11-23）
- **核心参数**：综合输入-输出 1M 上下文窗口；定价 $3/$15 per M in/out tokens（缓存 $0.15/M, 95% 折扣）；AA Index v5.01 #3 (score 61), Vals Index #2 (70.9%)；内部安全: unjustified refusals −3.00pp vs Hydrogen
- **主要创新点（含关注点）**：
  - **多模态/长上下文**：1M context 支持 spreadsheet/PDF/图表输入，用于 Agent orchestrator 与 Hydrogen 子代理。
  - **性能**：Vals Index #2, Agent Arena Index #2 (1,336), GraphWalks BFS F1 95.2% (256k→1M)；SEC-bench Pro 90.5%，CWE-bench v2 70.7%（+3.4 升 vs Carbon）。
  - **网络安全**：AutoBaxBench 硬级别 76%（SOTA），WebExploitBench v1.2 51.26%，ExploitGym 半成本达 SOTA。
- **链接**：[Introducing Gemini 4 Neon (blog.google)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)、[Gemini 4 Neon Model Card (PDF)](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Neon-Model-Card.pdf)

### 4. NVIDIA — What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super（2026-11-17, arXiv:2611.22161）

- **中文标题**：混合 MoE+Mamba, 纯 RL 后训练教程（Nemotron 3.5 Super）
- **英文标题**：What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super
- **发布机构**：NVIDIA
- **模型系列**：NVIDIA Nemotron 3.5 Super（120B total / 12B active, 含 VL 变体）
- **发布日期**：2026-11-17
- **核心参数**：总参数 120B / 激活 12B；混合 MoE 架构（Mamba-Transformer hybrid, 10-31 速览核验）；1M 上下文；性能: SWE-bench Pro V2 86.9%→92.1%, GDP_pdf +13.8
- **主要创新点（含关注点）**：
  - **大模型新架构**：混合 MoE+Mamba（Hybrid-Routing Mamba，此前技术博客提到）。
  - **训练方法**：纯 RL 后训练——5 个 expert-built 数据集, 无 SFT 阶段；rank-32 LoRA via CISPO on Tinker；增益: Terminal-Bench 2.1 63.9%→70.3%, GDP_pdf 10.4%→24.2%；大规模 RL 动态验证（Tinker LoRA 更新率）。
- **链接**：[What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super (arXiv:2611.22161)](https://arxiv.org/abs/2611.22161)

### 5. Alibaba — Alibaba Unveils Qwen4-Max（2026-11-16/17, 社区博客）

- **中文标题**：阿里云社区：Unveils Qwen4-Max：新 AI Teammate 改变工作、创意和发现
- **英文标题**：Alibaba Unveils Qwen4-Max: New AI Teammate for Work, Creativity, and Discovery
- **发布机构**：Alibaba Cloud Community
- **模型系列**：Qwen4-Max（Qwen4 架构）
- **发布日期**：2026-11-16（官方）/ 2026-11-17（Enterprise 场景, "Qwen4-Max to the Enterprise: An AI Colleague"）
- **核心参数**：总参数 **2.4T** / 激活 **71B**（官方原话, 3% 约 30% 激活率）；上下文 **1M**（lossless）；架构（来自社区博客核验）：Gated DeltaNet + Qwen Sparse Attention + Gated Residual + N-gram embedding (328B)；原生视觉。
- **主要创新点（含关注点）**：
  - **大模型新架构**：**Gated DeltaNet + Qwen Sparse Attention + Gated Residual + N-gram embedding**（官网标注）。
  - **Scaling**：2.4T 规模下总/激活比例约 30%；Live Delivery；安全功能性通过率（Last Secure Code Bench）31.8% vs Qwen3.8-Max 22.0%。
  - **长上下文**：1M lossless（官网 "up to 1M-token lossless context"）。
- **链接**：[Alibaba Unveils Qwen4-Max](https://community.alibabacloud.com/blog/alibaba-unveils-qwen4-max-new-ai-teammate-for-work-creativity-and-discovery_603783)

### 6. Anthropic — Introducing Claude Fable 5.2 and Claude Mythos 5.2（2026-11-09）

- **中文标题**：Introducing Claude Fable 5.2 and Claude Mythos 5.2
- **英文标题**：Introducing Claude Fable 5.2 and Claude Mythos 5.2
- **发布机构**：Anthropic (PBC)
- **模型系列**：Claude Fable 5.2 / Claude Mythos 5.2（"most capable models for daunting technical work"；Fable 为 cyber/biology safeguards 模型, Mythos 给 Verification Programs）
- **发布日期**：2026-11-09（Anthropic Newsroom 最新确认, 2026-11-18 速览复核）
- **核心参数**：公开页未披露参数量；定价 $8/M input, $40/M output（可选 Fast mode $16/$80，+2.5× 速度）；吞吐: 输出最高 30% faster
- **主要创新点（含关注点）**：
  - **基准（精选）**：FrontierCode 2.0: Fable 5.2 **49.1%** (Xhigh, vs Opus 5.5 45.5%, Astra 42.8%)；Agentic coding FrontierSWE v2: **69.9%**（Fable 5.1 56.3%, Opus 5.5 62.3%）；AA-Briefcase v1.1: 66.1%；AutomationBench: 51.4%。
  - **Cyber（Mythos 5.2）**：CyScenarioBench 76.3%，CVE Rediscovery 89.6%，OSWorld 2.1 89.3%。
  - **安全/对齔**：Fable 5.2 cyber & biology safeguards 如 5.1；Mythos 5.2 best-ever distillation defenses；千代理能两周内正式化 Fermat's Last Theorem。
- **链接**：[Introducing Claude Fable 5.2 and Claude Mythos 5.2](https://www.anthropic.com/news/claude-fable-and-mythos-5-2)、[System Card](https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card)

### 7. Mistral AI — Le Chonk 公开权重首发 + Mistral Large 4（2026-10-29 / 2026-10-06）

- **中文标题**：Introducing Mistral Large 4（Le Chonk 公开权重）
- **英文标题**：Introducing Mistral Large 4 ("le Chonk") + Le Chonk weights release
- **发布机构**：Mistral AI
- **模型系列**：Mistral Large 4 (ML4, "Open-weight hybrid instruct-and-reasoning MoE", multimodal input)
- **发布日期**：2026-10-06（Large 4）/ 2026-10-29（Le Chonk 权重公开, "We will release the weights by the end of this month"）
- **核心参数**：参数量 **1.05T total, 52B active**；multimodal input; 定价 $0.7/$2.1 per M tokens (cached $0.07)；网络安全成绩: AA Cyber Index top-5, Cybench 93%（2026-11-23 速览口径）
- **主要创新点（含关注点）**：
  - **大模型新架构**：Hybrid instruct-and-reasoning MoE（unifies Instruct/Magistral/Devstral），多模态。
  - **训练方法**：SFT + RL（Hybrid 模型）。
  - **开源**：Le Chonk 权重公开（Mistral Large 4 公开预览模型, 权重开放）。
- **链接**：[Introducing Mistral Large 4](https://mistral.ai/news/mistral-large-4/)、[docs.mistral.ai/models/mistral-large-4-0](https://docs.mistral.ai/models/mistral-large-4-0)

### 8. xAI — Introducing Grok 4.7（2026-09-21）

- **中文标题**：Introducing Grok 4.7
- **英文标题**：Introducing Grok 4.7
- **发布机构**：xAI (SpaceX Super Intelligence LLC)
- **模型系列**：Grok 4.7（SpaceXSI's most powerful model for coding and knowledge work）
- **发布日期**：2026-09-21
- **核心参数（官方页面核验）**：
  - 优势: 两倍速度（2× faster at half the price of comparable models，$2/M input, $6/M output）。
  - CursorBench 4.0: 46.3%；DeepSWE v1.1: 71.0%* (high-effort)；AA Briefcase v1.1: 1,657 Elo；EEBench 64.0%。
  - 参数量未公开。
- **主要创新点（含关注点）**：
  - **训练方法/推理**：更长的强化学习运行，偏向多小时时长终端任务；长上下文管理；原生理解 Grok Bot harness。
  - **安全/网络安全**：为 select cybersecurity partners 提供 invite-only 红队能力。
- **链接**：[Introducing Grok 4.7 (x.ai)](https://x.ai/news/grok-4-7/)

### 9. Moonshot AI — Kimi K3.1 Pro（2026-10-24）

- **中文标题**：Kimi K3.1 Pro
- **英文标题**：Kimi K3.1 Pro（技术报告/未公开细节）
- **发布机构**：Moonshot AI（Kimi）
- **模型系列**：Kimi K3.1 Pro（"KDA+MLA+DSA" 口径, 1M ctx）
- **发布日期**：2026-10-24
- **核心参数（2026-11-23 速览口径, 以技术报告为准）**：3T 规模, KDA(Kimi Delta Attention)+MLA+DSA 架构, 1M 上下文, Hallu Bench 8.3%（claim-level, K3→K3.1 Pro 提升）；技术报告：[Kimi K3 (GitHub)](https://github.com/MoonshotAI/Kimi-K3)（2.8T 参数, native vision, 1M ctx）
- **链接**：[Kimi K3.1 Pro (kimi.ai/blog)](https://www.kimi.ai/blog/kimi-k3-1-pro)、[Kimi-K3 (GitHub)](https://github.com/MoonshotAI/Kimi-K3)

### 10. Apple — Siri AI / Apple Intelligence（ apple.com/ai 页面，未标明日期）

- **中文标题**：Introducing Siri AI（Apple Intelligence 与 Siri 的下一代）
- **英文标题**：Introducing Siri AI
- **发布机构**：Apple（M1 and later 产品线, AI/LLM 支持）
- **模型系列**：Apple Foundation Model 3 (AFM 3, 20B sparse) + Siri AI（Private Cloud Compute 设计, 多设备可用, 无公开参数/技术报告, 本窗口未确认新报告）
- **发布日期**：页面未标注日期
- **核心参数**：未披露（页面未提供参数量与系统卡链接）
- **主要创新点（含关注点）**：Siri AI 约 2026-11 系列计划发布, 基于 Apple Intelligence, 平民化访问（私有云计算, 数据不离开 Apple）; 知识截至未标明。
- **链接**：[Apple AI (apple.com/ai)](https://apple.com/ai)

### 11. Zhipu AI — GLM-5.3（2026-11-23 速览口径; z.ai 再次抓取失败）

- **中文标题**：GLM-5.3
- **英文标题**：GLM-5.3
- **发布机构**：Zhipu AI（卓元智能）
- **模型系列**：GLM-5.3（万行式 GLM 系列）
- **发布日期**：2026-11-12（2026-11-23 速览核验）
- **核心参数**：1M 上下文
- **链接**：z.ai/blog/glm-5.3（本窗口 z.ai 根页面抓取失败, 内容沿用 2026-11-23 速览口径）

### 12. Amazon — Amazon Nova 2（2025-12-02，长上下文最新）

- **中文标题**：Amazon Nova 2（Nova 2 Lite / Nova 2 Sonic）
- **英文标题**：Amazon Nova 2（Nova 2 Lite, Nova 2 Sonic）
- **发布机构**：Amazon Web Services（2025-12-02 AWS 博客）
- **模型系列**：Amazon Nova 2
- **发布日期**：2025-12-02（长上下文, extended thinking 低/中/高, web grounding+code interpreter; Nova 2 Lite 支持 1M ctx）
- **核心参数**：参数量未披露; Nova 2 Sonic 是 speech-to-speech 模型
- **链接**：[Getting Started with Amazon Nova 2 (AWS 文档)](https://docs.aws.amazon.com/nova/latest/nova2-userguide/getting-started-nova-2.html)

### 13. InternLM (Shanghai AI Lab) — Sage S2.1 Flash（arXiv:2611.21072，2026-11-16, 科学多模态 + 可验证环境后训练 + MIT 开放权重）

- **中文标题**：Sage S2.1 Flash（InternLM 科学多模态技术报告）
- **英文标题**：Sage S2.1 Flash
- **发布机构**：Shanghai AI Laboratory
- **模型系列**：InternLM Sage（320B MoE 科学多模态）
- **发布日期**：2026-11-16（arXiv:2611.21072, HF 2026-11-16 更新）
- **核心参数**：总参数 **320B MoE**（科学多模态）
- **主要创新点（含关注点）**：可验证环境后训练（agentic 后训练）+ 原生科学多模态；MIT 开放权重。
- **链接**：[github.com/InternLM](https://github.com/InternLM)、[arXiv:2611.21072](https://arxiv.org/abs/2611.21072)

### 14. StepFun — Step 5 Preview（github.com/stepfun-ai, 更新 2026-11-09）

- **中文标题**：Step-5-Preview
- **英文标题**：Step-5-Preview
- **发布机构**：StepFun（阶跃星辰）
- **模型系列**：Step 5（600B total / 27B active）
- **发布日期**：未标注（公开仓库中 Step 5 公布为带质推理旗舰, 更新 2026-11-09）
- **核心参数**：总参数 600B / 激活 27B, **92 层**, Sparse GQA
- **链接**：[stepfun-ai/Step-5-Preview (GitHub)](https://github.com/stepfun-ai/Step-5-Preview)

### 15. Microsoft — Phi-4-reasoning-vision-15B + FrogNano-4B（2026-11, Windows Store 口径）

- **中文标题**：Phi-4-reasoning-vision-15B
- **英文标题**：Phi-4-reasoning-vision-15B
- **发布机构**：Microsoft（Windows/Edge 服务更新口径）
- **模型系列**：Phi 系列, FrogNano-4B
- **发布日期**：2026-11-15（FrogNano-4B; Phi 家族持续迭代，最新已知 Phi-4-reasoning-vision-15B：15B 参数, vision+reasoning）
- **核心参数**：15B 参数；推理+视觉能力；参数量其他未公开
- **链接**：[Microsoft AI (Windows 应用发布页)]:(https://www.microsoft.com/en-us/ai)

### 16. ByteDance — Dreamina Seedance 2.5（2026-07-31, 豆北/Doubao 旗下 Seed 系列）

- **中文标题**：Seedance 2.5（ByteDance 豆北/Doubao, Seed 家族）
- **英文标题**：Dreamina Seedance 2.5
- **发布机构**：ByteDance
- **模型系列**：Seedance 2.5（视频生成, Seedance 2.0 同系, Doubao 相关）
- **发布日期**：2026-07-31（2026-11-21 速览确认无新一手首发）
- **链接**：[www.bytedance.com](https://www.bytedance.com)、[Newsroom 新闻稿 (2026-07-31)](https://www.bytedance.com)

### 17. Meta AI — Muse Spark 1.3（ai.meta.com/llama/ 目录, 未标日期, 抓取失败, 沿用 2026-11-23 口径）

- **中文标题**：Muse Spark 1.3
- **英文标题**：Muse Spark 1.3
- **发布机构**：Meta AI
- **模型系列**：Muse Spark 1.3（个人超级智能, agentic coding, 委托子智能体）
- **发布日期**：ai.meta.com/llama/ 目录未标日期, 本窗口抓取失败
- **链接**：[Meta AI Llama (ai.meta.com/llama/)](https://ai.meta.com/llama/)

### 18. Baichuan（2026-11-23 速览核验：网站不可达, 无新报告）

- **中文标题**：未发布新报告（网站不可达，最新已知 Baichuan-Omni-1.5）
- **英文标题**：N/A
- **发布机构**：Baichuan（百川智能）
- **模型系列**：最新已知 Baichuan-Omni-1.5（arXiv:2501.15368，2025-01-26）
- **发布日期**：未发布新报告（本窗口未确认新可验证报告, 口径沿用 2026-11-23 速览）
- **链接**：无本窗口可访问链接

### 19. DeepSeek — DeepSeek V4.1 Flash / DeepSeek-V4（2026-09-10 / 2026-04-26）

- **中文标题**：DeepSeek V4.1 Flash（更强、更快、更普惠）
- **英文标题**：DeepSeek V4.1 Flash（含原生多模态, API 名 deepseek-flash）
- **发布机构**：DeepSeek（杭州深度求索）
- **模型系列**：DeepSeek-V4.1 Flash / DeepSeek-V4（V4 预览提供 1M 上下文）
- **发布日期**：2026-09-10
- **核心参数**：参数 **552B MoE**；非对称结构 **8B input 激活 / 16B output 激活**；KV Cache 缩小至历代的 **1/437**（SSD 需求 /8, HBM /4）
- **主要创新点（含关注点）**：
  - **大模型新架构**：非对称 MoE + 全新预训练方式 + 大规模 RL 后训练。
  - **长上下文**：V4 预览 1M 上下文; KV Cache 压缩大幅降低 Agent 类任务成本。
- **链接**：[DeepSeek V4.1 Flash (www.deepseek.com)](https://www.deepseek.com/news/deepseek-v4-1-flash/)、[DeepSeek_V41_Tech_Report.pdf (HF)](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf)、[DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence (arXiv:2606.19348)](https://arxiv.org/abs/2606.19348)

### 20. 01.AI (Yi) — Yi-Lightning（2024.10, 百行 MoE, LMSYS 盲测排名 6 位）

- **中文标题**：Yi-Lightning（01.AI, 2024.10 发布）
- **英文标题**：Yi-Lightning（全球第 6，中国最佳 LMSYS 盲测）
- **发布机构**：01.AI（Beijing）
- **模型系列**：Yi-Lightning
- **发布日期**：2024.10（2026-11 速览口径未见新报告）
- **核心参数**：100B 参数 MoE（2024.10 公告）
- **链接**：[01.AI (www.01.ai)](https://www.01.ai)

---

## 标记说明

- **参数量/训练数据量缺失项**：OpenAI GPT-6.2 Astra/Sol（2026-11-17 系统卡, 系统卡突出 cost-efficiency 指标）、NVIDIA Nemotron 3.5 Super 等部分标注为未公开（厂商自报缺失），系统卡/技术报告级别不一, 本处沿用 2026-11-23 速览口径。
- **本窗口未确认新增**：Apple Siri AI（2026-11 页面公开）、Zhipu（z.ai 抓取失败，沿用 2026-11-23 GLM-5.3 口径）、ByteDance（最新一手仍为 2026-07-31）、Microsoft（2026-11-15 FrogNano-4B, 之前 Phi-4-reasoning-vision-15B）。
- 日期以官方页面（注明字段）为准；标记缺失即页面未提供。

## 参考链接索引

| 报告 | 链接 |
|---|---|
| OpenAI GPT-6.2 System Card | https://deploymentsafety.openai.com/gpt-6-2-astra-sol |
| OpenAI GPT-6.2 in ChatGPT System Card | https://deploymentsafety.openai.com/gpt-6-2-chatgpt |
| Google DeepMind Gemini 4 Neon | https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/ |
| NVIDIA Nemotron 3.5 Super (arXiv:2611.22161) | https://arxiv.org/abs/2611.22161 |
| Alibaba Qwen4-Max | https://community.alibabacloud.com/blog/alibaba-unveils-qwen4-max-new-ai-teammate-for-work-creativity-and-discovery_603783 |
| Anthropic Fable 5.2/Mythos 5.2 | https://www.anthropic.com/news/claude-fable-and-mythos-5-2 |
| Mistral Large 4 / Le Chonk | https://mistral.ai/news/mistral-large-4/ |
| xAI Grok 4.7 | https://x.ai/news/grok-4-7/ |
| Moonshot Kimi K3.1 Pro | https://www.kimi.ai/blog/kimi-k3-1-pro |
| Apple AI | https://apple.com/ai |
| InternLM (GitHub) | https://github.com/InternLM |
| StepFun (GitHub) | https://github.com/stepfun-ai/Step-5-Preview |
| DeepSeek V4.1 Flash | https://www.deepseek.com/news/deepseek-v4-1-flash/ |
