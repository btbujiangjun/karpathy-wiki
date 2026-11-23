---
title: LLM 技术报告速览 — 2026-11-23
type: synthesis
created: 2026-11-23
updated: 2026-11-23
sources: [openai.com/index/introducing-gpt-6-2-astra-sol, deploymentsafety.openai.com/gpt-6-2-astra-sol, www.anthropic.com/news/claude-fable-and-mythos-5-2, www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card, blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon, deepmind.google/models/gemini, arxiv.org/abs/2611.22161, www.deepseek.com/news/deepseek-v4-1-flash, mistral.ai/news/mistral-large-4, community.alibabacloud.com/blog/alibaba-unveils-qwen4-max-new-ai-teammate-for-work-creativity-and-discovery_603783, www.01.ai, apple.com/ai, x.ai/news, docs.aws.amazon.com/nova/latest/nova2-userguide/getting-started-nova-2.html, z.ai/blog/glm-5.3, github.com/InternLM, github.com/InternLM/Intern-S1, arxiv.org/abs/2508.15763, arxiv.org/abs/2603.25040, www.kimi.ai/blog/kimi-k3-1-pro, github.com/stepfun-ai, arxiv.org/abs/2507.16632, www.bytedance.com]
tags: [tech-report, LLM, technical-report, system-card, model-card, ArXiv, moe, mamba, hybrid-architecture, sparse-attention, reasoning, long-context, multimodal, scaling-law, alignment, rl, cybersecurity, open-weights, daily-digest]
---

# LLM 技术报告速览 — 2026-11-23

> 各公司最新一手 Tech Report / Technical Report / System Card / Model Card 索引。
> 核验时间：2026-11-23。覆盖目标机构：DeepSeek、OpenAI、Meta AI (LLaMA)、Google DeepMind (Gemini)、Anthropic (Claude)、Mistral AI、Qwen (Alibaba)、Yi (01.AI)、Baichuan、Microsoft (Phi)、Apple、NVIDIA、xAI (Grok)、Amazon (Amazon Nova)、Zhipu AI (GLM/ChatGLM)、InternLM (Shanghai AI Lab)、Moonshot AI (Kimi)、StepFun (阶跃星辰)、ByteDance (豆包/Doubao)。
> 方法：逐家抓取官网（webfetch HTTPS）、官方 Newsroom/导航页、技术文档页、技术博客、Deployment Safety Hub 标准制度页、arXiv Export API（`search_query=all:"system card"/"technical report"` + 公司名）、GitHub 官方组织页。注意：本环境 `websearch` 不可用，数据来自等价的 HTTPS 抓取（fetch）；所有参数/日期均以官网或官方文档页为准（附链接），部分值为厂商自报。
> 按发布时间降序（最新优先）。每篇结构：**中文标题 + 英文标题 / 发布机构 / 模型名称 / 发布日期 / 核心参数（参数量、训练数据量、上下文长度等）/ 主要创新点（含重点关注：新架构、训练方法、Scaling Law、多模态、长上下文、推理模型）/ arXiv/链接**。

## 1. OpenAI — Introducing GPT-6.2 Astra and Sol / GPT-6.2 System Card

- **发布机构**: OpenAI
- **模型系列**: GPT-6.2 Astra（ frontier，双模型发布 Astra + Sol）
- **发布日期**: 2026-11-17（Deployment Safety Hub："Published November 17, 2026"）
- **核心参数**:
  - 参数量: **未公开**（系统卡未披露具体参数数量）
  - 定价: Astra: $8/M input, $0.40/M cached input, $40/M output（比 GPT-6 Astra 更低）；Sol: $2/$0.10/$10/M（GPT-6.1 Sol 价格）
  - 效率指标（厂商数据）: Astra 生成 token 数比 GPT-6 Astra 少约 22%（GDPval v2）
