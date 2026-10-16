---
title: "LLM Tech Report Digest — 2026-10-16"
type: synthesis
created: 2026-10-16
updated: 2026-10-16
sources: []
tags: [tech-report, LLM, technical-report, model-card, open-weights, meta, muse-spark-open, nvidia, nemotron, mamba, moe, vision-language, stepfun, step-5, ant-group, ling-3.1-flash, long-context, daily-digest]
---

# LLM Tech Report Digest — 2026-10-16

> **窗口判定：2026-10-15 → 2026-10-16。** 本期是一期**「开放权重超级周」**：在不到 24 小时内，**四家机构同时把可观规模的 open-weight 模型落到可下载状态**——**Meta Muse Spark Open（816B/42B，10-15）**、**NVIDIA Nemotron 3.5 Super VL 120B-A12B（10-15）**、**StepFun Step 5 Preview 开放权重正式落地（10-15，兑现 10-15 承诺日）**、**蚂蚁集团 inclusionAI Ling-3.1-flash（560B/25B，10-14/15）**。窗口内**没有**目标机构新发 arXiv technical report——本轮交付以**模型卡 / technical blog**为主（Muse Spark Open 另附 evaluation methodology report；Nemotron Super VL 附 technical blog + Nemotron 实验室技术页）。

> **本期主线：① 开放权重从"中国实验室主导"扩展到美国一线——Meta 用 816B natively-multimodal MoE 重新入场开放权重，并首次把"消费级桌面可跑"（2× Apple M5 Ultra Mac Studio）当作卖点；② NVIDIA 用 Mamba-2×MoE×Attention 混合架构 + NVFP4 把 VL agent 做到"美系开放权重智能榜首"（AA Index 26.5）；③ 承诺兑现——StepFun 按期释出 Step 5 Preview 全权重，把 10-15 期"承诺日到、交付未验"的悬案结清；④ 开放权重授权继续分叉——Meta（Muse Model License 限商用条款）、NVIDIA（OpenMDW-1.1）、StepFun（StepFun Model License 1.0 三重商用闸门）、蚂蚁（MIT）四种许可在同一周并置。**

---

## 本期要点（相对 2026-10-15 新增/更新）

