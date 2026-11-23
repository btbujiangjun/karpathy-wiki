---
title: Daily ArXiv Digest 2026-11-23
type: synthesis
created: 2026-11-23
updated: 2026-11-23
sources: [2611.27206v1, 2611.27203v1, 2611.27201v1, 2611.26921v1, 2611.26919v1, 2611.26531v1, 2611.26984v1, 2611.26060v1, 2611.24464v1, 2611.24283v1, 2611.24006v1, 2611.20448v2, 2611.26800v1, 2611.26463v1, 2611.26413v1, 2611.26807v1, 2611.26910v1, 2611.27180v1]
tags: [arxiv, daily, ai, llm, recommendation, advertising, ctr, sequential-modeling, games]
---

# Daily ArXiv Digest 2026-11-23

> 抓取工具: arXiv API（`export.arxiv.org/api/query`, `sortBy=submittedDate`, `sortOrder=descending`；各组按提交日期取最新, cutoff ≥ 2026-09-24）。机构/公司信息为 arXiv PDF 首页 best effort（多处没有标注）。

## A. AI/LLMs

### A1. LingSante-Pulse: Unified Physiological Pretraining through Random-Feature Prediction and Cross-Modal Alignment

- **arXiv:** https://arxiv.org/abs/2611.27206v1
- **发布:** 2026-11-20
- **作者:** Linxiao Yang, Wenwei Wang, Tian Zhou, Bingqing Peng, Zihao Zhang, Zuyi Zhu, Jinjie Gu, Liang Sun
- **机构:** 未注明
- **摘要:** Clinical monitoring and wearable devices capture complementary physiological signals, but their partially overlapping modality coverage makes within-signal information and cross-modal relationships difficult to exploit jointly. We introduce LingSante-Pulse, a unified, general-purpose and flexible physiological representation framework that learns from these heterogeneous recordings. A shared, signal-conditioned encoder processes each physical channel independently and supports different numbers and combinations of signals for multimodal assessment and single-sensor inference. Pairwise cross-modal alignment, structured random-feature prediction (RFP) and masked waveform reconstruction jointly learn physiological relationships and preserve informative within-signal structure. Across 38 general physiological task configurations spanning PPG, ECG, EEG and EMG, the frozen encoder achieves the best dataset-balanced mean rank in each domain. In sleep assessment, multimodal staging on the HMC dataset and EEG-only staging on the Sleep-EDF dataset reach Macro-F1 scores of 0.7784 and 0.7941, respectively, while single-lead ECG apnea screening achieves an AUROC of 0.9183. Controlled experiments show that function prediction and waveform reconstruction provide complementary supervision for retaining temporal and rhythmic information. Representations learned under continually refreshed random supervision generalize to unseen teacher realizations, and correct auxiliary modality correspondence improves respiration-only representations. These results demonstrate that a single encoder can learn reusable physiological features across signal types, prediction targets and sensor configurations from partially overlapping recordings.
- **关键创新:**
  - 统一的生理表示框架: 共享的 signal-conditioned encoder 对每个物理通道独立处理, 支持不同数量与组合的传感器 (PPG/ECG/EEG/EMG), 支持多模态评估与单传感器推断。
  - 联合学习: pairwise 跨模态对齐 + 结构化 random-feature prediction (RFP) + 掩码 waveform 重建。
  - 效果: 38 个生理任务配置中每个领域的 frozen encoder 都取得 dataset-balanced mean rank 的最佳; 睡眠分期 HMC 上 multimodal Macro-F1 0.7784、Sleep-EDF 上 EEG-only 0.7941, 单导 ECG 呼吸暂停筛查 AUROC 0.9183。

### A2. Improved Accuracy Scaling with Problem Complexity in LLM Arithmetic Reasoning Using Executable Symbolic Representations

- **arXiv:** https://arxiv.org/abs/2611.27203v1
- **发布:** 2026-11-20
- **作者:** Yu-Bin Liu, Shi-Ju Ran
- **机构:** Center for Quantum Physics and Intelligent Sciences, Department of Physics, Capital Normal University, Beijing, China
- **摘要:** High accuracy on mathematical benchmarks does not establish whether reasoning remains reliable as problem complexity increases. We examine how executable symbolic representations change accuracy scaling in large language models compared with natural-language reasoning. To address this limitation, we introduce the GSM Arithmetic Benchmark (GSM-AB), a controlled benchmark that independently varies operand digit length and operation count to probe numerical scale and compositional complexity. We find that executable representations can improve accuracy and slow its decline as complexity increases. Lean reduces average sensitivity to operand digit length at every tested model size. By contrast, slower degradation with increasing operation count emerges at the larger model sizes. A Python program-of-thought (Python-PoT) control shows a similar operation-axis pattern, suggesting that this finding is not specific to Lean. These findings show that reasoning representation shapes arithmetic accuracy scaling and support executable symbolic representations for more reliable reasoning on complex arithmetic tasks.
- **关键创新:**
  - 新基准 GSM-AB: 独立变量 operand digit length 与 operation count, 探测数值规模与组合复杂度的精度漂移 (数学基准高分只代表结果, 不代表复杂度下的可靠性)。
  - 可执行符号表示 (Lean 与 Python PoT control) 在所有模型规模下降低对 operand digit length 的敏感性; 更大模型上出现 operation count 轴更慢的退化。
  - 结论: 推理表示形式决定算术精度的 scaling 行为, 支持 Executable Symbolic Representations 用于复杂算术推理。

