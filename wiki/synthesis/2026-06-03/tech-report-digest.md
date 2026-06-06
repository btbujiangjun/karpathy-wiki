---
title: 各大 AI 公司最新技术报告汇总 (第六版) — 2026-06-03
type: synthesis
created: 2026-06-03
updated: 2026-06-03
sources: []
tags: [tech-report, system-card, moe, reasoning, multimodal, long-context, scaling-law]
---

# 各大 AI 公司最新技术报告汇总 (第六版) — 2026-06-03

> 涵盖 20 家核心机构的 30+ 份最新 Tech Report / System Card，重点关注大模型架构创新、训练方法、Scaling Law、多模态、长上下文和推理模型。

---

## 1. DeepSeek

### DeepSeek-V4 Technical Documentation / Model Card
| 项目 | 内容 |
|------|------|
| **发布机构** | DeepSeek AI (深度求索) |
| **模型系列** | DeepSeek V4 (V4-Pro / V4-Flash) |
| **发布日期** | 2026-04-24 |
| **总参数量** | Pro: 1.6T, Flash: 285B |
| **激活参数量** | Pro: 49B/ token, Flash: 13B/ token |
| **架构** | MoE + Hybrid CSA/HCA Attention (Compressed Sparse Attention + Heavily Compressed Attention) |
| **上下文长度** | 1M tokens |
| **训练数据** | 33T token |
| **优化器** | Muon Optimizer (Embedding: AdamW) |
| **许可证** | MIT |
| **arXiv** | https://arxiv.org/abs/2412.19437 (V3), https://arxiv.org/abs/2501.12948 (R1) |
| **主要创新** | (1) CSA 将 KV cache 压缩至约 10%（相对 V3.2）; (2) On-Policy Distillation 替代 RL 的后训练管线，融合 10+ 领域专家; (3) 首款 1M 上下文 + MIT 许可证的开源模型; (4) Codeforces 3206 (Pro-Max), SWE-bench Verified 80.6% |
| **关注方向** | MoE 架构, 长上下文, 蒸馏训练, 推理模型 (Think High/Max) |

---

## 2. OpenAI

### GPT-5 System Card
| 项目 | 内容 |
|------|------|
| **发布机构** | OpenAI |
| **模型系列** | GPT-5 (gpt-5-main / gpt-5-thinking / gpt-5-thinking-mini / gpt-5-thinking-nano) |
| **发布日期** | 2025-08-07 |
| **架构** | 统一路由系统: 快速模型 (gpt-5-main) + 深度推理模型 (gpt-5-thinking) + 实时路由器 |
| **上下文长度** | 400K input / 128K output |
| **主要创新** | (1) 实时路由系统在 prompt 层面自动选择 main/thinking 模型; (2) 幻觉降低 8x (vs o3); (3) Safe Completions 安全训练; (4) 多工具原生支持 (web browsing, Python, image processing) |
| **arXiv** | https://arxiv.org/abs/2601.03267 |
| **关注方向** | 推理模型, 多模态, 安全对齐 |

### GPT-5.5 发布
| 项目 | 内容 |
|------|------|
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.5 / GPT-5.5 Pro |
| **发布日期** | 2026-04-23 |
| **主要创新** | (1) Agentic Coding / Computer Use 大幅提升; (2) 保持 GPT-5.4 级延迟同时提升智能; (3) 显著更少 token 完成 Codex 任务; (4) 最强的安全防护体系 |
| **关注方向** | Agentic AI, 计算机使用, 代码生成 |

