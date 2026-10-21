---
title: "LLM Tech Report Digest — 2026-10-21"
type: synthesis
created: 2026-10-21
updated: 2026-10-21
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, meta, muse-glimmer, deepseek, deepinfer, inference-infra, google, torchtpu, pytorch, amazon, torchneuron, trainium, mistral, voxtral, voice-agent, openai, terra, anthropic, intent-inference, governance, dhs, deepseek-ban, export-control, mofcom, kimi-k3.1-rumor, gtc-berlin, backfill, daily-digest]
---

# LLM Tech Report Digest — 2026-10-21

> **窗口判定：2026-10-20 → 2026-10-21（周二→周三上午）。19 家目标机构窗口内 0 份全新 frontier 模型卡 / 系统卡**，但并非静默日——本期是**补录 + 基础设施开源日**。三条实质增量：① **补录 Meta Muse Glimmer 30B 技术报告**（arXiv:2610.24628，v1 10-17 提交、**v2 10-20 修订**，Meta 官方页面 10-19；模型本体 08-10 已录 09-22 期，但**技术报告本身在 10-19/10-20 两期漏收**——10-19 期扫描 Monday 1,162 标题时因标题不含 "Technical Report" 字样漏检，本期补录）；② **三家目标机构同日把内部推理/加速器软件栈开源**：**DeepSeek DeepInfer**（10-20，Apache 2.0，V4.1-Flash 生产推理引擎，全库首录）+ **Google TorchTPU**（10-20，PyTorch Conference，TPU 原生 PyTorch 后端，取代 PyTorch/XLA）+ **AWS TorchNeuron**（10-19 官宣/10-20 开源，Trainium 原生 PyTorch 后端）——后两者同日发生在 PyTorch Conference；③ **Mistral Voxtral 3**（10-20 一手，语音 agent SDK + STT/TTS 模型家族，无开放权重）。信号层：**The Information 10-19 三模型预告**（Anthropic 意图推断新模型 / Google Gemini 4 Carbon / OpenAI Terra 家族新模型"数周内"，全部 single-source 二手、无一确认）；**DHS 对 DeepSeek 的联邦民用采购禁令 10-20 公开**（7 月 24 日签发，CNBC/Federal Register 一手可查，全库首录）。**NVIDIA GTC Berlin Keynote 今日 11:00–13:00 CEST（北京 17:00–19:00）尚未开始**——本期唯一在途事件锚点。**arXiv：10-17/10-20 两个时间戳均指向 Muse Glimmer 一篇目标机构报告**；Tuesday 10-20 block 尚未到收割时点（tentative）。

> **本期主线：① "推理栈开源"取代"模型开源"成为 frontier 实验室的开放前沿**——DeepInfer 是 leading lab 首次共享内部生产推理栈（interconnects 评为"近几个月最大的开源 AI artifact 之一"，并给出"DeepSeek 卖 token 毛利率可达 90%"的估算，⚠️ 估算口径），TorchTPU/TorchNeuron 则是 Google/Amazon 把自研加速器的 PyTorch 生态门槛一次性拆除（PyTorch Conference 同日双开源，Meta PyTorch 团队共同参与）——三家开放的都不是模型权重而是**运行时效率**；**② Muse Glimmer 技术报告补录坐实"端侧 agentic"赛道**——30B + 感知编码器、~4-bit 单卡、100+ 语言、Apache 2.0，对标 Gemma4-31B / Qwen3.6-27B，与 10-20 期 Timestral（209M 时序）构成 Meta/Mistral 同周的"小模型反 scaling"双注脚；**③ 三个"数周内"预告同日抵达（The Information）**——Anthropic 意图推断模型、Gemini 4 Carbon、OpenAI Terra 新模型，叠加此前的 `aurora-*-alpha` 与 `gpt-6.1-terra` 配置文件指纹，10 月下半月的发布密度预期被抬高，但**全部为不可采信的二手源**；**④ 美国对 DeepSeek 的动作从采购限制落地为系统性禁令**，与 10-19 期已录的中国 48 号公告构成中美"双向管制周"的完整闭环（模型卡本周持续缺位、管制条文密集的周主题延续）。**

---

## 本期要点（相对 2026-10-20 新增/更新）

