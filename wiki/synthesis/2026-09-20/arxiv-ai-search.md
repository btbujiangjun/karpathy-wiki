---
title: "arXiv AI Research Paper Search Report"
type: synthesis
created: 2026-09-20
updated: 2026-09-20
sources: [arxiv.org]
tags: [arxiv, AI, LLM, architecture, sequence-mixing, attention, diffusion-LM, agents, long-horizon, agentic-rl, multi-agent, profiling, serializability, tool-hallucination, confidence, reasoning, safety, alignment, personalization, mechanism-design, contract-design, markets, forecasting, time-series, retrieval, daily-digest]
---

# arXiv AI Research Paper Search Report — 2026-09-20

Generated: 2026-09-20 (Sunday). **Weekend catch-up sweep of the Fri 18 Sep 2026 mailing** (Thu 17 Sep submissions; IDs **2609.19149–2609.20822**). arXiv announces nothing on weekends, so this report re-mines the Fri-18 window and features the **unclaimed AI/LLM/agents/economics/forecasting remainder** not taken by the 09-18 siblings (`arxiv-ai-search`, `arxiv-paper-check`, `game-rl-daily`, `conference-digest`, `tech-report-digest`) or the 09-19 siblings (`arxiv-paper-check`, `game-rl-daily`, `conference-digest`). All 34 curated IDs below were **grep-verified 0 hits in `wiki/`** and lie **outside every sibling-claimed ID set** for 09-18/09-19 at write time.

**Methodology**: The public arXiv API (`export.arxiv.org`) was reachable this window (used for shortlist abstract retrieval), while full ID coverage came from direct page fetches of `/list/{cat}/new` for **cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, cs.CY, cs.CV, cs.AR** (all announcing "Showing new listings for Friday, 18 September 2026"). **592 unique in-window IDs parsed**, of which **435 were unclaimed** after the 09-18/09-19 siblings; ~200 titles keyword-screened, ~40 abstracts fetched, **24 papers featured in full + 10 runner-ups**. Probe HTML and API XML cached under the pre-approved temp dir `/var/folders/q9/tsl_tl5548x7j892sgt3qvlc0000gn/T/opencode/arxiv-search/` and cleaned up after the report landed. Institutions are author-affiliation inferred where not printed on arXiv (marked *tentative*).

> **Dedup note**: Same-day/window siblings (`arxiv-paper-check` 09-18 & 09-19, `game-rl-daily` 09-19) already claimed the agentic-RL cluster (Reach-or-Solve 2609.19636, UnifiedPlayers 2609.20089, BATON 2609.19830, SoL-Pi 2609.20519) and the game/world-model content. Those sets are **not re-featured** here; the featured set is the genre-diverse remainder below.

## Summary Statistics

| Scope | Value |
|---|---|
| Window covered | Fri 18 Sep 2026 mailing (Thu 17 Sep submissions); IDs 2609.19149–2609.20822 |
| Categories parsed | cs.AI, cs.LG, cs.IR, cs.CL, cs.GT, cs.MA, cs.NE, cs.CY, cs.CV (+ cs.AR shortlist) |
| Unique IDs parsed | 592 (435 unclaimed after 09-18/09-19 siblings) |
| Featured in full in this report | 24 papers (5 sections) + 10 shortlisted runner-ups |
| Direct advertising / CTR-ML / ranker papers | **0** (7th consecutive window at the daily layer; the rec/e-commerce relevance lives in agent-mediated commerce: personalization study 20077, GUI-agent nudge audit 19843, resume-screening prompt-injection 20188) |
| Dedup | All 34 curated IDs grep-verified 0 hits in `wiki/` + absent from sibling 09-18/09-19 claimed sets |

**Theme of the window**: the unclaimed Fri-18 remainder is dominated by **long-horizon agent engineering** (a Level/Tick/Cascaded architecture from a 10-day campaign, semantic profile-based observability, database-style serializability for agentic transactions, "when more is less" for multi-agent), **attention/architecture science** (Latin-square mixed-mixer stacks showing homogeneity is the real penalty, a hybrid AR+diffusion LM, a "language model knows when to recall" local-first decoder, diagonal attention sparsity in visual AR), **calibration & confidence discipline** (preregistered CoT-entropy reproduction, training-free self-reported confidence, retrieval-dominated QA negatives), and an **economics/mechanism-design cluster** (contract design, taxation under agent delegation, the organization of inference, financially-agentic-security SoK). Games content was fully claimed by 09-19 game-rl-daily; no new game-AI paper remains for this layer.

---

## 1 LLM Architecture, Attention & Sequence Mixing

### 1.1 The Latin Square as a Provably-Balanced Mixed-Mixer Stack (2609.20269)
- **Title**: Placement Is Free, Composition Is Not: The Latin Square as a Provably-Balanced Construction for Heterogeneous Sequence-Mixer Stacks
- **Authors**: Taebong Kim, Youngsik Hong, Minsik Kim, Sunyoung Choi, Jaewon Jang, Minseo Kim
- **Institution**: — (Korean academy/industry; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing; submitted 29 Jul 2026)
- **arXiv**: https://arxiv.org/abs/2609.20269
- **Abstract**: Since GPT, most Transformers repeat the same attention mechanism at every layer, yet this is largely convention rather than a tested conclusion. Introducing **Aether-7B-5Attn**, a 6.59B-parameter (≈2.98B active) mixture-of-experts model whose 49 layers contain **seven sequence-mixing mechanisms arranged as a 7×7 Latin square** — each mechanism appears exactly once per row and column, guaranteeing balanced exposure across depth and eliminating placement confounds. A parameter-matched 4×4-Latin-square proxy (700.9M params, eight seeds per arm) reveals a clean dissociation: rearranging a distributed heterogeneous stack into a balanced periodic cycle changes validation loss by only **0.16%** (placement is nearly free), while clustering the same mechanisms into contiguous depth bands costs **0.59%** and replacing the heterogeneous stack with a homogeneous one costs **1.68%**. At 2.16× larger scale (1.514B), the homogeneous-stack penalty grows to **2.63%** and removing the SSM-family mechanism causes **3.20%** degradation. Performance depends mainly on **heterogeneous composition distributed across depth**, not on any particular permutation.
- **Key Innovations**: (1) Latin-square construction as a placement-confound-free experimental design for mixed-mixer models; (2) the "placement is free, composition is not" dissociation with per-mechanism cost profiles; (3) open weights/training code (49-layer causal-safety audit included) — the attack on the homogenous-stack convention is now driven by a deliberate architecture.
- **Venue**: Preprint (cs.LG).

