---
title: "LLM Tech Report Digest — 2026-10-13"
type: synthesis
created: 2026-10-13
updated: 2026-10-13
sources: []
tags: [tech-report, LLM, technical-report, model-card, system-card, meta, muse-wonder, agentic-models, active-memory, artificial-analysis, anthropic, distillation-defenses, watermarking, quantization, w2a4kv2, openai, textgrain, canonq, eu-ai-act, daily-digest]
---

# LLM Tech Report Digest — 2026-10-13

> **窗口判定：2026-10-12 → 2026-10-13。** 本期是久违的**"frontier 卡面回归"**——Meta 于 **10-12** 发布其**首个 frontier 模型** Muse Wonder / Muse Wonder Full（含 model card），Anthropic 同日发布 **distillation 防御**研究。这是自 09-29 GPT-6 Sol、09-28 Claude Sonnet 5.5 以来，19 家目标机构在 frontier 侧**首次出现真正的新 model card**。此外补录两条 10-上旬的**架构/效率级**发布（OpenAI textGrain 10-05、Meta CanonQ 10-06），均经 repo 级 grep 确认为 wiki 首见。

> **本期主线：① agentic frontier 的"记忆 + 专注"范式**（Muse Wonder 的 Active Memory / Active Focus）；**② 前沿实验室对"能力外流"的工程反制**（Anthropic distillation 防御三件套）；**③ 文本水印**（OpenAI textGrain）与 **极端低比特压缩**（Meta CanonQ）两条独立技术线。

---

## 本期要点（相对 2026-10-12 新增/更新）

- ★★★ **Meta Muse Wonder / Muse Wonder Full（Meta，2026-10-12）**——**Meta 首个 frontier 模型，面向"个人 + 专业"agent**。同族一体发布：**Muse Wonder**（走 Meta Model API + Muse Code）与 **Muse Wonder Full**（**仅 Muse Code 订阅者，不走 API**）。核心能力主张两条：**Active Memory**（跨对话携带重要上下文、按需主动检索）与 **Active Focus**（持续朝目标推进、试替代方案、处理 blocker、需要时澄清、重要动作前确认）。**Artificial Analysis Intelligence Index v4.3：Wonder Full (max)=56，Wonder (max)=52**（对照 Muse Spark 1.3 max=48，6 周内跃升；56 追平 Claude Sonnet 5.5、领先 GPT-6 Astra / Gemini 4 Argon / Claude Fable 5.1 的 53，落后 Claude Opus 5.5 的 58）。在 **gigawatt-scale Prometheus 数据中心**训练，model card 标 **1M 上下文、输入 text/image/video/audio、输出 text**。安全侧称"迄今最强 CBRN / cyber 防护"，完整安全报告"即将发布"。
- ★★ **Anthropic 强化 distillation 防御（Anthropic，2026-10-12）**——**对"能力蒸馏"的工程反制**：新方法使 distiller 攫取的数据量下降约 **90–99%**，平台侧被提取的 reasoning token 数较此前低 **10–100×**。三重手段：① **preserved thinking**（Fable 5.1 / Opus 5.5 起，**2026-08-31 及以后创建的新 API 账号不得编辑既有上下文**；reasoning 不再被弱防护的旧模型读取；Sonnet 5.5 的 reasoning 只对发起请求的组织可见）；② **两阶段 classifier**（沿用 constitutional classifiers 思路，**误报率 <0.1%**，号称与"阻止生物武器协助"的防护同等强度）；③ **限流 + 封号**（封禁数万蒸馏账号，常在两小时内；自 **09-24** 起对 <0.1% 误报区间内被拦截的请求**恢复计费**）。文内点名 **Zhipu (Z.ai) GLM-5.3** 与 **Moonshot**；据同期报道最大一条蒸馏链路指向 **阿里 Qwen**（2026-05~07 超 1.51 亿次交换）。Anthropic 承认有代价（放弃可观收入与数万亿 token 付费流量、部分集成需改造）。
- ★★ **OpenAI textGrain（OpenAI，2026-10-05，邻近补录）**——**熵校准文本水印**：把 token 生成耦合一串由密钥与上下文派生的随机量，构造为带 **KL 正则的 optimal transport** 问题（cost 基于 Gumbel 变量；Sinkhorn 求解）。把词表切成**密钥块（block）**再做 transport 以降维；**β = 允许平均损失的采样熵比例**，KL 散度 = 条件熵下降量，故水印强度有直接信息论解释。检测器**只需文本 + 密钥**（不需模型/提示/β），对 score 做 **Gamma(n,1) 检验**设定误报率。回应 **EU AI Act**：先在 **EU** 的 ChatGPT / Codex 分阶段铺开，API 客户全球可 opt-in（默认关），计划开源。EDITED 鲁棒性数据（1% FPR）：200 token ~80%、400 token ~95%；同义词替换 10% → 66%、25% → 17%。
- ★★ **Meta CanonQ（Meta AI，arXiv:2610.09202，2026-10-06，邻近补录）**——**极端低比特联合量化 QAT 框架**：把"源规范化"与"任务自适应"分离，用固定 **HDP 变换（Hadamard–diagonal–permutation）+ 能量归一化**把异构张量映到**规范坐标**，从而**冻结的 Gaussian-reference codebook 可跨层、跨模型复用**。主打 **W2A4KV2**（权重 2-bit / 激活 4-bit / KV 2-bit 联合）：在 **LLaMA3-1B/3B/8B** 上较此前 SOTA / 代表基线 **WikiText-2 PPL 最多低 14.28×、平均 zero-shot 准确率最多高 57.9%**。理论侧给出冻结码本迁移的 Wasserstein 界、normalization-aware STE Jacobian、以及失真相关的收敛性保证。
- ★ **交叉主题：frontier 竞争从"更大"转向"更能持续干活"**——Muse Wonder 把卖点放在**记忆持久性与长程专注**（FocusBench、SWE-Marathon），AA 的增益也集中在 agentic 评测（Terminal-Bench 4.0 +24pt、GDPval-AA v2.1 +176 Elo、AA-Briefcase +148 Elo）。这与 10-11/10-12 期的"decision model"外扩、以及 Mistral ML4 的 AutomationBench 叙事同源：**评测与产品重心正从静态 benchmark 移向长时程 agentic 任务**。

