---
title: Conference Digest — ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025
type: synthesis
created: 2026-07-31
updated: 2026-07-31
tags: [conference-digest, icml-2026, neurips-2025, iclr-2026, aaai-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025]
sources: []
---

# 会议摘要：2025–2026 顶级 ML/AI 会议论文纵览（2026-07-31 版）

> 覆盖 ICML 2026、NeurIPS 2025、ICLR 2026、AAAI 2026、KDD 2026、CVPR 2026、ACL 2026、EMNLP 2025、SIGIR 2026、WWW 2026、CIKM 2025、RecSys 2025 的获奖论文与工业界亮点。与同日 [arXiv Daily Digest](../2026-07-31/arxiv-daily.md)、[arXiv Paper Check](../2026-07-31/arxiv-paper-check.md) 互补。

---

## 1. ICML 2026（首尔 COEX，2026年7月6–11日）

- 有效投稿：23,918 | 接受：6,352 (26.6%) | Spotlight：536 | Oral：168
- ⚠️ 评审事件：497 篇论文因违反 "LLM 参与评审" 政策被 desk-reject（AI 生成评审泛滥成为大会治理焦点）
- 获奖公告：https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/

### Outstanding Paper Awards（最佳论文奖）

#### 🏆 The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
《灵活性陷阱：重新审视扩散语言模型中任意顺序生成的价值》
- **作者**: Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang（清华大学 LeapLab / 阿里巴巴）
- **链接**: https://arxiv.org/abs/2601.15165 | https://github.com/LeapLabTHU/JustGRPO
- **核心发现**: dLLM 的任意顺序生成自由在 RL 训练中是"陷阱"——模型利用自由度回避高不确定性的"分叉词"（如 Therefore、Since），导致 entropy degradation。JustGRPO 训练时强制左到右顺序、推理时保留双向注意力 + 并行解码，GSM8K 89.1%、MATH-500 45.1%，超越全部 diffusion-RL 专门方法。
- **与前作对比**: 此前 dLLM RL 方法（DAG、DiLM 等）均保留任意顺序；本文证明顺序约束反而更好，并解释了 RL 训练中 entropy collapse 的机制。

#### 🏆 High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions
《扩散模型与对数凹分布的高精度采样》
- **作者**: Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin（MIT）
- **核心贡献**: 给出扩散模型采样的高精度理论保证，连接 log-concave 采样文献，为扩散采样器的误差界提供统一框架。

### Outstanding Position Paper

#### Position: The Alignment Community is Unintentionally Building a Censor's Toolkit
《立场：对齐社区正无意中打造审查工具箱》
- **作者**: Sarah Ball, Phil Hackemann
- **核心观点**: RLHF、红队测试等对齐工具存在双用途风险，可能被滥用于内容审查。呼吁公开反思。

### Test of Time Award

- **A3C: Asynchronous Methods for Deep Reinforcement Learning**（Mnih, Badia, Mirza, Graves, Lillicrap, Harley, Silver, Kavukcuoglu, 2016, DeepMind）— 异步优势演员-评论家方法，定义了现代深度 RL 的异步训练范式。

### Honorable Mentions（节选）

- **The Obfuscation Atlas**: 用"欺骗探针"地图刻画 RLVR 中诚实/欺骗行为的涌现位置
- **Motion Attribution for Video Generation**: 视频生成中的运动归因方法
- **How much can language models memorize?**: LLM 记忆容量量化（Meta FAIR / DeepMind / Cornell / NVIDIA，≈3.6 bits/param 量级）
- **Training AI Co-Scientists Using Rubric Rewards**: 评分奖励训练 AI 研究协作者
- **Wait, Wait, Wait… Why Do Reasoning Models Loop?**: 推理模型循环"卡死"现象归因

### 其他 Notable

- **Don't Drop Dropout**: layer dropout 在 LLM 训练中的最佳实践
- **Foundation Model Operating System (FMOS)**: 基础模型操作系统的概念框架
- **Position: To Defend Against Cyber Attacks, We Must Teach AI Agents to Hack**: 安全攻防立场论文
- **Towards A Generative Protein Evolution Machine with DPLM-Evo**: 蛋白质进化的生成模型

---

## 2. NeurIPS 2025（圣地亚哥 / 墨西哥城，2025年12月）

