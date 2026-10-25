# LLM Tech Report Digest — 2026-10-25

> Daily digest of major AI company technical reports (Tech Report / Technical Report / System Card). Focus areas: new architectures (MoE, Mamba, hybrid), training methods (pre-training, post-training, alignment, RL), Scaling Law / 缩放分析, multimodal models, long-context models, reasoning models / reasoning model.

## 公司/组织覆盖

| 公司/组织 | 代表模型/系列 | 最新动态概览 |
|---|---|---|
| [DeepSeek](https://www.deepseek.com/) | DeepSeek-V3.2, DeepSeek-V3.2-Exp, DeepSeek-V4 (preview), DeepSeek-R1 | 持续推进稀疏注意力（DeepSeek Sparse Attention, DSA）、百万级上下文、强化学习规模化后训练，在开源模型中保持领先的效率与推理能力。 |
| [OpenAI](https://openai.com/) | GPT-5/5.5/6 系列、o3/o4-mini、Deep Research、GPT-4.5 等 | 统一系统路由架构（fast+deep reasoning）、强化学习大规模训练、工具使用能力强化、系统卡（System Card）持续发布，重点关注安全与能力评估。 |
| [Meta AI (LLaMA)](https://ai.meta.com/) | LLaMA 4 (Scout/Maverick/Behemoth), LLaMA 3.x 系列 | 采用稀疏 MoE 架构（LLaMA 4），原生多模态支持、10M 上下文窗口（Scout）、参数高效微调（PEFT）研究活跃。 |
| [Google DeepMind (Gemini)](https://deepmind.google/) | Gemini 2.5、Gemini 3.1 Pro、Gemini 3.8 Flash 等 | 思考模型（thinking model）、超长上下文、多模态理解（视频等）、代理能力（agentic capabilities）、持续更新模型卡与技术报告。 |
| [Anthropic (Claude)](https://www.anthropic.com/) | Claude 3.7 Sonnet、Claude Sonnet/Haiku/Opus 系列（4.x/5.x） | 混合推理（hybrid reasoning）、代理编程（agentic coding）、安全透明度（Risk Reports/System Cards）、Red Teaming、工具使用与沙盒安全研究。 |
| [Mistral AI](https://mistral.ai/) | Magistral（推理系列）、Mistral Large 3、Mistral Small/Medium、Voxtral、OCR 等 | 强化学习驱动的推理模型（Magistral）、稀疏 MoE（Mistral Large 3，41B 激活/675B 总参数）、多模态与领域应用（物理 AI、OCR 等）。 |
| [Qwen (Alibaba)](https://www.alibabacloud.com/zh/solutions/generative-ai/qwen) | Qwen3、Qwen2.5-1M、Qwen2.5-Omni、Qwen3.5-Omni、Qwen-Image 等 | 全模态（omni）模型系列、超长上下文（1M/256K）、MoE 架构、图像生成（Qwen-Image）、多语言支持与开源力度大。 |
| [Microsoft (Phi)](https://azure.microsoft.com/en-us/products/phi) | Phi-4、Phi-4-reasoning、Phi-4-mini/multimodal、Phi-4-reasoning-vision 等 | 小模型高性能（小参数量达到大模型性能）、合成数据驱动训练、推理能力强化、多模态与视觉推理（15B 视觉推理模型）。 |
| [Apple](https://machinelearning.apple.com/) | Apple Foundation Models（on-device + server） | 隐私优先（on-device）、KV cache 共享、2-bit 量化感知训练、Parallel-Track MoE（PT-MoE）服务端模型、Foundation Models 框架开放给开发者。 |
| [xAI (Grok)](https://x.ai/) | Grok 4/4.20/4.6/4.7 系列 | 实时信息、强推理与工具使用、多智能体能力（multi-agent）、持续发布模型卡，计算规模大。 |
| [ByteDance (豆包/Doubao)](https://www.volcengine.com/product/doubao) | Doubao/Seed 系列（Seed 2.0、Seed-Thinking、Seed1.5-VL、Seedream 等） | 多模态基础模型、思考模型（Seed-Thinking）、图像生成（Seedream）、端到端语音（Realtime Voice）、大规模生产部署（日均万亿 token）。 |
| [Zhipu AI (GLM/ChatGLM)](https://www.zhipuai.com/) | GLM-5/5.3、GLM-5.3-Flash、GLM-TTS 等 | 从 "vibe coding" 到 "agentic engineering" 转型、工程化智能、国产算力适配、MoE 架构、语音合成等。 |

## 重点报告详情

### DeepSeek
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| DeepSeek-V3.2 | DeepSeek-V3.2：推动开源大模型前沿 | [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://arxiv.org/abs/2512.02556) | DeepSeek-AI | 2025-12-02 | 未公开完整参数表（基于 V3 架构演进） | DeepSeek Sparse Attention（DSA）高效长上下文；可扩展强化学习框架，后训练算力规模化；高算力变体 DeepSeek-V3.2-Speciale 达到顶级推理水平。 | [arXiv 2512.02556](https://arxiv.org/abs/2512.02556) |
| DeepSeek-V3.2-Exp | DeepSeek-V3.2-Exp：实验性模型（引入 DSA） | [Introducing DeepSeek-V3.2-Exp](https://deepseek.com/en/news/v3-2-exp) | DeepSeek-AI | 2025-09-29 | 同 V3.1 架构基础（671B/37B 活跃） | 首次实验性引入 DeepSeek Sparse Attention（DSA），长上下文训练/推理更高效，API 降价 50%+。 | [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp), [GitHub](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp), [Tech Report PDF](https://fe-static.deepseek.com/chat/transparency/deepseek-v3.2-model-card-0414-EN.pdf) |
| DeepSeek-V4 (preview) | DeepSeek-V4：迈向高效百万 Token 上下文智能 | [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348) | DeepSeek-AI | 2026-04-26 | DeepSeek-V4-Pro: 1.6T 总参数（49B 激活）；DeepSeek-V4-Flash: 284B 总参数（13B 激活）；上下文 1M tokens | 混合注意力架构（hybrid attention）；极高效长上下文（百万 token 场景下单 token 推理 FLOPs 降至 27%，KV cache 降至 10%）；面向长时任务与测试时扩展。 | [arXiv 2606.19348](https://arxiv.org/abs/2606.19348), [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) |
| DeepSeek-R1 | DeepSeek-R1：通过强化学习激励大模型推理能力 | [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) | DeepSeek-AI | 2025-01-22（v2 2026-01-04） | 基于 DeepSeek-V3 | 大规模纯 RL 激励推理（无大量冷启动监督）、开源推理模型系列，对后续推理模型研究影响深远，发表于 Nature。 | [arXiv 2501.12948](https://arxiv.org/abs/2501.12948) |
| DeepSeek-V3 | DeepSeek-V3 技术报告 | [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) | DeepSeek-AI | 2024-12-27（v2 2025-02-18） | 671B 总参数（37B 激活） | Multi-head Latent Attention（MLA）、DeepSeekMoE、无辅助损失负载均衡（auxiliary-loss-free）、多 token 预测（MTP）等高效训练/推理设计。 | [arXiv 2412.19437](https://arxiv.org/abs/2412.19437) |

### OpenAI
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| GPT-5 | GPT-5 系统卡 | [GPT-5 System Card](https://openai.com/research/gpt-5-system-card) / [arXiv:2601.03267](https://arxiv.org/abs/2601.03267) | OpenAI | 2025-08-07 | 未公开精确参数（统一系统） | 统一系统架构（fast model + deep reasoning model + 实时路由器）、根据对话类型/复杂度/工具需求动态路由、用量限制后使用 mini 版本、系统卡详细评估。 | [OpenAI](https://openai.com/index/o3-o4-mini-system-card), [arXiv 2601.03267](https://arxiv.org/abs/2601.03267) |
| GPT-5.5 / GPT-6 Astra | GPT-5.5 系统卡 / GPT-6 Astra 系统卡 | [GPT-5.5 System Card](https://press:@openai.com/index/gpt-5-5-system-card) / [GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra) | OpenAI | 2026-04-23（GPT-5.5）/ 2026-09-03（GPT-6 Astra） | 未公开 | 面向复杂真实任务（编码、研究、文档、工具使用）、更强的任务理解与工具协调、持续更新的安全评估（Preparedness Framework）。 | [OpenAI](https://openai.com/index/gpt-5-5-system-card), [Deployment Safety](https://deploymentsafety.openai.com/gpt-6-astra) |
| o3 / o4-mini | OpenAI o3 和 o4-mini 系统卡 | [OpenAI o3 and o4-mini System Card](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf) / [OpenAI](https://openai.com/index/o3-o4-mini-system-card) | OpenAI | 2025-04-16 | 未公开 | 推理模型结合全套工具能力（网页浏览、Python、图像/文件分析、图像生成、Canvas、自动化等）、大规模强化学习链式思考训练。 | [PDF](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf), [OpenAI](https://openai.com/index/o3-o4-mini-system-card) |
| Deep Research | Deep Research 系统卡 | [Deep Research System Card](https://openai.com/index/deep-research-system-card) / [PDF](https://cdn.openai.com/deep-research-system-card.pdf) | OpenAI | 2025-02-25 | 未公开 | 代理式多步网络研究、浏览与信息综合、强化学习训练浏览任务、针对提示注入等安全风险的评估与防护。 | [OpenAI](https://openai.com/index/deep-research-system-card), [PDF](https://cdn.openai.com/deep-research-system-card.pdf) |

### Meta AI (LLaMA)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| LLaMA 4 (Scout/Maverick) | LLaMA 4 系列：新一代原生多模态 AI 创新 | [The LLaMA 4 herd: The beginning of a new era of natively multimodal AI innovation](https://ai.meta.com/blog/llama-4-multimodal-intelligence) | Meta AI | 2025-04-05 | LLaMA 4 Scout: 17B 活跃参数（16 experts，109B 总参数）、上下文 10M tokens；LLaMA 4 Maverick: 17B 活跃参数（128 experts） | 原生多模态、稀疏 Mixture-of-Experts（MoE）、极长上下文（10M）、单 GPU 部署（Scout）、高性能多模态理解。 | [Meta Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence), [HuggingFace](https://huggingface.co/meta-llama) |
| LLaMA 3 系列 | LLaMA 3：迄今最强开源大模型 | [Introducing Meta LLaMA 3: The most capable openly available LLM to date](https://ai.meta.com/blog/meta-Llama-3) | Meta AI | 2024-04-18 | 多尺寸（8B/70B/405B 等） | 更大规模预训练、更强能力、负责任 AI 方法（LLaMA Guard 2、CyberSecEval 2）、广泛开源生态。 | [Meta Blog](https://ai.meta.com/blog/meta-Llama-3) |

### Google DeepMind (Gemini)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Gemini 2.5 | Gemini 2.5：推动前沿，先进推理、多模态、长上下文与下一代代理能力 | [Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities](https://arxiv.org/abs/2507.06261) | Google DeepMind | 2025-07-07（v6 2025-12-19） | 未公开（Pro/Flash/Lite 系列） | 思考模型（thinking model）、顶级编码与推理、视频理解（数小时视频）、长上下文、多模态、代理能力、持续更新技术报告。 | [arXiv 2507.06261](https://arxiv.org/abs/2507.06261), [PDF](https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf) |
| Gemini 3.1 Pro / 3.8 Flash | Gemini 3.1 Pro / 3.8 Flash 模型卡 | [Gemini 3.1 Pro - Model Card](https://deepmind.google/models/model-cards/gemini-3-1-pro) / [Gemini 3.8 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber) | Google DeepMind | 2026-02-19 / 2026-09-02 | 未公开 | 持续提升推理、代理、专业领域能力（金融、法律、工程等）、网络安全变体（Flash Cyber）、模型卡定期更新。 | [DeepMind Model Cards](https://deepmind.google/models/model-cards/), [Google Blog](https://blog.google/innovation-and-ai/) |

### Anthropic (Claude)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Claude 3.7 Sonnet | Claude 3.7 Sonnet 与 Claude Code | [Claude 3.7 Sonnet and Claude Code](https://www.anthropic.com/news/claude-3-7-sonnet) | Anthropic | 2025-02-24 | 未公开 | 首个混合推理模型（标准模式 + 扩展思考模式）、编程能力大幅提升、API 提供思考时长精细控制、与 Claude Code 深度结合。 | [Anthropic News](https://www.anthropic.com/news/claude-3-7-sonnet) |
| Claude 系列（近期） | Anthropic 透明度中心与风险报告 | [Anthropic’s Transparency Hub](https://www.anthropic.com/transparency) / [Risk Reports](https://www.anthropic.com/research) | Anthropic | 持续更新（2026年多次） | 未公开 | 系统卡、风险报告（包含自主性威胁、网络安全等）、安全评估、负责任扩展政策、Claude Code 安全与沙盒研究。 | [Anthropic](https://www.anthropic.com/) |

### Mistral AI
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Magistral | Magistral：Mistral 的首个推理模型与可扩展 RL 流水线 | [Magistral](https://arxiv.org/abs/2506.10910) | Mistral AI | 2025-06-12 | Magistral Small（开源，Apache 2.0）、Magistral Medium（基于 Mistral Medium 3） | 首个推理模型、仅用 RL（无大量冷启动）训练的可扩展 RL 流水线、中英双语推理、开源小模型 Magistral Small。 | [arXiv 2506.10910](https://arxiv.org/abs/2506.10910), [PDF](https://arxiv.org/pdf/2506.10910) |
| Mistral Large 3 | Mistral Large 3 | [Mistral Large 3](https://docs.mistral.ai/models/mistral-large-3-25-12) | Mistral AI | 2025-12-02 | 675B 总参数（41B 激活），MoE 架构，256K 上下文 | 开源权重（Apache 2.0）、多模态通用模型、大规模 MoE、生产部署 API 支持。 | [Mistral Docs](https://docs.mistral.ai/models/mistral-large-3-25-12) |

### Qwen (Alibaba)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Qwen3 | Qwen3 技术报告 | [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) | Qwen Team, Alibaba Group | 2025-05-14 | 系列模型（涵盖多尺寸），预训练 36T tokens | 混合思考模式（thinking/non-thinking）、119 语言/方言支持、性能效率并重、大规模预训练数据。 | [arXiv 2505.09388](https://arxiv.org/abs/2505.09388) |
| Qwen2.5-1M | Qwen2.5-1M 技术报告 | [Qwen2.5-1M Technical Report](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/Qwen2_5_1M_Technical_Report.pdf) | Qwen Team | 2025-01-26 | Qwen2.5-7B-Instruct-1M、Qwen2.5-14B-Instruct-1M，1M 上下文 | 上下文扩展至 1M tokens、长上下文训练与推理优化、开源长上下文模型。 | [PDF](http://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/Qwen2_5_1M_Technical_Report.pdf) |
| Qwen2.5-Omni / Qwen3.5-Omni | Qwen2.5-Omni / Qwen3.5-Omni 技术报告 | [Qwen2.5-Omni Technical Report](https://arxiv.org/abs/2503.20215) / [Qwen3.5-Omni Technical Report](https://arxiv.org/abs/2604.15804) | Qwen Team | 2025-03-26 / 2026-04-22 | Qwen3.5-Omni 扩展至数百 B 参数，256K 上下文 | 全模态端到端（文本、图像、音频、视频）、流式输入/输出、块级处理、百亿小时级音视频数据训练。 | [arXiv 2503.20215](https://arxiv.org/abs/2503.20215), [arXiv 2604.15804](https://arxiv.org/abs/2604.15804) |
| Qwen-Image | Qwen-Image 技术报告 | [Qwen-Image Technical Report](https://arxiv.org/abs/2508.02324) | Qwen Team | 2025-08-04 | 未公开 | 复杂文本渲染（中英尤其突出）、精确图像编辑、综合数据流水线、在多项文本渲染基准领先。 | [arXiv 2508.02324](https://arxiv.org/abs/2508.02324), [PDF](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/Qwen_Image.pdf) |

### Microsoft (Phi)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Phi-4 | Phi-4 技术报告 | [Phi-4 Technical Report](https://arxiv.org/abs/2412.08905) | Microsoft Research | 2024-12-12 | 14B 参数 | 小模型大能力、合成数据驱动、复杂推理（数学等）优化、训练配方创新。 | [arXiv 2412.08905](https://arxiv.org/abs/2412.08905) |
| Phi-4-reasoning / Phi-4-reasoning-plus | Phi-4-reasoning 技术报告 | [Phi-4-reasoning Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf) | Microsoft Research | 2025-04-30 | 14B（reasoning 变体） | 强化推理能力、长思考训练、与更大推理模型竞争的性能/规模比。 | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-15b-technical-report/) |
| Phi-4-mini / Phi-4-multimodal | Phi-4-Mini 技术报告 | [Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743) | Microsoft Research | 2025-03-03 | Phi-4-Mini 3.8B，Phi-4-Multimodal | 混合 LoRA（Mixture-of-LoRAs）架构、小尺寸多模态、128K 上下文、高质量合成数据。 | [arXiv 2503.01743](https://arxiv.org/abs/2503.01743) |
| Phi-4-reasoning-vision-15B | Phi-4-reasoning-vision-15B 技术报告 | [Phi-4-reasoning-vision-15B Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/Phi-4-reasoning-vision-15B-Tech-Report-1.pdf) | Microsoft Research | 2026-03-04 | 15B 参数（多模态推理） | 紧凑型多模态推理模型、高分辨率/动态分辨率编码器、推理与非推理模式混合、系统性消融研究。 | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/) |

### Apple
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Apple Foundation Models (2025) | Apple Intelligence 基础语言模型技术报告 2025 | [Apple Intelligence Foundation Language Models: Tech Report 2025](https://arxiv.org/abs/2507.13575) | Apple | 2025-07-17（v3 2025-08-27） | ~3B（端侧）、可扩展服务端模型 | 端侧优化（KV-cache 共享、2-bit 量化感知训练、全局-局部注意力）、Parallel-Track MoE（PT-MoE）服务端架构、隐私（Private Cloud Compute）、Foundation Models 框架开放。 | [arXiv 2507.13575](https://arxiv.org/abs/2507.13575), [Apple ML Research](https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025) |

### xAI (Grok)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Grok 4 / 4.20 / 4.6 / 4.7 | Grok 模型卡 | [Grok 4 Model Card](https://data.x.ai/2025-08-20-grok-4-model-card.pdf), [Grok 4.20 System Card](https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf), [Model Card: Grok 4.7](https://media.x.ai/v1/website/4p7card-5eccc980.pdf) | xAI | 2025-08-20 / 2026-04-07 / 2026-09-21 | 未公开 | 强推理与工具使用、实时信息整合、多智能体能力（Grok 4.20）、大规模算力训练、持续发布模型卡与安全评估。 | [xAI News](https://x.ai/news), [xAI Docs](https://docs.x.ai/) |

### ByteDance (豆包/Doubao)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Seed 系列（Seed 2.0、Seed-Thinking-v1.5） | ByteDance Seed 模型技术报告 | [Seed 2.0 Official Launch](https://seed.bytedance.com/en/blog/seed-2-0-official-launch), [Seed-Thinking-v1.5 Technical Details](https://seed.bytedance.com/en/blog/bytedance-s-latest-thinking-model-seed-thinking-v1-5-technical-details-disclosed) | ByteDance Seed | 2026-02-14 / 2025-04-14 | 未公开（多尺寸） | 思考模型（Seed-Thinking）、多模态（Seed1.5-VL）、图像生成（Seedream）、端到端语音（Realtime Voice）、大规模生产（日均超 30T tokens）、强化学习系统（DAPO 等）。 | [ByteDance Seed](https://seed.bytedance.com/en), [GitHub](https://github.com/ByteDance-Seed) |
| Seed1.5-VL | Seed1.5-VL 技术报告 | [Seed1.5-VL Technical Report](https://github.com/ByteDance-Seed/Seed1.5-VL/blob/main/Seed1.5-VL-Technical-Report.pdf) | ByteDance Seed | 2025-05-12 | 未公开 | 视觉语言基础模型、通用多模态理解与推理、60 项公开基准中 38 项 SOTA。 | [GitHub](https://github.com/ByteDance-Seed/Seed1.5-VL) |
| Doubao 文生图（Seedream 2.0） | Doubao 文生图技术报告 | [Doubao Text-to-Image Technical Report Released](https://seed.bytedance.com/en/blog/doubao-text-to-image-technical-report-released-full-disclosure-of-data-processing-pre-training-and-rlhf-workflow) | ByteDance Seed | 2025-03-12 | 未公开 | 原生中英双语理解、文本渲染、高美学、分辨率控制、数据处理/预训练/RLHF 全流程公开。 | [ByteDance Seed](https://seed.bytedance.com/en/blog/) |

### Zhipu AI (GLM/ChatGLM)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| GLM-5 / GLM-5.3 | GLM-5：从 Vibe Coding 到 Agentic Engineering | [GLM-5: From Vibe Coding to Agentic Engineering](https://z.ai/blog/glm-5) / [GLM-5 Technical Report](https://arxiv.org/abs/2602.15763) | Zhipu AI (Z.ai) | 2026-02-12 / 2026-08-26（GLM-5.3-Flash） | 未公开（GLM-5.3 报道 743B 参数，Flash 版本更小） | 面向复杂系统工程和长时代理任务、从 vibe coding 到 agentic engineering 范式转变、国产算力适配（华为昇腾等）、MoE 架构、编程/代理能力强化。 | [Z.ai Blog](https://z.ai/blog/glm-5), [arXiv 2602.15763](https://arxiv.org/abs/2602.15763), [HuggingFace](https://huggingface.co/zai-org) |
| GLM-TTS | GLM-TTS 技术报告 | [GLM-TTS Technical Report](https://arxiv.org/pdf/2512.14291) | Zhipu AI | 2025-12-15 | 未公开 | 端到端语音合成、Vocos2D 等架构改进、少量数据（100k 小时）下高质量合成、发音准确性与说话人相似度。 | [arXiv PDF](https://arxiv.org/pdf/2512.14291), [GitHub](https://github.com/zai-org/GLM-TTS) |

## 技术趋势总结

| 研究方向 | 趋势观察 | 代表工作 |
|---|---|---|
| **新架构（MoE/Mamba/hybrid）** | 稀疏 MoE 成为大模型主流（DeepSeek、Meta LLaMA 4、Mistral Large 3），混合注意力（hybrid attention）用于长上下文效率，DSA 等稀疏注意力降低推理成本。 | DeepSeek-V3.2（DSA）、DeepSeek-V4（混合注意力）、LLaMA 4（MoE）、Mistral Large 3（MoE） |
| **训练方法（pre-training/post-training/RL/alignment）** | 大规模预训练仍是基础（Qwen3 36T tokens），后训练向强化学习转移（DeepSeek-R1、Magistral、Seed-Thinking），无辅助损失负载均衡、多 token 预测等工程创新提升效率。 | DeepSeek-R1（纯 RL 推理）、Magistral（可扩展 RL 流水线）、DeepSeek-V3（aux-loss-free、MTP） |
| **Scaling Law / 缩放分析** | 关注长上下文缩放、效率缩放（算力/显存/推理成本）、"small model strong performance"（Phi 系列），以及实际部署约束下的最优规模。 | Phi 系列（小模型高性能）、DeepSeek-V4（长上下文效率分析） |
| **多模态模型** | 从单模态向全模态（omni）演进，端到端音视频理解与生成，图像生成能力大幅提升（复杂文本渲染），视频理解走向长视频。 | Qwen2.5/3.5-Omni、Gemini 2.5（视频理解）、Seed1.5-VL、Qwen-Image、Apple Foundation Models（多模态） |
| **长上下文模型** | 上下文长度快速增长（1M、256K、10M），重点转向长上下文下的效率（注意力机制优化、KV cache 管理）而非单纯扩展长度。 | DeepSeek-V4（1M 上下文高效）、Qwen2.5-1M（1M）、LLaMA 4 Scout（10M）、Qwen3.5-Omni（256K） |
| **推理模型 / reasoning model** | 推理成为核心能力，混合推理（思考/非思考模式）成为常态，测试时扩展（test-time scaling）、工具使用与代理能力深度整合，强化学习成为主导训练手段。 | OpenAI o3/GPT-5、DeepSeek-R1/V3.2、Claude 3.7、Magistral、Seed-Thinking、Qwen3（混合思考） |

## 报告保存信息

- **保存路径**: `wiki/synthesis/2026-10-25/tech-report-digest.md`
- **更新时间**: 2026-10-25
- **涵盖范围**: 14 个目标公司/组织的最新技术报告、系统卡、博客发布
- **重点领域**: 架构、训练方法、Scaling Law、多模态、长上下文、推理模型
- **数据来源**: arXiv、官方博客、模型卡、HuggingFace、GitHub 等公开渠道

---

*注：部分模型参数未公开（尤其是闭源商业模型），上表中的参数信息主要来源于技术报告或公开披露。报告会随新版本发布持续更新。*
