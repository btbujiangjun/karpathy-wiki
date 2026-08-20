---
title: LLM Tech Report Digest — 2026-08-20
type: synthesis
created: 2026-08-20
updated: 2026-08-20
sources: [web-search]
tags: [tech-report, moe, scaling, multimodal, reasoning, daily-digest]
---

# LLM Tech Report Digest — 2026-08-20

> 19 家主流 AI 公司/实验室最新技术报告与旗舰模型汇总。每家一节：最新模型 + 发布日期 + 核心参数 + 架构创新 + 论文链接。

---

## 1. DeepSeek

| 项 | 值 |
|---|---|
| 最新旗舰 | DeepSeek-V4（Pro + Flash） |
| 发布日期 | 2026-04-24（Preview）/ 2026-08-13（V4-Pro GA） |
| 开源状态 | ✅ MIT License |
| 核心参数 | V4-Pro: 1.6T 总参 / 49B 激活 MoE；V4-Flash: 284B / 13B 激活 |
| 上下文窗口 | 1M（100 万 token） |
| 训练数据 | 32T–33T tokens |
| 架构创新 | 混合 CSA+HCA 注意力（4×/128× KV 压缩）；Manifold-Constrained Hyper-Connections (mHC)；Muon 优化器；FP4 MoE 路由专家 |
| 核心贡献 | 1M 上下文仅 27% 推理 FLOPs + 10% KV Cache（vs V3.2）；Agent 后训练：跨用户消息保留推理链 + `|DSML|` XML 工具调用格式；DSec 弹性沙箱 RL 环境 |
| 论文 | [DeepSeek-V4 Technical Report](https://arxiv.org/abs/2606.19348) |
| 最新动态 | V4-Pro GA（08-13）：Agent 能力大幅提升（HLE 60.0, TerminalBench 87.9, NL2Repo 61.5）；三档 Thinking Effort（low/high/max）；Responses API + Codex 适配；**08-16 API 定价调整**：峰值/非峰值双轨制，非峰值价格 50% 折扣 |

---

## 2. OpenAI

| 项 | 值 |
|---|---|
| 最新旗舰 | GPT-5.6（Sol / Terra / Luna） |
| 发布日期 | 2026-07-09（GPT-5.6 Sol 发布）/ 2026-08-06（ChatGPT 更新） |
| 开源状态 | ❌ 闭源 |
| 架构创新 | 三模型家族（旗舰 Sol + 高性价比 Terra + 最快 Luna）；统一系统 = Fast + Thinking + Router；GPT-Red 自动红队（self-play RL） |
| 核心贡献 | System Card 首次系统披露 Preparedness Framework 安全评估方法论；Cybersecurity / Bio 均为 High（非 Critical）；Safe-Completions 安全训练 |
| 论文 | [GPT-5.6 System Card](https://deploymentsafety.openai.com/gpt-5-6) |
| 最新动态 | **08-06 ChatGPT 更新**：GPT-5.6 Sol 新增 thinking effort 滑块（Plus/Pro 用户）；GPT-5.6 Luna 成为 Free/Go 用户默认模型，下周起无限文本聊天 + Think 按钮；**08-18 Model Spec 更新**：新增 safety 行为规范；Astra 定名（08-01 官方博客）——"next major model"；内部 Astra 证明 10 个数学/理论计算机科学定理（$2,000 API token） |

---

## 3. Meta AI

| 项 | 值 |
|---|---|
| 最新旗舰 | Llama 4 Scout / Maverick / Behemoth |
| 发布日期 | 2025-04-05 |
| 开源状态 | ✅ 开放权重（Llama 4 Community License） |
| 核心参数 | Scout: 17B×16E（109B 总参 / 17B 激活）；Maverick: 17B×128E（400B 总参 / 17B 激活）；Behemoth: 10T+（教师模型，未发布） |
| 上下文窗口 | Scout 10M / Maverick 1M |
| 训练数据 | Scout ~40T tokens / Maverick ~22T tokens |
| 架构创新 | 首代 MoE Llama；原生多模态 early fusion（文本+图像统一训练）；iRoPE（交错旋转位置编码 + 推理温度缩放）实现 10M 上下文 |
| 核心贡献 | 10M 上下文窗口（Scout）；开源 MoE 多模态模型达到商用水平；MetaP 自动超参选择 |
| 论文 | [Meta Llama 4 Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) |
| 最新动态 | 405B 开放权重承诺持续未兑现（自 08-11 起记录）；EAGLE 投机解码优化（Maverick 4ms/token, 8×H100）；无新 LLM 报告 |

---

## 4. Google DeepMind

| 项 | 值 |
|---|---|
| 最新旗舰 | Gemini 3.5 Flash |
| 发布日期 | 2026-05（GA） |
| 开源状态 | ❌ 闭源 |
| 核心参数 | 未公开具体参数量 |
| 上下文窗口 | 1M（输入）/ 65K（输出） |
| 架构创新 | Thinking Model 范式（4 档 Thinking Effort: minimal/low/medium/high）；Thought Preservation（多轮自动保留推理链）；原生多模态（文本/图像/视频/音频/PDF） |
| 核心贡献 | 最强 Flash 模型：Agent + Coding + Long-horizon 全面领先；ARC-AGI-2 72.1%；Terminal-Bench 2.1 76.2% |
| 论文 | [Gemini 3.5 Flash Model Card](https://deepmind.google/models/model-cards/gemini-3-5-flash/) |
| 最新动态 | Gemini 3.5 Flash GA（05 月）；Gemini 3.6 Flash 预告（下一代）；Gemini 4 预期 Q4 2026（Pichai"最雄心勃勃预训练"）；Hassabis 转任主席，Kavukcuoglu 升 SVP |

---

## 5. Anthropic

| 项 | 值 |
|---|---|
| 最新旗舰 | Claude Opus 5 / Sonnet 5 / Mythos 5 |
| 发布日期 | 2026-07-24（Opus 5）/ 2026-06-30（Sonnet 5）/ 2026-04-07（Mythos Preview） |
| 开源状态 | ❌ 闭源 |
| 架构创新 | Hybrid reasoning（extended thinking + 直接回答双模式）；RSP v3 安全框架（首个实践者）；多步 agentic 工具调用 |
| 核心贡献 | Opus 5: agentic coding / computer use / 长期知识工作大幅提升；Mythos Preview: 最强前沿模型（未公开发布，仅限防御性网络安全项目）；Sonnet 5: near-Opus intelligence + Sonnet 价格 |
| 论文 | [Claude Opus 5 System Card](https://www.anthropic.com/system-cards) |
| 最新动态 | Opus 5 现为最新旗舰（$5/$25 per MTok）；**Claude Opus 4.1 已退役**（API 返回错误）；Opus 5 thinking 默认开启，effort 梯度 low→max；mid-conversation tool changes beta；Claude Opus 4.6 MLE Bench 75.7%（最佳） |

---

## 6. Mistral AI

| 项 | 值 |
|---|---|
| 最新旗舰 | Mistral Medium 3 / Small 4 / Shieldstral / Ministral 3 |
| 发布日期 | 2026-08-03（Medium 3）/ 2026-03-16（Small 4）/ 2026-08-04（Shieldstral）/ 2026-01（Ministral 3） |
| 开源状态 | ✅ Apache 2.0 |
| 核心参数 | Medium 3: 285B 总参 / 38B 激活（8 expert + 1 shared）；Small 4: 119B 总参 / 6B 激活（128 专家 MoE）；Shieldstral: 3B（安全分类器）；Ministral 3: 3B/8B/14B（Dense） |
| 上下文窗口 | 256K（Medium 3）/ 256K（Small 4） |
| 架构创新 | Medium 3: Dense MoE 混合架构；Small 4: 统一 Magistral(推理) + Pixtral(多模态) + Devstral(编码) 为单一模型；Shieldstral: 策略自适应多模态安全分类器（推理时自然语言策略，无需重训）；Ministral 3: Cascade Distillation 预训练方法 |
| 核心贡献 | Medium 3: SWE-bench 58.8%（@200K tokens 首超 Claude Opus 4.6 + o3）；Small 4: 40% 延迟降低 + 3× 吞吐提升；Shieldstral: 3B 匹配 20B 安全模型；Ministral 3: 高效 Dense 模型 |
| 论文 | [Mistral Medium 3 Model Card](https://arxiv.org/abs/2608.02479) / [Ministral 3](https://arxiv.org/abs/2601.08584) |
| 最新动态 | **Mistral Medium 3（08-03）**：首个开源模型 SWE-bench 超 Claude Opus 4.6 + o3；多平台部署（Mistral API / Azure / AWS / GCP / Le Chat）；Shieldstral 1.0 3B（08-04）：Apache 2.0 多模态安全分类器；夏季新"大而稀疏"MoE 预告 |

---

## 7. Qwen (阿里通义)

| 项 | 值 |
|---|---|
| 最新旗舰 | Qwen3.8-Max / Qwen3.8-27B / Qwen3 Next 80B |
| 发布日期 | 2026-08-03（Max）/ 2026-08-17（27B + Max 权重）/ 2026-08-13（Next 80B 预告） |
| 开源状态 | ✅ Apache 2.0 |
| 核心参数 | Qwen3.8-Max: 2.4T 总参 / 95B 激活 MoE；Qwen3.8-27B: 27B Dense；Qwen3 Next 80B: 80B Dense（小尺寸替代 480B） |
| 上下文窗口 | 1M（Max）/ 262K（27B，可扩展至 1M） |
| 架构创新 | Sparse MoE + 混合注意力（Hybrid Attention）；Qwen3.8-Max 首次 Qwen-Max 级开源权重；27B Dense 可量化至笔记本运行；Next 80B 内置 RL Thinking + 标准模式 |
| 核心贡献 | 16 天自主编码（从空文件夹到生产级项目）；Text Arena #5 + Vision Arena #2；HF 151K 衍生模型（2.6× Meta 总量） |
| 论文 | [Qwen3.8-Max Blog](https://qwen.ai/blog?id=qwen3.8) |
| 最新动态 | Qwen3.8-27B 开源（08-17）：Apache 2.0，HF 2 天内 Top 5 最受欢迎模型；Max 权重同步开放；**Qwen3 Next 80B（08-13 预告）**：小尺寸替代 480B，内置 RL Thinking；Qwen MM-Plugins 多模态 Agent 框架开源 |

---

## 8. Yi / 01.AI (零一万物)

| 项 | 值 |
|---|---|
| 最新旗舰 | Yi-Lightning |
| 发布日期 | 2024-10-16（Chatbot Arena 首秀）/ 2024-12（技术报告） |
| 开源状态 | ✅ 开放权重 |
| 核心参数 | 未公开具体参数量（MoE 架构） |
| 架构创新 | Enhanced MoE（fine-grained expert segmentation + balanced routing + cross-layer KV cache sharing）；RAISE 四组件安全框架 |
| 核心贡献 | Chatbot Arena 第 6 名（中文第 2 / Math 第 3 / Coding 第 4） |
| 论文 | [Yi-Lightning Technical Report](https://arxiv.org/abs/2412.01253) |
| 最新动态 | 2026 年无新旗舰；转向企业 AI / 主权 AI；Yi-Lightning 仍为最新模型（2024-10） |

---

## 9. Baichuan (百川智能)

| 项 | 值 |
|---|---|
| 最新旗舰 | Baichuan-M2 / Baichuan-M3 |
| 发布日期 | 2026-08-11（M2）/ 2026-02（M3） |
| 开源状态 | ✅ 开源 |
| 核心参数 | M2: 32B；M3: 未公开（医疗增强型） |
| 架构创新 | M2: 医疗增强型大模型；M3: 超越基准模型；Medical-RoPE + Medical-Beta 权重在医疗数据上全量预训练 |
| 核心贡献 | M2: HealthBench 60.1（32B 超 120B）；M3: 超越基准模型；延续医疗垂直战略 |
| 论文 | [Baichuan-M3 Technical Report](https://arxiv.org/abs/2602.06570) |
| 最新动态 | M2（08-11）：开源医疗 32B 模型；M3（02 月）：医疗增强型；延续医疗垂直化路线 |

---

## 10. Microsoft (Phi 系列)

| 项 | 值 |
|---|---|
| 最新旗舰 | Phi-4-reasoning-vision-15B / Phi-4-reasoning |
| 发布日期 | 2026-03（Vision）/ 2025-04（Reasoning） |
| 开源状态 | ✅ 开放权重（MIT License） |
| 核心参数 | 14B–15B |
| 架构创新 | Phi-4-reasoning-vision-15B: 高效多模态推理模型（200B 多模态 token 训练）；混合 reasoning/non-reasoning 数据 + 显式模式 token；动态分辨率视觉编码器 |
| 核心贡献 | 以 15B 参数接近/超越 100B+ 模型；合成数据为核心训练范式；GRPO 强化学习增强推理 |
| 论文 | [Phi-4-reasoning-vision-15B Technical Report](https://arxiv.org/abs/2603.03975) |
| 最新动态 | Phi-4-reasoning-vision-15B（03 月）：多模态推理 SLM 标杆；Phi-5 仍为 single-source 传闻，无官方报告 |

---

## 11. Apple

| 项 | 值 |
|---|---|
| 最新旗舰 | Apple Intelligence Foundation Model 3（AFM 3）家族 |
| 发布日期 | 2026-06-08（公告）/ TR 待发（"summer"） |
| 开源状态 | ❌ 闭源 |
| 核心参数 | AFM 3 Core: ~3B Dense（端侧）；AFM 3 Core Advanced: 20B Sparse（1-4B 激活，端侧旗舰）；AFM 3 Cloud / Cloud Pro（云端） |
| 架构创新 | AFM 3 Core Advanced: Instruction-Following Pruning (IFP) 稀疏架构（首个端侧 20B Sparse 模型）；AFM 3 Cloud: PT-MoE 升级版；与 Google 联合开发；NVIDIA GPU in Private Cloud Compute |
| 核心贡献 | AFM 3 Core Advanced: 端侧最强 on-device LLM（表达式语音、高精度听写）；AFM 3 Cloud Pro: agentic tool use + 复杂推理 |
| 论文 | [Apple Foundation Models 3rd Gen](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) |
| 最新动态 | AFM 3 官方公告（06-08）；TR 承诺"summer"仍未兑现（截至 08-20）；5 模型家族（2 端侧 + 3 云端） |

---

## 12. NVIDIA

| 项 | 值 |
|---|---|
| 最新旗舰 | Nemotron 3 Ultra（550B-A55B） |
| 发布日期 | 2026-06-09 |
| 开源状态 | ✅ 开放权重（含训练数据和配方） |
| 核心参数 | 550B 总参 / 55B 激活（MoE Hybrid Mamba-Attention） |
| 上下文窗口 | 1M |
| 训练数据 | 20T tokens（NVFP4 预训练） |
| 架构创新 | Hybrid Mamba-Attention + LatentMoE + Multi-Token Prediction (MTP)；NVFP4 跨架构 GPU 部署；Multi-teacher On-Policy Distillation (MOPD) |
| 核心贡献 | 推理吞吐量 5.9× (vs GLM-5.1) / 4.8× (vs Kimi-K2.6) / 1.6× (vs Qwen-3.5)；50M SFT + 2M RL + 55 RL 环境全开源 |
| 论文 | [Nemotron 3 Ultra Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf) |
| 最新动态 | Nemotron 3 Ultra（06-09）：家族最强旗舰；Nemotron 3.5 Lightning（08-11）：30B-A3B 开放 MoE；Nemotron 3 Nano Omni（04-27）：首个多模态原生音频支持 |

---

## 13. xAI

| 项 | 值 |
|---|---|
| 最新旗舰 | Grok 4.6 |
| 发布日期 | 2026-08-12 |
| 开源状态 | ❌ 闭源 |
| 核心参数 | 1.5T 级别（官方未公开精确参数） |
| 上下文窗口 | 500K |
| 架构创新 | 与 Cursor 联合开发；Agentic RL（知识工作 + 通用编码 + 内核优化/Web开发/CAD 环境） |
| 核心贡献 | Artificial Analysis Intelligence Index 匹配 GPT-5.6 Sol；编程和长期 Agent 任务大幅提升；价格 $2/$6 per M tokens |
| 论文 | [Grok 4.6 Model Card](https://media.x.ai/v1/website/card-4p6-4cd2dc57.pdf) |
| 最新动态 | Grok 4.6 GA（08-12）：Cursor + Grok Build 首发；**08-14 GitHub Copilot 集成**：VS Code / Copilot CLI / Cloud Agent 全线支持；Grok 4.7（2.1T）计划 3-4 周后；Self-harm 合规从 0.5% 退步至 3.7%（Model Card 自报） |

---

## 14. Amazon (AWS)

| 项 | 值 |
|---|---|
| 最新旗舰 | Nova 家族（Pro / Lite / Micro / Canvas / Reel） |
| 发布日期 | 2024 |
| 开源状态 | ❌ 闭源 |
| 架构创新 | 多模态家族（文本/图像/视频生成）；端到端多模态理解 |
| 核心贡献 | AWS 原生 LLM 生态布局；多模态全家桶覆盖 |
| 论文 | [Amazon Nova Technical Report](https://www.amazon.science/publication/amazon-nova) |
| 最新动态 | Nova TR 2024 仍唯一正式报告；re:Invent 2026 为下一观察点 |

---

## 15. Zhipu AI (智谱清言 / Z.ai)

| 项 | 值 |
|---|---|
| 最新旗舰 | GLM-5.3 |
| 发布日期 | 2026-08-14 |
| 开源状态 | ✅ 开放权重（08-14 起两周内） |
| 核心参数 | 743B MoE（同 GLM-5.2 基座，全增益来自 post-training） |
| 上下文窗口 | 1M |
| 架构创新 | 完全复用 GLM-5.2 基座 + 规模化 post-training（更多环境、更长任务、更多算力）；slime 异步 RL 基础设施；IndexShare 长上下文处理 |
| 核心贡献 | Terminal-Bench 3.0: 4.6→28.3（开源最强）；CyberGym 84.5%（超越 Mythos 5 和 GPT-5.6 Sol）；发现 2,436 个真实漏洞（1,097 中高危，含 40 年历史漏洞） |
| 论文 | [GLM-5.3 Blog](https://z.ai/blog/glm-5.3) |
| 最新动态 | GLM-5.3 发布（08-14）：post-training scaling 驱动全部增益；网络安全能力涌现超出预期；**权重预计两周内开源**（08-14 起计），安全评估 + 加固后发布 |

---

## 16. InternLM (书生系列 / 上海 AI Lab)

| 项 | 值 |
|---|---|
| 最新旗舰 | Intern-S2-Preview-397B / Intern-S1-Pro（1T）/ Intern-S2-Mobius |
| 发布日期 | 2026-08（S2-Preview）/ 2026-03（S1-Pro）/ 2026-08（Mobius） |
| 开源状态 | ✅ 开放权重 |
| 核心参数 | S2-Preview: 397B（持续预训练自 Qwen3.5）；S1-Pro: 1T（首个万亿科学多模态）；Mobius: 35B（知识-推理解耦架构） |
| 架构创新 | S2-Preview: 科学多模态 + 时序建模 + Memory Decoder + MTP + CoT 压缩；Mobius: 全局共享 Memory(FFN) + 多 Reasoner(Self-Attn) 架构，4× 推理加速 |
| 核心贡献 | S1-Pro: 科学推理超越 Gemini-3-Pro/GPT-5.2（SciReasoner 55.5 vs 14.7/13.6）；Mobius: 35B 达 35B Transformer 等效分数，推理链更短 |
| 论文 | [Intern-S2-Preview](https://arxiv.org/abs/2608.13505) / [Intern-S2-Mobius](https://arxiv.org/abs/2608.14290) / [Intern-S1-Pro](https://arxiv.org/abs/2603.25040) |
| 最新动态 | 三篇论文同期发布（08 月）；S2-Preview 397B 仅用 397B 追平此前万亿模型；Mobius 架构验证知识-推理解耦有效性 |

---

## 17. Moonshot AI (月之暗面)

| 项 | 值 |
|---|---|
| 最新旗舰 | Kimi K3 |
| 发布日期 | 2026-07-27（权重 + 技术报告） |
| 开源状态 | ✅ 开放权重（Kimi K3 License） |
| 核心参数 | 2.8T 总参 / 104B 激活（MoE）；896 路由专家 / 16 激活 / 2 共享 |
| 上下文窗口 | 1M |
| 架构创新 | Kimi Delta Attention (KDA) 线性注意力（69/93 层）+ Gated MLA NoPE（24/93 层）；Attention Residuals (AttnRes) 跨层注意力；Stable LatentMoE + Quantile Balancing；MoonViT-V2 无对比预训练视觉编码器 |
| 核心贡献 | 2.5× scaling efficiency（vs K2）；WebDev Arena #1（1678 Elo，首个开源模型登顶）；BrowseComp 91.2% @ $2.03/task；发现 16 个真实漏洞（含 Linux 内核） |
| 论文 | [Kimi K3 Technical Report](https://arxiv.org/abs/2607.24653) |
| 最新动态 | K3 全量权重 + 47 页技术报告（07-27）按期兑现；K4 训练传闻（The Information 07-28/29）；Kimi Code CLI 0.34.0（08-06） |

---

## 18. StepFun (阶跃星辰)

| 项 | 值 |
|---|---|
| 最新旗舰 | Step 3.7 Flash |
| 发布日期 | 2026-05-29 |
| 开源状态 | ✅ Apache 2.0 |
| 核心参数 | 198B 总参 / 11B 激活（196B 语言 + 1.8B 视觉编码器） |
| 上下文窗口 | 256K |
| 架构创新 | MoE（288 routed + 1 shared expert / layer）；三档 Reasoning Effort；NVFP4 + MTP 投机解码（1.45× 加速）；Advisor Mode（小执行器 + 大顾问模型） |
| 核心贡献 | ClawEval-1.1 #1（67.1）；SWE-Bench PRO #2（56.3）；Advisor Mode 达 97% Claude Opus 4.6 性能 @ 1/9 成本 |
| 论文 | [Step 3.7 Flash](https://static.stepfun.com/blog/step-3.7-flash/) |
| 最新动态 | Step 3.7 Flash（05-29）：生产级 Agent Flash 模型；Step 3.5 Flash（01-31）：256K SWA 混合注意力；Step3-VL-10B: PaCoRe 多模态 |

---

## 19. ByteDance (字节跳动 / 豆包)

| 项 | 值 |
|---|---|
| 最新旗舰 | Seed 2.0 系列（Pro / Lite / Mini / Code） |
| 发布日期 | 2026-02-14（发布）/ 2026-06-30（Model Card arXiv） |
| 开源状态 | ❌ 闭源（API 通过火山引擎） |
| 核心参数 | Pro / Lite / Mini 三档；Code 专用模型 |
| 架构创新 | Agent 级长链推理；Omni-modal understanding（视频/图像/音频/文本统一）；端到端实时交互与应用生成 |
| 核心贡献 | SuperGPQA 超越 GPT-5.2；Codeforces Elo 3020（IMO/CMO 金牌水平）；155M 周活用户（Doubao，全球第 4 大 GenAI 应用） |
| 论文 | [Seed2.0 Model Card](https://arxiv.org/abs/2607.00248) |
| 最新动态 | Seed2.0 Model Card arXiv（06-30）；Seed2.1 Model Card（Pro+Turbo, Agent/视频理解 SOTA）；Seedream 3.0 图像生成（04-11）；>5T/10T 参数新模型训练传闻 |

---

## 交叉观察

### 架构趋势

| 趋势 | 代表公司 | 说明 |
|------|---------|------|
| MoE 统治 | DeepSeek/Qwen/Mistral/ByteDance/Kimi/NVIDIA/StepFun/GLM | 19 家中 8+ 家采用 MoE，总参 >1T 成标配 |
| Hybrid Attention | NVIDIA（Mamba-Attention）/ DeepSeek（CSA+HCA）/ Kimi（KDA+MLA） | 线性复杂度 + 全注意力混合 |
| 原生多模态 | Meta Llama 4 / Google Gemini / Apple AFM 3 / ByteDance Seed | 文本/图像/音频/视频统一训练 |
| Thinking 范式 | OpenAI / Anthropic / Google / Qwen / GLM / Kimi | 内置推理链 + 直接回答双模式 |
| 端侧部署 | Apple（IFP 20B Sparse）/ NVIDIA（3.5 Lightning）/ Qwen（27B 可笔记本运行） | 端侧 LLM 进入量产阶段 |
| 架构创新 | Kimi（KDA+AttnRes）/ InternLM（Mobius 知识-推理解耦）/ Mistral（Cascade Distillation） | 非 Transformer 变体和新型训练方法涌现 |

### 开放 vs 闭源格局

| 类型 | 公司 |
|------|------|
| 开放权重 | DeepSeek, Meta, Mistral, Qwen, Yi, Microsoft, Baichuan, NVIDIA, Zhipu, InternLM, Moonshot, StepFun |
| 闭源 | OpenAI, Google, Anthropic, Apple, Amazon, xAI, ByteDance |

### "承诺→兑现"信用追踪

| 承诺 | 状态 | 备注 |
|------|------|------|
| Meta 405B 开放权重 | ❌ 未兑现（08-11 起记录） | 无新发布实据 |
| Apple AFM 3 TR "summer" | ❌ 未兑现（截至 08-20） | 06-08 公告后无技术报告 |
| Moonshot K3 放权 | ✅ 按期兑现（07-27） | 47 页技术报告 + 全量权重 |
| DeepSeek V4 Pro GA | ✅ 兑现（08-13） | OpenRouter 上架 + API 定价调整 |
| Qwen3.8-Max 权重 | ✅ 兑现（08-17） | HF + ModelScope 同步开放 |
| GLM-5.3 开源 | ⏳ 计划中（08-14 起两周内） | 安全评估 + 加固后发布 |
| Grok 4.7 | ⏳ 计划中（3-4 周后） | 2.1T 参数 |

### 规模军备竞赛

| 公司 | 规模 | 状态 |
|------|------|------|
| ByteDance | >5T–10T | 预训练早期（3-6 个月） |
| xAI Grok 4.7 | 2.1T | 计划 3-4 周后 |
| Moonshot K4 | 未公开 | 训练中 |
| Qwen3.8-Max | 2.4T | ✅ 已发布 |
| Kimi K3 | 2.8T | ✅ 已发布 |
| NVIDIA Nemotron 3 Ultra | 550B | ✅ 已发布 |
| InternLM S1-Pro | 1T | ✅ 已发布 |

### 本期新发现

1. **Mistral Medium 3 SWE-bench 突破**：首个开源模型 SWE-bench 58.8% 超 Claude Opus 4.6 + o3（08-03 发布，08-05 SOTA 确认）
2. **Qwen3 Next 80B 小尺寸替代**：80B Dense 内置 RL Thinking，目标替代 480B 大模型，Qwen 策略从"做大"转向"做精"
3. **GLM-5.3 post-training scaling 有效性验证**：同一基座模型，纯 post-training 带来 Terminal-Bench 4.6→28.3 跳升 + 网络安全能力涌现
4. **Kimi K3 KDA 架构**：首个大规模纯线性注意力前沿模型（69/93 层 KDA），WebDev Arena 首次由开源模型登顶
5. **Apple AFM 3 Core Advanced**：首个端侧 20B Sparse 模型（IFP 剪枝），1-4B 激活
6. **InternLM Mobius 架构**：知识-推理解耦（共享 Memory FFN + 多 Reasoner Self-Attn），35B 达 4× 推理加速
7. **NVIDIA MOPD**：Multi-teacher On-Policy Distillation，10+ 专用教师模型指导学生训练
8. **Step 3.7 Advisor Mode**：小执行器 + 大顾问模型，97% Opus 4.6 性能 @ 1/9 成本
9. **Grok 4.6 GitHub Copilot 全线集成**：08-14 起 VS Code / Copilot CLI / Cloud Agent 均支持，Pro/Pro+/Max/Business/Enterprise 可用
10. **Baichuan-M2 医疗垂直化**：32B 参数 HealthBench 60.1 超 120B 模型，延续百川医疗战略

---

*Generated 2026-08-20. Source: Web search results. Cross-referenced with wiki/synthesis/2026-08-19/tech-report-digest.md.*
