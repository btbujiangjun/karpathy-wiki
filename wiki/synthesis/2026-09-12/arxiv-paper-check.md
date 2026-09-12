---
title: "arXiv Paper Check — AI & CTR (September 12, 2026)"
type: synthesis
created: 2026-09-12
updated: 2026-09-12
sources: [arxiv.org]
tags: [arxiv, daily-check, ai, ctr, recommendation, ads, agents, deep-research, reasoning, llm, efficiency, serving, scaling-law, learning-dynamics, daily-digest]
---

# arXiv Paper Check — AI & CTR (September 12, 2026)

> **Mailing**: Fri, 11 Sep 2026 (latest announcement; no Sat/Sun mailing — this is a *second pass* over the Sep 11 window).
> **Scan scope**: cs.AI (171 new), cs.IR (15 new), cs.LG (171 new).
> **Dedup**: Zero overlap with same-day-adjacent [[arxiv-paper-check]] (2026-09-11), [[arxiv-daily]] (2026-09-11), [[game-rl-daily]] (2026-09-11), [[conference-digest]] (2026-09-11) — all 16 featured IDs grep-verified 0 hits in `wiki/`.

## Summary

0 direct CTR papers in this window (all Sep-11-mailed CTR work was captured by the 09-11 digests). The window is instead strong on **agent evaluation** (deep-research/multimodal/scientific-reasoning benchmarks), **LLM serving efficiency** (KV-cache offload, power control, token-weighted training loss), and **reasoning post-training** (self-distillation, stability-aware TTA, an open IMO-gold recipe). 16 papers across 6 themes.

---

## ① Deep-Research & Scientific Reasoning Agents (3)

### Mr.LHDR: A Benchmark for Multimodal Real-World Long-Horizon Deep Research Agents
- **arXiv**: 2609.11318
- **Authors**: Minghao Guo, Meng Cao, Sui Zhao, Siyu Ning, Xin Wang, Haoze Zhao, Jiaxuan Yang, Haihong Hao, Mingfei Han, Shunlin Rong, Haijun Wu, Xiaodan Liang, Xiaojun Chang
- **Key contribution**: Benchmark over long, irreducible chains of interdependent evidence (hidden Node-Relation graphs) across 8 categories — avg. **12.1 necessary intermediate conclusions**, mean dependency depth **10.4**. Evidence is multimodal (images, maps, PDFs, logos, charts, tables, video frames); ≥1 non-text element changes the reasoning state. Strongest system only **43.1% OA / 34.3% SA**; stripping images drops DACS 12.6 pts; SA declines with chain length. Reports OA/SA/Checklist Score/Dependency-Aware Checklist Score (DACS).
- **Relevance**: Long-horizon multimodal reasoning is the clear gap for research/deep-research agents (cf. [[autoresearch]]). Pairs with Sci-MMR below as evidence-interdependency becomes the new eval frontier.

### Sci-MMR: Benchmarking Multi-Step Evidence-Grounded Scientific Reasoning in Multimodal Agents
- **arXiv**: 2609.11243
- **Authors**: Jiaqiang Li, Yajie Yang, Zhiheng Xi, Jiadong Chen, ... Lei Bai, Xingjun Ma, Tao Gui (18 authors)
- **Key contribution**: Checks whether multimodal-model answers are really supported by traceable evidence using structured argument graphs (claims → citation-grounded knowledge → visual evidence → supporting regions). 235 multi-hop tasks across 4 scientific disciplines, avg. 9 figure panels/task. Across 8 frontier multimodal models, **answer accuracy exceeds complete-evidence recovery by >20%** — models answer correctly without recovering evidence. Bottlenecks: evidence acquisition (57.2% of failures; cropping +4.5, gold evidence up to +37.0 pts) vs evidence integration (31.8%; strongest model 69.1% on hardest tasks even with gold evidence).
- **Relevance**: Diagnoses *why* multimodal agents fail — evidence halving/evaluation is a bigger lever than reasoning. Directly actionable for research-automation systems.