### 1.2 Zarya — Hybrid Autoregressive–Masked Diffusion LM (2609.19868)
- **Title**: Zarya: A Hybrid Autoregressive--Masked Diffusion Language Model with Flexible Training and Dual-Mode Inference
- **Authors**: Leonid Sinev, Ilya Koziev, Vladislav Leshchuk
- **Institution**: — (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19868
- **Abstract**: ARMs are constrained to sequential left-to-right generation, while masked diffusion models (MDMs) enable parallel decoding but pay high compute overhead — no KV-cache reuse — plus incoherent generation from learning over the intractable space of token combinations. **Zarya** jointly optimizes an AR objective and a masked-diffusion objective in a **single architecture**: training data is structured into variable-size *slots* with a curriculum that gradually increases slot granularity (smooth transition from fine-grained AR learning to coarse-grained diffusion learning). Inference offers two decoupled paradigms through a unified interface: (i) **MDM sampling with first-hitting denoising**, and (ii) **slotted speculative decoding** that interleaves inter-slot diffusion-based selection with intra-slot autoregressive infilling, achieving **full KV-cache reuse**. Training and inference regimes are fully decoupled — any trained config can be deployed in either mode. Grouped noise patterns (Prefix Completion, Fill-In-the-Prefix, Fill-In-the-Middle), ordered sampling schedules, and noise-permutation strategies enable flexible research. Models released at 0.6B / 1.7B / 4B.
- **Key Innovations**: (1) a single architecture jointly trained for AR and masked-diffusion objectives with a slot-granularity curriculum; (2) slotted speculative decoding recovering KV reuse for the diffusion path; (3) full train/infer decoupling → both decoding paradigms available from one checkpoint.
- **Venue**: Preprint (cs.CL).

### 1.3 On-Demand Attention — Local-First Decoding with a Learned Recall Head (2609.20734)
- **Title**: On-Demand Attention: Language Models Know When to Recall
- **Authors**: Haibo Feng, Ruiqi Liang, Hanyang Peng, Shiqi Yu
- **Institution**: — (Chinese academy; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20734
- **Abstract**: Full-attention decoding reads the entire growing history at every step regardless of its benefit to the next prediction, but reasoning/agentic workloads increasingly demand long-context efficiency. The paper shows a pretrained model's **decoding states already contain information predictive of that benefit, before the global read**. **On-Demand Attention (ODA)** is a local-first decoding method with a lightweight **recall head** that selectively invokes global attention as its predicted benefit changes during generation. ODA trains only the recall head — pretrained weights stay frozen and the complete historical KV cache remains available for future recall. GPU-side conditional execution is implemented in vLLM, converting reduced global reads into practical decoding speedups at long context lengths. Across Qwen and Gemma (incl. hybrid-attention backbones), selective recall recovers most of the performance lost under pure local attention while substantially reducing global reads.
- **Key Innovations**: (1) per-step *learned* global-attention invocation (recall-head only, weights frozen) rather than static sparsity or cache eviction; (2) "the model knows when to recall" — benefit prediction from pre-read decoding states; (3) vLLM conditional-execution implementation with measured long-context speedups.
- **Venue**: Preprint (cs.CL).

### 1.4 Diagonal Attention Sparsity in Autoregressive Image Generation (2609.19702)
- **Title**: Understanding and Exploiting Diagonal Attention Sparsity in Autoregressive Image Generation
- **Authors**: Daeun Kim, Junwha Hong, Changhun Oh, Yoonsung Kim, Yoonhyeong Lee, Jongse Park
- **Institution**: Seoul National University-aligned (Park; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19702
- **Abstract**: Autoregressive image generation is attractive to multimodal systems because it rides existing transformer/LLM serving infrastructure, but generating thousands of visual tokens per request makes decoding bottlenecked by **KV-cache accesses during attention**. Sparse attention has been extensively explored for text LLM inference, yet whether its sparsity assumptions transfer to autoregressive image generation was unknown. This is the **first systematic characterization of attention sparsity in visual AR generation** across diverse workloads and open models. Distinctive properties emerge: a pronounced **prefill–decode asymmetry**, strong concentration on prompt and local tokens, and a **unique diagonal attention sparsity pattern** arising from the spatial locality of visual tokens. A **diagonal-aware sparse attention** mechanism skips KV entries along the diagonal direction within a recent window, implemented on top of FlexGen + FlashAttention-2 with custom kernels: **up to 3.1× throughput and 1.19× latency improvement with <2% quality degradation** vs dense inference.
- **Key Innovations**: (1) first workload-scale sparsity characterization specific to visual AR generation (vs text-transfer assumptions); (2) identification of the diagonal/local-spatial sparsity signature; (3) a diagonal-aware kernel stack with measured serving gains.
- **Venue**: Preprint (cs.CV).

### 1.5 Next-Token Functional Estimation — Leave-a-Window-Out (2609.19529)
- **Title**: Next-token functional estimation
- **Authors**: Milind Nakul, Vidya Muthukumar, Ashwin Pananjady
- **Institution**: Georgia Tech-aligned (Muthukumar, Pananjady; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19529
- **Abstract**: Given the first *n* points of a sequence and the goal of estimating a functional of the unobserved final point and the empirical measure of the training points, classic **leave-one-out is inconsistent under temporal dependence**. Such next-token functionals include the *surprise probability* (probability the next token is novel), the tail probability of min-distance to training points, and the test error of a classifier trained on the observed points. The paper proposes a **leave-a-window-out estimator** that deletes a window of length τ after each index before forming the empirical measure (reducing to leave-one-out at τ=1). Under natural assumptions the error decays at a **parametric rate for any stationary β-mixing process admitting a Marton coupling**. A sharp **minimax lower bound** is given for estimating the surprise probability on mixing Markov chains. Simulations on Markov chains, moving-average, and autoregressive processes show success where leave-one-out and add-constant baselines fail.
- **Key Innovations**: (1) first parametric-rate estimator for next-token functionals under temporal dependence (windowed deletion); (2) minimax lower bound for surprise-probability estimation; (3) connects classical statistical validation theory to next-token evaluation practice.
- **Venue**: Preprint (stat.ML).

---

## 2 Long-Horizon Agents: Architecture, Serializability, Observability, Multi-Agent

### 2.1 An Architecture for Long-Horizon Agents — Levels, Ticks and Cascaded Intelligence (2609.19519)
- **Title**: An Architecture for Long-Horizon Agents: Levels, Ticks and Cascaded Intelligence
- **Authors**: Erik Nijkamp, Anurag Koul, Egor Pakhomov, Bo Pang
- **Institution**: industry research (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19519
- **Abstract**: A long-horizon agent is asked to carry out work spanning days or weeks — an operations remediation, a research programme — that **outlives any context window, any process, and any interval at which a person can attend**. The paper argues the agent must *run continually without forgetting before it can learn continually*, and that this ability lives in the harness around the model rather than in the model itself. Seven bottlenecks are derived from the long-horizon setting and answered with a hierarchical architecture: (i) **levels indexed by time scale**, each keeping a bounded file summarizing the level below; (ii) a **clocked tick** as the unit of autonomous action; (iii) **cascaded intelligence** — work escalates to a more capable model only after failing review. A ten-day campaign reproduced a published RL result with human attendance once a day: the agent **kept the thread across every context reset and session boundary**, operating knowledge written early changed later behaviour with no weight change, and the harness's existing checks are where a learner would enter the system.
- **Key Innovations**: (1) continual-before-continual-learning framing: harness (not model) is the substrate; (2) a concrete three-part design (time-scale levels, clocked tick, cascaded escalation); (3) a 10-day real-reproduction campaign as evaluation — direct continuation of the wiki's long-horizon-agent reliability line.
- **Venue**: Preprint (cs.AI).

### 2.2 When AI Agents Commit — Cognitive Serializability (2609.20261)
- **Title**: When AI Agents Commit: Cognitive Serializability Across Data, Evidence, Policy, and Authority
- **Authors**: Jun He, Deying Yu
- **Institution**: — (author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing; submitted 28 Jul 2026)
- **arXiv**: https://arxiv.org/abs/2609.20261
- **Abstract**: Autonomous agents derive concrete mutations from database reads, retrieved evidence, policy, beliefs, and delegated authority — inputs that **may change while reasoning is in progress**. Database isolation orders the submitted transaction; agentic transaction processing checks whether a proposal satisfies a contract; neither guarantees a common valid point for the mutation and its derivation inputs. Typed dependency tokens distinguish *content integrity* from *applicability*; trusted mediation captures the values exposed to reasoning. Under strict **Cognitive Serializability**, committed effects admit a serial order and a logical event at which every exposed value is unchanged. A weaker **Effect-Compatible Cognitive Admission** recertifies an effect against a simultaneously held current dependency vector and policy without claiming to serialize the original stochastic derivation. The **TCT** prototype combines immutable versioned executable definitions, registry-derived authority plans, sealed envelopes, guard-first commit transactions, co-committed receipts, idempotent finalization, and receipt-driven epistemic reconciliation. Results give serializability conditions plus an observational-equivalence boundary for zero-error soundness and positive progress; the falsification suite prevented all injected anomalies at **3.22 ms mean commit overhead**.
- **Key Innovations**: (1) recasts agent-derived mutations as a distributed-systems serializability problem with a knowledge-grounded isolation level; (2) typed dependency tokens separating content integrity from applicability; (3) a falsification suite with measured commit-latency overhead.
- **Venue**: Preprint (cs.AI).

### 2.3 AgentPProf — Semantic Profiling for Long-Horizon Agents (2609.20301)
- **Title**: AgentPProf: Semantic Profiler for Long Horizon AI Agents
- **Authors**: Yusheng Zheng, Chaokun Chang, Yu Mao, Tianyuan Wu, Yuxi Huang, Tao Ma, Wenan Mao, Shuyi Cheng, Andi Quinn, Wei Wang
- **Institution**: — (eunomia-bpf ecosystem; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing; submitted 14 Sep 2026)
- **arXiv**: https://arxiv.org/abs/2609.20301
- **Abstract**: To improve agent quality, safety, and cost, developers need to know where failures happen, what triggers unsafe effects, and which tasks consume budget — questions systems profiling answers for software by attributing resource use to responsible code paths. Agent observability tools today focus on per-execution debugging/tracing, not cross-run profiling: the responsible entities are **task intents** ("diagnose authentication", "compare branches") rather than code paths, and lack stable identifiers for aggregation. **AgentPProf** adapts profiling to trajectories via a **semantic operation stack model**: uniform operations represent all activities, operation stacks replace the runtime call stack (hierarchical attribution at any granularity), and **recursive operation segmentation** splits trajectories at task boundaries. Output is **pprof-compatible**, enabling flame-graph visualization and analysis. It reaches **0.764 B³ F1 vs human annotations on CodeTraceBench** and, on three problem-localization benchmarks, the profile raises MAP by up to 56% — at practical profiling cost.
- **Key Innovations**: (1) porting the pprof/flame-graph stack (systems profiling) to agent trajectories via semantic operation stacks; (2) recursive task-boundary segmentation as the analog of stack frames; (3) validated resource attribution + problem localization on real benchmarks (open source).
- **Venue**: Preprint (cs.AI).

### 2.4 Rethinking Multi-Agent Collaboration — When More Is Less (2609.19759)
- **Title**: Rethinking Multi-Agent Collaboration: When More Is Less
- **Authors**: Yishuo Yuan, Yibo Wu, Yihan Zhang, Minyuan Sun, Shenliang Li, Xinkai Ma, Yifan Li, Jiaheng Liu
- **Institution**: — (Chinese academy; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19759
- **Abstract**: As single-agent harnesses scale, multi-agent collaboration faces diminishing returns while incurring growing context overhead. The paper delineates the **capability boundaries of multi-agent vs single-agent**: multi-agent confers systematic benefits specifically in **long-horizon tasks with sparse dependencies**, while single-agent harnesses remain superior in tightly coupled, sequential workflows. **SAIGE** (Semantic-Aware Incremental Graph Evolution) models collaboration as a dynamically evolving graph — nodes are agent instances spawned on demand, edges encode semantic dependencies established via content-based retrieval. On long-horizon, complex-task benchmarks, SAIGE achieves a favorable **context-efficiency / task-performance trade-off**, and scaling the agent pool or deepening recursion does **not** consistently improve outcomes. The findings suggest multi-agent superiority is bounded by task structure rather than universal.
- **Key Innovations**: (1) a task-structure taxonomy separating where multi-agent wins and loses; (2) on-demand graph-spawned collaboration (SAIGE) minimizing context overhead; (3) negative evidence on naive agent-count/recursion scaling — the anti-"more is better" companion to 09-19's agent harness engineering.
- **Venue**: Preprint (cs.AI).

### 2.5 MAGS — Auto-Formalized Safety Guarantees for Agentic Code (2609.19391)
- **Title**: MAGS: Multi-agent Auto-formalization Guarantees Safety for Agentic Outputs
- **Authors**: Albert Wu, Nicholas Roberts, Tzu-Heng Huang, Haoran Lin, Gil Friedman, Sungjun Cho, Gabriel Orlanski, Frederic Sala
- **Institution**: University of Wisconsin–Madison-aligned (Sala; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19391
- **Abstract**: LLM coding agents now generate complex programs at a scale that makes human review impractical, and the standard defenses — fuzzing, static analysis, LLM-as-verifier — struggle to cover all edge cases. **MAGS** is a unified multi-agent framework that generates executable programs with formal safety guarantees, using **Dafny as a verification-aware intermediate representation**: it formalizes and freezes human-audited APIs and safety requirements, translates generated code into Dafny, **repairs violations using verifier feedback**, and compiles verified programs back into executable code. Evaluated on **100 CUDA kernels, 100 terminal scripts, and 20 robotic-arm tasks** (220 examples total): **100% success** in producing programs with non-trivial safety guarantees against frozen specifications. Independent evaluations show strong performance across all three domains, while revealing failures when the auto-formalized semantics do not fully capture target behavior.
- **Key Innovations**: (1) auto-formalization pipeline (human-audited API/spec → Dafny → verifier repair → compile) instead of hand-written verification; (2) multi-agent division of formalization/translation/repair labor; (3) 100% success across 220 heterogeneous examples with honest failure-mode disclosure.
- **Venue**: Preprint (cs.AI).

### 2.6 Do AI Agents Understand Computer Architecture? — AutoTuring (2609.19387)
- **Title**: Do AI Agents Understand Computer Architecture?
- **Authors**: Ambika Sharan, Grigory Chirkov, Soheil Abbasloo
- **Institution**: University of Toronto-aligned (Abbasloo; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19387
- **Abstract**: Agents are increasingly reported to design hardware, but such reports establish that a design improved — not *why*. An agent may be reasoning about the machine or searching competently over knobs whose meaning it never recovers; only the first transfers to the next architecture. Existing evaluations cannot tell the two apart because they vary the agent while holding the problem's framing fixed. **AutoTuring** does the opposite: it hands the same agent the same 15-dimensional accelerator space twice — once as *named architectural knobs with simulator counters*, once as *anonymous [0,1] variables* — with the evaluator, legal space, and reachable optima held identical. On a nine-kernel FP16 GEMM basket, **meaning pays**: the architect beats a modeled H200 by 5.4% and its blind counterpart by 12.3% on average, using 70.1% fewer simulator calls. It does **not** pay uniquely: a critic loop recovers most of that gap for the blind agent and buys the architect nothing — architectural knowledge and structured critique behave as substitutes, not complements. Reported as preliminary (5–6 runs/condition).
- **Key Innovations**: (1) an AB (named vs anonymized) eval design that isolates semantic understanding from value-search competence; (2) the knowledge/critique *substitutability* result; (3) a reusable template for measuring whether any agent "understands" its domain vs optimizes it.
- **Venue**: Preprint (cs.AI).

---

## 3 Reasoning Reliability, Confidence & Response Selection

### 3.1 Chain-of-Thought Entropy as a Reliability Signal — a Preregistered Reproduction (2609.19606)
- **Title**: Chain-of-Thought Entropy as a Reliability Signal: A Preregistered Reproduction
- **Authors**: Theodore O. Cochran
- **Institution**: — (independent; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19606
- **Abstract**: An independent, preregistered (OSF) reproduction of Zhao's 2026 finding that the **shape** of an LLM's chain-of-thought entropy trajectory predicts final-answer correctness while the **magnitude** of its total entropy drop does not — the magnitude half originally rested on a single 300-problem run. The reproduction crosses full GSM8K and MATH-500 with **four open-weight models including a reasoning-distilled model** the original didn't test. **The shape signal replicates**: on the anchor model, the accuracy gap between monotone and non-monotone chains is +9.6 pp (GSM8K) and +27.5 pp (MATH-500), while rank correlation of total entropy drop with correctness is −0.018 (GSM8K) vs +0.414 (MATH-500) — **the magnitude signal divides by setting**. On the reasoning-distilled model the binary shape signal fires too rarely to estimate, while a graded violation count stays predictive. Exploratory: final-step entropy alone beats the binary shape flag in all eight model-by-benchmark cells by ROC area.
- **Key Innovations**: (1) full-test-set-scale preregistered reproduction with seven documented protocol differences; (2) a map of settings where the magnitude signal holds and fails; (3) an upgraded exploitable signal (final-step entropy) — calibration-track material for the wiki's reasoning-reliability line.
- **Venue**: Preprint (cs.CL).

### 3.2 Training-Free Self-Reported Confidence — No Better than Calibrated Rhetoric (2609.20541)
- **Title**: An Analysis of Training-Free Self-Reported Confidence in Language Models
- **Authors**: Lukas Meyer, Sofia Rossi, Wei Chen, Thomas Laurent, Yiming Li
- **Institution**: — (academic; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20541
- **Abstract**: LLMs report a numeric confidence alongside content, but whether that report is more than calibrated rhetoric is unclear. Three training-free signals are analyzed on 100 TriviaQA questions across two model families: **direct verbalized confidence**, **post-hoc P(True)**, and **three-sample agreement**. Direct verbalization is a surprisingly strong baseline — after auditing benchmark errors it reaches **AUROC 0.956 / 0.937** for correctness prediction. Three-sample agreement is substantially weaker (0.765 / 0.790), and fixed interpolation with verbalized confidence gives no statistically reliable benefit. 4–9% of decisions flip at a 0.8 threshold when confidence is re-elicited with equivalent prompts (scores shift 0.043–0.084). **Self-consistency can amplify shared misconceptions**: four of nine errors from one model receive unanimous sample support. An exploratory audit of confidence-tagged biography claims finds only a modest confidence gap between supported and contradicted claims.
- **Key Innovations**: (1) direct comparison of the three dominant training-free signals on an error-audited benchmark; (2) demonstration that verbalized confidence dominates self-consistency (and interpolation adds nothing); (3) evidence that re-elicitation noise and correlated errors bound the practical ceiling of self-reports.
- **Venue**: Preprint (cs.CL).

### 3.3 Closed-World Resolution Against Tool Hallucination in LLM Agents (2609.19425)
- **Title**: Closed-World Resolution Against Tool Hallucination in LLM Agents
- **Authors**: Laxmipriya Ganesh Iyer
- **Institution**: — (independent; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19425
- **Abstract**: Tool-augmented agents fail in a way no tool-selection or security method addresses: **they call tools that do not exist and pass arguments no schema declares**. Selection and gating both presuppose the emitted call refers to a real tool — a hallucinated call is structurally not a decision any gate made, so no gate can reject it. This is primarily a measurement/benchmark study: a **five-class taxonomy of tool hallucination (H1–H5)** plus the **Resolution Rung**, a training-free closed-world resolver (registry membership + signature check) whose interest is *where it must sit*, not what it computes. Across ten hosted models and two invocation surfaces, **322 genuine hallucinations** were measured; fabricated-tool calls concentrate on the unconstrained raw-JSON surface (34 vs 3), and **model scale does not help** (a 675B model matches a 7–8B one). Extended to the Model Context Protocol (MCP), merging servers into one namespace creates surfaces a single registry cannot express (a second taxonomy, M1–M5): **154 hallucinations measured on the live MCP surface**, including from frontier models clean on the single-registry surface. Hallucinated-Tools Benchmark (HTB) released.
- **Key Innovations**: (1) tool hallucination posed as a structural blind spot of selection/gating, solved by resolver *placement*; (2) dual measurement (raw-JSON vs MCP) with scale-independence evidence; (3) the versioned HTB benchmark for comparable resolvers.
- **Venue**: Preprint (cs.AI).

---

## 4 Safety, Manipulation, and the Substrate of Interpretation

### 4.1 Safety Beyond the Interface — Latent-State Harm Detection (2609.19472)
- **Title**: Safety Beyond the Interface: Detecting Harm via Latent States in Large Language Models
- **Authors**: Alizishaan Khatri, Chiquita Prabhu, Omkar Neogi
- **Institution**: — (industry; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19472
- **Abstract**: External guardrail models remain blind to the model's internal workings, creating an assurance gap in resource-constrained, time-critical deployments where guardrail latency/compute overhead is prohibitive. The core question: **does the model already know when content is harmful?** Activations are extracted from LLaMA-3.1-8B and lightweight MLP probes (12.6M params) are trained to detect harmful prompts. On WildJailbreak, Beavertails, and AEGIS 2.0 the probes score **F1 99% / 83% / 84%**, competitive with guard models up to 1000× larger while cutting latency and compute costs.
- **Key Innovations**: (1) internal-state probes as a lightweight guardrail alternative to external models; (2) ~1000×-smaller-model parity on three harm benchmarks; (3) a latency-critical serving motivation — safety as a reading of the model's own knowledge.
- **Venue**: Preprint (cs.AI).

### 4.2 Dual-Process Nudge Susceptibility in LLM-Based GUI Agents (2609.19843)
- **Title**: A Dual-Process Perspective on Nudge Susceptibility in LLM-Based GUI Agents
- **Authors**: Haya Halimeh, Sascha Kaltenpoth, Kevin Bösch, Oliver Müller
- **Institution**: Paderborn University-aligned (Kaltenpoth, Müller; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19843
- **Abstract**: LLM-based GUI agents act on behalf of users in interfaces designed — and deliberately *steered* — for humans. In a randomized **online shopping experiment with 3,600 agents / 21,600 simulations across six frontier models from three providers**, agents are vulnerable to both automatic (Type 1) and reflective (Type 2) digital nudges. The reasoning configuration moderates effects in **opposing directions**: extended reasoning *reduces* susceptibility to automatic default nudges but *heightens* it to reflective social-influence nudges. **Extensive reasoning therefore did not make agents more robust — it redirected the route through which choice architecture takes effect**, with the redirection systematically structured by model scale. Positions interface design as a governance concern for organizations that delegate decisions to autonomous agents.
- **Key Innovations**: (1) first large-scale measurement of digital-nudge susceptibility in *acting* GUI agents (vs text-only LLM outputs); (2) the opposing Type1/Type2 moderation by reasoning configuration; (3) direct relevance to the wiki's AI-mediated-commerce and agent-governance tracks.
- **Venue**: Preprint (cs.AI).

### 4.3 Tailored to You — Longitudinal Effects of Personalising Language Models (2609.20077)
- **Title**: Tailored to you: longitudinal effects of personalising language models
- **Authors**: Canfer Akbulut, Justine Breuch, Arianna Manzini, Lujain Ibrahim, Matija Franklin, Roma Patel, Iason Gabriel, Kristian Lum, Laura Weidinger
- **Institution**: **Google DeepMind**-aligned (Gabriel, Lum, Weidinger, Ibrahim, Patel; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20077
- **Abstract**: Personalisation is framed as a mechanism to better serve diverse user needs, but the effects of *sustained* interaction with personalised models on perception and downstream behavior are poorly understood. **992 participants** completed daily advice-seeking interactions over **five days**, comparing a non-personalised baseline against **memory-based** (prior conversational history) and **survey-based** (pre-study intake) personalisation. Many changes over time are driven by repeated exposure rather than personalisation itself, but the personalised groups differed: **memory-based** participants engaged in **greater self-disclosure** and rated the model **less creepy**; **survey-based** participants reported **higher regret** about having shared personal information with the AI. Responsible-design implications for deployment of personalised AI are drawn.
- **Key Innovations**: (1) five-day longitudinal RCT of personalisation approaches (992 subjects) rather than single-session lab evals; (2) the memory-vs-survey trade-off (disclosure/trust vs privacy regret); (3) the personalisation-vs-repeated-exposure confound for future studies — rec/i-commerce-adjacent for the wiki.
- **Venue**: Preprint (cs.AI).

### 4.4 AUDITPLAN — Commit, Then Answer for Auditable Safety Alignment (2609.19325)
- **Title**: AUDITPLAN: Commit, Then Answer for Auditable Safety Alignment
- **Authors**: Sai Sri Pushpa Jampani, Kshitij Mishra, Asif Ekbal
- **Institution**: IIT Patna-aligned (Ekbal; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19325
- **Abstract**: Safety-tuning pipelines judge only the final answer, making it hard to distinguish robust refusal from blanket refusal on benign requests and from polished-but-unfaithful safety rationales. **AUDITPLAN** is a single-model **plan-then-answer** approach: the model first emits a compact structured **safety plan** (threat label, intended action, explicit constraints), then answers conditioned on it, enabling machine-checkable auditing while the plan stays hidden at deployment. Trained with SFT followed by RL with **FAITHGATE**, a reward-gating objective granting answer reward only when the safety plan is correct — discouraging safe-looking but unfaithful behavior. On Qwen2.5-3B-Instruct, FAITHGATE reduces **ASR 24.0%→11.6%**, loose rationales 1.0%→0.36%, and over-refusal 11.0%→2.0%, outperforming answer-only RL, free-form explanation, and weighted-sum structured rewards; trends hold on 1.5B/4B/7B variants.
- **Key Innovations**: (1) explicit internal commitments (plan-then-answer) as a trainable, auditable-alignment primitive vs answer-only judgment; (2) FAITHGATE reward-gating that couples plan correctness to answer reward; (3) robustness + auditability gains across four Qwen sizes.
- **Venue**: Preprint (cs.CR).

### 4.5 Xeno-Interpretability — the Alien Minds of LLMs (2609.20408)
- **Title**: Xeno-Interpretability: Investigating the Alien Minds of LLMs
- **Authors**: F. Pierucci, M. Bracale Syrnikov, M. Prandi, M. Galisai, F. Giarrusso, P. Bisconti
- **Institution**: — (Italian AI-safety research collective; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20408
- **Abstract**: LLMs are usually interpreted through concepts humans already possess (truthfulness, refusal, deception, personality…). This paper asks whether models may also represent distinctions for which **no adequate human concept exists** — *xeno-representations*. It argues the space of possible internal distinctions in an LLM is substantially larger than the space expressible via finite human descriptions, and that an internal representation may be **reproducibly located, geometrically characterized, causally manipulated, and linked to downstream behavior even when its semantic content cannot be adequately expressed in human terms**. An empirical programme for identifying xeno-representations is sketched. Implications for AI safety and multi-agent systems: model-native representations may propagate and stabilize across interacting agents while remaining only partially visible through human-readable communication.
- **Key Innovations**: (1) formalizes the interpretability blind spot (human-conceptual space vs model-native space); (2) separates experimental identification from semantic interpretation; (3) a research programme — timely counterpart to the wiki's mechanistic-interpretability track.
- **Venue**: Preprint (cs.CL).

---

## 5 Economics, Mechanism Design & Markets

### 5.1 SoK: Trading Agents or Market Crashers? — FARSIGHT (2609.19705)
- **Title**: SoK: Trading Agents or Market Crashers? Dissecting Robustness and Security Failures in Academic Financial LLM Trading Schemes
- **Authors**: Mengxiao Wang, Nitesh Saxena
- **Institution**: Texas A&M-aligned (Saxena; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.19705
- **Abstract**: Autonomous financial agents hold direct execution authority over real capital in an adversarial, reflexive market — a representative case of high-stakes agentic security that existing domain-agnostic agentic-AI studies overlook. **FARSIGHT** performs scheme-level evaluation on two axes: **robustness** under market turbulence (incl. flash-crash-like scenarios) and **security** against three attack classes — attacks on information sources, attacks on agents, and **agent-as-attacker** behavior. Applied to **15 academic schemes**: **80% fail at least one core robustness metric and 100% exhibit security vulnerabilities**. The two failure modes are inseparable — a small misjudgment can cascade into a market-wide crash on its own, while an adversary can deliberately trigger the same collapse at minimal cost.
- **Key Innovations**: (1) the first scheme-level SoK of academic financial-LLM trading agents with an attack taxonomy; (2) 15-scheme audit: robustness and security failure are jointly 100%+80%; (3) the "small misjudgment = market crash, cheaply triggerable" externality framing.
- **Venue**: Preprint (cs.CR).

### 5.2 Minimax-Optimal Online Contract Design (2609.20353)
- **Title**: Minimax-Optimal Online Contract Design with Unrestricted Bounded Contracts
- **Authors**: Rui Ai, David Simchi-Levi, Han Zhong
- **Institution**: MIT-aligned (Simchi-Levi; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20353
- **Abstract**: Repeated contract design when a principal observes outcomes but not the actions generating them, using **any** bounded outcome-contingent payment vector, with the agent's best response able to make expected profit *discontinuous* in payments. For every fixed m≥2 outcomes, **minimax regret over T rounds is order T^{m/(m+1)}** (up to log factors), with no smoothness or monotone-surplus assumption. The upper bound's key is an **effective-dimension reduction** — the benchmark can be normalized even when fixed tie-breaking is not shift-invariant, after which revealed preference yields a monotone response map in payment-difference coordinates; a Lipschitz-parametrized learner attains the rate using only observed outcome categories. The lower bound shows **each additional contractible outcome creates a precise, unavoidable increase** in learning cost.
- **Key Innovations**: (1) nonasymptotic minimax-optimal rates for online contract design with discontinuous payoffs and unrestricted action sets; (2) dimension-reduction via normalized benchmark + monotone response maps; (3) a clean scaling law of regret in the number of outcomes.
- **Venue**: Preprint (cs.LG).

### 5.3 Welfare-Opaque Income — Taxation under AI-Agent Delegation (2609.20425)
- **Title**: Welfare-Opaque Income: Taxation under AI-Agent Delegation
- **Authors**: Yukun Zhang, Kemu Xu, Yishen Chen
- **Institution**: — (Chinese academy; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20425
- **Abstract**: When an AI agent implements economically relevant choices through a rule hidden from the government, the agent's hidden preference-to-execution mapping creates **double unobservability**: the same observable tax-base response can carry different welfare consequences, making the income *welfare-opaque*. Tax-base statistics can coincide while reform welfare effects differ, even with identical mechanical welfare weights. An optimal-tax condition adds a **response-weighted execution wedge** to the familiar sufficient statistics: a higher marginal rate gains corrective benefit under local over-execution and cost under local under-execution. A controlled laboratory runs **4,500 model runs across five AI engines**: faithful delegation selects the score maximizer in essentially all runs; conflicted objectives produce heterogeneous responses (Claude largely preserves the score maximizer, GLM moves downward, GPT-mini/Qwen show lower-tail increases); engine ranking depends on which engine is included. Execution information is identified as a complement to conventional tax-base statistics.
- **Key Innovations**: (1) the double-unobservability / welfare-opaque-income construct for optimal taxation; (2) execution-wedge optimal-tax condition; (3) a 5-engine/4,500-run behavioral laboratory for agent delegation in economic choice.
- **Venue**: Preprint (cs.CY).

### 5.4 The Organization of Inference — Information, Resource Constraints, and AI Production (2609.20449)
- **Title**: The Organization of Inference: Information, Resource Constraints, and AI Production
- **Authors**: Yukun Zhang, Kemu Xu, Yishen Chen
- **Institution**: — (Chinese academy; author-inferred; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20449
- **Abstract**: The economic value of inference depends on how capacity and task information are distributed across stages of AI production. Controlled workflow experiments on verified software-engineering tasks, in two matched resource panels: **direct execution records 59.6% success at logical-token ceilings of 12,000 and 24,000**, while success under information-constrained planning rises from 36.2% to 51.2% as the ceiling grows — the planning disadvantage narrows by **15.0 pp**. In a strict read-only planning campaign, issue access raises success ~16 pp over issue-hidden planning at 12,000 tokens; vs direct execution, task-informed planning is ~10 pp lower at 12,000 tokens but shows a **29.6-point advantage at 24,000**. The planning workflow's binding rate falls from 46.2% to 0.8% under the higher ceiling, with downstream execution accounting for 89.9% of the increase in total use. **Scale sets capacity; workflow and information structure shape productive value.**
- **Key Innovations**: (1) inference as an organizational problem — resource distribution vs task information; (2) matched-panel controlled experiments isolating workflow (planning vs direct) from token ceilings; (3) interquantile evidence that planner+executor splits pay off mainly at scale.
- **Venue**: Preprint (cs.AI).

---

## 6 Forecasting & Time Series

### 6.1 QUALS — Corpus Equilibrium for Universal Forecasting (2609.20156)
- **Title**: QUALS: Corpus Equilibrium for Universal Forecasting via Pattern Quantization and Learnability Synchronization
- **Authors**: Yujie Li, Zezhi Shao, Chengqing Yu, Yisong Fu, Weijie Zhu, Yifan Du, Jilin Hu, Bin Yang, Yongjun Xu, Fei Wang
- **Institution**: CAS/ISCAS & academia-aligned (Xu, Bin Yang; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing)
- **arXiv**: https://arxiv.org/abs/2609.20156
- **Abstract**: Zero-shot forecasting foundation models are increasingly trained on massive corpora, but studies prioritize architecture while relying on naive sampling that fails to manage complex mixed data distributions. **QUALS** is a large-scale **time-series corpus equilibrium** framework that makes existing models reach superior performance with a small fraction of the original training data. Two mechanisms: a **pattern quantization** framework that systematically decodes heterogeneous patterns from mixed corpora via vector quantization and uniform binning; and a **learnability synchronization** framework that calibrates sampling weights across heterogeneous patterns, bridging the optimization gap between simple and complex motifs. Pre-training on QUALS consistently achieves superior zero-shot performance even under substantially reduced budgets.
- **Key Innovations**: (1) data-distribution engineering (not architecture) as the lever for TS foundation models; (2) quantized pattern decode + learnability-calibrated sampling; (3) superior zero-shot on reduced training budgets across benchmarks.
- **Venue**: Preprint (cs.LG).

### 6.2 When Does Retrieval Help Time-Series Forecasting? (2609.20193)
- **Title**: When Does Retrieval Help Time-Series Forecasting?
- **Authors**: Mert Onur Cakiroglu, Elham Buxton, Mehmet Dalkilic, Hasan Kurban
- **Institution**: Indiana University-aligned (Dalkilic, Kurban; tentative)
- **Date**: Announced 18 Sep 2026 (Fri mailing; submitted 29 Jul 2026)
- **arXiv**: https://arxiv.org/abs/2609.20193
- **Abstract**: Retrieval plug-ins supply a deep forecaster with information its lookback window cannot carry; published evaluations report consistent gains and each credits its own mechanism. The paper shows the benefit instead belongs to the **operating point: the relation between window length S and the dominant seasonal period L** — an axis the standard protocol never varies. At S=12, a simple control repeating the last observed period **beats the six standard backbones on four of seven benchmarks by 8–44% of MSE**, and beats the strongest plug-in on ETTm1 while matching it on ECL. The benefit boundary tracks the period (correlation +0.71), not the horizon (−0.23). A paired control with no phase to recover nearly erases the effect (phase starvation). Zero-shot pretraining does not escape it — a foundation model trails trained backbones by 22–50% on periodic benchmarks. Two interpretable statistics (trend test, staleness rate) predict per-cell benefit sign at 0.76 accuracy under leave-one-dataset-out.
- **Key Innovations**: (1) a regime map attributing retrieval gains to the S-vs-L operating point rather than to specific mechanisms; (2) the implication that simple periodic replication can dominate a six-backbone leaderboard; (3) two pre-deployment screening statistics predicting where retrieval will help.
- **Venue**: Preprint (cs.LG).

---

## Key Trends Across This Window

1. **"Placement is free, composition is not"** (2609.20269): the unclaimed remainder's most provocative architecture result — heterogeneous mixed-mixer stacks matter mainly *what* mixes across depth, not *where* it sits; homogeneity, not ordering, is the 1.7–2.6% penalty. Complements 09-17's SSM/attention-alternative papers with a controlled-design methodology.
2. **Long-horizon agent engineering matures from prompt-engineering to systems architecture** (2609.19519 Levels/Ticks/Cascaded 10-day campaign; 2609.20261 cognitive serializability with a 3.22 ms commit; 2609.20301 pprof-style semantic profiling; 2609.19759 "when more is less" task-structure boundaries; 2609.19391 auto-formalized Dafny safety; 2609.19387 understanding-vs-optimizing eval design): the reliability agenda now has *architecture, transactionality, observability, and evaluation* — a full systems stack for agents.
3. **Confidence & calibration discipline is converging on registered protocols** (2609.19606 preregistered CoT-entropy reproduction splitting shape from magnitude; 2609.20541 training-free self-report honesty audit; 2609.19942 runner-up on retrieval-dominated QA negatives): preregistration and error-auditing have become the norm for reliability claims in this window.
4. **The economics of AI agents is becoming an empirical field** (2609.19705 trading-agent SoK: 100% vulnerable; 2609.20425 welfare-opaque taxation with a 4,500-run multi-engine lab; 2609.20449 organization-of-inference panels; 2609.20353 contract-design regret rates): market/microeconomic externalities of agentic AI — collapse triggers, hidden delegation, workflow economics — now get controlled experiments.
5. **Ads/CTR/rec continues to live one layer up**: zero direct CTR/pCTR/rank-model papers for the 7th consecutive daily window; the e-commerce-relevant content here is *agent mediation* (2609.20077 personalisation RCT, 2609.19843 GUI-agent nudge audit, 2609.20188 resume-screen prompt injection). Classic tabular CTR ML remains at the conference-digest layer.

## ADS / CTR Coherence Check

This window contains **0 direct advertising / sponsored-search / CTR-ML / ranker papers** in the unclaimed Fri-18 remainder — consistent with the 09-16 → 09-19 daily-layer pattern (7th consecutive window). The e-commerce-adjacent entries are the mediating layer: DeepMind's longitudinal personalisation RCT (2609.20077), the Paderborn GUI-agent nudge-susceptibility shopping study (2609.19843), and the resume-screening indirect-prompt-injection benchmark (2609.20188, runner-up). No contradictions flagged vs the CTR-scaling landscape; today's entries are orthogonal to the 09-18 ad-retrieval (ANGLE) and 09-16 ads/auction coverage.

## Cross-Reference Index (Runner-Ups & Coordinates)

All runner-ups grep-verified 0 hits in `wiki/` and absent from sibling 09-18/09-19 claimed sets at write time:
- **2609.19502** Cairn — community reputation as collective memory for the agentic web (time-decayed Beta + confidence shrinkage reputation engine; Argonne/UChicago-aligned).
- **2609.19644** ScientistTwo — fully autonomous multi-agent scientific-discovery loop with simulated peer-review rebuttal, benchmarks vs ICLR/ICML/NeurIPS papers (Google-DeepMind-aligned).
- **2609.19607** DeltaSelect — budget-dollar A/B task selection for coding agents (19.5% of DeepSWE tasks track full-benchmark performance; $27.86 / 13 evals case study).
- **2609.20068** Marginal utility × matrix factorization × KV cache — a unified "retention is constrained utility maximization" information-economic framework with a geo-mining extraction demo (90% L1 accuracy at 2.62 ms).
- **2609.19394** Strategyproof aggregation in Euclidean spaces — coordinate-wise median is worst-case-optimal among continuous anonymous strategyproof mechanisms (rigidity + median optimality).
- **2609.19170** Regularized Emphatic TD — RETD stabilizes constant-stepsize off-policy dynamics (certified negative Lyapunov exponents, affine shift of ETD equilibrium).
- **2609.19942** Intrinsic sequence-likelihood confidence in retrieval-dominated extractive QA — two pre-specified negatives (distillation trigger + routing/abstention) fail when retrieval already recovers 92–99.8%.
- **2609.20543** LLM groups overstate consensus when replaying human Wason-group deliberations — 34–44 pp consensus gaps vs humans (Wason group winnowing / agent-sociology track).
- **2609.20614** Inference-engine fingerprinting attacks are practical — a misaligned model can fingerprint vLLM/SGLang locally from output tokens alone (to-the-bare-metal PoC chain; Harvard-aligned).
- **2609.20188** ResumeShield — channel separation + open benchmark for indirect prompt injection in AI hiring (defeat naive pipeline in 100% vs 0% of cases; OWASP LLM01).
- **2609.19887** Generalization through lexical abstraction — functional words as centrally-located, distinct embeddings; mixed training reveals shared structure (Genova-aligned).
- **2609.20398** SALR — schema-anchored latent reasoning for SP-based KBQA (delays discrete schema commitment; +2.86 F1 on GrailQA compositional).
- **2609.19940** Stringological sequence prediction III — layered ziplines: a less expressive complexity measure admitting quasilinear-time/polylog-space prediction.