- ★★ **补录：Meta Muse Glimmer 30B 技术报告（arXiv:2610.24628，v1 10-17 / v2 10-20；Meta 官方页面 10-19；328+ 作者）**——**模型本体 08-10 已录 09-22 期**（30B + 1.8B ViT-G、Apache 2.0、~4-bit <20GB、100+ 语言、Muse Spark 蒸馏），本期补的是**技术报告本身**：开源 30B 参数 causal LM + perception encoder，**为消费级硬件上的自主 agentic 任务专门构建**；文本+图入、文本出；**~4-bit 量化单 GPU 推理**；abstract 称在 tool use、multi-step planning、agentic task completion 上**同尺寸段 SOTA（vs Gemma4-31B 与 Qwen3.6-27B）**；Apache 2.0。arXiv v2 于 **10-20 修订**（落在窗口内）。**漏收标注：10-19 期 Monday block 扫描与 10-20 期均漏收（标题无 "Technical Report" 字样，被标题关键词过滤漏检）**；同日 `conference-digest`（10-21）已在其表格中列出该报告（Oct 19 条目），本页为机构线权威记录。**（详见 §1。）**
- ★★ **DeepSeek DeepInfer 开源（GitHub 一手，10-20；Apache 2.0；13.6k stars / 1.3k forks @核查时点）**——DeepSeek **生产级内部推理框架**首次公开，当前仅支持 DeepSeek-V4.1-Flash（默认 checkpoint `DeepSeek-V4.1-Flash-1017`）：优化 kernel 栈（FlashMLA / DeepGEMM / DeepEP / TileKernels / DeepSelect / 自研 TileLang kernel）、**DSpark + confidence-scheduled 投机解码**、SWA bounded replay（decoder prefill 截断保留后缀 140 tokens）、异步零开销批调度、**batch-invariant 推理 + 确定性采样**（NVIDIA）、结构化输出（regex/JSON schema/EBNF）；Attention DP + MoE EP + EPLB；**硬件：NVIDIA SM100 GPU + 华为 Ascend 950 NPU**；**基于 vLLM 构建（致谢 SGLang / TensorRT-LLM）**。**明确不含：KV cache 系统、VE/Prefill/Decode 分离（引擎侧大部分已实现）、DP 副本负载均衡——即开源的是核心引擎、非完整 serving 栈**。interconnects #25（10-20）：**"很可能比 vLLM/SGLang 在 DeepSeek 模型上高效得多"、"leading lab 首次共享内部推理工具"、"近几个月最大的开源 AI artifact 之一"**；给出"DeepSeek 在此栈上卖 token 毛利率可达 ~90%"估算（⚠️ 第三方估算，非 DeepSeek 口径）。全库此前 0 收录，本期首录。**（详见 §2。）**
- ★★ **Google TorchTPU + AWS TorchNeuron：PyTorch Conference 同日双开源（TorchTPU 10-20 一手三源；TorchNeuron 10-19 官宣/10-20 开源，Apache 2.0）**——**TorchTPU**（Google 与 Meta PyTorch 团队合作，2025 年中启动）：TPU 成为 PyTorch 原生设备（`torch.device("tpu")`），eager 默认 + `torch.compile`，**取代 PyTorch/XLA**；~450 Aten ops、Pallas/Helion 自定义 kernel、DTensor 分片；HF 下载量 top 5,000 模型开箱验证；四个仓库同日开源（TorchTPU / vLLM-TorchTPU / SGLang-TorchTPU / TorchTitan），vLLM-SGLang 原生后端分别与 Inferact / RadixArk 合作开发；已在 Google Cloud 最大客户生产在用；HF Transformers v5 原生 `device_map="tpu"`（Optimum TPU 不再必需）。**TorchNeuron**（Amazon）：Trainium 经 PyTorch `PrivateUse1` 注册为 `neuron` 设备，eager + `torch.compile` 双模式；Trainium2/3；集成 TorchTitan（FSDP）/ HF / vLLM Neuron；NKI 自定义 kernel（Neuron 2.33 同步新增 DeepSeek-V3.2、Kimi Delta Attention、GDN 等 25 个实验 kernel）；上游贡献 PyTorch 硬件无关化；早期用户 Cartesia、Lieber Institute 等。**战略含义：Google/Amazon 把"自研芯片的软件锁定"换成"PyTorch 生态的标准后端"——芯片竞争从硬件独占转向 PyTorch 设备注册表内竞争**。全库 0 收录，本期首录。**（详见 §3。）**
- ★ **Mistral Voxtral 3（mistral.ai/news 一手，10-20；无开放权重）**——语音 agent 全栈：① **Voxtral Small Transcribe 3**（50+ 语言 STT、diarization、keyphrase context-biasing、end-of-turn detection）；② **Voxtral Mini Transcribe Realtime 3**（实时转写，可配 80–2,400ms 延迟档，$0.008/min）；③ **Voxtral Mini TTS 3**（~90ms TTFA、34 情绪标签、Pro Voice 30 分钟音频适配，$13/1M 字符）；④ **Voice Agent SDK**（基于 LiveKit，听→推理→说单一流水线、各阶段独立模型可替换、SIP/WebRTC/IVR 接入，每轮 <1 秒，默认 Mistral Small 4 推理 $0.04/min）。EU/美国/全球端点 + on-prem；**HF 上无 Voxtral 3 权重（与早期 Voxtral 开源策略不同）**。定价对标 OpenAI/Deepgram/ElevenLabs（⚠️ Mistral 自报）。**注意与 10-20 期 Timestral 同为 Mistral"非 LLM 产品线"扩展，且 Voxtral 3 是封闭 API 形态。** **（详见 §4。）**
- ★ **The Information 10-19 三模型预告（single-source 二手，tbreak/testingcatalog/digitaltoday 等 10-19/10-20 二次传播；全库 0 收录，本期记为信号层）**——① **Anthropic**：正在准备一个**"比现有商用线更能推断用户底层意图与目标"**的新模型（测试者称：修一个 bug 会识别背后的问题族并询问是否一并修复）；**名称/系列（Fable 还是 Opus）/时间线/定价全部未知**，报道仅据一名测试者；testingcatalog 引述称"本月内发布"（⚠️ 二手的二手）；② **Google Gemini 4 Carbon**：Gemini 4 Argon（10-03 已录）的升级版，开发中（Business Insider 此前已报此代号；The Information 称开发者认为 Google 模型在视频分析/网站测试等视觉任务上仍强——Carbon 差异可能在感知而非推理）；③ **OpenAI Terra 家族新模型**："数周内"可能发布，**性能高于且价格低于 GPT-6.1 Sol**（Sol 本身"已接近 Astra"，⚠️ 均为报道口径）——填补 GPT-6 发布时缺席的 Terra 中档位。**公开法证旁证**：`gpt-6.1-terra` model id 10-16 出现在 **dotnet/efcore 的 PR**（18 个 eval 配置从 gpt-5.6-terra 切换）——**配置文件 ≠ 发布**。**三家均未确认名称/日期/定价，全部不采信为事实，仅作方向图**。**（详见 §5。）**
- ★ **DHS 对 DeepSeek 的联邦民用采购禁令 10-20 公开（Federal Register 一手 + CNBC 10-20；订单 2026-07-24 签发；全库首录）**——要求联邦民用机构（财政部/国务院/司法部等，**不含国防部**）从 IT 系统中移除 DeepSeek 相关技术、禁止采购其产品与服务，**覆盖使用 DeepSeek 模型构建的第三方产品与服务**；理由：敏感数据对华传输风险、模型安全隐患（引 iOS 应用多重漏洞的开源研究）；60 天内可申请例外。interconnects #25 同日讨论（含"是否波及以 DeepSeek 模型为训练配方的下游（如 Nemotron）"的开放问题）。**与 10-19 期已录的中国商务部 48 号公告（10-16）构成中美双向管制闭环**；MOFCOM 反应见 interconnects：其解读为"开源自动审批"，部分圈子反应过度。**（详见 §5。）**
- ★ **预告核验（连续第三日）**——"预计 10-19"双预告仍无落地：① **GPT-6.1 Sol 相关事件**：OpenAI 窗口内无新公告，`aurora-*-alpha` 三 ID 无新进展（OpenRouter 目录 10-18 收录维持既有记录，仍无成功调用证明）；② **智谱 GLM-5.3-Highspeed**：仍无官方发布。OpenAI 产品线窗口内动作 = **ChatGPT release notes 10-20**（GPT-6 Pro 并行 agent 拆分任务、GPT-Live-1.1、锁定对话、Slides）+ **Terminal X 研究/产品帖**（GPT-6.1 达资深投资人判断 88.6%）——均非模型卡。**Kimi K3.1 传闻二次出现**（interconnects #25：元数据开始出现在公共库，"rumored to be released very soon"）——**维持 10-03 期"传闻不采信"纪律**，无权重、无卡、无官方口径前不升格。
- ★ **GTC Berlin Keynote（今日 11:00–13:00 CEST / 北京 17:00–19:00，撰稿时尚未开始）**——10-15 Nemotron 3.5 Super VL/Bolt + RTX Spark 之后的 NVIDIA 下一机构动作窗口；Nemotron 系与 RTX Spark 生态后续卡大概率在此落地。10-20 二手报道（TechBriefly/SiliconANGLE）为 10-15 发布的二次传播，不重复。
- **补录（非窗口，修正既有漏收）**：① **Qwen-Image-2.1-Pro**（阿里；09-20 随 Qwen-Image-2.1 基座发布、10-02 百炼上架、10-09 Pro/Turbo API 开放——Turbo 已录 10-12 期，**Pro 此前 0 收录**；7B 单流 DiT、混合粒度注意力、前缀 KV 缓存复用、RGBA 透明、10 参考图；图像线，本期仅补索引不展开）；② **Anthropic Opus 5.5 fast mode GA**（10-15 Claude Platform release notes，10-16→10-20 五期均未录）：脱离 research preview、去 waitlist、2.5× 输出速度（OTPS 非 TTFT）、$8/$40 标准价 2×、Microsoft Foundry (Azure) 已上/Google Cloud "coming soon"、切档使 prompt cache 失效——**产品更新非新卡**，补记一行。
- **非目标机构排除记录（窗口内外围）**：Reflection **Beam-1.0-501B-A23B**（Apache 2.0，interconnects #25 称最强开源美国模型、token 效率仅次于 GPT-6-Astra——非目标机构）；MiniMax M3.1 Flash 权重 10-23 开放预告（10-20 期 M3.1 Flash 免费档后续）；Inception Mercury 3（10-20 期已排除）；Apple Tri-Modal Masked Diffusion 与 OpenAI low-resource programming languages 研究帖——**同日 `conference-digest` 10-21 已覆盖**，交叉引用不重复；Muse Spark Open on Fireworks（10-20，10-15 发布的分发渠道跟进，二手 10-15）。
- **静默**：**14/19 目标机构窗口内零新卡**——OpenAI（最新卡 09-29/10-07）、Google（Argon 无新卡；TorchTPU 为基础设施）、Anthropic（无新 Claude 卡；fast mode GA 为产品事件）、Qwen、Yi、Baichuan、Microsoft（MAI-Base-2 已录 10-17 期）、Apple（AFM 3 后持续静默）、xAI（**Grok 4.7 model card 已录 09-23 期；窗口内无新卡**——修正 10-19/10-20 期"卡仍缺"的错误措辞）、Amazon（**TorchNeuron 为基础设施，非模型卡**）、Zhipu（Highspeed 仍灰度）、InternLM、Moonshot（K3.1 传闻不采信）、StepFun、ByteDance。