### OpenAI o3 / o4-mini System Card
| 项目 | 内容 |
|------|------|
| **发布机构** | OpenAI |
| **模型系列** | o3 / o4-mini |
| **发布日期** | 2025-04-16 |
| **主要创新** | (1) 大规模 RL on chain-of-thought; (2) 首次在 ASL-3 框架下发布; (3) 工具使用融入思考链 (web browsing, Python, image analysis, canvas); (4) Deliberative Alignment |
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
| **架构** | MoE (Scout: 16 experts, Maverick: 128 experts) + Native Multimodal (early fusion) + iRoPE (interleaved NoPE layers) |
| **上下文长度** | Scout: 10M, Maverick: 1M |
| **训练数据** | Scout: ~40T tokens, Maverick: ~22T tokens (含 multimodal data) |
| **许可证** | Llama 4 Community License (≤700M MAU 商业免费, EU 多模态受限) |
| **主要创新** | (1) 首个将 MoE + 原生多模态结合的开放模型家族; (2) Scout 的 10M 上下文窗口为业界最大; (3) iRoPE 无需位置编码层实现超长上下文; (4) Maverick 通过 Behemoth codistillation 提升质量 |
| **GitHub** | https://github.com/meta-llama/llama-models |
| **关注方向** | MoE 架构, 超长上下文, 多模态, 开源 |

---

## 4. Google DeepMind

### Gemini 2.5 模型家族 Technical Report
| 项目 | 内容 |
|------|------|
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 2.5 (Pro / Flash / Flash-Lite) |
| **发布日期** | 2025-03-25 (Pro), 后续迭代至 2026 |
| **架构** | Sparse MoE Transformer + Native Multimodal (text, image, audio, video) |
| **上下文长度** | Pro: 1M tokens, Flash: 1M tokens |
| **主要创新** | (1) 内置推理能力 (非 bolt-on); (2) 可调节 thinking budget; (3) 音频+图像原生支持 (Flash); (4) Computer Use 和 Deep Think 模式 |
| **链接** | https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf |
| **关注方向** | MoE, 推理, 多模态, 长上下文, Agent |

### Gemini 3 / 3.1 系列
| 项目 | 内容 |
|------|------|
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 3 Pro (2025-11), Gemini 3.1 Pro (2026-02), Gemini 3.5 Flash (2026-05) |
| **发布日期** | 2025-11 ~ 2026-05 |
| **上下文长度** | 3.1 Pro: 2M tokens |
| **主要创新** | (1) 3.5 Flash 为默认模型, 编码能力超越 3.1 Pro; (2) 多步推理; (3) 价格分层 (Pro vs Flash vs Flash-Lite) |
| **关注方向** | 推理, 多模态, 长上下文, 价格优化 |

---

## 5. Anthropic

### Claude Opus 4 & Sonnet 4 System Card
| 项目 | 内容 |
|------|------|
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 4 / Claude Sonnet 4 |
| **发布日期** | 2025-05-22 |
| **架构** | Hybrid Reasoning LLM (Transformer-based) |
| **上下文长度** | ~200K tokens |
| **许可证** | 闭源 (API) |
| **主要创新** | (1) 首个 ASL-3 部署的前沿模型 (Opus 4); (2) Extended Thinking 模式; (3) 详尽的 Alignment Assessment (含系统性欺骗、sandbagging、reward hacking 评估); (4) 工具使用融入推理循环 |
| **链接** | https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47.pdf |
| **关注方向** | 推理模型, Agentic AI, 安全对齐, ASL-3 |

### 后续迭代 (2025-2026)
| 模型 | 日期 | 关键亮点 |
|------|------|---------|
| Claude Opus 4.1 | 2025-08 | Agent 任务增强, 真实世界编码 |
| Claude Sonnet 4.5 | 2025-09 | Opus 4.1 级能力, 更低价格 |
| Claude Haiku 4.5 | 2025-10 | 最快+最具性价比, 达到 Sonnet 4.5 的 90% 编码性能 |
| Claude Opus 4.5 | 2025-11-24 | SWE-bench 80.9%, 价格降低 67% |
| Claude Opus 4.7 | 2026-05 | 进一步提升 Agentic Coding 能力 |

---

## 6. Mistral AI

### Mistral 3 系列
| 项目 | 内容 |
|------|------|
| **发布机构** | Mistral AI |
| **模型系列** | Mistral Large 3 / Ministral 3 (14B, 8B, 3B) |
| **发布日期** | 2025-12-02 |
| **总参数量** | Large 3: 675B total, ~41B active |
| **架构** | Large 3: Sparse MoE (自 Mixtral 以来首个 MoE); Ministral 3: Dense |
| **上下文长度** | Large 3: 256K tokens |
| **训练数据** | 3,000 张 H200 GPU 训练 |
| **许可证** | Apache 2.0 (全系列) |
| **主要创新** | (1) 开放式 MoE 前沿模型; (2) Native 多模态 (text+image); (3) 全系列 Apache 2.0 许可; (4) 10 模型同时发布覆盖边端到前沿 |
| **链接** | https://mistral.ai/news/mistral-3/ |
| **关注方向** | MoE, 多模态, 开源, 端侧部署 |

