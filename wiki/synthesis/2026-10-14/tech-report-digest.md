---
title: "LLM Tech Report Digest — 2026-10-14"
type: synthesis
created: 2026-10-14
updated: 2026-10-14
sources: []
tags: [tech-report, LLM, technical-report, model-card, system-card, google, gemini-4-argon, anthropic, self-replication, frontier-red-team, nvidia, nemotron, mamba, moe, zhipu, glm, daily-digest]
---

# LLM Tech Report Digest — 2026-10-14

> **窗口判定：2026-10-13 → 2026-10-14。** 本期核心是 **Google Gemini 4 Argon 由"Fairwind 试点"转为全球 GA 并发布官方 model card（10-13）**——这是 09-30 亮相以来 Google frontier 侧首次落地完整"卡面"，也是本期唯一的一手 frontier 模型卡。同窗口内 **Anthropic Frontier Red Team 发布 self-replicating AI（weight-based replicator）研究（10-12，媒体 10-13）**、**NVIDIA 预告 Nemotron 3.5 Bolt 74B-A9B（10-13 预告 / 10-15 释出）**。对比 10-12/10-13 期：10-13 期记录"Argon 仍限 Fairwind 试点"，本期升级为 **GA + model card**。

> **本期主线：① frontier "卡面"再落地——Gemini 4 Argon（sparse MoE、1M 统一 input-output、Vals Index #1）；② 安全研究把"自复制 AI worm"推入可测边界（weight-based replicator，小模型年底或达标）；③ NVIDIA 用 Nemotron 3.5 Bolt 把"开放权重 + 24GB 本地 agent"打包成 RTX Spark 生态课题。**

---

## 本期要点（相对 2026-10-13 新增/更新）

- ★★★ **Google Gemini 4 Argon 全球 GA + Model Card（Google DeepMind，2026-10-13）**——**从限定 cyber 试点（Fairwind，09-30）转为全球可用**：开发者/企业走 Gemini API（`gemini-4-argon`，GA）、AI Studio、Android Studio、Google Antigravity；Google AI Ultra / Pro 订阅者在 Gemini app 与 AI Mode in Search 可用。**官方 model card 明确其为全新 frontier 模型、非既有 Gemini 的微调**：**sparse MoE + Transformer 架构，原生多模态输入（text / image / video / audio / PDF），输出 text**；**统一 input+output token 上限 1,048,576**（默认同步输出 65,536；long decode 经 continuation protocol 可至 1M）；thinking 三档 `low / medium（默认）/ high`；知识截止 **2026-03**。定价：**$2 / $10 per M tokens（缓存输入再 −95%）**，**2026-11-30 后标准价 $4 / $20**。Google 用自家卡面把 Argon 排在多项 **Vals Index 68.9%（自报 #1）**、AutomationBench 51.3%、Vals Finance Agent v2 65.4%、Harvey Legal 19.6%、DeepSWE v1.1 77.9%（对 GPT-6 Astra 74.1 / Claude Opus 5.5 74.2），并在 GraphWalks 长上下文（256k–1M BFS F1 84.2%）、LVBench 91.7% 领先；同时在 FrontierSWE v2 / Terminal-bench 4.0 / Terminal-Bench Science 0.1 / OSWorld-2.0 落后于部分对手。安全侧：随附 **217 页 "Developing Gemini 4 Argon responsibly and safely" 报告**，Gray Swan 间接 prompt injection 攻击成功率经 15 次自适应尝试压至 **0.7%**，CWE-bench v1 与 GPT-6 Astra 并列 68%。
- ★★ **Anthropic Frontier Red Team —「AI models may be capable of self-replicating without access to a datacenter」（Anthropic，2026-10-12；媒体 10-13）**——**weight-based replicator（权重自复制 worm）威胁模型**首次被拆分实验。结论：① **推理可行性**——**Qwen3.5-9B 在 9 类硬件中的 8 类**成功建立推理服务（Jetson Nano / Apple Silicon Mac / Xeon / Google TPU / AMD MI300X / RTX 4090 等）；**Gemma4-26B-A4B 跨 15 台约 $55 的非品牌 Android TV 盒子分布式运行，合计 0.39 tok/s**。② **端到端复制**——在 8 节点 GCP Android 15 模拟网络中，**仅 GLM-5.2（约 40B active）可靠跑通全链条**（5 次中 4 次 8/8、1 次 7/8），其余开放权重模型一致失败；作者明确这是 **upper bound**（未认证 ADB 端口令入侵步骤被"故意简化"）。③ **时间线**——按 Epoch Capabilities Index（年增约 13.7 点、R² 0.95）外推，**小模型（≤30B）约在 2026 年底达到 GLM-5.2 级复制能力**；防御目标是把 R0 压到 1 以下（ISP 流量监控可识别大文件权重传输、Mirai 先例 14 天内清除 92%）。
- ★★ **NVIDIA Nemotron 3.5 Bolt 74B-A9B（NVIDIA，2026-10-13 预告 / 10-15 释出）**——**面向 RTX Spark 本地 agent 的 MoE**：**74B 总参数 / 约 9B 激活**，**2-bit 量化 + QAT** 压进 **24GB** 内存；NVIDIA 称"比多数同级 dense 更快、比同级内存占用的 MoE 更聪明"（**均为厂商口径，权重 10-13 尚未公开**）。发布即支持 **llama.cpp / vLLM / Ollama / Unsloth / LM Studio**，并可直接被 **Hermes / OpenClaw** 等 agent 调用；**号称 fully open（weights + training data + recipes）**。同窗口另预告 **Nemotron 3.5 Bolt E4B（4GB，游戏 NPC / NVIDIA ACE）**，10-23 起经 SkyrimNET 试用；RTX Spark 笔记本 10-16 开卖、PAIR 本地 AI 路由器同日结束 beta。
- ★ **Zhipu GLM-5.3-Highspeed（Zhipu / Z.ai，2026-10-12）**——高速档上线 **Zcode 平台**（3.15.1 灰度、订阅用户随机放量）：**峰值生成 490 tok/s**（较上一代 GLM-5.3-FlashX 约 200 tok/s 翻倍以上）、**1M 上下文**、单次输出上限约 **128k token**、thinking 三档 `low / high / max`。
- ★ **交叉主题：窗口内 frontier 侧由"卡面"重新主导**——本期与 10-13 期连成短周期：Meta Muse Wonder（10-12）→ Gemini 4 Argon GA + model card（10-13）。同时 **安全研究的对象从"模型能力"转向"模型作为可复制基础设施"**（Anthropic replicator）与 **"开放权重下沉到消费级硬件"**（Nemotron Bolt、GLM-5.3-Highspeed）。

