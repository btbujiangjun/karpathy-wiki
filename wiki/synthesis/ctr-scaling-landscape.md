---
title: "CTR Scaling Landscape — Awesome-CTR-Scaling 论文全景"
type: synthesis
created: 2026-05-25
updated: 2026-05-25
sources: [Awesome-CTR-Scaling]
tags: [ctr, scaling-laws, ranking, recommendation, survey]
---

# CTR Scaling Landscape — 工业推荐系统缩放律论文全景

> 基于 GitHub [Awesome-CTR-Scaling](https://github.com/byby221b/Awesome-CTR-Scaling) 仓库整理，覆盖 49 篇论文，按公司和技术路线分类。

---

## 1. 按公司分类

### Meta (8 篇)
| 论文 | Venue | 年份 | 核心贡献 | Wiki 状态 |
|------|-------|------|---------|----------|
| Understanding Scaling Laws for Recommendation Models | arXiv | 2022 | 首个 DLRM 缩放律系统研究 | ❌ 缺失 |
| DHEN: Deep Hierarchical Ensemble Network | arXiv | 2022 | 层次异构交互模块集成 | ❌ 缺失 |
| **Wukong**: Scaling Law for Large-Scale Recommendation | ICML | 2024 | 分解式堆叠交互层实现参数缩放 | ❌ 缺失 |
| **HSTU**: Trillion-Parameter Sequential Transducers | ICML | 2024 | 万亿参数序列生成推荐范式 | 📎 提及 |
| InterFormer: Heterogeneous Interaction Learning | arXiv | 2024 | 用户画像+上下文+行为异构交互 | ❌ 缺失 |
| Foundation-Expert Paradigm | arXiv | 2025 | 基础模型+场景专家+HyperCast 部署 | ❌ 缺失 |
| **Kunlun**: Unified Scaling Laws Architecture | arXiv | 2026 | 统一架构设计实现可预测缩放律 | ❌ 缺失 |
| **LLaTTE**: Multi-Stage Scaling Laws for Ads Rec | arXiv | 2026 | 广告推荐两阶段异步架构缩放 | ❌ 缺失 |
| **ULTRA-HSTU**: Bending Scaling Law Curve | arXiv | 2026 | 稀疏注意力+FlashAttention-V3 突破 HSTU | ❌ 缺失 |

### ByteDance (9 篇)
| 论文 | Venue | 年份 | 核心贡献 | Wiki 状态 |
|------|-------|------|---------|----------|
| **RankMixer**: Scaling Up Ranking Models | CIKM | 2025 | TokenMixer 架构缩放 | 📎 提及 |
| **OneTrans**: Unified Feature Interaction + Sequence | arXiv | 2025 | 统一分词器+因果注意力+KV 缓存 | 📎 提及 |
| **HyFormer**: Sequence vs Feature Interaction | arXiv | 2026 | Sequence Modeling与Feature Interaction角色重审 | ❌ 缺失 |
| **Zenith**: Billion-Scale Livestreaming Ranking | arXiv | 2026 | 直播场景排名模型缩放 | ❌ 缺失 |
| **TokenMixer-Large**: Hardware Utilization Scaling | arXiv | 2026 | 硬件利用率优化的大规模 TokenMixer | 📎 提及 |
| **UG-Sep**: Compute Only Once for Large Rec | arXiv | 2026 | 用户通用特征分离减少冗余计算 | ❌ 缺失 |
| **MixFormer**: Co-Scaling Dense and Sequence | arXiv | 2026 | 用户-物品解耦架构联合缩放 | ❌ 缺失 |
| LONGER: Ultra-Long User Behavior Sequences | RecSys | 2025 | 超长用户行为序列缩放 | 📎 提及 |
| Make It Long, Keep It Fast: 10K-Sequence at Scale | arXiv | 2025 | end-to-end万级Sequence Modeling（抖音） | ❌ 缺失 |

### Alibaba (8 篇)
| 论文 | Venue | 年份 | 核心贡献 | Wiki 状态 |
|------|-------|------|---------|----------|
| **FAT**: Rethinking Transformers for CTR (Rademacher) | arXiv | 2025 | 首个基于 Rademacher 复杂度的 CTR 缩放律 | ❌ 缺失 |
| **HHFT**: Hierarchical Heterogeneous Feature Transformer | arXiv | 2025 | 分层异构特征 Transformer | ❌ 缺失 |
| **GPSD**: Generative Pretraining for Discriminative CTR | KDD | 2025 | 生成式预训练→判别式 CTR/CVR 下游 | ❌ 缺失 |
| **EST**: Efficient Scaling Laws for CTR | arXiv | 2026 | 高效统一建模实现 CTR 缩放 | 📎 提及 |
| **HeteroMixer**: Query-Mixed Interest Extraction | arXiv | 2026 | 查询混合兴趣提取+异构交互 | 📎 提及 |
| **SORT**: Systematically Optimized Ranking Transformer | arXiv | 2026 | 工业排名 Transformer 系统优化 | ❌ 缺失 |
| ENCODE: Clustering Long-Term User Interest | TKDE | 2025 | 高效聚类长程兴趣建模 | ❌ 缺失 |
| MUSE: 100K-Length Lifelong User Interest | arXiv | 2025 | 多模态搜索 10 万级行为建模 | ❌ 缺失 |

### Meituan (4 篇)
| 论文 | Venue | 年份 | 核心贡献 | Wiki 状态 |
|------|-------|------|---------|----------|
| **SUAN**: Scaling Laws for Online CTR | RecSys | 2025 | 线上 CTR 缩放方法学 | ❌ 缺失 |
| **MTmixAtt**: MoE + Multi-Mix Attention (1B params) | arXiv | 2025 | MoE+多混合注意力 10 亿参数 | ❌ 缺失 |
| **MTFM**: Alignment-Free Foundation Model | arXiv | 2026 | Full/Target Attn 交替+CPU-GPU 流水线 | ❌ 缺失 |
| **SparseCTR**: Sparse Attention Long-Term CTR | WWW | 2026 | 三分支稀疏注意力+缩放律 | 📎 提及 |

### Tencent (3 篇)
| 论文 | Venue | 年份 | 核心贡献 | Wiki 状态 |
|------|-------|------|---------|----------|
| **GE4Rec**: Generative CTR Prediction Paradigm | arXiv | 2025 | 判别式→生成式 CTR 范式转换 | ❌ 缺失 |
| **TokenFormer**: Unify Multi-Field and Sequential Rec | arXiv | 2026 | Bottom-Full-Top-Sliding 注意力解决序列坍缩 | ❌ 缺失 |
| **RankUp**: High-Rank Representations (Weixin) | KDD | 2026 | representation collapse缓解+微信全量部署 | ✅ 已创建 |

### Kuaishou (4 篇)
| 论文 | Venue | 年份 | 核心贡献 | Wiki 状态 |
|------|-------|------|---------|----------|
| **INFNet**: Linear-Complexity Feature Interaction | arXiv | 2025 | 线性复杂度任务感知Feature Interaction | ❌ 缺失 |
| **UniMixer**: Unified Architecture for Scaling Laws | arXiv | 2026 | 注意力/TokenMixer/FM 统一缩放框架 | ❌ 缺失 |
| CHIME: Holistic Interest Modeling + LLM + VQ | arXiv | 2025 | LLM 编码+残差 VQ 压缩 | ❌ 缺失 |
| VQL: Vector Quantization Attention for Long Behavior | arXiv | 2025 | 向量量化注意力超长行为建模 | ❌ 缺失 |

### LinkedIn (2 篇)
| 论文 | Venue | 年份 | 核心贡献 | Wiki 状态 |
|------|-------|------|---------|----------|
| **LiRank**: Large Scale Ranking at LinkedIn | arXiv | 2024 | Residual DCN+Transformer+Dense Gating | ❌ 缺失 |
| **CADET**: Decoder-Only Ads CTR | arXiv | 2026 | Decoder-only Transformer+门控注意力 | 📎 提及 |

### 其他 (6 篇)
| 论文 | 机构 | Venue | 年份 | 核心贡献 | Wiki 状态 |
|------|------|-------|------|---------|----------|
| **Hiformer**: Heterogeneous Feature Interactions | Google | arXiv | 2023 | Transformer 异构Feature Interaction | ❌ 缺失 |
| **Climber**: Efficient Scaling Laws | NetEase | WWW | 2025 | 多尺度序列+动态温度调制，首次公开连续线上缩放 | ❌ 缺失 |
| **OnePiece**: Context Engineering + Reasoning | Shopee | arXiv | 2025 | LLM 风格上下文工程+分块潜推理 | ❌ 缺失 |
| Beyond Dense Connectivity: Explicit Sparsity | - | SIGIR | 2026 | 显式稀疏机制替代稠密连接 | ❌ 缺失 |
| LIME: Linear Attention for Efficient Scaling | - | arXiv | 2025 | O(N) 线性注意力高效缩放 | ❌ 缺失 |
| MALLOC: Memory-Efficient Long Sequence Compression | - | arXiv | 2026 | 长序列压缩基准 | ❌ 缺失 |

---

## 2. 按技术路线分类

### 缩放律理论 (4 篇)
| 论文 | 核心贡献 | 机构 |
|------|---------|------|
| Understanding Scaling Laws for Rec Models | DLRM 缩放律奠基 | Meta |
| **Wukong** | 分解堆叠交互层实现参数缩放 | Meta |
| **FAT** | 首个基于 Rademacher 复杂度的 CTR 缩放律 | Alibaba |
| **SUAN** | 线上 CTR 缩放实践方法学 | Meituan |

### Transformer 架构缩放 (12 篇)
| 论文 | 核心贡献 | 机构 |
|------|---------|------|
| Hiformer | 异构Feature Interaction Transformer | Google |
| **HSTU** | 万亿参数序列生成推荐 | Meta |
| **RankMixer** | TokenMixer 缩放架构 | ByteDance |
| **TokenMixer-Large** | 硬件优化大规模 TokenMixer | ByteDance |
| **HyFormer** | 序列 vs Feature Interaction角色重审 | ByteDance |
| **MixFormer** | 用户-物品解耦联合缩放 | ByteDance |
| **TokenFormer** | 统一多字段与序列推荐 | Tencent |
| **SORT** | 工业排名 Transformer 系统优化 | Alibaba |
| **InterFormer** | 异构交互学习 | Meta |
| **HHFT** | 分层异构特征 Transformer | Alibaba |
| **LiRank** | Residual DCN+Transformer+Dense Gating | LinkedIn |
| **CADET** | Decoder-only Ads CTR | LinkedIn |

### 生成式/统一架构 (8 篇)
| 论文 | 核心贡献 | 机构 |
|------|---------|------|
| **HSTU** | 生成式推荐范式 | Meta |
| **OneTrans** | 统一Feature Interaction+Sequence Modeling | ByteDance |
| **Zenith** | 直播排名模型缩放 | ByteDance |
| **EST** | 高效统一 CTR 缩放 | Alibaba |
| **GE4Rec** | 判别式→生成式 CTR 范式 | Tencent |
| **UniMixer** | 注意力/TokenMixer/FM 统一缩放 | Kuaishou |
| **GPSD** | 生成式预训练→判别式下游 | Alibaba |
| **Foundation-Expert** | 基础模型+场景专家 | Meta |

### 长Sequence Modeling (8 篇)
| 论文 | 核心贡献 | 机构 |
|------|---------|------|
| **SparseCTR** | 稀疏注意力+缩放律 | Meituan |
| **LLaTTE** | 两阶段异步缩放 | Meta |
| LONGER | 超长序列两阶段检索 | ByteDance |
| ENCODE | 聚类长程兴趣建模 | Alibaba |
| MUSE | 10 万级多模态兴趣建模 | Alibaba |
| Make It Long, Keep It Fast | end-to-end万级序列（抖音） | ByteDance |
| VQL | 向量量化注意力超长行为 | Kuaishou |
| CHIME | LLM 编码+残差 VQ 压缩 | Kuaishou |

### 效率优化 (8 篇)
| 论文 | 核心贡献 | 机构 |
|------|---------|------|
| **UG-Sep** | 用户特征分离减少冗余 | ByteDance |
| **HeteroMixer** | 查询混合兴趣提取 | Alibaba |
| **MTmixAtt** | MoE+多混合注意力 1B | Meituan |
| **MTFM** | 全量/目标注意力交替+CPU-GPU | Meituan |
| **INFNet** | 线性复杂度Feature Interaction | Kuaishou |
| LIME | O(N) 线性注意力 | - |
| **RankUp** | representation collapse缓解 | Tencent |
| MALLOC | 长序列压缩基准 | - |

### 基础设施 (5 篇)
| 论文 | 核心贡献 | 机构 |
|------|---------|------|
| **Kunlun** | 统一架构可预测缩放 | Meta |
| **ULTRA-HSTU** | FlashAttention-V3 突破 HSTU | Meta |
| DHEN | 层次集成训练系统 | Meta |
| SOLARIS | 投机卸载大模型服务 | Meta |
| Versioned Late Materialization | 超长序列训练数据基建 | Meta |

---

## 3. 时间线

| 年份 | 关键里程碑 |
|------|-----------|
| **2022** | Meta 发布首个推荐缩放律；DHEN 层次集成 |
| **2023** | Google Hiformer：异构Feature Interaction Transformer |
| **2024** | Meta Wukong（ICML）+ HSTU（ICML, 万亿参数）；LinkedIn LiRank |
| **2025** | 爆发年：ByteDance RankMixer（CIKM）+ OneTrans；Alibaba GPSD（KDD）+ FAT/HHFT；Meituan SUAN（RecSys）；NetEase Climber（WWW）；Tencent GE4Rec；Kuaishou INFNet |
| **2025-2026** | 长序列成为主战场：SparseCTR（WWW 2026），LLaTTE，MUSE，Kunlun，ULTRA-HSTU；generative paradigm兴起：GE4Rec，GPSD，Foundation-Expert |

---

## 4. 与现有 Wiki 的交叉引用

已创建页面：
- [[rankup-advertising]] — RankUp (Tencent Weixin, KDD 2026)

会议报告提及：
- SparseCTR (WWW 2026) — `conference-digest-2026-05-25.md`
- CADET (LinkedIn) — `technical-roadmap.md`, `affiliation-landscape.md`
- EST (Alibaba) — `technical-roadmap.md`, `arxiv-broad-2026-05-25.md`
- HeteroMixer/HeMix (Alibaba) — `technical-roadmap.md`, `arxiv-broad-2026-05-25.md`
- OneTrans (ByteDance) — `conference-digest-2026-05-25.md`, `technical-roadmap.md`
- RankMixer (ByteDance CIKM) — `rankelastor-recommendation.md`, `arxiv-daily-2026-05-25.md`
- HSTU (Meta ICML 2024) — `arxiv-daily-2026-05-24.md`

待创建（高优先级）：
- Wukong (Meta, ICML 2024) — 推荐缩放律奠基
- Kunlun (Meta, 2026) — 统一架构缩放律
- SparseCTR (Meituan, WWW 2026) — 稀疏注意力缩放
- EST (Alibaba) — 高效 CTR 缩放
- OneTrans (ByteDance) — 统一Feature Interaction+序列
- FAT (Alibaba) — Rademacher CTR 缩放律
- LiRank (LinkedIn) — 大规模工业排名

---

## 5. 关键趋势总结

1. **从实证缩放到理论缩放**：2022 年 DLRM 经验缩放 → 2025 FAT Rademacher 复杂度理论 → 2026 Kunlun 统一架构
2. **中国公司主导**：ByteDance/Alibaba/Meituan/Tencent/Kuaishou 贡献了 ~60% 的论文
3. **长序列成为核心扩展维度**：从 ~200 到 10K+ 的用户行为序列长度
4. **generative paradigm崛起**：HSTU → GE4Rec → GPSD → Foundation-Expert，排序从判别式转向生成式
5. **硬件-算法协同优化**：FlashAttention, Triton kernel, CPU-GPU 流水线成为缩放关键支撑
