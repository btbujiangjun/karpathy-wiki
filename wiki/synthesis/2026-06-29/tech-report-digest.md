---
title: 各大 AI 公司最新大模型技术报告摘要 (LLM Tech Report Digest)
type: synthesis
created: 2026-06-29
updated: 2026-06-29
sources: []
tags: [tech-report, digest, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, amazon, minimax, 01-ai, zhipu, internlm, moonshot, stepfun, bytedance, xai, nvidia, apple, baichuan]
---

# 各大 AI 公司最新大模型技术报告摘要

> 编译日期：2026-06-29
> 覆盖 2024 Q4 — 2026 Q2 期间发布的主要技术报告

---

## 1. DeepSeek

### 1.1 DeepSeek-V3

| 条目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V3 技术报告 |
| **英文标题** | DeepSeek-V3 Technical Report |
| **发布机构** | DeepSeek-AI |
| **模型名称** | DeepSeek-V3 |
| **发布日期** | 2024-12-27 (v1), 2025-02-18 (v2) |
| **参数量** | 671B 总参数, 37B 激活参数/token |
| **训练数据** | 14.8T tokens |
| **架构** | MoE (Mixture-of-Experts) + Multi-head Latent Attention (MLA) |
| **上下文长度** | 128K tokens |
| **主要创新** | (1) 辅助损失免负载均衡策略 (auxiliary-loss-free load balancing); (2) Multi-Token Prediction (MTP) 训练目标; (3) FP8 混合精度训练; (4) 仅用 2.788M H800 GPU hours 完成全训练 |
| **论文链接** | https://arxiv.org/abs/2412.19437 |

### 1.2 DeepSeek-R1

| 条目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-R1：通过强化学习激励 LLM 推理能力 |
| **英文标题** | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning |
| **发布机构** | DeepSeek-AI |
| **模型名称** | DeepSeek-R1 / DeepSeek-R1-Zero |
| **发布日期** | 2025-01-22 (v1), 2026-01-04 (v2, 发表在 Nature) |
| **参数量** | 671B 总参数, 37B 激活参数/token (基于 V3 底座) |
| **架构** | MoE + MLA + GRPO RL |
| **主要创新** | (1) 纯 RL 激励推理能力 (无需人工标注推理轨迹); (2) emergent 高级推理模式 (self-reflection, verification, dynamic strategy adaptation); (3) DeepSeek-R1-Zero (纯 RL) 与 R1 (RL + cold-start SFT); (4) 蒸馏小模型 (1.5B ~ 70B) |
| **论文链接** | https://arxiv.org/abs/2501.12948 |
| **备注** | 发表于 Nature volume 645, pages 633-638 (2025) |

---

## 2. Meta AI (LLaMA)

### 2.1 Llama 4

| 条目 | 内容 |
|------|------|
| **中文标题** | Llama 4 系列：架构、训练、评估和部署笔记 |
| **英文标题** | The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes |
| **发布机构** | Meta AI |
| **模型名称** | Llama 4 (Scout, Maverick, Behemoth) |
| **发布日期** | 2026-01-15 |
| **架构** | MoE (routed + shared-expert), early-fusion 多模态, iRoPE 长上下文 |
| **核心变体** | Scout (轻量级), Maverick (中量级), Behemoth (教师模型) |
| **训练方法** | Pre-training → Mid-training (长上下文扩展) → Post-training (lightweight SFT + online RL + lightweight DPO) |
| **主要创新** | (1) 纯 MoE 架构; (2) 早期融合多模态; (3) iRoPE 长度泛化 |
| **论文链接** | https://arxiv.org/abs/2601.11659 |
| **备注** | arXiv 文章因作者问题被撤回，但技术细节仍可从官方发布材料获取 |

---

## 3. Google DeepMind (Gemini)

### 3.1 Gemini 2.5 Pro

