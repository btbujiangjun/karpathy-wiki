---
title: arXiv AI Research Search — August 7, 2026
type: synthesis
created: 2026-08-07
updated: 2026-08-07
sources: [arxiv-listing, arxiv-abstract-pages]
tags: [arxiv, ai, llm, recommendation, advertising, ctr, sequential-modeling, games, game-theory, daily-digest]
---

# arXiv AI Research Search — 2026-08-07

> Search window: arXiv new submissions Aug 5–6, 2026 (IDs ~2608.05150–2608.06380). Streams scanned: cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, econ.TH, cs.DB. The arXiv export API was intermittently rate-limited (HTTP 503/429), so all metadata was verified against the arXiv recent-listings pages and individual abstract pages instead.
>
> 17 papers curated. 9 were already covered by the 2026-08-05/06/07 daily digests — they are included here with full detail for a self-contained report and flagged with a coverage pointer. 8 are **new** (no prior wiki coverage, verified by grep on arXiv ID).

## Overview table

| # | Paper | Domain | Institution / Company | arXiv | Status |
|---|-------|--------|----------------------|-------|--------|
| 1 | RRC: Ranking-Based Reward Construction | LLM RL | Northeastern University | 2608.06310 | covered 08-07 |
| 2 | LC-GRPO: Langevin Correction for Flow GRPO | Diffusion RL | (not stated; Mengdi Wang = Princeton, tentative) | 2608.05600 | **new** |
| 3 | Reasoning Errors in Residual-Stream Trajectory | LLM interpretability | Univ. of Adelaide | 2608.05660 | **new** |
| 4 | Gryphon-v2: Generate-and-Rank Recommender | Rec (generative) | Yandex Music | 2608.06213 | covered 08-07 |
| 5 | OMEGA: Collaborative Memory for GR | Rec (generative) | Renmin Univ. of China | 2608.01315 | covered 08-05 |
| 6 | SITA: Semantic Interest Tokens | Rec (long-sequence) | Huawei / USTC | 2608.03692 | covered 08-05 |
| 7 | ATLAS: Cross-Domain Recommendation | Rec (zero-shot) | TCS Research | 2608.03899 | covered 08-05 |
| 8 | LIME-Rec: Semantic-Gain Recovery Test | Rec (eval/audit) | (not stated; tentative Huawei) | 2608.01260 | covered 08-05 |
| 9 | DEGR: Exploration-Driven Generative Re-Ranking | Ads / re-ranking | JD.com | 2608.04809 | covered 08-06 |
| 10 | LLM-OSDA: Ad Auction in LLM Conversations | Ads / mechanism design | (not stated; co-author C. Law = ByteDance/TikTok, tentative) | 2608.00123 | **new** |
| 11 | Beyond PPAD Hardness of Auto-bidding | Ads / auction theory | Univ. of Washington | 2608.01889 | **new** |
| 12 | VLM Relevance Measurement | Search eval | Pinterest | 2608.02446 | **new** |
| 13 | Algorithmic Collusion (Asynchronous) | Pricing / GT | ENS Paris-Saclay | 2608.01406 | **new** |
| 14 | CvLoss: Cross-Variable Loss for MTSF | Sequential / time series | UNSW Sydney | 2608.05742 | **new** |
| 15 | Multi-Objective Live-Streaming Ranking | Rec (industry) | Amazon / Twitch | 2608.04455 | covered 08-06 |
| 16 | AV-AIVAT: Agent Evaluation in Games | Games / evaluation | Tsinghua University | 2608.06362 | covered 08-07 |
| 17 | Humans Are More Diverse: LLM Races | Multi-agent / games | Teesside University | 2608.01193 | **new** |

---

## 1. LLM Training, RL & Reasoning

### 1.1 RRC: Unlocking Generative Reward Models in LLM RL via Ranking-Based Reward Construction

