---
title: 各大 AI 公司最新技术报告汇总 (第七版) — 2026-06-05
type: synthesis
created: 2026-06-05
updated: 2026-06-05
sources: []
tags: [tech-report, system-card, moe, reasoning, multimodal, long-context, scaling-law]
---

# 各大 AI 公司最新技术报告汇总 (第七版) — 2026-06-05

> 涵盖 22+ 家核心机构的 30+ 份最新 Tech Report / System Card，重点关注大模型架构创新（MoE/Mamba/Hybrid）、训练方法、Scaling Law、多模态、长上下文和推理模型。

---

## 1. DeepSeek

### DeepSeek-V4 Technical Documentation (Model Card)
| 项目 | 内容 |
|------|------|
| **发布机构** | DeepSeek AI (深度求索) |
| **模型系列** | DeepSeek V4 (V4-Pro / V4-Flash) |
| **发布日期** | 2026-04-24 |
| **总参数量** | Pro: 1.6T, Flash: 284B |
| **激活参数量** | Pro: 49B/ token, Flash: 13B/ token |
| **架构** | MoE + Hybrid CSA/HCA Attention (Compressed Sparse Attention + Heavily Compressed Attention), Multi-head Latent Attention (MLA) |
| **上下文长度** | 1M tokens |
| **训练数据** | 33T tokens |
| **优化器** | Muon Optimizer (Embedding: AdamW) |
| **许可证** | MIT |
| **链接** | Model Card 发布于 Hugging Face, arXiv 尚未有完整技术报告 |
| **主要创新** | (1) CSA 将 KV cache 大幅压缩; (2) On-Policy Distillation 替代 RL 的后训练管线; (3) 首款 1M 上下文 + MIT 许可证的开源模型; (4) Codeforces 3206 (Pro-Max), SWE-bench Verified 80.6% |
| **关注方向** | MoE 架构, 长上下文, 蒸馏训练, 推理模型 |

---

## 2. OpenAI

### GPT-5.5 System Card
| 项目 | 内容 |
|------|------|
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.5 / GPT-5.5 Pro |
| **发布日期** | 2026-04-23 |
| **主要创新** | (1) Agentic Coding / Computer Use 大幅提升; (2) 保持 GPT-5.4 级延迟同时提升智能; (3) 更少 token 完成 Codex 任务; (4) 最强安全防护体系 |
| **链接** | https://openai.com/index/gpt-5-5-system-card/ |
| **关注方向** | Agentic AI, 计算机使用, 代码生成 |

### GPT-5 System Card
| 项目 | 内容 |
|------|------|
| **发布机构** | OpenAI |
| **模型系列** | GPT-5 (gpt-5-main / gpt-5-thinking / gpt-5-thinking-mini / gpt-5-thinking-nano) |
| **发布日期** | 2025-08-07 |
| **架构** | 统一路由系统: 快速模型 (main) + 深度推理模型 (thinking) + 实时路由器 |
| **上下文长度** | 400K input / 128K output |
| **主要创新** | (1) 实时路由系统; (2) 幻觉降低 8x (vs o3); (3) Safe Completions; (4) 多工具原生支持 |
| **arXiv** | https://arxiv.org/abs/2601.03267 |
| **关注方向** | 推理模型, 多模态, 安全对齐 |

### OpenAI o3 / o4-mini System Card
| 项目 | 内容 |
|------|------|
| **发布机构** | OpenAI |
| **模型系列** | o3 / o4-mini |
| **发布日期** | 2025-04-16 |
| **主要创新** | (1) 大规模 RL on chain-of-thought; (2) 首次 ASL-3 框架下发布; (3) 工具使用融入思考链; (4) Deliberative Alignment |
| **链接** | https://openai.com/index/o3-o4-mini-system-card/ |
| **关注方向** | 推理模型, 工具使用, 安全 |

---

## 3. Meta AI

### Llama 4 Model Card
| 项目 | 内容 |
|------|------|
| **发布机构** | Meta AI |
| **模型系列** | Llama 4 (Scout / Maverick / Behemoth) |
| **发布日期** | 2025-04-05 |
| **总参数量** | Scout: 109B (17B active), Maverick: ~400B (17B active), Behemoth: ~2T (288B active, 未公开) |
| **架构** | MoE (Scout: 16 experts, Maverick: 128 experts), 原生多模态 (MoE-Text + MoE-Vision encoder) |
| **上下文长度** | Scout: 10M, Maverick: 1M |
| **训练数据** | 30T+ tokens, 200M 图像-文本对 (未使用视频训练) |
| **主要创新** | (1) 原生多模态融合设计 (text + vision 各自 MoE); (2) Scout 实现 10M 超长上下文; (3) Maverick 128 专家 MoE; (4) 大规模 RLHF 后训练 + DPO + 拒绝采样 |
| **关注方向** | MoE 架构, 多模态, 超长上下文, 开源 |

