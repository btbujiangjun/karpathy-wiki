---
title: Conference Digest — ICML 2026, NeurIPS 2025, ICLR 2026, AAAI 2026, KDD 2026, CVPR 2026, ACL 2026, EMNLP 2025, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025
type: synthesis
created: 2026-08-01
updated: 2026-08-01
tags: [conference-digest, icml-2026, neurips-2025, iclr-2026, aaai-2026, kdd-2026, cvpr-2026, acl-2026, emnlp-2025, sigir-2026, www-2026, cikm-2025, recsys-2025]
sources: []
---

# 会议摘要：2025–2026 顶级 ML/AI 会议论文纵览（2026-08-01 版）

> 覆盖 ICML 2026、NeurIPS 2025、ICLR 2026、AAAI 2026、KDD 2026、CVPR 2026、ACL 2026、EMNLP 2025、SIGIR 2026、WWW 2026、CIKM 2025、RecSys 2025 的获奖论文与工业界亮点，并精选 2026-07-30 arXiv 新批次。与同日 [arXiv AI Research Scan](../2026-08-01/arxiv-ai-search.md) 互补（该文件已覆盖 35 篇 arXiv 论文，本文不重复）。基准版本见 [2026-07-31 Conference Digest](../2026-07-31/conference-digest.md)。

---

## 1. ICML 2026（首尔 COEX，2026年7月6–11日）

- 有效投稿：23,918 | 接受：6,352 (26.6%) | Spotlight：536 | Oral：168
- ⚠️ 评审事件：497 篇论文因违反 "LLM 参与评审" 政策被 desk-reject（AI 生成评审泛滥成为大会治理焦点）
- 获奖公告：https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/

### Outstanding Paper Awards（最佳论文奖）

#### 🏆 The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models
《灵活性陷阱：重新审视扩散语言模型中任意顺序生成的价值》
- **作者**: Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang
- **机构**: 清华大学 LeapLab / 阿里巴巴
- **Venue**: ICML 2026 Oral
- **核心发现**: dLLM 的任意顺序生成自由在 RL 训练中是"陷阱"——模型利用自由度回避高不确定性的"分叉词"（如 Therefore、Since），导致 entropy degradation。JustGRPO 训练时强制左到右顺序、推理时保留双向注意力 + 并行解码，GSM8K 89.1%、MATH-500 45.1%，超越全部 diffusion-RL 专门方法。
- **与前作对比**: 此前 dLLM RL 方法（DAG、DiLM 等）均保留任意顺序；本文证明顺序约束反而更好，并解释了 RL 训练中 entropy collapse 的机制。
- **链接**: https://arxiv.org/abs/2601.15165 | https://github.com/LeapLabTHU/JustGRPO

#### 🏆 High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions
《扩散模型与对数凹分布的高精度采样》
- **作者**: Fan Chen, Sinho Chewi, Constantinos Daskalakis, Alexander Rakhlin
- **机构**: MIT
- **Venue**: ICML 2026 Oral
- **核心贡献**: 给出扩散模型采样的高精度理论保证，连接 log-concave 采样文献，为扩散采样器的误差界提供统一框架。

### Outstanding Position Paper

- **Position: The Alignment Community is Unintentionally Building a Censor's Toolkit**（Sarah Ball, Phil Hackemann）— RLHF、红队测试等对齐工具存在双用途风险，可能被滥用于内容审查。

### Test of Time Award

- **A3C: Asynchronous Methods for Deep Reinforcement Learning**（Mnih 等, 2016, DeepMind）— 异步优势演员-评论家方法。

### Honorable Mentions（节选）

- **The Obfuscation Atlas**: RLVR 中诚实/欺骗行为涌现位置的"欺骗探针"地图
- **How much can language models memorize?**: Meta FAIR / DeepMind / Cornell / NVIDIA，≈3.6 bits/param 量级记忆容量
- **Training AI Co-Scientists Using Rubric Rewards**: 评分奖励训练 AI 研究协作者
- **Wait, Wait, Wait… Why Do Reasoning Models Loop?**: 推理模型循环"卡死"现象归因
- **CausalGame**（Oral）: 30 个 LLM 的因果推理游戏测试，68% vs 人类最优 82%

---

## 2. NeurIPS 2025（圣地亚哥 / 墨西哥城，2025年12月）

- 投稿：21,575 | 接受：5,290 (24.5%)
- 获奖公告：https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/

