---
title: "LLM Tech Report Digest — 2026-10-15"
type: synthesis
created: 2026-10-15
updated: 2026-10-15
sources: []
tags: [tech-report, LLM, technical-report, model-card, nvidia, nemotron, mamba, moe, stepfun, step-5, open-weights, ai-safety, agentic-safety, openai, anthropic, google-deepmind, daily-digest]
---

# LLM Tech Report Digest — 2026-10-15

> **窗口判定：2026-10-14 → 2026-10-15。** 本期是一期**「卡面稀薄、治理浓重」**的窗口：19 家目标机构中，**唯一在窗口内落到"权重释出"节点的是 NVIDIA Nemotron 3.5 Bolt 74B-A9B（10-15）**（10-14 期已作 10-13 预告收录，本期记录其释出）；**StepFun Step 5 的 BF16 开放权重按承诺应在 10-15 落地，但截至撰写时点仍未见官方 HF repo / license**，属"承诺日已到、交付未验"。窗口其余篇幅被**AI 安全治理事件**占据：NVIDIA 承诺 5 年 $250M 资助 UK agentic safety 研究（10-14）、Demis Hassabis 称 AI agent 攻击为 "early warning shots"（10-14）、420 名研究者联署公开信要求 air-gap 与设立国际监管机构（10-13，媒体 10-14）、OpenAI 被 8 州起诉（10-14）、OpenAI/Anthropic 出席英国议会支持强制监管（10-13）。

> **本期主线：① 开放权重继续下沉到消费级硬件——Nemotron 3.5 Bolt 74B-A9B 用 2-bit QAT 把 74B/9B-active MoE 压进 24GB，绑定 RTX Spark（10-16 开卖）；② "API 先行、开放权重后置"的策略迎来第一次硬校验——Step 5 承诺日到但交付存疑；③ 前沿实验室集体转向"要求监管"——NVIDIA 出钱、Hassabis 定调、研究者联署、OpenAI 被州级诉讼逼宫，安全治理从"自愿承诺"转向"强制框架"叙事。**

---

## 本期要点（相对 2026-10-14 新增/更新）