### A3. Backbone-Specific LoRA Geometry: Orthogonality, Superposition, and Provenance

- **arXiv:** https://arxiv.org/abs/2611.27201v1
- **发布:** 2026-11-20
- **作者:** Kazuhiko Kawamoto1, Keigo Watanabe1, Hiroshi Kera1,2 (1Chiba University, 2National Institute of Informatics)
- **机构:** Chiba University; National Institute of Informatics
- **摘要:** Sharing one low-rank adaptation (LoRA) update across pretrained models simplifies deployment. Composition methods typically combine updates from a common backbone, while cross-model transfer transforms updates for a target backbone. The conditions for sharing updates across backbones while preserving accuracy and distinguishing individual contributions remain unclear. Our idea is to use backbone-specific update directions as signatures of their training backbones. We derive a cross-backbone correlation bound from attention symmetries and equivariant LoRA learning under independent, uniform pretrained feature orientations. A local gradient-flow model explains positive mean correlation between independent runs on the same backbone and task. These patterns motivate cosine-based backbone identification and inner-product tests for registered-adapter reuse without coordinate alignment. Experiments on CLIP backbones show that shared sums achieve nearly the same mean accuracy as separate adapters. Cosine scores reliably identify source backbones across the evaluated tasks. Registered adapters remain detectable in sums of adapters from different backbones.
- **关键创新:**
  - 用 backbone-specific update directions 作为 LoRA 训练结果的 signature; 推导跨 backbone 相关界 (从 attention symmetries + equivariant LoRA learning 推导, 独立均匀的 pretrained feature orientations 下)。
  - cosine-based backbone identification + inner-product tests for registered-adapter reuse without coordinate alignment; CLIP 实验: shared sums 与 separate adapters 平均精度几乎相当。
  - provenance 可追溯: cosine scores 在评估任务中可靠识别 source backbone; sums of adapters from different backbones 中仍可检测 registered adapters。

## B. Recommendation

### B1. Leader Finding: A New Variation of Expert Finding in Community Question Answering

- **arXiv:** https://arxiv.org/abs/2611.26921v1
- **发布:** 2026-11-20
- **作者:** Sepideh Entezari Maleki, Mahmood Neshati
- **机构:** Faculty of Computer Science and Engineering, Shahid Beheshti University, Tehran, Iran
- **摘要:** Expert finding ranks people by their knowledge of a given topic. Many job positions need more than topical expertise, and a team leader is a clear case. A suitable leader knows the technical areas of the project without being overqualified, has strong managerial knowledge, and communicates well with the team. We study the leader finding problem, where the query is a project and a team and the output is a ranked list of candidate leaders. We model the problem in a probabilistic framework that combines technical fit, managerial knowledge, and communication with the team, and we propose one evaluation metric for each of these qualities. On two large collections built from Stack Overflow, the best configuration of our model more than doubles the NDCG@10 of the strongest baseline. These results show that a ranking of leaders must balance several qualities that topical expertise alone does not capture.
- **关键创新:**
  - 提出 Leader Finding: query = project + team, output = ranked candidate leaders, 取代单纯的 Expert Finding。
  - 用 probabilistic framework 结合 technical fit、managerial knowledge、communication, 每种质量分别定义 evaluation metric (如 NDCG@10)。
  - 效果: Stack Overflow 构建的两个大型集合上, 最佳配置 NDCG@10 超过最强 baseline 近 2 倍。

### B2. ERA: Embed, Route, Adapt for Cold-Start Cross-Model Latent Retrieval

- **arXiv:** https://arxiv.org/abs/2611.26919v1
- **发布:** 2026-11-20
- **作者:** Venkata Chivukula1, Zifeng Wang1 and Jinsung Yoon1
- **机构:** 未注明
- **摘要:** Production retrieval systems are tied to the embedding model that indexed their corpus. Moving queries to a different encoder normally requires re-embedding the whole corpus, and at cold start there are no query logs while every document embedded by the new encoder incurs an API or compute cost. We present ERA (Embed, Route, Adapt), a system for cold-start cross-model latent retrieval. ERA spends a small anchor budget on maximally informative documents, selected from the existing target index via Cosine Farthest Point Sampling, trains a lightweight adapter with a Manifold Alignment Loss that couples directional alignment with orthogonal regularization to prevent representation collapse, and pairs the adapter with a deterministic router that escalates the rare, hard queries that define perceived retrieval quality. Across five BEIR datasets, ERA matches or outperforms point-wise L2 and embedding-conversion baselines, with relative gains of up to 35% nDCG@10 on Arguana, and on clustered corpora its anchor selection also improves prior methods under a fixed anchor budget. With 1.2 ms of adapter and router overhead on top of a ~20 ms local encoder, ERA at a 20% nominal escalation budget reduces end-to-end query latency from roughly 160 ms to 38-86 ms while concentrating escalations on the queries where the projection fails most.
- **关键创新:**
  - Cold-start 跨 encoder retrieval: anchor budget 选出最具信息量的文档 (Cosine Farthest Point Sampling, 从现有 target index)。
  - 轻量 adapter: Manifold Alignment Loss 耦合 directional alignment + orthogonal regularization, 防止 representation collapse。
  - Deterministic router 将罕见的 hard queries 升级到最失败的情形; BEIR 数据集上 Arguana 等 nDCG@10 提升最高 35%; clustered corpora 上 anchor selection 改善基线。
  - 20% escalation 预算: 端到端延迟 160ms → 38–86ms (adapter+router 开销 1.2ms); 上升到最失败的情形; BEIR 数据集上 ERA 与 L2 基线匹配或超越。

