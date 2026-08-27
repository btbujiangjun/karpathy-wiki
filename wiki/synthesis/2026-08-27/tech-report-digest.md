---
title: "LLM Tech Report Digest — 2026-08-27"
type: synthesis
created: 2026-08-27
updated: 2026-08-27
tags: [tech-report, llm, moe, mamba, multimodal, reasoning, scaling, digest]
sources: []
---

# LLM Tech Report Digest — 2026-08-27

> 最近半年主流厂商 LLM 技术报告/系统卡摘要，附核心参数、架构创新与链接。
> Last updated: 2026-08-27

---

## 目录 / Table of Contents

| # | 机构 | 模型 | 发布日期 | 核心架构 |
|---|------|------|----------|----------|
| 1 | DeepSeek | DeepSeek-V3 | 2025-01 | MoE 671B/37B |
| 2 | OpenAI | GPT-5.6 / GPT-5.5 / GPT-Live | 2026-04~07 | Closed |
| 3 | Meta AI | Llama 4 (Scout/Maverick) | 2025-04 | MoE |
| 4 | Google DeepMind | Gemini 2.5 (Pro/Flash) | 2025-07 | 混合架构 |
| 5 | Anthropic | Claude Opus 5 / Sonnet 5 / Opus 4.8 | 2026-05~07 | Closed |
| 6 | Mistral AI | Mistral Large 3 / Mistral Small 4 / Forge | 2025-12~2026 | Dense + MoE |
| 7 | Qwen (Alibaba) | Qwen3 (0.6B–235B) | 2025-05 | Dense + MoE，Thinking/Non-thinking 统一 |
| 8 | Microsoft | Phi-4 / Phi-4-Mini | 2024-12~2025-03 | Dense + MoLo (Mixture-of-LoRAs) |
| 9 | Apple | Apple Intelligence FLM 2025 | 2025-07 | On-device ~3B + Server |
| 10 | NVIDIA | Nemotron 3 Ultra (MoE Hybrid Mamba) | 2025-12~2026-06 | MoE + Mamba Hybrid |
| 11 | xAI | Grok 4.6 | 2026 | Closed，无公开技术报告 |
| 12 | Amazon | Nova (Pro/Lite/Micro/Canvas/Reel) | 2025-06 | 多模态多任务 |
| 13 | Zhipu AI | GLM-5 | 2026-02 | Agent Engineering |
| 14 | Moonshot AI | Kimi K2 | 2025-07 | Ultra-sparse MoE + MLA |
| 15 | StepFun | Step-3 | 2025-07 | Model-system co-design |
| 16 | ByteDance | Seed-Thinking-v1.5 | 2025-04 | MoE 200B/20B active |
| 17 | Baichuan | Baichuan-M3 (235B) | 2026-02 | 医疗增强，SPAR RL |
| 18 | InternLM (上海AI Lab) | InternLM3-8B / InternVL3 | 2025-01~04 | 轻量高效 + 多模态 |
| 19 | 01.AI | Yi-Lightning | 2024-12 | Enhanced MoE |

---

## 1. DeepSeek — DeepSeek-V3

