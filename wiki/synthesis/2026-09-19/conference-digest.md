---
title: "Conference & arXiv Digest: Top ML/AI Conferences 2025-2026 — 2026-09-19"
type: synthesis
created: 2026-09-19
updated: 2026-09-19
sources: [conference-web-searches]
tags: [conference-digest, ICML2026, ICLR2026, NeurIPS2025, KDD2026, CVPR2026, SIGIR2026, ACL2026, EMNLP2025, CIKM2025, RecSys2025, WWW2026, RecSys2026, EMNLP2026, ICDM2026, ACM-MM2026, recommendation, LLM, advertising, CTR, agents, generative-models, sequential-modeling, games, code-execution, benchmarks, daily-digest]
---

# Conference & arXiv Digest: Top ML/AI Conferences 2025-2026 — 2026-09-19

> Follow-up to the [2026-09-11 Full Edition](../2026-09-11). This edition scans the **fresh post-09-11 arXiv wave (~2608.30xxx–2609.17xxx)** plus newly-confirmed venue content: KDD 2026 / KDD Cup 2026 best-solution wave, RecSys 2026 (Minneapolis, Sep 29–Oct 1), EMNLP 2026 (Budapest, Oct 24–29; acceptances out ~Aug 20), ICDM 2026, ACM MM 2026, and fresh ICLR 2026 / NeurIPS 2026 additions. Every featured paper was verified absent from the sister daily digests (arxiv-daily / arxiv-paper-check / arxiv-ai-search 09-16/09-17/09-18).

---

## 1. KDD 2026 & KDD Cup 2026

### 1.1 QueryFormer — 查询驱动序列注意力的 KDD Cup 冠军排序方案
- **Title (EN)**: QueryFormer: KDD Cup 2026 Tencent UniRec Challenge Winning Solution
- **Authors**: Yuanzhe Zhou, Zhaoyang Zeng
- **Affiliation**: Wuhan University / Sun Yat-sen University competition teams
- **Venue**: KDD Cup 2026 — Tencent UniRec Challenge (Industrial Track, **1st place**)
- **arXiv**: https://arxiv.org/abs/2609.16548
- **Innovation**: Cross-attention-generated **query tokens** fed into a shared-parameter sequence-attention block. The learned query token copies/mixes the most relevant user-history information into the item representation context, decoupling *what to extract* from *how to represent* — information extraction is explicitly guided rather than implicit inside a full sequence model.
- **Results**: Official test **AUC 0.83254**; scaled-up variant 0.832713. With H=8 query heads, compile latency grows only ~1.89× vs H=1 — cheap scaling of expressive head count.
- **Comparison**: Beats the native UniRec/InRec sequence baselines and HyFormer-style pointwise/sequence hybrids that dominated earlier UniRec rounds; coherent with the CVR-specialized 1st-place findings on UniRec (paper 2609.19787, covered in [arxiv-paper-check 2026-09-18](../2026-09-18/arxiv-paper-check.md)).

### 1.2 PRIME — 共享 CTR Top 网络的即插即用残差条件 MoE
- **Title (EN)**: Plug-in Residual Input-Conditioned Mixture-of-Experts for Shared CTR Top Networks
- **Authors**: Heng Yao, Siyun Hou, Tianying Liu, Yulou Shu, Yong He, Chuan Yuan, Kaibin Qiu, Guowei Chen, Jiayu Zhao, Chao Yu, Ke Ding
- **Venue**: arXiv (KDD/eCommerce wave)
- **arXiv**: https://arxiv.org/abs/2608.30449
- **Innovation**: Identifies **subgroup gradient competition** in shared CTR top networks — Top-NN cosine similarity of gradients drops 0.23–0.37 on Avazu when subgroups disagree. PRIME plugs in a **residual input-conditioned MoE** so each subgroup gets a gated correction path without replacing the base network.
- **Results**: AUC **+0.0022** (Avazu), **+0.0066** (Criteo) over the shared top network; beats APG-style plug-ins with fewer added parameters.
- **Relevance**: Evidence that shared-sequence CTR architectures retain recoverable subgroup-interference signal — consistent with the UniCon context-centric direction (Section 8).

---

## 2. RecSys 2026 (Minneapolis — Sep 29 – Oct 1, 2026)