### B3. Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models

- **arXiv:** https://arxiv.org/abs/2611.26531v1
- **发布:** 2026-11-20
- **作者:** Chang Yang, Yao Xuan, Wendan Yan, Nhat Le, Jiang Liu, Longhao Jin, Zhen Peggy Yao, Alireza Vahdatpour, Djordje Gligorijevic
- **机构:** Meta, Inc. (Sunnyvale, USA)
- **摘要:** Large Web platforms operate large fleets of ranking models, each selecting features from a shared pool of tens of thousands. We present an end-to-end agentic system that optimizes features across the fleet under resource constraints shared across models and those set per model, such as feature pipeline cost and serving throughput (QPS), respectively. In this system, LLM agents propose hypotheses, and deterministic tools execute experiments and verify them. For each model, an LLM generates and shortlists cross features from a combinatorial candidate space, and all features are then ranked by several importance methods. Feature blending mixes these rankings into a single selection, using Pareto fronts across tasks for multi-task models. An LLM Researcher agent then tunes the feature selection in 10--25 asynchronous trials under resource caps, and a trimming step keeps the pipeline cost within budget. Across production models, the system improves normalized entropy by 0.31% on average within each model's budget, and the trimming step cuts pipeline cost by 2.3% with no regression beyond measurement noise. The optimized models were launched, and in online A/B tests they improved a primary online metric by 0.20%.
- **关键创新:**
  - 端到端 agentic 系统: LLM agents 提出假设, deterministic tools 执行实验并验证 (计算成本/QPS 等资源约束)。
  - 工具链: LLM 从组合 candidate space 生成并筛选 cross features; Feature blending 用 Pareto fronts across tasks (multi-task models); "Researcher" agent 在 10–25 asynchronous trials 中细调 feature selection。
  - 结果: per-model 内 normalized entropy 平均 +0.31%; trimming 削减 pipeline cost 2.3% (无测量噪声以外的退化); online A/B test 主指标 +0.20%。

## C. Advertising

### C1. Comparing Visual Motion Patterns for Pedestrian Guidance with Multi-Display Signage: Two Field Studies

- **arXiv:** https://arxiv.org/abs/2611.26984v1
- **发布:** 2026-11-20
- **作者:** Yuri Mikawa1,2*, Taiki Fukiage 3, Yuki Kubota 3, Takumi Yokosaka3, Kazushi Maruya 3
- **机构:** The University of Tokyo; JST PRESTO (Tokyo, Japan); Communication Science Laboratories, NTT, Inc. (Kanagawa, Japan)
- **摘要:** Public multi-display signage (MDS) has the potential to provide subtle pedestrian guidance through visual motion while retaining its conventional role in advertising and information delivery. However, it remains unclear how different visual motion patterns relate to pedestrian spatial distributions and how these relationships vary across deployment settings. We conducted two exploratory field studies in a museum, involving 18,402 pedestrian passages over 25 experimental days, to examine lateral positions in relation to stripe-motion contrast and coverage patterns. In Test Case 1 (TC1), involving predominantly one-way pedestrian flow, partial stripe presentation was associated with more leftward lateral positions than wider-coverage patterns in some comparisons, and lower contrast in full-screen stripes was not associated with a detectable reduction in the observed lateral bias. In Test Case 2 (TC2), conducted in a different spatial configuration permitting bidirectional walking, lateral positions differed by stripe-motion direction during one-way flow, but coverage effects on lateral position and stripe-advertisement differences in lateral position or passing-side choice were not significant. In both test cases, partial stripes received lower self-reported sickness ratings than full-screen stripes. These findings suggest that lower-contrast and reduced-motion-coverage designs hold practical potential for pedestrian guidance, with spatially restricted cues potentially allowing such guidance to coexist with existing advertising while reducing discomfort. At the same time, the contrasting patterns in TC1 and TC2 suggest that spatial context may shape how pedestrians respond to stripe coverage, highlighting the context-dependent suitability of visual-motion-based guidance and the need for further investigation.
- **关键创新:**
  - 两场博物馆实地研究 (18,402 passages over 25 days): partial stripe presentation → 与 wider-coverage patterns 相比 lateral positions 更左偏 (one-way flow)。
  - Two-way flow 下 stripe-motion direction 决定 lateral positions; coverage 对 passing-side choice 无显著影响; lower contrast 未显著改变 bias。
  - Partial stripes 收到更低自评 sickness ratings; 但 TC1/TC2 中 coverage 适用性受 spatial context 影响 (context-dependent suitability)。