- 投稿：21,575 | 接受：5,290 (24.5%)
- 获奖公告：https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/

### Best Paper Awards

#### 🏆 Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
《人工蜂巢思维：语言模型（及更多）的开放域趋同》
- **作者**: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu 等
- **核心贡献**: 系统性揭示 LLM 开放问答的"趋同"现象（hivemind homogeneity），发布 INFINITY-CHAT 真实开放查询多样性数据集。
- **启示**: 对模型多样性、评估去偏、红队覆盖都有直接含义。

#### 🏆 Gated Attention: An Empirical Study
《门控注意力：一项实证研究》
- **作者**: Alibaba Qwen Team
- **核心贡献**: softmax attention 后加 head-specific sigmoid gating，提升训练稳定性、抑制 attention sink、增强长上下文；已在 Qwen3-Next 部署，30+ 组消融实验。
- **与前作对比**: 相对 standard softmax attention 与 sliding-window 方案，门控以最小参数开销获得训练稳定性收益。

#### 🏆 Why Diffusion Models Don't Memorize
《扩散模型为何不记忆》
- **作者**: Giulio Biroli 等
- **核心贡献**: 证明扩散模型训练经历"泛化→记忆"两个可预测阶段：早期与数据无关的泛化、后期线性记忆，为记忆涌现提供动力学解释。

#### 🏆 1,000 Layer Networks for Self-Supervised RL（Best Paper + Datasets & Benchmarks）
《千层自监督强化学习网络》
- **作者**: Kevin Wang, Ishaan Javali 等
- **核心贡献**: 将自监督 RL 网络从 2–5 层推至 1024 层，locomotion/manipulation 上 2–50× 性能提升；打破"深 RL 网络难训练"的经验法则。

### Runners-Up

- **Transductive Online Learning**: 解决转导在线学习 30 年悬而未决的最优错误界问题
- **Neural Scaling Laws via Superposition**: 表示叠加（representation superposition）是神经 scaling law 的核心驱动机制
- **RLVR Reasoning Capabilities**: GRPO 数学推理能力涌现研究（清华）

### Test of Time Award

- **Faster R-CNN**（Ren, He, Girshick, Sun, 2015）— 目标检测的奠基性工作。

---

## 3. ICLR 2026（里约热内卢，2026年4月23–27日）

- 投稿：≈19,000–19,525 | 接受：5,355 (27.4%) | Oral：225
- ⚠️ 评审危机：45% 评审存在身份泄露、21% 为 AI 生成评审（ICLR 2026 引发全球评审改革讨论）

### Outstanding Papers

#### 🏆 Transformers are Inherently Succinct
《Transformer 天然简洁》
- **核心贡献**: 证明 Transformer 的表达力具备"简洁性"性质（与 padded depth / width 相关的表达边界），为理解深度堆叠的必要性提供理论依据。
- **详见**: [[transformers-inherently-succinct]]

#### 🏆 LLMs Get Lost in Multi-Turn Conversation
《LLM 在多轮对话中迷失》
- **核心贡献**: 多轮对话中信息保持能力随轮次显著衰减（部分测试集 39% 性能落差），刻画 "conversation context" 丢失问题。

### Honorable Mention

- **Polar Express / Muon 优化器的极分解变体**: 以 polar decomposition 替代 Muon 的 matrix 分解，提升大模型预训练稳定性。

### 其他 Notable

- **Common Corpus**: 大规模开放伦理预训练语料
- **Q-RAG**: 用 RL 训练 embedding 实现多步检索（Oral）
- **Why DPO is a Misspecified Estimator**: 从统计层面揭露 DPO 的误设问题
- **WebDevJudge**: LLM-as-a-Judge 的网页开发评测压力测试
- **MedAgentGym**: 72,000+ 生物医学任务 Agent 训练环境
- **Mamba-3**: 混合 SSM-Attention 架构（CMU/Princeton/Together AI/Cartesia，arXiv:2603.15569，详见 topic 章节）
- **FingerTip 20K**: 主动个性化移动 LLM Agent 基准
- **ENACT**（Stanford）: 具身推理 agent 研究

---

## 4. AAAI 2026（新加坡，2026年1月20–27日）