### 2.1 GenCDSR — 混合分词 + 串并行解码的跨域序列推荐
- **Title (EN)**: Empowering Cross-Domain Sequential Recommendation with Hybrid Tokenization and Serial-Parallel Decoding
- **Authors**: Yuxuan Hu, Yuhao Wang, Tianbo Huang, Chao Zhang, Ziwei Liu, Lihua Zhang, Xiangyu Zhao
- **Affiliation**: City University of Hong Kong / ByteDance
- **Venue**: RecSys 2026
- **arXiv**: https://arxiv.org/abs/2607.28659
- **Innovation**: Cross-domain sequential recommendation with a **multi-tower hybrid tokenizer** (domain-shared + domain-specific codes) that collapses the cross-domain item-ID space, paired with **serial-parallel decoding** that emits shared and specific tokens concurrently.
- **Results**: ~**+1.5%** accuracy over cross-domain GRec SOTA; **−85.1%** decoding latency vs serial baselines.
- **Comparison**: Attacks the two pain points of cross-domain GRec — ID-space explosion (hybrid tokens) and autoregressive latency (serial-parallel decode).

### 2.2 Position Paper — 自主智能体时代的推荐系统
- **Title (EN)**: A Position Paper on Recommender Systems in the Era of Autonomous Agents
- **Authors**: Aixin Sun
- **Affiliation**: Singapore Management University
- **Venue**: RecSys 2026
- **arXiv**: https://arxiv.org/abs/2607.24822
- **Key argument**: Recommenders are shifting from modeling human interactions to serving software agents (delegated shopping/browsing). Argues for agent-first metrics (task completion, goal alignment) over engagement/NDCG, aligning with the agentic-recommender trend (Alibaba AgenticRS, tracked in this wiki).

---

## 3. EMNLP 2026 (Budapest — Oct 24–29, 2026)

> Acceptances notified ~Aug 20, 2026; the camera-ready arXiv wave is the largest fresh venue content this cycle. Theme across the accepted list: **agent evaluation methodology and hybrid-architecture interpretability**.

### 3.1 What Attention Recalls and Recurrence Controls in Hybrid LMs (Findings) — 混合语言模型中 Attention 记得什么、Recurrence 控制什么
- **Authors**: Kirill Afendulev, Alexey Dontsov, Elena Tutubalina, Anton Korznikov
- **Venue**: EMNLP 2026 Findings
- **arXiv**: https://arxiv.org/abs/2609.04434
- **Innovation**: Two cache-level interventions — **split-prefill** (keep only KV or only recurrent state) and **state-swap** (KV from one context + recurrent state of another). On Qwen3.5 and Falcon-H1 the two channels **split sharply by function**: exact retrieval survives only through attention (64–98% of full accuracy, ~0 through recurrence); output language/persona survive recurrence (70–80% / 3–5×) while KV-only drops to ~1% language accuracy.
- **Causal conclusion**: *Attention provides a lookup over what was said; the recurrent state shapes how the model says it next.* Practical guidance for hybrid (Transformer + fixed-state) inference.

### 3.2 Dude — 论文-代码不一致双重检测多智能体系统 (Main)
- **Title (EN)**: Dude: A Dual-Detection Multi-Agent System for Paper-Code Discrepancy Detection
- **Authors**: Weijie Liu, Running Zhao, Wenhao Yuan, Jinfeng Xu, Zhanfeng Xu, Xiaoxi Zhang, Edith Cheuk-Han Ngai
- **Venue**: EMNLP 2026 Main
- **arXiv**: https://arxiv.org/abs/2609.03416
- **Innovation**: First **dual-detection multi-agent** system for paper-code discrepancy detection (mathematical/algorithmic + factual/informational), overcoming limited-context and one-sided detection of single-agent LLM reviewers; now open-sourced.

### 3.3 Beyond Confidence — 检索接地的 test-time scaling（Findings）
- **Authors**: (EMNLP 2026 Findings)
- **Venue**: EMNLP 2026 Findings
- **arXiv**: https://arxiv.org/abs/2608.24024
- **Innovation**: Uses **retrieval grounding as the test-time scaling axis** for multi-turn search agents — the agent spends its budget on grounded verification retrievals rather than confidence calibration; evaluates where confidence alone over-/under-trusts.