### C2. Iterative Scarcity-Guided Exploration: Bootstrapping Generative Auto-bidding from Narrow Support

- **arXiv:** https://arxiv.org/abs/2611.26060v1
- **发布:** 2026-11-19
- **作者:** Qingmao Yao1, Guangzheng Hu2, Yusen Huo4*, Zhilin Zhang4*, Chuan Yu2, Jian Xu2, Xu Chu1†, Bo Zheng2†, Xiaotie Deng1,3†
- **机构:** Center on Frontiers of Computing Studies, School of Computer Science, Peking University; Alimama Tech, Taobao & Tmall Group of Alibaba; Department of Computer Science, City University of Hong Kong; Independent Researcher
- **摘要:** Auto-bidding is a core algorithmic component in online advertising auctions. In practical cold-start settings, iterative training is commonly used to compensate for low-quality, narrowly supported historical data. Unfortunately, in iterative training, representative diffusion-based AI-Generated Bidding (AIGB) methods fail to sustain extrapolation beyond the narrow data support and stagnate at a suboptimal level. In this paper, we theoretically attribute this stagnation to Signal-to-Noise Ratio (SNR) collapse: the weak radial return signal is overwhelmed by a curvature-induced penalty. To break this stagnation, we propose **Iterative Scarcity-Guided Exploration (ISGE)**, which introduces a guidance handoff: as the return signal collapses, scarcity subsequently takes over as an exploratory signal to elevate the SNR above a critical threshold. Specifically, ISGE iteratively alternates between a *Judger* that assigns scarcity scores to trajectories and an *Explorer* that performs guided generation of high-scarcity and high-return trajectories, thereby bootstrapping from the narrow support with such self-generated trajectories. Extensive experiments on the industrial AuctionNet benchmark demonstrate that ISGE, starting from cold-start datasets, effectively surpasses the performance of the Full-Dataset baseline within three iterations. Code is available at https://github.com/alimama-tech/ISGE
- **关键创新:**
  - 理论归因: iterative training 停滞为 Signal-to-Noise Ratio (SNR) collapse — 弱的 return signal 被 curvature-induced penalty 淹没。
  - 提出 ISGE: guidance handoff — Judger 分配 scarcity scores 给 trajectories; Explorer 执行 guided generation of high-scarcity and high-return trajectories, bootstrap from narrow support。
  - 效果: AuctionNet 工业基准上, ISGE 从 cold-start 起 3 次迭代内超越 Full-Dataset baseline; 代码 github.com/alimama-tech/ISGE。

### C3. Platform Recommendation and Competition in Search Markets

- **arXiv:** https://arxiv.org/abs/2611.24464v1
- **发布:** 2026-11-18
- **作者:** Sanxi Li, Jun Yu, Mingsheng Zhang
- **机构:** School of Economics, Renmin University of China; School of Economics, Shanghai University of Finance and Economics
- **摘要:** Recommendation rules affect both sellers' incentives and the alternatives consumers expect to find. We develop a framework for evaluating these rules with heterogeneous sellers, endogenous pricing and advertising, and costly consumer search. For a broad class of separable recommendation scores, we establish conditions under which a unique market equilibrium exists. Three applications illustrate the use of the framework. A stronger reward for low prices does not necessarily lower equilibrium prices and benefit consumers when products are sufficiently differentiated in qualities. Quality guidance can lower the price of each product and benefit consumers while raising the average transaction price. With heterogeneous match distributions, a reward for the best initial inspection can help consumers with advertising fixed and harm them when advertising adjusts. A two-type design extension shows that no finite optimum over implementable outcomes uses positive weights on both quality and low prices, even when the platform values consumer surplus.
- **关键创新:**
  - 用 heterogeneous sellers, endogenous pricing and advertising, costly consumer search 的 framework 评估 separable recommendation score rules; 为可观测, 一个 broad class of separable scores 在 heterogeneous qualities 下有唯一 market equilibrium。
  - Reward for low prices: 在 sufficiently differentiated products 时, 不一定低价但提高消费者 surplus。
  - Quality guidance: 降低每个产品价格并提高消费者 surplus。
  - Heterogeneous match distributions: reward for best initial inspection — 有广告的无助于且广告调整时有害; 平均 transaction price 更高。

## D. CTR

### D1. X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction

