---
title: arXiv Daily — 2026-08-18
type: synthesis
created: 2026-08-18
updated: 2026-08-18
sources: []
tags: [arxiv, daily, llm, recommendation, ctr, advertising, games, sequential-modeling]
---

# arXiv Daily — 2026-08-18

> 自动检索并汇总近期 arXiv 上 AI、LLM、推荐系统、广告/CTR、序列建模、游戏 AI 等领域的代表性论文。每篇包含标题、作者/机构、摘要要点、核心创新及 arXiv 链接。

---

## 1. LLM / Large Language Models

### 1.1 LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models

- **Authors**: (来自 LLaDA 团队)
- **Institution**: —
- **Date**: 2026-08-04
- **Key Innovations**:
  - 系统研究 MoE 扩散语言模型 (dLLM) 的 scaling law，发现与 AR 模型存在定量差异（最优 batch size 增长更快、学习率衰减更快）
  - 训练 LLaDA MoE v2 (30B-A3B)，仅用 Qwen3 约 65% 的预训练 token (23.5T) 即可接近其性能
  - SFT 后在 8 个推理/编码基准中 7 个超越 SDAR Chat
- **Link**: https://arxiv.org/abs/2608.03457v1

### 1.2 LongCat Sparse Attention (LSA): Taming the Lightning via Streaming-aware Hierarchical Cross-Layer Indexing

- **Authors**: Meituan LongCat Team
- **Institution**: 美团
- **Date**: 2026-08-03
- **Key Innovations**:
  - 三种互补的稀疏 Attention 策略：Streaming-Aware Indexing（硬件友好内存访问）、Cross-Layer Indexing（跨层索引复用）、Hierarchical Indexing（粗到细候选筛选）
  - 在 69B-A3B 到 560B-A27B 规模验证，性能与 full attention 持平
  - 支持百万级 context length 训练，催生 LongCat-2.0 (1.6T-A48B)
  - 开源 LongCat-Flash-Lite-Sparse (69B-A3B)
- **Link**: https://arxiv.org/abs/2608.01662v2

### 1.3 Hierarchical Latent Prediction for Language Models (HiLP)

- **Authors**: —
- **Institution**: —
- **Date**: 2026-08-06
- **Key Innovations**:
  - 提出多尺度自预测学习：在 Transformer 预训练中引入分层 latent 预测，缓解 latent-space rollout 的误差累积
  - 推理时可完全移除辅助层级，零额外推理开销
  - 在 coding 和 multi-step reasoning 基准上提升性能，并改善 speculative decoding 效率
- **Link**: https://arxiv.org/abs/2608.05806v1

### 1.4 Mapping and Measuring the Behavioral Evolution of Large Language Models

- **Authors**: Dong Qiao et al.
- **Institution**: —
- **Date**: 2026-08-11
- **Key Innovations**:
  - 用 10,000 prompts 的共享回答对 32 个模型（6 个家族）进行行为特征分析
  - 三种互补的距离度量：aligned mean per-prompt distance、PCA-compressed prompt-wise disagreement、Gromov–Wasserstein discrepancy
  - 发现跨家族距离随时间缩小，近期 reasoning-oriented 模型响应更紧凑
- **Link**: https://arxiv.org/abs/2608.11027v1

### 1.5 ARCHead: Activation-Metric Residual Correction for LLM Output Heads

- **Authors**: Suayp Talha et al.
- **Institution**: —
- **Date**: 2026-08-03
- **Key Innovations**:
  - 压缩 LLM 量化后仍保留的 BF16 LM-head（输出投影层），存储降低 3.7–3.9×
  - 基于 activation-derived metric 的低秩残差修正，相对 PPL 仅 1.007
  - 可作为 AWQ/bitsandbytes 的 drop-in 补充，额外 CE 仅 +0.006–0.007
- **Link**: https://arxiv.org/abs/2608.02703v1

### 1.6 Shorter Reasoning, Earlier Answers? An Evaluation of Reasoning Interfaces