---

## 一、Meta Muse Glimmer 30B 技术报告（arXiv:2610.24628；本期补录）

| 字段 | 内容 |
|------|------|
| **中文标题** | Muse Glimmer 30B：端侧 agentic 模型 |
| **英文标题** | Muse Glimmer 30B: An On-Device Agentic Model |
| **发布机构** | Meta（arXiv 328+ 作者；`ai.meta.com/research/publications/muse-glimmer-30b-an-on-device-agentic-model/` 10-19） |
| **时间** | v1 提交 2026-10-17 11:05 UTC；**v2 修订 2026-10-20 10:14 UTC（窗口内）**；Meta 页面 10-19；模型本体 08-10 已录 09-22 期 |
| **性质** | **技术报告（模型已于 08-10 开源，本期补报告非补模型）** |
| **定位（abstract）** | 为**消费级硬件上自主 agentic 任务**专门构建的开源 30B causal LM + perception encoder；多步推理、可靠 tool use、失败恢复整合进单模型，**本地运行无需云基础设施** |
| **输入/输出/语言** | 文本+图像入、文本出；**100+ 语言**数据训练 |
| **推理** | **~4-bit 量化**，单 GPU 本地推理（09-22 期既有记录：配合 1.8B ViT-G、<20GB） |
| **基准（abstract 口径）** | tool use / multi-step planning / agentic task completion 上**同尺寸段 SOTA**，对标 **Gemma4-31B 与 Qwen3.6-27B**（⚠️ abstract 未给具体分数，细节须读正文；Muse Spark 蒸馏关系为 09-22 期既有记录） |
| **许可** | **Apache 2.0**（模型权重既有记录）；arXiv 本体 CC-BY |