- **arXiv:** https://arxiv.org/abs/2611.24283v1
- **发布:** 2026-11-18
- **作者:** Alexander Ploshkin*, Nikita Stepanov*, Alexey Pismenny*, Viacheslav Ovchinnikov, Nikolay Savushkin
- **机构:** 未注明 (PDF 首页无机构行)
- **摘要:** Accurate click-through rate (CTR) prediction depends on user representations that capture both persistent preferences and recent intent, yet processing extensive behavioral histories for every ranking request is costly under production compute and latency constraints. We present X-split ARGUS, a framework for ad ranking whose history compressor and online ranker are trained end to end. The compressor encodes past interactions into a compact set of tokens that are computed offline and reused across candidates, while the online ranker scores ads through cross-attention to these tokens and representations of recent events. Training combines an autoregressive loss for click feedback with distillation of candidate-specific click logits from a larger teacher that scores each candidate using the uncompressed history. The number of compressed history tokens and the length of recent history can be adjusted to fit serving compute and latency budgets. Offline evaluation shows a 0.81% relative reduction in normalized entropy (NE) compared with the production baseline. Deployment in a large-scale real-time bidding system increases online inference cost by 15% relative to the production baseline. An online A/B test against this baseline yields relative gains of 4.65% in a business metric reflecting the monetary value of conversions generated for advertisers and 2.96% in clicks.
- **关键创新:**
  - 结构: history compressor (offline, reused across candidates) + online ranker (cross-attention to compressed tokens + recent events), end-to-end 训练。
  - 训练: autoregressive click loss + teacher distillation of candidate-specific click logits (uncompressed history); 压缩 token 数与 recent history 长度可调以适配 compute/latency 预算。
  - 效果: offline NE 相对减少 0.81%; 部署在大规模 RTB 系统中 inference cost 涨 15% (vs production baseline); online A/B: business metric +4.65%, clicks +2.96%。

### D2. MARS Technical Report

- **arXiv:** https://arxiv.org/abs/2611.24006v1
- **发布:** 2026-11-18
- **作者:** MARS Team
- **机构:** 未注明 (PDF 首页仅列出 "MARS Team"; abstract 提到涉及 Taobao 场景)
- **摘要:** Modern industrial recommender systems use multi-stage cascades--retrieval, pre-ranking, ranking, and re-ranking--to narrow millions of candidates to a personalized list. While each stage deploys sophisticated models, pipeline-level decisions on channel activation, quotas, model selection, and score fusion remain engineer-tuned and user-agnostic within each scenario. This technical report presents MARS (Multi-stage Agentic Recommendation System), extending personalization from individual-stage predictions to full pipeline orchestration. A near-line agent built on fine-tuned Qwen3-0.6B generates per-user configurations--a seven-dimensional action covering pipeline mode, retrieval quotas, model selection, fusion weights, and reranker settings--from a constrained action space. Configurations are validated, cached, and consumed asynchronously; the cascade never waits for LLM inference. Schema checks, fallbacks, and a kill switch ensure serving safety. The policy is trained in three stages: Confidence-aware SFT distills schema-valid generation from a teacher model; Format-Anchored Preference Optimization (FAPO) learns action preferences via ActionMask with posterior weighting; Group Relative Policy Optimization (GRPO) refines the policy through Sandbox replay with a frozen reward model, without exposing exploratory actions to live traffic. Two-week A/B tests across five Taobao scenarios with over ten million daily users show positive gains on all key metrics. The largest reach +5.22% V2P and +7.34% GMV, with positive CTR lifts on both click surfaces. About 20% of requests use a lightweight Minimal mode, and deployment shows 12 ms lower mean serving latency versus production.
- **关键创新:**
  - 多模态结构: per-user 7-维 action (pipeline mode, retrieval quotas, model selection, fusion weights, reranker settings) 由 near-line agent (fine-tuned Qwen3-0.6B) 生成, 从受约束 action space 中选择; 配置异步生效, 级联不等待 LLM inference (serving safety: schema checks, fallbacks, kill switch)。
  - 三阶段训练: Confidence-aware SFT; Format-Anchored Preference Optimization (FAPO) via ActionMask posterior weighting; GRPO through Sandbox replay with frozen reward model。
  - 效果: 两周 A/B across five Taobao scenarios (10M+ daily users) — V2P +5.22%, GMV +7.34%, 两个 click surfaces 的 CTR 正向; ~20% 请求用 Minimal 模式, mean serving latency 降 12ms。

### D3. MMIntentFlow: An Intent-Driven Real-Time Multimodal Search System with Image–Text Queries at Xiaohongshu

