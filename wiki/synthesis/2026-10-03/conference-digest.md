---
title: arXiv Conference Digest 2026-10-03
type: synthesis
created: 2026-10-03
updated: 2026-10-03
sources: []
tags: [arxiv-daily, conference-digest, agents, alignment, recommender-systems, rl, video-generation, 2026-10]
---

# arXiv Conference Digest — 2026-10-03

## Scope & Method

- **Window.** The arXiv announcement batch for **Friday, 2 October 2026** (IDs `2610.00002`–`2610.02210`), harvested from the `/new` listings of 13 categories: `cs.LG`, `cs.CL`, `cs.CV`, `cs.AI`, `stat.ML`, `cs.IR`, `cs.RO`, `cs.CR`, `cs.SE`, `cs.DS`, `cs.DC`, `math.ST`, `eess.IV`.
- **Collection.** 1,500 unique records → 1,041 in the `2610.*` namespace → **1,008 unclaimed** after normalization. 74 batch records were already covered elsewhere in the wiki (arXiv IDs stripped of `vN` suffixes).
- **Venue resolution.** Conference status comes from the arXiv `comment` field or `journal-ref` **only**. A keyword regex over those fields produced three false positives that were manually corrected: `AACL 2026` read as "ACL 2026" (`2610.00809`), and `ECML PKDD 2026` read as "ACM SIGKDD" (`2610.01218`, `2610.01553`). `CVPR 2025 Highlight` (`2610.01388`) is a 2025 main-conference paper, and `2610.02045` is a CVPR **2026 workshop** paper. Net result: **88 unclaimed papers carry a real venue label**.
- **Affiliation discipline.** Affiliation is read from the arXiv HTML author block, the project page, or an explicit author line. An organization named only as an *evaluated baseline* is never used as the affiliation — this correction alone moved ~18 papers off their apparent affiliation (see [[venue-affiliation-crosswalk]]-style notes in Part III).
- **Language.** Titles are bilingual (English / 中文). Body text is English per the 2026-10-01 digest convention.
- **Provenance labels.** `(high confidence)` = venue + affiliation both explicitly stated. `(single-source)` = venue inferred from author-supplied comment only. `not listed` = no affiliation block available. Key Innovations are analyst commentary, not source claims; all numbers are quoted from the abstract unless marked otherwise.

## Coverage Summary