**要点**
1. **漏收原因**：标题不含 "Technical Report" 字样，10-19 期 Monday block（1,162 标题）以该关键词过滤时漏检；10-20 期沿用 10-19 期扫描结论未重扫。**本期起：周一 block 扫描须同时记录"标题关键词法的已知盲区"**。
2. **与 09-22/09-28 期记录的关系**：09-28 期曾把"Muse Glimmer 09-28 发布"传闻正确判为 08-10 旧闻二次传播；本期补录的 arXiv 报告是**真实的新增物**（v1 10-17），与旧闻传播是两回事。
3. **赛道注脚**：与 10-20 期 Mistral Timestral（209M 时序）同周构成"小模型/端侧"双注脚——但 Glimmer 是 30B 级 agentic 基准的正面竞争，不是边缘避战；"on-device agentic"正在成为独立产品类目（vs Apple AFM 端侧助手路线）。
4. ⚠️ abstract 的 SOTA 声明为 Meta 自报且未附分数；引用须等正文/模型卡细节复核（本页未逐条核对 HTML 正文基准表，tentative）。

---

## 二、DeepSeek DeepInfer（GitHub 一手，2026-10-20；本期首录）

| 字段 | 内容 |
|------|------|
| **名称** | DeepInfer：DeepSeek 模型的高性能大规模推理框架 |
| **发布机构** | DeepSeek-AI（`github.com/deepseek-ai/DeepInfer`） |
| **发布日期** | 2026-10-20（interconnects #25 同日报道；仓库 3 commits 初始发布形态） |
| **性质** | **生产推理引擎开源（非模型、非论文）**；citation 为 GitHub misc |
| **许可** | **Apache 2.0** |
| **支持模型** | 仅 **DeepSeek-V4.1-Flash**（默认自动拉取 `DeepSeek-V4.1-Flash-1017`） |
| **核心特性** | kernel：FlashMLA / DeepGEMM / DeepEP / TileKernels / DeepSelect / 自研 TileLang；**DSpark + confidence-scheduled verification**（MTP 变长草稿，默认 max draft 5）；**SWA bounded replay**（YOCO prefill 截断，V4.1 默认保留 140 tokens 后缀）；异步零开销批调度（默认开启）；**batch-invariant 推理 + 确定性采样**（NVIDIA，`DEEPINFER_BATCH_INVARIANT=1` + 固定 seq_seed）；结构化输出（regex / JSON schema / EBNF）；Attention DP + balanced CP；MoE EP + EPLB |
| **硬件** | **NVIDIA SM100 GPU + 华为 Ascend 950 NPU**（双栈：CUDA 13 / CANN 9.2，`DEEPINFER_ACCELERATOR` 切换） |
| **工程基础** | **主要基于 vLLM 构建**，致谢 SGLang / TensorRT-LLM；Python 3.12 / GCC≥13 |
| **不含（README 明示）** | **KV cache 系统；VE/Prefill/Decode 分离（注："most required engine functionality is already implemented"）；DP 副本负载均衡**——开源的是核心引擎，完整 serving 栈未随发布 |
| **基准** | prefill（4×SM100）/ decode（64×SM100，单 scale-up domain）Pareto 图见仓库 doc/；复现脚本随附（⚠️ README 为图表，未给表格数字） |
| **热度** | @核查时点 13.6k stars / 1.3k forks |