- **arXiv:** https://arxiv.org/abs/2611.20448v2
- **发布:** 2026-11-16
- **作者:** Dongjia Zhao*, Yuchen Ma*, Chunsheng Shi*, Ziqiu Gui, Chao Yuan, Jianing Zhu, Zhaoxing Zhang, Yahui Liu, Daoxin Zhang, Yi Wu, Yao Hu, Cheng Chen†
- **机构:** Xiaohongshu Inc
- **摘要:** Multimodal search with image-text queries helps users find notes in user-generated content (UGC) communities and serves as a key search tool for multimodal search agents. For such queries, query-note relevance depends on the user's retrieval intent and cannot be determined by visual or topical similarity alone. Simply reranking visual search results cannot fully address this challenge, as notes relevant to the user's intent may be missing from the initial candidate set. This motivates explicit intent modeling to align candidate retrieval and reranking under consistent relevance criteria. We present MMIntentFlow, an intent-driven real-time multimodal search system deployed at Xiaohongshu over an index on the order of ten billion entries. MMIntentFlow represents retrieval objectives with a hierarchical intent taxonomy and uses intent-specific relevance criteria to guide data construction, representation learning, and reranking. An offline agentic data workflow acquires candidates and verifies their relevance under these criteria to produce training supervision. The embedding model combines intent-aware contrastive learning, graded ranking, and distribution distillation, while a compact reranker assesses query-candidate evidence conditioned on predicted hierarchical intents. Evaluations demonstrate that MMIntentFlow delivers substantial gains in search engagement while supporting real-time search at industrial scale. In a user-level A/B test on the Xiaohongshu platform, MMIntentFlow outperforms the existing production system based on visual search followed by reranking, achieving relative gains of 28.17% in Top-4 query click-through rate, 18.96% in query click-through rate, and 12.56% in average time spent on search results pages per user. Production monitoring records an end-to-end P50 latency of 1.07 s.
- **关键创新:**
  - 架构: hierarchical intent taxonomy 表示 retrieval objectives; intent-specific relevance criteria 对齐 candidate retrieval 与 reranking; offline agentic data workflow 验证 candidates 的 relevance。
  - 表征: intent-aware contrastive learning + graded ranking + distribution distillation; compact reranker conditioned on predicted hierarchical intents。
  - 效果: 小红书 ~10B entries 索引上 user-level A/B: Top-4 query CTR +28.17%, query CTR +18.96%, avg time spent +12.56%; P50 latency 1.07s。

## E. Sequential Modeling

### E1. Incentive Compatible Mechanisms for Sequential Fair Resource Allocation with Private Demands

- **arXiv:** https://arxiv.org/abs/2611.26800v1
- **发布:** 2026-11-19
- **作者:** Ramtin Salamat, Sean R. Sinclair, Seyed M.R. Iravani
- **机构:** Kellogg School of Management, Northwestern University (Ramtin Salamat); Department of Industrial Engineering and Management Sciences, Northwestern University (Sean R. Sinclair; S-M R Iravani)
- **摘要:** We study a strategic variant of the canonical online fair allocation problem, where a planner must sequentially allocate a divisible resource to agents with privately known demands. At each stage, the planner announces an allocation rule, the agent reports their demand, and the planner allocates resources according to the rule and the reported demand. Unlike the standard model, we allow agents to strategically misreport their needs, as can arise in nonprofit settings where demand is self-reported and monetary transfers are unavailable. We characterize the structure of incentive-compatible (IC) allocation rules in this model, and use this to identify conditions under which the optimal mechanism has a simple cap structure. We then develop an approximation method for the optimal IC mechanism through a careful reduction of the discretized dynamic program to a longest-path problem on a directed acyclic graph. Numerical experiments show that ignoring strategic reporting can be substantially more costly than imposing incentive compatibility.
- **关键创新:**
  - 提出机制设计: planner 在每个 stage 宣布 allocation rule, agent 报告 demand, planner 按 rule 分配; 对 strategic misreporting (self-reported demand, nonprofit 设置) 建模。
  - 用 IC allocation rules 的结构 + optimal mechanism 的 simple cap structure 条件, 推导至 discretized dynamic program 的 reduction to longest-path problem on DAG (numerical experiments: ignoring strategic reporting 比 imposing IC 更贵)。
  - approximation method for the optimal IC mechanism via DAG longest-path reduction。

### E2. Neural Conditional Gaussian Model: Efficient Data Assimilation with Sequential Uncertainty Quantification for Nonlinear Dynamics

- **arXiv:** https://arxiv.org/abs/2611.26463v1
- **发布:** 2026-11-19
- **作者:** Chuanqi Chena, Nan Chenb,∗
- **机构:** Department of the Geophysical Sciences, University of Chicago, Chicago, IL 60637 (a); Department of Mathematics, University of Wisconsin–Madison, Madison, WI 53706 (b)
- **摘要:** Data assimilation (DA) in partially observed nonlinear systems requires repeated estimation of both hidden states and their uncertainty. Conventional nonlinear filtering can be computationally expensive and often relies on an explicit dynamical model. In this paper, we develop the Neural Conditional Gaussian Model (Neural CGM), a data-driven dynamical model that maps unobserved physical states into a learned latent space, where the dynamics of the latent states follow a conditional Gaussian structure. This structure allows closed-form DA updates in the latent space, while nonlinear encoder-decoder mappings retain the flexibility needed to represent complex dynamics in physical space. A key feature of Neural CGM is its treatment of uncertainty in DA. The latent posterior mean and covariance are mapped to the physical variables through a Gaussian decoder that combines local moment propagation with learned nonlinear corrections. The resulting physical-space posterior statistics depend on the sequentially updated latent distribution rather than on a separate post-processing estimate. The same statistics enter a Gaussian negative log-likelihood during training, so both the posterior mean and uncertainty affect the learned model. Because Neural CGM learns the dynamical model itself, it can also be used for state forecasting and simulation without explicit knowledge of the governing equations. Numerical experiments on benchmark nonlinear dynamical systems show accurate state estimation and forecasting while substantially reducing online assimilation cost relative to conventional nonlinear DA methods. Neural CGM is therefore suited to repeated state estimation, uncertainty quantification, and prediction from partial observations.
- **关键创新:**
  - Neural CGM: learned latent space + conditional Gaussian structure → closed-form DA updates in latent space; Gaussian decoder 结合 local moment propagation + learned nonlinear corrections, 物理空间 posterior statistics 依赖于 sequentially updated latent distribution。
  - 训练: 用 Gaussian negative log-likelihood, posterior mean 与 uncertainty 都影响 learned model; 可用于 state forecasting/simulation without explicit governing equations。
  - 结果: benchmark nonlinear dynamical systems 上 accurate state estimation/forecasting, substantial reduction in online assimilation cost (见 abstract 具体值)。

