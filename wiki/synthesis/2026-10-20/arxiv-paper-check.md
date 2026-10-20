---
title: ArXiv Paper Check - 2026-10-20
type: synthesis
created: 2026-10-20
updated: 2026-10-20
sources: []
tags: [arxiv, ai, ctr, click-through-rate, recommendation, advertising, papers, daily]
---

# ArXiv Paper Check - 2026-10-20

Quick scan of new submissions in AI and CTR-related areas from the last 24 hours (arXiv block announced 2026-10-19/20; newest v1 timestamps `2026-10-19T04:00Z` – `2026-10-19T08:07Z`).

**Harvest**: `export.arxiv.org/api/query` over (a) `cat:cs.IR OR cat:cs.LG OR cat:cs.AI` sorted by submission date, (b) `abs:"click-through" OR abs:"CTR" OR abs:"recommender"`, (c) `cat:cs.IR AND (abs:"CTR" OR abs:"click-through rate" OR abs:"ranking")`, (d) `abs:"click-through rate" OR abs:"CTR prediction" OR abs:"ad ranking" OR abs:"ad recommendation"` — all deduped and grep-checked against `wiki/`.

**Headline**: **CTR-prediction lane is EMPTY again** — no new `click-through rate` / `CTR prediction` modeling paper in this window (continues the October streak tracked in [[ctr-scaling-landscape]]). Ads/rec-adjacent yield = 2 fresh + 2 already claimed by sibling `arxiv-daily` 2026-10-20. AI lane is strong on **search-agent RL credit assignment**, **KV-cache/decoding efficiency**, and **agent reliability audits**.

---

## Selected Papers

### CTR / Recommendation / Advertising

