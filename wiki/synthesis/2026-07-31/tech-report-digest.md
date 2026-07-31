---
title: "大模型技术报告摘要（2025-2026）| LLM Tech Report Digest (2025-2026)"
type: synthesis
created: 2026-07-31
updated: 2026-07-31
tags: [tech-report, system-card, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, bytedance, zhipu, kimi, internlm, baichuan, stepfun]
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告 / System Card 汇总。
> 更新日期：2026-07-31

---

## 1. DeepSeek（深度求索）

### 1.1 DeepSeek-V4

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4：迈向高效百万 token 上下文智能 |
| **英文标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **发布机构** | DeepSeek-AI |
| **模型系列** | DeepSeek-V4-Pro / V4-Flash / V4-Pro-Max / V4-Flash-Max |
| **发布日期** | 2026-04-24（预览）/ 2026-04-26（技术报告） |
| **架构** | MoE；V4-Pro（1.6T 总参，49B 激活）；V4-Flash（284B 总参，13B 激活） |
| **训练数据** | 32T+ tokens |
| **上下文长度** | 1M（默认），384K 最大输出 |
| **核心创新** | CSA（Compressed Sparse Attention，token 级压缩 + DSA，KV 压缩 4:1）+ DeepSeek Sparse Attention；thinking / non-thinking 双模式；兼容 OpenAI 与 Anthropic API 格式；MIT 开源；V4-Pro-Max SWE-bench Verified 80.6%（开源最高，llm-stats 2026-06），LiveCodeBench 93.5、MMLU-Pro 87.5、GPQA Diamond 90.1（官方自报） |
| **论文** | https://arxiv.org/abs/2606.19348 |

### 1.2 DeepSeek-V3.2

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V3.2：推动开源大语言模型前沿 |
| **英文标题** | DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models |
| **发布机构** | DeepSeek |
| **模型系列** | DeepSeek-V3.2 / V3.2-Speciale |
| **发布日期** | 2025-12 |
| **架构** | MoE + DSA（DeepSeek Sparse Attention） |
| **核心创新** | DSA 稀疏注意力显著降低计算复杂度；大规模 RL 训练（超过预训练计算量的 10%）；Agentic 任务合成 pipeline；V3.2-Speciale 在 IMO 2025 和 IOI 2025 获得金牌级别成绩 |
| **论文** | https://arxiv.org/abs/2512.02556 |

### 1.3 Thinking with Visual Primitives（多模态推理新范式）

| 项目 | 内容 |
|------|------|
| **中文标题** | 基于视觉原语进行思考（Thinking with Visual Primitives） |
| **英文标题** | Thinking with Visual Primitives |
| **发布机构** | DeepSeek-AI 联合北京大学、清华大学 |
| **模型系列** | 基于 DeepSeek-V4-Flash 的多模态推理框架 |
| **发布日期** | 2026-04-30 |
| **核心创新** | 提出 "Reference Gap"（参照鸿沟）问题——自然语言无法精确定位稠密空间布局；将 points / bounding boxes 作为最小思维单元直接穿插进推理轨迹（"边推理边指"）；基于 DeepSeek-V4-Flash 的 CSA，将每 4 个视觉 token 的 KV cache 压缩为 1 项，极大降低图像 token 消耗；在 counting、spatial reasoning 等基准上匹敌 GPT-5.4、Claude Sonnet 4.6、Gemini 3 Flash；推理范式：Pretraining → 专家化 SFT → 专家化 RL → Unified RFT → On-Policy Distillation |
| **链接** | https://github.com/deepseek-ai/Thinking-with-Visual-Primitives |

### 1.4 DeepSeek-V3 / R1 / V3.1（历史条目）

- **DeepSeek-V3**（2024-12-27）：MoE 671B/37B 激活，14.8T tokens，128K 上下文；MLA + DeepSeekMoE，辅助损失-free 负载均衡，MTP 训练目标。https://arxiv.org/abs/2412.19437
- **DeepSeek-R1**（2025-01-01）：纯 RL 推理（R1-Zero 无 SFT）；GRPO 算法；多阶段训练 pipeline。https://arxiv.org/abs/2501.12948
- **DeepSeek-V3.1**（2025-08-21）：Hybrid Thinking 混合推理模式；840B tokens 继续预训练。https://api-docs.deepseek.com/news/news250821/

