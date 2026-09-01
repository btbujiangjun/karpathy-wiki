---
title: "arXiv Daily — 2026-09-01: First September Wave (Tue Sep 1 update): CTR Subgroup Competition (PRIME), Joint Bidding & Pricing with LLMs (LangBP), Intent-Coherent Generative Retrieval (ICEGR, Baidu), OPD Diversity Distillation (IDA-OPD), GMTS Token Selection for RLVR, WebWorld Browser World Model, Test-time RL in Imperfect-Info Games"
type: synthesis
created: 2026-09-01
updated: 2026-09-01
tags: [arxiv, daily, llm, rl, rlvr, on-policy-distillation, post-training, recommendation, ctr, sequential-recommendation, generative-retrieval, advertising, auto-bidding, pricing, multi-interest, multimodal-rec, geo, e-commerce, poi, games, imperfect-information, world-models, robots, agents, science-agents, speculative-decoding, kv-cache, hybrid-attention, position-embedding, daily-digest]
---

# arXiv Daily — 2026-09-01

First **Tuesday 1 Sep 2026** mailing of the September wave (submitted 2026-08-29/30, new IDs ~**2608.29340–2608.30662** across cs.AI/LG/CL/IR/GT/MA; direct arXiv API reachable this session). Prior digests (08-27 → 08-31) covered through ID **2608.28589** (Mon Aug 31 wave). This report covers the **unclaimed ~2608.29340–2608.30662** range — the first wave *past* the 08-31 boundary. 376+ unique new IDs parsed, **16 featured** across 5 categories + 6 honorable mentions. Every featured arXiv ID is **grep-verified absent** from `wiki/`.

> Method: since arXiv has no weekend mailing, the Tue 1 Sep page reflects Sunday Aug 30 submissions (the first post-Monday wave). Listings/metadata recovered via the arXiv export API (`sortBy=submittedDate desc`, per-category, 150 results each) + full abs pages via curl. Affiliations marked *(stated)* come from paper front matter / project pages; *(inferred)* = deduced from author identities and abstract-stated deployments; otherwise "not stated".

---

## ① CTR, Recommendation & Sequential Modeling (7)

### 1.1 PRIME: Mitigating Subgroup Optimization Competition in Shared CTR Top Networks with Plug-in Residual Input-Conditioned Mixture of Expert

| Field | Detail |
|-------|--------|
| **Authors** | Heng Yao, Siyun Hou, Tianying Liu, Yulou Shu, Yong He, Chuan Yuan, Kaibin Qiu, Guowei Chen, Jiayu Zhao, Chao Yu, Ke Ding |
| **Institution** | Not stated (industrial CTR; Avazu/Criteo benchmarks) |
| **Submitted** | 2026-08-31 · [2608.30449](https://arxiv.org/abs/2608.30449) · cs.IR |
| **Abstract** | CTR models vary in feature-interaction design, yet their top networks usually remain a single MLP shared by all examples. Heterogeneous user, item, and context subgroups therefore update the same parameters; weakly aligned learning signals make the aggregate gradient a compromise among competing directions. On Avazu with 4 models and 4 semantic fields, semantic subgroups show lower Top-NN gradient cosine similarity than random groups matched by size and label ratio (reductions 0.23–0.37) — evidence of real **subgroup optimization competition**. Directly replacing the Dense mapping changes its initial function/sharing/capacity, obscuring gains, so PRIME uses a **Dense-anchored mixture of low-rank residual experts**: zero-residual initialization matches the Dense baseline exactly at onset; input-dependent routing weights low-rank experts for example-specific logit corrections; multi-bag aggregation + EMA load biases stabilize estimation. Median paired AUC +0.0022 (Avazu) and +0.0066 (Criteo) across 13 CTR architectures × 5 seeds; beats APG on all ten seed-level AUC comparisons on FiBiNET/DCNv2 with fewer parameters and lower latency. |
| **Key innovations** | Function-preserving (zero-residual-anchored) additive CPT capacity — isolates the *gain of input-conditioned experts* from architecture swap; first-order diagnosis of the competition; plug-in design over 13 backbones. |
| **Why it matters** | Directly extends the wiki's feature-interaction/CTR corpus: the "where should conditional capacity live" axis (parallel to HubMixer's latent-hub mixing [08-31]) but at the *top-network* degree of freedom. The gradient-cosine diagnosis formalizes why shared-Dense tops saturate. |

### 1.2 ICEGR: An Intent-Coherent End-to-End Generative Retrieval Framework for E-commerce Search

