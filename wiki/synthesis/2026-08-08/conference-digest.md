---
title: "Conference Digest 2026-08-08：KDD 2026 开幕倒计时（最后一期开幕前全景）+ NeurIPS 2026 三城联动官宣 + RecSys/CIKM/EMNLP 2026 议程前瞻 + 大厂 arXiv 精选（DeepMind 临床模拟 RL / Meta 耦合 Scaling Law / 长序列推荐压缩蒸馏三件套）"
type: synthesis
created: 2026-08-08
updated: 2026-08-08
sources: []
tags: [conference-digest, kdd-2026, neurips-2026, recsys-2026, cikm-2026, emnlp-2026, emnlp-2025, arxiv, llm, rl, scaling-law, recommendation, ctr, long-sequence, agents, world-model, ragment, climate-ai]
---

# Conference Digest — 2026-08-08

本期为 **KDD 2026（Jeju, 8/9–13）开幕前最后一期全景**：官方站点数据口径复核（A*STAR CFAR 7 篇录用 + Bohrium 分析 1,215→256 ≈21%）与一项 **OpenReview 数据泄露通告**（tentative，见 §1）；报告 **NeurIPS 2026 三城联动官宣**（Sydney + Atlanta + Paris，12/6–13，修正 08-07 digest 的 San Jose 单城口径）；新增 **RecSys 2026 / CIKM 2026 / EMNLP 2026 议程前瞻**（含 EMNLP 2026 accepted 名单上线、EMNLP 2025 引用一条 Knowledge Infusion Scaling Law）；并补 **大厂 arXiv 精选**：Google DeepMind **ResidencyRL**（临床模拟 RL）、Meta **Skaling**（耦合 Scaling Law）、华为 **SITA / HD-Rec**、百度 **Autonomy-of-Heads**、**TM20K / CoinRAG / CreativeInstruct / MemWM**，外加 **WeatherNext**（Nature 8/6）与 DeepMind 组织变更背景。当日 arXiv 流由同日 [arxiv-daily](./arxiv-daily.md) 与 [arxiv-ai-search](./arxiv-ai-search.md) 覆盖，SITA / DEGR / Gryphon-v2 已在更早 digest 覆盖（本期仅导航）。

---

## 0. 顶会获奖/动态全景快速导航（已覆盖 → 详情入口）