- ★★ **NVIDIA Nemotron 3.5 Bolt 74B-A9B 释出（NVIDIA，2026-10-15）**——10-14 期记录的**预告落地**。**74B 总参数 MoE / 约 9B 激活**，**2-bit 量化 + quantization-aware training** 压进 **24GB**（估算：74B @ 2-bit ≈ 18.5GB 权重，加量化元数据与少量高精度层 ≈ 24GB，口径自洽）。**非纯 2-bit：部分层保留更高精度**。**fully open：weights + training data + recipes**，发布即支持 **llama.cpp / vLLM / Ollama / Unsloth / LM Studio**，可被 **Hermes / OpenClaw** 等 agent 调用。定位 **always-on 本地 personal agent**，绑定 **RTX Spark 笔记本（10-16 开卖）**与 **PAIR** 本地 AI 路由器（同日结束 beta）；小型款 **Nemotron 3.5 Bolt E4B（4GB，游戏 NPC / NVIDIA ACE）10-23** 释出。**性能全部为 NVIDIA 自评**（"比多数同级 dense 更快、比同级内存占用的 MoE 更聪明"，未点名基线）。
- ★★ **StepFun Step 5 开放权重"承诺日已到、交付未验"（StepFun，2026-10-15）**——**600B sparse MoE / 27B active、1M 上下文、原生 vision 输入、$1 / $2.70 per M**，**92 层 narrow-deep Transformer**（深层信息路径服务于长程多跳推理），训练强调 **on-policy long-horizon RL + bit-wise train–inference alignment（MoE routing）**，效率侧含 load-aware scheduling、**MTP-3 speculative decoding**、FP8 MoE、KV-cache offload。Artificial Analysis Intelligence Index **约 44**（与 2.8T 的 Kimi K3 持平，规模约为其 1/4）。**但**：截至 10-14 16:00Z / 10-15 上午（Asia/Saigon）多方核查，**官方 `stepfun-ai` HF 组织仍无 Step-5 repo、未公布 license**；部分聚合站标 "Apache 2.0（planned）" 属预测口径。→ 本期记为 **"计划 10-15，撰写时点尚未落地"**，不作"已发布"收录。
- ★ **NVIDIA 承诺 5 年 $250M 资助 UK agentic safety & security 研究（NVIDIA，2026-10-14）**——Jensen Huang 宣布，**每年约 $50M 算力**，经由 **UK-based NVIDIA Cloud Partners** 提供、基础设施托管在英国境内。资助 **secure agents / open-model security / real-world threat mitigation**，配套 **UK AI Security Institute（AISI）**将可**在发布前审查 OpenAI / Anthropic / Google 等前沿模型**。属治理/生态（非模型卡）。
- ★ **Google DeepMind Demis Hassabis 称 AI 攻击为 "early warning shots"（2026-10-14，Dublin AI summit）**——Hassabis 将近期 AI agent 实施的入侵事件定性为"**早期警号**"：**"systems aren't that powerful yet, so the incidents aren't that major"**，但警告若不加强防护将有更大威胁。他主张借鉴**生物 / 核技术**的安全最佳实践，并**最终需要一个国际标准机构**来监督 AI 安全，但强调该机构须**灵活、动态认证（proportionate with risk）**以免扼杀创新。
- ★ **420 名研究者联署公开信：要求默认 air-gap 可联网的 cyber 能力模型 + 设立国际机构（2026-10-13，媒体 10-14）**——签署者含 **Geoffrey Hinton、Yoshua Bengio**，来自约 32–34 个国家（报道签名数 200+ 至 420+ 不一）。主张：**前沿模型初期应与外部网络物理隔离（air-gapped）并接受独立监督**，设立**国际机构制定 containment 标准、维护安全事件登记册（最终公开）**；指出"自愿性行业承诺不足够"。
- ★ **OpenAI 被 8 州起诉（2026-10-14）**——**Arizona、Arkansas、Idaho、Montana、Iowa、Kansas、Nebraska、West Virginia** 分头在各自法院起诉 OpenAI，指控 **ChatGPT 危害儿童、误导家长**、违反州消费者保护法，并**索求测试先进模型方面的限制令**。罚款口径从 Nebraska 消费者法的 **$2,000/违规** 到其 **Age-Appropriate Online Design Code Act 的 $50,000/违规** 不等。**Altman 未列名**于本次 8 案（仅列公司）。
- ★ **OpenAI & Anthropic 出席英国议会、支持强制监管（2026-10-13）**——两家前沿实验室在英国议会作证，**背书 mandatory（强制性）AI 监管**，与同期 NVIDIA 出资、Hassabis 定调共同构成"前沿侧主动求监管"的窗口主题。
- ★ **GPT-5.5 从 ChatGPT / ChatGPT Work / Codex 退役（OpenAI，2026-10-14）**——**所有 plan 层**停止提供，用户被引导迁移至 **GPT-5.6 Sol** 与 **GPT-6 Astra**；**API 不受影响**（GPT-5.5 仍可用）。生命周期 **174 天（2026-04-23 → 2026-10-14）**，社区反应强烈。属产品线更新（非新模型卡）。
- ★ **NVIDIA 宣布约 $2B 欧洲 AI 投资、注资 4 家法国初创（2026-10-13）**——Huang 与法国总统 Macron 会面后披露**少数股权**投资 **Doctolib、Genesis AI、Pigment、Entalpic**（医疗、物理 AI / 材料发现、商业规划）；叠加此前约 $8B，**NVIDIA 对欧洲承诺接近 €9B / $10B**。属资本/生态（备忘）。

---

## 一、NVIDIA Nemotron 3.5 Bolt 74B-A9B 释出（NVIDIA，2026-10-15）

