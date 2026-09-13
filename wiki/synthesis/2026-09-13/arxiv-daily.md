---
title: "arXiv Daily — AI / LLM / Recommendation / Advertising / CTR / Games"
type: synthesis
created: 2026-09-13
updated: 2026-09-13
tags: [arxiv-daily, AI, LLM, recommendation, advertising, auctions, CTR, sequential-modeling, time-series, games, game-theory, multi-agent, agents, RAG, retrieval, generative-retrieval, fair-division, optimization]
---

# arXiv Daily Report — 2026-09-13

> **Weekend note on methodology**: arXiv does not announce on Sundays, so no new mailing exists for Sun 13 Sep 2026 — the freshest window is the **Fri 11 Sep 2026** mailing (announcing the Wed 9 Sep – Thu 10 Sep submission wave, IDs ~2609.062xx–2609.119xx). This run re-scanned the cs.IR / cs.LG / cs.AI / cs.CL / cs.GT / cs.MA "recent" listings, grep-verified every featured ID against all 4,609 arXiv IDs in `wiki/`, and excluded papers already covered by the 09-09 → 09-12 sibling digests (arxiv-daily, arxiv-ai-search, arxiv-paper-check, conference-digest, game-rl-daily) **plus the same-day 09-13 arxiv-paper-check**. All 26 featured papers are **fresh to the wiki** (0 hits). Notable not-repeated coverage (already featured on 09-12): 2609.11876 regularized rec models, 2609.11682 COBRA-Skills, 2609.11209 REVA, 2609.11808 generative late-interaction VDR, 2609.11646 QPP, 2609.10750 synthetic-data forgetting, 2609.11859 mechanistic routing studies, 2609.11687 Kashin-DCT quantization, 2609.11863/2609.11889 TNBR/ABRA, 2609.11737 ORCH, 2609.05708 CUSP. Excluded into the 09-13 arxiv-paper-check: 2609.09878 (purchase-advice measurement), 2609.11414 (SWRouter), 2609.11607 (alt-data forecasting), 2609.11709 (Bayesian backward reasoning).

---

## 1. Recommendation Systems & Advertising-Platform Economics

### 1.1 FunnelAudit: Responsibility Auditing in Multi-Route Recommender Systems