### 3.4 RefactorPlatform — 仓库级重构智能体受控评测平台（System Demo）
- **Title (EN)**: RefactorPlatform: An Open-Source Harness for Controlled Evaluation of Repository-Scale Refactoring Agents
- **Authors**: Aziz Ben Amor, Drish Mali, Mann Acharya, Vijayasri Iyer, Sébastien Bratières
- **Venue**: EMNLP 2026 System Demonstrations
- **arXiv**: https://arxiv.org/abs/2609.04898
- **Innovation**: Holds the environment fixed and varies each design axis explicitly — model backbone (OpenRouter / GitHub Copilot CLI), execution regime (baseline / retrieval-augmented / multi-agent), prompt specificity — isolating what actually determines refactoring-agent success.

---

## 4. ICDM 2026

### 4.1 HypRQ-VAE — 双曲项索引解决生成式推荐的长尾幻觉
- **Title (EN)**: Hyperbolic Item Indexing for Long-Tail-Aware Generative Recommender Systems
- **Authors**: Longfeng Wu, Tong Zeng, Giovanni Seni, Zhimin Peng, Bhanu Pratap Singh Rawat, Si Zhang, Yao Zhou, Lecheng Zheng, Bo Ji, Yujun Yan, Dawei Zhou
- **Affiliation**: Virginia Tech (+ Amazon/Meta/Google researchers)
- **Venue**: ICDM 2026
- **arXiv**: https://arxiv.org/abs/2609.03369
- **Innovation**: Replaces Euclidean assignments in residual-quantized VAE item indexing (the tokenization backbone of LLM-based generative recsys) with a **hyperbolic (Poincaré) item index**. Hyperbolic volume growth matches the power-law long tail of item popularity, fixing the mismatch by which quantization coerces rare items into crowded Euclidean clusters.
- **Results**: Reduces hallucinated rare-item generations and lifts long-tail recall/hit-rate for generative recommenders — targeting exactly the failure class seen in Tencent UniRec and other production GRec deployments.

---

## 5. ACM Multimedia 2026

### 5.1 WIDE — 通配符推理的动态扩展到跨模态生成式检索
- **Title (EN)**: Wildcard Inference with Dynamic Expansion for Cross-Modal Generative Retrieval
- **Authors**: Teng Guo, Xin Wang, Jiayou Xu, Keying Zhou, Jifeng Shen, Haoxin Ruan
- **Affiliation**: Jilin University
- **Venue**: ACM MM 2026
- **arXiv**: https://arxiv.org/abs/2609.03554
- **Innovation**: Diagnoses **forced hallucination** in trie-constrained beam search for cross-modal generative retrieval (candidate trie forces a token with tiny probability), and fixes it with **wildcard decoding + Adaptive Entropy Thresholding** — when entropy signals the forced token is unwarranted, the decoder expands to wildcard candidates dynamically.
- **Significance**: A practical tokenization/decoding-level repair for generative retrieval systems; complements the long-tail/ID-space papers above (HypRQ-VAE, GenCDSR).

---

## 6. ICLR 2026 (Rio de Janeiro — Apr 28 – May 2, 2026) — fresh additions

### 6.1 Code World Models for General Game Playing（Google DeepMind）— 代码世界模型用于通用游戏博弈
- **Authors**: Wolfgang Lehrach, Daniel Hennes, Miguel Lazaro-Gredilla, Xinghua Lou, Carter Wendelken, Zun Li, Antoine Dedieu, Marc Lanctot, Atil Iscen, John Schultz, Marcus Chiam, Ian Gemp, Piotr Zielinski, Satinder Singh, Kevin Murphy
- **Affiliation**: Google DeepMind
- **Venue**: ICLR 2026 (accepted)
- **arXiv/Proceedings**: ICLR 2026 proceedings page (proceedings.iclr.cc, hash d8a12fde9e72444e1b356e8c37e53753)
- **Innovation**: Instead of prompting the LLM directly for moves (which yields illegal moves and shallow play), the LLM **translates natural-language rules + trajectories into an executable Python world model** (state transition, legal-move enumeration, termination checks), then classical **MCTS** plans over the verified simulator. LLM also generates heuristic value functions (perfect-info efficiency) and inference functions (hidden-state estimation in imperfect-info games).
- **Results**: Evaluated on 10 games (5 perfect, 5 imperfect info; 4 novel). Outperforms or matches Gemini 2.5 Pro in **9/10** games. Three advertised advantages vs direct prompting: verifiability, strategic depth, and generalization (data-to-code meta-task).
- **Comparison**: Direct contrast to the "LLM as policy" line of game agents — same LLM, but reassigned to world-model compilation, retaining classical search optimality.