- **arXiv**: [2608.06310](https://arxiv.org/abs/2608.06310) (cs.LG; submitted 2026-08-06)
- **Authors**: Chenglong Wang, Ziming Zhu, Yifu Huo, Bei Li, Qiaozhi He, Yan Ding, Xiaoyang Hao, Yuxin Gao, Tianhua Zhou, Xiaojia Chang, Tongran Liu, Jingbo Zhu
- **Institution**: Northeastern University, China (high confidence — per 08-07 arxiv-daily attribution)
- **Abstract (faithful summary)**: Reward modeling is shifting from discriminative to generative reward models. Despite strong response-ranking ability, generative reward models have not delivered gains in RL. The authors diagnose a mismatch: generative reward modeling is comparative, but existing RL algorithms adopt scalar scoring. RRC derives rewards from relative preference rankings instead. Two strategies: **self-competitive ranking** (comparisons among sampled responses) and **anchor-guided ranking** (scalable ranking-based reward construction with a small set of reference responses). Experiments on open-ended chat and reasoning benchmarks show consistent gains over existing reward-construction approaches. Code: `github.com/wangclnlp/RRC`.
- **Key innovations**: (1) First principled bridge from comparative generative reward models to scalar RL signals; (2) ranking-based reward construction via self-competitive + anchor-guided strategies; (3) open-sourced code.
- **Coverage note**: Also in [2026-08-07 arXiv Daily Digest](./arxiv-daily.md).

### 1.2 LC-GRPO: Bridging Train-Inference Gap for Flow-Based GRPO with Langevin Correction

- **arXiv**: [2608.05600](https://arxiv.org/abs/2608.05600) (cs.LG; submitted 2026-08-06) — **NEW**
- **Authors**: Yingqing Guo, Hui Yuan, Zijian He, Mengdi Wang, Zheng Ding
- **Institution**: Not stated on abstract page. Co-author Mengdi Wang is affiliated with Princeton University (tentative); others unknown.
- **Abstract (faithful summary)**: Flow-based generative models are sampled at inference by solving a deterministic ODE, but online RL requires stochastic rollouts for exploration. Existing GRPO methods therefore replace the inference ODE with an SDE during training. ODE and SDE share the same marginals in continuous time, but finite-step discretizations diverge — SDE rollouts become blurry as exploration noise grows, mismatching test-time ODE sampling. LC-GRPO gives each rollout transition an **inference-aligned ODE Euler step** followed by a **stochastic Langevin correction** targeting the marginal at that timestep. The required score is recovered from the flow velocity (no extra score model); the transition stays an isotropic Gaussian with tractable likelihood. Theoretically, one Langevin step reduces the Wasserstein error of an imperfect ODE Euler step, and the transition is more accurate than Euler–Maruyama of the reverse SDE at matched randomness. Experiments on SD3.5-Medium, FLUX.1-Dev, and HunyuanVideo show consistent reward-optimization gains in text-to-image and text-to-video, preserved quality, and a narrowed train/test gap.
- **Key innovations**: (1) Langevin-correction transition that keeps stochastic exploration while staying inference-aligned; (2) score read off the flow velocity, no auxiliary score model; (3) Wasserstein-error reduction guarantee per correction step.

### 1.3 Reasoning Errors Have a Region and a Direction in the Residual-Stream Trajectory of LLMs

- **arXiv**: [2608.05660](https://arxiv.org/abs/2608.05660) (cs.LG; submitted 2026-08-06) — **NEW**
- **Authors**: Hamed Damirchi, Ignacio Meza De la Jara, Damith Ranasinghe, Yuhang Liu, Javen Shi
- **Institution**: University of Adelaide (high confidence — Damith Ranasinghe's affiliation)
- **Abstract (faithful summary)**: Detecting sound vs flawed reasoning is increasingly important. Trajectory-based detectors read layerwise residual-stream displacements, which capture how representations change while attenuating token-specific information — but displacement omits the originating state, while restoring full state risks shortcut-prone information. The authors propose a **three-stream detector**: motion (displacement) + a coarse **region reader** (vector quantization) + a fine **direction reader** over normalized multi-layer states. On unseen reasoning benchmarks it improves selection accuracy by up to 12% over displacement-only SOTA and 21% over single-layer probing. Trained only on reasoning, it also transfers to factual completion/verification — the signal tracks correctness, not reasoning type. Ablations show motion/region/direction are complementary.
- **Key innovations**: (1) State-conditioned motion instead of decontextualized trajectories; (2) quantized region + directional readers restore state context cheaply; (3) correctness signal generalizes beyond the training task family.

---

## 2. Recommendation & Generative Ranking

### 2.1 Gryphon-v2: One Model in Place of a Cascade — Generate-and-Rank Recommender with Rollout Distillation

- **arXiv**: [2608.06213](https://arxiv.org/abs/2608.06213) (cs.IR; submitted 2026-08-06)
- **Authors**: Anna Lipkina, Daria Tikhonovich, Viktor Yanush, Mariia Ulianova, Oleg Sorokin, Vladislav Dodonov, Ilya Murzin, Denis Burshtein, Nikolay Savushkin
- **Institution**: Yandex (Yandex Music) (high confidence — deployment stated in abstract)
- **Abstract (faithful summary)**: Industrial recommenders are multi-stage cascades (candidate generation, pre-ranking, final ranking) with repeated user-history processing. Semantic-ID generative retrieval promises simpler end-to-end systems, but next-item prediction alone misses production ranking preferences. Gryphon-v2 is a unified **generate-and-rank** architecture: encode user history once, generate Semantic-ID candidates with an autoregressive decoder, resolve to catalogue items, and rank via an item-level Ranking Module reusing shared encoder states. Production ranking preferences are transferred by **Rollout Distillation** from a training-only Teacher Ranker; teacher scores over two complementary distributions (decoder rollouts + logged impressions) are the only ranking supervision. Online A/B at Yandex Music: a single Gryphon-v2 replaces a cascade of **>15 candidate generators + pre-ranking + final ranking**, raising active users **+1.41%** at comparable serving latency.
- **Key innovations**: (1) One model replaces an entire production cascade; (2) teacher-only ranking supervision via rollout + logged-impression distillation; (3) shared encoder states amortize user-history processing.
- **Coverage note**: Also in [2026-08-07 arXiv Daily Digest](./arxiv-daily.md).

### 2.2 OMEGA: Collaborative Memory Augmentation for Generative Recommendation

- **arXiv**: [2608.01315](https://arxiv.org/abs/2608.01315) (cs.IR; submitted 2026-08-02)
- **Authors**: Enze Liu, Zhen Tian, Wayne Xin Zhao
- **Institution**: Renmin University of China (high confidence)
- **Abstract (faithful summary)**: Generative Recommendation (GR) models item transitions as sequence-to-sequence, but mostly within a constrained internal parametric space per user, ignoring cross-user collaborative signals. OMEGA bridges implicit parametric knowledge and explicit collaborative signals: (1) latent context compression via learnable query tokens distills sequential behavior into compact representations; (2) compressed representations aggregate into a **collaborative memory bank** — an explicit global behavioral-pattern repository; (3) a lightweight **target-aware retrieval** mechanism matches sequence-level and target-level similarities; (4) a gated cross-attention **context-aware integration** fuses retrieved memories with local user context while suppressing noise. Outperforms advanced GR models on multiple real-world datasets. Accepted to KDD 2026 Research Track.
- **Key innovations**: (1) Explicit external collaborative memory for GR; (2) learnable-query-token compression with low storage overhead; (3) target-aware memory retrieval + gated fusion.
- **Coverage note**: Also in [2026-08-05 arXiv Daily Digest](../2026-08-05/arxiv-daily.md).

### 2.3 SITA: Semantic Interest Tokens for Target-Aware Compression in Long-Sequence Recommendation

- **arXiv**: [2608.03692](https://arxiv.org/abs/2608.03692) (cs.IR; submitted 2026-08-04)
- **Authors**: Rui Zhou, Bo Chen, Qinglin Jia, Jiezhou Ji, Chaoyi Ma, Ruiming Tang, Hao Wang, Enhong Chen
- **Institution**: Huawei Noah's Ark Lab + University of Science and Technology of China (USTC) (high confidence)
- **Abstract (faithful summary)**: Long user histories are hard to model: target-aware retrieval of relevant behaviors requires target-dependent computation at inference; whole-sequence compression is efficient but target-independent. SITA gets target-aware compression via **semantic identifiers learned by parallel semantic quantization** that organize compressed interests into semantic structures; conditioned on the target item's semantic identifier, SITA adaptively aggregates the corresponding structured interests into a target-specific user representation. Consistently outperforms baselines on public + large-scale industrial datasets while maintaining scalability.
- **Key innovations**: (1) Target-aware compression that keeps the efficiency of pre-compressed user representations; (2) parallel semantic quantization producing structured, semantic-interest tokens; (3) industrial-scale validation.
- **Coverage note**: Also in [2026-08-05 arXiv Daily Digest](../2026-08-05/arxiv-daily.md).

### 2.4 ATLAS: Learning to Recommend Across Unseen Domains

- **arXiv**: [2608.03899](https://arxiv.org/abs/2608.03899) (cs.IR; submitted 2026-08-04)
- **Authors**: Pervez Shaik, Prosenjit Biswas, Abhinav Thorat, Ravi Kolla, Niranjan Pedanekar
- **Institution**: TCS Research (Tata Research Development and Design Centre, Pune) (high confidence)
- **Abstract (faithful summary)**: Recommenders are domain-bound; a movie recommender can't directly serve groceries. ATLAS learns a shared, domain-invariant user-item representation from disjoint source domains for **zero-shot recommendation on unseen domains**, without target adaptation or language-model pretraining. Components: **Gromov-Wasserstein alignment** preserving cross-domain user relationships; an **adversarial objective** making item representations domain-indistinguishable; **residual vector quantization (RVQ)** codebooks compressing embeddings into a discrete latent space that captures hierarchical interaction patterns while suppressing domain-specific variation. Trained on 5 Amazon domains, applied to 10 unseen domains: beats sequential, graph-based, cross-domain, quantization-based, and LLM baselines on most domains, **+24% average HitRate**. Source-domain diversity is a pronounced driver of transfer.
- **Key innovations**: (1) Recommendation-specific domain generalization without any target-domain adaptation or LLM pretraining; (2) GW alignment + adversarial + RVQ combination; (3) quantifies the source-diversity effect.
- **Coverage note**: Also in [2026-08-05 arXiv Daily Digest](../2026-08-05/arxiv-daily.md).

### 2.5 LIME-Rec: Auditing Semantic Gains in Sequential Recommendation (A Lightweight Recovery Test)

- **arXiv**: [2608.01260](https://arxiv.org/abs/2608.01260) (cs.IR; submitted 2026-08-02)
- **Authors**: Kong Wang, Zhongke He, Xiang Chen, Hongwei Zeng, Kai Deng, Long Wang, Kehua Yang
- **Institution**: Not stated on abstract page (tentative: Huawei; single-source).
- **Abstract (faithful summary)**: Semantic/generative-retrieval recommenders report big gains over ID-only sequential baselines, but the source of the gain is ambiguous (LM reasoning vs semantic-ID generation vs end-to-end semantics vs stronger item representations vs complementary signals). LIME-Rec is a lightweight, auditable **recovery test**: three independent experts — SASRec (sequential), ItemCF (co-occurrence), and a frozen `BAAI/bge-base-en-v1.5` semantic expert — fused by auditable score-level fusion + bounded history calibration (fitted on validation only, no serving-time LM inference). On Amazon Beauty/Toys/Sports, R@10 = 0.0996/0.1105/0.0593, beating the strongest baseline by 7.0–12.0%. Permuting item-text embeddings across IDs drops R@10 by 13.6–17.5%, showing gains depend on genuine text correspondence, not extra capacity. Conclusion: lightweight recovery from offline representations + transparent fusion must be ruled out before attributing gains to serving-time LM / semantic-ID machinery.
- **Key innovations**: (1) A cheap audit protocol for semantic-recommender claims; (2) three-expert auditable fusion with bounded calibration; (3) negative-control (embedding permutation) evidence that gains are text-grounded.
- **Coverage note**: Also in [2026-08-05 arXiv Daily Digest](../2026-08-05/arxiv-daily.md).

---

## 3. Advertising, CTR & Auctions

### 3.1 DEGR: Dual Exploration-Driven Generative Re-Ranking for Adaptive Cross-Request Context Bridging

- **arXiv**: [2608.04809](https://arxiv.org/abs/2608.04809) (cs.IR; submitted 2026-08-05)
- **Authors**: Binglei Zhao, Xuanhua Yang, Xiwei Zhao, Sulong Xu
- **Institution**: JD.com (high confidence — JD E-commerce deployment in abstract; KDD 2026 ADS Track)
- **Abstract (faithful summary)**: Re-ranking balances business objectives and diversity for sequence-level optimization, but fixed upstream supply caps gains, especially under low-quality supply. DEGR lets re-ranking actively trade immediate vs exploratory value — e.g. prioritize exploratory exposure under low-quality supply to preserve browsing potential and drive serendipitous conversion. DEGR uses a **hybrid supervised–RL exploration-and-optimization paradigm** driven by an **exploratory reward model** that adaptively balances immediate and exploratory value, integrating supervised learning, an exploration-diversity constraint, and **adaptive reward-weighted ORPO** preference optimization. Offline + online: up to **+1.22% UCTR** and **+0.20% PV** in JD's e-commerce recommender.
- **Key innovations**: (1) Explicitly models exploration value to escape the fixed-supply ceiling; (2) dual exploration (supervised + RL preference optimization); (3) adaptive reward-weighted ORPO for the generator.
- **Coverage note**: Also in [2026-08-06 arXiv Daily Digest](../2026-08-06/arxiv-daily.md) and [2026-08-06 arXiv Paper Check](../2026-08-06/arxiv-paper-check.md).

### 3.2 LLM-OSDA: An Optimal-Stopping Dynamic Auction for Native Advertising in Multi-Turn LLM Conversations

- **arXiv**: [2608.00123](https://arxiv.org/abs/2608.00123) (cs.CL; v1 2026-07-31, v2 2026-08-04) — **NEW**
- **Authors**: Yan Fang, Jialin Chen, Chun Gan, Hang Yu, Mingjun Nie, Yeyu Zhang, Fengxiang He, Ching Law
- **Institution**: Not stated on abstract page. Co-author Ching Law is associated with ByteDance/TikTok ads (tentative; single-source).
- **Abstract (faithful summary)**: LLM-native advertising embeds sponsored content directly into model responses, shifting the unit of sale from a fixed slot to a moment in an evolving conversation. Existing LLM ad auctions settle the winner within a single response but not the timing. With one native insertion per session, the stopping time depends on bids, coupling timing with allocation and breaking static truthfulness arguments. LLM-OSDA is a **dynamic cost-per-click auction** integrating Bellman optimal stopping, winner allocation, and envelope pricing. A **bid-independent LLM layer** estimates contextual click quality and renders the winning ad; bids enter only the committed auction mechanism. With an exact Bellman oracle, expected discounted-click allocation is monotone in each bid and the envelope payment makes truthful bidding weakly dominant in expectation. For deployment, a learned **StopNet** approximates Bellman action values; decisions differ from optimal only near the stopping boundary, and incentive loss is bounded by approximation error. On a simulated conversational ad corpus, LLM-OSDA improves net revenue **+11%** over the strongest fixed-timing baseline with comparable retention. Code: `github.com/2025Fang2025/llm-osda`. Submitted to AAAI 2027.
- **Key innovations**: (1) First auction mechanism where *when* to insert the ad is an optimal-stopping decision, not just *who* wins; (2) bid-independence of the LLM layer preserves incentive compatibility; (3) StopNet approximation with bounded incentive-loss guarantee.

### 3.3 Beyond the PPAD Hardness of Auto-bidding Auctions

- **arXiv**: [2608.01889](https://arxiv.org/abs/2608.01889) (cs.GT; submitted 2026-08-03) — **NEW**
- **Authors**: Li Chen, Jamie Morgenstern, Yuanyuan Yang
- **Institution**: University of Washington (high confidence)
- **Abstract (faithful summary)**: Computing certain autobidding equilibria is PPAD-complete in the worst case, yet advertisers running simple decentralized learning strategies converge quickly in practice. The authors show no contradiction: hardness requires atomicity and vanishes when the value distribution is non-atomic, as in real markets. They introduce **diffuse analysis**, a beyond-worst-case framework for equilibrium computation under general non-atomic distributions; the autobidding equilibrium becomes a separately monotone **generalized Nash equilibrium (GNE)**, for which they give the **first solver with last-iterate linear convergence** — hence polynomial diffuse complexity, matching observed convergence. The framework subsumes budget pacing and throttling equilibria when the payment rule is a convex combination of first- and second-price.
- **Key innovations**: (1) Explains worst-case hardness vs practical convergence via atomicity/non-atomicity; (2) diffuse-analysis framework; (3) first last-iterate-linear solver for the autobidding GNE.

### 3.4 Advancing Relevance Measurement with Vision-Language Models for Web-Scale Search

- **arXiv**: [2608.02446](https://arxiv.org/abs/2608.02446) (cs.IR; submitted 2026-08-03) — **NEW**
- **Authors**: Han Wang, Alex Whitworth, Pak Ming Cheung, Zhenjie Zhang, Krishna Kamath, Xi Chen, Roberto Konow, Kurchi Subhra Hazra
- **Institution**: Pinterest (high confidence — "Pinterest Search" deployment in abstract; RecSys 2026 Industry Track)
- **Abstract (faithful summary)**: Relevance evaluation is a guardrail alongside engagement in personalized search, but human annotation is expensive and slow. The paper presents a **VLM-based automated relevance-evaluation pipeline deployed in Pinterest Search** for online A/B experiments, rigorously validating alignment between VLM judgments and human annotations. VLMs provide reliable relevance measurement with far better evaluation efficiency, enabling expanded query sets, optimized sampling design, and assessment of more search experiences at scale — leading to higher-quality relevance metrics and **significantly reduced Minimum Detectable Effects (MDEs)** in online experiments.
- **Key innovations**: (1) Production deployment of VLM-as-judge for relevance (RecSys 2026 Industry); (2) human–VLM alignment validation methodology; (3) statistical payoff quantified via MDE reduction.

### 3.5 Algorithmic Collusion under Asynchronous Price Updating

- **arXiv**: [2608.01406](https://arxiv.org/abs/2608.01406) (econ.TH; submitted 2026-08-02) — **NEW**
- **Authors**: Ivan Conjeaud, Gaspard Abel, Argyris Kalogeratos
- **Institution**: ENS Paris-Saclay (high confidence)
- **Abstract (faithful summary)**: Studies how asynchrony in agents' updates affects algorithmic collusion. A continuous-time Bertrand duopoly model where two firms use **Q-learning** to set prices asynchronously, driven by a Poisson clock. Across three algorithm specifications, asynchrony **hampers collusion**, especially for stateless algorithms; when algorithms condition on the competitor's previous prices, sensitivity to asynchrony varies with the information they access. A collusion index plus automatic detection of reward-punishment schemes (comparing reactions to unilateral price cuts against untrained algorithms) measure strength. Regulatory implications for algorithmic pricing discussed.
- **Key innovations**: (1) First continuous-time treatment of asynchrony in algorithmic pricing; (2) reward-punishment scheme detection vs untrained-algorithm baseline; (3) differential asynchrony-sensitivity by information access.

---

## 4. Sequential Modeling & Time Series

### 4.1 CvLoss: Multivariate Time Series Forecasting Needs a Cross-Variable Loss

- **arXiv**: [2608.05742](https://arxiv.org/abs/2608.05742) (cs.LG; submitted 2026-08-06) — **NEW**
- **Authors**: Kuiye Ding, Yifan Hu, Hanchen Wang, Hao Xue
- **Institution**: University of New South Wales (UNSW) Sydney (high confidence)
- **Abstract (faithful summary)**: Future variables often co-evolve under shared system dynamics, but modern models mostly follow the Direct Forecasting (DF) paradigm with point-wise objectives that don't constrain cross-variable structure. The paper shows the DF objective is **mismatched** under cross-variable and lagged dependencies — an "objective gap." CvLoss is a plug-in structural regularizer that constrains forecast residuals on a **cross-variable graph**, penalizing inconsistent edge-wise residual differences over forecast patches to encourage consistency across synchronous and asynchronous interactions. Consistently improves competitive forecasting models and is compatible with a variety of forecasting backbones.
- **Key innovations**: (1) Identifies the objective gap in the DF paradigm; (2) graph-structured residual regularizer over forecast patches; (3) backbone-agnostic plug-in.

### 4.2 Multi-Objective Ranking for Live-Streaming: Balancing Fresh and Delayed Signals with Segment-Aware Targeting

- **arXiv**: [2608.04455](https://arxiv.org/abs/2608.04455) (cs.IR; submitted 2026-08-05)
- **Authors**: Xiaoyi Gu, Julia Tavares, Eder Santana, Carlos Mendoza-Cardenas, Nikita Mishra, Saad Ali
- **Institution**: Amazon / Twitch (high confidence — Twitch test named in abstract; RecSys 2026 Industry Track)
- **Abstract (faithful summary)**: Live-streaming recommendation faces sparse, delayed, concurrent user behaviors (watching, chatting, following, spending) with segment-dependent bias. Contributions: (1) a **delayed-window approach** extending feedback collection beyond immediate responses; (2) a **multi-model architecture** combining fresh and delayed signals plus a **segment-aware targeting module** optimizing ranking scores per user-lifecycle stage; (3) **Multi-gate Mixture-of-Experts (MMoE)** joint modeling of correlated targets, cutting parameters 41.9% vs independent models. Online A/B: **+0.09% DAV** (millions of added annual active-viewer days), **+0.56% capped ARPU** for highly engaged viewers, **+0.15% DAV** for newer/less engaged viewers via segment targeting, **+0.08% DAV** and **+0.27% new follows** from MMoE. Reproduced on Twitch's mobile live feed: **+1.12%** positive user-channel interactions.
- **Key innovations**: (1) Delayed-window feedback for sparse multi-behavior signals; (2) fresh + delayed dual-model + segment-aware targeting; (3) MMoE parameter consolidation at production scale.
- **Coverage note**: Also in [2026-08-06 arXiv Daily Digest](../2026-08-06/arxiv-daily.md) and [2026-08-06 arXiv Paper Check](../2026-08-06/arxiv-paper-check.md).

---

## 5. Games, Auctions & Multi-Agent

### 5.1 AV-AIVAT: 74× Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games

- **arXiv**: [2608.06362](https://arxiv.org/abs/2608.06362) (cs.GT; submitted 2026-08-06)
- **Authors**: Boning Li, Yu Chen, Longbo Huang
- **Institution**: Tsinghua University (high confidence)
- **Abstract (faithful summary)**: Deciding which of two agents is stronger means playing games until skill outweighs luck; fixed budgets either overpay or stop too early, while naive optional stopping invalidates confidence levels. AIVAT (action-informed value assessment) cuts variance via conditional mean-zero corrections (median **54×** across 15 LLM agent configs / 71,439 paired HUNL hands) but doesn't say when to stop. AV-AIVAT pairs AIVAT with continuously monitored **Confidence Sequences** — anytime-valid AIVAT; the online value model learns only from past games so no game scores its own correction. At nominal 95% and ±1 BB precision, raw outcomes need a median **74×** as many hands as AIVAT-corrected outcomes (AsympCS); exact finite-sample certification uses Empirical-Bernstein CS with a structurally established bound for Leduc hold'em, and descriptive HUNL EB-CS runs show median 1.37× stopping-time ratio. Separation of asymptotic screening from exact certification makes evaluation stop the moment evidence suffices and leaves a third-party-auditable verdict.
- **Key innovations**: (1) Variance reduction × anytime-valid stopping; (2) no self-scoring online value model; (3) two-tier (asymptotic screening / exact EB-CS certification) protocol.
- **Coverage note**: Also in [2026-08-07 arXiv Daily Digest](./arxiv-daily.md).

### 5.2 Humans Are More Diverse: Frontier LLMs Show Extreme Policies in Idealised AI Development Races

- **arXiv**: [2608.01193](https://arxiv.org/abs/2608.01193) (cs.AI; submitted 2026-08-02) — **NEW**
- **Authors**: Phu Hoa Pham, Duy Minh Dao Sy, Trung Kiet Huynh, Phu Quy Nguyen Lam, Chi Nguyen Tran, Minh Trung Le, Phong Hao Le, Dinh Nam Nguyen, Thien Ky Nguyen Dong, Elias Fernandez Domingos, Le Hong Trang, The Anh Han
- **Institution**: Teesside University (high confidence — The Anh Han's affiliation)
- **Abstract (faithful summary)**: An AI development race is a multi-agent safety dilemma: each company can develop slowly and safely, or move fast while risking the final reward. The authors study strategic safety behavior among LLM agents in 2–5 player repeated games, but gate behavior interpretation behind an **audit**: verify the game engine, test rule recall, state tracking, payoff calculation, and stability under equivalent task descriptions. Key findings: strong rule recall coexists with weak state tracking and payoff calculation; verified arithmetic and response-representation changes alter later actions even with fixed rules; across seven model endpoints, aggregate rates hide large differences in action sequences, opponent responses, and race-position responses; 3–5 player patterns are model-specific, not a single "added competitors" effect. Conclusion: multi-agent AI-race simulations need validity checks and trajectory-level analysis before outputs are called strategic, human-like, or safety-aware. Explicitly exploratory.
- **Key innovations**: (1) Audit-gated (validity-checked) behavioral interpretation of LLM agents in strategic games; (2) rule-recall vs state-tracking vs payoff-calculation dissociation; (3) cautionary evidence for LLM-based multi-agent safety simulations.
- **Institution note**: Uses `concepts/`-style caution — findings apply only to tested models, prompts, and decoding settings (exploratory).

---

## Cross-cutting trends

- **Generative ranking hits the serving wall / kills cascades** — Gryphon-v2 replaces a >15-model cascade at Yandex; OMEGA and SITA push generative/sequential rec toward target-aware, memory-augmented, compressible forms; LIME-Rec warns that cheap offline recoveries must be ruled out first.
- **LLM-native advertising becomes a mechanism-design problem** — LLM-OSDA makes ad insertion timing an optimal-stopping auction; auto-bidding theory (diffuse analysis) closes the gap between PPAD hardness and observed convergence.
- **RL training signals get finer and more aligned** — RRC (ranking-based rewards for generative RMs), LC-GRPO (train-inference-aligned flow rollouts).
- **Evaluation is becoming a research subject in itself** — anytime-valid stopping (AV-AIVAT), VLM-as-judge at Pinterest, recovery/audit tests (LIME-Rec), validity-gated agent simulation (Humans Are More Diverse).
- **Sequential modeling theory and practice both move** — CvLoss shows the DF objective is structurally mismatched for multivariate forecasting.

## Methodology & caveats

- Papers selected from the Aug 5–6, 2026 arXiv window across the requested domains (AI, LLM, recommendation, advertising, CTR, sequential modeling, games). Not exhaustive; ranked by novelty, industrial signal, and domain coverage.
- Institution/company attribution: high confidence where stated in the abstract (deployment/venue) or a well-known affiliation; **tentative** marks where only inferred from co-author affiliations (single-source). No affiliation should be treated as authoritative without checking the paper.
- 9 of 17 papers were already covered in 2026-08-05/06/07 digests; pointers given above. 8 are new to the wiki.
- arXiv export API returned HTTP 503/429 intermittently; metadata cross-checked against arXiv listing and abstract pages.
