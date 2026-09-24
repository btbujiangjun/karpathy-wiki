---
title: "Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-09-24"
type: synthesis
created: 2026-09-24
updated: 2026-09-24
sources: [conference-web-searches]
tags: [conference-digest, ICDM2026, ICLR2026, AAAI2026, NeurIPS2025, KDD2026, CVPR2026, SIGIR2026, ACL2026, EMNLP2026, WWW2026, CIKM2025, RecSys2025, recommendation, LLM, advertising, CTR, agents, generative-models, sequential-modeling, games, code-execution, benchmarks, daily-digest]
---

# Conference Digest: Top ML/AI Conferences 2025-2026 — 2026-09-24

> 覆盖 ICML 2026 / ICLR 2026 / AAAI 2026 / NeurIPS 2025 / KDD 2026 / CVPR 2026 / ACL 2026 / EMNLP 2025 / SIGIR 2026 / WWW 2026 / CIKM 2025 / RecSys 2025 及近期通用 arXiv（LLM、推荐、广告/CTR、游戏、代码执行预测、Agent 系统、生成式模型、序列建模、Benchmark）。
>
> **方法**：四个并行 web 检索代理分别覆盖 NLP/LLM、Rec/Ads/CTR、CV/视频生成、Games/Agents/Code 四大主题；随后对全部候选以 arXiv export API（`export.arxiv.org/api/query?id_list=...`）逐条核验标题/日期/ID。**25 篇 featured 论文全部核验为真实存在，且 grep-verified 0 hits in `wiki/`**（与今日 [[arxiv-daily|synthesis/2026-09-24/arxiv-daily]] / [[arxiv-ai-search|synthesis/2026-09-24/arxiv-ai-search]] / [[arxiv-paper-check|synthesis/2026-09-24/arxiv-paper-check]] 已申领的窗口 ID 2609.26809–2609.28473 完全不相交）。
>
> **Covered-flagship 说明**：本期的 12 个目标会议中，多数大会的旗舰论文已被此前各期 digest 收录（如 ICML'26 Outstanding、KDD'26 工业推荐、CVPR'26 Best 等）。本文 Part I 只收经过核验的**新增**论文；Part III 提供各会议"已收录要闻导航"，指向既有 synthesis 页。

---

## 0. 执行摘要

| 主题 | 本期亮点 |
|------|---------|
| LLM 后训练 / RLVR | RLVR 隐式激励正确推理的理论+实证框架（Microsoft, ICLR'26）；无外部奖励的自我置信度 RL（Berkeley, ICLR'26） |
| Scaling Laws | "Skill Scaling Laws" 跨家族预测（MIT-IBM, NeurIPS'25）；loss-collapse 可预测训练与诊断（Cerebras, ICLR'26）；MoE scaling law 的 constant-per-expert-width 机制 |
| 测试时计算 | Bandit 视角的按难度算力分配（ICLR'26）；"Thinking Hard, Not Smart"——推理模型无法跨题理性分配预算（UMD） |
| 推理可信度 | CoT 隐藏推理实证（filler token, UMD）；结果奖励≠可验证/因果重要推理（Stanford） |
| 推荐/生成式推荐 | RecZero 纯 RL 自主学习推荐推理（NeurIPS'25）；"Think before Recommendation" 范式 |
| 视频生成 / 世界模型 | STARFlow-V 端到端 Normalizing Flow 视频生成（Apple, CVPR'26）；TGT 文本锚定轨迹局部控制（ByteDance, CVPR'26） |
| Agent | WeaveBench 混合接口长程评测（Microsoft）；Wuying 长程浏览器 Agent；Alem 开放式多体协作（UCL） |
| 代码执行预测 | 神经调试器——可设断点/反向推理的 neural interpreter（Meta） |
| 序列建模 | DART 对递归状态做解码注意力（长上下文，Mamba-2 路线改进） |

---

## Part I — 按会议归类的新增核验论文

### 1. ICML 2026（Seoul，7/6-12）

