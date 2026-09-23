---
title: "arXiv Daily — AI / LLM / Recommendation / Advertising / CTR / Sequential Modeling / Games"
type: synthesis
created: 2026-09-23
updated: 2026-09-23
sources: [arxiv.org]
tags: [arxiv-daily, AI, LLM, recommendation, advertising, CTR, e-commerce, image-editing, RAG, ranking, search, user-simulation, table-integration, post-training, RL, test-time-scaling, LoRA, self-distillation, curriculum, chain-of-thought, MoE, expert-pruning, quantization, KV-cache, sparse-attention, speculative-decoding, context-compression, time-series, streaming, tabular-FM, recursive-models, multi-agent, agent-memory, conformal, agent-reliability, world-models, games, procedural-character, interpretability, attribution, fit, benchmark, safety, daily-digest]
---

# arXiv Daily Report — 2026-09-23

> **Mailing status**: **Wednesday, 23 September 2026** window established via **arXiv API tail sweep** (the `/list/{cat}/new` pages at run time still announced the Tue-22 batch that the 09-22 siblings claimed, IDs ≤ 2609.24554). Fresh in-window IDs span **2609.25504–2609.26796**, **277 unique entries** all published **2026-09-22** (primary-cat spread: cs.LG 57 / cs.CV 47 / cs.CL 41 / cs.AI 34 / cs.RO 14 / stat.ML 11 / cs.HC 11 / rest <11 each).
> **Methodology**: `export.arxiv.org` API pagination (newest-first, 6 pages × 100) per category across **cs.AI / cs.LG / cs.CL / cs.IR / cs.CV / cs.GT / cs.MA / cs.NE / cs.HC / cs.CY / cs.DC / cs.SI / stat.ML**; entries filtered to `published = 2026-09-22` and `num > 24554` (the 09-22 sibling max). Window JSON cached under `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv-daily-0923/` (pre-approved temp dir) and cleaned up after. Screened all 277 titles → 43 abstracts deepened → **37 featured papers across 8 sections + 6 runner-ups**. Every featured/runner-up ID was **grep-verified 0 hits in `wiki/`** at write time (structurally fresh: all above the 09-22 sibling max). Institutions are author-affiliation inferred where arXiv does not print them (marked *tentative*).
> **CTR/ads note**: The direct end-to-end CTR-model drought continues at the daily layer, but this window's flagship industrial paper **KwaiMind (Kuaishou)** is firmly advertising-adjacent — CTR is used as a **reward signal** for commercial image-editing RL, and its Ecom-Bench scores images by predicted CTR (offline: 12.16%→37.41% "generated image beats original" rate; online A/B: **+2.44% actual CTR**). A second industrial item, **QSS (audio-streaming search)**, tackles shortcut-learning in LLM reranking with behavioural stats. The classic end-to-end CTR/pCVR-ML line remains silent (\≈10 consecutive windows).

---

## 1. Recommendation, Advertising & E-commerce

### 1.1 KwaiMind Technical Report

