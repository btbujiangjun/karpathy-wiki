---
title: "arXiv AI/LLM/推荐/广告/游戏 近期论文搜索报告"
type: synthesis
created: 2026-08-19
updated: 2026-08-19
tags: [arxiv, CTR, recommendation, LLM, games, advertising, sequential-modeling, scaling-law]
---

# arXiv 近期论文搜索报告 — AI / LLM / 推荐 / 广告 / 游戏

> 搜索日期：2026-08-19 | 覆盖范围：2026 年 1–8 月 arXiv 预印本

---

## 一、CTR 预测 & 广告排序

### 1. DeRes: Decoupling Residual Stability and Adaptivity for Scalable CTR Prediction

| 字段 | 内容 |
|------|------|
| **Authors** | Wenzhuo Cheng, Shipeng Nie, Qixin Guo, Xuefeng Sun, Jianguo Lou, Zhengwei Zheng |
| **Institution** | 未明确（工业场景） |
| **Key Innovation** | 首次将 Attention Residual 引入 CTR Transformer；提出 DPN 风格双路径连接器 DeRes（Identity + Block Attention Residual），以及 Pointwise AttnRes（用 SiLU 替换 Softmax 以支持非竞争性多兴趣编码） |
| **Core Result** | 在 331M 交互的大规模工业数据集上 AUC 提升 +0.32%，8 层 DeRes ≈ 16 层 OneTrans（2× 计算节省），compute–AUC scaling law slope 0.118 vs OneTrans 0.071 |
| **arXiv** | [https://arxiv.org/abs/2606.07980](https://arxiv.org/abs/2606.07980) |

---

### 2. Dual-Stream MLP is All You Need for CTR Prediction

| 字段 | 内容 |
|------|------|
| **Authors** | Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen |
| **Institution** | Renmin University of China |
| **Key Innovation** | 提出 DS-MLP 框架，通过 distillation→alignment→overall optimization 三步渐进式构建双流 MLP，主 MLP 学习显式高阶交互，辅助 MLP 学习隐式交互，对齐两流消除分布偏差 |
| **Core Result** | 在三个 CTR benchmark 上一致超越所有 baseline（包括 DCNv2、DeepFM 等），推理延迟与高效模型持平 |
| **arXiv** | [https://arxiv.org/abs/2606.04944](https://arxiv.org/abs/2606.04944) |

---

### 3. LENS: A Staged Design for Interaction Granularity in Sequential CTR Prediction

| 字段 | 内容 |
|------|------|
| **Authors** | 未完整列出 |
| **Key Innovation** | 提出分阶段交互粒度设计框架：Stage 2（QueryPos 位置先验）+ Stage 3（LENS 目标条件查询路由）；发现密度驱动条件源规则——item 密度 < ~50 时需额外序列上下文 |
| **Core Result** | 在 HyFormer / MixFormer / OneTrans 三个 backbone 和四个数据集上 12 个 backbone×dataset 组合均为正增益 |
| **arXiv** | [https://arxiv.org/abs/2605.25583](https://arxiv.org/abs/2605.25583) |

---

### 4. PaletteID: Prototype-Composed Semantic Identifiers for Multimodal CTR Prediction

| 字段 | 内容 |
|------|------|
| **Authors** | Huanyu Liu et al. |
| **Key Innovation** | 用原型调色板（SQ-DPP 选择）替代 codebook 量化，将多模态 embedding 表示为连续相似度加权的原型组合，解决 SID 离散化丢失语义连续性和前缀码限制的问题 |
| **Core Result** | 在两个公开数据集上 CTR AUC 一致提升，长尾物品增益更大，比现有 SID 方法更鲁棒可解释 |
| **arXiv** | [https://arxiv.org/abs/2607.29000](https://arxiv.org/abs/2607.29000) |

---

### 5. GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm

| 字段 | 内容 |
|------|------|
| **Authors** | Baidu 广告团队 |
| **Institution** | Baidu |
| **Key Innovation** | 端到端生成式 CTR 框架，引入 Causal Action-aware Multi-channel Attention (CamA) 捕获时序动态和动作信号；STS 训练范式解决 sequence packing 分布偏移 |
| **Core Result** | 百度 feed 广告上线：CTR +3.49%, CPM +3.05%；AUC 随序列长度和模型容量单调线性提升 |
| **arXiv** | [https://arxiv.org/abs/2602.01865](https://arxiv.org/abs/2602.01865) |

---

### 6. SparseCTR: Unleashing the Potential of Sparse Attention on Long-term Behaviors for CTR Prediction

| 字段 | 内容 |
|------|------|
| **Authors** | Weijiang Lai et al. |
| **Key Innovation** | 个性化时间感知分块 + 三分支稀疏自注意力（全局兴趣 / 兴趣迁移 / 短期兴趣）+ 可学习头部级相对时序编码；在三个数量级 FLOPs 范围内展现明显 scaling law |
| **Core Result** | 线上 A/B：CTR +1.72%, CPM +1.41%；推理时间 40ms，序列长度 1024 |
| **arXiv** | [https://arxiv.org/abs/2601.17836](https://arxiv.org/abs/2601.17836) |
| **Code** | [https://github.com/laiweijiang/SparseCTR](https://github.com/laiweijiang/SparseCTR) |

---

### 7. LoopCTR: Unlocking the Loop Scaling Power for Click-Through Rate Prediction

| 字段 | 内容 |
|------|------|
| **Authors** | Jiakai Tang et al. |
| **Key Innovation** | 提出 loop scaling 范式：通过共享层的递归复用增加训练时计算，解耦计算与参数增长；train-multi-loop, infer-zero-loop 策略 |
| **Core Result** | 三个公开 benchmark + 一个工业数据集上 SOTA；oracle 分析显示 0.02–0.04 AUC 未挖掘空间 |
| **arXiv** | [https://arxiv.org/abs/2604.19550](https://arxiv.org/abs/2604.19550) |

---

### 8. Long-History User Transformers for Real-Time Ad Ranking

| 字段 | 内容 |
|------|------|
| **Authors** | Vyacheslav Ovchinnikov, G.G. Smirnov, Nikolai Savushkin, Veronika Ivanova, Maksim Kuzin |
| **Institution** | Yandex |
| **Key Innovation** | 离线-在线解耦架构：高容量离线 Transformer 异步编码全量跨端交互历史，轻量在线模型融合缓存表征 + 最近事件；离线编码器双目标预训练（feedback prediction + next-item prediction） |
| **Core Result** | 恢复 72–80% 全量历史 Transformer 质量；搜索广告 +2.77%, Yandex Ad Network +2.1%，无额外延迟 |
| **arXiv** | [https://arxiv.org/abs/2607.14331](https://arxiv.org/abs/2607.14331) |

---

### 9. LLaTTE: Scaling Laws for Multi-Stage Sequence Modeling in Large-Scale Ads Recommendation

| 字段 | 内容 |
|------|------|
| **Authors** | Lee Xiong, Zhirong Chen, Rahul Mayuranath et al. |
| **Institution** | Meta AI |
| **Key Innovation** | 系统验证推荐系统遵循类似 LLM 的 power-law scaling；发现语义特征是 scaling 的前提（弯曲 scaling curve）；两阶段架构将重计算卸载到异步上游用户模型（>45× FLOPs 不对称） |
| **Core Result** | Facebook Feed & Reels 上线：4.3% 转化提升；上游改进以 ~50% transfer ratio 转移到下游排序 |
| **arXiv** | [https://arxiv.org/abs/2601.20083](https://arxiv.org/abs/2601.20083) |

---

### 10. CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer

| 字段 | 内容 |
|------|------|
| **Authors** | David Pardoe, Neil Daftary, Miro Furtado et al. |
| **Institution** | LinkedIn |
| **Key Innovation** | 端到端 decoder-only Transformer 用于广告 CTR；context-conditioned decoding（多塔预测头解决 post-scoring 位置信号的鸡生蛋问题）；self-gated attention 稳定训练；timestamp-based RoPE 捕获跨时间尺度关系 |
| **Core Result** | 线上 A/B：CTR +11.04%（vs LiRank DCNv2+TransAct 混合 ensemble）；已全量上线 LinkedIn 广告 |
| **arXiv** | [https://arxiv.org/abs/2602.11410](https://arxiv.org/abs/2602.11410) |

---

### 11. MARCO: Click-Intent Decomposition for Calibrated Ads Conversion Prediction

| 字段 | 内容 |
|------|------|
| **Authors** | Shiwen Shen, Xiru Huang et al.（Meta AI 大团队） |
| **Institution** | Meta |
| **Key Innovation** | 将点击按 UI 交互类型分解为意图子类，每个意图子类训练独立 CVR head，serving 时按预测意图分布组合；理论上证明分解不提升 population risk，增益来自有限容量估计效应 |
| **Core Result** | 部署 at binary intent granularity：per-intent calibration ~100%，conversions per click +2.80%，topline +0.98% |
| **arXiv** | [https://arxiv.org/abs/2608.10562](https://arxiv.org/abs/2608.10562) |

---

### 12. SWAG-Bid: Sliding-Window Aware Generative Auto-Bidding for Long-Term Advertising Effectiveness

| 字段 | 内容 |
|------|------|
| **Authors** | Alibaba International Digital Commerce |
| **Key Innovation** | 层次化框架：Masked Trajectory Model 做 episode-level 前瞻规划 + Multi-Window MPC Sampling 评分滑动窗口约束 + PSG-AdaLN 做 step-level 自适应门控；解决跨 episode 滑动窗口约束耦合 |
| **Core Result** | AliExpress 线上 A/B（21 天）：GMV +3.42%, ROAS +5.65%, 约束达成率 +2.02pp |
| **arXiv** | [https://arxiv.org/abs/2607.25233](https://arxiv.org/abs/2607.25233) |

---

### 13. GOAL: Generative Optimization for Incentivized Advertising with Global Level Constraints

| 字段 | 内容 |
|------|------|
| **Authors** | 多机构合作（KDD 2026） |
| **Key Innovation** | 将激励分配建模为条件序列生成；层次化因果状态编码器 + Constraint-Aware MoE + Safe Constrained Policy Optimization (SCPO)，λ-generalization 使单一策略适应多种 ROI 约束 |
| **Core Result** | 在大规模真实数据和合成疲劳感知环境中，提高长期收入和用户留存，大幅降低 ROI 违反率 |
| **arXiv** | [https://arxiv.org/abs/2608.04421](https://arxiv.org/abs/2608.04421) |

---

## 二、序列推荐 & 用户行为建模

### 14. HyTRec: A Hybrid Temporal-Aware Attention Architecture for Long Behavior Sequential Recommendation

| 字段 | 内容 |
|------|------|
| **Authors** | 未完整列出 |
| **Key Innovation** | 混合注意力架构：线性注意力分支处理海量历史 + softmax 注意力分支保留近期精确检索；Temporal-Aware Delta Network (TADN) 动态增强新鲜信号、抑制历史噪声 |
| **Core Result** | 万级交互序列下保持线性推理速度，Hit Rate 提升 8%+（ultra-long sequence 用户） |
| **arXiv** | [https://arxiv.org/abs/2602.18283](https://arxiv.org/abs/2602.18283) |

---

### 15. GrIT: Group Informed Transformer for Sequential Recommendation

| 字段 | 内容 |
|------|------|
| **Authors** | Adamya Shyam et al. |
| **Key Innovation** | 在 Transformer 块中联合建模个人序列动态和群体级动态；时变群体成员权重通过偏好漂移统计特征学习，与序列表征融合 |
| **Core Result** | 五个 benchmark 数据集上一致超越 SASRec、BERT4Rec 等 SOTA |
| **arXiv** | [https://arxiv.org/abs/2602.19728](https://arxiv.org/abs/2602.19728) |

---

### 16. Efficient Sequential Recommendation for Long Term User Interest Via Personalization (PerSRec)

| 字段 | 内容 |
|------|------|
| **Authors** | Meta Research |
| **Key Innovation** | 将长用户交互历史压缩为可学习 token（personalized experts），与近期交互组合推理；应用于 HSTU 和 HLLM，大幅降低推理计算成本 |
| **Core Result** | 在 MerRec 数据集上几乎保留全序列性能，推理计算成本显著降低 |
| **arXiv** | [https://arxiv.org/abs/2601.03479](https://arxiv.org/abs/2601.03479) |
| **Code** | [https://github.com/facebookresearch/PerSRec](https://github.com/facebookresearch/PerSRec) |

---

### 17. HORIZON: A Benchmark for In-the-wild User Behaviour Modeling

| 字段 | 内容 |
|------|------|
| **Authors** | Arnav Goel et al. (Microsoft Research India) |
| **Key Innovation** | 跨域长时域用户建模 benchmark：54M 用户、35M 物品，评估 temporal generalization / sequence-length variation / unseen users |
| **Core Result** | 发现 BERT4Rec 在 OOD 用户上大幅退化但长时域外推仍强；LLM 并非在所有用户建模任务上一致优于专用架构 |
| **arXiv** | [https://arxiv.org/abs/2604.17259](https://arxiv.org/abs/2604.17259) |

---

### 18. RoTE: Coarse-to-Fine Multi-Level Rotary Time Embedding for Sequential Recommendation

| 字段 | 内容 |
|------|------|
| **Authors** | SIGIR 2026 |
| **Key Innovation** | 轻量即插即用的时间建模模块：将 timestamp 分解为年/月/日多粒度，通过 rotary embedding 注入 item 表征，无需修改 backbone |
| **Core Result** | Toys & Games 上 RPG + Recall@5 提升 17.51%, NDCG@5 提升 20.11%；可应用于传统和生成式两类序列模型 |
| **arXiv** | [https://arxiv.org/abs/2604.13389](https://arxiv.org/abs/2604.13389) |
| **Code** | [https://github.com/XiaoLongtaoo/RoTE](https://github.com/XiaoLongtaoo/RoTE) |

---

### 19. PSD: Privileged Self-Distillation for Sequential Recommendation

| 字段 | 内容 |
|------|------|
| **Authors** | 未完整列出 |
| **Key Innovation** | 利用未来交互作为训练时特权信息：单 backbone 两个 attention mask（privileged teacher + causal student），advantage-reachability gate 过滤不可达 dark knowledge，momentum teacher 稳定训练 |
| **Core Result** | 多个公开 benchmark 上一致大幅超越 baseline，部署成本不变 |
| **arXiv** | [https://arxiv.org/abs/2607.27055](https://arxiv.org/abs/2607.27055) |

---

### 20. RecRec: Latent Interests Recursive Reasoning for Sequential Recommendation

| 字段 | 内容 |
|------|------|
| **Authors** | Wenhao Deng et al. |
| **Key Innovation** | 解耦推理状态与预测状态：Context Compressor 提取多维 latent interests + Recursive Reasoner 在独立推理状态空间迭代精炼；RL-free，两阶段监督训练 |
| **Core Result** | 四个数据集上超越推理增强 baseline，三个数据集上推理深度超出训练深度仍有增益 |
| **arXiv** | [https://arxiv.org/abs/2607.12945](https://arxiv.org/abs/2607.12945) |

---

## 三、游戏 AI & 强化学习

### 21. Superhuman AI for Generals.io Using Self-Play Reinforcement Learning

| 字段 | 内容 |
|------|------|
| **Authors** | Matěj Straka, Viliam Lisý, Martin Schmid |
| **Key Innovation** | JAX 原生模拟器：单 GPU 达到 50.7M frames/sec（10,000× 加速）；纯 policy-gradient + 稀疏 win/loss reward 达到超人类水平，无需行为克隆、奖励塑形或 population-based self-play |
| **Core Result** | 公共 1v1 leaderboard #1（5000+ 玩家），vs top-2 人类玩家合计 199-70（269 场 ladder） |
| **arXiv** | [https://arxiv.org/abs/2606.23348](https://arxiv.org/abs/2606.23348) |

---

### 22. CAST: Game Solvers as Turn-Level Teachers for LLM Agents

| 字段 | 内容 |
|------|------|
| **Authors** | 多机构合作 |
| **Key Innovation** | 将游戏 solver 的状态价值变化转化为 turn-level solver advantage 注入 RLVR；在 soft-optimal solver 假设下等价于 logit-free on-policy distillation |
| **Core Result** | Sokoban / Minesweeper / Rush Hour 上所有 trained 方法最优；DAPO 峰值性能在 1.7–2.0× 更少步数达到；零样本迁移到 ALFWorld 和 WebShop |
| **arXiv** | [https://arxiv.org/abs/2607.25308](https://arxiv.org/abs/2607.25308) |
| **Code** | [https://github.com/Wloner0809/CAST](https://github.com/Wloner0809/CAST) |

---

### 23. Odysseus: Scaling VLMs to 100+ Turn Decision-Making in Games via Reinforcement Learning

| 字段 | 内容 |
|------|------|
| **Authors** | 多机构合作 |
| **Key Innovation** | 适配 PPO + 轻量级 turn-level critic（而非 token-level），positive-advantage filtering；预训练 VLM 提供强 action prior |
| **Core Result** | Super Mario Land 多关卡训练：平均 game progress 3×+ 超越 frontier models（GLM-4.6V），泛化到域内/域外关卡 |
| **arXiv** | [https://arxiv.org/abs/2605.00347](https://arxiv.org/abs/2605.00347) |

---

### 24. MemoPilot: Enhancing Test-Time Learning of LLM Agents via Reinforcement Learning over Memory

| 字段 | 内容 |
|------|------|
| **Authors** | 多机构合作 |
| **Key Innovation** | 将记忆更新建模为多轮决策过程，multi-turn GRPO 端到端优化；turn-wise reward + turn-level advantage estimation |
| **Core Result** | LHE 和 RPS 上 Elo #1（1762 / 1590），超越 DeepSeek-V3.2 等，可迁移至 Qwen3-235B |
| **arXiv** | [https://arxiv.org/abs/2606.08656](https://arxiv.org/abs/2606.08656) |

---

### 25. REAPER: Reflective Experiential Agent with Periodic Extraction of Rules

| 字段 | 内容 |
|------|------|
| **Authors** | Jakub Rada (AI Center, Dept. of CS) |
| **Key Innovation** | 将 case-based reasoning 适配到序列博弈：per-move reflection 进行细粒度 credit assignment + 周期性规则提取泛化为自然语言策略规则；无需权重更新 |
| **Core Result** | Tic-tac-toe 上 GPT-5 nano vs Optimal：draw rate 0.868（+5pp over baseline） |
| **arXiv** | [https://arxiv.org/abs/2608.03420](https://arxiv.org/abs/2608.03420) |

---

### 26. IFlowNets: Extending Generative Samplers to Learn Strategies in Incomplete Information Games

| 字段 | 内容 |
|------|------|
| **Authors** | 多机构合作 |
| **Key Innovation** | 将 Adversarial Flow Networks 推广到不完全信息博弈（IFlowNets）；证明先前 AFlowNets 约束在不完全信息下不可行，提出修正 |
| **Core Result** | Kuhn Poker 上与 OS-MCCFR 可比；Leduc Poker 上超越所有对比方法（OS-MCCFR / Deep CFR / NFSP）且更快 |
| **arXiv** | [https://arxiv.org/abs/2608.05422](https://arxiv.org/abs/2608.05422) |

---

### 27. AV-AIVAT: 74× Cheaper Agent Evaluation in Imperfect-Information Games

| 字段 | 内容 |
|------|------|
| **Authors** | Boning Li |
| **Key Innovation** | AIVAT 方差缩减 + 连续监控 Confidence Sequence 实现 anytime-valid early stopping；将 AIVAT 与 CS 结合，无需固定预算 |
| **Core Result** | HUNL 71,439 手上：AIVAT 比 raw outcome 节省中位 54× 样本，AV-AIVAT 节省 74× |
| **arXiv** | [https://arxiv.org/abs/2608.06362](https://arxiv.org/abs/2608.06362) |

---

### 28. Augmenting Game AI with Deep Reinforcement Learning

| 字段 | 内容 |
|------|------|
| **Authors** | Alessandro Sestini, Joakim Bergdahl et al. |
| **Key Innovation** | 将深度 RL 增强到商业游戏 AI 中（综述/方法论） |
| **arXiv** | [https://arxiv.org/abs/2606.20210](https://arxiv.org/abs/2606.20210) |

---

## 四、LLM 推理 & 多模态

### 29. UniT: Unified Multimodal Chain-of-Thought Test-time Scaling

| 字段 | 内容 |
|------|------|
| **Authors** | 多机构合作 |
| **Key Innovation** | 多模态 CoT test-time scaling 框架：单模型实现多轮 reasoning-verify-refine；短推理轨迹训练可泛化到更长推理链 |
| **Core Result** | 序列 CoT 比并行采样更可扩展和计算高效；生成+编辑轨迹训练提升 OOD 视觉推理 |
| **arXiv** | [https://arxiv.org/abs/2602.12279](https://arxiv.org/abs/2602.12279) |

---

### 30. ParVL: Parallel Scaling and Expandable Compute Allocation for Multimodal LLMs

| 字段 | 内容 |
|------|------|
| **Authors** | Yang Yang et al. (ANU, Shanghai AI Lab, ZJU, SJTU, NJU) |
| **Key Innovation** | 并行视觉-语言扩展：通过参数共享的 prefix-conditioned 分支在 ViT 和 LLM 间灵活分配计算，仅增加 ~4% 参数 |
| **Core Result** | 1B scale 9-benchmark 平均从 49.6 → 50.5；最佳分配因任务而异（数学推理偏好语言侧扩展，OCR 偏好视觉侧扩展） |
| **arXiv** | [https://arxiv.org/abs/2608.04010](https://arxiv.org/abs/2608.04010) |
| **Code** | [https://github.com/YangYangGirl/ParVL](https://github.com/YangYangGirl/ParVL) |

---

### 31. VisRef: Visual Refocusing while Thinking Improves Test-Time Scaling

| 字段 | 内容 |
|------|------|
| **Authors** | 多机构合作 |
| **Key Innovation** | 在推理过程中主动重新注入语义相关且多样化的视觉 token coreset，无需 RL 微调 |
| **Core Result** | 固定 TTS budget 下超越现有方法达 6.4% |
| **arXiv** | [https://arxiv.org/abs/2603.00207](https://arxiv.org/abs/2603.00207) |

---

### 32. MMDynOpt-Agent: Dynamic Optimization for Multimodal LLM Reasoning via RL

| 字段 | 内容 |
|------|------|
| **Authors** | Qwen 团队 |
| **Key Innovation** | 将多模态推理动态优化建模为 MDP；轻量 agent 作为决策策略，与目标 MLLM 交互，自适应生成多轮优化 prompt；Prism Reward 联合约束格式/正确性/预算 |
| **Core Result** | 15 个数据集上超越 baseline；OOD 泛化和跨模型迁移性强 |
| **arXiv** | [https://arxiv.org/abs/2608.14026](https://arxiv.org/abs/2608.14026) |

---

### 33. Visual Enhanced Depth Scaling for Multimodal Latent Reasoning

| 字段 | 内容 |
|------|------|
| **Key Innovation** | 视觉回放模块（saliency-aware causal self-attention）+ 路由深度扩展（per-layer token router 动态分配推理步数）+ 课程学习 |
| **Core Result** | 多 benchmark SOTA，推理延迟低于显式 CoT baseline |
| **arXiv** | [https://arxiv.org/abs/2604.10500](https://arxiv.org/abs/2604.10500) |

---

### 34. Look Light, Think Heavy: What Multimodal Chain-of-Thought Reasoning Can and Cannot Do

| 字段 | 内容 |
|------|------|
| **Key Innovation** | 系统分析 12 类多模态任务 × 22 个模型；揭示 "Look Light, Think Heavy" 现象：推理过程中 verbal reflection 先升后降，但 visual reflection 持续衰减 |
| **Core Result** | CoT 应选择性使用：感知任务可能退化，推理任务（数学/科学/多图推理）有效；开源推理模型因偏重数学训练提升有限 |
| **arXiv** | [https://arxiv.org/abs/2606.22565](https://arxiv.org/abs/2606.22565) |

---

### 35. Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility

| 字段 | 内容 |
|------|------|
| **Key Innovation** | 统一形式化 TTS 为前缀树上的预算化推理；区分三种结构化 regime（single-trajectory / leaf-level / prefix-level）；发布 2B+ 推理 trace |
| **arXiv** | [https://arxiv.org/abs/2608.04001](https://arxiv.org/abs/2608.04001) |

---

### 36. Switch-Reasoner: Learn When to Think in Multitask Mixtures via RL

| 字段 | 内容 |
|------|------|
| **Authors** | 多机构合作 |
| **Key Innovation** | GRPO 框架自适应选择 Thinking Mode vs Direct Mode；双层调控机制（全局模式平衡 + 样本级相对收益监督）防止模式坍塌 |
| **Core Result** | 11 个多模态任务上减少不必要推理，维持强性能，更好的 accuracy-efficiency trade-off |
| **arXiv** | [https://arxiv.org/abs/2607.08572](https://arxiv.org/abs/2607.08572) |
| **Code** | [https://github.com/fuyyyyy/Switch-Reasoner](https://github.com/fuyyyyy/Switch-Reasoner) |

---

## 五、关键趋势总结

| 趋势 | 代表工作 |
|------|---------|
| **Scaling Law 进入推荐系统** | LLaTTE (Meta), GRAB (Baidu), SparseCTR, DeRes |
| **Decoder-only Transformer 统一推荐排序** | CADET (LinkedIn), GRAB (Baidu) |
| **离线-在线两阶段架构成为工业标准** | LLaTTE (Meta), Long-History User Transformers (Yandex) |
| **Sparse/Efficient Attention for Long Behavior** | SparseCTR, HyTRec, LoopCTR |
| **时间建模精细化** | RoTE, SparseCTR (RelTemporal), LENS (QueryPos) |
| **LLM 赋能游戏 AI** | CAST, MemoPilot, REAPER, Odysseus |
| **Test-time Scaling 扩展到多模态** | UniT, VisRef, Switch-Reasoner, ParVL |
| **广告激励优化生成化** | GOAL, SWAG-Bid |
| **意图分解 / 因果建模** | MARCO (Meta) |

---

*报告生成时间：2026-08-19 13:00 UTC+8*
