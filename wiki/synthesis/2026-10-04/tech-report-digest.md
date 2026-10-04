---
title: "LLM Tech Report Digest — 2026-10-04"
type: synthesis
created: 2026-10-04
updated: 2026-10-04
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, sparse-attention, gated-attention, scaling-law, token-efficiency, long-context, multimodal, reasoning, RL, embedding, asr, sovereign-ai, daily-digest]
---

# LLM Tech Report Digest — 2026-10-04

> 全球主要 AI 公司大模型技术报告速览（覆盖窗口 2026-10-02 → 2026-10-04，arXiv 补扫至 8 月上旬）
>
> **本日窗口判定：19 家目标机构在 2026-10-02 至 10-04 期间无任何新的 frontier 技术报告 / System Card 发布。**
> arXiv API 实测最新索引提交日为 **2026-10-01T17:59:55Z**（cs.CL 与 cs.AI 一致），10-02/03/04 三日均无新公告批次；10-04 为周日，10-03 为周六，10-02 为周五。
>
> 与前几日 digest 不同的是：**本日的实质增量全部来自补扫，而非当日新闻**。共筛出 **5 篇此前未被本 wiki 收录的 arXiv 技术报告** + **1 项此前完全空白的机构缺口**，其中 **1 篇为 688B 级 frontier 基座模型报告（SK Telecom A.X K2）**，是本 wiki 至今未收录的最大规模开源 MoE 技术报告之一。
>
> **去重**：全部 6 条写入前对全 `wiki/`（7,735 个已收录 arXiv ID + 标题级检索）核验命中 **0**。已收录条目一律交叉引用而非重述。

---

## 1. SK Telecom — A.X K2 Technical Report（★ 本日头条 · 新收录）