### Magenta: Closing the Loop Between Mathematical Reasoning and Lean Verification
- **arXiv**: 2609.11319
- **Authors**: Joshua Ong Jun Leang, Haonan Li, Zheng Zhao, Xinyi Shang, Wenda Li, Zhengzhong Liu, Erix Xing, Shay Cohen, Eleonora Giunchiglia
- **Key contribution**: Training-free agentic pipeline: outputs a natural-language answer → formalizes as a Lean 4 statement → constructs a machine-checked proof. A statement judge verifies the formalization preserves the original problem; an error-attribution judge routes failures to re-derivation or local Lean repair. **100% on AIME 2025 / AIME 2026 / HMMT Feb 2026**; with open-weight K2-Horizon-7B reasoner, solves all six **IMO 2026** problems. Statement adjudication is essential to prevent false certificates; feedback-guided correction beats independent resampling.
- **Relevance**: Formal verification as a closed training-free loop — the verification-first paradigm Karpathy advocates in [[verifiability]] / [[software-3-0]].

---

## ② Agent Systems, Reliability & Web Access (3)

### The Agent Incident Registry: Toward Preventing Repeated AI Agent Failures
- **arXiv**: 2609.11030
- **Authors**: Divyanshu Kumar, Rohith HN, Nitin Aravind Birur, Sahil Agarwal, Prashanth Harshangi
- **Key contribution**: AIR = source-linked catalog of agent-incident records with stable IDs and missingness-aware labels (causal role, disclosure class, mechanism, outcome). Double-reviewer validated. Deployment-analogue audit: InjecAgent covers 3 of 12 incident surfaces (all attacker-triggered) vs AIR's no-adversary safety failures. Explicitly supports case retrieval and eval-scope auditing, **not** failure-rate estimation.
- **Relevance**: Incident-registry thinking for agents mirrors supply-chain/SOC practice; complements the wiki's [[supply-chain-attacks]] and safety-evaluation material.