### Best Paper Awards

#### 🏆 Gated Attention: An Empirical Study
《门控注意力：一项实证研究》
- **作者**: Alibaba Qwen Team
- **核心贡献**: softmax attention 后加 head-specific sigmoid gating，提升训练稳定性、抑制 attention sink、增强长上下文；已在 Qwen3-Next 部署，30+ 组消融实验。

#### 🏆 Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
《人工蜂巢思维：语言模型（及更多）的开放域趋同》
- **作者**: Liwei Jiang 等
- **核心贡献**: 系统性揭示 LLM 开放问答的"趋同"现象，发布 INFINITY-CHAT 真实开放查询多样性数据集。

#### 🏆 Why Diffusion Models Don't Memorize
《扩散模型为何不记忆》
- **核心贡献**: 证明扩散模型训练经历"泛化→记忆"两个可预测阶段，为记忆涌现提供动力学解释。

#### 🏆 1,000 Layer Networks for Self-Supervised RL（Best Paper + Datasets & Benchmarks）
《千层自监督强化学习网络》
- **核心贡献**: 将自监督 RL 网络从 2–5 层推至 1024 层，locomotion/manipulation 上 2–50× 性能提升。

### Test of Time Award

- **Faster R-CNN**（Ren, He, Girshick, Sun, 2015）— 目标检测奠基性工作。

---

## 3. ICLR 2026（里约热内卢，2026年4月23–27日）

- 投稿：≈19,000–19,525 | 接受：5,355 (27.4%) | Oral：225
- ⚠️ 评审危机：45% 评审存在身份泄露、21% 为 AI 生成评审

### Outstanding Papers

#### 🏆 Transformers are Inherently Succinct
《Transformer 天然简洁》
- **核心贡献**: 证明 Transformer 表达力具备"简洁性"性质，为理解深度堆叠必要性提供理论依据。

#### 🏆 LLMs Get Lost in Multi-Turn Conversation
《LLM 在多轮对话中迷失》
- **核心贡献**: 多轮对话信息保持能力随轮次显著衰减（部分测试集 39% 性能落差）。

### Honorable Mention

- **Polar Express / Muon 优化器极分解变体**: 提升大模型预训练稳定性。

### 其他 Notable

- **Mamba-3**: 混合 SSM-Attention 架构（CMU/Princeton/Together AI/Cartesia，arXiv:2603.15569）
- **Q-RAG**: 用 RL 训练 embedding 实现多步检索（Oral）
- **Why DPO is a Misspecified Estimator**: 统计层面揭露 DPO 的误设问题
- **MedAgentGym**: 72,000+ 生物医学任务 Agent 训练环境
- **FingerTip 20K**: 主动个性化移动 LLM Agent 基准

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

### AI Alignment Track Best Paper

- **On the Alignment of LLMs with Global Human Opinion**: LLM 与全球人类意见的对齐（提示 LLM 存在系统性"西方偏见"）

### 工业界 Notable

- **BAMAS: Budget-Aware Multi-Agent Systems**: 预算感知多智能体编排，成本最高 -86%

---

## 5. KDD 2026（济州岛，2026年8月9–13日，进行中）

- 双周期提交（Feb/July cycle）| Research Track + Applied Data Science Track
- 论文页：https://kdd2026.kdd.org/papers/

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

> KDD 2026 正式获奖名单 8/9–13 会后更新。

---

## 6. CVPR 2026（丹佛，2026年6月3–7日）

- 投稿：16,092 | 接受：4,089 (25.4%)

### 🏆 Best Paper: Efficiently Reconstructing Dynamic Scenes One D4RT at a Time
《一次一个 D4RT 的高效动态场景重建》
- **作者**: Google DeepMind / UCL / Oxford
- **核心贡献**: 统一 transformer 同时估计深度、时空对应与相机参数，实现高可扩展 4D 动态重建。

### 🏆 Best Student Paper: Native and Compact Structured Latents for 3D Generation（O-Voxel）
《原生紧凑结构化隐空间用于 3D 生成》
- **作者**: 清华 / 微软研究院 / 中科大
- **核心贡献**: 紧凑 3D 结构化隐空间（O-Voxel 体积表示），生成质量超过主流 3DGS/NeRF 生成式方法。

### Honorable Mentions