**要点**
1. **interconnects #25 口径**："DeepSeek 跟着上述新闻发布了内部推理栈 DeepInfer，很可能比 vLLM/SGLang 等现有开源工具在 DeepSeek 模型上高效得多"；"顶级实验室内部都有推理效率高得多的工具，这是**我们第一次看到 leading lab 把它们共享出来**"；"虽然不是开放模型或数据集，我们认为这是**近几个月最大的开源 AI artifact 之一**"；"推理公司将快速采用，将压低 DeepSeek 模型的生态价格（或抬高其毛利）"；给出"~90% 毛利率"估算（⚠️ 第三方估算）。
2. **与 10-19 期 deepseek-recipe（10-19 开源）的关系**：recipe 是训练配方，DeepInfer 是推理运行时——DeepSeek 在**同周开放了训练与推理两端的内部工具**，配合 48 号公告"开源入公共领域即豁免"的逻辑，开源节奏与管制窗口的互动值得持续观察。
3. **Ascend 950 一等支持**（与 NVIDIA SM100 并列）延续 09-30 已录的 DeepSeek×Huawei 合作线；DeepInfer 双栈 = 该合作的第一个开源运行时产物。
4. ⚠️ "比 vLLM/SGLang 高效"为 interconnects 判断，仓库仅给出自家 Pareto 图，**无第三方对照评测**；"90% 毛利率"为估算，不得作为 DeepSeek 财务事实引用。

---

## 三、Google TorchTPU + AWS TorchNeuron：PyTorch Conference 双开源（10-19/10-20；本期首录）

| 字段 | **TorchTPU（Google）** | **TorchNeuron（Amazon/AWS）** |
|------|------------------------|------------------------------|
| **发布** | 10-20，PyTorch Conference；`cloud.google.com/blog` + `pytorch.org/blog` + Google Developers Blog 三源一手 | 10-19 `aboutamazon.com` 官宣 / 10-20 PyTorch Conference NA 开源；`pytorch.org/blog` 同步 |
| **性质** | TPU 原生 PyTorch 后端开源（与 Meta PyTorch 团队共同开发，2025 年中启动） | Trainium 原生 PyTorch 后端开源（Apache 2.0） |
| **设备注册** | `torch.device("tpu")` | PyTorch `PrivateUse1` → `neuron` 设备 |
| **执行模式** | eager 默认（含 DeferAndFuse eager 融合）+ `torch.compile`（OpenXLA/StableHLO） | eager + `torch.compile`（vLLM Neuron 已切原生 compile 为默认） |
| **取代/替代** | **取代 PyTorch/XLA**（官方建议新负载直接用 TorchTPU、存量迁移） | 替代既有 Neuron SDK 的 torch_xla 路径（Public Beta） |
| **覆盖** | ~450 Aten ops；HF 下载量 top 5,000 模型开箱验证；DTensor 分片；多机推理/训练验证 | Trainium2/3；TorchTitan FSDP / HF / vLLM Neuron / vLLM Omni；NKI 自定义 kernel |
| **生态** | vLLM-TorchTPU（×Inferact）、SGLang-TorchTPU（×RadixArk）、TorchTitan 四仓同日开源；HF Transformers v5 `device_map="tpu"`（Optimum TPU 退役） | 上游贡献 PyTorch 硬件无关化；HF 原生 Trainium 支持；每 build 对数十万模型回归测试；早期用户 Cartesia / Lieber Institute 等 |
| **战略读法** | TPU 从 JAX/TF 生态锁定转向 PyTorch 设备竞争 | Trainium 以"零重写"降低采用门槛，与 Google 同日同策略 |