- **Authors**: Andres Algaba et al.
- **Institution**: —
- **Date**: 2026-08-04
- **Key Innovations**:
  - 在 GPQA Diamond 和 MMLU-Pro 上评估缩短推理链的效果
  - Qwen3-14B 的 numeric/concision prompt 缩短 12–17% 推理长度，准确率变化小且混合
  - 对 gpt-oss-20b/120b，低/中 effort 的 candidate-logit 答案比 matched-horizon 高 effort 高 14.5–26.3 点
  - 结论：tight deadline 下低 effort 或 concise instruction 有利，高 effort 完成后可恢复更高准确率
- **Link**: https://arxiv.org/abs/2608.03401v1

### 1.7 Reference-Free Post-Training of Open LLMs for Multilingual Machine Translation

- **Authors**: Xiaomi Research (MiLMMT Team)
- **Institution**: 小米
- **Date**: 2026-08-11
- **Key Innovations**:
  - 使用 GRPO + 参考无关质量估计奖励对 MiLMMT-46-v0.1 进行 post-training
  - 46 语言上一致提升翻译质量，12B 模型在参考无关指标上超越 Google Translate、Gemini 3 Pro 和 GPT-5
  - SFT-RL checkpoint 插值恢复 spBLEU 同时保留神经质量指标增益
  - 开源模型和代码
- **Link**: https://arxiv.org/abs/2608.10812v2

---

## 2. 推荐系统 — 序列推荐

### 2.1 Learning from the Future: Privileged Self-Distillation for Sequential Recommendation (PSD)

- **Authors**: —
- **Institution**: —
- **Date**: 2026-07
- **Key Innovations**:
  - 将序列中的 future interactions 视为训练时特权信息（inference 不可用）
  - 单一 Transformer backbone 在 privileged mask（双向）和 causal mask（部署用）两种视图下工作
  - Advantage-reachability gate 过滤不可达的 distillation 信号，momentum-averaged teacher 稳定自蒸馏
  - 零额外参数、零额外推理成本
- **Link**: https://arxiv.org/html/2607.27055

### 2.2 RecRec: Latent Interests Recursive Reasoning for Sequential Recommendation

- **Authors**: Wenhao Deng et al.
- **Institution**: —
- **Date**: 2026-07-14
- **Key Innovations**:
  - 首次将 dual-state recursive reasoning 引入序列推荐
  - Context Compressor 将 backbone hidden states 蒸馏为多向量 latent interests（Interest Diversity Regularizer 鼓励多样性）
  - Recursive Reasoner 在独立推理状态 S 中迭代精炼，GRU gate 控制对预测状态 M 的更新
  - 推理深度可在 inference 时自由调整（deep supervision + detached steps），无需重训练
  - 4 个数据集上超越 reasoning-enhanced SOTA
- **Link**: https://arxiv.org/html/2607.12945

### 2.3 GALLM: Graph-Aware Large Language Models for Sequential Recommendation

- **Authors**: —
- **Institution**: —
- **Date**: 2026-08
- **Key Innovations**:
  - 在 LLM attention 中注入协作图结构：Item–Item（全局共现）、Item–Text（语义对齐）、Text–Text（语义依赖）
  - 将图关系转换为轻量 learnable attention biases，无需外部图编码器
  - 4 个基准上 HR@5 平均提升 9.76%
- **Link**: https://arxiv.org/html/2608.12184

### 2.4 SRPFN: One Sequential Recommendation Model Pretrained from Synthetic Priors Predicts Multiple Datasets

- **Authors**: — (KDD 2026)
- **Institution**: —
- **Date**: 2026-06
- **Key Innovations**:
  - Prior-data Fitted Network 范式：在 25.6M 条合成序列（hDCSBM 先验）上预训练，推理时 zero gradient update
  - 通过 support set（目标域 item-item transition examples）条件化，单次 forward pass 适配新域
  - 跨 5 个基准平均优于第二名 7.53%，推理约 1 分钟/数据集
- **Link**: https://arxiv.org/html/2606.15752v1