| 条目 | 内容 |
|------|------|
| **模型名称** | Gemini 2.5 Pro / 2.5 Flash |
| **发布机构** | Google DeepMind |
| **发布日期** | 2025 Q1 — Q2 |
| **备注** | Gemini 2.5 Pro 是 Google 当前最先进的旗舰模型。截至 2026 年 6 月，尚未发布完整的 arXiv 技术报告，但被多个第三方评测和学术引文广泛提及。在 arXiv:2504.10479 (InternVL3) 和 arXiv:2506.11124 等论文中作为最强基线对比。另有 Gemini 3 Pro 在 arXiv:2511.15848 (Step-Audio-R1) 中被提及为 SOTA。 |

---

## 4. Microsoft (Phi)

### 4.1 Phi-4

| 条目 | 内容 |
|------|------|
| **中文标题** | Phi-4 技术报告 |
| **英文标题** | Phi-4 Technical Report |
| **发布机构** | Microsoft Research |
| **模型名称** | Phi-4 |
| **发布日期** | 2024-12-12 |
| **参数量** | 14B |
| **架构** | Dense Transformer (与 Phi-3 架构相似) |
| **训练数据** | 以合成数据为主的高质量数据 |
| **主要创新** | (1) 数据质量驱动的训练配方 (synthetic data throughout training); (2) 超过教师模型 (GPT-4) 的 STEM QA 能力; (3) 创新的 post-training scheme |
| **论文链接** | https://arxiv.org/abs/2412.08905 |

### 4.2 Phi-4-Mini & Phi-4-Multimodal

| 条目 | 内容 |
|------|------|
| **中文标题** | Phi-4-Mini 技术报告：通过 Mixture-of-LoRAs 实现的紧凑多模态语言模型 |
| **英文标题** | Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs |
| **发布机构** | Microsoft |
| **模型名称** | Phi-4-Mini (3.8B), Phi-4-Multimodal |
| **发布日期** | 2025-03-03 |
| **参数量** | 3.8B (Mini), 多模态版含文本/视觉/语音 LoRA |
| **主要创新** | (1) 200K tokens 词表扩展多语言支持; (2) Group Query Attention 提高长序列效率; (3) Mixture-of-LoRAs 模态扩展 (视觉+语言, 视觉+语音, 语音/音频); (4) OpenASR 排行榜第一 |
| **论文链接** | https://arxiv.org/abs/2503.01743 |

### 4.3 Phi-4-reasoning

| 条目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning 技术报告 |
| **英文标题** | Phi-4-reasoning Technical Report |
| **发布机构** | Microsoft Research |
| **模型名称** | Phi-4-reasoning (14B), Phi-4-reasoning-plus |
| **发布日期** | 2025-04-30 |
| **主要创新** | (1) SFT + outcome-based RL 训练推理链; (2) 超越 DeepSeek-R1-Distill-Llama-70B; (3) 推理改进向通用基准的非平凡迁移 |
| **论文链接** | https://arxiv.org/abs/2504.21318 |

### 4.4 Phi-4-reasoning-vision-15B

| 条目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning-vision-15B 技术报告 |
| **英文标题** | Phi-4-reasoning-vision-15B Technical Report |
| **发布机构** | Microsoft Research |
| **模型名称** | Phi-4-reasoning-vision-15B |
| **发布日期** | 2026-03-04 |
| **参数量** | 15B |
| **主要创新** | (1) 紧凑多模态推理模型; (2) 高分辨率动态分辨率编码器; (3) 推理+非推理数据的混合训练; (4) 模式标记 (mode tokens) 实现"快思考+慢思考"统一 |
| **论文链接** | https://arxiv.org/abs/2603.03975 |

---

## 5. Qwen (Alibaba)

### 5.1 Qwen3

| 条目 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **英文标题** | Qwen3 Technical Report |
| **发布机构** | Alibaba (Qwen Team) |
| **模型名称** | Qwen3 系列 (0.6B ~ 235B) |
| **发布日期** | 2025-05-14 |
| **架构** | Dense + MoE 混合架构 |
| **参数量范围** | 0.6B (dense) ~ 235B (MoE: 235B-A22B) |
| **主要创新** | (1) Thinking mode + Non-thinking mode 统一框架; (2) 动态思维预算机制 (thinking budget); (3) 多语言从 29 种扩展到 119 种; (4) 旗舰模型蒸馏小模型的高效知识迁移; (5) Apache 2.0 开源 |
| **论文链接** | https://arxiv.org/abs/2505.09388 |

