---
title: LLM 技术报告速览 — 2026-10-31
type: synthesis
created: 2026-10-31
updated: 2026-10-31
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, reasoning, long-context, multimodal, speech, cybersecurity, open-weights, daily-digest]
---

# LLM 技术报告速览 — 2026-10-31

> 覆盖窗口：2026-10-29 → 2026-10-31（增量版，基线为 [[tech-report-digest]] 2026-10-29）。本期只记录窗口内真正新增或状态变化的一手材料；上一期已详解的报告不重复展开。
>
> 口径：官方模型卡 / 系统卡 / 技术报告 / 开发者文档优先；厂商自报 benchmark 与第三方口径分开标注；未证实传闻不进入主表。

## 本期结论

- **Mistral Large 4 权重正式落地**：10-29 开放 FP8 / NVFP4 权重，采用 Mistral Ecosystem Open-Weight License；完整技术报告仍为「coming soon」。架构细节由 HF 技术博客补全：1T total / 49B active、72 层、MLA + DSA、128 experts top-4 + 1 shared、1M context。
- **OpenAI 发布 GPT-6 Luna（October 29）系统卡附录**：这不是新模型，而是 10-07 Luna 的行为更新，重点是更简洁、减少过度顺从；但 factual-error 指标全面变差，health / mental-health 多数下降，安全侧则出现 Pareto 改善与 99.91% 的 instruction-hierarchy 鲁棒性。
- **NVIDIA 同时补齐两条开放模型线**：Nemotron 3.5 Super / Lightning 技术报告（10-28，120B/12B 与 30B/3B，1M context，Mamba-Transformer hybrid MoE），以及 Nemotron 3.5 Transcribe（10-28，30B backbone / 34B checkpoint 含 MTP / 4.3B active，40 语种、1 小时音频）。
- **Gemini 4 Carbon 仍是「有发布、无模型卡」**：10-28 发布后，DeepMind model-card 列表截至 10-31 仍只更新到 Gemini 4 Argon（10-13）；Carbon 的参数、上下文与训练数据继续未披露。
- **DeepSeek V5 仍停留在代码占位符**：`deepseek-v5` / `v5-open` / `v5-next` 只在 Harness 测试文件中出现，官方无公告、无模型卡、无 API ID；截至 10-31 不应写成「已发布」。

## 24 小时变化总览

| 类型 | 条目 | 日期 | 状态 / 要点 |
|---|---|---|---|
| 权重发布 | Mistral Large 4（Le Chonk） | 2026-10-29 | **已开放** FP8 / NVFP4 权重；license 为 Mistral Ecosystem Open-Weight License；技术报告未发 |
| 系统卡更新 | GPT-6 Luna（October 29） | 2026-10-29 | 行为更新，非新模型；更简洁、降低过度顺从；factual error 上升 |
| 新增技术报告 | Nemotron 3.5 Super / Lightning | 2026-10-28 | arXiv `2610.38095`；120B/12B 多模态与 30B/3B 文本；1M context |
| 新增技术报告 | Nemotron 3.5 Transcribe | 2026-10-28 | 30B backbone / 34B checkpoint / 4.3B active；1h 音频、40 语种 |
| 发布但无模型卡 | Gemini 4 Carbon | 2026-10-28 | 官方博客 + 安全报告；model-card 列表未更新；限网络安全防御者 |
| 未证实信号 | DeepSeek V5 三个标识 | 2026-10-29 | GitHub 测试文件占位符；官方无公告 |
| 权重待发 | Kimi K3.1 Pro | 计划 2026-11-04 | 官方承诺 11-04 前发布权重；截至 10-31 未见 HF 仓库 |
| 未证实传闻 | GLM-5.5 | 2026-10 下旬 | 无官方 model card / API / 权重；不进入主表 |

## 公司与组织覆盖

