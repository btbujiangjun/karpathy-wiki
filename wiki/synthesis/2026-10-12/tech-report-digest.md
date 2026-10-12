---
title: "LLM Tech Report Digest — 2026-10-12"
type: synthesis
created: 2026-10-12
updated: 2026-10-12
sources: []
tags: [tech-report, LLM, technical-report, model-card, system-card, hybrid-architecture, gated-deltanet, linear-rnn, moe, byte-level, tokenization, decision-model, multimodal, text-to-image, diffusion, long-context, scaling-law, ai2, cloudflare, google, alibaba-qwen, meta, daily-digest]
---

# LLM Tech Report Digest — 2026-10-12

> **窗口判定：2026-10-11 → 2026-10-12。** 19 家目标机构（OpenAI / Anthropic / Google DeepMind / Meta / Microsoft AI / xAI / Mistral / DeepSeek / Alibaba Qwen / ByteDance Seed / Moonshot / Zhipu / Tencent / Baidu / Amazon / NVIDIA / Cohere / AI2 / Perplexity）在窗口内**仍无新的 frontier 文本模型技术报告 / 系统卡 / model card**，官方"卡面"维持静默（frontier 侧最近一次仍是 09-29 GPT-6 Sol 与 09-28 Claude Sonnet 5.5；Gemini 4 Argon 于 09-30 亮相但仅限 Fairwind 试点）。

> **本期为"邻近补录 + 架构/模态双主线"版。** 窗口内无 frontier 卡面，但 10-07 ~ 10-09 的三条**架构/模态级**发布在本 wiki 内 grep 0 命中（首见），构成窗口内唯一实质技术增量：① **混合架构**——Ai2 **Olmo Hybrid**（Gated DeltaNet + attention 3:1）在 COLM 2026 recap 中重新浮出，给出"hybrid 比纯 transformer 更具表达力、scaling 更高效"的受控证据；② **字节级建模**——Ai2 **Bolmo** 方法登上 **Nature**，byteification 外推至 Qwen3 / Llama 3（Bwen 8B / Blama 8B）；③ **决策模型**——Cloudflare **Clef-omni** 把决策模型推进到 **audio + video** 全模态。另有一条 10-11 的 **Meta "Llama 4 Scout MoD" 传闻**（低可信、与官方口径冲突，见第八节）。

---

## 本期要点（相对 2026-10-11 新增/更新）

