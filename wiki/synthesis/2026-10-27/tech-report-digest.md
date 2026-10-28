# LLM Tech Report Digest — 2026-10-27

> Daily digest of major AI company technical reports (Tech Report / Technical Report / System Card). Focus areas: new architectures (MoE, Mamba, hybrid), training methods (pre-training, post-training, alignment, RL), Scaling Law / 缩放分析, multimodal models, long-context models, reasoning models / reasoning model.

## 公司/组织覆盖

| 公司/组织 | 代表模型/系列 | 最新动态概览 |
|---|---|---|
| [DeepSeek](https://www.deepseek.com/) | DeepSeek-V3.2, DeepSeek-V3.2-Exp, DeepSeek-V4, DeepSeek-R1 | 持续推进 DeepSeek Sparse Attention（DSA）、百万级上下文、可扩展强化学习后训练；V4 混合注意力架构提升长上下文效率。 |
| [OpenAI](https://openai.com/) | GPT-6 系列、GPT-6 Sol/Luna、o3/o4-mini | 发布 GPT-6 Sol（2026-10-07）和 GPT-6 Luna 等，系统卡更新，关注 Preparedness Framework 评估（High：Cybersecurity/Bio/Chem）。 |
| [Meta AI (LLaMA)](https://ai.meta.com/) | Muse Wonder / Muse Wonder Full、LLaMA 5（传闻） | Muse Wonder 系列（2026-10-12）原生支持 text/image/video/audio 输入与 text 输出，1M 上下文，Model Card 于 2026-10-23 更新。 |
| [Google DeepMind (Gemini)](https://deepmind.google/) | Gemini 4 Argon、Gemini 3.8 Flash 等 | Gemini 4 Argon（2026-10-13）发布，统一 1M 上下文，在 Vals Index 等评估中领先，Model Card/PDF 已公开。 |
| [Anthropic (Claude)](https://www.anthropic.com/) | Claude Opus 5、Claude Opus 5.5 等 | Claude Opus 5.5（2026-09-22）等更新，系统卡持续发布，聚焦代理编程、安全评估。 |
| [Mistral AI](https://mistral.ai/) | Mistral Large 4（Le Chonk）、Magistral、Voxtral | Mistral Large 4（2026-10-06，公开预览）1T 总参数/49B 激活，granular MoE，多模态，混合推理，权重预计月底发布。 |
| [Qwen (Alibaba)](https://www.alibabacloud.com/zh/solutions/generative-ai/qwen) | Qwen3.8-Max、Qwen3.6 系列、Qwen3.5-Omni、Qwen-Image | Qwen3.8-Max（2026-08-03，2.4T MoE，1M 上下文，snapshot qwen3.8-max-0902），全模态与推理能力持续增强。 |
| [Moonshot AI (Kimi)](https://www.kimi.com/) | Kimi K3.1 Pro、Kimi K3、Kimi K2.5 | Kimi K3.1 Pro（2026-10-23，3T-class MoE，1M 上下文，后训练算力大幅提升）与高性能变体 K3.1 Pro Highspeed，计划 2026-11-04 开源权重。K3（2026-07-27，2.8T/104B 激活，Kimi Delta Attention + Attention Residuals）。 |
| [Zhipu AI (GLM/Z.ai)](https://www.zhipuai.com/) | GLM-5.3、GLM-5.3-Flash | GLM-5.3（2026-08-14，基于 GLM-5.2 后训练）着重复杂编程与长时代理；GLM-5.3-Flash（2026-08-26，320B/18B，原生多模态，推理成本大幅降低）。 |
| [StepFun](https://www.stepfun.com/) | Step-3、Step 3.7 Flash | Step-3（arXiv 2507.19427，模型-系统协同设计），Step 3.7 Flash（2026-05，198B/11B，原生多模态，代理/编码场景高效）。 |
| [Shanghai AI Lab (InternLM)](https://www.shlab.org.cn/) | Intern-S1-Pro、Intern-S2-397B | Intern-S2-397B（2026-09-13）397B-A17B 多模态 MoE，面向长周期科学研究与科学 Agent，Apache-2.0，vLLM 已支持。 |
| [ByteDance Seed (豆包)](https://seed.bytedance.com/) | Seed 2.0 系列 | Seed 2.0（arXiv 2607.00248，2026-06-30）Pro/Lite/Mini，omni-modal（video/image/audio/text），多模态理解与 Agent 能力增强。 |
| [xAI (Grok)](https://x.ai/) | Grok 4.5/4.6/4.7 | Grok 4.7（2026-09-21）等持续更新，实时信息、工具使用、多智能体能力；Grok 5 仍在训练（传闻）。 |
| [Amazon (Nova)](https://www.amazon.science/) | Amazon Nova 2 | Amazon Nova 2 技术报告（2025-12-02）公开，聚焦多模态能力与部署优化（更多详情待后续追踪）。 |
| [Microsoft (Phi/Nemotron 联动)](https://azure.microsoft.com/en-us/products/phi) | Phi-4-reasoning-vision-15B、Nemotron 3.5 Bolt 系列 | Phi-4-reasoning-vision-15B（2026-03）多模态推理；NVIDIA Nemotron 3.5 Bolt E4B 4GB（2026-10-23，基于 Gemma 4 E4B + Nemotron post-training），Bolt 74B-A9B 24GB（2026-10-15）等本地/边缘优化模型。 |
| [Apple](https://machinelearning.apple.com/) | Apple Foundation Models（AFM 2026） | AFM 2026（2026-06）第三代 Apple Foundation Models 家族（on-device + server），端侧优化与隐私优先，但缺乏官方完整技术报告 PDF 链接（需后续补齐）。 |
| [01.AI (Yi)](https://www.01.ai/) | Yi 系列（Yi-Lightning 等） | 近期无可验证的 2026 新技术报告/系统卡（主要以 API/产品更新为主，需进一步追踪）。 |
| [Baichuan AI](https://www.baichuan-ai.com/) | Baichuan-M3/M3 Plus/M4 | 聚焦医疗领域模型（M3 Plus 2026-01，M4 arXiv 2606.08982）等，通用大模型新报告暂未检索到明确 2026 主体技术报告。 |

## 重点报告详情

### DeepSeek
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| DeepSeek-V4-Pro/Flash | DeepSeek-V4：迈向高效百万 Token 上下文智能 | [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348) | DeepSeek-AI | 2026-04-26 | V4-Pro: 1.6T 总参数（49B 激活）；V4-Flash: 284B 总参数（13B 激活）；1M 上下文 | 混合注意力架构，长上下文推理 FLOPs 与 KV cache 大幅优化；面向长时任务与测试时扩展。 | [arXiv 2606.19348](https://arxiv.org/abs/2606.19348), [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) |
| DeepSeek-V4.1-Flash-1017 | DeepSeek-V4.1-Flash-1017（HF 发布） | [DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | DeepSeek-AI | 2026-10-17 | 552B MoE（原生视觉，非对称架构等相关信息见 HF/报告） | HF 上线时间 2026-10-17，配套技术报告 `DeepSeek_V41_Tech_Report.pdf`（社区已引用）。 | [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) |
| FlashMemory/DeepSeek-V4（稀疏注意力） | FlashMemory: ... Lookahead Sparse Attention | [FlashMemory: Supporting Large Memory Models with Self-Compacting Memories](https://arxiv.org/abs/2606.09079) | DeepSeek-AI | 2026-06-09 | 相关工作（Lookahead Sparse Attention） | 针对长上下文的稀疏注意力优化，提升长上下文推理效率。 | [arXiv 2606.09079](https://arxiv.org/abs/2606.09079) |

### OpenAI
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| GPT-6 Sol & Luna | GPT-6 October releases | [GPT-6 October](https://cdn.openai.com/pdf/gpt-6-october.pdf) | OpenAI | 2026-10-07（GPT-6 Sol & Luna） | 未公开（统一系统） | 10月发布的 GPT-6 Sol/Luna，系统卡包含 Preparedness Framework 评估，指出在 Cybersecurity、Bio/Chem 领域判定为 High。 | [PDF](https://cdn.openai.com/pdf/gpt-6-october.pdf) |
| GPT-6.1 Sol | GPT-6.1 Sol System Card | [oai_GPT_6_1_Sol.pdf](https://cdn.openai.com/pdf/38e3efcf-545e-44cd-99ec-2b7eb395f4cc/oai_GPT_6_1_Sol.pdf) | OpenAI | 2026-09-29 | 未公开 | 系统卡更新，延续统一路由与安全评估框架。 | [PDF](https://cdn.openai.com/pdf/38e3efcf-545e-44cd-99ec-2b7eb395f4cc/oai_GPT_6_1_Sol.pdf) |
| GPT-6 Astra | GPT-6 Astra System Card | [GPT-6 Astra](https://openai.com/index/gpt-6-astra/)（引用） | OpenAI | 2026-09-03 | 未公开 | 统一系统架构、强化学习大规模训练、工具使用与安全评估。 | [OpenAI Blog](https://openai.com/index/gpt-6-astra/) |

### Meta AI (LLaMA)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Muse Wonder / Muse Wonder Full | Muse Wonder Model Card | [Muse Wonder Model Card](https://research.meta.ai/static/muse-wonder-model-card) | Meta AI | 2026-10-12（发布）/2026-10-23（Model Card 更新） | 未公开（多模态） | 原生多模态输入（text/image/video/audio）、输出 text，1M 上下文窗口；面向统一多模态理解与生成场景。 | [Meta Research](https://research.meta.ai/static/muse-wonder-model-card) |

### Google DeepMind (Gemini)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Gemini 4 Argon | Gemini 4 Argon Model Card | [Gemini 4 Argon Model Card](https://deepmind.google/models/model-cards/gemini-4-argon) / [PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Argon-Model-Card.pdf) | Google DeepMind | 2026-10-13 | 未公开 | 统一 1M 上下文、思考模型、多模态与代理能力增强，在 Vals Index 等公开评估中表现领先。 | [Model Card](https://deepmind.google/models/model-cards/gemini-4-argon), [PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Argon-Model-Card.pdf) |

### Anthropic (Claude)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Claude Opus 5.5 | Claude Opus 5.5 | Anthropic 更新公告（相关页面） | Anthropic | 2026-09-22 | 未公开 | 代理编程、工具使用与推理能力增强，系统卡持续更新。 | [Anthropic](https://www.anthropic.com/) |

### Mistral AI
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Mistral Large 4（Le Chonk） | Introducing Mistral Large 4 | [Introducing Mistral Large 4](https://mistral.ai/news/mistral-large-4) | Mistral AI | 2026-10-06 | 1T 总参数（49B 激活），granular MoE，1.6B 视觉编码器，1M 上下文 | 开源权重预览（权重预计月底发布），混合推理（instruct+reasoning）统一、强推理与视觉 grounding、多语言支持。 | [Mistral Blog](https://mistral.ai/news/mistral-large-4), [Docs](https://docs.mistral.ai/models/mistral-large-4) |

### Qwen (Alibaba)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Qwen3.8-Max | Qwen3.8-Max | Alibaba Qwen 发布（社区/官方渠道） | Qwen Team, Alibaba Group | 2026-08-03 | 2.4T MoE，最大输入 991808（~1M），CoT 长度 262144，snapshot `qwen3.8-max-0902` | 大规模 MoE、超长上下文、混合思考模式，面向复杂推理与长任务场景。 | [Qwen Chat/Docs](https://chat.qwenlm.ai/)（引用信息） |

### Moonshot AI (Kimi)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Kimi K3.1 Pro / K3.1 Pro Highspeed | Kimi K3.1 Pro Tech Blog: Advancing Open Intelligence | [Kimi K3.1 Pro Tech Blog](https://www.kimi.ai/blog/kimi-k3-1-pro) | Moonshot AI | 2026-10-23 | 3T-class MoE（基于 Kimi K3，报道 2.8T 总参数/104B 激活），1M 上下文 | 基于 K3 大规模后训练，编码、3D 创作、金融研究与长时 Agent 能力大幅提升，高速变体 2-3x 吞吐，计划 2026-11-04 发布全量权重。 | [Kimi Blog](https://www.kimi.ai/blog/kimi-k3-1-pro), [Kimi Code Docs](https://www.kimi.com/code/docs/en/kimi-code/models.html) |
| Kimi K3 | Kimi K3 Technical Report | [Kimi K3 Technical Report](https://arxiv.org/abs/2607.24653) | Moonshot AI | 2026-07-27 | 2.8T 总参数（104B 激活），MoE，1M 上下文 | Kimi Delta Attention、Attention Residuals、原生视觉、DeepSWE 等 Agent 能力评估，开源权重已发布。 | [arXiv 2607.24653](https://arxiv.org/abs/2607.24653) |

### Zhipu AI (GLM)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| GLM-5.3 | GLM-5.3: Frontier Coding with Emergent Cyber Capabilities | [GLM-5.3 Blog](https://z.ai/blog/glm-5.3) | Zhipu AI (Z.ai) | 2026-08-14 | 753B 总参数（~40B 激活），MoE，DSA 架构（同 GLM-5.2 基座，纯后训练增强） | 复杂编程能力提升显著（Z.ai Code Bench +50%），长时 Agent 能力强化，思考强度可调。 | [Z.ai Blog](https://z.ai/blog/glm-5.3), [NVIDIA Build](https://build.nvidia.com/z-ai/glm-5-3) |
| GLM-5.3-Flash | GLM-5.3-Flash: Frontier Intelligence, Flash Cost | [GLM-5.3-Flash Blog](https://z.ai/blog/glm-5.3-flash) | Zhipu AI (Z.ai) | 2026-08-26 | 320B 总参数（18B 激活），原生多模态，混合稀疏+线性注意力，mHC 等优化 | 高性价比，接近旗舰编程/Agent 能力，中文开源社区广泛部署，推理成本大幅降低。 | [Z.ai Blog](https://z.ai/blog/glm-5.3-flash), [NGC](https://catalog.ngc.nvidia.com/orgs/nim/zai-org/models/glm-5.3-flash) |

### StepFun
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Step-3 | Step-3: A Large-Scale Mamba-Transformer Hybrid Architecture and Training Recipe | [Step-3 Technical Report](https://arxiv.org/abs/2507.19427) | StepFun | 2025-07-25（arXiv） | 321B 总参数（MoE，混合 Mamba-Transformer），长上下文 | 模型-系统协同设计，解码成本优化，长上下文与推理效率优化。 | [arXiv 2507.19427](https://arxiv.org/abs/2507.19427) |
| Step 3.7 Flash | Step 3.7 Flash | [Step 3.7 Flash](https://www.stepfun.com/step-3.7-flash) | StepFun | 2026-05-29 | 198B 总参数（11B 激活），Sparse MoE，原生多模态，256K 上下文 | 高效 Agent 能力，原生图像/视频理解，工具调用与 GUI 导向任务，推理强度可调（low/medium/high）。 | [StepFun](https://www.stepfun.com/step-3.7-flash), [GitHub](https://github.com/stepfun-ai/Step-3.7-Flash) |

### Shanghai AI Lab (InternLM)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Intern-S2-397B | Intern-S2-397B: Scientific Agentic Foundation Model | [Intern-S2-397B](https://arxiv.org/abs/2608.13505) | Shanghai AI Laboratory | 2026-09-13（正式发布） | 397B 总参数（17B 激活），Multimodal MoE，262K 上下文，MTP | 面向长周期科学研究与科学 Agent，生物/化学/材料等科学任务表现强，Apache-2.0 开源，vLLM day-0 支持。 | [HuggingFace](https://huggingface.co/internlm/Intern-S2-397B), [arXiv 2608.13505](https://arxiv.org/abs/2608.13505) |

### ByteDance Seed
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Seed 2.0 | Seed 2.0 Model Card | [Seed 2.0](https://github.com/ByteDance-Seed/Seed2.0/blob/master/Seed2.0%20Model%20Card.pdf) / [Blog](https://seed.bytedance.com/en/blog/seed-2-0-official-launch) | ByteDance Seed | 2026-06-30（arXiv）/2026-02-14（官宣） | 未公开（Pro/Lite/Mini 多尺寸） | Omni-modal（video/image/audio/text），实时交互、App 生成、音视频联合理解、Agent 编码与 GUI 能力增强。 | [GitHub](https://github.com/ByteDance-Seed/Seed2.0), [Model Card PDF](https://github.com/ByteDance-Seed/Seed2.0/blob/master/Seed2.0%20Model%20Card.pdf), [arXiv 2607.00248](https://arxiv.org/abs/2607.00248) |

### xAI (Grok)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Grok 4.7 | Grok 4.7 Model Card | [Model Card: Grok 4.7](https://media.x.ai/v1/website/4p7card-5eccc980.pdf) | xAI | 2026-09-21 | 未公开 | 推理、工具使用、实时信息整合、多智能体能力持续迭代。 | [xAI News](https://x.ai/news), [Model Card PDF](https://media.x.ai/v1/website/4p7card-5eccc980.pdf) |

### Amazon (Nova)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Amazon Nova 2 | Amazon Nova 2: Technical Report | [Amazon Nova 2 Technical Report](https://cdn.amazon.science/c5/3d/84514a224666b5be6de4b43ef4aa/nova-2-0-technical-report2.pdf) | Amazon AGI / AWS | 2025-12-02 | 未公开（多尺寸） | 多模态能力、推理与部署优化，详细技术报告已公开。 | [PDF](https://cdn.amazon.science/c5/3d/84514a224666b5be6de4b43ef4aa/nova-2-0-technical-report2.pdf) |

### Microsoft / NVIDIA
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Phi-4-reasoning-vision-15B | Phi-4-reasoning-vision-15B Technical Report | [Phi-4-reasoning-vision-15B Tech Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/Phi-4-reasoning-vision-15B-Tech-Report-1.pdf) | Microsoft Research | 2026-03-04 | 15B 参数（多模态推理） | 紧凑多模态推理，动态分辨率编码器，思考/非思考模式混合。 | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/) |
| Nemotron 3.5 Bolt E4B 4GB | Nemotron 3.5 Bolt E4B 4GB: An Open and Efficient Small Language Model for Fast Conversational Agents | [Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB-Technical-Report.pdf) | NVIDIA | 2026-10-23 | 8B 总参数（4B 有效），Gemma 4 E4B 基座 + Nemotron 后训练 | 面向本地对话 Agent，优化速度/智能/显存占比，支持 GGUF/NIM 等部署形态。 | [NVIDIA Nemotron](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB/), [HuggingFace](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB) |
| Nemotron 3.5 Bolt 74B-A9B 24GB | Nemotron 3.5 Bolt 74B-A9B 24GB: A Hybrid Vision-Language Model for Local AI | [Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-Technical-Report.pdf) | NVIDIA | 2026-10-15 | 74B 总参数（9B 激活），混合 Mamba-Transformer | 本地 Agent 场景，记忆/速度/智能平衡，支持多种量化格式。 | [NVIDIA Nemotron](https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Bolt-24GB/), [HuggingFace](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB) |

### Apple
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Apple Foundation Models (AFM 2026) | Third Generation of Apple’s Foundation Models | [Apple ML Research](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) | Apple | 2026-06-08 | AFM 3 Core（3B dense）、AFM 3 Core Advanced（20B MoE，1-4B 激活）等（5模型家族） | 隐私优先（Private Cloud Compute）、端侧优化、KV cache 共享、Parallel-Track MoE、Foundation Models 框架扩展支持第三方模型。 | [Apple ML Research](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models), [WWDC26](https://developer.apple.com/videos/play/wwdc2026/241/) |

## 技术趋势总结

| 研究方向 | 趋势观察 | 代表工作 |
|---|---|---|
| **新架构（MoE/Mamba/hybrid）** | 稀疏 MoE 持续主流，大规模 MoE（1T/2.4T/3T）常态化；混合注意力（hybrid attention）和稀疏注意力（DSA）用于长上下文效率；本地化场景也开始用混合架构提升显存效率。 | Mistral Large 4（1T MoE）、Qwen3.8-Max（2.4T MoE）、Kimi K3.1 Pro（3T-class）、DeepSeek-V4（混合注意力）、Nemotron 3.5 Bolt（Mamba-Transformer） |
| **训练方法（pre-training/post-training/RL/alignment）** | 后训练向大规模强化学习转移（纯 RL 驱动推理能力提升）、"post-training is all we did" 思路（GLM-5.3）、环境设计与 RL 算法优化成为提升核心，开源权重与预览同步加速。 | GLM-5.3（纯后训练提升）、DeepSeek-R1/V3.2（可扩展 RL）、Mistral Large 4（混合推理统一）、Seed 2.0（Agent/RL 能力增强） |
| **Scaling Law / 缩放分析** | 聚焦"效率缩放"（算力/参数激活/显存/推理成本），小模型高性能本地化（Phi/Nemotron Bolt），长上下文场景下的效率比成为竞争焦点。 | Nemotron 3.5 Bolt（每 GB 智能/速度）、Phi-4-reasoning-vision、DeepSeek-V4（百万上下文效率）、Kimi K3.1 Pro（后训练规模化） |
| **多模态模型** | 从理解向"原生全模态"演进（text/image/video/audio 统一输入），音视频联合理解、实时交互、GUI/VLM Agent 成为重点，图像/视频生成与理解一体化。 | Muse Wonder（原生多模态全输入）、Seed 2.0（omni-modal）、Qwen3.5-Omni、Gemini 4 Argon、GLM-5.3-Flash（原生多模态） |
| **长上下文模型** | 1M 上下文成为旗舰标配，重点转向长上下文效率（注意力优化、KV cache、稀疏注意力）与长时任务稳定性（goal drift 降低、agent 长时规划）。 | Kimi K3.1 Pro（1M）、DeepSeek-V4（1M 高效）、Mistral Large 4（1M）、Gemini 4 Argon（1M 统一上下文） |
| **推理模型 / reasoning model** | 混合推理（思考/非思考）普及，思考强度可调（low/high/max），工具使用与长时 Agent 深度整合，网络安全等高风险领域的评估（Preparedness Framework）日益重视。 | OpenAI GPT-6（Preparedness 高风险评估）、GLM-5.3（Agent 编程）、Mistral Large 4（混合推理）、Qwen3.8-Max（长 CoT）、Seed 2.0（Agent 能力） |

## 报告保存信息

- **保存路径**: `wiki/synthesis/2026-10-27/tech-report-digest.md`
- **更新时间**: 2026-10-27
- **涵盖范围**: 18+ 公司/组织的最新技术报告、系统卡、博客、模型卡（含预览/未完全公开参数模型）
- **重点领域**: 架构、训练方法、Scaling Law、多模态、长上下文、推理模型、Agent、安全评估
- **数据来源**: arXiv、官方博客、模型卡、HuggingFace、GitHub、NVIDIA/NIM、公司官网等公开渠道
- **备注**: 部分闭源模型参数未完全公开，上表参数多为厂商自报或社区推测；Apple AFM 2026、Yi/Baichuan 等仍缺乏完整主源技术报告，已在覆盖表中标注。

---

*注：本 digest 基于公开信息整理，参数与链接可能随版本更新变化，建议以官方最新发布为准。*