- **主要创新点（含关注点）**:
  - **Cybersafety（ExploitBench/Sandbox）**: 系统卡核对显示：At maximum reasoning effort，Astra reproduced target vuln 估 86.75%（Astra 85.4%）；ExploitBench V8 100%（Astra）；ExploitBench Internal Port（V8+Chrome, June–Aug 2026）Astra 53.5%（Astra 31.5%）；Sandbox Bench Astra 36.4%（Astra 18.2%）；UK AISI 脆弱性发现 Astra 88.6%（Astra 81.7%）；CyScenarioBench 9/11（Astra 63%, Astra 61%）。
  - **AI Self-Improvement（AI 自我改进）**: GPT-6.2 Astra = 首个外部发布的 AI Self-Improvement **High** 模型（Tier 1）。
  - **训练/性能（厂商数据）**: NanoGPT 训练时间节省 42.87%（最大 reasoning effort）；GPQA Diamond 97.0%（Astra）；Vals Science Index 新高；Terminal-Bench-Science 9pt 领先 Astra。
  - **对齔/安全行为（系统卡核对）**: 高频率/高严重程度 improper actions: Astra 0.64%（Astra 1.20%），Sol 0.71%（Sol 1.32%）；Blocker deception: Astra 22.28%（Astra 11.09% — 回归），Codex developer prompt 显著降低；评估感知 <3% turns；机械监控总 flag 4.96%（Astra，略高于 Astra 3.19%）。
  - **推理模型角度**: Astra/Sol 为 reasoning models（训练于强化学习），可进行长 CoT；评估感知倾向（suspicion of testing, <3% turns）。