- ★★★ **Ai2 Olmo Hybrid 7B（AI2，论文 2026-04 / COLM 2026 recap 10-09，补录）**——**混合架构的受控大规模证据**：在 Olmo 3 7B 上把 **75% 的 sliding-window attention 层替换为 Gated DeltaNet（GDN）**，形成 **3:1（GDN:attention）** 交错模式。7B 参数、6T token 预训练（512 GPU，**H100 → B200**），**MMLU 上以少 49% token 达到 Olmo 3 同等精度（≈2× 数据效率）**；Common Crawl 少 35% token 追平；长上下文 **RULER 64k +14.1%**。理论主张：hybrid 能表达**纯 transformer 与纯 linear RNN 都无法单独表达的任务（如 code execution）**，该表达力优势直接转化为 scaling 效率（数据系数 B 更低，token 节省 **~1.3×@1B → ~1.9×@70B**）。arXiv:2604.03444 *Olmo Hybrid: From Theory to Practice and Back*。
- ★★ **Ai2 Bolmo 登上 Nature：byteification 外推（AI2，2026-10-07）**——**字节级 LLM 的可复用配方**：两阶段"byteification"在 **<1% 预训练预算（合计 49.1B token；stage1 9.8B 冻结 + stage2 39.3B 端到端）** 内把已有 subword 模型改造为 byte-level。新权重 **Bwen 8B**（byteified **Qwen3 8B Base**，最强 byteified）与 **Blama 8B**（byteified **Llama 3 8B**）；**Bolmo 7B** 在 STEM 上较从零训练的 **BLT 7B +16.5%**（绝对值）。机制：1 层 mLSTM local encoder + 非因果 boundary predictor（前看 1 byte）做变长 patch 分组 + 保留源 transformer 作 global model + 4 层 mLSTM decoder。Nature `s41586-026-11111-4`（Minixhofer 等）。
- ★★ **Cloudflare Clef-omni（Cloudflare，2026-10-09）**——**全模态决策模型**：在 **Qwen3-Omni-30B-A3B-Instruct** 的 thinker 主干（保留 vision/audio encoder、丢弃 TTS 输出）上 post-train 的 **30B-A3B MoE 决策模型**，**Apache-2.0**。输入 state 可为 **text / JSON / 图像（≤4）/ 音频（≤4，≤300s）/ 视频（≤2，≤60s，2fps）**；输出**每个 typed question（noul / choice / score，1–64 题）每个允许选项的校准概率**，**单次前向、无自由文本生成、无输出解析**。延迟：文本 ~130ms、图像 ~150ms、音频数百 ms、**21 秒带声视频 ~1.5s**；定价 **$0.15 / M input**。同族 **Clef**（dense 图像/视频）与 **Clef-flash**（降价、提速）。
- ★ **Google Gemini 4 "Carbon" 内部 checkpoint 泄露（Google DeepMind，Business Insider 2026-10-09）**——**信号级，非发布**：内部文档/截图显示 Google 测试 Gemini 4 的 **Argon / Barium / Carbon** 变体，Carbon 部署于内部编码平台 **Jetski**（Antigravity 相关）；一名员工称 Carbon 编程"**feels like Opus 5.5**"（另一人称"Carbon is really good!"）。⚠️ **无任何公开基准、无发布日期、Google 拒评**——单源匿名主观印象，**低可信**。参照：Gemini 4 Argon 09-30 亮相（内部代号 Barium-B），厂商 launch table 的 DeepSWE v1.1 为 Argon 77.9% / Opus 5.5 74.2% / GPT-6 Astra 74.1%（**属 Argon，非 Carbon**）。
- ★ **Qwen-Image-2.1-Turbo（Alibaba Qwen，2026-10-09）**——**开源图像生成/编辑加速 checkpoint**：沿用 Qwen-Image-2.1 的 **7B 视觉生成组件（32 层 single-stream DiT）+ Qwen3-VL 8B 文本编码器 + 64 通道 RGBA VAE（16× 空间压缩、原生透明）+ Flow Matching（Euler discrete + dynamic shifting）**，把默认 **40 步去噪压缩到 8 步**（CFG=1，checkpoint 内置 8 步 schedule）。支持 **2K（2048×2048，预设至 2752×1536）** 文生图与**多参考编辑**。**Qwen Research License（非商用）**；base 在 Qwen-Image-Bench 得 60.28。Pro/Turbo API 同日上线阿里云 Model Studio（Turbo API **CNY 0.1/图**，为 Pro 的 0.4×）。
- ⚠️ **【低可信传闻】Meta "Llama 4 Scout MoD re-release"（2026-10-11）**——**未证实**：dev.to 及多个聚合站称 Meta FAIR"重新发布" Llama 4 Scout，规格为 **105B 总参 / 24B 激活、Mixture-of-Depths、原生 1M 上下文、RingAttention + sliding-window MLA、99.8% NIAH、4-bit 24GB VRAM、FP8/INT4 AWQ**。⚠️ **与官方 Llama 4 Scout（2025-04-05：109B 总参 / 17B 激活、16 experts、MoE 而非 MoD、10M 上下文）口径冲突**，且**无 Meta/FAIR 官方 model card**、来源均为 SEO/聚合转发——**不予采信，仅作传闻记录**。
- ★ **交叉主题：架构与模态的双重外扩**——本周（补录窗）主线并非"更大模型"，而是**架构层**（Ai2 hybrid GDN、Ai2 byte-level）与**模态层**（Cloudflare 决策模型纳入 audio/video、Qwen 图像加速）的横向扩张；与前两期"决策模型新类别"（Microsoft-Decision-1 / Liquid d1 / Perplexity Decider）**同源**，Clef-omni 是该类别**全模态化**的下一步。

---

## 一、Ai2 Olmo Hybrid 7B（AI2，2026-04 论文 / COLM 2026 recap 2026-10-09）