- ★★★ **Meta Muse Spark Open 释出（Meta Superintelligence Labs，2026-10-15）**——Meta 重新入场开放权重：**816B 总参数 / 42B 激活的 MoE Transformer + Perception Encoder**，**natively multimodal**（text / image / document / audio / audio-video 输入 → text 输出），**1M 上下文**（max output 131k，知识截止 **2026-01-04**），reasoning + tool calling。**权重 BF16 + NVFP4 两种**上 Hugging Face（`meta-models/Muse-Spark-Open-816B-A42B`，gated），许可为 **Muse Model License（含 Muse Spark Usage Policy，限商用条款）**。**首次把"消费级桌面可跑"做成卖点**——经 Apple MLX 在**两台 M5 Ultra Mac Studio（各 512GB 统一内存、1.2 TB/s 带宽）**上整模型本地推理；SGLang 内嵌自调优 **Helion GPU kernel**（NVIDIA/AMD 上 1.03–3.95× kernel 加速）。自评 **Artificial Analysis Intelligence Index 39**、GPQA Diamond 89.0、Terminal-Bench 2.1 76.4、DeepSWE 1.1 60。托管方含 Baseten / Fireworks / Groq / Modal / Nebius / OpenRouter / Together；权重另上 Amazon SageMaker、Google Cloud Model Garden、Microsoft Foundry。
- ★★★ **NVIDIA Nemotron 3.5 Super VL 120B-A12B 释出（NVIDIA，2026-10-15）**——**开放 120B / 12B 激活的多模态 VLM**：**混合 Mamba-2 + MoE + Attention 架构**（每 MoE 层 **512 routed experts**）+ **C-RADIO 视觉编码器** + VL connector；**1M 上下文**，**MTP 原生 speculative decoding**，可配置 reasoning（`enable_thinking`）。**训练口径：约 26T tokens（预训练 + 续训）→ 约 3.8M 样本后训练 + 数十个环境的 RL**。许可 **OpenMDW-1.1**，释出 **BF16 + NVFP4（quantization-aware distillation）**。第三方 **Artificial Analysis 测其 AA Intelligence Index ≈ 26.5，称其为"美系开放权重最高分"**，100k prompt 下约 **630 tok/s**，每任务输出 token 约为前代 Nemotron 3 Super 的 **40%（≈60% 更省）**。协作方为 **Nemotron Coalition**；后训练定制方含 Scale AI、AI21、CrowdStrike、Perplexity、Salesforce 等。
- ★★ **StepFun Step 5 Preview 开放权重正式落地（StepFun，2026-10-15）**——**10-15 期"承诺日已到、交付未验"结清**：北京时间 10-15 凌晨，**FP8 / BF16 / NVFP4 三份权重**在 Hugging Face（`stepfun-ai/Step-5-Preview`、`-BF16`、`-NVFP4`）与 ModelScope 同时公开（含 MTP 与 vision 文件），并放出 technical blog。**600B 总参数 / 27B 激活 sparse MoE、1M 上下文、原生 vision 输入**。**新许可 StepFun Model License 1.0**：对多数用户近似 Apache 2.0，但设**三重商用闸门**——设备厂商（手机/汽车/眼镜/机器人/智能家居）需另签、MaaS 年收入 >$20M 需另签、超大产品需展示 "Powered by StepFun AI"。官方分数：**StepCodeBench 49.0%、FrontierFinance 66.4%**；AA Intelligence Index 约 44。
- ★★ **蚂蚁集团 inclusionAI Ling-3.1-flash 开放权重（Ant Group，2026-10-14/15，邻近机构）**——**560B 总参数 / 25B 激活的 hybrid-linear 混合推理 MoE**：**63 层 KDA（Kimi-style Delta Attention 线性注意力）+ 9 层 Gated MLA（7:1）**、**1M 上下文**、8 routed + 1 shared experts，**MIT 许可**，权重上 Hugging Face / ModelScope。09-30 以 256K 预览 API 亮相，10-14 结束免费试用后**解锁 1M 上下文并释出全权重**。**Ant Group 不属本期目标机构清单**，但因同窗口、规模相当（对标 Step 5 / Qwen），作**邻近开放权重**全条目记录。
- ★ **Anthropic：给 METR 员工级模型访问权限（Anthropic，2026-10-15）**——Anthropic 宣布**授予 METR 类似员工的访问权限**用于 frontier 模型评估，并与 SecureBio、Accenture 合作、与 Hugging Face 洽谈评估事宜。属**治理/评估生态**（非模型卡）。
- ★ **Anthropic：AI worms 可经智能设备扩散（Anthropic，2026-10-15）**——安全研究博文延续 10-12 的 weight-based replicator 主题：称小模型可能"数月内"自复制到智能烤箱/电视/摄像头，**大模型已能做端到端复制**、无中心关停点。属安全研究（非模型卡）。

---

## 一、Meta Muse Spark Open（Meta Superintelligence Labs，2026-10-15）