### 2.5 CAST: Modeling Semantic-Level Transitions for Complementary-Aware Sequential Recommendation

- **Authors**: Qian Zhang, Lech Szymanski, Haibo Zhang, Jeremiah D. Deng
- **Institution**: —
- **Date**: 2026-04
- **Key Innovations**:
  - 在离散语义码空间建模动态语义转换（OPQ 量化 + 子空间 MLP 对齐）
  - LLM-verified complementary priors 注入 attention 机制
  - Transition-guided self-attention 学习可学习的语义转换张量
  - 65× 训练加速，Recall 提升最高 17.6%
- **Link**: https://arxiv.org/abs/2604.19414

### 2.6 Multi-LLM Token Filtering and Routing for Sequential Recommendation (MLTFR)

- **Authors**: Wuhan Chen, Min Gao et al.
- **Institution**: —
- **Date**: 2026-04
- **Key Innovations**:
  - 无需文本语料库（corpus-free），直接利用 LLM token embeddings
  - User-guided token filtering 选取任务相关 token 抑制噪声
  - 多 LLM MoE 架构 + Fisher-weighted semantic consensus expert 防止专家主导
  - 即插即用，不修改 backbone
- **Link**: https://arxiv.org/abs/2604.18200

---

## 3. CTR 预测 / 广告系统

### 3.1 GRAB: An LLM-Inspired Sequence-First CTR Prediction Modeling Paradigm (百度)

- **Authors**: Baidu Team
- **Institution**: 百度
- **Date**: 2026-02
- **Key Innovations**:
  - 端到端生成式 CTR 框架，借鉴 LLM 的 scaling 成功
  - Causal Action-aware Multi-channel Attention (CamA) 捕获时间动态和动作信号
  - Sequence-Then-Sparse (STS) 训练策略解耦稠密参数与稀疏 embedding 的优化
  - 在线 A/B：CTR +3.49%，CPM +3.05%，已全量部署
  - Scaling 表现单调近线性改善
- **Link**: https://arxiv.org/abs/2602.01865v2

### 3.2 CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer (LinkedIn)

- **Authors**: David Pardoe, Neil Daftary et al.
- **Institution**: LinkedIn
- **Date**: 2026-02
- **Key Innovations**:
  - Decoder-only Transformer 端到端广告 CTR 预测
  - Context-conditioned decoding：多 tower 预测头处理 post-scoring 信号（如广告位置），解决"鸡和蛋"问题
  - Self-gated attention 稳定训练
  - Timestamp-based RoPE 捕获秒到月的时间关系
  - Session masking 防止训练-服务偏差
  - 在线 A/B：CTR +11.04%，已部署
- **Link**: https://arxiv.org/html/2602.11410

### 3.3 EST: Efficiently Scalable Transformer for CTR Prediction (淘宝)

- **Authors**: Mingyang Liu, Yong Bai et al.
- **Institution**: 阿里巴巴/淘宝
- **Date**: 2026-02
- **Key Innovations**:
  - 全统一建模：所有原始输入（非行为特征 + 行为序列）单序列处理，无损聚合
  - Lightweight Cross Attention (LCA) 裁剪冗余自交互，聚焦跨特征依赖
  - Content Sparse Attention (CSA) 利用内容相似度动态选择高信号行为
  - 稳定幂律 scaling law，在线 A/B：RPM +3.27%，CTR +1.22%
- **Link**: https://arxiv.org/html/2602.10811

### 3.4 GenCI: Generative Modeling of User Interest Shift via Cohort-based Intent Learning for CTR Prediction (WWW 2026)

- **Authors**: —
- **Institution**: —
- **Date**: 2026-04
- **Key Innovations**:
  - 生成式用户意图框架：通过 NTP 任务生成候选兴趣 cohort（候选无关的即时意图表征）
  - 层次化 candidate-aware 网络将 cohort 注入排序阶段
  - 解决 point-wise CTR 模型的召回上下文缺失问题
- **Link**: https://arxiv.org/pdf/2601.18251