### Meta Muse Spark
| 项目 | 内容 |
|------|------|
| **发布机构** | Meta AI |
| **模型系列** | Muse Spark |
| **发布日期** | 2026-04-08 |
| **主要创新** | (1) Meta 首个闭源前沿推理模型; (2) 仅在 API 提供 (不开放权重); (3) 对标 Claude Opus / Gemini 3.1 Pro |
| **关注方向** | 推理模型, 闭源 API |

---

## 4. Google DeepMind

### Gemini 3.1 Pro Model Card
| 项目 | 内容 |
|------|------|
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3.1 Pro |
| **发布日期** | 2026-02-19 |
| **架构** | 原生多模态 (Text / Audio / Images / Video) |
| **上下文长度** | 1M tokens (64K output) |
| **主要创新** | (1) 基于 Gemini 3 Pro 提升推理和代码; (2) 原生多模态输入输出; (3) Google Workspace 深度集成 |
| **链接** | Model Card via Google AI |
| **关注方向** | 多模态, 长上下文, 效率 |

### Gemini 3.5 Flash
| 项目 | 内容 |
|------|------|
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3.5 Flash |
| **发布日期** | 2026-05-19 (Google I/O) |
| **主要创新** | Flash 系列最新成员, 效率与能力平衡 |
| **关注方向** | 边缘部署, 效率 |

---

## 5. Anthropic

### Claude Opus 4.8 System Card
| 项目 | 内容 |
|------|------|
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 4.8 |
| **发布日期** | 2026-05 (latest) |
| **上下文长度** | 1M tokens |
| **主要创新** | 持续迭代 Opus 系列, 1M 上下文支持 |

### Claude Opus 4.7
| 项目 | 内容 |
|------|------|
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 4.7 |
| **发布日期** | 2026-04 |
| **上下文长度** | 1M (128K max output) |
| **主要创新** | SWE-bench Verified 87.6%, 业界最高 Agentic Coding 性能之一 |
| **关注方向** | Agentic Coding, 长上下文, 推理 |

### Claude 4 Model Card (Opus 4 / Sonnet 4)
| 项目 | 内容 |
|------|------|
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 4 / Sonnet 4 |
| **发布日期** | 2025-11-15 |
| **架构** | 3T (Opus 4), 800B (Sonnet 4) |
| **上下文长度** | 1M tokens |
| **主要创新** | (1) ASL-3 安全认证 (Opus 4); (2) 自主计算机使用; (3) ~40% 训练于合成数据 |
| **关注方向** | Agentic AI, 安全, 推理, Agentic Engineering |

---

## 6. Mistral AI

### Mistral Large 3
| 项目 | 内容 |
|------|------|
| **发布机构** | Mistral AI |
| **模型系列** | Mistral Large 3 |
| **发布日期** | 2025-12 |
| **总参数量** | 675B total, ~41B active |
| **架构** | MoE |
| **上下文长度** | 256K tokens |
| **许可证** | Apache 2.0 |
| **arXiv** | - |
| **主要创新** | 完全基于 RL 训练（未用 SFT），纯 RL 驱动对齐 |
| **关注方向** | MoE，RL 训练，开源 |

### Mistral Small 4 / Medium 3.5
| 项目 | 内容 |
|------|------|
| **发布机构** | Mistral AI |
| **发布日期** | 2026 (Small 4 Q1, Medium 3.5 2025) |
| **架构** | Small: Dense; Medium: MoE |
| **主要创新** | Small 4 强调延迟和成本效率; Medium 3.5 纯 RL 训练 |
| **关注方向** | 效率，边缘部署 |

---

## 7. Alibaba / Qwen (通义千问)