### 6.2 Fine-Tuning Diffusion Models via Intermediate Distribution Shaping — GRAFT 广义拒绝采样微调
- **Title (EN)**: Fine-Tuning Diffusion Models via Intermediate Distribution Shaping
- **Authors**: (ICLR 2026)
- **Venue**: ICLR 2026
- **arXiv**: https://arxiv.org/abs/2510.02692v3
- **Innovation**: **GRAFT** (genеralized rejection sampling for fine-tuning target scores) shapes the intermediate distribution instead of the final one, enabling reward/score fine-tuning for layout & molecule generation on per-step guidance (IGD). Repurposes the diffusion generative prior rather than post-hoc guidance.
- **Significance**: With diffusion models returning to the top of the gen-model agenda (diffusion LMs, DSA, NN-DiT), a training-side alternative to guidance-with-classifiers.

### 6.3 Scaling Behavior of Discrete Diffusion Language Models — 离散扩散语言模型的 Scaling 行为
- **Venue**: ICLR 2026
- **Innovation**: Systematic scaling study of uniform discrete-diffusion LMs up to **10B parameters / ~1e22 FLOPs**, mapping the loss/scaling laws of the diffusion family vs autoregressive transformers; informs when a fixed-order diffusion model overtakes AR modeling on perplexity/cost frontiers.

---

## 7. NeurIPS 2025 / 2026 — fresh additions

### 7.1 Scaling Diffusion Transformers Efficiently via muP (SLAB-muP) — 深度 μP 缩放 DiT
- **Title (EN)**: Scaling Diffusion Transformers Efficiently via muP (SLAB-muP)
- **Venue**: NeurIPS 2025
- **Innovation**: Applies **maximal-update parameterization** to diffusion transformers: DiT-XL-2 under muP converges **~2.9× faster**; width-stability enables direct MMDiT scaling from 0.18B → 18B without tuning hyperparameters — making DiT scaling behave like LLM scaling.
- **Significance**: Bridges the diffusion scaling gap — the same hyperparameter-transfer recipe that stabilizes LLM pretraining now applies to DiT/MMDiT.

### 7.2 Diffusion Tree Sampling — 推理期对齐扩散模型
- **Venue**: NeurIPS 2026 (author-driven posting)
- **Innovation**: Inference-time alignment for diffusion models via tree-structured sampling with a reward-aware search/expansion rule, analogous to best-of-N / tree search for diffusion rather than autoregressive decoding.
- **Significance**: If confirmed at cameras-ready: diffusion gets an inference-time-scaling knob that mirrors MCTS for AR LLMs.

### 7.3 NeurIPS 2026 logistics note
- Author notifications for NeurIPS 2026 are due ~**Sep 24, 2026**; "under review" tagged submissions (incl. the diffusion-tree-sampling line) will resolve into accept/notify in the coming digest windows. Multi-site registration (San Diego + Mexico City precedent for 2025) continues for the 2026 mega-conference.

---

## 8. Advertising & CTR — 广告与点击率

### 8.1 UniCon (Meituan) — 统一 Context-Centric CTR 建模
- **Title (EN)**: UniCon: Unified Context-Centric Modeling Paradigm for CTR Prediction
- **Authors**: Jiajun Cui, Zhengqi Xu, Fan Zhang, Gu Tang, Honghong Zhu, Mengxi Wu, Yulin Liang, Xingxing Wang
- **Affiliation**: Meituan (search advertising) | E-commerce shelves + e-Tailing
- **Venue**: arXiv (v2)
- **arXiv**: https://arxiv.org/abs/2609.03290
- **Innovation**: Treats user **behavior as homogeneous context units** in a unified context-centric paradigm (vs the rigid user-behavior vs item-feature split): the item is placed back into its behavioral context and the CTR network reads the *unified context* rather than separate towers.
- **Results**: Offline AUC **+0.0139**; online RPM **+3.09%**, CTR **+2.07%**, revenue **+2.95%**.
- **Comparison**: Same direction as HyFormer/EST/OneTrans sequence-context unification — but more radical: it removes the feature/behavior dichotomy entirely; one of the strongest recent *unified-context* industrial reports (cross-referenced in the CTR-scaling thread).