### 5.2 Qwen3-VL

| 条目 | 内容 |
|------|------|
| **中文标题** | Qwen3-VL 技术报告 |
| **英文标题** | Qwen3-VL Technical Report |
| **发布机构** | Alibaba (Qwen Team) |
| **模型名称** | Qwen3-VL (2B/4B/8B/32B dense, 30B-A3B/235B-A22B MoE) |
| **发布日期** | 2025-11-26 |
| **上下文长度** | 256K tokens (原生支持交错图文) |
| **主要创新** | (1) 增强型 interleaved-MRoPE 空间-时间建模; (2) DeepStack 多级 ViT 特征融合; (3) 基于文本的时间对齐 (video temporal grounding); (4) 纯文本理解能力超越同类文本模型 |
| **论文链接** | https://arxiv.org/abs/2511.21631 |

### 5.3 Qwen3-Omni

| 条目 | 内容 |
|------|------|
| **中文标题** | Qwen3-Omni 技术报告 |
| **英文标题** | Qwen3-Omni Technical Report |
| **发布机构** | Alibaba (Qwen Team) |
| **模型名称** | Qwen3-Omni (30B-A3B) |
| **发布日期** | 2025-09-22 |
| **主要创新** | (1) Thinker-Talker MoE 架构，统一文本/图像/音频/视频感知与生成; (2) 119 种语言文本交互, 19 种语音理解, 10 种语音生成; (3) Thinking 模型跨模态推理; (4) 36 个音频/音视频基准中 22 个 SOTA |
| **论文链接** | https://arxiv.org/abs/2509.17765 |

---

## 6. Amazon (Amazon Nova)

### 6.1 Amazon Nova Family

| 条目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 模型家族：技术报告与模型卡 |
| **英文标题** | The Amazon Nova Family of Models: Technical Report and Model Card |
| **发布机构** | Amazon AGI |
| **模型名称** | Nova Pro / Nova Lite / Nova Micro / Nova Canvas / Nova Reel |
| **发布日期** | 2025-06-17 (arXiv submission) |
| **主要创新** | (1) Pro: 高能力多模态; (2) Lite: 低成本多模态 (图片/视频/文档/文本); (3) Micro: 最低延迟纯文本; (4) Canvas: 专业级图像生成; (5) Reel: 视频生成 |
| **论文链接** | https://arxiv.org/abs/2506.12103 |

---

## 7. MiniMax

### 7.1 MiniMax-M1

| 条目 | 内容 |
|------|------|
| **中文标题** | MiniMax-M1：使用 Lightning Attention 高效扩展测试时计算 |
| **英文标题** | MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention |
| **发布机构** | MiniMax |
| **模型名称** | MiniMax-M1 |
| **发布日期** | 2025-06-16 |
| **参数量** | 456B 总参数, 45.9B 激活参数/token |
| **架构** | Hybrid-Attention (Lightning Attention + Attention) + MoE |
| **上下文长度** | 1M tokens (原生支持, DeepSeek R1 的 8 倍) |
| **主要创新** | (1) 世界首个开源大规模混合注意力推理模型; (2) CISPO RL 算法 (clip importance sampling weights); (3) 全 RL 训练仅需 512 H800 GPUs + 3 周 ($534,700); (4) 40K/80K thinking budget 两个版本 |
| **论文链接** | https://arxiv.org/abs/2506.13585 |

---

## 8. 其他公司备注

以下公司截至 2026-06-29 未在 arXiv 上找到最新的完整技术报告，但其模型在第三方论文中广泛被引用：