---

## 2. OpenAI

### 2.1 GPT-5.5 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.5 系统卡 |
| **英文标题** | GPT-5.5 System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.5 / GPT-5.5 Pro（同模型 + 并行 test-time compute 设置） |
| **发布日期** | 2026-04-23 |
| **核心创新** | 面向复杂真实世界工作设计；完整 predeployment safety evals（Preparedness Framework）；约 200 家早期访问合作伙伴实测；系统卡在 OpenAI 官网与 Deployment Safety 页面双渠道发布 |
| **论文** | https://openai.com/index/gpt-5-5-system-card/ ；全文 https://deploymentsafety.openai.com/gpt-5-5 |

### 2.2 GPT-5.6 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 系统卡 |
| **英文标题** | GPT-5.6 System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（Sol / Terra / Luna） |
| **发布日期** | 2026-07-09 |
| **核心创新** | 三个模型家族（旗舰 Sol、经济 Terra、快速 Luna）；CoT-Control 思维链可控性；Preparedness Framework 评估；推理 effort 曲线报告 |
| **论文** | https://deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf |

### 2.3 GPT-5 / GPT-5.3-Codex（历史条目）

- **GPT-5 System Card**（2025-08-13）：统一系统（router 自动切换 fast/thinking）；safe-completions 安全训练；幻觉比 o3 少约 6 倍；AIME 2025 94.6%、SWE-bench 74.9%。https://cdn.openai.com/gpt-5-system-card.pdf
- **GPT-5.3-Codex System Card**（2026-02-05）：最强 Agentic Coding 模型；首次在网络安全领域标记为 High capability。https://cdn.openai.com/pdf/23eca107-a9b1-4d2c-b156-7deb4fbc697c/GPT-5-3-Codex-System-Card-02.pdf

---

## 3. Meta AI (LLaMA)

### 3.1 Llama 4

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama 4 系列：架构、训练、评估与部署 |
| **英文标题** | The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes |
| **发布机构** | Meta AI |
| **模型系列** | Llama 4 Scout (17Bx16E) / Maverick (17Bx128E) / Behemoth (288B 激活, ~2T 总参) |
| **发布日期** | 2025-04-05 |
| **架构** | MoE（首次 Llama 使用 MoE）；early-fusion 原生多模态 |
| **训练数据** | Scout: ~40T tokens；Maverick: ~22T tokens |
| **上下文长度** | Scout: 10M；Maverick: 1M |
| **核心创新** | iRoPE 架构（interleaved attention + RoPE）支持超长上下文；Scout 可在单张 H100 部署；Behemoth 作为 teacher 进行 co-distillation |
| **论文** | https://arxiv.org/abs/2601.11659 |

> ⚠️ **注意**：Llama 4 Herd 论文（arXiv:2601.11659）已被 arXiv 撤回/标记为 "Redacted by arXiv"，无法获取正式 PDF 版本。以上条目基于 2025-04 官方发布信息与第三方报道整理。

---

## 4. Google DeepMind (Gemini)

### 4.1 Gemini 3.6 Flash Model Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 3.6 Flash 模型卡 |
| **英文标题** | Gemini 3.6 Flash — Model Card |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3.6 Flash（基于 Gemini 3.5 Flash） |
| **发布日期** | 2026-07-21 |
| **上下文长度** | 1M token 输入，64K 输出 |
| **核心创新** | 效率型发布：比 3.5 Flash 少约 17% 输出 token 完成相同任务（DeepSWE 某些任务最多省 65%）；DeepSWE 49%（较 3.5 Flash 37% +12pt）；OSWorld-Verified 83%（内置 computer use 工具）；MLE-Bench 63.9%（所有跟踪模型中最高）；内置 computer use（浏览器/桌面自动化）；知识截止 2026-03；定价 $1.50/$7.50（与 3.5 Flash 相同，输出更便宜） |
| **论文** | https://deepmind.google/models/model-cards/gemini-3-6-flash/ ；PDF https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-6-Flash-Model-Card.pdf |

### 4.2 Gemini 3.5 Flash-Lite & 3.5 Flash Cyber