### Memory Compression for High-Fanout Agent Sandboxes (AgentZip)
- **arXiv**: 2609.11294
- **Authors**: Mengming Li, Ceyu Xu, Qijun Zhang, Jiangnan Yu, Xiangfeng Sun, Haohui Mai, Zhiyao Xie
- **Key contribution**: First memory compression system for AI-agent sandboxes: exploits template-relative and cross-sandbox redundancy; broadens compression to any profitable page; shifts overhead control from compress-time page selection to restore-time prefetching; aligns expensive compression with LLM waiting periods. Up to **8.7×** sandbox-owned memory reduction (Linux config: 2.1×). Prefetching + agent-aware scheduling cut aggressive-compression slowdown from 3.1× to **1.40×** while keeping memory savings.
- **Relevance**: Agent sandbox memory is a real infra bottleneck for high-fanout agent platforms (Karpathy's agent-era infra interests).

### terms.txt: A Consent and Compensation Protocol for Agentic Web Access
- **arXiv**: 2609.11152
- **Authors**: Rajarshi Chowdhury
- **Key contribution**: robots.txt-style `terms.txt` specifying per-path, per-purpose machine-access terms, plus origin-enforced exchange via Web Bot Auth signatures, signed intent, delegation tokens, HTTP 402 negotiation, and signed receipts. Motivated by measurements showing automated clients now compose most web requests and training dominates Cloudflare-classified crawling. Dependency-free, **+0.20–0.65 ms/request** on one vCPU.
- **Relevance**: A concrete proposal for the web-access/robots gap in the LLM-crawling era — relates to [[model-collapse]] data-hygiene discussions.

---

## ③ LLM Efficiency & Serving (3)

### Building py-kvcache: External KV Caching for vLLM with NVMe SSDs
- **arXiv**: 2609.11744
- **Authors**: Joseph Kanichai, Tiziano De Matteis, Animesh Trivedi
- **Key contribution**: Characterizes prefix-cache TTFT tradeoffs across GPU/CPU/NVMe tiers; shows cache performance depends on transfer granularity, intermediate memory, and scheduling — not just device bandwidth. `py-kvcache` = vLLM KV-offload connector with async direct I/O, bounded shared staging, scheduler-aware preloading. At 80K tokens, disk loading **2.0× faster than LMCache**; GPU+CPU+disk **1.23× vs LMCache and ~4% of native vLLM KV Offload**. Caveat: on H100 with Bailian traces, average requests fall below break-even — external KV caching should be an **admission decision per setup**.
- **Relevance**: KV offload economics matter for serving cost; the preloading insight generalizes to any tiered-memory LLM server.

### Rebalancing Token Importance in LLMs with TF-IDF Weighted Cross-Entropy Loss
- **arXiv**: 2609.11029
- **Authors**: Zhijian Li, Stefan Larson, Kevin Leach
- **Key contribution**: Information-weighted CE rescales token-level loss by TF-IDF, down-weighting ubiquitous tokens. Across five decoder-only LLMs (1.1B–13B): consistent reduction in memorized-substring length while preserving perplexity and downstream performance. LoRA fine-tuning: **avg −14% substring memorization**; full fine-tuning on TinyLLaMA 1.1B: **−58%**. Architecture-agnostic, <3% compute overhead.
- **Relevance**: Cheap training-time lever against memorization and (indirectly) rehearsal-based collapse — Ei. relevant to [[model-collapse]] and data-quality debates.

### Phase-Decoupled, Model-Calibrated Power Control for Disaggregated LLM Serving
- **arXiv**: 2609.11133
- **Authors**: Jae Gon Kim, Donghoon Yoo, Hanyul Ryu, Sungho Ha, Juyeon Lee, Soojung Ryu
- **Key contribution**: On disaggregated B200, NVIDIA Max-Q gains only +8.6% tokens/J with +5.2% latency cost and misapplies one setting to prefill/decode lanes in opposite hardware regimes. Proposes phase-decoupled controller: prefill lane under SM-clock window (latency-guaranteed floor), decode lane under auto-calibrated power cap just above a throughput/latency cliff. On 8×B200 serving Qwen3-Coder-480B (FP8): balanced mode **+20.4% tokens/J at +3.5% e2e** (Pareto-dominates Max-Q). Qwen3-235B-A22B (NVFP4) meets ITL-p99 in every repetition. **32.3% electricity saved** on a lane pair over 3 days. Scoped to MoE serving.
- **Relevance**: Production energy efficiency for MoE inference — a concrete serving-cost lever given data-center power pressure.

---

## ④ Reasoning & Post-Training (3)

### An Open Recipe for IMO Gold: Training Nemotron for Olympiad Mathematics
- **arXiv**: 2609.10712
- **Authors**: Ivan Moshkov, Stephen Ge, George Armstrong, Wei Du, Sadegh Mahdavi, Igor Gitman (NVIDIA)
- **Key contribution**: Post-training + test-time recipe for natural-language proof generation from Nemotron 3 Ultra: two specialist checkpoints (SFT + RL), iterative generate/verify/refine with a third checkpoint, plus a high-compute final-selection stage. Purely natural language — no formal prover, tools, or internet. **IMO 2026: 30/42 — reaches gold-medal threshold.** Releases checkpoints, training data, code, submitted solutions, and Nemotron-IMO-Bench (200 novel olympiad problems).
- **Relevance**: Open, verifiable-reward math RL recipe — a strong reference for [[rlvr]]-style pipelines; the closest open analogue to front-runner closed systems.

### Negative Self-Distillation: Learning to Reason by Avoiding Flaws
- **arXiv**: 2609.11699
- **Authors**: Rongcan Pei, Zhepei Wei, Shuyao Xu, Xinyu Zhu, Wei-Lin Chen, Yu Meng
- **Key contribution**: Argues On-Policy Self-Distillation (OPSD) degrades complex reasoning by imitation of artificially confident, privileged-information-conditioned traces, suppressing uncertainty and self-correction. NSD instead builds a question-specific *negative* teacher (e.g. "careless reasoner") and pushes the student *away* from it, gated dynamically to preserve linguistic priors on non-critical tokens. Consistently beats OPSD and other label-free self-bootstrapping RL baselines.
- **Relevance**: Directly challenges the "imitate your own traces" trend (cf. 09-11 on-policy distillation papers); evidence that *repulsion*, not imitation, can drive reasoning self-improvement.

### Beyond Confidence: Stability-Aware Test-Time Adaptation for LLM Reasoning (TASCO)
- **arXiv**: 2609.11393
- **Authors**: Bincheng Gu, Min Gao, Zongwei Wang, Yibing Bai, Yulan He, Junliang Yu
- **Key contribution**: Observation — high-confidence reasoning is more likely correct when confidence stays *stable under local perturbation*. TASCO keeps the LLM frozen and optimizes a lightweight task-level prefix under two perturbations: Random Perturbation (distributional stability) and Sharpness-Aware Perturbation (worst-case sensitivity). Improves reasoning accuracy and token efficiency across models/benchmarks while keeping confidence calibrated (no premature concentration).
- **Relevance**: Test-time adaptation without touching weights — a cheap, deployment-friendly reasoning boost.

---

## ⑤ Ads / Marketing / CTR-Adjacent (2)

### Generative Marketing Mix Modeling: Causal Inference Linking GEO and GEM to Business Impact
- **arXiv**: 2609.11915
- **Authors**: Masahiro Kato, Daiki Honma, Taka Kato
- **Key contribution**: Extends Marketing Mix Modeling to generative platforms: for GEO (generative engine optimization) it combines repeated generated answers, question counts, and share-of-use across generative systems, plus notice probabilities; for GEM (generative engine marketing) it combines sponsored-placement records with notice probabilities. Estimates expected business responses under counterfactual treatment sequences and establishes sufficient identification conditions. Evaluated on simulated product-recommendation answers (EN + JA).
- **Relevance**: The ad-measurement question for the LLM/agentic-search era — how 广告 spend on generative answers maps to business outcomes. Directly CTR/ads-adjacent.

### General Quantification of Covariate and Concept Shifts
- **arXiv**: 2609.11918 (ICML 2026)
- **Authors**: Hongbo Chen, Li Charlie Xia
- **Key contribution**: Shows the standard concept-shift definition breaks when source/target supports mismatch. Using entropic optimal transport, proposes **γ\*-concept shifts** and a general error bound unifying covariate and concept shifts for broad losses, label spaces, and stochastic labeling; shift estimators come with concentration guarantees; the **DataShifts** algorithm quantifies shifts and estimates the error bound.
- **Relevance**: The theory behind offline-vs-online ranking drift — supports CTR/rec robustness analysis when user/feature distributions shift between train and serve.

---

## ⑥ Scaling Laws & Learning Dynamics (2)

### Quantifying the Memorization-to-Generalization Transition: Scaling Laws and Phase Structure in Grokking
- **arXiv**: 2609.10657
- **Authors**: Anish Kataria
- **Key contribution**: Maps the memorization→generalization boundary across 384 configs (two-hidden-layer MLPs, modular arithmetic). Fits power-law scaling for generalization onset: **T_grok ∝ H^−0.27 · D^−2.04 · η^−0.50 · λ^−0.64** (R²=0.732; 0.821 with interactions). *Data complexity dominates over model capacity*: doubling data ≈4× faster generalization, doubling width only ≈1.2×. Sharp phase boundary at weight decay λ ≳ 1.0; weight-norm compression during transition supports implicit-regularization reading.
- **Relevance**: Data > capacity for fast generalization — a vivid scaling-law counterpart to CTR scaling-law work ([[concepts#scaling-law]] theme); reinforces the data-quality emphasis seen across this wiki.

---

## Key Trends

1. **Evidence-grounded agent evaluation is the new bottleneck** (Mr.LHDR, Sci-MMR): frontier agents answer correctly but fail to recover/report full evidence chains; multimodal long-horizon cascades stay stubbornly hard (43% OA best).
2. **Formal verification closes the reasoning loop** (Magenta, Nemotron IMO): training-free Lean pipelines and open natural-language proof recipes both hit 100%/gold-level math — verification-first RL is maturing.
3. **Repulsion beats imitation in self-improvement** (NSD): the strongest post-training signal this window challenges the imitation-of-self-traces paradigm.
4. **Serving economics precision-tunes** (py-kvcache, phase-decoupled power, AgentZip): KV offload and power control are treated as admission/placement decisions, not blanket wins; memory compression aligns with LLM idle-wait periods.
5. **Web-access governance is being formalized** (terms.txt) as robots.txt-style consent meets compensation — relevant to the crawling/training economy debates.
6. **Memorization is a first-class objective** (TF-IDF CE, grokking scaling): both training-loss design and theory now target the memorize-vs-generalize tradeoff explicitly.

---

## CTR Note

Zero new direct CTR papers in this window (the Sep-11 have CADET/FAT/DeRes/LoopCTR/LENS remain the freshest CTR batch — [[arxiv-daily]] 2026-09-11). Closest CTR-adjacent work: **Generative Marketing Mix Modeling** (GEO/GEM spend → business impact, the ads-measurement analogue for agentic search) and **General Quantification of Covariate and Concept Shifts** (train→serve drift bounds that underpin ranking robustness).