- 投稿：23,680 | 接受：4,167 (17.6%)
- 奖项：5 篇主赛道 Outstanding Papers + 2 篇 AI for Social Impact + 1 篇 AI Alignment Track Best

### Outstanding Papers

- **CADYT: Causal Structure Learning for Dynamical Systems**: 动力学系统的因果结构学习
- **LLM2CLIP**: 用 LLM 语义对齐 CLIP 视觉-语言空间，提升零样本迁移
- **ReconVLA**: 可重构的 Vision-Language-Action 模型
- **Model Change for Description Logic Concepts**: 描述逻辑概念的模型变更问题
- **High-pass Matters for Hypergraph Neural Networks**: 超图神经网络的高通滤波重要性

### AI for Social Impact

- **PlantTraitNet**: 植物性状自动识别
- **Generalizable Slum Detection**: 可泛化的贫民窟检测

### AI Alignment Track Best Paper

- **On the Alignment of LLMs with Global Human Opinion**: LLM 与全球人类意见的对齐研究（提示 LLM 存在系统性的"西方偏见"）

### 工业界 Notable

- **BAMAS: Budget-Aware Multi-Agent Systems**: 预算感知多智能体编排，成本最高 -86%
- **ViG-RAG**: 视觉基础模型 + RAG 的视频问答

---

## 5. KDD 2026（济州岛，韩国，2026年8月9–13日）

- 双周期提交（Feb/July cycle）| 主会场：Research Track + Applied Data Science Track
- 论文页：https://kdd2026.kdd.org/papers/ | SIGKDD best paper awards 页：https://kdd.org

### 工业界亮点（部署级）

| 论文 | 机构 | 亮点 |
|------|------|------|
| **MSN**（Memory-based Sparse Activation） | ByteDance | 基于记忆的稀疏激活网络，已部署于抖音搜索 |
| **EST: Efficient Scaling Laws for CTR** | Alibaba | CTR 幂律 scaling law 实证，线上 +3.27% RPM（详见 [[est]]） |
| **ULTRA-HSTU** | Meta | HSTU 2.0：动作编码 + 半局部注意力，训练 5.3×、推理 21.4× 加速 |
| **RankElastor** | Tencent | Effective-rank 动力学视角的推荐优化（详见 [[rankelastor-recommendation]]） |
| **MTFM** | Meituan | 美团多任务排序模型 |
| **MixFormer** | ByteDance | 混合架构序列模型 |
| **DeGRe** | Alibaba | 淘宝闪购场景，部署后 +3.75% GMV |
| **Climber-Pilot** | NetEase | 高效推荐 scaling（见 [[climber-scaling-laws]]） |
| **HGenPush** | Kuaishou | 快手推送场景生成式推荐 |
| **APAO** | Tsinghua | 面向广告拍卖的优化 |
| **FuXi-Linear** | — | 时序基础模型线性化高效变体 |

> KDD 2026 正在进行（8月9–13日），正式获奖名单会后更新。

---

## 6. CVPR 2026（丹佛，2026年6月3–7日）

- 投稿：16,092 | 接受：4,089 (25.4%)
- 新闻稿：https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers

### 🏆 Best Paper: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
《一次一个 D4RT 的高效动态场景重建》
- **作者**: Google DeepMind / UCL / Oxford 团队
- **核心贡献**: 统一 transformer 同时估计深度、时空对应与相机参数，实现高可扩展 4D 动态重建，显著优于逐帧/逐对象 pipeline。

### 🏆 Best Student Paper: Native and Compact Structured Latents for 3D Generation（O-Voxel）
《原生紧凑结构化隐空间用于 3D 生成》
- **作者**: 清华 / 微软研究院 / 中科大
- **核心贡献**: 紧凑 3D 结构化隐空间（O-Voxel 体积表示），生成质量超过主流 3DGS/NeRF 生成式方法。

### Honorable Mentions

- **SAM 3D**（Meta Superintelligence Labs）: 通用 3D 分割，人工偏好 5:1 优于基线
- **NitroGen**（NVIDIA 等）: 开源通用游戏 Agent 基础模型（40K 小时数据）——CVPR 关注游戏 AI 的信号
- **Real-Time One-Step Image Editing**: 免训练免反转的单步图像编辑

### 其他 Notable

