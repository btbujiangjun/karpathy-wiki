---
title: "LLM Tech Report Daily"
title-zh: "大模型技术报告日报"
type: synthesis
created: 2026-07-22
updated: 2026-07-22
sources: []
tags: [llm, tech-report, daily, moe, multimodal, reasoning, scaling, mamba, hybrid]
---

# 大模型技术报告日报 — 2026-07-22

> 自动整理：各大 AI 公司最新大模型技术报告概览
> 关注方向：新架构（MoE/Mamba/hybrid）、训练方法、Scaling Law、多模态、长上下文、推理模型
> 数据更新：2026-07-22
> 相较上期（07-21）主要更新：DeepSeek V4 技术报告发布（arXiv:2606.19348），Kimi K2.5 发布（arXiv:2602.02276），GLM-5.2 发布（1M 上下文 + IndexShare），Step 3.7 Flash 发布（198B MoE 400 TPS）

---

## 1. DeepSeek

| 项目 | 详情 |
|------|------|
| 组织 | DeepSeek |
| 模型 | DeepSeek-V4-Pro, DeepSeek-V4-Flash, DeepSeek-V3, DeepSeek-R1 |
| 日期 | V4: 2026-04-24; V3: 2024-12; R1: 2025-01 |
| 参数 | V4-Pro: 1.6T 总参 / 49B 激活; V4-Flash: 284B 总参 / 13B 激活; V3: 671B / 37B 激活 |
| 核心创新 | CSA + HCA 混合注意力架构 (压缩稀疏注意力 + 高度压缩注意力); Manifold-Constrained Hyper-Connections (mHC); Muon 优化器; 1M token 上下文; 32T+ tokens 预训练; FP4 + FP8 混合精度; V4-Pro-Max 推理增强模式 |
| 亮点 | V4-Pro 仅需 V3.2 的 27% 单 token FLOPs 和 10% KV cache 即可支持 1M 上下文; V4-Pro-Max 重新定义开源 SOTA; V4-Flash 284B/13B 激活实现极高效率; 开源 (MIT) |
| 链接 | [arXiv:2606.19348](https://arxiv.org/abs/2606.19348), [arXiv:2412.19437 (V3)](https://arxiv.org/abs/2412.19437), [arXiv:2501.12948 (R1)](https://arxiv.org/abs/2501.12948) |

**趋势关联**：DeepSeek V4 通过 CSA+HCA 混合注意力和 mHC 在长上下文效率上实现突破，1M 上下文成为标配。Muon 优化器成为多家公司共同选择。

---

## 2. OpenAI

| 项目 | 详情 |
|------|------|
| 组织 | OpenAI |
| 模型 | GPT-5.5, GPT-5.5 Pro, GPT-5.5 Ultra, GPT-5, o3, o4-mini |
| 日期 | GPT-5.5: 2026-04-23; GPT-5.5 Ultra: 2026-05-05; GPT-5.5 Pro: 2026-04-24; GPT-5: 2025-12 |
| 参数 | 未公开 |
| 核心创新 | GPT-5.5: "smartest and most intuitive" 模型; 增强 coding / computer use / deep research; GPT-5.5 Ultra: reasoning + coding 提升; GPT-5.5 Pro: 高级推理; o3: test-time compute 20K steps; GPT-5 System Card 安全评估框架 |
| 亮点 | GPT-5.5 为 Plus/Pro/Business/Enterprise 用户推出; o3 在 FrontierMath 达 0.1% 错误率; o3 Codeforces 99.5th percentile; ARC-AGI-1 87.5%; GPT-5.5 Ultra 提升 reasoning + coding; GPT-5 System Card 为首个详尽 frontier model 安全评估 |
| 链接 | [GPT-5.5 Blog](https://openai.com/index/introducing-gpt-5-5/), [arXiv:2601.03267 (GPT-5)](https://arxiv.org/abs/2601.03267), [GPT-5.5 System Card](https://deploymentsafety.openai.com/gpt-5-5/preparedness) |

**趋势关联**：OpenAI 以快速迭代（GPT-5→5.4→5.5 仅 4 个月）和安全评估为核心策略，o3/o4-mini 推理模型代表 test-time compute scaling 方向。

---

## 3. Meta AI

| 项目 | 详情 |
|------|------|
| 组织 | Meta (FAIR) |
| 模型 | Llama 4 Scout, Llama 4 Maverick, Llama 4 Behemoth (训练中) |
| 日期 | 2025-04 |
| 参数 | Scout: 109B / 17B 激活 (16 experts); Maverick: 400B / 17B 激活 (128 experts); Behemoth: ~2T / 288B 激活 (训练中) |
| 核心创新 | MoE 架构; 原生多模态 (早期融合, 文本+图像+视频+音频统一 tokenization); 超长上下文 (Scout 10M, Maverick 1M); iRoPE 位置编码; 在线知识蒸馏 (Behemoth→Scout/Maverick) |
| 亮点 | Scout 首个支持 10M 上下文的开源模型, NIAH 95%+; Maverick 128 专家 MoE; Behemoth (~2T) 目标最强开源模型; 训练稳定性关键挑战 (需 30 天连续训练) |
| 链接 | [llama.meta.com](https://llama.meta.com/) |

**趋势关联**：Meta 推动 MoE + 原生多模态 + 超长上下文，Llama 4 是首个支持 10M 上下文的开源模型。

---

## 4. Google DeepMind

| 项目 | 详情 |
|------|------|
| 组织 | Google DeepMind |
| 模型 | Gemini 3.1 Pro (新), Gemini 3 Pro, Gemini 3 Flash, Gemini 2.5 Pro/Flash |
| 日期 | Gemini 3.1 Pro: 2026-02-19; Gemini 3 Pro: 2025-11; Gemini 2.5: 2025-06 |
| 参数 | 未公开 |
| 核心创新 | 原生多模态 (文本/图像/音频/视频/代码); Thinking model 模式 (可调节思考预算 low/medium/high); Gemini 3.1 Pro: 核心推理大幅跃升; 原生工具调用; 长视频理解 (最高 3 小时) |
| 亮点 | Gemini 3.1 Pro: ARC-AGI-2 77.1% (3 Pro 仅 31.1%, 翻倍+); HLE 44.4% (无工具) / 51.4% (搜索+代码); GPQA-Diamond 94.3%; 超越 Claude Opus 4.6 和 GPT-5.2 Thinking; Gemini 3.1 Pro 现为 Google 最强模型; 3.5 Pro 即将发布 |
| 链接 | [Gemini 3.1 Pro Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/), [Model Card](https://deepmind.google/models/model-cards/gemini-3-1-pro/), [arXiv:2507.06261](https://arxiv.org/abs/2507.06261) |

**趋势关联**：Gemini 3.1 Pro 以 ARC-AGI-2 77.1% 刷新记录（3 Pro 仅 31.1%），推理能力呈指数级提升。Google 在多模态长上下文和推理能力上持续领先。

---

## 5. Anthropic

| 项目 | 详情 |
|------|------|
| 组织 | Anthropic |
| 模型 | Claude Mythos Preview (最强), Claude Opus 4.8, Claude Opus 4.7, Claude Fable 5 |
| 日期 | Opus 4.8: 2026-05-28; Opus 4/Sonnet 4: 2025-05; Mythos Preview: 2026 |
| 参数 | 未公开 |
| 核心创新 | 混合推理架构 (extended thinking + 工具调用交替); 动态工作流 (Dynamic Workflows: 数百并行子 agent); 努力控制 (Effort Control: low/medium/high/extra/max); ASL-3 安全等级; 诚实性提升 (4x 更少代码缺陷遗漏); Mythos Preview: Anthropic 最强模型 |
| 亮点 | Opus 4.8: 代码缺陷检测 4x 优于前代; Dynamic Workflows 支持代码库级迁移; 努力控制首次推出; Fast mode 2.5x 速度 3x 降价; Mythos Preview 超越所有 Opus 系列; System Card 详尽安全评估 (CB/autonomy/cyber) |
| 链接 | [Opus 4.8 Blog](https://www.anthropic.com/research/claude-opus-4-8), [System Card](https://www.anthropic.com/research/claude-opus-4-8-system-card) |

**趋势关联**：Anthropic 以 agentic 能力 (Dynamic Workflows) 和安全评估 (System Card) 为核心差异化。Mythos Preview 为当前最强闭源模型之一。

---

## 6. Mistral AI

| 项目 | 详情 |
|------|------|
| 组织 | Mistral AI |
| 模型 | Mistral Medium 3.5 (最新), Magistral Medium, Magistral Small, Large 3, Devstral Small |
| 日期 | Medium 3.5: 2026-04-29; Magistral Medium: 2025-06-10; Large 3: 2025-12 |
| 参数 | Medium 3.5: 128B dense; Large 3: 675B MoE / 41B 激活; Magistral Small: 24B |
| 核心创新 | Medium 3.5: 合并推理+编码+指令跟随 (三合一); 可配置推理努力; 256K 上下文; 原生视觉; Apache 2.0 开源; Magistral Medium: 纯 RL 训练推理模型 (无冷启动蒸馏); AIME'24 73.6% / majority@64 90.0% |
| 亮点 | Medium 3.5 取代 Devstral + Magistral + Medium 3.1, SWE-bench 77.6%; Magistral Medium: 纯 RL 训练 AIME'24 提升 50%; Magistral Small: Apache 2.0, 24B; Large 3: 675B MoE 开源; Mistral Saba 优化中东语言 |
| 链接 | [Magistral Paper](https://arxiv.org/abs/2506.10910), [Medium 3.5](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B) |

**趋势关联**：Mistral 以 "三合一" 合并模型 (推理+编码+指令) 简化产品线，纯 RL 训练推理模型 (Magistral Medium) 证明无需蒸馏即可获得强推理能力。

---

## 7. Qwen (阿里)

| 项目 | 详情 |
|------|------|
| 组织 | Alibaba (Qwen Team) |
| 模型 | Qwen3, Qwen3.5-ASR-Flash, Qwen3-VL |
| 日期 | 2025-05 |
| 参数 | 0.6B ~ 235B (含 dense 和 MoE 变体); Qwen3-235B-A22B: 235B 总参 / 22B 激活 |
| 核心创新 | Thinking / Non-thinking 模式切换; MoE 架构; 119 种语言; QAT 量化 (2/4/8-bit); QLoRA 微调; 原生多模态 (视觉、音频、视频); Agent 能力 (工具调用、MCP); Qwen3.5-ASR-Flash: 语音识别 |
| 亮点 | Qwen3-235B-A22B 在 AIME'25, MATH-500, LiveCodeBench 与 DeepSeek-R1, o3-mini 相当; Qwen3-30B-A3B 性能超越 Qwen2.5-32B 且推理快 10 倍 |
| 链接 | [arXiv:2505.09388](https://arxiv.org/abs/2505.09388), [GitHub](https://github.com/QwenLM/Qwen3) |

**趋势关联**：Qwen3 是国内开源生态最活跃的模型系列，MoE + 多模态 + Agent 全覆盖。

---

## 8. 01.AI (李开复)

| 项目 | 详情 |
|------|------|
| 组织 | 01.AI |
| 模型 | Yi-Lightning, Yi-Lightning-Vision |
| 日期 | 2024-12 |
| 参数 | 未公开 (MoE 架构) |
| 核心创新 | MoE 架构; 多模态 (视觉+文本); Chatbot Arena 排名世界第六; RAISE 安全框架; Yi-Lightning-Vision: 200K 上下文, 3D MR 安全 |
| 亮点 | Yi-Lightning 在 Chatbot Arena 达到 #6; Yi-Lightning-Vision 支持复杂图表分析、OCR、视频理解 |
| 链接 | [Yi-Lightning-Vision](https://platform.01.ai/blog?tag=18) |

**趋势关联**：01.AI 代表国内模型在竞技场上追赶前沿，MoE + 多模态 + 安全是核心策略。

---

## 9. Baichuan (百川)

| 项目 | 详情 |
|------|------|
| 组织 | Baichuan Inc. |
| 模型 | Baichuan-M4, Baichuan Omni-1.5 |
| 日期 | M4: 2026-06; Omni-1.5: 2025-01 |
| 参数 | Omni-1.5: 7B (基于 Qwen2.5-7B); Omni-1.5 训练数据 500B (文本+音频+视觉) |
| 核心创新 | 多模态原生融合 (文本+图像+视频+音频输入, 文本+音频输出); Baichuan-Audio-Tokenizer (语义+声学信息); 端到端音频生成; 医疗领域优化; 500B 高质量多模态数据; 4 阶段渐进训练 |
| 亮点 | M4 Medical Agent 幻觉率仅 3.3%; Omni-1.5 在 LiveBench 超越 Gemini 2.5 Pro; 7B 参数超越 GPT-4o-mini; 医疗图像理解 OpenMM-Medical 83.8% (超越 Qwen2-VL-72B 的 80.7%); 开源 (Apache 2.0) |
| 链接 | [arXiv:2606.12721](https://arxiv.org/abs/2606.12721), [arXiv:2501.15368 (Omni-1.5)](https://arxiv.org/abs/2501.15368) |

**趋势关联**：Baichuan Omni-1.5 以 7B 小参数量在医疗垂直领域和多模态融合上取得突破，证明小模型 + 专业数据可以在特定领域超越大模型。

---

## 10. Microsoft (Phi 系列)

| 项目 | 详情 |
|------|------|
| 组织 | Microsoft Research |
| 模型 | Phi-4 (14B), Phi-4-multimodal, Phi-4-reasoning, Phi-4-reasoning-vision-15B |
| 日期 | Phi-4: 2024-12; Phi-4-multimodal/reasoning: 2025-03 |
| 参数 | Phi-4: 14B (dense); Phi-4-reasoning-vision: 15B |
| 核心创新 | 小模型实现强推理; 多模态推理 (文本+图像); 开放权重; 基于 LLM 合成数据训练; 推理密集型任务专项优化; 1.5-bit / 2-bit / 4-bit 量化; 9.8T tokens 预训练 |
| 亮点 | Phi-4 (14B) 在推理和多模态任务上表现突出; 推理能力与更大模型相当; 设备端友好的量化方案 |
| 链接 | [arXiv:2412.08905 (Phi-4)](https://arxiv.org/abs/2412.08905), [arXiv:2603.16832](https://arxiv.org/abs/2603.16832) |

**趋势关联**：Phi 系列持续证明 "小模型 + 大数据 + 推理蒸馏" 路线的可行性。

---

## 11. Apple

| 项目 | 详情 |
|------|------|
| 组织 | Apple |
| 模型 | Apple Intelligence Foundation Language Models 2025 |
| 日期 | 2025-07 |
| 参数 | 约 3B (设备端); PT-MoE (服务端) |
| 核心创新 | 本地化推理 (设备端); 2-bit / 4-bit / 1.5-bit 量化 (PT-QAT); MoE (服务端); 混合精度训练 (2.15:1 等比例); 知识蒸馏 (大模型→小模型); Private Cloud Compute (PCC) |
| 亮点 | 设备端模型在 iPad Pro M4 上达 36 tok/s; 服务端模型 (PT-MoE) 在 LMSYS 排名 #5; PT-QAT 2-bit 量化实现高效设备端部署 |
| 链接 | [arXiv:2507.13575](https://arxiv.org/abs/2507.13575) |

**趋势关联**：Apple 强调隐私优先的本地推理，量化技术 + MoE 是其核心差异化。

---

## 12. NVIDIA

| 项目 | 详情 |
|------|------|
| 组织 | NVIDIA |
| 模型 | Nemotron 3 Ultra |
| 日期 | 2026-06 |
| 参数 | 550B 总参 (MoE hybrid Mamba-Attention); 55B 激活; 512 experts |
| 核心创新 | Mamba + Transformer hybrid 架构; 超长上下文 1M tokens; MoE 架构 (512 experts); 合成数据训练; 20T tokens 预训练 |
| 亮点 | 550B 参数, 55B 激活; hybrid Mamba-Attention 为长上下文提供线性复杂度; 专为工业部署优化 (制造、金融、医疗、零售) |
| 链接 | [arXiv:2512.17543](https://arxiv.org/abs/2512.17543) |

**趋势关联**：NVIDIA 强调 Mamba hybrid 架构和工业落地，hybrid Mamba-Attention 可能成为下一代长上下文主流。

---

## 13. xAI

| 项目 | 详情 |
|------|------|
| 组织 | xAI (Elon Musk) |
| 模型 | Grok 4, Grok 4 Heavy |
| 日期 | 2025-07-09 |
| 参数 | Grok 4: 未公开; Grok 4 Heavy: 多 agent 并行推理系统 |
| 核心创新 | 多 agent 并行推理 (Grok 4 Heavy: 多个 Grok 4 agent 并行工作, 比较后选最佳答案); 256K 上下文; 原生工具调用; 实时搜索 (X/网页/新闻); 256K context window; ARC-AGI V2 15.9%; HLE 50.7% (text-only) |
| 亮点 | Grok 4 Heavy: 首个 HLE 50%+ 模型; ARC-AGI V2 15.9% (近 2x Opus); Vending-Bench $4694 净资产 (人类 $844); SuperGrok Heavy $300/月; 未来路线图: 8月 coding model, 9月 multimodal agent, 10月 video gen |
| 链接 | [xAI Grok 4](https://x.ai/news/grok-4) |

**趋势关联**：xAI 通过多 agent 并行推理 (test-time compute) 和超算集群追求推理能力，Grok 4 Heavy 代表 "多 agent 即推理" 新范式。

---

## 14. Amazon (Nova)

| 项目 | 详情 |
|------|------|
| 组织 | Amazon Web Services (AWS) |
| 模型 | Amazon Nova (Micro, Lite, Pro, Canvas, Reel) |
| 日期 | 2024-12 |
| 参数 | 未公开 |
| 核心创新 | 多模态 (文本/图像/视频/音频输入); 文本/图像/视频生成; 原生嵌入; 知识蒸馏; 基于自研 Trainium 芯片训练; 超长上下文 300K; DPO/PPO 后训练 |
| 亮点 | Nova Pro 在图像理解/生成/视频理解任务上超越同级竞品; 使用知识蒸馏将大模型能力迁移至小模型; 基于 Trainium 芯片训练降低成本 |
| 链接 | [arXiv:2506.12103](https://arxiv.org/abs/2506.12103) |

**趋势关联**：Amazon 强调多模态全栈能力 (理解+生成) 和自研芯片生态。

---

## 15. Zhipu AI (智谱)

| 项目 | 详情 |
|------|------|
| 组织 | Zhipu AI (智谱 AI) |
| 模型 | GLM-5.2 (最新), GLM-5.1, GLM-5 |
| 日期 | GLM-5.2: 2026-06-16; GLM-5: 2026-02 |
| 参数 | 744B 总参 / 40B 激活 (MoE, DSA) |
| 核心创新 | Dynamic Sparse Attention (DSA); IndexShare (每 4 层共享 indexer, 1M 上下文 FLOPs 降低 2.9x); MTP + IndexShare + KV Share + Rejection Sampling (投机解码 accept length +20%); 异步 RL 训练框架 "Slime"; 异步 Agent RL; Anti-hacking 模块 (防 RL 训练中作弊); MIT 开源 |
| 亮点 | GLM-5.2: 首个真正可用的 1M 上下文开源模型; Terminal-Bench 2.1 81.0 (接近 Opus 4.8 的 85.0); FrontierSWE 74.4% (仅落后 Opus 4.8 1%); SWE-bench Pro 62.1; AIME 2026 99.2%; Artificial Analysis Intelligence Index 最强开源 (51 分); Effort Level 控制; 深度适配国产 GPU (华为昇腾/摩尔线程/海光/寒武纪/昆仑芯/沐曦/燧原) |
| 链接 | [GLM-5.2 Blog](https://z.ai/blog/glm-5.2), [arXiv:2602.15763](https://arxiv.org/abs/2602.15763), [IndexShare](https://arxiv.org/abs/2603.12201) |

**趋势关联**：GLM-5.2 以 IndexShare 架构创新解决 1M 上下文效率问题，异步 Agent RL 和 Anti-hacking 模块为训练方法创新。全面适配国产 GPU 生态。

---

## 16. InternLM (书生)

| 项目 | 详情 |
|------|------|
| 组织 | Shanghai AI Lab (上海 AI 实验室) |
| 模型 | Intern-S1-Pro, InternLM3-8B |
| 日期 | Intern-S1-Pro: 2026-03-26; InternLM3: 2025 |
| 参数 | Intern-S1-Pro: 1T 总参 (512 experts, 8 active, 22B 激活); InternLM3: 8B |
| 核心创新 | 万亿参数 MoE 科学多模态模型; 100+ 专业科学任务 (化学/材料/生命科学/地球科学); FoPE 位置编码; Agent 能力; 3-stage RL 训练; XTuner + LMDeploy 基础设施支持 |
| 亮点 | 首个万亿参数科学多模态基础模型; 在 AI4Science 领域领先; 强通用推理 + 专业科学深度融合; "Specializable Generalist" 定位 |
| 链接 | [arXiv:2603.25040](https://arxiv.org/abs/2603.25040), [HuggingFace](https://huggingface.co/internlm/Intern-S1-Pro) |

**趋势关联**：Intern-S1-Pro 代表 "科学 AI" 方向，万亿参数 + 100+ 专业任务的 "Specializable Generalist" 定位值得关注。

---

## 17. Moonshot AI (月之暗面)

| 项目 | 详情 |
|------|------|
| 组织 | Moonshot AI (月之暗面) |
| 模型 | Kimi K2.5 (新), Kimi K2, Kimi K2-Thinking |
| 日期 | K2.5: 2026-02-02; K2: 2025-07 |
| 参数 | K2.5: 1T 总参 / 32B 激活 (MoE, 384 experts, 8 selected + 1 shared); K2: 1.04T / 32B 激活 (128 experts) |
| 核心创新 | K2.5: Agent Swarm (自导向并行 agent 编排框架); 联合文本-视觉预训练 + 零视觉 SFT + 联合文本-视觉 RL; MoonViT-3D 视觉编码器; 3D ViT 压缩 (视频理解 4x 长度); PARL (Parallel-Agent RL); K2: MuonClip 优化器; MLA 注意力; 256K 上下文; INT4 量化 |
| 亮点 | K2.5 Agent Swarm: 延迟降低 4.5x (vs 单 agent); BrowseComp 78.4% (Agent Swarm); HLE 50.2% (w/ tools); AIME'25 96.1%; SWE-Bench Verified 76.8%; K2.5 开源 (MIT); 15T 混合视觉+文本 tokens 预训练; "joint text-vision enhancement" 双向增强 |
| 链接 | [arXiv:2602.02276 (K2.5)](https://arxiv.org/abs/2602.02276), [arXiv:2507.09816 (K2)](https://arxiv.org/abs/2507.09816) |

**趋势关联**：Kimi K2.5 引入 Agent Swarm (并行 agent 编排) 代表 Agent 范式从单 agent 向多 agent 协同演进。PARL 为多 agent RL 训练提供新范式。

---

## 18. StepFun (阶跃星辰)

| 项目 | 详情 |
|------|------|
| 组织 | StepFun (阶跃星辰) |
| 模型 | Step 3.7 Flash (新), Step 3.5 Flash, Step-DeepResearch, Step-3 |
| 日期 | Step 3.7 Flash: 2026-05-27; Step 3.5 Flash: 2026-02; Step-DeepResearch: 2025-12 |
| 参数 | Step 3.7 Flash: 198B MoE / 11B 激活 (196B 语言 + 1.8B 视觉); Step-3: 528B / 45B 激活; Step-DeepResearch: 32B |
| 核心创新 | Step 3.7 Flash: 400 TPS 高吞吐; 256K 上下文; 三级推理努力 (low/medium/high); 原生图像理解; NVFP4 量化 + MTP 投机解码; Step-DeepResearch: Checklist-style Judger reward; ADR-Bench (中文深度研究基准); 端到端 RL 训练 Agent |
| 亮点 | Step 3.7 Flash: 400 TPS, 专为 agentic workload 设计 (大规模报告解析/多步搜索/并行编码 agent); Step 3.5 Flash: ResearchRubrics 65.27 (接近 OpenAI/Gemini Deep Research); Step-DeepResearch: ResearchRubrics 61.42, 成本 <0.50 RMB (vs Gemini ~6.65 RMB); Step-3: 首个原生多模态推理模型 (开源) |
| 链接 | [Step 3.7 Flash](https://github.com/stepfun-ai/Step-3.7-Flash), [Step-DeepResearch Paper](https://arxiv.org/abs/2512.20491) |

**趋势关联**：StepFun 以高吞吐 (400 TPS) + 低成本 (Step-DeepResearch <0.50 RMB) 定位 agentic workload，证明 32B 模型可达到专家级深度研究能力。

---

## 19. ByteDance (字节跳动)

| 项目 | 详情 |
|------|------|
| 组织 | ByteDance (字节跳动) |
| 模型 | Doubao Seed 2.0 Pro, Seed 2.0 Lite/Mini/Code, Game-TARS |
| 日期 | 2026-02-14 |
| 参数 | Pro: 未公开; Game-TARS: 500B tokens 训练 |
| 核心创新 | 分层训练策略 (核心能力分层优化); 多模态原生融合; 高效 RL 训练; Agent 能力; 代码/数学专项优化; 256K 上下文; Game-TARS: 自主游戏推理 |
| 亮点 | Seed 2.0 系列覆盖全场景 (旗舰/轻量/端侧/代码); Game-TARS 500B tokens 训练超越 GPT-5; 字节跳动内部大规模部署验证 |
| 链接 | [arXiv:2602.16325](https://arxiv.org/abs/2602.16325) |

**趋势关联**：Seed 2.0 体现字节跳动在全场景模型布局上的策略，Game-TARS 代表游戏 AI 领域的突破。

---

## 综合趋势分析

### 1. 架构趋势：MoE 成为主流
所有 19 家公司中，**15+ 家采用或转向 MoE 架构**。代表性模型：
| 模型 | 总参 | 激活参 | 专家数 | 上下文 |
|------|------|--------|--------|--------|
| Kimi K2.5 | 1T | 32B | 384 | 256K |
| Grok 3 | 1.2T | - | 128 | 256K |
| Kimi K2 | 1.04T | 32B | 128 | 256K |
| DeepSeek-V4-Pro | 1.6T | 49B | - | 1M |
| Nemotron 3 Ultra | 550B | 55B | 512 | 1M |
| Mistral Large 3 | 675B | 41B | - | 128K |
| DeepSeek-V3 | 671B | 37B | 256 | 128K |
| GLM-5/5.2 | 744B | 40B | - | 200K→1M |

### 2. 推理能力：RL + Test-time Compute
推理模型成为 2025-2026 年最热门方向：
- **纯 RL 路线**：DeepSeek R1-Zero (无 SFT, 自发涌现 CoT), Mistral Magistral Medium (纯 RL 无冷启动, AIME'24 73.6%)
- **混合推理**：Anthropic Claude Opus 4.8 (extended thinking + tools, ASL-3), OpenAI o3 (test-time compute 20K steps)
- **多 agent 推理**：xAI Grok 4 Heavy (多 agent 并行, HLE 50.7%), Kimi K2.5 Agent Swarm (延迟降低 4.5x)
- **端到端 RL Agent**：Step-DeepResearch (BrowseComp 61.42, 成本 <0.50 RMB)
- **异步 RL**：智谱 GLM-5 "Slime" 框架 + 异步 Agent RL

### 3. 多模态：原生融合成为标配
几乎所有新模型都支持多模态：
- **原生多模态** (早期融合): Llama 4 (文本+图像+视频+音频), Gemini 3.1 Pro (3hr 视频), Kimi K2.5 (MoonViT-3D, 联合文本-视觉预训练), Qwen3 (119 语言), Baichuan Omni-1.5 (语音+视觉+语言)
- **后期融合**: GPT-5.5, Claude Opus 4.8
- **设备端多模态**: Apple AFM (3B), Phi-4-RV (15B)
- **视觉增强 agent**: Kimi K2.5 (Agent Swarm + 视觉), Step 3.7 Flash (原生图像理解)

### 4. 长上下文：从 128K 到 10M
- **10M tokens**: Llama 4 Scout (首个, NIAH 95%+)
- **1M tokens**: DeepSeek V4 (CSA+HCA, 27% FLOPs), Gemini 3.1 Pro, Nemotron 3 Ultra, GLM-5.2 (IndexShare 2.9x FLOPs 降低), Intern-S1-Pro, Claude Opus 4.8
- **256K**: Kimi K2.5, Step 3.7 Flash, GLM-5 (200K)
- **128K–200K**: Qwen3, Mistral Medium 3.5, ByteDance Seed 2.0

### 5. 小模型逆袭
- Microsoft Phi-4 (14B): 推理能力与大模型相当, 9.8T tokens 预训练
- InternLM3-8B: 4T tokens 训练达到 20B 模型性能
- Apple 设备端 3B 模型: 36 tok/s on iPad Pro, PT-QAT 2-bit 量化
- Baichuan Omni-1.5 (7B): 医疗图像理解超越 Qwen2-VL-72B
- Qwen3-30B-A3B: 超越 Qwen2.5-32B 且推理快 10 倍

### 6. Agent 化：从对话到自主执行
- **多 agent 并行**：xAI Grok 4 Heavy (多 agent 比较最佳答案), Kimi K2.5 Agent Swarm (PARL, 延迟降低 4.5x)
- **动态工作流**：Anthropic Claude Opus 4.8 Dynamic Workflows (数百并行子 agent)
- **端到端 Agent RL**：Step-DeepResearch (Checklist Judger reward), 智谱异步 Agent RL
- **垂直 Agent**：Baichuan-M4 (医疗 Agent, 幻觉率 3.3%), ByteDance Game-TARS (游戏 Agent)
- **高吞吐 Agent**：Step 3.7 Flash (400 TPS, 专为 agentic workload 设计)

### 7. 训练效率创新
- DeepSeek V4: CSA+HCA + Muon, 1M 上下文仅需 27% FLOPs (vs V3.2)
- GLM-5.2: IndexShare (每 4 层共享 indexer, 1M FLOPs 降低 2.9x)
- Kimi K2.5: 联合文本-视觉预训练避免模态冲突, 视觉 RL 增强文本性能
- Mistral Magistral Medium: 纯 RL 训练无需冷启动蒸馏
- Step-DeepResearch: 32B 模型达到专家级深度研究, 成本 <0.50 RMB
- Apple: 2-bit 量化 (PT-QAT) 实现设备端 36 tok/s
- DeepSeek V3: $5.58M 训练 671B 模型 (历史基线)

### 8. 安全与对齐
- Anthropic Claude Opus 4.8: ASL-3 安全等级, System Card 详尽披露 CB/autonomy/cyber 评估
- OpenAI GPT-5.5: GPT-5 System Card 为首个详尽 frontier model 安全评估文档
- Apple AFM: 本地化推理保障隐私 (Private Cloud Compute)
- 智谱 GLM-5.2: Anti-hacking 模块 (防 RL 训练中 GitHub 作弊)
- xAI Grok 4: SOC 2 Type 2, GDPR, CCPA 认证

### 9. 本期内重要更新 (vs 07-21)
- **DeepSeek V4 技术报告发布** (arXiv:2606.19348): CSA+HCA 混合注意力 + mHC + Muon, 1M 上下文效率突破
- **Kimi K2.5 发布** (arXiv:2602.02276): Agent Swarm 并行 agent 编排 + 联合文本-视觉 RL, BrowseComp 78.4%
- **GLM-5.2 发布**: IndexShare 架构 (1M FLOPs 降低 2.9x), MIT 开源, Terminal-Bench 81.0
- **Step 3.7 Flash 发布**: 198B MoE / 11B 激活, 400 TPS, 专为 agentic workload
- **GPT-5.5 Ultra 发布** (2026-05-05): reasoning + coding 提升
- **Mistral Medium 3.5 发布** (2026-04-29): 128B dense 三合一 (推理+编码+指令), SWE-bench 77.6%

---

> 本报告基于 2026-07-22 各公司公开技术报告、博客和论文整理。数据截至报告日期。