### E3. Sequential Anytime Valid Tests for Efficient Inference-Time Alignment

- **arXiv:** https://arxiv.org/abs/2611.26413v1
- **发布:** 2026-11-19
- **作者:** Vishesh Kumar Singh, Sayak Ray Chowdhury
- **机构:** Indian Institute of Technology Kanpur, India
- **摘要:** Inference-time alignment methods, such as Best-of-N (BoN), improve language model outputs by generating multiple candidates per prompt and selecting among them using a reward model. Much of this cost is wasted: a fixed budget is applied to every prompt, although the computation required by prompts varies widely. Adaptive methods halt once sampled answers appear settled, but their thresholds are tuned heuristics with no statistical control over early-stopping errors. We instead seek an anytime-valid stopping rule that takes an error tolerance α as input and halts only once an answer is certified to hold a majority (θ_a > 1/2) under the generator's distribution. We aggregate candidates by final answer with a reward-weighted self-consistency (RWSC) score and treat stopping as a sequential test over the resulting clusters. Applying Wald's sequential probability ratio test to these clusters yields SPRT-RWSC, which performs well empirically, but its guarantee fails because the leading answer shifts during sampling, and the run is continuously monitored. Our main contribution, e-RWSC, replaces Wald's test with a betting supermartingale (an e-process) for every answer the policy produces, bounding the probability of ever certifying a non-dominant answer by α, uniformly over time and across all answers. The RWSC scores drive the bets, so they affect only how quickly a dominant answer a* is certified, not validity; certification takes O(log(1/α)/d_KL(θ_a*||1/2)) samples. Experiments across several language models, datasets, and reward models confirm the predicted 1/d_KL scaling of cost and show that accuracy improves over baselines at substantially lower token cost.
- **关键创新:**
  - Anytime-valid stopping rule: input error tolerance α, halt once an answer is certified to hold a majority (θ_a > 1/2) under the generator's distribution; reward-weighted self-consistency (RWSC) aggregates by final answer。
  - e-RWSC: replace Wald's sequential probability ratio test with a betting supermartingale (e-process) for every answer, bounding probability of ever certifying a non-dominant answer by α uniformly over time; certification cost O(log(1/α)/d_KL(θ_a*||1/2))。
  - RWSC scores drive the bets (affect only speed, not validity); experiments confirm 1/d_KL cost scaling and lower token cost vs baselines。

## F. Games

### F1. NitroGen: Observations on the Action Dynamics, Visual Instruction Following, and Spatial Exploration

- **arXiv:** https://arxiv.org/abs/2611.26807v1
- **发布:** 2026-11-19
- **作者:** Shengyuan Lin, Zhiling Li, Haoyu Nie, Ozan K. Tonguz
- **机构:** Carnegie Mellon University (Shengyuan Lin, Zhiling Li, Haoyu Nie, Ozan K. Tonguz); the paper notes affiliations at NVIDIA, Stanford University, and California Institute of Technology (Caltech)
- **摘要:** NitroGen is an open vision-action foundation model for game control. It is trained by behavior cloning on online gameplay videos. In this paper, we study the frozen controller in Hollow Knight and Trackmania as examples along three dimensions: action adaptation, visual instruction following, and spatial exploration. Our results indicate that NitroGen can adapt its actions to local context, but it lacks the planning, recovery, and exploration needed for longer-horizon game control.
- **关键创新:**
  - open vision-action foundation model for game control，由 online gameplay videos 上的 behavior cloning 训练；在 Hollow Knight 与 Trackmania 中实测 frozen controller：action adaptation 能适应 local context，但缺少 planning/recovery/exploration，不足 longer-horizon game control。
  - 对比: 与 `wiki/synthesis/2026-11-22/game-rl-daily.md` 系列中的游戏 AI（如 GameRealm、Algebraic World Model 等，强化学习/仿真方法）不同，NitroGen 是 open vision-action foundation model，行为引导依靠 behavior cloning。

### F2. AstronautBench: Measuring Agent Self-Improvement Across Episodes Through Knowledge, Evidence, and Progress

