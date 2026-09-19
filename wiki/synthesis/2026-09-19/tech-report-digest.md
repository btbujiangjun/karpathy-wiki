---
title: "LLM Tech Report Digest — 2026-09-19"
type: synthesis
created: 2026-09-19
updated: 2026-09-19
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, reasoning, long-context, multimodal, hybrid-architecture, scaling-law, safety, daily-digest]
---

# LLM Tech Report Digest — 2026-09-19

> 全球主要 AI 公司大模型技术报告速览（截至 2026-09-19）
> 全量版：逐家覆盖当前最新 Tech Report / System Card / Model Card / White Paper（延续 09-11 全量版格式；09-18 增量版见 cross-ref）
> 本日主线：**09-17 前后进入"官卡静默 + 半官方/arXiv 信号化"窗口——无任何新 frontier 系统卡发布；信号层新增 = xAI Grok 4.7 有限 rollout 持续（09-17 起）+ DeepSeek-V4.1-Flash arXiv 技术报告上线（2609.19969，09-17 投稿）+ 各家中系新卡以 arXiv/开源卡形式累积（Kimi K3 / Step-3.7-Flash / Baichuan-M4 / Seed2.0 / GLM-5 / Intern-S2）**。全量版把各机构"当前最新"报告作一次盘点，并保留 09-18 已确立的三条纪律：Fable 5.2 rumor 不采信、Grok 4.7 规格创始人口述 low confidence、DeepSeek 763B/552B 参数口径按计量差异（tentative）。

---

## 自 2026-09-18 digest 的 Delta（★ = 09-19 新增确认）

- **DeepSeek-V4.1-Flash 技术报告正式上线 arXiv**（2609.19969，09-17 投稿）——09-14/09-17 摘要的规格得到论文级来源；官方 552B 口径与 The Register 763B（含 N-gram 池）分歧维持 tentative。
- **无新官方系统卡**：OpenAI / Anthropic / Google / Meta / xAI 官方 card 页面均未更新（Anthropic 最新仍 Fable 5.1 & Mythos 5.1 09-01；OpenAI 最新 GPT-6 Astra 09-03 / GPT-5.6 07-09）。
- **Grok 4.7**：limited rollout 持续（09-17 起），GA/定价/benchmark card 均未发布 —— 维持"灰度发布"判据。
- ⚠️ **CONTRADICTION**：kie.ai 声称 Fable 5.2 已于 09-10 发布 vs 官方 system-cards 页最新仍 5.1 —— 维持不采信（09-18 已录，本版不再重复论证）。
- 本版为全量盘点，不再标注每项 ★/⭐（见各条目"发布日期"）。

---

## 1. DeepSeek

### 1.1 DeepSeek-V4.1-Flash（最新）
- **中文标题**: DeepSeek-V4.1-Flash 技术报告
- **英文标题**: DeepSeek-V4.1-Flash Technical Report
- **发布机构**: DeepSeek-AI
- **模型名称**: DeepSeek-V4.1-Flash（V4 系列 Flash 档）
- **发布日期**: arXiv 投稿 2026-09-17（2609.19969）；模型上线 2026-07（V4-Flash-0731）
- **核心参数**: 552B 总参数 MoE（CED 架构，40 层）；prefill 激活 ~8B / decode 激活 ~16B；上下文 1M tokens；多模态（45T 混合训练语料）；⚠️ The Register 口径 763B（含巨量 N-gram 参数池）——计量口径差异 tentative
- **主要创新点**:
  - CED（Compressed Efficient Decoder）架构承接 V4 线 CSA+HCA
  - **CSA2 跨层 KV 复用 + FP4 KV 量化 → 890 B/token，仅为 V4-Flash 的 ~1/4 HBM 占用**
  - **SWA Bounded Replay → KV/参数 SSD 足迹约降至 1/8**
  - Native vision 多模态；1M 长上下文推理成本远低于同代 dense