### 8.2 DMRL (Kuaishou + SJTU) — 文档介导强化学习的广告技能优化
- **Title (EN)**: DMRL: Document-Mediated Reinforcement Learning for Skill Optimization in Advertising Recommendation
- **Authors**: Wei Zhang, Hongji Li, Song Sun, Peng Yu, Xue Yang, Lei Zhao, Peng Jiang
- **Affiliation**: Kuaishou Technology / Shanghai Jiao Tong University
- **Venue**: arXiv
- **arXiv**: https://arxiv.org/abs/2609.02170
- **Innovation**: Decomposes ad skill optimization into (a) **DRPO** — a post-training policy-optimization algorithm extending GRPO with a dual-relative advantage estimator, and (b) **LRP** — a long-term reward prediction module with population-invariant dynamics (adversarial regularization) to fight delayed/heterogeneous feedback. Two-stage training decouples long-term outcome prediction from advantage estimation; deployed on a real advertising platform with significant online gains.

---

## 9. Agents & Agentic RL — 智能体与智能体强化学习

### 9.1 CANOPY — 纯 outcome-only RL 足够长期程智能体
- **Title (EN)**: Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents
- **Authors**: Liming Pu, Xiaoxia Li, Yifu Liu, Teng Cao, Bin Yang
- **Venue**: arXiv
- **arXiv**: https://arxiv.org/abs/2609.01245
- **Innovation**: Argues the "outcome-only RL ceiling on small open models" is an artifact of two failures: **signal starvation** (group-relative RL gets no gradient when a rollout group is all-success or all-fail) and **policy drift** (unsqueezing updates from a small task pool collapses the sampling distribution). CANOPY = Coverage-ANchored On-PolicY RL: scale same-task exploration until the signal reappears, keep updates on-policy/KL-anchored on the agent's own action tokens.
- **Results**: Qwen3-14B trained through environment interaction alone (no SFT priors, no skill libraries) **topped the AppWorld leaderboard** (Feb 2026: Test-Normal TGC 86.9, Test-Challenge 67.6); the same recipe lifts Qwen3.5-9B **+16.6** on SWE-bench Verified.
- **Significance**: A strong counterpoint to the "need dense rewards / scaffolding" view — agentic RL alone can internalize long-horizon capability into small open models (cross-ref SPA self-play finetuning line, [SPIRAL](../papers/games/spiral-self-play-reasoning.md)).

### 9.2 Coding Agents Have Converged — SWE-bench Leaderboard 无法再排序头部
- **Title (EN)**: Coding Agents Have Converged: Why the SWE-bench Leaderboard Can No Longer Order Its Top Entries, and What to Measure Instead
- **Authors**: Fengshuo Liu, Ying Liu, Ruize Sun, Lie Luo, Siyuan Guo
- **Venue**: arXiv (benchmark meta-analysis)
- **arXiv**: https://arxiv.org/abs/2609.17394
- **Innovation**: Audits 254 SWE-bench submissions across four splits (no model runs): on Verified the **top two entries each resolve 396/500** — statistically indistinguishable. Reading small leaderboard deltas as system ordering is unsupported; proposes what to measure instead (task coverage, difficulty tiers, failure mode taxonomies).
- **Significance**: Mirrors the benchmark-validity thread (SWE-bench+ contamination, leaderboard-illusion concept page) — evaluation instrument saturation, not capability plateau, is the better reading.