- **SAM 3D**（Meta Superintelligence Labs）: 通用 3D 分割，人工偏好 5:1 优于基线
- **NitroGen**（NVIDIA 等）: 开源通用游戏 Agent 基础模型（40K 小时数据）
- **Real-Time One-Step Image Editing**: 免训练免反转的单步图像编辑

---

## 7. ACL 2026（圣地亚哥，2026年7月2–7日）

- 投稿：12,148 | Main：2,296 (18.9%) | Findings：2,163 (17.8%)
- ⚠️ 925 篇 desk-rejection（同比 +106%）——投稿质量/合规管控显著收紧
- 特殊主题：可解释性（Interpretability）

### Best Papers

- **The Imperfective Paradox in Large Language Models**: LLM 对"未完成体悖论"的语义理解测试（LMU Munich / 东京大学）
- **Memory Efficiency and Resource-Rational Encoding in Sentence Processing**: 资源理性工作记忆分配的神经实现（UCI / UMass）
- **Characterizing the Expressivity of Local Attention in Transformers**: 局部窗口注意力表达力精确刻画（ETH）

### Best Theme / Resource / Demo

- **CoSToM**: 心智理论（theory-of-mind）建模（Best Theme）
- **HSCodeComp**: 华为代码编译 Agent 基准（Best Resource）
- **olmOCR**: 开放文档 OCR 工具（Best Demo）

### Key Trends

- **Agent & Reasoning**: 相关论文从 142 篇增至 366 篇，为最大增幅板块
- **Citation Integrity**: ACL 对 AI 生成参考文献零容忍

---

## 8. EMNLP 2025（苏州，2025年11月4–9日）

- Main：1,811 (22.16%) | Findings：1,417 (17.34%) | 30 周年 | 特殊主题：效率

### Notable Papers

- **SVIP: Self-Verification Length Policy**: 长上下文 speculative decoding 的自验证长度策略
- **TreatRAG**: 药物预测 F1 0.14→0.34
- **FinRetrieval**: 金融数据检索 Agent 基准（Claude Opus 结构化 API 90.8% vs 纯网页搜索 19.8%）
- **Cross-Linguistic T2I Bias**: 语法性别如何影响文生图模型
- **ViMUL-Bench**: 14 语言多语言视频 LMM 基准

---

## 9. SIGIR 2026（墨尔本，2026年7月20–24日）

- 投稿：1,271 | 接受：656 篇总计（Full 234 / Perspective 12 / Reproducibility 28 / Resource 61 / Short 151 / Industry 131）

### Notable Papers（信息检索 × 推荐 × CTR 交叉）

| 论文 | 主题 | 亮点 |
|------|------|------|
| **FedMM** | 联邦 CTR | Federated Collaborative Signal Quantization for Multi-Market CTR |
| **HE-DeepFM** | 隐私 CTR | 全同态加密（FHE）推理的 DeepFM |
| **RQ-GMM** | 嵌入量化 | Residual Quantized Gaussian Mixture Models |
| **Beyond Static Best-of-N** | LLM 推荐对齐 | Bayesian List-wise Alignment |
| **HuffmanEmbed** | 嵌入压缩 | Huffman 编码嵌入表压缩 |
| **SORT** | 跨域检索 | Alibaba 多目标检索排序 |
| **TimelineReasoner** | 时序推理 | 时序推理模型 |
| **Modular Representation Compression** | 压缩 | Huawei 模块化表示压缩 |

---

## 10. WWW 2026（迪拜，2026年6月29日–7月3日）

- ACM 完全开放获取元年

### Notable Papers

- **Position Auctions in AI-Generated Content**（Google: Balseiro, Mirrokni, Mehta, Paes Leme 等）: 首次理论化"AI 生成内容中的位置拍卖"——搜索/推荐混排 AI 内容时的机制设计问题
- **DocResearcher: A Unified System for Multimodal Document Parsing and Deep Research**: 多模态文档解析 + 深度研究统一系统
- **GenCI: Generative CTR via Cohort Intent Learning**（详见 [[genci-ctr]]）
- **WeaveRec**: 跨域序列推荐的 model merging
- **R2NS**: recall 与 rerank 阶段难负样本联合采样

---

## 11. CIKM 2025（首尔，2025年11月10–14日）

- 投稿：2,761 | 接受：810 (29%)

### Best Paper