| 字段 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V3 技术报告 |
| **英文标题** | DeepSeek-V3 Technical Report |
| **发布机构** | DeepSeek AI |
| **模型系列** | DeepSeek-V3 |
| **发布日期** | 2025-01（arXiv: 2024-12 提交） |
| **参数量** | 总参数 671B，激活参数 37B（MoE） |
| **数据量** | 14.8T tokens（8.1T 用于最终训练阶段） |
| **上下文长度** | 128K |
| **主要创新点** | (1) DeepSeekMoE 架构：细粒度专家 + 共享专家，辅助 loss-free 负载均衡策略；(2) Multi-head Latent Attention (MLA)：压缩 KV cache，推理时 KV 维度大幅降低；(3) FP8 混合精度训练，2048 H800 GPU 上仅用 2.788M GPU-hours 完成训练，成本约为同等规模 Dense 模型的 1/20；(4) Multi-Token Prediction (MTP) 训练目标 |
| **论文链接** | [arXiv:2412.19437](https://arxiv.org/abs/2412.19437) |

---

## 2. OpenAI — GPT-5.6 / GPT-5.5 / GPT-Live

| 字段 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 系统卡 / GPT-5.5 系统卡 / GPT-Live 系统卡 |
| **英文标题** | GPT-5.6 System Card / GPT-5.5 System Card / GPT-Live System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.x |
| **发布日期** | GPT-Live: 2026-07-18；GPT-5.5: 2026-04-30；GPT-5.6: 2026-07-17 |
| **参数量** | 未公开 |
| **上下文长度** | GPT-5.6: 400K input tokens |
| **主要创新点** | **GPT-5.6**: 多模态（文本+图像+音频+视频+文本转语音），动态推理时间分配（thinking budget），83.2% SWE-Bench Verified，GDPval 人类偏好率 51.3%（vs Claude Opus 5 49.0%），USABase 高级数学 94.0%；**GPT-5.5**: 安全方面系统性红队，Long Form Factuality 比 GPT-5.4 提升 +21%，ChaosBench 物理模拟 63.2%（vs GPT-5.4 51.7%）；**GPT-Live**: 2025-12-05 截断训练，额外音频/视频模态，68.9% GAIA Level 1（2025-12 截断），"feels like talking to a good friend" 氛围 |
| **论文链接** | [GPT-5.6 System Card](https://cdn.openai.com/gpt-5-6-system-card.pdf) · [GPT-5.5 System Card](https://cdn.openai.com/gpt-5-5-system-card.pdf) · [GPT-Live System Card](https://cdn.openai.com/gpt-live-system-card.pdf) |

---

## 3. Meta AI — Llama 4

| 字段 | 内容 |
|------|------|
| **中文标题** | Llama 4 系列：Scout 与 Maverick |
| **英文标题** | The Llama 4 Herd of Models |
| **发布机构** | Meta AI |
| **模型系列** | Llama 4 Scout / Maverick |
| **发布日期** | 2025-04 |
| **参数量** | 未完全公开，Scout/Maverick 均为 MoE 架构，总参数规模 400B+ |
| **上下文长度** | Scout: 10M+ tokens（超长上下文） |
| **主要创新点** | (1) MoE 架构：Scout 为 10M+ 超长上下文 MoE；(2) 早期融合（early fusion）原生多模态，文本和图像统一在同一模型；(3) 基于 iRoPE 的长上下文训练策略；(4) 在推理时可动态调整 active expert 数量 |
| **论文链接** | [Meta AI Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) · [HuggingFace](https://huggingface.co/meta-llama) |

---

## 4. Google DeepMind — Gemini 2.5

| 字段 | 内容 |
|------|------|
| **中文标题** | Gemini 2.5 技术报告 |
| **英文标题** | Gemini 2.5: Our most intelligent AI model family |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 2.5 Pro / Flash |
| **发布日期** | 2025-07-10（arXiv: 2507.06261） |
| **参数量** | 未公开 |
| **上下文长度** | 1M+ tokens |
| **主要创新点** | (1) Gemini 2.5 Pro：最智能模型，强推理、代码、数学能力；(2) Gemini 2.5 Flash：低延迟高性价比；(3) Thinking 模式支持静默计算后输出答案；(4) 原生多模态：文本/图像/音频/视频/代码统一处理；(5) 从 2.0 Flash 思考模型进化，遵循 Scaling Law |
| **论文链接** | [arXiv:2507.06261](https://arxiv.org/abs/2507.06261) |

---

## 5. Anthropic — Claude Opus 5 / Sonnet 5 / Opus 4.8

| 字段 | 内容 |
|------|------|
| **中文标题** | Claude Opus 5 / Sonnet 5 / Claude Opus 4.8 系统卡 |
| **英文标题** | Claude Opus 5 System Card / Claude Sonnet 5 System Card / Claude Opus 4.8 System Card |
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 5 / Sonnet 5 / Opus 4.8 |
| **发布日期** | Opus 4.8: 2026-05-22；Sonnet 5: 2026-06-26；Opus 5: 2026-07-11 |
| **参数量** | 未公开 |
| **上下文长度** | 200K（Opus 4.8/Opus 5） |
| **主要创新点** | **Opus 5**: 宣称 "world's most intelligent model"，声称在推理、数学、编程、写作、翻译方面领先，"模型第一次在所有能力上都达到人类专家水平"；**Sonnet 5**: 性价比模型，有 Sonnet 5.6 快思考变体，误报率比 Sonnet 4.6 降低 48%，AppSec 漏洞发现率 +18%；**Opus 4.8**: 256K output token 扩展，agents.benchmark.agentic (aba) 基准，27B 参数变体（训练用） |
| **论文链接** | [Opus 5](https://www.anthropic.com/research/claude-opus-5-system-card) · [Sonnet 5](https://www.anthropic.com/research/claude-sonnet-5-system-card) · [Opus 4.8](https://www.anthropic.com/research/claude-opus-4-8-system-card) |

---

## 6. Mistral AI — Mistral Large 3 / Mistral Small 4 / Forge

| 字段 | 内容 |
|------|------|
| **中文标题** | Mistral Large 3 / Mistral Small 4 / Forge 平台技术报告 |
| **英文标题** | Mistral Large 3 / Mistral Small 4 / Voxtral TTS |
| **发布机构** | Mistral AI |
| **模型系列** | Mistral Large 3 / Mistral Small 4 / Forge |
| **发布日期** | Large 3: 2025-12；Small 4: 2026；Voxtral TTS: 2026-04 |
| **参数量** | Large 3: MoE；Small 4: 更小高效；Voxtral TTS: 语音合成 |
| **主要创新点** | **Mistral Large 3**: Multimodal Live API，实时多模态交互，128K context，tool calling + agentic workflow，Multi-head Latent Attention；**Mistral Small 4**: 更强 token 感知型视觉模型，更快更便宜；**Forge**: Enterprise-grade API 平台，价格比竞品便宜 8 倍，3-6x 吞吐提升；**Voxtral TTS**: 支持 8+ 语言的文本转语音模型 |
| **论文链接** | [Mistral Large 3](https://arxiv.org/abs/2503.15554) · [Forge Blog](https://mistral.ai/news/forge/) |

---

## 7. Qwen (Alibaba) — Qwen3

| 字段 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **英文标题** | Qwen3 Technical Report |
| **发布机构** | Alibaba / Qwen Team |
| **模型系列** | Qwen3（0.6B, 1.7B, 4B, 8B, 14B, 32B, 30B-A3B, 235B-A22B） |
| **发布日期** | 2025-05（arXiv: 2505.09388） |
| **参数量** | Dense: 0.6B–32B；MoE: 30B-A3B, 235B-A22B |
| **数据量** | 36T+ tokens（Qwen2.5 基础上，Qwen3 额外增加 44% 代码+数学数据，新增 28 种语言数据，总 token 从 18T 增至 36T+） |
| **上下文长度** | 32K（默认），支持 128K |
| **主要创新点** | (1) Thinking/Non-thinking 统一架构：训练时在思考与非思考模式间切换，推理时用 thinking_budget 参数动态控制思考深度；(2) 长期四阶段训练流程：预训练（30T → 36T+）、思考模式冷启动、思考模式 RL（30+ 任务，含代码/数学/推理/多语言/工具）、通用 RL（11 任务，含 instructions following/agent）；(3) 235B MoE 仅激活 22B，推理时可"即时思考"（thinking at inference time） |
| **论文链接** | [arXiv:2505.09388](https://arxiv.org/abs/2505.09388) |

---

## 8. Microsoft — Phi-4 / Phi-4-Mini

| 字段 | 内容 |
|------|------|
| **中文标题** | Phi-4 技术报告 / Phi-4-Mini 技术报告 |
| **英文标题** | Phi-4 Technical Report / Phi-4-Mini Technical Report |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4（14B dense）/ Phi-4-Mini（3.8B） |
| **发布日期** | Phi-4: 2024-12（arXiv: 2412.08905）；Phi-4-Mini: 2025-03（arXiv: 2503.01743） |
| **参数量** | Phi-4: 14B；Phi-4-Mini: 3.8B |
| **上下文长度** | Phi-4: 16K；Phi-4-Mini: 128K |
| **主要创新点** | **Phi-4**: (1) 合成数据为核心（教科书级高质量合成数据），多源数据课程学习；(2) 采用 RealWebQA 等真实 QA 数据补充；(3) 在 STEM/推理任务上超越同量级模型。**Phi-4-Mini**: (1) MoLo (Mixture-of-LoRAs) 多模态：文本+视觉+音频多模态统一；(2) 高质量多模态合成数据；(3) 在手机端高效运行；(4) 支持 tool use + function calling |
| **论文链接** | [Phi-4](https://arxiv.org/abs/2412.08905) · [Phi-4-Mini](https://arxiv.org/abs/2503.01743) |

---

## 9. Apple — Apple Intelligence Foundation Language Models 2025

| 字段 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型 2025 |
| **英文标题** | Apple Intelligence Foundation Language Models 2025 |
| **发布机构** | Apple |
| **模型系列** | Apple Foundation LMs (On-device ~3B + Server) |
| **发布日期** | 2025-07（arXiv: 2507.13575） |
| **参数量** | On-device: ~3B；Server: 更大未公开 |
| **主要创新点** | (1) On-device 3B 模型：优化 iPhone/iPad 上运行效率；(2) Server 模型：处理复杂任务，隐私+性能平衡；(3) Private Cloud Compute：设备端数据不离开设备，服务器端用加密计算保护数据；(4) 融合 Writing Tools、Image Playground、Genmoji 等功能；(5) 2025 年 WWDC 发布，已深度集成 iOS/macOS |
| **论文链接** | [arXiv:2507.13575](https://arxiv.org/abs/2507.13575) |

---

## 10. NVIDIA — Nemotron 3 Ultra (MoE Hybrid Mamba)

| 字段 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 系列：Nano / Super / Ultra |
| **英文标题** | Nemotron 3 Family |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 Nano（8B）/ Super（49B）/ Ultra（253B，MoE Hybrid Mamba） |
| **发布日期** | Nano/Super/Ultra: 2025-12；Ultra 系列：2026-06 |
| **参数量** | Nano: 8B；Super: 49B；Ultra: 253B MoE |
| **上下文长度** | Ultra: 128K（Mamba 混合架构支持长序列） |
| **主要创新点** | (1) Hybrid Mamba 架构：结合 Transformer attention + Mamba state-space model，推理效率大幅提高；(2) Ultra 是 253B MoE + Mamba 混合，256 个 expert 中激活 8 个；(3) MoE 拓扑优化：expert 选择策略降低通信开销；(4) 支持大 batch 推理，吞吐量比纯 Transformer MoE 高 2-5x；(5) Strong release for physical AI, robotics, drug discovery 应用 |
| **论文链接** | [NVIDIA Nemotron 3 Ultra Blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra/) |

---

## 11. xAI — Grok 4.6

| 字段 | 内容 |
|------|------|
| **中文标题** | Grok 4.6 |
| **英文标题** | Grok 4.6 |
| **发布机构** | xAI |
| **模型系列** | Grok 4 系列 |
| **发布日期** | 2026 |
| **参数量** | 未公开（推测 MoE 架构，27B active 变体） |
| **主要创新点** | (1) 据 x.ai 宣称，是"world's most intelligent model"；(2) 深度集成 X（Twitter）平台；(3) 多模态输入（图像/视频/文档）；(4) 内置 DeepSearch 能力；(5) 未发布公开技术报告，参数与训练细节未知 |
| **论文链接** | [x.ai](https://x.ai) · 无公开技术报告 |

---

## 12. Amazon — Amazon Nova Family

| 字段 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 家族技术报告 |
| **英文标题** | Amazon Nova: Technical Report |
| **发布机构** | Amazon Web Services (AWS) |
| **模型系列** | Nova Pro / Lite / Micro / Canvas / Reel |
| **发布日期** | 2025-06（arXiv: 2506.12103） |
| **参数量** | Micro: 最小高效；Lite: 轻量；Pro: 最强 |
| **上下文长度** | 300K |
| **主要创新点** | (1) 多任务多模态家族：文本/图像/视频/音频统一理解；(2) Nova Canvas: 图像生成（文本/图像 → 图像）；(3) Nova Reel: 视频生成；(4) Nova Lite: 亚秒级延迟的轻量模型；(5) Amazon Bedrock 集成，AWS 生态无缝接入；(6) 2025 AWS re:Invent 发布 |
| **论文链接** | [arXiv:2506.12103](https://arxiv.org/abs/2506.12103) |

---

## 13. Zhipu AI — GLM-5

| 字段 | 内容 |
|------|------|
| **中文标题** | GLM-5：从 Vibe Coding 到 Agentic Engineering |
| **英文标题** | GLM-5: From Vibe Coding to Agentic Engineering |
| **发布机构** | Zhipu AI (智谱AI) |
| **模型系列** | GLM-5 |
| **发布日期** | 2026-02（arXiv: 2602.15763） |
| **参数量** | 未公开 |
| **主要创新点** | (1) 从 "Vibe Coding" 到 "Agentic Engineering" 范式转变：强调模型不只是写代码，而是作为工程 agent 参与完整软件开发流程；(2) LongCoT (Long Chain-of-Thought) 推理增强；(3) 自主 agent 能力：工具使用、多步规划、代码执行；(4) 在中文基准上达到顶尖水平；(5) GLM 系列迭代：从 GLM-4 → GLM-5 的全面架构升级 |
| **论文链接** | [arXiv:2602.15763](https://arxiv.org/abs/2602.15763) |

---

## 14. Moonshot AI — Kimi K2

| 字段 | 内容 |
|------|------|
| **中文标题** | Kimi K2：Agentic Intelligence 模型 |
| **英文标题** | Kimi K2 Technical Report |
| **发布机构** | Moonshot AI (月之暗面) |
| **模型系列** | Kimi K2 |
| **发布日期** | 2025-07（arXiv: 2507.20534） |
| **参数量** | 未完全公开（超稀疏 MoE 架构） |
| **上下文长度** | 128K |
| **主要创新点** | (1) Ultra-sparse MoE + Multi-head Latent Attention (MLA)：极度稀疏的专家路由 + MLA 压缩 KV cache；(2) MuonClip 优化器：新型优化器改进训练稳定性；(3) Agentic Intelligence：专注 agent 场景，支持工具调用、代码执行、网络搜索；(4) 1T+ tokens 多阶段训练；(5) 中文 AGI 能力在多项基准上达到顶尖水平 |
| **论文链接** | [arXiv:2507.20534](https://arxiv.org/abs/2507.20534) |

---

## 15. StepFun — Step-3

| 字段 | 内容 |
|------|------|
| **中文标题** | Step-3：模型系统协同设计的高效推理 |
| **英文标题** | Step-3: Model-System Co-Design for Cost-Effective Decoding |
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | Step-3 |
| **发布日期** | 2025-07（arXiv: 2507.19427） |
| **参数量** | 未公开 |
| **主要创新点** | (1) Model-system co-design：同时优化模型架构和推理系统，而非独立优化；(2) 针对 decoding 阶段的 cost-effective 设计：优化 KV cache 复用和 memory 带宽；(3) 推理成本大幅降低的同时保持能力；(4) 与芯片/硬件协同设计，面向推理基础设施优化 |
| **论文链接** | [arXiv:2507.19427](https://arxiv.org/abs/2507.19427) |

---

## 16. ByteDance — Seed-Thinking-v1.5

| 字段 | 内容 |
|------|------|
| **中文标题** | Seed-Thinking-v1.5：200B 推理模型 |
| **英文标题** | Seed-Thinking-v1.5 |
| **发布机构** | ByteDance (字节跳动) |
| **模型系列** | Seed-Thinking-v1.5 |
| **发布日期** | 2025-04 |
| **参数量** | 总参数 200B MoE，激活参数 20B |
| **主要创新点** | (1) 200B MoE，仅激活 20B：极致的稀疏激活效率；(2) AIME 2024 达 86.7%：数学竞赛推理能力顶尖；(3) 推理链（thinking chain）生成能力；(4) 面向 deep reasoning 场景优化（数学/代码/逻辑推理）；(5) MoE 稀疏激活策略在推理场景的验证 |
| **论文链接** | [Seed-Thinking Blog](https://seed.bytedance.com/en/research/seed-thinking-v1-5) |

---

## 17. Baichuan — Baichuan-M3 (235B)

| 字段 | 内容 |
|------|------|
| **中文标题** | Baichuan-M3：建模临床问诊，实现可靠医疗决策 |
| **英文标题** | Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making |
| **发布机构** | Baichuan AI (百川智能) |
| **模型系列** | Baichuan-M3 (235B) |
| **发布日期** | 2026-02-06（arXiv: 2602.06570） |
| **参数量** | 235B |
| **主要创新点** | (1) 医疗增强大模型，从"回答正确"升级到"支持决策"；(2) SPAR: Segmented Pipeline Reinforcement Learning，分段流水线强化学习；(3) Fact-Aware RL：事实感知强化学习，减少医疗幻觉；(4) 在 HealthBench/HealthBench-Hard 幻觉评估上超越 GPT-5.2；(5) SCAN-bench 端到端临床决策基准（History Taking + Ancillary Investigations + Final Diagnosis），Baichuan-M3 三个维度均排名第一；(6) 基于 Qwen3 base 模型 |
| **论文链接** | [arXiv:2602.06570](https://arxiv.org/abs/2602.06570) · [Baichuan Blog](https://www.baichuan-ai.com/blog/baichuan-M3) |

---

## 18. InternLM (上海AI Lab) — InternLM3 / InternVL3

| 字段 | 内容 |
|------|------|
| **中文标题** | InternLM3 技术报告 / InternVL3 技术报告 |
| **英文标题** | InternLM3 / InternVL3 |
| **发布机构** | Shanghai AI Lab (上海AI实验室) / InternLM Team |
| **模型系列** | InternLM3-8B / InternVL3 |
| **发布日期** | InternLM3-8B: 2025-01；InternVL3: 2025-04-14（arXiv: 2504.10479） |
| **参数量** | InternLM3: 8B；InternVL3: 多尺寸 |
| **数据量** | InternLM3: 4T 高质量 tokens（比同等规模 LLM 节省 75%+ 训练成本） |
| **主要创新点** | **InternLM3**: (1) 超越 Llama3.1-8B/Qwen2.5-7B，仅 4T tokens 训练，成本大幅降低；(2) 强化推理和知识任务；(3) 开源 Apache-2.0；(4) Spatial-SSRL：自监督 RL 增强空间理解（CVPR 2026 接收）。**InternVL3**: (1) 开源多模态模型，先进训练+测试时策略；(2) 训练数据和权重完全公开，促进研究 |
| **论文链接** | [InternLM3](https://huggingface.co/internlm/internlm3-8b-instruct) · [InternVL3](https://arxiv.org/abs/2504.10479) |

---

## 19. 01.AI — Yi-Lightning

| 字段 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **发布机构** | 01.AI (零一万物) |
| **模型系列** | Yi-Lightning |
| **发布日期** | 2024-12-02（arXiv: 2412.01253） |
| **参数量** | 未完全公开（Enhanced MoE 架构） |
| **词汇量** | 100,352 tokens |
| **主要创新点** | (1) Enhanced MoE 架构：高级专家分割和路由机制 + 优化的 KV-caching；(2) Chatbot Arena 排名第 6，中文/数学/代码/Hard Prompts 类别第 2–4 名；(3) Multi-stage training：预训练+SFT+RLHF 分阶段优化；(4) RAISE (Responsible AI Safety Engine)：四组件安全框架，覆盖预训练/后训练/推理全生命周期；(5) 合成数据构造+奖励建模创新；(6) Benchmark disparity 观察：学术 benchmark 与 Chatbot Arena 人类偏好存在显著差异 |
| **论文链接** | [arXiv:2412.01253](https://arxiv.org/abs/2412.01253) |

---

## 行业趋势总结 / Key Industry Trends

1. **MoE 已成主流架构**：DeepSeek-V3 (671B/37B active), Qwen3 (235B/22B), Kimi K2, Mistral, Yi-Lightning, ByteDance Seed-Thinking 均采用 MoE；激活参数仅为总参数的 1/5–1/20，推理成本大幅降低。

2. **Thinking/Non-Thinking 统一推理**：Qwen3 率先提出 thinking_budget 动态控制，GPT-5.6 的 thinking mode（静默计算后输出），Claude Opus 5 的 extended thinking，Nemotron 3 Ultra 的推理模式，都指向同一方向：模型在思考深度上可调。

3. **长上下文竞赛白热化**：Llama 4 Scout (10M+), GPT-5.6 (400K), Claude Opus 5 (200K), Nova (300K), Gemini 2.5 (1M+)，context window 不断扩大，稀疏注意力和 KV cache 压缩是核心挑战。

4. **Agentic Engineering 范式确立**：GLM-5 明确从 Vibe Coding 到 Agentic Engineering；Kimi K2 定位 Agentic Intelligence；Anthropic Claude Opus 5 强调 agent 能力；OpenAI GPT-5.6 的 agents.benchmark.agentic；模型从"工具"向"工程师同事"角色转变。

5. **医疗/垂直领域增强成为独立赛道**：Baichuan-M2→M3 专注医疗（GRPO+SPAR RL），Apple Intelligence 集成健康功能，Amazon Nova 面向企业场景，垂直领域成为差异化竞争点。

6. **Mamba/SSM 混合架构崛起**：Nemotron 3 Ultra (MoE + Mamba hybrid) 证明 Transformer + 状态空间模型混合在长序列推理上的效率优势，可能成为下一代主流架构方向。

7. **合成数据成为训练核心**：Phi-4（教科书级合成数据）、Qwen3（额外 44% 合成代码/数学数据）、Yi-Lightning（合成数据构造策略），合成数据在后训练阶段的地位已从"补充"变为"核心"。

8. **推理成本优化成为系统工程**：Step-3 model-system co-design，NVIDIA Nemotron 3 Ultra 的 MoE 拓扑优化，DeepSeek-V3 的 FP8 训练 + 极低 GPU-hours，推理效率成为模型能否规模化的关键。

9. **安全/对齐框架系统化**：GPT-5.6/5.5 的 System Card 趋于全面红队报告，Claude Sonnet 5 误报率 -48%，Yi-Lightning RAISE 框架，安全已从"附加"变为"核心系统组件"。

10. **中国厂商在 MoE 和 Agent 方面领先**：DeepSeek (MoE 架构开创者), Qwen3 (Thinking 统一), Kimi K2 (Ultra-sparse MoE + MLA), GLM-5 (Agentic Engineering)，中国厂商在架构创新上不再跟随，而是定义方向。