- **链接**: [arXiv:2609.19969](https://arxiv.org/abs/2609.19969)；官方 V4.1-Flash 新闻页（552B/8B-16B active 口径）；The Register 763B 报道
- 前代（已录）：V3（2412.19437）、V3.2（2512.02556，DSA 稀疏注意力）、R1（2501.12948，GRPO）、V4（2606.19348，1.6T/49B active Pro）

## 2. OpenAI

### 2.1 GPT-6 Astra System Card（最新）
- **中文标题**: GPT-6 Astra 系统卡
- **英文标题**: GPT-6 Astra System Card
- **发布机构**: OpenAI
- **模型名称**: GPT-6 Astra
- **发布日期**: 2026-09-03（首个达 Preparedness Critical 网络安全级别的模型）
- **核心参数**: 参数量未公开；多模态
- **主要创新点**:
  - 首个在 Preparedness 框架下达到 **Critical 网络安全等级**的模型
  - Agent's Last Exam 59.3%（vs Fable 5 48.7% / Opus 5 52.7%）
  - Aidan Clark 自述：首个"训练显著由其他模型辅助"的模型
  - 分阶段灰度铺开（DevDay 09-29 为下节点）
- **链接**: [deploymentsafety.openai.com/gpt-6-astra](https://deploymentsafety.openai.com/gpt-6-astra/gpt-6-astra.pdf)

### 2.2 GPT-5.6 System Card
- **中文标题**: GPT-5.6 系统卡
- **英文标题**: GPT-5.6 System Card
- **发布机构**: OpenAI
- **模型名称**: GPT-5.6（家族：Sol / Terra / Luna）
- **发布日期**: 2026-07-09
- **核心参数**: 参数量未公开
- **主要创新点**: 家族化高低档配置；Sol 为当前推理旗舰参照（Kimi K3 报告自我对比对象）；安全评估体系延续 Preparedness
- **链接**: [deploymentsafety.openai.com/gpt-5-6](https://deploymentsafety.openai.com/gpt-5-6)
- 前代（已录）：GPT-5 System Card（arXiv:2601.03267，2025-08/2026-05）、o1（2412.16720）、GPT-4.5（2025-02）
- 注：GPT-6 Sol 传闻（09-16 CometAPI）维持 rumor 级，不入本版

## 3. Anthropic — Claude

### 3.1 Claude Fable 5.1 & Mythos 5.1 System Card（最新）
- **中文标题**: Claude Fable 5.1 与 Mythos 5.1 系统卡
- **英文标题**: System Card: Claude Fable 5.1 & Claude Mythos 5.1
- **发布机构**: Anthropic
- **模型名称**: Claude Fable 5.1 / Mythos 5.1
- **发布日期**: 2026-09-01（官方 system-cards 页最新；kie.ai 宣称的 5.2 不采信）
- **核心参数**: 参数量未公开；Fable 5.1 定价 $10/$50 per M
- **主要创新点**:
  - 编码 / 知识工作 / 问题解决前沿推进
  - **Mythos 5.1 网络安全评估史上最强**（ExploitBench / OSS-Fuzz / Firefox 147 / ExploitGym 全线优于 Opus 5）
  - Fable 5.1：CB-1 化学/生物能力但未达 CB-2 阈值；Terminal-Bench-Science 52.6
  - Mythos 5.1 在系统提示下的诚实度低于近期 Claude 模型（卡内披露）
- **链接**: [Anthropic CDN PDF](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20%26%20Claude%20Mythos%205.1%20System%20Card.pdf)；[anthropic.com/system-cards](https://www.anthropic.com/system-card)
- 前代（已录）：Claude Opus 5（2026-07-24，ECI 162.1）、Opus 4 & Sonnet 4（2025-05）
- 注：07 月威胁情报报告点名 DeepSeek 等 7 家中国实验室蒸馏（7 月 14 天约 1210 万 exchange）——单方指控，作行业叙事记录

## 4. Meta AI

### 4.1 Muse Spark（最新，1.3）
- **中文标题**: Meta Muse Spark 评估报告 / 模型卡
- **英文标题**: Muse Spark Evaluation Report / Model Card
- **发布机构**: Meta AI
- **模型名称**: Muse Spark 1.3（系列含 Muse Glimmer 08-10）
- **发布日期**: Muse Spark 1.3 — 2026-09-02；官方静态页为 "muse-spark-1-1-evaluation-report"（命名档位待复核，tentative）
- **核心参数**: 上下文 **1.05M tokens**；参数量未公开
- **主要创新点**:
  - 超长上下文多模态研究模型；评估报告覆盖预缓解前 Chem/Bio + Cyber "high risk" 分类
  - Artificial Analysis 第三方指数 **≈60**（补 pin，量级与 09-18 一致）
  - LLaMA 主线已退役（无新报告）
- **链接**: [research.meta.ai Muse Spark](https://research.meta.ai/static/muse-spark-1-1-evaluation-report)（文件名档位 tentative，1.3 以索引/第三方录为准）
- 前代（已录）：Llama 4 Scout & Maverick（2025-04）、Llama 3 Herd（2407.21783）

## 5. Google DeepMind — Gemini

### 5.1 Gemini 3.8 Flash Model Card（最新）
- **中文标题**: Gemini 3.8 Flash 模型卡
- **英文标题**: Gemini 3.8 Flash Model Card
- **发布机构**: Google DeepMind
- **模型名称**: Gemini 3.8 Flash（基于 Gemini 3.7 Flash）
- **发布日期**: 2026-09-02
- **核心参数**: 上下文 1M；输出 65K；thinking LOW/MED/HIGH；HLE-Verified 54.9 / TB2.1 90.8 / SWE-Bench Pro 61.6
- **主要创新点**:
  - 独立评测 AA Intelligence Index **≈59**（齐平/略超 GPT-Astra 58；第三方首个）
  - 定价 **$0.75–$3.75 per M**（引价至 2026 年底）——Flash 档性价比前沿
  - ⚠️ 社区 regression 帖（09-14 discuss.ai.google.dev，low confidence，无官方回复）
- **链接**: [Gemini 3.8 Flash Model Card](https://deepmind.google/models/model-cards/gemini-3-8-flash/)

### 5.2 Gemini 3.8 Live / Live Extended Thinking（最新）
- **中文标题**: Gemini 3.8 Live 实时语音模型卡
- **英文标题**: Gemini 3.8 Live / Live Extended Thinking
- **发布机构**: Google DeepMind
- **模型名称**: Gemini 3.8 Live / Live-ET
- **发布日期**: 2026-09-15
- **核心参数**: speech-to-speech；AA S2S 质量 ≈82.6；Live-ET 为 think-then-speak 深度思考变体
- **主要创新点**: **$3.50/hr** 实时语音定价（对赌 GPT-Live-1 Astra $5.83/hr）；实时语音 = 9 月新战场
- **链接**: [deepmind.google Gemini](https://deepmind.google/models/gemini/)
- 前代（已录）：Gemini 2.5 Technical Report（arXiv:2507.06261，2025-07）

## 6. Microsoft

### 6.1 MAI-Thinking-1（最新，MAI 线）
- **中文标题**: MAI-Thinking-1：构建爬山机器
- **英文标题**: MAI-Thinking-1: Building a Hill-Climbing Machine
- **发布机构**: Microsoft AI
- **模型名称**: MAI-Thinking-1
- **发布日期**: 2026-06-02（白皮书）
- **核心参数**: **1T 总参数 / 35B 激活（MoE）**；从零训练、无第三方蒸馏、自建企业级数据清洗
- **主要创新点**:
  - 从零训练（no distillation from third-party models）
  - SWE-Bench Pro 52.8% / AIME 2025 97.0% / LiveCodeBench v6 87.7%
  - "Hill-climbing"：在线 self-play 式推理改进训练范式
- **链接**: [microsoft.ai 白皮书 PDF](https://microsoft.ai/wp-content/uploads/2026/06/main%5F20260602%5F2.pdf)
- Phi-5 无官方报告（维持）；前代 Phi 线（已录）：Phi-4（2412.08905）、Phi-4-reasoning（2504.21318）、Phi-4-Mini（2503.01743）

## 7. NVIDIA

### 7.1 Nemotron 3 Family（最新线）+ Nemotron 3.5 Lightning
- **中文标题**: NVIDIA Nemotron 3 家族技术报告 / Nemotron 3.5 Lightning 发布
- **英文标题**: NVIDIA Nemotron 3: Efficient and Open Intelligence / Nemotron 3.5 Lightning
- **发布机构**: NVIDIA
- **模型名称**: Nemotron 3 Ultra (550B-A55B, 2026-06) / Super (120B-A12B, 2026-04) / Nano (30B-A3B, 2025-12)；**Nemotron 3.5 Lightning (30B-A3B)**
- **发布日期**: 家族 2025-12 起；3.5 Lightning 2026-09（无独立技术报告，官方以 README + HF 模型卡为权威）
- **核心参数**: Ultra 550B/55B active；3.5 Lightning 30B-A3B（52 层、hidden 2688、128 routed top-6 + 1 shared expert）；上下文 1M；NVFP4
- **主要创新点**:
  - **Hybrid Mamba-Transformer MoE**（SSM + Attention 混合架构）
  - **MTP（Multi-Token Prediction）** + LatentMoE + MOPD 训练目标
  - Multi-environment RL 后训练；粗粒度推理预算控制
  - NVFP4 4-bit 预训练稳定至 25T+ tokens；Ultra 推理吞吐 5.9× GLM-5.1-754B-A40B
  - 3.5 Lightning 主打高效推理（README 规格线）
- **链接**: [arXiv:2512.20856](https://arxiv.org/abs/2512.20856)（Nemotron 3）；[github.com/nvidia-nemo/nemotron/docs/nemotron/lightning35](https://github.com/nvidia-nemo/nemotron)

## 8. Apple

### 8.1 Third-Generation Apple Foundation Models（最新）
- **中文标题**: 第三代 Apple Foundation Models（AFM 3）
- **英文标题**: Introducing the Third Generation of Apple Foundation Models
- **发布机构**: Apple（与 Google 合作）
- **模型名称**: 家族 5 个模型：AFM 3 Core (3B dense) / AFM 3 Core Advanced (20B sparse，激活 1–4B 按需)；AfM 3 Server 系列
- **发布日期**: 2026-06-08（年度技术报告 2026 版"later this summer"已过期未发，官网研究笔记为准）
- **核心参数**: Core 3B 端侧 dense；Core Advanced 20B sparse 原生多模态（激活随请求 1–4B）
- **主要创新点**:
  - 稀疏按需激活（sparse request-dependent activation）——端侧算力预算自适应
  - 原生多模态；Private Cloud Compute 扩展
  - 与 Google 联合（AI 芯片/集群合作）
- **链接**: [machinelearning.apple.com](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models)
- 前代（已录）：AFM 2025 Tech Report（arXiv:2507.13575，PT-MoE）

## 9. Qwen / 阿里巴巴

### 9.1 Qwen3.8 系列（最新线）
- **中文标题**: Qwen3.8-Max / Qwen3.8-Flash-Next
- **英文标题**: Qwen3.8-Max / Qwen3.8-Flash-Next
- **发布机构**: Alibaba / Qwen Team
- **模型名称**: Qwen3.8-Max（2026-08，2.4T，1M ctx，原生多模态）；Qwen3.8-Flash-Next（2026-08-26，125B-A6B + **51B N-gram 嵌入**、off-accelerator 系统 RAM，Qwen4 架构预览）
- **发布日期**: 2026-08
- **主要创新点**:
  - Qwen3.8-Max：16 天自主执行真实软件工程项目；联合缩放 RL 环境与算力；Text Arena #5 / Vision Arena #2
  - Flash-Next：**N-gram 非激活嵌入 + off-accelerator** → 账面参数与激活稀疏的新记账（中系共识手法之一）
- **链接**: [arXiv:2605.10730](https://arxiv.org/abs/2605.10730)（Qwen-Image-2.0 Technical Report，Qwen3-VL encoder + Multimodal DiT，2026-05-11）；[Alibaba 官方](https://www.alibabagroup.com/en-US/)

## 10. xAI — Grok

### 10.1 Grok 4.7（最新，状态）
- **中文标题**: Grok 4.7（有限 rollout 中）
- **英文标题**: Grok 4.7 (limited rollout)
- **发布机构**: xAI
- **模型名称**: Grok 4.7（约 2.1T 创始人口述，low confidence）
- **发布日期**: 有限 rollout 2026-09-17 起（Google Cloud quota 先行）；GA/定价/benchmark card 未发布
- **主要创新点**:
  - Musk："roughly on par with Opus 5.0, not 5.1"
  - 路线图：Grok 4.8（2.5T，新 C++ 软件栈，收尾入 RL）→ 4.9（Astra/Fable class）→ Grok 5（3T）
  - 发布节奏 = 配额页 + 灰度 rollout（无卡阶段）
- **链接**: 无官方卡；HuggingNews 09-17 聚合 / DigitalToday 09-15
- 已发布卡（前代）：Grok 4 Model Card（2025-08-20，[data.x.ai](https://data.x.ai/2025-08-20-grok-4-model-card.pdf)）、Grok 4.20 System Card（2026-04-07）；Grok 4.6（08-12，500K ctx，$2/$0.5/$6 per M）为当前已发布旗舰
- ⚠️ 规格全为创始人口述/第三方，low confidence；不入 claim 页

## 11. 其他中系 & 目标机构（全量盘点，逐条复核）

### Moonshot AI — Kimi
- **最新**: Kimi K3 — **中文标题** Kimi K3：开放前沿智能；**英文标题** Kimi K3: Open Frontier Intelligence；**发布日期** 2026-07-16（arXiv v2）；**核心参数** **2.8T 总 / 104B 激活 MoE**、原生视觉、1M 上下文、896 专家（16 routed Stable LatentMoE）；**主要创新点** **Kimi Delta Attention (KDA) + Attention Residuals**、**Stable LatentMoE**、对 K2 约 **2.5× 数据效率**；自我对标落后 Claude Fable 5 与 GPT-5.6 Sol；权重 HF moonshotai/Kimi-K3
- **链接**: [arXiv:2607.24653](https://arxiv.org/abs/2607.24653)；前代 K2（2507.20534）、K2.5（2602.02276）

### Amazon
- **最新**: Amazon Nova 2 — **英文标题** Amazon Nova 2: Multimodal Reasoning and Generation Models；**核心参数** 家族 Nova 2 Lite/Pro/Omni/Sonic，最多 1M tokens；**发布日期** 2025-12-02
- **链接**: [amazon.science](https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models)；前代 Nova Family（2506.12103，2025-03）

### 智谱 AI — GLM
- **最新**: **GLM-5**（中文标题 GLM-5：从 Vibe Coding 到 Agentic Engineering）**arXiv:2602.15763v2**（2026-02）：约 744B/~40B active，DSA 稀疏注意力（KV -75%、推理 +3×），SWE-Bench Verified 77.8%，国产芯片七大平台，2026-01 港股上市
- **次新**: **GLM-5.3**（08-14，CyberGym 84.5 / 1M ctx，权重 ~08-28 开源）+ GLM-5.3-Flash（国产芯片全流程）；N-gram/稀疏注意力细节并入交叉主题
- **链接**: [arXiv:2602.15763](https://arxiv.org/abs/2602.15763)；[z.ai](https://z.ai/)

### InternLM / 上海 AI Lab
- **最新**: **Intern-S2-Preview**（arXiv:2608.13505，2026-08-14，科学 agentic 基础模型）；**Intern-S2-397B 正式版** 2026-09-13 Apache-2.0（wiki 09-15 已录）
- **链接**: [arXiv:2608.13505](https://arxiv.org/abs/2608.13505)；前代 InternVL3.5（2508.18265）

### StepFun — 阶跃星辰
- **最新**: **Step-3.7-Flash** — **中文标题** Step-3.7-Flash；**英文标题** Step-3.7-Flash；**日期** 2026-05-27（GitHub）；**核心参数** **198B 稀疏 MoE VLM = 196B LLM + 1.8B 视觉编码器，约 11B active**；256K 上下文；**主要创新点** 3 档推理级别、最快 400 tok/s、Agent 定位；Apache-2.0
- **链接**: [GitHub stepfun-ai/Step-3.7-Flash](https://github.com/stepfun-ai/Step-3.7-Flash)；前代 Step-3（2507.19427）、Step-3.5 Flash、Step-DeepResearch（2512.20491）

### ByteDance
- **最新**: **Seed2.0 Model Card**（家族 Seed2.0 Pro / Lite / Mini；评估框架 Science Discovery / Vibe Coding / Context Learning / Real-World Tasks；Volcano 平台接入）；**日期** 2026-02-14
- **链接**: [Seed2.0 Model Card PDF](https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/seed2/0214/Seed2.0%20Model%20Card.pdf)；前代 Seed1.6、Seed-Thinking-v1.5、Seed1.5-VL

### Baichuan
- **最新**: **Baichuan-M4**（arXiv:2606.08982，2026-06）——临床级医疗 Agent 系统（与清华 THUBPM 合作）；**SPAR++ span 级奖励建模**；**幻觉率 3.3%**
- **链接**: [arXiv:2606.08982](https://arxiv.org/abs/2606.08982)；前代 Baichuan-Omni（2410.08565）

### Mistral AI
- **最新**: **Mistral Large 3 675B Instruct 2512**（HF mistralai/Mistral-Large-3-675B-Instruct-2512-BF16）——675B 总 / **41B active 细粒度 MoE + 2.5B 视觉编码器**、256K 上下文、Apache-2.0；Mistral 3 家族 2025-12
- **链接**: [HF Mistral Large 3](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512-BF16)；前代 Magistral（2025-06）、Mistral Medium 3（2025-05）

### 01.AI — Yi
- **最新维持**: **Yi-Lightning（2024-10-16，商品卡）仍为最新**；confirmed 零动态（09-17/09-18 复核一致）。综合技术报告为 Yi: Open Foundation Models（arXiv:2403.04652，2024-03/v3 2025-01）
- **链接**: [arXiv:2403.04652](https://arxiv.org/abs/2403.04652)

### MiniMax（非目标清单但常被引用）
- **M3（428B-A23B）** 已录；无新

---

## 交叉主题分析

### 1. 官方卡静默 + "信号层发布"成常态
- 09-18→09-19 官方系统卡全面静默（Anthropic/OpenAI/Google/Meta 均无更新）；信息主要来自：arXiv 新投稿（DeepSeek V4.1-Flash 2609.19969）、第三方评测指数（AA）、灰度 rollout 实测（Grok 4.7）、泄漏/传闻（Fable 5.2、GPT-6 Sol）。**发布确认判据 = 官方卡/API 定价为准，其余一律 low confidence/tentative。**

### 2. "账面参数 vs 激活稀疏"记账语言成形（延续 09-18）
- DeepSeek V4.1-Flash（552B 官方 vs 763B 含 N-gram 池）、Qwen3.8-Flash-Next（51B N-gram 嵌入 off-accelerator）、GLM-5.3、NVIDIA Nemotron（LatentMoE/MTP）——**跨厂参数对比必须统一"激活参数 + KV/账单价"口径**，否则系统性高估稠密旗舰。

### 3. 推理档位与成本曲线双线竞争
- 成本线：Gemini 3.8 Flash $0.75–3.75/M、Grok 4.6 $0.5–6/M；语音时薪线：Gemini 3.8 Live $3.50/hr vs GPT-Live-1 Astra $5.83/hr。**"能力范式平替 + 价格战"成为中系开源（Step/Kimi/GLM/DeepSeek）针对前沿封闭模型的共性路线。**

### 4. 蒸馏指控与开源追赶叙事
- Anthropic 对 DeepSeek 等 7 家实验室的蒸馏指控（约 1210 万 exchange/14 天）与"从零训练"（MAI-Thinking-1 no-distillation）形成叙事对照；DeepSeek/Kimi/Step 在 45T/混合数据上跑出自有架构（CED、KDA、AFD 系）——**维持"指控为单方记录、架构本身从零成立"的分层**。

---

*Generated 2026-09-19. Sources: Web 检索（OpenAI deploymentsafety GPT-6 Astra / GPT-5.6、Anthropic CDN Fable& Mythos 5.1、deepmind.google 3.8 Flash / Live、arXiv 2609.19969 / 2607.24653 / 2605.10730 / 2602.15763v2 / 2608.13505 / 2606.08982 / 2403.04652 / 2606.19348、microsoft.ai MAI-Thinking-1、machinelearning.apple.com AFM 3、github.com/nvidia-nemo/nemotron、research.meta.ai Muse Spark、amazon.science Nova 2、lf3-static.bytednsdoc.com Seed2.0、HF Mistral Large 3、github.com/stepfun-ai/Step-3.7-Flash、HuggingNews/DigitalToday xAI）。Cross-referenced with wiki/synthesis/2026-09-18/tech-report-digest.md（Grok 4.7 rollout、Gemini 3.8 双档、Fable 5.2 纪律、DeepSeek 763B 口径）、2026-09-11/tech-report-digest.md（全量版格式与 2024-12–2026-08 基线）。*