### 3.5 IDProxy: Cold-Start CTR Prediction at Xiaohongshu with Multimodal LLMs

- **Authors**: Xiaohongshu Team
- **Institution**: 小红书
- **Date**: 2026-03
- **Key Innovations**:
  - 利用 MLLM 从多模态内容信号生成 proxy embeddings，解决 item 冷启动
  - Proxy embeddings 与已有 ID embedding 空间显式对齐，端到端 CTR 优化
  - 已部署于小红书 Explore Feed（Content Feed + Display Ads），服务数亿用户
- **Link**: https://arxiv.org/abs/2603.01590v1

### 3.6 LLM-HYPER: Generative CTR Modeling for Cold-Start Ad Personalization via LLM-Based Hypernetworks

- **Authors**: —
- **Institution**: 美国头部电商平台
- **Date**: 2026-04
- **Key Innovations**:
  - 将 LLM 视为 hypernetwork，通过 few-shot CoT prompting 直接生成线性 CTR 模型权重（training-free）
  - 通过 CLIP embeddings 检索语义相似历史 campaign 作为 few-shot 示例
  - NDCG@10 较冷启动 baseline 提升 55.9%
  - 30 天在线 A/B 与 warm-start 模型性能相当，已部署
- **Link**: https://arxiv.org/html/2604.12096v1

### 3.7 Dual-Stream MLP is All You Need for CTR Prediction

- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao et al.
- **Institution**: —
- **Date**: 2026-05 (TKDD)
- **Key Innovations**：
  - 双流 MLP 架构：main MLP（通过 KD 学习显式交互）+ parallel MLP（学习隐式交互）
  - 逐步训练：distillation → alignment → overall optimization
  - 纯 MLP 实现 SOTA 性能，推理延迟与高效 baseline 相当
- **Link**: https://arxiv.org/html/2606.04944

### 3.8 Long-History User Transformers for Real-Time Ad Ranking (Yandex)

- **Authors**: Vyacheslav Ovchinnikov et al.
- **Institution**: Yandex
- **Date**: 2026-07-15
- **Key Innovations**:
  - 离线异步 Transformer 编码全量跨端交互历史 → 缓存到特征存储
  - 轻量运行时模型组合缓存表示 + 最新事件 + 请求上下文
  - 离线预训练（feedback prediction + next-item prediction），恢复 full-history 质量的 72–80%
  - 在线 A/B：search ads 指标 +2.77%，YAN +2.1%，无延迟增加
- **Link**: https://arxiv.org/html/2607.14331

### 3.9 OneRanker: Unified Generation and Ranking with One Model (腾讯微信)

- **Authors**: Tencent Team
- **Institution**: 腾讯
- **Date**: 2026-03
- **Key Innovations**:
  - Value-aware 多任务解耦架构：task token + causal mask 分离兴趣覆盖与价值优化
  - Fake Item Tokens 隐式感知 + ranking decoder 显式价值对齐
  - KV pass-through + Distribution Consistency Loss 保证输入输出双侧一致性
  - 微信视频号广告全量部署，GMV +1.34%
- **Link**: https://arxiv.org/abs/2603.02999v2

### 3.10 GR4AD: Generative Recommendation for Large-Scale Advertising (快手)

- **Authors**: Kuaishou Team
- **Institution**: 快手
- **Date**: 2026-02
- **Key Innovations**:
  - UA-SID：MLLM 微调生成广告语义 ID，MGMR RQ-Kmeans 量化
  - LazyAR decoder 放松层间自回归依赖，加速多候选生成
  - VSL + RSPO（Ranking-Guided Softmax Preference Optimization）：list-wise RL 优化业务指标
  - Dynamic Beam Serving 自适应 beam width 和流量
  - 在线 A/B：广告收入最高 +4.2%，500+ QPS，<100ms 延迟，已全量部署
- **Link**: https://arxiv.org/abs/2602.22732v1

### 3.11 LLaTTE: Scaling Laws for Multi-Stage Sequence Modeling in Large-Scale Ads (Meta)