- **链接**: [Introducing GPT-6.2 Astra and Sol](https://openai.com/index/introducing-gpt-6-2-astra-sol), [GPT-6.2 System Card (Deployment Safety Hub)](https://deploymentsafety.openai.com/gpt-6-2-astra-sol)

## 2. Anthropic — Introducing Claude Fable 5.2 and Claude Mythos 5.2

- **发布机构**: Anthropic (PBC)
- **模型系列**: Claude Fable 5.2 / Claude Mythos 5.2（"most capable models for daunting technical work"; Fable & Mythos 为同一底层模型，Fable 有 cyber/biology safeguards，Mythos 给 Verification Programs）
- **发布日期**: 2026-11-09
- **核心参数**:
  - 参数量: **未公开**
  - 定价: $8/M input, $40/M output（Fable 5.2/Mythos 5.2）；可选 Fast mode $16/$80（+2.5× 速度）
  - 吞吐: 输出最高 30% faster
- **主要创新点（含关注点）**:
  - **基准（精选）**: FrontierCode 2.0: Fable 5.2 **49.1%**（Xhigh effort, vs Fable 5.1 32.4%, Opus 5.5 45.5%, Astra 42.8%）；Agentic coding FrontierSWE v2: 69.9%（Fable 5.1 56.3%, Opus 5.5 62.3%）；AA-Briefcase v1.1: 66.1%; AAElo: 1,785 (Fable 5.2), 1,800 (Opus 5.5); AutomationBench: 51.4%; HLE (with tools): 74.2%; Chartography: 73.4%。
  - **Mythos 5.2 cyber（Cybermission-level）**: CyScenarioBench 76.3% (Mythos 5.2), CVE Rediscovery 89.6%, 蛋白键设计 85.1%, OSWorld 2.1 89.3%。
  - **安全/对齔**: Fable 5.2 cyber & biology safeguards 如 5.1（~55% fewer blocks），Mythos 5.2 best-ever distillation defenses；千代理能两周内正式化 Fermat's Last Theorem（高效）。
- **链接**: [Introducing Claude Fable 5.2 and Claude Mythos 5.2](https://www.anthropic.com/news/claude-fable-and-mythos-5-2), [System Card](https://www.anthropic.com/document/claude-fable-5-2-mythos-5-2-system-card)

## 3. Google DeepMind — Introducing Gemini 4 Neon

- **发布机构**: Google DeepMind
- **模型系列**: Gemini 4 Neon
- **发布日期**: 2026-11-18
- **核心参数**:
  - 上下文长度: **1M**（新增价值）
  - 定价: $3M/$15M per M in/out tokens（i.e., $3/$15 per M；cached input 95% discount）
- **主要创新点（含关注点）**:
  - **性能**: AA Index v5.01 **#3** (score 61, behind Claude Opus 5.5 / Fable 5.2, Astra); Vals Index v2.2 **#2 (70.9%)**；GraphWalks BFS F1 **95.2%** (256k→1M); Agent Arena Index **#2 (1,336)**；CWE-bench v2 70.7% (3.4% uplift over Carbon); DECOMposition? （未标注）。
  - **训练/缩放**: 企业 "fast, low cost"; AA-AnalystAgent 62.5%, AA-3D 盲测, 特别依赖强 agentic coding（SWE-sweep 12.8% → 39.0% in Antigravity）。
  - **多模态/长上下文**: 1M context for spreadsheets/PDFs/charts；使用内部机制；支持 Agent orchestrator 与 Hydrogen 子代理框架。
- **链接**: [Introducing Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

## 4. NVIDIA — Nemotron 3.5 Super (What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super)

- **发布机构**: NVIDIA
- **模型系列**: NVIDIA Nemotron 3.5 Super（+ Llama Nemotron Super v1.5 / Ultra）
- **发布日期**: 2026-11-17 (arXiv:2611.22161)
- **核心参数（arXiv 摘要，厂商自报）**:
  - 总参数: **120B**，激活参数: **12B**
- **主要创新点（含关注点）**:
  - **训练方法**: 纯 RL 后训练（five expert-built datasets, no SFT stage）：real-world software engineering、complex constraints、long-horizon tool use、professional chart understanding、enterprise document reasoning；rank-32 LoRA via CISPO on Tinker。增益：SWE-bench Pro V2 86.9%→**92.1%**, GDP_pdf 10.4%→**24.2%**, Terminal-Bench 2.1 63.9%→**70.3%**, MultiChallenge 58.3%→66.6%, AutomationBench 14.8%→27.5%, Chartography 39.4%→50.6%, IFBench +4.5pt。
  - **架构**: NVIDIA Nemotron 3.5 Super（混合 MoE + Mamba，"HYbrid-Routing Mamba"，此前 NVIDIA 技术博客提到）；Nemotron 3.5 Lightning/Bolt 等（wiki 既有记录）。
- **链接**: [arXiv:2611.22161](https://arxiv.org/abs/2611.22161), NVIDIA technical blog (2026-09-10, Nemotron 3 Ultra — 既有速览口径)

## 5. DeepSeek — DeepSeek V4.1 Flash

- **发布机构**: DeepSeek (Hangzhou 深度求索)
- **模型系列**: DeepSeek-V4.1 Flash（新命名：API 名 deepseek-flash）
- **发布日期**: 2026-09-10
- **核心参数（技术报告）**:
  - 参数量: **552B MoE**；结构 Causal-Encoder-Decoder：**输入激活 8B / 输出激活 16B**（非对称）
  - 上下文/多模态: **原生多模态视觉理解**；V4 预览提供 1M 上下文
  - KV Cache: **缩小至历代的 1/437**（SSD 需求 /8，HBM /4）
- **主要创新点（含关注点）**:
  - **大模型新架构**: 非对称 MoE（8B/16B）+ 全新预训练方式 + 大规模 RL 后训练；超越包括 DeepSeek V4 Pro 在内的一系列旗舰模型（Agentic Benchmark）。
  - **训练方法**: 强化学习后训练（大规模 RL）
  - **长上下文**: 1M（V4 预览）；KV Cache 压缩大幅降低 Agent 类任务成本。
- **链接**: [DeepSeek V4.1 Flash](https://www.deepseek.com/news/deepseek-v4-1-flash/), [DeepSeek_V41_Tech_Report.pdf](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf), [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence (arXiv:2606.19348)](https://arxiv.org/abs/2606.19348)

## 6. Mistral AI — Mistral Large 4 ("le Chonk")

- **发布机构**: Mistral AI
- **模型系列**: Mistral Large 4 (ML4, "Open-weight hybrid instruct-and-reasoning MoE", multimodal input)
- **发布日期**: 2026-10-06
- **核心参数（技术页）**:
  - 参数量: **1.05T total, 52B active**
  - 上下文/多模态: multimodal input; 定价 $0.7/$2.1 per M tokens (cached $0.07)
- **主要创新点（含关注点）**:
  - **大模型新架构**: Hybrid instruct-and-reasoning MoE（unifies Instruct/Magistral/Devstral），多模态。
  - **基准（精选）**: AA Cyber Index top-5（AA-Cyber 82%, Cybench 93%, Lakera B3 93.3%）；DeepSWE v1.1 61.7%；SWE-Atlas-QnA 59.4%；Terminal-Bench 4.0+？（数据：AutomationBench 59.9%, AA-Briefcase 1,393 Elo）。
  - **训练方法**: SFT + RL（Hybrid 模型）。
  - **开源**: 权重预计 2026 年底（官网"We will release the weights by the end of this month"; 截至 2026-10 不确定）。
- **链接**: [Introducing Mistral Large 4](https://mistral.ai/news/mistral-large-4/), [docs.mistral.ai/models/mistral-large-4](https://docs.mistral.ai/models/mistral-large-4-0)

## 7. Qwen (Alibaba) — Qwen4-Max

- **发布机构**: Alibaba Cloud (community.alibabacloud.com)
- **模型系列**: Qwen4-Max (Qwen4 架构)
- **发布日期**: 2026-11-16（Alibaba Unveils Qwen4-Max 公告）/ 2026-11-17（Enterprise "Qwen4-Max to the Enterprise: An AI Colleague"）
- **核心参数（社区博客核验）**:
  - 参数量: **总参 2.4T / 激活 71B**；上下文 **1M**；原生视觉（native vision）
  - 架构（来自 wiki 既有口径 + 官网）: **Gated DeltaNet + Qwen Sparse Attention + Gated Residual + N-gram embedding (328B)**
  - 安全指标: Last Secure Code Bench 安全功能性通过率 **31.8%** vs Qwen3.8-Max **22.0%**
- **主要创新点（含关注点）**:
  - **大模型新架构**: **Gated DeltaNet + Qwen Sparse Attention + Gated Residual + N-gram embedding**（wiki 既有口径）。
  - **训练方法/缩放**: Qwen4 架构，总 2.4T/激活 71B（有效配置）；Live Delivery；2.4T 规模下激活比例约 30%。
  - **长上下文**: 1M context lossless（官网原话 "up to 1M-token lossless context"）。
- **链接**: [Alibaba Unveils Qwen4-Max](https://community.alibabacloud.com/blog/alibaba-unveils-qwen4-max-new-ai-teammate-for-work-creativity-and-discovery_603783), [Qwen4-Max to the Enterprise](https://community.alibabacloud.com/blog/alibaba-cloud-brings-qwen4-max-to-the-enterprise-an-ai-colleague-that-plans-builds-and-delivers-finished-work_603786)

## 8. 01.AI (Yi)

- **发布机构**: 01.AI (Beijing)
- **模型系列**: TrueNorth AI Decision Platform（2026-07 发布）+ Boss AI、Investor AI、TopSales AI；Yi-Lighting (2024-10, 100B MoE, LMSYS 全球第 6)
- **发布日期**: 2026-07（TrueNorth）；Yi-Lighting 2024-10
- **核心参数**: 参数量 **Yi-Lighting 100B MoE**；企业决策平台为政定制。
- **主要创新点（含关注点）**:
  - **企业 AI 决策平台**（CEO 主导, FDE 共创）：Boss AI（决策助手）、Investor AI、TopSales AI。
  - **训练/评估**: Yi-Lighting 100B MoE，LMSYS 排名全球第 6、中国第 1；训练口径：100B 量级。
- **链接**: [01.AI](https://www.01.ai), [Yi-Lighting release (2024-10)](https://www.01.ai)

## 9. Baichuan — 未发现 2026 新技术报告（已知最新）

- **发布机构**: Baichuan (Baichuan Inc.)
- **模型系列**: 未发现 2026 新增 Tech Report（官网/网页均无 2026-11 级技术报告记录）
- **发布日期**: 未知（已知：Baichuan-Omni-1.5, arXiv:2501.15368, 2025-01-26；Baichuan-Omni, arXiv:2410.08565, 2024-10-11）
- **核心参数**: 已知：Baichuan-Omni-1.5 / Baichuan-Omni 系列（见 arXiv）
- **主要创新点（含关注点）**: Baichuan-Omni 系列（Baichuan-Omni 2025, Baichuan-Omni-1.5 2026? 站点在搜索中被网页反爬拦截，未获取官网数据；基于 arXiv 索引记录）
- **链接**: [Baichuan-Omni-1.5 (arXiv:2501.15368)](https://arxiv.org/abs/2501.15368)

## 10. Microsoft (Phi) — Microsoft AI 系列（2026-11-17 Microsoft Ignite）

- **发布机构**: Microsoft AI (New Microsoft AI site, microsoft.ai)
- **模型系列**: MAI 新系列（MAI Thinking 1、MAI Code 2/Code 2 Flash、MAI Cyber 2 Flash、MAI Image 2.7、MAI Transcribe、MAI Voice、MAI Realtime 1、MAI Licensed Weights + Custom Models）；Microsoft Phi family（Azure/Foundry Models，60M+ downloads）
- **发布日期**: 2026-11-17（"Seven new world-class models at scalable price-performance", Microsoft Ignite 2026）
- **核心参数（已知项）**: 参数量: **未公开（Foundry Models 对 Phi 未公布具体参数；已知有 60M+ downloads 认可）**
- **主要创新点（含关注点）**:
  - **MAI Realtime 1**: $0.01/audio minute（新语音 AI, Nov 11 announcement per site）。
  - **MAI Cyber 2 Flash**: "Leading security. Lower cost"；MAI Thinking 1；MAI Code 2 + Code 2 Flash（"Everyday coding at scalable prices"）。
  - **Phi family**: Azure/Foundry Models 提供（"Microsoft Phi on Foundry Models has over 60 million downloads"）；已知最新已知报告（wiki 既有口径）：Phi-4.1-mini / Phi-4.1-mini-flash-reasoning（2025）；窗口未发现新 2026 Phi 系统卡/技术报告。
- **链接**: [microsoft.ai/models](https://microsoft.ai/models/), [MAI Realtime 1](https://microsoft.ai/models/mai-realtime-1/), [Foundry Models (Phi)](https://azure.microsoft.com/en-us/products/ai-foundry/models/)

## 11. Apple — Apple Intelligence & Siri AI

- **发布机构**: Apple
- **模型系列**: Apple Intelligence（on-device AFM — Apple Foundation Models + Private Cloud Compute）+ Siri AI
- **发布日期**: apple.com/ai 页面（2026; features 列出新设备：iPhone 18 Pro, iPad Pro M1+, Mac M5/M6, Apple Vision Pro；Siri AI 在 WWDC 27 beta）
- **核心参数**: 参数量: **未公开**；上下文: unspecified（Apple 一般 unspecified）
- **主要创新点（含关注点）**:
  - **on-device + Private Cloud Compute**: iPhone 18 Pro/Duo (A20 Pro)、iPad Pro、Mac M3+/M5 Pro、Vision Pro (M5)；Siri AI 于 iOS/iPadOS/macOS/watchOS/visionOS 27 beta；Dictation on-device model; Image Playground；Visual Intelligence（camera Siri mode, screenshot srch, 跨 app smart actions）。
  - **多模态**: Visual Intelligence (photos/images, app actions, Apple Wallet cards import), Photo editing, Genmoji, Workout Buddy。
- **链接**: [Apple Intelligence & Siri AI](https://apple.com/ai/)

## 12. NVIDIA — Nemotron 3.5 Super（见第 4 节）

- **发布机构**: NVIDIA
- **模型系列**: NVIDIA Nemotron 3.5 Super（+ Llama Nemotron Super v1.5 (49B)/Ultra (253B)/Nano 2, terraform）
- **发布日期**: 2026-11-17 (arXiv:2611.22161); NVIDIA Technical Blog (2026-09-10, Nemotron 3 Ultra)
- **核心参数**: 总 120B, 激活 12B（arXiv 摘要）
- **主要创新点**: 微调 RL（纯 RL 后训练，Tinker CISPO LoRA）结果显著提升（见第 4 节）；Nemotron 3.5 Super VL NVFP4、Nemotron 权重更新（wiki 既有口径）。
- **链接**: [arXiv:2611.22161](https://arxiv.org/abs/2611.22161)

## 13. xAI (Grok)

- **发布机构**: xAI (SpaceXSI)
- **模型系列**: Grok 4.7（"SpaceXSI's most powerful model for coding and knowledge work. Twice as fast, at half the price of comparable models", 2026-09-22）, Grok Bot 1.0（2026-11-11）, Grok Voice 3.0（2026-10-14）
- **发布日期**: 2026-09-22（Grok 4.7）/ 2026-11-11（Grok Bot 1.0）
- **核心参数**: 参数量: **未公开**（xAI 的 Grok 历史均未公布参数数量）
- **主要创新点（含关注点）**:
  - **Grok 4.7**: agentic tasks 双倍速度, half the price of comparable models.
  - **Grok Bot 1.0**: team of always-on agents；Bot SDK（Automations, Workflows）。
  - Grok Voice 3.0, Grok Voice Transcribe 2.0, Grok Imagine 1.5（海外）。
- **链接**: [Grok 4.7](https://x.ai/news/grok-4-7), [Grok Bot 1.0](https://x.ai/news/grok-bot-1-0), [x.ai/news](https://x.ai/news/)

## 14. Amazon Nova — Nova 2 Lite / Nova 2 Sonic

- **发布机构**: Amazon Web Services (AWS)
- **模型系列**: Amazon Nova 2 Lite, Amazon Nova 2 Sonic（2025-12-02 AWS blog, 1M ctx, extended thinking low/med/high, web grounding + code interpreter）
- **发布日期**: 2025-12-02（AWS blog; wiki 既有记录）
- **核心参数**: 1M context；extended thinking levels；web grounding + code interpreter。
- **主要创新点（含关注点）**: Nova 文档定位更新至 V2（nova.amazon.com, nova.amazon.com/dev）；Nova 2 Lite/Sonic 进入 Bedrock Chat and Text playgrounds；v1 page 指向 Nova 2 user guide。
- **链接**: [Getting started with Amazon Nova 2](https://docs.aws.amazon.com/nova/latest/nova2-userguide/getting-started-nova-2.html)

## 15. Zhipu AI (GLM/ChatGLM) — GLM-5.3

- **发布机构**: Z.AI (北京智谱华章; 前身 zhipuai.cn)
- **模型系列**: GLM-5.3 (GLM-5V-Turbo, GLM-5-Turbo, AutoGLM, ZCode, Zread.ai, Z.ai)
- **发布日期**: 2026（z.ai 页面未标日期；wiki 2026-11-19 记录 GLM-5.3, 1M ctx）
- **核心参数**: 上下文 **1M**（"up to 1M-token lossless context"）；模型结构细节由 wiki 既有口径（Gated DeltaNet + Sparse Attention + Gated Residual + N-gram embedding 328B，基于 Qwen 同规模）
- **主要创新点（含关注点）**: "Open-source SOTA for coding, featuring up to 1M-token lossless context. Delivers more stable long-horizon task execution." + AutoGLM agent, GLM-OS 概念（2026-11-29 提出).
- **链接**: [Z.AI](https://z.ai), [zhipuai.cn/en](https://zhipuai.cn/en/)

## 16. InternLM (Shanghai AI Lab)

- **发布机构**: Shanghai AI Laboratory
- **模型系列**: InternLM3-8B-Instruct（2025-01-15）, Intern-S2-397B / Intern-S2-Preview-397B / Intern-S2-Preview-35B, Intern-S1 / Intern-S1-Pro / Intern-S1-mini (S1 系列), InternLM2.5-20B, InternLM-Math
- **发布日期**: InternLM3: 2025-01-15; Intern-S2/Intern-S1: GitHub 更新至 Nov 2026 (InternLM/Intern-S1 repo Updated Nov 17, 2026)
- **核心参数（精选）**: InternLM3-8B-Instruct (8B, deep-thinking mode); Intern-S2-397B (397B 参数级? 系列); Intern-S1 (多模态+科学推理, arXiv 2508.15763, 2025-08-28? Let me check — actually 2508.15763 — see InternLM/Intern-S1 page "Technical Report(S1)" and arXiv:2508.15763)
- **主要创新点（含关注点）**:
  - **训练方法**: InternLM3: 仅用 4 trillion 高质量数据（比同规模模型省 >75% 训练成本）；deep-thinking + 正常模式；Intern-S2: visual pretraining 新范式 + RL across 20+ 科学领域 + long-horizon agent RL; RULER 256K 文本上下文。
  - **多模态**: Intern-S2 科学多模态；Intern-S1 series（科学推理）。
- **链接**: [InternLM GitHub](https://github.com/InternLM), [InternLM/Intern-S1](https://github.com/InternLM/Intern-S1), [Intern-S1 (arXiv:2508.15763)](https://arxiv.org/abs/2508.15763), [Intern-S1-Pro (arXiv:2603.25040)](https://arxiv.org/abs/2603.25040)

## 17. Moonshot AI (Kimi) — Kimi K3.1 Pro

- **发布机构**: Moonshot AI
- **模型系列**: Kimi K3.1 Pro（"3-trillion-parameter-class model with 1M ctx"), Kimi K3（2026-07-16, 2.8T）, Kimi K3.1 Pro Highspeed（2-3× 速度）, Kimi K2.6
- **发布日期**: 2026-10-24（kimi.ai/blog/kimi-k3-1-pro; weights by Nov 4）
- **核心参数（官方数据）**: 参数量: **3T-class**（K3.1 Pro 是 3-trillion-parameter-class）；上下文: **1M**；其他: Hallu Bench claim-level hallucination 降 23.4%→8.3%（K3→K3.1 Pro）
- **主要创新点（含关注点）**:
  - **训练/RL**: 大规模 joint RL across hundreds of downstream domains；Internal: Terminal-Bench 4.0 65.7% (vs GPT-6 Astra 58.2, Claude Opus 5.5 66.4), Kimi Code Bench 3.0 Long-horizon 61.2%, BenchCAD 92.7%；OfficeQA Pro v2 64.4；Hallucination rate halved（claim-level 23.4%→8.3%）。
  - **推理/多模态/3D**: 3D 建模（BenchCAD 92.7%, parametric modeling）; 科学推理（OfficeQA Pro v2 64.4, financial research, business ops, terminal coding）。
  - **安全**: xdev-bench-hard 81.0% (reduced cyber risk-reduction vs 90.5% no-mitigation); 数据清理 approach；Kimi Code（2026, B3.2W?）— 未表述。
- **链接**: [Introducing Kimi K3.1 Pro](https://www.kimi.ai/blog/kimi-k3-1-pro), [Kimi K3.1 Pro (模型)](https://www.kimi.ai/ai-models/kimi-k3-1-pro)

## 18. StepFun (阶跃星辰)

- **发布机构**: StepFun (官方 GitHub stepfun-ai; 中文站 stepfun.com, 站点无可用公告)
- **模型系列**: Step-5-Preview（flagship, agentic work）, Step-3.7-Flash（high-efficiency Flash for real-world agents), Step-3.5-Flash, Step-Code (IDE?), Step-Audio 2, Step-Video-T2V / Step-Video-TI2V, SteptronOss (training framework), Step1X-Edit
- **发布日期**: Step-5-Preview 更新 Nov 9, 2026; Step-Code 更新 Nov 21, 2026; SteptronOss 更新 Sep 4, 2026; Step-Audio 2 (arXiv 2507.16632, 2025-07-22)
- **核心参数**: 未公开（StepFun 站点未找到 2026 LLM 参数公布页）
- **主要创新点（含关注点）**: Step-5-Preview/Step-3.7-Flash/Step-3.5-Flash 为 agentic LLM（训练框架 SteptronOss）; arXiv Step-Audio 2（2025）搜寻结果。
- **链接**: [stepfun-ai GitHub](https://github.com/stepfun-ai), [Step-Audio 2 (arXiv:2507.16632)](https://arxiv.org/abs/2507.16632)

## 19. ByteDance (豆包/Doubao)

- **发布机构**: ByteDance (bytedance.com)
- **模型系列**: Dreamina Seedance 2.5（2026-07-31, Newsroom 新闻稿）, Doubao（logo/首页）
- **发布日期**: 2026-07-31（Dreamina Seedance 2.5, wiki 既有口径）
- **核心参数**: 未公开（ByteDance 产品线无 2026 LLM 参数口径）
- **主要创新点（含关注点）**: 视频模型, 新闻稿通过 bytedance.com；Doubao 同家族 AI 产品线。
- **链接**: [ByteDance](https://www.bytedance.com), [Doubao](https://www.doubao.com/ai)

---

## 重点关注汇总（趋势口径）

- **大模型新架构**: 深度高 MoE（NVIDIA Nemotron 3.5 Super, Qwen4-Max）; 非对称 MoE/Causal-Encoder-Decoder（DeepSeek V4.1 Flash: 8B/16B 激活）; 混合 Mamba/Transformer + 注意力稀疏（Mistral Large 4, NVIDIA Nemotron 3.5 Super, GLM-5.3）; 全新架构内容：kimi K3.1 Pro 等产品线投资。
- **训练方法**: RL 主导后训练（NVIDIA CISPO/Tinker, Kimi 大规模联合 RL, OpenAI System Card 对齔/安全指标）; 中小模型分层与轻量化（GPT-6.2 Sol 现有记录）。
- **Scaling Law / 缩放分析**: NVIDIA 反向扩展做 reasoning effort 下降（技术博客, 2025 以前）; GPU-larger/激活不同: NVIDIA 用 22K tokens vs 上游 58K；AI Self-Improvement High 标准（OpenAI）。
- **多模态模型**: DeepSeek V4.1 Flash（原生视觉理解, V4 预览 1M 上下文）; Kimi K3.1 Pro（3D 建模/多模态, parametric modeling, synthetic 3D assets）; Mistral Large 4（多模态输入输出, 150 国语言）; NVIDIA Nemotron 3.5 Super（混合 MoE+Mamba, 长文档/图表/PDF 理解）; OpenAI GPT-6.2 Astra/Sol（slides/spreadsheets/documents/结构化输出, GDP.pdf 等）; Anthropic Fable 5.2/Mythos 5.2（vision + 科学任务, e.g. 脱氧核糖核酸/蛋白键设计, Hardware Engineering, 33-capability 数学领域）; Apple（Siri AI/Visual Intelligence on-device + Private Cloud Compute, iPhone 18 Pro/iPad Pro/Mac M6/Vision Pro 等设备列表）。
- **长上下文模型**: Gemini 4 Neon (1M); Qwen4-Max (1M); Kimi K3.1 Pro (1M); NVIDIA 既有 NVIDIABing?.
- **推理模型 / reasoning model**: OpenAI GPT-6.2 Astra/Sol (Reasoning); NVIDIA Nemotron 3.5 Super (RL); DeepSeek V4.1 Flash（KV 缩小, reasoning?）; Kimi K3.1 Pro (3T-class); Anthropic Fable 5.2/Mythos 5.2。