| 项目 | 内容 |
|------|------|
| **英文标题** | Gemini 3.5 Flash-Lite / 3.5 Flash Cyber |
| **发布机构** | Google DeepMind |
| **发布日期** | 2026-07-21（与 3.6 Flash 同日） |
| **核心创新** | 3.5 Flash-Lite：最快速 Flash 级模型（350 tok/s，$0.30/$2.50），内置 computer use，Terminal-Bench 2.1 54%（vs 3.1 Flash-Lite 31%），GDM-MRCR v2 72.2%，GDPval-AA v2 1140；在 SWE-Bench Pro 与 OSWorld 上超过 Gemini 3 Flash；3.5 Flash Cyber：安全增强版，定位 CodeMender 漏洞挖掘/修复场景 |
| **链接** | https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/ |

### 4.3 Gemini 2.5（历史条目）

- **Gemini 2.5**（2025-07-07）：原生多模态；>1M token 上下文；Deep Think 技术（并行推理）；AIME 2025 88.0%；可处理 3 小时视频。https://arxiv.org/abs/2507.06261

---

## 5. Anthropic (Claude)

### 5.1 Claude Mythos Preview System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Mythos Preview 系统卡 |
| **英文标题** | Claude Mythos Preview System Card |
| **发布机构** | Anthropic |
| **模型系列** | Claude Mythos Preview（Claude 前沿系列） |
| **发布日期** | 2026-04-07（244 页系统卡） |
| **核心创新** | 2026 年 4 月时的前沿模型，未公开部署；因自主网络安全（autonomous cybersecurity）能力集群，通过 "Project Glasswing" 仅向经审核的安全合作伙伴开放；SWE-bench Verified 93.9%（llm-stats，受限访问）；后因美国商务部出口管制，于 2026-06-12 与 Fable 5 一同下线，2026-07-01 恢复 Fable 5，Mythos 5 仍仅限授权伙伴 |
| **链接** | https://www.anthropic.com/system-cards |

### 5.2 Claude Opus 5 / Sonnet 5 / Fable 5（2026 系列）

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 5 发布 |
| **英文标题** | Claude Opus 5 launch |
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 5（2026-07-24）；Claude Sonnet 5（2026-06-30）；Claude Fable 5（2026-06-09） |
| **发布日期** | Opus 5: 2026-07-24 |
| **核心创新** | Opus 5：主动式（proactive）模型，接近 Fable 5 的前沿智能，价格为 Fable 5 的一半；Arena Elo (Code) 1673（#2，仅次于 Kimi K3 1679）；Fable 5：SWE-bench Verified 95.5%、BullshitBench v2 95%（全局 #1），因出口管制 6/12 下线、7/1 恢复；Sonnet 5：2026-06-30 |
| **链接** | https://www.anthropic.com/system-cards |

### 5.3 后续 Claude 版本时间线

| 模型 | 发布日期 |
|------|----------|
| Claude Opus 4.1 | 2025-08 |
| Claude Sonnet 4.5 | 2025-09 |
| Claude Haiku 4.5 | 2025-10 |
| Claude Opus 4.5 | 2025-11 |
| Claude Opus 4.6 | 2026-02 |
| Claude Sonnet 4.6 | 2026-02 |
| Mythos Preview | 2026-04 |
| Claude Opus 4.7 | 2026-04 |
| Claude Opus 4.8 | 2026-05 |
| Claude Fable 5 | 2026-06-09（6/12-7/1 出口管制下线） |
| Claude Sonnet 5 | 2026-06-30 |
| Claude Opus 5 | 2026-07-24 |

**系统卡索引**: https://www.anthropic.com/system-cards

---

## 6. Mistral AI

### 6.1 Mistral Large 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral Large 3 技术文档 |
| **英文标题** | Mistral Large 3 Technical Documentation |
| **发布机构** | Mistral AI |
| **模型系列** | Mistral Large 3 / Ministral 3 (3B/8B/14B) |
| **发布日期** | 2025-12-02 |
| **架构** | Granular MoE（675B 总参数，41B 激活 + 2.5B Vision Encoder） |
| **上下文长度** | 256K |
| **核心创新** | Mistral 首个大规模 MoE（继 Mixtral 系列后）；Apache 2.0 开源；原生多模态视觉理解；多语言支持；与 NVIDIA 合作优化 |
| **链接** | https://mistral.ai/news/mistral-3/ |