| 公司/组织 | 最新已核实材料 | 日期 | 窗口内状态 |
|---|---|---|---|
| [OpenAI](https://openai.com/) | [GPT-6 Luna（October 29）System Card Addendum](https://deploymentsafety.openai.com/gpt-6-luna-october-28-2026-addendum) | 2026-10-29 | **新增**；行为更新；安全/事实性取舍明显 |
| [Mistral AI](https://mistral.ai/) | [Mistral Large 4 OSS](https://mistral.ai/news/mistral-large-4-oss/) + [HF Blog](https://huggingface.co/blog/mistral-large4) | 2026-10-29 | **权重已发**；技术报告待发 |
| [NVIDIA](https://research.nvidia.com/labs/nemotron/) | [Nemotron 3.5 Super / Lightning Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Super-and-Lightning-Technical-Report.pdf) | 2026-10-28 | **新增**；120B/12B + 30B/3B；1M context |
| [NVIDIA](https://research.nvidia.com/labs/nemotron/) | [Nemotron 3.5 Transcribe Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf) | 2026-10-28 | **新增**；语音线；34B checkpoint / 4.3B active |
| [Google DeepMind](https://deepmind.google/) | [Gemini 4 Carbon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) | 2026-10-28 | 有博客/安全报告；**仍无 model card** |
| [DeepSeek](https://www.deepseek.com/) | [DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969) | 2026-09-17 | V5 仅代码占位符；无新报告 |
| [Anthropic](https://www.anthropic.com/) | Claude Haiku 5.5 / Opus 5.5 | 2026-10 / 2026-09 | 无新系统卡 |
| [Meta AI](https://ai.meta.com/) | [Muse Spark Open](https://research.meta.ai/blog/muse-spark-open) / [Muse Glimmer 30B](https://arxiv.org/abs/2610.24628) | 2026-10-15 / 10-23 | 无新报告 |
| [xAI](https://x.ai/) | [Grok 4.7 Model Card](https://media.x.ai/v1/website/4p7card-5eccc980.pdf) | 2026-09-21 | 无新基础模型报告 |
| [Amazon (Nova)](https://www.amazon.science/) | Amazon Nova 2.5 Sonic（GA） | 2026-10-05 | 无新技术报告 |
| [Microsoft AI](https://microsoft.ai/) | [MAI-Base-2](https://microsoft.ai/pdf/Frontier-Pre-training-at-Microsoft-AI.pdf) | 2026-10-15 | 无新报告；Phi-5 仍无 model card |
| [Apple](https://machinelearning.apple.com/) | [AFM 3](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) | 2026-06-08 | 无新报告；仍无 arXiv 技术报告 |
| [ByteDance Seed](https://seed.bytedance.com/) | [Seed2.0](https://arxiv.org/abs/2607.00248) | 2026-06-30 | 无新报告 |
| [Qwen (Alibaba)](https://qwen.ai/) | [Qwen3.8-Flash-Next](https://arxiv.org/abs/2608.30320) | 2026-08-26 | 无新架构报告；Qwen3.8-Max 为产品线 |
| [Zhipu AI](https://z.ai/) | [GLM-5.3](https://z.ai/blog/glm-5.3) | 2026-08-14 | 无新报告；GLM-5.5 仍为传闻 |
| [Moonshot AI](https://www.kimi.com/) | [Kimi K3.1 Pro](https://www.kimi.ai/blog/kimi-k3-1-pro) | 2026-10-23 | 无新报告；权重计划 11-04 |
| [StepFun](https://www.stepfun.com/) | Step 5 Preview | 2026-10-15 | 无新报告；仍无正式 arXiv 技术报告 |
| [Shanghai AI Lab / InternLM](https://www.shlab.org.cn/) | [Intern-S2-Preview](https://arxiv.org/abs/2608.13505) | 2026-09-13 | 无新报告 |
| [Baichuan AI](https://www.baichuan-ai.com/) | [Baichuan-M4](https://arxiv.org/abs/2606.08982) | 2026-06-08 | 无新报告 |
| [01.AI (Yi)](https://www.01.ai/) | 无可验证的 2026 新技术报告 | — | 最新公开报告仍为 Yi-Lightning（2024-10） |

## 重点报告

### 1. OpenAI — GPT-6 Luna（October 29）System Card Addendum

| 字段 | 内容 |
|---|---|
| 中文标题 | GPT-6 Luna（2026-10-29）系统卡附录：更简洁、更少过度顺从的行为更新 |
| English title | Addendum to GPT-6 Luna System Card: October 29, 2026 Update |
| 发布机构 | OpenAI |
| 模型系列 | GPT-6 Luna |
| 发布日期 | 2026-10-29 |
| 核心参数 | 未披露；沿用 GPT-6 Luna（October 7）的数据与训练类型；文本 + 图像输入 |
| 安全等级 | Preparedness：Cybersecurity **High**；Biological and Chemical **High**；AI Self-Improvement 未达 High |
| 链接 | [Deployment Safety Hub](https://deploymentsafety.openai.com/gpt-6-luna-october-28-2026-addendum)；[PDF](https://deploymentsafety.openai.com/gpt-6-luna-october-28-2026-addendum/gpt-6-luna-october-28-2026-addendum.pdf) |

**主要变化**

- 这是 **行为更新**，不是新一代模型：同一 GPT-6 Luna 家族，10-07 首次进入 ChatGPT，10-29 更新为更简洁的回答并减少过度顺从（overly agreeable language）。
- 安全栈完全沿用 10-07 版本；Preparedness 等级不变，仍为 cyber High + bio/chem High，未达到 AI self-improvement High。
- 安全侧出现「Pareto 改善」：在 challenging prompts 上，安全处理率与合法请求 helpfulness 同时改善；prompt injection 的 instruction hierarchy 评测达到 **99.91%** 鲁棒性。
- 多轮 jailbreak 的 defender success rate 在每个 attacker budget 上都高于 10-07，但 OpenAI 注明攻击运行因基础设施问题提前终止，结论需谨慎。
- U18 安全评测在 sexual content、eating disorders、emotional reliance、gore 上改善；vision 评测与 10-07 基本持平。

**代价与回归**

- **事实性全面变差**：在 factuality-heavy、user-flagged、high-stakes 三组评测的六个指标上，10-29 版本的 factual-error rate 都高于 10-07；但仍低于 GPT-5.6 Luna。
- HealthBench 多数下降：Professional 长度调整分 48.2 → 47.4，HealthBench 50.4 → 48.2，Hard 27.2 → 22.8；Consensus 95.0 → 93.3。
- MentalHealthBench overall 51.73 → 48.68；non-acute 51.68 → 46.39，high acuity 53.92（较 10-07 的 56.15 下降），emergent 48.98 → 49.64。
- 生物安全拒答：severe prompts 改善（0.945 → 0.976），dual-use prompts 退步（0.968 → 0.922）。
- ExploitBench 46.19%，SEC-Bench Pro 51.75%（GPT-6 Astra 为 85.4%）。

**判断**

- 这次更新体现了一个明确取舍：**用更简洁、更少谄媚的交互换取事实性与健康/心理安全指标的下降**。对高风险场景，不能仅凭「更安全」的总体叙事忽略这些回归。
- 系统卡附录不是完整技术报告；没有参数、数据配比或训练细节。所有对比均为 OpenAI 自报，且注明历史模型可能使用后续版本。
- 对 agent 产品而言，99.91% 的 instruction-hierarchy 与 prompt-injection 结果比聊天风格更重要；但多轮 jailbreak 的攻击预算结论因运行中断而不完整。

### 2. Mistral AI — Mistral Large 4（Le Chonk）开放权重

| 字段 | 内容 |
|---|---|
| 中文标题 | Mistral Large 4（Le Chonk）：1T 级原生多模态开放权重 MoE |
| English title | Mistral Large 4 (Le Chonk) is now open weight |
| 发布机构 | Mistral AI |
| 模型系列 | Mistral Large 4 |
| 发布日期 | 2026-10-06 Public Preview；**2026-10-29 权重开放** |
| 核心参数 | 1.05T total；**49B active/token**；**52B including embeddings and output layers**；1M context；1.6B Pixtral vision encoder |
| 架构 | 72 层、hidden 6,144、64 attention heads；MLA + DeepSeek Sparse Attention（每 query 最多 2,048 key positions）；3:1 RoPE/NoPE；128 routed experts top-4 + 1 shared；首层 dense FFN，其余 71 层 MoE |
| 精度 / 许可 | FP8、NVFP4；GGUF（Unsloth / llama.cpp）；Mistral Ecosystem Open-Weight License（MIT 衍生，限制 model-as-a-service） |
| 链接 | [Mistral OSS 公告](https://mistral.ai/news/mistral-large-4-oss/)；[HF Blog](https://huggingface.co/blog/mistral-large4)；[HF 模型](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B) |

**主要创新点**

- 把 **MoE 稀疏 + 稀疏注意力** 组合在一起：router 选 expert，DSA indexer 选 context positions；两种稀疏性分别降低 FFN 与长上下文成本。
- 1M context 的原生多模态模型，文本 + 图像输入；视觉侧为 30 层、hidden 2,048、16 heads 的 Pixtral encoder，14×14 patch，patch-merge 空间合并 2。
- 三种 reasoning effort：`low` / `medium` / `high`，默认 `high`，且**不能真正关闭推理**（`none` 仍按 high 执行）。
- 明确面向 defensive cybersecurity：模型可在开放权重下复现漏洞再修补，避免闭源 API 的安全过滤阻断防御工作，也避免事件响应期间被断供。
- 推理生态 day-0：transformers、vLLM、llama.cpp、TRL 微调、HF Inference Endpoints；官方 vLLM 配方以 8×H200 服务 131K context（不是完整 1M）。

**关键数据（厂商自报 / HF 整理）**

- Artificial Analysis Intelligence Index：截至 10-29 为**第 5 好的开放权重模型**。
- DeepSWE v1.1 **61.7%**；SWE-Atlas-QnA **59.4%**；Terminal-Bench 4 **28.3%**；Coding Agent Index **49.8%**，高于 DeepSeek V4 Pro 0813 与 Qwen3.8 Max。
- AutomationBench **59.9%**；AA-Briefcase **1,393 Elo**。
- Artificial Analysis Cyber Index 漏洞复现+修补 **82%**；Cybench **93%**（40 题）；Lakera B3 攻击抵抗 **93.3%**。
- HF 实测：Q2_K 在单台 M3 Ultra 512GB 上 prefill ~90 tok/s、generation ~15 tok/s；4×RTX6000 Pro NVFP4 在 32K context 下 prefill 130–590 tok/s、generation ~10 tok/s。

**限制与判断**

- **完整技术报告仍未发布**；当前架构与 benchmark 主要来自 HF 技术博客、模型卡和合规文档，不是独立技术报告。
- 1M context 是模型能力，不等于服务能力：官方 vLLM 配方只服务 131K；长上下文真实吞吐需要按部署配置实测。
- 开放权重 license 不是 Apache/MIT：允许自托管与微调，但对模型即服务有限制；商用前需逐条阅读。
- Cyber 能力是双刃剑：开放权重让防御者可复现漏洞，也让滥用者获得同样能力；Mistral 以 refusal rate 与 usage policy 作为缓解，但不能替代部署侧管控。
- benchmark 全部为厂商自报；AA Index 与 Cyber Index 虽是第三方，但具体任务与评测口径仍需核对。

### 3. NVIDIA — Nemotron 3.5 Super 与 Lightning

| 字段 | 内容 |
|---|---|
| 中文标题 | Nemotron 3.5 Super 与 Lightning：面向 Agentic AI 的开放高效 MoE Hybrid Mamba-Transformer 模型 |
| English title | Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI |
| 发布机构 | NVIDIA |
| 模型系列 | Nemotron 3.5 |
| 发布日期 | 2026-10-28（arXiv `2610.38095`；技术报告 PDF 10-27） |
| 核心参数 | Super：**120B total / 12B active**，多模态（text / image / video / tool）；Lightning：**30B total / 3B active**，文本；两者均支持 **1M context** |
| 架构 | MoE Hybrid Mamba-Transformer；Super 从 Nemotron 3 Super 初始化，Lightning 从 Nano 3 Base 初始化；原生 MTP speculative decoding |
| 许可 / 精度 | OpenMDW 1.1；Base BF16、Post-trained BF16、NVFP4；附 LiLiCorr / DFlash / DSpark drafters |
| 链接 | [Technical Report PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Super-and-Lightning-Technical-Report.pdf)；[arXiv](https://arxiv.org/abs/2610.38095)；[项目页](https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Super-and-Lightning/) |

**训练与创新**

- **大规模蒸馏**：Super 用 Ultra 3 Base 作 teacher，Lightning 用 Super 3 Base 作 teacher，各蒸馏 1T tokens；Lightning 的 MTP head 通过 architecture-aware projection fusion + pruning 从 Super Base 初始化。
- **MTP 专门化**：两个非共享 MTP head 合并为一个递归共享 head；100B token MTP warm-up 时冻结 backbone；Super 增加 hidden-state mixing 以缓解递归 draft 的 train-inference mismatch。
- **Indic continued pretraining**：100B tokens（10B 合成/自然 Indic 数据 + 90B 原训练混合），覆盖 22 种印度语言、34 种语言-文字配置，五个 Indic benchmark 全部提升，最高 **+9.82pp**。
- **Agentic mid-training**：65.4B tokens、256K context，混合整仓库、issue-PR、commit history、build/CI log 与 agent trajectories；DeepSWE pass@1 6.4% → 10.4%，Codex harness 下 SWE-bench Verified 48.4% → 61.8%。
- **长上下文恢复**：256K mid-training 后追加 9B token recovery，RULER-1M 从 33.5 恢复到 **81.0**。
- **后训练**：两阶段 SFT 把 text-only base 变为 VLM；RLVR + RLHF；Super 额外训练 video reasoning/tracking、vision tool use、alignment 的专门 teacher，再用 Multi-teacher On-Policy Distillation（MOPD）合并。
- **测试时扩展**：并行 agent execution + self-verification，Terminal-Bench 2.1 **62.7% → 71.9%**，DeepSWE **24.6% → 34.5%**。

**关键数据（厂商自报）**

- Super SWE-bench Pro **51.78%**，超过 Nemotron 3 Ultra，且 active 参数约少 **4.6×**。
- MTP acceptance length：greedy 4.287 → **4.718**；probabilistic draft 3.787 → **4.612**（SPEED-Bench）。
- NVFP4 量化：36 个 benchmark 上相对 BF16 的 median accuracy recovery **99.62%**。
- 单张 GB200：20-turn agentic proxy workload 下最高 **4,856 output tokens/s/GPU**，同时维持 **≥50 tokens/s/user**。
- NVFP4 吞吐为 BF16 的 **2.43×**；Super 为 Qwen3.5 122B-A10B 的 **2.34×**、Qwen3.8 Flash-Next 的 **1.90×**。
- Lightning 为 30B/3B 文本模型，定位低成本部署；与 Super 共享 1M context 与 MTP 路线。

**限制与判断**

- **120B/12B 与 30B/3B 都是总参数/激活参数**，不能把 12B active 当成 12B dense 模型的显存占用；MoE 权重仍需按总参数存储。
- Super 的强项是 agentic software engineering 与长上下文；SWE-bench Pro 51.78% 是厂商自报，需与独立 harness 复现区分。
- Indic 增益是内部 benchmark，22 种语言不等于全部达到 production-ready；数据合成比例高，需关注污染与真实分布差异。
- 4,856 tok/s/GPU 是特定 20-turn proxy workload + NVFP4 + 优化 kernel 的结果，不是通用聊天吞吐。
- 技术报告很长且包含大量训练配方；复现时要注意数据、teacher 模型与 drafter 的耦合，单独换 backbone 未必保留同等收益。

### 4. NVIDIA — Nemotron 3.5 Transcribe

| 字段 | 内容 |
|---|---|
| 中文标题 | Nemotron 3.5 Transcribe：可指令控制的 40 语种语音转写语言模型 |
| English title | NVIDIA Nemotron 3.5 Transcribe Technical Report |
| 发布机构 | NVIDIA |
| 模型系列 | Nemotron 3.5（Transcribe） |
| 发布日期 | 2026-10-28 |
| 核心参数 | **30B backbone（31.6B）/ 34B checkpoint（含 1.3B MTP）/ 4.3B active**；65,536 token context；单段最长 1 小时；40 语种；最多 8 说话人 |
| 架构 | Transformer ASR encoder（0.6B）+ frozen Nemotron 3 Diarization（Sortformer，0.1B）+ modality adapter + Nemotron 3.5 Lightning 30B-A3B（52 层：23 Mamba-2、23 MoE、6 GQA）+ MTP + CTC timestamp adapter（50M） |
| 许可 / 精度 | OpenMDW-1.1；BF16 / FP8 / NVFP4 / GGUF；附 DFlash2 draft model |
| 链接 | [Technical Report PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf)；[项目页](https://research.nvidia.com/labs/nemotron/NVIDIA-Nemotron-3.5-Transcribe/)；[HF](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) |

**主要创新点**

- 单一 SALM 覆盖逐字转写、书面化、上下文注入、说话人归属、富文本事件/风格、语音翻译、语种识别与音频理解；转写风格由自然语言 instruction 在推理时选择，无需重训。
- Parallel Expert Encoder：ASR encoder 与 frozen Sortformer diarization 分支并行，30 秒 chunk 内独立处理，再由 LLM 维护跨 chunk 的长程一致性。
- 40 语种转写、31 语种与英语互译、13 语种说话人归属；最多 8 说话人；按需返回 word-level timestamps。
- CTC timestamp adapter 在生成后做 forced alignment，不要求模型在文本里显式输出时间戳。
- 训练为单阶段 SFT + 短 RL；发布 BF16/FP8/NVFP4/GGUF 与 NeMo Speech 微调工具包。

**关键数据（厂商自报）**

- English Open ASR Leaderboard 平均 WER **4.71%**；Multilingual Open ASR Leaderboard **4.62%**，均为开放权重最佳。
- 给定实体列表时，ContextASR-Bench 的命名实体错误降低 **6×**。
- 多说话人重叠语音的 speaker-attributed ASR 达到 SOTA；NVIDIA 称这是首个在该任务上超过专用级联系统的 SALM。
- NIM + NVFP4 下 **2,238× real time**；开源 vLLM/NeMo 路径会慢约 2×。
- checkpoint 总参数 **34B** 含 1.3B MTP；backbone 为 31.6B，active 4.3B 含音频编码器与适配器。

**限制与判断**

- 参数口径需要写清楚：模型名 30B、checkpoint 34B、backbone 31.6B、active 4.3B；上一期 digest 只写「34B total」容易让人误以为 backbone 是 34B。
- 这是**离线**模型，内部 30 秒 chunk 不等于流式实时 ASR；实时语音 agent 仍需流式方案。
- 说话人标签只区分录音内说话人，不建立真实身份；PII 场景需额外合规审查。
- 40 语种是覆盖范围，不是 40 个语种都达到同等质量；训练分布中英语占 36%，其余 32 个语种各不足 2.5%。
- 2,238× real time 是 NIM 优化路径的最优结果，开源复现应以 NeMo Speech / vLLM 为准。

### 5. 静默与未证实项复核

| 机构 / 条目 | 状态 | 复核结论 |
|---|---|---|
| Google DeepMind — Gemini 4 Carbon | 2026-10-28 发布 | 官方博客 + 安全报告；model-card 列表截至 10-31 仍无 Carbon；参数/上下文未披露；限 Fairwind 防御者 |
| DeepSeek — V5 | 2026-10-29 代码占位符 | `deepseek-v5`、`deepseek-v5-open`、`deepseek-v5-next` 仅在 Harness 测试文件；无官方公告/模型卡/API |
| Moonshot — Kimi K3.1 Pro | 2026-10-23 发布 | 权重承诺 2026-11-04；截至 10-31 未见 HF 仓库；K3 为 2.8T/104B、1M context |
| Zhipu — GLM-5.5 | 传闻 | 无官方 model card / API / 权重；GLM-5.3 仍是同 base 纯 post-training 的最新公开版本 |
| Anthropic — Haiku 5.5 / Opus 5.5 | 已发布 | 无窗口内新系统卡；Haiku 5.5 为 2026-10，Opus 5.5 为 2026-09 |
| Meta — Llama 5 | 传闻 | 无官方发布；Muse Spark Open / Muse Glimmer 30B 仍是最新可核实材料 |
| xAI — Grok 4.8 | 传闻 | 无官方发布；Grok 4.7 model card（09-21）仍是最新 |
| Microsoft — Phi-5 | 传闻 | 无官方 model card；MAI-Base-2（10-15）为最新可核实报告 |
| Qwen — Qwen3.8-Max 开放权重 | 未核实 | 2.4T/95B active 产品线存在；未确认窗口内开放权重 |
| Apple — AFM 3 技术报告 | 未发布 | 仍只有 2026-06-08 的 ML 博客与 model card，无 arXiv 技术报告 |
| ByteDance — Seed2.0 | 已发布 | 2026-06-30 arXiv `2607.00248`；无窗口内更新 |
| StepFun — Step 5 | Preview | 2026-10-15，600B/27B、1M context；仍无正式 arXiv 技术报告 |
| InternLM — Intern-S2 | 已发布 | Preview `2608.13505`（397B）；Mobius `2608.14290`（35B）；无窗口内更新 |
| Baichuan — M4 | 已发布 | 2026-06-08 arXiv `2606.08982`；临床 agent 系统，参数量未披露 |
| Yi (01.AI) | 无 2026 报告 | 最新仍为 Yi-Lightning（2024-10，arXiv `2412.01253`） |

## 跨公司趋势

| 方向 | 观察 | 代表工作 |
|---|---|---|
| 开放权重进入「1T 级 + 1M context」阶段 | 1T total / 50B active 成为新一代开放旗舰的常见规格；稀疏注意力 + MoE 是控制长上下文成本的核心 | Mistral Large 4、DeepSeek V4、Qwen3.8-Max、Kimi K3 |
| 效率优化从架构转向「训练 + 推理」全栈 | MTP、speculative drafters、NVFP4、hybrid state cache、量化感知蒸馏一起上；单点架构创新不足以解释吞吐提升 | Nemotron 3.5 Super/Lightning、Mistral Large 4、DeepSeek V4.1-Flash |
| 后训练与蒸馏仍是主要能力来源 | 同 base 纯 post-training 可显著提升 coding/agent；小模型通过大 teacher 蒸馏 + 领域 mid-training 逼近大模型 | GLM-5.3、Kimi K3.1 Pro、Nemotron 3.5（MOPD）、Mistral Large 4 |
| 安全与事实性出现显式取舍 | 更简洁、更少谄媚的更新可能带来 factual error 与 health benchmark 回退；安全评测不能只看单一总分 | GPT-6 Luna（October 29） |
| Cyber 能力成为旗舰模型的发布门槛 | 前沿模型以 cyber defense 为主卖点，同时以「限可信防御者」分阶段发布；开放权重则把 usage policy 交给部署方 | Gemini 4 Carbon、Mistral Large 4、GPT-6 Luna |
| 语音模型走向「可指令、可归因、长音频」 | 从单一转写扩展到说话人归属、翻译、富文本事件、上下文词表与音频问答；1 小时录音成为规格点 | Nemotron 3.5 Transcribe、Nova 2.5 Sonic、Grok Voice 3.0 |
| 「发布」与「可下载/可调用」继续分离 | 博客发布、model card、API、开放权重是四个不同状态；Carbon 有博客无模型卡，Mistral 有预览后补权重 | Gemini 4 Carbon、Mistral Large 4、Kimi K3.1 Pro |

## 与 2026-10-29 digest 的修订

| 条目 | 10-29 记录 | 10-31 核实 |
|---|---|---|
| Mistral Large 4 权重 | ETA 2026-10-29 18:00 UTC，尚未落地 | **已开放** FP8 / NVFP4 权重；license 为 Mistral Ecosystem Open-Weight License |
| Mistral Large 4 技术报告 | 架构细节未公开 | HF 技术博客补全 72 层 / MLA+DSA / 128 experts top-4 + 1 shared；**完整技术报告仍未发** |
| Nemotron 3.5 Transcribe 参数 | 34B total / 4.3B active | **30B backbone（31.6B）/ 34B checkpoint（含 1.3B MTP）/ 4.3B active** |
| OpenAI 最新材料 | GPT-6.1 Terra（10-26） | **GPT-6 Luna（October 29）系统卡附录**；Terra 仍是最新独立模型 |
| Mistral Large 4 激活参数 | 1T / 49B active（52B 含 embedding） | 维持；HF 模型名 `1T-A52B` 使用 52B 口径 |
| Gemini 4 Carbon | 无 model card | 维持；截至 10-31 model-card 列表仍无 Carbon |
| DeepSeek V5 | 代码占位符 | 维持；无官方公告/模型卡/API |

## 待验证与发布日历

| 日期 / 窗口 | 条目 | 需要验证的点 |
|---|---|---|
| 2026-11-04 | Kimi K3.1 Pro 权重 | HF 仓库是否出现、license、是否全量权重、是否含 K3.1 专属 drafter |
| 2026-11 上旬 | DeepSeek V5 | 是否正式发布、V5-Pro/V5-Flash 命名、是否延续 CSA+HCA、是否开放权重 |
| 待定 | Mistral Large 4 完整技术报告 | 训练数据、RL 配方、1M context 评测、cyber 能力细节 |
| 待定 | Gemini 4 Carbon 公开 model card / 广泛开放 | 参数、上下文、训练数据、guardrail 对 benchmark 的影响 |
| 待定 | GLM-5.5 | 是否存在官方 model card；目前只有传闻 |
| 待定 | Phi-5 | Microsoft 是否发布官方 model card / 技术报告 |
| 待定 | Qwen3.8-Max 开放权重 | 是否开放、license、与 Flash-Next 的架构差异 |

## 可信度与口径

- **所有 benchmark 均为厂商自报**，除 Artificial Analysis、Open ASR Leaderboard、Lakera B3 等第三方榜单外没有独立复现；跨厂商表格不可直接横比。
- **Gemini 4 Carbon 仍无 model card**：参数、上下文、训练数据均未披露；官方博客与安全报告是仅有的技术材料。
- **GPT-6 Luna（October 29）是行为更新，不是新模型**：系统卡附录明确沿用 10-07 的数据与训练；事实性/健康指标的回归是本期最重要的负面信号。
- **Mistral Large 4 的完整技术报告尚未发布**：架构与 benchmark 来自 HF 技术博客、模型卡与合规文档；license 对 model-as-a-service 有限制。
- **Nemotron 3.5 Transcribe 的参数口径容易混淆**：模型名 30B，backbone 31.6B，checkpoint 34B（含 MTP），active 4.3B（含音频编码器）。
- **DeepSeek V5、GLM-5.5、Llama 5、Grok 4.8、Phi-5 均为未证实或未发布项**：不进入主表，等待官方 model card。
- **开放权重的「发布」以可下载文件与 license 为准**，不以博客或 API 预览为准。

## 结论

- 如果只看窗口内真正新增的一手材料，优先级是：**Mistral Large 4 权重（10-29）> GPT-6 Luna 系统卡附录（10-29）> Nemotron 3.5 Super/Lightning（10-28）> Nemotron 3.5 Transcribe（10-28）**。
- 如果看「能力方向」，开放权重已经进入 1T 级 + 1M context 的竞争，但真正的差异化越来越在 **训练配方、蒸馏、量化与推理系统**，而不是单个架构名词。
- 如果看「安全」，GPT-6 Luna 的更新说明「更简洁、更少谄媚」不是免费午餐：事实性与健康/心理安全指标出现回退，安全评测必须分项看。
- 如果看「下一个节点」，Kimi K3.1 Pro 的 11-04 权重是最近一个确定日期；DeepSeek V5 仍只有代码占位符，不应提前赋予参数或发布时间。

---

*Generated for karpathy-wiki. 外部链接与厂商自报数据以 2026-10-31 抓取时点为准；后续 digest 应继续跟踪 Mistral Large 4 技术报告、Kimi K3.1 Pro 权重、DeepSeek V5、Gemini 4 Carbon model card 与 Phi-5 官方报告。*