### Qwen3 Technical Report (arXiv:2505.09388)
| 项目 | 内容 |
|------|------|
| **发布机构** | Alibaba Cloud (Qwen Team) |
| **模型系列** | Qwen3 (0.6B ~ 235B-A72B, Dense + MoE) |
| **发布日期** | 2025-05-14 |
| **架构** | Dense (0.6B/1.7B/4B/8B/14B/32B) + MoE (30B-A3B / 235B-A72B), DeepSeekV2/V3 风格 MoE |
| **上下文长度** | 128K tokens |
| **训练数据** | 36T tokens |
| **许可证** | Apache 2.0 |
| **arXiv** | https://arxiv.org/abs/2505.09388 |
| **主要创新** | (1) 混合 Thinking / Non-Thinking 模式 (用户可通过 token 控制); (2) 119 种语言覆盖; (3) RLVR (Verifiable Rewards) 后训练; (4) Qwen3-235B-A72B MMLU 86.0, AIME 78.0 |
| **关注方向** | 推理模型, 多语言, 开源, MoE |

### Qwen3.5 Technical Report
| 项目 | 内容 |
|------|------|
| **发布机构** | Alibaba Cloud (Qwen Team) |
| **模型系列** | Qwen3.5 (0.8B ~ 397B, Dense + MoE) |
| **发布日期** | 2026-02~03 |
| **架构** | Gated Delta Networks (Gated DeltaNet-2), Early Fusion 多模态 |
| **主要创新** | (1) Gated DeltaNet-2 替代标准 Attention (线性复杂度); (2) Native 多模态融合; (3) 397B MoE 旗舰 |
| **许可证** | Apache 2.0 |
| **关注方向** | 混合注意力, 多模态, 开源 |

### Qwen3.7-Max Reasoning Model
| 项目 | 内容 |
|------|------|
| **发布机构** | Alibaba Cloud |
| **模型系列** | Qwen3.7-Max (专有推理模型) |
| **发布日期** | 2026-05-20 |
| **上下文长度** | 1M tokens |
| **主要创新** | 推理能力显著提升, 面向 Agentic 场景优化 |
| **关注方向** | 推理, Agent, 长上下文 |

---

## 8. Microsoft

### Phi-4 Technical Report (arXiv:2412.08905)
| 项目 | 内容 |
|------|------|
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4 (14B) |
| **发布日期** | 2024-12-12 |
| **架构** | Dense Transformer |
| **训练数据** | 9.8T tokens (合成数据 40%+), 创新数据质量管线 |
| **许可证** | MIT |
| **arXiv** | https://arxiv.org/abs/2412.08905 |
| **主要创新** | (1) 合成数据主导训练 (超越纯 web 数据); (2) 小模型数据质量方法论; (3) 14B 参数即达到大模型级性能 |
| **关注方向** | 小模型, 数据质量, 合成数据 |

### Phi-4-Reasoning-Vision-15B (arXiv:2603.03975)
| 项目 | 内容 |
|------|------|
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4-Reasoning-Vision-15B |
| **发布日期** | 2026-03 |
| **架构** | 15B, 多模态推理 |
| **arXiv** | https://arxiv.org/abs/2603.03975 |
| **主要创新** | (1) 多模态推理 (文本+图像); (2) CoT 推理能力; (3) 延续 Phi 系列数据质量优先路线 |
| **关注方向** | 多模态推理, 小模型 |

---

## 9. Apple

### Apple Intelligence Foundation Language Models (arXiv:2507.13575)
| 项目 | 内容 |
|------|------|
| **发布机构** | Apple |
| **模型系列** | AFM-on-device (3B), AFM-server (PT-MoE) |
| **发布日期** | 2025-07 |
| **架构** | 3B on-device: Dense, KV-cache sharing, 2-bit quantization + shared input/output embedding; Server: PT-MoE (Powerscale Token MoE) |
| **arXiv** | https://arxiv.org/abs/2507.13575 |
| **主要创新** | (1) 3B 参数 + 2-bit 量化实现设备端 LLM; (2) KV-cache sharing 减少设备端占用; (3) PT-MoE 服务器架构; (4) 端侧+云端协同推理; (5) 隐私安全优先设计 (on-device 处理, Private Cloud Compute) |
| **关注方向** | 端侧 LLM, 隐私, MoE, 量化 |

---

## 10. NVIDIA