---

## 一、Meta Muse Wonder / Muse Wonder Full（Meta，2026-10-12）

| 字段 | 内容 |
|------|------|
| **中文标题** | Meta 发布首个 frontier 模型 Muse Wonder 系列：面向个人与专业 agent |
| **英文标题** | Introducing Muse Wonder and Muse Wonder Full: Frontier Models for Agents / Muse Wonder: A Frontier Model For Personal & Professional AI Agents |
| **发布机构** | Meta（Meta Superintelligence Labs） |
| **模型名称** | `Muse Wonder`、`Muse Wonder Full`（系列沿自 Muse Spark → Muse Spark 1.1 / 1.2） |
| **发布日期** | 2026-10-12（model card 同日；安全完整报告"coming soon"） |
| **核心参数** | model card 明列：**输入 text / image / video / audio，输出 text**；**上下文 1M tokens at inference**；多语言训练数据（覆盖全球语言）。**Muse Wonder** 经 Meta Model API + Muse Code 提供；**Muse Wonder Full 仅 Muse Code 订阅者**（**不走 API**，TechCrunch 指出）。**在 gigawatt-scale Prometheus 数据中心训练**，主张"预训练 + RL 双线 rigorous scaling"。 |
| **主要创新点** | ① **Active Memory**——跨对话携带用户重要上下文，并主动检索与当前任务相关的细节；② **Active Focus**——持续朝难目标推进、尝试替代路径、绕过 blocker、适配新信息，需要时澄清、重要动作前确认（评测用 **FocusBench** 与长程编码 **SWE-Marathon**）；③ **Artificial Analysis Intelligence Index v4.3：Wonder Full (max)=56 / Wonder (max)=52**（Muse Spark 1.3 max=48）；Wonder Full 在 10 项 AA 评测中**全涨**，agentic 增益最大：**Terminal-Bench 4.0 +24pt（33%→57%）、GDPval-AA v2.1 +176 Elo（1681→1857）、AA-Briefcase +148 Elo（1581→1729）**；④ 主张"更强 base 模型 → post-training 增益更可迁移到 OOD 任务"，用以回应"benchmaxxing vs big model smell"之争；⑤ 安全侧称迄今最强 **CBRN / cyber** 防护（沿用 Meta Superintelligence Scaling Framework）。 |
| **关键 benchmark（model card，max effort）** | Harvey LAB-AA 13.1 / 10.0；AutomationBench-AA 45.4 / 39.1；JobBench 75.3 / 70.5；**DeepSWE 1.1 79.0 / 78.8**；SWE-Marathon 57.5 / 53.1；Terminal-Bench 4.0-AA 57.1 / 52.0；HealthBench Pro 62.3 / 60.5（Wonder Full / Wonder）。 |
| **可信度** | 中高——**官方 model card + 第三方 Artificial Analysis 独立评测**并行；但 model card 混合了第三方结果与 Meta 自评（文档自述"取最大者"），Benchmark 间不可横向比较；安全细节待完整报告。 |
| **链接** | [research.meta.ai/blog/muse-wonder](https://research.meta.ai/blog/muse-wonder)；[about.fb.com/news/2026/10/introducing-muse-wonder-models](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/)；model card [research.meta.ai/static/muse-wonder-model-card](https://research.meta.ai/static/muse-wonder-model-card)；AA [artificialanalysis.ai/articles/muse-wonder](https://artificialanalysis.ai/articles/muse-wonder) |

**与 Prior 对读**：TechCrunch 称这是 **Scale AI 创始人 Alexandr Wang 于去年 8 月重组 Meta AI 后，Meta 的首个 frontier 模型发布**；此前 Meta 仅释出轻量 **Muse Spark** 与 **Muse** agent，刻意回避 OpenAI / Anthropic 式的 SOTA 发布。本期是 08-31 以来 Meta 首次以"卡面"回到 frontier 牌桌。

---

## 二、Anthropic distillation 防御（Anthropic，2026-10-12）

| 字段 | 内容 |
|------|------|
| **中文标题** | Anthropic 强化对"蒸馏攻击"的防御：数据攫取下降 90–99% |
| **英文标题** | Strengthening our defenses against distillation attacks |
| **发布机构** | Anthropic |
| **发布日期** | 2026-10-12（Reuters 同日报道） |
| **核心结论** | 新方法使 distiller 攫取的数据量下降约 **90–99%**；平台侧被提取的 reasoning token 数较此前低 **10–100×**，部分日期低到无法测量。两阶段 classifier 已能捕获其 9 月报告中描述的全部蒸馏手法。 |
| **三重防御** | ① **preserved thinking**（结构性）——Fable 5.1 / Opus 5.5 起，**2026-08-31 及以后创建的 API 账号不能编辑既有上下文**；reasoning 不再可被弱防护的旧模型读取；Sonnet 5.5 的 reasoning transcript **只对发起请求的组织可见**。② **两阶段 classifier**（沿用 constitutional classifiers 研究）——内外红队修洞，**FPR <0.1%**，号称"与阻止生物武器协助的防护同等强度"；可拦截"把先前 reasoning 翻成另一语言""写在 tag 内输出"等手法。③ **限流 + 封号 + 计费**——持续提取者面临更严限额、进而封号（封禁数万账号，常 <2h）；自 **09-24** 起对 classifier 在 <0.1% 误报区间内拦截的请求**恢复计费**。 |
| **点名对象** | 文内点名 **Zhipu (Z.ai) 的 GLM-5.3** 与 **Moonshot**；据同期报道（cryptobriefing 引 9 月威胁情报报告），5 条 campaign 共约 **2 亿次**蒸馏相关交换，最大一条指向**阿里 Qwen**（2026-05~07 超 1.51 亿次）。 |
| **代价（官方自陈）** | 放弃可观收入与**数万亿 token** 的付费流量；preserved thinking 迫使部分开发者改集成；classifier <0.1% 场景可能误拦正常请求且此类被拦请求仍计费；Anthropic 预期这是持续"猫鼠游戏"，尚未见到高复杂度、持续的规避尝试。 |
| **可信度** | 中——数字**全部来自 Anthropic 自测**，无独立审计；公司亦不公开"看不见的攻击"如何计量。机制描述具体、可验证性较高。 |
| **链接** | [anthropic.com/research/distillation-defenses](https://www.anthropic.com/research/distillation-defenses)；[Reuters 转述](https://www.devdiscourse.com/article/international/3991203-anthropic-says-new-safeguards-sharply-reduce-ai-distillation-attacks)；背景 [anthropic.com/research/detecting-and-preventing-distillation-attacks](https://www.anthropic.com/research/detecting-and-preventing-distillation-attacks)（2026-02-23 首报 DeepSeek / Moonshot / MiniMax） |

---

## 三、OpenAI textGrain：熵校准文本水印（OpenAI，2026-10-05，邻近补录）

| 字段 | 内容 |
|------|------|
| **中文标题** | OpenAI 发布 textGrain：面向 EU AI Act 的熵校准文本水印 |
| **英文标题** | textGrain: Entropy-Calibrated Watermarking for Language Model Text |
| **发布机构** | OpenAI 与 UPenn / Yale（Xiang Li, Garrett Wen, Xiaohong Chen, Qi Long, Arzav Jain, Florent Joly, Mike Lam, Qingquan Song, Weijie Su） |
| **发布日期** | 博客 + 技术报告 2026-10-05；报告挂 alphaXiv 2026-10-10 |
| **核心参数** | 生成侧：密钥 + 上下文窗口把词表切成 **B 个块**、每块 M 个等概率 **列**；密钥生成 **Gumbel 分数表**；求一个 **coupling π**（行和为块概率、列各为 1/m），在 **KL 正则**下最大化落在高分行列的质量（Sinkhorn 迭代，调 λ 逼近目标）。**β = 允许移除的平均采样熵比例**（β=0 无水印；β=0.2 平均保留约 80% 熵）；KL 散度 = token 与列的互信息 = 平均熵损失，故水印强度有信息论解释；损失上限 min{H(ρ), log m}（低熵步几乎不承载水印）。检测侧：**只需文本 + 密钥 + 同配置**（tokenizer、B、m、上下文规则），不解码模型概率、不需 β；每个位置重建块/分数/列 → 得 Gumbel 值 Z_t → 变换 Y_t → 求和 S_n，在"文本与密钥独立"假设下 **S_n ~ Gamma(n,1)**，超出 1−α 分位即判有水印。 |
| **主要创新点** | ① 把"检测所需的依赖"做成**可调**（而非让密钥决定每个 token），并给出熵预算的信息论解释；② 用**块级 OT** 降维同时保留块内相对 token 概率；③ **检测器与生成预算解耦**（无需知道生成时的 β）。对比：报告称先前的 **GumbelSoft** 不保证保持原 NTP 分布，textGrain 的 coupling 边际在固定上下文下（对列平均）**恢复原分布**；谱系可上溯 Kirchenbauer et al.（ICML 2023）与 Google **SynthID Text**（Dathathri et al., Nature 2024）。 |
| **落地** | EU AI Act 驱动：**先在 EU** 的 ChatGPT / Codex 全套餐分阶段推出；API 客户全球可 opt-in（默认关，**非全球默认**）；检测器先向获批研究者/机构开放；计划开源。 |
| **检测率（OpenAI 口径，1% FPR）** | 200 token 心理类文本 ~80%；400 token ~95%；400 token 基线 ~92%，同义词替换 10% → **66%**、25% → **17%**；数学文本、短答、代码、重度编辑明显更难。 |
| **可信度** | 中——**技术报告本身无实验**（仅数学与保证）；检测率来自发布报道口径，**无第三方复现**；短文本/代码为公认弱项。 |
| **链接** | 报告 PDF [cdn.openai.com/.../textgrain...pdf](https://cdn.openai.com/pdf/e9508624-d767-41b6-a26d-e34ca798ada6/textgrain-entropy-calibrated-watermarking-for-language-model-text.pdf)；[openai.com/index/eu-text-provenance](https://openai.com/index/eu-text-provenance/)；[alphaXiv 2610.textgrain...](https://www.alphaxiv.org/abs/2610.textgrain-entropy-calibrated-watermarking) |

---

## 四、Meta CanonQ：W2A4KV2 联合量化（Meta AI，arXiv:2610.09202，2026-10-06，邻近补录）

| 字段 | 内容 |
|------|------|
| **中文标题** | Meta 发布 CanonQ：面向 W2A4KV2 的统一权/激活/KV 联合量化 QAT 框架 |
| **英文标题** | Few Bits, One Law: Toward W2A4KV2 |
| **发布机构** | Meta AI（Kai Yi, Tarek Elgamal, Sruthikesh Surineni, Vignesh Vivekraja, Soumyadeep Ghosh, Steven Li） |
| **发布日期** | arXiv 2026-10-06（arXiv:2610.09202） |
| **核心参数** | **CanonQ** 把问题拆成"源规范化 + 任务自适应"：固定 **HDP 变换**（Hadamard–diagonal–permutation）混合每个 block，**能量归一化**去幅值，把异构张量映到**规范坐标**，从而**冻结的 Gaussian-reference codebook 可跨层/跨模型复用**。变体：**CanonQ-W**（仅权重）、**CanonQ-Omni**（W/A/KV 整条计算路径）。联合 QAT 让网络适配权重/激活/缓存量化**相互耦合**的误差，共用一套 scalar/vector 接口。 |
| **主要创新点** | ① **W2A4KV2**（权重 2-bit、激活 4-bit、KV 2-bit）下大幅领先：LLaMA3-**1B** 15.42 PPL / 53.56% vs **ParetoQ 90.57 / 40.47%**（PPL 低 5.87×、准确率高 13.09 点）；**3B** 11.16/60.04 vs 92.64/39.39（低 8.30×、+20.65 点）；**8B** 9.41/59.81 vs 134.36/37.87（**低 14.28×、准确率高 57.9%**）；② 外推 **Qwen3-1.7B**（W2A4：17.80/50.96 vs 43.56/42.35）与 **MobileLLM-Pro-1B**（W2A16KV16：**HumanEval pass@1 相对 +41.7%、GSM8K EM +39.1%**）；③ **理论**：冻结码本迁移的 **Wasserstein 界**、**normalization-aware STE Jacobian 恒等式**（把量化失真与梯度偏差挂钩）、以及平滑参考目标的失真相关收敛性保证；④ **消融**：W2A4 下表容量不变，仅靠 QAT 即把 PPL 从 7043.43 降到 13.84（说明"适配固定 codec"本身是主要收益来源）。 |
| **可信度** | 中高——arXiv 论文，方法 + 理论 + 多规模实验齐全；但**无第三方复现**，且 PPL/accuracy 为作者自评口径。 |
| **链接** | [arxiv.org/abs/2610.09202](https://arxiv.org/abs/2610.09202) |

---

## 五、其他候选（未达收录门槛 / 待确认）

| 候选 | 机构 | 日期 | 状态 |
|------|------|------|------|
| AWS 在 SageMaker AI 上为 llama.cpp 增加"decision model"部署路径（含可选 **SemIf**，返回应用定义选项的概率而非散文答案；CPU/GPU，g6e 等实例） | Amazon (AWS) | 2026-10-13 | **部署工程**，非 model card / 技术报告；仅作信号记录 |
| Kolibri-1（78B MoE，~3.46B 激活，德/英双语，1M 上下文，Apache-2.0） | Aleph Alpha | 2026-10-03/05 | **非目标机构**；且截至 10-13 无第三方复现、无 AA 条目 |
| Limite 1B - Violetto（1B，237B token 数学语料，131k 上下文，AIME 2026 94.01%） | Paradigma | 2026-09 | **非目标机构**；仅作数学推理小模型参照 |
| Parallax（ternary MoE） | Chutes | 2026-10-10 | **非目标机构**；wiki 内已有记录 |
| Gemini 4 "Carbon" 内部 checkpoint 泄露 | Google DeepMind | 2026-10-09 | 见 10-12 期，**非本期新增** |

---

## 19 家目标机构窗口内（2026-10-12 → 2026-10-13）复核

| 机构 | 窗口内新报告 / 系统卡 | 备注 |
|------|----------------------|------|
| OpenAI | 无（本期补录 **textGrain** 邻近 10-05） | 最近 frontier 报告仍为 09-29 GPT-6 Sol；10-07 有 GPT-6 Sol/Luna 十月更新（Deployment Safety Hub） |
| Anthropic | **有（★）** | **distillation 防御研究**（§2，2026-10-12） |
| Google DeepMind | 无 | Gemini 4 Argon 仍限 Fairwind 试点；Carbon 见 10-12 期 |
| Meta | **有（★★★，frontier 卡面）** | **Muse Wonder / Muse Wonder Full**（§1，2026-10-12）；另有 **CanonQ** 论文（§4，邻近 10-06） |
| Microsoft AI | 无 | Microsoft-Decision-1 见 10-11 期 |
| xAI | 无 | Grok 4.6 见往期；Grok 4.7 见 10-11 期 |
| Mistral | 无 | Mistral Large 4 "le Chonk" preview 见 10-06 起各期（权重月底释出） |
| DeepSeek | 无 | V4.1-Flash 见 10-12 期 |
| Alibaba Qwen | 无（新料） | Qwen-Image-2.1-Turbo 见 10-12 期；Qwen3.8-Max 为 08-02 旧料 |
| ByteDance Seed | 无 | — |
| Moonshot | 无 | 被 Anthropic 点名（§2）；Kimi K3 见往期 |
| Zhipu | 无 | GLM-5.3 被 Anthropic 点名（§2） |
| Tencent | 无 | — |
| Baidu | 无 | — |
| Amazon | **部署工程（非卡面）** | AWS SageMaker llama.cpp decision-model 部署路径（§5） |
| NVIDIA | 无 | — |
| Cohere | 无 | — |
| AI2 | 无（本期无新） | Olmo Hybrid / Bolmo 见 10-12 期 |
| Perplexity | 无 | Decider / pplx-embed-v2-late 见往期 |

---

## 本期不重复收录（交叉引用）

- **Gemini 4 "Carbon" 内部泄露 / Qwen-Image-2.1-Turbo / Ai2 Olmo Hybrid / Ai2 Bolmo in Nature / Cloudflare Clef-omni / Meta "Llama 4 Scout MoD" 传闻**：见 10-12 期 tech-report-digest。
- **Microsoft-Decision-1 / Liquid AI d1 / Perplexity Decider v1 / pplx-embed-v2-late / Anthropic agent 非预期行为报告**：见 10-11 期。
- **GLM-5.4/5.5（信号级）/ ByteDance Phase Sensitivity / Amazon Nova 2.5 Sonic GA / Mistral Large 4 "Le Chonk"**：见 10-08~10-12 各期。
- **DeepSeek-V4.1-Flash / Kimi K3 / Gemma 4 / GLM-5 / Grok 4.7 / Nova 2 / MAI-Thinking-1**：往期已录。

---

## 口径与不确定性声明

- **窗口边界**：主窗口为 **2026-10-12 → 2026-10-13**。Meta Muse Wonder（10-12）与 Anthropic distillation 防御（10-12）为**窗口内一手发布**；OpenAI textGrain（10-05）、Meta CanonQ（arXiv 10-06）为**邻近补录**，均经 repo 级 grep（`Muse Wonder` / `distillation defenses` / `textGrain` / `CanonQ` 等 0 命中）确认为 wiki 首见。
- **首次建档**：本期首次为 **Meta Muse 系列（Wonder / Wonder Full）**、**Anthropic distillation 防御**、**OpenAI textGrain**、**Meta CanonQ** 建立 wiki 记录。
- **未独立复现**：Muse Wonder 性能数字来自**官方 model card + Artificial Analysis 第三方评测**（并行、但 model card 混合第三方与自评）；Anthropic 90–99% 为**厂商自测**、无独立审计；textGrain 技术报告**无实验**、检测率来自发布报道口径；CanonQ 为 arXiv 自评、无第三方复现。
- **低可信 / 二手**：Muse Wonder 的完整安全评估**尚未发布**（官方称 coming soon），CBRN/cyber 结论暂为厂商声明；Anthropic 点名对象与 Qwen 大规模蒸馏数据部分来自**媒体转述**（Reuters / cryptobriefing），已在正文标注来源。
- **厂商口径**：AA Intelligence Index v4.3 为 Artificial Analysis 独立运行；Muse Wonder model card 的 benchmark "取最高者"（内部/官方/自报三选一），**benchmark 间不可横向比较**。
- **语言**：本期沿用 tech-report-digest 系列既有约定（中文正文 + 英文技术术语），与 10-11/10-12 期保持一致。