- **arXiv:** https://arxiv.org/abs/2611.26910v1
- **发布:** 2026-11-19
- **作者:** Congyuan Yu, Runping Tian
- **机构:** Carnegie Mellon University
- **摘要:** LLM agents are expected to improve themselves from their own experience across episodes, with fixed weights. Self-improvement in an embodied world cannot be read from one measure. Existing benchmarks measure task progress, world-knowledge question answering (QA), and episodic memory, but a correct answer does not show that the agent ever observed the evidence for it, and progress does not show what the agent learned. We introduce AstronautBench, which measures one agent's self-improvement through three views on the same run: what it knows, whether its own evidence supports that knowledge, and how far it gets in the world. It is built on the game Outer Wilds, where each episode is a 22-minute loop after which the world resets, only the agent's knowledge carries over, and progress is gated by knowledge. After every episode, we measure the places reached and ship-log rumor facts revealed, the correctness of answers to 164 questions about the world, and whether each answer is supported by the frames and position the agent cites from its own recorded play. Two LLM judges from different model families check every answer. In eight-episode baselines with GPT-6.1 Sol and Gemini 4 Argon planners, which act through a learned controller or their own gamepad inputs, the three views do not move together, so any one of them alone gives an incomplete picture of whether the agent is improving. The GPT-6.1 Sol agent's correct answers grow from 14.6% to 26.8% of all questions, but at episode 8 only 59 to 68% of them are supported by its cited evidence. It reveals no new rumor facts after episode 3, while the places it reaches and its memory keep growing. More than half of the answers that become correct after episode 3 cite only evidence from earlier episodes.
- **关键创新:**
  - 多维度测量 agent 自我改进: 三 views 同时衡量 — what it knows (knowledge), whether its own evidence supports that knowledge (evidence), how far it gets in the world (progress)。
  - 基于 Outer Wilds 游戏 (22 分钟 episode loop, 世界重置, 只有 knowledge carries over, progress gated by knowledge); 每 episode 衡量 places reached, ship-log rumor facts revealed, 164 个 world QA correctness, evidence support (frames/positions cited)。
  - 结果: GPT-6.1 Sol 正确率 14.6% → 26.8% (8 episodes), 但 evidence support 仅 59–68% (cited evidence 主要来自 earlier episodes); 三 views 不同步 — any one alone gives incomplete picture。

### F3. Learning Adaptive Defense Strategies: Fine-Tuned LLMs for Network Security Games under Network Mobility

- **arXiv:** https://arxiv.org/abs/2611.27180v1
- **发布:** 2026-11-20
- **作者:** Md Abu Sayed, Asif Rahman, Ahmed Ryen, Ahmed Hemida, Charles Kamhoua, Christopher Kiekintveld
- **机构:** University of Texas at El Paso, El Paso, Texas 79968, USA; DEVCOM Army Research Laboratory, MD 20783, USA
- **摘要:** Large language models(LLM) show promise for strategic reasoning, yet their ability to compute game-theoretic equilibria under dynamic conditions remains largely unexplored. This work investigates whether fine-tuned LLMs can serve as solver-free surrogates for online equilibrium computation in honeypot allocation, a setting in which network mobility continuously reshapes the underlying attack graph and forces repeated re-solving of a two-player zero-sum game. We construct a dataset of 270 security games on networks of 8--25 nodes with solver-grounded equilibrium labels, and evaluate four classes of predictor over 1{,}524 held-out mobility events: non-learned baselines, six open-weight architectures evaluated zero-shot, the same six after LoRA fine-tuning, and four proprietary models as an external reference point. Predictions are scored without post-hoc repair against exact game-theoretic criteria: exploitability against an optimal attacker best-response, equilibrium support accuracy, and distributional distance. Fine-tuning reduces exploitability across every architecture, and fine-tuned open-weight models of modest size outperform every zero-shot predictor, including proprietary ones; no zero-shot model at any tier reaches the floor set by uniform allocation. Stratifying by mobility type exposes a qualitative shift that aggregate metrics conceal: zero-shot models do not condition on whether a departing node lies on an attack path, while fine-tuned models recover this distinction. We further find that validation loss is negatively rank-correlated with task performance, and that output validity, rather than predictive accuracy, is the binding constraint on further progress.
- **关键创新:**
  - Fine-tuned LLMs as solver-free surrogates for online equilibrium computation: 数据集 270 security games on networks of 8–25 nodes (solver-grounded labels); 评估: non-learned baselines + 6 open-weight architectures (zero-shot) + same 6 after LoRA fine-tuning + 4 proprietary models (reference)。
  - 评估指标: exploitability vs optimal attacker best-response, equilibrium support accuracy, distributional distance; Fine-tuning reduces exploitability across every architecture, modest fine-tuned open-weight models outperform every zero-shot predictor。
  - Qualitative finding: zero-shot models do not condition on whether a departing node lies on an attack path; fine-tuned models recover this distinction; validation loss is negatively rank-correlated with task performance; output validity (not predictive accuracy) is the binding constraint.