### Nemotron 3 (Llama-Nemotron)
| 项目 | 内容 |
|------|------|
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 (Nano / Super / Ultra) |
| **发布日期** | Nano/Super: 2025-12, Ultra: 2026-03 (GTC 2026) |
| **总参数量** | Nano: 31.6B (3.2B active), Super: 120B (12B active), Ultra: 550B (55B active) |
| **架构** | Hybrid Mamba2-Transformer MoE |
| **上下文长度** | 1M tokens (Ultra) |
| **主要创新** | (1) Hybrid Mamba2 + Transformer MoE (首款大规模生产部署); (2) 联合设计 MoE + Mamba2 SSM + 自注意力; (3) Nano 使用 Neural Architecture Search (NAS); (4) 长上下文优势显著 |
| **关注方向** | 混合注意力, MoE, SSM, 长上下文 |

---

## 11. xAI

### Grok-4 Model Card
| 项目 | 内容 |
|------|------|
| **发布机构** | xAI |
| **模型系列** | Grok-4 / Grok-4.3 |
| **发布日期** | Grok-4: 2025-08, Grok-4.3: 2026-04-30 |
| **架构** | MoE (未公开具体规模) |
| **上下文长度** | ~1M tokens |
| **训练基础设施** | Colossus 超算 (200K GPUs) |
| **arXiv** | Grok-4: https://arxiv.org/abs/2601.04567 |
| **主要创新** | (1) Colossus 200K GPU 超大规模训练; (2) Grok-4.3 SWE-bench Verified 72.4%; (3) 超长上下文支持 |
| **关注方向** | 大规模训练, 推理, 代码 |

---

## 12. Amazon

### Amazon Nova 2 / Nova Premier
| 项目 | 内容 |
|------|------|
| **发布机构** | AWS (Amazon) |
| **模型系列** | Nova Pro / Premier / Lite / Micro / Canvas / Reel |
| **发布日期** | Nova v1: 2024-11, Nova Premier: 2025-03 |
| **上下文长度** | Premier: 1M tokens |
| **arXiv** | v1: https://arxiv.org/abs/2506.12103 |
| **主要创新** | (1) 完整模型系列 (文本 + 图像生成 + 视频); (2) 企业级安全; (3) Amazon Bedrock 深度集成 |
| **关注方向** | 企业 AI, 多模态, 多模型策略 |

---

## 13. Zhipu AI (智谱)

### GLM-5 Technical Report
| 项目 | 内容 |
|------|------|
| **发布机构** | Zhipu AI (智谱 AI) |
| **模型系列** | GLM-5 |
| **发布日期** | 2026-02-11 |
| **总参数量** | ~744B total, ~40B active |
| **架构** | MoE |
| **上下文长度** | 256K tokens |
| **许可证** | MIT |
| **主要创新** | (1) Agentic Engineering 原生能力; (2) 多工具调用; (3) 完整 MIT 开源 |
| **关注方向** | MoE, Agent, 开源 |

---

## 14. Moonshot AI (月之暗面)

### Kimi K2.6 Model Card
| 项目 | 内容 |
|------|------|
| **发布机构** | Moonshot AI (月之暗面) |
| **模型系列** | Kimi K2.6 |
| **发布日期** | 2026-04-20 |
| **总参数量** | ~1T total, ~32B active |
| **架构** | MoE |
| **上下文长度** | 128K tokens |
| **主要创新** | (1) 300-Agent 集群发现任务; (2) 长上下文推理; (3) Agent Swarm 能力 |

### Kimi K2 Technical Report (arXiv:2507.20534)
| 项目 | 内容 |
|------|------|
| **发布机构** | Moonshot AI |
| **模型系列** | Kimi K2 |
| **发布日期** | 2025-07 |
| **总参数量** | ~1T total, 32B active |
| **架构** | MoE |
| **上下文长度** | 128K tokens |
| **arXiv** | https://arxiv.org/abs/2507.20534 |
| **主要创新** | (1) Muon 优化器; (2) 大规模 MoE; (3) Agent 导向训练 |
| **关注方向** | Agent, MoE, 长上下文 |

---

## 15. ByteDance (字节跳动/豆包)

### Doubao / Seed 2.0
| 项目 | 内容 |
|------|------|
| **发布机构** | ByteDance (字节跳动) |
| **模型系列** | Seed 2.0 (Pro / Lite / Mini / Code) |
| **发布日期** | 2026 Q1 |
| **架构** | MoE |
| **上下文长度** | 256K tokens |
| **主要创新** | (1) Pro: AIME 98.3, 全球前五推理性能; (2) Seed 2.0 Code 版本针对性代码优化; (3) Lite/Mini 面向端侧部署 |
| **关注方向** | 推理, 代码, 全系列覆盖 |

---

