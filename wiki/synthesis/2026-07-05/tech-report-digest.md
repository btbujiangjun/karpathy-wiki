---
title: "大模型技术报告摘要 — LLM Tech Report Digest (2026-07-05)"
type: synthesis
created: 2026-07-05
updated: 2026-07-05
sources: [web-search]
tags: [tech-report, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, yi, baichuan, microsoft, apple, nvidia, xai, amazon, zhipu, internlm, moonshot, bytedance, stepfun]
---

# 大模型技术报告摘要 — LLM Tech Report Digest

> 覆盖 20 家 AI 机构最新发布的大模型技术报告（Tech Report / System Card），每日更新。本文档为 2026-07-05 综合版。

## 2026-07-05 新增 / 更新

| 机构 | 新增内容 |
|------|---------|
| DeepSeek | **DeepSeek-V4** — 1T MoE, CSA/HCA, 1M context, 2026-05 |
| Anthropic | **Claude Opus 4.6 System Card** — ASL-3, 2026-02 |
| Qwen (Alibaba) | **Qwen3-VL** — 多模态视觉语言模型, 2025-11 |
| Microsoft | **Phi-4-Reasoning-Vision** (15B), arXiv:2603.03975 |
| xAI | **Grok 4** — 媒体报道, 无正式 arXiv 论文 |
| Moonshot AI | **Kimi K2** 补充 MuonClip 优化器、RLVR 训练细节 |

---

## 目录