- **Authors**: Lee Xiong et al.
- **Institution**: Meta
- **Date**: 2026-01
- **Key Innovations**:
  - 证明推荐系统序列建模遵循可预测的幂律 scaling law（类似 LLM）
  - 语义特征是 scaling 的前提条件（bend the scaling curve）
  - 两阶段架构：异步上游大模型 + 轻量在线排序模型，上游改进 ~50% transfer ratio
  - Meta 最大用户模型部署，Facebook Feed & Reels 转化率 +4.3%
- **Link**: https://arxiv.org/html/2601.20083

### 3.12 SORT: Systematically Optimized Ranking Transformer

- **Authors**: —
- **Institution**: —
- **Date**: 2026-03
- **Key Innovations**:
  - 面向工业级 ranking 的 Transformer：request-centric sample organization、local attention、query pruning、generative pre-training
  - MFU 优化至 22%，跨数据/模型/序列长度展示优秀 scaling
  - 在线 A/B：订单 +6.35%，买家 +5.97%，GMV +5.47%，延迟 -44.67%，吞吐 +121.33%
- **Link**: https://arxiv.org/abs/2603.03988v1

### 3.13 UniVA: Unified Value Alignment for Generative Recommendation (腾讯微信)

- **Authors**: Tencent Team
- **Institution**: 腾讯
- **Date**: 2026-05
- **Key Innovations**:
  - Commercial SID 将商业属性注入 token 空间
  - Generation-as-Ranking SID Decoder：生成头 + value 头联合优化（SL + eCPM-aware RL）
  - Value-Guided Personalized Beam Search：在线单次解码完成 generation + ranking
  - Offline Hit Rate@100 +37.04%，在线 GMV +1.5%
- **Link**: https://arxiv.org/html/2605.05803v1

### 3.14 MetaStrategy: Generative Ranking with Executable LLM Strategies (淘宝)

- **Authors**: —
- **Institution**: 阿里巴巴/淘宝
- **Date**: 2026-08
- **Key Innovations**:
  - LLM 生成结构化、可执行的 ranking strategy（JSON），而非直接生成 item 序列
  - Generator-Evaluator 架构：LLM 控制的 Generator 与生产系统 Generator 竞争
  - Production-path replay 训练环境 + self-competitive curriculum + Evaluator-routed on-policy distillation
  - 在线 A/B：click PV +2.11%，IPV +3.12%，交易额 +2.83%，无 RT 增加
- **Link**: https://arxiv.org/html/2608.09440

### 3.15 DEGR: Dual Exploration-Driven Generative Re-Ranking (京东)

- **Authors**: — (KDD 2026)
- **Institution**: 京东
- **Date**: 2026-08
- **Key Innovations**:
  - 混合 supervised-reinforcement 探索与优化
  - Exploratory reward model 自适应平衡即时价值与探索价值
  - Adaptive Reward-weighted ORPO + 多机制采样策略
  - 在线：UCTR +1.22%，PV +0.20%
- **Link**: https://arxiv.org/abs/2608.04809v1

---

## 4. 游戏 AI / 强化学习

### 4.1 Superhuman AI for Generals.io Using Self-Play Reinforcement Learning

- **Authors**: Matěj Straka, Viliam Lisý, Martin Schmid
- **Institution**: —
- **Date**: 2026-06-22
- **Key Innovations**:
  - JAX-native simulator：单 GPU 达 50.7M frames/sec（~10,000× 加速）
  - Vision Transformer policy 端到端 self-play RL（sparse win/loss reward，无 reward shaping）
  - Top-advantage sample filtering + EMA policy parameters
  - 公开 1v1 leaderboard #1（>5000 人类玩家），对阵顶级人类 199-70
  - 关键发现：behavior cloning、reward shaping、population-based play 均非必要
- **Link**: https://arxiv.org/html/2606.23348

### 4.2 Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via RL