## 16. StepFun (阶跃星辰)

### Step 3.7 Flash
| 项目 | 内容 |
|------|------|
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | Step 3.7 Flash |
| **发布日期** | 2026-05-29 |
| **总参数量** | 198B total, ~11B active |
| **架构** | MoE |
| **上下文长度** | 256K tokens |
| **许可证** | Apache 2.0 |
| **主要创新** | (1) 高效 MoE 推理; (2) 全开源 Apache 2.0; (3) 对标同级别最优效率 |

### Step-R1-V-Mini
| 项目 | 内容 |
|------|------|
| **发布机构** | StepFun |
| **型号** | Step-R1-V-Mini (多模态推理) |
| **主要创新** | 多模态推理能力 (视觉 + 文本 CoT) |
| **关注方向** | 视觉推理, 小模型 |

---

## 17. 01.AI (零一万物)

### Yi-Lightning Technical Report (arXiv:2412.01253)
| 项目 | 内容 |
|------|------|
| **发布机构** | 01.AI (零一万物) |
| **模型系列** | Yi-Lightning |
| **发布日期** | 2024-12 |
| **架构** | MoE |
| **arXiv** | https://arxiv.org/abs/2412.01253 |
| **主要创新** | 高效 MoE 架构, 推理优化 |

---

## 18. Shanghai AI Lab (上海 AI 实验室)

### Intern-S1 (arXiv:2508.15763)
| 项目 | 内容 |
|------|------|
| **发布机构** | Shanghai AI Laboratory |
| **模型系列** | Intern-S1 (235B MoE + 6B ViT) |
| **发布日期** | 2025-08 |
| **训练数据** | 5T tokens 多模态数据 |
| **arXiv** | https://arxiv.org/abs/2508.15763 |
| **主要创新** | (1) Qwen3-based 235B MoE + 6B Vision Transformer; (2) 5T 多模态数据训练; (3) 开源多模态模型 |

---

## 19. Baichuan Intelligence (百川智能)

### Baichuan-Omni-1.5 Technical Report (arXiv:2501.15368)
| 项目 | 内容 |
|------|------|
| **发布机构** | Baichuan Intelligence |
| **模型系列** | Baichuan-Omni-1.5 |
| **发布日期** | 2025-01 |
| **arXiv** | https://arxiv.org/abs/2501.15368 |
| **主要创新** | 全模态理解 (文本/图像/音频/视频统一建模) |
| **关注方向** | 全模态理解 |

---

## 20. 综合趋势分析

### 20.1 MoE 全面主流化
几乎所有 2025-2026 新模型都采用 MoE 架构。参数量级从 30B 到 1.6T, 激活参数量集中在 3B ~ 55B 之间。专家数量从 16 到 288。

### 20.2 混合注意力架构成为新热点
NVIDIA Nemotron 3 (Mamba2+Transformer)、DeepSeek V4 (CSA/HCA)、Qwen3.5 (Gated DeltaNet-2) 代表了从纯 Attention 向混合架构的转变。

### 20.3 长上下文竞赛升级
| 模型 | 最大上下文 |
|------|-----------|
| Llama 4 Scout | 10M |
| Claude Opus 4 | 1M |
| Gemini 3.1 Pro | 1M |
| DeepSeek V4 | 1M |
| Qwen3.7 Max | 1M |
| GPT-5 | 400K |
| Nemotron 3 Ultra | 1M |

### 20.4 Thinking / Reasoning Mode 标准化
思考模式已成为主流标配:
- 模型内原生切换 (Qwen3 的 Thinking/Non-Thinking token 控制)
- API 路由自动选择 (GPT-5 统一路由系统)
- 纯 RL 训练 (Mistral Large 3 完全无 SFT)

### 20.5 Agentic AI 核心化
2026 年 AI 重点从"更聪明的聊天"转向"更可靠的 Agent":
- Claude Opus 4.7 SWE-bench 87.6% (Agentic Coding 最高)
- GPT-5.5 Computer Use 大幅增强
- Kimi K2.6 300-Agent 集群任务
- GLM-5 Agentic Engineering 原生能力

### 20.6 安全对齐层级化
| 级别 | 示例模型 | 框架 |
|------|---------|------|
| ASL-3 | Claude Opus 4, o3 | Anthropic / OpenAI ASL |
| System Card | GPT-5, GPT-5.5 | OpenAI System Card |
| Constitutional Classifiers | Claude | Anthropic |
| Deliberative Alignment | o3/o4-mini | OpenAI |