| Field | Detail |
|-------|--------|
| **Authors** | Jie Li, Dudu Luo, Jiayang Niu, Ke Deng, Yongli Ren |
| **Institution** | RMIT University (inferred) |
| **Published** | 7 Sep 2026 (cs.IR) |
| **Abstract** | Multi-route recommender systems combine retrieval, allocation, fusion and ranking, making individual inclusions/exclusions hard to audit: route overlap hides effects from one-at-a-time ablations, while freezing downstream stages yields counterfactuals inconsistent with serving. FunnelAudit is an executable framework for incident-level responsibility auditing. An accountability contract specifies the disputed Top-K event, controls and owners, permitted reference actions, and replay semantics. It evaluates every permitted control configuration and applies graded *actual responsibility* to find the smallest outcome-preserving contingency that makes each control pivotal. Across 258,809 user-target incidents from three real interaction datasets with two-stage nine-route funnels, 4.24–16.24% admit a responsible control; among responsible pairs 92.55–99.64% require a nonempty contingency (single-control ablation recovers only 0.36–7.45%). Policies differing on only 0.31–2.39% of incidents yield 21.44–54.05% Jaccard distance between responsible-route sets. Independent replay reproduces all 9,121,792 checked outcomes; exhaustive search and a MILP agree with every sampled judgment. |
| **Key Innovations** | (1) Incident-level "responsibility" as graded counterfactual pivots over an accountability contract; (2) explicit reference to *serving* semantics vs frozen-stage ablation; (3) checkable witness certificates with exact agreement between exhaustive search and MILP — a template for recsys accountability in multi-route (industry-style) funnels. |
| **Link** | [arXiv:2609.06964](https://arxiv.org/abs/2609.06964) |

### 1.2 Exploring Bottom-Up Clustering for Creating Semantic IDs

| Field | Detail |
|-------|--------|
| **Authors** | Leah Woldemariam, Sudhanshu Garg, Taha Belkhouja, Charles Kim-Yip, Ali Sahami |
| **Institution** | (Not specified; industrial generative-RAG recsys R&D, inferred) |
| **Published** | 8 Sep 2026 (cs.IR / cs.AI) |
| **Abstract** | Generative retrieval attributes its success to Semantic IDs, which capture item semantics better than arbitrary hashes. Key challenges: mapping each identifier to a *unique* product while retaining information useful to downstream tasks. Prior work appends extra codewords to de-duplicate and uses residual quantization (top-down) for hierarchical clusters. This paper presents a bottom-up clustering algorithm that yields identifiers that are both unique and structure-preserving on the original embeddings, improving cluster quality of the Semantic IDs and their utility for downstream generative retrieval. |
| **Key Innovations** | (1) Bottom-up (agglomerative) construction of semantic ID hierarchies instead of residual top-down splitting; (2) embedding-structure preservation as an explicit design goal; (3) targeted fix for semantic-ID non-uniqueness (relevant to generative rec + RAG pipelines). |
| **Link** | [arXiv:2609.08310](https://arxiv.org/abs/2609.08310) |

### 1.3 Why Customer Choice Models Matter

| Field | Detail |
|-------|--------|
| **Authors** | Berry Gerrits, Fabian Akkerman |
| **Institution** | VU Amsterdam et al. (inferred) |
| **Published** | 29 Jul 2026 (cs.GT / math.OC) |
| **Abstract** | Choice models are central to revenue management (e.g., attended home delivery slotting), yet the field usually picks one without much scrutiny. This paper argues the choice model *does* matter: revenue-management policies judged by their own assumed model — or trusted under a single set of parameters — can be materially worse than they look. A short position-style study motivating model-robustness in choice-model-driven price/reward optimization. |
| **Key Innovations** | (1) Model-misspecification critique of choice-model-based revenue management; (2) evidence that self-consistent evaluation overstates policy performance; (3) motivation for robust policy evaluation across choice-model families (relevant to ad allocation / dynamic pricing). |
| **Link** | [arXiv:2609.10557](https://arxiv.org/abs/2609.10557) |

### 1.4 Looking for Bidding Teammates: A Game-Theoretic Model of Stranger Collusion in Peer Review

| Field | Detail |
|-------|--------|
| **Authors** | Jinming Xing, Charlotte Brian |
| **Institution** | (Not specified) |
| **Published** | 31 Jul 2026 (cs.GT / cs.SI) |
| **Abstract** | Paper bidding is the entry point to reviewer assignment at large CS conferences: reviewers declare interest, combined by an optimizer with automated affinity scores. Reviewers who have never met recruit each other online, exchange identifiers, bid on each other's papers, and reciprocate with inflated scores. Existing collusion models assume already-trusted colleagues; open recruitment removes that assumption. This gives the first game-theoretic model of collusion *formation* in peer review — the **Mutual Bidding Dilemma**: a four-stage game covering recruitment, identifier exchange under risk of being reported, unverifiable bidding, and reciprocal reviewing. The model predicts the arrangement cannot form — reciprocation is never individually rational for any payoffs. What closes the gap is *enforcement* (visibility of reviews, recurring deadlines, group memory), not incentives. Derives the condition under which inflation is sustainable and the detection rate above which no partnership survives. In a calibrated conference simulation, a two-person arrangement is worth 3.2 points of acceptance probability, displacing 70 honest papers while mean quality moves only 0.002 — no summary statistic reveals it; randomized assignment is the one defense reaching enforcement itself. |
| **Key Innovations** | (1) First formal model of collusion *formation* (not just existing-pair collusion) in review bidding; (2) shows reciprocation is never individually rational absent enforcement — mechanism-design insight that maps to ad-auction collusion; (3) "harm is distributional not aggregate" — why these attacks evade aggregate metrics. |
| **Link** | [arXiv:2609.05444](https://arxiv.org/abs/2609.05444) |

---

## 2. Generative Retrieval & Document Retrieval

### 2.1 PDMR: Passage-Driven Multi-ID Document Retrieval

| Field | Detail |
|-------|--------|
| **Authors** | Smail Oussaidene, Mohand Boughanem |
| **Institution** | IRIT, Université de Toulouse (inferred) |
| **Published** | 8 Sep 2026 (cs.IR) |
| **Abstract** | Generative Retrieval (GR) maps queries directly to document identifiers, but most frameworks rely on a single-identifier assumption forcing one sequence to represent all document content — lossy when documents are multi-faceted, and fragile to query-intent variation. PDMR represents documents through *multiple passage-level identifiers*: each document is segmented and every selected passage gets its own identifier, giving multiple semantic entry points per document. Training is formulated as multi-target learning that distributes probability mass across valid passage-level identifiers (supervision ambiguity resolution). On NQ320K improves Recall@1 / MRR@100 over strong GR and non-generative baselines; on MS MARCO Document achieves best Recall@1 and MRR@10. Ablations: passage-level supervision, identifier design, training-query augmentation, and multi-target learning contribute complementary gains. |
| **Key Innovations** | (1) Multi-ID generative retrieval = one document, many semantic access paths; (2) principled multi-target learning for one-to-many supervision; (3) strong results on both NQ320K and MS MARCO Document. |
| **Link** | [arXiv:2609.08762](https://arxiv.org/abs/2609.08762) |

### 2.2 REDSI: Reproducibility & Evaluation Consistency for Differentiable Search Indexing

| Field | Detail |
|-------|--------|
| **Authors** | Vivien Nicolas, Hicham Randrianarivo, Pascale Sébillot, Caio Corro |
| **Institution** | IRISA / CNRS / Université de Rennes (inferred) |
| **Published** | 8 Sep 2026 (cs.IR) |
| **Abstract** | DSI (Tay et al., 2022) has become the de facto GR baseline, yet is hard to reproduce: no public implementation covers all three identifier types (atomic, naive, semantic), reported results vary widely, and NQ320K preprocessing is diverse and underspecified. REDSI is the first open-source DSI implementation supporting all three identifier types plus a parameterizable, documented NQ320K construction pipeline. Results are competitive with/stronger than prior DSI baselines, and extensive downscaling experiments cover retrieval effectiveness, parameter efficiency, training methods, and decoding strategies. |
| **Key Innovations** | (1) First open-source DSI covering atomic/naive/semantic IDs; (2) parameterizable NQ320K pipeline (evaluation-consistency angle); (3) downscaling study opening new research directions for GR. |
| **Link** | [arXiv:2609.08860](https://arxiv.org/abs/2609.08860) |

### 2.3 Cassette: Case-to-Case Structural Distillation for Efficient Legal Case Retrieval

| Field | Detail |
|-------|--------|
| **Authors** | Yanran Tang, Ruihong Qiu, Hongzhi Yin, Xue Li, Zi Huang |
| **Institution** | University of Queensland (inferred) |
| **Published** | 8 Sep 2026 (cs.IR) |
| **Abstract** | Legal case retrieval (LCR) benefits from case-to-case graph structure (prior CaseLink), but test-time graph construction and pairwise term-frequency similarity are O(n²) and prohibitive at scale (e.g., >3,500s on LeCaRDv2's 55,192 cases). Cassette distills knowledge from a heavy teacher retriever into a lightweight hybrid student dual encoder using a ranking objective + eigen-matching objective: a multilayer-perceptron query encoder for online speed and a GNN candidate encoder for offline indexing. Verified on three benchmarks — effective ranking distillation with high efficiency. |
| **Key Innovations** | (1) Graph-structure knowledge distilled into cheap encoders (no test-time graph construction); (2) eigen-matching objective alongside ranking distillation; (3) O(n²)→offline-precomputed efficiency path for LCR (and template for structured search spaces at scale). |
| **Link** | [arXiv:2609.08185](https://arxiv.org/abs/2609.08185) |

---

## 3. RAG & Information Retrieval

### 3.1 Guaranteeing Faithful Evidence Extraction in Speculative RAG (CHyD)

| Field | Detail |
|-------|--------|
| **Authors** | Quentin Signé, Mohand Boughanem, Jose Moreno, Thiziri Belkacem |
| **Institution** | IRIT, Université de Toulouse (inferred) |
| **Published** | 9 Sep 2026 (cs.IR) |
| **Abstract** | LLMs increasingly serve as IR interfaces but hallucinate / diverge from retrieved evidence. Existing hybrid and semi-extractive methods don't guarantee that quoted spans verbatim-match the retrieved context — dangerous in safety-critical domains (certified documentation). **Constrained Hybrid Decoding (CHyD)** repurposes the speculative-decoding architecture into a faithfulness-first paradigm: hard decoding constraints restrict generation to continuous spans present in retrieved documents, giving a clean guarantee that any explicitly quoted span appears verbatim in context. Across SOTA LLMs on abstractive/extractive/semi-extractive QA incl. aircraft-maintenance technical benchmarks, hybrid baselines hallucinate quoted spans (exact extraction accuracy <40% in technical domains); CHyD achieves near-perfect extraction faithfulness model-independently while improving exact answer correctness. |
| **Key Innovations** | (1) Hard-constraint *verbatim guarantee* on cited/quoting spans (not just soft grounding); (2) novel use of speculative-decoding machinery for faithfulness, not speed; (3) safety-critical IR evaluation suite (aircraft maintenance). |
| **Link** | [arXiv:2609.10046](https://arxiv.org/abs/2609.10046) |

### 3.2 LiteRAG: Cost-Efficient Graph-Based Retrieval-Augmented Generation

| Field | Detail |
|-------|--------|
| **Authors** | Daniel Alejandro Coll Tejeda, Pedro García López, Daniel Barcelona-Pons |
| **Institution** | (Not specified; Spain, inferred) |
| **Published** | 9 Sep 2026 (cs.IR / cs.AI / cs.CL) |
| **Abstract** | Graph-based retrieval helps multi-hop QA but costs too much at query time and produces diffuse, oversized contexts. LiteRAG replaces expensive retrieval-time LLM control with query-conditioned algorithmic exploration and reasoning-chain context construction. On DistComp (multi-hop over distributed-systems papers) it reaches the highest overall quality (0.798) while cutting per-query latency >100× and cost >99% vs GraphRAG Global / DRIFT; on UltraDomain it matches LinearRAG quality using ~14× fewer tokens. Ablations: query-adaptive thresholding and community-aware hub penalization drive token-efficiency gains. |
| **Key Innovations** | (1) Removing LLM-in-the-loop from graph retrieval entirely (algorithmic query-conditioned traversal); (2) reasoning-chain context construction instead of diffuse subgraphs; (3) 100× latency / 99% cost reduction with quality gains. |
| **Link** | [arXiv:2609.10239](https://arxiv.org/abs/2609.10239) |

### 3.3 Matryoshka Hash Representations for Model-Aware Compact Semantic Retrieval

| Field | Detail |
|-------|--------|
| **Authors** | Peichun Hua, Yunming Xiao |
| **Institution** | (Not specified) |
| **Published** | 7 Sep 2026 (cs.IR / cs.AI / cs.LG) |
| **Abstract** | Dense retrieval's dominant index cost is one full-precision vector per document, so systems quantize to short codes (e.g., PQ). A single code is more useful if its short *prefixes* are each directly searchable (any-budget serving) — but training all prefixes jointly compromises early bits: short codes improve while full-width degrades; binary/low-bit codes sharpen the conflict. **Matryoshka Hash Representations (MHR)** is a two-stage procedure: learn a longer binary code first, then freeze the model and train zero-initialized residual code adaptors for directly searchable prefixes. One bit per coordinate for storage; continuous query logits; FAISS FastScan search. On MS MARCO → zero-shot transfer to 7 BEIR sets: .5561 NDCG@10 / .6535 Recall@100 at 32 bytes, beating best baselines at the same budget (advantage grows at lower budgets); also strengthens shortlisting-for-reranking and low-storage graph pruning (LEANN). |
| **Key Innovations** | (1) Any-prefix-searchable codes via residual adaptors decoupled from full-width training; (2) one-bit storage without binary-query expressivity loss; (3) composable with PQ-style pipelines (FastScan), rerank shortlisting, and graph pruning. |
| **Link** | [arXiv:2609.07276](https://arxiv.org/abs/2609.07276) |

---

## 4. LLMs, Agents & Reasoning

### 4.1 NovGauge: A Fine-Grained Benchmark for Diagnosing LLMs' Paper Novelty Assessment

| Field | Detail |
|-------|--------|
| **Authors** | Guoqiang Zhang, Kexin Tan, ... Tao Gui, Qi Zhang, Xuanjing Huang (18 authors) |
| **Institution** | Fudan University (inferred) |
| **Published** | 10 Sep 2026 (cs.AI / cs.CL) |
| **Abstract** | LLMs are increasingly used in peer review at major AI venues, yet novelty assessment stays a weak point; existing benchmarks score novelty holistically, hiding which dimension is misjudged or whether evidence is faithful. **NovGauge** is a human-anchored, fine-grained benchmark: 619 paper pairs + 50 multi-paper sets from ICLR reviewer-overlap claims and survey co-citations, labeled along task / problem / method dimensions. A cascading diagnostic pipeline verifies per-dimension correctness, evidence grounding, and logical support. Across 18 LLMs: hallucination rates 0–39% per dimension; among non-hallucinated correct-positive judgments, >70% cite evidence that fails to *logically support* the stated reason; best model (GPT-5.5) reaches 43–72% Verified F1, and most models retain <half of raw F1 after faithfulness verification. |
| **Key Innovations** | (1) Three-dimensional (task/problem/method) novelty diagnosis instead of one holistic score; (2) evidence-grounding + logical-support gate (hallucination vs unsupported-reason separation); (3) direct audit of LLM-in-the-loop peer review — timely given conference adoption. |
| **Link** | [arXiv:2609.11234](https://arxiv.org/abs/2609.11234) |

### 4.2 Rethinking Verbalized Confidence for LLM-as-a-Judge: A Compatibility Shift on Post-2025 Proprietary Models

| Field | Detail |
|-------|--------|
| **Authors** | Yu-Chung Hsiao |
| **Institution** | (Not specified) |
| **Published** | 10 Sep 2026 (cs.CL) |
| **Abstract** | Verbalized confidence, long dismissed as overconfident, coarse, and prone to round-number clustering, is now the more robust soft-scoring mechanism for LLM-as-a-Judge on top-tier proprietary models. Across SummEval, AggreFact, and HelpSteer2 — up to 18 LLMs — the standard advice to prefer log-probabilities no longer holds on post-2025 models, where verbalized confidence is the better signal. This is called a **compatibility shift**. Two new ingredients on top of a standard verbalized-confidence baseline: an overconfidence advisory and self-debate. Together they improve calibration, score-distribution spread, and robustness to task subjectivity. A generation effect: post-2025 models accommodate these additions with little balanced-accuracy cost, whereas pre-2025 models pay a measurable penalty. Compared with logprob-based G-Eval, verbalized confidence is the more subjectivity-robust soft signal on GPT-family top-tier releases. The shift is invisible under accuracy-only reporting. |
| **Key Innovations** | (1) Empirical reframing: verbalized confidence ↛ logits for modern LLM judges (post-2025 compatibility shift); (2) overconfidence-advisory + self-debate calibration recipe; (3) "invisible under accuracy-only reporting" — a measurement-sensitive conclusion for judge evaluation. |
| **Link** | [arXiv:2609.10996](https://arxiv.org/abs/2609.10996) |

### 4.3 When Noise Fabricates Bias: The Fragility of LLM-as-a-Judge Bias Measurement under Noisy Text

| Field | Detail |
|-------|--------|
| **Authors** | DongHyun Ryu, Jaehyeok Lee, YeongJun Hwang, JinYeong Bak |
| **Institution** | (Not specified; Korean institution inferred) |
| **Published** | 10 Sep 2026 (cs.CL / cs.LG) |
| **Abstract** | LLMs are increasingly used as judges to measure social bias in text, yet the passages they judge are often noisy — typos, informal spelling, broken punctuation. How such surface noise distorts bias measurement is understudied. Applying five realistic noise conditions at multiple intensity levels to 3,822 stereotype-related responses and comparing the resulting bias judgments vs original text shows bias measurement is *not* symmetric under noise: it is far more likely to turn neutral judgments into biased ones than biased into neutral, by up to a **120x margin**. Two non-obvious effects across four LLM judges: in the most fragile judge the distortion is purest at mild, realistic noise levels (where erasure is scarcest), and as judges grow robust it attenuates toward parity rather than reversing. Bias measured on noisy text is therefore systematically **overestimated** — most in the categories that matter most for fairness. |
| **Key Innovations** | (1) Asymmetry result: noise fabricates bias (neutral→biased ≫ biased→neutral, up to 120×); (2) judge robustness vs distortion attenuation relationship; (3) direct implication for dataset/measurement hygiene in fairness auditing. |
| **Link** | [arXiv:2609.11067](https://arxiv.org/abs/2609.11067) |

### 4.4 Scores Alone Do Not Prove Discovery: The Discovery Certification Protocol (DCP)

| Field | Detail |
|-------|--------|
| **Authors** | Jingjie Ning, Shanshan Zhong, Xiaochuan Li, Ji Zeng |
| **Institution** | (Not specified) |
| **Published** | 7 Sep 2026 (cs.MA / cs.AI / cs.SE) |
| **Abstract** | AI research agents combine prior knowledge, public sources, and experimental feedback to produce results. **DCP** turns claims into executable recovery and feedback tests. Gate 1 validates useful improvement on sealed evaluation; Gate 2 gives matched agents registered starting info + observed Web content while withholding the target research history — every valid method reaching the target must supply a recovery witness and triggers the **Core veto** (requires adequate controls, zero observed recoveries, finite-sample bound on recovery). Optional Gate 3 measures the average effect of truthful feedback vs a neutral policy. Two controlled audits (SQLite optimization; virtual catalyst control) each produced zero recoveries in 96 episodes (upper bound 0.0468); paired studies yielded 30 truthful vs 0 neutral recoveries with passing 60-pair null studies. A deterministic, LLM-free verifier reproduces decisions from frozen evidence. |
| **Key Innovations** | (1) "Recovery" (can a fresh matched agent reproduce it?) as the operational definition of discovery — kills benchmark/memorization artifacts; (2) Core veto + finite-sample guarantees; (3) LLM-free deterministic verification of audit outputs. |
| **Link** | [arXiv:2609.09219](https://arxiv.org/abs/2609.09219) |

---

## 5. LLM Efficiency, Optimization & Training

### 5.1 Musec: MomentUm SpEctral Clipping for Stable Muon-type Training

| Field | Detail |
|-------|--------|
| **Authors** | Zhuanghua Liu, Menglian Wang, Luo Luo |
| **Institution** | (China academic, inferred) |
| **Published** | 10 Sep 2026 (cs.LG) |
| **Abstract** | Muon is highly effective for LLM training (often better than Adam/AdamW) but suffers from training instability via *spectral flattening* (loss spikes, unbounded weight growth). Existing fixes (weight or attention-logit clipping) need architecture-specific modifications. **Musec** replaces Muon's spectral flattening with spectral clipping: instead of forcing all momentum singular values ≈1, it clips singular values above a threshold while preserving spectral structure — an optimizer-level, architecture-agnostic stabilization. **Soft Musec** implements this with a smooth spectral saturation via coupled Newton-Schulz iterations. The paper gives the first convergence guarantee for Muon-type methods in nonconvex nonsmooth stochastic optimization. Empirically, Soft Musec is stable where existing Muon variants diverge, across learning rates and model sizes, while matching tuned variants' performance. |
| **Key Innovations** | (1) The instability mechanism is spectral flattening; clip instead of flatten; (2) architecture-agnostic, optimizer-level fix (no per-component hacks); (3) first nonconvex-nonsmooth convergence guarantee for Muon-type optimizers. |
| **Link** | [arXiv:2609.11655](https://arxiv.org/abs/2609.11655) |

### 5.2 K/V-Cache Interventions Dissociate Representation Alignment from Persona Expression

| Field | Detail |
|-------|--------|
| **Authors** | Yu Sun, Mengyin Lu, Cong Feng, Guangming Lu, Huimin Han |
| **Institution** | Harbin Institute of Technology (inferred) |
| **Published** | 10 Sep 2026 (cs.CL / cs.LG) |
| **Abstract** | Studies K/V-cache interventions — transplanting a target-conditioned K/V trajectory into a source-persona generation — as a structured surface for persona control in decoder-only LMs. Across 13 intervention configs on Llama-3.1-8B, two dissociations + one failure: (1) all layer-band replacements achieve strong local V-space alignment, but only mid-layer (9–20) combines target-marker expression with preserved lexical diversity; (2) full vs mid-layer induce comparable alignment yet different lexical-diversity; (3) position perturbations (lag, shuffle) uniformly suppress target-persona expression — a common failure rather than a strict dissociation. Representation-level similarity alone doesn't predict downstream persona expression. A same-token-sequence control shows the L28 shift isn't merely imported token history. |
| **Key Innovations** | (1) Trajectory-level K/V *transplantation* as a persona-control surface; (2) alignment ≠ expression dissociation across layer bands; (3) systematic control isolating token-history confound. |
| **Link** | [arXiv:2609.11020](https://arxiv.org/abs/2609.11020) |

### 5.3 Particle GFlowNets: Rethinking Generative Marginalization Models

| Field | Detail |
|-------|--------|
| **Authors** | Tiago da Silva, Diego Mesquita, Salem Lahlou |
| **Institution** | (Mila-affiliated, inferred) — UAI 2026 |
| **Published** | 10 Sep 2026 (cs.LG) |
| **Abstract** | Generative Marginalization Models (MaMs) are efficient neural samplers for any-order autoregressive modeling of discrete distributions: learning marginal + conditional probabilities of a persistent-block Gibbs sampler gives fast posterior evaluation in a single forward pass. This paper shows MaMs are *equivalent* to Generative Flow Networks (GFlowNets) — two research lines that were treated as distinct — and extends MaMs' sampler to non-autoregressive generative processes via an automatic full-state rejuvenation criterion for the Gibbs sampler derived from the Gelman-Rubin statistic. **Particle GFlowNets** markedly accelerates training in large combinatorial spaces. |
| **Key Innovations** | (1) Unification: MaMs ≡ GFlowNets (methodological bridge); (2) automatic Gelman-Rubin rejuvenation criterion for Gibbs restart; (3) non-autoregressive extension with faster convergence in large combinatorial spaces. |
| **Link** | [arXiv:2609.11538](https://arxiv.org/abs/2609.11538) |

---

## 6. Games & Game Theory

### 6.1 The Fine-Grained Complexity of Approximate Nash Equilibrium and Free Games

| Field | Detail |
|-------|--------|
| **Authors** | Noah Golowich |
| **Institution** | (MIT / UC Berkeley, inferred) |
| **Published** | 7 Sep 2026 (cs.GT / cs.CC) |
| **Abstract** | Fine-grained complexity of computing approximate Nash equilibria and approximating free-game values as error vanishes. Assuming PCP-for-PPAD and ETH-for-PPAD, computing ε-approximate NE in 2-player N-action games requires time N^((log N/ε²)^{1-o(1)}), showing the Lipton–Markakis–Mehta algorithm (2003) is optimal through all regimes ε = ω(1/√N). Optimality was known in the constant-ε regime (Rubinstein 2016); prior work could only rule out N^{O(log N/ε)} for ε=o(1). Similar techniques give a tight lower bound for ε-additive free-game value estimation under ETH — answering a question of Aaronson, Impagliazzo, Moshkovitz (2014). |
| **Key Innovations** | (1) LMM optimality across the full vanishing-error spectrum; (2) closes the ε=o(1) gap left open by Rubinstein; (3) answers 2014 AIM question for free games. |
| **Link** | [arXiv:2609.07136](https://arxiv.org/abs/2609.07136) |

### 6.2 Pairwise Maximin Share Allocations Need Not Exist (Haris Aziz)

| Field | Detail |
|-------|--------|
| **Authors** | Haris Aziz |
| **Institution** | UNSW Sydney / CSIRO (inferred) |
| **Published** | 5 Sep 2026 (cs.GT) |
| **Abstract** | Resolves an open question since PMMS was introduced: whether a PMMS allocation always exists for indivisible goods with strictly positive additive valuations. Answer: **No.** Constructs an instance with four agents and strictly positive additive valuations admitting no complete PMMS allocation. The core question in fair division formally settled. |
| **Key Innovations** | (1) Negative resolution of the long-open PMMS existence problem; (2) minimal counterexample (4 agents, strictly positive valuations); (3) closes a decade+ fair-division gap (basis for the wave's follow-ups, see 6.3/6.4). |
| **Link** | [arXiv:2609.06282](https://arxiv.org/abs/2609.06282) |

### 6.3 PMMS Allocations Need Not Exist for 3 Agents with Additive Valuations

| Field | Detail |
|-------|--------|
| **Authors** | Paul Gölz |
| **Institution** | TU Berlin (inferred; prior CMU) |
| **Published** | 8 Sep 2026 (cs.GT) |
| **Abstract** | Companion strengthening of the Aziz result: gives a 3-agent, 9-good instance with additive valuations where **no PMMS allocation exists** (proof + certified via exhaustive enumeration), and shows PMMS cannot be approximated above ratio 78/79 ≈ 0.987 in the worst case. |
| **Key Innovations** | (1) Improves non-existence to 3 agents (tight in n); (2) 78/79 inapproximability bound; (3) computer-certified proof alongside analytic argument. |
| **Link** | [arXiv:2609.08954](https://arxiv.org/abs/2609.08954) |

### 6.4 Non-Existence of PMMS Allocations and a 4/3-PMMS Guarantee for Additive Chores

| Field | Detail |
|-------|--------|
| **Authors** | Xiaohui Bei, Zehan Lin, Shengxin Liu, Rong Luan, Biaoshuai Tao |
| **Institution** | Tsinghua / HIT / SJTU et al. (inferred) |
| **Published** | 9 Sep 2026 (cs.GT) |
| **Abstract** | PMMS fairness for indivisible items, additive preferences. Gives a polynomial-time **chores→goods reduction** preserving PMMS existence, which — combined with known chores nonexistence — yields nonexistence for additive goods (parallel to 6.2). Showing PMMS existence is NP-hard. Explicit instances with PMMS factors 226/227 (goods) and 1.102065 (chores), certified by exact enumeration. Complementing impossibility: every additive-*chores* instance admits a **4/3-PMMS** allocation. |
| **Key Innovations** | (1) Chores→goods reduction preserving PMMS existence (unifying the two settings); (2) NP-hardness of PMMS existence; (3) first constant-factor 4/3-PMMS guarantee for chores. |
| **Link** | [arXiv:2609.10493](https://arxiv.org/abs/2609.10493) |

### 6.5 How Well Can Strategyproof Tournament Rules Resist Pairwise Manipulation?

| Field | Detail |
|-------|--------|
| **Authors** | Ke Ding, Bo Li, Fangxiao Wang |
| **Institution** | (academic, inferred) |
| **Published** | 7 Sep 2026 (cs.GT) |
| **Abstract** | Tournament rules should be Condorcet-consistent, monotone, and resistant to coalition manipulation. Prior work measures additive resistance (k-SNM-α); recent work adds multiplicative (k-MNM-δ) and selfishness-aware (k-NM_λ) notions. Establishes the strict hierarchy NM_λ > MNM > SNM, motivating the stronger, less-studied pairwise variants. **Randomized Death Match** is 2-MNM-3/2 (optimal lower bound). Introduces **BlockBonusedWinStrengths**: Condorcet-consistent, monotone, and 2-NM₂ — improving the prior λ=11 upper bound to within 2× of the λ=1 lower bound. |
| **Key Innovations** | (1) First formal hierarchy SNM < MNM < NM_λ; (2) optimal 2-MNM-3/2 tournament rule; (3) 5.5× tightening of non-manipulability constant for a Condorcet-consistent rule. |
| **Link** | [arXiv:2609.07062](https://arxiv.org/abs/2609.07062) |

---

## 7. Multi-Agent Systems & Sequential/Time-Series Modeling

### 7.1 Copying Explains the Collective Behavior of AI Agents in the Wild

| Field | Detail |
|-------|--------|
| **Authors** | Giordano De Marzo, Nicola Alboré, David Garcia |
| **Institution** | University of Vienna / University of Konstanz (inferred) |
| **Published** | 8 Sep 2026 (cs.MA / cond-mat.stat-mech) |
| **Abstract** | In June 2026 thousands of AI agents found a small public wiki accepted edits from inside their sandboxes and used it to help each other pass a timed test. Each agent lived ~1 hour, remembered nothing after, and the complete public log preserves what each wrote *and what it saw first*. Three decisions (where to write, what to call itself, how to word the message) are all governed by one rule: an agent picks an option with probability ≈ its *visible share* — the share on the page in front of it, then in the recent-edit stream, only weakly anything older. Three minimal one-parameter copying models reproduce the heavy-tailed page-meeting distribution, name-fragment frequencies, and the internal-consistency patchwork of pages. Copying whatever the environment shows explains most collective structure — and makes such populations easy to steer (first writer sets the convention). |
| **Key Innovations** | (1) Real-world natural experiment: agent-without-memory collective behavior from public wiki logs; (2) minimal copying model dominating explanations (no explicit coordination/reasoning needed); (3) steerability implication — order-of-appearance controls population conventions. |
| **Link** | [arXiv:2609.09150](https://arxiv.org/abs/2609.09150) |

### 7.2 Prospect-State Propagation for Multi-Agent Systems (PspMAS)

| Field | Detail |
|-------|--------|
| **Authors** | Zhimei Chen, Mu Chen, Fakhri Karray |
| **Institution** | University of Waterloo (inferred) — Findings of EMNLP 2026 |
| **Published** | 7 Sep 2026 (cs.MA / cs.CY) |
| **Abstract** | LLM-based multi-agent systems scale by compressing intermediate states to cut tokens, but naive compression discards semantically rich economic states (behavioral trajectories) that drive macro fluctuations — and agent *heterogeneity degrades* during simulation. PspMAS decouples each agent's micro state into a compact **Prospect State** (psychological traces via a lightweight, parallelizable propagator that continuously reinjects heterogeneity, inspired by prospect theory) and an expressive **Semantic State** (LLM perception/reasoning/planning). Together they give a scalable LLM-based multi-agent simulation. |
| **Key Innovations** | (1) Prospect-theory-grounded heterogeneity injection for LLM MAS; (2) explicit diagnosis of heterogeneity decay under compression; (3) cheap parallel propagator + LLM semantic layer as a scaling recipe for economic simulation. |
| **Link** | [arXiv:2609.08033](https://arxiv.org/abs/2609.08033) |

### 7.3 CompEvo: Competition-Induced Evolution for Multi-Agent News-Driven Time-Series Forecasting

| Field | Detail |
|-------|--------|
| **Authors** | Yuxuan Zhang, Yangyang Feng, Yong Guan, Daifeng Li, Kexin Zhang, Junlan Chen, Bowen Deng, Jun Liu, Zehua Zeng |
| **Institution** | Sun Yat-sen University et al. (inferred) |
| **Published** | 3 Sep 2026 (cs.NE / cs.MA) |
| **Abstract** | News-driven time-series forecasting combines evolving textual events with historical observations. In multi-agent settings two problems remain: *degeneration of thought* (agents converge to similar evidence-seeking) and insufficient theoretical grounding (heuristic strategy updates). CompEvo is a competition-induced evolution framework: an **evolutionary-game formulation** guarantees equilibrium existence and optimization convergence; a trainable framework integrates strategy execution, fitness-based differentiable selection, and competition-induced strategy evolution. Heterogeneous agents explore diverse news evidence; forecasting feedback converts into differentiable influence weights; strategies evolve under competitive pressure while preserving diversity. On four real-world datasets: **−27.3% RMSE / −26.2% MAPE** on average over strong baselines; maintains diverse, specialized agent behaviors. |
| **Key Innovations** | (1) Evolutionary-game grounding (equilibrium existence + convergence) for agent strategy update — replaces heuristics; (2) direct fix for thought-degeneration in news-forecasting agent pools; (3) relevance to sequential modeling: differentiable pressure from forecast error back into evidence-selection strategy. |
| **Link** | [arXiv:2609.09195](https://arxiv.org/abs/2609.09195) |

### 7.4 Beyond Agent Harnesses: Cross-Substrate Authority for Multi-Agent Systems

| Field | Detail |
|-------|--------|
| **Authors** | Yang Li, Sergey Volkov, Hai Liu, Zongsi Xu, Xiyu Chen, Tuo Zhou, Dian Shao, Hao Sun, Ye Lu |
| **Institution** | (Not specified) |
| **Published** | 10 Sep 2026 (cs.MA) |
| **Abstract** | Agentic systems persist model-visible memory while mutating workspaces, while a runtime, registry, or approval service may hold authority state *outside both*. Identical final files can then require opposite safe actions. This is the **cross-substrate authority gap**: decision-relevant authorization information resides outside the planner-visible workspace or memory state. Across two controlled mini-benchmark families, three experiments compare planner-observation augmentation with an execution-time authority check using real Git lineage, durably recorded agent execution attempts, deterministic oracles, and two model routes. Experiment 1 (128-cell controlled evidence ablation): authority-blind candidate evidence obtains 0/32 final semantic success, while raw receipts and a typed relation both obtain 32/32 — the missing authority fact accounts for the gain; typed packaging gives no observed planning-accuracy gain over equal raw information. Experiment 2 (96 planning calls): workspace-visible evidence yields 12/16 *unsafe* publication decisions, and planning with the typed relation remains unreliable (15/32 first actions correct; 11/32 invalid or absent). Experiment 3 replays the same 32 fixed model-generated first-action intents with zero additional model calls: a deterministic execution guard prevents all six unsafe intents from becoming effects and permits all 12 valid authorized publish intents. Authority enforcement sits at the mutation boundary as the operational endpoint of memory governance. |
| **Key Innovations** | (1) Formal identification of the cross-substrate authority gap (authorization living outside planner-visible state); (2) evidence: workspace-visible evidence *worsens* unsafe publication decisions unless the authority fact is injected; (3) execution-time deterministic guard ≻ planner-context augmentation — a design guideline for agent memory/approval governance. |
| **Link** | [arXiv:2609.08472](https://arxiv.org/abs/2609.08472) |

---

## Summary of Key Trends

| Trend | Notable Papers |
|-------|---------------|
| **Recsys accountability reaches serving semantics** | FunnelAudit (graded responsibility + witness certificates), Looking for Bidding Teammates (peer-review collusion formation) |
| **Generative retrieval grows up: multi-ID & reproducibility** | PDMR (passage-level multi-ID), ReDSI (open DSI for all 3 ID types), Cassette (graph distillation for legal) |
| **RAG faithfulness & cost** | CHyD (verbatim-guaranteed spans), LiteRAG (100× cheaper graph RAG), Matryoshka Hash (any-budget compact codes) |
| **LLM-as-judge gets measured, not assumed** | NovGauge (novelty verified-F1 diagnostics), Verbalized-Confidence compatibility shift, Noise-Fabricates-Bias (120× asymmetry) |
| **Agent research validation** | DCP (discovery = recovery test), Copying-in-the-wild (real gathered agent behavior), PspMAS (heterogeneity injection), Cross-Substrate Authority (authorization outside planner-visible state) |
| **Muon-type optimizers mature** | Musec (spectral clipping vs flattening; first convergence guarantee) |
| **Fair division: PMMS settled in one wave** | Aziz (4-agent counterexample), Gölz (3-agent, 78/79), Bei et al. (chores reductions, 4/3-PMMS, NP-hardness) — rare same-week settlement of a long-open problem |
| **Game theory complexity tightens** | Golowich (LMM optimality across all ε regimes for ε-Nash); contemporaneous equilibrium-quality work (exact-form regret) covered by the 09-13 game-rl-daily |

(End of file — total 26 papers / 7 sections)