---

## 7. Qwen（阿里通义千问）

### 7.1 Qwen3.5-Omni

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.5-Omni 技术报告 |
| **英文标题** | Qwen3.5-Omni Technical Report |
| **发布机构** | Alibaba（Qwen Team） |
| **模型系列** | Qwen3.5-Omni（Plus / Flash） |
| **发布日期** | 2026-04-22（arXiv） |
| **架构** | Hybrid Attention Mixture-of-Experts（混合注意力 MoE）；Thinker-Talker 架构（源自 Qwen2.5-Omni） |
| **训练数据** | 异构文本-视觉对 + 1 亿+小时音视频内容 |
| **上下文长度** | 256K |
| **核心创新** | 参数量可扩展到数千亿级；相对 Qwen3-Omni 五大升级；Qwen3.5-Omni-Plus 在 215 项 audio / audio-visual 子任务中 SOTA，关键音频任务超越 Gemini 3.1 Pro；原生 omni agent（WebSearch、FunctionCall、语音输出、实时流式）；Vibe Coding 能力 |
| **论文** | https://arxiv.org/abs/2604.15804 |

### 7.2 Qwen3 / Qwen3.5（历史条目）

- **Qwen3**（2025-05-14）：统一 thinking / non-thinking；119 种语言；235B-A22B 旗舰超越 DeepSeek-R1/V3；36T tokens；Apache 2.0。https://arxiv.org/abs/2505.09388
- **Qwen3.5**（2026-02-16）：397B-A17B 等；原生多模态 Agent；Thinker-Talker 升级。https://qwen.ai/blog?id=qwen3.5
- **Qwen3.8 Max**（2026-07 前后）：2.4T 参数（参考投资日报/技术报告速递记录，待正式技术报告确认）

---

## 8. Microsoft (Phi)

### 8.1 Phi-4 系列

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4 技术报告 |
| **英文标题** | Phi-4 Technical Report |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4 (14B) / Phi-4-reasoning (14B) |
| **发布日期** | Phi-4: 2024-12-12；Phi-4-reasoning: 2025-04-30 |
| **核心创新** | 数据质量优先预训练；大规模合成数据（multi-agent prompting、self-revision、instruction reversal）；STEM QA 超越 teacher（GPT-4）；Phi-4-reasoning 从 o3-mini 蒸馏 + SFT + outcome-based RL，超越 DeepSeek-R1-Distill-Llama-70B |
| **论文** | https://arxiv.org/abs/2412.08905 ；https://arxiv.org/abs/2504.21318 |

---

## 9. Apple

### 9.1 Apple Intelligence Foundation Language Models

| 项目 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型 2025 技术报告 |
| **英文标题** | Apple Intelligence Foundation Language Models: Tech Report 2025 |
| **发布机构** | Apple |
| **模型系列** | On-Device (~3B) / Server (PT-MoE) |
| **发布日期** | 2025-07-17 |
| **核心创新** | On-device: KV-cache sharing + 2-bit QAT；Server: Parallel-Track MoE (PT-MoE) + interleaved global-local attention；Private Cloud Compute；Swift Foundation Models framework |
| **论文** | https://arxiv.org/abs/2507.13575 |

---

## 10. NVIDIA

### 10.1 Nemotron 3 Super

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Super 技术报告 |
| **英文标题** | NVIDIA Nemotron 3 Super Technical Report |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 Super（120B 总参，12B 激活） |
| **发布日期** | 2026-03-10 |
| **架构** | MoE + Hybrid Mamba-Transformer；LatentMoE |
| **核心创新** | Nemotron 3 系列首个基于 LatentMoE 的模型；随报告开源 RL 环境与 SFT 数据集以支持 agentic 能力；与 Nemotron 3 Ultra / Nano 构成完整系列 |
| **论文** | https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf |

### 10.2 Nemotron 3 Ultra / Nano（历史条目）