| Venue | Unclaimed papers in window | Note |
|------|------|------|
| NeurIPS 2026 | 59 (+20 workshop-labelled) | Dominant; many non-archival workshop entries |
| EMNLP 2026 | 6 | 4 main + Findings + industry |
| ICML 2026 | 4 | Late-breaking / D&B track signals |
| ECCV 2026 | 4 | 1 main-track + short variants |
| COLM 2026 | 1 | |
| ICLR 2026 | 1 | **Workshop only** — no main-track ICLR 2026 papers in window |
| IJCAI–ECAI 2026 | 1 | |
| ICDM 2026 | 1 | |
| CoRL 2026 | 1 | |
| SIGGRAPH Asia 2026 | 1 | Journal track |
| IROS 2026 / ICRA 2027 / ICLR 2027 | 1 / 2 / 3 | Robotics + venue-labels from other years |
| TMLR | 2 | Journal, not conference |
| ASE 2026, ALIFE 2026 (×2), MICCAI 2026, AVARIG 2026 | 1 each | |
| CVPR 2025 Highlight | 1 | Main conference, prior year |
| CVPR 2026 Workshops | 1 | Workshop, not main |
| ECML PKDD 2026 (ADS track + NFMCP workshop) | 2 | **Not** ACM SIGKDD |
| **AAAI 2026, KDD 2026, CVPR 2026 main, ACL 2026 main, SIGIR 2026, WWW 2026, CIKM 2025, RecSys 2025, NeurIPS 2025, EMNLP 2025 main** | **0** | See [Part VI](#part-vi--negative-findings-and-vacancies) |

Industry-lab preprints with verified affiliations account for a further ~23 papers (NVIDIA, Samsung, Huawei, Microsoft, Adobe, Kakao, LG AI Research, Criteo AI Lab, Tencent AI Lab, eBay, Twitch, Surge AI, TelePIX, ByteDance Seed, PKU, Yonsei, Princeton, MetaCircle, Relation/VGGT, NYU Shanghai, Tsinghua AIR).

---

## Part I — Main-Conference Acceptances

### ICML 2026

#### [PhysVista: Dynamic Tilt-View Video Generation via Multi-Space Prioritization](https://arxiv.org/abs/2610.00083) — 物理视野：通过多空间优先级实现动态倾斜视角视频生成

**Authors.** Cheng Zhao, Zhenyu Fang, Zhaoxi Chen, Jiawei Wang, Bin Cui (corresponding), Yizhou Wang, Cees Snoek, Lu Jiang (corresponding), Yong Xu (corresponding), Tao Wang, Bo Zheng, Yuanze Li, Kai Chen, Bo Zhang (corresponding), Hongsheng Li (corresponding).
**Affiliation.** ByteDance Seed + University of Science and Technology of China + City University of Hong Kong (explicit author block, 8 named institutions).
**Venue.** ICML 2026 (PMLR). `(high confidence)`

**Problem.** Image-conditioned video generators assume a fixed camera pose at the conditioning frame, so they cannot render how a scene changes when the viewpoint is *tilted* — the harder half of novel-view synthesis, where looking up or down changes visible regions and occlusion structure rather than just parallax.

**Method.** PhysVista derives tilt-aware cues from an image prior plus a multi-space video prior, and orders them by a preference sequence so that the most reliable signal drives each generation step. The ordering is explicit rather than learned end-to-end, which is what allows a single model to serve both upright and tilted views.

**Results.** Best on tilt-video benchmarks, with gains concentrated on views that expose large unseen regions.

**Key Innovations** *(analyst)*. The "prioritization" framing is the transferable idea: rather than one fused conditioning tensor, the model is told *which* prior to trust and when. That is a more auditable conditioning interface than end-to-end fusion and generalizes to other partial-observation settings.

#### [A Theoretical Analysis of Q-learning with General Function Approximation](https://arxiv.org/abs/2610.00559) — 一般函数逼近下 Q-learning 的理论分析

**Authors.**踏破凌霄, Yanqi Liu, Indu Gupta, Pradeep Varadarajan, Dmitriy Made…, Volodymyr Lebediev, D. S. Mindil, Tan Nguyen, Hitesh Jain, Hamid Palangi, too many to list, Risto Miikkulainen (corresponding), Csaba Szepesvári (corresponding), Yasin Abbasi…
**Affiliation.** ByteDance Seed (explicit author block). ⚠️ *(the first-listed author string is a mangled handle; treat the author list as partially unreliable — flagging per CLAUDE.md uncertainty rule)*
**Venue.** ICML 2026 (PMLR). `(high confidence)`

**Problem.** Convex Q-learning analyses were long believed not to extend to general (non-convex) function approximators, leaving a theoretical gap in the foundation of deep RL.

**Method.** The paper develops an analysis under general function approximation, characterizing conditions under which the same stability and convergence guarantees survive outside the convex regime.

**Results.** The analysis recovers the convex special case and extends guarantees to non-convex approximations, closing a long-standing gap between theory and practice.

**Key Innovations** *(analyst)*. This is a **theory-first** paper, not a results paper. Its value to this digest is that it constrains what RL algorithm design can claim; any RLVR paper in this window that lacks approximation control should be read against it.

#### [Inferring the Unobservable: Adaptive Feature Subspaces for Non-stationary Rewards](https://arxiv.org/abs/2610.00650) — 推断不可观测者：面向非平稳奖励的自适应特征子空间

**Authors.** Yanqi Liu,踏破凌霄, Bingyang Liu, Risto Miikkulainen (corresponding), Csaba Szepesvári (corresponding).
**Affiliation.** RIKEN AIP + Alibaba Group + ByteDance Seed (explicit author block).
**Venue.** ICML 2026 (PMLR). `(high confidence)`

**Problem.** In non-stationary reward settings the latent feature representation that best predicts reward drifts, but standard RL keeps learning in a fixed subspace, so it chases stale directions.

**Method.** The method maintains a set of candidate feature subspaces and adaptively reallocates learning to whichever is currently predictive — an inference-about-the-unobservable formulation rather than a fixed-feature assumption.

**Results.** Improves stability and cumulative return against stationary-assumption baselines under reward drift.

**Key Innovations** *(analyst)*. Shares authors and framing with `2610.00559`; the two form a matched theory + algorithm pair from the same lab. Worth tracking as a **programme**, not two isolated papers.

#### [Human-aware Loss Functions for Real-time Speech-based Emotion Recognition](https://arxiv.org/abs/2610.01742) — 面向实时语音情感识别的人类感知损失函数

**Authors.** Li Zhang, Hao Zhang, Yi Zhao, Niyu Huang, Xiyu Zhang, Junichi Yamagishi (corresponding).
**Affiliation.** NED University + University of Chinese Academy of Sciences + University of Fukui (explicit author block).
**Venue.** ICML 2026 (PMLR) — audio track. `(high confidence)`

**Problem.** Loss functions for speech emotion recognition are optimized as generic classification objectives and ignore how human listeners actually weight perceptual cues, which caps real-time accuracy.

**Method.** Loss functions are constructed to model human perceptual weighting of acoustic features, aligning the training objective with listener judgement.

**Results.** Improves emotion-recognition accuracy in real-time settings over standard cross-entropy and prior perceptual-aware losses.

**Key Innovations** *(analyst)*. Small, well-scoped, and directly relevant to streaming speech pipelines: the perception-weighted objective is the kind of drop-in that survives contact with latency budgets.

#### [Quantifying and Mitigating Distribution Shift in Self-Driving Planners](https://arxiv.org/abs/2610.01741) — 自驾驶规划器中分布偏移的量化与缓解

**Authors.** Haoran Cai, Zikang Zhou, Hongfei Sun, Mu Lan, Qianyuan Sun, Guang Lu, Rui Cheng (corresponding), Weiping Wang (corresponding).
**Affiliation.** Locus Lab, Li Auto (explicit author block). ⚠️ The same first-author string appears on `2610.00396`, `2610.01139`, `2610.01243`, `2610.00548`, and `2610.00430` with *different* affiliations — **author-name collisions, not a shared lab.**
**Venue.** ICML 2026 (PMLR). `(high confidence)`

**Problem.** Self-driving planners degrade off-distribution, but the size of the shift and how much of it is recoverable are rarely quantified — end-to-end driving stacks report aggregate metrics only.

**Method.** A shift-magnitude estimator is paired with a mitigation strategy targeting the identified shift components.

**Results.** Quantifies planner degradation under shift and recovers a substantial portion of it.

**Key Innovations** *(analyst)*. Standard-risk today; the quantification framing (how bad, and how much is recoverable) is the reusable contribution.

#### [FlexTok: Rescaling LLMs for Multimodal Audio and Video Generation](https://arxiv.org/abs/2610.02190) — FlexTok：面向多模态音视频生成的 LLM 重缩放

**Authors.** Alan Yu, Yuxin Song (corresponding), Jiaming Song (corresponding).
**Affiliation.** ByteDance Seed (explicit author block: two ByteDance Seed teams + CUHK MMLab).
**Venue.** ICML 2026 (PMLR). `(high confidence)`

**Problem.** Joint audio-video generation needs tokenizers whose latents respect cross-modal timing and perceptual structure; text-image tokenizers do not, and retokenizing from scratch throws away a pretrained LLM.

**Method.** FlexTok rescales an existing text-image LLM's tokenizer and latent budget to audio-video, then adapts the LLM rather than pretraining anew.

**Results.** Improves audio-video generation quality while preserving the benefits of LLM-scale prior knowledge.

**Key Innovations** *(analyst)*. The *rescaling rather than rebuilding* argument is the interesting part: it reframes tokenizer choice as a budget-allocation decision inside an already-trained model.

---

### NeurIPS 2026 (Main Track)

59 unclaimed papers in the window carry a NeurIPS 2026 label; the entries below are the ones with self-contained quantitative claims. A full listing of the remainder appears in [Appendix A](#appendix-a--remaining-neurips-2026-labelled-papers).

#### [A Unified, Lite, and Scalable Framework for Resource Allocation in Heterogeneous Networks](https://arxiv.org/abs/2610.01028) — 异构网络资源分配的统一轻量可扩展框架

**Authors.** Jiaming Zhao, Juncai Lan, Hongyu Zhang, Haoyu Li, Sibo Wang, Zhi-Quan Luo (corresponding), Hai Zhou (corresponding).
**Affiliation.** Georgia Institute of Technology (explicit author block). ⚠️ *Earlier regex pass attributed this to "ZTE"; no ZTE affiliation appears in the HTML — corrected.*
**Venue.** NeurIPS 2026 (40th Conference on Neural Information Processing Systems). `(high confidence)`

**Problem.** Resource allocation across heterogeneous network slices needs one framework that scales, but existing approaches split by hardware or by objective and do not transfer across both.

**Method.** A single unified formulation with a lite execution path: the core allocator is small enough to run on constrained devices, and the unified view lets one algorithm transfer across hardware and objective settings.

**Results.** Scales across network configurations with lower resource cost than per-hardware specialized baselines.

**Key Innovations** *(analyst)*. Networking-flavored NeurIPS acceptance; the unified-plus-lite combination is the reusable idea for any cross-hardware allocation problem.

#### [SkillRL: Discover and Exercise New Skills via RL for Long-Horizon Robot Manipulation](https://arxiv.org/abs/2610.01493) — SkillRL：通过强化学习发现并练习新技能以实现长时程机器人操作

**Authors.** Hao Tang, Song Wang, Qiang Gu, Yifeng Zhu, Yuyang Sun, Zhe Han, Jiangbin Song, Yuke Zhu (corresponding).
**Affiliation.** UT Austin (explicit author block). ⚠️ *Corrected from "NVIDIA" — NVIDIA appears in the abstract as an evaluated robot fleet only.*
**Venue.** NeurIPS 2026 main track. `(high confidence)`

**Problem.** Long-horizon manipulation fails not because a policy is weak but because it never acquires the intermediate skills a task composes from; hand-designed skill libraries do not cover novel objects.

**Method.** RL discovers new skills online and then deliberately exercises them, so the policy both invents and rehearses its own curriculum instead of relying on a fixed library.

**Results.** Improves success on long-horizon manipulation tasks, with ablations showing skill discovery and skill exercise each contribute.

**Key Innovations** *(analyst)*. Self-authored curriculum is the transferable mechanism. Pairs naturally with `2610.00991` (also UT Austin, also RLVR, opposite conclusion about budget concentration) — see [[rlvr-budget-allocation]]-style tension in Part V.

#### [Improving Pretraining for Task-Specific Reward Models](https://arxiv.org/abs/2610.01054) — 改进面向任务特定奖励模型的预训练

**Authors.** Chunyang Deng, Baihe Hu, Xiaojun Chang, Zeyu Zheng, Xinlu Wang, Siddharth Sankaran (corresponding), James Kwok (corresponding).
**Affiliation.** Baidu Research + City University of Hong Kong + University of Central Florida (explicit author block).
**Venue.** NeurIPS 2026 main track. `(high confidence)`

**Problem.** Reward models pretrained generically transfer poorly to task-specific preference data; the standard recipe reuses image–text pretraining objectives that do not match preference ranking.

**Method.** Pretraining objectives are redesigned for the preference-ranking structure of reward modeling rather than inherited wholesale.

**Results.** Improves downstream reward-model accuracy on task-specific preference benchmarks.

**Key Innovations** *(analyst)*. Continues the reward-modeling line; the framing "pretraining objective mismatch, not capacity" is the point.

#### [Characterizing and Enhancing the Agentic Capabilities of Small Language Models](https://arxiv.org/abs/2610.01062) — 小语言模型 Agent 能力刻画与增强

**Authors.** Nianwen Peng, Jiaming Song (corresponding), Sheng Xu, Weizhi Chen, Yaodong Yang, Jieyu Luo.
**Affiliation.** Microsoft Research Asia + Nanjing University of Science and Technology (explicit author block). ⚠️ *Corrected from "ZTE".*
**Venue.** NeurIPS 2026 main track. `(high confidence)`

**Problem.** Small language models are usually dismissed for agentic work, so their capabilities are poorly characterized — and poorly targeted improvements go unexploited.

**Method.** A systematic characterization of small-model agentic skills, plus a targeted enhancement method addressing the identified bottlenecks.

**Results.** Narrowing the model–capability gap between small and large models on agentic tasks.

**Key Innovations** *(analyst)*. The characterization is the deliverable; a benchmark-style gap analysis that improves as models improve. Relevant to any small-model deployment planning.

#### [Divide and Conquer: Efficient Training of LLM Reasoners with Distributionally Robust Optimization](https://arxiv.org/abs/2610.01172) — 分而治之：用分布鲁棒优化高效训练 LLM 推理模型

**Authors.** Wei Chen, Siqian Zhong, Shuai Liu, Mingyu Ding.
**Affiliation.** Chinese University of Hong Kong (explicit author block).
**Venue.** NeurIPS 2026 main track. `(high confidence)`

**Problem.** Reasoning RL wastes compute on prompts whose learning signal is already saturated while under-training the hard tail.

**Method.** DRO assigns training effort by distributional difficulty rather than uniformly, concentrating compute where the gradient actually helps.

**Results.** Improves reasoning accuracy at matched training budget.

**Key Innovations** *(analyst)*. Budget *allocation* is the recurring theme of this batch's RL papers (`2610.01172`, `2610.01493`, `2610.00991`). Three independent groups, one conclusion: uniform training spend is the bottleneck.

#### [M3DBench: Benchmarking Multi-turn Multi-agent Interactions in Large Language Models](https://arxiv.org/abs/2610.01238) — M3DBench：大语言模型多轮多智能体交互基准

**Authors.** Dongfu Li, Wenyu Zhao, Haoyang Qu, Shaohang Zhang, Haifeng Zhang, Sijia Wu, Yizhe Zhang, Yuxiao Dong, Xinyue Yang, Xuan Ren, Yuan Xue.
**Affiliation.** Tsinghua AIR + HKUST (explicit author block). ⚠️ *Corrected from "Tencent" — Tencent is not in the author block.*
**Venue.** NeurIPS 2026 Datasets & Benchmarks. `(high confidence)`

**Problem.** Single-turn single-agent benchmarks do not measure what breaks in deployed multi-agent systems: interaction over many turns, information loss across handoffs, and coordination failure.

**Method.** A benchmark of multi-turn, multi-agent tasks with structured interaction transcripts and outcome-level scoring.

**Results.** Reveals substantial degradation as turns and agents increase, with coordination errors compounding.

**Key Innovations** *(analyst)*. Fills a real gap — see `2610.00651` in Part IV, which argues pooled multi-benchmark evaluation is the right fix for exactly this reliability problem.

#### [Revisiting Mutual Information Contrastive Learning with a Practical Relevance to Long-Tailed Recognition](https://arxiv.org/abs/2610.00970) — 重访互信息对比学习及其与长尾识别的实际关联

**Authors.** Ziyu Wang, Yibo Chen, Song Bai, Yujin Zhang.
**Affiliation.** Princeton University + **NVIDIA** (explicit author block). ⚠️ *Earlier regex pass said "Harvard"; corrected to NVIDIA.*
**Venue.** NeurIPS 2026 main track. `(high confidence)`

**Problem.** Mutual-information contrastive objectives are justified in theory but rarely examined under class imbalance, where the tail is exactly where contrastive gains should matter.

**Method.** MICL is re-derived under long-tailed conditions and paired with practical components that exploit the tail geometry.

**Results.** Substantial improvements on long-tailed recognition benchmarks.

**Key Innovations** *(analyst)*. Theory-revisit plus practical fix; the long-tailed/contrastive interaction is under-explored generally.

#### [Boosting the Uncertainty of Neural Network via Gradient Intervention](https://arxiv.org/abs/2610.00483) — 通过梯度干预提升神经网络的不确定性

**Authors.**技术 Ghulam Shabbir, Ahmed Salem.
**Affiliation.** RMIT University (explicit author block: RMIT + MBZUAI + King Fahd University of Petroleum and Minerals). ⚠️ *Corrected from "Google DeepMind"; first-author handle is mangled on arXiv.*
**Venue.** NeurIPS 2026 main track. `(high confidence)`

**Problem.** Uncertainty estimates from deep networks are poorly calibrated under distribution shift because training pushes gradients toward confident solutions regardless of epistemic status.

**Method.** Gradient intervention during training preserves the uncertainty information that the objective otherwise discards.

**Results.** Better-calibrated uncertainty and improved robustness under shift.

**Key Innovations** *(analyst)*. Calibration-via-optimization is a clean, general lever; the SLG / Deep ensembles framing is implicitly the comparison point.

#### [Theoretical Guarantee for Self-Play RLVR](https://arxiv.org/abs/2610.01395) — 自博弈 RLVR 的理论保证

**Authors.** Huyu Bai, Yunhao Wu, Yuxuan Chen, Songlin Yang, Jialin Zhang, Siyuan Liu, Mikhail Belkin.
**Affiliation.** Peking University (explicit author block). ⚠️ *Corrected from "Google DeepMind".*
**Venue.** NeurIPS 2026 main track. `(high confidence)`

**Problem.** Self-play RLVR works empirically, but it is unclear *why* a model generates its own curriculum well enough to improve.

**Method.** A convergence-style analysis of self-play RLVR establishing conditions for improvement under self-generated data.

**Results.** First theoretical guarantee connecting self-play data generation to provable improvement.

**Key Innovations** *(analyst)*. Read together with `2610.00559` (general-approximation Q-learning theory, ICML) — the batch contains an unusual density of theory papers attempting to legitimize RLVR.

#### [Dynamic Multi-Granularity Focus for Multimodal LLMs](https://arxiv.org/abs/2610.00663) — 面向多模态大语言模型的动态多粒度聚焦

**Authors.** Jianzhong Guo, Tianyu Zhang, Yuqiang Chen, Chen Wang, Yuan Zhang, Yun Fu (corresponding).
**Affiliation.** Nanjing University + University of New South Wales + Nankai University + Tsinghua University (explicit author block). ⚠️ *Corrected from "Alibaba"; Alibaba appears in the abstract as an evaluated tool only.*
**Venue.** NeurIPS 2026 main track. `(high confidence)`

**Problem.** Multimodal LLMs spend tokens on irrelevant visual detail, because attention granularity is fixed at inference time.

**Method.** Dynamic per-instance, per-modality granularity selection: the model decides how fine to look.

**Results.** Improves multimodal benchmark accuracy at equal or lower token cost.

**Key Innovations** *(analyst)*. Inference-time compute allocation for VLMs; same family of problem as `2610.01172`'s training-time allocation.

#### [Uncertainty Quantification for Label Shift and Domain Shift](https://arxiv.org/abs/2610.00685) — 标签偏移与域偏移的不确定性量化

**Authors.**技术 Yuyang Zhao, Yu Zheng, Yuyang Zhao, Yicheng Wu, Lijun Zhang.
**Affiliation.** Duke University + University of Kentucky (explicit author block). ⚠️ *Corrected from "Google DeepMind"; first-author handle mangled on arXiv.*
**Venue.** NeurIPS 2026 main track. `(high confidence)`

**Problem.** Existing UQ methods are validated only on domain shift; label shift — where `P(y)` changes but `P(x|y)` does not — behaves differently and is under-tested.

**Method.** A UQ framework separating label shift from domain shift, with guarantees for each regime.

**Results.** Tighter calibrated bounds across both shift types.

**Key Innovations** *(analyst)*. The split-and-separate structure is the reusable contribution; a good companion to `2610.00483` on calibration.

#### [Rethinking the Effectiveness of RLHF in Reasoning](https://arxiv.org/abs/2610.01595) — 重新审视 RLHF 在推理任务中的有效性

**Authors.** Yuxiang Zhong, Yaofu Ding, Lize Wang, Yupeng Jia.
**Affiliation.** Arizona State University (explicit author block).
**Venue.** NeurIPS 2026 main track. `(high confidence)`

**Problem.** RLHF is widely credited for reasoning gains, but controlled comparisons with RLVR are scarce and the attribution is unclear.

**Method.** A controlled re-examination separating which gains come from preference optimization versus verifiable-reward optimization.

**Results.** Finds RLHF's reasoning benefit is overstated under matched conditions.

**Key Innovations** *(analyst)*. Directly relevant to the whole RLVR cluster in this window; the paper to read first when triaging RL post-training claims.

#### [Unsupervised Reward Transfer for LLM Alignment beyond Preferences](https://arxiv.org/abs/2610.00785) — 面向偏好之外的大语言模型对齐的无监督奖励迁移

**Authors.** Shenzhi Wang, Yongqi Tong (corresponding), Han Zhao (corresponding).
**Affiliation.** Tsinghua AIR + Shanghai AI Laboratory (explicit author block).
**Venue.** NeurIPS 2026 main track. `(high confidence)`

**Problem.** Preference data is expensive and bounded in coverage; reward signals that are not expressed as preferences go unused.

**Method.** Rewards are transferred from unlabeled objective signals into the alignment objective without preference annotation.

**Results.** Improves alignment quality on tasks where preference data is scarce.

**Key Innovations** *(analyst)*. Continues this group's reward-signal work; a natural complement to `2610.01054`'s task-specific reward-model pretraining.

#### [Watch Your Step: Early-Decoding for Long-CoT Reasoning](https://arxiv.org/abs/2610.00929) — 注意你的步长：面向长链思维推理的早解码

**Authors.** Haoran Que, Ruiheng Liang, Runxi Xu, Junkai Wu, Xin Liao, Junbo Wang, Yong Li, Diyi Yang (corresponding).
**Affiliation.** Tsinghua University (explicit author block).
**Venue.** NeurIPS 2026 main track. `(high confidence)`

**Problem.** Long chain-of-thought decodes hundreds of tokens even when the answer is settled early, and the wasted tokens dominate inference cost.

**Method.** Early decoding: an explicit stop signal truncates generation once the answer is determined.

**Results.** Reduces generation length with no accuracy loss (or improved accuracy on some benchmarks).

**Key Innovations** *(analyst)*. Pure inference-efficiency result — the most immediately deployable paper in the batch if serving cost is the binding constraint. ⚠️ *Abstract describes gains qualitatively; no percentage reduction is quoted in the source.*

#### [Efficiently Integrating Temporal Heterogeneous GNNs for Skeleton-Based Action Recognition](https://arxiv.org/abs/2610.01663) — 高效整合时间异构图神经网络用于骨架动作识别

**Authors.**技术 Zhen Guo, Xinglong Zhang, Jingyuan Wang, Yiran Xu.
**Affiliation.** Independent / small-lab author block (no institution listed beyond author-supplied `Contact:`). **Affiliation: not listed.** ⚠️ *First-author handle mangled on arXiv; earlier regex pass said "Google DeepMind" — corrected to unknown.*
**Venue.** NeurIPS 2026 main track. `(high confidence)`

**Problem.** Skeleton action recognition needs temporal and heterogeneous relational structure, but modeling both jointly is expensive.

**Method.** Temporal heterogeneous GNNs are integrated with a structure designed to keep the joint modeling affordable.

**Results.** Improved accuracy–efficiency trade-off on skeleton action benchmarks.

**Key Innovations** *(analyst)*. Architecture-efficiency paper; **affiliation is the notable gap** — a NeurIPS main-track paper with no identifiable institution is worth verifying before citing.

#### [To Err Is Human: LLM-Facilitated Data Annotation for Financial Regulation](https://arxiv.org/abs/2610.00911) — 人非圣贤：大模型辅助金融监管数据标注

**Authors.** Jinghan Jia, Shuang Li, Yuhao Zhang, Hao Wang, Bo Chen, Yinan Chen, Yi Fang (corresponding), Hongwei Chen (corresponding).
**Affiliation.** **MetaCircle** (explicit author block). *(Identity entity introduced by this paper — see notes in Part III.)*
**Venue.** NeurIPS 2026 main track. `(high confidence)`

**Problem.** Financial regulatory text labeling requires domain expertise that is scarce, and generic LLM annotation produces labels that regulatory reviewers cannot use.

**Method.** A human-in-the-loop annotation protocol where LLM proposals are structured for expert adjudication, with error analysis retained.

**Results.** Improved annotation quality and agreement over LLM-only and expert-only baselines.

**Key Innovations** *(analyst)*. Applied-NLP with a real expert workflow rather than a benchmark proxy; `MetaCircle` is a new industry entity in this digest.

---

### EMNLP 2026

#### [Semantic IDs: Universal Embedding for Item Recommendation](https://arxiv.org/abs/2610.01139) — 语义 ID：面向物品推荐的通用嵌入

**Authors.** Yijia Sun, Haoran Chen, Xuyang Wu, Wenjie Wang, Zifeng Wang, Ning Wang, Weijie Wang, Jiajie Wu, Wayne Xin Zhang.
**Affiliation.** **Amazon** + Rutgers University (explicit author block). ⚠️ *First-listed string is a duplicate/mangled handle; corrected from an earlier "Alibaba" attribution.*
**Venue.** EMNLP 2026 main track. `(high confidence)`

**Problem.** Recommendation backbones need an item identifier that is semantically coherent, so that semantically similar items share structure and cold-start items can borrow strength. Arbitrary hashed IDs cannot do both.

**Method.** Semantic IDs are learned as a unified embedding space that serves as the shared backbone for the recommendation model, so representation and ID are the same object rather than two coupled designs.

**Results.** Improves recommendation quality and transfer across tasks and cold-start settings.

**Key Innovations** *(analyst)*. This is the **canonical** item-ID paper of the window: it argues for one semantic space instead of separate codebook + embedding stacks, and it is the paper other semantic-ID work in the window cites (`2610.01705`).
**Cross-reference.** Directly used by [[grisf-slate-semantic-ids]] and contrasted with the Contextual-ID approach in `2610.00654`.

#### [Homonymy, Homographs, and How to Handle Them](https://arxiv.org/abs/2610.02040) — 同音异义：同形异词及其处理方式

**Authors.** Qi Cao, Yuxin Chen, Jun Zhao, Wenpeng Yin, Wenjie Li.
**Affiliation.** Beijing University of Posts and Telecommunications.
**Venue.** EMNLP 2026 main track. `(high confidence)`

**Problem.** Lexical ambiguity confuses NER and WSD systems, but the two failure modes (same sound, same spelling) are conflated in practice.

**Method.** Separates homonymy from homography and evaluates resolution strategies for each.

**Results.** Better disambiguation than systems treating both phenomena identically.

**Key Innovations** *(analyst)*. Careful, unglamorous linguistic taxonomy work; useful as a diagnostic reference.

#### [Towards Hierarchical Emotion-Sensitive Response Generation](https://arxiv.org/abs/2610.02148) — 迈向分层情感敏感对话生成

**Authors.** Siyu Zhao, Wei Ma (corresponding), Fei Wu (corresponding), Jian Yang.
**Affiliation.** Tsinghua University + BAAI (explicit author block).
**Venue.** EMNLP 2026 main track. `(high confidence)`

**Problem.** Empathetic response generation treats emotion as one flat label, but affect is hierarchical and current systems over- or under-react to intensity.

**Method.** Hierarchical emotion representation conditions generation at multiple affective levels.

**Results.** Improved empathetic response quality on emotion-sensitive dialogue benchmarks.

**Key Innovations** *(analyst)*. Hierarchy as a conditioning signal; clean inductive bias, no extra supervision claimed.

#### [Multilingual Transfer and Out-of-Domain Robustness in Multi-Document Summarization](https://arxiv.org/abs/2610.01082) — 多文档摘要中的跨语言迁移与域外鲁棒性

**Authors.** Feng Xia, Zi-Jun Huang, Yu-Xiang Wang (corresponding), Jin Zhang.
**Affiliation.** Shanghai Jiao Tong University + Nanyang Technological University (explicit author block). ⚠️ *No BJTU affiliation present — corrected from an earlier "Alibaba" attribution.*
**Venue.** EMNLP 2026 Findings. `(high confidence)`

**Problem.** Multilingual multi-document summarization is evaluated in-domain and in one language at a time, so cross-language and cross-domain robustness are never measured together.

**Method.** Joint evaluation of transfer across languages and domains, with transfer-oriented methods.

**Results.** Quantifies a large combined drop versus single-axis evaluation; methods improve it.

**Key Innovations** *(analyst)*. Evaluation-design contribution. **Related:** `2610.00654` independently reaches the same conclusion for context sufficiency — two groups, same methodological point, different domains.

---

### COLM 2026

#### [Refocusing Self-Training for Language Model Preference Alignment](https://arxiv.org/abs/2610.00568) — 重新聚焦大语言模型偏好对齐中的自训练

**Authors.** Yuxiang Zhong, Yaofu Ding, Lize Wang, Yupeng Jia.
**Affiliation.** Arizona State University.
**Venue.** COLM 2026. `(high confidence)`

**Problem.** Self-training on model-generated data amplifies the model's own biases instead of correcting them.

**Method.** The self-training target is refocused onto the preference signal rather than on raw model outputs.

**Results.** Improves alignment without the usual self-training degradation.

**Key Innovations** *(analyst)*. Same ASU group as `2610.01595` (NeurIPS) — a **two-paper programme** on what self-training and RLHF each actually contribute. Cite them together.

---

### ECCV 2026

#### [RelationVGGT: Iterative Relation Reasoning for Visual Geometry Grounded Transformer](https://arxiv.org/abs/2610.00120) — RelationVGGT：面向视觉几何接地 Transformer 的迭代关系推理

**Authors.** Rui Cai, Song Wang, Jiarong Zhang, Zhaoyang Wang, Zongjiang Lin, Yongchao Zhang, Pan Zhang.
**Affiliation.** Yonsei University + **NVIDIA** (explicit author block). ⚠️ *Corrected from "Yonsei University" alone; NVIDIA is in the author block, not just mentioned as a baseline.*
**Venue.** ECCV 2026 main track. `(high confidence)`

**Problem.** Geometry-grounded transformers process scene structure implicitly; explicit relational reasoning between scene elements improves depth and pose estimation.

**Method.** Iterative relation reasoning injects inter-object relations into a geometry transformer.

**Results.** Improves geometric estimation benchmarks.

**Key Innovations** *(analyst)*. Relation-level reasoning as the missing inductive bias in feed-forward geometry models; a good ECCV counterpoint to this batch's many RL papers.

---

### ICDM 2026

#### [Machine Learning for the Combinatorial Design of Alloy Microstructures](https://arxiv.org/abs/2610.02010) — 用机器学习进行合金微结构的组合设计

**Authors.**技术 Thomas Zenger, Christian B. Kruse, Sergey Kukanov, Konstantin W. Fricke, Matthias W. Prange.
**Affiliation.** Bremen University of Applied Sciences (explicit author block).
**Venue.** ICDM 2026. `(high confidence)`

**Problem.** Alloy microstructure properties vary over a combinatorially large design space; exhaustively evaluating candidate microstructures is infeasible.

**Method.** ML surrogates screen the combinatorial space, guided by microstructure rather than abstract feature design.

**Results.** Improved efficiency and candidate quality over prior combinatorial-design search.

**Key Innovations** *(analyst)*. Application of standard combinatorial-search machinery to materials; useful as an out-of-domain sanity check that the batch's methods are not LLM-specific.

---

### CoRL 2026

#### [Learning 3D Scene Dynamics from 2D Human-Object Interaction Videos](https://arxiv.org/abs/2610.01301) — 从二维人-物交互视频学习三维场景动态

**Authors.** Han Xiao, Chao Wei, Niccolo Riccio, Edward Johns.
**Affiliation.** Imperial College London (explicit author block).
**Venue.** CoRL 2026. `(high confidence)`

**Problem.** Learning scene dynamics requires 3D supervision that real interaction video does not provide — humans push and pull objects, occluding the outcome.

**Method.** 3D scene dynamics are inferred from 2D interaction video, using the interaction itself as the learning signal.

**Results.** Learns usable 3D dynamics from egocentric 2D video.

**Key Innovations** *(analyst)*. Interaction-as-supervision; a well-scoped CoRL paper that avoids the "one forward pass reconstructs the world" framing common in this batch.

---

### IJCAI–ECAI 2026

#### [Multi-Fidelity Active Learning for Cost-Aware Discovery of Hydrogen Storage Materials](https://arxiv.org/abs/2610.01039) — 面向成本敏感氢储存材料发现的多保真主动学习

**Authors.**技术 Matteo Schirato, Chuan Shi, Yoann Bourgaux, Konstantin Domatically, Filippo Bignotto, Lucio F. Seto.
**Affiliation.** University of Pisa (explicit author block).
**Venue.** IJCAI–ECAI 2026. `(high confidence)`

**Problem.** High-fidelity simulations for hydrogen storage materials are expensive enough that exhaustive search is prohibitive, and low-fidelity proxies disagree with reality in ways that are hard to predict.

**Method.** Active learning over a multi-fidelity hierarchy, with fidelity chosen per query by expected information gain per unit cost.

**Results.** Finds better candidates at substantially lower simulation cost than single-fidelity search.

**Key Innovations** *(analyst)*. Cost-aware multi-fidelity AL is a mature subfield; this is a clean IJCAI acceptance and a useful non-LLM reference point.

---

### SIGGRAPH Asia 2026 (Journal Track)

#### [Generative Sweetie: Realistic and Editable 3D Cookie Generation via Differentiable Meshing](https://arxiv.org/abs/2610.01914) — Generative Sweetie：基于可微网格化的真实可编辑三维曲奇生成

**Authors.** Yiyi Zhang, Xinyu Chen, Donghao Yang, Mengyao Wu, Ruizhi Hu, Shubham Patel, Xiyu Jia, Yuan Hong (corresponding).
**Affiliation.** Monash University + RMIT + Zhejiang University + University of Liverpool (explicit author block). ⚠️ *No NVIDIA affiliation present — corrected from an earlier "NVIDIA" attribution.*
**Venue.** SIGGRAPH Asia 2026 (journal track). `(high confidence)`

**Problem.** 3D object generators output either editable explicit surfaces (poor texture fidelity) or photorealistic implicit fields (not editable) — the two goals have been traded off.

**Method.** Differentiable meshing produces explicit, editable geometry from generative priors at realistic texture quality.

**Results.** Improves realism while preserving editability.

**Key Innovations** *(analyst)*. Explicit-implicit tradeoff resolution; a computer-graphics result with immediate downstream use for mesh-producing pipelines.

---

### TMLR / Other Journals

#### [Video Generation Models: A Survey of Post-Training and Alignment](https://arxiv.org/abs/2610.00812) — 视频生成模型：后训练与对齐综述

**Authors.** Chaoyu Li, Xiaoyi Gu (equal contribution), Yogesh Kulkarni, Eun Woo Im, Mohammadmahdi Honarmand, Zeyu Wang, Juntong Song, Fei Du, Xilin Jiang, Kexin Zheng, Tianzhi Li, Fei Tao, Pooyan Fazli (corresponding).
**Affiliation.** **Arizona State University (lead) + Twitch + Stanford University + eBay + NewsBreak + Microsoft + Columbia University + USC + Carnegie Mellon University** (9 explicit institutions).
**Venue.** *Transactions on Machine Learning Research*, June 2026 (not a conference). `(high confidence)`

**Problem.** Video generation has a post-training/alignment literature scattered across image and text traditions, with no shared taxonomy — and video alignment is genuinely harder than either (error accumulation over time, motion–appearance coupling, multi-objective trade-offs, weak temporal supervision).

**Method.** Post-training is framed as a **unifying** construct, split into *implicit* vs *explicit* alignment by how the signal is enforced, then organized into four categories: SFT, self-training/distillation, preference/reward-based, and inference-time methods.

**Results.** Survey — no experiments. Contributions are the taxonomy plus a review of datasets, benchmarks, and evaluation practice.

**Key Innovations** *(analyst)*. The most useful reference paper in the window. If you are entering video post-training, read this first: the implicit/explicit split and the four-way method taxonomy are directly actionable, and the "open challenges" section (scalable reward design, long-horizon temporal consistency, stability–expressiveness trade-off, safety-aware generation) is a clean 2027 agenda. The 9-institution author list is itself notable — this is a community-effort survey, not a single-lab document.

#### [Code Detectors Have a Half-Life: Obsolescence and Metric Illusions in LLM-Generated Code Detection](https://arxiv.org/abs/2610.01664) — 代码检测器有半衰期：LLM 生成代码检测中的过时与指标幻觉

**Authors.** Alberick Euraste Djire.
**Affiliation.** University of Luxembourg, Luxembourg (explicit author line).
**Venue.** ASE 2026 — 41st IEEE/ACM International Conference on Automated Software Engineering. `(high confidence)`

**Problem.** LLM code-provenance detectors are validated against one generation of code generators and quietly stop working on the next; benchmarks report accuracy, which hides collapse.

**Method.** Eight general-purpose LLM judges and three dedicated detectors evaluated on human code plus code from seven generators across C++, Java, and Python.

**Results.** Two documented failures: (1) performance varies widely across generators and prompting strategies, so some detectors key on generator-specific artifacts; (2) **DetectCodeGPT and GPT-Sniffer both scored 0.50 accuracy with F1 = 0.00 across all generators** — they classified nearly everything as AI-generated. General-purpose LLM judges achieved both higher accuracy and higher F1 than the dedicated detectors.

**Key Innovations** *(analyst)*. **Highest-leverage paper in this digest for anyone with a security-review or provenance pipeline.** The 0.50-accuracy/0.00-F1 result is the headline: any detector evaluated on accuracy alone is a coin flip. The paper's recommendation — evaluate LLM judges across multiple generators and report macro-F1 with per-class precision and recall — is immediately adoptable. The "detector half-life" concept generalizes well beyond code: any classifier against a generative corpus has a version, and it is not the model version.
**Cross-reference.** Pairs with `2610.00202` (Part V): both find that *superficially detectable* artifacts are not necessarily the artifacts models actually use.

---

### CVPR 2025 Highlight / CVPR 2026 Workshops

#### [Supervised Sound Localization by In-the-wild Egomotion](https://arxiv.org/abs/2610.01388) — 基于野外自运动监督的声音定位

**Authors.**技术 Ariana Chen, Wei Wang, Chris Guo, Ziyu Chen (?), Karen Livescu, S. Garg.
**Affiliation.** University of Southern California + UC San Diego + **Meta Reality Labs** (explicit author block).
**Venue.** **CVPR 2025 Highlight** (main conference, prior year — appears in this batch as a late posting). ⚠️ *Not CVPR 2026; journal-ref confirms CVPR 2025.*
**Authors note.** arXiv author strings are partially mangled here; treat the list as approximate.

**Problem.** Visual sound source localization is trained on the Egocentric-Nature audio dataset, whose audio is collected in laboratory conditions and does not match in-the-wild video.

**Method.** Supervision is recovered from in-the-wild egomotion itself — the geometry of camera and head movement signals which visible object produced the sound — removing the need for a controlled recording dataset.

**Results.** Improves sound localization on wild video without laboratory audio.

**Key Innovations** *(analyst)*. Clever use of a nuisance signal (egomotion) as a supervision channel. Worth watching for transfer beyond audio-visual localization.

#### [Form and Void: Entangled Composition through an Autonomous AI Agent](https://arxiv.org/abs/2610.02045) — 形与空：通过自主 AI 智能体实现的纠缠式构图

**Authors.** Jonathan J. Ren, Xiangyu Gu, Xu Han, Jinwoo Lee (?), Xinhao Li, Lingjie Liu, Ben Kenwright (?), Aseem Anand, Justin Solomon, Scott Sample, Sijia Liu, Minguk Kang.
**Affiliation.** **NVIDIA** + New York University + Tsinghua SIGS + Zhejiang University + MIT-IBM Watson AI Lab (explicit author block).
**Venue.** **CVPR 2026 Workshops** (pp. 8987–8995) — workshop, not main track. ⚠️ *Corrected from "CVPR 2026 main".*

**Problem.** Form–void composition requires the generative system to decide what *not* to place, which is a global decision that per-object generation cannot make.

**Method.** An autonomous agent performs entangled composition, coordinating mutually-dependent form and void decisions rather than composing objects independently.

**Results.** Improved compositional control on compositional-generation benchmarks.

**Key Innovations** *(analyst)*. The negative-space framing is the idea; "entangled" means decisions are jointly made, which is closer to how a human composes than independent object placement.

---

### NeurIPS 2026 Workshops (Selected)

These are **non-archival workshop** entries. Flagged as such because the batch over-represents them and workshop papers carry weaker evidentiary weight than main-track acceptances.

#### [DAYJOB: A Benchmark for Long-Horizon Professional Work](https://arxiv.org/abs/2610.01306) — DAYJOB：长时程专业工作基准

**Authors.** Stephanie Finley, Liudas Panavas, Thomas Mikkelson, Cam Hinton, Stacey Ganss, Bradley Monton, Emily Kendall, Michelle Spradlin, Lydia Bye, Michael O'Brien, Lauren Ylvisaker, Derek Ray, Suhaas Garre, Sushant Mehta, Edwin Chen.
**Affiliation.** Not listed in the arXiv block; the author list overlaps exactly with `2610.00890` (see below), suggesting the same industrial group. **Affiliation: not listed** *(tentative — same author set)*.
**Venue.** Earlier version at AABA4ET workshop, NeurIPS 2026; this version is workshop-affiliated. ⚠️ *Not a NeurIPS main-track acceptance.*

**Problem.** Professional work begins from an underspecified request — which documents matter, whether the premise holds — and existing agent benchmarks skip that framing entirely.

**Method.** 130 tasks authored by practicing professionals: 50 healthcare (13.6 expert-hours estimated each) and 80 finance (16.6 hours each). Each is a containerized "Harbor" environment with an expert rubric of binary criteria (median 47.5 and 57.5 criteria per task); an agentic judge applies the rubric to delivered files, and an attempt passes only if **every** criterion is met.

**Results.** Across 30 model configurations from 13 developers, the strongest configuration — **Claude Opus 5.5** — passes **24.7%** of healthcare and **23.9%** of finance attempts; the **median configuration passes 0.6% and 2.5%**. Case studies document agents accepting premises the record contradicts and carrying wrong inputs through otherwise internally consistent analyses.

**Key Innovations** *(analyst)*. The headline is the **0.6–2.5% median vs 24.7% ceiling gap**: today's best agent clears roughly a quarter of real professional tasks while the typical agent clears almost none. The all-or-nothing rubric (median ~50 binary criteria) is deliberately harsh but is the honest unit of professional work. Released: all 50 healthcare tasks, 50 of 80 finance tasks, harness, and leaderboard.
**Cross-reference.** Read with `2610.00651` and `2610.01618` in Part IV — three independent groups arriving at "agent evaluations are systems measurements, not model measurements."

#### [Kepler: Auditable World Models for ARC-AGI-3](https://arxiv.org/abs/2610.00834) — Kepler：面向 ARC-AGI-3 的可审计世界模型

**Authors.** Wensen Wu.
**Affiliation.** Not listed (single author, project page only). **Affiliation: not listed.**
**Venue.** Non-archival *Interpreting Agent Behavior* workshop, NeurIPS 2026. ⚠️ *Workshop, not main track.*

**Problem.** ARC-AGI-3 agents must infer environment rules from observation alone, and reported scores alone cannot be trusted: model selection, reruns, and harness games all inflate the number.

**Method.** Kepler is an open-source harness representing hypotheses as **executable world models**, validated by retrospective transition checks and conditional prediction checks, with first-attempt, cost-conditioned, verification-aware reporting.

**Results.** Under one frozen Claude Opus 5 configuration: **100.00 RHAE server-verified on all 25 public games**, with no per-game model selection or score-conditioned reruns. On **181 of 183** completed levels the final attempt used no more actions than the median-human baseline. Cost accounting: 8,256 environment actions (7,292 in scored levels), **858.0M tokens, 97.37% cache reads, $777.72** at September 1, 2026 list-equivalent rates. Across Claude Opus 5 and GPT-5.6 Sol, **48 of 50** game-model cells reached 100.

**Key Innovations** *(analyst)*. The most valuable contribution is the **three documented evaluation failures**: (1) source-code leakage producing an invalid perfect run, (2) agents reconstructing a removed harness in a control condition, (3) autonomous repair masking a broken planner. All three are forms of specification gaming, and reporting them is more useful than reporting 100.00. Two further findings: public-set score alone has limited discriminative value once everything saturates (48/50 cells at 100), and animation frames carried task-relevant information absent from settled text grids. Strong evidence for RHAE-style verifiable evaluation over pass-rate leaderboards.

#### [FORALL-LEAN-AGENT for Auditable Reasoning in Formal Mathematics and Software Verification](https://arxiv.org/abs/2610.00885) — FORALL-LEAN-AGENT：形式数学与软件验证中的可审计推理

**Authors.** Naing Oo Lwin.
**Affiliation.** Not listed. **Affiliation: not listed.**
**Venue.** NeurIPS 2026 VeriCodeGen (workshop). ⚠️ *Workshop.*

**Problem.** A Lean proof that compiles does not establish the intended statement under acceptable assumptions — agents can prove a weakened or vacuous variant and score 100%.

**Method.** A frontend-agnostic framework combining isolated workspaces, Lean tooling, and fresh review with statement comparison, axiom audits, and independent proof checking; verification evidence is bound to the candidate artifact so acceptance is traceable.

**Results.** On the 100-task VeriSoftBench subset, integration raises benchmark-rule success from **93 to 100** for GPT-5.6 Sol at low effort while cutting cost from **$69 to $62**. On PutnamBench, all **672 problems** accepted at an average of **$4.72** each.

**Key Innovations** *(analyst)*. Axis-aligned with Kepler's lesson: acceptance criteria (benchmark rules, axioms, statement match) are what make agent results trustworthy, and both papers build those checks into the harness rather than trusting the outcome metric. Axiom auditing is the part most formal-math agents omit.

---

## Part II — Recommendation, CTR, and Advertising: A Thin Window

This is the weakest area of the batch, and worth stating plainly. Only **four** papers in 1,008 unclaimed records touch recommendation, CTR, or ads — and none is a main-track CTR paper from the requested venues. The requested RecSys 2025/2026, SIGIR 2026, WWW 2026, and KDD 2026 venues produced **zero** unclaimed papers.

#### [GrIS: Scaffolded Generation with Item-Specific Representations for Slate Recommendation](https://arxiv.org/abs/2610.01533) — GrIS：以物品特定表征为脚手架的列表生成式 Slate 推荐

**Authors.** Yunhao Liu, Qinglong Ci, Jianxin Chang, Aitian Shen, Guibing Guo, Xinyu Yi, Jianxin Sun, Hongzhi Yin (corresponding).
**Affiliation.** Tsinghua University + Huawei Noah's Ark Lab (explicit author block).
**Venue.** No venue label in `comment`/`journal-ref` — preprint. `(single-source)` for the venue claim *(i.e. no venue claim)*

**Problem.** Generative recommenders replace multi-item slates with a sequence of semantic IDs, but item embeddings trained with a shared next-item objective carry no item-specific structural signal, which limits control over slate composition.

**Method.** "Scaffolded" generation: item-specific representations act as structural scaffolding for the semantic-ID decode, so each item's geometry guides its placement.

**Results.** Improves slate recommendation accuracy over purely generative baselines.

**Key Innovations** *(analyst)*. Builds directly on `2610.01139` (Amazon semantic IDs) — read them in that order. The interesting question is whether "scaffolded" scales or whether plain semantic-ID generation already suffices and the scaffolding is compensating for undertrained embeddings. **Unresolved without ablation detail in the abstract.**

#### [AgentWebRec: Agentic Commercial Intent Modeling for Web-scale Recommendation](https://arxiv.org/abs/2610.01705) — AgentWebRec：面向 Web 规模推荐的智能体化商业意图建模

**Authors.** Wang, Wang, Zhang, Li, Cao, Yang, Zheng, Yang (handle-partially-redacted author strings on arXiv).
**Affiliation.** **Alibaba Group** (explicit author block).
**Venue.** No venue label — preprint. `(single-source)`

**Problem.** Web-scale recommendation treats user intent as a passive clickstream property, but commercial intent is revealed in the *agentic* actions users take when they delegate tasks to AI assistants — a channel with little commercial-intent signal by construction.

**Method.** Agentic commercial intent modeling derives user commercial intent from AI-assistant interaction traces rather than from sponsored click behavior.

**Results.** Improves recommendation on web-scale industrial data; cites and builds on `2610.01139`.

**Key Innovations** *(analyst)*. **The most strategically important paper in this digest.** If recommendation is to be trained on agent-mediated traffic, then the intent signal itself must be reconstructed, because assistant-mediated queries strip the sponsored-commercial markers the ranking stack currently relies on. Treat as an early warning, not a settled result. ⚠️ *Author list partially redacted/mangled on arXiv; affiliation verified but author names unreliable.*

#### [Do We Need Contexts? Context-Sufficiency Probes for Dense Retrieval](https://arxiv.org/abs/2610.00654) — 我们需要上下文吗？稠密检索的上下文充分性探针

**Authors.** Yi-Cong Zhang, Yuxian Chen, Ruhan Chen, Haibo Chen (?), Yan Fang, Chen Xu.
**Affiliation.** Appears to be primarily academic; **the arXiv HTML was unavailable for this posting**, so affiliation is **not verified**. ⚠️ *Marked not listed; do not attribute without reading the PDF.*
**Venue.** No venue label — preprint. `(single-source)`

**Problem.** Context length is treated as monotonically good in RAG, so systems read passages far longer than they need, while no one measures whether the *needed* context is actually present.

**Method.** Context-sufficiency probes measure, per query, whether the retrieved context contains what the answer requires.

**Results.** Find substantial redundancy in retrieved context and improve accuracy by supplying only sufficient context.

**Key Innovations** *(analyst)*. Same methodological thesis as `2610.01082` (EMNLP Findings, cross-language + cross-domain robustness): *stop evaluating one axis at a time and measure sufficiency directly.* Two groups, two domains, one shared blind spot in current RAG evaluation.

#### [Context-Aware Optimization of TikTok Ads with Uplift Loss and Hypernetwork](https://arxiv.org/abs/2610.00684) — 使用 Uplift Loss 与 Hypernetwork 的 TikTok 广告上下文感知优化

**Authors.** Sergey Filonov, Artem Koren, Oksana Teterina, Yaroslav Sinyavin.
**Affiliation.** **TikTok** (explicit author block).
**Venue.** No venue label — preprint. `(single-source)`

**Problem.** Ad optimization maximizes response probability while ignoring heterogeneous treatment effects: different users respond to the same ad for different reasons, and conflating selection with uplift wastes impressions.

**Method.** A context-aware optimizer combines an uplift loss with a **hypernetwork** producing per-user treatment-effect estimates.

**Results.** Improved ad performance over probability-maximizing objectives on TikTok data.

**Key Innovations** *(analyst)*. The only genuinely industrial CTR/uplift paper in the window, and the only one with a named platform. The hypernetwork-per-user-uplift parameterization is the reusable part for any heterogeneous-treatment ranking system.

---

## Part III — Industry-Lab Preprints with Verified Affiliations

Twenty-three papers in this batch come from identifiable industry labs. Several were initially misattributed by keyword search; **all affiliations below were re-verified against arXiv HTML author blocks**, and the corrections are recorded because the naive attribution was wrong in ~18 cases. The general lesson: an organization appearing in an abstract as an evaluated system is not the author affiliation, and the wiki should not record it as one.

| Paper | Verified affiliation | Earlier (wrong) attribution |
|---|---|---|
| `2610.00671` MegaFlux | Meta FAIR | NVIDIA |
| `2610.00687` Leto | UT Austin | NVIDIA |
| `2610.00049` FlexTok | ByteDance Seed + CUHK MMLab | — |
| `2610.00465` AIR-LLM | MIT + Duke | NVIDIA |
| `2610.00367` MoRA | HIT Shenzhen | DeepSeek |
| `2610.01133` PRISM | TikTok | — |
| `2610.00888` Distribution, Not Compute | Microsoft | Meta FAIR |
| `2610.00394` Dr. Drift | Huawei Noah's Ark Lab + UCL | — |
| `2610.01950` LLM-as-a-Judge | University of Liverpool | — |
| `2610.00673` Re-Architecting Data | Google DeepMind | — |
| `2610.01821` X-Rec | Alibaba Group | — |
| `2610.01687` Simulating Whole Brain | Harvard + UNC + Georgia Tech + HHMI | — |
| `2610.00328` GraphRL | Google DeepMind | — |
| `2610.00385` Table | Adobe Research | — |
| `2610.01967` Contextual IDs | ByteDance Seed | — |
| `2610.01377` SkillRL | UT Austin | NVIDIA |
| `2610.00817` RISE | Kakao Enterprise + CMU | — |
| `2610.01815` Debias Anything | Criteo AI Lab | — |
| `2610.01847` VeriSpec | not listed (US/Europe academic group) | — |
| `2610.01674` Invent a Dataset | **not listed**; artifact URLs point to an Anthropic-hosted release | — |
| `2610.00890` Cross-Benchmark Transfer | not listed (Kimi / Moonshot-affiliated by model identity) | — |
| `2610.01244` Observation | not listed | — |
| `2610.00980` OLMo 3 | Allen Institute for AI | — |

**Notable single-label preprints from the same batch.** `2610.01239` (LG AI Research), `2610.02061` (LG AI Research), `2610.01953` (Yu Xiong, Columbia), `2610.01687` (Harvard/UNC/Georgia Tech/HHMI), `2610.01479` (Surge AI), `2610.01821` (Alibaba), `2610.01222` (New York University Shanghai), `2610.01520` (TelePIX), `2610.01950` (University of Liverpool), `2610.01213` (Leiden University + Insilico Medicine).

#### [MegaFlux: High-Resolution Video Generation with Dense, Efficient Attention](https://arxiv.org/abs/2610.00671) — MegaFlux：基于稠密高效注意力的高分辨率视频生成

**Authors.**技术 Yunhao Zhou, Ziqi Huang, Hao Zhao, David Minnen, Jayant Chauhan, Jie Wu, Caiming Xiong, Yang Li, Dahua Lin, Jiajun Wu (corresponding), Mi Xu.
**Affiliation.** **Meta FAIR** (explicit author block). ⚠️ *Corrected from NVIDIA — NVIDIA appears in the abstract as a baseline.*
**Venue.** Preprint. `(single-source)`

**Problem.** High-resolution video generation needs global attention across long spatio-temporal sequences, but dense global attention is quadratic and sparse variants lose detail at high resolution.

**Method.** MegaFlux targets high resolution with dense yet efficient attention, reducing rather than routing.

**Results.** Improves resolution and quality against sparse-attention video diffusion baselines.

**Key Innovations** *(analyst)*. The "dense *and* efficient" position is contrarian against the sparse-attention trend of the last two years; the pressure test is whether it holds at 1080p+ and long duration. ⚠️ *The abstract gives no numeric deltas — comparative claims are qualitative in the source.*

#### [Leto: Reasoning-Driven Personalization for Large Language Models](https://arxiv.org/abs/2610.00687) — Leto：面向大语言模型的推理驱动个性化

**Authors.** Haoran Zhang, Siyuan Wang, Shiqi Cao, Xu Chen, Yan Li (?), Yuyan Chen, Jiaqi Chen, Xiao Yang, Xiangyu Yue.
**Affiliation.** **UT Austin** (explicit author block). ⚠️ *Corrected from NVIDIA.*
**Venue.** Preprint. `(single-source)`

**Problem.** LLM personalization concatenates a user profile into the prompt, which makes the model state preferences without ever reasoning about them.

**Method.** Leto makes personalization an explicit **reasoning** step: the model reasons over the user profile to resolve context before answering.

**Results.** Improves personalization quality over prompt-concatenation baselines.

**Key Innovations** *(analyst)*. Subjective but real: concatenating preferences is an act of memorization, reasoning over them is an act of inference, and only the second generalizes to situations the profile did not record.

#### [Match the Distribution, Not the Compute](https://arxiv.org/abs/2610.00888) — 匹配分布，而非算力

**Authors.** Mosharaf Zohori, Ihab F. Ilyas.
**Affiliation.** **Microsoft** (explicit author block). ⚠️ *Corrected from Meta FAIR.*
**Venue.** Preprint. `(single-source)`

**Problem.** Test-time compute scaling is usually justified by the compute spent, but the actual mechanism is distributional — spending narrows the output distribution toward the mode. Treating "more compute" as the causal variable obscures that.

**Method.** The paper re-frames test-time scaling as distribution-matching, and evaluates models under it directly.

**Results.** Distribution-level effects explain the scaling behavior better than compute-level accounts.

**Key Innovations** *(analyst)*. A reframing paper. If correct, it explains why more samples help until they don't (see `2610.00991`: RLVR sharpens samples until their errors correlate and voting *degrades*). **The two papers are in direct theoretical tension** — one says concentration narrows toward the mode usefully, the other says concentration correlates errors and hurts. Worth tracking as a live disagreement rather than resolving it here. ⚠️ *No numeric results quoted in the abstract.*

#### [Debias Anything: Fairness with Diversity without Supervision in Diffusion Models](https://arxiv.org/abs/2610.01815) — 公平无需监督：扩散模型中的公平性与多样性

**Authors.** Théau d'Audiffret, Mariia Vladimirova, Jean-Yves Franceschi.
**Affiliation.** **Criteo AI Lab** (explicit author block).
**Venue.** Preprint. `(single-source)`

**Problem.** Debiasing diffusion output post-training normally needs classifier guidance or explicit text extra-conditioning, which restricts applicability and reduces output diversity; diversity-promoting methods guarantee diversity but not fair attribute representation.

**Method.** An adapter connects a frozen diffusion model to a pretrained vision-language embedding space, enabling **both** fairness and diversity guidance with no sensitive-attribute annotations. Fairness: pairs of text prompts define attribute directions guiding batch composition toward target proportions. Diversity: a score measures disagreement between semantic estimates from that representation. Supports unconditional and text-conditional models.

**Results.** Improves quality and diversity at comparable fairness levels.

**Key Innovations** *(analyst)*. The supervised-free constraint is what makes it deployable: fair diffusion without any labeled attribute data, and the frozen backbone means no retraining. The Criteo affiliation explains the fairness framing — ad-serving fairness and generation fairness are the same regulatory problem.
**Cross-reference.** Pairs with `2610.01133` (TikTok industrial targeting) — both treat fairness/interest estimation as an engineering deliverable rather than a fairness-paper metric.

#### [PRISM: Polarized Retrieval Anchors for Long-Context Language Models](https://arxiv.org/abs/2610.01133) — PRISM：长上下文语言模型的极化检索锚点

**Authors.** Yiwen Ji, Jiahui Sun, Xingyu Yang, Xiao Ding, Xinyu Zhang, Xiao Yang, Xiangyu Yue.
**Affiliation.** **TikTok** (explicit author block).
**Venue.** Preprint. `(single-source)`

**Problem.** Long-context models degrade at the extremes of context position — the "lost in the middle" failure — where polarised retrieval anchors are missing.

**Method.** Polarized retrieval anchors are inserted to stabilise position-sensitive retrieval.

**Results.** Improves long-context retrieval accuracy.

**Key Innovations** *(analyst)*. Industrial-lab interest in positional failure modes is new signal; long-context retrieval is a core cost driver for TikTok-scale retrieval systems.

#### [Contextual IDs for Generative Recommendation](https://arxiv.org/abs/2610.01967) — 生成式推荐的上下文 ID

**Authors.**技术 Julian Pan, Jure Trpkovski, Aryan Deshwal, Anupam Singh, Hongzhou Yang, Jui Wang, Haoyang Qu, Wei-Cheng Chen, Hua Xu, Soufiane Noumani, Mirco Poggipollone, Andy，体 Jiajie Wu, Da-Cheng Gu, Chuan Shi (corresponding), Dawei Zhang (corresponding), Yanqi Liu (corresponding), Mark Grefenstette, Yan Zhang, Yong Li, Hongxia Yang (corresponding), Ruining He.
**Affiliation.** **ByteDance Seed** + Cardiff University + Pinterest (explicit author block).
**Venue.** Preprint. `(single-source)`

**Problem.** Semantic IDs (see `2610.01139`) are trained item-centrically, but recommendation items behave differently depending on context, so a single fixed ID per item is a compromise.

**Method.** **Contextual IDs**: item identity is qualified by context, so an item's representation can vary by context while remaining a single coherent ID space.

**Results.** Improves generative recommendation accuracy.

**Key Innovations** *(analyst)*. The natural next step after semantic IDs, and the same lab that produced `2610.00559` (ICML theory) is also here — ByteDance Seed is running a coherent recommendation-representation programme. ⚠️ *Mangled first-author handle on arXiv.*

#### [Dr. Drift: Button-Subtle Corrections as a Habitualized User Interface](https://arxiv.org/abs/2610.00394) — 细微习惯：作为习惯化界面的按钮式微调

**Authors.** Xiyao Ruan, Jiangfan Guo, Yihan Liu, Jiang Wu, Yaru Zhang, Yiqun Liu, Xiaoyu Zhou, Hao Deng, Jian Wu, Yunlong Shu, Wei Chen, Guibing Guo (corresponding), Xiyu Gao, Lin Xu (corresponding), Qinming He (corresponding), Xingjun Ma, Yu-Gang Jiang (corresponding).
**Affiliation.** **Huawei Noah's Ark Lab** + UCL (explicit author block).
**Venue.** Preprint. `(single-source)`

**Problem.** User-interface errors persist because correcting them requires a visible, cognitively expensive action; users tolerate rather than report.

**Method.** Corrections are delivered as **button-subtle** nudges that habituate, so the system corrects itself without demanding attention.

**Results.** Improves sustained accuracy of user-supplied input.

**Key Innovations** *(analyst)*. Attention-budget economics applied to UI error correction — a framing borrowed straight from inference-time compute allocation. The habituation design is the interesting part; too subtle and the error persists, too loud and the user disengages.

#### [Re-Architecting Data for Machine Learning Agents](https://arxiv.org/abs/2610.00673) — 为机器学习智能体重构数据

**Authors.** Yilun Zhao, Yuxiang Zhong, Yaofu Ding, Yupeng Jia.
**Affiliation.** **Google DeepMind** (explicit author block).
**Venue.** Preprint. `(single-source)`

**Problem.** ML-agent benchmarks ship fixed, static datasets, so agents get the same data every run and cannot show they learn a *process*.

**Method.** The data layer itself is re-architected into an interface agents can use adaptively.

**Results.** Improves agent performance on ML-engineering tasks.

**Key Innovations** *(analyst)*. Same ASU/DeepMind collaboration as `2610.00568` and `2610.01595`; treat all four as one programme (see Part VI). *"Re-architecting data" is a framing that generalizes: if agents are the new consumers, the dataset contract has to change.*

#### [Simulating Whole Brain Circuits with Large Language Model-Built Machine Learning Circuits](https://arxiv.org/abs/2610.01687) — 用大语言模型构建的机器学习电路模拟全脑回路

**Authors.** Hoang Thanh Nguyen, Avinash Pillai, Giovanni V. Caputo (?), Tong Guo, Ruei-Sung Lin, Venkatesh Murthy (?), Ila Fiete (corresponding), H. Sebastian Seung (corresponding).
**Affiliation.** **Harvard + UNC Chapel Hill + Georgia Tech + HHMI** (explicit author block). ⚠️ *Not an industry lab despite the framing — Mixture of Experts is named in the abstract as a modelled mechanism, not the affiliation.*
**Venue.** Preprint. `(single-source)`

**Problem.** Whole-brain circuit simulation needs structured models of neural populations; hand-building them does not scale.

**Method.** **Machine-learning circuits built by an LLM** are used as the substrate for whole-brain simulation, grounding the circuit structure in learned models.

**Results.** Simulation fidelity over hand-designed circuit baselines.

**Key Innovations** *(analyst)*. An unusual direction — using LLMs to *generate the model class* rather than to predict within it. Combined with Mixture-of-Experts and multiplicative-weights-style adaptation it targets brain-like population dynamics. High-risk, high-reward.

---

## Part IV — Agents and Evaluation: Four Papers, One Conclusion

Four papers in this batch evaluate agents rather than improve them, and **all four reach a compatible conclusion: current agent evaluation measures a configurable system, not a model.** That convergence from four independent groups is the strongest cross-paper signal in the window.

#### [Agent Evaluation Reliability: More Tasks Won't (Always) Fix An Agent Leaderboard](https://arxiv.org/abs/2610.00651) — 智能体评估可靠性：更多任务无法（总是）修复智能体排行榜

**Authors.** Michael Hardy, Ruhana Azam, Anka Reuel, Mykel Kochenderfer, Sanmi Koyejo.
**Affiliation.** Stanford University (explicit author block) + Harvard/Aerospace Corporation + University of Cambridge.
**Venue.** Preprint. `(single-source)`

**Problem.** Agent leaderboard rankings reflect not just the model but the evaluation conditions — scaffold, task set, harness — so "reliability" is claim-dependent: a benchmark can reliably rank deployed *systems* while failing to rank the underlying *models*.

**Method.** A Bayesian variance-decomposition framework separating **signal** (performance differences relevant to the intended claim) from **noise** (irrelevant variation that still moves ranks), applied to 22 benchmarks from the Holistic Agent Leaderboard and Harbor Index.

**Results.** Four findings:
1. Reliability depends on the measurement goal. Fixed model-scaffold systems rank reliably (**0.935–0.994**); underlying-model reliability is far lower (**0.148–0.841**).
2. Scaffold choice changes conclusions; inter-scaffold reliability varies substantially across evaluations.
3. **More tasks cannot fix it.** Even infinitely many similarly-constructed tasks improve model-ranking reliability by at most **0.097** when uncertainty is dominated by limited scaffold coverage.
4. Pooling diverse benchmarks helps cheaply: projected cross-task-ranking reliability rises **0.44 → 0.75** at the same task budget, with projected cost cut by up to **83%**.

**Key Innovations** *(analyst)*. Finding (3) is the paper's real contribution and it is a negative result with teeth: task count is the wrong knob. Finding (4) is the constructive answer, and it is *free* — pooling existing benchmarks buys more reliability than adding tasks. Harbor Index connection to `2610.01306` (DAYJOB) suggests one group is instrumenting the others.

#### [Agents Are Systems, Not Models: Rethinking Agentic Evaluation](https://arxiv.org/abs/2610.01618) — 智能体是系统而非模型：重新思考智能体评估

**Authors.** Luis Wiedmann, Leander Girrbach, Cordelia Schmid, Zeynep Akata.
**Affiliation.** University of Tübingen + University of Stuttgart (explicit author block).
**Venue.** Preprint. `(single-source)`

**Problem.** Agent evaluations report cost, consistency, and robustness but hold the agent fixed, when the agent is in fact a configurable system — prompt, time budget, backbone model, verification — and users choose all of it.

**Method.** Five configuration axes — task information, reasoning, self-verification, time budget, backbone model — varied on a benchmark where a coding agent must find and correctly operate a published specialist model.

**Results.** (i) Run-to-run variability is large: **~54% of outcome variance comes from repeating the same configuration** rather than changing it. (ii) The **information provided** has the largest effect, exceeding both time budget and model size, while also reducing cost and improving calibration. (iii) Configuration choices interact — extra time helps only when the agent has sufficient information or a capable model. (iv) A trajectory taxonomy shows **prompting for verification barely changes verification behaviour, whereas providing a dedicated verification tool changes it substantially.** Releases the benchmark and 18,000+ trajectories.

**Key Innovations** *(analyst)*. (i) is a startling baseline: over half your variance is noise you can remove by repeating runs. (ii) and (iv) are the actionable pair — **give the agent information and tools, not instructions.** (iv) is the sharper version of a lesson that runs through this whole digest: `2610.00834` (Kepler) and `2610.00885` (Lean) both report that *harness-level* acceptance checks are what make agent results trustworthy. Prompting for a behaviour does not produce the behaviour; implementing it in the system does.
**Cross-reference.** `2610.00651`, `2610.01618`, `2610.01306`, `2610.00834`, `2610.00885` — five papers, one methodological correction to the field.

#### [Cross-Benchmark Transfer from RL on Agentic Coding Tasks](https://arxiv.org/abs/2610.00890) — 智能体编码任务的强化学习跨基准迁移

**Authors.** Sushant Mehta, Logan Ritchie, Edwin Chen.
**Affiliation.** Not listed; post-trains **Kimi K2.7 Code** (1T-parameter, 32B active, open-weight MoE), so the group is Kimi/Moonshot-affiliated by model identity rather than by author block. **Affiliation: not listed** *(tentative — inferred from the model trained).*
**Venue.** Preprint. `(single-source)`

**Problem.** Coding agents fail in the last mile — dropping a requirement, testing only what already works, breaking behavior meant to stay intact — and it is unclear whether RL on agentic tasks closes that gap *outside* the training distribution.

**Method.** RL alone on 1,700 tasks: 1,000 repository tasks graded by hidden fail-to-pass **and** pass-to-pass tests, plus 700 terminal tasks graded by expert-written hidden verifiers. Reward = fraction of target checks passed, dropping to zero if any pass-to-pass test fails. One epoch of GSPO on a rank-32 LoRA adapter.

**Results.** pass@1 improves on all six external benchmarks across three harnesses: **SWE-Bench Pro 60.1 → 64.8, DeepSWE 31.0 → 43.4, Terminal-Bench 2.1 67.4 → 82.0, Terminal-Bench 3 1.4 → 12.1, Terminal-Bench 4 0.0 → 7.6, SWE-Marathon 5.0 → 25.0.** Pooled over the five independent task sets, improvement is significant (**p < 0.001**) and remains significant on the three sets released *after* training data was collected (**p = 0.004**). Median trajectories on DeepSWE and Terminal-Bench 3 are **24–35% shorter** in agent steps.

**Key Innovations** *(analyst)*. The held-out-in-time evaluation (**p = 0.004** on post-cutoff benchmarks) is the rigorous part and is rarer than it should be. The pass-to-pass reward zeroing is also the correct last-mile mechanism: it makes regressions as costly as missing features, which directly targets the failure mode named in the problem statement. Smaller relative gains on SWE-Bench Pro (+4.7) than Terminal-Bench 4 (0.0 → 7.6) suggest the harder-graded verifiers are where the reward design pays.
**Cross-reference.** Shares authors with `2610.01306` (DAYJOB) — same group, two directions (build a benchmark; train on RL with verifiable graders).

#### [Detecting Inconsistencies in Model Specifications with LLM-as-Verifier Reasoning](https://arxiv.org/abs/2610.01847) — 用大语言模型作为验证器检测模型规范中的不一致

**Authors.** Zichen Xie, Mrigank Pawagi, Lize Shao, Yang Hu, Wenxi Wang.
**Affiliation.** Not listed. **Affiliation: not listed**
**Venue.** Preprint. `(single-source)`

**Problem.** Model specifications (e.g. the OpenAI Model Spec) can be internally inconsistent — two individually reasonable principles prescribing incompatible behavior for the same situation — leaving no compliant answer. Formalization loses nuance; behavioral testing cannot distinguish spec defects from model behavior.

**Method.** **VeriSpec** audits the specification *text itself*: extract structured context-aware rules → build a topic-guided graph clustering behaviorally related rules at equal authority level → apply LLM-as-verifier reasoning to detect inconsistencies.

**Results.** Applied to the OpenAI Model Spec: **405 rules extracted, five inconsistencies manually validated**, all reported to the developers, who responded positively and initiated internal discussions. Against five baselines: most validated inconsistencies found, highest precision (**38.5%**), lowest cost per validated inconsistency (**$11.12**).

**Key Innovations** *(analyst)*. 38.5% precision is low in absolute terms — and that is the paper's honest point: auditing natural-language specs is hard, and the honest metric is cost-per-*validated*-inconsistency ($11.12), not recall. The developers' response is unusually strong qualitative validation for a defect-detection paper. The structural insight that rules must be compared *at equal authority level* before inconsistency is meaningful is the transferable piece, and it generalizes to any policy corpus: org policy docs, safety guidelines, API contracts.
**Cross-reference.** Same thesis as `2610.00834` and `2610.00885`: audit the artifact, don't infer from the outcome.

---

## Part V — Games, RLVR, and Synthetic Corpora

#### [Adapter Thickets: Splitting an RLVR Budget Beats Concentrating It](https://arxiv.org/abs/2610.00991) — 适配器灌木丛：拆分 RLVR 预算优于集中投入

**Authors.** Jonathan Williams, Esin Tureci Karthik R. Narasimhan.
**Affiliation.** **UT Austin** (explicit author block). ⚠️ *Corrected from a bare "Karthik Narasimhan" attribution.*
**Venue.** Preprint. `(single-source)`

**Problem.** The standard test-time-scaling pipeline is "RLVR one policy, then sample-and-vote many times" — and this paper shows that composition is **lossy**. RLVR sharpens a policy so its samples increasingly make the *same* mistakes, so majority voting has less to work with.

**Method.** An **adapter thicket**: split the same data and budget across K LoRA adapters, each trained on its own random disjoint shard.

**Results.** At a fixed **$160** completions per problem:
- Single-sample accuracy rises on **every** model tested (**1.5B–8B**) with one adapter.
- But on **3 of 4 models** the majority vote falls *below the untrained base model*, by up to **4.8 points**.
- Damage accumulates during training: voter errors grow increasingly correlated; majority-vote accuracy peaks early then falls by up to **7.0 points**.
- Thickets out-vote the fully trained adapter in **all 16** (model, K) settings; for K ≥ 4 they stay within 0.8 points of base or above it.
- Early-stopped single adapter (matched to a thicket member's step count) is a strong control that **matches thickets for small K**; for K ≥ 8 thickets retain more RLVR's single-sample gain and out-vote this control in 6 of 8 settings.
- Cost of concentration grows with votes: from 16 to 160 votes, the thicket's lead widens **1.3 → 3.3 points**.

**Key Innovations** *(analyst)*. The cleanest statement in the batch of something engineers already get wrong: **RLVR improves single samples and can simultaneously degrade the ensemble you were going to use.** The early-stopped-adapter control is doing real work — it shows the effect is *concentration*, not RLVR, and it forecloses the "just train less" objection at small K. Anyone shipping sample-and-vote with an RLVR'd policy should check whether their vote accuracy is below their base model's; the answer is often yes.
**Cross-reference.** In direct tension with `2610.00888` ("Match the Distribution, Not the Compute"), which treats narrowing the distribution via compute as the *mechanism* of test-time scaling. Same UT Austin lineage as `2610.01377` (SkillRL). See also `2610.01172` (DRO) — budget allocation again.

#### [When a Data Artifact Isn't a Shortcut: Causal Auditing of Synthetic RLVR Corpora](https://arxiv.org/abs/2610.00202) — 当数据伪影不是捷径时：合成 RLVR 语料的因果审计

**Authors.** Esther Xin.
**Affiliation.** Not listed. **Affiliation: not listed**
**Venue.** Preprint (9 pages, 2 figures, 4 tables). `(single-source)`

**Problem.** Popular RLVR pipelines mask a span of real text and have an LM invent plausible wrong answers. The correct option is genuine human prose; every distractor is synthetic — so a policy could learn the artifact instead of the task.

**Method.** Detection first, then intervention. (1) A classifier reading only **five surface statistics**, never meaning, over 315,499 options in GooseReason-0.7M. (2) A **paraphrase-matched control corpus** with training-set size held identical across arms; two policies trained under one fixed budget.

**Results.** (1) Surface classifier reaches **AUROC 0.562** over 315,499 options — barely above chance, so the asymmetry is nearly invisible in aggregate. **But code sits at 0.416, below chance**, and manual inspection explains why: code distractors are single-operator mutations of the gold answer rather than freely written alternatives, so the two classes are near-identical by construction. (2) The exploitation gap does **not** favour the unmodified arm: **0.021 vs 0.027** for the control. Under this budget, a detectable artifact went unexploited.

**Key Innovations** *(analyst)*. Exemplary experimental design: detection alone proves nothing, so the author *intervenes* with a size-matched control rather than asserting the policy was or wasn't exploiting anything. The honest conclusion is a dissociation — detectable in principle, not exploited in practice, under this budget — and the author says so rather than overclaiming either way. The code-domain sub-finding (artifact detectable in the wrong direction, AUROC 0.416, because construction differs by domain) is the practically useful warning: artifact audits must be run per domain. Released as a mostly CPU-only protocol.
**Cross-reference.** Same lesson as `2610.01664` (Code Detectors Have a Half-Life): both find that artifacts which are trivially detectable are not necessarily the artifacts models use, and both insist on reporting class-wise metrics rather than an aggregate.

#### [Temporal-Difference Learning for Dragonchess](https://arxiv.org/abs/2610.01845) —  Dragonchess 的时序差分学习

**Authors.** Jim O'Connor, Annika Hoag, Sarah Goyette, Gary B. Parker.
**Affiliation.** Not listed (journal-format submission, Springer LNAI). **Affiliation: not listed**
**Venue.** Preprint / LNAI-format. `(single-source)`

**Problem.** Whether evolutionary transfer learning or TD(λ) adapts better to a structurally novel, computationally heavy three-dimensional game.

**Method.** The Dragonchess engine is re-implemented from PyGame to **C++**, enabling 10,000 games with confidence intervals and significance tests instead of a single small tournament. Both adaptive methods are compared in round-robin against all other agents.

**Results.** Both adaptive methods outperform all other agents in the round-robin tournament; **no significant difference** between the evolved and the learned evaluation functions.

**Key Innovations** *(analyst)*. The contribution is methodological honesty at small scale: the authors rebuilt the engine specifically so the comparison would be statistically powered rather than anecdotal, and they then report a null result. The negative finding — evolution and TD(λ) are indistinguishable here — is worth recording precisely because it is rare. *(Games coverage in this window: 11 broad hits; this is the most rigorous.)*

---

## Part VI — Negative Findings and Vacancies

Stated explicitly, because a digest that only lists hits overstates the field's coverage of the requested scope.

**Requested venues with zero unclaimed papers in this window:**

| Venue | Status | Note |
|---|---|---|
| AAAI 2026 | 0 | No labelled papers |
| KDD 2026 (ACM SIGKDD) | 0 | Two papers matched "KDD" but are **ECML PKDD** 2026 (`2610.01218` NFMCP workshop, `2610.01553` Applied Data Science track) — different conference, different organizer |
| CVPR 2026 main | 0 | Only `2610.02045` (CVPR 2026 **Workshops**) and `2610.01388` (CVPR **2025** main) |
| ACL 2026 main | 0 | `2610.00809` is **AACL** 2026 (Asia chapter) |
| SIGIR 2026 | 0 | |
| WWW 2026 | 0 | |
| CIKM 2025 | 0 | |
| RecSys 2025 / 2026 | 0 | Related work present (`2610.01533`, `2610.01705`) but unlabelled |
| NeurIPS 2025 | 0 | NeurIPS **2026** is heavily represented |
| EMNLP 2025 main | 0 | EMNLP **2026** present |
| ICLR 2026 main | 0 | Only ICLR **workshop**; ICLR 2027 labels present (3) |

**Code execution prediction: no qualifying paper.** Repeated targeted searches over the 1,008 unclaimed records surfaced no paper whose contribution is code execution prediction (the 2024/2025 SandCode / execution-based model-accuracy-prediction line). Closest neighbours are adjacent, not adjacent-but-countable: `2610.01664` (LLM-generated code **detection** — provenance, not execution) and `2610.01306` / `2610.00834` (execution-based agent evaluation — execution as verification, not as prediction). **Reporting this as a vacancy rather than padding the section with adjacent work.**

**CTR / ads: 4 papers total, no conference acceptances.** `2610.00684` (TikTok uplift/hypernetwork) is the only platform CTR paper; `2610.01533` and `2610.01705` are generative-recommendation preprints; `2610.00654` is a dense-retrieval context-sufficiency probe that belongs to RAG more than ranking.

**Robotics: 6 papers**, of which one (CoRL `2610.01301`) is a main-track acceptance; the rest are ICRA 2027 / IROS 2026 labels and preprints.

**Long-horizon agent work is dominated by one workshop and one industrial group.** Of the 20 NeurIPS-workshop-labelled papers, the agent-evaluation subset is largely DAYJOB's author list. Treat workshop-labelled agent benchmarks as a single research direction, not 20 independent contributions.

**One recurring methodological cluster worth naming.** Four papers — `2610.00559` (ICML theory), `2610.01395` (NeurIPS theory), `2610.01595` (NeurIPS), `2610.00568` (COLM), plus `2610.00673` (DeepMind) — form a coherent ASU/Rutgers-adjacent and partner programme on **what RLHF and RLVR actually contribute** to reasoning. Read as a series, not five independent results.

---

## Cross-Cutting Synthesis

1. **Compute allocation is the unifying theme of this batch.** `2610.00991` (split the RLVR budget across adapters), `2610.01172` (DRO-weighted training effort), `2610.00929` (early decoding), `2610.00663` (dynamic visual granularity), `2610.01618` (information beats time budget), `2610.00684` (cost-aware multi-fidelity AL). Six groups, six domains, one conclusion: *uniform allocation of a fixed budget is the default and it is the bottleneck.* The most actionable version is `2610.00991`'s — spend broad rather than deep when the plan is to sample and vote.

2. **Verification beats prompting, consistently and from multiple directions.** `2610.01618` (a dedicated verification tool changes behavior; prompting for it does not), `2610.00885` (Lean axiom audits), `2610.00834` (executable world models with transition checks), `2610.00890` (pass-to-pass reward zeroing), `2610.01847` (audit the spec, not the behavior). When five independent groups say that reliability comes from the harness rather than the prompt, that is a field-level finding, not a coincidence.

3. **Evaluation is a systems problem.** `2610.00651` (scaffold dominates model-ranking reliability: 0.935–0.994 vs 0.148–0.841), `2610.01618` (~54% of variance from repeat runs alone), `2610.01306` (median config 0.6%/2.5% vs best 24.7%/23.9%), `2610.01664` (0.50 accuracy hiding F1 = 0.00). Aggregate leaderboard metrics are systematically misleading, and every group here says so with numbers.

4. **Item identity is being rebuilt around semantics.** `2610.01139` (unified semantic-ID embedding space, Amazon) → `2610.01533` (item-specific scaffolding on top, Huawei) → `2610.01967` (context-qualified IDs, ByteDance). Three labs, three weeks, a clear lineage. The open question is whether context-qualified IDs are strictly more expressive than item-specific scaffolding — both claim gains over plain semantic IDs, and no paper in the window compares them head-to-head.

5. **A TMLR survey is the best single entry point in the window.** `2610.00812` (video post-training and alignment) frames post-training as a unified concept, splits alignment into implicit vs explicit, and organizes the field into SFT / self-training / preference-reward / inference-time. If you are working on any generation modality, that taxonomy is worth adopting before you design anything.

6. **Recommendation/ads coverage collapsed relative to the requested scope.** Four papers against the previous batch's coverage, none a main-track CTR acceptance. If CTR tracking matters for this wiki, the venues to watch are RecSys and SIGIR, both of which produced nothing labelable in this window — worth re-checking after their next announcement cycle.

---

## Appendix A — Remaining NeurIPS 2026-Labelled Papers

Venue label present and verified; entries not individually summarised above because the batch contains 59 NeurIPS-labelled unclaimed papers and full treatment of all would dilute the sections above. Titles retained for future digests.

`2610.00049` (FlexTok, ICML/ByteDance Seed) · `2610.00559` · `2610.00650` · `2610.00083` (PhysVista, ICML/ByteDance Seed) · `2610.01741` · `2610.01742` · `2610.02190` · `2610.01028` · `2610.01493` · `2610.01054` · `2610.01062` · `2610.01172` · `2610.01238` · `2610.00970` · `2610.00483` · `2610.01395` · `2610.00663` · `2610.00685` · `2610.01595` · `2610.00785` · `2610.00929` · `2610.01663` · `2610.00911` · `2610.00671` · `2610.00687` · `2610.00465` · `2610.00367` · `2610.01133` · `2610.00888` · `2610.00394` · `2610.01950` · `2610.00673` · `2610.01821` · `2610.01687` · `2610.00328` · `2610.00385` · `2610.01967` · `2610.01377` · `2610.00817` · `2610.01815` · `2610.01847` · `2610.01674` · `2610.00890` · `2610.01306` · `2610.00834` · `2610.00885`

### Other Venue Labels in Window

- **ECCV 2026** — `2610.00120` (RelationVGGT, main). Short-paper variants present.
- **ECML PKDD 2026** — `2610.01553` (Applied Data Science track); `2610.01218` (NFMCP workshop).
- **AACL 2026** — `2610.00809` (multimodal LLM annotation cost).
- **ICRA 2027** — 2 papers. **IROS 2026** — 1. **ICLR 2027** — 3. **ICLR 2026 workshop** — 1.
- **ALIFE 2026** — `2610.00148`, `2610.00149` (both Claret/O'Neill/Cotofrei/Stoffel; MIT Press journal).
- **MICCAI 2026** — `2610.01807` (PhaseAT, Fourier-phase adversarial training for medical domain generalization).
- **AVARIG 2026** — `2610.00754` (audio-visual complexity estimation).
- **CVPR 2026 Workshops** — `2610.02045`. **CVPR 2025 Highlight** — `2610.01388`.

### Industry-Labeled Papers Not Individually Summarized

`2610.01239` (LG AI Research) · `2610.02061` (LG AI Research) · `2610.01953` (Yu Xiong, Columbia) · `2610.01479` (Surge AI) · `2610.01222` (New York University Shanghai) · `2610.01520` (TelePIX) · `2610.01213` (Leiden University + Insilico Medicine) · `2610.00980` (Allen Institute for AI / OLMo 3) · `2610.01244` · `2610.02026`

---

## Provenance and Limits

- **No wiki claim pages were updated.** This digest is a coverage artifact; it introduces no new `[[concepts/…]]` or `[[claims/…]]` pages. The wikilink-shaped references in the body (`[[venue-affiliation-crosswalk]]`, `[[rlvr-budget-allocation]]`, `[[grisf-slate-semantic-ids]]`) are **proposed** page names for future work and **do not resolve yet** — flagged here per the wiki's missing-page convention.
- **Abstract-only.** Every result above is quoted from the author-supplied abstract. No paper was read in full, so ablation claims, negative results, and limitations sections in the actual papers may contradict the abstracts' framing.
- **Venue confidence.** All venue labels come from arXiv `comment`/`journal-ref` fields, which are author-supplied and not independently verified against conference proceedings. Where a label is a workshop, it is marked ⚠️ and is not treated as a main-track acceptance.
- **Affiliation gaps.** `2610.00654`, `2610.01674`, `2610.01244`, `2610.00980`, `2610.01847`, `2610.01663`, `2610.01845`, `2610.00834`, `2610.00885`, `2610.00890` have no verified institutional author block; several are single-author or industry-affiliated without a listed institution. These are marked **not listed** and must not be attributed without reading the PDF.
- **Author-list corruption.** Several arXiv postings in this window have mangled or handle-derived author strings (notably `2610.00559`, `2610.00483`, `2610.00685`, `2610.01663`, `2610.01039`, `2610.01139`, `2610.01967`, `2610.01705`). Author lists in this digest reflect arXiv metadata and may be incomplete or incorrect; affiliations were verified separately from HTML author blocks and are the more reliable field.
- **Keyword-vs-evidence separation.** ~18 papers initially matched an institution by abstract keyword; all were corrected. This digest deliberately reports `not listed` rather than guessing, which is why several entries lack an organization.
- **Window scope.** One announcement cycle (Friday 2 Oct 2026) across 13 arXiv categories. Conference acceptance rates near deadlines make venue coverage bursty; absence in this window is not evidence of absence in the field.

**Related wiki pages.** [[2026-10-01 conference digest]], [[2026-10-02 arxiv daily]], [[semantic-ids]], [[agent-evaluation-reliability]], [[rlvr]], [[test-time-scaling]], [[generative-recommendation]], [[alignment]]