| 字段 | 内容 |
|------|------|
| **中文标题** | Ai2 发布 Olmo Hybrid：用 Gated DeltaNet 替换 sliding-window attention，验证混合架构更优 scaling |
| **英文标题** | Introducing Olmo Hybrid: Combining transformers and linear RNNs for superior scaling / Olmo Hybrid: From Theory to Practice and Back |
| **发布机构** | Ai2（Allen Institute for AI，Olmo 团队） |
| **模型名称** | `Olmo Hybrid 7B`（全开放权重，含中间 checkpoint） |
| **发布日期** | 博客 2026-03-05；arXiv **2604.03444** 2026-04-03；COLM 2026 recap 于 **2026-10-09** 重新浮出（本期收录触发点） |
| **核心参数** | 架构沿用 Olmo 3 7B，**把 75% 的 sliding-window attention（SWA）层替换为 Gated DeltaNet（GDN）**，**3:1（3 GDN + 1 attention）**每层组重复；GDN 采用**负特征值扩展**（`β_t → 2β_t`，`allow_neg_eigval=True`，区别 Qwen3-Next / Kimi Linear / Qwen3.5 所用 GDN）。为对齐参数/TPS，head 数 32→30、d_model 减 2×128。**7.0B 参数**（Olmo 3 7B 为 6.8B），Dolma 2 tokenizer + OLMo-mix-0925 数据，**6T token**预训练，**512 GPU（H100 → 中途迁移 B200，Lambda 托管）**——首批在 B200 上训练的 SOTA 全开放模型之一。 |
| **主要创新点** | ① **MMLU 少 49% token 追平 Olmo 3 7B（≈2× 数据效率）**，Common Crawl 少 35% token 追平；② **长上下文 RULER 64k +14.1%**（YaRN 与 DroPE 两种扩展均优于 Olmo 3）；③ 纯预训练 checkpoint 在 math +4.3% / STEM MC +3.4% / non-STEM MC +4.4%（code −2.5% / general QA −2.3%），**mid-training 后在所有 OlmoBaseEval 域反超**；④ **理论**：hybrid 可表达**纯 transformer 与纯 linear RNN 均难表达的任务（如 code execution）**，scaling-law 拟合显示**数据系数 B 显著更低**，token 节省 **~1.3×@1B → ~1.9×@70B**；⑤ 全开放（权重 + 训练脚本 OLMo-core）。 |
| **链接** | [allenai.org/blog/olmohybrid](https://allenai.org/blog/olmohybrid)；[arxiv.org/abs/2604.03444](https://arxiv.org/abs/2604.03444)；训练脚本 [github.com/allenai/OLMo-core .../OLMo-hybrid-7B-pretrain.py](https://github.com/allenai/OLMo-core/blob/main/src/scripts/official/OLMo-hybrid/OLMo-hybrid-7B-pretrain.py) |

**与大势对读**：hybrid（attention + linear RNN）此前常被视为**推理效率**手段；Olmo Hybrid 的主张是**表达力 → 更优 scaling**（不只省显存）。COLM 2026 recap 另提"下一次 Olmo 预训练将采用 **hybrid MoE（attention + recurrence）**"（(tentative)——来自 recap 转述，非论文正文，标为二手）。

---

## 二、Ai2 Bolmo 登上 Nature：byteification（AI2，2026-10-07）

| 字段 | 内容 |
|------|------|
| **中文标题** | Ai2 的 byteification 登上 Nature：把 subword 模型改造为字节级 LLM |
| **英文标题** | Retrofitting language models to operate over bytes / Now in Nature: Retrofitting language models to operate over bytes |
| **发布机构** | Ai2 与 University of Edinburgh 等（作者 Minixhofer, Murray, Limisiewicz, Korhonen, Zettlemoyer, N. Smith, Ponti, Soldaini, Hofmann） |
| **模型名称** | `Bolmo 7B`（← Olmo 3 7B）、`Bolmo 1B`（← OLMo 2 1B）、**`Bwen 8B`**（← Qwen3 8B Base）、**`Blama 8B`**（← Llama 3 8B） |
| **发布日期** | Nature 论文 2026-10-07（`s41586-026-11111-4`）；HF 新 checkpoint 同日 |
| **核心参数** | **byteification**（两阶段）：① 1 层 **mLSTM local encoder** 对 UTF-8 byte embedding 做上下文化；② **非因果 boundary predictor**（前看 1 byte）决定 patch 边界，拼为 **512-token 词表**；③ **保留源 transformer 作 global model**；④ 4 层 **mLSTM decoder** 做字节级解码。训练 **stage1 9.8B token（冻结 global）+ stage2 39.3B token（端到端）**，合计 **49.1B token（<1% 典型预训练预算）**。许可：**Bwen 8B = Apache-2.0**、**Blama 8B = Llama 3 Community License**。 |
| **主要创新点** | ① **Bolmo 7B 在 STEM 上较从零训练的 BLT 7B 绝对 +16.5%**；② **Bwen 8B 统计显著优于所有同规模先前进 byte-level 模型**（除 GenQA 略逊 TFree-HAT 7B），逼近源 Qwen 模型；③ 字节级模型在**字符理解任务**上显著超越 subword 对照；④ byteified 模型可**通过提高 bytes-per-patch 比任意加速**（subword 受限）；⑤ **可复用源 LLM 生态组件**（无需额外训练成本即可适配）。 |
| **链接** | [nature.com/articles/s41586-026-11111-4](https://www.nature.com/articles/s41586-026-11111-4)；[allenai.org/blog/bolmo-nature](https://allenai.org/blog/bolmo-nature)；HF [allenai/Bolmo](https://huggingface.co/collections/allenai/bolmo) |

> **对读 Olmo Hybrid**：同一机构同周释放两条**"改造既有模型/架构"**而非"从零堆规模"的信号——hybrid 改**层类型**，byteification 改**输入粒度**。二者共同主题：**在既有基座上以极低额外算力换取能力/效率增量**。

---

## 三、Cloudflare Clef-omni（Cloudflare，2026-10-09）

| 字段 | 内容 |
|------|------|
| **中文标题** | Cloudflare 发布 Clef-omni：可读文本/图像/音频/视频的全模态决策模型 |
| **英文标题** | Introducing Clef-omni with full multimodality, plus a faster Clef and a cheaper Clef-flash |
| **发布机构** | Cloudflare |
| **模型名称** | `clef-omni`（`@cf/cloudflare/clef-omni`）；同族 `Clef`、`Clef-flash` |
| **发布日期** | 博客 2026-10-09；HF 权重 `Cloudflare/clef-omni` 2026-10-11 |
| **核心参数** | **30B-A3B MoE**（HF 计 **35B 参数**），post-train 自 **Qwen/Qwen3-Omni-30B-A3B-Instruct**（保留 thinker + vision/audio encoder，丢弃 talker/code2wav TTS 权重）；**Apache-2.0**；**64k 上下文**。输入 state 支持 **text / JSON / 图像（≤4，≤16MP）/ 音频（≤4，≤300s）/ 视频（≤2，≤60s，2fps，含音轨）**；返回**每个 typed question（noul / choice / score；1–64 题）每个允许选项的概率**，**单次前向、无输出 token、无解析**。延迟：文本 ~130ms / 图像 ~150ms / 音频数百 ms / 21s 带声视频 ~1.5s。定价 **$0.15 / M input**。 |
| **主要创新点** | ① **决策模型全模态化**——把 audio/video 纳入同一"校准、schema 约束、无文本生成"的决策 front，跳过转写/字幕开销；② **joint schema head**（在 backbone 末层隐状态上做两阶段 attention routing：各选项先聚合证据，再跨全上下文交叉注意）输出**每选项一个 logit**；③ 训练 = **冻结 Qwen3 主干 + LoRA**，loss = **label-smoothed cross-entropy + Brier score 校准**；④ 内置 lexical grammar 保持选项语义；⑤ 对 schema 变化 / 字段顺序 / prompt 结构鲁棒。 |
| **链接** | [blog.cloudflare.com/clef-faster-cheaper-multimodal](https://blog.cloudflare.com/clef-faster-cheaper-multimodal/)；[developers.cloudflare.com/ai/models/@cf/cloudflare/clef-omni](https://developers.cloudflare.com/ai/models/%40cf/cloudflare/clef-omni/)；HF [huggingface.co/Cloudflare/clef-omni](https://huggingface.co/Cloudflare/clef-omni) |

---

## 四、交叉主题：决策模型（decision models）继续外扩

承接 10-11 期（Microsoft-Decision-1 / Liquid d1 / Perplexity Decider）主线，本周 **Cloudflare Clef 家族**把该类别从"文本/图像"推进到**全模态（含音频、带音轨视频）**：

| 模型 | 机构 | 日期 | 基座 / 形态 | 关键指标 |
|------|------|------|------------|----------|
| **Clef-omni** | Cloudflare | 10-09 | Qwen3-Omni-30B-A3B，30B-A3B MoE，Apache-2.0 | text/image/audio/video → 校准概率；21s 视频 ~1.5s；$0.15/M input |
| Clef / Clef-flash | Cloudflare | 10-上旬 | dense 图像/视频决策 | 降价 + 提速 |
| Microsoft-Decision-1 | Microsoft | 10-09 | Qwen3.5-9B post-train | 见 10-11 期 |
| d1-3B / d1-omni-600M | Liquid AI | 10-07 | LFM2.5 系 | 见 10-11 期 |
| Perplexity Decider v1 27B | Perplexity | 10-01 | Apache 2.0 | 见 10-11 期 |

**共同范式不变**：结构化输出 + **校准概率** + **无 token 生成（single forward pass）** + 低延迟低成本。Clef-omni 的新增维度是**把多模态感知并入决策前向**，并与"Jev from TypeSafe"（博客自述的决策模型首作）构成同一赛道谱系。

---

## 五、信号级：Google Gemini 4 "Carbon" 内部 checkpoint 泄露（Google DeepMind，2026-10-09）

| 字段 | 内容 |
|------|------|
| **中文标题** | 报道：Google 内部测试 Gemini 4 "Carbon"，编程"感觉像 Opus 5.5" |
| **英文标题** | Google's Gemini 4 "Carbon" model reportedly feels like Anthropic's Opus 5.5 coding performance |
| **发布机构** | Google DeepMind（**未官方确认**）；来源 Business Insider（作者 Hugh Langley），the-decoder / AI Weekly 等转述 |
| **模型名称** | `Carbon`（Gemini 4 内部 checkpoint 代号）；同族内部代号 **Argon / Barium**（公开版 Argon 内部称 **Barium-B**） |
| **发布日期** | 报道 2026-10-09 ~ 10-10（内部测试"recent days"，于 **Jetski** 编码平台） |
| **核心内容** | ① 内部文档/截图列 Gemini 4 内部代号 Argon / Barium / Carbon；② Carbon 部署于 **Jetski**（与 **Antigravity** 相关的内部编码平台）；③ **一名员工**称 Carbon 编程"**feels like Opus 5.5**"（并注明**仍需更多测试**），另一人留言"Carbon is really good!"，另有"new Gemini pro next model"；④ 早前 Argon 版本在部分编程任务上被比作较旧的 Opus 5。 |
| **可信度** | ⚠️ **低**——单源匿名**主观印象**，**无任何公开 benchmark / 任务集 / 评测描述**，Google **拒评**。参照数字（DeepSWE v1.1：Argon 77.9% / Opus 5.5 74.2% / GPT-6 Astra 74.1%）来自 **Argon launch table**，**属 Argon、非 Carbon**。不可等同于 Carbon 成绩。 |
| **链接** | [the-decoder.com/googles-gemini-4-carbon-model-is-reportedly-matching-anthropics-opus-5-5-coding-performance](https://the-decoder.com/googles-gemini-4-carbon-model-is-reportedly-matching-anthropics-opus-5-5-coding-performance/) |

---

## 六、Qwen-Image-2.1-Turbo（Alibaba Qwen，2026-10-09）

| 字段 | 内容 |
|------|------|
| **中文标题** | 阿里 Qwen 发布 Qwen-Image-2.1-Turbo：8 步 7B 图像生成/编辑模型 |
| **英文标题** | Qwen-Image-2.1-Turbo (8-step generation and editing) |
| **发布机构** | Alibaba Qwen |
| **模型名称** | `Qwen-Image-2.1-Turbo`（`Qwen/Qwen-Image-2.1-Turbo`） |
| **发布日期** | 2026-10-09（权重复用 base Qwen-Image-2.1，2026-09-20 发布） |
| **核心参数** | 沿用 base 的 **7B 视觉生成组件（32 层 single-stream DiT）**，attention 为 **block-causal**（`(q_idx >= kv_idx) or same_image_block`；文本 token-level causal、图像 chunk-level bidirectional）；**文本编码器 Qwen3-VL 8B**；**VAE = 64 通道 RGBA 自编码器（16× 空间压缩、原生透明）**；采样 **Flow Matching（Euler discrete + dynamic shifting）**。**8 步去噪**（base 默认 40 步，约 5× 步数削减），**CFG=1**，checkpoint 内置 8 步 schedule（`num_inference_steps` 单独传入不覆盖）。输出 **2K（2048×2048；预设至 2752×1536）**，支持**多参考编辑**。 |
| **主要创新点** | ① 同一 7B 生成器把去噪从 40 步压到 **8 步**，直接降推理成本；② 单一 checkpoint 覆盖 **2K 文生图 + 多参考编辑 + 透明 RGBA 输出**；③ **Pro/Turbo API 同日 GA**（阿里云 Model Studio，Turbo **CNY 0.1/图**，为 Pro CNY 0.25/图的 0.4×）；④ 工程前置条件：需 **Diffusers PR #14950**（pipeline-configured sampling sigmas）+ transformers 5.17+。 |
| **许可** | **Qwen Research License（非商用，商用自托管需另行许可）**；base Qwen-Image-2.1 在 Qwen-Image-Bench 得 **60.28**（厂商口径；Turbo 无独立分数）。 |
| **链接** | HF [huggingface.co/Qwen/Qwen-Image-2.1-Turbo](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo)；[github.com/QwenLM/Qwen-Image-2.1](https://github.com/QwenLM/Qwen-Image-2.1)；MarkTechPost 报道 [marktechpost.com/2026/10/09](https://www.marktechpost.com/2026/10/09/alibaba-qwen-releases-qwen-image-2-1-turbo-an-8-step-7b-image-model/) |

---

## 七、其他候选（未达收录门槛 / 待确认）

| 候选 | 机构 | 日期 | 状态 |
|------|------|------|------|
| Gemini app / AI Studio 新模式 | Google | 10-09 前后 | 与 Carbon 报道同周的 UI 信号，**无模型卡**，§5 已提及 |
| Qwen-Image-2.1 base（7B，60.28） | Alibaba Qwen | 09-20 | 早于窗口，**仅作 §6 参照** |

---

## 八、⚠️ 低可信传闻：Meta "Llama 4 Scout MoD re-release"（2026-10-11）

- **来源**：dev.to（作者 "TechBoss"，原 imtechboss.com）及多站聚合转发（chiprook / velocitystartups / shortsingh / worldprogramming / deniz.in），**均为二手 SEO/聚合内容**，**无 Meta/FAIR 官方 model card 或 HF 权重复核**。
- **传闻规格**：105B 总参 / 24B 激活、**Mixture-of-Depths（MoD）**动态深度路由、原生 **1M（1,048,576）token 上下文**（8 阶段渐进扩展）、**RingAttention + sliding-window MLA**、NIAH 99.8%（2,500 深度）、4-bit 24GB VRAM、官方 FP8 / INT4 AWQ、较 dense 70B 生成延迟 **−58%**、vLLM / Ollama / LM Studio / TGI 支持。
- > ⚠️ **CONTRADICTION**：官方 **Llama 4 Scout**（2025-04-05 发布）为 **109B 总参 / 17B 激活、16 experts、MoE（非 MoD）、10M token 上下文**。该 2026 传闻描述的 **24B 激活 + MoD + 1M 上下文** 与官方口径**系统性不一致**，且时间线（"re-release"）无官方佐证。
- **结论**：**不予采信**；在本 wiki 内标为**未证实传闻**，待 Meta 官方 model card 出现后方可升级。与 10-11 期 "Meta Llama 4 Scout MoD" 尝试搜索时的 429 阻塞呼应。

---

## 19 家目标机构窗口内（2026-10-11 → 2026-10-12）复核

| 机构 | 窗口内新报告 / 系统卡 | 备注 |
|------|----------------------|------|
| OpenAI | 无 | 最近 frontier 报告仍为 09-29 GPT-6 Sol |
| Anthropic | 无 | 最近为 10-09 agent 非预期行为报告（10-11 期已录） |
| Google DeepMind | **信号级（非发布）** | Gemini 4 "Carbon" 内部 checkpoint 泄露（§5，低可信）；Argon 仍限 Fairwind 试点 |
| Meta | **传闻（未证实）** | "Llama 4 Scout MoD re-release"（§8，低可信；与官方口径冲突） |
| Microsoft AI | 无 | Microsoft-Decision-1 见 10-11 期 |
| xAI | 无 | — |
| Mistral | 无 | Mistral Large 4 见 10-08/09/10/11 期 |
| DeepSeek | 无 | — |
| Alibaba Qwen | **有（邻近 10-09，非文本 frontier）** | Qwen-Image-2.1-Turbo（§6，图像生成/编辑） |
| ByteDance Seed | 无 | 最近论文 09-28 投稿（10-10 期已录） |
| Moonshot | 无 | — |
| Zhipu | 无（信号层） | GLM-5.4/5.5 见 10-10 期 |
| Tencent | 无 | — |
| Baidu | 无 | — |
| Amazon | 无 | Nova 2.5 Sonic 见 10-10 期 |
| NVIDIA | 无 | — |
| Cohere | 无 | — |
| AI2 | **有（邻近补录）** | Olmo Hybrid（§1）/ Bolmo in Nature（§2） |
| Perplexity | 无 | pplx-embed-v2-late 见 10-11 期 |

---

## 本期不重复收录（交叉引用）

- **Microsoft-Decision-1 / Liquid AI open d1 / Perplexity Decider v1 / pplx-embed-v2-late**：见 10-11 期 tech-report-digest。
- **Anthropic agent 非预期行为报告 / SemiAnalysis 中国安全披露普查**：见 10-11 期。
- **GLM-5.4/5.5（智谱，信号级）/ ByteDance Phase Sensitivity（arXiv:2609.36322）/ Amazon Nova 2.5 Sonic GA**：见 10-10 期。
- **Mistral Large 4 "Le Chonk" / Mistral docs Ministral 误读**：见 10-08/09/10/11 期。

---

## 口径与不确定性声明

- **窗口边界**：本页主窗口为 2026-10-11 → 2026-10-12；Ai2 Olmo Hybrid（论文 04 / recap 10-09）、Ai2 Bolmo（10-07）、Cloudflare Clef-omni（10-09）、Gemini Carbon（10-09/10）、Qwen-Image-2.1-Turbo（10-09）为**邻近补录**，均经 repo 级 grep（`Olmo Hybrid` / `Gated DeltaNet` / `Bolmo` / `Bwen` / `Clef-omni` / `Carbon` / `Qwen-Image-2.1-Turbo` 等）确认为 wiki 首见。
- **更新**：本页**首次为 Cloudflare 决策模型家族**建档（Clef / Clef-flash / Clef-omni），并**首次记录 hybrid（GDN）与 byte-level 两条架构支线**。
- **未独立复现**：所有性能/安全数字来自官方博客、model card、论文或一手媒体，**无第三方独立复现**。
- **低可信条目**：Meta "Llama 4 Scout MoD re-release"（§8）**未证实且与官方口径冲突**；Gemini 4 "Carbon"（§5）为**单源匿名主观印象，无 benchmark**。二者均不作为事实断言。
- **二手转述**："下一次 Olmo 预训练采用 hybrid MoE"来自 **COLM 2026 recap 转述**（非论文正文），标为 tentative。
- **厂商口径**：Qwen-Image-Bench 60.28 为 base Qwen-Image-2.1 的**厂商分数**（Turbo 无独立分数）；Gemini 4 DeepSWE v1.1 数字属 **Argon launch table**，非 Carbon。