- **tttLRM**: test-time training 大型重建模型
- **CoTyle**: 风格化与文本控制的协同设计
- **BadVLM**: VLM 后门攻击分析

---

## 7. ACL 2026（圣地亚哥，2026年7月2–7日）

- 投稿：12,148 | Main：2,296 (18.9%) | Findings：2,163 (17.8%)
- ⚠️ 925 篇 desk-rejection（同比 +106%）——投稿质量/合规管控显著收紧
- 特殊主题：可解释性（Interpretability）

### Best Papers

- **The Imperfective Paradox in Large Language Models**: LLM 对"未完成体悖论"（"正在画画" vs "画了画"）的语义理解测试（LMU Munich / 东京大学）
- **Memory Efficiency and Resource-Rational Encoding in Sentence Processing**: 资源理性工作记忆分配的神经实现（UCI / UMass）
- **Characterizing the Expressivity of Local Attention in Transformers**: 局部窗口注意力的表达力精确刻画（ETH）

### Best Theme / Resource / Demo

- **CoSToM**: 心智理论（theory-of-mind）建模（Best Theme Paper）
- **HSCodeComp**: 华为代码编译 Agent 基准（Best Resource）
- **olmOCR**: 开放文档 OCR 工具（Best Demo）

### Key Trends & Notable

- **Agent & Reasoning**: 相关论文从 142 篇增至 366 篇，为最大增幅板块
- **RAG & Retrieval**: ReasonEmbed、BordaRAG 等推动检索增强推理
- **Evolutionary Guided Decoding**: 演化搜索引导解码
- **Rethinking Entropy Interventions in RLVR**: 熵干预的重新审视（浙江大学 / 腾讯）
- **MediEval**: 医疗评估基准（Dresden）
- **ViLL-E**: 视频长上下文理解（UCF）
- **Multimodal NLP**: Uni-MMMU、FastV-RAG
- **Citation Integrity**: ACL 对 AI 生成参考文献零容忍

---

## 8. EMNLP 2025（苏州，2025年11月4–9日）

- Main：1,811 (22.16%) | Findings：1,417 (17.34%) | 30 周年 | 特殊主题：效率
- Proceedings：https://aclanthology.org/2025.emnlp-main.0.pdf

### Notable Papers

- **SVIP: Self-Verification Length Policy**: 长上下文 speculative decoding 的自验证长度策略
- **Thinking Out Loud: Do Reasoning Models Know When They're Right?**: 推理模型自我认知研究
- **OmniEval**: 金融 RAG 综合评测基准
- **TreatRAG**: 药物预测 F1 0.14→0.34（BioGPT 等基准上显著提升）
- **SLoW: Select Low-frequency Words**: 低频词选择的 LLM 翻译词典
- **ViMUL-Bench**: 14 语言多语言视频 LMM 基准
- **Cross-Linguistic T2I Bias**: 语法性别如何影响文生图模型（5 性别语言 + 2 中性对照）
- **FinRetrieval**: 金融数据检索 Agent 基准（Claude Opus 结构化 API 90.8% vs 纯网页搜索 19.8%）

---

## 9. SIGIR 2026（墨尔本，2026年7月20–24日）

- 投稿：1,271 | 接受：656 篇总计（Full 234 / Perspective 12 / Reproducibility 28 / Resource 61 / Short 151 / Industry 131）
- 已接受论文页：https://sigir2026.org/en-AU/pages/program/accepted-papers

### Notable Papers（信息检索 × 推荐 × CTR 交叉）

| 论文 | 主题 | 亮点 |
|------|------|------|
| **FedMM** | 联邦 CTR | Federated Collaborative Signal Quantization for Multi-Market CTR |
| **Hypergraph Diffusion-Based Sequential Ensemble** | 序列 CTR | 超图扩散的序列集成建模 |
| **RQ-GMM** | 嵌入量化 | Residual Quantized Gaussian Mixture Models |
| **HE-DeepFM** | 隐私 CTR | 全同态加密（FHE）推理的 DeepFM |
| **Beyond Static Best-of-N** | LLM 推荐对齐 | Bayesian List-wise Alignment（贝叶斯列表级对齐） |
| **Dual-Diffusional Generative Fashion Rec** | 生成式时尚推荐 | 双扩散生成式推荐 |
| **HuffmanEmbed** | 嵌入压缩 | Huffman 编码嵌入表压缩 |
| **SORT** | 跨域检索 | Alibaba 多目标检索排序 |
| **Beyond Dense Connectivity** | 稀疏架构 | Alibaba（见 [[beyond-dense-connectivity]]） |
| **TimelineReasoner** | 时序推理 | 时序推理模型 |
| **Modular Representation Compression** | 压缩 | Huawei 模块化表示压缩 |

