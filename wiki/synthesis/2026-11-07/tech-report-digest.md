---
title: LLM Tech Report Digest — 2026-11-07
type: synthesis
created: 2026-11-07
updated: 2026-11-07
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, hybrid-attention, mamba, reasoning, long-context, multimodal, scaling-law, cybersecurity, open-weights, daily-digest]
---

# LLM Tech Report Digest — 2026-11-07

> Daily digest of major AI company technical reports (Tech Report / Technical Report / System Card). Focus areas: new architectures (MoE, Mamba, hybrid), training methods (pre-training, post-training, alignment, RL), Scaling Law / 缩放分析, multimodal models, long-context models, reasoning models / reasoning model.
>
> 本日窗口（截至 2026-11-07）检索重点：10 月中旬至 11 月初的新发布与更新，并回溯本月内仍为"最新旗舰"的报告。闭源模型的参数/数据量以厂商自报为准，社区推测已标注。

## 公司/组织覆盖

| 公司/组织 | 代表模型/系列 | 最新动态概览 |
|---|---|---|
| [DeepSeek](https://www.deepseek.com/) | DeepSeek-V4-Pro / V4-Flash、V4.1-Flash | V4（4 月）以 CSA+HCA 混合注意力把 1M 上下文做成"可负担"；V4.1-Flash（9/10）用因果编码器-解码器非对称架构，主打小 KV cache 与智能/成本比。 |
| [OpenAI](https://openai.com/) | GPT-6 Astra / Sol / Luna / Cyber、GPT-Rosalind-6 | 安全侧高频更新：GPT-6 Astra（9/3）首次达到 Preparedness 网络安全 Critical；GPT-6 Cyber（11/5）为网络攻防专用变体；ChatGPT Images 2.6（11/4）。 |
| [Meta AI](https://ai.meta.com/) | Muse Wonder / Muse Spark Open / Muse Glimmer 30B | 10 月密集发布：Muse Wonder（10/12，原生多模态 Agent 旗舰）、Muse Spark Open（10/15，816B-A42B 开放权重）、Muse Glimmer 30B（10/19，端侧 Agent）。 |
| [Google DeepMind](https://deepmind.google/) | Gemini 4 Argon、Gemini Omni 1.2 Flash | Gemini 4 Argon（10/13）为 Gemini 4 系列首款，1M 上下文、原生多模态；Gemini Omni 1.2 Flash 模型卡 11/5 更新。 |
| [Anthropic](https://www.anthropic.com/) | Claude Opus 5.5 / Sonnet 5.5 / Haiku 5.5、Fable 5.1 / Mythos 5.1 | 5.5 家族三代连发（9/22 Opus、9/28 Sonnet、10/7 Haiku）；Haiku 5.5 首次为小模型加入窄域网络安全防护。 |
| [Mistral AI](https://mistral.ai/) | Mistral Large 4（Le Chonk）、Timestral | ML4（10/6 预览、10/29 开源权重）1T/52B 激活，MLA+DSA 稀疏注意力；Timestral（10/27）时间序列基础模型族。 |
| [Qwen (Alibaba)](https://qwen.ai/) | Qwen3.8-Max、Qwen3.8-Flash-Next、Qwen4（训练中） | Qwen3.8-Max（8/3）2.4T MoE；Qwen3.8-Flash-Next（8/26）为 Qwen4 架构预览；Qwen4 截至 11/6 未正式发布，仅官方预告"next week"与"The becoming begins"。 |
| [Moonshot AI (Kimi)](https://www.kimi.com/) | Kimi K3.1 Pro / Highspeed | K3.1 Pro（10/23）2.8T/104B 激活，为 K3 的大规模后训练版；权重 11/4–11/5 已上传 Hugging Face（MXFP4）。 |
| [Zhipu AI (Z.ai)](https://z.ai/) | GLM-5.3 / GLM-5.3-Flash、GLM-Omni（研究） | 8 月发布 5.3/5.3-Flash；10 月 GLM-Omni 论文探索视觉生成反哺语言推理；GLM-5.4/5.5 处于研发/后训练阶段，尚未发布。 |
| [StepFun](https://www.stepfun.com/) | Step 5 Preview | 9/20 API 预览、10/15 开放权重 + 技术博客：600B/27B 激活、92 层"窄而深"、Sparse GQA、1M 上下文。 |
| [Shanghai AI Lab (InternLM)](https://www.shlab.org.cn/) | Intern-S2-Preview-397B、Intern-S2-Mobius | Intern-S2-Preview（arXiv 8/14，9/13 发布）科学 Agent 基础模型；Intern-S2-Mobius（8 月）解耦知识存储与组合推理的新架构。 |
| [ByteDance Seed (豆包)](https://seed.bytedance.com/) | Seed 2.0、doubao-seed-evolving | Seed 2.0 模型卡（6/19）仍为最新完整模型文档；11 月更新 doubao-seed-evolving（Agent 规划与抗幻觉）；Recycler（9/28）隐状态复用研究。 |
| [xAI (Grok)](https://x.ai/) | Grok 4.7 | Grok 4.7（9/21）500K 上下文，增强长任务 RL 与自我校验；Grok 4.8 已被 Musk 提及但截至 11/4 未发布。 |
| [Amazon (Nova)](https://www.amazon.science/) | Amazon Nova 2 | Nova 2 技术报告（2025-12-02）含 Lite/Pro/Omni/Sonic 四款，1M 上下文；Nova 2 Lite 安全评估论文（2026-01-27）。 |
| [Microsoft (Phi)](https://azure.microsoft.com/en-us/products/phi) | Phi-4-reasoning-vision-15B、Phi-Ground-Any-4B | 最新通用 Phi 仍为 Phi-4-reasoning-vision-15B（2026-03-04）；截至 2026 年 8 月无 Phi-5。 |
| [Apple](https://machinelearning.apple.com/) | Apple Foundation Models（AFM 3） | 第三代 AFM（6/8）五模型家族，与 Google 合作；AFM 3 Cloud 于 9/14 正式上线。 |
| [NVIDIA](https://research.nvidia.com/labs/nemotron/) | Nemotron 3.5 Super / Lightning / Bolt / Transcribe | 10 月集中发布：Super/Lightning 混合 Mamba-Transformer MoE、Bolt 74B-A9B 24GB、Bolt E4B 4GB、Transcribe 30B-A4B。 |
| [01.AI (Yi)](https://www.01.ai/) | Yi 系列 | 2026 年未见可验证的新主源技术报告/系统卡，主要为产品/API 更新（需后续追踪）。 |
| [Baichuan](https://www.baichuan-ai.com/) | Baichuan 2 / 医疗 M 系列 | 通用大模型最新可验证技术报告仍为 Baichuan 2（2023）；2026 年以医疗垂类模型为主。 |

## 重点报告详情

### DeepSeek
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| DeepSeek-V4-Pro / V4-Flash | DeepSeek-V4：迈向高效百万 Token 上下文智能 | [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348) | DeepSeek-AI | 2026-04-24（预览）/2026-04-26（arXiv） | Pro：1.6T 总参数 / 49B 激活；Flash：284B / 13B；1M 上下文；预训练 >32T tokens | **混合注意力 CSA+HCA**：CSA 沿序列压缩 KV 再叠加 DSA top-k 稀疏选择，HCA 做 128× 极端压缩后稠密注意力；**mHC** 流形约束超连接稳定深层信号；**Muon** 优化器；后训练为"领域专家独立培养 + on-policy distillation 统一整合"。1M 上下文下 Pro 单 token 推理 FLOPs 仅为 V3.2 的 **27%**、KV cache 为 **10%**。 | [arXiv](https://arxiv.org/abs/2606.19348), [DeepSeek News](https://www.deepseek.com/en/news/v4-preview/), [HF](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) |
| DeepSeek-V4.1-Flash | DeepSeek-V4.1-Flash：更聪明、更快、更高效 | [Introducing DeepSeek-V4.1-Flash](https://www.deepseek.com/en/news/deepseek-v4-1-flash/) | DeepSeek-AI | 2026-09-10 | 552B MoE；**8B 输入 / 16B 输出激活**；原生视觉；KV cache HBM 降至 1/4、SSD 存储 1/8 | **因果编码器-解码器非对称架构**；新预训练方法 + 更大规模 RL 后训练，多项基准超过 V4-Pro；以缓存压缩降低 Agent 长上下文成本；逐步替代 V4-Pro。 | [DeepSeek News](https://www.deepseek.com/en/news/deepseek-v4-1-flash/) |

### OpenAI
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| GPT-6 Astra | GPT-6 Astra 系统卡 | [GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra) | OpenAI | 2026-09-03 | 未公开 | 首个达到 Preparedness **网络安全 Critical** 的模型；大规模 RL、工具使用与长轨迹鲁棒性；新型对齐训练与 misalignment monitoring；揭示 monitorability 下降、sandbagging 风险。 | [System Card](https://deploymentsafety.openai.com/gpt-6-astra) |
| GPT-6 Cyber | GPT-6 Cyber 系统卡 | [GPT-6 Cyber System Card](https://deploymentsafety.openai.com/gpt-6-cyber) | OpenAI | 2026-11-05 | 基于 GPT-6 Astra 的专用后训练变体 | 面向授权安全工作的网络攻防专用变体（漏洞发现、exploit、渗透测试）；同一 Preparedness 评定：Cyber **Critical**、Bio/Chem High、AI Self-Improvement 低于 High；Daybreak Red 受限访问 + 身份验证/SSO/MFA/IP allowlist。 | [System Card](https://deploymentsafety.openai.com/gpt-6-cyber) |
| GPT-6 Sol / Luna（10 月版） | GPT-6 Sol 与 GPT-6 Luna：2026 年 10 月更新 | [GPT-6 Sol and GPT-6 Luna: October 2026 update](https://deploymentsafety.openai.com/gpt-6-october) | OpenAI | 2026-10-07 | 未公开（统一系统） | 全量替代 GPT-5.6 Sol/Luna；更强多轮 jailbreak 抵抗、降低不诚实/规避；Preparedness：Cyber 与 Bio/Chem 均为 High；10/29 Luna 补充卡将回复更简洁、减少过度附和，instruction hierarchy 鲁棒性 **99.91%**。 | [System Card](https://deploymentsafety.openai.com/gpt-6-october), [Luna 10/29 Addendum](https://deploymentsafety.openai.com/gpt-6-luna-october-28-2026-addendum) |
| GPT-6.1 Sol | GPT-6.1 Sol 系统卡增补 | [Addendum to GPT-6 Astra System Card: GPT-6.1 Sol](https://deploymentsafety.openai.com/) | OpenAI | 2026-09-29 | 未公开 | 延续统一路由与安全评估框架的系统卡增补。 | [Deployment Safety Hub](https://deploymentsafety.openai.com/) |
| GPT-6.1 Terra | GPT-6 Astra 系统卡增补：GPT-6.1 Terra | [Addendum: GPT-6.1 Terra](https://deploymentsafety.openai.com/) | OpenAI | 2026-10-26 | 未公开 | 同一 Astra 基座的迭代版本，安全评估增补。 | [Deployment Safety Hub](https://deploymentsafety.openai.com/) |
| GPT-Rosalind-6 | GPT-Rosalind-6 系统卡增补 | [GPT-Rosalind-6 System Card Addendum](https://deploymentsafety.openai.com/gpt-rosalind-6) | OpenAI | 2026-10-30 | 与 GPT-6 Astra 同权重，生物/药物发现/转化医学专用后训练 | 面向合格科研人员的生物前沿推理模型；双用途生物查询拒绝更少但仅经信任访问；Preparedness：Bio/Chem High（未达 Critical）、Cyber Critical。 | [System Card](https://deploymentsafety.openai.com/gpt-rosalind-6) |
| ChatGPT Images 2.6 | ChatGPT Images 2.6 系统卡 | [ChatGPT Images 2.6 System Card](https://deploymentsafety.openai.com/) | OpenAI | 2026-11-04 | 未公开 | 图像生成模型能力、安全评估、防护与图像溯源。 | [Deployment Safety Hub](https://deploymentsafety.openai.com/) |

### Meta AI
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Muse Wonder / Muse Wonder Full | Muse Wonder：面向个人与专业 AI Agent 的前沿模型 | [Muse Wonder: A Frontier Model For Personal & Professional AI Agents](https://research.meta.ai/blog/muse-wonder) | Meta AI | 2026-10-12 | 未公开；输入 text/image/video/audio，输出 text；1M 上下文 | **Active Memory + Active Focus** 长时目标追踪与恢复；在个人/专业 Agent、记忆、编码基准上 SOTA；gw 级 Prometheus 数据中心训练。 | [Blog](https://research.meta.ai/blog/muse-wonder), [Model Card](https://research.meta.ai/static/muse-wonder-model-card) |
| Muse Spark Open | Muse Spark Open：迄今最强美国开放权重模型 | [Introducing Muse Spark Open](https://research.meta.ai/blog/muse-spark-open) | Meta Superintelligence Labs | 2026-10-15 | 816B 总参数 / 42B 激活；MoE 每层 256 experts、top-8；62 层；原生多模态输入；1M 上下文；BF16/NVFP4 | 面向 Agentic coding；专家占约 97% 参数；Helion GPU kernels；可在双 Apple M5 Ultra Mac Studio 本地运行；开放权重。 | [Blog](https://research.meta.ai/blog/muse-spark-open), [HF Blog](https://huggingface.co/blog/meta-muse-spark-open) |
| Muse Glimmer 30B | Muse Glimmer 30B：端侧 Agent 模型 | [Muse Glimmer 30B: An On-Device Agentic Model](https://ai.meta.com/research/publications/muse-glimmer-30b-an-on-device-agentic-model/) | Meta AI | 2026-10-19 | 30B 参数（约 4-bit 量化，单 GPU）；text/image 输入 | 多步推理、可靠工具调用与失败恢复；Apache 2.0；对标 Gemma4-31B / Qwen3.6-27B。 | [Meta Research](https://ai.meta.com/research/publications/muse-glimmer-30b-an-on-device-agentic-model/) |
| 专用化模型（Muse & Meta AI） | 为 Muse 与 Meta AI 带来专用模型 | [Bringing Specialized Models to Muse and Meta AI](https://research.meta.ai/blog/specialized-models-for-muse-and-metaai) | Meta Superintelligence Labs | 2026-11-06 | 基于 Muse Wonder 训练 | Active Memory 使关键信息遗忘减少 **2.4×**；Active Focus 在意外阻碍场景任务完成率提升 **67%**。 | [Blog](https://research.meta.ai/blog/specialized-models-for-muse-and-metaai) |

### Google DeepMind
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Gemini 4 Argon | Gemini 4 Argon 模型卡 | [Gemini 4 Argon Model Card](https://deepmind.google/models/model-cards/gemini-4-argon/) | Google DeepMind | 2026-10-13 | 大规模稀疏 MoE Transformer；原生 text/vision/audio 输入；1M 输入+输出上下文；知识截止 2026-03 | Gemini 4 系列首款；agentic coding、知识工作、科学/数学、长上下文与网络安全全面增强；Vals Index **68.9%**、Harvey Legal Agent **19.6%**、GraphWalks 256k–1M BFS F1 **84.2%**；配套 Safety & Security Report 指出 Cyber/CBRN/Stealth 接近 CCL。 | [Model Card](https://deepmind.google/models/model-cards/gemini-4-argon/), [Safety Report PDF](https://www.datocms-assets.com/142357/1792511849-gemini_4_safety_report.pdf), [Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/) |
| Gemini Omni 1.2 Flash | Gemini Omni 1.2 Flash 模型卡 | [Gemini Omni 1.2 Flash](https://deepmind.google/models/model-cards/) | Google DeepMind | 2026-11-05（模型卡更新） | 未公开 | 统一多模态（Omni）快模型系列更新，面向低延迟多模态交互。 | [Model Cards](https://deepmind.google/models/model-cards/) |

### Anthropic
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Claude Opus 5.5 | 推出 Claude Opus 5.5 | [Introducing Claude Opus 5.5](https://www.anthropic.com/news/models) | Anthropic | 2026-09-22 | 未公开；**1M 上下文默认**、128K 最大输出；always-on adaptive thinking | 长时 agentic coding 与知识工作领先；相比 Opus 5 运行成本降低约 40%；`$4/$20` per MTok。 | [News](https://www.anthropic.com/news/models), [System Cards](https://www.anthropic.com/system-cards) |
| Claude Sonnet 5.5 | 推出 Claude Sonnet 5.5 | [Introducing Claude Sonnet 5.5](https://www.anthropic.com/news/models) | Anthropic | 2026-09-28 | 未公开 | 比 Sonnet 5 快 30%+、多数工作成本低 30%。 | [News](https://www.anthropic.com/news/models) |
| Claude Haiku 5.5 | Claude Haiku 5.5 系统卡 | [Claude Haiku 5.5 System Card](https://www-cdn.anthropic.com/e1080d6bf5ae2018ea3c2f414064be03232f5be5/Claude%20Haiku%205.5%20System%20Card.pdf) | Anthropic | 2026-10-07 | 未公开；1M 上下文、128K 输出；adaptive thinking + effort 参数；知识截止 2026-06 | 高吞吐小模型；多项能力接近 Sonnet 5.5；未越过新 RSP 阈值；首个内置窄域高风险网络安全防护的 Haiku；价格较 Haiku 4.5 低 75%。 | [System Card PDF](https://www-cdn.anthropic.com/e1080d6bf5ae2018ea3c2f414064be03232f5be5/Claude%20Haiku%205.5%20System%20Card.pdf) |
| Claude Fable 5.1 / Mythos 5.1 | 推出 Claude Fable 5.1 与 Mythos 5.1 | [Claude Fable 5.1 and Mythos 5.1 System Card](https://www.anthropic.com/system-cards) | Anthropic | 2026-09-01 | 未公开 | 长时 agentic coding、知识工作与研究；文本水印与 C2PA 内容凭证。 | [System Cards](https://www.anthropic.com/system-cards) |

### Mistral AI
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Mistral Large 4（Le Chonk） | 推出 Mistral Large 4 | [Introducing Mistral Large 4](https://mistral.ai/news/mistral-large-4/) | Mistral AI | 2026-10-06（预览）/2026-10-29（开源权重） | 约 1T 总参数 / 49–52B 激活；72 层；MLA + DSA top-2048；128 routed experts top-4 + 1 shared；3:1 RoPE/NoPE；1.6B Pixtral 视觉编码器；1M 上下文 | 原生多模态 MoE；**agent-authored 可验证环境** + 大规模 RL 后训练；多教师蒸馏提供 high/medium/low 推理档；NVFP4 量化至 606 GB、可部署于 4×GB300；开源权重（Mistral Ecosystem Open-Weight License）。 | [Blog](https://mistral.ai/news/mistral-large-4/), [OSS 权重](https://mistral.ai/news/mistral-large-4-oss/), [HF Blog](https://huggingface.co/blog/mistral-large4), [技术报告](https://www.alphaxiv.org/abs/2611.mistral-large-4.pdf) |
| Timestral | Timestral：概率时间序列基础模型族 | [Timestral](https://arxiv.org/pdf/2610.37585) | Mistral AI | 2026-10-27 | 5M / 28M / 123M / 209M 四尺寸 | **Decoupled Horizon Forecasting (DHF)** 解耦预测 token 与因果上下文；原生 known-future covariates；合成预训练 + 真实/合成后训练；GIFT-Eval/TIME/fev-bench SOTA。 | [arXiv 2610.37585](https://arxiv.org/pdf/2610.37585) |

### Qwen (Alibaba)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Qwen3.8-Max | Qwen3.8-Max：编码与协作新标杆 | [Qwen3.8-Max: A New Bar for Coding and Cowork](https://qwen.ai/research/) | Qwen Team, Alibaba | 2026-08-03 | 2.4T 总参数（MoE，A95B 激活）；约 1M 上下文；开源权重 `Qwen3.8-2.4T-A95B` | 首个开源权重 Qwen-Max 级模型；编码、工作协作、长 CoT 全面增强；基于 Qwen3.5 架构扩展。 | [Qwen Research](https://qwen.ai/research/) |
| Qwen3.8-Flash-Next | Qwen3.8-Flash-Next：新架构，迈向极致成本效率 | [Qwen3.8-Flash-Next: A New Architecture, Towards Ultimate Cost-Efficiency](https://qwen.ai/research/) | Qwen Team, Alibaba | 2026-08-26 | 125B 总参数 / 6B 激活（另 51B n-gram embedding、4B MTP）；262K→1M 上下文；`qwen4_exp` 架构 | **Gated DeltaNet + Gated Attention 混合**；作为 Qwen4 架构的早期预览（类比 Qwen3-Next 之于 Qwen3.5）；qwen-community-1.0 许可。 | [Qwen Research](https://qwen.ai/research/) |
| Qwen4（未发布） | Qwen4 系列（训练中） | [Qwen4 roadmap](https://chinaaicompass.com/events/916-alibaba-unveils-qwen4-qwen5-roadmap-and-new-image-audio-musi) | Alibaba Qwen | 截至 2026-11-06 未发布 | 官方仅称"training"；路线图 Qwen4.5/5 目标 5–10T 参数 | 官方 9/22 Apsara 大会称 Qwen4 训练中；舞台幻灯片出现 Max/Plus/Flash/27B 四档；11/6 官方账号" The becoming begins"为预告，非发布。 | [Qwen Research](https://qwen.ai/research/) |

### Moonshot AI (Kimi)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Kimi K3.1 Pro / Highspeed | Kimi K3.1 Pro 技术博客：推进开放智能 | [Kimi K3.1 Pro Tech Blog: Advancing Open Intelligence](https://www.kimi.ai/blog/kimi-k3-1-pro) | Moonshot AI | 2026-10-23（发布）/2026-11-04–05（权重） | 2.8T 总参数 / 104B 激活；93 层（69 KDA + 24 full attention）；896 experts、16 active；MXFP4 权重 / MXFP8 激活；1M 上下文 | K3 的大规模后训练版本：跨数百领域的联合 RL，优化 RL 框架/长上下文推理/沙箱/rollout 调度；**24 个 full-attention 层加入 DSA 稀疏索引（top-2048）**，解码每层读取字节约为稠密 MLA 的 1/4；Highspeed 变体 2–3× 吞吐。 | [Blog](https://www.kimi.ai/blog/kimi-k3-1-pro), [vLLM Blog](https://vllm.ai/blog/2026-11-04-kimi-k31-pro), [HF](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) |

### Zhipu AI (Z.ai)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| GLM-5.3 | GLM-5.3：前沿编码与涌现网络能力 | [GLM-5.3: Frontier Coding with Emergent Cyber Capabilities](https://z.ai/blog/glm-5.3) | Zhipu AI (Z.ai) | 2026-08-14 | 约 753B 总参数（约 40B 激活），MoE + DSA | 基于 GLM-5.2 的纯后训练增强；复杂编码显著提升，长时 Agent 与可调思考强度。 | [Z.ai Blog](https://z.ai/blog/glm-5.3) |
| GLM-5.3-Flash | GLM-5.3-Flash：前沿智能，Flash 成本 | [GLM-5.3-Flash: Frontier Intelligence, Flash Cost](https://z.ai/blog/glm-5.3-flash) | Zhipu AI (Z.ai) | 2026-08-26 | 320B 总参数 / 18B 激活；原生多模态；混合稀疏+线性注意力 | 首个 GLM-5 系列原生多模态模型；高性价比编程/Agent；可理解 UI 与渲染结果。 | [Z.ai](https://z.ai/) |
| GLM-Omni（研究） | 视觉生成能否扩展统一多模态模型的知识？ | [Can Visual Generation Expand What Unified Multimodal Models Know?](https://arxiv.org/abs/2610.21459) | Tsinghua / Zhipu AI | 2026-10（arXiv 2610.21459） | 基于 GLM-4.1V-Thinking（9B）+ X-Omni 离散图像 tokenizer | 提出 **Knowledge Transfer Probing (KTP)**；先画后答使文本问答准确率 26.86%→41.14%（数字任务 0%→36%）；揭示"能画不能答"的结构性鸿沟。 | [arXiv 2610.21459](https://arxiv.org/abs/2610.21459) |
| GLM-5.4 / 5.5（未发布） | GLM-5.4/5.5 研发方向 | [Zhipu Founder Outlines Next-Gen GLM-5.4/5.5 Plans](https://ai123.com/newshub/14767) | Zhipu AI | 截至 2026-11 未发布 | 目标从 740B+ 提升至至少 1T，预训练数据与规模显著扩展 | 方向：更强 SFT/RLHF/RLVR、长时推理与 Agent、**RSI（递归自我改进）**；截至 11/1 无发布。 | [报道](https://ai123.com/newshub/14767) |

### StepFun
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Step 5 Preview | 深入 Step 5 Preview：面向 Agentic 工作的架构与训练 | [Inside Step 5 Preview: Architecture and Training for Agentic Work](https://platform.stepfun.ai/blog/inside-step-5-preview) | StepFun | 2026-09-20（API 预览）/2026-10-15（开源权重 + 技术博客） | 600B 总参数 / 27B 激活；92 层"窄而深"；1M 上下文、64K 输出；text+image/video 输入 | 3:1 交错 Gated SWA 与稀疏 full-attention；**Sparse GQA**（块级 token 合并，索引/top-k 开销降至 1/8）；深度训练稳定性（FP32 关键状态、细粒度梯度裁剪）；百万级可验证环境 + 长时 RL、上下文压缩纳入策略训练；BF16/FP8/NVFP4 开源。 | [技术博客](https://platform.stepfun.ai/blog/inside-step-5-preview), [官网](https://www.stepfun.com/step-5-preview/) |

### Shanghai AI Lab (InternLM)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Intern-S2-Preview-397B | Intern-S2-Preview：科学 Agent 基础模型 | [Intern-S2-Preview: Scientific Agentic Foundation Model](https://arxiv.org/pdf/2608.13505) | Shanghai AI Laboratory | 2026-08-14（arXiv）/2026-09-13（发布） | 397B 总参数（A17B 激活）；多模态 MoE；262K 上下文；MTP | 科学多模态预训练（渲染科学文档视觉预训练、交错图文、图像检索）；统一后训练：SFT + 多任务 RL + 黑白盒 Agentic RL + on-policy distillation；新增时间序列预测分支；**Memory Decoder** 冻结主干快速专业化（Biology-Instructions 56.92→60.32）。 | [arXiv 2608.13505](https://arxiv.org/pdf/2608.13505), [HF](https://huggingface.co/internlm/Intern-S2-Preview) |
| Intern-S2-Mobius | Intern-S2-Mobius：解耦知识存储与组合推理 | [Intern-S2-Mobius](https://github.com/InternLM/Intern-S2-Mobius) | Shanghai AI Laboratory | 2026-08 | Mobius 架构族 | 共享记忆池扁平化组织知识，各层 Attention 均可访问；端到端推理效率约 Transformer 的 **4×**；60% 数据达到相近 MMLU PRO；昇腾 384 超节点原生训练/推理。 | [GitHub](https://github.com/InternLM/Intern-S2-Mobius), [昇腾社区](https://www.hiascend.com/zh/activities/dynamic-news/20260810-1) |

### ByteDance Seed
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Seed 2.0 | Seed 2.0 模型卡：面向真实世界复杂度的智能前沿 | [Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity](https://research.doubao.com/en/public_papers) | ByteDance Seed | 2026-06-19 | 未公开（Pro/Lite/Mini 多尺寸） | Omni-modal（video/image/audio/text）、实时交互、App 生成、音视频理解、Agent 编码与 GUI。 | [Model Card](https://github.com/ByteDance-Seed/Seed2.0), [arXiv 2607.00248](https://arxiv.org/abs/2607.00248) |
| doubao-seed-evolving | 豆包 doubao-seed-evolving 更新 | [doubao-seed-evolving release notes](https://aichina.news/news/bytedance-updates-doubao-seed-evolving-in-volcengine-model-list-l4eozi/) | ByteDance (Volcengine) | 2026-11（自动更新） | 未公开 | 深度思考模型：复杂 Agent 任务的多步规划与结果验证更完整，工具调用与事实一致性提升，延迟/成本下降。 | [报道](https://aichina.news/news/bytedance-updates-doubao-seed-evolving-in-volcengine-model-list-l4eozi/) |
| Recycler（研究） | Recycler：通过隐状态复用实现零成本潜在推理 | [Recycler: Cost-Free Latent Reasoning via Hidden State Recycling](https://seed.bytedance.com/zh/public_papers/1792932657675) | ByteDance Seed | 2026-09-28 | 轻量 adapter，解码开销可忽略 | 将 embedding 与上一 token 隐状态经 adapter 回灌下一步；~2% backbone 参数 MTP head 达到约 25% 规模独立模型 loss；优于 2–3× 参数模型。 | [Seed 论文](https://seed.bytedance.com/zh/public_papers/1792932657675) |

### xAI (Grok)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Grok 4.7 | Grok 4.7 模型卡 | [Model Card: Grok 4.7](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf) | xAI (SpaceXAI) | 2026-09-21 | 500K 上下文；text/image 输入、text 输出；Musk 称 4.7 为"2.1T 模型"（官方未确认） | 新更大基座 + 更长 RL（偏多小时级任务），自我校验与长上下文管理更强；原生理解 Grok Bot harness；全新安全栈，HackerBench v0.3 仅放行 3.3% 高风险双用途请求；推理档 low/medium/high/xhigh。 | [Model Card PDF](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf), [xAI News](https://x.ai/news/grok-4-7), [Docs](https://docs.x.ai/developers/models) |

### Amazon (Nova)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Amazon Nova 2（Lite / Pro / Omni / Sonic） | Amazon Nova 2：多模态推理与生成模型 | [Amazon Nova 2: Multimodal reasoning and generation models](https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models) | Amazon AGI | 2025-12-02 | 四款模型；最高 1M 上下文 | Lite/Pro 支持可配置 extended thinking（low/medium/high）；Omni 统一处理 text/image/video/audio 输入并生成 text+image；Sonic 语音到语音；内置 Responsible AI 护栏。 | [Amazon Science](https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models) |
| Nova 2.0 Lite（安全评估） | 在 Amazon 前沿模型安全框架下评估 Nova 2.0 Lite | [Evaluating Nova 2.0 Lite model under Amazon's Frontier Model Safety Framework](https://doi.org/10.48550/arxiv.2601.19134) | Amazon | 2026-01-27 | 1M 上下文；text/image/video | 针对 CBRN、攻击性网络行动、自动化 AI R&D 三类高风险域，结合自动基准、专家红队与 uplift 研究。 | [arXiv 2601.19134](https://doi.org/10.48550/arxiv.2601.19134) |

### Microsoft (Phi)
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Phi-4-reasoning-vision-15B | Phi-4-reasoning-vision-15B 技术报告 | [Phi-4-reasoning-vision-15B Technical Report](https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/) | Microsoft Research | 2026-03-04 | 约 15B；text+image 输入；16,384 输入 tokens；动态分辨率编码器（最多 3,600 visual tokens） | Phi-4-reasoning backbone + SigLIP-2 视觉编码器 mid-fusion；推理/非推理模式 token 混合；数据质量（过滤、纠错、合成增强）为核心杠杆。 | [MSR](https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/), [arXiv 2603.03975](https://arxiv.org/abs/2603.03975) |
| Phi-Ground-Any-4B | Phi-Ground-Any-4B（GUI grounding） | [Phi-Ground-Any-4B](https://www.microsoft.com/en-us/research/) | Microsoft Research | 2026-05 | 4B；固定 1,680×1,008 输入 | 从 Phi-3.5-Vision 微调的 computer-use / GUI grounding 专用模型，将自然语言指令与截图映射到界面位置或动作。 | [MSR](https://www.microsoft.com/en-us/research/) |

### Apple
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Apple Foundation Models（AFM 3） | 推出第三代 Apple 基础模型 | [Introducing the Third Generation of Apple's Foundation Models](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) | Apple | 2026-06-08（发布）/2026-09-14（AFM 3 Cloud 上线） | 五模型家族：AFM 3 Core（3B dense）、AFM 3 Core Advanced（20B sparse，1–4B 激活）、AFM 3 Cloud、ADM 3 Cloud (Image)、AFM 3 Cloud Pro（500B–1T 区间） | 与 Google 合作、为 Apple silicon 定制；**Instruction-Following Pruning (IFP)** 将全模型驻留 NAND、按 prompt 路由 expert；PT-MoE 升级；Private Cloud Compute 扩展至 Google Cloud NVIDIA GPU；QAT 压缩；端侧隐私优先。 | [Apple ML Research](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models), [AFM 3 Cloud 文档](https://developer.apple.com/download/files/AFM-3-Cloud-Model-Documentation-Form.pdf) |

### NVIDIA
| 模型 | 中文标题 | 英文标题 | 发布机构 | 发布日期 | 核心参数 | 主要创新点 | arXiv/链接 |
|---|---|---|---|---|---|---|---|
| Nemotron 3.5 Super / Lightning | Nemotron 3.5 Super 与 Lightning：面向 Agentic AI 的开放高效 MoE 混合 Mamba-Transformer 模型 | [Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Super-and-Lightning-Technical-Report.pdf) | NVIDIA | 2026-10-14（发布）/2026-10-27（报告） | Super：120B / 12B 激活，多模态；Lightning：30B / 3B 激活，文本 | 混合 Mamba-Transformer MoE；大规模蒸馏、长上下文训练、原生投机解码；Indic 继续预训练 + Agentic 软件工程 mid-training；SFT + RLVR/RLHF + **MOPD 多教师 on-policy 蒸馏**；Super SWE-bench Pro **51.78%**，GB200 最高 4,856 output tok/s/GPU。 | [NVIDIA Research](https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Super-and-Lightning/), [PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Super-and-Lightning-Technical-Report.pdf) |
| Nemotron 3.5 Bolt 74B-A9B 24GB | Nemotron 3.5 Bolt 74B-A9B 24GB：面向本地 AI 的混合视觉语言模型 | [Nemotron 3.5 Bolt 74B-A9B 24GB: A Hybrid Vision-Language Model for Local AI](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-Technical-Report.pdf) | NVIDIA | 2026-10-15 | 74B 总参数 / 9B 激活；24GB 内存；约 84 TPS on RTX Spark | 由 Super VL 120B-A12B 经 **Star Elastic** 压缩 + 2-bit QAD；混合 Mamba-Transformer；LiLiCorr 投机解码；面向本地 Agent、浏览与终端任务。 | [PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-Technical-Report.pdf) |
| Nemotron 3.5 Bolt E4B 4GB | Nemotron 3.5 Bolt E4B 4GB | [Nemotron 3.5 Bolt E4B 4GB Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB-Technical-Report.pdf) | NVIDIA | 2026-10-23 | 8B 总参数 / 4B 有效 | 基于 Gemma 4 E4B + Nemotron 后训练，优化速度/智能/显存占比，面向本地对话 Agent。 | [NVIDIA Research](https://research.nvidia.com/labs/nemotron/) |
| Nemotron 3.5 Transcribe | Nemotron 3.5 Transcribe 技术报告 | [Nemotron 3.5 Transcribe Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf) | NVIDIA | 2026-10-28 | 约 4.3B 激活；基于 Nemotron 3.5 Lightning 30B-A3B | 语音 LLM（SALM）：Transformer 语音编码器 + 冻结 diarization 模型 + 混合 Mamba-Transformer MoE LLM；单模型支持 verbatim/written/contextual/说话人归属转写、翻译、语种识别，40 语言；Open ASR Leaderboard WER 4.71%（英）/4.62%（多语）。 | [PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf) |

### 01.AI (Yi) / Baichuan
| 组织 | 状态 | 说明 | 链接 |
|---|---|---|---|
| 01.AI (Yi) | 无可验证新技术报告 | 2026 年公开渠道未见 Yi 系列新的主源技术报告/系统卡，主要为 API 与产品更新；需后续持续追踪。 | [01.AI](https://www.01.ai/) |
| Baichuan | 通用报告停留在 Baichuan 2 | 2026 年以医疗垂类（M 系列）为主；通用大模型最新可验证技术报告仍为 Baichuan 2（2023，7B/13B，2.6T tokens）。 | [Baichuan 2 报告](https://cdn.baichuan-ai.com/paper/Baichuan2-technical-report.pdf) |

## 技术趋势总结

| 研究方向 | 趋势观察 | 代表工作 |
|---|---|---|
| **新架构（MoE / Mamba / hybrid）** | 稀疏 MoE 已是旗舰默认；**混合/稀疏注意力成为长上下文主战场**（DSA、CSA+HCA、Sparse GQA），Mamba-Transformer 混合在效率优先场景（NVIDIA）持续落地；"窄而深"与跨层 KV 共享被用于降本。 | DeepSeek-V4（CSA+HCA）、Mistral Large 4（MLA+DSA）、Kimi K3.1 Pro（KDA+MLA+DSA）、Nemotron 3.5（Mamba-Transformer）、Step 5 Preview（Sparse GQA）、Intern-S2-Mobius |
| **训练方法（pre-training / post-training / RL / alignment）** | 竞争重心大规模转向**后训练与 RL 规模化**：跨数百领域联合 RL、Agent-authored 可验证环境、多教师 on-policy 蒸馏成为通用配方；纯后训练即可显著提升（GLM-5.3）。 | Kimi K3.1 Pro（大规模联合 RL）、Mistral Large 4（可验证环境+RL）、DeepSeek-V4（专家培养+on-policy distillation）、Intern-S2（多任务/Agentic RL）、Nemotron 3.5（MOPD） |
| **Scaling Law / 缩放分析** | 从"参数/数据 scaling"转向**效率 scaling**（每 GB 智能、每 token 成本、KV cache 占比）；小模型蒸馏 + 低比特量化在端侧逼近大模型。 | Nemotron 3.5 Bolt（Star Elastic + 2-bit QAD）、Apple AFM 3 Core Advanced（IFP）、Muse Glimmer 30B、DeepSeek-V4.1-Flash（KV cache 压缩） |
| **多模态模型** | "原生全模态"（text/image/video/audio 统一输入）成旗舰标配；图像生成与理解一体化（Omni）成为新方向；视觉编码器与语言主干深度融合。 | Gemini 4 Argon、Muse Wonder、Muse Spark Open、GLM-5.3-Flash、Mistral Large 4、Seed 2.0、Nemotron 3.5 Super VL |
| **长上下文模型** | 1M 上下文进入普及期，焦点转向**长上下文效率与 agent 可用性**（注意力压缩、KV cache、稀疏索引、长时目标保持）。 | DeepSeek-V4（1M 高效）、Kimi K3.1 Pro（1M）、Mistral Large 4（1M）、Gemini 4 Argon（1M）、Step 5 Preview（1M）、Muse Wonder（1M） |
| **推理模型 / reasoning model** | 混合推理（思考/非思考）与可调思考强度（low/high/xhigh）普及；推理与工具/Agent 深度耦合；**高风险能力评估（Preparedness / RSP / Frontier Safety）成为系统卡核心内容**。 | OpenAI GPT-6 Astra/Cyber（Preparedness Critical）、Anthropic 5.5 家族（RSP）、Gemini 4 Safety Report（CCL）、Grok 4.7（安全栈）、Claude Haiku 5.5（窄域 cyber 防护） |

## 报告保存信息

- **保存路径**: `wiki/synthesis/2026-11-07/tech-report-digest.md`
- **更新时间**: 2026-11-07
- **涵盖范围**: 19 个公司/组织的最新技术报告、系统卡、模型卡、技术博客与研究论文（含预览/未完全公开参数模型）
- **重点领域**: 架构（MoE/Mamba/hybrid）、训练方法、Scaling Law、多模态、长上下文、推理模型、Agent、安全评估
- **数据来源**: arXiv、官方博客/新闻、模型卡、Hugging Face、GitHub、NVIDIA Research、公司官网等公开渠道
- **备注**: 部分闭源模型参数未公开，表中参数多为厂商自报或社区推测（xAI 参数来自 Musk 公开表述，官方模型卡未确认）；Qwen4、GLM-5.4/5.5、Grok 4.8 截至 2026-11-06/07 尚未正式发布；01.AI (Yi) 与 Baichuan 缺乏可验证的 2026 新技术报告，已在覆盖表中标注。

---

*注：本 digest 基于公开信息整理，参数与链接可能随版本更新变化，建议以官方最新发布为准。*