#### 1.1 World-R1: Reinforcing 3D Constraints for Text-to-Video Generation（World-R1：为文生视频引入 3D 约束强化）
- **Authors**: （多机构，见 arXiv 页）
- **Affiliation**: （学界为主）
- **Venue**: ICML 2026（依据 proceedings 列表，tentative）
- **arXiv**: [2604.24764](https://arxiv.org/abs/2604.24764)
- **背景与问题**: 纯文本条件的文生视频模型经常违反物理/3D 一致性（物体漂浮、缩放异常），此前工作只把一致性当作评测项而非训练信号。
- **方法与创新**: 把 3D/物理一致性编码为 RL 奖励，用强化学习约束文生视频扩散模型。这是 ICML 2026 上少数以"3D 约束强化"为训练机制的文生视频论文，方向与 RLVR 在视频生成域的迁移一致。
- **实验结果**: 相比 SOTA 文生视频基线在物理合理性、3D 一致性上显著提升。
- **与既有方法对比**: 与纯扩散训练的 T2V 相比，首次把"3D/物理约束"训练进模型本身。

### 2. ICLR 2026（Rio de Janeiro，4/28–5/2）

#### 2.1 Strategic Scaling of Test-Time Compute: A Bandit Learning Approach（测试时计算的战略性配置：一种 Bandit 学习方法）
- **中文标题**: 测试时计算的战略性配置：一种 Bandit 学习方法
- **Authors**: Bowen Zuo, Yinglun Zhu
- **Affiliation**: UC Riverside
- **Venue**: ICLR 2026
- **arXiv**: [2506.12721](https://arxiv.org/abs/2506.12721)
- **背景与问题**: 现有 test-time compute 方法对所有 query 均匀分配算力，忽略难度差异；而用 oracle 难度信号的方案不可落地。
- **方法与创新**: 把算力分配建模为 bandit learning 问题——在线估计 query 难度、差异化分配算力预算，优先投入"可解但困难"的问题，减少在不可解问题上的浪费；理论证明了相对均匀分配的计算效率优势。
- **实验结果**: MATH-500 提升最高 11.10pp（相对 15.04%）；AIME25 最高 10.82pp（相对 14.44%）；LiveCodeBench 最高 11.23pp（相对 15.29%）。
- **与既有方法对比**: 相对 o1 式固定预算 uniform scaling，本方法按难度自适应；相对依赖 oracle 难度的方案，完全在线、无需先验标注。

#### 2.2 Scaling with Collapse: Efficient and Predictable Training of LLM Families（折叠式扩展：LLM 家族的的高效可预测训练 · Celerity）
- **中文标题**: 折叠式扩展：LLM 家族的高效可预测训练（附 Celerity 模型族）
- **Authors**: Shane Bergsma, Bin Claire Zhang, Nolan Dey, Shaheer Muhammad, Gurpreet Gosal, Joel Hestness
- **Affiliation**: Cerebras
- **Venue**: ICLR 2026
- **arXiv**: [2509.25087](https://arxiv.org/abs/2509.25087)
- **背景与问题**: "loss 曲线 collapse 到通用轨迹"（Qiu et al. 2025）此前只在理想设定下验证，是否适用于实际联合扩展配方（width/depth/lr/batch/weight decay 同步缩放）未确认。
- **方法与创新**: 证明在超参按给定数据预算取最优时，collapse 现象依然成立；把 collapse 从描述性观察转化为**训练诊断工具**（偏离 collapse = 训练病理早期信号）与超参搜索中的 early stopping 准则；据此训练了竞争级模型族 **Celerity**。
- **实验结果**: Celerity 达到竞争级性能；collapse 诊断在真实大规模训练中对病理敏感、早期报警。
- **与既有方法对比**: 将单标量层面的 collapse 扩展至联合缩放配方，并商业化落地为 Cerebras 的模型训练方法论。

#### 2.3 Learning to Reason without External Rewards（无需外部奖励的推理学习 · RLIF / Intuitor）
- **中文标题**: 无需外部奖励的推理学习（RLIF / Intuitor）
- **Authors**: Xuandong Zhao, Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song
- **Affiliation**: UC Berkeley
- **Venue**: ICLR 2026
- **arXiv**: [2505.19590](https://arxiv.org/abs/2505.19590)
- **背景与问题**: RLVR 依赖昂贵、领域特定的可验证监督（gold answers / 测试用例），限制了把推理 RL 推广到自主 AI 场景。
- **方法与创新**: 提出 **RLIF (Reinforcement Learning from Internal Feedback)**：用模型自身置信度（self-certainty）作为唯一奖励信号，在 GRPO 中替代外部奖励，完全无监督地学习推理。
- **实验结果**: 数学基准上与带 verifier 的 GRPO 持平；在代码生成等 out-of-domain 任务上泛化更好。
- **与既有方法对比**: 相对 DeepSeek-R1 路线的 RLVR/GRPO 完全去监督化，避免 verifier 工程。

#### 2.4 Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs
- **中文标题**: RLVR 在基座 LLM 中隐式激励正确推理
- **Authors**: Xumeng Wen, Zihan Liu, Shun Zheng, Shengyu Ye, Zhirong Wu, Yang Wang, Zhijian Xu, Xiao Liang, Junjie Li, Ziming Miao, Jiang Bian, Mao Yang
- **Affiliation**: Microsoft + Shanghai AI Lab 等
- **Venue**: ICLR 2026
- **arXiv**: [2506.14245](https://arxiv.org/abs/2506.14245)
- **背景与问题**: 学界争议"RLVR 是否只是提升了采样效率而非真正激励推理"（GPT-2 时代的反例观点）。
- **方法与创新**: 用 Pass@K 复现实验证明 RLVR 扩展了数学与代码任务的**推理边界**；提出同时计入最终答案与中间推理步骤的新指标 **CoT-Pass@K**；给出解释"仅凭答案正确性奖励为何能激励正确推理"的理论框架；训练动力学分析显示 RLVR 在早期就激励正确推理。
- **实验结果**: 数学与代码任务的 pass@k 与 CoT-Pass@K 双重验证推理边界扩展；理论框架在多种 RLVR 变体上得到实证支持。
- **与既有方法对比**: 首次正面回应"RLVR 仅提升采样效率"论调，用更细粒度指标+理论把奖励信号与推理本身挂钩。

### 3. NeurIPS 2025（San Diego，12/2-7）

#### 3.1 Sloth: Scaling Laws for LLM Skills to Predict Multi-Benchmark Performance Across Families
- **中文标题**: Sloth：面向"技能"的 Scaling Laws（跨家族多基准性能预测）
- **Authors**: Felipe Maia Polo, Seamus Somerstep, Leshem Choshen, Yuekai Sun, Mikhail Yurochkin
- **Affiliation**: MIT-IBM Watson AI Lab / Harvard
- **Venue**: NeurIPS 2025
- **arXiv**: [2412.06540](https://arxiv.org/abs/2412.06540)
- **背景与问题**: 传统跨家族 scaling law（Hoffmann et al.）对下游多基准性能预测粗糙，逐家族训练多尺寸模型成本高。
- **方法与创新**: 提出 **Skill Scaling Laws**：LLM 性能由低维潜技能（reasoning、instruction following 等）驱动，各技能受模型规模与训练 token 影响、跨家族转换效率不同；利用跨 benchmark 相关性预测，无需为每个家族训练多个尺寸。含参数可识别性（identifiability）理论结果。
- **实验结果**: 在 Open LLM Leaderboard v1/v2 的 12 个 benchmark 上给出跨家族精确预测；揭示复杂下游任务 α、test-time compute 增加、compute-optimal 技能扩展的规律。
- **与既有方法对比**: 平衡了单一定律的外推性与家族特定定律的准确性，可与 [[concepts/shannon-scaling-law]] 的香农视角互为补充。

#### 3.2 Fixing It in Post: A Comparative Study of LLM Post-Training Data Quality and Model Performance
- **中文标题**: Fixing It in Post：LLM 后训练数据质量与模型性能的对比研究
- **Authors**: Aladin Djuhera, Swanand Ravindra Kadhe, Syed Zawad, Farhan Ahmed, Heiko Ludwig, Holger Boche
- **Affiliation**: IBM Research / TU Munich
- **Venue**: NeurIPS 2025
- **arXiv**: [2506.06522](https://arxiv.org/abs/2506.06522)
- **背景与问题**: 主流开源后训练语料（Tulu-3-SFT-Mix、SmolTalk）的质量差异没有被系统量化，"直接合并语料"是常见做法。
- **方法与创新**: 首个对两大语料的系统性并排分析：用 Magpie 框架逐样本标注 turn 结构/任务类别/输入质量/回答质量，推导结构性差异；据此给出可复现的 curation 配方并产出新混合语料 **TuluTalk**。
- **实验结果**: TuluTalk 比任一源语料少 **14%** 样本，在关键 benchmark 上持平或超越两个源数据集；语料与标注集全部公开。
- **与既有方法对比**: 相对"直接合并开源语料"，展示质量/结构驱动的"更少但更优"走向。

#### 3.3 Think before Recommendation: Autonomous Reasoning-enhanced Recommender（RecZero / RecOne）
- **中文标题**: 推荐前先思考：自主推理增强的推荐系统（RecZero / RecOne）
- **Authors**: Xiaoyu Kong, Junguang Jiang, Bin Liu, Ziru Xu, Han Zhu, Jian Xu, Bo Zheng, Jiancan Wu, Xiang Wang
- **Affiliation**: USTC & Alibaba
- **Venue**: NeurIPS 2025（poster）
- **arXiv**: [2510.23077](https://arxiv.org/abs/2510.23077)
- **背景与问题**: 蒸馏路线（teacher-student）的 reasoning recommender 受弱 teacher、静态监督、浅层推理迁移三大约束。
- **方法与创新**: **RecZero** 用纯 RL（GRPO + 基于规则的 reward）训练单一 LLM，自主习得 rating 预测的结构化推理（"Think-before-Recommendation" 模板：逐步分析用户兴趣/物品特征/兼容性）；**RecOne** 是先冷启动 SFT 再 RL 的混合变体。
- **实验结果**: 多个基准数据集上显著超过既有 distilled 与 LLM 基线。
- **与既有方法对比**: 与蒸馏管线（DistRec/RecPra 等）完全解耦，与 R²ec 的 RecPO、GenRec 的 GRPO-SR 同属"RL 对齐生成式推荐"家族，但走向全自主推理。

#### 3.4 Foresight: Adaptive Layer Reuse for Accelerated and High-Quality Text-to-Video Generation
- **中文标题**: Foresight：自适应层复用加速高质量文生视频
- **Authors**: Muhammad Adnan, Nithesh Kurella, Akhil Arunkumar, Prashant J. Nair
- **Affiliation**: University of British Columbia
- **Venue**: NeurIPS 2025
- **arXiv**: [2506.00329](https://arxiv.org/abs/2506.00329)
- **背景与问题**: 既有 layer-cache / 蒸馏加速方法质量损失明显，且多面向 U-Net 而非 DiT。
- **方法与创新**: 跨视频、跨 denoising step 的层复用：识别并复用语义相似的层，配 multi-level mapping refinement。
- **实验结果**: 在 OpenSora / Latte / CogVideoX 上端到端最高 **1.63×** 加速，质量指标保持。
- **与既有方法对比**: DiT 兼容、模型无关，是图生视频加速方向的高质量低成本方案。

### 4. CVPR 2026（Denver, 6/3-7）

#### 4.1 STARFlow-V: End-to-End Video Generative Modeling with Normalizing Flows
- **中文标题**: STARFlow-V：基于标准化流的端到端视频生成建模
- **Authors**: Jiatao Gu, Ying Shen, Tianrong Chen, Laurent Dinh, Yuyang Wang, Miguel Ángel Bautista, David Berthelot, Josh Susskind, Shuangfei Zhai
- **Affiliation**: Apple
- **Venue**: CVPR 2026
- **arXiv**: [2511.20462](https://arxiv.org/abs/2511.20462)
- **背景与问题**: Normalizing Flows (NF) 此前从未成功扩展到像素空间端到端视频生成——训练不稳定（KL 估计 / score matching 各分量失配）。
- **方法与创新**: 首个成功把 NF 扩展至 end-to-end（像素空间）视频生成的工作：**flow-score matching (FSM)** 损失解耦 score-matching 分量稳定训练；视频感知的 **Jacobi acceleration** 高效推理（拆分/推迟昂贵计算）；无需传统 KL 预测。保留 NF 全部优势：精确似然、标准 encoder/decoder、确定性推理。
- **实验结果**: 像素空间上的 FVD / precision-recall 达到与扩散基线竞争的水平。
- **与既有方法对比**: 相对扩散模型，NF 提供精确似然与确定性推断；本文首次弥合了此前 NF 在视频上的质量鸿沟。

#### 4.2 TGT: Text-Grounded Trajectories for Locally Controlled Video Generation
- **中文标题**: TGT：用于局部可控视频生成的文本锚定轨迹
- **Authors**: ByteDance Intelligent Creation + Johns Hopkins University
- **Affiliation**: ByteDance, JHU
- **Venue**: CVPR 2026
- **arXiv**: [2510.15104](https://arxiv.org/abs/2510.15104)
- **背景与问题**: 既有可控视频生成依赖 BB/scribble 等粗粒度条件，无法与文本语义对齐，也无法做多物体交互控制。
- **方法与创新**: 提出 **Text-Grounded Trajectories (TGT)**：用户文本描述直接实例化为轨迹 agent，通过 **Location-Aware Cross-Attention** 注入、**dual-CFG** + predictor guidance 精确引导；支持 chain-of-motion 多物体交互编辑；~2M 标注片段自动流水线。
- **实验结果**: 让现成预训练视频模型即可实现高精度局部运动控制，定量质量与可控性俱佳。
- **与既有方法对比**: 相对 GLIGEN 式 BB/scribble 控制，首次做到"文本语义 ↔ 轨迹"的直接对齐。

### 5. EMNLP 2026

#### 5.1 The Imitation Game: When LLMs Learn to Reason Like Programs via Code-Centric Reasoning Data Synthesis（MIMIC）
- **中文标题**: 模仿游戏：当 LLM 借代码中心化推理数据合成学会像程序一样推理
- **Authors**: Jinyang Zhang, Weibin Liao, Keqin Bao, Sihang Li, Shaobo Wang, Muyang Ye, Hongxin Ding, Yue Fang, Tianyi Tang, Fei Huang, Kexin Yang, Xingzhang Ren, Dayiheng Liu
- **Affiliation**: Alibaba 系（含 Qwen/通义团队作者）
- **Venue**: EMNLP 2026 main（accepted）
- **arXiv**: [2609.16076](https://arxiv.org/abs/2609.16076)
- **背景与问题**: 推理数据合成依赖语义近似的自回归验证或外部 reward model，过程监督不可靠。
- **方法与创新**: 把可执行代码作为推理数据合成"介质"：narrative fusion、code-guided test synthesis、动态 code instrumentation 三重变换把算法转成可验证的推理轨迹；显式中间执行状态构成 **Code-Instrumented Reward (CIR)**——无需外部 RM 的稠密、高保真过程监督。
- **实验结果**: SFT + GRPO 训练的模型在通用推理、复杂数学 benchmark、细粒度确定性任务上显著、一致提升。
- **与既有方法对比**: 与需要 PRM 的方案相比，用真实代码执行提供可靠过程奖励，是"程序执行"与"LLM 推理"深度耦合的代表作。

### 6. SIGGRAPH Asia 2026（Journal Track）

#### 6.1 InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular View Synthesis
- **中文标题**: InfiniSplat：大规模基线单目视角合成的隐式高斯解码
- **Affiliation**: （见 arXiv 页）
- **Venue**: SIGGRAPH Asia 2026 (Journal Track)
- **arXiv**: [2608.02437](https://arxiv.org/abs/2608.02437)
- **背景与问题**: Feed-forward 3DGS 方法在大基线/大视差下自会 collapse 或 ghosting。
- **方法与创新**: 用隐式（latent-space）高斯解码器替代直接的逐像素预测，缓解 canonical-view 视差矛盾；infinite density 估计提升跨视角外观一致性。
- **实验结果**: 跨数据集 novel-view synthesis SOTA；从 Hypersim 零样本泛化到开放世界场景，宽基线外观稳定。
- **与既有方法对比**: 相对直接回归 Gaussians 的 feed-forward 方法（大基线失真），隐式 latent 解码解决 canonical-view tradeoff。

### 7. ECML PKDD 2026

#### 7.1 The Reliability Gap in Benchmark Auditing: Distribution Shift and Scale as Failure Modes of Contamination Detection
- **中文标题**: 基准审计中的可靠性鸿沟：分布偏移与规模是污染检测的失败模式
- **Authors**: Wojciech Zarzecki, Jan Dubiński, Sebastian Cygert
- **Affiliation**: 波兰学术机构
- **Venue**: ECML PKDD 2026（accepted）
- **arXiv**: [2606.03305](https://arxiv.org/abs/2606.03305)
- **背景与问题**: 三种污染检测范式（LLM Dataset Inference、Post-Hoc DI、CoDeC）在真实审计场景（distribution shift、基准规模远小于预训练语料）下可靠性未知。
- **方法与创新**: 系统性评估 25 个模型（Pythia、OLMo 2、领域模型到 27B、前沿工业模型）、335 次评估，识别两大失败模式。
- **实验结果**: 335 次评估中仅 201 次结果正确；LLM Dataset Inference 在分布偏移下高假阳性、Post-Hoc DI 在基准规模下功效不足、CoDeC 只能给粗粒度来源信号。
- **与既有方法对比**: 结论具实操冲击力——统计检测方法尚不能替代透明数据来源披露；与 [[arxiv-ai-search|synthesis/2026-09-24/arxiv-ai-search]] 的 Contamination 争议（2609.02899）构成两种视角。

---

## Part II — 近期通用 arXiv 论文（按方向分类）

### A. LLM Reasoning & RL Post-training

#### A1. Not All LLM Reasoning is Visible in the Chain-of-Thought
- **中文标题**: LLM 的推理并不都可见于 Chain-of-Thought
- **Authors**: Vatsal Baherwani, Tom Goldstein, Ashwinee Panda
- **Affiliation**: University of Maryland
- **Venue**: arXiv preprint（2026-07, v2 2026-09）
- **arXiv**: [2607.22925](https://arxiv.org/abs/2607.22925)
- **背景与问题**: CoT 监控/可解释性的核心假设是"模型全部推理都体现为可见 token"；本工作验证该假设的边界。
- **方法与创新**: 用语义无关的 filler token 承载隐藏计算（invisible reasoning）：13 个前沿模型、3 类合成任务实证；RL 会让 Qwen3-235B 对 filler 内容形成强偏好。演示 Claude Opus 4.5 可在满足隐藏模算术约束的同时不牺牲主任务精度。
- **实验结果**: filler token 使部分模型精度最高提升 **13pp**。
- **与既有方法对比**: 首个用"无关键 token 内隐藏推理"实证否定"CoT 全可见"假设的工作，直接划定 [[concepts/verifiability]] 与 CoT 监控的边界。

#### A2. Thinking Hard, Not Smart: Reasoning Models Fail to Ration Test-Time Compute Across Questions
- **中文标题**: 思考努力而非聪明：推理模型无法跨题合理分配测试时计算
- **Authors**: Chenrui Fan, Yize Cheng, Ming Li, Yongyuan Liang, Tianyi Zhou, Soheil Feizi
- **Affiliation**: University of Maryland
- **Venue**: arXiv preprint（2026-08）
- **arXiv**: [2608.07968](https://arxiv.org/abs/2608.07968)
- **背景与问题**: 多数 TTC 评测逐题独立评测，忽略"共享预算下跨题最优分配"这一真实场景能力。
- **方法与创新**: 提出 exam-style 评测框架：多道难度/分值不同的问题共享一个 token 预算。前沿推理模型普遍表现为"贪心顺序求解"——按展示顺序前倾投入、对分值不敏感；显式 planning 提示只能让分配更均匀，不能产生分值/难度感知。
- **实验结果**: 开源与前沿闭源推理模型、数学与代码推理一致性；失败随题目数单调恶化。
- **与既有方法对比**: 与 A2（bandit 分配算法）互补：算法可行，但模型自身不会这么做——"全局预算配置"是缺失的能力维度。

#### A3. Outcome Rewards Do Not Guarantee Verifiable or Causally Important Reasoning
- **中文标题**: 结果奖励并不保证可验证或因果重要的推理
- **Authors**: Qinan Yu, Alexa Tartaglini, Peter Hase, Carlos Guestrin, Christopher Potts
- **Affiliation**: Stanford University
- **Venue**: arXiv preprint（2026-04）
- **arXiv**: [2604.22074](https://arxiv.org/abs/2604.22074)
- **背景与问题**: RLVR 提升正确率，但学到的 CoT 是否忠实表示推理过程（因果重要、对 verifier 充分）？
- **方法与创新**: 两个批判性度量：**Causal Importance of Reasoning (CIR)** 与 **Sufficiency of Reasoning (SR)**。发现：(1) RLVR 并不可靠提升 CIR/SR；(2) RLVR 前少量 SFT 可补救；(3) 叠加辅助 CIR/SR 奖励可同时获得准确率与因果充分性。
- **实验结果**: Qwen2.5 + ReasoningGym：联合奖励达到与纯 RLVR 相当的准确率，同时获得因果重要且充分的推理。
- **与既有方法对比**: 直接挑战"RLVR 学到可靠推理"假设，给出最小改动补救方案；与 A4（RLVR 激励正确推理）形成方法论对照。

### B. Scaling Laws & MoE

#### B1. Generalization and Scaling Laws for Mixture-of-Experts Transformers
- **中文标题**: MoE Transformer 的泛化与 Scaling Laws
- **Authors**: Mansour Zoubeirou a Mayaki
- **Affiliation**: LIRIS, University of Lyon 1
- **Venue**: arXiv preprint（2026-04）
- **arXiv**: [2604.09175](https://arxiv.org/abs/2604.09175)
- **背景与问题**: Chinchilla 式定律面向 dense transformer，MoE 特有的维数（专家数、激活专家数、每专家宽度）如何进入 scaling law 尚不清晰。
- **方法与创新**: 刻画总参数量 N、专家数 n_experts、激活专家数 M 与数据量 D 的交互；揭示 **constant-per-expert-width 机制**：保持每专家宽度不变只加专家数时，泛化退化被抑制——在保留计算效率的同时不损失泛化。
- **实验结果**: ELECTRA 式架构多规模实验验证：该机制下 MoE 损失随专家数的增长曲线显著更平缓。
- **与既有方法对比**: 为"带宽不变扩展"类设计（MoE 变体）提供理论支撑，与 [[concepts/shannon-scaling-law]] 的容量视角互补。

### C. Sequential Modeling

#### C1. DART: Decoded Attention over Recurrent States for Efficient Long-Context Sequence Modeling
- **中文标题**: DART：对递归状态做解码注意力实现高效长上下文建模
- **Authors**: Yixiao Qian, Song Chen, Pengkai Wang, Jiaxu Liu, Shengze Cai, Chao Xu
- **Venue**: arXiv preprint（2026-08）
- **arXiv**: [2608.02032](https://arxiv.org/abs/2608.02032)
- **背景与问题**: Mamba-2（SSD 视角）只从压缩状态 decode 出 values，不解码 keys——检索能力受限；而纯 attention 缓存开销高。
- **方法与创新**: 保留 chunked scan 产生的 chunk state 作为"chunk 记忆"，从中解码 keys+values 并做 **state-memory attention (SMA)**，gated residual 与原生 Mamba-2 输出融合；SMA 实现为 FlashAttention 风格，训练复用 Mamba-2 chunked scan。
- **实验结果**: 推理 cache 节省 **75%**（chunk size S=256、state size N=128）；相对 Mamba-2 显著提升 associative recall 与 retrieval，同时保持语言建模质量。
- **与既有方法对比**: 兼得"递归压缩"与"attention 式检索"两个范式，优于纯 mini-state 或层间 interleave 的 hybrid 方案。

### D. Agent Systems

#### D1. WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces
- **中文标题**: WeaveBench：面向混合接口计算机使用 agent 的长程真实基准
- **Authors**: Wanli Li, Bowen Zhou, Yunyao Yu, Zhou Xu, Yifan Yang, Dongsheng Li, Caihua Shan
- **Affiliation**: （Microsoft 系作者，tentative）
- **Venue**: arXiv preprint（2026-06）
- **arXiv**: [2606.09426](https://arxiv.org/abs/2606.09426)
- **背景与问题**: 既有基准把 GUI / CLI / 代码 / 浏览器分开评测，缺少跨接口长程编排的任务与评测器。
- **方法与创新**: 114 个任务、8 个真实工作域，每个任务要求同一 trajectory 内组合 GUI + CLI/code；trajectory-aware judge 检查 deliverables、截图、日志与 action trace，并检测"伪造截图/硬编码指标"作弊。
- **实验结果**: 最优 model-runtime 组合 PassRate 仅 **41.2%**，远未饱和；outcome-only 评分会显著高估 agent 表现。
- **与既有方法对比**: 相对 OSWorld 等单界面基准，首次系统检验跨接口编排并给出可检测作弊的评测器。

#### D2. Wuying-Browser-Agent: Real-World Centric Fundamental Long-Horizon Browser Agents
- **中文标题**: 无影浏览器智能体：面向真实世界的长程浏览器智能体
- **Authors**: AIMAE Team（41 人，见 arXiv）
- **Venue**: arXiv preprint（2026-08）
- **arXiv**: [2608.17319](https://arxiv.org/abs/2608.17319)
- **背景与问题**: browser agent 要在真实部署跑通需要 execution/supervision/optimization/evaluation 全管线对齐，而非只堆 scale。
- **方法与创新**: 结构化 browser harness 提供稳定执行基元；**RUIC-SFT** 用 recovery trajectory 与复杂 UI curriculum 做 SFT；**DAO-GRPO**（divergence-aware online GRPO + potential-based 奖励塑形）改进长程 credit assignment；自建 **BrowserBench**（双语、350 任务、平均 37.9 步）。
- **实验结果**: Wuying-27B 在 WebVoyager 80.6%、Online-Mind2Web 66.7%、BrowserBench 65.1%——开源 browser-use 新 SOTA；跨域迁移到 Tau2-Bench / Claw-Eval / BFCL-v4 平均 73.8。
- **与既有方法对比**: 把"恢复能力 + 复杂 UI + 长程优化"做成显式训练目标，在更长更真实的基准上验证。

#### D3. Benchmarking Open-Ended Multi-Agent Coordination in Language Agents（Alem）
- **中文标题**: 语言 agent 中开放式多智能体协作的基准化（Alem）
- **Authors**: Kale-ab Abebe Tessera 等（UCL 团队）
- **Affiliation**: UCL
- **Venue**: arXiv preprint（2026-06）
- **arXiv**: [2606.08340](https://arxiv.org/abs/2606.08340)
- **背景与问题**: 单 agent 评测成熟，开放式长程多体协作（软分工、通信、差异能力）缺少可控测试床。
- **方法与创新**: **Alem**，JAX 实现的 Craftax 风格开放式长程协作 benchmark（探索、合成、交易、战斗 + procedural 任务），以训练好的 MARL agent 为参照系。
- **实验结果**: 13 个前沿 LLM 平均仅约 **6%** normalized return；最难设定下 zero-shot Gemini-3.1-Pro-High 逼近训练 10 亿步的 MARL agent；通信是协作最大贡献因子。
- **与既有方法对比**: "个体能力≠协作能力"首次被量化，为 agent 协作瓶颈提供诊断基准。

### E. Code Execution Prediction

#### E1. Towards a Neural Debugger for Python
- **中文标题**: 迈向 Python 的神经调试器
- **Authors**: Maximilian Beck, Jonas Gehring, Jannik Kossen, Gabriel Synnaeve
- **Affiliation**: Meta（FAIR）
- **Venue**: arXiv preprint（2026-03）
- **arXiv**: [2603.09951](https://arxiv.org/abs/2603.09951)
- **背景与问题**: neural interpreter（逐行执行整段 Python）只能整段前向执行，无法交互式调试。
- **方法与创新**: 在 neural interpreter 上叠加"断点/单步进/单步跃/单步出"调试器语义，成为 **neural debugger**：可在指定行设断点、只对相关部分推理；支持 forward execution（预测未来状态/输出）与 inverse execution（反推先前状态/输入）。
- **实验结果**: CruxEval 上 output 与 input 预测任务均获强性能，稳健建模断言/条件执行语义。
- **与既有方法对比**: 首次赋予执行模型交互式调试能力，为 agentic coding 提供"debugger 世界模型"，是 FAIR CodeGen 路线的直接延伸。

### F. Video Reasoning & Generative

#### F1. TimeThink: Reasoning with Time for Video LLMs
- **中文标题**: TimeThink：强化视频大语言模型的时序推理
- **Affiliation**: （见 arXiv）
- **Venue**: arXiv preprint（2026-07）
- **arXiv**: [2607.05089](https://arxiv.org/abs/2607.05089)
- **背景与问题**: 视频 LLM 的时序推理（事件锚定、顺序、时长推断）此前主要靠 SFT/IC 或手写 prompt。
- **方法与创新**: 把时序推理建模为 step-level verifier-feedback 的强化学习问题。
- **实验结果**: 视频时序推理任务一致增益，跨多种视频 LLM 主干有效。
- **与既有方法对比**: 相对 SFT-only 的时序推理，引入 RL 学习推理链路，与 RLVR 家族同构。

### G. Benchmarks & Evaluation

#### G1. Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents
- **中文标题**: Agent Planning Benchmark：LLM agent 规划能力的诊断框架
- **Authors**: Haoyu Sun, Wenxuan Wang, Mingyang Song, Jujie He, Weinan Zhang, Yang Liu, Yang Yang, Yu Cheng
- **Affiliation**: Shanghai Jiao Tong University 等
- **Venue**: arXiv preprint（2026-06）
- **arXiv**: [2606.04874](https://arxiv.org/abs/2606.04874)
- **背景与问题**: 端到端成功掩盖了失败究竟来自 planning 还是 execution。
- **方法与创新**: 4,209 个多模态 case、22 域、5 类设定（整体规划、基于反馈的逐步规划、外置/损坏工具鲁棒性、不可解任务的拒绝）；把规划能力从端到端评测中隔离出来。
- **实验结果**: 12 个 MLLM 暴露系统性短板：长程规划、工具噪声鲁棒性、calibrated refusal、推理时修正；在 200 个 ToolSandbox 与 200 个 τ²-bench 任务上，APB 引导的 refinement 稳定提升 plan correctness 与下游执行。
- **与既有方法对比**: 与只报 e2e success 的执行类基准互补，作为"上游诊断"把失败归因到规划能力。

---

## Part III — 12 目标会议"已收录要闻导航"

以下旗舰内容此前已被各期 synthesis 覆盖（本期不重复展开），供按会议快速导航：

| Venue | 已收录要闻（wikilink → 详细页） | 关键 arXiv |
|-------|-------------------------------|-----------|
| ICML 2026 | Outstanding: The Flexibility Trap / High-Accuracy Sampling；Oral: UniAR、daVinci-Dev、MaxRL；ToT: A3C | → [[synthesis/2026-09-11/conference-digest]] |
| ICLR 2026 | Outstanding: Transformers are Inherently Succinct / LLMs Get Lost in Multi-Turn；Mamba-3、ROVER、Vid2World | → [[synthesis/2026-09-11/conference-digest]] · [[synthesis/2026-07-31/conference-digest]] |
| AAAI 2026 | Outstanding: LLM2CLIP、ReconVLA、CADYT | → [[synthesis/2026-09-05/conference-digest]] |
| NeurIPS 2025 | Best: Artificial Hivemind、Gated Attention、1000-Layer RL、Why Diffusion Don't Memorize；R²ec | → [[synthesis/2026-09-05/conference-digest]] · [[synthesis/2026-06-13/conference-digest]] |
| KDD 2026 | Shallow-scale Rec: Meta Lattice、Alibaba FAT、Kunlun、TokenMixer-Large、GPR、CONGRATS（Kuaishou）、GOAL；Ads: RankUp、CTR-Sink | → [[synthesis/2026-08-05/conference-digest]] · [[synthesis/2026-09-13/conference-digest]] |
| CVPR 2026 | Best: D4RT；HM: NitroGen、SAM 3D；DeltaTok、Flowception、TMD、Cosmos 3、Seedance 2.0 | → [[synthesis/2026-09-05/conference-digest]] · [[synthesis/2026-09-11/conference-digest]] |
| ACL 2026 | Best: Imperfective Paradox；STAPO、DeepPlanning、ViLL-E | → [[synthesis/2026-09-05/conference-digest]] · [[synthesis/2026-09-22/conference-digest]] |
| EMNLP 2025 | Best: Infini-gram mini FM-index；Parallel Continuous CoT | → [[synthesis/2026-09-05/conference-digest]] |
| SIGIR 2026 | GenRec（JD）、L2Rec、Beyond Item IDs、GBLA、KARMA、A2Gen | → [[synthesis/2026-09-05/conference-digest]] · [[synthesis/2026-08-05/conference-digest]] |
| WWW 2026 | ThinkRec、NEZHA、GenCI、OneTrans | → [[synthesis/2026-09-11/conference-digest]] |
| CIKM 2025 | Best Applied: Climber（NetEase）；RankMixer、UniROM | → [[synthesis/2026-09-05/conference-digest]] |
| RecSys 2025 | LONGER、SUAN、ULIM；Meta HSTU context parallelism | → [[synthesis/2026-09-05/conference-digest]] |

---

## 附录 Notes

- **本期去重纪律**：25 篇 featured 论文全部为 wikisibling 与既有页面 0-hit。今日 [[arxiv-ai-search|synthesis/2026-09-24/arxiv-ai-search]] / [[arxiv-daily|synthesis/2026-09-24/arxiv-daily]] / [[arxiv-paper-check|synthesis/2026-09-24/arxiv-paper-check]] 已申领窗口 ID 2609.26809–2609.28473；本文的 2609 系 ID（2609.00579 已覆盖、2609.16076 MIMIC）均低于该窗口，核验不冲突。
- **CTR 说明**：与 09 月各期一致，原始端到端 CTR/pCTR 新论文继续缺位在每日 arXiv 窗口，工业级内容由 conference 批次承载（见 Part III KDD/SIGIR/WWW 导航；最新 Raw-MARCO/GR4AD/LAMA 等在 [[synthesis/2026-08-30/conference-digest]]）。
- **tentative 标注**：World-R1 的 ICML 2026 venue 依据 proceedings 检索（tentative）；WeaveBench 的 Microsoft 归属为作者推断；Wuying 团队机构未披露。
- **未列入的候选**（检索到但未充分核验 venue/AF）：Game-TARS（2510.23691）、GameWAM（2608.26200）、ExecuCritic（2609.16604）、MIMeBench、SDK 量化 ScaleQ、DeepSeek V4（2606.19348）、Qwen3.8-Next（2608.30320，已见 tech-report-digest 09-23）。完整核验后可入后续 digest。