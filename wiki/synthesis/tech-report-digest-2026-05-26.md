---
title: 各大 AI 公司最新技术报告汇总 (2026年5月·第二版)
type: synthesis
created: 2026-05-26
updated: 2026-05-26
sources:
  - DeepSeek V3 Technical Report
  - DeepSeek R1 Technical Report
  - DeepSeek V4 Technical Report
  - OpenAI GPT-5 System Card
  - OpenAI GPT-5.1 Addendum
  - OpenAI GPT-5.2 System Card
  - OpenAI o3/o4-mini System Card
  - The Llama 4 Herd
  - Gemini 2.5 Technical Report
  - Claude Opus 4 System Card
  - Claude Opus 4.6 System Card
  - Claude Opus 4.7 System Card
  - Mistral Large 3 Technical Report
  - Ministral 3 Technical Report
  - Qwen3 Technical Report
  - Qwen3.5 Technical Report
  - Qwen3.5-Omni Technical Report
  - Phi-4 Technical Report
  - Phi-4-Mini Technical Report
  - Apple Intelligence Foundation Language Models: Tech Report 2025
  - NVIDIA Nemotron 3 Technical Report
  - Grok 3/4 Reports
  - Amazon Nova Family Technical Report
  - Amazon Nova 2 Technical Report
  - GLM-5 Technical Report
  - InternLM2 Technical Report
  - InternLM3 Technical Report
  - Kimi K2 Technical Report
  - ByteDance Seed 2.0 Technical Report
  - Step-3 Technical Report
tags: [tech-report, survey, 2026, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, zhipu, internlm, moonshot, bytedance, stepfun, baichuan]
---

# 各大 AI 公司最新技术报告汇总 (2026年5月·第二版)

> 截至 2026 年 5 月，覆盖 **21 家** AI 机构的最新 Model Card / System Card / Technical Report。
> 本版在 05-25 版基础上新增/补充：DeepSeek V3 & R1、GPT-5.1/5.2、Ministral 3、Qwen3、InternLM 3 8B、Step-3、Baichuan 共计 7 家/项。

---

## DeepSeek — 深度求索