**要点**
1. **同日双开源的信号**：自研加速器的竞争焦点从"硬件峰值/独占软件栈"转移到 **PyTorch 设备注册表内的可迁移性**——Meta（PyTorch 本家）同时参与 Google 侧合作，"PyTorch 成为硬件中立层"的行业收敛在本窗口获得最密集的一次确认。
2. **对模型报告线的间接含义**：训练/推理栈的 PyTorch 化降低多芯片供给壁垒——与 48 号公告的算力管制逻辑（管芯片不 PyTorch 代码）形成有趣张力（分析，非事件）。
3. ⚠️ 两者均无模型、无基准卡；TorchNeuron 为 Public Beta，TorchTPU 亦"active development"；性能宣称（如 HF 的 TPU decode 加速数字）为生态伙伴自报。

---

## 四、Mistral Voxtral 3（一手，2026-10-20）

| 字段 | 内容 |
|------|------|
| **发布机构** | Mistral AI（`mistral.ai/news/voxtral-3/`；docs.mistral.ai 模型页同日） |
| **发布日期** | 2026-10-20（the-decoder / AiLookout 同日跟进） |
| **性质** | **语音模型家族 + Voice Agent SDK 产品发布；无开放权重**（AiLookout 核查 HF 组织：0 权重，与早期 Voxtral 开源策略不同） |
| **组成** | Voxtral Small Transcribe 3（50+ 语言、diarization、context-biasing、end-of-turn）；Voxtral Mini Transcribe Realtime 3（80–2,400ms 可配延迟、WebSocket 流式，$0.008/min）；Voxtral Mini TTS 3（~90ms TTFA、35+ 语言/50+ 方言、34 情绪标签、Pro Voice 30 分钟音频，$13/1M 字符）；Voice Agent SDK（LiveKit；听→推理→说单流水线、阶段独立模型可换、SIP/WebRTC/IVR；默认 Mistral Small 4 推理 $0.04/min，其他模型 $0.08/min） |
| **部署** | Mistral API（EU/US/全球端点）+ on-prem / 私有云（联系销售）；主权部署是明牌卖点 |
| **要点** | ① 与端到端 speech-to-speech 路线相反：**分阶段模块化**（可换 LLM/语音/语言而不重写 agent）；② 与 10-20 期 Timestral 同属 Mistral"非文本基座"扩张，但 Voxtral 3 是封闭 API 形态、Timestral 是开放权重——**同公司两种开放度**；③ 定价对标 OpenAI/Deepgram/ElevenLabs（⚠️ Mistral 自报） |

---

## 五、信号层：The Information 三模型预告 + DHS DeepSeek 禁令 + 其他

### 5.1 The Information 10-19 三模型预告（single-source 二手；全部不采信为事实）

| 机构 | 报道内容 | 旁证 | 可信度 |
|------|----------|------|--------|
| **Anthropic** | 新模型"更能推断用户底层意图/目标"（修 1 bug → 识别问题族并询问是否全修）；推理与直觉更强；**名称/系列/时间/定价全未知**，仅一名测试者 | testingcatalog 引述"本月内发布" | **tentative（single-source 二手）** |
| **Google** | **Gemini 4 Carbon** = Argon 升级版，开发中；开发者称 Google 模型视觉任务（视频分析/网站测试）仍强，Carbon 差异可能在感知 | BI 此前已报 Carbon 代号 | tentative（代号多源，细节无） |
| **OpenAI** | **Terra 家族新模型**"数周内"；性能高于且**价格低于 GPT-6.1 Sol**（Sol"已接近 Astra"） | **`gpt-6.1-terra` id 见于 dotnet/efcore PR（10-16 合并，@LuminaBench 10-19 发现），18 个 eval 配置切换** | tentative；配置 ≠ 发布 |