- **Nemotron 3 Ultra**（550B-A55B）：Hybrid Mamba-Attention + LatentMoE + MTP；NVFP4 预训练（最大规模验证）；MOPD 多教师在线策略蒸馏；推理吞吐量比 GLM-5.1 高 5.9x。https://research.nvidia.com/labs/nemotron/
- **Nemotron 3 Nano**（30B-A3B，2025-12-23）：Mamba-2 + GQA + MoE；25T tokens；1M 上下文；LV 训练（multi-environment RLVR + RLHF）；吞吐量 3.3x。
- **Llama-Nemotron**（2025-05-02）：NAS + FFN Fusion；LN-Ultra (253B) 超越 DeepSeek-R1。https://arxiv.org/abs/2505.00949

---

## 11. xAI (Grok)

### 11.1 Grok 4.20 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.20 系统卡 |
| **英文标题** | Grok 4.20 System Card |
| **发布机构** | xAI |
| **模型系列** | Grok 4.20（单代理 SA 模式 / 多代理 MA 模式） |
| **发布日期** | 2026-04-07 |
| **核心创新** | 高级推理 + 多代理能力，两种运行模式；预训练数据（公开数据 + 第三方数据 + 内部数据）+ 定向 mid-training；SFT + RL（人类与合成 reward 信号）post-training；按 Frontier AI Framework (FAIF) 沿风险轴评估：恶意使用、失控、CBRN、网络安全、有害操纵 |
| **论文** | https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf |

### 11.2 Grok 3（历史条目）

- **Grok 3**（2025-02-19）：Colossus 超算训练；大规模 RL 推理（Think 模式）；DeepSearch Agent；AIME 2025 93.3%（cons@64）。https://x.ai/news/grok-3

---

## 12. Amazon (Amazon Nova)

### 12.1 Amazon Nova

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 模型家族：技术报告与模型卡 |
| **英文标题** | The Amazon Nova Family of Models: Technical Report and Model Card |
| **发布机构** | Amazon AGI |
| **模型系列** | Nova Pro / Lite / Micro / Canvas / Reel |
| **发布日期** | 2025-06（arXiv） |
| **核心创新** | 多模态（text/image/video/document）；200+ 语言支持；视频理解首个在 Bedrock 提供；Canvas 图像生成 + Reel 视频生成；SFT + DPO + PPO 对齐 |
| **论文** | https://arxiv.org/abs/2506.12103 |

---

## 13. ByteDance (字节跳动 / 豆包 / Doubao)

### 13.1 Seed 系列技术报告

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed 系列模型技术报告 |
| **英文标题** | ByteDance Seed Series Technical Reports |
| **发布机构** | ByteDance Seed |
| **模型系列** | Seed2.0 Pro / Lite / Mini；Seed1.5-VL；Seed-Thinking-v1.5；Seedream 2.0；Seedance 2.0 |
| **发布日期** | 2025-04 ~ 2026-04 |
| **核心创新** | Seed2.0（2026-02）：全模态理解（video/image/audio/text）+ Agent 能力升级，Lite 为首个全模态理解模型；Seed1.5-VL：SeedViT + MLP Adapter + LLM，多模态 Scaling Law，60 个公开 benchmark 中 38 个 SOTA；Seed-Thinking-v1.5：Dual-track reward + HybridFlow + SRS 提速 3x；Seedream 2.0（arXiv:2503.07703）：文生图，中英双语，text rendering 强；Seedance 2.0（arXiv:2604.14148）：视频生成 |
| **链接** | Seedream 2.0 https://arxiv.org/abs/2503.07703 ；Seedance 2.0 https://arxiv.org/abs/2604.14148 ；Seed1.5-VL https://arxiv.org/abs/2505.07062 |

---

## 14. Zhipu AI（智谱 AI）

### 14.1 GLM-5.2

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5.2：为长时程任务而生 |
| **英文标题** | GLM-5.2: Built for Long-Horizon Tasks |
| **发布机构** | Zhipu AI（智谱 AI / Z.ai） |
| **模型系列** | GLM-5.2（HOT 版本）/ GLM-5.1 / GLM-5 / GLM-5-Turbo / GLM-4.7 / GLM-4.6 / GLM-4.5 |
| **发布日期** | 2026-06-13 首发（Coding Plan），2026-06-16 官方博客，6 月下旬 API / MIT 权重开放 |
| **架构** | MoE（744B 总参数，40B 激活） |
| **上下文长度** | 1M token |
| **核心创新** | 四大架构创新：IndexShare、KVShare、LayerSplit、HiSparse（128K→1M 工程路径）；面向长时程（long-horizon）任务显著超越 GLM-5.1；在 SWE-bench Pro、FrontierSWE 等长任务编码榜单逼近 Claude Opus 4.8；API 成本约为 GPT-5.5 的 1/6；MIT 开源；发布于 Anthropic Fable 5/Mythos 5 因出口管制下线（6/12）仅 5 天后，承接开源替代需求 |
| **链接** | https://z.ai/blog/glm-5.2 ；https://docs.bigmodel.cn/cn/guide/models/text/glm-5.2 |

