---
title: arXiv Daily - 2026-09-07
type: synthesis
created: 2026-09-07
updated: 2026-09-07
tags: [arxiv, daily, LLM, recommendation, CTR, advertising, sequential-modeling, games, game-theory, multi-agent, AI]
---

# arXiv Daily Report — 2026-09-07

> Curated selection of recent arXiv papers across LLMs, recommendation systems, CTR prediction, advertising, sequential modeling, and games.
>
> **Note on methodology**: This is the **Mon 7 Sep 2026 mailing** (papers submitted Fri 4 Sep – Mon 7 Sep), the first new mailing after the 09-05/09-06 weekend digests that only covered through Fri 4 Sep. All featured arXiv IDs are grep-verified **0 hits** in `wiki/` (absent from 09-01 → 09-06 sibling digests — arxiv-daily, arxiv-ai-search, game-rl-daily, arxiv-paper-check). Data gathered directly from arXiv `list/recent` pages (cs.IR / cs.LG / cs.CL / cs.AI / cs.GT / cs.MA) and individual `/abs/` pages. The arXiv Atom API remained unavailable (HTTP 429/empty), so listings were scraped directly.

---

## Large Language Models & Agents

### 1. Optimal Rates for Agentic Networked Information Aggregation

| Field | Detail |
|-------|--------|
| **Authors** | MohammadHossein Bateni, Zahra Hadizadeh, MohammadTaghi Hajiaghayi, Mahdi JafariRaviz, Shayan Taherijam |
| **Institution** | Academic (Meta Research / UC San Diego / MIT / Univ. of Maryland et al.) — *(opencode-compiled)* |
| **arXiv** | [2609.05318](https://arxiv.org/abs/2609.05318) |
| **Submitted** | 7 Sep 2026 (cs.LG / cs.GT) |

**Abstract**: Building on Kearns, Roth, and Ryu (SODA'26), this work studies information aggregation in a networked learning model capturing a central pattern in agentic AI: each agent sees only part of the data and passes on only its own conclusion. Agents sit in a DAG over a linear-regression (MSE) problem; each sees a subset of features plus its parents' predictions and passes only its prediction forward. For an $M$-covered path (every block of $M$ consecutive agents collectively sees all features), they close the known gap: excess error is constant up to depth $M^2$, then $\Theta(M^2/D)$ beyond it.

**Key innovations**:
- **Tight rate** $\Theta(M^2/D)$ for `M`-covered depth-`D` paths, improving both the prior upper bound $O(M/\sqrt D)$ **and** the lower bound $\Omega(M/D)$; yields a constant lower bound below $M^2$ and geometric contraction of excess error for any fixed distribution.
- Proves the same optimal rate for **logistic classification** in the logit-passing model of Bateni et al. (binary cross-entropy), transferring all regression lower bounds.
- A clean theoretical characterization of the *lossy-relay* protocol underlying modern multi-step agent pipelines (each node passes only its conclusion downstream).

---

### 2. How to Speculate about Uncertainty in Agentic Coding? A Draft-Model Gate Method

| Field | Detail |
|-------|--------|
| **Authors** | Konstantin Grotov, Valentin Malykh |
| **Institution** | Industry (AI research lab) — *(opencode-compiled: authors independent/research lab)* |
| **arXiv** | [2609.05274](https://arxiv.org/abs/2609.05274) |
| **Submitted** | 6 Sep 2026 (cs.LG) — **EMNLP 2026 Industry Track** |

**Abstract**: LLM agents deployed for software engineering fail expensively: they act confidently wrong, and bad actions are only recognized after costly execution and retry. The authors present **Speculative Uncertainty (SU)**, which recovers a predictive failure signal for a black-box agent from its output tokens alone — no logits, weights, activations, or repeated sampling. Inverting speculative decoding, a small open-weight draft model scores the agent's already-generated trajectory in a single forward pass; phase-aware features separate reasoning vs. action spans and are calibrated against a verifiable objective.

**Key innovations**:
- **Logits-free failure signal** from one draft-model forward pass — complements the KV/efficiency thread by using speculative-style cross-likelihoods for *risk detection*.
- Instantiated as a **pre-execution veto gate** on Qwen3-Coder-480B and Claude 3.5 Sonnet: cuts execution error rate by **6–8 pp** and token cost by **14–19%** in deployment; transfers to OOD benchmarks without retraining, generalizes across agent models.

---

### 3. BeaconKV: Key-Value Cache Compression Guided by Beacon Queries

| Field | Detail |
|-------|--------|
| **Authors** | Janghyeon Kim, Minsoo Kim, Kyuhong Shim, Jungwook Choi |
| **Institution** | Academic (Hanyang University) — *(opencode-compiled)* |
| **arXiv** | [2609.04971](https://arxiv.org/abs/2609.04971) |
| **Submitted** | 7 Sep 2026 (cs.LG) — **ICML 2026** |

**Abstract**: Large Reasoning Models (LRMs) generate long chains-of-thought whose KV cache grows linearly with length, often exceeding GPU capacity. Existing KV compression relies on recent queries as proxies for future attention importance — an assumption that fails in long-horizon reasoning because certain decoding steps produce **Thought Revisiting Tokens (TRT)** that re-attend to distant context (e.g., early task plans). Systematic analysis shows TRT queries cluster into a small number of similarity groups in embedding space.

**Key innovations**:
- **Beacon queries** — compact per-cluster representatives that anticipate which KV pairs will be revisited *without storing the full query history* (training-free).
- Across four open LRMs and diverse reasoning benchmarks, BeaconKV achieves up to **5.8× memory reduction** nearly preserving full-cache accuracy, with **>4.3× throughput** — a response to the long-CoT KV bottleneck theme (cf. Random Attention 2609.03430, VestigeKV 2609.03949).

---

### 4. Unifying ICL, SFT, KL-Regularized RL Through a Bayesian Lens

| Field | Detail |
|-------|--------|
| **Authors** | Junxin Fan |
| **Institution** | Independent theoretical note — *(opencode-compiled)* |
| **arXiv** | [2609.05111](https://arxiv.org/abs/2609.05111) |
| **Submitted** | 6 Sep 2026 (cs.AI) |

**Abstract**: A theoretical note developing a Bayesian perspective that puts SFT, few-shot ICL, KL-regularized RLHF/RLVR, on-policy distillation (OPD), and test-time reasoning on the same footing. Core template: (i) construct a (generalized) Bayes/Gibbs posterior $q^*$ over outputs given a context using a prior/reference model plus a utility signal; (ii) approximate $q^*$ via forward-KL projection onto a parametric family, either in-weights (SFT/RL) or in-context (ICL).

**Key innovations**:
- Shows KL-regularized RLHF/RLVR, reward-weighted SFT, reward-weighted ICL (RW-ICL), and advantage-weighted SFT are all instances of **forward-KL projection onto reward/advantage-induced posteriors**; disentangles where equivalences hold (objectives, first-order updates) vs. not (signal source/granularity).
- Explains *why* cold-start/SFT warm-up is practically unavoidable for importance-weighted KL projections, and frames DeepSeek-R1/o1-style reasoning as **test-time Bayesian search + training-time KL amortization** — relevant to the OPD-then-RL thread from 2609.04108.

---

### 5. What Matters in On-Policy Distillation? Data Efficiency and Data Selection

| Field | Detail |
|-------|--------|
| **Authors** | Zhinan Hou, Jiaqi Zhang, Xunliang Cai, Keyou You |
| **Institution** | Academic (Tsinghua University) — *(opencode-compiled)* |
| **arXiv** | [2609.05198](https://arxiv.org/abs/2609.05198) |
| **Submitted** | 6 Sep 2026 (cs.AI) |

**Abstract**: On-Policy Distillation (OPD) is a widely adopted post-training paradigm, but its data-centric mechanisms are underexplored. The authors investigate an extreme setting — **1-shot OPD** (training on a single example) — and find it consistently effective across all sampled examples, with harder examples yielding superior gains. The driver is not high token entropy but the **longer CoT paths** that hard problems naturally produce: lengthier CoT keeps the student aligned with the teacher over a long reasoning horizon and teaches critical reflection patterns (`Alternatively`) absent from short CoTs.

**Key innovations**:
- **Long-CoT, not entropy, is the OPD signal**; even "unsolvable" examples beyond the teacher's capability can be used successfully.
- A simple **hard-example-only selection** rule: training on just **8 selected hard examples** matches the 17K-dataset baseline across four models (1.5B–7B) — a dramatic data-efficiency result with practical implications for the OPD-recipes thread (cf. RISE 2609.05295, Sequential Beats Joint 2609.04108).

---

### 6. RISE: Recursive Improvement via Self-Extrapolating Policy Distillation

| Field | Detail |
|-------|--------|
| **Authors** | Yang Li, Semih Yavuz, Shafiq Joty |
| **Institution** | Industry (Salesforce AI Research) — *(opencode-compiled)* |
| **arXiv** | [2609.05295](https://arxiv.org/abs/2609.05295) |
| **Submitted** | 6 Sep 2026 (cs.AI) |

**Abstract**: OPD's effectiveness is bottlenecked by teacher quality: external teachers suffer distribution mismatch, while self-distillation with privileged conditioning is limited by in-context capacity. **RISE** constructs a synthetic teacher directly from the model's **own RLVR training trajectory** by extrapolating the displacement between the current checkpoint and a trailing anchor — in parameter space or output logit space — converting a sparse outcome-induced parameter update into a dense token-level target, with no external model or privileged conditioning.

**Key innovations**:
- **Self-extrapolating teacher** refreshed each iteration → distillation becomes *recursive improvement* rather than one-shot compression; combines RLVR (grounds the extrapolation) + OPD (refines token decisions) in a complementary loop.
- Beats RLVR-only training and on-policy self-distillation across math reasoning, multi-domain STEM, code, and multi-turn agentic tasks — a direct contribution to the on-policy-distillation consolidation theme of late-August/early-September digests.

---

### 7. ACE: Adaptive Calibration-Free Expert Skipping for MoE-based LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Zukang Xu, Zhixiong Zhao, Xing Hu, Jiangyong Yu, Houji Wen, Jun Li, Zhe Jiang, Dawei Yang |
| **Institution** | Industry + academic (Huawei-affiliated + university) — *(opencode-compiled)* |
| **arXiv** | [2609.05228](https://arxiv.org/abs/2609.05228) |
| **Submitted** | 6 Sep 2026 (cs.AI) |

**Abstract**: Fixed top-k routing activates the same number of expert slots for every token, causing redundant compute; existing expert-skipping relies on router confidence, calibration data, or extra training and cannot reliably estimate a routed expert's true contribution. **ACE** is a training-free, calibration-free, checkpoint-preserving token-adaptive expert-skipping framework for MoE LLMs, combining a **Global Spectral Proxy (GSP)** (estimates global transformation capacity from coupled gate/up/down projections + RMSNorm scaling) and a **Router-Conditioned Refinement (RCR)** (expert-specific direction prototypes from centered router weights, evaluated along routing-preferred directions).

**Key innovations**:
- Skips an expert slot **only when both views** agree it is low-contribution, always retaining top-1; all statistics computed offline (only table lookups online).
- At **50% skipping** on Qwen3.6-35B-A3B, reduces WikiText-2 perplexity by **7.96%** and improves average downstream accuracy by **4.15 pp** over the strongest competing method across three MoE LLMs and eight benchmarks.

---

### 8. DEX-Comp: Compression Beyond the Uncompressed (Soft Context Compression in RAG)

| Field | Detail |
|-------|--------|
| **Authors** | Shuyu Guo, Shuo Zhang, Zhaochun Ren |
| **Institution** | Academic (Univ. of Amsterdam / Radboud et al.) — *(opencode-compiled)* |
| **arXiv** | [2609.05152](https://arxiv.org/abs/2609.05152) |
| **Submitted** | 6 Sep 2026 (cs.CL) |

**Abstract**: Soft context compression encodes each retrieved document into a shorter embedding sequence, but prior approaches are trained by distilling outputs from *uncompressed* RAG systems, capping performance at the original model's level. **DEX-Comp** uses a two-stage recipe: **Pure Distillation** warm-starts the compression model on the uncompressed RAG's correct responses only, then **Hard Exploration** runs RL solely on queries the uncompressed RAG *fails*, forcing the model to explore computation patterns suited to compressed representations.

**Key innovations**:
- Compresses retrieved contexts **16×** and accelerates inference **4×–24×** while meeting or exceeding uncompressed-RAG performance across retrieval depths (top-5 to top-30) on five open-domain QA benchmarks.
- "Train beyond the teacher" via hard-exploration RL — a RAG-side analogue of the reasoning-RL observation that failing/hard examples carry the learning signal (cf. 2609.05198).

---

### 9. At Equal Inference Cost, Multi-Agent Structure Does Not Beat a Single Frozen Agent

| Field | Detail |
|-------|--------|
| **Authors** | David Dylan, Aoife Brennan, Cian Murphy, Niamh O'Sullivan, Conor Kelly, Saoirse Walsh |
| **Institution** | Academic / industry research — *(opencode-compiled)* |
| **arXiv** | [2609.04217](https://arxiv.org/abs/2609.04217) |
| **Submitted** | 5 Sep 2026 (cs.MA) |

**Abstract**: Multi-agent LLM pipelines (Planner-Executor-Critic teams) often report gains over single agents, but typically at higher inference cost. The authors fix the total number of language-model calls and evolve either a team or a single agent under the **same budget** — introducing **MA-Evolve**, which represents a Planner-Executor-Critic team as three evolvable role prompts optimized by per-role coordinate ascent over a shared frozen 7B backbone.

**Key innovations**:
- On ALFWorld, evolving a single executor significantly beats the unevolved agent; the full team hits the highest mean but is **not statistically better** than the single agent (0.769 vs 0.754, p=0.80) despite 1.8× more evaluation calls.
- **Leave-one-in analysis** shows all realized value comes from the executor; planner and critic evolve to empty/low-impact prompts. On WebShop, evolution is null and the team trends worse — a rigorous *negative result* on multi-agent value under matched compute (complements the MAS theme and 2609.05279 "agent interchangeability").

---

### 10. EvoHarnessBench: Can Your Agents Keep Pace with an Evolving Harness?

| Field | Detail |
|-------|--------|
| **Authors** | Zixuan Ke, Vaidehi Patil, Haizhou Shi, Yang Li, Ye Liu, Sarath Shekkizhar, Anurag Koul, Jiayu Wang, Xuan Phi Nguyen, Semih Yavuz, Mohit Bansal, Shafiq Joty |
| **Institution** | Industry + academic (Salesforce AI Research + Univ. of North Carolina et al.) — *(opencode-compiled)* |
| **arXiv** | [2609.04280](https://arxiv.org/abs/2609.04280) |
| **Submitted** | 5 Sep 2026 (cs.MA / cs.CL) |

**Abstract**: LLM agents operate through a *harness* of tools, reusable skills, and specialist agents that is continually evolving. Existing agent continual-learning benchmarks place non-stationarity in the task stream while keeping the harness fixed; **EvoHarnessBench** instead places non-stationarity in the **externally supplied harness itself** — 17 multi-stage harness streams, 802 tasks, 520 tools, 42 skills, 62 agents, built from verifier-based benchmarks.

**Key innovations**:
- Two settings: **deployment evaluation** (retention as harness expands) and **self-evolving adaptation evaluation** (does accumulated experience stay useful?).
- Three persistent gaps: **harness-induced forgetting** (expansion alone degrades previously-solved tasks); inconsistent self-evolving gains across stages/axes/environments; and retention vs. adaptation can pull in **opposite directions** — establishing harness evolution as a distinct agent challenge.

---

## Recommendation Systems

### 11. AlleCompanion: Beyond Co-purchase — Complementary Recommendations at Allegro

| Field | Detail |
|-------|--------|
| **Authors** | Aleksandra Osowska-Kurczab, Klaudia Nazarko, Eliška Kosturová, Lidia Wojciechowska, Michał Bień |
| **Institution** | Industry — **Allegro** (production retrieval) |
| **arXiv** | [2609.05063](https://arxiv.org/abs/2609.05063) |
| **Submitted** | 6 Sep 2026 (cs.IR) — **RecSys 2026 OARS Workshop** |

**Abstract**: When a customer adds a professional camera to their cart, should the system suggest a matching lens, a generic tripod, or another camera body? Complementary Product Recommendation is vital for basket building, yet standard models often fail to distinguish items merely *bought together* from items that truly *work together*. **AlleCompanion** is a production-scale retrieval framework deployed at Allegro that transforms noisy behavioral signals into precise semantic compatibility.

**Key innovations**:
- **Category-constrained Two-Tower** with a **Category Adapter** guiding candidates within logically complementary boundaries, plus **ComCat** — a multi-source Complementary Categories Mapping that distils patterns from noisy traffic using expert rules, human-in-the-loop feedback, LLM reasoning, and statistical mining.
- Serving **20M+ active users monthly** with significant attributed-GMV uplifts for organic discovery and substantial sponsored-placement revenue growth.

---

### 12. AtomRec: Evolving Atomic Memory for Agentic Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Peiyu Hu, Weihai Lu, Siying Gu, Zhuodong Liu, Zhaokai Luo, Yuean Niu, Zhiyong Wang, Jia Wang |
| **Institution** | Industry + academic — *(opencode-compiled)* |
| **arXiv** | [2609.04882](https://arxiv.org/abs/2609.04882) |
| **Submitted** | 7 Sep 2026 (cs.IR) |

**Abstract**: Agentic recommenders use LLMs to maintain semantic memory for evidence-aware recommendation, but existing memory mechanisms compress user/item info into coarse summaries connected by scalar collaborative links, struggling to preserve fine-grained preference stages or retrieve interpretable evidence as interests evolve. **AtomRec** builds *evolving atomic collaborative memory*: structured atomic units for user and item memories, semantic links across related memories, and evolution of related historical fields as new interactions arrive.

**Key innovations**:
- Retrieves **multi-hop evidence paths** (linked memories) rather than isolated neighbor summaries, letting collaborative signals support grounded ranking.
- **~8.5% average relative improvement** over state-of-the-art agentic and memory-augmented baselines across four public benchmarks.

---

### 13. PTDG: Personalized Task Dependency Graphs for Multi-Task Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Fuyuan Liu, Tiandeng Wu, Yaqun Fang, Wei Zhou, Zehao Zhou, Wenping Chen, Qishun Mei, Jiaxin Zhou, Heng Chang, Yi Cao, Jiandong Ding |
| **Institution** | Industry (large Chinese e-commerce/ad platform) — *(opencode-compiled; author cluster overlaps IGPO/Alibaba)* |
| **arXiv** | [2609.04862](https://arxiv.org/abs/2609.04862) |
| **Submitted** | 7 Sep 2026 (cs.IR) — **CIKM 2026** |

**Abstract**: Optimizing multiple conversion objectives in industrial recommendation is often limited by *signal erosion* in rigid architectures: existing Multi-Task Learning methods enforce uniform dependency strengths across a static conversion funnel, overlooking how task correlations vary by item. Hierarchical message passing along fixed chains causes cumulative signal attenuation on sparse, deep-funnel objectives. **PTDG** dynamically "rewires" dependency-pathway intensity per item via low-rank approximation while respecting physical causal constraints (e.g., Click → Pay).

**Key innovations**:
- **GCN-based propagation with hard causal masking** creates adaptive information shortcuts; **Adaptive Progressive Masking (APM)** decouples shared parameters by task sparsity for stable optimization.
- Improves sparse-conversion-task AUC by up to **1.45%** on KuaiRand1K + industrial data; online A/B: **CVR +1.2%** and **eCPM +1.9%** relative to baseline.

---

### 14. Latent-Aligned Reasoning for Multimodal Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Jiarui Jin, Anyang Ji |
| **Institution** | Academic (Zhejiang University-affiliated, Jiarui Jin) — *(opencode-compiled)* |
| **arXiv** | [2609.04645](https://arxiv.org/abs/2609.04645) |
| **Submitted** | 6 Sep 2026 (cs.IR / cs.CL / cs.CV) |

**Abstract**: Vision-Language Models show strong cross-modal understanding, yet as representations propagate through multi-step reasoning, both visual and textual signals progressively attenuate — *cross-modal dilution*. **LARK** is a two-stage latent reasoning framework with complementary alignment mechanisms within a single VLM: (1) learnable latent tokens interleaved with multi-step CoT and **explicitly aligned to a frozen vision encoder**, serving as visual checkpoints that preserve perceptual detail; (2) latent representations projected via a bridge MLP and trained with item-to-item contrastive learning, intermediate features aligned to first-stage CoT hidden states to anchor final embeddings to the model's own reasoning.

**Key innovations**:
- State-of-the-art across three public benchmarks + one industrial dataset, with ablations confirming each component's distinct contribution — part of the growing multimodal-reasoning-for-rec line.

---

### 15. MURAL: Multimodal Uncertainty-aware Recommendation via Adaptive Edge Learning

| Field | Detail |
|-------|--------|
| **Authors** | Ahmad Mousavi, Majid Alikhani, Yeon-Chang Lee, Roberto Corizzo, Yeganeh Abdollahinejad |
| **Institution** | Academic (American Univ. / UNIST / Michigan State Univ.) |
| **arXiv** | [2609.04574](https://arxiv.org/abs/2609.04574) |
| **Submitted** | 6 Sep 2026 (cs.IR / cs.LG) |

**Abstract**: Multimodal GNNs have become standard for recommendation, but face two bottlenecks: *structural rigidity* (static precomputed similarity graphs that can't adapt to evolving preferences) and *semantic fragility* (noisy modality signals indiscriminately fused, distorting collaborative signal). **MURAL** shifts multimodal rec from fixed structural augmentation to **dynamic topology discovery**.

**Key innovations**:
- **Adaptive Edge Learner** combines differentiable retrieval-augmented search with ANN to discover latent item-item correlations — semantically adaptive and computationally scalable (O(N log N)).
- **Uncertainty-Aware Fusion** models aleatoric uncertainty of modalities, down-weighting unreliable features; **contrastive teacher-student alignment** anchors modality representations to stable behavioral signals without gradient leakage.
- Significantly surpasses structural and generative SOTA on large-scale benchmarks (TikTok, Amazon), with interpretability + robustness under data corruption.

---

### 16. Distill Globally, Adapt Locally: Reasoning Distillation + Product-Type TTT for Trade-Up Rec

| Field | Detail |
|-------|--------|
| **Authors** | Siliang Liu, Mohammad Ghasemi, Sapan Patel, Amin Banitalebi-Dehkordi |
| **Institution** | Industry (Amazon-affiliated) — *(opencode-compiled)* |
| **arXiv** | [2609.05363](https://arxiv.org/abs/2609.05363) |
| **Submitted** | 7 Sep 2026 (cs.LG) — **RecSys 2026 GenAIECommerce Workshop** |

**Abstract**: Trade-up recommendation identifies higher-quality alternatives preserving purchase intent; LLMs reason about such distinctions but can't be applied directly to hundreds of millions of product pairs. A two-level framework distills LLM reasoning into an efficient non-generative student and adapts its decision boundary to product-type-specific criteria.

**Key innovations**:
- **Level 1**: retrieval-augmented few-shot LLM teacher generates structured labels + natural-language rationales that supervise a compact embedding-pair classifier via alignment + contrastive objectives; student uses only two precomputed 768-d product embeddings — no LLM calls at inference. A 15.5M-param four-class student hits **AUC 0.924** (vs 0.912 label-only), on 8,352 human-annotated pairs.
- **Level 2**: product-type test-time training (PT-TTT) with few-shot demonstrations raises AUC to **0.941**.
- On a 100K-pair proxy catalog, the distilled student is ~**5,000× faster** and ~**10,000× lower cost** than direct LLM inference on a single 8-GPU machine.

---

### 17. AutoLR: Automating Research-to-Launch Review in Industrial Recommenders

| Field | Detail |
|-------|--------|
| **Authors** | Qi Zhang, Yanlin Chen, Wenchao Xiao |
| **Institution** | Industry — **NetEase DASHEN** (gaming-community app) |
| **arXiv** | [2609.04871](https://arxiv.org/abs/2609.04871) |
| **Submitted** | 6 Sep 2026 (cs.AI) |

**Abstract**: Improving an industrial recommender is an iterative research-and-engineering process, not a direct path from idea to deployment. LLMs can assist individual stages but the overall process stays human-dependent without a harness that coordinates them across long-running, often multi-day experimental cycles. **AutoLR** (initially *Auto Launch Review*, later extended upstream) is an autonomous research-to-launch harness.

**Key innovations**:
- **Multi-expert council** debates/adversarially reviews proposals; a **deterministic evidence-weighted E/E selector** allocates a limited trial budget across candidate directions; a **layered knowledge system** combines external research, production knowledge, and DASHEN domain knowledge (game communities, player characteristics) with posterior evidence from configs/patches/logs/offline outcomes.
- LLM agents do semantic reasoning + code generation while **deterministic controllers retain authority** over execution, metric extraction, guardrails, and state transitions — an industrial "agent orchestration with hard guardrails" reference case (cf. RecEvolve 2609.01622).

---

## CTR Prediction, Advertising & Search

### 18. SAM-D2Q: Business-Aligned Multimodal Doc2Query for E-commerce Search

| Field | Detail |
|-------|--------|
| **Authors** | Hui Zhou, Jian Hui Ji, Lei Ma, Rong Xiao, Xiaoyi Zeng |
| **Institution** | Industry — **AliExpress / Alibaba** (production search) |
| **arXiv** | [2609.04961](https://arxiv.org/abs/2609.04961) |
| **Submitted** | 7 Sep 2026 (cs.IR) — **CIKM 2026 Oral Full Paper** |

**Abstract**: E-commerce search suffers vocabulary mismatch between queries and product titles; Doc2Query generates pseudo-queries for document expansion, but traditional methods are text-only and not optimized for business objectives — producing semantically plausible but commercially ineffective expansions and missing image attributes. **SAM-D2Q** is a business-aligned multimodal document-expansion framework under Boolean retrieval constraints.

**Key innovations**:
- Three stages: (1) task-adapted multimodal SFT for vision-language understanding of titles/images/queries; (2) multimodal data augmentation for visual-attribute perception; (3) **RL-based preference alignment toward search business objectives**.
- Deployed in AliExpress production: **GMV +3.38%** and **Pay Count +2.27%** online — a concrete case of aligning generative document expansion with conversion/revenue objectives.

---

### 19. IGPO: Inventory-Grounded Policy-Level Optimization for Training-Free AI Search

| Field | Detail |
|-------|--------|
| **Authors** | Wei Zhou, Tiandeng Wu, Jiandong Ding, Zhufeng Fan, Yi Cao |
| **Institution** | Industry (commercial AI-search; author cluster overlaps PTDG/Alibaba) — *(opencode-compiled)* |
| **arXiv** | [2609.04813](https://arxiv.org/abs/2609.04813) |
| **Submitted** | 7 Sep 2026 (cs.IR) — **EMNLP 2026 Industry Track** |

**Abstract**: Early deployment AI search operates over a frequently updated catalog, so items/properties can't be encoded as stable knowledge. Fine-tuning, RL, and static prompt patches fit poorly. **IGPO** is a training-free approach for fixed AI-search pipelines that separates policy from environment facts: it learns **Policy Guidelines** for acting on runtime inventory evidence rather than memorizing items.

**Key innovations**:
- Online, grounds each query by probing inventory into an **inventory portrait**, injecting relevant guidelines into retrieval/selection prompts; offline, stochastic rollouts grouped by query yield contrastive signal, with an inventory-guided exploration loop distinguishing missed-retrieval from no-matching-support cases.
- **Deployed since May 2026** in a commercial smart-assistant; 14-day A/B shows a **3.17% relative CTR lift** and **38.9% reduction in audited bad cases** — training-free adaptation to a shifting catalog.

---

### 20. Embedding Surgery: Localized Updates for Adaptive Ranking Correction in Dense Retrieval

| Field | Detail |
|-------|--------|
| **Authors** | Maddalena Amendola, Antonio Mallia, Raffaele Perego |
| **Institution** | Academic (Univ. of Pisa / ISTI-CNR) |
| **arXiv** | [2609.05110](https://arxiv.org/abs/2609.05110) |
| **Submitted** | 7 Sep 2026 (cs.IR) — **CIKM 2026** |

**Abstract**: Dense retrieval encodes documents/queries into dense embeddings for semantic search, but since document embeddings are computed offline and stored in static indexes, systems struggle to adapt to user feedback or evolving intent. **Embedding surgery** applies localized, minimal updates to selected document embeddings at query time, guided by editorial feedback, user interactions, or LLM pseudo-labels.

**Key innovations**:
- Formulated as a **convex optimization** enforcing ranking constraints while minimizing changes to affected document representations.
- Consistent gains on TREC DL/Robust/CAsT and MS MARCO (up to **+60.64% relative nDCG@10** on DL-Hard under editorial feedback), robust to noise/shift; updates applied safely to ANN indexes via in-place overwriting (no reconstruction). Complements query-side adaptation (CoRocchio) with additional gains and better noise robustness.

---

## Sequential Modeling & Time-Series

### 21. RCBNB-MB: Non-Stationary Causal Discovery via Markov Blankets and Latent Regimes

| Field | Detail |
|-------|--------|
| **Authors** | Lei Zan, Charles K. Assaad, Emilie Devijver, Eric Gaussier |
| **Institution** | Academic (Univ. Grenoble Alpes / LIG) — *(opencode-compiled)* |
| **arXiv** | [2609.05150](https://arxiv.org/abs/2609.05150) |
| **Submitted** | 6 Sep 2026 (cs.LG) — **ECML PKDD 2026 AALTD Workshop** |

**Abstract**: A causal-discovery algorithm for time series that relaxes the assumption of a single, time-consistent causal structure. **RCBNB-MB** identifies *latent causal regimes* — subsets of time points within which a stable causal structure holds — by segmenting the series and discovering the causal graph within each regime, leveraging the **Markov blanket** (rather than direct parents) for robustness and predictive information preservation.

**Key innovations**:
- Theoretical guarantees for recovering both regime transitions and causal graphs under reasonable assumptions.
- Systematically outperforms baselines on simulated data with known ground truth and real-world **IT monitoring data** — a practical answer to "beyond stationarity" for sequential/dynamic systems (relevant to CTR/feature-dynamic and time-series forecasting threads).

---

## Games, Game Theory & Multi-Agent Systems

### 22. Abstraction Agent: LLM-Discovered Strategic Features for Imperfect-Information Games

| Field | Detail |
|-------|--------|
| **Authors** | Boning Li, Longbo Huang |
| **Institution** | Academic (Tsinghua University) |
| **arXiv** | [2609.04303](https://arxiv.org/abs/2609.04303) |
| **Submitted** | 5 Sep 2026 (cs.MA / cs.GT) |

**Abstract**: Information abstraction groups strategically similar private states into tractable buckets — essential for scaling game-solving to large imperfect-information games, but constructors traditionally require domain-specific evaluators (hand-strength calculators, equity estimators). The **Abstraction Agent** is a **zero-shot LLM pipeline** that discovers continuous strategic features from a natural-language game description, scores private states, and clusters them into abstraction buckets — no game-specific evaluator, training data, or game-tree traversal during construction.

**Key innovations**:
- Four phases: feature discovery with calibration anchors, batched state scoring, correlation-based feature selection, $k$-means clustering.
- Reduces lifted-strategy exploitability by up to **62%** vs expected-hand-strength baseline on HUNL turn endgames; beats a scalar rank baseline on **ROVER Trials** (a game absent from any pretraining corpus); transfers unchanged to PLO, HUNL preflop/flop, and Riichi Mahjong — structured knowledge elicitation turning implicit LLM strategic knowledge into explicit numeric features.

---

### 23. PPR: Online Change-point Detection for Cooperative Multi-Agent RL

| Field | Detail |
|-------|--------|
| **Authors** | Fatemeh Saberi Khomami, Julita Vassileva |
| **Institution** | Academic (Univ. of Saskatchewan) |
| **arXiv** | [2609.05298](https://arxiv.org/abs/2609.05298) |
| **Submitted** | 6 Sep 2026 (cs.MA) — **PAAMS 2026** |

**Abstract**: Cooperative MARL relies on past experience that may become unreliable if the environment or task objective changes during training; agents first need to *recognize* change before adapting. The authors propose **Patterns of Past Rewards (PPR)**, a lightweight algorithm-agnostic detector that smooths agents' return streams, highlights recent changes, and applies a statistical drift detector to flag shifts.

**Key innovations**:
- Evaluated in a custom Speaker-Listener (Multi-Agent Particle) environment under two controlled non-stationarity scenarios; shows a detection-speed vs. alarm-stability trade-off — smoothed returns detect earlier but alarm repeatedly, raw returns often miss the shift, while PPR balances the two.
- A lightweight reward-based monitoring primitive for making cooperative MARL robust to task/environment drift.

---

## Cross-Cutting Observations

- **On-policy distillation hits a data-efficiency inflection point**: 2609.05198 shows **8 hard examples match a 17K dataset** (the driver is long CoT, not entropy), and RISE (2609.05295) makes OPD *recursive* by self-extrapolating a teacher from the model's own RLVR trajectory. These extend the OPD consolidation thread (2609.04108 "sequential beats joint", Rethinking OPD 2609.04172) toward "algorithm-starved, not data-starved" and teacher-free recipes.
- **A Bayesian unification of post-training**: 2609.05111 casts ICL/SFT/KL-RL/OPD as forward-KL projection onto reward/advantage-induced posteriors, explaining *why* SFT warm-up is practically necessary (cold-start of importance-weighted KL projections) — a tidy theoretical counterpart to the empirical stage-ordering results.
- **Long-CoT inference remains the dominant bottleneck**: BeaconKV (2609.04971) targets Thought-Revisiting-Token clusters with 5.8× KV memory reduction / 4.3× throughput, joining Random Attention (2609.03430), VestigeKV (2609.03949), and the cache/router work as the week's acceleration theme.
- **Critical tests of multi-agent value**: 2609.04217 (equal-inference-cost: a team of three frozen-backbone agents is *not* statistically better than the single executor; thinker/critic evolve to empties) and 2609.04280 EvoHarnessBench (harness-induced forgetting, retention-vs-adaptation tension) both push back on naive "more agents = better" — with a rigorous *lower-bound* theory contribution in 2609.05318 for agentic networked aggregation.
- **Industrial rec returns to search/generative alignment**: SAM-D2Q (AliExpress, GMV +3.38%) aligns multimodal Doc2Query with business objectives via RL preference alignment; AlleCompanion (Allegro, 20M users) uses category-constrained two-tower + ComCat for true complementary rec; both pair an LLM/neural component with explicit domain/constraint structure. AutoLR (NetEase) and IGPO automate the research/ops loop with deterministic guardrails — signal eroduction/multi-task explicit dependency graphs (PTDG, eCPM +1.9%) round out a strongly industrial, search-and-conversion-oriented cs.IR batch.
- **Modal reasoning and uncertainty enter rec**: LARK (latent-aligned, cross-modal-dilution-aware) and MURAL (uncertainty-aware adaptive edge learning, O(N log N) topology discovery) both push multimodal GNN/LLM rec beyond static structural augmentation — consistent with the generative/multimodal-rec maturation noted through August.
- **Games: abstraction, not just self-play**: the Abstraction Agent (2609.04303) is a notable *zero-shot data-free* alternative to expert-built evaluators for imperfect-information game abstraction (62% exploitability reduction, transfers across 4 games) alongside the lighter PPR drift detector for MARL — two distinct ways to make game/RL systems adaptive without bespoke supervision.

> ⚠️ NOTE: Entries marked "opencode-compiled" have institutions/companies inferred from author affiliations embedded in papers/HTML versions, project pages, or domain knowledge; arXiv abstract pages carry no canonical institution field. Verify against arXiv `/html/` pages or the papers before citing institution names in formal writing. Titles, IDs, abstracts, and arXiv links are as retrieved from arxiv.org on 2026-09-07 (Mon 7 Sep 2026 mailing). A handful of IDs fall slightly earlier in the 2609.04xxx range (e.g., 2609.04217, 2609.04303) but are confirmed absent from all prior wiki digests via grep.