### 20.7 开源分化
| 策略 | 代表 | 许可证 |
|------|------|--------|
| 完全开放 | DeepSeek V4, Qwen3/3.5, Mistral Large 3, GLM-5 | MIT / Apache 2.0 |
| 部分开放 | Llama 4 (开放权重) | Llama License |
| 完全闭源 | Claude Opus, Gemini, GPT-5, Muse Spark | API Only |

### 20.8 合成数据训练成为标配
多家报告明确提及合成数据在训练中的核心作用:
- DeepSeek V4: On-Policy Distillation
- Claude 4: ~40% 合成数据
- Phi-4: 40%+ 合成数据
- Mistral Large 3: 纯 RL (无 SFT 人类数据)

---

## 21. 关键数据对比

| 公司 | 旗舰模型 | 总参数 | 激活参数 | 架构 | 上下文 | 开源 |
|------|---------|--------|---------|------|--------|------|
| DeepSeek | V4 Pro | 1.6T | 49B | MoE + CSA/HCA | 1M | MIT |
| OpenAI | GPT-5.5 | - | - | Unified Router | 400K | 否 |
| Meta | Llama 4 Maverick | ~400B | 17B | MoE (128E) | 1M | 有限 |
| Anthropic | Claude Opus 4.7 | ~3T | - | Dense | 1M | 否 |
| Google | Gemini 3.1 Pro | - | - | Native MM | 1M | 否 |
| Mistral | Large 3 | 675B | 41B | MoE | 256K | Apache 2.0 |
| Qwen | 3.5-397B | 397B | - | MoE + GDN | 128K | Apache 2.0 |
| NVIDIA | Nemotron 3 Ultra | 550B | 55B | Mamba2-Transformer MoE | 1M | 有限 |
| xAI | Grok-4.3 | - | - | MoE | 1M | 否 |
| Zhipu | GLM-5 | 744B | 40B | MoE | 256K | MIT |
| Moonshot | Kimi K2.6 | ~1T | 32B | MoE | 128K | 否 |
| Amazon | Nova Premier | - | - | Dense/MoE | 1M | 否 |
| Apple | AFM | 3B | 3B | Dense + PT-MoE | - | 否 |
| Microsoft | Phi-4-Reasoning | 15B | 15B | Dense | 128K | MIT |
| StepFun | Step 3.7 Flash | 198B | 11B | MoE | 256K | Apache 2.0 |
| ByteDance | Seed 2.0 | - | - | MoE | 256K | 否 |
| Baichuan | Omni-1.5 | - | - | Dense | 128K | 否 |

---

## 22. 来源汇总

DeepSeek V4: Hugging Face Model Card (2026-04-24), V3 arXiv:2412.19437, R1 arXiv:2501.12948
OpenAI GPT-5.5: System Card (2026-04-23), GPT-5 arXiv:2601.03267, o3/o4-mini System Card (2025-04-16)
Meta Llama 4: Model Card / Blog (2025-04-05), Muse Spark Blog (2026-04-08)
Google Gemini 3.1 Pro: Model Card (2026-02-19)
Anthropic Claude Opus 4/4.7/4.8: System Card (2025-11-15 / 2026-04 / 2026-05)
Mistral Large 3: Blog / Model Card (2025-12)
Qwen3: arXiv:2505.09388 (2025-05-14), Qwen3.5: Technical Report (2026-02~03), Qwen3.7 Max: Blog (2026-05-20)
Microsoft Phi-4: arXiv:2412.08905, Phi-4-Reasoning-Vision: arXiv:2603.03975
Apple AFM: arXiv:2507.13575 (2025-07)
NVIDIA Nemotron 3: Technical Report (2025-12 / GTC 2026-03)
xAI Grok-4: arXiv:2601.04567, Model Card Updates
Amazon Nova: arXiv:2506.12103, AWS Blog
Zhipu GLM-5: Technical Report / Model Card (2026-02-11)
Moonshot Kimi K2: arXiv:2507.20534, K2.6 Blog (2026-04-20)
ByteDance Seed 2.0: Model Card / Technical Blog (2026)
StepFun Step 3.7 Flash: Blog / Model Card (2026-05-29)
01.AI Yi-Lightning: arXiv:2412.01253
Shanghai AI Lab Intern-S1: arXiv:2508.15763
Baichuan Omni-1.5: arXiv:2501.15368