### 14.2 GLM-5（历史条目）

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5：从 Vibe Coding 到 Agentic Engineering |
| **英文标题** | GLM-5: From Vibe Coding to Agentic Engineering |
| **发布机构** | Zhipu AI & Tsinghua University |
| **模型系列** | GLM-5 (744B total, 40B active) |
| **发布日期** | 2026-02-12 |
| **架构** | MoE + DSA（DeepSeek Sparse Attention） |
| **训练数据** | 28.5T tokens |
| **核心创新** | DSA 降低注意力计算 1.5-2x；异步 RL 基础设施（slime 框架）；异步 Agent RL 算法；Muon Split（MLA+Muon 兼容方案）；参数共享多 token 预测（接受长度比 DeepSeek-V3 高 ~8%）；SWE-bench Verified 77.8%、BrowseComp 75.9%；幻觉率创纪录新低（34%）；全栈适配国产 GPU（华为昇腾等 7 款芯片）；MIT 开源 |
| **论文** | https://arxiv.org/abs/2602.15763 |

---

## 15. Moonshot AI（月之暗面 / Kimi）

### 15.1 Kimi K2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2.5 技术报告 |
| **英文标题** | Kimi K2.5 Technical Report |
| **发布机构** | Moonshot AI (Kimi) |
| **模型系列** | Kimi K2 / K2.5（万亿参数 MoE LLM 系列） |
| **发布日期** | 2026-01（K2.5） |
| **核心创新** | 原生多模态视觉（MoonViT-3D）；"Agent Swarm Mode" 可并行协调最多 100 个子代理；agentic 基准较 K2 Thinking 提升 59.3%；K2（2025-07-28）：MuonClip 优化器（QK-clip）、15.5T tokens 零 loss spike、SWE-bench Verified 65.8%、开源；Moonshot 2025-12 完成 $5 亿 C 轮（估值 $43 亿） |
| **论文** | https://arxiv.org/abs/2507.20534 ；K2.5 tech report https://github.com/MoonshotAI/Kimi-K2.5 |

---

## 16. InternLM（上海 AI 实验室 / 上海人工智能实验室）

### 16.1 InternLM3 / Intern-S1-Pro

| 项目 | 内容 |
|------|------|
| **中文标题** | InternLM3 / Intern-S1-Pro |
| **英文标题** | InternLM3 / Intern-S1-Pro |
| **发布机构** | Shanghai AI Laboratory |
| **模型系列** | InternLM3-8B-Instruct；Intern-S1-Pro（1T MoE，科学推理） |
| **发布日期** | InternLM3: 2025-01-15 |
| **训练数据** | InternLM3: 4T tokens（仅同类 1/4 成本） |
| **核心创新** | InternLM3 数据效率革命；Thinking Density（IQPT）指标；通用-专家融合数据合成；Intern-S1-Pro 专注科学（science）推理的 1T MoE |
| **链接** | https://internlm.readthedocs.io/en/latest/model_card/InternLM3.html |

---

## 17. Baichuan（百川智能）

### 17.1 Baichuan-M4 / Baichuan4-Finance

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan-M4 / Baichuan4-Finance 技术报告 |
| **英文标题** | Baichuan-M4 Technical Report / Baichuan4-Finance Technical Report |
| **发布机构** | Baichuan Inc. |
| **模型系列** | Baichuan-M4（2026-06 前后，幻觉率约 3.3%）；Baichuan4-Finance |
| **发布日期** | Baichuan4-Finance: 2024-12-17 |
| **核心创新** | Baichuan4-Finance：金融领域 LLM；Domain Self-Constraint 继续预训练；双 Scaling Law 确定数据配比；SFT + RLHF + AI Feedback。Baichuan-M4：极低幻觉率（~3.3%），详见 2026-07 技术报告速递记录 |
| **论文** | https://arxiv.org/abs/2412.15270 ；Baichuan-M4 https://arxiv.org/abs/2606.12721 |