### 9.3 PTA-IRT — 轨迹感知的高效 SWE 智能体评测
- **Title (EN)**: Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation
- **Authors**: Kefeng Duan, Dewu Zheng, Yanlin Wang, Xiwen Wang, Ensheng Shi, Xilin Liu, Yuchi Ma, Jiachi Chen, Mingwei Liu, Zibin Zheng
- **Affiliation**: Sun Yat-sen University (DeepSoftwareAnalytics)
- **Venue**: arXiv
- **arXiv**: https://arxiv.org/abs/2609.01603
- **Innovation**: **PTA-IRT** = Privileged Trajectory-Aware Item Response Theory: uses historical execution trajectories (explored context, attempted edits, solving paths) as privileged process-level evidence beyond pass/fail, for calibration-subset selection and ability estimation. Beats prior IRT baselines on score/rank recovery across four SWE benchmarks under low calibration budgets.
- **Significance**: Answers the cost problem behind 9.2 — we can estimate full-benchmark performance from cheap trajectory-aware subsets instead of running everything.

### 9.4 RobustSGPO (Kuaishou) — 搜索空间控制的 Agent Harness 演化
- **Title (EN)**: RobustSGPO: Search-Space Control for Agent Harness Evolution
- **Authors**: Zibo Zhao, Jijun Shi, Mo Zhou, Zhongyuan Wang, Shifu Bie, Yunfei Zhang, Xuanting Zhou, Xiangyu Wu, Bin Liu, Ruiming Tang, Wenwu Ou, Kun Gai
- **Affiliation**: Wuhan University / Kuaishou Technology
- **Venue**: arXiv
- **arXiv**: https://arxiv.org/abs/2609.09646
- **Innovation**: Repairs semantic-gradient prompt optimization (SGPO) — whose local update rule leaves edit scope/operation unresolved — by specifying the requested edit, constructing+checking the patch, and continuing search from either the incumbent or retained snapshots. Evaluated on permission scheduling, cumulative controls, task-family transfer in Kuaishou's AgentX brainstorming workflow (120 tasks / 95 runs / 7,350 candidate attempts).
- **Results**: Periodic 1→2→3 scheduling beats fixed max permissions by **+0.28 test-score**; completion on 30 held-out tasks **60.0%→80.0%**, test quality **3.77→4.14** under a 20M-token budget.

---

## 10. Code & Software Engineering — 代码与软件工程

### 10.1 Beyond Confidence — 已在 EMNLP 一节收录(见 3.3)
- Retrieval-grounded test-time scaling for multi-turn search agents (EMNLP 2026 Findings).

### 10.2 AgentSpec — 批量 LLM 智能体推理的投机解码
- **Title (EN)**: AgentSpec: Speculative Decoding for Batch LLM Agent Inference
- **Venue**: EMNLP 2026 (accepted list)
- **Innovation**: Exploits the repetitive, structured trajectories of agent sessions (tool-call schemas, JSON returns) to speculatively predict next agent steps/tokens across a batch, reducing per-turn latency for multi-agent orchestrations.
- **Significance**: Serving-level answer to agent cost at scale — complements RefactorPlatform (harness) and CANOPY (training) as the inference-speed axis of the agent stack.

---

## 11. Sequential Modeling & Hybrid Architectures — 序列建模

### 11.1 Dynamic Linear Attention (DLA) — 动态记忆的多态线性注意力
- **Title (EN)**: Dynamic Linear Attention
- **Authors**: Xin Wang, Hui Shen, Boyuan Zheng, Xueshen Liu, Minkyoung Cho, Zhongwei Wan, Zesen Zhao, Zhuoqing Mao, Shen Yan, Mi Zhang
- **Venue**: arXiv (June 2026)
- **arXiv**: https://arxiv.org/abs/2606.10650
- **Innovation**: Multi-state linear attention with a **State Information Score** that detects semantic drift and creates new states on demand; a capacity-bounded cache merges the *least informative* adjacent state pair (lowest info density `(I_i+I_j)/(n_i+n_j)`) to stay within budget K. Preserves high-resolution information for rare/critical transitions.
- **Results**: With a Mamba-2 backbone, DLA improves average commonsense-reasoning accuracy by **~8%** over the prior multi-state SOTA (Log-Linear Attention) at constant memory budget.
- **Context**: Complements the hybrid-LM interpretability finding (3.1) — how to keep a *multi*-state recurrence useful rather than a single fixed state.