**读法**：三家同月预告 + `aurora` 三 ID（10-17/18 已录）+ `gpt-6.1-terra` 指纹 → 10 月下半月发布密度预期抬高；但**报道全部依赖匿名源，无一公司确认**——在官方公告前维持"传闻不采信"，仅登记为预告核验清单新条目（Terra"数周内"、Carbon"本月"、Anthropic 新模型"本月"）。

### 5.2 DHS DeepSeek 联邦禁令公开（Federal Register + CNBC，10-20；全库首录）

- 订单 **2026-07-24 签发、10-20 公开**（Federal Register `2026-21447`）：联邦民用机构须从 IT 系统移除 DeepSeek 相关技术并禁止采购；**覆盖基于其模型的第三方产品/服务**；财政部/国务院/司法部等适用，**国防部除外**；60 天例外申请通道。
- 理由（order 口径）：敏感政府数据对华传输风险、模型安全隐患（引 iOS 应用漏洞研究）。
- **开放问题（interconnects）**：对微调模型/以其输出训练的模型（例：Nemotron 配方长期依赖 DeepSeek 模型）如何适用，未明确。
- **周主题闭环**：10-16 中国 48 号公告（已录 10-19 期）+ 10-20 DHS 禁令 = **中美双向管制同一周落地**；模型卡稀薄、管制条文密集的周判断（10-20 期）在本期得到第二条腿。

### 5.3 其他

- **Kimi K3.1 传闻二次出现**（interconnects #25，10-20："metadata appearing in public libraries"、"rumored very soon"）——**维持不采信**；与 10-03 期纪律一致。
- **MOFCOM 反应**（interconnects #25）：开源自动审批、反应过度论、"防 Manus 式出售多于防前沿模型"的另类解读——48 号公告已有记录，本条为解读层交叉引用。
- **OpenAI 产品线 10-20**：ChatGPT release notes（GPT-6 Pro 并行 agent、GPT-Live-1.1、锁定对话、Slides）+ Terminal X 研究帖（88.6%）——非卡。
- **GTC Berlin Keynote**：今日 17:00–19:00 北京时间，**撰稿时未开始**——产出归下期；Nemotron 3.5 Super VL/Bolt（10-15）的 10-20 二手报道不重复。

---

## 六、19 家目标机构窗口复核（2026-10-20 → 10-21）

| 机构 | 本期状态 | 窗口内事件 / 最新已录卡 |
|------|----------|--------------------------|
| **Meta** | ★★ 补录 | **Muse Glimmer 30B 技术报告**（arXiv:2610.24628，v1 10-17 / v2 10-20，漏收两期后补录）；模型本体 08-10 已录；10-21 财报 |
| **DeepSeek** | ★★ 一手（infra） | **DeepInfer 推理栈开源（10-20，Apache 2.0）**；1017+Search API（10-17）已录 10-19 期；DHS 禁令公开（治理线） |
| **Google** | ★★ 一手（infra） | **TorchTPU 开源（10-20，PyTorch Conference）**；Gemini 2.5 系 10-20 退役（生命周期）；Argon 无新卡；Carbon 仅预告 |
| **Amazon** | ★★ 一手（infra） | **TorchNeuron 官宣开源（10-19/20，Apache 2.0，Trainium2/3）**；Nova 2（2025-12）后无新模型卡 |
| **Mistral** | ★ 一手（产品） | **Voxtral 3（10-20，封闭 API 语音栈）**；Timestral 已录 10-20 期；Large 4 开放权重仍承诺 10-31 |
| **Anthropic** | ★ 预告+补记 | The Information 意图推断新模型预告（tentative）；Opus 5.5 fast mode GA（10-15）本期补记；无新 Claude 卡 |
| **OpenAI** | 预告 | Terra 新模型"数周内"预告 + `gpt-6.1-terra` 配置指纹；"预计 10-19"事件连续第三日落空；产品线 10-20 更新非卡 |
| Zhipu | 无 | GLM-5.3-Highspeed 仍灰度；"预计 10-19"落空（连续第三日） |
| Moonshot (Kimi) | 传闻（不采信） | K3.1 metadata 传闻二次出现（interconnects #25）；K3 权重 07-27 既有 |
| xAI | 无 | **无新卡（Grok 4.7 model card 已录 09-23 期）**——修正 10-19/10-20 期"卡仍缺"错误措辞 |
| Qwen (Alibaba) | 补索引 | Qwen-Image-2.1-Pro（09-20 发布/10-02 上架）此前漏收，本期补索引不展开；无新 LLM 卡 |
| Microsoft | 无 | MAI-Base-2（10-15）已录 10-17 期；Guardian Agents（10-19）已录 10-20 期 |
| NVIDIA | 前瞻 | GTC Berlin Keynote **今日 17:00–19:00 北京**，未开始；Super VL/Bolt 已录 10-16 期 |
| Yi (01.AI) | 无 | 2026 年内持续静默 |
| Baichuan | 无 | 最新仍 Baichuan-M4（既有记录） |
| Apple | 无 | AFM 3（06-08）后持续静默；Tri-Modal Masked Diffusion 由 conference-digest 10-21 覆盖 |
| InternLM | 无 | Atria Dawn 正式版（10-17）已录 10-19 期 |
| StepFun | 无 | Step 5 权重（10-15）已录 10-16 期 |
| ByteDance (Seed) | 无 | Seed2.0 模型卡后无新卡 |