### 后续迭代
| 模型 | 日期 | 关键亮点 |
|------|------|---------|
| Mistral Medium 3.5 | 2026-04-29 | 128B dense, SWE-Bench 77.6% |
| Mistral Small 4 | 2026 | 下一代小模型 |

---

## 7. Alibaba (Qwen)

### Qwen3.5 系列 Technical Report
| 项目 | 内容 |
|------|------|
| **发布机构** | Alibaba Cloud (Qwen Team) |
| **模型系列** | Qwen3.5 (397B-A17B / 122B-A10B / 35B-A3B / 27B Dense / Flash / 0.8B~9B Small) |
| **发布日期** | 2026-02-16 (旗舰), 2026-02-24 (中型), 2026-03-02 (小型) |
| **总参数量** | 旗舰: 397B total, 17B active |
| **架构** | Sparse MoE (Gated Delta Networks) + Early-Fusion Native Multimodal |
| **上下文长度** | 256K native (可扩展至 1M tokens) |
| **词汇表** | 250K tokens (较 Qwen3 的 150K 扩展) |
| **语言支持** | 201 种语言/方言 |
| **许可证** | Apache 2.0 |
| **主要创新** | (1) 原生多模态 (text+vision 早期融合); (2) Thinking 和 Non-Thinking 双模式推理; (3) ARIA (Adaptive Rate Interleave Alignment); (4) Thinker-Talker 架构 (Omni); (5) 小模型 (9B GPQA 81.7) 超越大模型 |
| **arXiv** | https://arxiv.org/abs/2604.15804 (Omni) |
| **关注方向** | MoE, 多模态, 开源, 小模型高性能, Agent |

### Qwen3.7 Max
| 项目 | 内容 |
|------|------|
| **发布日期** | 2026-05-20 |
| **主要亮点** | 1M context, 92.4 GPQA Diamond, 中文最强模型 |
| **关注方向** | 推理, 长上下文 |

---

## 8. 智谱 AI (Zhipu AI / Z.ai)

### GLM-5 Technical Report
| 项目 | 内容 |
|------|------|
| **发布机构** | Zhipu AI (智谱 AI, 现品牌 Z.ai) |
| **模型系列** | GLM-5 / GLM-5.1 |
| **发布日期** | 2026-02-11 (GLM-5), 2026-04-07 (GLM-5.1) |
| **总参数量** | ~744B total, ~40B active |
| **架构** | MoE + DeepSeek Sparse Attention (DSA) |
| **上下文长度** | 200K tokens |
| **训练数据** | 28.5T tokens |
| **训练硬件** | 华为昇腾 (Ascend) |
| **框架** | MindSpore |
| **许可证** | 预期 MIT |
| **arXiv** | https://arxiv.org/abs/2602.15763 |
| **主要创新** | (1) 从 "Vibe Coding" 到 "Agentic Engineering" 的范式转换; (2) 异步 RL 基础设施 (decouple generation from training); (3) 异步 Agent RL 算法提升长期交互学习效果; (4) SWE-bench Verified 77.8%; (5) 5.1 版本在长周期 Agent 任务上显著突破 |
| **关注方向** | Agentic AI, 编程, MoE, 长上下文 |

---

## 9. 月之暗面 (Moonshot AI)

