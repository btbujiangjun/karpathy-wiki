---
title: "LLM Tech Report Digest — 2026-10-07"
type: synthesis
created: 2026-10-07
updated: 2026-10-07
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, hybrid-attention, scaling-law, long-context, multimodal, reasoning, RL, post-training, kv-cache]
---

# LLM Tech Report Digest — 2026-10-07

> 搜索各大 AI 公司最新大模型技术报告（Tech Report / Technical Report / System Card），重点关注大模型新架构（MoE, Mamba, hybrid）、训练方法（pre-training, post-training, alignment, RL）、Scaling Law / 缩放分析、多模态模型、长上下文模型、推理模型 / reasoning model。

> 本次检索基于最新公开技术报告与系统卡，聚焦 DeepSeek、OpenAI、Meta AI、Google DeepMind、Anthropic、Mistral AI、Qwen、Yi、Baichuan、Microsoft、Apple、NVIDIA、xAI、Amazon、Zhipu AI、InternLM、Moonshot AI、StepFun、ByteDance、Tencent、AI2、Xiaomi 等机构。检索窗口侧重 2026-09 至 2026-10-07。

## 本期要点（相对 2026-10-06 新增/更新）

- **DeepSeek-V4.1-Flash**（2026-09-10 发布，arXiv:2609.19969）：将 KV cache 压缩推向新极限，宣称在性能、成本、速度与总时延上全面超越 V4-Pro，并计划下线 V4-Pro。本期最重要的技术报告。
- **Gemini 4**（Google，2026-09-30 官宣）：仅公告、尚未正式上线（截止 2026-10-01 仍为 "Announced (not yet live)"），以长输出与网络防御 agent 能力为卖点。
- **OpenAI GPT-6.1 Sol / Sol Pro**（2026-09-29）、**Anthropic Claude Sonnet 5.5**（2026-09-28）：两家前沿 API 模型在本周内迭代。
- **Qwen3.8 Max Prime / GLM-5.3 Prime**（均 2026-09-23）：两家中国厂商同日推出旗舰（Prime）版本。
- **NVIDIA Nemotron 3 Diarization**（2026-10-04）、**AI2 Olmo-core 3**（2026-10-01）：月末月初的开放权重与训练系统进展。

---

## DeepSeek