### 11.2 CSP — 复数状态传播器：确定性状态跟踪只需状态传播
- **Title (EN)**: State Propagation Also Satisfies: A Complex-Valued State-Space Model for Deterministic State Tracking
- **Authors**: Xiaohe Li, Yang Lu
- **Venue**: arXiv
- **arXiv**: https://arxiv.org/abs/2608.03425
- **Innovation**: A minimal recurrent architecture that *only propagates hidden states* (no output projections mid-stream), complex-valued with input-dependent rotations; block-level skip connections + element-wise complex normalization + SiLU at boundaries fix deep-propagation gradient issues.
- **Results**: **100% accuracy / perfect F1** on parity, modular counting, and parenthesis matching with Focal Loss — showing state propagation alone (no attention) is sufficient for deterministic state tracking.

### 11.3 PVMC (ICML 2026) — 并行变分蒙特卡洛训练深度状态空间模型
- **Title (EN)**: Efficient Learning of Deep State Space Models via Importance Smoothing (PVMC)
- **Authors**: John-Joseph Brady, Nikolas Nusken, Yunpeng Li
- **Venue**: ICML 2026
- **arXiv**: https://arxiv.org/abs/2605.21108
- **Innovation**: Bridges auto-encoding and SMC-based DSSM training with **parallel variational Monte Carlo** — trains DSSMs for both discriminative and generative tasks without the sequential SMC forward pass.
- **Results**: Matches/exceeds DSSM SOTA while training **10× faster** than the fastest competing SMC-based approach. Bayesian sequential-modeling relevance (with latent diffusion DSSMs like DDSSM appearing this year for time series).

---

## 12. Generative Models — 扩散/自回归生成

### 12.1 LLaDA-Image — 开放的规模化无条件图像生成器
- **Title (EN)**: LLaDA-Image: (open image generator)
- **Venue**: arXiv
- **arXiv**: https://arxiv.org/abs/2609.03796
- **Innovation**: A **6B DiT** open image generator trained with LLaDA2.0-Mini-style large-diluted-attention methodology — extending the LLaDA family from text to image generation with an open model release.
- **Significance**: Continues the trend of open large diffusion/LDM image models; relevant to the diffusion-LM scaling thread (Section 6.3, 7.1).

---

## 13. Cross-Cutting Observations & Calendar

- **Unified context / unified-scaling tension (CTR thread)**: KDD Cup 2026 UniRec CVR paper (2609.19787) reported dense-feature representations +0.0095 AUC vs all sequence-modeling ≤0.0005 at 34.82M records, while UniCon (Meituan) reports +0.0139 from a fully context-centric paradigm and QueryFormer (KDD Cup #1) wins via query-token-guided sequence attention. The tension (dense-vs-sequence at what scale) is flagged for the CTR-scaling claims in this wiki.
- **Hybrid LMs are now interpretable as two instruments**: attention = episodic lookup, recurrence = language/persona (3.1); multi-state linear attention recovers more (11.1). Converges with DeepSeek-V4 / Kimi-K3-class million-token hybrids — a clean story for architecture families.
- **Agent evaluation is saturating**: SWE-bench top entries statistically tied (9.2), trajectory-aware subsets cut eval cost (9.3), harness/refactor platforms control design axes (3.4), outcome-only RL removes scaffolding (9.1). The agent stack's remaining bottleneck is evaluation measurement, not raw score.
- **Games**: LLM-as-world-model-compiler (Code World Models, 6.1) is now the accepted ICLR vehicle for top-lab game agents, complementing the self-play line (SPIRAL, already in this wiki).
- **Coming calendar**: NeurIPS 2026 author notifications ~Sep 24 (this window's under-review items will resolve); RecSys 2026 conference Sep 29–Oct 1 (final program → next digest); EMNLP 2026 conference Oct 24–29; NeurIPS 2026 conference Dec. Expect the KDD/RecSys/EMNLP camera-ready arXiv wave to peak mid-October.

---

## Data Quality Notes

- arXiv IDs quoted are the latest versions seen in this run; venue assignments come from arXiv comments fields / official proceedings where available (`accepted to ...`). Posting dates for the fresh wave: Aug 25 – Sep 15, 2026.
- Where a number is a single-source report (e.g., DMRL online gains, WIDE metrics), it is kept as reported by the authors and marked tentative where the venue is not yet search-confirmed.
- No contradictions with existing wiki claims surfaced; the UniRec dense-vs-sequence ablation sits against the unified-sequence-scaling thesis and is flagged as an open tension, not a resolved contradiction.