#### 🏆 Generative Recommendation with Semantic IDs: A Practitioner's Handbook
《基于 Semantic IDs 的生成式推荐：实践者手册》（Meta）
- **核心贡献**: 系统化总结 semantic ID 生成式推荐的工程实践——tokenization 选择、sequence 构造、生成式 vs 判别式排序组合，成为生成式推荐落地的操作性指南。

### Notable Papers

- **Meituan Generative Recommendation**: HSTU 生成式推荐 + DLRM cross-feature 的"生成式 + 判别式"混合路线
- **C-Former**: transformer 聚类建模超长用户生命周期行为
- **RankMixer**（ByteDance）: 高效序列混合排序
- **BordaRAG**（人大）: 基于排序理论的冲突文档选择

---

## 12. RecSys 2025（布拉格，2025年9月22–26日）

### Best Papers & Key Works

- **Yambda-5B**（Yandex）: 多模态大规模检索/排序数据集
- **RecSys Challenge 2025: Universal Behavioral Profiles**（Synerise）: 通用行为画像挑战赛
- **PinFM**（Pinterest）: Pinterest 推荐基础模型
- **Zero-shot Cross-Domain Knowledge Distillation**: YouTube → 音乐的无监督跨域迁移
- **Conformal Risk Control for Unwanted Content**: 保形风险控制过滤不良内容推荐

### 生成式推荐主线（跨会议回顾）

- **R²ec**（NeurIPS 2025）: 首个带推理链的统一大规模推荐模型 + RecPO RL 框架
- **OneRec / OneRec-V2**（Kuaishou）: 生成式推荐取代级联检索+排序，在线观看时长 +1.6%
- **ULTRA-HSTU**（Meta）: HSTU 2.0 训练 5.3×、推理 21.4× 加速
- **Actions Speak Louder than Words**（Meta, ICML 2024）: 生成式推荐 scaling law 开创性工作

---

## 13. 最新 arXiv 精选（2026-07-30 批次）

> 六篇尚未被同日 [arXiv AI Research Scan](../2026-08-01/arxiv-ai-search.md) 覆盖的新论文（已验证 arXiv API）。均已注明 7 项字段（中英标题、作者、机构、Venue、摘要与创新、对比、链接）。

### Vision-Language / 长视觉上下文

#### ReToken: One Token to Improve Vision-Language Models for Visual Retrieval
《ReToken：一个 Token 提升视觉-语言模型的视觉检索能力》
- **作者**: Yao Xiao, Reuben Tan, Zhen Zhu, Yuqun Wu, Jianfeng Gao, Derek Hoiem
- **机构**: UIUC / Microsoft Research（含 Jianfeng Gao, Derek Hoiem）(tentative)
- **Venue**: arXiv 2607.28627（2026-07-30）
- **核心贡献**: 用单个可学习 embedding 作为显式检索目标（retrieval token），从预填充的视觉 KV cache 中选取稀疏的 query 相关视觉 token。只需小规模 image-QA 数据集训练，Visual Haystacks 上 Qwen3VL-8B +13.4 分、InternVL3.5 +12.4 分（>20% 相对提升）；LVBench 上零样本迁移到长视频，Qwen3VL-8B +8.0 分。轻量设计使训练与长视频推理均可跑在单张 H100 上。
- **与前作对比**: 相比全量注意力（随 distractor 增加性能下降、GPU 显存不可行）与依赖外部检索器的方法，ReToken 直接在预填充 KV cache 内检索，成本极低且免额外模型。
- **链接**: https://arxiv.org/abs/2607.28627 | https://github.com/avaxiao/ReToken

### 金融 × LLM

#### Can Large Language Models Execute Parent Orders? (PACE)
《大语言模型能执行母单吗？》
- **作者**: Zane Shen, Xinli Xu, Guangyi Zhang, Jialong Chen, Jinsong Zhou, Cong Chen, Guibao Shen, Dongyu Yan, Luozhou Wang, Zhen Yang
- **机构**: 中国金融科技/量化机构（含券商背景，具体机构未披露）(tentative)
- **Venue**: arXiv 2607.28410（2026-07-30）
- **核心贡献**: 首个系统研究 LLM 用于 parent-order execution（把大单拆成小单、降低执行成本）的论文，把 LLM 在金融中的应用从"买什么"（what to trade）推进到"怎么执行"（how to execute）。提出 PACE（Plan-Ahead Controlled Execution）分层框架：长时程规划 + 短时程执行，无需显式市场假设或任务特定训练。在深交所 Level-1 数据上超越 TWAP、Almgren-Chriss 和学习型基线，比最强基线高 0.65 bps。
- **与前作对比**: 传统方法依赖预先指定的市场假设（如 Almgren-Chriss）或需任务特定训练；PACE 既无假设也无需专门训练。行为分析发现 LLM 高置信度预测更好（而非收益更差）、且更早交易而非拖到截止时间。
- **链接**: https://arxiv.org/abs/2607.28410

