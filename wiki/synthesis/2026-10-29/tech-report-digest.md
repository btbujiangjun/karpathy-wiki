---
title: LLM 技术报告速览 — 2026-10-29
type: synthesis
created: 2026-10-29
updated: 2026-10-29
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, reasoning, long-context, multimodal, speech, cybersecurity, open-weights, daily-digest]
---

# LLM 技术报告速览 — 2026-10-29

> 覆盖窗口：2026-10-28 → 2026-10-29（增量版，基线为 [[tech-report-digest]] 2026-10-28）。本期重点不是重复全量盘点，而是记录 24 小时内真正新增的一手材料、权重发布状态，以及仍未证实的发布信号。
>
> 口径：官方模型卡 / 系统卡 / 技术报告 / 开发者文档优先；厂商自报 benchmark 与第三方口径分开标注；未证实传闻不进入主表。

## 本期结论

- **Gemini 4 Carbon 把「网络安全」做成了旗舰模型的主卖点**：10-28 发布，Google 称其为最强模型，Artificial Analysis Intelligence Index v5 排名第 1（59），SEC-bench Pro 88.2%、ExploitGym 54.8%、CWE-bench 71.0%。但当前只向网络安全防御者小范围开放，且**尚无公开 model card**（模型卡 URL 与 PDF 均为 404）。
- **NVIDIA 补齐语音侧开放权重**：Nemotron 3.5 Transcribe 于 10-28 发布，34B total / 4.3B active，单段最长 1 小时、40 语种、最多 8 说话人，附完整技术报告 PDF，OpenMDW-1.1 许可，BF16/FP8/NVFP4 三档权重。
- **Mistral Large 4 权重进入最后倒计时**：HF 页面 ETA 为 **2026-10-29 18:00 UTC**（抓取时剩余约 18 小时，991 人等待）。官方文案为 **49B active/token，52B 含 embedding 与输出层**；10-28 digest 的「52B active」需要修正。
- **DeepSeek V5 只出现了代码占位符**：10-28 社区在 DeepSeek Harness 仓库测试文件中发现 `deepseek-v5`、`deepseek-v5-open`、`deepseek-v5-next` 三个标识，但官方没有公告、模型卡或 API ID；这是发布信号，不是技术报告。
- **其余目标机构 24 小时内无新增一手报告**：OpenAI、Anthropic、Meta、xAI、Amazon、Microsoft、Apple、ByteDance、Qwen、Zhipu、Moonshot、StepFun、InternLM、Baichuan、Yi 均维持此前材料；Kimi K3.1 Pro 权重仍计划 11-04。

## 24 小时变化总览

| 类型 | 条目 | 日期 | 状态 / 要点 |
|---|---|---|---|
| 新增一手报告 | Gemini 4 Carbon | 2026-10-28 | 发布博客 + 安全报告；无 model card；限网络安全防御者 |
| 新增一手报告 | NVIDIA Nemotron 3.5 Transcribe | 2026-10-28 | 技术报告 + 开放权重 + Granary v2 数据集 |
| 权重发布状态 | Mistral Large 4（Le Chonk） | ETA 2026-10-29 | HF `Upcoming release`；19:56 UTC 倒计时约 17h56m（抓取时） |
| 权重发布状态 | Kimi K3.1 Pro | 计划 2026-11-04 | 未提前；官方仍称 11-04 发布全量权重 |
| 未证实信号 | DeepSeek V5 (`v5` / `v5-open` / `v5-next`) | 2026-10-28 | GitHub 测试文件占位符；官方无公告 |
| 未证实传闻 | GLM-5.5 | 2026-10 下旬 | 参数 2.5–3.5T、窗口「10 月底/11 月初」；无官方材料 |
| 未证实传闻 | Meta Llama 5 / xAI Grok 4.8 | — | 均无官方发布；不进入主表 |

## 公司与组织覆盖