### 评审/产业信号

- **Perfect Personalization / Feature Selection CTR** 等继续强调可解释特征选择
- Agentic Search、查询重构漂移（When More Reformulations Hurt）等 Agent-IR 议题持续升温

---

## 10. WWW 2026（迪拜，2026年6月29日–7月3日（调整后））

- ACM 完全开放获取元年 | 研究赛道论文页：https://www2026.thewebconf.org/accepted/research-tracks.html

### Notable Papers

- **Position Auctions in AI-Generated Content**（Google: Balseiro, Mirrokni, Mehta, Paes Leme 等）: 首次理论化"AI 生成内容中的位置拍卖"——搜索/推荐混排 AI 内容时的机制设计问题，横跨机制设计 × 内容经济
- **DocResearcher: A Unified System for Multimodal Document Parsing and Deep Research**: 多模态文档解析 + 深度研究统一系统
- **GenCI: Generative CTR via Cohort Intent Learning**（详见 [[genci-ctr]]）
- **Field Matters**: 轻量 LLM 增强 CTR 模型的特征重要性视角
- **WeaveRec**: 跨域序列推荐的 model merging 方法
- **R2NS**: recall 与 rerank 阶段难负样本联合采样
- **Same Last-Item Confusion**: 会话推荐中"末项相同"混淆问题
- **Drifting with Intent: Generative Interest Trajectories**: 生成式兴趣轨迹建模

---

## 11. CIKM 2025（首尔，2025年11月10–14日）

- 投稿：2,761 | 接受：810 (29%)
- 亮点汇总：https://resources.paperdigest.org/2025/11/cikm-2025-papers-highlights

### Best Paper

#### 🏆 Generative Recommendation with Semantic IDs: A Practitioner's Handbook
《基于 Semantic IDs 的生成式推荐：实践者手册》（Meta）
- **核心贡献**: 系统化总结 semantic ID 生成式推荐的工程实践——tokenization 选择、sequence 构造、生成式推荐 vs 判别式排序的组合，成为生成式推荐从论文走向落地的操作性指南。

### Notable Papers

- **Meituan Generative Recommendation**（美团）: 基于 HSTU 的生成式推荐，同时保留 DLRM 的 cross-feature 能力——"生成式 + 判别式"混合路线的代表性工程
- **C-Former**: transformer 聚类建模超长用户生命周期行为
- **PMMAE**（微信）: 多模态掩码自编码的 CTR
- **SCV: Selectively Crossing Vectors**（NAVER）: 选择性特征交叉
- **ORCA**（NAVER）: 因果解耦的停留时长建模
- **RankMixer**（ByteDance）: 高效序列混合排序
- **Improving Text Embedding Models with Positive-aware Hard-negative Mining**（NVIDIA）: 正例感知难负样本挖掘
- **BordaRAG**（人大）: 基于排序理论的冲突文档选择
- **FollowGPT**: 从对话日志挖掘用户追问意图

---

## 12. RecSys 2025（布拉格，2025年9月22–26日）

- Challenge proceedings：https://dl.acm.org/doi/proceedings/10.1145/3758126

### Best Papers & Key Works

- **Yambda-5B**（Yandex）: 多模态大规模检索/排序数据集，推动多模态排名研究
- **RecSys Challenge 2025: Universal Behavioral Profiles**（Synerise）: 通用行为画像挑战赛，跨平台行为建模成为社区共同任务
- **TreatRAG**: 推荐场景的 RAG 药物预测，F1 大幅提升
- **Zero-shot Cross-Domain Knowledge Distillation**: YouTube → 音乐的无监督跨域迁移
- **Conformal Risk Control for Unwanted Content**: 用保形风险控制过滤不良内容推荐
- **PinFM**（Pinterest）: Pinterest 推荐基础模型
- **RES**: 播放列表生成的检索-增强序列建模