### Multimodal Agent 可信推理

#### LedgerMind: Provenance-Constrained Multimodal Agentic Reasoning with a Structured Evidence Ledger
《LedgerMind：结构化证据账本约束来源的多模态 Agent 推理》
- **作者**: Enjun Du, Hange Zhou, Chenxu Du, Siyi Liu, Zirong Chen, Ziyu Zheng, Yongqi Zhang
- **机构**: N/A（机构未披露）(single-source)
- **Venue**: arXiv 2607.28374（2026-07-30）
- **核心贡献**: 把多模态 Agent 轨迹视为"来源受限的状态机"：工具输出归一化为 Structured Evidence Ledger（轨迹状态），下游推理/决策只能引用活跃账本条目，grounding 在实体与数值层面被检查，修复被实现为有类型的状态转移（不能引入无工具来源的内容）。配套 Three-Layer Grounding Protocol、Adaptive Dual-Path Dispatcher（按问题复杂度匹配推理深度）、Event-Triggered Verification-and-Repair（带形式化的 provenance non-amplification 保证）。
- **与前作对比**: 传统评估只看 final-answer accuracy，无法区分"grounded 证据"与"语言先验/错误抵消"；LedgerMind 直接针对四类被 accuracy 掩盖的失败模式——无支撑中间推理、引用性实体幻觉（Phantom Grounding）、简单问题上的 over-reasoning、修复时放大。
- **链接**: https://arxiv.org/abs/2607.28374

### 视频世界模型

#### ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamics Representations from a Video and Its Shadow
《ShadowDancer：从视频与其"影子"学习统一动力学表示，教会视频世界模型任意动作》
- **作者**: Jin Cao, Zian Meng, Kaipeng Zhang
- **机构**: 上海人工智能实验室 / N/A (tentative)
- **Venue**: arXiv 2607.28362（2026-07-30）
- **核心贡献**: 面向交互式视频世界模型的任意动作、帧级控制。核心是表示问题：现有接口要么松编码动作（模型即兴发挥）、要么精确编码但只服务单一 dynamics family 且难以获取。两大创新：(1) shadow pairs——用 Shadow Library 大规模构造"同一动力学、独立重采样外观"的视频对，使动力学族可控当且仅当能构造这样的对；(2) cross-shadow prediction——用一个影子预测另一个，被重采样的外观被构造性丢弃、被保留的成为动作，得到统一动力学表示驱动 block-causal 世界模型。无需 action labels、motion estimators 或 fine-tuning。
- **与前作对比**: 相对 latent-action 与交互式世界模型基线，动作迁移与长动作 rollout 显著改善，rollout 对比平均盲胜率 86%。
- **链接**: https://arxiv.org/abs/2607.28362 | https://ShadowDancer-1.github.io

### MoE 推理数值稳定性

#### From Expert Reduction to Behavioral Divergence: Tracing Numerical State through Sparse MoE Inference
《从专家归约到行为发散：追踪稀疏 MoE 推理中的数值状态》
- **作者**: Tianyang Zhu
- **机构**: N/A（作者独立）(tentative)
- **Venue**: arXiv 2607.28097（2026-07-30）
- **核心贡献**: 证明数学上等价的 expert-reduction 顺序可产生可观测不同的稀疏 MoE 执行。在原生 DeepSeek-V4-Flash 上冻结局部 MoE 状态、仅改变聚合语义做隔离实验：第 5 层一个 fork 处，720 种 A-mode 顺序产生 10 个 continuation basins，720 种 B-mode 顺序形成 360 个精确结构类、11 个 basins。识别出 post-mHC 是 intra-token 边界、full persistent state 是 cross-token 延续边界——相同 token 不必然意味着相同的自回归状态。
- **与前作对比**: 揭示同一模型的确定性推理可因归约顺序产生行为分歧，把专家操作数转换、累加器精度、归约顺序纳入 sparse-MoE 运行时与硬件后端的"数值兼容契约"。（作者强调是受控因果可能性，非部署发生率。）
- **链接**: https://arxiv.org/abs/2607.28097