#### 1. CATH: Learning Complementary Agent Groups via Task Hypergraphs for Next-POI Recommendation with Missing Modalities
- **Authors**: Jinze Wang, Yuze Liu, Liang Yuan, Gaoyuan Du, Xiaohang Xu, Yong Xiang, Jiong Jin
- **ArXiv**: [2610.25801](https://arxiv.org/abs/2610.25801)
- **Category**: cs.IR
- **Key contribution**: Selects *groups* of LLM agents with distinct processing roles (task hypergraph nodes; hyperedges = selected group + analysis goal) to handle POI recommendation when text/images are missing. Policy picks members conditioned on request/task/already-selected agents; a shared ranking head turns candidate states into corrections to a fixed base ranking, trained by supervised ranking then cost-aware policy optimization. **+8.4–9.1% relative NDCG@20** over HyperAgent4POI on Gowalla-CA / Foursquare-NYC / TKY under natural missingness.

#### 2. A Cue's Hidden Price: Auditing Seller Influence on AI Shoppers
- **Authors**: Felix Buecheler, Gerardo Berbeglia, Mingyu Guo
- **ArXiv**: [2610.25843](https://arxiv.org/abs/2610.25843)
- **Category**: cs.AI
- **Key contribution**: Generative Engine Optimization (GEO) auditing that *prices* seller cues (badges, endorsements, framing) in money rather than choice rate — raises the cued product's price until it wins 50% of the time ("price-equivalent"). **113,472 trials × 7 models × 2 categories**; choice-rate audits under-resolve seller influence because strong cues saturate. First PE audit of a decision-native model (Jev): resists most cues but is susceptible to the strongest social-proof claims. Directly relevant to ad-cue measurement as AI shoppers become a shopping surface.

> **Cross-referenced, not re-featured** (already covered by [[arxiv-daily]] 2026-10-20): **MAPS** `2610.25748` (Kuaishou multi-agent script-driven video ads; online A/B **CTR +2.87%**, CVR +2.74%, ARPU +9.85%) and **OneChord** `2610.25805` (semantic-ID rec, "distill what you rank"; Recall@5 +6.30% / NDCG@5 +7.12% avg vs strongest baseline, 1.04–1.18× speedup).

### AI / LLM

#### 3. ClueFlow: Learning Long-Horizon Search through Attributed Research-State Transitions ★
- **Authors**: Yicheng Wang, Wentao Tan, Yidan Huang, Yifei Liu, Qiong Cao
- **ArXiv**: [2610.25980](https://arxiv.org/abs/2610.25980)
- **Category**: cs.AI
- **Key contribution**: Builds **Source–State–Final attribution chains** connecting evidence-acquiring browser actions → Evidence/Candidate updates → final answer. Attribution guides both SFT (which decisions get supervised, in original context) and Turn-PPO (outcome advantages credited along the chains). Transition-level validation recovers useful supervision from trajectories with *wrong* final answers. **BrowseComp 60.0% / BrowseComp-Plus 72.0%** (Qwen3.5-35B-A3B); attribution-guided SFT matches all-turn exact-context SFT at **~30% of training tokens**; attribution-guided PPO beats outcome-only PPO by **+4.1 pp**.

#### 4. Correctness-Dependent Asymmetric Target Distributions for Self-Distillation Policy Optimization (APSD)
- **Authors**: Suwan Yoon, Seongryong Jung, Changhee Lee
- **ArXiv**: [2610.25973](https://arxiv.org/abs/2610.25973)
- **Category**: cs.LG / cs.AI / cs.CL
- **Key contribution**: Directly matching a feedback-conditioned self-teacher damages correct rollouts and under-corrects incorrect ones. APSD **interpolates** student↔teacher on correct rollouts (preserve success) and **extrapolates** beyond the teacher on incorrect ones (strengthen correction), analyzed via divergence decomposition, reverse-KL barycentric geometry, and gradient flow through student-dependent targets. **Matches SDPO performance with 2.6× fewer training steps** across Qwen3 scales under RLVR and rich-feedback settings.

#### 5. GLOBE: Geometry-Led Online Behavioral Early Exit via Unit-Sphere Trajectories
- **Authors**: Xinyue Peng, Zhenlin Liang, Meng Cai, Hua Wang
- **ArXiv**: [2610.25970](https://arxiv.org/abs/2610.25970)
- **Category**: cs.AI / cs.CL
- **Key contribution**: Training-free online CoT termination. Each completed reasoning segment is embedded as a point on a unit sphere; a trial branch emits short trial answers (confidence-gated), and a trajectory phase stops the stream when the semantic path repeatedly reverses direction with little net progress. **−49.7% output tokens and −51.0% active E2E wall time** across two models on five benchmarks, at a five-task average of 80.58% — comparable to full CoT. Serving-cost angle for any CoT-heavy ranking/inference stack.

#### 6. The KV-Surgeon: Compensation-Aware Offline KV-Cache Compaction
- **Authors**: Moritz Wagner, Christophe Roux, Max Zimmer, Sebastian Pokutta
- **ArXiv**: [2610.25933](https://arxiv.org/abs/2610.25933)
- **Category**: cs.LG / cs.AI
- **Key contribution**: Existing offline KV compaction scores entries independently, ignoring that softmax renormalization couples all decisions. KV-Surgeon derives a **quadratic surrogate with closed-form joint greedy removal + compensation** within retained entries, fit on calibration data. Advances the cost–accuracy Pareto frontier for dense and MoE models 4B–30B on QuALITY / LongHealth / Long Code Arena; at **50× compaction, +up to 4 pts QA accuracy** over attention matching (SOTA) at comparable cost, plus a 2/5-cost faster variant.

#### 7. OrderGPT: Generation Order as a Learnable Modeling Choice
- **Authors**: Chenhe Yang, Yuhuan Lyu, Tianyang Hu
- **ArXiv**: [2610.25949](https://arxiv.org/abs/2610.25949)
- **Category**: cs.AI / cs.LG
- **Key contribution**: Frames left-to-right autoregression and masked diffusion as two endpoints of a single **generation-order axis**, and learns a task-level order with no canonical-order supervision: random reveal prefixes produce recurring attention patterns → reciprocal dependency graph → spectral teacher → continuous priorities predicted by a lightweight OrderMLP inside one training run. Recovers near-L2R in language, anatomically organized factorizations on human pose, coherent field grouping on tabular data; improves downstream metrics in all domains. Code: github.com/Chenhe-yang/OrderGPT.

#### 8. Claim Laundering: When Agent Decision Models Trust Records Over Reality
- **Authors**: Tina Khezresmaeilzadeh, Seyedarmin Azizi, Erfan Baghaei Potraghloo, Mehdi Kamal, Massoud Pedram
- **ArXiv**: [2610.25947](https://arxiv.org/abs/2610.25947)
- **Category**: cs.AI
- **Key contribution**: Paired states independently varying observation vs logged action vs explicit success claim, across Android / ALFWorld / WebShop. In **all 12 configurations** (4 decision models × 3 domains), records dominate observations: after claimed-but-failed steps, models still stop/advance/purchase in **53–100%** of cases. Yet evidence exists internally — linear probes separate success from failure (AUROC 0.77–1.00); activation patching shows records gain influence in later layers. **EVIGATE**, an intermediate-layer veto needing no extra forward pass (+0.04–2.0% latency), lifts task success by **+18.7 pts** (ALFWorld), +5.0 (WebShop), +5.1 (phone simulator). Important reliability caveat for any tool-using/agent pipeline.

#### 9. Keep the Lineages Alive: Diversity-Preserving SMC for Diffusion LLM Decoding (LP-SMC)
- **Authors**: Minoo Ahmadi, Seyedarmin Azizi, Mehdi Kamal, Massoud Pedram
- **ArXiv**: [2610.25932](https://arxiv.org/abs/2610.25932)
- **Category**: cs.LG / cs.AI / cs.CL / stat.ML
- **Key contribution**: Multinomial resampling in inference-time SMC for diffusion LLMs duplicates high-weight particles and silently destroys lineages — and **ESS resets to max, hiding the loss**. LP-SMC combines Chopthin resampling (bounds max/min weight ratio, carries unequal weights forward) with an input weight floor so low-early-weight lineages can recover. Raises oracle coverage by **+1.8 to +25.6 pts** in every setting and end-to-end accuracy in **11 of 12** settings (up to +7.9 on LLaDA-1.5, +18.3 on Dream-7B); gain persists under an external reward model → diversity preservation and reward guidance contribute separately.

#### 10. Productive State-Space Exploration for Multi-turn RL in LLM Agents
- **Authors**: Mohammed Haroon Dupty, Yong Liang Goh, Song Guo, Wee Sun Lee
- **ArXiv**: [2610.25957](https://arxiv.org/abs/2610.25957)
- **Category**: cs.AI / cs.LG
- **Key contribution**: Diagnoses why multi-turn LLM agents stall — high-confidence unproductive actions violate environment preconditions (state representation ↔ environment dynamics mismatch) and produce cycles. Proposes conditional state-space exploration balancing task completion with intrinsic information-seeking, plus an intrinsic reward that **penalizes actions whose observation duplicates prior state memory** (no general information-theoretic measure needed). Substantially reduces invalid actions and repetitive loops.

#### 11. Behavioral Probes for Information Flow in LLM Swarms
- **Authors**: Junhui Chen, Yu Zhang, Lantian Li, Dong Wang
- **ArXiv**: [2610.25966](https://arxiv.org/abs/2610.25966) — **Accepted at NeurIPS 2026**
- **Category**: cs.MA / cs.AI
- **Key contribution**: Repurposes External Context Score (ECS) and Parametric Knowledge Score (PKS) — originally hallucination metrics — as probes of information flow inside LLM swarms. ECS rises with input relevance and separates useful multi-source contributions; PKS falls as informative context accumulates. Probe-guided node pruning cuts redundant communication/tokens; probe-guided reasoning-path search beats utility-only structure optimization. Makes swarm internals observable without changing the utility objective.

#### 12. CXBench: A Benchmark for Process-Compliant LLM Agents in Regulated Customer-Experience Workflows
- **Authors**: Boxi Yu, Yuzhong Zhang, Zhenfeng Su, Linfu Xi, Yinghan Yao, Shitao Chen, Yang Cao, Liting Lin, Lionel Briand, Emir Muñoz
- **ArXiv**: [2610.25954](https://arxiv.org/abs/2610.25954)
- **Category**: cs.AI
- **Key contribution**: Scores **outcome and process compliance separately** across six regulated domains (rule cards tie regulatory obligations to trace evidence; hybrid grader = deterministic ordering/authority checks + LLM judge). Across 7 models × 120 tasks: **55.5% of retained executions are false-passes** (outcome-pass but process-fail), = 80.1% of outcome-passing runs; only **13.8% pass both**. Process-inclusive evaluation **changes the model ranking** — outcome-only scoring hides real differences.

#### 13. Policy Search in Code Space for Multi-Agent Pathfinding
- **Authors**: Matthias Eder, Pantelis Emmanouil, Vivek Farias, Fabian Fischer, Adam Jozefiak, Tianyi Peng, Thomas Ulz, Raphael Watschinger, Fangyu Wu, Andrew Zheng
- **ArXiv**: [2610.25946](https://arxiv.org/abs/2610.25946)
- **Category**: cs.RO / cs.AI
- **Key contribution**: Coding agents iteratively propose → implement → evaluate → diagnose → refine algorithms guided by simulation feedback and explicit correctness verification, as a third path beyond hand-design and opaque task-specific RL. Two-day search beat the stronger reproduced 2024 League of Robot Runners entry by **35.0%** on the densest instance; a week-long search found a **new class of MAPF algorithm** beating a calibrated proprietary solution by **58.9% throughput** in irregular-lane warehouses, with a proof of collision-freedom and finite-time completion.

---

## Additional Fresh Items (bullets)

- **GraphEvoResearcher** `2610.25978` (Suxing Liu) — training-free self-reflective reasoning lifted onto an explicit reasoning graph (support / contradict / depends_on edges); graph meta-reward + convergence early-stop. GSM8K 98% / MATH 92% / BBH 82% on DeepSeek, +24 pp over single-shot on MATH, bounded at ~2 steps / 4.5–5 nodes.
- **ABACUS** `2610.25963` (Yuhao Wang, Zelin Zang) — reusable composition programs over *frozen* judgment models; 99.67% macro accuracy on held-out BBH questions vs 64.00% direct Kev and 68.80% Qwen3.5-4B, with an **8.43× online speedup** vs Qwen's unrestricted policy (0.255s vs 2.150s/question).
- **AdaExploreBench** `2610.25950` (Rui Wang et al., 18 authors incl. HKUST/TikTok-affiliated) — proactive exploration + test-time adaptation under *implicit rule drift*; GPT-6 Sol only **61.9% calibrated accuracy**; bottleneck is acquiring the right evidence and noticing stale evidence, not reasoning over it.
- **EmbodiedWorld-200K** `2610.25959` (X. Feng et al., **NeurIPS 2026**) — 200K+ open-world embodied navigation-planning samples with multi-level annotations; video world model used as a low-cost environment proxy for RL post-training, improving OOD scenes.
- **PaceVLA** `2610.25961` (Hojin Jeon et al.) — adaptive temporal action quantization in VLA policies (mode-specific decoders + quantizability-guided router) to fix the speed/accuracy trade-off; 3 sim benchmarks + 6 real-world tasks.
- **On the Benefits of Uncertainty Estimation for Species Classification** `2610.25977` (Kamenan N'Gadi et al., ICPR 2026) — ResNet-18 on 759-class diatoms; temperature scaling ECE 0.117 → 0.055, selective macro-F1 99.01% at 66.2% coverage. Illustrative of the calibration/selective-prediction pattern recurring across this batch.

---

## Notes

- **CTR-prediction lane empty** for a further consecutive October window; nearest hits in a dedicated `abs:"click-through rate"` sweep are WeGR `2610.16979` (2026-10-12) and ECC `2610.13066` (2026-10-09) — both already on file or out of window. [[ctr-scaling-landscape]] gains no entrant.
- Rec/ads papers in-window (**MAPS**, **OneChord**) were first claimed by sibling `arxiv-daily` 2026-10-20; this page cross-references rather than duplicates them.
- All items above were `grep`-verified as new-to-wiki at write time (0 hits) except the two cross-referenced IDs.
- Single-source / abstract-only: all claims above are taken from arXiv abstracts; no full-text or code verification performed in this pass.
- Affiliations are "not stated" unless the abstract declares a venue/company — never inferred.