1. [DeepSeek — V3 / R1 / V3.2 / V4](#1-deepseek)
2. [OpenAI — GPT-5 / o3 / o4-mini](#2-openai)
3. [Meta AI — Llama 4](#3-meta-ai)
4. [Google DeepMind — Gemini 2.5](#4-google-deepmind)
5. [Anthropic — Claude Opus 4 / Sonnet 4 / Opus 4.6](#5-anthropic)
6. [Mistral AI — Mistral Large 3 / Ministral 3](#6-mistral-ai)
7. [Qwen (Alibaba) — Qwen3 / Qwen3-VL](#7-qwen-alibaba)
8. [Yi (01.AI) — Yi-Lightning](#8-yi-01ai)
9. [Baichuan — Baichuan4](#9-baichuan)
10. [Microsoft — Phi-4 系列](#10-microsoft)
11. [Apple — Apple Intelligence Foundation Language Models](#11-apple)
12. [NVIDIA — Nemotron 3 系列](#12-nvidia)
13. [xAI — Grok 3 / Grok 4](#13-xai)
14. [Amazon — Amazon Nova](#14-amazon)
15. [Zhipu AI — GLM-5](#15-zhipu-ai)
16. [InternLM (Shanghai AI Lab) — InternLM3](#16-internlm)
17. [Moonshot AI — Kimi K2 / K2.5](#17-moonshot-ai)
18. [ByteDance (Seed) — Seed2.0 / Seed1.5-VL](#18-bytedance)
19. [StepFun (阶跃星辰) — Step-2](#19-stepfun)
20. [关注要点总结](#20-关注要点总结)

---

## 1. DeepSeek

### 1.1 DeepSeek-V3

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V3 技术报告 |
| **英文标题** | DeepSeek-V3 Technical Report |
| **发布机构** | DeepSeek-AI |
| **模型名称** | DeepSeek-V3 |
| **发布日期** | 2024-12-27 |
| **架构** | MoE（Mixture-of-Experts），671B 总参数，37B 激活参数 |
| **上下文长度** | 128K tokens |
| **主要创新** | Multi-head Latent Attention (MLA)；DeepSeekMoE 架构；Multi-Token Prediction (MTP)；FP8 混合精度训练；大规模流水线并行；辅助损失-free 负载均衡 |
| **链接** | https://arxiv.org/abs/2412.19437 |

### 1.2 DeepSeek-R1

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-R1：通过强化学习激励 LLM 推理能力 |
| **英文标题** | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning |
| **发布机构** | DeepSeek-AI |
| **模型名称** | DeepSeek-R1 / R1-Zero |
| **发布日期** | 2025-01-20 |
| **架构** | 基于 V3-Base，Dense 蒸馏版本 1.5B-70B |
| **主要创新** | R1-Zero：纯 RL 训练（无 SFT）涌现推理行为；R1：冷启动数据 + 多阶段训练（RL → 拒绝采样 SFT → RL）；蒸馏 R1 到小模型效果显著；开源 6 个蒸馏版本 |
| **链接** | https://arxiv.org/abs/2501.12948 |

### 1.3 DeepSeek-V3.2

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V3.2：推动开放大语言模型前沿 |
| **英文标题** | DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models |
| **发布机构** | DeepSeek-AI |
| **模型名称** | DeepSeek-V3.2 / V3.2-Speciale |
| **发布日期** | 2025-12-02 |
| **架构** | MoE，基于 V3.1-Terminus 继续预训练 |
| **主要创新** | DeepSeek Sparse Attention (DSA) — 高效稀疏注意力机制；可扩展 RL 框架，后训练计算量超过预训练的 10%；V3.2-Speciale 超越 GPT-5，IMO/IOI 2025 金牌水平；大规模 Agentic 任务合成管线 |
| **链接** | https://arxiv.org/abs/2512.02556 |

### 1.4 DeepSeek-V4 (新增 2026-07-05)

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4：MoE 架构在效率、可扩展性和长上下文能力上的飞跃 |
| **英文标题** | DeepSeek-V4: A Leap in MoE Architecture for Efficiency, Scalability, and Long-Context Capabilities |
| **发布机构** | DeepSeek-AI |
| **模型名称** | DeepSeek-V4 |
| **发布日期** | 2026-05-30 (arXiv) |
| **架构** | MoE — 约 1T 总参数，约 50B 激活参数 |
| **训练数据** | ~32–33T tokens |
| **上下文长度** | 1M tokens |
| **主要创新** | Chain-Selective Attention (CSA) 与 Hybrid Cross-Attention (HCA) 协同 KV-cache 管理；升级版 MLA；改进负载均衡策略；On-Policy Distillation 后训练；FP8 混合精度延续 |
| **链接** | https://arxiv.org/abs/2605.21510 |

---

## 2. OpenAI

### 2.1 GPT-5 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5 系统卡 |
| **英文标题** | GPT-5 System Card |
| **发布机构** | OpenAI |
| **模型名称** | GPT-5 (gpt-5-main / gpt-5-thinking / gpt-5-pro) |
| **发布日期** | 2025-08-07 |
| **架构** | 统一系统：快速模型 (gpt-5-main) + 深度推理模型 (gpt-5-thinking) + 实时路由器；含 mini/nano 变体 |
| **上下文长度** | 未公开 |
| **主要创新** | 统一推理/快速模型系统；路由器持续训练（用户切换/偏好/正确性信号）；幻觉大幅减少；指令遵循改进；sycophancy 降低；safe-completions 安全机制；Preparedness Framework High capability 分类 |
| **链接** | https://arxiv.org/abs/2601.03267 |

### 2.2 o3 / o4-mini System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | OpenAI o3 和 o4-mini 系统卡 |
| **英文标题** | OpenAI o3 and o4-mini System Card |
| **发布机构** | OpenAI |
| **模型名称** | o3 / o4-mini / o3-pro |
| **发布日期** | 2025-04-16 |
| **主要创新** | 结合 SOTA 推理与完整工具能力（web browsing, Python, image/video/file analysis）；o3-pro 用于 Pro 用户 |
| **链接** | https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf |

---

## 3. Meta AI

### 3.1 Llama 4

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama 4 族系：架构、训练、评估与部署笔记 |
| **英文标题** | The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes |
| **发布机构** | Meta AI |
| **模型系列** | Llama 4 Scout / Maverick / Behemoth |
| **发布日期** | 2025-04-05 (Scout/Maverick)；2026-01-06 (附录更新) |
| **架构** | MoE + 早期融合原生多模态 |
| **模型规格** | Scout: 17B 激活 / 109B 总参 (16 experts)，10M 上下文，~40T tokens |
| | Maverick: 17B 激活 / 400B 总参 (128 experts)，1M 上下文，~22T tokens |
| **输入模态** | 多语言文本 + 图像 |
| **输出模态** | 多语言文本 + 代码 |
| **主要创新** | 原生多模态（早期融合，非 adapter）；Scout 单 H100 int4 可部署；Maverick FP8 单 DGX 节点可部署；10M 超长上下文 (Scout)；Behemoth 为教师模型（288B 激活，2T 总参）；iRoPE 位置编码；在线训练框架（RL + DPO 后训练） |
| **链接** | https://doi.org/10.5281/zenodo.18246522 |

---

## 4. Google DeepMind

### 4.1 Gemini 2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 2.5：以前沿推理、多模态、长上下文和下一代 Agent 能力推动边界 |
| **英文标题** | Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 2.5 Pro / Flash / Flash-Lite；Gemini 2.0 Flash / Flash-Lite |
| **发布日期** | 2025-03-25 (Pro Exp)；2025-06-17 (GA) |
| **上下文长度** | 1M tokens (全系列) |
| **输出长度** | 65,536 tokens |
| **主要创新** | Thinking model — 混合推理（可调节推理预算）；多模态：文本/图像/视频/音频/PDF 输入；3 小时视频处理能力；Agentic 工作流；SoTA coding/reasoning (Aider Polyglot, GPQA Diamond, HLE)；完整 Pareto frontier (Pro/Flash/Lite) |
| **链接** | https://arxiv.org/abs/2507.06261 |

---

## 5. Anthropic

### 5.1 Claude Opus 4 & Sonnet 4 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | 系统卡：Claude Opus 4 和 Claude Sonnet 4 |
| **英文标题** | System Card: Claude Opus 4 & Claude Sonnet 4 |
| **发布机构** | Anthropic |
| **模型名称** | Claude Opus 4 / Claude Sonnet 4 |
| **发布日期** | 2025-05-22 |
| **架构** | Hybrid reasoning LLM |
| **主要创新** | 高级推理 + 视觉分析 + Computer use + Tool use；自主长周期 Coding 任务；首次包含 alignment assessment + model welfare assessment；Opus 4 在 ASL-3 Standard 下部署；reward hacking 评估 |
| **链接** | https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47/claude-opus-4-and-claude-sonnet-4-system-card.pdf |

### 5.2 Claude Opus 4.6 System Card (新增 2026-07-05)

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4.6 系统卡 |
| **英文标题** | Claude Opus 4.6 System Card |
| **发布机构** | Anthropic |
| **模型名称** | Claude Opus 4.6 |
| **发布日期** | 2026-02-21 |
| **主要创新** | 安全从头设计，达到 ASL-3 标准；包含 sabotage risk evaluations（破坏风险评估）；使用无监督激活引导的 SFT 数据（针对高风险拒绝）；更严格的安全性标准而非纯粹追求 benchmark 分数 |
| **链接** | https://anthropic.com/research/claude-opus-4-6-system-card |

---

## 6. Mistral AI

### 6.1 Mistral Large 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral Large 3 技术文档 |
| **英文标题** | Mistral Large 3 Technical Documentation |
| **发布机构** | Mistral AI |
| **模型名称** | Mistral Large 3 |
| **发布日期** | 2025-12-02 |
| **架构** | 多模态粒度 MoE；总参 500B-1T，激活 15B-50B |
| **上下文长度** | 256K tokens |
| **输入模态** | 文本 + 图像 |
| **训练算力** | 3000 张 NVIDIA H200 GPU |
| **主要创新** | 开放权重 SOTA；粒度 MoE 设计；长上下文 + 多模态推理；Agentic 能力 |
| **链接** | https://mistral.ai/news/mistral-3/ |

### 6.2 Ministral 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Ministral 3 技术报告 |
| **英文标题** | Ministral 3 Technical Report |
| **发布机构** | Mistral AI |
| **发布日期** | 2026-01-13 |
| **主要创新** | 小参数高效模型系列 |
| **链接** | https://arxiv.org/abs/2601.08584 |

---

## 7. Qwen (Alibaba)

### 7.1 Qwen3

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **英文标题** | Qwen3 Technical Report |
| **发布机构** | Alibaba (Qwen Team) |
| **模型系列** | Qwen3（6 个 Dense + 2 个 MoE） |
| **发布日期** | 2025-05-14 |
| **模型规格** | Dense: 0.6B / 1.7B / 4B / 8B / 14B / 32B |
| | MoE: 30B-A3B / 235B-A22B (235B 总参，22B 激活) |
| **训练数据** | 第一阶段 ~30T tokens；第二阶段 STEM/coding 增强；第三阶段长上下文扩展 |
| **上下文长度** | 预训练 32K（可扩展至 131K-1M） |
| **主要创新** | Hybrid thinking mode（同一模型切换 thinking/non-thinking）；MoE 旗舰仅需 10% 激活参数即达 Qwen2.5 Dense 性能；119 种语言支持；MCP 协议支持；YARN + DCA 长上下文扩展 |
| **链接** | https://arxiv.org/abs/2505.09388 |

### 7.2 Qwen3-VL (新增 2026-07-05)

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3-VL 技术报告 |
| **英文标题** | Qwen3-VL Technical Report |
| **发布机构** | Alibaba (Qwen Team) |
| **模型系列** | Qwen3-VL (多模态视觉-语言模型) |
| **发布日期** | 2025-11-29 |
| **架构** | Dense 和 MoE 混合视觉-语言；原生多模态融合 |
| **主要创新** | 基于 Qwen3 的多模态扩展；支持 2 小时视频分析；视觉数学推理领先 |
| **链接** | https://arxiv.org/abs/2512.00593 |

---

## 8. Yi (01.AI)

### 8.1 Yi-Lightning

| 项目 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **发布机构** | 01.AI |
| **模型名称** | Yi-Lightning |
| **发布日期** | 2024-12-02 |
| **架构** | 增强 MoE — 先进专家分割与路由机制 + 优化 KV-caching |
| **主要创新** | Chatbot Arena 总排名第 6，中文/数学/Coding/Hard 分类第 2-4；多阶段训练策略；合成数据 + 奖励建模；RAISE 安全框架（四组件覆盖预训练/后训练/部署）；低成本训练/推理 |
| **链接** | https://arxiv.org/abs/2412.01253 |

---

## 9. Baichuan

### 9.1 Baichuan4

| 项目 | 内容 |
|------|------|
| **中文标题** | 百川 4 大模型 |
| **英文标题** | Baichuan 4 |
| **发布机构** | Baichuan Intelligent Technology |
| **模型名称** | Baichuan 4 / Baichuan 4 Turbo |
| **发布日期** | 2024-05 |
| **上下文长度** | 128K-192K tokens |
| **主要创新** | 中文企业级性能领先；金融/医疗领域变体（Baichuan4-Finance）；C-Eval/CMMLU 高分 |
| **链接** | 未公开详细技术报告 |

---

## 10. Microsoft

### 10.1 Phi-4 系列

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4 技术报告 / Phi-4-reasoning / Phi-4-reasoning-vision 技术报告 |
| **英文标题** | Phi-4 Technical Report / Phi-4-reasoning Technical Report / Phi-4-reasoning-vision Technical Report |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4 (14B) / Phi-4-reasoning (14B) / Phi-4-reasoning-vision (15B) |
| **发布日期** | 2025-04-30 / 2026-03-04 |
| **架构** | Dense Transformer |
| **主要创新** | 数据质量为中心的训练方案；小参数 SOTA 推理性能；多模态推理（vision 版）；紧凑开放权重模型 |
| **链接** | Phi-4: https://arxiv.org/abs/2504.21318 |
| | Phi-4-reasoning-vision: https://arxiv.org/abs/2603.03975 (新增 2026-07-05) |

---

## 11. Apple

### 11.1 Apple Intelligence Foundation Language Models

| 项目 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型 — 2025 技术报告 |
| **英文标题** | Apple Intelligence Foundation Language Models — Tech Report 2025 |
| **发布机构** | Apple |
| **模型名称** | AFM on-device / AFM server |
| **发布日期** | 2025-07-17 (arXiv 更新) |
| **架构** | 多语言、多模态基础语言模型 |
| **主要创新** | 端侧 + 服务端双模型架构；Apple Intelligence 全产品线驱动；隐私保护设计；设备端高效推理优化 |
| **链接** | https://arxiv.org/abs/2507.13575 |

---

## 12. NVIDIA

### 12.1 Nemotron 3 系列

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Nano/Super/Ultra：开放高效混合 Mamba-Transformer MoE 模型 |
| **英文标题** | Nemotron 3 Nano/Super/Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 Nano / Super / Ultra |
| **发布日期** | 2026-04-03 (Super) / 2026-06-04 (Ultra) |
| **架构** | MoE Hybrid Mamba-Attention + LatentMoE |
| **模型规格** | Ultra: 550B 总参 / 55B 激活；Super: 120B 总参 / 12B 激活 |
| **上下文长度** | 支持至 1M tokens |
| **主要创新** | 混合 Mamba-Attention 架构；LatentMoE 提升精度；MTP 层原生 speculative decoding；推理时推理预算控制；NVFP4 预训练；MOPD (Multi-teacher On-Policy Distillation) 后训练；RULER 1M 上下文 SOTA；5.9x 推理吞吐优势 (vs GLM-5) |
| **链接** | https://research.nvidia.com/labs/nemotron/ |

---

## 13. xAI

### 13.1 Grok 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 3 Beta — 推理代理时代 |
| **英文标题** | Grok 3 Beta — The Age of Reasoning Agents |
| **发布机构** | xAI |
| **模型名称** | Grok 3 / Grok 3 mini |
| **发布日期** | 2025-02-19 |
| **架构** | Decoder-only Transformer（未公开详细参数） |
| **训练算力** | Colossus 超算集群，10x 前代算力 |
| **主要创新** | 大规模 RL 推理训练（分钟级思考、纠错、探索替代方案）；AIME 2025 93.3% (cons@64)；Chatbot Arena Elo 1402；Grok 3 mini 成本效率推理；实时信息接入；持续训练中 |
| **链接** | https://x.ai/news/grok-3 |

### 13.2 Grok 4 (新增 2026-07-05)

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4 |
| **英文标题** | Grok 4 |
| **发布机构** | xAI |
| **模型名称** | Grok 4 |
| **发布日期** | 2026-07 (预计) |
| **架构** | 未公开 |
| **主要创新** | 媒体报道称 xAI 团队在加速开发 Grok 4，预计显著超越前代推理能力；截至 2026-07-05 尚无正式 arXiv 论文或技术报告 |
| **链接** | 无正式报告 |

---

## 14. Amazon

### 14.1 Amazon Nova 家族

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 模型家族：技术报告与模型卡 |
| **英文标题** | The Amazon Nova Family of Models: Technical Report and Model Card |
| **发布机构** | Amazon AGI |
| **模型系列** | Nova Micro / Lite / Pro / Premier / Canvas / Reel |
| **发布日期** | 2025-03-17 (家族报告) / 2025-04-30 (Premier) |
| **架构** | Transformer（Micro/Lite/Pro/Premier）；Latent Diffusion (Canvas/Reel) |
| **上下文长度** | Premier: 1M tokens |
| **主要创新** | 多模态（文本/图像/视频/音频）；全 Pareto 覆盖（Micro 到 Premier）；Premier 支持复杂推理 + agentic + 模型蒸馏；200+ 语言训练；DPO + PPO 对齐 |
| **链接** | https://arxiv.org/abs/2506.12103 |

---

## 15. Zhipu AI

### 15.1 GLM-5

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5：从 Vibe Coding 到 Agentic Engineering |
| **英文标题** | GLM-5: From Vibe Coding to Agentic Engineering |
| **发布机构** | Zhipu AI (智谱 AI) |
| **模型名称** | GLM-5 / GLM-5.1 / GLM-5.2 |
| **发布日期** | 2026-02-17 |
| **架构** | MoE — 744B 总参 / 40B 激活（GLM-5）；355B/32B → 744B/40B 缩放 |
| **训练数据** | 28.5T tokens |
| **主要创新** | 集成 DeepSeek Sparse Attention (DSA)；slime 异步 RL 基础设施；Agentic engineering 长程任务；CC-Bench-V2 评估；开放权重 SOTA 推理/编码/Agent 能力 |
| **链接** | https://arxiv.org/abs/2602.15763 |

---

## 16. InternLM (Shanghai AI Lab)

### 16.1 InternLM3

| 项目 | 内容 |
|------|------|
| **中文标题** | 书生·浦语大模型第 3 代 |
| **英文标题** | InternLM3 |
| **发布机构** | Shanghai AI Laboratory (上海人工智能实验室) |
| **模型名称** | InternLM3-8B-Instruct |
| **发布日期** | 2025-01-15 |
| **架构** | Dense Transformer |
| **参数量** | 8B |
| **训练数据** | 4T tokens（节省 75%+ 训练成本） |
| **主要创新** | 极低数据量（4T）达到 SOTA — 超越 Llama3.1-8B / Qwen2.5-7B；深度思考模式（long CoT）+ 普通模式双模；推理与知识密集型任务领先 |
| **链接** | https://arxiv.org/abs/2403.17297（技术报告引用 InternLM2，InternLM3 详见 HuggingFace model card） |

---

## 17. Moonshot AI

### 17.1 Kimi K2 / K2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2：开放智能代理 / Kimi K2.5：开放原生多模态 Agentic 模型 |
| **英文标题** | Kimi K2: Open Agentic Intelligence / Kimi K2.5: Open Native Multimodal Agentic Model |
| **发布机构** | Moonshot AI (月之暗面) |
| **模型系列** | Kimi K2 / K2.5 |
| **发布日期** | 2025-07-28 (K2) / 2026-01-30 (K2.5) |
| **架构** | MoE — 1T 总参 / 32B 激活；384 experts，8 selected per token；MLA 注意力 |
| **上下文长度** | 256K tokens |
| **训练数据** | 15.5T tokens (K2)；K2.5 额外 ~15T 混合视觉+文本 tokens |
| **主要创新** | Agentic 能力 SoTA；MLA (Multi-head Latent Attention)；原生多模态 Agent（K2.5）；Thinking + Instant 双模式；开源；MuonClip 优化器训练（K2）；RLVR 训练（基于 self-critique rubric 的强化学习，非 reward model） |
| **链接** | K2: https://arxiv.org/abs/2507.20534 / K2.5: https://github.com/MoonshotAI/Kimi-K2.5 |

---

## 18. ByteDance (Seed)

### 18.1 Seed2.0

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed2.0 模型卡：面向真实世界复杂性的智能前沿 |
| **英文标题** | Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity |
| **发布机构** | ByteDance Seed |
| **模型系列** | Seed2.0 Pro / Lite / Mini / Code |
| **发布日期** | 2026-02-14 (发布) / 2026-06-30 (arXiv) |
| **架构** | 未公开详细参数 |
| **主要创新** | 长尾知识挑战；复杂指令跟随；视觉理解 SOTA (BabyVision)；推理 + 搜索能力；基于真实用户反馈的评估体系；驱动豆包（Doubao）数亿用户产品 |
| **链接** | https://arxiv.org/abs/2607.00248 |

### 18.2 Seed1.5-VL

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed1.5-VL 技术报告 |
| **英文标题** | Seed1.5-VL Technical Report |
| **发布机构** | ByteDance Seed |
| **发布日期** | 2025-05-12 |
| **主要创新** | 视觉-语言多模态理解 |
| **链接** | https://github.com/ByteDance-Seed/Seed1.5-VL |

---

## 19. StepFun (阶跃星辰)

### 19.1 Step-2

| 项目 | 内容 |
|------|------|
| **中文标题** | Step-2 万亿参数大模型 |
| **英文标题** | Step-2 |
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | Step-2 (16K) / Step-2-mini |
| **发布日期** | 2025 (Exact date TBD) |
| **架构** | MoE — 万亿参数级别（Trillion-scale） |
| **上下文长度** | 16K (Step-2) / 32K (Step-2-mini) |
| **主要创新** | 自研 MFA (Multi-Flow Attention) 加速架构 (Step-2-mini)；万亿参数 MoE；推理/Planning 能力逼近国际主流；Scaling Laws 前沿成果 |
| **是否发布报告** | 无独立技术报告，仅 API 文档 |

---

## 20. 关注要点总结

### 架构趋势

| 维度 | 趋势 |
|------|------|
| **MoE** | 几乎所有旗舰模型（DeepSeek-V3/V3.2/V4, Llama 4, Qwen3-235B, Mistral Large 3, Nemotron 3, GLM-5, Kimi K2/K2.5, Step-2）均采用 MoE。激活参数比率从 5%~10% 不等 |
| **Hybrid Mamba-Attention** | NVIDIA Nemotron 3 系列率先落地混合 Mamba-Transformer 架构 |
| **MLA (Multi-head Latent Attention)** | DeepSeek 自研 MLA 被 Kimi K2/K2.5 采纳；DeepSeek-V4 进一步升级 MLA 与 CSA/HCA |
| **DeepSeek Sparse Attention (DSA)** | DeepSeek V3.2 提出，被 GLM-5 集成 |
| **原生多模态** | Llama 4 早期融合（非 adapter）；Kimi K2.5 原生融合视觉；Qwen3-VL 多模态扩展 |

### 训练方法趋势

| 技术 | 代表模型 |
|------|---------|
| **纯 RL 训练（无 SFT）** | DeepSeek-R1-Zero |
| **多阶段 RL + 拒绝采样** | DeepSeek-R1, V3.2 |
| **混合推理（thinking/non-thinking 切换）** | Qwen3, Gemini 2.5, Claude Opus 4 |
| **可扩展 RL 后训练** | DeepSeek V3.2 (10%+ 预训练算力用于 RL) |
| **MOPD (多教师 on-policy 蒸馏)** | NVIDIA Nemotron 3 Ultra |
| **slime 异步 RL 框架** | GLM-5 (Zhipu AI) |
| **On-Policy Distillation 后训练** | DeepSeek-V4 |
| **RLVR (Self-Critique Rubric RL)** | Kimi K2 |

### Scaling Law / 缩放分析

- **DeepSeek V3.2**: 将后训练 RL 算力提升至预训练的 10%+，获得显著收益
- **DeepSeek V4**: 1T MoE 延续缩放，32–33T tokens 训练，配合 On-Policy Distillation
- **Qwen3**: MoE 仅需 10% 激活参数即达到 Dense SOTA
- **Nemotron 3 Ultra**: 550B→55B 激活，推理吞吐 5.9x vs GLM-5
- **InternLM3**: 仅 4T 数据即达 SOTA，数据质量 > 数量

### 长上下文模型

| 模型 | 上下文长度 |
|------|-----------|
| DeepSeek-V4 | 1M |
| DeepSeek-V3 | 128K |
| Llama 4 Scout | 10M |
| Llama 4 Maverick | 1M |
| Gemini 2.5 全系列 | 1M |
| Mistral Large 3 | 256K |
| Qwen3 | 32K (可扩展至 1M) |
| Nemotron 3 Ultra | 1M |
| Kimi K2/K2.5 | 256K |
| Amazon Nova Premier | 1M |
| Baichuan 4 | 128K-192K |

### 推理模型 / Reasoning Model

| 模型 | 策略 |
|------|------|
| DeepSeek-R1 / V3.2 / V4 | CoT RL, thinking mode |
| GPT-5 (thinking) | 统一路由器 + 深度推理模型 |
| Gemini 2.5 Pro/Flash | Hybrid thinking (可调节推理预算) |
| Claude Opus 4 | Hybrid reasoning |
| Qwen3 | Hybrid thinking mode (单模型切换) |
| Kimi K2.5 | Thinking + Instant 双模式 |
| Grok 3 | 大规模 RL 推理（分钟级思考） |
| Nemotron 3 | 推理时推理预算控制 |
| Phi-4-reasoning | 小参数推理专注 |
| Amazon Nova Premier | 原生 reasoning 支持 |
| Seed2.0 | 推理 + 搜索增强 |
| InternLM3 | 深度思考（long CoT）|