| 字段 | 内容 |
|------|------|
| **中文标题** | Meta 释出 Muse Spark Open：816B/42B 原生多模态开放权重 MoE，首次可在双 Mac Studio 上本地跑 |
| **英文标题** | Introducing Muse Spark Open, The Most Capable US Open-Weight Model to Date |
| **发布机构** | Meta（Meta Superintelligence Labs, MSL；模型卡署名 Meta Platforms, Inc. / Meta Platforms Ireland Ltd.） |
| **模型名称** | `Muse-Spark-Open-816B-A42B`（BF16）；`Muse-Spark-Open-816B-A42B-NVFP4`（量化版） |
| **发布日期** | 2026-10-15 |
| **核心参数** | **816B 总参数 / 42B 激活**；**Mixture-of-Experts Transformer + Perception Encoder**；**natively multimodal**（输入 text / image / document / audio / audio-video，输出 text）；**1M 上下文**，**max output 131k**，**知识截止 2026-01-04**；reasoning + tool calling；**许可 Muse Model License**（含 Muse Spark Usage Policy，限商用条款，gated）；权重 **BF16 + NVFP4**；MoE 采用**自调优 Helion GPU kernel**（SGLang 内，NVIDIA/AMD 1.03–3.95× kernel 加速，AMD MI350 端到端 +3%）。 |
| **主要创新点** | ① **Meta 重新入场开放权重**，且一端到底覆盖"桌面本地"——经 **Apple MLX** 在**两台 M5 Ultra Mac Studio**（各 512GB 统一内存、1.2 TB/s 带宽）上整模型推理，"两台 Mac Studio 像一台 1TB 统一内存超算"；② **原生多模态 + reasoning** 的开放权重旗舰，面向 coding / long-horizon agentic；③ **额外的 safety post-training**（因开放权重而加，配合 Meta Superintelligence Scaling Framework 评估）；④ 在 SGLang 中集成**自调优 Helion kernel**，把"开放模型 + 推理栈协同优化"作为交付的一部分。 |
| **关键 benchmark（模型卡，自评）** | **AA Intelligence Index 39**（同表对照：Inkling 26 / Nemotron 3 Ultra 23 / Mistral Large 4 38 / Qwen3.8-2.4T-A95B 40 / GLM 5.3 45 / Kimi K3 44）；**GPQA Diamond 89.0**；**HLE 61 / HLE-Diamond 26.1**；**Terminal-Bench 2.1（Terminus 2 agent）76.4**（Beam 80.1 / Qwen3.8-Max 82.0 / GLM 5.3 83.9 / Kimi K3 85.0）；**DeepSWE 1.1 60**；SWE-Atlas-QnA 58；**MCP Atlas 89.2**；**OSWorld-Verified 80.4**；Toolathlon-Verified 72.8；JobBench 61.8；GDPval-AA 1401 Elo；AA-Omniscience 25；SciCode 58.5；ZeroBench（w/tools）50.0；BabyVision（w/tools）80.2；Video-MME 61.5。 |
| **交付/生态** | 权重：Hugging Face、Amazon SageMaker AI、Google Cloud Model Garden、Microsoft Foundry Models；托管推理：Baseten、Fireworks AI、Groq、Modal、Nebius、OpenRouter、Together AI；推理引擎：SGLang、vLLM、TensorRT-LLM、HF Transformers、Apple MLX、llama.cpp、Unsloth（AMD / Apple / Intel / NVIDIA 优化）。微调走 PyTorch TorchTitan。 |
| **可信度** | 中——**官方 model card + 自评 benchmark 表**（模型卡自带对照表，含竞品同基准分数）；AA Intelligence Index 为第三方口径但由 Meta 引用。**⚠️ 与 NVIDIA 同日"美系开放权重榜首"主张冲突**（见下方对读）。 |
| **链接** | [research.meta.ai/blog/muse-spark-open](https://research.meta.ai/blog/muse-spark-open)；[Hugging Face 模型卡](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)；[SageMaker blog](https://aws.amazon.com/blogs/machine-learning/metas-muse-spark-open-now-available-in-amazon-sagemaker-jumpstart/)；[9to5Mac](https://9to5mac.com/2026/10/15/meta-launches-new-muse-spark-open-model-optimized-to-run-on-mac-studio/) |

> **与 10-12/10-13 期对读**：10-12/10-13 期记录的是 **Meta Muse Wonder / Muse Wonder Full（10-12，闭源 frontier，AAII 52/56）**；**Muse Spark Open 是同日线的"开放权重"分支**，命名沿用 Muse Spark（1.x）系列而非 Wonder。**不要把"Wonder 闭源 frontier"与"Spark Open 开放权重"混为一谈**。
>
> ⚠️ **CONTRADICTION（口径）**：同一窗口内，**NVIDIA 与 Meta 均自称"美系开放权重最强者"**——Artificial Analysis 10-15 文章称 **Nemotron 3.5 Super VL（AA Index 26.5）为"leading US open weight model"**，而 Meta 称 Muse Spark Open 为 "most capable US open-weight model to date"（模型卡报 AA Index 39）。两者 **AA Index 数值口径不一致（26.5 vs 39）**，疑因指数版本 / effort 设置 / 自报口径差异；**不宜直接比较**，需以 Artificial Analysis 官方榜为准复核。

---

## 二、NVIDIA Nemotron 3.5 Super VL 120B-A12B（NVIDIA，2026-10-15）

| 字段 | 内容 |
|------|------|
| **中文标题** | NVIDIA 释出 Nemotron 3.5 Super VL：120B/12B 混合 Mamba×MoE×Attention 多模态开放权重 |
| **英文标题** | NVIDIA Expands Nemotron Family With Highest Efficiency Super VL and Bolt Models |
| **发布机构** | NVIDIA（Nemotron Coalition 协作） |
| **模型名称** | `NVIDIA-Nemotron-3.5-Super-VL-120B-A12B`（BF16）；`...-NVFP4`（量化） |
| **发布日期** | 2026-10-15（Hugging Face / Build.NVIDIA.com 同日） |
| **核心参数** | **120B 总参数 / 12B 激活**；**混合（interleaved）Mamba-2 + Mixture-of-Experts + Attention**，每 MoE 层 **512 routed experts**；**C-RADIO 视觉编码器** + vision-language connector；**1M 上下文**；**MTP（Multi-Token Prediction）原生 speculative decoding**；推理可开关（`enable_thinking`）；语言 EN/FR/DE/IT/JA/ES/ZH；许可 **OpenMDW-1.1**；**BF16 + NVFP4（由 BF16 做 quantization-aware distillation）**。训练：**约 26T tokens（预训练 + 续训）**，后训练 **约 3.8M 样本 + 数十个环境的 RL**。 |
| **主要创新点** | ① **混合序列架构工程化落地**——Mamba-2（线性）+ MoE + Attention 交错，配合 MTP 投机解码，把"高吞吐 agentic"作为第一目标（官方称比同类快最高 **5×**）；② **NVFP4 近乎无损**——AA 测其 NVFP4 与 BF16 在 Intelligence Index 上差 **0.1 分**、任一子项波动 ≤2.6 分；③ **开放（weights + datasets + training recipes）**，强调企业可 post-train、on-prem 部署、数据驻留；④ 面向 agent 的**视觉文档理解**（OCR / 表格 / 图表 / PDF / 网页）；⑤ Nemotron 家族分层（Lightning 高吞吐 / Ultra 硬推理 / Super VL 多模态 agent / Bolt 边缘）。 |
| **关键 benchmark（NVIDIA 自评 + AA 第三方）** | **AA Intelligence Index ≈ 26.5（第三方，称美系开放权重第一）**，100k prompt 下约 **630 tok/s**（AA 测得，pre-release DeepInfra NVFP4 端点），每任务输出 token ≈46k（前代 Nemotron 3 Super 114k 的 ~40%）。NVIDIA 卡面（BF16 / NVFP4）：**GPQA-Diamond 89.52 / 89.90**；HLE（text-only）31.79 / 31.44；MMLU-ProX 76.91 / 73.76；AA-Omniscience accuracy 26.20 / 25.86、hallucination 30.0 / 27.7、index 4.03 / 5.3；APEX shortlist 88.36 / 89.36。 |
| **可信度** | 中高——**官方 blog + 模型卡 + 第三方 AA 测量**；AA Index 与吞吐为第三方（AA / DeepInfra），但 NVIDIA 卡面 benchmark 多为**自评**；NVFP4 近无损为 AA 口径。 |
| **链接** | [blogs.nvidia.com/nemotron-3-5-super-vl](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl)；[Build.NVIDIA.com 模型页](https://build.nvidia.com/nvidia/nemotron-3.5-super-vl-120b-a12b)；[Artificial Analysis 文章](https://artificialanalysis.ai/zh/articles/nemotron-3-5-super-and-bolt)；[developer.nvidia.com technical blog](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/) |

> **与 10-15 期对读**：10-15 期已收录 **Nemotron 3.5 Bolt 74B-A9B 释出（10-15）**；本期**新增其同批发布的旗舰 Super VL（10-15）**。**Bolt 74B-A9B / E4B 4GB**（E4B 10-23 释出）见 10-15 期，本期不重复，仅确认 NVIDIA 官方 blog 把三者打包为"数据中心→桌面→边缘"分层。

---

## 三、StepFun Step 5 Preview 开放权重正式落地（StepFun，2026-10-15）

| 字段 | 内容 |
|------|------|
| **中文标题** | StepFun 按期释出 Step 5 Preview 全权重：600B/27B sparse MoE，FP8/BF16/NVFP4 齐发 |
| **英文标题** | Step 5 Preview is now open weights (StepFun) |
| **发布机构** | StepFun（阶跃星辰，上海） |
| **模型名称** | `stepfun-ai/Step-5-Preview`（FP8）、`Step-5-Preview-BF16`、`Step-5-Preview-NVFP4` |
| **发布日期** | **承诺 2026-10-15，实释 2026-10-15（北京时间凌晨，约 01:30 UTC 前 repo 转公开）** |
| **核心参数** | **600B 总参数 / 27B 激活 sparse MoE**；**1M 上下文**（输入+输出合计，max output 亦至 1M）；**原生 text + image + video 输入 → text 输出**；面向 long-horizon agentic（coding、软件工程、金融、知识工作）。**权重 FP8 / BF16 / NVFP4** 上 Hugging Face + ModelScope + GitHub（`stepfun-ai/Step-5...`），含 MTP 与 vision 文件；部署配方覆盖 vLLM / SGLang / Transformers。API 价 **$1.00 / $2.70 per M**。推荐采样 temp=1.0 / top_p=0.95 / top_k=0。 |
| **主要创新点** | ① **"承诺即交付"**——在预览 API 上线（09-20）不足一个月内落地 600B 级全权重；② **三份量化权重并行**（FP8 主打、BF16 精调、NVFP4 面向 Blackwell），是少数同时覆盖这三种精度的开放旗舰；③ **新许可 StepFun Model License 1.0**——大体近 Apache 2.0，但设**三重商用闸门**（设备厂商 / MaaS 年收入 >$20M / 超大产品署名 "Powered by StepFun AI"）；含**蒸馏条款**（呼应 10-12 Anthropic distillation 争议）；④ 为国内开放 agent 模型中规模最大者之一（次日/同周对标蚂蚁 560B Ling-3.1-flash）。 |
| **关键 benchmark（官方自评）** | **StepCodeBench 49.0%**；**FrontierFinance 66.4%**；**AA Intelligence Index 约 44**（与 2.8T 的 Kimi K3 持平，规模约为其 1/4）；DeepSWE v1.1 67.7%（早前口径）；GDPval-AA v2.1（引用 Artificial Analysis 2026-09-20 数据）。评测用 High reasoning 设置。 |
| **可信度** | 中——**权重交付已实证**（repo 公开、三精度齐发、license 明确）；benchmark 多为**自评**（AA Index 为第三方）；stepfun-ai 组织域名早期聚合站曾标 "Apache 2.0（planned）"，实际为 **StepFun Model License 1.0**（非 Apache）。 |
| **链接** | [Hugging Face Step-5-Preview](https://huggingface.co/stepfun-ai/Step-5-Preview)；[X @StepFun_ai 公告](https://x.com/StepFun_ai/status/2110717330657616092)；[postcutoff 交付核查](https://postcutoff.com/e/2026-10-15-stepfun-step-5-preview-open-weights/)；[stepfun.com/step-5-preview](https://www.stepfun.com/step-5-preview) |

> **与 10-14/10-15 期对读**：10-14 期列为**候选（"权重 10-15 前无法核，license 风险"）**；10-15 期升级为主线并记"**承诺日已到、交付未验**"（HF 无 repo、无 license）。**本期结清：10-15 权重落地、license（StepFun Model License 1.0）明确**——由"待验"转为"已交付"，是本轮"开放权重超级周"的关键闭环。

---

## 四、蚂蚁集团 inclusionAI Ling-3.1-flash 开放权重（Ant Group，2026-10-14/15，邻近机构）

| 字段 | 内容 |
|------|------|
| **中文标题** | 蚂蚁集团释出 Ling-3.1-flash 全权重：560B/25B 混合线性 MoE，MIT 许可 |
| **英文标题** | Ant Group open-sources Ling-3.1-flash (560B MoE, MIT) |
| **发布机构** | Ant Group（蚂蚁集团）inclusionAI 团队 |
| **模型名称** | `inclusionAI/Ling-3.1-flash` |
| **发布日期** | **预览 2026-09-30；结束免费试用并释出全权重 2026-10-14/15** |
| **核心参数** | **560B 总参数 / 25B 激活**（8 routed + 1 shared experts）；**hybrid-linear MoE**：**63 层 KDA（线性注意力）+ 9 层 Gated MLA（7:1）**；**1M 上下文**（试用期 256K，10-14 后解锁 1M）；**MIT 许可**；权重上 Hugging Face / ModelScope；定位 agent / search / office / 专门应用。 |
| **主要创新点** | ① 用 **KDA 线性注意力 + Gated MLA 的 7:1 混合**把 1M 长上下文的内存从二次降到可控（同类思路见 Kimi Linear / KDA 线）；② **MIT 全开放**（无区域 / 商用限制），在"中国开放模型授权分叉"背景下属最宽松一档；③ 规模约为前代 Ling-3.0-flash（124B/5.1B）的 **4.5×**。 |
| **关键 benchmark** | AA Intelligence Index **41.1**（第三方）；AutomationBench-AA 61.7%；AA-Briefcase 1400 Elo；GDPval-AA v2 1622 Elo；AA-LCR v1.1 83.0%；HLE 39.4%；CritPt 18.0%；Terminal-Bench v4.0 33.3%；SciCode 54.1%。 |
| **可信度** | 中——**权重已公开、MIT license 明确**；benchmark 以 Artificial Analysis 为准（部分自报）；**Ant Group 不在本期目标机构清单**，作**邻近开放权重**记录。 |
| **链接** | [Hugging Face inclusionAI/Ling-3.1-flash](https://huggingface.co/inclusionAI/Ling-3.1-flash)；[Pandaily](https://pandaily.com/ant-group-ling-3-1-flash-open-weights-mit-560b-moe-25b-active-1m-context)；[IAMag 分析](https://iamag.it/en/news/ling-3-1-flash-open-weights-mit-560b) |

---

## 五、其他候选 / 备忘（未达收录门槛）

| 候选 | 机构 | 日期 | 状态 |
|------|------|------|------|
| **给 METR 员工级模型访问权限**（frontier 评估；另与 SecureBio、Accenture 合作，与 HF 洽谈） | Anthropic | 2026-10-15 | **治理/评估生态（非卡面）**；与前沿侧"主动求外部评测"叙事同向 |
| **AI worms 可经智能设备扩散**（小模型或"数月内"自复制到智能烤箱/电视/摄像头；大模型已可端到端复制） | Anthropic | 2026-10-15 | **安全研究（非卡面）**；延续 10-12 weight-based replicator 主题 |
| **AI 教练 GPT 于 10-14 从 ChatGPT / ChatGPT Work / Codex 退役**（迁移 GPT-5.6 Sol / GPT-6 Astra；API 不受影响） | OpenAI | 2026-10-14 | **产品线更新（非新卡）**；见 10-15 期 |
| **Grok Voice 3.0**（xAI 语音模型；10-14 上线） | xAI | 2026-10-14 | **语音/产品（非 LLM tech report）**；作信号记录 |
| **Gemini 4 Argon Cyber Permissive**（Argon 的 cyber 变体；10-13） | Google DeepMind | 2026-10-13 | **变体（Argon 本体见 10-14 期）**；跨列见 10-13 期 |
| **WeatherNext 3 / 抗菌肽发现（Google Antigravity for Science）** | Google DeepMind | 2026-10-15 / 09-03 | **科学模型 / 博客（非 LLM 卡面）**；作信号记录 |
| **豆包助手开始按风险评级逐步开放第三方 App**（中国 AI 手机入口之争） | ByteDance | 2026-10-15 | **产品/生态（非模型卡）**；作信号记录 |
| **Moondream 3 Preview / Moondream 3.1** | Moondream | 2026-10-15/16 | **非目标机构**；小 VL 模型，作参照 |
| **Reflection AI Beam（501B/23B，Apache 2.0，承诺 10 月全权重 + tech report）** | Reflection AI | 2026-10-05 预告 | **非目标机构**；权重/tech report 待落地 |
| **Aleph Alpha Kolibri（78.1B/3.46B，英德双语 MoE，1M ctx，Apache 2.0）** | Aleph Alpha | 2026-10-03/04 | **非目标机构**；主权模型，窗口外，作参照 |
| **Mistral Large 4（1T 参数 natively multimodal，49B active，preview；权重承诺 10 月底）** | Mistral AI | 2026-10-06 起 | 目标机构；**权重截至本窗口未落地**，见往期 |

---

## 19 家目标机构窗口内（2026-10-15 → 2026-10-16）复核

| 机构 | 窗口内新报告 / 系统卡 | 备注 |
|------|----------------------|------|
| OpenAI | 无（模型卡） | GPT-5.5 退役（10-14）、GPT-6.1 Sol 预计 **10-19**，均非窗口内新卡 |
| Anthropic | 无（模型卡） | **METR 员工级访问（10-15）**、**AI worms 安全博文（10-15）** 属治理/安全 |
| Google DeepMind | 无（模型卡） | Gemini 4 Argon 本体见 10-14 期；Argon Cyber Permissive（10-13）；WeatherNext 3 / 抗菌肽为科学博客 |
| Meta | **有（★★★，开放权重）** | **Muse Spark Open 816B/42B（§1，10-15）**；Muse Wonder 闭源见 10-13 期 |
| Microsoft AI | 无 | Maia 300 / Microsoft-Decision-1 见往期 |
| xAI | 无（模型卡） | **Grok Voice 3.0（10-14，语音）**；Grok 4.7 见 10-11 期 |
| Mistral | 无 | Mistral Large 4 preview 见 10-06 起各期（权重承诺 10 月底） |
| DeepSeek | 无 | V4.1-Flash 见 10-12 期；V4.1-Pro 预计 **11-12** |
| Alibaba Qwen | 无（新料） | Qwen3.8-Omni-Flash 候选见 10-14 期；Qwen3.5 定价更新（10-14） |
| ByteDance Seed | 无（模型卡） | **豆包 App 开放策略（10-15）** 属产品生态 |
| Moonshot | 无 | Kimi K3 往期（下次预计 **10-22**） |
| Zhipu | 无 | GLM-5.3-Highspeed 见 10-14 期；（下次预计 **10-19**） |
| Tencent | 无 | Hy4 preview 往期 |
| Baidu | 无 | — |
| Amazon | 无（模型卡） | Nova 2.5 Sonic GA 见 10-10 期；Muse Spark Open 上 SageMaker（托管，非自有新模型） |
| NVIDIA | **有（★★★，开放权重）** | **Nemotron 3.5 Super VL 120B-A12B（§2，10-15）**；**Nemotron 3.5 Bolt 74B-A9B / E4B** 见 10-15 期 |
| Cohere | 无 | — |
| AI2 | 无 | Olmo Hybrid / Bolmo 见 10-12 期 |
| Perplexity | 无（模型卡） | 作为 Nemotron Super VL 集成方被点名（搜索 / Computer）；Decider 往期 |
| StepFun | **有（★★，开放权重落地）** | **Step 5 Preview 全权重落地（§3，10-15）** |

> 附注（非 19 家，同窗口）：**Ant Group / inclusionAI Ling-3.1-flash（§4，10-14/15）**、**Reflection AI Beam（待落地）**、**Aleph Alpha Kolibri（窗口外）**。

---

## 本期不重复收录（交叉引用）

- **NVIDIA Nemotron 3.5 Bolt 74B-A9B / E4B 4GB**：见 10-15 期（本期由官方 blog 确认分层定位，参数/口径不重复）。
- **Meta Muse Wonder / Muse Wonder Full（闭源 frontier）**：见 10-13 期（本期仅澄清与 Muse Spark Open 的区别）。
- **Google Gemini 4 Argon GA + Model Card**：见 10-14 期。
- **Zhipu GLM-5.3-Highspeed / Anthropic weight-based replicator / OPENAI GPT-5.5 退役 / NVIDIA $250M UK**：见 10-14 / 10-15 期。
- **Ai2 Olmo Hybrid / Microsoft Maia 300 / Mistral Large 4 / NVIDIA Nemotron 3.5 Lightning / Ultra**：往期已录。

---

## 口径与不确定性声明

- **窗口边界**：主窗口 **2026-10-15 → 2026-10-16**。Muse Spark Open（10-15）、Nemotron 3.5 Super VL（10-15）、Step 5 Preview 权重落地（10-15）、Anthropic METR/AI-worms（10-15）为窗口内一手事件；Ling-3.1-flash 权重释出（10-14/15）为**邻近补录**。
- **首次建档**：本期首次为 **Meta Muse Spark Open**、**NVIDIA Nemotron 3.5 Super VL 120B-A12B**、**Step 5 Preview 开放权重落地（含 StepFun Model License 1.0）**、**Ant Ling-3.1-flash 开放权重**、**Anthropic METR 访问 / AI-worms 博文** 建立 wiki 记录。
- **无 arXiv technical report**：本窗口内**未见目标机构新发 arXiv technical report**；交付形态为**模型卡 / technical blog / evaluation methodology report**（Muse Spark Open 附 evaluation methodology；Nemotron Super VL 附 technical blog + Nemotron 实验室页）。arXiv 上 10-15/16 窗口内检索到的 LLM 训练/推理报告（如 vLLM-Omni 2610.09307 为 10-07）**均早于本窗口**，不收录。
- **未独立复现 / 自评**：Muse Spark Open 与 Nemotron Super VL 的 benchmark **多为厂商自评**（AA Intelligence Index / 吞吐为第三方）；Step 5 / Ling benchmark 除 AA 外多为自评。**各厂商 benchmark 表不可跨厂商横向比较**（harness、effort、采样设置不同）。
- ⚠️ **口径冲突（已显式标注）**：**Meta 与 NVIDIA 同日各称"美系开放权重最强"**，AA Index 数值（39 vs 26.5）口径不一致，**以 Artificial Analysis 官方榜为复核准绳**，本报告并列呈现不作裁定。
- **许可分叉（重点提示）**：同周四种开放权重许可并置——**Muse Model License（限商用）/ OpenMDW-1.1 / StepFun Model License 1.0（三重商用闸门 + 蒸馏条款）/ MIT（Ant）**。使用前须逐份读 license，"开放权重"≠"可无条件商用"。
- **语言**：本期沿用 tech-report-digest 系列既有约定（中文正文 + 英文技术术语），与 10-11 → 10-15 期保持一致。