---

## 18. StepFun（阶跃星辰）

### 18.1 Step 3 / Step 3.5 Flash / Step 3.7 Flash

| 项目 | 内容 |
|------|------|
| **中文标题** | Step 系列技术报告 |
| **英文标题** | Step Technical Report |
| **发布机构** | StepFun（阶跃星辰） |
| **模型系列** | Step-3 / Step-3.5 Flash / Step-3.7 Flash |
| **发布日期** | Step-3: 2025-07-31 开源；Step-3.5 Flash: 2026-02-02 开源基座；Step-3.7 Flash: 2026 年中 |
| **核心创新** | Step-3：千亿参数多模态推理模型，MMMU / MathVision / SimpleVQA / AIME 2025 / LiveCodeBench 开源多模态推理 SOTA；解码效率为 DeepSeek-R1 的 300%（国产芯片）、NVIDIA Hopper 上吞吐 +70%；Step-3.5 Flash：高效开源基座；Step-3.7 Flash（196B，约 400 TPS）；"1+N" 模型矩阵（11 个多模态模型覆盖语音/图像/视频）；2026-01 完成 50 亿元 B+ 轮融资，印奇（旷视创始人）任董事长 |
| **链接** | https://www.stepfun.com/ |

---

## 19. Yi / 01.AI（零一万物）

### 19.1 Yi-Lightning

| 项目 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **发布机构** | 01.AI（零一万物） |
| **模型系列** | Yi-Lightning / Yi-Lightning 2 / Yi-Large |
| **发布日期** | 2025 年底（Yi-Lightning）；Yi-Lightning 2（2026） |
| **核心创新** | 高效推理模型；MoE 架构；低成本高推理效率（详见 2026-07 技术报告速递中的 Yi-Lightning 2 条目） |
| **论文** | https://arxiv.org/abs/2412.01253 |

---

## 关键趋势分析

### 1. 架构趋势
- **MoE 成为绝对主流**：DeepSeek-V4（1.6T/49B）、GLM-5.2（744B/40B）、Llama 4、Qwen3.5-Omni、Mistral Large 3（675B/41B）、Kimi K2/K2.5（1T）、Nemotron 3 全系列
- **稀疏注意力成熟**：DeepSeek CSA+DSA 被 GLM-5 采用 DSA；GLM-5.2 演进为 IndexShare / KVShare / HiSparse 四件套
- **混合架构落地**：NVIDIA Nemotron 3 Super/Ultra/Nano 系列验证 Mamba-Transformer 混合 + LatentMoE
- **量化预训练**：NVFP4 预训练（Nemotron 3 Ultra）、2-bit QAT（Apple）

### 2. 推理 / Reasoning
- **Thinking/Non-Thinking 统一**：Qwen3、DeepSeek-V3.1/V4、GLM-5、GPT-5.6（CoT-Control）均支持推理模式切换与可控
- **RL 成为推理训练核心**：DeepSeek V4 / V3.2（RL 超预训练 10%）、Grok 4.20（SFT+RL）、Phi-4-reasoning（SFT+RL）
- **视觉推理新范式**：DeepSeek 以 points/boxes 作为思维单元（Visual Primitives），解决 Reference Gap

### 3. 多模态
- **原生多模态 + 全模态**：Qwen3.5-Omni（256K 上下文、1 亿+小时音视频）、Gemini 3.6 Flash（内置 computer use）、Kimi K2.5（MoonViT-3D）、Seed2.0
- **多模态生成**：Amazon Nova Canvas/Reel、ByteDance Seedream 2.0 / Seedance 2.0

### 4. Agent 能力
- **Agent 成为第一优先级**：GLM-5.2 定位 long-horizon 任务；GPT-5.5 面向复杂真实工作；Grok 4.20 单/多代理双模式；Kimi K2.5 Agent Swarm（100 子代理）
- **Agentic 评估成熟**：SWE-bench Verified / SWE-bench Pro / DeepSWE / OSWorld 成为标准指标（注意口径差异：DeepSeek V4 Pro 在 DeepSWE 仅 8% 而 SWE-bench 80.6%）
- **出口管制影响模型可得性**：Anthropic Fable 5/Mythos 5 因美商务部出口管制 6/12 下线、Fable 5 于 7/1 恢复——直接催化 GLM-5.2 开源承接