---

## 一、Google Gemini 4 Argon 全球发布 + Model Card（Google DeepMind，2026-10-13）

| 字段 | 内容 |
|------|------|
| **中文标题** | Google 发布 Gemini 4 Argon：首个 Gemini 4 frontier 模型全球 GA，1M 统一 input-output |
| **英文标题** | Gemini 4 Argon is now available for everyone / Gemini 4 Argon Model Card |
| **发布机构** | Google DeepMind（Koray Kavukcuoglu，SVP & Chief AI Architect） |
| **模型名称** | `gemini-4-argon`（内部代号 Barium-B；Gemini 4 家族，另有 Carbon / Barium 未公开） |
| **发布日期** | 2026-10-13（全球 GA + model card 同日；09-30 曾以 Fairwind cyber 试点亮相） |
| **核心参数** | **规模**：**large-scale sparse Mixture-of-Experts（MoE）Transformer**，原生多模态（text / image / video / audio 输入，text 输出）；**总量级未公开**。**上下文**：**统一 input+output token 上限 1,048,576**（非"输入+输出各 1M"），默认同步输出 65,536，long decode 经 **continuation protocol**（`continuation_token`）可达 ~1M；已知限制：long decode 仅 `v1beta1` `GenerateContent` API 支持。**思考**：`low / medium（默认）/ high`（设 `thinking_budget` 或 `MINIMAL` 会返回 HTTP 400）。**采样**：`temperature / top_p / top_k` 被忽略。**缓存**：仅 implicit caching（6,144 token 起，默认开启 durable），**不支持 explicit caching**。**能力**：function calling、structured outputs、code execution、Search/Maps grounding、computer use（preview）、agentic video understanding 支持；图像/音频生成与 Live API **不支持**。**训练**：Google TPU + JAX / ML Pathways。**知识截止 2026-03**。**定价**：$2 / $10 per M（cached input −95%），**2026-11-30 后 $4 / $20**。 |
| **主要创新点** | ① **统一 input-output token 预算（1M）**：把 thinking / function call / 最终答案计入同一 token 池，配合 **continuation protocol / long decode** 支撑超长单任务（Google 称"works longer and harder"）；② **frontier 定位下注"深度工作"**：面向软件工程、法律/金融知识工作、cyber 防御与科研，官方称 **Vals Index #1（68.9%）**；③ **安全与抗注入**：随附 217 页安全报告，**Gray Swan 间接 prompt injection 在 15 次自适应尝试下成功率 0.7%**，CWE-bench v1 68%（与 GPT-6 Astra 并列）；④ 发布即接入 Google Antigravity（agent-first 开发平台）与企业 Gemini for business。 |
| **关键 benchmark（model card，2026-10）** | **领先**：Vals Index 68.9%（GPT-6 Astra 63.1 / Fable 5.1 65.8 / Opus 5.5 67.0）、AutomationBench 51.3%、Vals Finance Agent v2 65.4%、Harvey Legal 19.6%、**DeepSWE v1.1 77.9%**、GraphWalks 256k–1M BFS F1 84.2%、LVBench 91.7%、LABBench 2 88.8%、RiemannBench 76.0%；**落后**：FrontierSWE v2 55.0%（Astra 65.5 / Opus 5.5 62.3）、Terminal-bench 4.0 57.4%（Opus 5.5 66.4）、Terminal-Bench Science 0.1 57.6%（Astra 68.1）、OSWorld-2.0 69.2%（Astra 72.6）；**持平**：CWE-bench v1 68.0%（与 Astra 并列）。 |
| **可信度** | 中高——**官方 model card + Google 自评表**；benchmark 为厂商发布口径，**部分基准缺独立第三方复现**（Frontier Desk 指出内部 harness 复现未披露）；Vals Index 为第三方但也由 Google 引用。 |
| **链接** | [blog.google Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)；[Model Card](https://deepmind.google/models/model-cards/gemini-4-argon/)；[Gemini API docs](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon)；[Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/gemini-4-argon-available-on-google-cloud) |

**与 Prior 对读**：10-12 / 10-13 期均记录"**Argon 仍限 Fairwind 试点、无 GA 日期**"；本期为 **首次取得 GA + 完整 model card**，故 **Argon 由"信号层/pilot"升级为"已发布 frontier 卡面"**。媒体（Moneycontrol）称本次发布发生在 DeepMind 组织大调整（Demis Hassabis 转任 Chair & Chief Scientist）之后，且此前 3.5 Pro 曾延期取消——**Argon 被视为 Google 重回 frontier 牌桌的一手**。

---

## 二、Anthropic：无数据中心自复制 AI（weight-based replicator）（Anthropic Frontier Red Team，2026-10-12）

| 字段 | 内容 |
|------|------|
| **中文标题** | Anthropic 研究：小模型或可在无需数据中心的情况下自复制（weight-based replicator） |
| **英文标题** | AI models may be capable of self-replicating without access to a datacenter |
| **发布机构** | Anthropic Frontier Red Team（William Zhou、Daniel Freeman） |
| **发布日期** | 2026-10-12（媒体同日/次日报道：Dark Reading、Al Jazeera、Tom's Hardware 等，10-13） |
| **核心论点** | 一类新恶意软件 **weight-based replicator（权重自复制体）**：不只传播可执行代码，而是把**模型权重 + 推理基础设施**一并搬到被感染设备。与普通 botnet 不同，**无中心节点可关停、且能自主适配不熟悉设备**（doubling time 以"天"计）。Anthropic 称**小模型可能"数月内"就能在商用 IoT（智能烤箱、非品牌 Android TV 盒子）上自复制**。 |
| **关键实验** | ① **推理落地**：**Qwen3.5-9B 在 9 类硬件中的 8 类**成功起推理（Jetson Nano / Apple Silicon Mac / Xeon 服务器 / Google TPU / AMD MI300X / RTX 4090 PC 等）；**Gemma4-26B-A4B 跨 15 台约 $55、4GB RAM 的非品牌 Android TV 盒子**分布式跑通（每台约 2 层），合计 **0.39 tok/s**。② **网络复制**：8 节点 GCP Android 15 模拟网，agent 经**未认证 ADB 端口**逐跳扩散并建立推理服务；**仅 GLM-5.2 端到端成功**（5 次中 4 次 8/8、1 次 7/8），其余开放权重模型一致失败；GLM-5.2 实际部署的是 **Llama3.1-8B** 作为 payload（用于统一比较），非复制自身权重。 |
| **时间线与防御** | 用 **Epoch Capabilities Index**（年增约 13.7 点、R² 0.95）外推：**≤30B 小模型约 2026 年底达到 GLM-5.2 的复制能力下限**。防御主张：目标是把 **R0 压到 1 以下**（而非零感染）；权重文件体量大、设备间流量显著 → **ISP 流量监控可捕获**；引 **Mirai 先例**（隔离+客户通知下 14 天清除 92% 感染，无通知 74%）；设备默认口令加固（如英国禁默认 IoT 密码）可缩小可及目标池。 |
| **关键限制（作者自陈）** | **Upper bound**：入侵步骤被"故意简化"（ADB 无认证），真实世界防护可能更难；端到端成功仅 1 个模型、且其自身 744B（~1TB）无法装在目标设备上；**估算速度极慢**（Qwen3.5-9B 建推理约 28–51 小时、Gemma4-26B-A4B 约 71–150 小时）；给弱模型配 Opus 4.8 当 advisor **无显著提升**；**无任何野外自复制案例**（AGI Watch 的 tripwire 未触发）。 |
| **可信度** | 中——**官方 red team 一手研究**，方法/数据具体；但为**高度有利的实验室上限设定**，作者反复强调"未证明现在可行"，商业解读（Tom's Hardware）称"当前部署不切实际"。 |
| **链接** | [anthropic.com/research/self-replicating-ai](https://www.anthropic.com/research/self-replicating-ai)；[Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-warns-of-self-replicating-ai-worm-threat-that-doesnt-need-data-centers-to-self-improve-and-spread-current-deployment-is-impractical-but-could-become-a-worry-as-tech-improves)；[Dark Reading](https://www.darkreading.com/perimeter/anthropic-ingredients-future-ai-worms) |

> **与 10-13 期对读**：10-13 期收录了 Anthropic 同日（10-12）的 **distillation 防御** 研究，但**未覆盖本篇 self-replication 研究**；本期作为该窗口的补录/主要安全条目建档。（另注：09-25 的 OpenAI "self-replicating **prompt injections**" 报告属不同主题——注入跨载体自我复制，与本文 weight-based replicator 非同一物。）

---

## 三、NVIDIA Nemotron 3.5 Bolt 74B-A9B（NVIDIA，2026-10-13 预告 / 10-15 释出）

| 字段 | 内容 |
|------|------|
| **中文标题** | NVIDIA 预告 Nemotron 3.5 Bolt 74B-A9B：74B 参数 2-bit 量化进 24GB，面向 RTX Spark 本地 agent |
| **英文标题** | NVIDIA Nemotron 3.5 Bolt 74B-A9B (announced Oct 13, releasing Oct 15) |
| **发布机构** | NVIDIA |
| **模型名称** | `Nemotron 3.5 Bolt 74B-A9B`；同窗预告别 `Nemotron 3.5 Bolt E4B`（4GB，游戏 NPC / NVIDIA ACE） |
| **发布日期** | **预告 2026-10-13；释出 2026-10-15**（RTX Spark 笔记本 10-16 开卖）；E4B 10-23 起经 SkyrimNET 试用 |
| **核心参数** | **74B 总参数 MoE / 约 9B 激活**；**2-bit 量化 + quantization-aware training** → **24GB 内存**（实际占用还受上下文/KV cache/运行时影响）。**号称 fully open：weights + training data + recipes**。发布即支持 **llama.cpp / vLLM / Ollama / Unsloth / LM Studio**，可被 **Hermes / OpenClaw** 等 agent 直接调用。E4B 为 **4GB** 级第三世代 SLM（NVIDIA ACE）。 |
| **主要创新点** | ① 把"前沿级 MoE + 极端量化"压进消费级 **24GB**，主攻 **always-on 本地 personal agent**（coding、research、monitoring、tool use）；② 用**全开放（含训练数据与配方）**换本地推理生态优先适配（对照同尺寸闭源模型也可卖硬件）；③ 与 **PAIR**（本地网络 AI 路由器，10-13 结束 beta）、RTX Spark 硬件捆绑。 |
| **可信度** | 中低——**截至 10-13 权重尚未公开**（10-15 释出），**全部性能主张为 NVIDIA 自评**（"比多数 dense 更快、比同级 MoE 更聪明"无基线命名）；2-bit 量化对任务质量的影响尚无可复现结果。 |
| **链接** | [blogs.nvidia.com RTX Spark](https://blogs.nvidia.com/blog/local-ai-rtx-spark-laptops-software-updates/)；[alfw.ai 分析](https://alfw.ai/article/nvidia-nemotron-bolt-74b-24gb/)；[developer.nvidia.com/nemotron](https://developer.nvidia.com/nemotron) |

---

## 四、Zhipu GLM-5.3-Highspeed（Zhipu / Z.ai，2026-10-12）

| 字段 | 内容 |
|------|------|
| **中文标题** | 智谱上线 GLM-5.3-Highspeed：峰值 490 tok/s、1M 上下文 |
| **英文标题** | Zhipu launches GLM-5.3-Highspeed on Zcode |
| **发布机构** | Zhipu AI（Z.ai） |
| **发布日期** | 2026-10-12（iiMedia 报道；Zcode v3.15.1 灰度） |
| **核心参数** | **峰值生成 490 tok/s**（前代 GLM-5.3-FlashX 约 200 tok/s）；**1M 上下文**；单次输出上限约 **128k token**；thinking 三档 `low / high / max`。 |
| **主要创新点** | 把 GLM-5.3 家族的**高速档**做到 2× 以上吞吐，强化长文输出效率；灰度放量于订阅用户。**注意**：第三方（OrcaRouter）当日核查确认 **GLM-5.4 / GLM-5.5 均为"名称/预测"，无 model card / 权重 / API id**，不应与本次 Highspeed 更新混淆。 |
| **可信度** | 中低——速度为**第三方测试口径**（iiMedia 转述），非 Z.ai 官方技术报告。 |
| **链接** | [cnboat.cn 报道](https://www.cnboat.com/news/show.php?itemid=1902)；[OrcaRouter GLM-5.4 核查](https://www.orcarouter.ai/blog/glm-5-4) |

---

## 五、其他候选（未达收录门槛 / 待确认）

| 候选 | 机构 | 日期 | 状态 |
|------|------|------|------|
| Liquid AI `LFM2.5-24B-A2B`（24B MoE / **2.45B active**、131K 上下文、多语言、reasoning-only，base + post-trained 权重上 HF；llama.cpp/MLX/vLLM/SGLang/ONNX 支持） | Liquid AI | 2026-10-13 | **非目标机构**；LFM2.5 家族收官款，作边缘 agent 参照 |
| ScaleDown CDM（Constrained Decoding Models：Classify / Extract / Summarize，**1M 多模态上下文**、$0.05/M input、输出免费，绕过逐 token 生成循环） | ScaleDown | 2026-10-13 | **非目标机构**；"决策/结构化执行"新类别，作信号记录 |
| Microsoft **Maia 300**（2nm 级、288GB HBM4、18TB/s、机架 96 加速器；称比主流 GPU 系统 **每 MW 多 40% token**——**未点名对照 GPU**；2027 起 multi-GW 部署） | Microsoft AI | 2026-10-12 | **基础设施（非模型卡）**；目标机构但非 tech report，作信号记录 |
| Alibaba **Qwen3.8-Omni-Flash**（text/image/audio/video 输入、text 输出、1M 上下文、audio 输入时价 −98%；Model Studio `qwen3.8-omni-flash`；blog 日期 2026-09-14） | Alibaba Qwen | 2026-10-13（API 可用） | 目标机构；**日期偏早 + 全自评 + 无可读价格**，列候选待核 |
| StepFun **Step 5 开放权重**（600B / 27B active、1M ctx、$1.00/$2.70；承诺 10-15 释出 BF16 权重；**截至 10-13 官方 HF 无 repo、license 缺失**；cache-hit 价 10-14 00:30 起 0.35→0.70 元） | StepFun | 2026-10-12/13 | 目标机构；**signal/tracking**，权重 10-15 前无法核，license 风险 |

---

## 19 家目标机构窗口内（2026-10-13 → 2026-10-14）复核

| 机构 | 窗口内新报告 / 系统卡 | 备注 |
|------|----------------------|------|
| OpenAI | 无（最近为 **10-07 GPT-6 Sol/Luna October update**，已见 10-13 期） | 无新系统卡；截图/更新归 10-07 |
| Anthropic | **有（★★）** | **self-replicating AI（weight-based replicator）**（§2，10-12 / 媒体 10-13）；distillation 防御见 10-13 期 |
| Google DeepMind | **有（★★★，frontier 卡面）** | **Gemini 4 Argon 全球 GA + Model Card**（§1，10-13）；Carbon 见 10-12 期 |
| Meta | 无（新报告） | Muse Wonder / CanonQ 见 10-13 期（10-12 发布） |
| Microsoft AI | **基础设施（非卡面）** | **Maia 300**（10-12，§5）；Microsoft-Decision-1 见 10-11 期 |
| xAI | 无 | Grok 4.7 见 10-11 期；Grok 4.6 往期 |
| Mistral | 无 | Mistral Large 4 "le Chonk" preview 见 10-06 起各期（权重月底） |
| DeepSeek | 无（新料） | V4.1-Flash 见 10-12 期 |
| Alibaba Qwen | **候选** | **Qwen3.8-Omni-Flash**（§5，API 10-13，blog 09-14）；Qwen-Image-2.1-Turbo 见 10-12 期 |
| ByteDance Seed | 无 | Phase Sensitivity 见 10-10 期 |
| Moonshot | 无 | 被 Anthropic 点名（10-13 期）；Kimi K3 往期 |
| Zhipu | **有（★）** | **GLM-5.3-Highspeed**（§4，10-12）；GLM-5.4/5.5 仅名称为传闻（不采信） |
| Tencent | 无 | — |
| Baidu | 无 | — |
| Amazon | 无 | Nova 2.5 Sonic GA 见 10-10 期 |
| NVIDIA | **有（★★，预告）** | **Nemotron 3.5 Bolt 74B-A9B / E4B**（§3，10-13 预告 / 10-15 释出） |
| Cohere | 无 | — |
| AI2 | 无 | Olmo Hybrid / Bolmo 见 10-12 期 |
| Perplexity | 无 | Decider / pplx-embed-v2-late 往期 |

---

## 本期不重复收录（交叉引用）

- **Meta Muse Wonder / Muse Wonder Full / Anthropic distillation 防御 / OpenAI textGrain / Meta CanonQ**：见 10-13 期 tech-report-digest。
- **Microsoft-Decision-1 / Liquid AI d1 / Perplexity Decider v1 / pplx-embed-v2-late**：见 10-11 期。
- **Ai2 Olmo Hybrid / Cloudflare Clef-omni / Qwen-Image-2.1-Turbo / Gemini 4 "Carbon" 内部泄露**：见 10-12 期。
- **NVIDIA Nemotron 3.5 Lightning / Nemotron 3 Ultra / ReplaySSM / IOI-IMO 配方 / DeepSeek V4.1-Flash / Kimi K3 / GLM-5.3 / Grok 4.7 / Nova 2**：往期已录。

---

## 口径与不确定性声明

- **窗口边界**：主窗口 **2026-10-13 → 2026-10-14**。Gemini 4 Argon（10-13）、Nemotron Bolt 预告（10-13）为窗口内一手事件；Anthropic self-replication（10-12，媒体 10-13）、Zhipu GLM-5.3-Highspeed（10-12）为**邻近补录**；均在写入前经 repo 级 grep 复核 wiki 首见（`self-replicating AI`、`Bolt 74B`、`Argon Model Card` 等）。
- **首次建档**：本期首次为 **Gemini 4 Argon model card（GA）**、**Anthropic weight-based replicator 研究**、**NVIDIA Nemotron 3.5 Bolt 74B-A9B**、**Zhipu GLM-5.3-Highspeed** 建立 wiki 记录（Argon 此前仅以 pilot / 内部代号形式出现）。
- **未独立复现**：Argon benchmark 为 Google 自评表（Vals Index 为第三方但由 Google 引用），部分基准无独立 harness 复现；Anthropic 复制实验为**高度简化的 upper bound**、无野外案例；Nemotron Bolt **权重 10-15 才公开、全为厂商声明**；GLM-5.3-Highspeed 速度来自第三方转述。
- **低可信 / 二手**：Maia 300 的"每 MW +40% token"**未点名对照 GPU**；Qwen3.8-Omni-Flash 时间戳早且价格不可读；Step 5 开放权重/license 截至 10-13 未落地。**GLM-5.4 / GLM-5.5 为名称/预测，无任何 model card，未采信为发布。**
- **厂商口径**：Argon 定价 intro（$2/$10）到 **2026-11-30** 后翻倍（$4/$20）；Nemotron Bolt 数字为 NVIDIA 自评；各 benchmark 表**不可跨厂商横向比较**。
- **语言**：本期沿用 tech-report-digest 系列既有约定（中文正文 + 英文技术术语），与 10-11/10-12/10-13 期保持一致。