### 生成式推荐主线（跨会议回顾）

- **R²ec**（NeurIPS 2025）: 首个带推理链的统一大规模推荐模型 + RecPO RL 框架
- **RecZero**: 纯 RL（GRPO）训练 LLM 自主发展评分推理
- **OneRec / OneRec-V2**（Kuaishou）: 生成式推荐取代级联检索+排序，在线观看时长 +1.6%
- **ULTRA-HSTU**（Meta）: HSTU 2.0 训练 5.3×、推理 21.4× 加速
- **Netflix Foundation Model**: 自回归 Transformer 推荐基础模型
- **Actions Speak Louder than Words**（Meta, ICML 2024）: 生成式推荐 scaling law 开创性工作
- **Lasso**: 基于 LLM 的跨域用户模拟器

---

## 13. 主题研究精选（2026年7月 arXiv + 跨会议）

### LLM Agents & Code Execution Prediction

#### Speculate with Memory: Lossless Acceleration for LLM Agents
《与记忆一起投机：LLM Agent 的无损加速》
- **作者**: Li, Ye, Choubey, Zhang, Wu 等
- **Venue**: arXiv（2607.12236，2026-07-14）
- **核心贡献**: 用可验证的"记忆化投机执行"（memory-based speculation）预测 Agent 工具调用结果，对可验证子步骤无损加速，Agent 任务延迟显著下降。
- **与前作对比**: 相比标准 speculative decoding 依赖 draft model，本方法利用 Agent 工作流的结构化记忆，无需额外小模型。

### Sequential Modeling & Hybrid Architectures

#### Mamba-3（Princeton / CMU / Together AI / Cartesia）
- **链接**: arXiv:2603.15569 | ICLR 2026 Poster
- **核心贡献**: 第三代 Mamba 混合架构，SSM + attention 的组合在长上下文（M3 达 32K+）与效率间取得新平衡，部分推理质量超越同等规模 dense Transformer。
- **启示**: 与 Nemotron 3 的 Hybrid Mamba-Attention 相互印证，混合架构成为 2026 年主流趋势。

#### Hybrid Architectures: A Survey on Neural Networks that Mix Attention and State-Space Models
《混合架构综述：注意力与状态空间模型混合的神经网络》
- **Venue**: arXiv 2510.04800
- **核心贡献**: 系统梳理 Mamba/SSM、Hyena、Based、Mamba-2、HyenaDNA 等混合设计的权衡（质量 vs 效率 vs 记忆），归纳设计空间。

### 工业界推荐/CTR 最新（部署级）

| 论文 | 机构 | 亮点 |
|------|------|------|
| **Long-History User Transformers** | Yandex | 超长用户历史建模，排名 +2.77%、收入 +2.26%（2607.14331） |
| **TSGR** | Alibaba | 生成式推荐，IPV +0.43%、交易 +1.12%、GMV +1.64%（2607.18796） |
| **BARGE** | Tencent | 生成式推荐，CTR +0.60%（2607.21028） |
| **WhisperRec** | Kuaishou | latent reasoning 推荐（见同日 [[arxiv-paper-check]]） |
| **ShopX** | Alibaba 淘宝 | Agentic shopping 推荐基础模型（2606.31693） |
| **LoopCTR** | Alibaba | 闭环 CTR 建模（2604.19550） |
| **Diffusion-GR2** | Meta | 扩散式生成推荐（2607.01170） |
| **User Foundation Model** | RecSys'26 | 开放网页用户基础模型，CTR +2.13% |

### Games & RL

- **NitroGen**（CVPR 2026 HM）: 通用游戏 Agent 基础模型，40K 小时数据
- **AlayaWorld / ABot-World-0**: 开放实时交互世界模型
- **CausalGame**（ICML 2026 Oral）: 30 个 LLM 的因果推理游戏测试，68% vs 人类最优 82%
- **EvolvingWorld**: 57 本小说共同演化的多智能体世界

---

## 14. 综合性 Trends 分析

### 最突出的研究趋势