### Kimi K2 / K2.5 / K2.6 技术报告
| 项目 | 内容 |
|------|------|
| **发布机构** | Moonshot AI (月之暗面) |
| **模型系列** | Kimi K2 / K2 Thinking / K2.5 / K2.6 |
| **发布日期** | K2: 2025-07-11, K2.5: 2026-01-27, K2.6: 2026-04-20 |
| **总参数量** | ~1T total (~1.04T), ~32B active |
| **架构** | MoE (384 experts, 8 active per token) + MLA (Multi-head Latent Attention) |
| **上下文长度** | K2/K2.5: 128K → K2.6: 256K |
| **训练数据** | 15.5T tokens |
| **优化器** | MuonClip (Muon + QK-Clip 稳定训练) |
| **许可证** | Modified MIT |
| **主要创新** | (1) 超稀疏 MoE (sparsity 48, 384 experts); (2) 合成 Agentic 数据管线 (~20K tools); (3) Self-Critique Rubric Reward 扩展 RLVR; (4) K2.5: Agent Swarm (100 sub-agents, 1500 并行工具调用); (5) K2.6: 300 agents, 4000 coordinated steps, 13h 自主编码; (6) 首次在 1T 级开源模型中验证 Muon 族优化器稳定性 |
| **GitHub** | https://github.com/MoonshotAI/Kimi-K2 |
| **关注方向** | MoE, Agent Swarm, 推理, 多模态, 超长上下文 |

---

## 10. ByteDance (字节跳动)

### Doubao Seed 2.0 系列
| 项目 | 内容 |
|------|------|
| **发布机构** | ByteDance Seed (字节跳动) |
| **模型系列** | Doubao Seed 2.0 (Pro / Code / Lite / Mini) |
| **发布日期** | 2026-02-14 |
| **架构** | Transformer-based, 四层分级 |
| **上下文长度** | Pro/Code: 128K, Lite: 64K, Mini: 32K |
| **主要亮点** | Pro: AIME 2025 98.3, Codeforces 3020, GPQA 88.9, SWE-Bench 76.5, LiveCodeBench 87.8 |
| **多模态** | VideoMME 89.5 (小时级视频理解), 空间/运动推理 |
| **定价** | Pro: $0.47/$2.37 (input/output per M tokens), 极具竞争力 |
| **主要创新** | (1) 四模型分层覆盖 (Agent / Code / High-throughput / Edge); (2) Agent-first 设计 (Pro 全局 Agent 任务排名第三); (3) 多模态视频理解能力领先; (4) 价格约为西方竞品 1/10 |
| **关注方向** | Agent, 推理, 多模态, 分层定价 |

---

## 11. Microsoft

### Phi-4 / Phi-4-Reasoning-Vision 系列
| 项目 | 内容 |
|------|------|
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4 (14B) / Phi-4-mini (3.8B) / Phi-4-multimodal (5.6B) / Phi-4-Reasoning-Vision (15B) |
| **发布日期** | Phi-4: 2024-12-12, Phi-4-RV: 2026-03 |
| **架构** | Decoder-only Transformer |
| **上下文长度** | 16K tokens |
| **许可证** | MIT |
| **arXiv** | https://arxiv.org/abs/2412.08905 (Phi-4), https://arxiv.org/abs/2603.03975 (Phi-4-RV) |
| **主要创新** | (1) 数据质量优先的训练策略 (合成数据 + 精选学术数据); (2) 14B 在 STEM 推理上超越教师模型 GPT-4; (3) Phi-4-RV: 首次在 15B 级融合推理+视觉; (4) 混合推理模式 (快速直接 vs 逐步推理) |
| **关注方向** | 小模型高性能, 数据质量, 多模态推理 |

---

## 12. Apple

### Apple Intelligence Foundation Language Models Tech Report 2025
| 项目 | 内容 |
|------|------|
| **发布机构** | Apple |
| **模型系列** | AFM (On-Device: ~3B / Server: MoE) |
| **发布日期** | 2025-06-09 (更新版) |
| **架构** | On-Device: 2-bit QAT 压缩, KV-cache sharing; Server: PT-MoE (Parallel Track MoE) |
| **主要创新** | (1) 5:3 depth ratio KV-cache sharing (37.5% 节省); (2) 2-bit weights + 4-bit embedding 量化; (3) Private Cloud Compute 隐私架构; (4) Swift Foundation Models 框架 (guided generation, constrained tool calling, LoRA) |
| **arXiv** | https://arxiv.org/abs/2507.13575 |
| **关注方向** | 端侧部署, 隐私, MoE, 量化, 多模态 |

---