### 5. 长上下文
- **1M 上下文成为旗舰标配**：DeepSeek V4、Gemini 3.6 Flash、GLM-5.2、Nemotron 3、Kimi、Grok 均 1M+
- **10M 上限探索**：Llama 4 Scout（10M，iRoPE）
- **长上下文工程**：GLM-5.2 通过 IndexShare/KVShare/LayerSplit/HiSparse 实现 128K→1M

### 6. Scaling Law
- **Post-training Scaling**：DeepSeek-V3.2/V4 报告 RL 计算量已超预训练 10%+
- **数据效率**：InternLM3 以 4T tokens 实现 SOTA；DeepSeek V4 32T+；Qwen3.5-Omni 视频数据 1 亿+ 小时
- **效率驱动定价战**：DeepSeek V4-Flash $0.28/M 输出、Gemini 3.5 Flash-Lite $0.30/$2.50、GLM-5.2 为 GPT-5.5 的 1/6

---

## 论文索引

| # | 机构 | 模型 | arXiv ID | 日期 |
|---|------|------|----------|------|
| 1 | DeepSeek | DeepSeek-V4 | 2606.19348 | 2026-04 |
| 2 | DeepSeek | DeepSeek-V3 | 2412.19437 | 2024-12 |
| 3 | DeepSeek | DeepSeek-R1 | 2501.12948 | 2025-01 |
| 4 | DeepSeek | DeepSeek-V3.2 | 2512.02556 | 2025-12 |
| 5 | DeepSeek | Thinking with Visual Primitives | GitHub (技术报告 PDF) | 2026-04 |
| 6 | OpenAI | GPT-5.5 System Card | openai.com + deploymentsafety | 2026-04 |
| 7 | OpenAI | GPT-5.6 System Card | deploymentsafety.openai.com | 2026-07 |
| 8 | Meta | Llama 4 | 2601.11659（已撤回） | 2026-01 |
| 9 | Google | Gemini 3.6 Flash Model Card | deepmind.google/model-cards | 2026-07 |
| 10 | Google | Gemini 2.5 | 2507.06261 | 2025-07 |
| 11 | Anthropic | Claude Mythos Preview System Card | anthropic.com/system-cards | 2026-04 |
| 12 | Alibaba | Qwen3 | 2505.09388 | 2025-05 |
| 13 | Alibaba | Qwen3.5-Omni | 2604.15804 | 2026-04 |
| 14 | Microsoft | Phi-4 | 2412.08905 | 2024-12 |
| 15 | Microsoft | Phi-4-reasoning | 2504.21318 | 2025-04 |
| 16 | Apple | Apple Intelligence FM | 2507.13575 | 2025-07 |
| 17 | NVIDIA | Nemotron 3 Super TR | research.nvidia.com PDF | 2026-03 |
| 18 | NVIDIA | Llama-Nemotron | 2505.00949 | 2025-05 |
| 19 | xAI | Grok 4.20 System Card | data.x.ai PDF | 2026-04 |
| 20 | Amazon | Amazon Nova | 2506.12103 | 2025-06 |
| 21 | ByteDance | Seed1.5-VL | 2505.07062 | 2025-05 |
| 22 | ByteDance | Seedream 2.0 | 2503.07703 | 2025-03 |
| 23 | ByteDance | Seedance 2.0 | 2604.14148 | 2026-04 |
| 24 | Moonshot | Kimi K2 | 2507.20534 | 2025-07 |
| 25 | Zhipu AI | GLM-5 | 2602.15763 | 2026-02 |
| 26 | Zhipu AI | GLM-4.5 | 2508.06471 | 2025-08 |
| 27 | Baichuan | Baichuan4-Finance | 2412.15270 | 2024-12 |
| 28 | Baichuan | Baichuan-M4 | 2606.12721 | 2026-06 |
| 29 | 01.AI | Yi-Lightning | 2412.01253 | 2024-12 |