| 会议 | 状态 | 覆盖入口 |
|------|------|----------|
| **ICML 2026**（Seoul, 7/6–11） | 3 Outstanding + 3 HM 已覆盖 | [08-04](../2026-08-04/conference-digest.md) §1.2 |
| **NeurIPS 2025**（San Diego, 12/2–7） | 4 Best + 3 runners-up 已覆盖 | [08-01](../2026-08-01/conference-digest.md) + [08-04](../2026-08-04/conference-digest.md) §1.6 |
| **ICLR 2026**（Rio, 4/23–27） | Outstanding/HM/ToT/e3 已覆盖 | [08-01](../2026-08-01/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §6 |
| **AAAI 2026**（Singapore, 1/20–27） | Best 已覆盖（录用率 17.6%） | [08-01](../2026-08-01/conference-digest.md) |
| **CVPR 2026**（Denver, 6/3–7） | 全部奖项已覆盖（16,092/4,089, 25.4%） | [08-04](../2026-08-04/conference-digest.md) §1.1 |
| **KDD 2026**（Jeju, 8/9–13） | Research Best = PiPNN 已覆盖；**开幕倒计时，最后一期开幕前全景**（A*STAR CFAR 7 篇 + Bohrium 21% + OpenReview 通告） | [08-04](../2026-08-04/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §1 + [08-07](../2026-08-07/conference-digest.md) §1 + 本期 §1 |
| **ACL 2026**（San Diego, 7/2–7） | 完整奖项 + Long 世界模型新作已覆盖 | [08-04](../2026-08-04/conference-digest.md) §1.4 + [08-06](../2026-08-06/conference-digest.md) §1 |
| **EMNLP 2025**（Suzhou, 11/4–9） | 完整奖项已覆盖（Main 22.16%）+ **Knowledge Infusion Scaling Law 引用** | [08-04](../2026-08-04/conference-digest.md) §1.5 + 本期 §3.3 |
| **WWW 2026**（Dubai, 6/29–7/3） | Best/Best Short/ToT + NEZHA 已覆盖 | [08-04](../2026-08-04/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §4 |
| **SIGIR 2026**（Melbourne, 7/20–24） | 奖项名单最终确认已覆盖 | [08-05](../2026-08-05/conference-digest.md) §2 + [08-07](../2026-08-07/conference-digest.md) §2 |
| **CIKM 2025**（Seoul, 11/10–14） | Best Full + Best Student 已覆盖 | [08-03](../2026-08-03/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §5 |
| **RecSys 2025**（Prague, 9/22–26） | Best Full/Short + ULIM 已覆盖 | [08-03](../2026-08-03/conference-digest.md) + [08-05](../2026-08-05/conference-digest.md) §5 |
| **NeurIPS 2026** | **三城官宣**（Sydney + Atlanta + Paris, 12/6–13）+ rebuttal 争议已覆盖 | [08-07](../2026-08-07/conference-digest.md) §3 + 本期 §2 |
| **RecSys 2026**（Minneapolis, 9/28–10/2） | **议程前瞻**（PC/GC 名单确认） | 本期 §3.1 |
| **CIKM 2026**（Tokyo, 9/13–17） | accepted 名单 TBD | 本期 §3.2 |
| **EMNLP 2026**（Porto, 11/2–6） | **accepted 名单已上线** | 本期 §3.3 |

---

## 1. KDD 2026（Jeju, 8/9–13）— 开幕倒计时：最后一期开幕前全景

> 明日开幕（workshops & tutorials 8/9–10，主会 8/11–13）。数据口径：Vol.1 共 1,215 投稿 / 256 录用（≈21%）；Research Best = PiPNN（[08-04 digest](../2026-08-04/conference-digest.md)）已覆盖，奖励 8/13 现场公布。本期仅补官方站点状态与两处数据口径。

### 1.1 官方站点/机构口径

- **A*STAR CFAR（新加坡计算先进研究院）7 篇论文入选 KDD 2026**：覆盖多模态数据表示（multimodal representation）、几何学习、可信 AI、大规模 LLM 等方向，显示 KDD 2026 工业/学术交叉叙事中的亚太研究机构活跃度。
- **Bohrium 投稿分析**：1,215 篇投稿 → 256 篇录用（≈21%），与 [08-05 digest §1](../2026-08-05/conference-digest.md) 的数据口径一致，录用难度与 2025 年相当（对比见 [08-07 digest](../2026-08-07/conference-digest.md) §1）。
- **⚠️ OpenReview 相关通告**：KDD 2026 官方站点（kdd2026.kdd.org）出现与 OpenReview 相关的数据泄露/访问异常通告。(tentative, single-source) 评审基础设施安全事件继 NeurIPS 2026「rebuttal 不可见」界面故障（[08-07 digest §3](../2026-08-07/conference-digest.md)）之后再添一例——本轮审稿周期的「评审基础设施可信度」主题仍在延续。

### 1.2 日程提示

- 8/9–10：workshops & tutorials（含 SynthIR 类 workshop 生态、AI for Sciences Track 相关 tutorial）
- 8/11–13：主会；8/13 现场公布全部奖项（Best Paper / Best Student / ADS / Blue Sky 等）

---

## 2. NeurIPS 2026 — 三城联动官宣 + 周期动态

> ⚠️ **口径修正**：08-07 digest §3 记录为「San Jose, 12/6–12」。本期核验到官方为**三城联动**：**Sydney（12/6–12）+ Atlanta（12/8–13）+ Paris（12/9–13）**，多时区并行的混合场次。以本期为准。

- **时间线**：abstract 5/4、全文 5/6 已截止；reviews 7/22 发布（7/23 重新发布全部 reviews 与 initial meta-reviews）；author 讨论窗 7/27–8/3 已结束（**rebuttal 周「集体沉默」争议**见 [08-07 digest §3](../2026-08-07/conference-digest.md)，AC pilot 机制 + ARR 抢评审池）；reviewer/AC 审议至 8/10；**通知 9/24**。
- **8/8–9 决策批次**：Competition Track 决策已公布（Scientific AI / Physics / Engineering / Healthcare / Foundation Models / Reasoning / Robotics / Agents / Embodied AI 等方向）；workshop accept/reject 通知 8/9。Creative AI Track 截止顺延至 **8/10 AoE**。

---

## 3. 2027 议程前瞻：RecSys 2026 / CIKM 2026 / EMNLP 2026

### 3.1 RecSys 2026（Minneapolis, 9/28–10/2）

- **主会议程**：Main Sessions **9/29–10/1**（9/28 为 workshops & tutorials 日，10/2 为 industry day 等收尾）。
- **领导架构**：PC Chairs = **Minmin Chen**（Google DeepMind）、**Bart Goethals**（FLAIR）、**Martijn Willemsen**（Eindhoven）；General Chairs = **Joseph Konstan**（UMN, Minneapolis 本地）、**George Karypis**、**Gediminas Adomavicius**。
- **意义**：Minmin Chen 领衔 PC + Konstan 回归 General Chair，延续 RecSys「工业界 RL/生成式推荐 × 经典人机交互评估」双主线；与本期 §4 长序列推荐三件套形成议程呼应。

### 3.2 CIKM 2026 — accepted 名单 TBD

- 官方站（cikm2026.diag.uniroma1.it）accepted papers 页面仍为 **TBD**（截至 8/8 未发布）；track 结构沿用 Full/Short/Industry/Applied 等。与 KDD 2026 同期审稿周期重叠，预计未来数周放榜。

### 3.3 EMNLP 2026 — accepted 名单已上线 + EMNLP 2025 引用一条

- **EMNLP 2026**（Porto, 11/2–6）：主会 accepted papers 列表已上线（2026.emnlp.org/program/main_papers/）。示例：TU Darmstadt 团队关于**对话式 AI 错误发现/诊断**的论文在列；完整榜单可作为后续 digest 的逐篇挖掘源。
- **引用（已出版论文集，不展开）**：*Knowledge Infusion Scaling Law*（EMNLP 2025 Main, **2025.emnlp-main.1331**, Alibaba, Kangtao Lv 等）。要点：外部知识注入存在 **memory-collapse threshold**——低于该阈值时模型微调后遗忘外部知识；且 **critical collapse point 随模型规模增大而 scale up**，即越大模型越能在更高知识量下保持注入知识（为「知识注入的 scaling 行为」提供首个系统刻画，与 CTR/LLM 的 scaling law 主线 [08-05 digest §1](../2026-08-05/conference-digest.md) 平行）。

---

## 4. arXiv 大厂/重点实验室精选（2608.xxxxx 本周批次，全库 grep 去重）

> 收录原则：本期新收录 8 篇（全部 grep 核验无既有覆盖）；SITA / DEGR / Gryphon-v2 已在更早 digest 覆盖，此处仅导航。当日 arXiv 流（LLM reasoning/agents/TS）见同日 [arxiv-daily](./arxiv-daily.md) 与 [arxiv-ai-search](./arxiv-ai-search.md)。

### 4.1 Google DeepMind: ResidencyRL — RL 进入临床模拟环境
**中文标题**：《ResidencyRL：面向临床住院医师训练的强化学习》

- **作者**：35 人（含 Quoc V. Le、Raia Hadsell、Joelle Barral、Dale R. Webster 等 DeepMind 领导层）
- **会议**：arXiv:2608.07418（cs.LG, 2026-08-07 批次）
- **背景与创新**：把 RL 应用于**模拟临床环境中的医疗住院医师（residency）训练**——agent 在可交互的临床模拟中学习诊断/决策序列，而非仅静态病例。这是「RL + 医学模拟」从单任务（如血糖控制、用药）走向**结构化职业能力训练**的规模化尝试，作者阵容罕见地包含 DeepMind 研究与组织领导层。
- **意义**：与 KDD 2026 的 MSR Battery-Sim-Agent（[08-07 digest §1.2.7](../2026-08-07/conference-digest.md)）同属「**模拟器在环（simulator-in-the-loop）RL**」叙事，也呼应 [08-03 digest](../2026-08-03/conference-digest.md) 的 From AGI to ASI 主线。

### 4.2 Meta: Skaling — Chinchilla 指数耦合，把 Scaling Law 做「闭式」
**中文标题**：《Skaling：模型规模指数与数据规模指数的耦合定律》

- **作者**：M. Videau, B. Youbi-Idrissi, D. Lopez-Paz, K. Ahuja（Meta FAIR）
- **会议**：arXiv:2608.07222（cs.LG, 2026-08-07 批次）
- **背景与创新**：经典 Chinchilla 把 loss 分解为 `L(N,D) = A/N^α + B/D^β`（两个独立指数）。**Skaling** 让模型规模指数 α 与数据规模指数 β **互相耦合**（coupling exponent），统一了 Chinchilla（独立指数）与 Kaplan（早期耦合观）两条路线。
- **实验结果**：外推误差（MAPE）相对经典定律 **降低 1.5–3×**；在**全网格外推**场景约需 **10× 更少计算**即可达到同精度。
- **意义**：Scaling Law 研究从「拟合更准」走向「结构先验正确」——耦合指数给出的是更可迁移的外推器，直接影响 compute-optimal allocation 决策。与 [08-05 digest §1](../2026-08-05/conference-digest.md) 的 CTR scaling law（Alibaba FAT）构成「通用模型 / 垂直领域」两端呼应。

### 4.3 长序列推荐三件套：华为 SITA（导航）+ TM20K + HD-Rec（新增）

#### 4.3.1 SITA（华为 Noah's Ark + USTC）— 已覆盖，仅导航
**中文标题**：《SITA：面向目标感知长序列推荐压缩的语义兴趣 Token》
- **arXiv**: 2608.03692；**已在 [08-07 arxiv-ai-search](../2026-08-07/arxiv-ai-search.md) 详细覆盖**（Semantic Interest Tokens，目标感知压缩，华为 Bo Chen / Ruiming Tang + 中科大 Enhong Chen）。此处不重复。

#### 4.3.2 TM20K: 电商广告超长序列的「老师保留全 token」蒸馏
**中文标题**：《TM20K：两万级序列建模的师生蒸馏——老师保留全部 Token，学生学会合并》

- **会议**：arXiv:2608.07055（cs.IR/cs.LG, 2026-08-07 批次）
- **背景与创新**：电商广告场景序列长度达 20K 级。既有蒸馏常让**老师也截断/采样**，丢失长尾行为。本文教师模型**保留全量 token** 进行前向，学生模型在有限长度下学习**如何合并**冗余历史（distill "merging" behavior），从而在推理长度不变的前提下逼近全历史建模。
- **意义**：与 SITA（目标感知压缩）、HD-Rec（跨域量化）共同构成「**长序列推荐三件套**」——三者分别从压缩、蒸馏、生成三条路径处理「上下文爆炸」。本节三篇互相独立、互为补充。

#### 4.3.3 HD-Rec: 分层量化 + 域自适应稀疏路由的生成式跨域推荐
**中文标题**：《HD-Rec：面向生成式跨域推荐的分层量化与域自适应稀疏路由》

- **作者**：华为 Noah's Ark（Bo Chen, Ruiming Tang, Guorui Zhou, Han Li）+ CityU（Xiangyu Zhao）
- **会议**：arXiv:2608.06997（cs.IR, 2026-08-07 批次）
- **背景与创新**：生成式推荐（GenRec）需要把用户行为离散化为 token 序列。HD-Rec 用**分层量化（hierarchical quantization）**得到跨域共享的高层语义 + 域特定细节，并以**域自适应稀疏路由（domain-adaptive sparse routing）**选择生效的专家，缓解跨域迁移中的域混淆。
- **意义**：延续华为 Noah's Ark 在生成式推荐/长序列的主线（与 FOUNDv2 量化 tokenizer 思路同族，见 [08-07 digest §1.2.4](../2026-08-07/conference-digest.md)），且由 Xiangyu Zhao（CityU）参与，工业-学界双署名。

#### 4.3.4 导航（已覆盖）：DEGR + Gryphon-v2
- **DEGR**（2608.04809）：双探索驱动生成式重排（cross-request 上下文桥接）——**已在 [08-06 arxiv-daily](../2026-08-06/arxiv-daily.md) 与 [08-06 arxiv-paper-check](../2026-08-06/arxiv-paper-check.md) 覆盖**（JD, KDD 2026 ADS, +1.22% UCTR）。
- **Gryphon-v2**（2608.06213）：单一 generate-and-rank 模型取代 15+ 级联生成器（rollout distillation, Yandex）——**已在 [08-07 arxiv-daily](../2026-08-07/arxiv-daily.md) 与 [08-07 arxiv-ai-search](../2026-08-07/arxiv-ai-search.md) 覆盖**（+1.41% active users）。

### 4.4 效率/推理/世界模型/生成

#### 4.4.1 Baidu: Autonomy-of-Heads — 免数据稀疏 Attention（冻结 QK 几何）
**中文标题**：《Head 的自主性：基于冻结 QK 谱几何的无数据稀疏注意力》

- **作者**：Yehan Yang, Junyuan Shang, Shuohuan Wang, Dianhai Yu（百度）
- **会议**：arXiv:2608.06849（cs.LG, 2026-08-07 批次）
- **背景与创新**：既有稀疏注意力通常需微调或依赖训练中数据统计。本文证明**冻结模型的 QK 谱几何**已编码足够信息：利用 spectral geometry 在**无需任何数据**（data-free）的情况下决定各 head 的稀疏模式，直接为预训练模型套上稀疏 attention。
- **意义**：与 08-06/07 的 KV 效率工作（NOVA-KV / Spend-Bits 等）同属「预训练模型的稀疏/量化后装」，但把「需要校准数据」的普遍前提去掉，纯几何驱动。中文大厂效率叙事（华为长序列、百度稀疏化）本期集中出现。

#### 4.4.2 CoinRAG: 信息 nugget 的 KV 缓存复用（长上下文 RAG）
**中文标题**：《CoinRAG：上下文化信息点的 KV 缓存复用》

- **作者**：Gyuwan Kim 等（Naver Cloud / LLM 研究者）
- **会议**：arXiv:2608.07458（cs.CL/cs.LG, 2026-08-07 批次）
- **背景与创新**：长上下文 RAG 中，检索到的文档被反复处理成上下文。CoinRAG 把证据块加工为**上下文化信息点（contextualized info nugget）**并缓存其 KV，使后续相关查询可复用检索结果的计算，而不用重复 prefill。
- **意义**：RAG 的「检索-生成」边界开始出现显式的**缓存/复用层**，与 08-06 的「KV 走向分配+调度」趋势一致（[08-04 digest](../2026-08-04/conference-digest.md) §6 的 VarRate 同族）。

#### 4.4.3 UNC: CreativeInstruct — 教 LLM 平衡质量 / 创造力 / 多样性
**中文标题**：《CreativeInstruct：以质量、创造力与多样性的平衡为目标训练 LLM》

- **作者**：Mohit Bansal, Elias Stengel-Eskin（UNC Chapel Hill）等
- **会议**：arXiv:2608.07460（cs.CL, 2026-08-07 批次）
- **背景与创新**：生成任务的 RL 对齐通常只优化单一质量信号，导致输出趋同。CreativeInstruct 显式构造**质量-创造力-多样性**三目标的平衡训练信号，避免「高分但千篇一律」。
- **意义**：与 Creative AI Track 顺延至 8/10 的 NeurIPS 2026（§2）呼应——「创造力的可优化性」正在成为对齐研究的显式维度。

#### 4.4.4 LMU: MemWM — 记忆增强的文本世界模型
**中文标题**：《MemWM：以记忆库为条件的文本世界模型》

- **作者**：LMU Munich 等
- **会议**：arXiv:2608.07107（cs.AI, 2026-08-07 批次）
- **背景与创新**：把长期记忆显式接入文本世界模型——状态转移同时受当前文本与**记忆库（memory bank）**条件，缓解长时程任务中的状态遗忘。**SSF（single-stage framework）相对 SFT 提升 +206.3%**，在 ALFWorld / WebShop / ScienceWorld 上相对任务成功率 +65.4%。
- **意义**：世界模型「记忆化」三件套（记忆 → 状态保真）在文本域的最新解，与 [08-06 digest §1](../2026-08-06/conference-digest.md) ACL 2026 文本世界模型评测、以及当日 [game-rl-daily](./game-rl-daily.md) 的游戏世界模型主题互证。

### 4.5 WeatherNext（Nature, 8/6）— 气旋预报 +1 天预警

- **发布**：Nature（2026-08-06, DOI s41586-026-10953-2），Google DeepMind；模型已开源。
- **要点**：气旋**路径 / 强度 / 风结构**三指标达 SOTA；关键增益是**把有效预警提前量提高约 1 天**——对灾难响应（疏散、防御）的边际价值显著大于分数微涨。
- **意义**：科学基础模型的「可行动增益」叙事（不只刷基准，而是给出决策可用的提前量）与 §4.1 ResidencyRL、KDD 2026 AI for Sciences Track 共振；也印证 DeepMind 重组后（见下）继续以「科学 + 气候」为公开叙事主轴的判断。

### 4.6 背景：Google DeepMind 组织变更（8/5，交叉引用）

- Demis Hassabis 卸任 GDM CEO → **Chair of GDM + Alphabet Chief Scientist**；**Koray Kavukcuoglu → SVP 领导 GDM**；Jeff Dean 离开 Alphabet（另立 Discovery Loop）。
- **已在 [08-06 investment-daily](../2026-08-06/investment-daily.md) / [wq101-alpha-daily](../2026-08-06/wq101-alpha-daily.md) 覆盖**（GOOGL -4% 组织风险）。此处仅作为本期 arXiv（ResidencyRL 作者名单含 Barral/Hadsell）与 WeatherNext 发布的组织背景引用。

---

## 5. 本期主题串讲

1. **医学/科学 AI 进入「模拟器在环 + 可行动增益」**：ResidencyRL（临床模拟 RL）+ WeatherNext（+1 天预警）+ KDD 2026 的 MSR Battery-Sim-Agent——三者共享同一方法论结构：**在可交互模拟器中训练/验证，产出决策场景可用的增益**，而非仅离线指标。这与 KDD 2026 主旨 Barzilay「高预测精度不足以保证支撑临床决策」的警示（[08-07 digest §1.1](../2026-08-07/conference-digest.md)）构成正面回答。
2. **长序列推荐进入「压缩 + 蒸馏 + 生成」三件套**：SITA（目标感知压缩）、TM20K（全 token 蒸馏）、HD-Rec（跨域量化生成）——「上下文爆炸」的三种解法在本期同批出现；叠加已覆盖的 DEGR / Gryphon-v2，生成式/长序列推荐在 8 月上旬迎来方法论密集输出。
3. **中国大厂效率叙事收敛**：百度（免数据稀疏注意力）、华为（长序列三件套）、阿里（EMNLP 2025 知识注入 scaling law）——「把既有模型的每一分参数榨干」成为中文大厂 arXiv 主旋律，与 Meta 的 Scaling Law 理论化（Skaling）形成「实证 × 理论」双轨。
4. **审评基础设施仍是 2027 周期的核心变量**：NeurIPS 2026 三城 + 竞争性评审机制改革（AC pilot）推进中，而 KDD 2026 站点出现 OpenReview 通告、NeurIPS 2026 出现 rebuttal 界面故障——「评审机制可信度」从 08-06/08-07 digest 的方法论质疑扩展为基础设施层面事件，建议后续 digest 持续跟踪。

---

## 附：本期核验与去重记录

- **已覆盖、排除**：SITA（2608.03692，[08-07 arxiv-ai-search](../2026-08-07/arxiv-ai-search.md)）、DEGR（2608.04809，[08-06 arxiv-daily](../2026-08-06/arxiv-daily.md) + [08-06 arxiv-paper-check](../2026-08-06/arxiv-paper-check.md)）、Gryphon-v2（2608.06213，[08-07 arxiv-daily](../2026-08-07/arxiv-daily.md) + [08-07 arxiv-ai-search](../2026-08-07/arxiv-ai-search.md)）、Google DeepMind 组织变更（[08-06 investment-daily](../2026-08-06/investment-daily.md)）、NeurIPS 2026 rebuttal 争议（[08-07 digest §3](../2026-08-07/conference-digest.md)）、KDD 2026 主旨/工业论文/KDD Cup（[08-07 digest §1](../2026-08-07/conference-digest.md)）。
- **核验方式**：每篇新收录 arXiv 论文均对 index.md、log.md、wiki/synthesis/** 全文 grep（arXiv ID + 关键词双查）后才收录。KDD 2026 官方站点通告与 Bohrium 分析为独立来源；NeurIPS 2026 三城与 RecSys 2026 PC/GC 名单以官方站点为准；OpenReview 通告为 (tentative, single-source)，标注待后续核验。