## 13. NVIDIA

### Nemotron 3 系列 Technical Report
| 项目 | 内容 |
|------|------|
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 (Nano / Super / Ultra) |
| **发布日期** | Nano: 2025-12-15, Super: 2026-03-11, Ultra: TBD |
| **总参数量** | Nano: 30B (3.2B active), Super: 120B (12B active) |
| **架构** | Mamba2-Transformer Hybrid MoE (Nano: 23 MoE + 23 Mamba2 + 6 GQA layers) |
| **上下文长度** | 1M tokens |
| **训练数据** | Nano: 25T tokens |
| **许可证** | 开放权重 (Permissive) |
| **arXiv** | https://arxiv.org/pdf/2512.20856 (White Paper) |
| **主要创新** | (1) 首个将 Mamba2 + Transformer + MoE 混合的开源模型; (2) LatentMoE (Super/Ultra 上的新型硬件感知专家设计); (3) 多环境 RL Post-training; (4) 细粒度推理预算控制; (5) Multi-Token Prediction (Super/Ultra); (6) NVFP4 训练 (Super/Ultra) |
| **关注方向** | Mamba-Transformer Hybrid, Agentic AI, MoE, 长上下文 |

---

## 14. xAI (Grok)

### Grok 3 / Grok 4 系列
| 项目 | 内容 |
|------|------|
| **发布机构** | xAI |
| **模型系列** | Grok 3 (Beta) / Grok 3 mini / Grok 4 / Grok 4.1 Fast / Grok 4.3 |
| **发布日期** | Grok 3: 2025-02-17, Grok 4: 2025-07-09, Grok 4.3: 2026-05-01 |
| **上下文长度** | Grok 3: 1M, Grok 4.1 Fast: 2M |
| **主要创新** | (1) Grok 3: 10x compute vs 前代, RL 增强 Think 模式, DeepSearch; (2) Grok 4: 100% AIME 2025 (with tools), 88% GPQA; (3) Grok 4.1 Fast: 2M context, 最佳工具调用; (4) Grok 4.3: 语音克隆, 激进定价 |
| **关注方向** | 推理, 长上下文, 实时搜索 |

---

## 15. Amazon

### Amazon Nova 系列 Technical Report
| 项目 | 内容 |
|------|------|
| **发布机构** | Amazon AGI |
| **模型系列** | Nova (Micro / Lite / Pro / Premier) + Nova Canvas (image) + Nova Reel (video) |
| **发布日期** | 2025-03-17 (v1), 2025-12 (Nova 2) |
| **架构** | Transformer + Latent Diffusion (Canvas/Reel) |
| **上下文长度** | Pro: 300K, Premier: 1M |
| **多语言** | 200+ 语言 |
| **arXiv** | https://arxiv.org/abs/2506.12103 |
| **主要创新** | (1) 完整模型生态 (理解+生成+视频); (2) 价格性能比领先 (Micro 210 tok/s); (3) Nova 2 Pro/Lite 具备推理模式; (4) 知识蒸馏支持 (Premier as teacher) |
| **关注方向** | 多模态, 多语言, 价格性能比, 视频生成 |

---

## 16. 上海 AI 实验室 (InternLM)

### InternLM3 技术报告
| 项目 | 内容 |
|------|------|
| **发布机构** | Shanghai AI Lab (上海人工智能实验室) |
| **模型系列** | InternLM3 (8B) |
| **发布日期** | 2025-01-15 |
| **参数量** | 8B |
| **架构** | Transformer + Deep Thinking Mode |
| **上下文长度** | 128K tokens |
| **训练数据** | 4T tokens (仅用 4T 达到其他模型 18T 效果) |
| **许可证** | Apache 2.0 |
| **主要创新** | (1) 首次在通用模型中融合常规对话 + 深度思考; (2) 数据效率革命 (75% 训练成本节省); (3) Intelligent Quality Per Token (IQPT) 框架 |
| **关注方向** | 数据效率, 推理, 开源 |

---

## 17. 阶跃星辰 (StepFun)

