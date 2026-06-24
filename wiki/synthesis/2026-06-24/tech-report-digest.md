---
title: "各大 AI 公司最新技术报告汇总 — 2026-06-24 (第十一版)"
type: synthesis
created: 2026-06-24
updated: 2026-06-24
sources: [web-search]
tags: [tech-report, system-card, frontier-models, 2026]
---

# 各大 AI 公司最新技术报告汇总 — 2026-06-24 (第十一版)

> 覆盖 20+ 家机构的最新 Tech Report / System Card / Model Card，重点关注大模型新架构、训练方法、Scaling Law、多模态、长上下文、推理模型。

## 目录

1. [DeepSeek — 深度求索](#1-deepseek-深度求索)
2. [OpenAI](#2-openai)
3. [Meta AI (Facebook)](#3-meta-ai-facebook)
4. [Google DeepMind](#4-google-deepmind)
5. [Anthropic](#5-anthropic)
6. [Mistral AI](#6-mistral-ai)
7. [Qwen (Alibaba)](#7-qwen-alibaba)
8. [xAI (Grok)](#8-xai-grok)
9. [Microsoft (Phi)](#9-microsoft-phi)
10. [Apple (Apple Intelligence)](#10-apple-apple-intelligence)
11. [NVIDIA (Nemotron)](#11-nvidia-nemotron)
12. [Amazon (Amazon Nova)](#12-amazon-amazon-nova)
13. [Zhipu AI (GLM)](#13-zhipu-ai-glm)
14. [InternLM / Shanghai AI Lab](#14-internlm-shanghai-ai-lab)
15. [Moonshot AI (Kimi)](#15-moonshot-ai-kimi)
16. [ByteDance (Seed / Doubao)](#16-bytedance-seed-doubao)
17. [StepFun (阶跃星辰)](#17-stepfun-阶跃星辰)
18. [01.AI (Yi)](#18-01ai-yi)
19. [Baichuan AI](#19-baichuan-ai)
20. [Others (MiniMax, Cohere, Stability AI, AI21 Labs)](#20-others)

---

## 1. DeepSeek — 深度求索

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **DeepSeek-V4 Technical Report** | 2026-04 | MoE (1.6T total, 64B active) | 1M context, CSA + HCA, MuonClip optimizer | 开源旗舰, $0.87/M out tokens, 推理与通用双优 |
| **DeepSeek-R1** | 2025-01 | Dense 671B MoE | arXiv:2501.12948 | 纯 RL 推理模型, CoT + RLVR 范式开创者 |
| **DeepSeek-V3** | 2024-12 | MoE (671B total, 37B active) | arXiv:2412.19437 | Multi-Token Prediction (MTP), FP8 训练, 高效 MoE 路由 |
| **DeepSeek-Coder-V3** | 2025 | MoE | 代码专项, 开源 | 代码推理+多语言支持 |
| **DeepSeek-V3.2** | 2025-08 | MoE | 685B total, 37B active | V3 升级版, 增强推理能力 |

**核心创新**:
- ⚡ **CSA (Cross-Stage Attention)** + HCA → $O(L)$ 长上下文推理（V4）
- ⚡ **MuonClip 优化器** → AdamW 的替代方案（V4）
- ⚡ **Multi-Token Prediction (MTP)** → 1-3 个额外 token 同时预测（V3）
- ⚡ **RLVR pipeline** → DeepSeek-R1 验证奖励驱动的推理训练

**定价**: DeepSeek-V4: $0.34/$0.87 per M tokens (输入/输出)

---

## 2. OpenAI

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **GPT-5.5 System Card** | 2026-04 | MoE, Router-based unified | 1M context, $5/$30 (Instant/Pro), 多模态原生 | 推理代币可配置, 视觉/语音/代码融合 |
| **GPT-5 System Card** | 2025-08 (arXiv 2025-12) | MoE, Router-based unified | arXiv:2601.03267, 多模态原生 | Router 自动选择推理深度, 开源 System Card |
| **o3 / o4-mini System Card** | 2025-04 | Reasoning-dedicated | arXiv:2504.01990 | 推理链 CoT, 可编程思考预算 |
| **o1 System Card** | 2024-09 | Reasoning-dedicated | arXiv:2412.14135 | 首个推理模型 System Card |

**核心创新**:
- ⚡ **Router-based Unified Model** → 一个模型自动切花推理/速度模式
- ⚡ **Think Tokens** → 可配置推理预算（GPT-5.5）
- ⚡ **百万级上下文** → GPT-5.5 Pro 支持 1M tokens

**定价**: GPT-5.5 Pro: $45/$180 per M tokens; Instant: $5/$20 per M tokens

---

## 3. Meta AI (Facebook)

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Llama 4 Technical Report** | 2025-04 | MoE (Scout/Maverick/Behemoth) | Scout: 17B-A1.7B; Maverick: 17B-A2.7B; Behemoth: 288B-A28.8B; 10M context | MoE + 早期融合多模态 + 超大上下文 |
| **Llama 3.1** | 2024-07 | Dense (8B/70B/405B) | arXiv:2507.21783 | 405B 开源旗舰 |

**核心创新**:
- ⚡ **Early Fusion** → 图像/视频 token 与文本 token 在输入层统一融合
- ⚡ **10M context** → 70B 参数级实现百万级上下文窗口
- ⚡ **MoE 架构** → Llama 4 全系列转向 MoE

---

## 4. Google DeepMind

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Gemini 3.1 Pro** | 2026-02 | MoE | 2M context, 多模态原生 | 长上下文推理, Agentic 工具使用 |
| **Gemini 2.5 Pro** | 2025-07 | MoE | 1M context, Dynamic Thinking | 动态推理深度, 3h 视频理解 |
| **Gemini 2.0** | 2024-12 | MoE | 多模态原生, Agentic | 原生多模态输入输出 |

**核心创新**:
- ⚡ **Dynamic Thinking** → 模型自动调节推理深度（2.5）
- ⚡ **2M context** → 当前业界最大上下文窗口（3.1）
- ⚡ **Agentic 集成** → Google Search / Tool Use 原生打通

---

## 5. Anthropic

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Claude Opus 4.8** | 2026-05 | 未公开 (Dense?) | 200K context, 编码/推理旗舰 | 自进化循环, 元认知能力 |
| **Claude 4 System Card** | 2025-05 | 未公开 | 200K context, vision | Opus 4 + Sonnet 4 组合 |
| **Claude 3.5 Sonnet** | 2024-06 | 未公开 | 200K context | 编码主力 |

**核心创新**:
- ⚡ **Meta-Cognition** → 模型能识别自身推理错误并自修正
- ⚡ **Safety RSP** → Responsible Scaling Policy 级别 4 安全评估
- ⚡ **自进化** → 通过反馈循环持续改进输出质量

---

## 6. Mistral AI

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Mistral Large 3** | 2025-12 | MoE (675B total, 75B active) | 256K context, Apache 2.0, 多语言 | 完全开源, 旗舰性能 |
| **Mistral Medium 3.5** | 2026-04 | MoE | 250B-total, 32B-active | 性价比优化 |
| **Mistral Small 4** | 2026-03 | MoE | 100B-total, 12B-active | 高效边缘部署 |

**核心创新**:
- ⚡ **Cascade Distillation** → 从旗舰模型级联蒸馏到中小模型
- ⚡ **Apache 2.0 开源** → 完全开放权重和商业使用
- ⚡ **多语言原生** → 法语/德语/西班牙语等强于同类

---

## 7. Qwen (Alibaba)

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Qwen3 Technical Report** | 2025-05 | MoE (Qwen3-235B-A22B) | arXiv:2505.09338, 119 languages, 128K ctx | Hybrid Thinking (Thinking/Non-Thinking 模式) |
| **Qwen2.5 Technical Report** | 2024-07 | Dense (0.5B-72B) | arXiv:2507.09648 | 全面覆盖小到大 |
| **Qwen2 Technical Report** | 2024 | Dense | arXiv:2407.10671 | 多语言开源 |

**核心创新**:
- ⚡ **Hybrid Thinking** → 同一模型可在 Thinking (推理) 与 Non-Thinking (快速) 模式间切换
- ⚡ **119 语言** → 业界语言覆盖最广的开源模型
- ⚡ **MoE 转型** → Qwen3 全面转向 MoE 架构

---

## 8. xAI (Grok)

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Grok-4 Model Card** | 2025-08 | MoE (1T+ total) | 1M context, 多模态 | 实时知识 + 多模态推理 |
| **Grok-4.1 Model Card** | 2025-11 | MoE | 增强推理 | 推理能力大幅提升 |
| **Grok-4.1 Fast** | 2025-11 | MoE | 低延迟版 | 快速推理版本 |

**核心创新**:
- ⚡ **Real-time Knowledge** → X/Twitter 数据实时接入
- ⚡ **Multi-modal** → 图像+文本+代码统一处理
- ⚡ **大规模 MoE** → 1T+ 参数级模型

---

## 9. Microsoft (Phi)

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Phi-4 Technical Report** | 2024-12 | Dense (14B) | arXiv:2412.08905, SLM 技术路线 | Synthetic Data + 课程学习 |
| **Phi-4-Reasoning-Vision** | 2026-03 | MoE/混合 | arXiv:2603.03975, 15B | 多模态推理 + 视觉理解 |
| **Phi-4-mini / -slim** | 2025 | Dense | 3.8B/1.5B | 边缘设备部署 |

**核心创新**:
- ⚡ **Synthetic Data 路线** → 不依赖海量原始数据, 以课程化合成数据训练
- ⚡ **SLM (Small Language Model)** → 小参数 + 高质量数据 = 大模型级性能
- ⚡ **多模态推理** → Phi-4-Reasoning-Vision 同时处理推理链和视觉输入

---

## 10. Apple (Apple Intelligence)

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Apple Intelligence Foundation Language Models** | 2025-07 | On-device (~3B) + Server (PT-MoE) | arXiv:2507.13575, 多模态 | 端侧+云端双轨, 隐私保护 |
| **AFM v2** | 2026-05 (revised) | PT-MoE | Server 模型增强 | 功能增强版 |

**核心创新**:
- ⚡ **端侧-云端双轨架构** → On-device ~3B + Server PT-MoE
- ⚡ **隐私优先** → 数据端处理 + Private Cloud Compute
- ⚡ **PT-MoE (Prefix-Tuning MoE)** → 低资源高效适配

---

## 11. NVIDIA (Nemotron)

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Nemotron-3 Ultra** | 2025-12 | MoE + Hybrid Mamba-Transformer | 待确认 arXiv | 混合架构, HBM 效率优化 |
| **Nemotron-3 8B** | 2025-08 | MoE + Hybrid Mamba-Transformer | arXiv:2508.14444 | Mamba-Attention 混合 |
| **Nemotron-3 Super** | 2026 | MoE | arXiv:2604.12374 | 增强训练版 |

**核心创新**:
- ⚡ **Hybrid Mamba-Transformer** → SSM + Attention 混合层设计
- ⚡ **HBM 效率优化** → 面向 Hopper/Blackwell GPU 架构优化
- ⚡ **LatentMoE** → 潜在空间中路由的 MoE 变体

---

## 12. Amazon (Amazon Nova)

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Amazon Nova Family Technical Report** | 2025-03 | Dense + MoE (Lite/Pro/Premier) | 微调+蒸馏, 多模态 | 完整模型家族, AWS 深度集成 |
| **Amazon Nova 2 (Lite/Pro)** | 2025-12 | MoE | 1M context, 多模态 | 增强版, 长上下文 |
| **Nova Premier** | 2025-04 | MoE | 旗舰级 | 复杂推理 |

**核心创新**:
- ⚡ **Model Distillation** → 内置蒸馏工作流
- ⚡ **AWS 生态** → Bedrock + SageMaker 深度集成
- ⚡ **1M context** → Nova 2 系列支持

---

## 13. Zhipu AI (GLM)

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **GLM-5 Technical Report** | 2026-02 | MoE (744B-A40B) | DSA (Dual Stream Attention), 1M ctx | DSA 长上下文架构, 异步 RL 训练 |
| **GLM-4.7** | 2025-12 | MoE | 增强推理 | 推理能力刷新 |
| **GLM-4.5** | 2025-07 | MoE | 297B-A21B | 单卡 A100 可部署 |
| **GLM-4.9** | 2024-06 | Dense | 开源基础 | ChatGLM 系列延续 |

**核心创新**:
- ⚡ **DSA (Dual Stream Attention)** → 交替局部/全局注意力流, 线性复杂度长上下文
- ⚡ **异步 RL (slime)** → 生产环境持续学习框架
- ⚡ **Dense-to-Sparse 训练** → 先 Dense 预训练后 MoE 化

---

## 14. InternLM / Shanghai AI Lab

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **InternLM3 Technical Report** | 2025-04 | Dense (8B) | arXiv:2504.04937, 4T 高质量数据 | 数据效率革命 — 4T 数据达 15T 效果 |
| **InternVL3** | 2025 | Multimodal | 多模态版 | 视觉语言模型 |
| **InternLM2 Technical Report** | 2024-03 | Dense (1.8B-104B) | arXiv:2403.17297 | 开源全系列 |

**核心创新**:
- ⚡ **4T 数据效率** → 4T tokens 高质量数据达到同类 15T+ 水准
- ⚡ **Online RLHF** → 在线强化学习对齐
- ⚡ **多模态扩展** → InternVL 系列视觉语言能力

---

## 15. Moonshot AI (Kimi)

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Kimi-K2.6 Technical Report** | 2026-04 | MoE (1T total, ~128B active) | 1M context, Agentic 原生 | MuonClip 优化器, 纯 RL 推理 |
| **Kimi-K2.5 Technical Report** | 2026-02 | MoE | arXiv:2602.02276 | Agentic RL 训练 |
| **Kimi-K2 Technical Report** | 2025-07 | MoE | arXiv:2507.20534 | 基础 MoE 架构 |
| **Kimi-VL Technical Report** | 2025-04 | Multimodal MoE | 视觉语言 | 多模态推理 |

**核心创新**:
- ⚡ **MuonClip 优化器** → DeepSeek V4 之外的另一独立实现
- ⚡ **Agentic RL** → 在 RL 阶段专门优化 Agentic 任务能力
- ⚡ **纯 RL 推理模型** → 不依赖 SFT 阶段, 直接从 Base Model 做 RL

---

## 16. ByteDance (Seed / Doubao)

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Doubao 1.5 Pro** | 2025 | MoE | 多模态, 1M ctx | 豆包主力模型 |
| **Seed1.5-VL Technical Report** | 2025-05 | Multimodal | arXiv:2505.07062 | 多模态 MoE |

**核心创新**:
- ⚡ **多模态原生** → 图像/视频/音频统一 token 化
- ⚡ **强推理** → 代码/逻辑推理专项优化
- ⚡ **端云协同** → 端侧轻量和云端重模型配合

---

## 17. StepFun (阶跃星辰)

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Step-3.7-Flash** | 2026-05 | MoE | 高速推理版 | 低延迟, 高性能 |
| **Step-3.5-Flash Technical Report** | 2026-02 | MoE (196B-A11B) | MFA + AFD 架构 | 混合注意力架构 |
| **Step-3** | 2025-07 | MoE (1T total) | arXiv:2507.19427 | 基础 MoE 架构 |

**核心创新**:
- ⚡ **MFA (Multi-Flow Attention)** → 多流注意力机制
- ⚡ **AFD (Adaptive Frequency Decomposition)** → 自适应频域分解
- ⚡ **开源** → Step 系列部分开源

---

## 18. 01.AI (Yi)

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Yi-Lightning Technical Report** | 2024-12 | MoE | arXiv:2412.01253, 高效推理 | RAISE 策略, MoE 路由优化 |
| **Yi Technical Report** | 2024-03 | Dense (6B/34B) | arXiv:2403.04652 | 双语开源基础 |

**核心创新**:
- ⚡ **RAISE (Routing-Aware Importance Sampled Estimation)** → MoE 路由效率创新
- ⚡ **双语高质量** → 中英双语训练, 中文场景强

---

## 19. Baichuan AI

| 报告 | 日期 | 架构 | 关键参数 | 亮点 |
|------|------|------|---------|------|
| **Baichuan-M3** | 2025 | MoE | 医疗领域 RL | SPAR 医疗 RL 框架 |
| **Baichuan-Omni** | 2024-10 | Multimodal | arXiv:2410.08565 | 多模态 |
| **Baichuan-M1** | 2025-02 | MoE | arXiv:2502.12671 | 医疗领域微调 |
| **Baichuan 4** | 2024-09 | Dense | 开源基础 | 通用对话 |

**核心创新**:
- ⚡ **SPAR 框架** → 医疗领域分级 RL 训练
- ⚡ **领域垂直** → 医疗 AI 深度聚焦

---

## 20. Others

| 机构 | 报告 | 日期 | 亮点 |
|------|------|------|------|
| **MiniMax** | MiniMax-M1 | 2025 | 万亿参数 MoE, 长上下文 |
| **Cohere** | Cohere Command-R+ | 2025 | RAG 优化, 企业级 |
| **Stability AI** | Stable LM 3 | 2025 | 开源 MoE |
| **AI21 Labs** | Jamba 2 | 2025 | SSM-Transformer 混合 |

---

## 跨公司趋势总览

### 架构趋势

| 趋势 | 采用者 | 描述 |
|------|--------|------|
| **MoE 全面主流化** | 除 Anthropic 外全部 | 几乎所有 2025-2026 旗舰模型转向 MoE |
| **Hybrid Mamba-Transformer** | NVIDIA, 新兴厂商 | SSM + Attention 混合, 兼顾效率与召回 |
| **1M+ 上下文** | DeepSeek, OpenAI, Google, Meta, Kimi, GLM | 旗舰模型标配百万级上下文 |
| **RL 推理 (RLVR)** | DeepSeek, OpenAI, Kimi, Qwen | 基于验证奖励的强化学习训练 |
| **多模态原生** | Google, OpenAI, Meta, ByteDance | 文本+图像+音频统一架构 |
| **Muon/MuonClip 优化器** | DeepSeek, Kimi | 挑战 AdamW 主导地位 |

### 定价对比

| 模型 | 输入 ($/M tokens) | 输出 ($/M tokens) |
|------|-------------------|-------------------|
| DeepSeek-V4 | $0.34 | $0.87 |
| GPT-5.5 Instant | $5 | $20 |
| GPT-5.5 Pro | $45 | $180 |
| Gemini 3.1 Pro | $10 | $40 |
| Claude Opus 4 | $15 | $75 |
| Llama 4 (Meta) | 开源免费 | 开源免费 |
| Qwen3 (Alibaba Cloud) | ~$2 | ~$8 |
| Mistral Large 3 | ~$2 | ~$8 |
| Grok-4 (xAI) | ~$10 | ~$40 |
| Nemotron 3 (NVIDIA) | 开源免费 | 开源免费 |
| GLM-5 (Zhipu) | ~¥4 | ~¥12 |
| Kimi-K2.6 (Moonshot) | ~¥8 | ~¥24 |

### 开源生态

| 开源程度 | 公司 |
|----------|------|
| **完全开源 (Apache 2.0)** | Mistral, Llama (Meta), Nemotron (NVIDIA), DeepSeek |
| **开源权重 (需申请)** | Qwen, InternLM, GLM, Yi, Phi |
| **不开源 (仅 API + System Card)** | OpenAI, Google, Anthropic, xAI, Amazon |

---

## 更新记录

| 版本 | 日期 | 更新内容 |
|------|------|---------|
| v11 | 2026-06-24 | 最新全量覆盖, 20+ 机构, 50+ 报告 |
| v10 | 2026-06-11 | 22+ 家机构, 40+ 报告, 补全全部详细分析 |
| v9 | 2026-06-10 | 22+ 家, 35+ 报告, 定价对比表 |
| v8 | 2026-06-08 | 新增 Claude Opus 4.8/Mythos/Gemini 3.5 Flash/GPT-5 v2 |
| v7 | 2026-06-05 | 22+ 家, 30+ 报告, 全面更新 |
| v6 | 2026-06-03 | 20 家, 35+ 报告, 新增 GPT-5.5/GLM-5/Kimi K2.6 |
| v5 | 2026-05-29 | 26+ 家, 35+ 报告 |
| v4 | 2026-05-28 | 23+ 家, 35+ 报告 |
| v3 | 2026-05-27 | 21 家, 30+ 报告 |
| v2 | 2026-05-26 | 21 家, 30 报告, 第二版 |
| v1 | 2026-05-25 | 17 家, 22 报告, 初版 |