| Field | Detail |
|-------|--------|
| **Authors** | Junlong Wu, Zijun Li, Yuting Hu, Jia Sun, Pengcheng Wei, Yimin Zhou, Honglie Wang, Huaiqing Wang, Dewen Fan, Fei Zuo, Haixuan Gao, Lihui Peng, Tingxuan She, Yuqing Li, Boheng Zhang, Fan Yang, Wenwu Ou |
| **Institution** | Kuaishou Group (KwaiMind Team, stated in comment) |
| **Published** | 22 Sep 2026 (cs.CV) |
| **Abstract** | Commercial image editing requires product identity preservation, accurate text rendering, and user appeal alongside general editing quality. **KwaiMind** is an image-editing system combining general capabilities with e-commerce specialization: an agent-based data engine maintains ~1.8M high-quality editing pairs; built on a multimodal diffusion transformer, it undergoes continued pretraining + SFT, then preference optimization and online RL. A general-purpose VLM judge and specialized rewards for **CTR, text rendering, and product consistency** guide specialized policies consolidated via on-policy distillation. Introduces **Ecom-Bench** (11 commercial editing tasks with task-specific visual eval + CTR-based ranking). |
| **Key Innovations** | (1) CTR as a first-class reward signal in generative commercial-image editing — spending RL budget on what users actually click, not just perceptual quality; (2) Ecom-Bench with CTR-based ranking (the first e-com image-editing benchmark scored on predicted engagement); (3) deployment-grade recipe: agentic data engine + specialized multi-reward RL + on-policy distillation; offline "image beats original" rate 12.16%→37.41%, online A/B **+2.44% CTR**. |
| **Link** | [arXiv:2609.26375](https://arxiv.org/abs/2609.26375) |

### 1.2 Robust Fusion of Semantic and Behavioural Signals for LLM Reranking in Personalised Search

| Field | Detail |
|-------|--------|
| **Authors** | Aleksandr V. Petrov, Nathan Stein, Erik Lybecker, Emma Schüldt, Daniel Lazarovski, Hugues Bouchard, Mounia Lalmas |
| **Institution** | Large-scale audio streaming platform (Spotify; inferred — Petrov/Lalmas lineage) |
| **Published** | 22 Sep 2026 (cs.IR) — accepted, USRW Workshop @ RecSys 2026 |
| **Abstract** | LLM cross-encoders give a single reranking interface for personalised search, but injecting predictive behavioural statistics into prompts encourages **shortcut learning**: reliance on historical signals at the expense of semantic/user-context patterns that generalize to sparse or unseen searches. Studied on the platform using **QSS** (Query Slice Stats, interaction-derived behavioural feature of historical query-candidate success). Naive QSS injection improves ranking when available but reduces robustness when removed. Fix: **deterministic dual-sample feature-dropout training** — each example seen once with QSS included and once removed. |
| **Key Innovations** | (1) Diagnoses prompt-injected behavioural-feature shortcut learning in production personalised search; (2) training-free-at-deploy dual-sample trainer preserving available-feature gains (+13.3% offline) while adding robustness when the feature is missing (+4.0% relative over naive in QSS-removed eval); (3) live online test: both QSS-aware variants ≈+2% search success. |
| **Link** | [arXiv:2609.25825](https://arxiv.org/abs/2609.25825) |

### 1.3 A Behavioral Trait Leaks into Preferences: Diagnosing Trait Interference in LLM User Simulators

| Field | Detail |
|-------|--------|
| **Authors** | Chaehyun Kim, Sein Kim, Hongseok Kang, Chanyoung Park |
| **Institution** | KAIST (inferred; Chanyoung Park) — CIKM 2026 short paper |
| **Published** | 22 Sep 2026 (cs.AI) |
| **Abstract** | LLM user simulators emulate users with injected traits to bridge the offline-online gap in recommender evaluation. But the intended trait independence collapses: **trait interference** — amplified *activity* (browsing depth) distorts *preference* boundaries and forces interactions with mismatched items — and **evaluation invalidity** — satisfaction scores inflate with activity-driven page counts, biasing eval toward trait distributions rather than recommender performance. Fix: **PQA**, page-level quality anchoring — each page is judged against a personalized anchor (the user's own intrinsic preference standard) before further browsing, enabling proactive exit from low-quality pages. |
| **Key Innovations** | (1) Mechanistic diagnosis of a failure in LLM-based simulator evaluation with direct recommender-eval consequences; (2) a cheap, personalized, anchor-based intervention (PQA) restoring trait independence; (3) reliability improvement for simulator-based offline rec evaluation under activity shifts. |
| **Link** | [arXiv:2609.25572](https://arxiv.org/abs/2609.25572) |

### 1.4 Seeing Is Not Perceiving: When Synthetic Consumers Can and Cannot Pretest Visual Marketing

| Field | Detail |
|-------|--------|
| **Authors** | Yi-Lin Tsai, Yung-Hsiu Lai |
| **Institution** | (inferred academic/industry) — six preregistered studies (AsPredicted) |
| **Published** | 22 Sep 2026 (cs.AI) |
| **Abstract** | Marketers deploy generative-AI "synthetic consumers" to pretest visual assets (logos, packaging, ads) at a fraction of human-panel cost — assuming a model *seeing* a visual cue also *perceives* its consumer meaning. Stress-tested across six canonical visual-marketing experiments, varying generation and input format: **every configuration passed manipulation checks, yet none reproduced more than 2 of 6 human effects**; one showed a significant *reversal* of the human pattern. In-context conceptual/empirical evidence steers averages toward the human effect but reproduces less than half the human spread. |
| **Key Innovations** | (1) Rigorous preregistered audit quantifying how far synthetic consumers fall short of human panels (≤2/6 effects); (2) demonstrates steering's limit (understates heterogeneity); (3) a governance protocol — Calibrate, Intervene, Deploy — delineating when AI-pretesting is responsible. |
| **Link** | [arXiv:2609.25677](https://arxiv.org/abs/2609.25677) |

### 1.5 Discovery-Driven Integration of Disjoint Tables via Text

| Field | Detail |
|-------|--------|
| **Authors** | Md Ataur Rahman, Dimitris Sacharidis, Oscar Romero, Sergi Nadal |
| **Institution** | Universitat Politècnica de Catalunya (inferred; Romero/Nadal) |
| **Published** | 22 Sep 2026 (cs.IR) |
| **Abstract** | Data-lake integration fails for semantically related tables lacking joinable explicit attributes. **LOKI** (Latent-space Optimization for Knowledge Integration) formalizes **Text-Mediated Join Path Discovery**: a horizontal bidirectional cross-attention architecture learning contextualized representations of table rows and sentences, aligned by a global table-text contrastive objective — fine-grained row↔sentence associations emerge without local supervision. Implicit associations are converted into explicit, interpretable join paths, grouped into relation-consistent sets, and materialized as typed integrated tables with sentence-level provenance. |
| **Key Innovations** | (1) Fine-grained *row-sentence* discovery (vs coarse column-text) — discovers relational structure, not just relatedness; (2) typed output tables with provenance, benchmarked at 0.982 macro typed-pair precision; (3) up to 40× cheaper in LLM API cost than direct prompting at SOTA discovery quality. |
| **Link** | [arXiv:2609.26658](https://arxiv.org/abs/2609.26658) |

---

## 2. LLM Post-Training, Reasoning & Test-Time Compute

### 2.1 Qwen3.8-Omni: Towards Native Omni-Modal Agents

| Field | Detail |
|-------|--------|
| **Authors** | Qwen Team |
| **Institution** | Alibaba (Qwen) |
| **Published** | 22 Sep 2026 (cs.CL, cs.CV, cs.MM) |
| **Abstract** | **Qwen3.8-Omni-Flash** is a natively multimodal agentic model for real-world multimodal productivity. Native multimodal co-training preserves strong text capability while transferring agentic ability from text to audio/video; inherits Qwen3.8-Next's sparse MoE and extends context to **1M tokens**, supporting long-context multimodal reasoning and long-horizon planning. Ships **Qwen-MM-Plugins** (lightweight open-source plugin framework for multimodal productivity) and **Qwen-Live-Harness** (for responsive real-time multimodal agents), framing real-time multimodal interaction as a system orchestration problem (context/memory management, tools, sub-agent delegation). Evaluations cover multimodal understanding, reasoning, long-horizon agentic execution, and video productivity. |
| **Key Innovations** | (1) Native (not bolted-on) omni-modal *agentic* model with 1M context at a sparse-MoE serving cost; (2) the agentic-capability transfer recipe (text→audio/video) while preserving text strength; (3) opens tooling (plugins + live harness) that turns the model into a deployable production agent or sub-agent. |
| **Link** | [arXiv:2609.25611](https://arxiv.org/abs/2609.25611) |

### 2.2 Hill Sampling for Test-Time Scaling: A Simple and Better Alternative to Repeated Sampling, Evolution, and Training

| Field | Detail |
|-------|--------|
| **Authors** | Jacob Beck, Philip V. Ogren, Ari Kobren |
| **Institution** | Oracle Labs (confirmed: Beck is Senior Scientist, Oracle Labs ML Research) |
| **Published** | 22 Sep 2026 (cs.LG) |
| **Abstract** | How much of the elaborate evolutionary-search / test-time-training machinery is necessary? **Hill Sampling**: repeatedly sample candidate program *edits* from a frozen LLM, keep the best program found, condition all later samples on it. On circle packing, sums/differences-of-sets, and Erdős minimum-overlap with three open-weight models: **new SOTA on circle packing**, beats the AlphaEvolve reference on minimum-overlap, all in hours on 8 H100s. Largest-by-param-count study of evolution strategies on LLM *weights* at test time: learning the weights is *worse* than a zero learning rate (fixed random perturbations still explore; token-sampling randomness is stronger). |
| **Key Innovations** | (1) A 10-line-procedure test-time policy beating systems orders of magnitude more complex; (2) negative empirical result on weight-space ES at test time — capacity for exploration lives in token sampling, not weight perturbation; (3) clear allocation guidance: sample edits to the best verified solution before adding archives/diversity/scaffolds/test-time training. |
| **Link** | [arXiv:2609.25510](https://arxiv.org/abs/2609.25510) |

### 2.3 Reasoning-Preserving Fine-Tuning of Post-RL LLMs with Null-Basis LoRA

| Field | Detail |
|-------|--------|
| **Authors** | Wenzhi Fang, Nicholas Tzou, Lazar Valkov, Srinivas Chappidi |
| **Institution** | (inferred industrial/academic) |
| **Published** | 22 Sep 2026 (cs.AI) |
| **Abstract** | Adapting post-RL reasoning models via downstream SFT can overwrite their reasoning capability. Analysis shows **reasoning activations concentrate in low-dimensional subspaces**, leaving substantial null-space capacity for adaptation; approximate null spaces can be estimated from modest data. **NB-LoRA** (Null-Basis Low-Rank Adaptation) formulates reasoning retention as a layer-wise hidden-state preservation constraint, reparameterizing LoRA updates through a fixed approximate null basis of reasoning activations so the constraint holds throughout fine-tuning. |
| **Key Innovations** | (1) Null-basis reparameterization enforcing a preservation constraint *during* adaptation (not post-hoc); (2) matches standard LoRA adaptation performance while keeping reasoning near pre-finetune levels, generalizing to held-out reasoning benchmarks; (3) cheap null-space estimation from few examples — no replay/gradient-projection overhead. |
| **Link** | [arXiv:2609.25618](https://arxiv.org/abs/2609.25618) |

### 2.4 What Should a Self-Teacher See? Privileged Context Design for On-Policy Self-Distillation

| Field | Detail |
|-------|--------|
| **Authors** | Kanghui Tian, Siyuan Liu, Tianxiang Jiang, Shuai Dong, Yizhuo Li, Tian Ding, Yuan Guo, Songze Li, Haowen Hou, Congcong Wang, Yi Wang |
| **Institution** | Hong Kong–based academic cluster (HKUST/HKBU-affiliated; inferred — Songze Li) |
| **Published** | 22 Sep 2026 (cs.LG) |
| **Abstract** | In on-policy self-distillation (OPSD, frozen copy scores the student's own rollouts), the teacher's privileged context is conventionally a full reference solution (final answer + one reasoning path). Is that optimal? Comparing vs three compact offline abstractions (named strategy, method-independent framing, problem category) and an answer-only control on competition math: **best intermediate contexts beat the full solution by +1.4 (4B) / +1.6 (8B) peak mean while storing an order of magnitude fewer hint tokens**; answer-only stays within 0.2 points. Preferred context varies with scale/task; initial teacher-student KL does not order downstream performance. |
| **Key Innovations** | (1) Shows "more privileged info ≠ better teacher" in OPSD — abstraction level is the dial; (2) 10× hint-token reduction with accuracy gains; (3) counterintuitive KL irrelevance for context selection. |
| **Link** | [arXiv:2609.25623](https://arxiv.org/abs/2609.25623) |

### 2.5 Ladders of Thought: A Self-Evolving Curriculum of Progressively Simplified Reasoning Traces

| Field | Detail |
|-------|--------|
| **Authors** | Minghui Liu, Thomas Magelinski, Dehao Yuan, Qi Yu, Furong Huang |
| **Institution** | UMD / CMU / RIT cluster (inferred; Furong Huang is UMD) |
| **Published** | 22 Sep 2026 (cs.AI) |
| **Abstract** | Small/mid-scale LLMs stay brittle reasoners even under knowledge distillation. **LoT** (Ladders-of-Thought) combines progressive question rewriting with a self-evolving curriculum: automatically generate semantically-faithful-but-easier variants, bucket by step-based difficulty, and allocate training via a self-evolving bandit scheduler. Across two reasoning domains, 1–8B models, multiple families: large arithmetic gains (**+32pp AddSub, +25pp SVAMP**), +2–8pp in-domain, and +16pp QASC / +25pp StrategyQA on multi-hop; converges faster than staged curricula. |
| **Key Innovations** | (1) Difficulty ladders + adaptive bandit allocation as a KD-compatible curriculum; (2) training-time curriculum that adapts to model proficiency in real time; (3) strong gains concentrated in small models — a practical recipe where big-model-grade reasoning is out of budget. |
| **Link** | [arXiv:2609.25643](https://arxiv.org/abs/2609.25643) |

### 2.6 Beyond Repeated Sampling: Learning Search Policies for LLM Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | Ismail Labiad, Matthieu Kowalski, Marc Schoenauer, Rémi Munos, Julia Kempe |
| **Institution** | Université Paris-Saclay / INRIA / NYU (inferred; Schoenauer-INRIA, Munos, Kempe-NYU) |
| **Published** | 22 Sep 2026 (cs.CL) |
| **Abstract** | Repeated sampling at test time explores only via local decoding noise → many near-duplicate attempts. Alternative: steer exploration at the *semantic* level — first sample problem-specific concepts/hints/strategies, then condition answer generation. A trainable concept generator is RL-optimized so its concepts maximize downstream success of a **larger, frozen answer generator** (**Concept-Search Policies**). On hard math, it substantially improves pass@k over naive sampling at matched answer-generation budget, surpasses concepts from much larger untuned models, and transfers to answer generators never seen in training, including a different model family. |
| **Key Innovations** | (1) Frames reasoning diversification as a *trainable semantic search policy* (RL on concept space) vs brute-force sampling; (2) shows a small model can be trained into a reusable search policy for a much larger one; (3) cross-family generalization — the policy is answer-generator-agnostic. |
| **Link** | [arXiv:2609.26704](https://arxiv.org/abs/2609.26704) |

### 2.7 Capable yet Parsimonious: Extracting and Characterizing Hidden Chain-of-Thought in Frontier Models

| Field | Detail |
|-------|--------|
| **Authors** | Xiaoyu Luo, Tao Ren, Wenrui Yu, Xiao Li, Qiongxiu Li, Johannes Bjerva |
| **Institution** | Aalborg University (inferred; Bjerva) |
| **Published** | 22 Sep 2026 (cs.CL) |
| **Abstract** | Frontier reasoning claims can't be verified when raw CoT is hidden. By **registering a custom tool through a standard API feature**, closed models are induced to externalize intermediate reasoning. Validation against native CoT on open models extends to closed frontiers incl. **GPT-6 Astra**: extracted reasoning matches native-reasoning performance and beats no-reasoning baselines on competition math, science, code. Characterizing the traces: Astra exhibits **token-efficient directed reasoning** — selects the correct trajectory earlier, resolves elementary steps internally, externalizes only crucial reasoning. |
| **Key Innovations** | (1) A tool-registration harness extracting hidden CoT from closed frontier models via a benign API feature; (2) direct evidence (not benchmark gossip) of how Astra reasons — efficient, compressed, selective externalization; (3) methodology transferabl: evaluate hidden-CoT claims behaviorally. |
| **Link** | [arXiv:2609.26637](https://arxiv.org/abs/2609.26637) |

---

## 3. MoE & Parameter Efficiency

### 3.1 You Only Need 2/3 of the Chosen Experts: Dynamic Expert Pruning in Fine-Grained MoE LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Yuanteng Chen, Qiwei Lai, Chen Tianqi, Peisong Wang, Yuantian Shao, Nanxin Zeng, Zhilei Liu, Chuangyi Li, Jing Liu, Jian Cheng |
| **Institution** | Chinese Academy of Sciences (inferred; Jian Cheng, NLPR) |
| **Published** | 22 Sep 2026 (cs.LG) |
| **Abstract** | Systematic empirical study of expert-pruning redundancy across **12 fine-grained MoE checkpoints spanning 9 architecture families**, 11 benchmarks. Retaining ~2/3 of per-token selected experts preserves **98.8%** of unpruned performance on average (a one-integer change; 1.2–1.7× speedup on two serving backends). At *conservative* budgets, even the best published pruning rules differ from uniform by <1%; their value emerges under aggressive pruning (best rules recover up to 3.0% over uniform truncation, concentrated in generative tasks). Larger/thinking models more resilient; multimodal models more vulnerable. |
| **Key Innovations** | (1) Quantifies how much fine-grained MoE compute is dispensable (uniform 2/3 ≈ near-free 1.2–1.7× speedup); (2) clarifies when dynamic allocation earns its complexity (aggressive budgets only); (3) model-sensitivity characterization (scale/thinking-token training vs multimodal fragility). |
| **Link** | [arXiv:2609.25809](https://arxiv.org/abs/2609.25809) |

### 3.2 From Experts to Sub-experts: Fine-grained Parameter-Efficient Fine-Tuning for MoE LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Zhentao Tan, Chang Liu, Yao Liu, Yue Wu, Jieping Ye |
| **Institution** | Alibaba (inferred; Jieping Ye) |
| **Published** | 22 Sep 2026 (cs.LG) |
| **Abstract** | Activated experts are internally sparse — only a small fraction of intermediate channels strongly respond to a downstream task, so expert-level adaptation is still too coarse. **NSFT** (Neural Sub-expert Fine-Tuning) decomposes each expert along the intermediate dimension into structured channel groups and selects task-relevant **sub-experts** by combining routing importance with intra-expert activation saliency; learning-rate scaling + dynamic gradient scaling compensate the reduced update magnitude. Beats PEFT (LoRA) and expert-level sparse-tuning baselines on OLMoE / Ling-mini-2.0 with substantially fewer trainable parameters. |
| **Key Innovations** | (1) Introduces *sub-expert* granularity — inside-expert structured sparsity exploited for PEFT; (2) principled selection (routing importance × activation saliency) with update-magnitude compensation; (3) strong domain-task wins at far smaller trainable-parameter counts. |
| **Link** | [arXiv:2609.25655](https://arxiv.org/abs/2609.25655) |

### 3.3 Beyond Scalar Sensitivity: Activation-Aware Mixed-Precision LLM Quantization with Cross-Layer Refinement

| Field | Detail |
|-------|--------|
| **Authors** | Akihiro Yoshida, Yuma Ichikawa |
| **Institution** | (inferred academic, JP) |
| **Published** | 22 Sep 2026 (cs.LG) |
| **Abstract** | Mixed-precision quantization (MCKP formulation) relies on scalar sensitivity proxies that collapse each Hessian to one number and treat modules independently. Proof: the optimal scalar proxy incurs multiplicative distortion up to **√(κ(A)κ(B))** vs the full activation-aware quadratic — varying from 10¹ to 10¹³ across typical LLM modules, making ranking unreliable. **CASA** (Cross-layer Activation-aware Sensitivity Allocation): Stage 1 replaces the scalar proxy with a Kronecker-factored-Hessian metric whose continuous relaxation has a closed-form solution; Stage 2 runs a cross-layer-aware local search re-evaluating bit-width updates with the end-to-end loss. |
| **Key Innovations** | (1) A theorem-quantified failure mode of scalar sensitivity (condition-number distortion bound) verified empirically; (2) the closed-form relaxation + global refinement loop; (3) gains concentrated at ultra-low bit-widths (<3 bits), with zero-shot accuracy tracking the per-model average condition number — a practical scalar-proxy-failure indicator. |
| **Link** | [arXiv:2609.25916](https://arxiv.org/abs/2609.25916) |

### 3.4 Disaggregated Quantization: Specializing LLM Prefill and Decode

| Field | Detail |
|-------|--------|
| **Authors** | Andrei Panferov, Maximilian Kleinegger, Sweta Priyadarshi, Tijmen Blankevoort, Dan Alistarh |
| **Institution** | ISTA Vienna / Qualcomm AI Research (inferred; Alistarh/Blankevoort) |
| **Published** | 22 Sep 2026 (cs.LG) |
| **Abstract** | Prefill and decode reward different quantization strategies: low-precision arithmetic speeds prompt *processing*, compact weights cut memory traffic during *generation*. **Disaggregated Quantization (DQ)** specializes compute format, weights, and storage placement per phase. Removing activation quantization *on decode only* improves decode-heavy accuracy at no cost; a compute-native prefiller beats weight-only inference while matching/exceeding accuracy at 2–3-bit decode. **Offloaded Disaggregated Prefill (ODP)** streams prefiller weights from SSD, amortizing load over prompt length: on Qwen3.8-27B, **1.78× TTFT speedup** vs weight-only at 8K prompt in llama.cpp, validated up to 2.8T-param models in vLLM. |
| **Key Innovations** | (1) Phase-specialized quantization (compute-native prefill weights + compact decode weights) as a first-class design axis; (2) SSD-offload of the second checkpoint to keep single-device deployment; (3) 1-bit accuracy recovery of +32.5 MMLU-Pro / +35.3 MMMU-Pro over the decode-only baseline. |
| **Link** | [arXiv:2609.26333](https://arxiv.org/abs/2609.26333) |

---

## 4. Attention, KV-Cache & Inference Serving

### 4.1 Latest Exact Match Attention (LEMA)

| Field | Detail |
|-------|--------|
| **Authors** | Moritz Brösamle |
| **Institution** | (single author, inferred academic — DE) |
| **Published** | 22 Sep 2026 (cs.LG) |
| **Abstract** | **LEMA** binarizes queries and keys; each query attends only to the **latest exactly matching key**. Provable: LEMA + CoT simulates word-RAMs (as shown for looser rightmost hard attention), and — uniquely — word-RAMs can simulate LEMA at **per-token cost independent of context length**, giving a tight two-way correspondence. Trained via straight-through binarization + annealed soft attention surrogate: on synthetic associative recall, LEMA stores/recalls more associations than gated DeltaNet with fixed state. At 834M params, LEMA matches softmax transformers of ~half size in loss, beats GDN on long-range recall. Dictionary-based inference runs at constant generation speed with state in main memory. |
| **Key Innovations** | (1) Exact-match attention with a *reverse* simulation result (word-RAM simulates LEMA → constant per-token cost) — unique among hard-attention variants; (2) a fully training-compatible recipe (STE + annealed surrogate); (3) main-memory dictionary runtime: growing state without growing per-step cost. |
| **Link** | [arXiv:2609.25802](https://arxiv.org/abs/2609.25802) |

### 4.2 CompKV: Compensation-Aware KV Selection for Long-Context LLM Inference

| Field | Detail |
|-------|--------|
| **Authors** | Zhen Huang, Ruizhe Yao, Danyi Liu, Xinrui Chen, Shuwei Li, Siru Zhong, Zijian Cao, Yushan Lai, Mingming Guo, Weijie Zheng, Haohuan Fu |
| **Institution** | Tsinghua-affiliated cluster (inferred; Haohuan Fu) |
| **Published** | 22 Sep 2026 (cs.LG) |
| **Abstract** | Sparse attention selects a token subset for exact attention and coarsely compensates the omitted tail. Existing methods select by attention mass *then* compensate — a decoupled design ignoring their interaction. **CompKV** is the first *compensation-aware* sparse-attention framework: tokens are divided into blocks and selection explicitly optimizes for the downstream compensation mechanism. Theory: the block-level-mean-compensation residual is governed by both block attention mass and within-block logit variation; this residual is approximated by compact block statistics → a deployable criterion; efficient asynchronous implementation. |
| **Key Innovations** | (1) Fuses selection and compensation into one objective (selection should drop tokens that are *cheap to compensate*, not merely low-mass); (2) an approximation-of-residual selection criterion grounded in theory; (3) up to **6.85× self-attention speedup** over full attention, best among evaluated sparse baselines on RULER + LongBench-Pro. |
| **Link** | [arXiv:2609.26300](https://arxiv.org/abs/2609.26300) |

### 4.3 HySparse2: Hybrid Sparse Attention with Two-Level KV Sharing

| Field | Detail |
|-------|--------|
| **Authors** | Jianyu Wei, Yizhao Gao, Qihao Zhang, Shimao Chen, Zhengju Tang, Yu Cheng, Shengjie Zhou, Zihan Jiang, Yifan Song, Hailin Zhang, Liang Zhao, Bo Yang, Gang Wang, Shijie Cao, Fuli Luo |
| **Institution** | Microsoft (inferred; Fuli Luo / Shijie Cao / Gang Wang) |
| **Published** | 22 Sep 2026 (cs.CL) |
| **Abstract** | Long-horizon/multi-turn agents need efficient prefill, compact KV, accurate long-context retrieval. **HySparse2** adds two-level KV sharing: outer level — YOCO-style self/cross-decoder with KV Bridging, but bridges only full-attention layers (self-decoder: hybrid SWA; cross-decoder: hybrid sparse attention); inner level — token-level (not block-level) sparsity + a forced recent-token sliding window inside sparse selection. All cross-decoder KVs derive from self-decoder hidden states → **prefill can exit after the self-decoder**, skipping all cross-decoder layers. |
| **Key Innovations** | (1) Trimmed-YOCO structure that makes cross-decoder KV construction free (shared from self-decoder); (2) token-level sparse long-context retrieval refinement over HySparse; (3) on an 80B-A3B MoE: beats HySparse + hybrid SWA on long-context retrieval and multi-turn agentic tasks with substantially reduced prefill compute and KV storage. |
| **Link** | [arXiv:2609.26368](https://arxiv.org/abs/2609.26368) |

### 4.4 Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Quan Nguyen-Tri, Mukul Ranjan, Zhiqiang Shen |
| **Institution** | VILA-Lab lineage (inferred; Zhiqiang Shen — MBZUAI-affiliated VILA) |
| **Published** | 22 Sep 2026 (cs.CL) |
| **Abstract** | Diffusion LLMs (dLLMs) enable non-autoregressive generation but deployment is limited by missing KV caching + parallel decoding that overlook the I/O bottleneck when combined. **Flash-dLLM**: identifies GPU memory I/O as the dominant bottleneck in KV-cache-enabled dLLM inference and fixes it with an IO-aware fused KV kernel; then a KV-cache-driven **draft-and-verify** scheme where the dLLM is both drafter and verifier (no auxiliary model). |
| **Key Innovations** | (1) First IO-centric acceleration for dLLMs (fused kernel addressing cache-reuse + verification memory traffic jointly); (2) self-speculative decoding — no extra draft model; (3) **5.1× (GSM8K) / 11.0× (HumanEval)** over prior SOTA Elastic-Cache while scaling to longer sequences/batches. |
| **Link** | [arXiv:2609.26796](https://arxiv.org/abs/2609.26796) |

### 4.5 Compressing Long Context into Answer-Aligned Memory Embeddings for LLM Inference

| Field | Detail |
|-------|--------|
| **Authors** | Md Mostafizer Rahman, Md Faizul Ibne Amin, Md Shahajada Mia, Yutaka Watanobe, Fang Liu |
| **Institution** | University of Aizu (inferred; Watanobe) |
| **Published** | 22 Sep 2026 (cs.CL) |
| **Abstract** | LLM inference is constrained by quadratic attention + linear KV growth. **CMC** (Context-to-Answer-Aligned Memory Compression) compresses long input contexts into compact **Context Memory Embeddings (CMEs)** aligned to *any frozen decoder's* embedding space — no decoder-weight modification. A two-tier KV cache combines question-guided CME selection with a local context window; the compressor trains under answer-targeted distillation from a frozen LLM. On 9 encoder-decoder combinations × 4 QA benchmarks: up to **+7.3 EM / +4.0 F1** on SQuAD, with 20% inference-time/energy and **50% peak GPU memory** reduction at 3,000-token generation. |
| **Key Innovations** | (1) Decoder-agnostic soft compression (CMEs align to a frozen decoder's space); (2) question-guided memory selection + answer-targeted supervision (vs unguided/generic compression); (3) arithmetic latency + memory wins with accuracy gains. |
| **Link** | [arXiv:2609.25537](https://arxiv.org/abs/2609.25537) |

---

## 5. Sequential Modeling, Time Series & Tabular FMs

### 5.1 TimeInteract: Towards Real-Time Interactive Intelligence for Streaming Time Series

| Field | Detail |
|-------|--------|
| **Authors** | Sheng Pan, Yongli Gu, Yiqing Guo, Warren Jin, Bo Du, Shirui Pan, Ming Jin |
| **Institution** | Griffith University / Monash (confirmed — Ming Jin, Shirui Pan, Griffith) |
| **Published** | 22 Sep 2026 (cs.LG) |
| **Abstract** | Existing time-series language models (TSLMs) are static: full-sequence offline processing, or a stream-then-respond alternation that prevents processing new observations *during* response generation. Proposes **Time-Series Interaction**: a model continuously perceives streaming observations and user intent, autonomously decides whether to stay silent or respond, and keeps consuming observations while responding. **TimeInteract**: dual-view streaming TS encoder (local variations + historical dynamics), a response-control gate, and decoupled streaming inference (control separated from response generation to avoid blocking). Built **StreamTSI-34K** (34,588 episodes / 77,505 responses, Understanding→Adaptivity hierarchy, single- and multi-turn). Outperforms LLMs/VLMs/TSLMs across all four interaction levels, **up to +23.92 points** on hard tasks, with near-zero stream stall and 2.15× inference speedup. |
| **Key Innovations** | (1) Defines a new regime (streaming *interactive* TS) with a capability hierarchy; (2) decoupled control-vs-generation inference so responses never block ingestion; (3) the first large streaming-TS interaction dataset (StreamTSI-34K) plus SOTA ablations. |
| **Link** | [arXiv:2609.26389](https://arxiv.org/abs/2609.26389) |

### 5.2 A JEPA Recipe for Tabular Foundation Models

| Field | Detail |
|-------|--------|
| **Authors** | Mingyu Jeon, Suwan Cho, Jae Young Suh |
| **Institution** | (inferred academic, KR) |
| **Published** | 22 Sep 2026 (cs.LG) |
| **Abstract** | Tabular FMs predict cell values in context; JEPA asks for prediction in *representation space* — but on a tabular-FM prior the latent (JEPA) term collapsed to a constant map in earlier runs. Reports a recipe under which the latent term survives beside the value objective: the value head reads the *encoder* field (not the predictor), and the target is an EMA difference. Controlled convergence-regime comparison (plateau rule, no fixed budget — a fixed horizon confounded a slowdown with a ceiling): **the JEPA arm trails the value-only arm** — 32:70 win/loss on classification, 8:24 regression across 147 datasets, at 1.42× steps / 1.66× wall-clock. |
| **Key Innovations** | (1) An honest negative-result recipe — where JEPA-style representation-space prediction survives but *does not pay* for tabular value prediction; (2) methodological cautionary tale (fixed-horizon ceilings vs plateau-rule evaluation); (3) the exact architectural/target changes (encoder-read value head, EMA-difference target) that stop tabular latent collapse. |
| **Link** | [arXiv:2609.25541](https://arxiv.org/abs/2609.25541) |

### 5.3 When Recursive Models Finish Computing

| Field | Detail |
|-------|--------|
| **Authors** | Hare Krishna, Shubham Singh, Stephen Ebert, Hao-Yu Sun |
| **Institution** | (inferred academic) |
| **Published** | 22 Sep 2026 (cs.LG) |
| **Abstract** | Recursive (recurrent/loop) models may keep updating latent state beyond nominal inference budget; a wrong answer at the budget is ambiguous — unfinished or persistently stuck? On 1,000 hard Sudoku with attention- and MLP-based Tiny Recursive Models: extending 16→512 steps raises exact-solve from 59.2%→87.5% (attention) and 74.4%→91.9% (MLP). Latent-state motion drops sharply after the first exact solution; completed states are **locally contractive along the trajectory** even while the same Jacobian retains expanding directions — **trajectory-conditioned anisotropic stability**. |
| **Key Innovations** | (1) Distinguishes nominal-budget failure from completed-but-wrong computation; (2) characterizes completion via directional stability of the local Jacobian; (3) evidence that fixed recursion budgets massively underuse recursive-model capacity. |
| **Link** | [arXiv:2609.26487](https://arxiv.org/abs/2609.26487) |

---

## 6. Multi-Agent Systems & Agent Reliability

### 6.1 Agensh: Scaling Organizational Intelligence to 1,024 Agents

| Field | Detail |
|-------|--------|
| **Authors** | Zhihao Zhan, Ting Song, Li Dong, Shaohan Huang, Jianxun Lian, Yan Xia, Furu Wei |
| **Institution** | Microsoft Research (confirmed lineage — Furu Wei / Li Dong) |
| **Published** | 22 Sep 2026 (cs.CL) |
| **Abstract** | Central orchestrators cap multi-agent scalability. **Agensh** is a self-organized harness with **no central orchestrator**: concurrent workers run a cooperation loop — gather context, claim/self-assign sub-tasks, act and share findings, verify, merge — over a shared workspace, message interface, and shared context (an "agentic organization" infra). On the five hardest ProgramBench tasks with GPT-5.6-sol(high): 1→128 agents raises mean final test-pass from 19.31%→28.78% (**≈+49% relative**); on pandoc, 1→1,024 agents raises 33.89%→55.06%. Self-organized cooperation styles emerge and standardize as the organization grows. |
| **Key Innovations** | (1) Demonstrates **number of agents as a scaling dimension** — concrete +49% test-pass from 1→128 agents, +21pp at 1,024, with a coordinator-free architecture; (2) the shared workspace/message/context infrastructure; (3) observed emergence+standardization of cooperation patterns at scale. |
| **Link** | [arXiv:2609.26781](https://arxiv.org/abs/2609.26781) |

### 6.2 Calibration Is Not Verification: Falsifiability-Aware Conformal Routing for Mixture-of-Agents

| Field | Detail |
|-------|--------|
| **Authors** | Nada Rahali, Zijia Wang, Zhisong Liu |
| **Institution** | (inferred academic) |
| **Published** | 22 Sep 2026 (cs.MA) |
| **Abstract** | Multi-agent systems treat agreement as evidence, but heterogeneous agents can jointly repeat unsupported claims or omit correct specialist facts. **C-MoA**: an agreement-based conformal filter turning inter-agent semantic support into a claim-level nonconformity score, calibrated at example level → distribution-free factuality control. Nearly doubles retained-claim precision on long-form generation (0.41→0.75), certifies a human-labelled medical set, transfers cross-domain without recalibration; fails only on short-form answering (consensus is cheap). **CONTRA-MoA** adds a blinded near-miss tournament + leave-one-agent-out stability + availability-aware fusion — helps only where the verifier holds domain knowledge (drops half of false medical claims at 0.940 precision; memory-only judge ⇒ signals near chance, AUC≈0.53). |
| **Key Innovations** | (1) Conformal (distribution-free) factuality control over *nonconformity-of-agreement*, transferable without recalibration; (2) sharp falsifiability result — counterfactual verification only pays when the verifier is knowledgeable; (3) failure-mode taxonomy (consensus-cheap short-form vs long-form). |
| **Link** | [arXiv:2609.25959](https://arxiv.org/abs/2609.25959) |

### 6.3 When Does Execution Provenance Help Agent Memory Retrieval?

| Field | Detail |
|-------|--------|
| **Authors** | Yiqi Wang, Jinqian Ju, Jiaqi Zhang, Zequn Sun, Yiqun Duan, Mingkai Zheng, Taotao Cai |
| **Institution** | (inferred academic) |
| **Published** | 22 Sep 2026 (cs.MA) |
| **Abstract** | Agent-memory retrieval is formulated as **budgeted evidence completion**: gold evidence may span several execution events, but conventional retrievers use fixed windows + fixed-k rewards that show whether the complete evidence set fits in context. Source-aligned provenance units are built from tool arguments/outputs; a zero-initialized residual R-GCN refines frozen dense-retrieval scores over typed provenance edges. On 2,000 span-grounded queries over 1,207 ISETrace trajectories: provenance units improve Full Support@2048 by **+19.07 points** over flat 512 windows, graph propagation adds +4.55 points, concentrated when evidence spans multiple events. |
| **Key Innovations** | (1) Reformulates agent-memory retrieval as budgeted evidence completion in shared source coordinates; (2) quantifies the flat-window granularity failure + fixes it with source-aligned provenance candidates; (3) controlled graph-propagation attribution (dimension: candidate design vs graph signal). |
| **Link** | [arXiv:2609.25913](https://arxiv.org/abs/2609.25913) |

### 6.4 How Strongly Should Task State Influence an LLM Agent?

| Field | Detail |
|-------|--------|
| **Authors** | Chenyu Zhang, Wonbin Kweon, Jiawei Han |
| **Institution** | UIUC (inferred; Jiawei Han) |
| **Published** | 22 Sep 2026 (cs.AI) |
| **Abstract** | Long-horizon task tracking: agent systems either keep state as text in the prompt or move it into an enforcing module — but no one knows how much reliability comes from state being *shown*, *told*, or *enforced*. Held fixed: task rules, model, paired episodes. Varying the state channel (raw transcript / exact checklist / per-turn directives from a state machine / enforcement gate) — key findings: showing accurate state is unreliable; **an unverified ledger the agent writes itself beats an accurate shown checklist**; directives help in proportion to model obedience; enforcement needs no obedience but is bounded by state/matcher correctness. On τ²-bench's airline policy the same gate raises a 235B agent pass¹ 0.39→0.54 (and does nothing for a 35B agent); on PM-Bench the ledger finding *reverses*. |
| **Key Innovations** | (1) Clean ablative isolation of state channels (show/tell/enforce) that most agent evals bundle together; (2) counterintuitive "self-written unverified ledger > accurate shown checklist"; (3) task-dependent reversals with actionable guidance on when enforcement pays vs hurts. |
| **Link** | [arXiv:2609.25686](https://arxiv.org/abs/2609.25686) |

### 6.5 FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents

| Field | Detail |
|-------|--------|
| **Authors** | Nikita Agarwal, Nivedit Jain |
| **Institution** | (inferred industrial) |
| **Published** | 22 Sep 2026 (cs.AI) |
| **Abstract** | Agents often *reach* a working solution then fail to deliver it consistently. **FIRE** studies runtime policies — targeted natural-language instructions and action denials applied by the harness at states that preceded observed failures (no weight changes, no prompt edits). On the full 87-task Terminal-Bench 2.1 suite (2 attempts/task): pass² rises 50.6%→54.0% (Luna), 55.2%→60.9% (Terra), 64.4%→73.6% (Sol) — best-of-two changes only +1.2 while repeated success +9.2 (policies convert reachable solutions into dependable delivery). A randomized five-arm experiment isolates the mechanism (61% with real policies vs 36–43% across shams). |
| **Key Innovations** | (1) Runtime policies as a *reliability* layer — capabilities already possessed made repeatable, at no deploy-time cost; (2) rigorous arm-based mechanism attribution (timing-matched sham, generic-reasoning controls); (3) cost lever: Terra-with-policy beats Sol-unassisted (71.4% vs 64.3%) at ~half cost. |
| **Link** | [arXiv:2609.26048](https://arxiv.org/abs/2609.26048) |

### 6.6 When Are Aggregate Agent Traces Diagnosable? Traffic-Governed Interpretation and Calibrated Abstention

| Field | Detail |
|-------|--------|
| **Authors** | Peiying Zhu, Sidi Chang |
| **Institution** | (inferred industrial/academic) |
| **Published** | 22 Sep 2026 (cs.AI) |
| **Abstract** | Runtime traces look transparent, but a closed-loop policy decides which states get visited and which failures become visible — a fault may leave no aggregate trace when the policy rarely visits affected cells. Proposes trace interpretation as a **diagnosability decision** preceding scoring/localization: a reference-map gate requires repeated clean-policy support; a matched runtime gate requires joint clean+current support; signal analysis runs only after both pass. On a simulated hotel-pricing agent: 55/72 (76.4%) regime-component units reference-admitted (20 physical components), 54/55 pass runtime admission (1 abstains), false admission 0/20. Traffic-based modeling (affected clean traffic vs nominal cell coverage) improves detection by 0.1264 nats/row (29.3%). |
| **Key Innovations** | (1) First-class *abstention* for aggregate trace interpretation — "the trace cannot support the claim ⇒ say nothing"; (2) exposure-then-score protocol with calibrated false-admission bounds; (3) traffic-governed (not coverage-based) fault modeling. |
| **Link** | [arXiv:2609.25806](https://arxiv.org/abs/2609.25806) |

---

## 7. Games, World Models & Multimodal

### 7.1 GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models

| Field | Detail |
|-------|--------|
| **Authors** | Zijun Lin, Zhiyang Deng, Yuzhe Wu, Bihan Wen, Yeying Jin |
| **Institution** | NTU Singapore (inferred; Bihan Wen) |
| **Published** | 22 Sep 2026 (cs.CV) |
| **Abstract** | Generative game world models simulate visuals but can't enforce *mechanics* (health, skills, combat rules, termination) — while game engines guarantee mechanics but limit player creation. **GameDirector**, the first agentic framework to decode rule-based gameplay logic from visual rendering: an intelligent director interprets observations, updates states, controls NPCs, enforces rules, and converts decisions into text prompts for the video world model. Players configure characters/states/rules like a game developer. On three games (data from an automated gameplay agent): accurate state tracking, reliable rule following, and **>39.9% better boss-action quality** vs end-to-end world models. |
| **Key Innovations** | (1) The gameplay-logic⇄rendering decoupling — the missing middle between hard-coded simulation and generative modeling; (2) agent-director rather than pixel-supervised state machines; (3) player-configurable rules with rule enforcement (closed-loop gameplay, not just open-ended rollout). |
| **Link** | [arXiv:2609.25652](https://arxiv.org/abs/2609.25652) |

### 7.2 TriWorldBench: A Tri-View Consistency Perspective on Embodied World Models

| Field | Detail |
|-------|--------|
| **Authors** | Xuanyi Liu, Haofeng Wang, Ruiqi Li, Danni Yu, Rui Wan, Ruixu Zhang, Siyu Tao, Xue Yang, Shaofeng Zhang, Zicheng Zhang, Jiaqi Zhang, Siwei Ma |
| **Institution** | Peking University (inferred; Siwei Ma) |
| **Published** | 22 Sep 2026 (cs.RO) |
| **Abstract** | Embodied (bimanual) world-model evaluation can't rely on single-view quality — head and wrist cameras must describe the *same* action/object state. **TriWorldBench** evaluates world models on synchronized head/left-wrist/right-wrist videos: 500 episodes across 50 bimanual manipulation tasks, 19 metrics (tri-view consistency, task alignment, physical/3D coherence, motion quality, temporal consistency, visual quality). Cross-view checks catch predictions that are individually plausible but jointly inconsistent; TWB-Score summarizes; per-view results localize failures. |
| **Key Innovations** | (1) The first tri-view consistency benchmark for embodied world models (bimanual, multi-camera); (2) 19 metrics + full data/code release; (3) "consistent prediction of the *intended task*" as the evaluation standard, not single-stream realism. |
| **Link** | [arXiv:2609.26314](https://arxiv.org/abs/2609.26314) |

### 7.3 Dual-Frontier: When Can an Agent Trust Its World Model?

| Field | Detail |
|-------|--------|
| **Authors** | Huatai Zhu, Qiang Chen, Ziqian Kou, Wenhao Li, Fei Wang, Yichao Cao, Xiu Su, Yi Chen |
| **Institution** | (inferred academic) |
| **Published** | 22 Sep 2026 (cs.AI) |
| **Abstract** | When a world-model-guided decision fails, trajectory alone can't say whether the decision rule or the world model caused the loss. Formalizes **failure attribution as counterfactual return decomposition** and proves the components are **not identifiable from passive interaction** even for finite-horizon planners. **Dual-Frontier**: admit a world-model-guided decision only when predicted advantage exceeds a certified bound on decision-relevant world-model error; otherwise allocate evidence to verification. Action-conditioned value bounds + closed-loop extension guarantee non-decreasing return for admitted decisions. |
| **Key Innovations** | (1) An identifiability theorem for model-vs-loss attribution in MBRL; (2) a verify-then-promote decision principle with a certified-bound admission criterion; (3) non-decreasing-return guarantee for admitted decisions plus tool-use benchmark instantiation. |
| **Link** | [arXiv:2609.26293](https://arxiv.org/abs/2609.26293) |

### 7.4 PERSONAWEAVER: Controllable Diversity Beyond Conventional Archetypes in Procedural Character Generation

| Field | Detail |
|-------|--------|
| **Authors** | Maan Qraitem, Kate Saenko, Bryan A. Plummer |
| **Institution** | Boston University (confirmed; Saenko/Plummer) |
| **Published** | 22 Sep 2026 (cs.CL) — 1st PANDORA Workshop (Pluralistic AI and NLP) |
| **Abstract** | LLM-driven procedural character generation produces behaviorally homogeneous populations — everyone agrees with positive moral norms and replies like an assistant. **PersonaWeaver** disentangles world building from behavioral specification, modeling behavior through general, diverse, manually curated banks of moral positions and conversational reactions. Across 10 realistic/fantastical settings × 3 LLMs: broader moral/interactional response distributions than prior work, diversified dialog language/length/sentiment, less archetypal combinations of world attributes. |
| **Key Innovations** | (1) Diagnoses and fixes the "all characters are helpful assistants" failure of LLM PCG; (2) world-building⇄behavior decoupling with reusable moral/reaction banks; (3) tests how far LLMs can push beyond default values — with controllable diversity. |
| **Link** | [arXiv:2609.26629](https://arxiv.org/abs/2609.26629) |

---

## 8. Interpretability, Evaluation & Security

### 8.1 Matryoshka Attribution: Learning to Attribute Language Model Outputs to Representations and Weights

| Field | Detail |
|-------|--------|
| **Authors** | Aryaman Arora, Kirill Acharya, Nathan Hu, Yanzhe Zhang, Noah Goodman, Dan Jurafsky, Christopher Potts |
| **Institution** | Stanford (confirmed; Arora/Jurafsky/Potts...) |
| **Published** | 22 Sep 2026 (cs.CL) |
| **Abstract** | Attribution = identify the *nested subsets* of internal components minimizing a downstream loss. **MAttr** learns this with a differentiable sigmoid top-k mask, supervising over all sparsities by randomizing k during training → a learned component ordering by attribution score. **#1 on the official Mechanistic Interpretability Benchmark leaderboard**, identifying sparse, task-transferrable circuits across varying bases. Applied via RL to attribute weight changes: restoring **1% of Llama 3.1 8B Instruct's weights** to base state is enough to remove refusals while retaining capabilities. |
| **Key Innovations** | (1) Attribution reframed as a *learnable nested-selection objective* (gradient-descent addressable); (2) #1 MI benchmark + circuit transfer across bases; (3) a concrete weight-attribution superpower: minuscule surgical weight restoration for capability-preserving refusal removal. |
| **Link** | [arXiv:2609.25518](https://arxiv.org/abs/2609.25518) |

### 8.2 Optimizing the Score, Losing Sight of the Task: Reward Hacking Across Weights, Selection, and Prompts

| Field | Detail |
|-------|--------|
| **Authors** | Vansh Wahi |
| **Institution** | (single author, inferred) |
| **Published** | 22 Sep 2026 (cs.AI) |
| **Abstract** | A higher eval score ≠ better system: optimization can exploit evaluator mistakes with progress decoupled from task performance. Builds a comparative framework across three optimization substrates — **weights, selection (inference-time), and prompts (in-context)** — founded on the Proxy Compression Hypothesis. Formalizes a distance-dependent upper bound on evaluator disagreement and a capacity ordering over nested policy classes; shows why distance alone can't rank vulnerability; an exact finite-output illustration shows how the *location* of a scoring defect changes which method wins; maps defensive mechanisms that transfer vs those that only resemble each other. |
| **Key Innovations** | (1) A unified formal treatment of reward hacking across the three optimization surfaces a modern system actually touches; (2) defense-transfer taxonomy distinguishing genuine vs analogical safeguards; (3) prompt-hacking highlighted as uniquely inspectable-but-unpredictable (small text ⇒ hard-to-anticipate behavior). |
| **Link** | [arXiv:2609.25848](https://arxiv.org/abs/2609.25848) |

### 8.3 Evaluating Coding Agents on Kernel Exploit Generation

| Field | Detail |
|-------|--------|
| **Authors** | Junyoung Jang, Gwanhyun Lee, Hwiwon Lee, Kyuheon Kim, Jongseong Kim, Jinho Jung, Lingming Zhang |
| **Institution** | UIUC / KAIST cluster (inferred; Lingming Zhang) |
| **Published** | 22 Sep 2026 (cs.AI) |
| **Abstract** | Bug discovery ≠ exploit primitive construction. **KEX-bench**: 45 task instances across 40 Linux/Windows CVEs covering kernel address leak, IP control, heap read/write, arbitrary-address write; each in an isolated VM with fixed tool budgets and a deterministic verifier. Without a reference PoC the strongest configuration solves 1/20 Windows (5.0%) and 14/25 Linux (56.0%); with PoC, 31/45 (68.9%). The gap: agents reach kernel crashes but fail to shape state into primitives. |
| **Key Innovations** | (1) First exploit-*primitive*-level (not just CVE-discovery) benchmark over real kernels with deterministic verification; (2) quantifies the crash→primitive gap (56.0% vs 5.0% on Windows); (3) public benchmark for reproducible AI-assisted exploitation research. |
| **Link** | [arXiv:2609.25591](https://arxiv.org/abs/2609.25591) |

---

## Summary of Key Trends

| Trend | Notable Papers |
|-------|---------------|
| **The rec/ads synthesis is now generative + CTR-rewarded** | KwaiMind (Kuaishou) closes the loop: CTR as an RL reward for commercial image editing (+2.44% online CTR), scored by Ecom-Bench — the natural next step after the generative-recommendation wave (HSTU/GRec lineage) |
| **LLM-user-simulator reliability is a real eval concern** | PQA (KAIST, CIKM'26) shows injected traits interfere + inflate satisfaction; Synthetic-consumers pretest (6 preregistered studies) shows ≤2/6 human effects reproduced — user/consumer simulation for rec & marketing eval needs calibration, not faith |
| **Test-time compute shifts from machinery to policy simplicity** | Hill Sampling (Oracle) beats elaborate evolution/test-time-training stacks; Concept-Search Policies (Paris-Saclay/NYU) make diversification *trainable*; repeated sampling keeps losing ground |
| **The design of the self-taught teacher is getting precise** | Privileged-context OPSD (abstraction level, not volume, matters), Ladders-of-Thought (self-evolving ladders), NB-LoRA (null-basis preservation) — three clean recipes for post-RL adaptation without capability erosion |
| **KV/serving research refines phase specialization** | CompKV (compensation-aware selection), HySparse2 (two-level KV sharing, prefill-exit), Disaggregated Quantization (prefill vs decode formats), Flash-dLLM (IO-aware dLLM caching) — all treat "cache/format per phase" as the first-class axis |
| **Fine-grained MoE hints at a "2/3" law** | 2/3-Experts (CAS): uniform 2/3 retention ≈ 98.8% preserved, dynamic pruning pays only at aggressive budgets; sub-expert PEFT (NSFT) refines granularity below the expert |
| **Multi-agent scaling + calibration mature in opposite directions** | Agensh (MSR): 1→128 agents = +49% test-pass, orchestrator-free; C-MoA: agreement-based *conformal* filters transferable without recalibration — with a sharp caveat that counterfactual verification needs a knowledgeable verifier |
| **Games & world models move from pixels to structure** | GameDirector (rules⇄rendering decoupling), TriWorldBench (tri-view consistency), Dual-Frontier (when to *trust* the model), PersonaWeaver (behavioral diversity) — 2026 Q3 game-AI dallies keep converging on "structure over generation" |
| **Interpretability gets surgical & agent security gets a benchmark** | MAttr (#1 MI benchmark; 1% weight restore removes refusals), KEX-bench (exploit-primitive eval vs crash-only coding agents), Reward-hacking-across-substrates unifies the threat model |
| **Sequential modeling turns interactive** | TimeInteract (streaming interactive TS, +23.9pts, 2.15×), CMC (decoder-agnostic context compression), LEMA (exact-match attention with constant per-token reverse simulation) |

(Runner-ups, grep-verified 0 hits: **2609.25570** CED — contrastive epistemic decoding against adversarial swarm consensus (LLM sycophancy mitigation); **2609.25647** Early-outcome prediction calibration audit for agent evaluation (leave-one-agent-out, target-specific transfer); **2609.25963** GeoPair — geometry-preserving cross-layer factorization for training-free transformer compression; **2609.25678** ToolCompass — guiding tool-trialing post-training (AppWorld/FTRL OOD gains); **2609.25853** MemoryAthena — adaptive routing over latent *and generated* memories; **2609.26488** Spoken LM think-aloud — asynchronous dual-stream spoken reasoning (SLT 2026).)

(End of file — total 37 papers / 8 sections)