| 项目 | 信息 |
|---|---|
| 中文标题 | DeepSeek-V4.1-Flash：突破 KV Cache 压缩的极限 |
| 英文标题 | DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression |
| 发布机构 | DeepSeek-AI |
| 模型名称/系列 | DeepSeek-V4.1-Flash（V4 架构家族最小成员） |
| 发布日期 | 2026-09-10（HuggingFace/API）；arXiv 2026-09-17 |
| 核心参数 | 552B backbone MoE 参数，另有约 196B Engram n-gram memory；prefill 激活 8B / decode 激活 16B；原生多模态（文本+图像）；1M token 上下文；45T token 多模态预训练语料 |
| 主要创新点 | **Causal Encoder-Decoder (CED)** 新架构（40 层拆为 20 层 encoder + 20 层 decoder，decoder 的 global KV 由 encoder 末层隐状态投影，prefill 仅跑 encoder 一半）；**Compressed Sparse Attention 2 (CSA2)** 跨层 KV 复用 + **FP4 KV caching**，将 global KV 降至 890 bytes/token（约为 V4-Flash 的 1/4）；**SWA Bounded Replay** 将持久化 KV 降至约 1/8；Engram n-gram memory、Hyper-Connections、DSpark 多 token 预测 draft head；混合 MXFP4/MXFP8 量化权重 |
| 基准 | GPQA Diamond 90.9、HLE 36.8、Codeforces 3471、Terminal-Bench 2.1 90.6、DeepSWE v1.1 74.2、CyberGym 88.1 |
| arXiv/论文链接 | [arXiv:2609.19969](https://arxiv.org/abs/2609.19969) · [HuggingFace 技术报告](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf) |

### DeepSeek-V4 系列（背景）

| 项目 | 信息 |
|---|---|
| 中文标题 | DeepSeek-V4：迈向高效百万 token 上下文智能体 |
| 英文标题 | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| 发布机构 | DeepSeek-AI |
| 模型名称/系列 | DeepSeek-V4-Pro（1.6T/49B 激活）、DeepSeek-V4-Flash（284B/13B 激活） |
| 发布日期 | 2026-04-26（preview） |
| 核心参数 | 1M token 上下文；>32T token 预训练 |
| 主要创新点 | 混合 CSA + HCA 注意力；Manifold-Constrained Hyper-Connections (mHC)；Muon 优化器；FP4 量化感知训练（QAT） |
| arXiv/论文链接 | [arXiv:2606.19348](https://arxiv.org/abs/2606.19348) |

## OpenAI

| 项目 | 信息 |
|---|---|
| 中文标题 | GPT-6.1 Sol 模型说明 / 系统卡 |
| 英文标题 | GPT-6.1 Sol Model / System Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-6.1 Sol、GPT-6.1 Sol Pro（含 batch 端点）；前序 GPT-6 Sol / GPT-6 Luna（2026-09-22）、GPT-6 Astra（2026-09-03） |
| 发布日期 | 2026-09-29（GPT-6.1 Sol / Sol Pro） |
| 核心参数 | 未公开参数量；GPT-6 Sol 系列 1M token 上下文、128k 最大输出；GPT-6 Astra 约 1.05M 上下文 |
| 主要创新点 | 持续迭代的推理/编码/agent 能力；Batch 端点与 Pro 档位覆盖成本敏感场景；系统卡侧重安全评估与路由（具体报告以官方发布为准） |
| arXiv/论文链接 | [OpenAI 发布页 / System Cards](https://openai.com/safety/) |

## Google DeepMind

| 项目 | 信息 |
|---|---|
| 中文标题 | Gemini 4（Argon）发布信息 |
| 英文标题 | Gemini 4 (Argon) Launch / System Documentation |
| 发布机构 | Google DeepMind |
| 模型名称/系列 | Gemini 4（"Argon"） |
| 发布日期 | 2026-09-30（官宣；截至 2026-10-01 尚未公开上线） |
| 核心参数 | 百万级 token 上下文与长输出（发布信息口径，具体数值以官方系统卡为准） |
| 主要创新点 | 长时程（long-horizon）推理与 agent 工作流；网络防御场景（自主发现/验证/修补漏洞）为对外演示重点；面向受信防御方分批开放，暂无公开 GA 日期 |
| arXiv/论文链接 | [Google DeepMind Gemini](https://deepmind.google/models/gemini/)（系统卡/技术报告见官方页面） |

> ⚠️ 说明：Gemini 4 的参数量、定价与基准数值在不同二手来源间存在差异，本条仅保留已确认的发布日期与定位，细节待官方系统卡发布后补录。

## Anthropic

| 项目 | 信息 |
|---|---|
| 中文标题 | Claude Sonnet 5.5 / Opus 5.5 系统卡 |
| 英文标题 | Claude Sonnet 5.5 & Opus 5.5 System Cards |
| 发布机构 | Anthropic |
| 模型名称/系列 | Claude Sonnet 5.5（2026-09-28）、Claude Opus 5.5（2026-09-22）、Claude Fable 5.1 / Mythos 5.1（2026-09-01） |
| 发布日期 | 2026-09-28（Sonnet 5.5） |
| 核心参数 | Opus 5.5：1M token 上下文、128k 输出；$4/$20（较 Opus 5 降约 20%）；Sonnet 5.5：$2/$10 |
| 主要创新点 | always-on thinking（默认开启思考，medium 思考预算）；计算机使用与终端 agent 能力（Terminal-Bench 4.0、OSWorld 2.0 提升）；安全评估驱动的系统卡 |
| arXiv/论文链接 | [Anthropic System Cards](https://www.anthropic.com/research/system-cards) |

## Meta AI

| 项目 | 信息 |
|---|---|
| 中文标题 | Muse Spark 1.3 / 1.3 Max |
| 英文标题 | Muse Spark 1.3 & 1.3 Max |
| 发布机构 | Meta AI |
| 模型名称/系列 | Muse Spark 1.3（2026-09-02）、Muse Spark 1.3 Max（2026-09-05） |
| 发布日期 | 2026-09-02 |
| 核心参数 | 1M token 上下文、131k 输出；$1.25/$4.25；API 形态（承诺后续开放权重） |
| 主要创新点 | 长上下文检索与代码库问答能力（MRCR、CodeBase QnA）强化；配套 Muse Spark Safety & Preparedness Report（安全与预备评估） |
| arXiv/论文链接 | 安全报告见 [arXiv:2606.12429](https://arxiv.org/abs/2606.12429)；模型见 Meta 发布页 |

## Mistral AI

| 项目 | 信息 |
|---|---|
| 中文标题 | Ministral 3 技术报告 |
| 英文标题 | Ministral 3 Technical Report |
| 发布机构 | Mistral AI |
| 模型名称/系列 | Ministral 3（3B / 8B / 14B）；Mistral Medium 3.5 |
| 发布日期 | 2026-01-13（arXiv） |
| 核心参数 | 小型 dense 系列 3B/8B/14B，262K 上下文（Mistral Medium 3.5 口径） |
| 主要创新点 | Cascade Distillation（级联蒸馏）训练配方；小模型效率与质量平衡；开放权重 |
| arXiv/论文链接 | [arXiv:2601.08584](https://arxiv.org/abs/2601.08584) |

> 注：Mistral 距预期下一次前沿发布已明显迟于节奏（据第三方 tracker，约为预约发布日之后 76 天），本期未见全新 frontier 系统卡。

## Qwen (Alibaba)

| 项目 | 信息 |
|---|---|
| 中文标题 | Qwen3.8-Next 架构设计：评估、效率与训练稳定性 |
| 英文标题 | On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability |
| 发布机构 | Qwen Team（阿里巴巴） |
| 模型名称/系列 | Qwen3.8-Flash-Next；旗舰 Qwen3.8-Max Prime（2026-09-23） |
| 发布日期 | 2026-08-31 |
| 核心参数 | 125B 总参数、6B 激活（MoE）+ 51B n-gram embedding 表（host offload）；上下文可扩展至 1M token |
| 主要创新点 | Gated DeltaNet (GDN) + Qwen Sparse Attention (QSA) 混合注意力；Gated Residual (GR)；n-gram embedding 扩容量；Muon 优化器与训练稳定性改进；约 1/9 训练 FLOPs 达到接近 397B-A17B 水平 |
| arXiv/论文链接 | [arXiv:2608.30320](https://arxiv.org/abs/2608.30320) |

### Qwen3.8-Omni

| 项目 | 信息 |
|---|---|
| 中文标题 | Qwen3.8-Omni：迈向原生全模态智能体 |
| 英文标题 | Qwen3.8-Omni: Towards Native Omni-Modal Agents |
| 发布机构 | Qwen Team |
| 模型名称/系列 | Qwen3.8-Omni-Flash |
| 发布日期 | 2026-09-22 |
| 核心参数 | 基于 Qwen3.8-Next MoE；上下文扩展至 1M token；原生多模态协同训练 |
| 主要创新点 | 原生全模态（文本-图像-音频-视频）协同训练；长上下文多模态推理；文本向音视频迁移 agent 能力；配套 Qwen-MM-Plugins、Qwen-Live-Harness |
| arXiv/论文链接 | [arXiv:2609.25611](https://arxiv.org/abs/2609.25611) |

## NVIDIA

| 项目 | 信息 |
|---|---|
| 中文标题 | Nemotron 3 Ultra 技术报告 |
| 英文标题 | NVIDIA Nemotron 3 Ultra Technical Report |
| 发布机构 | NVIDIA |
| 模型名称/系列 | Nemotron 3 Ultra（550B/55B 激活）、Nemotron 3 Super（120B/12B 激活）、Nemotron 3 Nano |
| 发布日期 | 2026-06-12（Ultra arXiv） |
| 核心参数 | 550B 总参数、55B 激活（MoE）；混合 Mamba–Transformer；NVFP4 预训练；1M 上下文（家族能力） |
| 主要创新点 | 混合 Mamba–Transformer MoE；NVFP4 预训练；多 token 预测（MTP）heads；开放权重（Open Model） |
| arXiv/论文链接 | [arXiv:2606.15007](https://arxiv.org/abs/2606.15007) |

### Nemotron 3 Diarization

| 项目 | 信息 |
|---|---|
| 中文标题 | Nemotron 3 Diarization（说话人日志模型） |
| 英文标题 | Nemotron 3 Diarization |
| 发布机构 | NVIDIA |
| 模型名称/系列 | Nemotron 3 Diarization |
| 发布日期 | 2026-10-04 |
| 核心参数 | 约 100M 参数；支持最多 8 个说话人 |
| 主要创新点 | 轻量级说话人日志（diarization）；面向流式/会议场景 |
| arXiv/论文链接 | 见 NVIDIA 模型页/技术博客 |

## xAI

| 项目 | 信息 |
|---|---|
| 中文标题 | Grok 4.7 发布信息 |
| 英文标题 | Grok 4.7 Release |
| 发布机构 | xAI / SpaceXAI |
| 模型名称/系列 | Grok 4.7（2026-09-21）；Grok 4.6（2026-08-12） |
| 发布日期 | 2026-09-21 |
| 核心参数 | Grok 4.6：500K 上下文、知识截止 2026-02-01、$2/$6（口径以官方为准） |
| 主要创新点 | 实时信息访问、推理与工具使用能力迭代；产品导向发布节奏 |
| arXiv/论文链接 | [xAI Blog](https://x.ai/blog/) |

## Zhipu AI（智谱 AI）

| 项目 | 信息 |
|---|---|
| 中文标题 | GLM-5.3 系列技术信息 |
| 英文标题 | GLM-5.3 Series |
| 发布机构 | Zhipu AI（智谱 AI / Z.ai） |
| 模型名称/系列 | GLM-5.3（2026-08-18）、GLM-5.3-Flash（2026-08-26）、GLM-5.3 Prime（2026-09-23） |
| 发布日期 | 2026-08-18（GLM-5.3） |
| 核心参数 | 约 753B MoE、约 40B 激活（5.3 系列口径）；GLM-5.3-Flash 支持 1M+ 上下文 |
| 主要创新点 | MoE 架构 + 强化 post-training；Flash 档以极低成本提供长上下文（$0.15/$0.50 量级）；工具调用与推理强化 |
| arXiv/论文链接 | [智谱 AI / Z.ai](https://www.zhipuai.com/) |

## Moonshot AI

| 项目 | 信息 |
|---|---|
| 中文标题 | Kimi K3 技术报告 |
| 英文标题 | Kimi K3 Technical Report |
| 发布机构 | Moonshot AI |
| 模型名称/系列 | Kimi K3（K2 后继） |
| 发布日期 | 2026-07-27 |
| 核心参数 | 2.8T 总参数、104B 激活（MoE）；原生视觉；1M 上下文 |
| 主要创新点 | KDA + Attention Residuals 混合设计；Stable LatentMoE（896 专家中激活 16）；相对 K2 约 2.5× 缩放效率；Muon 优化器；MoonViT-V2 视觉塔（从零训练） |
| arXiv/论文链接 | [arXiv:2607.24653](https://arxiv.org/abs/2607.24653) |

## Tencent（腾讯）

| 项目 | 信息 |
|---|---|
| 中文标题 | Hunyuan-A13B 技术报告 |
| 英文标题 | Hunyuan-A13B Technical Report |
| 发布机构 | 腾讯混元（Tencent Hunyuan） |
| 模型名称/系列 | Hunyuan-A13B；Hy4 Preview（2026-08-28） |
| 发布日期 | 2026-09-23 |
| 核心参数 | 80B 总参数、13B 激活（MoE）；20T token 预训练；256K 上下文 |
| 主要创新点 | 细粒度 MoE 与高效推理；长上下文（256K）；开放权重 |
| arXiv/论文链接 | [arXiv:2609.27284](https://arxiv.org/abs/2609.27284) |

## 其他值得关注

| 机构 | 模型/报告 | 日期 | 要点 | 链接 |
|---|---|---|---|---|
| AI2 | Olmo-core 3 | 2026-10-01 | 开放 MoE 训练系统，可扩展至万亿参数规模的开放训练栈 | [allenai.org](https://allenai.org/) |
| Fireworks AI | Ember-1 | 2026-09-24 | 面向高效推理的新模型 | [fireworks.ai](https://fireworks.ai/) |
| Google DeepMind | DiffusionGemma | 2026-07-31 | 离散扩散语言模型，256-token block，H100 约 1500 TPS，基于 Gemma 4 MoE（3.8B/25.2B） | [arXiv:2608.00146](https://arxiv.org/abs/2608.00146) |
| Xiaomi | MiMo-V2.6 Flash/Pro | 2026-09-21 | 轻量/旗舰双档；Pro-UltraSpeed 变体 | 官方模型页 |
| ByteDance | Douyin Multimodal Embedding (DME) | 2026-08-03 | 2B/9B 双档多模态嵌入，MMEB-v2 74.8/78.4 | [arXiv:2608.02148](https://arxiv.org/abs/2608.02148) |
| Microsoft | VibeVoice-ASR-Streaming | 2026-09-02 | LLM 端到端流式说话人归属 ASR | [arXiv:2609.02812](https://arxiv.org/abs/2609.02812) |

## 其他关注机构状态

| 机构 | 状态（2026-10-07） | 备注 |
|---|---|---|
| Yi（01.AI） | 较低活跃度 | 近期未见新的 frontier 技术报告/系统卡 |
| Baichuan | 持续更新 | Baichuan-Omni-1.5、Baichuan-M3-235B 等公开；需跟踪新报告 |
| Apple | 技术报告缺席 | 研究更多体现在系统与端侧智能层（AFM/Apple Intelligence），未见新 frontier 系统卡 |
| Microsoft (Phi) | 无新 frontier 报告 | 本期以 VibeVoice-ASR-Streaming 等应用/语音模型为主 |
| Amazon (Nova) | 无新报告 | Nova 系列持续更新，本期未见新技术报告 |
| StepFun（阶跃星辰） | 持续迭代 | Step 系列音频/多模态报告见 arXiv，未见新旗舰系统卡 |
| InternLM（上海 AI 实验室） | 持续迭代 | InternLumina-U2 等全视觉/扩散路线持续推进 |

## 补充说明

- **去重原则**：优先收录 2026-09 至 2026-10-07 的新报告/系统卡；对旧旗舰仅作背景保留（如 DeepSeek-V4、Qwen3.8-Next）。
- **口径说明**：OpenAI、Gemini、Claude、Grok 等未公开全部参数量，条目侧重发布时间、上下文/输出与定价等公开信息；部分数值来自第三方 tracker，存在不确定性，已在正文标注。
- **本期核心信号**：① **KV cache / 长上下文成本**成为竞争焦点（DeepSeek V4.1-Flash 的 CSA2 + FP4 与 CED 架构）；② **百万 token 上下文 + 长输出**趋于标配；③ **Prime/旗舰同日发布**显示中国厂商（Qwen、GLM）节奏加快；④ 开放权重阵营（NVIDIA、AI2、Tencent、Moonshot）持续供给可复现训练栈。
- **待复核**：Gemini 4 的定价/基准、GPT-6.1 Sol 的官方系统卡、Claude 5.5 系列完整评估，均需在官方文档公开后补录。