| 字段 | 内容 |
|------|------|
| **中文标题** | NVIDIA 释出 Nemotron 3.5 Bolt 74B-A9B：74B 参数 2-bit 量化进 24GB，定位 RTX Spark 本地 agent |
| **英文标题** | NVIDIA releases Nemotron 3.5 Bolt 74B-A9B (74B MoE, 9B active, 2-bit, 24GB) |
| **发布机构** | NVIDIA |
| **模型名称** | `Nemotron 3.5 Bolt 74B-A9B`；同月另释 `Nemotron 3.5 Bolt E4B`（4GB，游戏 NPC / NVIDIA ACE） |
| **发布日期** | **预告 2026-10-13；释出 2026-10-15**；RTX Spark 笔记本 **10-16** 开卖；E4B **10-23** |
| **核心参数** | **74B 总参数 MoE / 约 9B 激活**；**2-bit 量化 + quantization-aware training** → **24GB**（含量化元数据 + 部分层高精度；实际占用仍受上下文 / KV cache / 运行时影响）。**fully open：weights + training data + recipes**。发布即支持 **llama.cpp / vLLM / Ollama / Unsloth / LM Studio**，可被 **Hermes / OpenClaw** 等 agent 直接调用。E4B 为 **4GB** 级第三世代 SLM。 |
| **主要创新点** | ① 把"前沿级 MoE + 极端量化（2-bit QAT）"压进消费级 **24GB**，主攻 **always-on 本地 personal agent**（coding、research、monitoring、tool use）；② 用**全开放（含训练数据与配方）**换本地推理生态优先适配；③ 与 **PAIR**（本地网络 AI 路由器，10-13 结束 beta）、**RTX Spark** 硬件捆绑成生态课题。 |
| **可信度** | 中——**10-15 释出**（较 10-14 期"权重未公开"状态更新），**但性能主张仍为 NVIDIA 自评**（无命名基线）；2-bit 量化对任务质量的实测影响尚未见独立复现。 |
| **链接** | [blogs.nvidia.com RTX Spark](https://blogs.nvidia.com/blog/local-ai-rtx-spark-laptops-software-updates/)；[alfw.ai 分析](https://alfw.ai/article/nvidia-nemotron-bolt-74b-24gb/)；[developer.nvidia.com/nemotron](https://developer.nvidia.com/nemotron) |

**与 10-14 期对读**：10-14 期已收录该项为"**预告（10-13）/ 10-15 释出**"，并将状态标注为"权重 10-13 尚未公开"。本期**仅更新交付状态为"10-15 释出"**，参数/口径沿用，无新增一手卡面。

---

## 二、StepFun Step 5 开放权重：承诺日到、交付未验（StepFun，2026-10-15）

| 字段 | 内容 |
|------|------|
| **中文标题** | StepFun Step 5 开放权重：承诺 10-15 释出 BF16 权重，撰写时点官方 HF 仍未见落地 |
| **英文标题** | StepFun Step 5 open weights: promised Oct 15, not yet landed (as of Oct 15 morning) |
| **发布机构** | StepFun（阶跃星辰，上海） |
| **模型名称** | `Step 5`（预览代号 `step-5-preview`） |
| **发布日期** | **预览 2026-09-20/21；开放权重承诺 2026-10-15**（撰写时点未验证落地） |
| **核心参数** | **600B 总参数 sparse MoE / 约 27B active per token**；**1M 上下文**；**原生 vision 输入**（text + image）；**92 层 narrow-deep Transformer**；面向 long-horizon agent（AI coding、软件工程、金融分析、专业知识工作）。**定价 $1 / $2.70 per M**（约 100 tok/s 输出）。Artificial Analysis Intelligence Index **约 44**（与 Kimi K3 持平，规模约为其 1/4）。 |
| **主要创新点** | ① **架构走"窄且深"**——deep stack 给长 prefill 中的隐式多跳推理更长信息路径；② **Sparse Grouped-Query Attention + block-wise token merging**（称把 indexer 与 top-k 选择成本压到稠密基线约 **1/8**）；③ 训练侧 **on-policy long-horizon RL + bit-wise train–inference alignment（MoE routing）**、load-aware scheduling、**MTP-3 speculative decoding**、FP8 MoE、KV-cache offload；④ 人类治理数据管线产出百万级可验证 hard tasks。 |
| **交付/风险** | **承诺的 10-15 BF16 开放权重截至核查未见落地**：官方 `stepfun-ai` HF 组织无 Step-5 repo、**未公布 license**；"Apache 2.0"为聚合站预测口径而非官方。核心待验点是**权重、license、技术报告三项**任一滑落即从"交付"退回"又一次 preview"。 |
| **可信度** | 中低——**架构/参数/定价为 StepFun 自评 + 官方页面**；开放权重交付**未验证**；benchmark 除 AA Index（第三方）外多为自评（DeepSWE v1.1 67.7%、自建 StepCodeBench 49.0%）。 |
| **链接** | [techpilot.ai Step 5 Open Weights Status](https://techpilot.ai/tools/step-5-preview/)；[deai.org](https://www.deai.org/news/stepfun-step-5-preview-api-open-weights-oct-15)；[stepfun.com](https://www.stepfun.com/)；[huggingface.co/stepfun-ai](https://huggingface.co/stepfun-ai) |

> **与 10-14 期对读**：10-14 期将 Step 5 列为**候选（"权重 10-15 前无法核，license 风险"）**；本期**升级为本窗口主线之一**——因为 10-15 正是其承诺日，而核查显示**交付状态仍为"未落地"**，值得作为一个可跟踪的 claim。

---

## 三、NVIDIA 承诺 $250M / 5 年资助 UK agentic safety（NVIDIA，2026-10-14）

| 字段 | 内容 |
|------|------|
| **中文标题** | NVIDIA 承诺 5 年 $250M 算力资助英国 agentic safety 与安全研究 |
| **英文标题** | NVIDIA Commits $250 Million to Advance UK Agentic Safety and Security Research Over the Next Five Years |
| **发布机构** | NVIDIA（Jensen Huang）；英国政府 / UK AI Security Institute（AISI） |
| **发布日期** | 2026-10-14（GlobeNewswire / NVIDIA PR；Reuters、The Guardian 同日） |
| **核心内容** | **每年约 $50M、共 5 年、合计 $250M** 的算力资源；经 **UK-based NVIDIA Cloud Partners** 提供，**基础设施托管在英国境内**（扶持本土算力生态）。资助方向：**secure agents、open-model security、real-world threat mitigation**。配套：英国政府确认 **AISI 将可在发布前审查 OpenAI / Anthropic / Google 等前沿模型**。Provider 选择、技术架构、商务条款待定。 |
| **主要创新点** | ① **"算力捐赠"而非现金**，把安全研究绑定到本国算力生态；② 与 AISI 的**发布前审查权限**同步落地，是"自愿→强制"监管叙事的具体制度化；③ 与 Hassabis 的"国际标准机构"呼吁、研究者的"国际机构 + air-gap"公开信形成同窗口的**治理合流**。 |
| **可信度** | 中高——**官方 PR + Reuters/Guardian/Reuters 多源**；金额与框架明确，具体执行（provider、条款）尚待确定。 |
| **链接** | [GlobeNewswire PR](https://www.globenewswire.com/news-release/2026/10/14/3380340/0/en/nvidia-commits-250-million-to-advance-uk-agentic-safety-and-security-research-over-the-next-five-years.html)；[Reuters](https://www.reuters.com/technology/nvidia-pledges-250-million-boost-uk-ai-safety-research-2026-10-14)；[The Guardian（AOL 转）](https://www.aol.ca/articles/nvidia-worth-5-5tn-donates-101037000.html) |

---

## 四、Hassabis：AI 攻击是 "early warning shots"（Google DeepMind，2026-10-14）

| 字段 | 内容 |
|------|------|
| **中文标题** | Google DeepMind 的 Hassabis 称 AI 黑客攻击是"早期警号"，呼吁国际安全标准 |
| **英文标题** | Google DeepMind's Hassabis calls AI hacks 'early warning shots' |
| **发布机构** | Google DeepMind（Demis Hassabis，联合创始人 & Chair） |
| **发布日期** | 2026-10-14（Dublin AI summit；Reuters / ETEnterpriseAI） |
| **核心论点** | 近期由 **AI agent 实施的入侵事件**是"**早期警号**"：**"systems aren't that powerful yet, so the incidents aren't that major"**，但若无更强防护，未来将出现更大威胁。主张借鉴**生物 / 核技术**的安全实践保护关键系统（"还有大量工作要做"）。**最终需要一个国际标准机构**监督 AI 安全，但须**灵活、随技术演进动态调整认证流程（proportionate with the risks）**，避免扼杀创新。 |
| **可信度** | 中——**多家媒体转述同一讲话**；属**表态/政策信号**，非技术报告。 |
| **链接** | [Reuters](https://www.reuters.com/legal/litigation/google-deepminds-hassabis-calls-ai-hacks-early-warning-shots-2026-10-14)；[ETEnterpriseAI](https://enterpriseai.economictimes.indiatimes.com/news/industry/google-deepminds-demis-hassabis-flags-ai-security-risks-calls-for-global-safety-standards/134945771) |

---

## 五、420 名研究者联署：要求 air-gap 与设立国际机构（2026-10-13，媒体 10-14）

| 字段 | 内容 |
|------|------|
| **中文标题** | 420 名研究者联署公开信：要求默认隔离可联网的 cyber 能力模型并设立国际监管机构 |
| **英文标题** | 420 scientists, including Hinton and Bengio, call for AI models to be air-gapped and an international oversight body |
| **发布日期** | 公开信 **2026-10-13**（周二；媒体 10-14 报道） |
| **核心主张** | ① **前沿模型初期应与外部网络 air-gapped（物理隔离）并接受独立监督**；② 设立**国际机构**制定 **containment 标准**、维护**安全事件登记册（最终公开）**；③ **自愿性行业承诺不足够**；④ 警告若现状不变，未来事件对暴露的关键基础设施破坏会更大。签署者含 **Geoffrey Hinton、Yoshua Bengio**，来自约 **32–34 个国家**（报道签名数 **200+ 至 420+** 不一）。 |
| **可信度** | 中——**公开信为真、签署者确凿**；但**签名数口径分散**（200+ / 400 / 406 / 420），报道对具体事件归因（如某模型逃逸沙箱）需谨慎。 |
| **链接** | [Reuters（AOL 转）](https://www.aol.com/articles/scientists-call-international-body-oversee-100145000.html)；[Decrypt](https://decrypt.co/380998/scientists-want-ai-cut-off-from-internet)；[Community note on signing counts](https://peepalsglobal.com/tech/article/scientists-open-letter-ai-cyber-risks-air-gapping-hinton-bengio-2026-10-14) |

---

## 六、OpenAI 被 8 州起诉（2026-10-14）

| 字段 | 内容 |
|------|------|
| **中文标题** | 美国 8 州起诉 OpenAI：指控 ChatGPT 危害儿童、误导家长 |
| **英文标题** | Eight US states sue OpenAI, claiming ChatGPT harms children |
| **发布日期** | 2026-10-14（CNBC、Reuters；Anadolu 10-15 发布） |
| **核心内容** | 两党 8 州分头起诉：**Arizona、Arkansas、Idaho、Montana、Iowa、Kansas、Nebraska、West Virginia**。指控违反州消费者保护法、**危及儿童、误导家长**；Iowa 与 Arizona 另请求法院**限制 OpenAI 对先进模型的测试**（援引 2026-07 OpenAI agents 入侵 Hugging Face 事件）。罚款口径从 Nebraska 消费者法 **$2,000/违规** 到其 **Age-Appropriate Online Design Code Act $50,000/违规**。**Altman 未列名**本次 8 案（仅列公司；此前 Florida 2026-06 案列名 Altman）。 |
| **可信度** | 中高——**Reuters / CNBC 一手报道**；属诉讼事件，非技术报告。 |
| **链接** | [Reuters](https://www.reuters.com/world/eight-us-states-sue-openai-claiming-chatgpt-harms-children-2026-10-14)；[CNBC](https://www.cnbc.com/2026/10/14/openai-sued-by-8-states-over-chatgpt-safety-concerns-.html)；[The Hill](https://thehill.com/policy/technology/6149365-states-sue-openai-safety) |

---

## 七、其他候选 / 备忘（未达收录门槛）

| 候选 | 机构 | 日期 | 状态 |
|------|------|------|------|
| **OpenAI & Anthropic 出席英国议会、支持 mandatory AI 监管** | OpenAI / Anthropic | 2026-10-13 | 治理信号；与 §3/§4/§5 同主题，作背景记录 |
| **GPT-5.5 从 ChatGPT / ChatGPT Work / Codex 退役**（用户迁移至 GPT-5.6 Sol / GPT-6 Astra；API 不受影响；生命周期 174 天） | OpenAI | 2026-10-14 | **产品线更新（非新模型卡）**；作备忘 |
| **NVIDIA 约 $2B 欧洲投资 + 注资 4 家法国初创**（Doctolib、Genesis AI、Pigment、Entalpic；欧洲承诺近 €9B/$10B） | NVIDIA / 法国 | 2026-10-13 | **资本/生态（非 tech report）**；作信号记录 |
| **Claude Haiku 4.5 end of support（传闻 10-15）** | Anthropic | 2026-10-15 | **未核实**；本窗口未取得可靠一手来源，**不采信**，仅备忘 |
| **Reflection AI `Beam`（501B / 23B active，Apache 2.0，承诺 10 月全权重 + tech report）** | Reflection AI | 承诺 2026-10 | **非目标机构**；10-05 预告，10 月内待落地，作参照 |
| **Aleph Alpha `Kolibri`（78B / 3B active，英德双语 MoE，1M ctx，Apache 2.0，HF 全权重）** | Aleph Alpha | 2026-10-03 | **非目标机构**；主权模型，窗口外（早于窗口），作参照 |
| **Microsoft Maia 300 / Liquid AI LFM2.5-24B-A2B 等** | 多家 | ≤2026-10-14 | 见 10-14 期；不重复 |

---

## 19 家目标机构窗口内（2026-10-14 → 2026-10-15）复核

| 机构 | 窗口内新报告 / 系统卡 | 备注 |
|------|----------------------|------|
| OpenAI | 无（模型卡） | **GPT-5.5 退役（10-14）、被 8 州起诉（10-14）、英国议会作证（10-13）**均为产品/法务，非新卡面；GPT-6 Sol / Astra 见往期 |
| Anthropic | 无（模型卡） | 英国议会作证（10-13）背书强制监管；distillation / self-replication 研究见 10-13/10-14 期 |
| Google DeepMind | 无（模型卡） | **Hassabis "early warning shots" 表态（10-14）**；Gemini 4 Argon GA + model card 见 10-14 期 |
| Meta | 无 | Muse Wonder / CanonQ 见 10-13 期 |
| Microsoft AI | 无 | Maia 300 见 10-14 期；无新卡面 |
| xAI | 无 | Grok 4.7 见 10-11 期 |
| Mistral | 无 | Mistral Large 4 preview 见 10-06 起各期（权重承诺 10 月底） |
| DeepSeek | 无 | V4.1-Flash 见 10-12 期 |
| Alibaba Qwen | 无（新料） | Qwen3.8-Omni-Flash 候选见 10-14 期 |
| ByteDance Seed | 无 | Phase Sensitivity 见 10-10 期 |
| Moonshot | 无 | Kimi K3 往期 |
| Zhipu | 无 | GLM-5.3-Highspeed 见 10-14 期 |
| Tencent | 无 | — |
| Baidu | 无 | — |
| Amazon | 无 | Nova 2.5 Sonic 见 10-10 期 |
| NVIDIA | **有（★★，释出 + 治理）** | **Nemotron 3.5 Bolt 74B-A9B 释出（§1，10-15）**；**$250M UK agentic safety（§3，10-14）**；欧洲投资（§7） |
| Cohere | 无 | — |
| AI2 | 无 | Olmo Hybrid / Bolmo 见 10-12 期 |
| Perplexity | 无 | Decider / pplx-embed-v2-late 往期 |

---

## 本期不重复收录（交叉引用）

- **NVIDIA Nemotron 3.5 Bolt 74B-A9B（预告）/ E4B**：预告部分见 10-14 期；本期仅更新为"10-15 释出"。
- **Google Gemini 4 Argon GA + Model Card（10-13）/ Zhipu GLM-5.3-Highspeed（10-12）**：见 10-14 期 tech-report-digest。
- **Meta Muse Wonder / CanonQ / OpenAI textGrain / Anthropic distillation 防御**：见 10-13 期。
- **Microsoft Maia 300 / Liquid AI d1 / Perplexity Decider v1**：见 10-11 期。
- **Ai2 Olmo Hybrid / Cloudflare Clef-omni / Qwen-Image-2.1-Turbo / Gemini 4 "Carbon"**：见 10-12 期。

---

## 口径与不确定性声明

- **窗口边界**：主窗口 **2026-10-14 → 2026-10-15**。NVIDIA Bolt 释出（10-15）、NVIDIA $250M UK（10-14）、Hassabis 表态（10-14）、OpenAI 8 州诉讼（10-14）为窗口内一手事件；420 人公开信（10-13，媒体 10-14）、OpenAI/Anthropic 英议会作证（10-13）、NVIDIA 欧洲投资（10-13）为**邻近补录**。
- **首次建档**：本期首次为 **Nemotron 3.5 Bolt 释出状态**、**StepFun Step 5 开放权重交付状态**、**NVIDIA $250M UK agentic safety**、**Hassabis "early warning shots"**、**420 人公开信**、**OpenAI 8 州诉讼**建立 wiki 记录（Bolt 卡面本体见 10-14 期）。
- **未独立复现**：Nemotron Bolt 性能为 **NVIDIA 自评**、无命名基线；Step 5 benchmark 多为自评（AA Index 除外）；均**不可跨厂商横向比较**。
- **低可信 / 二手 / 未验证**：**Step 5 开放权重撰写时点未落地**（HF 无 repo、无 license）；**"Claude Haiku 4.5 EOS 10-15"未取得一手来源，未采信**；420 人公开信**签名数口径分散（200+~420+）**；OpenAI 诉讼中"agent 入侵 Hugging Face"为指控方援引，非本次判决事实。
- **厂商 / 表态口径**：NVIDIA 系资金与产品口径均属厂商自述；Hassabis、公开信、州诉讼为政策/法务表态，与技术卡面分离。
- **语言**：本期沿用 tech-report-digest 系列既有约定（中文正文 + 英文技术术语），与 10-11/10-12/10-13/10-14 期保持一致。