| 公司/组织 | 最新模型 | 状态 |
|-----------|----------|------|
| **OpenAI** | GPT-5 / o3 / o4-mini | 未发布公开发技术报告; o3-mini 在 arXiv:2501.18438 中被安全测试引用 |
| **Anthropic** | Claude 4 / Claude Opus 4.7 | 未在 arXiv 上发布技术报告; Claude Opus 4.7 在 arXiv:2606.03410 中被作为基线 |
| **Mistral AI** | Mistral Large / Mistral Small | 未在 arXiv 上找到最新公开技术报告 |
| **xAI (Grok)** | Grok-3 | 未在 arXiv 上发布技术报告 |
| **Yi (01.AI)** | Yi-Lightning | 未在 arXiv 上找到最新公开技术报告 |
| **Baichuan** | Baichuan 4 | 未在 arXiv 上找到最新公开技术报告 |
| **Zhipu AI (GLM)** | GLM-4 / GLM-4.6V | GLM-4.6V-106B 在 arXiv:2601.09668 中被作为基线提及; 未找到独立技术报告 |
| **InternLM** | InternLM3 / InternVL3 | InternVL3 在 arXiv:2504.10479 (2025-04) 中有技术报告，但 InternLM3 最新报告未找到 |
| **Moonshot AI (Kimi)** | Kimi k1.5 | 在 arXiv:2501.12599 有技术报告 |
| **StepFun (阶跃星辰)** | Step-Audio-R1 | 在 arXiv:2511.15848 (2025-11) 有音频推理技术报告 |
| **ByteDance (豆包)** | Doubao / Seed | 未有公开 arXiv 技术报告 |
| **Apple** | Apple Foundation Models | 未有最新公开技术报告 |
| **NVIDIA** | Nemotron / Llama-Nemotron | 未有最新公开技术报告 |

---

## 9. 重点趋势分析

### 9.1 推理模型 (Reasoning Models) 爆发
2025 年是推理模型的元年。从 DeepSeek-R1 (纯 RL 激励推理) 到 Phi-4-reasoning、MiniMax-M1、Qwen3 (thinking/non-thinking 统一)，几乎所有主要玩家都推出了推理增强模型。

### 9.2 MoE 成为主流架构
DeepSeek-V3 (671B/37B)、Qwen3 (235B-A22B)、Llama 4、MiniMax-M1 (456B/45.9B) 均采用 MoE 架构，以更低的激活参数实现更高的模型容量。

### 9.3 混合注意力机制
MiniMax-M1 提出了 Lightning Attention + Softmax Attention 的混合注意力机制，原生支持 1M 上下文窗口。Qwen3-VL 使用 interleaved-MRoPE 支持 256K 上下文。

### 9.4 多模态统一
Qwen3-Omni 实现了 Thinker-Talker MoE 架构，统一文本/图像/音频/视频。Phi-4-Multimodal 通过 Mixture-of-LoRAs 实现模态扩展。Amazon Nova 系列覆盖文本/图像/视频生成全模态。

### 9.5 合成数据与数据质量
Phi-4 展示了以合成数据为中心的训练配方可以超越教师模型。Qwen3 通过知识蒸馏高效构建小模型。

### 9.6 扩展上下文窗口
MiniMax-M1 (1M tokens)、Qwen3-VL (256K)、DeepSeek-V3 (128K) 持续推动上下文长度边界。

---

## 10. 参考文献汇总

| # | arXiv ID | 标题 | 日期 |
|---|----------|------|------|
| 1 | 2412.19437 | DeepSeek-V3 Technical Report | 2024-12 |
| 2 | 2501.12948 | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL | 2025-01 |
| 3 | 2412.08905 | Phi-4 Technical Report | 2024-12 |
| 4 | 2503.01743 | Phi-4-Mini Technical Report | 2025-03 |
| 5 | 2504.21318 | Phi-4-reasoning Technical Report | 2025-04 |
| 6 | 2603.03975 | Phi-4-reasoning-vision-15B Technical Report | 2026-03 |
| 7 | 2505.09388 | Qwen3 Technical Report | 2025-05 |
| 8 | 2511.21631 | Qwen3-VL Technical Report | 2025-11 |
| 9 | 2509.17765 | Qwen3-Omni Technical Report | 2025-09 |
| 10 | 2506.12103 | The Amazon Nova Family of Models | 2025-06 |
| 11 | 2506.13585 | MiniMax-M1: Scaling Test-Time Compute | 2025-06 |
| 12 | 2601.11659 | The Llama 4 Herd | 2026-01 |
| 13 | 2503.12524 | EXAONE Deep: Reasoning Enhanced Language Models | 2025-03 |
| 14 | 2504.10479 | InternVL3 | 2025-04 |