- **Authors**: Chengshuai Shi et al.
- **Institution**: —
- **Date**: 2026-05-01
- **Key Innovations**:
  - 适配 PPO + 轻量 turn-level critic（非大型 model-based critic），解决 VLM 在长 horizon 任务中的训练不稳定
  - Positive-advantage filtering 改善训练稳定性
  - 预训练 VLM 提供强 action prior，显著提升 sample efficiency（对比从零训练 deep RL）
  - Open framework：SFT 初始化 + multi-task RL，跨 level 和跨游戏泛化
  - 平均游戏进度至少 3× 优于 frontier 模型
- **Link**: https://arxiv.org/html/2605.00347

### 4.3 From Player to Master: MEMOPILOT — Enhancing Test-Time Learning of LLM Agents via RL over Memory

- **Authors**: Yishuo Cai et al.
- **Institution**: —
- **Date**: 2026-06-07
- **Key Innovations**:
  - Memory Copilot：将 memory update 视为 multi-turn 决策问题，多轮 GRPO 端到端优化
  - Turn-wise reward + turn-level advantage estimation 实现细粒度 credit assignment
  - 在 RPS 和 Limit Texas Hold'em 上 Elo 评分第一（LHE 1762, RPS 1590），超越 DeepSeek V3.2
- **Link**: https://arxiv.org/html/2606.08656

### 4.4 CAST: Game Solvers as Turn-Level Teachers for LLM Agents

- **Authors**: —
- **Institution**: —
- **Date**: 2026-07
- **Key Innovations**:
  - 利用 game solver 的 state value 变化生成 turn-level credit（solver advantage）
  - 在 soft-optimal solver 假设下，最大化 solver advantage 等价于 on-policy distillation（无需 teacher logits）
  - Sokoban/Minesweeper/Rush Hour 上均达最佳，零样本迁移到 ALFWorld 和 WebShop
  - 用 ~50% 更少的训练步数达到 DAPO 的峰值性能
- **Link**: https://arxiv.org/html/2607.25308v1

### 4.5 Augmenting Game AI with Deep Reinforcement Learning (EA SPORTS FC 25)

- **Authors**: Alessandro Sestini et al.
- **Institution**: EA Sports
- **Date**: 2026-06-18
- **Key Innovations**:
  - 将 RL 应用于 AAA 游戏守门员 AI（EA SPORTS FC 25）
  - SAC + 高 update-to-data ratio + 网络重置 + 离线数据 + scenario-based training，训练时间从 4 天降至 12 小时
  - 5 层 MLP (300K params)，推理 170µs，满足 200µs 预算
  - 实战验证：RL 增强（而非替代）传统 game AI 的可行路径
- **Link**: https://arxiv.org/abs/2606.20210

### 4.6 MEMO: Memory-Augmented Model Context Optimization for Multi-Turn Multi-Agent LLM Games

- **Authors**: —
- **Institution**: —
- **Date**: 2026-03
- **Key Innovations**:
  - 无需更新权重的 self-play 框架：Retention（持久记忆库，CRUD 操作）+ Exploration（tournament-style prompt evolution + TrueSkill）
  - 均胜率从 25.1% → 49.5%（GPT-4o-mini），20.9% → 44.3%（Qwen-2.5-7B），仅用 2,000 场自我博弈
  - 对比 RL baseline 减少 19× 数据量，run-to-run variance 降低 7×
  - 谈判和不完美信息游戏增益最大
- **Link**: https://arxiv.org/abs/2603.09022v2

---

## 5. LLM + 推荐系统（Foundation Model for RecSys）

### 5.1 RecGOAT: Graph Optimal Adaptive Transport for LLM-Enhanced Multimodal Recommendation

- **Authors**: Yanzeng Li et al.
- **Institution**: —
- **Date**: 2026-02
- **Key Innovations**:
  - 解决 LLM 表征与 ID 协同信号的语义异质性
  - 双粒度对齐：instance-level（跨模态对比学习）+ distribution-level（optimal adaptive transport，最小化 1-Wasserstein 距离）
  - 理论证明统一表征的误差严格低于任何单模态表征
  - 使用 Qwen3-Embedding-8B 和 LLaVA-1.5-7B 编码多模态特征
