---
title: 各大 AI 公司最新技术报告汇总 (第八版) — 2026-06-08
type: synthesis
created: 2026-06-08
updated: 2026-06-08
sources: []
tags: [tech-report, system-card, moe, reasoning, multimodal, long-context, scaling-law, agentic-ai]
---

# 各大 AI 公司最新技术报告汇总 (第八版) — 2026-06-08

> 涵盖 22+ 家核心机构的 35+ 份最新 Tech Report / System Card。本版新增 Claude Opus 4.8 System Card、Claude Mythos Preview（受限发布）、Gemini 3.5 Flash 完整规格、GPT-5 arXiv v2 更新、Gemma 4 开源发布，并更新所有已知报告的 arXiv 链接与系统卡 URL。

---

## 1. DeepSeek（深度求索）

### DeepSeek-V4 Technical Documentation
| 项目 | 内容 |
|------|------|
| **模型系列** | DeepSeek V4 (V4-Pro / V4-Flash) |
| **发布日期** | 2026-04-24 |
| **总参数量** | Pro: 1.6T, Flash: 284B |
| **激活参数量** | Pro: 49B/token, Flash: 13B/token |
| **架构** | MoE + Hybrid CSA/HCA (Compressed Sparse Attention + Heavily Compressed Attention), Multi-head Latent Attention (MLA), Manifold-Constrained Hyper-Connections (mHC) |
| **上下文长度** | 1M tokens |
| **训练数据** | 33T tokens |
| **优化器** | Muon (Embedding: AdamW) |
| **推理模式** | Non-think / Think High / Think Max 三种模式 |
| **许可证** | MIT |
| **链接** | [Model Card PDF](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf) · [Hugging Face](https://huggingface.co/collections/deepseek-ai/deepseek-v4) |
| **主要创新** | (1) CSA 将 KV cache 压缩至 V3 的 10%; (2) HCA 128x 压缩密集注意力; (3) Muon 优化器加速收敛; (4) mHC 增强信号传播稳定性; (5) On-Policy Distillation 替代 RL 后训练; (6) Codeforces 3206 (Pro-Max), SWE-bench Verified 80.6%, LiveCodeBench 93.5 |
| **关键词** | MoE, 混合注意力, 长上下文, 稀疏注意力, 开源 |

### DeepSeek-R1 (arXiv:2501.12948)
| 项目 | 内容 |
|------|------|
| **发布日期** | 2025-01-20 |
| **架构** | 671B MoE (37B active), 基于 V3-Base |
| **arXiv** | https://arxiv.org/abs/2501.12948 |
| **主要创新** | (1) 纯 RL 训练 (无 SFT 冷启动 → 推理行为涌现); (2) 可验证奖励 (RLVR) + 语言一致性奖励; (3) 拒绝采样 + SFT 冷启动数据蒸馏; (4) 开源 1.5B ~ 70B 蒸馏模型 |
| **关键词** | 推理模型, RLVR, 蒸馏, MoE |

### DeepSeek-V3 (arXiv:2412.19437)
| 项目 | 内容 |
|------|------|
| **发布日期** | 2024-12-26 |
| **总参数量** | 671B total, 37B active |
| **架构** | MoE + MLA |
| **训练数据** | 14.8T tokens |
| **训练成本** | 2.788M H800 GPU hours |
| **优化器** | AdamW (FP8 混合精度) |
| **arXiv** | https://arxiv.org/abs/2412.19437 |
| **主要创新** | (1) Multi-Token Prediction (MTP); (2) 无辅助损失负载均衡; (3) FP8 混合精度训练; (4) DualPipe 流水线并行; (5) 超稳定训练 (无 loss spike) |

---

## 2. OpenAI

### GPT-5 System Card (arXiv:2601.03267v2)
| 项目 | 内容 |
|------|------|
| **模型系列** | GPT-5 (gpt-5-main / gpt-5-thinking / gpt-5-thinking-mini / gpt-5-thinking-nano) |
| **发布日期** | 2025-08-07 (v2 updated: 2026-05-01) |
| **架构** | 统一路由系统: 快速模型 (main) + 深度推理模型 (thinking) + 实时路由器 |
| **上下文长度** | 400K input / 128K output |
| **arXiv** | https://arxiv.org/abs/2601.03267 |
| **主要创新** | (1) 实时路由系统; (2) 幻觉降低 8x (vs o3); (3) Safe Completions; (4) 多工具原生支持; (5) v2 新增 monitorability evals |
| **关键词** | 推理模型, 统一路由, 安全对齐 |

### GPT-5.5 System Card
| 项目 | 内容 |
|------|------|
| **模型系列** | GPT-5.5 / GPT-5.5 Pro |
| **发布日期** | 2026-04-23 (System Card updated: 2026-04-24) |
| **主要创新** | (1) Agentic Coding / Computer Use 大幅提升; (2) 保持 GPT-5.4 级延迟的同时提升智能; (3) 更少 token 完成 Codex 任务; (4) 最强安全防护体系 (Safe Completions + Preparedness Framework) |
| **链接** | [System Card](https://openai.com/index/gpt-5-5-system-card/) |
| **关键词** | Agentic AI, 计算机使用, 代码生成 |

### OpenAI o3 / o4-mini System Card
| 项目 | 内容 |
|------|------|
| **模型系列** | o3 / o4-mini |
| **发布日期** | 2025-04-16 |
| **主要创新** | (1) 大规模 RL on chain-of-thought; (2) 首次 ASL-3 框架下发布; (3) 工具使用融入思考链; (4) Deliberative Alignment |
| **链接** | [System Card](https://openai.com/index/o3-o4-mini-system-card/) |
| **关键词** | 推理模型, 工具使用, ASL-3 |

---

## 3. Meta AI

### Llama 4 Model Card
| 项目 | 内容 |
|------|------|
| **模型系列** | Llama 4 (Scout / Maverick / Behemoth) |
| **发布日期** | 2025-04-05 |
| **总参数量** | Scout: 109B (17B active), Maverick: ~400B (17B active), Behemoth: ~2T (288B active, 未公开) |
| **架构** | MoE (Scout: 16 experts, Maverick: 128 experts), 原生多模态 (MoE-Text + MoE-Vision encoder) |
| **上下文长度** | Scout: 10M, Maverick: 1M |
| **训练数据** | 30T+ tokens, 200M 图像-文本对 |
| **主要创新** | (1) 原生多模态融合设计; (2) Scout 10M 超长上下文; (3) Maverick 128 专家 MoE; (4) 大规模 RLHF + DPO + 拒绝采样 |
| **关键词** | MoE, 多模态, 超长上下文, 开源 |

### Meta Muse Spark
| 项目 | 内容 |
|------|------|
| **发布日期** | 2026-04-08 |
| **主要创新** | Meta 首个闭源前沿推理模型, 仅 API 提供 |
| **关键词** | 推理模型, 闭源 |

---

## 4. Google DeepMind

### Gemini 3.5 Flash
| 项目 | 内容 |
|------|------|
| **发布日期** | 2026-05-19 (Google I/O) |
| **架构** | 原生多模态 (Text / Audio / Images / Video input, Text output) |
| **主要创新** | (1) 在绝大多数 agentic 基准上超越 3.1 Pro; (2) 比 3.1 Pro 成本低 40%, 速度快 4x; (3) 免费在 Gemini app 中使用; (4) Antigravity 2.0 + Gemini Spark 深度集成 |
| **关键词** | Agentic AI, 多模态, 效率, Google I/O 2026 |

### Gemini 3.1 Pro / Gemini 3.5 Pro (upcoming)
| 项目 | 内容 |
|------|------|
| **发布日期** | 3.1 Pro: 2026-02-19; 3.5 Pro: June 2026 (预计) |
| **上下文长度** | 1M tokens (64K output) |
| **主要创新** | 原生多模态输入输出, Google Workspace 深度集成; 3.5 Pro 将在 6 月发布 |
| **关键词** | 多模态, 长上下文, 企业 |

### Gemma 4 (开源)
| 项目 | 内容 |
|------|------|
| **发布日期** | 2026-04 |
| **定位** | "Byte for byte, the most capable open models" |
| **关键词** | 开源, 小模型 |

---

## 5. Anthropic

### Claude Opus 4.8 System Card
| 项目 | 内容 |
|------|------|
| **发布日期** | May 2026 |
| **上下文长度** | 1M tokens (128K max output) |
| **安全等级** | AI Safety Level 3 |
| **链接** | [System Card](https://anthropic.com/claude-opus-4-8-system-card) |
| **主要创新** | 持续迭代 Opus 系列; 1M 上下文 + ASL-3 安全认证 |
| **关键词** | 安全, 长上下文, ASL-3 |

### Claude Opus 4.7 System Card
| 项目 | 内容 |
|------|------|
| **发布日期** | 2026-04-16 |
| **上下文长度** | 1M tokens (128K max output) |
| **价格** | $5/M input, $25/M output |
| **安全等级** | AI Safety Level 3 |
| **链接** | [System Card](https://anthropic.com/claude-opus-4-7-system-card) |
| **主要创新** | SWE-bench Verified 87.6% (业界最高之一); SWE-bench Pro 64.3%; 视觉基准大幅提升 (XBOW 54.5% → 98.5%); 注意: 长上下文多针检索出现倒退 (8-needle @ 256k: 91.9% → 59.2%) |
| **关键词** | Agentic Coding, 长上下文, 推理, 性能倒退 |

### Claude Mythos Preview
| 项目 | 内容 |
|------|------|
| **发布日期** | 2026-04-07 |
| **定位** | 新 Capybara 层级, 高于 Opus |
| **可用性** | 不公开发布, 仅通过 Project Glasswing 提供给 12 家创始合作伙伴 |
| **SWE-bench Verified** | 93.9% |
| **SWE-bench Pro** | 77.8% |
| **Terminal-Bench 2.0** | 82.0% |
| **USAMO 2026** | 97.6% |
| **链接** | [System Card](https://www.anthropic.com/claude-mythos-preview-system-card) |
| **主要创新** | (1) 自主发现数千 0-day 漏洞 (包括 OpenBSD 27 年未修复 bug); (2) 244 页最详细 System Card; (3) 最"心理稳定"模型; (4) Project Glasswing: $100M 防御性安全项目 |
| **关键词** | 超前沿, 网络安全, 受限发布, Capybara |

### Claude 4 Model Card (Opus 4 / Sonnet 4)
| 项目 | 内容 |
|------|------|
| **发布日期** | 2025-11-15 |
| **架构** | 3T (Opus 4), 800B (Sonnet 4) |
| **上下文长度** | 1M tokens |
| **主要创新** | ASL-3 安全认证; 自主计算机使用; ~40% 合成数据训练 |
| **关键词** | Agentic AI, 安全, 合成数据 |

---

## 6. Mistral AI

### Mistral Large 3
| 项目 | 内容 |
|------|------|
| **发布日期** | 2025-12 |
| **总参数量** | 675B total, ~41B active |
| **架构** | MoE |
| **上下文长度** | 256K tokens |
| **许可证** | Apache 2.0 |
| **主要创新** | 完全基于 RL 训练 (未用 SFT), 纯 RL 驱动对齐 |
| **关键词** | MoE, RL 训练, 开源 |

### Mistral Small 4 / Medium 3.5
| 项目 | 内容 |
|------|------|
| **发布日期** | Small 4: 2026 Q1; Medium 3.5: 2025 |
| **架构** | Small: Dense; Medium: MoE |
| **关键词** | 效率, 边缘部署 |

---

## 7. Alibaba / Qwen (通义千问)

### Qwen3 Technical Report (arXiv:2505.09388)
| 项目 | 内容 |
|------|------|
| **模型系列** | Qwen3 (0.6B ~ 235B-A72B, Dense + MoE) |
| **发布日期** | 2025-05-14 |
| **架构** | Dense (0.6B/1.7B/4B/8B/14B/32B) + MoE (30B-A3B / 235B-A72B) |
| **上下文长度** | 128K tokens |
| **训练数据** | 36T tokens |
| **许可证** | Apache 2.0 |
| **arXiv** | https://arxiv.org/abs/2505.09388 |
| **主要创新** | (1) 混合 Thinking / Non-Thinking 模式; (2) 119 种语言; (3) RLVR 后训练; (4) Qwen3-235B-A72B: MMLU 86.0, AIME 78.0 |
| **关键词** | 推理模型, 多语言, 开源, MoE |

### Qwen3.5 Technical Report
| 项目 | 内容 |
|------|------|
| **模型系列** | Qwen3.5 (0.8B ~ 397B, Dense + MoE) |
| **发布日期** | 2026-02~03 |
| **架构** | Gated DeltaNet-2 (线性复杂度), Early Fusion 多模态 |
| **关键词** | 混合注意力, 多模态, 开源 |

### Qwen3.7-Max Reasoning Model
| 项目 | 内容 |
|------|------|
| **发布日期** | 2026-05-20 |
| **上下文长度** | 1M tokens |
| **关键词** | 推理, Agent, 长上下文 |

---

## 8. Microsoft

### Phi-4 Technical Report (arXiv:2412.08905)
| 项目 | 内容 |
|------|------|
| **模型** | Phi-4 (14B) |
| **发布日期** | 2024-12-12 |
| **架构** | Dense Transformer |
| **训练数据** | 9.8T tokens (合成数据 40%+) |
| **许可证** | MIT |
| **arXiv** | https://arxiv.org/abs/2412.08905 |
| **主要创新** | 合成数据主导训练; 小模型数据质量方法论 |
| **关键词** | 小模型, 合成数据, MIT |

### Phi-4-Reasoning-Vision-15B (arXiv:2603.03975)
| 项目 | 内容 |
|------|------|
| **发布日期** | 2026-03 |
| **架构** | 15B, 多模态推理 |
| **arXiv** | https://arxiv.org/abs/2603.03975 |
| **关键词** | 多模态推理, 小模型 |

---

## 9. Apple

### Apple Intelligence Foundation Language Models (arXiv:2507.13575)
| 项目 | 内容 |
|------|------|
| **模型** | AFM-on-device (3B), AFM-server (PT-MoE) |
| **发布日期** | 2025-07 |
| **架构** | 3B on-device: Dense, KV-cache sharing, 2-bit quantization; Server: PT-MoE |
| **arXiv** | https://arxiv.org/abs/2507.13575 |
| **关键词** | 端侧 LLM, 隐私, MoE, 量化 |

---

## 10. NVIDIA

### Nemotron 3 (Llama-Nemotron)
| 项目 | 内容 |
|------|------|
| **模型** | Nemotron 3 (Nano / Super / Ultra) |
| **发布日期** | Nano/Super: 2025-12; Ultra: 2026-03 (GTC) |
| **总参数量** | Nano: 31.6B (3.2B active), Super: 120B (12B active), Ultra: 550B (55B active) |
| **架构** | Hybrid Mamba2-Transformer MoE |
| **上下文长度** | 1M tokens (Ultra) |
| **关键词** | 混合注意力, SSM, 长上下文 |

---

## 11. xAI

### Grok-4 Model Card (arXiv:2601.04567)
| 项目 | 内容 |
|------|------|
| **模型** | Grok-4 / Grok-4.3 |
| **发布日期** | Grok-4: 2025-08; Grok-4.3: 2026-04-30 |
| **架构** | MoE (规模未公开) |
| **上下文长度** | ~1M tokens |
| **训练基础设施** | Colossus 超算 (200K GPUs) |
| **arXiv** | https://arxiv.org/abs/2601.04567 |
| **关键词** | 大规模训练, 推理, 代码 |

---

## 12. Amazon

### Amazon Nova 2 / Nova Premier
| 项目 | 内容 |
|------|------|
| **模型** | Nova Pro / Premier / Lite / Micro / Canvas / Reel |
| **发布日期** | Nova v1: 2024-11; Nova Premier: 2025-03 |
| **上下文长度** | Premier: 1M tokens |
| **arXiv** | https://arxiv.org/abs/2506.12103 |
| **关键词** | 企业 AI, 多模态 |

---

## 13. Zhipu AI (智谱)

### GLM-5 Technical Report
| 项目 | 内容 |
|------|------|
| **模型** | GLM-5 |
| **发布日期** | 2026-02-11 |
| **总参数量** | ~744B total, ~40B active |
| **架构** | MoE |
| **上下文长度** | 256K tokens |
| **许可证** | MIT |
| **关键词** | MoE, Agent, 开源 |

---

## 14. Moonshot AI (月之暗面)

### Kimi K2.6 Model Card
| 项目 | 内容 |
|------|------|
| **发布日期** | 2026-04-20 |
| **总参数量** | ~1T total, ~32B active |
| **架构** | MoE |
| **上下文长度** | 128K tokens |
| **主要创新** | 300-Agent 集群发现任务; Agent Swarm 能力 |

### Kimi K2 Technical Report (arXiv:2507.20534)
| 项目 | 内容 |
|------|------|
| **发布日期** | 2025-07 |
| **总参数量** | ~1T total, 32B active |
| **架构** | MoE |
| **arXiv** | https://arxiv.org/abs/2507.20534 |
| **主要创新** | Muon 优化器; 大规模 MoE; Agent 导向训练 |

---

## 15. ByteDance (字节跳动/豆包)

### Doubao / Seed 2.0
| 项目 | 内容 |
|------|------|
| **模型** | Seed 2.0 (Pro / Lite / Mini / Code) |
| **发布日期** | 2026 Q1 |
| **架构** | MoE |
| **上下文长度** | 256K tokens |
| **主要创新** | Pro: AIME 98.3 (全球前五推理性能) |

---

## 16. StepFun (阶跃星辰)

### Step 3.7 Flash
| 项目 | 内容 |
|------|------|
| **发布日期** | 2026-05-29 |
| **总参数量** | 198B total, ~11B active |
| **架构** | MoE |
| **上下文长度** | 256K tokens |
| **许可证** | Apache 2.0 |

### Step-R1-V-Mini
| 项目 | 内容 |
|------|------|
| **定位** | 多模态推理 (视觉 + 文本 CoT) |

---

## 17. 01.AI (零一万物)

### Yi-Lightning Technical Report (arXiv:2412.01253)
| 项目 | 内容 |
|------|------|
| **发布日期** | 2024-12 |
| **架构** | MoE |
| **arXiv** | https://arxiv.org/abs/2412.01253 |

---

## 18. Shanghai AI Lab (上海 AI 实验室)

### Intern-S1 (arXiv:2508.15763)
| 项目 | 内容 |
|------|------|
| **模型** | Intern-S1 (235B MoE + 6B ViT) |
| **发布日期** | 2025-08 |
| **arXiv** | https://arxiv.org/abs/2508.15763 |

---

## 19. Baichuan Intelligence (百川智能)

### Baichuan-Omni-1.5 (arXiv:2501.15368)
| 项目 | 内容 |
|------|------|
| **发布日期** | 2025-01 |
| **arXiv** | https://arxiv.org/abs/2501.15368 |
| **主要创新** | 全模态理解 (文本/图像/音频/视频统一建模) |

---

## 20. 完整 System Card 索引

| 机构 | 最新 System Card | 链接 |
|------|-----------------|------|
| Anthropic | Claude Opus 4.8 (May 2026) | https://anthropic.com/claude-opus-4-8-system-card |
| Anthropic | Claude Opus 4.7 (Apr 2026) | https://anthropic.com/claude-opus-4-7-system-card |
| Anthropic | Claude Mythos Preview (Apr 2026) | https://www.anthropic.com/claude-mythos-preview-system-card |
| Anthropic | Claude Sonnet 4.6 (Feb 2026) | https://anthropic.com/claude-sonnet-4-6-system-card |
| Anthropic | Claude Opus 4.6 (Feb 2026) | https://anthropic.com/claude-opus-4-6-system-card |
| Anthropic | Claude 4 (May 2025) | https://www-cdn.anthropic.com/.../Model_Card_Claude_4.pdf |
| OpenAI | GPT-5.5 (Apr 2026) | https://openai.com/index/gpt-5-5-system-card/ |
| OpenAI | GPT-5 (Aug 2025, v2 May 2026) | https://arxiv.org/abs/2601.03267 |
| OpenAI | o3/o4-mini (Apr 2025) | https://openai.com/index/o3-o4-mini-system-card/ |
| DeepSeek | DeepSeek V4 (Apr 2026) | https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf |
| DeepSeek | DeepSeek R1 (Jan 2025) | https://arxiv.org/abs/2501.12948 |
| DeepSeek | DeepSeek V3 (Dec 2024) | https://arxiv.org/abs/2412.19437 |
| Qwen | Qwen3 (May 2025) | https://arxiv.org/abs/2505.09388 |
| Microsoft | Phi-4 (Dec 2024) | https://arxiv.org/abs/2412.08905 |
| Microsoft | Phi-4-Reasoning-Vision (Mar 2026) | https://arxiv.org/abs/2603.03975 |
| Apple | AFM (Jul 2025) | https://arxiv.org/abs/2507.13575 |
| Amazon | Nova (Nov 2024) | https://arxiv.org/abs/2506.12103 |
| xAI | Grok-4 (Aug 2025) | https://arxiv.org/abs/2601.04567 |
| Moonshot | Kimi K2 (Jul 2025) | https://arxiv.org/abs/2507.20534 |
| 01.AI | Yi-Lightning (Dec 2024) | https://arxiv.org/abs/2412.01253 |
| Shanghai AI Lab | Intern-S1 (Aug 2025) | https://arxiv.org/abs/2508.15763 |
| Baichuan | Omni-1.5 (Jan 2025) | https://arxiv.org/abs/2501.15368 |

---

## 21. 关键数据对比

| 公司 | 旗舰模型 | 总参数 | 激活参数 | 架构 | 上下文 | 开源 |
|------|---------|--------|---------|------|--------|------|
| DeepSeek | V4 Pro | 1.6T | 49B | MoE + CSA/HCA | 1M | MIT |
| OpenAI | GPT-5.5 | - | - | Unified Router | 400K | 否 |
| Meta | Llama 4 Maverick | ~400B | 17B | MoE (128E) | 1M | 有限 |
| Anthropic | Claude Opus 4.7 | ~3T | - | Dense | 1M | 否 |
| Anthropic | Claude Mythos | - | - | Capybara tier | - | 受限 |
| Google | Gemini 3.5 Flash | - | - | Native MM | - | 否 |
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

## 22. 综合趋势分析

### 22.1 MoE 全面主流化
几乎所有 2025-2026 新模型都采用 MoE 架构。专家数量从 16 到 288。激活参数量 3B~55B。

### 22.2 混合注意力架构崛起
- NVIDIA Nemotron 3: Mamba2 + Transformer 混合 MoE
- DeepSeek V4: CSA + HCA (稀疏 + 重度压缩注意力)
- Qwen3.5: Gated DeltaNet-2 (线性复杂度替代标准 Attention)

### 22.3 System Card 透明度提升
2026 年 System Card 发布已成行业标准:
- Anthropic 连续发布 Opus 4.6/4.7/4.8 + Mythos 共 4 份 System Card (2026)
- OpenAI 至少 3 份: GPT-5.5, GPT-5 (v2 更新), o3
- DeepSeek V4 发布正式 Model Card PDF

### 22.4 Agentic AI 全面核心化
2026 年 AI 重点从"更聪明的聊天"转向"更可靠的 Agent":
- Claude Opus 4.7 SWE-bench 87.6%, Mythos 93.9%
- GPT-5.5 Computer Use / Agentic Coding
- Kimi K2.6 300-Agent 集群
- GLM-5 Agentic Engineering 原生能力
- Gemini 3.5 Flash 全面 Agentic AI 优化

### 22.5 安全层级进一步细化
- Anthropic: ASL-3 (Opus 4.7/4.8) + 非公开模型 (Mythos)
- OpenAI: Preparedness Framework + Safe Completions
- 受限发布新范式: Claude Mythos 仅通过 Project Glasswing 提供 (12 家合作伙伴)

### 22.6 开源分化格局
| 策略 | 代表 | 许可证 |
|------|------|--------|
| 完全开放 | DeepSeek V4, Qwen3/3.5, Mistral Large 3, GLM-5 | MIT / Apache 2.0 |
| 部分开放 | Llama 4, Nemotron 3 | 自定义 |
| 完全闭源 | Claude, Gemini, GPT-5/5.5, Muse Spark, Nova Premier | API Only |

### 22.7 长上下文竞赛格局
| 模型 | 最大上下文 |
|------|-----------|
| Llama 4 Scout | 10M |
| Claude Opus 4/4.7/4.8 | 1M |
| Gemini 3.1 Pro | 1M |
| DeepSeek V4 | 1M |
| Qwen3.7 Max | 1M |
| Nemotron 3 Ultra | 1M |
| GPT-5 | 400K |

### 22.8 合成数据与 RL 训练
- DeepSeek V4: On-Policy Distillation
- Claude 4: ~40% 合成数据
- Phi-4: 40%+ 合成数据
- Mistral Large 3: 纯 RL (无 SFT)
- o3: 大规模 RL on CoT

---

## 23. 来源汇总

- DeepSeek V4: [Model Card PDF](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf) (2026-04-27) · [Hugging Face](https://huggingface.co/collections/deepseek-ai/deepseek-v4)
- DeepSeek R1: [arXiv:2501.12948](https://arxiv.org/abs/2501.12948) · DeepSeek V3: [arXiv:2412.19437](https://arxiv.org/abs/2412.19437)
- GPT-5.5: [System Card](https://openai.com/index/gpt-5-5-system-card/) · GPT-5: [arXiv:2601.03267](https://arxiv.org/abs/2601.03267) · o3: [System Card](https://openai.com/index/o3-o4-mini-system-card/)
- Meta Llama 4: [Blog](https://ai.meta.com/blog/llama-4/) · Muse Spark: [Blog](https://ai.meta.com/blog/muse-spark/)
- Gemini 3.5 Flash: [Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/) · Gemma 4: [Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)
- Claude Opus 4.8: [System Card](https://anthropic.com/claude-opus-4-8-system-card) · Opus 4.7: [System Card](https://anthropic.com/claude-opus-4-7-system-card) · Mythos: [System Card](https://www.anthropic.com/claude-mythos-preview-system-card) · Claude 4: [System Card](https://www-cdn.anthropic.com/...)
- Qwen3: [arXiv:2505.09388](https://arxiv.org/abs/2505.09388) · Qwen3.5: Technical Report (2026) · Qwen3.7-Max: Blog (2026-05-20)
- Phi-4: [arXiv:2412.08905](https://arxiv.org/abs/2412.08905) · Phi-4-Reasoning-Vision: [arXiv:2603.03975](https://arxiv.org/abs/2603.03975)
- Apple AFM: [arXiv:2507.13575](https://arxiv.org/abs/2507.13575)
- NVIDIA Nemotron 3: Technical Report (2025-12 / GTC 2026-03)
- xAI Grok-4: [arXiv:2601.04567](https://arxiv.org/abs/2601.04567)
- Amazon Nova: [arXiv:2506.12103](https://arxiv.org/abs/2506.12103)
- Zhipu GLM-5: Technical Report / Model Card (2026-02-11)
- Kimi K2: [arXiv:2507.20534](https://arxiv.org/abs/2507.20534) · K2.6: Blog (2026-04-20)
- ByteDance Seed 2.0: Model Card (2026)
- StepFun Step 3.7 Flash: Blog (2026-05-29)
- Yi-Lightning: [arXiv:2412.01253](https://arxiv.org/abs/2412.01253)
- Intern-S1: [arXiv:2508.15763](https://arxiv.org/abs/2508.15763)
- Baichuan Omni-1.5: [arXiv:2501.15368](https://arxiv.org/abs/2501.15368)