| 趋势 | 说明 | 代表会议 |
|------|------|----------|
| 扩散模型统治 | ICML 两项最佳论文均为扩散模型 | ICML 2026 |
| 评审治理收紧 | LLM 生成评审被禁、desk-reject 激增 | ICML 2026, ACL 2026 |
| LLM Agent 与推理 | Agent 论文数量翻倍增长 | ACL 2026, ICLR 2026 |
| 生成式推荐落地 | Semantic IDs 手册化、HSTU 2.0、美团混合路线 | CIKM 2025, KDD 2026 |
| 混合架构主流化 | Mamba-3、Nemotron 3 印证 Hybrid 趋势 | ICLR 2026 |
| 效率压倒规模 | 量化、蒸馏、压缩成为主流假设 | ICLR 2026, SIGIR 2026 |
| 对齐与安全成熟化 | DPO 被质疑、safeRL 兴起、审查双用途讨论 | ICLR 2026, ICML 2026 |
| 多模态理解深化 | 视频理解、VLM、3D 生成交叉 | CVPR 2026, ACL 2026 |
| AI 内容经济的机制设计 | AI 生成内容混排的拍卖理论 | WWW 2026 |
| 长上下文与记忆 | 多轮迷失、KV 压缩、记忆层 | ICLR 2026, NeurIPS 2025 |

### 重点实验室/公司方向

| 机构 | 重点方向 |
|------|----------|
| Google DeepMind | D4RT 4D 重建、A3C ToT、位置拍卖机制设计 |
| OpenAI | 推理模型、Agent SDK、对齐研究 |
| Anthropic | 宪法 AI、可解释性、双用途讨论 |
| Meta | ULTRA-HSTU 生成式推荐、SAM 3D、Semantic IDs 手册 |
| Microsoft | 3D 生成（O-Voxel 合作）、Phi 系列 |
| 阿里巴巴 (Qwen) | Gated Attention（NeurIPS Best）、EST/FAT CTR scaling、TSGR |
| 字节跳动 | MSN 稀疏激活、MixFormer、RankMixer |
| 快手 (Kuaishou) | OneRec、WhisperRec、HGenPush |
| NVIDIA | NitroGen 游戏 Agent、MicroMix 量化、LEAF 嵌入 |
| 清华大学 | The Flexibility Trap（ICML Best）、JustGRPO、APAO |
| Netflix | 自回归推荐基础模型 |
| Yandex | Yambda-5B、Long-History User Transformers |

---

## 15. 关键论文链接汇总

| 论文 | Venue | 链接 |
|------|-------|------|
| The Flexibility Trap | ICML 2026 | https://arxiv.org/abs/2601.15165 |
| High-Accuracy Sampling for Diffusion | ICML 2026 | https://icml.cc/virtual/2026/oral/71132 |
| ICML 2026 Awards 公告 | ICML 2026 | https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/ |
| Artificial Hivemind | NeurIPS 2025 | https://openreview.net/forum?id=saDOrrnNTz |
| NeurIPS 2025 Best Paper Awards | NeurIPS 2025 | https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/ |
| D4RT Dynamic Scene Reconstruction | CVPR 2026 | https://openaccess.thecvf.com/content/CVPR2026/html/ |
| CVPR 2026 Best Papers | CVPR 2026 | https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers |
| JustGRPO Code | ICML 2026 | https://github.com/LeapLabTHU/JustGRPO |
| SIGIR 2026 Accepted Papers | SIGIR 2026 | https://sigir2026.org/en-AU/pages/program/accepted-papers |
| WWW 2026 Research Tracks | WWW 2026 | https://www2026.thewebconf.org/accepted/research-tracks.html |
| RecSys 2025 Proceedings | RecSys 2025 | https://dl.acm.org/doi/proceedings/10.1145/3758126 |
| CIKM 2025 Highlights | CIKM 2025 | https://resources.paperdigest.org/2025/11/cikm-2025-papers-highlights |
| KDD 2026 Papers | KDD 2026 | https://kdd2026.kdd.org/papers/ |
| Mamba-3 | ICLR 2026 | https://arxiv.org/abs/2603.15569 |
| Hybrid Architectures Survey | arXiv | https://arxiv.org/abs/2510.04800 |
| Speculate with Memory | arXiv | https://arxiv.org/abs/2607.12236 |
| Long-History User Transformers | arXiv | https://arxiv.org/abs/2607.14331 |