- **Link**: https://arxiv.org/html/2602.00682

### 5.2 SAILRec: Steering LLM Attention to Dual-Side Semantically Aligned Collaborative Embeddings

- **Authors**: —
- **Institution**: —
- **Date**: 2026-06
- **Key Innovations**:
  - 双侧语义对齐：item 侧与 LLM 文本表征对齐，user 侧与 codebook-based 语义 profile 对齐
  - Hierarchical attention steering：浅层抑制过早协同干扰、中层保持自然交互、深层强化协同证据
  - 在 MovieLens-1M 和 Amazon-Book 上一致超越所有 baseline
- **Link**: https://arxiv.org/html/2606.04514v1

### 5.3 TCA4Rec: Token-level Collaborative Alignment for LLM-based Generative Recommendation

- **Authors**: Fake Lin et al.
- **Institution**: 中国科学技术大学
- **Date**: 2026-01
- **Key Innovations**:
  - Model-agnostic plug-and-play 框架：Collaborative Tokenizer 将 item-level CF logits 投影到 token-level 分布
  - Soft Label Alignment：将 CF 分布与 one-hot 监督融合为软标签，优化 soft NTP 损失
  - 显式平衡协同对齐与语义流畅性
  - 兼容任意 CF 模型（SASRec, BERT4Rec）和 decoder-based LLM（TALLRec, LLaRA, CoLLM）
- **Link**: https://arxiv.org/html/2601.18457

### 5.4 DeepInterestGR: Mining Deep Multi-Interest Using Multi-Modal LLMs for Generative Recommendation

- **Authors**: —
- **Institution**: —
- **Date**: 2026-02
- **Key Innovations**:
  - Multi-LLM Interest Mining (MLIM)：利用 GPT-5.1, Gemini-3-Pro, Kimi-K2-Thinking, Grok-4 等前沿 LLM 通过 CoT 提取深度兴趣
  - Interest-Enhanced Item Discretization (IEID)：将兴趣编码到 SID tokens
  - Interest-Aware Reward 为 RL 提供语义监督
  - 两个 Amazon 基准上较 SOTA 提升 9.2%–15.1%
- **Link**: https://arxiv.org/html/2602.18907v1

---

## 6. 其他相关

### 6.1 OctoLong: Mid-Training On Cross-Repository Code Contexts Enhances Long-Context Modeling

- **Authors**: Indraneil Paul et al.
- **Institution**: —
- **Date**: 2026-08-05
- **Key Innovations**:
  - 利用 AST parser + language server + package manager 构建跨仓库依赖丰富代码上下文（百万级 token）
  - 仅替换 12% 传统上下文扩展语料为 OctoLong 数据即显著提升 long-range retrieval 和 agentic task
  - 开源 600M–14B 参数模型套件
- **Link**: https://arxiv.org/abs/2608.05141v1

### 6.2 CMSL: Constructive Multi-Sequence Learning for Recommendation Systems

- **Authors**: Zikun Cui et al.
- **Institution**: —
- **Date**: 2026-07
- **Key Innovations**:
  - 建设性多序列学习框架（详细信息见原文）
- **Link**: https://arxiv.org/html/2606.28533

---

## 统计摘要

| 类别 | 论文数 | 代表性机构/公司 |
|------|--------|----------------|
| LLM / 基础模型 | 7 | 美团、小米、Meta |
| 序列推荐 | 6 | — |
| CTR / 广告 | 15 | 百度、LinkedIn、淘宝、小红书、腾讯、快手、Meta、Yandex、EA、京东 |
| 游戏 AI / RL | 6 | EA Sports |
| LLM + 推荐 | 5 | 中国科学技术大学 |
| 其他 | 2 | — |
| **合计** | **41** | — |

> 注：部分论文可能同时归入多个类别，此处按主要贡献归类。所有论文日期为 2026 年 1–8 月发表或提交至 arXiv。