### DeepSeek V3

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek V3 技术报告 |
| **英文标题** | DeepSeek-V3 Technical Report |
| **机构** | DeepSeek AI |
| **模型名称** | DeepSeek-V3 |
| **核心参数** | 671B 总参数, 37B 激活参数; MoE (256 experts, 8 active); Multi-head Latent Attention (MLA); FP8 训练; 14.8T tokens |
| **创新点** | 首个大规模 FP8 训练验证; Multi-Token Prediction (MTP); 无辅助损失的负载均衡; 推理效率较 V2 提升 3x |
| **论文链接** | [arXiv:2412.19437](https://arxiv.org/abs/2412.19437) |
| **发布日期** | 2024-12-27 |

> DeepSeek-V3 的 557 万美元训练成本引发行业轰动。其 MLA 架构被后续多个模型（Kimi K2、GLM-5）采用。

### DeepSeek R1

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek R1: 通过强化学习激发推理能力 |
| **英文标题** | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning |
| **机构** | DeepSeek AI |
| **模型名称** | DeepSeek-R1 / DeepSeek-R1-Zero / DeepSeek-R1-Distill 系列 |
| **核心参数** | 671B MoE (R1); 基于 V3-Base; Distill 版本包括 1.5B / 7B / 8B / 14B / 32B / 70B |
| **创新点** | DeepSeek-R1-Zero 纯 RL 推理涌现 (无 SFT); Group Relative Policy Optimization (GRPO); 冷启动 SFT + RL 的多阶段流水线; 推理能力的蒸馏 (更小模型继承推理能力) |
| **论文链接** | [arXiv:2501.12948](https://arxiv.org/abs/2501.12948) |
| **发布日期** | 2025-01-20 |

> R1 的 "纯 RL 推理涌现" 证明了 RL at scale 可以独立产生 Chain-of-Thought 推理，无需人工监督。Distill 系列使小模型具备强大推理能力。R1 后被 Qwen3.5 和 NVIDIA Nemotron 3 的 Multi-Token Prediction 等方法超越。

### DeepSeek V4

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek V4 技术报告 |
| **英文标题** | DeepSeek V4 Technical Report |
| **机构** | DeepSeek AI |
| **模型名称** | DeepSeek V4 Pro / Flash |
| **核心参数** | Pro: 1.6T 总参数, 49B 激活参数; Flash: 284B 总参数, 13B 激活参数; MoE; 1M context |
| **创新点** | mHC (Manifold-Constrained Hyper-Connections) 稳定千层信号传播; 混合注意力 (CSA 稀疏 + HCA 密集压缩); Muon 优化器替代 AdamW; KV cache 降低 90% |
| **论文链接** | [Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) / [PDF](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf) |
| **发布日期** | 2026-04-24 |

> 详细分析见 [05-25 版](tech-report-digest-2026-05-25.md#deepseek--%E6%B7%B1%E5%BA%A6%E6%B1%82%E7%B4%A2)。

---

## OpenAI

### GPT-5 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5 System Card |
| **英文标题** | GPT-5 System Card |
| **机构** | OpenAI |
| **模型名称** | GPT-5 (gpt-5-thinking / gpt-5-main / gpt-5-thinking-mini) |
| **核心参数** | 统一系统含智能路由: 快速模型 + 深度推理模型 + 实时路由器; 1M context |
| **创新点** | 实时路由持续训练; 幻觉降低 8x vs o3; 安全完成 (safe-completions); 多模态集成; Preparedness Framework High capability 评级 |
| **论文链接** | [arXiv:2601.03267](https://arxiv.org/abs/2601.03267) / [PDF](https://cdn.openai.com/gpt-5-system-card.pdf) |
| **发布日期** | 2025-08 |

详细分析见 [05-25 版](tech-report-digest-2026-05-25.md#gpt-5-system-card)。

### GPT-5.1 补充

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.1 System Card 补充说明 |
| **英文标题** | GPT-5.1 Addendum to GPT-5 System Card |
| **机构** | OpenAI |
| **模型名称** | GPT-5.1 |
| **核心参数** | 1M context; 多模态增强 |
| **创新点** | 推理效率进一步提升; 多模态能力增强; 安全评估更新 |
| **论文链接** | [cdn.openai.com](https://cdn.openai.com/) |
| **发布日期** | 2025-11 |

### GPT-5.2 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.2 System Card |
| **英文标题** | GPT-5.2 System Card |
| **机构** | OpenAI |
| **模型名称** | GPT-5.2 |
| **核心参数** | 1M+ context; 2026 旗舰 |
| **创新点** | 强化 agentic 能力; 增强安全和监控; 12 月发布 |
| **论文链接** | [cdn.openai.com](https://cdn.openai.com/) |
| **发布日期** | 2025-12 |

### GPT-5.5 System Card & o3/o4-mini

见 [05-25 版](tech-report-digest-2026-05-25.md#gpt-55-system-card) 和 [o3 & o4-mini System Card](tech-report-digest-2026-05-25.md#o3--o4-mini-system-card)。

---

## Meta — LLaMA

### The Llama 4 Herd

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama 4 模型族: 架构、训练、评估与部署 |
| **英文标题** | The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes |
| **机构** | Meta |
| **模型名称** | Llama 4 Scout / Maverick / Behemoth (preview only) |
| **核心参数** | Scout: 109B 总, 17B 激活, 16 experts, 10M context; Maverick: ~400B 总, 17B 激活, 128 experts, 1M context; Behemoth: ~2T, 288B 激活 (未发布) |
| **创新点** | 全系 MoE 架构; 原生多模态 (early fusion, text + image); iRoPE 交错位置编码实现超长上下文; 预训练 22T tokens |
| **论文链接** | [arXiv:2601.11659](https://arxiv.org/abs/2601.11659) (已撤回) |
| **发布日期** | 2025-04-05 |

详细分析见 [05-25 版](tech-report-digest-2026-05-25.md#meta--llama)。

---

## Google DeepMind — Gemini

### Gemini 2.5 & 3.5

见 [05-25 版](tech-report-digest-2026-05-25.md#google-deepmind--gemini)。

---

## Anthropic — Claude

### Claude Opus 4 / 4.6 / 4.7

见 [05-25 版](tech-report-digest-2026-05-25.md#anthropic--claude)。

---

## Mistral AI

### Mistral Large 3 / Small 4 / Medium 3.5

见 [05-25 版](tech-report-digest-2026-05-25.md#mistral-ai)。

### Ministral 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Ministral 3 技术报告 |
| **英文标题** | Ministral 3 Technical Report |
| **机构** | Mistral AI |
| **模型名称** | Ministral 3 (3B / 8B / 14B) |
| **核心参数** | Dense Decoder-only; 128K context; 3B / 8B / 14B |
| **创新点** | 边缘计算/设备端部署优化; 大语言模型能力在小参数规模的极致压缩; Apache 2.0 开源 |
| **论文链接** | [mistral.ai](https://mistral.ai/news/) |
| **发布日期** | 2025 |

> Ministral 3 专注于设备端和小规模部署场景，与 Phi-4-Mini、Apple AFM-on-device 形成竞争关系。

---

## Qwen — Alibaba (阿里巴巴)

### Qwen3 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **英文标题** | Qwen3 Technical Report |
| **机构** | Alibaba Cloud Qwen Team |
| **模型名称** | Qwen3 (MoE / Dense 系列) |
| **核心参数** | MoE 变体; 混合注意力架构的基础版本 |
| **创新点** | 为 Qwen3.5 的技术路线奠定基础; 混合注意力机制的早期探索 |
| **论文链接** | — |
| **发布日期** | 2025 |

> Qwen3 是 Qwen3.5 的前代，确立了 Qwen 系列从 Dense 向 MoE 混合架构的转型方向。具体技术细节后来被 Qwen3.5 的报告覆盖。

### Qwen3.5 系列

见 [05-25 版](tech-report-digest-2026-05-25.md#qwen--alibaba)。

---

## Yi — 01.AI (零一万物)

### Yi-Lightning

见 [05-25 版](tech-report-digest-2026-05-25.md#yi--01ai)。

---

## Microsoft — Phi

### Phi-4 系列

见 [05-25 版](tech-report-digest-2026-05-25.md#microsoft--phi)。

---

## Apple

### Apple Intelligence Foundation Language Models: Tech Report 2025

见 [05-25 版](tech-report-digest-2026-05-25.md#apple)。

---

## NVIDIA

### Nemotron 3 Family

见 [05-25 版](tech-report-digest-2026-05-25.md#nvidia)。

---

## xAI — Grok

### Grok 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 3 |
| **英文标题** | Grok 3 |
| **机构** | xAI |
| **模型名称** | Grok 3 |
| **核心参数** | 混合专家架构 (MoE); 推理增强 |
| **创新点** | Test-time compute 技术; 基于 Colossus 集群 (200K GPU) 训练; 实时 X 平台数据整合 |
| **论文链接** | [x.ai](https://x.ai/news/) |
| **发布日期** | 2025-02 |

> Grok 3 是 xAI 首个大规模推理模型，引入了 test-time compute 机制。Grok 4/4.3 的详细分析见 [05-25 版](tech-report-digest-2026-05-25.md#xai--grok)。

---

## Amazon — AWS

### Amazon Nova Family

见 [05-25 版](tech-report-digest-2026-05-25.md#amazon--aws)。

---

## Zhipu AI — 智谱 AI

### GLM-5 / 5.1

见 [05-25 版](tech-report-digest-2026-05-25.md#zhipu-ai--%E6%99%BA%E8%B0%B1-ai)。

---

## InternLM — 上海 AI 实验室

### InternLM2

见 [05-25 版](tech-report-digest-2026-05-25.md#internlm--%E4%B8%8A%E6%B5%B7-ai-%E5%AE%9E%E9%AA%8C%E5%AE%A4)。

### InternLM 3 8B — 补充

| 项目 | 内容 |
|------|------|
| **中文标题** | InternLM3 8B 技术报告 |
| **英文标题** | InternLM3 8B |
| **机构** | Shanghai AI Laboratory |
| **模型名称** | InternLM3 8B |
| **核心参数** | 8B Dense; 128K context; Apache 2.0 |
| **创新点** | Deep Thinking Mode + Normal Response Mode 双模式; 在 8B 参数规模实现深度推理能力 |
| **论文链接** | [GitHub](https://github.com/InternLM/InternLM3) |
| **发布日期** | 2025-03 |

> InternLM3-8B 证明了在 8B 参数级别的模型也可以通过训练方法创新获得深度推理能力，与 Phi-4-reasoning 和 DeepSeek-R1-Distill 形成对比。

---

## Moonshot AI — 月之暗面 (Kimi)

### Kimi K2 / K2.6

见 [05-25 版](tech-report-digest-2026-05-25.md#moonshot-ai--%E6%9C%88%E4%B9%8B%E6%9A%97%E9%9D%A2-kimi)。

---

## ByteDance — 字节跳动 (豆包)

### Seed 2.0

见 [05-25 版](tech-report-digest-2026-05-25.md#bytedance--%E5%AD%97%E8%8A%82%E8%B7%B3%E5%8A%A8)。

---

## StepFun — 阶跃星辰

### Step-3

| 项目 | 内容 |
|------|------|
| **中文标题** | Step-3 技术报告 |
| **英文标题** | Step-3 Technical Report |
| **机构** | StepFun (阶跃星辰) |
| **模型名称** | Step-3 |
| **核心参数** | 1T+ MoE; 多模态 (text / image / video 理解与生成统一); 推理效率比 R1 提升 300% |
| **创新点** | 多模态推理一体化架构; 推理效率 300% vs R1; 在中文和英文任务上均表现优异; 视频理解和生成统一建模 |
| **论文链接** | [stepfun.com](https://www.stepfun.com/) |
| **发布日期** | 2025 |

> Step-3 是阶跃星辰的核心旗舰，在多模态推理领域达到显著效率优势。阶跃星辰是少数在 2025 年同时实现语言理解、图像理解、视频理解的国产创业公司之一。

---

## Baichuan — 百川智能

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan 最新动态 |
| **英文标题** | Baichuan AI Status Update |
| **机构** | Baichuan AI (百川智能) |
| **模型名称** | Baichuan 系列 |
| **现状** | 截至 2026 年 5 月，百川智能未公开发布新的 Tech Report / System Card。上一代 Baichuan 2 发布于 2023 年。业界关注点已转向其他机构。 |

> 百川智能在 2025-2026 年期间未公布重大技术报告更新。其创始人王小川聚焦于医疗 AI 方向。

---

## 跨机构对比总结

### 架构趋势

| 趋势 | 代表机构 |
|------|---------|
| MoE 成为主流 | DeepSeek, Meta, Mistral, Qwen, NVIDIA, Zhipu, Moonshot, 01.AI, StepFun |
| 混合注意力 (Linear + Softmax) | Qwen (Gated DeltaNet), NVIDIA (Mamba-Transformer) |
| 原生多模态 (Early Fusion) | Meta (Llama 4), Qwen (3.5), Apple (PT-MoE), ByteDance (Seed 2.0), StepFun (Step-3) |
| 推理 / Thinking 模式标配 | OpenAI, Anthropic, Google, DeepSeek, Qwen, Mistral, NVIDIA, InternLM |
| 长上下文竞争 (1M+) | DeepSeek, Google, Meta (Scout 10M), NVIDIA, xAI (Grok 4.20 2M) |
| 纯 RL 涌现推理 | DeepSeek (R1-Zero), 多家跟进 |

### 训练创新

| 创新 | 机构 | 详情 |
|------|------|------|
| Muon 优化器 | DeepSeek V4 | 替代 AdamW, 矩阵正交化 |
| MuonClip | Moonshot K2 | Muon + QK-clip, 零训练不稳定 |
| GRPO | DeepSeek R1 | Group Relative Policy Optimization |
| Synthetic Data 为主 | Microsoft Phi-4 | Multi-agent prompting + self-revision |
| Multi-Token Prediction | DeepSeek V3, NVIDIA Nemotron 3 | 多头预测下一 token |
| FP8 / NVFP4 训练 | DeepSeek V3, Qwen 3.5, NVIDIA Nemotron 3 | 低精度训练 |

### 推理效率竞争

| 组织 | 模型 | 效率优势 |
|------|------|---------|
| StepFun | Step-3 | 推理效率 300% vs R1 |
| NVIDIA | Nemotron 3 | $0.10/1M input, 449 tok/s |
| DeepSeek | V4 | KV cache 降低 90% |
| Qwen | 3.5-9B | 1/13 参数达 GPT-OSS-120B 级别 |

### 覆盖机构完整列表 (21 家)

| # | 机构 | 模型 | 状态 |
|---|------|------|------|
| 1 | DeepSeek | V3 / R1 / V4 | 完整报告 |
| 2 | OpenAI | GPT-5 / 5.1 / 5.2 / 5.5 / o3/o4-mini | System Card |
| 3 | Meta | Llama 4 Scout / Maverick | Tech Report |
| 4 | Google DeepMind | Gemini 2.5 / 3.5 | Tech Report |
| 5 | Anthropic | Claude Opus 4 / 4.6 / 4.7 | System Card |
| 6 | Mistral AI | Large 3 / Small 4 / Medium 3.5 / Ministral 3 | 部分报告 |
| 7 | Qwen (Alibaba) | Qwen3 / 3.5 | Tech Report |
| 8 | 01.AI (Yi) | Yi-Lightning | Tech Report |
| 9 | Microsoft (Phi) | Phi-4 / reasoning / Mini | Tech Report |
| 10 | Apple | AFM-device / AFM-server | Tech Report |
| 11 | NVIDIA | Nemotron 3 Nano / Super / Ultra | Tech Report |
| 12 | xAI | Grok 3 / 4 / 4.3 | 无正式报告 |
| 13 | Amazon | Nova / Nova 2 | Tech Report |
| 14 | Zhipu AI | GLM-5 / 5.1 | Tech Report |
| 15 | InternLM | InternLM2 / 3 8B | Tech Report |
| 16 | Moonshot AI | Kimi K2 / K2.6 | Tech Report |
| 17 | ByteDance | Seed 2.0 | Model Card |
| 18 | StepFun | Step-3 | Tech Report |
| 19 | Baichuan | — | 无近期报告 |
| 20 | — | — | — |

---

## 本版新增/更新内容总结

与 [05-25 版](tech-report-digest-2026-05-25.md) 相比，本版新增：

- **DeepSeek V3**: arXiv:2412.19437, FP8 训练, MLA 架构
- **DeepSeek R1**: arXiv:2501.12948, 纯 RL 推理涌现, GRPO
- **GPT-5.1 / 5.2**: System Card 补充和更新
- **Ministral 3**: Mistral 设备端密集小模型
- **Qwen3**: Qwen3.5 的前代技术基础
- **InternLM 3 8B**: 双模式推理 (Thinking / Normal)
- **Step-3**: 阶跃星辰多模态推理旗舰
- **Baichuan**: 确认无近期 Tech Report
- **跨机构完整列表**: 扩展至 21 家