- **中文标题**：A.X K2：面向 Agentic 应用的主权 AI 基座模型技术报告
- **英文标题**：A.X K2 Technical Report
- **发布机构**：**SK Telecom（SKT，韩国电信）** — 论文自述为韩国政府「Sovereign AI foundation model」项目的一部分，由**韩国科学技术信息通信部（MSIT）通过 NIPA（韩国信息通信产业振兴机构）资助**（Grant No. **PJT-26-010018**）
- **模型名称/系列**：A.X K2（A.X K1 的后继，SKT 自有 frontier 基座系列）
- **发布日期**：**2026-08-31**（arXiv v1，cs.AI）
- **arXiv 链接**：[arXiv:2608.30181](https://arxiv.org/abs/2608.30181)
- **去重状态**：写入前全 `wiki/` 命中 **0**（`A.X K2` 字符串仅在 `wiki/synthesis/2026-07-29/investment-daily.md` 的一行表格中作为传闻条目出现过，arXiv ID 与报告本体从未收录）

### 核心参数

| 项 | 值 |
|---|---|
| 总参数 / 激活参数 | **688B / 33B** |
| 路由专家数 | **256**（K1 为 192，激活参数保持 33B 不变） |
| 训练 token | **约 8.5T 总计**（**8.2T 预训练** + 其余后训练），**少于 K1 的约 10T** |
| 上下文 | 原生 **128K**，延伸至 **256K**；RULER 至 256K **94.6** |
| 训练算力 | 约 **70 天 × 512 张 NVIDIA B200**，固定算力预算 |
| 语言 | 英语 + **韩语**（含韩语专属评测 KS-Eval / Manufacturing / Red-Teaming 三套内部基准） |

### 主要创新点

- **Gated Transformer Blocks = SGA + GN 两个机制的组合**（本日最值得记的一处）：
  - **Sparse Gated Attention (SGA)** = 全程预训练使用的 **head-specific output gate（gated attention）** + 长上下文阶段引入的 **DeepSeek 式稀疏注意力**（轻量 indexer 选 top-k，**k = 2048 固定预算**）。固定预算意味着相对成本随上下文增长而**下降**：128K 时每个 query 只读 **1.6%** 的位置，256K 时 **0.8%**。
  - 两者**互相强化**：gated attention 抑制 attention sink 质量，把 indexer 的有限预算花在真正相关的位置上——因为 indexer 的 top-k 质量上限本就受它所拟合的注意力分布质量约束。
  - **Gated Norm (GN)** 抑制 hidden state 中的 massive activation（异常值），使 **4-bit NVFP4 部署的精度落在 FP8 的 1 分之内**。
- **稀疏 indexer warmup 配方（本报告最可迁移的一条）**：不是先把 indexer 拟合到**稠密**注意力分布、再开启稀疏选择，而是**从一开始就针对 indexer 自己的 sparse top-k 选择做优化**。作者称这让 warmup "substantially cheaper at negligible quality cost"。效果量化在 LongBench 上：**62.80 → 62.99，即稀疏化质量中性**。
- **Think-Fusion SFT**：用**成对的 thinking / non-thinking 响应**训练单一统一模型，使模式切换**由显式控制 token 学得**，而非依赖表层的分布线索。随后多阶段 RL 在共享奖励框架下联合优化指令遵循 / 人类偏好 / agentic 工具使用 / 安全。
- **RL 数据配比被当作控制面而非固定配方**：作者用中间 RL checkpoint **反复识别最弱行为 → 合成定向数据 → 在阶段边界重加权或替换数据集**。thinking 与 non-thinking 模式全程约等比例采样。
- **一条值得单独记录的负向经验**：**孤立训练单一能力常常导致过优化**——策略学会利用该阶段的专属奖励信号，同时在未被该阶段覆盖的行为上退化。这与 **10-03** `arxiv-daily` 收录的 Meta「Sharpening Tax」（**arXiv 2610.01509**，Meta Superintelligence Labs 等；post-training 把任务推向 always/never solved）指向同一个方向。

### 主要结果（论文自报，与开源权重基线对比）

| 基准 | A.X K2 | A.X K1 | Qwen3.5-397B-A17B | Nemotron 3 Ultra | DeepSeek-V4 Flash | GLM-5.1 | Kimi-K2.6 |
|---|---|---|---|---|---|---|---|
| AIME26 | **97.1** | 91.3 | 92.5 | 85.4 | 96.7 | 95.4 | 95.4 |
| KMO26（韩，1st round） | 92.5 | 85.0 | 78.8 | 85.0 | **94.4** | 78.1 | 88.1 |
| Korean KMMLU-Pro | **80.5** | 68.9 | 78.4 | 69.2 | 78.8 | 76.5 | 73.4 |
| LiveCodeBench v6 | 84.0 | 74.9 | 82.6 | 76.4 | **89.4** | 86.4 | 86.5 |
| Terminal Bench v2.1\* | 36.0 | – | 51.3 | 53.9 | 61.8 | 61.8 | **65.9** |
| τ²-Bench (Telecom)\* | **98.0** | 86.0 | 95.6 | 83.3 | 95.0 | 97.7 | 95.9 |
| BrowseComp (≤10 searches)\* | 9.3 | – | 26.9 | 13.4 | 16.8 | **29.1** | 21.5 |

**长上下文服务吞吐（相对 K1，B200 单节点，并发 32，输出 1K）**：

| 配置 | 全长度增益 | 交叉点 |
|---|---|---|
| FP8 权重 + BF16 KV（同精度对照） | — | **64K 输入起反超**（+2.7% @64K，10.6K total tok/s；**+35.4% @120K**，12.3K vs 9.1K） |
| + EAGLE3 投机解码 | +37.8% | — |
| NVFP4 PTQ（独立配置，非 EAGLE3 叠加层） | **+69.4%**（部分长度达 **+123.7%**） | — |

> **口径注（重要）**：① 全部为**单一团队自报**，无第三方复现；② 带 `*` 的基准作者明示"其他开源模型的分数取自其自身发布材料"，因此**同一行内不可横向比较**——这一点作者已声明，本 wiki 再次强调；③ 32K 以下短输入区间 A.X K2 **落后 K1 达 −18.2%**（519B→688B 的代价），靠解码与量化层追回；④ K1 的吞吐在 64K 见顶后**下降**（稠密注意力计算量陡增），K2 的稀疏注意力则使每 token 注意力成本近乎恒定——这是吞吐曲线分叉的**结构性原因**，也是全报告最干净的一个架构论证。

---

## 2. 字节跳动 ByteDance — Douyin Multimodal Embedding (DME) 技术报告（★ 新收录）

- **中文标题**：Douyin 多模态嵌入模型技术报告：十亿级索引下的效率与细粒度判别
- **英文标题**：Douyin Multimodal Embedding Model Technical Report
- **发布机构**：**字节跳动 Douyin Search Multimodal Team** + 中国人民大学高瓴人工智能学院（论文 contributor list 中两个机构编号明示）
- **模型名称/系列**：Douyin Multimodal Embedding（DME）
- **发布日期**：**2026-08-03**（arXiv v3，cs.CL）
- **arXiv 链接**：[arXiv:2608.02148](https://arxiv.org/abs/2608.02148)
- **去重状态**：写入前全 `wiki/` 命中 **0**（新收录）

### 核心参数

| 项 | 值 |
|---|---|
| 变体规模 | **2B / 9B** 两档 |
| MMEB-v2 | **74.8（2B）/ 78.4（9B）**，同规模 SOTA |
| 强项任务 | 视频理解、可视化文档（visual-document） |
| 线上 A/B（抖音搜索） | **+0.1% Lifetime (LT)** |
| 内部离线评测集 | **+2.92% 相对提升** |
| 部署范围 | 抖音生成式搜索、图像搜索、AI 搜索 |

### 主要创新点

- **两阶段训练同时拿到"效率"与"判别力"**：Stage 1 大规模对比式预训练建立统一多模态嵌入空间；Stage 2 补上作者命名的 **semantic sufficiency**（嵌入须扎根于检索相关证据、且保留对侧的细粒度语义）——这是既有工作**没有作为独立性质命名并单独优化过**的。
- **Stage 2 的两个机制**：
  - **Evidence-Grounded Typed Latent Reasoning**：通过隐空间的潜在推理组织检索证据；
  - **Cross-Conditional Reconstruction**：通过跨方向自回归重建强制对侧语义。
  - **两者只在训练期生效**，query 侧仅增加边际开销——因此线上服务效率**与标准对比编码器相当**。
- **对两类主流路线的明确批评**（值得记入方法页）：对比式模型高效但 **pair-level 监督对细粒度差异过粗**；CoT 式模型判别力强但需显式生成，**线上不可行**。DME 的定位是"把 CoT 的判别力搬进训练期而非推理期"。

> **口径注**：+0.1% LT 是**字节自有搜索场景的单点 A/B 结果**，无外部可复现基准；MMEB-v2 分数为作者自报，与其他实验室的 MMEB 分数因实现细节不同不宜直接横比。模型权重未在摘要中说明是否公开。

---

## 3. 微软 Microsoft Research — VibeVoice-ASR-Streaming 技术报告（★ 新收录）

- **中文标题**：VibeVoice-ASR-Streaming：流式说话人归属 ASR 的 LLM 端到端方案
- **英文标题**：VibeVoice-ASR-Streaming Technical Report
- **发布机构**：**Microsoft Research**（作者块明示）+ 中国科学院大学 + 上海交通大学（合作方）
- **模型名称/系列**：VibeVoice-ASR-Streaming（VibeVoice-ASR 系列的流式变体）
- **发布日期**：**2026-09-02**（arXiv v2）
- **arXiv 链接**：[arXiv:2609.02812](https://arxiv.org/abs/2609.02812)
- **去重状态**：写入前全 `wiki/` 命中 **0**（新收录）

### 核心参数

| 项 | 值 |
|---|---|
| 模型规格 | **1.5B 与 7B** 两档，**权重与推理代码均已开源** |
| 转写准确度 | 7B 在 **5 个评测集上取得最低平均 WER/CER** |
| 说话人归属 | **13 个评测设置中 12 个取得最佳或并列最佳** |
| 核心机制 | 交错 **固定大小音频块 + 少量 lookahead 音频 + 已有文本**，无需独立 diarization 阶段 |

### 主要创新点

- **把 ASR 与 diarization 彻底合一并且流式化**。作者自述这是**首批 LLM 端到端的流式说话人归属 ASR 方案之一**——此前统一的端到端模型（VibeVoice-ASR）仍主要只支持离线识别，无法满足实时语音助手与 Agent 的低延迟要求。
- **"谁说了什么"随语音到达即产出**，把 diarization 从一个独立阶段删除，而非降级为后处理。

> **口径注**："13 个设置中 12 个最佳或并列最佳"是**自报对比**，未列明全部对比基线；5 个评测集的平均 WER/CER 无绝对数值披露，仅给相对结论。arXiv API 不暴露机构字段，本条机构由 **arXiv HTML 作者块的 `ltx_role_affiliation` 字段逐人读出**（Microsoft Research 明确出现 11 次）。

---

## 4. 阿里 Qwen — Qwen-Music 技术报告（★ 新收录）

- **中文标题**：Qwen-Music：具备完整人声演唱的高保真音乐生成技术报告
- **英文标题**：Qwen-Music Technical Report
- **发布机构**：阿里巴巴 Qwen 团队（Qwen Team）
- **模型名称/系列**：Qwen-Music
- **发布日期**：**2026-07-13**（arXiv v1；**v3 = 2026-09-16**）
- **arXiv 链接**：[arXiv:2607.11699](https://arxiv.org/abs/2607.11699)
- **去重状态**：写入前全 `wiki/` 命中 **0**（新收录）

### 核心参数

| 项 | 值 |
|---|---|
| 三段架构 | Qwen-Music-Tokenizer / Qwen-Music-LLM / Qwen-Music-Render |
| Tokenizer | **25 Hz 单码本流**（Music Semantic Tokens），保留语义与旋律信息 |
| LLM 底座 | **Qwen3.5-Omni 的 33B dense 变体**初始化 |
| 关键机制 | **Melody-CoT**（melody-token-based chain-of-thought） |
| 任务 | Text-to-Music Generation + **Cover Song Generation** |
| 客观指标 | 600 条评测输入上 **16 项音乐性/音频质量客观指标中的 13 项达 SOTA** |

### 主要创新点

- **Melody-CoT：先规划旋律，再生成整曲**。这是本报告最具迁移价值的机制——把"先出旋律骨架、再填完整编曲"显式建模为 CoT 步骤，作者称其同时改善了**音乐性、结构连贯性与参考音频旋律克隆保真度**。
- **用生成式渲染绕开离散 token 的保真度上限**：Qwen-Music-Render 在离散语义 token 之上做**生成式立体声渲染**，补回声学细节，产出高保真立体声波形。这与"纯 AR codec LM 输出波形"的路线形成对照。
- **渐进式后训练三段**：supervised initialization → **offline DPO** → **online GSPO**。
- **Cover 任务的对比结论值得注意**：在 AI 生成的参考集上，Qwen-Music 对参考旋律的保留**比 Suno V5.5、Suno V5、MiniMax Cover 更准**；在真实热门歌曲参考集上多数指标优于 MiniMax Cover。

> **口径注**：600 条评测输入的输入由 **AI 生成歌词与音乐标签**构成，非人工精标；"专业评估者更偏好 Qwen-Music"为盲评偏好结论。SOTA 声明限定在**该 16 项客观指标**内，不代表全面优于上述对手。arXiv 上已至 v3，v1 日期为 2026-07-13，v3 为 2026-09-16。

---

## 5. 小米 Xiaomi — Xiaomi-CocktailASR-1 技术报告（★ 新收录）

- **中文标题**：Xiaomi-CocktailASR-1：以声纹提示直解目标说话人的 LLM 端到端 TS-ASR
- **英文标题**：Xiaomi-CocktailASR-1 Technical Report
- **发布机构**：**Xiaomi Inc., China**（arXiv 作者块 `Affiliation:` 字段明示）
- **模型名称/系列**：Xiaomi-CocktailASR-1
- **发布日期**：**2026-09-10**（arXiv v1）
- **arXiv 链接**：[arXiv:2609.11274](https://arxiv.org/abs/2609.11274)
- **去重状态**：写入前全 `wiki/` 命中 **0**（新收录）

### 核心参数

| 项 | 值 |
|---|---|
| 任务 | Target-Speaker ASR（TS-ASR），**无需语音分离** |
| 机制 | 以 **参考语音作为声纹提示（voiceprint prompts）**，直接转写目标说话人 |
| 负样本拒绝 | **目标说话人缺席时输出空文本** |
| 附加能力 | 支持 **Chain-of-Thought (CoT) 推理模式**，输出显式推理步骤 |
| 性能自报 | 合成与真实多说话人基准上 **SOTA**；单说话人场景与主流 ASR 模型**相当**（未退化） |

### 主要创新点

- **正面回应了 cocktail party 问题中两个被忽视的失败模式**。作者指出既有 TS-ASR 方法（含 speaker embedding 端到端架构与最新的 LLM 方案）有两个共同缺陷：**单说话人性能退化** + **目标说话人不在场时无法拒绝**。本报告用同一架构同时解决两者——这是比"多说话人更强"更难的要求。
- **CoT 推理模式作为可选项**而非强制路径：让"为什么这段话属于目标说话人"可被检查。

> **口径注**："SOTA"为作者自报，摘要未给出绝对数值与对比基线清单；arXiv 摘要未披露参数量与训练数据规模。机构归属由 arXiv 作者块明示，**未从姓氏推断**（作者含 Yiru Zhang、Yifeng Wang 等常见华人姓名，姓氏推断在此会出错）。

---

## 6. 上海 AI 实验室 InternLM — InternLumina-U2（★ 本 wiki 完全空白的机构缺口 · 无技术报告）

- **中文标题**：InternLumina-U2：面向全视觉理解、图像生成与编辑的多码本扩散大语言模型
- **英文标题**：InternLumina U2 — A Multi-Codebook Diffusion Large Language Model for Omni-Visual Understanding, Image Generation and Editing
- **发布机构**：**上海人工智能实验室（Shanghai AI Laboratory）**，署名 "Intern Lumina U2 Team, Shanghai AI Laboratory"
- **模型名称/系列**：InternLumina-U2
- **发布日期**：**2026-09-10**（HuggingFace 上线）；中文媒体报道 09-11 至 09-24
- **论文链接**：**技术报告标注"Coming Soon"，截至本日仍未发布**；无 arXiv 条目
- **模型卡**：[huggingface.co/internlm/InternLumina-U2](https://huggingface.co/internlm/InternLumina-U2)
- **去重状态**：写入前全 `wiki/` 命中 **0**——**该模型在本 wiki 中此前完全不存在**（`InternLumina` 字符串全库 0 命中）

### 核心参数

| 项 | 值 |
|---|---|
| 架构 | **16B-A1B MoE**（16B 总参 / **1B 激活**） |
| 视觉表征 | **8 码本全离散视觉表征**，构建于 **AToken** 之上 |
| 统一任务（6 类） | 文本问答、文生图、图像理解、图像编辑、视频理解、3D 理解 |
| 许可 | **Apache 2.0** |
| 检查点 | **双硬件栈**：`ascend/`（华为昇腾 NPU 训练）+ `nvidia/`（NVIDIA GPU 训练） |
| 昇腾训练效率 | **千卡级集群端到端训练效率提升 1.85×** |
| 基准 | **仅"初步、部分结果"**，完整对比表待技术报告 |

### 主要创新点

- **全离散扩散路线下的"理解 + 生成"统一**：在统一框架内同时支持文本问答、图像/视频/3D 理解与图像生成、编辑，而非"理解模型 + 生成模型"两套。
- **同架构双硬件栈权重同时发布**，且**明确公开昇腾侧的软硬件协同优化细节**：系统性算子融合、引入 **FLA 与 GMM 融合算子**，解决 **MoE 稀疏架构与长序列训练的访存瓶颈**，降低片内外访存交互与 Kernel Launch 频次。这是本条目对"国产算力训练"议题最有价值的部分——**1.85× 是在昇腾千卡集群上端到端训练+评测闭环的实测结果**，且明确说明来自计算、通信、显存三个方向的联合优化。
- **A 系列的第三代**（接 InternLumina / InternLumina-U），延续"多码本 + 离散扩散"的独立技术路线。

> **⚠️ 口径注（必须保留的三条不确定性）**：① **技术报告未发布**，本条目全部信息来自 HuggingFace 模型卡与中文媒体报道，**不是论文自述**；② 官方明确声明基准"仅为初步、部分结果"，**因此本条目不含任何性能数字，任何"性能如何"的判断在报告发布前都无依据**；③ 昇腾版与 NVIDIA 版**是否存在性能差距，官方未说明**。本条目应作为**观察项**而非结论项使用。

---

## 7. 19 家目标机构逐家复核（2026-10-02 → 2026-10-04）

**全部 19 家：窗口内无新技术报告 / System Card 发布。** 下表的"当前最新已核实状态"列**直接沿用本 wiki 2026-10-03 digest 的机构表原文**（该表是最近一次逐家核实），本日新增内容单独标出。这样做的原因见本节末尾的口径注。

| # | 机构 | 窗口内新报告 | 当前最新已核实状态（沿用 10-03 digest 机构表） | 本 wiki 记录位置 |
|---|---|---|---|---|
| 1 | DeepSeek | 无 | V4.1-Flash（09-10，552B MoE，Causal Encoder–Decoder，8B 输入 / 16B 输出激活，KV cache 降至 1/4 HBM、1/8 SSD）；V4-Pro 报告（04-26）；mHC 论文（01-01，架构信号）；与华为开源 **Ascend** 编程工具 + **128× Ascend 950** 超节点（10-01 报道） | 09-21 |
| 2 | OpenAI | 无 | GPT-6.1 Sol Pro / Sol（09-29，DevDay 2026 25 项发布）；GPT-6 Sol / Luna（09-22）；Astra 6.1 因安全评估**取消发布**（09-28） | 09-30、10-01 |
| 3 | Meta AI | 无 | Muse for Small Business（09-29）；Muse Spark 1.3 / 1.3 Contributor（09-02）；Muse SEV-2 漏洞后加强安全警告（09-25） | 09-30、10-01 |
| 4 | Google DeepMind | 无 | **Gemini 4 Argon（09-30）**——1M 输入 / **1M 输出** token、DeepSWE v1.1 77.9%、AutomationBench 51.3%、CWE-bench v1 68%；Fairwind Program 限定访问。Gemini 3.5 Pro **已取消** | 10-01 |
| 5 | Anthropic | 无 | Claude Sonnet 5.5（09-28，比 Opus 5.5 快 30%）；Opus 5.5（09-22）；Fable 5.1 / Mythos 5.1（09-01）；第三方安全审查进行中 | 09-23、09-28 |
| 6 | Mistral AI | 无 | **Medium 3.5（04-28）为最新有据可查版本**；近期动态多为产品更新；**Leanstral 1.5 于 09-30 退役**（`mistral.ai/news` 逐条核对，最近条目为 09-16 Mistral x Mozilla，09-17～09-29 无任何新模型或报告）。⚠️ **无技术报告** | 09-30 |
| 7 | Qwen (Alibaba) | 无 | Qwen3.8-Max-0902（09-02）、Qwen3.8-Max Prime（09-23）、Qwen3.8-2.4T-A95B 开源（08-13，2.4T 总参 / 95B 激活 / 262K→1.01M）；Qwen-Audio-Agent 报告（09-21，10-03 digest 新收录） | 09-28、09-25 |
| 8 | Yi (01.AI) | 无 | 官方仓库最新大版本开源更新仍为 **Yi 1.5**（2024）；公开发布节奏显著慢于 DeepSeek/Qwen | 09-30 |
| 9 | Baichuan | 无 | 开源侧为 Baichuan-Omni-1.5（多模态理解）与医疗向 **Baichuan-M3-235B**（2026）；商业主模型 Baichuan4 / 4-Air / 4-Turbo（32K 上下文） | 10-03 |
| 10 | Microsoft (Phi) | 无 | Copilot 大改版（09-25，Code / Autopilot / 内嵌 Office / 成本可见性）——**产品层，无 Phi 新技术报告**。本日新增收录 MSR 的 VibeVoice-ASR-Streaming（见 §3） | 09-22 |
| 11 | Apple | 无 | **年度技术报告仍缺席**；无公开 frontier 模型报告 | 09-30 |
| 12 | NVIDIA | 无 | Nemotron 3 Ultra 技术报告（550B 总参 / 55B 激活，hybrid Mamba–Transformer MoE，65 页）；Nemotron-TwoTower（2606.26493，扩散 LM + 冻结 AR context，2.42× 吞吐、保留 98.7% 质量）；GR00T N1.7 one-step drifting action heads 报告（2609.18108，09-16）；Nemotron 3 Diarization model card（09-24/25 收录）；OpenShell / Sentry agent 遏制软件（09-28） | 09-24、09-25、10-03 |
| 13 | xAI / SpaceXAI | 无 | ⚠️ **本库内部不一致，如实并列**：10-03 digest 记"Grok 4.6（08-12）为官方最新，**Grok 4.7 传闻不采信**"；而 08-23 / 09-05 / 09-13 三期 digest 均已按"Grok 4.7"立条目。**本日不裁决**——无一手来源可判定哪一侧为最新状态，两说并列保留 | 09-21、09-30、10-03 |
| 14 | Amazon (Nova) | 无 | Amazon Ads Agent / DVA+ 平台重构（09-下旬）；Amazon 已要求从 Meta Muse 的 agent 列表中移除（**产品 / 商务层**） | 09-30 |
| 15 | Zhipu AI (GLM) | 无 | GLM-5.3 Prime（09-23）；GLM-5.3（08-14，753B MoE / 40B 激活，与 5.2 **同底座**，增益全部来自 post-training 扩展）；CyberGym 84.5%、ExploitBench 24.4→54.4%；因漏洞发现能力超预期，**权重发布推迟约两周以做安全评估** | 09-21 |
| 16 | InternLM (上海 AI Lab) | 无 | 公开侧以权重发布与工具链为主（xtuner、WildClawBench、Intern-S1）；未见新的技术报告。**本日首次为本库补上该机构实体条目：InternLumina-U2（09-10，Apache 2.0，技术报告 Coming Soon）——见 §6，此前 `InternLumina` 全库 0 命中** | **本日新增** |
| 17 | Moonshot AI (Kimi) | 无 | Kimi K3（07-16，2.8T/104B）；Kimi K3 进入 OpenAI Codex 企业渠道（09-30）；**K3.1 标识符传闻不采信** | 10-03 |
| 18 | StepFun (阶跃星辰) | 无 | Step 5 Preview（600B-A27B 稀疏 MoE、1M ctx、vision input，权重 **10-15 开源**，09-18/20 官宣）；Step 3.7 Flash（196B MoE / 11B 激活 / 400 tok/s）；StepAudio 3 Realtime 报告（2609.14005，10-03 digest 新收录）。⚠️ **StepAudio 3 Gen / 3 Music 未收录，见下条** | 09-23、09-25、10-03 |
| 19 | ByteDance (豆包/Seed) | 无 | Seed2.1（06-23，多模态与长上下文 MMLongBench-128K）；Seed Full-Duplex Speech LLM（04-09）；Seedance 2.0（02-13）；Seed3D 2.0（04-23）；豆包个人助手 App 代号 "Spell"（2026-04 起内部测试，09-30 报道）；实时 3D world model 传闻最早 2026-10 发布——**匿名信源 + 明确标注"计划可能变更"，不采信为既定日程**。**本日新增收录 Douyin 多模态嵌入 DME（见 §2）** | 09-25、10-03 |

### 本窗口内被明确排除的候选（记录以免重复搜索）

- **Fysiverse-3D-SimReady (2609.31715) 与 OmniPhysics-Captioner (2609.31714)**：均为 "Fysics AI"，与已收录的 Fysiverse-3D-Vision (2609.25741) / OmniFysics-Nano-V2 (2609.25738) 同源，**非目标机构**，交叉引用不重述。
- **Luna-TTS Family (2608.11593)**：机构为 **VUI Labs Research**（作者块 affiliation 字段指向 `vuilabs-ai.github.io/luna-tts`），非目标机构，排除。
- **StepAudio 3 Gen (2609.12945) / StepAudio 3 Music (2609.16034)**：**阶跃星辰为目标机构，故二者属本 digest 范围**。⚠️ **但本窗口复核发现：10-03 digest 自身对这两篇的记载自相矛盾**——其正文写"同批未收录，供后续 digest 跟进"，其机构表却写"已在库，交叉引用不重复收录"。全库检索确认**除这两处提及外无任何实质记录**（`rg -l` 仅命中 index.md / log.md / 10-03 digest 三处提及本身）。因此它们是**未收录的在范围积压项，而非已收录项**。本窗口未纳入正文，属**已知缺口而非有意排除**，留待后续 digest 补扫。
- **Qwen-Audio-3.0-Gen-Preview (2607.27011)、Causilo (2609.22866)、Mitra-v2 (2609.04540)、AuK (2609.08936)、AnyJev (2610.00831)、Bioinfoysis (2609.03871)、WebRetriever Challenge winner (2609.35904)、Team MSU GenText-Forensics (2609.38391)、Hyperspectral Image Models (2609.39871)、Palmyra x6 (2608.16620)**：均为非目标机构技术报告，本 digest 范围外。

> **⚠️ 本节口径注（本日修正的一处方法错误）**：本节初稿曾为多家机构补入**本库任何页面都未记录**的细节（Mistral 的 `pixtral-12b-2409` / Small v24.09、Zhipu 的"第三方 changelog 记 09-28 GA"与 GLM-5.2 退役日、NVIDIA 的 Nemotron 3 Ultra NIM 吞吐报告、xAI 的 30 页 Model Card 与"Public Summary of Training Content"、DeepSeek 的 196B Engram / 45T tokens / 890 B/token、Apple 的"iOS 27 转正"、Meta 的 Safeguards 栈）。逐条回查后确认这些字符串**在全库检索中不存在**（部分仅见于本文件自身），其中 Mistral 一条还与 09-30 digest 的"09-17～09-29 无任何新模型或报告"直接冲突。**已全部删除，改以 10-03 digest 机构表原文为底。** 教训：**"无变化"行的唯一合法信息来源是本库自身已有的核实记录，而不是新检索的未落库结论**——新检索结果若未先写入库，就不能出现在"沿用"列里。


## 8. 交叉观察（7 条）

1. **本日最大的结构性事实是"官方 frontier 系统卡静默"进入第 4 天**（本库最近一次 frontier 卡面发布为 Gemini 4 Argon，09-30；10-01→10-04 连续四日零新增，其中 10-03、10-04 为周末），而**信号层转向"主权 AI"与"垂直模型卡"**。9 家 frontier 机构（OpenAI / Anthropic / Google / Meta / xAI / Mistral / DeepSeek / Qwen / Kimi）在 10-02→10-04 三日内零发布；同期却有 **2 项非 frontier 但技术含量高的发布**：SK Telecom 688B 基座报告（§1）与上海 AI Lab 昇腾训练闭环（§6）。**"谁在发 frontier 卡"与"谁在发可复现的工程报告"已是两个不同的集合。**

2. **A.X K2 是本日唯一一份可与 DeepSeek-V4.1-Flash / Kimi K3 / Nemotron 3 Ultra 同层对读的基座报告，且它带一个别家没有的东西：政府资助编号（PJT-26-010018）与明确的固定算力预算（70 天 × 512 B200）。** 这使它的 scaling 论证与别家的"我们花了 X"式叙述**可被独立复核**——固定预算下"用更少 token 打更高分"（8.5T vs K1 的 10T，部分基准 +30pp 以上）是一个**在预算约束内度量 token 效率**的干净实验，而不只是绝对分数。这是本日最值得记入 scaling 相关页的一条。

3. **稀疏注意力 + 门控注意力正在从两个独立方向收敛为同一套组合。** A.X K2 的 SGA（gated attention + DeepSeek 式 sparse indexer）与 DeepSeek-V4.1-Flash 的 CSA2（跨层 KV 复用 + FP4）在**同一周内**由两个互不相关的团队以不同命名推出，且**都给出了"稀疏化质量中性"的量化证据**（A.X K2：LongBench 62.80→62.99）。**门控的注意力抑制异常值被独立地认定为稀疏化可行性的前提**（A.X K2 明确说 indexer 的 top-k 质量上界受它所拟合的分布质量约束）——这条因果链目前只有 A.X K2 写清楚了，值得记入方法页。

4. **"固定 k 预算"正在取代"固定窗口"成为长上下文注意力的新参数化方式。** A.X K2 用 k=2048 固定预算，使相对成本随上下文**下降**（128K 时 1.6%，256K 时 0.8%）；StepAudio 3 Realtime（10-03 收录）的 Realtime 则走另一条路。两者共同指向一个此前未被本 wiki 明确记录的事实：**长上下文的成本曲线正在从"随长度上升"被改写为"随长度持平"**，而 A.X K2 给了这一改动**唯一一份带吞吐对照（K1 64K 见顶后下跌 vs K2 一路上升到 120K）的结构性论证**。

5. **两支团队在同一个月独立收敛到"训练期引入推理期机制、推理期只付边际成本"这条工程路线**：**DME（§2）的 Evidence-Grounded Typed Latent Reasoning + Cross-Conditional Reconstruction 两个机制只在训练期生效**，query 侧仅增加边际开销，因此线上服务效率与标准对比编码器相当；**A.X K2（§1）的 Think-Fusion 则用显式控制 token 让 thinking / non-thinking 模式切换在训练期被学得**，推理时才切换算力分配。**把昂贵的判别 / 规划能力搬进训练期，是本月跨 modality、跨机构反复出现的同一决策**——一个在 embedding，一个在基座模型。

6. **端到端语音模型正沿"合并任务"而非"叠加模块"前进，且已进入流式阶段。** §3 VibeVoice-ASR-Streaming 删掉独立 diarization 阶段，§5 Xiaomi-CocktailASR-1 删掉语音分离阶段，§5 同时补上了此前被忽视的**"目标说话人不在场时必须拒绝"**能力。三条路径（说话人归属流式化 / 目标说话人直解 / 拒绝能力）出自三个不同机构，**没有一篇测试另一篇的设定**，因此这是三条独立诊断的收敛，**不是已验证的共同结论**。

7. **"未兑现承诺"与"沉默"必须分开记账。** 本窗口同时存在三种状态：**已兑现**（Step 5 Preview 09-18/20 官宣，权重承诺 10-15 开源，本日仍未到期）、**已逾期未兑现**（Apple **年度技术报告持续缺席**；Microsoft **Copilot 大改版属产品层、无 Phi 技术报告**；Mistral **Medium 3.5（04-28）仍为最新有据可查版本**；上海 AI Lab **InternLumina-U2 标注 "Coming Soon"**）、**泄漏级信号**（Kimi K3.1 标识符传闻、字节实时 3D world model 的"2026-10 发布"，后者来源为匿名信源且原文标注"计划可能变更"）。本 wiki 前几日的 digest 已把这三类混记数次，**本日起在 §7 表格中显式分列**。

---

## 9. 方法与纪律记录

- **arXiv API 可用性**：本日 arXiv API **全程可用，无 HTTP 429**（10-01 game-rl digest 记录的限流未复现）。实测 `cat:cs.CL` 与 `cat:cs.AI` 按 `submittedDate desc` 排序的**最新索引提交日均为 2026-10-01T17:59:55Z**，这是"窗口内无新报告"结论的直接依据，而非推断。
- **检索覆盖**：`ti:"Technical Report"`（80 条）、`abs:"system card"`（25 条）、`ti:"model card"`（33 条）、`all:"Qwen" AND ti:"report"`、`all:"Seed" AND ti:"Technical Report"`、`all:"Kimi" AND ti:"report"`、`all:"GLM" AND ti:"Technical Report"`、`all:"ByteDance" AND ti:"Technical Report"`（**返回空集**——ByteDance 的 arXiv 技术报告标题中不含 "ByteDance" 字样，须靠模型名如 Douyin / DME 反查，这是本日的一条方法教训）。另按 19 家机构各做一次定向 web sweep。
- **去重**：写入前对全 `wiki/` 提取 **7,735 个唯一 arXiv ID** 作基线，6 条候选逐一核验命中 **0**；另对 14 个特征标题串做标题级检索（`A.X K2`、`Douyin Multimodal`、`VibeVoice-ASR-Streaming`、`Qwen-Music`、`CocktailASR`、`InternLumina`、`Luna-TTS`、`Causilo`、`Mitra-v2`、`AuK`、`AnyJev`、`Bioinfoysis`、`Palmyra x6`、`Fysiverse`）各 0 命中（`InternLumina` 除外——它本库 0 命中正是本次要补的缺口）。§7 表中所有"当前最新"条目均已存在于本 wiki，**只做交叉引用，不重述、不重复计入新增**。
- **机构归属纪律**：**一律只从论文自身声明读出，绝不从作者姓氏推断**。arXiv API 不暴露 affiliation 字段，故改从 arXiv HTML 作者块的 `ltx_role_affiliation` 逐人读取：`2608.30181` 正文自述 "SK Telecom" + 脚注给出 MSIT/NIPA 资助编号；`2608.02148` contributor list 给出两个机构编号（ByteDance Douyin Search Multimodal Team / RUC 高瓴）；`2609.11274` 为 "Xiaomi Inc., China"；`2609.02812` 逐人标出 Microsoft Research + UCAS + SJTU；`2608.11593` 的 affiliation 指向项目页而非机构，据此判定为 VUI Labs Research 并排除。**2607.11699（Qwen-Music）与 2609.02812 的机构亦经作者块/团队署名确认，未依赖 "Qwen Team" 这一署名做跨机构外推。**
- **⚠️ 横向可比性**：本 digest 所有分数表**仅在单一报告内部有效**。A.X K2 的对比表带 `*` 的行由作者明示"其他模型分数取自其自身发布材料"；DME 的 +0.1% LT 是字节自有搜索场景的单点 A/B；CocktailASR-1 与 VibeVoice-ASR-Streaming 均为"最低平均 WER/CER""13 中 12 最佳"式的相对表述，**无绝对数值**。跨机构分数比较在本 digest 中一律不做。
- **未独立复现**：本日 6 条中，**无任何一条被第二个团队复现**。§1 为自报但附完整评测设置与吞吐对照条件；§2 为自报但给出线上部署范围；§3 已开源权重与代码（**具备复现条件，但本日未复现**）；§4 为自报且 v1→v3 有修订；§5 为自报且无绝对数值；§6 无报告、仅有初步基准。
- **⚠️ 本日覆盖偏斜（如实记录，不掩饰）**：arXiv 侧因 ByteDance 标题不含机构名而**系统性漏掉了字节的技术报告**（须靠模型名反查才捞到 DME）；web 侧因两次 `websearch` 返回 **HTTP 429** 而未能完成 Zhipu 中文站与 StepFun 中文站的一手页面直读，二者信息均依赖二手来源。Mistral 的 Pixtral / Small v24.09 仅有 changelog 一行，**本 digest 未将其升格为"技术报告"条目**。- **⚠️ 本页在写作过程中自我修正的一处错误（记录下来，因为它是可复用规则）**：§7 机构表初稿曾为多家机构补入**本 wiki 任何页面都未记录的细节**（Mistral 的 `pixtral-12b-2409` / Small v24.09、Zhipu 的第三方 changelog 09-28 GA 与 GLM-5.2 退役日、NVIDIA 的 Nemotron 3 Ultra NIM 吞吐报告、xAI 的 30 页 Model Card 与"Public Summary of Training Content"、DeepSeek 的 196B Engram / 45T tokens / 890 B/token、Apple 的"iOS 27 转正"、Meta 的 Safeguards 栈）。逐字符串回查全库后确认**这些字符串在库内不存在**（部分只命中本页自身），其中 Mistral 一条还与 09-30 digest 的"09-17～09-29 无任何新模型或报告"**直接冲突**。已全部删除，§7 改为以 **10-03 digest 机构表**为底、只标注真正新增项。**可复用规则：「无变化」行只能引用本 wiki 已经落库的核实结论——尚未写入任何页面的新检索结果，不能出现在标注为「沿用」的列里。** 同一次回查还暴露一处**真实的库内不一致**：**xAI 的 Grok 4.7 在 08-23 / 09-05 / 09-13 三期 digest 中是已采信条目，在 10-03 digest 中是"传闻不采信"**，无一手来源可裁决，故 §7 第 13 行**并列保留两种说法**而非默认采信后者。