### Step 系列模型
| 项目 | 内容 |
|------|------|
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | Step-2 (万亿MoE) / Step-3 (321B MoE) / Step 3.5 Flash (11B active) / Step R-mini / Step-Audio / Step-Video |
| **发布日期** | 持续迭代至 2026-05 |
| **架构** | MoE + MFA (Multi-Matrix Factorization Attention), 5B Vision Encoder |
| **上下文长度** | Step 3.5 Flash: 256K |
| **主要创新** | (1) MFA 注意力机制 (硬件感知低秩注意力, KV cache < DeepSeek-V3); (2) 5B Vision Encoder + 2D 卷积降采样 (视觉 token 减至 1/16); (3) Step 3.5 Flash: 11B active Agent 基座模型, 350 tok/s; (4) Step DeepResearch: 32B 端到端深度研究 Agent (Scale AI 61.4%); (5) Step 3.7 Flash: 400 tok/s, 强化 Agent 能力 |
| **arXiv** | https://arxiv.org/pdf/2512.20491 (DeepResearch) |
| **关注方向** | MoE, 多模态, Agent, 推理, 开源 |

---

## 18. Yi (01.AI) / Baichuan / 其他

（此版本暂未获取到 Yi / Baichuan 的最新完整技术报告，将在后续版本中补充）

---

## 跨机构主题分析

### 1. MoE 全面主导
2025-2026 年发布的绝大部分前沿模型均采用 MoE 架构。关键演进方向：
- **超稀疏化**: Kimi K2 (384 experts, sparsity 48), DeepSeek V4
- **混合注意力**: Mamba2 + Transformer 混合 (Nemotron 3), CSA + HCA 混合 (DeepSeek V4)
- **原生多模态 + MoE**: Llama 4, Qwen3.5, Gemini 2.5

### 2. 推理模型 (Reasoning Model) 成为标配
- OpenAI o3 / GPT-5-thinking / GPT-5.5
- DeepSeek V4 Think High/Max
- Claude Opus 4 extended thinking
- Gemini 2.5 thinking budget
- Kimi K2 Thinking / K2.5 Agent Swarm
- InternLM3 Deep Thinking
- GLM-5 Agentic Engineering

### 3. 后训练创新超越预训练
- **On-Policy Distillation** (DeepSeek V4) 替代传统 RL
- **异步 RL 基础设施** (GLM-5)
- **多环境 RL Post-training** (Nemotron 3)
- **Self-Critique Rubric Reward** (Kimi K2)
- **Agent Swarm** (Kimi K2.5/K2.6)

### 4. 上下文长度竞赛
| 模型 | 最大上下文 |
|------|-----------|
| Llama 4 Scout | 10M |
| Gemini 3.1 Pro | 2M |
| Grok 4.1 Fast | 2M |
| DeepSeek V4 / Nemotron 3 | 1M |
| Qwen3.5 (扩展) | 1M |
| Amazon Nova Premier | 1M |

### 5. 开源生态成熟
| 机构 | 许可证 | 是否开放权重 |
|------|--------|------------|
| DeepSeek V4 | MIT ✅ | ✅ |
| Qwen3.5 | Apache 2.0 ✅ | ✅ |
| Llama 4 | Custom (限制较多) | ✅ |
| Mistral 3 | Apache 2.0 ✅ | ✅ |
| Nemotron 3 | Permissive ✅ | ✅ |
| GLM-5 | 预期 MIT ✅ | ✅ |
| Kimi K2.x | Modified MIT ✅ | ✅ |
| InternLM3 | Apache 2.0 ✅ | ✅ |

### 6. 价格趋近收敛
中国模型厂商 (DeepSeek, Qwen, GLM, Doubao, StepFun) 的 API 价格显著低于西方竞争对手，价格差可达 5-15 倍。这一趋势正在重塑全球 AI 应用开发的成本结构。

---

## 汇总统计

| 维度 | 涵盖报告数 |
|------|-----------|
| 总机构数 | 20 |
| 总报告/文档数 | 35+ |
| MoE 架构 | 14 |
| 多模态 | 12 |
| 推理模型 (Reasoning) | 10 |
| 开源/开放权重 | 12 |
| 长上下文 (≥128K) | 16 |
| 1M+ 上下文 | 6 |