### 大动作空间策略学习（博士论文）

#### On-Policy and Off-Policy Learning for Large Action Spaces
《大动作空间中的在线与离线策略学习》
- **作者**: Imad Aouali
- **机构**: CentraleSupélec / Université Paris-Saclay（博士论文，241 页）(tentative)
- **Venue**: arXiv 2607.28408（2026-07-30）
- **核心贡献**: 博士论文，研究上下文 bandit 两大范式中大动作空间的策略学习。(1) on-policy：meTS（mixed-effect Thompson sampling）、dTS（diffusion 先验 TS），跨动作共享信息，遗憾界依赖有效动作数；(2) off-policy：sDM（结构化直接方法）、可凹且高效优化的 policy-weighted log-likelihood 目标、基于指数平滑与 PAC-Bayesian 界的可微悲观方法，控制正则化重要性采样估计的偏差-方差权衡。
- **与前作对比**: 针对大动作空间的主要挑战（探索低效、数据覆盖稀疏、重要性权重高方差、外推偏差、优化困难）逐项提出结构化解法。
- **链接**: https://arxiv.org/abs/2607.28408

> 同日 arXiv 批次的其余重要论文（Sample More, Reflect Less；Change2Task；CoMem；Coherent Overlap in Sparse MoE；ReTopK；ORCA-bench 等）已在 [arXiv AI Research Scan](../2026-08-01/arxiv-ai-search.md) 覆盖。

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
| 长上下文与记忆 | 多轮迷失、KV 压缩、记忆层、检索 token | ICLR 2026, NeurIPS 2025, arXiv |
| MoE 数值契约 | 归约顺序/精度影响行为，浮现运行时兼容性要求 | arXiv 2026-07 |
| 可信 Agent 推理 | 来源约束、证据账本、可审计轨迹 | arXiv 2026-07 |

### 重点实验室/公司方向

| 机构 | 重点方向 |
|------|----------|
| Google DeepMind | D4RT 4D 重建、A3C ToT、位置拍卖机制设计 |
| Meta | ULTRA-HSTU 生成式推荐、SAM 3D、Semantic IDs 手册 |
| Microsoft | 3D 生成（O-Voxel 合作）、ReToken 视觉检索、Phi 系列 |
| 阿里巴巴 (Qwen) | Gated Attention（NeurIPS Best）、EST/FAT CTR scaling、TSGR |
| 字节跳动 | MSN 稀疏激活、MixFormer、RankMixer |
| 快手 (Kuaishou) | OneRec、WhisperRec、HGenPush |
| NVIDIA | NitroGen 游戏 Agent、SAM 3D、MicroMix 量化 |
| 清华大学 | The Flexibility Trap（ICML Best）、JustGRPO、CoMem |
| UIUC | ReToken 视觉检索（与 MSR 合作） |
| 上海人工智能实验室 | ShadowDancer 视频世界模型 |

---

## 15. 关键论文链接汇总

| 论文 | Venue | 链接 |
|------|-------|------|
| The Flexibility Trap | ICML 2026 | https://arxiv.org/abs/2601.15165 |
| ICML 2026 Awards 公告 | ICML 2026 | https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/ |
| NeurIPS 2025 Best Paper Awards | NeurIPS 2025 | https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/ |
| Artificial Hivemind | NeurIPS 2025 | https://openreview.net/forum?id=saDOrrnNTz |
| CVPR 2026 Best Papers | CVPR 2026 | https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers |
| SIGIR 2026 Accepted Papers | SIGIR 2026 | https://sigir2026.org/en-AU/pages/program/accepted-papers |
| KDD 2026 Papers | KDD 2026 | https://kdd2026.kdd.org/papers/ |
| Mamba-3 | ICLR 2026 | https://arxiv.org/abs/2603.15569 |
| ReToken | arXiv | https://arxiv.org/abs/2607.28627 |
| PACE (Parent Orders) | arXiv | https://arxiv.org/abs/2607.28410 |
| LedgerMind | arXiv | https://arxiv.org/abs/2607.28374 |
| ShadowDancer | arXiv | https://arxiv.org/abs/2607.28362 |
| Expert Reduction → Behavioral Divergence | arXiv | https://arxiv.org/abs/2607.28097 |
| On/Off-Policy Learning for Large Action Spaces | arXiv | https://arxiv.org/abs/2607.28408 |