---

## 七、口径与不确定性

1. **Muse Glimmer 报告的 SOTA 声明为 abstract 级自报**：无具体分数（本页未逐条核对 HTML 正文基准表）；对标对象 Gemma4-31B / Qwen3.6-27B 分数未列——引用前须读正文，暂标 tentative。
2. **DeepInfer "更高效"与 "~90% 毛利率"均为 interconnects 第三方判断/估算**，无 DeepSeek 官方口径、无第三方对照评测；README 自家 Pareto 图未给表格数字。
3. **The Information 三预告全部 single-source/匿名源**：Anthropic 模型仅一名测试者、名称/时间全无；Carbon 仅有代号；Terra"数周内"无日期——**三家均未确认，全部维持不采信**，`gpt-6.1-terra` 配置文件仅证明 Microsoft 团队计划调用，不证明发布。
4. **DHS 禁令对下游模型（Nemotron 等使用 DeepSeek 配方者）的适用性未明**——order 文本未涵盖，interconnects 明确列为开放问题。
5. **漏收标注**：Muse Glimmer 技术报告漏收 10-19/10-20 两期（标题关键词过滤盲区，已记录方法论教训）；Opus 5.5 fast mode GA（10-15）漏收五期（10-16→10-20），本期补记；Qwen-Image-2.1-Pro 长期漏收，本期补索引。
6. **Grok 4.7 措辞纠错**：10-19/10-20 期"xAI | Grok 4.7 卡仍缺"与 09-23 期已补录的官方 model card 矛盾——正确表述为"卡已录 09-23 期，窗口内无新卡"，本期起沿用。
7. **arXiv 收割**：export API 此前持续空响应；Muse Glimmer v2（10-20 修订）经 abs 页直接核实；**Tuesday 10-20 block 尚未到常规收割时点**（本页以 abs/检索复核为主，tentative）。
8. **TorchTPU/TorchNeuron 性能数字**（如 HF TPU decode 加速、vLLM Neuron 吞吐提升）为生态伙伴/厂商自报，无第三方复现。

---

## 八、方法论

- **窗口与来源**：2026-10-20 → 10-21 上午；一手 = arXiv:2610.24628 abs 页（v1/v2 时间戳）+ `ai.meta.com` 出版物页、`github.com/deepseek-ai/DeepInfer` README（全文直读）、`cloud.google.com/blog` + `pytorch.org/blog`（TorchTPU）、`aboutamazon.com` + AWS Neuron 2.33 文档（TorchNeuron）、`mistral.ai/news/voxtral-3/` + docs、`federalregister.gov` 2026-21447（DHS）；二手 = interconnects #25（Brand/Lambert，10-20）、The Information 10-19 的 tbreak / theaigentic / aireport / digitaltoday / explainx 转述链、CNBC（DHS）、the-decoder / AiLookout（Voxtral）、Hugging Face blog（TorchTPU）。
- **去重（grep 全库，写入前）**：`DeepInfer` 0 命中；`Voxtral 3` 0 命中（Voxtral 1 系既有记录不受影响）；`Muse Glimmer` 命中 09-22/09-28/09-29 期（模型本体，非报告）——本期条目明确区分"模型已录/报告补录"；`TorchTPU`/`TorchNeuron` 0 命中；`2610.24628` 0 命中；`Carbon`/`Terra family`/`gpt-6.1-terra` 0 命中；`DHS` 命中为 09-24 及更早无关语境。
- **同日兄弟**：`conference-digest` 10-21（其表格已含 Glimmer Oct 19 条目 + Apple Tri-Modal + OpenAI low-resource languages——本页交叉引用不重复）；`arxiv-daily` / `arxiv-paper-check` 10-21（论文线；Glimmer 未入其 frontier 表，本页为机构线权威记录）；`investment-daily`（财报/GTC 投资视角由其覆盖）。
- **19 家机构以 CLAUDE.md 官方清单为准**（与 10-20 期复核表一致）；Amazon/Google 的 infra 发布计入机构动作但明确标注"非模型卡"。
- **在途事件纪律**：GTC keynote 撰稿时未开始——**不预写结论**，产出归 10-22 期（或今日晚些的追加条目）。