| 公司/组织 | 最新已核实材料 | 日期 | 24h 状态 |
|---|---|---|---|
| [Google DeepMind](https://deepmind.google/) | [Gemini 4 Carbon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) | 2026-10-28 | **新增**；网络安全 + 长程能力；限防御者；参数/上下文未披露 |
| [NVIDIA](https://research.nvidia.com/labs/nemotron/) | [Nemotron 3.5 Transcribe Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf) | 2026-10-28 | **新增**；34B/4.3B，1h 音频，40 语种，OpenMDW-1.1 |
| [Mistral AI](https://mistral.ai/) | [Mistral Large 4](https://mistral.ai/news/mistral-large-4/) | 2026-10-06 preview | 权重 ETA **2026-10-29**；1T total / 49B active（52B 含 embedding） |
| [DeepSeek](https://www.deepseek.com/) | [DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969) | 2026-09-17 | 无新报告；V5 仅代码占位符，未发布 |
| [OpenAI](https://openai.com/) | [GPT-6.1 Terra](https://openai.com/index/introducing-gpt-6-1-terra/) + [System Card Addendum](https://deploymentsafety.openai.com/gpt-6-1-terra) | 2026-10-26 | 已由 10-28 digest 覆盖；24h 内无新模型报告 |
| [Anthropic](https://www.anthropic.com/) | Claude Haiku 5.5（10-07）/ Claude Opus 5.5（09-22） | 2026-10-07 | 无新模型报告；10-28 为 AI for Science 药物研发博文 |
| [Meta AI](https://ai.meta.com/) | [Muse Spark Open](https://research.meta.ai/blog/muse-spark-open) / [Muse Glimmer 30B](https://arxiv.org/abs/2610.24628) | 2026-10-15 / 10-23 | 无新报告；Llama 5 传闻无官方发布 |
| [xAI](https://x.ai/) | [Grok 4.7 Model Card](https://media.x.ai/v1/website/4p7card-5eccc980.pdf) | 2026-09-21 | 无新基础模型；Grok Voice 3.0 为 10-14 语音模型 |
| [Amazon (Nova)](https://www.amazon.science/) | Amazon Nova 2.5 Sonic（GA） | 2026-10-05 | 无新技术报告；Nova 2 正式报告仍为 2025-12-02 |
| [Microsoft AI](https://microsoft.ai/) | MAI-Base-2 | 2026-10-15 | 无新报告；Phi-5 仍无官方 model card |
| [Apple](https://machinelearning.apple.com/) | [AFM 3](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) | 2026-06-08 | 无新报告；仍无 arXiv 技术报告 |
| [ByteDance Seed](https://seed.bytedance.com/) | [Seed2.0](https://arxiv.org/abs/2607.00248) | 2026-06-30 | 无新报告 |
| [Qwen (Alibaba)](https://qwen.ai/) | [Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next) | 2026-08-26 | 无新架构报告；Qwen3.8-Max 为产品线 |
| [Zhipu AI](https://z.ai/) | [GLM-5.3](https://z.ai/blog/glm-5.3) | 2026-08-14 | 无新报告；GLM-5.5 仅为传闻 |
| [Moonshot AI](https://www.kimi.com/) | [Kimi K3.1 Pro](https://www.kimi.ai/blog/kimi-k3-1-pro) | 2026-10-23 | 无新报告；权重仍计划 11-04 |
| [StepFun](https://www.stepfun.com/) | Step 5 Preview | 2026-10-15 | 无新报告；仍无正式 arXiv 技术报告 |
| [Shanghai AI Lab / InternLM](https://www.shlab.org.cn/) | [Intern-S2-397B](https://arxiv.org/abs/2608.13505) | 2026-09-13 | 无新报告 |
| [Baichuan AI](https://www.baichuan-ai.com/) | [Baichuan-M4](https://arxiv.org/abs/2606.08982) | 2026-06-08 | 无新报告 |
| [01.AI (Yi)](https://www.01.ai/) | 无可验证的 2026 新技术报告 | — | 最新公开报告仍为 Yi-Lightning（2024-10） |

## 重点报告

### 1. Google DeepMind — Gemini 4 Carbon

| 字段 | 内容 |
|---|---|
| 中文标题 | Gemini 4 Carbon：面向网络安全与长程任务的新一代前沿模型 |
| English title | Gemini 4 Carbon: our next frontier model |
| 发布机构 | Google DeepMind |
| 模型系列 | Gemini 4 |
| 发布日期 | 2026-10-28 |
| 核心参数 | 未披露（参数、上下文、训练数据均未公开）；原生多模态；基于 Gemini 4 Argon 继续推进 |
| 价格 | 介绍期 $2 / MTok input、$10 / MTok output；缓存输入 95% off；介绍期后 $4 / $20 |
| 链接 | [Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)；[Gemini 4 安全报告 PDF](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_safety_report.pdf) |

**主要创新点**

- 定位从「通用最强」转向 **cybersecurity defense + long-horizon agentic engineering**：Google 称 Carbon 可在内部连续运行数天，根因定位并修补大型代码库与底层系统中的隐蔽 bug。
- 网络安全覆盖完整生命周期：漏洞发现（SEC-bench Pro）、可利用性验证（ExploitGym）、根因修复（CWE-bench）。
- 在 Argon 的多层安全栈上继续做 alignment：减少走捷径、减少无依据断言、减少 overreach/under-service，并强化对间接 prompt injection 的抵抗。
- 发布策略保守：先向美国网络安全防御者小范围开放，再通过 Fairwind Program 扩大可信伙伴；同时参与美国政府自愿性预发布测试。

**关键数据（厂商自报）**

- Artificial Analysis Intelligence Index **v5 第 1，59 分**（第三方榜单，Google 引用）。
- SEC-bench Pro **88.2%**（发现真实漏洞）；ExploitGym **54.8%**（利用验证）；CWE-bench **71.0%**（补丁）。
- WebDev Arena **#4，1768**（+89 Elo）。
- 内部评测：生成安全代码成功率较 Argon **>2×**；Chrome 团队称其生成高质量补丁的表现比另一家实验室的前沿模型 **>10×**。
- Terminal-Bench 4.0 作弊成功率为 **0.0%**（尝试作弊率 0.4%）；内部高严重度 misalignment 告警下降近 **80%**。
- 无依据断言较 Argon 减少约 **2×**；overreach **-26%**、under-service **-29%**。
- Gray Swan Indirect Prompt Injection Benchmark 攻击成功率 **0.0%**（Argon 为 0.7%）。

**限制与判断**

- 这是发布博客 + 安全报告，不是完整技术报告；**没有 model card**（`deepmind.google/models/model-cards/gemini-4-carbon/` 与对应 PDF 均返回 404）。
- 当前不可公开调用，benchmark 为「无 guardrail」条件下的首方/第三方混合口径；实际部署能力会受安全层影响。
- 网络安全能力越强，滥用与出口管制/部署审查风险越高；「限防御者」是产品策略，也是风险控制。
- 与 Argon 的对比是家族内对比；跨厂商仍应看独立复现。

### 2. NVIDIA — Nemotron 3.5 Transcribe

| 字段 | 内容 |
|---|---|
| 中文标题 | Nemotron 3.5 Transcribe：面向 40 语种、长音频与说话人分离的开放语音语言模型 |
| English title | NVIDIA Nemotron 3.5 Transcribe Technical Report |
| 发布机构 | NVIDIA |
| 模型系列 | Nemotron 3.5（Transcribe） |
| 发布日期 | 2026-10-28 |
| 核心参数 | **34B total / 4.3B active**（含音频编码器）；65,536 token context；单段最长 1 小时；40 语种；最多 8 说话人 |
| 架构 | Mamba-2–Transformer hybrid MoE 语言模型 + Parallel Expert Encoder（Transformer ASR encoder + Sortformer speaker encoder）+ CTC timestamp head + MTP |
| 许可 / 精度 | OpenMDW-1.1；BF16 / FP8 / NVFP4；另有 DFlash2 draft model |
| 链接 | [Technical Report PDF](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Transcribe-Technical-Report.pdf)；[Hugging Face](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B)；[Granary v2](https://huggingface.co/datasets/nvidia/Granary-v2) |

**主要创新点**

- 单一 speech-augmented language model（SALM）覆盖转写、翻译、上下文转写、说话人归属、富文本转写、时间戳、语种识别与音频问答，减少多模型流水线。
- 通过 instruction 控制转写风格：逐字（含口头语）vs 书面化；可注入领域词表、说话人标签与时间戳。
- Parallel Expert Encoder 把 ASR 与 diarization 两条感知分支并行接入语言主干，支持长会议与多人对话。
- 训练数据以 Granary v2 为核心：约 **172 万小时**唯一音频（含重复曝光 653 万小时）、3.72 亿条音频样本、56 亿唯一文本 token。
- 推理侧提供 NIM 优化：单张 RTX PRO 6000 Blackwell 在 NVFP4 + DFlash2 下可达 **2,238 秒音频/秒**，30 秒录音 **0.13 秒**返回；开源 vLLM 路径约慢 2×。

**关键数据（厂商自报）**

- Open ASR Leaderboard 英文九集合平均 WER **4.71**（最佳开放权重；Qwen3-ASR-1.7B 为 4.94）。
- Long-form Open ASR Leaderboard 平均 WER **10.98**（Parakeet-TDT-0.6B-v3 为 13.37）。
- Multilingual Open ASR Leaderboard 平均 WER **4.62**（Qwen3-ASR-1.7B 为 6.49）。
- 多说话人 ASR 平均 cpWER **15.80**（DiCoW v3.3 + DiariZen 为 16.83）。
- Preference-ASR：默认/指令风格 WER **7.56 / 6.16**（Canary-Qwen 为 8.16 / 8.36）。
- FLEURS 部分语种：德语 2.73、法语 3.16、意大利语 1.41、中文 CER 8.62、日语 CER 4.42。

**限制与判断**

- 模型名写 30B，但官方 model card 明确 **34B total**；active 4.3B 含音频编码器，不能按 4B 纯文本模型估算显存/吞吐。
- 这是**离线**模型：内部 30 秒 chunk 不等于流式实时 ASR；实时语音 agent 仍需另配流式方案。
- 多说话人标签只用于区分录音内的说话人，不建立真实身份；PII 场景需额外合规审查。
- 部分语种为「Supported」而非「Leading/Production-ready」（如 Norwegian 在矩阵中几乎未验证，FLEURS WER 63.76），不能按「40 语种全覆盖」宣传。
- NIM 的最优吞吐尚未进入开源 vLLM/NeMo Speech 主线，复现时要以官方开源路径为准。

### 3. Mistral AI — Mistral Large 4（权重 ETA 2026-10-29）

| 字段 | 内容 |
|---|---|
| 中文标题 | Mistral Large 4（Le Chonk）：1T 级原生多模态开放权重 MoE |
| English title | Introducing Mistral Large 4 |
| 发布机构 | Mistral AI |
| 发布日期 | 2026-10-06（Public Preview）；权重 ETA **2026-10-29 18:00 UTC** |
| 核心参数 | 1T total；**49B active/token**；**52B including embeddings and output layers**；原生多模态；1M context；1.6B vision encoder |
| 价格 | $1.36 / MTok input；$0.14 cached；$4.18 / MTok output |
| 链接 | [Mistral Blog](https://mistral.ai/news/mistral-large-4/)；[Hugging Face（Upcoming release）](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B) |

**发布状态**

- HF 页面标题为 **Upcoming release**，ETA 显示 **October 29, 2026**；抓取时倒计时约 **17 小时 56 分**，**991** 人点击等待。
- 页面仍无模型文件、无 `LICENSE`、无 config/tokenizer；计划 artifact 只有 `mistralai/Mistral-Large-4-1T-A52B`。
- 10-28 digest 记录的 ETA 为 **10-31 15:00Z**；当前页面已改为 **10-29**，说明 Mistral 提前了目标时间（或页面倒计时口径变化）。
- 若今日 18:00 UTC 仍未落地，应继续标注「open-weight promised」，而不是「open-weight available」。

**参数口径修正**

- 10-28 digest 写「1.05T total / 52B active」；HF 官方文案更精确的表述是 **1 trillion total / 49B active per token / 52B including embeddings and output layers**。
- 模型名 `1T-A52B` 使用 52B（含 embedding/output）口径；做推理成本估算时应使用 **49B active**（或按实现确认是否包含 output layer）。
- 架构细节（层数、专家数、注意力模式）仍只在合规技术文档中，未公开完整技术报告。

**限制与判断**

- 权重未落地前，所有「开放权重」判断都只是承诺；license 未知，商用与再分发不可预设。
- 1T 级 + 49B active 的推理成本远高于 10B 级小模型，1M context 的真实吞吐需实测。
- 预览 API 可用不等于权重可用；HF 倒计时是平台展示，不是法律意义上的发布承诺。

### 4. DeepSeek — V5 代码占位符（未发布信号）

| 字段 | 内容 |
|---|---|
| 信号 | `deepseek-v5`、`deepseek-v5-open`、`deepseek-v5-next` |
| 发现时间 | 2026-10-28 |
| 来源 | DeepSeek Harness 官方 GitHub 仓库测试文件（与 `deepseek-v4-pro` 并列） |
| 官方状态 | 无公告、无 model card、无 API ID；截至 10-28 未发布 |
| 解读 | `v5-open` 不设版本阈值；`v5-next` 要求客户端升级；暗示「平滑过渡」与「强制更新」两条交付路径 |

**判断**

- 代码占位符只能说明团队在为 V5 做客户端/API 兼容准备，**不能推断发布时间或参数规模**。
- DeepSeek 当前最新可核实模型仍是 **V4.1-Flash-1017**（10-17，552B backbone，CED，1M context）。
- 若后续出现官方 model card，应重点核对：是否延续 CED、prefill/decode 非对称激活、FP4 KV，以及 V5 是否改变稀疏注意力路线。

### 5. 静默机构复核（24h 内无新增一手材料）

| 机构 | 最新已核实材料 | 复核结论 |
|---|---|---|
| OpenAI | GPT-6.1 Terra（10-26） | 10-28 新闻为 ServiceNow / Oracle 合作与「The future of the firm」，非模型报告；Terra 已由 10-28 digest 覆盖 |
| Anthropic | Claude Haiku 5.5（10-07）/ Opus 5.5（09-22） | 10-28 为 AI for Science 药物研发博文；无新系统卡 |
| Meta AI | Muse Spark Open（10-15）/ Muse Glimmer 30B（10-23） | 无新报告；Llama 5 相关说法互相矛盾且无官方来源，不采信 |
| xAI | Grok 4.7（09-21）/ Grok Voice 3.0（10-14） | Grok 4.8 未发布；语音模型不属于基础模型技术报告 |
| Amazon | Nova 2.5 Sonic（10-05 GA）/ Nova 2 报告（2025-12-02） | 无新报告；Sonic 为语音点版本 |
| Microsoft | MAI-Base-2（10-15）/ Phi-4-reasoning-vision（2026-03） | 无新报告；Phi-5 仍无官方 model card，二手规格不纳入 |
| Apple | AFM 3（2026-06-08） | 无新报告；iPhone 18 发布不等于新技术报告 |
| ByteDance Seed | Seed2.0（2026-06-30） | 无新报告 |
| Qwen | Qwen3.8-Flash-Next（2026-08-26） | 无新架构报告；Qwen3.8-Max / Flash-Next 为不同产品线 |
| Zhipu | GLM-5.3（2026-08-14）/ GLM-5.3-Flash（08-26） | GLM-5.5 传闻（2.5–3.5T、10 月底/11 月初）无官方确认 |
| Moonshot | Kimi K3.1 Pro（10-23）/ K3（07-27） | 无新报告；K3.1 Pro 权重仍计划 11-04 |
| StepFun | Step 5 Preview（10-15）/ Step 3.7 Flash（05-29） | 无新报告；仍无正式 arXiv 技术报告 |
| InternLM | Intern-S2-397B（09-13）/ Intern-S2-Mobius（08-14） | 无新报告 |
| Baichuan | Baichuan-M4（2026-06-08） | 无新报告；医疗模型路线未变 |
| Yi (01.AI) | Yi-Lightning（2024-10） | 仍无可验证的 2026 新技术报告 |

## 跨公司趋势

| 方向 | 观察 | 代表工作 |
|---|---|---|
| 安全能力成为发布门槛 | 前沿模型开始以 cyber 能力作为主卖点，同时以「限可信防御者」方式分阶段发布；cyber 风险等级直接决定部署范围 | Gemini 4 Carbon（限防御者）、GPT-6.1 Terra（cyber Critical）、GLM-5.3（emergent cyber） |
| 语音 / 音频成为新竞争面 | 开放权重语音模型从「转写」扩展到说话人分离、翻译、音频问答与 PII 脱敏；长音频（1 小时）与多说话人成为规格点 | Nemotron 3.5 Transcribe、Nova 2.5 Sonic、Grok Voice 3.0、Qwen3.8-Omni-Flash |
| 开放权重的「发布—可下载」时间差 | 1T 级模型先预览 API、后放权重，且 ETA 会滑动；license 与文件可用性比发布博客更重要 | Mistral Large 4（ETA 10-29）、Kimi K3.1 Pro（11-04）、Muse Spark Open（已发） |
| 长上下文转向长时任务 | 1M context 已不稀缺；竞争点变成「能否连续运行数天、跨代码库根因定位与修复」 | Gemini 4 Carbon、GPT-6.1 Terra、Kimi K3.1 Pro |
| 后训练仍是主增益 | 同基座纯 post-training 即可显著提升 coding/agent；新架构报告更多解决效率而非能力上限 | GLM-5.3、Kimi K3.1 Pro、Nemotron 3.5（MOPD + RLVR） |
| 混合架构继续扩散 | Mamba-2 + Transformer、GDN + QSA、Causal Encoder-Decoder 都在把长上下文成本拆开优化 | Nemotron 3.5 Transcribe（Mamba-2–Transformer）、Qwen3.8-Flash-Next（GDN+QSA）、DeepSeek V4.1-Flash（CED） |

## 与 2026-10-28 digest 的修订

| 条目 | 10-28 记录 | 10-29 核实 |
|---|---|---|
| Mistral Large 4 激活参数 | 1.05T total / 52B active | **1T total / 49B active per token / 52B including embeddings and output layers** |
| Mistral Large 4 权重 ETA | 2026-10-31 15:00Z | **2026-10-29 18:00 UTC**（HF 页面当前 ETA；仍未落地） |
| Google 最新模型 | Gemini 4 Argon（10-13） | **Gemini 4 Carbon（10-28）**；Argon 仍是最新有 model card 的 Gemini 4 |
| NVIDIA 最新报告 | Nemotron 3.5 Super / Lightning（10-21） | 新增 **Nemotron 3.5 Transcribe（10-28）**；语音/音频线 |
| DeepSeek 状态 | V4.1-Flash 为最新技术报告 | 维持；新增 **V5 代码占位符**信号（未发布） |
| 开放权重待发 | Mistral 10-31、Kimi 11-04 | Mistral 提前至 **10-29**；Kimi 维持 **11-04** |

## 可信度与口径

- **所有 benchmark 均为厂商自报**，除 Artificial Analysis / WebDev Arena 等第三方榜单外没有独立复现；跨厂商表格不可直接横比。
- **Gemini 4 Carbon 尚无 model card**：参数、上下文、训练数据均未披露；安全报告与博客是仅有的官方技术材料。
- **Nemotron 3.5 Transcribe 的名称与总参数不一致**：模型名 30B，官方 model card 为 34B total / 4.3B active（含音频编码器）。
- **Mistral Large 4 权重仍未落地**：HF 页面是 `Upcoming release`，ETA 可能再次滑动；license 未知。
- **DeepSeek V5 只是代码占位符**：没有官方公告、模型卡或 API ID，不应写成「已发布」。
- **GLM-5.5 / Llama 5 / Grok 4.8 均为未证实传闻**：不进入主表，等待官方 model card。
- **语音模型的语种覆盖需看质量分级**：40 语种不等于 40 语种都达到 production-ready；部分语种只有 Supported 级。
- **StepFun / InternLM / Baichuan** 的部分材料是博客或 model card，不是完整技术报告；已逐条标注。

## 结论

- 如果只看 24 小时内真正新增的一手材料，优先级是：**Gemini 4 Carbon（10-28）> Nemotron 3.5 Transcribe（10-28）> Mistral Large 4 权重落地（ETA 10-29）**。
- 如果看「能力方向」，Carbon 说明 frontier 竞争正在从通用 benchmark 转向 **cyber defense + 长时工程任务**；这类能力的发布将越来越受部署审查约束。
- 如果看「开放权重」，NVIDIA 把语音模型做成了完整技术报告 + 多精度权重 + 数据集；Mistral 则再次证明「预览 API ≠ 权重可用」，license 与文件才是硬指标。
- 如果看「下一个节点」，DeepSeek V5 的代码占位符值得跟踪，但在官方 model card 出现前不应赋予参数或日期；Kimi K3.1 Pro 的 11-04 权重发布是最近一个确定日期。

---

*Generated for karpathy-wiki. 外部链接与厂商自报数据以 2026-10-29 抓取时点为准；后续 digest 应继续跟踪 Mistral Large 4 权重、DeepSeek V5、Kimi K3.1 Pro 权重与 Phi-5 官方报告。*