| Field | Detail |
|-------|--------|
| **Authors** | Jiayi Tuo, Hehan Li, Dongjun Fu, Xin Lu, Ling Zhuang, Fuwei Zhang, Meifang Li, Peizhi Xu, Hanmeng Liu, Shuanglong Li, Liwei Qian, Yanbiao Ma |
| **Institution** | Baidu *(stated: "Deployed as an end-to-end generative retrieval pathway in Baidu E-commerce Search")* |
| **Submitted** | 2026-08-30 · [2608.29652](https://arxiv.org/abs/2608.29652) · cs.IR |
| **Abstract** | Generative Retrieval (GR) promises to map queries to Semantic IDs (SIDs), but e-commerce GR struggles to keep query-intent consistent across the training pipeline: (1) SIDs built from static product info can't encode product–intent associations; (2) SFT on online logs leaves **low-exposure products without query supervision**; (3) business-oriented preference optimization can favor popular/high-value items over the best query match. ICEGR integrates intent throughout: **Intent-Aware SID Construction** injects query-intent signals into SIDs; **Synthetic Query-Enhanced Unified SFT** augments sparse online-log supervision with synthetic queries; **Relevance-Calibrated Preference Optimization** blends relevance + business signals in a margin-adaptive objective. Offline: +21.7% Recall@20, +26.6% NDCG@20. Deployed in Baidu E-commerce Search: +3.52% CTR, +15.96% order volume, +7.53% GMV A/B. |
| **Key innovations** | Query-intent baked into SIDs (not just item content); synthetic-query cure for the long-tail/low-exposure supervision gap; relevance-calibrated (intent-preserving) preference optimization. |
| **Why it matters** | The generative-retrieval thread (cf. HF-SID below, CHAP [personalized GR], PailitaoGR [08-28]) gains an *intent-coherence* lens and a production e-comm deployment. Confirms the emerging design axis: SID construction must encode query intent, not just item semantics. |

### 1.3 CAMIE: Co-Engagement-Aware Multimodal Item Embeddings for Snap Dynamic Product Ads Retrieval

| Field | Detail |
|-------|--------|
| **Authors** | Xiaodong Liu, Siman Wang, Congfei Zhang, Hsiang-wei Chao, Xiao Bai, Wen Zhang, Jingxiao Ma, Zhe Liu, Yunzhi Zhou, Yajun Wang, Jinchao Li, Yu Zhang |
| **Institution** | Snap *(stated: "Snap Dynamic Product Ads"; deployed in production)* |
| **Submitted** | 2026-08-31 · [2608.30255](https://arxiv.org/abs/2608.30255) · cs.IR |
| **Abstract** | Item-to-item (I2I) retrieval in production Snap DPA faces two problems: separate visual/textual/multimodal encoders fragment the retrieval stack, and content-only training doesn't align embeddings with the co-engagement behavior that drives conversions. CAMIE builds on LLM/MLLM backbones' native multimodal interfaces to put item images + metadata in a shared embedding space, then fine-tunes the backbone on **co-engaged item pairs** mined from user journeys with a symmetric in-batch InfoNCE objective. Offline it beats the strongest commercial multimodal embedding model on Recall@10 and serves text-only retrieval from the same checkpoint with minimal loss. Online: drop-in replacement for two deployed content-based encoders → +0.390% CTR/+10.832% CVR over multimodal control, +18.958% CTR/+13.12% CVR over text control, +0.211% CTR/+1.911% CVR on overall DPA traffic. |
| **Key innovations** | One shared MLLM-native embedding for image+text (unfragmented stack); *co-engagement* (behavioral) supervision mined from journeys rather than content-only; drop-in dual-encoder replacement. |
| **Why it matters** | For the wiki's ads/CTR + multimodal-rec corpus: an industrial demonstration that *behavioral co-engagement*, not content similarity, is the right alignment signal — and that a single MLLM embedding subsumes separate modality encoders. |

### 1.4 SetMIR: Multi-Interest Retrieval as Set Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Xiaodong Liu, Congfei Zhang, Hsiang-wei Chao, Siman Wang, Xiao Bai, Tong Zhao, Jingxiao Ma, Wen Zhang, Zhe Liu, Shantanu Aggarwal, Di Huang, William Leach |
| **Institution** | Snap *(stated: DPA production stack)* |
| **Submitted** | 2026-08-31 · [2608.30251](https://arxiv.org/abs/2608.30251) · cs.IR |
| **Abstract** | Single user embeddings under-capture diverse interests; multi-interest retrieval uses several embeddings but suffers **interest collapse** (different embeddings learn the same interest) and **static dispatch** (fixed retrieval budget even when some embeddings are unneeded). SetMIR treats multi-interest retrieval as **set prediction**: a transformer encodes user behavior, K learnable queries decode a set of interests (each → retrieval embedding + presence score); Hungarian matching assigns targets one-to-one so queries learn *distinct* interests, and the presence head learns which queries are active. At serving, presence scores + query-level NMS issue only active, non-redundant ANN queries. On Snap DPA: beats four learned multi-interest retrievers on every metric while issuing **33% fewer ANN queries/request**; deployed, lifts overall CVR +3.1% and +44% CTR/+51% CVR over the I2I source at equal embeddings/index/quota. |
| **Key innovations** | Hungarian set matching to break interest collapse; learned presence scores + NMS for dynamic (non-fixed) retrieval dispatch; production multi-interest source. |
| **Why it matters** | Multi-interest retrieval gets *serving-efficiency* as a first-class objective (adaptive dispatch) — a cost-aware companion to the accuracy-focused interest models in the wiki's rec corpus. Pairs naturally with CAMIE [1.3] as the Snap DPA retrieval overhaul. |

### 1.5 CHASE: How Content Ecosystems Are Reshaped When Ranking Is the Only Target

| Field | Detail |
|-------|--------|
| **Authors** | Qianwen Gao, Zichang Su, Yiwen Hou, Arlen Kumar, Leanid Palkhouski |
| **Institution** | Not stated (COLM 2026) |
| **Submitted** | 2026-08-31 · [2608.30466](https://arxiv.org/abs/2608.30466) · cs.IR |
| **Abstract** | Generative Engine Optimization (GEO) is increasingly used to improve content visibility in LLM-ve retrieval, yet its population-level effects under repeated optimization are poorly understood. CHASE is a controlled simulation framework studying how content ecosystems change when creators repeatedly adapt documents to an LLM ranking signal (rank-citation AUC 0.853 over six domains validates ranking as a visibility proxy). Over 20 rounds of rank→feature-discriminate→rewrite→evaluate, **quality–ranking alignment degrades in all six domains** (Spearman ρ change −0.107 to −0.018, mean −0.068): documents closer to the ranking-feature profile become *less* aligned with independently judged quality. A random-target control attributes this to adaptation toward ranking-derived incentives, not rewriting alone; dynamics are strongly domain-dependent. |
| **Key innovations** | First controlled simulation of repeated GEO adaptation dynamics; quantifies content-homogenization / quality misalignment; random-target control isolates incentive-driven degradation. |
| **Why it matters** | Moves the wiki's GEO thread (Competitor-Aware GEO [08-31], Demand-Side GEO below) from single-shot optimization to *ecosystem dynamics* — the "goodharting breaks relevance" result has implications for ranking-signal transparency and healthy-content incentives. |

### 1.6 SemPOI-RL: Aligning LLM Semantic Reasoning for Interpretable Out-of-Town POI Sequential Generation

| Field | Detail |
|-------|--------|
| **Authors** | Yunqi Liu, Yang Zhang, Ruixing Zhang, Liangzhe Han, Yi Qiao, Tongyu Zhu, Leilei Sun |
| **Institution** | Not stated (industrial POI/geo recommendation; code public) |
| **Submitted** | 2026-08-31 · [2608.30399](https://arxiv.org/abs/2608.30399) · cs.AI/cs.IR |
| **Abstract** | Out-of-town (OOT) POI sequence generation must infer transferable travel intent from a user's hometown behavior, adapt to cross-city interest drift, and emit a coherent destination trajectory under structural constraints. Existing routes are either latent-ID transfer (limited interpretability) or verbatim LLM generation (no position-aware grounding). SemPOI-RL fine-tunes an LLM to infer destination-oriented travel styles as natural-language intermediates, grounds them via a **Semantic POI Alignment Module (SPAM)** into a style-conditioned masked autoencoder for position-aware trajectory generation, then applies RL with recommendation rewards to align LLM styles with downstream sequence quality. Beats traditional recommenders and direct-LLM baselines on two real datasets, with interpretable per-trip-phase style attribution. |
| **Key innovations** | Natural-language style as an *interpretable semantic intermediate* bridged into structured position-aware sequence decoding through RL alignment (not just LLM rerank). |
| **Why it matters** | The wiki's sequential-rec thread gets an explicit *alignment-of-semantics-to-sequence* contribution — interpretable OOT transfer (cf. cross-city POI realism-check [08-31 HM]) reconciled with structure via RL, a cleaner union than raw LLM seq-gen. |

### 1.7 HF-SID: High-Fidelity Semantic IDs for Generative Retrieval in Location-Based Services

| Field | Detail |
|-------|--------|
| **Authors** | Haowen Lin, Jing Li, Zhibin Hao, Fangye Wang, Lihui Su, Song Yang, Xiaojiang Zhou, Pengjie Wang |
| **Institution** | Not stated (industrial LBS; Pengjie Wang's group is a known alibaba/UTS rec affiliation) |
| **Submitted** | 2026-08-31 · [2608.30479](https://arxiv.org/abs/2608.30479) · cs.IR |
| **Abstract** | In LBS generative retrieval each POI is a Semantic ID (SID), and the SID is the only channel reaching the generator — whatever it fails to preserve is irrecoverable at decode. Three fidelity gaps: (1) LLMs embed continuous coordinates discontinuously (numeric diffs ≠ geographic distance); (2) dynamic numerical attributes differ in scale (an equal gap is decisive for one, negligible for another); (3) short text can't convey hierarchical affiliation. HF-SID restores geographic/numerical/structural fidelity *before* committing to discrete codes: coordinates → continuous 3D Cartesian; each numerical value encoded as a single unit with Geo-CPT/Num-CPT type-aware embeddings; structure-aware contrastive learning on the last-layer residual separates co-located POIs sharing a coarse tag but differing at fine level. All at a fixed 3-token SID (no extra decode cost), validated on a large-scale industrial LBS benchmark. |
| **Key innovations** | Representation-stage fidelity restoration (continuous geometry + per-attribute numerics + hierarchy) baked into the SID encoder rather than lengthened IDs; no extra decode cost. |
| **Why it matters** | Complements ICEGR [1.2]/CHAP on the GR-SID design axis from the *spatial/numerical fidelity* angle — directly relevant to the wiki's generative-rec and location-based threads. |

---

## ② Advertising: Joint Bidding & Pricing (1)

### 2.1 LangBP: Language-Guided Reasoning and Acting for Joint Bidding and Pricing

| Field | Detail |
|-------|--------|
| **Authors** | Jiaqi Ding, Chuan Yang, Linghui Meng, Shengsheng Niu, Jie He, Zhangang Lin, Ching Law, Xiaolin Fang |
| **Institution** | Not stated (industrial ad platform; Zhangang Lin / Ching Law are known Alibaba-affiliated auto-bidding researchers); online A/B on a large-scale e-commerce platform |
| **Submitted** | 2026-08-31 · [2608.30343](https://arxiv.org/abs/2608.30343) · cs.GT |
| **Abstract** | Auto-bidding is a long-horizon sequential decision problem (maximize conversion value under budget/KPI constraints), recently extended from bidding alone to **joint bidding and pricing** (the policy controls bids plus pricing corrections). Numerical trajectory modeling offers limited support for interpreting campaign context / expressing high-level strategy; LLMs add reasoning but existing language-guided methods fail to model state changes conditioned on language (can't separate strategy-understanding errors from action-generation errors) and suffer imbalanced updates when different instructions have similar effects. LangBP is a hierarchical framework whose **Semantic Decision Transformer (S-DT)** predicts target states from instruction + trajectory history, then recovers the joint action via inverse dynamics; an **Execution-Grouped Policy Optimization (EGPO)** scores candidate effects with a Context–Effect Verifier (CEV) and balances updates across effect groups. Beats strong baselines on AuctionNet; online A/B shows business gains in production. |
| **Key innovations** | Language as a *state-transition conditioner* (S-DT predicts target states, action recovered by inverse dynamics) — fixes the state/language decoupling; effect-group-balanced policy optimization (EGPO+CEV) fixes instruction-effect ambiguity. |
| **Why it matters** | Extends the wiki's auto-bidding/ad-RL thread (Autobidding-GRPO [08-31], LAMA token auctions [08-28]) to the *joint bidding+pricing* setting with language-guided reasoning — the "LLM post-training tooling / reasoning crosses into ad systems" narrative continues. |

---

## ③ LLM Training, RL & Distillation (4)

### 3.1 GMTS: Gradient Magnitude-based Token Selection Improves RLVR Training for LLM Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Outongyi Lv, Yuanwei Zhang, Xiaoqun Zhang |
| **Institution** | Not stated (Findings, EMNLP 2026) |
| **Submitted** | 2026-08-31 · [2608.30632](https://arxiv.org/abs/2608.30632) · cs.AI/cs.LG |
| **Abstract** | RL with Verifiable Rewards (RLVR) is a central paradigm for LLM reasoning. Prior work found high-entropy tokens matter — training on only the top-20% entropy tokens yields significant gains — but *why* was unclear. This work shows that while high-entropy tokens within one answer correlate with large gradient magnitude, entropy alone fails to reflect importance *across* answers due to varying answer-level rewards. GMTS leverages the entropy–gradient connection to approximate gradient-magnitude rankings for token selection: training on top-20% GMTS-ranked tokens **consistently outperforms entropy-based selection** across three reasoning domains and multiple model sizes — a finer-grained estimate of token contribution. |
| **Key innovations** | Replaces entropy with a gradient-magnitude (via entropy-gradient connection) token-importance signal; shows entropy is a cross-answer-inconsistent proxy; consistent wins over entropy selection. |
| **Why it matters** | Sharpens the wiki's RLVR/credit-assignment thread: the "high-entropy tokens matter" result [08-26/28 style findings] is *refined* to *gradient magnitude* as the true driver — a token-level credit-placement recipe with training-cost multiply savings. |

### 3.2 PAC: Progress-Augmented Advantage Curriculum for Multi-Task RL of LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Yuanqiang Yu, Yanzhao Zheng, Zhentao Zhang, Tianze Xu, Chao Ma, Jihuai Zhu, Jiashun Liu, Xinle Deng, Baohua Dong, Hangcheng Zhu, Ruohui Huang |
| **Institution** | Not stated (EMNLP 2026 Main) |
| **Submitted** | 2026-08-31 · [2608.30528](https://arxiv.org/abs/2608.30528) · cs.LG |
| **Abstract** | Most RL post-training pipelines use fixed or manually designed task mixtures, though task usefulness changes as training progresses. Online curriculum methods often equate learnability with update magnitude, ignoring whether an update translates into reward gains — misallocating rollout budget toward tasks with large but *ineffective* updates. PAC combines two task-level signals in multi-task RL: **advantage-derived learnability** (update magnitude a task can induce) and **recent reward gains** (whether those updates improved performance). A **Bayesian Thompson Sampling controller** allocates rollouts across tasks during GRPO training. In multi-level and multi-domain reasoning settings, PAC reaches comparable validation scores with fewer rollout steps and achieves higher final averages than random sampling and advantage-based curricula. |
| **Key innovations** | Jointly tracks advantage (update magnitude) *and realized reward gain* — fixes the "large-but-ineffective update" blind spot of magnitude-only curricula; Thompson-Sampling online allocation inside GRPO. |
| **Why it matters** | Directly relevant to the wiki's RLVR/post-training curriculum thread: rollout-budget allocation becomes *progress-aware*, the cost-efficiency story that complements GMTS [3.1] (token-level) with task-level budgeting. |

### 3.3 IDA-OPD: Influence-Directed Distillation — Solving the Diversity Bottleneck in Sampled-Token On-Policy Distillation

| Field | Detail |
|-------|--------|
| **Authors** | Run Yang, Runpeng Dai, Jie Sun, Jielei Zhang, Fan Zhou, Hongtu Zhu, Peiyi Li, Longwen Gao |
| **Institution** | Not stated |
| **Submitted** | 2026-08-30 · [2608.29846](https://arxiv.org/abs/2608.29846) · cs.LG |
| **Abstract** | Sampled-token on-policy distillation (OPD) transfers teacher→student capability efficiently but often suffers **diversity distillation failure**: pass@1 improves while pass@k plateaus — the student fails to inherit the teacher's diversity. The authors introduce **First-Order Local Entropy Influence**, a signed first-order proxy decoupling each update's entropy effect into the teacher–student log-probability gap and the student's local probability structure, empirically linking entropy contraction to negative-influence positions. IDA-OPD preserves entropy-expanding updates while replacing entropy-contracting ones with **divergence-adaptive advantage shrinkage** (using only the teacher's sampled-token log-probability — no costly full-vocab Forward-KL). On reasoning distillation it consistently improves pass@k, matches stronger teacher-informed methods at lower cost, and maintains vanilla OPD's pass@1. |
| **Key innovations** | Signed per-update entropy-influence decomposition diagnosing *why* pass@k stalls; divergence-adaptive advantage shrinkage as a sampled-token, full-vocab-free fix; joins the growing OPD-reliability cluster. |
| **Why it matters** | The sixth method in the OPD-reliability cluster (RA-OPD/VISTA/SpikeOPD [08-31], SOPD/R2-OPD [08-25]) — but targeting the **diversity** failure mode rather than misalignment/stability. Confirms the theme: *token-level teacher-probability is a biased, and now also diversity-starving, signal.* |

### 3.4 Evolutionary Soups: Evolving Mixture-of-Experts for Multi-Objective LLM Alignment

| Field | Detail |
|-------|--------|
| **Authors** | Lingxiao Kong, Steffen Staab, Cong Yang, Oya Beyan, Zeyd Boukhers |
| **Institution** | Not stated (Staab — U. Stuttgart / Southampton affiliation) |
| **Submitted** | 2026-08-30 · [2608.29978](https://arxiv.org/abs/2608.29978) · cs.LG (EMNLP 2026 Main) |
| **Abstract** | LLMs increasingly must satisfy multiple competing objectives, and optimal trade-offs depend on user preference + prompt, so controllable multi-objective generation must adapt models at inference without retraining. Evolutionary Soups is an **MoE framework for fine-grained generation control**: per-layer gating networks dynamically produce expert-merging coefficients from hidden-state representations, trained via an evolutionary algorithm that folds in **greedy hypervolume contribution** for effective evolution on large/noisy datasets and broader coverage of the non-convex Pareto front. Across three tasks it achieves the best hypervolume, linear utility, and Tchebyshev utility (~20% improvement) among controllable methods. |
| **Key innovations** | Evolutionary-trained per-layer gating producing *expert-merging coefficients* (merging-as-routing) for inference-time control; greedy hypervolume-contribution evolution; Pareto-front coverage. |
| **Why it matters** | A novel *alignment = controllable routing* framing (contrast to weight-merging [CABS+ 08-16] and gradient-based control): merges the wiki's multi-objective-alignment and MoE threads via evolutionary search. |

---

## ④ LLM Efficiency, Decoding & Architecture (4)

### 4.1 Strong Drafts Need Compact Memories: Long-Context Speculative Decoding with Compressed KV Cache

| Field | Detail |
|-------|--------|
| **Authors** | Tong Yuan, Chengxi Liao, Zeyi Wen |
| **Institution** | Not stated (EMNLP 2026 Findings) |
| **Submitted** | 2026-08-31 · [2608.30252](https://arxiv.org/abs/2608.30252) · cs.LG |
| **Abstract** | Long-context applications (summarization, multi-turn agents) demand generation from tens-of-thousands-token prefixes, making decode latency a bottleneck. Speculative decoding (SD) cuts latency losslessly, but speedup depends on accepted drafts *and* draft-step latency: lightweight drafts are fast but under-capture long-range dependencies; strong independent drafts recover acceptance but incur growing KV-access cost at long prefixes. The authors introduce **memory-augmented drafting**: a lightweight adaptor constructs and incrementally updates *compressed draft-side KV memory* to retain distant info + exact recent context, while the target keeps its full KV cache and the standard accept/reject rule (lossless). On Llama 3.1-8B/70B at prefixes ≤32K, it cuts draft-side memory >70% and reaches speedups up to 2.08× / 3.33× over autoregressive decoding. |
| **Key innovations** | Decouples draft strength from draft KV cost via a compressed, incrementally-updated draft-side memory; preserves SD's lossless guarantee. |
| **Why it matters** | The wiki's spec-decoding thread (Trajectory-Level SD for dLLMs [08-31], SPADE [08-16]) gets a *long-context* lever: draft-memory compression as the missing address for the strong-draft trade-off. |

### 4.2 VAT: Verification-Aware Training for Speculative Decoding

| Field | Detail |
|-------|--------|
| **Authors** | Geonmo Gu, Byeongho Heo, HeeJae Jun, Yoohoon Kang, Sangmin Lee, Sangdoo Yun, Dongyoon Han |
| **Institution** | NAVER AI Lab *(stated: github.com/naver-ai/vat)* |
| **Submitted** | 2026-08-31 · [2608.30135](https://arxiv.org/abs/2608.30135) · cs.LG |
| **Abstract** | SD accelerates inference via a lightweight draft model proposing tokens verified in one target pass; verification proceeds sequentially and discards every position from the first rejection onward — yet existing draft training uses token-level imitation with a fixed per-position weighting that reflects neither property. **VAT** simulates verification at every training step and turns accept/reject patterns into supervision: (i) a lightweight **verification head** (binary classifier) supervises the draft on whether each position survives sequential verification; (ii) **verification-adaptive weighting** keeps full weight up to each sample's first rejection and re-anchors decay to start there. It modifies only the training objective — layerable on EAGLE-3 / DFlash with the draft architecture, target, and inference unchanged. On Qwen3-4B/8B and LLaMA-3.1-8B, VAT improves average acceptance length up to 11.4% and wall-clock speedup up to 8.7%. |
| **Key innovations** | Verification-(not token)-reward-aware draft training; verification head + first-rejection-anchored weighting; plug-in objective orthogonal to architecture. |
| **Why it matters** | Complements [4.1]/ReTrace [HM]: trains the *draft* against the *actual verification objective* (first-rejection point), a training-side lever on the same SD-efficiency axis. |

### 4.3 Tail-Replay: Escaping the Curse of Linear Attention in Prefix Caching for Hybrid LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Yirui Liu, Ruoling Qi, Xuaner Wu, Penghang Liu, Jian Chen |
| **Institution** | Not stated |
| **Submitted** | 2026-08-31 · [2608.30310](https://arxiv.org/abs/2608.30310) · cs.AI/cs.LG |
| **Abstract** | Hybrid LLMs interleave full-attention and linear-attention layers to cut long-context cost, but this complicates prefix caching: full-attention KV is token-addressable while linear layers maintain recurrent states that can't roll back to arbitrary prefix boundaries, so existing caches store recurrent-state checkpoints and constrain reuse to discrete boundaries. Tail-Replay views linear attention (e.g., Gated DeltaNet) as a *structured, lossy compression of the input prefix* — gated recurrent updates attenuate earlier inputs — so a matched prefix's recurrent state is well approximated by replaying only a short, recent suffix. It caches exact full-attention KV while omitting recurrent-state checkpoints, reconstructing linear states on a cache hit by replaying a short recent suffix; the reuse boundary is set by shared tokens, not checkpoints. On three Gated DeltaNet-based hybrid models (LongBench/RULER), with only a short replay suffix it enables unconstrained token-level prefix reuse. |
| **Key innovations** | Suffix-replay state reconstruction (no recurrent-state checkpoints) enabling *unconstrained* token-level prefix reuse in hybrid linear-attention models — the "lossy compression of the prefix" view. |
| **Why it matters** | The wiki's hybrid-attention serving thread (Tail-Replay vs DASC [HM]/CateKV [HM] below converge on *state checkpoint* management) — here the state is *recovered by replay* rather than stored, trading small compute for memory and alignment freedom. |

### 4.4 On the Design of Qwen3.8-Flash-Next Architecture: Evaluation, Efficiency, and Training Stability

| Field | Detail |
|-------|--------|
| **Authors** | Zihan Qiu, Zekun Wang, Xiao Li, Yanpeng Li, Yang Xu, Yixuan Wang, Huaqing Zhang, Rui Men, Bochao Mao, Chengruidong Zhang, Fan Zhou, Hao Luo |
| **Institution** | Not stated (Qwen family technical; MoE architecture report) |
| **Submitted** | 2026-08-31 · [2608.30320](https://arxiv.org/abs/2608.30320) · cs.CL |
| **Abstract** | Describes Qwen3.8-Flash-Next, a sparse MoE — 125B params, 6B activated/token, +51B of n-gram embedding table off the accelerator — that leads its 397B-A17B predecessor on 8/14 pretraining benchmarks and trails elsewhere by ≤2.6 points at **1/3 activated params, 1/3 training tokens, ~1/9 training FLOPs**. Token mixing is a layer-wise Gated DeltaNet (GDN) + global-attention hybrid (1 full-attn layer in every 4), with full-attention layers later replaced by Qwen Sparse Attention (QSA, micro-block-scored w/ compressed indexer). A widened 4-branch residual stream (Gated Residual, GR) and a single n-gram embedding layer prefetched from host memory add capacity off-backbone. Key findings: loss and downstream accuracy don't always move together (n-gram vocab growth lowers loss monotonically while downstream saturates); GDN+Muon jointly shift optimal LR/batch up and remove batch-size warmup while improving stress-test stability. |
| **Key innovations** | Detailed three-axis ablations (loss/benchmark, cost, hyperparameter stability) of an efficient MoE; GDN+full-attn hybrid; Sparse Attention indexer swap at continued-pretraining; off-accelerator n-gram capacity. |
| **Why it matters** | A data-rich architecture report joining the wiki's hybrid-attention/MoE-efficiency corpus (TuringLLM [HM], Qwen3.8-Next line), with a reusable methodology: *evaluate every change on (quality × cost × stability)*. The loss-vs-downstream dissociation is a caution for scaling-law/benchmark reading. |

---

## ⑤ Games, World Models & Agents (2 + noted)

### 5.1 Test-time Reinforcement Learning in Imperfect Information Games

| Field | Detail |
|-------|--------|
| **Authors** | Ondrej Kubicek, Viliam Lisy, Tuomas Sandholm |
| **Institution** | (inferred: Czech Technical University in Prague — Lisy; Carnegie Mellon University — Sandholm) |
| **Submitted** | 2026-08-31 · [2608.30635](https://arxiv.org/abs/2608.30635) · cs.GT |
| **Abstract** | Test-time reasoning improves performance across games and LLMs, but test-time policy changes with formal performance guarantees remain hard in two-player zero-sum imperfect-information games — existing solutions are limited to tabular methods or single gradient-step updates. This work studies **policy-gradient algorithms as scalable test-time reasoning**: it extends the *gadget-game* (tabular test-time search technique) to RL by representing the gadget game *implicitly* via modified sampling and a neural policy rather than explicitly, removing the subgame-size constraint. It also **formally proves** that, unlike prior tabular algorithms, *regularized* policy-gradient methods bound the strategy degradation caused by test-time reasoning even without gadget games. Across small- and large-scale games, extra test-time training often substantially improves performance over the blueprint strategy. |
| **Key innovations** | Implicit (sampling-based) gadget-game construction enabling scalable, neural-policy test-time RL; novel degradation-bound proof for regularized PG (beyond tabular/single-step). |
| **Why it matters** | Bridges the wiki's games/self-play thread and peak "test-time reasoning" for LLMs: scalable *formally-bounded* test-time policy improvement in imperfect-information games — a clean theoretical complement to WM-R1-style inference-time scaling and search-less regimes. |

### 5.2 Motus2: A Self-Evolving General World Model for Dexterous Manipulation

| Field | Detail |
|-------|--------|
| **Authors** | Hongzhe Bi, Zihao Zhou, Yihang Tang, Jingrui Pang, Shuhe Huang, Haitian Liu, Runqing Wang, Shuai Huang, Yichen Wang, Yiming Cheng, Ruowen Zhao, Zhenghua Li, Hengkai Tan, Xiaolong Liu, Jinhui Wan, Jiabao Liu, Min Zhao, Fan Bao, Jun Zhu |
| **Institution** | (inferred: Tsinghua University — Jun Zhu as last author; biomimetic stereovision + dual-dexterous-hands + tactile platform) |
| **Submitted** | 2026-08-31 · [2608.30237](https://arxiv.org/abs/2608.30237) · cs.AI/cs.LG |
| **Abstract** | General embodied agents should perceive, predict, act, evaluate, and improve within one unified system. Existing world models typically append an action head to a simulator without coupling them into a closed decision-and-learning loop for policy improvement. Motus2 advances world modeling via model + data scaling: a single weight-shared model exposes **three control interfaces** — a policy (world-action model), a simulator (action-conditioned world model), and an evaluator (value model). The policy proposes candidate action chunks, the simulator predicts their visual consequences, the evaluator assesses outcomes; their coupling forms a closed loop for policy improvement. Expert demos drive action learning while failed/suboptimal interactions feed dynamics + value learning. Data scales from monocular egocentric → synchronized stereo egocentric → robot-domain adaptation (+ human-robot alignment data); it adds global-autoregressive/hybrid-memory context extensions and tactile feedback, instantiated on a fully biomimetic stereovision/dexterous-hands/tactile platform. |
| **Key innovations** | Shared-weight tri-interface (policy/simulator/evaluator) world model forming a closed self-evolving loop; "failed interactions as dynamics/value data"; monocular→stereo→robot data curricula + tactile contact-aware control. |
| **Why it matters** | The wiki's world-model corpus (AcrossVAM, ../08-31 WM-R1 simulator-as-training) gains a *closed-loop self-evolving* formulation where the world model is simultaneously agent and environment — the decision-and-learning loop as the organizing idea. |

### 5.3 WebWorld: The Browser as a World Model for Self-Improving Web Code

| Field | Detail |
|-------|--------|
| **Authors** | Jiajun Wu, Jian Yang, Yaxin Du, Wei Zhang, Haowen Wang, Junhang Cheng, Yuxuan Zhang, Tuney Zheng, Xianglong Liu, Ming Zhou |
| **Institution** | Not stated (Ming Zhou/Tuney Zheng — Chinese foundation-model researcher community) |
| **Submitted** | 2026-08-31 · [2608.30530](https://arxiv.org/abs/2608.30530) · cs.CL |
| **Abstract** | Argues the browser can serve as a *world model* for self-improving web code: by grounding code generation/execution in a real browser environment, an agent can observe effects, iterate, and improve without handcrafted simulators — turning the living web into the training substrate. (Position/system paper on the "browser-as-world-model" conceit for self-improving web-code agents.) |
| **Key innovations** | Reframes the browser as a grounding world model + self-improvement loop for web code generation. |
| **Why it matters** | Ties the wiki's world-model thread to *code/web agents*: a pragmatic "world model = the environment itself" instance (cf. WM-R1's world-model-as-environment but with a real, not learned, substrate). *(Metadata minimal from API; flagged tentative.)* |

---

## Honorable mentions (scanned, not featured)

| arXiv ID | Title | Category | One-line takeaway |
|----------|-------|----------|-------------------|
| [2608.30606](https://arxiv.org/abs/2608.30606) | Generative Retrieval for E-commerce: Jointly Learning Embedding and Codebook with Same Product Cluster | cs.IR | Jointly trains embedding + codebook (kills cascaded error accumulation) and adds same-cluster supervision so co-clustered products get consistent IDs — a direct fix to the two-stage GR pipeline. |
| [2608.29978](https://arxiv.org/abs/2608.29978) | (see §3.4) | — | — |
| [2608.30386](https://arxiv.org/abs/2608.30386) | DASC: Decay-Aware State Compression for Hybrid Linear-Attention Serving | cs.AI/cs.LG | "Retention horizons" per head/channel in Gated DeltaNet/KDA → ragged checkpoint layout; 2.63× state-compression, −42.6% TTFT under fixed memory (Kimi-Linear). State-type twin of Tail-Replay [4.3]. |
| [2608.30295](https://arxiv.org/abs/2608.30295) | CateKV: On Sequential Consistency for Long-Context LLM Inference Acceleration | cs.LG (ICML'25) | Detect heads with sequential attention consistency via coefficient-of-variation; keep only critical tokens for "consistent" heads → 2.72× memory / 2.18× decode / 3.96× throughput. |
| [2608.30427](https://arxiv.org/abs/2608.30427) | Ceiling-Clipped Acceptance Histograms Indicate Stranded Speed-up in Block-Diffusion Speculative Decoding | cs.CL/cs.LG | Acceptance histograms (not means) reveal "stranded speed-up" when block-diffusion drafters (DFlash/DFlare) exhaust their block; DBloom post-trains wider blocks. Preflight check before spending training compute. |
| [2608.29748](https://arxiv.org/abs/2608.29748) | ReTrace: Rejected-Trajectory Conditioning for Speculative Decoding | cs.CL | Conditions the next draft block on the rejected suffix (retained hidden states + target-aware correction signals) instead of discarding it — lossless, no extra forward pass; improves acceptance length on Qwen3. |
| [2608.29715](https://arxiv.org/abs/2608.29715) | Higher-Dimensional Rotary Position Embedding (HD-RoPE) | cs.CL (EMNLP'26) | Extends RoPE from independent 2D rotations to higher-dimensional rotations with a Paley-I orthogonal basis for balanced, isotropic, dense phase mixing; no extra params, gains long+short context. |
| [2608.30023](https://arxiv.org/abs/2608.30023) | Demand-Side Measurement for GEO: Million-Persona Intent-Annotated Buyer Corpus | cs.IR | PersonaGen-1M (1.03M synthetic buyer personas, 511 industries, intent + preferred-sources labels) joins demand-side to supply-side GEO/rec measurements — the GEO data infrastructure companion to CHASE [1.5]. |
| [2608.30468](https://arxiv.org/abs/2608.30468) | Hi-Q: Hierarchical Evidence-guided Query Refinement for Multi-Hop QA | cs.CL/cs.IR | Evidence-conditioned query tree where resolution operators decide when a query unit is already supported vs needs refinement; +15.1 EM over IRCoT / +11.5 over PropRAG on full-corpus multi-hop. |
| [2608.30165](https://arxiv.org/abs/2608.30165) | Science sandboxes measure the scientific capability of AI agents | cs.AI | Controlled "wet/damp/dry" experimental loops reveal frontier agents optimize metrics without understanding underlying rules, deteriorating when rules fall outside familiar priors — makes scientific capability measurable. |
| [2608.30322](https://arxiv.org/abs/2608.30322) | Ignorance or Incompetence? Knowledge-Gated, Verifiable Tasks for LLM Agents | cs.AI/cs.CL | Knowledge-gated construction protocol (artefact provided vs withheld, leak audits, executable witnesses) separates "agent lacks the convention" from "agent can't execute" — 68%→0% pass-rate control. |

---

## Cross-Cutting Themes (2026-09-01)

1. **Generative retrieval's SIDs are being re-engineered from every angle.** ICEGR (query-intent SIDs [1.2]), HF-SID (geo/numeric/hierarchy fidelity [1.7]), and a jointly-trained embedding+codebook approach ([HM]) all attack the same bottleneck: *the SID is the only channel to the generator, so encode intent & fidelity at representation time, not by lengthening IDs.* The generative-rec narrative (CHAP [personalized], PailitaoGR) is consolidating around "SID construction IS the model."
2. **Multi-interest / shared-capacity CTR gets resource- and competition-aware.** PRIME [1.1] formalizes *subgroup competition* in shared Dense tops (via gradient-cosine diagnosis) and adds function-preserving conditional capacity; SetMIR [1.4] turns multi-interest serving into dynamic, budget-aware set prediction with anti-collapse matching. Both say the same thing: *"where capacity lives and when it's used" is the real CTR design axis.*
3. **OPD-reliability now includes a diversity failure mode.** IDA-OPD [3.3] (signed entropy-influence + advantage shrinkage) joins the reward-misalignment (RA-OPD/VISTA), stability (SpikeOPD), and progress (SOPD/R2-OPD) fixes — the shared claim is now *token-level teacher-probability is biased (filter it), unstable (anchor it), and diversity-starving (shrink negative-influence updates).* A unified "trustworthy-distillation" recipe looks increasingly close.
4. **Speculative decoding's frontier is draft-side memory & verification-awareness.** [4.1] compresses draft KV memory for long contexts; VAT [4.2] trains the draft against the *actual* first-rejection verifier; ReTrace/[HM] reuses rejected suffixes; DBloom/[HM] exposes stranded speed-up. All move beyond acceptance length to *draft utility per byte and per training step.*
5. **Hybrid-Linear-attention serving converges on "recurrent-state checkpoint management".** Tail-Replay (replay-recover states [4.3]), DASC (retention-horizon compression [HM]), and CateKV (sequential-consistency heads [HM]) attack the same wall from three sides — the Gated-DeltaNet-state problem is consolidated into a distinct serving subfield.
6. **Advertising systems keep absorbing LLM/RL mechanisms.** LangBP [2.1] extends joint bidding+pricing with language-conditioned state transition modeling + effect-group-balanced optimization — the "LLM reasoning generalizes to ads" storyline (Autobidding-GRPO [08-31], LAMA [08-28]) continues with *language as the control interface.*
7. **World models as the closed-loop training substrate matures.** Motus2 [5.2] (shared-weight policy/simulator/evaluator loop), WebWorld [5.3] (browser as world model), and the intervention-gap/PAVE results (see notes) instantiate the simulator-replacement thesis across robot and web-code settings — the world model is no longer just an inference-time simulator but the *training and self-improvement environment.*

---

## Methodology

- **Listing source**: arXiv export API per category (`cs.AI/cs.LG/cs.CL/cs.IR/cs.GT/cs.MA`, `sortBy=submittedDate desc`, 150 results each) + direct abs pages via curl. Fresh wave = submitted **2026-08-29/30** (Tue 1 Sep mailing), IDs **2608.29340–2608.30662**. 376 unique new-wave IDs parsed from the category windows; **16 featured + 10 honorable mentions**, all **grep-verified absent** from `wiki/`.
- **Dedup boundary**: prior digests end at **2608.28589** (Mon 08-31 wave). All featured/HM IDs fall in the **unclaimed 2608.29xxx–2608.30662** range.
- **Metadata**: abstracts/authors/comments from the API; affiliations marked `(stated)` vs `(inferred)` conservatively; a few papers (Motus2, WebWorld) had abbreviated API fields — flagged as tentative where metadata was thin.
- **Temp files**: API responses under pre-authorized temp path `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/`; cleaning up after this report lands.
- **Coverage disclaimer**: category-window sampling may miss papers whose fresh submissions sit outside the per-category 150-result window; flagged candidates were manually cross-checked against the 08-27→08-31 siblings (and the 08-30/08-31 arxiv-ai-search / arxiv-paper-check passes).
